const wg = document.getElementById('wg');
const slices = document.querySelectorAll('.sg');
const contents = document.querySelectorAll('.segment-icon-content');
let angle = -60; // Initial angle matches the center of the first segment

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

    // Center targets for the 3 segments
    const targets = [-45, -135, -225, -315];
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
    });

    const next = document.querySelector(`.sg[data-i="${idx}"]`);
    if (next) {
        next.classList.add('active');
    }

    // Toggle corresponding content panels
    document.querySelectorAll('.content-panel').forEach(p => {
        p.classList.add('hidden');
    });
    
    const activePanel = document.getElementById(`panel-${idx}`);
    if (activePanel) {
        activePanel.classList.remove('hidden');
    }
}