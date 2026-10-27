# Proyecto RENOVA

Repositorio de RENOVA, el programa de entrenamiento, alimentación y descanso de Nacho Portillo.
Todo el trabajo se guarda acá, en la rama `main`. Lo que no se commitea y pushea se pierde al cerrar la sesión.

## Estructura

- `ebook/`: los ebooks RENOVA, generados desde un mismo `build.py` en dos ediciones:
  - **Ebook 1 · "Entrená desde casa"** (producto de entrada): plan de fuerza de 8 semanas + bonus
    (recetario, 2 talleres: Organizar la heladera y Gestión de la ansiedad, consulta con Nacho). → `entrena.html`, `Ebook_Entrena_desde_casa_RENOVA.pdf`.
  - **Programa RENOVA completo** (entrenamiento + alimentación + descanso): base para los ebooks de upsell.
    → `ebook.html`, `Ebook_Programa_RENOVA.pdf`.
  - **Ebook Talleres RENOVA** (upsell, 3 hojas: portada, talleres con quién los da y qué se dicta, CTA rutinas personalizadas / plan integral al WhatsApp de Nacho). Sale de `talleres.py` (no de `build.py`); datos de cada taller en `TALLERES`. → `talleres.html`, `Ebook_Talleres_RENOVA.pdf`.
  - `build.py`: todos los textos, recetas, menús, ejercicios (cada rutina en 3 hojas: entrada en calor, bloque 1, bloque 2; elongación al final), plan de 8 semanas (`PLAN8`), pausa activa (`PAUSA`, `TIPS_DIA`), extra de zona media (`CORE`) y links (`LINKS`; `VIDEOS` = links de Harbiz de cada ejercicio).
  - `style.css`: diseño. `paginate.js`: paginación automática A4. `export.js`: exporta el PDF con Playwright.
  - `img/`: fotos, ilustraciones, recetas y testimonios. `fonts/`: tipografía Inter.
  - `Ebook_Programa_RENOVA.pdf`: versión final vigente. `Ebook_Programa_RENOVA.txt`: su texto extraído.
  - `version-anterior_7_1.pdf`: exportación anterior (solo referencia, no editar).
- `index.html`: landing de venta del Ebook 1 para pegar en Impultienda (HTML propio). **No editar a mano**: se genera con `cd landing && python3 build.py` desde `landing/landing.html` (encierra el CSS en `#rnv` e imágenes desde GitHub en `landing/img/`, fijadas al último commit de esa carpeta: commitear y pushear las imágenes nuevas antes de regenerar). Compra con `<a href="/checkout">`, precios con `{{price}}`, `{{original_price}}`, `{{savings}}` y upsell 1 con `{{upsell_1_*}}` + `data-upsell-toggle="1"` (tokens de Impultienda).
- `upsell.html`: página de upsell post-compra ("desbloqueá todos los talleres").
- `css/styles.css`: estilos compartidos de la landing y el upsell.

## Regenerar el PDF del ebook

```
cd ebook && python3 build.py entrena && node export.js entrena   # Ebook 1 · Entrená desde casa
cd ebook && python3 build.py && node export.js                   # Programa RENOVA completo
cd ebook && python3 talleres.py && node export.js talleres       # Ebook Talleres RENOVA (3 hojas)
```

Debe imprimir `OVERFLOW []` (sin páginas con texto cortado).

## Estrategia de producto

- Ebook 1 (solo entrenamiento) es el producto de entrada; alimentación (menús, compras) y descanso quedan para ebooks de upsell.
- El equipo incluye **médico deportólogo** (medicina deportiva): mantenerlo en ambas ediciones.
- Investigación de mercado de referencia: Google Doc "RENOVA_investigacion_ebooks_entrenamiento_mujeres_40_plus".

## Forma de trabajo

- Editar textos y contenido del ebook en `build.py`, no en `ebook.html` (se regenera).
- Después de cada cambio: regenerar el PDF, commitear y pushear a `main`.
- Idioma: español rioplatense (voseo).
- Se lee en el celular: letra grande (cuerpo 15 pt). Si algo no entra en la hoja, acortar texto o separar en hojas, no achicar la letra.
