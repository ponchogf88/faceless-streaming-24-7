# Memoria operativa completa — FINANZAS DIVINAS

## 1. Propósito de este archivo

Este documento conserva el contexto, las decisiones y las reglas de trabajo del proyecto para retomarlo en otra computadora, otra sesión o con otro agente sin volver a empezar desde cero.

## 2. Identidad del proyecto

- Proyecto técnico: `faceless-streaming-24-7`.
- Repositorio: `https://github.com/ponchogf88/faceless-streaming-24-7`.
- Cuenta: `ponchogf88`.
- Canal: **FINANZAS DIVINAS**.
- Propósito: transmisión 24/7 de música/ambientes de concentración, éxito y finanzas con visuales celestiales y de lujo.
- Computadora actual de producción inicial: iMac.
- Computadora para retomar, operar y probar: Dell Windows.

## 3. Concepto creativo aprobado

La estética aprobada no utiliza Biblia, iglesias, cruces, velas, altares ni símbolos religiosos visibles. El lenguaje visual debe ser celestial, aspiracional y elegante:

- nubes, palomas, amaneceres y cielos amplios;
- vuelos sobre montañas, playas, puertos y ciudades;
- tomas aéreas tipo dron o sobre un águila;
- yates, mansiones, marinas, hoteles, jets, lujo y éxito;
- destinos de referencia: Mónaco, Islas Caimán, Tailandia, Dubái, Miami, Río de Janeiro y playas tropicales.

No se debe transformar el canal en un canal de oración ni insertar símbolos religiosos solo porque el nombre contiene “Divinas”. La marca significa elevación, abundancia, enfoque y visión.

## 4. Preferencias de operación del propietario

El propietario paga por herramientas de IA y espera que el agente ejecute el trabajo. No quiere recibir instrucciones que lo conviertan en editor manual ni tener que buscar, arrastrar, seleccionar o ensamblar elementos si el agente puede hacerlo.

Reglas de comunicación:

1. Tomar acción primero y reportar el resultado después.
2. No pedirle al propietario que haga tareas técnicas repetitivas.
3. Si una acción requiere autenticación, CAPTCHA, clave RTMP o permiso humano, detenerse exactamente en ese punto y explicar una sola intervención concreta.
4. Trabajar por fases cerradas, pero sin inventar bloqueos innecesarios.
5. No declarar “listo” sin verificar archivos con FFprobe o una prueba equivalente.
6. Mantener los originales intactos; crear versiones nuevas.
7. No usar una playlist ajena de Spotify, YouTube o una estación de radio sin licencia.

## 5. Herramientas y capacidades disponibles

- Canva Business: biblioteca de videos y exportación del visual base.
- Page Agent para Chrome: puede navegar y operar interfaces web mediante DOM, pero no es confiable para elegir visualmente “el mejor” clip de una biblioteca ni para operaciones complejas de arrastrar y soltar. Por eso el flujo actual usa el video ya exportado desde Canva y deja el ensamblaje a FFmpeg.
- FFmpeg/FFprobe: ensamblaje, bucles, mezcla de audio, validación y preparación para emisión.
- ElevenLabs: reservado para voz hablada si posteriormente se crea una versión narrada; el piloto actual no lleva voz.
- n8n local: automatización futura de generación, registro y publicación.
- VPS Ubuntu/Hetzner: destino futuro de la emisión 24/7.
- YouTube Live: primero prueba privada/no listada; después emisión pública.

## 6. Decisiones técnicas tomadas

- Primero se construye un piloto de 15 minutos.
- Después se valida un directo de 30–60 minutos.
- Solo después se prepara el master de 1–4 horas y el VPS.
- El video actual conserva 4K/60 fps para calidad visual.
- Para emisión se generará una versión 1080p/30 fps y aproximadamente 4.5 Mbps, porque es más eficiente para YouTube Live y VPS.
- La playlist se construye internamente con pistas locales y crossfades.
- El audio del piloto no contiene voz, narración ni promesas médicas.

## 7. Archivos creados en el piloto

Directorio de trabajo local:

`/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/FINANZAS DIVINAS_PILOTO/`

Archivos principales:

- `FINANZAS_DIVINAS_PILOTO_15M_PLAYLIST_CELESTIAL.mp4` — video final 4K de 15:00 con playlist mezclada.
- `finanzas_divinas_piloto_4k_15m.mp4` — video 4K de 15:00 con audio base.
- `playlist_celestial_15m.m4a` — playlist de audio de 15:00.
- `finanzas_divinas_piloto_15m_v01.mp4` — salida incompleta/no utilizable; no usar.

Fuente visual descargada desde Canva Business:

`/Users/imac/Downloads/aerial luxury city sunrise.mp4`

Características verificadas de la fuente: 3840×2160, 60 fps, aproximadamente 4:08.8, toma aérea de ciudad/puerto/yates.

Pistas locales utilizadas:

- `assets/audio/onda_alfa_10hz_estudio_5min.wav`
- `assets/audio/frecuencia_sacra_432hz_5min.wav`

Secuencia del piloto:

`onda alfa → 432 Hz/ambiente → onda alfa`, con crossfade de 8 segundos.

## 8. Estado técnico verificado

El archivo final `FINANZAS_DIVINAS_PILOTO_15M_PLAYLIST_CELESTIAL.mp4` fue validado con estas características:

- duración: `900.000000` segundos;
- video: H.264, 3840×2160, 60 fps;
- audio: AAC, 44.1 kHz, estéreo, aproximadamente 189 kbps;
- prueba de decodificación al final del archivo: correcta;
- el visual no contiene símbolos religiosos visibles.

## 9. Qué falta para terminar el 24/7

### Fase siguiente inmediata — Dell

1. Instalar/verificar Git, FFmpeg y FFprobe.
2. Clonar o actualizar `ponchogf88/faceless-streaming-24-7`.
3. Copiar/sincronizar el master y la playlist desde el iMac mediante Google Drive, red local o disco externo.
4. Ejecutar una prueba local de 30–60 minutos.
5. Crear la salida 1080p/30 fps para emisión.
6. Abrir un directo privado o no listado en YouTube.
7. Verificar continuidad, audio, bitrate y temperatura/estabilidad de la Dell.

### Después de la prueba

1. Confirmar o contratar VPS.
2. Subir el master al VPS.
3. Guardar la clave RTMP como secreto o variable de entorno, nunca dentro del repositorio.
4. Activar `livestream.service` con systemd.
5. Añadir reinicio automático y procedimiento de emergencia.
6. Crear la variante vertical para TikTok.
7. Diseñar una playlist de varias horas para evitar repetición evidente.

## 10. Estado de Git al corte

El remoto está configurado como:

`https://github.com/ponchogf88/faceless-streaming-24-7.git`

La rama es `main`. Existía un script no versionado relacionado con el piloto:

`scripts/render_piloto_15m_v01.sh`

La memoria y el reporte deben registrarse en Git. El video 4K de aproximadamente 4 GB no debe subirse a GitHub; debe permanecer en almacenamiento de assets, Drive, disco externo o almacenamiento de objetos.

## 11. Historial de decisiones importantes

- Se descartó la estética de Biblia/iglesia porque el propietario no la quiere.
- Se descartó pedir al propietario que haga manualmente la selección y edición en Canva.
- Page Agent no se utilizará como editor creativo principal; Canva exporta el material y FFmpeg ensambla.
- El primer video debe ser un piloto real de 15 minutos antes de construir un directo de 24 horas.
- Se creó una playlist propia en vez de retransmitir una estación de terceros.
- Se conservaron los archivos originales y se generaron salidas nuevas.
- La emisión 24/7 todavía no está confirmada; solo está listo el piloto audiovisual.

## 12. Frase de recuperación para una sesión futura

> Retoma el proyecto `ponchogf88/faceless-streaming-24-7` desde `MEMORIA_OPERATIVA_COMPLETA.md`. El canal se llama FINANZAS DIVINAS. El piloto 4K de 15 minutos ya está verificado en el iMac. No me pidas editar manualmente: prepara la versión 1080p, prueba local de 30–60 minutos en la Dell y después configura el directo privado de YouTube. Conserva la estética celestial/de lujo sin símbolos religiosos.
