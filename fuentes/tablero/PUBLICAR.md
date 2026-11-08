# Publicar el tablero de MÉTODO 40

Se publica **una sola vez**. Todos los compradores usan el mismo link; los datos de cada uno quedan en su propio celular o computadora (no hay servidor ni base de datos, así que 300 o 3.000 compradores no cambian nada).

Lo que se publica es **un solo archivo**: `fuentes/tablero/dist/index.html` (se genera con `python3 build.py`).

## Opción recomendada: Cloudflare Pages (gratis, uso comercial permitido)

1. Entrá a https://pages.cloudflare.com y creá una cuenta (o usá la tuya).
2. **Workers & Pages → Create → Pages → Upload assets** (subir archivos, sin GitHub).
3. Nombre del proyecto: por ejemplo `metodo40-progreso`.
4. Arrastrá la carpeta `fuentes/tablero/dist` (la que tiene `index.html`) y tocá **Deploy**.
5. Te da un link como `https://metodo40-progreso.pages.dev`. Ese es el link del tablero.
6. (Opcional) **Custom domains** → por ejemplo `progreso.metodorenova.fit`, si el dominio está en Cloudflare o agregás el registro DNS que te indica.

Para actualizarlo más adelante: mismo proyecto → **Create deployment** → subí de nuevo la carpeta `dist`.

## Alternativa: GitHub Pages

1. Creá un repositorio **público** nuevo, por ejemplo `metodo40-tablero` (no uses este repositorio: tiene todo RENOVA).
2. Subí el `index.html` de `dist/`.
3. **Settings → Pages → Branch: main / root → Save**.
4. El link queda `https://<tu-usuario>.github.io/metodo40-tablero/`.

## Después de publicar

1. Poné el link en `LINK_TABLERO` de `fuentes/ebook/hombres.py`.
2. Regenerá la guía: `cd fuentes/ebook && python3 hombres.py metricas && node export.js hombres_metricas`.
3. Abrí el link desde tu celular y probá: configurar, cargar una semana, subir una foto, "Guardar copia" y "Recuperar copia".

Nota: el link es abierto (quien lo tenga lo puede usar). Es una herramienta de acompañamiento del producto, no el producto.
