# Template: Document

- **File**: `templates/document.html`
- **Formats**: DOCX, PDF
- **Use for**: any document without a closer template.

## Structure

1. Compact header (emblem and wordmark, right-aligned).
2. Eyebrow: `01 — <document type>`.
3. H1 title, then one lead line with the result.
4. Sections: H2 with a gold rule, short paragraphs, lists.
5. Tables with the `.data` class (`<span class="th">` in header cells).
6. Page breaks with `class="page-break"` on the next H2.

## Content

- Highlight the number that matters with `<span class="key">`.
- Move to a closer template when the request fits one (report, proposal,
  letter, comparison).
