# Mesures pour le plan de calcul de P3 — v1

Mesures de la session 15 (2026-10-17), sur la machine de la session (4 processeurs, 15 Gio, partagée) : **ordres de grandeur
seulement**. Les temps d'entraînement sont dominés par une part fixe (passage en double précision, normalisation) et
bruités (pentes négatives à 4 fils) ; le budget du run se fixe à la répétition sur l'instance et par une garde de durée.
Données synthétiques gaussiennes à d = 4 096 ; code de T0.7 tel quel (`sondes.familles.entrainer`,
`sondes.evaluation.scores_actions`).

| fichier | contenu |
|---|---|
| `chrono_familles.py` | entraînement à 20 époques et notation de 20 actions, par famille |
| `chrono-familles-1fil-v1.txt`, `chrono-familles-4fils-v1.txt` | sorties brutes (1 et 4 fils) |
| `pente_epoques.py` | coût marginal d'une époque (10 contre 60 époques, 20 000 jetons) |
| `pente-epoques-v1.txt` | sortie brute |
| `longueurs_consignes.py` | longueurs en jetons des textes privés de P3, lus dans le fichier des consignes |
| `longueurs-consignes-brouillon2-v1.txt` | sortie brute sur `brouillons/P3-consignes-v1-brouillon2.md` (`50850b5b…`) |

Lecture retenue (R-194) : la notation de Mahalanobis par le code de référence coûte de l'ordre de 1,6 à 2,2 s par action de
100 jetons sur un fil (produit en `einsum` sans BLAS) : la notation en ligne de P3 se fait sur la carte, vectorisée, avec
une garde d'identité contre le code de référence ; l'entraînement reste celui de T0.7, sur processeur, tous fils.
