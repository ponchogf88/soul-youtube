#!/usr/bin/env python3
"""Synthesize M01 locution with DON MARIO. One request per cycle, then concat."""
from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path("/Users/imac/Desktop/Projects/YOUTUBE CHANNEL")
SRC = ROOT / "SOUL_CORE/03_WORKFLOWS/LOCUCION_M01_15MIN.md"
OUT_DIR = ROOT / "MAQUILA/01_MORNING_M01/DON_MARIO"
CHUNKS = OUT_DIR / "chunks"
MASTER = ROOT / "MAQUILA/01_MORNING_M01/LOCUCION_M01_DON_MARIO.mp3"
SHORT = ROOT / "MAQUILA/01_MORNING_M01/SHORT_SAMPLE_CYCLE03_DON_MARIO.mp3"
VOICE_ID = "k0cKCpdFDYiojW6PwPrO"
MODEL = "eleven_multilingual_v2"

PAYLOAD_SETTINGS = {
    "stability": 0.80,
    "similarity_boost": 0.78,
    "style": 0.08,
    "use_speaker_boost": True,
    "speed": 0.96,
}


def keys() -> list[str]:
    text = pathlib.Path("/Users/imac/Desktop/apis.txt").read_text()
    found = re.findall(r"ELEVENLABS_API_KEY=(\S+)", text)
    # maquila fallbacks if present later in file
    extra = re.findall(r"sk_[0-9a-f]{40,}", pathlib.Path(ROOT / "MAQUILA/run_autonomous_production.py").read_text())
    out = []
    for k in found + extra:
        if k not in out:
            out.append(k)
    if not out:
        sys.exit("no elevenlabs key")
    return out


def spoken_cycles(md: str) -> list[tuple[str, str]]:
    body = md.split("## Texto hablado", 1)[1].split("## Corte Short", 1)[0]
    parts = re.split(r"<!--\s*(CYCLE_\d+|CIERRE).*?-->", body)
    # split keeps delimiters when using capturing groups: [pre, label, text, label, text...]
    cycles = []
    i = 1
    while i < len(parts) - 1:
        label = parts[i].strip()
        text = parts[i + 1]
        text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        text = text.replace("\u00a0", " ")
        # spoken line breaks → pause-friendly
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        if text:
            cycles.append((label, text))
        i += 2
    return cycles


def tts(text: str, dest: pathlib.Path, keyring: list[str]) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "text": text,
        "model_id": MODEL,
        "voice_settings": PAYLOAD_SETTINGS,
    }
    last = None
    for key in keyring:
        req = urllib.request.Request(
            f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}?output_format=mp3_44100_128",
            data=json.dumps(payload).encode("utf-8"),
            method="POST",
            headers={
                "xi-api-key": key,
                "Content-Type": "application/json",
                "Accept": "audio/mpeg",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                dest.write_bytes(resp.read())
            if dest.stat().st_size < 2000:
                raise RuntimeError("tiny audio")
            return
        except Exception as e:
            last = e
            continue
    raise RuntimeError(f"tts failed: {last}")


def duration(path: pathlib.Path) -> float:
    p = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    return float(p.stdout.strip())


def silence(path: pathlib.Path, seconds: float) -> None:
    subprocess.run(
        [
            "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
            "-t", str(seconds), "-c:a", "libmp3lame", "-q:a", "4", str(path),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def concat(files: list[pathlib.Path], dest: pathlib.Path) -> None:
    lst = dest.with_suffix(".concat.txt")
    lst.write_text("".join(f"file '{p.resolve()}'\n" for p in files))
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(dest)],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CHUNKS.mkdir(parents=True, exist_ok=True)
    md = SRC.read_text()
    cycles = spoken_cycles(md)
    if len(cycles) < 7:
        sys.exit(f"expected >=7 cycles, got {len(cycles)}: {[c[0] for c in cycles]}")
    keyring = keys()
    print(f"cycles={len(cycles)} keys={len(keyring)}")

    sil_open = CHUNKS / "sil_open_8s.mp3"
    sil_gap = CHUNKS / "sil_gap_0p7.mp3"
    silence(sil_open, 8.0)
    silence(sil_gap, 0.7)

    audio_files = [sil_open]
    report = []
    for idx, (label, text) in enumerate(cycles, 1):
        chunk = CHUNKS / f"{idx:02d}_{label}.mp3"
        print(f"TTS {label} chars={len(text)} words={len(text.split())}")
        tts(text, chunk, keyring)
        d = duration(chunk)
        report.append(f"{label}\t{d:.2f}s\t{len(text)}c")
        print(f"  -> {d:.2f}s")
        audio_files.append(chunk)
        if idx < len(cycles):
            audio_files.append(sil_gap)

    concat(audio_files, MASTER)
    master_dur = duration(MASTER)

    # Short sample: first ~22s of cycle 03 (file 03)
    c3 = next(CHUNKS.glob("*CYCLE_03*.mp3"), None)
    if c3:
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(c3), "-t", "22", "-c:a", "libmp3lame", "-q:a", "3", str(SHORT)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    qa = {
        "voice": "DON MARIO",
        "voice_id": VOICE_ID,
        "master": str(MASTER),
        "duration_seconds": round(master_dur, 2),
        "cycles": report,
        "bytes": MASTER.stat().st_size,
        "target": "14:30–15:30 plus 8s atmosphere",
        "pass_duration": 13.5 <= master_dur <= 17.5,
        "pass_file": MASTER.stat().st_size > 100_000,
    }
    (OUT_DIR / "QA.json").write_text(json.dumps(qa, indent=2, ensure_ascii=False))
    print(json.dumps(qa, indent=2, ensure_ascii=False))
    if not (qa["pass_duration"] and qa["pass_file"]):
        sys.exit("QA FAIL")


if __name__ == "__main__":
    main()
