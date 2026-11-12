#!/bin/bash
# Lanceur de l'« épreuve fraîche » du pont fiche -> loi v2 (GO-2026-11-01-09, plafond cumulé 5 USD). Rédigé le 1er novembre 2026
# par un sous-agent neuf de session-depot ; jamais lancé par son rédacteur. Protocole : preregistrement-epreuve-pont-v2.md (scellé).
# Version 2 = version 1 (inchangée, R12) : noms des fichiers v2 (lanceur Python v2 : Argon sans reprise interne, témoins scellés
# et inscrits exigés, environnement du run scellé) ; commentaire des clés rendu exact (contre-lecture 1, CL-13 a).
# Usage :
#   GO_ID=GO-2026-11-01-09 bash lancer-epreuve-pont-v2.sh lancer SORTIE [PARALLELE]
#   GO_ID=GO-2026-11-01-09 bash lancer-epreuve-pont-v2.sh reprendre-refus RUN_PRECEDENT PREAMBULE SORTIE [PARALLELE]
# Clés : GEMINI_API_KEY_2 (Argon) donnée au seul processus Python, sous le nom GEMINI_API_KEY que lit appeler_gemini ; KIMI_API_KEY
# donnée au seul relais Kimi local (relais_kimi_v3.py, empreinte vérifiée), PID vérifié (R10), arrêté par trap ; le Python des
# appels ne voit aucune clé Kimi. Aucune clé en argument du Python ni du relais, aucune en fichier. Limite dite (CL-13 a) : les
# clés transitent par la ligne de commande d'`env -i` jusqu'à son `exec`, donc quelques microsecondes dans /proc ; pratique
# commune de tous les lanceurs du dépôt, conteneur à un seul utilisateur ; correction prévue dans une version ultérieure
# (passage par un descripteur ou par l'environnement hérité). Sans `set -e`.
# Codes : 0 fini ; 2 refus de lancer ; 3 relais ; 6 clé trouvée dans une sortie ; autre : code du lanceur Python ou de timeout.
set -uo pipefail; set +x
cd "$(dirname "$0")" || exit 2
D="$PWD"; REPO=/home/user/controle-ia-travail
GO_ID="${GO_ID:?GO_ID absent}"; MODE="${1:?mode : lancer ou reprendre-refus}"
case "$MODE" in
  lancer) S="${2:?sortie}"; PAR="${3:-3}"; EXTRA=() ;;
  reprendre-refus) PREC="${2:?run précédent}"; PRE="${3:?préambule}"; S="${4:?sortie}"; PAR="${5:-3}"
                   EXTRA=(--run-precedent "$PREC" --preambule "$PRE") ;;
  *) echo "mode : lancer ou reprendre-refus" >&2; exit 2 ;;
esac
[ "$GO_ID" = "GO-2026-11-01-09" ] || { echo "l'épreuve ne court que sous GO-2026-11-01-09" >&2; exit 2; }
grep -q "^| $GO_ID |" "$REPO/registres/go.md" || { echo "$GO_ID absent de registres/go.md" >&2; exit 2; }
[ ! -e "$S" ] || { echo "$S existe déjà (R12)" >&2; exit 2; }
PY=/tmp/claude-0/-home-user-controle-ia-travail/4ff7d1a3-3d12-504e-b550-a8bc2f8510b1/scratchpad/collisionneur-venv/bin/python
[ -x "$PY" ] || { echo "Python des appels absent : $PY" >&2; exit 2; }
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
[ -n "${KIMI_API_KEY:-}" ] || { echo "KIMI_API_KEY absente" >&2; exit 2; }
K=$REPO/docs/notes/ideation-organisme-v1/relais-kimi-v1
(cd "$K" && sha256sum -c --quiet relais_kimi_v3.py.sha256) || { echo "relais Kimi v3 non conforme" >&2; exit 2; }
sha256sum -c --quiet lancer_epreuve_pont_v2.py.sha256 tirer_fiches_v2.py.sha256 preregistrement-epreuve-pont-v2.md.sha256 \
  || { echo "lanceur, tirage ou préenregistrement non scellés ou modifiés" >&2; exit 2; }

# Orchestrateur v56 (vraie garde du noyau `proposeur.valider_proposition`, vrai validateur `ideation_v2.valider_fiche_ideation`),
# tiré de la branche de conv-audit (code seulement, jamais une ref donnees/*), empreinte vérifiée avant dépliage.
ZIP=CODE-orchestrateur-pole-v7-v56.zip
SHA_ZIP=29b1b38cfee5e279a06c947fdf1f855628b574e81e44c2d7e48a029151c1b24c
REF=origin/canal/conv-audit-n04:docs/notes/ideation-organisme-v1/orchestrateur-v56/$ZIP
mkdir -p "$S" || exit 2
SA="$(cd "$S" && pwd)"
git -C "$REPO" show "$REF" > "$SA/$ZIP" || { echo "archive v56 introuvable sur la branche" >&2; exit 2; }
echo "$SHA_ZIP  $SA/$ZIP" | sha256sum -c --quiet - || { echo "archive v56 : empreinte non conforme" >&2; exit 2; }
mkdir "$SA/orchestrateur-v56" && python3 -I -B -m zipfile -e "$SA/$ZIP" "$SA/orchestrateur-v56" \
  || { echo "archive v56 non dépliée" >&2; exit 2; }

# Plafond du relais Kimi = ce qui reste sous le plafond cumulé (second barrage ; la garde du lanceur Python est la première).
if [ "$MODE" = "lancer" ]; then PLAF=5; else
  PLAF=$("$PY" -I -B lancer_epreuve_pont_v2.py restant --run-precedent "$PREC") || { echo "dépense précédente illisible" >&2; exit 2; }
fi
PID_K=""; PORT=8802
arreter() { [ -n "$PID_K" ] || return 0; local i=0; kill "$PID_K" 2>/dev/null; while kill -0 "$PID_K" 2>/dev/null && [ $i -lt 20 ]; do sleep 0.5; i=$((i+1)); done; kill -0 "$PID_K" 2>/dev/null && kill -9 "$PID_K" 2>/dev/null; true; }
trap arreter EXIT; trap 'arreter; exit 130' INT TERM HUP
python3 -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',$PORT)) else 1)" || { echo "port $PORT déjà pris" >&2; exit 2; }
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt \
  python3 -I -B "$K/relais_kimi_v3.py" --port $PORT --modeles-permis kimi-k3.1-pro --plafond-usd "$PLAF" --reserve-par-appel 0.05 \
  --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 40 --max-jetons-sortie-pire-cas 24000 --delai-amont-s 1800 \
  --delai-silence-s 600 --journal "$SA/relais-kimi-journal.jsonl" > "$SA/relais-kimi.log" 2>&1 &
PID_K=$!; sleep 1; tr '\0' ' ' < /proc/$PID_K/cmdline | grep -q relais_kimi_v3.py || { echo "PID $PID_K n'est pas le relais (R10)" >&2; exit 3; }
i=0; until python3 -I -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:$PORT/relais/etat', timeout=2)" 2>/dev/null; do
  i=$((i+1)); [ $i -lt 30 ] || { echo "relais Kimi non prêt" >&2; exit 3; }; sleep 1; done

ENVI=(env -i PATH=/usr/bin:/bin HOME="$D" LANG=C.UTF-8 GO_ID="$GO_ID" HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}"
      NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}"
      GEMINI_API_KEY="$GEMINI_API_KEY_2" KIMI_RELAIS_URL="http://127.0.0.1:$PORT")
code=0
"${ENVI[@]}" timeout 7000 "$PY" -I -B lancer_epreuve_pont_v2.py "$MODE" --pole-v56 "$SA/orchestrateur-v56" --sortie "$SA" \
  --parallele "$PAR" "${EXTRA[@]}" || code=$?
for v in GEMINI_API_KEY_2 KIMI_API_KEY; do grep -rqF -- "${!v}" "$SA" 2>/dev/null && { echo "ALERTE : $v trouvée dans une sortie" >&2; code=6; }; done
arreter; trap - EXIT; echo "code $code"; exit $code
