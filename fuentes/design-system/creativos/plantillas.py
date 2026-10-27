"""Plantillas de creativos RENOVA para Instagram y Facebook.

Cada función recibe los datos del producto (datos.py) y una función img() que resuelve las rutas
de las imágenes, y devuelve el HTML del <body>. El estilo está en creativos.css (solo tokens).

Imágenes (1080×1350 y 1080×1920): gancho, antes_despues, incluye, oferta.
Carrusel (1080×1350): carrusel() devuelve una lista de 7 slides.
Videos (1080×1920): video_beneficios, video_testimonio → (html, duración en segundos).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from design_system import ICON_CHECK, ICON_ARROW, DESCARGO, GARANTIA  # noqa: E402


def _tildes(items):
    return '<ul class="lista">' + "".join(f'<li><span class="tilde">{ICON_CHECK}</span><span>{i}</span></li>' for i in items) + "</ul>"


def _top(d, img, derecha=""):
    return f'<div class="top"><img class="logo" src="{img(d["logo"])}" alt="RENOVA">{derecha}</div>'


def _precio(d):
    if not d.get("precio"):
        return '<p class="chico">Acceso inmediato · 100% digital</p>'
    antes = f' <s style="color:var(--rnv-gris);font-size:40px">{d["precio_antes"]}</s>' if d.get("precio_antes") else ""
    return (f'<p style="font-family:var(--rnv-fuente-display);font-weight:900;font-size:96px;color:var(--rnv-tinta);margin:10px 0">'
            f'{d["precio"]}{antes}</p>')


def _garantia():
    return f'<p class="chico">{GARANTIA}</p>' if GARANTIA else ""


# ------------------------------------------------------------------ IMÁGENES
def gancho(d, img, fmt):
    return f'''<div class="lienzo">
  {_top(d, img)}
  <span class="pill">{d["pill"]}</span>
  <h1 class="gancho">{d["gancho"]}</h1>
  <p class="sub">{d["sub"]}</p>
  <div class="tapa-wrap" style="margin:{"40px" if fmt == "1920" else "24px"} 0"><img class="tapa" src="{img(d["tapa"])}" alt=""></div>
  <span class="boton ancho">{d["cta_organico"]} {ICON_ARROW}</span>
</div>'''


def antes_despues(d, img, fmt, i=0):
    t = d["testimonios"][i]
    return f'''<div class="lienzo">
  {_top(d, img)}
  <h1 class="titulo">Ellas ya lo <em>lograron</em></h1>
  <p class="sub" style="margin-bottom:36px">Mujeres que siguieron el método con el equipo RENOVA.</p>
  <div class="ba">
    <figure><img src="{img(t["antes"])}" style="object-position:{t["pos_antes"]}" alt=""><span class="tag">ANTES</span></figure>
    <figure><img src="{img(t["despues"])}" style="object-position:{t["pos_despues"]}" alt=""><span class="tag d">DESPUÉS</span></figure>
  </div>
  <div class="quien"><b>{t["nombre"]}</b><span>{t["resultado"]}</span></div>
  <p class="descargo">{DESCARGO}</p>
</div>'''


def incluye(d, img, fmt):
    return f'''<div class="lienzo">
  {_top(d, img)}
  <h1 class="titulo">Qué incluye <em>{d["nombre"]}</em></h1>
  <div class="card" style="margin-top:44px">{_tildes(d["incluye"])}</div>
  <div style="margin-top:44px"><span class="bonus-tag">3 BONUS DE REGALO</span>
    <div class="chips">{"".join(f'<span class="chip">{b}</span>' for b in d["bonus"])}</div></div>
  <div class="espacio"></div>
  <div class="grilla">{"".join(f'<img src="{img(e)}" alt="">' for e in d["ejercicios"][:3 if fmt == "1350" else 6])}</div>
</div>'''


def oferta(d, img, fmt):
    return f'''<div class="lienzo turquesa">
  {_top(d, img)}
  <h1 class="gancho">Empezá <em>hoy</em></h1>
  <p class="sub">{d["nombre"]}: plan de 8 semanas + video de cada ejercicio + 3 bonus.</p>
  <div class="tapa-wrap" style="margin:40px 0"><img class="tapa" src="{img(d["tapa"])}" alt=""></div>
  {_precio(d)}
  {_garantia()}
  <span class="boton blanco ancho" style="margin-top:24px">{d["cta_anuncio"]} {ICON_ARROW}</span>
</div>'''


IMAGENES = [("1-gancho", gancho), ("2-antes-despues", antes_despues), ("3-que-incluye", incluye), ("4-oferta", oferta)]


# ------------------------------------------------------------------ CARRUSEL (7 slides, 1080×1350)
def carrusel(d, img):
    n = 7
    num = lambda k: f'<span class="contador">{k}/{n}</span>'
    titulo_p, dolores = d["carrusel_problema"]
    t = d["testimonios"][0]
    pq_t, pq_p = d["por_que_fuerza"]
    grilla = lambda k, desde=0: '<div class="grilla">' + "".join(f'<img src="{img(e)}" alt="">' for e in d["ejercicios"][desde:desde + k]) + '</div>'
    return [
        f'''<div class="lienzo">{_top(d, img, num(1))}<span class="pill">{d["pill"]}</span>
  <h1 class="gancho">{d["carrusel_gancho"]}</h1><div class="espacio"></div>{grilla(3)}<span class="desliza" style="margin-top:28px">Deslizá →</span></div>''',
        f'''<div class="lienzo">{_top(d, img, num(2))}<h1 class="titulo">{titulo_p}</h1>
  <div class="card" style="margin-top:48px">{_tildes(dolores)}</div>
  <p class="sub">No te falta voluntad. Te falta un plan pensado para vos.</p><span class="desliza">Deslizá →</span></div>''',
        f'''<div class="lienzo turquesa">{_top(d, img, num(3))}<h1 class="titulo">{pq_t}</h1>
  <p class="sub">{pq_p}</p><div class="espacio"></div>{grilla(3, 3)}<span class="desliza" style="margin-top:28px">Deslizá →</span></div>''',
        f'''<div class="lienzo">{_top(d, img, num(4))}<h1 class="titulo">{d["carrusel_solucion"]}</h1>
  <div class="tapa-wrap" style="margin-top:30px"><img class="tapa" src="{img(d["tapa"])}" alt=""></div><span class="desliza">Deslizá →</span></div>''',
        f'''<div class="lienzo">{_top(d, img, num(5))}<h1 class="titulo">8 semanas en <em>3 fases</em></h1>
  <div class="fases" style="margin-top:44px">{"".join(f'<div class="fase"><span class="n">{k}</span><div><small>{s}</small><b>{f}</b><p>{p}</p></div></div>' for k, (s, f, p) in enumerate(d["fases"], 1))}</div>
  <p class="sub">Cada semana sabés exactamente qué hacer, cuántas vueltas y con qué esfuerzo.</p><span class="desliza">Deslizá →</span></div>''',
        f'''<div class="lienzo">{_top(d, img, num(6))}<h1 class="titulo">Ellas ya lo <em>lograron</em></h1>
  <div class="ba" style="margin-top:40px">
    <figure><img src="{img(t["antes"])}" style="object-position:{t["pos_antes"]}" alt=""><span class="tag">ANTES</span></figure>
    <figure><img src="{img(t["despues"])}" style="object-position:{t["pos_despues"]}" alt=""><span class="tag d">DESPUÉS</span></figure></div>
  <div class="quien"><b>{t["nombre"]}</b><span>{t["resultado"]}</span></div><p class="descargo">{DESCARGO}</p></div>''',
        f'''<div class="lienzo turquesa">{_top(d, img, num(7))}<h1 class="gancho">Empezá <em>hoy</em></h1>
  <p class="sub">{d["nombre"]}: plan de 8 semanas, video de cada ejercicio y 3 bonus.</p>
  <div class="tapa-wrap" style="margin:20px 0"><img class="tapa" src="{img(d["tapa"])}" alt=""></div>{_precio(d)}<span class="boton blanco ancho">{d["cta_organico"]} {ICON_ARROW}</span></div>''',
    ]


# ------------------------------------------------------------------ VIDEOS (1080×1920)
def _esc(s, e, cuerpo, cls=""):
    return f'<div class="esc {cls}" style="--s:{s};--e:{e}">{cuerpo}</div>'


def video_beneficios(d, img):
    """Gancho → 3 beneficios → tapa y CTA. 21 s."""
    b = d["beneficios"]
    escenas = [_esc(0, 4.5, f'''{_top(d, img)}<span class="pill">{d["pill"]}</span><h1 class="gancho">{d["gancho"]}</h1>''')]
    t = 4.5
    for k, (tit, txt) in enumerate(b, 1):
        escenas.append(_esc(t, t + 4, f'''{_top(d, img, f'<span class="contador">{k}/3</span>')}
  <h1 class="gancho" style="margin-top:120px">{tit}</h1><p class="sub sube" style="--s:{t};--d:.5">{txt}</p>
  <div class="grilla sube" style="--s:{t};--d:.9;margin-top:auto">{"".join(f'<img src="{img(e)}" alt="">' for e in d["ejercicios"][(k-1)*2:(k-1)*2+3])}</div>'''))
        t += 4
    escenas.append(_esc(t, t + 4.5, f'''{_top(d, img)}<h1 class="gancho">Empezá <em>hoy</em></h1>
  <div class="tapa-wrap"><img class="tapa zoom" style="--s:{t}" src="{img(d["tapa"])}" alt=""></div>
  <span class="boton ancho sube" style="--s:{t};--d:.6">{d["cta_anuncio"]} {ICON_ARROW}</span>''', "ultima"))
    dur = t + 4.5
    return "".join(escenas) + f'<div class="barra" style="--t:{dur}"><i></i></div>', dur


def video_testimonio(d, img):
    """Resultado → antes → después → más casos → CTA. 22 s."""
    t1, t2 = d["testimonios"][0], d["testimonios"][1]
    r = d["romi"]
    foto = lambda src, pos, tag, cls, s: (f'<figure style="position:relative;flex:1;border-radius:32px;overflow:hidden;box-shadow:var(--rnv-sombra-fuerte);margin-top:40px">'
                                          f'<img class="zoom" style="--s:{s};width:100%;height:100%;object-fit:cover;object-position:{pos}" src="{img(src)}" alt="">'
                                          f'<span class="tag {cls}">{tag}</span></figure>')
    escenas = [
        _esc(0, 4, f'''{_top(d, img)}<span class="pill">Resultados reales</span>
  <h1 class="gancho">{t1["nombre"]}: <em>{t1["resultado"].rstrip(".").lower()}</em></h1><p class="descargo">{DESCARGO}</p>'''),
        _esc(4, 8, f'{_top(d, img)}<h1 class="titulo">Antes</h1>' + foto(t1["antes"], t1["pos_antes"], "ANTES", "", 4)),
        _esc(8, 12, f'{_top(d, img)}<h1 class="titulo"><em>Después</em></h1>' + foto(t1["despues"], t1["pos_despues"], "DESPUÉS", "d", 8)),
        _esc(12, 17, f'''{_top(d, img)}<h1 class="titulo">Y no es <em>la única</em></h1>
  <div class="card sube" style="--s:12;--d:.4;margin-top:50px"><div class="quien" style="margin:0"><b>{t2["nombre"]}</b><span>{t2["resultado"]}</span></div></div>
  <div class="card sube" style="--s:12;--d:1.2;margin-top:30px"><div class="quien" style="margin:0"><b>{r["nombre"]}</b><span>{r["resultado"]}</span></div></div>
  <p class="descargo">{DESCARGO}</p>'''),
        _esc(17, 22, f'''{_top(d, img)}<h1 class="gancho">{d["nombre"]}</h1>
  <div class="tapa-wrap"><img class="tapa zoom" style="--s:17" src="{img(d["tapa"])}" alt=""></div>
  <span class="boton ancho sube" style="--s:17;--d:.6">{d["cta_anuncio"]} {ICON_ARROW}</span>''', "ultima"),
    ]
    return "".join(escenas) + '<div class="barra" style="--t:22"><i></i></div>', 22


VIDEOS = [("video-beneficios", video_beneficios), ("video-testimonio", video_testimonio)]
