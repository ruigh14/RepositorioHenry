# Tablero de MÉTODO 40: dónde está publicado y cómo actualizarlo

**Link:** https://metodo40-progreso.metodo40.workers.dev
(identidad RENOVA: logo y paleta --rnv-* de los ebooks; publicado el 8/11/2026 en la cuenta de Cloudflare de Nacho, como Worker con archivos estáticos, plan gratis;
subdominio de la cuenta: `metodo40.workers.dev`). El mismo link está en `LINK_TABLERO` de `fuentes/ebook/hombres.py`.

Es **un solo archivo** (`dist/index.html`) y todos los compradores usan el mismo link. Los datos de cada uno quedan en su
celular o computadora: no hay servidor ni base de datos, así que la cantidad de compradores no cambia nada.

## Actualizarlo (después de cambiar `tablero.html`)

```
cd fuentes/tablero
python3 build.py                 # arma dist/index.html con los tokens del design system
npm install                      # la primera vez: instala wrangler y cf (quedan en node_modules, que no se sube a git)
~/.local/bin/cf deploy           # publica en el mismo link
```

Requisitos: el CLI `cf` de Cloudflare (`npm install -g cf --prefix ~/.local`) con la sesión iniciada (`~/.local/bin/cf auth login`).

## Configuración

- `cloudflare.config.ts`: nombre del Worker (`metodo40-progreso`).
- `wrangler.config.ts`: carpeta que se publica (`./dist`).

## Más adelante

- Dominio propio: en el panel de Cloudflare, **Workers & Pages → metodo40-progreso → Settings → Domains & Routes**
  (por ejemplo `progreso.metodorenova.fit`, si el dominio pasa a Cloudflare). Si cambia el link, actualizar `LINK_TABLERO`
  y regenerar la guía de métricas.
- El link es abierto: quien lo tenga lo puede usar. Es una herramienta que acompaña el producto, no el producto.
