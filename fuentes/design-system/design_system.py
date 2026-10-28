"""RENOVA · design system — piezas compartidas en Python.

Lo usan el ebook (fuentes/ebook/build.py), la landing (fuentes/landing/build.py),
los creativos (creativos/generar.py) y la muestra (muestra.py).

    import sys; sys.path.insert(0, "<ruta>/fuentes/design-system")
    from design_system import css, esc, eyebrow, ...
"""
import html
import os

DS = os.path.dirname(os.path.abspath(__file__))


def leer(nombre):
    with open(os.path.join(DS, nombre), encoding="utf-8") as f:
        return f.read()


def css(desde, fuentes=True):
    """Tokens (+ tipografías locales) listos para meter en un <style>.

    desde: carpeta del HTML que los va a usar, para armar la ruta relativa a las fuentes.
    fuentes=False: solo los tokens (para la landing, que carga las fuentes de Google).
    """
    out = leer("tokens.css")
    if fuentes:
        rel = os.path.relpath(os.path.join(DS, "fonts"), desde).replace(os.sep, "/")
        out = leer("fuentes.css").replace("FONTS/", rel + "/") + "\n" + out
    return out


def esc(s):
    return html.escape(s, quote=True)


# ---- Íconos (trazo, heredan el color del texto)
ICON_CHECK = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
ICON_ARROW = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ICON_HAND = ('<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M22 14a8 8 0 0 1-8 8"/><path d="M18 11v-1a2 2 0 0 0-4 0"/>'
             '<path d="M14 10V9a2 2 0 0 0-4 0v1"/><path d="M10 9.5V4a2 2 0 0 0-4 0v10"/>'
             '<path d="M18 11a2 2 0 1 1 4 0v3a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-6-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.83L7 15"/></svg>')
ICON_PLAY = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5l11 7-11 7z"/></svg>'
ICON_LOCK = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>'


# ---- Componentes de texto del ebook (clases en fuentes/ebook/style.css)
def eyebrow(t):
    """Etiqueta chica arriba del título (pill)."""
    return f'<span class="pill">{t}</span>'


def chap_head(num, title_html, lead):
    """Apertura de capítulo: número grande, título y bajada."""
    return (f'<div class="chead"><span class="cnum">{num}</span>'
            f'<h1>{title_html}</h1><p class="lead">{lead}</p></div>')


def ul(items, cls="list"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def checks(items):
    """Lista con tildes."""
    return '<ul class="checks">' + "".join(f"<li>{ICON_CHECK}<span>{i}</span></li>" for i in items) + "</ul>"


def box(content, kind=""):
    """Recuadro: kind '' (turquesa claro), 'soft' o 'note'."""
    return f'<div class="box {kind}">{content}</div>'


def block_head(label, info):
    """Encabezado de bloque de rutina: etiqueta negra + datos."""
    return f'<div class="blk"><span>{label}</span><p>{info}</p></div>'


def params(items):
    """Fila de datos: [(etiqueta, valor), ...]."""
    return '<div class="params">' + "".join(f'<div><span>{k}</span><b>{v}</b></div>' for k, v in items) + '</div>'


# ---- Reglas de venta
DESCARGO = "Los resultados dependen de cada persona: tu punto de partida, tu constancia y tu situación de salud."
# Garantía definida por Nacho: 7 días, sin preguntas. Las piezas que la usan la muestran.
GARANTIA = "Garantía de 7 días: si no te gusta el material, te devolvemos el dinero."
