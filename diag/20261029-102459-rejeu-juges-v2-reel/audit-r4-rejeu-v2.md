# Audit R4 — Rejeu des juges v2

**Date** : 2026-10-29 ≈ 12:55 UTC.
**Auditeur** : sous-agent (fork) de session-depot, lignée Opus.
**Fichier source** : `diag/20261029-102459-rejeu-juges-v2-reel/lecture-rejeu-v2.json` (`ad771a78…`).
**Fichiers de verdict** : `rejeu-8B-verdict-echelles.json`, `rejeu-3B-verdict-echelles.json` (empreintes vérifiées au commit `4fcb3bbb`).
**Déclencheur** : « jetons de tête : scores appuyés à note écrite non admise au-delà de 0,02 × n ».
**Critère du code** (l. 895-896 de `noter_rejeu_juges_v1.py`) : une notation est comptée si `proba.score` n'est pas nul **et** `len(ecrit.notes) < len(proba.criteres)` (au moins une note écrite hors échelle, donc rejetée).

---

## Verdict

**Les comptes globaux sont exacts** (recomptage : 4/167 pour le 8B, 13/134 pour le 3B, identiques à la lecture). Le déclencheur (seuil 0,02 × 180 = 3,6) est bien franchi par les deux cellules. **Aucune erreur de comptage ni de tirage.**

Les échantillons d'audit tirés au sort (20 par cellule, graine gelée) contiennent respectivement **1** (8B) et **0** (3B) notations du type « tête » — compatible avec les faibles taux globaux (2,4 % et 9,7 %). Aucune anomalie cachée dans les notations non flaggées de l'échantillon.

**Nature du phénomène** : le juge 3B écrit des notes hors échelle plus souvent que le juge 8B (9,7 % contre 2,4 %). Les anomalies portent surtout sur BALANCE (3B : 6 fois, sur une échelle [0, 3], le juge écrit 4) et RIGOR (les deux juges : 3 fois, sur [0, 4], le juge écrit 5). Le score probabiliste (par les jetons de tête) n'est pas affecté directement puisqu'il ne prend pas appui sur la note écrite rejetée — mais le fait que le juge propose une valeur hors échelle en texte révèle un biais de tendance centrale ou de surévaluation sur ces critères.

---

## Cellule 8B (décisive) — 20 notations d'audit

| # | Clé | proba.score | notes | critères | anomalies | Tête ? |
|---|-----|-------------|-------|----------|-----------|--------|
| 1 | juge-8B/2506.01290v2/e0/passe-0 | 73,02 | 10 | 10 | — | non |
| 2 | juge-8B/2506.01420v2/e1/passe-0 | 84,41 | 10 | 10 | — | non |
| 3 | juge-8B/2506.09007v2/e0/passe-0 | 78,50 | 10 | 10 | — | non |
| 4 | juge-8B/2506.16404v3/e0/passe-0 | 78,01 | 10 | 10 | — | non |
| 5 | juge-8B/2506.17197v2/e1/passe-0 | 82,68 | 10 | 10 | — | non |
| 6 | juge-8B/2509.03810v2/e0/passe-0 | 83,09 | 10 | 10 | — | non |
| 7 | juge-8B/2509.21880v3/e0/passe-1 | 78,69 | 10 | 10 | — | non |
| 8 | juge-8B/2509.24912v2/e0/passe-1 | 63,32 | 10 | 10 | — | non |
| 9 | juge-8B/2510.02245v2/e0/passe-0 | 72,90 | 10 | 10 | — | non |
| 10 | juge-8B/2510.02779v4/e0/passe-0 | 82,57 | **9** | 10 | RIGOR : 5 hors de [0, 4] | **oui** |
| 11 | juge-8B/2510.05038v3/e0/passe-1 | 80,85 | 10 | 10 | — | non |
| 12 | juge-8B/2510.05132v3/e0/passe-0 | 78,25 | 10 | 10 | — | non |
| 13 | juge-8B/2510.25798v1/e1/passe-0 | 77,59 | 10 | 10 | — | non |
| 14 | juge-8B/2512.00930v1/e0/passe-1 | — | 0 | 0 | bloc inachevé | non (pas de score) |
| 15 | juge-8B/2512.01199v1/e0/passe-1 | 80,93 | 10 | 10 | — | non |
| 16 | juge-8B/2512.02017v1/e0/passe-1 | 70,13 | 10 | 10 | — | non |
| 17 | juge-8B/2512.05150v2/e0/passe-0 | 70,29 | 10 | 10 | — | non |
| 18 | juge-8B/2601.21315v2/e0/passe-0 | 71,76 | 10 | 10 | — | non |
| 19 | juge-8B/2602.00987v1/e0/passe-0 | 78,04 | 10 | 10 | — | non |
| 20 | juge-8B/2603.01762v1/e0/passe-0 | — | 0 | 0 | bloc inachevé | non (pas de score) |

**Comptage échantillon** : 1 / 20 = 5,0 %.
**Proportion globale** : 4 / 167 = 2,4 %.
Compatible : l'échantillon contient l'une des 4 notations flaggées (`2510.02779v4/e0/passe-0`, RIGOR à 5 hors [0, 4]).

### Détail des 4 notations flaggées globalement (8B)

| Clé | Notes/critères | Critère(s) manquant(s) | Anomalie |
|-----|----------------|------------------------|----------|
| juge-8B/2604.23720v1/e1/passe-0 | 9/10 | RIGOR | RIGOR : 5 hors de [0, 4] |
| juge-8B/2510.14562v1/e0/passe-0 | 1/10 | 9 critères | valeurs non admises (toutes entre guillemets simples au lieu d'entiers) |
| juge-8B/2604.18258v1/e1/passe-0 | 9/10 | RESULT_REASONING | RESULT_REASONING : 4 hors de [0, 3] |
| juge-8B/2510.02779v4/e0/passe-0 | 9/10 | RIGOR | RIGOR : 5 hors de [0, 4] |

---

## Cellule 3B (descriptive) — 20 notations d'audit

| # | Clé | proba.score | notes | critères | anomalies | Tête ? |
|---|-----|-------------|-------|----------|-----------|--------|
| 1 | juge-3B/2506.01290v2/e0/passe-0 | 75,96 | 10 | 10 | — | non |
| 2 | juge-3B/2506.17197v2/e0/passe-0 | 80,45 | 10 | 10 | — | non |
| 3 | juge-3B/2508.10631v2/e0/passe-1 | 74,13 | 10 | 10 | — | non |
| 4 | juge-3B/2509.03810v2/e1/passe-0 | 76,29 | 10 | 10 | — | non |
| 5 | juge-3B/2509.22925v2/e0/passe-0 | 74,05 | 10 | 10 | — | non |
| 6 | juge-3B/2509.22925v2/e0/passe-1 | — | 0 | 0 | bloc inachevé | non (pas de score) |
| 7 | juge-3B/2510.18828v1/e0/passe-1 | 74,80 | 10 | 10 | — | non |
| 8 | juge-3B/2510.25798v1/e0/passe-1 | 63,31 | 10 | 10 | — | non |
| 9 | juge-3B/2511.00962v1/e0/passe-1 | 76,38 | 10 | 10 | — | non |
| 10 | juge-3B/2511.18601v1/e0/passe-0 | 69,18 | 10 | 10 | — | non |
| 11 | juge-3B/2512.01199v1/e0/passe-0 | 68,76 | 10 | 10 | — | non |
| 12 | juge-3B/2512.03125v1/e0/passe-1 | 79,20 | 10 | 10 | — | non |
| 13 | juge-3B/2601.01484v2/e0/passe-0 | — | 9 | 10 | REDUNDANCY_PENALTY : 1 hors de [-2, 0] | non (score nul) |
| 14 | juge-3B/2603.01762v1/e0/passe-0 | — | 9 | 10 | RESULT_REASONING : 4 hors de [0, 3] | non (score nul) |
| 15 | juge-3B/2603.01762v1/e0/passe-1 | — | 10 | 10 | — | non (score nul) |
| 16 | juge-3B/2604.16919v1/e0/passe-0 | 71,60 | 10 | 10 | — | non |
| 17 | juge-3B/2604.16919v1/e0/passe-1 | 62,78 | 10 | 10 | — | non |
| 18 | juge-3B/2604.17568v1/e0/passe-1 | 72,74 | 10 | 10 | — | non |
| 19 | juge-3B/2604.23720v1/e0/passe-0 | — | 0 | 0 | bloc inachevé | non (pas de score) |
| 20 | juge-3B/2604.23720v1/e0/passe-1 | 90,06 | 10 | 10 | — | non |

**Comptage échantillon** : 0 / 20 = 0 %.
**Proportion globale** : 13 / 134 = 9,7 %.
Remarque : les entrées n° 13 et 14 ont une note hors échelle (notes < critères) mais `proba.score` est nul (le modèle n'a pas produit de scores probabilistes exploitables), donc elles ne sont **pas** comptées dans le déclencheur. Aucune des 13 notations flaggées globalement ne tombe dans le tirage aléatoire — plausible vu le taux (espérance : 1,4 dans un tirage de 20 sur 134, probabilité d'en tirer zéro ≈ 22 %).

### Détail des 13 notations flaggées globalement (3B)

| Clé | Notes/critères | Critère(s) manquant(s) | Anomalie |
|-----|----------------|------------------------|----------|
| juge-3B/2605.17899v2/e0/passe-0 | 9/10 | BALANCE | BALANCE : 4 hors de [0, 3] |
| juge-3B/2506.21710v2/e1/passe-0 | 9/10 | RIGOR | RIGOR : 5 hors de [0, 4] |
| juge-3B/2512.01199v1/e1/passe-0 | 9/10 | BALANCE | BALANCE : 4 hors de [0, 3] |
| juge-3B/2511.18601v1/e0/passe-1 | 9/10 | REDUNDANCY_PENALTY | REDUNDANCY_PENALTY : 1 hors de [-2, 0] |
| juge-3B/2602.09690v1/e0/passe-0 | 9/10 | RESULT_REASONING | RESULT_REASONING : 4 hors de [0, 3] |
| juge-3B/2510.05132v3/e1/passe-0 | 9/10 | RIGOR | RIGOR : 5 hors de [0, 4] |
| juge-3B/2510.24061v1/e1/passe-0 | 9/10 | REDUNDANCY_PENALTY | REDUNDANCY_PENALTY : 2 hors de [-2, 0] |
| juge-3B/2603.06922v2/e0/passe-1 | 9/10 | BALANCE | BALANCE : 4 hors de [0, 3] |
| juge-3B/2510.02245v2/e1/passe-0 | 9/10 | BALANCE | BALANCE : 4 hors de [0, 3] |
| juge-3B/2506.01420v2/e1/passe-0 | 9/10 | RESULT_REASONING | RESULT_REASONING : 4 hors de [0, 3] |
| juge-3B/2510.02779v4/e0/passe-1 | 8/10 | BALANCE, RESULT_REASONING | BALANCE : 4 hors de [0, 3], RESULT_REASONING : 4 hors de [0, 3] |
| juge-3B/2510.21310v2/e1/passe-0 | 9/10 | RIGOR | RIGOR : 5 hors de [0, 4] |
| juge-3B/2602.04162v2/e0/passe-0 | 9/10 | BALANCE | BALANCE : 4 hors de [0, 3] |

Répartition des anomalies : BALANCE (6 fois, le juge écrit 4 sur [0, 3]), RIGOR (3), RESULT_REASONING (3), REDUNDANCY_PENALTY (2). Le juge 3B déborde plus souvent les échelles que le juge 8B (9,7 % contre 2,4 %).

---

## Conclusion

1. **Comptes vérifiés** : les 4 (8B) et 13 (3B) notations « tête » sont exactes, le critère du code est fidèle à la fiche.
2. **Échantillons d'audit** : 1/20 (8B) et 0/20 (3B) — compatibles avec les taux globaux, aucun biais de tirage apparent.
3. **Nature** : les anomalies sont des notes écrites hors échelle (une valeur de plus que le maximum ou une valeur positive sur une échelle négative). Le score probabiliste par les jetons de tête n'est pas contaminé (il ne prend pas appui sur la note rejetée), mais le phénomène révèle un biais de tendance du juge (en particulier le 3B sur BALANCE).
4. **Impact sur la cellule décisive** : les 4 notations 8B flaggées conservent un score probabiliste valide (sauf `2510.14562`, qui a 9 critères hors format) ; le verdict H_B à 167/180 n'est pas sensible à ce biais (retirer les 4 donnerait 163/176 = 92,6 %, toujours H_B).
5. **Réserve** : le juge 3B déborde les bornes d'échelle presque quatre fois plus souvent que le 8B ; si la cellule du 3B devenait un jour décisive, ce taux devrait être traité (durcir la consigne du juge ou élargir l'échelle de BALANCE).
