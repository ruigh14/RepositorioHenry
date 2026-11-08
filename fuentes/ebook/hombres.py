"""MÉTODO 40 · Entrenamiento de fuerza para hombres 40+ (submarca para la otra tienda de Impultienda).
Tres ebooks que se venden juntos (el de métricas va de regalo), desde el mismo script:
  python3 hombres.py casa     → hombres_casa.html     → metodo-40/Ebook_Metodo40_Casa.pdf       (node export.js hombres_casa)
  python3 hombres.py gym      → hombres_gym.html      → metodo-40/Ebook_Metodo40_Gimnasio.pdf   (node export.js hombres_gym)
  python3 hombres.py metricas → hombres_metricas.html → metodo-40/Ebook_Metodo40_Metricas.pdf   (node export.js hombres_metricas)
Upsell (aparte del pack): "Zona media fuerte", rutinas de abdominales con mitos y cuidados (sin giro ruso ni toes to bar):
  python3 hombres.py abdomen  → hombres_abdomen.html  → metodo-40/Ebook_Metodo40_Zona_Media.pdf  (node export.js hombres_abdomen)

Programa: 8 semanas, 3 días por semana, rutinas de cuerpo completo A/B/C que rotan. Planificación ondulada:
la carga sube cada semana (1→2→3 y 5→6→7) con descarga en la 4 y en la 8 (la 8 incluye la evaluación de fuerza).
El esfuerzo se controla con RIR (repeticiones en reserva). Miembros inferiores: solo ejercicios bipodales.
Gimnasio: cada rutina suma un ejercicio de brazos.
Cada ejercicio usa un video propio de Ignacio en Harbiz (con la marca LEVEL UP: Nacho decidió dejarla) y una captura
de ese video (img/m40/). La guía de métricas enseña a medir (balanza, cinta, fotos), a evaluar la fuerza con RIR y a
usar el tablero web (fuentes/tablero/). Paleta: tokens --m40-* (body.m40 en style.css).
Cada hoja se arma completa a mano: ningún bloque partido entre hojas y sin huecos grandes (ver FREE de export.js).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "design-system"))
from design_system import css as ds_css, esc, ICON_ARROW, ICON_HAND, ICON_PLAY, eyebrow, chap_head, ul, checks, box, block_head, params

ED = sys.argv[1] if len(sys.argv) > 1 else "casa"
assert ED in ("casa", "gym", "metricas", "abdomen"), "edición: casa, gym, metricas o abdomen"
GYM = ED == "gym"
MET = ED == "metricas"
ABD = ED == "abdomen"


def G(casa, gym):
    return gym if GYM else casa


LUGAR = {"casa": "EN CASA", "gym": "EN EL GIMNASIO", "metricas": "GUÍA DE MÉTRICAS", "abdomen": "COMPLEMENTO · 8 SEMANAS"}[ED]
AUTOR = "Ignacio Portillo"
AUTOR_TIT = "Licenciado en Alto Rendimiento Deportivo · Preparador físico de fútbol profesional"   # Racing: solo con autorización
LINK_TABLERO = ""   # link del tablero web publicado (fuentes/tablero/); mientras esté vacío, el ebook muestra "LINK PENDIENTE"
PAGES, TOC = [], []
INDICE_EXTRA = []   # bloques que se suman debajo del índice


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


def boton_tablero():
    if LINK_TABLERO:
        return f'<div class="cta-center"><a class="btn btn-big" href="{esc(LINK_TABLERO)}">ABRIR MI TABLERO {ICON_ARROW}</a></div>'
    return '<div class="cta-center"><span class="btn btn-big">ABRIR MI TABLERO · LINK PENDIENTE</span></div>'


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
    "remo_unilateral": ("remo_unilateral", "Remo con mancuerna", "Espalda y bíceps", "Una mano y una rodilla apoyadas. Llevá la mancuerna hacia la cadera, con el codo pegado al cuerpo.", "girar el tronco para subir el peso.", "con menos peso y más control.", "1 mancuerna y banco", "https://youtu.be/6a1emLHfGYg"),
    "press_hombros_arrodillado": ("press_hombros_arrodillado", "Press de hombros arrodillado", "Hombros y tríceps", "Arrodillado, abdomen firme. Empujá la mancuerna hacia arriba hasta estirar el brazo, sin arquear la espalda.", "inclinarte hacia atrás para empujar.", "con menos peso.", "Mancuernas", "https://youtu.be/RZXbCZ_fneQ"),
    "plancha_frontal": ("plancha_frontal", "Plancha frontal", "Zona media", "Antebrazos apoyados, cuerpo en línea de hombros a talones. Apretá abdomen y glúteos.", "cadera muy alta o caída.", "con las rodillas apoyadas.", "Colchoneta", "https://youtu.be/nd0qbgESlao"),
    "swing": ("swing", "Swing con pesa rusa", "Glúteos, isquiotibiales y zona media", "Pies al ancho de hombros. Llevá la cadera atrás con la pesa entre las piernas y extendé la cadera con fuerza: la pesa sube por el impulso.", "subir la pesa con los brazos o redondear la espalda.", "peso muerto con mancuerna, sin impulso.", "Pesa rusa o mancuerna", "https://youtu.be/-y2HmihdvbE"),
    "sentadilla_sumo": ("sentadilla_sumo", "Sentadilla sumo", "Cuádriceps, aductores y glúteos", "Pies bien abiertos, puntas hacia afuera, peso entre las piernas. Bajá con el torso alto y subí empujando el piso.", "rodillas que se cierran.", "sin peso.", "Mancuerna o pesa rusa", "https://youtu.be/Ro3dhcOXiYw"),
    "fondos_banco": ("fondos_banco", "Fondos de tríceps en banco", "Tríceps y pecho", "Manos en el borde del banco, cola cerca. Bajá doblando los codos hacia atrás y empujá.", "bajar demasiado y forzar el hombro.", "con las rodillas flexionadas y menos recorrido.", "Banco o silla", "https://youtu.be/FqLq6-WRoqw"),
    "vuelo_posterior": ("vuelo_posterior", "Vuelo posterior con mancuernas", "Hombros posteriores y espalda alta", "Tronco inclinado y espalda recta. Abrí los brazos hacia los costados con los codos apenas flexionados.", "tirar con impulso del tronco.", "con botellas o menos peso.", "2 mancuernas", "https://youtu.be/Stpq0KwR5iQ"),
    "curl_biceps": ("curl_biceps", "Curl de bíceps con mancuernas", "Bíceps", "Codos pegados al cuerpo. Subí las mancuernas girando las palmas hacia arriba y bajá lento.", "balancear el cuerpo.", "curl con banda elástica.", "2 mancuernas", "https://youtu.be/ToxLEnNgKXA"),
    "bicho_muerto_botella": ("bicho_muerto_botella", "Bicho muerto con peso", "Zona media", "Boca arriba, brazos y rodillas a 90°. Estirá brazo y pierna contraria sin despegar la zona lumbar del piso.", "arquear la espalda al estirar.", "sin peso y con menos recorrido.", "Botella o mancuerna", "https://youtu.be/MqbAxttwogg"),
    "sentadilla_cajon": ("sentadilla_cajon", "Sentadilla a cajón con pausa", "Cuádriceps y glúteos", "Bajá controlado hasta rozar el banco o cajón, pausa de 1 segundo sin relajarte y subí empujando con los talones.", "dejarte caer sobre el cajón.", "un cajón más alto.", "Banco o cajón y mancuerna", "https://youtu.be/gFTgLpn08Xc"),
    "puente_peso": ("puente_peso", "Puente de glúteos con peso", "Glúteos e isquiotibiales", "Boca arriba, pies apoyados y mancuerna sobre la cadera. Subí la cadera apretando glúteos 2 segundos arriba.", "empujar con la zona lumbar.", "sin peso.", "Mancuerna y colchoneta", "https://youtu.be/YopfscyxtK0"),
    "push_press": ("push_press", "Push press con mancuernas", "Hombros, tríceps y piernas", "Mancuernas a la altura de los hombros. Flexioná apenas las rodillas y empujá con las piernas y los brazos hacia arriba.", "arquear la espalda al final.", "press de hombros con banda.", "2 mancuernas", "https://youtu.be/2ZDHMjr2pkM"),
    "renegade_row": ("renegade_row", "Remo en plancha (renegade row)", "Espalda, zona media y hombros", "En plancha alta con las manos sobre las mancuernas, pies abiertos. Remá con un brazo sin girar la cadera.", "rotar el cuerpo al subir el peso.", "remo con mancuerna apoyado en un banco.", "2 mancuernas", "https://youtu.be/ouNjv25ffI4"),
    "elevaciones_laterales": ("elevaciones_laterales", "Elevaciones laterales", "Hombros", "Codos apenas flexionados. Subí los brazos a los costados hasta la altura de los hombros y bajá lento.", "subir con impulso o por encima de los hombros.", "con botellas o de a un brazo.", "2 mancuernas", "https://youtu.be/vguq1MBRh_Y"),
    "plancha_lateral": ("plancha_lateral", "Plancha lateral", "Oblicuos y zona media", "Apoyado en un antebrazo, cuerpo en línea. Mantené la cadera alta.", "dejar caer la cadera.", "con la rodilla de abajo apoyada.", "Colchoneta", "https://youtu.be/bxQgU1eK4dc"),
    "press_pallof": ("press_pallof", "Press Pallof", "Zona media (antirrotación)", G("Banda atada a la altura del pecho, de costado. Llevá las manos al frente sin dejar que el tronco gire.", "Polea a la altura del pecho, de costado. Llevá las manos al frente sin dejar que el tronco gire."),
                     "girar el tronco hacia la banda.", "más cerca del anclaje, menos tensión.", G("Banda elástica", "Polea"), "https://youtu.be/t9jDygFEbU0"),
    # gimnasio
    "sentadilla_barra": ("sentadilla_barra", "Sentadilla con barra", "Cuádriceps, glúteos y zona media", "Barra apoyada en la parte alta de la espalda. Bajá con la cadera atrás y las rodillas siguiendo las puntas; subí empujando el piso.", "despegar los talones o redondear la espalda.", "prensa.", "Barra y rack", "https://youtu.be/idl_EYsUlzQ"),
    "curl_isquio": ("curl_isquio", "Curl de isquiotibiales sentado", "Isquiotibiales", "Rodillas alineadas con el eje de la máquina. Flexioná bajando el rodillo y volvé con control.", "levantar la cadera del asiento.", "con menos peso.", "Máquina", "https://youtu.be/8I7lYLxvAf0"),
    "press_plano": ("press_plano", "Press plano con barra", "Pecho, hombros y tríceps", "Pies firmes en el piso, escápulas juntas. Bajá la barra al pecho con los codos a 45° y empujá.", "rebotar la barra en el pecho.", "press de pecho en máquina.", "Barra y banco", "https://youtu.be/HDmYWB7TEds"),
    "remo_polea_baja": ("remo_polea_baja", "Remo en polea baja", "Espalda y bíceps", "Espalda derecha. Llevá el agarre hacia el abdomen juntando las escápulas y volvé sin perder la postura.", "tirar con el tronco hacia atrás.", "con menos peso.", "Polea", "https://youtu.be/hkFC0uc7G6A"),
    "biceps_polea": ("biceps_polea", "Curl de bíceps en polea", "Bíceps", "Barra en la polea baja, codos pegados al cuerpo. Subí la barra sin mover los codos y bajá lento.", "balancear el tronco.", "con menos peso.", "Polea y barra", "https://www.youtube.com/shorts/oJGSW0z5Hew"),
    "peso_muerto_barra": ("peso_muerto_barra", "Peso muerto con barra", "Glúteos, isquiotibiales y espalda", "Barra pegada a las piernas, espalda recta. Llevá la cadera atrás para bajar y subí empujando el piso.", "redondear la espalda o alejar la barra.", "peso muerto rumano en máquina.", "Barra", "https://youtu.be/MeXBpLzezlw"),
    "hack": ("hack", "Sentadilla hack", "Cuádriceps y glúteos", "Espalda apoyada en el respaldo, pies al ancho de hombros. Bajá controlado y empujá sin bloquear las rodillas.", "despegar la espalda del respaldo.", "con menos peso y recorrido.", "Máquina", "https://youtu.be/pxVyXSOplss"),
    "ext_cuadriceps": ("ext_cuadriceps", "Extensión de cuádriceps", "Cuádriceps", "Rodilla alineada con el eje de la máquina. Estirá las piernas, pausa arriba y bajá lento.", "levantar la cola del asiento.", "con menos peso.", "Máquina", "https://youtu.be/xxGUzhNzyh4"),
    "press_45_barra": ("press_45_barra", "Press inclinado con barra", "Pecho alto y hombros", "Banco a 45°, escápulas juntas. Bajá la barra a la parte alta del pecho y empujá.", "despegar la cola del banco.", "press inclinado con mancuernas.", "Barra y banco inclinado", "https://youtu.be/N7yZeklJkE8"),
    "jalones": ("jalones", "Jalón al pecho", "Dorsales y bíceps", "Agarre un poco más abierto que los hombros. Llevá la barra a la clavícula con el pecho alto.", "tirar hacia atrás con todo el cuerpo.", "con menos peso.", "Polea alta", "https://youtu.be/Vfeh314bQX4"),
    "face_pull": ("face_pull", "Face pull", "Hombros posteriores y manguito rotador", "Soga a la altura de la cara. Tirá hacia los ojos abriendo los codos hacia afuera.", "subir los hombros a las orejas.", "con menos peso.", "Polea y soga", "https://youtu.be/R1FeK4isaHE"),
    "press_frances": ("press_frances", "Press francés con mancuernas", "Tríceps", "Acostado en el banco, mancuernas arriba. Bajalas hacia los costados de la cabeza doblando solo los codos y volvé.", "abrir los codos hacia afuera.", "con menos peso.", "Banco y mancuernas", "https://youtu.be/bE-34UluKFA"),
    "pm_rumano_maquina": ("pm_rumano_maquina", "Peso muerto rumano en máquina", "Isquiotibiales y glúteos", "Rodillas apenas flexionadas. Llevá la cadera atrás con la espalda recta hasta sentir los isquiotibiales y volvé apretando glúteos.", "redondear la espalda.", "con menos peso y recorrido.", "Máquina", "https://www.youtube.com/shorts/cR8Edd7GcbI"),
    "prensa": ("prensa", "Prensa", "Cuádriceps y glúteos", "Espalda apoyada, pies al ancho de la cadera. Bajá a 90° y empujá sin bloquear las rodillas.", "despegar la cola del asiento al bajar.", "con menos peso y recorrido.", "Máquina", "https://youtu.be/ddfmGBWmB88"),
    "press_militar_maquina": ("press_militar_maquina", "Press de hombros en máquina", "Hombros y tríceps", "Espalda apoyada. Empujá hacia arriba sin bloquear los codos y bajá hasta la altura del mentón.", "arquear la espalda.", "con menos peso.", "Máquina", "https://youtu.be/epNNDB486H4"),
    "remo_45_barra": ("remo_45_barra", "Remo inclinado con barra", "Espalda y bíceps", "Tronco inclinado a 45°, espalda recta. Llevá la barra hacia el abdomen y bajá con control.", "subir el tronco para ayudarte.", "remo en máquina.", "Barra", "https://youtu.be/6o78vcu6BOY"),
    "triceps_soga": ("triceps_soga", "Extensión de tríceps con soga", "Tríceps", "Codos fijos al costado del cuerpo. Estirá los brazos hacia abajo abriendo la soga al final.", "mover los codos hacia adelante.", "con menos peso.", "Polea y soga", "https://youtu.be/E5-R8s44Ix4"),
    "biceps_martillo": ("biceps_martillo", "Bíceps martillo", "Bíceps y antebrazo", "Palmas enfrentadas, codos pegados. Subí las mancuernas sin girar las muñecas y bajá lento.", "balancear el cuerpo.", "con menos peso.", "2 mancuernas", "https://youtu.be/UDhAd_wovw8"),
    # zona media (upsell)
    "plancha_alta": ("plancha_alta", "Plancha alta", "Zona media, hombros y pecho", "Manos debajo de los hombros, brazos estirados, cuerpo en línea. Apretá glúteos y abdomen.", "hundir la zona lumbar o subir la cadera.", "con las rodillas apoyadas.", "Colchoneta", "https://youtu.be/OsO8HdLap-o"),
    "plancha_alta_din": ("plancha_alta_din", "Plancha alta con alcance", "Zona media (antirrotación) y hombros", "En plancha alta con los pies abiertos, llevá una mano al frente y volvé, sin que la cadera se mueva ni gire.", "girar la cadera al levantar la mano.", "pies más abiertos o rodillas apoyadas.", "Colchoneta", "https://youtu.be/zVOcJUakivg"),
    "bicho_alt": ("bicho_alt", "Bicho muerto alternado", "Zona media (antiextensión)", "Boca arriba, brazos al techo y rodillas a 90°. Estirá brazo y pierna contraria exhalando, con la zona lumbar pegada al piso.", "arquear la espalda al estirar.", "mové solo las piernas.", "Colchoneta", "https://youtu.be/kgG0lb4XfMQ"),
    "bird_dog": ("bird_dog", "Bird dog", "Zona media y espalda baja", "En cuatro apoyos, estirá un brazo y la pierna contraria hasta la línea del cuerpo. Pausa de 2 segundos y alterná.", "girar la cadera o arquear la espalda.", "mové solo la pierna.", "Colchoneta", "https://youtu.be/kyNrWqz1iqs"),
    "mountain": ("mountain", "Mountain climber", "Zona media, hombros y cardio", "En plancha alta, llevá una rodilla hacia el pecho y volvé, alternando. La cadera queda a la altura de los hombros.", "subir la cola o rebotar con la cadera.", "más lento, apoyando el pie en cada paso.", "Propio cuerpo", "https://youtu.be/k9_dNW743ng"),
    "caminata_manos": ("caminata_manos", "Caminata de manos", "Zona media, hombros e isquiotibiales", "De pie, flexioná la cadera y caminá con las manos hasta la plancha alta; volvé caminando hasta quedar de pie.", "hundir la zona lumbar en la plancha.", "no llegues tan lejos con las manos.", "Propio cuerpo", "https://youtu.be/ZXnoeAd8B5c"),
    "flex_inclinadas": ("flex_inclinadas", "Flexiones inclinadas", "Pecho, tríceps y zona media", "Manos en un banco o cajón, cuerpo en línea. Bajá el pecho al borde y empujá.", "dejar caer la cadera.", "un apoyo más alto.", "Banco o cajón", "https://youtu.be/xr_4kJVoShc"),
    "flex_toque": ("flex_toque", "Flexión con toque de hombro", "Pecho, tríceps y zona media (antirrotación)", "Hacé una flexión y, arriba, tocá el hombro contrario con una mano, sin mover la cadera. Alterná.", "girar la cadera al tocar el hombro.", "con las rodillas apoyadas.", "Propio cuerpo", "https://www.youtube.com/shorts/cDSdmJ_9xvQ"),
    "flex_declinadas": ("flex_declinadas", "Flexiones declinadas", "Pecho alto, hombros y zona media", "Pies sobre un banco o cajón, manos en el piso. Bajá con el cuerpo en línea y empujá.", "dejar caer la cadera.", "flexiones comunes.", "Banco o cajón", "https://youtu.be/MBlrW8E_YFc"),
    "bicho_muerto_disco": ("bicho_muerto_disco", "Bicho muerto con disco", "Zona media", "Boca arriba, disco en las manos y rodillas a 90°. Estirá las piernas de a una sin despegar la zona lumbar.", "arquear la espalda.", "sin disco.", "Disco", "https://youtu.be/fKAKLkzfhvQ"),
}

CALOR = ["mov_cadera", "mov_escapular", "cat_cow", "mov_baston", "rodillas_arriba"]
# rutina → [(ejercicio, tipo)]: P = principal (sigue el plan ondulado), A = accesorio (3 × 12–15), Z = zona media
RUT = G({
    "A": [("sentadilla_copa", "P"), ("elevacion_cadera_cajon", "P"), ("flexiones", "P"), ("remo_unilateral", "P"), ("press_hombros_arrodillado", "A"), ("plancha_frontal", "Z")],
    "B": [("swing", "P"), ("sentadilla_sumo", "P"), ("fondos_banco", "P"), ("vuelo_posterior", "A"), ("curl_biceps", "A"), ("bicho_muerto_botella", "Z")],
    "C": [("sentadilla_cajon", "P"), ("puente_peso", "P"), ("push_press", "P"), ("renegade_row", "P"), ("elevaciones_laterales", "A"), ("plancha_lateral", "Z")],
}, {
    "A": [("sentadilla_barra", "P"), ("curl_isquio", "A"), ("press_plano", "P"), ("remo_polea_baja", "P"), ("elevaciones_laterales", "A"), ("biceps_polea", "A"), ("plancha_frontal", "Z")],
    "B": [("peso_muerto_barra", "P"), ("hack", "P"), ("ext_cuadriceps", "A"), ("press_45_barra", "P"), ("jalones", "P"), ("face_pull", "A"), ("press_frances", "A"), ("press_pallof", "Z")],
    "C": [("pm_rumano_maquina", "P"), ("prensa", "P"), ("press_militar_maquina", "P"), ("remo_45_barra", "P"), ("triceps_soga", "A"), ("biceps_martillo", "A"), ("bicho_muerto_disco", "Z")],
})
FOCO = G({"A": "piernas y empuje", "B": "bisagra y tirón", "C": "sentadilla y hombros"},
         {"A": "sentadilla y empuje", "B": "bisagra y tirón", "C": "piernas, espalda y brazos"})
TIPO = {"P": "Principal", "A": "Accesorio", "Z": "Zona media"}
DESC = {"P": G("90 s", "2 min"), "A": "60 s", "Z": "45 s"}
POR_HOJA = G(3, 4)   # ejercicios por hoja de rutina

# Plan ondulado: la carga sube cada semana y la 4 y la 8 son de descarga
PLAN = [("1", "3 × 12", "3", "Aprender la técnica y elegir cargas"), ("2", "3 × 10", "2–3", "Más peso, menos repeticiones"),
        ("3", "4 × 8", "2", "El pico del bloque 1"), ("4 · descarga", "2 × 10", "4", "Recuperar: mismo ejercicio, menos esfuerzo"),
        ("5", "4 × 10", "2", "Arranca el bloque 2, más pesado que la semana 2"), ("6", "4 × 8", "2", "Más peso que la semana 3"),
        ("7", "4 × 6", "1–2", "El pico del programa"), ("8 · descarga", "2 × 8", "4", "Recuperar y hacer la evaluación de fuerza")]

CLAVES = G({
    "A": ["La sentadilla es el ejercicio principal: hacela con la cabeza fresca.", "En las flexiones, el cuerpo es una tabla de la cabeza a los talones.", "Si las flexiones te salen fáciles, poné los pies en el banco."],
    "B": ["El swing es explosivo: la fuerza sale de la cadera, no de los brazos.", "En la sentadilla sumo, las rodillas siguen la dirección de las puntas.", "En los fondos, cuidá el hombro: bajá solo hasta los 90°."],
    "C": ["En la sentadilla a cajón, la pausa es activa: no te relajes sobre el banco.", "El push press usa las piernas: es un empuje explosivo, no un press estricto.", "En el remo en plancha, abrí los pies para no girar la cadera.", "Las elevaciones laterales van con poco peso: el hombro se trabaja con control."],
}, {
    "A": ["La sentadilla con barra es el ejercicio principal: hacela con la cabeza fresca.", "Hacé 2 series de aproximación antes de la sentadilla y del press plano."],
    "B": ["El peso muerto es el ejercicio más exigente del programa: técnica antes que kilos.", "Entre series de peso muerto, descansá completo: 2 minutos."],
    "C": ["En el rumano en máquina, la cadera va atrás y la espalda no se redondea.", "En la prensa, no bloquees las rodillas al estirar."],
})


def card(k):
    img, name, mus, how, evita, princ, mat, url = E[k]
    ev = f'<p class="ev"><b>Evitá:</b> {evita}</p>' if evita else ""
    pr = f'<p><b>Principiante:</b> {princ}</p>' if princ else ""
    return (f'<div class="mx"><div class="mx-l"><div class="mx-im"><img src="img/m40/{img}.jpg" alt=""></div><span class="mat">{mat}</span></div>'
            f'<div><div class="mx-h"><h4>{name}</h4><a class="vbtn-sm" href="{esc(url)}">{ICON_PLAY} VIDEO</a></div>'
            f'<span class="mus">{mus}</span><p>{how}</p>{ev}{pr}</div></div>')


def portada(titulo, sub):
    page(f'''
<div class="mcv">
  <img class="mcv-foto" src="img/m40/autor.jpg" alt="{AUTOR}">
  <div class="mcv-fade"></div>
  <div class="mcv-in">
    <div class="mcv-brand">MÉTODO <b>40</b></div>
    <div class="mcv-bar"></div>
    <h1>{titulo}</h1>
    <span class="mcv-lugar">{LUGAR}</span>
    <p class="mcv-sub">{sub}</p>
  </div>
  <div class="mcv-autor">{AUTOR.upper()}<small>Lic. en Alto Rendimiento Deportivo</small></div>
</div>
''', pid="portada", cls="p-cover", header=False)


def hoja_autor():
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


# =========================================================================================== PROGRAMA (casa / gimnasio)
def programa():
    portada('Fuerza<br>para hombres<br><span>40+</span>', "Programa de 8 semanas · 3 días por semana · 45 minutos")

    page(f'''
{eyebrow("BIENVENIDO")}
<h1 class="h1">Un plan para recuperar <span class="t">fuerza y músculo</span></h1>
<p class="lead">Después de los 40 el cuerpo cambia, pero sigue respondiendo al entrenamiento. Este programa te dice <b>qué hacer, cuántas veces, con qué carga y cómo progresar</b>, {G("en tu casa, con poco equipamiento", "en cualquier gimnasio")}.</p>
{table(["Qué es", "Cómo es"], [
 ["<b>Duración</b>", "8 semanas, en dos bloques de 4"],
 ["<b>Frecuencia</b>", "3 días por semana (por ejemplo, lunes, miércoles y viernes)"],
 ["<b>Cada sesión</b>", "8 minutos de calentamiento + 35 a 40 de fuerza"],
 ["<b>Rutinas</b>", "3 de cuerpo completo (A, B y C) que rotan"],
 ["<b>Material</b>", G("Mancuernas, pesa rusa, banda elástica, banco o silla firme y colchoneta", "Barras, mancuernas, máquinas y poleas")],
])}
<h2>Cómo usar este ebook</h2>
{checks(["Leé los capítulos 01 a 04 antes de la primera sesión: son 10 minutos.",
         "Cada ejercicio tiene su foto, la técnica, el error a evitar, la opción para principiantes y el <b>video</b>.",
         "Con el pack viene la <b>Guía de métricas</b>: cómo medirte, evaluar tu fuerza y usar tu tablero de progreso."])}
''', chapter="Bienvenido", pid="bienvenida")

    page("__TOC__", chapter="Índice", pid="indice")

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
         "Cargar las bolsas del súper o una valija te pesa más que antes.", "Te duele la espalda después de estar mucho tiempo sentado.",
         "Te cansás antes que tus amigos en un partido o una caminata larga."])}
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
 ["Peso, cintura y fotos", "Como explica la <b>Guía de métricas</b> que viene con el pack."],
 ["Fuerza", "Tu evaluación de la semana 1 (Guía de métricas, capítulo de fuerza)."],
 ["Cargas", "Los pesos de cada sesión, en la planilla (página " + pref("cargas") + ")."],
])}
''', chapter="02 · Antes de empezar", pid="c2", toc="02 · Antes de empezar")

    page(f'''
{chap_head("03", 'Cómo funciona <span class="t">el programa</span>', "Tres rutinas, tres días, dos bloques de 4 semanas.")}
{table(["Rutina", "Foco", "Página"], [[f"<b>{r}</b>", FOCO[r].capitalize(), pref(f"r{r}")] for r in "ABC"])}
<h2>Planificación ondulada</h2>
{tips([("Semanas 1 a 3", "La carga sube cada semana: menos repeticiones y más peso."),
       ("Semana 4", "Descarga: menos series y menos esfuerzo para recuperarte."),
       ("Semanas 5 a 8", "Segundo bloque, más pesado. La 8 es de descarga y evaluación.")], "t3")}
<h2>Tu semana</h2>
{table(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"], [["Rutina A", "Caminata", "Rutina B", "–", "Rutina C", "Caminata", "–"]])}
<p class="small">Dejá siempre un día entre dos sesiones de fuerza. La caminata (30 a 40 minutos) es opcional y suma a la salud y a bajar grasa.</p>
{box("<b>¿Solo podés 2 días?</b> Hacé A y B una semana, C y A la siguiente, y así. Vas más lento, pero seguís progresando.", "")}
''', chapter="03 · El programa", pid="c3", toc="03 · Cómo funciona el programa")

    page(f'''
{chap_head("04", 'Esfuerzo con <span class="t">RIR</span>', "RIR son las repeticiones que te quedan en reserva al terminar la serie. Es la forma de dosificar el esfuerzo sin llegar al fallo.")}
{table(["RIR", "Cómo se siente al terminar la serie"], [
 ["<b>4</b>", "Podrías hacer 4 repeticiones más. Esfuerzo moderado."],
 ["<b>3</b>", "Te quedan 3. Las últimas empiezan a costar."],
 ["<b>2</b>", "Te quedan 2. Es exigente, pero la técnica es perfecta."],
 ["<b>1</b>", "Te queda 1 sola. Solo en el pico del programa."],
 ["<b>0</b>", "Fallo: no podés hacer otra. <b>No lo usamos.</b>"],
], first="16%")}
<h2>Cómo ajustar el peso con el RIR</h2>
{table(["Si al terminar la serie…", "Entonces"], [
 ["Te quedaban más repeticiones que el RIR del plan", "Subí el peso en la serie siguiente."],
 ["Te quedaba justo el RIR del plan", "Es el peso correcto."],
 ["Te quedaban menos, o perdiste la técnica", "Bajá el peso."],
])}
<p class="small"><b>Cómo anotarlo:</b> peso × repeticiones @ RIR. Por ejemplo, <b>20 kg × 10 @2</b>.</p>
{box(G("<b>En casa:</b> si ya no tenés más peso, bajá en 3 segundos o sumá una pausa abajo: el RIR baja sin sumar kilos.", "<b>Subí lo mínimo:</b> 1 a 2 kg en mancuernas, 2,5 a 5 kg en barra o máquina."), "soft")}
''', chapter="04 · RIR", pid="c4", toc="04 · Esfuerzo con RIR")

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

    for r in "ABC":
        ejs = RUT[r]
        cab = (chap_head("06", f'Rutina {r}: <span class="t">{FOCO[r]}</span>', "Tu resumen para la sesión. La técnica, en las páginas siguientes.") if r == "A"
               else eyebrow(f"RUTINA {r} · {LUGAR}") + f'<h1 class="h1">Rutina {r}: <span class="t">{FOCO[r]}</span></h1>')
        page(f'''
{cab}
{table(["Ejercicio", "Músculos", "Tipo", "Descanso"], [[f"<b>{E[k][1]}</b>", E[k][2], TIPO[t], DESC[t]] for k, t in ejs], first="34%")}
<p class="small"><b>Principales:</b> series, repeticiones y RIR del plan de la semana (página {pref("plan")}). <b>Accesorios:</b> 3 × 12–15 con RIR 2. <b>Zona media:</b> 3 × 30–45 s. Hacelos en el orden de la tabla. Antes, el calentamiento (página {pref("c5")}).</p>
<h2>Claves de esta rutina</h2>
{checks(CLAVES[r])}
''', chapter=f"06 · Rutina {r}", pid=f"r{r}", toc=f"Rutina {r} · {FOCO[r]}")
        grupos = [ejs[i:i + POR_HOJA] for i in range(0, len(ejs), POR_HOJA)]
        for n, gr in enumerate(grupos, 1):
            fin = '<p class="small"><b>Al terminar:</b> anotá las cargas en tu planilla y caminá 5 minutos para bajar pulsaciones.</p>' if n == len(grupos) else ""
            page(f'''
{eyebrow(f"RUTINA {r} · {LUGAR} · {n} DE {len(grupos)}")}
{"".join(card(k) for k, _ in gr)}
{fin}
''', chapter=f"06 · Rutina {r}", pid=f"r{r}{n}")

    page(f'''
{chap_head("07", 'Tu plan de <span class="t">8 semanas</span>', "Planificación ondulada: la carga sube cada semana y cada 4 descargás.")}
{table(["Semana", "Principales", "RIR", "Objetivo"], [[f"<b>{s}</b>", sr, rir, obj] for s, sr, rir, obj in PLAN], first="20%")}
<p class="small"><b>Accesorios:</b> 3 × 12–15 con RIR 2 (en las descargas, 2 × 12 con RIR 4). <b>Zona media:</b> 3 × 30 s las semanas 1 a 4 y 3 × 45 s de la 5 a la 8. Cada semana pesa un poco más que la anterior del mismo bloque.</p>
''', chapter="07 · Plan", pid="plan", toc="07 · Tu plan de 8 semanas")

    page(f'''
{eyebrow("TU PLAN DE 8 SEMANAS")}
<h1 class="h1">Calendario: <span class="t">tildá cada sesión</span></h1>
<p class="lead">Marcá cada sesión que hacés. Ver las tildes juntas es lo que te sostiene en las semanas difíciles.</p>
<div class="tall">{table(["Semana", "Rutina A", "Rutina B", "Rutina C", "Caminatas"], [[f"<b>{s}</b>" + (" · descarga" if s in (4, 8) else ""), "☐", "☐", "☐", "☐ ☐"] for s in range(1, 9)])}</div>
{box("<b>Agendá tus 3 días</b> como si fueran reuniones: día y hora fijos. Lo que está en la agenda se hace.", "soft")}
''', chapter="07 · Plan", pid="calendario", toc="Calendario de 8 semanas")

    ERR = [("Arrancar con demasiado peso", "Las primeras dos semanas son para aprender. El ego es la lesión más común después de los 40."),
           ("Saltear el calentamiento", "Son 8 minutos. Sin ellos, las articulaciones llegan frías a la carga."),
           ("Entrenar siempre al fallo", "Respetá el RIR del plan. Progresás igual y te recuperás mejor."),
           ("No anotar", "Sin planilla no sabés si subiste o no. La memoria engaña."),
           ("Hacer solo cardio para bajar la panza", "El cardio suma, pero la fuerza conserva el músculo mientras bajás grasa."),
           ("Dormir poco", "Menos de 6 horas frena la recuperación y aumenta el hambre."),
           ("Ignorar un dolor articular", "El dolor muscular es normal; el articular punzante, no. Cambiá el ejercicio y consultá."),
           ("Saltearte la descarga", "Las semanas 4 y 8 no son vacaciones: son las que te dejan seguir subiendo.")]
    page(f'''
{chap_head("08", 'Errores frecuentes <span class="t">después de los 40</span>', "Los que más frenan el progreso, y cómo evitarlos.")}
<div class="mitos">{"".join(f"<div><b>{t}</b><p>{p}</p></div>" for t, p in ERR)}</div>
{box("<b>¿Tenés una lesión vieja</b> en hombro, rodilla o espalda? Empezá todos los ejercicios con la opción de principiante y subí de a poco. Si duele, consultá.", "note")}
''', chapter="08 · Errores", pid="c8", toc="08 · Errores frecuentes")

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

    ej_clave = [E[k][1] for r in "ABC" for k, t in RUT[r] if t == "P"]
    page(f'''
{eyebrow("HERRAMIENTA")}
<h1 class="h1">Planilla <span class="t">de cargas</span></h1>
<p class="small">Ejercicios principales. Anotá el peso y las repeticiones de la última serie, por ejemplo <b>20 kg × 10</b>. {G("Si es con peso corporal, anotá las repeticiones.", "")} Los accesorios, en una libreta o en tu tablero.</p>
<div class="mid">{table(["Ejercicio", "S1", "S2", "S3", "S5", "S6", "S7"], [[e] + [""] * 6 for e in ej_clave], first="34%")}</div>
''', chapter="Herramientas", pid="cargas", toc="Herramienta: planilla de cargas")

    page(f'''
{chap_head("11", 'Después de las <span class="t">8 semanas</span>', "Compará la semana 8 con la 1 y elegí cómo seguir.")}
{tips([("Repetí con más carga", "Volvé a la semana 1 con los pesos de tu semana 5. Es un nuevo ciclo más exigente."),
       ("Mantené", "Seguí 3 días por semana rotando A, B y C con RIR 2. Conservás lo ganado."),
       ("Cambiá de modalidad", G("Si tenés acceso a un gimnasio, pasá al ebook de gimnasio: mismo sistema, más carga.", "Si una temporada no podés ir, seguí con el ebook de casa: mismo sistema."))], "t3")}
<h2>Cómo armar el nuevo ciclo</h2>
{table(["Si en la semana 8…", "En el nuevo ciclo"], [
 ["Tu evaluación de fuerza mejoró", "Empezá el bloque 1 con los pesos de tu semana 5."],
 ["Te costó sostener 3 días", "Hacé 2 días por semana con la rotación de 2 días (capítulo 03)."],
 ["Algún ejercicio te molesta", "Usá su opción de principiante o consultá por un plan a medida."],
])}
<h2>Qué cambió para vos</h2>
{checks(["Levanto más peso que en la semana 1.", "Mi cintura bajó o se mantuvo mientras subían las cargas.",
         "Duermo mejor y tengo más energía.", "Las tareas del día me cuestan menos."])}
''', chapter="11 · Después", pid="c11", toc="11 · Después de las 8 semanas")

    hoja_autor()


# =========================================================================================== GUÍA DE MÉTRICAS (gratis en el pack)
def metricas():
    portada('Medí tu<br>progreso', "Peso, medidas, fotos y fuerza: cómo tomarlos bien y cómo leerlos")

    page(f'''
{eyebrow("BIENVENIDO")}
<h1 class="h1">Lo que no se mide, <span class="t">no se mejora</span></h1>
<p class="lead">El espejo engaña y la balanza sola también. Esta guía te enseña a medir <b>cuatro cosas</b>, siempre igual, para saber si el programa está funcionando.</p>
{table(["Qué medís", "Con qué", "Cada cuánto"], [
 ["<b>Peso</b>", "Balanza", "3 veces por semana (promedio semanal)"],
 ["<b>Perímetros</b>", "Cinta métrica", "Semanas 1, 4 y 8"],
 ["<b>Fotos</b>", "Celular", "Semanas 1, 4 y 8"],
 ["<b>Fuerza</b>", "Test de repeticiones con RIR", "Semanas 1 y 8"],
])}
<h2>Cómo usar esta guía</h2>
{checks(["Leela entera antes de tu primera medición: son 15 minutos.", "Cargá cada dato en tu <b>tablero de progreso</b> (capítulo 07): calcula y grafica todo solo.",
         "Si preferís papel, al final tenés una planilla para imprimir."])}
<h2>Qué necesitás</h2>
{checks(["Una balanza (digital, si podés).", "Una cinta métrica flexible.", "El celular para las fotos y el tablero."])}
''', chapter="Bienvenido", pid="bienvenida")

    page("__TOC__", chapter="Índice", pid="indice")
    INDICE_EXTRA.append(f'''<h2>Tu calendario de mediciones</h2>
{table(["Semana", "Peso", "Perímetros", "Fotos", "Fuerza"], [["1", "✓", "✓", "✓", "✓"], ["2 y 3", "✓", "", "", ""], ["4", "✓", "✓", "✓", ""], ["5 a 7", "✓", "", "", ""], ["8", "✓", "✓", "✓", "✓"]])}''')

    page(f'''
{chap_head("01", 'El peso: <span class="t">cómo pesarte</span>', "El peso sube y baja por agua, sal y comida. Por eso se mide siempre igual y se mira el promedio.")}
{checks(["<b>En ayunas,</b> después de ir al baño y antes de tomar agua.", "<b>Misma balanza,</b> sobre piso firme, siempre en el mismo lugar.",
         "<b>Sin ropa</b> o siempre con la misma.", "<b>3 días por semana,</b> por ejemplo lunes, miércoles y viernes."])}
<h2>Usá el promedio, no un día</h2>
{table(["Lunes", "Miércoles", "Viernes", "Promedio"], [["84,6", "85,3", "84,4", "<b>84,8</b>"]])}
<p class="small">Un día podés pesar 1 kg más por una cena salada o poca agua: no es grasa. Compará el promedio de una semana con el de la anterior.</p>
{table(["Error", "Por qué engaña"], [["Pesarte después de comer o entrenar", "Sumás comida y agua, no grasa."], ["Cambiar de balanza", "Cada balanza marca distinto."], ["Pesarte todos los días y reaccionar", "Las subidas de un día son agua."]], first="40%")}
{box("<b>Qué esperar:</b> si buscás bajar grasa, un descenso de entre 0,25 y 0,75 kg por semana en el promedio es un buen ritmo. Si buscás ganar músculo, lo normal es que el peso suba muy despacio.", "soft")}
''', chapter="01 · Peso", pid="c1", toc="01 · El peso")

    page(f'''
{chap_head("02", 'Perímetros <span class="t">con cinta</span>', "Son los que mejor muestran si bajás grasa y ganás músculo, aunque la balanza no se mueva.")}
{checks(["Cinta métrica flexible, de modista.", "De pie, relajado, sin inflar ni meter la panza.", "La cinta apoyada sobre la piel, sin apretar ni hundir.", "Medí 2 veces cada perímetro y anotá el promedio."])}
{table(["Perímetro", "Dónde va la cinta"], [
 ["<b>Cintura</b>", "A la altura del ombligo, al final de una exhalación normal."],
 ["<b>Cadera</b>", "En la parte más saliente de los glúteos, con los pies juntos."],
 ["<b>Pecho</b>", "A la altura de las tetillas, con los brazos relajados al costado."],
 ["<b>Brazo</b>", "En el punto medio entre hombro y codo, brazo relajado."],
 ["<b>Muslo</b>", "A mitad de camino entre la ingle y la rodilla, de pie."],
], first="22%")}
<h2>Errores comunes</h2>
{checks(["Medir un día de un lado y otro día del otro: medí siempre el lado derecho.", "Apretar la cinta para que dé menos.", "Medir el pecho solo: pedile ayuda a alguien para que la cinta quede derecha."])}
''', chapter="02 · Perímetros", pid="c2", toc="02 · Perímetros con cinta")

    page(f'''
{eyebrow("PERÍMETROS")}
<h1 class="h1">Cintura y altura: <span class="t">un dato que importa</span></h1>
<p class="lead">El <b>índice cintura-altura</b> es una forma simple de mirar la grasa abdominal: dividís tu cintura por tu altura, las dos en centímetros.</p>
{table(["Ejemplo", "Cuenta", "Resultado"], [["Cintura 96 cm · altura 176 cm", "96 ÷ 176", "<b>0,55</b>"]])}
{table(["Índice", "Lectura orientativa"], [["Menos de 0,5", "Rango de referencia saludable"], ["0,5 a 0,6", "Conviene bajar la cintura"], ["Más de 0,6", "Prioridad: bajar la cintura y consultar con tu médico"]])}
<h2>Qué te dice cada perímetro</h2>
{table(["Si…", "Probablemente…"], [
 ["Baja la cintura", "Estás bajando grasa abdominal."],
 ["Suben brazo, pecho o muslo y la cintura no", "Estás ganando músculo."],
 ["Sube la cintura", "Estás sumando grasa: revisá la alimentación."],
])}
<p class="small">Es una referencia general, no un diagnóstico.</p>
''', chapter="02 · Perímetros", pid="c2b")

    page(f'''
{chap_head("03", 'Fotos <span class="t">de progreso</span>', "Muestran lo que la balanza no ve. La clave es sacarlas siempre en las mismas condiciones.")}
{table(["Qué cuidar", "Cómo"], [
 ["<b>Luz</b>", "La misma: de día, frente a una ventana o con la misma lámpara."],
 ["<b>Lugar</b>", "La misma pared lisa, sin espejo."],
 ["<b>Cámara</b>", "A la altura de la cintura, a 2 o 3 metros, con temporizador o con ayuda."],
 ["<b>Ropa</b>", "Short o malla, siempre la misma."],
 ["<b>Momento</b>", "En ayunas, el mismo día que te medís."],
])}
<h2>Las tres poses</h2>
{tips([("De frente", "Brazos relajados al costado, pies al ancho de la cadera."),
       ("De perfil", "Mirando a un costado, brazos relajados, sin meter la panza."),
       ("De espalda", "Igual que de frente, de espaldas a la cámara.")], "t3")}
{box("<b>Compará de a dos:</b> la de la semana 1 al lado de la de la semana 8, misma pose. No te mires todos los días: el cambio se ve cada 4 semanas.", "soft")}
''', chapter="03 · Fotos", pid="c3", toc="03 · Fotos de progreso")

    page(f'''
{chap_head("04", 'Evaluación <span class="t">de fuerza</span>', "No hace falta levantar el máximo: con un test de repeticiones y el RIR estimás tu fuerza sin riesgo.")}
<h2>Qué es el RIR</h2>
<p>RIR son las <b>repeticiones en reserva</b>: las que te quedan al terminar la serie. Es la forma de medir el esfuerzo sin llegar al fallo.</p>
{table(["RIR", "Cómo se siente"], [["4", "Podrías hacer 4 más. Esfuerzo moderado."], ["2", "Te quedan 2. Exigente, técnica perfecta."], ["1", "Te queda 1 sola."], ["0", "Fallo. No lo usamos."]], first="20%")}
<h2>Cómo aprender a usarlo</h2>
{checks(["Al principio vas a calcular de menos: casi todos creen que les quedan menos repeticiones de las que les quedan.",
         "Probá en una serie: cuando creas que te quedan 2, hacé 1 más y fijate si acertaste.",
         "En 2 o 3 semanas vas a calcularlo bien. Anotá siempre el RIR junto al peso."])}
''', chapter="04 · Fuerza", pid="c4", toc="04 · Evaluación de fuerza")

    page(f'''
{eyebrow("EVALUACIÓN DE FUERZA")}
<h1 class="h1">El test <span class="t">paso a paso</span></h1>
<ol class="steps-ol">
<li>Hacé el calentamiento completo y 2 series de aproximación (50 % y 75 % del peso que vas a usar).</li>
<li>Elegí un peso con el que creas poder hacer <b>entre 6 y 10 repeticiones</b>.</li>
<li>Hacé una sola serie hasta quedarte con <b>RIR 1</b>: frená cuando te quede una sola en reserva.</li>
<li>Anotá el peso, las repeticiones que hiciste y el RIR.</li>
<li>Descansá 3 minutos y pasá al ejercicio siguiente.</li>
</ol>
{table(["Testeá", "En casa", "En el gimnasio"], [["Piernas", "Sentadilla en copa", "Sentadilla con barra"], ["Empuje", "Flexiones (repeticiones)", "Press plano con barra"], ["Tirón", "Remo con mancuerna", "Remo en polea baja"]], first="18%")}
<h2>Frená el test si…</h2>
{checks(["Perdés la técnica, aunque te queden repeticiones.", "Aparece un dolor articular (no el cansancio muscular).", "Te mareás o te falta el aire."])}
{box("<b>Cuándo:</b> en la semana 1, con prudencia, y en la semana 8 (descarga). Nunca hagas el test si te duele algo o dormiste muy mal.", "note")}
''', chapter="04 · Fuerza", pid="c4b")

    page(f'''
{eyebrow("EVALUACIÓN DE FUERZA")}
<h1 class="h1">Tu fuerza <span class="t">estimada</span></h1>
<p class="lead">Con el test calculás tu máximo estimado para una repetición (1RM), sin levantarlo nunca.</p>
<div class="box"><b>1RM estimado = peso × (1 + (repeticiones + RIR) ÷ 30)</b></div>
{table(["Ejemplo", "Cuenta", "1RM estimado"], [["60 kg × 8 repeticiones con RIR 1", "60 × (1 + 9 ÷ 30)", "<b>78 kg</b>"]])}
<p>No te preocupes por la cuenta: <b>tu tablero la hace solo</b>. Lo que importa es comparar el número de la semana 8 con el de la semana 1.</p>
<h2>Tu registro</h2>
<div class="tall">{table(["Ejercicio", "Semana 1 (peso × reps · RIR)", "Semana 8 (peso × reps · RIR)"], [["Piernas", "", ""], ["Empuje", "", ""], ["Tirón", "", ""]], first="22%")}</div>
''', chapter="04 · Fuerza", pid="c4c")

    page(f'''
{chap_head("05", 'El RIR para <span class="t">progresar</span>', "El RIR no solo mide: te dice cuándo subir el peso. Así funciona tu plan de 8 semanas.")}
{table(["Si en la serie te quedaron…", "Entonces"], [
 ["Más repeticiones que el RIR del plan", "Subí el peso en la serie siguiente."],
 ["Justo el RIR del plan", "Es el peso correcto: mantenelo."],
 ["Menos, o perdiste la técnica", "Bajá el peso."],
])}
<h2>La planificación ondulada</h2>
{table(["Semana", "1", "2", "3", "4", "5", "6", "7", "8"], [["Series × reps", "3×12", "3×10", "4×8", "2×10", "4×10", "4×8", "4×6", "2×8"], ["RIR", "3", "2–3", "2", "4", "2", "2", "1–2", "4"]], first="20%")}
<p class="small">La carga sube cada semana y en la 4 y la 8 descargás. La semana 8 es la de tu evaluación final.</p>
<h2>Un ejemplo real</h2>
{table(["Semana", "Sentadilla", "RIR", "Decisión"], [["1", "16 kg × 12", "4", "Sobraron: subir"], ["2", "20 kg × 10", "3", "Correcto"], ["3", "22 kg × 8", "2", "Correcto"], ["4", "16 kg × 10", "4", "Descarga"]])}
''', chapter="05 · RIR", pid="c5", toc="05 · El RIR para progresar")

    page(f'''
{chap_head("06", 'Cómo leer <span class="t">tus datos</span>', "Lo que importa es la combinación, no un número suelto.")}
{table(["Si ves…", "Significa…", "Qué hacer"], [
 ["Peso baja, cintura baja, fuerza sube", "Bajás grasa y conservás músculo.", "Seguí así."],
 ["Peso igual, cintura baja, fuerza sube", "Recomposición: menos grasa y más músculo.", "Seguí así: es el mejor escenario."],
 ["Peso sube, cintura igual, fuerza sube", "Ganás músculo.", "Bien si ese es tu objetivo."],
 ["Peso y cintura suben", "Sumás grasa.", "Revisá la alimentación."],
 ["Fuerza estancada 2 semanas", "Falta descanso, comida o carga.", "Revisá sueño, proteína y el RIR."],
], first="32%")}
<h2>Errores al leer tus datos</h2>
{checks(["Desanimarte porque la balanza no baja, cuando la cintura sí.", "Comparar una medición hecha en otras condiciones.", "Sacar conclusiones con una sola semana de datos."])}
{box("<b>Mirá la tendencia de 2 a 4 semanas,</b> no una medición. Y medí siempre en las mismas condiciones: si cambian las condiciones, cambia el número.", "soft")}
''', chapter="06 · Leer los datos", pid="c6", toc="06 · Cómo leer tus datos")

    page(f'''
{chap_head("07", 'Tu tablero <span class="t">de progreso</span>', "Cargás tus datos desde el celular y ves todo graficado: peso, cintura, fuerza y sesiones.")}
{boton_tablero()}
{checks(["<b>Cargá cada semana:</b> peso promedio, perímetros (semanas 1, 4 y 8), cargas y sesiones hechas.",
         "<b>El tablero calcula solo:</b> los cambios desde la semana 1, tu 1RM estimado y el índice cintura-altura.",
         "<b>Tus datos son tuyos:</b> se guardan en tu celular o computadora, no en internet.",
         "<b>Guardá una copia</b> con el botón del tablero cada tanto, por si cambiás de celular."])}
<h2>Qué vas a ver</h2>
{tips([("Indicadores", "Tu cambio de peso, cintura y fuerza desde la semana 1."), ("Gráficos", "La evolución semana a semana."), ("Sesiones", "Cuántas de las 24 hiciste.")], "t3")}
{box("<b>Usalo siempre desde el mismo celular o computadora</b> y el mismo navegador, así tus datos te esperan cada vez que entrás.", "note")}
''', chapter="07 · Tablero", pid="c7", toc="07 · Tu tablero de progreso")

    page(f'''
{eyebrow("HERRAMIENTA")}
<h1 class="h1">Planilla <span class="t">para imprimir</span></h1>
<div class="tall2">{table(["Medida", "Semana 1", "Semana 4", "Semana 8"], [["Peso promedio (kg)", "", "", ""], ["Cintura (cm)", "", "", ""], ["Cadera (cm)", "", "", ""], ["Pecho (cm)", "", "", ""],
 ["Brazo (cm)", "", "", ""], ["Muslo (cm)", "", "", ""], ["Índice cintura-altura", "", "", ""], ["Fotos", "☐", "☐", "☐"], ["Sesiones hechas", "", "", ""], ["Cómo me siento (1 a 10)", "", "", ""]], first="40%")}</div>
''', chapter="Herramientas", pid="planilla", toc="Herramienta: planilla para imprimir")

    hoja_autor()


ABD_RUT = {
    1: ("Antiextensión", ["plancha_frontal", "flexiones", "bicho_alt", "mountain"]),
    2: ("Antirrotación y lateral", ["plancha_lateral", "press_pallof", "bird_dog", "renegade_row"]),
    3: ("Plancha alta", ["plancha_alta", "flex_toque", "plancha_alta_din", "caminata_manos"]),
    4: ("Fuerza y control", ["flex_declinadas", "bicho_muerto_botella", "plancha_lateral", "mountain"]),
}
ABD_MAS = {"plancha_frontal": "Plancha alta con alcance", "flexiones": "Flexiones declinadas", "bicho_alt": "Con una mancuerna en las manos", "mountain": "Más rápido, sin perder la línea",
           "plancha_lateral": "Elevá la pierna de arriba", "press_pallof": "Más lejos del anclaje", "bird_dog": "Pausa de 5 segundos", "renegade_row": "Más peso",
           "plancha_alta": "Pies sobre un banco", "flex_toque": "Pies juntos", "plancha_alta_din": "Pies juntos", "caminata_manos": "Más lejos con las manos",
           "flex_declinadas": "Banco más alto", "bicho_muerto_botella": "Más peso"}
ABD_CLAVES = {1: ["En los cuatro ejercicios, la zona lumbar no se arquea.", "En el bicho muerto, exhalá mientras estirás.", "El mountain climber va controlado: la cadera no rebota."],
              2: ["Tu trabajo es que el tronco no gire ni se incline.", "En el Pallof, los brazos se estiran pero el pecho queda de frente.", "En el remo en plancha, abrí los pies para estar más estable."],
              3: ["Toda la rutina es en plancha alta: hombros arriba de las manos.", "Al tocar el hombro o estirar el brazo, la cadera no se mueve.", "En la caminata de manos, llegá solo hasta donde mantengas la línea."],
              4: ["Las flexiones declinadas son las más exigentes: técnica antes que repeticiones.", "En el bicho muerto con peso, la zona lumbar sigue pegada al piso.", "Repetís dos ejercicios: buscá hacerlos mejor que en la rutina 1 y 2."]}
ABD_DOSIS = {"plancha_frontal": "tiempo", "plancha_lateral": "tiempo por lado", "plancha_alta": "tiempo", "flexiones": "reps", "flex_toque": "reps",
             "flex_declinadas": "reps", "bicho_alt": "reps por lado", "bird_dog": "reps por lado", "bicho_muerto_botella": "reps por lado",
             "press_pallof": "reps por lado", "renegade_row": "reps por lado", "plancha_alta_din": "reps por lado", "mountain": "reps por lado", "caminata_manos": "reps"}


def abdomen():
    portada('Zona media<br><span>fuerte</span>', "4 rutinas para sumar a tu programa · mitos, verdades y cómo hacerlo bien")

    page(f'''
{eyebrow("BIENVENIDO")}
<h1 class="h1">Un abdomen fuerte <span class="t">se entrena distinto</span></h1>
<p class="lead">Este es el complemento de MÉTODO 40 para la <b>zona media</b>: menos abdominales clásicos y más ejercicios que la entrenan para lo que hace en la vida real, que es <b>sostener la columna mientras te movés</b>.</p>
{table(["Qué es", "Cómo es"], [
 ["<b>Rutinas</b>", "4 distintas, de 4 ejercicios cada una"],
 ["<b>Cuándo</b>", "2 veces por semana, 15 minutos al final de una sesión de MÉTODO 40"],
 ["<b>Duración</b>", "8 semanas, con la misma planificación ondulada del programa"],
 ["<b>Material</b>", "Colchoneta, banco o cajón, banda elástica y una mancuerna"],
])}
<h2>Qué vas a aprender</h2>
{checks(["Qué es de verdad la zona media y para qué sirve.", "Los mitos más comunes, y por qué el giro ruso o el toes to bar no son lo que parecen.",
         "Cómo respirar en las flexiones y en las planchas.", "Cómo progresar sin hacer planchas eternas."])}
{box("<b>No es solo estética:</b> una zona media fuerte te deja levantar más en el programa, cuidar la espalda y moverte mejor en el día a día. El abdomen marcado depende además de la alimentación.", "soft")}
''', chapter="Bienvenido", pid="bienvenida")

    page("__TOC__", chapter="Índice", pid="indice")
    INDICE_EXTRA.append(f'''<h2>Tu semana</h2>
{table(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"], [["MÉTODO 40 + zona media", "–", "MÉTODO 40", "–", "MÉTODO 40 + zona media", "–", "–"]])}''')

    page(f'''
{chap_head("01", 'Qué es la <span class="t">zona media</span>', "No es solo el “six pack”: es un cilindro de músculos que rodea y sostiene tu columna.")}
{table(["Músculo", "Qué hace"], [
 ["<b>Recto abdominal</b>", "El de adelante. Frena que la columna se arquee hacia atrás."],
 ["<b>Oblicuos</b>", "A los costados. Frenan la rotación y la inclinación del tronco."],
 ["<b>Transverso</b>", "El más profundo. Funciona como una faja natural."],
 ["<b>Diafragma y piso pélvico</b>", "Cierran el cilindro por arriba y por abajo: por eso la respiración importa."],
], first="32%")}
<h2>Su trabajo real: frenar, no mover</h2>
{tips([("Antiextensión", "Que la zona lumbar no se arquee. Ejemplo: plancha."), ("Antirrotación", "Que el tronco no gire. Ejemplo: press Pallof."),
       ("Antiflexión lateral", "Que no te inclines de costado. Ejemplo: plancha lateral."), ("Transmitir fuerza", "Pasar la fuerza de las piernas a los brazos sin perderla.")])}
''', chapter="01 · Zona media", pid="c1", toc="01 · Qué es la zona media")

    MITOS = [("“Hacer abdominales baja la panza.”", "No se puede quemar grasa de un lugar elegido. La panza baja con alimentación, fuerza en todo el cuerpo y movimiento."),
             ("“Hay que hacer cientos de repeticiones.”", "La zona media se entrena como cualquier músculo: con buena técnica, carga y progresión."),
             ("“Si no arde, no sirve.”", "El ardor no mide la calidad del trabajo. Un ejercicio bien hecho puede no arder nada."),
             ("“Cuanto más larga la plancha, mejor.”", "Pasados los 45 a 60 segundos aporta poco. Es mejor una variante más difícil que un minuto más."),
             ("“El giro ruso marca los oblicuos.”", "Los oblicuos se entrenan mejor frenando la rotación que girando con carga (capítulo 03)."),
             ("“Colgarse y subir las piernas es el mejor abdominal.”", "Trabaja sobre todo el psoas, el flexor de la cadera (capítulo 03)."),
             ("“Hay que entrenarlos todos los días.”", "Necesitan recuperarse como cualquier músculo: 2 veces por semana alcanzan."),
             ("“Con abdominales fuertes no duele la espalda.”", "Ayuda, pero el dolor lumbar tiene muchas causas. Si te duele, consultá.")]
    page(f'''
{chap_head("02", 'Mitos <span class="t">y verdades</span>', "Lo que se repite en el gimnasio y lo que en realidad pasa.")}
<div class="mitos">{"".join(f"<div><b>{t}</b><p>{p}</p></div>" for t, p in MITOS)}</div>
{box("<b>La verdad que sí funciona:</b> fuerza en todo el cuerpo, una zona media que sepa frenar el movimiento y una alimentación ordenada.", "soft")}
''', chapter="02 · Mitos", pid="c2", toc="02 · Mitos y verdades")

    page(f'''
{chap_head("03", 'Cuidados: <span class="t">punto fijo y punto móvil</span>', "La clave para entender qué músculo trabaja de verdad en cada ejercicio.")}
<p>Un músculo une dos huesos. Cuando se contrae, uno queda quieto (<b>punto fijo</b>) y el otro se mueve hacia él (<b>punto móvil</b>). Según cuál se mueva, cambia qué músculo hace el trabajo.</p>
{table(["Ejercicio", "Qué se mueve", "Quién trabaja más"], [
 ["<b>Toes to bar o elevación de piernas colgado</b>", "Las piernas hacia el tronco (flexión de cadera)", "El <b>psoas</b>, flexor de la cadera. El abdomen solo estabiliza."],
 ["<b>Crunch bien hecho</b>", "El tronco se enrolla hacia la pelvis", "El recto abdominal."],
 ["<b>Plancha, bicho muerto, Pallof</b>", "Nada: tu trabajo es que no se mueva", "Toda la zona media, que frena el movimiento."],
], first="32%")}
<p class="small"><b>Regla práctica:</b> si sentís la zona lumbar en un ejercicio de abdominales, la pelvis se está despegando: frená o hacé la variante más fácil.</p>
{box("<b>Por qué importa:</b> si el psoas tira fuerte y el abdomen no llega a sostener la pelvis, la zona lumbar se arquea y se carga. Por eso el toes to bar no es un ejercicio para entrenar abdominales, y en este programa no está.", "note")}
''', chapter="03 · Cuidados", pid="c3", toc="03 · Cuidados: punto fijo y móvil")

    page(f'''
{eyebrow("CUIDADOS")}
<h1 class="h1">El giro ruso y <span class="t">el cizallamiento</span></h1>
{box("<b>Ojo:</b> hablamos del <b>giro ruso</b> (russian twist), sentado con el tronco inclinado girando de lado a lado. No tiene nada que ver con el swing con pesa rusa del programa.", "soft")}
<p>El <b>cizallamiento</b> es una fuerza que tiende a hacer deslizar una vértebra sobre la otra. La columna lumbar tolera bien cargas en línea, pero no tanto la combinación de <b>flexión sostenida + rotación repetida</b>, y menos con peso y velocidad.</p>
<p>El giro ruso junta todo eso: tronco flexionado, giros rápidos, muchas repeticiones y, muchas veces, un disco en las manos. Puede sumar carga innecesaria sobre los discos lumbares, sobre todo después de los 40.</p>
{table(["En vez de…", "Hacé…", "Por qué"], [
 ["Giro ruso", "Press Pallof", "El oblicuo trabaja frenando la rotación, con la columna neutra."],
 ["Toes to bar", "Bicho muerto", "El abdomen sostiene la pelvis mientras se mueven las piernas."],
 ["Abdominales con tirón de cuello", "Plancha y sus variantes", "Toda la zona media trabaja sin forzar el cuello."],
], first="26%")}
{box("<b>Si te duele la espalda baja,</b> evitá cualquier ejercicio que combine flexión y rotación, y consultá con un profesional antes de seguir.", "note")}
''', chapter="03 · Cuidados", pid="c3b")

    page(f'''
{chap_head("04", 'Cómo <span class="t">respirar</span>', "La respiración es parte del ejercicio: arma la faja natural que protege tu columna.")}
<h2>En las flexiones de brazos</h2>
<ol class="steps-ol">
<li><b>Arriba:</b> tomá aire por la nariz y apretá el abdomen como si te fueran a dar un golpe suave.</li>
<li><b>Bajando:</b> mantené esa tensión, sin soltar el aire de golpe.</li>
<li><b>Subiendo:</b> soltá el aire por la boca mientras empujás el piso.</li>
</ol>
<h2>En las planchas</h2>
{checks(["Respirá corto y continuo, sin aflojar el abdomen.", "No aguantes el aire: si te ponés colorado, estás trabado.", "Si al exhalar se te cae la cadera, la plancha es demasiado larga o difícil."])}
<h2>Respiración 360°</h2>
<p>Acostado boca arriba, manos en las costillas: inhalá llevando el aire a los costados y a la espalda, no solo a la panza. Exhalá largo sintiendo cómo se cierra la cintura. Hacé 5 antes de cada rutina.</p>
{box("<b>Si tenés presión alta,</b> nunca hagas fuerza aguantando el aire. Exhalá siempre en el esfuerzo.", "note")}
''', chapter="04 · Respirar", pid="c4", toc="04 · Cómo respirar")

    page(f'''
{chap_head("05", 'Cómo se suma <span class="t">a tu programa</span>', "Dos veces por semana, 15 minutos al final de una sesión de MÉTODO 40.")}
{table(["Semana", "Lunes", "Viernes"], [["Impares (1, 3, 5, 7)", "Rutina 1", "Rutina 2"], ["Pares (2, 4, 6, 8)", "Rutina 3", "Rutina 4"]], first="34%")}
<p class="small">Si preferís, hacé las dos rutinas de la semana juntas en un día aparte (30 minutos). Lo importante es no hacerlas el día antes de una sesión con peso muerto o sentadilla pesada.</p>
<h2>Cómo es cada rutina</h2>
{table(["Parte", "Cómo"], [["Respiración 360°", "5 respiraciones"], ["Circuito", "4 ejercicios seguidos, sin descanso entre ejercicios"],
 ["Vueltas", "Según el plan (página " + pref("plan") + ")"], ["Descanso", "Entre vueltas, según el plan"]], first="34%")}
{table(["Rutina", "Foco", "Página"], [[f"<b>{n}</b>", foco, pref(f"ab{n}")] for n, (foco, _) in ABD_RUT.items()])}
''', chapter="05 · Cómo se suma", pid="c5", toc="05 · Cómo se suma a tu programa")

    for n, (foco, ejs) in ABD_RUT.items():
        page(f'''
{eyebrow(f"RUTINA {n} · ZONA MEDIA")}
<h1 class="h1">Rutina {n}: <span class="t">{foco.lower()}</span></h1>
{params([("Duración", "15 min"), ("Formato", "Circuito"), ("Ejercicios", "4"), ("Vueltas", "Ver plan")])}
{table(["Ejercicio", "Dosis", "Más fácil", "Más difícil"], [[f"<b>{E[k][1]}</b>", ABD_DOSIS[k].capitalize() + " del plan", E[k][5].capitalize(), ABD_MAS[k]] for k in ejs], first="28%")}
<p class="small">Hacé los 4 seguidos, sin descanso entre ejercicios, y descansá al terminar cada vuelta. La técnica de cada uno, en la hoja siguiente.</p>
<h2>Claves de esta rutina</h2>
{checks(ABD_CLAVES[n])}
''', chapter=f"Rutina {n}", pid=f"ab{n}", toc=f"Rutina {n} · {foco.lower()}")
        page(f'''
{eyebrow(f"RUTINA {n} · ZONA MEDIA · 2 DE 2")}
{"".join(card(k) for k in ejs)}
<p class="small"><b>Al terminar:</b> 5 respiraciones 360° y anotá tiempos y repeticiones en tu registro.</p>
''', chapter=f"Rutina {n}", pid=f"ab{n}b")

    page(f'''
{chap_head("06", 'Tu plan de <span class="t">8 semanas</span>', "La misma lógica ondulada de MÉTODO 40: sube cada semana y descarga en la 4 y la 8.")}
{table(["Semana", "Vueltas", "Planchas", "Repeticiones", "Descanso"], [
 ["<b>1</b>", "3", "20–30 s", "8", "60 s"], ["<b>2</b>", "3", "30 s", "10", "60 s"], ["<b>3</b>", "4", "30–40 s", "10", "60 s"],
 ["<b>4 · descarga</b>", "2", "20 s", "8", "60 s"], ["<b>5</b>", "3", "40 s", "12", "45 s"], ["<b>6</b>", "4", "40 s", "12", "45 s"],
 ["<b>7</b>", "4", "45 s", "15", "45 s"], ["<b>8 · descarga</b>", "2", "30 s", "10", "60 s"]], first="22%")}
<p class="small">“Repeticiones” vale por lado en los ejercicios alternados. Las flexiones, con RIR 2: si llegás al número del plan con más reserva, pasá a la variante más difícil.</p>
{box("<b>Progresá con variantes, no con tiempo:</b> si una plancha de 45 segundos te sale fácil, pasá a la plancha alta con alcance o subí los pies.", "soft")}
''', chapter="06 · Plan", pid="plan", toc="06 · Tu plan de 8 semanas")

    ERR = [("Cola arriba en la plancha", "La cadera va en línea con hombros y talones."), ("Zona lumbar hundida", "Apretá glúteos y llevá las costillas hacia abajo."),
           ("Mountain climber a toda velocidad", "Primero controlado: la cadera no rebota."), ("Aguantar el aire", "Respirá corto y continuo."),
           ("Flexiones con la cadera caída", "Si no podés sostener la línea, pasá a flexiones inclinadas."), ("Estirar el tiempo en vez de progresar", "Más de 45 a 60 segundos de plancha aporta poco.")]
    page(f'''
{chap_head("07", 'Errores <span class="t">frecuentes</span>', "Los que más se ven, y cómo corregirlos.")}
<div class="mitos">{"".join(f"<div><b>{t}</b><p>{p}</p></div>" for t, p in ERR)}</div>
<h2>Tu registro</h2>
<div class="tall2">{table(["", "Semana 1", "Semana 4", "Semana 8"], [["Plancha frontal (segundos)", "", "", ""], ["Plancha lateral der. / izq. (s)", "", "", ""], ["Flexiones en una serie (RIR 1)", "", "", ""]], first="40%")}</div>
''', chapter="07 · Errores", pid="c7", toc="07 · Errores y registro")

    hoja_autor()


programa() if not (MET or ABD) else metricas() if MET else abdomen()


def render():
    num = {p["id"]: i + 1 for i, p in enumerate(PAGES)}
    toc_html = '<div class="tocl tc">' + "".join(
        f'<a class="tocr" href="#{pid}"><span class="tt">{esc(t)}</span><span class="dots"></span><span class="pg">{num[pid]}</span></a>'
        for t, pid in TOC) + "</div>"
    inicio = (f'<div class="box soft"><b>Para empezar:</b> leé los capítulos 01 a 04 (páginas {pref("c1")} a {pref("c4")}), '
              f'mirá la rutina A (página {pref("rA")}) y anotá tus cargas en la planilla (página {pref("cargas")}).</div>') if not MET else (
              f'<div class="box soft"><b>Para empezar:</b> leé la guía entera, hacé tu primera medición y cargala en tu tablero (página {pref("c7")}).</div>') if MET else (
              f'<div class="box soft"><b>Para empezar:</b> leé los capítulos 01 a 04 (páginas {pref("c1")} a {pref("c4")}) y mirá cómo se suma a tu programa (página {pref("c5")}).</div>')
    out = []
    for p in PAGES:
        body = p["body"]
        if body == "__TOC__":
            body = (f'{eyebrow("CONTENIDO")}<div class="idxhead"><h1 class="h1">Índice</h1>'
                    f'<p class="idxtip">{ICON_HAND} Tocá donde quieras ir. Para volver al índice, abajo de cada página tenés el botón.</p></div>{toc_html}{inicio}{"".join(INDICE_EXTRA)}')
        hdr = ""
        if p["header"]:
            hdr = (f'<div class="hdr"><span>MÉTODO <b>40</b> · {"MÉTRICAS" if MET else "ZONA MEDIA" if ABD else G("CASA", "GIMNASIO")}</span><span>{esc(p["chapter"])}</span></div>'
                   f'<div class="ftr"><a class="toidx" href="#indice">{ICON_HAND} Volvé al índice</a><span class="pgnum"></span></div>')
        out.append(f'<section class="page {p["cls"]}" id="{p["id"]}">{hdr}<div class="body">{body}</div></section>')
    css = ds_css(HERE) + "\n" + open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
    titulo = {"casa": "En casa", "gym": "En el gimnasio", "metricas": "Guía de métricas", "abdomen": "Zona media fuerte"}[ED]
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>MÉTODO 40 · {titulo}</title>'
            f'<style>{css}</style></head><body class="grande m40 {"m40g" if GYM or ABD else "m40c" if ED == "casa" else "m40m"}">' + "".join(out) + '<script src="paginate.js"></script></body></html>')


if __name__ == "__main__":
    out = f"hombres_{ED}.html"
    with open(os.path.join(HERE, out), "w", encoding="utf-8") as f:
        f.write(render())
    print(out, "·", len(PAGES), "páginas:", " ".join(f"{i + 1}:{p['id']}" for i, p in enumerate(PAGES)))
