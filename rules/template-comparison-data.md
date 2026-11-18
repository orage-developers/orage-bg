# Template: Comparison data

- **File**: `templates/comparison-data.html`
- **Formats**: XLSX, CSV, PDF
- **Use for**: the numbers behind a period vs period comparison.
- **Also follow**: [comparisons.md](comparisons.md),
  [format-xlsx.md](format-xlsx.md).
- **Length**: one landscape page in the PDF. With more rows than the
  sample, tighten the cells (`th, td { padding: 2pt 6pt; }`) and move notes
  into HTML comments before cutting data. Two pages are acceptable only when
  the data does not fit after that.

## Structure

1. Header with the emblem, no background (PDF only).
2. % change tiles, one per metric: label, % change, `before → after`
   (PDF only).
3. Sheet `Comparison`: `Metric`, `A`, `B`, `Change`, `% change`. Raw numbers
   in `data-value`, change as a formula, % change as a formula with
   `data-format="percent"`.
4. Sheet `Monthly`: one row per month with its period, then a total per
   period and a `B vs A` row with the % change.
