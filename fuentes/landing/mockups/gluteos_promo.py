"""Glúteos Fuertes: 3 portadas publicitarias (1080x1350) y un video de 4 s (1080x1920) para redes y tiendas.
Son dos ebooks que se entregan juntos (casa y gimnasio): la portada 1 y el video muestran las dos tapas reales
(pack/tapa_gluteos_casa.jpg y tapa_gluteos_gym.jpg, las saca gluteos_promo.js de fuentes/ebook/gluteos_casa.html y gluteos_gym.html),
las ilustraciones de los ejercicios del ebook y los tokens del design system.

Uso: cd fuentes/ebook && python3 gluteos.py casa && python3 gluteos.py gym
     cd fuentes/landing/mockups && python3 gluteos_promo.py && node gluteos_promo.js
     → gluteos-fuertes/creativos/portada_1..3.jpg y video_4s.mp4
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "design-system"))
from design_system import css

HERE = Path(__file__).parent
IMG = "../../ebook/img/"
TAPAS = {"casa": ("pack/tapa_gluteos_casa.jpg", "GLÚTEOS FUERTES · EN CASA"), "gym": ("pack/tapa_gluteos_gym.jpg", "GLÚTEOS FUERTES · GIMNASIO")}
LOGO = IMG + "logo_renova.png"

BASE = css(str(HERE)) + """
*{margin:0;padding:0;box-sizing:border-box}
body{width:var(--w);height:var(--h);overflow:hidden;position:relative;font-family:var(--rnv-fuente);color:var(--rnv-tinta)}
.disp{font-family:var(--rnv-fuente-display);font-weight:900;text-transform:uppercase;letter-spacing:-.02em;line-height:.88}
.pill{display:inline-block;border-radius:99px;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
/* libro 3D (mismo estilo que libros3d.py) */
.st{position:absolute;inset:0;perspective:2400px}
.bk{position:absolute;transform-style:preserve-3d}
.fr{position:absolute;inset:0;border-radius:5px 16px 16px 5px;overflow:hidden;
 box-shadow:0 0 0 3px var(--rnv-turquesa),0 0 0 8px rgba(20,177,199,.22),0 0 60px rgba(20,177,199,.6),40px 60px 90px rgba(0,0,0,.45)}
.fr img{width:100%;height:100%;object-fit:cover;display:block}
.fr::before{content:"";position:absolute;inset:0;z-index:2;background:linear-gradient(115deg,rgba(255,255,255,.4) 0%,rgba(255,255,255,0) 30%,rgba(255,255,255,0) 72%,rgba(255,255,255,.12))}
.fr::after{content:"";position:absolute;left:0;top:0;bottom:0;width:4%;z-index:2;background:linear-gradient(90deg,rgba(0,0,0,.35),rgba(255,255,255,.28),transparent)}
.sp{position:absolute;left:0;top:0;height:100%;transform-origin:left;transform:rotateY(90deg);backface-visibility:hidden;border-radius:4px;
 background:linear-gradient(90deg,var(--rnv-turquesa-profundo),var(--rnv-turquesa-titulo) 45%,var(--rnv-turquesa) 55%,var(--rnv-turquesa-profundo));box-shadow:inset 0 0 0 2px rgba(255,255,255,.35)}
.sp span{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-90deg);white-space:nowrap;font:900 var(--fs) InterTightW,sans-serif;letter-spacing:.18em;color:#fff}
.shadow{position:absolute;height:60px;border-radius:50%;background:radial-gradient(ellipse,rgba(0,0,0,.55),transparent 70%)}
.ill{background:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;overflow:hidden;box-shadow:var(--rnv-sombra-fuerte)}
.ill img{width:88%;height:88%;object-fit:contain}
"""


def book(x, y, w, ry, cls="", ed="casa"):
    tapa, lomo = TAPAS[ed]
    h = round(w * 1.414); sw = round(w * .1)
    return (f'<div class="shadow {cls}s" style="left:{x + w * .05}px;top:{y + h - 18}px;width:{w * 1.05}px"></div>'
            f'<div class="bk {cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotateY({ry}deg)">'
            f'<div class="sp" style="width:{sw}px;--fs:{round(w * .045)}px"><span>{lomo}</span></div>'
            f'<div class="fr"><img src="{tapa}"></div></div>')


def ill(name, size, extra=""):
    return f'<div class="ill" style="width:{size}px;height:{size}px;{extra}"><img src="{IMG}{name}"></div>'


def write(name, w, h, style, body):
    (HERE / f"{name}.html").write_text(
        f'<!doctype html><meta charset="utf-8"><style>{BASE}body{{--w:{w}px;--h:{h}px}}{style}</style>{body}', encoding="utf-8")


# ---------------------------------------------------------------- 1 · LIBRO 3D (oscuro, como el pack)
write("gluteos_promo_1", 1080, 1350, """
body{background:radial-gradient(ellipse 60% 45% at 50% 58%,rgba(20,177,199,.45),transparent 70%),#0b1214;color:#fff}
.top{position:absolute;top:64px;left:0;right:0;text-align:center}
.top img{height:46px;filter:brightness(0) invert(1)}
.top .pill{margin-top:26px;background:var(--rnv-turquesa);color:#fff;font-size:24px;padding:12px 30px}
.top h1{font-size:104px;margin-top:22px}
.top h1 span{color:var(--rnv-turquesa-claro)}
.bot{position:absolute;bottom:60px;left:0;right:0;text-align:center}
.bot p{font-size:36px;font-weight:700}
.bot .row{margin-top:20px;display:flex;gap:14px;justify-content:center}
.bot .row span{border:2px solid var(--rnv-turquesa);color:#fff;font-size:24px;padding:10px 24px;border-radius:99px;font-weight:700}
""", f'''
<div class="top"><img src="{LOGO}"><br><span class="pill">Nuevo · 2 ebooks · Método RENOVA</span><h1 class="disp">Glúteos <span>fuertes</span></h1></div>
<div class="st">{book(110, 420, 410, 22, ed="gym")}{book(550, 400, 420, -22, ed="casa")}</div>
<div class="bot"><p>Tu día extra: 8 semanas para glúteos y cadera</p>
<div class="row"><span>En casa + en el gimnasio</span><span>Mujeres 40+</span><span>Plan de 8 semanas</span></div></div>
''')

# ---------------------------------------------------------------- 2 · TIPOGRÁFICA CLARA (como la tapa del ebook)
write("gluteos_promo_2", 1080, 1350, """
body{background:#fff;border:22px solid var(--rnv-turquesa-profundo)}
.in{position:absolute;inset:0;padding:70px 70px 0;display:flex;flex-direction:column;align-items:center;text-align:center}
.in img.logo{height:50px}
.in .pill{margin-top:30px;background:var(--rnv-tinta);color:#fff;font-size:26px;padding:14px 34px}
.in h1{font-size:176px;color:var(--rnv-turquesa-oscuro);margin-top:30px}
.claim{font-family:var(--rnv-fuente-display);font-weight:900;font-size:58px;margin-top:22px}
.claim b{display:inline-block;transform:rotate(-2.5deg);padding:0 14px;background:linear-gradient(transparent 58%,var(--rnv-turquesa-borde) 58%,var(--rnv-turquesa-borde) 92%,transparent 92%);text-shadow:4px 4px 0 var(--rnv-turquesa-claro)}
.hero{position:absolute;left:0;right:0;bottom:0;height:600px;background:#fff;border-top:6px solid var(--rnv-turquesa-borde);display:flex;align-items:center;justify-content:center;gap:40px}
.hero .big{width:600px}
.hero ul{list-style:none;text-align:left}
.hero li{font-size:34px;font-weight:800;margin:14px 0}
.hero li::before{content:"✓ ";color:var(--rnv-turquesa-titulo)}
""", f'''
<div class="in"><img class="logo" src="{LOGO}"><span class="pill">Método RENOVA · Mujeres 40+</span>
<h1 class="disp">Glúteos<br>fuertes</h1><p class="claim">TU DÍA EXTRA, <b>8 SEMANAS.</b></p></div>
<div class="hero"><img class="big" src="{IMG}r1_4.png"><ul><li>Cadera</li><li>Rodillas</li><li>Espalda</li><li>Postura</li></ul></div>
''')

# ---------------------------------------------------------------- 3 · EJERCICIOS (turquesa profundo)
EJS = [("gym_hipthrust.png", "Hip thrust"), ("r3_5b.png", "Peso muerto"), ("r3_3.png", "Sentadilla sumo"), ("r2_1.png", "Subida al banco")]
write("gluteos_promo_3", 1080, 1350, """
body{background:linear-gradient(160deg,var(--rnv-turquesa-profundo),#05363E);color:#fff}
.hd{position:absolute;top:70px;left:70px;right:70px}
.hd img{height:42px;filter:brightness(0) invert(1)}
.hd h1{font-size:150px;margin-top:34px}
.hd h1 span{-webkit-text-stroke:4px var(--rnv-turquesa-claro);color:transparent}
.hd p{font-size:36px;font-weight:600;margin-top:24px;max-width:860px;line-height:1.25}
.grid{position:absolute;top:660px;left:70px;right:70px;display:grid;grid-template-columns:repeat(4,1fr);gap:20px;text-align:center}
.grid b{display:block;margin-top:14px;font-size:24px}
.chips{position:absolute;top:1010px;left:70px;right:70px;display:flex;gap:14px}
.chips span{flex:1;text-align:center;border:2px solid var(--rnv-turquesa-claro);border-radius:99px;font-size:26px;font-weight:700;padding:14px 0}
.ft{position:absolute;bottom:70px;left:70px;right:70px;display:flex;justify-content:space-between;align-items:center}
.ft .pill{background:var(--rnv-turquesa);color:#fff;font-size:28px;padding:18px 36px}
.ft span{font-size:28px;font-weight:700;opacity:.9}
""", f'''
<div class="hd"><img src="{LOGO}"><h1 class="disp">Glúteos<br><span>fuertes</span></h1>
<p>Un día por semana, 8 semanas, en casa o en el gimnasio. Para cuidar tu cadera, tus rodillas y tu espalda.</p></div>
<div class="grid">{"".join(f"<div>{ill(i, 210, 'margin:0 auto')}<b>{t}</b></div>" for i, t in EJS)}</div>
<div class="chips"><span>Casa o gimnasio</span><span>Plan de 8 semanas</span><span>1 día por semana</span></div>
<div class="ft"><span class="pill">Sumalo a tu Método RENOVA</span><span>Mujeres 40+</span></div>
''')

# ---------------------------------------------------------------- VIDEO 4 s (vertical)
# gluteos_promo.js pausa las animaciones y saca un cuadro cada 1/30 s (120 cuadros) → ffmpeg → mp4.
write("gluteos_promo_video", 1080, 1920, """
body{background:radial-gradient(ellipse 70% 40% at 50% 55%,rgba(20,177,199,.5),transparent 70%),#0b1214;color:#fff}
@keyframes up{from{transform:translateY(120%)}to{transform:none}}
@keyframes fade{from{opacity:0}to{opacity:1}}
@keyframes pop{0%{transform:scale(.4);opacity:0}70%{transform:scale(1.08);opacity:1}100%{transform:scale(1)}}
@keyframes spin{from{transform:rotateY(-75deg) translateX(-200px);opacity:0}to{transform:rotateY(-18deg);opacity:1}}
@keyframes float{from{transform:rotateY(-18deg) translateY(0)}to{transform:rotateY(-12deg) translateY(-18px)}}
@keyframes zoom{from{transform:scale(1)}to{transform:scale(1.06)}}
.all{position:absolute;inset:0;animation:zoom 4s linear both}
.logo{position:absolute;top:110px;left:0;right:0;text-align:center;animation:fade .4s both}
.logo img{height:52px;filter:brightness(0) invert(1)}
.t{position:absolute;top:210px;left:0;right:0;text-align:center}
.t div{overflow:hidden;line-height:.9;padding-top:40px;margin-top:-30px}
.t h1{font-size:200px;animation:up .5s cubic-bezier(.2,.9,.3,1) both}
.t div:nth-child(2) h1{color:var(--rnv-turquesa-claro);animation-delay:.18s}
@keyframes spinr{from{transform:rotateY(75deg) translateX(200px);opacity:0}to{transform:rotateY(18deg);opacity:1}}
@keyframes floatr{from{transform:rotateY(18deg) translateY(0)}to{transform:rotateY(12deg) translateY(-18px)}}
.bk{animation:spin .8s .5s cubic-bezier(.2,.9,.3,1) both,float 2.7s 1.3s ease-in-out both}
.bk.bkr{animation:spinr .8s .75s cubic-bezier(.2,.9,.3,1) both,floatr 2.45s 1.55s ease-in-out both}
.shadow{animation:fade .6s .7s both}
.pills{position:absolute;top:1430px;left:0;right:0;display:flex;gap:16px;justify-content:center}
.pills span{border:3px solid var(--rnv-turquesa);border-radius:99px;font-size:34px;font-weight:800;padding:14px 30px;animation:pop .45s both}
.pills span:nth-child(1){animation-delay:1.5s}.pills span:nth-child(2){animation-delay:1.75s}.pills span:nth-child(3){animation-delay:2s}
.cta{position:absolute;bottom:170px;left:0;right:0;text-align:center;animation:pop .5s 2.6s both}
.cta span{display:inline-block;background:var(--rnv-turquesa);border-radius:99px;font-size:46px;font-weight:900;padding:26px 56px;box-shadow:var(--rnv-sombra-boton)}
.cta p{margin-top:22px;font-size:32px;font-weight:600;opacity:.9}
""", f'''
<div class="all">
<div class="logo"><img src="{LOGO}"></div>
<div class="t disp"><div><h1 class="disp">Glúteos</h1></div><div><h1 class="disp">fuertes</h1></div></div>
<div class="st"><div class="g2">{book(150, 700, 370, 18, "bkr", ed="gym")}</div>{book(560, 660, 390, -18, ed="casa")}</div>
<div class="pills"><span>Cadera</span><span>Rodillas</span><span>Espalda</span></div>
<div class="cta"><span>TU DÍA EXTRA · 8 SEMANAS</span><p>2 ebooks: en casa + en el gimnasio · Mujeres 40+</p></div>
</div>
''')
print("ok: gluteos_promo_1..3.html y gluteos_promo_video.html")
