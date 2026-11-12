"""Construit le PDF d'un rapport au directeur à partir de sa source HTML.

Usage : python -I construire-rapport-pdf-v1.py SOURCE.html SORTIE.pdf DOSSIER_TEMPORAIRE "PIED DE PAGE"

Deux étapes : (1) typographie française sur les seuls nœuds de texte du corps
(espaces insécables, apostrophes, groupes de chiffres) ; (2) rendu A4 par le
Chromium installé, piloté par Playwright (Node). Aucune lecture hors des
chemins donnés ; aucun appel réseau.
"""
import pathlib
import re
import subprocess
import sys

INSECABLE = chr(0x00A0)  # espace insécable
FINE = chr(0x202F)  # espace fine insécable


def typographier(texte: str) -> str:
    texte = texte.replace("'", chr(0x2019))
    texte = re.sub(r"(\d) (\d{3})(?!\d)", rf"\1{FINE}\2", texte)
    texte = texte.replace("« ", "«" + INSECABLE).replace(" »", INSECABLE + "»")
    texte = texte.replace(" :", INSECABLE + ":")
    for signe in (";", "?", "!"):
        texte = texte.replace(" " + signe, FINE + signe)
    texte = texte.replace(" %", INSECABLE + "%")
    texte = re.sub(r"(\d) (dollars|UTC)\b", rf"\1{INSECABLE}\2", texte)
    texte = re.sub(r"(\d{2}:\d{2}) UTC", rf"\1{INSECABLE}UTC", texte)
    return texte


def main() -> int:
    source, sortie, temporaire, pied = sys.argv[1:5]
    html = pathlib.Path(source).read_text(encoding="utf-8")
    tete, corps = html.split("<body>", 1)
    morceaux = re.split(r"(<[^>]+>)", corps)
    corps = "".join(m if m.startswith("<") else typographier(m) for m in morceaux)
    tmp = pathlib.Path(temporaire)
    tmp.mkdir(parents=True, exist_ok=True)
    page = tmp / "rendu.html"
    page.write_text(tete + "<body>" + corps, encoding="utf-8")
    script = tmp / "rendre.js"
    script.write_text(
        """
const { chromium } = require('playwright');
(async () => {
  const [src, out, pied] = process.argv.slice(2);
  const nav = await chromium.launch();
  const p = await nav.newPage();
  await p.goto('file://' + src);
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({
    path: out, format: 'A4', printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: `<div style="font-family: Carlito, sans-serif; font-size: 7.4pt; color: #56636f; width: 100%; padding: 0 16mm; display: flex; justify-content: space-between;"><span>${pied}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
    margin: { top: '15mm', bottom: '16mm', left: '16mm', right: '16mm' },
  });
  await nav.close();
})();
""",
        encoding="utf-8",
    )
    return subprocess.run(["node", str(script), str(page.resolve()), str(pathlib.Path(sortie).resolve()), pied], check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
