#!/usr/bin/env bash
# Scellement de la revalidation (T0.5) : un seul commit S (préenregistrement, configuration, rapports de vérification,
# archives des répétitions, registres), poussé vers le dépôt de travail. Plan de lancement v3, étape 1.
# Usage : sceller_revalidation_v2.sh (candidat vérifié : candidat-6, épinglé par son empreinte normalisée)
set -euo pipefail
B=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation
DEPOT=/home/user/controle-ia-travail
CODE=3b8c049bec316272b4f65a0e51ef54a2c1e83217
PY=$B/venv-gpu-neuf/bin/python
cd "$DEPOT"
[ "$(git rev-parse HEAD)" = "$CODE" ] || { echo "HEAD ≠ commit du code"; exit 2; }
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "arbre suivi non propre"; exit 2; }
P=prereg/T0.5-revalidation-equivalence-pilote-v1.md; CFG=prereg/T0.5-revalidation-config-v1.json; CL=prereg/contre-lectures
for f in "$P" "$CFG"; do [ -e "$f" ] && { echo "$f existe déjà (R12)"; exit 2; }; done
# rapports et archives, copiés octet pour octet, scellés
for f in T0.5-revalidation-verification-remplissage-1-v1.md T0.5-revalidation-verification-remplissage-1-v1.json \
         T0.5-revalidation-verification-remplissage-2-v1.md T0.5-revalidation-verification-remplissage-2-v1.json \
         T0.5-revalidation-verification-remplissage-3-v1.md T0.5-revalidation-verification-remplissage-3-v1.json \
         T0.5-revalidation-verification-remplissage-4-v1.md T0.5-revalidation-verification-remplissage-4-v1.json \
         T0.5-revalidation-repetition-jouet-v4.tar T0.5-revalidation-repetition-jouet-v5.tar; do
    [ -e "$CL/$f" ] && { echo "$CL/$f existe déjà (R12)"; exit 2; }
    cp "$B/rapports/$f" "$CL/$f"
    PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$CL/$f" > /dev/null
done
DATE=$(date -u '+%Y-%m-%d %H:%M UTC')
"$PY" -I "$B/remplir_revalidation_v4.py" . "$CODE" "$B/entropie-revalidation.txt" reel "$DATE" \
    "$CL/T0.5-revalidation-repetition-jouet-v5.tar" racine-1-sain/t05/tests.txt "$P" "$CFG" \
    "$B/candidat-4/T0.5-revalidation-equivalence-pilote-v1.md" \
    "$CL/T0.5-revalidation-verification-remplissage-1-v1.md" "$CL/T0.5-revalidation-verification-remplissage-2-v1.md" \
    "$CL/T0.5-revalidation-verification-remplissage-3-v1.md" > /dev/null
n=$(sed -E '3s/2026-10-1[0-9] [0-9]{2}:[0-9]{2}/AAAA-MM-JJ HH:MM/; 6s/2026-10-1[0-9] [0-9]{2}:[0-9]{2}/AAAA-MM-JJ HH:MM/' "$P" | sha256sum | cut -d' ' -f1)
[ "$n" = 1977387f2792aacd93be7802e0e5e94cca635f3274bd9aaaab2dcc2c1bbf6bbe ] || { echo "préenregistrement ≠ candidat vérifié (empreinte normalisée $n)"; exit 2; }
cmp -s "$B/candidat-6/T0.5-revalidation-config-v1.json" "$CFG" || { echo "configuration ≠ candidat vérifié"; exit 2; }
PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$CFG" > /dev/null
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import sceller_prereg; sceller_prereg('$P')"
SHA_P=$(cut -d' ' -f1 "$P.sha256"); SHA_C=$(cut -d' ' -f1 "$CFG.sha256")
python3 -I "$B/registres_scellement_v2.py" . "$DATE" "$SHA_P" "$SHA_C"
python3 -I "$B/etat_scellement.py" . "$DATE" "$SHA_P"
[ "$(git diff --name-only -- registres | sort | tr '\n' ' ')" = "registres/decisions.md registres/etat.md " ] || { echo "registres : changements inattendus"; exit 2; }
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . | tail -1
git add "$P" "$P.sha256" "$CFG" "$CFG.sha256" "$CL"/T0.5-revalidation-verification-remplissage-* \
    "$CL"/T0.5-revalidation-repetition-jouet-v4.tar* "$CL"/T0.5-revalidation-repetition-jouet-v5.tar* \
    registres/decisions.md registres/etat.md
git commit -q -F - <<EOF
T0.5 : revalidation courte de l'équivalence scellée (préenregistrement v1, configuration v1) ; vérifications du remplissage et répétitions jouet versées ; R-127 à R-129

Préenregistrement $SHA_P ; configuration $SHA_C (empreinte canonique 50930b37…) ; commit du code cité
$CODE ; 670 tests attendus. Lancement subordonné au crédit Vast.ai (au moins 6 h au prix de l'offre retenue,
plus 0,9 USD).

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01W5L3BRJg9Vso4Gru9tWAzM
EOF
git rev-parse HEAD
timeout 600 git push -q origin HEAD:main
git ls-remote origin refs/heads/main
