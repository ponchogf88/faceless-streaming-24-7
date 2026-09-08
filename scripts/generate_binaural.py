#!/usr/bin/env python3
"""
Generador de Ondas Binaurales y Frecuencias Solfeggio en Python
AMDA Agentic Engine · Ecosistema de Canales Faceless & Streaming 24/7

Permite sintetizar archivos WAV de alta fidelidad (16-bit 44.1kHz estéreo)
para incrustar en pistas musicales y crear la 'Huella Creativa Original'.
"""

import sys
import math
import wave
import struct
import argparse

def generate_binaural_wav(filename, duration_sec=600, base_freq=200.0, beat_freq=10.0, volume=0.15):
    """
    Genera un archivo WAV estéreo con frecuencia binaural.
    Canal Izquierdo: base_freq
    Canal Derecho: base_freq + beat_freq
    Diferencia percibida por el cerebro: beat_freq (ej. 10 Hz Onda Alfa)
    """
    sample_rate = 44100
    num_samples = int(duration_sec * sample_rate)
    
    freq_left = base_freq
    freq_right = base_freq + beat_freq
    
    print(f"Generando pista binaural: {filename}")
    print(f"Duración: {duration_sec}s ({duration_sec/60:.1f} min)")
    print(f"Canal Izquierdo: {freq_left:.1f} Hz | Canal Derecho: {freq_right:.1f} Hz")
    print(f"Frecuencia Cerebral Resultante: {beat_freq:.1f} Hz")
    
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(2)        # Estéreo
        wav_file.setsampwidth(2)        # 16 bits por muestra
        wav_file.setframerate(sample_rate)
        
        # Buffer de escritura en bloques de 4096 frames
        chunk_size = 4096
        frames = bytearray()
        
        for i in range(num_samples):
            t = float(i) / sample_rate
            
            # Onda senoidal canal izquierdo
            val_left = math.sin(2.0 * math.pi * freq_left * t)
            # Onda senoidal canal derecho
            val_right = math.sin(2.0 * math.pi * freq_right * t)
            
            # Escalar a 16-bit signed integer (-32768 a 32767)
            int_left = int(val_left * volume * 32767.0)
            int_right = int(val_right * volume * 32767.0)
            
            frames.extend(struct.pack('<hh', int_left, int_right))
            
            if len(frames) >= chunk_size * 4:
                wav_file.writeframes(frames)
                frames.clear()
                
        if frames:
            wav_file.writeframes(frames)
            
    print(f"✅ Archivo generado con éxito: {filename}")

def generate_solfeggio_wav(filename, duration_sec=600, solfeggio_freq=432.0, volume=0.20):
    """
    Genera un tono puro armónico Solfeggio (ej. 432 Hz o 528 Hz) en ambos canales.
    """
    sample_rate = 44100
    num_samples = int(duration_sec * sample_rate)
    
    print(f"Generando tono Solfeggio armónico: {filename}")
    print(f"Frecuencia: {solfeggio_freq:.1f} Hz | Duración: {duration_sec/60:.1f} min")
    
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(2)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        
        chunk_size = 4096
        frames = bytearray()
        
        for i in range(num_samples):
            t = float(i) / sample_rate
            val = math.sin(2.0 * math.pi * solfeggio_freq * t)
            sample_val = int(val * volume * 32767.0)
            frames.extend(struct.pack('<hh', sample_val, sample_val))
            
            if len(frames) >= chunk_size * 4:
                wav_file.writeframes(frames)
                frames.clear()
                
        if frames:
            wav_file.writeframes(frames)
            
    print(f"✅ Tono Solfeggio generado con éxito: {filename}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generador de Frecuencias AMDA")
    parser.add_argument("--mode", choices=["binaural", "solfeggio"], default="binaural", help="Tipo de generador")
    parser.add_argument("--out", type=str, default="onda_alfa_10hz.wav", help="Ruta de salida WAV")
    parser.add_argument("--duration", type=int, default=300, help="Duración en segundos (default: 300s)")
    parser.add_argument("--base", type=float, default=200.0, help="Frecuencia portadora en Hz (default: 200)")
    parser.add_argument("--beat", type=float, default=10.0, help="Frecuencia de pulso en Hz (ej. 10.0 para Alfa, 6.0 Theta, 2.0 Delta)")
    parser.add_argument("--solfeggio", type=float, default=432.0, help="Frecuencia Solfeggio en Hz (ej. 432, 528)")
    parser.add_argument("--volume", type=float, default=0.15, help="Volumen relativo 0.0 a 1.0 (default: 0.15)")
    
    args = parser.parse_args()
    
    if args.mode == "binaural":
        generate_binaural_wav(args.out, args.duration, args.base, args.beat, args.volume)
    else:
        generate_solfeggio_wav(args.out, args.duration, args.solfeggio, args.volume)
