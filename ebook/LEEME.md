# Ebook Programa RENOVA

- `build.py`: textos, recetas, menús, ejercicios y links (diccionario `LINKS` y `VIDEOS`).
- `style.css`: diseño. `paginate.js`: paginación automática A4.
- `img/`: fotos e ilustraciones. `fonts/`: tipografía Inter.

Regenerar el PDF:

    python3 build.py && node export.js

(`export.js` usa Playwright con Chromium.)
