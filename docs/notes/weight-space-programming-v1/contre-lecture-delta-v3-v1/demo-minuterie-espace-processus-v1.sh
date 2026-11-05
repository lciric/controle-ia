#!/bin/bash
# Démonstrations du contre-lecteur (aucun réseau : curl simulé ; aucun dépôt cloné)
D="$1"; cd "$D"
run() { # run NOM SCRIPT PATHBIN ECH LIMITE [unshare]
  local n=$1 s=$2 b=$3 e=$4 l=$5 u=${6:-}; rm -rf "$D/r-$n"; mkdir -p "$D/r-$n"; : > "$D/faux.log"
  local t0=$(date +%s)
  env -i PATH="$b:/usr/bin:/bin" HOME="$D" RACINE_AMORCE="$D/r-$n" CONTAINER_ID=123456 CONTAINER_API_KEY=factice \
     COMMIT=$(printf 'a%.0s' {1..40}) COMMIT_CODE=$(printf 'a%.0s' {1..40}) PRIX_HEURE_USD=0.8 PRIX_STOCKAGE_HEURE_USD=0.05 \
     ECHEANCE_UTC_S="$e" DEPOT_URL=file:///nulle-part MINUTERIE_PAS_S=1 MINUTERIE_REESSAI_S=1 MINUTERIE_MARGE_S=4 \
     timeout "$l" $u bash "$s" > "$D/r-$n/sortie.txt" 2>&1
  local c=$?; sleep 3
  echo "== $n : code $c en $(( $(date +%s) - t0 )) s ; DELETE au journal de la minuterie : $(grep -c DELETE "$D/r-$n/sparks-v3-minuterie.log" 2>/dev/null || echo 0)"
  sed 's/^/   /' "$D/r-$n/sortie.txt" | head -6
}
NOW=$(date +%s)
run apres-echeance-pidns "$D/amorce.sh" "$D/bin" $((NOW - 5)) 60 "unshare -pf --mount-proc"
run apres-echeance-pidns-sans-attente "$D/amorce-sans-attente.sh" "$D/bin" $((NOW - 5)) 60 "unshare -pf --mount-proc"
run git-bloque-creation "$D/amorce.sh" "$D/bin-git-bloque" $((NOW + 3600)) 20 "unshare -pf --mount-proc"
