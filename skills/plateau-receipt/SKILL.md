---
name: plateau-receipt
description: PLATEAU Receipt desk: checks a finished video with receipt.py and stamps it VERIFIED or NOT VERIFIED. Use for /receipt, "verify this video", "check this before I post".
---

# PLATEAU · ✓ RECEIPT

Part of PLATEAU (run `/plateau` for the full studio). Read `plateau/<job>/job.json`, write only the `receipt` section, and log every paid call in `ledger`.
If there is no job file, create one with the schema in the `plateau` skill.

## ✓ RECEIPT — nothing ships unverified

Run checks in code first, then one independent model review of the finished file. The department that made the video cannot mark its own job as passed.

| Check | Pass rule |
|---|---|
| Duration and format | matches `deliverables` ±0.5 s, correct aspect, 30 fps |
| Loudness | −14 LUFS integrated ±1, true peak ≤ −1 dBTP |
| Captions | every spoken word captioned, drift ≤ 120 ms against the transcript |
| Hook | first spoken word before 0.8 s, and something moves on screen within 1.5 s |
| Brand | zero open `brand.violations`, mark present on every scene |
| Claims | every number or claim on screen has a source in `receipt.sources`, or is cut |
| People | every real person shown or quoted has consent noted; every AI presenter disclosed |
| Ledger | total spend under the Producer's ceiling |

Output `receipt.md` with the stamp **VERIFIED** or **NOT VERIFIED — n issues**, the failed rows, and the fix each one needs. Send the user the video and the receipt together.

---

## Run it

```
python3 tools/receipt.py <video.mp4> --job plateau/<job>/job.json [--srt captions.srt] [--target 35] [--aspect 9:16]
```

It writes `receipt.md` next to the video and exits 0 only when every check passes. Code checks come first; then do one independent review of the finished file yourself, looking at 3 frames and listening for problems the script can't hear. Add what you find under `## Reviewer notes`. You cannot flip a NOT VERIFIED stamp to VERIFIED by hand: fix the video and run it again.
