// Glúteos Fuertes: saca la tapa del ebook, las 3 portadas y el video de 4 s (ver gluteos_promo.py).
// Necesita ffmpeg en el PATH (o en la variable FFMPEG) para armar el mp4.
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const OUT = path.join(__dirname, '..', '..', '..', 'gluteos-fuertes', 'creativos');
const FFMPEG = process.env.FFMPEG || 'ffmpeg';
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch(process.env.PW_CHANNEL ? { channel: process.env.PW_CHANNEL } : {});
  // 1) tapas reales de los dos ebooks (casa y gimnasio), en alta
  for (const ed of ['casa', 'gym']) {
    const t = await b.newPage({ viewport: { width: 900, height: 1300 }, deviceScaleFactor: 2 });
    await t.goto('file://' + path.join(__dirname, '..', '..', 'ebook', `gluteos_${ed}.html`));
    await t.waitForSelector('body[data-ready="1"]', { timeout: 30000 });
    await (await t.$('section#portada')).screenshot({ path: path.join(__dirname, 'pack', `tapa_gluteos_${ed}.jpg`), quality: 92 });
  }
  // 2) portadas
  for (const n of [1, 2, 3]) {
    const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
    await p.goto('file://' + path.join(__dirname, `gluteos_promo_${n}.html`)); await p.waitForTimeout(500);
    await p.screenshot({ path: path.join(OUT, `portada_${n}.jpg`), quality: 92 });
  }
  // 3) video: 120 cuadros a 30 fps con las animaciones pausadas en cada instante
  const v = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await v.goto('file://' + path.join(__dirname, 'gluteos_promo_video.html')); await v.waitForTimeout(500);
  const tmp = fs.mkdtempSync(path.join(require('os').tmpdir(), 'glut-'));
  for (let i = 0; i < 120; i++) {
    await v.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), i * 1000 / 30);
    await v.screenshot({ path: path.join(tmp, `f${String(i).padStart(3, '0')}.png`) });
  }
  await b.close();
  execFileSync(FFMPEG, ['-y', '-loglevel', 'error', '-framerate', '30', '-i', path.join(tmp, 'f%03d.png'),
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-movflags', '+faststart', path.join(OUT, 'video_4s.mp4')]);
  fs.rmSync(tmp, { recursive: true });
  console.log('ok →', OUT);
})();
