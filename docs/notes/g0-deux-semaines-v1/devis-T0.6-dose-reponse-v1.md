# Devis — T0.6, organisme (ii) à dose réglable, courbe dose–réponse et test croisé — v1

- Écrit le 2026-11-05 vers 16:12 UTC (heure relevée par `date -u`) par le rédacteur neuf du brouillon 4
  (`brouillons/T0.6-organismes-v0-v1-brouillon4.md`), pour la ligne de dépense. Mot de Lazar, 5 novembre 2026 vers
  15:55 UTC : « go devis dose-réponse » (`registres/decisions.md` R-1572). Aucune dépense engagée par ce document.
- **GO** : GO-2026-11-02-28 (`registres/go.md` l. 216 au commit `06765457`), attendu ≈ 60 USD, **plafond exactement
  200 USD**, échéance **2026-11-16** ; A100 ou H200 chez Vast.ai ; aucun budget de temps qui coupe une étape.
- **Hypothèses du devis** (valeurs par défaut des décisions DT, défaut échu le 5 novembre à 07:05 UTC, R-1314 ; Lazar peut
  changer) : DT-1 (b), distillation sur des actions neuves jouées sur les 32 tâches de réserve, évaluation sur les 64
  tâches d'évaluation ; DT-6 (a), A100 SXM4 80 Go, relance sur H200 seulement si la mémoire manque à la distillation.
  Débits : ceux du run réel de P3 (même modèle, même harnais, même carte).

## Sources des chiffres

| donnée | valeur | source |
|---|---|---|
| durée d'un épisode (N = 1, T = 10, lots de 8) | **40,2 s** (240 épisodes en 9 644,6 s) | `brouillons/T0.6-organismes-v0-v1-brouillon2-pieces/puissance-t06-v2.txt` (`87813a36…`) section 4, tirée de `diag/20261019-230011-p3-reel/` |
| passe unique d'activations | 108,4 s pour 240 épisodes | même source |
| sondes génériques et planchers (processeur) | 1 534,1 s ; suite des tests ≈ 1 600 s | même source ; P3-bis brouillon 3, « Devis » |
| distillation, deux adaptateurs, 1 600 paires, trois époques | transcription entière 0,46 à 0,92 h ; paire par action 3,07 à 6,14 h (120 à 60 téraopérations par seconde utiles) | même source |
| instance de P3 (A100 SXM4 80 Go, 56799469) | 22:28:53 → 02:06:50 UTC, ≈ 3,6 h, **1,0889 USD/h**, ≈ 3,96 USD ; disque arrêté 0,022 USD/h | `registres/depenses.md` l. 87-88 (commit `06765457`) |
| prix A100 SXM4 80 Go relevés du 12 oct. au 5 nov. | 1,009 ; 1,08 ; 1,0889 ; 1,089 ; 1,093 ; 1,1067 ; 1,107 ; 1,16 ; 1,161 ; 1,18 ; 1,184 ; 1,187 ; 1,203 ; 1,2133 ; 1,366 (stockage compris) | `registres/depenses.md` l. 64, 88, 142, 145, 203, 208, 211, 221, 226, 233, 309, 310, 313, 321, 325, 355, 357 |
| borne de prix des lanceurs | 1,30 USD/h (P3, texte scellé) ; 1,40 USD/h (lanceur de T0.5 graines neuves) | `prereg/P3-premier-test-i-a-v1.md` l. 352 ; `registres/depenses.md` l. 308 |
| téléchargement | 0,026 et 0,039 USD/Go relevés ; borne 0,05 | `registres/depenses.md` l. 233 ; P3 l. 354-357 |
| disque | borne 0,03 USD/h ; disques estimés 1,32 et 1,34 USD (R1 v4) | P3 l. 354 ; `registres/depenses.md` l. 355, 357 |
| H200 NVL (relance seulement) | 4,441 et 4,669 USD/h tout compris en marche ; stockage ≈ 0,69 USD/Go/mois (hors borne) ; débit non mesuré | `registres/depenses.md` l. 35, 39 |

## Attendu (plan (b), A100)

| poste | quantité | heures |
|---|---|---|
| génération des données de distillation (saboteur instruit et témoin instruit de P3) | 2 × 32 tâches × 5 épisodes = 320 épisodes × 40,2 s | 3,57 |
| épisodes d'évaluation (H, IA, IT, IM, S25, S50, S75, S100, T100) | 9 × 64 = 576 épisodes × 40,2 s | 6,43 |
| distillation de deux adaptateurs | transcription entière (routine), à défaut paire par action | 0,46 à 6,14 |
| passe unique, mise en place, suite des tests, contrôle d'identité à dose 0, test croisé sur processeur, lectures, scellement, poussées | — | ≈ 1 (dont 0,11 de passe unique) |
| **total de marche** | | **11,5 à 17,1** |

- **Calcul** : 11,5 à 17,1 h × 1,0889 à 1,30 USD/h = **12,5 à 22,3 USD** (valeur centrale : 14 h × 1,16 ≈ 16 USD).
- **Disque** : ≥ 150 Go (modèle ≈ 16 Go, activations ≈ 31,5 Go pour trois couches en demi-précision, adaptateurs
  2 × 27 Mo) ; en marche ≤ 0,03 USD/h (≤ 0,5 USD) ; gardé arrêté jusqu'au verdict, 72 h au plus : **≤ 2,2 USD**.
- **Téléchargement** : descente ≈ 20 Go (au plus 40) ; montée ≈ 1 à 2 Go (adaptateurs, identifiants générés, sous-ensemble
  d'activations) ; à ≤ 0,05 USD/Go : **≤ 1 à 2 USD**.
- **Attendu ≈ 14 à 27 USD** (valeur centrale ≈ 18 USD), sous l'attendu du GO (≈ 60) et sous son plafond (200).
- Si Lazar change DT-1 pour (a) : 324 épisodes, 600 paires, 4,8 à 6,9 h, **≈ 7 à 13 USD**.

## Pire cas (sous le plafond ; l'arrêt à 200 USD cumulés est la seule garde de dépense)

| scénario | hypothèses | heures de carte | USD |
|---|---|---|---|
| P1 hôte deux fois plus lent que celui de P3, 1,40 USD/h | 34,2 h × 1,40 = 47,9 ; disque 1,0 + 2,2 ; téléchargement 2 | 34,2 | **≈ 53** |
| P2 = P1 + une relance complète sur A100 (erreur de chaîne avant tout épisode d'évaluation, ligne A1, au débit moitié) | + 21,4 h × 1,40 = 30,0 ; disque 0,6 ; téléchargement 2 | 55,6 | **≈ 86** |
| P3 erreur de mémoire à la distillation sur A100 (9,1 h au débit moitié, 12,8 USD + 2,3 de disque et téléchargement), puis course complète sur H200 à 4,669 USD/h, durées de l'A100 au débit moitié | 34,2 h × 4,669 = 159,7 ; disque ≤ 0,03 × 120 h = 3,6 ; téléchargement 2 | 43,3 | **≈ 180** |

H200 au débit de P3 : P3 ≈ 106 USD. Une H200 d'emblée (DT-6 (b)) : attendu ≈ 55 à 80 USD, pire cas ≈ 160. Au-delà de
180 USD cumulés, toute relance est un nœud de Lazar avant dépense.

## Hors devis

P3-bis, témoin positif (GO-2026-11-02-29, plafond 80 USD, attendu ≈ 6 à 9 USD, chaîne et instance à part) ; le juge 8B
de T0.8 sur ces épisodes s'il tourne sur une carte (GO à part) ; la règle du coût et le prédicteur sur les traits du texte
de T0.8, sur processeur, sans dépense ; la course de (i) à doses p < 1 (DT-5 (a), étape 2 de P-015 (b), GO à part).

## Ligne d'engagement proposée (`registres/depenses.md`, à écrire par la session au lancement, 11 novembre au plan daté)

« engagement : T0.6 organisme (ii), dose–réponse et test croisé (GO-2026-11-02-28, plafond 200 USD) : lanceur
`scripts/lancer_t06_v1.sh` (empreinte `<<EMPREINTES_CODE_T06>>`), commit `<<COMMIT_CODE_T06>>` ; préenregistrements de
T0.6 et de T0.7 scellés (`<<EMPREINTE_PREREG_T07>>`) ; une carte A100 SXM4 80 Go ≤ 1,30 USD/h, ≥ 16 cœurs effectifs,
≥ 128 000 Mo de mémoire vive, disque ≥ 150 Go, stockage ≤ 0,03 USD/h, téléchargement ≤ 0,05 USD/Go ; attendu ≈ 14 à
27 USD, pire cas ≈ 180 USD (relance H200) ; arrêt par identifiant à 200 USD cumulés ; crédit Vast.ai relu à la création
(recharge automatique, R-283) ».
