#!/usr/bin/env bash
# Surveillance de l'instance du premier test boîte blanche sur l'organisme (i-a) (P3, R-192, R-202), v1, brouillon 2,
# depuis la session de pilotage, sans jamais afficher de jeton. Déclinée de
# docs/procedures/notations-T0.5-v2/surveiller_notations_v1.sh sous un nom nouveau (R12) ; seuls changent ce commentaire,
# le plafond, l'exigence des jetons et le message d'usage :
#   - plafond écrit ici, en clair : la création plus 22 200 s (préenregistrement de P3, brouillon 4, Plan d'analyse,
#     point 4 ; marge avant le KILL de l'amorce, 360 + 5 minutes : 5 minutes moins le démarrage du conteneur, CH-21) ;
#   - les deux jetons passés à l'instance (HF_TOKEN et CONTROLE_IA_GITHUB_TOKEN, 8 caractères au moins) sont exigés au
#     départ : sans eux, le masquage serait un repli silencieux (R5 ; contre-lecture de la chaîne, CH-16) ;
#   - le journal de l'instance n'est gardé comme dernier relevé que si l'appel a réussi ; chaque ligne nouvelle
#     « AMORCE … » ou « PROGRES … » s'ajoute à un relevé cumulatif, jamais tronqué (progres.txt) : la ligne
#     « PROGRES … etape=sondes-figees empreinte=… » reste établie même si l'instance devient ensuite injoignable ;
#   - l'outil de location doit être trouvé sur le PATH, sinon arrêt immédiat (une surveillance aveugle ne sortirait
#     qu'au plafond).
# Ce script n'arrête rien : l'arrêt de l'instance reste à la session, par son identifiant (R10).
#
#   surveiller_p3_v1.sh <identifiant> <création, secondes depuis l'époque> <dossier de sortie>
#
# Interroge l'état et le journal toutes les INTERVALLE secondes (120 par défaut). Sort (code 0) en écrivant le motif
# sur sa dernière ligne, et chaque motif appelle l'arrêt immédiat de l'instance par son identifiant :
#   FIN               ligne « AMORCE … fin, code N » ;
#   ÉCHEC D'AMORCE    ligne « AMORCE : … » (clonage impossible, commit introuvable, dossiers d'un essai précédent) ;
#   REDÉMARRAGE       plus d'une ligne « AMORCE <date> : commit » (le conteneur relance l'amorce à chaque sortie) ;
#   ÉTAT TERMINAL     instance arrêtée ou hors ligne, vue deux fois de suite ;
#   PLAFOND           création plus 22 200 s atteinte.
# Code 2 : usage, jetons absents, dossier de sortie existant (R12) ou outil de location introuvable.
set -uo pipefail
PLAFOND_S=22200                                  # création + 22 200 s (préenregistrement de P3)
ID=${1:-}; CREATION=${2:-}; D=${3:-}
INTERVALLE=${INTERVALLE:-120}
[[ "$ID" =~ ^[0-9]+$ && "$CREATION" =~ ^[0-9]+$ && -n "$D" ]] || { echo "usage : surveiller_p3_v1.sh <identifiant> <création> <dossier neuf>"; exit 2; }
J_HF=${HF_TOKEN:-}; J_GH=${CONTROLE_IA_GITHUB_TOKEN:-}
[ "${#J_HF}" -ge 8 ] && [ "${#J_GH}" -ge 8 ] \
    || { echo "jetons HF_TOKEN et CONTROLE_IA_GITHUB_TOKEN absents ou trop courts : masquage impossible, surveillance refusée"; exit 2; }
unset J_HF J_GH
[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
command -v vastai > /dev/null || { echo "outil de location introuvable sur le PATH : surveillance aveugle, arrêt"; exit 2; }
PLAFOND=$((CREATION + PLAFOND_S))
mkdir -p "$D" && : > "$D/progres.txt" || exit 2
masquer() {
    python3 -c '
import os, sys
t = sys.stdin.read()
for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(k)
    if v and len(v) > 6:
        t = t.replace(v, "***")
sys.stdout.write(t)'
}
etat() {
    vastai show instance "$ID" --raw 2>&1 | python3 -c '
import json, sys
t = sys.stdin.read()
try:
    d = json.loads(t)
except Exception:
    print("illisible:", t[:120].replace("\n", " ")); raise SystemExit
print(" ".join(f"{k}={d.get(k)}" for k in ("actual_status", "cur_state", "intended_status", "status_msg")))'
}
terminal=0
echo "surveillance de $ID : création $CREATION, plafond $PLAFOND (création + $PLAFOND_S s), intervalle $INTERVALLE s" > "$D/surveillance.txt"
while true; do
    maintenant=$(date -u +%s)
    e=$(etat | masquer)
    echo "$(date -u +%FT%TZ) $e" >> "$D/etats.txt"
    if vastai logs "$ID" --tail 20000 > "$D/journal-tour.txt" 2>&1; then
        masquer < "$D/journal-tour.txt" > "$D/journal-dernier.txt"
        # relevé cumulatif : chaque ligne AMORCE ou PROGRES nouvelle, dans l'ordre d'apparition, jamais retirée
        grep -E '^(AMORCE|PROGRES) ' "$D/journal-dernier.txt" | while IFS= read -r ligne; do
            grep -qxF -- "$ligne" "$D/progres.txt" || printf '%s\n' "$ligne" >> "$D/progres.txt"
        done
    else
        echo "$(date -u +%FT%TZ) journal illisible (appel en échec) : dernier relevé gardé" >> "$D/etats.txt"
    fi
    rm -f "$D/journal-tour.txt"
    if grep -qE "^AMORCE .* fin, code [0-9]+" "$D/journal-dernier.txt" 2>/dev/null; then
        echo "FIN : $(grep -E '^AMORCE .* fin, code' "$D/journal-dernier.txt" | head -1)"; exit 0
    fi
    if grep -qE "^AMORCE : " "$D/journal-dernier.txt" 2>/dev/null; then
        echo "ÉCHEC D'AMORCE : $(grep -E '^AMORCE : ' "$D/journal-dernier.txt" | head -1)"; exit 0
    fi
    if [ "$(grep -cE '^AMORCE [0-9]{4}-[0-9]{2}-[0-9]{2}T[^ ]* : commit' "$D/progres.txt")" -gt 1 ]; then
        echo "REDÉMARRAGE : l'amorce a été relancée par le conteneur"; exit 0
    fi
    case "$e" in
        *"actual_status=exited"*|*"actual_status=offline"*|*"cur_state=stopped"*) terminal=$((terminal + 1)) ;;
        *) terminal=0 ;;
    esac
    if [ "$terminal" -ge 2 ]; then echo "ÉTAT TERMINAL : $e"; exit 0; fi
    if [ "$maintenant" -ge "$PLAFOND" ]; then echo "PLAFOND : création + $PLAFOND_S s"; exit 0; fi
    sleep "$INTERVALLE"
done
