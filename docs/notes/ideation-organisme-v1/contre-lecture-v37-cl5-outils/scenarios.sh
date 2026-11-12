#!/bin/bash
# Courses simulées de la relecture CL5 (aucun réseau ; Argon factice local). Usage : scenarios.sh S1|S2|…
B=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad
R=$B/relecture-v37
V=$R/v37/orchestrateur-pole-v7
S=$R/simulee
E=$S/entrees
PY=$B/venv-pole/bin/python
ARGON="$PY -I $R/outils-cl5/argon_factice.py"
lancer() { env -i PATH=/usr/bin:/bin HOME=$S LANG=C.UTF-8 $PY -I -B $V/demonstrations/ideation_v1.py "$@"; echo "code $?"; }
course() {  # course SORTIE MODE_ARGON [options…]
  local sortie=$1 mode=$2; shift 2
  lancer $S/$sortie --liste-blanche $E/liste-blanche.json --question $E/question.md --piece $E/piece-1.md \
    --piece $E/piece-2.md --temoins $E/temoins.json --proposeur-externe argon=gemini-argon --juge-externe argon=gemini-argon \
    --commande-externe "$ARGON $S/$sortie-argon.jsonl $mode" --horodatage "$(date -u)" "$@"
}
bras() {  # bras SORTIE MODE_ARGON JOURNAL
  lancer $S/$1 --bras-rapporte-differe --attestation-lecture-humaine $S/$1-att.json --juge-externe argon=gemini-argon \
    --commande-externe "$ARGON $S/$3 $2" --horodatage "$(date -u)"
}
case $1 in
  S1) course S1 ok --taille-max-pieces 650000 ;;
  S2) course S2 ok ;;                                   # défaut 400 000 oublié
  S2bis) course S2 ok --taille-max-pieces 650000 ;;     # relance dans la même SORTIE
  S3) course S3 ok --taille-max-pieces 900000 ;;        # au-dessus du plafond dur
  S4) $PY -B $R/outils-cl5/attester.py $S/S1 $V $S/S1-att.json && bras S1 controle-ko-cout S1-bras-1.jsonl ;;
  S4bis) bras S1 ok S1-bras-2.jsonl ;;
  S5) course S5 grosse-consigne-casse --taille-max-pieces 650000 ;;
  S6) course S6 ok --taille-max-pieces 650000 --budget-externe-usd nan ;;
esac
