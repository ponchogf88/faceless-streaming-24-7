#!/usr/bin/env bash
# ==============================================================================
# Script de Renderizado: Piloto Audiovisual 15 Minutos (Fase A-1)
# Ecosistema: AMDA Agentic Engine · Proyecto: faceless-streaming-24-7
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

INPUT_IMAGE="${REPO_ROOT}/assets/miniatura_youtube_16_9_432hz.jpg"
INPUT_AUDIO="${REPO_ROOT}/assets/audio/onda_alfa_10hz_estudio_5min.wav"
OUTPUT_DIR="${REPO_ROOT}/output"
OUTPUT_FILE="${OUTPUT_DIR}/piloto_15m_v01.mp4"

mkdir -p "$OUTPUT_DIR"

echo "======================================================================"
echo "  🎬 INICIANDO RENDERIZADO DEL PILOTO AUDIOVISUAL (15:00 EXACTOS)"
echo "======================================================================"
echo "Imagen base:   $INPUT_IMAGE"
echo "Audio origen:  $INPUT_AUDIO"
echo "Destino final: $OUTPUT_FILE"
echo "Especificación: 1920x1080 | 30fps | H.264 (CBR 4500k) | Keyframes 2s | AAC 44.1kHz Estéreo"
echo "======================================================================"

ffmpeg -y \
  -loop 1 -i "$INPUT_IMAGE" \
  -stream_loop 2 -i "$INPUT_AUDIO" \
  -t 900 \
  -vf "zoompan=z='1.03+0.02*sin(2*PI*in/1800)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=30,format=yuv420p" \
  -c:v libx264 \
  -preset veryfast \
  -b:v 4500k \
  -maxrate 4500k \
  -bufsize 9000k \
  -g 60 \
  -keyint_min 60 \
  -sc_threshold 0 \
  -c:a aac \
  -b:a 160k \
  -ar 44100 \
  -ac 2 \
  -movflags +faststart \
  "$OUTPUT_FILE"

echo "======================================================================"
echo "  ✅ RENDERIZADO COMPLETADO CON ÉXITO: $OUTPUT_FILE"
echo "======================================================================"
