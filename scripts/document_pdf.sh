#!/usr/bin/env bash
# Markdown → HTML autonome (pandoc du venv) → PDF A4 (Chromium par Playwright, numéros de page).
# Usage : scripts/document_pdf.sh DOCUMENT.md FEUILLE.css SORTIE.pdf "Pied de page" [SORTIE.docx]
# Le HTML intermédiaire va dans un dossier temporaire, effacé à la fin ; rien n'est écrit ailleurs que SORTIE.
set -euo pipefail
racine="$(cd "$(dirname "$0")/.." && pwd)"
pandoc="$racine/.venv/lib/python3.11/site-packages/pypandoc/files/pandoc"
[ "$#" -ge 4 ] || { echo "usage : $0 DOCUMENT.md FEUILLE.css SORTIE.pdf PIED [SORTIE.docx]" >&2; exit 2; }
md="$1"; css="$2"; pdf="$3"; pied="$4"; docx="${5:-}"
[ -x "$pandoc" ] || { echo "pandoc introuvable : $pandoc" >&2; exit 1; }
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
"$pandoc" "$md" -f markdown -t html5 --standalone --embed-resources --css "$css" -o "$tmp/document.html"
NODE_PATH="$(npm root -g)" node "$racine/scripts/document_pdf.mjs" "$tmp/document.html" "$pdf" "$pied"
if [ -n "$docx" ]; then
  "$pandoc" "$md" -f markdown -t docx -o "$docx"
  echo "DOCX écrit : $docx"
fi
