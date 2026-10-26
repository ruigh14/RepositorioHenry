# Proyecto RENOVA

Repositorio de RENOVA, el programa de entrenamiento, alimentación y descanso de Nacho Portillo.
Todo el trabajo se guarda acá, en la rama `main`. Lo que no se commitea y pushea se pierde al cerrar la sesión.

## Estructura

- `ebook/`: ebook "Programa RENOVA · Guía práctica" (64 páginas A4).
  - `build.py`: todos los textos, recetas, menús, ejercicios y links (`LINKS`, `VIDEOS`). Genera `ebook.html`.
  - `style.css`: diseño. `paginate.js`: paginación automática A4. `export.js`: exporta el PDF con Playwright.
  - `img/`: fotos, ilustraciones, recetas y testimonios. `fonts/`: tipografía Inter.
  - `Ebook_Programa_RENOVA.pdf`: versión final vigente. `Ebook_Programa_RENOVA.txt`: su texto extraído.
  - `version-anterior_7_1.pdf`: exportación anterior (solo referencia, no editar).
- `index.html`: landing de venta del ebook + talleres.
- `upsell.html`: página de upsell post-compra ("desbloqueá todos los talleres").
- `css/styles.css`: estilos compartidos de la landing y el upsell.

## Regenerar el PDF del ebook

```
cd ebook && python3 build.py && node export.js
```

Debe imprimir `PAGINAS 64 OVERFLOW []` (o la cantidad de páginas que corresponda) sin páginas con overflow.

## Forma de trabajo

- Editar textos y contenido del ebook en `build.py`, no en `ebook.html` (se regenera).
- Después de cada cambio: regenerar el PDF, commitear y pushear a `main`.
- Idioma: español rioplatense (voseo).
