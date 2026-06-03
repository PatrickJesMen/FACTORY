  const wg = document.getElementById('wg');
  const slices = document.querySelectorAll('.sg');
  const contents = document.querySelectorAll('.segment-icon-content');
  const labels = document.querySelectorAll('.lbl');
  let angle = 0;

  const AudioCtx = window.AudioContext || window.webkitAudioContext;
  let actx;
  function tick() {
    if (!actx) actx = new AudioCtx();
    if (actx.state === 'suspended') actx.resume();
    const o = actx.createOscillator(), g = actx.createGain();
    o.connect(g); g.connect(actx.destination);
    o.type = 'sine';
    o.frequency.setValueAtTime(1600, actx.currentTime);
    o.frequency.exponentialRampToValueAtTime(300, actx.currentTime + 0.035);
    g.gain.setValueAtTime(0.18, actx.currentTime);
    g.gain.exponentialRampToValueAtTime(0.001, actx.currentTime + 0.035);
    o.start(); o.stop(actx.currentTime + 0.035);
  }

  function sel(idx) {
    const cur = document.querySelector('.sg.active');
    if (cur && parseInt(cur.dataset.i) === idx) return;

    const targets = [0, -90, -180, -270];
    let ta = targets[idx];
    let d = ta - (angle % 360);
    if (d > 180) d -= 360;
    if (d < -180) d += 360;
    angle += d;

    tick();
    wg.style.transform = `rotate(${angle}deg)`;

    contents.forEach(c => {
      const cx = c.getAttribute('data-cx');
      const cy = c.getAttribute('data-cy');
      c.setAttribute('transform', `rotate(${-angle}, ${cx}, ${cy})`);
    });

    slices.forEach(s => {
      s.classList.remove('active');
      const lbl = s.querySelector('.lbl');
      if (lbl) lbl.style.fill = '#94A3B8';
    });

    const next = document.querySelector(`.sg[data-i="${idx}"]`);
    next.classList.add('active');
    const nextLbl = next.querySelector('.lbl');
    if (nextLbl) nextLbl.style.fill = 'rgba(255,255,255,0.85)';
  }

  const firstLbl = document.querySelector('.sg.active .lbl');
  if (firstLbl) firstLbl.style.fill = 'rgba(255,255,255,0.85)';


