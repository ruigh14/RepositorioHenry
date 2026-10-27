"""Textos e imágenes de los creativos de cada producto.

Para hacer creativos nuevos: copiá un bloque, cambiá los textos y corré generar.py.
No hace falta tocar el diseño (plantillas.py) ni el CSS.

Imágenes: "landing:archivo" = fuentes/landing/img/archivo · "ebook:archivo" = fuentes/ebook/img/archivo.
En títulos, <em>…</em> pinta la palabra en turquesa.
Reglas (ver README): voseo, frases cortas, una idea por pieza, nada de promesas médicas,
resultados siempre con el descargo, precio solo si se completa "precio".
"""

COMUN = dict(
    logo="ebook:logo_renova.png",
    nacho="landing:nacho.jpg",
    cta_organico="Encontralo en el link de la bio",
    cta_anuncio="Comprar ahora",
    testimonios=[
        dict(nombre="Mari", resultado="Bajó 8 kg de grasa y 10 cm de cintura.",
             antes="landing:mari_a.jpg", despues="landing:mari_d.jpg", pos_antes="52% 50%", pos_despues="58% 50%"),
        dict(nombre="Moni", resultado="Bajó 6 kg y logró el hábito de entrenar.",
             antes="landing:moni_d.jpg", despues="landing:moni_a.jpg", pos_antes="43% 50%", pos_despues="52% 50%"),
    ],
    romi=dict(nombre="Romi", resultado="Ganó masa muscular y volvió a correr sin dolores.", foto="landing:ba_romi.jpg"),
    fases=[("Semanas 1 y 2", "Base", "Aprendés la técnica, sin sobrecargas."),
           ("Semanas 3 a 6", "Construcción", "Sube el estímulo. La semana 6 es de descarga."),
           ("Semanas 7 y 8", "Consolidación", "Fijás el hábito y medís tu progreso.")],
    por_que_fuerza=("Desde los 30 perdemos <em>músculo</em> cada década",
                    "Y en la menopausia ese proceso se acelera. El entrenamiento de fuerza es la herramienta más efectiva para frenarlo."),
    bonus=["Recetario: 23 recetas", "2 talleres del equipo", "50% off en tu plan a medida"],
    precio=None,            # por ejemplo "$15.000"; si queda en None, los creativos no muestran precio
    precio_antes=None,      # por ejemplo "$30.000"
)

PRODUCTOS = {
    "entrena-desde-casa": dict(
        COMUN,
        nombre="Entrená desde casa",
        tapa="landing:pag_1.jpg",
        paginas=["landing:pag_16.jpg", "landing:pag_9.jpg", "landing:pag_31.jpg"],
        pill="Para mujeres de 40+ con poco tiempo",
        gancho="Tu cuerpo cambió después de los 40. <em>Tu plan también.</em>",
        sub="Plan de fuerza de 8 semanas para hacer en casa, en 20 a 40 minutos.",
        incluye=["Plan de 8 semanas, día por día", "3 rutinas con video de cada ejercicio",
                 "Sesión express de 15 minutos", "Zona media, elongación y pausa activa"],
        beneficios=[("En tu casa", "Con una colchoneta, una silla y un peso liviano."),
                    ("20 a 40 minutos", "2 o 3 veces por semana. Y una versión de 15 para los días difíciles."),
                    ("Video de cada ejercicio", "Con una variante más fácil para empezar sin miedo.")],
        ejercicios=["landing:ej_r1_3.jpg", "landing:ej_r2_4.jpg", "landing:ej_r3_7.jpg",
                    "landing:ej_r1_6.jpg", "landing:ej_core_bicho.jpg", "landing:ej_r1_8.jpg"],
        carrusel_gancho="Después de los 40 tu cuerpo no responde como antes. <em>No es falta de voluntad.</em>",
        carrusel_problema=("Empezaste mil veces", ["Rutinas sueltas de redes", "Poco tiempo entre trabajo y casa",
                                                   "Nadie que te diga qué hacer", "Miedo a lastimarte"]),
        carrusel_solucion="Un plan de 8 semanas para entrenar <em>en tu casa</em>",
    ),
    "entrena-en-el-gimnasio": dict(
        COMUN,
        nombre="Entrená en el gimnasio",
        tapa="landing:gpag_1.jpg",
        paginas=["landing:gpag_17.jpg", "landing:gpag_9.jpg", "landing:gpag_31.jpg"],
        pill="Nivel inicial · mujeres de 40+",
        gancho="¿Vas al gimnasio y no sabés qué hacer? <em>Seguí un plan.</em>",
        sub="8 semanas de fuerza para empezar desde cero, con máquinas y video de cada ejercicio.",
        incluye=["Plan de 8 semanas, día por día", "3 rutinas con máquinas, mancuernas y poleas",
                 "Video de cada ejercicio", "Zona media, elongación y registro de cargas"],
        beneficios=[("Desde cero", "Aunque nunca hayas ido a un gimnasio."),
                    ("Paso a paso", "Máquinas, mancuernas y poleas, con video y variante más fácil."),
                    ("45 a 60 minutos", "2 o 3 veces por semana, con la entrada en calor incluida.")],
        ejercicios=["landing:gym_prensa.jpg", "landing:gym_jalon.jpg", "landing:gym_hipthrust.jpg",
                    "landing:gym_presspecho.jpg", "landing:gym_remopolea.jpg", "landing:gym_presshombro.jpg"],
        carrusel_gancho="¿Te anotaste en el gimnasio y no sabés por dónde empezar? <em>Te pasa a muchas.</em>",
        carrusel_problema=("No es falta de ganas", ["Máquinas que no sabés usar", "Rutinas pensadas para otros",
                                                    "Miedo a lastimarte", "Ir sin un plan y dejar a las dos semanas"]),
        carrusel_solucion="Un plan de 8 semanas para entrenar <em>en el gimnasio</em>",
    ),
}
