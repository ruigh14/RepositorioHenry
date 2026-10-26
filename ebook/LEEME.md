# Ebook Programa RENOVA

- `build.py`: textos, recetas, menús, ejercicios y links (diccionario `LINKS` y `VIDEOS`).
- `style.css`: diseño. `paginate.js`: paginación automática A4.
- `img/`: fotos e ilustraciones. `fonts/`: tipografía Inter.

Regenerar los PDF:

    python3 build.py entrena && node export.js entrena   # Ebook 1 · Entrená desde casa
    python3 build.py && node export.js                   # Programa RENOVA completo

(`export.js` usa Playwright con Chromium.)
