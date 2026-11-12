#!/usr/bin/env bash
# Essai de CLC-P3-05 (R-2311), v1 : la ligne de l'étape 13 du script v4, prise telle quelle dans le fichier, la commande du module
# remplacée par un lecteur de l'environnement du processus fils et de ses arguments ; jouée sous `set -u` pour trois états de
# ENV_CPU : vide (branche EPYC), deux valeurs (hors EPYC), non défini (état que prend un tableau vide dans un bash antérieur à
# 4.4, où `"${t[@]}"` vide échoue sous `set -u`). La forme du v3 est jouée aussi, pour comparaison.
#   bash essai_env_cpu_v4.sh SCRIPT_V4 SCRIPT_V3
set -uo pipefail
V4="$1"; V3="$2"
lire='python3 -c "import os, sys; print(\"argv\", len(sys.argv), \"CUBLAS\", os.environ.get(\"CUBLAS_WORKSPACE_CONFIG\"), \"ATEN\", os.environ.get(\"ATEN_CPU_CAPABILITY\"), \"MKL\", os.environ.get(\"MKL_CBWR\"))"'
for v in "$V4" "$V3"; do
    ligne=$(grep -m 1 '^env CUBLAS_WORKSPACE_CONFIG' "$v")
    corps="${ligne%% PYTHONPATH=src*}"                       # « env CUBLAS_WORKSPACE_CONFIG=:4096:8 <développement d'ENV_CPU> »
    echo "== $(basename "$v") : ${corps}"
    for etat in vide deux non_defini; do
        case "$etat" in
            vide) prelude='ENV_CPU=()';;
            deux) prelude='ENV_CPU=(ATEN_CPU_CAPABILITY=avx2 MKL_CBWR=AVX2)';;
            non_defini) prelude='unset ENV_CPU';;
        esac
        sortie=$(bash -c "set -u; $prelude; $corps $lire" 2>&1); c=$?
        echo "   $etat : code $c ; $sortie"
    done
done
echo "bash : $BASH_VERSION"
