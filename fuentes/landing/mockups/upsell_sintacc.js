const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const out = __dirname + '/../../../sin-tacc-inteligente/creativos/';
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1080 } });
  await p.goto('file://' + __dirname + '/upsell_sintacc.html'); await p.waitForTimeout(800);
  await p.screenshot({ path: out + 'upsell_portada.png' });
  const v = await b.newPage({ viewport: { width: 1080, height: 1440 } });   // vertical 3:4: tarjetas de Impultienda
  await v.goto('file://' + __dirname + '/upsell_sintacc_v.html'); await v.waitForTimeout(800);
  await v.screenshot({ path: out + 'upsell_portada_vertical.png' });
  await b.close();
})();
