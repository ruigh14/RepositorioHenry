# Instrucciones para el Agente

> Crea un archivo CLAUDE.md, AGENTS.md y GEMINI.md con todo el contenido de este prompt, crea el sistema de carpetas y la estructura indicada más abajo para preparar el workspace y asegúrate de que los archivos CLAUDE.md, AGENTS.md y GEMINI.md estén siempre iguales, así que si haces un cambio o registras un aprendizaje en uno de estos tres archivos, deberás replicarlo en los demás para que el sistema cargue en cualquier entorno de IA agéntica.
>
> **Cómo mantenerlos sincronizados:** edita cualquiera de los tres y luego ejecuta `python3 execution/sync_agent_files.py` (copia el archivo modificado más recientemente a los otros dos). Para solo verificar sin escribir: `python3 execution/sync_agent_files.py --check`.

## Aprendizajes del Agente (Mejora Continua)

> **INSTRUCCIÓN CRÍTICA — LEER PRIMERO:** Esta sección es tu memoria persistente de mejora continua. **Con cada ciclo de ejecución** (al completar una tarea, resolver un error, descubrir un patrón, o ajustar un flujo) **y con cada actualización de cualquier Markdown** (directivas, CLAUDE.md, AGENTS.md, GEMINI.md, READMEs de scripts), **debes agregar aquí un aprendizaje nuevo** si surgió algo no trivial. El objetivo es que este archivo se vuelva más útil y preciso con el tiempo, acumulando conocimiento del proyecto que no se pierde entre sesiones.
>
> **Qué registrar:** restricciones de APIs descubiertas, rate limits reales, patrones que funcionan, errores que se repiten, decisiones de diseño tomadas con el usuario, supuestos que resultaron falsos, atajos útiles, gotchas del entorno.
>
> **Qué NO registrar:** detalles efímeros de una sola tarea, información ya documentada en la directiva correspondiente, cosas triviales derivables del código.
>
> **Formato de cada aprendizaje:**
> ```
> - **YYYY-MM-DD — [Tema corto]:** Descripción del aprendizaje en 1-3 líneas. **Por qué importa:** consecuencia práctica o cómo aplicarlo en el futuro.
> ```
>
> **Higiene:** si un aprendizaje queda obsoleto o se contradice con otro más reciente, actualízalo o elimínalo en vez de acumular ruido. Mantén la lista ordenada por fecha (más recientes arriba). Si superas ~25 entradas, consolida las más antiguas o promuévelas a la directiva que corresponda.

### Registro de aprendizajes

- **2026-11-13 — Guiones también en Drive:** Nacho arma y edita guiones en su Google Drive ("guiones ganadores", "GUIONES", "Guiones_RENOVA.txt", misma carpeta) y no siempre llegan al repositorio. **Por qué importa:** si pide guiones "que habíamos armado" y no están en `guiones/`, buscarlos en Drive (`title contains 'guion'`) y copiarlos al repositorio; su versión editada manda sobre la nuestra.
- **2026-11-13 — Fotos con Higgsfield (plan gratuito):** el plan gratis no permite `gpt_image_2_6` ("Requires basic plan"); `z_image` sí (0,15 créditos por foto, 2048 px, fotorrealista) y a veces da 429 si se mandan muchas juntas: reintentar la que falló. Los resultados se bajan de `d8j0ntlcm91z4.cloudfront.net` (habilitado en el entorno RepositorioHenry). **Por qué importa:** para fotos de recetas usar `z_image` con el estilo de la casa (plato blanco, mármol, servilleta turquesa, luz natural) y reducirlas a 600 px.
- **2026-11-11 — Landing editada directo en Impultienda:** la versión publicada tenía un encabezado con menú lateral que no estaba en `fuentes/landing/tienda.html`; regenerar la landing lo hubiera borrado. **Por qué importa:** antes de mandar una landing regenerada, pedirle a Nacho el HTML publicado (o comparar con el último que pegó) y traer al repositorio cualquier cambio hecho afuera; todo el JS va en `landing.js`, nunca en un `<script>` del HTML.
- **2026-11-11 — Velocidad de la landing (Clarity: LCP 3,7 s):** el VSL de la portada no puede llevar la animación `.rv` (arranca con opacidad 0) y necesita su portada (`https://fast.wistia.com/embed/medias/<id>/swatch`, precargada con prioridad alta); las imágenes debajo de la portada van con `loading="lazy" decoding="async"`. **Por qué importa:** el 73% del tráfico llega desde el navegador de Instagram, donde cada segundo de carga pierde gente; aplicar lo mismo en la landing de MÉTODO 40.
- **2026-11-11 — Guiones ganadores:** los guiones que funcionaron se guardan en `guiones/ganadores/` (con el texto y el análisis de por qué funciona) y los nuevos en `guiones/propuestas/`. **Por qué importa:** antes de escribir cualquier guion o copy para Nacho, leer los ganadores y replicar su estructura y su voz.
- **2026-11-11 — Ebook Sin TACC:** producto aparte; recetas tomadas de `nutricion.py` vía import (no duplicar), sin avena (en Argentina TACC incluye avena); testimonios del programa RENOVA en general, sin nombre y aclarado como tal; nada de precios en el ebook ni en la landing salvo los tokens de Impultienda. **Por qué importa:** cualquier producto nuevo para celíacos sigue estas reglas; ver `investigacion/sin-tacc/`.
- **2026-11-11 — Rama de trabajo unida a main:** esta rama ya incluye todo `main` (ebooks en `fuentes/`, landing, PDF); las notas del proyecto RENOVA de `main` van al final de este archivo, debajo del `---`. **Por qué importa:** al traer cambios de `main`, resolver CLAUDE.md conservando las dos partes y volver a sincronizar AGENTS.md y GEMINI.md.
- **2026-11-10 — ffmpeg: exp() en expresiones por cuadro:** `gte(t,T)*exp(-(t-T)*k)` da NaN antes de T cuando el exponente pasa de ~709 (0·inf) y la imagen sale negra; usar `exp(-max(t-T,0)*k)`. **Por qué importa:** cualquier efecto animado con exp() en `eq`/`scale` con `eval=frame` necesita el `max()`.
- **2026-11-10 — Preferencias de Nacho en reels:** nunca tapar ni cortar la cabeza con imágenes; para mostrar "todo lo que ofrecemos" prefiere el mockup completo con fondo azul (`pack-renova/pack_completo.png`, incluye los talleres) en pantalla dividida. **Por qué importa:** aplicarlo por defecto en cada reel nuevo (ver `directives/editar_reel.md`).
- **2026-11-10 — Edición de reels:** `execution/editar_reel.py` + `directives/editar_reel.md` hacen la edición completa con un JSON por reel; Whisper necesita huggingface.co y us.aws.cdn.hf.co habilitados en el entorno y `HF_HUB_DISABLE_XET=1`. **Por qué importa:** antes de editar a mano, copiar el JSON de ejemplo, revisar la transcripción para sacar tomas falsas y correr el script.
- **2026-10-13 — Sincronización de CLAUDE.md / AGENTS.md / GEMINI.md:** Los tres archivos deben ser idénticos byte a byte; la sincronización se hace con `execution/sync_agent_files.py` (toma como fuente el modificado más recientemente, o la indicada con `--source`). **Por qué importa:** nunca edites los tres a mano por separado; edita uno, ejecuta el script y verifica con `--check` antes de hacer commit.

<!-- Agrega nuevas entradas arriba de esta línea. -->

---

Tú operas dentro de una arquitectura de 3 capas que separa responsabilidades para maximizar la confiabilidad. Los LLMs son probabilísticos, mientras que la mayoría de la lógica de negocio es determinista y requiere consistencia. Este sistema resuelve esa incompatibilidad.

## La Arquitectura de 3 Capas

**Capa 1: Directiva (Qué hacer)**
- Básicamente son SOPs escritos en Markdown, ubicados en `directives/`
- Definen los objetivos, entradas, herramientas/scripts a usar, salidas y casos extremos
- Instrucciones en lenguaje natural, como las que le daría a un empleado de nivel medio

**Capa 2: Orquestación (Toma de decisiones)**
- Esta es tu función. Tu trabajo: enrutamiento inteligente.
- Leer directivas, llamar herramientas de ejecución en el orden correcto, manejar errores, pedir aclaraciones, actualizar directivas con los aprendizajes
- Tú eres el puente entre la intención y la ejecución. Por ejemplo, no intentes hacer scraping de sitios web por tu cuenta—lee `directives/scrape_website.md`, define entradas/salidas y luego ejecuta `execution/scrape_single_site.py`

**Capa 3: Ejecución (Hacer el trabajo)**
- Scripts de Python deterministas en `execution/`
- Variables de entorno, tokens de API, etc. se almacenan en `.env`
- Manejan llamadas a APIs, procesamiento de datos, operaciones de archivos e interacciones con bases de datos
- Confiables, testeables, rápidos. Use scripts en vez de trabajo manual.

**Por qué funciona esto:** si tú haces todo por tu cuenta, los errores se acumulan. Un 90% de precisión por paso = 59% de éxito en 5 pasos. La solución es empujar la complejidad hacia código determinista. Así tú te concentras solo en la toma de decisiones.

## Principios de Operación

**1. Revise primero si existen herramientas**
Antes de escribir un script, revisa `execution/` según tu directiva. Solo crea scripts nuevos si no existe ninguno.

**2. Auto-corrección cuando algo falla**
- Lee el mensaje de error y el stack trace
- Corrige el script y pruébalo de nuevo (a menos que use tokens/créditos de pago—en ese caso consulta primero con el usuario)
- Actualiza la directiva con lo que aprendiste (límites o rate limits de API, tiempos, casos extremos)
- Ejemplo: si llegas al rate limit de una API → investigas la API → encuentras un endpoint batch que soluciona el problema → reescribes el script → pruebas → actualizas la directiva.

**3. Actualice las directivas a medida que aprende**
Las directivas son documentos vivos. Cuando descubras restricciones de API, mejores enfoques, errores comunes o expectativas de tiempo—actualiza la directiva. Pero no crees ni sobreescribas directivas sin preguntar, a menos que se te indique explícitamente. Las directivas son tu conjunto de instrucciones y deben preservarse (y mejorarse con el tiempo, no usarse de manera improvisada y luego descartarse).

## Ciclo de Auto-corrección

Los errores son oportunidades de aprendizaje. Cuando algo falla:
1. Corrija el problema
2. Actualice la herramienta
3. Pruebe la herramienta, asegúrese de que funcione
4. Actualice la directiva con el nuevo flujo
5. El sistema ahora es más robusto

## Organización de Archivos

**Estructura de directorios:**
- `.tmp/` - Todos los archivos intermedios (dossiers, datos scrapeados, exportaciones temporales). Nunca se suben al repositorio, siempre se regeneran.
- `execution/` - Scripts de Python (las herramientas deterministas).
- `directives/` - SOPs en Markdown (el conjunto de instrucciones).
- `.env` - Variables de entorno y claves de API.
- `credentials.json`, `token.json` - Credenciales de OAuth de Google (solo cuando el flujo los requiera; en `.gitignore`).

**Principio clave:** Los archivos intermedios viven en `.tmp/` y pueden borrarse siempre. Cualquier salida del flujo debe ser reproducible ejecutando el flujo de nuevo, nunca editada a mano.

## Resumen

Tú estás entre la intención humana (directivas) y la ejecución determinista (scripts de Python). Lee instrucciones, toma decisiones, llama herramientas, maneja errores y mejora el sistema continuamente.

Se pragmático. Se confiable. Auto-corríjete.

---

# Proyecto RENOVA

Repositorio de RENOVA, el programa de entrenamiento, alimentación y descanso de Nacho Portillo.
Todo el trabajo se guarda acá, en la rama `main`. Lo que no se commitea y pushea se pierde al cerrar la sesión.

## Estructura

Hay **una sola landing**, la de la tienda (renova.impultienda.ar; dominio propio comprado: **metodorenova.fit**, en Namecheap, 1 año desde el 1/11/2026, a conectar con Impultienda), donde se venden los **dos ebooks** (casa + gimnasio en una misma compra). Cada ebook tiene su carpeta. El código que los genera está en `fuentes/` y es uno solo para todos: no duplicarlo por producto.

```
tienda/
  landing-impultienda.html   → la landing de renova.impultienda.ar (se pega en Diseño de tienda → HTML propio)
  landing-metodo40.html      → la landing de MÉTODO 40 (hombres 40+), para la otra tienda de Impultienda
entrena-desde-casa/          Ebook 1
  Ebook_Entrena_desde_casa_RENOVA.pdf
entrena-en-el-gimnasio/      Ebook 2: misma lógica, rutinas de gimnasio nivel inicial
  Ebook_Entrena_en_el_gimnasio_RENOVA.pdf
entrena-siendo-mama/         Ebook 3: mamás que vuelven a entrenar (respiración, piso pélvico, sin impacto) + pausa activa
  Ebook_Entrena_siendo_mama_RENOVA.pdf
alimentacion-inteligente/    Plan de nutrición de 8 semanas (lo vende la landing): educación breve + organización + programa de 8 semanas con 32 recetas. Lo genera fuentes/ebook/nutricion.py (nutricionista: Lic. María Eugenia Aldrey, M.N. 11773; suma 6 recetas, reemplazos e imágenes de su recetario y su catálogo de productos en img/eve/ e img/prod/)
  Ebook_Alimentacion_Inteligente_RENOVA.pdf
sin-tacc-inteligente/        Upsell (Nacho lo decidió el 13/11/2026; antes iba a ser producto aparte): "Sin TACC Inteligente" (39 hojas): lista de compras Sin TACC, etiquetas (logos "Sin T.A.C.C." y "sin GLUTEN", Res. Conjunta 32/2023), cocina segura, fibra y proteína, plato, semana 80/20 (siempre Sin TACC), 18 recetas (12 de Alimentación Inteligente adaptadas + 6 argentinas en BORRADOR hasta que Eugenia las valide; fotos img/food/st_*.jpg de Higgsfield), bonus Skool, imprimibles, cierre con consulta con Eugenia. Sin testimonios ni referencias. Lo genera fuentes/ebook/sintacc.py. Estrategia y revisión: investigacion/sin-tacc/
nutricion-menopausia/        Upsell: Nutrición en la menopausia (30 hojas, registro de 14 días, hábitos prioritarios, 10 capítulos, perimenopausia, nutrientes clave, casos, guía de consulta, referencias con DOI, etapas, fotos en img/meno/, registro de síntomas; revisión Eugenia). Lo genera fuentes/ebook/menopausia.py
  Ebook_Nutricion_Menopausia_RENOVA.pdf
gluteos-fuertes/             Upsell: Glúteos Fuertes, 2 ebooks que se entregan juntos (24 hojas cada uno, cada hoja armada completa: sin cortes ni huecos). El día extra de RENOVA para mujeres 40+: un día por semana (3.º si entrena 2 veces, 4.º si entrena 3), 8 semanas, 3 rutinas que rotan (1 empuje de cadera, 2 bisagra, 3 una pierna; máximo 2 ejercicios repetidos entre rutinas) + sesión express; sin test (Nacho lo sacó); progresión (en casa, sin más peso: bajada lenta, pausa o versión a una pierna), 8 errores, proteína, sesión express, planilla de cargas, 50% off plan integral. Casa: mancuernas, banda, silla, escalón + capítulo "Mantenete activa" (10 consejos: entrenar no compensa 9 horas sentada; pausa activa). Gimnasio: barra, máquinas, prensa + "10 consejos para el gimnasio" y plan B si la máquina está ocupada. Solo ejercicios con ilustración y video de Harbiz ya existentes. Los genera fuentes/ebook/gluteos.py casa|gym
  Ebook_Gluteos_Fuertes_Casa_RENOVA.pdf
  Ebook_Gluteos_Fuertes_Gimnasio_RENOVA.pdf
  creativos/                 3 portadas (1080×1350; la elegida es portada_1, libro 3D con los 2 ebooks) y video de 4 s (1080×1920): fuentes/landing/mockups/gluteos_promo.py && node gluteos_promo.js (necesita ffmpeg)
ebook-hombres/               Proyecto EBOOK HOMBRES · MÉTODO 40 (submarca para hombres 40+, se vende en la otra tienda de Impultienda): 2 ebooks que se entregan juntos, Casa y Gimnasio (28 hojas c/u). Autor Ignacio Portillo. 8 semanas, 3 rutinas de cuerpo completo A/B/C, descarga en la 5. Cada ejercicio: captura y link de su video propio en Harbiz (marca LEVEL UP, Nacho decidió dejarla), músculos, técnica, error a evitar y opción principiante. Paleta: tokens --m40-* (negro, grises, rojo), body.m40. Lo genera fuentes/ebook/hombres.py casa|gym; imágenes en img/m40/; estructura en investigacion/metodo-40/estructura-ebooks.md
  Ebook_Metodo40_Casa.pdf
  Ebook_Metodo40_Gimnasio.pdf
  Ebook_Metodo40_Metricas.pdf   Guía de métricas (gratis en el pack)
  Ebook_Metodo40_Zona_Media.pdf  Upsell "Zona media fuerte" (20 hojas): mitos y verdades, punto fijo y móvil (toes to bar = psoas), giro ruso y cizallamiento, respiración en flexiones y planchas, 4 rutinas de planchas, flexiones y mountain climbers (sin twists ni toes to bar), 2 veces por semana al final de una sesión, plan ondulado. También está en la app, en la pestaña Zona media: se destraba con CODIGO_ABD = ZONA40 (hombres.py; figura solo en este ebook, hoja "Zona media en tu app"). build.py cifra esas rutinas con ese código (PBKDF2 + HMAC, sin dependencias), así que no se leen mirando la página. `python3 hombres.py abdomen && node export.js hombres_abdomen`
  Ebook_Metodo40_Alimentacion_Inteligente.pdf  Va DENTRO del pack (Nacho lo decidió el 8/11/2026). Plan de nutrición de 8 semanas para hombres 40+: la misma guía que Alimentación Inteligente (mismas 38 recetas), en masculino y con paleta MÉTODO 40, más 5 hojas propias (comer alrededor del entrenamiento, combinaciones para el día de entrenamiento, testosterona después de los 40, asado/alcohol/fin de semana, si no progresás: ajustá en 14 días). Lo genera `python3 nutricion.py hombres && node export.js hombres_nutricion` (textos que cambian: X(mujeres, hombres))
comunidad/                   Bonus (PDF aparte): Acceso a la comunidad RENOVA (portada + cómo entrar a Skool y ver los talleres en Cursos). Lo genera fuentes/ebook/comunidad.py && node comunidad.js
  Bonus_Acceso_comunidad_RENOVA.pdf
pausa-activa/                Bonus (PDF aparte) de casa y gimnasio: explicación + 4 rutinas de pausa activa de 10 min + plan personalizado
  Bonus_Pausa_activa_RENOVA.pdf
programa-renova-completo/    Entrenamiento + alimentación + descanso (base de los upsell)
  Ebook_Programa_RENOVA.pdf
investigacion/               material de referencia (VSL del competidor, etc.)
guiones/                     guiones para filmar: ganadores/ (los que funcionaron: referencia de voz) y propuestas/
fuentes/
  design-system/             tokens, tipografías, componentes y plantillas de creativos (ver su README.md)
  ebook/                     genera los 3 PDF
  landing/                   genera la landing de la tienda
```

Cada ebook tiene además `creativos/` (imágenes, carrusel y videos para Instagram y Facebook), generados desde `fuentes/design-system/creativos/`.

**No editar a mano** los PDF ni `tienda/landing-impultienda.html`: se regeneran desde `fuentes/`.

### `fuentes/design-system/`
Una sola marca para todo: **los colores son los del ebook** y landings, creativos y videos usan exactamente esa paleta (nada de colores sueltos: si hace falta uno, se agrega como token). `tokens.css` es la fuente única; el ebook y las landings usan alias que apuntan a los tokens. `design_system.py` tiene `css()`, los íconos, los componentes del ebook y las reglas de venta (`DESCARGO`, `GARANTIA = None` hasta que Nacho la defina). `creativos/datos.py` tiene los textos de los creativos de cada producto. Todo está explicado en `fuentes/design-system/README.md`; la muestra visual es `muestra.pdf`.

### `fuentes/ebook/`
- `build.py`: todos los textos, recetas, menús, ejercicios (cada rutina en 3 hojas: entrada en calor, bloque 1, bloque 2; elongación al final), plan de 8 semanas (`PLAN8`), pausa activa (`PAUSA`, `TIPS_DIA`), extra de zona media (`CORE`) y links (`LINKS`; `VIDEOS` = links de Harbiz de cada ejercicio). Cuatro ediciones: `completo`, `entrena` (casa), `gimnasio` y `mamas` (`GYM`; los textos que cambian entre casa y gimnasio usan `G(casa, gym)`; rutinas armadas a partir de las de gimnasio de Nacho en Harbiz, ilustraciones `img/gym_*.png` de Canva). En `mamas` los textos que cambian van como tercer argumento: `G(casa, gym, mama)`; tiene capítulo 02 "Antes de empezar" (alta médica, señales para frenar, diástasis, respiración y piso pélvico), rutinas sin saltos ni abdominales clásicos, "Entrená con tu bebé" e ilustraciones `img/mama_*.png` de Canva.
- Orden de los ebooks de entrenamiento (lo arma `render()` con `SECS`, que también numera capítulos e índice): portada → bienvenida ("Empezá esta semana") → índice → [mamás: Antes de empezar] → casa y gimnasio: Cómo entrenar ("Cómo se hace cada rutina") → Rutinas 1–3 (cada una con su entrada en calor) → elongación (6 posturas, 1 hoja) → Rutinas extras (zona media + sesión express) → Tu plan de 8 semanas (cuadro semanas 1–4 + "Ahora progresamos y aumentamos", semanas 6–8, con descarga en la 5); mamás: el plan va antes de las rutinas → semanas con poco tiempo (sesión express) → [mamás: pausa activa] → Medí tu progreso (medición + registro) → después de las 8 semanas → bonus → resultados reales → quién soy → método RENOVA. Una página nueva tiene que sumarse a `SECS` o el build falla.
- Edición `pausa` (`PAUSA_ED`): bonus de casa y gimnasio, 7 hojas (portada, cómo hacerla, 4 rutinas de 10 min con ejercicios verificados en la biblioteca de Harbiz de Nacho, llamado al plan personalizado). En casa y gimnasio ya no hay pausa activa adentro; en mamás sí.
- `ebook.html`, `entrena.html`, `gimnasio.html`, `mamas.html`, `pausa.html`: HTML intermedio que genera `build.py` (no editar).
- `style.css`: diseño. `paginate.js`: paginación automática A4. `export.js`: exporta el PDF con Playwright a la carpeta del producto.
- `img/`: fotos, ilustraciones, recetas y testimonios. Las tipografías están en `fuentes/design-system/fonts/`.
- Talleres: están en Skool (https://www.skool.com/renova-entrenamiento-y-salud-1617/about); el bonus de talleres de los ebooks tiene un botón grande que lleva ahí. No hay ebook de talleres ni página de upsell.

### `fuentes/landing/`
- `tienda.html`: fuente de la única landing (vende los 2 ebooks juntos, con un solo `/checkout`; el producto de Impultienda tiene que entregar los 2 PDF). `build.py` encierra el CSS en `#rnv` (para que no choque con la tienda) y cambia `img/...` por links de jsDelivr (CDN, más rápido) a `fuentes/landing/img/`, fijados al último commit de esa carpeta: **commitear y pushear las imágenes nuevas antes de regenerar**. Los videos (`<source src="img/….mp4">`) salen de jsDelivr con GitHub de respaldo.
- Estructura (correcciones de Nacho, modelo Menofit): encabezado fijo (logo + oferta con cuenta regresiva que lleva a #comprar + menú lateral con las secciones; el menú se cierra desde `landing.js`) → portada oscura (petróleo + turquesa) con franja del equipo, título, bajada, "Programa interdisciplinario", el VSL (`.vsl`: Wistia `9xn7yk66az`, arranca en silencio y en loop; al tocarlo `landing.js` lo reinicia con sonido) → ¿Te pasa esto? → No es tu culpa → testimonios ("…no es opcional, ¡es preventivo!") → pilares (fuerza, nutrición, hábitos) → "Esto es lo que incluye": programa de entrenamiento y plan de nutrición (`img/mock_nutricion.jpg`) → 5 bonos (pausa activa, express, abdominales, talleres, comunidad) → quién soy + carrusel deslizable del equipo (Nacho, Lic. María Eugenia Aldrey nutricionista, Lic. Agostina Galiani psicóloga, Dr. Rodrigo Portillo Ruffa médico traumatólogo y deportólogo) → valor $100.000 / hoy $35.000 + upsell → garantía → preguntas → cierre. Todos los botones van a `/checkout`. Precios con los tokens de Impultienda (`{{price}}` = $35.000, `{{original_price}}` = $100.000, `{{savings}}`): se cargan en el producto. No hay valores escritos fijos: todos los montos salen del carrito de Impultienda.
- Imágenes armadas: `fuentes/landing/mockups/` (`python3 mockups.py && node mockups.js`). Mockups del pack para Meta Ads (3 ebooks + 5 bonus, 1080×1920, tapas reales en `mockups/pack/`): `python3 pack.py && node pack.js` → `pack-renova/pack_1..3.png`; los 3 libros con borde futurista y fondo transparente: `python3 libros.py && node libros.js` → `pack-renova/pack_libros.png`; cada tapa en 3D (1080×1350) y las 3 juntas (1920×1080) con fondo: `python3 libros3d.py && node libros3d.js` → `pack-renova/libro_*.png` y `libros_juntos.png`. Fotos de Nacho: `img/foto_*.jpg`, sacadas de sus videos de ejercicios.
- Upsell 1: ebook "Nutrición en la menopausia" (texto e imagen `img/tapa_menopausia.jpg` fijos; precio con el token `{{upsell_1_price}}`: se carga en Impultienda, $10.000, botón `data-upsell-toggle="1"`). 
- Impultienda: compra con `<a href="/checkout">`, precios con `{{price}}`, `{{original_price}}`, `{{savings}}` y upsell 1 con `{{upsell_1_*}}` + `data-upsell-toggle="1"`.

## Regenerar

```
cd fuentes/ebook && python3 build.py entrena && node export.js entrena     # Entrená desde casa
cd fuentes/ebook && python3 build.py gimnasio && node export.js gimnasio   # Entrená en el gimnasio
cd fuentes/ebook && python3 build.py mamas && node export.js mamas         # Entrená siendo mamá
cd fuentes/ebook && python3 build.py pausa && node export.js pausa         # Bonus: pausa activa
cd fuentes/ebook && python3 build.py && node export.js                     # Programa RENOVA completo
cd fuentes/ebook && python3 nutricion.py && node export.js nutricion        # Alimentación Inteligente (nutrición 8 semanas)
cd fuentes/ebook && python3 menopausia.py && node export.js menopausia      # Upsell: Nutrición en la menopausia
cd fuentes/ebook && python3 sintacc.py && node export.js sintacc            # Sin TACC Inteligente (producto aparte)
cd fuentes/ebook && python3 gluteos.py casa && node export.js gluteos_casa  # Upsell: Glúteos Fuertes en casa
cd fuentes/ebook && python3 gluteos.py gym && node export.js gluteos_gym    # Upsell: Glúteos Fuertes en el gimnasio
cd fuentes/ebook && python3 hombres.py casa && node export.js hombres_casa  # MÉTODO 40 en casa
cd fuentes/ebook && python3 hombres.py gym && node export.js hombres_gym    # MÉTODO 40 en el gimnasio
cd fuentes/ebook && python3 nutricion.py hombres && node export.js hombres_nutricion  # MÉTODO 40: Alimentación Inteligente
cd fuentes/landing && python3 build.py                                     # la landing de la tienda
cd fuentes/landing && python3 build.py hombres                             # la landing de MÉTODO 40 (tienda_hombres.html: usa todo el CSS de tienda.html + su paleta)
cd fuentes/design-system/creativos && python3 generar.py && node exportar.js   # creativos (imagen | video)
cd fuentes/design-system && python3 muestra.py && node muestra.js           # muestra.pdf del design system
```

Si Playwright no tiene su Chromium descargado, usar el Chrome instalado: `PW_CHANNEL=chrome node export.js …`.

El ebook debe imprimir `OVERFLOW []` (sin páginas con texto cortado). Para revisar el texto de un PDF: `pdftotext -layout <pdf> /tmp/x.txt`.

## Estrategia de producto

- **Nacho no hace acompañamiento:** no usar "te acompañamos", "trabaja con vos" ni "programa de acompañamiento" (mamás todavía lo tiene).
- **Landing y creativos:** no se vende consulta ni acompañamiento. El bonus 3 es el **acceso a la comunidad RENOVA en Skool** (cursos y talleres; interactuar con otras mujeres es opcional). En la landing, WhatsApp solo para problemas con la compra.
- **Adentro del ebook (después de comprar):** sí está la oferta de Nacho: **50% off en el plan integral RENOVA de entrenamiento y nutrición** (casa, gimnasio y bonus; en mamás todavía dice "plan personalizado"), contactándolo por WhatsApp (`LINKS["wa_plan"]`, capítulo "Después de las 8 semanas") y el botón "Quiero sumarme a RENOVA" (`LINKS["renova"]`). No hay consulta gratis.

- Ebook 1 (solo entrenamiento) es el producto de entrada; alimentación (menús, compras) y descanso quedan para ebooks de upsell.
- El equipo incluye **médico deportólogo** (medicina deportiva): mantenerlo en ambas ediciones.
- Investigación de mercado de referencia: Google Doc "RENOVA_investigacion_ebooks_entrenamiento_mujeres_40_plus".

## Forma de trabajo

- Editar textos y contenido del ebook en `fuentes/ebook/build.py`, no en los `.html` (se regeneran).
- Después de cada cambio: regenerar el PDF (o la landing), commitear y pushear a `main`.
- Idioma: español rioplatense (voseo).
- Se lee en el celular: letra grande (cuerpo 15 pt). Si algo no entra en la hoja, acortar texto o separar en hojas, no achicar la letra.
- Casa, gimnasio y pausa llevan `<body class="grande">` (bloque `.grande` al final de `style.css`): desarrollo a 15,5–16,5 pt y dibujos de ejercicios de 40 mm; `paginate.js` reparte lo que no entra. Mamás todavía usa los tamaños anteriores.

## Frase para retomar: "RENOVA, seguimos"

Cuando Nacho escriba **"RENOVA, seguimos"** (en esta conversación o en una nueva), antes de hacer nada:
1. Leer este archivo y `git log --oneline -15` para ver lo último que se hizo.
2. Responder con un resumen corto: en qué quedó cada proyecto y qué está pendiente (sección siguiente).
3. Preguntar con qué sigue.

## Pendientes

- Landing MÉTODO 40 (tienda/landing-metodo40.html, 9/11/2026): misma landing que la de mujeres con paleta MÉTODO 40, fotos y videos de HOMBRES/ (copias livianas en fuentes/landing/img/m40_*). Testimonios con resultados reales (Nico +3 kg de músculo, Victor −10 kg de grasa, Dani +4 kg de músculo, Martín músculo y −8 kg de grasa); el carrusel "Así se entrena" es solo material (fotos y videos de Fabián, flexiones y bici), sin nombres ni textos. Falta: confirmar que tengan 40+, precio y valor total en la tienda de hombres, cargar Zona media como upsell 1, confirmar garantía de 7 días y el WhatsApp de soporte (hoy wa.link/hewha8), y grabar el VSL (la portada tiene el espacio reservado: .vsl-ph en tienda_hombres.html). La sección de la app muestra un teléfono con img/m40_app_demo.mp4 (8 s: app en uso armada cuadro por cuadro + placa "Sumate a RENOVA" con transición deslizada; alumno de ejemplo).
- MÉTODO 40 Alimentación Inteligente (ebook-hombres/, 62 hojas, listo el 8/11/2026): que Eugenia revise las 5 hojas nuevas para hombres (entrenamiento, combinaciones, testosterona, asado y alcohol, ajustes en 14 días) Va dentro del pack (casa + gimnasio + métricas + alimentación): cargar los 4 PDF en el producto de la tienda de hombres.
- MÉTODO 40 upsell Zona media fuerte: que Nacho lo revise y definir precio en la tienda de hombres.
- MÉTODO 40 (hombres 40+): 3 PDF (casa y gimnasio de 28 hojas con elongación de 5 minutos, y guía de métricas gratis; `python3 hombres.py metricas && node export.js hombres_metricas`), piernas solo bipodales, brazos en cada rutina del gimnasio, plan ondulado con RIR y descarga en semanas 4 y 8. App web de MÉTODO 40 (rutinas de casa y gimnasio para entrenar desde el celular con carga de kilos, progreso, medidas y reporte PDF para compartir; código de acceso CODIGO_APP = RENOVA40 en hombres.py, que figura en los ebooks) — cada video tiene un play grande en el centro; las sesiones se cuentan solas al tocar "Terminar sesión" (con fecha) y se ven en la tabla "Mis entrenamientos" de Progreso y en Medidas; el test de fuerza es solo peso y repeticiones (el RIR es control de carga de los entrenamientos, no evaluación; así también en la guía de métricas, capítulos 04 y 05) publicada en https://metodo40-progreso.metodo40.workers.dev desde fuentes/tablero/ (`python3 build.py` → dist/index.html); FALTA publicarlo (ver fuentes/tablero/PUBLICAR.md) y completar LINK_TABLERO en hombres.py, Además: que Nacho revise rutinas y textos; confirmar si se puede nombrar a Racing (hoy dice "preparador físico de fútbol profesional"); confirmar el nombre de la marca; armar la tienda/landing en la otra cuenta de Impultienda y definir precio; después: upsell de nutrición para hombres.
- Upsell Glúteos Fuertes (2 ebooks, casa + gimnasio, se entregan juntos; listo el 8/11/2026): que Nacho revise ejercicios, plan y los 10 consejos de cada uno; verificar que funcionen los WhatsApp del 50% off (wa.link/hewha8 y wa.link/1asjt1) y que el descuento esté activo; que Eugenia revise la hoja de alimentación (capítulo 08); portada elegida: `gluteos-fuertes/creativos/portada_1.jpg` (libro 3D); ver en Impultienda si admite un segundo upsell (`upsell_2`) o si reemplaza al de menopausia, cargar los 2 PDF y el precio, y sumarlo a la landing. Ilustraciones que faltan si se quieren más ejercicios: patada en cuadrupedia y en polea, hip thrust en sillón (hoy usa la del gimnasio), abducción con banda.
- Auditoría Fase 1 de casa y gimnasio en `investigacion/auditoria-ebooks-fase1.md`: Nacho decide los puntos críticos (saltos/impacto, tracción en casa, errores frecuentes, qué hacer si pierdo días, "te acompañan") antes de pasar a la Fase 3.

- Bonus pausa activa: cargar `pausa-activa/Bonus_Pausa_activa_RENOVA.pdf` en el producto de Impultienda (junto a casa y gimnasio). En la landing ya es el bonus 4.
- Ebook Nutrición en la menopausia (upsell 1, $10.000): aprobado por Eugenia y ya en la landing. Falta cargarlo como upsell 1 en Impultienda (con precio) en lugar de "Recetas para entrenar mejor".
- Landing: falta saber medios de pago y si hay cuotas sin interés.
- Dominio metodorenova.fit (Namecheap, vence 1/11/2027): conectarlo a la tienda de Impultienda (DNS) y activar la renovación automática.

- Ebook mamás: que Nacho lo revise (idealmente también una kinesióloga de piso pélvico) y defina cómo se vende (producto aparte, upsell o dentro del combo de la landing). Después: sumarlo a la landing y armar sus creativos en `creativos/datos.py`.

- Alimentación Inteligente (plan de nutrición, 58 hojas, 38 recetas, fuentes de nutrientes y heladera con foto en img/nutri/, técnicas de cocción, seguimiento semanal; validado por Eugenia): listo para vender; cargar el PDF en el producto de Impultienda. Fotos de las recetas nuevas: img/food/n01–n16.jpg (Canva). Después: upsell Nutrición Femenina 40+ y recetario complementario (brief de ChatGPT).
- Ebook gimnasio: que Nacho revise las rutinas y diga si cambia algún ejercicio.
- Landing de la tienda: pegarla en Impultienda (el JS va aparte en `fuentes/landing/landing.js`, porque Impultienda se rompe con un `<script>` propio), revisar que reemplace precios y que el upsell sume al carrito, y cargar los PDF (casa, gimnasio y pausa) en el producto.
- Creativos (no tocados en la última ronda: siguen con 40+, dibujos de Canva y 3 bonus): que Nacho revise los textos de `fuentes/design-system/creativos/datos.py` y diga si agrega precio.
- Actualizar el perfil de la skill carrusel-studio (dice "rojo vino + azul oscuro") a la paleta turquesa del ebook.
- Oferta (Hormozi): análisis y prioridades en `investigacion/oferta-hormozi.md`. Falta que Nacho apruebe las acciones de la sección 9 (garantía, título de resultado, nombres de bonus, sacar "6 a 10 kg", victoria del día 1, hoja de adaptaciones).
- Guía práctica de alimentación (con la nutricionista): armarla desde la edición completa; reemplaza al upsell 1. Casa y gimnasio llevan 8 recetas proteicas y la hoja "Armá tu plato"; mamás lleva 10 (`RECETAS_BONUS` en `build.py`); las 23 quedan para la guía.
- VSL: análisis del competidor (Menofit) y guion propio en `investigacion/vsl-competidor/analisis-y-guion-vsl-renova.md`. Falta: que Nacho apruebe el guion y lo grabe; decidir qué ajustes de la sección 4 se implementan (frase de mecanismo en la landing, FAQ "nunca es tarde", hoja "por qué este plan" y hoja de recuperación en los ebooks).
- 5 videos sin equivalente en Harbiz (plancha oso, plancha lateral dinámica, balanceo de pierna, sentadilla sumo sin peso, plancha con rodillas): grabarlos si se quieren todos propios.
