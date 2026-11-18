# Format: XLSX

- Each top-level `<table>` is one sheet. Sheet name: `data-sheet="Name"`,
  else the `<caption>`, else `Sheet1`, `Sheet2`…
- The script applies the brand style for Google Sheets: Montserrat
  `#FEFEFE` on `#010101` in every table cell, `<th>` in Montserrat Bold gold
  on `#151515`, thin `#543C1C` row lines, gridlines hidden. The HTML's CSS
  does not affect the XLSX. When the first row is all `<th>`, it is frozen.
- Types: plain numbers like `12` or `19.90` are stored as numbers. Force text
  with `data-type="text"` (codes with leading zeros, ISO dates, phone
  numbers). Force a number with `data-type="number"`. Boolean:
  `data-type="bool"`.
- Formatted numbers: show `405,000` as the cell text and put the raw number
  in `data-value="405000"`. The XLSX and CSV use `data-value`; the PDF shows
  the text.
- Percentages: `data-format="percent"` stores the value as a fraction and
  shows it as `+42.0%`. Use it with a formula
  (`data-formula="=(C2-B2)/B2"`) or with a text value like `+42.0%`.
- Formulas: `<td data-formula="=SUM(B2:B3)">17</td>`. Sheets recalculates on
  open. Put the computed value as the cell text so the PDF and CSV show it
  too. Cross-sheet references use the sheet name: `=SUM(Tracker!F2:F7)`.
- `colspan` is kept by padding empty cells. `rowspan` is not supported:
  repeat the value on each row.
- `<br>` inside a cell makes a line break.
- Content outside `<table>` (header, tiles, `.note` paragraphs) appears only
  in the PDF.
