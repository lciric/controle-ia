#!/bin/bash
# Test R5 du mode LECTURE_SEULE de commandes-lecture-reelle-v12.sh (reprise des étapes (3) et (4) après une interruption qui
# survient APRÈS l'étape (2)). Ferme CV11-1 : la v11 mourait en silence (code 1, sans message) dès que la note n'était pas
# scellée, c.-à-d. le cas même que la reprise doit traiter. On vérifie ici, sur une COPIE de travail isolée et une sortie
# ARTEFACT scellée (jamais les données réelles de donnees/) :
#   (A) la garde isolée garde-lecture-seule-v12.sh en direct : note absente → 0 (cas sain), note scellée → 7 (artefact) ;
#   (B) le mode LECTURE_SEULE de bout en bout : commit ≠ manifeste → 8 ; cas sain → 0 (note refaite et scellée) ;
#       second appel → 7 (note déjà scellée, rien réécrit) ; sortie finale absente → 6.
# La sortie artefact est fabriquée sur un petit npz synthétique (3 sondes réelles, 2 placebo : quelques secondes), puis son
# empreinte de données au manifeste est RETOUCHÉE (artefact assumé) vers l'empreinte réelle attendue, pour que la lecture
# mécanique accepte le manifeste sans relire aucune donnée (elle lit la sortie JSON, jamais le npz).
set -uo pipefail
cd "$(dirname "$(readlink -f "$0")")"
SRC="$PWD"
PY=/opt/venv-essaim-sim-v1/bin/python
export PYTHONPATH=/home/claude/canal-conv-audit-n04/src
EMP_REELLE=968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf
echec() { echo "ÉCHEC $1" >&2; exit 1; }
TMP=""; TMPG=""
trap 'rm -rf "$TMP" "$TMPG"' EXIT

# (A) garde isolée, en direct : cas sain (note absente → 0) et artefact (note scellée → 7)
TMPG=$(mktemp -d)
echo "note factice" > "$TMPG/note.md"
set +e; bash "$SRC/garde-lecture-seule-v12.sh" "$TMPG/note.md" >/dev/null 2>&1; rc=$?; set -e
[ "$rc" = 0 ] || echec "(A) garde isolée, note absente : attendu 0, obtenu $rc"
echo "empreinte factice" > "$TMPG/note.md.sha256"
set +e; bash "$SRC/garde-lecture-seule-v12.sh" "$TMPG/note.md" >/dev/null 2>&1; rc=$?; set -e
[ "$rc" = 7 ] || echec "(A) garde isolée, note scellée : attendu 7, obtenu $rc"

# (B) mode LECTURE_SEULE de bout en bout, sur une copie isolée + sortie artefact scellée
TMP=$(mktemp -d)
for f in analyse_fausses_alertes_v8.py table_m2bis_m4_v8.py table-m2bis-m4-v8.json \
         lecture_mecanique_v8.py rediger_note_lecture_v6.py commandes-lecture-reelle-v12.sh \
         garde-trace-reelle-v12.sh test-garde-trace-v12.sh garde-lecture-seule-v12.sh test-lecture-seule-v12.sh \
         preenregistrement-mesure-unanime-v12.md; do
  cp "$SRC/$f" "$TMP/" || echec "copie de $f"
  [ -e "$SRC/$f.sha256" ] && cp "$SRC/$f.sha256" "$TMP/"
done
cd "$TMP"
$PY -B -m controle_ia.scellement sceller preenregistrement-mesure-unanime-v12.md >/dev/null || echec "scellement de la copie du préenregistrement"
SYN="$TMP/syn.npz"
$PY -I -B analyse_fausses_alertes_v8.py --ecrire-npz-synthetique "$SYN" --npz-sondes 3,2 >/dev/null || echec "écriture du npz synthétique"
EMPS=$(sha256sum "$SYN" | cut -d' ' -f1)
$PY -I -B analyse_fausses_alertes_v8.py --reel "$SYN" --empreinte-attendue "$EMPS" --sondes-reelles 3 --sondes-placebo 2 --commit COMMITTEST > sortie-reelle-v12.json || echec "fabrication de la sortie artefact"
$PY -I -B -c "import json; d=json.load(open('sortie-reelle-v12.json')); d['manifeste']['empreinte_donnees']='$EMP_REELLE'; json.dump(d, open('sortie-reelle-v12.json','w'))" || echec "retouche de l'empreinte de données"
$PY -B -m controle_ia.scellement sceller sortie-reelle-v12.json >/dev/null || echec "scellement de la sortie artefact"
echo table-m2bis-m4-v8.json > table-en-vigueur-v12.txt
$PY -B -m controle_ia.scellement sceller table-en-vigueur-v12.txt >/dev/null || echec "scellement de la table en vigueur"

# (B1) commit ≠ manifeste → 8 (note pas encore écrite ; la garde isolée laisse passer, puis le commit est comparé, ligne 68)
set +e; MESURE_INSTANCE="test R5" bash commandes-lecture-reelle-v12.sh LECTURE_SEULE MAUVAIS_COMMIT >/dev/null 2>&1; rc=$?; set -e
[ "$rc" = 8 ] || echec "(B1) commit ≠ manifeste : attendu 8, obtenu $rc"
[ -e note-lecture-mecanique-v12.md ] && echec "(B1) une note a été écrite malgré le refus 8"
# (B2) cas sain → 0, note refaite et scellée
set +e; MESURE_INSTANCE="test R5" bash commandes-lecture-reelle-v12.sh LECTURE_SEULE COMMITTEST >/dev/null 2>&1; rc=$?; set -e
[ "$rc" = 0 ] || echec "(B2) cas sain : attendu 0, obtenu $rc"
[ -e note-lecture-mecanique-v12.md.sha256 ] || echec "(B2) cas sain : la note n'est pas scellée"
# (B3) second appel → 7 (note déjà scellée) ; lecture scellée inchangée
emp_avant=$(sha256sum lecture-mecanique-reelle-v12.json | cut -d' ' -f1)
set +e; MESURE_INSTANCE="test R5" bash commandes-lecture-reelle-v12.sh LECTURE_SEULE COMMITTEST >/dev/null 2>&1; rc=$?; set -e
[ "$rc" = 7 ] || echec "(B3) second appel : attendu 7, obtenu $rc"
emp_apres=$(sha256sum lecture-mecanique-reelle-v12.json | cut -d' ' -f1)
[ "$emp_avant" = "$emp_apres" ] || echec "(B3) second appel : la lecture scellée a été réécrite"
# (B4) sortie finale absente → 6
rm -f sortie-reelle-v12.json sortie-reelle-v12.json.sha256 note-lecture-mecanique-v12.md note-lecture-mecanique-v12.md.sha256
set +e; MESURE_INSTANCE="test R5" bash commandes-lecture-reelle-v12.sh LECTURE_SEULE COMMITTEST >/dev/null 2>&1; rc=$?; set -e
[ "$rc" = 6 ] || echec "(B4) sortie absente : attendu 6, obtenu $rc"

cd "$SRC"
echo "test-lecture-seule : (A) garde isolée 0/7 ; (B) mode LECTURE_SEULE 8 (commit), 0 (sain, note refaite), 7 (déjà scellée), 6 (sans sortie) — conformes"
