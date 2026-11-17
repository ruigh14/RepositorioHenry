// Ver tienda_sintacc_extras.py
const { chromium } = require('playwright'); const path = require('path');
const OUT = path.join(__dirname, '..', '..', '..', 'sin-tacc-inteligente', 'creativos');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1440 } });
  for (const n of ['bonus_comunidad', 'bonus_pausa', 'upsell_entrenamiento']) {
    await p.goto('file://' + path.join(__dirname, n + '.html')); await p.waitForTimeout(700);
    await p.screenshot({ path: path.join(OUT, n + '.png') }); }
  await b.close(); console.log('ok'); })();
