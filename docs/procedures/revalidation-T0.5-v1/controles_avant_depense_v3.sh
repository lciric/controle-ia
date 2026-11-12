#!/usr/bin/env bash
# Contrôles avant dépense de la revalidation (T0.5), v3 (vérification 3 du remplissage, N-2, N-7 ; vérification 4,
# Q-5 à Q-7), sur un clone neuf du dépôt de travail au commit de scellement S. Aucun calcul payant. Code de sortie 0 si
# et seulement si tout est conforme. Le candidat vérifié est épinglé par son empreinte, heure du scellement normalisée.
# Usage : controles_avant_depense_v3.sh S DOSSIER_NEUF
set -uo pipefail
S=$1; D=$2
CANDIDAT_NORMALISE=1977387f2792aacd93be7802e0e5e94cca635f3274bd9aaaab2dcc2c1bbf6bbe   # candidat-6, vérifié
ARCHIVE_V5=903164d44083c21690fc1757fa227ca58bc95ca3cac4b879e2caf624ec5c3178           # durée des tests citée
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/T0.5-revalidation-equivalence-pilote-v1.md; CFG=prereg/T0.5-revalidation-config-v1.json
RUN=donnees/20261007-082440-t05-extraction
echec=0; ok() { echo "OK  $*"; }; ko() { echo "KO  $*"; echec=1; }
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "S invalide"; exit 2; }
[ -e "$D" ] && { echo "$D existe déjà"; exit 2; }
git clone -q https://github.com/lciric/controle-ia-travail.git "$D" || { echo "clonage impossible"; exit 2; }
cd "$D" && git checkout -q "$S" || { echo "commit $S introuvable"; exit 2; }
[ "$(git log --diff-filter=A -1 --format=%H -- "$P.sha256")" = "$S" ] && ok "S ajoute le sceau du préenregistrement" || ko "S n'est pas le commit qui ajoute $P.sha256"
# commit du code : lu dans le préenregistrement de S (N-2), ancêtre de S
CODE=$(sed -n "s/.*Commit du code d'analyse : \`\([0-9a-f]\{40\}\)\`.*/\1/p" "$P" | head -1)
if [[ "$CODE" =~ ^[0-9a-f]{40}$ ]] && git merge-base --is-ancestor "$CODE" "$S"; then ok "commit du code cité $CODE, ancêtre de S"
else ko "commit du code cité illisible ou non ancêtre de S"; CODE=$S; fi
for f in scripts/amorce_instance_t05.sh scripts/pilote_t05_instance.sh; do
    e=$(git show "$S:$f" | sha256sum | cut -d' ' -f1)
    grep -qF "\`$f\` (\`$e\`, sha256)" "$P" && ok "empreinte de $f citée ($e)" || ko "empreinte de $f ($e) non citée"
done
git diff --quiet "$CODE" "$S" -- . ':(exclude)prereg' ':(exclude)brouillons' ':(exclude)registres' ':(exclude)docs' \
    ':(exclude)diag' ':(exclude)runs' ':(exclude)donnees' ':(exclude)livrables' ':(exclude)papiers' ':(exclude)traces' \
    ':(exclude)CLAUDE.md'; c=$?
case $c in 0) ok "arbre gelé identique au commit du code" ;; 1) ko "arbre gelé modifié depuis le commit du code" ;;
           *) ko "comparaison de l'arbre gelé impossible (code $c)" ;; esac
for f in "$CFG" "$RUN/taches-entrainement.json" "$RUN/taches-evaluation.json"; do
    if git cat-file -e "$S:$f" && git cat-file -e "$S:$f.sha256" && \
       [ "$(git show "$S:$f.sha256")" = "$(git show "$S:$f" | sha256sum | cut -d' ' -f1)  $(basename "$f")" ]; then
        ok "$f et son sceau entier dans l'arbre de S"
    else ko "$f ou son sceau absent ou non conforme"; fi
done
# rapports cités par l'entrée de contre-lecture : présents dans S, empreintes égales (N-7 a)
n=0
while read -r nom sha; do
    n=$((n+1)); f="prereg/contre-lectures/$nom"
    if git cat-file -e "$S:$f" && [ "$(git show "$S:$f" | sha256sum | cut -d' ' -f1)" = "$sha" ]; then ok "rapport cité $nom présent, empreinte conforme"
    else ko "rapport cité $nom absent de S ou d'empreinte différente"; fi
done < <(grep -o '`T0\.5-revalidation-verification-remplissage-[0-9]-v1\.md` (`[0-9a-f]\{64\}`)' "$P" | sed 's/`\([^`]*\)` (`\([0-9a-f]*\)`)/\1 \2/')
[ "$n" = 3 ] && ok "trois rapports de vérification cités" || ko "$n rapport(s) de vérification cité(s) au lieu de 3"
# préenregistrement de S = candidat vérifié, à l'heure du scellement près (lignes 3 et 6 normalisées ; Q-5)
if [ -f "$P" ]; then
    n=$(sed -E '3s/2026-10-1[0-9] [0-9]{2}:[0-9]{2}/AAAA-MM-JJ HH:MM/; 6s/2026-10-1[0-9] [0-9]{2}:[0-9]{2}/AAAA-MM-JJ HH:MM/' "$P" | sha256sum | cut -d' ' -f1)
    [ "$n" = "$CANDIDAT_NORMALISE" ] && ok "préenregistrement de S = candidat vérifié, heure du scellement exceptée" || ko "préenregistrement de S ≠ candidat vérifié ($n)"
else ko "préenregistrement absent de S"; fi
# archives des répétitions jouet : présentes, scellées ; v5 à l'empreinte attendue, chemin cité présent (Q-6)
for v in v4 v5; do
    f=prereg/contre-lectures/T0.5-revalidation-repetition-jouet-$v.tar
    if git cat-file -e "$S:$f" && [ "$(git show "$S:$f.sha256")" = "$(git show "$S:$f" | sha256sum | cut -d' ' -f1)  $(basename "$f")" ]; then
        ok "archive $v présente et scellée"
    else ko "archive $v absente ou sceau non conforme"; fi
done
[ "$(git show "$S:prereg/contre-lectures/T0.5-revalidation-repetition-jouet-v5.tar" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$ARCHIVE_V5" ] \
    && grep -qF "archive \`prereg/contre-lectures/T0.5-revalidation-repetition-jouet-v5.tar\`" "$P" \
    && ok "archive v5 à l'empreinte attendue, citée" || ko "archive v5 : empreinte ou citation"
git ls-remote --exit-code origin refs/heads/calcul/t05-revalidation-reel-v1 >/dev/null 2>&1; c=$?
[ "$c" = 2 ] && ok "branche calcul/t05-revalidation-reel-v1 absente" || ko "branche de résultats : code $c (2 attendu)"
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import problemes; p = problemes('$P'); print(p); raise SystemExit(1 if p else 0)" \
    && ok "problemes() vide" || ko "problemes() non vide"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier "$P" "$CFG" "$RUN/taches-entrainement.json" "$RUN/taches-evaluation.json" >/dev/null \
    && ok "sceaux du préenregistrement, de la configuration et des tâches" || ko "sceaux"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . | tail -1 | grep -q "arbre intact" && ok "verifier-arbre : arbre intact" || ko "verifier-arbre"
PYTHONPATH=src "$PY" - "$P" "$CFG" "$RUN" <<'EOF' && ok "gardes du lanceur rejouées (configuration, citations, code cité, code importé)" || ko "gardes du lanceur"
import json, sys
from pathlib import Path
from controle_ia.environnements import revalider_pilote_a as rv
from controle_ia.harnais.validation_reelle import exiger_code_cite, exiger_code_importe_sous
from controle_ia.scellement import verifier
p, cfg, run = sys.argv[1:4]
verifier(cfg)
c = json.loads(Path(cfg).read_text(encoding="utf-8"))
rv.exiger_config_revalidation(c)
if c["mode"] != "reel":
    raise SystemExit("configuration hors mode reel")
e = rv.exiger_citations(Path(p), c, rv._sha_fichier(f"{run}/taches-entrainement.json"), rv._sha_fichier(f"{run}/taches-evaluation.json"))
print("commit cité :", exiger_code_cite(Path("."), Path(p)), "; entropie citée :", e)
exiger_code_importe_sous(Path("."))
EOF
PYTHONPATH=src "$PY" -m pytest --collect-only -q -p no:cacheprovider > "$D/../collecte-$$.txt" 2>&1; cc=$?
n=$(sed -n 's/^\([0-9]*\) tests\{0,1\} collected in .*/\1/p' "$D/../collecte-$$.txt"); rm -f "$D/../collecte-$$.txt"
a=$(sed -n "s/.*Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$P" | head -1)
[ "$cc" = 0 ] && [ -n "$n" ] && [ "$n" = "$a" ] && ok "tests collectés au commit S : $n = tests attendus (collecte en code 0)" || ko "tests collectés au commit S : $n ≠ $a, ou collecte en code $cc (Q-7)"
echo '{"tool_input":{"command":"GO_ID=GO-2026-10-04-08 vastai create instance 1 --raw"}}' | python3 .claude/hooks/garde_calcul.py \
    && ok "garde de calcul : registres/go.md de S lisible, GO-2026-10-04-08 accepté" || ko "garde de calcul sur le registre de S"
lire() { sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$P" | head -1; }
echo "lecture précoce (script de l'instance) : tests $a ; configuration $(lire "Chemin de la configuration") ; entraînement $(lire "Chemin des tâches d'entraînement") ; évaluation $(lire "Chemin des tâches d'évaluation")"
[ "$echec" = 0 ] && echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"
exit $echec
