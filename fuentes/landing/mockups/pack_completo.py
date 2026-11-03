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
.scr{position:absolute;background:#111;border-radius:22px;padding:14px;box-shadow:0 0 0 3px #14B1C7,0 0 50px rgba(20,177,199,.6),40px 50px 90px rgba(0,0,0,.6);transform:perspective(1800px) rotateY(-14deg)}
.scr .in{position:relative;width:100%;height:100%;border-radius:10px;overflow:hidden}
.scr img{width:100%;height:100%;object-fit:cover;display:block}
.play{position:absolute;left:50%;top:50%;width:92px;height:92px;margin:-46px 0 0 -46px;border-radius:50%;background:rgba(20,177,199,.92);box-shadow:0 0 30px rgba(20,177,199,.8)}
.play:after{content:"";position:absolute;left:36px;top:26px;border-left:30px solid #fff;border-top:20px solid transparent;border-bottom:20px solid transparent}
.live{position:absolute;left:16px;top:16px;background:#E63333;color:#fff;font:800 18px InterTightW,sans-serif;letter-spacing:.1em;padding:6px 12px;border-radius:8px}
.lb{position:absolute;color:#fff;font:800 22px InterTightW,sans-serif;letter-spacing:.12em;text-transform:uppercase;text-align:center}
.lb b{color:#14B1C7}
.chips{position:absolute;left:0;right:0;bottom:46px;display:flex;justify-content:center;gap:16px;z-index:6}
.chips span{background:rgba(255,255,255,.95);color:#141414;font:800 22px InterTightW,sans-serif;padding:12px 22px;border-radius:999px;box-shadow:0 10px 24px rgba(0,0,0,.35)}
.chips i{font-style:normal;color:#0A7F90;margin-right:6px}
.top{position:absolute;top:44px;left:0;right:0;text-align:center;color:#fff;z-index:6}
.top h1{font:900 64px/1 InterTightW,sans-serif;text-transform:uppercase;letter-spacing:-.02em}
.top h1 b{color:#14B1C7}
"""
CSS2 = CSS + X
def pg(name,w,h,inner):
    Path(name + ".html").write_text(f'<!doctype html><meta charset="utf-8"><style>{CSS2}body{{--w:{w}px;--h:{h}px}}</style><div class="grid"></div><div class="st">{inner}</div>')
inner = """<div class="top"><img src="../img/logo.png" style="height:40px;filter:brightness(0) invert(1)"><h1 style="margin-top:12px">Método RENOVA · 3 ebooks <b>+ 5 bonus</b></h1></div>"""
# pausa activa (bonus) a la izquierda
inner += book("tapa_pausa.jpg","PAUSA ACTIVA",50,340,230,-24)
inner += book("express_casa.jpg","SESIÓN EXPRESS",230,420,210,-20)
# 3 ebooks al centro
inner += book("tapa_casa.jpg","ENTRENÁ DESDE CASA",480,300,300,-18,2)
inner += book("tapa_gym.jpg","ENTRENÁ EN EL GIMNASIO",1110,300,300,18,2)
inner += book("tapa_nutri.jpg","ALIMENTACIÓN INTELIGENTE",800,250,320,0,4)
# talleres en pantalla a la derecha
inner += '<div class="scr" style="left:1420px;top:330px;width:440px;height:280px"><div class="in"><img src="../img/habitos.jpg"><span class="live">EN VIVO</span><div class="play"></div></div></div>'
inner += '<div class="scr" style="left:1450px;top:640px;width:380px;height:220px"><div class="in"><img src="../img/comunidad.jpg"></div></div>'
inner += '<div class="lb" style="left:1420px;top:290px;width:440px">Talleres <b>grabados y en vivo</b></div>'
inner += '<div class="lb" style="left:1450px;top:875px;width:380px">Comunidad <b>de por vida</b></div>'
inner += '<div class="chips"><span><i>+</i>Pausa activa</span><span><i>+</i>Rutinas express</span><span><i>+</i>Abdominales</span><span><i>+</i>Talleres</span><span><i>+</i>Comunidad</span></div>'
pg("pack_completo",1920,1080,inner)
print("ok")
