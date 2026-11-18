# Orage AI Agency — Brand Guidelines

**Working reference compiled from the official `BRAND.md` source.**  

Source last updated 2026-05-05; maintainer: George Moffat.

> This document preserves the explicit brand rules in `BRAND.md`. Where the source gives no specification, this guide does not invent one. The source itself is the final authority.

## 1. Identity

- **Company:** Orage AI Agency

- **Founder:** George Moffat

- **Location:** Edmond, Oklahoma

- **Domain:** orage.agency

- **Category:** AI infrastructure and automation for service businesses

- **Positioning:** “We make your team operate at 3× capacity without adding a single hire.”

- **Primary market:** Service businesses at $1M–$100M+ ARR; OKC-first, scaling nationally.

### Offer ladder

| Tier | Offer | Price | Delivery | Source guidance |

|---|---|---|---|---|

| 1 | Orage AI Toolkit | TBD entry | DIY | For buyers testing the water |

| 2 | Orage 90 — AI Enabled Business | $2,500/mo | DFY | Promoted core offer; sell this when in doubt |

| 3 | Orage AI First — Agentic Infrastructure | Custom | DFY+ | For scaled organizations needing custom agents |

### Flagship products and services

- **STACY:** 24/7 AI phone agent; answers, qualifies, books, and logs to CRM; live within 24 hours of signup.

- **AI Chat / Messaging Agent:** Website chat and SMS automation.

- **Pre-Configured CRM:** Fills itself from STACY and chat interactions.

- **Weekly Group Call:** Bring a problem and leave with a framework, agent, or tool.

- **Trickle-down agent model:** Custom agents built for Tier 3 clients are pushed to Tier 2 at no extra cost.

## 2. Choose the right visual mode

| Mode | Use | Background | Text |

|---|---|---|---|

| **Dark** | Web UI, product apps (Orage Core, Scout), docs, slide decks, PDFs | `#000000` → `#151515` → `#212121` | Tan family: `#FFD69C`, `#FFE8C7` |

| **Light** | Every email, with no exceptions | `#FFFFFF` | Deep brown: `#2C1A00` |

**Non-negotiable:** Never put email content on a dark background. Never put web or product UI on a light background.

## 3. Voice and copy

**Confident · direct · premium · action-led.** Sound like a senior operator making a clear recommendation, not a vendor pitching a feature.

### Do

- Lead with the result, not the feature.

- Use short sentences and strong verbs.

- Be specific; prefer numbers to adjectives.

- Speak to the buyer’s outcome, not the technology.

- Use “we” for the company and “you” for the buyer.

### Don’t

- Use hype: “revolutionary,” “game-changing,” and “next-level” are banned.

- Hedge or apologize.

- Use jargon as decoration.

- Write long; cut every sentence by 30% before shipping.

### Source examples

| Off-brand | On-brand |

|---|---|

| “We’re excited to announce our new AI solution!” | “Your intake team is now 4 people running like 12.” |

| “Cutting-edge automation built on the latest LLMs.” | “STACY answers your phone in 24 hours. Handles 90% of inbound. You review 10%.” |

| “Click here to learn more!” | “Secure my Orage 90 →” |

| “AI will replace your team.” | “AI plus humans, not AI versus humans.” |

**Recurring frames in the source:** AI vs. hiring cost; AI plus humans rather than AI versus humans; first-mover timing; Orage as the filter that supplies a working stack; cost of waiting expressed in lost productive hours. Use claims and numbers only in the contexts supported by the source.

## 4. Typography

**Two fonts only. Never introduce a third.**

| Font | Use | Weight | Rules |

|---|---|---|---|

| **Bebas Neue** | Headings, eyebrow labels, prices, button text | 400 only | Always uppercase; letter spacing 1–6px |

| **Montserrat** | Body, paragraphs, signatures, captions | 500 default; 600 intro; 700 emphasis | Sentence case; line-height 1.6–1.75 |

### Type scale

| Element | Size and treatment |

|---|---|

| H1 hero | 32px; letter spacing 6px |

| H2 section | 26–30px; letter spacing 3px |

| H3 feature | 22–24px; letter spacing 2px |

| Eyebrow label | 11–12px; letter spacing 3–5px |

| Intro / lead | 15px; Montserrat 600 |

| Body copy | 13–14px; Montserrat 500 |

| Caption | 11–12px; Montserrat 700 |

### Font loading and fallbacks

Load Bebas Neue and Montserrat weights 500, 600, 700 from Google Fonts when available. Use these fallback chains so layouts remain stable when remote fonts are unavailable:

```css

font-family: 'Bebas Neue', Impact, 'Anton', 'Oswald', 'Arial Narrow', 'Helvetica Neue Condensed', sans-serif;

font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;

```

## 5. Color system

### Dark mode — web, docs, slides

| Token | Hex | Use from source |

|---|---|---|

| `bg-primary` | `#000000` | Pure black; main body backgrounds |

| `bg-secondary` | `#151515` | Near-black; secondary backgrounds |

| `bg-container` | `#212121` | Dark gray; cards and modals |

| `accent-primary` | `#B68039` | Anchor gold; primary CTAs and titles |

| `accent-highlight` | `#E4AF7A` | Copper/bronze; headings and highlights |

| `accent-highlight-alt` | `#E3C19E` | Optional highlight variation |

| `dark-accent` | `#543C1C` | Deep brown; icons and dividers |

| `text-primary` | `#FFD69C` | Light tan; main body text and labels |

| `text-secondary` | `#FFE8C7` | Soft tan; secondary and input text |

| `text-alt` | `#F5E5D7` | Soft neutral tan |

| `light-utility` | `#FCE8D4` | Light cream; accents and highlights |

### Light mode — email only

| Token | Value | Use from source |

|---|---|---|

| `bg-primary` | `#FFFFFF` | Email body background |

| `feature-box-fill` | `rgba(182,128,57,0.10)` | Feature boxes |

| `code-fill` | `rgba(182,128,57,0.06)` | Code blocks |

| `outer-card-border` | `#D4C4AE` | Outer email-card border |

| `inner-border` | `rgba(182,128,57,0.25)` | Feature borders |

| `hero-divider` | `#B68039` (2px solid) | Hero/footer dividers |

| `accent-primary` | `#B68039` | Buttons, prices, headings |

| `accent-secondary` | `#7A5A2E` | Feature-box headings |

| `accent-tertiary` | `#8C6830` | Eyebrows and secondary CTAs |

| `body-primary` | `#2C1A00` | Headlines and intro paragraphs |

| `body-secondary` | `#3D2500` | Feature-box body copy |

### Color hierarchy

- `#B68039` is the anchor; every Orage artifact has it visible somewhere.

- Use dark-mode `#E4AF7A` and light-mode `#7A5A2E` for headings and emphasis.

- Never use pure black for email body text; use `#2C1A00`.

- Never use pure white in dark mode; use the tan family.

## 6. Email system

Every email uses the light mode. The source defines a fixed component set: combine or repeat these components, but do not invent new ones.

### Feature box

- Fill `rgba(182,128,57,0.10)`; border `1px solid rgba(182,128,57,0.25)`; radius 12px.

- Padding: 25px 22px desktop; 20px 18px mobile.

- Contents: Bebas 11px gold eyebrow → Bebas 22–24px H3 → Montserrat 500, 13–14px body.

### Price box

- Same as a feature box, with a 2px `#B68039` border.

- Use large Bebas price (source example: `$2,500 /MO`), the Bebas eyebrow `ORAGE 90 — AI ENABLED BUSINESS`, and a small Montserrat trust line (`Done-for-you · 90-day performance guarantee`).

### Primary CTA

- One per email, no exceptions.

- Fill `#B68039`; white Bebas Neue uppercase text with 2px letter spacing.

- Padding 16px 32px; radius 4px.

- Follow with an 11px gold trust line.

### Secondary CTA

- Transparent fill; 1px `#B68039` border; `#B68039` uppercase Bebas text.

- Same padding and radius as primary; use inside feature boxes for tertiary actions only.

### Section header

- Eyebrow: Bebas 11px, 5px letter spacing, `#8C6830` (example format: `02 — What's Included`).

- Title: Bebas 26–30px, 3px letter spacing, `#B68039`.

### Email order

1. Header: centered 88px logo; white background; 24px breathing room above and below.

2. Hero: centered gold Bebas H1; finish with a 2px solid `#B68039` divider.

3. Intro: 2–3 short centered paragraphs; Montserrat 600; deep brown.

4. Feature boxes: stack vertically.

5. Price/emphasis: optional; 2px gold border signals highest emphasis.

6. CTA block: centered primary button and trust line.

7. Signature: “Talk soon,” then Bebas name, title, email, and website.

8. Footer: centered small print, copyright and location, with 2px gold top border.

### Email layout and dark-mode resilience

- Email max width: 600px; feature boxes inside max 480px.

- Mobile breakpoint: 500px.

- Outer card radius: 12px; button radius: 4px.

- Primary logo: centered, 88px wide. Source URL: https://assets.cdn.filesafe.space/651kIrlKk834C2FEl66i/media/69b0c2eebfc81fb1ab616b02.png

- Include `color-scheme` and `supported-color-schemes` metadata as shown in the source. In dark-mode media rules, force body/wrapper/mid-backgrounds to white. Inline `background-color: #FFFFFF` on every body `<td>` and `<div>`; wrap for Outlook desktop with `<!--[if mso]>`.

## 7. Non-negotiable rules

1. No emoji in headings, buttons, or labels; `→` is the only allowed glyph.

2. No third typeface: Bebas Neue and Montserrat only.

3. No light backgrounds for web/product UI; dark only.

4. No dark backgrounds for email; light only.

5. No pure-black text in email; use `#2C1A00`.

6. Exactly one `#B68039` primary button per email.

7. No lowercase Bebas; always uppercase and letter-spaced.

8. Email width must not exceed 600px.

9. No hype words such as “revolutionary,” “cutting-edge,” or “game-changing.”

10. No left-aligned email logo; center it at 88px.

11. Body copy is sentence case; Bebas elements are uppercase.

12. No quotation marks for emphasis; use bold or `accent-primary`.

## 8. Source and scope

Primary source: **`BRAND.md` — Orage AI Agency Brand Brief**, identified in the source itself as the single source of truth; last updated 2026-05-05. A legacy visual-guidelines HTML file in Drive conflicts with the current brief on email colors and typography weights. This document follows `BRAND.md` for those topics and does not merge conflicting legacy guidance.

No additional logo-use/clear-space, photography, illustration, accessibility-contrast, or print-production rules are added because the primary source does not specify them.
