// JavaScript de la landing. build.py lo carga desde jsDelivr (Impultienda rompe la página si el HTML trae un bloque <script> propio).
(function(){
  var root = document.getElementById('rnv') || document.body;
  root.classList.add('js');

  // Pestaña del navegador: nombre y logo de RENOVA (Impultienda pone el título de la tienda)
  document.title = root.getAttribute('data-titulo') || 'Método RENOVA';   // build.py: RENOVA o MÉTODO 40
  var F = 'https://cdn.jsdelivr.net/gh/ruigh14/RepositorioHenry@main/fuentes/landing/img/favicon.png';
  [].forEach.call(document.querySelectorAll('link[rel~="icon"],link[rel="apple-touch-icon"]'), function(l){ l.parentNode.removeChild(l); });
  ['icon', 'apple-touch-icon'].forEach(function(r){ var l = document.createElement('link'); l.rel = r; l.href = F; document.head.appendChild(l); });

  // Aparición de las secciones
  var els = root.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){ if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: .1 });
    els.forEach(function(el){ io.observe(el); });
  } else { els.forEach(function(el){ el.classList.add('in'); }); }

  // Videos: se reproducen solo mientras se ven (ahorra datos en el celular)
  var vids = root.querySelectorAll('video');
  if ('IntersectionObserver' in window) {
    var vo = new IntersectionObserver(function(es){
      es.forEach(function(e){
        var v = e.target;
        if (e.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function(){}); } else v.pause();
      });
    }, { threshold: .3 });
    vids.forEach(function(v){ vo.observe(v); });
  }

  // Reloj de la oferta: 15 minutos desde que entra (se guarda en el navegador; al terminar vuelve a empezar)
  var tm = document.getElementById('tmr');
  if (tm) {
    var D = 15 * 60 * 1000, t0 = Date.now();
    try { var g = +localStorage.getItem('rnv_t0'); if (g && Date.now() - g < D) t0 = g; else localStorage.setItem('rnv_t0', t0); } catch (e) {}
    var z = function(n){ return (n < 10 ? '0' : '') + n; };
    var tick = function(){
      var r = D - (Date.now() - t0);
      if (r <= 0) { t0 = Date.now(); r = D; try { localStorage.setItem('rnv_t0', t0); } catch (e) {} }
      var x = Math.floor(r / 1000);
      tm.textContent = z(Math.floor(x / 3600)) + ':' + z(Math.floor(x / 60) % 60) + ':' + z(x % 60);
    };
    tick(); setInterval(tick, 1000);
  }

  // VSL (Wistia, embed sin iframe): arranca solo, en silencio y en loop.
  // Al tocar, el sonido se activa al instante y el video vuelve al principio.
  var von = document.getElementById('vsl-on');
  if (von) {
    ['https://fast.wistia.com/embed/medias/9xn7yk66az.jsonp', 'https://fast.wistia.com/assets/external/E-v1.js'].forEach(function(u){
      var sc = document.createElement('script'); sc.src = u; sc.async = true; document.body.appendChild(sc);
    });
    var vid = null, pend = false;
    var go = function(){
      vid.unmute(); vid.volume(1); vid.time(0); vid.play();
      try { vid.setControlEnabled('playbar', true); } catch (e) {}
      von.classList.add('off');
    };
    window._wq = window._wq || [];
    window._wq.push({ id: '9xn7yk66az', onReady: function(v){ vid = v; if (pend) go(); } });
    von.onclick = function(){ if (vid) go(); else pend = true; };
  }

  // Upsell: si Impultienda no lo completó, no se muestra
  var ups = document.getElementById('ups');
  if (ups) {
    var t = ups.querySelector('.ups-f b').textContent.trim();   // el precio lo completa Impultienda
    if (!t || t.indexOf('{{') > -1) ups.style.display = 'none';
  }

  // Carruseles (testimonios, mensajes de clientas y equipo): pasan solos cada 4 s y se deslizan con el dedo
  function carrusel(tr, dw){
    if (!tr || !dw) return;
    var ms = tr.children, k = 0, timer;
    for (var j = 0; j < ms.length; j++) (function(j){
      var d = document.createElement('button'); d.setAttribute('aria-label', (j + 1) + ' de ' + ms.length);
      d.onclick = function(){ go(j); restart(); }; dw.appendChild(d);
    })(j);
    var go = function(n){
      k = (n + ms.length) % ms.length;
      tr.scrollTo({ left: ms[k].offsetLeft - tr.offsetLeft - (tr.clientWidth - ms[k].offsetWidth) / 2, behavior: 'smooth' });
      [].forEach.call(dw.children, function(d, x){ d.classList.toggle('on', x === k); });
    };
    var restart = function(){ clearInterval(timer); timer = setInterval(function(){ go(k + 1); }, 4000); };
    go(0); restart();
    tr.addEventListener('touchstart', function(){ clearInterval(timer); }, { passive: true });
    tr.addEventListener('touchend', restart, { passive: true });
    tr.addEventListener('scroll', function(){
      var c = tr.scrollLeft + tr.clientWidth / 2, best = 0, bd = 1e9;
      for (var j = 0; j < ms.length; j++){ var m = ms[j].offsetLeft - tr.offsetLeft + ms[j].offsetWidth / 2, dd = Math.abs(m - c); if (dd < bd){ bd = dd; best = j; } }
      k = best; [].forEach.call(dw.children, function(d, x){ d.classList.toggle('on', x === k); });
    }, { passive: true });
  }
  carrusel(document.getElementById('msgs'), document.getElementById('msgs-dots'));
  carrusel(document.getElementById('clientas'), document.getElementById('clientas-dots'));   // testimonios con foto
  carrusel(document.getElementById('team'), document.getElementById('team-dots'));
  carrusel(document.getElementById('entrenan'), document.getElementById('entrenan-dots'));   // landing MÉTODO 40

  // Barra de compra en el celular: aparece apenas el botón de la portada sale de la pantalla
  // (Clarity: casi nadie baja del 15-35%) y se esconde sobre la caja de precio
  var bar = document.getElementById('mbar'), buy = document.querySelector('#comprar .card'), hb = document.querySelector('.hero .btn');
  var upd = function(){
    var b = buy.getBoundingClientRect(), t = hb ? hb.getBoundingClientRect().bottom < 0 : window.scrollY > 600;
    bar.classList.toggle('show', t && !(b.top < window.innerHeight && b.bottom > 0));
  };
  window.addEventListener('scroll', upd, { passive: true });
})();

// Menú lateral: se cierra al tocar una sección o el botón, y con Escape.
(function () {
  var chk = document.getElementById('nav-chk');
  if (!chk) return;
  document.querySelectorAll('#rnv .nav-link, #rnv .nav-dbtn').forEach(function (el) {
    el.addEventListener('click', function () { chk.checked = false; });
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && chk.checked) chk.checked = false; });
})();
