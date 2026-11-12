#!/usr/bin/env bash
# Fenêtre de carte de la course de T0.6 (GO-2026-11-07-02, option (b) de Lazar, R-1700) : le jour de la course, recherche d'une A100 SXM4 de 80 Go conforme toutes les 15 minutes
# pendant 3 heures (12 recherches, 0 USD : `creation auto course` ne loue rien, il choisit l'offre et imprime la commande de création que la session exécute ensuite).
#   bash scripts/fenetre_carte_t06_v1.sh LANCEUR DOSSIER DEPENSE_ANTERIEURE_USD [ECHEANCE_UTC_S]
# Variables : FENETRE_N (défaut 12), FENETRE_PAS_S (défaut 900). Le journal de la fenêtre est `DOSSIER/fenetre.txt`.
# Codes : 0 = une A100 conforme est prête (la sortie du lanceur, avec la commande de création, est imprimée) ; 10 = fenêtre épuisée sans A100 conforme (la session lance alors
# `creation auto relance` sur la H200 NVL) ; 2 = arrêt : toute autre réponse du lanceur (jeton, GO, inventaire, plafond, trois essais…) n'est PAS « pas d'offre » : on ne bascule pas, message à la mère.
set -uo pipefail
L="${1:?lanceur (scripts/lancer_t06_v10.sh)}"; D="${2:?dossier}"; ANT="${3:?dépense antérieure en USD}"; ECH="${4:-}"
N="${FENETRE_N:-12}"; PAS="${FENETRE_PAS_S:-900}"
[[ "$N" =~ ^[0-9]+$ ]] && [ "$N" -ge 1 ] && [[ "$PAS" =~ ^[0-9]+$ ]] || { echo "FENETRE_N ou FENETRE_PAS_S illisible"; exit 2; }
[ -d "$D" ] || { echo "dossier absent ($D) : lancer d abord « controles »"; exit 2; }
for i in $(seq 1 "$N"); do
    sortie=$(bash "$L" creation auto course "$ANT" "$D" ${ECH:+"$ECH"} 2>&1); code=$?
    echo "$(date -u +%FT%TZ) recherche $i/$N : code $code : $(printf '%s\n' "$sortie" | head -n 1 | cut -c1-200)" >> "$D/fenetre.txt"
    if [ "$code" = 0 ]; then
        echo "A100 CONFORME à la recherche $i/$N"; printf '%s\n' "$sortie"; exit 0
    fi
    if [ "$code" = 3 ] && printf '%s' "$sortie" | grep -q "aucune offre conforme"; then
        [ "$i" -lt "$N" ] && sleep "$PAS"
        continue
    fi
    echo "ARRÊT de la fenêtre à la recherche $i/$N (code $code) : ce n'est pas une absence d'offre : pas de bascule sur la relance, message à la mère"; printf '%s\n' "$sortie"; exit 2
done
echo "FENÊTRE ÉPUISÉE : $N recherches sans A100 conforme : lancer « creation auto relance » (H200 NVL) sur le même dossier"; exit 10
