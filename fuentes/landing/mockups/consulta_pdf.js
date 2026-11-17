// Ver consulta_pdf.py
const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'consulta_pdf.html')); await p.waitForTimeout(800);
  await p.pdf({ path: path.join(__dirname, '..', '..', '..', 'sin-tacc-inteligente', 'Consulta_equipo_RENOVA.pdf'), format: 'A4', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await b.close(); console.log('ok'); })();
