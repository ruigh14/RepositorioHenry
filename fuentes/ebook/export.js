// Exporta el HTML de una edición a PDF A4 (la paginación la hace paginate.js dentro de la página).
// Cada PDF se guarda en la carpeta de su producto, en la raíz del repositorio:
//   node export.js            → ebook.html    → programa-renova-completo/Ebook_Programa_RENOVA.pdf
//   node export.js entrena    → entrena.html  → entrena-desde-casa/Ebook_Entrena_desde_casa_RENOVA.pdf
//   node export.js gimnasio   → gimnasio.html → entrena-en-el-gimnasio/Ebook_Entrena_en_el_gimnasio_RENOVA.pdf
const { chromium } = require('playwright');
const path = require('path');
const EDITIONS = {
  completo: ['ebook.html', 'programa-renova-completo/Ebook_Programa_RENOVA.pdf'],
  entrena: ['entrena.html', 'entrena-desde-casa/Ebook_Entrena_desde_casa_RENOVA.pdf'],
  gimnasio: ['gimnasio.html', 'entrena-en-el-gimnasio/Ebook_Entrena_en_el_gimnasio_RENOVA.pdf'],
};
const [htmlFile, pdfFile] = EDITIONS[process.argv[2] || 'completo'] || EDITIONS.completo;
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(__dirname, htmlFile), { waitUntil: 'load' });
  await page.waitForSelector('body[data-ready="1"]', { timeout: 30000 });
  const info = await page.evaluate(() => {
    const ps = [...document.querySelectorAll('section.page')];
    const over = ps.map((p, i) => { const b = p.querySelector('.body'); return { n: i + 1, id: p.id, extra: Math.round(b.scrollHeight - b.clientHeight) }; }).filter(x => x.extra > 1);
    const free = ps.map((p, i) => { const b = p.querySelector('.body'); const r = b.getBoundingClientRect(); let m = r.top; b.querySelectorAll('*').forEach(e => { const q = e.getBoundingClientRect(); if (q.height && q.bottom > m) m = q.bottom; }); return (i + 1) + ':' + Math.round((r.bottom - m) / 3.78); }).join(' ');
    return { n: ps.length, over, free };
  });
  console.log(pdfFile, 'PAGINAS', info.n, 'OVERFLOW', JSON.stringify(info.over));
  console.log('FREE', info.free);
  await page.pdf({ path: path.join(__dirname, '..', '..', pdfFile), format: 'A4', printBackground: true, preferCSSPageSize: true });
  await browser.close();
})();
