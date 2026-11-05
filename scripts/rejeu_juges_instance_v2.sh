#!/usr/bin/env bash
# Rejeu de la cellule de juge redéfinie sur les 180 notations (120 textes) du pilote de T0.5, sur l'instance de calcul
# (GO-2026-10-29-04), v2. Copie adaptée de `rejeu_juges_instance_v1.sh` sous un nom nouveau (R12 : la v1 n'est pas
# modifiée) : mise en place, suite ciblée des tests au nombre attendu, un run de
# `controle_ia.environnements.noter_rejeu_juges_v2` (variante « verdict-echelles » : 8B, décisif, puis 3B, descriptif,
# dans l'ordre de priorité de la configuration),
# poussée des résultats et des traces sur BRANCHE (rien ne reste sur l'instance). Les lignes de progression du module
# (préfixe « PROGRES », nombres, noms de juges et de variantes, statuts) sont recopiées dans le journal ; aucune autre
# ligne n'y passe (aucun texte, aucun compte de scores). Devis et fiche de lancement :
# docs/notes/couche-2-preparation-v1/rejeu-juges-v2/.
#
#   COMMIT=<commit de scellement de la fiche> bash rejeu_juges_instance_v2.sh
#
# Variables :
#   COMMIT          (obligatoire) commit à extraire ; le module vérifie en plus le commit du code, la configuration, les
#                   runs rejoués, les empreintes, la consigne, les tâches et l'entropie que cite la fiche
#   MODE            reel (défaut) ou jouet (répétition sur processeur)
#   FICHE           défaut docs/notes/couche-2-preparation-v1/rejeu-juges-v2/fiche-lancement-rejeu-juges-v2.md ; elle
#                   cite une seule fois chacun « Tests attendus : `N` » et les chemins lus ci-dessous, avant l'installation
#   PREREG_ABSENT   1 seulement en mode jouet : répétition sans fiche ; CONFIG, TACHES, TESTS_ATTENDUS donnés
#   ECHEANCE_AMORCE horodatage (secondes depuis 1970, UTC) du plafond de l'amorce : le délai externe du run est borné
#                   par le temps qui reste avant lui, moins 13 minutes (KILL du run 5, poussées 8) ; l'échéance du
#                   module (--echeance-externe) est ce délai moins MARGE_DERNIER_LOT (contre-lecture, CLJ-02)
#   DEPOT_URL       défaut https://github.com/lciric/controle-ia-travail.git (dépôt de travail privé ; N-016)
#   GH_TOKEN        jeton GitHub à grain fin ; lu par un assistant d'identification, jamais écrit ni affiché
#   HF_TOKEN        jeton Hugging Face en lecture (mode reel)
#   BRANCHE         défaut calcul/rejeu-juges-v2 ; une branche qui existe déjà arrête avant tout calcul (jamais celle
#                   de la v1, calcul/rejeu-juges-v1)
#   TRAVAIL         défaut $HOME/rejeu
#   VENV_EXISTANT   environnement Python prêt à réutiliser (sinon : python3.11 -m venv + requirements-gpu.txt)
#   SAUTER_TESTS    1 seulement en mode jouet (banc de la chaîne)
set -euo pipefail

: "${COMMIT:?COMMIT obligatoire (commit de scellement de la fiche de lancement)}"
MODE="${MODE:-reel}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE="${BRANCHE:-calcul/rejeu-juges-v2}"
FICHE="${FICHE:-docs/notes/couche-2-preparation-v1/rejeu-juges-v2/fiche-lancement-rejeu-juges-v2.md}"
TRAVAIL="${TRAVAIL:-$HOME/rejeu}"
PREREG_ABSENT="${PREREG_ABSENT:-0}"
DELAI_RUN_MAX=65                 # minutes : durée globale du module (55 minutes), plus la marge du dernier lot, et 4
MARGE_FIN=8                      # minutes gardées avant le plafond de l'amorce pour consigner et pousser
DELAI_RUN_MIN=45                 # en dessous, le run ne commence pas (consigné) : la phase décisive (8B, 35 minutes),
                                 # les chargements (≈ 4) et la marge du dernier lot (6) ne tiendraient plus ; le 3B
                                 # seul, descriptif, ne justifie pas la dépense
MARGE_DERNIER_LOT=6              # minutes : l'échéance passée au module précède le délai externe d'autant ; une phase ne
                                 # commence que si elle tient avant cette échéance, et son dernier lot (≈ 1,5 minute au
                                 # pire : 256 pas du 8B et la lecture de 8 blocs) finit avant le TERM : aucune phase
                                 # commencée n'est tuée
# suite ciblée (devis, § 4) : le module v2, le module v1 dont il importe les fonctions, le lanceur des notations, le
# pilote, le manifeste, le scellement et les préenregistrements ; le nombre exact est cité par la fiche
TESTS_CIBLES=(tests/test_noter_rejeu_juges_v2.py tests/test_noter_rejeu_juges_v1.py tests/test_noter_pilote_a.py
              tests/test_pilote_a.py tests/test_manifeste.py tests/test_scellement.py tests/test_prereg.py)
case "$MODE" in reel|jouet) ;; *) echo "MODE=$MODE : reel ou jouet" >&2; exit 2 ;; esac
if [ "$PREREG_ABSENT" = 1 ] && [ "$MODE" != jouet ]; then
    echo "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1)" >&2; exit 2
fi
if [ "${SAUTER_TESTS:-0}" = 1 ] && [ "$MODE" != jouet ]; then
    echo "SAUTER_TESTS=1 n'est permis qu'en mode jouet" >&2; exit 2
fi
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-z_]+=[^ ]+)+$'

mkdir -p "$TRAVAIL"
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'

journal "début : rejeu des juges v2 ; MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE"
[ "$MODE" = reel ] && : "${HF_TOKEN:?HF_TOKEN obligatoire en mode reel}"

DEPOT="$TRAVAIL/controle-ia"
if [ -e "$DEPOT" ]; then
    echo "$DEPOT existe déjà : R12, aucune réécriture ; choisir un autre TRAVAIL" >&2
    exit 2
fi
git -c credential.helper="$AIDE_GIT" clone -q "$DEPOT_URL" "$DEPOT"
cd "$DEPOT"
git config credential.helper "$AIDE_GIT"
git config user.name "instance de calcul (rejeu des juges v2)"
git config user.email "instance-calcul@invalid"
git checkout -q "$COMMIT"
code_branche=0
git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>"$TRAVAIL/ls-remote.err" || code_branche=$?
case "$code_branche" in
    0) journal "branche $BRANCHE déjà présente sur le dépôt distant : arrêt avant l'installation (R12)"; exit 2 ;;
    2) ;;
    *) journal "vérification de la branche $BRANCHE impossible (git ls-remote, code $code_branche) : arrêt avant l'installation"
       exit 2 ;;
esac
git checkout -q -b "$BRANCHE"

# Lecture précoce de la fiche, avant toute installation : chaque intitulé lu y figure une seule fois
lire_unique() {
    local n
    n=$(grep -c "$1 : \`" "$FICHE" || true)
    if [ "$n" != 1 ]; then echo ""; return 0; fi
    sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$FICHE"
}
ARGS=()
if [ "$PREREG_ABSENT" = 1 ]; then
    ATTENDUS="${TESTS_ATTENDUS:-}"
    : "${CONFIG:?CONFIG obligatoire sans fiche}" "${TACHES:?TACHES obligatoire sans fiche}"
    journal "répétition sans fiche (jouet, non décisive)"
else
    [ -f "$FICHE" ] && [ -f "$FICHE.sha256" ] || { journal "fiche $FICHE ou son sceau absent au commit $COMMIT : arrêt avant l'installation"; exit 2; }
    # marqueur restant (même contrôle que le lanceur) : sinon le module ne l'arrêterait qu'après la mise en place payée
    if grep -q -e 'À REMPLIR' -e '<<[A-Z0-9_]*>>' "$FICHE"; then
        journal "fiche : marqueur restant (« À REMPLIR » ou marqueur entre chevrons) : arrêt avant l'installation"; exit 2
    fi
    ATTENDUS=$(lire_unique "Tests attendus")
    [[ "$ATTENDUS" =~ ^[0-9]+$ ]] || { journal "nombre de tests attendus introuvable ou cité plusieurs fois dans la fiche : arrêt avant l'installation"; exit 2; }
    CONFIG=$(lire_unique "Chemin de la configuration du rejeu")
    TACHES=$(lire_unique "Chemin des tâches du pilote rejoué")
    CITES=("$FICHE" "$CONFIG" "$TACHES")
    for intitule in "Chemin du manifeste du pilote rejoué" "Chemin des épisodes du pilote rejoué" \
                    "Chemin de l'arrêt du pilote rejoué" "Chemin du manifeste des notations rejouées" \
                    "Chemin des notations rejouées du 8B" "Chemin des notations rejouées du 3B"; do
        CITES+=("$(lire_unique "$intitule")")
    done
    for f in "${CITES[@]}"; do
        [ -n "$f" ] || { journal "chemin cité introuvable ou cité plusieurs fois dans la fiche : arrêt avant l'installation"; exit 2; }
        [ -f "$f" ] && [ -f "$f.sha256" ] || { journal "fichier cité $f ou son sceau absent au commit $COMMIT : arrêt avant l'installation"; exit 2; }
    done
    if ! PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -u -m controle_ia.scellement verifier "${CITES[@]}" \
            >"$TRAVAIL/sceaux.txt" 2>&1; then
        journal "sceau non conforme parmi les fichiers cités ($(grep -v '^OK ' "$TRAVAIL/sceaux.txt" | tail -n 1)) : arrêt avant l'installation"
        exit 2
    fi
    ARGS=(--prereg "$FICHE")
    journal "fiche lue : $ATTENDUS tests attendus ; configuration $CONFIG ; tâches $TACHES ; pilote et notations rejouées présents et scellés"
fi

pousser() {
    local essai cause
    for essai in 1 2 3; do
        if git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee.err"; then return 0; fi
        cause=$( (grep -E '^(fatal|error|remote):' "$TRAVAIL/poussee.err" || tail -n 2 "$TRAVAIL/poussee.err") | tr '\n' ' ' || true)
        journal "poussée de la branche $BRANCHE : tentative $essai refusée ($cause)"
        if [ "$essai" -lt 3 ]; then sleep $((15 * essai * essai)); fi
    done
    return 1
}
pousser || { journal "poussée initiale de $BRANCHE refusée (droit d'écriture du jeton ?) : arrêt avant l'installation"; exit 2; }
journal "branche $BRANCHE poussée avant l'installation (droit d'écriture éprouvé)"

traces() {
    local d
    mkdir -p traces
    d=$(mktemp -d "traces/rejeu-juges-v2-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$TRAVAIL/encodage.json" "$TRAVAIL/encodage.err" "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" "$TRAVAIL/run.json" "$TRAVAIL/run.err" \
             "$TRAVAIL/machine.txt" "$TRAVAIL/pip-freeze.txt"; do
        [ -f "$f" ] && cp "$f" "$d/"
    done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    git add "$d" && git commit -qm "Rejeu des juges v2 : traces de l'instance ($1)" >/dev/null 2>&1 || true
}
CONSIGNE=""
consigner_arret() {
    CONSIGNE=1
    git add -A runs diag 2>/dev/null || true
    if git commit -qm "Rejeu des juges v2 : arrêt pendant $1" >/dev/null 2>&1; then
        journal "ARRÊT pendant $1 : résultats partiels committés (dont arret.json s'il existe)"
    else
        journal "ARRÊT pendant $1 : aucun résultat à committer"
    fi
    traces "arrêt pendant $1"
    if pousser; then journal "branche $BRANCHE poussée"; else journal "poussée impossible : résultats restés sur l'instance"; fi
}
ETAPE="mise en place"
PID_RUN=""
sur_term() {
    trap '' TERM
    journal "TERM reçu pendant $ETAPE (plafond de l'amorce)"
    if [ -n "$PID_RUN" ]; then
        kill -TERM "$PID_RUN" 2>/dev/null || true
        wait "$PID_RUN" 2>/dev/null || true
    fi
    consigner_arret "$ETAPE (plafond de l'amorce)" || true
    exit 124
}
trap sur_term TERM
sur_sortie() {
    local code=$?
    if [ "$code" -ne 0 ] && [ -z "$CONSIGNE" ]; then
        trap '' TERM
        journal "sortie imprévue (code $code) pendant $ETAPE" || true
        consigner_arret "$ETAPE (sortie imprévue, code $code)" || true
    fi
    exit "$code"
}
trap sur_sortie EXIT

{ nproc; lscpu 2>/dev/null | grep -E '^(Model name|CPU\(s\))' || true; free -g 2>/dev/null | head -2 || true;
  [ "$MODE" = reel ] && nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv; } > "$TRAVAIL/machine.txt" 2>&1 || true
tee -a "$JOURNAL" < "$TRAVAIL/machine.txt" >/dev/null

if [ -n "${VENV_EXISTANT:-}" ]; then
    # shellcheck disable=SC1091
    . "$VENV_EXISTANT/bin/activate"
else
    python3.11 -m venv .venv
    # shellcheck disable=SC1091
    . .venv/bin/activate
    pip install -q -r requirements-gpu.txt
fi
python -m pip freeze --all >"$TRAVAIL/pip-freeze.txt" 2>/dev/null || journal "pip freeze impossible (descriptif, sans effet sur le run)"
python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())" | tee -a "$JOURNAL"
if [ "$MODE" = reel ] && ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
    journal "carte indisponible pour torch : arrêt avant les tests"; consigner_arret "contrôle de la carte"; exit 1
fi

# garde d'encodage préalable (contre-lecture R2, CLR2-06) : tokeniseurs seuls des juges, avant la suite de tests ; un
# découpage inattendu arrête ici en quelques secondes, et non après ≈ 25 minutes payées. La garde du run reste faite.
ETAPE="contrôle préalable de l'encodage"
if ! PYTHONPATH=src python -m controle_ia.environnements.noter_rejeu_juges_v2 --controle-encodage "$CONFIG" \
        >"$TRAVAIL/encodage.json" 2>"$TRAVAIL/encodage.err"; then
    grep -v '^PROGRES ' "$TRAVAIL/encodage.err" | tail -n 3 | tee -a "$JOURNAL" || true
    journal "garde d'encodage préalable en échec : arrêt avant les tests"; consigner_arret "contrôle préalable de l'encodage"; exit 1
fi
journal "garde d'encodage préalable réussie (tokeniseurs seuls des juges)"

ETAPE="tests"
if [ "${SAUTER_TESTS:-0}" = 1 ]; then
    journal "tests sautés (banc jouet seulement)"
elif ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no "${TESTS_CIBLES[@]}" >"$TRAVAIL/tests.txt" 2>"$TRAVAIL/tests.err"; then
    tail -n 5 "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" | tee -a "$JOURNAL"
    journal "tests en échec : arrêt"; consigner_arret "tests"; exit 1
fi
DERNIERE=$(tail -1 "$TRAVAIL/tests.txt" 2>/dev/null || true)
[ -n "$DERNIERE" ] && journal "tests : $DERNIERE"
if [ "${SAUTER_TESTS:-0}" != 1 ] && [ -n "$ATTENDUS" ] && ! printf '%s\n' "$DERNIERE" | grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then
    journal "tests : « $DERNIERE » ≠ « $ATTENDUS passed », sans test sauté ni en échec : arrêt"; consigner_arret "tests"; exit 1
fi

# délai externe du run : DELAI_RUN_MAX minutes, borné par le temps restant avant le plafond de l'amorce moins MARGE_FIN ;
# TERM converti en arrêt consigné par le module, puis KILL cinq minutes plus tard ; le signal vise le processus lancé par
# timeout, par son identifiant (R10)
DELAI=$DELAI_RUN_MAX
if [ -n "${ECHEANCE_AMORCE:-}" ]; then
    [[ "$ECHEANCE_AMORCE" =~ ^[0-9]+$ ]] || { journal "ECHEANCE_AMORCE illisible : arrêt"; consigner_arret "délai du run"; exit 1; }
    RESTE=$(( (ECHEANCE_AMORCE - $(date -u +%s)) / 60 - MARGE_FIN - 5 ))
    [ "$RESTE" -lt "$DELAI" ] && DELAI=$RESTE
fi
if [ "$DELAI" -lt "$DELAI_RUN_MIN" ]; then
    journal "temps restant avant le plafond de l'amorce insuffisant ($DELAI minutes < $DELAI_RUN_MIN) : le run ne commence pas"
    consigner_arret "délai du run"; exit 1
fi
RUN="$(date -u +%Y%m%d-%H%M%S)-rejeu-juges-v2-$MODE"
ETAPE="run $RUN"
# échéance absolue du module : délai externe moins la marge du dernier lot, calculée juste avant de lancer timeout ;
# le module retient la plus proche de celle-ci et de sa durée globale, et la consigne (résumé, arrêt)
ECHEANCE_RUN=$(( $(date -u +%s) + (DELAI - MARGE_DERNIER_LOT) * 60 ))
journal "run : $RUN ; délai externe $DELAI minutes ; échéance du module $(date -u -d "@$ECHEANCE_RUN" +%FT%TZ) ; configuration $CONFIG ; tâches $TACHES"
code=0
: >"$TRAVAIL/run.err"
PYTHONPATH=src timeout --signal=TERM --kill-after=5m "${DELAI}m" python -m controle_ia.environnements.noter_rejeu_juges_v2 \
    --config "$CONFIG" --taches "$TACHES" --run-id "$RUN" --echeance-externe "$ECHEANCE_RUN" "${ARGS[@]}" \
    >"$TRAVAIL/run.json" 2>>"$TRAVAIL/run.err" &
PID_RUN=$!
# relais des lignes de progression : tail s'arrête de lui-même à la fin du run (--pid), sans arrêt par motif (R10)
( tail -n +1 -F --pid="$PID_RUN" "$TRAVAIL/run.err" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" \
    | while IFS= read -r ligne; do printf '%s\n' "$ligne" | tee -a "$JOURNAL"; done ) &
PID_RELAIS=$!
wait "$PID_RUN" || code=$?
PID_RUN=""
wait "$PID_RELAIS" 2>/dev/null || true
if [ "$code" -ne 0 ]; then
    if [ -f "diag/$RUN/resume.json" ] && [ ! -f "diag/$RUN/arret.json" ]; then
        journal "run : code $code, mais résumé écrit sans arrêt consigné : run complet"
    else
        grep -v '^PROGRES ' "$TRAVAIL/run.err" | tail -n 5 | tee -a "$JOURNAL" || true
        consigner_arret "run (code $code)"; exit 1
    fi
fi
git add "runs/$RUN" "diag/$RUN"
git commit -qm "Rejeu des juges v2 ($MODE), run $RUN"
# le résumé reste dans run.json, versé aux traces ; il n'est pas recopié au journal que lit la surveillance
journal "run terminé : $RUN"
ETAPE="poussée"
pousser || journal "poussée du run impossible : résultats restés sur l'instance"
ETAPE="fin"
CONSIGNE=1
traces "fin"
if pousser; then
    journal "fin : $RUN ; branche $BRANCHE poussée (résultats et traces) ; arrêter l'instance par son identifiant (R10)"
else
    journal "run complet, mais poussée finale impossible après trois tentatives : résultats et traces restés sur l'instance"
    exit 1
fi
