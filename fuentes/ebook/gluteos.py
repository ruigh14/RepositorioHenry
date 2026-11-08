"""Upsell "Glúteos Fuertes": el día extra de RENOVA, en dos ebooks que se entregan juntos.
  python3 gluteos.py casa  → gluteos_casa.html → gluteos-fuertes/Ebook_Gluteos_Fuertes_Casa_RENOVA.pdf
  python3 gluteos.py gym   → gluteos_gym.html  → gluteos-fuertes/Ebook_Gluteos_Fuertes_Gimnasio_RENOVA.pdf
(después: node export.js gluteos_casa / gluteos_gym)

Un día de entrenamiento por semana dedicado a glúteos y cadera, que se suma a las rutinas del Método RENOVA
(si entrenás 2 veces, es tu tercer día; si entrenás 3, el cuarto). 8 semanas. Sesiones A (empuje de cadera) y
B (bisagra) que se alternan. Para la mujer RENOVA 40+: glúteo fuerte = cadera, rodillas y espalda sanas, postura,
y también estética. Sin promesas de centímetros: el progreso se mide con el test del día 1 contra el de la semana 8.

Cada hoja se arma completa a mano (sin cortes de paginate.js): ningún bloque queda partido entre dos hojas
y ninguna hoja queda con mucho espacio libre (revisar el FREE de export.js).
Usa solo ejercicios que ya tienen ilustración (img/) y video de Harbiz en los ebooks de casa y gimnasio.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "design-system"))
from design_system import (css as ds_css, esc, ICON_ARROW, ICON_HAND, ICON_PLAY, eyebrow, chap_head, ul, checks,
                           box, block_head, params, DESCARGO)

ED = sys.argv[1] if len(sys.argv) > 1 else "casa"
assert ED in ("casa", "gym"), "edición: casa o gym"
GYM = ED == "gym"


def G(casa, gym):
    return gym if GYM else casa


LUGAR = G("EN CASA", "EN EL GIMNASIO")
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


def tips(items, cls="", start=1):
    """Tarjetas numeradas: [(título, texto), ...]. start: número de la primera (para seguir la cuenta en otra hoja)."""
    return f'<div class="tips10 {cls}">' + "".join(
        f'<div><span>{i:02d}</span><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(items, start)) + "</div>"


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
    "Peso muerto rumano con barra": "https://youtu.be/W5FS9E0Lib4",
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
                        "la rodilla sigue la línea del pie.", "escalón más bajo.", G("Escalón o silla firme", "Cajón y mancuernas")),
    "Estocada split con mancuernas": ("r1_2_mancuernas.png", "Estocada split con mancuernas", "10 por lado",
                                      "Un pie adelante y otro atrás. Bajá la rodilla de atrás con el tronco un poco inclinado hacia adelante y subí con la pierna de adelante.",
                                      "rodilla de adelante alineada.", "sin peso o con apoyo.", "2 mancuernas"),
    "Peso muerto con mancuernas": ("r3_5b.png", "Peso muerto rumano", "10–12",
                                   "Rodillas apenas flexionadas. Llevá la cadera hacia atrás bajando las mancuernas pegadas a las piernas hasta sentir los isquiotibiales, y subí apretando glúteos.",
                                   "espalda recta, no redondees.", "menos recorrido.", "2 mancuernas"),
    "Peso muerto rumano con barra": ("r3_5b.png", "Peso muerto rumano con barra", "10–12",
                                     "Rodillas apenas flexionadas. Llevá la cadera hacia atrás bajando la barra pegada a las piernas y subí apretando glúteos.",
                                     "espalda recta, no redondees.", "mancuernas o menos peso.", "Barra o mancuernas"),
    "Sentadilla sumo": ("r3_3.png", "Sentadilla sumo", "12",
                        "Pies bien abiertos y puntas hacia afuera, mancuerna entre las piernas. Bajá con el torso alto y subí empujando el piso.",
                        "rodillas hacia las puntas.", "sin peso o a una silla.", G("1 mancuerna", "Mancuerna o pesa rusa")),
    "Puente a una pierna": ("r1_4.png", "Puente a una pierna", "10 por lado",
                            "Boca arriba, un pie apoyado y la otra pierna estirada. Subí la cadera con el glúteo y bajá lento.",
                            "la pelvis no se cae de un lado.", "puente con los dos pies.", "Colchoneta"),
    "Estocada cruzada": ("r3_1.png", "Estocada cruzada", "10 por lado",
                         "Llevá una pierna atrás y en diagonal, como una reverencia, y bajá con control. Volvé empujando con la de adelante.",
                         "la cadera queda de frente.", "estocada hacia atrás sin cruzar.", G("Propio cuerpo o mancuernas", "2 mancuernas")),
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


# Sesión → (activación, principal, complementario) de esta edición
SES = {
    "A": G((["Almeja", "Puente de glúteos"], ["Hip thrust en sillón", "Subida al banco"], ["Abducción de pierna de pie", "Puente a una pierna"]),
           (["Abducción en máquina", "Puente de glúteos"], ["Hip thrust con barra", "Prensa con pies altos"], ["Subida al banco", "Estocada split con mancuernas"])),
    "B": G((["Bird dog con pausa", "Abducción de pierna de pie"], ["Peso muerto con mancuernas", "Sentadilla sumo"], ["Estocada cruzada", "Almeja"]),
           (["Bird dog con pausa", "Abducción en máquina"], ["Peso muerto rumano con barra", "Sentadilla sumo"], ["Estocada cruzada", "Curl de isquiotibiales sentada"])),
}
FOCO = {"A": "empuje de cadera y una pierna", "B": "bisagra de cadera y apertura"}
CLAVE = {"A": "<b>La clave de la sesión A:</b> en el hip thrust, pausa de 1 segundo arriba apretando glúteos. Si lo sentís en la zona lumbar o en los cuádriceps, revisá la posición de los pies (capítulo 07).",
         "B": "<b>La clave de la sesión B:</b> en el peso muerto, la cadera va hacia atrás como si cerraras una puerta con la cola. La espalda queda recta y el peso cerca de las piernas."}
MATERIAL = G("Mancuernas, sillón o banco, escalón o silla, colchoneta y, si tenés, una banda elástica.",
             "Banco y barra, prensa, mancuernas, cajón, máquinas de abducción y de isquiotibiales.")

# ================================================================== PORTADA
page(f'''
<div class="cv3 glut{" gym" if GYM else ""}">
  <div class="c3-in">
    <img class="c3-logo" src="img/logo_renova.png" alt="RENOVA">
    <span class="c3-pill">{LUGAR} · MUJERES 40+</span>
    <h1 class="c3-title">GLÚTEOS<br>FUERTES</h1>
    <p class="c3-claim">TU DÍA EXTRA, <b><span>8 SEMANAS.</span></b></p>
    <p class="c3-sub">Fortalecé <b>glúteos</b> y <em>cadera</em> con un plan claro,<br><span>{G("en <mark>casa</mark>, con <mark>mancuernas</mark> y <mark>banda</mark>.", "en el <mark>gimnasio</mark>, con <mark>barra</mark> y <mark>máquinas</mark>.")}</span></p>
  </div>
  <div class="c3-team"><img src="img/equipo_tapa.png" alt="Equipo RENOVA"></div>
</div>
''', pid="portada", cls="p-cover", header=False)

# ================================================================== BIENVENIDA
page(f'''
{eyebrow("BIENVENIDA")}
<h1 class="h1">Tu día extra <span class="t">de RENOVA</span></h1>
<p class="lead">Glúteos Fuertes es <b>un día de entrenamiento por semana</b> dedicado a glúteos y cadera, {G("para hacer en casa", "para hacer en el gimnasio")}. No reemplaza tus rutinas del Método RENOVA: se suma a lo que ya hacés.</p>
{table(["Si entrenás…", "Glúteos Fuertes es…"], [
 ["<b>2 veces por semana</b> con RENOVA", "tu <b>tercer día</b>"],
 ["<b>3 veces por semana</b> con RENOVA", "tu <b>cuarto día</b>"],
])}
<h2>Cómo es cada sesión</h2>
{checks(["<b>Unos 40 minutos:</b> activación, bloque principal y bloque complementario.",
         "<b>Dos sesiones que se alternan:</b> la A (empuje de cadera) y la B (bisagra de cadera).",
         G("<b>Con poco material:</b> mancuernas, una silla o sillón, un escalón y una colchoneta.",
           "<b>Con lo que hay en un gimnasio:</b> barra, banco, prensa, mancuernas y máquinas."),
         "<b>8 semanas,</b> igual que el método, para que avancen juntos.",
         G("<b>Y también en el gimnasio:</b> si un día vas, tenés el ebook de gimnasio con las mismas sesiones.",
           "<b>Y también en casa:</b> si un día no podés ir, tenés el ebook de casa con las mismas sesiones.")])}
{box("<b>Dejá al menos un día entre esta sesión y la rutina de RENOVA</b> que más trabaja piernas. Así llegás descansada y el músculo se recupera.", "soft")}
''', chapter="Bienvenida", pid="bienvenida")

page("__TOC__", chapter="Índice", pid="indice")
INICIO = (f'<div class="box soft"><b>Empezá por acá:</b> 1) hacé tu test del día 1 (página {pref("test")}); '
          f'2) leé la sesión A (página {pref("a1")}); 3) elegí tu día de glúteos en la semana (página {pref("plan2")}).</div>')

# ================================================================== 01
page(f'''
{chap_head("01", 'Por qué el glúteo <span class="t">importa después de los 40</span>', "No es solo estética: es el músculo que sostiene tu cadera, protege tus rodillas y cuida tu espalda.")}
<h2>Tres músculos, tres funciones</h2>
{table(["Músculo", "Qué hace", "Lo usás cuando…"], [
 ["<b>Glúteo mayor</b>", "Extiende la cadera: te empuja hacia adelante y hacia arriba.", "Subís una escalera, te levantás de una silla, caminás en subida."],
 ["<b>Glúteo medio</b>", "Estabiliza la pelvis y abre la pierna al costado.", "Caminás, te parás en una pierna, bajás un escalón."],
 ["<b>Glúteo menor</b>", "Ayuda al medio a mantener la cadera firme.", "En cada paso, sin que te des cuenta."],
])}
<h2>Señales de que tu glúteo está trabajando poco</h2>
{checks(["Al bajar un escalón, la rodilla se te va hacia adentro.", "Después de estar mucho de pie, te molesta la zona lumbar.",
         "Al pararte en una pierna, la cadera del otro lado cae.", "Para levantarte de una silla necesitás ayudarte con las manos.", "Te cansás rápido al subir una cuesta o una escalera larga."])}
''', chapter="01 · Por qué el glúteo", pid="c1", toc="01 · Por qué el glúteo importa")

page(f'''
{eyebrow("POR QUÉ EL GLÚTEO")}
<h1 class="h1">Qué ganás con <span class="t">un glúteo fuerte</span></h1>
<p class="lead">Entrenarlo una vez por semana, con un plan y progresión, te da beneficios que se notan en tu día a día.</p>
{tips([("Cadera y rodillas", "Un glúteo medio débil deja que la rodilla se vaya hacia adentro. Fortalecerlo ordena el movimiento."),
       ("Espalda baja", "Si el glúteo no empuja, la zona lumbar compensa. Un glúteo fuerte le saca carga."),
       ("Equilibrio", "Pararte firme en una pierna es la base para caminar segura y prevenir caídas."),
       ("Postura", "Sostiene la pelvis y te ayuda a estar derecha sin esfuerzo."),
       ("Vida diaria", "Subir escaleras, levantarte del piso, cargar bolsas: todo pasa por el glúteo."),
       ("Forma", "Un glúteo con más músculo se ve más firme. Es una consecuencia, no el único objetivo.")])}
{box("<b>Después de los 40 se pierde músculo</b> si no hay estímulo de fuerza, y en la menopausia la pérdida se acelera. El glúteo es uno de los músculos más grandes del cuerpo: entrenarlo es cuidar tu fuerza para los próximos años.", "")}
''', chapter="01 · Por qué el glúteo", pid="c1b")

# ================================================================== 02
page(f'''
{chap_head("02", 'Cómo se fortalece <span class="t">un músculo</span>', "Tres claves explican casi todo. Si las cumplís, el músculo responde a cualquier edad.")}
{tips([("Esfuerzo suficiente", "Las últimas repeticiones tienen que costar. Si terminás fresca, el músculo no tiene motivo para cambiar."),
       ("Constancia", "Un día por semana, todas las semanas, suma más que tres días una semana y ninguno la siguiente."),
       ("Progresión", "Cada pocas semanas, un poco más: más peso, más repeticiones o más series.")], "t3")}
<h2>Con qué esfuerzo: la escala del 1 al 10</h2>
{table(["Esfuerzo", "Cómo se siente", "Cuándo"], [
 ["<b>5 – 6</b>", "Podrías hacer 4 o 5 repeticiones más.", "Semanas 1 y 2, y semana 5 (descarga)."],
 ["<b>7</b>", "Podrías hacer 3 más. Las últimas cuestan.", "Semanas 3 y 4."],
 ["<b>8</b>", "Podrías hacer 2 más, con buena técnica.", "Semanas 6 a 8."],
])}
<p>Nunca hace falta llegar a no poder más. <b>Primero la técnica, después el peso.</b> Y el músculo crece cuando descansás: dormir bien y comer proteína también son entrenamiento (capítulo 08).</p>
''', chapter="02 · Cómo se fortalece", pid="c2", toc="02 · Cómo se fortalece un músculo")

# ================================================================== 03
page(f'''
{chap_head("03", 'Tu test <span class="t">del día 1</span>', "Antes de la primera sesión, medí tu punto de partida. En la semana 8 lo repetís y ves cuánto avanzaste.")}
{ul(["<b>Puente a una pierna:</b> repeticiones seguidas con cada pierna, sin que la pelvis se caiga.",
     "<b>Sentadilla a la silla (30 s):</b> cuántas veces te sentás y te parás sin usar las manos.",
     "<b>Equilibrio en una pierna:</b> segundos en cada pierna, con los brazos cruzados (hasta 30).",
     "<b>Contorno de cadera:</b> en la parte más saliente de los glúteos, de pie y pies juntos."])}
{table(["Test", "Día 1", "Semana 8"], [
 ["Puente a una pierna (der. / izq.)", "&nbsp;&nbsp;&nbsp;/", "&nbsp;&nbsp;&nbsp;/"],
 ["Sentadilla a la silla (30 s)", "", ""],
 ["Equilibrio en segundos (der. / izq.)", "&nbsp;&nbsp;&nbsp;/", "&nbsp;&nbsp;&nbsp;/"],
 ["Contorno de cadera (cm)", "", ""],
])}
{box("<b>Tu primera victoria:</b> con hacer el test ya empezaste. Los números son tu punto de partida, no una nota. Si querés, sumá una foto de perfil el día 1 y la semana 8.", "soft")}
''', chapter="03 · Tu test", pid="test", toc="03 · Tu test del día 1")

# ================================================================== 04
page(f'''
{chap_head("04", 'Cómo <span class="t">progresar</span>', "Una regla simple para saber cuándo subir el peso, sin adivinar.")}
<p>Cada ejercicio tiene un rango, por ejemplo <b>10 a 12</b>. Empezá con un peso que te permita hacer 10 con el esfuerzo de la semana.</p>
<ol class="steps-ol">
<li>Cuando hagas <b>12 en todas las series</b> con buena técnica, la sesión siguiente subí un poco el peso.</li>
<li>Con el peso nuevo vas a volver a hacer 10. Está perfecto.</li>
<li>Vas sumando repeticiones de a poco hasta llegar otra vez a 12.</li>
</ol>
{table(["Si…", "Hacé esto"], [
 ["Hiciste el tope del rango en todas las series", G("Subí el peso: 1 a 2 kg en mancuernas. Sin más peso, sumá una serie o bajá más lento.", "Subí el peso: 1 a 2 kg en mancuernas, 2,5 a 5 kg en barra o máquina.")],
 ["Te quedaste dentro del rango", "Mantené el peso e intentá sumar una repetición."],
 ["No llegaste al mínimo o perdiste la técnica", "Bajá un poco el peso."],
 ["Te dolió una articulación (no es cansancio)", "Pará ese ejercicio y usá la opción más fácil."],
])}
{box("<b>Dolor muscular al día siguiente:</b> es normal las primeras semanas y baja solo. Si el dolor es en una rodilla, la cadera o la espalda, y no en el músculo, consultá antes de seguir.", "note")}
{box(f"<b>Anotá cada sesión</b> en tu planilla de cargas (página {pref('cargas')}). Sin registro no sabés si progresás.", "soft")}
''', chapter="04 · Cómo progresar", pid="c4", toc="04 · Cómo progresar")

# ================================================================== 05 · SESIONES
page(f'''
{chap_head("05", 'Tus <span class="t">sesiones</span>', "Dos sesiones que se alternan semana a semana.")}
{table(["Sesión", "Foco", "Página"], [
 ["<b>A</b>", "Empuje de cadera y una pierna", pref("a1")],
 ["<b>B</b>", "Bisagra de cadera y apertura", pref("b1")],
])}
<h2>Cómo se hace cada sesión</h2>
{table(["Parte", "Cómo"], [
 ["<b>Entrada en calor</b>", G("5 minutos de caminata en el lugar o subiendo y bajando un escalón.", "5 minutos de cinta, bici o elíptica.")],
 ["<b>Activación</b>", "2 vueltas seguidas de los 2 ejercicios, sin peso."],
 ["<b>Bloque principal</b>", f"Series según el plan (página {pref('plan')}). Descanso 90 s."],
 ["<b>Complementario</b>", "Series según el plan. Descanso 60 s."],
 ["<b>Elongación</b>", "La de tu ebook RENOVA, 5 minutos."],
])}
<p class="small"><b>Material:</b> {MATERIAL}</p>
{G(box("<b>Antes de cada sesión:</b> agua cerca, el material listo, tu planilla de cargas y algo comido 1 a 3 horas antes.", "soft"),
   "<h2>Antes de cada sesión</h2>" + checks(["Agua cerca y ropa cómoda.", "El plan B por si una máquina está ocupada (página " + pref("c9b") + ").",
                                            "Tu planilla de cargas para anotar.", "Haber comido algo 1 a 3 horas antes."]))}
''', chapter="05 · Sesiones", pid="c5", toc="05 · Tus sesiones")

for s in ("A", "B"):
    act, prin, comp = SES[s]
    page(f'''
{eyebrow(f"SESIÓN {s} · {LUGAR}")}
<h1 class="h1">Sesión {s}: <span class="t">{FOCO[s]}</span></h1>
{params([("Duración", "40 min"), ("Sesión", s), ("Lugar", G("Casa", "Gimnasio")), ("Hoja", "1 de 2")])}
<p class="small">Antes: 5 minutos de entrada en calor. Las series y repeticiones de cada semana están en el plan (página {pref("plan")}).</p>
{block_head("ACTIVACIÓN", "2 vueltas · sin peso · sin descanso entre ejercicios")}
{"".join(card(k) for k in act)}
{block_head("BLOQUE PRINCIPAL", "series del plan · descanso 90 s")}
{card(prin[0])}
''', chapter=f"05 · Sesión {s}", pid=f"{s.lower()}1", toc=f"Sesión {s} · {FOCO[s]}")
    page(f'''
{eyebrow(f"SESIÓN {s} · {LUGAR} · HOJA 2 DE 2")}
{block_head("BLOQUE PRINCIPAL", "series del plan · descanso 90 s")}
{card(prin[1])}
{block_head("COMPLEMENTARIO", "series del plan · descanso 60 s")}
{"".join(card(k) for k in comp)}
{box(CLAVE[s], "")}
{box("<b>Para cerrar:</b> 5 minutos de la elongación de tu ebook RENOVA. Anotá los pesos en tu planilla.", "soft")}
''', chapter=f"05 · Sesión {s}", pid=f"{s.lower()}2")

# ================================================================== 06 · PLAN
page(f'''
{chap_head("06", 'Tu plan de <span class="t">8 semanas</span>', "Igual que el Método RENOVA: base, descarga y progresión.")}
{table(["Semana", "Sesión", "Principal", "Complem.", "Esfuerzo"], [
 ["<b>1</b>", "A", "3 × 12", "2 × 10", "5 – 6"],
 ["<b>2</b>", "B", "3 × 12", "2 × 10", "5 – 6"],
 ["<b>3</b>", "A", "3 × 10 – 12", "3 × 10", "7"],
 ["<b>4</b>", "B", "3 × 10 – 12", "3 × 10", "7"],
 ["<b>5 · descarga</b>", "A", "2 × 10 liviano", "2 × 10", "5"],
 ["<b>6</b>", "B", "4 × 8 – 10", "3 × 10", "8"],
 ["<b>7</b>", "A", "4 × 8 – 10", "3 × 10", "8"],
 ["<b>8</b>", "B + test", "4 × 8 – 10", "3 × 10", "8"],
])}
<p class="small">“3 × 12” = 3 series de 12 repeticiones. En los ejercicios de una pierna, las repeticiones son por lado. La activación es siempre igual: 2 vueltas.</p>
{tips([("Aprendé y construí", "Semanas 1 a 4. Técnica primero; desde la 3, subí el peso."),
       ("Descarga", "Semana 5. Menos series y peso: el cuerpo asimila."),
       ("Progresá", "Semanas 6 a 8. Más series y peso. Al final, el test.")], "t3")}
{box(f"<b>Semana 8:</b> después de la sesión, o el día siguiente, repetí tu test (página {pref('test')}) y compará.", "soft")}
''', chapter="06 · Plan", pid="plan", toc="06 · Tu plan de 8 semanas")

page(f'''
{eyebrow("TU PLAN DE 8 SEMANAS")}
<h1 class="h1">Cómo encaja <span class="t">en tu semana</span></h1>
<h2>Si entrenás 2 veces con RENOVA</h2>
{table(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"], [["RENOVA", "–", "Glúteos", "–", "RENOVA", "Caminata", "–"]])}
<h2>Si entrenás 3 veces con RENOVA</h2>
{table(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"], [["RENOVA", "–", "RENOVA", "Glúteos", "–", "RENOVA", "–"]])}
<h2>Tu semana</h2>
{table(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"], [["", "", "", "", "", "", ""]])}
<p class="small">Son ejemplos: mové los días según tu semana. Lo importante es no hacer Glúteos Fuertes el día antes o el día después de la rutina que más trabaja piernas.</p>
{box("<b>¿Perdiste una semana?</b> No pasa nada. Retomá con la sesión que te tocaba y el esfuerzo de la semana anterior. No intentes recuperar haciendo dos sesiones juntas.", "soft")}
{box("<b>¿Una semana muy cargada?</b> Hacé la sesión express de 20 minutos (página " + pref("express") + "). Mejor 20 minutos que nada.", "")}
''', chapter="06 · Plan", pid="plan2")

# ================================================================== 07 · ERRORES
ERR = [("Sentir todo en los cuádriceps", "En el hip thrust y el puente, acercá los pies a la cola hasta que las canillas queden verticales arriba. Empujá con los talones."),
       ("Arquear la espalda arriba", "El movimiento termina cuando la cadera se alinea con el torso. Mentón al pecho y costillas abajo."),
       ("Bajar rápido", "La bajada también entrena. Contá 2 o 3 segundos para bajar en cada repetición."),
       ("Subir peso antes de dominar la técnica", "Si el peso te cambia el movimiento, es demasiado. Usá la regla del rango (capítulo 04)."),
       ("Quedarse siempre con el mismo peso", "Si hace tres semanas que hacés lo mismo con facilidad, el músculo ya se adaptó. Toca subir."),
       ("No descansar entre series", "En el bloque principal, 90 segundos. Apurarte te hace levantar menos y progresar menos."),
       ("Saltearte la activación", "Son 5 minutos que despiertan el glúteo. Sin ellos, el trabajo se lo llevan las piernas y la espalda."),
       ("Mirar solo la balanza", "El músculo pesa. Medí tu progreso con el test, la cinta y los pesos que levantás.")]
page(f'''
{chap_head("07", 'Errores que frenan <span class="t">tu progreso</span>', "Los más frecuentes, y cómo corregirlos.")}
<div class="mitos">{"".join(f"<div><b>{t}</b><p>{p}</p></div>" for t, p in ERR)}</div>
{box("<b>¿Dudas con la técnica?</b> Cada ejercicio tiene su botón <b>VER VIDEO</b>: miralo antes de la primera sesión.", "soft")}
''', chapter="07 · Errores", pid="c7", toc="07 · Errores frecuentes")

# ================================================================== 08 · ALIMENTACIÓN
page(f'''
{chap_head("08", 'Comer para <span class="t">construir músculo</span>', "El entrenamiento da la señal; la alimentación pone los materiales.")}
{checks(["<b>Proteína en cada comida:</b> huevo, lácteos, carnes, pollo, pescado, legumbres, tofu. Repartida en el día rinde más que concentrada en la cena.",
         "<b>No entrenes en ayunas largas:</b> una comida o colación 1 a 3 horas antes te da energía para levantar más.",
         "<b>Después de entrenar,</b> una comida con proteína ayuda a la recuperación. No hace falta que sea inmediata."])}
{table(["Momento", "Ideas"], [
 ["Antes de entrenar", "Yogur con fruta, tostada con queso, banana con un puñado de frutos secos"],
 ["Después de entrenar", "Huevos con verduras, pollo o pescado con arroz y ensalada, legumbres"],
 ["Si entrenás a la noche", "Merienda completa con proteína y una cena liviana después"],
])}
{box("<b>Comer muy poco frena el músculo.</b> Si estás haciendo un plan para bajar de peso, no recortes la proteína. Las cantidades para vos las define tu nutricionista. En <b>Alimentación Inteligente</b> tenés 8 semanas de menús y recetas.", "note")}
''', chapter="08 · Alimentación", pid="c8", toc="08 · Comer para construir músculo")

# ================================================================== 09 · CONSEJOS (distinto en cada edición)
if GYM:
    CONSEJOS = [("Regulá cada máquina", "Asiento, respaldo y topes a tu medida antes de la primera serie. Sacale una foto a la posición para la próxima."),
                ("Empezá con poco peso", "La primera semana es para aprender el movimiento. Subí con la regla del rango."),
                ("Siempre la entrada en calor", "5 minutos de cinta o bici y la activación. Llegás a la barra con la cadera despierta."),
                ("Llevá tu planilla", "En papel o en el celular. Anotá peso y repeticiones de cada ejercicio."),
                ("Pedí ayuda la primera vez", "Que el profe te muestre la máquina o te ayude a armar la barra del hip thrust."),
                ("Usá almohadilla en la barra", "En el hip thrust, con almohadilla o una toalla doblada sobre la cadera no molesta."),
                ("Tené un plan B", "Si la máquina está ocupada, usá el reemplazo de la hoja siguiente y seguí."),
                ("Respetá los descansos", "90 s en el principal y 60 s en el complementario. Usá el cronómetro del celular."),
                ("Toalla, agua y zapatillas firmes", "Suela plana y estable para empujar con los talones."),
                ("Tu progreso es contra vos", "No copies los pesos de otras. Compará tu semana con tu semana anterior.")]
    page(f'''
{chap_head("09", '10 consejos <span class="t">para el gimnasio</span>', "Para sacarle el máximo a cada sesión y sentirte cómoda desde el primer día.")}
{tips(CONSEJOS[:6])}
{box("<b>Si es tu primera vez en un gimnasio,</b> es normal sentirse perdida. Llevá este ebook abierto en el celular y seguí la sesión paso a paso.", "soft")}
''', chapter="09 · Consejos", pid="c9", toc="09 · 10 consejos para el gimnasio")
    page(f'''
{eyebrow("CONSEJOS PARA EL GIMNASIO")}
{tips(CONSEJOS[6:], start=7)}
<h2>Plan B: si la máquina está ocupada</h2>
{table(["Si está ocupado…", "Hacé…"], [
 ["Banco y barra del hip thrust", "Hip thrust con mancuerna en un banco, o puente con barra en el piso"],
 ["Prensa", "Sentadilla sumo con mancuerna o subida al cajón"],
 ["Máquina de abducción", "Abducción de pie en la polea baja o con banda"],
 ["Máquina de isquiotibiales", "Peso muerto rumano con mancuernas"],
 ["Cajón", "Estocada split con mancuernas"],
])}
{box("<b>Horarios:</b> a media mañana y a primera hora de la tarde suele haber menos gente. Si vas en hora pico, empezá por el ejercicio que esté libre.", "")}
''', chapter="09 · Consejos", pid="c9b")
else:
    CONSEJOS = [("Levantate cada hora", "Cada 60 a 90 minutos sentada, parate 2 o 3 minutos: caminá, buscá agua, estirate."),
                ("Pausa activa dos veces por día", "Una rutina de 10 minutos a media mañana y otra a media tarde. Tenés 4 en el bonus Pausa activa."),
                ("Caminá cuando hablás", "Cada llamada por teléfono, de pie o caminando por la casa."),
                ("Sumá pasos de a poco", "Mirá cuántos hacés hoy y sumá 1.000 por semana hasta llegar a tu meta."),
                ("Escaleras siempre que puedas", "Es fuerza de glúteo gratis, varias veces por día."),
                ("Caminá después de comer", "10 minutos después del almuerzo o la cena. Ayuda a la digestión y suma movimiento."),
                ("Glúteos en los tiempos muertos", "Mientras se calienta el agua o esperás el microondas: 10 puentes o 10 sentadillas."),
                ("Alterná sentada y de pie", "Si trabajás en computadora, armá un rato de pie con la notebook sobre una mesada."),
                ("Bajate antes, estacioná lejos", "Una parada antes del colectivo o el auto más lejos: 10 minutos más de caminata."),
                ("Movete con otros", "Caminá con una amiga, con tu pareja o con el perro. Es más fácil sostenerlo acompañada.")]
    page(f'''
{chap_head("09", 'Mantenete <span class="t">activa</span>', "Entrenar 40 minutos no compensa estar sentada 9 horas. Lo que hacés el resto del día también cuenta.")}
{box("<b>Estar mucho tiempo sentada apaga el glúteo:</b> la cadera queda flexionada y el músculo casi no trabaja. Por eso, además de entrenar, moverte durante el día es parte del programa.", "note")}
{tips(CONSEJOS[:6])}
''', chapter="09 · Mantenete activa", pid="c9", toc="09 · Mantenete activa: 10 consejos")
    page(f'''
{eyebrow("MANTENETE ACTIVA")}
{tips(CONSEJOS[6:], start=7)}
<h2>Un día activo, de ejemplo</h2>
{table(["Momento", "Qué hacer"], [
 ["Mañana", "10 minutos de caminata o subir y bajar escaleras"],
 ["Media mañana", "Pausa activa de 10 minutos"],
 ["Después de almorzar", "Caminata de 10 minutos"],
 ["Media tarde", "Pausa activa de 10 minutos"],
 ["Mientras cocinás", "10 puentes y 10 sentadillas"],
 ["Antes de dormir", "5 minutos de elongación de cadera"],
])}
{box("<b>¿Qué hacés en la pausa activa?</b> Usá las 4 rutinas de 10 minutos del bonus <b>Pausa activa</b> de tu Método RENOVA.", "soft")}
''', chapter="09 · Mantenete activa", pid="c9b")

# ================================================================== BONUS EXPRESS
EXP = G([("Puente de glúteos", "12"), ("Peso muerto con mancuernas", "12"), ("Subida al banco", "10 por lado")],
        [("Hip thrust con barra", "12"), ("Abducción en máquina", "15"), ("Estocada split con mancuernas", "10 por lado")])
page(f'''
{eyebrow(f"BONUS · {LUGAR}")}
<h1 class="h1">Sesión express <span class="t">de 20 minutos</span></h1>
<p class="lead">Para las semanas con poco tiempo. Mantenés el hábito y el estímulo.</p>
{G(params([("Duración", "20 min"), ("Vueltas", "3"), ("Descanso", "30 s"), ("Esfuerzo", "7")]), "")}
{block_head("CIRCUITO", "3 vueltas · 30 s de descanso entre vueltas")}
{"".join(card(k, d) for k, d in EXP)}
{box("<b>Usala como excepción:</b> si la hacés más de dos semanas seguidas, el progreso se frena. Volvé a la sesión completa apenas puedas.", "soft")}
''', chapter="Bonus · Express", pid="express", toc="Bonus: sesión express de 20 min")

# ================================================================== PLANILLA
CARGAS = G(["Hip thrust en sillón", "Subida al banco", "Peso muerto rumano", "Sentadilla sumo", "Estocada cruzada", "Puente a una pierna", "Abducción de pie"],
           ["Hip thrust con barra", "Prensa con pies altos", "Peso muerto rumano", "Sentadilla sumo", "Estocada split / cruzada", "Curl de isquiotibiales", "Abducción en máquina"])
page(f'''
{eyebrow("HERRAMIENTA")}
<h1 class="h1">Tu planilla <span class="t">de cargas</span></h1>
<p class="small">Anotá el peso (kg) y las repeticiones de la última serie. Ejemplo: <b>8 kg × 12</b>.</p>
<div class="tall">{table(["Ejercicio"] + [f"S{i}" for i in range(1, 9)], [[e] + [""] * 8 for e in CARGAS], first="30%")}</div>
<h2>Cómo me sentí</h2>
{table(["Semana"] + [f"S{i}" for i in range(1, 9)], [["Energía (1 a 5)"] + [""] * 8, ["Dolor muscular (1 a 5)"] + [""] * 8], first="30%")}
''', chapter="Herramientas", pid="cargas", toc="Herramienta: planilla de cargas")

# ================================================================== DESPUÉS
page(f'''
{eyebrow("DESPUÉS DE LAS 8 SEMANAS")}
<h1 class="h1">Repetí el test <span class="t">y elegí cómo seguir</span></h1>
<p>En la semana 8 repetí los tests y la medida de cadera (página {pref("test")}). Compará con tu día 1: más repeticiones y más segundos en una pierna son fuerza que ganaste.</p>
{tips([("Subí la carga", "Repetí las 8 semanas empezando con los pesos de la semana 8."),
       ("Mantené", "Seguí con un día por semana alternando A y B, con esfuerzo 7."),
       ("Plan a tu medida", "Pedí un plan integral armado para vos (página siguiente).")], "t3")}
<h2>Qué cambió para vos</h2>
{checks(["Subo escaleras con menos esfuerzo.", "Me levanto de la silla sin usar las manos.", "Me siento más firme parada en una pierna.",
         "Me molesta menos la espalda o la rodilla.", "Levanto más peso que en la semana 1."])}
{box("<b>Lo que ganaste no se pierde en una semana.</b> Si cortás un tiempo, volvé con el esfuerzo de las semanas 1 y 2 y subí de a poco.", "soft")}
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
                    f'<p class="idxtip">{ICON_HAND} Hacé clic donde quieras ir. Para volver al índice, abajo de cada página tenés el botón.</p></div>{toc_html}{INICIO}')
        hdr = ""
        if p["header"]:
            hdr = (f'<div class="hdr"><span>GLÚTEOS FUERTES · {G("EN CASA", "GIMNASIO")} · <b>RENOVA</b></span><span>{esc(p["chapter"])}</span></div>'
                   f'<div class="ftr"><a class="toidx" href="#indice">{ICON_HAND} Hacé clic y volvé al índice</a><span class="pgnum"></span></div>')
        out.append(f'<section class="page {p["cls"]}" id="{p["id"]}">{hdr}<div class="body">{body}</div></section>')
    css = ds_css(HERE) + "\n" + open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Glúteos Fuertes {G("en casa", "en el gimnasio")} · RENOVA</title>'
            f'<style>{css}</style></head><body class="grande">' + "".join(out) + '<script src="paginate.js"></script></body></html>')


if __name__ == "__main__":
    out = f"gluteos_{ED}.html"
    with open(os.path.join(HERE, out), "w", encoding="utf-8") as f:
        f.write(render())
    print(out, "·", len(PAGES), "páginas:", " ".join(f"{i + 1}:{p['id']}" for i, p in enumerate(PAGES)))
