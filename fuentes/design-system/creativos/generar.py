"""Genera los HTML de los creativos de cada producto y la lista para exportar.

    cd fuentes/design-system/creativos && python3 generar.py && node exportar.js

Salida final (la escribe exportar.js), en la carpeta de cada producto:
    <producto>/creativos/imagenes/   1-gancho, 2-antes-despues, 3-que-incluye, 4-oferta  (feed 1080×1350 y vertical 1080×1920)
    <producto>/creativos/carrusel/   slide-1 … slide-7 (1080×1350)
    <producto>/creativos/videos/     video-beneficios, video-testimonio (1080×1920, MP4 sin audio)
"""
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, "..", "..", ".."))
sys.path.insert(0, os.path.join(AQUI, ".."))
from design_system import css  # noqa: E402
from datos import PRODUCTOS  # noqa: E402
import plantillas as P  # noqa: E402

CARPETAS_IMG = {"landing": os.path.join(RAIZ, "fuentes", "landing", "img"),
                "ebook": os.path.join(RAIZ, "fuentes", "ebook", "img")}
HTML = os.path.join(AQUI, "html")   # HTML intermedio (no se versiona)
CSS_CREATIVOS = open(os.path.join(AQUI, "creativos.css"), encoding="utf-8").read()


def pagina(destino_html, cuerpo, fmt, video=False):
    carpeta = os.path.dirname(destino_html)
    estilo = css(carpeta) + "\n" + CSS_CREATIVOS
    clase = f"f-{fmt}" + (" video" if video else "")
    script = ""
    if video:
        # Arranca las animaciones cuando cargaron fuentes e imágenes; exportar.js mide ese momento.
        script = ('<script>Promise.all([document.fonts.ready,...[...document.images].map(i=>i.complete?1:new Promise(r=>{i.onload=i.onerror=r}))])'
                  '.then(()=>setTimeout(()=>{document.documentElement.classList.add("go");window.__go=performance.now()},300))</script>')
    return (f'<!doctype html><html lang="es" class="{clase}"><head><meta charset="utf-8"><style>{estilo}</style></head>'
            f'<body>{cuerpo}{script}</body></html>')


def generar():
    lista = []
    for prod, d in PRODUCTOS.items():
        base = os.path.join(HTML, prod)
        os.makedirs(base, exist_ok=True)

        def img(ref):
            donde, archivo = ref.split(":", 1)
            return os.path.relpath(os.path.join(CARPETAS_IMG[donde], archivo), base).replace(os.sep, "/")

        def guardar(nombre, cuerpo, fmt, tipo, salida, dur=None):
            ruta = os.path.join(base, nombre + ".html")
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(pagina(ruta, cuerpo, fmt, video=(tipo == "video")))
            lista.append(dict(html=ruta, ancho=1080, alto=int(fmt), tipo=tipo, duracion=dur,
                              salida=os.path.join(RAIZ, prod, "creativos", salida)))

        for nombre, fn in P.IMAGENES:
            for fmt, sufijo in (("1350", "feed-1080x1350"), ("1920", "vertical-1080x1920")):
                guardar(f"{nombre}-{fmt}", fn(d, img, fmt), fmt, "imagen", f"imagenes/{nombre}-{sufijo}.png")
        for k, slide in enumerate(P.carrusel(d, img), 1):
            guardar(f"carrusel-{k}", slide, "1350", "imagen", f"carrusel/slide-{k}.png")
        for nombre, fn in P.VIDEOS:
            cuerpo, dur = fn(d, img)
            guardar(nombre, cuerpo, "1920", "video", f"videos/{nombre}-1080x1920.mp4", dur)

    with open(os.path.join(HTML, "lista.json"), "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=1)
    print(len(lista), "piezas listas para exportar")


if __name__ == "__main__":
    generar()
