const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 1.5 });
  await p.goto('file://' + __dirname + '/tapa_express.html'); await p.waitForTimeout(600);
  await p.locator('#portada').screenshot({ path: __dirname + '/../landing/mockups/pack/tapa_express.png' }); await b.close();
})();
