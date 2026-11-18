"""Mockup 3D de Repostería Sin TACC con fondo azul (1080×1350 y 1080×1920).
Uso: cd fuentes/landing/mockups && python3 reposteria3d.py && node reposteria3d.js → ../../../sin-tacc-inteligente/creativos/reposteria_mockup*.png"""
import libros3d as L
from pathlib import Path
AZUL = "body{background:radial-gradient(ellipse 60% 50% at 50% 45%,rgba(20,177,199,.55),transparent 70%),linear-gradient(180deg,#0B3C6E,#062448)}"
def page(name, w, h, inner):
    Path(name + ".html").write_text(f'<!doctype html><meta charset="utf-8"><style>{L.CSS}{AZUL}body{{--w:{w}px;--h:{h}px}}</style><div class="grid"></div><div class="st">{inner}</div>')
page("reposteria_mockup", 1080, 1350, L.book("tapa_reposteria.png", "REPOSTERÍA SIN TACC", 250, 240, 600, -22))
page("reposteria_mockup_vertical", 1080, 1920, L.book("tapa_reposteria.png", "REPOSTERÍA SIN TACC", 210, 480, 660, -22))
