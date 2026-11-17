"""Portadas (1080x1440) de los 2 bonus y el upsell de la tienda Sin TACC: comunidad con talleres, pausa activa
y pack de entrenamiento casa + gimnasio. Mismo fondo y libro 3D que el resto de los mockups.
Uso: cd fuentes/landing/mockups && python3 tienda_sintacc_extras.py && node tienda_sintacc_extras.js
  → ../../../sin-tacc-inteligente/creativos/{bonus_comunidad,bonus_pausa,upsell_entrenamiento}.png"""
import io, contextlib
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    from libros3d import CSS, book
EXTRA = """
.tag{position:absolute;left:50%;top:90px;transform:translateX(-50%);z-index:9;background:#14B1C7;color:#fff;font:900 30px InterTightW,sans-serif;letter-spacing:.16em;padding:12px 34px;border-radius:999px;box-shadow:0 0 30px rgba(20,177,199,.6)}
.tit{position:absolute;left:60px;right:60px;bottom:110px;z-index:9;text-align:center;color:#fff;font:900 76px/1.02 InterTightW,sans-serif;text-transform:uppercase;letter-spacing:-.02em}
.tit b{color:#6FD8E6}.tit small{display:block;margin-top:18px;font:700 34px/1.3 InterW,sans-serif;text-transform:none;letter-spacing:0;color:#BDEFF5}
.foto{position:absolute;left:110px;right:110px;top:220px;height:720px;border-radius:30px;overflow:hidden;z-index:5;
 box-shadow:0 0 0 6px #14B1C7,0 0 0 16px rgba(20,177,199,.22),0 0 70px rgba(20,177,199,.7),0 40px 80px rgba(0,0,0,.6)}
.foto img{width:100%;height:100%;object-fit:cover;object-position:50% 35%}
.mini{position:absolute;right:70px;top:780px;width:330px;height:250px;border-radius:22px;overflow:hidden;z-index:6;transform:rotate(4deg);
 box-shadow:0 0 0 6px #fff,0 30px 60px rgba(0,0,0,.6)}
.mini img{width:100%;height:100%;object-fit:cover}
"""
def page(name, inner):
    Path(name + ".html").write_text(f'<!doctype html><meta charset="utf-8"><style>{CSS}{EXTRA}body{{--w:1080px;--h:1440px}}</style>'
                                    f'<div class="grid"></div><div class="st">{inner}</div>', encoding="utf-8")
page("bonus_comunidad", '<span class="tag">BONUS 1</span>'
     '<div class="foto"><img src="../img/comunidad.jpg"></div><div class="mini"><img src="../img/taller_super.jpg"></div>'
     '<div class="tit">Comunidad <b>RENOVA</b><small>Talleres de nuestra nutricionista y nuestra psicóloga</small></div>')
page("bonus_pausa", '<span class="tag">BONUS 2</span>' + book("tapa_pausa.jpg", "PAUSA ACTIVA", 250, 200, 580, -16)
     + '<div class="tit">Pausa activa <b>en 10 minutos</b><small>4 rutinas para moverte en casa o en el trabajo</small></div>')
page("upsell_entrenamiento", '<span class="tag">SUMALO A TU COMPRA</span>'
     + book("tapa_casa.jpg", "ENTRENÁ DESDE CASA", 90, 260, 470, -18, 1)
     + book("tapa_gym.jpg", "ENTRENÁ EN EL GIMNASIO", 520, 230, 470, 18, 2)
     + '<div class="tit">Entrená en <b>casa o gimnasio</b><small>Planes de 8 semanas, de bajo impacto, con video de cada ejercicio</small></div>')
print("ok")
