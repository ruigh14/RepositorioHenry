// Saca las capturas de las 2 imágenes armadas (ver mockups.py).
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const [src, out] of [['nutricion.html', 'mock_nutricion.jpg'], ['programa.html', 'mock_programa.jpg']]) {
    const p = await b.newPage({ viewport: src === 'programa.html' ? { width: 2000, height: 950 } : { width: 1200, height: 900 } });
    await p.goto('file://' + __dirname + '/' + src); await p.waitForTimeout(600);
    await p.screenshot({ path: __dirname + '/../img/' + out });
  }
  await b.close();
})();
