"""Tablero de progreso de MÉTODO 40 (página web que acompaña la Guía de métricas).

Arma dist/index.html desde tablero.html metiendo los tokens RENOVA del design system (fuente única de colores),
el logo de RENOVA y el ícono de la landing (en base64), las rutinas y el plan (de hombres.py) y la huella del código
de acceso. Copia las fotos de los ejercicios a dist/img/ (se publica toda la carpeta dist/).
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


import json
import runpy
import sys


import hashlib
import shutil

IMG = os.path.join(HERE, "..", "ebook", "img", "m40")
DATOS = {}


def ejercicios():
    """Rutinas completas de casa y gimnasio, calentamiento, plan ondulado y código de acceso, sacados de
    fuentes/ebook/hombres.py: la app no se desfasa nunca del ebook. Copia a dist/img/ las fotos que usa."""
    out, argv, imgs = {}, sys.argv, set()
    for ed in ("casa", "gym"):
        sys.argv = ["hombres.py", ed]
        g = runpy.run_path(os.path.join(HERE, "..", "ebook", "hombres.py"), run_name="tablero")
        ej = lambda k: dict(zip(("img", "n", "mus", "how", "evita", "princ", "mat", "url"), g["E"][k]))
        out[ed] = {"rutinas": {r: [dict(ej(k), t=t) for k, t in g["RUT"][r]] for r in "ABC"},
                   "foco": g["FOCO"], "desc": g["DESC"], "calor": [ej(k) for k in g["CALOR"]]}
        imgs |= {g["E"][k][0] for k in g["E"]}
        DATOS["plan"] = [{"s": s, "sr": sr, "rir": rir} for s, sr, rir, _ in g["PLAN"]]
        DATOS["hash"] = hashlib.sha256(g["CODIGO_APP"].strip().upper().encode()).hexdigest()
    sys.argv = argv
    os.makedirs(os.path.join(HERE, "dist", "img"), exist_ok=True)
    for i in imgs:
        shutil.copy(os.path.join(IMG, i + ".jpg"), os.path.join(HERE, "dist", "img", i + ".jpg"))
    out["plan"] = DATOS["plan"]
    return out


html = (open(os.path.join(HERE, "tablero.html"), encoding="utf-8").read().replace("/*TOKENS*/", raiz)
        .replace("/*EJERCICIOS*/", json.dumps(ejercicios(), ensure_ascii=False))
        .replace("/*HASH*/", DATOS["hash"])
        .replace("/*LOGO*/", data_uri(os.path.join(HERE, "logo_renova.png")))                              # logo RENOVA (480 px)
        .replace("/*FAVICON*/", data_uri(os.path.join(HERE, "..", "landing", "img", "favicon_180.png"))))   # ícono de la landing
os.makedirs(os.path.join(HERE, "dist"), exist_ok=True)
with open(os.path.join(HERE, "dist", "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("dist/index.html ·", len(html) // 1024, "KB")
