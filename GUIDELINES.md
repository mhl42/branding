# Mostly Harmless · brand guidelines

The system is small on purpose. One accent colour, one typeface, one geometric motif, one illustration style. The constraint is the brand.

## 01 · Voice

Mostly Harmless is an AI security consultancy. The writing should sound like a careful engineer explaining something to a peer: calm, concrete, a little dry.

- **Sentence case** for headings. No title case. All-caps only for small mono labels.
- **Headings are statements.** They say what we do or what something is. Not questions, not slogans, not puns.
- **Short sentences. One idea each.** End with a fact, not a flourish.
- **First person plural** for the company ("we review, test and design"). **Second person** only when speaking to the reader.
- **Labels use the middle dot.** `01 · Services`, `MHL · 42`. Never a hyphen in the product name.
- **Em dashes sparingly.** Prefer a full stop or a comma. Middle dots and colons carry most separators.
- **No emoji, no exclamation marks.** Substitute a middle dot or restructure the sentence.
- **Mono is for identifiers**: `mhl42.ai`, `info@mhl42.ai`, code, file names, section labels. Never body copy.
- **Wit is allowed, quietly.** The name is a Hitchhiker's Guide reference and that may show as a callback ("Don't-Panic Gold"). Never as a punchline, never as costume.

Forbidden words: supercharge, unlock, revolutionise, "AI-powered" as filler, "let's", "click here", "trusted by", "on a mission".

| Don't | Do |
|---|---|
| Supercharge your AI agents! | We review, test and design agentic systems. |
| Can this agent cross a boundary? | Agentic system review |
| Click here to learn more → | Read the guidelines |
| AI-powered security solutions | AI security consulting |

## 02 · Colour

Three colours. Every surface is Paper or Ink. Gold is an accent, never a surface for text.

| Token | Value | Use |
|---|---|---|
| Ink | `#0E1116` | Strokes, type, dark panels |
| Paper | `#FAF6EE` | Page background. Warmer than white, closer to a book page |
| Don't-Panic Gold | `#F5C518` | The dot on the tile, one accent per surface |

Rules:

- **One gold element per surface.** The dot on the mark, or a label, or a callout rule, or a link underline. Never two at once.
- **Text on Gold is always Ink.** Never Paper on Gold.
- Secondary text is Ink at 68 % opacity; muted text and labels at 48 %. On Ink panels, body text is Paper at 74 %, headings at full Paper.
- Dividers are hairlines: Ink at 14 % on Paper, Paper at 16 % on Ink.
- No gradients, no textures, no tints beyond the paper and ink scales in `tokens.css`.

## 03 · Typography

[Inter](https://rsms.me/inter/), self-hosted from `fonts/`, weights 400 / 500 / 700 / 800, with OpenType features `cv11`, `ss01`, `ss03` on.

- **Display and headings**: weight 800, tight leading (1.05), letter-spacing from −0.035em to −0.045em at large sizes.
- **Body**: 16 to 17px, weight 400, leading 1.6.
- **Labels and captions**: system mono, 10 to 12px, uppercase, letter-spacing 0.1 to 0.12em.
- **Buttons and navigation**: 14px, weight 700 or 500.

Every SVG in this repo has its text outlined to paths, so the font is not needed to render the assets.

## 04 · The mark

*Element 42* is a periodic-table tile: an outlined Ink stroke, the glyph `MHL`, the caption `42`, and a gold dot in the top-right corner.

- **The tile is always an outline.** Never filled, never given a shadow.
- **Only Ink, Paper or Gold.** No other colour, no gradients.
- **The gold dot stays top-right.** Do not move, resize or duplicate it.
- **Do not stretch, rotate or crop** the tile.
- **Clear space** on every side equals the height of the `42` caption. This is the only mandatory whitespace rule.
- **First contact uses the mark with the phrase** (hero, deck cover, business card). Repeat appearances drop the phrase (favicon, app chrome, footer).
- **One lockup per surface.** A page or slide carries either the tile or the wordmark, never both.
- **Ship light and dark versions as a pair** and switch with CSS. Never invert an SVG with a filter.

Forms: mark with phrase, mark without phrase, mono; lockups horizontal and vertical; name lockup ("Mostly Harmless" without the domain); wordmark. All in `logos/`, numbered.

## 05 · Illustrations

The website uses editorial line illustrations. They are the only imagery in the system. No stock photography, no 3D renders, no abstract gradients.

- **Black ink line drawing** on Paper or on Ink. Hatching and dashed lines for motion and boundaries.
- **One gold element** per illustration, placed on the control that matters: the stop sign, the approval point, the scoped key.
- **The scene shows a mechanism**: an untrusted input reaching an agent, an approval before a consequential action, a finding becoming a test. Not decoration.
- **Framed, never full-bleed.** Hairline border, 14px radius, a mono caption strip below naming the two or three stages shown.
- Files in `illustrations/` are the current set. New ones follow the same style and the same framing.

## 06 · Layout and components

- **Spacing** on a 4px base. Section padding runs from 64px on small screens to 120px on large ones. Gutters from 20px to 64px.
- **Radii**: 6px chips, 10px inputs, **14px cards and tiles**, 22px hero plates, 999px pills.
- **Cards** are a hairline border, 14px radius, Paper fill, **no shadow**. On Ink panels, the border is Paper at 16 %.
- **Section labels** sit above the heading: mono, uppercase, numbered (`01 · Services`). Gold on Ink, muted Ink on Paper.
- **Lists of services or items** are rows separated by hairlines, with a mono index on the left, not floating cards.
- **Buttons** are pills, 48px tall. Primary is Ink on Paper; on Ink panels use Gold with Ink text or a Paper outline.
- **Links** in body copy use a dotted underline that turns solid on hover. No colour change.
- **Focus rings** are gold at 45 %, three pixels, always visible.
- **Motion** is acknowledgement, not entertainment. 120 to 260ms, fades and small translates only. No bounces, no scale-from-zero.
- **UI icons**, where product work needs them, come from [Lucide](https://lucide.dev): outline, stroke 1.75, `currentColor`. No filled or multi-colour icon sets. The tile is a logo, never a generic icon.

## 07 · Presentations

The rules above apply. In decks, additionally:

- Body text at 1920 × 1080 is at least 24px; labels at least 22px. Large numerals stay large; reflow the layout rather than shrinking them.
- One lockup per slide. The cover carries the tile or the wordmark, never both.
- The gold dot lives in card chrome (top-right of a tile), never over typography. One dot per card.
- Product or hardware photography, if ever used, is contained on an Ink panel at 16:9, not cropped to fill.
- QR codes are static SVG, Ink on Paper, with the URL captioned below in mono.

## 08 · Do and don't

| Do | Don't |
|---|---|
| Use the tile in outline on Paper or Ink | Fill the tile, add a shadow, or recolour it |
| Give the tile clear space equal to the `42` caption | Crowd the mark with other elements |
| Use Gold for one element per surface | Use Gold as a background for text |
| Write headings as plain statements | Write headings as questions or slogans |
| Frame illustrations with a hairline and caption | Run imagery full-bleed behind text |
| Set labels in mono with a middle dot | Use hyphens or title case in labels |
