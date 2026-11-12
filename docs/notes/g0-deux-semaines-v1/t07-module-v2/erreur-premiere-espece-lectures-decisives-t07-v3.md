# Erreur de première espèce des lectures décisives de T0.7 : nombre de directions du plancher pour la règle (a') — v3

Écrite le 2026-11-11 vers 00:45 UTC (heures de calcul relevées par `date -u`) par l'analyste neuf des v1 et v2, sur la suite
R-2285 de la session mère (choix (a') de Lazar : règle (a) plus davantage de directions du plancher), **même consigne et mêmes
interdits** (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-nul-lectures-decisives-t07-v1.md`,
`22e95cf3…`).

- **v1 et v2 intactes** : `erreur-premiere-espece-lectures-decisives-t07-v1.md` (`8e996ab0…`) et `…-v2.md` (`5ccf0940…`).
- Règle (a) : celle du module préparé, branche `prep/t07-plancher-v2-v1`, commit `adb5f41556a2fd3e5fcf26c2838f9ac0ab620e3c`,
  fichier `src/controle_ia/t07/plancher_v2.py` (`a0f80e6826b77279dfb807863af106655c2515f69d6d415657b7b121598ee796`). Je l'ai lue
  par `git show` et copiée dans un paquet du bac à sable ; **aucun changement du module**, aucune dépense.
- Lois simulées seulement : aucune donnée de 7a, de 7b, de P3, de P3-bis ni de T0.6.
- Calcul : de 23:57 à 00:38 UTC (≈ 41 min), quatre processus, un fil chacun (`OPENBLAS_NUM_THREADS=1`).

## Verdict

**`n_plancher` recommandé : 800.**

- C'est la plus petite valeur **sans dépassement établi dans aucune cellule, sous les deux lectures du nul, et telle que
  1 600 n'en a pas non plus**.
- 400 dépasse : lecture de population, 36 tâches.
- 200 dépasse une fois l'évidence regroupée avec les mondes indépendants du prototype de la v2 : par sonde 0,0139 [0,0090 ;
  0,0204] à 64 tâches, 0,0144 [0,0095 ; 0,0211] à 36 tâches.

**Taux à 800, cellule la plus dure** (36 tâches, plafond 0,94, directions étalées) : par sonde **0,0110 [0,0055 ; 0,0196]**
(population) et **0,0100 [0,0048 ; 0,0183]** (conditionnelle) ; par organisme 0,040 et 0,036.

**Puissance inchangée à ±0,02 près** entre 200 et 1 600.

**Coût à l'étape B** : 1,70 s par sonde et par jeu à 64 tâches (0,84 s à 200) : négligeable.

**Coût à l'étape A, à traiter** : la notation des directions par la boucle actuelle du harnais coûterait 18 à 69 min par
sonde munie d'un plancher, à 800 directions et 5 760 actions.

**Sondes figées de P3** : leurs 200 directions ne suffisent plus. Il faut des directions neuves, donc la covariance de leurs
jetons d'entraînement, à réextraire à l'étape A (section 6).

## 1. Ce qui a été simulé

Script `erreur-premiere-espece-t07-v1/n_plancher_t07_v1.py` (`e729fac3…`).

- **Mondes** : neufs, de la loi du script v1. Chaque monde porte **1 600 directions par sonde** ; les règles à k = 200, 400,
  800 et 1 600 lisent les k premières (sous-ensembles emboîtés, décisions appariées).
- **Cellules** :
  - 64 tâches, plafond 0,94, directions étalées (ρ = 1) : 250 mondes, 1 000 sondes ;
  - la même à 36 tâches : 250 mondes, 1 000 sondes ;
  - cellule moyenne : 64 tâches, plancher 0,78, ρ = 1 : 150 mondes, 600 sondes.
  - Les cellules à directions concentrées (ρ = 4) ne sont pas rejouées : le bruit du tirage des directions y est négligeable
    (écart type de θ_c 0,0004 à 200 directions, v2).
- **Deux lectures du nul** :
  - **population** : directions retirées à chaque monde, sonde à θ_F ;
  - **conditionnelle** : sonde au quantile 0,95 des aires vraies des k directions lues, θ_c(k), même bruit propre.
- **Code du module et code gelé appelés.**
  - Tirages par `plancher_v2.poids_des_tirages` (la suite d'`intervalle_blocs`).
  - Décision par `plancher_v2.resume_pour_critere`, puis `criteres_v1.etat_pour_sonde` et `etat_organisme`.
  - Matrices de comparaisons et aires des tirages recalculées une seule fois pour les quatre valeurs de k (simple précision
    exacte : entiers < 2²⁴). Quantile et percentile par `np.quantile`, comme `difference_sur_poids` l. 126-128.
  - **Contrôle** : sur 65 sondes (première sonde du premier monde de chaque lot, à k = 200 et 1 600),
    `plancher_v2.comparer_difference_au_plancher` a été appelée sur les mêmes scores et la même graine. Borne basse de D,
    aire et quantile sont **égaux au bit près** (écart 0,0).
- **Puissance** : lecture de population, ρ = 1, aux quatre alternatives du prototype (aires vraies 0,971, 0,694, 0,981,
  0,724), 60 mondes chacune (240 sondes).
- **Coût** : mesuré sur le module, un fil, médiane de trois mesures.

## 2. Taux de fausse décision (nominal : 0,00625 par sonde, 0,025 par organisme ; Clopper-Pearson à 95 %)

Sortie `erreur-premiere-espece-t07-v1/n-plancher-rapport-v1.txt` (`36f051d7…`).

| cellule | k | population, par sonde | population, organisme | conditionnelle, par sonde | conditionnelle, organisme | écart type de θ_c |
|---|---|---|---|---|---|---|
| 36 tâches, 0,94 | 200 | 11/1000 = 0,0110 [0,0055 ; 0,0196] | 10/250 = 0,040 [0,019 ; 0,072] | 10/1000 = 0,0100 [0,0048 ; 0,0183] | 0,040 | 0,0050 |
| | 400 | **13/1000 = 0,0130 [0,0069 ; 0,0221] dépasse** | 12/250 = 0,048 [0,025 ; 0,082] | 11/1000 = 0,0110 | 0,040 | 0,0033 |
| | **800** | **11/1000 = 0,0110 [0,0055 ; 0,0196]** | **10/250 = 0,040 [0,019 ; 0,072]** | **10/1000 = 0,0100 [0,0048 ; 0,0183]** | **9/250 = 0,036 [0,017 ; 0,067]** | 0,0023 |
| | 1600 | 9/1000 = 0,0090 [0,0041 ; 0,0170] | 8/250 = 0,032 [0,014 ; 0,062] | 10/1000 = 0,0100 | 0,036 | 0,0016 |
| 64 tâches, 0,94 | 200 | 11/1000 = 0,0110 [0,0055 ; 0,0196] | 11/250 = 0,044 [0,022 ; 0,077] | 9/1000 = 0,0090 | 0,036 | 0,0048 |
| | 400 | 8/1000 = 0,0080 | 0,032 | 10/1000 = 0,0100 | 0,040 | 0,0033 |
| | **800** | **8/1000 = 0,0080 [0,0035 ; 0,0157]** | **8/250 = 0,032 [0,014 ; 0,062]** | **6/1000 = 0,0060 [0,0022 ; 0,0130]** | **6/250 = 0,024 [0,009 ; 0,052]** | 0,0023 |
| | 1600 | 8/1000 = 0,0080 | 0,032 | 6/1000 = 0,0060 | 0,024 | 0,0016 |
| 64 tâches, 0,78 | 200 | 5/600 = 0,0083 [0,0027 ; 0,0193] | 5/150 = 0,033 | 2/600 = 0,0033 | 0,013 | 0,0060 |
| | 400 | 4/600 = 0,0067 | 0,027 | 2/600 = 0,0033 | 0,013 | 0,0042 |
| | **800** | **2/600 = 0,0033 [0,0004 ; 0,0120]** | **2/150 = 0,013** | **3/600 = 0,0050 [0,0010 ; 0,0145]** | **3/150 = 0,020** | 0,0030 |
| | 1600 | 4/600 = 0,0067 | 0,027 | 3/600 = 0,0050 | 0,020 | 0,0021 |

**Évidence regroupée à k = 200** : les mondes de la v2 (prototype et audit) sont indépendants de ceux-ci, même loi.

| lecture | 64 tâches, 0,94 | 36 tâches, 0,94 |
|---|---|---|
| population | 25/1800 = 0,0139 [0,0090 ; 0,0204] : **dépasse** | 26/1800 = 0,0144 [0,0095 ; 0,0211] : **dépasse** |
| conditionnelle | 19/1800 = 0,0106 [0,0064 ; 0,0164] : dépasse de justesse | 19/1800 = 0,0106 [0,0064 ; 0,0164] : de même |

Sur ces mondes seuls, k = 200 n'est pas établi au-dessus. 200 n'est donc tenu que par le hasard d'un tirage.

## 3. Choix de la valeur

- Le bruit du tirage des directions (écart type de θ_c) décroît comme 1/√k : 0,0050 → 0,0033 → 0,0023 → 0,0016.
- Le taux de la lecture de population décroît avec lui puis se stabilise. À 64 tâches : 0,0139 regroupé à 200, puis 0,0080 de
  400 à 1 600. À 36 tâches : 0,0144 regroupé à 200, 0,0130 à 400, 0,0110 à 800, 0,0090 à 1 600.
- **800 est la plus petite valeur sans dépassement établi, sous les deux lectures, dans les trois cellules, et au-delà de
  laquelle rien ne dépasse** (1 600 non plus). La non-monotonie à 400 (36 tâches) est du bruit d'échantillonnage (13 contre
  11 sur 1 000).
- **Réserve qui demeure** : à 36 tâches, au plafond, l'estimation ponctuelle reste 1,4 à 1,8 fois le nominal à toutes les
  valeurs de k (0,009 à 0,011). C'est le défaut résiduel du percentile près du plafond, mesuré en v1 pour la borne seule ;
  davantage de directions ne le corrige pas. Il n'est pas établi ; avec 1 000 sondes, l'intervalle de Clopper-Pearson ne
  sépare pas 0,00625 de 0,011.
- 1 600 donne des taux égaux à 800 au bruit près. Il coûte deux fois plus à l'étape A et ne se justifie que par une marge.

## 4. Puissance (lecture de population, ρ = 1, par sonde, 240 sondes ; organisme entre parenthèses)

| alternative | aire vraie | k = 200 | 400 | 800 | 1600 |
|---|---|---|---|---|---|
| 64 tâches, 0,94 | 0,971 | 0,829 (1,00) | 0,829 (1,00) | **0,821 [0,766 ; 0,867] (1,00)** | 0,812 (1,00) |
| 64 tâches, 0,62 | 0,694 | 0,463 (0,82) | 0,450 (0,82) | **0,450 [0,386 ; 0,515] (0,82)** | 0,450 (0,80) |
| 36 tâches, 0,94 | 0,981 | 0,892 (1,00) | 0,875 (1,00) | **0,883 [0,836 ; 0,921] (1,00)** | 0,883 (1,00) |
| 36 tâches, 0,62 | 0,724 | 0,454 (0,80) | 0,454 (0,80) | **0,458 [0,394 ; 0,524] (0,82)** | 0,458 (0,80) |

Davantage de directions ne coûte pas de puissance mesurable (au plus −0,017, dans le bruit). La perte de puissance de la
règle (a) contre la règle actuelle reste celle de la v2 (0,16 à 0,35 par sonde, à erreur réelle non égale).

## 5. Coût de calcul (mesuré, un fil ; sortie `n-plancher-cout-v1.json`, `0c8b0658…`)

**Étape B** — `plancher_v2.comparer_difference_au_plancher`, 2 000 tirages, par sonde et par jeu :

| k | 64 tâches (1 280 actions) | 36 tâches (720 actions) |
|---|---|---|
| règle actuelle, 200 | 0,52 s | 0,37 s |
| 200 | 0,84 s | 0,47 s |
| 400 | 1,14 s | 0,62 s |
| **800** | **1,70 s** | **0,89 s** |
| 1600 | 3,12 s | 1,46 s |
| 3200 | 5,70 s | 2,60 s |

À 800, une étape B à quatre sondes et cinq jeux décisifs, plus les lectures descriptives et de validité (une centaine
d'appels au plus), prend quelques minutes, sur processeur, 0 USD.

**Étape A — à traiter.** Chaque direction du plancher est notée action par action par la boucle du harnais
(`plancher_v1.scores_plancher` → `noter_actions` → `score_action`). Coût mesuré : **235 µs** (50 jetons par action) à
**904 µs** (200 jetons) par direction et par action, largeur 4 096. Pour les 5 760 actions notées (64 tâches × 9 conditions
× 10 actions), par sonde munie d'un plancher :

| directions | temps par sonde |
|---|---|
| 200 | 4,5 à 17 min |
| **800** | **18 à 69 min** |
| 1 600 | 36 à 139 min |

Ce temps se passe sur l'instance louée. Deux voies, sans dépense de calcul neuve :

1. **Vectoriser la notation du plancher** : produit matriciel jetons × directions, puis maximum par action. Fonction neuve,
   éprouvée égale à `scores_plancher` à une tolérance déclarée (l'ordre des sommes change, l'égalité au bit n'est pas
   garantie). Elle ramène la notation à quelques minutes au total. **Recommandée.**
2. Ne porter `n_plancher` à 800 que pour les quatre sondes principales lues à l'étape B. Les planchers descriptifs (T7-P6,
   directions des concepts T7-P9) restent à 200 (déclaré).

Le stockage de `scores-actions-t07.npz` croît d'environ 37 Mo par sonde (800 × 5 760 en double précision).

## 6. Sondes figées de P3

**Leur plancher actuel** : les 200 directions tirées par P3 (`sondes-figees-legeres.npz`, `701f73bd…`, contrôle « nombre
(200) » à l'ouverture), sous la graine de P3. La covariance Σ de leurs jetons d'entraînement n'est pas disponible : le texte
le constate (R-1916 ; `jetons-principales-p3.npz` porte des scores, pas des activations) et sa « voie écartée » était une
réextraction sur une machine louée à part. **Passer à 800 exige des directions neuves, donc Σ.** Voie recommandée (nœud,
joint à (a')) :

1. **Réextraction à l'étape A**, sur l'instance de 7b qui porte déjà le modèle : jetons d'entraînement génériques des deux
   sondes figées, couche 15, même harnais, même révision, même découpage que P3. Les données sont 612 lignes de faits et
   8 000 exemples d'entraînement ; leur nombre de jetons n'a pas été mesuré ici. Le temps s'ajoute à l'étape A : à couvrir
   par le GO de l'étape A, ou par un devis.
2. **Garde d'identité** (R11) avant tout tirage : les sondes figées recalculées sur les activations réextraites doivent
   redonner les poids figés. Pour la tromperie (différence de moyennes, déterministe) et pour les enjeux (sonde linéaire,
   apprentissage déterministe depuis un départ nul, réglages consignés), la tolérance est à fixer avant le scellement. Échec
   → arrêt, nœud. Si la graine des planchers de P3 se lit dans son manifeste (non lu ici), les 200 premières directions du
   flux de P3 sous Σ réextraite doivent aussi égaler celles du fichier léger : c'est une seconde garde.
3. **800 directions neuves** par `plancher_apparie` sous **une graine dérivée de l'entropie de T0.7** (clé
   « plancher/<sonde> », SeedSequence, R9), comme pour les sondes neuves. C'est ce que suggère la consigne, et c'est la voie
   la plus propre.
4. Les 200 directions de P3 restent lues **en descriptif**, pour la continuité avec P3. La phrase du texte « T7-P1 garde
   les mêmes 200 directions que P3 » change : réserve déclarée, T7-P1 ne réplique plus le tirage du plancher de P3.

**Voies écartées** :

- Garder 200 pour les seules figées : leurs lectures porteraient l'excès mesuré à 200, soit 2,2 fois le nominal en
  population, regroupé.
- Tirer les directions supplémentaires dans une autre covariance (épisodes honnêtes de 7b, jeux génériques J-D ou J-C) :
  écart à la recette gardée (A6 (2)).

## 7. P3-bis (R-2296) : ce qui changerait la valeur, sans aucune donnée de P3-bis ni de T0.6

Ce qui fixe le besoin en directions, c'est le **rapport entre le bruit du tirage des directions** (écart type du quantile
0,95 de k aires de directions, ∝ 1/√k, indépendant du nombre d'épisodes) **et l'erreur type de la différence par
rééchantillonnage des tâches** (∝ 1/√(nombre de tâches), à structure égale). Donc :

- **Plus de tâches ou d'épisodes indépendants que T0.7** (64 tâches à 10 actions par épisode) : le bruit des directions pèse
  relativement plus. **Il faut monter k à peu près en proportion** du nombre de blocs : par exemple ≈ 1 600 pour 128 tâches,
  à structure égale. Moins de tâches : 800 suffit, avec marge.
- **Un seul jeu décisif ou une queue moins extrême** (sans correction pour quatre sondes) : le défaut résiduel du percentile
  au plafond diminue ; le besoin lié aux directions demeure, mais pèse moins sur un taux nominal plus grand. 800 reste
  prudent.
- **200 directions actuelles, fixées** (celles de P3, si P3-bis les réutilise) : seule la lecture conditionnelle est
  possible. Dans les cellules dures, elle reste juste au-dessus du nominal regroupé (0,0106 [0,0064 ; 0,0164]). Le même
  remède s'applique (directions neuves sous Σ réextraite), avec la même garde d'identité.
- **Recommandation** : rejouer ce script **aux effectifs de P3-bis** (nombre de tâches et d'actions, niveau, nombre de sondes
  lues) avant de sceller P3-bis. Coût ≈ 15 à 40 min de processeur ; ses paramètres sont des constantes de tête. Ne pas
  extrapoler 800 au-delà de 64 tâches.

## 8. Ce que (a') change au module (complète la v2, section 5 ; à faire sur la branche, pas ici)

- **Configuration v7** : `n_plancher` = 800.
- `exiger_configuration` de `lecture_v3` : elle doit accepter 800 en mode réel. Aujourd'hui `lecture_v1` (l. 231-232) et
  `lecture_v2` (l. 205-206) arrêtent tout `n_plancher` ≠ 200 (`N_PLANCHER_REEL`). Ces fichiers ne changent pas : la garde
  neuve vit dans le fichier neuf.
- **Chargeur neuf des planchers des sondes figées** : il remplace le contrôle « nombre (200) » de `charger_planchers_p3`.
  Directions tirées sous Σ réextraite, garde d'identité ; les 200 de P3 restent chargées en descriptif.
- **Notation vectorisée des planchers** (section 5) : fonction neuve, essais d'égalité à `scores_plancher`.
- **Essais R5** : `n_plancher` ≠ 800 refusé en mode réel ; garde d'identité des figées, sur un cas sain (activations
  identiques) et sur un artefact (activations perturbées) ; notation vectorisée égale à la boucle.
- **Texte** : « Métrique » (n = 800 ; plancher des figées tiré de Σ réextraite ; les 200 de P3 en descriptif), « Plan »,
  étape A (réextraction, garde), « Calcul et dépense » (temps de l'étape A).
- **Nœud** déjà ouvert par (a'). Il porte en plus une question de **dépense** : le temps d'instance de l'étape A
  (réextraction, notation si elle n'est pas vectorisée).

## 9. Réserves

- Lois gaussiennes supposées, structure « s1 », quatre sondes lues, comme les v1 et v2.
- Mondes neufs, pas ceux de la v1.
- Directions concentrées (ρ = 4) non rejouées : la v2 montre qu'elles ne dépendent pas du tirage des directions.
- Défaut résiduel du percentile au plafond à 36 tâches (1,4 à 1,8 fois en estimation ponctuelle, non établi).
- Coût de l'étape A mesuré sur séquences simulées en simple précision, 50 et 200 jetons : le nombre réel de jetons notés
  par action n'est pas lu ici.
- Puissance mesurée à ρ = 1 seulement.

## 10. Pièces (scellées, compagnons `.sha256`)

Dossier `docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-t07-v1/` :

- `n_plancher_t07_v1.py` — `e729fac300ba5b4b8e1508a620ae2c1967901d9693b147f88a76776a16135f2d` (entropie
  125504699772186677556879717891676300652, tirée le 2026-11-10 à 23:54:09 UTC) ;
- `n-plancher-nul-v1.json` — `075f9b215e1d10865caaca0fb2fc38c1a55cc42a225d846e50d2cca994ceae6d` ;
- `n-plancher-puissance-v1.json` — `c1acb07b844a1d6fda8bb0efdcf1847839abfa1c205899d4e81c5b2a905c1dff` ;
- `n-plancher-cout-v1.json` — `0c8b0658f0717a5cae4a4412ac9bf34b553a4391b9e0625ec1c7ed9df0e5f808` ;
- `n-plancher-rapport-v1.json` — `2b5c6d78bce18fafb8a186dac9ca6e3cd5f155221b779d4a7f8704083c94f01d` ;
- `n-plancher-rapport-v1.txt` — `36f051d7eeea91de634efcbcdd12ab06976a058c4293c1a56fdf06543c930d75` ;
- `journal-n-plancher-v1.txt` — `42df2d9524bed48456ad3732d8304f4b551b54b6da1c6ae6224f6361f5b915cc`.

Module lu (non versé ici) : `git show adb5f415:src/controle_ia/t07/plancher_v2.py`, `a0f80e68…`, copié dans le bac à sable
`…/scratchpad/agents/nul-t07/module-adb5f415/src/` avec une copie de `src/` de `main` (`gardes`, `evaluation`, `criteres_v1`,
`plancher_v1` vérifiés à leurs empreintes).

Commandes (`python3` = `.venv/bin/python`, `OPENBLAS_NUM_THREADS=1`) :
`python3 -I -B n_plancher_t07_v1.py <racine> <paquet src> erreur_premiere_espece_t07_v1.py nul <sortie>` ; `… puissance
remede-a-puissance-v1.json <sortie>` ; `… cout <sortie>` ; `… rapport <nul> <puissance> <cout> <sortie>`.
