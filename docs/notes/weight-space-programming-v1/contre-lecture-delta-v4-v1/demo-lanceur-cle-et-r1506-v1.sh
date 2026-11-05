#!/usr/bin/env bash
# Démonstrations sur le lanceur v4 (53d4eda6), sans réseau : vastai factice, aucune clé réelle.
# (1) la commande de destruction imprimée retire VAST_API_KEY (env -i) ; un refus sur stderr avec le code 0 s'affiche « code 0 » ;
# (2) apres-creation sur un refus R-1506 (code 0, stderr seul) ; (3) certificat et identifiant dans la même sortie ; (4) forme --raw.
set -u
L=/home/claude/wt/sparks-exp7-nul-v4/scripts/lancer_sparks_exp7_nul_v4.sh
S=$(mktemp -d); mkdir -p "$S/fb" "$S/home"
printf '#!/bin/bash\nenv | cut -d= -f1 | sort > "%s/env-vu.txt"\necho "failed with error 401: missing api key" >&2\nexit 0\n' "$S" > "$S/fb/vastai"; chmod +x "$S/fb/vastai"
CMD=$(env -i PATH=/usr/bin:/bin HOME="$S/home" SPARKS_ETAT_DIR="$S/etat" HTTPS_PROXY=http://p:1 bash "$L" destruction 59079406 | grep "vastai destroy instance")
echo "(1) session avec VAST_API_KEY=factice :"; env -i PATH="$S/fb:/usr/bin:/bin" HOME="$S/home" HTTPS_PROXY=http://p:1 VAST_API_KEY=factice bash -c "$CMD"
echo "    variables vues par vastai : $(tr '\n' ' ' < "$S/env-vu.txt")"
printf 'failed with error 404/3603: no_such_ask ... not available\n' > "$S/r1506.txt"
echo "(2) refus R-1506, code 0 :"; env -i PATH=/usr/bin:/bin HOME="$S/home" SPARKS_ETAT_DIR="$S/etat" bash "$L" apres-creation "$S/r1506.txt" 0; echo "    code $?"
rm -f "$S/etat/.creation-incertaine"
printf "SSLError: CERTIFICATE_VERIFY_FAILED (requête annexe)\nStarted. {'success': True, 'new_contract': 59079406}\n" > "$S/mixte.txt"
echo "(3) certificat et identifiant :"; env -i PATH=/usr/bin:/bin HOME="$S/home" SPARKS_ETAT_DIR="$S/etat" bash "$L" apres-creation "$S/mixte.txt" 0; echo "    code $? ; marqueur : $(ls -A "$S/etat" | grep -c creation-incertaine)"
printf '{"success": true, "new_contract": 59079406}\n' > "$S/raw.txt"
echo "(4) forme --raw :"; env -i PATH=/usr/bin:/bin HOME="$S/home" SPARKS_ETAT_DIR="$S/etat" bash "$L" apres-creation "$S/raw.txt" 0; echo "    code $?"
rm -rf "$S"
