# MHL · 42 — Brand Kit & Design System

Visual identity and design system for **Mostly Harmless** ([mhl42.ai](https://mhl42.ai)). AI security consulting, agentic AI, education, safety, intelligent apps. The identity is a periodic-tile **Element 42** mark in three colours (Ink, Paper, Don't-Panic Gold) set in Inter.

The system is small on purpose. One accent colour, one typeface, one geometric motif (the outline tile). The constraint is the brand.

Open `brand-sheet.html` in a browser for an interactive index of every asset with click-to-download. Open `preview/*.html` for the design-system review cards.

## What's here

```
brand-sheet.html        Interactive index — colors, typography, every mark, download links
README.md               This file — voice, visual foundations, iconography
SKILL.md                Agent Skill manifest — point Claude Code at this repo
colors_and_type.css     Design tokens — color, type, spacing, radii, elevation, motion
presentation-rules.md   Deck-specific rules; supersede the general rules where they conflict
logos/                  17 SVGs — mark, lockups, name lockup, wordmark · light / dark / mono / white
icons/                  App icons (gold + ink, 512px) and favicons (dark + outline)
social/                 OG image, LinkedIn cover, X header, email signature, square avatar
fonts/                  Inter .woff2 — 400 / 500 / 700 / 800, wired via @font-face in the token CSS
site/                   mhl42.ai assets — marks, section icons, OG image, threat-model covers
preview/                18 design-system review cards, one HTML each
ui_kits/website/        mhl42.ai marketing-site recreation, built from live source
png/                    Pre-rendered raster exports at practical sizes
  ├── logos/            256–2000 px
  ├── icons/            16, 32, 64, 192, 256, 512, 1024 px
  └── social/           Native size + 2×
```

## Design tokens

Full token set in [`colors_and_type.css`](./colors_and_type.css). The primitives:

| Token | Value | Use |
|---|---|---|
| `--ink` | `#0E1116` | Primary — strokes, type, dark backgrounds |
| `--paper` | `#FAF6EE` | Bright background, warm off-white pages |
| `--gold` | `#F5C518` | Don't-Panic Gold — single accent, sparingly |
| `--font-sans` | Inter 400 / 500 / 700 / 800 | Display, heading, body, caption |
| `--font-mono` | `ui-monospace` system stack | Identifiers, addresses, code |

The CSS also carries the paper/ink surface scales, semantic fg/bg mappings, the 4px spacing scale, radii, elevation, motion durations and easings, and element-level base styles. Drop it in via `<link>` or paste the `:root` block into a target stylesheet.

## Typography

[Inter](https://rsms.me/inter/) by Rasmus Andersson — open source (SIL Open Font License 1.1). Self-hosted as `.woff2` in `fonts/`, so the system works offline. OpenType features `cv11`, `ss01`, `ss03` are on. Every text element in the SVGs is **outlined to vector paths**, so files render identically anywhere with no font dependency.

## Content fundamentals

The voice is **calm, technical, dryly literary**. The brand is named after *The Hitchhiker's Guide to the Galaxy*, and that influence is allowed to show — but as wit, never as costume.

- **Sentence case** for headings. No title case. No all-caps except for the spaced-tracked caption (`MOSTLY HARMLESS`).
- **First person plural** ("we design, ship, and audit AI systems") for the company; **second person** ("you") only when speaking *to* the reader.
- **Short. Declarative. End with a fact, not a flourish.** "Three colors. That's the system." is the model.
- **Em-dashes and middle-dots** are part of the voice. The product is "MHL · 42", not "MHL-42". Section labels read `01 · Color`, `02 · Typography`.
- **No emoji.** Not in copy, not in UI, not as bullets. Substitute a `·` middle dot, an em dash, or restructure the sentence.
- **Allowed wit:** quietly nerdy callbacks ("Don't-Panic Gold", `<MHL/42>`). Never punchlines. Never exclamation points.
- **Forbidden:** "supercharge", "unlock", "revolutionize", "AI-powered" as filler, "let's", any emoji, gradient hype copy, exclamation marks, "click here".
- **Mono is brand**: `mhl42.ai`, `stefan@mhl42.ai`, `<MHL/42>`. Identifiers, addresses, code references — never body copy.
- **Tone benchmark:** the brand sheet itself. *"Mark + wordmark, horizontal and vertical."* — five words, no flourish, factual.

| Don't | Do |
|---|---|
| Supercharge your AI agents! | We design, ship, and audit AI systems. |
| Click here to learn more → | [Read the audit framework](#) |
| "AI-powered security solutions" | AI security consulting. |
| "We're on a mission to…" | What we do · How we work · Get in touch |
| "Trusted by leading brands" | Selected work · 2023 – present |

## Visual foundations

**Colour.** Three swatches. Paper is warmer than white, closer to a book page. Gold is a **single accent per surface** — the dot on the tile, *or* a callout rule, *or* a link underline. Never two at once.

**Spacing.** 4px base. Scale is `4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 56 / 64 / 80`. Section padding `40px 56px`; header padding `56px 56px 24px`; footer `28px 56px 56px`. Generous gutters; the brand breathes.

**Backgrounds.** Mostly flat. Paper for default surfaces, Ink for inverse panels. **No gradients, no textures, no background images on text content.** The OG and social SVGs use a single dark plate with the mark and a gold dot — that is the maximal background density in the system. Full-bleed imagery is not part of the system.

**Corner radii.** `6px` chips and inline tags · `10px` inputs and small cards · **`14px` the default tile and card radius** · `22px` hero plates · `999px` pills.

**Cards.** 1px hairline border, 14px radius, paper fill, **no shadow**. The bottom label strip is `border-top: 1px solid var(--line); padding: 10px 14px; font-size: 12px; color: var(--fg-2)`. That is the canonical card.

**Borders.** Hairline. `1px solid rgba(14, 17, 22, .12)` is the default divider everywhere. Inset borders on cards, dashed borders between type-line samples, no border on inverse cards. Mark stroke weight is `8px` at 512 — the system reads outline-first.

**Shadows.** Almost none. The card system is border + radius, not shadow. Reserve shadows for floating elements that genuinely need depth (popovers, dropdowns) and keep them small and warm: `0 4px 14px rgba(14, 17, 22, .06)`.

**Transparency and blur.** Sparing. Lines use rgba alpha (`.12`, `.22`). No backdrop blur, no glassmorphism. `rgba(245, 197, 24, .18)` is allowed as a callout fill. Anything beyond that is foreign to the brand.

**Animation.** Restrained. Motion is acknowledgement, not entertainment. Durations `120ms` / `180ms` / `260ms`; anything longer is wrong for this brand. Easing `cubic-bezier(.2, .7, .2, 1)` for incoming elements, `cubic-bezier(.45, 0, .25, 1)` for state changes. **Fades and small translates only.** No bounces, springs, rotation, or scale-from-zero.

**States.** Link hover: dotted underline goes solid, colour shifts ink → gold, no background change. Button hover: primary fills shift one notch warmer, ghost buttons gain a paper-200 wash. Press: one shade darker, **no scale shrink**. Focus: `0 0 0 3px rgba(245, 197, 24, .35)` ring, gold, soft, always visible.

**Layout.** Grids snap to 2 / 3 / 4 columns with `gap: 18px`. Single column at `<= 900px`, gutters drop to `20px`. The mark gets **clear space equal to the height of the "42" caption** on every side. That is the only mandatory whitespace rule.

**Imagery.** Cool, neutral, monochrome preferred. No oversaturated stock. No photography ships on the marketing site today; when introduced, treat photographs as placeholder slots — a neutral inset on paper — rather than full-bleed heroes.

## Element 42 — the mark

Periodic-table tile. Outlined ink stroke, gold dot top-right, "42" caption below the "MHL" glyph. **The tile is always an outline, never filled.** Three forms (with phrase / no phrase / mono) and three colour modes (light / dark / mono). Every other rule traces back to keeping the tile recognisable.

**Do** use the mark with the phrase on first contact (web hero, deck cover, business card front), then drop the phrase for repeat appearances. Use the gold accent for one element per surface.

**Don't** recolour the mark with anything but ink, paper, or gold. Don't add shadows. Don't put the gold dot anywhere except the top-right of the tile. Don't stretch, rotate, or fill the tile interior.

## Iconography

The brand ships **only logo and lockup SVGs**. There is no first-party UI-icon set.

**Substitution policy:** when product UI needs icons (settings, chevrons, search, copy, share), use [Lucide](https://lucide.dev) — same outline-first, single-stroke aesthetic as the mark. Stroke width `1.75`, `currentColor`, 24×24 default. *Flagged substitution — confirm Lucide as the canonical UI icon set or supply your own.*

Allowed: imported SVG logos from this repo; Lucide outline icons; the `·` middle dot and `—` em dash as inline typographic separators; the Element-42 glyph, but only as the actual logo, never as a generic UI icon.

Forbidden: emoji, filled or chunky icon sets (Material filled, Heroicons solid), multi-colour icons, hand-drawn SVG decoration.

## Quick-start picks

| Use | File |
|---|---|
| Website favicon | `icons/favicon.svg` |
| App / GitHub avatar | `png/social/avatar-square-512-512.png` |
| LinkedIn cover | `png/social/linkedin-banner-1584x396-1584.png` |
| X / Twitter header | `png/social/x-header-1500x500-1500.png` |
| Pitch deck cover | `logos/07-lockup-horizontal-light.svg` |
| Email signature | `png/social/email-signature-600x180-1200.png` |
| Open Graph share image | `png/social/og-image-1200x630-1200.png` |
| Design tokens for a new build | `colors_and_type.css` + `fonts/` |

## Using this repo as a Claude skill

[`SKILL.md`](./SKILL.md) is an Agent Skill manifest (`name: mhl42-design`). Point Claude Code at this repo and it will read the rules above, pull tokens from `colors_and_type.css`, and copy assets out when generating branded HTML or production code. For decks, `presentation-rules.md` supersedes the general rules.

## License

See [`LICENSE`](./LICENSE) for the full terms. Short version:

- **Brand assets** (the MHL · 42 mark, wordmark, name "Mostly Harmless", and all derivatives) are © Beyer Ventures, S.L. and reserved. You may reference them editorially; you may not use them to represent another entity, product, or service.
- **Code and document structure** (HTML/CSS in `brand-sheet.html`, `colors_and_type.css`, `preview/`, `ui_kits/`) is MIT-licensed.
- **Inter typography** © The Inter Project Authors, SIL Open Font License 1.1.

Questions, partnerships, trademark matters: info@mhl42.ai
