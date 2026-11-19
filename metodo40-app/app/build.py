"""App MÉTODO 40 (versión con planificación anual). Arma dist/index.html desde app.html con:
- la planificación de cada objetivo (../planificacion/*.json, generados por generar.py),
- los ejercicios con foto, técnica y video (fuentes/ebook/hombres.py: misma fuente que los ebooks),
- la paleta MÉTODO 40 (tokens --m40-* del design system) y la huella del código de acceso (CODIGO_APP).
Uso: cd metodo40-app/app && python3 build.py → dist/index.html + dist/img/ (se publica la carpeta dist/)."""
import base64, hashlib, json, os, re, runpy, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
tokens = (ROOT / "fuentes/design-system/tokens.css").read_text(encoding="utf-8")
raiz = ":root{" + "".join(re.findall(r"(--m40-[\w-]+:[^;]+;)", tokens)) + "}"

argv = sys.argv; sys.argv = ["hombres.py", "casa"]
g = runpy.run_path(str(ROOT / "fuentes/ebook/hombres.py"), run_name="app")
sys.argv = argv
CAMPOS = ("img", "n", "mus", "how", "evita", "princ", "mat", "url")

planes = {}
for f in sorted((HERE.parent / "planificacion").glob("*.json")):
    planes[f.stem] = json.loads(f.read_text(encoding="utf-8"))
usados = set()
for p in planes.values():
    for m in p["meses"]:
        for lugar in m["rutinas"].values():
            for r in lugar.values():
                usados |= {e["id"] for e in r["entrada_en_calor"] + r["elongacion"]} | {e["id"] for b in r["centrales"] for e in b}
    for zonas in p["dolores"].values():
        for c in zonas.values():
            usados |= set(c) | set(c.values())
falta = [i for i in usados if i not in g["E"]]
assert not falta, f"ejercicios sin ficha en hombres.py: {falta}"
EJ = {i: dict(zip(CAMPOS, g["E"][i])) for i in sorted(usados)}

dist = HERE / "dist"; (dist / "img").mkdir(parents=True, exist_ok=True)
for i in usados:
    src = ROOT / "fuentes/ebook/img/m40" / (g["E"][i][0] + ".jpg")
    if src.exists():
        shutil.copy(src, dist / "img" / src.name)

logo = "data:image/png;base64," + base64.b64encode((ROOT / "fuentes/tablero/logo_renova.png").read_bytes()).decode()
DATOS = {"planes": planes, "ej": EJ, "hash": hashlib.sha256(g["CODIGO_APP"].strip().upper().encode()).hexdigest(),
         "wa": "https://wa.me/5491133209619"}
html = ((HERE / "app.html").read_text(encoding="utf-8").replace("/*TOKENS*/", raiz)
        .replace("/*DATOS*/", json.dumps(DATOS, ensure_ascii=False)).replace("/*LOGO*/", logo))
(dist / "index.html").write_text(html, encoding="utf-8")
(dist / "_headers").write_text("/*\n  Referrer-Policy: strict-origin-when-cross-origin\n", encoding="utf-8")
print("dist/index.html ·", len(html) // 1024, "KB ·", len(usados), "ejercicios")
