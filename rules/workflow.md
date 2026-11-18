# Workflow

Every file starts as HTML. The HTML is the source of truth. To change the
file, edit the HTML and convert again. Do not use python-docx, python-pptx,
openpyxl, reportlab or binary editors to create content.

Files are opened mainly in **Google Workspace**: DOCX in Google Docs, PPTX in
Google Slides, XLSX and CSV in Google Sheets. LibreOffice only does the
conversion; do not tune output for how LibreOffice displays it. The PDF of
the same HTML is the visual reference.

`<skill-dir>` is the folder that contains `SKILL.md`.

## Steps

1. Read `BRAND-GUIDELINES.md` and [brand.md](brand.md).
2. Pick the template rule that fits the request (index in `SKILL.md`) and
   read it.
3. Copy its HTML template next to the deliverable:
   ```bash
   cp <skill-dir>/templates/report.html <out>/report.html
   ```
4. Write the content in that HTML. Change the `<title>`. Keep the `<style>`
   block and the header with the emblem. You may add CSS rules for new
   components. Follow the format rule for each target format.
5. Convert:
   ```bash
   python3 <skill-dir>/scripts/html2file.py <out>/report.html --to docx
   ```
   Without `-o`, the output is the HTML path with the new extension
   (`<out>/report.docx`).
6. Verify the result ([verification.md](verification.md)).
7. Deliver the file and keep the HTML next to it.

When a PDF of a DOCX, PPTX, XLSX or CSV is also requested, convert it from
the **same HTML** with `--to pdf`. It lands as `<name>.pdf` next to the other
file. Never convert the binary to PDF for delivery.

## Engines

| Format | Engine | Requires |
|---|---|---|
| PDF | Headless Chrome (`--print-to-pdf`) | Chrome or Chromium |
| DOCX | LibreOffice Writer (HTML import) | `soffice` |
| PPTX | Chrome to PDF, then LibreOffice Impress (PDF import) | Chrome + `soffice` |
| XLSX | Built-in stdlib writer | Python 3 |
| CSV | stdlib `csv` | Python 3 |

Optional variables: `CHROME_BIN`, `SOFFICE_BIN` (binary paths),
`CHROME_NO_SANDBOX=1` (containers without a sandbox).

## Script options

```
html2file.py INPUT.html --to pdf|docx|pptx|xlsx|csv [-o OUTPUT]
  --wait MS        time Chrome waits for fonts/JS (default 3000)
  --table N|NAME   csv: export only this table (1-based index or sheet name)
  --delimiter ;    csv: field delimiter (default ,)
  --bom            csv: write a UTF-8 BOM so Excel detects UTF-8
```

The script prints the path of each file it creates. It exits non-zero with
an `html2file: error:` message when something fails.
