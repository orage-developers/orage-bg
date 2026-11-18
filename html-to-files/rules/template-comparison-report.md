# Template: Comparison report

- **File**: `templates/comparison-report.html`
- **Formats**: DOCX, PDF
- **Use for**: period vs period reports (e.g. TikTok views Q1 vs Q2).
- **Also follow**: [comparisons.md](comparisons.md).

## Structure

1. Header with the emblem (no background).
2. Eyebrow: `Comparison report · <channel> · <period A> vs <period B>`.
3. H1 headline with the main % change ("Views up +42.0% in Q2"), then a
   lead line and a sample-data or source line.
4. KPI tiles: three metrics, each with % change, and `before → after`.
5. `<A> vs <B> by metric`: legend, then one pair of bars per metric
   (single-row tables), each with its value.
6. Comparison table: `Metric`, `A`, `B`, `Change`, `% change`.
7. Monthly (or weekly) trend: one bar per period, colored by period.
8. `What changed`: numbered drivers backed by the data.
9. `Next quarter`: table `Action`, `Target`, `Owner`.

## Content

- Every number appears in the table; bars and tiles repeat it, never add new
  ones.
- Bar width = value / max of that metric × 52 (the bar column width).
