---
name: html-to-files
description: >
  Create DOCX, PPTX, PDF, XLSX and CSV files, always from an HTML source and
  always in the Orage AI Agency brand. Use it whenever an agent must deliver a
  Word document, a PowerPoint deck, a PDF, an Excel workbook or a CSV, or
  convert content into any of those formats, mainly for Google Workspace
  (Docs, Slides, Sheets): reports, proposals, one-pagers,
  letters, pitch decks, comparison reports (period vs period, e.g. TikTok views
  Q1 vs Q2), trackers and lists. The agent picks a template, writes the HTML
  following brand/BRAND-GUIDELINES.md, and converts it with
  scripts/html2file.py. It never builds the binary directly.
---

# HTML to files (DOCX, PPTX, PDF, XLSX, CSV)

Two rules, no exceptions:

1. **Every file starts as HTML.** The HTML is the source of truth. To change
   the file, edit the HTML and convert again. Do not use python-docx,
   python-pptx, openpyxl, reportlab or binary editors to create content.
2. **Every file follows the Orage AI Agency brand**: the palette below plus
   the fonts, voice and facts in `brand/BRAND-GUIDELINES.md`, unless the
   request explicitly names another brand.

Files are opened mainly in **Google Workspace**: DOCX in Google Docs, PPTX
in Google Slides, XLSX and CSV in Google Sheets. LibreOffice only does the
conversion; do not tune output for how LibreOffice displays it. The PDF of
the same HTML is the visual reference.

In this document, `<skill-dir>` is the folder that contains this `SKILL.md`.

## Brand guidelines (required)

Before you write the HTML, read `brand/BRAND-GUIDELINES.md` in full. Take
the voice, typography and company facts (offer, prices, products, location)
from it. Take colors from this file: the palette below replaces the color
section of the guidelines for every file this skill makes. Never invent clients, results, numbers, prices or contact
details that are not in that file. Mark sample data as sample data.

The templates in `templates/` already apply the brand. Every file meets
these rules:

- **Palette: gold accent, black and dark backgrounds, text inverted to the
  background.** Tokens are in `brand/tokens.css`; no other colors.
  - Backgrounds: `#010101` (page, slide), `#151515` (bands, covers, cells),
    `#212121` (cards, boxes, table headers). **Never `#000000`**: the
    darkest color is `#010101`.
  - Gold accent: `#B68039` on every file (h1, rules, key numbers, CTAs);
    `#E4AF7A` for h2, h3 and table header text; `#543C1C` for borders.
  - Text, inverted to the background: `#FEFEFE` body, `#DEDEDE` lead,
    notes and labels.
  - Charts: baseline or earlier series `#A6A6A6`, main or later series
    `#B68039`.
- **Two fonts, never a third**: Bebas Neue (weight 400 only, always
  UPPERCASE and letter-spaced) for headings, eyebrows, prices and buttons;
  Montserrat (500 body, 600 lead, 700 emphasis) in sentence case for
  everything else.
- **Font names Google knows.** Both fonts are Google Fonts, so Docs, Slides
  and Sheets show them without installing anything. In the HTML, request
  Medium and SemiBold by name with `font-weight: normal`:
  `"Montserrat Medium"` (body), `"Montserrat SemiBold"` (lead) and
  `"Montserrat"` with `font-weight: 700` (emphasis). The PDF shows those
  weights; the script renames them to `Montserrat` in DOCX and PPTX, which
  Google opens as Montserrat Regular. Never use `font-weight: 500` or `600`:
  DOCX turns them into bold. The templates already declare the
  `@font-face` rules.
- Bebas Neue has no `→` or `×`. Write `3X`, not `3×`, in Bebas text, and put
  the arrow in Montserrat: `<span class="arrow">→</span>`. Otherwise a third
  fallback font appears.
- **Emblem** `brand://logo/logo.png` on every piece, unaltered.
- **Voice**: confident, direct, premium, action-led. Result first, short
  sentences, numbers over adjectives, "we" for Orage and "you" for the buyer.
  No hype words ("revolutionary", "cutting-edge", "game-changing").
- No emoji in headings, buttons or labels; `→` is the only allowed glyph. No
  quotation marks for emphasis: use bold or gold.
- PDF document footer: "© Orage AI Agency · Edmond, Oklahoma ·
  orage.agency" (already in the templates). DOCX has none; that is fine.

### `brand://` URLs

In the HTML, `brand://<path>` points to this skill's `brand/` folder. The
script resolves it on every conversion. Examples:

```html
<img src="brand://logo/logo.png" width="56" alt="Orage AI Agency">
<style>
  @font-face { font-family: "Bebas Neue"; src: url("brand://fonts/BebasNeue-Regular.ttf"); }
</style>
```

For DOCX the script embeds local images as `data:` URIs. For DOCX and PPTX
it installs the brand fonts in the user font folder
(`~/.local/share/fonts/orage-brand` on Linux, `~/Library/Fonts` on macOS)
when they are missing, so the conversion measures text with the real fonts.

`brand/` holds `BRAND-GUIDELINES.md`, `tokens.css`, `fonts/` (Bebas Neue,
Montserrat Regular/Medium/SemiBold/Bold, OFL licenses) and `logo/logo.png`.
`brand/BRAND-GUIDELINES.md` is a copy of `BRAND-GUIDELINES.md` at the
repository root: when the root file changes, update the copy.

## Templates

Pick the closest template. Each one is a complete, branded HTML page with
sample content in `[brackets]` or marked as sample data.

| Template | Use for | Convert to |
|---|---|---|
| `document.html` | Any document without a closer template | DOCX, PDF |
| `report.html` | Report: summary, metrics table, findings, recommendations, next steps | DOCX, PDF |
| `comparison-report.html` | Period vs period report (e.g. TikTok views Q1 vs Q2): KPI tiles, bar charts, comparison table, monthly trend, drivers | DOCX, PDF |
| `proposal.html` | Client proposal: problem, products, Orage 90 price box, timeline, CTA | DOCX, PDF |
| `one-pager.html` | One-page overview: positioning, products, offer ladder, CTA (one page in PDF) | PDF, DOCX |
| `letter.html` | Letter: date, recipient, subject, body, signature | DOCX, PDF |
| `slides.html` | Any deck without a closer template: cover, bullets, big number, close | PPTX, PDF |
| `pitch-deck.html` | Sales deck: problem, products, offer tiers side by side, trickle-down, CTA | PPTX, PDF |
| `comparison-deck.html` | Period vs period deck: headline change, monthly bars, per-metric bars, full table, drivers | PPTX, PDF |
| `data.html` | Any data without a closer template: two sheets, types, formulas, total row | XLSX, CSV, PDF |
| `comparison-data.html` | Period vs period numbers: change and % change formulas, monthly sheet with quarter totals | XLSX, CSV, PDF |
| `tracker.html` | Project tracker: tasks, status, done flag, summary sheet | XLSX, PDF |
| `contact-list.html` | Contact or lead list, one table | CSV, XLSX, PDF |

You may add CSS rules to a template's `<style>` block for new components.
Keep the existing rules, the fonts and the header with the emblem.

### Comparison reports

Use the `comparison-*` templates whenever the request compares two periods,
two channels or two groups (Q1 vs Q2, this month vs last month, TikTok vs
Instagram).

- The earlier or baseline series is gray `#A6A6A6`; the later or main
  series is gold `#B68039`. Keep that order in every chart, legend and table.
- Every chart has a legend and prints its values next to the bars, and a
  table shows the same numbers. Color is never the only way to read a
  value.
- One scale per chart. When metrics have different units (views, seconds,
  posts), give each metric its own pair of bars scaled to its own maximum,
  and say so ("Each metric uses its own scale"). Never two y-axes.
- Bar widths: `value / max * width`. In documents each bar is one
  single-row table (DOCX keeps those widths). In decks bars are `<div>`s
  with `%` heights or widths.
- Change columns: absolute change (`+170,000`) and % change (`+42.0%`), both
  computed from the same numbers as the table. In XLSX use formulas.
- Headline = the main change in one line ("Views up +42.0% in Q2").

## Workflow

1. Read `brand/BRAND-GUIDELINES.md`.
2. Copy the template next to the deliverable:
   ```bash
   cp <skill-dir>/templates/report.html <out>/report.html
   ```
3. Write the content in that HTML. Change the `<title>`. Keep the `<style>`
   block and the header with the emblem. Follow the format rules below.
   `text-transform: uppercase` works in every format.
4. Convert:
   ```bash
   python3 <skill-dir>/scripts/html2file.py <out>/report.html --to docx
   ```
   Without `-o`, the output is the HTML path with the new extension
   (`<out>/report.docx`).
5. Verify the result (see "Verification").
6. Deliver the file and keep the HTML next to it.

When a PDF of a DOCX, PPTX, XLSX or CSV is also requested, convert it from
the **same HTML** with `--to pdf`. It lands as `<name>.pdf` next to the other
file. Never convert the binary to PDF for delivery: the source is always the
HTML.

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

## Format rules

### PDF

- Page size and background: `@page { size: Letter; margin: …;
  background: #010101; }`. The `@page` background also covers the margins.
- Repeating footer: `@page { @bottom-center { content: "…"; } }`. Use
  `"Montserrat Medium"` there: Chrome only loads a font for a margin box when
  the page body also uses it.
- Page break: `page-break-before: always` on the element.
- Chrome renders all modern CSS (flex, grid, web fonts, SVG).

### DOCX

The DOCX is made by LibreOffice's HTML import and opened in Google Docs.
The import keeps a subset of HTML/CSS. For a faithful DOCX:

- Semantic structure: `h1`–`h3`, `p`, `ul`/`ol`, `table`, `strong`, `em`,
  `a`, `img`. Headings become real Word heading styles.
- Page background: `<body bgcolor="#010101">`. The script applies it as the
  DOCX page color, which Google Docs shows as the page color.
- Declare font and color on every selector (`body, p, li, td, th, span`).
  The import does not inherit from `body`.
- Hex colors, not `var(--o-…)`: the import does not read CSS variables.
- Tables: attributes `border="1" cellspacing="0" cellpadding="6"
  width="100%"`. Cell fill with `bgcolor` and alignment with `align`. The
  `th` text color is lost: wrap it in `<span class="th">`.
- When a CSS rule and a `bgcolor` disagree, the PDF follows CSS. Put the
  color in an inline `style` too (as the comparison bars do).
- No flex, grid or `position`: they are dropped. Lay out columns with tables
  (like the header band in the templates).
- Nested tables lose their column widths. Use single-row tables for bars.
- The DOCX has no footer: `@page` exists only in the PDF. That is fine.
- Page count is guaranteed only in the PDF. Google Docs lays out the DOCX
  with its own margins; a page more or less there is fine.
- Images: paths relative to the HTML, `brand://` or `data:` URIs, with an
  explicit `width`.

### PPTX

- Each `<section class="slide">` is one 13.333 × 7.5 in slide (16:9).
- Do not change `@page` or the `.slide` size. Overflowing content is cut
  (`overflow: hidden`).
- All Chrome CSS works (flex, grid, web fonts, SVG).
- Cover and closing slides use class `cover` and the emblem; content slides
  sit on black.
- The PPTX has editable text and shapes, placed absolutely. To change the
  design, edit the HTML and convert again.
- After the import the script sets Google font names and Bebas Neue
  letter-spacing. Spacing in the PPTX is approximate; that is fine as long
  as the slide reads well. The PDF of the same HTML is the exact reference.
- Text that fits: titles 54–88pt, body 20–24pt, card text 17pt. At most 5
  bullets or about 40 words of body text per slide, cards included.

### XLSX

- Each top-level `<table>` is one sheet. Sheet name: `data-sheet="Name"`,
  else the `<caption>`, else `Sheet1`, `Sheet2`…
- The script applies the brand style for Google Sheets: Montserrat
  `#FEFEFE` on `#010101` in every table cell, `<th>` in Montserrat Bold gold
  on `#151515`, thin `#543C1C` row lines, gridlines hidden. The HTML's CSS
  does not affect the XLSX. When the first row is all `<th>`, it is frozen.
- Types: numbers like `12` or `19.90` are stored as numbers. Write raw
  numbers without thousands separators (`405000`, not `405,000`). Force text
  with `data-type="text"` (codes with leading zeros, ISO dates, phone
  numbers). Force a number with `data-type="number"`. Boolean:
  `data-type="bool"`.
- Formulas: `<td data-formula="=SUM(B2:B3)">17</td>`. Excel recalculates on
  open. Put the computed value as the cell text so the PDF and CSV show it
  too. Cross-sheet references use the sheet name: `=SUM(Tracker!F2:F7)`.
- A value different from the visible text: `data-value="1234.5"`.
- `colspan` is kept by padding empty cells. `rowspan` is not supported:
  repeat the value on each row.
- `<br>` inside a cell makes a line break.
- Content outside `<table>` (header, `.note` paragraphs) appears only in the
  PDF.

### CSV

- Same source as XLSX (`data.html`, `contact-list.html`, …).
- One table: one file. Several tables: one file per table with a `-<sheet>`
  suffix, unless you pick one with `--table`.
- Exports `data-value` when present, else the visible text. Formulas are not
  exported: the cell text must hold the value.
- Default: UTF-8, `,` delimiter. Only when the target is Excel with a
  `;` locale (e.g. Spanish), use `--delimiter ";" --bom`.

## Verification

Use your own temporary check folder (`$CHECK`), such as the session
scratchpad or `mktemp -d`. Never use the output folder: the review PDF would
overwrite the delivered PDF. Look at every page, not only the first (set
`-l`), at 70 dpi or more. Always check:

- PDF: `head -c 4 file.pdf` prints `%PDF`. Rasterize and look at the pages:
  ```bash
  pdfinfo file.pdf | grep Pages
  pdftoppm -r 70 -png file.pdf "$CHECK/p"
  ```
- DOCX and PPTX: convert them to PDF for review only and look at the pages.
  This LibreOffice render is a proxy for Google Docs and Slides: check
  content, colors, fonts and order, not exact line breaks or page count.
  ```bash
  soffice --headless --convert-to pdf --outdir "$CHECK" file.docx
  pdfinfo "$CHECK/file.pdf" | grep Pages
  pdftoppm -r 70 -png "$CHECK/file.pdf" "$CHECK/p"
  ```
- Fonts: in every PDF (delivered or review), `pdffonts` lists only
  BebasNeue and Montserrat (plus OpenSymbol for DOCX bullets). Any other
  font means a glyph the brand fonts lack or a misspelled family.
- Colors: `grep -ci '#000000' file.html` prints 0.
- PPTX: the slide count equals the number of `.slide` sections:
  `unzip -l file.pptx | grep -c 'ppt/slides/slide[0-9]*.xml'`.
- XLSX: export every sheet to CSV (one file per sheet) and check values and
  computed formulas:
  ```bash
  soffice --headless --convert-to 'csv:Text - txt - csv (StarCalc):44,34,76,1,,0,false,true,false,false,false,-1' \
    --outdir "$CHECK" file.xlsx
  ```
- CSV: `head` the file; check accents and the delimiter.
- Comparison reports: recompute one change and one % change by hand and
  match them against the table, the chart labels and the headline.

## Common errors

- `LibreOffice produced no output`: the HTML is missing or has an encoding
  error. Always save UTF-8 with `<meta charset="utf-8">`.
- `Chrome/Chromium not found`: install Chrome or set `CHROME_BIN`.
- Wrong fonts in DOCX: the font was not declared on every selector.
- Bold body text in DOCX: `font-weight: 500/600` was used instead of the
  per-weight family.
- LiberationSans or another extra font in `pdffonts`: a `→`/`×` in Bebas
  Neue, or a margin-box footer using a font the body does not use.
- White page in DOCX: `bgcolor` is missing on `<body>`.
- Bars without color in the PDF: a CSS rule overrides `bgcolor`; add an
  inline `style="background:…"`.
- Extra slides in PPTX: a `.slide` overflows or content sits outside the
  sections.
