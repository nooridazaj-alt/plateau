---
name: plateau-motion
description: PLATEAU Motion desk: animates real app UI and makes product launch shots. Use for /motion, "animate our app screens", "launch shots for this product".
---

# PLATEAU · 04 MOTION

Part of PLATEAU (run `/plateau` for the full studio). Read `plateau/<job>/job.json`, write only the `motion` section, and log every paid call in `ledger`.
If there is no job file, create one with the schema in the `plateau` skill.

## 04 MOTION — app UI into motion · product launch shots

- **App UI into motion:** take screens from Figma (`get_screenshot`) or uploads, rebuild them as layers (HTML/Remotion or HyperFrames `compose`), then animate: scroll-through, tap highlights, number counters, a camera push on the key element. Real UI only: never invent a feature the product does not have.
- **Product launch shots:** packshot → 3–6 hero shots (Higgsfield `generate_video` image-to-video, or `ads_studio_generate` with the product added once by `ads_studio_add_product`): orbit, macro detail, reveal, in-hand, in-context.
- Every prompt carries the Brand locked style block.
