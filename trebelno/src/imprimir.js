// Convierte los HTML a PDF A4 con pie de página numerado.
const { chromium } = require('playwright');
const path = require('path');

const docs = [
  ['cuestionario.html', 'Trebelno_Cuestionario_Comercial.pdf', 'Cuestionario comercial', '#8c6f72'],
  ['00_estrategia.html', 'Trebelno_00_Estrategia_y_Campana.pdf', '00 · Estrategia y campaña', '#8a8178'],
  ['01_guiones.html', 'Trebelno_01_Guiones.pdf', '01 · Guiones', '#8a8178'],
  ['02_grabacion.html', 'Trebelno_02_Plan_de_Grabacion.pdf', '02 · Plan de grabación', '#8a8178'],
  ['03_edicion.html', 'Trebelno_03_Plan_de_Edicion.pdf', '03 · Plan de edición', '#8a8178'],
];

(async () => {
  const browser = await chromium.launch();
  for (const [src, out, nombre, color] of docs) {
    const page = await browser.newPage();
    await page.goto('file://' + path.join(__dirname, src), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({
      path: path.join(__dirname, '..', 'pdf', out), format: 'A4', printBackground: true, preferCSSPageSize: true,
      displayHeaderFooter: true, headerTemplate: '<span></span>',
      footerTemplate: `<div style="width:100%;font-family:Inter,sans-serif;font-size:7px;letter-spacing:.14em;text-transform:uppercase;color:${color};padding:0 14mm;display:flex;justify-content:space-between;">
        <span>Trebelno Recepciones · Agenda 2027 · ${nombre}</span><span>Hoja <span class="pageNumber"></span> de <span class="totalPages"></span></span></div>`,
    });
    console.log('PDF', out);
    await page.close();
  }
  await browser.close();
})();
