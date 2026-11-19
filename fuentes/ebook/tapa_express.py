"""Tapa del bonus "Rutinas express de 15 minutos" con el mismo diseño que casa, gimnasio y pausa activa.
Uso: cd fuentes/ebook && python3 tapa_express.py && node tapa_express.js → ../landing/mockups/pack/tapa_express.png"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "design-system"))
from design_system import css as ds_css
body = '''<section class="page p-cover" id="portada"><div class="body">
<div class="cv3 pausa">
  <div class="c3-in">
    <img class="c3-logo" src="img/logo_renova.png" alt="RENOVA">
    <span class="c3-pill">BONUS · MÉTODO RENOVA</span>
    <h1 class="c3-title">RUTINAS<br>EXPRESS</h1>
    <p class="c3-claim">15 MINUTOS PARA <b><span>NO CORTAR.</span></b></p>
    <p class="c3-sub">Sesiones <b>cortas</b> de <em>cuerpo completo</em><br><span>para las <mark>semanas</mark> con <mark>poco tiempo</mark>.</span></p>
  </div>
  <div class="c3-team"><img src="img/equipo_tapa.png" alt="Equipo RENOVA"></div>
</div></div></section>'''
css = ds_css(HERE) + "\n" + open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
open(os.path.join(HERE, "tapa_express.html"), "w", encoding="utf-8").write(
    f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head><body class="grande">{body}</body></html>')
print("ok")
