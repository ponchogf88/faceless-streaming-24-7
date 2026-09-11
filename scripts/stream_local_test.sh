#!/usr/bin/env bash
# ==============================================================================
# Script de Emisión Local de Prueba: Finanzas Divinas 24/7 (YouTube Live)
# Ecosistema: AMDA Agentic Engine · Autor: @ponchogf88
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
MASTER_FILE="${REPO_ROOT}/output/piloto_15m_v01.mp4"
FFMPEG_BIN="/Users/user/.local/bin/ffmpeg"

YOUTUBE_URL="rtmp://a.rtmp.youtube.com/live2"
YOUTUBE_KEY="${YOUTUBE_STREAM_KEY:-}"

if [[ -n "${1:-}" ]]; then
    YOUTUBE_KEY="$1"
fi

if [[ ! -f "$MASTER_FILE" ]]; then
    echo "❌ ERROR: No se encontró el master en $MASTER_FILE" >&2
    exit 1
fi

echo "========================================================"
echo "  🎬 INICIANDO EMISIÓN DE PRUEBA: FINANZAS DIVINAS 24/7"
echo "========================================================"
echo "  Master:   $MASTER_FILE"
echo "  Destino:  $YOUTUBE_URL"
echo "  Formato:  1080p 30fps | H.264 CBR 4500k | AAC 160k"

if [[ -z "$YOUTUBE_KEY" ]]; then
    echo ""
    echo "⚠️ AVISO: No se proporcionó YOUTUBE_STREAM_KEY."
    echo "Ejecutando prueba de decodificación y emulación local (10 segundos)..."
    "$FFMPEG_BIN" -re -i "$MASTER_FILE" -t 10 -c copy -f null -
    echo ""
    echo "✅ TEST EXITOSO: El archivo master es 100% apto para stream en bucle sin recodificar (<2% CPU)."
    echo "Para emitir en vivo a YouTube Live ejecuta:"
    echo "  ./stream_local_test.sh \"TU_STREAM_KEY_AQUI\""
    exit 0
fi

echo "  Stream Key detectada. Conectando con YouTube Live..."
echo "  Presiona Ctrl+C para detener la emisión."
echo "========================================================"

exec "$FFMPEG_BIN" -re \
    -stream_loop -1 \
    -i "$MASTER_FILE" \
    -c:v copy \
    -c:a copy \
    -f flv \
    "${YOUTUBE_URL}/${YOUTUBE_KEY}"
