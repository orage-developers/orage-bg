# Template: Status report

- **File**: `templates/report.html`
- **Formats**: DOCX, PDF
- **Use for**: daily, weekly or project status reports.
- **Length**: one page in the PDF for a daily report; a weekly or project
  report may run two. Add `style="page-break-inside: avoid"` to short tables
  so they do not split across pages.

## Structure

1. Compact header.
2. H1: `Daily report` (or `Weekly report`, `Project report`).
3. Meta table: `Date`, `Name / Role`, `Project / Department`. Label cells
   `#212121` with `<span class="th">`, value cells `#151515`.
4. `1. Executive summary`: one or two sentences with the main result.
5. `2. Completed tasks`: bullets, each stated as a result.
6. `3. In progress / ongoing tasks`: bullets ending in
   `— Status: <strong>planning / in progress / blocked</strong>`.
7. `4. Roadblocks & challenges`: bullets with what is needed to clear each
   one, or "None".
8. `5. Plan for tomorrow` (or next period): numbered list.
9. `6. Additional notes / metrics`: table `Metric / KPI`, `Value`, `Notes`.

## Content

- Keep the numbered section titles and their order.
- Short items, one line each. No paragraphs inside lists.
- Uses the compact type scale (H1 24pt, H2 14pt, body 10pt).
