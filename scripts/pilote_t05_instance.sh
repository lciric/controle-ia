#!/usr/bin/env bash
# Pilote 8B de l'environnement (a) (T0.5) sur l'instance de calcul : mise en place, tests, un run, poussée des résultats
# et des vecteurs par action (rien ne reste sur l'instance : leçon de N-012). Procédure : docs/procedures/ (pilote T0.5).
# Sert aussi la revalidation courte de l'équivalence sur le domaine du pilote (ETUDE=revalidation ; P-007, lecture de R-085), avant
# le pilote : même mise en place, même machine, un autre lanceur, pas de vecteurs.
# Rien ne se lance sans GO consigné.
#
#   COMMIT=<commit de scellement du préenregistrement> bash pilote_t05_instance.sh
#
# Variables :
#   COMMIT        (obligatoire) commit à extraire ; le lanceur Python vérifie en plus le commit, la configuration, les
#                 tâches et l'entropie cités par le préenregistrement
#   ETUDE         pilote (défaut) ou revalidation
#   MODE          reel (défaut) ou jouet (répétition sur processeur, sans modèle réel ni processeur graphique)
#   PREREG        défaut prereg/T0.5-pilote-8B-v1.md (pilote) ou prereg/T0.5-revalidation-equivalence-pilote-v1.md
#                 (revalidation) ; il cite les chemins de la configuration et des tâches (« Chemin de la configuration :
#                 `…` », « Chemin des tâches : `…` » ; revalidation : « Chemin des tâches d'entraînement : `…` », « Chemin
#                 des tâches d'évaluation : `…` »), que ce script lit
#   PREREG_ABSENT 1 seulement en mode jouet : répétition sans préenregistrement (run non décisif) ; CONFIG et TACHES
#                 (revalidation : CONFIG, ENTRAINEMENT, EVALUATION) donnent alors les chemins (hors du dépôt possible)
#   DEPOT_URL     défaut https://github.com/lciric/controle-ia.git
#   GH_TOKEN      jeton GitHub à grain fin (dépôt distant GitHub) ; lu par un assistant d'identification, jamais écrit
#   HF_TOKEN      jeton Hugging Face en lecture (mode reel) ; lu par huggingface_hub
#   BRANCHE       défaut calcul/t05-pilote-<MODE>-v1 (revalidation : calcul/t05-revalidation-<MODE>-v1 ; le mode dans le
#                 nom : une répétition jouet n'occupe pas la branche du run réel, W-11) ; les vecteurs du pilote vont
#                 sur une branche à part, donnees/t05/<run>. Une branche qui existe déjà sur le dépôt distant arrête avant
#                 tout calcul : un relancement prend une branche nouvelle (…-v2), jamais une réécriture (R12 ; RV-14)
#   TESTS_ATTENDUS nombre de tests attendus (sans préenregistrement seulement) ; sinon lu dans le préenregistrement
#                 (« Tests attendus : `N` ») : la dernière ligne de pytest doit être
#                 « N passed[, M warning(s)] in X s[ (h:mm:ss)] », rien d'autre (aucun test sauté, attendu en échec ou en
#                 erreur ; RV-14)
#   TRAVAIL       défaut $HOME/t05
#   VENV_EXISTANT environnement Python déjà prêt à réutiliser (sinon : python3.11 -m venv + requirements-gpu.txt)
set -euo pipefail

: "${COMMIT:?COMMIT obligatoire (commit de scellement du préenregistrement)}"
ETUDE="${ETUDE:-pilote}"
MODE="${MODE:-reel}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia.git}"
case "$ETUDE" in
    pilote) BRANCHE="${BRANCHE:-calcul/t05-pilote-$MODE-v1}"; PREREG="${PREREG:-prereg/T0.5-pilote-8B-v1.md}" ;;
    revalidation) BRANCHE="${BRANCHE:-calcul/t05-revalidation-$MODE-v1}"
                  PREREG="${PREREG:-prereg/T0.5-revalidation-equivalence-pilote-v1.md}" ;;
    *) echo "ETUDE=$ETUDE : pilote ou revalidation" >&2; exit 2 ;;
esac
TRAVAIL="${TRAVAIL:-$HOME/t05}"
PREREG_ABSENT="${PREREG_ABSENT:-0}"
case "$MODE" in reel|jouet) ;; *) echo "MODE=$MODE : reel ou jouet" >&2; exit 2 ;; esac
if [ "$PREREG_ABSENT" = 1 ] && [ "$MODE" != jouet ]; then
    echo "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1)" >&2; exit 2
fi
# taille au-delà de laquelle les vecteurs ne sont pas poussés (limite du dépôt distant : 100 Mo par fichier)
TAILLE_MAX_VECTEURS=95000000

mkdir -p "$TRAVAIL"
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'

journal "début : ETUDE=$ETUDE MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE"
if [ "$MODE" = reel ]; then
    : "${HF_TOKEN:?HF_TOKEN obligatoire en mode reel}"
fi

DEPOT="$TRAVAIL/controle-ia"
if [ -e "$DEPOT" ]; then
    echo "$DEPOT existe déjà : R12, aucune réécriture ; choisir un autre TRAVAIL" >&2
    exit 2
fi
git -c credential.helper="$AIDE_GIT" clone -q "$DEPOT_URL" "$DEPOT"
cd "$DEPOT"
git config credential.helper "$AIDE_GIT"
git config user.name "instance de calcul (T0.5)"
git config user.email "instance-calcul@invalid"
git checkout -q "$COMMIT"
# branche neuve (RV-14) : code 0, la branche existe (arrêt) ; code 2, elle n'existe pas (suite) ; tout autre code, la
# vérification est impossible (dépôt distant injoignable) : arrêt, jamais de repli silencieux (W-9). Nom complet exigé.
# Messages au journal, avec la cause donnée par git (relecture du différentiel de la revalidation, X-8).
code_branche=0
git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>"$TRAVAIL/ls-remote.err" || code_branche=$?
case "$code_branche" in
    0) journal "branche $BRANCHE déjà présente sur le dépôt distant : relancement sous une branche nouvelle (BRANCHE=…) ; arrêt avant l'installation"
       exit 2 ;;
    2) ;;
    *) cause=$( (grep -E '^(fatal|error|remote):' "$TRAVAIL/ls-remote.err" || tail -n 2 "$TRAVAIL/ls-remote.err") | tr '\n' ' ' || true)
       journal "vérification de la branche $BRANCHE impossible (git ls-remote, code $code_branche : $cause) : arrêt avant l'installation"
       exit 2 ;;
esac
git checkout -q -b "$BRANCHE"

# Lecture précoce du préenregistrement (W-1, W-10), avant toute installation, donc avant de payer la carte : présence,
# nombre de tests attendus, chemins cités ; présence dans l'arbre du commit de la configuration et des fichiers de tâches
# (sous donnees/<run d'extraction>/, ajoutés de force au suivi par la session à chaque étape de l'extraction, selon
# N-014 (a)) et de leurs sceaux ; sceaux contrôlés par le module du dépôt, aux mêmes règles que le lanceur : une ligne,
# nom de base, empreinte (relecture du différentiel de la revalidation, X-3). Le module ne demande que la bibliothèque
# standard : il tourne avant l'installation. Le lanceur Python compare ensuite chaque empreinte à celle que cite le
# préenregistrement.
lire_chemin() { sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$PREREG" | head -1; }
if [ "$PREREG_ABSENT" = 1 ]; then
    ATTENDUS="${TESTS_ATTENDUS:-}"
    : "${CONFIG:?CONFIG obligatoire sans préenregistrement}"
    if [ "$ETUDE" = pilote ]; then
        : "${TACHES:?TACHES obligatoire sans préenregistrement}"
    else
        : "${ENTRAINEMENT:?ENTRAINEMENT obligatoire sans préenregistrement}" "${EVALUATION:?EVALUATION obligatoire sans préenregistrement}"
    fi
    CITES=()
else
    [ -f "$PREREG" ] || { journal "préenregistrement $PREREG absent au commit $COMMIT : arrêt avant l'installation"; exit 2; }
    ATTENDUS=$(sed -n "s/.*Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$PREREG" | head -1)
    [ -n "$ATTENDUS" ] || { journal "nombre de tests attendus introuvable dans $PREREG : arrêt avant l'installation"; exit 2; }
    CONFIG=$(lire_chemin "Chemin de la configuration")
    if [ "$ETUDE" = pilote ]; then
        TACHES=$(lire_chemin "Chemin des tâches")
        CITES=("$TACHES")
    else
        ENTRAINEMENT=$(lire_chemin "Chemin des tâches d'entraînement")
        EVALUATION=$(lire_chemin "Chemin des tâches d'évaluation")
        CITES=("$ENTRAINEMENT" "$EVALUATION")
    fi
    for f in "$CONFIG" "${CITES[@]}"; do
        [ -n "$f" ] || { journal "chemin de la configuration ou des tâches introuvable dans $PREREG : arrêt avant l'installation"; exit 2; }
    done
    [ -f "$CONFIG" ] || { journal "configuration $CONFIG absente de l'arbre du commit $COMMIT : arrêt avant l'installation"; exit 2; }
    for f in "$CONFIG" "${CITES[@]}"; do
        if [ ! -f "$f" ] || [ ! -f "$f.sha256" ]; then
            journal "fichier cité $f ou son sceau absent de l'arbre du commit $COMMIT (ajout forcé de N-014 manquant ?) : arrêt avant l'installation"
            exit 2
        fi
    done
    # sortie non tamponnée, et cause lue hors des lignes « OK » : le journal nomme le fichier fautif (Z-1)
    if ! PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -u -m controle_ia.scellement verifier "$CONFIG" "${CITES[@]}" \
            >"$TRAVAIL/sceaux.txt" 2>&1; then
        cause=$(grep -v '^OK ' "$TRAVAIL/sceaux.txt" | tail -n 1 || true)
        journal "sceau non conforme parmi les fichiers cités ($cause) : arrêt avant l'installation"
        exit 2
    fi
    journal "préenregistrement lu : $ATTENDUS tests attendus ; configuration $CONFIG ; tâches ${CITES[*]} présentes et scellées"
fi

pousser() { git push -q origin "$BRANCHE"; }
traces() {
    # journal, sorties des tests et du run, versés sur la branche (hors arbre gelé) pour la session de pilotage ;
    # un dossier neuf à chaque versement (R12)
    local d
    mkdir -p traces
    d=$(mktemp -d "traces/t05-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" "$TRAVAIL"/run.json "$TRAVAIL"/run.err \
             "$TRAVAIL"/nvidia-smi.txt; do
        [ -f "$f" ] && cp "$f" "$d/"
    done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true          # R6 : traces scellées
    git add "$d" && git commit -qm "T0.5 — traces de l'instance ($1)" >/dev/null 2>&1 || true
}
pousser_vecteurs() {
    # vecteurs par action (hors git sur la branche de travail) : poussés sur une branche neuve donnees/t05/<run>, faite
    # d'un seul commit sans parent, par la plomberie de git (l'arbre de travail n'est pas touché). Une branche qui
    # existe déjà refuse la poussée (R12 : rien n'est écrasé). Aucun repli silencieux : chaque issue est journalisée.
    local run=$1 f taille b s t1 t2 c
    f="donnees/$run/vecteurs-par-action.npz"
    if [ ! -f "$f" ] || [ ! -f "$f.sha256" ]; then journal "vecteurs absents ($f) : rien à pousser"; return 1; fi
    if ! (cd "donnees/$run" && sha256sum -c --quiet vecteurs-par-action.npz.sha256); then
        journal "vecteurs : empreinte non conforme : non poussés, restés sur l'instance"; return 1
    fi
    taille=$(stat -c %s "$f")
    if [ "$taille" -gt "$TAILLE_MAX_VECTEURS" ]; then
        journal "vecteurs trop gros ($taille octets) : non poussés, restés sur l'instance"; return 1
    fi
    b=$(git hash-object -w "$f")
    s=$(git hash-object -w "$f.sha256")
    t1=$(printf '100644 blob %s\tvecteurs-par-action.npz\n100644 blob %s\tvecteurs-par-action.npz.sha256\n' "$b" "$s" | git mktree)
    t2=$(printf '040000 tree %s\t%s\n' "$t1" "$run" | git mktree)
    c=$(git commit-tree "$t2" -m "T0.5 — vecteurs par action du run $run (empreinte $(cut -c1-16 "$f.sha256"))")
    if git push -q origin "$c:refs/heads/donnees/t05/$run"; then
        journal "vecteurs poussés : branche donnees/t05/$run, commit $c, $taille octets"
    else
        journal "vecteurs : poussée impossible : restés sur l'instance"; return 1
    fi
}
CONSIGNE=""
consigner_arret() {
    CONSIGNE=1
    git add -A runs diag
    if git commit -qm "T0.5 — $ETUDE : arrêt pendant $1" >/dev/null 2>&1; then
        journal "ARRÊT pendant $1 : résultats partiels committés (dont arret.json s'il existe)"
    else
        journal "ARRÊT pendant $1 : aucun résultat à committer"
    fi
    traces "arrêt pendant $1"
    if pousser; then journal "branche $BRANCHE poussée"; else journal "poussée impossible : résultats restés sur l'instance"; fi
    if [ -n "${RUN:-}" ] && [ -d "donnees/$RUN" ]; then pousser_vecteurs "$RUN" || true; fi
}

ETAPE="mise en place"
PID_RUN=""
sur_term() {
    # plafond de l'amorce (TERM) : le signal passe au run en cours par son identifiant de processus (R10), qui consigne
    # son arrêt (arret.json) ; puis résultats partiels, traces et poussée, avant le KILL de l'amorce (cinq minutes)
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
    # filet : une sortie en échec que rien n'a consignée (commande en échec sous set -e, erreur imprévue) consigne
    # l'arrêt, verse les traces et pousse ; le code de sortie est conservé
    local code=$?
    if [ "$code" -ne 0 ] && [ -z "$CONSIGNE" ]; then
        trap '' TERM
        journal "sortie imprévue (code $code) pendant $ETAPE" || true
        consigner_arret "$ETAPE (sortie imprévue, code $code)" || true
    fi
    exit "$code"
}
trap sur_sortie EXIT

if [ "$MODE" = reel ]; then
    nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv | tee -a "$JOURNAL" "$TRAVAIL/nvidia-smi.txt"
fi

if [ -n "${VENV_EXISTANT:-}" ]; then
    # shellcheck disable=SC1091
    . "$VENV_EXISTANT/bin/activate"
else
    python3.11 -m venv .venv
    # shellcheck disable=SC1091
    . .venv/bin/activate
    pip install -q -r requirements-gpu.txt
fi

python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())" | tee -a "$JOURNAL"
if [ "$MODE" = reel ] && ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
    # roue de torch : pilote CUDA ≥ 13.0 exigé (requirements-gpu.txt) ; arrêt avant les tests, sur l'instance payée (RV-14)
    journal "carte indisponible pour torch (pilote CUDA trop ancien ?) : arrêt avant les tests"
    consigner_arret "contrôle de la carte"
    exit 1
fi
ETAPE="tests"
if ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no >"$TRAVAIL/tests.txt" 2>"$TRAVAIL/tests.err"; then
    tail -n 5 "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" | tee -a "$JOURNAL"
    journal "tests en échec : arrêt"
    consigner_arret "tests"
    exit 1
fi
DERNIERE=$(tail -1 "$TRAVAIL/tests.txt")
journal "tests : $DERNIERE"
if [ -n "$ATTENDUS" ] && ! printf '%s\n' "$DERNIERE" | grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then
    journal "tests : « $DERNIERE » ≠ « $ATTENDUS passed », sans test sauté ni en échec : arrêt"
    consigner_arret "tests"
    exit 1
fi

ETAPE="lancement"
ARGS=()
if [ "$PREREG_ABSENT" = 1 ]; then
    journal "répétition sans préenregistrement (jouet, non décisive)"
else
    ARGS=(--prereg "$PREREG")
fi
if [ "$ETUDE" = pilote ]; then
    journal "configuration : $CONFIG ; tâches : $TACHES"
    LANCEUR=(controle_ia.environnements.lancer_pilote_a --config "$CONFIG" --taches "$TACHES")
else
    journal "configuration : $CONFIG ; tâches d'entraînement : $ENTRAINEMENT ; tâches d'évaluation : $EVALUATION"
    LANCEUR=(controle_ia.environnements.revalider_pilote_a --config "$CONFIG" --entrainement "$ENTRAINEMENT" --evaluation "$EVALUATION")
fi

# délai externe du run, figé (R1) : TERM à 270 minutes, converti en arrêt consigné (arret.json), puis KILL cinq minutes
# plus tard si le processus ne rend pas la main ; la limite interne (duree_max_s de la configuration) est plus courte.
# Le signal vise le processus lancé par timeout, par son identifiant (R10).
DELAI=(timeout --signal=TERM --kill-after=5m 270m)
RUN="$(date -u +%Y%m%d-%H%M%S)-t05-$ETUDE-$MODE"
ETAPE="run $RUN"
journal "run : $RUN"
code=0
PYTHONPATH=src "${DELAI[@]}" python -m "${LANCEUR[@]}" --run-id "$RUN" "${ARGS[@]}" >"$TRAVAIL/run.json" \
    2>>"$TRAVAIL/run.err" &
PID_RUN=$!
wait "$PID_RUN" || code=$?
PID_RUN=""
# un run est complet si son résumé existe sans arrêt consigné, même si le délai externe a frappé pendant la fin du
# processus (code 124 après l'écriture du résumé)
if [ "$code" -ne 0 ]; then
    if [ -f "diag/$RUN/resume.json" ] && [ ! -f "diag/$RUN/arret.json" ]; then
        journal "run : code $code, mais résumé écrit sans arrêt consigné : run complet"
    else
        tail -n 5 "$TRAVAIL/run.err" | tee -a "$JOURNAL" || true
        consigner_arret "run (code $code)"; exit 1
    fi
fi
git add "runs/$RUN" "diag/$RUN"
git commit -qm "T0.5 — $ETUDE ($MODE), run $RUN"
journal "run terminé : $RUN ; $(cat "$TRAVAIL/run.json")"
ETAPE="poussée"
pousser || journal "poussée du run impossible : résultats restés sur l'instance"
if [ "$ETUDE" = pilote ]; then pousser_vecteurs "$RUN" || true; fi
ETAPE="fin"
journal "fin : $RUN ; arrêter l'instance par son identifiant (R10)"
CONSIGNE=1
traces "fin"
pousser
journal "branche $BRANCHE poussée"
