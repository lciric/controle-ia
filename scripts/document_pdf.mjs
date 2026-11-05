// Met en page un document HTML autonome en PDF A4 avec Chromium (Playwright), numéros de page en pied.
// Usage : node scripts/document_pdf.mjs ENTREE.html SORTIE.pdf "Pied de page"
// Chromium : PLAYWRIGHT_BROWSERS_PATH (préinstallé), jamais téléchargé ici. Playwright est cherché par require,
// donc aussi dans NODE_PATH (par exemple NODE_PATH=$(npm root -g)), qu'un import ESM ignorerait.
import { createRequire } from "node:module";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";

const { chromium } = createRequire(import.meta.url)("playwright");

const [entree, sortie, pied = ""] = process.argv.slice(2);
if (!entree || !sortie) {
  console.error("usage : node scripts/document_pdf.mjs ENTREE.html SORTIE.pdf [pied]");
  process.exit(2);
}
const echapper = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const navigateur = await chromium.launch();
try {
  const page = await navigateur.newPage();
  await page.goto(pathToFileURL(resolve(entree)).href, { waitUntil: "load" });
  await page.pdf({
    path: sortie,
    format: "A4",
    preferCSSPageSize: true,
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: "<span></span>",
    footerTemplate:
      '<div style="width:100%;font-family:Liberation Sans,DejaVu Sans,sans-serif;font-size:7.5pt;color:#57606a;' +
      'padding:0 17mm;display:flex;justify-content:space-between;">' +
      `<span>${echapper(pied)}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
  });
} finally {
  await navigateur.close();
}
console.log(`PDF écrit : ${sortie}`);
