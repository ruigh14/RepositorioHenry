const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const out = __dirname + '/../../../pack-renova/';
  for (const [n, w, h] of [['libro_1_casa',1080,1350],['libro_2_gimnasio',1080,1350],['libro_3_alimentacion',1080,1350],['libros_juntos',1920,1080]]) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + __dirname + '/' + n + '.html'); await p.waitForTimeout(600);
    await p.screenshot({ path: out + n + '.png' }); await p.close();
  }
  await b.close();
})();
