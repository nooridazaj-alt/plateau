#!/usr/bin/env python3
"""PLATEAU receipt: checks a finished video and stamps it VERIFIED or NOT VERIFIED.

usage: python3 receipt.py video.mp4 [--job job.json] [--srt captions.srt]
                          [--target SECONDS] [--aspect 9:16] [--out receipt.md]
needs: ffmpeg + ffprobe on PATH. No other dependencies.
exit code 0 only when every check passes.
"""
import argparse, json, re, subprocess, sys, datetime, os


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def probe(path):
    r = run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path])
    if r.returncode:
        sys.exit(f"cannot read {path}: {r.stderr.strip()}")
    return json.loads(r.stdout)


def loudness(path):
    r = run(["ffmpeg", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"])
    s = r.stderr.split("Summary:")[-1]
    i = re.search(r"I:\s+(-?[\d.]+) LUFS", s)
    tp = re.search(r"Peak:\s+(-?[\d.]+) dBFS", s)
    return (float(i.group(1)) if i else None, float(tp.group(1)) if tp else None)


def first_sound(path, thresh=-45):
    """seconds until the audio first rises above the silence threshold"""
    r = run(["ffmpeg", "-nostats", "-i", path, "-af", f"silencedetect=n={thresh}dB:d=0.05", "-f", "null", "-"])
    starts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    if not starts or starts[0] > 0.05:
        return 0.0
    return ends[0] if ends else None


def first_motion(path, limit=3.0):
    """seconds until the picture visibly changes"""
    # compare small greyscale frames (10 per second) against the first frame,
    # so slow fades and drifting titles count as motion, not just hard cuts
    fw, fh, rate = 48, 85, 10
    r = subprocess.run(["ffmpeg", "-v", "error", "-t", str(limit), "-i", path, "-vf",
                        f"fps={rate},scale={fw}:{fh},format=gray", "-f", "rawvideo", "-"],
                       capture_output=True)
    data, n = r.stdout, fw * fh
    frames = [data[k:k + n] for k in range(0, len(data) - n + 1, n)]
    if not frames:
        return None
    first = frames[0]
    for idx, f in enumerate(frames[1:], 1):
        changed = sum(1 for a, b in zip(first, f) if abs(a - b) > 12)
        if changed / n > 0.005:
            return idx / rate
    return None


def srt_times(path):
    txt = open(path, encoding="utf-8").read()
    def sec(h, m, s, ms): return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000
    found = re.findall(r"(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,.](\d+)", txt)
    return [(sec(*m[:4]), sec(*m[4:])) for m in found]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--job")
    ap.add_argument("--srt")
    ap.add_argument("--target", type=float)
    ap.add_argument("--aspect")
    ap.add_argument("--out")
    a = ap.parse_args()

    job = json.load(open(a.job)) if a.job else {}
    deliv = (job.get("deliverables") or [{}])[0]
    target = a.target or deliv.get("duration_s")
    aspect = a.aspect or deliv.get("format")

    info = probe(a.video)
    v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    au = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    dur = float(info["format"]["duration"])
    rows = []  # (check, measured, rule, ok)

    def add(name, measured, rule, ok):
        rows.append((name, measured, rule, ok))

    # format
    if target:
        add("Duration", f"{dur:.2f} s", f"{target} s ±0.5", abs(dur - target) <= 0.5)
    else:
        add("Duration", f"{dur:.2f} s", "no target set", True)
    w, h = int(v["width"]), int(v["height"])
    num, den = map(int, v["r_frame_rate"].split("/"))
    fps = num / den
    if aspect:
        aw, ah = map(int, aspect.split(":"))
        add("Aspect", f"{w}×{h}", aspect, abs(w / h - aw / ah) < 0.01)
    add("Frame rate", f"{fps:.2f} fps", "30 fps", abs(fps - 30) < 0.05)

    # sound
    if au:
        i, tp = loudness(a.video)
        add("Loudness", f"{i} LUFS", "−14 ±1 LUFS", i is not None and abs(i + 14) <= 1)
        add("True peak", f"{tp} dBFS", "≤ −1 dBTP", tp is not None and tp <= -1.0)
        fs = first_sound(a.video)
        add("Hook · first sound", f"{fs:.2f} s" if fs is not None else "never", "≤ 0.8 s",
            fs is not None and fs <= 0.8)
    else:
        add("Audio track", "none", "required", False)

    fm = first_motion(a.video)
    add("Hook · first motion", f"{fm:.2f} s" if fm is not None else "none in 3 s", "≤ 1.5 s",
        fm is not None and fm <= 1.5)

    # captions
    if a.srt:
        cues = srt_times(a.srt)
        late = [c for c in cues if c[1] > dur + 0.12]
        add("Captions", f"{len(cues)} cues, {len(late)} past end", "all cues inside the video",
            bool(cues) and not late)

    # job-file checks
    if job:
        bv = job.get("brand", {}).get("violations", [])
        add("Brand", f"{len(bv)} open violations", "0", not bv)
        claims = job.get("receipt", {}).get("claims", [])
        unsourced = [c for c in claims if not c.get("source")]
        add("Claims", f"{len(claims) - len(unsourced)}/{len(claims)} sourced", "all sourced", not unsourced)
        people = job.get("talent", {}).get("people", [])
        bad = [p for p in people if not (p.get("consent") or p.get("ai_disclosed"))]
        add("People", f"{len(people) - len(bad)}/{len(people)} cleared", "consent or AI disclosure", not bad)
        ledger = job.get("ledger", [])
        spent = sum(float(x.get("credits_or_cost") or 0) for x in ledger)
        ceiling = job.get("producer", {}).get("budget_ceiling")
        add("Spend", f"{spent:g}" + (f" / {ceiling}" if ceiling else ""), "under ceiling",
            ceiling is None or spent <= float(ceiling))

    fails = [r for r in rows if not r[3]]
    stamp = "VERIFIED" if not fails else f"NOT VERIFIED — {len(fails)} issue{'s' * (len(fails) > 1)}"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    md = [f"# Receipt · {os.path.basename(a.video)}", "", f"**{stamp}**", "", f"checked {now} by PLATEAU receipt.py", "",
          "| Check | Measured | Rule | |", "|---|---|---|---|"]
    md += [f"| {n} | {m} | {r} | {'✓' if ok else '✕'} |" for n, m, r, ok in rows]
    if fails:
        md += ["", "## To fix"] + [f"- **{n}**: measured {m}, needs {r}" for n, m, r, _ in fails]
    md += ["", "## Reviewer notes", "", "_Independent review of the finished file goes here._", ""]
    out = a.out or os.path.splitext(a.video)[0] + ".receipt.md"
    open(out, "w", encoding="utf-8").write("\n".join(md))
    print("\n".join(md[:4 + 4 + len(rows)]))
    print(f"\nwritten: {out}")
    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
