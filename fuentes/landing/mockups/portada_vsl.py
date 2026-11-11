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

X = """
body{background:#0b1214}
.bgp{position:absolute;inset:0;background:url(pack/nacho_vsl.jpg) center 85%/cover;filter:blur(28px) brightness(.85);transform:scale(1.1)}
.ph{position:absolute;left:-100px;top:167px;width:2120px;height:913px;background:url(pack/nacho_vsl.jpg) center/100% 100%;
 -webkit-mask-image:linear-gradient(180deg,transparent 0,#000 140px)}
.shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,18,20,.55) 0,rgba(11,18,20,0) 28%,rgba(11,18,20,0) 74%,rgba(11,18,20,.55) 100%)}
.team{position:absolute;right:40px;top:330px;width:440px;background:#fff;border-radius:22px;overflow:hidden;
 box-shadow:0 0 0 4px #14B1C7,0 0 50px rgba(20,177,199,.6),30px 40px 80px rgba(0,0,0,.5);transform:perspective(1600px) rotateY(-12deg)}
.team img{width:100%;display:block;background:linear-gradient(#E8F6F8,#fff)}
.team p{background:#141414;color:#fff;text-align:center;font:800 24px InterTightW,sans-serif;letter-spacing:.12em;padding:14px 10px;text-transform:uppercase}
.team p b{color:#14B1C7}
.tit{position:absolute;top:40px;left:0;right:0;text-align:center;z-index:6;color:#fff;text-shadow:0 4px 20px rgba(0,0,0,.5)}
.tit img{height:46px;filter:brightness(0) invert(1)}
.lbl{position:absolute;left:60px;top:950px;width:440px;background:rgba(20,20,20,.85);border-radius:999px;padding:12px 0;text-align:center;color:#fff;font:800 24px InterTightW,sans-serif;letter-spacing:.12em;text-transform:uppercase;z-index:6;text-shadow:0 3px 12px rgba(0,0,0,.6)}
.lbl b{color:#14B1C7}
"""
CSS2 = CSS + X
inner = '<div class="bgp"></div><div class="ph"></div><div class="shade"></div>'
inner += '<div class="tit"><img src="../img/logo.png"></div>'
inner += book("tapa_casa.jpg","ENTRENÁ DESDE CASA",40,210,210,-14,2)
inner += book("tapa_gym.jpg","ENTRENÁ EN EL GIMNASIO",275,250,210,-14,2)
inner += book("tapa_nutri.jpg","ALIMENTACIÓN INTELIGENTE",140,560,240,-14,4)
inner += '<div class="lbl">3 ebooks <b>+ 5 bonus</b></div>'
inner += '<div class="team"><img src="../img/equipo_tapa_limpia.png"><p>Equipo <b>interdisciplinario</b></p></div>'
Path("portada_vsl.html").write_text(f'<!doctype html><meta charset="utf-8"><style>{CSS2}body{{--w:1920px;--h:1080px}}</style><div class="st">{inner}</div>')
print("ok")
