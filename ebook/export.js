// Exporta ebook.html a PDF A4 (la paginación la hace paginate.js dentro de la página).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(__dirname, 'ebook.html'), { waitUntil: 'load' });
  await page.waitForSelector('body[data-ready="1"]', { timeout: 30000 });
  const info = await page.evaluate(() => {
    const ps = [...document.querySelectorAll('section.page')];
    const over = ps.map((p, i) => { const b = p.querySelector('.body'); return { n: i + 1, id: p.id, extra: Math.round(b.scrollHeight - b.clientHeight) }; }).filter(x => x.extra > 1);
    const free = ps.map((p, i) => { const b = p.querySelector('.body'); const r = b.getBoundingClientRect(); let m = r.top; b.querySelectorAll('*').forEach(e => { const q = e.getBoundingClientRect(); if (q.height && q.bottom > m) m = q.bottom; }); return (i + 1) + ':' + Math.round((r.bottom - m) / 3.78); }).join(' ');
    return { n: ps.length, over, free };
  });
  console.log('PAGINAS', info.n, 'OVERFLOW', JSON.stringify(info.over));
  console.log('FREE', info.free);
  await page.pdf({ path: path.join(__dirname, 'Ebook_Programa_RENOVA.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });
  await browser.close();
})();
