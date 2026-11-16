# Editar un video a cámara como reel de Instagram (estilo RENOVA)

**Objetivo:** convertir un video vertical grabado a cámara en un reel listo para publicar o pautar:
sin tomas falsas ni silencios largos, subtítulos dinámicos, gancho arriba, imagen del producto y cartel de oferta.

**Entradas**
- Videos grandes: que Nacho los suba a Google Drive y pase el link. Se bajan con
  `curl -L -o .tmp/<nombre>/original.mp4 "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"`
  (host habilitado en el entorno RepositorioHenry; no usar el conector de Drive, que devuelve el archivo en base64).
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
- `carteles[].tamano`: tamaño de letra del cartel. Preferencia de Nacho: el gancho del principio va al mismo tamaño que los subtítulos (92);
  si no entra en una línea dentro de la zona segura (más de ~16 caracteres), partirlo en dos líneas con `\n`. Dejar margen a los costados: el recuadro no puede tocar los bordes.
- `cierre`: placa final a pantalla completa (`archivo`, `duracion` 2,5 s, `transicion` 0,4 s, `efecto` de xfade: `fade`, `slideup`…).
  El script estira el último tramo lo que dura la transición, así el fundido no tapa la última frase: poner `fin` al final real del video.
  Para "todo lo que ofrecemos" usar `pack-renova/pack_1.png` (vertical, 3 ebooks + 5 bonus).
- Pantalla dividida (`imagenes[]` con `bajar`): la imagen entra deslizando desde arriba (alto `alto`, fondo `fondo`) y el video baja `bajar` px,
  así un mockup horizontal se ve grande sin tapar la cabeza. Para el pack completo (ebooks + bonus + talleres) usar `pack-renova/pack_completo.png`
  recortado (`pack_completo_recorte.png`: del logo a los productos, sin la fila de etiquetas) con `bajar` 190, `alto` 700, `fondo` #0b1214 y `hasta` null (queda hasta el cierre). Bajar los subtítulos a `subtitulos_y` 1550 para que no tapen el mentón.
- Subtítulos: un número nunca queda solo, va en el mismo bloque que la palabra siguiente ("8 SEMANAS", "35 AÑOS").
- `clips`: videos a pantalla completa (ej. clientas entrenando fuerza) con `archivo`, `inicio_clip`, `desde`/`hasta` (s del original);
  `entra`/`sale` false quitan el fundido para encadenar dos clips sin que se vea el video de fondo entre ellos. La voz sigue y los subtítulos van encima.
- `transiciones`: lista de segundos del original donde hay un cambio de tema (ej. "Soy Nacho Portillo", antes de "Hacé clic"): zoom de 7% que se relaja + destello leve.
- En pantalla dividida, `ancho` centra una imagen más chica sobre `fondo` (foto del equipo: `fuentes/landing/img/equipo_tapa_limpia.png`, `ancho` 760, `alto` 830, 2 s).
- Regla de Nacho: ninguna imagen puede tapar ni cortar la cabeza. Revisar cuadros con la cabeza más alta antes de entregar.
- Subtítulos: Inter Display Black, blanco con borde negro, palabras clave en turquesa #14B1C7, a 1440 px (encima de la zona segura de abajo de 340 px).

**Casos extremos y aprendizajes**
- `unir`: {"de Portólogo": "deportólogo"} junta palabras que Whisper partió (las `correcciones` son globales y no sirven para eso).
- Tarjetas arriba (ej. "Perdés músculo" con 💪↓ y barras que bajan; foto de Rodrigo con nombre y especialidad): PNG transparente de 980×190 en `y` 255, sobre el techo, sin tapar cabeza ni subtítulos. Plantilla: `fuentes/landing/mockups/reels/tarjetas_pierdes_musculo.html` (foto de Rodrigo: `fuentes/landing/img/equipo_rodrigo.jpg`).
- Regla de Nacho (15/11): destellos, transiciones y cambios de toma (entrada al b-roll, cambio de clip, vuelta a cámara) van **en los silencios**: en la unión de dos tramos cortados o en una micro-pausa medida en el audio (`silencios_audio`), nunca en medio de una palabra. El primer clip de b-roll entra con corte seco (`entra` false) y el destello va encima. Las imágenes de productos van fijas (`fijo`: true, sin zoom).
- `cortar: "oraciones"` (con `margen` 0,15 y `pausa_max` 0,25): para charla fluida. Solo corta silencios después de una palabra con . ? ! y solo la parte que el audio confirma como silencio (RMS), así no se come el final de una frase aunque Whisper corra los tiempos. Es el modo por defecto que pidió Nacho (15/11).
- `sin_cortes`: lista de [desde, hasta] del original que van enteros con sus silencios (ej. la mueca del principio o el cierre "Y si llegaste hasta acá…", que Nacho quiere seguidos).
- `tiempos`: {"palabra": [s, e]} corrige una palabra que Whisper corrió a un silencio (pasó con "localizada.": la puso 0,4 s tarde y el corte de silencios la borraba). Si Nacho dice que una frase quedó cortada, medir la energía del audio en ese tramo y comparar con la transcripción.
- `destellos`: segundos del original con un destello fuerte (más marcado que el de `transiciones`), ej. después de cortar un silencio entre dos ideas.
- Pedido frecuente de Nacho: cada producto que nombra, 2 s a pantalla completa (`pack-renova/libro_1_casa.png`, `libro_2_gimnasio.png`, `libro_3_alimentacion.png` con `fondo` #0b1416 y `zoom` 1.15; el pack con `pack_1.png`). Talleres: Agostina en el "Taller de hábitos" de Drive (`1Uid63Yq6lt3jqdnuAlrGo4AtHikXtZ-J`, seg. 575), armado vertical con la cámara arriba y la diapositiva abajo, como `clip`.
- Nacho corrige de a una y pide esperar: responder "ok" a cada corrección sin editar hasta que diga que empiece.
- Whisper a veces pega una toma anterior al principio (ej. "Más cinco bonos de regalo" + 2 s de silencio): mirar siempre la transcripción y mover `inicio`.
- `correcciones` con valor vacío borra la palabra (Whisper separa "e-books" en "e" + "-books": `"e": "E-BOOKS", "books": ""`).
- Escribe "Hace clic", "conoce" sin tilde: corregir el voseo en `correcciones`.
- Red: el modelo se baja de huggingface.co y us.aws.cdn.hf.co; con `HF_HUB_DISABLE_XET=1` evita cas-server.xethub.hf.co (bloqueado).
- La versión de PyAV instalada falla con `decode_audio` de faster-whisper: el script le pasa el audio ya decodificado con ffmpeg.
- Video HDR (iPhone, `color_transfer=arib-std-b67`): pasarlo antes a SDR 1080×1920 y usar ese archivo como `video`:
  `ffmpeg -i original.mp4 -vf "zscale=t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,scale=1080:1920" -c:v libx264 -crf 17 -preset fast -c:a copy sdr.mp4` (un video 4K de 1 min tarda ~3 min).
- B-roll de clientas entrenando fuerza: carpeta de Drive `1J2_w83crv0ZeotXJk-kIBzI6NnM8J6ut` (verticales: `20190421_151852` sentadilla, `20190421_150532` estocadas; `WhatsApp Video 2026-03-30 1.55.54` press con mancuernas y `1.55.49` sentadilla con banda, baja resolución). Para volver a cámara sin ver el giro de cabeza, el último clip va con `sale` false (corte seco).
