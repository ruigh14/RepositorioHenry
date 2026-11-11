// Tablero de progreso de MÉTODO 40 en Cloudflare (Worker con archivos estáticos).
// Publicar: cd fuentes/tablero && python3 build.py && ~/.local/bin/cf deploy
import { defineConfig } from "cf/config";

export default defineConfig({
  worker: {
    "name": "metodo40-progreso",
    "compatibilityDate": "2026-11-04",
    "observability": {
      "enabled": false
    }
  }
});
