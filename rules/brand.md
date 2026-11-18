# Brand

Every file follows the Orage AI Agency brand, unless the request explicitly
names another brand. Read `BRAND-GUIDELINES.md` in full before you
write the HTML. Take the voice, typography and company facts (offer, prices,
products, location) from it. Take colors from this rule: this palette
replaces the color section of the guidelines for every file this skill
makes.

Never invent clients, results, numbers, prices or contact details that are
not in the guidelines. Mark sample data as sample data.

## Palette

Gold accent, black and dark backgrounds, text inverted to the background.
Tokens are in `brand/tokens.css`. Use no other colors.

| Role | Color | Use |
|---|---|---|
| Background | `#010101` | Page and slide background |
| Background | `#151515` | Bands, covers, table cells |
| Background | `#212121` | Cards, boxes, table headers |
| Gold accent | `#B68039` | On every file: h1, rules, key numbers, CTAs |
| Light gold | `#E4AF7A` | h2, h3, table header text |
| Dark gold | `#543C1C` | Borders and dividers |
| Text | `#FEFEFE` | Body text (inverse of `#010101`) |
| Text | `#DEDEDE` | Lead, notes, labels (inverse of `#212121`) |
| Chart series 1 | `#A6A6A6` | Baseline or earlier period |
| Chart series 2 | `#B68039` | Main or later period |

**Never `#000000`.** The darkest color is `#010101`.

## Fonts

- **Two fonts, never a third**: Bebas Neue (weight 400 only, always
  UPPERCASE and letter-spaced) for headings, eyebrows, prices and buttons;
  Montserrat (500 body, 600 lead, 700 emphasis) in sentence case for
  everything else.
- Both are Google Fonts, so Google Docs, Slides and Sheets show them without
  installing anything.
- In the HTML, request Medium and SemiBold by name with
  `font-weight: normal`: `"Montserrat Medium"` (body), `"Montserrat
  SemiBold"` (lead) and `"Montserrat"` with `font-weight: 700` (emphasis).
  The PDF shows those weights. The script renames them to `Montserrat` in
  DOCX and PPTX, which Google opens as Montserrat Regular.
- Never use `font-weight: 500` or `600`: DOCX turns them into bold.
- Bebas Neue has no `→` or `×`. Write `3X`, not `3×`, in Bebas text. Put the
  arrow in Montserrat: `<span class="arrow">→</span>`. Otherwise a third
  fallback font appears.
- The templates already declare the `@font-face` rules.

## Emblem and header

- Emblem `brand://logo/logo.png` on every file, unaltered.
- Headers have no background: the emblem and wordmark sit on the page.
- Documents and data files use the compact header: a 22 px emblem and the
  "ORAGE AI AGENCY" wordmark (Bebas Neue 11pt, gold), right-aligned.
  `comparison-report.html` and `comparison-data.html` keep the larger,
  left-aligned header.
- Decks put the emblem on the cover and closing slides.

## Voice

- Confident, direct, premium, action-led.
- Result first, short sentences, numbers over adjectives.
- "We" for Orage and "you" for the buyer.
- No hype words ("revolutionary", "cutting-edge", "game-changing").
- No emoji in headings, buttons or labels; `→` is the only allowed glyph.
- No quotation marks for emphasis: use bold or gold.

## Footer

PDF documents carry "© Orage AI Agency · Edmond, Oklahoma · orage.agency"
(already in the templates). DOCX has no footer; that is fine.

## `brand://` URLs

In the HTML, `brand://<path>` points to the skill's `brand/` folder. The
script resolves it on every conversion.

```html
<img src="brand://logo/logo.png" width="22" alt="Orage AI Agency">
<style>
  @font-face { font-family: "Bebas Neue"; src: url("brand://fonts/BebasNeue-Regular.ttf"); }
</style>
```

For DOCX the script embeds local images as `data:` URIs. For DOCX and PPTX
it installs the brand fonts in the user font folder
(`~/.local/share/fonts/orage-brand` on Linux, `~/Library/Fonts` on macOS)
when they are missing, so the conversion measures text with the real fonts.

## Brand folder

`BRAND-GUIDELINES.md` sits at the skill root. `brand/` holds `tokens.css`,
`fonts/` (Bebas Neue, Montserrat Regular/Medium/SemiBold/Bold, OFL licenses)
and `logo/logo.png`.
