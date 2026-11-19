#!/usr/bin/env python3
"""Pipeline audiovisual anti-Content-ID para contenido faceless de GTA 6.

Transforma capturas crudas de gameplay y pistas de voz (ElevenLabs) en piezas
listas para monetizar en YouTube 16:9 (-14 LUFS, micro-zoom anti-duplicado,
sidechain ducking) y verticales 9:16 (>62s) para TikTok Creator Rewards Program.
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Sequence

FALLBACK_BIN_DIRS = (
    Path.home() / ".local" / "bin",
    Path("/opt/homebrew/bin"),
    Path("/usr/local/bin"),
)

MIN_CRP_DURATION_SEC = 62.0
TARGET_LUFS = -14.0
TARGET_TRUE_PEAK = -1.5
TARGET_LRA = 11.0


def find_binary(name: str) -> str | None:
    """Localiza un binario en PATH o rutas comunes de macOS."""
    resolved = shutil.which(name)
    if resolved:
        return resolved
    for directory in FALLBACK_BIN_DIRS:
        candidate = directory / name
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)
    return None


def require_binaries(*names: str) -> dict[str, str]:
    """Verifica que los binarios requeridos existan y devuelve sus rutas."""
    found: dict[str, str] = {}
    missing: list[str] = []
    for name in names:
        path = find_binary(name)
        if path:
            found[name] = path
        else:
            missing.append(name)
    if missing:
        raise RuntimeError(
            f"Binarios no encontrados: {', '.join(missing)}. "
            "Instala FFmpeg (p. ej. brew install ffmpeg o en ~/.local/bin)."
        )
    return found


def probe_duration(ffprobe_bin: str, media_path: Path) -> float:
    """Obtiene la duracion en segundos de un archivo de audio o video."""
    cmd = [
        ffprobe_bin,
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "json",
        str(media_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    payload = json.loads(result.stdout or "{}")
    duration_raw = payload.get("format", {}).get("duration")
    if duration_raw is None:
        raise ValueError(f"No se pudo determinar la duracion de {media_path}")
    return float(duration_raw)


def validate_inputs(paths: Sequence[Path | None]) -> None:
    """Valida existencia de archivos de entrada obligatorios u opcionales."""
    for path in paths:
        if path is not None and not path.is_file():
            raise FileNotFoundError(f"Archivo de entrada no encontrado: {path}")


def run_ffmpeg_command(cmd: Sequence[str], dry_run: bool) -> int:
    """Imprime y opcionalmente ejecuta un comando de FFmpeg."""
    formatted = " ".join(shlex.quote(part) for part in cmd)
    print(f"[CMD] {formatted}")
    if dry_run:
        print("[DRY-RUN] Comando validado sin ejecucion.")
        return 0
    completed = subprocess.run(cmd)
    return completed.returncode


def build_audio_ducking_filter(
    game_gain_db: float,
    has_bgm: bool,
    bgm_gain_db: float,
    voice_input_idx: int = 1,
    bgm_input_idx: int = 2,
) -> tuple[str, str]:
    """Construye filtro FFmpeg con sidechain ducking y normalizacion a -14 LUFS.

    Mantiene el audio del gameplay atenuado (-22 dB por defecto) y lo comprime
    automaticamente cuando entra la locucion, evitando Content ID de radio residual
    y protegiendo claridad vocal.
    """
    filters = [
        f"[0:a]volume={game_gain_db}dB,highpass=f=120,lowpass=f=7500[game_clean]",
        f"[{voice_input_idx}:a]aresample=48000,asplit=2[vo_sc][vo_mix]",
        "[game_clean][vo_sc]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=250[game_ducked]",
    ]
    if has_bgm:
        filters.append(f"[{bgm_input_idx}:a]volume={bgm_gain_db}dB[bgm_low]")
        filters.append(
            "[game_ducked][vo_mix][bgm_low]amix=inputs=3:duration=first:dropout_transition=2[mixed]"
        )
    else:
        filters.append(
            "[game_ducked][vo_mix]amix=inputs=2:duration=first:dropout_transition=2[mixed]"
        )
    filters.append(
        f"[mixed]loudnorm=I={TARGET_LUFS}:TP={TARGET_TRUE_PEAK}:LRA={TARGET_LRA},aresample=48000[aout]"
    )
    return ";".join(filters), "[aout]"


def handle_check() -> int:
    """Verifica disponibilidad de FFmpeg, FFprobe y filtros clave."""
    ffmpeg_bin = find_binary("ffmpeg")
    ffprobe_bin = find_binary("ffprobe")
    print("=== DIAGNOSTICO DEL ENTORNO GTA 6 FACELESS PIPELINE ===")
    print(f"Python  : {sys.version.split()[0]}")
    print(f"ffmpeg  : {ffmpeg_bin or 'NO ENCONTRADO'}")
    print(f"ffprobe : {ffprobe_bin or 'NO ENCONTRADO'}")

    if not ffmpeg_bin or not ffprobe_bin:
        print("[ERROR] Instala ffmpeg/ffprobe antes de renderizar.")
        return 1

    version_out = subprocess.run(
        [ffmpeg_bin, "-version"], capture_output=True, text=True, check=False
    )
    first_line = (version_out.stdout or "").splitlines()[0] if version_out.stdout else ""
    print(f"Version : {first_line}")

    filters_out = subprocess.run(
        [ffmpeg_bin, "-hide_banner", "-filters"],
        capture_output=True,
        text=True,
        check=False,
    )
    required_filters = ("loudnorm", "sidechaincompress", "drawbox", "crop", "scale")
    missing_filters = [f for f in required_filters if f not in (filters_out.stdout or "")]
    if missing_filters:
        print(f"[WARN] Filtros no detectados en build de ffmpeg: {', '.join(missing_filters)}")
        return 1

    print(f"Filtros : {', '.join(required_filters)} [OK]")
    print(
        f"Estandar: -{abs(TARGET_LUFS):.0f} LUFS | TP {TARGET_TRUE_PEAK} dBTP | "
        f"Minimo TikTok CRP: {MIN_CRP_DURATION_SEC:.0f}s"
    )
    return 0


def cmd_sanitize_audio(args: argparse.Namespace) -> int:
    """Aplica sidechain ducking al gameplay con voz ElevenLabs y masteriza a -14 LUFS."""
    bins = require_binaries("ffmpeg")
    validate_inputs([args.gameplay, args.voice, args.bgm])

    cmd = [bins["ffmpeg"], "-y", "-i", str(args.gameplay), "-i", str(args.voice)]
    if args.bgm:
        cmd.extend(["-stream_loop", "-1", "-i", str(args.bgm)])

    filter_complex, aout = build_audio_ducking_filter(
        game_gain_db=args.game_gain_db,
        has_bgm=args.bgm is not None,
        bgm_gain_db=args.bgm_gain_db,
    )
    cmd.extend(
        [
            "-filter_complex",
            filter_complex,
            "-map",
            "0:v:0",
            "-map",
            aout,
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-shortest",
            str(args.output),
        ]
    )
    return run_ffmpeg_command(cmd, args.dry_run)


def cmd_master_16x9(args: argparse.Namespace) -> int:
    """Genera master 16:9 con micro-zoom anti-duplicado, HUD opcional y -14 LUFS."""
    bins = require_binaries("ffmpeg")
    validate_inputs([args.gameplay, args.voice, args.bgm, args.hud])

    cmd = [bins["ffmpeg"], "-y", "-i", str(args.gameplay), "-i", str(args.voice)]
    next_idx = 2
    bgm_idx = -1
    hud_idx = -1
    if args.bgm:
        cmd.extend(["-stream_loop", "-1", "-i", str(args.bgm)])
        bgm_idx = next_idx
        next_idx += 1
    if args.hud:
        cmd.extend(["-i", str(args.hud)])
        hud_idx = next_idx

    # Micro-oscilacion suave (100% -> 104%) cada 6s para evitar deteccion de plano estatico
    video_chain = (
        "[0:v]scale=1996:1124:force_original_aspect_ratio=increase,"
        "crop=1920:1080:"
        "x='(iw-ow)/2*(1+0.6*sin(2*PI*t/6))':"
        "y='(ih-oh)/2*(1+0.6*cos(2*PI*t/6))',"
        "eq=contrast=1.03:saturation=1.05[vbase]"
    )
    if args.hud:
        video_chain += f";[vbase][{hud_idx}:v]overlay=0:0:format=auto[vout]"
        vout = "[vout]"
    else:
        vout = "[vbase]"

    audio_chain, aout = build_audio_ducking_filter(
        game_gain_db=args.game_gain_db,
        has_bgm=args.bgm is not None,
        bgm_gain_db=args.bgm_gain_db,
        voice_input_idx=1,
        bgm_input_idx=bgm_idx,
    )

    cmd.extend(
        [
            "-filter_complex",
            f"{video_chain};{audio_chain}",
            "-map",
            vout,
            "-map",
            aout,
            "-c:v",
            "libx264",
            "-preset",
            args.preset,
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-movflags",
            "+faststart",
            "-shortest",
            str(args.output),
        ]
    )
    return run_ffmpeg_command(cmd, args.dry_run)


def cmd_render_crp_9x16(args: argparse.Namespace) -> int:
    """Convierte clip a vertical 1080x1920 (>62s CRP) con barra de progreso y -14 LUFS."""
    bins = require_binaries("ffmpeg", "ffprobe")
    validate_inputs([args.gameplay, args.voice, args.bgm])

    if not args.dry_run:
        voice_dur = probe_duration(bins["ffprobe"], args.voice)
        game_dur = probe_duration(bins["ffprobe"], args.gameplay)
        effective_dur = min(voice_dur, game_dur)
    else:
        effective_dur = args.target_duration

    if effective_dur < MIN_CRP_DURATION_SEC and not args.allow_short:
        raise ValueError(
            f"Duracion efectiva ({effective_dur:.2f}s) menor a {MIN_CRP_DURATION_SEC:.0f}s. "
            "TikTok Creator Rewards Program paga $0 a videos <60s. "
            "Alarga el guion/gameplay a >=62s o pasa --allow-short para YouTube Shorts."
        )

    bar_duration = max(effective_dur, 1.0)
    cmd = [bins["ffmpeg"], "-y", "-i", str(args.gameplay), "-i", str(args.voice)]
    if args.bgm:
        cmd.extend(["-stream_loop", "-1", "-i", str(args.bgm)])

    # Encuadre 9:16 nitido (sin barras negras muertas) + barra de retencion superior Vice Magenta
    video_chain = (
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,"
        "crop=1080:1920,eq=contrast=1.04:saturation=1.06,"
        "drawbox=x=0:y=0:w=1080:h=14:color=#090D16@0.85:t=fill,"
        f"drawbox=x=0:y=0:w='min(1080,1080*t/{bar_duration:.2f})':h=14:color=#FF2A85@0.95:t=fill,"
        "drawbox=x=60:y=1360:w=960:h=260:color=#090D16@0.35:t=fill[vout]"
    )
    audio_chain, aout = build_audio_ducking_filter(
        game_gain_db=args.game_gain_db,
        has_bgm=args.bgm is not None,
        bgm_gain_db=args.bgm_gain_db,
    )

    cmd.extend(
        [
            "-filter_complex",
            f"{video_chain};{audio_chain}",
            "-map",
            "[vout]",
            "-map",
            aout,
            "-c:v",
            "libx264",
            "-preset",
            args.preset,
            "-crf",
            "18",
            "-r",
            "60",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-movflags",
            "+faststart",
            "-shortest",
            str(args.output),
        ]
    )
    return run_ffmpeg_command(cmd, args.dry_run)


def add_common_audio_args(parser: argparse.ArgumentParser) -> None:
    """Registra argumentos compartidos de audio y ejecucion."""
    parser.add_argument("--gameplay", type=Path, required=True, help="Video MP4/MKV capturado sin radio.")
    parser.add_argument("--voice", type=Path, required=True, help="Pista de locucion ElevenLabs (WAV/MP3).")
    parser.add_argument("--bgm", type=Path, default=None, help="Musica royalty-free opcional (-18 dB).")
    parser.add_argument("--output", type=Path, required=True, help="Ruta de salida MP4.")
    parser.add_argument("--game-gain-db", type=float, default=-22.0, help="Atenuacion del gameplay (dB).")
    parser.add_argument("--bgm-gain-db", type=float, default=-18.0, help="Nivel de musica de fondo (dB).")
    parser.add_argument("--dry-run", action="store_true", help="Valida e imprime comando FFmpeg sin renderizar.")


def build_parser() -> argparse.ArgumentParser:
    """Construye el parser CLI principal."""
    parser = argparse.ArgumentParser(
        description="Pipeline audiovisual anti-Content-ID para GTA 6 Faceless Monetization."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verifica FFmpeg, FFprobe y filtros disponibles en el sistema.",
    )
    subparsers = parser.add_subparsers(dest="command")

    p_sanitize = subparsers.add_parser(
        "sanitize-audio",
        help="Aplica sidechain ducking (-22 dB) al audio del juego y masteriza a -14 LUFS.",
    )
    add_common_audio_args(p_sanitize)

    p_master = subparsers.add_parser(
        "master-16x9",
        help="Renderiza video largo 1080p con micro-zoom anti-duplicado, HUD opcional y -14 LUFS.",
    )
    add_common_audio_args(p_master)
    p_master.add_argument("--hud", type=Path, default=None, help="Imagen PNG transparente 1920x1080 con HUD.")
    p_master.add_argument("--preset", default="medium", help="Preset x264 (default: medium).")

    p_crp = subparsers.add_parser(
        "render-crp-9x16",
        help="Renderiza vertical 1080x1920 (>62s obligatorio para TikTok CRP) con barra de progreso.",
    )
    add_common_audio_args(p_crp)
    p_crp.add_argument("--preset", default="medium", help="Preset x264 (default: medium).")
    p_crp.add_argument(
        "--target-duration",
        type=float,
        default=65.0,
        help="Duracion estimada en segundos usada en modo --dry-run (default: 65.0).",
    )
    p_crp.add_argument(
        "--allow-short",
        action="store_true",
        help="Permite clips <62s (solo para YouTube Shorts/Reels; no monetiza en TikTok CRP).",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Punto de entrada CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.check:
        return handle_check()

    if not args.command:
        parser.print_help()
        return 0

    handlers = {
        "sanitize-audio": cmd_sanitize_audio,
        "master-16x9": cmd_master_16x9,
        "render-crp-9x16": cmd_render_crp_9x16,
    }
    try:
        return handlers[args.command](args)
    except (FileNotFoundError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
