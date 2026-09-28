/* Brasas ascendentes ao fundo da página.
   Cria o próprio <canvas>, respeita "reduzir movimento" e pausa em aba oculta. */
(function () {
    'use strict';

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    var canvas = document.createElement('canvas');
    canvas.className = 'embers';
    canvas.setAttribute('aria-hidden', 'true');
    document.body.prepend(canvas);

    var ctx = canvas.getContext('2d');
    var COLORS = ['255,138,61', '226,87,30', '236,208,138', '201,162,75'];
    var w = 0, h = 0, embers = [], frame = null;

    function rand(min, max) { return min + Math.random() * (max - min); }

    function spawn(anywhere) {
        return {
            x: rand(0, w),
            y: anywhere ? rand(0, h) : h + rand(4, 40),
            r: rand(.6, 2.2),
            rise: rand(.25, .9),
            phase: rand(0, Math.PI * 2),
            speed: rand(.01, .03),
            drift: rand(.15, .6),
            alpha: rand(.35, .9),
            color: COLORS[Math.floor(Math.random() * COLORS.length)]
        };
    }

    function resize() {
        var dpr = Math.min(window.devicePixelRatio || 1, 2);
        w = window.innerWidth;
        h = window.innerHeight;
        canvas.width = w * dpr;
        canvas.height = h * dpr;
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        var target = Math.max(30, Math.min(100, Math.round(w * h / 16000)));
        while (embers.length < target) embers.push(spawn(true));
        embers.length = target;
    }

    function tick() {
        ctx.clearRect(0, 0, w, h);
        for (var i = 0; i < embers.length; i++) {
            var e = embers[i];
            e.phase += e.speed;
            e.x += Math.sin(e.phase) * e.drift;
            e.y -= e.rise;

            if (e.y < -10) { embers[i] = spawn(false); continue; }

            var flicker = .65 + .35 * Math.sin(e.phase * 3);
            var fade = Math.min(1, (e.y / h) * 2.2);
            var a = e.alpha * flicker * fade;

            ctx.beginPath();
            ctx.fillStyle = 'rgba(' + e.color + ',' + (a * .18).toFixed(3) + ')';
            ctx.arc(e.x, e.y, e.r * 4, 0, Math.PI * 2);
            ctx.fill();

            ctx.beginPath();
            ctx.fillStyle = 'rgba(' + e.color + ',' + a.toFixed(3) + ')';
            ctx.arc(e.x, e.y, e.r, 0, Math.PI * 2);
            ctx.fill();
        }
        frame = requestAnimationFrame(tick);
    }

    function start() { if (!frame) frame = requestAnimationFrame(tick); }
    function stop() { if (frame) { cancelAnimationFrame(frame); frame = null; } }

    window.addEventListener('resize', resize);
    document.addEventListener('visibilitychange', function () {
        document.hidden ? stop() : start();
    });

    resize();
    start();
})();