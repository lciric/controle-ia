#!/bin/sh
# CL11 : enveloppe de l'essai — pose une clé factice, pointe la vraie commande vers le faux serveur local (même options que la marche).
GEMINI_API_KEY=cle-factice; export GEMINI_API_KEY
exec /usr/bin/timeout -k 20 1700 /usr/bin/python3 -I -B /tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-v44/cl11/../lancement-ideation-v1/commande_argon_v1.py --compter-jetons --delai-s 1500 --prix-entree 8.3 --prix-sortie 41.5 --url-base http://127.0.0.1:8799/v1beta --modele gemini-argon
