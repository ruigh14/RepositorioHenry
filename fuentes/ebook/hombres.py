"""MÉTODO 40 · Entrenamiento de fuerza para hombres 40+ (submarca para la otra tienda de Impultienda).
Dos ebooks que se venden juntos, desde el mismo script:
  python3 hombres.py casa → hombres_casa.html → metodo-40/Ebook_Metodo40_Casa.pdf      (node export.js hombres_casa)
  python3 hombres.py gym  → hombres_gym.html  → metodo-40/Ebook_Metodo40_Gimnasio.pdf  (node export.js hombres_gym)

Programa: 8 semanas, 3 días por semana, rutinas de cuerpo completo A/B/C que rotan; fase 1 (semanas 1–4),
descarga (5) y fase 2 (6–8). Cada ejercicio usa un video propio de Ignacio en Harbiz (con la marca LEVEL UP:
Nacho decidió dejarla) y una captura de ese video (img/m40/). Autor: Ignacio Portillo.
Estructura aprobada en investigacion/metodo-40/estructura-ebooks.md. Paleta: tokens --m40-* (body.m40 en style.css).
Cada hoja se arma completa a mano: ningún bloque partido entre hojas y sin huecos grandes (ver FREE de export.js).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "design-system"))
from design_system import css as ds_css, esc, ICON_HAND, ICON_PLAY, eyebrow, chap_head, ul, checks, box, block_head, params

ED = sys.argv[1] if len(sys.argv) > 1 else "casa"
assert ED in ("casa", "gym"), "edición: casa o gym"
GYM = ED == "gym"


def G(casa, gym):
    return gym if GYM else casa


LUGAR = G("EN CASA", "EN EL GIMNASIO")
AUTOR = "Ignacio Portillo"
AUTOR_TIT = "Licenciado en Alto Rendimiento Deportivo · Preparador físico de fútbol profesional"   # Racing: solo con autorización
PAGES, TOC = [], []


def page(body, chapter="", pid=None, cls="", toc=None, header=True):
    pid = pid or f"p{len(PAGES) + 1}"
    PAGES.append(dict(id=pid, chapter=chapter, body=body, cls=cls, header=header))
    if toc:
        TOC.append((toc, pid))


def table(head, rows, first=None, cls=""):
    th = "".join((f'<th style="width:{first}">' if first and i == 0 else "<th>") + f"{h}</th>" for i, h in enumerate(head))
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="grid-t ntab {cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def pref(pid):
    return f'<span class="pref" data-ref="{pid}"></span>'


def tips(items, cls="", start=1):
    return f'<div class="tips10 {cls}">' + "".join(
        f'<div><span>{i:02d}</span><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(items, start)) + "</div>"


# ------------------------------------------------------------------ EJERCICIOS
# clave: (imagen en img/m40, nombre, músculos, técnica, evitá, principiante, material, video propio en Harbiz)
E = {
    # calentamiento
    "mov_cadera": ("mov_cadera", "Movilidad de cadera", "Cadera", "Sentado en el piso, rodillas flexionadas: llevá las dos rodillas a un lado y al otro, con el tronco alto.", "", "", "Colchoneta", "https://youtu.be/5zdTIdhtZjU"),
    "mov_escapular": ("mov_escapular", "Movilidad escapular", "Hombros y escápulas", "Brazos al frente: juntá y separá las escápulas sin doblar los codos.", "", "", "Propio cuerpo", "https://youtu.be/kctm9ouv5GU"),
    "cat_cow": ("cat_cow", "Gato-vaca", "Columna", "En cuatro apoyos, redondeá la espalda al exhalar y arqueala suave al inhalar.", "", "", "Colchoneta", "https://youtu.be/rEosL__rD5k"),
    "mov_baston": ("mov_baston", "Movilidad con bastón", "Hombros", "Con un bastón o palo de escoba, llevá los brazos estirados de adelante hacia atrás por arriba de la cabeza.", "", "", "Bastón o palo", "https://youtu.be/ti_VnUlkvg4"),
    "rodillas_arriba": ("rodillas_arriba", "Rodillas arriba dinámico", "Cadera y piernas", "Marchá en el lugar subiendo las rodillas a la altura de la cadera, con ritmo creciente.", "", "", "Propio cuerpo", "https://youtu.be/SslB3xLpngI"),
    # casa
    "sentadilla_copa": ("sentadilla_copa", "Sentadilla en copa", "Cuádriceps y glúteos", "Mancuerna pegada al pecho, pies al ancho de hombros. Bajá con la cadera atrás y el pecho alto; subí empujando el piso.", "rodillas que se van hacia adentro.", "sentadilla a una silla, sin peso.", "1 mancuerna", "https://youtu.be/4vdE4BQJdIM"),
    "elevacion_cadera_cajon": ("elevacion_cadera_cajon", "Elevación de cadera en banco", "Glúteos e isquiotibiales", "Boca arriba, talones sobre un banco o silla firme. Subí la cadera hasta alinear rodillas, cadera y hombros; bajá lento.", "arquear la zona lumbar arriba.", "con los pies en el piso.", "Banco o silla", "https://youtu.be/25WCgPAdc_o"),
    "flexiones": ("flexiones", "Flexiones de brazos", "Pecho, hombros y tríceps", "Manos un poco más abiertas que los hombros, cuerpo en línea. Bajá con los codos a 45° y empujá.", "cadera caída o codos abiertos a 90°.", "flexiones inclinadas, con las manos en un banco.", "Propio cuerpo", "https://youtu.be/P5_xMDhaVHs"),
    "remo_unilateral": ("remo_unilateral", "Remo unilateral con mancuerna", "Espalda y bíceps", "Una mano y una rodilla apoyadas. Llevá la mancuerna hacia la cadera, con el codo pegado al cuerpo.", "girar el tronco para subir el peso.", "con menos peso y más control.", "1 mancuerna y banco", "https://youtu.be/6a1emLHfGYg"),
    "press_hombros_arrodillado": ("press_hombros_arrodillado", "Press de hombros arrodillado", "Hombros y tríceps", "Arrodillado, abdomen firme. Empujá la mancuerna hacia arriba hasta estirar el brazo, sin arquear la espalda.", "inclinarte hacia atrás para empujar.", "de a un brazo y con menos peso.", "Mancuernas", "https://youtu.be/RZXbCZ_fneQ"),
    "plancha_frontal": ("plancha_frontal", "Plancha frontal", "Zona media", "Antebrazos apoyados, cuerpo en línea de hombros a talones. Apretá abdomen y glúteos.", "cadera muy alta o caída.", "con las rodillas apoyadas.", "Colchoneta", "https://youtu.be/nd0qbgESlao"),
    "peso_muerto_1_pierna": ("peso_muerto_1_pierna", "Peso muerto a una pierna", "Isquiotibiales, glúteos y equilibrio", "Mancuerna en una mano, peso en la pierna contraria. Inclinate con la espalda recta y la otra pierna hacia atrás; volvé apretando glúteo.", "redondear la espalda o girar la cadera.", "peso muerto con bastón, con las dos piernas.", "1 mancuerna", "https://youtu.be/0KFZn0giQJQ"),
    "estocada_bulgara": ("estocada_bulgara", "Estocada búlgara", "Cuádriceps y glúteos", "Pie de atrás sobre un banco. Bajá la rodilla de atrás con el tronco firme y subí empujando con la de adelante.", "que la rodilla de adelante se vaya hacia adentro.", "estocada común, sin banco.", "Banco y mancuernas", "https://youtu.be/rf1CvaGe5JU"),
    "fondos_banco": ("fondos_banco", "Fondos de tríceps en banco", "Tríceps y pecho", "Manos en el borde del banco, cola cerca. Bajá doblando los codos hacia atrás y empujá.", "bajar demasiado y forzar el hombro.", "con las rodillas flexionadas y menos recorrido.", "Banco o silla", "https://youtu.be/FqLq6-WRoqw"),
    "vuelo_posterior": ("vuelo_posterior", "Vuelo posterior con mancuernas", "Hombros posteriores y espalda alta", "Tronco inclinado y espalda recta. Abrí los brazos hacia los costados con los codos apenas flexionados.", "tirar con impulso del tronco.", "con botellas o menos peso.", "2 mancuernas", "https://youtu.be/Stpq0KwR5iQ"),
    "curl_biceps": ("curl_biceps", "Curl de bíceps con mancuernas", "Bíceps", "Codos pegados al cuerpo. Subí las mancuernas girando las palmas hacia arriba y bajá lento.", "balancear el cuerpo.", "curl con banda elástica.", "2 mancuernas", "https://youtu.be/ToxLEnNgKXA"),
    "bicho_muerto_botella": ("bicho_muerto_botella", "Bicho muerto con peso", "Zona media", "Boca arriba, brazos y rodillas a 90°. Estirá brazo y pierna contraria sin despegar la zona lumbar del piso.", "arquear la espalda al estirar.", "sin peso y con menos recorrido.", "Botella o mancuerna", "https://youtu.be/MqbAxttwogg"),
    "subida_banco": ("subida_banco", "Subida al banco", "Cuádriceps y glúteos", "Pie entero arriba del banco. Subí empujando con esa pierna, sin impulsarte con la de abajo; bajá lento.", "que la rodilla se vaya hacia adentro.", "un escalón más bajo, sin peso.", "Banco o escalón", "https://www.youtube.com/shorts/70DS_CBZwfY"),
    "estocada": ("estocada", "Estocada", "Cuádriceps y glúteos", "Un pie adelante y otro atrás. Bajá la rodilla de atrás hasta casi tocar el piso y subí con la pierna de adelante.", "tronco caído hacia adelante.", "con apoyo en una silla.", "Mancuernas (opcional)", "https://youtu.be/s7ewEzHwXgQ"),
    "push_press": ("push_press", "Push press con mancuernas", "Hombros, tríceps y piernas", "Mancuernas a la altura de los hombros. Flexioná apenas las rodillas y empujá con las piernas y los brazos hacia arriba.", "arquear la espalda al final.", "press de hombros con banda.", "2 mancuernas", "https://youtu.be/2ZDHMjr2pkM"),
    "renegade_row": ("renegade_row", "Remo en plancha (renegade row)", "Espalda, zona media y hombros", "En plancha alta con las manos sobre las mancuernas, pies abiertos. Remá con un brazo sin girar la cadera.", "rotar el cuerpo al subir el peso.", "remo unilateral apoyado en un banco.", "2 mancuernas", "https://youtu.be/ouNjv25ffI4"),
    "elevaciones_laterales": ("elevaciones_laterales", "Elevaciones laterales", "Hombros", "Codos apenas flexionados. Subí los brazos a los costados hasta la altura de los hombros y bajá lento.", "subir con impulso o por encima de los hombros.", "con botellas o de a un brazo.", "2 mancuernas", "https://youtu.be/vguq1MBRh_Y"),
    "plancha_lateral": ("plancha_lateral", "Plancha lateral", "Oblicuos y zona media", "Apoyado en un antebrazo, cuerpo en línea. Mantené la cadera alta.", "dejar caer la cadera.", "con la rodilla de abajo apoyada.", "Colchoneta", "https://youtu.be/bxQgU1eK4dc"),
    "press_pallof": ("press_pallof", "Press Pallof", "Zona media (antirrotación)", G("Banda atada a la altura del pecho, de costado. Llevá las manos al frente sin dejar que el tronco gire.", "Polea a la altura del pecho, de costado. Llevá las manos al frente sin dejar que el tronco gire."),
                     "girar el tronco hacia la banda.", "más cerca del anclaje, menos tensión.", G("Banda elástica", "Polea"), "https://youtu.be/t9jDygFEbU0"),
    # gimnasio
    "sentadilla_barra": ("sentadilla_barra", "Sentadilla con barra", "Cuádriceps, glúteos y zona media", "Barra apoyada en la parte alta de la espalda. Bajá con la cadera atrás y las rodillas siguiendo las puntas; subí empujando el piso.", "despegar los talones o redondear la espalda.", "prensa.", "Barra y rack", "https://youtu.be/idl_EYsUlzQ"),
    "curl_isquio": ("curl_isquio", "Curl de isquiotibiales sentado", "Isquiotibiales", "Rodillas alineadas con el eje de la máquina. Flexioná bajando el rodillo y volvé con control.", "levantar la cadera del asiento.", "con menos peso.", "Máquina", "https://youtu.be/8I7lYLxvAf0"),
    "press_plano": ("press_plano", "Press plano con barra", "Pecho, hombros y tríceps", "Pies firmes en el piso, escápulas juntas. Bajá la barra al pecho con los codos a 45° y empujá.", "rebotar la barra en el pecho.", "press de pecho en máquina.", "Barra y banco", "https://youtu.be/HDmYWB7TEds"),
    "remo_polea_baja": ("remo_polea_baja", "Remo en polea baja", "Espalda y bíceps", "Espalda derecha. Llevá el agarre hacia el abdomen juntando las escápulas y volvé sin perder la postura.", "tirar con el tronco hacia atrás.", "con menos peso.", "Polea", "https://youtu.be/hkFC0uc7G6A"),
    "peso_muerto_barra": ("peso_muerto_barra", "Peso muerto con barra", "Glúteos, isquiotibiales y espalda", "Barra pegada a las piernas, espalda recta. Llevá la cadera atrás para bajar y subí empujando el piso.", "redondear la espalda o alejar la barra.", "peso muerto rumano en máquina o con mancuernas.", "Barra", "https://youtu.be/MeXBpLzezlw"),
    "estocada_split_mancuernas": ("estocada_split_mancuernas", "Estocada split con mancuernas", "Cuádriceps y glúteos", "Un pie adelante y otro atrás, mancuernas a los costados. Bajá la rodilla de atrás y subí con la de adelante.", "que la rodilla de adelante se vaya hacia adentro.", "sin peso.", "2 mancuernas", "https://youtu.be/JOQYcHKf83I"),
    "press_45_barra": ("press_45_barra", "Press inclinado con barra", "Pecho alto y hombros", "Banco a 45°, escápulas juntas. Bajá la barra a la parte alta del pecho y empujá.", "despegar la cola del banco.", "press inclinado con mancuernas.", "Barra y banco inclinado", "https://youtu.be/N7yZeklJkE8"),
    "jalones": ("jalones", "Jalón al pecho", "Dorsales y bíceps", "Agarre un poco más abierto que los hombros. Llevá la barra a la clavícula con el pecho alto.", "tirar hacia atrás con todo el cuerpo.", "con menos peso.", "Polea alta", "https://youtu.be/Vfeh314bQX4"),
    "face_pull": ("face_pull", "Face pull", "Hombros posteriores y manguito rotador", "Soga a la altura de la cara. Tirá hacia los ojos abriendo los codos hacia afuera.", "subir los hombros a las orejas.", "con menos peso.", "Polea y soga", "https://youtu.be/R1FeK4isaHE"),
    "hip_thrust_unipodal": ("hip_thrust_unipodal", "Hip thrust a una pierna", "Glúteos", "Espalda alta en el banco, pesa rusa sobre la cadera, una pierna apoyada. Subí la cadera con el glúteo y bajá lento.", "arquear la zona lumbar arriba.", "con las dos piernas y sin peso.", "Banco y pesa rusa", "https://youtu.be/nym6wROJ9UM"),
    "prensa": ("prensa", "Prensa", "Cuádriceps y glúteos", "Espalda apoyada, pies al ancho de la cadera. Bajá a 90° y empujá sin bloquear las rodillas.", "despegar la cola del asiento al bajar.", "con menos peso y recorrido.", "Máquina", "https://youtu.be/ddfmGBWmB88"),
    "press_militar_maquina": ("press_militar_maquina", "Press de hombros en máquina", "Hombros y tríceps", "Espalda apoyada. Empujá hacia arriba sin bloquear los codos y bajá hasta la altura del mentón.", "arquear la espalda.", "con menos peso.", "Máquina", "https://youtu.be/epNNDB486H4"),
    "remo_45_barra": ("remo_45_barra", "Remo inclinado con barra", "Espalda y bíceps", "Tronco inclinado a 45°, espalda recta. Llevá la barra hacia el abdomen y bajá con control.", "subir el tronco para ayudarte.", "remo en máquina.", "Barra", "https://youtu.be/6o78vcu6BOY"),
    "triceps_soga": ("triceps_soga", "Extensión de tríceps con soga", "Tríceps", "Codos fijos al costado del cuerpo. Estirá los brazos hacia abajo abriendo la soga al final.", "mover los codos hacia adelante.", "con menos peso.", "Polea y soga", "https://youtu.be/E5-R8s44Ix4"),
    "bicho_muerto_disco": ("bicho_muerto_disco", "Bicho muerto con disco", "Zona media", "Boca arriba, disco en las manos y rodillas a 90°. Estirá las piernas de a una sin despegar la zona lumbar.", "arquear la espalda.", "sin disco.", "Disco", "https://youtu.be/fKAKLkzfhvQ"),
}

CALOR = ["mov_cadera", "mov_escapular", "cat_cow", "mov_baston", "rodillas_arriba"]
# rutina → [(ejercicio, series/reps fase 1, fase 2, descanso)]
RUT = G({
    "A": [("sentadilla_copa", "3 × 12", "4 × 8", "90 s"), ("elevacion_cadera_cajon", "3 × 12", "4 × 10", "60 s"), ("flexiones", "3 × 10", "4 × 8–12", "90 s"),
          ("remo_unilateral", "3 × 12", "4 × 8", "60 s"), ("press_hombros_arrodillado", "3 × 10", "4 × 8", "60 s"), ("plancha_frontal", "3 × 30 s", "3 × 45 s", "45 s")],
    "B": [("peso_muerto_1_pierna", "3 × 10", "4 × 8", "90 s"), ("estocada_bulgara", "3 × 10", "4 × 8", "90 s"), ("fondos_banco", "3 × 10", "4 × 10", "60 s"),
          ("vuelo_posterior", "3 × 12", "4 × 12", "60 s"), ("curl_biceps", "3 × 12", "4 × 10", "60 s"), ("bicho_muerto_botella", "3 × 10", "3 × 12", "45 s")],
    "C": [("subida_banco", "3 × 10", "4 × 8", "90 s"), ("estocada", "3 × 10", "4 × 8", "90 s"), ("push_press", "3 × 10", "4 × 8", "90 s"),
          ("renegade_row", "3 × 8", "4 × 8", "60 s"), ("elevaciones_laterales", "3 × 12", "4 × 12", "60 s"), ("plancha_lateral", "3 × 25 s", "3 × 40 s", "45 s")],
}, {
    "A": [("sentadilla_barra", "3 × 10", "4 × 6–8", "2 min"), ("curl_isquio", "3 × 12", "4 × 10", "60 s"), ("press_plano", "3 × 10", "4 × 6–8", "2 min"),
          ("remo_polea_baja", "3 × 12", "4 × 8", "90 s"), ("elevaciones_laterales", "3 × 12", "4 × 12", "60 s"), ("plancha_frontal", "3 × 30 s", "3 × 45 s", "45 s")],
    "B": [("peso_muerto_barra", "3 × 8", "4 × 5–6", "2 min"), ("estocada_split_mancuernas", "3 × 10", "4 × 8", "90 s"), ("press_45_barra", "3 × 10", "4 × 8", "90 s"),
          ("jalones", "3 × 12", "4 × 8", "90 s"), ("face_pull", "3 × 15", "4 × 12", "60 s"), ("press_pallof", "3 × 10", "3 × 12", "45 s")],
    "C": [("hip_thrust_unipodal", "3 × 10", "4 × 8", "90 s"), ("prensa", "3 × 12", "4 × 8", "90 s"), ("press_militar_maquina", "3 × 10", "4 × 8", "90 s"),
          ("remo_45_barra", "3 × 10", "4 × 8", "90 s"), ("triceps_soga", "3 × 12", "4 × 10", "60 s"), ("bicho_muerto_disco", "3 × 10", "3 × 12", "45 s")],
})
FOCO = G({"A": "piernas y empuje", "B": "bisagra y tirón", "C": "una pierna y hombros"},
         {"A": "sentadilla y empuje", "B": "bisagra y tirón", "C": "glúteos, espalda y brazos"})


CLAVES = G({
    "A": ["La sentadilla es el ejercicio principal: hacela con la cabeza fresca.", "En las flexiones, el cuerpo es una tabla de la cabeza a los talones.", "Si las flexiones te salen fáciles, poné los pies en el banco."],
    "B": ["El peso muerto a una pierna es de control: bajá lento y sin apuro.", "En la búlgara, el peso va en la pierna de adelante.", "En los fondos, cuidá el hombro: bajá solo hasta los 90°."],
    "C": ["En la subida al banco, la pierna de abajo no empuja.", "El push press usa las piernas: es un empuje explosivo, no un press estricto.", "En el remo en plancha, abrí los pies para no girar la cadera.", "Las elevaciones laterales van con poco peso: el hombro se trabaja con control."],
}, {
    "A": ["La sentadilla con barra es el ejercicio principal: hacela con la cabeza fresca.", "Hacé 2 series de aproximación antes de la sentadilla y del press plano."],
    "B": ["El peso muerto es el ejercicio más exigente del programa: técnica antes que kilos.", "Entre series de peso muerto, descansá completo: 2 minutos.", "En el face pull, pensá en abrir el pecho, no en tirar con los brazos."],
    "C": ["El hip thrust a una pierna es de control: pausa de 1 segundo arriba.", "En la prensa, no bloquees las rodillas al estirar.", "En el remo inclinado, la espalda no se mueve: solo los brazos.", "Si te sobra energía, sumá 2 series de bíceps martillo al final."],
})


def card(k):
    img, name, mus, how, evita, princ, mat, url = E[k]
    ev = f'<p class="ev"><b>Evitá:</b> {evita}</p>' if evita else ""
    pr = f'<p><b>Principiante:</b> {princ}</p>' if princ else ""
    return (f'<div class="mx"><div class="mx-l"><div class="mx-im"><img src="img/m40/{img}.jpg" alt=""></div><span class="mat">{mat}</span></div>'
            f'<div><h4>{name}</h4><span class="mus">{mus}</span><p>{how}</p>{ev}{pr}'
            f'<a class="vbtn-sm" href="{esc(url)}">{ICON_PLAY} VER VIDEO</a></div></div>')


# ================================================================== PORTADA
page(f'''
<div class="mcv">
  <img class="mcv-foto" src="img/m40/autor.jpg" alt="{AUTOR}">
  <div class="mcv-fade"></div>
  <div class="mcv-in">
    <div class="mcv-brand">MÉTODO <b>40</b></div>
    <div class="mcv-bar"></div>
    <h1>Fuerza<br>para hombres<br><span>40+</span></h1>
    <span class="mcv-lugar">{LUGAR}</span>
    <p class="mcv-sub">Programa de 8 semanas · 3 días por semana · 45 minutos</p>
  </div>
  <div class="mcv-autor">{AUTOR.upper()}<small>Lic. en Alto Rendimiento Deportivo</small></div>
</div>
''', pid="portada", cls="p-cover", header=False)

# ================================================================== BIENVENIDA
page(f'''
{eyebrow("BIENVENIDO")}
<h1 class="h1">Un plan para recuperar <span class="t">fuerza y músculo</span></h1>
<p class="lead">Después de los 40 el cuerpo cambia, pero sigue respondiendo al entrenamiento. Este programa te dice <b>qué hacer, cuántas veces, con qué carga y cómo progresar</b>, {G("en tu casa, con poco equipamiento", "en cualquier gimnasio")}.</p>
{table(["Qué es", "Cómo es"], [
 ["<b>Duración</b>", "8 semanas"],
 ["<b>Frecuencia</b>", "3 días por semana (por ejemplo, lunes, miércoles y viernes)"],
 ["<b>Cada sesión</b>", "8 minutos de calentamiento + 35 a 40 de fuerza"],
 ["<b>Rutinas</b>", "3 de cuerpo completo (A, B y C) que rotan"],
 ["<b>Material</b>", G("Mancuernas, banda elástica, banco o silla firme y colchoneta", "Barras, mancuernas, máquinas y poleas")],
])}
<h2>Cómo usar este ebook</h2>
{checks(["Leé los capítulos 01 a 04 antes de la primera sesión: son 10 minutos.",
         "Cada ejercicio tiene su foto, la técnica, el error a evitar, la opción para principiantes y el <b>video</b>.",
         "Anotá cada sesión en la planilla de cargas: es lo que te muestra si progresás."])}
''', chapter="Bienvenido", pid="bienvenida")

page("__TOC__", chapter="Índice", pid="indice")
INICIO = (f'<div class="box soft"><b>Para empezar:</b> leé los capítulos 01 a 04 (páginas {pref("c1")} a {pref("c4")}), '
          f'mirá la rutina A (página {pref("rA")}) y anotá tus cargas en la planilla (página {pref("cargas")}).</div>')

# ================================================================== 01
page(f'''
{chap_head("01", 'Qué cambia <span class="t">después de los 40</span>', "No es la edad: es lo que el cuerpo pierde cuando no recibe estímulo.")}
{table(["Qué cambia", "Qué significa para vos"], [
 ["<b>Masa muscular</b>", "Se pierde de a poco desde los 30 si no entrenás fuerza, y la pérdida se acelera con los años."],
 ["<b>Fuerza y potencia</b>", "Bajan más rápido que el músculo: cuesta más levantar, empujar o subir escaleras rápido."],
 ["<b>Grasa abdominal</b>", "Tiende a acumularse más en la cintura, sobre todo con poco movimiento y mal descanso."],
 ["<b>Recuperación</b>", "Necesitás un poco más de descanso entre sesiones intensas."],
])}
<h2>Señales de que perdiste fuerza</h2>
{checks(["Te cuesta levantarte del piso sin apoyar las manos.", "Subir dos pisos por escalera te deja agitado.",
         "Cargar las bolsas del súper o una valija te pesa más que antes.", "Te duele la espalda después de estar mucho tiempo sentado.", "Te cansás antes que tus amigos en un partido o una caminata larga."])}
''', chapter="01 · Después de los 40", pid="c1", toc="01 · Qué cambia después de los 40")

page(f'''
{eyebrow("DESPUÉS DE LOS 40")}
<h1 class="h1">Por qué la fuerza <span class="t">es la base</span></h1>
{box("<b>Lo que no cambia:</b> el músculo sigue respondiendo a la fuerza a cualquier edad. Con un plan, carga progresiva y constancia se puede ganar fuerza y masa muscular después de los 40, los 50 y los 60.", "soft")}
{tips([("Más músculo", "Es el estímulo que más ayuda a conservar y ganar masa muscular."),
       ("Mejor composición", "Junto con la alimentación, ayuda a bajar grasa sin perder músculo."),
       ("Vida diaria", "Cargar, levantarte del piso, jugar con tus hijos o nietos: todo es fuerza."),
       ("Huesos y articulaciones", "La carga progresiva estimula el hueso y fortalece lo que sostiene tus articulaciones.")])}
{table(["Fuerza", "Cardio"], [
 ["Construye y conserva músculo", "Mejora el corazón y la resistencia"],
 ["Sube el gasto de energía en reposo", "Gasta energía mientras lo hacés"],
 ["Mejora la postura y la capacidad de cargar", "Ayuda a recuperarte entre sesiones"],
])}
<p class="small"><b>No es fuerza o cardio:</b> en este programa la fuerza es la base y la caminata los días libres completa el trabajo.</p>
''', chapter="01 · Después de los 40", pid="c1b")

# ================================================================== 02
page(f'''
{chap_head("02", 'Antes de <span class="t">empezar</span>', "Dos minutos que te ahorran problemas.")}
<h2>Consultá a tu médico antes de empezar si…</h2>
{checks(["Tenés presión alta, diabetes, problemas cardíacos o tomás medicación de forma habitual.",
         "Hace años que no hacés actividad física y tenés sobrepeso importante.",
         "Tuviste una lesión, cirugía o dolor articular que todavía te molesta.",
         "Sentiste dolor en el pecho, falta de aire o mareos al hacer esfuerzo."])}
{box("<b>Pará la sesión y consultá</b> si aparece dolor en el pecho, falta de aire fuera de lo normal, mareos o un dolor articular punzante.", "note")}
<h2>Registrá tu punto de partida</h2>
{table(["Qué medir", "Cómo"], [
 ["Peso", "En ayunas, misma balanza, mismo día de la semana."],
 ["Cintura", "A la altura del ombligo, de pie y sin apretar la cinta."],
 ["Foto", "De frente y de perfil, con la misma luz y la misma ropa."],
 ["Cargas", "Los pesos de tu semana 1, en la planilla (página " + pref("cargas") + ")."],
])}
''', chapter="02 · Antes de empezar", pid="c2", toc="02 · Antes de empezar")

# ================================================================== 03
page(f'''
{chap_head("03", 'Cómo funciona <span class="t">el programa</span>', "Tres rutinas, tres días, dos fases.")}
{table(["Rutina", "Foco", "Página"], [[f"<b>{r}</b>", FOCO[r].capitalize(), pref(f"r{r}")] for r in "ABC"])}
<h2>Las fases</h2>
{tips([("Semanas 1 a 4", "Fase 1: aprendé la técnica y construí la base. 3 series, más repeticiones."),
       ("Semana 5", "Descarga: menos series y menos peso para recuperarte."),
       ("Semanas 6 a 8", "Fase 2: más series, menos repeticiones y más carga.")], "t3")}
<h2>Tu semana</h2>
{table(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"], [["Rutina A", "Caminata", "Rutina B", "–", "Rutina C", "Caminata", "–"]])}
<p class="small">Dejá siempre un día entre dos sesiones de fuerza. La caminata (30 a 40 minutos) es opcional y suma a la salud y a bajar grasa.</p>
{box("<b>¿Solo podés 2 días?</b> Hacé A y B una semana, C y A la siguiente, y así. Vas más lento, pero seguís progresando.", "")}
''', chapter="03 · El programa", pid="c3", toc="03 · Cómo funciona el programa")

# ================================================================== 04
page(f'''
{chap_head("04", 'Esfuerzo, cargas <span class="t">y progresión</span>', "Cómo elegir el peso y cuándo subirlo, sin adivinar.")}
<h2>La escala de esfuerzo (1 a 10)</h2>
{table(["Esfuerzo", "Cómo se siente", "Cuándo"], [
 ["<b>6</b>", "Te quedan 4 repeticiones en reserva.", "Semanas 1 y 2"],
 ["<b>7</b>", "Te quedan 3. Las últimas cuestan.", "Semanas 3 y 4"],
 ["<b>8</b>", "Te quedan 2, con buena técnica.", "Semanas 6 a 8"],
])}
<h2>Cómo elegir el peso la primera semana</h2>
{table(["Si en la última serie…", "Entonces"], [
 ["Te sobraron más de 5 repeticiones", "Subí el peso en la serie siguiente."],
 ["Te sobraron 3 o 4", "Es el peso correcto para empezar."],
 ["No llegaste o perdiste la técnica", "Bajá el peso."],
])}
<h2>La regla del rango</h2>
<ol class="steps-ol">
<li>La primera semana, elegí un peso con el que hagas las repeticiones del plan con el esfuerzo indicado.</li>
<li>Cuando completes <b>todas las series con el tope del rango</b> y buena técnica, subí la carga en la sesión siguiente.</li>
<li>{G("Si no tenés más peso: bajá en 3 segundos, sumá una pausa abajo o pasá a la variante más difícil.", "Subí lo mínimo: 1 a 2 kg en mancuernas, 2,5 a 5 kg en barra o máquina.")}</li>
</ol>
{box("<b>La técnica manda.</b> Si el peso te cambia el movimiento, es demasiado. Nunca hace falta llegar al fallo.", "soft")}
''', chapter="04 · Cargas", pid="c4", toc="04 · Esfuerzo, cargas y progresión")

# ================================================================== 05 · CALENTAMIENTO
page(f'''
{chap_head("05", 'Calentamiento <span class="t">y movilidad</span>', "8 minutos, antes de cada rutina. No lo saltees: después de los 40 es lo que te deja entrenar con carga.")}
{params([("Duración", "8 min"), ("Vueltas", "1"), ("Cada ejercicio", "45 s"), ("Cuándo", "Siempre")])}
{block_head("CIRCUITO", "1 vuelta · 45 segundos cada ejercicio · " + G("después, 2 minutos de saltar o marcha rápida", "antes, 3 minutos de bici o cinta"))}
{"".join(card(k) for k in CALOR[:2])}
{box("<b>¿Poco tiempo?</b> Nunca recortes el calentamiento: recortá un ejercicio del final de la rutina.", "soft")}
''', chapter="05 · Calentamiento", pid="c5", toc="05 · Calentamiento y movilidad")
page(f'''
{eyebrow("CALENTAMIENTO")}
{"".join(card(k) for k in CALOR[2:])}
<h2>Series de aproximación</h2>
{table(["Antes del primer ejercicio pesado", "Peso", "Repeticiones"], [["Serie 1", "50 % del peso de trabajo", "10"], ["Serie 2", "75 % del peso de trabajo", "5"]])}
''', chapter="05 · Calentamiento", pid="c5b")

# ================================================================== 06 · RUTINAS
for r in "ABC":
    ejs = RUT[r]
    page(f'''
{chap_head("06" if r == "A" else "", f'Rutina {r}: <span class="t">{FOCO[r]}</span>', "Tu resumen para la sesión. La técnica, en las páginas siguientes.") if r == "A" else eyebrow(f"RUTINA {r} · {LUGAR}") + f'<h1 class="h1">Rutina {r}: <span class="t">{FOCO[r]}</span></h1>'}
{table(["Ejercicio", "Músculos", "Sem. 1–4", "Sem. 6–8", "Descanso"], [[f"<b>{E[k][1]}</b>", E[k][2], f1, f2, d] for k, f1, f2, d in ejs], first="30%")}
<p class="small">Hacé los ejercicios en el orden de la tabla, todas las series de uno antes de pasar al siguiente. Semana 5 (descarga): 2 × 10 con el 70 % del peso. Antes, el calentamiento (página {pref("c5")}).</p>
<h2>Claves de esta rutina</h2>
{checks(CLAVES[r])}
''', chapter=f"06 · Rutina {r}", pid=f"r{r}", toc=f"Rutina {r} · {FOCO[r]}")
    page(f'''
{eyebrow(f"RUTINA {r} · {LUGAR} · 1 DE 2")}
{"".join(card(k) for k, *_ in ejs[:3])}
''', chapter=f"06 · Rutina {r}", pid=f"r{r}1")
    page(f'''
{eyebrow(f"RUTINA {r} · {LUGAR} · 2 DE 2")}
{"".join(card(k) for k, *_ in ejs[3:])}
<p class="small"><b>Al terminar:</b> anotá las cargas en tu planilla y caminá 5 minutos para bajar pulsaciones.</p>

''', chapter=f"06 · Rutina {r}", pid=f"r{r}2")

# ================================================================== 07 · PLAN
page(f'''
{chap_head("07", 'Tu plan de <span class="t">8 semanas</span>', "Qué cambia cada semana.")}
{table(["Semana", "Series × reps", "Esfuerzo", "Descanso", "Objetivo"], [
 ["<b>1–2</b>", "Fase 1 de la tabla", "6", "60–90 s", "Aprender la técnica y elegir cargas"],
 ["<b>3–4</b>", "Fase 1 de la tabla", "7", "60–90 s", "Subir la carga con la regla del rango"],
 ["<b>5</b>", "2 × 10", "5", "60 s", "Descarga: recuperar"],
 ["<b>6–7</b>", "Fase 2 de la tabla", "8", "90 s – 2 min", "Más series y más carga"],
 ["<b>8</b>", "Fase 2 de la tabla", "8", "90 s – 2 min", "Comparar con la semana 1"],
])}
{tips([("Fase 1", "Semanas 1 a 4. Aprendé, construí la base y empezá a subir carga."),
       ("Descarga", "Semana 5. Menos series y peso: el cuerpo asimila lo hecho."),
       ("Fase 2", "Semanas 6 a 8. Más series, menos repeticiones y más carga.")], "t3")}
{box("<b>Semana 8:</b> compará tus cargas, tu cintura y tus fotos con la semana 1 (página " + pref("progreso") + ").", "soft")}
''', chapter="07 · Plan", pid="plan", toc="07 · Tu plan de 8 semanas")

page(f'''
{eyebrow("TU PLAN DE 8 SEMANAS")}
<h1 class="h1">Calendario: <span class="t">tildá cada sesión</span></h1>
<p class="lead">Marcá cada sesión que hacés. Ver las tildes juntas es lo que te sostiene en las semanas difíciles.</p>
<div class="tall">{table(["Semana", "Rutina A", "Rutina B", "Rutina C", "Caminatas"], [[f"<b>{s}</b>" + (" · descarga" if s == 5 else ""), "☐", "☐", "☐", "☐ ☐"] for s in range(1, 9)])}</div>
{box("<b>Agendá tus 3 días</b> como si fueran reuniones: día y hora fijos. Lo que está en la agenda se hace.", "soft")}
''', chapter="07 · Plan", pid="calendario", toc="Calendario de 8 semanas")

# ================================================================== 08 · ERRORES
ERR = [("Arrancar con demasiado peso", "Las primeras dos semanas son para aprender. El ego es la lesión más común después de los 40."),
       ("Saltear el calentamiento", "Son 8 minutos. Sin ellos, las articulaciones llegan frías a la carga."),
       ("Entrenar siempre al fallo", "Dejá 2 o 3 repeticiones en reserva. Progresás igual y te recuperás mejor."),
       ("No anotar", "Sin planilla no sabés si subiste o no. La memoria engaña."),
       ("Hacer solo cardio para bajar la panza", "El cardio suma, pero la fuerza conserva el músculo mientras bajás grasa."),
       ("Dormir poco", "Menos de 6 horas frena la recuperación y aumenta el hambre."),
       ("Ignorar un dolor articular", "El dolor muscular es normal; el articular punzante, no. Cambiá el ejercicio y consultá."),
       ("Compararte con tus 25 años", "Tu referencia es tu semana anterior, no tu yo de antes.")]
page(f'''
{chap_head("08", 'Errores frecuentes <span class="t">después de los 40</span>', "Los que más frenan el progreso, y cómo evitarlos.")}
<div class="mitos">{"".join(f"<div><b>{t}</b><p>{p}</p></div>" for t, p in ERR)}</div>
{box("<b>¿Tenés una lesión vieja</b> en hombro, rodilla o espalda? Empezá todos los ejercicios con la opción de principiante y subí de a poco. Si duele, consultá.", "note")}
''', chapter="08 · Errores", pid="c8", toc="08 · Errores frecuentes")

# ================================================================== 09 · ALIMENTACIÓN
page(f'''
{chap_head("09", 'Comer para ganar músculo <span class="t">y bajar grasa</span>', "Sin dietas raras: cuatro claves que hacen la diferencia.")}
{tips([("Proteína en cada comida", "Carne, pollo, pescado, huevos, lácteos o legumbres en desayuno, almuerzo y cena."),
       ("Plato ordenado", "Mitad verduras, un cuarto proteína y un cuarto hidratos (arroz, papa, pan, fideos)."),
       ("Alcohol con medida", "Suma calorías, empeora el sueño y frena la recuperación. Que sea ocasional."),
       ("Agua", "Tomá agua durante el día y en cada sesión. Muchas veces la sed parece hambre.")])}
{table(["Si querés…", "Qué hacer"], [
 ["Bajar grasa", "Comé un poco menos de lo habitual, sin bajar la proteína. Bajar de golpe hace perder músculo."],
 ["Ganar músculo", "Comé lo suficiente: si el peso no se mueve y no progresás en cargas, sumá una colación con proteína."],
])}
{box("<b>Las cantidades exactas dependen de tu peso, tu salud y tus objetivos.</b> Si tenés una condición médica, consultá con un nutricionista.", "note")}
''', chapter="09 · Alimentación", pid="c9", toc="09 · Comer para ganar músculo")

# ================================================================== 10 · RECUPERACIÓN
page(f'''
{chap_head("10", 'Recuperación <span class="t">y constancia</span>', "El músculo crece cuando descansás.")}
{table(["Tema", "Qué hacer"], [
 ["<b>Sueño</b>", "Apuntá a 7 u 8 horas. Mismo horario para acostarte y levantarte."],
 ["<b>Dolor muscular</b>", "Es normal las primeras semanas (1 a 3 días). Moverte suave ayuda."],
 ["<b>Dolor articular</b>", "Punzante o que no baja: cambiá el ejercicio por la opción de principiante y consultá."],
 ["<b>Semana complicada</b>", "Hacé 2 sesiones en vez de 3. Mejor dos que ninguna."],
 ["<b>Perdiste una semana</b>", "Volvé con las cargas de la semana anterior y seguí el plan."],
 ["<b>Estrés</b>", "La caminata y la respiración lenta después de entrenar ayudan a bajar revoluciones."],
 ["<b>Días libres</b>", "Caminá y hacé el calentamiento como rutina de movilidad: 10 minutos."],
 ["<b>Después de entrenar</b>", "Una comida con proteína en las 2 a 3 horas siguientes ayuda a recuperarte."],
])}
{box("<b>La constancia le gana a la intensidad.</b> Tres sesiones correctas por semana durante 8 semanas valen más que dos semanas perfectas y un abandono.", "soft")}
''', chapter="10 · Recuperación", pid="c10", toc="10 · Recuperación y constancia")

# ================================================================== PLANILLAS
EJ_CLAVE = [E[k][1] for r in "ABC" for k, *_ in RUT[r][:4]]
page(f'''
{eyebrow("HERRAMIENTA")}
<h1 class="h1">Planilla <span class="t">de cargas</span></h1>
<p class="small">Anotá el peso y las repeticiones de la última serie. Ejemplo: <b>20 kg × 10</b>. {G("Si es con peso corporal, anotá las repeticiones.", "")}</p>
<div class="mid">{table(["Ejercicio", "S1", "S2", "S3", "S4", "S6", "S7", "S8"], [[e] + [""] * 7 for e in EJ_CLAVE], first="34%")}</div>
''', chapter="Herramientas", pid="cargas", toc="Herramienta: planilla de cargas")

page(f'''
{eyebrow("HERRAMIENTA")}
<h1 class="h1">Registro <span class="t">de progreso</span></h1>
<div class="tall">{table(["Medida", "Semana 1", "Semana 4", "Semana 8"], [["Peso (kg)", "", "", ""], ["Cintura (cm)", "", "", ""], ["Foto de frente y perfil", "☐", "☐", "☐"],
 ["Cómo duermo (1 a 10)", "", "", ""], ["Energía en el día (1 a 10)", "", "", ""], ["Cómo me siento al entrenar (1 a 10)", "", "", ""]], first="40%")}</div>
<h2>Mis 3 objetivos para estas 8 semanas</h2>
{table(["Objetivo", "Cómo lo mido"], [["1", ""], ["2", ""], ["3", ""]], first="50%")}
{box("<b>Mirá la tendencia, no un día.</b> El peso sube y baja por agua y comida. La cintura y las cargas cuentan mejor la historia.", "soft")}
''', chapter="Herramientas", pid="progreso", toc="Herramienta: registro de progreso")

# ================================================================== 11 · DESPUÉS
page(f'''
{chap_head("11", 'Después de las <span class="t">8 semanas</span>', "Compará la semana 8 con la 1 y elegí cómo seguir.")}
{tips([("Repetí con más carga", "Volvé a la semana 1 con los pesos de tu semana 8. Es un nuevo ciclo más exigente."),
       ("Mantené", "Seguí 3 días por semana rotando A, B y C con esfuerzo 7. Conservás lo ganado."),
       ("Cambiá de modalidad", G("Si tenés acceso a un gimnasio, pasá al ebook de gimnasio: mismo sistema, más carga.", "Si una temporada no podés ir, seguí con el ebook de casa: mismo sistema."))], "t3")}
<h2>Cómo armar el nuevo ciclo</h2>
{table(["Si en la semana 8…", "En el nuevo ciclo"], [
 ["Completaste todo con buena técnica", "Empezá con los pesos de la semana 8 y repetí el plan."],
 ["Te costó sostener 3 días", "Hacé 2 días por semana con la rotación de 2 días (capítulo 03)."],
 ["Algún ejercicio te molesta", "Usá su opción de principiante o consultá por un plan a medida."],
])}
<h2>Qué cambió para vos</h2>
{checks(["Levanto más peso que en la semana 1.", "Mi cintura bajó o se mantuvo mientras subían las cargas.",
         "Duermo mejor y tengo más energía.", "Las tareas del día me cuestan menos."])}
''', chapter="11 · Después", pid="c11", toc="11 · Después de las 8 semanas")

# ================================================================== AUTOR
page(f'''
{eyebrow("EL AUTOR")}
<div class="bio-m"><img src="img/m40/autor.jpg" alt="{AUTOR}"><div>
<h1 class="h1">{AUTOR}</h1>
<p class="lead">{AUTOR_TIT}.</p>
<p>Más de 15 años entrenando personas y preparando deportistas. Armé MÉTODO 40 para los hombres que quieren volver a entrenar en serio sin vivir en el gimnasio: un plan claro, con carga progresiva y la técnica explicada como la explico en el día a día.</p>
</div></div>
<h2>Trayectoria</h2>
{checks(["Licenciado en Alto Rendimiento Deportivo.", "Preparador físico de fútbol profesional.", "Más de 15 años en entrenamiento de fuerza y preparación física.", "Creador de MÉTODO 40."])}
{box("<b>Este programa es una guía general.</b> No reemplaza la consulta médica. Los resultados dependen de cada persona: tu punto de partida, tu constancia, tu descanso y tu alimentación.", "note")}
<div class="quote dark">La fuerza no se pierde con la edad. <span class="t2">Se pierde cuando dejás de entrenarla.</span></div>
''', chapter="El autor", pid="autor", toc="El autor")


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
                    f'<p class="idxtip">{ICON_HAND} Tocá donde quieras ir. Para volver al índice, abajo de cada página tenés el botón.</p></div>{toc_html}{INICIO}')
        hdr = ""
        if p["header"]:
            hdr = (f'<div class="hdr"><span>MÉTODO <b>40</b> · {G("CASA", "GIMNASIO")}</span><span>{esc(p["chapter"])}</span></div>'
                   f'<div class="ftr"><a class="toidx" href="#indice">{ICON_HAND} Volvé al índice</a><span class="pgnum"></span></div>')
        out.append(f'<section class="page {p["cls"]}" id="{p["id"]}">{hdr}<div class="body">{body}</div></section>')
    css = ds_css(HERE) + "\n" + open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>MÉTODO 40 · {G("En casa", "En el gimnasio")}</title>'
            f'<style>{css}</style></head><body class="grande m40">' + "".join(out) + '<script src="paginate.js"></script></body></html>')


if __name__ == "__main__":
    out = f"hombres_{ED}.html"
    with open(os.path.join(HERE, out), "w", encoding="utf-8") as f:
        f.write(render())
    print(out, "·", len(PAGES), "páginas:", " ".join(f"{i + 1}:{p['id']}" for i, p in enumerate(PAGES)))
