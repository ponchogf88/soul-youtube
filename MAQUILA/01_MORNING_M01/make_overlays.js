const fs = require('fs');

function makeSvg(text1, text2, filename) {
  const svg = `
<svg width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.8"/>
    </filter>
  </defs>
  <style>
    .title { font-family: -apple-system, BlinkMacSystemFont, "Georgia", "Helvetica Neue", sans-serif; font-size: 38px; fill: #FFFFFF; font-weight: 500; filter: url(#shadow); }
    .subtitle { font-family: -apple-system, BlinkMacSystemFont, "Georgia", "Helvetica Neue", sans-serif; font-size: 28px; fill: #FFD700; font-weight: 400; filter: url(#shadow); }
  </style>
  <text x="960" y="960" text-anchor="middle" class="title">${text1}</text>
  ${text2 ? `<text x="960" y="1010" text-anchor="middle" class="subtitle">${text2}</text>` : ''}
</svg>`;
  fs.writeFileSync(filename, svg.trim());
}

makeSvg("Detén un momento el paso... Respira la paz de este día.", "", "overlay_1.svg");
makeSvg('"Nuevas son cada mañana sus misericordias; grande es tu fidelidad."', "— Lamentaciones 3:23", "overlay_2.svg");
makeSvg("Dios bendiga tu hogar hoy y siempre.", "Escribe AMÉN para recibir esta paz", "overlay_3.svg");
console.log("SVGs creados correctamente.");
