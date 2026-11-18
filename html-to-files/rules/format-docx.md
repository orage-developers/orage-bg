# Format: DOCX

The DOCX is made by LibreOffice's HTML import and opened in Google Docs. The
import keeps a subset of HTML/CSS. For a faithful DOCX:

- Semantic structure: `h1`–`h3`, `p`, `ul`/`ol`, `table`, `strong`, `em`,
  `a`, `img`. Headings become real heading styles.
- Page background: `<body bgcolor="#010101">`. The script applies it as the
  DOCX page color, which Google Docs shows as the page color.
- Declare font and color on every selector (`body, p, li, td, th, span`).
  The import does not inherit from `body`.
- Hex colors, not `var(--o-…)`: the import does not read CSS variables.
- Tables: attributes `border="1" cellspacing="0" cellpadding="6"
  width="100%"`. Cell fill with `bgcolor` and alignment with `align`. The
  `th` text color is lost: wrap it in `<span class="th">`.
- When a CSS rule and a `bgcolor` disagree, the PDF follows CSS. Put the
  color in an inline `style` too (as the comparison bars do).
- No flex, grid or `position`: they are dropped. Lay out columns with tables
  (like the header in the templates).
- Nested tables lose their column widths. Use single-row tables for bars.
- No footer: `@page` exists only in the PDF. That is fine.
- Google Docs lays out the DOCX with its own margins; a page more or less
  than the PDF is fine.
- Images: paths relative to the HTML, `brand://` or `data:` URIs, with an
  explicit `width`.
