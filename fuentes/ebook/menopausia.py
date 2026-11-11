"""Ebook upsell "Nutrición en la menopausia" (Nutrición Femenina 35+): profundiza en la etapa hormonal.
No repite "Alimentación Inteligente" (organización y recetas): explica qué cambia y cómo acompañarlo desde la alimentación.
Material educativo: sin dosis, sin tratamientos, con indicación de consultar. Revisión: Lic. María Eugenia Aldrey.

Uso:  cd fuentes/ebook && python3 menopausia.py && node export.js menopausia
      → nutricion-menopausia/Ebook_Nutricion_Menopausia_RENOVA.pdf
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "design-system"))
from design_system import css as ds_css, esc, ICON_ARROW, ICON_HAND, eyebrow, chap_head, ul, checks, box

NUTRI, NUTRI_TIT = "María Eugenia Aldrey", "Lic. en Nutrición · M.N. 11773"
LINK_PLAN = "https://wa.link/1asjt1"
PAGES, TOC = [], []


def page(body, chapter="", pid=None, cls="", toc=None, header=True):
    pid = pid or f"p{len(PAGES) + 1}"
    PAGES.append(dict(id=pid, chapter=chapter, body=body, cls=cls, header=header))
    if toc:
        TOC.append((toc, pid))


def table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="grid-t ntab"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def evid(nivel, texto):
    """Etiqueta de evidencia: sólida / limitada / no demostrada."""
    cls = {"Sólida": "ev-ok", "Limitada": "ev-mid", "No demostrada": "ev-no"}[nivel]
    return f'<p class="ev {cls}"><b>Evidencia {nivel.lower()}:</b> {texto}</p>'


# ================================================================== PORTADA
page('''
<div class="cv3 meno">
  <div class="c3-in">
    <img class="c3-logo" src="img/logo_renova.png" alt="RENOVA">
    <span class="c3-pill">MÉTODO RENOVA · MUJERES 35+</span>
    <h1 class="c3-title">NUTRICIÓN EN<br>LA MENOPAUSIA</h1>
    <p class="c3-claim">ENTENDÉ TU CUERPO, <b><span>CUIDALO.</span></b></p>
    <p class="c3-sub">Qué cambia en la <b>perimenopausia</b> y la <em>menopausia</em>,<br><span>y cómo acompañarlo con <mark>alimentación</mark> y <mark>hábitos</mark>.</span></p>
  </div>
  <div class="c3-team"><img src="img/equipo_tapa.png" alt="Equipo RENOVA"></div>
</div>
''', pid="portada", cls="p-cover", header=False)

page(f'''
{eyebrow("BIENVENIDA")}
<h1 class="h1">Una etapa, <span class="t">no un problema</span></h1>
<p class="lead">Para mujeres en <b>perimenopausia, menopausia o posmenopausia</b>. La menopausia no es una enfermedad: es una etapa de la vida. Pero trae cambios reales en el cuerpo, y entenderlos te ayuda a tomar mejores decisiones.</p>
<div class="nutri-card"><img src="img/eugenia.jpg" alt="{NUTRI}"><div><span class="pill">TE GUÍA</span><h3>{NUTRI}</h3><p class="nc-t">{NUTRI_TIT} · Equipo RENOVA</p>
<p>En esta guía te explico, con evidencia y sin mitos, cómo la alimentación puede acompañar tu músculo, tus huesos, tu corazón y tu energía en esta etapa.</p></div></div>
<h2>Cómo leer esta guía</h2>
{ul(["<b>Cada capítulo es corto</b> y termina con acciones concretas.",
     "<b>Marcamos el nivel de evidencia:</b> sólida, limitada o no demostrada, para que sepas qué está probado.",
     "<b>No es un tratamiento:</b> es educación. Las indicaciones individuales las da tu equipo de salud.",
     "<b>Complementa a Alimentación Inteligente:</b> allá te organizás y tenés las recetas; acá entendés la etapa."])}

''', chapter="Bienvenida", pid="bienvenida")

page("__TOC__", chapter="Índice", pid="indice")

# ================================================================== 01
page(f'''
{chap_head("01", 'Comprender <span class="t">la etapa</span>', "Perimenopausia, menopausia y posmenopausia no son lo mismo. Saber en cuál estás ayuda a entender lo que sentís.")}
{table(["Etapa", "Qué pasa", "Cuándo"], [
 ["<b>Perimenopausia</b>", "Los ovarios producen hormonas de forma irregular. Los ciclos cambian y pueden aparecer sofocos, alteraciones del sueño o del ánimo.", "Suele empezar entre los 40 y los 50, y dura varios años."],
 ["<b>Menopausia</b>", "Es el momento de la última menstruación. Se confirma después de 12 meses seguidos sin menstruar.", "En promedio, alrededor de los 50."],
 ["<b>Posmenopausia</b>", "Los estrógenos quedan bajos de forma estable. Cobra importancia cuidar huesos, músculo y corazón.", "El resto de la vida, a partir de la menopausia."],
])}
<div class="etapas"><div class="et e1"><b>Perimenopausia</b><span>Ciclos irregulares, primeros síntomas</span></div><div class="et e2"><b>Menopausia</b><span>Última menstruación (12 meses sin ciclo)</span></div><div class="et e3"><b>Posmenopausia</b><span>Estrógenos bajos estables</span></div></div>
<h2>¿Por qué importa tanto el estrógeno?</h2>
<p>El estrógeno no solo regula el ciclo: también participa en el mantenimiento del hueso, en la distribución de la grasa corporal, en el metabolismo de las grasas en sangre y en la regulación de la temperatura. Cuando baja, todo eso se modifica.</p>
{box("<b>Cada mujer lo vive distinto.</b> Hay quienes casi no tienen síntomas y quienes los sienten mucho. Si los síntomas afectan tu calidad de vida, consultá con tu ginecólogo/a: existen tratamientos efectivos y seguros para muchas mujeres.", "note")}
<div class="esen"><h3>En la práctica</h3>{checks(['Anotá durante un mes tus ciclos y síntomas (sofocos, sueño, ánimo): te sirve para la consulta.', 'Pedí un control ginecológico si tus ciclos cambiaron o tenés síntomas que te molestan.', 'Empezá ya con fuerza y buena alimentación: cuanto antes, mejor llegás a la posmenopausia.'])}</div>
''', chapter="01 · Comprender la etapa", pid="c1", toc="01 · Comprender la etapa")


page(f'''
{eyebrow("COMPRENDER LA ETAPA")}
<h1 class="h1">Perimenopausia: <span class="t">los cambios empiezan antes</span></h1>
<p>Muchas mujeres notan cambios <b>años antes</b> de la última menstruación, y no siempre los relacionan con esta etapa. Las hormonas suben y bajan de forma irregular, por eso los síntomas pueden ir y venir.</p>
{table(["Lo que podés notar", "Qué hacer"], [
 ["Ciclos más cortos, más largos o más abundantes", "Registrarlos y consultar si el sangrado es muy abundante o fuera de lo habitual."],
 ["Sofocos o sudoración nocturna", "Identificar disparadores y consultar si afectan tu descanso."],
 ["Dormir peor, despertarte de noche", "Rutina de sueño, menos cafeína y alcohol a la tarde y noche."],
 ["Cambios de ánimo, irritabilidad, más ansiedad", "Movimiento, descanso y pedir ayuda si interfiere en tu vida."],
 ["Cambios en el peso y la cintura", "Fuerza, proteína en cada comida y no hacer dietas extremas."],
])}
{box("<b>Es el mejor momento para empezar.</b> Lo que construís en la perimenopausia —músculo, hueso, hábitos— es lo que te cuida en la posmenopausia.", "soft")}
''', chapter="01 · Comprender la etapa", pid="c1b")
# ================================================================== 02
page(f'''
{chap_head("02", 'Hormonas y <span class="t">composición corporal</span>', "No es solo “el metabolismo que se pone lento”: cambia dónde se acumula la grasa y cuánto músculo conservás.")}
<h2>Qué cambia</h2>
{checks(["<b>La grasa tiende a ubicarse más en el abdomen</b> (grasa visceral). La baja de estrógenos se asocia a este cambio, junto con la edad, el sueño y la actividad física.",
         "<b>Se pierde masa muscular</b> más rápido si no hay estímulo de fuerza.",
         "<b>Baja un poco el gasto de energía</b>, sobre todo por tener menos músculo y menos movimiento.",
         "<b>El sueño y el estrés</b> influyen en el apetito y en las elecciones de comida."])}
<img class="mimg" src="img/meno/activa.jpg" alt="Mujer activa entrenando">
<h2>Qué podés hacer</h2>
<div class="tips10 t3">
  <div><span>01</span><h3>Entrená fuerza</h3><p>Es la herramienta principal para conservar y ganar músculo.</p></div>
  <div><span>02</span><h3>Proteína en cada comida</h3><p>Ayuda a que el entrenamiento rinda (capítulo 3).</p></div>
  <div><span>03</span><h3>Calidad, no restricción</h3><p>Dietas muy bajas en calorías aceleran la pérdida de músculo.</p></div>
</div>
{evid("Sólida", "el entrenamiento de fuerza con una alimentación adecuada en proteínas preserva la masa muscular en mujeres de mediana edad y mayores.")}
{box("<b>Mirá la cintura, no solo la balanza.</b> El perímetro de cintura refleja mejor la grasa abdominal que el peso. Medilo cada 4 semanas, siempre igual.", "soft")}
<div class="esen"><h3>En la práctica</h3>{checks(['Medí tu cintura hoy y anotala.', 'Agendá 2 o 3 sesiones de fuerza esta semana.', 'Revisá si tus comidas tienen proteína y verduras.', 'No hagas dietas muy restrictivas: cuidá el músculo.'])}</div>
''', chapter="02 · Hormonas y cuerpo", pid="c2", toc="02 · Hormonas y composición corporal")

# ================================================================== 03
page(f'''
{chap_head("03", 'Proteínas y <span class="t">masa muscular</span>', "Con los años, el músculo responde menos a la proteína. Por eso importa la cantidad, la calidad y cómo la repartís.")}
<h2>Tres claves</h2>
{ul(["<b>Repartila en el día:</b> una fuente de proteína en desayuno, almuerzo, merienda y cena rinde más que concentrarla en la cena.",
     "<b>Elegí fuentes variadas:</b> huevo, lácteos, carnes, pollo, pescado, legumbres, soja y derivados.",
     "<b>Combinala con fuerza:</b> la proteína sola no construye músculo; el estímulo del entrenamiento es el que lo hace."])}
{table(["Momento", "Ideas de proteína"], [
 ["Desayuno", "Yogur natural o griego, huevo, queso, leche"],
 ["Almuerzo / cena", "Pollo, carne magra, pescado, legumbres, tofu, huevo"],
 ["Merienda", "Yogur, queso fresco, hummus, frutos secos con lácteo"],
])}
<p>Las recomendaciones generales para adultos mayores sugieren que la necesidad de proteína puede ser algo mayor que en la juventud, sobre todo si entrenás. <b>La cantidad exacta para vos depende de tu peso, tu actividad y tu salud renal</b>: pedila a tu nutricionista.</p>
{evid("Sólida", "repartir la proteína en las comidas y combinarla con entrenamiento de fuerza favorece el mantenimiento muscular.")}
<div class="esen"><h3>En la práctica</h3>{checks(['Sumá proteína al desayuno: yogur, huevo o queso.', 'Tené siempre a mano una proteína rápida: huevos, atún, legumbres de lata, yogur.', 'Si no comés carne, combiná legumbres, huevo, lácteos y soja durante el día.'])}</div>
''', chapter="03 · Proteínas y músculo", pid="c3", toc="03 · Proteínas y masa muscular")


page(f'''
{eyebrow("NUTRIENTES CLAVE")}
<h1 class="h1">Nutrientes clave <span class="t">en esta etapa</span></h1>
{table(["Nutriente", "Para qué", "Fuentes"], [
 ["<b>Proteína</b>", "Músculo y hueso", "Huevo, lácteos, carnes, pescado, legumbres, soja"],
 ["<b>Calcio</b>", "Hueso", "Leche, yogur, quesos, sardinas, almendras, vegetales de hoja, alimentos fortificados"],
 ["<b>Vitamina D</b>", "Absorción de calcio, músculo", "Sol, pescados grasos, huevo, alimentos fortificados"],
 ["<b>Fibra</b>", "Saciedad, intestino, colesterol", "Verduras, frutas, legumbres, avena, integrales"],
 ["<b>Omega-3</b>", "Corazón", "Pescados grasos (caballa, sardina, salmón), nueces, chía, lino"],
 ["<b>Hierro</b>", "Energía (clave si tenés sangrados abundantes)", "Carnes, legumbres + vitamina C, vegetales de hoja"],
])}
<p class="small">Las cantidades individuales las define tu nutricionista según tu edad, actividad y análisis.</p>
''', chapter="03 · Proteínas y músculo", pid="c3b", toc="Nutrientes clave")
# ================================================================== 04
page(f'''
{chap_head("04", 'Salud <span class="t">ósea</span>', "Después de la menopausia la pérdida de hueso se acelera. La buena noticia: hay mucho que podés hacer.")}
<div class="tips10">
  <div><span>Ca</span><h3>Calcio</h3><p>Lácteos, quesos, yogur, sardinas con espinas, almendras, vegetales de hoja verde, bebidas vegetales fortificadas.</p></div>
  <div><span>D</span><h3>Vitamina D</h3><p>Se forma con el sol en la piel; está en pescados grasos, huevo y alimentos fortificados.</p></div>
  <div><span>P</span><h3>Proteína</h3><p>El hueso también necesita proteína para mantenerse.</p></div>
  <div><span>F</span><h3>Fuerza e impacto</h3><p>El hueso responde a la carga: entrenar fuerza lo estimula.</p></div>
</div>
<figure class="mfig"><img src="img/meno/calcio.jpg" alt="Alimentos con calcio"><figcaption>Fuentes de calcio: lácteos, sardinas, almendras, vegetales de hoja verde, legumbres, tofu y sésamo.</figcaption></figure>
{ul(["<b>Priorizá el calcio de los alimentos.</b> Para muchas mujeres, 2 o 3 porciones de lácteos (o alternativas fortificadas) por día cubren buena parte; tu nutricionista ajusta la cantidad.",
     "<b>Vitamina D:</b> si tenés poca exposición al sol, pedí que te la midan. El suplemento solo con indicación.",
     "<b>Menos alcohol y nada de tabaco:</b> ambos aumentan la pérdida ósea.",
     "<b>Densitometría:</b> consultá con tu médico/a cuándo hacerla según tus factores de riesgo."])}
{evid("Sólida", "calcio y vitamina D adecuados, junto con ejercicio con carga, son pilares en la prevención de la osteoporosis.")}
<div class="esen"><h3>En la práctica</h3>{checks(['Si los tolerás, 2 o 3 porciones de lácteos al día; si no, alternativas fortificadas o sin lactosa.', 'Pasá tiempo al aire libre; la exposición solar necesaria varía según estación, lugar, horario y tipo de piel. Preguntá si conviene medir tu vitamina D.', 'Consultá por la densitometría y por medir vitamina D.', 'Entrená fuerza: el hueso responde a la carga.'])}</div>
''', chapter="04 · Salud ósea", pid="c4", toc="04 · Salud ósea")

# ================================================================== 05
page(f'''
{chap_head("05", 'Alimentación <span class="t">y síntomas</span>', "Sofocos, sueño, apetito y energía: qué puede ayudar desde la alimentación y qué no tiene respaldo.")}
{table(["Síntoma", "Puede ayudar", "Evidencia"], [
 ["<b>Sofocos</b>", "Identificar disparadores (alcohol, picante, café muy caliente, ambientes calurosos). Las isoflavonas de soja muestran un efecto modesto en algunas mujeres.", "Limitada"],
 ["<b>Sueño</b>", "Cenar liviano y temprano, limitar cafeína después del mediodía y alcohol a la noche, horarios regulares.", "Sólida (higiene del sueño)"],
 ["<b>Apetito y ansiedad</b>", "Comidas con proteína y fibra, no saltear comidas, dormir mejor y manejar el estrés.", "Sólida"],
 ["<b>Energía</b>", "Comer a intervalos regulares, hidratarte, hacer actividad física y descartar déficit de hierro o vitamina B12 con tu médico/a.", "Sólida"],
 ["<b>Salud intestinal</b>", "Fibra variada (verduras, frutas, legumbres, integrales), yogur y agua.", "Sólida"],
])}
<h2>Qué puede y qué no puede la alimentación</h2>
<div class="cols2 keep"><div class="esen"><h3>Puede</h3>{checks(["Ayudarte a dormir y descansar mejor.", "Darte energía más estable en el día.", "Cuidar músculo, hueso y corazón a largo plazo.", "Hacer más llevaderos algunos síntomas."])}</div>
<div class="esen"><h3>No puede</h3>{ul(["“Equilibrar” tus hormonas con un alimento.", "Eliminar los sofocos por sí sola.", "Reemplazar un tratamiento médico cuando hace falta."])}</div></div>
{box("<b>Si los síntomas son intensos,</b> la alimentación ayuda pero no siempre alcanza. La terapia hormonal y otros tratamientos son opciones que se evalúan con tu ginecólogo/a, según tu historia.", "note")}
<div class="esen"><h3>En la práctica</h3>{checks(['Anotá qué dispara tus sofocos durante dos semanas.', 'Cortá la cafeína después del mediodía y probá cenar más temprano.', 'Si te cuesta dormir, armá una rutina: misma hora, poca pantalla, cuarto fresco.'])}</div>
''', chapter="05 · Alimentación y síntomas", pid="c5", toc="05 · Alimentación y síntomas")

# ================================================================== 06
page(f'''
{chap_head("06", 'Salud <span class="t">cardiometabólica</span>', "Con la baja de estrógenos aumenta el riesgo cardiovascular. Es el momento de cuidar el corazón con hábitos.")}
<h2>Qué suele cambiar</h2>
{checks(["Sube el colesterol LDL (el “malo”).", "En algunas mujeres empeora la sensibilidad a la insulina; influyen la edad, la grasa abdominal y la actividad física, no solo las hormonas.", "Puede subir la presión arterial."])}
<figure class="mfig"><img src="img/meno/mediterraneo.jpg" alt="Plato tipo mediterráneo"><figcaption>Un plato tipo mediterráneo: pescado, cereal integral, verduras, palta y aceite de oliva.</figcaption></figure>
<h2>Qué ayuda</h2>
{table(["Hábito", "Cómo llevarlo a la práctica"], [
 ["<b>Patrón tipo mediterráneo</b>", "Verduras, frutas, legumbres, integrales, aceite de oliva, frutos secos y pescado."],
 ["<b>Fibra soluble</b>", "Avena, legumbres, frutas como manzana y cítricos: ayudan con el colesterol."],
 ["<b>Menos sal</b>", "Cociná con hierbas y especias; leé el sodio en las etiquetas."],
 ["<b>Grasas de calidad</b>", "Preferí aceite de oliva, palta, frutos secos y pescado; limitá frituras y procesados."],
 ["<b>Menos azúcar agregada</b>", "Agua como bebida principal; postres ocasionales."],
 ["<b>Movimiento</b>", "Fuerza 2 o 3 veces por semana y caminatas."],
])}
{evid("Sólida", "el patrón alimentario mediterráneo y la actividad física regular reducen el riesgo cardiovascular.")}
{box("<b>Controles:</b> pedí a tu médico/a perfil lipídico, glucemia y control de presión con la frecuencia que te indique.", "soft")}
<div class="esen"><h3>En la práctica</h3>{checks(['Cambiá la manteca por aceite de oliva y sumá frutos secos.', 'Comé legumbres 2 o 3 veces por semana y pescado al menos 1 o 2.', 'Cociná con hierbas y especias para usar menos sal.', 'Pedí tus análisis de rutina.'])}</div>
''', chapter="06 · Corazón y metabolismo", pid="c6", toc="06 · Salud cardiometabólica")

# ================================================================== 07
page(f'''
{chap_head("07", 'Suplementos <span class="t">y desinformación</span>', "Hay muchos productos “para la menopausia”. Pocos tienen respaldo y algunos pueden tener riesgos.")}
{table(["Suplemento", "Qué se sabe"], [
 ["<b>Vitamina D</b>", "Útil si hay déficit comprobado. La dosis la indica tu médico/a según tu análisis."],
 ["<b>Calcio</b>", "Primero, de los alimentos. El suplemento se indica si la dieta no alcanza."],
 ["<b>Proteína en polvo</b>", "Práctica si no llegás con comida; no es obligatoria."],
 ["<b>Creatina</b>", "Evidencia creciente junto al entrenamiento de fuerza; consultá antes de usarla."],
 ["<b>Isoflavonas de soja</b>", "Efecto modesto sobre sofocos en algunas mujeres; consultá si tenés antecedentes de cáncer de mama."],
 ["<b>Productos “quemagrasa” o “detox”</b>", "Sin evidencia. Pueden interactuar con medicamentos."],
])}
{ul(["<b>Natural no significa seguro:</b> algunas hierbas interactúan con medicación o afectan el hígado.",
     "<b>Desconfiá de promesas rápidas</b> y de quien vende el producto que recomienda.",
     "<b>Antes de tomar cualquier suplemento,</b> contale a tu médico/a qué medicación tomás."])}
<div class="esen"><h3>En la práctica</h3>{checks(['Hacé una lista de lo que tomás hoy (medicación y suplementos) y llevala a la consulta.', 'Antes de comprar un suplemento, preguntate: ¿tengo un déficit comprobado?', 'Desconfiá de “resultados rápidos” y “naturales sin riesgos”.'])}</div>
''', chapter="07 · Suplementos", pid="c7", toc="07 · Suplementos y desinformación")

# ================================================================== 08
page(f'''
{chap_head("08", 'Alimentación <span class="t">en la vida real</span>', "Llevar todo esto a una semana con trabajo, familia y poco tiempo.")}
<h2>Un día de ejemplo</h2>
{table(["Momento", "Ejemplo"], [
 ["<b>Desayuno</b>", "Yogur natural con avena, fruta y semillas"],
 ["<b>Almuerzo</b>", "Pollo con ensalada de hojas, garbanzos y aceite de oliva"],
 ["<b>Merienda</b>", "Tostada integral con queso y una fruta"],
 ["<b>Cena</b>", "Pescado al horno con verduras y papa"],
])}
<p class="small">Es un ejemplo para orientarte, no un menú obligatorio. En <b>Alimentación Inteligente</b> tenés 8 semanas de recetas y combinaciones.</p>
<h2>Tres situaciones frecuentes</h2>
{ul(["<b>“No tengo hambre a la mañana”:</b> empezá con algo chico con proteína (un yogur) y sumá más a media mañana.",
     "<b>“A la noche me agarra la ansiedad”:</b> revisá si comiste suficiente proteína y fibra durante el día; la cena temprana y completa ayuda.",
     "<b>“Viajo o tengo eventos”:</b> elegí proteína y vegetales cuando puedas, hidratate y volvé a tu rutina en la comida siguiente."])}
<div class="esen"><h3>En la práctica</h3>{checks(['Elegí un desayuno con proteína para esta semana.', 'Prepará dos comidas de respaldo para los días complicados.', 'Usá el programa de 8 semanas de Alimentación Inteligente para organizarte.'])}</div>
''', chapter="08 · Vida real", pid="c8", toc="08 · Alimentación en la vida real")


page(f'''
{eyebrow("CASOS PRÁCTICOS")}
<h1 class="h1">Tres situaciones <span class="t">de la vida real</span></h1>
<div class="mitos">
  <div><b>Laura, 46 · perimenopausia</b><p>Duerme mal y a la noche pica. <b>Qué cambia:</b> cena completa con proteína, sin café después de las 14, rutina de sueño y registro de síntomas para su consulta.</p></div>
  <div><b>Claudia, 53 · posmenopausia</b><p>Su densitometría salió baja. <b>Qué cambia:</b> 3 porciones de lácteos al día, fuerza 2 veces por semana, consulta por vitamina D y seguimiento médico.</p></div>
  <div><b>Silvia, 49 · viaja por trabajo</b><p>Come en aeropuertos y hoteles. <b>Qué cambia:</b> yogur y frutos secos en la cartera, proteína y verduras en el menú, y fuerza en la habitación 20 minutos.</p></div>
  <div><b>Mariana, 51 · sofocos</b><p>Los sofocos la despiertan. <b>Qué cambia:</b> identifica que el vino y el picante los empeoran, ajusta la cena y consulta con su ginecóloga por opciones de tratamiento.</p></div>
</div>
<p class="small">Casos ilustrativos, no personas reales. Cada situación necesita una evaluación individual.</p>
''', chapter="08 · Vida real", pid="c8b")
# ================================================================== 09
page(f'''
{chap_head("09", 'Mitos <span class="t">frecuentes</span>', "Lo que circula en redes y lo que dice la evidencia.")}
<div class="mitos">
  <div><b>Mito:</b> “En la menopausia hay que dejar los carbohidratos.”<p><b>Realidad:</b> no hace falta eliminarlos. Elegí integrales, legumbres y frutas, y ajustá la cantidad a tu actividad.</p></div>
  <div><b>Mito:</b> “El ayuno intermitente es lo mejor para esta etapa.”<p><b>Realidad:</b> puede servirle a algunas personas, pero no es superior a otras formas de comer y puede dificultar llegar a la proteína que necesitás.</p></div>
  <div><b>Mito:</b> “La soja es peligrosa.”<p><b>Realidad:</b> como alimento (tofu, porotos de soja, bebida) forma parte de una alimentación saludable. Si tenés antecedentes oncológicos, consultá.</p></div>
  <div><b>Mito:</b> “Los lácteos inflaman.”<p><b>Realidad:</b> no hay evidencia de eso en la población general, y son una fuente clave de calcio y proteína.</p></div>
  <div><b>Mito:</b> “Subir de peso es inevitable.”<p><b>Realidad:</b> los cambios son reales, pero la fuerza, la proteína, el sueño y el movimiento diario marcan una gran diferencia.</p></div>
  <div><b>Mito:</b> “Hay que hacer mucho cardio para bajar la panza.”<p><b>Realidad:</b> la fuerza es prioridad para conservar músculo; el cardio suma, pero no reemplaza.</p></div>
</div>
''', chapter="09 · Mitos", pid="c9", toc="09 · Mitos frecuentes")

# ================================================================== 10
page(f'''
{chap_head("10", 'Tu plan <span class="t">de continuidad</span>', "Elegí tus prioridades, llevá preguntas a la consulta y medí lo que importa.")}
<h2>Guía para tu consulta</h2>
<div class="cols2 keep"><div><h3>Con tu ginecólogo/a o médico/a</h3>{checks(["¿En qué etapa estoy?", "¿Conviene una densitometría? ¿Cada cuánto?", "¿Medimos vitamina D, hierro o B12?", "¿Cómo están colesterol, glucemia y presión?", "¿La terapia hormonal es una opción para mí?"])}</div>
<div><h3>Con tu nutricionista</h3>{checks(["¿Cuánta proteína necesito con mi entrenamiento?", "¿Llego al calcio con mi alimentación?", "¿Necesito algún suplemento?", "¿Cómo adapto mis comidas a mis síntomas?"])}</div></div>
<p class="small"><b>Llevá:</b> tu registro de síntomas (página <span class="pref" data-ref="registro"></span>), la lista de medicación y suplementos, y tus últimos análisis.</p>
<h2>Mis 3 prioridades para este mes</h2>
{table(["Prioridad", "Qué voy a hacer", "Cómo lo mido"], [["1", "", ""], ["2", "", ""], ["3", "", ""]])}
<p class="small"><b>Cada 4 semanas medí:</b> perímetro de cintura, tu fuerza (repeticiones o peso) y cómo dormís y tu energía (del 1 al 10).</p>
''', chapter="10 · Continuidad", pid="c10", toc="10 · Tu plan de continuidad")


page(f'''
{eyebrow("HERRAMIENTA")}
<h1 class="h1">Tus hábitos <span class="t">prioritarios</span></h1>
<p class="small">Marcá los que ya hacés y elegí 2 para sumar este mes. No hace falta hacer todo junto.</p>
{table(["Hábito", "Ya lo hago", "Lo sumo"], [[h, "☐", "☐"] for h in ["Entreno fuerza 2 o 3 veces por semana", "Como proteína en cada comida", "Como verduras en almuerzo y cena", "Sumo lácteos o alternativas con calcio", "Como legumbres 2 o 3 veces por semana", "Como pescado 1 o 2 veces por semana", "Camino o me muevo todos los días", "Duermo 7 a 8 horas", "Limito alcohol y cafeína a la tarde", "Tomo agua durante el día"]])}
''', chapter="Herramientas", pid="habitos", toc="Herramienta: hábitos prioritarios")

page(f'''
{eyebrow("HERRAMIENTA")}
<h1 class="h1">Registro de <span class="t">14 días</span></h1>
<p class="small">Completalo 2 semanas antes de tu consulta. Puntuá del 0 (nada) al 3 (mucho). En “Actividad”, anotá si entrenaste o caminaste; en “Hábito”, el que estés trabajando. No sirve para diagnosticar: es información para tu profesional.</p>
{table(["Día", "Sofocos", "Sueño", "Ánimo", "Energía", "Actividad", "Hábito"], [[f"Día {d}", "", "", "", "", "", ""] for d in range(1, 15)])}
''', chapter="Herramientas", pid="registro", toc="Herramienta: registro de 14 días")
page(f'''
{eyebrow("FUENTES")}
<h1 class="h1">Fuentes <span class="t">y aclaraciones</span></h1>
{ul(["Ministerio de Salud de la Nación (2016). <i>Guías Alimentarias para la Población Argentina</i>. argentina.gob.ar/salud",
     "Organización Mundial de la Salud (2024). <i>Menopausia</i> (nota descriptiva). who.int/news-room/fact-sheets/detail/menopause",
     "The North American Menopause Society (2022). The 2022 hormone therapy position statement. <i>Menopause</i>, 29(7), 767–794. doi:10.1097/GME.0000000000002028",
     "The Menopause Society (2023). The 2023 nonhormone therapy position statement. <i>Menopause</i>, 30(6), 573–590. doi:10.1097/GME.0000000000002200",
     "El Khoudary, S. R., et al. (2020). Menopause transition and cardiovascular disease risk. <i>Circulation</i>, 142(25), e506–e532. doi:10.1161/CIR.0000000000000912",
     "International Osteoporosis Foundation. <i>Nutrition and bone health</i>. osteoporosis.foundation"])}
{box("<b>Material educativo general.</b> Esta guía no reemplaza la consulta médica, ginecológica ni nutricional. No indica tratamientos, dosis de suplementos ni cantidades individuales de nutrientes. Ante síntomas, enfermedades o medicación, consultá con tu equipo de salud.", "note")}
<p class="small">Revisión de contenidos: {NUTRI}, {NUTRI_TIT}.</p>
''', chapter="Fuentes", pid="fuentes", toc="Fuentes y aclaraciones")

page(f'''
<div class="bio metodo">
  {eyebrow("PLAN INTEGRAL RENOVA")}
  <h1 class="h1 big">Tu plan integral <span class="t">1 a 1 con Nacho</span></h1>
  <div class="team-big"><img src="img/equipo2.jpg" alt="Equipo RENOVA" style="height:auto;max-height:120mm;object-fit:contain"></div>
  <p class="lead center">Esta guía te explica la etapa. <b>Si querés un plan hecho para vos,</b> lo armamos con el equipo RENOVA:</p>
  <div class="cp-pills"><span>✓ Entrenamiento a tu medida</span><span>✓ Nutrición para tu etapa</span><span>✓ Seguimiento de tu progreso</span></div>
  <p class="center"><b>Consultá por tu plan integral 1 a 1 con Nacho</b> y contanos en qué etapa estás.</p>
  <div class="cta-center"><a class="btn btn-big" href="{esc(LINK_PLAN)}">CONSULTÁ POR TU PLAN {ICON_ARROW}</a></div>
  <div class="quote dark">Esta etapa no es un final. <span class="t2">Es un buen momento para cuidarte.</span></div>
</div>
''', chapter="Plan integral", pid="metodo", toc="Tu plan integral 1 a 1")


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
            hdr = (f'<div class="hdr"><span>NUTRICIÓN EN LA MENOPAUSIA · <b>RENOVA</b></span><span>{esc(p["chapter"])}</span></div>'
                   f'<div class="ftr"><a class="toidx" href="#indice">{ICON_HAND} Hacé clic y volvé al índice</a><span class="pgnum"></span></div>')
        out.append(f'<section class="page {p["cls"]}" id="{p["id"]}">{hdr}<div class="body">{body}</div></section>')
    css = ds_css(HERE) + "\n" + open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Nutrición en la menopausia · RENOVA</title>'
            f'<style>{css}</style></head><body class="grande">' + "".join(out) + '<script src="paginate.js"></script></body></html>')


if __name__ == "__main__":
    with open(os.path.join(HERE, "menopausia.html"), "w", encoding="utf-8") as f:
        f.write(render())
    print("menopausia.html ·", len(PAGES), "páginas antes de paginar")
