// Exporta muestra.html a muestra.pdf (A4).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(__dirname, 'muestra.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const over = await page.evaluate(() => [...document.querySelectorAll('.body')].map((b, i) => b.scrollHeight - b.clientHeight > 1 ? i + 1 : 0).filter(Boolean));
  await page.pdf({ path: path.join(__dirname, 'muestra.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });
  console.log('muestra.pdf · OVERFLOW', JSON.stringify(over));
  await browser.close();
})();
