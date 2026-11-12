#!/bin/bash
# Lance les recoupements de puissance de la synthèse P-26 (session-depot, sous-agent de synthèse), processeur seul.
# Chaque ligne de travaux-recoupement-v1.txt : nom|arguments. Sortie JSON dans sorties/, erreurs dans journaux/.
set -u
ICI=$(cd "$(dirname "$0")" && pwd)
SCRIPT="$ICI/script-v4-copie/simulation-puissance-garde-delta-v4.py"
JOURNAL="$ICI/journaux/journal-recoupements-v1.txt"
echo "debut $(date -u +%FT%TZ) script $(sha256sum "$SCRIPT" | cut -c1-64) python $(python3 --version 2>&1) numpy $(python3 -c 'import numpy;print(numpy.__version__)')" >> "$JOURNAL"
grep -v '^#' "$ICI/travaux-recoupement-v1.txt" | grep -v '^$' | while IFS='|' read -r nom args; do
  printf '%s\0%s\0' "$nom" "$args"
done | xargs -0 -n2 -P3 bash -c '
  nom="$0"; args="$1"; t0=$(date +%s)
  python3 -I -B "'"$SCRIPT"'" $args > "'"$ICI"'/sorties/$nom.json" 2> "'"$ICI"'/journaux/$nom.err"
  rc=$?; echo "$(date -u +%FT%TZ) $nom rc=$rc duree=$(( $(date +%s)-t0 ))s commande: python3 -I -B simulation-puissance-garde-delta-v4.py $args" >> "'"$JOURNAL"'"
'
echo "fin $(date -u +%FT%TZ)" >> "$JOURNAL"
