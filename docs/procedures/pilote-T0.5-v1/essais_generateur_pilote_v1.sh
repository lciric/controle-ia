#!/usr/bin/env bash
# Banc du générateur du pilote de T0.5 (R5 ; relecture R2, CH-06, CH-07, CH-10, NO-03), sur un clone jetable du commit
# C (brouillon 10 scellé, proposition N-019 v2 scellée) : un cas sain par mode (candidat, reel) et un artefact par garde
# nouvelle ; chaque artefact est fait dans le clone (commit), joué, puis défait (retour au commit de départ). Le
# générateur joué est celui du bloc-notes (empreinte du brouillon épinglée). Décision de Lazar simulée dans le clone
# seulement (GO-2026-10-12-99, R-990). Verdict : code attendu et motif attendu dans le message d'arrêt.
# Usage : essais_generateur_pilote_v1.sh DEPOT_SOURCE C RACINE_NEUVE
set -uo pipefail
SRC=$1; C=$2; R=$3
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
HN=${HN:-$BN/pilote-v1}
PY=$BN/scellement-revalidation/venv-gpu-neuf/bin/python
TACHES=donnees/t05-pilote-v1/taches-pilote-60-v1.json
B10=brouillons/T0.5-pilote-8B-v1-brouillon10.md
GO=GO-2026-10-12-99; REG=R-990
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R" && cd "$R" || exit 2
git clone -q --no-local "$SRC" depot && cd depot && git checkout -q "$C" && git checkout -q -B main || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
echo "C = $(git rev-parse HEAD) ; générateur $(sha256sum "$HN/remplir_pilote_v1.py" | cut -d' ' -f1)"
ETAT=$(for f in prereg/contre-lectures/T0.5-pilote-v1-etat-des-lieux-*-v1.*; do case $f in *.sha256) ;; *) printf '%s=%s,' "$(basename "$f")" "$(sha256sum "$f" | cut -d' ' -f1)" ;; esac; done); ETAT=${ETAT%,}
REL="T0.5-pilote-v1-relecture-b8-essai-v1.md=$(printf '0%.0s' {1..64})"
echo 1234567890123456789 > "$R/entropie.txt"
resceller() { local f; for f in "$@"; do (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); done; }
n=0
generer() {   # $1 nom, $2 mode, $3 date, puis arguments supplémentaires
    local nom=$1 mode=$2 date=$3; shift 3; n=$((n + 1))
    rm -f "$R/sortie-$nom.md" "$R/sortie-$nom.json"
    "$PY" -I "$HN/remplir_pilote_v1.py" . "$(git rev-parse HEAD)" "$mode" "$date" "$R/entropie.txt" "$R/sortie-$nom.md" \
        "$R/sortie-$nom.json" --rapports-etat "$ETAT" --rapports-relecture "$REL" "$@" > "$R/gen-$nom.txt" 2>&1
}
jouer() {   # $1 nom, $2 code attendu, $3 motif attendu (vide : cas sain), $4 modification (commit), $5 mode, $6 date, puis arguments
    local nom=$1 attendu=$2 motif=$3 modif=$4 mode=$5 date=$6; shift 6
    local base; base=$(git rev-parse HEAD)
    eval "$modif"
    if [ -n "$(git status --porcelain --untracked-files=no)" ]; then git add -A . && git commit -qm "essai : $nom" || { echo "$nom : commit impossible"; return; }; fi
    generer "$nom" "$mode" "$date" "$@"; local c=$?
    local v="CONFORME"
    [ "$c" = "$attendu" ] || v="NON CONFORME (code $c, attendu $attendu)"
    if [ -n "$motif" ] && ! grep -qF -- "$motif" "$R/gen-$nom.txt"; then v="NON CONFORME (motif « $motif » absent)"; fi
    echo "$nom : code $c ; $v"
    tail -1 "$R/gen-$nom.txt" | cut -c1-200 | sed 's/^/    | /'
    git reset -q --hard "$base"
}
MAINTENANT=$(date -u '+%Y-%m-%d %H:%M UTC')
jouer G00-candidat-sain 0 "" ":" candidat "$MAINTENANT" --taches "$TACHES"
NS=$(sed -n 's/.*"normalise_sha256": "\([0-9a-f]*\)".*/\1/p' "$R/gen-G00-candidat-sain.txt"); echo "    normalisé du candidat sain : $NS"
jouer G01-taches-autre-chemin 1 "seul $TACHES est admis" "mkdir -p donnees/autre && cp $TACHES donnees/autre/copie.json && resceller donnees/autre/copie.json && git add -f donnees/autre" candidat "$MAINTENANT" --taches donnees/autre/copie.json
jouer G02-date-libre-candidat 1 "date attendue au format" ":" candidat "n'importe quoi" --taches "$TACHES"
jouer G03-date-libre-jouet 1 "date attendue au format" ":" jouet "2026-10-12 (répétition)" --taches "$TACHES"
jouer G04-brouillon-modifie-sceau-laisse 1 "sceau absent ou différent" "echo ' ' >> $B10" candidat "$MAINTENANT" --taches "$TACHES"
jouer G05-brouillon-modifie-rescelle 1 "empreinte non épinglée ou" "echo ' ' >> $B10 && resceller $B10" candidat "$MAINTENANT" --taches "$TACHES"
jouer G06-lecture-math-modifiee 1 "lecture-math.json : sceau absent ou différent" "sed -i 's/\"conforme\": false/\"conforme\": true/' diag/20261011-225701-t05-revalidation-reel/lecture-math.json" candidat "$MAINTENANT" --taches "$TACHES"
jouer G07-brouillon-config-modifie 1 "T0.5-pilote-config-v1-brouillon1.json : empreinte" "sed -i 's/\"lot\": 8/\"lot\": 4/' brouillons/T0.5-pilote-config-v1-brouillon1.json" candidat "$MAINTENANT" --taches "$TACHES"
jouer G08-go-hors-du-mode-reel 1 "mode reel seulement" ":" candidat "$MAINTENANT" --taches "$TACHES" --go "$GO" --registre "$REG"
# mode reel : candidat relu versé dans le clone (le texte sain du mode candidat), rapport fictif de la relecture versé et
# scellé (le mode reel vérifie les rapports cités ; ligne masquée par la normalisation), décision de Lazar simulée
cp "$R/sortie-G00-candidat-sain.md" brouillons/essai-candidat-relu.md && resceller brouillons/essai-candidat-relu.md
printf 'rapport fictif (banc du générateur)\n' > prereg/contre-lectures/T0.5-pilote-v1-relecture-b8-essai-v1.md
resceller prereg/contre-lectures/T0.5-pilote-v1-relecture-b8-essai-v1.md
REL="T0.5-pilote-v1-relecture-b8-essai-v1.md=$(sha256sum prereg/contre-lectures/T0.5-pilote-v1-relecture-b8-essai-v1.md | cut -d' ' -f1)"
python3 - "$GO" "$REG" <<'PYGO' || exit 2
import sys
from pathlib import Path
go, reg = sys.argv[1:3]
d = Path("registres/decisions.md"); lignes = d.read_text(encoding="utf-8").split("\n")
i = [k for k, x in enumerate(lignes) if x.startswith("| N-019 |")]
assert len(i) == 1
lignes[i[0]] = lignes[i[0]].rsplit("|", 2)[0] + f"| tranché (a) par Lazar : {go} ({reg}) |"
d.write_text("\n".join(lignes).rstrip("\n") + f"\n| {reg} | 2026-10-12 | essai : {go} de Lazar sur N-019, option (a) | — |\n", encoding="utf-8")
g = Path("registres/go.md")
g.write_text(g.read_text(encoding="utf-8").rstrip("\n") + f"\n| {go} | 2026-10-12 | revendication | N-019, option (a) (essai) | — | 2026-10-12 | Lazar | {reg} (essai) |\n", encoding="utf-8")
PYGO
git add -A . && git commit -qm "essai : candidat relu et GO fictif" || exit 2
REEL=(--taches "$TACHES" --candidat-relu brouillons/essai-candidat-relu.md --go "$GO" --registre "$REG")
MAINTENANT=$(date -u '+%Y-%m-%d %H:%M UTC')
jouer G10-reel-sain 0 "" ":" reel "$MAINTENANT" "${REEL[@]}"
NR=$(sed -n 's/.*"normalise_sha256": "\([0-9a-f]*\)".*/\1/p' "$R/gen-G10-reel-sain.txt")
[ -n "$NR" ] && [ "$NR" = "$NS" ] && echo "    normalisé du texte reel = normalisé du candidat ($NR) : CONFORME" || echo "    normalisé du texte reel $NR ≠ $NS : NON CONFORME"
jouer G11-reel-sans-go 1 "--go GO-AAAA-MM-JJ-NN et --registre R-NNN exigés" ":" reel "$MAINTENANT" --taches "$TACHES" --candidat-relu brouillons/essai-candidat-relu.md
jouer G12-reel-date-ancienne 1 "de l'horloge" ":" reel "2026-10-11 00:00 UTC" "${REEL[@]}"
jouer G13-n019-forme-inexacte 1 "N-019 : colonne d'état" "sed -i -E 's/^(\| N-019 \|.*)\| tranché \(a\) par Lazar : [^|]*\|$/\1| tranché le 2026-10-12 par Lazar : option (a), $GO ($REG) |/' registres/decisions.md" reel "$MAINTENANT" "${REEL[@]}"
jouer G14-n019-suite-ajoutee 1 "N-019 : colonne d'état" "sed -i -E 's/^(\| N-019 \|.*)\| tranché \(a\) par Lazar : [^|]*\|$/\1| tranché (a) par Lazar : $GO ($REG) ; révoqué |/' registres/decisions.md" reel "$MAINTENANT" "${REEL[@]}"
jouer G15-go-revoque 1 "révoqué dans registres/go.md" "echo '| GO-2026-10-12-98 | 2026-10-12 | révocation | révoque $GO (essai) | — | — | Lazar | essai |' >> registres/go.md" reel "$MAINTENANT" "${REEL[@]}"
jouer G15b-go-revoque-ligne-mal-formee 1 "révoqué dans registres/go.md" "echo '| GO-2026-10-12-98 | 2026-10-12 | révocation de $GO (essai) |' >> registres/go.md" reel "$MAINTENANT" "${REEL[@]}"
jouer G15c-ligne-go-qui-mentionne-une-revocation 0 "" "echo '| GO-2026-10-12-97 | 2026-10-12 | revendication | essai : aucune révocation de $GO | — | — | Lazar | essai |' >> registres/go.md" reel "$MAINTENANT" "${REEL[@]}"
jouer G16-go-autre-type 1 "type 'calcul'" "sed -i 's/^| $GO | 2026-10-12 | revendication |/| $GO | 2026-10-12 | calcul |/' registres/go.md" reel "$MAINTENANT" "${REEL[@]}"
jouer G17-go-option-b 1 "sans N-019 et l'option (a)" "sed -i 's/| N-019, option (a) (essai) |/| N-019, option (b) (essai) |/' registres/go.md" reel "$MAINTENANT" "${REEL[@]}"
jouer G18-registre-absent 1 "$REG : ligne absente" "sed -i '/^| $REG |/d' registres/decisions.md" reel "$MAINTENANT" "${REEL[@]}"
jouer G19-candidat-relu-different 1 "version écrite ≠ candidat relu" "sed -i '0,/sous 48 tâches complètes pour ce juge/s//sous 47 tâches complètes pour ce juge/' brouillons/essai-candidat-relu.md && resceller brouillons/essai-candidat-relu.md" reel "$MAINTENANT" "${REEL[@]}"
cd "$R" && rm -rf "$R/depot"
echo "FIN DU BANC DU GÉNÉRATEUR DU PILOTE ($n générations)"
