# Proyecto RENOVA

Repositorio de RENOVA, el programa de entrenamiento, alimentación y descanso de Nacho Portillo.
Todo el trabajo se guarda acá, en la rama `main`. Lo que no se commitea y pushea se pierde al cerrar la sesión.

## Estructura

Hay **una sola landing**, la de la tienda (renova.impultienda.ar), donde se venden los **dos ebooks** (casa + gimnasio en una misma compra). Cada ebook tiene su carpeta. El código que los genera está en `fuentes/` y es uno solo para todos: no duplicarlo por producto.

```
tienda/
  landing-impultienda.html   → la landing de renova.impultienda.ar (se pega en Diseño de tienda → HTML propio)
entrena-desde-casa/          Ebook 1
  Ebook_Entrena_desde_casa_RENOVA.pdf
entrena-en-el-gimnasio/      Ebook 2: misma lógica, rutinas de gimnasio nivel inicial
  Ebook_Entrena_en_el_gimnasio_RENOVA.pdf
entrena-siendo-mama/         Ebook 3: mamás que vuelven a entrenar (respiración, piso pélvico, sin impacto) + pausa activa
  Ebook_Entrena_siendo_mama_RENOVA.pdf
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
- `ebook.html`, `entrena.html`, `gimnasio.html`: HTML intermedio que genera `build.py` (no editar).
- `style.css`: diseño. `paginate.js`: paginación automática A4. `export.js`: exporta el PDF con Playwright a la carpeta del producto.
- `img/`: fotos, ilustraciones, recetas y testimonios. Las tipografías están en `fuentes/design-system/fonts/`.
- `archivo/version-anterior_7_1.pdf`: exportación vieja, solo referencia.
- Talleres: están en Skool (https://www.skool.com/renova-entrenamiento-y-salud-1617/about); el bonus de talleres de los ebooks tiene un botón grande que lleva ahí. No hay ebook de talleres ni página de upsell.

### `fuentes/landing/`
- `tienda.html`: fuente de la única landing (vende los 2 ebooks juntos, con un solo `/checkout`; el producto de Impultienda tiene que entregar los 2 PDF). `build.py` encierra el CSS en `#rnv` (para que no choque con la tienda) y cambia `img/...` por links de GitHub a `fuentes/landing/img/`, fijados al último commit de esa carpeta: **commitear y pushear las imágenes nuevas antes de regenerar**. Los videos (`<source src="img/….mp4">`) salen de jsDelivr con GitHub de respaldo.
- Portada: secuencia en `#stage` (video de alumnas 6 s → fotos de logros 1,5 s c/u → collage fijo) y foto de Nacho fija. Mensajes de clientas: carrusel `#msgs`; para sumar uno, otra `<figure class="msg">` con la captura en `img/`.
- Impultienda: compra con `<a href="/checkout">`, precios con `{{price}}`, `{{original_price}}`, `{{savings}}` y upsell 1 con `{{upsell_1_*}}` + `data-upsell-toggle="1"`.

## Regenerar

```
cd fuentes/ebook && python3 build.py entrena && node export.js entrena     # Entrená desde casa
cd fuentes/ebook && python3 build.py gimnasio && node export.js gimnasio   # Entrená en el gimnasio
cd fuentes/ebook && python3 build.py mamas && node export.js mamas         # Entrená siendo mamá
cd fuentes/ebook && python3 build.py && node export.js                     # Programa RENOVA completo
cd fuentes/landing && python3 build.py                                     # la landing de la tienda
cd fuentes/design-system/creativos && python3 generar.py && node exportar.js   # creativos (imagen | video)
cd fuentes/design-system && python3 muestra.py && node muestra.js           # muestra.pdf del design system
```

El ebook debe imprimir `OVERFLOW []` (sin páginas con texto cortado). Para revisar el texto de un PDF: `pdftotext -layout <pdf> /tmp/x.txt`.

## Estrategia de producto

- **Landing y creativos:** no se vende consulta ni acompañamiento. El bonus 3 es el **acceso a la comunidad RENOVA en Skool** (cursos y talleres; interactuar con otras mujeres es opcional). En la landing, WhatsApp solo para problemas con la compra.
- **Adentro del ebook (después de comprar):** sí está la oferta de Nacho: **50% off en el plan personalizado** (rutinas de entrenamiento o programa integral RENOVA), contactándolo por WhatsApp (`LINKS["wa_plan"]`, capítulo "Después de las 8 semanas") y el botón "Quiero sumarme a RENOVA" (`LINKS["renova"]`). No hay consulta gratis.

- Ebook 1 (solo entrenamiento) es el producto de entrada; alimentación (menús, compras) y descanso quedan para ebooks de upsell.
- El equipo incluye **médico deportólogo** (medicina deportiva): mantenerlo en ambas ediciones.
- Investigación de mercado de referencia: Google Doc "RENOVA_investigacion_ebooks_entrenamiento_mujeres_40_plus".

## Forma de trabajo

- Editar textos y contenido del ebook en `fuentes/ebook/build.py`, no en los `.html` (se regeneran).
- Después de cada cambio: regenerar el PDF (o la landing), commitear y pushear a `main`.
- Idioma: español rioplatense (voseo).
- Se lee en el celular: letra grande (cuerpo 15 pt). Si algo no entra en la hoja, acortar texto o separar en hojas, no achicar la letra.

## Frase para retomar: "RENOVA, seguimos"

Cuando Nacho escriba **"RENOVA, seguimos"** (en esta conversación o en una nueva), antes de hacer nada:
1. Leer este archivo y `git log --oneline -15` para ver lo último que se hizo.
2. Responder con un resumen corto: en qué quedó cada proyecto y qué está pendiente (sección siguiente).
3. Preguntar con qué sigue.

## Pendientes

- Ebook mamás: que Nacho lo revise (idealmente también una kinesióloga de piso pélvico) y defina cómo se vende (producto aparte, upsell o dentro del combo de la landing). Después: sumarlo a la landing y armar sus creativos en `creativos/datos.py`.

- Ebook gimnasio: que Nacho revise las rutinas y diga si cambia algún ejercicio.
- Landing de la tienda: pegarla en Impultienda, revisar que reemplace precios y que el upsell sume al carrito, y cargar los 2 PDF en el producto (casa + gimnasio). Si Nacho prefiere vender el de gimnasio como upsell, cambiar en `tienda.html`.
- Garantía: Nacho tiene que definir si hay (y cuál). Cuando la defina, completar `GARANTIA` en `fuentes/design-system/design_system.py` y sumarla a la landing.
- Creativos: que Nacho revise los textos de `fuentes/design-system/creativos/datos.py` y diga si agrega precio.
- Actualizar el perfil de la skill carrusel-studio (dice "rojo vino + azul oscuro") a la paleta turquesa del ebook.
- Oferta (Hormozi): análisis y prioridades en `investigacion/oferta-hormozi.md`. Falta que Nacho apruebe las acciones de la sección 9 (garantía, título de resultado, nombres de bonus, sacar "6 a 10 kg", victoria del día 1, hoja de adaptaciones).
- Guía práctica de alimentación (con la nutricionista): armarla desde la edición completa; reemplaza al upsell 1. Los ebooks de entrenamiento llevan solo las 10 recetas más proteicas (`RECETAS_BONUS` en `build.py`); las 23 quedan para la guía.
- VSL: análisis del competidor (Menofit) y guion propio en `investigacion/vsl-competidor/analisis-y-guion-vsl-renova.md`. Falta: que Nacho apruebe el guion y lo grabe; decidir qué ajustes de la sección 4 se implementan (frase de mecanismo en la landing, FAQ "nunca es tarde", hoja "por qué este plan" y hoja de recuperación en los ebooks).
- 5 videos sin equivalente en Harbiz (plancha oso, plancha lateral dinámica, balanceo de pierna, sentadilla sumo sin peso, plancha con rodillas): grabarlos si se quieren todos propios.
