"""Anuncios de Sin TACC Inteligente + Repostería Sin TACC (1080×1350). Fondos de Higgsfield (z_image, pack/st_fondo*.jpg)
y tapas reales en 3D, así no se duplican ebooks ni se deforman textos.
Uso: cd fuentes/landing/mockups && python3 anuncios_sintacc.py && node anuncios_sintacc.js → ../../../sin-tacc-inteligente/creativos/anuncio_*.png"""
import io, contextlib
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    from libros3d import CSS, book
X = """
body{background:#fff}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.bg::after{content:"";position:absolute;inset:0;background:rgba(255,255,255,.6)}
.msg{position:absolute;z-index:6;border-radius:28px;overflow:hidden;box-shadow:0 0 0 5px #14B1C7,0 25px 50px rgba(0,0,0,.3)}.msg img{display:block;width:100%}
.lbl{position:absolute;z-index:7;font:800 30px InterTightW;color:#06343B;background:#fff;border:3px solid #14B1C7;padding:10px 24px;border-radius:999px}
.stars{position:absolute;z-index:7;font:900 54px/1 InterTightW;color:#FFC400;letter-spacing:6px;text-shadow:0 3px 8px rgba(0,0,0,.2)}
.logo{position:absolute;left:50%;transform:translateX(-50%);height:58px;z-index:5}
.t{position:absolute;left:0;right:0;text-align:center;z-index:5;font-family:InterTightW,sans-serif}
.t h1{font:900 92px/0.95 InterTightW;letter-spacing:-.03em;color:#06343B;text-transform:uppercase}
.t h1 span{color:#14B1C7}
.t h2{display:inline-block;margin-top:16px;font:800 50px/1 InterTightW;color:#fff;background:#14B1C7;padding:12px 34px;border-radius:999px;box-shadow:0 10px 30px rgba(20,177,199,.35)}
.fr{box-shadow:0 0 0 3px #14B1C7,0 0 0 8px rgba(20,177,199,.22),0 0 40px rgba(20,177,199,.45),30px 50px 70px rgba(0,0,0,.35)}
.cn{display:none}
.tag{position:absolute;z-index:9;font:900 34px/1 InterTightW;color:#06343B;background:#FFD400;padding:14px 26px;border-radius:999px;transform:rotate(-6deg);box-shadow:0 10px 24px rgba(0,0,0,.25)}
.precio{position:absolute;z-index:9;right:50px;bottom:60px;background:#06343B;color:#fff;border-radius:36px;padding:22px 44px;text-align:center;box-shadow:0 0 0 6px #14B1C7,0 20px 40px rgba(0,0,0,.35)}
.precio small{display:block;font:800 30px InterTightW;letter-spacing:.12em;color:#9EE6F0}
.precio b{display:block;font:900 120px/1 InterTightW;letter-spacing:-.03em}
.pills{position:absolute;z-index:6;left:40px;right:40px;display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.pills span{background:rgba(255,255,255,.95);border:3px solid #14B1C7;color:#06343B;font:800 27px InterTightW;padding:12px 22px;border-radius:999px;box-shadow:0 6px 16px rgba(0,0,0,.1)}
.card{position:absolute;z-index:4;border-radius:22px;overflow:hidden;box-shadow:0 0 0 4px #14B1C7,20px 30px 50px rgba(0,0,0,.3)}
.card img{display:block;width:100%}
.plus{position:absolute;z-index:8;width:90px;height:90px;border-radius:50%;background:#14B1C7;color:#fff;font:900 70px/86px InterTightW;text-align:center;box-shadow:0 0 0 8px #fff}
.sello{position:absolute;z-index:9;width:230px;height:230px;border-radius:50%;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;transform:rotate(-8deg);
 box-shadow:0 0 0 8px #14B1C7,0 0 0 18px rgba(20,177,199,.25),0 20px 50px rgba(0,0,0,.3)}
.sello b{font:900 80px/0.95 InterTightW;color:#141414;letter-spacing:-.04em}.sello i{font:900 36px/1 InterTightW;font-style:normal;color:#0A7F90;margin-top:6px}
"""
ST = ("tapa_sintacc_comida.png", "SIN TACC INTELIGENTE")
RP = ("tapa_reposteria.png", "REPOSTERÍA SIN TACC")
TIT = '<div class="t" style="top:{y}px"><h1>Sin TACC <span>Inteligente</span></h1><h2>Comé rico y seguro</h2></div>'
LOGO = '<img class="logo" src="../img/logo.png" style="top:{y}px">'
SELLO = '<div class="sello" style="{p}"><b>100%</b><i>SIN TACC</i></div>'
def pg(n, fondo, inner):
    Path(n + ".html").write_text(f'<!doctype html><meta charset="utf-8"><style>{CSS}{X}body{{--w:1080px;--h:1350px}}</style>'
                                 f'<div class="bg" style="background-image:url(pack/{fondo})"></div><div class="st">{inner}</div>', encoding="utf-8")
# 1 · precio
pg("anuncio_1_precio", "st_fondo1.jpg", LOGO.format(y=50) + TIT.format(y=130) +
   book(*ST, 150, 400, 400, -18, 3) + book(*RP, 560, 450, 360, 18, 2) +
   '<div class="tag" style="left:640px;top:395px">+ DE REGALO</div>' +
   '<div class="precio"><small>PACK COMPLETO</small><b>$7.700</b></div>')
# 2 · todo lo que incluye
pg("anuncio_2_incluye", "st_fondo2.jpg", '<div style="position:absolute;left:0;right:0;top:0;height:380px;z-index:4;background:linear-gradient(#fff 70%,rgba(255,255,255,0))"></div>' + LOGO.format(y=45) + TIT.format(y=120) +
   book(*ST, 110, 420, 380, -14, 3) + '<div class="plus" style="left:495px;top:640px">+</div>' + book(*RP, 600, 420, 380, 14, 3) +
   '<div class="tag" style="left:700px;top:385px">DE REGALO</div>' +
   '<div class="card" style="left:200px;top:1000px;width:190px;transform:rotate(-5deg)"><img src="../../../sin-tacc-inteligente/creativos/bonus_comunidad.png"></div>'
   '<div class="card" style="left:445px;top:990px;width:190px"><img src="../../../sin-tacc-inteligente/creativos/bonus_pausa.png"></div>'
   '<div class="tag" style="left:680px;top:1080px;transform:rotate(-3deg);font-size:30px">+ 2 BONUS:<br>Comunidad RENOVA<br>y Pausa activa</div>')
# 3 · testimonio real (msg_3: alumna de RENOVA, sin nombre; el programa en general, no el ebook Sin TACC)
pg("anuncio_3_testimonio", "st_fondo1.jpg", LOGO.format(y=50) + TIT.format(y=130) +
   '<div class="stars" style="left:60px;top:410px">★★★★★</div>' +
   '<div class="msg" style="left:60px;top:490px;width:560px;transform:rotate(-2deg)"><img src="../img/msg_3.jpg"></div>' +
   '<div class="lbl" style="left:90px;top:1010px">Alumna de RENOVA</div>' +
   book(*ST, 660, 470, 330, -16, 3) + book(*RP, 780, 820, 230, -16, 4) +
   '<div class="tag" style="left:800px;top:790px;font-size:28px;white-space:nowrap">DE REGALO</div>')
# 4 · 3D en podio
pg("anuncio_4_3d", "st_fondo4.jpg", LOGO.format(y=50) + TIT.format(y=130) +
   book(*RP, 580, 470, 330, 24, 2) + book(*ST, 210, 385, 400, -24, 3) +
   SELLO.format(p="left:30px;top:360px") +
   '<div class="pills" style="bottom:50px"><span>✓ Recetas caseras</span><span>✓ Guía de etiquetas</span><span>✓ Cocina sin contaminación</span></div>')
print("ok")
# Portada de Facebook 1640×624 (todo dentro del centro, que es lo que se ve en el celular)
Path("portada_facebook.html").write_text(f'<!doctype html><meta charset="utf-8"><style>{CSS}{X}body{{--w:1640px;--h:624px}}'
    '.t{left:250px;right:auto;width:640px;text-align:left}.t h1{font-size:84px}.t h2{font-size:42px}.bg::after{background:rgba(255,255,255,.75)}.shadow{display:none}.fr{box-shadow:0 0 0 3px #14B1C7,0 0 30px rgba(20,177,199,.45),12px 18px 30px rgba(0,0,0,.18)}</style>'
    '<div class="bg" style="background-image:url(pack/st_fondo1.jpg);background-position:50% 70%"></div><div class="st">'
    '<img class="logo" src="../img/logo.png" style="top:110px;left:250px;transform:none;height:50px">'
    '<div class="t" style="top:185px"><h1>Sin TACC <span>Inteligente</span></h1><h2>Comé rico y seguro</h2></div>'
    + book(*ST, 900, 100, 290, -14, 3) + book(*RP, 1240, 130, 265, 14, 2) + '</div>', encoding="utf-8")
