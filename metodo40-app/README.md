# MÉTODO 40 · App de entrenamiento para hombres 40+

Proyecto de la app con planificación anual (segunda unidad de negocio, separada de RENOVA mujeres).
Lo que ya existe y se reutiliza: ebooks en `ebook-hombres/` y la app web actual en `fuentes/tablero/`.

## Carpetas
- `PROYECTO.md`: resumen integral (decisiones tomadas y propuestas comerciales a ajustar).
- `metodologia/`: reglas de entrenamiento por objetivo (frecuencia, progresión, descargas, niveles, casa/gimnasio, lesiones).
- `planificacion/`: los 12 meses de cada objetivo, generados a partir de las reglas.

## Orden de trabajo acordado
1. Metodología (empezando por Base general y mantenimiento).
2. Recortar combinaciones (frecuencias, niveles) para que sea mantenible.
3. Decidir plataforma: Harbiz o app propia (cuentas, base de datos, suscripción Mercado Pago).
4. Precios y modelo comercial definitivo.

## App (versión nueva)
`cd metodo40-app/app && python3 build.py` → `dist/index.html` (+ `dist/img/`). Lee `planificacion/*.json` y los ejercicios de `fuentes/ebook/hombres.py`.
Pantallas: código → perfil inicial (datos, experiencia → nivel, casa/gimnasio, días, objetivo, dolores, apto médico) → Hoy (próxima rutina A/B/C del mes y semana que corresponden desde la fecha de inicio: entrada en calor, centrales, elongación, carga de kilos) → Dolores (ajusta la rutina sola + botón al equipo médico) → Progreso (sesiones, peso, cintura) → Perfil (antropometría profesional por WhatsApp).
Los objetivos sin planificación aparecen como "Próximamente". Los datos quedan en el celular (localStorage) hasta definir la plataforma.
