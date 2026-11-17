# RENOVA · 10 creatividades para Meta Ads (1080×1350)
# 5 de testimonios reales (textos y fotos tal cual de las alumnas) + 5 de ebooks y bonus.
# Fondos de producto: img/hf_*.jpg, generados con Higgsfield (GPT Image 2.6), sin texto ni personas.
# Uso: python3 generar.py && ./exportar.sh  → pack-renova/meta-ads/*.png
import os, pathlib
AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parents[3]
L = "../../../landing/img/"          # imágenes de la landing
E = "../../../ebook/img/"            # imágenes del ebook
P = "../../../../pack-renova/"       # mockups del pack
M = "../../../../MATERIAL PARA AUDIOVISUAL PARA EDITAR/imagenes clientes/TESTIMONIOS CLIENTAS/"
F = "../../fonts/"

CSS = f"""
@font-face{{font-family:I;font-weight:400;src:url("{F}inter-latin-400-normal.woff2")}}
@font-face{{font-family:I;font-weight:500;src:url("{F}inter-latin-500-normal.woff2")}}
@font-face{{font-family:I;font-weight:600;src:url("{F}inter-latin-600-normal.woff2")}}
@font-face{{font-family:I;font-weight:700;src:url("{F}inter-latin-700-normal.woff2")}}
@font-face{{font-family:I;font-weight:800;src:url("{F}inter-latin-800-normal.woff2")}}
@font-face{{font-family:I;font-weight:900;src:url("{F}inter-latin-900-normal.woff2")}}
@font-face{{font-family:T;font-weight:100 900;src:url("{F}inter-tight-latin-var.woff2")}}
:root{{--tq:#14B1C7;--tqt:#0E9DB2;--tqo:#0A7F90;--tqp:#075E6B;--tqf:#E8F6F8;--tqb:#CDEEF3;--tqc:#6FD8E6;
--tinta:#141414;--texto:#2A2F33;--gris:#555C62;--osc:#141414;--rojo:#E63333;--oro:#E2A928}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{font-family:I,sans-serif;color:var(--texto);background:#fff;position:relative}}
.c{{position:absolute;inset:0;display:flex;flex-direction:column;padding:64px 64px 56px}}
.eye{{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;font:800 26px/1 I;letter-spacing:.14em;text-transform:uppercase;color:var(--tqo);background:var(--tqf);border:2px solid var(--tqb);padding:14px 22px;border-radius:999px}}
.eye.d{{color:var(--tqc);background:rgba(20,177,199,.12);border-color:rgba(111,216,230,.35)}}
.eye.w{{color:#fff;background:var(--tq);border-color:var(--tq)}}
h1{{font:900 84px/1.0 T,sans-serif;letter-spacing:-.025em;color:var(--tinta);margin-top:26px}}
h1 .t{{color:var(--tqt)}} h1 .hl{{white-space:nowrap;display:inline-block;line-height:1.02;margin-top:10px;background:var(--tq);color:#fff;padding:0 14px;border-radius:10px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.d h1,h1.d{{color:#fff}} .d h1 .t{{color:var(--tqc)}}
.sub{{font:600 38px/1.25 I;color:var(--gris);margin-top:18px}}
.d .sub{{color:rgba(255,255,255,.82)}}
.stars{{color:var(--oro);font-size:40px;letter-spacing:4px}}
.btn{{display:inline-flex;align-items:center;gap:16px;background:var(--tq);color:#fff;font:900 36px/1 T;letter-spacing:.04em;padding:28px 46px;border-radius:999px;box-shadow:0 14px 30px rgba(20,177,199,.38),inset 0 -4px 0 rgba(0,0,0,.12)}}
.btn svg{{width:34px;height:34px}}
.foot{{display:flex;align-items:center;justify-content:space-between;margin-top:auto}}
.logo{{height:58px}}
.logo.k{{height:46px;background:#fff;padding:10px 16px;border-radius:14px;box-sizing:content-box}}
.disc{{font:500 20px/1.3 I;color:#7a8288;margin-top:16px}}
.d .disc{{color:rgba(255,255,255,.55)}}
.ok{{display:flex;flex-direction:column;gap:16px;margin-top:28px}}
.ok div{{display:flex;gap:16px;align-items:flex-start;font:600 36px/1.2 I;color:var(--texto)}}
.ok b{{color:var(--tinta);font-weight:800}}
.ok i{{flex:none;width:44px;height:44px;border-radius:50%;background:var(--tq);display:grid;place-items:center;margin-top:-2px}}
.ok i svg{{width:26px;height:26px}}
.d .ok div{{color:rgba(255,255,255,.9)}} .d .ok b{{color:#fff}}
/* WhatsApp */
.wa{{background:#fff;border-radius:28px;padding:30px 34px 22px;font:500 36px/1.36 I;color:#111b21;position:relative;box-shadow:0 18px 44px rgba(20,20,20,.14)}}
.wa:before{{content:"";position:absolute;left:-14px;top:0;border-top:26px solid #fff;border-left:26px solid transparent}}
.wa .h{{font:700 26px/1 I;color:#0A7F90;margin-bottom:12px}}
.wa .tm{{text-align:right;font:500 22px/1 I;color:#667781;margin-top:8px}}
.wa.dk{{background:#202c33;color:#e9edef}} .wa.dk:before{{border-top-color:#202c33}} .wa.dk .tm{{color:#8696a0}} .wa.dk .h{{color:#53bdeb}}
.firma{{display:flex;align-items:center;gap:18px;margin-top:22px;font:800 32px/1.2 I;color:var(--tinta)}}
.firma small{{display:block;font:600 26px/1.2 I;color:var(--gris)}}
.firma img{{width:84px;height:84px;border-radius:50%;object-fit:cover;border:4px solid var(--tq)}}
/* antes / después */
.ba{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:30px;flex:1;min-height:0}}
.ba div{{position:relative;border-radius:26px;overflow:hidden;background:#ddd}}
.ba img{{width:100%;height:100%;object-fit:cover;display:block}}
.ba span{{position:absolute;left:18px;top:18px;font:900 26px/1 T;letter-spacing:.12em;color:#fff;background:rgba(20,20,20,.78);padding:12px 18px;border-radius:999px}}
.ba span.dd{{background:var(--tq)}}
.chip{{position:absolute;z-index:3;background:#fff;border-radius:22px;padding:18px 26px;box-shadow:0 18px 40px rgba(0,0,0,.22);font:900 56px/1 T;color:var(--tqt);letter-spacing:-.02em}}
.chip small{{display:block;font:700 24px/1.15 I;color:var(--texto);letter-spacing:0;margin-top:6px}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.tapa{{border-radius:6px 14px 14px 6px;box-shadow:-2px 0 0 #0E9DB2, 0 30px 60px rgba(0,0,0,.35),0 8px 18px rgba(0,0,0,.2);transform:perspective(1600px) rotateY(-14deg);display:block}}
.pills{{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}}
.pills span{{font:800 28px/1 I;color:var(--tqp);background:var(--tqf);border:2px solid var(--tqb);padding:14px 20px;border-radius:999px}}
.d .pills span{{color:#fff;background:rgba(255,255,255,.08);border-color:rgba(111,216,230,.4)}}
"""

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
LOGO = E + "logo_renova.png"
LOGO_B = L + "logo.png"

def ok(*items):
    return '<div class="ok">' + "".join(f'<div><i>{CHECK}</i><span>{t}</span></div>' for t in items) + "</div>"

def btn(t="EMPEZÁ HOY"):
    return f'<span class="btn">{t} {ARROW}</span>'

def foot(cta="EMPEZÁ HOY", dark=False, disc=True):
    d = '<p class="disc">Resultados reales de alumnas. Dependen de cada persona: punto de partida, constancia y salud.</p>' if disc else ""
    return f'<div class="foot"><img class="logo{" k" if dark else ""}" src="{LOGO}">{btn(cta)}</div>{d}'

def page(body, extra_css="", cls=""):
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}{extra_css}</style></head><body class="{cls}">{body}</body></html>'

P_ = {}

# ---------------- TESTIMONIOS ----------------
# 1 · Mari: antes/después + datos verificados (landing y ebook: 8 kg de grasa y 10 cm de cintura)
P_["01_testimonio_mari"] = page(f'''
<div class="c">
  <span class="eye">Resultado real · Alumna RENOVA</span>
  <h1>Mari bajó <span class="t">8 kg de grasa</span> y <span class="t">10 cm</span> de cintura</h1>
  <div class="ba" style="position:relative">
    <div><img src="{L}mari_a.jpg" style="object-position:52% 35%"><span>ANTES</span></div>
    <div><img src="{L}mari_d.jpg" style="object-position:58% 35%"><span class="dd">DESPUÉS</span></div>
  </div>
  <p class="sub" style="color:var(--texto);margin-top:24px">Con <b>entrenamiento de fuerza</b> y orden en la alimentación. Sin dietas extremas.</p>
  <div style="margin-top:24px">{foot()}</div>
</div>''')

# 2 · Moni: antes/después (6 kg y el hábito de entrenar)
P_["02_testimonio_moni"] = page(f'''
<div class="c" style="background:var(--tqf)">
  <span class="eye w">Resultado real · Alumna RENOVA</span>
  <h1>Moni bajó <span class="t">6 kg</span> y logró <span class="t">el hábito</span> de entrenar</h1>
  <div class="ba">
    <div><img src="{L}moni_antes_al.jpg" style="object-position:50% 40%"><span>ANTES</span></div>
    <div><img src="{L}moni_despues_al.jpg" style="object-position:50% 40%"><span class="dd">DESPUÉS</span></div>
  </div>
  <p class="sub" style="color:var(--texto);margin-top:24px">Rutinas cortas de fuerza para tu semana real.</p>
  <div style="margin-top:24px">{foot()}</div>
</div>''')

# 3 · Romi: WhatsApp textual (ganador 1) + foto real de su media maratón
P_["03_testimonio_romi"] = page(f'''
<img class="bg" src="{L}ba_romi.jpg" style="object-position:50% 42%">
<div class="ov-romi" style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,94,107,1) 0%,rgba(7,94,107,.99) 21%,rgba(7,94,107,0) 34%,rgba(20,20,20,0) 50%,rgba(20,20,20,.9) 78%,rgba(20,20,20,.95) 100%)"></div>
<div class="c d">
  <span class="eye w">Fuerza para mujeres</span>
  <h1 style="font-size:78px">“Me siento <span class="t">bárbara</span> en todos los deportes”</h1>
  <div class="wa" style="margin-top:auto;width:900px;font-size:31px;padding:24px 30px 18px">
    <div class="h">Romi</div>
    Nooo yo nose pero posta que comencé el gym ya metimos 2 semanas completa y yo me siento bárbara en todos los deportes. Hoy tuve una clase de tenis 🎾 y no sabes lo bien que llegué a todas las pelotas. 🎾 Gracias Nacho. Impecable el plan 🙌
    <div class="tm">9:03 p. m.</div>
  </div>
  <div style="margin-top:22px">
    <p style="font:800 32px/1.25 I;color:#fff">Romi ganó masa muscular y volvió a correr <span style="color:var(--tqc)">sin dolores</span>.</p>
    <div style="margin-top:26px">{foot(dark=True)}</div>
  </div>
</div>''')

# 4 · Daniela: WhatsApp textual (constancia + bajó de peso y medidas en un mes)
P_["04_testimonio_daniela"] = page(f'''
<div class="c" style="background:linear-gradient(180deg,#fff 0%,var(--tqf) 100%)">
  <span class="eye">Testimonio real · Alumna RENOVA</span>
  <h1 style="font-size:80px">“Antes arrancaba y <span class="t">no lo podía sostener</span>”</h1>
  <div class="wa dk" style="margin-top:34px;font-size:34px">
    <div class="h">Daniela</div>
    Antes arrancaba en hacer algo y no lo podia sostener, la primer semana bien y ya la segunda por una o por otra razon siempre encontraba la excusa y lo dejaba, ahora estoy a un mes que vengo y sigo con ganas.<br>En cuanto a lo fisico baje de peso y medidas eso te motiva, ver resultados.<br>La adaptacion a la rutina con pocos tiempos es cuestion de dejar de poner excusas porque entre 30 o 50 min todos tenemos, es querer hacerlo.
    <div class="tm">12:42</div>
  </div>
  <div class="pills"><span>1 mes sin abandonar</span><span>Bajó peso y medidas</span><span>30 a 50 min</span></div>
  <div class="firma" style="margin-top:34px"><img src="{L}nacho.jpg" style="object-position:50% 20%"><div>Nacho Portillo<small>Entrenador · creador de RENOVA</small></div></div>
  <div style="margin-top:auto">{foot()}</div>
</div>''')

# 5 · Alumna del ebook: WhatsApp textual (fragmento, sin la parte de acompañamiento)
P_["05_testimonio_ebook"] = page(f'''
<img class="bg" src="img/hf_casa.jpg" style="object-position:50% 100%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,255,255,.97) 0%,rgba(255,255,255,.93) 55%,rgba(255,255,255,.35) 80%,rgba(255,255,255,.1) 100%)"></div>
<div class="c">
  <span class="eye">Lo que nos escriben</span>
  <h1 style="font-size:80px">“Me resultó <span class="t">muuuy fácil</span> de seguir”</h1>
  <div class="wa" style="margin-top:34px;font-size:34px;background:#d9fdd3">
    <div class="h" style="color:#075E6B">Alumna RENOVA, sobre el ebook</div>
    Me resultó muuuy fácil de seguir y adaptar a mi rutina (…) pude alcanzar mis objetivos y bajar de peso sin hacer cambios imposibles. Lo que más me gustó es que aprendí a cuidar mi cuerpo desde un lugar más saludable, sin presiones y disfrutando el proceso. Lo re recomiendo!
    <div class="tm">7:28 p. m.</div>
  </div>
  <div style="display:flex;align-items:flex-end;gap:30px;margin-top:auto">
    <img class="tapa" src="{L}tapa_casa.jpg" style="width:250px">
    <div style="flex:1">
      <p style="font:800 34px/1.25 I;color:var(--tinta);background:rgba(255,255,255,.92);padding:16px 20px;border-radius:18px">Para mujeres que andan corriendo todo el día, con poco tiempo para ellas.</p>
      <div style="margin-top:22px">{btn()}</div>
    </div>
  </div>
  <div style="display:flex;justify-content:space-between;align-items:center;margin-top:22px"><img class="logo" src="{LOGO}" style="height:50px"><p class="disc" style="margin:0;color:#3b4247;text-align:right">Resultados reales. Dependen de cada persona.</p></div>
</div>''')

# ---------------- EBOOKS Y BONUS ----------------
P_["06_pack_completo"] = page(f'''
<img class="bg" src="img/hf_estudio.jpg">
<div class="c d" style="align-items:center;text-align:center">
  <img class="logo k" src="{LOGO}">
  <h1 style="font-size:92px;margin-top:30px">3 ebooks <span class="t">+ 5 bonus</span></h1>
  <p class="sub" style="margin-top:14px">Entrenamiento y alimentación para mujeres de 35+, en un solo pack.</p>
  <img src="{P}pack_libros.png" style="width:860px;margin:-10px 0 -150px">
  <div class="pills" style="justify-content:center;margin-top:0;transform:scale(.92)">
    <span>Entrená desde casa</span><span>Entrená en el gimnasio</span><span>Alimentación Inteligente</span>
  </div>
  <p style="font:700 27px/1.3 I;color:#fff;margin-top:16px;text-shadow:0 2px 10px rgba(0,0,0,.6)">+ Pausa activa · Rutinas express · Abdominales · Talleres · Comunidad</p>
  <div style="margin-top:auto;display:flex;flex-direction:column;align-items:center;gap:16px">
    {btn("QUIERO EL PACK")}
    <p style="font:700 26px/1 I;color:rgba(255,255,255,.75)">Acceso inmediato · Lo descargás en el celular</p>
  </div>
</div>''')

P_["07_ebook_casa"] = page(f'''
<img class="bg" src="img/hf_casa.jpg">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,255,255,.96) 0%,rgba(255,255,255,.9) 38%,rgba(255,255,255,0) 64%)"></div>
<div class="c">
  <span class="eye">Ebook 1 · Entrená desde casa</span>
  <h1>Volvé a sentirte <span class="hl">fuerte</span> sin salir de tu casa</h1>
  <p class="sub">Sesiones de <b style="color:var(--tinta)">30 minutos</b>, de bajo impacto, con lo que tenés a mano.</p>
  <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-top:auto">
    <div style="background:rgba(255,255,255,.95);border-radius:26px;padding:26px 30px 30px;box-shadow:0 18px 40px rgba(0,0,0,.14);width:560px">
      <div class="ok" style="margin-top:0;gap:14px">
        <div style="font-size:31px"><i>{CHECK}</i><span><b>3 rutinas</b> de fuerza</span></div>
        <div style="font-size:31px"><i>{CHECK}</i><span>Plan de <b>8 semanas</b></span></div>
        <div style="font-size:31px"><i>{CHECK}</i><span><b>Video</b> de cada ejercicio</span></div>
      </div>
      <div style="margin-top:26px">{btn()}</div>
    </div>
    <img class="tapa" src="{L}tapa_casa.jpg" style="width:340px;margin-right:4px">
  </div>
  <div style="display:flex;justify-content:space-between;align-items:center;margin-top:24px"><img class="logo" src="{LOGO}" style="height:50px;background:rgba(255,255,255,.9);padding:8px 14px;border-radius:12px;box-sizing:content-box"><span style="font:800 26px/1 I;color:#fff;background:var(--osc);padding:12px 18px;border-radius:999px">Acceso inmediato</span></div>
</div>''')

P_["08_ebook_gimnasio"] = page(f'''
<img class="bg" src="img/hf_gym.jpg">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,20,20,.88) 0%,rgba(20,20,20,.7) 40%,rgba(20,20,20,.15) 65%,rgba(20,20,20,.75) 100%)"></div>
<div class="c d">
  <span class="eye d">Ebook 2 · Entrená en el gimnasio</span>
  <h1>Llegá al gimnasio y <span class="t">sabé exactamente</span> qué hacer</h1>
  <p class="sub">Rutinas de nivel inicial, máquina por máquina, pensadas para mujeres de 35+.</p>
  <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-top:auto">
    <div style="width:560px;background:rgba(20,20,20,.82);border:2px solid rgba(111,216,230,.3);border-radius:26px;padding:26px 30px 30px">
      <div class="ok" style="gap:14px;margin-top:0">
        <div style="font-size:31px"><i>{CHECK}</i><span><b>3 rutinas</b> de 45 minutos</span></div>
        <div style="font-size:31px"><i>{CHECK}</i><span>Plan de <b>8 semanas</b></span></div>
        <div style="font-size:31px"><i>{CHECK}</i><span><b>Video</b> de cada ejercicio</span></div>
      </div>
      <div style="margin-top:28px">{btn()}</div>
    </div>
    <img class="tapa" src="{L}tapa_gym.jpg" style="width:340px">
  </div>
  <div style="display:flex;justify-content:space-between;align-items:center;margin-top:24px"><img class="logo k" src="{LOGO}"><span style="font:800 26px/1 I;color:var(--tinta);background:#fff;padding:12px 18px;border-radius:999px">Acceso inmediato</span></div>
</div>''')

P_["09_ebook_alimentacion"] = page(f'''
<img class="bg" src="img/hf_nutri.jpg" style="object-position:50% 100%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,255,255,.97) 0%,rgba(255,255,255,.9) 36%,rgba(255,255,255,0) 58%)"></div>
<div class="c">
  <span class="eye">Ebook 3 · Alimentación Inteligente</span>
  <h1>Comé mejor, <span class="hl">sin dietas</span></h1>
  <p class="sub">Un plan de <b style="color:var(--tinta)">8 semanas</b> para tu semana real, hecho con nuestra nutricionista.</p>
  <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-top:auto">
    <div style="background:rgba(255,255,255,.95);border-radius:26px;padding:26px 30px 30px;box-shadow:0 18px 40px rgba(0,0,0,.16);width:560px">
      <div class="ok" style="margin-top:0;gap:14px">
        <div style="font-size:31px"><i>{CHECK}</i><span><b>38 recetas</b> fáciles</span></div>
        <div style="font-size:31px"><i>{CHECK}</i><span><b>Menús</b> semana a semana</span></div>
        <div style="font-size:31px"><i>{CHECK}</i><span><b>Listas de compras</b></span></div>
      </div>
      <div style="margin-top:26px">{btn()}</div>
    </div>
    <img class="tapa" src="{L}tapa_nutricion.jpg" style="width:330px">
  </div>
  <div style="display:flex;justify-content:space-between;align-items:center;margin-top:24px"><img class="logo" src="{LOGO}" style="height:50px;background:rgba(255,255,255,.92);padding:8px 14px;border-radius:12px;box-sizing:content-box"><span style="font:700 24px/1.2 I;color:var(--tinta);background:rgba(255,255,255,.92);padding:10px 16px;border-radius:12px">Lic. María Eugenia Ballini · M.N. 11773</span></div>
</div>''')

BON = [("Pausa activa", "4 rutinas de 10 minutos para tu día"),
       ("Rutinas express", "para las semanas con poco tiempo"),
       ("Abdominales", "rutinas extra de zona media"),
       ("Talleres", "con el equipo RENOVA, grabados y en vivo"),
       ("Comunidad RENOVA", "cursos y talleres en Skool")]
P_["10_bonus"] = page(f'''
<img class="bg" src="img/hf_oficina.jpg" style="object-position:50% 100%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,255,255,.97) 0%,rgba(255,255,255,.94) 62%,rgba(255,255,255,.55) 100%)"></div>
<div class="c">
  <span class="eye w">Incluidos en el pack</span>
  <h1 style="font-size:76px">Además te llevás <span class="t">5 bonus</span></h1>
  <p class="sub">Para que entrenar entre en tu día, aunque trabajes muchas horas sentada.</p>
  <div style="display:flex;gap:28px;margin-top:30px;align-items:flex-start">
    <div style="flex:1;display:flex;flex-direction:column;gap:14px">
      {"".join(f'<div style="display:flex;gap:18px;align-items:center;background:#fff;border:2px solid var(--tqb);border-radius:22px;padding:16px 20px;box-shadow:0 8px 22px rgba(20,20,20,.06)"><b style="flex:none;width:58px;height:58px;border-radius:16px;background:var(--tq);color:#fff;display:grid;place-items:center;font:900 32px/1 T">{i+1}</b><span style="font:600 25px/1.22 I;color:var(--gris)"><b style="display:block;font:800 31px/1.15 I;color:var(--tinta)">{t}</b>{s}</span></div>' for i,(t,s) in enumerate(BON))}
    </div>
    <img class="tapa" src="{L}tapa_pausa.jpg" style="width:270px;margin-top:20px">
  </div>
  <div style="margin-top:auto">{foot("QUIERO MIS BONUS", disc=False)}</div>
</div>''')

# Historias y Reels (1080×1920): mismo diseño, con las zonas seguras de Instagram
# (arriba ~250 px y abajo ~340 px quedan tapados por el perfil y los botones).
HISTORIA = """
html,body{height:1920px}
.c{padding:210px 64px 290px}
h1{font-size:92px}
.sub{font-size:40px}
.ov-romi{background:linear-gradient(180deg,rgba(7,94,107,1) 0%,rgba(7,94,107,1) 25%,rgba(7,94,107,0) 33%,rgba(20,20,20,0) 50%,rgba(20,20,20,.9) 74%,rgba(20,20,20,.96) 100%)!important}
"""
for n, h in P_.items():
    (AQUI / f"{n}.html").write_text(h, encoding="utf-8")
    (AQUI / f"h_{n}.html").write_text(h.replace("height:1350px", "height:1920px").replace("</style>", HISTORIA + "</style>", 1), encoding="utf-8")
print(len(P_), "html × 2 formatos")
