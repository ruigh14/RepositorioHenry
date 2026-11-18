"""Ebook "Repostería Sin TACC": 20 recetas dulces (upsell de RENOVA). Formato RENOVA, a partir del borrador de Nacho.
Uso: cd fuentes/ebook && python3 reposteria.py && node export.js reposteria
  → sin-tacc-inteligente/Ebook_Reposteria_Sin_TACC_RENOVA.pdf"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "design-system"))
from design_system import css as ds_css, esc, ICON_ARROW, ICON_HAND, eyebrow, chap_head, ul, checks, box
from reposteria_recetas import RECETAS

LINK_SKOOL = "https://www.skool.com/renova-entrenamiento-y-salud-1617/about"
PAGES, TOC = [], []


def page(body, chapter="", pid=None, cls="", toc=None, header=True):
    pid = pid or f"p{len(PAGES) + 1}"
    PAGES.append(dict(id=pid, chapter=chapter, body=body, cls=cls, header=header))
    if toc:
        TOC.append((toc, pid))


def ficha(r, n):
    rinde, prep, coc, temp = r["meta"]
    ing = "".join(f"<li>{esc(i)}</li>" for i in r["ing"])
    pas = "".join(f"<li>{esc(p)}</li>" for p in r["pasos"])
    return (f'<article class="nrec con-img"><div class="nr-img"><img src="img/food/rp{n:02d}.jpg" alt="{esc(r["t"])}"></div><div class="nr-tx">'
            f'<div class="nr-h"><span class="nr-n">{n:02d}</span><div><span class="nr-cat">REPOSTERÍA SIN TACC</span><h3>{esc(r["t"])}</h3>'
            f'<p class="nr-meta">Rinde {esc(rinde)} · Preparación {esc(prep)} · Cocción {esc(coc)} · {esc(temp)}</p></div></div>'
            f'<div class="nr-cols"><div><h5>Ingredientes</h5><ul>{ing}</ul></div><div><h5>Preparación</h5><ol>{pas}</ol></div></div>'
            f'<p class="nr-x"><b>Consejo:</b> {esc(r["consejo"])}</p></div></article>')


CAPS = [("01", "Tortas <span class=\"t\">y budines</span>", "Para la merienda, un cumpleaños o la mesa de todos los días.", "Tortas y budines"),
        ("02", "Galletitas <span class=\"t\">y alfajores</span>", "Para tener siempre algo rico y apto en la alacena.", "Galletitas y alfajores"),
        ("03", "Postres <span class=\"t\">clásicos</span>", "Los de siempre, en versión Sin TACC.", "Postres clásicos"),
        ("04", "Dulces <span class=\"t\">fáciles</span>", "Rápidos, con pocos ingredientes y sin complicarte.", "Dulces fáciles"),
        ("05", "Para <span class=\"t\">compartir</span>", "Para llevar a una reunión sin preocuparte.", "Para compartir")]

# ------------------------------------------------------------------ portada
page('''
<div class="cv3 nutri">
  <div class="c3-in">
    <img class="c3-logo" src="img/logo_renova.png" alt="RENOVA">
    <span class="c3-pill">RECETARIO · SIN TACC</span>
    <h1 class="c3-title">REPOSTERÍA<br>SIN TACC</h1>
    <p class="c3-claim">20 RECETAS <b><span>DULCES.</span></b></p>
    <p class="c3-sub">Tortas, budines, galletitas, alfajores y postres <b>para disfrutar</b>,<br><span><em>compartir</em> y <mark>preparar en casa</mark>.</span></p>
  </div>
  <div class="c3-team"><img src="img/equipo_tapa.png" alt="Equipo RENOVA"></div>
</div>
''', pid="portada", cls="p-cover", header=False)

# ------------------------------------------------------------------ bienvenida
page(f'''
{eyebrow("BIENVENIDA")}
<h1 class="h1">Comer Sin TACC <span class="t">no es renunciar a lo dulce</span></h1>
<p class="lead">Una torta de chocolate, unos alfajores de maicena, un budín casero o unas galletitas recién horneadas también pueden estar en tu mesa.</p>
<p>Juntamos <b>20 recetas dulces</b> con ingredientes fáciles de conseguir y pasos simples. No hace falta ser pastelero: cada receta trae cantidades, porciones, tiempos y el paso a paso.</p>
<h2>Cómo usar este recetario</h2>
{ul(["<b>Leé la receta completa antes de empezar,</b> pesá los ingredientes y prepará los utensilios.",
     "<b>Los tiempos de horno son orientativos:</b> cambian según el horno, el molde y la marca de premezcla.",
     "<b>Antes de cocinar, leé «Antes de empezar»:</b> ahí está cómo evitar la contaminación cruzada.",
     "<b>Disfrutalas con equilibrio:</b> son recetas para darte un gusto, no para todos los días."])}
{box("<b>Material educativo general.</b> No reemplaza la consulta médica ni nutricional. Una preparación es apta solo si todos sus ingredientes son aptos y se evita la contaminación cruzada.", "note")}
''', chapter="Bienvenida", pid="bienvenida")

page("__TOC__", chapter="Índice", pid="indice")

# ------------------------------------------------------------------ antes de empezar
page(f'''
{chap_head("", 'Antes de <span class="t">empezar</span>', "Una receta casera es segura solo si todos los ingredientes son aptos y no hay contaminación cruzada.")}
<h2>Compras</h2>
{checks(["Elegí productos envasados con el logo oficial <b>«Sin T.A.C.C.»</b> o <b>«sin GLUTEN»</b> y, ante la duda, buscalos en el listado de ANMAT.",
         "Que un ingrediente no tenga trigo no lo hace seguro: puede contaminarse al fraccionarse.",
         "Evitá productos sueltos o a granel y revisá la etiqueta en cada compra."])}
<h2>Cocina limpia</h2>
{checks(["Lavate las manos y limpiá mesadas, moldes y utensilios antes de empezar.",
         "Usá utensilios exclusivos para lo difícil de limpiar: coladores, palo de amasar y tostadora.",
         "Cociná primero lo Sin TACC y mantené todo tapado y separado.",
         "No compartas manteca, dulce de leche ni mermelada si el cuchillo tocó pan con gluten."])}
<h2>Horno y heladera</h2>
{checks(["No hornees preparaciones con y sin gluten en la misma bandeja.",
         "Guardá lo apto en recipientes cerrados, rotulados y separados.",
         "Lo que lleva crema, ricota, leche o huevo va siempre a la heladera."])}
{box("<b>Regla práctica:</b> ante la duda sobre un ingrediente, no lo uses para alguien celíaco.", "tip")}
''', chapter="Antes de empezar", pid="antes", toc="Antes de empezar: cocina segura")

page(f'''
{chap_head("", 'Medidas <span class="t">y trucos</span>', "Lo que hace la diferencia en la repostería sin gluten.")}
<h2>Medidas</h2>
<p>1 taza = 240 ml · 1 cucharada = 15 ml · 1 cucharadita = 5 ml. Cuando la receta dice gramos, usá balanza: es más precisa.</p>
<h2>Premezclas</h2>
<p>Cada marca absorbe distinto. Empezá con las cantidades de la receta y no agregues líquido ni harina de más.</p>
<h2>Textura</h2>
<p>No batas de más después de sumar la premezcla. Dejá enfriar antes de desmoldar o cortar: lo sin gluten es frágil en caliente y se afirma al enfriarse.</p>
<h2>Conservación</h2>
<p>Guardá todo frío y en recipientes cerrados. Si congelás, porcioná, envolvé y poné la fecha.</p>
{box("<b>Huevos en recetas sin cocción</b> (como la mousse): usá huevos pasteurizados y mantené la preparación en la heladera.", "note")}
''', chapter="Medidas y trucos", pid="medidas", toc="Medidas y trucos")

for k, (num, tit, sub, nombre) in enumerate(CAPS):
    rs = RECETAS[k * 4:(k + 1) * 4]
    page(f'''{chap_head(num, tit, sub)}
{"".join(ficha(r, k * 4 + i + 1) for i, r in enumerate(rs))}''', chapter=f"{num} · {nombre}", pid=f"c{num}", toc=f"{num} · {nombre}")

# ------------------------------------------------------------------ lista de compras
GRUPOS = [("Harinas, almidones y secos", ["Premezcla sin TACC", "Almidón de maíz", "Coco rallado", "Cacao amargo", "Polvo para hornear", "Nueces y almendras", "Canela y esencia de vainilla"]),
          ("Heladera", ["Huevos (pasteurizados para recetas sin cocción)", "Leche", "Yogur natural", "Manteca", "Crema de leche", "Ricota", "Dulce de leche"]),
          ("Chocolates, azúcar y frutas", ["Chocolate semiamargo", "Chips de chocolate", "Azúcar", "Azúcar impalpable", "Manzanas", "Limones", "Zanahorias"])]
page(f'''
{chap_head("", 'Lista <span class="t">de compras</span>', "Todo lo envasado, con logo oficial Sin TACC. Tildá lo que tenés y llevá el resto.")}
{"".join(f"<h2>{g}</h2>" + checks(items) for g, items in GRUPOS)}
''', chapter="Lista de compras", pid="compras", toc="Lista de compras")

# ------------------------------------------------------------------ cierre
page(f'''
<div class="bio metodo">
  {eyebrow("PARA DISFRUTAR Y COMPARTIR")}
  <h1 class="h1 big">Cocinar también es <span class="t">probar y disfrutar</span></h1>
  <p class="lead">No hace falta que todo salga perfecto la primera vez. Probá, ajustá a tu horno y quedate con tus favoritas para compartir en la mesa de siempre.</p>
  <div class="cp-pills"><span>✓ Talleres de nutrición</span><span>✓ Hábitos</span><span>✓ Comunidad RENOVA</span></div>
  <p class="center"><b>Seguí aprendiendo con nuestro equipo</b> en la comunidad RENOVA.</p>
  <div class="cta-center"><a class="btn btn-big" href="{esc(LINK_SKOOL)}">IR A LA COMUNIDAD {ICON_ARROW}</a></div>
  <div class="quote dark">Comer Sin TACC no es una limitación. <span class="t2">Es tu forma de cuidarte.</span></div>
</div>
''', chapter="Cierre", pid="cierre", toc="Para disfrutar y compartir")


def render():
    num = {p["id"]: i + 1 for i, p in enumerate(PAGES)}
    toc_html = '<div class="tocl tc">' + "".join(
        f'<a class="tocr" href="#{pid}"><span class="tt">{esc(t)}</span><span class="dots"></span><span class="pg">{num[pid]}</span></a>'
        for t, pid in TOC) + "</div>"
    out = []
    for p in PAGES:
        body = p["body"]
        if body == "__TOC__":
            body = (f'{eyebrow("CONTENIDO")}<div class="idxhead"><h1 class="h1">Índice</h1>'
                    f'<p class="idxtip">{ICON_HAND} Hacé clic donde quieras ir. Para volver al índice, abajo de cada página tenés el botón.</p></div>{toc_html}')
        hdr = ""
        if p["header"]:
            hdr = (f'<div class="hdr"><span>REPOSTERÍA SIN TACC · <b>RENOVA</b></span><span>{esc(p["chapter"])}</span></div>'
                   f'<div class="ftr"><a class="toidx" href="#indice">{ICON_HAND} Hacé clic y volvé al índice</a><span class="pgnum"></span></div>')
        out.append(f'<section class="page {p["cls"]}" id="{p["id"]}">{hdr}<div class="body">{body}</div></section>')
    css = ds_css(HERE) + "\n" + open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Repostería Sin TACC · RENOVA</title>'
            f'<style>{css}</style></head><body class="grande">' + "".join(out) + '<script src="paginate.js"></script></body></html>')


if __name__ == "__main__":
    with open(os.path.join(HERE, "reposteria.html"), "w", encoding="utf-8") as f:
        f.write(render())
    print("reposteria.html ·", len(PAGES), "páginas antes de paginar")
