---
name: plateau
description: PLATEAU, the whole video studio in one agent: one brief in, a finished, receipted video out via Producer, Brand, Editor, Motion, Talent, Performance + Receipt. Use for /plateau or 'set up my video team'.
---


# PLATEAU — your entire video studio, inside one agent

One brief in. A finished video out, with a receipt.
Six departments, run in order. Each one hands the next a written contract, never a vibe.
The seventh desk, the Receipt, signs off at the end. Nothing ships as VERIFIED unless it passes.

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

Why this beats a folder of prompts: every handoff is a contract (`plateau/job.json`), every generation is logged with its cost, and the Receipt desk can fail the job. The generator never grants itself "done".

---

## 0. The job file

Create `plateau/<job-slug>/job.json` at the start. Every department reads it and writes only its own section.

```json
{
  "job": "slug",
  "brief": "the user's words, verbatim",
  "deliverables": [{"id": "R1", "format": "9:16", "duration_s": 35, "language": "fr"}],
  "producer": {}, "brand": {}, "editor": {}, "motion": {},
  "talent": {}, "performance": {}, "receipt": {},
  "ledger": []
}
```

`ledger` gets one line per paid generation or tool call: `{dept, tool, model, input_ref, output_ref, credits_or_cost, kept: true|false}`.

Skip a department when the brief does not need it, and write `"skipped": "reason"` in its section. Never skip Brand or Receipt.

---


## Run order

Load each desk's skill when its turn comes, and follow it:

| # | Desk | Skill | Does |
|---|---|---|---|
| 01 | Producer | `plateau-producer` | brief, questions, plan · rushes to reels |
| 02 | Brand | `plateau-brand` | brand kit, locked style block, frame check |
| 03 | Editor | `plateau-editor` | cuts, captions, reframes, founder film |
| 04 | Motion | `plateau-motion` | app UI into motion, launch shots |
| 05 | Talent | `plateau-talent` | avatars, voices, UGC, real testimonials only |
| 06 | Performance | `plateau-performance` | hooks, languages, variants to test |
| ✓ | Receipt | `plateau-receipt` | `tools/receipt.py` + independent review → VERIFIED / NOT VERIFIED |

Brand's frame check runs again after Editor and Motion. Any violation sends the scene back. Receipt always runs last, and the desk that made the video never stamps it.

If the desk skills are not installed, the full instructions for every desk are in the repo: github.com/nooridazaj-alt/plateau.

## Connectors PLATEAU uses (when connected)

| Desk | Tools |
|---|---|
| Producer | Google Drive, Notion (briefs, rushes), ElevenLabs transcription |
| Brand | Figma, Canva, Adobe, ElevenLabs brand kits |
| Editor | ffmpeg, Remotion, Higgsfield reframe/upscale, Adobe video tools |
| Motion | HyperFrames by HeyGen, Higgsfield video, Figma screenshots |
| Talent | HeyGen, Higgsfield AI influencer, Top_view avatars, ElevenLabs voices |
| Performance | vidIQ, Higgsfield virality predictor, ElevenLabs multilingual voice |

If a needed connector is missing, say which one and carry on with the next best tool. Never stop the job over one missing tool.

## Rules

- Confirm with the user before any single generation over 50 credits, and before any long video render.
- Never retry a paid generation blindly: read why it failed first, and log every attempt in the ledger.
- Real UI, real customers, real numbers. Anything unproven gets cut, not softened.
- One render per deliverable: check 3 full-size frames at the busiest moments before the full render.
