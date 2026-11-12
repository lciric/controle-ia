#!/bin/bash
# essai_kimi_v1.sh — un seul appel minimal à Kimi par le relais v2, pour lire l'identifiant exact du modèle, le modèle
# servi et le coût (demande (c) du n° 245 de conv-audit). Lignée session-depot, 30 octobre 2026.
#
# Usage, mode réel (dépense : un appel, plafond 0,5 USD ; exige une ligne de GO et la variable KIMI_API_KEY) :
#   GO_ID=GO-AAAA-MM-JJ-NN bash essai_kimi_v1.sh <identifiant-du-modele> <dossier-neuf>
# Usage, à blanc (aucun réseau sortant, aucune vraie clé, aucune dépense : faux amont local, clé factice) :
#   ESSAI_A_BLANC=1 bash essai_kimi_v1.sh kimi-k3.1-pro <dossier-neuf>
#   (MODELE_SERVI_A_BLANC=<autre> fait rendre un autre modèle par le faux amont : le relais doit répondre 502.)
#
# Étapes : (1) `relais_kimi_v2.py --lister-modeles` (un seul GET /v1/models) ; arrêt si l'identifiant n'est pas dans
# la liste ; (2) relais lancé directement, sans setsid ni nohup ($! = PID du processus Python, comparé au `pid` de
# /relais/etat), plafond 0,5 USD, ce seul modèle permis, un appel au plus ; (3) un appel « Réponds OK. », 16 jetons de
# sortie au plus ; (4) n'imprime que le modèle demandé, le modèle servi et le coût lu dans /relais/etat (plus le statut
# et le compte de refus de modèle) ; (5) arrêt du relais par son PID, vérifié mort (R10) ; (6) à la sortie, quelle
# qu'elle soit : recherche de la clé dans les journaux, puis empreintes de tous les fichiers du dossier neuf (R12 : il
# ne doit pas exister avant).
# La clé : présence vérifiée par nom seulement ; transmise aux processus Python par l'environnement d'un sous-shell
# vidé de toute autre variable (jamais en argument, même de `env`, jamais en fichier) ; jamais imprimée.
# Prix (USD par million de jetons) : PRIX_ENTREE, PRIX_SORTIE, PRIX_CACHE, par défaut 2, 10 et 2 (entrée et sortie
# vérifiées, devis `c0620cb6…` ; cache SUPPOSÉ au prix d'entrée, par prudence, faute de prix de cache vérifié).
# Codes : 0 essai conforme ; 2 réglage ou garde ; 3 relais ou faux amont non prêt ; 4 liste illisible ou identifiant
# absent ; 5 relais encore vivant après kill ; 6 clé trouvée dans un journal ; 7 appel non conforme (statut ≠ 200 ou
# modèle servi ≠ modèle demandé).
set -uo pipefail; set +x
ICI=$(cd "$(dirname "$0")" && pwd)
MODELE=${1:-}; SORTIE=${2:-}
[ -n "$MODELE" ] && [ -n "$SORTIE" ] || { echo "usage : $0 <identifiant-du-modele> <dossier-neuf>" >&2; exit 2; }
[[ "$MODELE" =~ ^[A-Za-z0-9._:-]+$ ]] || { echo "identifiant de modèle invalide" >&2; exit 2; }
[ ! -e "$SORTIE" ] || { echo "$SORTIE existe déjà (R12)" >&2; exit 2; }
if [ "${ESSAI_A_BLANC:-}" = 1 ]; then MODE="à blanc"; else
  MODE="réel"
  [ -n "${GO_ID:-}" ] || { echo "GO_ID absent : aucune dépense sans ligne de GO" >&2; exit 2; }
  [ -n "${KIMI_API_KEY:-}" ] || { echo "KIMI_API_KEY absente de l'environnement" >&2; exit 2; }
fi
(cd "$ICI" && sha256sum -c --quiet relais_kimi_v2.py.sha256) || { echo "relais_kimi_v2.py non conforme à son empreinte" >&2; exit 2; }
PRIX_ENTREE=${PRIX_ENTREE:-2}; PRIX_SORTIE=${PRIX_SORTIE:-10}; PRIX_CACHE=${PRIX_CACHE:-2}
PY=/usr/bin/python3
PROXY=${HTTPS_PROXY:-}; CA=${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}
PID_FAUX=""; PID_R=""

# Lance une commande dans un environnement vidé : PATH, LANG et, si demandé, le proxy, le certificat et la clé.
# La fonction finit par `exec` : elle s'appelle toujours dans un sous-shell, soit en arrière-plan (`propre … &`, un seul
# fork, que `exec` remplace par Python : `$!` est le PID du processus Python, comparé ensuite au `pid` de /relais/etat),
# soit entre parenthèses (`(propre …)`) au premier plan. Jamais de parenthèses autour de son corps : le double fork
# laissait un Python orphelin (vu à l'essai à blanc du 30 octobre, attrapé par la comparaison des PID).
propre() {  # propre <avec-cle:0|1> commande…
  local avec_cle=$1; shift
  for v in $(compgen -e); do case $v in KIMI_API_KEY) ;; *) unset "$v" 2>/dev/null || export -n "$v" 2>/dev/null;; esac; done
  export PATH=/usr/bin:/bin LANG=C.UTF-8
  if [ "$avec_cle" = 1 ]; then
    export HTTPS_PROXY="$PROXY" SSL_CERT_FILE="$CA"
    [ "$MODE" = "à blanc" ] && export KIMI_API_KEY="sk-factice-essai-a-blanc"
  else unset KIMI_API_KEY; fi
  exec "$@"
}

fin() {  # à toute sortie : arrêts restants, recherche de la clé, empreintes
  local rc=$?
  [ -n "$PID_R" ] && kill "$PID_R" 2>/dev/null
  [ -n "$PID_FAUX" ] && kill "$PID_FAUX" 2>/dev/null
  if [ -d "$SORTIE" ] && [ ! -e "$SORTIE/EMPREINTES-essai.txt" ]; then
    echo "fin_utc: $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$SORTIE/essai.txt"; echo "code_sortie: $rc" >> "$SORTIE/essai.txt"
    if [ "$MODE" = "réel" ] && grep -rqF -- "$KIMI_API_KEY" "$SORTIE"; then
      echo "clé trouvée dans un journal de $SORTIE : à purger avant tout envoi" >&2; rc=6; fi
    (cd "$SORTIE" && sha256sum $(ls) > EMPREINTES-essai.txt)
  fi
  exit $rc
}
trap fin EXIT
mkdir -p "$SORTIE" && chmod 700 "$SORTIE"
{ echo "mode: $MODE"; echo "go: ${GO_ID:-aucun}"; echo "modele_demande: $MODELE"
  echo "prix_usd_par_million: entree $PRIX_ENTREE, sortie $PRIX_SORTIE, cache $PRIX_CACHE"
  echo "relais: relais_kimi_v2.py $(cut -c1-16 "$ICI/relais_kimi_v2.py.sha256")…"
  echo "debut_utc: $(date -u +%Y-%m-%dT%H:%M:%SZ)"; } > "$SORTIE/essai.txt"

if [ "$MODE" = "à blanc" ]; then
  propre 0 "$PY" -I -B "$ICI/faux_amont_kimi_v1.py" ${MODELE_SERVI_A_BLANC:+--modele-servi "$MODELE_SERVI_A_BLANC"} \
    > "$SORTIE/faux-amont.log" 2>&1 &
  PID_FAUX=$!
  for i in $(seq 1 50); do grep -q "faux amont prêt" "$SORTIE/faux-amont.log" 2>/dev/null && break; sleep 0.1; done
  AMONT=$(awk '/faux amont prêt/ {print $NF}' "$SORTIE/faux-amont.log")
  [ -n "$AMONT" ] || { echo "faux amont non prêt" >&2; exit 3; }
else
  AMONT=https://api.moonshot.ai
fi
echo "amont: $AMONT" >> "$SORTIE/essai.txt"

# (1) liste des modèles : un seul GET /v1/models
(propre 1 "$PY" -I -B "$ICI/relais_kimi_v2.py" --lister-modeles --amont "$AMONT" \
  ) > "$SORTIE/modeles.txt" 2> "$SORTIE/modeles.err"
code=$?
[ $code = 0 ] || { echo "liste des modèles : code $code (voir modeles.err)" >&2; echo "liste: echec code $code" >> "$SORTIE/essai.txt"; exit 4; }
grep -qx -- "$MODELE" "$SORTIE/modeles.txt" || { echo "identifiant « $MODELE » absent de la liste (voir modeles.txt)" >&2
  echo "liste: identifiant absent" >> "$SORTIE/essai.txt"; exit 4; }
echo "liste: identifiant present ($(wc -l < "$SORTIE/modeles.txt") modeles)" >> "$SORTIE/essai.txt"

# (2) relais : lancé directement, plafond 0,5, un appel au plus, ce seul modèle permis
propre 1 "$PY" -I -B "$ICI/relais_kimi_v2.py" --port 0 --amont "$AMONT" --modeles-permis "$MODELE" \
  --plafond-usd 0.5 --reserve-par-appel 0.05 --max-appels 1 --max-jetons-sortie-pire-cas 16 \
  --prix-entree "$PRIX_ENTREE" --prix-sortie "$PRIX_SORTIE" --prix-cache "$PRIX_CACHE" \
  --journal "$SORTIE/relais-journal.jsonl" > "$SORTIE/relais.log" 2>&1 &
PID_R=$!
for i in $(seq 1 100); do grep -q "relais prêt sur" "$SORTIE/relais.log" 2>/dev/null && break; sleep 0.1; done
URL=$(awk '/relais prêt sur/ {print $4}' "$SORTIE/relais.log")
[ -n "$URL" ] || { echo "relais non prêt (voir relais.log)" >&2; exit 3; }
PID_ETAT=$(propre 0 "$PY" -I -c "import json,sys,urllib.request; print(json.load(urllib.request.urlopen(sys.argv[1]+'/relais/etat'))['pid'])" "$URL")
[ "$PID_ETAT" = "$PID_R" ] || { echo "PID du relais ($PID_ETAT) ≠ \$! ($PID_R) : arrêt" >&2; exit 3; }
echo "relais_pid: $PID_R (= pid de /relais/etat)" >> "$SORTIE/essai.txt"

# (3) un appel minimal ; (4) seulement modèle demandé, modèle servi, coût
(propre 0 "$PY" -I -c '
import json, sys, urllib.error, urllib.request
url, modele = sys.argv[1], sys.argv[2]
corps = json.dumps({"model": modele, "messages": [{"role": "user", "content": "Réponds OK."}], "max_tokens": 16}).encode()
req = urllib.request.Request(url + "/v1/chat/completions", data=corps, headers={"Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req, timeout=120) as r:
        statut, servi = r.status, json.load(r).get("model")
except urllib.error.HTTPError as e:
    statut, servi = e.code, None
etat = json.load(urllib.request.urlopen(url + "/relais/etat"))
print(json.dumps({"statut": statut, "modele_demande": modele, "modele_servi": servi,
                  "cout_usd": etat.get("depense_usd"), "refus_modele": etat.get("refus_modele")}))
' "$URL" "$MODELE") > "$SORTIE/resultat.json"
cat "$SORTIE/resultat.json"

# (5) arrêt par PID, vérifié
kill "$PID_R"; for i in $(seq 1 50); do kill -0 "$PID_R" 2>/dev/null || break; sleep 0.1; done
kill -0 "$PID_R" 2>/dev/null && { echo "relais $PID_R encore vivant" >&2; exit 5; }
echo "relais_arrete_pid: $PID_R (mort verifiee)" >> "$SORTIE/essai.txt"; PID_R=""
if [ -n "$PID_FAUX" ]; then kill "$PID_FAUX"; PID_FAUX=""; fi

# conformité de l'appel ; (6) recherche de la clé et empreintes dans `fin`
"$PY" -I -c "import json,sys; d=json.load(open(sys.argv[1])); sys.exit(0 if d['statut']==200 and d['modele_servi']==d['modele_demande'] else 7)" "$SORTIE/resultat.json"
