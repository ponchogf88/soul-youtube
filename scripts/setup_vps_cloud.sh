#!/usr/bin/env bash
# ==============================================================================
# Script de Despliegue Automatizado 1-Click para VPS Cloud (Hetzner / AWS / Ubuntu)
# Ecosistema: AMDA Agentic Engine · Autor: @ponchogf88
# ==============================================================================

set -euo pipefail

echo "========================================================"
echo "  🚀 INICIANDO APROVISIONAMIENTO DE SERVIDOR DE STREAMING 24/7"
echo "  Ecosistema AMDA · @ponchogf88"
echo "========================================================"

# 1. Actualización del sistema e instalación de paquetes esenciales
sudo apt-get update -y
sudo apt-get install -y ffmpeg curl git ufw htop ca-certificates

# 2. Creación del usuario y carpetas de trabajo
if ! id "stream" &>/dev/null; then
    sudo useradd -m -s /bin/bash stream
    echo "Usuario 'stream' creado."
fi

sudo mkdir -p /home/stream/media /home/stream/scripts /var/log/livestream
sudo chown -R stream:stream /home/stream /var/log/livestream

# 3. Configuración de Firewall básico
sudo ufw allow OpenSSH
sudo ufw --force enable

# 4. Instalación del servicio systemd para autorecuperación
cat << 'EOF' | sudo tee /etc/systemd/system/livestream.service > /dev/null
[Unit]
Description=AMDA 24/7 Livestreaming Engine (YouTube & TikTok)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=stream
WorkingDirectory=/home/stream
ExecStart=/home/stream/scripts/stream_loop.sh
Restart=always
RestartSec=5
StandardOutput=append:/var/log/livestream/stdout.log
StandardError=append:/var/log/livestream/stderr.log

# Límites de seguridad
LimitNOFILE=65536
KillMode=control-group

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable livestream.service

echo "========================================================"
echo "  ✅ SERVIDOR APROVISIONADO CON ÉXITO"
echo "========================================================"
echo "Pasos finales para emitir:"
echo "1. Sube tu video maestro a: /home/stream/media/master_stream.mp4"
echo "2. Copia tu stream_loop.sh a: /home/stream/scripts/stream_loop.sh"
echo "3. Exporta tus claves: export YOUTUBE_STREAM_KEY='tu-clave'"
echo "4. Inicia el demonio con: sudo systemctl start livestream"
echo "5. Monitorea logs con: tail -f /var/log/livestream/stderr.log"
echo "========================================================"
