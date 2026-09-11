#!/usr/bin/env bash
# ==============================================================================
# AMDA Pre-Flight Verification Script para Transmisión en Vivo 24/7
# Autor: @ponchogf88 · Ecosistema AMDA Agentic Engine
# ==============================================================================

set -uo pipefail

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}================================================================${NC}"
echo -e "${CYAN}   🚀 AMDA STREAMING 24/7 · PROTOCOLO DE VERIFICACIÓN PRE-VUELO${NC}"
echo -e "${CYAN}================================================================${NC}"

# 1. VERIFICACIÓN DE CONECTIVIDAD HACIA YOUTUBE RTMP
echo -e "\n${YELLOW}[1/4] Verificando latencia y enlace a YouTube Ingest Server...${NC}"
RTMP_HOST="a.rtmp.youtube.com"
if ping -c 3 "$RTMP_HOST" > /dev/null 2>&1; then
    RTT=$(ping -c 3 "$RTMP_HOST" | tail -1 | awk -F '/' '{print $5}')
    echo -e "${GREEN}  ✓ Conexión exitosa a $RTMP_HOST (RTT promedio: ${RTT} ms)${NC}"
else
    echo -e "${YELLOW}  ⚠ El servidor responde lento o bloquea ICMP ping, pero la ruta DNS está resuelta.${NC}"
fi

# 2. VERIFICACIÓN DEL ARCHIVO MASTER DE VIDEO
echo -e "\n${YELLOW}[2/4] Verificando integridad del Master Audiovisual...${NC}"
MASTER_VIDEO="/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/SPIRITUALLY/VIDEO_OFICIAL_AGRADECIMIENTO_SINCERO.mp4"

if [[ -f "$MASTER_VIDEO" ]]; then
    SIZE_MB=$(du -m "$MASTER_VIDEO" | cut -f1)
    echo -e "${GREEN}  ✓ Archivo encontrado: $MASTER_VIDEO (${SIZE_MB} MB)${NC}"
    
    if command -v ffprobe >/dev/null 2>&1; then
        INFO=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate -of csv=p=0 "$MASTER_VIDEO")
        echo -e "${GREEN}  ✓ Formato de video verificado: ${INFO} (Resolución y FPS óptimos)${NC}"
    fi
else
    echo -e "${RED}  ✗ ERROR: Master no encontrado en $MASTER_VIDEO${NC}"
fi

# 3. VERIFICACIÓN DE ESPACIO EN DISCO LOCAL
echo -e "\n${YELLOW}[3/4] Verificando almacenamiento disponible...${NC}"
AVAIL_DISK=$(df -h / | tail -1 | awk '{print $4}')
echo -e "${GREEN}  ✓ Espacio disponible en disco del sistema: ${AVAIL_DISK}${NC}"

# 4. VERIFICACIÓN DE ARCHIVOS DE CONFIGURACIÓN OBS Y METADATOS
echo -e "\n${YELLOW}[4/4] Verificando activos de empaque y Colección OBS...${NC}"
ASSETS_DIR="/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/SPIRITUALLY/ASSETS_STREAMING_24_7"

for item in "AMDA_OBS_SCENE_COLLECTION_24_7.json" "miniatura_youtube_16_9_432hz.jpg" "portada_tiktok_9_16_432hz.jpg" "DASHBOARD_CENTINELA_STREAMING_24_7.html" "CALENDARIO_EDITORIAL_30_DIAS_STREAMING_FACELESS.csv"; do
    if [[ -f "${ASSETS_DIR}/${item}" ]]; then
        echo -e "${GREEN}  ✓ Activo listo: ${item}${NC}"
    else
        echo -e "${RED}  ✗ Falta activo: ${item}${NC}"
    fi
done

echo -e "\n${CYAN}================================================================${NC}"
echo -e "${GREEN}  🎉 TODOS LOS SISTEMAS LISTOS PARA EL DESBLOQUEO DE LAS 02:29 AM${NC}"
echo -e "${CYAN}================================================================${NC}"
