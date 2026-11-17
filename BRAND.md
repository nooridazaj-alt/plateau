# PLATEAU

**Your entire video studio, inside one agent.**
*Tout votre studio vidéo, dans un seul agent.*

PLATEAU is a video studio in one agent: six desks (Producer, Brand, Editor, Motion, Talent, Performance) and a seventh, the Receipt, that checks every video before it ships. Open source at github.com/nooridazaj-alt/plateau. Built by AHMADOU O.

## The idea behind the look

*Plateau* is French for a film set: the studio floor where everything gets made. It is also a landform with a flat top, which is the logo: a lilac mesa. Above it sits one coral dot, the **tally light**, the red lamp a camera shows when it is recording. Everything in the system comes from those two images:

- **The set**: deep studio violet, glass panels, soft light. Calm, premium, after-hours.
- **The tally**: one coral signal per view. It means *live*, *act here*, or *stop*. Never decoration.
- **The receipt**: monospace, rows, a stamp. Proof sits next to every promise.

## Voice

Direct, short, receipts-first. We say what it does, then show the proof.

- Do: short declaratives. "One brief in. A finished video out, with a receipt." Numbers with units. A real fail before a pass.
- Do: write French and English as equals. FR uses *vous* in public copy.
- Don't: hype words (revolutionary, insane, game-changer), emoji in product UI, invented testimonials or results, claims without a source.
- Taglines: "Your entire video studio, inside one agent." · "Nothing ships unverified." · FR: "Rien ne sort sans preuve."

## Colour

Two themes. **Studio** (dark violet) is the default and the brand; **Paper** is the light theme for docs and print.

| Role | Token | Rule |
|---|---|---|
| Ground | `surface`, `surface-raised`, `glass` | The set. Studio grounds use a soft radial: `studio` at centre top, `surface` at the edges. |
| Text | `ink`, `ink-muted`, `accent-text` | Headlines run in two lines: first in `ink`, second in `accent-text` ("One agent. / Your entire studio."). |
| Brand | `studio`, `violet`, `lilac` | Large fields and fills. Lilac is the mesa: logo, highlights, second headline line. |
| Signal | `tally`, `on-tally`, `tally-text` | One tally element per view. Text on tally is always `on-tally` (deep ink), never white. |
| State | `pass`, `warn`, `fail` | Product UI and receipts only. Never in marketing art. |

Never: obsidian black grounds, amber, blue-purple gradients, more than one coral element fighting for attention.

## Type

- **Inter Display** for everything people read first: ExtraBold 800, tight tracking (−2.5% to −3%). Headlines are short, sentence case, ending in a full stop.
- **Inter** for body text when Inter Display is unavailable (same metrics).
- **JetBrains Mono** for the machine voice: terminal lines, receipts, counters (`01 / 06`), file names, the eyebrow mark. Load from Google Fonts.
- The eyebrow mark `AHMADOU O.` is mono, 600, tracked 0.24em, in `ink-muted`, centred at the top of every reel and carousel.

## Shape and depth

- Glass cards: `glass` fill, 1.5px `line` border, `radius-lg`, `shadow-glass`.
- Chips, CTAs and buttons are pills (`radius-pill`).
- Spacing on a 4px grid; reels use 72px side margins at 1080 wide.
- No left-border cards, no emoji cards, no stock gradients beyond the studio radial.

## Reels and carousels (1080 × 1920)

- Mark `AHMADOU O.` at the top. Headline at y ≈ 300. Main card starts at y ≈ 540.
- Keep the bottom 20% clear of anything important (platform UI). The CTA sits above it.
- Motion: ease-out entrances (rise 20–40px and fade in), back-ease pops for chips and checks, one stamp slam per video. 30 fps.
- Sound: soft pad and a light kick; a tick on every checkmark; a low hit on the stamp. Master to −14 LUFS, true peak ≤ −1 dB, and run `receipt.py` before posting.

## Logo

- `plateau-lockup.svg`: mark + wordmark, for studio grounds.
- `plateau-mark.svg`: the mesa and tally dot, for avatars and favicons. Clear space: one dot diameter all round.
- `plateau-mark-mono.svg` / `plateau-wordmark.svg`: single ink, set CSS `color`.
- Never recolour the dot to anything but tally, never put the mark on coral, never stretch it.

## Components

Desk chip · Prompt bar · Button · Receipt (rows + stamp) · Terminal. Logos are in `media/brand/`.
