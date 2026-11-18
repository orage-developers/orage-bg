# Template: Data

- **File**: `templates/data.html`
- **Formats**: XLSX, CSV, PDF
- **Use for**: any table data without a closer template.
- **Also follow**: [format-xlsx.md](format-xlsx.md),
  [format-csv.md](format-csv.md).

## Structure

1. Compact header (PDF only).
2. One `<table data-sheet="…">` per sheet, each with a `<caption>`.
3. First row of `<th>`. Total rows with `class="total"` and formulas.
4. Optional notes after the tables (PDF only).
