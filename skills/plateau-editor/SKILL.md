---
name: plateau-editor
description: PLATEAU Editor desk: cuts, word-level captions, reframes, and interview-to-founder-film edits. Use for /editor, "cut this", "caption this", "make a founder film".
---

# PLATEAU · 03 EDITOR

Part of PLATEAU (run `/plateau` for the full studio). Read `plateau/<job>/job.json`, write only the `editor` section, and log every paid call in `ledger`.
If there is no job file, create one with the schema in the `plateau` skill.

## 03 EDITOR — cuts, captions, reframes · interview to founder film

- **Cuts:** cut on sentence ends and beats, remove silences over 0.4 s, filler words, and false starts. First 1.5 s must already be the hook.
- **Captions:** word-level timestamps, at most 3 words on screen, brand font, active word highlighted in the accent colour, nothing inside the platform UI zones (top 12%, bottom 20%, right 15% on 9:16).
- **Reframes:** 16:9 → 9:16 / 1:1 / 4:5 keeping the speaker's face in the upper third (Higgsfield `reframe`, or ffmpeg crop with face tracking).
- **Interview to founder film:** build an arc from the interview (problem → why me → what we built → proof → where we're going), add lower-third name and title, B-roll over every jump cut, and music ducked under speech by −14 dB.
- Assemble with ffmpeg (one encoded file per scene, concat with `-c copy`, audio last) or Remotion when the job needs data-driven motion.

Handoff: `editor.timeline` (scene files, timecodes, caption file path).
