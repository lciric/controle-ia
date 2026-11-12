#!/usr/bin/env bash
# Répétition finale à blanc du scellement du pilote de T0.5 et des contrôles avant dépense (plan de lancement du pilote,
# préalable 5), sur le modèle de repetition_finale_scellement_v1.sh de la revalidation. Sur un clone jetable du commit
# des préalables C (épingles réelles, rapports réels, copies versées réelles) et un dépôt nu local : copie versée du
# scellement remplacée par une copie dont seules les lignes H et DEPOT changent (re-scellée) ; les autres scripts du faux
# bloc-notes H sont les copies versées à C, à l'identique. Puis scellement (code 0 et un commit attendus) et contrôles
# sur le commit produit (copie dont seule la ligne DEPOT change ; tous conformes attendus, suite complète comprise).
# Aucun service de location n'est appelé ; seuls GitHub n'est pas touché (dépôt nu local) et Hugging Face est lu
# (tokeniseurs des contrôles).
# Décision de Lazar sur N-019 simulée dans le clone jetable seulement : GO fictif GO-2026-10-12-99 (type « revendication »,
# accordé par Lazar, option (a)), colonne d'état de N-019 à la forme exacte qui le cite, ligne R-990 qui le consigne.
# Usage : repetition_finale_pilote_v1.sh RACINE_NEUVE C
set -uo pipefail
E=$1; C=$2
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
HN=$BN/pilote-v1
D=/home/user/controle-ia-travail
PY=$BN/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/T0.5-pilote-8B-v1.md; V=docs/procedures/pilote-T0.5-v1
GO=GO-2026-10-12-99; REG=R-990
SCRIPTS="deriver_taches_pilote_v1.py remplir_pilote_v1.py normaliser_pilote_v1.py controles_avant_depense_pilote_v1.sh
         lancer_pilote_v1.sh sceller_pilote_v1.sh recuperation_pilote_v1.sh repetition_jouet_pilote_v1.sh
         repetition_finale_pilote_v1.sh essais_lanceur_pilote_v1.sh essais_controles_pilote_v1.sh essais_generateur_pilote_v1.sh
         essais_scellement_pilote_v1.sh"   # liste CHAINE du scellement
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/H" && cd "$E" || exit 2
git clone -q --no-local "$D" depot && cd depot && git checkout -q "$C" && git checkout -q -B main || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
echo "C = $(git rev-parse HEAD)"
for s in $SCRIPTS; do
    cmp -s "$V/$s" "$HN/$s" && echo "copie versée de $s = bloc-notes" || { echo "copie versée de $s ≠ bloc-notes"; exit 2; }
done
grep -q "A_EPINGLER" "$V/controles_avant_depense_pilote_v1.sh" && { echo "épingles absentes de la copie versée des contrôles"; exit 2; }
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . | tail -1 | grep -q "arbre intact" && echo "C : arbre intact" || { echo "C : arbre non intact"; exit 2; }
python3 - "$GO" "$REG" <<'PYGO' || exit 2
import sys
from pathlib import Path
go, reg = sys.argv[1:3]
d = Path("registres/decisions.md"); t = d.read_text(encoding="utf-8")
lignes = t.split("\n")
i = [k for k, x in enumerate(lignes) if x.startswith("| N-019 |")]
assert len(i) == 1
cellules = lignes[i[0]].rsplit("|", 2)
lignes[i[0]] = cellules[0] + f"| tranché (a) par Lazar : {go} ({reg}) |"     # forme exacte (CH-10)
t = "\n".join(lignes).rstrip("\n") + f"\n| {reg} | 2026-10-12 | essai : {go} de Lazar sur N-019, option (a) | — |\n"
d.write_text(t, encoding="utf-8")
g = Path("registres/go.md")
g.write_text(g.read_text(encoding="utf-8").rstrip("\n") + f"\n| {go} | 2026-10-12 | revendication | N-019, option (a) (essai) | — | — | Lazar | {reg} (essai) |\n", encoding="utf-8")
PYGO
for s in $SCRIPTS; do cp "$V/$s" "$E/H/$s"; done
sed -e "s|^H=.*|H=$E/H|" -e "s|^DEPOT=.*|DEPOT=$E/depot|" "$V/sceller_pilote_v1.sh" > "$E/H/sceller_pilote_v1.sh"
echo "lignes changées dans la copie du scellement : $(diff "$V/sceller_pilote_v1.sh" "$E/H/sceller_pilote_v1.sh" | grep -c '^>')"
cp "$E/H/sceller_pilote_v1.sh" "$V/sceller_pilote_v1.sh" && (cd "$V" && sha256sum sceller_pilote_v1.sh > sceller_pilote_v1.sh.sha256)
git add -A "$V" registres && git commit -qm "essai : GO fictif de Lazar sur N-019, copie du scellement de la répétition" || exit 2
git clone -q --bare . "$E/distant.git" && git remote set-url origin "$E/distant.git" && git fetch -q origin || exit 2
BASE=$(git rev-parse HEAD)
bash "$E/H/sceller_pilote_v1.sh" "$GO" "$REG" > "$E/sortie-scellement.txt" 2>&1; c=$?
S=$(git rev-parse HEAD)
echo "scellement : code $c ; $(grep -v '^$' "$E/sortie-scellement.txt" | tail -1 | cut -c1-160)"
if [ "$c" = 0 ] && [ "$S" != "$BASE" ] && [ "$(git -C "$E/distant.git" rev-parse main)" = "$S" ] && [ "$(git rev-parse "$S^")" = "$BASE" ] \
   && [ "$(git diff --name-only "$BASE" "$S" | sort | tr '\n' ' ')" = "prereg/T0.5-pilote-8B-v1.md prereg/T0.5-pilote-8B-v1.md.sha256 prereg/T0.5-pilote-config-v1.json prereg/T0.5-pilote-config-v1.json.sha256 " ] \
   && [ -z "$(git status --porcelain --untracked-files=no)" ]; then
    echo "scellement : CONFORME (commit $S poussé, enfant de la base, qui n'ajoute que le préenregistrement, la configuration et leurs sceaux)"
else echo "scellement : NON CONFORME"; fi
echo "préenregistrement : $(cut -d' ' -f1 "$P.sha256" 2>/dev/null)"
sed "s|^DEPOT=.*|DEPOT=$E/distant.git|" "$V/controles_avant_depense_pilote_v1.sh" > "$E/controles-repetition.sh"
echo "lignes changées dans la copie des contrôles : $(diff "$V/controles_avant_depense_pilote_v1.sh" "$E/controles-repetition.sh" | grep -c '^>')"
debut=$(date +%s)
bash "$E/controles-repetition.sh" "$S" "$E/clone-controles" > "$E/sortie-controles.txt" 2>&1; c2=$?; rm -rf "$E/clone-controles"
echo "contrôles sur le commit scellé : code $c2 ; $(tail -1 "$E/sortie-controles.txt") ; $(grep -c '^OK' "$E/sortie-controles.txt") OK, $(grep -c '^KO' "$E/sortie-controles.txt") KO ; $(( $(date +%s) - debut )) s"
grep '^KO' "$E/sortie-controles.txt" | sed 's/^/    /'
{ git -C "$E/distant.git" log --stat -3 main; } > "$E/depot-resume.txt" 2>&1
[ "$c" = 0 ] && [ "$c2" = 0 ] && echo "RÉPÉTITION FINALE : CONFORME" || echo "RÉPÉTITION FINALE : NON CONFORME"
