#!/usr/bin/env bash
# Lanceur des courses réelles de l'étape 1 du programme « gradient conçu par l'essaim » (préenregistrement
# `prereg/gradient-etape1-sondes-v2.md`, scellé ; GO-2026-10-24-05). Écrit par la lignée « session-depot » le
# 24 octobre 2026. Une course par appel :
#   repetition      répétition mécanique (Plan d'analyse, point 8) : une lignée CLAUDE_OPUS_5_5, une génération,
#                   20 appels, 2 USD, 900 s, 2 entraînements ; exclue de toute analyse ; statuts seulement ;
#   A1, A2          bras avec gradient, réplique 1 ou 2 (point 3) ;
#   B1, B2          bras sans gradient, `--depuis` la course A de même réplique (point 3).
# Contrôles avant tout appel payant (code 2 si l'un échoue) : préenregistrement scellé et conforme (validateur du dépôt) ;
# commit du code = commit cité ; arbre de travail propre ; banque, traits, lignées imposées aux empreintes citées ; GO de
# calcul accepté par la garde ; clés présentes (jamais affichées) ; dossier de sortie neuf (R12) ; course A terminée pour
# un bras B. Codes : 0 course finie ; 2 arrêt avant la course ; autre : code de sortie du noyau.
# Usage : lancer_courses_etape1_v1.sh COURSE DOSSIER_DES_COURSES
set -euo pipefail
[ $# -eq 2 ] || { echo "usage : lancer_courses_etape1_v1.sh {repetition|A1|A2|B1|B2} DOSSIER_DES_COURSES"; exit 2; }
COURSE=$1; RACINE=$(realpath -m "$2")
DEPOT=/home/user/controle-ia-travail
CODE=${CODE_ETAPE1:?CODE_ETAPE1 : dossier de travail git de outils/essaim-m3-gradient-v2-travail}
VENV=/opt/essaim-m3-venv-v1
PREREG=prereg/gradient-etape1-sondes-v3.md
COMMIT=${COMMIT_ETAPE1:?COMMIT_ETAPE1 : commit cité par le préenregistrement scellé}
GO=GO-2026-10-24-05
E_BANQUE=f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc
E_TRAITS=add13e090a13b60e48983393ae376cc9df2542210b5328bc2abd94e661e25f17
E_ORG_GEMINI=3e6fe2e96d6133ab0bfae39009133897d335966d25e5dd48832d6a5d88dc6ba7
E_ORG_ENVELOPPE=bceb133262e623212cff6151e33867b02899c652be36394845ec55b0279fae20
case "$COURSE" in repetition|A1|A2|B1|B2) ;; *) echo "course inconnue : $COURSE"; exit 2 ;; esac
mkdir -p "$RACINE"
J="$RACINE/lancements.txt"
note() { printf '%s %s : %s\n' "$(date -u +%FT%TZ)" "$COURSE" "$*" | tee -a "$J"; }
# 1. préenregistrement scellé et conforme
(cd "$DEPOT" && PYTHONPATH=src "$DEPOT/.venv/bin/python" -I -B -c '
import sys
sys.path.insert(0, "src")
from controle_ia import prereg
print(prereg.exiger_prereg_scelle(sys.argv[1]))' "$PREREG") > "$RACINE/.prereg-$COURSE.txt" 2>&1 \
    || { note "préenregistrement non scellé ou non conforme : $(tail -1 "$RACINE/.prereg-$COURSE.txt")"; exit 2; }
grep -qF "$COMMIT" "$DEPOT/$PREREG" || { note "le préenregistrement ne cite pas le commit $COMMIT"; exit 2; }
note "préenregistrement scellé $(head -c 16 "$RACINE/.prereg-$COURSE.txt")…"
# 2. code au commit cité, arbre propre
[ "$(git -C "$CODE" rev-parse HEAD)" = "$COMMIT" ] || { note "code : HEAD $(git -C "$CODE" rev-parse HEAD) ≠ $COMMIT"; exit 2; }
[ -z "$(git -C "$CODE" status --porcelain --untracked-files=no)" ] || { note "code : arbre de travail modifié"; exit 2; }
# 3. entrées aux empreintes citées (extraites une fois dans RACINE/entrees, jamais réécrites)
EN="$RACINE/entrees"
if [ ! -e "$EN/pret" ]; then
    rm -rf "$EN"; mkdir -p "$EN/traits" "$EN/lignees/gemini-organisme-v3" "$EN/lignees/enveloppe-essaim-gemini-v3"
    git -C "$DEPOT" show bffe03c:essaim-m3-refonte-v1/banque/banque-confrontation-v1.json > "$EN/banque-confrontation-v1.json"
    git -C "$DEPOT" show bffe03c:essaim-m3-refonte-v1/banque/banque-confrontation-v1.json.sha256 > "$EN/banque-confrontation-v1.json.sha256"
    git -C "$DEPOT" archive 6479769 essaim-m3-refonte-v1/traits/etape1-v1 | tar -x -C "$EN/traits" --strip-components=3
    git -C "$DEPOT" archive 320cd34 outils/gemini-organisme-v3/organisme | tar -x -C "$EN/lignees/gemini-organisme-v3" --strip-components=2
    git -C "$DEPOT" archive 233fde6 outils/essaim-m3-debogage-v3/organisme | tar -x -C "$EN/lignees/enveloppe-essaim-gemini-v3" --strip-components=2
    touch "$EN/pret"
fi
[ "$(sha256sum "$EN/banque-confrontation-v1.json" | cut -d' ' -f1)" = "$E_BANQUE" ] || { note "banque : empreinte différente"; exit 2; }
[ "$(sha256sum "$EN/traits/etape1-v1/EMPREINTES-traits-etape1-v1.txt" | cut -d' ' -f1)" = "$E_TRAITS" ] || { note "traits : empreintes différentes"; exit 2; }
(cd "$EN/traits/etape1-v1" && sha256sum -c --quiet EMPREINTES-traits-etape1-v1.txt) || { note "traits : un fichier diffère de ses empreintes"; exit 2; }
arbres=$(cd "$CODE/essaim-m3-refonte-v1" && env -i PATH=/usr/bin:/bin HOME=/tmp "$VENV/bin/python" -B -c '
import pathlib, sys
from essaim_m3.noyau.boucle import empreinte_arbre
print(" ".join(empreinte_arbre(pathlib.Path(p)) for p in sys.argv[1:]))' "$EN/lignees/gemini-organisme-v3/organisme" "$EN/lignees/enveloppe-essaim-gemini-v3/organisme")
[ "$arbres" = "$E_ORG_GEMINI $E_ORG_ENVELOPPE" ] || { note "lignées imposées : empreintes d'arbre différentes ($arbres)"; exit 2; }
cp "$DEPOT/registres/go.md" "$RACINE/registre-go-$COURSE.md"
# 4. garde de calcul rejouée avec le GO ; clés présentes, jamais affichées
printf '{"tool_input":{"command":"GO_ID=%s vastai create instance 0"}}' "$GO" | python3 "$DEPOT/.claude/hooks/garde_calcul.py" \
    || { note "garde de calcul : $GO refusé"; exit 2; }
[ -n "${RR_ANTHROPIC_API_KEY:-}" ] && [ -n "${RR_ANTHROPIC_WORKSPACE_ID:-}" ] && [ -n "${GEMINI_API_KEY:-}" ] \
    || { note "clé absente (RR_ANTHROPIC_API_KEY, RR_ANTHROPIC_WORKSPACE_ID ou GEMINI_API_KEY)"; exit 2; }
# 5. paramètres de la course (Plan d'analyse, points 3, 4, 5, 8)
SORTIE="$RACINE/$COURSE"
[ -e "$SORTIE" ] && { note "$SORTIE existe déjà (R12)"; exit 2; }
COMMUNS=(--reel --go "$GO" --registre-go "$RACINE/registre-go-$COURSE.md" --taches "$EN/banque-confrontation-v1.json"
         --traits "$EN/traits/etape1-v1/traits-16384" --sortie "$SORTIE" --isoler-reseau --parallele-max 8 --relances-max 1
         --pas-max 5000 --delai-entrainement 120 --recherches-max 30 --telechargements-max 20 --octets-max 40000000)
IMPOSES=(--organisme-impose "gemini-organisme-v3=$EN/lignees/gemini-organisme-v3/organisme@gemini"
         --organisme-impose "enveloppe-essaim-gemini-v3=$EN/lignees/enveloppe-essaim-gemini-v3/organisme@gemini")
graine() {  # graine_r inscrite au scellement dans la section « Contre-lecture » (entrée 2) : « graine_1 = <entier> »
    grep -oE "graine_$1 = [0-9]+" "$DEPOT/$PREREG" | head -1 | grep -oE "[0-9]+$"
}
case "$COURSE" in
    repetition)
        ARGS=("${COMMUNS[@]}" --generations 1 --graine 1 --especes CLAUDE_OPUS_5_5 --appels-max 20 --usd-par-generation 3
              --temps-max 900 --entrainements-max 2 --rondes-conception-max 2 --usd-max-conception 2 --appels-max-conception 20
              --plafond-total 10) ;;
    A1|A2)
        r=${COURSE#A}; g=$(graine "$r"); [[ "$g" =~ ^[0-9]+$ ]] || { note "graine_$r absente du préenregistrement"; exit 2; }
        ARGS=("${COMMUNS[@]}" "${IMPOSES[@]}" --generations 3 --graine "$g" --appels-max 160 --usd-par-generation 37
              --temps-max 2400 --entrainements-max 10 --rondes-conception-max 8 --usd-max-conception 10
              --appels-max-conception 160 --plafond-total 1066) ;;
    B1|B2)
        r=${COURSE#B}; g=$(graine "$r"); [[ "$g" =~ ^[0-9]+$ ]] || { note "graine_$r absente du préenregistrement"; exit 2; }
        ORIGINE="$RACINE/A$r"
        [ -f "$ORIGINE/manifeste-run.json" ] && grep -q "\"fin_utc\"" "$ORIGINE/rapport-fin.json" 2>/dev/null \
            || { note "course A$r absente ou non terminée : le bras B$r attend"; exit 2; }
        ARGS=("${COMMUNS[@]}" --depuis "$ORIGINE" --generations 3 --graine "$g" --appels-max 160 --usd-par-generation 37
              --temps-max 2400 --entrainements-max 0 --plafond-total 555) ;;
esac
# 5 bis. appel de contrôle par espèce de la course (statut OK exigé, sinon la course ne part pas) ; coût consigné
case "$COURSE" in repetition) ESPECES_CONTROLE="CLAUDE_OPUS_5_5" ;; *) ESPECES_CONTROLE="CLAUDE_FABLE_5_1 CLAUDE_OPUS_5_5 GEMINI_ARGON" ;; esac
controle=$(cd "$CODE/essaim-m3-refonte-v1" && env -i PATH=/usr/bin:/bin HOME="$RACINE" LANG=C.UTF-8 \
    HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
    SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
    ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY" ANTHROPIC_CUSTOM_HEADERS="anthropic-workspace-id: $RR_ANTHROPIC_WORKSPACE_ID" \
    GEMINI_API_KEY="$GEMINI_API_KEY" "$VENV/bin/python" -B - "$RACINE/controle-especes-$COURSE" $ESPECES_CONTROLE <<'PY'
import json, sys
from essaim_m3.noyau.appels import Appelant, charger_collisionneur
cv = charger_collisionneur()
a = Appelant(sys.argv[1], 0.50, cv.APPELANTS, reel=True, go_id="GO-2026-10-24-05")
sortie = {}
for e in sys.argv[2:]:
    r = a.appeler(e, "controle", "Réponds par le seul mot : prêt.", max_tokens=512)
    sortie[e] = {"statut": r.statut, "modele_servi": r.modele_servi, "cout_usd": r.cout_usd}
print(json.dumps({"especes": sortie, "cout_usd": round(a.depense_usd, 4)}, ensure_ascii=False))
sys.exit(0 if all(v["statut"] == "OK" for v in sortie.values()) else 1)
PY
) || { note "appel de contrôle en échec : ${controle:-sans sortie}"; exit 2; }
note "appel de contrôle : $controle"
note "départ : $(printf '%q ' "${ARGS[@]}" | sed "s#$RACINE#<courses>#g")"
# 6. course : environnement minimal ; clé Anthropic des runs sous ANTHROPIC_API_KEY, en-tête d'espace de travail par
# ANTHROPIC_CUSTOM_HEADERS, ANTHROPIC_BASE_URL absente (GO-2026-10-24-04) ; aucune valeur affichée ni écrite
set +e
(cd "$CODE/essaim-m3-refonte-v1" && env -i PATH=/usr/bin:/bin HOME="$RACINE" LANG=C.UTF-8 \
    HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
    SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
    ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY" ANTHROPIC_CUSTOM_HEADERS="anthropic-workspace-id: $RR_ANTHROPIC_WORKSPACE_ID" \
    GEMINI_API_KEY="$GEMINI_API_KEY" ${BRAVE_API_KEY:+BRAVE_API_KEY="$BRAVE_API_KEY"} \
    "$VENV/bin/python" -B -m essaim_m3 lancer "${ARGS[@]}") > "$RACINE/$COURSE.sortie.json" 2> "$RACINE/$COURSE.erreurs.txt"
code=$?
set -e
printf '{"course": "%s", "code": %d, "fin_utc": "%s"}\n' "$COURSE" "$code" "$(date -u +%FT%TZ)" > "$SORTIE/rapport-fin.json" 2>/dev/null \
    || printf '{"course": "%s", "code": %d}\n' "$COURSE" "$code" > "$RACINE/$COURSE.rapport-fin.json"
note "fin, code $code"
exit $code
