"""Genera la landing de la tienda (renova.impultienda.ar), donde se venden los dos ebooks.

- Encierra todo en <div id="rnv"> y antepone #rnv a cada selector, para que el CSS
  de la tienda no pise la landing ni la landing pise la tienda.
- Mueve el <style> dentro del <body> (por si la tienda descarta el <head>).
- Cambia img/... por la URL pública de GitHub (fijada al último commit de img/), así las imágenes cargan desde cualquier lado.

Uso:  cd fuentes/landing && python3 build.py      tienda.html → tienda/landing-impultienda.html
Se pega en Impultienda: Diseño de tienda → HTML propio.
"""
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "design-system"))
from design_system import css as ds_css   # tokens compartidos con los ebooks y los creativos

HERE = Path(__file__).parent
# Commit fijo de la última versión de landing/img (evita la caché de GitHub con archivos nuevos).
# Antes de correr esto, commitear y pushear las imágenes nuevas.
SHA = subprocess.check_output(["git", "log", "-1", "--format=%H", "--", "img"], cwd=HERE, text=True).strip()
IMG = f"https://raw.githubusercontent.com/ruigh14/RepositorioHenry/{SHA}/fuentes/landing/img/"
FONTS = "https://fonts.googleapis.com/css2?family=Inter+Tight:wght@600;700;800;900&family=Inter:wght@400;500;600;700&display=swap"


def prefix(sel):
    out = []
    for x in sel.split(","):
        x = x.strip()
        if not x:
            continue
        if x == "html":
            out.append("html")
        elif x in ("body", ":root"):
            out.append("#rnv")
        elif x == "*":
            out.append("#rnv,#rnv *")
        elif x.startswith(".js "):
            out.append("#rnv.js " + x[4:])
        else:
            out.append("#rnv " + x)
    return ",".join(out)


def block_end(css, j):
    d = 0
    for k in range(j, len(css)):
        if css[k] == "{":
            d += 1
        elif css[k] == "}":
            d -= 1
            if d == 0:
                return k
    raise ValueError("llave sin cerrar")


def scope(css):
    out, i = "", 0
    while i < len(css):
        j = css.find("{", i)
        if j < 0:
            return out + css[i:]
        sel = css[i:j]
        s = sel.strip()
        if s.startswith("@keyframes") or s.startswith("@font-face"):
            k = block_end(css, j)
            out += css[i:k + 1]
            i = k + 1
            continue
        if s.startswith("@media"):
            k = block_end(css, j)
            out += sel + "{" + scope(css[j + 1:k]) + "}"
            i = k + 1
            continue
        k = css.find("}", j)
        lead = sel[: len(sel) - len(sel.lstrip())]
        out += lead + prefix(s) + css[j:k + 1]
        i = k + 1
    return out


SRC, OUT = "tienda.html", Path("tienda") / "landing-impultienda.html"
src = (HERE / SRC).read_text()
css = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
css = ds_css(str(HERE), fuentes=False) + css
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
head = re.sub(r"<style>.*?</style>\s*", "", src.split("<body>")[0], flags=re.S)
body = src.split("<body>", 1)[1].split("</body>")[0]
html = (head + "<body>\n<div id=\"rnv\">\n<style>@import url(\"" + FONTS + "\");\n"
        + scope(css).strip() + "\n</style>\n" + body.strip() + "\n</div>\n</body>\n</html>\n")
html = re.sub(r'(src|href)="img/', r'\1="' + IMG, html)
html = html.replace("url('img/", "url('" + IMG)
(HERE.parent.parent / OUT).write_text(html)
print(OUT, len(html) // 1024, "KB")
