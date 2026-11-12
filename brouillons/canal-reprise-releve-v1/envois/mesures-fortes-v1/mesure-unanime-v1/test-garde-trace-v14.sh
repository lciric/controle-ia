#!/bin/bash
# Test déposé (R5, CV10-1, CV13-1) de la garde `garde-trace-reelle-v14.sh` : un état **sain** (y compris avec le sous-dossier
# `repetition-v14/` et ses fichiers `sortie-reelle-v14.json`) passe ; chaque trace réelle plantée bloque (code 3). Vérifie
# aussi que les noms plantés sont les noms que la séquence v14 utilise réellement (CV13-1 : les noms de la séquence **sont**
# les noms du test, plus de noms codés en dur qui divergent).
set -uo pipefail
cd "$(dirname "$(readlink -f "$0")")"
G="$(readlink -f garde-trace-reelle-v14.sh)"
# les trois noms que la séquence v14 pose (mêmes variables que la séquence)
TEMOIN=execution-reelle-v14.commencee
SORTIE=sortie-reelle-v14.json
PARTIEL="$SORTIE.partiel"
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
essai() { # $1 nom attendu, $2 code attendu
  ( cd "$tmp/d" && bash "$G" "$TEMOIN" "$SORTIE" "$PARTIEL" ) >/dev/null 2>&1; local c=$?
  [ "$c" = "$2" ] && echo "OK   $1 → code $c" || { echo "ÉCHEC $1 → code $c attendu $2"; FAIL=1; }
}
FAIL=0
# sain : un sous-dossier de répétition ne bloque pas, même avec des noms sortie-reelle-v14-*
rm -rf "$tmp/d"; mkdir -p "$tmp/d/repetition-v14"; : > "$tmp/d/repetition-v14/sortie-reelle-v14.json"; essai "sain + répétition" 0
rm -rf "$tmp/d"; mkdir -p "$tmp/d"; : > "$tmp/d/$TEMOIN"; essai "témoin posé" 3
rm -rf "$tmp/d"; mkdir -p "$tmp/d"; : > "$tmp/d/$SORTIE"; essai "sortie finale" 3
rm -rf "$tmp/d"; mkdir -p "$tmp/d"; : > "$tmp/d/$PARTIEL"; essai "partiel" 3
rm -rf "$tmp/d"; mkdir -p "$tmp/d"; essai "dossier vide" 0
# vérifie que les noms du test sont ceux de la séquence v14 (CV13-1 : jamais de divergence)
SEQ=commandes-lecture-reelle-v14.sh
if [ -e "$SEQ" ]; then
  grep -q "TEMOIN=execution-reelle-v14.commencee" "$SEQ" || { echo "ÉCHEC : le TEMOIN de la séquence ne correspond pas"; FAIL=1; }
  grep -q "sortie-reelle-v14.json" "$SEQ" || { echo "ÉCHEC : la SORTIE de la séquence ne correspond pas"; FAIL=1; }
  echo "OK   noms du test = noms de la séquence v14"
else
  echo "INFO séquence v14 absente (pas encore déposée) ; vérification des noms reportée"
fi
[ "$FAIL" = 0 ] && echo "garde-trace : tous les cas conformes" || { echo "garde-trace : AU MOINS UN ÉCHEC"; exit 1; }
