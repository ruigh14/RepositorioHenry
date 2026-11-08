# Proyecto RENOVA

Repositorio de RENOVA, el programa de entrenamiento, alimentación y descanso de Nacho Portillo.
Todo el trabajo se guarda acá, en la rama `main`. Lo que no se commitea y pushea se pierde al cerrar la sesión.

## Estructura

Hay **una sola landing**, la de la tienda (renova.impultienda.ar; dominio propio comprado: **metodorenova.fit**, en Namecheap, 1 año desde el 1/11/2026, a conectar con Impultienda), donde se venden los **dos ebooks** (casa + gimnasio en una misma compra). Cada ebook tiene su carpeta. El código que los genera está en `fuentes/` y es uno solo para todos: no duplicarlo por producto.

```
tienda/
  landing-impultienda.html   → la landing de renova.impultienda.ar (se pega en Diseño de tienda → HTML propio)
entrena-desde-casa/          Ebook 1
  Ebook_Entrena_desde_casa_RENOVA.pdf
entrena-en-el-gimnasio/      Ebook 2: misma lógica, rutinas de gimnasio nivel inicial
  Ebook_Entrena_en_el_gimnasio_RENOVA.pdf
entrena-siendo-mama/         Ebook 3: mamás que vuelven a entrenar (respiración, piso pélvico, sin impacto) + pausa activa
  Ebook_Entrena_siendo_mama_RENOVA.pdf
alimentacion-inteligente/    Plan de nutrición de 8 semanas (lo vende la landing): educación breve + organización + programa de 8 semanas con 32 recetas. Lo genera fuentes/ebook/nutricion.py (nutricionista: Lic. María Eugenia Ballini, M.N. 11773; suma 6 recetas, reemplazos e imágenes de su recetario y su catálogo de productos en img/eve/ e img/prod/)
  Ebook_Alimentacion_Inteligente_RENOVA.pdf
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
  Ebook_Metodo40_Zona_Media.pdf  Upsell "Zona media fuerte" (20 hojas): mitos y verdades, punto fijo y móvil (toes to bar = psoas), giro ruso y cizallamiento, respiración en flexiones y planchas, 4 rutinas de planchas, flexiones y mountain climbers (sin twists ni toes to bar), 2 veces por semana al final de una sesión, plan ondulado. `python3 hombres.py abdomen && node export.js hombres_abdomen`
  Ebook_Metodo40_Alimentacion_Inteligente.pdf  Plan de nutrición de 8 semanas para hombres 40+: la misma guía que Alimentación Inteligente (mismas 38 recetas), en masculino y con paleta MÉTODO 40, más 4 hojas propias (comer alrededor del entrenamiento, combinaciones para el día de entrenamiento, asado/alcohol/fin de semana, si no progresás: ajustá en 14 días). Lo genera `python3 nutricion.py hombres && node export.js hombres_nutricion` (textos que cambian: X(mujeres, hombres))
comunidad/                   Bonus (PDF aparte): Acceso a la comunidad RENOVA (portada + cómo entrar a Skool y ver los talleres en Cursos). Lo genera fuentes/ebook/comunidad.py && node comunidad.js
  Bonus_Acceso_comunidad_RENOVA.pdf
pausa-activa/                Bonus (PDF aparte) de casa y gimnasio: explicación + 4 rutinas de pausa activa de 10 min + plan personalizado
  Bonus_Pausa_activa_RENOVA.pdf
programa-renova-completo/    Entrenamiento + alimentación + descanso (base de los upsell)
  Ebook_Programa_RENOVA.pdf
investigacion/               material de referencia (VSL del competidor, etc.)
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
- Estructura (correcciones de Nacho, modelo Menofit): barra de oferta fija (toda la barra lleva al carrito) → portada oscura (petróleo + turquesa) con franja del equipo, título, bajada, "Programa interdisciplinario", el VSL (`.vsl`: Wistia `9xn7yk66az`, arranca en silencio y en loop; al tocarlo `landing.js` lo reinicia con sonido) → ¿Te pasa esto? → No es tu culpa → testimonios ("…no es opcional, ¡es preventivo!") → pilares (fuerza, nutrición, hábitos) → "Esto es lo que incluye": programa de entrenamiento y plan de nutrición (`img/mock_nutricion.jpg`) → 5 bonos (pausa activa, express, abdominales, talleres, comunidad) → quién soy + carrusel deslizable del equipo (Nacho, Lic. María Eugenia Ballini nutricionista, Lic. Agostina Galiani psicóloga, Dr. Rodrigo Portillo Ruffa médico traumatólogo y deportólogo) → valor $100.000 / hoy $35.000 + upsell → garantía → preguntas → cierre. Todos los botones van a `/checkout`. Precios con los tokens de Impultienda (`{{price}}` = $35.000, `{{original_price}}` = $100.000, `{{savings}}`): se cargan en el producto. No hay valores escritos fijos: todos los montos salen del carrito de Impultienda.
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
cd fuentes/ebook && python3 gluteos.py casa && node export.js gluteos_casa  # Upsell: Glúteos Fuertes en casa
cd fuentes/ebook && python3 gluteos.py gym && node export.js gluteos_gym    # Upsell: Glúteos Fuertes en el gimnasio
cd fuentes/ebook && python3 hombres.py casa && node export.js hombres_casa  # MÉTODO 40 en casa
cd fuentes/ebook && python3 hombres.py gym && node export.js hombres_gym    # MÉTODO 40 en el gimnasio
cd fuentes/ebook && python3 nutricion.py hombres && node export.js hombres_nutricion  # MÉTODO 40: Alimentación Inteligente
cd fuentes/landing && python3 build.py                                     # la landing de la tienda
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

- MÉTODO 40 Alimentación Inteligente (ebook-hombres/, 61 hojas, listo el 8/11/2026): que Eugenia revise las 4 hojas nuevas para hombres (entrenamiento, combinaciones, asado y alcohol, ajustes en 14 días) y definir si va en el pack o como upsell, y su precio.
- MÉTODO 40 upsell Zona media fuerte: que Nacho lo revise y definir precio en la tienda de hombres.
- MÉTODO 40 (hombres 40+): 3 PDF (casa y gimnasio de 28 hojas con elongación de 5 minutos, y guía de métricas gratis; `python3 hombres.py metricas && node export.js hombres_metricas`), piernas solo bipodales, brazos en cada rutina del gimnasio, plan ondulado con RIR y descarga en semanas 4 y 8. App web de MÉTODO 40 (rutinas de casa y gimnasio para entrenar desde el celular con carga de kilos, progreso, medidas y reporte PDF para compartir; código de acceso CODIGO_APP = RENOVA40 en hombres.py, que figura en los ebooks) publicada en https://metodo40-progreso.metodo40.workers.dev desde fuentes/tablero/ (`python3 build.py` → dist/index.html); FALTA publicarlo (ver fuentes/tablero/PUBLICAR.md) y completar LINK_TABLERO en hombres.py, Además: que Nacho revise rutinas y textos; confirmar si se puede nombrar a Racing (hoy dice "preparador físico de fútbol profesional"); confirmar el nombre de la marca; armar la tienda/landing en la otra cuenta de Impultienda y definir precio; después: upsell de nutrición para hombres.
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
