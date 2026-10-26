# Proyecto RENOVA

Repositorio de RENOVA, el programa de entrenamiento, alimentación y descanso de Nacho Portillo.
Todo el trabajo se guarda acá, en la rama `main`. Lo que no se commitea y pushea se pierde al cerrar la sesión.

## Estructura

- `ebook/`: los ebooks RENOVA, generados desde un mismo `build.py` en dos ediciones:
  - **Ebook 1 · "Entrená desde casa"** (producto de entrada): plan de fuerza de 8 semanas + bonus
    (recetario, 2 talleres: Descanso y Heladera, consulta con Nacho). → `entrena.html`, `Ebook_Entrena_desde_casa_RENOVA.pdf`.
  - **Programa RENOVA completo** (entrenamiento + alimentación + descanso, 64 páginas): base para los ebooks de upsell.
    → `ebook.html`, `Ebook_Programa_RENOVA.pdf`.
  - `build.py`: todos los textos, recetas, menús, ejercicios (rutinas en formato entrada en calor + bloque 1 + bloque 2 + elongación), plan de 8 semanas (`PLAN8`), pausa activa (`PAUSA`, `TIPS_DIA`), extra de zona media (`CORE`) y links (`LINKS`; `VIDEOS` = links de Harbiz de cada ejercicio).
  - `style.css`: diseño. `paginate.js`: paginación automática A4. `export.js`: exporta el PDF con Playwright.
  - `img/`: fotos, ilustraciones, recetas y testimonios. `fonts/`: tipografía Inter.
  - `Ebook_Programa_RENOVA.pdf`: versión final vigente. `Ebook_Programa_RENOVA.txt`: su texto extraído.
  - `version-anterior_7_1.pdf`: exportación anterior (solo referencia, no editar).
- `index.html`: landing de venta del ebook + talleres.
- `upsell.html`: página de upsell post-compra ("desbloqueá todos los talleres").
- `css/styles.css`: estilos compartidos de la landing y el upsell.

## Regenerar el PDF del ebook

```
cd ebook && python3 build.py entrena && node export.js entrena   # Ebook 1 · Entrená desde casa
cd ebook && python3 build.py && node export.js                   # Programa RENOVA completo
```

Debe imprimir `OVERFLOW []` (sin páginas con texto cortado).

## Estrategia de producto

- Ebook 1 (solo entrenamiento) es el producto de entrada; alimentación (menús, compras) y descanso quedan para ebooks de upsell.
- El equipo incluye **médico deportólogo** (medicina deportiva): mantenerlo en ambas ediciones.
- Investigación de mercado de referencia: Google Doc "RENOVA_investigacion_ebooks_entrenamiento_mujeres_40_plus".

## Forma de trabajo

- Editar textos y contenido del ebook en `build.py`, no en `ebook.html` (se regenera).
- Después de cada cambio: regenerar el PDF, commitear y pushear a `main`.
- Idioma: español rioplatense (voseo).
- Se lee en el celular: letra grande (cuerpo 15 pt). Si algo no entra en la hoja, acortar texto o separar en hojas, no achicar la letra.
