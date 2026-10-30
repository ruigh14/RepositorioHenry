"""Genera las 2 imágenes armadas de la landing: el plan de nutrición y el collage del programa.
Uso: cd fuentes/landing/mockups && python3 mockups.py && node mockups.js  → ../img/mock_nutricion.jpg y ../img/mock_programa.png"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "design-system"))
from design_system import css

I = "../img/"
BASE = css(str(Path(__file__).parent)) + """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1200px;height:900px;overflow:hidden;font-family:InterW,sans-serif;background:var(--rnv-turquesa-fondo);position:relative}
.bk{position:absolute;background:#fff;border-radius:6px 14px 14px 6px;overflow:hidden;box-shadow:24px 30px 50px rgba(20,20,20,.28)}
.bk::after{content:"";position:absolute;inset:0 auto 0 0;width:6%;background:linear-gradient(90deg,rgba(0,0,0,.22),transparent)}
.cv{position:absolute;inset:0;display:flex;flex-direction:column}
.ttl{font-family:InterTightW,sans-serif;font-weight:900;text-transform:uppercase;letter-spacing:-.02em;line-height:.92;color:#fff}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:6px;flex:1}
.grid img{width:100%;height:100%;object-fit:cover}
.card{position:absolute;background:#fff;border-radius:14px;box-shadow:0 18px 40px rgba(20,20,20,.18);padding:18px 20px}
.card h4{font-family:InterTightW,sans-serif;font-weight:900;color:var(--rnv-tinta);font-size:22px;margin-bottom:10px}
.row{display:flex;align-items:center;gap:10px;font-size:15px;color:var(--rnv-tinta);padding:7px 0;border-bottom:1px solid var(--rnv-linea)}
.ck{width:18px;height:18px;border-radius:4px;border:2px solid var(--rnv-turquesa);flex:none}
.ck.on{background:var(--rnv-turquesa)}
.wk{position:absolute;background:var(--rnv-turquesa);color:#fff;font-family:InterTightW,sans-serif;font-weight:900;font-size:56px;padding:4px 22px;border-radius:10px;transform:rotate(-4deg);box-shadow:0 12px 26px rgba(0,0,0,.25)}
.logo{height:34px;width:auto}
"""

NUT = f"""<!doctype html><meta charset="utf-8"><style>{BASE}</style>
<div class="bk" style="left:60px;top:70px;width:380px;height:520px;transform:rotate(-4deg)"><div class="cv">
  <div style="background:var(--rnv-turquesa);padding:26px 24px 20px"><img class="logo" src="{I}logo.png" style="filter:brightness(0) invert(1)"><p class="ttl" style="font-size:54px;margin-top:14px">Recetario<br>proteico</p>
  <p style="color:#fff;font-weight:700;margin-top:8px;font-size:16px">Recetas ricas en proteína y fibra</p></div>
  <div class="grid" style="padding:6px"><img src="{I}comida_01.jpg"><img src="{I}comida_05.jpg"><img src="{I}comida_09.jpg"><img src="{I}comida_14.jpg"></div></div></div>
<div class="bk" style="left:380px;top:40px;width:380px;height:520px;transform:rotate(3deg)"><div class="cv" style="background:var(--rnv-tinta)">
  <div style="padding:26px 24px"><img class="logo" src="{I}logo.png" style="filter:brightness(0) invert(1)"><p class="ttl" style="font-size:54px;margin-top:14px">Plan de<br><span style="color:var(--rnv-turquesa)">nutrición</span><br>8 semanas</p>
  <p style="color:#fff;font-weight:700;margin-top:10px;font-size:16px">Más proteína · más fibra · comidas simples</p></div>
  <div style="flex:1;background:url({I}comida_18.jpg) center/cover"></div></div></div>
<div class="wk" style="left:120px;top:600px">SEMANA 1</div>
<div class="card" style="left:110px;top:690px;width:520px"><h4>Menú semanal</h4>
  <div class="row"><b style="width:90px">Desayuno</b>Yogur con avena y frutos rojos</div>
  <div class="row"><b style="width:90px">Almuerzo</b>Pollo, quinoa y vegetales</div></div>
<div class="card" style="left:790px;top:330px;width:340px;transform:rotate(4deg)"><h4>Lista de compras</h4>
  <div class="row"><span class="ck on"></span>Huevos y yogur natural</div><div class="row"><span class="ck on"></span>Pollo y pescado</div>
  <div class="row"><span class="ck"></span>Avena, legumbres y quinoa</div><div class="row"><span class="ck"></span>Verduras de estación</div><div class="row"><span class="ck"></span>Frutos secos</div></div>
<div class="card" style="left:780px;top:60px;width:230px;height:230px;padding:8px;transform:rotate(-5deg)"><img src="{I}comida_yogur.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:8px"></div>
<div class="card" style="left:660px;top:640px;width:250px;height:230px;padding:8px;transform:rotate(-3deg)"><img src="{I}comida_15.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:8px"></div>
<div class="card" style="left:930px;top:600px;width:240px;transform:rotate(3deg);text-align:center"><h4>Armá tu plato</h4>
  <div style="width:150px;height:150px;margin:6px auto 10px;border-radius:50%;border:6px solid #fff;box-shadow:0 0 0 2px var(--rnv-linea);background:conic-gradient(var(--rnv-turquesa) 0 50%,var(--rnv-tinta) 50% 75%,var(--rnv-turquesa-borde) 75% 100%)"></div>
  <div style="font-size:13px;text-align:left;line-height:1.6;color:var(--rnv-tinta)"><b style="color:var(--rnv-turquesa)">■</b> ½ verduras<br><b>■</b> ¼ proteína<br><b style="color:var(--rnv-turquesa-borde)">■</b> ¼ carbohidratos</div></div>
"""

PRO = f"""<!doctype html><meta charset="utf-8"><style>{BASE}
body{{width:2200px;height:1000px;background:#fff}}
.tab{{position:absolute;background:var(--rnv-tinta);border-radius:22px;padding:12px;box-shadow:0 22px 44px rgba(20,20,20,.28)}}
.tab img{{display:block;width:100%;height:100%;object-fit:cover;border-radius:10px}}
.ft{{position:absolute;background:#fff;border-radius:16px;padding:7px;box-shadow:0 14px 30px rgba(20,20,20,.2)}}
.ft img{{display:block;width:100%;height:100%;object-fit:cover;border-radius:10px}}
.sh{{position:absolute;background:#fff;border-radius:6px;box-shadow:0 14px 30px rgba(20,20,20,.18);overflow:hidden}}
.sh .hd{{background:var(--rnv-tinta);color:#fff;font-family:InterTightW,sans-serif;font-weight:900;font-size:30px;padding:14px 18px}}
.sh .tg{{position:absolute;top:-2px;left:40px;background:var(--rnv-turquesa);color:#fff;font-family:InterTightW,sans-serif;font-weight:900;font-size:22px;padding:6px 16px;border-radius:0 0 8px 8px}}
.sh table{{width:100%;border-collapse:collapse;font-size:12px}} .sh td{{border:1px solid var(--rnv-linea);height:30px}}
.mon{{position:absolute;left:640px;top:150px;width:760px;height:470px;background:var(--rnv-tinta);border-radius:22px;padding:16px;box-shadow:0 26px 54px rgba(20,20,20,.3)}}
.scr{{width:100%;height:100%;border-radius:10px;background:var(--rnv-degrade);position:relative;overflow:hidden}}
</style>
<div class="sh" style="left:400px;top:70px;width:380px;height:300px;transform:rotate(-7deg)"><span class="tg">SEMANA 2</span><div class="hd" style="padding-top:40px">RENOVA</div><table>{"<tr><td></td><td></td><td></td><td></td></tr>"*7}</table></div>
<div class="sh" style="left:540px;top:50px;width:380px;height:300px;transform:rotate(-3deg)"><span class="tg">SEMANA 1</span><div class="hd" style="padding-top:40px">RENOVA</div><table>{"<tr><td></td><td></td><td></td><td></td></tr>"*7}</table></div>
<div class="ft" style="left:60px;top:150px;width:260px;height:200px;transform:rotate(-5deg)"><img src="{I}comida_11.jpg"></div>
<div class="ft" style="left:40px;top:370px;width:250px;height:190px;transform:rotate(3deg)"><img src="{I}comida_yogur.jpg"></div>
<div class="ft" style="left:60px;top:580px;width:250px;height:190px;transform:rotate(-3deg)"><img src="{I}comida_15.jpg"></div>
<div class="ft" style="left:300px;top:420px;width:230px;height:180px;transform:rotate(4deg)"><img src="{I}comida_01.jpg"></div>
<div class="mon"><div class="scr">
  <img src="{I}logo.png" style="position:absolute;left:40px;top:40px;height:48px;filter:brightness(0) invert(1)">
  <p class="ttl" style="position:absolute;left:40px;top:120px;font-size:72px">RENOVA</p>
  <p style="position:absolute;left:42px;top:210px;color:#fff;font-family:InterTightW,sans-serif;font-weight:800;font-size:28px;line-height:1.2">Para volver a sentirte<br>fuerte después<br>de los 35</p>
  <img src="{I}foto_estocada.jpg" style="position:absolute;right:22px;bottom:22px;width:290px;height:290px;object-fit:cover;border-radius:12px;border:5px solid #fff">
</div></div>
<div style="position:absolute;left:960px;top:620px;width:120px;height:50px;background:var(--rnv-tinta)"></div>
<div class="bk" style="left:1660px;top:40px;width:250px;height:354px;transform:rotate(6deg)"><img src="{I}tapa_gym.jpg" style="width:100%;height:100%"></div>
<div class="bk" style="left:1920px;top:90px;width:230px;height:325px;transform:rotate(-4deg)"><img src="{I}tapa_pausa.jpg" style="width:100%;height:100%"></div>
<div class="bk" style="left:1470px;top:430px;width:250px;height:354px;transform:rotate(-5deg);z-index:3"><img src="{I}tapa_casa.jpg" style="width:100%;height:100%"></div>
<div class="tab" style="left:1790px;top:450px;width:360px;height:225px"><img src="{I}foto_l_patada.jpg"></div>
<div class="tab" style="left:1790px;top:720px;width:360px;height:225px"><img src="{I}foto_l_pesomuerto.jpg"></div>
<div class="tab" style="left:330px;top:720px;width:370px;height:230px"><img src="{I}foto_l_remo.jpg"></div>
<div class="tab" style="left:720px;top:730px;width:370px;height:230px;z-index:2"><img src="{I}foto_l_subidas.jpg"></div>
<div class="bk" style="left:1100px;top:650px;width:180px;height:255px;transform:rotate(-6deg);z-index:4"><div class="cv" style="background:var(--rnv-tinta)"><div style="padding:12px"><img src="{I}logo.png" style="height:15px;filter:brightness(0) invert(1)"><p class="ttl" style="font-size:19px;margin-top:8px">Nutrición<br>en la<br><span style=\"color:var(--rnv-turquesa)\">menopausia</span></p><p style="color:#fff;font-weight:700;font-size:10px;margin-top:4px">Qué comer en esta etapa</p></div><div style="flex:1;background:url({I}comida_11.jpg) center/cover"></div></div></div>
<div class="bk" style="left:1250px;top:690px;width:180px;height:255px;transform:rotate(0deg);z-index:4"><div class="cv" style="background:var(--rnv-turquesa)"><div style="padding:12px"><img src="{I}logo.png" style="height:15px;filter:brightness(0) invert(1)"><p class="ttl" style="font-size:19px;margin-top:8px">Recetario<br>fácil y<br>saludable</p><p style="color:#fff;font-weight:700;font-size:10px;margin-top:4px">Recetas ricas en proteína</p></div><div style="flex:1;background:url({I}comida_01.jpg) center/cover"></div></div></div>
<div class="bk" style="left:1390px;top:650px;width:180px;height:255px;transform:rotate(7deg);z-index:4"><div class="cv" style="background:var(--rnv-turquesa-profundo)"><div style="padding:12px"><img src="{I}logo.png" style="height:15px;filter:brightness(0) invert(1)"><p class="ttl" style="font-size:19px;margin-top:8px">Plan de<br>nutrición<br>8 semanas</p><p style="color:#fff;font-weight:700;font-size:10px;margin-top:4px">Menús y lista de compras</p></div><div style="flex:1;background:url({I}comida_15.jpg) center/cover"></div></div></div>
"""
Path("nutricion.html").write_text(NUT)
Path("programa.html").write_text(PRO)
print("ok")
