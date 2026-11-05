#!/bin/sh
# appel-argon-v4d.sh (30 octobre 2026) — copie de appel-argon-v4c.sh (inchangée, R12) ; seul changement : elle lance
# commande_argon_v3d.py (la v3c corrigée : totalTokenCount lu, son écart aux jetons comptés compté au prix de sortie, et
# code 11 « usage incohérent ») au lieu de commande_argon_v3c.py. Les réglages figés après "$@" (prix, bornes de la
# garde, adresse du relais) et --delai-s avant "$@" sont ceux de la v4c, tels quels.
# --- en-tête de la v4c, tel quel ---
# appel-argon-v4c.sh (30 octobre 2026) — copie de appel-argon-v4b.sh (inchangée, R12) ; deux changements : (1) elle lance
# commande_argon_v3c.py (la v3b corrigée : code 10 au-delà du plafond, excédent d'entrée compté contre la provision
# d'outil) au lieu de commande_argon_v3b.py ; (2) les prix et les bornes de la garde sont posés APRÈS "$@" (mineur 4 de la
# contre-lecture de la v3b) : la commande garde la dernière occurrence d'un réglage (argparse), le noyau ne peut donc ni
# baisser les prix, ni régler la provision d'outil, le prix ou le maximum des requêtes de recherche. "$@" sert aux autres
# réglages seulement (--recherche-web, --delai-s qui reste borné par timeout, marge, provision de pensée, sorties).
# --- en-tête de la v4b, tel quel ---
# appel-argon-v4b.sh (30 octobre 2026) — copie de appel-argon-v4.sh (inchangée, R12) ; seul changement : elle lance
# commande_argon_v3b.py (la v3 corrigée) au lieu de commande_argon_v3.py. La vraie clé n'est masquée dans le corps relayé
# que par relais_gemini_v2.py (le relais v1 ne la masque que dans les en-têtes) ; la commande ne tient que la clé factice.
# --- en-tête de la v4, tel quel ---
# appel-argon-v4.sh (30 octobre 2026) — copie de appel-argon-v3.sh (inchangée, R12) ; seul changement : elle lance
# commande_argon_v3.py (option --recherche-web, transmise par "$@" comme tout réglage) au lieu de commande_argon_v2.py.
# --- en-tête de la v3, tel quel ---
# appel-argon-v3.sh — enveloppe d'utilisateur distinct pour Argon, v3 (session-depot, 29 octobre 2026) : **aucune clé** (ni
# fichier, ni variable réelle). Remplace appel-argon-v2.sh (qui lisait /home/argon/.cle-gemini). La commande commande_argon_v2.py (inchangée, R12)
# parle au relais Gemini local relais_gemini_v1.py, lancé par le noyau sous `env -i` avec la vraie clé dans son seul
# environnement ; elle pose la clé FACTICE ci-dessous dans l'en-tête x-goog-api-key, le relais la retire et pose la vraie.
# Boucle locale : la commande n'utilise aucun mandataire (ni HTTPS_PROXY ni SSL_CERT_FILE ne sont posés) ; c'est le relais qui
# sort par le mandataire de son propre environnement.
# L'adresse du relais vient APRÈS "$@" : elle prime sur tout --url-base reçu (la commande garde le dernier) ; "$@" sert aux
# autres réglages seulement. Installation (noyau, hors de cette session) : install -m 755 -o root -g root dans /opt/argon.
set -eu
umask 077
[ "$(id -un)" = argon ] || { echo '{"texte": "", "cout_usd": 1e-06, "erreur": "enveloppe hors utilisateur argon"}'; exit 2; }
GEMINI_API_KEY=factice-relais; export GEMINI_API_KEY
exec /usr/bin/timeout -k 20 1700 /usr/bin/python3 -I -B /opt/argon/commande_argon_v3d.py --delai-s 1500 \
     "$@" --prix-entree 8.3 --prix-sortie 41.5 --prix-requete-web-usd 0.05 --max-requetes-web-pire-cas 20 \
     --provision-outil-jetons 32768 --url-base http://127.0.0.1:8788/v1beta
