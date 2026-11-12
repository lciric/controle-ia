#!/usr/bin/env bash
# Amorce de l'hôte durable de la troisième course d'A1-v3 (GO-2026-11-04-06), v1. Lancée par le script de démarrage de la
# machine louée sans carte (`onstart` écrit par `src/controle_ia/hote_durable_a1_v3.py louer`), qui a cloné le dépôt privé
# au commit COMMIT_PRIVE dans /root/amorce-depot. Elle installe le strict nécessaire (git, numpy au numéro exact), fait
# exister /usr/bin/python3 (chemin écrit dans la configuration gelée), puis remplace son processus par la partie « hote » du
# module (exec : aucune ligne de ce fichier n'est relue après le départ). Toute la suite (GO, pièces, relais, course, garde,
# scellement, versement, destruction par identifiant) est dans le module ; une reprise du conteneur ne relance jamais rien.
# Variables (corps de création, jamais affichées) : COMMIT_PRIVE COMMIT_PUBLIC SHA_TEXTE COMMIT_REGISTRE GO_ID PRIX_H_USD
# DEPOT_URL CLE_ARGON GH_TOKEN ; posées par Vast : CONTAINER_ID CONTAINER_API_KEY.
# Essai local : RACINE_AMORCE (défaut /root) et SAUTER_INSTALLATION=1 (aucune installation, aucun réseau).
set -uo pipefail
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
echo "AMORCE $(date -u +%FT%TZ) : hôte durable A1-v3 v1 ; machine ${CONTAINER_ID:-?} ; GO ${GO_ID:-?}"
for v in COMMIT_PRIVE COMMIT_PUBLIC SHA_TEXTE COMMIT_REGISTRE GO_ID PRIX_H_USD CLE_ARGON GH_TOKEN; do
    [ -n "${!v:-}" ] || { echo "AMORCE : variable $v absente : rien ne part"; exit 2; }
done
[ "$GO_ID" = "GO-2026-11-04-06" ] || { echo "AMORCE : GO $GO_ID au lieu de GO-2026-11-04-06"; exit 2; }
M="$RACINE_AMORCE/amorce-depot/src/controle_ia/hote_durable_a1_v3.py"
[ -f "$M" ] || { echo "AMORCE : module absent du commit $COMMIT_PRIVE"; exit 2; }
if [ "${SAUTER_INSTALLATION:-0}" != "1" ] && [ ! -e "$RACINE_AMORCE/a1-v3-troisieme-v1/ETAT" ]; then
    export DEBIAN_FRONTEND=noninteractive
    command -v git >/dev/null || { apt-get update -qq && apt-get install -y -qq git ca-certificates >/dev/null; } \
        || { echo "AMORCE : installation de git impossible"; exit 2; }
    python3 -c 'import numpy' 2>/dev/null || python3 -m pip install -q --no-cache-dir "numpy==2.5.3" \
        || { echo "AMORCE : installation de numpy impossible"; exit 2; }
    [ -x /usr/bin/python3 ] || ln -s "$(command -v python3)" /usr/bin/python3
    echo "AMORCE $(date -u +%FT%TZ) : $(python3 --version 2>&1), numpy $(python3 -c 'import numpy; print(numpy.__version__)')"
fi
exec python3 -I -B "$M" hote
