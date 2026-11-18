#!/usr/bin/env python3
"""Convert one HTML source file into PDF, DOCX, PPTX, XLSX or CSV.

HTML is the single source of truth. Each target uses one fixed pipeline:

  pdf   headless Chrome print (CSS @page controls size and margins)
  docx  LibreOffice Writer HTML import, export to Word 2007+
  pptx  Chrome prints one page per <section class="slide">, then
        LibreOffice imports the PDF into Impress and exports PPTX
  xlsx  every <table> becomes one sheet (pure stdlib writer)
  csv   every <table> becomes one CSV file (pure stdlib)

Only the Python standard library is required. PDF and PPTX need Chrome or
Chromium. DOCX and PPTX need LibreOffice (soffice).

Brand assets: any "brand://<path>" URL in the HTML resolves to the skill's
brand/ folder (logo, fonts, tokens.css). For DOCX and PPTX the brand fonts are
installed in the user font folder when missing, so LibreOffice can use them.

Usage:
  html2file.py INPUT.html --to pdf|docx|pptx|xlsx|csv [-o OUTPUT] [options]
"""

import argparse
import base64
import contextlib
import csv
import html
import mimetypes
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from html.parser import HTMLParser
from pathlib import Path

CHROME_CANDIDATES = [
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
    "chrome", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]
SOFFICE_CANDIDATES = [
    "soffice", "libreoffice",
    "/Applications/LibreOffice.app/Contents/MacOS/soffice",
]
BRAND_DIR = Path(__file__).resolve().parent.parent / "brand"
BRAND_FONTS = {
    "Bebas Neue": ["BebasNeue-Regular.ttf"],
    "Montserrat": ["Montserrat-Medium.ttf", "Montserrat-SemiBold.ttf", "Montserrat-Bold.ttf"],
}


def fail(msg):
    sys.exit(f"html2file: error: {msg}")


def find_binary(env_var, candidates, label):
    override = os.environ.get(env_var)
    if override:
        return override
    for name in candidates:
        path = shutil.which(name) or (name if os.path.isfile(name) else None)
        if path:
            return path
    fail(f"{label} not found. Install it or set {env_var}.")


def run(cmd, timeout=180):
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if proc.returncode != 0:
        fail(f"command failed ({proc.returncode}): {' '.join(cmd)}\n{proc.stderr.strip()}")
    return proc


# --- Source preparation ----------------------------------------------------

IMG_SRC_RE = re.compile(r'(<img\b[^>]*?\bsrc\s*=\s*)(["\'])(.*?)\2', re.I | re.S)


def inline_image(base: Path, url: str):
    """Return a data: URI for a local image URL, or None to keep the URL."""
    if url.startswith(("data:", "http:", "https:")):
        return None
    path = Path(url[7:]) if url.startswith("file://") else base / url
    if not path.is_file():
        return None
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


@contextlib.contextmanager
def prepared_source(src: Path, inline_images: bool):
    """Yield an HTML path with brand:// resolved and, for DOCX, images embedded.

    LibreOffice keeps file images as external links in DOCX; data: URIs are
    embedded. The temporary copy sits next to the source so relative paths work.
    """
    text = src.read_text(encoding="utf-8")
    new = text.replace("brand://", BRAND_DIR.as_uri() + "/")
    if inline_images:
        def repl(m):
            data = inline_image(src.parent, html.unescape(m.group(3)))
            return f"{m.group(1)}{m.group(2)}{data}{m.group(2)}" if data else m.group(0)
        new = IMG_SRC_RE.sub(repl, new)
    if new == text:
        yield src
        return
    tmp = src.with_name(f".{src.stem}.html2file.html")
    tmp.write_text(new, encoding="utf-8")
    try:
        yield tmp
    finally:
        tmp.unlink(missing_ok=True)


def ensure_brand_fonts():
    """Install the brand fonts for LibreOffice when the system lacks them."""
    if platform.system() == "Darwin":
        target = Path.home() / "Library/Fonts"
    elif shutil.which("fc-list"):
        target = Path.home() / ".local/share/fonts/orage-brand"
    else:
        return
    installed = ""
    if shutil.which("fc-list"):
        installed = subprocess.run(["fc-list", ":", "family"], capture_output=True,
                                   text=True).stdout
    missing = [f for fam, files in BRAND_FONTS.items() if fam not in installed
               for f in files if (BRAND_DIR / "fonts" / f).is_file()]
    if not missing:
        return
    target.mkdir(parents=True, exist_ok=True)
    for f in missing:
        shutil.copy2(BRAND_DIR / "fonts" / f, target / f)
    if shutil.which("fc-cache"):
        subprocess.run(["fc-cache", "-f", str(target)], capture_output=True)


# --- PDF -------------------------------------------------------------------

def chrome_pdf(src: Path, out: Path, wait_ms: int):
    chrome = find_binary("CHROME_BIN", CHROME_CANDIDATES, "Chrome/Chromium")
    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            chrome, "--headless=new", "--disable-gpu", "--no-first-run",
            "--no-default-browser-check", "--no-pdf-header-footer",
            "--run-all-compositor-stages-before-draw",
            f"--virtual-time-budget={wait_ms}",
            f"--user-data-dir={profile}",
            f"--print-to-pdf={out}",
            src.resolve().as_uri(),
        ]
        if os.environ.get("CHROME_NO_SANDBOX") == "1" or os.geteuid() == 0:
            cmd.insert(1, "--no-sandbox")
        run(cmd)
    if not out.exists() or out.stat().st_size == 0:
        fail("Chrome produced no PDF")


# --- LibreOffice -----------------------------------------------------------

def soffice_convert(src: Path, out: Path, infilter: str, convert_to: str):
    soffice = find_binary("SOFFICE_BIN", SOFFICE_CANDIDATES, "LibreOffice (soffice)")
    with tempfile.TemporaryDirectory() as tmp:
        # Separate profile so a running LibreOffice instance does not swallow the job.
        profile = Path(tmp, "profile").as_uri()
        outdir = Path(tmp, "out")
        run([
            soffice, f"-env:UserInstallation={profile}", "--headless",
            "--norestore", f"--infilter={infilter}",
            "--convert-to", convert_to, "--outdir", str(outdir), str(src.resolve()),
        ])
        produced = list(outdir.glob("*"))
        if not produced:
            fail(f"LibreOffice produced no output for {src}")
        shutil.move(str(produced[0]), out)


BODY_BGCOLOR_RE = re.compile(r'<body\b[^>]*\bbgcolor\s*=\s*["\']?#([0-9a-fA-F]{6})', re.I)


def set_docx_page_color(docx: Path, hex_color: str):
    """Give every page of the DOCX a background color (LibreOffice drops body bgcolor)."""
    tmp = docx.with_suffix(".tmp.docx")
    with zipfile.ZipFile(docx) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                text = re.sub(r"<w:background\b[^>]*/>", "", data.decode("utf-8"))
                text = re.sub(r"(<w:document\b[^>]*>)",
                              rf'\1<w:background w:color="{hex_color}"/>', text, count=1)
                data = text.encode("utf-8")
            elif item.filename == "word/settings.xml":
                text = data.decode("utf-8")
                if "displayBackgroundShape" not in text:
                    text = re.sub(r"(<w:settings\b[^>]*>)", r"\1<w:displayBackgroundShape/>",
                                  text, count=1)
                data = text.encode("utf-8")
            zout.writestr(item, data)
    tmp.replace(docx)


def to_docx(src, out, args):
    ensure_brand_fonts()
    soffice_convert(src, out, "HTML (StarWriter)", "docx:MS Word 2007 XML")
    m = BODY_BGCOLOR_RE.search(src.read_text(encoding="utf-8"))
    if m:
        set_docx_page_color(out, m.group(1).upper())


def to_pdf(src, out, args):
    chrome_pdf(src, out, args.wait)


def to_pptx(src, out, args):
    with tempfile.TemporaryDirectory() as tmp:
        pdf = Path(tmp, src.stem + ".pdf")
        chrome_pdf(src, pdf, args.wait)
        ensure_brand_fonts()
        soffice_convert(pdf, out, "impress_pdf_import", "pptx")


# --- Tables (XLSX / CSV) ---------------------------------------------------

class TableParser(HTMLParser):
    """Collect top-level <table> elements as rows of cell dicts."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables = []
        self.depth = 0
        self.cell = None
        self.row = None
        self.in_caption = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "table":
            self.depth += 1
            if self.depth == 1:
                self.tables.append({"name": a.get("data-sheet"), "caption": "", "rows": []})
            return
        if self.depth != 1:
            return
        if tag == "caption":
            self.in_caption = True
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th") and self.row is not None:
            self.cell = {
                "text": [], "header": tag == "th",
                "type": a.get("data-type", "auto"),
                "value": a.get("data-value"),
                "formula": a.get("data-formula"),
                "colspan": int(a.get("colspan", "1") or 1),
            }
        elif tag == "br" and self.cell is not None:
            self.cell["text"].append("\n")

    def handle_endtag(self, tag):
        if tag == "table":
            self.depth -= 1
            return
        if self.depth != 1:
            return
        if tag == "caption":
            self.in_caption = False
        elif tag in ("td", "th") and self.cell is not None:
            raw = "".join(self.cell["text"])
            lines = [re.sub(r"[ \t\r\f\v]+", " ", ln).strip() for ln in raw.split("\n")]
            self.cell["text"] = "\n".join(lines).strip()
            self.row.append(self.cell)
            for _ in range(self.cell["colspan"] - 1):
                self.row.append({"text": "", "header": self.cell["header"], "type": "text",
                                 "value": None, "formula": None, "colspan": 1})
            self.cell = None
        elif tag == "tr" and self.row is not None:
            self.tables[-1]["rows"].append(self.row)
            self.row = None

    def handle_data(self, data):
        if self.depth != 1:
            return
        if self.cell is not None:
            self.cell["text"].append(data)
        elif self.in_caption:
            self.tables[-1]["caption"] += data


def parse_tables(src: Path):
    parser = TableParser()
    parser.feed(src.read_text(encoding="utf-8"))
    tables = [t for t in parser.tables if t["rows"]]
    if not tables:
        fail(f"no <table> with rows found in {src}")
    used = set()
    for i, t in enumerate(tables, 1):
        name = t["name"] or t["caption"].strip() or f"Sheet{i}"
        name = re.sub(r"[\[\]:*?/\\]", "-", name)[:31] or f"Sheet{i}"
        base, n = name, 2
        while name.lower() in used:
            suffix = f" ({n})"
            name = base[:31 - len(suffix)] + suffix
            n += 1
        used.add(name.lower())
        t["name"] = name
    return tables


NUMBER_RE = re.compile(r"^-?(0|[1-9]\d*)(\.\d+)?([eE][+-]?\d+)?$")


def cell_value(cell):
    """Return (kind, value): kind is 'formula', 'number', 'bool' or 'text'."""
    if cell["formula"]:
        return "formula", cell["formula"].lstrip("=")
    raw = cell["value"] if cell["value"] is not None else cell["text"]
    kind = cell["type"]
    if kind == "number" or (kind == "auto" and NUMBER_RE.match(raw)):
        cleaned = raw.replace(",", "").replace(" ", "")
        try:
            float(cleaned)
            return "number", cleaned
        except ValueError:
            pass
    if kind == "bool" and raw.lower() in ("true", "false", "1", "0"):
        return "bool", "1" if raw.lower() in ("true", "1") else "0"
    return "text", raw


def col_letter(idx):
    s = ""
    idx += 1
    while idx:
        idx, r = divmod(idx - 1, 26)
        s = chr(65 + r) + s
    return s


def sheet_xml(table):
    rows = table["rows"]
    ncols = max(len(r) for r in rows)
    widths = [8] * ncols
    out = []
    for r_i, row in enumerate(rows, 1):
        cells = []
        for c_i, cell in enumerate(row):
            ref = f"{col_letter(c_i)}{r_i}"
            style = ' s="1"' if cell["header"] else ""
            kind, val = cell_value(cell)
            longest = max((len(x) for x in str(val).split("\n")), default=0)
            widths[c_i] = min(max(widths[c_i], longest + 2), 60)
            if kind == "formula":
                cells.append(f'<c r="{ref}"{style}><f>{html.escape(val)}</f></c>')
            elif kind == "number":
                cells.append(f'<c r="{ref}"{style}><v>{val}</v></c>')
            elif kind == "bool":
                cells.append(f'<c r="{ref}"{style} t="b"><v>{val}</v></c>')
            elif val != "":
                style = ' s="2"' if not cell["header"] and "\n" in val else style
                cells.append(f'<c r="{ref}"{style} t="inlineStr"><is>'
                             f'<t xml:space="preserve">{html.escape(val)}</t></is></c>')
        out.append(f'<row r="{r_i}">{"".join(cells)}</row>')
    header = rows[0] and all(c["header"] for c in rows[0])
    pane = ('<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" '
            'activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>') if header else ""
    cols = "".join(f'<col min="{i}" max="{i}" width="{w}" customWidth="1"/>'
                   for i, w in enumerate(widths, 1))
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
            f'{pane}<cols>{cols}</cols><sheetData>{"".join(out)}</sheetData></worksheet>')


STYLES_XML = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
    # Brand: Montserrat body; header row in Copper (#E4AF7A) bold on #151515.
    '<fonts count="2"><font><sz val="10"/><name val="Montserrat"/></font>'
    '<font><b/><sz val="10"/><color rgb="FFE4AF7A"/><name val="Montserrat"/></font></fonts>'
    '<fills count="3"><fill><patternFill patternType="none"/></fill>'
    '<fill><patternFill patternType="gray125"/></fill>'
    '<fill><patternFill patternType="solid"><fgColor rgb="FF151515"/></patternFill></fill></fills>'
    '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
    '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
    '<cellXfs count="3"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
    '<xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1"/>'
    '<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1">'
    '<alignment wrapText="1" vertical="top"/></xf></cellXfs>'
    '</styleSheet>'
)


def to_xlsx(src, out, args):
    tables = parse_tables(src)
    n = len(tables)
    ct_sheets = "".join(
        f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/'
        'vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        for i in range(1, n + 1))
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml",
                   '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                   '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                   '<Default Extension="xml" ContentType="application/xml"/>'
                   '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
                   '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
                   f'{ct_sheets}</Types>')
        z.writestr("_rels/.rels",
                   '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
                   '</Relationships>')
        sheets = "".join(f'<sheet name="{html.escape(t["name"])}" sheetId="{i}" r:id="rId{i}"/>'
                         for i, t in enumerate(tables, 1))
        z.writestr("xl/workbook.xml",
                   '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
                   'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                   f'<sheets>{sheets}</sheets><calcPr fullCalcOnLoad="1"/></workbook>')
        rels = "".join(
            f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/'
            f'2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>'
            for i in range(1, n + 1))
        rels += (f'<Relationship Id="rId{n + 1}" Type="http://schemas.openxmlformats.org/'
                 'officeDocument/2006/relationships/styles" Target="styles.xml"/>')
        z.writestr("xl/_rels/workbook.xml.rels",
                   '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   f'{rels}</Relationships>')
        z.writestr("xl/styles.xml", STYLES_XML)
        for i, t in enumerate(tables, 1):
            z.writestr(f"xl/worksheets/sheet{i}.xml", sheet_xml(t))


def to_csv(src, out, args):
    tables = parse_tables(src)
    if args.table is not None:
        picked = [t for i, t in enumerate(tables, 1)
                  if str(i) == args.table or t["name"] == args.table]
        if not picked:
            fail(f"table {args.table!r} not found; have: {[t['name'] for t in tables]}")
        tables = picked
    encoding = "utf-8-sig" if args.bom else "utf-8"
    written = []
    for t in tables:
        path = out if len(tables) == 1 else out.with_name(
            f"{out.stem}-{re.sub(r'[^A-Za-z0-9_-]+', '_', t['name'])}{out.suffix}")
        with open(path, "w", newline="", encoding=encoding) as f:
            w = csv.writer(f, delimiter=args.delimiter)
            for row in t["rows"]:
                w.writerow([c["value"] if c["value"] is not None else c["text"] for c in row])
        written.append(path)
    return written


CONVERTERS = {"pdf": to_pdf, "docx": to_docx, "pptx": to_pptx, "xlsx": to_xlsx, "csv": to_csv}


def main():
    p = argparse.ArgumentParser(description="Convert an HTML source file to an office file.")
    p.add_argument("input", type=Path, help="source .html file")
    p.add_argument("--to", required=True, choices=sorted(CONVERTERS), help="target format")
    p.add_argument("-o", "--output", type=Path, help="output path (default: input name + new extension)")
    p.add_argument("--wait", type=int, default=3000, help="ms Chrome waits for fonts/scripts (pdf, pptx)")
    p.add_argument("--table", help="csv: only export this table (1-based index or sheet name)")
    p.add_argument("--delimiter", default=",", help="csv: field delimiter (default ,)")
    p.add_argument("--bom", action="store_true", help="csv: write UTF-8 BOM so Excel detects UTF-8")
    args = p.parse_args()

    src = args.input
    if not src.is_file():
        fail(f"input not found: {src}")
    out = args.output or src.with_suffix("." + args.to)
    out.parent.mkdir(parents=True, exist_ok=True)

    with prepared_source(src, inline_images=args.to == "docx") as source:
        written = CONVERTERS[args.to](source, out, args) or [out]
    for path in written:
        print(path)


if __name__ == "__main__":
    main()
