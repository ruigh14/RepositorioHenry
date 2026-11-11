"""Tapas reales en 3D, una por imagen y las 3 juntas, con fondo de presentación.
Uso: cd fuentes/landing/mockups && python3 libros3d.py && node libros3d.js → ../../../pack-renova/libro_*.png y libros_juntos.png"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "design-system"))
from design_system import css
P = "pack/"
CSS = css(str(Path(__file__).parent)) + """
*{margin:0;padding:0;box-sizing:border-box}
body{width:var(--w);height:var(--h);overflow:hidden;position:relative;
 background:radial-gradient(ellipse 55% 50% at 50% 46%,rgba(20,177,199,.45),transparent 70%),
 radial-gradient(ellipse 80% 30% at 50% 100%,rgba(20,177,199,.15),transparent 70%),#0b1214}
.grid{position:absolute;inset:0;opacity:.07;background-image:linear-gradient(#14B1C7 1px,transparent 1px),linear-gradient(90deg,#14B1C7 1px,transparent 1px);background-size:60px 60px;
 mask-image:radial-gradient(ellipse at 50% 60%,#000 20%,transparent 70%)}
.st{position:absolute;inset:0;perspective:2400px}
.bk{position:absolute;transform-style:preserve-3d}
.fr{position:absolute;inset:0;border-radius:5px 16px 16px 5px;overflow:hidden;
 box-shadow:0 0 0 3px #14B1C7,0 0 0 8px rgba(20,177,199,.22),0 0 60px rgba(20,177,199,.7),50px 70px 100px rgba(0,0,0,.6)}
.fr img{width:100%;height:100%;object-fit:cover;display:block}
.fr::before{content:"";position:absolute;inset:0;z-index:2;background:linear-gradient(115deg,rgba(255,255,255,.4) 0%,rgba(255,255,255,0) 30%,rgba(255,255,255,0) 72%,rgba(255,255,255,.12))}
.fr::after{content:"";position:absolute;left:0;top:0;bottom:0;width:4%;z-index:2;background:linear-gradient(90deg,rgba(0,0,0,.35),rgba(255,255,255,.28),transparent)}
.sp{position:absolute;left:0;top:0;height:100%;transform-origin:left;transform:rotateY(90deg);backface-visibility:hidden;border-radius:4px;
 background:linear-gradient(90deg,#075E6B,#0E9DB2 45%,#14B1C7 55%,#075E6B);box-shadow:inset 0 0 0 2px rgba(255,255,255,.35)}
.sp.r{left:auto;right:0;transform-origin:right;transform:rotateY(-90deg)}
.sp span{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-90deg);white-space:nowrap;font:900 var(--fs) InterTightW,sans-serif;letter-spacing:.18em;color:#fff}
.pg{position:absolute;top:1.5%;bottom:1.5%;right:-1.5%;width:3%;background:repeating-linear-gradient(90deg,#f3f3f3 0 2px,#d9d9d9 2px 3px);transform:rotateY(90deg) translateZ(-2px);transform-origin:left}
.cn{position:absolute;width:6%;aspect-ratio:1;border:4px solid #F9FEFF;z-index:3;filter:drop-shadow(0 0 8px #14B1C7)}
.cn.a{left:-2.5%;top:-1.8%;border-right:0;border-bottom:0}.cn.b{right:-2.5%;bottom:-1.8%;border-left:0;border-top:0}
.shadow{position:absolute;height:70px;border-radius:50%;background:radial-gradient(ellipse,rgba(0,0,0,.75),transparent 70%)}
"""
def book(f, t, x, y, w, ry, z=1):
    h = round(w * 1.414); sw = round(w * .1)
    return (f'<div class="shadow" style="left:{x+w*.05}px;top:{y+h-20}px;width:{w*1.05}px"></div>'
            f'<div class="bk" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;z-index:{z};transform:rotateY({ry}deg)">'
            f'<div class="sp{" r" if ry>0 else ""}" style="width:{sw}px;--fs:{round(w*.042)}px"><span>{t}</span></div>'
            f'<div class="fr"><img src="{P}{f}"></div><div class="cn a"></div><div class="cn b"></div></div>')
def page(name, w, h, inner):
    Path(name + ".html").write_text(f'<!doctype html><meta charset="utf-8"><style>{CSS}body{{--w:{w}px;--h:{h}px}}</style><div class="grid"></div><div class="st">{inner}</div>')
B = [("tapa_casa.jpg", "ENTRENÁ DESDE CASA", "libro_1_casa"), ("tapa_gym.jpg", "ENTRENÁ EN EL GIMNASIO", "libro_2_gimnasio"),
     ("tapa_nutri.jpg", "ALIMENTACIÓN INTELIGENTE", "libro_3_alimentacion")]
for f, t, n in B:
    page(n, 1080, 1350, book(f, t, 250, 150, 600, -22))
page("libros_juntos", 1920, 1080,
     book(B[0][0], B[0][1], 250, 230, 470, -26) + book(B[1][0], B[1][1], 1200, 230, 470, 26) + book(B[2][0], B[2][1], 700, 150, 540, -18, 3))
print("ok")
