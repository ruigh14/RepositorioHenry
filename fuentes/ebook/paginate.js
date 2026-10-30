// Reparte el contenido en páginas A4, numera, completa el índice y distribuye el espacio libre.
(function () {
  const mm = 3.7795;
  function unwrapCols() {
    document.querySelectorAll('.cols2:not(.keep)').forEach(c => {
      const frag = document.createDocumentFragment();
      [...c.children].forEach(col => {
        if (col.tagName === 'DIV' && !col.className) { [...col.childNodes].forEach(n => frag.appendChild(n)); }
        else frag.appendChild(col);
      });
      c.replaceWith(frag);
    });
  }
  function over(b) { return b.scrollHeight > b.clientHeight + 1; }
  function paginate() {
    let guard = 0;
    for (let i = 0; i < document.querySelectorAll('section.page').length && guard < 400; i++, guard++) {
      const p = document.querySelectorAll('section.page')[i];
      const b = p.querySelector('.body');
      if (p.classList.contains('p-cover') || p.classList.contains('p-spread') || !over(b)) continue;
      if (b.children.length < 2) continue;

      // Salvaguarda ejercicios RENOVA: nunca dividir bloques de 4 ejercicios o menos
      const initialExs = b.querySelectorAll('.ex').length;
      if (initialExs > 0 && initialExs <= 4) continue;

      const np = document.createElement('section');
      np.className = p.className; np.id = p.id + '-' + i;
      const h = p.querySelector('.hdr'), f = p.querySelector('.ftr');
      if (h) np.appendChild(h.cloneNode(true));
      if (f) np.appendChild(f.cloneNode(true));
      const nb = document.createElement('div'); nb.className = 'body'; np.appendChild(nb);
      p.after(np);
      while (over(b) && b.children.length > 1) nb.prepend(b.lastElementChild);
      // no dejar títulos sueltos al pie
      while (b.children.length > 1 && /^(H1|H2|H3|SPAN)$/.test(b.lastElementChild.tagName)) nb.prepend(b.lastElementChild);

      // Regla RENOVA: nunca puede quedar una página con 1 o 2 ejercicios (.ex)
      const exP = b.querySelectorAll('.ex').length;
      const exNP = nb.querySelectorAll('.ex').length;
      if ((exP > 0 && exP < 3) || (exNP > 0 && exNP < 3)) {
        while (nb.firstChild) b.appendChild(nb.firstChild);
        np.remove();
        continue;
      }
    }
  }
  function space() {
    document.querySelectorAll('section.page').forEach(p => {
      if (p.classList.contains('p-cover') || p.classList.contains('p-spread')) return;
      const b = p.querySelector('.body'); const kids = [...b.children];
      if (kids.length < 2) return;
      const last = kids[kids.length - 1];
      const free = b.getBoundingClientRect().bottom - last.getBoundingClientRect().bottom - parseFloat(getComputedStyle(last).marginBottom || 0);
      if (free < 8 * mm) return;
      const targets = kids.slice(1);
      const add = Math.min((free - 4 * mm) / targets.length, 6 * mm);
      targets.forEach(k => { k.style.marginTop = (parseFloat(getComputedStyle(k).marginTop) + add) + 'px'; });
    });
  }
  function number() {
    const pages = [...document.querySelectorAll('section.page')];
    const idx = id => { const el = document.getElementById(id); const s = el && el.closest('section.page'); return s ? pages.indexOf(s) + 1 : '?'; };
    pages.forEach((p, i) => { const s = p.querySelector('.pgnum'); if (s) s.textContent = i + 1; });
    document.querySelectorAll('.tocr').forEach(a => { a.querySelector('.pg').textContent = idx(a.getAttribute('href').slice(1)); });
    document.querySelectorAll('.pref').forEach(s => { s.textContent = idx(s.dataset.ref); });
  }
  function run() { unwrapCols(); paginate(); number(); space(); document.body.dataset.ready = '1'; }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => requestAnimationFrame(run)); else window.addEventListener('load', run);
})();
