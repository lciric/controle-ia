#!/bin/bash
# Destruction des machines A et B de l'essai à blanc, v1 — session-depot, 30 octobre 2026 (R-808, R10).
# Par IDENTIFIANT seulement, jamais par motif de nom. À lancer par Lazar avec l'outil du loueur (Hetzner : `hcloud`), son
# jeton d'accès posé par lui dans HCLOUD_TOKEN (jamais en argument). Avant : rapatrier /var/log/essai de A et le journal de B.
# Usage : ID_A=<identifiant> ID_B=<identifiant> bash detruire-machines-v1.sh
set -euo pipefail
: "${ID_A:?}" "${ID_B:?}" "${HCLOUD_TOKEN:?}"
for id in "$ID_A" "$ID_B"; do
  [[ "$id" =~ ^[0-9]+$ ]] || { echo "identifiant non numérique : $id" >&2; exit 2; }
  hcloud server describe "$id" -o format='{{.ID}} {{.Name}} {{.Status}}'
  hcloud server delete "$id"
done
echo "restantes :"; hcloud server list -o noheader
echo "à consigner dans registres/arrets.md : $ID_A, $ID_B, heure UTC $(date -u +%H:%M:%S)"
