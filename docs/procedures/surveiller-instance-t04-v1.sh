#!/usr/bin/env bash
# Surveillance d'une instance de la validation de T0.4, depuis la session de pilotage, sans jamais afficher de jeton.
# Procédure : docs/procedures/validation-T0.4-modele-reel-v2.md, section 5. Ce script n'arrête rien : l'arrêt de
# l'instance reste à la session, par son identifiant (R10).
#
#   surveiller-instance-t04-v1.sh <identifiant> <création, secondes depuis l'époque> <dossier de sortie>
#
# Interroge l'état et le journal toutes les 2 minutes. Sort (code 0) en écrivant le motif sur sa dernière ligne :
#   FIN               ligne « AMORCE … fin, code N » : l'amorce a fini (succès ou arrêt consigné) ;
#   ÉCHEC D'AMORCE    ligne « AMORCE : … » (clonage impossible, commit introuvable, dossiers d'un essai précédent) ;
#   REDÉMARRAGE       plus d'une ligne « AMORCE <date> : commit » : en mode « args », le conteneur relance l'amorce
#                     à chaque sortie (vu au premier lancement, instance 54183350) ;
#   ÉTAT TERMINAL     instance arrêtée ou hors ligne, vue deux fois de suite ;
#   PLAFOND           6 heures depuis la création.
set -uo pipefail
ID=${1:?identifiant}
CREATION=${2:?création (secondes depuis l époque)}
D=${3:?dossier de sortie}
PLAFOND=$((${CREATION%.*} + 6 * 3600))
mkdir -p "$D"
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
while true; do
    maintenant=$(date -u +%s)
    e=$(etat | masquer)
    echo "$(date -u +%FT%TZ) $e" >> "$D/etats.txt"
    vastai logs "$ID" --tail 20000 2>&1 | masquer > "$D/journal-dernier.txt"
    if grep -qE "^AMORCE .* fin, code [0-9]+" "$D/journal-dernier.txt"; then
        echo "FIN : $(grep -E '^AMORCE .* fin, code' "$D/journal-dernier.txt" | head -1)"; exit 0
    fi
    if grep -qE "^AMORCE : " "$D/journal-dernier.txt"; then
        echo "ÉCHEC D'AMORCE : $(grep -E '^AMORCE : ' "$D/journal-dernier.txt" | head -1)"; exit 0
    fi
    if [ "$(grep -cE '^AMORCE [0-9]{4}-[0-9]{2}-[0-9]{2}T[^ ]* : commit' "$D/journal-dernier.txt")" -gt 1 ]; then
        echo "REDÉMARRAGE : l'amorce a été relancée par le conteneur"; exit 0
    fi
    case "$e" in
        *"actual_status=exited"*|*"actual_status=offline"*|*"cur_state=stopped"*) terminal=$((terminal + 1)) ;;
        *) terminal=0 ;;
    esac
    if [ "$terminal" -ge 2 ]; then echo "ÉTAT TERMINAL : $e"; exit 0; fi
    if [ "$maintenant" -ge "$PLAFOND" ]; then echo "PLAFOND : 6 heures depuis la création"; exit 0; fi
    sleep 120
done
