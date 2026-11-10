# Editar un video a cámara como reel de Instagram (estilo RENOVA)

**Objetivo:** convertir un video vertical grabado a cámara en un reel listo para publicar o pautar:
sin tomas falsas ni silencios largos, subtítulos dinámicos, gancho arriba, imagen del producto y cartel de oferta.

**Entradas**
- Video vertical 1080×1920 (el .mov del iPhone sirve tal cual). Copiarlo a `.tmp/<nombre>/original.mov`.
- Imagen del producto (mockup o tapa) en `.tmp/<nombre>/`. Los mockups están en `main`: `pack-renova/*.png` y `fuentes/landing/img/tapa_*.jpg`.
- Un archivo de configuración `execution/reels/<nombre>.json` (copiar `te-cuesta-comer-bien.json` como modelo).

**Herramienta:** `python3 execution/editar_reel.py --config execution/reels/<nombre>.json`
1. La primera vez transcribe con faster-whisper (`medium`) y guarda `.tmp/<nombre>/palabras.json`. Leer esa transcripción
   para decidir `inicio`/`fin` (sacar tomas falsas), las `correcciones` (voseo: "Hacé", "conocé") y qué palabras `destacar`.
2. Ajustar el JSON y volver a correr: reutiliza la transcripción (usar `--retranscribir` si cambia el video).
3. Revisar cuadros sueltos (`ffmpeg -ss T -i salida.mp4 -frames:v 1 cuadro.png`) antes de entregar.

**Salida:** `.tmp/<nombre>.mp4`: H.264 + AAC, 1080×1920, 30 fps, audio a -14 LUFS.

**Configuración**
- `inicio`/`fin` (s del original): todo lo de afuera se descarta.
- `pausa_max` + `margen`: silencios mayores a `pausa_max + 2·margen` se acortan (0,2 + 0,1 deja el ritmo de reel).
- `carteles`: textos arriba (dentro de la zona segura de 250 px). `desde`/`hasta` en segundos del original; `null` = principio o final.
- `imagenes`: imagen a pantalla completa con zoom lento entre `desde` y `hasta`; `zoom` agranda (1,35 para los mockups de 1080×1350 con fondo oscuro).
  Con `ancho` (y opcional `y`) la imagen va superpuesta en esa posición en vez de a pantalla completa: usar PNG con transparencia
  recortado al contenido (ej. `pack_libros.png` recortado, `ancho` 580, `y` 255 queda justo sobre la cabeza sin salir de la zona segura).
- `carteles[].tamano`: tamaño de letra del cartel. En una sola línea entran ~21 caracteres a 84 px dentro de los márgenes.
- `cierre`: placa final a pantalla completa (`archivo`, `duracion` 2,5 s, `transicion` 0,4 s, `efecto` de xfade: `fade`, `slideup`…).
  El script estira el último tramo lo que dura la transición, así el fundido no tapa la última frase: poner `fin` al final real del video.
  Para "todo lo que ofrecemos" usar `pack-renova/pack_1.png` (vertical, 3 ebooks + 5 bonus).
- Pantalla dividida (`imagenes[]` con `bajar`): la imagen entra deslizando desde arriba (alto `alto`, fondo `fondo`) y el video baja `bajar` px,
  así un mockup horizontal se ve grande sin tapar la cabeza. Para el pack completo (ebooks + bonus + talleres) usar `pack-renova/pack_completo.png`
  con `bajar` 340, `alto` 880, `fondo` #0b1214 y `hasta` null (queda hasta el cierre). Bajar los subtítulos a `subtitulos_y` 1550 para que no tapen el mentón.
- Regla de Nacho: ninguna imagen puede tapar ni cortar la cabeza. Revisar cuadros con la cabeza más alta antes de entregar.
- Subtítulos: Inter Display Black, blanco con borde negro, palabras clave en turquesa #14B1C7, a 1440 px (encima de la zona segura de abajo de 340 px).

**Casos extremos y aprendizajes**
- Whisper a veces pega una toma anterior al principio (ej. "Más cinco bonos de regalo" + 2 s de silencio): mirar siempre la transcripción y mover `inicio`.
- Escribe "Hace clic", "conoce" sin tilde: corregir el voseo en `correcciones`.
- Red: el modelo se baja de huggingface.co y us.aws.cdn.hf.co; con `HF_HUB_DISABLE_XET=1` evita cas-server.xethub.hf.co (bloqueado).
- La versión de PyAV instalada falla con `decode_audio` de faster-whisper: el script le pasa el audio ya decodificado con ffmpeg.
- No hay tono mapping: si el video es HDR (iPhone con `color_transfer=arib-std-b67`), grabar en SDR o agregar `zscale`/`tonemap`.
