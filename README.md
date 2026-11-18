# Orage html-to-files skill

An agent skill that creates DOCX, PPTX, PDF, XLSX and CSV files for Orage AI
Agency. Every file starts as an HTML page built from a branded template and
is converted with one script. The output is meant mainly for Google
Workspace: DOCX opens in Google Docs, PPTX in Google Slides, and XLSX and CSV
in Google Sheets.

Agents read [SKILL.md](SKILL.md). This README is for the people who install
and maintain the skill.

## Layout

| Path | Contents |
|---|---|
| `SKILL.md` | Entry point for agents: always follow the brand guidelines and the rules, plus the rules index |
| `BRAND-GUIDELINES.md` | Orage brand guidelines: voice, typography, company facts |
| `rules/` | One Markdown rule per topic: brand, workflow, verification, comparisons, each format and each template |
| `templates/` | Branded HTML templates, one per kind of document |
| `scripts/html2file.py` | Converts an HTML file to PDF, DOCX, PPTX, XLSX or CSV |
| `brand/` | `tokens.css`, fonts (Bebas Neue, Montserrat) and the emblem |

## Requirements

- Python 3.9 or newer (standard library only).
- Google Chrome or Chromium for PDF and PPTX.
- LibreOffice (`soffice`) for DOCX and PPTX.
- Poppler (`pdftoppm`, `pdfinfo`, `pdffonts`) for the verification steps.

Set `CHROME_BIN` or `SOFFICE_BIN` when the binaries are not on `PATH`, and
`CHROME_NO_SANDBOX=1` inside containers without a sandbox.

## Install

Clone the repository and link it into the agent's skills folder. For Claude
Code:

```bash
git clone git@github.com:orage-developers/orage-bg.git
ln -s "$PWD/orage-bg" ~/.claude/skills/html-to-files
```

The first DOCX or PPTX conversion installs the brand fonts in
`~/.local/share/fonts/orage-brand` (Linux) or `~/Library/Fonts` (macOS) when
they are missing.

## Usage

```bash
cp templates/report.html out/report.html
# edit out/report.html
python3 scripts/html2file.py out/report.html --to docx
python3 scripts/html2file.py out/report.html --to pdf
```

Each call writes the file next to the HTML with the new extension, or to the
path given with `-o`. Run `python3 scripts/html2file.py --help` for the CSV
options.

## Templates

| Template | Formats |
|---|---|
| `document.html` | DOCX, PDF |
| `report.html` (status report) | DOCX, PDF |
| `comparison-report.html` (period vs period) | DOCX, PDF |
| `proposal.html` | DOCX, PDF |
| `one-pager.html` | PDF, DOCX |
| `letter.html` | DOCX, PDF |
| `slides.html` | PPTX, PDF |
| `pitch-deck.html` | PPTX, PDF |
| `data.html` | XLSX, CSV, PDF |
| `comparison-data.html` (period vs period) | XLSX, CSV, PDF |
| `tracker.html` | XLSX, PDF |
| `contact-list.html` | CSV, XLSX, PDF |

Each template has a rule in `rules/template-<name>.md` that describes its
structure and content.

## Brand at a glance

- Gold accent `#B68039`, black and dark backgrounds (`#010101`, `#151515`,
  `#212121`), text inverted to the background (`#FEFEFE`, `#DEDEDE`). Never
  `#000000`.
- Bebas Neue for headings, Montserrat for text. No third font.
- Full rules: [rules/brand.md](rules/brand.md) and
  [BRAND-GUIDELINES.md](BRAND-GUIDELINES.md).

## Maintaining

- Change a template's HTML and its rule in `rules/` together.
- Add a new template with a matching `rules/template-<name>.md` and a row in
  the `SKILL.md` index.
- Check every change with the steps in
  [rules/verification.md](rules/verification.md).
