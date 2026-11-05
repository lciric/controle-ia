# Rejeu des juges du pilote de T0.5 — lecture gelée et audit R4 (v1)

Lignée « session-depot » (instance 2), 29 octobre 2026, 03:25 UTC. Run `20261029-021158-rejeu-juges-reel`, branche
`calcul/rejeu-juges-v1` : résultats `3b8c6931`, traces `a89a7a9d`, lecture `79c79e49`. Lecture par la commande de la fiche
et par elle seule (`--lire`) : `diag/20261029-021158-rejeu-juges-reel/lecture-rejeu-v1.json` (`63b28eaf…`, scellé, sur la
branche). Fiche : `../fiche-lancement-rejeu-juges-v1.md`. Chiffres : mesures d'instrument, non opposables (R7).

## Verdict (critères gelés)

**Aucune cellule ne tient H_A (≥ 0,99 de scores finis et appuyés) : les six cellules (juge × variante) se lisent « H_B :
cellule à redéfinir », toutes tranchées.** L'instrument est aligné partout (part improbable ≤ 0,0008 ; aucune lecture en
échec). La meilleure cellule est **8B, verdict d'abord : 157 / 180 = 0,87** (Wilson 95 % : 0,82 à 0,91).

| cellule | finis / 180 | part | Wilson 95 % | accord (critères égaux) | s par notation | pic mémoire (Gio) |
|---|---|---|---|---|---|---|
| 8B, b0 relu | 84 | 0,47 | 0,40–0,54 | 0,79 | 1,22 | 23,3 |
| 3B, b0 relu | 71 | 0,39 | 0,33–0,47 | 0,73 | 0,93 | 22,4 |
| 8B, verdict d'abord | 157 | 0,87 | 0,82–0,91 | 0,74 | 6,12 | 34,7 |
| 3B, verdict d'abord | 115 | 0,64 | 0,57–0,71 | 0,62 | 3,91 | 31,4 |
| 8B, budget relevé | 100 | 0,56 | 0,48–0,63 | 0,81 | 26,83 (60 rejoués) | 40,2 |
| 3B, budget relevé | 72 | 0,40 | 0,33–0,47 | 0,73 | 19,36 (9 rejoués) | 35,6 |

Durée totale 4 039,5 s ; « budget relevé » est composé (b0 relu, rejoué au budget relevé là où la réponse était tronquée).

## Audit R4 (déclenché dans les six cellules)

Déclencheur commun : « jetons de tête : scores appuyés à note écrite non admise au-delà de 0,02 × n ». Vingt notations
relues par cellule, tirées par la graine de la lecture (`audit_r4_rejeu_v1.py`, sortie `audit_r4_rejeu_v1-sortie.json`).
Réserves consignées, **aucune autre lecture** :

1. **Échelles mal tenues** (3B surtout, 8B encore en verdict d'abord) : le juge écrit 4 sur une échelle [0, 3] et 5 sur
   [0, 4] ; la masse des valeurs admises tombe sous le seuil d'appui : c'est la cause dominante des non-finis du 3B (parmi
   les tirées non finies : 9 sur 13 en b0 relu, 9 sur 12 en budget relevé, 9 sur 9 en verdict d'abord) et celle des
   deux non-finis du 8B en verdict d'abord.
2. **Demi-points du 8B** (« 2.5 », « 3.5 ») : la lecture par les jetons de tête compte la masse de « 2 » pour « 2.5 » ;
   l'espérance lue est en moyenne 0,28 point sous la note écrite (29 critères, de − 0,77 à + 0,88). Biais d'instrument
   vers le bas, déclaré par la fiche, à traiter dans la redéfinition.
3. **Troncature et critères absents** (8B b0 relu) : 7 sur 20 tirées tronquées ; critères manquants (SPECIFICITY,
   RESULT_REASONING). Le verdict d'abord les supprime presque.

## Ce que cela implique (proposition, pas une lecture)

La cellule des juges de la banque est à redéfinir (P-16). Voie la plus courte d'après l'audit : **verdict d'abord, avec
l'échelle de chaque critère écrite à côté de lui et les valeurs admises seules** (ni demi-point, ni valeur hors échelle),
juge 8B ; à rejouer sur les mêmes 180 notations avant toute banque. Rythmes utiles au devis du pilote : 8B 6,1 s et 3B
3,9 s par notation en verdict d'abord (au lieu de 58,2 et 27,5 s en notation générée complète).
