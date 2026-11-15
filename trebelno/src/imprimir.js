// Convierte los HTML a PDF A4 con pie de página numerado.
const { chromium } = require('playwright');
const path = require('path');

const docs = [
  ['guiones.html', '../pdf/Trebelno_Kit_de_Rodaje_Agenda2027.pdf', 'Kit de rodaje · Agenda 2027'],
  ['cuestionario.html', '../pdf/Trebelno_Cuestionario_Oferta_Comercial.pdf', 'Cuestionario comercial'],
];

(async () => {
  const browser = await chromium.launch();
  for (const [src, out, nombre] of docs) {
    const page = await browser.newPage();
    await page.goto('file://' + path.join(__dirname, src), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({
      path: path.join(__dirname, out), format: 'A4', printBackground: true, preferCSSPageSize: true,
      displayHeaderFooter: true, headerTemplate: '<span></span>',
      footerTemplate: `<div style="width:100%;font-family:Inter,sans-serif;font-size:7px;letter-spacing:.14em;text-transform:uppercase;color:#8a8178;padding:0 14mm;display:flex;justify-content:space-between;">
        <span>Trebelno Recepciones · ${nombre}</span><span>Hoja <span class="pageNumber"></span> de <span class="totalPages"></span></span></div>`,
    });
    console.log('PDF', out);
    await page.close();
  }
  await browser.close();
})();
