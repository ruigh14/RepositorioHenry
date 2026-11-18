"""Imagen de Sin TACC Inteligente para el checkout de Impultienda (va arriba del botón de compra), 1080x1310.
Fondo claro como el checkout, tapas reales y los 5 bonus con los nombres de la landing.
Uso: cd fuentes/landing/mockups && python3 sintacc_checkout.py && node sintacc_checkout.js → ../../../sin-tacc-inteligente/creativos/checkout.png"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "design-system"))
from design_system import css

I, P = "../img/", "pack/"
LIBROS = [(P + "tapa_sintacc_comida.png", "Sin TACC<br>Inteligente", ""), (P + "tapa_reposteria.png", "Repostería Sin TACC:<br>20 recetas dulces", "DE REGALO")]
BONUS = [(I + "taller_super.jpg", "Talleres con profesionales y comunidad RENOVA", ""),
         (P + "tapa_pausa.jpg", "Pausa activa", "object-position:50% 12%"),
         (P + "st_imprimible.png", "Imprimibles", "object-position:50% 0")]

CSS = css(str(Path(__file__).parent)) + """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1310px;overflow:hidden;font-family:InterW,sans-serif;color:var(--rnv-tinta);
 background:linear-gradient(180deg,#fff 0%,var(--rnv-turquesa-fondo) 100%)}
.top{text-align:center;padding-top:56px}
.top img{height:52px}
h1{font:900 76px/1 InterTightW,sans-serif;letter-spacing:-.02em;text-transform:uppercase;margin-top:22px}
h1 b{color:var(--rnv-turquesa-titulo)}
.sub{font:600 34px InterW,sans-serif;color:var(--rnv-gris);margin-top:10px}
.libros{display:flex;justify-content:center;align-items:flex-start;gap:60px;margin-top:40px;padding:0 90px}
.lib{text-align:center;flex:1;min-width:0}
.tapa{border-radius:4px 12px 12px 4px;overflow:hidden;background:#fff;aspect-ratio:210/297;position:relative;
 box-shadow:18px 26px 44px rgba(6,52,59,.28),0 0 0 1px rgba(0,0,0,.05)}
.tapa img{width:100%;height:100%;object-fit:cover;display:block}
.tapa::after{content:"";position:absolute;inset:0 auto 0 0;width:5%;background:linear-gradient(90deg,rgba(0,0,0,.25),rgba(255,255,255,.15) 60%,transparent)}
.lib b{display:block;font:800 36px/1.1 InterTightW,sans-serif;margin-top:14px}
.lib.op span{background:var(--rnv-oro);color:var(--rnv-tinta);letter-spacing:.08em;font-size:21px}
.lib.op .tapa{outline:4px dashed var(--rnv-oro);outline-offset:6px}
.lib span{display:inline-block;margin-top:18px;font:800 21px InterTightW,sans-serif;letter-spacing:.12em;color:#fff;
 background:var(--rnv-turquesa);padding:5px 14px;border-radius:999px}
.bh{display:flex;align-items:center;gap:22px;margin:44px 50px 0}
.bh i{flex:1;height:3px;background:var(--rnv-turquesa-borde)}
.bh b{white-space:nowrap;font:900 60px InterTightW,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:var(--rnv-turquesa-oscuro)}
.bon{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:0 60px}
.bo{display:flex;align-items:center;gap:18px;background:#fff;border:2px solid var(--rnv-turquesa-borde);border-radius:20px;padding:12px 18px 12px 12px;
 box-shadow:0 8px 20px rgba(6,52,59,.08)}
.bo img{width:92px;height:92px;border-radius:12px;object-fit:cover;flex:none}
.bo i{display:block;font:800 19px InterTightW,sans-serif;letter-spacing:.12em;color:var(--rnv-turquesa-oscuro);font-style:normal}
.bo b{display:block;font:800 30px/1.1 InterTightW,sans-serif}
.bo:first-child{grid-column:1/-1}
"""


def libro(i, f, t, op):
    c, tag = (" op", op) if op else ("", "EBOOK")
    return f'<div class="lib{c}"><div class="tapa"><img src="{f}"></div><span>{tag}</span><b>{t}</b></div>'


def bono(i, src, t, pos):
    return f'<div class="bo"><img src="{src}" style="{pos}"><div><i>BONUS {i+1}</i><b>{t}</b></div></div>'


html = f"""<!doctype html><meta charset="utf-8"><style>{CSS}</style>
<div class="top"><img src="{I}logo.png"><h1>Todo lo que <b>recibís</b></h1><p class="sub">Acceso inmediato en tu celular</p></div>
<div class="libros">{''.join(libro(i, f, t, o) for i, (f, t, o) in enumerate(LIBROS))}</div>
<div class="bh"><i></i><b>+ 3 bonus incluidos</b><i></i></div>
"""
Path(__file__).with_name("sintacc_checkout.html").write_text(html, encoding="utf-8")
print("ok")
