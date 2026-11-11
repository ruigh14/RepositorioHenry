"""Brief para que Eugenia valide las recetas nuevas de Alimentación Inteligente (las que no salen de su recetario ni del de RENOVA).
Uso: cd fuentes/ebook && python3 revision_eugenia.py y exportar revision_eugenia.html a PDF con Playwright → alimentacion-inteligente/Revision_recetas_Eugenia.pdf"""
import os, sys
sys.argv = [sys.argv[0]]
import nutricion as N

nuevas = [(s["n"], r) for s in N.SEMANAS for r in s["recetas"] if r["foto"] is None]
filas = []
for i, (sem, r) in enumerate(nuevas, 1):
    filas.append(f'''<div class="r"><h3>{i}. {r["t"]} <small>· Semana {sem} · {r["cat"]} · {r["tiempo"]} · {r["porc"]}</small></h3>
<div class="c"><div><b>Ingredientes</b><ul>{"".join(f"<li>{x}</li>" for x in r["ing"])}</ul></div>
<div><b>Preparación</b><ol>{"".join(f"<li>{x}</li>" for x in r["pasos"])}</ol></div></div>
<p><b>Reemplazos:</b> {r["cambio"]} {("<br><b>Conservación:</b> " + r["conserva"]) if r["conserva"] else ""}</p>
<p class="ok">☐ OK &nbsp;&nbsp; ☐ Cambiar: ______________________________________________</p></div>''')
html = f'''<!doctype html><meta charset="utf-8"><style>
body{{font-family:Arial,sans-serif;font-size:10.5pt;color:#141414;margin:16mm}}
h1{{color:#0E9DB2;margin:0}} .lead{{margin:2mm 0 6mm}}
.r{{border:1px solid #CDEEF3;border-radius:6px;padding:3mm 4mm;margin-bottom:4mm;break-inside:avoid}}
h3{{margin:0 0 2mm;font-size:12pt}} small{{color:#555;font-weight:normal}}
.c{{display:grid;grid-template-columns:1fr 1.3fr;gap:5mm}} ul,ol{{margin:1mm 0;padding-left:5mm}} p{{margin:2mm 0 0}}
.ok{{color:#0A7F90}} .q li{{margin-bottom:1.5mm}}
</style>
<h1>Revisión de recetas · Alimentación Inteligente</h1>
<p class="lead">Para: Lic. María Eugenia Ballini (M.N. 11773) · De: Nacho Portillo / RENOVA</p>
<p>Euge: el ebook de nutrición de 8 semanas ya está armado (57 hojas). Usa tus recetas y las del recetario RENOVA, que ya están probadas. Estas <b>{len(nuevas)} recetas son nuevas</b> y necesitamos tu OK antes de venderlo.</p>
<p><b>Qué revisar en cada una:</b></p>
<ul class="q"><li>Cantidades y porciones razonables para una mujer adulta activa.</li>
<li>Tiempos de cocción y temperaturas.</li><li>Seguridad: cocción de carnes, huevo y pescado; tiempos de conservación.</li>
<li>Reemplazos: que sean equivalentes.</li><li>Si alguna no te convence, proponé otra de tu recetario.</li></ul>
<p><b>Además, revisá en el PDF completo:</b> el cuadro de 7 días de cada semana, la tabla de reemplazos saludables (incluye tus equivalencias de endulzantes), las porciones con la mano y los tiempos de heladera (SENASA).</p>
<p style="margin-bottom:6mm">Marcá OK o escribí el cambio y devolvémelo.</p>
{"".join(filas)}'''
open(os.path.join(N.HERE, "revision_eugenia.html"), "w", encoding="utf-8").write(html)
print(len(nuevas), "recetas")
