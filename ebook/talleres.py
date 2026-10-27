# -*- coding: utf-8 -*-
"""Ebook "Talleres RENOVA" (upsell): 3 hojas con el mismo diseño que los otros ebooks.

  1. Portada.
  2. Los talleres: quién los da (foto, nombre, profesión), qué se dicta y botón para verlos.
  3. CTA: rutinas personalizadas y plan integral, con link al WhatsApp de Nacho.

  python3 talleres.py && node export.js talleres   → Ebook_Talleres_RENOVA.pdf

Para completar: en TALLERES cargá el nombre y la foto de cada profesional
(dejá foto="" mientras no la tengas y se ve el recuadro "FOTO").
"""
import html, os

LINKS = {
    "wa_plan": "https://wa.link/hewha8",   # WhatsApp de Nacho: rutinas personalizadas y plan integral
}

TALLERES = [
    dict(titulo="Organizar la heladera",
         profe="[Nombre y apellido]", rol="Nutricionista del equipo RENOVA",
         foto="",
         link="https://youtu.be/bLRL_0--zwU",
         que="Cómo guardar, porcionar y ordenar tu heladera para tener siempre opciones listas y sanas a mano.",
         temas=["Qué comprar y cómo guardarlo", "Porciones listas para toda la semana", "El orden que te ahorra tiempo y tentaciones"]),
    dict(titulo="Gestión de la ansiedad",
         profe="[Nombre y apellido]", rol="Psicólogo del equipo RENOVA",
         foto="",
         link="https://youtu.be/t6jTfVukNa4",
         que="Herramientas para reconocer la ansiedad y manejarla en el día a día, sin que maneje tus comidas.",
         temas=["Hambre real o hambre emocional", "Qué hacer cuando aparece la ansiedad", "Rutinas simples que te ordenan"]),
]

esc = lambda s: html.escape(s, quote=True)
ICON_ARROW = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ICON_PLAY = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5l11 7-11 7z"/></svg>'
ICON_CHECK = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
BRAND = "TALLERES · <b>RENOVA</b>"

def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{ICON_CHECK}<span>{i}</span></li>" for i in items) + "</ul>"

def taller(t):
    foto = (f'<img src="{esc(t["foto"])}" alt="{esc(t["profe"])}">' if t["foto"]
            else '<div class="tl-ph">FOTO</div>')
    return f'''<div class="tl-card">
  <div class="tl-who">{foto}<div><b>{t["profe"]}</b><span>{t["rol"]}</span></div></div>
  <div class="tl-tx">
    <span class="wtag">TALLER</span>
    <h2>{t["titulo"]}</h2>
    <p>{t["que"]}</p>
    {checks(t["temas"])}
    <a class="btn tbtn" href="{esc(t["link"])}">{ICON_PLAY} VER TALLER</a>
  </div>
</div>'''

PAGES = [
    ("portada", "p-cover", False, f'''
<div class="cv2 tl-cover">
  <div class="c2-top">
    <img class="c2-logo" src="img/logo_renova.png" alt="RENOVA">
    <span class="c2-kick">ACCESO A LOS TALLERES · EQUIPO RENOVA</span>
  </div>
  <h1 class="c2-title">TALLERES <span class="c2-t">RENOVA.</span><br>APRENDÉ CON <span class="c2-r">EXPERTOS.</span></h1>
  <div class="c2-bar"></div>
  <p class="c2-sub">Herramientas concretas para comer mejor, manejar la ansiedad y sostener tus hábitos.</p>
  <p class="c2-desc">Talleres grabados por los profesionales del equipo RENOVA. Miralos cuando quieras, desde el celular, todas las veces que necesites.</p>
  <div class="c2-photos one">
    <figure class="c2-team"><div class="c2-img"><img src="img/equipo_cover.jpg" alt="Equipo RENOVA"></div>
      <figcaption><b>EQUIPO RENOVA</b><span>Profesionales que te acompañan en cada pilar.</span></figcaption></figure>
    <div class="c2-roles"><span>Entrenadores</span><span>Médico deportólogo</span><span>Psicólogo</span><span>Nutricionista</span></div>
  </div>
</div>'''),
    ("talleres", "p-spread", True, f'''
<span class="pill">TUS TALLERES</span>
<h1 class="h1">Quién da cada taller <span class="t">y qué vas a aprender</span></h1>
{"".join(taller(t) for t in TALLERES)}'''),
    ("plan", "p-spread", True, f'''
<div class="tl-cta">
  <span class="pill">EL SIGUIENTE PASO</span>
  <h1 class="h1 big">¿Querés un plan <span class="t">hecho a tu medida?</span></h1>
  <p class="lead">Los talleres te dan herramientas. Con el equipo RENOVA las convertís en un plan pensado para tu cuerpo, tu agenda y tu etapa hormonal.</p>
  <div class="tl-opts">
    <div class="tl-opt"><span class="wtag">OPCIÓN 1</span><h2>Rutinas personalizadas</h2>
      {checks(["Entrenamiento armado según tu nivel y tus objetivos", "Ajustes según tu evolución", "Seguimiento de tu entrenador"])}</div>
    <div class="tl-opt on"><span class="wtag">OPCIÓN 2 · LA MÁS COMPLETA</span><h2>Plan integral RENOVA</h2>
      {checks(["Entrenamiento, nutrición, psicología y medicina deportiva", "Equipo completo, con médico deportólogo", "Enfoque en tu etapa hormonal"])}</div>
  </div>
  <div class="quote dark">No necesitás hacerlo perfecto. <span class="t2">Necesitás un sistema que puedas sostener.</span></div>
  <div class="ctapanel">
    <p class="ctatitle">Escribile a Nacho</p>
    <p class="small center">Contale tu objetivo y te dice qué plan te conviene.</p>
    <a class="btn btn-big" href="{esc(LINKS["wa_plan"])}">QUIERO MI PLAN PERSONALIZADO {ICON_ARROW}</a>
  </div>
</div>'''),
]

def render():
    here = os.path.dirname(os.path.abspath(__file__))
    css = open(os.path.join(here, "style.css"), encoding="utf-8").read()
    out = []
    for pid, cls, header, body in PAGES:
        hdr = (f'<div class="hdr"><span>{BRAND}</span><span></span></div><div class="ftr"><span></span><span class="pgnum"></span></div>'
               if header else "")
        out.append(f'<section class="page {cls}" id="{pid}">{hdr}<div class="body">{body}</div></section>')
    doc = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Talleres RENOVA</title>'
           f'<style>{css}</style></head><body>' + "".join(out) + '<script src="paginate.js"></script></body></html>')
    with open(os.path.join(here, "talleres.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    print("talleres.html ·", len(PAGES), "páginas")

if __name__ == "__main__":
    render()
