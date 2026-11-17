---
name: plateau-producer
description: PLATEAU Producer desk: turns a brief or raw rushes into a plan, scene list and selects. Use for /producer, "plan this video", "turn these rushes into reels".
---

# PLATEAU · 01 PRODUCER

Part of PLATEAU (run `/plateau` for the full studio). Read `plateau/<job>/job.json`, write only the `producer` section, and log every paid call in `ledger`.
If there is no job file, create one with the schema in the `plateau` skill.

## 01 PRODUCER — brief, questions, plan

1. Read the brief and any attached rushes, scripts, decks or links.
2. Ask at most 3 questions, only ones whose answer changes the plan: audience, platform, CTA, deadline, language. If the user is away, take the most reasonable reading and write it in `producer.assumptions`.
3. Write the plan: deliverables, running order (scene list with intent `hook | proof | turn | payoff`), which departments run, budget ceiling in credits.
4. **Rushes to Reels mode:** when the input is raw footage, transcribe it (ElevenLabs `creative_transcribe_audio`, or local Whisper), score every sentence for hook strength and standalone sense, and pick the 3–5 strongest self-contained moments (20–60 s each). Write their in/out timecodes to `producer.selects`.

Handoff: `producer.plan` with scenes, each one with its intent, duration, and source (rush / generated / motion / avatar).
