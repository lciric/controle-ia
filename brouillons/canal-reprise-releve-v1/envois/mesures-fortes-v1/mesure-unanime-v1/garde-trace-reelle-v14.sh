#!/bin/bash
# Garde « une seule exécution réelle » (CV10-1, CV13-1), isolée pour être **testable** (R5) : exit 3 si une trace d'exécution
# réelle existe dans le dossier courant, 0 sinon. Les noms des traces sont passés en **arguments** (la garde est indépendante de
# la version ; CV13-1). Ne regarde **que** les noms passés, jamais un préfixe que la répétition partage. Appelée par
# `commandes-lecture-reelle-v14.sh` en mode réel, et exercée par `test-garde-trace-v14.sh` sur des états plantés.
#
# Usage : bash garde-trace-reelle-v14.sh TEMOIN SORTIE SORTIE_PARTIEL
set -euo pipefail
[ $# -ge 1 ] || { echo "usage : garde-trace-reelle-v14.sh TEMOIN [SORTIE [PARTIEL]]" >&2; exit 2; }
for f in "$@"; do
  [ -e "$f" ] && { echo "trace d'exécution réelle : $f (la relance est une version nouvelle, R12 ; ne rien renommer ni effacer)" >&2; exit 3; }
done
exit 0
