"""Ebook upsell "Glúteos Fuertes": el día extra de RENOVA.
Un día de entrenamiento por semana dedicado a glúteos y cadera, que se suma a las rutinas del Método RENOVA
(si entrenás 2 veces, es tu tercer día; si entrenás 3, el cuarto). 8 semanas, en casa o en el gimnasio.
Para la mujer RENOVA 40+: glúteo fuerte = cadera, rodillas y espalda sanas, postura, y también estética.
Sin promesas de centímetros: el progreso se mide con el test del día 1 contra el de la semana 8.

Usa solo ejercicios que ya tienen ilustración (img/) y video de Harbiz en los ebooks de casa y gimnasio.

Uso:  cd fuentes/ebook && python3 gluteos.py && node export.js gluteos
      → gluteos-fuertes/Ebook_Gluteos_Fuertes_RENOVA.pdf
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "design-system"))
from design_system import (css as ds_css, esc, ICON_ARROW, ICON_HAND, ICON_PLAY, eyebrow, chap_head, ul, checks,
                           box, block_head, params, DESCARGO)

LINK_PLAN = "https://wa.link/hewha8"     # WhatsApp de Nacho: plan integral con 50% off (igual que LINKS["wa_plan"] de build.py)
LINK_RENOVA = "https://wa.link/1asjt1"   # WhatsApp: Programa RENOVA integral (igual que LINKS["renova"])
PAGES, TOC = [], []


def page(body, chapter="", pid=None, cls="", toc=None, header=True):
    pid = pid or f"p{len(PAGES) + 1}"
    PAGES.append(dict(id=pid, chapter=chapter, body=body, cls=cls, header=header))
    if toc:
        TOC.append((toc, pid))


def table(head, rows, first=None):
    """first: ancho de la primera columna (por ejemplo "30%"), para planillas con muchas columnas."""
    th = "".join((f'<th style="width:{first}">' if first and i == 0 else "<th>") + f"{h}</th>" for i, h in enumerate(head))
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="grid-t ntab"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def pref(pid):
    """Número de página de otra hoja (lo completa paginate.js)."""
    return f'<span class="pref" data-ref="{pid}"></span>'


# ------------------------------------------------------------------ EJERCICIOS
# Videos de Harbiz que ya usan los ebooks de casa y gimnasio (build.py: VIDEOS y su versión GYM).
VIDEOS = {
    "Almeja": "https://youtu.be/9ayi-DrA98o",
    "Puente de glúteos": "https://youtu.be/YopfscyxtK0",
    "Bird dog con pausa": "https://youtu.be/kyNrWqz1iqs",
    "Abducción de pierna de pie": "https://youtu.be/4C0pyUW9DaQ",
    "Abducción en máquina": "https://youtu.be/fyVNH7X5wv4",
    "Hip thrust en sillón": "https://youtu.be/dLX0Uob8y4k",
    "Hip thrust con barra": "https://youtu.be/dLX0Uob8y4k",
    "Prensa con pies altos": "https://youtu.be/ddfmGBWmB88",
    "Subida al banco": "https://youtu.be/CMlvRdB7dIk",
    "Estocada split con mancuernas": "https://youtu.be/JOQYcHKf83I",
    "Peso muerto con mancuernas": "https://youtu.be/MeXBpLzezlw",
    "Peso muerto rumano con mancuernas": "https://youtu.be/W5FS9E0Lib4",
    "Sentadilla sumo": "https://youtu.be/Ro3dhcOXiYw",
    "Puente a una pierna": "https://youtu.be/xVvVhmIp7sM",
    "Estocada cruzada": "https://youtu.be/5yYgxASNwZ8",
    "Curl de isquiotibiales sentada": "https://youtu.be/8I7lYLxvAf0",
}

# (imagen, nombre, dosis, cómo se hace, cuidá, más fácil, material)
EJ = {
    "Almeja": ("calor_4.png", "Almeja", "15 por lado",
               "De costado, rodillas flexionadas y pies juntos. Abrí la rodilla de arriba sin mover la pelvis y bajá lento.",
               "la cadera no rota hacia atrás.", "menos apertura.", "Colchoneta"),
    "Puente de glúteos": ("calor_5.png", "Puente de glúteos", "15",
                          "Boca arriba, pies apoyados. Empujá con los talones, subí la cadera y apretá glúteos 2 s arriba.",
                          "no arquees la zona lumbar.", "subí solo unos centímetros.", "Colchoneta"),
    "Bird dog con pausa": ("calor_6.png", "Bird dog con pausa", "8 por lado",
                           "En cuatro apoyos, estirá un brazo y la pierna contraria. Sostené 3 s apretando el glúteo y alterná.",
                           "la espalda no gira.", "mové solo la pierna.", "Colchoneta"),
    "Abducción de pierna de pie": ("calor_2.png", "Abducción de pierna de pie", "15 por lado",
                                   "Apoyada en una silla, llevá la pierna al costado sin inclinar el tronco y volvé con control.",
                                   "el pie mira hacia adelante.", "menos apertura.", "Silla (banda opcional)"),
    "Abducción en máquina": ("gym_abduccion.png", "Abducción en máquina", "15",
                             "Sentada, piernas en los apoyos externos. Abrí con fuerza de glúteo y cerrá despacio.",
                             "el regreso es lento, sin rebote.", "menos peso.", "Máquina"),
    "Hip thrust en sillón": ("gym_hipthrust.png", "Hip thrust en sillón", "10–12",
                             "Espalda alta apoyada en el sillón y mancuerna sobre la cadera. Empujá con los talones hasta alinear el torso y apretá glúteos arriba.",
                             "mentón al pecho, costillas abajo.", "sin peso o puente en el piso.", "Sillón y 1 mancuerna"),
    "Hip thrust con barra": ("gym_hipthrust.png", "Hip thrust con barra", "10–12",
                             "Espalda alta en el banco y barra sobre la cadera, con almohadilla. Empujá con los talones hasta alinear el torso y apretá glúteos arriba.",
                             "mentón al pecho, empujá con talones.", "con disco o sin peso.", "Banco y barra"),
    "Prensa con pies altos": ("gym_prensa.png", "Prensa con pies altos", "10–12",
                              "Pies arriba en la plataforma y un poco más abiertos que la cadera. Bajá a 90° y empujá con los talones.",
                              "la zona lumbar queda apoyada.", "menos peso y menos recorrido.", "Máquina"),
    "Subida al banco": ("r2_1.png", "Subida al banco", "10 por lado",
                        "Pie entero arriba del escalón. Subí empujando con esa pierna, sin impulsarte con la de abajo, y bajá lento.",
                        "la rodilla sigue la línea del pie.", "escalón más bajo.", "Escalón o silla firme"),
    "Estocada split con mancuernas": ("r1_2_mancuernas.png", "Estocada split con mancuernas", "10 por lado",
                                      "Un pie adelante y otro atrás. Bajá la rodilla de atrás con el tronco un poco inclinado hacia adelante y subí con la pierna de adelante.",
                                      "rodilla de adelante alineada.", "sin peso o con apoyo.", "2 mancuernas"),
    "Peso muerto con mancuernas": ("r3_5b.png", "Peso muerto rumano", "10–12",
                                   "Rodillas apenas flexionadas. Llevá la cadera hacia atrás bajando las mancuernas pegadas a las piernas hasta sentir los isquiotibiales, y subí apretando glúteos.",
                                   "espalda recta, no redondees.", "menos recorrido.", "2 mancuernas"),
    "Peso muerto rumano con mancuernas": ("r3_5b.png", "Peso muerto rumano", "10–12",
                                          "Rodillas apenas flexionadas. Llevá la cadera hacia atrás bajando las mancuernas pegadas a las piernas y subí apretando glúteos.",
                                          "espalda recta, no redondees.", "menos peso y recorrido.", "2 mancuernas o barra"),
    "Sentadilla sumo": ("r3_3.png", "Sentadilla sumo", "12",
                        "Pies bien abiertos y puntas hacia afuera, mancuerna entre las piernas. Bajá con el torso alto y subí empujando el piso.",
                        "rodillas hacia las puntas.", "sin peso o a una silla.", "1 mancuerna"),
    "Puente a una pierna": ("r1_4.png", "Puente a una pierna", "10 por lado",
                            "Boca arriba, un pie apoyado y la otra pierna estirada. Subí la cadera con el glúteo y bajá lento.",
                            "la pelvis no se cae de un lado.", "puente con los dos pies.", "Colchoneta"),
    "Estocada cruzada": ("r3_1.png", "Estocada cruzada", "10 por lado",
                         "Llevá una pierna atrás y en diagonal, como una reverencia, y bajá con control. Volvé empujando con la de adelante.",
                         "la cadera queda de frente.", "estocada hacia atrás sin cruzar.", "Propio cuerpo o mancuernas"),
    "Curl de isquiotibiales sentada": ("gym_curlisq.png", "Curl de isquiotibiales", "12",
                                       "Rodillas al borde del asiento. Flexioná bajando el rodillo y volvé con control.",
                                       "la cadera queda en el asiento.", "menos peso.", "Máquina"),
}


def card(key, dose=None):
    img, name, d, how, cuida, easy, mat = EJ[key]
    url = VIDEOS.get(key, "")
    vb = f'<a class="vbtn-sm" href="{esc(url)}">{ICON_PLAY} VER VIDEO</a>' if url else ""
    return (f'<div class="ex exrow"><div class="exl"><div class="exim"><img src="img/{img}" alt=""></div><span class="mat">{mat}</span></div>'
            f'<div class="extx"><div class="exh"><h4>{name}</h4><span class="dose">{dose or d}</span>{vb}</div>'
            f'<p>{how} <span class="ojo"><b>Cuidá:</b> {cuida}</span></p><p class="easy"><b>Más fácil:</b> {easy}</p></div></div>')


# Sesión → lugar → (activación, principal, complementario)
SES = {
    "A": {
        "casa": (["Almeja", "Puente de glúteos"], ["Hip thrust en sillón", "Subida al banco"], ["Abducción de pierna de pie", "Puente a una pierna"]),
        "gym": (["Abducción en máquina", "Puente de glúteos"], ["Hip thrust con barra", "Prensa con pies altos"], ["Subida al banco", "Estocada split con mancuernas"]),
    },
    "B": {
        "casa": (["Bird dog con pausa", "Abducción de pierna de pie"], ["Peso muerto con mancuernas", "Sentadilla sumo"], ["Estocada cruzada", "Almeja"]),
        "gym": (["Bird dog con pausa", "Abducción en máquina"], ["Peso muerto rumano con mancuernas", "Sentadilla sumo"], ["Estocada cruzada", "Curl de isquiotibiales sentada"]),
    },
}
FOCO = {"A": "empuje de cadera y una pierna", "B": "bisagra de cadera y apertura"}
LUGAR = {"casa": ("EN CASA", "Mancuernas, sillón o banco, escalón o silla, colchoneta"),
         "gym": ("EN EL GIMNASIO", "Banco y barra, prensa, mancuernas, máquinas")}

# ================================================================== PORTADA
page('''
<div class="cv3 glut">
  <div class="c3-in">
    <img class="c3-logo" src="img/logo_renova.png" alt="RENOVA">
    <span class="c3-pill">MÉTODO RENOVA · MUJERES 40+</span>
    <h1 class="c3-title">GLÚTEOS<br>FUERTES</h1>
    <p class="c3-claim">TU DÍA EXTRA, <b><span>8 SEMANAS.</span></b></p>
    <p class="c3-sub">Fortalecé <b>glúteos</b> y <em>cadera</em> con un plan claro,<br><span>en <mark>casa</mark> o en el <mark>gimnasio</mark>.</span></p>
  </div>
  <div class="c3-team"><img src="img/equipo_tapa.png" alt="Equipo RENOVA"></div>
</div>
''', pid="portada", cls="p-cover", header=False)

# ================================================================== BIENVENIDA
page(f'''
{eyebrow("BIENVENIDA")}
<h1 class="h1">Tu día extra <span class="t">de RENOVA</span></h1>
<p class="lead">Glúteos Fuertes es <b>un día de entrenamiento por semana</b> dedicado a glúteos y cadera. No reemplaza tus rutinas del Método RENOVA: se suma a lo que ya hacés.</p>
{table(["Si entrenás…", "Glúteos Fuertes es…"], [
 ["<b>2 veces por semana</b> con RENOVA", "tu <b>tercer día</b>"],
 ["<b>3 veces por semana</b> con RENOVA", "tu <b>cuarto día</b>"],
])}
<h2>Cómo es cada sesión</h2>
{checks(["<b>Unos 40 minutos:</b> activación, bloque principal y bloque complementario.",
         "<b>Dos sesiones que se alternan:</b> la A (empuje de cadera) y la B (bisagra de cadera).",
         "<b>En casa o en el gimnasio:</b> cada sesión tiene las dos versiones. Elegí una o combiná según la semana.",
         "<b>8 semanas,</b> igual que el método, para que avancen juntos."])}
{box("<b>Dejá al menos un día entre esta sesión y la rutina de RENOVA</b> que más trabaja piernas. Así llegás descansada y el músculo se recupera.", "soft")}
''', chapter="Bienvenida", pid="bienvenida")

page("__TOC__", chapter="Índice", pid="indice")

# ================================================================== 01
page(f'''
{chap_head("01", 'Por qué el glúteo <span class="t">importa después de los 40</span>', "No es solo estética: es el músculo que sostiene tu cadera, protege tus rodillas y cuida tu espalda.")}
<h2>Tres músculos, tres funciones</h2>
{table(["Músculo", "Qué hace", "Lo usás cuando…"], [
 ["<b>Glúteo mayor</b>", "Extiende la cadera: te empuja hacia adelante y hacia arriba.", "Subís una escalera, te levantás de una silla, caminás en subida."],
 ["<b>Glúteo medio</b>", "Estabiliza la pelvis y abre la pierna al costado.", "Caminás, te parás en una pierna, bajás un escalón."],
 ["<b>Glúteo menor</b>", "Ayuda al medio a mantener la cadera firme.", "En cada paso, sin que te des cuenta."],
])}
<h2>Qué ganás con un glúteo fuerte</h2>
<div class="tips10 t3">
  <div><span>01</span><h3>Cadera y rodillas</h3><p>Un glúteo medio débil deja que la rodilla se vaya hacia adentro. Fortalecerlo ordena el movimiento.</p></div>
  <div><span>02</span><h3>Espalda baja</h3><p>Si el glúteo no empuja, la zona lumbar compensa. Un glúteo fuerte le saca carga.</p></div>
  <div><span>03</span><h3>Equilibrio</h3><p>Pararte firme en una pierna es la base para caminar seguro y prevenir caídas.</p></div>
</div>
{box("<b>Después de los 40 se pierde músculo</b> si no hay estímulo de fuerza, y en la menopausia la pérdida se acelera. El glúteo es uno de los músculos más grandes del cuerpo: entrenarlo es cuidar tu fuerza para los próximos años.", "")}
''', chapter="01 · Por qué el glúteo", pid="c1", toc="01 · Por qué el glúteo importa")

# ================================================================== 02
page(f'''
{chap_head("02", 'Cómo se fortalece <span class="t">un músculo</span>', "Tres claves explican casi todo. Si las cumplís, el músculo responde a cualquier edad.")}
<div class="tips10 t3">
  <div><span>01</span><h3>Esfuerzo suficiente</h3><p>Las últimas repeticiones tienen que costar. Si terminás fresca, el músculo no tiene motivo para cambiar.</p></div>
  <div><span>02</span><h3>Constancia</h3><p>Un día por semana, todas las semanas, suma más que tres días una semana y ninguno la siguiente.</p></div>
  <div><span>03</span><h3>Progresión</h3><p>Cada pocas semanas, un poco más: más peso, más repeticiones o más series.</p></div>
</div>
<h2>Con qué esfuerzo: la escala del 1 al 10</h2>
{table(["Esfuerzo", "Cómo se siente", "Cuándo"], [
 ["<b>5 – 6</b>", "Podrías hacer 4 o 5 repeticiones más.", "Semanas 1 y 2, y semana 5 (descarga)."],
 ["<b>7</b>", "Podrías hacer 3 más. Las últimas cuestan.", "Semanas 3 y 4."],
 ["<b>8</b>", "Podrías hacer 2 más, con buena técnica.", "Semanas 6 a 8."],
])}
<p>Nunca hace falta llegar a no poder más. <b>Primero la técnica, después el peso.</b></p>
{box("<b>El músculo crece cuando descansás.</b> Dormir bien y comer proteína suficiente son parte del entrenamiento (capítulo 07).", "soft")}
''', chapter="02 · Cómo se fortalece", pid="c2", toc="02 · Cómo se fortalece un músculo")

# ================================================================== 03
page(f'''
{chap_head("03", 'Tu test <span class="t">del día 1</span>', "Antes de la primera sesión, medí tu punto de partida. En la semana 8 lo repetís y ves cuánto avanzaste.")}
<h2>Los tres tests</h2>
{ul(["<b>Puente a una pierna:</b> cuántas repeticiones hacés seguidas con cada pierna, con buena técnica (sin que la pelvis se caiga).",
     "<b>Sentadilla a la silla en 30 segundos:</b> cuántas veces te sentás y te parás sin usar las manos.",
     "<b>Equilibrio en una pierna:</b> cuántos segundos te sostenés en cada pierna, con los brazos cruzados (hasta 30 s)."])}
{table(["Test", "Día 1", "Semana 8"], [
 ["Puente a una pierna · derecha", "", ""],
 ["Puente a una pierna · izquierda", "", ""],
 ["Sentadilla a la silla (30 s)", "", ""],
 ["Equilibrio · derecha (s)", "", ""],
 ["Equilibrio · izquierda (s)", "", ""],
 ["Contorno de cadera (cm)", "", ""],
])}
<p class="small"><b>Contorno de cadera:</b> medí en la parte más saliente de los glúteos, de pie y con los pies juntos. Si querés, sacate una foto de perfil con la misma luz y la misma ropa.</p>
{box("<b>Tu primera victoria:</b> con hacer el test ya empezaste. Anotá los números aunque te parezcan bajos: son tu punto de partida, no una nota.", "soft")}
''', chapter="03 · Tu test", pid="test", toc="03 · Tu test del día 1")

# ================================================================== 04
page(f'''
{chap_head("04", 'Cómo <span class="t">progresar</span>', "Una regla simple para saber cuándo subir el peso, sin adivinar.")}
<h2>La regla del rango de repeticiones</h2>
<p>Cada ejercicio tiene un rango, por ejemplo <b>10 a 12</b>. Empezá con un peso que te permita hacer 10 con el esfuerzo de la semana.</p>
<ol class="steps-ol">
<li>Cuando hagas <b>12 en todas las series</b> con buena técnica, la sesión siguiente subí un poco el peso.</li>
<li>Con el peso nuevo vas a volver a hacer 10. Está perfecto.</li>
<li>Vas sumando repeticiones de a poco hasta llegar otra vez a 12.</li>
</ol>
{table(["Si…", "Hacé esto"], [
 ["Hiciste el tope del rango en todas las series", "Subí el peso: 1 a 2 kg en mancuernas, 2,5 a 5 kg en barra o máquina."],
 ["Te quedaste dentro del rango", "Mantené el peso e intentá sumar una repetición."],
 ["No llegaste al mínimo o perdiste la técnica", "Bajá un poco el peso."],
 ["Te dolió una articulación (no es cansancio)", "Pará ese ejercicio y usá la opción más fácil."],
])}
{box(f"<b>Anotá cada sesión</b> en tu planilla de cargas (página {pref('cargas')}). Sin registro no sabés si progresás.", "soft")}
''', chapter="04 · Cómo progresar", pid="c4", toc="04 · Cómo progresar")

# ================================================================== 05 · SESIONES
page(f'''
{chap_head("05", 'Tus <span class="t">sesiones</span>', "Dos sesiones que se alternan semana a semana, cada una en versión casa y gimnasio.")}
{table(["Sesión", "Foco", "Casa", "Gimnasio"], [
 ["<b>A</b>", "Empuje de cadera y una pierna", f"página {pref('a-casa')}", f"página {pref('a-gym')}"],
 ["<b>B</b>", "Bisagra de cadera y apertura", f"página {pref('b-casa')}", f"página {pref('b-gym')}"],
])}
<h2>Cómo se hace cada sesión</h2>
{table(["Parte", "Qué es", "Cómo"], [
 ["<b>Activación</b>", "Despierta el glúteo antes de cargar.", "2 vueltas seguidas de los 2 ejercicios, sin peso."],
 ["<b>Bloque principal</b>", "Los ejercicios más pesados.", "Series según el plan (página " + pref("plan") + "). Descanso 90 s entre series."],
 ["<b>Complementario</b>", "Trabajo de una pierna y glúteo medio.", "Series según el plan. Descanso 60 s."],
 ["<b>Elongación</b>", "Para cerrar.", "La elongación de tu ebook RENOVA, 5 minutos."],
])}
{box("<b>Antes de la activación,</b> caminá o pedaleá 5 minutos para entrar en calor.", "soft")}
''', chapter="05 · Sesiones", pid="c5", toc="05 · Tus sesiones")

ORDEN = [("A", "casa"), ("A", "gym"), ("B", "casa"), ("B", "gym")]
for s, lugar in ORDEN:
    act, prin, comp = SES[s][lugar]
    tag, mat = LUGAR[lugar]
    page(f'''
{eyebrow(f"SESIÓN {s} · {tag}")}
<h1 class="h1">Sesión {s}: <span class="t">{FOCO[s]}</span></h1>
{params([("Duración", "40 min"), ("Sesión", s), ("Lugar", "Casa" if lugar == "casa" else "Gimnasio"), ("Material", mat.split(",")[0])])}
<p class="small"><b>Material:</b> {mat}. Las series, repeticiones y el esfuerzo de cada semana están en el plan (página {pref("plan")}).</p>
{block_head("ACTIVACIÓN", "2 vueltas · sin peso · sin descanso entre ejercicios")}
{"".join(card(k) for k in act)}
{block_head("BLOQUE PRINCIPAL", "series del plan · descanso 90 s")}
{"".join(card(k) for k in prin)}
{block_head("COMPLEMENTARIO", "series del plan · descanso 60 s")}
{"".join(card(k) for k in comp)}
''', chapter=f"05 · Sesión {s}", pid=f"{s.lower()}-{lugar}", toc=f"Sesión {s} · {tag.lower()}")

# ================================================================== 06 · PLAN
page(f'''
{chap_head("06", 'Tu plan de <span class="t">8 semanas</span>', "Igual que el Método RENOVA: base, descarga y progresión.")}
{table(["Semana", "Sesión", "Principal", "Complementario", "Esfuerzo"], [
 ["<b>1</b>", "A", "3 × 12", "2 × 10", "5 – 6"],
 ["<b>2</b>", "B", "3 × 12", "2 × 10", "5 – 6"],
 ["<b>3</b>", "A", "3 × 10 – 12", "3 × 10", "7"],
 ["<b>4</b>", "B", "3 × 10 – 12", "3 × 10", "7"],
 ["<b>5 · descarga</b>", "A", "2 × 10, peso liviano", "2 × 10", "5"],
 ["<b>6</b>", "B", "4 × 8 – 10", "3 × 10", "8"],
 ["<b>7</b>", "A", "4 × 8 – 10", "3 × 10", "8"],
 ["<b>8</b>", "B + test", "4 × 8 – 10", "3 × 10", "8"],
])}
<p class="small">“3 × 12” = 3 series de 12 repeticiones. En los ejercicios de una pierna, las repeticiones son por lado. La activación es siempre igual: 2 vueltas.</p>
<h2>Las tres etapas</h2>
<div class="tips10 t3">
  <div><span>1–4</span><h3>Aprendé y construí</h3><p>Técnica primero. A partir de la semana 3, empezá a subir el peso.</p></div>
  <div><span>5</span><h3>Descarga</h3><p>Menos series y menos peso. El cuerpo asimila lo que hiciste.</p></div>
  <div><span>6–8</span><h3>Progresá</h3><p>Más series, menos repeticiones y más peso. Al final, repetí el test.</p></div>
</div>
''', chapter="06 · Plan", pid="plan", toc="06 · Tu plan de 8 semanas")

page(f'''
{eyebrow("TU PLAN DE 8 SEMANAS")}
<h1 class="h1">Cómo encaja <span class="t">en tu semana</span></h1>
<h2>Si entrenás 2 veces con RENOVA</h2>
{table(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"], [["RENOVA", "–", "Glúteos", "–", "RENOVA", "Caminata", "–"]])}
<h2>Si entrenás 3 veces con RENOVA</h2>
{table(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"], [["RENOVA", "–", "RENOVA", "Glúteos", "–", "RENOVA", "–"]])}
<p class="small">Son ejemplos: mové los días según tu semana. Lo importante es no hacer Glúteos Fuertes el día antes o el día después de la rutina que más trabaja piernas.</p>
{box("<b>¿Perdiste una semana?</b> No pasa nada. Retomá con la sesión que te tocaba y el esfuerzo de la semana anterior. No intentes recuperar haciendo dos sesiones juntas.", "soft")}
''', chapter="06 · Plan", pid="plan2")

# ================================================================== 07 · ERRORES
page(f'''
{chap_head("07", 'Errores que frenan <span class="t">tu progreso</span>', "Los más frecuentes, y cómo corregirlos.")}
<div class="mitos">
  <div><b>Sentir todo en los cuádriceps</b><p>En el hip thrust y el puente, acercá los pies a la cola hasta que las canillas queden verticales arriba. Empujá con los talones.</p></div>
  <div><b>Arquear la espalda arriba</b><p>En el hip thrust, el movimiento termina cuando la cadera se alinea con el torso. Mentón al pecho y costillas abajo.</p></div>
  <div><b>Bajar rápido</b><p>La bajada también entrena. Contá 2 o 3 segundos para bajar en cada repetición.</p></div>
  <div><b>Subir peso antes de dominar la técnica</b><p>Si el peso te cambia el movimiento, es demasiado. Usá la regla del rango (capítulo 04).</p></div>
  <div><b>Quedarse siempre con el mismo peso</b><p>Si hace tres semanas que hacés lo mismo con facilidad, el músculo ya se adaptó. Toca subir.</p></div>
  <div><b>No descansar entre series</b><p>En el bloque principal, 90 segundos. Apurarte te hace levantar menos y progresar menos.</p></div>
</div>
''', chapter="07 · Errores", pid="c7", toc="07 · Errores frecuentes")

# ================================================================== 08 · ALIMENTACIÓN
page(f'''
{chap_head("08", 'Comer para <span class="t">construir músculo</span>', "El entrenamiento da la señal; la alimentación pone los materiales.")}
<h2>Tres claves</h2>
{checks(["<b>Proteína en cada comida:</b> huevo, lácteos, carnes, pollo, pescado, legumbres, tofu. Repartida en el día rinde más que concentrada en la cena.",
         "<b>No entrenes en ayunas largas:</b> una comida o colación 1 a 3 horas antes te da energía para levantar más.",
         "<b>Después de entrenar,</b> una comida con proteína ayuda a la recuperación. No hace falta que sea inmediata."])}
{table(["Momento", "Ideas"], [
 ["Antes de entrenar", "Yogur con fruta, tostada con queso, banana con un puñado de frutos secos"],
 ["Después de entrenar", "Huevos con verduras, pollo o pescado con arroz y ensalada, legumbres"],
])}
{box("<b>Comer muy poco frena el músculo.</b> Si estás haciendo un plan para bajar de peso, no recortes la proteína. Las cantidades para vos las define tu nutricionista.", "note")}
<p class="small">En <b>Alimentación Inteligente</b> tenés 8 semanas de menús y recetas para organizar tus comidas.</p>
''', chapter="08 · Alimentación", pid="c8", toc="08 · Comer para construir músculo")

# ================================================================== BONUS EXPRESS
page(f'''
{eyebrow("BONUS · SEMANAS CARGADAS")}
<h1 class="h1">Sesión express <span class="t">de 20 minutos</span></h1>
<p class="lead">Para las semanas con poco tiempo. Mejor 20 minutos que nada: mantenés el hábito y el estímulo.</p>
{block_head("EN CASA", "3 vueltas · 12 repeticiones · 30 s de descanso entre vueltas")}
{card("Puente de glúteos", "12")}{card("Peso muerto con mancuernas", "12")}{card("Subida al banco", "10 por lado")}
{block_head("EN EL GIMNASIO", "3 vueltas · 12 repeticiones · 30 s de descanso entre vueltas")}
{card("Hip thrust con barra", "12")}{card("Abducción en máquina", "15")}{card("Estocada split con mancuernas", "10 por lado")}
''', chapter="Bonus · Express", pid="express", toc="Bonus: sesión express de 20 min")

# ================================================================== PLANILLA
CARGAS = ["Hip thrust", "Subida al banco / prensa", "Peso muerto rumano", "Sentadilla sumo", "Estocada", "Abducción / puente a una pierna"]
page(f'''
{eyebrow("HERRAMIENTA")}
<h1 class="h1">Tu planilla <span class="t">de cargas</span></h1>
<p class="small">Anotá el peso (kg) y las repeticiones de la última serie. Ejemplo: <b>8 kg × 12</b>.</p>
{table(["Ejercicio"] + [f"S{i}" for i in range(1, 9)], [[e] + [""] * 8 for e in CARGAS], first="30%")}
<h2>Cómo me sentí</h2>
{table(["Semana"] + [f"S{i}" for i in range(1, 9)], [["Energía (1 a 5)"] + [""] * 8, ["Dolor muscular (1 a 5)"] + [""] * 8], first="30%")}
''', chapter="Herramientas", pid="cargas", toc="Herramienta: planilla de cargas")

# ================================================================== DESPUÉS
page(f'''
{eyebrow("DESPUÉS DE LAS 8 SEMANAS")}
<h1 class="h1">Repetí el test <span class="t">y elegí cómo seguir</span></h1>
<p>En la semana 8 repetí los tres tests y la medida de cadera (página {pref("test")}). Compará con tu día 1: más repeticiones y más segundos en una pierna son fuerza que ganaste.</p>
<div class="tips10 t3">
  <div><span>1</span><h3>Subí la carga</h3><p>Repetí las 8 semanas empezando con los pesos de la semana 8.</p></div>
  <div><span>2</span><h3>Mantené</h3><p>Seguí con un día por semana alternando A y B, con esfuerzo 7.</p></div>
  <div><span>3</span><h3>Plan a tu medida</h3><p>Pedí un plan integral armado para vos (abajo).</p></div>
</div>
<p class="small">{DESCARGO}</p>
''', chapter="Después", pid="despues", toc="Después de las 8 semanas")

page(f'''
<div class="bio metodo">
  {eyebrow("PLAN INTEGRAL RENOVA")}
  <h1 class="h1 big">50% off en tu plan <span class="t">integral RENOVA</span></h1>
  <div class="team-big"><img src="img/equipo2.jpg" alt="Equipo RENOVA" style="height:auto;max-height:110mm;object-fit:contain"></div>
  <p class="lead center">Por tener Glúteos Fuertes, tenés <b>50% off en el plan integral RENOVA</b> de entrenamiento y nutrición, armado para vos.</p>
  <div class="cp-pills"><span>✓ Entrenamiento a tu medida</span><span>✓ Nutrición para tu etapa</span><span>✓ Seguimiento de tu progreso</span></div>
  <div class="cta-center"><a class="btn btn-big" href="{esc(LINK_PLAN)}">QUIERO MI 50% OFF {ICON_ARROW}</a></div>
  <div class="cta-center"><a class="btn" href="{esc(LINK_RENOVA)}">QUIERO SUMARME A RENOVA {ICON_ARROW}</a></div>
  <div class="quote dark">Un glúteo fuerte no es un capricho. <span class="t2">Es tu base para moverte bien muchos años.</span></div>
</div>
''', chapter="Plan integral", pid="metodo", toc="50% off en tu plan integral")


def render():
    num = {p["id"]: i + 1 for i, p in enumerate(PAGES)}
    toc_html = '<div class="tocl tc">' + "".join(
        f'<a class="tocr" href="#{pid}"><span class="tt">{esc(t)}</span><span class="dots"></span><span class="pg">{num[pid]}</span></a>'
        for t, pid in TOC) + "</div>"
    out = []
    for p in PAGES:
        body = p["body"]
        if body == "__TOC__":
            body = (f'{eyebrow("CONTENIDO")}<div class="idxhead"><h1 class="h1">Índice</h1>'
                    f'<p class="idxtip">{ICON_HAND} Hacé clic donde quieras ir. Para volver al índice, abajo de cada página tenés el botón.</p></div>{toc_html}')
        hdr = ""
        if p["header"]:
            hdr = (f'<div class="hdr"><span>GLÚTEOS FUERTES · <b>RENOVA</b></span><span>{esc(p["chapter"])}</span></div>'
                   f'<div class="ftr"><a class="toidx" href="#indice">{ICON_HAND} Hacé clic y volvé al índice</a><span class="pgnum"></span></div>')
        out.append(f'<section class="page {p["cls"]}" id="{p["id"]}">{hdr}<div class="body">{body}</div></section>')
    css = ds_css(HERE) + "\n" + open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Glúteos Fuertes · RENOVA</title>'
            f'<style>{css}</style></head><body class="grande">' + "".join(out) + '<script src="paginate.js"></script></body></html>')


if __name__ == "__main__":
    with open(os.path.join(HERE, "gluteos.html"), "w", encoding="utf-8") as f:
        f.write(render())
    print("gluteos.html ·", len(PAGES), "páginas antes de paginar")
