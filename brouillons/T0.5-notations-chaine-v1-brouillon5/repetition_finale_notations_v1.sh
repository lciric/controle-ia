#!/usr/bin/env bash
# Répétition finale à blanc du scellement des notations refaites du pilote de T0.5 (N-021, option (a)) et des contrôles
# avant dépense, déclinée de repetition_finale_pilote_v1.sh. Sur un clone jetable du commit des préalables C (épingles
# réelles, candidat et configuration relus réels, rapports réels, copies versées réelles, registres réels : la décision
# de Lazar sur N-021 est déjà consignée, aucun GO fictif) et un dépôt nu local : copie versée du scellement remplacée par
# une copie dont seules les lignes H et DEPOT changent (re-scellée, committée dans le clone) ; les autres scripts du faux
# bloc-notes H sont les copies versées à C, à l'identique. Puis scellement (code 0 et un commit attendus) et contrôles
# sur le commit produit (copie dont seule la ligne DEPOT change ; tous conformes attendus, suite complète et vrais
# tokeniseurs compris). Aucun service de location n'est appelé ; GitHub n'est pas touché (dépôt nu local) ; Hugging Face
# est lu (tokeniseurs des contrôles). Brouillon 3 (contre-lecture R2 de la chaîne) : liste des scripts lue dans la liste
# CHAINE de la copie versée du scellement (jamais recopiée ici) ; copies jouées vérifiées sans adresse du dépôt réel ;
# chemins absolus ; code 1 si la répétition n'est pas conforme.
# Usage : repetition_finale_notations_v1.sh RACINE_NEUVE C
set -uo pipefail
E=$(realpath -m "${1:?racine neuve}"); C=${2:?commit des préalables}; SOI=$(realpath "$0")
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
HN=$BN/notations-v1
D=/home/user/controle-ia-travail
PY=$BN/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/T0.5-pilote-notations-v1.md; CFG=prereg/T0.5-pilote-notations-config-v1.json; V=docs/procedures/notations-T0.5-v1
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/H" && cd "$E" || exit 2
git clone -q --no-local "$D" depot && cd depot && git checkout -q "$C" && git checkout -q -B main || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
echo "C = $(git rev-parse HEAD)"
# scripts éprouvés : les copies versées à C (la copie jouée du scellement n'en change que les lignes H et DEPOT, celle des
# contrôles la ligne DEPOT), et cette répétition
for s in sceller_notations_v1.sh controles_avant_depense_notations_v1.sh verifications_notations_v1.py; do
    echo "script éprouvé : $s $(sha256sum "$V/$s" | cut -d' ' -f1)"; done
echo "script éprouvé : $(basename "$SOI") $(sha256sum "$SOI" | cut -d' ' -f1)"
SCRIPTS=$(sed -n '/^CHAINE="/,/"$/p' "$V/sceller_notations_v1.sh" | tr -d '"' | sed 's/^CHAINE=//')
echo "scripts de la chaîne : $(echo $SCRIPTS | wc -w)"
[ "$(echo $SCRIPTS | wc -w)" = 13 ] || { echo "liste CHAINE inattendue"; exit 2; }
for s in $SCRIPTS; do
    cmp -s "$V/$s" "$HN/$s" && echo "copie versée de $s = bloc-notes" || { echo "copie versée de $s ≠ bloc-notes"; exit 2; }
done
grep -q "^[A-Z_]*=\"\{0,1\}A_EPINGLER" "$V/controles_avant_depense_notations_v1.sh" && { echo "épingles absentes de la copie versée des contrôles"; exit 2; }
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . | tail -1 | grep -q "arbre intact" && echo "C : arbre intact" || { echo "C : arbre non intact"; exit 2; }
for s in $SCRIPTS; do cp "$V/$s" "$E/H/$s"; done
sed -e "s|^H=.*|H=$E/H|" -e "s|^DEPOT=.*|DEPOT=$E/depot|" -e "s|^DISTANT=.*|DISTANT=$E/distant.git|" "$V/sceller_notations_v1.sh" > "$E/H/sceller_notations_v1.sh"
echo "lignes changées dans la copie du scellement : $(diff "$V/sceller_notations_v1.sh" "$E/H/sceller_notations_v1.sh" | grep -c '^>')"
grep -n "controle-ia-travail\|github" "$E/H/sceller_notations_v1.sh" && { echo "COPIE DU SCELLEMENT NON SÛRE"; exit 2; }
cp "$E/H/sceller_notations_v1.sh" "$V/sceller_notations_v1.sh" && (cd "$V" && sha256sum sceller_notations_v1.sh > sceller_notations_v1.sh.sha256)
git add -A "$V" && git commit -qm "essai : copie du scellement de la répétition" || exit 2
git clone -q --bare . "$E/distant.git" && git remote set-url origin "$E/distant.git" && git fetch -q origin || exit 2
BASE=$(git rev-parse HEAD)
bash "$E/H/sceller_notations_v1.sh" > "$E/sortie-scellement.txt" 2>&1; c=$?
S=$(git rev-parse HEAD)
echo "scellement : code $c ; $(grep -v '^$' "$E/sortie-scellement.txt" | tail -1 | cut -c1-160)"
if [ "$c" = 0 ] && [ "$S" != "$BASE" ] && [ "$(git -C "$E/distant.git" rev-parse main)" = "$S" ] && [ "$(git rev-parse "$S^")" = "$BASE" ] \
   && [ "$(git diff --name-only "$BASE" "$S" | sort | tr '\n' ' ')" = "$(printf '%s\n' "$CFG" "$CFG.sha256" "$P" "$P.sha256" | sort | tr '\n' ' ')" ] \
   && [ -z "$(git status --porcelain --untracked-files=no)" ]; then
    echo "scellement : CONFORME (commit $S poussé, enfant de la base, qui n'ajoute que le préenregistrement, la configuration et leurs sceaux)"
    SCELLEMENT_CONFORME=oui
else echo "scellement : NON CONFORME"; SCELLEMENT_CONFORME=non; fi
echo "préenregistrement : $(cut -d' ' -f1 "$P.sha256" 2>/dev/null)"
sed "s|^DEPOT=.*|DEPOT=$E/distant.git|" "$V/controles_avant_depense_notations_v1.sh" > "$E/controles-repetition.sh"
echo "lignes changées dans la copie des contrôles : $(diff "$V/controles_avant_depense_notations_v1.sh" "$E/controles-repetition.sh" | grep -c '^>')"
grep -n "github" "$E/controles-repetition.sh" && { echo "COPIE DES CONTRÔLES NON SÛRE"; exit 2; }
debut=$(date +%s)
bash "$E/controles-repetition.sh" "$S" "$E/clone-controles" > "$E/sortie-controles.txt" 2>&1; c2=$?; rm -rf "$E/clone-controles"
echo "contrôles sur le commit scellé : code $c2 ; $(tail -1 "$E/sortie-controles.txt") ; $(grep -c '^OK' "$E/sortie-controles.txt") OK, $(grep -c '^KO' "$E/sortie-controles.txt") KO ; $(( $(date +%s) - debut )) s"
grep '^KO' "$E/sortie-controles.txt" | sed 's/^/    /'
grep -E '^OK  suite complète|^OK  format' "$E/sortie-controles.txt" | sed 's/^/    /' | cut -c1-200
{ git -C "$E/distant.git" log --stat -3 main; } > "$E/depot-resume.txt" 2>&1
# verdict : scellement conforme (code, commit, contenu, poussée) et contrôles conformes (vérification courte, constat 2)
if [ "$SCELLEMENT_CONFORME" = oui ] && [ "$c2" = 0 ]; then echo "RÉPÉTITION FINALE : CONFORME"; else echo "RÉPÉTITION FINALE : NON CONFORME"; exit 1; fi
