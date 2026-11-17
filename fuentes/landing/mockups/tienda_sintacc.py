"""Tapa alternativa de "Sin TACC Inteligente" para su tienda propia (comida + nutricionista, sin la foto del equipo)
y sus mockups en 3D. La tapa con el equipo (pack/tapa_sintacc.png) queda para el upsell de la tienda RENOVA.
Uso: cd fuentes/landing/mockups && python3 tienda_sintacc.py && node tienda_sintacc.js
  → pack/tapa_sintacc_comida.png y ../../../sin-tacc-inteligente/creativos/tienda_portada{,_vertical}.png"""
import io, contextlib
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    from libros3d import CSS, book

F = "../../design-system/fonts/"
FOOD = "../../ebook/img/food/"
TAPA = f"""<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:IT;src:url({F}inter-tight-latin-var.woff2);font-weight:100 900}}
@font-face{{font-family:I;src:url({F}inter-latin-700-normal.woff2);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1240px;height:1754px;overflow:hidden;background:#fff;font-family:IT,sans-serif;color:#141414;position:relative}}
.top{{text-align:center;padding-top:70px}}
.top img{{height:64px}}
.tag{{display:inline-block;margin-top:30px;background:#06343B;color:#fff;font:800 28px IT;letter-spacing:.14em;padding:12px 34px;border-radius:999px}}
h1{{font:900 150px/0.92 IT;letter-spacing:-.03em;color:#14B1C7;margin-top:26px;text-transform:uppercase}}
h2{{font:900 62px/1 IT;margin-top:22px;text-transform:uppercase;letter-spacing:-.01em}}
h2 span{{background:#14B1C7;color:#fff;padding:0 16px;border-radius:10px}}
.grid{{position:absolute;left:70px;right:70px;top:720px;display:grid;grid-template-columns:1fr 1fr;gap:22px}}
.grid div{{position:relative;height:340px;border-radius:26px;overflow:hidden;box-shadow:0 14px 30px rgba(6,52,59,.18)}}
.grid img{{width:100%;height:100%;object-fit:cover}}
.grid b{{position:absolute;left:16px;bottom:16px;background:rgba(255,255,255,.95);font:800 26px IT;padding:8px 18px;border-radius:999px;color:#06343B}}
.chip{{position:absolute;left:50%;top:1052px;transform:translateX(-50%);background:#06343B;color:#fff;font:900 34px IT;letter-spacing:.04em;padding:16px 40px;border-radius:999px;white-space:nowrap;box-shadow:0 10px 24px rgba(0,0,0,.25);text-transform:uppercase}}
.chip i{{font-style:normal;color:#6FD8E6}}
.aut{{position:absolute;left:70px;right:70px;bottom:70px;display:flex;align-items:center;gap:30px;background:#E8F6F8;border-radius:30px;padding:26px 34px}}
.aut img{{width:150px;height:150px;border-radius:50%;object-fit:cover;object-position:50% 20%;border:6px solid #14B1C7;flex:none}}
.aut p{{font:700 30px/1.3 I;color:#2A2F33}}
.aut p b{{display:block;font:900 40px/1.1 IT;color:#141414}}
.aut p span{{color:#0A7F90}}
</style>
<div class="top"><img src="../img/logo.png"><br><span class="tag">GUÍA PRÁCTICA · CELIAQUÍA</span>
<h1>Sin TACC<br>Inteligente</h1><h2>Comé rico y <span>seguro</span></h2></div>
<div class="grid">
 <div><img src="{FOOD}st_pizza.jpg"><b>Pizza de fainá</b></div>
 <div><img src="{FOOD}st_empanadas.jpg"><b>Empanadas</b></div>
 <div><img src="{FOOD}st_des1.jpg"><b>Desayunos express</b></div>
 <div><img src="{FOOD}st_budin.jpg"><b>Budín de banana</b></div>
</div>
<div class="chip">18 recetas <i>+</i> 5 desayunos express</div>
<div class="aut"><img src="../img/equipo_eugenia.jpg"><p><b>Lic. María Eugenia Aldrey</b>Nutricionista · M.N. 11773 <span>· Equipo RENOVA</span></p></div>
"""
Path("tapa_sintacc_comida.html").write_text(TAPA, encoding="utf-8")

SELLO = """.sello{position:absolute;width:270px;height:270px;border-radius:50%;z-index:9;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
 box-shadow:0 0 0 8px #14B1C7,0 0 0 18px rgba(20,177,199,.25),0 0 70px rgba(20,177,199,.8),0 30px 60px rgba(0,0,0,.5);transform:rotate(-8deg)}
.sello b{display:block;font:900 96px/0.95 InterTightW,sans-serif;color:#141414;letter-spacing:-.04em}
.sello i{display:block;font:900 44px/1 InterTightW,sans-serif;font-style:normal;color:#0A7F90;margin-top:8px}"""
s = '<div class="sello" style="right:{r}px;top:{t}px"><b>100%</b><i>SIN TACC</i></div>'
for name, w, h, bk, sello in [("tienda_sintacc_v", 1080, 1440, ("tapa_sintacc_comida.png", "SIN TACC INTELIGENTE", 190, 300, 680, -16), (110, 80)),
                              ("tienda_sintacc", 1080, 1080, ("tapa_sintacc_comida.png", "SIN TACC INTELIGENTE", 110, 85, 550, -20), (60, 110))]:
    Path(name + ".html").write_text(f'<!doctype html><meta charset="utf-8"><style>{CSS}{SELLO}body{{--w:{w}px;--h:{h}px}}</style>'
                                    f'<div class="grid"></div><div class="st">{book(*bk)}{s.format(r=sello[0], t=sello[1])}</div>', encoding="utf-8")
print("ok")
