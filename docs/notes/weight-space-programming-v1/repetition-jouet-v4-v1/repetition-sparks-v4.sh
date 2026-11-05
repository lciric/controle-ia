#!/usr/bin/env bash
# Répétition jouet de SPARKS-EXP7-NUL v4 : création, redémarrage de copie, phase causale, fin. Aucune instance, aucun vastai,
# curl simulé (aucun appel à Vast) ; écrit seulement des branches essai/… et ordres/… sur le dépôt distant, supprimées à la fin.
set -uo pipefail
CODE=53d4eda68560a7eb5b2ceca1fd069f9fd9dcaa30           # commit du code v4 (le remplacer par le commit final s'il change)
DEPOT=/home/user/controle-ia-travail                   # clone de la session mère (relié au dépôt distant)
URL=https://github.com/lciric/controle-ia-travail.git
J=$(mktemp -d /tmp/repetition-sparks-v4-XXXX); mkdir -p "$J/faux-bin" "$J/racine" "$J/home"
T() { timeout -k 10 "$@"; }                            # tout est borné
# 0. Commit de répétition dans un arbre à part (l'arbre du code n'est pas touché) : addendum FICTIF scellé + GO de main
T 600 git -C "$DEPOT" worktree add -q --no-checkout -b essai/sparks-v4-repetition "$J/prep" "$CODE"
T 60 git -C "$J/prep" sparse-checkout set --no-cone '/*' '!/*/' '/prereg/SPARKS-EXP7-NUL-*' '/registres/go.md'
T 600 git -C "$J/prep" checkout -q essai/sparks-v4-repetition
cp "$DEPOT/registres/go.md" "$J/prep/registres/go.md"
printf 'Addendum fictif de répétition (aucune valeur) ; commit du code %s\n' "$CODE" > "$J/prep/prereg/SPARKS-EXP7-NUL-addendum-1.md"
(cd "$J/prep/prereg" && sha256sum SPARKS-EXP7-NUL-addendum-1.md > SPARKS-EXP7-NUL-addendum-1.md.sha256)
T 60 git -C "$J/prep" add -A && T 60 git -C "$J/prep" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : répétition v4 (addendum fictif)"
T 300 git -C "$J/prep" push -q origin essai/sparks-v4-repetition || { echo "poussée de la branche d'essai impossible : arrêt"; exit 2; }
LANCE=$(git -C "$J/prep" rev-parse HEAD); COURT=${LANCE:0:12}
printf '#!/bin/bash\necho "curl $*" >> "%s/faux.log"\nprintf 200\n' "$J" > "$J/faux-bin/curl"; chmod +x "$J/faux-bin/curl"
cp "${HOME}/.gitconfig" "$J/home/.gitconfig" 2>/dev/null || true
PROXY=(); for v in HTTPS_PROXY HTTP_PROXY NO_PROXY https_proxy http_proxy no_proxy GIT_SSL_CAINFO SSL_CERT_FILE REQUESTS_CA_BUNDLE; do
  [ -n "${!v:-}" ] && PROXY+=("$v=${!v}"); done
ENV=(env -i PATH="$J/faux-bin:/usr/bin:/bin" HOME="$J/home" GIT_CONFIG_GLOBAL="$J/home/.gitconfig" "${PROXY[@]}"
     RACINE_AMORCE="$J/racine" MODE=jouet BRANCHE_PREFIXE=essai/ VENV_EXISTANT="$DEPOT/.venv" GO_DATE="$(date -u +%F)"
     COMMIT="$LANCE" COMMIT_CODE="$CODE" GH_TOKEN="${GH_TOKEN:-}" PRIX_HEURE_USD=0.8 PRIX_STOCKAGE_HEURE_USD=0.05
     ECHEANCE_UTC_S=$(( $(date +%s) + 7200 )) CONTAINER_ID=1 CONTAINER_API_KEY=factice DEPOT_URL="$URL")
A="$J/prep-code/scripts/amorce_instance_sparks_exp7_nul_v4.sh"
mkdir -p "$J/prep-code/scripts"; T 60 git -C "$DEPOT" show "$CODE:scripts/amorce_instance_sparks_exp7_nul_v4.sh" > "$A"
etape() { local n="$1"; shift; T 3600 "${ENV[@]}" bash "$A" > "$J/$n.txt" 2>&1; echo "== $n : code $?"
          cat "$J/racine/sparks-v4-minuterie.pid" >> "$J/minuteries.txt" 2>/dev/null || true; }
attendu() { if grep -q -- "$2" "$J/$1.txt"; then echo "   OK   $1 : « $2 »"; else echo "   ÉCART $1 : « $2 » absent"; fi; }
# Dépôt d'ordres à part, branche liée au commit de répétition
O="$J/ordres-depot"; T 60 git init -q "$O"; T 60 git -C "$O" remote add origin "$URL"; mkdir -p "$O/ordres"
ordre() { echo "$2" > "$O/ordres/ordre-$1.json"; T 60 git -C "$O" add ordres && T 60 git -C "$O" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : ordre $1" \
          && T 300 git -C "$O" push -q origin "HEAD:refs/heads/ordres/sparks-exp7-nul-v4-$COURT"; }
# 1. Création : minuterie, GO, borne, durée, garde du code, fabrication jouet (attendu : arrêt de la fabrication jouet)
etape 1-creation
attendu 1-creation "minuterie lancée"; attendu 1-creation "AMORCE V4 : création"; attendu 1-creation "fabrication, durée plafonnée"
# 2. Redémarrage de copie (attendu : ordre lu, borne retenue, « lot impossible » en jouet)
ordre 001 '{"numero": 1, "instance": "1", "phase": "copie", "deja_usd": 1.0, "cas": ["vraie01"], "premier": true, "copie_minutes": 5}'
etape 2-copie
attendu 2-copie "AMORCE V4 : redémarrage"; attendu 2-copie "ordre 1 (copie)"; attendu 2-copie "borne retenue"; attendu 2-copie "lot impossible"
# 3. Redémarrage « causal » (clé et réponses factices ; attendu : branche essai/…-causal-v4-<court>-002, calcul jouet en échec, pas de destruction)
mkdir -p "$O/ordres/causal/reponses" && echo '{}' > "$O/ordres/causal/cle-ouverte-v1.json" && touch "$O/ordres/causal/reponses/.garde"
ordre 002 '{"numero": 2, "instance": "1", "phase": "causal", "deja_usd": 2.0}'
etape 3-causal
attendu 3-causal "ordre 2 (causal)"; attendu 3-causal "sans poussée vérifiée"
# 4. Ordre rejoué (attendu : refus), puis « fin » (attendu : DELETE par la minuterie, curl simulé)
etape 4-rejoue; attendu 4-rejoue "ordre refusé"
ordre 003 '{"numero": 3, "instance": "1", "phase": "fin", "deja_usd": 2.0}'
etape 5-fin
attendu 5-fin "ordre 3 (fin)"; grep -c "DELETE instance 1" "$J/racine/sparks-v4-minuterie.log" | sed 's/^/   DELETE au journal : /'
# 6. Nettoyage : toutes les minuteries par leur numéro (R10), branches distantes d'essai, arbre à part
sort -u "$J/minuteries.txt" 2>/dev/null | while read -r p; do kill "$p" 2>/dev/null && echo "   minuterie $p arrêtée"; done
for b in essai/sparks-v4-repetition "essai/sparks-exp7-nul-v4-$COURT" "essai/sparks-exp7-nul-causal-v4-$COURT-002" "ordres/sparks-exp7-nul-v4-$COURT"; do
  T 300 git -C "$DEPOT" push -q origin --delete "$b" 2>/dev/null && echo "   branche $b supprimée" || echo "   branche $b absente ou non supprimée"; done
T 120 git -C "$DEPOT" worktree remove --force "$J/prep"; T 60 git -C "$DEPOT" branch -D essai/sparks-v4-repetition
echo "sorties : $J/*.txt ; journal de la minuterie : $J/racine/sparks-v4-minuterie.log"
