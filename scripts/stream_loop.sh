#!/usr/bin/env bash
# ==============================================================================
# Script Maestro de Transmisión Continua 24/7 con FFmpeg (YouTube & TikTok Live)
# Ecosistema: AMDA Agentic Engine · Autor: @ponchogf88
# ==============================================================================

set -euo pipefail

# --- CONFIGURACIÓN DE ARCHIVOS Y RUTAS ---
MEDIA_DIR="/home/stream/media"
MASTER_FILE="${MEDIA_DIR}/master_stream.mp4"
LOG_FILE="/var/log/livestream.log"

# --- CLAVES DE TRANSMISIÓN RTMP ---
# Configura tus claves aquí o a través de variables de entorno:
YOUTUBE_URL="rtmp://a.rtmp.youtube.com/live2"
YOUTUBE_KEY="${YOUTUBE_STREAM_KEY:-TU_CLAVE_YOUTUBE_AQUI}"

TIKTOK_URL="rtmp://live-push.tiktok.com/live"
TIKTOK_KEY="${TIKTOK_STREAM_KEY:-}"

# Validar existencia del archivo maestro
if [[ ! -f "$MASTER_FILE" ]]; then
    echo "ERROR: El archivo maestro $MASTER_FILE no existe." >&2
    echo "Por favor sube tu video renderizado al VPS antes de iniciar." >&2
    exit 1
fi

echo "========================================================"
echo "Iniciando Transmisión 24/7..."
echo "Archivo origen: $MASTER_FILE"
echo "Destino primario: YouTube Live ($YOUTUBE_URL)"
echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
echo "========================================================"

# --- MODO 1: TRANSMISIÓN HORIZONTAL A YOUTUBE (1080p CBR) ---
# Si el archivo maestro ya viene pre-renderizado con H.264 y AAC desde tu MacBook M1,
# se usa modo de copia directa (-c:v copy -c:a copy) consumiendo menos del 3% de CPU.

if [[ -z "$TIKTOK_KEY" ]]; then
    exec ffmpeg -re \
        -stream_loop -1 \
        -i "$MASTER_FILE" \
        -c:v copy \
        -c:a copy \
        -f flv \
        "${YOUTUBE_URL}/${YOUTUBE_KEY}"
else
    # --- MODO 2: DUAL STREAM SIMULTÁNEO (YOUTUBE 16:9 + TIKTOK 9:16) ---
    echo "Modo Dual Stream detectado. Emitiendo hacia YouTube y TikTok..."
    exec ffmpeg -re \
        -stream_loop -1 \
        -i "$MASTER_FILE" \
        -map 0:v -map 0:a \
        -c:v:0 copy -c:a:0 copy \
        -f flv "${YOUTUBE_URL}/${YOUTUBE_KEY}" \
        -map 0:v -map 0:a \
        -vf "crop=ih*(9/16):ih,scale=1080:1920" \
        -c:v:1 libx264 -preset veryfast -b:v:1 3000k -maxrate 3000k -bufsize 6000k -g 60 \
        -c:a:1 aac -b:a:1 128k -ar 44100 \
        -f flv "${TIKTOK_URL}/${TIKTOK_KEY}"
fi
