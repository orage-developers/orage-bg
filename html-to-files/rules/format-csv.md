# Format: CSV

- Same source as XLSX: any template whose content lives in `<table>`s.
- One table: one file. Several tables: one file per table with a `-<sheet>`
  suffix, unless you pick one with `--table`.
- Exports `data-value` when present, else the visible text. Formulas are not
  exported: the cell text must hold the value.
- Default: UTF-8, `,` delimiter. Only when the target is Excel with a
  `;` locale (e.g. Spanish), use `--delimiter ";" --bom`. Google Sheets reads
  the default as is.
