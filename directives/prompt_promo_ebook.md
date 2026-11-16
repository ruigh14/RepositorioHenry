# PROMO EBOOK · prompt para editar reels que venden el pack RENOVA (modelo: "¿Hay que entrenar todos los días?", 15/11/2026)

> Para los reels del día a día se usa `directives/prompt_edicion_diaria.md` (EDICIÓN DIARIA). Las reglas técnicas son las mismas en los dos: zonas seguras, gancho más arriba en modo selfie (`cartel_y` 272, `tamano` 86), tarjetas arriba y tiempos.

Copiar, completar lo que está entre [corchetes] y pegar en una conversación nueva. Referencia técnica: `directives/editar_reel.md`; configuración modelo: `execution/reels/no-todos-los-dias.json`.

---

Editá este video como reel de Instagram en el estilo RENOVA: [link de Google Drive del video]

Usá `execution/editar_reel.py` y `directives/editar_reel.md`, con `execution/reels/no-todos-los-dias.json` como modelo. Seguí estas reglas:

**1. Preparación**
- Bajá el video de Drive a `.tmp/<nombre>/`. Si es HDR (iPhone), pasalo a SDR 1080×1920 antes de editar.
- Transcribí con Whisper y leé la transcripción completa antes de decidir nada: sacá las tomas falsas y corregí los subtítulos al voseo y al nombre real de los productos (por ejemplo "E-BOOKS", "Hacé clic", "pack RENOVA").
- Los subtítulos dicen lo mismo que yo digo en el video, aunque mi frase no sea perfecta.

**2. Cortes de silencio**
- Es una charla fluida: usá `cortar: "oraciones"`. Solo se cortan los silencios entre oraciones, nunca dentro de una frase.
- Cada oración tiene que terminar completa: confirmá con el audio, no solo con los tiempos de Whisper (puede correr una palabra a un silencio y el corte la borra).
- Si te digo que una parte va sin cortes (una mueca al principio, el cierre "si llegaste hasta acá…"), usá `sin_cortes`.

**3. Transiciones**
- Destellos, transiciones y cambios de toma (entrada al b-roll, cambio de clip, vuelta a cámara) van siempre en un silencio: en la unión de dos tramos cortados o en una pausa medida en el audio. Nunca en medio de una palabra.
- Transición sutil cuando cambio de tema: "Soy Nacho Portillo" y el llamado final ("Hacé clic…").
- Destello después de un silencio largo que separa dos ideas (por ejemplo, al pasar del problema a "La realidad es que…"), con el b-roll entrando con corte seco.

**4. Gancho**
- La pregunta o idea del principio va arriba, en la zona segura, al mismo tamaño que los subtítulos (92), en una o dos líneas, sin tocar los bordes.

**5. B-roll de clientas**
- Cuando hablo de entrenar fuerza (o cuando miro a otro lado), van clientas entrenando fuerza a pantalla completa, unos 1,5 a 2,5 segundos cada una, cambiando en mis micro-pausas.
- Los clips salen de la carpeta de Drive `1J2_w83crv0ZeotXJk-kIBzI6NnM8J6ut` (sentadilla, estocadas, press con mancuernas, sentadilla con banda).

**6. Productos a pantalla completa, imagen fija (sin zoom)**
- "RENOVA" / "el pack" → `pack-renova/pack_1.png` (3 ebooks + 5 bonus).
- "casa" → `libro_1_casa.png`; "gimnasio" → `libro_2_gimnasio.png`; "guía de nutrición / alimentación" → `libro_3_alimentacion.png`.
- "rutinas express" → `bonus_express.png`.
- "talleres" → Agostina en el Taller de hábitos (Drive `1Uid63Yq6lt3jqdnuAlrGo4AtHikXtZ-J`, seg. 575), vertical: cámara arriba y diapositiva abajo.
- "otros bonus de regalo" → el pack.
- Cada imagen aparece justo cuando lo nombro y dura lo que dura esa parte de la frase (idealmente 2 segundos).

**7. Cierre**
- Placa final con el pack a pantalla completa, 2,5 s, con fundido.

**8. Reglas fijas**
- Nunca tapar ni cortar mi cabeza ni la de nadie con imágenes.
- Palabras clave en turquesa en los subtítulos (números con su palabra: "8 SEMANAS", "15 MINUTOS").
- Antes de mandarme el video, revisá cuadros sueltos en cada corte, transición e imagen.

**9. Forma de trabajo**
- Si te doy correcciones de a una, respondé "ok" a cada una y no edites hasta que te diga "comenzá".
- Al terminar, guardá la configuración en `execution/reels/<nombre>.json`, anotá en la directiva lo nuevo que aprendas y subí los cambios al repositorio.

[Indicaciones propias de este video: momentos especiales, qué mostrar y dónde, partes sin cortes.]
