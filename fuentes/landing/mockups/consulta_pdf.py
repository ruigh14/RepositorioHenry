"""Entregable del upsell post compra de la tienda Sin TACC: primera consulta con la nutricionista + charla con Nacho.
Uso: cd fuentes/landing/mockups && python3 consulta_pdf.py && node consulta_pdf.js
  → ../../../sin-tacc-inteligente/Consulta_equipo_RENOVA.pdf"""
from pathlib import Path
F = "../../design-system/fonts/"
WA = "https://wa.link/1asjt1"
TEL, TEL_WA = "11 3320-9619", "https://wa.me/5491133209619"
CSS = f"""@font-face{{font-family:IT;src:url({F}inter-tight-latin-var.woff2);font-weight:100 900}}
@font-face{{font-family:I;src:url({F}inter-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:I;src:url({F}inter-latin-700-normal.woff2);font-weight:700}}
@page{{size:A4;margin:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:I,sans-serif;color:#2A2F33;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;padding:22mm 18mm}}
.pg:last-child{{page-break-after:auto}}
.cv{{background:radial-gradient(ellipse 80% 50% at 50% 38%,rgba(20,177,199,.35),transparent 70%),linear-gradient(165deg,#06343B,#075E6B);color:#fff;text-align:center;padding-top:30mm}}
.marco{{position:absolute;inset:8mm;border:5mm solid #14B1C7;border-radius:12mm;box-shadow:0 0 0 1.6mm #6FD8E6,inset 0 0 0 1.6mm #6FD8E6}}
.logo{{height:13mm}} .cv .logo{{filter:brightness(0) invert(1)}}
.tag{{display:inline-block;margin-top:8mm;background:#14B1C7;color:#fff;font:900 11pt IT;letter-spacing:.14em;padding:2.5mm 7mm;border-radius:99px}}
.cv h1{{font:900 40pt/1 IT;text-transform:uppercase;margin-top:8mm;letter-spacing:-.02em}} .cv h1 b{{color:#6FD8E6}}
.cv p.sub{{font:400 15pt/1.4 I;margin:7mm auto 0;max-width:140mm;color:#E3F6F8}}
.fotos{{display:flex;justify-content:center;gap:16mm;margin-top:14mm}}
.fotos div{{width:62mm}} .fotos img{{width:46mm;height:46mm;border-radius:50%;object-fit:cover;object-position:50% 22%;border:2.4mm solid #14B1C7}}
.fotos b{{display:block;font:900 14pt/1.15 IT;margin-top:4mm}} .fotos span{{display:block;font:700 11pt/1.3 I;color:#BDEFF5;margin-top:1mm}}
h2{{font:900 26pt/1.05 IT;color:#141414;text-transform:uppercase;letter-spacing:-.01em}} h2 b{{color:#0E9DB2}}
.lead{{font:400 15pt/1.45 I;margin-top:5mm}}
.card{{margin-top:8mm;border:.6mm solid #CDEEF3;border-radius:6mm;padding:7mm 8mm;background:#F4FAFB}}
.card h3{{display:flex;align-items:center;gap:5mm;font:900 18pt/1.1 IT;color:#141414}}
.card h3 img{{width:20mm;height:20mm;border-radius:50%;object-fit:cover;object-position:50% 22%;border:1.2mm solid #14B1C7}}
.card h3 small{{display:block;font:700 11pt I;color:#0A7F90;margin-top:1mm}}
ul{{list-style:none;margin-top:5mm}} li{{font:400 14pt/1.45 I;padding-left:9mm;position:relative;margin-top:2.5mm}}
li:before{{content:"✓";position:absolute;left:0;top:0;color:#fff;background:#14B1C7;width:6mm;height:6mm;border-radius:50%;font:900 10pt/6mm IT;text-align:center;margin-top:1mm}}
li b{{color:#141414}}
.steps{{counter-reset:s;margin-top:8mm}} .st{{display:flex;gap:5mm;margin-top:5mm;align-items:flex-start}}
.st i{{flex:none;width:11mm;height:11mm;border-radius:50%;background:#06343B;color:#fff;font:900 16pt/11mm IT;font-style:normal;text-align:center}}
.st p{{font:400 14pt/1.45 I}} .st p b{{color:#141414}}
.btn{{display:block;margin:12mm auto 0;width:150mm;text-align:center;background:linear-gradient(135deg,#14B1C7,#0E9DB2);color:#fff;text-decoration:none;font:900 20pt IT;padding:6mm;border-radius:99px;box-shadow:0 3mm 8mm rgba(20,177,199,.45);text-transform:uppercase}}
.tel{{text-align:center;margin-top:6mm;font:400 14pt I}} .tel a{{color:#0A7F90;font:900 18pt IT;text-decoration:none}}
.note{{margin-top:10mm;font:400 11pt/1.4 I;color:#555C62;text-align:center}}"""
HTML = f"""<!doctype html><meta charset="utf-8"><style>{CSS}</style>
<section class="pg cv"><div class="marco"></div>
<img class="logo" src="../img/logo.png"><br><span class="tag">SIN TACC · EQUIPO RENOVA</span>
<h1>Tu primera consulta<br><b>con el equipo</b></h1>
<p class="sub">Gracias por sumarte. Acá tenés todo lo que incluye tu consulta y cómo coordinarla.</p>
<div class="fotos"><div><img src="../img/equipo_eugenia.jpg"><b>Lic. María Eugenia Aldrey</b><span>Nutricionista · M.N. 11773</span></div>
<div><img src="../img/nacho.jpg"><b>Nacho Portillo</b><span>Coordinador de RENOVA</span></div></div>
</section>
<section class="pg">
<img class="logo" src="../img/logo.png">
<h2 style="margin-top:8mm">Qué <b>incluye</b></h2>
<p class="lead">Todo esto está incluido en tu primera consulta, online y desde tu casa.</p>
<div class="card"><h3><img src="../img/equipo_eugenia.jpg"><span>Consulta con la nutricionista<small>Lic. María Eugenia Aldrey · M.N. 11773</small></span></h3>
<ul><li><b>Tu plan Sin TACC armado para vos,</b> con comidas que te gusten y que puedas sostener.</li>
<li><b>Tus dudas del súper resueltas:</b> qué productos usar, cuáles evitar y cómo leer las etiquetas.</li>
<li><b>Ajustes a tu rutina,</b> tus horarios y tus gustos, para que la guía funcione en tu día a día.</li></ul></div>
<div class="card"><h3><img src="../img/nacho.jpg"><span>Charla con Nacho Portillo<small>Coordinador de RENOVA · Lic. en Alto Rendimiento Deportivo</small></span></h3>
<ul><li><b>Hábitos para tu día a día:</b> movimiento, descanso y organización.</li>
<li><b>Un primer paso concreto</b> para empezar esta misma semana.</li></ul></div>
</section>
<section class="pg">
<img class="logo" src="../img/logo.png">
<h2 style="margin-top:8mm">Cómo <b>coordinar</b></h2>
<div class="steps">
<div class="st"><i>1</i><p><b>Escribinos por WhatsApp</b> con el botón de abajo y contanos que compraste la consulta Sin TACC.</p></div>
<div class="st"><i>2</i><p><b>Coordinamos el día y el horario</b> de tu consulta con la nutricionista y de tu charla con Nacho.</p></div>
<div class="st"><i>3</i><p><b>Antes de la consulta,</b> anotá tus dudas, qué comés en un día normal y qué te cuesta más. Así aprovechamos mejor el tiempo.</p></div>
</div>
<a class="btn" href="{WA}">Escribinos por WhatsApp</a>
<p class="tel">Si el botón no funciona, agendá este número:<br><a href="{TEL_WA}">{TEL}</a></p>
<p class="note">Es tu primera consulta, con la charla incluida; no es un seguimiento semanal.<br>No reemplaza la consulta con tu médico.</p>
</section>"""
Path("consulta_pdf.html").write_text(HTML, encoding="utf-8")
print("ok")
