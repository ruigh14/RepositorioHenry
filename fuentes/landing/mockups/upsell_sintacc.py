"""Portada del upsell post compra "Sin TACC Inteligente" (1080×1080): tapa real en 3D + sello "100% SIN TACC".
Uso: cd fuentes/landing/mockups && python3 upsell_sintacc.py && node upsell_sintacc.js → ../../../sin-tacc-inteligente/creativos/upsell_portada.png
La tapa (pack/tapa_sintacc.png) es la hoja 1 del PDF: pdftoppm -r 150 -png -f 1 -l 1 <pdf> pack/tapa_sintacc
"""
import io
import contextlib
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    from libros3d import CSS, book   # mismo libro 3D y fondo que el resto de los mockups

EXTRA = """
.sello{position:absolute;right:60px;top:110px;width:270px;height:270px;border-radius:50%;z-index:9;
 background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
 box-shadow:0 0 0 8px #14B1C7,0 0 0 18px rgba(20,177,199,.25),0 0 70px rgba(20,177,199,.8),0 30px 60px rgba(0,0,0,.5);transform:rotate(-8deg)}
.sello b{display:block;font:900 96px/0.95 InterTightW,sans-serif;color:#141414;letter-spacing:-.04em}
.sello i{display:block;font:900 44px/1 InterTightW,sans-serif;font-style:normal;color:#0A7F90;letter-spacing:.02em;margin-top:8px}
.sello small{display:block;margin-top:12px;font:800 15px InterW,sans-serif;letter-spacing:.16em;color:#555C62}
.pie{position:absolute;left:0;right:0;bottom:56px;text-align:center;z-index:9;font:800 34px InterTightW,sans-serif;color:#fff;letter-spacing:.01em}
.pie span{color:#6FD8E6}
"""
inner = (book("tapa_sintacc.png", "SIN TACC INTELIGENTE", 110, 85, 550, -20)
         + '<div class="sello"><b>100%</b><i>SIN TACC</i><small>18 RECETAS</small></div>')
Path("upsell_sintacc.html").write_text(
    f'<!doctype html><meta charset="utf-8"><style>{CSS}{EXTRA}body{{--w:1080px;--h:1080px}}</style><div class="grid"></div><div class="st">{inner}</div>')
print("ok")
