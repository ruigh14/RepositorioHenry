#!/usr/bin/env python3
"""Edita un video a cámara (vertical 1080x1920) como reel de Instagram con el estilo RENOVA.

Pasos (todo determinista, con ffmpeg):
  1. Transcribe con faster-whisper (palabra por palabra) o reutiliza la transcripción guardada.
  2. Corta lo que queda fuera de [inicio, fin] y acorta los silencios.
  3. Subtítulos en bloques de 1 a 3 palabras, en mayúsculas, con palabras clave en turquesa.
  4. Gancho arriba al principio, cartel de oferta al final e imagen del producto en el medio.
  5. Audio normalizado a -14 LUFS (lo que pide Instagram) y exportación H.264 + AAC.

Uso:
    python3 execution/editar_reel.py --config execution/reels/te-cuesta-comer-bien.json

Necesita: ffmpeg con libass, la fuente "Inter Display" instalada y `pip install faster-whisper`.
La primera transcripción descarga el modelo desde huggingface.co (y us.aws.cdn.hf.co); exportar
HF_HUB_DISABLE_XET=1 para que no use cas-server.xethub.hf.co.
Directiva: directives/editar_reel.md
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W, H, FPS = 1080, 1920, 30
TURQUESA = "&HC7B114&"      # #14B1C7 en formato ASS (&HBBGGRR&)
TINTA = "&H141414&"
ZONA_ARRIBA, ZONA_ABAJO = 250, 340   # zonas seguras de reels (tokens.css)


def run(cmd):
    subprocess.run(cmd, check=True)


def transcribir(video, destino, modelo):
    from faster_whisper import WhisperModel
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(video), "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, check=True).stdout
    audio = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    segs, _ = WhisperModel(modelo, device="cpu", compute_type="int8").transcribe(audio, language="es", word_timestamps=True)
    palabras = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3)} for s in segs for w in s.words]
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(palabras, ensure_ascii=False, indent=1))
    return palabras


def tramos(palabras, pausa_max, margen):
    """Intervalos del original que se conservan: el habla, con los silencios largos acortados."""
    out = []
    for p in palabras:
        a, b = p["s"] - margen, p["e"] + margen
        if out and a - out[-1][1] <= pausa_max:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([max(a, 0), b])
    return out


def a_nuevo(t, cortes):
    """Pasa un tiempo del original a la línea de tiempo editada."""
    acc = 0.0
    for a, b in cortes:
        if t < a:
            return acc
        if t <= b:
            return acc + t - a
        acc += b - a
    return acc


def ts(t):
    t = max(t, 0)
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


def norm(w):
    return re.sub(r"[^\wáéíóúñü]", "", w.lower())


def bloques(palabras, max_pal, max_car):
    grupo = []
    for p in palabras:
        texto = " ".join(x["w"] for x in grupo + [p])
        if grupo and (len(grupo) >= max_pal or len(texto) > max_car):
            yield grupo
            grupo = []
        grupo.append(p)
        if re.search(r"[.,?!]$", p["w"]):
            yield grupo
            grupo = []
    if grupo:
        yield grupo


def ass(cfg, palabras, cortes, dur):
    fuente = cfg.get("fuente", "Inter Display Black")
    y_sub = cfg.get("subtitulos_y", 1440)
    lineas = [
        "[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}", "WrapStyle: 2", "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
        f"Style: Sub,{fuente},92,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,7,3,2,60,60,{H - y_sub},1",
        f"Style: Cartel,{fuente},76,&H00FFFFFF,&H00FFFFFF,&H00{TURQUESA[2:-1]},&H00000000,0,0,0,0,100,100,0,0,3,22,0,8,60,60,{ZONA_ARRIBA + 60},1",
        "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ]
    fix = {k.lower(): v for k, v in cfg.get("correcciones", {}).items()}
    destacar = {norm(w) for w in cfg.get("destacar", [])}
    lista = list(bloques(palabras, cfg.get("max_palabras", 3), cfg.get("max_caracteres", 16)))
    for i, g in enumerate(lista):
        ini = a_nuevo(g[0]["s"], cortes)
        fin = a_nuevo(lista[i + 1][0]["s"], cortes) if i + 1 < len(lista) else dur
        fin = min(fin, a_nuevo(g[-1]["e"], cortes) + 0.6)
        partes = []
        for p in g:
            w = fix.get(norm(p["w"]), p["w"])
            w = re.sub(r"[.,]$", "", w).upper()
            partes.append(f"{{\\c{TURQUESA}}}{w}{{\\c&HFFFFFF&}}" if norm(p["w"]) in destacar else w)
        pop = "{\\fscx82\\fscy82\\t(0,90,\\fscx100\\fscy100)}"
        lineas.append(f"Dialogue: 0,{ts(ini)},{ts(fin)},Sub,,0,0,0,,{pop}{' '.join(partes)}")
    for c in cfg.get("carteles", []):
        ini = 0 if c.get("desde") is None else a_nuevo(c["desde"], cortes)
        fin = dur if c.get("hasta") is None else a_nuevo(c["hasta"], cortes)
        texto = c["texto"].replace("\n", "\\N")
        if c.get("tamano"):
            texto = f"{{\\fs{c['tamano']}}}" + texto
        entra = "{\\fad(120,120)\\fscx90\\fscy90\\t(0,140,\\fscx100\\fscy100)}"
        lineas.append(f"Dialogue: 1,{ts(ini)},{ts(fin)},Cartel,,0,0,0,,{entra}{texto}")
    return "\n".join(lineas) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True)
    ap.add_argument("--retranscribir", action="store_true", help="Volver a transcribir aunque exista la transcripción")
    args = ap.parse_args()
    cfg_path = Path(args.config)
    cfg = json.loads(cfg_path.read_text())
    base = cfg_path.parent
    video = (base / cfg["video"]).resolve() if not Path(cfg["video"]).is_absolute() else Path(cfg["video"])
    tmp = ROOT / ".tmp" / cfg_path.stem
    tmp.mkdir(parents=True, exist_ok=True)
    salida = ROOT / cfg.get("salida", f".tmp/{cfg_path.stem}.mp4")

    trans = tmp / "palabras.json"
    palabras = json.loads(trans.read_text()) if trans.exists() and not args.retranscribir \
        else transcribir(video, trans, cfg.get("modelo", "medium"))
    ini, fin = cfg.get("inicio", 0), cfg.get("fin", 1e9)
    palabras = [p for p in palabras if p["s"] >= ini and p["e"] <= fin]
    if not palabras:
        sys.exit("ERROR: no quedan palabras entre inicio y fin")

    cortes = tramos(palabras, cfg.get("pausa_max", 0.3), cfg.get("margen", 0.1))
    if cfg.get("cierre"):   # que la transición empiece cuando termina de hablar, no encima de la última frase
        cortes[-1][1] = min(cortes[-1][1] + cfg["cierre"].get("transicion", 0.4), fin)
    dur = sum(b - a for a, b in cortes)
    (tmp / "subs.ass").write_text(ass(cfg, palabras, cortes, dur))

    # Video y audio: recorte de cada tramo y concatenación.
    f = []
    for i, (a, b) in enumerate(cortes):
        f.append(f"[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS[v{i}];[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[a{i}]")
    f.append("".join(f"[v{i}][a{i}]" for i in range(len(cortes))) + f"concat=n={len(cortes)}:v=1:a=1[vc][ac]")
    f.append(f"[vc]scale={W}:{H},fps={FPS},eq=contrast=1.04:saturation=1.08[vb]")
    entradas = ["-i", str(video)]
    ult = "vb"
    for k, img in enumerate(cfg.get("imagenes", []), start=1):
        a = a_nuevo(img["desde"], cortes)
        b = dur if img.get("hasta") is None else a_nuevo(img["hasta"], cortes)
        d = b - a
        entradas += ["-loop", "1", "-t", f"{d:.3f}", "-i", str((base / img["archivo"]).resolve())]
        if img.get("bajar"):   # pantalla dividida: la imagen entra desde arriba y el video baja, sin tapar la cabeza
            fondo, alto, baja = img.get("fondo", "#0b1214"), img.get("alto", 880), img["bajar"]
            sale = "1" if img.get("hasta") is None else f"clip(({b:.3f}-t)/0.3,0,1)"
            r = f"(clip((t-{a:.3f})/0.3,0,1)*{sale})"
            f.append(f"color=c={fondo}:s={W}x{H}:r={FPS}[lienzo{k}]")
            f.append(f"[lienzo{k}][{ult}]overlay=0:'{baja}*{r}':shortest=1[vd{k}]")
            f.append(f"[{k}:v]scale={W}:-2,pad={W}:{alto}:0:oh-ih:color={fondo},fps={FPS},setsar=1,"
                     f"setpts=PTS-STARTPTS+{a:.3f}/TB[im{k}]")
            f.append(f"[vd{k}][im{k}]overlay=0:'-{alto}*(1-{r})':eof_action=pass:enable='between(t,{a:.3f},{b:.3f})'[vo{k}]")
            ult = f"vo{k}"
            continue
        if img.get("ancho"):   # imagen con transparencia en una posición fija (ej. mockup sobre la cabeza)
            f.append(f"[{k}:v]scale={img['ancho']}:-2,fps={FPS},format=rgba,"
                     f"fade=in:st=0:d=0.2:alpha=1,fade=out:st={d - 0.2:.3f}:d=0.2:alpha=1,setpts=PTS-STARTPTS+{a:.3f}/TB[im{k}]")
            f.append(f"[{ult}][im{k}]overlay=(W-w)/2:{img.get('y', ZONA_ARRIBA)}:eof_action=pass:enable='between(t,{a:.3f},{b:.3f})'[vo{k}]")
            ult = f"vo{k}"
            continue
        f.append(f"[{k}:v]scale={W}:-2,pad={W}:{H}:0:(oh-ih)/2:color={img.get('fondo', '#081416')},"
                 f"zoompan=z='{img.get("zoom", 1)}+0.0016*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},"
                 f"format=yuva420p,fade=in:st=0:d=0.12:alpha=1,fade=out:st={d - 0.12:.3f}:d=0.12:alpha=1,"
                 f"setpts=PTS-STARTPTS+{a:.3f}/TB[im{k}]")
        f.append(f"[{ult}][im{k}]overlay=0:0:eof_action=pass:enable='between(t,{a:.3f},{b:.3f})'[vo{k}]")
        ult = f"vo{k}"
    ass_path = str(tmp / "subs.ass").replace(":", "\\:")
    total = dur
    cierre = cfg.get("cierre")
    if cierre:   # placa final a pantalla completa con fundido desde el video
        tr, dc = cierre.get("transicion", 0.4), cierre.get("duracion", 2.5)
        n = sum(1 for x in entradas if x == "-i")
        entradas += ["-loop", "1", "-t", f"{dc + tr:.3f}", "-i", str((base / cierre["archivo"]).resolve())]
        f.append(f"[{ult}]ass='{ass_path}'[vs]")
        f.append(f"[{n}:v]scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color={cierre.get('fondo', '#081416')},"
                 f"zoompan=z='1+0.0008*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},format=yuv420p,setsar=1[cz]")
        f.append(f"[vs]format=yuv420p,setsar=1[vs2];[vs2][cz]xfade=transition={cierre.get('efecto', 'fade')}:duration={tr}:offset={dur - tr:.3f}[vout]")
        total = dur + dc
    else:
        f.append(f"[{ult}]ass='{ass_path}'[vout]")
    f.append(f"[ac]highpass=f=80,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000,apad=whole_dur={total:.3f}[aout]")

    salida.parent.mkdir(parents=True, exist_ok=True)
    run(["ffmpeg", "-v", "error", "-y", *entradas, "-filter_complex", ";".join(f), "-map", "[vout]", "-map", "[aout]",
         "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-profile:v", "high",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(salida)])
    print(f"OK: {salida.relative_to(ROOT)} ({total:.1f} s, {len(cortes)} tramos)")


if __name__ == "__main__":
    main()
