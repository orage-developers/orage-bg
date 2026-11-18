# Template: Tracker

- **File**: `templates/tracker.html`
- **Formats**: XLSX (primary), PDF
- **Use for**: project or task trackers.
- **Also follow**: [format-xlsx.md](format-xlsx.md).

## Structure

1. Sheet `Tracker`: `Week`, `Task`, `Owner`, `Status`, `Due`, `Done`.
   `Done` is `=IF(D<n>="Done",1,0)`.
2. Sheet `Summary`: tasks (`COUNTA`), done (`SUM`), progress (%).

## Content

- Status values: `Done`, `In progress`, `Not started`.
- Dates as text in ISO format (`data-type="text"`).
