// Ver consulta_sintacc.py
const { chromium } = require('playwright'); const path = require('path');
const OUT = path.join(__dirname, '..', '..', '..', 'sin-tacc-inteligente', 'creativos');
(async () => { const b = await chromium.launch();
  for (const [n, h, o] of [['consulta_sintacc_v', 1440, 'consulta_portada_vertical.png'], ['consulta_sintacc', 1080, 'consulta_portada.png']]) {
    const p = await b.newPage({ viewport: { width: 1080, height: h } });
    await p.goto('file://' + path.join(__dirname, n + '.html')); await p.waitForTimeout(600);
    await p.screenshot({ path: path.join(OUT, o) }); }
  await b.close(); console.log('ok'); })();
