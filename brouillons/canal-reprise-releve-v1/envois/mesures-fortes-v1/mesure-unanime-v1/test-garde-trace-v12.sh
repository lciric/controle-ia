#!/bin/bash
# Test déposé (R5, CV10-1) de la garde `garde-trace-reelle-v12.sh` : un état **sain** (y compris avec le sous-dossier
# `repetition-v12/` et ses fichiers `sortie-reelle-v12-...`) passe ; chaque trace réelle plantée bloque (code 3).
set -uo pipefail
cd "$(dirname "$(readlink -f "$0")")"
G="$(readlink -f garde-trace-reelle-v12.sh)"
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
essai() { # $1 nom attendu, $2 code attendu
  ( cd "$tmp/d" && bash "$G" ) >/dev/null 2>&1; local c=$?
  [ "$c" = "$2" ] && echo "OK   $1 → code $c" || { echo "ÉCHEC $1 → code $c attendu $2"; FAIL=1; }
}
FAIL=0
# sain : un sous-dossier de répétition ne bloque pas, même avec des noms sortie-reelle-v12-*
rm -rf "$tmp/d"; mkdir -p "$tmp/d/repetition-v12"; : > "$tmp/d/repetition-v12/sortie-reelle-v12.json"; essai "sain + répétition" 0
rm -rf "$tmp/d"; mkdir -p "$tmp/d"; : > "$tmp/d/execution-reelle-v12.commencee"; essai "témoin posé" 3
rm -rf "$tmp/d"; mkdir -p "$tmp/d"; : > "$tmp/d/sortie-reelle-v12.json"; essai "sortie finale" 3
rm -rf "$tmp/d"; mkdir -p "$tmp/d"; : > "$tmp/d/sortie-reelle-v12.json.partiel"; essai "partiel" 3
rm -rf "$tmp/d"; mkdir -p "$tmp/d"; essai "dossier vide" 0
[ "$FAIL" = 0 ] && echo "garde-trace : tous les cas conformes" || { echo "garde-trace : AU MOINS UN ÉCHEC"; exit 1; }
