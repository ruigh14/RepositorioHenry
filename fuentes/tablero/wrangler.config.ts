// Archivos estáticos del tablero: lo que arma build.py en dist/.
import { defineWranglerConfig } from "wrangler/experimental-config";

export default defineWranglerConfig({
  "assetsDirectory": "./dist"
});
