#!/usr/bin/env python3
"""Build M01 90-min vigilia: DON MARIO cycles + beds + looped scene + BGM."""
from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys
import urllib.request

ROOT = pathlib.Path("/Users/imac/Desktop/Projects/YOUTUBE CHANNEL")
SRC = ROOT / "SOUL_CORE/03_WORKFLOWS/LOCUCION_M01_90MIN.md"
OUT = ROOT / "MAQUILA/01_MORNING_M01/M01_90MIN"
CHUNKS = OUT / "chunks"
VOICE_ID = "k0cKCpdFDYiojW6PwPrO"
TARGET = 90 * 60
OPEN_S = 20.0
STAY_S = 9 * 60 + 40  # 80:20–90:00
BGM = ROOT / "SPIRITUALLY/STACK/VOZ/bgm_sacred_final.aac"
VIDEO = ROOT / "MAQUILA/01_MORNING_M01/cinematica_fondo_m01.mp4"
MASTER_A = OUT / "LOCUCION_M01_DON_MARIO_90.m4a"
MASTER_V = OUT / "VIDEO_M01_90MIN.mp4"
CHAPTERS = OUT / "CHAPTERS.txt"

SETTINGS = {
    "stability": 0.80,
    "similarity_boost": 0.78,
    "style": 0.08,
    "use_speaker_boost": True,
    "speed": 0.96,
}


def keys() -> list[str]:
    text = pathlib.Path("/Users/imac/Desktop/apis.txt").read_text()
    found = re.findall(r"ELEVENLABS_API_KEY=(\S+)", text)
    extra = re.findall(r"sk_[0-9a-f]{40,}", (ROOT / "MAQUILA/run_autonomous_production.py").read_text())
    out = []
    for k in found + extra:
        if k not in out:
            out.append(k)
    return out


def cycles(md: str) -> list[tuple[str, str]]:
    body = md.split("## Texto hablado", 1)[1].split("## Corte Short", 1)[0]
    parts = re.split(r"<!--\s*(C\d+)\s*-->", body)
    out = []
    i = 1
    while i < len(parts) - 1:
        out.append((parts[i].strip(), parts[i + 1].strip()))
        i += 2
    return out


def tts(text: str, dest: pathlib.Path, keyring: list[str]) -> None:
    payload = {"text": text, "model_id": "eleven_multilingual_v2", "voice_settings": SETTINGS}
    last = None
    for key in keyring:
        req = urllib.request.Request(
            f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}?output_format=mp3_44100_128",
            data=json.dumps(payload).encode(),
            method="POST",
            headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"},
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                dest.write_bytes(resp.read())
            if dest.stat().st_size < 2000:
                raise RuntimeError("tiny")
            return
        except Exception as e:
            last = e
    raise RuntimeError(last)


def dur(path: pathlib.Path) -> float:
    p = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True, check=True,
    )
    return float(p.stdout.strip())


def run(cmd: list[str]) -> None:
    r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-800:])


def sil(path: pathlib.Path, seconds: float) -> None:
    run([
        "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
        "-t", f"{seconds:.3f}", "-c:a", "libmp3lame", "-q:a", "4", str(path),
    ])


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    CHUNKS.mkdir(parents=True, exist_ok=True)
    keyring = keys()
    cyc = cycles(SRC.read_text())
    print(f"cycles={len(cyc)} keys={len(keyring)}")
    reports = []
    voice_files = []
    for i, (lab, text) in enumerate(cyc, 1):
        chunk = CHUNKS / f"{i:02d}_{lab}.mp3"
        if not chunk.exists() or chunk.stat().st_size < 2000:
            print(f"TTS {lab} chars={len(text)}")
            tts(text, chunk, keyring)
        d = dur(chunk)
        reports.append({"id": lab, "seconds": round(d, 2), "chars": len(text)})
        print(f"  {lab} {d:.2f}s")
        voice_files.append(chunk)

    speech = sum(x["seconds"] for x in reports)
    n_gaps = max(len(voice_files) - 1, 1)
    remain = TARGET - OPEN_S - speech - STAY_S
    if remain < n_gaps * 8:
        # shrink stay to keep minimum beds
        stay = max(120.0, TARGET - OPEN_S - speech - n_gaps * 90)
        remain = TARGET - OPEN_S - speech - stay
    else:
        stay = STAY_S
    gap = max(8.0, remain / n_gaps)
    print(f"speech={speech:.1f}s gap={gap:.1f}s stay={stay:.1f}s total={OPEN_S+speech+gap*n_gaps+stay:.1f}")

    sil_open = CHUNKS / "sil_open.mp3"
    sil_gap = CHUNKS / "sil_gap.mp3"
    sil_stay = CHUNKS / "sil_stay.mp3"
    sil(sil_open, OPEN_S)
    sil(sil_gap, gap)
    sil(sil_stay, stay)

    lst = CHUNKS / "concat.txt"
    files = [sil_open]
    titles = [("0:00", "Amanecer")]
    t = OPEN_S
    labels = [
        "Gracias por este día", "Si ayer fallé", "Misericordia nueva", "La casa",
        "Lo que pesa", "Un solo paso", "El hogar", "La mente", "El pan de hoy",
        "Los hijos", "Perdón", "El cuerpo", "Los que están lejos",
        "Otra vez misericordia", "Cúbrenos", "Segunda gratitud", "Mi paz os doy",
        "Quédate", "Este día es Tuyo", "Amén",
    ]
    for i, vf in enumerate(voice_files):
        mm, ss = divmod(int(t), 60)
        titles.append((f"{mm}:{ss:02d}", labels[i] if i < len(labels) else f"Ciclo {i+1}"))
        files.append(vf)
        t += dur(vf)
        if i < len(voice_files) - 1:
            files.append(sil_gap)
            t += gap
    files.append(sil_stay)
    mm, ss = divmod(int(t), 60)
    titles.append((f"{mm}:{ss:02d}", "Permanecer"))

    lst.write_text("".join(f"file '{p.resolve()}'\n" for p in files))
    raw = CHUNKS / "timeline.mp3"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(raw)])

    # pad/trim to exact 90:00 and mix BGM
    run([
        "ffmpeg", "-y",
        "-i", str(raw),
        "-stream_loop", "-1", "-i", str(BGM),
        "-filter_complex",
        f"[0:a]atrim=0:{TARGET},asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[v];"
        f"[1:a]volume=0.16,atrim=0:{TARGET},asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[b];"
        f"[v][b]amix=inputs=2:duration=first:dropout_transition=2,loudnorm=I=-16:LRA=11:TP=-1.5[a]",
        "-map", "[a]", "-t", str(TARGET), "-c:a", "aac", "-b:a", "192k", str(MASTER_A),
    ])

    print("encoding video 90min…")
    run([
        "ffmpeg", "-y",
        "-stream_loop", "-1", "-i", str(VIDEO),
        "-i", str(MASTER_A),
        "-map", "0:v:0", "-map", "1:a:0",
        "-t", str(TARGET),
        "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "23", "-pix_fmt", "yuv420p",
        "-c:a", "copy",
        "-movflags", "+faststart",
        str(MASTER_V),
    ])

    chap_lines = [f"{stamp} {title}" for stamp, title in titles]
    CHAPTERS.write_text("\n".join(chap_lines) + "\n")
    qa = {
        "voice": "DON MARIO",
        "speech_seconds": round(speech, 2),
        "gap_seconds": round(gap, 2),
        "stay_seconds": round(stay, 2),
        "target": TARGET,
        "audio": str(MASTER_A),
        "video": str(MASTER_V),
        "audio_duration": round(dur(MASTER_A), 2),
        "video_duration": round(dur(MASTER_V), 2) if MASTER_V.exists() else None,
        "cycles": reports,
        "pass_90": abs(dur(MASTER_A) - TARGET) < 1.5,
    }
    (OUT / "QA.json").write_text(json.dumps(qa, indent=2, ensure_ascii=False))
    (OUT / "TIMECODE_REAL.md").write_text(
        "# TIMECODE REAL M01 90\n\n```\n" + "\n".join(chap_lines) + "\n```\n"
    )
    print(json.dumps({k: qa[k] for k in qa if k != "cycles"}, indent=2))
    if not qa["pass_90"]:
        sys.exit("QA 90 FAIL")


if __name__ == "__main__":
    main()
