"""Ebook "Sin TACC Inteligente": lista de compras, cocina y organización semanal 80/20 para personas con celiaquía.
Producto aparte (no upsell). Promesa: "Tu semana Sin TACC resuelta: qué comprar, qué cocinar y cómo organizarte".
Autores: Nacho Portillo y la nutricionista del equipo, + Equipo RENOVA. Estrategia y fuentes: investigacion/sin-tacc/.
Las recetas salen de Alimentación Inteligente (nutricion.py): solo las que son sin TACC o se adaptan sin avena ni trigo.

Uso:  cd fuentes/ebook && python3 sintacc.py && node export.js sintacc
      → sin-tacc-inteligente/Ebook_Sin_TACC_Inteligente_RENOVA.pdf
"""
import copy
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "design-system"))
from design_system import css as ds_css, esc, ICON_ARROW, ICON_HAND, eyebrow, chap_head, ul, checks, box

# Recetas, ficha y datos de la nutricionista: los mismos de Alimentación Inteligente (un solo lugar para cada dato).
_spec = importlib.util.spec_from_file_location("nutricion", os.path.join(HERE, "nutricion.py"))
NUT = importlib.util.module_from_spec(_spec)
_argv, sys.argv = sys.argv, ["nutricion.py"]   # edición de mujeres
_spec.loader.exec_module(NUT)
sys.argv = _argv

NUTRI, MATRICULA, AUTOR = NUT.NUTRI, NUT.MATRICULA, "Nacho Portillo"
LINK_PLAN = "https://wa.link/1asjt1"
LINK_SKOOL = "https://www.skool.com/renova-entrenamiento-y-salud-1617/about"
LINK_ANMAT = "https://listadoalg.anmat.gob.ar"
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


def practica(items):
    return f'<div class="esen"><h3>En la práctica</h3>{checks(items)}</div>'


# ------------------------------------------------------------------ recetas (de Alimentación Inteligente)
_TODAS = [r for s in NUT.SEMANAS for r in s["recetas"]]
for _v in vars(NUT).values():
    if isinstance(_v, list) and _v and isinstance(_v[0], dict) and "ing" in _v[0]:
        _TODAS += [r for r in _v if r not in _TODAS]


def receta(titulo, **cambios):
    r = copy.deepcopy(next(x for x in _TODAS if x["t"] == titulo))
    r.update(cambios)
    return r


RECETAS = [
    receta("Pancake de coco", ing=["2 huevos (o 1 huevo y 1 clara)", "5 cdas de coco rallado", "1 cdita de polvo de hornear con logo oficial", "Esencia de vainilla y gotas de stevia"],
           cambio="coco por harina de almendras; stevia por fruta pisada."),
    receta("Granola de quinoa", ing=["1 taza de quinoa cocida (⅓ taza cruda)", "¼ taza de semillas de girasol y zapallo", "¼ taza de frutos secos picados", "¼ taza de coco rallado y canela"],
           cambio="si la querés más dulce, 2 dátiles picados en lugar de miel o azúcar."),
    receta("Galletitas de 4 ingredientes sin azúcar", ing=["¼ taza de harina de garbanzos con logo oficial", "2 cdas de pasta de maní", "4 dátiles sin carozo (remojados si están secos)", "4 nueces picadas, 3 cdas de agua y ½ cdita de polvo de hornear Sin TACC"]),
    receta("Crackers de semillas"),
    receta("Ensalada tibia de vegetales, legumbres y pollo"),
    receta("Pescado al horno con papas y vegetales"),
    receta("Omelette de espinaca y queso"),
    receta("Batatas rellenas de pollo y queso"),
    receta("Tortilla de verduras en sartén"),
    receta("Pollo con calabaza en una sola fuente"),
    receta("Crema de zapallo con lentejas rojas", ing=["500 g de zapallo en cubos", "½ taza de lentejas rojas", "1 cebolla", "Caldo casero o agua (si usás caldo en cubo, con logo oficial), sal y comino"]),
    receta("Milanesas de berenjena", ing=["1 berenjena grande en rodajas", "2 huevos batidos", "Rebozador o pan rallado con logo oficial, polenta o semillas, con orégano", "Queso y tomate para napolitana (opcional)"],
           cambio="berenjena por zucchini o pechuga de pollo; acompañá con una proteína."),
]

# Recetas argentinas de alta demanda: BORRADOR armado por RENOVA, a validar por la nutricionista. Foto pendiente.
# Cuando estén aprobadas: sacar " · BORRADOR" de la categoría, el aviso de la página de recetas y poner la foto.
B = " · BORRADOR"
RECETAS_BORRADOR = [
    NUT.rec("Pizza de fainá", "Almuerzo o cena" + B, "45 min (con reposo)", "2 porciones",
            ["1 taza de harina de garbanzos con logo oficial", "1 taza de agua", "1 cda de aceite de oliva y sal",
             "Salsa de tomate casera, muzzarella con logo oficial y orégano"],
            ["Mezclá la harina, el agua, el aceite y la sal sin grumos y dejala reposar 30 minutos.",
             "Volcá en una pizzera aceitada y horneá 10 a 12 minutos en horno alto, hasta que se despegue.",
             "Cubrí con salsa, muzzarella y orégano, y horneá 6 a 8 minutos más."],
            "muzzarella por queso port salut con logo; sumá vegetales asados arriba.", "1 día en heladera; recalentar en sartén.", foto="pendiente"),
    NUT.rec("Empanadas de carne al horno", "Para compartir" + B, "60 min", "12 unidades",
            ["Masa: 2 tazas de premezcla con logo oficial, ½ cdita de sal, 3 cdas de aceite y ½ taza de agua tibia (aprox.)",
             "Relleno: 400 g de carne picada magra, 1 cebolla, ½ morrón y 1 huevo duro",
             "Comino, pimentón y ají molido con logo oficial"],
            ["Uní la premezcla con la sal, el aceite y el agua hasta lograr una masa suave; si se agrieta, sumá agua de a cucharadas.",
             "Rehogá la cebolla y el morrón, sumá la carne y los condimentos, cociná y dejá enfriar; agregá el huevo picado.",
             "Estirá la masa entre dos films, cortá discos, rellená, cerrá con repulgue y horneá 15 a 20 minutos en horno alto."],
            "carne por pollo desmenuzado o por verdura y queso. Si tu premezcla no trae goma xántica, sumá ½ cdita.",
            "Congelalas crudas en una bandeja y después pasalas a una bolsa: se pueden freezar.", foto="pendiente"),
    NUT.rec("Tarta de verduras con masa casera", "Almuerzo o vianda" + B, "50 min", "4 porciones",
            ["Masa: 1 taza de harina de garbanzos o premezcla con logo oficial, 2 cdas de semillas, 3 cdas de aceite, sal y agua",
             "Relleno: 1 atado de acelga o espinaca, 1 cebolla, 3 huevos y 3 cdas de ricota o queso untable con logo oficial"],
            ["Uní los ingredientes de la masa con agua de a poco hasta que se pueda estirar; forrá una tartera aceitada.",
             "Rehogá la cebolla, sumá la verdura picada y cociná hasta que pierda el agua; mezclá con los huevos y la ricota.",
             "Rellená y horneá 30 a 35 minutos en horno medio, hasta que el centro esté firme."],
            "acelga por zapallo y choclo, o por calabaza y queso.", "3 días en heladera; se puede freezar en porciones.", foto="pendiente"),
    NUT.rec("Pan casero de semillas", "Desayuno o merienda" + B, "1 h 30 min (con levado)", "1 pan (12 rodajas)",
            ["2 tazas de premezcla con logo oficial", "1 sobre de levadura seca con logo oficial", "1 cdita de sal y 2 cdas de aceite",
             "1 ¼ taza de agua tibia", "3 cdas de semillas (girasol, lino, chía)"],
            ["Mezclá los secos, sumá el aceite y el agua tibia y batí hasta lograr una masa blanda (no se amasa como el pan común).",
             "Pasala a un molde aceitado, cubrí con semillas y dejá levar 40 minutos en un lugar cálido.",
             "Horneá 35 a 40 minutos en horno alto; desmoldá y dejá enfriar sobre una rejilla antes de cortar."],
            "semillas por nueces picadas. Si tu premezcla no trae goma xántica, sumá 1 cdita.",
            "Cortalo en rodajas y freezalo: tostás solo lo que vas a comer.", foto="pendiente"),
    NUT.rec("Ñoquis de papa", "Almuerzo" + B, "60 min", "4 porciones",
            ["1 kg de papas", "1 huevo", "1 taza de fécula de mandioca o premezcla con logo oficial (aprox.)", "Sal y nuez moscada con logo oficial"],
            ["Hervé las papas con cáscara, pelalas y pisalas en caliente.",
             "Sumá el huevo, la sal y la nuez moscada, y agregá la fécula de a poco hasta que la masa no se pegue.",
             "Hacé cilindros, cortá los ñoquis y hervilos en agua solo para ellos: están listos cuando suben."],
            "papa por batata o calabaza (necesitan algo más de fécula); salsa de tomate casera o filetto.",
            "Congelalos crudos y separados en una bandeja: se pueden freezar.", foto="pendiente"),
    NUT.rec("Budín de banana sin azúcar", "Desayuno o merienda" + B, "50 min", "1 budín (10 rodajas)",
            ["2 bananas bien maduras", "3 huevos", "1 ½ taza de harina de arroz o premezcla con logo oficial",
             "1 cdita de polvo de hornear con logo oficial, 3 cdas de aceite y canela", "Nueces picadas (opcional)"],
            ["Pisá las bananas y batilas con los huevos y el aceite.",
             "Sumá la harina, el polvo de hornear y la canela, y mezclá sin batir de más; agregá las nueces.",
             "Horneá en un molde aceitado 35 a 40 minutos en horno medio, hasta que un palillo salga seco."],
            "banana por manzana rallada; nueces por chips de chocolate amargo con logo oficial.",
            "4 días en heladera; en rodajas se puede freezar.", foto="pendiente"),
]

# ================================================================== PORTADA
page('''
<div class="cv3 nutri">
  <div class="c3-in">
    <img class="c3-logo" src="img/logo_renova.png" alt="RENOVA">
    <span class="c3-pill">GUÍA PRÁCTICA · CELIAQUÍA</span>
    <h1 class="c3-title">SIN TACC<br>INTELIGENTE</h1>
    <p class="c3-claim">TU SEMANA, <b><span>RESUELTA.</span></b></p>
    <p class="c3-sub">Para vos y tu familia: <b>qué comprar</b>,<br><span><em>qué cocinar</em> y <mark>cómo organizarte</mark>.</span></p>
  </div>
  <div class="c3-team"><img src="img/equipo_tapa.png" alt="Equipo RENOVA"></div>
</div>
''', pid="portada", cls="p-cover", header=False)

# ================================================================== BIENVENIDA
page(f'''
{eyebrow("BIENVENIDA")}
<h1 class="h1">Comer Sin TACC <span class="t">no tiene por qué ser complicado</span></h1>
<p class="lead">Esta guía es para vos si tenés <b>celiaquía diagnosticada</b> o cocinás para alguien que la tiene, y querés comer rico y sano sin depender de los productos envasados.</p>
<div class="nutri-card"><img src="img/nacho_full.jpg" alt="{AUTOR}"><div><span class="pill">TE GUÍA</span><h3>{AUTOR}</h3><p class="nc-t">Lic. en Alto Rendimiento · Creador de RENOVA</p>
<p>Con el equipo armamos esta guía para que dejes de pensar qué comprar y qué cocinar cada día, y puedas sostenerlo en una semana real.</p></div></div>
<div class="nutri-card"><img src="img/eugenia.jpg" alt="{NUTRI}"><div><span class="pill">TE GUÍA</span><h3>{NUTRI}</h3><p class="nc-t">Lic. en Nutrición · {MATRICULA} · Equipo RENOVA</p>
<p>Te explico cómo elegir en el súper, cómo cocinar sin riesgo y cómo sumar fibra y proteína cuando no comés gluten.</p></div></div>
<h2>Cómo usar esta guía</h2>
{ul(["<b>Leé los capítulos 1 a 6 una vez:</b> son cortos y te dan la base.",
     "<b>Usá la lista de compras y el plan 80/20 todas las semanas.</b> Están también en versión imprimible al final.",
     "<b>Cociná las recetas</b> y repetí las que más te gusten.",
     "<b>No reemplaza a tu médico/a ni a tu nutricionista:</b> es una guía práctica para el día a día."])}
{box("<b>Material educativo general.</b> Esta guía no reemplaza la consulta médica ni nutricional. La alimentación sin TACC es para personas con celiaquía diagnosticada. Ante síntomas, dudas o medicación, consultá con tu equipo de salud.", "note")}
''', chapter="Bienvenida", pid="bienvenida")

page("__TOC__", chapter="Índice", pid="indice")

# ================================================================== 01
page(f'''
{chap_head("01", 'Celiaquía <span class="t">en 5 minutos</span>', "Lo básico que necesitás tener claro para elegir y cocinar tranquila.")}
<h2>Qué es TACC</h2>
<div class="tips10">
  <div><span>T</span><h3>Trigo</h3><p>Harina, pan, fideos, galletitas, rebozadores.</p></div>
  <div><span>A</span><h3>Avena</h3><p>Solo si el producto está autorizado y figura vigente en el listado de ANMAT. Si no, afuera.</p></div>
  <div><span>C</span><h3>Cebada</h3><p>Malta, cerveza, algunas bebidas y extractos.</p></div>
  <div><span>C</span><h3>Centeno</h3><p>Panes y galletas de centeno.</p></div>
</div>
{ul(["<b>La celiaquía es una enfermedad autoinmune:</b> el gluten daña el intestino de quien la tiene, aunque no haya síntomas.",
     "<b>El único tratamiento es una alimentación sin TACC, estricta y de por vida.</b> No alcanza con \"comer poquito\".",
     "<b>Las trazas también cuentan:</b> por eso importan la etiqueta y la cocina (capítulos 3 y 4)."])}
{box("<b>Solo para celiaquía diagnosticada.</b> Si sospechás que el gluten te hace mal, no lo saques por tu cuenta: consultá antes, porque dejar el gluten puede alterar los estudios del diagnóstico.", "note")}
''', chapter="01 · Celiaquía en 5 minutos", pid="c1", toc="01 · Celiaquía en 5 minutos")

# ================================================================== 02
page(f'''
{chap_head("02", 'La trampa de los <span class="t">envasados sin gluten</span>', "Que un producto sea apto no quiere decir que sea saludable.")}
<p>Para que un pan, una galletita o un snack sin gluten tenga buena textura, muchas veces se hace con <b>almidones</b> (de maíz, arroz o mandioca) y se le suma <b>grasa, azúcar y sal</b>. Por eso:</p>
{table(["Comparados con su versión con gluten, muchos productos sin gluten…", "Qué significa para vos"], [
 ["Tienen <b>menos proteína</b>", "Te llenan menos y ayudan menos a tu músculo."],
 ["Tienen <b>más grasa</b> y, a veces, <b>más azúcar y sal</b>", "Suman calorías sin darte más nutrientes."],
 ["Pueden tener <b>menos fibra</b> (depende de la marca)", "Más riesgo de constipación y de tener hambre al rato."],
 ["Son <b>más caros</b>", "Comprar menos envasados también te ahorra plata."],
])}
<h2>La salida: cocinar más</h2>
{checks(["La base de tu semana son <b>alimentos naturalmente sin TACC</b>: verduras, frutas, carnes, huevos, legumbres, arroz, papa, batata, quinoa, lácteos.",
         "Los envasados aptos los usás <b>para resolver</b>, no como base: un pan para el desayuno, una galletita para la cartera.",
         "Cuando compres uno, <b>leé la etiqueta</b> y elegí el que tenga menos ingredientes, menos azúcar y más fibra."])}
''', chapter="02 · Los envasados", pid="c2", toc="02 · La trampa de los envasados sin gluten")

# ================================================================== 03
page(f'''
{chap_head("03", 'Leer la etiqueta <span class="t">Sin TACC</span>', "En 30 segundos sabés si un producto es apto y si te conviene. Basado en el taller de Eugenia en la comunidad RENOVA.")}
<h2>Paso 1 · ¿Es apto?</h2>
{checks(["Buscá el <b>logo oficial</b>: hoy conviven el anterior, <b>\"Sin T.A.C.C.\"</b>, y el nuevo, <b>\"sin GLUTEN\"</b> (desde fines de 2023 conviven los dos). Los dos son válidos.",
         f"<b>Comprobá que el producto figure vigente</b> en el Listado Integrado de Alimentos Libres de Gluten de ANMAT (<a href=\"{LINK_ANMAT}\">listadoalg.anmat.gob.ar</a>): hubo productos con logos que no correspondían.",
         "<b>No compres sueltos, a granel ni artesanales sin rótulo</b>: no hay forma de saber si se contaminaron."])}
<h2>Paso 2 · ¿Me conviene?</h2>
{table(["Mirá", "Qué buscar"], [
 ["<b>Ingredientes</b>", "Están ordenados de mayor a menor. Pocos, conocidos y coherentes con el producto."],
 ["<b>Porción</b>", "La tabla nutricional se calcula por porción: fijate cuánto es."],
 ["<b>Azúcar</b>", "Tiene muchos nombres: jarabe de maíz, dextrosa, maltodextrina, miel, azúcar invertido. Cuanto más arriba en la lista, más tiene."],
 ["<b>Grasas</b>", "Pocas grasas saturadas y nada de grasas trans o \"hidrogenadas\"."],
 ["<b>Fibra y proteína</b>", "Entre dos opciones aptas, elegí la que tenga más."],
 ["<b>Octógonos</b>", "Exceso de azúcares, grasas, sodio o calorías: si tiene varios, que sea ocasional."],
])}
''', chapter="03 · Leer la etiqueta", pid="c3", toc="03 · Leer la etiqueta Sin TACC")

page(f'''
{eyebrow("LEER LA ETIQUETA")}
<h1 class="h1">Marketing <span class="t">que confunde</span></h1>
{table(["Lo que dice el envase", "Lo que tenés que saber"], [
 ["\"Sin gluten\" escrito, sin logo oficial", "No alcanza: buscá el logo oficial y el producto en el listado de ANMAT."],
 ["\"Natural\", \"light\", \"0%\"", "No significa saludable ni apto. Leé la etiqueta."],
 ["\"Avena sin gluten\"", "Solo si tiene logo oficial y figura vigente en el listado de ANMAT. Si no lo encontrás, no la compres."],
 ["\"Puede contener trazas de trigo\"", "No es apto."],
 ["\"Integral\" o \"multicereal\"", "Si es de trigo, avena, cebada o centeno, no es apto aunque sea integral."],
])}
<div class="cols2 keep"><div class="esen"><h3>Elegí</h3>{checks(["Productos con logo y pocos ingredientes", "Harinas de legumbres, arroz integral, quinoa, trigo sarraceno con logo oficial", "Yogur natural, quesos con logo", "Frutos secos y semillas envasados con logo"])}</div>
<div class="esen"><h3>Limitá</h3>{ul(["Panificados y galletitas dulces aptos de todos los días", "Snacks y rebozados industriales", "Productos con muchos octógonos", "Lo suelto o sin rótulo: no comprar"])}</div></div>
''', chapter="03 · Leer la etiqueta", pid="c3b")

# ================================================================== 04
page(f'''
{chap_head("04", 'Cocina <span class="t">segura</span>', "La contaminación cruzada es la causa más común de comer gluten sin darte cuenta.")}
<div class="tips10 t3">
  <div><span>01</span><h3>Utensilios propios</h3><p>Tostadora, tabla de madera, colador y palo de amasar: los que tienen restos de harina, no se comparten.</p></div>
  <div><span>02</span><h3>Primero lo Sin TACC</h3><p>Cociná primero lo apto y después lo demás. Lavá bien sartenes y mesada entre una cosa y otra.</p></div>
  <div><span>03</span><h3>Aceite y agua aparte</h3><p>No frías en el aceite donde se hizo algo rebozado ni hiervas fideos aptos en el agua de los comunes.</p></div>
</div>
<h2>Antes de cocinar</h2>
{checks(["<b>Lavate las manos</b> antes de empezar y después de tocar algo con gluten.",
         "<b>Limpiá la mesada</b> con un trapo o esponja propios.",
         "<b>Separá lo ya preparado</b> Sin TACC: tapado y lejos de harinas y pan.",
         "<b>Licuadora, procesadora y mixer:</b> si no se pueden desarmar y lavar bien, conviene que sean solo para lo Sin TACC."])}
<h2>Si en tu casa se come con gluten</h2>
{checks(["Un estante de la alacena y otro de la heladera solo Sin TACC, arriba (para que no caigan migas).",
         "Frascos propios de manteca, dulces y untables: un cuchillo con migas los contamina.",
         "Esponja o repasador aparte para lo Sin TACC.",
         "Rotulá: \"Sin TACC\" en recipientes y viandas.",
         "Si hay dudas sobre algo, no se come."])}
{box("<b>Lo más fácil: que la comida de toda la familia sea Sin TACC.</b> Con la base de alimentos naturales (capítulo 6) es posible y más barato que tener dos menús.", "soft")}
''', chapter="04 · Cocina segura", pid="c4", toc="04 · Cocina segura en casa")

# ================================================================== 05
page(f'''
{chap_head("05", 'Fibra y proteína <span class="t">sin gluten</span>', "Al sacar el trigo y la avena, la fibra suele bajar. Hay que buscarla en otros alimentos.")}
{table(["Fuente", "Fibra", "Proteína"], [
 ["<b>Legumbres</b> (lentejas, garbanzos, porotos)", "✓✓", "✓✓"],
 ["<b>Verduras y frutas con cáscara</b>", "✓✓", ""],
 ["<b>Semillas</b> (chía, lino, girasol, zapallo)", "✓✓", "✓"],
 ["<b>Quinoa, arroz integral, trigo sarraceno</b> (con logo)", "✓", "✓"],
 ["<b>Huevo, carnes, pescado, lácteos</b>", "", "✓✓"],
 ["<b>Frutos secos</b> (envasados con logo)", "✓", "✓"],
])}
{ul(["<b>Sumá fibra de a poco:</b> si de golpe agregás mucha, puede hincharte. Subí de a una porción por semana.",
     "<b>Tomá agua:</b> la fibra necesita líquido. Como referencia general se habla de unos 2 litros de líquidos por día, sobre todo agua; tu necesidad depende de tu actividad, el clima y tu salud.",
     "<b>Proteína en cada comida:</b> huevo, yogur, queso, carne, pescado o legumbres."])}
<p class="small">Como referencia general se recomiendan 20 a 35 g de fibra por día. Tu cantidad la ajusta tu nutricionista.</p>
''', chapter="05 · Fibra y proteína", pid="c5", toc="05 · Fibra y proteína sin gluten")

# ================================================================== 06
page(f'''
{chap_head("06", 'El plato RENOVA <span class="t">Sin TACC</span>', "Una forma simple de armar cualquier comida sin pesar ni contar.")}
<div class="cols2 keep"><div>
<h2>Almuerzo y cena</h2>
{checks(["<b>Mitad del plato: verduras</b>, crudas o cocidas, de varios colores.",
         "<b>Un cuarto: proteína</b>: carne, pollo, pescado, huevo, legumbres o tofu con logo.",
         "<b>Un cuarto: energía</b>: papa, batata, choclo, arroz, quinoa, polenta o fideos Sin TACC.",
         "<b>Grasa buena:</b> aceite de oliva, palta, semillas o frutos secos."])}
</div><div>
<h2>Desayuno y merienda</h2>
{checks(["<b>Proteína:</b> yogur, queso, huevo o ricota.",
         "<b>Fruta</b> fresca.",
         "<b>Energía (opcional):</b> galletas de arroz, pan Sin TACC, granola de quinoa casera.",
         "<b>Grasa buena:</b> frutos secos, semillas, pasta de maní o palta."])}
</div></div>
<h2>Ideas de desayunos y meriendas</h2>
{ul(["Yogur natural + fruta + granola de quinoa casera (receta en la página <span class=\"pref\" data-ref=\"recetas\"></span>).",
     "2 galletas de arroz + queso + tomate + 1 fruta.",
     "Omelette de 2 huevos + 1 fruta.",
     "Pancake de coco + yogur + frutillas.",
     "Infusión con leche + 1 rodaja de pan Sin TACC con palta y huevo."])}
''', chapter="06 · El plato", pid="c6", toc="06 · El plato RENOVA Sin TACC")

# ================================================================== 07 LISTA DE COMPRAS
GONDOLAS = [
    ("Verdulería", "Naturalmente sin TACC", ["Verduras de hoja: lechuga, espinaca, acelga, rúcula", "Zapallo, calabaza, zanahoria, brócoli, coliflor, zucchini, berenjena, morrón, tomate", "Papa, batata, choclo, cebolla, ajo", "Frutas de estación", "Hierbas frescas"]),
    ("Carnicería y pescadería", "Naturalmente sin TACC (frescos, sin condimentar)", ["Carne vacuna magra, pollo, cerdo magro", "Pescado fresco o congelado al natural", "Evitá: milanesas, hamburguesas y embutidos sin logo"]),
    ("Lácteos y huevos", "Con logo los quesos y yogures", ["Huevos", "Leche y yogur natural con logo", "Quesos con logo: untable, fresco, port salut, ricota"]),
    ("Almacén", "Siempre con logo oficial", ["Arroz (blanco, integral, yamaní), quinoa, polenta", "Fideos y harinas Sin TACC (de arroz, garbanzo, almendras, premezcla)", "Legumbres secas o en lata con logo", "Atún y caballa al natural", "Aceite de oliva, vinagre", "Especias, caldos y salsas con logo (salsa de soja: solo con logo)", "Polvo de hornear y levadura con logo"]),
    ("Desayuno y colaciones", "Siempre con logo oficial", ["Galletas de arroz", "Pan Sin TACC (mejor si tiene semillas o más fibra)", "Frutos secos y semillas envasados", "Pasta de maní", "Cacao amargo"]),
    ("Freezer", "Con logo o al natural", ["Verduras congeladas al natural", "Frutas congeladas", "Pescado al natural"]),
]
gond = table(["Góndola", "Qué comprar"], [[f"<b>{g}</b><br><span class=\"small\">{nota}</span>", " · ".join(items)] for g, nota, items in GONDOLAS])
page(f'''
{chap_head("07", 'Tu lista de compras <span class="t">Sin TACC</span>', "Ordenada por góndola, para hacer la compra de la semana sin pensar.")}
{box("<b>La regla:</b> lo fresco y natural (verdura, fruta, carne, huevo) es apto sin logo. <b>Todo lo envasado, con logo oficial (\"Sin T.A.C.C.\" o \"sin GLUTEN\") y vigente en el listado de ANMAT.</b>", "soft")}
{gond}
<h2>Qué no va al carrito</h2>
{ul(["Productos sueltos o a granel (frutos secos, legumbres, especias) sin rótulo.",
     "Avena o productos con avena que no figuren en el listado de ANMAT.",
     "Envasados sin logo, aunque \"no tengan harina\" en los ingredientes.",
     "Panificados de panaderías comunes."])}
<p class="small">La lista imprimible está en la página <span class="pref" data-ref="imp-lista"></span>.</p>
''', chapter="07 · Lista de compras", pid="c7", toc="07 · Tu lista de compras Sin TACC")

# ================================================================== 08 SEMANA 80/20
page(f'''
{chap_head("08", 'Tu semana <span class="t">80/20</span>', "Planificar la mayoría de las comidas y disfrutar el resto sin culpa.")}
<div class="tips10 t3">
  <div><span>28</span><h3>comidas por semana</h3><p>4 por día (desayuno, almuerzo, merienda y cena) × 7 días.</p></div>
  <div><span>23</span><h3>planificadas</h3><p>Caseras, con el plato RENOVA y la lista de compras.</p></div>
  <div><span>5</span><h3>a elección</h3><p>Una salida, una picada, un postre. <b>Siempre Sin TACC.</b></p></div>
</div>
{box("<b>El 80/20 es sobre organización, nunca sobre el gluten.</b> En celiaquía no hay 20% de permiso: las 28 comidas de la semana son Sin TACC. Lo que cambia en las 5 a elección es que no las planificás ni las cocinás vos.", "note")}
<h2>Cómo organizarte</h2>
{checks(["<b>El fin de semana:</b> elegí el menú (página <span class=\"pref\" data-ref=\"menu\"></span>) y armá la lista.",
         "<b>Un día de cocina (60 a 90 min):</b> una proteína al horno, una olla de legumbres y una bandeja de vegetales asados. Te resuelven 3 o 4 comidas.",
         "<b>Viandas:</b> porcioná y rotulá \"Sin TACC\" con la fecha.",
         "<b>Las 5 a elección las decidís vos:</b> marcalas en el registro (página <span class=\"pref\" data-ref=\"imp-registro\"></span>)."])}
''', chapter="08 · Semana 80/20", pid="c8", toc="08 · Tu semana 80/20")

page(f'''
{eyebrow("SEMANA 80/20")}
<h1 class="h1">Menú de <span class="t">ejemplo</span></h1>
{table(["Día", "Almuerzo", "Cena"], [
 ["Lun", "Ensalada tibia de vegetales, legumbres y pollo", "Omelette de espinaca y queso + ensalada"],
 ["Mar", "Sobras de ensalada tibia + arroz", "Pescado al horno con papas y vegetales"],
 ["Mié", "Batatas rellenas de pollo y queso", "Crema de zapallo con lentejas rojas"],
 ["Jue", "Tortilla de verduras + ensalada", "Pollo con calabaza en una sola fuente"],
 ["Vie", "Arroz + huevo + vegetales asados", "<b>A elección (Sin TACC):</b> salida o pizza Sin TACC"],
 ["Sáb", "Milanesas de berenjena + ensalada", "<b>A elección (Sin TACC):</b> picada con productos aptos"],
 ["Dom", "Asado o almuerzo en familia (carne sin condimentar, ensaladas)", "Crema de zapallo + queso"],
])}
<p class="small">Desayunos y meriendas: elegí de las ideas de la página <span class="pref" data-ref="c6"></span>. En esta semana quedan 3 comidas a elección más, siempre Sin TACC.</p>
''', chapter="08 · Semana 80/20", pid="menu", toc="Menú de ejemplo")

# ================================================================== 09 RECETAS
page(f'''
{chap_head("09", '18 recetas <span class="t">Sin TACC</span>', "Caseras, sin azúcar agregada y con proteína y fibra. Todos los envasados que uses, con logo oficial.")}
{"".join(NUT.ficha(r, i + 1) for i, r in enumerate(RECETAS))}
{box("<b>BORRADOR · Recetas 13 a 18:</b> pizza, empanadas, tarta, pan, ñoquis y budín. Pendientes de validación de la nutricionista y de foto.", "note") if RECETAS_BORRADOR else ""}
{"".join(NUT.ficha(r, len(RECETAS) + i + 1) for i, r in enumerate(RECETAS_BORRADOR))}
''', chapter="09 · Recetas", pid="recetas", toc="09 · 18 recetas Sin TACC")

# ================================================================== 10 COMER AFUERA
page(f'''
{chap_head("10", 'Comer afuera <span class="t">y en reuniones</span>', "Tus comidas a elección también tienen que ser 100% seguras.")}
{checks(["<b>Restaurantes:</b> elegí lugares con menú Sin TACC y preguntá cómo lo cocinan (aceite, plancha, horno aparte).",
         "<b>Pedí simple:</b> carne o pescado a la plancha con ensalada o papas hervidas es más seguro que algo rebozado o con salsa.",
         "<b>En una casa:</b> avisá antes y ofrecé llevar un plato tuyo para compartir.",
         "<b>Asado:</b> carne sin condimentar y achuras con dudas, afuera. Ojo con la parrilla donde se tostó pan.",
         "<b>Llevá algo en la cartera:</b> frutos secos o galletas de arroz con logo, para no quedarte sin opción."])}
{box("<b>Si no estás segura, no lo comas.</b> Una comida que te salteás no arruina tu semana; una contaminación sí te puede hacer mal.", "note")}
''', chapter="10 · Comer afuera", pid="c10", toc="10 · Comer afuera y en reuniones")

# ================================================================== BONUS SKOOL
page(f'''
{eyebrow("BONUS · INCLUIDO")}
<h1 class="h1 big">Talleres y <span class="t">comunidad RENOVA</span></h1>
<p class="lead">Con esta guía tenés acceso a los talleres del equipo RENOVA en Skool. Empezá por <b>"Elecciones inteligentes en el súper"</b>, el taller de Eugenia sobre cómo leer etiquetas.</p>
<div class="tk10"><div class="tk10-im"><img src="img/taller_super.png" alt=""><img src="img/taller_ansiedad.png" alt=""></div><div class="tk10-tx"><span class="wtag">TALLERES</span><h3>Nutrición, hábitos, ansiedad y mucho más</h3><p>Dictados por los profesionales del equipo RENOVA.</p></div></div>
<p><b>Con el mismo acceso entrás a la comunidad RENOVA:</b> mujeres con tus mismos objetivos. Participar es opcional.</p>
<a class="skool" href="{esc(LINK_SKOOL)}">
  <img src="img/equipo_cover.jpg" alt="Equipo RENOVA">
  <div class="skx"><span class="wtag">COMUNIDAD RENOVA · SKOOL</span><h3>Entrá a los talleres y a la comunidad</h3>
  <p>Tocá el botón: se abre la comunidad RENOVA en Skool, con los cursos y talleres del equipo.</p>
  <span class="btn btn-big">{ICON_ARROW} ENTRAR A SKOOL</span></div>
</a>
''', chapter="Bonus · Talleres", pid="talleres", cls="p-spread", toc="Bonus: talleres y comunidad")

# ================================================================== IMPRIMIBLES
IMP = [("Verdulería", ["Hojas verdes", "Zapallo / calabaza", "Zanahoria", "Brócoli / coliflor", "Zucchini / berenjena", "Tomate / morrón", "Papa / batata / choclo", "Cebolla / ajo", "Frutas"]),
       ("Carnes y pescado", ["Carne magra", "Pollo", "Pescado", "____________"]),
       ("Lácteos y huevos", ["Huevos", "Yogur natural (logo)", "Queso (logo)", "Leche (logo)"]),
       ("Almacén (con logo)", ["Arroz / quinoa / polenta", "Fideos o harina Sin TACC", "Legumbres", "Atún / caballa", "Aceite de oliva", "Especias y caldos", "Polvo de hornear"]),
       ("Desayuno (con logo)", ["Galletas de arroz", "Pan Sin TACC", "Frutos secos / semillas", "Pasta de maní", "Cacao amargo"]),
       ("Freezer", ["Verduras congeladas", "Frutas congeladas", "____________"])]
def _bloques(grupo):
    return "".join(f'<div class="esen"><h3>{g}</h3><p>{"<br>".join("☐ " + i for i in items)}</p></div>' for g, items in grupo)
page(f'''
{eyebrow("IMPRIMIBLE")}
<h1 class="h1">Lista de compras <span class="t">de la semana</span></h1>
<div class="cols2 keep"><div>{_bloques(IMP[:3])}</div><div>{_bloques(IMP[3:])}</div></div>
''', chapter="Imprimibles", pid="imp-lista", toc="Imprimible: lista de compras")

page(f'''
{eyebrow("IMPRIMIBLE")}
<h1 class="h1">Registro <span class="t">semanal 80/20</span></h1>
<p class="small">Marcá con una cruz tus comidas a elección (siempre Sin TACC). Objetivo: 23 planificadas y hasta 5 a elección. Semana N°: ______</p>
{table(["", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"], [[m] + [""] * 7 for m in ["Desayuno", "Almuerzo", "Merienda", "Cena"]])}
<h2>Organización de la semana</h2>
<p class="small">Completalo el día de cocina y revisalo antes de la próxima compra.</p>
{table(["Lo que dejé preparado", "Para cuántas comidas", "Lo que falta reponer", "Receta para repetir"], [["", "", "", ""] for _ in range(6)])}
''', chapter="Imprimibles", pid="imp-registro", toc="Imprimible: registro 80/20 y organización")

# ================================================================== CIERRE
page(f'''
<div class="bio metodo">
  {eyebrow("CONSULTA NUTRICIONAL RENOVA")}
  <h1 class="h1 big">Tu plan Sin TACC <span class="t">con {NUTRI.split()[0]} {NUTRI.split()[1]}</span></h1>
  <div class="nutri-card"><img src="img/eugenia.jpg" alt="{NUTRI}"><div><span class="pill">CONSULTA INDIVIDUAL</span><h3>Lic. {NUTRI}</h3><p class="nc-t">Lic. en Nutrición · {MATRICULA} · Equipo RENOVA</p>
  <p>Esta guía te organiza la semana. En una consulta armamos tu plan Sin TACC según tus gustos, tus horarios, tu familia y tus objetivos.</p></div></div>
  <div class="cp-pills"><span>✓ Plan Sin TACC a tu medida</span><span>✓ Compras y menú para tu casa</span><span>✓ Seguimiento</span></div>
  <p class="center"><b>Escribinos y coordinamos tu consulta.</b> Contanos tu caso.</p>
  <div class="cta-center"><a class="btn btn-big" href="{esc(LINK_PLAN)}">QUIERO MI CONSULTA {ICON_ARROW}</a></div>
  <p class="center small">¿Querés sumar entrenamiento de fuerza? También podés pedir el <b>plan integral RENOVA 1 a 1 con Nacho</b> (nutrición + entrenamiento) desde el mismo botón.</p>
  <div class="quote dark">Comer Sin TACC no es una limitación. <span class="t2">Es tu forma de cuidarte.</span></div>
</div>
''', chapter="Consulta nutricional", pid="metodo", toc="Tu consulta nutricional Sin TACC")


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
            hdr = (f'<div class="hdr"><span>SIN TACC INTELIGENTE · <b>RENOVA</b></span><span>{esc(p["chapter"])}</span></div>'
                   f'<div class="ftr"><a class="toidx" href="#indice">{ICON_HAND} Hacé clic y volvé al índice</a><span class="pgnum"></span></div>')
        out.append(f'<section class="page {p["cls"]}" id="{p["id"]}">{hdr}<div class="body">{body}</div></section>')
    css = ds_css(HERE) + "\n" + open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Sin TACC Inteligente · RENOVA</title>'
            f'<style>{css}</style></head><body class="grande">' + "".join(out) + '<script src="paginate.js"></script></body></html>')


if __name__ == "__main__":
    with open(os.path.join(HERE, "sintacc.html"), "w", encoding="utf-8") as f:
        f.write(render())
    print("sintacc.html ·", len(PAGES), "páginas antes de paginar")
