"""Catálogo visual del design system: paleta, tipografía, componentes y creativos.

    cd fuentes/design-system && python3 muestra.py && node muestra.js   → muestra.pdf

La paleta y las escalas se leen de tokens.css: si cambia un token, la muestra se actualiza sola.
"""
import os
import re

from design_system import (DS, css, leer, eyebrow, chap_head, checks, box, block_head, params,
                           ICON_ARROW, ICON_PLAY, DESCARGO)

RAIZ = os.path.normpath(os.path.join(DS, "..", ".."))
EBOOK_CSS = open(os.path.join(DS, "..", "ebook", "style.css"), encoding="utf-8").read()
TOKENS = leer("tokens.css")


def tokens(prefijo):
    """[(nombre, valor, comentario)] de los tokens que empiezan con prefijo."""
    out = []
    for m in re.finditer(r"--(rnv-[\w-]+):([^;]+);[ \t]*(?:/\*[ \t]*(.*?)[ \t]*\*/)?", TOKENS):
        if m.group(1).startswith(prefijo):
            out.append((m.group(1), m.group(2).strip(), m.group(3) or ""))
    return out


def rel(ruta):
    return os.path.relpath(os.path.join(RAIZ, ruta), DS).replace(os.sep, "/")


def hoja(cuerpo, titulo):
    return (f'<section class="page"><div class="hdr"><span>DESIGN SYSTEM · <b>RENOVA</b></span><span>{titulo}</span></div>'
            f'<div class="body">{cuerpo}</div></section>')


COLORES = [t for t in tokens("rnv-") if t[1].startswith("#")]
swatches = "".join(
    f'<div class="sw"><span style="background:{v}"></span><b>{n.replace("rnv-", "")}</b><code>{v}</code><p>{c}</p></div>'
    for n, v, c in COLORES)

ESCALAS = [("Ebook (A4)", tokens("rnv-pdf")), ("Web (landing)", tokens("rnv-web")), ("Redes (lienzo de 1080 px)", tokens("rnv-red"))]
escalas = '<div class="ds-esc">' + "".join(
    f'<div><h3>{t}</h3><table class="grid-t ds-t"><tbody>' +
    "".join(f'<tr><th>{n.replace("rnv-", "")}</th><td>{v}</td></tr>' for n, v, c in ts) + "</tbody></table></div>"
    for t, ts in ESCALAS) + "</div>"

feed = "".join(f'<img src="{rel(f"entrena-desde-casa/creativos/imagenes/{n}-feed-1080x1350.png")}">'
               for n in ["1-gancho", "2-antes-despues", "3-que-incluye", "4-oferta"])
vert = "".join(f'<img src="{rel(f"entrena-en-el-gimnasio/creativos/imagenes/{n}-vertical-1080x1920.png")}">'
               for n in ["1-gancho", "2-antes-despues", "3-que-incluye", "4-oferta"])
carr = "".join(f'<img src="{rel(f"entrena-desde-casa/creativos/carrusel/slide-{k}.png")}">' for k in range(1, 8))

paginas = [
    hoja(f'''{chap_head("DS", 'Design system <span class="t">RENOVA</span>', "Una sola marca para los ebooks, las landings y los creativos de venta. Estos son los colores del ebook: todo usa exactamente esta paleta.")}
<div class="sws">{swatches}</div>
{box("<b>Degradé</b> (botones y fondos de web y redes): solo turquesas del ebook, de <code>#14B1C7</code> a <code>#0E9DB2</code>. Azul y rojo son los del logo: solo en el logo y la portada del ebook.", "soft")}''',
         "Paleta"),
    hoja(f'''{eyebrow("TIPOGRAFÍA")}
<h1 class="h1">Inter para todo, <span class="t">Inter Tight</span> para titulares de web y redes</h1>
<p class="lead">Las dos están en <code>fuentes/design-system/fonts/</code>. Títulos en peso 800–900, cuerpo en 400.</p>
<div class="ds-tipos"><p style="font-family:var(--rnv-fuente);font-weight:900;font-size:30pt">Inter 900 · Aa</p>
<p style="font-family:var(--rnv-fuente-display);font-weight:900;font-size:30pt;text-transform:uppercase">Inter Tight 900 · Aa</p>
<p style="font-family:var(--rnv-fuente);font-size:16pt">Inter 400 · cuerpo del ebook: 16 pt (mínimo 15 pt, se lee en el celular)</p></div>
{escalas}''', "Tipografía"),
    hoja(f'''{eyebrow("COMPONENTES DEL EBOOK")}
<h1 class="h1">Piezas que se <span class="t">repiten</span></h1>
<p class="small">Funciones de <code>design_system.py</code>: eyebrow(), chap_head(), checks(), box(), block_head(), params().</p>
{eyebrow("ESTO ES UN EYEBROW")}
{checks(["Lista con tildes: <b>checks()</b>", "Una idea por línea, frases cortas"])}
{box("<b>Recuadro</b> box(…, 'soft'): para aclaraciones y datos importantes.", "soft")}
{box("<b>Nota</b> box(…, 'note'): advertencias de salud y seguridad.", "note")}
{block_head("RUTINA 1 · BLOQUE 1", "2 o 3 vueltas · 30–60 s entre ejercicios")}
{params([("Vueltas", "2 o 3"), ("Pausa", "30–60 s"), ("Esfuerzo", "7 de 10"), ("Duración", "20–40 min")])}
<div class="quote dark">Frase destacada: <span class="t2">fondo negro del ebook.</span></div>
<div class="cta-center"><span class="btn btn-big">BOTÓN DEL EBOOK {ICON_ARROW}</span> <span class="vbtn-sm">{ICON_PLAY} VER VIDEO</span></div>
<p class="small"><b>Descargo obligatorio con resultados:</b> {DESCARGO}</p>''', "Componentes"),
    hoja(f'''{eyebrow("CREATIVOS · INSTAGRAM Y FACEBOOK")}
<h1 class="h1">Imágenes, carrusel y <span class="t">videos</span></h1>
<p class="small">Se generan desde <code>creativos/datos.py</code>: cambiás los textos y salen piezas nuevas con el mismo diseño.</p>
<h3>Feed 1080×1350 · gancho, antes y después, qué incluye, oferta</h3><div class="ds-strip">{feed}</div>
<h3>Historias y reels 1080×1920 · zonas seguras: 250 px arriba y 340 px abajo</h3><div class="ds-strip v">{vert}</div>
<h3>Carrusel 1080×1350 · 7 slides</h3><div class="ds-strip c">{carr}</div>
<p class="small">Videos 1080×1920 de 21–22 s, MP4 sin audio: <b>video-beneficios</b> (gancho, 3 beneficios, CTA) y <b>video-testimonio</b> (resultado, antes, después, más casos, CTA). Música: agregala en Instagram o en el editor.</p>''',
         "Creativos"),
]

EXTRA = """
.page{width:210mm;height:297mm;padding:21mm 17mm 17mm;position:relative;overflow:hidden;break-after:page}
.body{height:259mm;overflow:hidden}
.sws{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm 4mm;margin:5mm 0}
.sw span{display:block;height:12mm;border-radius:3mm;border:.3mm solid var(--rnv-linea)}
.sw b{display:block;font-size:11pt;margin-top:1.5mm;color:var(--rnv-tinta)}
.sw code{font-size:10pt;color:var(--rnv-turquesa-oscuro)}
.sw p{font-size:8.5pt;line-height:1.3;color:var(--rnv-gris);margin:.5mm 0 0}
.ds-t th{text-align:left}.ds-t td,.ds-t th{font-size:9pt;padding:1.2mm 2mm}
.ds-esc{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4mm}.ds-esc td{word-break:break-all}
.ds-tipos p{margin:2mm 0;color:var(--rnv-tinta)}
.ds-strip{display:flex;gap:3mm;margin:2mm 0 5mm}.ds-strip img{width:23.5%;border-radius:2mm;box-shadow:0 1mm 3mm rgba(20,20,20,.15)}
.ds-strip.v img{width:18%}.ds-strip.c img{width:13.3%}
code{font-family:"DejaVu Sans Mono",monospace;font-size:.9em}
"""

html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Design system RENOVA</title><style>'
        + css(DS) + EBOOK_CSS + EXTRA + '</style></head><body>' + "".join(paginas) + '</body></html>')
with open(os.path.join(DS, "muestra.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("muestra.html ·", len(paginas), "hojas")
