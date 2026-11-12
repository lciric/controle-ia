#!/usr/bin/env bash
# Contrôles avant dépense de la revalidation (T0.5), v7 : version 2 du préenregistrement (N-018). v7 : après le contrôle
# mécanique des dernières corrections (R-137 : CM-05 trois candidats, CM-06 commentaires, CM-07 rapports attendus
# complets et bien formés) ; v6 : après la vérification des corrections (R-136 : VC-01 à VC-03, VC-10, VT-09, VT-10) ;
# v5 : après la relecture R2 du candidat 2 (R-135). Sur un clone neuf du dépôt de travail au commit de scellement S ;
# aucun calcul payant ; code 0 si et seulement si tout est conforme ; code 2 si les épingles manquent.
# Épingles écrites ici : candidats relu, vérifié et final (chemins sous brouillons/, empreintes ; le final aussi
# normalisé), rapports attendus (paires nom=empreinte, égales à l'ensemble des rapports de la v2 présents à S),
# lignes de corrections. Normalisation : première date « AAAA-MM-JJ HH:MM » des lignes 3 et 8, et fin « Pièces : … » de
# l'unique entrée « - Version 2 (N-018) : », qui suit immédiatement la dernière entrée de l'historique de la v1. La fin
# « Pièces » est reconstruite depuis les épingles, le GO et la ligne de registre qu'elle cite, et comparée à l'identique ;
# GO de type « revendication », accordé par Lazar, qui cite N-018, sans révocation ; N-018 tranché sur l'option (a) et
# ce GO ; dates des lignes 3 et 8 égales et à moins de deux heures du commit S ; candidats et pièces citées contre leurs
# sceaux. Aucune valeur n'est lue dans l'environnement : le banc (essais_controles_v7.sh) joue une copie dont seules
# la ligne DEPOT et les épingles du candidat final et des rapports changent.
# Usage : controles_avant_depense_v7.sh S DOSSIER_NEUF
set -uo pipefail
S=$1; D=$2
DEPOT=https://github.com/lciric/controle-ia-travail.git
CANDIDAT_RELU=af09c78b13f4b4dc18c005b216ccc738bc39fd02828242cc8c1f61e64eb38fb8        # candidat 2, relu (R2)
CANDIDAT_RELU_CHEMIN=brouillons/T0.5-revalidation-equivalence-pilote-v2-candidat2.md
CANDIDAT_VERIFIE=f5adb5718304d701e7065c3e80b6212f6c543f7be1a1b0ab15665c4052b1823e     # candidat 3, vérifié (R-136)
CANDIDAT_VERIFIE_CHEMIN=brouillons/T0.5-revalidation-equivalence-pilote-v2-candidat3.md
CANDIDAT_FINAL=e6f19820b61557e6b8309d09629cf2e43ae9479b98d320f0efcff826ea2691d3       # candidat 5, final (R-137)
CANDIDAT_FINAL_CHEMIN=brouillons/T0.5-revalidation-equivalence-pilote-v2-candidat5.md
CANDIDAT_NORMALISE=83a1e3269e523ea6d1b2ea1417a901e8b556e678ad1a7e7d0282ed38ede1aeeb   # candidat 5, normalisé
# rapports attendus : les 17 rapports de la v2 (relecture, vérification, contrôle mécanique, bancs), paires nom=empreinte
RAPPORTS_ATTENDUS="T0.5-revalidation-v2-relecture-chaine-v1.md=c6df0cf3adfdb3cefd72912b0186fbbc4f283f7f02769c99e81e86c14f0532fa T0.5-revalidation-v2-relecture-code-v1.md=a3b7e1648bb26a93853ef431ec83eba8db6c775090e8644fad3f4971a9e4fbf1 T0.5-revalidation-v2-relecture-contre-verifications-v1.md=dd1f63057003b9768fc723f5eb314098ae2707c00ccf18aa3a960d60875425ae T0.5-revalidation-v2-relecture-fichiers-de-travail-v1.tar=aa6c9d5fdc3753c5a3f6ae83e01d760fe6524591cd785bea8955f2b6911b9595 T0.5-revalidation-v2-relecture-resultats-v1.json=801039eced23ffd2fd1537df836db65c92e85344057e416b0fd43369364b065f T0.5-revalidation-v2-relecture-texte-v1.md=2ccecbcdf217e48d027dd0151d5a12dabcac0879bcf4bb0c0168e8bb0c2bb2e4 T0.5-revalidation-v2-verification-banc-controles-final-v1.tar=d6b2de1426a7c22c0afeffde5bdd87a7db4e09b56b95b8b6fd9ff97c54d87c28 T0.5-revalidation-v2-verification-banc-controles-v1.tar=6938752d7432e42d58921343f7168aafa3f15ca155df8154135f11ef39735913 T0.5-revalidation-v2-verification-banc-lanceur-scellement-v1.tar=c3de55e82987d0efd1094a256ad723d7fcc73d9c4e0c11d2b3cab93c19d870e2 T0.5-revalidation-v2-verification-chaine-v1.md=fdef110d4e7a3464ab95d09ab557b91515a50d2a8183b2ea59b1f74b0c2de61c T0.5-revalidation-v2-verification-contre-verifications-v1.md=47bbd7d1dcf37365a150c95fa6eb385dee65322e959e113f157d401faba00a10 T0.5-revalidation-v2-verification-controle-mecanique-fichiers-de-travail-v1.tar=d1d84e96c68dc20ffb69f6f305cc1fd3131654babaec829d9f7ff81c184ea463 T0.5-revalidation-v2-verification-controle-mecanique-resultats-v1.json=c68fb3f94382d04aedc3c41c27b64b6f17a78766e616da74825d64bf1e346ec2 T0.5-revalidation-v2-verification-controle-mecanique-v1.md=26f4fb9a437dc960d918e2e51593114e395d32c1f93d49267c5e463c4beeb25d T0.5-revalidation-v2-verification-fichiers-de-travail-v1.tar=5828afbc49eb32ee416abc1ac8ec4493bcd7f5092c869473dc6ecd7aa4491e99 T0.5-revalidation-v2-verification-resultats-v1.json=8d8d68cfeddd5c430f380a11897367dfb803c1c7ae1c08ddd672e49d1aa0f201 T0.5-revalidation-v2-verification-texte-v1.md=592d1af09ef58d649ee8c6911322f1fe0c9e217ffe683e48fd864af4285cb0b0"
CORRECTIONS="R-135 et R-136 et R-137"
ARCHIVE_V5=903164d44083c21690fc1757fa227ca58bc95ca3cac4b879e2caf624ec5c3178
SUITE=docs/procedures/revalidation-T0.5-v2/suite-6ec7434-environnement-neuf-v1.txt
SUITE_SHA=90d3984fb99ea575d2bf32c3af2d8ac86592cb72da82c6a1bc2f5d7fa70cdac2
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/T0.5-revalidation-equivalence-pilote-v2.md; CFG=prereg/T0.5-revalidation-config-v1.json
P1=prereg/T0.5-revalidation-equivalence-pilote-v1.md; ANCIEN=3b8c049bec316272b4f65a0e51ef54a2c1e83217
BRANCHE=calcul/t05-revalidation-reel-v2
RUN=donnees/20261007-082440-t05-extraction
echec=0; ok() { echo "OK  $*"; }; ko() { echo "KO  $*"; echec=1; }
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "S invalide"; exit 2; }
[ -e "$D" ] && { echo "$D existe déjà"; exit 2; }
for v in "$CANDIDAT_FINAL" "$CANDIDAT_NORMALISE"; do [[ "$v" =~ ^[0-9a-f]{64}$ ]] || { echo "empreinte du candidat final non épinglée"; exit 2; }; done
[[ "$CANDIDAT_FINAL_CHEMIN" == brouillons/* ]] || { echo "chemin du candidat final non épinglé"; exit 2; }
n_paires=0
for paire in $RAPPORTS_ATTENDUS; do [[ "$paire" =~ ^[^=]+=[0-9a-f]{64}$ ]] || { echo "rapports attendus mal formés : $paire (CM-07)"; exit 2; }; n_paires=$((n_paires+1)); done
[ "$n_paires" -ge 1 ] || { echo "liste des rapports attendus vide (CM-07)"; exit 2; }
git clone -q "$DEPOT" "$D" || { echo "clonage impossible"; exit 2; }
cd "$D" && git checkout -q "$S" || { echo "commit $S introuvable"; exit 2; }
[ "$(git log --diff-filter=A -1 --format=%H -- "$P.sha256")" = "$S" ] && ok "S ajoute le sceau du préenregistrement v2" || ko "S n'est pas le commit qui ajoute $P.sha256"
# commit du code : lu dans le préenregistrement de S, ancêtre de S
CODE=$(sed -n "s/.*Commit du code d'analyse : \`\([0-9a-f]\{40\}\)\`.*/\1/p" "$P" | head -1)
if [[ "$CODE" =~ ^[0-9a-f]{40}$ ]] && git merge-base --is-ancestor "$CODE" "$S"; then ok "commit du code cité $CODE, ancêtre de S"
else ko "commit du code cité illisible ou non ancêtre de S"; CODE=$S; fi
for f in scripts/amorce_instance_t05.sh scripts/pilote_t05_instance.sh; do
    e=$(git show "$S:$f" | sha256sum | cut -d' ' -f1)
    grep -qF "\`$f\` (\`$e\`, sha256)" "$P" && ok "empreinte de $f citée ($e)" || ko "empreinte de $f ($e) non citée"
done
GELES=(. ':(exclude)prereg' ':(exclude)brouillons' ':(exclude)registres' ':(exclude)docs' ':(exclude)diag' ':(exclude)runs'
       ':(exclude)donnees' ':(exclude)livrables' ':(exclude)papiers' ':(exclude)traces' ':(exclude)CLAUDE.md')
git diff --quiet "$CODE" "$S" -- "${GELES[@]}"; c=$?
case $c in 0) ok "arbre gelé identique au commit du code" ;; 1) ko "arbre gelé modifié depuis le commit du code" ;;
           *) ko "comparaison de l'arbre gelé impossible (code $c)" ;; esac
git merge-base --is-ancestor "$ANCIEN" "$CODE" && [ "$(git diff --name-only "$ANCIEN" "$CODE" -- "${GELES[@]}")" = "tests/test_validation_reelle.py" ] \
    && ok "code : seul tests/test_validation_reelle.py change depuis le commit de la v1" || ko "code : différentiel depuis la v1 inattendu"
for f in "$CFG" "$RUN/taches-entrainement.json" "$RUN/taches-evaluation.json"; do
    if git cat-file -e "$S:$f" && git cat-file -e "$S:$f.sha256" && \
       [ "$(git show "$S:$f.sha256")" = "$(git show "$S:$f" | sha256sum | cut -d' ' -f1)  $(basename "$f")" ]; then
        ok "$f et son sceau entier dans l'arbre de S"
    else ko "$f ou son sceau absent ou non conforme"; fi
done
# rapports de vérification de la v1, toujours cités par l'historique (trois)
n=0
while read -r nom sha; do
    n=$((n+1)); f="prereg/contre-lectures/$nom"
    if git cat-file -e "$S:$f" && [ "$(git show "$S:$f" | sha256sum | cut -d' ' -f1)" = "$sha" ]; then ok "rapport cité $nom présent, empreinte conforme"
    else ko "rapport cité $nom absent de S ou d'empreinte différente"; fi
done < <(grep -o '`T0\.5-revalidation-verification-remplissage-[0-9]-v1\.md` (`[0-9a-f]\{64\}`)' "$P" | sed 's/`\([^`]*\)` (`\([0-9a-f]*\)`)/\1 \2/')
[ "$n" = 3 ] && ok "trois rapports de vérification de la v1 cités" || ko "$n rapport(s) de vérification de la v1 cité(s) au lieu de 3"
# v1 intacte et citée par son empreinte
e1=$(git show "$S:$P1" | sha256sum | cut -d' ' -f1)
[ "$(git show "$S:$P1.sha256" | cut -d' ' -f1)" = "$e1" ] && grep -qF "(\`$P1\`, \`$e1\`" "$P" \
    && ok "v1 intacte, citée par son empreinte ($e1)" || ko "v1 : sceau ou citation"
# entrée « - Version 2 (N-018) : » : une seule, juste après la dernière entrée de l'historique de la v1
nv=$(grep -c '^- Version 2 (N-018)' "$P")
lc=$(grep -n '^- Contrôle mécanique des corrections du brouillon 6' "$P" | cut -d: -f1)
lv=$(grep -n '^- Version 2 (N-018) : ' "$P" | cut -d: -f1)
[ "$nv" = 1 ] && [ -n "$lc" ] && [ "$lv" = "$((lc + 1))" ] && ok "entrée Version 2 unique, à sa place (ligne $lv)" || ko "entrée Version 2 : $nv ligne(s), place $lv (attendue $((lc + 1)))"
# dates des lignes 3 et 8 : égales, à moins de deux heures du commit S (VC-10)
d3=$(sed -n '3p' "$P" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}' | head -1)
d8=$(sed -n '8p' "$P" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}' | head -1)
ds=$(git log -1 --format=%ct "$S"); dp=$(date -u -d "$d3" +%s 2>/dev/null || echo 0)
[ -n "$d3" ] && [ "$d3" = "$d8" ] && [ "$(( ds > dp ? ds - dp : dp - ds ))" -le 7200 ] && ok "dates des lignes 3 et 8 égales ($d3), à moins de 2 h du commit S" || ko "dates des lignes 3 et 8 ($d3 ; $d8) ou écart au commit S"
# préenregistrement de S = candidat vérifié, normalisé (dates des lignes 3 et 8 ; fin « Pièces » de l'entrée)
n=$(sed -E '3s/[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}/AAAA-MM-JJ HH:MM/; 8s/[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}/AAAA-MM-JJ HH:MM/' "$P" \
    | sed -E 's/^(- Version 2 \(N-018\) : .*) Pièces : .*$/\1 Pièces : (remplies au scellement)./' | sha256sum | cut -d' ' -f1)
[ "$n" = "$CANDIDAT_NORMALISE" ] && ok "préenregistrement de S = candidat final, normalisé ($n)" || ko "préenregistrement de S ≠ candidat final ($n)"
# candidats versés sous brouillons/, scellés, aux empreintes épinglées (VT-09)
for paire in "$CANDIDAT_RELU_CHEMIN=$CANDIDAT_RELU" "$CANDIDAT_VERIFIE_CHEMIN=$CANDIDAT_VERIFIE" "$CANDIDAT_FINAL_CHEMIN=$CANDIDAT_FINAL"; do
    f=${paire%%=*}; e=${paire#*=}
    [ "$(git show "$S:$f" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] && [ "$(git show "$S:$f.sha256" 2>/dev/null)" = "$e  $(basename "$f")" ] \
        && ok "candidat $f versé, scellé, à l'empreinte épinglée" || ko "candidat $f absent, non scellé ou d'empreinte différente"
done
# rapports attendus : présents à S, scellés, aux empreintes épinglées (VC-01)
for paire in $RAPPORTS_ATTENDUS; do
    nom=${paire%%=*}; e=${paire#*=}; f="prereg/contre-lectures/$nom"
    [ "$(git show "$S:$f" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] && [ "$(git show "$S:$f.sha256" 2>/dev/null)" = "$e  $nom" ] \
        && ok "rapport $nom présent, scellé, à l'empreinte épinglée" || ko "rapport $nom absent, non scellé ou d'empreinte différente"
done
# complétude : l'ensemble des rapports de la v2 présents à S égale l'ensemble des rapports attendus (CM-07)
presents=$(git ls-tree -r --name-only "$S" prereg/contre-lectures/ | grep -E '^prereg/contre-lectures/T0\.5-revalidation-v2-(relecture|verification)-[a-z-]+-v1\.(md|json|tar)$' | xargs -n1 basename | sort | tr '\n' ' ')
attendus=$(for paire in $RAPPORTS_ATTENDUS; do echo "${paire%%=*}"; done | sort | tr '\n' ' ')
[ "$presents" = "$attendus" ] && ok "rapports de la v2 présents à S = rapports attendus ($n_paires)" || ko "rapports de la v2 présents à S « $presents » ≠ attendus « $attendus »"
# fin « Pièces » : reconstruite depuis les épingles, le GO et la ligne de registre qu'elle cite ; égalité exacte (VC-02)
PIECES=$(sed -n 's/^- Version 2 (N-018) : .* Pièces : \(.*\)$/\1/p' "$P")
GO=$(sed -n 's/.* ; décision de Lazar : \(GO-[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}-[0-9]\{2\}\) (R-[0-9]\{1,4\})\.$/\1/p' <<<"$PIECES")
REG=$(sed -n 's/.* ; décision de Lazar : GO-[0-9-]* (\(R-[0-9]\{1,4\}\))\.$/\1/p' <<<"$PIECES")
attendu="candidat relu \`$CANDIDAT_RELU_CHEMIN\` (\`$CANDIDAT_RELU\`) ; candidat vérifié \`$CANDIDAT_VERIFIE_CHEMIN\` (\`$CANDIDAT_VERIFIE\`) ; candidat final, contrôlé après les dernières corrections \`$CANDIDAT_FINAL_CHEMIN\` (\`$CANDIDAT_FINAL\`)"
for paire in $RAPPORTS_ATTENDUS; do attendu="$attendu ; \`${paire%%=*}\` (\`${paire#*=}\`)"; done
attendu="$attendu ; corrections : $CORRECTIONS ; décision de Lazar : $GO ($REG)."
[ -n "$GO" ] && [ -n "$REG" ] && [ "$PIECES" = "$attendu" ] && ok "fin « Pièces » = reconstruction exacte ($GO, $REG)" || ko "fin « Pièces » différente de la reconstruction (GO « $GO », registre « $REG »)"
# GO : une ligne, 8 colonnes, type revendication, accordé par Lazar, cite N-018, sans révocation (VC-03)
lgo=$(grep "^| $GO |" registres/go.md)
python3 - "$GO" "$lgo" <<'PYEOF' && ok "GO $GO : revendication, accordé par Lazar, cite N-018" || ko "GO $GO : ligne absente, en double, mal formée, d'un autre type ou sans N-018"
import sys
go, l = sys.argv[1], sys.argv[2]
ls = [x for x in l.split("\n") if x.strip()]
c = [x.strip() for x in ls[0].strip().strip("|").split("|")] if len(ls) == 1 else []
sys.exit(0 if len(c) == 8 and c[0] == go and c[2] == "revendication" and c[6] == "Lazar" and "N-018" in c[3] else 1)
PYEOF
! grep '^| GO-' registres/go.md | grep 'révocation' | grep -qF "$GO" && ok "GO $GO non révoqué" || ko "GO $GO révoqué"
l18=$(grep '^| N-018 |' registres/decisions.md)
etat18=$(awk -F'|' '{print $(NF-1)}' <<<"$l18")
[ "$(grep -c '^| N-018 |' registres/decisions.md)" = 1 ] && grep -qF "$GO" <<<"$etat18" && grep -qF "(a)" <<<"$etat18" && ! grep -q 'en attente' <<<"$etat18" \
    && ok "N-018 tranché : option (a), $GO" || ko "N-018 absent, en attente, ou état sans l'option (a) et ce GO"
lreg=$(grep "^| $REG |" registres/decisions.md)
[ -n "$REG" ] && [ "$(grep -c "^| $REG |" registres/decisions.md)" = 1 ] && grep -qF "$GO" <<<"$lreg" && ok "$REG consigne $GO" || ko "ligne $REG absente, en double ou sans $GO"
for r in ${CORRECTIONS// et / }; do grep -q "^| $r |" registres/decisions.md && ok "$r (corrections) consigné" || ko "$r absent"; done
# pièces citées par le texte : conformes à leurs sceaux (VT-10)
for f in traces/t05-instance-55292763-processeur-20261011/processeur.json traces/t05-20261010-223801-JOkW/tests.txt \
         traces/t05-instance-55292763-20261010-224000/journal-instance.txt; do
    e=$(git show "$S:$f" | sha256sum | cut -d' ' -f1)
    git show "$S:$(dirname "$f")/empreintes.sha256" | grep -qx "$e  $(basename "$f")" && grep -qF "\`$e\`" "$P" \
        && ok "pièce $f scellée et citée" || ko "pièce $f : sceau ou citation"
done
f=prereg/contre-lectures/T0.5-revalidation-v2-repetition-jouet-v3-passage4-interrompu-v1.tar; e=$(git show "$S:$f" | sha256sum | cut -d' ' -f1)
[ "$(git show "$S:$f.sha256")" = "$e  $(basename "$f")" ] && grep -qF "\`$f\`, \`$e\`" "$P" && ok "répétition jouet v3 scellée et citée" || ko "répétition jouet v3 : sceau ou citation"
# sortie de la suite au commit cité : versée, scellée, à l'empreinte attendue, citée
[ "$(git show "$S:$SUITE" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$SUITE_SHA" ] && [ "$(git show "$S:$SUITE.sha256")" = "$SUITE_SHA  $(basename "$SUITE")" ] \
    && grep -qF "\`$SUITE\` (\`$SUITE_SHA\`)" "$P" && ok "sortie de la suite versée, scellée, citée" || ko "sortie de la suite : empreinte, sceau ou citation"
# archives des répétitions jouet de la v1 : présentes, scellées ; v5 à l'empreinte attendue, citée
for v in v4 v5; do
    f=prereg/contre-lectures/T0.5-revalidation-repetition-jouet-$v.tar
    if git cat-file -e "$S:$f" && [ "$(git show "$S:$f.sha256")" = "$(git show "$S:$f" | sha256sum | cut -d' ' -f1)  $(basename "$f")" ]; then
        ok "archive $v présente et scellée"
    else ko "archive $v absente ou sceau non conforme"; fi
done
[ "$(git show "$S:prereg/contre-lectures/T0.5-revalidation-repetition-jouet-v5.tar" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$ARCHIVE_V5" ] \
    && grep -qF "archive \`prereg/contre-lectures/T0.5-revalidation-repetition-jouet-v5.tar\`" "$P" \
    && ok "archive v5 à l'empreinte attendue, citée" || ko "archive v5 : empreinte ou citation"
git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>&1; c=$?
[ "$c" = 2 ] && ok "branche $BRANCHE absente" || ko "branche de résultats $BRANCHE : code $c (2 attendu)"
grep -qF "\`PREREG=$P\`, \`BRANCHE=$BRANCHE\`" "$P" && ok "PREREG et BRANCHE cités par la v2 (ligne 3) = constantes" || ko "PREREG ou BRANCHE : la v2 cite autre chose"
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import problemes; p = problemes('$P'); print(p); raise SystemExit(1 if p else 0)" \
    && ok "problemes() vide" || ko "problemes() non vide"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier "$P" "$P1" "$CFG" "$RUN/taches-entrainement.json" "$RUN/taches-evaluation.json" >/dev/null \
    && ok "sceaux de la v2, de la v1, de la configuration et des tâches" || ko "sceaux"
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
[ "$cc" = 0 ] && [ -n "$n" ] && [ "$n" = "$a" ] && ok "tests collectés au commit S : $n = tests attendus (collecte en code 0)" || ko "tests collectés au commit S : $n ≠ $a, ou collecte en code $cc"
echo '{"tool_input":{"command":"GO_ID=GO-2026-10-04-08 vastai create instance 1 --raw"}}' | python3 .claude/hooks/garde_calcul.py \
    && ok "garde de calcul : registres/go.md de S lisible, GO-2026-10-04-08 accepté" || ko "garde de calcul sur le registre de S"
lire() { sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$P" | head -1; }
echo "lecture précoce (script de l'instance, PREREG=$P) : tests $a ; configuration $(lire "Chemin de la configuration") ; entraînement $(lire "Chemin des tâches d'entraînement") ; évaluation $(lire "Chemin des tâches d'évaluation")"
[ "$echec" = 0 ] && echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"
exit $echec
