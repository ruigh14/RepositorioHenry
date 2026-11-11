"""Bonus: Acceso a la comunidad RENOVA (2 hojas: portada + cómo entrar a Skool y ver los talleres).
Uso: cd fuentes/ebook && python3 comunidad.py && node comunidad.js → comunidad/Bonus_Acceso_comunidad_RENOVA.pdf"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "design-system"))
from design_system import css

SKOOL = "https://www.skool.com/renova-entrenamiento-y-salud-1617/about"
L = "../landing/img/"
CSS = css(str(Path(__file__).parent)) + """
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--rnv-fuente);color:var(--rnv-texto)}
.pg{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always}
/* PORTADA */
.cov{background:linear-gradient(165deg,#06343b 0%,var(--rnv-turquesa-profundo) 55%,var(--rnv-turquesa-oscuro) 100%);color:#fff;text-align:center;padding:22mm 18mm 0}
.cov .logo{height:15mm;filter:brightness(0) invert(1)}
.cov .tag{display:inline-block;margin-top:12mm;border:2px solid var(--rnv-turquesa-claro);color:var(--rnv-turquesa-claro);border-radius:999px;padding:2.5mm 7mm;font:800 11pt var(--rnv-fuente-display);letter-spacing:.2em;text-transform:uppercase}
.cov h1{font:900 46pt/0.98 var(--rnv-fuente-display);letter-spacing:-.02em;text-transform:uppercase;margin-top:9mm}
.cov h1 b{color:var(--rnv-turquesa-claro)}
.cov p{font-size:15pt;line-height:1.4;margin:8mm auto 0;max-width:150mm;color:rgba(255,255,255,.9)}
.cov p b{color:var(--rnv-turquesa-claro)}
.cov .ph{position:absolute;left:18mm;right:18mm;bottom:26mm;height:92mm;border-radius:8mm;overflow:hidden;border:2px solid rgba(111,216,230,.6);box-shadow:0 0 30px rgba(20,177,199,.35)}
.cov .ph{background:#fff}
.cov .ph img{width:100%;height:100%;object-fit:contain;object-position:50% 100%}
.cov .ft{position:absolute;left:0;right:0;bottom:10mm;font:800 10.5pt var(--rnv-fuente-display);letter-spacing:.22em;text-transform:uppercase;color:rgba(255,255,255,.8)}
/* HOJA 2 */
.in{padding:18mm 17mm}
.in .eye{font:800 10pt var(--rnv-fuente-display);letter-spacing:.22em;text-transform:uppercase;color:var(--rnv-turquesa-oscuro)}
.in h2{font:900 28pt/1.05 var(--rnv-fuente-display);color:var(--rnv-tinta);letter-spacing:-.02em;margin:2mm 0 4mm}
.in h2 b{color:var(--rnv-turquesa-titulo)}
.in .lead{font-size:14.5pt;line-height:1.45;margin-bottom:6mm}
.st{display:flex;gap:5mm;align-items:flex-start;margin-bottom:5.5mm}
.st i{flex:none;width:11mm;height:11mm;border-radius:50%;background:var(--rnv-degrade);color:#fff;font:900 15pt/11mm var(--rnv-fuente-display);text-align:center;font-style:normal}
.st div{font-size:14pt;line-height:1.42;padding-top:1.5mm}
.st b{color:var(--rnv-tinta)}
.bar{display:flex;gap:2mm;flex-wrap:wrap;margin:3mm 0 0;background:#fff;border:1.5px solid var(--rnv-linea);border-radius:3mm;padding:2.5mm 3mm;box-shadow:0 3px 10px rgba(0,0,0,.06)}
.bar span{font:600 11pt var(--rnv-fuente);padding:1.5mm 3.5mm;border-radius:2mm;color:var(--rnv-gris)}
.bar span.on{background:var(--rnv-turquesa-fondo);color:var(--rnv-turquesa-profundo);font-weight:800;outline:2px solid var(--rnv-turquesa)}
.btn{display:block;margin:7mm auto 0;width:150mm;text-align:center;background:var(--rnv-degrade);color:#fff;text-decoration:none;font:900 16pt var(--rnv-fuente-display);letter-spacing:.04em;text-transform:uppercase;padding:5.5mm;border-radius:4mm;box-shadow:0 8px 20px rgba(20,177,199,.35)}
.url{text-align:center;font-size:10.5pt;color:var(--rnv-gris);margin-top:2.5mm;word-break:break-all}
.note{margin-top:6mm;background:var(--rnv-turquesa-fondo);border-left:4px solid var(--rnv-turquesa);border-radius:2mm;padding:4mm 5mm;font-size:12.5pt;line-height:1.45}
.foot{position:absolute;left:17mm;right:17mm;bottom:10mm;display:flex;justify-content:space-between;font:700 9pt var(--rnv-fuente-display);letter-spacing:.18em;text-transform:uppercase;color:var(--rnv-gris)}
"""

html = f"""<!doctype html><html lang="es-AR"><meta charset="utf-8"><style>{CSS}</style><body>
<section class="pg cov">
  <img class="logo" src="img/logo_renova.png" alt="RENOVA">
  <div><a href="{SKOOL}" style="text-decoration:none"><span class="tag">Bonus · Método RENOVA</span></a></div>
  <h1>Acceso a la<br><b>comunidad</b><br>RENOVA</h1>
  <p>Talleres <b>grabados y en vivo</b> con nuestro equipo, y una comunidad de mujeres en tu misma etapa. <b>Acceso de por vida.</b></p>
  <div class="ph"><img src="{L}comunidad.jpg" alt=""></div>
  <div class="ft">Entrenamiento · Nutrición · Hábitos</div>
</section>
<section class="pg in">
  <div class="eye">Cómo entrar</div>
  <h2>Tu acceso a la <b>comunidad</b> y a los <b>talleres</b></h2>
  <p class="lead">La comunidad RENOVA está en <b>Skool</b>, una plataforma simple que podés usar desde el celular o la computadora. Ahí vas a encontrar todos los talleres del equipo.</p>
  <div class="st"><i>1</i><div><a href="{SKOOL}" style="color:inherit;text-decoration:none"><b>Tocá el botón de abajo</b></a> para entrar a la comunidad RENOVA en Skool.</div></div>
  <div class="st"><i>2</i><div><b>Creá tu cuenta o ingresá</b> con el mismo correo que usaste en la compra y pedí el acceso. Lo aprobamos a la brevedad.</div></div>
  <div class="st"><i>3</i><div>Una vez adentro, mirá la <b>barra de arriba</b>. Ahí tenés varias opciones, y una de ellas es <b>Cursos</b>.
    <div class="bar"><span>Comunidad</span><span class="on">Cursos</span><span>Calendario</span><span>Miembros</span><span>Ranking</span></div></div></div>
  <div class="st"><i>4</i><div>Entrá a <b>Cursos</b> y vas a ver <b>todos los talleres</b> (hábitos, nutrición, mindfulness, sueño y más) para mirarlos cuando quieras.</div></div>
  <a class="btn" href="{SKOOL}">Entrar a la comunidad →</a>
  <p class="url"><a href="{SKOOL}" style="color:inherit">{SKOOL}</a></p>
  <div class="note">En <b>Calendario</b> vas a ver las fechas de los <b>talleres en vivo</b>. Participar en la comunidad es opcional: podés solo mirar los cursos a tu ritmo.</div>
  <div class="foot"><span>Método RENOVA</span><span>Bonus · Comunidad</span></div>
</section>
</body></html>"""
Path(__file__).with_name("comunidad.html").write_text(html)
print("ok")
