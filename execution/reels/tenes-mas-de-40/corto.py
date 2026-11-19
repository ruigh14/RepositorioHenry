"""Versión corta del reel ganador (≈50 s). Cortes en pausas; el subtítulo quemado del original se adelanta ~0,3 s a la voz,
así que en el final de cada tramo se congela la franja de subtítulos (y 960-1300) desde el cambio hasta el corte.
Transiciones: zoom alternado por tramo (1,00 / 1,08) + destello en cada unión (fuerte en gancho → presentación)."""
import subprocess
# (inicio, fin, momento en que el subtítulo quemado cambia a la frase siguiente o None)
SEG = [(0.0, 9.22, 9.05), (12.30, 28.48, 28.15), (33.00, 41.19, None),
       (41.40, 48.70, 48.25), (51.26, 57.30, 57.10), (67.55, 71.62, None)]
FONT = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
for i, (a, b, sw) in enumerate(SEG):
    if sw:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{sw-0.05:.2f}", "-i", "in.mp4", "-frames:v", "1", "-vf", "crop=1080:340:0:960", f"banda{i}.png"], check=True)
inp, f, n_in = ["-i", "in.mp4"], [], 1
out_t, joins = 0, []
for i, (a, b, sw) in enumerate(SEG):
    d = b - a
    f.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[r{i}]")
    src = f"r{i}"
    if sw:
        inp += ["-loop", "1", "-framerate", "30", "-t", f"{d:.2f}", "-i", f"banda{i}.png"]
        f.append(f"[{src}][{n_in}:v]overlay=0:960:enable='gte(t,{sw-a-0.03:.2f})'[f{i}]"); src = f"f{i}"; n_in += 1
    z = 1.0 if i % 2 == 0 else 1.08
    f.append(f"[{src}]crop=iw/{z}:ih/{z}:(iw-iw/{z})/2:(ih-ih/{z})*0.35,scale=1080:1920,setsar=1[v{i}]")
    f.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={d-0.05:.2f}:d=0.05[a{i}]")
    out_t += d
    if i < len(SEG) - 1: joins.append(out_t)
n = len(SEG)
f.append("".join(f"[v{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[cv][ca]")
E = "enable='lt(t,3.4)'"
fx = [f"drawbox=x=90:y=252:w=900:h=112:color=0x0E0F10@0.88:t=fill:{E}",
      f"drawtext=fontfile={FONT}:text='¿TENÉS MÁS DE 40?':fontcolor=white:fontsize=74:x=(w-text_w)/2:y=272:{E}"]
for k, T in enumerate(joins):   # destello: fuerte en la primera unión (gancho → presentación), leve en el resto
    peak = 0.55 if k == 0 else 0.28
    fx.append(f"drawbox=x=0:y=0:w=iw:h=ih:color=white@{peak}:t=fill:enable='between(t,{T:.3f},{T+0.06:.3f})'")
    fx.append(f"drawbox=x=0:y=0:w=iw:h=ih:color=white@{peak/2:.2f}:t=fill:enable='between(t,{T+0.06:.3f},{T+0.14:.3f})'")
f.append("[cv]" + ",".join(fx) + ",format=yuv420p[hv]")
inp += ["-loop", "1", "-framerate", "30", "-t", "2.5", "-i", "/home/user/RepositorioHenry/pack-renova/pack_1.png"]
f.append(f"[{n_in}:v]scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x0d1416,setsar=1,format=yuv420p,fade=t=in:d=0.4[end]")
f.append("anullsrc=r=48000:cl=stereo,atrim=0:2.5[sil]")
f.append("[hv][ca][end][sil]concat=n=2:v=1:a=1[ov][oa]")
open("corto.filter", "w").write(";\n".join(f))
subprocess.run(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex_script", "corto.filter", "-map", "[ov]", "-map", "[oa]", "-r", "30",
                "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "corto.mp4"], check=True)
print("uniones", [round(j, 2) for j in joins], "duración", round(out_t + 2.5, 1))
