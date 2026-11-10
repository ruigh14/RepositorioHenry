# Ejecución (Capa 3)

Scripts de Python deterministas. Reglas:

- Leen claves desde `.env` (nunca hardcodeadas).
- Escriben archivos intermedios en `.tmp/`.
- Antes de crear un script nuevo, revisa si ya existe uno que sirva.

## Scripts disponibles

| Script | Qué hace |
|---|---|
| `sync_agent_files.py` | Mantiene CLAUDE.md, AGENTS.md y GEMINI.md idénticos (`--check` para verificar, `--source` para elegir la fuente). |
| `editar_reel.py` | Edita un video a cámara como reel de Instagram (cortes, subtítulos, carteles, imagen del producto, audio a -14 LUFS). Directiva: `directives/editar_reel.md`. |
