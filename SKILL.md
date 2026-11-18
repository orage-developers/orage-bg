---
name: html-to-files
description: >
  Create DOCX, PPTX, PDF, XLSX and CSV files, always from an HTML source and
  always in the Orage AI Agency brand, mainly for Google Workspace (Docs,
  Slides, Sheets). Use it whenever an agent must deliver a document, deck,
  PDF, spreadsheet or CSV: reports, status reports, proposals, one-pagers,
  letters, pitch decks, comparison reports (period vs period, e.g. TikTok
  views Q1 vs Q2), trackers and lists. The agent follows the brand guidelines
  and the rules in rules/, writes the HTML from a template and converts it
  with scripts/html2file.py.
---

# HTML to files (DOCX, PPTX, PDF, XLSX, CSV)

Always, without exception:

1. **Follow the brand guidelines**: `BRAND-GUIDELINES.md` and
   [rules/brand.md](rules/brand.md).
2. **Follow the rules for files** in `rules/`: read
   [rules/workflow.md](rules/workflow.md), the rule for the template you use
   and the rule for each target format, then
   [rules/verification.md](rules/verification.md) before you deliver.

## Rules index

### General

| Rule | Covers |
|---|---|
| [brand.md](rules/brand.md) | Palette, fonts, emblem, header, voice, `brand://` URLs |
| [workflow.md](rules/workflow.md) | HTML first, steps, engines, script options |
| [verification.md](rules/verification.md) | Checks before delivery, common errors |
| [comparisons.md](rules/comparisons.md) | Period vs period comparisons: % change, series colors, charts |

### Formats

| Rule | Covers |
|---|---|
| [format-pdf.md](rules/format-pdf.md) | Page size, background, footer, page breaks |
| [format-docx.md](rules/format-docx.md) | HTML subset for Google Docs, tables, page color |
| [format-pptx.md](rules/format-pptx.md) | Slide sections, sizes, text that fits |
| [format-xlsx.md](rules/format-xlsx.md) | Sheets, types, formulas, percent format |
| [format-csv.md](rules/format-csv.md) | Files per table, values, delimiter |

### Templates

| Rule | Template | Formats |
|---|---|---|
| [template-document.md](rules/template-document.md) | `document.html` | DOCX, PDF |
| [template-report.md](rules/template-report.md) | `report.html` | DOCX, PDF |
| [template-comparison-report.md](rules/template-comparison-report.md) | `comparison-report.html` | DOCX, PDF |
| [template-proposal.md](rules/template-proposal.md) | `proposal.html` | DOCX, PDF |
| [template-one-pager.md](rules/template-one-pager.md) | `one-pager.html` | PDF, DOCX |
| [template-letter.md](rules/template-letter.md) | `letter.html` | DOCX, PDF |
| [template-slides.md](rules/template-slides.md) | `slides.html` | PPTX, PDF |
| [template-pitch-deck.md](rules/template-pitch-deck.md) | `pitch-deck.html` | PPTX, PDF |
| [template-data.md](rules/template-data.md) | `data.html` | XLSX, CSV, PDF |
| [template-comparison-data.md](rules/template-comparison-data.md) | `comparison-data.html` | XLSX, CSV, PDF |
| [template-tracker.md](rules/template-tracker.md) | `tracker.html` | XLSX, PDF |
| [template-contact-list.md](rules/template-contact-list.md) | `contact-list.html` | CSV, XLSX, PDF |
