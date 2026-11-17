---
name: plateau-brand
description: PLATEAU Brand desk: loads logo, fonts, colours into a brand kit and locked style block, then checks every frame on-brand. Use for /brand or "check this is on-brand".
---

# PLATEAU · 02 BRAND

Part of PLATEAU (run `/plateau` for the full studio). Read `plateau/<job>/job.json`, write only the `brand` section, and log every paid call in `ledger`.
If there is no job file, create one with the schema in the `plateau` skill.

## 02 BRAND — logo, fonts, colours · on-brand check on every frame

1. Load the brand kit: a Figma file (`get_variable_defs`, `get_design_context`), Canva, an ElevenLabs brand kit (`creative_get_brand_kit`, or `creative_create_brand_kit_from_website` from a URL), or the user's design system. If no kit exists, build one from their site and ask them to confirm it once.
2. Write `brand.kit`: hex palette, fonts with fallbacks, logo files, safe zones, caption style, banned words, voice and tone in 3 lines, and the mark that sits on every video (for Ahmadou: "AHMADOU O.").
3. Write one **locked style block**: a paragraph pasted unchanged into every image and video prompt so scenes match.
4. **On-brand check (runs again after Editor and Motion):** sample one frame per second, and for each frame check palette distance from the kit, logo present and inside safe zones, captions in brand font, nothing in the banned list. Write failures with timestamps to `brand.violations`. Any violation sends that scene back to its department.
