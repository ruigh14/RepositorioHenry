const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1600, height: 1300 } });
  await p.goto('file://' + __dirname + '/libros.html'); await p.waitForTimeout(600);
  await p.screenshot({ path: __dirname + '/../../../pack-renova/pack_libros.png', omitBackground: true });
  await b.close();
})();
