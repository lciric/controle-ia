#!/usr/bin/env bash
# Lance une liste de scénarios du banc, l'un après l'autre (un processus), sorties dans le bac à sable.
SB=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v5
PY=/home/user/controle-ia-travail/.venv/bin/python
mkdir -p "$SB/banc" "$SB/tmp"
SORTIE=$1; shift
while [ $# -ge 3 ]; do
    nom=$1; g=$2; n=$3; shift 3
    TMPDIR="$SB/tmp" GIT_OPTIONAL_LOCKS=0 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
        PYTHONDONTWRITEBYTECODE=1 "$PY" -B -I "$SB/scripts/banc_v5.py" "$nom" "$g" "$n" 300 "$SB/banc/$SORTIE" \
        >> "$SB/banc/journal-$nom.txt" 2>&1
    echo "$nom fini, code $?" >> "$SB/banc/journal-lot.txt"
done
