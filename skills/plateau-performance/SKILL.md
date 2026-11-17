---
name: plateau-performance
description: PLATEAU Performance desk: hooks, formats, languages and one-variable variants to test. Use for /performance, "make variants to test", "translate this video".
---

# PLATEAU · 06 PERFORMANCE

Part of PLATEAU (run `/plateau` for the full studio). Read `plateau/<job>/job.json`, write only the `performance` section, and log every paid call in `ledger`.
If there is no job file, create one with the schema in the `plateau` skill.

## 06 PERFORMANCE — hooks, formats, languages · variants to test

1. Pull what is working in the niche right now (vidIQ `vidiq_outliers`, `vidiq_instagram_tiktok_outlier_search`, `vidiq_trending_videos`).
2. Write 6–12 hooks across different angles: pain, curiosity, proof, contrarian, number, demo. Score them (`vidiq_score_title` for titles, Higgsfield `virality_predictor` for finished cuts) and keep the top ones.
3. **Variants to test:** change one variable per variant (hook / first frame / CTA / length / language) so the test can say what worked. Name files `R1_hookB_fr_30s.mp4`.
4. **Languages:** translate the script, regenerate the voice in the same voice (ElevenLabs), re-time the captions, and have a native speaker or the user check any language PLATEAU cannot verify.
5. Write `performance.test_plan`: variants, the one variable each one tests, the metric to watch (3-s hold, completion, CTR), and the kill rule.
