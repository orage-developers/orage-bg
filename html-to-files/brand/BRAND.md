# ORAGE AI AGENCY — Brand Brief (default)

> Default brand for the Additional Orage agent stack. Every agent in this stack
> uses it for copy, pages, documents, decks, images, video, ads and email,
> unless the request names another brand. Source: the public website
> https://orage.agency (styles, logo and copy read 2026-11-13). Company facts
> live in `COMPANY.md` next to this file. No official brand guide PDF yet; when
> one arrives, add it here and update this file.

---

## 1. Identity

| Field | Value |
|---|---|
| Name | ORAGE AI AGENCY (short: Orage). Legal: ORAGE AGENCY LLC, est. 2025 |
| What it is | An AI agency that finds the highest-leverage constraint in a service business and builds custom AI systems to remove it |
| Audience | Owners and leaders of service businesses doing $1M+ a year: agencies, consultancies, coaching operations, professional service firms |
| Tagline | "Turn your business into a high-margin machine." |
| Brand line | "Taking the world by storm" (orage is French for storm) |
| Founder | George Moffat |
| Values | People-first, AI-first |

---

## 2. Voice

Confident, direct, results-oriented. Short declarative sentences. Talk to an
owner who is busy and skeptical of tools.

- Lead with the outcome (margin, capacity, retention), then the how.
- One idea per sentence. Concrete verbs: diagnose, build, automate, scale.
- Uppercase short headlines are on brand ("SCALE WITH AI", "LEARN AI").
- Say "custom AI systems", never "software package" or "plugin".
- Results are claims, not promises. Any mention of results or income carries
  the disclaimer in `COMPANY.md`.

### Don't

- No guaranteed revenue, savings or timelines.
- No invented clients, testimonials, case studies, prices or contact details.
- No hype stacks ("revolutionary", "game-changing", "insane"), no emoji in
  headings or buttons, at most one exclamation mark in a whole piece.
- No jargon without a plain-language line after it.

### Spanish

Same voice, "usted", short sentences. Keep "ORAGE AI AGENCY" and service names
in English when they are product names.

---

## 3. Visual identity principles

Dark, premium, editorial. Black and near-black surfaces, generous space, gold
used as the single accent, large uppercase display type. The storm emblem is
the anchor of every piece.

---

## 4. Logo

| File | Use |
|---|---|
| `logo/logo.png` | Gold storm emblem (cloud, lightning, waves, circuit lines in a rope circle), 700 × 700, transparent. Primary logo |
| `logo/logo-white.png` | Same emblem; use on dark backgrounds (gold reads on black) |
| `logo/brandmark.png` | Same emblem for square spaces (avatars, favicons, stamps) |
| `logo/icon-180.png` | 180 × 180 app icon from the site |

- Pair the emblem with the wordmark set in Syne Bold uppercase:
  "ORAGE AI AGENCY". There is no separate wordmark file yet.
- Use unaltered: no recolor, rotation, outline, shadow or crop. Minimum
  clear space: a quarter of the emblem width on every side.
- Minimum size: 48 px digital, 0.5" print.

---

## 5. Color

### Primary palette

| Token | Name | HEX | Use |
|---|---|---|---|
| `--o-ink` | Ink | `#0A0A0A` | Dark backgrounds, text on light |
| `--o-gold` | Storm Gold | `#B68039` | The one accent: buttons, links, rules, highlights, key numbers |
| `--o-white` | White | `#FFFFFF` | Light backgrounds, text on dark |

### Supporting palette

| Token | Name | HEX | Use |
|---|---|---|---|
| `--o-gold-light` | Light Gold | `#C8922A` | Hover, gradient end |
| `--o-off-white` | Off-white | `#FAFAFA` | Text on ink, light cards |
| `--o-surface` | Surface | `#F5F5F5` | Light section backgrounds |
| `--o-border` | Border | `#E5E5E5` | Lines on light |
| `--o-graphite` | Graphite | `#262626` | Cards and lines on dark |
| `--o-charcoal` | Charcoal | `#171717` | Raised surfaces on dark |
| `--o-muted` | Muted | `#A1A1A1` | Secondary text on dark |
| `--o-slate` | Slate | `#525252` | Secondary text on light |

### Color usage (proportion)

About 60% ink or white surface, 30% neutrals, 10% gold. Gold never fills a
whole page. No other hues (no blue, red, green accents) except in charts that
need more series: then use gold, graphite and muted tints.

---

## 6. Typography

| Role | Font | Notes |
|---|---|---|
| Display, H1, H2 | **Syne** Bold or ExtraBold | Uppercase, tight leading (1.0), letter-spacing 0 to -1% |
| H3, labels | Syne SemiBold | Uppercase allowed |
| Body, UI | **Space Grotesk** Regular, Medium for emphasis | Leading 1.5 |
| Fallback | Arial, Helvetica, sans-serif | |

Local copies: `fonts/Syne.ttf`, `fonts/SpaceGrotesk.ttf` (variable, OFL).
Google Fonts:
`https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=Space+Grotesk:wght@400;500;700&display=swap`.
Never another family.

---

## 7. Photography

Real people at work (owners, teams, meetings), moody and high-contrast, warm
tones. A dark overlay (`rgba(10,10,10,0.6)`) under any text on a photo. No
stock robots, glowing brains or blue circuit clichés.

---

## 8. Iconography

Simple line icons, 1.5 px stroke, in gold on ink or ink on white. One style per
piece.

---

## 9. Supporting graphics and email

- Thin gold rules (1–2 px) to separate sections.
- Storm motifs from the emblem (lightning stroke, wave line, circuit dots) as
  subtle accents, never as a busy pattern.
- **Email**: start from `email-starter.html`: ink header with the emblem,
  white body, gold button, ink footer with the legal name.

---

## 10. Digital assets

- **Social**: portrait 1080 × 1350 px; reels 1080 × 1920. Big uppercase Syne
  headline, one line of Space Grotesk, emblem in a corner.
- **Video**: ink backgrounds, gold accent wipes, captions in Space Grotesk
  Medium white with an ink box; end card with emblem, "ORAGE AI AGENCY" and
  https://orage.agency.
- **Documents and PDFs**: white pages, ink text, gold rules and key numbers,
  cover page in ink with the emblem. Footer: "ORAGE AGENCY LLC · orage.agency".
- **Decks**: ink title slides, white content slides, gold for the one number
  that matters.

---

## 11. Printed assets

Bleed 0.125". Ink or white stock; gold as a spot color or foil where budget
allows. Business card 3.5" × 2": emblem on the ink side, name and role on the
white side.

---

## 12. How to use this brief

- **Copy**: §2 voice, facts only from `COMPANY.md`.
- **UI, pages, documents, decks**: §5 tokens from `tokens.css`, §6 fonts,
  emblem on every piece (§4).
- **Images and video**: §7, §8, §9, §10.
- **Open points**: official brand guide, vector emblem, standalone wordmark,
  public contact email and address.
