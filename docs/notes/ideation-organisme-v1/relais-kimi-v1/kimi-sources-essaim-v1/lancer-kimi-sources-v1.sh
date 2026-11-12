#!/bin/bash
# Kimi K3.1 Pro avec recherche Web (outil officiel web_search, API Formula) sur les sources de l'essaim et des 722 (conv-audit n° 263),
# consigne v2. GO-2026-10-30-17 (poste 2, ≤ 3 USD). Relais v4 sur le port 8791 (8790 tient le tour bisociation). Arrêt par PID (R10).
set -u
D=/root/ideation-v1/kimi-sources-essaim-v1; R=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1
cd $R || exit 9
[ "${GO_ID:-}" = GO-2026-10-30-17 ] || { echo "GO_ID absent ou faux"; exit 9; }
sha256sum -c --quiet relais_kimi_v4.py.sha256 commande_kimi_recherche_v1.py.sha256 consigne-kimi-sources-essaim-722-v2.md.sha256 || exit 9
python3 -I -c "import socket,sys; sys.exit(0 if socket.socket().connect_ex(('127.0.0.1',8791)) else 1)" || { echo "8791 pris"; exit 9; }
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="$HTTPS_PROXY" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt \
  python3 -I -B relais_kimi_v4.py --port 8791 --modeles-permis kimi-k3.1-pro --plafond-usd 3 --prix-entree 2 --prix-sortie 10 \
  --prix-cache 2 --max-appels 12 --max-recherches 20 --prix-recherche 0.005 --delai-amont-s 1800 --delai-silence-s 600 \
  --journal $D/relais-journal.jsonl > $D/relais.log 2>&1 &
PID=$!; echo $PID > $D/relais.pid
arreter() { kill $PID 2>/dev/null; sleep 1; kill -0 $PID 2>/dev/null && kill -9 $PID; true; }
trap arreter EXIT
sleep 1; tr '\0' ' ' < /proc/$PID/cmdline | grep -q relais_kimi_v4.py || { echo "PID $PID n'est pas le relais"; exit 3; }
for i in $(seq 30); do python3 -I -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8791/relais/etat', timeout=2)" 2>/dev/null && break; sleep 1; done
DEBUT=$(date -u +%FT%TZ)
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PLAFOND_SESSION_USD=3 ROLE_POLE=lecteur_sources timeout 3600 python3 -I -B commande_kimi_recherche_v1.py \
  --url-relais http://127.0.0.1:8791 --max-tours 10 --max-recherches 20 --reasoning-effort high --max-sortie-jetons 32768 \
  --sortie-min-jetons 8192 < consigne-kimi-sources-essaim-722-v2.md > $D/sortie.jsonl 2> $D/sortie.err
CODE=$?
python3 -I -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8791/relais/etat').read().decode()[:1500])" > $D/relais-etat-final.txt 2>/dev/null || true
arreter; trap - EXIT
printf 'go: GO-2026-10-30-17 (poste 2)\ndebut_utc: %s\nfin_utc: %s\ncode: %s\npid_relais_arrete: %s\n' "$DEBUT" "$(date -u +%FT%TZ)" "$CODE" "$PID" > $D/lancement.txt
cd $D; for f in lancement.txt relais-journal.jsonl relais.log sortie.jsonl sortie.err relais-etat-final.txt; do [ -e $f ] && sha256sum $f > $f.sha256; done
grep -rqF -- "$KIMI_API_KEY" $D 2>/dev/null && echo "ALERTE : clé trouvée" >> $D/lancement.txt
echo fin
