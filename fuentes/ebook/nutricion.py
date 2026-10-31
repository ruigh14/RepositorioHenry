"""Ebook "Alimentación Inteligente" (plan de nutrición de 8 semanas de RENOVA).

Basado en el borrador de la nutricionista (Eugenia) y en el brief editorial: educación breve y visual,
organización de la semana y un programa práctico de 8 semanas con 32 recetas (4 por semana).
Usa el mismo diseño que los ebooks de entrenamiento (style.css + paginate.js).

Uso:  cd fuentes/ebook && python3 nutricion.py && node export.js nutricion
      → alimentacion-inteligente/Ebook_Alimentacion_Inteligente_RENOVA.pdf
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "design-system"))
from design_system import css as ds_css, esc, ICON_ARROW, ICON_HAND, eyebrow, chap_head, ul, checks, box

NUTRI = "María Eugenia Ballini"
NUTRI_TITULO = "Lic. en Nutrición"
MATRICULA = "M.N. 11773"
LINK_PLAN = "https://wa.link/1asjt1"   # WhatsApp de Nacho: plan integral personalizado 1 a 1

PAGES, TOC = [], []


def page(body, chapter="", pid=None, cls="", toc=None, header=True):
    pid = pid or f"p{len(PAGES) + 1}"
    PAGES.append(dict(id=pid, chapter=chapter, body=body, cls=cls, header=header))
    if toc:
        TOC.append((toc, pid))


def table(head, rows, cls="grid-t ntab"):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def esencial(items, accion):
    return (f'<div class="esen"><h3>Lo esencial</h3>{checks(items)}</div>'
            f'<p class="accion"><b>Acción de hoy:</b> {accion}</p>')


# ================================================================== RECETAS (4 por semana)
# foto = número de img/food/NN.jpg (o "yogur"); None = sin foto (ficha compacta)
def rec(t, cat, tiempo, porc, ing, pasos, cambio, conserva="", foto=None):
    return dict(t=t, cat=cat, tiempo=tiempo, porc=porc, ing=ing, pasos=pasos, cambio=cambio, conserva=conserva, foto=foto)


SEMANAS = [
 dict(n=1, titulo='Aprendé a armar <span class="t">tu plato</span>',
  objetivo="Combinar alimentos para armar comidas completas: proteína, vegetales y una fuente de energía en cada plato.",
  recetas=[
   rec("Bowl de yogur, avena y fruta", "Desayuno o merienda", "5 min", "1 porción",
       ["1 pote de yogur natural (190 g)", "3 cdas de avena", "1 fruta picada (banana, manzana o frutillas)", "1 cda de semillas o nueces picadas", "Canela a gusto"],
       ["Poné el yogur en un bowl.", "Sumá la avena y la fruta.", "Terminá con semillas o nueces y canela."],
       "yogur griego para más proteína; queso untable con tostadas si preferís salado.", "armalo en el momento.", foto="yogur"),
   rec("Ensalada tibia de vegetales, legumbres y pollo", "Almuerzo o vianda", "25 min", "2 porciones",
       ["1 pechuga de pollo en cubos", "1 taza de garbanzos o lentejas cocidos", "2 tazas de vegetales en cubos (zapallo, zanahoria, brócoli)", "Hojas verdes", "1 cda de aceite de oliva, limón, sal y pimienta"],
       ["Asá los vegetales en el horno o la sartén hasta que estén tiernos.", "Cociná el pollo hasta que no quede rosado en el centro.", "Mezclá con las legumbres y las hojas, y condimentá al servir."],
       "pollo por atún, huevo duro o más legumbres.", "2 a 3 días en heladera, con el aderezo aparte.", foto=11),
   rec("Pescado al horno con papas y vegetales", "Cena", "35 min", "2 porciones",
       ["2 filetes de merluza o el pescado que consigas", "2 papas medianas en rodajas finas", "1 zucchini y 1 morrón en tiras", "1 cda de aceite, limón, ajo y perejil"],
       ["Horneá las papas con el aceite 15 minutos en horno medio-alto.", "Sumá los vegetales y el pescado con limón, ajo y perejil.", "Horneá 12 a 15 minutos más, hasta que el pescado se separe en láminas."],
       "pescado por pollo (cocción más larga); papa por batata.", "1 a 2 días en heladera."),
   rec("Tostadas con queso, huevo y tomate", "Desayuno salado", "10 min", "1 porción",
       ["2 rebanadas de pan integral", "2 cdas de queso untable", "1 huevo", "1 tomate en rodajas", "Orégano"],
       ["Tostá el pan y untá el queso.", "Cociná el huevo a la plancha, duro o revuelto, bien cocido.", "Armá con el tomate y el orégano."],
       "huevo por queso fresco o atún; pan por galletas de arroz."),
  ],
  dias=[("Ensalada tibia (receta 2)", "Pescado al horno (receta 3)"), ("Sobrante de pescado + ensalada", "Tortilla simple + vegetales"),
        ("Ensalada tibia", "Carne magra + puré de zapallo"), ("Milanesa al horno + ensalada", "Sobras recalentadas + vegetales"),
        ("Arroz + huevo + vegetales", "Pescado al horno"), ("Comida libre en familia", "Tostadas completas (receta 4)"),
        ("Asado o almuerzo social", "Sopa de verduras + queso")],
  orga=["Cociná una fuente de proteína para dos comidas.", "Lavá y dejá listas las hojas verdes.", "Hacé una bandeja de vegetales para usar en 2 o 3 platos."],
  compras=["Pollo, merluza, huevos", "Yogur natural, queso untable", "Garbanzos o lentejas", "Papas, zapallo, zucchini, morrón, brócoli, tomates, hojas", "Frutas de estación", "Avena, pan integral, semillas"],
  aprendizaje="No necesitás comer siempre lo mismo: necesitás aprender a combinar."),
 dict(n=2, titulo='Más <span class="t">proteína</span> en cada comida',
  objetivo="Sumar una fuente de proteína en desayuno, almuerzo, merienda y cena, variando entre animales y vegetales.",
  recetas=[
   rec("Pancake de avena", "Desayuno o merienda", "10 min", "1 porción",
       ["1 huevo", "3 cdas de avena", "1 cda de leche o bebida vegetal", "1 cdita de polvo de hornear", "Esencia de vainilla"],
       ["Mezclá todo en un bowl.", "Volcá en sartén antiadherente a fuego bajo.", "Cuando aparezcan burbujas, dalo vuelta y cociná del otro lado."],
       "sumá yogur o queso untable arriba para más proteína.", foto=1),
   rec("Omelette de espinaca y queso", "Cena rápida", "10 min", "1 porción",
       ["2 huevos", "1 puñado de espinaca o acelga", "1 feta o 30 g de queso", "Sal, pimienta y nuez moscada"],
       ["Saltéa la espinaca 1 minuto.", "Batí los huevos, volcalos en la sartén y sumá la espinaca y el queso.", "Doblá y cociná hasta que el huevo esté firme."],
       "espinaca por champiñones o tomate; acompañá con pan o una papa."),
   rec("Wok de verduras con arroz y pollo", "Almuerzo o vianda", "30 min", "2 porciones",
       ["1 pechuga de pollo en tiras", "1 taza de arroz cocido", "2 tazas de verduras en tiras (morrón, zanahoria, cebolla, zucchini)", "1 cda de aceite y 1 cda de salsa de soja"],
       ["Saltéa el pollo hasta que esté bien cocido.", "Sumá las verduras y cociná a fuego fuerte 5 minutos.", "Agregá el arroz y la salsa de soja, y mezclá."],
       "pollo por carne, langostinos o tofu.", "2 a 3 días en heladera.", foto=15),
   rec("Albóndigas en salsa de tomate", "Cena o vianda", "35 min", "3 porciones",
       ["400 g de carne picada magra", "1 huevo", "2 cdas de avena o pan rallado", "Ajo, perejil y sal", "1 lata de tomate triturado y cebolla"],
       ["Mezclá la carne con huevo, avena y condimentos, y formá bolitas.", "Rehogá la cebolla, sumá el tomate y llevá a hervor.", "Cociná las albóndigas en la salsa 20 minutos, hasta que estén cocidas por dentro."],
       "carne por pollo picado; servilas con arroz, fideos o puré.", "3 días en heladera o 3 meses en freezer."),
  ],
  dias=[("Wok de pollo (receta 3)", "Omelette + ensalada"), ("Albóndigas + arroz", "Sobras del wok"),
        ("Ensalada con atún y huevo", "Albóndigas + puré"), ("Albóndigas (freezer)", "Pescado + vegetales"),
        ("Legumbres + vegetales asados", "Omelette (receta 2)"), ("Almuerzo libre", "Tarta de verduras"),
        ("Pollo al horno + ensalada", "Sopa + queso")],
  orga=["Hacé doble porción de albóndigas y congelá la mitad.", "Tené huevos y yogur siempre en la heladera.", "Sumá una lata de atún o de legumbres a la alacena."],
  compras=["Huevos, pollo, carne picada magra, atún", "Yogur, queso", "Arroz, avena", "Espinaca, morrón, zanahoria, zucchini, cebolla", "Tomate triturado, salsa de soja"],
  aprendizaje="La proteína rinde más repartida en todas las comidas que concentrada en la cena."),
 dict(n=3, titulo='Más <span class="t">vegetales y fibra</span>',
  objetivo="Llegar a vegetales en almuerzo y cena, sumar legumbres 2 o 3 veces y frutas todos los días.",
  recetas=[
   rec("Porridge de avena", "Desayuno", "10 min", "1 porción",
       ["¼ taza de avena", "1 taza de leche o bebida vegetal", "Canela y vainilla", "Fruta y semillas para servir"],
       ["Cociná la avena con la leche a fuego bajo 5 minutos, revolviendo.", "Perfumá con canela y vainilla.", "Serví con fruta y semillas."],
       "sumá 1 cda de pasta de maní o yogur para más proteína.", foto=3),
   rec("Ensalada completa de garbanzos", "Almuerzo o vianda", "15 min", "2 porciones",
       ["1 taza y ½ de garbanzos cocidos", "1 tomate, ½ pepino y ½ cebolla morada", "1 huevo duro o 60 g de queso fresco en cubos", "Perejil, limón, aceite de oliva y comino"],
       ["Cortá los vegetales en cubos chicos.", "Mezclá con los garbanzos y el huevo o queso.", "Condimentá al servir."],
       "garbanzos por lentejas o porotos.", "2 días en heladera, sin condimentar."),
   rec("Budín de brócoli", "Almuerzo o cena", "45 min", "3 porciones",
       ["1 brócoli grande hervido y picado", "3 huevos", "½ taza de queso rallado o en cubos", "Cebolla rehogada, sal y nuez moscada"],
       ["Mezclá el brócoli con la cebolla, los huevos y el queso.", "Volcá en un molde aceitado.", "Horneá 30 minutos en horno medio, hasta que esté firme."],
       "brócoli por espinaca, acelga o zapallitos.", "3 días en heladera.", foto=13),
   rec("Crema de zapallo con lentejas rojas", "Cena", "30 min", "3 porciones",
       ["500 g de zapallo en cubos", "½ taza de lentejas rojas", "1 cebolla", "Caldo casero o agua, sal y comino"],
       ["Rehogá la cebolla, sumá el zapallo, las lentejas y líquido hasta cubrir.", "Cociná 20 minutos, hasta que todo esté tierno.", "Procesá y ajustá la sal. Serví con semillas o queso."],
       "lentejas rojas por porotos blancos cocidos.", "3 días en heladera o 3 meses en freezer."),
  ],
  dias=[("Ensalada de garbanzos (receta 2)", "Crema de zapallo (receta 4)"), ("Budín de brócoli + ensalada", "Pollo + vegetales asados"),
        ("Ensalada de garbanzos", "Budín de brócoli"), ("Carne + ensalada de colores", "Crema de zapallo + huevo"),
        ("Legumbres + arroz + vegetales", "Pescado + vegetales al vapor"), ("Almuerzo libre", "Tortilla de verduras"),
        ("Pastas + salsa de verduras", "Crema de zapallo (freezer)")],
  orga=["Cociná una olla de legumbres o usá de lata enjuagadas.", "Elegí 3 colores de verduras para la semana.", "Sumá la fibra de a poco y tomá más agua."],
  compras=["Garbanzos, lentejas rojas", "Huevos, queso, pollo, pescado", "Zapallo, brócoli, tomate, pepino, cebolla morada, hojas", "Frutas variadas", "Avena, semillas"],
  aprendizaje="Más fibra, de a poco y con agua: así la panza la tolera mejor."),
 dict(n=4, titulo='Carbohidratos y <span class="t">energía</span>',
  objetivo="Incluir carbohidratos de calidad sin miedo: son energía para el día y para entrenar.",
  recetas=[
   rec("Granola casera", "Desayuno o merienda", "30 min", "Aprox. 8 porciones",
       ["2 tazas de avena", "½ taza de frutos secos picados", "2 cdas de semillas", "2 cdas de miel", "1 cda de aceite y canela"],
       ["Mezclá todo en una placa.", "Horneá a temperatura baja 20 minutos, revolviendo a mitad de cocción.", "Dejá enfriar antes de guardar."],
       "miel por puré de banana.", "2 semanas en frasco cerrado.", foto=7),
   rec("Fideos integrales con atún y vegetales", "Almuerzo o vianda", "20 min", "2 porciones",
       ["160 g de fideos integrales", "1 lata de atún al natural", "1 zucchini y 10 tomates cherry", "Ajo, aceite de oliva y albahaca"],
       ["Herví los fideos según el paquete.", "Saltéa el ajo, el zucchini y los tomates.", "Sumá el atún y los fideos, y mezclá."],
       "atún por pollo desmenuzado o garbanzos.", "2 días en heladera."),
   rec("Pastel veggie de lentejas", "Almuerzo o cena", "1 h", "4 porciones",
       ["1 taza de lentejas cocidas", "1 cebolla, 1 zanahoria y 1 morrón picados", "Tomate triturado", "4 papas o batatas para el puré", "Queso rallado"],
       ["Rehogá las verduras, sumá las lentejas y el tomate, y cociná 10 minutos.", "Hacé un puré con las papas.", "Armá en una fuente: lentejas abajo, puré arriba y queso. Gratiná 15 minutos."],
       "lentejas por carne picada magra.", "3 días en heladera o 3 meses en freezer.", foto=17),
   rec("Batatas rellenas de pollo y queso", "Cena", "45 min", "2 porciones",
       ["2 batatas medianas", "1 taza de pollo cocido desmenuzado", "2 cdas de queso untable", "Cebolla de verdeo y pimentón"],
       ["Horneá las batatas pinchadas 35 a 40 minutos, hasta que estén tiernas.", "Abrilas y mezclá la pulpa con el pollo, el queso y la cebolla de verdeo.", "Rellená y gratiná 5 minutos."],
       "pollo por atún o porotos negros.", "2 días en heladera."),
  ],
  dias=[("Fideos con atún (receta 2)", "Batatas rellenas (receta 4)"), ("Pastel de lentejas", "Omelette + pan"),
        ("Arroz + pollo + vegetales", "Pastel de lentejas"), ("Fideos con atún", "Pescado + papas"),
        ("Pastel de lentejas (freezer)", "Batatas rellenas"), ("Almuerzo libre", "Pizza casera + ensalada"),
        ("Asado o almuerzo social", "Sopa + tostadas")],
  orga=["Cociná batatas o papas de más para otra comida.", "Hacé la granola el fin de semana.", "Tené fideos y arroz para resolver en 15 minutos."],
  compras=["Pollo, atún, huevos, pescado", "Queso untable, queso rallado", "Fideos integrales, arroz, avena", "Batatas, papas, zucchini, tomates cherry, cebolla, zanahoria, morrón", "Lentejas, frutos secos, semillas"],
  aprendizaje="No hay que eliminar los carbohidratos: hay que elegirlos y acompañarlos bien."),
 dict(n=5, titulo='Cocinar con <span class="t">poco tiempo</span>',
  objetivo="Resolver comidas en 10 a 20 minutos con ingredientes de heladera, freezer y alacena.",
  recetas=[
   rec("Huevos revueltos con palta y tostada", "Desayuno", "8 min", "1 porción",
       ["2 huevos", "¼ palta", "1 rebanada de pan integral", "Tomate, sal y pimienta"],
       ["Revolvé los huevos a fuego bajo hasta que estén bien cocidos.", "Tostá el pan y pisá la palta encima.", "Serví con el tomate."],
       "palta por queso untable; pan por una fruta."),
   rec("Tortilla de verduras en sartén", "Almuerzo o cena", "20 min", "2 porciones",
       ["4 huevos", "2 tazas de verduras congeladas o picadas", "1 cebolla", "Sal, pimienta y orégano"],
       ["Saltéa la cebolla y las verduras.", "Volcá los huevos batidos y cociná tapado a fuego bajo.", "Dala vuelta con un plato y cociná 2 minutos más."],
       "sumá papa hervida o queso; verduras de lata escurridas.", "2 días en heladera."),
   rec("Milanesas de berenjena", "Almuerzo o cena", "30 min", "2 porciones",
       ["1 berenjena grande en rodajas", "2 huevos batidos", "Pan rallado o avena con orégano", "Queso y tomate para napolitana (opcional)"],
       ["Pasá las rodajas por huevo y por el rebozador.", "Horneá en placa aceitada 20 minutos, dando vuelta a mitad.", "Si querés, sumá tomate y queso y gratiná."],
       "berenjena por zucchini; acompañá con una proteína.", "2 días en heladera o congeladas crudas.", foto=18),
   rec("Wrap de pollo y vegetales", "Almuerzo para llevar", "10 min", "1 porción",
       ["1 rapidita o tortilla integral", "½ taza de pollo cocido", "Hojas verdes, zanahoria rallada y tomate", "1 cda de queso untable o hummus"],
       ["Untá la tortilla con el queso o el hummus.", "Sumá el pollo y los vegetales.", "Enrollá apretando y cortá al medio."],
       "pollo por atún o huevo duro.", "llevalo con bolsa térmica y comelo en el día."),
  ],
  dias=[("Wrap de pollo (receta 4)", "Tortilla de verduras (receta 2)"), ("Sobrante de tortilla + ensalada", "Milanesas de berenjena + huevo"),
        ("Wrap de atún", "Fideos rápidos con verduras"), ("Arroz + huevo + vegetales congelados", "Milanesas de berenjena"),
        ("Ensalada de lata: atún, choclo y arvejas", "Tortilla de verduras"), ("Almuerzo libre", "Huevos revueltos + pan"),
        ("Pollo al horno", "Sopa + queso")],
  orga=["Armá tu alacena de emergencia: atún, legumbres, choclo, arvejas, tomate.", "Tené verduras congeladas para una tortilla.", "Dejá pollo cocido para wraps y ensaladas."],
  compras=["Huevos, pollo, atún", "Queso untable, queso", "Tortillas o rapiditas integrales, pan integral", "Berenjena, palta, tomate, hojas, zanahoria", "Verduras congeladas, choclo y arvejas en lata"],
  aprendizaje="Con 5 ingredientes de emergencia, una comida completa sale en 15 minutos."),
 dict(n=6, titulo='Organización y <span class="t">meal prep</span>',
  objetivo="Preparar bases en 60 a 90 minutos y combinarlas durante la semana.",
  recetas=[
   rec("Base: pollo al horno desmenuzado", "Base de proteína", "40 min", "4 a 5 usos",
       ["1 kg de pechuga o muslos de pollo", "Ajo, pimentón, limón y sal", "1 cda de aceite"],
       ["Condimentá el pollo y horneá en una fuente 35 minutos, hasta que no quede rosado.", "Dejá entibiar y desmenuzá.", "Porcioná en recipientes y rotulá."],
       "pollo por carne magra al horno.", "3 días en heladera o 3 meses en freezer."),
   rec("Base: legumbres cocidas", "Base de proteína vegetal", "1 h + remojo", "6 a 8 usos",
       ["500 g de garbanzos, porotos o lentejas", "Agua y 1 hoja de laurel"],
       ["Remojá garbanzos o porotos de 8 a 12 horas (las lentejas no hace falta).", "Cociná en agua nueva hasta que estén tiernas: lentejas 25 min, garbanzos y porotos 1 h o más.", "Escurrí, enfriá y porcioná."],
       "legumbres de lata, enjuagadas.", "3 días en heladera o 3 meses en freezer."),
   rec("Base: bandeja de vegetales asados", "Base de vegetales", "40 min", "4 usos",
       ["1 kg de vegetales (zapallo, zanahoria, cebolla, morrón, brócoli)", "1 cda de aceite", "Sal y especias"],
       ["Cortá en trozos parecidos y distribuí en una sola capa.", "Horneá 30 a 35 minutos en horno medio-alto.", "Dividí en recipientes y condimentá distinto al servir."],
       "cualquier verdura de estación.", "3 a 4 días en heladera."),
   rec("Hummus de garbanzos", "Merienda o para untar", "10 min", "4 porciones",
       ["1 taza y ½ de garbanzos cocidos", "1 cda de pasta de sésamo (tahini) o semillas de sésamo", "Jugo de ½ limón, ajo, comino y sal", "Agua fría"],
       ["Procesá todo, sumando agua de a poco.", "Ajustá sal y limón.", "Serví con bastones de vegetales o tostadas."],
       "garbanzos por porotos blancos.", "3 a 4 días en heladera.", foto=10),
  ],
  dias=[("Pollo + legumbres + vegetales asados", "Wrap de pollo + hummus"), ("Ensalada de legumbres + huevo", "Pollo + vegetales + arroz"),
        ("Bowl de legumbres y vegetales", "Tortilla con vegetales asados"), ("Pollo + ensalada", "Sopa con legumbres"),
        ("Bowl libre con las bases", "Pescado + vegetales asados"), ("Almuerzo libre", "Tostadas con hummus y huevo"),
        ("Asado o almuerzo social", "Bases que sobraron")],
  orga=["Reservá 60 a 90 minutos un día de la semana.", "Prepará primero lo que tarda más (horno y legumbres).", "Rotulá con nombre y fecha; congelá lo que no uses en 3 días."],
  compras=["Pollo (1 kg), huevos, pescado", "Legumbres secas o en lata", "Zapallo, zanahoria, cebolla, morrón, brócoli, hojas", "Limón, ajo, especias, tahini o sésamo", "Arroz, pan integral"],
  aprendizaje="Preparar componentes rinde más que preparar platos idénticos."),
 dict(n=7, titulo='Flexibilidad y <span class="t">vida social</span>',
  objetivo="Sostener tus hábitos con reuniones, salidas, delivery y viajes, sin compensar ni prohibirte nada.",
  recetas=[
   rec("Talitas de garbanzos", "Snack para llevar", "35 min", "1 placa", ["1 taza de harina de garbanzos", "1 taza de agua", "1 cda de aceite", "Sal, pimienta y romero"],
       ["Mezclá la harina con el agua y dejá reposar 10 minutos.", "Volcá en una placa aceitada en capa fina.", "Horneá 20 minutos en horno medio-alto y cortá en bastones."],
       "sumá semillas o especias.", "4 días en recipiente cerrado.", foto=9),
   rec("Croquetas de zucchini", "Para compartir", "35 min", "2 a 3 porciones",
       ["2 zucchinis rallados y escurridos", "1 huevo", "½ taza de queso rallado", "3 cdas de avena", "Ajo y perejil"],
       ["Escurrí bien el zucchini apretándolo con un repasador.", "Mezclá con el resto y formá croquetas.", "Horneá 20 minutos en placa aceitada, dando vuelta a mitad."],
       "zucchini por zanahoria o calabaza rallada.", "2 días en heladera.", foto=16),
   rec("Bowl de atún, arroz y palta", "Almuerzo o vianda", "15 min", "1 porción",
       ["½ taza de arroz cocido", "1 lata chica de atún al natural", "¼ palta", "Pepino, zanahoria rallada y choclo", "Limón y salsa de soja"],
       ["Poné el arroz en la base.", "Sumá el atún y los vegetales.", "Terminá con la palta, el limón y la soja."],
       "atún por salmón cocido, pollo o huevo."),
   rec("Cheesecake en taza", "Postre", "5 min", "1 porción",
       ["2 cdas de queso untable", "1 huevo", "1 cda de yogur", "Esencia de vainilla y endulzante a gusto", "Galletitas de avena trituradas para la base (opcional)"],
       ["Mezclá queso, huevo, yogur y vainilla.", "Volcá en una taza apta para microondas.", "Cociná 1 a 2 minutos, hasta que esté firme. Dejá enfriar."],
       "sumá frutos rojos arriba.", "1 día en heladera.", foto=23),
  ],
  dias=[("Bowl de atún (receta 3)", "Cena con amigas: elegí proteína + vegetales"), ("Vianda de bases", "Croquetas + ensalada + huevo"),
        ("Menú del día: plancha + ensalada", "Sopa casera"), ("Bowl de atún", "Delivery: pedí una opción con proteína y vegetales"),
        ("Viaje: talitas + fruta + yogur", "Comida simple con lo que haya"), ("Asado o reunión", "Cena liviana: tostadas + queso + fruta"),
        ("Almuerzo libre", "Cheesecake en taza de postre")],
  orga=["Mirá la carta antes de ir y elegí con calma.", "En reuniones, servite un plato y disfrutalo sin culpa.", "En viajes, llevá un snack: talitas, frutos secos, fruta o yogur."],
  compras=["Atún, huevos, queso untable, yogur", "Harina de garbanzos, avena, arroz", "Zucchini, palta, pepino, zanahoria, choclo", "Frutas fáciles de llevar"],
  aprendizaje="Una comida diferente no arruina la semana: volvé a tu estructura en la siguiente."),
 dict(n=8, titulo='Autonomía y <span class="t">continuidad</span>',
  objetivo="Armar tu propia semana combinando lo aprendido, sin depender de un menú cerrado.",
  recetas=[
   rec("Barritas de avena caseras", "Merienda", "35 min + enfriado", "8 barritas",
       ["2 tazas de avena", "2 bananas maduras pisadas", "2 cdas de pasta de maní", "Semillas o frutos secos picados", "Canela"],
       ["Mezclá todo hasta integrar.", "Estirá en un molde con papel manteca, de 1 cm de alto.", "Horneá 20 a 25 minutos, dejá enfriar y cortá."],
       "pasta de maní por miel; sumá chips de chocolate amargo.", "5 días en heladera.", foto=5),
   rec("Tarta de verduras con masa de avena", "Almuerzo o cena", "50 min", "4 porciones",
       ["Masa: 1 taza de avena, 1 huevo, 3 cdas de agua y sal", "Relleno: 1 atado de acelga o espinaca, 1 cebolla", "2 huevos y ½ taza de queso"],
       ["Mezclá la masa, estirala en un molde y precocinala 10 minutos.", "Rehogá la cebolla y la verdura, y mezclá con huevos y queso.", "Rellená y horneá 25 a 30 minutos."],
       "acelga por zapallitos o calabaza.", "3 días en heladera.", foto=12),
   rec("Pollo con calabaza en una sola fuente", "Cena", "45 min", "3 porciones",
       ["3 muslos o 2 pechugas de pollo", "½ calabaza en cubos", "1 cebolla morada", "Romero, ajo, aceite y limón"],
       ["Poné todo en una fuente con los condimentos.", "Horneá 35 a 40 minutos, dando vuelta a mitad.", "Verificá que el pollo no quede rosado en el centro."],
       "calabaza por papa o batata.", "3 días en heladera."),
   rec("Puré de coliflor con merluza", "Cena", "25 min", "2 porciones",
       ["½ coliflor en ramitos", "1 papa chica", "2 filetes de merluza", "Leche, nuez moscada, sal y limón"],
       ["Herví la coliflor y la papa hasta que estén tiernas, y hacé un puré con un chorrito de leche.", "Cociná la merluza a la plancha con limón.", "Serví juntos."],
       "merluza por huevo, pollo o lentejas.", "2 días en heladera.", foto=14),
  ],
  dias=[("Armado propio", "Armado propio"), ("Armado propio", "Armado propio"), ("Armado propio", "Armado propio"), ("Armado propio", "Armado propio"),
        ("Armado propio", "Armado propio"), ("Almuerzo libre", "Armado propio"), ("Asado o almuerzo social", "Armado propio")],
  orga=["Elegí tus 4 recetas favoritas de las 8 semanas.", "Completá el planificador del final con tu agenda real.", "Repetí lo que te funcionó: no hace falta innovar cada semana."],
  compras=["Armá tu lista con la plantilla del final", "Base fija: huevos, legumbres, yogur, avena, verduras de estación, una proteína para cocinar", "Sumá lo que pidan tus 4 recetas"],
  aprendizaje="El objetivo no es seguir un menú: es saber armarlo vos."),
]
assert sum(len(s["recetas"]) for s in SEMANAS) == 32


def ficha(r, n):
    img = ""
    if r["foto"] is not None:
        f = f"img/{r['foto']}.jpg" if str(r["foto"]).startswith("eve/") else (f"img/food/{r['foto']}.jpg" if isinstance(r["foto"], str) else f"img/food/{r['foto']:02d}.jpg")
        img = f'<div class="nr-img"><img src="{f}" alt="{esc(r["t"])}"></div>'
    ing = "".join(f"<li>{i}</li>" for i in r["ing"])
    pas = "".join(f"<li>{p}</li>" for p in r["pasos"])
    cons = f'<p class="nr-x"><b>Conservación:</b> {r["conserva"]}</p>' if r["conserva"] else ""
    return (f'<article class="nrec{" con-img" if img else ""}">{img}<div class="nr-tx">'
            f'<div class="nr-h"><span class="nr-n">{n:02d}</span><div><span class="nr-cat">{r["cat"].upper()}</span><h3>{r["t"]}</h3>'
            f'<p class="nr-meta">{r["tiempo"]} · {r["porc"]}</p></div></div>'
            f'<div class="nr-cols"><div><h5>Ingredientes</h5><ul>{ing}</ul></div><div><h5>Preparación</h5><ol>{pas}</ol></div></div>'
            f'<p class="nr-x"><b>Cambialo por:</b> {r["cambio"]}</p>{cons}</div></article>')


# ================================================================== PORTADA
page(f'''
<div class="cv3 nutri">
  <div class="c3-in">
    <img class="c3-logo" src="img/logo_renova.png" alt="RENOVA">
    <span class="c3-pill">MÉTODO RENOVA · MUJERES 35+</span>
    <h1 class="c3-title">ALIMENTACIÓN<br>INTELIGENTE</h1>
    <p class="c3-claim">COMÉ MEJOR, <b><span>SIN DIETAS.</span></b></p>
    <p class="c3-sub"><b>8 semanas</b> de plan práctico con <em>32 recetas</em>,<br><span><mark>menús</mark> y <mark>listas de compras</mark> para tu semana real.</span></p>
  </div>
  <div class="c3-team"><img src="img/equipo_tapa.png" alt="Equipo RENOVA"></div>
</div>
''', pid="portada", cls="p-cover", header=False)

# ================================================================== BIENVENIDA + QUIÉN TE GUÍA
mat = f" · {MATRICULA}" if MATRICULA else ""
page(f'''
{eyebrow("BIENVENIDA")}
<h1 class="h1">Comer mejor, <span class="t">sin vivir a dieta</span></h1>
<p class="lead">Esta guía no busca que cocines todo el domingo, peses cada alimento ni sigas un menú rígido. Busca que tengas <b>decisiones resueltas antes de que llegue el momento de comer</b>.</p>
<div class="nutri-card"><img src="img/eugenia.jpg" alt="{NUTRI}"><div><span class="pill">TE GUÍA</span><h3>{NUTRI}</h3><p class="nc-t">{NUTRI_TITULO}{mat} · Equipo RENOVA</p>
<p>Armé esta guía para mujeres con poco tiempo que quieren comer mejor y acompañar su entrenamiento, con comidas simples y alimentos que conseguís en cualquier súper.</p></div></div>
<h2>Cómo usar esta guía</h2>
<div class="pillars">
  <div class="pillar"><span class="pn">01</span><h3>Aprendé lo básico</h3><p>Capítulos cortos para entender qué poner en el plato.</p></div>
  <div class="pillar"><span class="pn">02</span><h3>Organizate</h3><p>Planificá, comprá y prepará con un sistema simple.</p></div>
  <div class="pillar"><span class="pn">03</span><h3>Aplicalo 8 semanas</h3><p>Cada semana: recetas, cómo combinarlas y lista de compras.</p></div>
</div>
''', chapter="Bienvenida", pid="bienvenida")

page("__TOC__", chapter="Índice", pid="indice")

# ================================================================== PARTE 1 · FUNDAMENTOS
page(f'''
{chap_head("01", 'Un sistema, <span class="t">no otra dieta</span>', "Organizar tu alimentación sirve para reducir decisiones de último momento, no para llenar tu agenda de reglas.")}
<p>Organizarse es decidir con anticipación lo que suele aparecer cuando ya tenés hambre y poco tiempo: <b>qué hay en casa, qué vas a llevar al trabajo, qué falta comprar</b> y qué podés resolver en 15 minutos. Pensalo como un guardarropa: no usás siempre la misma combinación, pero tenés prendas que combinan entre sí.</p>
<h2>Las cuatro piezas del sistema</h2>
<div class="tips10 t4">
  <div><span>01</span><h3>Planificar</h3><p>Mirar la agenda real y elegir qué comidas necesitan resolverse antes.</p></div>
  <div><span>02</span><h3>Comprar</h3><p>Lo que vas a usar, en cantidades razonables y con alternativas.</p></div>
  <div><span>03</span><h3>Preparar</h3><p>Adelantar componentes, no necesariamente platos completos.</p></div>
  <div><span>04</span><h3>Revisar</h3><p>Ver qué funcionó, qué sobró y qué cambiar la semana siguiente.</p></div>
</div>
{box("<b>Empezá por una sola comida.</b> La que más improvisás. Prepará una opción principal y otra de respaldo, y probalo una semana.", "soft")}
''', chapter="01 · Un sistema, no una dieta", pid="cap1", toc="01 · Un sistema, no otra dieta")

page(f'''
{chap_head("02", 'Armá <span class="t">tu plato</span>', "No hace falta memorizar listas de alimentos permitidos: alcanza con reconocer qué aporta cada grupo y combinarlo.")}
<div class="plate-wrap">
  <div class="plate" aria-hidden="true">
    <div class="pl-veg">½ Verduras</div><div class="pl-pro">¼ Proteína</div><div class="pl-car">¼ Carbohi&shy;dratos</div>
  </div>
  <div>
    {ul(["<b>Mitad del plato:</b> verduras crudas o cocidas, de distintos colores.",
         "<b>Un cuarto:</b> proteína: carne, pollo, pescado, huevo, lácteos, legumbres o tofu.",
         "<b>Un cuarto:</b> energía: arroz, papa, batata, pan, pastas, choclo, avena o legumbres.",
         "<b>Un toque de grasas:</b> aceite de oliva, palta, frutos secos o semillas.",
         "<b>Para tomar:</b> agua."])}
  </div>
</div>
<h3>Paso a paso</h3>
<ol class="steps-ol">
<li><b>Elegí la proteína</b> que tengas disponible.</li>
<li><b>Sumá vegetales:</b> frescos, congelados o de lata.</li>
<li><b>Definí la fuente de energía</b> según tu hambre y tu actividad.</li>
<li><b>Dale sabor:</b> hierbas, especias, limón o un poco de aceite.</li>
</ol>
{box("<b>El plato es una guía, no una regla exacta.</b> Si entrenás, tenés mucha actividad o poco apetito, la distribución puede cambiar. Lo que importa es el conjunto del día.", "note")}
''', chapter="02 · Armá tu plato", pid="cap2", toc="02 · Armá tu plato")

page(f'''
{eyebrow("ARMÁ TU PLATO")}
<h1 class="h1">Los nutrientes, <span class="t">en una hoja</span></h1>
{table(["", "Para qué sirve", "Dónde está", "Cómo sumarla"], [
 ["<b>Proteínas</b>", "Forman y reparan tejidos, incluido el músculo.", "Huevo, carnes, pescado, lácteos, legumbres, soja.", "Una fuente en cada comida, no todo en la cena."],
 ["<b>Carbohidratos</b>", "Energía para el día y para entrenar.", "Arroz, avena, pan, pastas, papa, batata, legumbres, frutas.", "Preferí integrales y no los elimines."],
 ["<b>Grasas</b>", "Necesarias para el cuerpo; aportan mucha energía.", "Aceite de oliva, palta, frutos secos, semillas, pescados.", "Usalas como toque, medidas con cuchara."],
 ["<b>Fibra</b>", "Saciedad, tránsito intestinal y salud digestiva.", "Verduras, frutas, legumbres, avena, integrales.", "Aumentala de a poco y con más agua."],
])}
<h2>Proteína después de los 35</h2>
<p>La proteína ayuda a mantener el músculo, sobre todo si entrenás fuerza. <b>No hay una cantidad universal</b>: depende de tu peso, tu actividad y tu salud. Revisá que cada comida tenga alguna fuente de proteína y, si querés una cifra para vos, consultala con un profesional. No hace falta empezar con suplementos.</p>
{box("<b>Error frecuente:</b> sacar el arroz, la papa, el pan o las frutas por miedo a los carbohidratos. Si entrenás, restringir energía sin criterio perjudica el rendimiento y la recuperación.", "soft")}
''', chapter="02 · Armá tu plato", pid="cap2b")

page(f'''
{eyebrow("ARMÁ TU PLATO")}
<h1 class="h1">Frutas, verduras <span class="t">y agua</span></h1>
<p>Variar colores y tipos amplía los nutrientes que recibís. Frescas, congeladas o cocidas: todas suman.</p>
{table(["Color", "Ejemplos", "Cómo usarlos"], [
 ["<b>Verde</b>", "Espinaca, acelga, brócoli, rúcula", "Ensaladas, tortillas, salteados"],
 ["<b>Rojo</b>", "Tomate, morrón, frutilla, sandía", "Frescos, asados o en salsas"],
 ["<b>Naranja</b>", "Zanahoria, zapallo, naranja, durazno", "Purés, bastones, colaciones"],
 ["<b>Violeta</b>", "Berenjena, repollo morado, arándanos", "Asados, salteados, frescos"],
 ["<b>Blanco</b>", "Coliflor, cebolla, ajo, pera", "Base de preparaciones y sabor"],
])}
<h2>Hidratación</h2>
{ul(["<b>Tené una botella a la vista</b> y tomá de a poco durante el día.", "<b>Agua como bebida principal</b>; sumá infusiones o agua saborizada natural (con limón o menta).", "<b>Más agua si entrenás</b>, hace calor o sumás fibra.", "Si tenés indicaciones médicas sobre líquidos, seguí las de tu profesional."])}
''', chapter="02 · Armá tu plato", pid="cap2c")

page(f'''
{chap_head("03", 'Porciones y <span class="t">etiquetas</span>', "Referencias simples para servir y comprar, sin balanza ni calculadora.")}
<h2>Tu mano como medida</h2>
{table(["Grupo", "Referencia orientativa"], [
 ["<b>Proteína</b> (carne, pollo, pescado)", "La palma de tu mano, sin los dedos"],
 ["<b>Carbohidratos</b> (arroz, pastas, papa)", "Lo que entra en tu mano cerrada"],
 ["<b>Verduras</b>", "Dos manos abiertas, o medio plato"],
 ["<b>Grasas</b> (aceite, frutos secos)", "La punta del pulgar o un puñado chico"],
])}
<p class="small">Son referencias para empezar, no cantidades obligatorias: ajustalas a tu hambre, tu actividad y la indicación de tu profesional.</p>
<h2>Cómo leer una etiqueta</h2>
<ol class="steps-ol">
<li><b>Porción y contenido neto:</b> mirá a qué cantidad corresponden los números.</li>
<li><b>Ingredientes:</b> van de mayor a menor cantidad. Mirá los primeros.</li>
<li><b>Tabla nutricional:</b> compará por 100 g productos de la misma categoría.</li>
<li><b>Sellos (octógonos):</b> advierten excesos de nutrientes críticos. Son una alerta, no una prohibición.</li>
</ol>
{box("<b>“Light”, “diet” o “con proteínas”</b> no dicen todo: revisá qué se redujo o agregó, la porción y el resto de la composición.", "soft")}
''', chapter="03 · Porciones y etiquetas", pid="cap3", toc="03 · Porciones y etiquetas")

# ================================================================== PARTE 2 · ORGANIZACIÓN
page(f'''
{chap_head("04", 'Planificá <span class="t">tu semana</span>', "El menú útil no es el que se cumple al pie de la letra: es el que tiene alternativas cuando la semana cambia.")}
<h2>Primero la agenda, después el menú</h2>
<p>Mirá el calendario: días de oficina, home office, reuniones, actividades familiares. Marcá cada comida como <b>en casa</b>, <b>para llevar</b> o <b>comprar afuera</b>. Eso define qué necesitás preparar.</p>
<h2>El plan A, B y C</h2>
<div class="tips10 t3">
  <div><span>A</span><h3>Día normal</h3><p>Tenés tiempo: usás el menú planificado.</p></div>
  <div><span>B</span><h3>Día complicado</h3><p>Vianda del freezer o una combinación de alacena.</p></div>
  <div><span>C</span><h3>Día afuera</h3><p>Sabés dónde comprar o llevás algo transportable.</p></div>
</div>
{box("<b>Ejemplo:</b> Mariana, 47 años, trabaja desde casa lunes y miércoles. Planifica solo tres almuerzos para llevar, deja una porción congelada para un imprevisto y decide antes dónde almorzar el viernes. Un plan menos ambicioso, y más fácil de cumplir.", "note")}
''', chapter="04 · Planificá tu semana", pid="cap4", toc="04 · Planificá tu semana")

page(f'''
{chap_head("05", 'Compras <span class="t">inteligentes</span>', "La buena compra empieza antes de entrar al súper: con tu agenda, tu heladera y tu despensa.")}
<h2>La revisión de 5 minutos</h2>
{ul(["<b>Heladera:</b> qué hay que usar pronto.", "<b>Freezer y alacena:</b> legumbres, cereales, conservas, porciones listas.", "<b>Tu semana:</b> cuántas comidas necesitás resolver.", "<b>Lista con cantidades:</b> no “verduras”, sino cuáles y para qué."])}
<h2>Económico y práctico</h2>
{table(["Recurso", "Por qué conviene"], [
 ["<b>Verduras congeladas</b>", "Duran, no se desperdician y salen en minutos."],
 ["<b>Legumbres secas o en lata</b>", "Proteína y fibra económicas. Las de lata, enjuagadas."],
 ["<b>Atún, caballa o sardinas</b>", "Proteína lista para una comida de emergencia."],
 ["<b>Frutas y verduras de estación</b>", "Más baratas y en mejor estado. Preguntá en la verdulería."],
 ["<b>Precio por kilo</b>", "Compará envases distintos, pero comprá lo que vas a usar."],
])}
{box("<b>Cadena de frío:</b> dejá carnes, pescados y lácteos para el final de la compra y llevalos a la heladera sin demoras.", "soft")}
''', chapter="05 · Compras inteligentes", pid="cap5", toc="05 · Compras inteligentes")

page(f'''
{chap_head("06", 'Meal prep <span class="t">sin pasar el domingo en la cocina</span>', "Adelantar parte de las comidas no exige cocinar siete platos: alcanza con preparar componentes.")}
<div class="tips10 t3">
  <div><span>1</span><h3>Ingredientes listos</h3><p>Lavar y cortar vegetales, porcionar frutos secos.</p></div>
  <div><span>2</span><h3>Componentes cocidos</h3><p>Una proteína, un cereal y una bandeja de vegetales.</p></div>
  <div><span>3</span><h3>Comidas completas</h3><p>Algunas viandas listas para heladera o freezer.</p></div>
</div>
<h2>El método de 60 a 90 minutos</h2>
<ol class="steps-ol">
<li><b>Revisá agenda y heladera</b> (10 min): cuántas comidas necesitás.</li>
<li><b>Elegí dos componentes base</b>, por ejemplo vegetales y legumbres.</li>
<li><b>Empezá por lo que tarda más:</b> horno u olla de legumbres.</li>
<li><b>Mientras se cocina,</b> lavá y cortá, con tablas separadas para crudos.</li>
<li><b>Porcioná y rotulá</b> con nombre y fecha.</li>
</ol>
{box("<b>Para que no todo tenga el mismo gusto:</b> condimentá distinto al servir (limón y hierbas; ajo y pimentón; comino) y guardá aderezos y hojas aparte.", "soft")}
''', chapter="06 · Meal prep", pid="cap6", toc="06 · Meal prep")

page(f'''
{chap_head("07", 'Heladera, freezer <span class="t">y seguridad</span>', "Una comida organizada también tiene que ser segura. El olor no alcanza para saber si un alimento está bien.")}
<div class="tips10">
  <div><span>01</span><h3>Limpiar</h3><p>Manos, mesadas, tablas y utensilios.</p></div>
  <div><span>02</span><h3>Separar</h3><p>Crudos lejos de cocidos y listos para comer.</p></div>
  <div><span>03</span><h3>Cocinar bien</h3><p>Carnes, pollo, pescado y huevo, cocidos hasta el centro.</p></div>
  <div><span>04</span><h3>Enfriar rápido</h3><p>No más de 2 horas a temperatura ambiente.</p></div>
</div>
{table(["Zona de la heladera", "Qué va"], [
 ["<b>Estantes de arriba y del medio</b>", "Listos para comer, lácteos y preparaciones tapadas."],
 ["<b>Estante de abajo</b>", "Carnes y pescados crudos, en recipientes."],
 ["<b>Cajones</b>", "Frutas y verduras."],
 ["<b>Puerta</b>", "Condimentos y lo que tolera cambios de temperatura."],
])}
''', chapter="07 · Heladera y seguridad", pid="cap7", toc="07 · Heladera, freezer y seguridad")

page(f'''
{eyebrow("HELADERA Y SEGURIDAD")}
<h1 class="h1">Cuánto <span class="t">guardar</span></h1>
{table(["Alimento", "Heladera (4 °C o menos)"], [
 ["Carnes crudas y cocidas", "2 a 3 días"],
 ["Verduras cocidas", "3 a 4 días"],
 ["Platos cocinados", "3 a 5 días, según la preparación"],
])}
<p class="small">Tiempos orientativos de SENASA. Ante la duda, consumí antes o congelá a tiempo.</p>
<h2>Freezer a tu favor</h2>
{ul(["<b>Congelá</b> lo que no vas a comer en los próximos días.", "<b>Rotulá</b> con nombre y fecha.", "<b>Descongelá en la heladera</b>, no sobre la mesada.", "<b>No vuelvas a congelar</b> un alimento crudo ya descongelado."])}
<h2>Viandas</h2>
<p>Llevalas en bolsa térmica con refrigerantes y guardalas en la heladera apenas llegues. Al recalentar, que quede bien caliente en todas partes: revolvé a mitad si usás microondas.</p>
''', chapter="07 · Heladera y seguridad", pid="cap7b")

page(f'''
{chap_head("08", 'Comer <span class="t">fuera de casa</span>', "Oficina, reuniones, restaurantes, delivery y viajes: la misma estructura, en otro lugar.")}
{table(["Situación", "Cómo resolverla"], [
 ["<b>Oficina</b>", "Vianda de componentes o un menú del día con plancha y ensalada."],
 ["<b>Reuniones</b>", "Servite un plato con proteína y vegetales, comé tranquila y disfrutá."],
 ["<b>Restaurante</b>", "Mirá la carta antes; elegí una proteína, sumá vegetales y compartí el postre si querés."],
 ["<b>Delivery</b>", "Wok, ensaladas completas, sushi o carnes con guarnición de vegetales."],
 ["<b>Viajes</b>", "Llevá snacks: fruta, frutos secos, yogur, talitas. Hidratate."],
 ["<b>Día sin planificar</b>", "Menú de emergencia: huevo o atún + vegetal + pan, arroz o papa."],
])}
{box("<b>Sin compensar:</b> una comida diferente no se “paga” salteando la siguiente ni con ejercicio extra. Volvé a tu estructura en la próxima comida.", "soft")}
''', chapter="08 · Fuera de casa", pid="cap8", toc="08 · Comer fuera de casa")

# ================================================================== PARTE 3 · PROGRAMA DE 8 SEMANAS
page(f'''
<div class="divider dv8">
  <img class="dv-logo" src="img/logo_renova.png" alt="RENOVA">
  <p class="dv-kick">TU PROGRAMA PRÁCTICO</p>
  <h1 class="dv-title">8 SEMANAS</h1>
  <p class="dv-sub">32 recetas · menús · listas de compras</p>
  <div class="dv-bar"></div>
  <p class="dv-desc">Cada semana tiene un objetivo, 4 recetas, una idea de cómo combinarlas los 7 días, cómo organizarte y tu lista de compras.</p>
  <div class="dv-list">
    {"".join(f'<a href="#sem{s["n"]}"><span>{s["n"]}</span><b>{re.sub("<[^>]+>", "", s["titulo"])}</b><em>Página <span class="pref" data-ref="sem{s["n"]}"></span></em></a>' for s in SEMANAS)}
  </div>
</div>
''', pid="programa", cls="p-cover", header=False, toc="09 · Tu programa de 8 semanas")

page(f'''
{eyebrow("TU PROGRAMA")}
<h1 class="h1">Cómo usar <span class="t">las 8 semanas</span></h1>
{ul(["<b>Una semana, un objetivo:</b> no cambies todo junto; sumá un hábito por semana.",
     "<b>4 recetas por semana</b> que se reutilizan: lo que cocinás para el almuerzo sirve para otra comida.",
     "<b>El cuadro de los 7 días es una idea,</b> no una obligación. Movelo según tu agenda.",
     "<b>Desayunos y meriendas:</b> elegí entre las opciones de la semana o las anteriores.",
     "<b>Las cantidades son orientativas</b> y para personas sanas. Ajustalas a tu hambre y actividad."])}
{box("<b>Aclaración:</b> estas semanas son etapas para aprender hábitos, no un tratamiento nutricional. Si tenés una enfermedad, tomás medicación, estás embarazada o tenés antecedentes de trastornos de la conducta alimentaria, consultá con un profesional antes de cambiar tu alimentación.", "note")}
<div class="quote">Pequeños cambios sostenidos <span class="t">valen más que una semana perfecta.</span></div>
''', chapter="09 · Programa de 8 semanas", pid="prog-como")

n = 0
for s in SEMANAS:
    dias = table(["Día", "Almuerzo", "Cena"], [[d, a, c] for d, (a, c) in zip(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"], s["dias"])], cls="grid-t ntab semtab")
    desay = ", ".join(r["t"] for r in s["recetas"] if any(k in r["cat"].lower() for k in ("desayuno", "merienda", "snack", "postre")))
    page(f'''
<div class="semhead"><span class="semn">SEMANA {s["n"]}</span><h1 class="h1">{s["titulo"]}</h1>
<p class="lead"><b>Objetivo:</b> {s["objetivo"]}</p><p class="semap"><b>Aprendizaje:</b> {s["aprendizaje"]}</p></div>
<h3>Tu semana, combinada</h3>
{dias}
<p class="small"><b>Desayunos y meriendas:</b> {desay or "elegí entre las opciones de semanas anteriores"}, o yogur con fruta, tostadas con queso y huevo, fruta con frutos secos.</p>
<div class="cols2 keep semoc"><div class="semorg"><h3>Organizate</h3>{ul(s["orga"])}</div>
<div class="semshop"><h3>Lista de compras</h3>{checks(s["compras"])}</div></div>
''', chapter=f"09 · Semana {s['n']}", pid=f"sem{s['n']}")
    cards = []
    for r in s["recetas"]:
        n += 1
        cards.append(ficha(r, n))
    org = (f'<div class="cols2 keep semoc"><div class="semorg"><h3>Organizate</h3>{ul(s["orga"])}</div>'
           f'<div class="semshop"><h3>Lista de compras</h3>{checks(s["compras"])}</div></div>')
    page(f'''<h2 class="semrh">Recetas de la semana {s["n"]}</h2>''' + "".join(cards), chapter=f"09 · Semana {s['n']} · Recetas", pid=f"sem{s['n']}r")


# ================================================================== EXTRA · DESAYUNOS Y MERIENDAS DE EUGENIA + REEMPLAZOS + PRODUCTOS
EXTRAS = [
 rec("Pancake de coco", "Desayuno o merienda", "10 min", "1 porción",
     ["2 huevos (o 1 huevo y 1 clara)", "5 cdas de coco rallado", "1 cdita de polvo de hornear", "Esencia de vainilla y gotas de stevia"],
     ["Batí todo enérgicamente para que no queden grumos.", "Volcá en una sartén aceitada a fuego mínimo.", "Cociná vuelta y vuelta. Toppings: fruta, frutos secos o pasta de maní."],
     "coco por avena; stevia por fruta pisada.", foto="eve/r5"),
 rec("Galletitas de 4 ingredientes sin azúcar", "Merienda", "30 min", "8 a 10 galletitas",
     ["¼ taza de harina de garbanzos", "2 cdas de pasta de maní", "4 dátiles sin carozo (remojados si están secos)", "4 nueces picadas, 3 cdas de agua y ½ cdita de polvo de hornear"],
     ["Mezclá todo hasta formar una masa (si hace falta, enfriala un rato).", "Formá las galletitas sobre una placa.", "Horneá a 200 °C unos 20 minutos, hasta que estén doradas."],
     "dátiles por pasas remojadas; nueces por almendras.", "3 a 4 días en recipiente hermético o 2 meses en freezer.", foto="eve/r18"),
 rec("Granola de quinoa", "Desayuno o merienda", "35 min", "Aprox. 6 porciones",
     ["1 taza de quinoa cocida (⅓ taza cruda)", "¼ taza de semillas de girasol y zapallo", "¼ taza de frutos secos picados", "¼ taza de coco rallado y 2 cdas de miel"],
     ["Lavá bien la quinoa, hervila hasta que esté transparente, colala y enfriala.", "Mezclá con semillas, frutos secos, coco y miel.", "Horneá en placa con papel manteca a 180 °C, revolviendo cada 5 minutos, unos 15 minutos."],
     "miel por azúcar mascabo o dulce de dátiles.", "2 semanas en frasco cerrado.", foto="eve/r15"),
 rec("Budín de manzana, canela y nuez", "Merienda", "45 min", "1 budín (6 porciones)",
     ["3 a 4 cdas de avena", "3 claras y 1 huevo", "1 manzana en láminas finas", "1 puñado de nueces, canela, stevia y 1 cdita de polvo de hornear"],
     ["Precalentá el horno a 180 °C.", "Licuá todo menos la manzana y las nueces, y volcá en una budinera.", "Acomodá la manzana y las nueces arriba y horneá unos 40 minutos."],
     "manzana por banana o pera.", "3 a 4 días en heladera o 2 meses en freezer.", foto="eve/r23"),
 rec("Crackers de semillas", "Snack salado", "1 h + hidratación", "Aprox. 30 crackers",
     ["½ taza de harina de garbanzos + ½ taza de agua", "1 taza de chía y lino", "1 taza y ½ de semillas de girasol, zapallo y sésamo", "1 cda de aceite de oliva, ajo en polvo y curry"],
     ["Hidratá la harina de garbanzos con el agua entre 1 y 8 horas.", "Mezclá con las semillas, el aceite y los condimentos.", "Estirá fino en placa con papel manteca, marcá los cortes y horneá a 180 °C hasta que estén secos y dorados."],
     "condimentos a elección: orégano, pimentón, sésamo negro.", "2 semanas en recipiente hermético.", foto="eve/r26"),
 rec("Snack de garbanzos tostados", "Snack salado", "35 min", "3 porciones",
     ["1 lata de garbanzos (o 150 g secos, remojados y hervidos)", "2 cdas de aceite de oliva", "Orégano, pimienta, comino y sal"],
     ["Escurrí y secá muy bien los garbanzos.", "Mezclalos con el aceite y los condimentos.", "Horneá en placa con papel manteca a horno moderado 30 minutos, hasta que estén crocantes."],
     "probá con pimentón ahumado o curry.", "4 a 5 días en frasco cerrado.", foto="eve/r28"),
]
cards = "".join(ficha(r, 32 + i) for i, r in enumerate(EXTRAS, 1))
page(f'''
{eyebrow("EXTRA · RECETARIO DE EUGENIA")}
<h1 class="h1">Desayunos y <span class="t">meriendas extra</span></h1>
<p class="lead">Seis recetas del recetario de {NUTRI} para sumar variedad a tus mañanas y tardes.</p>
{cards}
{box("<b>Conservación de lo casero:</b> sin conservantes, duran poco fuera de la heladera (3 a 4 días). Guardalas en recipientes herméticos y, si hacés en cantidad, congelalas hasta 2 meses. Antes de comerlas, un golpe de horno de 5 minutos.", "soft")}
''', chapter="Extra · Recetario", pid="extras", toc="Extra: desayunos y meriendas")

page(f'''
{eyebrow("EXTRA")}
<h1 class="h1">Reemplazos <span class="t">saludables</span></h1>
<p>No se trata de prohibir, sino de tener alternativas a mano. Usalos cuando te sirvan.</p>
{table(["En vez de…", "Probá con…"], [
 ["<b>Azúcar</b>", "Stevia, dulce de dátiles o pasas, o fruta madura (banana, manzana)."],
 ["<b>Harina blanca</b>", "Harina integral, de avena o de garbanzos (o una mezcla)."],
 ["<b>Manteca</b>", "Aceite de oliva o de girasol, palta o pasta de maní."],
 ["<b>Crema o mayonesa</b>", "Yogur natural, queso untable o palta pisada."],
 ["<b>Snacks de paquete</b>", "Garbanzos tostados, crackers de semillas, frutos secos o fruta."],
 ["<b>Gaseosas y jugos</b>", "Agua, agua con frutas o menta, infusiones frías."],
 ["<b>Pan rallado</b>", "Avena, semillas o harina de garbanzos."],
 ["<b>Huevo (en budines)</b>", "Gel de chía o lino: 1 cda de semillas + 3 cdas de agua, 20 min."],
])}
{box("<b>Equivalencias de endulzantes:</b> 1 cda sopera de stevia ≈ 50 g de azúcar ≈ 40 g de dulce de pasas o dátiles. La idea es ir usando cada vez menos, para que tu paladar se adapte.", "note")}
''', chapter="Extra · Reemplazos", pid="reemplazos", toc="Extra: reemplazos saludables")

PROD = [("c2", "Panes, galletas y granolas"), ("c3", "Granos integrales y harinas"), ("c4", "Avena y fideos"), ("c8", "Crackers y snacks salados"),
        ("c16", "Lácteos"), ("c17", "Yogures"), ("c21", "Congelados y semillas"), ("c22", "Proteínas")]
for k in (0, 4):
    grid = "".join(f'<figure class="prodf"><img src="img/prod/{f}.jpg" alt="{t}"><figcaption>{t}</figcaption></figure>' for f, t in PROD[k:k + 4])
    page(f'''
{eyebrow("EXTRA · PRODUCTOS RECOMENDADOS")}
<h1 class="h1">{"Qué comprar <span class=\"t\">en el súper</span>" if k == 0 else "Más productos <span class=\"t\">recomendados</span>"}</h1>
{"<p class=\"small\">Selección de " + NUTRI + ": marcas que conseguís en supermercados y dietéticas. Hacé zoom para ver cada producto.</p>" if k == 0 else ""}
<div class="prodg">{grid}</div>
''', chapter="Extra · Productos", pid=f"prod{k}", toc="Extra: productos recomendados" if k == 0 else None)

# ================================================================== PARTE 4 · SOSTENER
page(f'''
{chap_head("10", 'Cuando la semana <span class="t">no sale como esperabas</span>', "La constancia no se construye con semanas perfectas, sino con una estructura que te deje volver a empezar sin castigos.")}
<h2>La trampa del todo o nada</h2>
<p>Una comida improvisada no arruina una semana. <b>Volvé a la próxima decisión posible:</b> si no llevaste vianda, elegí algo razonable donde estés; si no pudiste cocinar, usá tu menú de emergencia.</p>
<h2>Una pausa antes de decidir</h2>
{ul(["<b>Frená un momento</b> y alejate de la pantalla.", "<b>¿Qué necesitás?</b> ¿Hambre, cansancio, aburrimiento, un descanso?", "<b>Respondé a eso:</b> si es hambre, comé; si es cansancio, pausá.", "<b>Sin compensar:</b> no saltees comidas ni sumes ejercicio como castigo."])}
<h2>La revisión de 10 minutos</h2>
<p>Un día por semana: ¿qué preparación usé más?, ¿qué sobró?, ¿qué momento fue difícil?, ¿qué cambio chico hago la semana que viene?</p>
{box("<b>Cuándo pedir ayuda:</b> si tenés una enfermedad, tomás medicación que cambia el apetito o la glucemia, estás embarazada o amamantando, o tenés una relación angustiante con la comida, necesitás una orientación individual. Los talleres de gestión de la ansiedad de RENOVA también te pueden ayudar.", "note")}
''', chapter="10 · Sostener el cambio", pid="cap10", toc="10 · Cuando la semana no sale")

page(f'''
{eyebrow("HERRAMIENTAS")}
<h1 class="h1">Tu <span class="t">planificador semanal</span></h1>
<p class="small">Completalo en 10 minutos, una vez por semana. Usá el lápiz: se cambia.</p>
{table(["Día", "Agenda", "Almuerzo", "Cena", "Plan B"], [[d, "", "", "", ""] for d in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]], cls="grid-t ntab plan-in")}
''', chapter="Herramientas", pid="plantilla1", toc="Herramientas: planificador y lista")

page(f'''
{eyebrow("HERRAMIENTAS")}
<h1 class="h1">Tu <span class="t">lista de compras</span></h1>
{table(["Grupo", "Ya tengo", "Necesito", "Para qué comida"], [[g, "", "", ""] for g in ["Verduras", "Frutas", "Proteínas", "Legumbres y cereales", "Lácteos", "Alacena", "Freezer"]], cls="grid-t ntab plan-in")}
<h2>Auditoría rápida de heladera</h2>
{checks(["Está fría y el aire circula.", "Todo tapado y rotulado.", "Crudos separados de cocidos; carnes abajo.", "Lo más viejo adelante.", "Nada sin fecha ni contenido conocido."])}
''', chapter="Herramientas", pid="plantilla2")

page(f'''
{eyebrow("FUENTES")}
<h1 class="h1">Fuentes <span class="t">y aclaraciones</span></h1>
{ul(["<b>Ministerio de Salud de la Nación</b> — Guías Alimentarias para la Población Argentina y gráfica de alimentación saludable.",
     "<b>ANMAT</b> — Recomendaciones para la manipulación segura de los alimentos.",
     "<b>SENASA / Argentina.gob.ar</b> — Pautas de refrigeración y tiempos orientativos de conservación.",
     "<b>Argentina.gob.ar</b> — Manipulación de alimentos y cadena de frío.",
     "<b>Ley 27.642</b> de Promoción de la Alimentación Saludable — etiquetado frontal de alimentos."])}
{box("<b>Material educativo general.</b> Esta guía no reemplaza una consulta con un/a licenciado/a en Nutrición ni una evaluación médica. No establece calorías, porciones obligatorias, objetivos de peso ni cantidades individuales de nutrientes. Las necesidades cambian según tu historia clínica, actividad, preferencias, medicación y etapa de vida.", "note")}
<p class="small">Revisión de contenidos: {NUTRI}, {NUTRI_TITULO}{mat}.</p>
''', chapter="Fuentes", pid="fuentes", toc="Fuentes y aclaraciones")

page(f'''
<div class="bio metodo">
  {eyebrow("PLAN INTEGRAL RENOVA")}
  <h1 class="h1 big">Tu plan integral <span class="t">1 a 1 con Nacho</span></h1>
  <div class="team-big"><img src="img/equipo2.jpg" alt="Equipo RENOVA" style="height:auto;max-height:120mm;object-fit:contain"></div>
  <p class="lead center"><b>Consultá por tu plan integral personalizado 1 a 1 con Nacho:</b> entrenamiento y nutrición armados para vos, con el equipo RENOVA.</p>
  <div class="cta-center"><a class="btn btn-big" href="{esc(LINK_PLAN)}">CONSULTÁ POR TU PLAN {ICON_ARROW}</a></div>
  <div class="quote dark">No necesitás una semana perfecta. <span class="t2">Necesitás herramientas para la semana que tenés.</span></div>
</div>
''', chapter="Plan integral", pid="metodo", toc="Tu plan integral 1 a 1")


# ================================================================== RENDER
def render():
    num = {p["id"]: i + 1 for i, p in enumerate(PAGES)}
    toc_html = '<div class="tocl">' + "".join(
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
            hdr = (f'<div class="hdr"><span>ALIMENTACIÓN INTELIGENTE · <b>RENOVA</b></span><span>{esc(p["chapter"])}</span></div>'
                   f'<div class="ftr"><a class="toidx" href="#indice">{ICON_HAND} Hacé clic y volvé al índice</a><span class="pgnum"></span></div>')
        out.append(f'<section class="page {p["cls"]}" id="{p["id"]}">{hdr}<div class="body">{body}</div></section>')
    css = ds_css(HERE) + "\n" + open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Alimentación Inteligente · RENOVA</title>'
            f'<style>{css}</style></head><body class="grande">' + "".join(out) + '<script src="paginate.js"></script></body></html>')


if __name__ == "__main__":
    with open(os.path.join(HERE, "nutricion.html"), "w", encoding="utf-8") as f:
        f.write(render())
    print("nutricion.html ·", len(PAGES), "páginas antes de paginar")
