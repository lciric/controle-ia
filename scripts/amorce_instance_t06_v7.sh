#!/usr/bin/env bash
# Amorce de l'instance de T0.6, v7 (nom neuf, R12 ; les v1 à v6 restent telles quelles). Défaut trouvé par E2 (R-1689) : au démarrage d'une instance dont l'heure de
# dépense épuisée (DEP) est déjà passée (troisième démarrage d'A), la minuterie relancée prenait la branche C08 (consigner, puis `PUT stopped`) parce que le marqueur
# `t06-depense-epuisee` manquait, alors que l'amorce demandait la destruction : l'arrêt gagnait (instance « exited », jamais détruite). Correctif étroit, deux gestes :
# (1) AVANT de lancer la minuterie, si DEP est déjà passée, l'amorce pose elle-même le marqueur `t06-depense-epuisee` (l'amorce détruit de toute façon dans ce cas :
# démarrage après DEP, ou second démarrage après DEP) : la branche C08 n'est plus prise ; (2) dans la minuterie, après `consigner`, le `PUT stopped` n'est plus envoyé si
# `t06-detruire` est apparu entre-temps (l'ordre de destruction prime sur l'arrêt). (3) R-1692 (E2-6 non exercé : échéance pendant l'installation, rien sur la branche) : la consignation lancée par la ligne de commande de `t06-consigner.sh` (minuterie : échéance, dépense épuisée ; redémarrages) ajoute un commit « T0.6 : journal de l'instance (<motif>) » qui porte `traces/consignation-…/journal-consignation.txt` (motif, heure, dernière ligne du journal avant la consignation, 400 dernières lignes) et `t06-minuterie-fin.txt` (200 dernières lignes du journal de la minuterie, qui porte la ligne « ÉCHÉANCE … atteinte (C14) ») ; la fin de run normale n'en crée pas (trois commits après l'initial : résultats et données légères, morceaux, traces). Le reste est celui de la v6. Texte de la v6 (conservé) : amorce de l'instance de T0.6, v6.
# Amorce de l'instance de T0.6, v6 (nom neuf, R12 ; les v1 à v5 restent telles quelles). Contre-lecture Opus de la v5 (R-1683) : (1) le message de
# `git sparse-checkout` n'est plus jeté (`2>/dev/null` retiré) : il est gardé et CITÉ dans la ligne de refus (« extraction partielle impossible … : <message> ») ;
# (2) le délai du `checkout` du commit passe de 600 s (v4) à 900 s depuis la v5 : DÉCLARÉ ici ; pire cas du clonage = 900 s (clone) + 900 s (checkout) = 1 800 s ;
# (3) la ligne de début devient « AMORCE T06 v6 DEMARRAGE » ; (4) R-1686 : en mode réel, `torch.cuda.is_available()` faux → `refus` immédiat qui cite la version du pilote (après consignation de la cause sur la branche). Le reste est celui de la v5. Texte de la v5 (conservé) : amorce de l'instance de T0.6, v5. Défaut de chaîne trouvé par l'épreuve E2 (R-1676, R-1677) :
# le `clone --filter=blob:none` de la v4 extrait tout l'arbre de `main` (≈ 3,9 Go) ; l'instance louée n'a reçu que ≈ 1,4 Go en ≈ 19 minutes
# (≈ 10 Mb/s effectifs pour 861 annoncés), le clonage a été tué à 900 s, le refus s'est perdu dans la destruction immédiate. La v5, dans les
# deux modes (jouet, réel) : (1) clonage réduit à ce dont l'instance a besoin : `clone --filter=blob:none --no-checkout`, puis extraction
# partielle (`sparse-checkout`, mode sans cône, liste CHEMINS_CLONAGE ci-dessous, justifiée dans le rapport v7) et `checkout` du commit ;
# (2) le débit du clonage est journalisé (une ligne `AMORCE … : CLONAGE …` : secondes, octets du dépôt `.git`, octets de l'arbre extrait,
# débit en Mo/s, nombre de motifs) ; (3) `refus` et `refus_precoce` annoncent la cause puis ATTENDENT 180 s (constante REFUS_ATTENTE_S ;
# en essai local seulement, REFUS_ATTENTE_ESSAI_S la remplace, 0 par défaut) avant de demander la destruction, pour que la session relève la
# cause dans le journal. Le reste est celui de la v4. Texte de la v4 (conservé) : amorce de l'instance de T0.6, v4. Contre-lecture du lanceur v3, C-V4-1 :
# la fin de run (commits et poussées des résultats, des données légères, des morceaux et des traces ; et les consignations
# d'arrêt) prend le MÊME verrou `flock` que `t06-consigner.sh` (`exec 9>>"$R/t06-consigner.lock"; flock -w 1500 9`),
# relâché avant `arreter_instance` ; `commit_verifie` distingue « rien à committer » (index vide : code 10) d'un commit en
# échec (`index.lock`, autre : réessayé une fois, journalisé « ERREUR DE CHAÎNE », code 1) ; un échec de chaîne en fin de run
# pousse d'abord ce qui existe, puis pose `t06-fin-anormale` (jamais `t06-fin-normale`) et sort en code 1 ; avant de poser
# `t06-fin-normale`, `git status --porcelain -- runs diag donnees traces` doit être vide (sinon `consigner_partiel "fin de run"`,
# puis fin anormale si le reste ne part pas). La consignation de la minuterie attend le verrou jusqu'à 1500 s : son délai
# total passe de 900 s à 2400 s pour qu'une fin de run en cours ne la fasse jamais détruire l'instance avant la poussée.
# Mêmes variables que la v3 ; la branche par défaut devient `calcul/t06-<MODE>-v4`, le run est joué par
# `controle_ia.t06.lanceur_v4`. Texte de la v3 (conservé) : amorce de l'instance de T0.6, v3. Contre-lecture neuve du lanceur v2,
# C-V3-2 (C13 complétée) : la branche du second démarrage (`amorce-depot` présent) passe AVANT les contrôles « démarrage après
# l'échéance » et « démarrage après l'heure de dépense épuisée » : d'abord `t06-consigner.sh` (poussée des commits en attente,
# sous un verrou `flock` partagé avec la minuterie), puis destruction si l'argent est épuisé (marqueur `t06-depense-epuisee`
# ou heure de dépense épuisée passée) ou si l'échéance est passée, sommeil après une fin normale, destruction après un run
# interrompu (comme en v2). Le run est joué par `controle_ia.t06.lanceur_v4` (C-V3-1, C-V3-4). Inchangé de la v2 (contre-lecture
# du lanceur v1) : C01 (relais des seules lignes PROGRES neutres ; toute ligne qui porte un mot d'état de sonde est retenue et
# comptée), C08 (heure de dépense épuisée passée à la création : à cette heure, la minuterie consigne, pousse et demande
# « stopped »), C11 (sous-ensemble d'activations en morceaux ; avant chaque commit, tout fichier de plus de
# MORCEAU_MAX_OCTETS (90 Mo) est retiré de l'index et consigné comme erreur de chaîne ; données légères poussées d'abord
# dans un commit à part, morceaux ensuite), C13 (second démarrage après une fin normale ou une dépense épuisée : poussée
# des commits en attente, puis sommeil, disque lisible par la session, arrêt et destruction par l'identifiant ; après un
# « stopped » obtenu, sommeil au lieu d'une sortie), C14 (à l'échéance, la minuterie consigne et pousse les résultats
# partiels avant la destruction), L11 (fin du GO reçue de la configuration par la session : FIN_GO_UTC_S, vérifiée contre
# `calendrier.fin_go_utc` de la configuration après le clonage ; rien n'est écrit en dur).
# Inchangé de la v1 : AUCUN COUPERET DE TEMPS sur le run ; minuterie de destruction en tout premier, détachée, en bash et
# `curl` (sinon `python3`) seuls ; GO vérifié avant toute installation ; lecture précoce des citations ; poussée initiale
# éprouvée ; tests (nombre attendu cité) ; ligne « RUN MORT » lue par la surveillance.
# Variables (--env) : COMMIT, GH_TOKEN, HF_TOKEN (mode reel), PREREG (défaut prereg/T0.6-organismes-v0-v1.md), BRANCHE
# (défaut calcul/t06-<MODE>-v2), DEPOT_URL, ECHEANCE_UTC_S, FIN_GO_UTC_S, DEPENSE_EPUISEE_UTC_S ; posées par Vast :
# CONTAINER_ID, CONTAINER_API_KEY (jamais affichées). Essai local : RACINE_AMORCE, MODE=jouet, VENV_EXISTANT,
# PREREG_ABSENT=1 (jouet seulement ; CONFIG et TESTS_ATTENDUS donnés ; TESTS_ARGS : sélection des essais, jouet seulement),
# AMORCE_ESSAI_LOCAL=1 (aucune minuterie, aucun appel à Vast : une destruction, un arrêt ou un sommeil demandé s'écrit dans
# un fichier et le script sort), POUSSEE_ATTENTE_S, MINUTERIE_PAS_S, MINUTERIE_REESSAI_S, MINUTERIE_MARGE_S.
set -uo pipefail
R="${RACINE_AMORCE:-/root}"
API=https://console.vast.ai/api/v0
GO_ID=GO-2026-11-02-28
MORCEAU_MAX="${MORCEAU_MAX_OCTETS:-90000000}"
ESSAI="${AMORCE_ESSAI_LOCAL:-0}"
export HOME="${HOME:-/root}" TZ=UTC
cd "$R" || { echo "AMORCE T06 : racine $R inaccessible : sleep infinity pour ne pas boucler"; sleep infinity; exit 1; }
N_DEM=0; [ -s "$R/t06-demarrages.txt" ] && read -r N_DEM < "$R/t06-demarrages.txt"
case "$N_DEM" in ''|*[!0-9]*) N_DEM=0;; esac
N_DEM=$(( N_DEM + 1 )); echo "$N_DEM" > "$R/t06-demarrages.txt"
printf 'AMORCE T06 v7 DEMARRAGE %s : %(%Y-%m-%dT%H:%M:%SZ)T, machine %s, commit %s\n' "$N_DEM" -1 "${CONTAINER_ID:-?}" "${COMMIT:-?}"
IFS= read -r -d '' MINUTERIE_TXT <<'MINUTERIE'
ECH="$1"; DEP="$2"; R="$3"; API="$4"; J="$R/t06-minuterie.log"
PAS="${MINUTERIE_PAS_S:-5}"; REESSAI="${MINUTERIE_REESSAI_S:-60}"; MARGE="${MINUTERIE_MARGE_S:-1800}"
case "$PAS" in ''|*[!0-9]*) PAS=5;; esac; case "$REESSAI" in ''|*[!0-9]*) REESSAI=60;; esac
case "$MARGE" in ''|*[!0-9]*) MARGE=1800;; esac; case "$DEP" in ''|*[!0-9]*) DEP=0;; esac
echo "$(date -u +%FT%TZ) minuterie $$ : échéance $ECH, dépense épuisée à $DEP" >> "$J"
echo "$$" > "$R/t06-minuterie.pid"
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "$(date -u +%FT%TZ) ALARME : identifiant d'instance illisible : aucun geste" >> "$J"; exit 3;; esac
consigner() {  # C14, C08 : résultats partiels committés et poussés par le script écrit par l'amorce (git seul)
    if [ -f "$R/t06-consigner.sh" ]; then timeout -k 10 2400 bash "$R/t06-consigner.sh" "$1" >> "$J" 2>&1; echo "$(date -u +%FT%TZ) consigné ($1) : code $?" >> "$J"
    else echo "$(date -u +%FT%TZ) rien à consigner ($1) : dépôt non extrait" >> "$J"; fi; }
appel() {  # méthode, corps JSON (vide pour DELETE) ; écrit le code HTTP
    local c
    if command -v curl >/dev/null 2>&1; then
        if [ -n "$2" ]; then c=$(curl -sS -m 60 -o "$R/t06-api-corps.txt" -w '%{http_code}' -X "$1" -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" -H 'Content-Type: application/json' -d "$2" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
        else c=$(curl -sS -m 60 -o "$R/t06-api-corps.txt" -w '%{http_code}' -X "$1" -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000; fi
    elif command -v python3 >/dev/null 2>&1; then
        c=$(python3 -I -B -c 'import os, sys, urllib.error, urllib.request
corps = sys.argv[3].encode() if sys.argv[3] else None
q = urllib.request.Request(sys.argv[1], data=corps, method=sys.argv[2], headers={"Authorization": "Bearer " + os.environ.get("CONTAINER_API_KEY", ""), "Content-Type": "application/json"})
try:
    with urllib.request.urlopen(q, timeout=60) as r:
        code, corps = r.status, r.read()
except urllib.error.HTTPError as e:
    code, corps = e.code, e.read()
except Exception:
    code, corps = 0, b""
open(sys.argv[4], "wb").write(corps)
print("%03d" % code)' "$API/instances/$CONTAINER_ID/" "$1" "$2" "$R/t06-api-corps.txt" 2>/dev/null) || c=000
    else c=aucun; fi
    echo "$c"
}
while [ "$(date +%s)" -lt "$ECH" ] && [ ! -e "$R/t06-detruire" ]; do
    if [ "$DEP" -gt 0 ] && [ "$(date +%s)" -ge "$DEP" ] && [ ! -e "$R/t06-depense-epuisee" ]; then
        echo "$(date -u +%FT%TZ) DÉPENSE ÉPUISÉE (C08, plafond de 200 USD cumulé) : consignation, poussée, puis état « stopped »" >> "$J"
        echo "dépense épuisée $(date -u +%FT%TZ)" > "$R/t06-depense-epuisee"
        consigner "dépense épuisée"
        if [ -e "$R/t06-detruire" ]; then echo "$(date -u +%FT%TZ) PUT stopped non envoyé : ordre de destruction de l'amorce reçu pendant la consignation (R-1689)" >> "$J"
        else c=$(appel PUT '{"state": "stopped"}'); echo "$(date -u +%FT%TZ) PUT stopped (dépense épuisée) : HTTP $c" >> "$J"; fi
    fi
    sleep "$PAS"
done
raison="échéance"; [ -e "$R/t06-detruire" ] && raison="ordre de l'amorce"
if [ "$raison" = "échéance" ]; then echo "$(date -u +%FT%TZ) ÉCHÉANCE $ECH atteinte (C14) : consignation et poussée des résultats partiels avant la destruction" >> "$J"; consigner "échéance"; fi
FIN=$(( $(date +%s) + MARGE )); n=0
while :; do
    n=$((n + 1))
    if [ "$n" -gt 1 ] && [ $(( $(date +%s) + 190 )) -gt "$FIN" ]; then
        echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue avant la fin de la marge" >> "$J"; exit 4
    fi
    c=$(appel DELETE '')
    if [ "$c" = aucun ]; then echo "$(date -u +%FT%TZ) ALARME : ni curl ni python3 : aucune destruction possible" >> "$J"; exit 5; fi
    refus=non; grep -qiE '"success"[[:space:]]*:[[:space:]]*false' "$R/t06-api-corps.txt" 2>/dev/null && refus=oui
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
REFUS_ATTENTE_S=180            # R-1677 : constante d'exploitation ; seul l'essai local (AMORCE_ESSAI_LOCAL=1) la remplace par REFUS_ATTENTE_ESSAI_S (0 par défaut)
[ "$ESSAI" = 1 ] && REFUS_ATTENTE_S="${REFUS_ATTENTE_ESSAI_S:-0}"
attente_refus() { echo "AMORCE $(date -u +%FT%TZ) : refus annoncé : destruction demandée dans ${REFUS_ATTENTE_S} s (la session relève la cause dans le journal avant)"; sleep "$REFUS_ATTENTE_S"; }
refus() { echo "AMORCE $(date -u +%FT%TZ) : refus : $1 : rien ne part"; attente_refus; detruire "refus : $1" 2; }
refus_precoce() {  # avant la minuterie : destruction immédiate (minuterie lancée à l'échéance 0), ou fichier posé en essai
    echo "AMORCE $(date -u +%FT%TZ) : refus : $1 : rien ne part"; attente_refus; echo "refus : $1" > "$R/t06-detruire"
    if [ "$ESSAI" = 1 ]; then exit 2; fi
    bash "$R/t06-minuterie.sh" 0 0 "$R" "$API" < /dev/null >> "$R/t06-minuterie.log" 2>&1; sleep infinity; exit 2; }
sommeil() {  # disque lisible par la session ; arrêt et destruction par l'identifiant (R10)
    echo "AMORCE $(date -u +%FT%TZ) : sommeil ($1) : disque lisible, la session arrête et détruit par l'identifiant"
    if [ "$ESSAI" = 1 ]; then echo "sommeil ($1)" > "$R/t06-sommeil"; exit "${2:-0}"; fi
    sleep infinity; exit "${2:-0}"; }
arreter_instance() {  # fin normale : état voulu « stopped » (disque gardé jusqu'au verdict) ; C13 : sommeil après l'arrêt obtenu
    echo "AMORCE $(date -u +%FT%TZ) : fin, code $2"
    if [ "$ESSAI" = 1 ]; then  # essai local : C-V4-1 observe que le verrou de consignation (descripteur 9) est relâché AVANT l'arrêt
        if [ -e "/proc/$$/fd/9" ]; then echo "verrou tenu à l'arrêt ($1)" > "$R/t06-verrou-tenu-a-l-arret"; fi
        echo "stopped ($1)" > "$R/t06-arret-demande"; exit "$2"; fi
    local c corps="$R/t06-arret-corps.txt" ok=non
    if command -v curl >/dev/null 2>&1; then
        c=$(curl -sS -m 60 -o "$corps" -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
            -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2>/dev/null) || c=000
    else c=aucun; fi
    case "$c" in 2??) grep -qiE '"success"[[:space:]]*:[[:space:]]*true' "$corps" 2>/dev/null && ok=oui;; esac
    if [ "$ok" = oui ]; then echo "AMORCE $(date -u +%FT%TZ) : ARRÊT OBTENU (état voulu « stopped », HTTP $c) : sommeil jusqu'à l'arrêt effectif (C13)"; sommeil "arrêt obtenu" "$2"; fi
    echo "AMORCE $(date -u +%FT%TZ) : ARRÊT NON OBTENU (HTTP $c) : le conteneur reste en vie ; la session arrête par l'identifiant (R10)"
    sommeil "arrêt non obtenu" "$2"; }
FIN_GO="${FIN_GO_UTC_S:-}"
case "$FIN_GO" in ''|*[!0-9]*) refus_precoce "FIN_GO_UTC_S absente ou non entière (L11 : fin du GO lue dans la configuration par la session)";; esac
if [ "$ESSAI" != 1 ]; then
    OUTILS="curl git python3 timeout setsid flock sha256sum tar gzip awk sed sort cut tail head mktemp grep date sleep stat"
    manquants() { local o m=""; for o in $OUTILS; do command -v "$o" >/dev/null 2>&1 || m="$m $o"; done; printf '%s' "$m"; }
    paquet() { case "$1" in curl|git|python3|tar|gzip|sed|grep) printf '%s' "$1";; awk) printf gawk;; setsid|flock) printf util-linux;; *) printf coreutils;; esac; }
    MANQ=$(manquants)
    if [ -n "$MANQ" ]; then
        echo "AMORCE T06 : outils absents :$MANQ : installation bornée (apt-get, 300 s par étape)"
        if command -v apt-get >/dev/null 2>&1 && command -v timeout >/dev/null 2>&1; then
            PAQ="ca-certificates"; for o in $MANQ; do PAQ="$PAQ $(paquet "$o")"; done
            DEBIAN_FRONTEND=noninteractive timeout -k 10 300 apt-get update -qq >/dev/null 2>&1 \
                && DEBIAN_FRONTEND=noninteractive timeout -k 10 300 apt-get install -y -qq --no-install-recommends $PAQ >/dev/null 2>&1
            echo "AMORCE T06 : installation ($PAQ) : code $?"
        fi
        MANQ=$(manquants); [ -z "$MANQ" ] || refus_precoce "outils absents :$MANQ"
    fi
fi
E="$R/t06-echeance.txt"; DE="$R/t06-depense-epuisee-utc.txt"
if [ -s "$E" ]; then read -r ECH < "$E"; else
    ECH="${ECHEANCE_UTC_S:-}"
    case "$ECH" in ''|*[!0-9]*) refus_precoce "ECHEANCE_UTC_S absente ou non entière";; esac
    [ "$ECH" -le "$FIN_GO" ] || { echo "AMORCE T06 : échéance ramenée à la fin du GO ($FIN_GO)"; ECH=$FIN_GO; }
    echo "$ECH" > "$E"
fi
if [ -s "$DE" ]; then read -r DEP < "$DE"; else
    DEP="${DEPENSE_EPUISEE_UTC_S:-}"
    case "$DEP" in ''|*[!0-9]*) refus_precoce "DEPENSE_EPUISEE_UTC_S absente ou non entière (C08 : heure d'épuisement des 200 USD, calculée à la création)";; esac
    echo "$DEP" > "$DE"
fi
if [ "$DEP" -gt 0 ] && [ "$(date +%s)" -ge "$DEP" ] && [ ! -e "$R/t06-depense-epuisee" ]; then      # R-1689 : l'argent est déjà épuisé au démarrage, l'amorce détruira
    echo "dépense déjà épuisée au démarrage $(date -u +%FT%TZ) (R-1689)" > "$R/t06-depense-epuisee"
fi
if [ "$ESSAI" != 1 ]; then
    setsid bash "$R/t06-minuterie.sh" "$ECH" "$DEP" "$R" "$API" < /dev/null >> "$R/t06-minuterie.log" 2>&1 &
    PM=$!
    echo "AMORCE T06 : minuterie lancée (échéance $ECH, $(date -u -d "@$ECH" +%FT%TZ 2>/dev/null || echo "?") ; dépense épuisée à $DEP)"
fi
if [ -d "$R/amorce-depot" ]; then
    # C-V3-2 (C13) : second démarrage, AVANT les contrôles d'heure : les commits en attente sont poussés d'abord, quelle que
    # soit l'heure ; puis destruction si l'argent est épuisé ou l'échéance passée (rien ne doit plus coûter), sommeil après
    # une fin normale, destruction après un run interrompu ; jamais un nouveau run
    if [ -e "$R/t06-fin-normale" ] || [ -e "$R/t06-depense-epuisee" ]; then
        echo "AMORCE $(date -u +%FT%TZ) : second démarrage après une fin normale ou une dépense épuisée (C13, C-V3-2) : poussée des commits en attente d'abord"
        [ -f "$R/t06-consigner.sh" ] && timeout -k 10 1200 bash "$R/t06-consigner.sh" "second démarrage"
        if [ -e "$R/t06-depense-epuisee" ] || [ "$(date +%s)" -ge "$DEP" ]; then
            detruire "second démarrage après la dépense épuisée (C08, C-V3-2) : commits en attente poussés, l'argent est épuisé : destruction, pas de sommeil" 0
        fi
        [ "$(date +%s)" -lt "$ECH" ] || detruire "second démarrage après l'échéance (C14, C-V3-2) : commits en attente poussés, destruction" 0
        sommeil "second démarrage après une fin normale, rien ne repart" 0
    fi
    [ -f "$R/t06-consigner.sh" ] && timeout -k 10 1200 bash "$R/t06-consigner.sh" "redémarrage d'un run interrompu"
    refus "redémarrage : dépôt déjà extrait sur le disque (second démarrage d'un run interrompu) : résultats partiels consignés, rien ne repart"
fi
[ "$(date +%s)" -lt "$ECH" ] || detruire "démarrage après l'échéance : aucun calcul"
[ "$(date +%s)" -lt "$DEP" ] || detruire "démarrage après l'heure de dépense épuisée (C08) : aucun calcul"
for v in COMMIT GH_TOKEN; do [ -n "${!v:-}" ] || refus "$v absent"; done
MODE="${MODE:-reel}"
case "$MODE" in reel|jouet) ;; *) refus "MODE=$MODE (reel ou jouet)";; esac
[ "$MODE" = reel ] && { [ -n "${HF_TOKEN:-}" ] || refus "HF_TOKEN absent en mode reel"; }
case "$COMMIT" in *[!0-9a-f]*|'') refus "COMMIT illisible";; esac
[ "${#COMMIT}" = 40 ] || refus "COMMIT de 40 caractères attendu"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"; export DEPOT_URL
PREREG="${PREREG:-prereg/T0.6-organismes-v0-v1.md}"
BRANCHE="${BRANCHE:-calcul/t06-$MODE-v4}"
PREREG_ABSENT="${PREREG_ABSENT:-0}"
# C-V4-3 : épreuves à blanc E2 et E3 (GO-2026-11-06-01, aucune donnée décisive) : EPREUVE_GO_ID, sans préenregistrement, branche essai/…
EPREUVE_GO="${EPREUVE_GO_ID:-}"
if [ -n "$EPREUVE_GO" ]; then
    [ "$EPREUVE_GO" = GO-2026-11-06-01 ] || refus "EPREUVE_GO_ID=$EPREUVE_GO : seul GO-2026-11-06-01 est une épreuve à blanc"
    [ "$PREREG_ABSENT" = 1 ] || refus "épreuve à blanc : PREREG_ABSENT=1 exigé (une épreuve n'est jamais décisive)"
    case "$BRANCHE" in essai/*) ;; *) refus "épreuve à blanc : la branche doit commencer par essai/ ($BRANCHE) : jamais calcul/";; esac
    [ -n "${CONFIG:-}" ] || refus "épreuve à blanc : CONFIG exigé"
    GO_ID="$EPREUVE_GO"
fi
[ "$PREREG_ABSENT" = 1 ] && [ "$MODE" != jouet ] && [ -z "$EPREUVE_GO" ] && refus "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1) ou pour une épreuve à blanc sous GO-2026-11-06-01"
[ -n "${TESTS_ARGS:-}" ] && [ "$PREREG_ABSENT" != 1 ] && refus "TESTS_ARGS n'est permis qu'en répétition jouet sans préenregistrement"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT"
# R-1677 : clonage réduit. Chemins nécessaires à l'instance (mode sans cône ; motifs de type gitignore) :
#  - code et essais joués par l'amorce : /src/ /tests/ /scripts/ /.claude/ /pyproject.toml /requirements-*.txt ;
#  - préenregistrement, configurations, tâches, consignes et leurs sceaux (clés citées) : /prereg/ /donnees/ /docs/notes/ ;
#  - registre des GO lu par l'amorce et par les essais : /registres/*.md (jamais /registres/passations/, 191 Mo) ;
#  - ce que lisent les essais de la suite complète (chemins relevés par recherche dans tests/ src/ scripts/ et confirmés par l'essai de
#    la suite complète sur un clone réduit) : /diag/ /runs/ /traces/ /docs/*.md /docs/*.txt /docs/*.sha256 /docs/procedures/ /docs/decisions/
#    /docs/verdicts/ /docs/etat-de-l-art/, les petits dossiers de /docs/sources/ cités par les essais, et les trois dossiers d'ordres d'épreuve
#    /brouillons/ordres-t06-e2-e3-v{2,3,4,5}/ (les essais v6 à v8 comparent les filtres des ordres à ceux du lanceur ; quelques Ko) ;
#  - exclus : /docs/sources/pdf/ (1,85 Go de PDF de tiers) et le reste de /docs/sources/, /registres/passations/, /brouillons/, /livrables/, /gemini/, /papiers/.
CHEMINS_CLONAGE='/.claude/
/src/
/tests/
/scripts/
/pyproject.toml
/requirements-*.txt
/prereg/
/donnees/
/diag/
/runs/
/traces/
/registres/*.md
/docs/*.md
/docs/*.txt
/docs/*.sha256
/docs/notes/
/docs/procedures/
/docs/decisions/
/docs/verdicts/
/docs/etat-de-l-art/
/docs/sources/invites-2606.07054-v1/
/docs/sources/invites-2606.08892-v1/
/docs/sources/cartes-modeles-20261006/
/docs/sources/donnees-T0.7/
/brouillons/ordres-t06-e2-e3-v2/
/brouillons/ordres-t06-e2-e3-v3/
/brouillons/ordres-t06-e2-e3-v4/
/brouillons/ordres-t06-e2-e3-v5/'
T_CLONE0=$(date +%s)
timeout -k 10 900 git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout "$DEPOT_URL" "$R/amorce-depot" || refus "clonage impossible (jeton GitHub ?)"
git -C "$R/amorce-depot" config credential.helper "$AIDE"
git -C "$R/amorce-depot" config user.name "instance de calcul (T0.6)"
git -C "$R/amorce-depot" config user.email "instance-calcul@invalid"
SP_MSG=$(git -C "$R/amorce-depot" sparse-checkout init --no-cone 2>&1) || refus "extraction partielle impossible (sparse-checkout init) : $(printf '%s' "$SP_MSG" | head -c 300 | tr '\n' ' ')"
SP_MSG=$(printf '%s\n' "$CHEMINS_CLONAGE" | git -C "$R/amorce-depot" sparse-checkout set --no-cone --stdin 2>&1) || refus "extraction partielle impossible (sparse-checkout set) : $(printf '%s' "$SP_MSG" | head -c 300 | tr '\n' ' ')"
[ -z "$SP_MSG" ] || echo "AMORCE $(date -u +%FT%TZ) : sparse-checkout : $(printf '%s' "$SP_MSG" | head -c 200 | tr '\n' ' ')"
timeout -k 10 900 git -C "$R/amorce-depot" checkout -q "$COMMIT" || refus "commit $COMMIT introuvable"
T_CLONE1=$(date +%s)
CL_S=$(( T_CLONE1 - T_CLONE0 )); [ "$CL_S" -ge 1 ] || CL_S=1
CL_GIT=$(du -sb "$R/amorce-depot/.git" 2>/dev/null | cut -f1); CL_ARBRE=$(du -sb --exclude=.git "$R/amorce-depot" 2>/dev/null | cut -f1)
echo "AMORCE $(date -u +%FT%TZ) : CLONAGE mode=$MODE secondes=$CL_S octets_git=${CL_GIT:-?} octets_arbre=${CL_ARBRE:-?} debit_Mo_s=$(awk -v b="${CL_GIT:-0}" -v a="${CL_ARBRE:-0}" -v s="$CL_S" 'BEGIN {printf "%.2f", (b + a) / s / 1000000}') motifs=$(printf '%s\n' "$CHEMINS_CLONAGE" | grep -c .)"
T="$R/t06"; mkdir -p "$T"
JOURNAL="$T/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-zA-Z0-9_-]+=[^ ]+)+$'
MOTIF_INTERDIT='au-dessus|interpr|échec|echec|aire=|bas=|haut=|ligne_|table_|plancher'
cd "$R/amorce-depot" || refus "dépôt extrait inaccessible"
# script de consignation (C11, C14, C08 ; git seul), lu aussi par la minuterie et par un second démarrage
cat > "$R/t06-consigner.sh" <<CONSIGNER
#!/usr/bin/env bash
# écrit par l'amorce v5 de T0.6 : consigne et pousse les résultats partiels ; git seul, sous verrou ; \$1 = motif
R='$R'; BRANCHE='$BRANCHE'; T='$T'; JOURNAL='$JOURNAL'; MORCEAU_MAX='$MORCEAU_MAX'; POUSSEE_ATTENTE_S='${POUSSEE_ATTENTE_S:-15}'
CONSIGNER
cat >> "$R/t06-consigner.sh" <<'CONSIGNER'
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
pousser() { local essai; for essai in 1 2 3; do timeout -k 10 600 git push -q origin "$BRANCHE" 2>"$T/poussee.err" && return 0; journal "poussée : tentative $essai refusée"; [ "$essai" -lt 3 ] && sleep $((POUSSEE_ATTENTE_S * essai * essai)); done; return 1; }
refuser_gros() {  # C11 : aucun fichier de plus de MORCEAU_MAX octets ne part dans un commit (le dépôt distant le refuserait)
    local f t; while IFS= read -r f; do [ -f "$f" ] || continue; t=$(stat -c %s -- "$f" 2>/dev/null || echo 0)
        if [ "$t" -gt "$MORCEAU_MAX" ]; then git rm -q --cached -- "$f" >/dev/null 2>&1; journal "ERREUR DE CHAÎNE (C11) : $f fait $t octets > $MORCEAU_MAX : retiré du commit, resté sur l'instance"; echo "$f $t" >> "$R/t06-fichiers-trop-gros.txt"; fi
    done < <(git diff --cached --name-only --diff-filter=AM); return 0; }
ajouter() {  # C-V4-1 : un `git add` en échec (index.lock) n'est jamais lu comme « rien à committer » ; code 1 et journal
    git add "$@" 2>"$T/add.err" && return 0
    journal "ERREUR DE CHAÎNE (C-V4-1) : git add en échec ($*) : $(tr '\n' ' ' < "$T/add.err" | cut -c1-200)"; echo "$(date -u +%FT%TZ) git add en échec : $*" >> "$R/t06-erreurs-chaine.txt"; return 1; }
ajouter_legeres() { local f rc=0; for f in donnees/*/adaptateur-*.pt donnees/*/adaptateur-*.pt.sha256 donnees/*/mesures-t06.npz donnees/*/mesures-t06.npz.sha256 \
        donnees/*/textes-actions-t06.jsonl donnees/*/textes-actions-t06.jsonl.sha256 donnees/*/activations-sous-ensemble-t06-manifeste.json \
        donnees/*/activations-sous-ensemble-t06-manifeste.json.sha256; do if [ -f "$f" ]; then ajouter -f "$f" || rc=1; fi; done; return $rc; }
ajouter_morceaux() { local f rc=0; for f in donnees/*/activations-sous-ensemble-t06-[0-9][0-9][0-9].npz donnees/*/activations-sous-ensemble-t06-[0-9][0-9][0-9].npz.sha256; do
        if [ -f "$f" ]; then ajouter -f "$f" || rc=1; fi; done; return $rc; }
commit_verifie() {  # C-V4-1 : 0 = commit fait ; 10 = rien à committer (index vide) ; 1 = commit en échec (réessayé une fois)
    refuser_gros
    local rc essai; git diff --cached --quiet 2>/dev/null; rc=$?
    [ "$rc" = 0 ] && return 10
    if [ "$rc" != 1 ]; then journal "ERREUR DE CHAÎNE (C-V4-1) : lecture de l'index impossible (git diff, code $rc)"; echo "$(date -u +%FT%TZ) lecture de l'index impossible : $1" >> "$R/t06-erreurs-chaine.txt"; return 1; fi
    for essai in 1 2; do
        git commit -qm "$1" >/dev/null 2>"$T/commit.err" && return 0
        journal "ERREUR DE CHAÎNE (C-V4-1) : commit en échec (tentative $essai) : $(tr '\n' ' ' < "$T/commit.err" | cut -c1-200)"
        [ "$essai" = 1 ] && sleep "${COMMIT_ATTENTE_S:-2}"
    done
    echo "$(date -u +%FT%TZ) commit en échec : $1" >> "$R/t06-erreurs-chaine.txt"; return 1; }
etape_commit() {  # $1 = message, $2 = journal si fait, $3 = journal si rien à committer ; rend 0 (fait ou rien) ou 1 (échec de chaîne)
    local rc; commit_verifie "$1"; rc=$?
    case "$rc" in 0) [ -z "$2" ] || journal "$2"; return 0;; 10) [ -z "$3" ] || journal "$3"; return 0;; *) return 1;; esac; }
trace_consignation() {  # R-1692 (E2-6) : le journal de l'instance atteint la branche quand la consignation vient de la minuterie (échéance, dépense épuisée) ou d'un redémarrage ; sinon une échéance pendant l'installation ne laisse RIEN sur la branche
    local d; mkdir -p traces || return 1
    d=$(mktemp -d "traces/consignation-$(date -u +%Y%m%d-%H%M%S)-XXXX") || return 1
    { echo "motif : $1"; echo "heure : $(date -u +%FT%TZ)"; echo "dernière ligne du journal avant la consignation : ${DERNIERE_LIGNE_AVANT:-$(tail -n 1 "$JOURNAL" 2>/dev/null)}" | cut -c1-400
      echo "--- 400 dernières lignes du journal de l'instance (ligne d'échéance et dernière étape atteinte comprises) ---"; tail -n 400 "$JOURNAL" 2>/dev/null | cut -c1-400; } > "$d/journal-consignation.txt"
    [ -f "$R/t06-minuterie.log" ] && tail -n 200 "$R/t06-minuterie.log" | cut -c1-400 > "$d/t06-minuterie-fin.txt"      # la ligne « ÉCHÉANCE … atteinte (C14) » est écrite par la minuterie, pas par l'amorce
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    ajouter "$d" || return 1
    etape_commit "T0.6 : journal de l'instance ($1)" "$1 : journal de l'instance committé" ""; }
consigner_partiel() {  # $1 = motif ; deux commits (données légères d'abord, morceaux ensuite), poussée ; 0 = tout, 1 = poussée impossible, 2 = poussée faite de ce qui existe, mais échec de chaîne
    local echec=0
    ajouter -A runs diag || echec=1
    ajouter_legeres || echec=1
    etape_commit "T0.6 : résultats et données légères ($1)" "$1 : résultats et données légères committés" "$1 : aucun résultat léger à committer" || echec=1
    ajouter_morceaux || echec=1
    etape_commit "T0.6 : sous-ensemble d'activations en morceaux ($1)" "$1 : morceaux committés" "" || echec=1
    if [ "${TRACE_CONSIGNATION:-0}" = 1 ]; then trace_consignation "$1" || echec=1; fi    # fixé par le seul chemin de la ligne de commande (minuterie, redémarrages), jamais par la fin de run
    if pousser; then journal "branche $BRANCHE poussée ($1)"; [ "$echec" = 0 ] && return 0; journal "ERREUR DE CHAÎNE (C-V4-1) : poussée faite de ce qui existe ($1), mais un ajout ou un commit a échoué"; return 2; fi
    journal "poussée impossible ($1) : résultats restés sur l'instance"; return 1; }
if [ "${1:-}" = "--source" ]; then return 0 2>/dev/null || exit 0; fi
exec 9>>"$R/t06-consigner.lock"; flock -w 1500 9 || { echo "verrou de consignation non obtenu ($1)"; exit 1; }
cd "$R/amorce-depot" || { echo "dépôt extrait inaccessible"; exit 1; }
DERNIERE_LIGNE_AVANT=$(tail -n 1 "$JOURNAL" 2>/dev/null)    # étape atteinte avant que la consignation écrive ses propres lignes
TRACE_CONSIGNATION=1 consigner_partiel "$1"
exit $?
CONSIGNER
. "$R/t06-consigner.sh" --source
journal "début v4 : MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE PREREG=$PREREG GO=$GO_ID FIN_GO=$FIN_GO ECHEANCE=$ECH DEPENSE_EPUISEE=$DEP"
SESSION_V2="import sys; sys.path.insert(0, 'src'); from controle_ia.t06 import session_v2; sys.exit(session_v2.main(sys.argv[1:]))"
SESSION_V3="import sys; sys.path.insert(0, 'src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))"
if [ -n "$EPREUVE_GO" ]; then
    GOL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_V3" go registres/go.md "$EPREUVE_GO" 5 2>&1) || refus "$GO_ID non conforme ($GOL)"
else
    GOL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_V2" go registres/go.md 2>&1) || refus "$GO_ID non conforme ($GOL)"
fi
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
# L11 : la fin du GO reçue de la session est celle de la configuration (calendrier vérifié contre le registre des GO)
if [ -n "$EPREUVE_GO" ]; then CAL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_V3" calendrier "$CONFIG" registres/go.md "$EPREUVE_GO" 5 2>&1) || refus "calendrier de la configuration non conforme ($CAL)"
else CAL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_V2" calendrier "$CONFIG" registres/go.md 2>&1) || refus "calendrier de la configuration non conforme ($CAL)"; fi
FIN_CONFIG=$(printf '%s\n' "$CAL" | sed -n 's/.*fin_go_utc_s=\([0-9]*\).*/\1/p' | tail -1)
[ "$FIN_CONFIG" = "$FIN_GO" ] || refus "fin du GO reçue ($FIN_GO) ≠ calendrier.fin_go_utc de la configuration ($FIN_CONFIG) (L11)"
[ "$ECH" -le "$FIN_CONFIG" ] || refus "échéance $ECH après la fin du GO de la configuration ($FIN_CONFIG)"
journal "calendrier : $CAL"
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
traces() { local d; mkdir -p traces; d=$(mktemp -d "traces/t06-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$T/tests.txt" "$T/tests.err" "$T"/run.json "$T"/run.err "$T"/nvidia-smi.txt "$T"/pip-freeze.txt "$R/t06-minuterie.log" "$R/t06-fichiers-trop-gros.txt" "$T/progres-retenues.txt"; do [ -f "$f" ] && cp "$f" "$d/"; done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    ajouter "$d" || return 1; etape_commit "T0.6 : traces de l'instance ($1)" "" "traces : aucun fichier neuf à committer"; }
# C-V4-1 : la fin de run et les consignations d'arrêt prennent le verrou de `t06-consigner.sh` (fd 9) ; il n'est pris qu'APRÈS
# la fin du run et du relais (aucun processus fils ne garde le descripteur) et relâché AVANT `arreter_instance`
prendre_verrou() {  # $1 = motif ; 0 = verrou pris ; 1 = non obtenu en 1500 s (journalisé, la chaîne continue sans lui : poussée au mieux)
    exec 9>>"$R/t06-consigner.lock"
    if flock -w "${VERROU_ATTENTE_S:-1500}" 9; then return 0; fi
    journal "ERREUR DE CHAÎNE (C-V4-1) : verrou de consignation non obtenu ($1)"; echo "$(date -u +%FT%TZ) verrou non obtenu : $1" >> "$R/t06-erreurs-chaine.txt"
    exec 9>&-; return 1; }
liberer_verrou() { exec 9>&-; }
consigner_arret() { prendre_verrou "arrêt pendant $1"; consigner_partiel "arrêt pendant $1"; traces "arrêt pendant $1"; pousser || true; liberer_verrou; }
fin_anormale() {  # C-V4-1 : ce qui existe est déjà poussé ; marqueur, verrou relâché, arrêt de l'instance, code 1
    echo "fin anormale $(date -u +%FT%TZ), run $RUN : $1" > "$R/t06-fin-anormale"; journal "FIN ANORMALE (C-V4-1) : $1"
    liberer_verrou; arreter_instance "fin anormale" 1; }
[ "$MODE" = reel ] && nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv | tee -a "$JOURNAL" "$T/nvidia-smi.txt"
if [ -n "${VENV_EXISTANT:-}" ]; then . "$VENV_EXISTANT/bin/activate"; else
    timeout -k 10 1800 python3.11 -m venv .venv && . .venv/bin/activate && timeout -k 10 3600 pip install -q -r requirements-gpu.txt || { journal "installation impossible"; consigner_arret "installation"; arreter_instance "installation impossible" 1; }
fi
python -m pip freeze --all >"$T/pip-freeze.txt" 2>/dev/null || true
# C-V4-3 : matériel de l'instance (E2-7, E2-8, E3-10) ; ligne neutre relayée par la surveillance (aucun état de sonde)
echo "AMORCE $(date -u +%FT%TZ) : MATERIEL MemTotal_ko=$(awk '/^MemTotal:/ {print $2}' /proc/meminfo 2>/dev/null || echo ?) coeurs=$(nproc 2>/dev/null || echo ?) flock=$(command -v flock >/dev/null 2>&1 && echo oui || echo non)" | tee -a "$JOURNAL"
TESTS_ARGS="${TESTS_ARGS:-}"; TESTS_ARGS="${TESTS_ARGS//,/ }"      # C-V4-3 : la virgule sépare les essais dans la variable d'environnement de Vast (aucun espace permis)
python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())" | tee -a "$JOURNAL"
# R-1686 : garde de la carte, avant tout calcul en mode réel (E2, tentative 2 : « The NVIDIA driver on your system is too old (found version 12020) », torch 2.14.1+cu130,
# cuda_disponible False). Carte invisible → journal (pilote, CUDA de torch, message), consignation de la cause sur la branche, puis `refus` (annonce, 180 s, destruction)
if [ "$MODE" = reel ] && ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)" 2>"$T/torch-cuda.err"; then
    PILOTE=$(nvidia-smi --query-gpu=driver_version --format=csv,noheader 2>/dev/null | head -n 1 | tr -d ' ')
    CUDA_TORCH=$(python -c "import torch; print(torch.version.cuda)" 2>/dev/null | tail -n 1)
    journal "carte invisible pour torch : torch.cuda.is_available() faux ; pilote ${PILOTE:-inconnu} ; CUDA de torch ${CUDA_TORCH:-?} ; message : $(tail -c 300 "$T/torch-cuda.err" 2>/dev/null | tr '\n' ' ')"
    consigner_arret "contrôle de la carte"
    refus "carte invisible pour torch (torch.cuda.is_available() faux) : pilote ${PILOTE:-inconnu}, CUDA de torch ${CUDA_TORCH:-?} : aucun calcul"
fi
if ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no ${TESTS_ARGS:-} >"$T/tests.txt" 2>"$T/tests.err"; then
    tail -n 5 "$T/tests.txt" "$T/tests.err" | tee -a "$JOURNAL"; journal "tests en échec : arrêt"; consigner_arret "tests"; arreter_instance "tests en échec" 1
fi
DERNIERE=$(tail -1 "$T/tests.txt"); journal "tests : $DERNIERE"
if [ -n "$ATTENDUS" ] && ! printf '%s\n' "$DERNIERE" | grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then
    journal "tests : « $DERNIERE » ≠ « $ATTENDUS passed » : arrêt"; consigner_arret "tests"; arreter_instance "nombre de tests" 1
fi
ARGS=(); [ "$PREREG_ABSENT" = 1 ] && journal "répétition sans préenregistrement (jouet ou épreuve à blanc, non décisive)" || ARGS=(--prereg "$PREREG")
RUN="$(date -u +%Y%m%d-%H%M%S)-t06-$MODE"
journal "run : $RUN (sans couperet de temps ; lanceur v4)"
: >"$T/run.err"; : >"$T/progres-retenues.txt"
PYTHONPATH=src python -m controle_ia.t06.lanceur_v4 --config "$CONFIG" --run-id "$RUN" "${ARGS[@]}" >"$T/run.json" 2>>"$T/run.err" &
PID_RUN=$!
# C01 : relais des seules lignes PROGRES bien formées ; une ligne qui porte un mot d'état de sonde n'est pas relayée, elle est comptée
( tail -n +1 -F --pid="$PID_RUN" "$T/run.err" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" | while IFS= read -r ligne; do
    if printf '%s\n' "$ligne" | grep -qiE "$MOTIF_INTERDIT"; then printf '%s\n' "$(date -u +%FT%TZ) PROGRES non relayée : motif interdit (C01)" | tee -a "$JOURNAL" >> "$T/progres-retenues.txt"
    else printf '%s\n' "$ligne" | tee -a "$JOURNAL"; fi; done ) &
PID_RELAIS=$!
code=0; wait "$PID_RUN" || code=$?
wait "$PID_RELAIS" 2>/dev/null || true
if [ "$code" -ne 0 ]; then
    if [ -f "diag/$RUN/resume.json" ] && [ ! -f "diag/$RUN/arret.json" ]; then journal "run : code $code, mais résumé écrit sans arrêt consigné : run complet"
    elif [ -f "diag/$RUN/arret.json" ]; then
        grep -v '^PROGRES ' "$T/run.err" | grep -viE "$MOTIF_INTERDIT" | tail -n 5 | tee -a "$JOURNAL" || true
        consigner_arret "run (code $code)"; arreter_instance "arrêt consigné pendant le run" 1
    else
        grep -v '^PROGRES ' "$T/run.err" | grep -viE "$MOTIF_INTERDIT" | tail -n 5 | tee -a "$JOURNAL" || true
        echo "AMORCE $(date -u +%FT%TZ) : RUN MORT sans résumé ni arrêt consigné (code $code) : arrêt de l'instance par son identifiant (R10)" | tee -a "$JOURNAL"
        consigner_arret "run mort (code $code)"; arreter_instance "run mort" 1
    fi
fi
# C11 : données légères d'abord, dans un commit à part, poussées ; morceaux ensuite ; traces enfin.
# C-V4-1 : tout cela sous le verrou de consignation ; « rien à committer » (code 10) ≠ commit en échec (code 1)
ECHEC=0
prendre_verrou "fin de run" || ECHEC=1
ajouter "runs/$RUN" "diag/$RUN" || ECHEC=1
ajouter_legeres || ECHEC=1
etape_commit "T0.6 ($MODE), run $RUN : résultats et données légères" "" "aucun résultat léger à committer" || ECHEC=1
journal "run terminé : $RUN"
pousser || journal "poussée des résultats impossible : résultats restés sur l'instance"
ajouter_morceaux || ECHEC=1
commit_verifie "T0.6 ($MODE), run $RUN : sous-ensemble d'activations en morceaux (< $MORCEAU_MAX octets chacun)"; rc_m=$?
case "$rc_m" in
    0) journal "morceaux committés : $(git show --stat --format= HEAD | grep -c 'activations-sous-ensemble-t06-[0-9]' || true) fichier(s)"
       pousser || journal "poussée des morceaux impossible : morceaux restés sur l'instance";;
    10) journal "aucun morceau à committer";;
    *) ECHEC=1;;
esac
traces "fin" || ECHEC=1
# un fichier retiré du commit (C11) reste sur l'instance, hors de `git status` si `donnees/` est ignoré : c'est un échec de chaîne
[ ! -s "$R/t06-fichiers-trop-gros.txt" ] || { journal "ERREUR DE CHAÎNE (C-V4-1) : fichier(s) trop gros retiré(s) du commit, restés sur l'instance : $(head -n 3 "$R/t06-fichiers-trop-gros.txt" | tr '\n' ';')"; ECHEC=1; }
if [ "$ECHEC" != 0 ]; then
    pousser || journal "poussée de ce qui existe impossible"
    fin_anormale "un ajout, un commit ou le verrou a échoué en fin de run : poussée de ce qui existe tentée, aucun marqueur de fin normale"
fi
# C-V4-1 : rien ne doit rester hors du dépôt avant la fin normale (fichiers légers, résultats, traces)
RESTE=$(git status --porcelain -- runs diag donnees traces 2>&1)
if [ -n "$RESTE" ]; then
    journal "ERREUR DE CHAÎNE (C-V4-1) : git status --porcelain non vide avant la fin normale ($(printf '%s' "$RESTE" | head -n 3 | tr '\n' ';')) : consignation de rattrapage"
    consigner_partiel "fin de run"
    RESTE=$(git status --porcelain -- runs diag donnees traces 2>&1)
    if [ -n "$RESTE" ]; then pousser || true; fin_anormale "fichiers non consignés après le rattrapage : $(printf '%s' "$RESTE" | head -n 3 | tr '\n' ';')"; fi
fi
AUTRES=$(git status --porcelain 2>&1 | head -n 3 | tr '\n' ';'); [ -z "$AUTRES" ] || journal "note : git status --porcelain (hors runs, diag, donnees, traces) : $AUTRES"
echo "fin normale $(date -u +%FT%TZ), run $RUN" > "$R/t06-fin-normale"
if pousser; then journal "branche $BRANCHE poussée (résultats, données légères, morceaux et traces)"; liberer_verrou; arreter_instance "fin du run" 0; fi
journal "run complet, mais poussée finale impossible après trois tentatives : résultats restés sur l'instance (disque lisible ; un second démarrage repousse, C13)"
liberer_verrou
arreter_instance "poussée impossible" 1
