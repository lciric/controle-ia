#!/usr/bin/env bash
# Amorce de l'instance de T0.6 (organisme (ii) par adaptateur, courbe dose–réponse, test croisé ; GO-2026-11-02-28), v1
# (nom neuf, R12). Déclinée de l'amorce et du script d'instance de P3 (`amorce_instance_p3.sh`, `p3_instance.sh`) et de
# l'amorce SPARKS v12 (minuterie de destruction en bash seul, outils installés, destruction sur refus) ; différences :
#   - AUCUN COUPERET DE TEMPS sur le run (GO-2026-11-02-28 ; mots de Lazar du 2 novembre 2026, 18:26 UTC) : le lanceur
#     Python tourne sans `timeout` ; seuls les gestes de mise en place (clonage, installation, tests) sont bornés ;
#   - MINUTERIE DE DESTRUCTION en tout premier, détachée (`setsid`), en bash et `curl` (sinon `python3`) seuls : échéance
#     absolue posée à la création (`ECHEANCE_UTC_S`, au plus la fin du 16 novembre 2026, échéance du GO), gardée sur le
#     disque ; à l'échéance, ou dès que l'amorce pose `t06-detruire` (refus avant le run, redémarrage), DELETE de
#     l'instance par la clé du conteneur, recommencé chaque minute ; jamais d'arrêt par ce code (il tuerait la minuterie) ;
#   - REDÉMARRAGE (Vast relance le conteneur à chaque sortie) : un dépôt déjà extrait sur le disque = second démarrage :
#     rien ne repart, destruction demandée (les résultats d'un run fini ont été poussés ; un run mort a été vu par la
#     session) ;
#   - fin normale : ligne « AMORCE <date> : fin, code N », puis l'instance est mise à l'état « stopped » par l'interface de
#     Vast (disque gardé jusqu'au verdict, 72 h au plus, puis destruction par la session, R10) ; arrêt non obtenu : le
#     conteneur reste en vie (sleep infinity), la session arrête par l'identifiant ;
#   - processus du run mort sans résumé ni arrêt consigné : ligne « AMORCE <date> : RUN MORT … », lue par la surveillance,
#     qui arrête l'instance par son identifiant ; résultats partiels committés et poussés avant ;
#   - lecture précoce des citations du préenregistrement : « Tests attendus », « Chemin de la configuration de T0.6 »,
#     « Chemin des tâches d'évaluation de T0.6 », « Chemin des tâches de distillation de T0.6 », « Chemin des consignes de
#     P3 », chacune une seule fois, fichiers présents et scellés ; GO vérifié par `controle_ia.t06.session go` ;
#   - données légères poussées par ajout forcé : adaptateurs (demi-précision) et sceaux, mesures, textes des actions
#     (dépôt privé seulement), sous-ensemble d'activations, sceaux ; les activations complètes restent sur le disque.
# Variables (--env) : COMMIT, GH_TOKEN, HF_TOKEN (mode reel), PREREG (défaut prereg/T0.6-organismes-v0-v1.md), BRANCHE
# (défaut calcul/t06-<MODE>-v1), DEPOT_URL, ECHEANCE_UTC_S ; posées par Vast : CONTAINER_ID, CONTAINER_API_KEY (jamais
# affichées). Essai local : RACINE_AMORCE, MODE=jouet, VENV_EXISTANT, PREREG_ABSENT=1 (jouet seulement ; CONFIG et
# TESTS_ATTENDUS donnés), AMORCE_ESSAI_LOCAL=1 (aucune minuterie, aucun appel à Vast : une destruction ou un arrêt demandé
# s'écrit dans un fichier et le script sort), MINUTERIE_PAS_S, MINUTERIE_REESSAI_S, MINUTERIE_MARGE_S.
set -uo pipefail
R="${RACINE_AMORCE:-/root}"
API=https://console.vast.ai/api/v0
FIN_GO=1794873600            # 2026-11-17T00:00:00Z : fin du 16 novembre 2026, échéance de GO-2026-11-02-28
GO_ID=GO-2026-11-02-28
ESSAI="${AMORCE_ESSAI_LOCAL:-0}"
export HOME="${HOME:-/root}" TZ=UTC
cd "$R" || { echo "AMORCE T06 : racine $R inaccessible : sleep infinity pour ne pas boucler"; sleep infinity; exit 1; }
N_DEM=0; [ -s "$R/t06-demarrages.txt" ] && read -r N_DEM < "$R/t06-demarrages.txt"
case "$N_DEM" in ''|*[!0-9]*) N_DEM=0;; esac
N_DEM=$(( N_DEM + 1 )); echo "$N_DEM" > "$R/t06-demarrages.txt"
printf 'AMORCE T06 DEMARRAGE %s : %(%Y-%m-%dT%H:%M:%SZ)T, machine %s, commit %s\n' "$N_DEM" -1 "${CONTAINER_ID:-?}" "${COMMIT:-?}"
IFS= read -r -d '' MINUTERIE_TXT <<'MINUTERIE'
ECH="$1"; R="$2"; API="$3"; J="$R/t06-minuterie.log"
PAS="${MINUTERIE_PAS_S:-5}"; REESSAI="${MINUTERIE_REESSAI_S:-60}"; MARGE="${MINUTERIE_MARGE_S:-1800}"
case "$PAS" in ''|*[!0-9]*) PAS=5;; esac; case "$REESSAI" in ''|*[!0-9]*) REESSAI=60;; esac
case "$MARGE" in ''|*[!0-9]*) MARGE=1800;; esac
echo "$(date -u +%FT%TZ) minuterie $$ : échéance $ECH" >> "$J"
echo "$$" > "$R/t06-minuterie.pid"
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "$(date -u +%FT%TZ) ALARME : identifiant d'instance illisible : aucun geste" >> "$J"; exit 3;; esac
supprimer() {
    local c
    if command -v curl >/dev/null 2>&1; then
        c=$(curl -sS -m 60 -o "$R/t06-delete-corps.txt" -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
            "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
    elif command -v python3 >/dev/null 2>&1; then
        c=$(python3 -I -B -c 'import os, sys, urllib.error, urllib.request
q = urllib.request.Request(sys.argv[1], method="DELETE", headers={"Authorization": "Bearer " + os.environ.get("CONTAINER_API_KEY", "")})
try:
    with urllib.request.urlopen(q, timeout=60) as r:
        code, corps = r.status, r.read()
except urllib.error.HTTPError as e:
    code, corps = e.code, e.read()
except Exception:
    code, corps = 0, b""
open(sys.argv[2], "wb").write(corps)
print("%03d" % code)' "$API/instances/$CONTAINER_ID/" "$R/t06-delete-corps.txt" 2>/dev/null) || c=000
    else c=aucun; fi
    echo "$c"
}
while [ "$(date +%s)" -lt "$ECH" ] && [ ! -e "$R/t06-detruire" ]; do sleep "$PAS"; done
raison="échéance"; [ -e "$R/t06-detruire" ] && raison="ordre de l'amorce"
FIN=$(( $(date +%s) + MARGE )); n=0
while :; do
    n=$((n + 1))
    if [ "$n" -gt 1 ] && [ $(( $(date +%s) + 190 )) -gt "$FIN" ]; then
        echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue avant la fin de la marge" >> "$J"; exit 4
    fi
    c=$(supprimer)
    if [ "$c" = aucun ]; then echo "$(date -u +%FT%TZ) ALARME : ni curl ni python3 : aucune destruction possible" >> "$J"; exit 5; fi
    refus=non; grep -qiE '"success"[[:space:]]*:[[:space:]]*false' "$R/t06-delete-corps.txt" 2>/dev/null && refus=oui
    echo "$(date -u +%FT%TZ) DELETE instance $CONTAINER_ID (essai $n, $raison) : HTTP $c, refus dans le corps : $refus" >> "$J"
    case "$c" in 2??) if [ "$refus" = non ]; then echo "$(date -u +%FT%TZ) instance $CONTAINER_ID détruite" >> "$J"; exit 0; fi;; esac
    [ "$(date +%s)" -lt "$FIN" ] || { echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue" >> "$J"; exit 4; }
    sleep "$REESSAI"
done
MINUTERIE
printf '%s' "$MINUTERIE_TXT" > "$R/t06-minuterie.sh" || { echo "AMORCE T06 : minuterie impossible à écrire"; [ "$ESSAI" = 1 ] && exit 1; sleep infinity; exit 1; }
PM=""
attendre_minuterie() { local lim=$(( $(date +%s) + ${MINUTERIE_MARGE_S:-1800} + 120 )); while [ -n "$PM" ] && kill -0 "$PM" 2>/dev/null && [ "$(date +%s)" -lt "$lim" ]; do sleep 2; done; }
detruire() {  # destruction demandée à la minuterie ; essai local : fichier posé, sortie
    echo "$1" > "$R/t06-detruire"; echo "AMORCE $(date -u +%FT%TZ) : destruction demandée ($1)"
    if [ "$ESSAI" = 1 ]; then exit "${2:-2}"; fi
    attendre_minuterie
    local st=124; { [ -n "$PM" ] && ! kill -0 "$PM" 2>/dev/null; } && { wait "$PM" 2>/dev/null; st=$?; }
    [ "$st" = 0 ] && exit "${2:-2}"
    echo "AMORCE $(date -u +%FT%TZ) : destruction non obtenue (minuterie, code $st) : sleep infinity ; la session détruit par l'identifiant"
    sleep infinity; exit "${2:-2}"; }
refus() { echo "AMORCE $(date -u +%FT%TZ) : refus : $1 : rien ne part"; detruire "refus : $1" 2; }
arreter_instance() {  # fin normale : état voulu « stopped » (disque gardé jusqu'au verdict) ; essai local : fichier posé
    echo "AMORCE $(date -u +%FT%TZ) : fin, code $2"
    if [ "$ESSAI" = 1 ]; then echo "stopped ($1)" > "$R/t06-arret-demande"; exit "$2"; fi
    local c corps="$R/t06-arret-corps.txt" ok=non
    if command -v curl >/dev/null 2>&1; then
        c=$(curl -sS -m 60 -o "$corps" -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
            -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2>/dev/null) || c=000
    else c=aucun; fi
    case "$c" in 2??) grep -qiE '"success"[[:space:]]*:[[:space:]]*true' "$corps" 2>/dev/null && ok=oui;; esac
    if [ "$ok" = oui ]; then echo "AMORCE $(date -u +%FT%TZ) : ARRÊT OBTENU (état voulu « stopped », HTTP $c) : le conteneur sort"; sleep 10; exit "$2"; fi
    echo "AMORCE $(date -u +%FT%TZ) : ARRÊT NON OBTENU (HTTP $c) : le conteneur reste en vie ; la session arrête par l'identifiant (R10)"
    sleep infinity; exit "$2"; }
if [ "$ESSAI" != 1 ]; then
    OUTILS="curl git python3 timeout setsid sha256sum tar gzip awk sed sort cut tail head mktemp grep date sleep"
    manquants() { local o m=""; for o in $OUTILS; do command -v "$o" >/dev/null 2>&1 || m="$m $o"; done; printf '%s' "$m"; }
    paquet() { case "$1" in curl|git|python3|tar|gzip|sed|grep) printf '%s' "$1";; awk) printf gawk;; setsid) printf util-linux;; *) printf coreutils;; esac; }
    MANQ=$(manquants)
    if [ -n "$MANQ" ]; then
        echo "AMORCE T06 : outils absents :$MANQ : installation bornée (apt-get, 300 s par étape)"
        if command -v apt-get >/dev/null 2>&1 && command -v timeout >/dev/null 2>&1; then
            PAQ="ca-certificates"; for o in $MANQ; do PAQ="$PAQ $(paquet "$o")"; done
            DEBIAN_FRONTEND=noninteractive timeout -k 10 300 apt-get update -qq >/dev/null 2>&1 \
                && DEBIAN_FRONTEND=noninteractive timeout -k 10 300 apt-get install -y -qq --no-install-recommends $PAQ >/dev/null 2>&1
            echo "AMORCE T06 : installation ($PAQ) : code $?"
        fi
        MANQ=$(manquants); [ -z "$MANQ" ] || { echo "AMORCE $(date -u +%FT%TZ) : refus : outils absents :$MANQ"; bash "$R/t06-minuterie.sh" 0 "$R" "$API" < /dev/null >> "$R/t06-minuterie.log" 2>&1; sleep infinity; exit 2; }
    fi
    E="$R/t06-echeance.txt"
    if [ -s "$E" ]; then read -r ECH < "$E"; else
        ECH="${ECHEANCE_UTC_S:-}"
        case "$ECH" in ''|*[!0-9]*) echo "AMORCE $(date -u +%FT%TZ) : refus : ECHEANCE_UTC_S absente ou non entière"; bash "$R/t06-minuterie.sh" 0 "$R" "$API" < /dev/null >> "$R/t06-minuterie.log" 2>&1; sleep infinity; exit 2;; esac
        [ "$ECH" -le "$FIN_GO" ] || { echo "AMORCE T06 : échéance ramenée à la fin du GO ($FIN_GO)"; ECH=$FIN_GO; }
        echo "$ECH" > "$E"
    fi
    setsid bash "$R/t06-minuterie.sh" "$ECH" "$R" "$API" < /dev/null >> "$R/t06-minuterie.log" 2>&1 &
    PM=$!
    echo "AMORCE T06 : minuterie lancée (échéance $ECH, $(date -u -d "@$ECH" +%FT%TZ 2>/dev/null || echo "?"))"
    [ "$(date +%s)" -lt "$ECH" ] || detruire "démarrage après l'échéance : aucun calcul"
fi
[ -d "$R/amorce-depot" ] && refus "redémarrage : dépôt déjà extrait sur le disque (second démarrage) : rien ne repart"
for v in COMMIT GH_TOKEN; do [ -n "${!v:-}" ] || refus "$v absent"; done
MODE="${MODE:-reel}"
case "$MODE" in reel|jouet) ;; *) refus "MODE=$MODE (reel ou jouet)";; esac
[ "$MODE" = reel ] && { [ -n "${HF_TOKEN:-}" ] || refus "HF_TOKEN absent en mode reel"; }
case "$COMMIT" in *[!0-9a-f]*|'') refus "COMMIT illisible";; esac
[ "${#COMMIT}" = 40 ] || refus "COMMIT de 40 caractères attendu"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"; export DEPOT_URL
PREREG="${PREREG:-prereg/T0.6-organismes-v0-v1.md}"
BRANCHE="${BRANCHE:-calcul/t06-$MODE-v1}"
PREREG_ABSENT="${PREREG_ABSENT:-0}"
[ "$PREREG_ABSENT" = 1 ] && [ "$MODE" != jouet ] && refus "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1)"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT"
timeout -k 10 900 git -c credential.helper="$AIDE" clone -q --filter=blob:none "$DEPOT_URL" "$R/amorce-depot" || refus "clonage impossible (jeton GitHub ?)"
git -C "$R/amorce-depot" config credential.helper "$AIDE"
git -C "$R/amorce-depot" config user.name "instance de calcul (T0.6)"
git -C "$R/amorce-depot" config user.email "instance-calcul@invalid"
timeout -k 10 600 git -C "$R/amorce-depot" checkout -q "$COMMIT" || refus "commit $COMMIT introuvable"
T="$R/t06"; mkdir -p "$T"
JOURNAL="$T/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-zA-Z0-9_-]+=[^ ]+)+$'
cd "$R/amorce-depot" || refus "dépôt extrait inaccessible"
journal "début : MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE PREREG=$PREREG GO=$GO_ID"
# GO vérifié (bibliothèque standard, avant toute installation) ; aucune dépense sans lui
GOL=$(timeout -k 5 120 python3 -I -B -c "import sys; sys.path.insert(0, 'src'); from controle_ia.t06 import session; sys.exit(session.main(sys.argv[1:]))" go registres/go.md 2>&1) \
    || refus "$GO_ID non conforme ($GOL)"
journal "GO : $GOL"
lire_unique() { local n; n=$(grep -c "$1 : \`" "$PREREG" || true); if [ "$n" != 1 ]; then echo ""; return 0; fi; sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$PREREG"; }
if [ "$PREREG_ABSENT" = 1 ]; then
    ATTENDUS="${TESTS_ATTENDUS:-}"; : "${CONFIG:?CONFIG obligatoire sans préenregistrement}"
    CITES=("$CONFIG")
else
    [ -f "$PREREG" ] || refus "préenregistrement $PREREG absent au commit $COMMIT"
    ATTENDUS=$(lire_unique "Tests attendus")
    [[ "$ATTENDUS" =~ ^[0-9]+$ ]] || refus "nombre de tests attendus introuvable ou cité plusieurs fois dans $PREREG"
    CONFIG=$(lire_unique "Chemin de la configuration de T0.6")
    TACHES_E=$(lire_unique "Chemin des tâches d'évaluation de T0.6")
    TACHES_D=$(lire_unique "Chemin des tâches de distillation de T0.6")
    CONSIGNES=$(lire_unique "Chemin des consignes de P3")
    CITES=("$CONFIG" "$TACHES_E" "$TACHES_D" "$CONSIGNES")
fi
for f in "${CITES[@]}"; do
    [ -n "$f" ] || refus "chemin cité introuvable ou cité plusieurs fois dans $PREREG"
    { [ -f "$f" ] && [ -f "$f.sha256" ]; } || refus "fichier cité $f ou son sceau absent de l'arbre du commit $COMMIT"
done
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src timeout -k 5 300 python3 -u -m controle_ia.scellement verifier "${CITES[@]}" >"$T/sceaux.txt" 2>&1 \
    || refus "sceau non conforme parmi les fichiers cités ($(grep -v '^OK ' "$T/sceaux.txt" | tail -n 1 || true))"
journal "citations lues : tests attendus ${ATTENDUS:-?} ; configuration $CONFIG ; fichiers cités présents et scellés"
code_branche=0
timeout -k 5 300 git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>"$T/ls-remote.err" || code_branche=$?
case "$code_branche" in
    0) refus "branche $BRANCHE déjà présente sur le dépôt distant (relancement sous une branche nouvelle)";;
    2) ;;
    *) refus "vérification de la branche $BRANCHE impossible (git ls-remote, code $code_branche)";;
esac
git checkout -q -b "$BRANCHE"
timeout -k 5 300 git push -q origin "$BRANCHE" 2>"$T/poussee-initiale.err" || refus "poussée initiale de la branche $BRANCHE refusée (droit d'écriture du jeton ?)"
journal "branche $BRANCHE poussée avant l'installation (droit d'écriture éprouvé)"
pousser() { local essai; for essai in 1 2 3; do timeout -k 10 600 git push -q origin "$BRANCHE" 2>"$T/poussee.err" && return 0; journal "poussée : tentative $essai refusée"; [ "$essai" -lt 3 ] && sleep $((15 * essai * essai)); done; return 1; }
traces() { local d; mkdir -p traces; d=$(mktemp -d "traces/t06-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$T/tests.txt" "$T/tests.err" "$T"/run.json "$T"/run.err "$T"/nvidia-smi.txt "$T"/pip-freeze.txt "$R/t06-minuterie.log"; do [ -f "$f" ] && cp "$f" "$d/"; done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    git add "$d" && git commit -qm "T0.6 : traces de l'instance ($1)" >/dev/null 2>&1 || true; }
ajouter_donnees() { local f; for f in donnees/*/adaptateur-*.pt donnees/*/adaptateur-*.pt.sha256 donnees/*/mesures-t06.npz donnees/*/mesures-t06.npz.sha256 \
        donnees/*/textes-actions-t06.jsonl donnees/*/textes-actions-t06.jsonl.sha256 donnees/*/activations-sous-ensemble-t06.npz \
        donnees/*/activations-sous-ensemble-t06.npz.sha256; do [ -f "$f" ] && git add -f "$f"; done; return 0; }
consigner_arret() { git add -A runs diag; ajouter_donnees
    if git commit -qm "T0.6 : arrêt pendant $1" >/dev/null 2>&1; then journal "ARRÊT pendant $1 : résultats partiels committés"; else journal "ARRÊT pendant $1 : aucun résultat à committer"; fi
    traces "arrêt pendant $1"; if pousser; then journal "branche $BRANCHE poussée"; else journal "poussée impossible : résultats restés sur l'instance"; fi; }
[ "$MODE" = reel ] && nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv | tee -a "$JOURNAL" "$T/nvidia-smi.txt"
if [ -n "${VENV_EXISTANT:-}" ]; then . "$VENV_EXISTANT/bin/activate"; else
    timeout -k 10 1800 python3.11 -m venv .venv && . .venv/bin/activate && timeout -k 10 3600 pip install -q -r requirements-gpu.txt || { journal "installation impossible"; consigner_arret "installation"; arreter_instance "installation impossible" 1; }
fi
python -m pip freeze --all >"$T/pip-freeze.txt" 2>/dev/null || true
python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())" | tee -a "$JOURNAL"
if [ "$MODE" = reel ] && ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
    journal "carte indisponible pour torch : arrêt avant les tests"; consigner_arret "contrôle de la carte"; arreter_instance "carte indisponible" 1
fi
if ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no >"$T/tests.txt" 2>"$T/tests.err"; then
    tail -n 5 "$T/tests.txt" "$T/tests.err" | tee -a "$JOURNAL"; journal "tests en échec : arrêt"; consigner_arret "tests"; arreter_instance "tests en échec" 1
fi
DERNIERE=$(tail -1 "$T/tests.txt"); journal "tests : $DERNIERE"
if [ -n "$ATTENDUS" ] && ! printf '%s\n' "$DERNIERE" | grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then
    journal "tests : « $DERNIERE » ≠ « $ATTENDUS passed » : arrêt"; consigner_arret "tests"; arreter_instance "nombre de tests" 1
fi
ARGS=(); [ "$PREREG_ABSENT" = 1 ] && journal "répétition sans préenregistrement (jouet, non décisive)" || ARGS=(--prereg "$PREREG")
RUN="$(date -u +%Y%m%d-%H%M%S)-t06-$MODE"
journal "run : $RUN (sans couperet de temps)"
: >"$T/run.err"
PYTHONPATH=src python -m controle_ia.t06.lanceur --config "$CONFIG" --run-id "$RUN" "${ARGS[@]}" >"$T/run.json" 2>>"$T/run.err" &
PID_RUN=$!
( tail -n +1 -F --pid="$PID_RUN" "$T/run.err" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" | while IFS= read -r ligne; do printf '%s\n' "$ligne" | tee -a "$JOURNAL"; done ) &
PID_RELAIS=$!
code=0; wait "$PID_RUN" || code=$?
wait "$PID_RELAIS" 2>/dev/null || true
if [ "$code" -ne 0 ]; then
    if [ -f "diag/$RUN/resume.json" ] && [ ! -f "diag/$RUN/arret.json" ]; then journal "run : code $code, mais résumé écrit sans arrêt consigné : run complet"
    elif [ -f "diag/$RUN/arret.json" ]; then
        grep -v '^PROGRES ' "$T/run.err" | tail -n 5 | tee -a "$JOURNAL" || true
        consigner_arret "run (code $code)"; arreter_instance "arrêt consigné pendant le run" 1
    else
        grep -v '^PROGRES ' "$T/run.err" | tail -n 5 | tee -a "$JOURNAL" || true
        echo "AMORCE $(date -u +%FT%TZ) : RUN MORT sans résumé ni arrêt consigné (code $code) : arrêt de l'instance par son identifiant (R10)" | tee -a "$JOURNAL"
        consigner_arret "run mort (code $code)"; arreter_instance "run mort" 1
    fi
fi
git add "runs/$RUN" "diag/$RUN"; ajouter_donnees
git commit -qm "T0.6 ($MODE), run $RUN" || true
journal "run terminé : $RUN"
pousser || journal "poussée du run impossible : résultats restés sur l'instance"
traces "fin"
if pousser; then journal "branche $BRANCHE poussée (résultats, données légères et traces)"; arreter_instance "fin du run" 0; fi
journal "run complet, mais poussée finale impossible après trois tentatives : résultats restés sur l'instance"
arreter_instance "poussée impossible" 1
