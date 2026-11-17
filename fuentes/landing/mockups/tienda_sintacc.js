// Ver tienda_sintacc.py: primero la tapa (1240x1754), después los dos mockups 3D.
const { chromium } = require('playwright');
const path = require('path');
const OUT = path.join(__dirname, '..', '..', '..', 'sin-tacc-inteligente', 'creativos');
(async () => {
  const b = await chromium.launch();
  const t = await b.newPage({ viewport: { width: 1240, height: 1754 } });
  await t.goto('file://' + path.join(__dirname, 'tapa_sintacc_comida.html')); await t.waitForTimeout(700);
  await t.screenshot({ path: path.join(__dirname, 'pack', 'tapa_sintacc_comida.png') });
  for (const [n, w, h, o] of [['tienda_sintacc_v', 1080, 1440, 'tienda_portada_vertical.png'], ['tienda_sintacc', 1080, 1080, 'tienda_portada.png']]) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + path.join(__dirname, n + '.html')); await p.waitForTimeout(700);
    await p.screenshot({ path: path.join(OUT, o), omitBackground: false });
  }
  await b.close(); console.log('ok');
})();
