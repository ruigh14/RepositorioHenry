"""Carrusel del pack RENOVA mujeres: 3 ebooks + 5 bonus, una imagen por producto (1080×1350), mismo estilo que pack_checkout.
Uso: cd fuentes/landing/mockups && python3 carrusel_pack.py && node carrusel_pack.js → ../../../pack-renova/carrusel/01..08.png"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "design-system"))
from design_system import css
I, P = "../img/", "pack/"
# (archivo, tipo: libro|foto, etiqueta, título, descripción)
ITEMS = [
 (P + "tapa_casa.jpg", "libro", "EBOOK 1", "Entrená<br>desde casa", "8 semanas de rutinas de fuerza, con video de cada ejercicio."),
 (P + "tapa_gym.jpg", "libro", "EBOOK 2", "Entrená en<br>el gimnasio", "El plan de 8 semanas con máquinas y pesas, desde nivel inicial."),
 (P + "tapa_nutri.jpg", "libro", "EBOOK 3", "Alimentación<br>Inteligente", "Plan de 8 semanas con recetas, menús y lista de compras."),
 (P + "tapa_pausa.jpg", "libro", "BONUS 1", "Pausa<br>activa", "4 rutinas de 10 minutos para la oficina o tu casa."),
 (P + "tapa_express.png", "libro", "BONUS 2", "Rutinas express<br>de 15 minutos", "Para las semanas con poco tiempo, sin cortar el plan."),
 (P + "plancha.jpg", "foto", "BONUS 3", "Rutinas de<br>abdominales", "Para fortalecer tu zona media."),
 (I + "taller_super.jpg", "foto", "BONUS 4", "Talleres con<br>profesionales", "Nutrición, hábitos, estrés y sueño, con nuestro equipo."),
 (P + "tapa_comunidad.png", "libro", "BONUS 5", "Comunidad<br>RENOVA", "Acceso a la comunidad en Skool, con cursos y talleres."),
]
CSS = css(str(Path(__file__).parent)) + """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;overflow:hidden;font-family:InterW,sans-serif;color:var(--rnv-tinta);text-align:center;
 background:linear-gradient(180deg,#fff 0%,var(--rnv-turquesa-fondo) 100%)}
.top{padding-top:80px}.top img{height:56px}
.tag{display:inline-block;margin-top:30px;font:900 30px InterTightW,sans-serif;letter-spacing:.14em;color:#fff;background:var(--rnv-turquesa);padding:10px 30px;border-radius:999px}
.tag.b{background:var(--rnv-oro);color:var(--rnv-tinta)}
.obj{margin:44px auto 0;display:flex;justify-content:center;align-items:center;height:760px}
.tapa{height:740px;aspect-ratio:210/297;border-radius:6px 16px 16px 6px;overflow:hidden;background:#fff;position:relative;
 box-shadow:26px 36px 60px rgba(6,52,59,.3),0 0 0 1px rgba(0,0,0,.05)}
.tapa img{width:100%;height:100%;object-fit:cover;object-position:50% 0;display:block}
.tapa::after{content:"";position:absolute;inset:0 auto 0 0;width:5%;background:linear-gradient(90deg,rgba(0,0,0,.25),rgba(255,255,255,.15) 60%,transparent)}
.foto{width:900px;height:675px;border-radius:30px;overflow:hidden;box-shadow:0 0 0 8px #fff,0 0 0 11px var(--rnv-turquesa-borde),26px 36px 60px rgba(6,52,59,.25)}
.foto img{width:100%;height:100%;object-fit:cover;display:block}
h1{font:900 64px/1.02 InterTightW,sans-serif;letter-spacing:-.02em;text-transform:uppercase;margin-top:44px}
p{font:600 42px/1.25 InterW,sans-serif;color:var(--rnv-gris);margin:18px 70px 0}
"""
out = Path(".")
for n, (src, tipo, tag, tit, desc) in enumerate(ITEMS, 1):
    obj = f'<div class="tapa"><img src="{src}"></div>' if tipo == "libro" else f'<div class="foto"><img src="{src}"></div>'
    tit1 = tit.replace("<br>", " ")
    h = (f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><div class="top"><img src="{I}logo.png"><br>'
         f'<span class="tag{" b" if tag.startswith("BONUS") else ""}">{tag}</span></div><div class="obj">{obj}</div><h1>{tit1}</h1><p>{desc}</p>')
    (out / f"carrusel_{n:02d}.html").write_text(h.replace('src="../../', 'src="../../').replace("../../img/", "../../img/"), encoding="utf-8")
print("ok")
