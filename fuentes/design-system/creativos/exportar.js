// Exporta los creativos que armó generar.py: imágenes a PNG y videos a MP4 (sin audio).
//   node exportar.js            → todo
//   node exportar.js imagen     → solo imágenes y carruseles
//   node exportar.js video      → solo videos
// Los videos se graban con Playwright (WebM) y se pasan a MP4 H.264 con ffmpeg.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const lista = JSON.parse(fs.readFileSync(path.join(__dirname, 'html', 'lista.json'), 'utf8'));
const solo = process.argv[2];

(async () => {
  const browser = await chromium.launch();
  for (const p of lista) {
    if (solo && p.tipo !== solo) continue;
    fs.mkdirSync(path.dirname(p.salida), { recursive: true });
    if (p.tipo === 'imagen') {
      const page = await browser.newPage({ viewport: { width: p.ancho, height: p.alto } });
      await page.goto('file://' + p.html, { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      await page.screenshot({ path: p.salida });
      await page.close();
    } else {
      const tmp = fs.mkdtempSync(path.join(require('os').tmpdir(), 'rnv-video-'));
      const ctx = await browser.newContext({ viewport: { width: p.ancho, height: p.alto },
        recordVideo: { dir: tmp, size: { width: p.ancho, height: p.alto } } });
      const page = await ctx.newPage();
      await page.goto('file://' + p.html);
      await page.waitForFunction(() => window.__go !== undefined, null, { timeout: 30000 });
      const inicio = await page.evaluate(() => window.__go / 1000);   // segundos desde que empezó la grabación
      await page.waitForTimeout(p.duracion * 1000 + 600);
      const webm = await page.video().path();
      await ctx.close();
      execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-ss', inicio.toFixed(2), '-i', webm, '-t', String(p.duracion),
        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '30', '-movflags', '+faststart', '-an', p.salida]);
      fs.rmSync(tmp, { recursive: true, force: true });
    }
    console.log('ok', path.relative(path.join(__dirname, '..', '..', '..'), p.salida));
  }
  await browser.close();
})();
