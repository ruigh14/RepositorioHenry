"""Genera la planificación anual de MÉTODO 40 (app) a partir de reglas fijas.
Uso: cd metodo40-app/planificacion && python3 generar.py → base.json (para la app) y base.md (para revisar).
Estructura de cada sesión: entrada en calor → central 1..N → elongación. Ejercicios = ids de fuentes/ebook/hombres.py (con video de Harbiz)."""
import json, re
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "fuentes/ebook/hombres.py"
NOMBRE = dict(re.findall(r'^\s+"(\w+)": \("\w+", "([^"]+)"', SRC.read_text(encoding="utf-8"), re.M))

CALOR = ["mov_cadera", "mov_escapular", "cat_cow", "mov_baston", "circ_cadera"]          # 5 ejercicios × 40 s
ELONG = ["el_gigante", "el_isquios", "el_espalda_baja", "el_pectoral", "el_hombro", "el_abductores"]  # 30 s c/u

# Rutinas por variante: cada rutina = lista de bloques centrales (central 1, 2, 3…).
# Central 1: básicos pesados · Central 2: complementarios · Central 3: accesorios + zona media.
RUT = {
 "casa": {
  1: {"A": [["sentadilla_copa", "flexiones"], ["elevacion_cadera_cajon", "remo_unilateral"], ["press_hombros_arrodillado", "plancha_frontal"]],
      "B": [["swing", "remo_unilateral"], ["sentadilla_sumo", "fondos_banco"], ["vuelo_posterior", "curl_biceps", "bicho_muerto_botella"]],
      "C": [["sentadilla_cajon", "push_press"], ["puente_peso", "renegade_row"], ["elevaciones_laterales", "plancha_lateral"]]},
  2: {"A": [["sentadilla_cajon", "flex_inclinadas"], ["puente_peso", "remo_unilateral"], ["elevaciones_laterales", "bird_dog"]],
      "B": [["sentadilla_sumo", "renegade_row"], ["elevacion_cadera_cajon", "flexiones"], ["vuelo_posterior", "curl_biceps", "press_pallof"]],
      "C": [["sentadilla_copa", "push_press"], ["swing", "remo_unilateral"], ["fondos_banco", "bicho_alt", "plancha_lateral"]]},
 },
 "gimnasio": {
  1: {"A": [["sentadilla_barra", "press_plano"], ["remo_polea_baja", "curl_isquio"], ["elevaciones_laterales", "biceps_polea", "plancha_frontal"]],
      "B": [["peso_muerto_barra", "press_45_barra"], ["hack", "jalones"], ["ext_cuadriceps", "face_pull", "press_frances"]],
      "C": [["prensa", "press_militar_maquina"], ["pm_rumano_maquina", "remo_45_barra"], ["triceps_soga", "biceps_martillo", "bicho_muerto_disco"]]},
  2: {"A": [["hack", "press_45_barra"], ["jalones", "curl_isquio"], ["face_pull", "triceps_soga", "press_pallof"]],
      "B": [["pm_rumano_maquina", "press_plano"], ["prensa", "remo_polea_baja"], ["elevaciones_laterales", "biceps_martillo", "plancha_lateral"]],
      "C": [["sentadilla_barra", "press_militar_maquina"], ["peso_muerto_barra", "remo_45_barra"], ["ext_cuadriceps", "press_frances", "bicho_muerto_disco"]]},
 },
}

# 12 meses de BASE GENERAL Y MANTENIMIENTO con periodización ondulada semanal:
# semanas 1, 2 y 3 aumentan (la 3 es la más intensa); la 4 es descarga: carga y volumen 15 % por debajo de la semana 1.
# (mes, fase, objetivo, variante, series, reps sem 1-2-3, RIR sem 1-2-3, descanso central 1)
MESES = [
 (1, "Adaptación", "Aprender la técnica y crear el hábito", 1, 2, ("15", "12", "10"), ("4", "3", "3"), "60 s"),
 (2, "Adaptación", "Consolidar técnica y subir un poco la carga", 1, 3, ("12", "10", "8"), ("3", "3", "2"), "75 s"),
 (3, "Base de fuerza", "Más peso con buena técnica", 1, 3, ("10", "8", "6"), ("3", "2", "2"), "90 s"),
 (4, "Fuerza", "Primer bloque más pesado", 1, 4, ("8", "6", "5"), ("3", "2", "1-2"), "2 min"),
 (5, "Músculo", "Volumen moderado para ganar o mantener músculo", 1, 4, ("12", "10", "8"), ("3", "2", "2"), "90 s"),
 (6, "Consolidación + evaluación", "Afianzar y medir progreso (semana 4: test)", 1, 3, ("10", "8", "6"), ("3", "2", "2"), "2 min"),
 (7, "Nuevo estímulo", "Cambian los ejercicios: adaptarse a la variante 2", 2, 3, ("12", "10", "8"), ("3", "3", "2"), "75 s"),
 (8, "Fuerza", "Segundo bloque pesado", 2, 4, ("8", "6", "5"), ("3", "2", "1-2"), "2 min"),
 (9, "Densidad", "Mismo trabajo en menos tiempo (descansos cortos)", 2, 3, ("15", "12", "10"), ("3", "2", "2"), "45 s"),
 (10, "Músculo", "Segundo bloque de volumen", 2, 4, ("12", "10", "8"), ("3", "2", "2"), "90 s"),
 (11, "Fuerza", "El mes más exigente del año", 2, 4, ("6", "5", "4"), ("2", "2", "1"), "2-3 min"),
 (12, "Mantenimiento + evaluación anual", "Bajar exigencia, test final y preparar el año 2", 2, 3, ("10", "8", "6"), ("3", "3", "2"), "2 min"),
]


def semanas(series, reps, rir):
    """Ondulada: 1 y 2 suben, la 3 es la más intensa (+1 serie en el central 1), la 4 = semana 1 con 15 % menos de carga y volumen."""
    r4 = max(1, round(int(reps[0]) * 0.85))   # repeticiones de la semana 1 −15 %
    return [
        {"semana": 1, "series": series, "reps": reps[0], "rir": rir[0], "carga": "base", "nota": "Base del mes"},
        {"semana": 2, "series": series, "reps": reps[1], "rir": rir[1], "carga": "sube", "nota": "Menos repeticiones, más peso"},
        {"semana": 3, "series": series, "series_central_1": series + 1, "reps": reps[2], "rir": rir[2], "carga": "la más alta",
         "nota": "La semana más intensa: +1 serie en el central 1"},
        {"semana": 4, "series": series, "reps": str(r4), "rir": "4", "carga": "15 % menos que la semana 1",
         "nota": "Descarga: carga y volumen 15 % por debajo de la semana 1"},
    ]


NIVEL = {  # ajustes por nivel (por años de entrenamiento continuo)
 "basico": {"centrales": 2, "series": -1, "rir": "+1", "duracion": "40-45 min"},
 "intermedio": {"centrales": 3, "series": 0, "rir": "0", "duracion": "50-60 min"},
 "avanzado": {"centrales": 3, "series": 1, "rir": "0", "duracion": "50-60 min"},
}

# Dolores: el usuario marca la zona → rutina sin impacto, nivel básico y estos cambios.
DOLOR = {
 "rodilla": {"swing": "puente_peso", "sentadilla_copa": "sentadilla_cajon", "sentadilla_sumo": "sentadilla_cajon", "sentadilla_barra": "prensa",
             "hack": "prensa", "ext_cuadriceps": "curl_isquio", "push_press": "press_hombros_arrodillado", "mountain": "plancha_frontal"},
 "lumbar": {"peso_muerto_barra": "elevacion_cadera_cajon", "swing": "puente_peso", "remo_45_barra": "remo_polea_baja", "renegade_row": "remo_unilateral",
            "push_press": "press_militar_maquina", "sentadilla_barra": "prensa", "pm_rumano_maquina": "puente_peso"},
 "hombro": {"press_hombros_arrodillado": "face_pull", "push_press": "vuelo_posterior", "press_militar_maquina": "face_pull", "fondos_banco": "triceps_soga",
            "press_plano": "flex_inclinadas", "press_45_barra": "flex_inclinadas", "flexiones": "flex_inclinadas", "renegade_row": "remo_unilateral"},
}


# En casa no hay poleas ni máquinas: estos cambios reemplazan a los de arriba
DOLOR_CASA = {"lumbar": {"push_press": "press_hombros_arrodillado"},
              "hombro": {"press_hombros_arrodillado": "vuelo_posterior", "fondos_banco": "press_frances"}}
SOLO_GYM = {i for v in RUT["gimnasio"].values() for r in v.values() for b in r for i in b} - {i for v in RUT["casa"].values() for r in v.values() for b in r for i in b} - {"press_frances"}


def dolores(lugar):
    out = {}
    for z, c in DOLOR.items():
        c = {**c, **(DOLOR_CASA.get(z, {}) if lugar == "casa" else {})}
        if lugar == "casa":
            c = {a: b for a, b in c.items() if a not in SOLO_GYM}
            assert not [b for b in c.values() if b in SOLO_GYM], (z, c)
        out[z] = c
    return out


def ej(i):
    assert i in NOMBRE, f"ejercicio sin video en hombres.py: {i}"
    return {"id": i, "nombre": NOMBRE[i]}


def plan():
    meses = []
    for m, fase, obj, var, series, reps, rir, desc in MESES:
        meses.append({"mes": m, "fase": fase, "objetivo": obj, "variante": var,
                      "descanso": {"central_1": desc, "resto": "60 s"},
                      "semanas": semanas(series, reps, rir),
                      "rutinas": {lugar: {r: {"entrada_en_calor": [ej(i) for i in CALOR],
                                              "centrales": [[ej(i) for i in b] for b in bloques],
                                              "elongacion": [ej(i) for i in ELONG]}
                                          for r, bloques in RUT[lugar][var].items()} for lugar in RUT}})
    return {"objetivo": "base", "nombre": "Base general y mantenimiento", "rotacion": "A → B → C; si entrena más días vuelve a A",
            "frecuencia": "2 a 3 por semana", "niveles": NIVEL, "dolores": {l: dolores(l) for l in RUT}, "meses": meses}


def md(p):
    L = [f"# {p['nombre']} · planificación de 12 meses", "",
         "Cada sesión: **entrada en calor** (5 ejercicios × 40 s) → **central 1, 2, 3** → **elongación** (6 posturas × 30 s).",
         f"Frecuencia {p['frecuencia']}, rotación {p['rotacion']}.",
         "**Periodización ondulada:** semanas 1 y 2 suben, la 3 es la más intensa (+1 serie en el central 1) y la 4 es descarga: carga y repeticiones 15 % por debajo de la semana 1.", "",
         "| Mes | Fase | Variante | Semana 1 | Semana 2 | Semana 3 (pico) | Semana 4 (−15 %) | Descanso central 1 |", "|---|---|---|---|---|---|---|---|"]
    for m in p["meses"]:
        w = m["semanas"]
        c = [f"{x['series']} × {x['reps']} · RIR {x['rir']}" for x in w[:2]] + [f"{w[2]['series_central_1']} × {w[2]['reps']} · RIR {w[2]['rir']}", f"{w[3]['series']} × {w[3]['reps']} · −15 % carga"]
        L.append(f"| {m['mes']} | {m['fase']} | {m['variante']} | " + " | ".join(c) + f" | {m['descanso']['central_1']} |")
    L += ["", "**Niveles:** básico = 2 centrales, 1 serie menos y RIR +1 (40-45 min) · intermedio = 3 centrales (50-60 min) · avanzado = 3 centrales y 1 serie más.", ""]
    for lugar in RUT:
        for var in (1, 2):
            L.append(f"## {lugar.capitalize()} · variante {var} (meses {'1-6' if var == 1 else '7-12'})")
            for r, bloques in RUT[lugar][var].items():
                L.append(f"- **Rutina {r}:** " + " · ".join(f"Central {k}: " + ", ".join(NOMBRE[i] for i in b) for k, b in enumerate(bloques, 1)))
            L.append("")
    L.append("## Dolores (cambios automáticos; además: sin impacto y nivel básico)")
    for lugar, zonas in p["dolores"].items():
        L.append(f"### {lugar.capitalize()}")
        for z, cambios in zonas.items():
            L.append(f"- **{z.capitalize()}:** " + "; ".join(f"{NOMBRE[a]} → {NOMBRE[b]}" for a, b in cambios.items()))
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    p = plan()
    Path("base.json").write_text(json.dumps(p, ensure_ascii=False, indent=1), encoding="utf-8")
    Path("base.md").write_text(md(p), encoding="utf-8")
    print("ok", len(p["meses"]), "meses")
