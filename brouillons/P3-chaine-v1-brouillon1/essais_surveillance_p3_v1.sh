#!/usr/bin/env bash
# Banc de la surveillance de P3 (R5) : surveiller_p3_v1.sh joué contre un faux outil de location qui rejoue, tour par
# tour, un scénario d'états et de journaux (aucun service appelé). Décliné du banc de la surveillance des notations sous un
# nom nouveau (R12). Cas : fin normale ; instance perdue après la ligne « etape=sondes-figees empreinte=… » (la ligne reste
# au relevé cumulatif) ; échec d'amorce ; redémarrage de l'amorce ; plafond à la création + 20 400 s ; outil introuvable ;
# dossier de sortie existant ; jeton masqué ; état hors ligne passager, seul ou alterné avec la marche (jamais terminal) ;
# usage faux.
# Usage : essais_surveillance_p3_v1.sh RACINE_NEUVE
set -uo pipefail
E=$(realpath -m "${1:?racine neuve}")
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
HN=${HN:-$BN/p3-v1}
SURV=$HN/surveiller_p3_v1.sh
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/bin" || exit 2
echo "script éprouvé : surveiller_p3_v1.sh $(sha256sum "$SURV" | cut -d' ' -f1)"
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
cat > "$E/bin/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil de location du banc de la surveillance : scénario dans $SCENARIO (tour n : etat-n.txt, logs-n.txt ou logs-n.err)
S=${SCENARIO:?}
case "$1 $2" in
  "show instance")
    n=$(( $(cat "$S/tour" 2>/dev/null || echo 0) + 1 )); echo "$n" > "$S/tour"
    e=$(cat "$S/etat-$n.txt" 2>/dev/null || cat "$S/etat-defaut.txt" 2>/dev/null || echo running)
    printf '{"actual_status": "%s", "cur_state": "%s", "intended_status": "running", "status_msg": "essai"}\n' "$e" "$( [ "$e" = running ] && echo running || echo stopped)" ;;
  "logs "*)
    n=$(cat "$S/tour"); [ -e "$S/logs-$n.err" ] && { echo "erreur factice : instance injoignable" >&2; exit 1; }
    cat "$S/logs-$n.txt" 2>/dev/null || cat "$S/logs-defaut.txt" ;;
  *) echo "verbe inattendu : $*" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/bin/vastai"
NON_CONFORMES=0
MAINTENANT=$(date -u +%s)
cas() {   # $1 nom, $2 code attendu, $3 motif attendu sur la dernière ligne, $4 création (défaut : maintenant), $5 PATH
    local n=$1 attendu=$2 motif=$3 creation=${4:-$MAINTENANT} chemin=${5:-$E/bin:/usr/bin:/bin}
    local d="$E/sortie-$n" c v
    env -i PATH="$chemin" HOME="$E" LANG=C.UTF-8 SCENARIO="$E/scenario-${n%%-*}" INTERVALLE=0 GH_TOKEN=factice-gh-0000000 \
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
# M04 : plafond (création il y a 20 400 s)
scenario M04; printf '%s\n%s\n' "$A1" "$P1" > "$E/scenario-M04/logs-defaut.txt"
cas M04-plafond 0 "PLAFOND : création + 20400 s" "$((MAINTENANT - 20400))"
# M04b : juste avant le plafond, un tour puis la fin : pas de plafond
scenario M04b; printf '%s\n' "$A1" > "$E/scenario-M04b/logs-1.txt"; printf '%s\nAMORCE 2026-10-13T12:00:00Z : fin, code 1\n' "$A1" > "$E/scenario-M04b/logs-2.txt"
cas M04b-avant-le-plafond 0 "FIN" "$((MAINTENANT - 20300))"
# M05 : outil introuvable
scenario M05; cas M05-outil-introuvable 2 "outil de location introuvable" "$MAINTENANT" /usr/bin:/bin
# M06 : dossier de sortie existant
scenario M06; mkdir -p "$E/sortie-M06-dossier-existant"; cas M06-dossier-existant 2 "existe déjà (R12)"
# M07 : jeton dans le journal : masqué au relevé
scenario M07; printf '%s\nPROGRES 2026-10-13T09:00:00Z etape=episodes lot=1/23 actions=80\nfuite factice-gh-0000000\nAMORCE 2026-10-13T12:00:00Z : fin, code 0\n' "$A1" > "$E/scenario-M07/logs-1.txt"
cas M07-jeton-masque 0 "FIN"
grep -rq "factice-gh-0000000" "$E/sortie-M07-jeton-masque" && { echo "    JETON AFFICHÉ : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); } \
    || echo "    jeton masqué dans les relevés : CONFORME"
# M08 : un seul état hors ligne, puis retour en marche, puis la fin : pas d'état terminal (vu deux fois de suite exigé)
scenario M08; printf '%s\n' "$A1" > "$E/scenario-M08/logs-defaut.txt"; echo offline > "$E/scenario-M08/etat-1.txt"
printf '%s\nAMORCE 2026-10-13T12:00:00Z : fin, code 0\n' "$A1" > "$E/scenario-M08/logs-3.txt"
cas M08-hors-ligne-passager 0 "FIN : AMORCE 2026-10-13T12:00:00Z : fin, code 0"
# M08b : hors ligne, en marche, hors ligne, en marche, puis la fin : le compte repart à zéro à chaque retour en marche
# (deux états hors ligne non consécutifs ne font pas un état terminal ; vérification courte de la chaîne, second tour,
# constat 2)
scenario M08b; printf '%s\n' "$A1" > "$E/scenario-M08b/logs-defaut.txt"
echo offline > "$E/scenario-M08b/etat-1.txt"; echo offline > "$E/scenario-M08b/etat-3.txt"
printf '%s\nAMORCE 2026-10-13T12:00:00Z : fin, code 0\n' "$A1" > "$E/scenario-M08b/logs-5.txt"
cas M08b-hors-ligne-alterne 0 "FIN : AMORCE 2026-10-13T12:00:00Z : fin, code 0"
# M09 : usage faux (identifiant non numérique)
scenario M09
env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E" bash "$SURV" abc 123 "$E/sortie-M09" > "$E/console-M09.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$E/console-M09.txt" | grep -qF "usage" && [ ! -e "$E/sortie-M09" ] && echo "M09-usage-faux : code 2 ; CONFORME" \
    || { echo "M09-usage-faux : code $c ; NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
echo "FIN DU BANC DE LA SURVEILLANCE DE P3 ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
