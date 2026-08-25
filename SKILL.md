---
name: mhl42-design
description: Use this skill to generate well-branded interfaces and assets for Mostly Harmless (MHL · 42), either for production or throwaway prototypes/mocks/etc. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping.
user-invocable: true
---

Read the README.md file within this skill, and explore the other available files.

If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.

If the user invokes this skill without any other guidance, ask them what they want to build or design, ask some questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.

## Quick orientation

- `README.md` — voice, content fundamentals, visual foundations, iconography rules.
- `colors_and_type.css` — copy this in. CSS custom properties for color, type, spacing, motion. Drop it in via `<link>` or paste the `:root` block into the target stylesheet.
- `logos/` — 14 SVG logo variants (mark / lockup / wordmark · light / dark / mono). Always SVG-first.
- `fonts/` — Inter `.woff2` (400 / 500 / 700 / 800) — wired via `@font-face` in `colors_and_type.css`.
- `icons/` — app icons + favicons.
- `social/` — OG image, LinkedIn, X, email signature, avatar.
- `preview/` — design-system review cards (one HTML each).
- `ui_kits/website/` — the marketing-site recreation; `index.html` shows it click-thru, components are small JSX files.

## Hard rules

- Three colors. Ink `#0E1116`, Paper `#FAF6EE`, Don't-Panic Gold `#F5C518`. Gold is **one element per surface**.
- Inter, weights 400 / 500 / 700 / 800. Sentence case headings, mono for identifiers.
- **No emoji. No gradients. No drop shadows on cards.** Border + 14px radius is the card.
- The Element-42 tile is always an outline. Never recolour, fill, rotate, or move the gold dot.
- Lucide is the substituted UI icon set (flagged) — outline-first, stroke `1.75`, `currentColor`.

## Presentation rules

When building decks, also read **`presentation-rules.md`** — it captures real
deck-review corrections (Paper-text-on-Gold ban, single-lockup-per-slide,
24px / 22px / 80px floors at 1920×1080, gold-dot placement, theme-pair lockups
without `filter: invert()`, QR rules, tweaks-panel form). The presentation
rules supersede the general rules where they conflict.
