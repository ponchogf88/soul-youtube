#!/usr/bin/env bash
# ==============================================================================
# Script Autónomo de Ensamblaje de Video Maestro 1080p para Transmisión 24/7
# Ecosistema: AMDA Agentic Engine · Autor: @ponchogf88
# ==============================================================================

set -euo pipefail

GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ASSETS_DIR="${PROJECT_ROOT}/assets"
AUDIO_DIR="${ASSETS_DIR}/audio"
OUTPUT_DIR="${PROJECT_ROOT}/output"
OUTPUT_FILE="${OUTPUT_DIR}/master_stream_1hora.mp4"

mkdir -p "${OUTPUT_DIR}"

BG_IMAGE="${ASSETS_DIR}/miniatura_youtube_16_9_432hz.jpg"
AUDIO_FILE="${AUDIO_DIR}/frecuencia_sacra_432hz_5min.wav"

if [[ ! -f "$BG_IMAGE" ]]; then
    BG_IMAGE="/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/SPIRITUALLY/ASSETS_STREAMING_24_7/miniatura_youtube_16_9_432hz.jpg"
fi

if [[ ! -f "$AUDIO_FILE" ]]; then
    AUDIO_FILE="/Users/imac/Desktop/Projects/FACELESS_STREAMING_24_7_YOUTUBE_TIKTOK/assets/audio/frecuencia_sacra_432hz_5min.wav"
fi

echo -e "${CYAN}================================================================${NC}"
echo -e "${CYAN}   🎬 AMDA ENSAMBLADOR MAESTRO DE VIDEO 1080p 24/7 (FFmpeg)${NC}"
echo -e "${CYAN}================================================================${NC}"
echo -e "${YELLOW}Fondo visual:${NC} $BG_IMAGE"
echo -e "${YELLOW}Pista de audio:${NC} $AUDIO_FILE"
echo -e "${YELLOW}Destino de salida:${NC} $OUTPUT_FILE"

# Detectar aceleración por hardware (Apple VideoToolbox en macOS)
ENCODER="libx264"
ENCODER_OPTS="-preset veryfast -b:v 4500k -maxrate 4500k -bufsize 9000k"

if ffmpeg -encoders 2>/dev/null | grep -q "h264_videotoolbox"; then
    echo -e "${GREEN}✓ Aceleración por hardware Apple VideoToolbox detectada (Metal GPU)${NC}"
    ENCODER="h264_videotoolbox"
    ENCODER_OPTS="-b:v 4500k -maxrate 4500k -bufsize 9000k -profile:v high"
fi

# Renderizado de bucle audiovisual con zoom lento cinematográfico (Ken Burns suave)
# Duración default: 3600s (1 hora completa continua)
DURATION_SEC="${1:-3600}"

echo -e "\n${CYAN}Iniciando renderizado de ${DURATION_SEC} segundos (~$(awk "BEGIN {print ${DURATION_SEC}/60}") minutos)...${NC}"

ffmpeg -y \
    -loop 1 -i "$BG_IMAGE" \
    -stream_loop -1 -i "$AUDIO_FILE" \
    -t "$DURATION_SEC" \
    -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,format=yuv420p" \
    -c:v $ENCODER $ENCODER_OPTS \
    -r 30 -g 60 -keyint_min 60 -sc_threshold 0 \
    -c:a aac -b:a 160k -ar 44100 \
    -shortest \
    "$OUTPUT_FILE"

echo -e "\n${GREEN}================================================================${NC}"
echo -e "${GREEN}  ✓ VIDEO MAESTRO GENERADO CON ÉXITO: ${OUTPUT_FILE}${NC}"
echo -e "${GREEN}  ✓ Especificaciones: 1920x1080 @ 30fps | CBR 4500k | Keyframes: 2.0s | Audio 432Hz AAC${NC}"
echo -e "${GREEN}================================================================${NC}"
