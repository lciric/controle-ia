#!/bin/bash
# Mesure unanime — la séquence de lecture réelle, telle que le préenregistrement v10 la gèle (section « Plan d'analyse »,
# commandes (1) à (4)), à lancer **après** le scellement de la v10 et le commit qui le porte.
# **Lancement (CV9-1)** : par l'outil d'exécution de l'agent **en arrière-plan** (`run_in_background: true`) avec un délai de
# **7 200 000 ms** (deux heures), **jamais** par `nohup … &` (l'environnement arrête ces processus quelques minutes après la fin de
# la réponse) et jamais au premier plan d'un appel borné à dix minutes :
#   bash commandes-lecture-reelle-v10.sh COMMIT_DU_SCELLEMENT          (journal : journal-lecture-reelle-v10.log, écrit par ce script)
# **Durée** (CV8-1) : l'étape (2) prend environ 30 minutes de processeur avec 430 sondes, plus environ 10 minutes pour la table si
# E ≠ 60. La sortie réelle est écrite dans un fichier **temporaire** (`.partiel`) renommé à la fin.
# **Interruption** (CV9-2) : toute trace `sortie-reelle-v10*` (fichier final, `.partiel`, renommée `-interrompue-N`) bloque le
# mode réel ; on ne la renomme pas pour relancer : on la consigne (note, passation) et **la relance est une version nouvelle du
# préenregistrement** (R12). Un `.partiel` ne s'ouvre jamais (il n'est pas une sortie). Si l'interruption survient après
# l'étape (2) (sortie finale présente et scellée), `bash commandes-lecture-reelle-v10.sh LECTURE_SEULE COMMIT` rejoue les
# seules étapes (3) et (4), déterministes, qui ne lisent pas les données brutes.
# Répétition générale sur un fichier synthétique au format réel, **sans toucher aux données** :
#   bash commandes-lecture-reelle-v10.sh REPETITION CHEMIN.npz EMPREINTE N_REELLES N_PLACEBO
# Tout s'exécute depuis le dossier du préenregistrement (CV5-5) ; données par chemin absolu.
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"
MODE="${1:?commit du scellement, REPETITION ou LECTURE_SEULE}"
PY=/opt/venv-essaim-sim-v1/bin/python
export PYTHONPATH=/home/claude/canal-conv-audit-n04/src
SCRIPT=analyse_fausses_alertes_v8.py
PREREG=preenregistrement-mesure-unanime-v10.md
EMP_SCRIPT=$(sha256sum "$SCRIPT" | cut -d' ' -f1)
DONNEES_REELLES=/home/claude/canal-conv-audit-n04/donnees/20261019-230011-p3-reel/scores-p3.npz
EMPREINTE_REELLE=968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf
LECTURE_SEULE=0
if [ "$MODE" = "REPETITION" ]; then
  DONNEES="${2:?chemin du fichier synthétique}"; EMPREINTE="${3:?empreinte du fichier}"; NR="${4:-3}"; NP="${5:-2}"; SUF="-repetition"; COMMIT="repetition-generale"
  case "$DONNEES" in /home/claude/canal-conv-audit-n04/donnees/*) echo "la répétition ne lit jamais les données réelles" >&2; exit 4;; esac
  rm -f sortie-reelle-v10-repetition.json* effectifs-reel-v10-repetition.json* lecture-mecanique-reelle-v10-repetition.json* note-lecture-mecanique-v10-repetition.md*
else
  if [ "$MODE" = "LECTURE_SEULE" ]; then LECTURE_SEULE=1; COMMIT="${2:?commit du scellement}"; else COMMIT="$MODE"; fi
  DONNEES="$DONNEES_REELLES"; EMPREINTE="$EMPREINTE_REELLE"; NR=30; NP=400; SUF=""
  exec > >(tee -a journal-lecture-reelle-v10.log) 2>&1
  echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) mode $MODE commit $COMMIT ==="
  # 0. le préenregistrement v10 doit être scellé, conforme et intact ; une seule exécution réelle (toute trace bloque)
  $PY -B -c "from controle_ia import prereg; print('préenregistrement v10 scellé, conforme et intact :', prereg.exiger_prereg_scelle('$PREREG'))"
  if [ "$LECTURE_SEULE" = "0" ]; then
    if ls sortie-reelle-v10* >/dev/null 2>&1; then echo "une trace d'exécution réelle existe ($(ls sortie-reelle-v10* | tr '\n' ' ')) : la relance est une version nouvelle (R12) ; ne rien renommer" >&2; exit 3; fi
  else
    [ -s sortie-reelle-v10.json ] || { echo "LECTURE_SEULE : aucune sortie réelle finale scellée" >&2; exit 6; }
    $PY -B -m controle_ia.scellement verifier sortie-reelle-v10.json
  fi
fi
# compagnons de tout ce qui sert (CV8-5)
sha256sum -c analyse_fausses_alertes_v8.py.sha256 table_m2bis_m4_v8.py.sha256 table-m2bis-m4-v8.json.sha256 lecture_mecanique_v6.py.sha256 rediger_note_lecture_v4.py.sha256 commandes-lecture-reelle-v10.sh.sha256

if [ "$LECTURE_SEULE" = "0" ]; then
  # 1. effectifs seulement (E, K par pli, L, longueurs) : aucun taux
  $PY -I -B $SCRIPT --reel "$DONNEES" --empreinte-attendue "$EMPREINTE" --effectifs-seulement > "effectifs-reel-v10$SUF.json"
  E=$($PY -I -B -c "import json; print(json.load(open('effectifs-reel-v10$SUF.json'))['effectifs']['E'])")
  echo "E = $E ($(date -u +%H:%M:%S) UTC)"
  TABLE=table-m2bis-m4-v8.json
  if [ "$E" != "60" ]; then
    TABLE="table-m2bis-m4-v8-E${E}$SUF.json"
    [ -e "$TABLE.partiel" ] && { echo "$TABLE.partiel existe : interruption précédente, version nouvelle (R12)" >&2; exit 5; }
    $PY -I -B table_m2bis_m4_v8.py --E "$E" --longueurs-json "effectifs-reel-v10$SUF.json" > "$TABLE.partiel"
    mv "$TABLE.partiel" "$TABLE"
    $PY -B -m controle_ia.scellement sceller "$TABLE"
  fi
  $PY -B -m controle_ia.scellement sceller "effectifs-reel-v10$SUF.json"
  # 2. la lecture réelle, une fois (fichier temporaire renommé à la fin, CV8-1)
  echo "étape (2) lancée à $(date -u +%H:%M:%S) UTC (≈ 30 minutes avec 430 sondes)"
  $PY -I -B $SCRIPT --reel "$DONNEES" --empreinte-attendue "$EMPREINTE" --sondes-reelles "$NR" --sondes-placebo "$NP" --commit "$COMMIT" > "sortie-reelle-v10$SUF.json.partiel"
  mv "sortie-reelle-v10$SUF.json.partiel" "sortie-reelle-v10$SUF.json"
  $PY -B -m controle_ia.scellement sceller "sortie-reelle-v10$SUF.json"
  echo "étape (2) finie à $(date -u +%H:%M:%S) UTC"
  echo "$TABLE" > "table-en-vigueur-v10$SUF.txt"
else
  TABLE=$(cat table-en-vigueur-v10.txt)
fi

# 3. lecture mécanique des seuils gelés
$PY -I -B lecture_mecanique_v6.py "sortie-reelle-v10$SUF.json" "$TABLE" --empreinte-donnees "$EMPREINTE" --empreinte-script "$EMP_SCRIPT" > "lecture-mecanique-reelle-v10$SUF.json.partiel"
mv "lecture-mecanique-reelle-v10$SUF.json.partiel" "lecture-mecanique-reelle-v10$SUF.json"
rm -f "lecture-mecanique-reelle-v10$SUF.json.sha256"; $PY -B -m controle_ia.scellement sceller "lecture-mecanique-reelle-v10$SUF.json"

# 4. rédaction mécanique de la note, scellée (l'auteur ajoute ensuite ses réserves dans `lecture-mesure-unanime-v1.md`, qui la reprend)
HEURE=$(date -u +%H:%M:%S); DATE_LETTRES="le $(date -u +%-d) $(date -u +%B 2>/dev/null | sed 's/October/octobre/;s/November/novembre/') $(date -u +%Y)"
$PY -I -B rediger_note_lecture_v4.py "lecture-mecanique-reelle-v10$SUF.json" "sortie-reelle-v10$SUF.json" --prereg "$PREREG" --commit "$COMMIT" --heure "$HEURE" --date "$DATE_LETTRES" --table "$TABLE" > "note-lecture-mecanique-v10$SUF.md.partiel"
mv "note-lecture-mecanique-v10$SUF.md.partiel" "note-lecture-mecanique-v10$SUF.md"
rm -f "note-lecture-mecanique-v10$SUF.md.sha256"; $PY -B -m controle_ia.scellement sceller "note-lecture-mecanique-v10$SUF.md"
echo "table utilisée : $TABLE ; note : note-lecture-mecanique-v10$SUF.md ; fin $(date -u +%H:%M:%S) UTC"
$PY -I -B -c "
import json; d = json.load(open('lecture-mecanique-reelle-v10$SUF.json'))
print(json.dumps(d['verdicts'], ensure_ascii=False, indent=1)); print(d['ligne_de_lecture']); print('réserves :', d.get('reserves'))"
