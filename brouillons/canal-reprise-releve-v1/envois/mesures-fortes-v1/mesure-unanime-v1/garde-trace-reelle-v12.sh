#!/bin/bash
# Garde « une seule exécution réelle » (CV10-1), isolée pour être **testable** (R5) : exit 3 si une trace d'exécution réelle
# existe dans le dossier courant (témoin, sortie finale, ou `.partiel`), 0 sinon. Ne regarde **que** des noms explicites, jamais
# un préfixe que la répétition (sous-dossier `repetition-v12/`) partage. Appelée par `commandes-lecture-reelle-v12.sh` en mode
# réel, et exercée par `test-garde-trace-v12.sh` sur des états plantés.
set -euo pipefail
for f in execution-reelle-v12.commencee sortie-reelle-v12.json sortie-reelle-v12.json.partiel; do
  [ -e "$f" ] && { echo "trace d'exécution réelle : $f (la relance est une version nouvelle, R12 ; ne rien renommer ni effacer)" >&2; exit 3; }
done
exit 0
