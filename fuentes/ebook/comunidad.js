// Exporta el bonus "Acceso a la comunidad" (comunidad.html) a PDF A4 de 2 hojas.
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const out = path.join(__dirname, '..', '..', 'comunidad');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'comunidad.html'), { waitUntil: 'load' });
  await p.waitForTimeout(500);
  await p.pdf({ path: path.join(out, 'Bonus_Acceso_comunidad_RENOVA.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });
  await b.close();
  console.log('comunidad/Bonus_Acceso_comunidad_RENOVA.pdf');
})();
