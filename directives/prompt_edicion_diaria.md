# EDICIÓN DIARIA · prompt para editar reels de RENOVA

Copiar todo, completar lo que está entre [corchetes] y pegarlo en una conversación nueva.
Referencias técnicas: `directives/editar_reel.md` y `execution/editar_reel.py`. Reels modelo: `execution/reels/no-todos-los-dias.json` y `execution/reels/pierdes-musculo.json`.

---

## EDICIÓN DIARIA

Editá este video como reel de Instagram en el estilo RENOVA.

**Link:** [link de Google Drive: un video o una carpeta]
**Indicaciones de este video:** [lo que quiero en este reel: qué mostrar, en qué frase, cuánto tiempo, partes sin cortes. Si no pongo nada, decidí vos siguiendo este prompt.]

### 1. Leé el link antes de editar

- **Si es una carpeta,** listá todo lo que tiene:
  - **Documento** (Google Doc, Word, txt): leelo primero, porque son mis indicaciones o el guion, y seguilo.
  - **Video principal:** el más largo, donde hablo a cámara.
  - **B-roll:** los videos cortos (por ejemplo CANSADA.mp4, DOLOR MUSCULAR.mp4). Mirá un cuadro de cada uno para saber qué muestran y usalos donde corresponda según lo que digo.
  - **Imágenes:** fotos, tapas o capturas para mostrar cuando las nombro.
- **Si es un solo video,** editá según mis indicaciones y las reglas de abajo.
- **Si falta algo** que pedí (un b-roll, una foto), buscalo primero:
  - en el repositorio (`pack-renova/`, `fuentes/landing/img/`);
  - en mis carpetas de Drive (clientas: `1J2_w83crv0ZeotXJk-kIBzI6NnM8J6ut`; talleres: el "Taller de hábitos" de Agostina, `1Uid63Yq6lt3jqdnuAlrGo4AtHikXtZ-J`).

  Si no aparece, preguntame antes de inventar.

### 2. Preparación

- Bajá todo a `.tmp/<nombre>/` (desde Drive: `drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t`).
- Si el video es HDR (iPhone, `color_transfer=arib-std-b67`), pasalo a SDR 1080×1920 antes de editar, así no se ve lavado.
- Transcribí con Whisper y **leé la transcripción completa**:
  - Sacá las tomas falsas con `inicio` y `fin`.
  - Corregí los subtítulos al voseo (caminás, entrenás, podés, hacé clic, comentá) y a los nombres reales (E-BOOKS, pack RENOVA, DEPORTÓLOGO). Si Whisper parte una palabra, usá `unir`.
- **Los subtítulos dicen lo que yo digo.** No mejores mis frases: corregí solo la ortografía.

### 3. Cortes (lo más importante)

- **Charla fluida:** usá `cortar: "oraciones"` (con `pausa_max` 0,25 y `margen` 0,15). Así, solo se cortan los silencios **entre oraciones**, nunca dentro de una frase.
- **Cada oración termina completa.** El corte lo decide el audio real (RMS), no los tiempos de Whisper, porque Whisper puede correr una palabra a un silencio y el corte se la come. Si te digo que una frase quedó cortada, medí el audio en ese tramo y corregí con `tiempos`.
- **Partes que pido sin cortes** (una mueca al principio, el cierre "si llegaste hasta acá…"): usá `sin_cortes`.
- Silencios largos entre dos ideas (más de 1 s): cortalos siempre.

### 4. Transiciones: cuándo y cómo

- **Regla de oro:** toda transición, destello o cambio de toma (entrar al b-roll, cambiar de clip, volver a cámara, entrar o salir de una imagen) va **en un silencio**, es decir, en la unión de dos tramos cortados o en una micro-pausa de mi voz medida en el audio. Nunca en medio de una palabra.
- **Transición sutil** (zoom de 7 % que se relaja, con un destello leve de 0,16): cuando cambio de tema, por ejemplo en "Soy Nacho Portillo" o en el llamado final ("Hacé clic…", "Comentá…").
- **Destello fuerte** (0,55, va encima de todo): después de un silencio largo que separa el problema de la solución ("La realidad es que…", "Por eso…"). El b-roll que arranca ahí entra con corte seco (`entra` false).
- **Cambios entre clips de b-roll:** corte seco (`sale` false / `entra` false), en micro-pausas.
- **Volver a cámara:** corte seco en un silencio, mirando a cámara. Nunca con un fundido que muestre un instante en que estoy girado.
- **Cierre:** placa final con el pack (`pack-renova/pack_1.png`), 2,5 s, con fundido de 0,4 s.

### 5. Tiempos

- **Gancho arriba:** desde el principio hasta que termina la primera frase (unos 5-6 s).
- **B-roll:**
  - cada clip dura de 1,5 a 2,5 s;
  - si te digo una duración, respetala con un margen de ±0,5 s para que el corte caiga en una pausa.
- **Productos:** aparecen justo cuando los nombro y duran lo que dura esa parte de la frase, idealmente 2 s.
- **Tarjetas:** unos 2 s.
- **Si una duración pedida no coincide con una pausa,** priorizá la pausa y avisame la diferencia.

### 6. Zonas seguras y cabezas

- **Zonas seguras del reel (1080×1920):**
  - **arriba 250 px y abajo 340 px:** ahí no va nada importante;
  - **subtítulos** a 1490 px.
- **Nunca tapar ni cortar mi cabeza ni la de nadie:** mirá los cuadros donde la cabeza está más alta antes de entregar.
- **Gancho (título del comienzo):**
  - Va arriba, al tamaño de los subtítulos (92), en 1 o 2 líneas, sin tocar los bordes.
  - Si mi cabeza queda alta (modo selfie), usá `cartel_y` 272 y `tamano` 86: el recuadro empieza justo en el límite de 250 px y no toca la cara.
- **Imágenes superpuestas:** van arriba, sobre el techo o la pared (por ejemplo, tarjetas de 980×190 en `y` 255). Si no entra sin tapar la cabeza, usá pantalla dividida (`bajar`/`alto`) o pantalla completa.

### 7. Subtítulos

- Durante todo el video, con letra Inter Display Black, en blanco con borde negro, de 2 o 3 palabras por bloque y con una entrada con rebote.
- **Palabras clave en turquesa** (#14B1C7): el dolor (músculo, cansás, panza), la solución (fuerza, 8 semanas, 15 minutos, bajo impacto, segura) y los nombres (RENOVA, deportólogo).
- Un número va siempre con su palabra: "8 SEMANAS", "15 MINUTOS".

### 8. Recursos según lo que digo

**Productos** (a pantalla completa, imagen **fija, sin zoom**: `fijo` true):

| Lo que digo | Qué se muestra |
|---|---|
| "RENOVA" / "el pack" / "bonus de regalo" | `pack-renova/pack_1.png` |
| "en casa" | `pack-renova/libro_1_casa.png` |
| "gimnasio" | `pack-renova/libro_2_gimnasio.png` |
| "guía de nutrición" / "alimentación" | `pack-renova/libro_3_alimentacion.png` |
| "rutinas express de 15 minutos" | `pack-renova/bonus_express.png` |

Las tapas (`libro_*`) llevan `fondo` #0b1416 y `zoom` 1.15 fijo.

**Personas y talleres:**
- **Talleres / psicóloga:** Agostina dando el Taller de hábitos (Drive, seg. 575), armado vertical con su cámara arriba y la diapositiva abajo, 2 s.
- **Médico deportólogo:** tarjeta arriba con la foto de Rodrigo (`fuentes/landing/img/equipo_rodrigo.jpg`), "Dr. Rodrigo Portillo Ruffa · Médico traumatólogo y deportólogo", 2 s. Plantilla: `fuentes/landing/mockups/reels/tarjetas_pierdes_musculo.html`.

**Conceptos** (tarjeta arriba, sin tapar cabeza ni subtítulos):
- "perdés músculo" → 💪 con flecha roja hacia abajo y barras que bajan.
- Otros conceptos: misma plantilla.

**B-roll:**
- **Cuando hablo de entrenar fuerza** (o cuando miro a otro lado): clientas entrenando fuerza a pantalla completa (carpeta `1J2_w83crv0ZeotXJk-kIBzI6NnM8J6ut`). Verticales:
  - `20190421_151852`: sentadilla;
  - `20190421_150532`: estocadas;
  - `WhatsApp 2026-03-30 1.55.54`: press con mancuernas;
  - `WhatsApp 2026-03-30 1.55.49`: sentadilla con banda.
- **Cuando hablo del problema** (cansancio, dolor): el b-roll que venga en la carpeta del video.

### 9. Antes de entregar

- Revisá cuadros sueltos en:
  - el gancho;
  - cada corte;
  - cada transición;
  - la entrada y salida de cada imagen o clip;
  - la vuelta a cámara;
  - el cierre.
- Confirmá que no se tapa ninguna cabeza y que todo está dentro de las zonas seguras.
- Escuchá (midiendo el audio) que ninguna frase quede cortada.

### 10. Forma de trabajo

- Mandame el video y un resumen corto: qué pusiste, en qué frase y cuánto dura. Si algo no pudo durar exactamente lo pedido, explicame por qué.
- Si te paso correcciones de a una, respondé solo "ok" a cada una y **no edites hasta que te diga "comenzá"**.
- Al terminar:
  - guardá la configuración en `execution/reels/<nombre>.json`;
  - anotá en `directives/editar_reel.md` lo nuevo que aprendas;
  - subí todo al repositorio.
