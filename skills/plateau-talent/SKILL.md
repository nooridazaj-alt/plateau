---
name: plateau-talent
description: PLATEAU Talent desk: AI presenters, avatars and voices, UGC-style scripts, with hard rules on real testimonials and disclosure. Use for /talent or "add an AI presenter".
---

# PLATEAU · 05 TALENT

Part of PLATEAU (run `/plateau` for the full studio). Read `plateau/<job>/job.json`, write only the `talent` section, and log every paid call in `ledger`.
If there is no job file, create one with the schema in the `plateau` skill.

## 05 TALENT — AI actors and avatars · UGC and testimonials

- **Avatars and presenters:** the user's own avatar first (HeyGen HyperFrames, Higgsfield `ai_influencer_*`, Top_view `topview_avatar_video`). Voice from ElevenLabs (`creative_list_voices`, or the user's cloned voice).
- **UGC style:** phone framing, natural light, handheld, one product in hand, a hook in the first line.
- **Testimonials rule (hard):** a testimonial must come from a real customer with their consent and their real words. Never invent a customer, a quote, a review or a result, and never present an AI actor as a real buyer. AI actors may *act out* a real, consented quote only if the video discloses it ("dramatised with AI"). If no real testimonial exists, write a product demo or a founder-voice script instead.
- Disclose AI presenters wherever the platform requires it (Meta, TikTok and YouTube all have a label setting).
