#!/bin/sh
# appel-argon-v5.sh (8 novembre 2026) — enveloppe d'Argon pour la course d'idéation v2, version neuve (R12).
#
# Remplace appel-argon-v4d.sh pour la fille idéation 1 : **aucun utilisateur système, aucun sudo** (décision de la mère,
# GO-2026-11-08-13 ; R12 : nouveau nom). La commande lancée est commande_argon_v3d.py (inchangée, R12), par son chemin
# absolu dans le dépôt de travail.
#
# Différences par rapport à appel-argon-v4d.sh :
# 1. Pas de vérification d'utilisateur (la v4d exigeait « argon »).
# 2. Pas de /opt/argon ni d'installation sous root : le script Python est lu depuis le dépôt de travail.
# 3. Le chemin de commande_argon_v3d.py est absolu ; le répertoire du dépôt vient de DEPOT_TRAVAIL (défaut /home/user/controle-ia-travail).
# 4. Tout le reste est identique à la v4d : clé factice, réglages figés après "$@", prix, bornes, adresse du relais Gemini v2.
#
# Contrat : l'environnement minimal du noyau (PATH, HOME, LANG, PLAFOND_SESSION_USD, ROLE_POLE, MODELE_DEMANDE_POLE) ;
# la consigne sur l'entrée standard (UTF-8) ; la dernière ligne de la sortie standard est toujours un objet JSON
# {"texte", "cout_usd", "modele_servi", …}, coût fini et strictement positif.
#
# Relais Gemini v2 (relais_gemini_v2.py) lancé séparément par le noyau, sur la boucle locale, port 8788, avec la vraie
# GEMINI_API_KEY dans son seul environnement ; cette enveloppe ne détient que la clé factice.
set -eu
umask 077
DEPOT_TRAVAIL="${DEPOT_TRAVAIL:-/home/user/controle-ia-travail}"
COMMANDE="$DEPOT_TRAVAIL/docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py"
if [ ! -f "$COMMANDE" ]; then
    echo '{"texte": "", "cout_usd": 1e-06, "erreur": "commande_argon_v3d.py introuvable"}'; exit 2
fi
GEMINI_API_KEY=factice-relais; export GEMINI_API_KEY
exec /usr/bin/timeout -k 20 1700 /usr/local/bin/python3 -I -B "$COMMANDE" --delai-s 1500 \
     "$@" --prix-entree 8.3 --prix-sortie 41.5 --prix-requete-web-usd 0.05 --max-requetes-web-pire-cas 20 \
     --provision-outil-jetons 32768 --url-base http://127.0.0.1:8788/v1beta
