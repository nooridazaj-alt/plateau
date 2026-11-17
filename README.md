<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="media/brand/plateau-lockup.svg">
    <img src="media/brand/plateau-lockup-ink.svg" width="360" alt="PLATEAU">
  </picture>
</p>

<p align="center"><img src="media/hero.gif" width="300" alt="PLATEAU launch reel"></p>

<p align="center"><b>Your entire video studio, inside one agent.</b><br>One brief in. A finished video out, with a receipt.</p>

```
PLATEAU
├─ 01 PRODUCER     brief, questions, plan · rushes to reels
├─ 02 BRAND        logo, fonts, colours · on-brand check on every frame
├─ 03 EDITOR       cuts, captions, reframes · interview to founder film
├─ 04 MOTION       app UI into motion · product launch shots
├─ 05 TALENT       AI actors and avatars · UGC and testimonials
├─ 06 PERFORMANCE  hooks, formats, languages · variants to test
└─ ✓  RECEIPT      every claim, every frame, every cut checked
```

## Why another video agent?

Most "AI video teams" stop when the file renders. PLATEAU adds a seventh desk: the **Receipt**.

`tools/receipt.py` measures the finished file: length, aspect, frame rate, loudness, true peak, how fast the first sound and first motion arrive, caption timing, open brand issues, unsourced claims, consent for real people, and spend. It stamps **VERIFIED** or **NOT VERIFIED**, and the desk that made the video can't stamp its own work.

## Proof: it caught us first

The launch reel above was made with PLATEAU, then checked by it. The first pass **failed**: the soundtrack peaked at −0.9 dBFS (rule: ≤ −1). We fixed the master and ran it again.

| Run | Stamp | |
|---|---|---|
| [`receipt_v1_before.md`](examples/launch-reel/receipt_v1_before.md) | NOT VERIFIED — 1 issue | true peak −0.9 dBFS |
| [`receipt.md`](examples/launch-reel/receipt.md) | **VERIFIED** | EN cut · [R1_en_34s.mp4](examples/launch-reel/R1_en_34s.mp4) |
| [`receipt_fr.md`](examples/launch-reel/receipt_fr.md) | **VERIFIED** | FR cut · [R2_fr_34s.mp4](examples/launch-reel/R2_fr_34s.mp4) |

The full job file, with plan, brand kit, claims and ledger, is in [`examples/launch-reel/job.json`](examples/launch-reel/job.json).

## Eight skills

| Skill | Desk |
|---|---|
| [`plateau`](skills/plateau/SKILL.md) | the studio: runs every desk in order |
| [`plateau-producer`](skills/plateau-producer/SKILL.md) | brief, questions, plan · rushes to reels |
| [`plateau-brand`](skills/plateau-brand/SKILL.md) | brand kit, locked style block, frame check |
| [`plateau-editor`](skills/plateau-editor/SKILL.md) | cuts, captions, reframes, founder film |
| [`plateau-motion`](skills/plateau-motion/SKILL.md) | app UI into motion, launch shots |
| [`plateau-talent`](skills/plateau-talent/SKILL.md) | avatars, voices, UGC, real testimonials only |
| [`plateau-performance`](skills/plateau-performance/SKILL.md) | hooks, languages, variants to test |
| [`plateau-receipt`](skills/plateau-receipt/SKILL.md) | runs `receipt.py` + independent review |

Every job lives in `plateau/<job>/job.json`. Each desk writes only its own section, so every handoff is a contract, and every paid generation goes into a ledger with its cost.

## Install

**Claude Code**
```
git clone https://github.com/nooridazaj-alt/plateau
cp -r plateau/skills/* ~/.claude/skills/
```
Then say *"set up my video team"* or `/plateau`.

**Claude app:** add each folder in `skills/` in Settings → Capabilities → Skills (start with `plateau` and `plateau-receipt`).

**Just the receipt** (needs ffmpeg):
```
python3 tools/receipt.py your_video.mp4 --target 30 --aspect 9:16
```

## Connectors it uses (when you have them)

Higgsfield · ElevenLabs · HeyGen HyperFrames · Figma · Canva · Adobe · Google Drive · Notion · vidIQ · Top_view, plus ffmpeg, Remotion and Whisper.
Missing one? PLATEAU says which, and carries on with the next best tool.

## Brand

Studio violet `#21145A` · violet `#5A3DC0` · lilac `#B9A8FF` · tally coral `#FF5A4E` · paper `#F4F1FF`.
The mark is a mesa (a *plateau*) with one coral dot: the tally light a camera shows when it's recording. One coral element per view, always a signal. Type: Inter Display ExtraBold, JetBrains Mono. Logos in [`media/brand/`](media/brand/), full rules in [`BRAND.md`](BRAND.md).

## House rules

- Real UI, real customers, real numbers. Anything unproven gets cut.
- No invented testimonials. AI actors may only act out a real, consented quote, and it's disclosed.
- Confirm before any big generation. Never blind-retry a paid render.

---

Built by **Ahmadou O.** · [LinkedIn](https://www.linkedin.com/in/ahmadou-ouedraogo-787717345) · MIT License
