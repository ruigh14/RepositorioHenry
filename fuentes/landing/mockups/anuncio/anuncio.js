// Exporta anuncio.html a anuncio_15s.mp4 (1080x1920, 30 fps, sin audio: la voz en off se suma después).
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs'), path = require('path'), os = require('os');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'anuncio.html')); await p.waitForTimeout(800);
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'anu-')), N = 450;
  for (let i = 0; i < N; i++) {
    await p.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), i * 1000 / 30);
    await p.screenshot({ path: path.join(tmp, `f${String(i).padStart(3, '0')}.jpg`), type: 'jpeg', quality: 92 });
  }
  await b.close();
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', '30', '-i', path.join(tmp, 'f%03d.jpg'),
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-movflags', '+faststart', path.join(__dirname, 'anuncio_15s.mp4')]);
  fs.rmSync(tmp, { recursive: true });
  console.log('ok');
})();
