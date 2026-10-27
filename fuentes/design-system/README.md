# Design system RENOVA

Una sola marca para todo el proyecto de venta: **ebooks, landings y creativos** (imágenes, carruseles y videos para Instagram y Facebook).
Los colores son **los del ebook**. Landings, creativos y videos usan exactamente esa paleta.

Muestra visual de todo el sistema: [`muestra.pdf`](muestra.pdf).

## Qué hay acá

```
fuentes/design-system/
  tokens.css         colores, tipografías, escalas, espacios, radios, sombras y zonas seguras (fuente única)
  fuentes.css        tipografías locales (Inter e Inter Tight)
  fonts/             archivos de las tipografías
  design_system.py   css() para cargar tokens y fuentes, íconos, componentes del ebook y reglas de venta
  creativos/         plantillas de imágenes, carrusel y videos para Instagram y Facebook
  muestra.py / .js   genera muestra.pdf
```

Quién lo usa:
- **Ebooks:** `fuentes/ebook/build.py` carga `css()` y los componentes. En `style.css`, los alias cortos (`--tq`, `--ink`, …) apuntan a los tokens.
- **Landings:** `fuentes/landing/build.py` suma los tokens al CSS de cada landing. Sus alias (`--br`, `--grad`, …) apuntan a los tokens.
- **Creativos:** `creativos/creativos.css` usa solo tokens.

Si cambiás un token, cambia en todo. Después regenerá lo que corresponda (ver CLAUDE.md).

## Paleta (la del ebook)

| Token | Hex | Uso |
|---|---|---|
| `--rnv-turquesa` | `#14B1C7` | Rellenos, líneas, números grandes, botones |
| `--rnv-turquesa-titulo` | `#0E9DB2` | Palabras destacadas en títulos, botón del ebook |
| `--rnv-turquesa-oscuro` | `#0A7F90` | Texto chico en turquesa: pills, etiquetas, links |
| `--rnv-turquesa-profundo` | `#075E6B` | Texto sobre fondo turquesa claro |
| `--rnv-turquesa-fondo` | `#E8F6F8` | Fondo de recuadros y tarjetas |
| `--rnv-turquesa-borde` | `#CDEEF3` | Bordes suaves |
| `--rnv-azul` | `#0033A0` | Solo logo y portada del ebook |
| `--rnv-rojo` | `#E63333` | Solo logo y portada del ebook |
| `--rnv-tinta` / `--rnv-oscuro` | `#141414` | Títulos; barras, pie y recuadros oscuros |
| `--rnv-texto` | `#2A2F33` | Cuerpo |
| `--rnv-gris` | `#555C62` | Bajadas, notas, texto secundario |
| `--rnv-linea` | `#E3ECEE` | Separadores |
| `--rnv-fondo` | `#F4FAFB` | Fondo alternativo de secciones |
| `--rnv-degrade` | `#14B1C7 → #0E9DB2` | Botones y fondos de web y redes (solo turquesas del ebook) |

No hay otros colores: ni verde para los tildes, ni dorado para sellos, ni grises sueltos. Si hace falta uno nuevo, primero se agrega como token.

## Tipografía

- **Inter**: todo el texto del ebook y el cuerpo de la web y las redes.
- **Inter Tight**: titulares de la web y las redes, en mayúscula, peso 900 y con letras apretadas (`letter-spacing` negativo).
- Títulos en peso 800–900, cuerpo en 400. Las palabras clave del título van en turquesa (`<em>` o `<span class="t">`).

| Escala | Valores |
|---|---|
| Ebook (A4) | portada 37 pt · h1 26 pt · h2 18 pt · h3 16 pt · **cuerpo 16 pt (mínimo 15 pt)** · chico 13 pt |
| Web | h1 hasta 80 px · h2 hasta 42 px · cuerpo 17 px |
| Redes (lienzo de 1080 px) | gancho 104 px (88 px en feed) · título 72 px · subtítulo 48 px · **cuerpo 40 px mínimo** · etiqueta 28 px |

En el celular, una pieza de 1080 px se ve a ~36% de su tamaño: por eso el cuerpo de las redes no baja de 40 px.

## Componentes

**Ebook** (`design_system.py`): `eyebrow()` (pill), `chap_head()` (apertura de capítulo), `checks()` (lista con tildes), `box()` (recuadro: `''`, `'soft'` o `'note'`), `block_head()` (bloque de rutina), `params()` (fila de datos) y los íconos `ICON_*`. Las tarjetas de ejercicio (`ex_card`) quedan en `fuentes/ebook/build.py` porque dependen de los datos de cada edición.

**Venta** (landing y creativos): botón con relieve y degradé, bloque de precio, antes y después con etiquetas ANTES/DESPUÉS, testimonio con nombre y resultado, bonus en chips, tapa del ebook en 3D, compromiso de Nacho y garantía.

## Reglas de marca

- Español rioplatense con voseo: tenés, podés, empezá.
- Frases cortas, una idea por pieza o por slide.
- Se lee en el celular: letra grande siempre.
- El equipo incluye **médico deportólogo**: mencionarlo cuando se nombra al equipo.
- Fotos reales de RENOVA (Nacho, el equipo, los testimonios) antes que imágenes de stock.
- Ilustraciones de ejercicios hechas en Canva, con este prompt base: *"Flat vector illustration, simple cartoon style, white background, full body side view. A woman with brown hair in a ponytail, teal sports top and black leggings, [ejercicio]. Clean lines, no text, no background objects other than [equipo]."*
- Evitar: "holístico", "ecosistema", "pérdida de peso" como objetivo central, culpar a la mujer por falta de voluntad, promesas absolutas, miedo a envejecer.

## Reglas de venta

- **Precios en la landing:** siempre con los tokens de Impultienda (`{{price}}`, `{{original_price}}`, `{{savings}}`); nunca escritos a mano.
- **Precios en los creativos:** solo si se completan `precio` y `precio_antes` en `creativos/datos.py`; si no, se muestra "Acceso inmediato · 100% digital".
- **Resultados** (6 a 10 kg en 90 días, antes y después, testimonios): siempre con el descargo `DESCARGO` (*"Los resultados dependen de cada persona…"*). Solo casos reales que haya dado Nacho.
- Nada de promesas médicas.
- **Garantía:** todavía no está definida. `GARANTIA = None` en `design_system.py`, así no aparece en ninguna pieza. Cuando exista, se completa ahí.

## Creativos para Instagram y Facebook

```
cd fuentes/design-system/creativos && python3 generar.py && node exportar.js          # todo
node exportar.js imagen      # solo imágenes y carruseles (≈30 s)
node exportar.js video       # solo videos (≈2 min)
```

Salida, en la carpeta de cada producto (`entrena-desde-casa/creativos/`, `entrena-en-el-gimnasio/creativos/`):

| Carpeta | Piezas | Formato |
|---|---|---|
| `imagenes/` | 1-gancho, 2-antes-despues, 3-que-incluye, 4-oferta | feed 1080×1350 y vertical 1080×1920, PNG |
| `carrusel/` | slide-1 a slide-7: gancho, problema, por qué fuerza, solución, 3 fases, prueba social, CTA | 1080×1350, PNG |
| `videos/` | video-beneficios (21 s) y video-testimonio (22 s) | 1080×1920, MP4 H.264 sin audio |

- **Zonas seguras** en 1080×1920: nada importante en los 250 px de arriba ni en los 340 px de abajo, porque ahí Instagram pone su interfaz. Las plantillas ya las respetan.
- **Música:** los videos salen sin audio, para no usar música con derechos. Se agrega en Instagram o en el editor.
- **Hacer piezas nuevas:** editá `creativos/datos.py` (textos, gancho, beneficios, testimonios, imágenes) y volvé a generar. No hace falta tocar `plantillas.py` ni el CSS.
- **Plantilla nueva:** agregá una función en `plantillas.py` que use las clases de `creativos.css` y sumala a `IMAGENES` o `VIDEOS`.
- **Imágenes:** `"landing:archivo"` sale de `fuentes/landing/img/`, `"ebook:archivo"` de `fuentes/ebook/img/`. No se copian a otra carpeta.

## Cómo hacer algo nuevo

- **Ebook nuevo:** agregá una edición en `fuentes/ebook/build.py` (como `gimnasio`, con `G(casa, gym)` para los textos que cambian) y su salida en `export.js`.
- **Landing nueva:** copiá `fuentes/landing/casa.html`, cambiá textos e imágenes y sumala en `fuentes/landing/build.py`.
- **Creativos de un producto nuevo:** agregá un bloque en `creativos/datos.py`.

## Decisiones tomadas al unificar

| Antes | Ahora |
|---|---|
| La landing tenía su propio turquesa (`#16AEC6`, `#0E93A8`, `#31C7DB`) | Turquesas del ebook (`#14B1C7`, `#0E9DB2`) |
| La landing usaba otros negros y grises (`#111`, `#3A3F44`, `#62696F`, `#111418`) | `#141414`, `#2A2F33`, `#555C62` del ebook |
| Tildes verdes y sello dorado en la landing | Turquesa del ebook |
| Las tipografías estaban dentro de `fuentes/ebook/` | `fuentes/design-system/fonts/`, compartidas |
| Los colores estaban repetidos en `style.css`, `casa.html` y `gimnasio.html` | Un solo `tokens.css`; los demás usan alias |

El perfil de carruseles de la skill *carrusel-studio* habla de "rojo vino + azul oscuro". **En este proyecto de venta manda la paleta turquesa del ebook.** Conviene actualizar ese perfil para que no aparezcan dos estilos distintos.
