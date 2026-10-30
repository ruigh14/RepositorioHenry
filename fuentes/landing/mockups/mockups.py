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
<div class="card" style="left:760px;top:70px;width:220px;height:220px;padding:8px;transform:rotate(-5deg)"><img src="{I}comida_21.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:8px"></div>
"""

PRO = f"""<!doctype html><meta charset="utf-8"><style>{BASE} body{{background:linear-gradient(135deg,var(--rnv-turquesa-fondo),#fff)}}
.ph{{position:absolute;border:10px solid var(--rnv-tinta);border-radius:22px;overflow:hidden;box-shadow:0 22px 44px rgba(20,20,20,.3);background:#000}}
.ph img{{width:100%;height:100%;object-fit:cover}}</style>
<div class="ph" style="left:40px;top:470px;width:300px;height:220px"><img src="{I}foto_remo.jpg"></div>
<div class="ph" style="left:70px;top:150px;width:260px;height:260px;transform:rotate(-4deg)"><img src="{I}foto_estocada.jpg"></div>
<div class="ph" style="left:880px;top:150px;width:260px;height:260px;transform:rotate(4deg)"><img src="{I}foto_patada.jpg"></div>
<div class="ph" style="left:860px;top:470px;width:300px;height:220px"><img src="{I}foto_subidas.jpg"></div>
<div class="bk" style="left:300px;top:150px;width:300px;height:424px;transform:rotate(-6deg)"><img src="{I}tapa_gym.jpg" style="width:100%;height:100%"></div>
<div class="bk" style="left:610px;top:150px;width:300px;height:424px;transform:rotate(6deg)"><img src="{I}tapa_pausa.jpg" style="width:100%;height:100%"></div>
<div class="bk" style="left:420px;top:90px;width:360px;height:509px;z-index:3"><img src="{I}tapa_casa.jpg" style="width:100%;height:100%"></div>
<div class="bk" style="left:330px;top:600px;width:540px;height:270px;z-index:4;border-radius:14px"><img src="{I}mock_nutricion.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<div class="card" style="left:60px;top:740px;width:250px;height:140px;padding:6px"><img src="{I}comida_05.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:8px"></div>
<div class="card" style="left:890px;top:740px;width:250px;height:140px;padding:6px"><img src="{I}habitos.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:8px"></div>
"""
Path("nutricion.html").write_text(NUT)
Path("programa.html").write_text(PRO)
print("ok")
