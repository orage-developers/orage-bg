# Comparisons

Applies to [template-comparison-report.md](template-comparison-report.md)
and [template-comparison-data.md](template-comparison-data.md): any request
that compares two periods, two channels or two groups (Q1 vs Q2, this month
vs last month, TikTok vs Instagram).

- Lead with how much it changed, in %: the headline is the main change in
  one line ("Views up +42.0% in Q2").
- Every compared metric shows the absolute change (`+170,000`) and the %
  change (`+42.0%`), both computed from the same numbers. In XLSX use
  formulas and `data-format="percent"`.
- The earlier or baseline series is gray `#A6A6A6`; the later or main series
  is gold `#B68039`. Keep that order in every chart, legend and table.
- Every chart has a legend and prints its values next to the bars, and a
  table shows the same numbers. Color is never the only way to read a value.
- One scale per chart. When metrics have different units (views, seconds,
  posts), give each metric its own pair of bars scaled to its own maximum,
  and say so ("Each metric uses its own scale"). Never two y-axes.
- Bar widths: `value / max * width`. In documents each bar is one single-row
  table (DOCX keeps those widths).
