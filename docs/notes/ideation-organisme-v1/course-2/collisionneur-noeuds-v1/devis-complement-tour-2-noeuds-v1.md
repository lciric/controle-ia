# Devis de complément — tour 2 du collisionneur des nœuds (question v12, attaque des recommandations) — v1

session-depot (instance 3), 31 octobre 2026, ≈ 18:34 UTC. Complète GO-2026-10-31-06 (45 USD séquencé, deux tours de 22 ;
avenant GO-2026-10-31-09 : tour 1 v12 à 30). Aucune dépense avant un mot direct de Lazar.

## Où en est GO-06

| Poste | Dépensé |
|---|---:|
| Run v10, arrêté (question périmée, R-921) | 6,36 |
| Run v12, tour 1, 12/12 (R-925) | 23,87 |
| **Cumul** | **30,23 / 45** ; reste 14,77 |

## Ce qui serait lancé

Collisionneur v7, quatre espèces, étage III (12 cellules), run neuf `run-noeuds-v12-tour2-e3-v1`, port 8793, gabarit éprouvé
(R-919) et Python neuf de l'instance 3 ; question du tour 2 `question-noeuds-v12-tour2-v1.md` (`19ff79d9…`, 837 mots :
consigne des verdicts de la question v12, puis l'annexe v5 de conv-audit servie telle quelle) ; faits = la **synthèse du tour 1**
(lecteur neuf, critères scellés `criteres-lecture-noeuds-v12-tour1-v1.md`, `22edbf47…`), seule ; les 45 811 mots de faits du
tour 1 ne sont pas resservis. Règle R-831 sur les refus. Lecture : critères scellés avant ouverture, lecteur neuf.

## Chiffrage (commande `devis` du collisionneur, sans appel, 31 octobre 18:28 UTC)

| Taille des faits | Pire cas sans relance | Attendu (rapport 0,55 observé au tour 1 v12) | Plafond ≥ 1,5 × attendu (R-924) |
|---:|---:|---:|---:|
| 8 000 mots | 34,22 | ≈ 19 | 28,5 |
| 12 000 mots | 35,29 | ≈ 19,5 | 29,3 |

Rapports réalisé / pire cas observés sur trois runs : 0,55 (nœuds tour 1 v12), 0,58 (protocelles tour 1), 0,20 (D-ML-1).
Garde de plafond (R-923) : la dernière cellule d'Opus pèse ≈ 5,8 au pire cas ; un plafond de 22 (GO-06 initial) ou de 14,77
(reste) arrêterait le run avant la fin.

## Options

| Option | Plafond du tour 2 | GO-06 porté à | Avantage | Inconvénient |
|---|---:|---:|---|---|
| (a) | **30 USD** | **61 USD** (30,23 + 30, arrondi) | règle R-924 respectée ; aucune coupure attendue | complément de 16 USD |
| (b) | 22 USD (plafond initial par tour) | 53 USD | moindre complément | coupure probable vers la dixième cellule, script suite et avenant ensuite |
| (c) | 14,77 USD (reste de GO-06, sans complément) | 45 (inchangé) | aucun complément | run arrêté à mi-chemin presque sûrement (R-923) ; faits et synthèse perdus pour les cellules manquantes jusqu'à un avenant |

## Recommandation

(a) : complément de **16 USD** (GO-06 porté à 61 USD, tour 2 plafond de run 30), lancement après le scellement de la synthèse
du tour 1 et la contre-lecture de sa table des empreintes. Confiance 0,65 sur l'attendu (≈ 19 USD). Nœud de dépense : pas de
défaut à 48 heures.
