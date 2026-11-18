const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const out = __dirname + '/../../../sin-tacc-inteligente/creativos/';
  for (const [n, w, h] of [['reposteria_mockup',1080,1350],['reposteria_mockup_vertical',1080,1920]]) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + __dirname + '/' + n + '.html'); await p.waitForTimeout(600);
    await p.screenshot({ path: out + n + '.png' }); await p.close();
  }
  await b.close();
})();
