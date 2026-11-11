"""Mockups del PACK RENOVA (3 ebooks + 5 bonus) para videos de Meta Ads, 1080x1920.
Usa las tapas e interiores reales de los PDF (pack/*.jpg, sacados con pdftoppm).
Uso: cd fuentes/landing/mockups && python3 pack.py && node pack.js  →  ../../../pack-renova/pack_1..3.png"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "design-system"))
from design_system import css

I, P = "../img/", "pack/"
BASE = css(str(Path(__file__).parent)) + """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;overflow:hidden;position:relative;font-family:InterW,sans-serif;color:#fff;
 background:radial-gradient(ellipse 70% 45% at 50% 42%,rgba(20,177,199,.38),transparent 70%),
            radial-gradient(ellipse 60% 30% at 50% 100%,rgba(20,177,199,.18),transparent 70%),#0d1416}
.top{position:absolute;top:96px;left:0;right:0;text-align:center}
.top img{height:58px;filter:brightness(0) invert(1)}
.eye{display:inline-block;margin-top:26px;font:800 26px InterTightW,sans-serif;letter-spacing:.28em;text-transform:uppercase;color:var(--rnv-turquesa)}
h1{font:900 92px/0.98 InterTightW,sans-serif;text-transform:uppercase;letter-spacing:-.02em;margin-top:14px}
h1 b{color:var(--rnv-turquesa)}
.book{position:absolute;border-radius:4px 12px 12px 4px;overflow:hidden;background:#fff;
 box-shadow:30px 40px 70px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.06)}
.book img{width:100%;height:100%;object-fit:cover;display:block}
.book::after{content:"";position:absolute;inset:0 auto 0 0;width:5%;background:linear-gradient(90deg,rgba(0,0,0,.28),rgba(255,255,255,.18) 60%,transparent)}
.floor{position:absolute;left:90px;right:90px;height:60px;border-radius:50%;background:radial-gradient(ellipse,rgba(0,0,0,.6),transparent 70%)}
.lbl{position:absolute;font:800 24px InterTightW,sans-serif;letter-spacing:.08em;text-transform:uppercase;text-align:center}
.bon{position:absolute;display:flex;align-items:center;gap:18px;background:rgba(255,255,255,.96);color:var(--rnv-tinta);
 border-radius:22px;padding:14px 22px 14px 14px;box-shadow:0 22px 44px rgba(0,0,0,.4)}
.bon img{width:96px;height:96px;border-radius:14px;object-fit:cover;flex:none}
.bon i{display:block;font:800 18px InterTightW,sans-serif;letter-spacing:.14em;color:var(--rnv-turquesa-oscuro);font-style:normal}
.bon b{display:block;font:800 30px/1.1 InterTightW,sans-serif}
.foot{position:absolute;bottom:92px;left:0;right:0;text-align:center;font:800 34px InterTightW,sans-serif;letter-spacing:.12em;text-transform:uppercase}
.foot span{color:var(--rnv-turquesa)}
.tab{position:absolute;background:#111;border-radius:46px;padding:26px;box-shadow:40px 50px 90px rgba(0,0,0,.6),inset 0 0 0 3px #2b3236}
.tab .sc{width:100%;height:100%;border-radius:20px;overflow:hidden;background:#fff}
.tab .sc img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.ph{position:absolute;background:#111;border-radius:56px;padding:16px;box-shadow:30px 40px 80px rgba(0,0,0,.65),inset 0 0 0 3px #2b3236}
.ph .sc{width:100%;height:100%;border-radius:42px;overflow:hidden;background:#fff;position:relative}
.ph .sc img{position:absolute;display:block}
.ph .notch{position:absolute;top:30px;left:50%;width:110px;height:30px;margin-left:-55px;background:#111;border-radius:20px;z-index:2}
"""

BONUS = [("pausa_bon.jpg", "Pausa activa"), ("foto_subidas.jpg", "Rutinas express de 15 minutos"),
         ("foto_abdominales.jpg", "Rutinas de abdominales"), ("taller_super.jpg", "Talleres del equipo RENOVA"),
         ("comunidad.jpg", "Acceso de por vida a la comunidad")]


def bon(i, x, y, w):
    f, t = BONUS[i]
    src = (P + "tapa_pausa.jpg") if f == "pausa_bon.jpg" else (I + f)
    pos = "object-position:50% 12%" if f == "pausa_bon.jpg" else ""
    return f'<div class="bon" style="left:{x}px;top:{y}px;width:{w}px"><img src="{src}" style="{pos}"><div><i>BONUS {i+1}</i><b>{t}</b></div></div>'


def head(eye, h):
    return f'<div class="top"><img src="{I}logo.png"><br><span class="eye">{eye}</span><h1>{h}</h1></div>'


def page(body):
    return f'<!doctype html><meta charset="utf-8"><style>{BASE}</style>{body}'


# 1 — PACK COMPLETO: 3 libros en abanico + 5 bonus
W, H = 290, 410
p1 = page(head("Pack digital", "3 ebooks <b>+</b><br>5 bonus") + f"""
<div class="floor" style="top:1060px"></div>
<div class="book" style="left:95px;top:600px;width:{W}px;height:{H}px;transform:rotate(-8deg)"><img src="{P}tapa_casa.jpg"></div>
<div class="book" style="right:95px;top:600px;width:{W}px;height:{H}px;transform:rotate(8deg)"><img src="{P}tapa_gym.jpg"></div>
<div class="book" style="left:340px;top:540px;width:400px;height:566px;z-index:3"><img src="{P}tapa_nutri.jpg"></div>
{bon(0, 60, 1180, 470)}{bon(1, 550, 1180, 470)}
{bon(2, 60, 1335, 470)}{bon(3, 550, 1335, 470)}
{bon(4, 280, 1490, 520)}
<div class="foot">Acceso <span>inmediato</span></div>""")

# 2 — LOS TRES EBOOKS, cada uno con su etiqueta
BW, BH = 320, 452
labels = [("tapa_casa.jpg", "Entrená<br>desde casa"), ("tapa_gym.jpg", "Entrená en<br>el gimnasio"), ("tapa_nutri.jpg", "Alimentación<br>inteligente")]
books = ""
for k, (f, t) in enumerate(labels):
    x = 40 + k * 340
    books += (f'<div class="book" style="left:{x}px;top:640px;width:{BW}px;height:{BH}px"><img src="{P}{f}"></div>'
              f'<div class="lbl" style="left:{x}px;top:1130px;width:{BW}px;font-size:28px">0{k+1}<br><span style="color:var(--rnv-turquesa)">{t}</span></div>')
p2 = page(head("Los 3 ebooks", "Entrenamiento<br><b>y nutrición</b>") + f"""
<div class="floor" style="top:1070px"></div>{books}
<div class="lbl" style="left:90px;right:90px;top:1420px;font-size:30px;letter-spacing:.04em;text-transform:none;font-weight:700;color:#cfe9ee">
En casa o en el gimnasio, con video de cada ejercicio,<br>y un plan de nutrición de 8 semanas.</div>
<div class="foot">Método <span>RENOVA</span></div>""")

# 3 — EN DISPOSITIVOS: tablet con rutina + celular con receta + libros chicos
p3 = page(head("Llevalo en tu celular", "Todo en tus<br><b>dispositivos</b>") + f"""
<div class="tab" style="left:70px;top:560px;width:690px;height:930px;transform:rotate(-4deg)"><div class="sc"><img src="{P}in_casa.jpg"></div></div>
<div class="ph" style="left:600px;top:800px;width:380px;height:780px;transform:rotate(5deg)"><div class="notch"></div>
 <div class="sc"><img src="{P}in_nutri.jpg" style="width:820px;left:-14px;top:40px"></div></div>
<div class="book" style="left:110px;top:1430px;width:170px;height:240px;transform:rotate(-6deg)"><img src="{P}tapa_casa.jpg"></div>
<div class="book" style="left:270px;top:1450px;width:170px;height:240px;transform:rotate(2deg)"><img src="{P}tapa_gym.jpg"></div>
<div class="book" style="left:430px;top:1440px;width:170px;height:240px;transform:rotate(7deg)"><img src="{P}tapa_nutri.jpg"></div>
<div class="foot" style="bottom:70px">Rutinas · videos · <span>recetas</span></div>""")

for n, h in (("pack_1", p1), ("pack_2", p2), ("pack_3", p3)):
    Path(n + ".html").write_text(h)
print("ok")
