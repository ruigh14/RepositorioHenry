"""Versión recreada del reel ganador: pantalla dividida (Nacho arriba, b-roll IA y tapas abajo), subtítulos propios en la unión."""
import json, subprocess
from PIL import Image
R = "/home/user/RepositorioHenry/"
SEG = [(0, 9.22), (12.30, 24.72), (24.70, 28.48), (33.00, 34.84), (35.10, 38.30), (38.50, 41.30), (41.40, 52.98), (52.96, 57.30), (65.80, 71.90)]
starts, t = [], 0
for a, b in SEG: starts.append(t); t += b - a
DUR = t
END = 2.5
# abajo: (archivo, tipo, desde, hasta)
C = R + "pack-renova/carrusel/"
BOT = [("ai1.mp4", "v", 0, 4.6), ("ai2.mp4", "v", 4.6, 9.22),
       (R + "fuentes/landing/img/equipo_tapa.png", "i", 9.22, 13.0), (R + "pack-renova/pack_1.png", "i", 13.0, 16.9),
       (C + "01.png", "i", 16.9, 19.3), (C + "02.png", "i", 19.3, 21.64),
       (R + "pack-renova/libro_1_casa.png", "i", 21.64, 23.5), (R + "pack-renova/libro_2_gimnasio.png", "i", 23.5, 25.42),
       ("ai3.mp4", "v", 25.42, 27.26), ("ai4.mp4", "v", 27.26, 30.46), ("ai5.mp4", "v", 30.46, 33.26),
       (C + "03.png", "i", 33.26, 39.0), ("ai6.mp4", "v", 39.0, 44.84),
       (C + "07.png", "i", 44.84, 47.0), (C + "08.png", "i", 47.0, 49.18),
       (C + "bonus.png", "i", 49.18, 52.2), (R + "pack-renova/pack_1.png", "i", 52.2, DUR)]
# ---------- subtítulos ----------
FIX = {"enganchas": "enganchás", "escúchame.": "escuchame.", "avumiences": "comiences", "toca": "tocá", "Renova,": "RENOVA,", "Renova": "RENOVA", "que hacer": "qué hacer"}
KEY = {"40,", "fuerza,", "gimnasio,", "nada", "internet", "Nacho", "Portillo,", "RENOVA,", "RENOVA", "8", "semanas", "profesionales", "casa", "videos", "fácil", "nivel,", "impacto", "articulaciones.", "nutricionista", "dietas", "talleres", "gratuito", "link,", "hoy"}
W = json.load(open("palabras.json"))
words = []
for i, (a, b) in enumerate(SEG):
    for w in W:
        if a - 0.05 <= w["s"] < b - 0.05:
            txt = FIX.get(w["w"].strip(), w["w"].strip())
            if txt == "que" and words and False: pass
            words.append((starts[i] + w["s"] - a, starts[i] + min(w["e"], b) - a, txt))
for k in range(len(words) - 1):   # "que hacer" → "qué hacer"
    if words[k][2] == "que" and words[k + 1][2].startswith("hacer"): words[k] = (words[k][0], words[k][1], "qué")
def ts(x): h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60; return f"{h}:{m:02d}:{s:05.2f}"
ev, grp = [], []
for w in words:
    grp.append(w)
    if len(grp) == 3 or w[2][-1] in ",.?!":
        ev.append(grp); grp = []
if grp: ev.append(grp)
lines = []
for k, g in enumerate(ev):
    s, e = g[0][0], (ev[k + 1][0][0] if k + 1 < len(ev) else g[-1][1] + 0.3)
    e = min(e, g[-1][1] + 0.6)
    txt = " ".join(("{\\c&H00D4FF&}" + x[2].upper() + "{\\c&HFFFFFF&}") if x[2] in KEY else x[2].upper() for x in g)
    lines.append(f"Dialogue: 0,{ts(s)},{ts(e)},Sub,,0,0,0,,{{\\an5\\pos(540,960)\\fscx80\\fscy80\\t(0,90,\\fscx105\\fscy105)\\t(90,160,\\fscx100\\fscy100)}}{txt}")
lines.append(f"Dialogue: 1,{ts(0)},{ts(3.2)},Hook,,0,0,0,,{{\\an8\\pos(540,1010)}}¿TENÉS MÁS DE 40?")
ass = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Inter Display Black,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,7,2,5,60,60,0,1
Style: Hook,Inter Display Black,84,&H00FFFFFF,&H00FFFFFF,&H00100F0E,&H00100F0E,0,0,0,0,100,100,0,0,3,22,0,8,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(lines) + "\n"
open("recreada.ass", "w").write(ass)
# ---------- video ----------
inp = ["-i", "in.mp4"]; NIN = [1]
f = []
for i, (a, b) in enumerate(SEG):
    f.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS,crop=1080:960:0:0[t{i}];[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={b-a-0.04:.2f}:d=0.04[a{i}]")
n = len(SEG)
f.append("".join(f"[t{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[top][aud]")
f.append(f"color=c=0x0d1416:s=1080x1920:d={DUR}:r=30[bg]")
f.append("[bg][top]overlay=0:0[base0]")
cur = "base0"
for k, (src, typ, s, e) in enumerate(BOT):
    idx = NIN[0]; NIN[0] += 1
    d = e - s
    if typ == "v":
        inp += ["-stream_loop", "-1", "-i", src]
        f.append(f"[{idx}:v]trim=0:{d:.2f},setpts=PTS-STARTPTS+{s}/TB,scale=-2:960,crop=1080:960,setsar=1[b{k}]")
    else:
        im = Image.open(src).convert("RGB"); c = im.getpixel((5, im.height - 5)); col = "0x%02x%02x%02x" % c
        inp += ["-loop", "1", "-framerate", "30", "-t", f"{d:.2f}", "-i", src]
        f.append(f"[{idx}:v]scale=1060:640:force_original_aspect_ratio=decrease,pad=1080:960:(ow-iw)/2:14:color={col},setsar=1,setpts=PTS-STARTPTS+{s}/TB[b{k}]")
    # entra deslizándose desde la derecha en 0,22 s
    f.append(f"[{cur}][b{k}]overlay=x='if(lt(t-{s},0.22),W*(1-(t-{s})/0.22),0)':y=960:enable='between(t,{s},{e})':eof_action=pass[o{k}]")
    cur = f"o{k}"
f.append(f"[{cur}]drawbox=x=0:y=956:w=1080:h=8:color=0xD62828:t=fill,ass=recreada.ass,format=yuv420p[main]")
idx = NIN[0]
inp += ["-loop", "1", "-framerate", "30", "-t", str(END), "-i", R + "pack-renova/pack_1.png"]
f.append(f"[{idx}:v]scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x0d1416,setsar=1,format=yuv420p,fade=t=in:d=0.3[end]")
f.append(f"anullsrc=r=48000:cl=stereo,atrim=0:{END}[sil]")
f.append("[main][aud][end][sil]concat=n=2:v=1:a=1[ov][oa]")
open("recreada.filter", "w").write(";\n".join(f))
cmd = ["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex_script", "recreada.filter", "-map", "[ov]", "-map", "[oa]", "-r", "30",
       "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "recreada.mp4"]
subprocess.run(cmd, check=True)
print("ok", round(DUR + END, 1), "s")
