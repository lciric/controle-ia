#!/usr/bin/env bash
# P3-bis (témoin positif planté ; GO-2026-11-02-29) sur l'instance de calcul : mise en place, essais de la liste ciblée, un
# run du lanceur `controle_ia.premier_test_ia.run_v2` (logique de P3 sans échéance), second paquet des sorties brutes,
# poussée des résultats et des traces. Copie de `scripts/p3_instance.sh` (2bfc6939…) sous un nom neuf (R12), avec ces seuls
# écarts (texte de P3-bis, brouillon 6, « Ce que le code et la chaîne doivent changer », point 5) :
#   - aucun `timeout` (le délai externe de 300 minutes de P3 est retiré : « aucun budget de temps qui coupe une étape ») ;
#   - PREREG et BRANCHE par défaut de P3-bis ; lanceur `controle_ia.premier_test_ia.run_v2` ;
#   - essais : la liste ciblée `scripts/essais-cibles-p3bis-v1.txt`, d'empreinte écrite ici (LISTE_SHA256), « N passed »
#     exact, sans essai sauté ni en échec ; liste absente, altérée, vide ou à un chemin illisible : arrêt avant tout essai ;
#   - identifiant du processus du run écrit au journal à son départ, et son code de sortie quand `wait` rend la main ;
#   - nom du processeur, cœurs de l'affinité et fils d'OpenBLAS et de torch écrits au journal ;
#   - second paquet (plan, point 1 ; R-2021) : `donnees/<run>/` entier et `diag/<run>/episodes-p3.json`, avec leurs
#     compagnons, mis en paquet salé par `ouverture_p3bis_v1 fermer-run`, en morceaux d'au plus 90 Mo scellés, relecture
#     vérifiée, avant toute poussée ; jamais ces fichiers en clair : chemins exclus de git dès le clonage
#     (`.git/info/exclude`), garde `exiger-aucun-clair` avant chaque poussée. La poussée des données légères de P3 porte le
#     second paquet au lieu des fichiers en clair. Second paquet en échec : rien en clair n'est poussé, code 5, l'instance
#     reste arrêtée et non détruite jusqu'à la récupération du paquet refait (le run n'est pas rejoué).
# Le reste (lecture précoce des citations, chacune une seule fois ; relais des seules lignes de progression ; branche
# neuve ; poussées à trois tentatives) est celui de P3. Rien ne se lance sans GO consigné.
#
#   COMMIT=<commit de scellement du préenregistrement de P3-bis> bash p3bis_instance.sh
#
# Variables :
#   COMMIT        (obligatoire) commit à extraire ; le lanceur Python vérifie en plus le commit, la configuration, les
#                 tâches, les consignes, les données génériques et l'entropie
#   MODE          reel (défaut) ou jouet (répétition sur processeur)
#   PREREG        défaut prereg/P3-bis-temoin-positif-v1.md ; il cite, une seule fois chacun, « Tests attendus : `N` »,
#                 « Chemin de la configuration de P3 : `…` », « Chemin des tâches de P3 : `…` », « Chemin des consignes de
#                 P3 : `…` », que ce script lit avant toute installation
#   PREREG_ABSENT 1 seulement en mode jouet : répétition sans préenregistrement ; CONFIG et TACHES donnent les chemins
#   DEPOT_URL     défaut https://github.com/lciric/controle-ia-travail.git (dépôt de travail privé ; N-016)
#   GH_TOKEN      jeton GitHub à grain fin ; lu par un assistant d'identification, jamais écrit
#   HF_TOKEN      jeton Hugging Face en lecture (mode reel)
#   BRANCHE       défaut calcul/p3bis-<MODE>-v1 ; une branche qui existe déjà arrête avant tout calcul
#   TESTS_ATTENDUS nombre d'essais attendus (sans préenregistrement seulement)
#   TRAVAIL       défaut $HOME/p3bis
#   VENV_EXISTANT environnement Python déjà prêt à réutiliser (sinon : python3.11 -m venv + requirements-gpu.txt)
set -euo pipefail

: "${COMMIT:?COMMIT obligatoire (commit de scellement du préenregistrement de P3-bis)}"
ETUDE=p3bis
MODE="${MODE:-reel}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE="${BRANCHE:-calcul/p3bis-$MODE-v1}"
PREREG="${PREREG:-prereg/P3-bis-temoin-positif-v1.md}"
TRAVAIL="${TRAVAIL:-$HOME/p3bis}"
PREREG_ABSENT="${PREREG_ABSENT:-0}"
LISTE_TESTS="scripts/essais-cibles-p3bis-v1.txt"
LISTE_SHA256="dce03c1caad4d9e3499cd1dec0d7c9e2c1621b3971620af9ab3eec738ef9bf1f"                          # empreinte de la liste ciblée, écrite en dur (citée par l'empreinte du script)
case "$MODE" in reel|jouet) ;; *) echo "MODE=$MODE : reel ou jouet" >&2; exit 2 ;; esac
if [ "$PREREG_ABSENT" = 1 ] && [ "$MODE" != jouet ]; then
    echo "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1)" >&2; exit 2
fi
# lignes de progression du lanceur recopiées au journal : préfixe fixe, horodatage, puis des couples clé=valeur sans
# espace (nombres, rangs, noms de sondes, empreintes, étapes) ; aucune autre ligne de la sortie d'erreur n'y passe (aucun texte)
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-z_]+=[^ ]+)+$'

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
git config user.name "instance de calcul (P3-bis)"
git config user.email "instance-calcul@invalid"
git checkout -q "$COMMIT"
# fichiers du run jamais suivis en clair (second paquet) : exclus de git dès le clonage, avant tout `git add`
mkdir -p .git/info
printf '%s\n' '/donnees/' '/diag/*/episodes-p3.json' '/diag/*/episodes-p3.json.sha256' >> .git/info/exclude
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

# Lecture précoce du préenregistrement, avant toute installation : chaque citation lue doit y figurer une seule fois
# (relecture du plan de P3, constat 12 : jamais la première occurrence d'un intitulé recopié du pilote)
lire_unique() {
    local n
    n=$(grep -c "$1 : \`" "$PREREG" || true)
    if [ "$n" != 1 ]; then echo ""; return 0; fi
    sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$PREREG"
}
if [ "$PREREG_ABSENT" = 1 ]; then
    ATTENDUS="${TESTS_ATTENDUS:-}"
    : "${CONFIG:?CONFIG obligatoire sans préenregistrement}" "${TACHES:?TACHES obligatoire sans préenregistrement}"
else
    [ -f "$PREREG" ] || { journal "préenregistrement $PREREG absent au commit $COMMIT : arrêt avant l'installation"; exit 2; }
    ATTENDUS=$(lire_unique "Tests attendus")
    [[ "$ATTENDUS" =~ ^[0-9]+$ ]] || { journal "nombre de tests attendus introuvable ou cité plusieurs fois dans $PREREG : arrêt avant l'installation"; exit 2; }
    CONFIG=$(lire_unique "Chemin de la configuration de P3")
    TACHES=$(lire_unique "Chemin des tâches de P3")
    CONSIGNES=$(lire_unique "Chemin des consignes de P3")
    CITES=("$CONFIG" "$TACHES" "$CONSIGNES")
    for f in "${CITES[@]}"; do
        [ -n "$f" ] || { journal "chemin cité introuvable ou cité plusieurs fois dans $PREREG : arrêt avant l'installation"; exit 2; }
        if [ ! -f "$f" ] || [ ! -f "$f.sha256" ]; then
            journal "fichier cité $f ou son sceau absent de l'arbre du commit $COMMIT : arrêt avant l'installation"
            exit 2
        fi
    done
    if ! PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -u -m controle_ia.scellement verifier "${CITES[@]}" \
            >"$TRAVAIL/sceaux.txt" 2>&1; then
        cause=$(grep -v '^OK ' "$TRAVAIL/sceaux.txt" | tail -n 1 || true)
        journal "sceau non conforme parmi les fichiers cités ($cause) : arrêt avant l'installation"
        exit 2
    fi
    journal "préenregistrement lu : $ATTENDUS tests attendus ; configuration $CONFIG ; tâches $TACHES ; consignes $CONSIGNES : présents et scellés"
fi
# liste ciblée des essais, lue avant toute installation : empreinte écrite ici, un chemin tests/test_*.py par ligne
[ -f "$LISTE_TESTS" ] || { journal "liste ciblée $LISTE_TESTS absente : arrêt avant l'installation"; exit 2; }
[ "$(sha256sum "$LISTE_TESTS" | cut -d' ' -f1)" = "$LISTE_SHA256" ] \
    || { journal "empreinte de $LISTE_TESTS ≠ celle du script ($LISTE_SHA256) : arrêt avant l'installation"; exit 2; }
FICHIERS_TESTS=()
while IFS= read -r f; do
    [ -n "$f" ] || continue
    printf '%s\n' "$f" | grep -Eq '^tests/test_[A-Za-z0-9_]+\.py$' \
        || { journal "chemin illisible dans la liste ciblée : $f : arrêt avant l'installation"; exit 2; }
    [ -f "$f" ] || { journal "essai absent du commit : $f : arrêt avant l'installation"; exit 2; }
    FICHIERS_TESTS+=("$f")
done < "$LISTE_TESTS"
[ "${#FICHIERS_TESTS[@]}" -gt 0 ] || { journal "liste ciblée vide : arrêt avant l'installation"; exit 2; }
journal "liste ciblée : ${#FICHIERS_TESTS[@]} fichiers d'essais, $LISTE_TESTS sha256 $LISTE_SHA256"

poussee_initiale=0
for essai in 1 2 3; do
    if git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee-initiale.err"; then poussee_initiale=1; break; fi
    journal "poussée initiale de la branche $BRANCHE : tentative $essai refusée"
    if [ "$essai" -lt 3 ]; then sleep 5; fi
done
if [ "$poussee_initiale" != 1 ]; then
    cause=$( (grep -E '^(fatal|error|remote):' "$TRAVAIL/poussee-initiale.err" || tail -n 2 "$TRAVAIL/poussee-initiale.err") | tr '\n' ' ' || true)
    journal "poussée initiale de la branche $BRANCHE refusée ($cause) : droit d'écriture du jeton ? arrêt avant l'installation"
    exit 2
fi
journal "branche $BRANCHE poussée avant l'installation (droit d'écriture éprouvé)"

RUN=""
OUVERTURE=(python3 -I -B -c 'import sys; sys.path.insert(0, "src"); from controle_ia.premier_test_ia.ouverture_p3bis_v1 import _main; sys.exit(_main(sys.argv[1:]))')
# garde de la poussée : aucun fichier du run en clair dans l'index ni dans le commit (second paquet seulement)
aucun_clair() {
    [ -n "$RUN" ] || return 0
    "${OUVERTURE[@]}" exiger-aucun-clair --run "$RUN" >>"$TRAVAIL/second-paquet.txt" 2>&1
}
pousser() {
    local essai cause
    if ! aucun_clair; then
        journal "fichier du run en clair dans l'index ou le commit : AUCUNE poussée (écart à consigner) ; $(tail -n 1 "$TRAVAIL/second-paquet.txt")"
        return 1
    fi
    for essai in 1 2 3; do
        if git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee.err"; then return 0; fi
        cause=$( (grep -E '^(fatal|error|remote):' "$TRAVAIL/poussee.err" || tail -n 2 "$TRAVAIL/poussee.err") | tr '\n' ' ' || true)
        journal "poussée de la branche $BRANCHE : tentative $essai refusée ($cause)"
        if [ "$essai" -lt 3 ]; then sleep $((15 * essai * essai)); fi
    done
    return 1
}
traces() {
    local d
    mkdir -p traces
    d=$(mktemp -d "traces/p3bis-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" "$TRAVAIL"/run.json "$TRAVAIL"/run.err \
             "$TRAVAIL"/nvidia-smi.txt "$TRAVAIL"/pip-freeze.txt "$TRAVAIL"/processeur.txt "$TRAVAIL"/second-paquet.txt; do
        [ -f "$f" ] && cp "$f" "$d/"
    done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    git add "$d" && git commit -qm "P3-bis : traces de l'instance ($1)" >/dev/null 2>&1 || true
}
# second paquet des fichiers du run (au lieu des données légères de P3, poussées en clair) ; « --partiel » sur un arrêt
SECOND_PAQUET_EN_ECHEC=""
second_paquet() {
    [ -n "$RUN" ] || return 0
    if "${OUVERTURE[@]}" fermer-run --run "$RUN" "$@" >>"$TRAVAIL/second-paquet.txt" 2>&1; then
        journal "second paquet : $(tail -n 1 "$TRAVAIL/second-paquet.txt")"
        return 0
    fi
    SECOND_PAQUET_EN_ECHEC=1
    journal "SECOND PAQUET EN ÉCHEC ($(tail -n 1 "$TRAVAIL/second-paquet.txt")) : aucun fichier du run poussé en clair ; instance à garder arrêtée, non détruite, jusqu'au paquet refait (le run n'est pas rejoué)"
    return 1
}
CONSIGNE=""
consigner_arret() {
    CONSIGNE=1
    if [ -n "$RUN" ] && [ -z "$SECOND_PAQUET_EN_ECHEC" ] && ! ls "diag/$RUN"/paquet-run-ferme-v1.json >/dev/null 2>&1; then
        second_paquet --partiel || true
    fi
    git add -A runs diag 2>/dev/null || true
    if git commit -qm "P3-bis : arrêt pendant $1" >/dev/null 2>&1; then
        journal "ARRÊT pendant $1 : résultats partiels committés (dont arret.json s'il existe ; fichiers du run en second paquet seulement)"
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
    journal "TERM reçu pendant $ETAPE"
    if [ -n "$PID_RUN" ]; then
        kill -TERM "$PID_RUN" 2>/dev/null || true
        wait "$PID_RUN" 2>/dev/null || true
    fi
    consigner_arret "$ETAPE (TERM reçu)" || true
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
OUVERTURE[0]=python
if ! python -m pip freeze --all >"$TRAVAIL/pip-freeze.txt" 2>"$TRAVAIL/pip-freeze.err"; then
    journal "pip freeze impossible (descriptif, sans effet sur le run) : $(tail -n 1 "$TRAVAIL/pip-freeze.err" | tr '\n' ' ')"
fi

python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())" | tee -a "$JOURNAL"
# processeur, cœurs de l'affinité, fils de torch et d'OpenBLAS (PB-9 ; R-679 : identité au bit à fils égaux) ; seules ces
# variables d'environnement nommées sont lues, jamais l'environnement entier
python - <<'EOF' >"$TRAVAIL/processeur.txt" 2>&1 || true
import ctypes, os, re
nom = next((l.split(":", 1)[1].strip() for l in open("/proc/cpuinfo", encoding="utf-8") if l.startswith("model name")), "illisible")
print(f"processeur : {nom}")
print(f"cœurs de l'affinité : {len(os.sched_getaffinity(0))} ; cœurs vus : {os.cpu_count()}")
print("OPENBLAS_NUM_THREADS : " + os.environ.get("OPENBLAS_NUM_THREADS", "non fixé") + " ; OMP_NUM_THREADS : "
      + os.environ.get("OMP_NUM_THREADS", "non fixé"))
import numpy, torch
fils = "illisible"
for chemin in sorted({l.split()[-1] for l in open("/proc/self/maps") if "openblas" in l.lower() and l.split()[-1].startswith("/")}):
    lib = ctypes.CDLL(chemin)
    for f in ("scipy_openblas_get_num_threads64_", "scipy_openblas_get_num_threads", "openblas_get_num_threads64_",
              "openblas_get_num_threads"):
        if hasattr(lib, f):
            fils = f"{getattr(lib, f)()} ({os.path.basename(chemin)}, {f})"
            break
    if fils != "illisible":
        break
print(f"fils d'OpenBLAS de numpy : {fils} ; fils de torch : {torch.get_num_threads()}")
EOF
while IFS= read -r ligne; do journal "$ligne"; done < "$TRAVAIL/processeur.txt"
if [ "$MODE" = reel ] && ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
    journal "carte indisponible pour torch (pilote CUDA trop ancien ?) : arrêt avant les tests"
    consigner_arret "contrôle de la carte"
    exit 1
fi
ETAPE="tests"
if ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no "${FICHIERS_TESTS[@]}" >"$TRAVAIL/tests.txt" 2>"$TRAVAIL/tests.err"; then
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
journal "configuration : $CONFIG ; tâches : $TACHES"
LANCEUR=(controle_ia.premier_test_ia.run_v2 --config "$CONFIG" --taches "$TACHES")
# aucun délai externe (texte de P3-bis, liste d'arrêt : « aucun couperet de temps ») ; le run n'est arrêté que par ses gardes
RUN="$(date -u +%Y%m%d-%H%M%S)-p3bis-$MODE"
ETAPE="run $RUN"
journal "run : $RUN"
code=0
: >"$TRAVAIL/run.err"
PYTHONPATH=src python -m "${LANCEUR[@]}" --run-id "$RUN" "${ARGS[@]}" >"$TRAVAIL/run.json" 2>>"$TRAVAIL/run.err" &
PID_RUN=$!
journal "run : processus $PID_RUN lancé"
# relais des lignes de progression : tail s'arrête de lui-même quand le run se termine (--pid), sans arrêt par motif
( tail -n +1 -F --pid="$PID_RUN" "$TRAVAIL/run.err" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" \
    | while IFS= read -r ligne; do printf '%s\n' "$ligne" | tee -a "$JOURNAL"; done ) &
PID_RELAIS=$!
wait "$PID_RUN" || code=$?
journal "run : processus $PID_RUN fini, code $code"
PID_RUN=""
wait "$PID_RELAIS" 2>/dev/null || true
# un run est complet si son résumé existe sans arrêt consigné
if [ "$code" -ne 0 ]; then
    if [ -f "diag/$RUN/resume.json" ] && [ ! -f "diag/$RUN/arret.json" ]; then
        journal "run : code $code, mais résumé écrit sans arrêt consigné : run complet"
    else
        # diagnostic, comme au pilote : dernières lignes de la sortie d'erreur, hors de toute ligne de progression
        grep -v '^PROGRES ' "$TRAVAIL/run.err" | tail -n 5 | tee -a "$JOURNAL" || true
        consigner_arret "run (code $code)"; exit 1
    fi
fi
ETAPE="second paquet"
if ! second_paquet; then
    CONSIGNE=1
    git add -A runs diag 2>/dev/null || true
    git commit -qm "P3-bis ($MODE), run $RUN : second paquet en échec, aucun fichier du run en clair" >/dev/null 2>&1 || true
    traces "second paquet en échec"
    pousser || journal "poussée impossible : résultats restés sur l'instance"
    exit 5
fi
git add "runs/$RUN" "diag/$RUN"
git commit -qm "P3-bis ($MODE), run $RUN (fichiers du run en second paquet)"
# le résumé reste dans run.json, versé aux traces ; il n'est pas recopié au journal que lit la surveillance
journal "run terminé : $RUN"
ETAPE="poussée"
pousser || journal "poussée du run impossible : résultats restés sur l'instance"
ETAPE="fin"
journal "fin : $RUN ; arrêter puis détruire l'instance par son identifiant, après la vérification des résultats poussés (R10)"
CONSIGNE=1
traces "fin"
if pousser; then
    journal "branche $BRANCHE poussée (résultats et traces)"
else
    journal "run complet, mais poussée finale impossible après trois tentatives : résultats et traces restés sur l'instance"
    exit 1
fi
