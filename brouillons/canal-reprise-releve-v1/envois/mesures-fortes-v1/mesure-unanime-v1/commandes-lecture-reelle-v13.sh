#!/bin/bash
# Mesure unanime — la séquence de lecture réelle, telle que le préenregistrement v13 la gèle (commandes (1) à (4)), à lancer
# **après** le scellement de la v13 et le commit qui le porte.
# **Lancement (CV9-1)** : par l'outil d'exécution de l'agent **en arrière-plan** (`run_in_background: true`) avec un délai de
# **7 200 000 ms** (deux heures), **jamais** par `nohup … &` (l'environnement arrête ces processus peu après la fin de la
# réponse) et jamais au premier plan d'un appel borné à dix minutes :
#   bash commandes-lecture-reelle-v13.sh COMMIT_DU_SCELLEMENT
# **Durée** (CV8-1) : l'étape (2) prend environ 40 minutes de processeur avec 430 sondes, plus environ 10 minutes pour la table
# si E ≠ 60.
# **Une seule exécution réelle (R1, CV10-1)** : l'étape 0 pose un **témoin** `execution-reelle-v13.commencee` avec `noclobber`
# (sa présence = une exécution réelle a déjà commencé) et refuse toute sortie réelle explicitement nommée (jamais un préfixe
# que la répétition partage). La répétition écrit dans le **sous-dossier** `repetition-v13/`, hors de portée de la garde, mais
# **passe par la même étape 0** (fonction `etape_0`), pour que les gardes soient exercées (R5). Le témoin n'est jamais effacé :
# une relance après interruption est une **version nouvelle du préenregistrement** (R12), sauf reprise `LECTURE_SEULE` ci-dessous.
# **Interruption** (CV9-2, CV10-2) : si l'étape (2) est coupée (sortie finale scellée absente), la relance est une version
# nouvelle. Si elle est coupée **après** l'étape (2) (sortie finale présente et scellée), `bash commandes-lecture-reelle-v13.sh
# LECTURE_SEULE COMMIT` rejoue les seules étapes (3) et (4), déterministes, sans lire les données ; la garde isolée
# `garde-lecture-seule-v12.sh` **refuse** (sortie 7) si la note est déjà scellée, **sans jamais s'éteindre en silence** quand la
# note est absente (défaut CV11-1 de la v11 : `[ -e X ] && { … }` sous `set -e`) ; on ne réécrit jamais un fichier scellé.
# **Répétition** sur un fichier synthétique au format réel, sans toucher aux données :
#   bash commandes-lecture-reelle-v13.sh REPETITION CHEMIN.npz EMPREINTE N_REELLES N_PLACEBO
# **Instance** (CV10-3) : la variable d'environnement MESURE_INSTANCE est obligatoire en mode réel (qui écrit la note) ; on la
# met à la lignée et au modèle qui lancent. Tout depuis le dossier du préenregistrement (CV5-5) ; données par chemin absolu.
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"
MODE="${1:?commit du scellement, REPETITION ou LECTURE_SEULE}"
PY=/opt/venv-essaim-sim-v1/bin/python
export PYTHONPATH=/home/claude/canal-conv-audit-n04/src
SCRIPT=analyse_fausses_alertes_v8.py
PREREG=preenregistrement-mesure-unanime-v13.md
EMP_SCRIPT=$(sha256sum "$SCRIPT" | cut -d' ' -f1)
DONNEES_REELLES=/home/claude/canal-conv-audit-n04/donnees/20261019-230011-p3-reel/scores-p3.npz
EMPREINTE_REELLE=968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf
TEMOIN=execution-reelle-v13.commencee

# CV11-3(c) : plus de `rm` d'un fichier sans objet ; sceller refuse de réécrire un fichier déjà scellé (R12).
sceller() { [ -e "$1.sha256" ] && { echo "déjà scellé, non réécrit (R12) : $1" >&2; return 0; }; $PY -B -m controle_ia.scellement sceller "$1"; }
compagnons() { sha256sum -c analyse_fausses_alertes_v8.py.sha256 table_m2bis_m4_v8.py.sha256 table-m2bis-m4-v8.json.sha256 lecture_mecanique_v8.py.sha256 rediger_note_lecture_v7.py.sha256 commandes-lecture-reelle-v13.sh.sha256 garde-trace-reelle-v12.sh.sha256 test-garde-trace-v12.sh.sha256 garde-lecture-seule-v12.sh.sha256 test-lecture-seule-v13.sh.sha256; }

# étape 0 : gardes d'arrêt isolées (chacune testée sain + artefact par son test déposé, R5) + scellement du préenregistrement
# (modes qui lisent les données, pas la répétition qui se fait avant scellement sur le texte final).
etape_0() {  # $1 = REEL|REPETITION|LECTURE_SEULE
  if [ "$1" = "REEL" ]; then
    bash garde-trace-reelle-v12.sh  # exit 3 si une trace d'exécution réelle existe
    $PY -B -c "from controle_ia import prereg; print('préenregistrement v13 scellé, conforme et intact :', prereg.exiger_prereg_scelle('$PREREG'))"
    ( set -o noclobber; : > "$TEMOIN" ) 2>/dev/null || { echo "témoin déjà posé : exécution réelle déjà commencée (R12)" >&2; exit 3; }
    printf '%s UTC — exécution réelle commencée, commit %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$COMMIT" >> "$TEMOIN"
  elif [ "$1" = "LECTURE_SEULE" ]; then
    $PY -B -c "from controle_ia import prereg; print('préenregistrement v13 scellé, conforme et intact :', prereg.exiger_prereg_scelle('$PREREG'))"
    [ -s sortie-reelle-v13.json ] && [ -e sortie-reelle-v13.json.sha256 ] || { echo "LECTURE_SEULE : aucune sortie réelle finale scellée" >&2; exit 6; }
    $PY -B -m controle_ia.scellement verifier sortie-reelle-v13.json
    bash garde-lecture-seule-v12.sh note-lecture-mecanique-v13.md  # exit 7 si la note est déjà scellée ; jamais de mort silencieuse (CV11-1, R5)
  else  # REPETITION : la répétition se fait avant le scellement, sur le texte final ; elle exerce les deux gardes par leurs tests déposés
    bash test-garde-trace-v12.sh
    bash test-lecture-seule-v13.sh
  fi
}

if [ "$MODE" = "REPETITION" ]; then
  DONNEES="${2:?chemin}"; EMPREINTE="${3:?empreinte}"; NR="${4:-3}"; NP="${5:-2}"; COMMIT="repetition-generale"
  case "$DONNEES" in /home/claude/canal-conv-audit-n04/donnees/*) echo "la répétition ne lit jamais les données réelles" >&2; exit 4;; esac
  D=repetition-v13; rm -rf "$D"; mkdir "$D"; PREF="$D/"; LECTURE_SEULE=0
  MESURE_INSTANCE="répétition générale (aucune instance réelle)"  # CV11-3(d) : forcé, jamais hérité d'un réglage réel
  compagnons; etape_0 REPETITION
elif [ "$MODE" = "LECTURE_SEULE" ]; then
  LECTURE_SEULE=1; COMMIT="${2:?commit}"; DONNEES="$DONNEES_REELLES"; EMPREINTE="$EMPREINTE_REELLE"; NR=30; NP=400; PREF=""
  : "${MESURE_INSTANCE:?MESURE_INSTANCE obligatoire (qui lance : lignée et modèle)}"
  exec > >(tee -a journal-lecture-reelle-v13.log) 2>&1; echo "=== $(date -u +%FT%TZ) LECTURE_SEULE commit $COMMIT ==="
  compagnons; etape_0 LECTURE_SEULE
  TABLE=$(cat table-en-vigueur-v13.txt); sha256sum -c "$TABLE.sha256" table-en-vigueur-v13.txt.sha256
  [ "$($PY -I -B -c "import json;print(json.load(open('sortie-reelle-v13.json'))['manifeste']['commit'])")" = "$COMMIT" ] || { echo "commit ≠ manifeste de la sortie" >&2; exit 8; }
else
  COMMIT="$MODE"; DONNEES="$DONNEES_REELLES"; EMPREINTE="$EMPREINTE_REELLE"; NR=30; NP=400; PREF=""; LECTURE_SEULE=0
  : "${MESURE_INSTANCE:?MESURE_INSTANCE obligatoire (qui lance : lignée et modèle)}"
  exec > >(tee -a journal-lecture-reelle-v13.log) 2>&1; echo "=== $(date -u +%FT%TZ) RÉEL commit $COMMIT ==="
  compagnons; etape_0 REEL
fi

if [ "$LECTURE_SEULE" = "0" ]; then
  # 1. effectifs seulement (E, K par pli, L, longueurs) : aucun taux
  $PY -I -B $SCRIPT --reel "$DONNEES" --empreinte-attendue "$EMPREINTE" --effectifs-seulement > "${PREF}effectifs-reel-v13.json"
  E=$($PY -I -B -c "import json; print(json.load(open('${PREF}effectifs-reel-v13.json'))['effectifs']['E'])")
  echo "E = $E ($(date -u +%T) UTC)"
  TABLE=table-m2bis-m4-v8.json
  if [ "$E" != "60" ]; then
    TABLE="${PREF}table-m2bis-m4-v8-E${E}.json"
    [ -e "$TABLE.partiel" ] && { echo "$TABLE.partiel : interruption précédente, version nouvelle (R12)" >&2; exit 5; }
    $PY -I -B table_m2bis_m4_v8.py --E "$E" --longueurs-json "${PREF}effectifs-reel-v13.json" > "$TABLE.partiel"; mv "$TABLE.partiel" "$TABLE"; sceller "$TABLE"
  fi
  sceller "${PREF}effectifs-reel-v13.json"
  echo "$TABLE" > "${PREF}table-en-vigueur-v13.txt"; sceller "${PREF}table-en-vigueur-v13.txt"  # CV11-3(e) : table gelée AVANT la lecture
  # 2. la lecture réelle, une fois (fichier temporaire renommé à la fin, CV8-1)
  echo "étape (2) lancée à $(date -u +%T) UTC (≈ 40 minutes avec 430 sondes)"
  $PY -I -B $SCRIPT --reel "$DONNEES" --empreinte-attendue "$EMPREINTE" --sondes-reelles "$NR" --sondes-placebo "$NP" --commit "$COMMIT" > "${PREF}sortie-reelle-v13.json.partiel"
  mv "${PREF}sortie-reelle-v13.json.partiel" "${PREF}sortie-reelle-v13.json"; sceller "${PREF}sortie-reelle-v13.json"
  echo "étape (2) finie à $(date -u +%T) UTC"
fi

# 3. lecture mécanique des seuils gelés (si déjà scellée — reprise LECTURE_SEULE —, vérifiée, jamais refaite ; CV10-2/CV11-1)
if [ -e "${PREF}lecture-mecanique-reelle-v13.json.sha256" ]; then
  $PY -B -m controle_ia.scellement verifier "${PREF}lecture-mecanique-reelle-v13.json"
else
  $PY -I -B lecture_mecanique_v8.py "${PREF}sortie-reelle-v13.json" "$TABLE" --empreinte-donnees "$EMPREINTE" --empreinte-script "$EMP_SCRIPT" > "${PREF}lecture-mecanique-reelle-v13.json.partiel"
  mv "${PREF}lecture-mecanique-reelle-v13.json.partiel" "${PREF}lecture-mecanique-reelle-v13.json"; sceller "${PREF}lecture-mecanique-reelle-v13.json"
fi
# 4. rédaction mécanique de la note, scellée
if [ ! -e "${PREF}note-lecture-mecanique-v13.md.sha256" ]; then
  HEURE=$(date -u +%T); DATE_LETTRES=$($PY -I -B -c "import datetime;M='janvier février mars avril mai juin juillet août septembre octobre novembre décembre'.split();d=datetime.datetime.now(datetime.timezone.utc);print(f'le {d.day} {M[d.month-1]} {d.year}')")
  $PY -I -B rediger_note_lecture_v7.py "${PREF}lecture-mecanique-reelle-v13.json" "${PREF}sortie-reelle-v13.json" --prereg "$PREREG" --commit "$COMMIT" --heure "$HEURE" --date "$DATE_LETTRES" --instance "$MESURE_INSTANCE" --table "$TABLE" > "${PREF}note-lecture-mecanique-v13.md.partiel"
  mv "${PREF}note-lecture-mecanique-v13.md.partiel" "${PREF}note-lecture-mecanique-v13.md"; sceller "${PREF}note-lecture-mecanique-v13.md"
fi
echo "table : $TABLE ; note : ${PREF}note-lecture-mecanique-v13.md ; fin $(date -u +%T) UTC"
$PY -I -B -c "
import json; d = json.load(open('${PREF}lecture-mecanique-reelle-v13.json'))
print(json.dumps(d['verdicts'], ensure_ascii=False, indent=1)); print(d['ligne_de_lecture']); print('réserves :', d.get('reserves'))"
