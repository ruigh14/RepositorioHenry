# -*- coding: utf-8 -*-
"""Ebooks RENOVA — genera el HTML (fuente editable) que export.js pasa a PDF A4.

Dos ediciones salen de este mismo archivo:
  python3 build.py            → Programa RENOVA completo (ebook.html)
  python3 build.py entrena    → Ebook 1 "Entrená desde casa" (entrena.html):
                                plan de 8 semanas + bonus recetario, talleres y consulta.

Para editar textos: modificá este archivo y volvé a correr build.py.
Para cambiar links: completá el diccionario LINKS (dejá "" si todavía no lo tenés).
"""
import html, os, sys

EDITION = sys.argv[1] if len(sys.argv) > 1 else "completo"
if EDITION not in ("completo", "entrena"):
    sys.exit("Edición desconocida: usá 'completo' o 'entrena'")
FULL = EDITION == "completo"
ENT = EDITION == "entrena"
NE = "02" if FULL else "04"   # número del capítulo de entrenamiento en cada edición

LINKS = {
    "talleres": "https://www.nachoportillo.com/",   # reemplazar por el link directo a los talleres
    "consulta": "https://www.nachoportillo.com/",   # reemplazar por el link directo de reserva
    "renova": "https://www.nachoportillo.com/",
    "video_talleres": "",     # link del video de presentación de los talleres
    "foto_equipo": "img/equipo2.jpg",        # ruta de la foto del equipo, por ejemplo "img/equipo.jpg"
    "video_explicacion": "",  # [INSERTAR LINK DEL VIDEO EXPLICATIVO]
    "videos_calor": "",
    "videos_r1": "",
    "videos_r2": "",
    "videos_r3": "",
    "videos_elong": "",
}

def esc(s):
    return html.escape(s, quote=True)

ICON_CHECK = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
ICON_ARROW = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ICON_HAND = ('<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M22 14a8 8 0 0 1-8 8"/><path d="M18 11v-1a2 2 0 0 0-4 0"/>'
             '<path d="M14 10V9a2 2 0 0 0-4 0v1"/><path d="M10 9.5V4a2 2 0 0 0-4 0v10"/>'
             '<path d="M18 11a2 2 0 1 1 4 0v3a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-6-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.83L7 15"/></svg>')
ICON_PLAY = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5l11 7-11 7z"/></svg>'

def button(text, key, marker, big=False, light=False):
    url = LINKS.get(key, "")
    cls = "btn" + (" btn-big" if big else "") + (" btn-light" if light else "")
    if url:
        return f'<a class="{cls}" href="{esc(url)}">{text} {ICON_ARROW}</a>'
    return (f'<div class="btnwrap"><span class="{cls}">{text} {ICON_ARROW}</span>'
            f'<span class="marker">{marker}</span></div>')

def video_btn(key, label="VER VIDEOS DE ESTA RUTINA"):
    url = LINKS.get(key, "")
    if url:
        return f'<a class="vbtn" href="{esc(url)}">{ICON_PLAY} {label}</a>'
    return ""   # sin link verificado no se muestra el botón

# ------------------------------------------------------------------ PÁGINAS
PAGES = []   # (id, chapter_label, html)
TOC = []     # (title, page_id)

def page(body, chapter="", pid=None, cls="", toc=None, header=True):
    pid = pid or f"p{len(PAGES)+1}"
    PAGES.append(dict(id=pid, chapter=chapter, body=body, cls=cls, header=header))
    if toc:
        TOC.append((toc, pid))
    return pid

def eyebrow(t):
    return f'<span class="pill">{t}</span>'

def chap_head(num, title_html, lead):
    return (f'<div class="chead"><span class="cnum">{num}</span>'
            f'<h1>{title_html}</h1><p class="lead">{lead}</p></div>')

def ul(items, cls="list"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{ICON_CHECK}<span>{i}</span></li>" for i in items) + "</ul>"

def box(content, kind=""):
    return f'<div class="box {kind}">{content}</div>'

# ================================================================== PORTADA
if ENT:
    page(f'''
<div class="cv2">
  <div class="c2-top">
    <img class="c2-logo" src="img/logo_renova.png" alt="RENOVA">
    <span class="c2-kick">PLAN DE 8 SEMANAS · FUERZA EN CASA · CON VIDEOS</span>
  </div>
  <h1 class="c2-title">ENTRENÁ DESDE <span class="c2-t">CASA.</span><br>TRANSFORMÁ TU <span class="c2-r">CUERPO.</span></h1>
  <div class="c2-bar"></div>
  <p class="c2-sub">Ganá fuerza, energía y constancia en 8 semanas.</p>
  <p class="c2-desc">Un plan progresivo de 20 a 40 minutos por sesión para mujeres con poco tiempo que quieren resultados sostenibles. Incluye de bonus el recetario, dos talleres y una consulta con Nacho.</p>
  <div class="c2-photos one">
    <figure class="c2-team"><div class="c2-img"><img src="img/equipo_cover.jpg" alt="Equipo RENOVA"></div>
      <figcaption><b>EQUIPO RENOVA</b><span>Profesionales que te acompañan en cada pilar.</span></figcaption></figure>
    <div class="c2-roles"><span>Entrenadores</span><span>Médico deportólogo</span><span>Psicólogo</span><span>Nutricionista</span></div>
  </div>
</div>
''', pid="portada", cls="p-cover", header=False)

if FULL:
    page(f'''
<div class="cv2">
  <div class="c2-top">
    <img class="c2-logo" src="img/logo_renova.png" alt="RENOVA">
    <span class="c2-kick">GUÍA PRÁCTICA · ENTRENAMIENTO · ALIMENTACIÓN · DESCANSO</span>
  </div>
  <h1 class="c2-title">CAMBIA TUS <span class="c2-t">HÁBITOS.</span><br>TRANSFORMA TU <span class="c2-r">CUERPO.</span></h1>
  <div class="c2-bar"></div>
  <p class="c2-sub">Bajá de peso, ganá fuerza y recuperá energía.</p>
  <p class="c2-desc">Un sistema práctico de alimentación, entrenamiento y descanso para personas con poco tiempo que quieren resultados sostenibles.</p>
  <div class="c2-photos one">
    <figure class="c2-team"><div class="c2-img"><img src="img/equipo_cover.jpg" alt="Equipo RENOVA"></div>
      <figcaption><b>EQUIPO RENOVA</b><span>Profesionales que te acompañan en cada pilar.</span></figcaption></figure>
    <div class="c2-roles"><span>Entrenadores</span><span>Médico deportólogo</span><span>Psicólogo</span><span>Nutricionista</span></div>
  </div>
</div>
''', pid="portada", cls="p-cover", header=False)

# ================================================================== BIENVENIDA
if ENT:
    page(f'''
{eyebrow("BIENVENIDA")}
<h1 class="h1">Te damos la bienvenida a <span class="t">Entrená desde casa</span></h1>
<p class="lead">Un plan de 8 semanas para ganar fuerza en casa en una semana real: con trabajo, familia y poco tiempo libre. No es para hacerlo perfecto: es para entrenar con constancia y ver tu progreso.</p>
<h2>Qué incluye</h2>
<div class="pillars">
  <div class="pillar"><span class="pn">01</span><h3>Plan de 8 semanas</h3><p>Tres fases con un calendario semana a semana.</p></div>
  <div class="pillar"><span class="pn">02</span><h3>Rutinas con video</h3><p>Tres rutinas en bloques y una extra de zona media.</p></div>
  <div class="pillar"><span class="pn">03</span><h3>Seguimiento</h3><p>Evaluación inicial y registro de cargas.</p></div>
</div>
{box("<b>Bonus incluidos:</b> recetario con 23 recetas, dos talleres (Descanso y Organización de la heladera) y una consulta con Nacho.", "soft")}
<div class="firstweek">
  <h2>Tu primera semana</h2>
  <div class="fw">
    <div><span>1</span><b>Evaluá</b><p>Hacé la evaluación inicial del capítulo 02.</p></div>
    <div><span>2</span><b>Agendá</b><p>Elegí 2 días para la fuerza y 2 para caminar.</p></div>
    <div><span>3</span><b>Prepará</b><p>Una colchoneta, una silla firme y un peso liviano.</p></div>
    <div><span>4</span><b>Registrá</b><p>Anotá cada sesión en la planilla del capítulo 07.</p></div>
  </div>
</div>
''', chapter="Bienvenida", pid="bienvenida")

if FULL:
    page(f'''
{eyebrow("BIENVENIDA")}
<h1 class="h1">Te damos la bienvenida a <span class="t">RENOVA</span></h1>
<p class="lead">Esta guía reúne lo esencial para organizar tu entrenamiento, tu alimentación y tu descanso en una semana real: con trabajo, reuniones, familia y poco tiempo libre.</p>
<p>No es un plan para hacerlo perfecto: es un sistema para construir hábitos que puedas sostener.</p>
<h2>Tres pilares</h2>
<div class="pillars">
  <div class="pillar"><span class="pn">01</span><h3>Fuerza y actividad física</h3><p>Tres rutinas en casa y un plan semanal.</p></div>
  <div class="pillar"><span class="pn">02</span><h3>Alimentación práctica</h3><p>Menús, recetas y lista de compras.</p></div>
  <div class="pillar"><span class="pn">03</span><h3>Descanso y recuperación</h3><p>Hábitos para dormir y recuperarte mejor.</p></div>
</div>
<div class="firstweek">
  <h2>Tu primera semana</h2>
  <div class="fw">
    <div><span>1</span><b>Agendá</b><p>Elegí 2 días para la fuerza y uno para caminar.</p></div>
    <div><span>2</span><b>Elegí un menú</b><p>Tomá el menú semanal 1 y armá tu lista de compras.</p></div>
    <div><span>3</span><b>Prepará</b><p>Dejá verduras cortadas y una proteína lista para los días de más trabajo.</p></div>
    <div><span>4</span><b>Registrá</b><p>Completá la planilla del capítulo 9 al final de cada día.</p></div>
  </div>
</div>
''', chapter="Bienvenida", pid="bienvenida")

page(f'''
{eyebrow("ANTES DE EMPEZAR")}
<h1 class="h1">Esta es la base que usamos con <span class="t">decenas de clientes</span></h1>
<p class="lead">Con esta rutina como base de entrenamiento, y orden en la alimentación, acompañamos a decenas de clientes a bajar de 6 a 10 kilos de grasa en 90 días.</p>
<div class="claim">
  <div><b>6 a 10 kg</b><span>de grasa</span></div>
  <div><b>90 días</b><span>de proceso</span></div>
  <div><b>30 min</b><span>por sesión</span></div>
</div>
<p>Estos pasos básicos te van a ayudar a lograrlo si los seguís de manera consciente: entrenar fuerza, ordenar tus comidas y cuidar tu descanso, semana a semana.</p>
{box("<b>Es una guía.</b> Los resultados dependen de cada persona: tu punto de partida, tu constancia y tu situación de salud. Si necesitás un plan a tu medida, el equipo RENOVA te acompaña, con entrenadores, nutricionista, psicólogo y medicina deportiva a cargo de nuestro médico deportólogo.", "soft")}
''', chapter="Bienvenida", pid="base")

page(f'''
{eyebrow("RESULTADOS REALES")}
<h1 class="h1">Ellas ya lo <span class="t">lograron</span></h1>
<p class="lead">Personas que siguieron este método con el equipo RENOVA.</p>
<div class="res3">
  <div class="rc"><div class="rc-img two"><div><img src="img/mari_a.jpg" alt="" style="object-position:52% 50%"><span>ANTES</span></div><div><img src="img/mari_d.jpg" alt="" style="object-position:58% 50%"><span class="d">DESPUÉS</span></div></div>
    <p><b>Mari</b>Bajó 8 kg de grasa y 10 cm de cintura.</p></div>
  <div class="rc"><div class="rc-img two"><div><img src="img/moni_d.jpg" alt="" style="object-position:43% 50%"><span>ANTES</span></div><div><img src="img/moni_a.jpg" alt="" style="object-position:52% 50%"><span class="d">DESPUÉS</span></div></div>
    <p><b>Moni</b>Bajó 6 kg y logró el hábito de entrenar.</p></div>
  <div class="rc"><div class="rc-img"><img src="img/ba_romi.jpg" alt="" style="object-position:50% 45%"><span class="d">RESULTADO</span></div>
    <p><b>Romi</b>Ganó masa muscular y volvió a correr sin dolores.</p></div>
</div>
<h3>Testimonios en video</h3>
<div class="res3">
  <a class="vc" href="https://drive.google.com/file/d/148OfnqomkPfmFo5MJvyK83iUPBGzrpzh/view?usp=drive_link"><div class="vc-img"><span class="play">{ICON_PLAY}</span><span class="vc-n">Mari</span><span class="vc-t">Testimonio en video</span></div><span class="vc-btn">{ICON_PLAY} TOCÁ PARA VER</span></a>
  <a class="vc" href="https://drive.google.com/file/d/1GW01RADaj9Btfstkefd4ynRJqBtf-HTD/view?usp=drive_link"><div class="vc-img"><span class="play">{ICON_PLAY}</span><span class="vc-n">Marina</span><span class="vc-t">Testimonio en video</span></div><span class="vc-btn">{ICON_PLAY} TOCÁ PARA VER</span></a>
  <a class="vc" href="https://drive.google.com/file/d/1pLl70FqmtkZ4GdpvcbpxJJ1E0wXcHBv6/view?usp=drive_link"><div class="vc-img"><span class="play">{ICON_PLAY}</span><span class="vc-n">Sussy</span><span class="vc-t">Testimonio en video</span></div><span class="vc-btn">{ICON_PLAY} TOCÁ PARA VER</span></a>
</div>
''', chapter="Bienvenida", pid="testimonios", toc="Resultados reales")

# ================================================================== ÍNDICE (se completa al final)
page("__TOC__", chapter="Índice", pid="indice")

# ================================================================== CAP 1
if ENT:
    page(f'''
{chap_head("01", 'Cómo usar <span class="t">esta guía</span>', "Evaluá tu punto de partida, seguí el plan semana a semana y registrá lo que hacés. Con eso alcanza para arrancar.")}
<div class="cols2">
<div>
<h3>1. Hacé la evaluación inicial</h3>
<p>En 10 minutos medís tu punto de partida (capítulo 02). La repetís en la semana 4 y en la 8. Además, cada 3 semanas te pesás y medís tu cintura.</p>
<h3>2. Elegí tus días de entrenamiento</h3>
<p>Reservá 2 o 3 momentos de 30 a 40 minutos por semana, con un día libre entre sesiones de fuerza. Agendalos como una reunión.</p>
<h3>3. Seguí el plan de 8 semanas</h3>
<p>El capítulo 03 te dice qué rutinas hacer cada semana, cuántas vueltas y con qué esfuerzo. No te adelantes: la progresión está pensada para que llegues bien a la semana 8.</p>
</div>
<div>
<h3>4. Registrá tus avances</h3>
<p>Anotá en el capítulo 07 tus sesiones, las repeticiones y los pesos que usás. Es la mejor forma de ver que estás progresando.</p>
<h3>5. Si perdés una sesión</h3>
<p>Retomá en tu próximo día disponible. No hagas dos sesiones juntas.</p>
<h3>6. Si se interrumpe una semana entera</h3>
<p>Repetí la última semana que completaste antes de avanzar. No compenses con más ejercicio ni comiendo menos.</p>
</div>
</div>
''', chapter="01 · Cómo usar esta guía", pid="cap1", toc="01 · Cómo usar esta guía")

    page(f'''
{chap_head("02", 'Evaluación <span class="t">inicial</span>', "Antes de empezar, medí tu punto de partida. No es un examen: es tu referencia para ver cuánto avanzás.")}
<h2>Tres pruebas simples</h2>
<div class="steps">
  <div class="step"><span>1</span><b>Sentarse y pararse</b><p>Sentada en una silla firme, con los brazos cruzados: contá cuántas veces te parás y te sentás en 30 segundos.</p></div>
  <div class="step"><span>2</span><b>Flexiones</b><p>Contá cuántas hacés con buena técnica: contra la pared, en una mesa, con rodillas apoyadas o completas. Anotá la variante.</p></div>
  <div class="step"><span>3</span><b>Plancha</b><p>Sostené la plancha prona (o con rodillas apoyadas) con buena técnica. Anotá los segundos, hasta 60.</p></div>
</div>
<p class="small">Hacé las pruebas después de la entrada en calor, en un día sin entrenar. Si sentís dolor, frená.</p>
<h2>Mis resultados</h2>
<table class="grid-t"><thead><tr><th>Prueba</th><th>Inicio</th><th>Semana 4</th><th>Semana 8</th></tr></thead><tbody>
{"".join(f"<tr><th>{t}</th><td></td><td></td><td></td></tr>" for t in ["Sentarse y pararse (en 30 s)","Flexiones (variante: ________)","Plancha (segundos)","Energía general (1 a 5)"])}
</tbody></table>
<h2>Con qué variante empezar</h2>
<div class="tiles">
<div class="tile"><h3>Si recién empezás</h3><p>Si hiciste menos de 12 repeticiones en la silla o no llegaste a 15 segundos de plancha, empezá con la variante más fácil de cada ejercicio y sin peso.</p></div>
<div class="tile"><h3>Si ya entrenaste antes</h3><p>Si superaste esas marcas, usá la variante principal y un peso liviano desde la semana 1.</p></div>
</div>
<p class="small">Estas marcas son orientativas. Ante la duda, empezá por lo más fácil: subir un escalón es rápido; recuperarte de una molestia, no.</p>
<h2>Mi punto de partida</h2>
<div class="cbox">
{"".join(f'<div class="cb"><span class="sq"></span>{t}</div>' for t in ["Puedo entrenar fuerza 3 días por semana","Puedo entrenar fuerza 2 días por semana","Tengo colchoneta","Tengo una silla firme","Tengo peso: mancuernas, botellas o mochila","Puedo caminar 20–30 minutos 2 o 3 veces por semana"])}
</div>
''', chapter="02 · Evaluación inicial", pid="eval", toc="02 · Evaluación inicial")

    page(f'''
{eyebrow("EVALUACIÓN INICIAL")}
<h1 class="h1">Peso y <span class="t">perímetro de cintura</span></h1>
<p class="lead">Registralos al empezar y cada 3 semanas. La cintura muestra cambios que la balanza a veces no refleja.</p>
<div class="meas">
<figure><img src="img/medir_cintura.png" alt="Cómo medir el perímetro de cintura"></figure>
<div>
<h3>Cómo medir la cintura</h3>
<ol class="steps-ol">
<li>Usá una cinta métrica flexible, de costura.</li>
<li>Parate relajada, con los pies juntos y sin meter la panza.</li>
<li>Ubicá el punto medio entre la última costilla y el borde de arriba del hueso de la cadera. Suele quedar a la altura del ombligo.</li>
<li>Pasá la cinta alrededor, derecha y paralela al piso, apoyada sobre la piel sin apretar.</li>
<li>Leé la medida al final de una exhalación normal. Medí dos veces y anotá el promedio.</li>
</ol>
</div>
</div>
<h3>Cómo pesarte</h3>
{ul(["Siempre con la misma balanza y el mismo día de la semana.", "A la mañana, en ayunas y después de ir al baño, con poca ropa."])}
<table class="grid-t meas-t"><thead><tr><th></th><th>Inicio</th><th>Semana 3</th><th>Semana 6</th><th>Semana 8</th></tr></thead><tbody>
{"".join(f"<tr><th>{t}</th><td></td><td></td><td></td><td></td></tr>" for t in ["Fecha","Peso (kg)","Cintura (cm)"])}
</tbody></table>
<p class="small">El peso cambia de un día a otro por los líquidos, la sal o el ciclo. Mirá la tendencia entre una medición y otra, no un número aislado.</p>
''', chapter="02 · Evaluación inicial", pid="medidas")

if FULL:
    page(f'''
{chap_head("01", 'Cómo usar <span class="t">esta guía</span>', "Definí cuándo entrenar, qué comer y qué registrar. Con eso alcanza para arrancar.")}
<div class="cols2">
<div>
<h3>1. Elegí tus días de entrenamiento</h3>
<p>Reservá 2 o 3 momentos de 30 a 40 minutos por semana, con un día libre entre sesiones de fuerza. Agendalos como una reunión.</p>
<h3>2. Organizá las comidas con anticipación</h3>
<p>Elegí un menú, hacé las compras y dejá algo preparado: verduras cortadas, una legumbre cocida, una proteína lista.</p>
<h3>3. Poné objetivos de proceso</h3>
<p>Definí acciones que dependen de vos: por ejemplo, 2 sesiones de fuerza esta semana.</p>
</div>
<div>
<h3>4. Registrá tus avances</h3>
<p>Usá la planilla del capítulo 9: marcá lo que hiciste y anotá tu energía.</p>
<h3>5. Si perdés una sesión</h3>
<p>Retomá en tu próximo día disponible. No hagas dos sesiones juntas.</p>
<h3>6. Si se interrumpe una semana entera</h3>
<p>Volvé con una semana liviana (2 vueltas, una rutina) y después seguí con tu plan. No compenses con más ejercicio ni comiendo menos.</p>
{box('<b>Importante.</b> Esta guía es orientativa. Si tenés una condición médica, una lesión o estás embarazada, consultá a un profesional antes de empezar.', "note")}
</div>
</div>
''', chapter="01 · Cómo usar esta guía", pid="cap1", toc="01 · Cómo usar esta guía")

# ================================================================== CAP 2 ENTRENAMIENTO
page(f'''
{chap_head(NE, 'Entrenamiento de <span class="t">fuerza en casa</span>', "Tres rutinas de cuerpo completo, de bajo impacto y con variantes, para empezar a ganar fuerza sin gimnasio.")}
<h2>Por qué entrenar fuerza</h2>
<p>El entrenamiento de fuerza ayuda a mantener y desarrollar masa muscular, cuidar la salud ósea y sostener la capacidad para las tareas del día a día. A partir de los 35–40 años la masa muscular tiende a disminuir si no se estimula, por eso la fuerza es la base de esta guía.</p>
<h2>Cómo está organizado</h2>
<div class="steps steps4">
  <div class="step"><span>1</span><b>Entrada en calor</b><p>5 a 10 min</p></div>
  <div class="step"><span>2</span><b>Bloque 1</b><p>4 ejercicios</p></div>
  <div class="step"><span>3</span><b>Bloque 2</b><p>4 ejercicios</p></div>
  <div class="step"><span>4</span><b>Elongación</b><p>5 min</p></div>
</div>
<h2>Qué necesitás y cuánto dura</h2>
<p>Una colchoneta, una silla firme y un peso liviano (mancuernas, botellas de agua o una mochila con carga); si no tenés peso, usá tu propio cuerpo. Una sesión completa lleva entre 30 y 40 minutos.</p>
{box('<b>Antes de empezar.</b> Si sentís dolor articular, mareos, falta de aire inusual o dolor en el pecho, frená el ejercicio. Si tenés una lesión, dolor persistente o una condición médica, consultá con un profesional antes de hacer los ejercicios que puedan agravarla.', "note")}
''', chapter=NE + " · Entrenamiento", pid="cap2", toc=NE + " · Entrenamiento")

page(f'''
{eyebrow("CÓMO HACER CADA RUTINA")}
<h1 class="h1">Series, repeticiones y <span class="t">pausas</span></h1>
<h3>Repetición</h3><p>Es un movimiento completo. Por ejemplo, bajar y subir en una sentadilla.</p>
<h3>Serie</h3><p>Es un conjunto de repeticiones. “3 series de 10–12” significa hacer el ejercicio 10 a 12 veces, tres veces.</p>
<h3>Formato en bloques</h3><p>Cada rutina tiene entrada en calor, bloque 1, bloque 2 y elongación. Dentro de cada bloque, hacé los 4 ejercicios uno detrás de otro: eso es una vuelta. Completá las vueltas del bloque 1, descansá 2 minutos y pasá al bloque 2.</p>
<h3>Pausas</h3>
{ul(["Entre ejercicios: 30 a 60 segundos.", "Entre vueltas: 1 minuto.", "Entre el bloque 1 y el bloque 2: 2 minutos.", "Si te falta el aire o perdés la técnica, alargá la pausa."])}
<h3>Ejercicios por tiempo</h3><p>Las planchas y algunos ejercicios dinámicos se hacen por segundos (por ejemplo, 15–20 s) en lugar de repeticiones.</p>
<h3>Videos de cada ejercicio</h3><p>En cada ejercicio vas a encontrar el botón <span class="vbtn-sm inline">{ICON_PLAY} VER VIDEO</span>. Tocalo para ver la demostración. Las primeras veces, mirate en un espejo o filmate con el celular para revisar la técnica.</p>
''', chapter=NE + " · Entrenamiento", pid="cap2b")

page(f'''
{eyebrow("CÓMO HACER CADA RUTINA")}
<h1 class="h1">Dificultad y <span class="t">progresión</span></h1>
<h3>Cómo elegir la dificultad</h3>
<p>Al terminar cada serie deberías sentir que podrías hacer 2 o 3 repeticiones más con buena técnica. En una escala de esfuerzo de 1 a 10, apuntá a un 7. Si terminás muy holgada, usá la variante más difícil o sumá peso; si no llegás a las repeticiones, usá la variante más simple.</p>
<h3>Cómo progresar</h3>
{ul((["<b>Semana 1:</b> 2 vueltas, aprendiendo la técnica.",
     "<b>Semana 2 en adelante:</b> 3 vueltas."] if FULL else
    ['<b>Seguí el plan de 8 semanas</b> (<a href="#plan8">capítulo 03</a>): ahí está cuántas vueltas y qué esfuerzo corresponde a cada semana.']) + [
     "Cuando completes las 12 repeticiones con facilidad, sumá peso o pasá a una variante más exigente.",
     "En los ejercicios por tiempo, sumá 5 segundos por semana hasta llegar a 30–40 s."])}
<h3>Si tenés poco tiempo: versión de 20 minutos</h3>
{ul(["Entrada en calor: 1 vuelta.", "Rutina del día: 2 vueltas.", "Elongación: 3 o 4 posturas."])}
<h3>Escala de esfuerzo</h3>
<div class="rpe">
  <div><b>1–4</b><span>Muy fácil</span><p>Podrías seguir mucho tiempo.</p></div>
  <div class="on"><b>6–8</b><span>Zona objetivo</span><p>Te quedan 2 o 3 repeticiones.</p></div>
  <div><b>9–10</b><span>Máximo</span><p>No podrías hacer una más.</p></div>
</div>
''', chapter=NE + " · Entrenamiento", pid="cap2c")

# ---- tarjetas de ejercicios
# VIDEOS: link de cada ejercicio (por nombre), tomados de la biblioteca de Harbiz de Nacho.
# Vacío = botón visible sin link.
VIDEOS = {
 # entrada en calor
 "Movilidad de brazos": "https://youtu.be/2LWFYoBjS5I",
 "Abducción de pierna": "https://youtu.be/4C0pyUW9DaQ",
 "Sentadilla lateral": "https://www.youtube.com/watch?v=AhPJmY4v3Z4",
 "Movilidad de cadera acostada": "https://youtu.be/9ayi-DrA98o",
 "Elevación de cadera": "https://youtu.be/YopfscyxtK0",
 "Bird dog": "https://youtu.be/kyNrWqz1iqs",
 # rutina 1
 "Sentadilla en copa": "https://youtu.be/SYu43ORBDiM",
 "Estocada split": "https://youtu.be/s7ewEzHwXgQ",
 "Flexiones de brazo": "https://youtu.be/mBv-_kaIzME",
 "Puente a una pierna": "https://youtu.be/xVvVhmIp7sM",
 "Fondo en banco": "https://youtu.be/FqLq6-WRoqw",
 "Jumping jack": "https://youtu.be/t-warTAW-QY",
 "Plancha prona": "https://youtu.be/nd0qbgESlao",
 "Crunch abdominal": "https://youtu.be/dCXP5MiZQNc",
 # rutina 2
 "Subida al banco": "https://youtu.be/CMlvRdB7dIk",
 "Mountain climber": "https://youtu.be/k9_dNW743ng",
 "Sentadilla con press de hombros": "https://youtu.be/2ZDHMjr2pkM",
 "Abdominales bicicleta": "https://youtu.be/KURCyY_ctnI",
 "Sentadilla búlgara": "https://youtu.be/rf1CvaGe5JU",
 "Skipping en el lugar": "https://youtu.be/PyuFTClaUXE",
 "Plancha alta dinámica": "https://youtu.be/LiKEC5Cbxrs",
 "Remo inclinado": "https://youtu.be/6a1emLHfGYg",
 # rutina 3
 "Estocada cruzada": "https://youtu.be/5yYgxASNwZ8",          # catálogo Harbiz ("Zancada cruzada alterna sin peso")
 "Plancha lateral dinámica": "https://www.youtube.com/watch?v=WtRo2-kOJ7A",
 "Sentadilla sumo": "https://youtu.be/Ro3dhcOXiYw",
 "Elevaciones de pierna": "https://www.youtube.com/watch?v=ozyvbTK9E5U",   # catálogo Harbiz
 "Peso muerto a una pierna": "https://youtu.be/0KFZn0giQJQ",
 "Bíceps con peso": "https://youtu.be/ToxLEnNgKXA",
 "Plancha oso": "https://www.youtube.com/shorts/poQj12MCTJQ",  # no está en Harbiz: link del plan en Canva
 "Vuelo posterior con peso": "https://youtu.be/Stpq0KwR5iQ",
 # elongación
 "Isquiotibiales a una pierna": "https://youtu.be/50BsrPx3-mU",
 "Abdominales": "https://youtu.be/OZX2s2yAIU4",
 "Espalda baja": "https://youtu.be/gswS7KoAjMc",
 "Aductores": "https://youtu.be/RYs_nKnDzx4",
 "Espalda e isquiotibiales": "https://youtu.be/7t7SIeQrmxY",
 "Pectoral en pared": "https://youtu.be/5reQDGL1cA4",
 "Hombros": "https://youtu.be/ecGClH49zxk",
 "Cuello": "https://youtu.be/3kWdTdnKvVw",
 # pausa activa en el trabajo
 "Estiramiento de cuello": "https://youtu.be/3kWdTdnKvVw",
 "Círculos de hombros": "https://youtu.be/2LWFYoBjS5I",
 "Rotación de tronco sentada": "https://youtu.be/8ZhHlY4Aq_Y",
 "Sentadilla a la silla": "https://www.youtube.com/watch?v=hd5OuSxMgcE",
 "Elevación de talones": "https://youtu.be/XEmxAHBzMTg",
 "Estiramiento de pecho en pared": "https://youtu.be/5reQDGL1cA4",
 # extra: zona media
 "Bicho muerto alternado": "https://youtu.be/kgG0lb4XfMQ",
 "Plancha": "https://www.youtube.com/watch?v=qVnZtJGK4zY",
 "Plancha lateral": "https://youtu.be/bxQgU1eK4dc",
 "Abdominales cruzados": "https://youtu.be/25NgueIPUfo",
}

def ex_card(img, name, dose, how, easy=None, easy_label="Más fácil", row=False):
    e = f'<p class="easy"><b>{easy_label}:</b> {easy}</p>' if easy else ""
    url = VIDEOS.get(name, "")
    vb = (f'<a class="vbtn-sm" href="{esc(url)}">{ICON_PLAY} VER VIDEO</a>' if url
          else f'<span class="vbtn-sm">{ICON_PLAY} VER VIDEO</span>')
    if row:   # tarjeta en fila: el botón de video va junto al título
        return (f'<div class="ex exrow"><div class="exim"><img src="img/{img}" alt=""></div>'
                f'<div class="extx"><div class="exh"><h4>{name}</h4><span class="dose">{dose}</span>{vb}</div>'
                f'<p>{how}</p>{e}</div></div>')
    return (f'<div class="ex"><div class="exim"><img src="img/{img}" alt=""></div>'
            f'<div class="extx"><div class="exh"><h4>{name}</h4><span class="dose">{dose}</span></div>'
            f'<p>{how}</p>{e}{vb}</div></div>')

def warm_card(img, name, dose):
    url = VIDEOS.get(name, "")
    vb = (f'<a class="vbtn-sm" href="{esc(url)}">{ICON_PLAY} VIDEO</a>' if url
          else f'<span class="vbtn-sm">{ICON_PLAY} VIDEO</span>')
    return (f'<div class="wc"><div class="wcim"><img src="img/{img}" alt=""></div>'
            f'<b>{name}</b><span class="dose">{dose}</span>{vb}</div>')

def block_head(label, info):
    return f'<div class="blk"><span>{label}</span><p>{info}</p></div>'

def params(items):
    return '<div class="params">' + "".join(f'<div><span>{k}</span><b>{v}</b></div>' for k, v in items) + '</div>'

def routine(eyebrow_t, title_html, prm, note, cards, end_box, pid):
    page(f"""
{eyebrow(eyebrow_t)}
<h1 class="h1">{title_html}</h1>
{params(prm)}
<p class="small">{note}</p>
{"".join(cards)}
{end_box}
""", chapter=NE + " · Entrenamiento", pid=pid)

CALOR = [
 ("calor_1.png","Movilidad de brazos","10–12","De pie, llevá los brazos hacia arriba y luego en círculos amplios, hacia adelante y hacia atrás. Podés sostener un bastón o un palo de escoba.","solo hacia adelante y con menor amplitud."),
 ("calor_2.png","Abducción de pierna","10–12 por lado","Apoyada en el respaldo de una silla, separá una pierna hacia el costado sin inclinar el tronco y volvé con control.","menor apertura, sin apuro."),
 ("calor_3.png","Sentadilla lateral","10–12 por lado","Con los pies bien separados, llevá el peso a una pierna flexionando la rodilla y dejá la otra estirada. Volvé al centro y cambiá de lado.","menos profundidad y con apoyo en una silla."),
 ("calor_4.png","Movilidad de cadera acostada","10–12 por lado","Acostada de costado con las rodillas flexionadas, abrí y cerrá la rodilla de arriba sin despegar los pies.","menor apertura de la rodilla."),
 ("calor_5.png","Elevación de cadera","10–12","Boca arriba con las rodillas flexionadas, apretá los glúteos y elevá la cadera hasta alinear rodillas, cadera y hombros. Bajá lento.","subí menos la cadera."),
 ("calor_6.png","Bird dog","10–12 por lado","En cuatro apoyos, estirá un brazo y la pierna contraria, sostené un segundo y volvé. Mantené la espalda quieta.","mové solo el brazo o solo la pierna."),
]

RUT = {
"1": dict(title="Rutina 1", note="Las planchas: 15–20 s.", ex=[
 ("r1_1.png","Sentadilla en copa","10–12","Pies al ancho de los hombros y el peso sostenido contra el pecho. Llevá la cadera hacia atrás y abajo con el pecho alto; subí empujando el piso.","sentadilla hacia una silla: tocá el asiento y subí, sin peso."),
 ("r1_2.png","Estocada split","10–12 por pierna","Un pie adelante y otro atrás. Bajá en vertical hasta que ambas rodillas formen un ángulo cercano a 90° y volvé a subir.","menos recorrido y apoyando una mano en una pared o silla."),
 ("r1_3.png","Flexiones de brazo","8–12","Manos debajo de los hombros y el cuerpo alineado. Bajá el pecho hacia el piso con los codos a unos 45° y empujá para subir.","con las rodillas apoyadas o con las manos sobre una mesa firme o una pared."),
 ("r1_4.png","Puente a una pierna","10–12 por lado","Boca arriba, un pie apoyado y la otra pierna elevada. Subí la cadera apretando el glúteo y bajá lento.","puente con los dos pies apoyados."),
 ("r1_5.png","Fondo en banco","8–12","Manos en el borde de una silla firme y los pies en el piso. Flexioná los codos hacia atrás hasta unos 90° y subí. Evitá si te molestan los hombros.","rodillas flexionadas y pies cerca de la silla, con menos recorrido."),
 ("r1_6.png","Jumping jack","10–12","Saltá abriendo piernas y brazos a la vez y volvé a cerrar. Aterrizá suave.","sin salto: paso lateral alternado, abriendo los brazos."),
 ("r1_7.png","Plancha prona","15–20 s","Antebrazos y puntas de pie apoyados, el cuerpo en línea recta. Apretá abdomen y glúteos sin dejar caer la cadera.","con las rodillas apoyadas."),
 ("r1_8.png","Crunch abdominal","10–12","Boca arriba con las rodillas flexionadas, despegá los hombros del piso llevando las costillas hacia la cadera. Sin tirar del cuello.","manos sobre los muslos y menor recorrido."),
]),
"2": dict(title="Rutina 2", note="Mountain climber, skipping y plancha: 15–20 s.", ex=[
 ("r2_1.png","Subida al banco","10–12 por pierna","Apoyá un pie completo en un escalón o banco firme y subí empujando con esa pierna. Bajá con control.","escalón más bajo y sosteniéndote de una pared."),
 ("r2_2.png","Mountain climber","15–20 s","En plancha alta, llevá las rodillas hacia el pecho de forma alternada, manteniendo la cadera estable.","lento, sin saltar, o con las manos sobre una silla firme."),
 ("r2_3.png","Sentadilla con press de hombros","10–12","Con un peso en cada mano a la altura de los hombros, hacé una sentadilla y, al subir, empujá los pesos por encima de la cabeza.","sin peso o con botellas chicas; podés separar los dos movimientos."),
 ("r2_4.png","Abdominales bicicleta","10–12 por lado","Boca arriba, acercá un codo a la rodilla contraria mientras estirás la otra pierna. Alterná sin apuro.","con los pies apoyados en el piso, alternando solo la rotación."),
 ("r2_5.png","Sentadilla búlgara","10–12 por pierna","Pie de atrás apoyado sobre una silla. Bajá en vertical flexionando la pierna de adelante y subí empujando con el talón.","estocada split con los dos pies en el piso."),
 ("r2_6.png","Skipping en el lugar","15–20 s","Corré en el lugar elevando las rodillas y acompañando con los brazos.","marcha en el lugar elevando las rodillas, sin salto."),
 ("r2_7.png","Plancha alta dinámica","15–20 s","Desde plancha alta, tocá el hombro contrario con una mano y alterná, sin rotar la cadera.","con las rodillas apoyadas."),
 ("r2_8.png","Remo inclinado","10–12 por brazo","Una mano y una rodilla sobre un banco o silla. Con la espalda recta, tirá del peso hacia la cadera y bajá lento.","peso más liviano o con una botella."),
]),
"3": dict(title="Rutina 3", note="Elevaciones de pierna y plancha oso: 15–20 s.", ex=[
 ("r3_1.png","Estocada cruzada","10–12 por pierna","Llevá una pierna en diagonal hacia atrás, por detrás de la otra, y bajá con el tronco erguido. Volvé al centro.","menos recorrido y con apoyo en una silla."),
 ("r3_2.png","Plancha lateral dinámica","10–12 por lado","Apoyada sobre un antebrazo, con el cuerpo de costado, bajá la cadera hacia el piso y subila apretando el lateral del abdomen.","con las rodillas flexionadas y apoyadas."),
 ("r3_3.png","Sentadilla sumo","10–12","Pies bien separados y puntas hacia afuera. Bajá con la espalda recta y las rodillas en dirección a los pies; subí apretando glúteos.","menor profundidad o hacia una silla."),
 ("r3_4.png","Elevaciones de pierna","15–20 s","Boca arriba, con la zona lumbar apoyada, subí y bajá las piernas de forma controlada.","con las rodillas flexionadas o una pierna por vez."),
 ("r3_5.png","Peso muerto a una pierna","10–12 por pierna","Inclinate hacia adelante desde la cadera mientras la pierna de atrás se eleva, con la espalda recta. Volvé apretando el glúteo.","punta del pie de atrás apoyada en el piso y una mano en la pared."),
 ("r3_6.png","Bíceps con peso","10–12","De pie, codos pegados al cuerpo. Flexioná los codos llevando el peso hacia los hombros y bajá lento.","peso más liviano."),
 ("r3_7.png","Plancha oso","15–20 s","En cuatro apoyos, elevá las rodillas unos centímetros del piso y sostené con la espalda plana.","sostené menos tiempo y descansá en el medio."),
 ("r3_8.png","Vuelo posterior con peso","10–12","Inclinada hacia adelante con la espalda recta, abrí los brazos hacia los costados llevando los omóplatos hacia atrás.","sin peso o con botellas chicas."),
]),
}
VUELTAS = "3 vueltas (2 en la semana 1)" if FULL else "2 o 3 vueltas, según tu semana del plan"
for k, r in RUT.items():
    page(f"""
{eyebrow("RUTINA EN CASA")}
<h1 class="h1">{r["title"]}: <span class="t">cuerpo completo</span></h1>
{block_head("ENTRADA EN CALOR", "1 o 2 vueltas · 10–12 rep. · 20–30 s de pausa")}
{"".join(ex_card(*c[:4], row=True) for c in CALOR)}
""", chapter=NE + " · Entrenamiento", pid=f"rutina{k}")
    page(f"""
<h2 class="bh">{r["title"]} · <span class="t">Bloque 1</span></h2>
{block_head("BLOQUE 1", VUELTAS + " · 30–60 s entre ejercicios · 1 min entre vueltas · " + r["note"])}
{"".join(ex_card(*e, row=True) for e in r["ex"][:4])}
<p class="small"><b>Al terminar las vueltas</b>, descansá 2 minutos y pasá al bloque 2.</p>
""", chapter=NE + " · Entrenamiento", pid=f"rutina{k}b1")
    page(f"""
<h2 class="bh">{r["title"]} · <span class="t">Bloque 2</span></h2>
{block_head("BLOQUE 2", VUELTAS + " · 30–60 s entre ejercicios · 1 min entre vueltas · " + r["note"])}
{"".join(ex_card(*e, row=True) for e in r["ex"][4:])}
<p class="small"><b>Al terminar el bloque 2</b>, hacé la <a href="#elong">rutina de elongación</a> (página <span class="pref" data-ref="elong"></span>).</p>
""", chapter=NE + " · Entrenamiento", pid=f"rutina{k}b2")

ELONG = [
 ("elong_1.png","Isquiotibiales a una pierna","Sentada, una pierna estirada y la otra flexionada. Inclinate hacia adelante desde la cadera, con la espalda larga.","flexioná un poco la rodilla de la pierna estirada."),
 ("elong_2.png","Abdominales","Boca abajo, apoyá las manos y elevá suavemente el pecho, sin forzar la zona lumbar.","apoyá los antebrazos en el piso."),
 ("elong_3.png","Espalda baja","Boca arriba, llevá una rodilla hacia el pecho y sostenela con las manos. Cambiá de lado.","sostené por detrás del muslo."),
 ("elong_4.png","Aductores","Sentada, juntá las plantas de los pies y dejá caer las rodillas hacia los costados.","alejá los pies del cuerpo."),
 ("elong_5.png","Espalda e isquiotibiales","Manos y pies en el piso, llevá la cadera hacia arriba y atrás formando una V invertida. Podés flexionar las rodillas.","rodillas flexionadas o manos sobre una silla."),
 ("elong_6.png","Pectoral en pared","Apoyá el antebrazo en una pared y girá suavemente el cuerpo hacia el lado contrario.","apoyá el brazo más bajo."),
 ("elong_7.png","Hombros","Cruzá un brazo por delante del pecho y sostenelo con el otro, sin elevar el hombro.","menos presión con el brazo que sostiene."),
 ("elong_8.png","Cuello","Incliná la cabeza hacia un lado, ayudándote suavemente con la mano. Sin tirones.","sin ayudarte con la mano."),
]
page(f"""
{eyebrow("AL TERMINAR CADA RUTINA")}
<h1 class="h1">Rutina de <span class="t">elongación</span></h1>
{params([("Vueltas","1 a 2"),("Cada postura","15–30 s"),("Intensidad","Suave, sin dolor"),("Duración","5–8 min")])}
<p class="small">Sostené cada postura sin rebotes y respirando con calma.</p>
{"".join(ex_card(i, n, "15–30 s", h, e, row=True) for i, n, h, e in ELONG[:4])}
""", chapter=NE + " · Entrenamiento", pid="elong")
page(f"""
<h2 class="bh">Elongación · <span class="t">continuación</span></h2>
{"".join(ex_card(i, n, "15–30 s", h, e, row=True) for i, n, h, e in ELONG[4:])}
<p class="small"><b>¡Bien hecho!</b> Anotá la sesión en tu planilla de registro.</p>
""", chapter=NE + " · Entrenamiento", pid="elong2")

# ================================================================== CAP 3 ORGANIZACIÓN SEMANAL
def cal_row(label, days):
    cells = ""
    for d in days:
        if d in ("1","2","3"):
            cells += f'<td><span class="chip c{d}">R{d}</span></td>'
        elif d == "A":
            cells += '<td><span class="chip ca">A</span></td>'
        elif d == "D":
            cells += '<td><span class="chip cd">Descanso</span></td>'
        else:
            cells += '<td><span class="chip ce">Libre</span></td>'
    return f"<tr><th>{label}</th>{cells}</tr>"

if FULL:
    page(f'''
{chap_head("03", 'Organización <span class="t">semanal</span>', "Una propuesta progresiva de cuatro semanas que combina fuerza, actividad aeróbica y descanso. Tomala como guía y movela según tu agenda.")}
<table class="cal">
<thead><tr><th></th><th>Lun</th><th>Mar</th><th>Mié</th><th>Jue</th><th>Vie</th><th>Sáb</th><th>Dom</th></tr></thead>
<tbody>
{cal_row("Semana 1", ["1","-","2","-","-","A","D"])}
{cal_row("Semana 2", ["1","A","2","-","3","A","D"])}
{cal_row("Semana 3", ["1","A","2","A","3","-","D"])}
{cal_row("Semana 4", ["1","A","2","A","3","A","D"])}
</tbody></table>
<div class="legend"><span><span class="chip c1">R1</span> Rutina 1</span><span><span class="chip c2">R2</span> Rutina 2</span><span><span class="chip c3">R3</span> Rutina 3</span><span><span class="chip ca">A</span> Actividad aeróbica 30–40 min</span></div>
<div class="cols2">
<div>
<h3>Qué cuenta como actividad aeróbica</h3>
<p>Cualquier actividad que puedas sostener de forma continua durante 30 a 40 minutos a un ritmo en el que podés hablar, pero no cantar: caminar rápido, andar en bicicleta, nadar, bailar o usar una elíptica. Elegí la que disfrutes: es la que vas a sostener.</p>
<h3>Reglas simples</h3>
{ul(["Dejá al menos un día entre dos sesiones de fuerza.", "Los días se pueden mover: lo importante es el total de la semana.", "El domingo es de descanso. Una caminata tranquila también suma.", "A partir de la semana 5, repetí la semana 4 o ajustá según tu energía."])}
</div>
</div>
''', chapter="03 · Organización semanal", pid="cap3", toc="03 · Organización semanal")

if FULL:
    page(f'''
{eyebrow("ORGANIZACIÓN SEMANAL")}
<h1 class="h1">Semanas con <span class="t">menos tiempo</span></h1>
<p class="lead">Si tu agenda no permite la propuesta completa, elegí una versión reducida. Hacer menos, pero sostenido, suma más que intentar todo y abandonar.</p>
<table class="cal">
<thead><tr><th></th><th>Lun</th><th>Mar</th><th>Mié</th><th>Jue</th><th>Vie</th><th>Sáb</th><th>Dom</th></tr></thead>
<tbody>
{cal_row("2 días", ["1","-","-","2","-","A","D"])}
{cal_row("3 días", ["1","-","2","-","3","A","D"])}
</tbody></table>
<h3>Si tenés menos tiempo</h3>
{ul(["<b>2 días de fuerza:</b> alterná Rutina 1 y Rutina 2 y sumá la 3 cuando puedas.",
     "<b>Versión de 20 minutos:</b> 1 vuelta de entrada en calor y 2 de la rutina.",
     "<b>Aeróbico en bloques:</b> 3 caminatas de 10 minutos en el día también suman.",
     "<b>Días largos sentada:</b> levantate 2 o 3 minutos cada hora."])}
{box("La OMS recomienda para adultos entre 150 y 300 minutos semanales de actividad aeróbica moderada y ejercicios de fortalecimiento al menos 2 días por semana. La semana 4 de esta propuesta se acerca a esa referencia; las primeras semanas son de adaptación.", "soft")}

''', chapter="03 · Organización semanal", pid="cap3x")

def blank_week():
    rows = ""
    for lab in ["Fuerza (R1, R2, R3)", "Aeróbico (minutos)", "Elongación"]:
        rows += f"<tr><th>{lab}</th>" + "<td></td>"*7 + "</tr>"
    return rows

if FULL:
    page(f'''
{eyebrow("PLANILLA IMPRIMIBLE")}
<h1 class="h1">Mi semana de <span class="t">entrenamiento</span></h1>
<p>Completá los días que elegís para entrenar y marcá lo que hiciste. Imprimí una planilla por semana o usala como modelo en tu agenda.</p>
{"".join(f'<h3 class="wk">Semana {n} · del ____ al ____</h3><table class="grid-t"><thead><tr><th></th><th>Lun</th><th>Mar</th><th>Mié</th><th>Jue</th><th>Vie</th><th>Sáb</th><th>Dom</th></tr></thead><tbody>{blank_week()}</tbody></table>' for n in (1,2,3))}
''', chapter="03 · Organización semanal", pid="cap3b")

# ================================================================== EBOOK 1: PLAN DE 8 SEMANAS
# Semana, fase, rutinas, vueltas, repeticiones · tiempo, pausa entre ejercicios, esfuerzo (1–10), aeróbico.
PLAN8 = [
 ("1", "Base",          "R1 · R2",         "2",          "10 · 15 s",                    "60 s",    "5–6", "2 × 20 min"),
 ("2", "Base",          "R1 · R2 · R3",    "2",          "10–12 · 15–20 s",              "60 s",    "6",   "2 × 30 min"),
 ("3", "Construcción",  "R1 · R2 · R3",    "3",          "10–12 · 20 s",                 "60 s",    "6–7", "2 × 30 min"),
 ("4", "Construcción",  "R1 · R2 · R3",    "3",          "12 · 25 s",                    "45 s",    "7",   "3 × 30 min"),
 ("5", "Construcción",  "R1 · R2 · R3",    "3",          "12 con más peso · 30 s",       "45 s",    "7–8", "3 × 30–40 min"),
 ("6", "Descarga",      "R1 · R2",         "2",          "10 · 20 s",                    "60 s",    "6",   "2 × 30 min"),
 ("7", "Consolidación", "R1 · R2 · R3",    "3",          "10–12 bajando en 3 s · 30 s",  "30–45 s", "7–8", "3 × 40 min"),
 ("8", "Consolidación", "R1 · R2 · R3",    "3 (+1 opcional)", "12 · 35–40 s",            "30–45 s", "7–8", "3 × 40 min"),
]
PLAN8_DAYS = {
 "1": ["1","A","-","2","-","A","D"],
 "2": ["1","A","2","-","3","A","D"],
 "3": ["1","A","2","-","3","A","D"],
 "4": ["1","A","2","A","3","A","D"],
 "5": ["1","A","2","A","3","A","D"],
 "6": ["1","A","-","2","-","A","D"],
 "7": ["1","A","2","A","3","A","D"],
 "8": ["1","A","2","A","3","A","D"],
}
LEGEND = '<div class="legend"><span><span class="chip c1">R1</span> Rutina 1</span><span><span class="chip c2">R2</span> Rutina 2</span><span><span class="chip c3">R3</span> Rutina 3</span><span><span class="chip ca">A</span> Actividad aeróbica</span></div>'
def plan8_table(rows):
    return ('<table class="plan8"><thead><tr><th>Sem.</th><th>Fase</th><th>Fuerza</th><th>Vueltas por bloque</th><th>Repeticiones · planchas</th><th>Pausa</th><th>Esfuerzo</th><th>Aeróbico</th></tr></thead><tbody>'
            + "".join(f'<tr class="{"dl" if f == "Descarga" else ""}"><th>{w}</th><td>{f}</td><td>{r}</td><td>{v}</td><td>{rp}</td><td>{pa}</td><td>{e}</td><td>{a}</td></tr>' for w, f, r, v, rp, pa, e, a in rows)
            + '</tbody></table>')
DAYS_HEAD = "<thead><tr><th></th><th>Lun</th><th>Mar</th><th>Mié</th><th>Jue</th><th>Vie</th><th>Sáb</th><th>Dom</th></tr></thead>"

if ENT:
    page(f'''
{chap_head("03", 'Tu plan de <span class="t">8 semanas</span>', "Tres fases para pasar de aprender la técnica a entrenar con más carga. Cada semana te dice qué hacer y con qué esfuerzo.")}
<div class="phases"><span><b>Fase 1 · Base</b> semanas 1–2</span><span><b>Fase 2 · Construcción</b> semanas 3–6</span><span><b>Fase 3 · Consolidación</b> semanas 7–8</span></div>
<h2>Semanas 1 a 4</h2>
{plan8_table(PLAN8[:4])}
<h3>Cómo progresar</h3>
{ul(["<b>Semanas 1 y 2:</b> aprendé la técnica con 2 vueltas por bloque y esfuerzo moderado. Tenés que terminar con energía.",
     "<b>Semana 3:</b> pasás a 3 vueltas por bloque, con el mismo peso. Al final de la semana, <a href=\"#medidas\">pesate y medí tu cintura</a>.",
     "<b>Semana 4:</b> bajá la pausa a 45 s y subí las planchas a 25 s. Al final de la semana, repetí la <a href=\"#eval\">evaluación inicial</a>."])}
''', chapter="03 · Plan de 8 semanas", pid="plan8", toc="03 · Plan de 8 semanas")

    page(f'''
{eyebrow("PLAN DE 8 SEMANAS")}
<h1 class="h1">Semanas 5 a 8: <span class="t">más exigencia</span></h1>
{plan8_table(PLAN8[4:])}
<h3>Cómo progresar</h3>
{ul(["<b>Semana 5:</b> sumá peso o pasá a la variante más difícil en los ejercicios donde ya llegás cómoda a 12 repeticiones.",
     "<b>Semana 6, de descarga:</b> 2 vueltas por bloque y esfuerzo 6. Recuperarte también es parte del plan. Al final de la semana, pesate y medí tu cintura.",
     "<b>Semana 7:</b> bajá en 3 segundos en cada repetición y acortá la pausa a 30–45 s.",
     "<b>Semana 8:</b> si te sentís bien, sumá una 4.ª vuelta al bloque 1. Cerrá con la evaluación final, el peso y la cintura."])}
<p class="small"><b>Pausa</b> entre ejercicios; entre vueltas, 1 minuto, y entre bloques, 2 minutos. <b>Esfuerzo</b> según la escala del capítulo {NE}.</p>
''', chapter="03 · Plan de 8 semanas", pid="plan8w2")

    page(f'''
{eyebrow("PLAN DE 8 SEMANAS")}
<h1 class="h1">Tu calendario <span class="t">semana a semana</span></h1>
<p>Una propuesta para organizar los días. Movelos según tu agenda: lo importante es el total de la semana.</p>
<table class="cal cal8">
{DAYS_HEAD}
<tbody>
{"".join(cal_row(f"Semana {w}", PLAN8_DAYS[w]) for w in PLAN8_DAYS)}
</tbody></table>
{LEGEND}
<h3>Reglas simples</h3>
{ul(["Dejá al menos un día entre dos sesiones de fuerza.",
     "Aeróbico: caminar rápido, bicicleta, nadar o bailar, a un ritmo en el que podés hablar pero no cantar.",
     "Si una semana te costó mucho (esfuerzo 9 o más, o no completaste las sesiones), repetila antes de avanzar.",
     "Si solo podés 2 días de fuerza, seguí la versión del capítulo 05."])}
''', chapter="03 · Plan de 8 semanas", pid="plan8b")

    page(f'''
{eyebrow("PLAN DE 8 SEMANAS")}
<h1 class="h1">Cómo avanzar en <span class="t">cada ejercicio</span></h1>
<p class="lead">El plan sube las vueltas y baja las pausas. Vos, además, subís de escalón en cada ejercicio cuando te resulta fácil.</p>
<div class="minplan">
<div><span>Escalón 1</span><p><b>Variante fácil.</b> La que figura como “Más fácil” en cada ejercicio.</p></div>
<div><span>Escalón 2</span><p><b>Variante principal.</b> Sin peso o con tu propio cuerpo.</p></div>
<div><span>Escalón 3</span><p><b>Con peso.</b> Mancuernas, botellas o una mochila con carga.</p></div>
<div><span>Escalón 4</span><p><b>Más peso o más lento.</b> Sumá carga o bajá en 3 segundos.</p></div>
</div>
<h3>Cuándo subir un escalón</h3>
<p>Cuando completes las 12 repeticiones en todas las vueltas con un esfuerzo de 7 o menos, dos sesiones seguidas. Subí de a un ejercicio por vez.</p>
<h3>Qué significa “bajando en 3 segundos”</h3>
<p>En la semana 7, hacé la parte de bajada de cada movimiento contando lento hasta 3 (por ejemplo, al bajar en la sentadilla) y subí a ritmo normal. Con el mismo peso, el ejercicio se vuelve más exigente.</p>
<h3>Por qué la semana 6 es más liviana</h3>
<p>Después de tres semanas de subir la exigencia, una semana de descarga ayuda a recuperarte y a llegar con energía a la fase final. No es perder tiempo: es parte del plan.</p>
{box("<b>Si algo duele</b>, volvé al escalón anterior en ese ejercicio. Molestia muscular al día siguiente es normal; dolor articular o punzante, no: frená y consultá.", "note")}
''', chapter="03 · Plan de 8 semanas", pid="plan8c")

    # ---------------------------------------------------------- CAP 5 SEMANAS CON POCO TIEMPO
    page(f'''
{chap_head("05", 'Semanas con <span class="t">poco tiempo</span>', "Si tu agenda no permite la semana completa, elegí una versión reducida. Hacer menos, pero sostenido, suma más que intentar todo y abandonar.")}
<table class="cal">
{DAYS_HEAD}
<tbody>
{cal_row("2 días", ["1","-","-","2","-","A","D"])}
{cal_row("3 días", ["1","-","2","-","3","A","D"])}
</tbody></table>
{LEGEND}
<h3>Con 2 días de fuerza</h3>
<p>Seguí las vueltas, repeticiones y esfuerzo de tu semana del plan, pero alterná las rutinas: R1 y R2 una semana, R3 y R1 la siguiente. El plan te va a llevar más de 8 semanas, y está bien.</p>
<h2>Tu plan mínimo para semanas difíciles</h2>
<div class="minplan">
<div><span>Fuerza</span><p>1 o 2 sesiones express de 15 minutos.</p></div>
<div><span>Movimiento</span><p>Caminatas de 10 minutos; 3 en el día también suman.</p></div>
<div><span>Recuperación</span><p>Mismo horario para levantarte y 30 minutos sin pantallas.</p></div>
<div><span>Registro</span><p>Un tilde por día en la planilla, aunque sea uno solo.</p></div>
</div>
<p class="small">Para los días con muy poco tiempo, usá la <a href="#express">sesión express de 15 minutos</a>.</p>
''', chapter="05 · Semanas con poco tiempo", pid="cap5e", toc="05 · Semanas con poco tiempo")

    EXPRESS = {"Sentadilla en copa", "Flexiones de brazo", "Remo inclinado", "Plancha prona"}
    exp_cards = [ex_card(e[0], e[1], "40 s", e[3], row=True) for r in RUT.values() for e in r["ex"] if e[1] in EXPRESS]
    page(f'''
<h1 class="h1">Sesión express de <span class="t">15 minutos</span></h1>
{params([("Vueltas","3"),("Trabajo","40 s por ejercicio"),("Pausa","20 s · 1 min entre vueltas"),("Duración","15 min")])}
<p class="small">Antes, 2 minutos de movilidad de brazos y sentadilla lateral. Usá la variante y el peso de tu semana del plan.</p>
{"".join(exp_cards)}
''', chapter="05 · Semanas con poco tiempo", pid="express")

    # ---------------------------------------------------------- CAP 6 ACTIVA EN EL TRABAJO
    PAUSA = [
     ("elong_8.png","Estiramiento de cuello","15 s por lado","Sentada con la espalda derecha, incliná la cabeza hacia un hombro y ayudate suavemente con la mano. Sin tirones."),
     ("calor_1.png","Círculos de hombros","10 + 10","De pie o sentada, hacé círculos amplios con los brazos: 10 hacia adelante y 10 hacia atrás."),
     ("pausa_rotacion.png","Rotación de tronco sentada","8 por lado","Sentada en el borde de la silla, con los brazos cruzados sobre el pecho, girá el tronco hacia un lado y hacia el otro sin mover la cadera."),
     ("pausa_sentadilla.png","Sentadilla a la silla","10","Parada delante de la silla, llevá la cadera hacia atrás hasta rozar el asiento y volvé a subir empujando el piso."),
     ("pausa_talones.png","Elevación de talones","15","Con una mano en el respaldo de la silla, subí a puntas de pie y bajá lento."),
     ("elong_6.png","Estiramiento de pecho en pared","20 s por lado","Apoyá el antebrazo en una pared o en el marco de una puerta y girá suavemente el cuerpo hacia el lado contrario."),
    ]
    page(f'''
{chap_head("06", 'Activa en <span class="t">el trabajo</span>', "Pasar muchas horas sentada también cuenta. Una pausa activa de 5 minutos por día y algunos hábitos simples te ayudan a moverte más, aunque no sea día de entrenamiento.")}
<h2>Rutina de pausa activa</h2>
{params([("Cuándo","1 vez al día"),("Vueltas","1 o 2"),("Dónde","En tu lugar de trabajo"),("Duración","5 minutos")])}
<p class="small">Hacé los ejercicios en orden, sin pausa entre ellos. No necesitás cambiarte de ropa: alcanza con una silla firme y una pared.</p>
{"".join(ex_card(*e) for e in PAUSA)}
''', chapter="06 · Activa en el trabajo", pid="pausa", toc="06 · Activa en el trabajo")

    TIPS_DIA = [
     ("Cada 2 horas, caminá", "Levantate y caminá 3 a 5 minutos: al baño más lejano, a buscar agua o por el pasillo."),
     ("Elongá durante el día", "Dos minutos de cuello, hombros y espalda entre una tarea y otra."),
     ("Pausa activa, 1 vez al día", "Hacé la rutina de esta página. Agendala como una reunión."),
     ("Recordatorios para tomar agua", "Una botella a la vista y una alarma cada 2 horas. Un vaso con cada pausa."),
     ("Desconectá una hora antes de dormir", "Sin pantallas ni mails de trabajo. Bajá la luz y prepará el día siguiente."),
     ("Escaleras en vez de ascensor", "Cada tramo suma. Si son muchos pisos, subí una parte y tomá el ascensor el resto."),
     ("Llamadas de pie o caminando", "Las llamadas y reuniones sin pantalla son una buena excusa para moverte."),
     ("Caminata después de almorzar", "10 minutos alcanzan y ayudan a cortar la tarde sentada."),
     ("Ordená tu puesto de trabajo", "Pantalla a la altura de los ojos, pies apoyados y la espalda contra el respaldo."),
     ("Luz natural a la mañana", "Unos minutos de sol al empezar el día te ayudan a tener más energía y a dormir mejor."),
    ]
    page(f'''
{eyebrow("ACTIVA EN EL TRABAJO")}
<h1 class="h1">10 recomendaciones <span class="t">para tu día</span></h1>
<p class="lead">No hace falta hacerlas todas desde el primer día: elegí 2 o 3, sostenelas una semana y sumá otra.</p>
<div class="tips10">
{"".join(f'<div><span>{i:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(TIPS_DIA, 1))}
</div>
''', chapter="06 · Activa en el trabajo", pid="tips10")

    # ---------------------------------------------------------- CAP 6 REGISTRO
    def week_table(n):
        return (f'<h3 class="wk">Semana {n} · del ____ al ____</h3><table class="grid-t wk8">{DAYS_HEAD}'
                f'<tbody>{blank_week()}</tbody></table>')
    page(f'''
{chap_head("07", 'Registro de <span class="t">evolución</span>', "Anotá lo que hacés para ver tu progreso. No es para calificarte: una semana con casilleros vacíos también te da información.")}
<p>Marcá en cada día la rutina que hiciste (R1, R2 o R3), los minutos de aeróbico y si elongaste. Imprimí estas planillas o usalas de modelo en tu agenda.</p>
{"".join(week_table(n) for n in range(1, 9))}
''', chapter="07 · Registro de evolución", pid="registro", toc="07 · Registro de evolución")

    LOADS = ["Sentadilla en copa","Estocada split","Flexiones de brazo","Sentadilla con press de hombros","Sentadilla búlgara","Remo inclinado","Sentadilla sumo","Peso muerto a una pierna","Bíceps con peso","Plancha prona (segundos)"]
    page(f'''
{eyebrow("REGISTRO DE EVOLUCIÓN")}
<h1 class="h1">Mis cargas y <span class="t">repeticiones</span></h1>
<p>Una vez por semana, anotá el peso y las repeticiones de la última vuelta. Por ejemplo: <b>4 kg × 12</b>. Si usaste una variante, agregá F (fácil) o P (principal).</p>
<table class="grid-t loads"><thead><tr><th>Ejercicio</th>{"".join(f"<th>S{n}</th>" for n in range(1, 9))}</tr></thead>
<tbody>{"".join(f"<tr><th>{e}</th>" + "<td></td>"*8 + "</tr>" for e in LOADS)}</tbody></table>
<h3 class="wk">Cómo me sentí</h3>
<table class="track feel"><thead><tr><th></th>{"".join(f"<th>S{n}</th>" for n in range(1, 9))}</tr></thead>
<tbody>{"".join(f"<tr><th>{t}</th>" + "<td></td>"*8 + "</tr>" for t in ["Energía general (1 a 5)","Esfuerzo promedio (1 a 10)","Cómo dormí (1 a 5)"])}</tbody></table>
''', chapter="07 · Registro de evolución", pid="cargas")

    # ---------------------------------------------------------- CAP 7 DESPUÉS DE LAS 8 SEMANAS
    page(f'''
{chap_head("08", 'Después de las <span class="t">8 semanas</span>', "Terminar el plan no es el final: es el punto de partida para seguir, ahora con más fuerza y experiencia.")}
<h2>Tres caminos para seguir</h2>
<div class="pillars">
  <div class="pillar"><span class="pn">01</span><h3>Subí la carga</h3><p>Repetí las semanas 7 y 8 con más peso o variantes más exigentes. Repetí la evaluación cada 4 semanas.</p></div>
  <div class="pillar"><span class="pn">02</span><h3>Nuevo ciclo</h3><p>Volvé a la semana 1 con el peso que usás hoy. Vas a notar que todo te cuesta menos.</p></div>
  <div class="pillar"><span class="pn">03</span><h3>Mantené</h3><p>Si tu agenda está cargada, 2 sesiones por semana alcanzan para sostener lo que ganaste.</p></div>
</div>
<div class="cols2 keep">
<div>
<h3>Cómo retomar</h3>
{ul(["Volvé en la próxima oportunidad, no “el lunes”.","Empezá con la mitad: 2 vueltas y un escalón menos.","No compenses con ejercicio extra ni comiendo menos."])}
</div>
<div>
<h3>Cuándo pedir ayuda</h3>
<p>Si no lográs sostener los cambios o tenés una lesión o condición médica, un acompañamiento personalizado te ayuda a ajustar el plan.</p>
</div>
</div>
{box("<b>El próximo paso: la alimentación.</b> Con el entrenamiento en marcha, ordenar tus comidas potencia los resultados. Empezá por las recetas del bonus y, si querés un plan a tu medida, el equipo RENOVA te acompaña.", "soft")}
''', chapter="08 · Después de las 8 semanas", pid="cap7e", toc="08 · Después de las 8 semanas")

    # ---------------------------------------------------------- EXTRA: ZONA MEDIA
    CORE = [
     ("core_bicho.png","Bicho muerto alternado","6–10 por lado","Boca arriba, brazos hacia el techo y rodillas a 90°. Estirá un brazo hacia atrás y la pierna contraria hacia adelante sin despegar la zona lumbar del piso. Volvé y cambiá de lado.",
      "<b>S1–2:</b> solo las piernas, 6 por lado. <b>S3–4:</b> brazo y pierna, 8 por lado. <b>S5–8:</b> 10 por lado, bajando lento."),
     ("r1_7.png","Plancha","15–30 s","Antebrazos debajo de los hombros y el cuerpo en línea recta. Apretá abdomen y glúteos y respirá sin aguantar el aire.",
      "<b>S1–2:</b> rodillas apoyadas, 15 s. <b>S3–4:</b> rodillas, 25 s. <b>S5–6:</b> plancha completa, 15–20 s. <b>S7–8:</b> completa, 30 s."),
     ("r3_2.png","Plancha lateral","10–25 s por lado","De costado, apoyada en un antebrazo con el codo debajo del hombro. Elevá la cadera y sostené el cuerpo alineado.",
      "<b>S1–2:</b> rodillas flexionadas, 10 s. <b>S3–4:</b> rodillas, 15 s. <b>S5–6:</b> piernas estiradas, 15 s. <b>S7–8:</b> piernas estiradas, 20–25 s."),
     ("calor_6.png","Bird dog","6–10 por lado","En cuatro apoyos, estirá un brazo y la pierna contraria sin mover la espalda. Sostené y volvé con control.",
      "<b>S1–2:</b> 6 por lado. <b>S3–4:</b> 8 por lado, sosteniendo 2 s. <b>S5–8:</b> 10 por lado, sosteniendo 3 s."),
     ("core_cruzados.png","Abdominales cruzados","6–12 por lado","Boca arriba con las rodillas flexionadas y las manos detrás de la cabeza. Despegá la espalda alta y llevá el codo hacia la rodilla contraria, sin tirar del cuello.",
      "<b>S1–2:</b> 6 por lado. <b>S3–4:</b> 8 por lado. <b>S5–8:</b> 10–12 por lado, bajando lento."),
    ]
    page(f'''
{eyebrow("EXTRA")}
<h1 class="h1">Rutina de <span class="t">zona media</span></h1>
<p class="lead">Cinco ejercicios simples para fortalecer el abdomen y la espalda baja. Pensada para nivel inicial: sin saltos y sin cargar el cuello.</p>
{params([("Cuándo","2 o 3 veces por semana"),("Vueltas","2 (3 desde la semana 5)"),("Pausa","30 s entre ejercicios"),("Duración","8–10 min")])}
<p class="small">Hacela al terminar el bloque 2, antes de elongar, o en un día de aeróbico.</p>
{"".join(ex_card(*c[:4], easy=c[4], easy_label="Cómo avanzar") for c in CORE)}
{box("<b>Regla simple para variar:</b> cada 2 semanas, sumá 5 segundos o 2 repeticiones por ejercicio. Si sentís molestia en la zona lumbar o en el cuello, volvé al paso anterior.", "soft")}
''', chapter="Extra · Zona media", pid="core", toc="Extra: Rutina de zona media")

# ================================================================== CAP 4 ALIMENTACIÓN
if FULL:
    page(f'''
{chap_head("04", 'Alimentación <span class="t">práctica</span>', "Comer bien con poco tiempo no depende de recetas complicadas, sino de tener un criterio simple y algunas opciones resueltas.")}
<div class="plate-wrap">
  <div class="plate" aria-hidden="true">
    <div class="pl-veg">½ Verduras</div><div class="pl-pro">¼ Proteína</div><div class="pl-car">¼ Carbohi&shy;dratos</div>
  </div>
  <div>
    <h2>El plato como guía</h2>
    {ul(["<b>Mitad del plato:</b> verduras crudas o cocidas, de distintos colores.",
         "<b>Un cuarto:</b> una fuente de proteína: carne vacuna, pollo, pescado, huevo, legumbres, tofu o quesos.",
         "<b>Un cuarto:</b> carbohidratos: papa, batata, arroz, fideos, pan, quinoa, legumbres o choclo.",
         "<b>Una porción de grasas de calidad:</b> aceite de oliva, palta, frutos secos o semillas.",
         "<b>Para tomar:</b> agua como bebida principal."])}
  </div>
</div>
<div class="cols2">
<div>
<h3>Proteína en cada comida</h3>
<p>Sumá proteína en cada comida: ayuda a la saciedad y, junto con la fuerza, a cuidar el músculo. Una porción de carne o pescado ocupa la palma de tu mano.</p>
<h3>Los carbohidratos no son el enemigo</h3>
<p>Son energía, también para entrenar. Elegí integrales, legumbres y frutas, y ajustá la cantidad a tu hambre.</p>
</div>
<div>
<h3>Flexibilidad, no prohibiciones</h3>
<p>No hay alimentos prohibidos. Una comida fuera del plan no arruina la semana.</p>
</div>
</div>
''', chapter="04 · Alimentación práctica", pid="cap4", toc="04 · Alimentación práctica")

if FULL:
    page(f'''
{eyebrow("ALIMENTACIÓN EN LA VIDA REAL")}
<h1 class="h1">Días de trabajo, comidas afuera y <span class="t">poco tiempo</span></h1>
<div class="cols2">
<div>
<h3>Para los días laborales</h3>
{ul(["Llevá el almuerzo resuelto desde casa: una vianda armada con el criterio del plato.",
     "Tené una opción de emergencia: atún al natural, huevos duros, legumbres en lata, pan integral, fruta.",
     "Si entre comidas pasan muchas horas, planificá una merienda con proteína: yogur, queso, frutos secos.",
     "Tené agua a mano durante la jornada."])}
<h3>Cuando comés afuera</h3>
{ul(["Buscá una opción con proteína y verduras: carnes, pescados, ensaladas completas, tartas con ensalada.",
     "Pedí salsas y aderezos aparte.",
     "Comé despacio y registrá cuándo estás satisfecha.",
     "Disfrutá sin culpa y volvé a tu organización en la comida siguiente."])}
</div>
<div>
<h3>Planificar sin complicarte</h3>
{ul(["Elegí 2 o 3 cenas que repitas durante la semana.",
     "Cociná una vez y comé dos veces: duplicá las porciones y guardá.",
     "Tené bases listas: arroz o quinoa cocidos, legumbres, verduras al horno.",
     "Combiná bases con distintas proteínas y condimentos para variar."])}
</div>
</div>
''', chapter="04 · Alimentación práctica", pid="cap4b")

if FULL:
    page(f'''
{eyebrow("ALIMENTACIÓN EN LA VIDA REAL")}
<h1 class="h1">Cambios de etapa y un <span class="t">día organizado</span></h1>
<h3>Perimenopausia, menopausia y metabolismo</h3>
<p>En la perimenopausia y la menopausia pueden aparecer cambios en la composición corporal, el sueño y la energía. Los principios de esta guía (fuerza, proteína suficiente, alimentación variada y descanso) siguen siendo una base útil. Sin embargo, no todos los cambios de peso o de energía se explican por las hormonas, y síntomas como cansancio persistente, cambios de peso sin causa aparente o alteraciones del ciclo merecen una consulta médica, por ejemplo para evaluar la tiroides u otras causas.</p>
<h2>Ejemplo de un día laboral organizado</h2>
<div class="dayex">
  <div><span>Desayuno en casa</span><b>Tostada integral con queso fresco y fruta + infusión</b></div>
  <div><span>Vianda del almuerzo</span><b>Ensalada tibia de vegetales, garbanzos y pollo (preparada la noche anterior)</b></div>
  <div><span>Merienda en la oficina</span><b>Yogur natural con un puñado de frutos secos</b></div>
  <div><span>Cena rápida</span><b>Omelette con verduras salteadas y una porción de arroz cocido del fin de semana</b></div>
</div>
<h3>Cantidades orientativas</h3>
<p>Los menús de esta guía no indican cantidades porque las necesidades cambian según el tamaño corporal, la actividad, la edad y los objetivos. Usá el plato y tu hambre como referencia. Si necesitás un plan con cantidades, consultá con un profesional de la nutrición.</p>
''', chapter="04 · Alimentación práctica", pid="cap4c")

# ================================================================== CAP 5 MENÚS
MENUS = {
"Menú semanal 1": [
 ("Lun","Tostada integral con queso fresco + fruta + infusión","Pechuga de pollo con vegetales al horno (calabaza, zanahoria, zapallito, berenjena)","Tostada con huevo y tomate + infusión","Wok de verduras de 3 colores, arroz integral y trozos de pollo"),
 ("Mar","Yogur con cereales sin azúcar, quinoa pop y banana + infusión","Milanesa de carne o pollo con ensalada de tomate, zanahoria, repollo y choclo","Pan árabe con huevo, queso y tomate + infusión","Tarta de espinaca o acelga y ricota"),
 ("Mié","Tostada con ricota, pera, miel y nueces + infusión","Omelette de huevo y queso fresco relleno de verduras (zanahoria, tomate, espinaca)","Panqueques de avena, coco y banana + infusión","Rapiditas rellenas de vegetales (morrón, berenjena, zapallito, zanahoria) y cubos de carne"),
 ("Jue","Budín de avena y banana con yogur descremado y fruta","Ensalada de atún, huevo, tomate, remolacha, zanahoria y choclo","Tostadas con ricota, fruta y frutos secos + infusión","Milanesa de merluza con rodajas de calabaza y boniato al horno"),
 ("Vie","Panqueques de avena, manzana y pasta de maní + infusión","Hamburguesas caseras de lenteja o de carne con ensalada de repollo, tomate y lechuga","Yogur con granola, frutos secos y banana + infusión","Tarta de pollo y espinaca"),
 ("Sáb","Tostada con queso untable y huevo + fruta + infusión","Arroz integral con verduras salteadas y huevo o pollo en trozos","Pancakes de harina de algarroba con manzana + infusión","Pechuga de pollo con papas al horno + ensalada de zanahoria y tomate"),
 ("Dom","Galletas de arroz con ricota magra, manzana, miel y nuez + infusión","Guiso de lentejas con abundantes verduras y dados de carne","Muffins de avena y banana + infusión","Tacos rellenos de verdura cruda y cocida con pollo o tofu"),
],
"Menú semanal 2": [
 ("Lun","Tostada con huevo y hummus de garbanzos + infusión","Canastitas de espinaca, cebolla, queso y champiñones con masa integral","Grisines integrales con palta + infusión","Zapallitos rellenos con cebolla, zanahoria, morrón, choclo y pollo o tofu"),
 ("Mar","Cookies de avena y banana + infusión","Omelette con queso, ricota y arvejas + ensalada caprese","Tostadas con ricota, pasta de maní y frutas + infusión","Milanesa con verduras salteadas (berenjena, morrón, cebolla, zapallito)"),
 ("Mié","Tostada con ricota, rúcula y tomate + infusión","Ensalada de tomate, zanahoria, espinaca fresca, huevo y quinoa","Yogur natural con granola y banana + infusión","Filet de merluza al horno con papas + ensalada de remolacha y huevo"),
 ("Jue","Pancakes con manzana y pasta de maní + infusión","Tacos rellenos con lechuga, zanahoria, garbanzos, palta, ricota y queso","Smoothie de arándanos y banana + frutos secos","Carne al horno con rodajas de calabaza a la napolitana"),
 ("Vie","Yogur natural con granola y frutillas + infusión","Milanesa de berenjena con queso + calabaza y papa al horno","Yogur con granola y frutos rojos + infusión","Budín de acelga y queso con arroz + vegetales al horno"),
 ("Sáb","Tostadas con queso, palta y tomates cherry + infusión","Ensalada de atún, huevo, tomate, zanahoria, repollo y trigo burgol","Porridge de avena con fruta + infusión","Pechuga de pollo con ensalada de garbanzos, tomate y lechuga"),
 ("Dom","Barrita de cereal casera con frutas + infusión","Tarta mousse de zapallitos y brócoli","Pan árabe con jamón, queso y tomate + infusión","Wok de fideos, cebolla, zapallito, berenjena, zanahoria y calabaza"),
],
"Menú semanal 3": [
 ("Lun","Rapiditas con huevo, tomate y rúcula + infusión","Tarta de coliflor, ricota y queso","Yogur con avena, pasta de maní y frutas + infusión","Omelette con choclo y queso, con ensalada de hojas verdes"),
 ("Mar","Pancakes de avena y harina de algarroba + infusión","Sándwich de hummus de garbanzos, huevo, tomate y rúcula","Galletas de arroz con queso untable, palta y tomate + infusión","Pollo al horno con puré de papa y calabaza"),
 ("Mié","Huevos revueltos con queso fresco, jamón y tomate + infusión","Milanesa al horno con puré de coliflor y ensalada de tomate y huevo","Yogur natural con granola y banana + infusión","Filet de merluza con zapallitos revueltos"),
 ("Jue","Budín de avena y limón con yogur + infusión","Canelones de espinaca y pollo","Tostadas de arroz con queso fresco, ricota, pera y pasta de maní + infusión","Pastel de calabaza con carne o lentejas"),
 ("Vie","Yogur natural con frutas y tostada con ricota + infusión","Zapallitos rellenos con carne y vegetales","Pancakes de manzana y banana + infusión","Pollo al horno con ensalada mixta y cuscús"),
 ("Sáb","Tostadas con queso, ricota y tomates cherry + infusión","Ratatouille de verduras con carne o milanesa","Pancake salado con queso fresco y lomito + infusión","Omelette con queso, tomate y vegetales asados"),
 ("Dom","Rapiditas con ricota, queso untable y frutas + infusión","Tarta de pollo con ensalada","Pan árabe con queso, jamón y tomate + infusión","Wok de quinoa, cebolla, zapallito, berenjena, zanahoria y brócoli"),
],
"Menú vegetariano": [
 ("Lun","Rapiditas con huevo y hummus + infusión","Tarta de verduras con masa de avena","Tostadas con ricota, pasta de maní y frutas + infusión","Wok de verduras variadas con tofu y lentejas"),
 ("Mar","Pancakes de avena y coco + infusión","Budín de brócoli con papas y batatas al horno","Galletas de arroz con queso fresco y tomate + infusión","Milanesas de soja con puré de coliflor"),
 ("Mié","Porridge de avena y canela con fruta + infusión","Berenjenas a la napolitana con hamburguesas de lentejas","Yogur natural con granola y banana + infusión","Croquetas de zucchini con verduras y tofu salteados al wok"),
 ("Jue","Barritas de quinoa y semillas + infusión","Pastel de calabaza con lentejas","Budín de banana y chocolate + frutos secos","Fideos salteados con verduras y huevo"),
 ("Vie","Yogur natural con granola casera + infusión","Guiso de arroz con verduras y garbanzos","Muffins de manzana y nuez + infusión","Milanesas de tofu con ensalada de repollo y manzana"),
 ("Sáb","Tostadas con queso, palta y tomates cherry + infusión","Ensalada de garbanzos, huevo, tomate, zanahoria, repollo y trigo burgol","Talitas de garbanzos con hummus + infusión","Croquetas de quinoa y espinaca con puré de calabaza"),
 ("Dom","Yogur con copos sin azúcar, quinoa y frutas + infusión","Tarta de zapallitos y brócoli","Pan árabe con queso, tofu y tomate + infusión","Wok de cuscús, cebolla, zapallito, berenjena, zanahoria, calabaza y lentejas"),
],
}

if FULL:
    page(f'''
{chap_head("05", 'Menús <span class="t">semanales</span>', "Tres menús semanales y un menú vegetariano como punto de partida. Usalos tal cual o como ideas para armar tu propia semana.")}
<h2>Cómo usar los menús</h2>
{ul(["Elegí un menú por semana y armá tu lista de compras a partir de él (capítulo 7).",
     "Podés cambiar de lugar las comidas o repetir un día que te resulte práctico.",
     "Las preparaciones marcadas con <span class='rmark'>R</span> tienen receta en el capítulo 6.",
     "“Infusión” significa té, mate, café o mate cocido, idealmente sin azúcar."])}
<h2>Equivalencias para adaptar</h2>
<table class="eq">
<thead><tr><th>Si no tenés o no te gusta…</th><th>Podés usar…</th></tr></thead>
<tbody>
<tr><td>Pollo</td><td>Carne magra, pescado, huevo, tofu o legumbres</td></tr>
<tr><td>Merluza</td><td>Otro pescado blanco, atún al natural o caballa</td></tr>
<tr><td>Ricota o queso fresco</td><td>Queso untable descremado, yogur natural o huevo</td></tr>
<tr><td>Arroz integral</td><td>Quinoa, trigo burgol, cuscús, papa, batata o fideos</td></tr>
<tr><td>Una verdura en particular</td><td>Cualquier verdura de estación: lo importante es la variedad</td></tr>
</tbody></table>
{box("<b>Menú vegetariano.</b> Incluye huevo y lácteos. Sumá legumbres, tofu o huevo en almuerzo y cena. Si sos vegetariana o vegana de forma sostenida, consultá a un nutricionista (B12, hierro, calcio).", "soft")}
''', chapter="05 · Menús semanales", pid="cap5", toc="05 · Menús semanales")

RECIPE_MARKS = ["Hummus","Cookies de avena","Porridge","Pancakes de avena y coco","Barrita de cereal casera","Barritas de quinoa","Granola","granola casera","Muffins de manzana y nuez","Talitas de garbanzos","Tarta de verduras con masa de avena","Budín de brócoli","puré de coliflor","Croquetas de zucchini","Pastel de calabaza con lentejas","Milanesa de berenjena","Budín de banana y chocolate"]
def mark(t):
    for m in RECIPE_MARKS:
        if m.lower() in t.lower():
            return t + ' <span class="rmark">R</span>'
    return t

for name, rows in (MENUS.items() if FULL else []):
    body = "".join(f'<tr><th>{d}</th>' + "".join(f"<td>{mark(c)}</td>" for c in cs) + "</tr>" for d, *cs in rows)
    page(f'''
{eyebrow("MENÚS")}
<h1 class="h1">{name.split(" ")[0]} <span class="t">{" ".join(name.split(" ")[1:])}</span></h1>
<table class="menu"><thead><tr><th></th><th>Desayuno</th><th>Almuerzo</th><th>Merienda</th><th>Cena</th></tr></thead><tbody>{body}</tbody></table>
<p class="small"><span class="rmark">R</span> Receta en el capítulo 6. Ajustá las porciones con el criterio del plato (capítulo 4).</p>
''', chapter="05 · Menús semanales", pid="menu" + str(list(MENUS).index(name)+1))

# ================================================================== CAP 6 RECETAS
R = [
dict(t="Pancake individual", cat="Desayunos y meriendas", rinde="1 porción", tiempo="10 min",
 ing=["1 huevo","3 cdas de avena o harina de avena","1 cda de leche descremada o bebida vegetal","Unas gotas de esencia de vainilla","1 cdita de polvo de hornear"],
 pasos=["Mezclá todos los ingredientes en un bowl.","Calentá una sartén antiadherente a fuego mínimo y volcá la mezcla.","Cuando aparezcan las primeras burbujas en la superficie, dalo vuelta y cociná del otro lado.","Serví con el topping que prefieras: fruta, frutos secos, semillas, canela, cacao amargo, coco rallado o pasta de maní."],
 tip="Podés endulzar con gotas de stevia o sumar fruta a la mezcla: pera o manzana rallada, o banana pisada."),
dict(t="Cookies de avena y fruta", cat="Desayunos y meriendas", rinde="10–12 cookies", tiempo="30 min",
 ing=["1 banana madura pisada, 1 manzana rallada o 1 pera en cubos","1 taza de avena o harina integral (o una mezcla)","2 huevos","2 a 4 cdas de miel o azúcar, a gusto","1 cda de aceite","Esencia de vainilla","Opcional: semillas, frutos secos, granola o 1 cda de pasta de maní"],
 pasos=["Precalentá el horno a temperatura media.","Mezclá todos los ingredientes hasta integrar.","Con una cuchara, formá las cookies sobre una placa aceitada o con papel manteca.","Horneá unos 20 minutos, hasta que estén doradas."],
 tip="Conservalas en un recipiente hermético hasta 4 días."),
dict(t="Porridge de avena", cat="Desayunos y meriendas", rinde="1 porción", tiempo="10 min",
 ing=["¼ taza de avena tradicional","1 taza de leche o bebida vegetal","Canela y esencia de vainilla","Toppings a gusto: fruta, pasta de maní, cacao, almendras, semillas de zapallo"],
 pasos=["Poné la avena, la leche y la canela en una olla a fuego medio.","Revolvé suavemente hasta que espese, entre 5 y 10 minutos.","Agregá la vainilla y serví con los toppings."],
 tip="Si te queda muy espeso, agregá un chorrito más de leche."),
dict(t="Pancakes de banana y coco", cat="Desayunos y meriendas", rinde="4 pancakes chicos", tiempo="15 min",
 ing=["¼ taza de harina de garbanzos","1 huevo + 1 clara (o 3 cditas de chía hidratadas 20 min en ¼ vaso de agua)","¼ taza de puré de banana","2 cditas de coco rallado","1 cdita de cacao amargo","¼ cdita de polvo de hornear (solo si usás chía)"],
 pasos=["Mixeá o batí todos los ingredientes.","Calentá una sartén y volcá la preparación de a partes, dándole forma redonda.","Cociná a fuego bajo y con la sartén tapada.","Cuando aparezcan burbujas arriba, dalos vuelta y volvé a tapar hasta que estén cocidos."],
 tip="Con chía en lugar de huevo, la receta no lleva ingredientes de origen animal."),
dict(t="Barritas de cereal caseras", cat="Desayunos y meriendas", rinde="8 barritas", tiempo="35 min + enfriado",
 ing=["⅓ taza de quinoa cocida","¾ taza de mezcla de semillas y frutos secos (girasol, zapallo, sésamo, chía, lino, nueces, almendras, maní)","3 cdas de miel o azúcar","Opcional: coco rallado, cacao o canela"],
 pasos=["Picá los frutos secos en trozos bien chiquitos.","Integrá con la quinoa, las semillas y la miel.","Volcá en un molde forrado con papel manteca y aplastá hasta que quede compacto, de 1 cm de espesor.","Horneá a temperatura media hasta que esté dorado en los costados y en la superficie.","Dejá enfriar por completo antes de cortar."],
 tip="Guardalas en un recipiente hermético hasta una semana."),
dict(t="Budín de banana y chocolate", cat="Desayunos y meriendas", rinde="1 budín (10–12 porciones)", tiempo="50 min",
 ing=["2 tazas de harina de avena o integral","½ taza de azúcar mascabo","2 huevos","2 bananas maduras pisadas","6 cdas de aceite","2 cdas de cacao amargo","1 cda de polvo de hornear","Esencia de vainilla","Agua, leche o bebida vegetal, cantidad necesaria","Opcional: chips de chocolate o frutos secos"],
 pasos=["Batí los huevos con el azúcar.","Incorporá el resto de los ingredientes y mezclá de forma suave y envolvente, agregando líquido hasta lograr una masa espesa.","Volcá en un molde de budín grande o de torta de 24 cm.","Horneá a temperatura media entre 30 y 40 minutos, hasta que un palillo salga limpio."],
 tip="Se puede congelar en porciones: sacá una la noche anterior."),
dict(t="Granola casera", cat="Desayunos y meriendas", rinde="Aprox. 450 g", tiempo="30 min",
 ing=["150 g de avena en hojuelas","100 g de copos de maíz sin azúcar","100 g de quinoa inflada","50 g de frutos secos","Semillas de zapallo, lino y sésamo","3 cdas de miel","Opcional: coco rallado, chips de chocolate, arándanos deshidratados"],
 pasos=["Mezclá todos los ingredientes en un bowl hasta que quede pegajoso.","Esparcí sobre una placa con papel manteca.","Horneá a temperatura moderada unos 25 minutos, revolviendo cada tanto, hasta que esté crocante.","Dejá enfriar antes de guardar (los agregados como chips o frutas secas, sumalos al final)."],
 tip="Conservala en un frasco hermético hasta 2 semanas."),
dict(t="Muffins de manzana y nuez", cat="Desayunos y meriendas", rinde="6–8 muffins", tiempo="40 min",
 ing=["½ taza de harina de avena","½ taza de harina de trigo","¼ taza de azúcar","1 huevo","3 cdas de aceite","1 manzana rallada","½ manzana en cubos chiquitos","10 mariposas de nuez picadas","1 cdita de polvo de hornear","1 cdita de canela (opcional)"],
 pasos=["Batí el huevo con el azúcar hasta formar una crema.","Incorporá el aceite y batí unos segundos.","Agregá las harinas tamizadas de a poco.","Sumá el resto de los ingredientes y mezclá.","Distribuí en un molde con pirotines y horneá a temperatura media entre 20 y 30 minutos, hasta que un palillo salga limpio."],
 tip="Duran 3 días en un recipiente hermético o se pueden congelar."),
dict(t="Talitas de garbanzos", cat="Salados", rinde="1 placa", tiempo="35 min",
 ing=["300 g de harina de garbanzos","Sal a gusto","Orégano, provenzal o condimento para pizza","2 cdas de queso crema light","Agua, cantidad necesaria (aprox. ½ taza)","3 puñados de semillas (chía, sésamo, girasol, lino)"],
 pasos=["Mezclá todos los ingredientes en un bowl hasta formar una masa que se pueda amasar; agregá el agua de a poco.","Dejá reposar unos minutos.","Estirá sobre la mesada enharinada y cortá tiras.","Acomodalas en una placa con rocío vegetal y pincelalas con agua; si querés, espolvoreá semillas o condimentos.","Horneá a 200 °C unos 15 minutos, hasta que estén doradas."],
 tip="Acompañan muy bien al hummus."),
dict(t="Hummus de garbanzos", cat="Salados", rinde="4 porciones", tiempo="15 min (con garbanzos cocidos)",
 ing=["1 taza de garbanzos cocidos (en lata o hidratados y hervidos)","Jugo de ½ limón o más, a gusto","2 cdas de aceite de oliva","Sal, ajo, pimienta y pimentón","Agua de cocción de los garbanzos"],
 pasos=["Si usás garbanzos secos: hidratalos 12 horas o más, colalos y hervilos con ajo y laurel unos 40 minutos, hasta que se deshagan al apretarlos. Guardá el agua de cocción.","Procesá los garbanzos con los condimentos y el jugo de limón.","Agregá de a poco agua de cocción hasta lograr una consistencia cremosa.","Por último, sumá el aceite de oliva y procesá un poco más."],
 tip="Se conserva en la heladera, tapado, 3 a 4 días."),
dict(t="Ensalada tibia de vegetales, legumbres y pollo", cat="Almuerzos y cenas", rinde="2 porciones", tiempo="25 min",
 ing=["1 pechuga de pollo en cubos","1 taza de brócoli en ramilletes","1 zanahoria en rodajas","½ zucchini en medias lunas","½ morrón rojo en tiras","1 taza de garbanzos cocidos (o fideos o arroz)","1 cda de aceite de oliva","Jugo de ½ limón","Sal, pimienta, pimentón o comino","Perejil o cilantro (opcional)"],
 pasos=["Saltá el pollo con un chorrito de aceite hasta que esté dorado y bien cocido por dentro. Condimentá y reservá.","En la misma sartén, cociná el brócoli, la zanahoria, el zucchini y el morrón 5 a 7 minutos, hasta que estén tiernos pero firmes.","Sumá los garbanzos y el pollo y cociná 2 minutos más.","Rociá con limón, agregá perejil o cilantro y serví tibio."],
 tip="Es una buena vianda: llevala en un recipiente hermético y refrigerada."),
dict(t="Tarta de verduras con masa de avena", cat="Almuerzos y cenas", rinde="1 tarta (4 porciones)", tiempo="50 min",
 ing=["<b>Masa:</b> 2 tazas de harina de avena","2 huevos","2 cdas de aceite de oliva","Semillas a gusto","Sal y pimienta","<b>Relleno:</b> 2 cebollas","2 tazas de acelga cocida al vapor","2 cdas de harina de garbanzos","Sal y pimienta"],
 pasos=["Mezclá los ingredientes de la masa en un bowl y llevá a la heladera mientras preparás lo demás.","Picá las cebollas y rehogalas con un poco de aceite de oliva.","Estirá la masa en un molde antiadherente o aceitado ayudándote con la punta de los dedos.","Horneá la masa unos 15 minutos, hasta que se dore.","Mientras tanto, picá la acelga y mezclala con la cebolla y la harina de garbanzos.","Rellená la masa y horneá unos 20 minutos más."],
 tip="Podés reemplazar la acelga por espinaca, zapallitos o brócoli."),
dict(t="Budín de brócoli", cat="Almuerzos y cenas", rinde="3–4 porciones", tiempo="45 min",
 ing=["1 planta grande de brócoli","2 huevos","Cubos de queso (o un queso vegetal)","Verduras salteadas: zanahoria, cebolla y morrón","Sal y pimienta"],
 pasos=["Herví o cociná al vapor el brócoli.","Salteá el resto de las verduras en una sartén.","Batí los huevos y agregá los cubos de queso.","Mezclá todo; si queda muy seco, agregá un poco de agua.","Volcá en una budinera y horneá unos 25 minutos, hasta que esté firme."],
 tip="En el menú vegetariano se acompaña con papas y batatas al horno."),
dict(t="Puré de coliflor", cat="Almuerzos y cenas", rinde="3–4 porciones", tiempo="25 min",
 ing=["1 coliflor","1 cda de queso untable descremado","Nuez moscada, sal y pimienta a gusto"],
 pasos=["Cortá la coliflor y hervila o cocinala al vapor hasta que esté tierna.","Colala bien.","Procesá con el queso untable y los condimentos hasta lograr un puré."],
 tip="Podés mezclarlo mitad y mitad con puré de papa o calabaza."),
dict(t="Wok de verduras con arroz y pollo", cat="Almuerzos y cenas", rinde="2–3 porciones", tiempo="40 min",
 ing=["½ taza de arroz integral crudo","2 pechugas de pollo en cubos","1 cebolla","1 zanahoria","½ morrón verde y ½ morrón rojo","1 planta de brócoli cocido","2 cdas de aceite de oliva","1 cda de agua","Sal y pimienta negra"],
 pasos=["Herví el arroz.","En el wok, con un poco de agua y aceite, salteá primero la cebolla y después la zanahoria.","Agregá los morrones y luego el brócoli cocido.","Sumá el pollo y cociná unos 10 minutos, hasta que esté bien cocido, sin partes rosadas.","Incorporá el arroz y mezclá. Si querés, sumá una cucharada de queso untable para que quede más cremoso."],
 tip="Cambiá el pollo por tofu o huevo para una versión vegetariana."),
dict(t="Croquetas de zucchini", cat="Almuerzos y cenas", rinde="2–3 porciones", tiempo="35 min",
 ing=["2 zucchinis medianos","1 cebolla chica y 1 diente de ajo","1 taza de avena (aprox. 90 g)","1 huevo","1 cdita de polvo de hornear","Sal y pimienta"],
 pasos=["Precalentá el horno a temperatura alta.","Rallá los zucchinis y escurrí bien el líquido con las manos o un repasador.","Mezclá con la cebolla y el ajo picados y el resto de los ingredientes.","Formá bolitas o medallones y colocalos en una placa con rocío vegetal.","Horneá unos 15 minutos, hasta que estén dorados."],
 tip="Si la mezcla queda muy húmeda, agregá un poco más de avena."),
dict(t="Pastel veggie de lentejas", cat="Almuerzos y cenas", rinde="4 porciones", tiempo="1 h 15 min + remojo",
 ing=["1 calabaza grande","1 taza de lentejas cocidas","2 cebollas medianas","1 cdita de cúrcuma","1 cda de pimentón","Ajo en polvo, sal y pimienta","Aceite de oliva"],
 pasos=["Remojá las lentejas al menos 12 horas, descartá el agua y hervilas en agua abundante hasta que estén tiernas.","Horneá la calabaza con un poco de aceite, sal y pimienta. Hacé un puré y sumá la cúrcuma.","Rehogá la cebolla picada con aceite de oliva.","Mezclá las lentejas con la cebolla y condimentá con pimentón, ajo, sal y pimienta.","Armá el pastel: lentejas abajo y puré de calabaza arriba. Gratiná en horno fuerte."],
 tip="Con lentejas en lata, el tiempo baja a unos 45 minutos."),
dict(t="Milanesas de berenjena", cat="Almuerzos y cenas", rinde="2 porciones", tiempo="30 min",
 ing=["1 berenjena grande","1 huevo batido con un chorrito de agua","Rebozador: pan rallado, avena o una mezcla"],
 pasos=["Cortá la berenjena en rodajas de ½ cm.","Pasalas por el huevo y luego por el rebozador.","Cocinalas en una placa para horno o en una sartén antiadherente a fuego medio, dándolas vuelta, hasta que estén tiernas y doradas."],
 tip="A la napolitana: al final sumá salsa de tomate y queso y gratiná."),
dict(t="Heladitos de banana y chocolate", cat="Postres", rinde="4 porciones", tiempo="10 min + 3 h de freezer",
 ing=["2 bananas maduras","1 cda de cacao amargo","2 sobres de edulcorante (opcional)","½ taza de leche","Para arriba: frutos secos o chips de chocolate"],
 pasos=["Procesá todos los ingredientes, menos los de arriba.","Distribuí en vasitos o potecitos y agregá los frutos secos o chips.","Llevá al freezer hasta que estén firmes."],
 tip=""),
dict(t="Flancito en taza", cat="Postres", rinde="1 porción", tiempo="5 min",
 ing=["1 huevo","½ taza de leche descremada","Esencia de vainilla","Edulcorante a gusto","1 cda de coco rallado"],
 pasos=["Mezclá todo en una taza apta para microondas.","Tapala y cociná en el microondas entre 2 y 3 minutos, controlando desde el primer minuto: el tiempo depende de cada equipo.","Está listo cuando el centro está firme. Dejá entibiar antes de comer."],
 tip=""),
dict(t="Mug cake de limón", cat="Postres", rinde="1 porción", tiempo="5 min",
 ing=["1 huevo","Jugo y ralladura de ½ limón","Esencia de vainilla","Edulcorante a gusto","1 cda de coco rallado","1 cda de harina de avena o avena","2 cdas de yogur natural","1 cdita de polvo de hornear"],
 pasos=["Mezclá todo en una taza apta para microondas.","Tapala y cociná entre 2 y 3 minutos, controlando desde el primer minuto.","Está listo cuando al pincharlo sale seco."],
 tip=""),
dict(t="Cheesecake en taza", cat="Postres", rinde="1 porción", tiempo="5 min",
 ing=["<b>Base:</b> 1 cda de avena o granola","1 cda de pasta de maní","<b>Relleno:</b> 100 g de queso untable descremado (4 a 5 cdas)","1 huevo","Esencia de vainilla","1 sobre de edulcorante","<b>Arriba:</b> 1 cda de mermelada sin azúcar"],
 pasos=["En una taza, mezclá la avena o granola con la pasta de maní y presioná para formar la base.","Aparte, mezclá los ingredientes del relleno y volcalos sobre la base.","Cociná en el microondas unos 2 minutos, hasta que esté firme.","Serví con la mermelada arriba."],
 tip=""),
dict(t="Brownie de banana", cat="Postres", rinde="6 cuadrados", tiempo="30 min",
 ing=["3 bananas maduras","3 cdas de pasta de maní","3 cdas de cacao amargo"],
 pasos=["Pisá muy bien las bananas con un tenedor o procesalas.","Integrá la pasta de maní y el cacao.","Volcá en una fuente y horneá a temperatura media unos 20 minutos.","Dejá enfriar antes de cortar."],
 tip=""),
]

R = R[:19] + [R[22]] + R[19:22]   # el brownie va junto a los otros postres de horno/freezer


TIPS = {
"Pancake individual": [
 "<b>Antes de empezar:</b> mezclá primero el huevo con la leche y recién después sumá la avena y el polvo de hornear. Así no quedan grumos.",
 "<b>Reposo:</b> dejá la mezcla 2 o 3 minutos para que la avena se hidrate. El pancake queda más esponjoso y no se rompe al darlo vuelta.",
 "<b>La sartén:</b> calentala bien, untala apenas con aceite usando un papel y bajá a fuego mínimo antes de volcar. Con fuego alto se quema afuera y queda crudo adentro.",
 "<b>El momento justo:</b> dalo vuelta cuando aparezcan burbujas en toda la superficie y los bordes se vean secos. Usá una espátula ancha y un movimiento rápido.",
 "<b>Variantes:</b> endulzá con gotas de stevia o sumá fruta a la mezcla (pera o manzana rallada, banana pisada). Los toppings agregalos recién al servir."],
"Cookies de avena y fruta": [
 "<b>La fruta:</b> usá banana bien madura, con pintitas negras. Endulza más, une mejor la masa y te permite usar menos miel o azúcar.",
 "<b>La textura de la masa:</b> tiene que quedar húmeda pero que se pueda tomar con cuchara. Si está muy líquida, agregá una cucharada más de avena.",
 "<b>Al armarlas:</b> dejá 2 cm entre cookie y cookie y aplastalas apenas con el dorso de la cuchara, porque se expanden un poco en el horno.",
 "<b>Punto de cocción:</b> sacalas cuando los bordes estén dorados aunque el centro siga blando. Terminan de endurecer al enfriarse sobre la placa.",
 "<b>Conservación:</b> guardalas frías en un recipiente hermético hasta 4 días, o congelalas y sacá de a una cuando las necesites."],
"Porridge de avena": [
 "<b>La avena correcta:</b> usá avena tradicional (arrollada). La instantánea se cocina más rápido pero queda más pastosa.",
 "<b>A fuego bajo:</b> cociná a fuego medio-bajo y revolvé seguido, sobre todo al final, para que la avena no se pegue al fondo de la olla.",
 "<b>La textura:</b> sacalo un poco antes de que esté como te gusta: sigue espesando unos minutos fuera del fuego.",
 "<b>Si se espesa de más:</b> agregá un chorrito de leche caliente, no fría, y revolvé hasta que vuelva a quedar cremoso.",
 "<b>Al servir:</b> sumá la vainilla y los toppings fuera del fuego. Una cucharada de pasta de maní o unas semillas suman proteína y saciedad."],
"Pancakes de banana y coco": [
 "<b>Antes de empezar:</b> si reemplazás el huevo por chía, hidratala 20 minutos antes en el agua hasta que quede gelatinosa.",
 "<b>Reposo:</b> dejá la mezcla 5 minutos. La harina de garbanzos absorbe líquido y la masa toma más cuerpo.",
 "<b>Tamaño:</b> hacelos chicos, de una cucharada sopera cada uno. Con harina de garbanzos son más frágiles y así se dan vuelta sin romperse.",
 "<b>Cocción:</b> fuego bajo y sartén tapada, para que se cocinen por dentro sin quemarse por fuera.",
 "<b>Sabor:</b> la harina de garbanzos cruda tiene sabor fuerte; cocinalos bien de los dos lados para que desaparezca."],
"Barritas de cereal caseras": [
 "<b>La quinoa:</b> lavala bien antes de cocinarla para quitarle el amargor y escurrila muy bien. Si queda húmeda, las barritas se desarman.",
 "<b>Los frutos secos:</b> picalos bien chiquitos. Los trozos grandes hacen que la barrita se quiebre al cortarla.",
 "<b>El molde:</b> forralo con papel manteca que sobresalga de los bordes: así después la levantás entera sin romperla.",
 "<b>Compactar:</b> presioná la mezcla con fuerza, con el dorso de una cuchara o la base de un vaso, hasta que quede bien pareja.",
 "<b>El corte:</b> esperá a que esté totalmente fría y cortá con un cuchillo bien filoso. Caliente se desarma."],
"Budín de banana y chocolate": [
 "<b>Antes de empezar:</b> precalentá el horno al menos 10 minutos y aceitá y enharinalá el molde.",
 "<b>Las bananas:</b> cuanto más maduras, más dulce y húmedo queda el budín. Pisalas bien para que no queden trozos grandes.",
 "<b>El mezclado:</b> después de sumar la harina, mezclá suave y solo hasta integrar. Si batís de más, queda duro y con túneles.",
 "<b>Punto de cocción:</b> pinchá el centro con un palillo: tiene que salir seco o con migas, no con masa líquida.",
 "<b>Desmolde y conservación:</b> dejalo 10 minutos en el molde antes de desmoldar. Se puede congelar en porciones: sacá una la noche anterior."],
"Granola casera": [
 "<b>La mezcla:</b> integrá bien la miel con todos los ingredientes secos hasta que todo quede apenas pegajoso. Si queda seca, no se forman los clusters.",
 "<b>Capa fina:</b> esparcila en una sola capa sobre la placa. Si queda amontonada, se cocina al vapor y no se pone crocante.",
 "<b>Revolver:</b> movela cada 8 a 10 minutos para que se dore pareja y no se queme en los bordes de la placa.",
 "<b>Engaña al sacarla:</b> recién salida del horno parece blanda. Se vuelve crocante al enfriarse, así que no la cocines de más.",
 "<b>Agregados:</b> sumá chips de chocolate o frutas secas recién cuando esté fría, para que no se derritan ni se quemen."],
"Muffins de manzana y nuez": [
 "<b>Antes de empezar:</b> precalentá el horno y prepará los pirotines. Los muffins crecen mejor si entran al horno apenas mezclada la masa.",
 "<b>La manzana:</b> si la manzana rallada suelta mucho jugo, escurrila un poco con la mano para que la masa no quede aguada.",
 "<b>No batir de más:</b> integrá las harinas de a poco y mezclá solo hasta que no se vea harina seca.",
 "<b>Llenado:</b> completá los pirotines hasta 3/4: necesitan espacio para crecer y formar el copete.",
 "<b>El horno:</b> no lo abras los primeros 15 minutos porque se pueden bajar. Probá con un palillo antes de sacarlos."],
"Talitas de garbanzos": [
 "<b>El agua:</b> sumala de a poco. La masa tiene que quedar suave, que se pueda amasar y no se pegue en las manos.",
 "<b>Reposo:</b> dejala descansar unos minutos tapada: se hidrata la harina y se estira mucho más fácil.",
 "<b>Estirado parejo:</b> estirala fina y del mismo espesor en toda la superficie, así se cocinan todas al mismo tiempo.",
 "<b>Las semillas:</b> pincelá con agua antes de espolvorearlas para que se peguen y no se caigan al hornear.",
 "<b>Ojo al final:</b> los últimos minutos pasan rápido de doradas a quemadas. Mirá el horno y sacalas cuando estén doradas y firmes."],
"Hummus de garbanzos": [
 "<b>Garbanzos secos:</b> remojalos al menos 12 horas y cambiales el agua. Se cocinan más rápido y caen mejor.",
 "<b>Cocción completa:</b> tienen que deshacerse al apretarlos con los dedos. Si quedan firmes, el hummus sale granulado.",
 "<b>Más cremoso:</b> procesalos todavía tibios y, si lo querés extra suave, quitales la piel frotándolos entre las manos.",
 "<b>La textura:</b> ajustala con el agua de cocción de a una cucharada, no toda junta. Siempre podés agregar, no sacar.",
 "<b>Conservación:</b> guardalo tapado en la heladera 3 a 4 días, con un hilo de aceite de oliva arriba para que no se seque."],
"Ensalada tibia de vegetales, legumbres y pollo": [
 "<b>Organizá todo antes:</b> cortá el pollo y las verduras antes de prender el fuego; la cocción es rápida.",
 "<b>Cortes parejos:</b> cubos de pollo del mismo tamaño se cocinan al mismo tiempo y no quedan partes crudas.",
 "<b>No llenes la sartén:</b> si está muy cargada, el pollo larga agua y se hierve en vez de dorarse. Cociná en dos tandas si hace falta.",
 "<b>El orden de las verduras:</b> sumalas de la más dura a la más blanda (brócoli y zanahoria primero, zucchini al final) y dejalas al dente.",
 "<b>Como vianda:</b> llevala en un recipiente hermético y refrigerada. El limón agregalo al momento de comer para que no se ablanden las verduras."],
"Tarta de verduras con masa de avena": [
 "<b>La masa:</b> dejala al menos 15 minutos en la heladera. Fría se maneja mucho mejor y se estira fácil con la punta de los dedos.",
 "<b>Base precocida:</b> horneala sola antes de rellenar. Es el secreto para que no quede cruda o húmeda abajo.",
 "<b>La acelga:</b> después de cocinarla, apretala bien con las manos para sacarle toda el agua. El exceso de líquido arruina la masa.",
 "<b>La cebolla:</b> rehogala a fuego bajo hasta que esté transparente y dulce; le da mucho sabor al relleno.",
 "<b>Variantes:</b> cambiá la acelga por espinaca, zapallitos o brócoli. Dejala reposar 10 minutos antes de cortar."],
"Budín de brócoli": [
 "<b>El brócoli:</b> cocinalo al vapor o hervido solo hasta que esté tierno, y escurrilo muy bien para que el budín no quede aguado.",
 "<b>Las verduras salteadas:</b> cocinalas hasta que pierdan el agua; así suman sabor y no humedad.",
 "<b>El molde:</b> aceitá y enharinalá la budinera, o forrala con papel manteca, para desmoldar sin que se rompa.",
 "<b>Punto de cocción:</b> está listo cuando el centro está firme y al pincharlo no sale líquido.",
 "<b>Reposo:</b> dejalo 10 minutos antes de cortar: se asienta y las porciones salen enteras."],
"Puré de coliflor": [
 "<b>El corte:</b> separá la coliflor en ramilletes del mismo tamaño para que se cocinen parejo.",
 "<b>Cocción:</b> cocinala hasta que esté bien tierna al pincharla, pero sin que se deshaga en el agua.",
 "<b>Escurrido:</b> dejala unos minutos en el colador para que largue el vapor. Es la clave para que el puré no quede aguado.",
 "<b>Procesado:</b> procesala caliente: queda más lisa y cremosa que si la pisás fría.",
 "<b>Sabor:</b> probá y ajustá la sal y la nuez moscada al final. Podés mezclarlo mitad y mitad con puré de papa o calabaza."],
"Wok de verduras con arroz y pollo": [
 "<b>Todo listo antes:</b> tené el arroz cocido y todas las verduras cortadas antes de prender el fuego: en el wok todo pasa rápido.",
 "<b>El arroz:</b> el arroz cocido del día anterior se saltea mejor y no se empasta.",
 "<b>Fuego fuerte:</b> usá fuego alto y revolvé sin parar para que las verduras queden crocantes y con color.",
 "<b>El pollo:</b> cocinalo hasta que no tenga partes rosadas por dentro; cortalo en cubos chicos para que se haga rápido.",
 "<b>Versión vegetariana:</b> cambiá el pollo por tofu o huevo. Una cucharada de queso untable al final lo hace más cremoso."],
"Croquetas de zucchini": [
 "<b>El paso más importante:</b> rallá el zucchini, salalo apenas, esperá 10 minutos y escurrilo con un repasador. Sin este paso se desarman.",
 "<b>La mezcla:</b> si queda muy húmeda, agregá una cucharada más de avena hasta que se pueda formar con las manos.",
 "<b>Al formarlas:</b> mojate apenas las manos para que no se peguen y hacelas del mismo tamaño.",
 "<b>El horno:</b> precalentalo bien fuerte y usá rocío vegetal en la placa para que se doren abajo.",
 "<b>Dorado parejo:</b> dalas vuelta a mitad de cocción para que queden doradas de los dos lados."],
"Pastel veggie de lentejas": [
 "<b>Las lentejas:</b> remojalas, descartá esa agua y cocinalas hasta que estén tiernas pero enteras, no pasadas. Con lentejas en lata ahorrás tiempo.",
 "<b>La calabaza:</b> horneada tiene más sabor que hervida y queda más seca, ideal para un puré espeso.",
 "<b>Un puré firme:</b> si el puré queda líquido se hunde en las lentejas. Tiene que quedar espeso, que se sostenga con la cuchara.",
 "<b>El armado:</b> esparcí las lentejas parejas y cubrí con el puré de los bordes hacia el centro, así queda sellado.",
 "<b>Gratinado:</b> los últimos minutos, horno bien fuerte para dorar la superficie. Dejalo reposar antes de servir."],
"Milanesas de berenjena": [
 "<b>Cortes parejos:</b> cortá rodajas del mismo espesor, de medio centímetro, para que se cocinen todas igual.",
 "<b>Quitar el amargor:</b> salalas y dejalas 15 minutos. Después secalas con papel: pierden agua y amargor.",
 "<b>Rebozado firme:</b> presioná bien el rebozador con la mano para que se adhiera y no se despegue al cocinar.",
 "<b>Cocción:</b> en placa con rocío vegetal o en sartén antiadherente; dalas vuelta una sola vez para que queden crocantes.",
 "<b>A la napolitana:</b> al final sumá salsa de tomate y queso y gratiná unos minutos."],
"Heladitos de banana y chocolate": [
 "<b>Las bananas:</b> cuanto más maduras, más dulce y cremoso queda el helado, sin necesidad de agregar azúcar.",
 "<b>El procesado:</b> procesá hasta que no quede ningún grumo; la textura final depende de este paso.",
 "<b>Los recipientes:</b> usá vasitos chicos o moldes de silicona: se congelan más rápido y salen porciones justas.",
 "<b>El freezer:</b> dejalos al menos 3 horas, o mejor toda la noche.",
 "<b>Al servir:</b> sacalos 5 minutos antes de comerlos para que estén cremosos y no duros como piedra."],
"Flancito en taza": [
 "<b>La taza:</b> usá una taza apta para microondas, de cerámica o vidrio, y tapala para que no salpique.",
 "<b>La mezcla:</b> batí bien el huevo con la leche hasta que esté totalmente integrado, así el flan queda liso.",
 "<b>De a poco:</b> cociná de a 30 a 60 segundos y controlá: cada microondas es distinto y se pasa rápido.",
 "<b>Punto justo:</b> está listo cuando el centro está firme y apenas tiembla al mover la taza.",
 "<b>Reposo:</b> dejalo un minuto antes de comer: sigue cocinándose con el calor y toma mejor textura."],
"Mug cake de limón": [
 "<b>La taza:</b> usá una taza grande y no la llenes más de la mitad: crece mucho en el microondas.",
 "<b>La ralladura:</b> rallá solo la parte amarilla del limón. La parte blanca da amargor.",
 "<b>Mezcla pareja:</b> integrá bien todo dentro de la taza, raspando el fondo para que no quede harina seca.",
 "<b>El tiempo:</b> controlá desde el primer minuto. Está listo cuando al pincharlo sale seco.",
 "<b>No te pases:</b> si lo cocinás de más, se seca y queda gomoso. Mejor sacarlo un poco antes."],
"Cheesecake en taza": [
 "<b>La base:</b> presioná bien la avena con la pasta de maní en el fondo de la taza para que no se mezcle con el relleno.",
 "<b>El queso:</b> usalo a temperatura ambiente: se integra mejor y el relleno queda liso, sin grumos.",
 "<b>El batido:</b> mezclá el relleno hasta que esté homogéneo antes de volcarlo sobre la base.",
 "<b>Cocción:</b> está listo cuando el relleno está firme y apenas tiembla en el centro.",
 "<b>El toque final:</b> dejalo enfriar y llevalo 1 hora a la heladera antes de sumar la mermelada: toma textura de cheesecake."],
"Brownie de banana": [
 "<b>Las bananas:</b> usá bananas muy maduras: son las que dan el dulzor y la humedad.",
 "<b>El pisado:</b> pisalas muy bien o procesalas para que la mezcla quede lisa y sin trozos.",
 "<b>El molde:</b> forralo con papel manteca para desmoldar fácil y cortar prolijo.",
 "<b>No lo cocines de más:</b> el centro tiene que quedar apenas húmedo; así queda húmedo y no seco.",
 "<b>El corte:</b> dejalo enfriar por completo antes de cortar para que salgan cuadrados prolijos."],
}

def recipe_img(n, title):
    path = f"img/food/{n:02d}.jpg"
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), path)):
        return f'<div class="recimg"><img src="{path}" alt="{esc(title)}"></div>'
    return f'<div class="recimg ph"><span>FOTO {n:02d} · {esc(title).upper()}</span></div>'

def recipe_html(r, n=0):
    ing = "".join(f"<li>{i}</li>" for i in r["ing"])
    pasos = "".join(f"<li>{p}</li>" for p in r["pasos"])
    tip = f'<p class="tip"><b>Tip:</b> {r["tip"]}</p>' if r["tip"] else ""
    return (f'<article class="rec">{recipe_img(n, r["t"])}<div class="rech"><span class="rcat">{r["cat"].upper()}</span><h2>{r["t"]}</h2>'
            f'<div class="rmeta"><span>Rinde: <b>{r["rinde"]}</b></span><span>Tiempo: <b>{r["tiempo"]}</b></span></div></div>'
            f'<div class="recb"><div><h5>Ingredientes</h5><ul class="ing">{ing}</ul></div>'
            f'<div><h5>Preparación</h5><ol class="steps-ol">{pasos}</ol></div></div></article>'
            + f'<div class="keytips"><h5>Consejos clave de preparación</h5><ul>' + "".join(f"<li>{t}</li>" for t in TIPS[r["t"]]) + '</ul></div>')

REC_HEAD = (chap_head("06", 'Recetas <span class="t">fáciles</span>', "Recetas simples para resolver desayunos, meriendas, comidas y postres. La mayoría aparece en los menús del capítulo 5.") if FULL else
            eyebrow("BONUS 1 · INCLUIDO") + '<h1 class="h1">Recetario <span class="t">fácil</span></h1><p class="lead">' + str(len(R)) + ' recetas simples para resolver desayunos, meriendas, comidas y postres, con ingredientes de cualquier súper.</p>')
REC_CH = "06 · Recetas" if FULL else "Bonus 1 · Recetario"
page(f'''
{REC_HEAD}
<div class="cols2 keep">
<div>
<h3>Abreviaturas y medidas</h3>
{ul(["<b>cda:</b> cucharada sopera.", "<b>cdita:</b> cucharadita de té.", "<b>taza:</b> taza de desayuno, aprox. 240 ml.", "<b>Horno medio:</b> 180 °C · <b>alto:</b> 200–220 °C."])}
<h3>Seguridad en la cocina</h3>
{ul(["El pollo y la carne picada deben quedar bien cocidos, sin partes rosadas.", "Enfriá las preparaciones antes de guardarlas y refrigeralas dentro de las 2 horas.", "Los tiempos de horno y microondas son orientativos: cada equipo es distinto."])}
</div>
<div>
<h3>Índice de recetas</h3>
<ol class="rindex">{"".join(f'<li><a href="#rec{i}">{r["t"]}</a></li>' for i, r in enumerate(R))}</ol>
</div>
</div>
''', chapter=REC_CH, pid="cap6", toc="06 · Recetas" if FULL else "Bonus 1 · Recetario")

# agrupación de recetas por página (ajustada para que entren sin cortar)
page("".join(f'<div class="recw" id="rec{i}">{recipe_html(r, i+1)}</div>' for i, r in enumerate(R)), chapter=REC_CH, pid="recetas")

# ================================================================== CAP 7 ORGANIZACIÓN Y COMPRAS
if FULL:
    page(f'''
{chap_head("07", 'Organización y <span class="t">lista de compras</span>', "Un poco de organización al principio de la semana te ahorra decisiones, tiempo y compras de urgencia.")}
<div class="tiles">
<div class="tile"><h3>Planificación semanal</h3><p>Elegí el menú un día fijo. Los días más cargados, comidas simples o ya listas.</p></div>
<div class="tile"><h3>Preparación anticipada</h3><p>En 60 a 90 minutos dejá verduras cortadas, legumbres y una proteína lista.</p></div>
<div class="tile"><h3>Uso del freezer</h3><p>Cociná de más y congelá porciones. Rotulá con nombre y fecha.</p></div>
<div class="tile"><h3>Aprovechamiento</h3><p>Antes de comprar, revisá qué tenés y planificá con eso.</p></div>
<div class="tile"><h3>Heladera y alacena</h3><p>Adelante y a la vista, lo que hay que consumir primero. Lo nuevo, atrás.</p></div>
<div class="tile"><h3>Cómo comprar</h3><p>Andá con lista y sin hambre. Leé las etiquetas.</p></div>
</div>
<h2>Checklist semanal de organización</h2>
<div class="cbox">
{"".join(f'<div class="cb"><span class="sq"></span>{t}</div>' for t in ["Elegí el menú de la semana","Revisé heladera, freezer y alacena","Armé la lista de compras","Hice las compras","Lavé y corté verduras","Cociné una legumbre o un cereal base","Dejé una proteína preparada","Organicé las viandas de los días con más trabajo","Ubiqué adelante lo que hay que consumir primero","Anoté qué cenas repito esta semana"])}
</div>
''', chapter="07 · Organización y compras", pid="cap7", toc="07 · Organización y lista de compras")

SHOP = [
 ("Proteínas", ["Carne vacuna magra: lomo, nalga, cuadril, palomita, peceto","Pollo: pechuga, muslo sin piel","Pescados: merluza, atún al natural, caballa","Cerdo magro","Huevos","Tofu o soja texturizada (menú vegetariano)"]),
 ("Verduras y frutas", ["Verduras variadas de estación","Hojas verdes: lechuga, rúcula, espinaca, acelga","Zapallito, zucchini, berenjena, brócoli, coliflor","Zanahoria, calabaza, cebolla, morrón, tomate","Papa, batata y choclo","Frutas variadas","Limón y palta"]),
 ("Cereales, legumbres y otros carbohidratos", ["Avena (instantánea o arrollada)","Pan integral, pan árabe o rapiditas","Arroz integral o yamaní","Fideos integrales o de legumbres","Quinoa, trigo burgol, cuscús, amaranto, mijo, trigo sarraceno","Legumbres: lentejas, garbanzos, porotos, arvejas","Harinas: de avena, integral, de garbanzos, de algarroba","Cereales sin azúcar, quinoa pop, granola","Masa de tarta o empanada integral","Galletas de arroz"]),
 ("Lácteos o alternativas", ["Leche descremada o bebida vegetal","Yogur natural descremado","Queso untable descremado","Queso fresco descremado","Ricota magra"]),
 ("Grasas, semillas y frutos secos", ["Aceite de oliva, girasol o maíz","Frutos secos: nueces, almendras, maní","Semillas: chía, lino, sésamo, zapallo, girasol","Pasta de maní"]),
 ("Condimentos y básicos", ["Té, mate cocido, café, yerba","Sal, pimienta, orégano, albahaca, romero, ají molido","Nuez moscada, pimentón, ajo en polvo, cúrcuma, comino, canela","Aceto y vinagre","Miel, stevia, mermelada sin azúcar","Cacao amargo y chocolate amargo","Esencia de vainilla y polvo de hornear"]),
]
def shop_block(t, items):
    return f'<div class="shop"><h3>{t}</h3>' + "".join(f'<div class="cb"><span class="sq"></span>{i}</div>' for i in items) + "</div>"

if FULL:
    page(f'''
{eyebrow("LISTA DE COMPRAS IMPRIMIBLE")}
<h1 class="h1">Lista de <span class="t">compras</span></h1>
<p>Una base con los alimentos que aparecen en los menús y recetas. Las cantidades dependen del menú elegido y de cuántas personas comen en tu casa: marcá lo que necesitás esta semana.</p>
<div class="shopgrid">
<div>{shop_block(*SHOP[0])}{shop_block(*SHOP[1])}{shop_block(*SHOP[3])}</div>
<div>{shop_block(*SHOP[2])}{shop_block(*SHOP[4])}{shop_block(*SHOP[5])}</div>
</div>
''', chapter="07 · Organización y compras", pid="cap7b")

# ================================================================== CAP 8 DESCANSO
if FULL:
    page(f'''
{chap_head("08", 'Descanso y <span class="t">recuperación</span>', "Dormir bien influye en tu energía, tu humor, tu apetito y en cómo te recuperás del entrenamiento. Estos hábitos ayudan; ninguno es una garantía.")}
<div class="cols2">
<div>
<h3>Cómo saber si estás descansando bien</h3>
<p>Una señal práctica es cómo te sentís durante el día: si te despertás con energía y podés sostener la jornada sin depender de la cafeína, probablemente tu descanso es adecuado. La mayoría de los adultos necesita al menos 7 horas de sueño por noche.</p>
<h3>Regularidad de horarios</h3>
<p>Intentá acostarte y levantarte a horarios parecidos todos los días, también los fines de semana. Es uno de los hábitos con más impacto.</p>
<h3>Ambiente de descanso</h3>
<p>Una habitación oscura, silenciosa y fresca favorece el sueño. Usá la cama para dormir y evitá trabajar en ella.</p>
<h3>Cafeína</h3>
<p>El efecto de la cafeína dura varias horas. Como referencia, evitá el café, el mate y las bebidas energéticas en las 6 horas previas a acostarte.</p>
</div>
<div>
<h3>Luz y pantallas</h3>
<p>La exposición a la luz natural durante la mañana ayuda a ordenar el reloj biológico. A la noche, bajá las luces y alejate de las pantallas un rato antes de dormir: no solo por la luz, sino porque mails, redes y noticias mantienen la mente activa.</p>
<h3>Estrés y preocupaciones</h3>
<p>Si te acostás con la cabeza llena de pendientes, probá escribirlos en un papel antes de ir a la cama, junto con el primer paso para resolverlos al día siguiente. Una lectura tranquila o ejercicios de respiración también pueden ayudarte a bajar el ritmo.</p>
<h3>Actividad física y recuperación</h3>
<p>La actividad física regular se asocia con un mejor descanso. Si entrenás de noche y notás que te cuesta dormirte, probá adelantar la sesión o hacer la versión más suave.</p>
<h3>Alcohol y comidas tardías</h3>
<p>El alcohol puede ayudar a conciliar el sueño, pero empeora su calidad durante la noche. Las cenas muy abundantes justo antes de acostarte también pueden dificultar el descanso.</p>
<h3>¿Hay alimentos que ayudan a dormir?</h3>
<p>Algunos alimentos, como los frutos secos, el pescado, el huevo, ciertas frutas y las verduras de hoja, aportan nutrientes que participan en la regulación del sueño. Una infusión caliente sin cafeína, como la manzanilla, puede ser parte de una rutina relajante. La evidencia sobre alimentos puntuales es limitada: suman dentro de una alimentación variada, pero ningún alimento o infusión por sí solo garantiza dormir mejor.</p>
</div>
</div>
''', chapter="08 · Descanso y recuperación", pid="cap8", toc="08 · Descanso y recuperación")

if FULL:
    page(f'''
{eyebrow("DESCANSO")}
<h1 class="h1">Rutina nocturna y <span class="t">cuándo consultar</span></h1>
<div class="cols2">
<div>
<h3>Una rutina para la última hora del día</h3>
{checks(["Bajá las luces y dejá el celular fuera de alcance.","Anotá los pendientes del día siguiente.","Ducha tibia, lectura o respiración lenta.","Acostate cuando tengas sueño, a un horario regular."])}
</div>
<div>
<h3>Dificultades ocasionales o un problema persistente</h3>
<p>Tener algunas noches malas es habitual, sobre todo en épocas de estrés. Pero si te cuesta dormirte o mantener el sueño al menos 3 noches por semana durante más de 3 meses, y eso afecta tu día, puede tratarse de insomnio crónico.</p>
<h3>Terapia cognitivo-conductual para el insomnio (TCC-I)</h3>
<p>La TCC-I es el tratamiento de primera línea recomendado para el insomnio crónico en adultos. Es una intervención que guía un profesional capacitado y combina, entre otras herramientas, el trabajo sobre las creencias en torno al sueño y cambios de hábitos. Algunas de sus técnicas, como la restricción del tiempo en cama, deben indicarse y supervisarse profesionalmente: no conviene aplicarlas por tu cuenta.</p>
{box("<b>Consultá con un profesional si:</b> roncás fuerte o te dicen que hacés pausas al respirar, tenés mucho sueño durante el día, el insomnio se sostiene en el tiempo, o notás cambios en el ánimo. Un médico o un especialista en medicina del sueño puede evaluarte.", "note")}
</div>
</div>
''', chapter="08 · Descanso y recuperación", pid="cap8b")

# ================================================================== CAP 9 SEGUIMIENTO
TRACK = ["Sesión de fuerza","Actividad física / aeróbico","Comidas organizadas","Preparación anticipada","Hora de acostarme","Hora de levantarme","Energía percibida (1 a 5)"]
if FULL:
    page(f'''
{chap_head("09", 'Seguimiento de <span class="t">hábitos</span>', "Una planilla para detectar patrones y tomar mejores decisiones. No es para calificarte: una semana con casilleros vacíos también te da información.")}
<p class="small">Marcá con un tilde lo que hiciste. Energía: 1 = muy baja, 5 = muy buena.</p>
<h3 class="wk">Semana del ____ / ____ al ____ / ____</h3>
<table class="track"><thead><tr><th></th><th>Lun</th><th>Mar</th><th>Mié</th><th>Jue</th><th>Vie</th><th>Sáb</th><th>Dom</th></tr></thead>
<tbody>{"".join(f"<tr><th>{t}</th>" + "<td></td>"*7 + "</tr>" for t in TRACK)}</tbody></table>
<div class="cols2 keep notes">
<div><h3>Lo que me funcionó esta semana</h3><div class="lines"></div></div>
<div><h3>Lo que voy a ajustar la próxima</h3><div class="lines"></div></div>
</div>
''', chapter="09 · Seguimiento de hábitos", pid="cap9", toc="09 · Seguimiento de hábitos")

# ================================================================== CAP 10 SOSTENER
if FULL:
    page(f'''
{chap_head("10", 'Cómo sostener <span class="t">los resultados</span>', "Ser constante no es no fallar: es volver rápido cuando algo se desordena.")}
<div class="cols2">
<div>
<h3>Semanas complicadas o viajes</h3>
<p>Bajá el plan en lugar de suspenderlo: sesiones de 20 minutos, que podés hacer hasta en un hotel, y comidas simples.</p>
<h3>Fines de semana</h3>
<p>Disfrutá sin compensar después. Mantené el desayuno o una caminata como ancla.</p>
</div>
<div>
<h3>Cómo retomar</h3>
{ul(["Volvé en la próxima oportunidad, no “el lunes”.","Empezá con la mitad: 2 vueltas y comidas simples.","No compenses con ejercicio extra ni comiendo menos."])}
<h3>Cuándo pedir ayuda</h3>
<p>Si no lográs sostener los cambios o tenés una lesión o condición médica, un acompañamiento personalizado te ayuda a ajustar el plan.</p>
</div>
</div>
<h2>Tu plan mínimo para semanas difíciles</h2>
<div class="minplan">
<div><span>Entrenamiento</span><p>1 o 2 sesiones de 20 minutos y caminatas cortas.</p></div>
<div><span>Alimentación</span><p>Desayuno resuelto, una vianda simple y cenas que repetís.</p></div>
<div><span>Descanso</span><p>Mismo horario para levantarte y 30 minutos sin pantallas.</p></div>
<div><span>Registro</span><p>Un tilde por día en la planilla, aunque sea uno solo.</p></div>
</div>
''', chapter="10 · Cómo sostener los resultados", pid="cap10", toc="10 · Cómo sostener los resultados")

# ================================================================== TALLERES
TEAM_IMG = ('<img src="' + LINKS["foto_equipo"] + '" alt="Equipo RENOVA">') if LINKS["foto_equipo"] else '<div class="team-ph">FOTO DEL EQUIPO RENOVA</div>'
TEAM_VIDEO = (('<a class="vbtn-sm" href="' + esc(LINKS["video_talleres"]) + '">' + ICON_PLAY + ' VER VIDEO DE LOS TALLERES</a>') if LINKS["video_talleres"]
              else ('<span class="vbtn-sm">' + ICON_PLAY + ' VER VIDEO DE LOS TALLERES</span>'))
if ENT:
    page(f'''
{eyebrow("BONUS 2 · INCLUIDO")}
<h1 class="h1 big">Dos talleres <span class="t">incluidos</span></h1>
<p class="lead">Con este ebook accedés a dos talleres del equipo RENOVA para sumar herramientas a tu entrenamiento y a tu semana.</p>
<div class="wgrid">
  <div class="wcard"><span class="wtag">TALLER INCLUIDO</span><h3>Descanso</h3><p>Estrategias para mejorar tu descanso y tu recuperación entre entrenamientos.</p></div>
  <div class="wcard"><span class="wtag">TALLER INCLUIDO</span><h3>Organización de alimentos en la heladera</h3><p>Cómo guardar, porcionar y ordenar para tener siempre opciones listas.</p></div>
</div>
<p class="small">Además, en RENOVA vas a encontrar más talleres, como <b>Fines de semana</b> y <b>Mindfulness</b>, para seguir avanzando.</p>
<div class="team">
  {TEAM_IMG}
  <div class="team-tx">
    <span class="wtag">EQUIPO RENOVA</span>
    <p>Los talleres están a cargo del equipo RENOVA: entrenadores, médico deportólogo, psicólogo y nutricionista. Abordan los hábitos clave que sostienen el cambio en la vida real.</p>
    {TEAM_VIDEO}
  </div>
</div>
<div class="cta-center">{button("ACCEDER A MIS TALLERES", "talleres", "[INSERTAR LINK REAL DE ACCESO A TALLERES]", big=True)}</div>
''', chapter="Bonus 2 · Talleres", pid="talleres", cls="p-spread", toc="Bonus 2: Talleres RENOVA")

if FULL:
    page(f'''
{eyebrow("TALLERES RENOVA")}
<h1 class="h1 big">Seguí avanzando <span class="t">con RENOVA</span></h1>
<p class="lead">Accedé a los talleres para profundizar en entrenamiento, nutrición, descanso y hábitos. Encontrá herramientas prácticas para aplicar lo aprendido a tu vida cotidiana.</p>
<div class="wgrid">
  <div class="wcard"><span class="wtag">TALLER</span><h3>Descanso</h3><p>Estrategias para mejorar tu descanso y tu recuperación.</p></div>
  <div class="wcard"><span class="wtag">TALLER</span><h3>Organización de alimentos en la heladera</h3><p>Cómo guardar, porcionar y ordenar para tener siempre opciones listas.</p></div>
  <div class="wcard"><span class="wtag">TALLER</span><h3>Fines de semana</h3><p>Cómo disfrutar sin perder lo construido durante la semana.</p></div>
  <div class="wcard"><span class="wtag">TALLER</span><h3>Mindfulness</h3><p>Herramientas de atención plena aplicadas a la alimentación y los hábitos.</p></div>
</div>
<div class="team">
  {('<img src="' + LINKS["foto_equipo"] + '" alt="Equipo RENOVA">') if LINKS["foto_equipo"] else '<div class="team-ph">FOTO DEL EQUIPO RENOVA</div>'}
  <div class="team-tx">
    <span class="wtag">EQUIPO RENOVA</span>
    <p>Los talleres están a cargo del equipo RENOVA: entrenadores, médico deportólogo, psicólogo y nutricionista. Abordan los hábitos clave que sostienen el cambio en la vida real.</p>
    {('<a class="vbtn-sm" href="' + esc(LINKS["video_talleres"]) + '">' + ICON_PLAY + ' VER VIDEO DE LOS TALLERES</a>') if LINKS["video_talleres"] else ('<span class="vbtn-sm">' + ICON_PLAY + ' VER VIDEO DE LOS TALLERES</span>')}
  </div>
</div>
<div class="cta-center">{button("ACCEDER A LOS TALLERES", "talleres", "[INSERTAR LINK REAL DE ACCESO A TALLERES]", big=True)}</div>
''', chapter="Talleres", pid="talleres", cls="p-spread", toc="Talleres RENOVA")

page(f'''
<div class="bonus">
{eyebrow("BONUS EXCLUSIVO" if FULL else "BONUS 3 · INCLUIDO")}
<h1 class="h1 big">Consulta personalizada <span class="t">con Nacho</span></h1>
<p class="lead">Como complemento de esta guía, podés acceder a una consulta personalizada con Nacho para conversar sobre tus objetivos, revisar tus principales dificultades y orientar tus próximos pasos.</p>
<div class="cols2">
<div><h3>En la consulta vas a poder</h3>
{checks(["Contar tus objetivos y tu situación actual.","Revisar qué te está costando sostener.","Definir los próximos pasos con más claridad."])}
</div>
<div><h3>Para aprovecharla</h3>
{checks(["Completá antes un par de semanas de la planilla de seguimiento.","Anotá tus preguntas.","Tené a mano tu agenda semanal."])}
</div>
</div>
<div class="ctapanel">
  <p class="ctatitle">Reservá tu lugar</p>
  <p class="small center">Elegí el día y el horario que mejor te queden.</p>
  {button("RESERVAR MI CONSULTA CON NACHO", "consulta", "[INSERTAR LINK REAL DE RESERVA DE CONSULTA]", big=True)}
</div>
</div>
''', chapter="Bonus" if FULL else "Bonus 3 · Consulta", pid="bonus", cls="p-spread", toc="Bonus: consulta con Nacho" if FULL else "Bonus 3: Consulta con Nacho")

# ================================================================== FUENTES


# ================================================================== QUIÉN SOY
page(f'''
<div class="bio">
  <div class="bio-top">
    <div class="bio-photo"><img src="img/nacho_full.jpg" alt="Nacho Portillo"></div>
    <div>
      {eyebrow("QUIÉN SOY")}
      <h1 class="h1">Soy <span class="t">Nacho Portillo</span></h1>
      <p class="role">Licenciado en Alto Rendimiento Deportivo</p>
      <p>Hace más de 15 años trabajo en entrenamiento, rendimiento físico y transformación de hábitos. Mi experiencia en el ámbito deportivo y acompañando a personas con distintos objetivos me enseñó algo fundamental: no alcanza con tener un plan; necesitás un sistema que puedas sostener.</p>
      <p>Por eso, en RENOVA trabajamos sobre los pilares que influyen en tu progreso: entrenamiento de fuerza, nutrición, medicina deportiva, descanso y hábitos. El objetivo es ayudarte a organizar un método realista, adaptado a tus posibilidades y compatible con tu vida cotidiana.</p>
    </div>
  </div>
  <div class="what">
    <h2>¿Qué es <span class="t">Programa RENOVA</span>?</h2>
    <p>PROGRAMA RENOVA es un programa de acompañamiento que integra entrenamiento de fuerza, nutrición, medicina deportiva a cargo de nuestro médico deportólogo, descanso y gestión de hábitos para ayudarte a mejorar tu composición corporal y construir una rutina sostenible.</p>
    <p>No se trata de seguir una dieta extrema ni de entrenar sin estrategia. Se trata de organizar un proceso, aprender a tomar mejores decisiones y contar con herramientas que puedas mantener en el tiempo.</p>
    <div class="pills4"><span>Fuerza</span><span>Nutrición</span><span>Medicina deportiva</span><span>Descanso</span><span>Hábitos</span></div>
  </div>
  <div class="quote dark">No necesitás hacerlo perfecto. <span class="t2">Necesitás un sistema que puedas sostener.</span></div>
  <div class="cta-center">{button("CONOCÉ PROGRAMA RENOVA", "renova", "[INSERTAR LINK OFICIAL DE PROGRAMA RENOVA]", big=True)}</div>
</div>
''', chapter="Quién soy", pid="bio", toc="Quién soy y qué es RENOVA")

# ------------------------------------------------------------------ ENSAMBLADO
CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "style.css"), encoding="utf-8").read()

BRAND = "PROGRAMA <b>RENOVA</b>" if FULL else "ENTRENÁ DESDE CASA · <b>RENOVA</b>"
TITLE = "Programa RENOVA · Guía práctica" if FULL else "Entrená desde casa · RENOVA"
OUT_HTML = "ebook.html" if FULL else "entrena.html"

def render():
    if ENT:
        plan = [p for p in PAGES if p["id"].startswith("plan8")]
        rest = [p for p in PAGES if not p["id"].startswith("plan8")]
        at = next(i for i, p in enumerate(rest) if p["id"] == "cap2")
        PAGES[:] = rest[:at] + plan + rest[at:]
    order = {p["id"]: i for i, p in enumerate(PAGES)}
    TOC.sort(key=lambda t: order[t[1]])
    num = {p["id"]: i + 1 for i, p in enumerate(PAGES)}
    toc_html = '<div class="tocl">' + "".join(
        f'<a class="tocr" href="#{pid}"><span class="tt">{esc(t)}</span><span class="dots"></span><span class="pg">{num[pid]}</span></a>'
        for t, pid in TOC) + "</div>"
    out = []
    for i, p in enumerate(PAGES, 1):
        body = p["body"]
        if body == "__TOC__":
            body = f'{eyebrow("CONTENIDO")}<h1 class="h1">Índice</h1>{toc_html}'
        hdr = ""
        if p["header"]:
            hdr = (f'<div class="hdr"><span>{BRAND}</span><span>{esc(p["chapter"])}</span></div>'
                   f'<div class="ftr"><a class="toidx" href="#indice">{ICON_HAND} Hacé clic y volvé al índice</a><span class="pgnum"></span></div>')
        out.append(f'<section class="page {p["cls"]}" id="{p["id"]}">{hdr}<div class="body">{body}</div></section>')
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>' + TITLE + '</title>'
            f'<style>{CSS}</style></head><body>' + "".join(out) + '<script src="paginate.js"></script></body></html>')

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, OUT_HTML), "w", encoding="utf-8") as f:
        f.write(render())
    print(OUT_HTML, "·", len(PAGES), "páginas antes de paginar")
