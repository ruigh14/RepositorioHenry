// Exporta los 3 mockups del pack (ver pack.py) a pack-renova/ en la raíz del repo.
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const out = __dirname + '/../../../pack-renova';
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  for (const n of ['pack_1', 'pack_2', 'pack_3']) {
    await p.goto('file://' + __dirname + '/' + n + '.html'); await p.waitForTimeout(700);
    const h = await p.evaluate(() => document.body.scrollHeight);
    await p.screenshot({ path: out + '/' + n + '.png' });
    console.log(n, h);
  }
  await b.close();
})();
