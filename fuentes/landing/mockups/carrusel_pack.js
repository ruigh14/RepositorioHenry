const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = __dirname + '/../../../pack-renova/carrusel/'; fs.mkdirSync(out, { recursive: true });
  for (let i = 1; i <= 8; i++) {
    const n = String(i).padStart(2, '0'); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
    await p.goto('file://' + __dirname + '/carrusel_' + n + '.html'); await p.waitForTimeout(500);
    const h = await p.evaluate(() => document.body.scrollHeight); if (h > 1350) console.log('ALTO', n, h);
    await p.screenshot({ path: out + n + '.png' }); await p.close();
  }
  { const p = await b.newPage({ viewport: { width: 1080, height: 1350 } }); await p.goto('file://' + __dirname + '/carrusel_bonus.html'); await p.waitForTimeout(500);
    await p.screenshot({ path: out + 'bonus.png' }); await p.close(); }
  await b.close();
})();
