# Format: PDF

- Page size and background: `@page { size: Letter; margin: …;
  background: #010101; }`. The `@page` background also covers the margins.
- Repeating footer: `@page { @bottom-center { content: "…"; } }`. Use
  `"Montserrat Medium"` there: Chrome only loads a font for a margin box when
  the page body also uses it.
- Page break: `page-break-before: always` on the element. Headings carry
  `break-after: avoid` so they stay with their content.
- Chrome renders all modern CSS (flex, grid, web fonts, SVG).
- The PDF is the visual reference for every other format made from the same
  HTML. Page counts are guaranteed only here.
