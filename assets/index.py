from pathlib import Path

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ATCG — Play Something Different</title>
<style>
  * { box-sizing: border-box; }
  html, body { margin: 0; min-height: 100%; }
  body {
    font-family: Inter, Arial, sans-serif;
    color: #fff;
    background:
      radial-gradient(circle at 15% 20%, rgba(183, 255, 0, .18), transparent 28%),
      radial-gradient(circle at 85% 75%, rgba(155, 70, 255, .22), transparent 30%),
      #09070f;
    overflow-x: hidden;
  }
  .noise {
    position: fixed; inset: 0; pointer-events: none; opacity: .055;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 160 160' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  }
  main {
    width: min(1100px, 92vw);
    margin: 0 auto;
    padding: 42px 0 55px;
    text-align: center;
  }
  .badge {
    display: inline-block;
    padding: 8px 14px;
    border: 1px solid rgba(255,255,255,.18);
    border-radius: 999px;
    color: #caff4a;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: .2em;
    text-transform: uppercase;
    backdrop-filter: blur(8px);
  }
  .logo-wrap {
    margin: 28px auto 8px;
    width: min(620px, 90vw);
  }
  canvas {
    width: 100%;
    height: auto;
    display: block;
    filter: drop-shadow(0 0 30px rgba(190,255,0,.18));
  }
  .tagline {
    margin: 0 auto 42px;
    max-width: 720px;
    font-size: clamp(20px, 3vw, 34px);
    font-weight: 800;
    line-height: 1.12;
  }
  .tagline span { color: #caff4a; }
  section {
    margin-top: 30px;
    padding: 30px;
    border: 1px solid rgba(255,255,255,.1);
    border-radius: 28px;
    background: rgba(255,255,255,.045);
    box-shadow: 0 20px 80px rgba(0,0,0,.28);
    backdrop-filter: blur(14px);
  }
  h2 {
    margin: 0 0 24px;
    font-size: 14px;
    letter-spacing: .18em;
    text-transform: uppercase;
    color: #caff4a;
  }
  .team {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }
  .member {
    padding: 24px 16px;
    border-radius: 20px;
    background: linear-gradient(145deg, rgba(255,255,255,.09), rgba(255,255,255,.025));
    border: 1px solid rgba(255,255,255,.08);
    transition: transform .2s ease, border-color .2s ease;
  }
  .member:hover {
    transform: translateY(-6px) rotate(-1deg);
    border-color: rgba(202,255,74,.55);
  }
  .member strong { display: block; font-size: 22px; }
  .member small {
    display: block;
    margin-top: 7px;
    color: #b9b3c8;
    font-weight: 700;
    letter-spacing: .08em;
  }
  .video {
    aspect-ratio: 16 / 9;
    overflow: hidden;
    border-radius: 18px;
    background: #030305;
    border: 1px solid rgba(255,255,255,.1);
    display: grid;
    place-items: center;
    position: relative;
  }
  .video::before {
    content: "▶";
    width: 74px; height: 74px;
    border-radius: 50%;
    display: grid; place-items: center;
    background: #caff4a;
    color: #09070f;
    font-size: 28px;
    padding-left: 4px;
    box-shadow: 0 0 35px rgba(202,255,74,.35);
  }
  .video p {
    position: absolute;
    bottom: 18px;
    margin: 0;
    color: #aaa4b7;
    font-size: 13px;
  }
  .contact {
    margin-top: 30px;
    padding: 34px 20px;
  }
  .email {
    color: #fff;
    text-decoration: none;
    font-size: clamp(20px, 4vw, 34px);
    font-weight: 900;
    word-break: break-word;
  }
  .email:hover { color: #caff4a; }
  footer {
    margin-top: 28px;
    color: #777181;
    font-size: 12px;
    letter-spacing: .12em;
  }
  @media (max-width: 700px) {
    .team { grid-template-columns: 1fr; }
    section { padding: 22px 16px; }
  }
</style>
</head>
<body>
<div class="noise"></div>

<main>
  <div class="badge">INDIE GAME STUDIO • 2026</div>

  <div class="logo-wrap">
    <canvas id="logo" width="1000" height="360" aria-label="ATCG logo"></canvas>
  </div>

  <p class="tagline">
    WE MAKE GAMES THAT ARE <span>WEIRD, PLAYFUL &amp; ALIVE.</span>
  </p>

  <section>
    <h2>The Team</h2>
    <div class="team">
      <div class="member"><strong>NOA</strong><small>CEO</small></div>
      <div class="member"><strong>JONATHAN</strong><small>PROGRAMMER</small></div>
      <div class="member"><strong>YASMIN</strong><small>TECH ARTIST</small></div>
    </div>
  </section>

  <section>
    <h2>Watch Us Play</h2>
    <div class="video" id="videoBox">
      <p>Replace this panel with your YouTube video embed.</p>
    </div>
  </section>

  <section class="contact">
    <h2>Let's Make Something</h2>
    <a class="email" href="mailto:contact@playatcg.com">contact@playatcg.com</a>
  </section>

  <footer>ATCG — PLAY. BREAK. CREATE.</footer>
</main>

<script>
const canvas = document.getElementById("logo");
const ctx = canvas.getContext("2d");

function drawLogo() {
  const w = canvas.width, h = canvas.height;
  ctx.clearRect(0, 0, w, h);

  // playful DNA/game-inspired helix
  ctx.save();
  ctx.translate(w / 2, 42);

  ctx.lineWidth = 12;
  ctx.lineCap = "round";

  const colors = ["#caff4a", "#b46cff", "#59f0ff", "#ff5c9a"];

  for (let strand = 0; strand < 2; strand++) {
    ctx.beginPath();
    for (let x = -300; x <= 300; x += 5) {
      const y = 105 + Math.sin(x / 55) * 48 * (strand ? -1 : 1);
      if (x === -300) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.strokeStyle = colors[strand];
    ctx.stroke();
  }

  // connecting "DNA" / controller bars
  for (let x = -275; x <= 275; x += 55) {
    const a = Math.sin(x / 55) * 48;
    ctx.beginPath();
    ctx.moveTo(x, 105 - a);
    ctx.lineTo(x, 105 + a);
    ctx.strokeStyle = "rgba(255,255,255,.34)";
    ctx.lineWidth = 5;
    ctx.stroke();
  }

  ctx.restore();

  // ATCG wordmark
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.font = "900 170px Arial Black, Arial, sans-serif";
  ctx.shadowColor = "rgba(202,255,74,.22)";
  ctx.shadowBlur = 22;
  ctx.fillStyle = "#ffffff";
  ctx.fillText("ATCG", w/2, 240);

  // small accent
  ctx.shadowBlur = 0;
  ctx.font = "800 22px Arial, sans-serif";
  ctx.fillStyle = "#caff4a";
  ctx.letterSpacing = "8px";
  ctx.fillText("PLAY SOMETHING DIFFERENT", w/2, 326);
}
drawLogo();
</script>
</body>
</html>
'''

path = Path("ATCG_landing_page.html")
path.write_text(html, encoding="utf-8")
print(f"Created: {path}")
