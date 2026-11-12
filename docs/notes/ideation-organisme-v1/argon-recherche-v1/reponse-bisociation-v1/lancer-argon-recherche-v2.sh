#!/bin/bash
# Appel unique d'Argon avec recherche Google (GO-2026-10-30-14, plafond 3 USD) sur la question fusionnée de conv-audit
# (aab8ced8…). Relais Gemini v2 (masque la clé dans le corps), commande v3d, enveloppe v4d (lancement v2, R-850), utilisateur argon.
# La clé passe par variable sous env -i au seul relais ; jamais en argument, fichier ou journal. Arrêt du relais par PID (R10).
set -u
D=/root/ideation-v1/argon-recherche-bisociation-v1
R=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1
cd $D || exit 9
[ "${GO_ID:-}" = GO-2026-10-30-14 ] || { echo "GO_ID absent ou faux"; exit 9; }
sha256sum -c --quiet question-fusionnee-argon-collisionneur-v1.md.sha256 || exit 9
(cd $R && sha256sum -c --quiet relais_gemini_v2.py.sha256) || exit 9
echo 46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46 /opt/argon/commande_argon_v3d.py | sha256sum -c --quiet || exit 9
echo abce8e5849b3f485a6cfb5a1d4a463a6eaaf1f330f82cc95dc562c8be43af3f8 /opt/argon/appel-argon-v4d.sh | sha256sum -c --quiet || exit 9
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$GEMINI_API_KEY" HTTPS_PROXY="$HTTPS_PROXY" \
    SSL_CERT_FILE=/root/.ccr/ca-bundle.crt /usr/bin/python3 -I -B $R/relais_gemini_v2.py --port 8788 --max-appels 4 \
    --journal $D/relais-gemini-journal-v2.jsonl > $D/relais-gemini-v2.log 2>&1 &
PID=$!
echo $PID > relais-gemini.pid
for i in $(seq 50); do grep -q "relais prêt" relais-gemini-v2.log && break; sleep 0.2; done
grep -q "relais prêt" relais-gemini-v2.log || { echo "relais pas prêt"; kill $PID; exit 9; }
DEBUT=$(date -u +%FT%TZ)
printf '%s' "$(cat question-fusionnee-argon-collisionneur-v1.md)" | PLAFOND_SESSION_USD=3 ROLE_POLE=proposeur_ideation \
    /usr/bin/timeout 1900 /usr/bin/setpriv --reuid=argon --regid=argon --init-groups /opt/argon/appel-argon-v4d.sh \
    --recherche-web --max-sortie-jetons 32000 > reponse-argon-recherche-v1.json 2> reponse-argon-recherche-v1.err
CODE=$?
FIN=$(date -u +%FT%TZ)
kill $PID; wait $PID 2>/dev/null
cat > lancement.txt <<FIN_
go: GO-2026-10-30-14
question: $D/question-fusionnee-argon-collisionneur-v1.md
empreinte_question: aab8ced8605ead096c94e66fae52770fe138e5032ed4aba7579b385fe50df58e
pid_relais: $PID
commande: /opt/argon/appel-argon-v4d.sh --recherche-web --max-sortie-jetons 32000 (PLAFOND_SESSION_USD=3, setpriv argon)
debut_utc: $DEBUT
fin_utc: $FIN
code_retour: $CODE
relais_arrete_pid: $PID
FIN_
for f in lancement.txt relais-gemini-journal-v2.jsonl relais-gemini-v2.log reponse-argon-recherche-v1.json reponse-argon-recherche-v1.err; do [ -e $f ] && sha256sum $f > $f.sha256; done
echo "code $CODE"
