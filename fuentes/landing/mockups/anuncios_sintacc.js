const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const out = __dirname + '/../../../sin-tacc-inteligente/creativos/';
  for (const n of ['anuncio_1_precio', 'anuncio_2_incluye', 'anuncio_3_testimonio', 'anuncio_4_3d']) {
    const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
    await p.goto('file://' + __dirname + '/' + n + '.html'); await p.waitForTimeout(700);
    await p.screenshot({ path: out + n + '.png' }); await p.close();
  }
  await b.close();
})();
