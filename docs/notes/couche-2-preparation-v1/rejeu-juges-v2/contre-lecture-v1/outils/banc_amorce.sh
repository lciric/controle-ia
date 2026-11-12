#!/usr/bin/env bash
# Banc de la chaîne v2 en jouet : lance l'amorce v2 du commit du banc contre le dépôt nu local.
# Usage : banc_amorce.sh CAS PLAFOND_MIN [VAR=valeur…]
set -u
S=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-rejeu-v2
B=$S/banc; CAS=$1; PL=$2; shift 2
R=$B/racine-$CAS; rm -rf "$R"; mkdir -p "$R"
cp $B/source/scripts/amorce_rejeu_juges_v2.sh $B/amorce-$CAS.sh
env -i PATH="/home/user/controle-ia-travail/.venv/bin:/usr/local/bin:/usr/bin:/bin" HOME="$R" \
    COMMIT=$(cat $B/commit.txt) GH_TOKEN=jeton-factice HF_TOKEN=jeton-factice DEPOT_URL="file://$B/origin.git" \
    RACINE_AMORCE="$R" PLAFOND_MIN="$PL" MODE=jouet VENV_EXISTANT=/home/user/controle-ia-travail/.venv \
    PREREG_ABSENT=1 CONFIG=config-rejeu-v2-jouet.json TACHES=taches.json SAUTER_TESTS=1 "$@" \
    bash $B/amorce-$CAS.sh > $B/banc-$CAS.log 2>&1
echo "code $?"
