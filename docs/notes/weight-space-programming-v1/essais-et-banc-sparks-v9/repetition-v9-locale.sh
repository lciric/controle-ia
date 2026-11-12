#!/usr/bin/env bash
# Répétition jouet v9, locale : dépôt nu local (objets empruntés au dépôt de travail), aucun réseau, aucune poussée distante.
set -uo pipefail
CODE=${1:?commit du code}
DEPOT=/home/user/controle-ia-travail
V=$DEPOT/.venv/bin/python
OUT=$DEPOT/docs/notes/weight-space-programming-v1/repetition-jouet-v9-locale-${2:-v1}; mkdir -p "$OUT"
J=$(mktemp -d /tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/rep9-XXXX); mkdir -p "$J/faux-bin" "$J/racine" "$J/home"
T() { timeout -k 10 "$@"; }
B="$J/depot.git"; git init -q --bare "$B"; echo "$DEPOT/.git/objects" > "$B/objects/info/alternates"; cp "$DEPOT/.git/shallow" "$B/shallow"
git -C "$B" config uploadpack.allowFilter true; git -C "$B" config uploadpack.allowAnySHA1InWant true
# commit lancé : le code + l'addendum factice marqué (écrit par addendum_factice.py, tiré du commit du code)
git -C "$DEPOT" show "$CODE:src/controle_ia/sparks_exp7_nul_v8/addendum_factice.py" > "$J/addendum_factice.py"
python3 -I -B "$J/addendum_factice.py" "$J/SPARKS-EXP7-NUL-addendum-1.md" "$CODE" > /dev/null || { echo "addendum factice non écrit"; exit 2; }
export GIT_DIR="$B" GIT_INDEX_FILE="$J/index"
git read-tree "$CODE"
HA=$(git hash-object -w "$J/SPARKS-EXP7-NUL-addendum-1.md"); HS=$(git hash-object -w "$J/SPARKS-EXP7-NUL-addendum-1.md.sha256"); HG=$(git hash-object -w "$DEPOT/registres/go.md")   # registre des GO de main, comme la répétition officielle
git update-index --add --cacheinfo 100644 "$HA" prereg/SPARKS-EXP7-NUL-addendum-1.md --cacheinfo 100644 "$HS" prereg/SPARKS-EXP7-NUL-addendum-1.md.sha256 --cacheinfo 100644 "$HG" registres/go.md
ARBRE=$(git write-tree); LANCE=$(git -c user.name=essai -c user.email=essai@invalid commit-tree "$ARBRE" -p "$CODE" -m "essai : répétition v9 locale (addendum factice)")
git update-ref refs/heads/essai/sparks-v9-repetition "$LANCE"; unset GIT_DIR GIT_INDEX_FILE
COURT=${LANCE:0:12}; echo "commit lancé $LANCE" | tee "$OUT/00-commit.txt"
printf '#!/bin/bash\necho "curl $*" >> "%s/faux.log"\nprintf 200\n' "$J" > "$J/faux-bin/curl"; chmod +x "$J/faux-bin/curl"
ENV=(env -i PATH="$J/faux-bin:/usr/sbin:/usr/bin:/sbin:/bin" HOME="$J/home"
     RACINE_AMORCE="$J/racine" MODE=jouet BRANCHE_PREFIXE=essai/ VENV_EXISTANT="$DEPOT/.venv" GO_DATE="$(date -u +%F)"
     COMMIT="$LANCE" COMMIT_CODE="$CODE" GH_TOKEN= PRIX_HEURE_USD=0.8 PRIX_STOCKAGE_HEURE_USD=0.05
     ECHEANCE_UTC_S=$(( $(date +%s) + 10800 )) CONTAINER_ID=1 CONTAINER_API_KEY=factice DEPOT_URL="file://$B")
A="$J/amorce-v9.sh"; git -C "$DEPOT" show "$CODE:scripts/amorce_instance_sparks_exp7_nul_v9.sh" > "$A"
etape() { T 5400 unshare -pf --mount-proc "${ENV[@]}" bash "$A" 2>&1 | grep -v 'rejected bcf1445467fd' > "$J/$1.txt"; echo "== $1 : code ${PIPESTATUS[0]}" | tee -a "$OUT/attendus.txt"
          cp "$J/$1.txt" "$OUT/"; for f in "$J"/racine/sparks/journal.txt "$J"/racine/sparks-causal-*/journal.txt "$J"/racine/sparks/run.err "$J"/racine/sparks-causal-*/run.err "$J/racine/sparks-v5-minuterie.log" "$J/racine/sparks-v5-demarrages.txt"; do
            [ -f "$f" ] && cp "$f" "$OUT/$(echo "${f#$J/racine/}" | tr / _)"; done; }
attendu() { if grep -qE -- "$3" "$2"; then echo "   OK   $1 : « $3 »"; else echo "   ÉCART $1 : « $3 » absent de $2"; fi | tee -a "$OUT/attendus.txt"; }
absent() { if grep -qE -- "$3" "$2" 2>/dev/null; then echo "   ÉCART $1 : « $3 » présent dans $2"; else echo "   OK   $1 : pas de « $3 »"; fi | tee -a "$OUT/attendus.txt"; }
O="$J/ordres-depot"; git init -q "$O"; git -C "$O" remote add origin "file://$B"; mkdir -p "$O/ordres"
ordre() { echo "$2" > "$O/ordres/ordre-$1.json"; git -C "$O" add ordres && git -C "$O" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : ordre $1" \
          && git -C "$O" push -q origin "HEAD:refs/heads/ordres/sparks-exp7-nul-v5-$COURT"; }
etape 1-creation
attendu 1 "$J/1-creation.txt" "AMORCE V5 : outils : curl oui, git oui, unshare oui"
attendu 1 "$J/1-creation.txt" "mode jouet : addendum non exigé"
attendu 1 "$J/1-creation.txt" "fabrication, durée plafonnée"
attendu 1 "$J/racine/sparks/journal.txt" "essais : [0-9]+ passed"
attendu 1 "$J/racine/sparks/journal.txt" "essai d'égalité des lots : oui"
attendu 1 "$J/racine/sparks/journal.txt" "MANIFESTE CRÉÉ : runs/.*préenregistrement prereg/SPARKS-EXP7-NUL-addendum-1.md"
attendu 1 "$J/racine/sparks/journal.txt" "ADDENDUM FACTICE \(jouet\)"
absent  1 "$J/racine/sparks/run.err" "No module named"
attendu 1 "$J/racine/sparks/run.err" "ARRET 0/28 modèles dans les bornes"
attendu 1 "$J/racine/sparks/journal.txt" "poussée vérifiée sur essai/sparks-exp7-nul-v5-$COURT"
attendu 1 "$J/racine/sparks-v5-demarrages.txt" "^d [0-9]+ [0-9]+$"
ordre 001 '{"numero": 1, "instance": "1", "phase": "copie", "deja_usd": 1.0, "cas": ["vraie01"], "premier": true, "copie_minutes": 5}'
etape 2-copie
attendu 2 "$J/2-copie.txt" "redémarrage consigné au registre des démarrages : démarrage n° 2"
attendu 2 "$J/2-copie.txt" "ordre 1 \(copie\)"
attendu 2 "$J/2-copie.txt" "lot impossible"
absent  2 "$J/2-copie.txt" "boucle de redémarrage présumée"
mkdir -p "$O/ordres/causal/reponses" && echo '{}' > "$O/ordres/causal/cle-ouverte-v1.json" && touch "$O/ordres/causal/reponses/.garde"
ordre 002 '{"numero": 2, "instance": "1", "phase": "causal", "deja_usd": 2.0}'
etape 3-causal
attendu 3 "$J/3-causal.txt" "ordre 2 \(causal\)"
attendu 3 "$J/racine/sparks-causal-002/journal.txt" "essais : [0-9]+ passed"
attendu 3 "$J/racine/sparks-causal-002/journal.txt" "MANIFESTE CRÉÉ : runs/.*préenregistrement prereg/SPARKS-EXP7-NUL-addendum-1.md"
absent  3 "$J/racine/sparks-causal-002/run.err" "No module named"
attendu 3 "$J/racine/sparks-causal-002/journal.txt" "fin du calcul, code [1-9]"
attendu 3 "$J/3-causal.txt" "fin de la phase causale, code [1-9], poussée vérifiée"
absent  3 "$J/3-causal.txt" "boucle de redémarrage présumée"
etape 4-relance-sans-ordre-neuf
attendu 4 "$J/4-relance-sans-ordre-neuf.txt" "démarrage n° 6"
attendu 4 "$J/4-relance-sans-ordre-neuf.txt" "ordre refusé \(aucun ordre neuf\) : boucle de redémarrage présumée, destruction immédiate"
echo "   DELETE au journal : $(grep -c 'DELETE instance 1 ' "$J/racine/sparks-v5-minuterie.log") (attendu : 1)" | tee -a "$OUT/attendus.txt"
if pgrep -f "$J/racine/sparks-v5-minuterie.sh" >/dev/null; then echo "   ÉCART : minuterie restante"; else echo "   OK   aucune minuterie restante"; fi | tee -a "$OUT/attendus.txt"
cp "$J/racine/sparks-v5-minuterie.log" "$J/racine/sparks-v5-demarrages.txt" "$OUT/" 2>/dev/null
echo "FIN DE LA RÉPÉTITION $(date -u +%FT%TZ)" | tee -a "$OUT/attendus.txt"
