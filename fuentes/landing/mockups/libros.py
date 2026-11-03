"""Los 3 ebooks en 3D con borde futurista (tapas reales), fondo transparente.
Uso: cd fuentes/landing/mockups && python3 libros.py && node libros.js → ../../../pack-renova/pack_libros.png"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "design-system"))
from design_system import css
P = "pack/"
B = [("tapa_casa.jpg", "ENTRENÁ DESDE CASA", -26, 60, 230, .86),
     ("tapa_gym.jpg", "ENTRENÁ EN EL GIMNASIO", 26, 980, 230, .86),
     ("tapa_nutri.jpg", "ALIMENTACIÓN INTELIGENTE", -12, 460, 150, 1)]
CSS = css(str(Path(__file__).parent)) + """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1600px;height:1300px;background:transparent;overflow:hidden}
.st{position:absolute;inset:0;perspective:2200px}
.bk{position:absolute;width:560px;height:792px;transform-style:preserve-3d}
.fr{position:absolute;inset:0;border-radius:6px 18px 18px 6px;overflow:hidden;
 box-shadow:0 0 0 3px #14B1C7,0 0 0 7px rgba(20,177,199,.25),0 0 46px rgba(20,177,199,.75),40px 60px 90px rgba(0,0,0,.55)}
.fr img{width:100%;height:100%;object-fit:cover;display:block}
.fr::before{content:"";position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.38) 0%,rgba(255,255,255,0) 28%,rgba(255,255,255,0) 70%,rgba(255,255,255,.12) 100%);z-index:2}
.fr::after{content:"";position:absolute;left:0;top:0;bottom:0;width:22px;background:linear-gradient(90deg,rgba(0,0,0,.35),rgba(255,255,255,.25),transparent);z-index:2}
.sp{position:absolute;left:0;top:0;width:56px;height:792px;transform-origin:left;transform:rotateY(90deg);
 background:linear-gradient(90deg,#075E6B,#0E9DB2 45%,#14B1C7 55%,#075E6B);border-radius:4px;
 box-shadow:inset 0 0 0 2px rgba(255,255,255,.35),0 0 30px rgba(20,177,199,.6)}
.sp.r{left:auto;right:0;transform-origin:right;transform:rotateY(-90deg)}
.sp{backface-visibility:hidden}
.sp span{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-90deg);white-space:nowrap;
 font:900 24px InterTightW,sans-serif;letter-spacing:.18em;color:#fff}
.cn{position:absolute;width:44px;height:44px;border:4px solid #F9FEFF;z-index:3;filter:drop-shadow(0 0 8px #14B1C7)}
.cn.a{left:-14px;top:-14px;border-right:0;border-bottom:0}.cn.b{right:-14px;bottom:-14px;border-left:0;border-top:0}
"""
html = ""
for f, t, ry, x, y, sc in B:
    z = 3 if sc == 1 else 1
    html += (f'<div class="bk" style="left:{x}px;top:{y}px;z-index:{z};transform:scale({sc}) rotateY({ry}deg)">'
             f'<div class="sp{" r" if ry>0 else ""}"><span>{t}</span></div><div class="fr"><img src="{P}{f}"></div>'
             f'<div class="cn a"></div><div class="cn b"></div></div>')
Path("libros.html").write_text(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><div class="st">{html}</div>')
print("ok")
