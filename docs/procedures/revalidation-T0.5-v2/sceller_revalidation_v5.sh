#!/usr/bin/env bash
# Scellement de la version 2 du préenregistrement de la revalidation (T0.5), après le GO de Lazar sur N-018 (plan de
# lancement v7, étape 1). v5 : après le contrôle mécanique (R-137 : trois candidats, relu, vérifié et final ; générateur
# r4, contrôles v7 ; CM-03 éprouvé par un banc). v4 : après la vérification des corrections (R-136 : VC-04 empreintes brute et normalisée du
# candidat vérifié liées, candidat relu comparé à son épingle ; VC-06 scripts égaux à leurs copies versées).
# Prérequis, committés et poussés : copies versées des scripts sous docs/procedures/revalidation-T0.5-v2/ (épingles
# remplies) ; candidats sous brouillons/ ; rapports scellés ; ligne du GO dans registres/go.md (8 colonnes, type
# « revendication », accordé par Lazar, cite N-018) ; N-018 tranché (option (a), ce GO) ; R-135, R-136 et la ligne R-…
# qui consigne le GO. Le texte est régénéré par remplir_revalidation_v2_r4.py en mode reel (qui refait toutes ces
# vérifications) ; son empreinte normalisée doit égaler l'épingle. Un seul commit S, poussé. Aucune instance créée.
# Usage : sceller_revalidation_v5.sh GO_ID REGISTRE_DU_GO
set -euo pipefail
GO=${1:?GO de Lazar sur N-018}; REG=${2:?ligne R-… qui consigne le GO}
H=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/revalidation-v2
DEPOT=/home/user/controle-ia-travail
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
CODE=6ec7434119781a3abebac789174101b9ed6ae087
P=prereg/T0.5-revalidation-equivalence-pilote-v2.md
CTL=$H/controles_avant_depense_v7.sh
epingle() { sed -n "s/^$1=\"\{0,1\}\([^\"#]*\)\"\{0,1\}.*/\1/p" "$CTL" | sed 's/[[:space:]]*$//'; }
RELU=$(epingle CANDIDAT_RELU_CHEMIN); VERIFIE=$(epingle CANDIDAT_VERIFIE_CHEMIN); FINAL=$(epingle CANDIDAT_FINAL_CHEMIN)
NORMALISE=$(epingle CANDIDAT_NORMALISE)
[[ "$(epingle CANDIDAT_FINAL)" =~ ^[0-9a-f]{64}$ && "$NORMALISE" =~ ^[0-9a-f]{64}$ && "$FINAL" == brouillons/* ]] \
    || { echo "épingles du candidat final absentes des contrôles v7"; exit 2; }
cd "$DEPOT"
git fetch -q origin main
[ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] || { echo "HEAD ≠ origin/main : pousser d'abord les préalables"; exit 2; }
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "arbre suivi non propre"; exit 2; }
[ -e "$P" ] && { echo "$P existe déjà (R12)"; exit 2; }
for s in remplir_revalidation_v2_r4.py controles_avant_depense_v7.sh lancer_revalidation_v7.sh sceller_revalidation_v5.sh recuperation_revalidation_v2.sh; do
    cmp -s "$H/$s" "docs/procedures/revalidation-T0.5-v2/$s" || { echo "$s du bloc-notes ≠ copie versée (VC-06)"; exit 2; }
done
[ "$(sha256sum "$RELU" | cut -d' ' -f1)" = "$(epingle CANDIDAT_RELU)" ] || { echo "candidat relu ≠ épingle (VC-04)"; exit 2; }
[ "$(sha256sum "$VERIFIE" | cut -d' ' -f1)" = "$(epingle CANDIDAT_VERIFIE)" ] || { echo "candidat vérifié ≠ épingle"; exit 2; }
[ "$(sha256sum "$FINAL" | cut -d' ' -f1)" = "$(epingle CANDIDAT_FINAL)" ] || { echo "candidat final ≠ épingle brute"; exit 2; }
normaliser() { sed -E '3s/[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}/AAAA-MM-JJ HH:MM/; 8s/[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}/AAAA-MM-JJ HH:MM/' "$1" \
    | sed -E 's/^(- Version 2 \(N-018\) : .*) Pièces : .*$/\1 Pièces : (remplies au scellement)./' | sha256sum | cut -d' ' -f1; }
[ "$(normaliser "$FINAL")" = "$NORMALISE" ] || { echo "candidat final : empreinte normalisée ≠ épingle (VC-04)"; exit 2; }
SORTIE=$(mktemp -d "$H/scellement-XXXX")/T0.5-revalidation-equivalence-pilote-v2.md
"$PY" -I "$H/remplir_revalidation_v2_r4.py" . "$CODE" reel "$(date -u '+%Y-%m-%d %H:%M UTC')" "$SORTIE" --controles "$CTL" \
    --candidat-relu "$RELU" --candidat-verifie "$VERIFIE" --candidat-final "$FINAL" --go "$GO" --registre "$REG"
[ "$(normaliser "$SORTIE")" = "$NORMALISE" ] || { echo "v2 régénérée ≠ candidat final"; exit 2; }
cp "$SORTIE" "$P"
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import sceller_prereg; sceller_prereg('$P')"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . | tail -1
SHA=$(cut -d' ' -f1 "$P.sha256")
git add "$P" "$P.sha256"
git commit -q -F - <<EOF
T0.5 : revalidation courte de l'équivalence, préenregistrement v2 scellé (N-018, $GO)

Préenregistrement $SHA ; commit du code cité $CODE (seul le test M-1 change depuis la v1 dans l'arbre gelé) ;
670 tests attendus ; PREREG et BRANCHE passés à l'instance (calcul/t05-revalidation-reel-v2). Empreinte normalisée
égale au candidat final ($NORMALISE).

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01W5L3BRJg9Vso4Gru9tWAzM
EOF
git rev-parse HEAD
timeout 600 git push -q origin HEAD:main
git ls-remote origin refs/heads/main
