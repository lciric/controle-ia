#!/bin/bash
# Contre-lecture v12 — exercice du mode LECTURE_SEULE de commandes-lecture-reelle-v12.sh sur une COPIE isolée du dossier
# (jamais le dépôt, jamais donnees/). La sortie « réelle » est un ARTEFACT fabriqué sur un petit npz synthétique, dont
# l'empreinte de données au manifeste est retouchée vers l'empreinte réelle attendue (comme le test déposé), pour que la
# lecture mécanique accepte le manifeste sans qu'aucune donnée réelle soit lue.
# Cas : 0 (sans MESURE_INSTANCE), A (préenregistrement non scellé), B (scellé, sans sortie), C (sortie non scellée),
# C bis (sortie scellée puis corrompue), D1 (table en vigueur absente), D1 bis (compagnon de la table en vigueur faux),
# D2 (commit ≠ manifeste), D3 (empreinte des données ≠ réelle), E (cas sain → 0), F (second appel → 7, rien réécrit),
# G (note retirée, lecture scellée intacte → 0, lecture intacte), G ter (lecture scellée puis corrompue d'un octet → refus à
# l'étape (3), aucune note), G quater (lecture présente non scellée → refaite à l'identique), H (`.partiel` de lecture
# laissé → refait), I (note présente non scellée → refaite).
# Usage : bash lecture_seule_cv12_v1.sh DOSSIER_SOURCE_COPIE DOSSIER_DE_TRAVAIL
set -uo pipefail
SRC="${1:?copie source du dossier}"; W="${2:?dossier de travail}"
PY=/opt/venv-essaim-sim-v1/bin/python
export PYTHONPATH=/home/claude/canal-conv-audit-n04/src
EMP_REELLE=968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf
rm -rf "$W"; mkdir -p "$W"
for f in analyse_fausses_alertes_v8.py table_m2bis_m4_v8.py table-m2bis-m4-v8.json lecture_mecanique_v8.py rediger_note_lecture_v6.py \
         commandes-lecture-reelle-v12.sh garde-trace-reelle-v12.sh test-garde-trace-v12.sh garde-lecture-seule-v12.sh test-lecture-seule-v12.sh \
         preenregistrement-mesure-unanime-v12.md; do
  cp "$SRC/$f" "$W/"; [ -e "$SRC/$f.sha256" ] && cp "$SRC/$f.sha256" "$W/"
done
cd "$W"
SEQ="bash commandes-lecture-reelle-v12.sh LECTURE_SEULE"
lance() { # $1 étiquette, $2 code attendu, reste : commande
  local et="$1" att="$2"; shift 2
  rm -f journal-lecture-reelle-v12.log
  "$@" > "ls-$et.out" 2>&1; local rc=$?
  local j=""; [ -e journal-lecture-reelle-v12.log ] && j=$(tail -n 2 journal-lecture-reelle-v12.log | tr '\n' ' ' | cut -c1-230)
  local verdict="OK"; [ "$rc" = "$att" ] || verdict="ÉCART"
  printf '%-6s %-8s code %-3s (attendu %-3s) | dernière(s) ligne(s) du journal : %s\n' "$et" "$verdict" "$rc" "$att" "${j:-$(tail -n 1 "ls-$et.out" | cut -c1-200)}"
}
etat() { ls -1 | grep -E '^(lecture-mecanique-reelle-v12|note-lecture-mecanique-v12|sortie-reelle-v12|table-en-vigueur-v12)' | tr '\n' ' '; echo; }

echo "== cas 0 : sans MESURE_INSTANCE (attendu 1, message « MESURE_INSTANCE obligatoire »)"
lance cas0 1 env -u MESURE_INSTANCE bash commandes-lecture-reelle-v12.sh LECTURE_SEULE abc1234
grep -o 'MESURE_INSTANCE obligatoire[^"]*' ls-cas0.out | head -1

echo "== cas A : préenregistrement non scellé (attendu 1, GardeArret)"
lance casA 1 env MESURE_INSTANCE=x $SEQ abc1234
grep -o 'GardeArret[^\n]*' ls-casA.out journal-lecture-reelle-v12.log 2>/dev/null | head -1 | cut -c1-200

$PY -B -m controle_ia.scellement sceller preenregistrement-mesure-unanime-v12.md > /dev/null
echo "== cas B : préenregistrement scellé (copie), aucune sortie (attendu 6)"
lance casB 6 env MESURE_INSTANCE=x $SEQ abc1234

echo "== fabrication de la sortie ARTEFACT (npz synthétique 3 + 2 sondes ; empreinte de données retouchée vers la réelle)"
$PY -I -B analyse_fausses_alertes_v8.py --ecrire-npz-synthetique "$W/syn.npz" --npz-sondes 3,2 > /dev/null
EMPS=$(sha256sum syn.npz | cut -d' ' -f1)
$PY -I -B analyse_fausses_alertes_v8.py --reel "$W/syn.npz" --empreinte-attendue "$EMPS" --sondes-reelles 3 --sondes-placebo 2 --commit abc1234 > sortie-reelle-v12.json.brute
$PY -I -B -c "import json; d=json.load(open('sortie-reelle-v12.json.brute')); d['manifeste']['empreinte_donnees']='$EMP_REELLE'; json.dump(d, open('sortie-reelle-v12.json','w'))"
echo "artefact : $(wc -c < sortie-reelle-v12.json) octets ; empreinte_donnees retouchée = $EMP_REELLE"

echo "== cas C : sortie présente, non scellée (attendu 6)"
lance casC 6 env MESURE_INSTANCE=x $SEQ abc1234

$PY -B -m controle_ia.scellement sceller sortie-reelle-v12.json > /dev/null
echo "== cas C bis : sortie scellée puis corrompue d'un octet (attendu ≠ 0, message du vérificateur, aucune lecture écrite)"
cp sortie-reelle-v12.json sortie-reelle-v12.json.intacte
printf ' ' >> sortie-reelle-v12.json
lance casCb 1 env MESURE_INSTANCE=x $SEQ abc1234
grep -oiE '(empreinte|diff|corromp|GardeArret)[^\n]{0,120}' ls-casCb.out | head -2
cp sortie-reelle-v12.json.intacte sortie-reelle-v12.json; rm sortie-reelle-v12.json.intacte
echo "   état après C bis : $(etat)"

echo "== cas D1 : table en vigueur absente (attendu ≠ 0, message de cat)"
lance casD1 1 env MESURE_INSTANCE=x $SEQ abc1234

echo table-m2bis-m4-v8.json > table-en-vigueur-v12.txt
$PY -B -m controle_ia.scellement sceller table-en-vigueur-v12.txt > /dev/null
echo "== cas D1 bis : compagnon de la table en vigueur faux (attendu ≠ 0, sha256sum)"
cp table-en-vigueur-v12.txt.sha256 tev.sha256.sauve
sed -i 's/^./0/' table-en-vigueur-v12.txt.sha256
lance casD1b 1 env MESURE_INSTANCE=x $SEQ abc1234
cp tev.sha256.sauve table-en-vigueur-v12.txt.sha256; rm tev.sha256.sauve
echo "   état après D1 bis : $(etat)"

echo "== cas D2 : commit ≠ manifeste (attendu 8)"
lance casD2 8 env MESURE_INSTANCE=x $SEQ pas-le-bon-commit
echo "   état après D2 : $(etat)"

echo "== cas D3 : empreinte des données du manifeste ≠ réelle (attendu : refus de la lecture à l'étape (3), code 1, aucune note)"
cp sortie-reelle-v12.json sortie-reelle-v12.json.sauve; cp sortie-reelle-v12.json.sha256 sortie-reelle-v12.json.sha256.sauve
$PY -I -B -c "import json; d=json.load(open('sortie-reelle-v12.json')); d['manifeste']['empreinte_donnees']='$EMPS'; json.dump(d, open('sortie-reelle-v12.json','w'))"
rm sortie-reelle-v12.json.sha256; $PY -B -m controle_ia.scellement sceller sortie-reelle-v12.json > /dev/null
lance casD3 1 env MESURE_INSTANCE=x $SEQ abc1234
grep -oiE 'empreinte[^\n]{0,160}' ls-casD3.out | head -2
echo "   état après D3 : $(etat)"
rm -f lecture-mecanique-reelle-v12.json.partiel
cp sortie-reelle-v12.json.sauve sortie-reelle-v12.json; cp sortie-reelle-v12.json.sha256.sauve sortie-reelle-v12.json.sha256; rm sortie-reelle-v12.json.sauve sortie-reelle-v12.json.sha256.sauve

echo "== cas E : cas sain (attendu 0 ; lecture et note écrites et scellées)"
lance casE 0 env MESURE_INSTANCE='contre-lecture v12 (Fable 5.1), artefact' $SEQ abc1234
echo "   état après E : $(etat)"
for f in lecture-mecanique-reelle-v12.json note-lecture-mecanique-v12.md; do sha256sum -c "$f.sha256"; done
sed -n '3p' note-lecture-mecanique-v12.md | cut -c1-300
grep -c 'RÉPÉTITION GÉNÉRALE' note-lecture-mecanique-v12.md | sed 's/^/   occurrences de « RÉPÉTITION GÉNÉRALE » dans la note (attendu 0 : commit ≠ repetition-generale) : /'

echo "== cas F : second appel (attendu 7 ; rien réécrit)"
sha256sum lecture-mecanique-reelle-v12.json lecture-mecanique-reelle-v12.json.sha256 note-lecture-mecanique-v12.md note-lecture-mecanique-v12.md.sha256 > avant-F.txt
lance casF 7 env MESURE_INSTANCE=x $SEQ abc1234
sha256sum -c avant-F.txt | sed 's/^/   /'

echo "== cas G : note et compagnon retirés, lecture scellée intacte (attendu 0 ; note refaite ; lecture et compagnon intacts)"
sha256sum lecture-mecanique-reelle-v12.json lecture-mecanique-reelle-v12.json.sha256 > avant-G.txt
touch -d '2000-01-01' lecture-mecanique-reelle-v12.json
rm note-lecture-mecanique-v12.md note-lecture-mecanique-v12.md.sha256
lance casG 0 env MESURE_INSTANCE=x $SEQ abc1234
sha256sum -c avant-G.txt | sed 's/^/   /'
echo "   date de la lecture (attendu 2000) : $(stat -c %y lecture-mecanique-reelle-v12.json | cut -c1-10) ; note : $(ls note-lecture-mecanique-v12.md* | tr '\n' ' ')"

echo "== cas G ter : lecture scellée puis corrompue d'un octet, note retirée (attendu : refus à l'étape (3), code ≠ 0, AUCUNE note)"
rm note-lecture-mecanique-v12.md note-lecture-mecanique-v12.md.sha256
cp lecture-mecanique-reelle-v12.json lecture-intacte.sauve
printf ' ' >> lecture-mecanique-reelle-v12.json
lance casGt 1 env MESURE_INSTANCE=x $SEQ abc1234
grep -oiE '(empreinte|diff|corromp|GardeArret)[^\n]{0,140}' ls-casGt.out | head -2
echo "   note écrite ? $(ls note-lecture-mecanique-v12.md* 2>/dev/null || echo 'aucune (attendu)')"
cp lecture-intacte.sauve lecture-mecanique-reelle-v12.json; rm lecture-intacte.sauve

echo "== cas G quater : lecture présente mais NON scellée (coupure entre mv et sceller) (attendu 0 ; lecture refaite à l'identique et scellée ; note écrite)"
EMPL=$(sha256sum lecture-mecanique-reelle-v12.json | cut -d' ' -f1)
rm lecture-mecanique-reelle-v12.json.sha256
lance casGq 0 env MESURE_INSTANCE=x $SEQ abc1234
echo "   lecture identique à l'octet ? $([ "$(sha256sum lecture-mecanique-reelle-v12.json | cut -d' ' -f1)" = "$EMPL" ] && echo oui || echo NON) ; état : $(etat)"

echo "== cas H : lecture absente, un .partiel de lecture laissé (coupure pendant l'étape (3)) ; note absente (attendu 0 ; lecture refaite, .partiel disparu)"
rm note-lecture-mecanique-v12.md note-lecture-mecanique-v12.md.sha256 lecture-mecanique-reelle-v12.json lecture-mecanique-reelle-v12.json.sha256
: > lecture-mecanique-reelle-v12.json.partiel
lance casH 0 env MESURE_INSTANCE=x $SEQ abc1234
echo "   lecture identique à l'octet ? $([ "$(sha256sum lecture-mecanique-reelle-v12.json | cut -d' ' -f1)" = "$EMPL" ] && echo oui || echo NON) ; état : $(etat)"

echo "== cas I : note présente mais NON scellée (coupure entre mv et sceller de la note) (attendu 0 ; note refaite et scellée)"
rm note-lecture-mecanique-v12.md.sha256
lance casI 0 env MESURE_INSTANCE=x $SEQ abc1234
echo "   état : $(etat)"

echo "== témoin et garde isolée, dans ce dossier de travail (hors de la séquence) : pose 1 → 0 ; pose 2 → 3 ; garde → 3"
( set -o noclobber; : > execution-reelle-v12.commencee ) 2>/dev/null; echo "   pose 1 : rc=$?"
( set -o noclobber; : > execution-reelle-v12.commencee ) 2>/dev/null; echo "   pose 2 : rc=$?"
bash garde-trace-reelle-v12.sh > /dev/null 2>&1; echo "   garde isolée : rc=$?"
echo '== relecture : où la séquence écrit « && { » (aucune ne doit finir une fonction)'
grep -nE '&& \{' commandes-lecture-reelle-v12.sh | cut -c1-160
echo "fin"
