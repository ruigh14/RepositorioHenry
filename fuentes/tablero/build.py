"""Tablero de progreso de MÉTODO 40 (página web que acompaña la Guía de métricas).

Arma dist/index.html desde tablero.html metiendo los tokens del design system (fuente única de colores).
Los datos de cada comprador se guardan solo en su navegador (localStorage), con copia descargable.

Uso: cd fuentes/tablero && python3 build.py   → dist/index.html (eso es lo que se publica)
Publicarlo: ver PUBLICAR.md. Después, poner el link en LINK_TABLERO de fuentes/ebook/hombres.py y regenerar la guía.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
tokens = open(os.path.join(HERE, "..", "design-system", "tokens.css"), encoding="utf-8").read()
m40 = ":root{" + "".join(re.findall(r"(--m40-[\w-]+:[^;]+;)", tokens)) + "}"
html = open(os.path.join(HERE, "tablero.html"), encoding="utf-8").read().replace("/*TOKENS*/", m40)
os.makedirs(os.path.join(HERE, "dist"), exist_ok=True)
with open(os.path.join(HERE, "dist", "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("dist/index.html ·", len(html) // 1024, "KB")
