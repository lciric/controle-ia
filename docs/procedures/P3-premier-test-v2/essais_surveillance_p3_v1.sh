#!/usr/bin/env bash
# Banc de la surveillance de P3 et du contrôle à cinq minutes (R5), v1, brouillon 2 : surveiller_p3_v1.sh et
# controle_cinq_minutes_p3_v1.sh joués contre de faux outils de location (aucun service appelé). Décliné du banc de la
# surveillance des notations sous un nom nouveau (R12). Surveillance : fin normale ; instance perdue après la ligne
# « etape=sondes-figees empreinte=… » (la ligne reste au relevé cumulatif) ; échec d'amorce ; redémarrage de l'amorce ;
# plafond à la création + 22 200 s ; outil introuvable ; dossier de sortie existant ; jeton masqué ; état hors ligne
# passager, seul ou alterné avec la marche (jamais terminal) ; réponse illisible de l'état (jamais terminale, CH-14) ;
# jetons absents ou trop courts (code 2, CH-16) ; usage faux. Contrôle à cinq minutes (CH-23) : cas sain ; trop tôt ;
# échec d'amorce ; commit autre ; tests attendus autres ; carte autre ; prix au-dessus de celui de l'offre choisie ;
# prix au-dessus du plafond ; machine autre ; étiquette autre ; instance arrêtée ; branche non poussée ; redémarrage ;
# état illisible ; journal illisible ; jetons absents ; dossier existant ; traces incomplètes ; jeton masqué ; retard
# écrit ; usage faux.
# Usage : essais_surveillance_p3_v1.sh RACINE_NEUVE
set -uo pipefail
E=$(realpath -m "${1:?racine neuve}")
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
HN=${HN:-$BN/p3-v1}
SURV=$HN/surveiller_p3_v1.sh
CINQ=$HN/controle_cinq_minutes_p3_v1.sh
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/bin" "$E/bin-cinq" || exit 2
echo "script éprouvé : surveiller_p3_v1.sh $(sha256sum "$SURV" | cut -d' ' -f1)"
echo "script éprouvé : controle_cinq_minutes_p3_v1.sh $(sha256sum "$CINQ" | cut -d' ' -f1)"
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
JETONS=(HF_TOKEN=factice-hf-0000000 CONTROLE_IA_GITHUB_TOKEN=factice-gi-0000000 GH_TOKEN=factice-gh-0000000)
cat > "$E/bin/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil de location du banc de la surveillance : scénario dans $SCENARIO (tour n : etat-n.txt, logs-n.txt ou logs-n.err)
S=${SCENARIO:?}
case "$1 $2" in
  "show instance")
    n=$(( $(cat "$S/tour" 2>/dev/null || echo 0) + 1 )); echo "$n" > "$S/tour"
    [ -e "$S/etat-illisible-$n" ] && { echo "réponse non JSON (essai)"; exit 0; }
    e=$(cat "$S/etat-$n.txt" 2>/dev/null || cat "$S/etat-defaut.txt" 2>/dev/null || echo running)
    printf '{"actual_status": "%s", "cur_state": "%s", "intended_status": "running", "status_msg": "essai"}\n' "$e" "$( [ "$e" = running ] && echo running || echo stopped)" ;;
  "logs "*)
    n=$(cat "$S/tour"); [ -e "$S/logs-$n.err" ] && { echo "erreur factice : instance injoignable" >&2; exit 1; }
    cat "$S/logs-$n.txt" 2>/dev/null || cat "$S/logs-defaut.txt" ;;
  *) echo "verbe inattendu : $*" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/bin/vastai"
cat > "$E/bin-cinq/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil de location du banc du contrôle à cinq minutes : état (etat.json) et journal (logs.txt, ou logs.err)
S=${SCENARIO:?}
case "$1 $2" in
  "show instance") cat "$S/etat.json" ;;
  "logs "*) [ -e "$S/logs.err" ] && { echo "erreur factice : instance injoignable" >&2; exit 1; }; cat "$S/logs.txt" ;;
  *) echo "verbe inattendu : $*" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/bin-cinq/vastai"
NON_CONFORMES=0
MAINTENANT=$(date -u +%s)
cas() {   # $1 nom, $2 code attendu, $3 motif attendu sur la dernière ligne, $4 création (défaut : maintenant), $5 PATH, $6 jetons (défaut : oui)
    local n=$1 attendu=$2 motif=$3 creation=${4:-$MAINTENANT} chemin=${5:-$E/bin:/usr/bin:/bin} jetons=${6:-oui}
    local d="$E/sortie-$n" c v env_j=()
    [ "$jetons" = oui ] && env_j=("${JETONS[@]}")
    env -i PATH="$chemin" HOME="$E" LANG=C.UTF-8 SCENARIO="$E/scenario-${n%%-*}" INTERVALLE=0 "${env_j[@]}" \
        bash "$SURV" 99999999 "$creation" "$d" > "$E/console-$n.txt" 2>&1; c=$?
    v="CONFORME"
    [ "$c" = "$attendu" ] || v="NON CONFORME (code $c, attendu $attendu)"
    tail -1 "$E/console-$n.txt" | grep -qF -- "$motif" || v="NON CONFORME (motif « $motif » absent de la dernière ligne)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$n : code $c ; $v"
    tail -1 "$E/console-$n.txt" | cut -c1-160 | sed 's/^/    | /'
}
scenario() { mkdir -p "$E/scenario-$1"; }
A1="AMORCE 2026-10-13T08:00:00Z : commit 0123456789abcdef0123456789abcdef01234567"
P1="PROGRES 2026-10-13T09:00:00Z etape=entrainement concept=tromperie principale=tromperie-lineaire-c7 aire_validation=0.91"
P2="PROGRES 2026-10-13T09:40:00Z etape=sondes-figees empreinte=0123456789abcdef sondes=430"
# M00 : fin normale
scenario M00; printf '%s\n%s\n' "$A1" "$P1" > "$E/scenario-M00/logs-1.txt"
printf '%s\n%s\n%s\nAMORCE 2026-10-13T12:00:00Z : fin, code 0\n' "$A1" "$P1" "$P2" > "$E/scenario-M00/logs-2.txt"
cas M00-fin 0 "FIN : AMORCE 2026-10-13T12:00:00Z : fin, code 0"
[ "$(wc -l < "$E/sortie-M00-fin/progres.txt")" = 4 ] && echo "    relevé cumulatif : 4 lignes (début de l'amorce, deux PROGRES, fin de l'amorce), sans doublon d'un tour à l'autre : CONFORME" \
    || { echo "    relevé cumulatif : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# M01 : instance perdue après la ligne des sondes figées : la ligne reste au relevé cumulatif
scenario M01; printf '%s\n%s\n%s\n' "$A1" "$P1" "$P2" > "$E/scenario-M01/logs-1.txt"
touch "$E/scenario-M01/logs-2.err" "$E/scenario-M01/logs-3.err"; echo offline > "$E/scenario-M01/etat-2.txt"; echo offline > "$E/scenario-M01/etat-3.txt"
cas M01-perdue-apres-sondes-figees 0 "ÉTAT TERMINAL"
grep -qxF "$P2" "$E/sortie-M01-perdue-apres-sondes-figees/progres.txt" && grep -qxF "$P2" "$E/sortie-M01-perdue-apres-sondes-figees/journal-dernier.txt" \
    && echo "    ligne des sondes figées gardée au relevé cumulatif et au dernier journal lisible : CONFORME" \
    || { echo "    ligne des sondes figées perdue : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# M02 : échec d'amorce
scenario M02; printf '%s\nAMORCE : clonage impossible (jeton GitHub ?)\n' "$A1" > "$E/scenario-M02/logs-1.txt"
cas M02-echec-d-amorce 0 "ÉCHEC D'AMORCE : AMORCE : clonage impossible"
# M03 : redémarrage de l'amorce (deux lignes « AMORCE <date> : commit », vues à deux tours)
scenario M03; printf '%s\n' "$A1" > "$E/scenario-M03/logs-1.txt"
printf '%s\n' "AMORCE 2026-10-13T08:05:00Z : commit 0123456789abcdef0123456789abcdef01234567" > "$E/scenario-M03/logs-2.txt"
cas M03-redemarrage 0 "REDÉMARRAGE"
# M04 : plafond (création il y a 22 200 s)
scenario M04; printf '%s\n%s\n' "$A1" "$P1" > "$E/scenario-M04/logs-defaut.txt"
cas M04-plafond 0 "PLAFOND : création + 22200 s" "$((MAINTENANT - 22200))"
# M04b : juste avant le plafond, un tour puis la fin : pas de plafond
scenario M04b; printf '%s\n' "$A1" > "$E/scenario-M04b/logs-1.txt"; printf '%s\nAMORCE 2026-10-13T12:00:00Z : fin, code 1\n' "$A1" > "$E/scenario-M04b/logs-2.txt"
cas M04b-avant-le-plafond 0 "FIN" "$((MAINTENANT - 22100))"
# M05 : outil introuvable
scenario M05; cas M05-outil-introuvable 2 "outil de location introuvable" "$MAINTENANT" /usr/bin:/bin
# M06 : dossier de sortie existant
scenario M06; mkdir -p "$E/sortie-M06-dossier-existant"; cas M06-dossier-existant 2 "existe déjà (R12)"
# M07 : jeton dans le journal : masqué au relevé
scenario M07; printf '%s\nPROGRES 2026-10-13T09:00:00Z etape=episodes lot=1/30 actions=80\nfuite factice-gh-0000000 factice-hf-0000000\nAMORCE 2026-10-13T12:00:00Z : fin, code 0\n' "$A1" > "$E/scenario-M07/logs-1.txt"
cas M07-jeton-masque 0 "FIN"
grep -rqE "factice-(gh|hf)-0000000" "$E/sortie-M07-jeton-masque" && { echo "    JETON AFFI""CHÉ : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); } \
    || echo "    jetons masqués dans les relevés : CONFORME"
# M08 : un seul état hors ligne, puis retour en marche, puis la fin : pas d'état terminal (vu deux fois de suite exigé)
scenario M08; printf '%s\n' "$A1" > "$E/scenario-M08/logs-defaut.txt"; echo offline > "$E/scenario-M08/etat-1.txt"
printf '%s\nAMORCE 2026-10-13T12:00:00Z : fin, code 0\n' "$A1" > "$E/scenario-M08/logs-3.txt"
cas M08-hors-ligne-passager 0 "FIN : AMORCE 2026-10-13T12:00:00Z : fin, code 0"
# M08b : hors ligne, en marche, hors ligne, en marche, puis la fin : le compte repart à zéro à chaque retour en marche
scenario M08b; printf '%s\n' "$A1" > "$E/scenario-M08b/logs-defaut.txt"
echo offline > "$E/scenario-M08b/etat-1.txt"; echo offline > "$E/scenario-M08b/etat-3.txt"
printf '%s\nAMORCE 2026-10-13T12:00:00Z : fin, code 0\n' "$A1" > "$E/scenario-M08b/logs-5.txt"
cas M08b-hors-ligne-alterne 0 "FIN : AMORCE 2026-10-13T12:00:00Z : fin, code 0"
# M10 : réponse non JSON de l'état (deux tours) : relevée « illisible », jamais terminale ; puis la fin (CH-14)
scenario M10; printf '%s\n' "$A1" > "$E/scenario-M10/logs-defaut.txt"; touch "$E/scenario-M10/etat-illisible-1" "$E/scenario-M10/etat-illisible-2"
printf '%s\nAMORCE 2026-10-13T12:00:00Z : fin, code 0\n' "$A1" > "$E/scenario-M10/logs-3.txt"
cas M10-etat-illisible 0 "FIN : AMORCE 2026-10-13T12:00:00Z : fin, code 0"
[ "$(grep -c 'illisible: réponse non JSON' "$E/sortie-M10-etat-illisible/etats.txt" 2>/dev/null)" = 2 ] \
    && echo "    deux états illisibles relevés, sans état terminal : CONFORME" \
    || { echo "    états illisibles : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# M11 : jetons absents ; M11b : jeton trop court (CH-16) : code 2, aucun dossier écrit
scenario M11; cas M11-jetons-absents 2 "masquage impossible" "$MAINTENANT" "$E/bin:/usr/bin:/bin" non
[ ! -e "$E/sortie-M11-jetons-absents" ] && echo "    aucun relevé écrit sans jetons : CONFORME" || { echo "    relevé écrit sans jetons : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
scenario M11b
env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$E/scenario-M11b" INTERVALLE=0 HF_TOKEN=court CONTROLE_IA_GITHUB_TOKEN=factice-gi-0000000 \
    bash "$SURV" 99999999 "$MAINTENANT" "$E/sortie-M11b" > "$E/console-M11b.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$E/console-M11b.txt" | grep -qF "masquage impossible" && [ ! -e "$E/sortie-M11b" ] && echo "M11b-jeton-trop-court : code 2 ; CONFORME" \
    || { echo "M11b-jeton-trop-court : code $c ; NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# M09 : usage faux (identifiant non numérique)
scenario M09
env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E" "${JETONS[@]}" bash "$SURV" abc 123 "$E/sortie-M09" > "$E/console-M09.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$E/console-M09.txt" | grep -qF "usage" && [ ! -e "$E/sortie-M09" ] && echo "M09-usage-faux : code 2 ; CONFORME" \
    || { echo "M09-usage-faux : code $c ; NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# ---- contrôle à cinq minutes (CH-23)
SC=0123456789abcdef0123456789abcdef01234567
traces() {   # $1 dossier, $2 création ; lancement.txt, prereg-S.md et offre.json du lanceur, factices
    mkdir -p "$1"
    printf 'offre choisie : 4242 (1.0933333333333333 USD/h), la moins chère des offres conformes\ncommit %s\noffre 4242\nprereg prereg/P3-premier-test-i-a-v1.md\nbranche calcul/p3-reel-v1\netiquette p3-v1\ngo GO-2026-10-04-08\ncreation %s\n' "$SC" "$2" > "$1/lancement.txt"
    printf '# texte factice\n- Tests attendus : `868`\n' > "$1/prereg-S.md"
    printf '{"id": 4242, "machine_id": 30574, "host_id": 125728, "dph_total": 1.0933333333333333}\n' > "$1/offre.json"
}
journal_sain() {   # $1 fichier
    printf 'AMORCE 2026-10-19T10:00:14Z : commit %s\n2026-10-19T10:00:32Z début : ETUDE=p3 MODE=reel COMMIT=%s BRANCHE=calcul/p3-reel-v1\n2026-10-19T10:00:50Z préenregistrement lu : 868 tests attendus ; configuration prereg/P3-premier-test-config-v1.json\n2026-10-19T10:00:51Z branche calcul/p3-reel-v1 poussée avant l%sinstallation (droit d%sécriture éprouvé)\nname, driver_version, memory.total [MiB]\nNVIDIA A100-SXM4-80GB, 580.159.03, 81920 MiB\n' "$SC" "$SC" "'" "'" > "$1"
}
etat_sain='{"actual_status": "running", "cur_state": "running", "dph_total": 1.0933333333333333, "machine_id": 30574, "host_id": 125728, "gpu_name": "A100 SXM4", "inet_down_cost": 0.0390625, "label": "p3-v1", "extra_env": [["GH_TOKEN", "factice-gh-0000000"]]}'
cinq() {   # $1 nom, $2 code attendu, $3 motif de la dernière ligne, $4 expression sed sur le journal (vide : sain), $5 expression sed sur l'état, $6 âge de la création (s), $7 jetons (oui/non)
    local n=$1 attendu=$2 motif=$3 sj=${4:-} se=${5:-} age=${6:-240} jetons=${7:-oui} c v env_j=()
    local s="$E/cinq-$n" t="$E/cinq-$n/traces"
    mkdir -p "$s"; traces "$t" "$((MAINTENANT - age))"
    journal_sain "$s/logs.txt"; [ -n "$sj" ] && sed -i "$sj" "$s/logs.txt"
    printf '%s\n' "$etat_sain" > "$s/etat.json"; [ -n "$se" ] && sed -i "$se" "$s/etat.json"
    [ "$jetons" = oui ] && env_j=("${JETONS[@]}")
    env -i PATH="$E/bin-cinq:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$s" "${env_j[@]}" \
        bash "$CINQ" 99999999 "$t" "$s/sortie" > "$E/console-cinq-$n.txt" 2>&1; c=$?
    v="CONFORME"
    [ "$c" = "$attendu" ] || v="NON CONF""ORME (code $c, attendu $attendu)"
    tail -1 "$E/console-cinq-$n.txt" | grep -qF -- "$motif" || v="NON CONF""ORME (motif « $motif » absent de la dernière ligne)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$n : code $c ; $(grep -c '^KO' "$E/console-cinq-$n.txt") KO ; $v"
    grep '^KO' "$E/console-cinq-$n.txt" | cut -c1-160 | sed 's/^/    /'
    tail -1 "$E/console-cinq-$n.txt" | cut -c1-160 | sed 's/^/    | /'
}
cinq C00-sain 0 "CONTRÔLE À CINQ MINUTES : CONFORME"
[ -s "$E/cinq-C00-sain/sortie/journal-5min.txt" ] && [ -s "$E/cinq-C00-sain/sortie/controle-5min.txt" ] \
    && echo "    journal à cinq minutes et relevé du contrôle gardés : CONFORME" || { echo "    journal ou relevé absent : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
cinq C01-trop-tot 2 "trop tôt" "" "" 60
[ ! -e "$E/cinq-C01-trop-tot/sortie" ] && echo "    rien d'écrit trop tôt : CONFORME" || { echo "    sortie écrite trop tôt : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
cinq C02-echec-d-amorce 1 "1 KO" '1a AMORCE : clonage impossible (jeton GitHub ?)'
cinq C03-commit-autre 1 "2 KO" "s/$SC/fedcba9876543210fedcba9876543210fedcba98/g"
cinq C04-tests-attendus-autres 1 "1 KO" 's/868 tests attendus/867 tests attendus/'
cinq C05-carte-autre 1 "1 KO" 's/NVIDIA A100-SXM4-80GB, 580.159.03, 81920 MiB/NVIDIA A100-PCIE-40GB, 580.159.03, 40960 MiB/'
cinq C06-prix-au-dessus-du-prix-choisi 1 "1 KO" "" 's/"dph_total": 1.0933333333333333/"dph_total": 1.2/'
cinq C06b-prix-au-dessus-du-plafond 1 "2 KO" "" 's/"dph_total": 1.0933333333333333/"dph_total": 1.35/'
cinq C07-machine-autre 1 "1 KO" "" 's/"machine_id": 30574/"machine_id": 1/'
cinq C08-etiquette-autre 1 "1 KO" "" 's/"label": "p3-v1"/"label": "t05-notations-v1"/'
cinq C09-instance-arretee 1 "1 KO" "" 's/"actual_status": "running"/"actual_status": "exited"/'
cinq C10-branche-non-poussee 1 "1 KO" '/poussée avant l.installation/d'
cinq C11-redemarrage 1 "1 KO" "1a AMORCE 2026-10-19T10:03:00Z : commit $SC"
cinq C12-etat-illisible 1 "1 KO" "" 's/.*/pas du JSON/'
mkdir -p "$E/cinq-C13-journal-illisible"; touch "$E/cinq-C13-journal-illisible/logs.err"
cinq C13-journal-illisible 1 "1 KO"
cinq C14-jetons-absents 2 "masquage impossible" "" "" 240 non
mkdir -p "$E/cinq-C15-dossier-existant/sortie"
cinq C15-dossier-existant 2 "existe déjà (R12)"
cinq C16-jeton-masque 0 "CONFORME" '$a fuite factice-gh-0000000 et factice-hf-0000000'
grep -rqE "factice-(gh|hf)-0000000" "$E/cinq-C16-jeton-masque/sortie" "$E/console-cinq-C16-jeton-masque.txt" \
    && { echo "    JETON AFFI""CHÉ : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); } || echo "    jetons masqués (journal et état) : CONFORME"
cinq C17-retard-ecrit 0 "CONFORME" "" "" 1000
grep -q "^--  contrôle fait après" "$E/console-cinq-C17-retard-ecrit.txt" && echo "    retard écrit : CONFORME" \
    || { echo "    retard non écrit : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# traces incomplètes (offre.json absente) ; usage faux : code 2
mkdir -p "$E/cinq-C18/traces"; traces "$E/cinq-C18/traces" "$((MAINTENANT - 240))"; rm -f "$E/cinq-C18/traces/offre.json"
env -i PATH="$E/bin-cinq:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$E/cinq-C18" "${JETONS[@]}" bash "$CINQ" 99999999 "$E/cinq-C18/traces" "$E/cinq-C18/sortie" > "$E/console-cinq-C18.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$E/console-cinq-C18.txt" | grep -qF "traces du lancement incomplètes" && echo "C18-traces-incompletes : code 2 ; CONFORME" \
    || { echo "C18-traces-incompletes : code $c ; NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
env -i PATH="$E/bin-cinq:/usr/bin:/bin" HOME="$E" "${JETONS[@]}" bash "$CINQ" abc "$E/cinq-C18/traces" "$E/cinq-C19" > "$E/console-cinq-C19.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$E/console-cinq-C19.txt" | grep -qF "usage" && [ ! -e "$E/cinq-C19" ] && echo "C19-usage-faux : code 2 ; CONFORME" \
    || { echo "C19-usage-faux : code $c ; NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# aucun jeton factice dans les sorties des consoles
FUITES=$(grep -lE "factice-(gh|hf|gi)-0000000" "$E"/console-*.txt 2>/dev/null || true)
[ -z "$FUITES" ] && echo "aucun jeton affiché : CONFORME" || { printf '%s\n' $FUITES | sed 's/^/JETON AFFI''CHÉ : /'; NON_CONFORMES=$((NON_CONFORMES + 1)); }
echo "FIN DU BANC DE LA SURVEILLANCE DE P3 ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
