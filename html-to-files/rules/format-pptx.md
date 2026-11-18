# Format: PPTX

- Each `<section class="slide">` is one 13.333 × 7.5 in slide (16:9).
- Do not change `@page` or the `.slide` size. Overflowing content is cut
  (`overflow: hidden`).
- All Chrome CSS works (flex, grid, web fonts, SVG).
- Cover and closing slides use class `cover` and the emblem; content slides
  sit on `#010101`.
- The PPTX has editable text and shapes, placed absolutely. Google Slides
  opens it as is. To change the design, edit the HTML and convert again.
- After the import the script sets Google font names and Bebas Neue
  letter-spacing. Spacing is approximate; that is fine as long as the slide
  reads well. The PDF of the same HTML is the exact reference.
- Text that fits: titles 54–88pt, body 20–24pt, card text 17pt. At most 5
  bullets or about 40 words of body text per slide, cards included.
