// JavaScript de la landing. build.py lo carga desde jsDelivr (Impultienda rompe la página si el HTML trae un bloque <script> propio).
(function(){
  var root = document.getElementById('rnv') || document.body;
  root.classList.add('js');

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

  // Reloj de la oferta: 5 horas desde que entra (se guarda en el navegador; al terminar vuelve a empezar)
  var tm = document.getElementById('tmr');
  if (tm) {
    var D = 5 * 3600 * 1000, t0 = Date.now();
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

  // Upsell: si Impultienda no lo completó, no se muestra
  var ups = document.getElementById('ups');
  if (ups) {
    var t = ups.querySelector('.ups-f b').textContent.trim();   // el precio lo completa Impultienda
    if (!t || t.indexOf('{{') > -1) ups.style.display = 'none';
  }

  // Mensajes de clientas: pasan solos cada 4 s
  var tr = document.getElementById('msgs'), dw = document.getElementById('msgs-dots');
  if (tr) {
    var ms = tr.children, k = 0, timer;
    for (var j = 0; j < ms.length; j++) (function(j){
      var d = document.createElement('button'); d.setAttribute('aria-label', 'Mensaje ' + (j + 1));
      d.onclick = function(){ go(j); restart(); }; dw.appendChild(d);
    })(j);
    var go = function(n){
      k = (n + ms.length) % ms.length;
      tr.scrollTo({ left: ms[k].offsetLeft - (tr.clientWidth - ms[k].offsetWidth) / 2, behavior: 'smooth' });
      [].forEach.call(dw.children, function(d, x){ d.classList.toggle('on', x === k); });
    };
    var restart = function(){ clearInterval(timer); timer = setInterval(function(){ go(k + 1); }, 4000); };
    go(0); restart();
    tr.addEventListener('touchstart', restart, { passive: true });
  }

  // Barra de compra en el celular: aparece después del 30% de la página y se esconde sobre la caja de precio
  var bar = document.getElementById('mbar'), buy = document.querySelector('#comprar .card');
  window.addEventListener('scroll', function(){
    var h = document.documentElement.scrollHeight - window.innerHeight;
    var b = buy.getBoundingClientRect();
    bar.classList.toggle('show', h > 0 && window.scrollY / h > .3 && !(b.top < window.innerHeight && b.bottom > 0));
  }, { passive: true });
})();
