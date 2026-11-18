// Exporta sintacc_checkout.html (ver pack_checkout.py) a pack-renova/pack_checkout.png
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1310 } });
  await p.goto('file://' + __dirname + '/sintacc_checkout.html'); await p.waitForTimeout(800);
  console.log('alto', await p.evaluate(() => document.body.scrollHeight));
  await p.screenshot({ path: __dirname + '/../../../sin-tacc-inteligente/creativos/checkout.png' });
  await b.close();
})();
