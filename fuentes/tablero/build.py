"""Tablero de progreso de MÉTODO 40 (página web que acompaña la Guía de métricas).

Arma dist/index.html desde tablero.html metiendo los tokens RENOVA del design system (fuente única de colores),
el logo de RENOVA y el ícono de la landing (en base64), las rutinas y el plan (de hombres.py) y la huella del código
de acceso. Copia las fotos de los ejercicios a dist/img/ (se publica toda la carpeta dist/).
Los datos de cada comprador se guardan solo en su navegador (localStorage), con copia descargable.

La parte Zona media (upsell) va cifrada con CODIGO_ABD de hombres.py: se destraba con ese código, que está solo en
el ebook de Zona media fuerte.

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
                   "foco": g["FOCO"], "desc": g["DESC"], "calor": [ej(k) for k in g["CALOR"]], "elong": [ej(k) for k in g["ELONG"]]}
        imgs |= {g["E"][k][0] for k in g["E"]}
        DATOS["plan"] = [{"s": s, "sr": sr, "rir": rir} for s, sr, rir, _ in g["PLAN"]]
        DATOS["hash"] = hashlib.sha256(g["CODIGO_APP"].strip().upper().encode()).hexdigest()
    sys.argv = argv
    os.makedirs(os.path.join(HERE, "dist", "img"), exist_ok=True)
    for i in imgs:
        shutil.copy(os.path.join(IMG, i + ".jpg"), os.path.join(HERE, "dist", "img", i + ".jpg"))
    out["plan"] = DATOS["plan"]
    return out


def zona_media():
    """Rutinas del upsell Zona media (ABD_RUT de hombres.py), CIFRADAS con el código CODIGO_ABD: aunque alguien
    mire el código de la página, sin el código del ebook no las puede leer.
    Cifrado sin dependencias (igual en Python y en el navegador con Web Crypto):
    clave = PBKDF2-SHA256(código, sal, 150.000) · flujo = HMAC-SHA256(clave, nonce + n.º de bloque) XOR texto ·
    sello = HMAC-SHA256(clave, "tag" + nonce + cifrado) para saber si el código es correcto."""
    argv = sys.argv
    sys.argv = ["hombres.py", "abdomen"]
    g = runpy.run_path(os.path.join(HERE, "..", "ebook", "hombres.py"), run_name="tablero")
    sys.argv = argv
    ej = lambda k: dict(zip(("img", "n", "mus", "how", "evita", "princ", "mat", "url"), g["E"][k]), dosis=g["ABD_DOSIS"][k], mas=g["ABD_MAS"][k])
    datos = {"plan": g["ABD_PLAN"],
             "rutinas": {str(n): {"foco": foco, "claves": g["ABD_CLAVES"][n], "ejs": [ej(k) for k in ks]} for n, (foco, ks) in g["ABD_RUT"].items()}}
    texto = json.dumps(datos, ensure_ascii=False).encode()
    sal, nonce = os.urandom(16), os.urandom(12)
    clave = hashlib.pbkdf2_hmac("sha256", g["CODIGO_ABD"].strip().upper().encode(), sal, 150000, 32)
    flujo = b"".join(hmac.new(clave, nonce + i.to_bytes(4, "big"), hashlib.sha256).digest() for i in range(len(texto) // 32 + 1))
    cifrado = bytes(a ^ b for a, b in zip(texto, flujo))
    sello = hmac.new(clave, b"tag" + nonce + cifrado, hashlib.sha256).digest()
    b64 = lambda b: base64.b64encode(b).decode()
    return {"sal": b64(sal), "nonce": b64(nonce), "cifrado": b64(cifrado), "sello": b64(sello)}


import hmac

html = (open(os.path.join(HERE, "tablero.html"), encoding="utf-8").read().replace("/*TOKENS*/", raiz)
        .replace("/*EJERCICIOS*/", json.dumps(ejercicios(), ensure_ascii=False))
        .replace("/*ZONA*/", json.dumps(zona_media()))
        .replace("/*HASH*/", DATOS["hash"])
        .replace("/*LOGO*/", data_uri(os.path.join(HERE, "logo_renova.png")))                              # logo RENOVA (480 px)
        .replace("/*FAVICON*/", data_uri(os.path.join(HERE, "..", "landing", "img", "favicon_180.png"))))   # ícono de la landing
os.makedirs(os.path.join(HERE, "dist"), exist_ok=True)
with open(os.path.join(HERE, "dist", "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("dist/index.html ·", len(html) // 1024, "KB")
