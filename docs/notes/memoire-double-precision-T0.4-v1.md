# Note — mémoire de la carte pour la logique en double précision (T0.4, version 2) — v1

Rédigée le 2026-10-05 par la session de mise en œuvre. Elle fixe la carte de la version 2 de la validation de T0.4 et corrige une estimation de la proposition N-010. Elle ne lit aucun écart ni aucune équivalence : seulement de la mémoire, des longueurs et des durées.

## Ce qui était faux

La proposition N-010 (`docs/decisions/proposition-N-010-v1.md`, sha256 `06b4ff5627abd03c6708ea628b157d2c90d03b853be8d24a0d80e3b299bbe0ef`) annonçait « environ 73 Go de mémoire sur une carte de 80 Go ». La sonde de mémoire a repris la même base : un lot de 8 contextes d'au plus 1 400 jetons.

Cette base était le domaine observé de la v1, soit 1 184 jetons au plus. Mais ce domaine ne porte que sur les **actions comparées** (épisodes 1 et 6). Or la génération remplit chaque lot à la longueur du plus long contexte de ses 8 lignes. Dans la v1, cette longueur remplie a atteint **2 329 jetons** (épisode 7, agent 0, pas 9 : une transcription dont plusieurs actions vont jusqu'à 256 jetons).

## Entrées (scellées)

- Sonde de mémoire, instance 54311651 (A100 SXM4 80 Go, commit `6556b4e`) : `traces/t04-20261005-121227-nRet/sonde-memoire.json`, sha256 `85b186bd42ad8120ebc1c9974e853645677060c5e5e787714c142c788274a45a`.
- Run A de la v1 (`20261005-102042-validation-reelle`) :
  - `diag/20261005-102042-validation-reelle/arret.json`, sha256 `4eb2d92069e270631bf3e4d25345b44191cbe419d71a4f06725659c32846aeed` (pic de la phase de logique en simple précision : 51,912 Go) ;
  - ses huit trajectoires de logique (`logique-episode-k-trajectoire.json`, chacune avec son empreinte compagnon).
- Calcul : `docs/notes/memoire-T0.4-v2/calcul_memoire_v1.py` (empreinte compagnon), lancé depuis la racine du dépôt.

## Méthode

- Le surcroît de mémoire d'un lot de 8 en génération, pour une longueur remplie L, suit s(L) = a·L² + b·L. Le terme quadratique vient des matrices d'attention du noyau « math ». Le terme linéaire vient du cache, des activations et des couches denses.
- Deux points fixent a et b :
  - la sonde, en double précision : L = 1 400, s = 81,413 − 64,242 = 17,17 Go ;
  - le pic de la v1, en simple précision : L = 2 329, s = 51,912 − 32,121 = 19,79 Go. Doublé pour la double précision, cela donne 39,58 Go.
- Le second point est une borne haute : si le pic de la v1 venait d'une autre étape que la génération, le surcroît réel est plus petit.
- Borne théorique de L : le plus long premier contexte, plus 9 pas d'au plus 256 jetons générés, chacun suivi du surcoût par pas maximal observé dans la v1 (clôture, observation, en-têtes). L'observation est bornée par construction (trois entrées du journal, tronquées à 20 caractères).

## Résultats

| grandeur | valeur |
|---|---|
| poids en double précision | 64,24 Go |
| a, b | 5,09e-6 Go par jeton², 5,14e-3 Go par jeton |
| pic estimé, L = 1 400 (sonde) | 81,4 Go |
| pic estimé, L = 2 329 (v1) | 103,8 Go |
| borne théorique de L | 3 097 jetons (82 + 9 × (256 + 79)) |
| pic estimé à la borne | 129,0 Go |
| L maximale, A100 80 Go (79,25 Gio, 1 Go de réserve) | 1 534 jetons |
| L maximale, H200 141 Go (140,4 Gio) | 3 625 jetons |
| L maximale, B200 (179,1 Gio) | 4 516 jetons |

- Sur la carte de 80 Go, la v1 aurait manqué de mémoire au pas 7 de l'agent 0 (1 676 jetons).
- Sur une H200, la borne théorique tient avec environ 20 Go de marge.
- Si le surcoût par pas montait à 97 jetons (60 caractères tronqués, un jeton chacun au pire, plus le texte fixe et les en-têtes), la borne passerait à 3 259 jetons et le pic à 135 Go : la H200 tient encore.

## Conséquences (décision de routine R-042)

- La v2 tourne sur une carte de 141 Go : H200 ou H200 NVL, ou à défaut B200.
- La garde de mémoire de la carte passe de 75 à 130 Gio, au commit `47d3c61`. Une carte de 80 Go est donc refusée avant toute génération.
- Le plus long contexte rempli d'un lot est désormais consigné dans le chrono de chaque phase (`longueur_remplie_max`).
- Coût : environ 4,15 USD de l'heure. Un essai complet prend 1 à 1,5 heure, soit environ 4 à 6 USD. Au plafond cumulatif de T0.4 (5,44 heures restantes), le coût serait d'environ 23 USD. Tout cela reste dans le GO-2026-10-04-08 (plafond de 150 USD).
- En heures équivalent A100, l'unité du devis, une heure de H200 en vaut probablement au moins deux : selon les fiches du constructeur (non vérifiées ici), sa bande passante mémoire est environ 2,4 fois plus grande et son débit en double précision environ 3,4 fois plus grand. Le coût par heure équivalente resterait donc dans la fourchette du devis. Le run de la v2 le mesurera (débit consigné).

## Limites

- Le modèle repose sur deux points, dont l'un est une borne haute.
- La production (bfloat16) n'est pas concernée : 16 Go de poids et le noyau d'attention par défaut.
- Un manque de mémoire de la carte reste une cause déterministe dans la table de lecture : nœud, sans relancement à l'identique.
