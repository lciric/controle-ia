#!/usr/bin/env bash
# Banc du lanceur v2 devant le faux vastai. Usage : banc_lanceur.sh CAS COMMIT [VAR=valeur…]
S=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-rejeu-v2
B=$S/banc; CAS=$1; C=$2; shift 2
T=$B/lanceur/traces-$CAS; rm -rf "$T"
env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=$B/lanceur VASTAI=$S/outils/faux_vastai DEPOT=$B/source \
    FAUX_OFFRES=$B/lanceur/offres.json FAUX_JOURNAL=$B/lanceur/vastai-$CAS.log HF_TOKEN=hf-factice-123456 \
    CONTROLE_IA_GITHUB_TOKEN=gh-factice-123456 "$@" \
    bash $B/source/docs/procedures/rejeu-juges-v2/lancer_rejeu_juges_v2.sh "$C" "$T" > $B/lanceur/lanceur-$CAS.log 2>&1
echo "$CAS : code $?"
