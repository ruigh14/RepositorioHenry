"""Tablero de progreso de MÉTODO 40 (página web que acompaña la Guía de métricas).

Arma dist/index.html desde tablero.html metiendo los tokens RENOVA del design system (fuente única de colores),
el logo de RENOVA y el ícono de la landing (en base64, para que siga siendo un solo archivo).
Los datos de cada comprador se guardan solo en su navegador (localStorage), con copia descargable.

Uso: cd fuentes/tablero && python3 build.py   → dist/index.html (eso es lo que se publica)
Publicarlo: ver PUBLICAR.md. Después, poner el link en LINK_TABLERO de fuentes/ebook/hombres.py y regenerar la guía.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
tokens = open(os.path.join(HERE, "..", "design-system", "tokens.css"), encoding="utf-8").read()
import base64
raiz = ":root{" + "".join(re.findall(r"(--rnv-[\w-]+:[^;]+;)", tokens)) + "}"   # paleta RENOVA (la de los ebooks)


def data_uri(ruta):
    with open(ruta, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


html = (open(os.path.join(HERE, "tablero.html"), encoding="utf-8").read().replace("/*TOKENS*/", raiz)
        .replace("/*LOGO*/", data_uri(os.path.join(HERE, "logo_renova.png")))                              # logo RENOVA (480 px)
        .replace("/*FAVICON*/", data_uri(os.path.join(HERE, "..", "landing", "img", "favicon_180.png"))))   # ícono de la landing
os.makedirs(os.path.join(HERE, "dist"), exist_ok=True)
with open(os.path.join(HERE, "dist", "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("dist/index.html ·", len(html) // 1024, "KB")
