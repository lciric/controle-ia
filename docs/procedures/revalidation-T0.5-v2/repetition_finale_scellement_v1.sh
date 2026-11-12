#!/usr/bin/env bash
# Répétition finale à blanc du scellement de la v2 et des contrôles avant dépense (plan de lancement v7, préalable 3).
# Sur un clone jetable du commit des préalables C (épingles réelles, rapports réels, copies versées réelles) et un dépôt
# nu local : GO fictif accordé par Lazar sur N-018, N-018 tranché, ligne R-990 ; copie versée du scellement remplacée
# par une copie dont seules les lignes H et DEPOT changent (re-scellée) ; les autres scripts du faux bloc-notes H sont
# les copies versées à C, à l'identique. Puis scellement (code 0 et un commit attendus) et contrôles v7 sur le commit
# produit (copie dont seule la ligne DEPOT change ; tous conformes attendus). Aucun service extérieur n'est appelé.
# Usage : repetition_finale_scellement_v1.sh RACINE_NEUVE C
set -uo pipefail
E=$1; C=$2
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
R=$BN/revalidation-v2
D=/home/user/controle-ia-travail
PY=$BN/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/T0.5-revalidation-equivalence-pilote-v2.md; V=docs/procedures/revalidation-T0.5-v2
GO=GO-2026-10-11-99; REG=R-990
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/H" && cd "$E" || exit 2
git clone -q --no-local "$D" depot && cd depot && git checkout -q "$C" && git checkout -q -B main || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
echo "C = $(git rev-parse HEAD)"
for s in remplir_revalidation_v2_r4.py controles_avant_depense_v7.sh lancer_revalidation_v7.sh sceller_revalidation_v5.sh recuperation_revalidation_v2.sh; do
    cmp -s "$V/$s" "$R/$s" && echo "copie versée de $s = bloc-notes" || { echo "copie versée de $s ≠ bloc-notes"; exit 2; }
done
grep -q "A_EPINGLER" "$V/controles_avant_depense_v7.sh" && { echo "épingles absentes de la copie versée des contrôles"; exit 2; }
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . | tail -1 | grep -q "arbre intact" && echo "C : arbre intact" || { echo "C : arbre non intact"; exit 2; }
python3 - <<EOF || exit 2
from pathlib import Path
d = Path("registres/decisions.md"); t = d.read_text(encoding="utf-8")
l = [x for x in t.split("\n") if x.startswith("| N-018 |")][0]
t = t.replace(l, l.rsplit("| en attente |", 1)[0] + "| tranché : option (a), $GO (essai) |")
d.write_text(t.rstrip("\n") + "\n| $REG | 2026-10-11 | essai : $GO consigné | — |\n", encoding="utf-8")
g = Path("registres/go.md")
g.write_text(g.read_text(encoding="utf-8").rstrip("\n") + "\n| $GO | 2026-10-11 | revendication | N-018, option (a) (essai) | — | — | Lazar | $REG (essai) |\n", encoding="utf-8")
EOF
for s in remplir_revalidation_v2_r4.py controles_avant_depense_v7.sh lancer_revalidation_v7.sh recuperation_revalidation_v2.sh; do cp "$V/$s" "$E/H/$s"; done
sed -e "s|^H=.*|H=$E/H|" -e "s|^DEPOT=.*|DEPOT=$E/depot|" "$V/sceller_revalidation_v5.sh" > "$E/H/sceller_revalidation_v5.sh"
echo "lignes changées dans la copie du scellement : $(diff "$V/sceller_revalidation_v5.sh" "$E/H/sceller_revalidation_v5.sh" | grep -c '^>')"
cp "$E/H/sceller_revalidation_v5.sh" "$V/sceller_revalidation_v5.sh" && (cd "$V" && sha256sum sceller_revalidation_v5.sh > sceller_revalidation_v5.sh.sha256)
git add -A registres "$V" && git commit -qm "essai : GO fictif, N-018 tranché, copie du scellement de l'essai" || exit 2
git clone -q --bare . "$E/distant.git" && git remote set-url origin "$E/distant.git" && git fetch -q origin || exit 2
BASE=$(git rev-parse HEAD)
bash "$E/H/sceller_revalidation_v5.sh" "$GO" "$REG" > "$E/sortie-scellement.txt" 2>&1; c=$?
S=$(git rev-parse HEAD)
echo "scellement : code $c ; $(grep -v '^$' "$E/sortie-scellement.txt" | tail -1 | cut -c1-160)"
if [ "$c" = 0 ] && [ "$S" != "$BASE" ] && [ "$(git -C "$E/distant.git" rev-parse main)" = "$S" ] && [ "$(git rev-parse "$S^")" = "$BASE" ] \
   && [ "$(git diff --name-only "$BASE" "$S" | sort | tr '\n' ' ')" = "$P $P.sha256 " ] && [ -z "$(git status --porcelain)" ]; then
    echo "scellement : CONFORME (commit $S poussé, enfant de la base, qui ajoute la v2 et son sceau seulement ; arbre propre)"
else echo "scellement : NON CONFORME"; fi
echo "v2 : $(cut -d' ' -f1 "$P.sha256")"
sed "s|^DEPOT=.*|DEPOT=$E/distant.git|" "$V/controles_avant_depense_v7.sh" > "$E/controles-repetition.sh"
echo "lignes changées dans la copie des contrôles : $(diff "$V/controles_avant_depense_v7.sh" "$E/controles-repetition.sh" | grep -c '^>')"
bash "$E/controles-repetition.sh" "$S" "$E/clone-controles" > "$E/sortie-controles.txt" 2>&1; c2=$?; rm -rf "$E/clone-controles"
echo "contrôles v7 sur le commit scellé : code $c2 ; $(tail -1 "$E/sortie-controles.txt") ; $(grep -c '^OK' "$E/sortie-controles.txt") OK, $(grep -c '^KO' "$E/sortie-controles.txt") KO"
grep '^KO' "$E/sortie-controles.txt" | sed 's/^/    /'
{ git -C "$E/distant.git" log --stat -3 main; } > "$E/depot-resume.txt" 2>&1
[ "$c" = 0 ] && [ "$c2" = 0 ] && echo "RÉPÉTITION FINALE : CONFORME" || echo "RÉPÉTITION FINALE : NON CONFORME"
