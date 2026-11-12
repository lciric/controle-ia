#!/usr/bin/env bash
# Répétition jouet de l'amorce et du script d'instance de T0.5 (ETUDE=revalidation, MODE=jouet), au commit cité, sur un
# dépôt jetable du bloc-notes (préalable 8 de la procédure du pilote ; Y-1, Z-5). Trois passages :
#   1. cas sain (branche par défaut calcul/t05-revalidation-jouet-v1) ; temps de la ligne « AMORCE » à la fin des tests ;
#   2. relancement sous BRANCHE=calcul/t05-revalidation-jouet-v2 (cas sain du relancement) ;
#   3. artefact : relancement sans branche nouvelle → arrêt avant l'installation (code 2), consigné au journal.
# Jetons factices : aucun jeton réel n'entre dans la répétition.
# Usage : repetition_jouet.sh DEPOT COMMIT_CODE RACINE TESTS_ATTENDUS
set -uo pipefail
DEPOT=$1; CODE=$2; R=$3; ATTENDUS=$4
S=$(cd "$(dirname "$0")" && pwd)
PY=${VENV_REPETITION:?VENV_REPETITION}/bin/python
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R"
git clone -q --no-local "$DEPOT" "$R/source" && git -C "$R/source" checkout -q -B main "$CODE" || exit 2
cd "$R/source"
git config user.email essai@invalid; git config user.name essai
"$PY" -I "$S/remplir_revalidation_v2.py" . "$CODE" "$ATTENDUS" 20261010 jouet "2026-10-10 (répétition jouet)" "(répétition)" \
    prereg/T0.5-revalidation-equivalence-pilote-v1.md prereg/T0.5-revalidation-config-v1.json > "$R/remplissage.json" || exit 2
PYTHONPATH=src "$PY" -m controle_ia.scellement sceller prereg/T0.5-revalidation-config-v1.json > /dev/null || exit 2
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import sceller_prereg; sceller_prereg('prereg/T0.5-revalidation-equivalence-pilote-v1.md')" || exit 2
git add prereg/T0.5-revalidation-equivalence-pilote-v1.md prereg/T0.5-revalidation-equivalence-pilote-v1.md.sha256 \
    prereg/T0.5-revalidation-config-v1.json prereg/T0.5-revalidation-config-v1.json.sha256
git commit -qm "essai : préenregistrement jouet de la revalidation" || exit 2
ESSAI=$(git rev-parse HEAD); echo "$ESSAI" > "$R/commit-essai.txt"
git clone -q --bare "$R/source" "$R/distant.git" || exit 2
cd "$R"
passage() {   # $1 nom, $2 BRANCHE (vide : défaut)
    local n=$1 b=$2 debut fin
    mkdir -p "$R/racine-$n"
    debut=$(date +%s)
    env -i PATH="$PATH" LANG=C.UTF-8 HOME="$R/racine-$n" COMMIT="$ESSAI" GH_TOKEN=factice HF_TOKEN=factice \
        ETUDE=revalidation MODE=jouet DEPOT_URL="$R/distant.git" RACINE_AMORCE="$R/racine-$n" \
        VENV_EXISTANT="$VENV_REPETITION" ${b:+BRANCHE=$b} \
        bash "$R/source/scripts/amorce_instance_t05.sh" > "$R/amorce-$n.log" 2>&1
    local code=$?
    fin=$(date +%s)
    echo "passage $n : code $code ; durée totale $((fin-debut)) s"
}
passage 1-sain ""
passage 2-relancement-v2 calcul/t05-revalidation-jouet-v2
passage 3-artefact-branche-presente ""
git -C "$R/distant.git" branch -a | sed 's/^/branche distante : /'
echo "FIN DE LA RÉPÉTITION"
