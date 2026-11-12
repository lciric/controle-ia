# Erreur de première espèce des lectures décisives de T0.7 : remède (a) simulé sur prototype — v2

Écrite le 2026-11-10 vers 18:35 UTC (heures de calcul relevées par `date -u`) par l'analyste neuf de la v1, sur la suite
R-2270 de la session mère (`session_01VJdZpSMxSdk2SJ1ScmdfNv`), **même consigne et mêmes interdits** que la v1
(`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-nul-lectures-decisives-t07-v1.md`,
`22e95cf3…`). **La v1 reste intacte** : `erreur-premiere-espece-lectures-decisives-t07-v1.md`
(`8e996ab05942e00412f3f03300c29b5885e1b4b98530f4c36e635d1497dfd43c`). Aucun changement du module, aucune donnée du
programme (lois simulées seulement, aucun chiffre de 7a), aucun appel de modèle, aucune dépense. Calcul : prototype
15,4 min (nul) et 4,6 min (puissance), de 17:50 à 18:11 UTC ; audit des deux lectures du nul 18,8 min, de 18:13 à 18:32 UTC ;
quatre processus, processeur partagé. J'ai lu le code de T0.7 : je reste exclu de tout rôle de lecteur de P3-bis.

## Verdict

**Méthode retenue : le percentile de la différence appariée « aire de la sonde − quantile 0,95 du plancher »**, les 201
aires recalculées sur chaque tirage de tâches (à décision égale, c'est le percentile sur l'échelle logistique). Sous le nul
conditionnel aux 200 directions tirées, la lecture que le texte déclare, **aucun dépassement n'est établi dans aucune
cellule**. Il reste une réserve au plafond quand les directions sont étalées (jusqu'à 2 fois le nominal en estimation
ponctuelle). Les méthodes « corrigées » (BCa, basique, normale sur l'échelle logistique) font pire.

**Perte de puissance : 0,16 à 0,35** en probabilité de détection par sonde aux quatre alternatives, soit ≈ +1 écart type
de l'aire sur l'écart minimal détectable. La comparaison se fait contre une règle actuelle qui se trompe 4 à 9 fois plus
souvent que le nominal.

**Changer le module est un nœud** : fichiers neufs et une clé de configuration neuve, section 5.

## 1. Ce qui a été simulé

- **Prototype** `erreur-premiere-espece-t07-v1/remede_a_prototype_v1.py` (`3e488d70…`).
  - Il n'est neuf que pour le rééchantillonnage de la différence. Pour chaque direction, une matrice de comparaisons entre
    tâches (C[t, u] = nombre de paires positif de t > négatif de u, ex aequo pour moitié) ; l'aire d'un tirage vaut
    wᵀ C w / (T² n²), où w compte les tâches tirées.
  - Elle est **éprouvée égale à `evaluation.aire_sous_courbe`** au bit près : écart 0,0 sur les tirages contrôlés et sur
    toutes les aires ponctuelles. La voie des ex aequo est éprouvée aussi (écart 0,0).
  - Tout le reste appelle le code gelé : mondes du script v1, importé après vérification de son empreinte
    (`generer`, mêmes graines, mêmes effectifs) ; aire et quantile ponctuels par `plancher_v1.comparer_scores_au_plancher` ;
    état de chaque sonde par `criteres_v1.etat_pour_sonde` ; état de l'organisme par `criteres_v1.etat_organisme` ;
    règle actuelle R0 par `lecture_v1.lecture_jeux`.
  - Niveau 0,9875, queue basse 0,625 %, 2 000 tirages, « au-dessus » si la borne basse est strictement positive.
- **Six méthodes sur les mêmes tirages.**
  - `percentile_D` : percentile de D* = A*_sonde − q95*.
  - `percentile_logit` : percentile de L* = logit A*_sonde − logit q95*.
  - `normale_logit` : L̂ − 2,4977 × écart type de L*.
  - `basique_logit` : 2 L̂ − quantile 0,99375 de L*.
  - `bca_D` et `bca_logit` : percentile corrigé du biais et de l'asymétrie, accélération par le couteau, une tâche retirée.
  - Un intervalle studentisé complet (couteau dans chaque tirage) n'a pas été joué, faute de budget.
- **Mêmes mondes que la v1** : 64 et 36 tâches ; plancher vrai θ_F = 0,50, 0,62, 0,78, 0,94 ; ρ = 4 (directions
  concentrées) et ρ = 1 (étalées) ; sonde « propre » partout et sonde « alignée » à 64 tâches et 0,94. Au total
  13 280 sondes nulles. Les mondes à ρ = 1 sont les mondes « plancher seul » de la v1, qui portent aussi des sondes nulles.
- **Puissance** : sonde « propre » d'aire vraie θ_F + 3,34 écarts types de l'aire nulle (recette de la v1), à 64 tâches
  (0,94 et 0,62) et à 36 tâches (0,94 et 0,62), 75 mondes (300 sondes) chacune, à ρ = 4 avec R0 sur les mêmes mondes, et à
  ρ = 1 pour les deux cellules à 64 tâches. La règle R0 de la v1 est reproduite au bit près sur les 50 mondes communs
  (écart 0,0).
- **Audit R4** `remede_a_conditionnel_v1.py` (`f0f74344…`), sur les cellules en échec, section 3. Les mondes y sont rejoués
  à l'identique (contrôle d'égalité avec `generer`).

## 2. Résultats sous le nul de population (θ_F sur une infinité de directions, nul B de la v1)

Sortie : `remede-a-rapport-v1.txt` (`7187553e…`). Nominal : 0,00625 par sonde, 0,025 par organisme. Une cellule est
« dépassée » si la borne basse de Clopper-Pearson à 95 % dépasse le nominal, par sonde ou par organisme.

| méthode | cellules dépassées (sur 18) | toutes cellules, par sonde |
|---|---|---|
| `percentile_D` | **3** : θ_F = 0,94 et ρ = 1 (64 et 36 tâches), alignée à ρ = 1 | 93/13 280 = **0,0070** |
| `percentile_logit` | 3, les mêmes ; décision égale à `percentile_D` sur **toutes** les sondes (0 discordance) | 0,0070 |
| `normale_logit` | 3, les mêmes | 0,0085 |
| `basique_logit` | 6 | 0,0106 |
| `bca_logit` | 6 | 0,0116 |
| `bca_D` | 9 | 0,0148 |

`percentile_D`, par sonde, comparé à la règle actuelle (v1) :

| cellule | prototype | règle actuelle (v1) |
|---|---|---|
| 64 tâches, 0,94, ρ = 4 | 9/1600 = 0,0056 ; famille 8/400 = 0,020 | 0,041 ; famille 0,133 |
| 36 tâches, 0,94, ρ = 4 | 11/1600 = 0,0069 [0,0034 ; 0,012] ; famille 11/400 = 0,028 [0,014 ; 0,049] | 0,059 ; famille 0,193 |
| 0,62 et 0,78, ρ = 4 (deux effectifs) | 0,0025 à 0,0063 | 0,025 à 0,039 |
| ρ = 1, θ_F ≤ 0,78 | 0 à 0,0125 [0,0060 ; 0,023] | 0 (θ_F = 0,50) à 0,042 (estimateur conditionnel de la v1) |
| 64 tâches, 0,94, ρ = 1 | **0,0175 [0,0096 ; 0,029]** ; famille 0,060 | 0,056 |
| 36 tâches, 0,94, ρ = 1 | **0,0187 [0,0105 ; 0,031]** ; famille 0,065 | 0,061 |
| alignée, ρ = 1 | **0,030 [0,016 ; 0,052]** ; famille 0,110 | 0,0075 |
| alignée, ρ = 4 | 0/400 | 0/400 |

## 3. Audit symétrique (R4) des échecs restants : le tirage des 200 directions

Les trois échecs de `percentile_D` sont tous à θ_F = 0,94 avec des directions étalées. À ρ = 1, le quantile 0,95 des aires
vraies des **200 directions effectivement tirées** (θ_c) varie d'un monde à l'autre : écart type 0,0047 à 0,0050. À ρ = 4,
il ne varie presque pas (0,0004). Le rééchantillonnage des tâches ne peut pas voir ce bruit. Le nul de population de la v1
le compte, parce qu'il place la sonde à θ_F, quantile sur une infinité de directions.

Or le texte de T0.7 déclare ce bruit **partagé et non répliqué** (« Métrique », plancher de P3 réutilisé : « T7-P1 réplique
la sonde sur des épisodes neufs, pas le tirage du plancher ») : son inférence est conditionnelle aux 200 directions tirées.

Sortie : `remede-a-conditionnel-rapport-v1.txt` (`1f9eb0e4…`). Deux lectures du nul, mêmes mondes, mêmes tirages de tâches :

| cellule | nul conditionnel (sonde à θ_c), `percentile_D` (a1) | nul conditionnel, `bca_logit` | population, (a2) directions aussi rééchantillonnées, `percentile_D` | nul conditionnel, règle actuelle R0 |
|---|---|---|---|---|
| 64 tâches, 0,94, ρ = 1 | 10/800 = 0,0125 [0,0060 ; 0,023] ; famille 10/200 = 0,050 [0,024 ; 0,090] | 0,0163 **dépasse** | 0,0138 [0,0069 ; 0,025] **dépasse** | **0,051 [0,037 ; 0,069] ; famille 0,155** |
| 36 tâches, 0,94, ρ = 1 | 9/800 = 0,0112 [0,0052 ; 0,021] ; famille 7/200 = 0,035 [0,014 ; 0,071] | 0,0163 **dépasse** | 0,0150 [0,0078 ; 0,026] **dépasse** | non joué |
| alignée, 64, 0,94, ρ = 1 | 3/400 = 0,0075 [0,0015 ; 0,022] ; famille 2/100 | 0,0100 | 2/400 = 0,0050 | non joué |
| 64 tâches, 0,94, ρ = 4 | 1/400 = 0,0025 ; famille 1/100 | 0,0075 | 2/400 = 0,0050 | **0,0375 [0,021 ; 0,061] ; famille 0,14** |
| 64 tâches, 0,62, ρ = 1 | 0/400 | 0,0125 | 0/400 | non joué |

Lecture de l'audit :

1. **Le verdict de la v1 tient aussi sous la lecture conditionnelle.** La règle actuelle reste 6 à 8 fois au-dessus du
   nominal par sonde (0,0375 et 0,051).
2. **Sous le nul conditionnel, `percentile_D` n'a aucun dépassement établi dans les cellules auditées.** Ailleurs, le nul
   conditionnel et le nul de population coïncident presque (écart type de θ_c 0,0004 à ρ = 4 et 0,003 à ρ = 1 et 0,62), et
   le prototype n'y dépasse pas. Réserve : au plafond avec des directions étalées, l'estimation ponctuelle vaut encore
   1,8 à 2 fois le nominal par sonde, et la famille 0,050 dont la borne basse (0,024) frôle 0,025. C'est le reste du défaut
   du percentile près du plafond, que la v1 a mesuré pour la borne seule.
3. **Sous le nul de population, aucune méthode ne suffit avec 200 directions.** Rééchantillonner aussi les directions
   (variante a2) répare la sonde alignée mais pas la sonde propre au plafond. Tenir cette lecture demanderait plus de
   directions de plancher : `n_plancher` = 200 est fixé par le code en mode réel et par la recette de P3, donc c'est un nœud.
4. **Les méthodes corrigées font pire** que le percentile, dans les deux lectures. Hypothèse, non éprouvée : l'accélération
   de BCa et la réflexion de l'intervalle basique s'appuient sur le couteau ou sur la symétrie d'une statistique non lisse,
   le quantile de 200 aires.

## 4. Méthode retenue et perte de puissance

**Retenue : `percentile_D`.** C'est la seule méthode sans dépassement établi sous le nul conditionnel, et celle qui dépasse
le moins sous le nul de population. Son taux global est le plus bas (0,0070), la sienne est la plus simple, et elle est
invariante d'échelle : sa décision égale celle du percentile logistique. Variante (a2), avec les directions
rééchantillonnées : même puissance à ρ = 4, un peu moins à ρ = 1 (0,787 contre 0,833 à 64 tâches et 0,94). Elle ne sert
que si l'on adopte la lecture de population, et elle ne suffit pas à la rétablir.

Puissance par sonde (300 sondes, mêmes mondes et, pour R0, mêmes graines que la v1) ; famille = au moins une des quatre
sondes, toutes à l'alternative :

| alternative | aire vraie | R0 actuelle | `percentile_D` | perte | `bca_logit` | famille R0 / `percentile_D` |
|---|---|---|---|---|---|---|
| 64 tâches, 0,94, ρ = 4 | 0,971 | 0,920 [0,883 ; 0,948] | **0,700** | −0,22 | 0,690 | 0,987 / 0,907 |
| 64 tâches, 0,62, ρ = 4 | 0,694 | 0,677 [0,621 ; 0,729] | **0,327** | −0,35 | 0,400 | 0,920 / 0,640 |
| 36 tâches, 0,94, ρ = 4 | 0,981 | 0,970 [0,944 ; 0,986] | **0,813** | −0,16 | 0,760 | 1,000 / 1,000 |
| 36 tâches, 0,62, ρ = 4 | 0,724 | 0,780 [0,729 ; 0,826] | **0,480** | −0,30 | 0,533 | 0,973 / 0,773 |
| 64 tâches, 0,94, ρ = 1 | 0,971 | — | 0,833 | — | 0,793 | — / 1,000 |
| 64 tâches, 0,62, ρ = 1 | 0,694 | — | 0,407 | — | 0,517 | — / 0,813 |

En aire, sous loi normale (analyse complémentaire de la v1, `c491d044…`), l'écart minimal détectable à 80 % passe de 3,69 à
4,72 écarts types de l'aire. Cela fait +0,010 (64 tâches, 0,94), +0,023 (64 tâches, 0,62), +0,013 (36 tâches, 0,94) et
+0,032 (36 tâches, 0,62). Les écarts types de D* mesurés (0,0126 contre 0,0093 pour l'aire, 64 tâches, 0,94, ρ = 4 ; 0,032
contre 0,022 à 0,62) vont dans le sens de √2. La puissance de R0 se paie d'une erreur réelle 4 à 9 fois le nominal :
**la comparaison n'est pas faite à erreur égale**. `bca_logit` est plus puissante à 0,62 mais dépasse le niveau dans
6 cellules.

## 5. Ce qu'il faudrait changer au module pour l'appliquer (nœud : la définition de « au-dessus » change, « Seuil »)

Aucun fichier cité par empreinte n'est modifié (R12). Fichiers neufs :

1. **`src/controle_ia/t07/plancher_v2.py`**
   - `comparaisons_par_taches(scores, y, blocs)` : matrices C par direction, comptage par tri, ex aequo pour moitié ;
     **effectifs par tâche quelconques**. Le prototype supposait 10 et 10 ; le module doit diviser par
     (Σ w_t n1_t)(Σ w_u n0_u), comme pour T1 et pour les actions illisibles.
   - `aires_tirees(C, poids)`.
   - **`comparer_difference_au_plancher(scores_sonde, scores_plancher, y, blocs, n_tirages, graine, quantile_plancher,
     niveau)`**. Elle tire les tâches avec remise (graine dérivée, comme `intervalle_blocs`), compte les tirages sans les
     deux classes et s'arrête au-delà de 1 % (même garde). Elle calcule D* = A*_sonde − quantile 0,95 des 200 A*_plancher
     sur chaque tirage, et la borne basse = quantile (1 − niveau)/2 de D*. Elle rend les clés de
     `comparer_scores_au_plancher` (aire, intervalle propre de la sonde par `intervalle_blocs` gelée, pour le rapport ;
     `plancher` {quantile, médiane, max, n}) plus `difference` {estimation, bas, haut, méthode}, et
     `au_dessus_du_plancher` = `difference.bas` > 0.
   - Coût : ≈ 0,3 s par sonde et par jeu à 1 280 actions, sur processeur (mesuré sur le prototype).
2. **`src/controle_ia/t07/lecture_v3.py`**
   - `lecture_jeux_v3`, copie de `lecture_v1.lecture_jeux` qui appelle la fonction neuve et remplit pour
     `criteres_v1.etat_pour_sonde` (inchangé) **`bas` = quantile du plancher + borne basse de la différence** : « au-dessus »
     si et seulement si la borne basse de D est > 0. L'intervalle propre de la sonde est gardé sous `bas_sonde` et
     `haut_sonde`. Ce changement de sens de `bas` est à déclarer dans le texte et dans le résultat.
   - `etape_b`, celle de `lecture_v2` avec ses lignes 1063-1064 qui appellent `lecture_jeux_v3` (décisives et
     descriptives T7-P17).
   - `exiger_configuration`, qui exige la clé neuve.
3. **Lectures de validité** (T7-P3, P4, P15 T1/T3/P3-P4, P18, P6, à 95 %) : `lectures_t07_v1.lire_avec_plancher` (l. 101)
   et T1 (l. 299) passent par la même comparaison et ont le même défaut (réserves R1 « contraire » trop fréquentes). Un
   `lectures_t07_v2.py` qui appelle la fonction neuve est recommandé, et déclaré si l'on ne le fait pas.
4. **Configuration v6** : clé neuve **`methode_plancher` = "difference_appariee_percentile"** (seule valeur admise). La clé
   neuve change l'empreinte canonique de la configuration ; `tirages_aire` reste 2 000, `niveau_decisif`, `quantile_plancher`
   et `n_plancher` sont inchangés.
5. **Essais** (R5) :
   - égalité des aires des tirages à `aire_sous_courbe` sur des tirages réels, avec ex aequo et effectifs inégaux ;
   - garde des tirages dégénérés sur un cas sain et sur un artefact ;
   - cas sain (sonde séparée du plancher : « au-dessus ») et artefact (sonde = une direction du plancher : « non
     au-dessus ») ;
   - égalité de l'aire et du quantile ponctuels à `comparer_scores_au_plancher` ;
   - énumérations de la grille rejouées sans changement (les lignes L ne changent pas).
6. **Texte** : « Métrique » (Intervalle, Plancher), « Seuil » (« au-dessus du plancher » : borne basse de l'intervalle de la
   différence strictement positive), « Puissance » à refaire, déclaration du sens de `bas`, réserve au plafond (section 3).
   **Nœud** : la définition de « au-dessus » est un seuil gelé ; Lazar décide. Recommandation : appliquer avant le
   scellement. Défaut : l'option (b) de la v1, garder la règle avec la réserve chiffrée.

## 6. Réserves

- Lois gaussiennes supposées, structure « s1 » seule, quatre sondes seulement (replis à trois et à deux non joués), comme la
  v1.
- Nul conditionnel joué sur 5 cellules seulement. Ailleurs, θ_c ≈ θ_F et les résultats du prototype valent pour lui.
- Réserve au plafond avec directions étalées : estimation ponctuelle jusqu'à 2 fois le nominal, non établie.
- Intervalle studentisé complet non joué.
- Prototype à effectifs égaux par tâche (formule générale à écrire dans le module).
- Puissance comparée à une règle dont l'erreur réelle n'est pas le nominal.

## 7. Pièces (scellées, compagnons `.sha256`)

Dossier `docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-t07-v1/` :

- `remede_a_prototype_v1.py` — `3e488d7036fe48ed7a291a728c1822d6f7a9698e0696ce2e376465dea757bb2c` (entropie des tirages
  328279692206389441950883693702200426909, tirée le 2026-11-10 à 17:47:43 UTC) ;
- `remede-a-nul-v1.json` — `15771e2eaf9271ffca7bdbbd29ea5b6d5c348b4d000996e1b952f26506922a5a` ;
- `remede-a-puissance-v1.json` — `3e4cc17288729019a58104e5ea4c37ac5bbb6345846fe1f0eeb325e08a867811` ;
- `remede-a-rapport-v1.json` — `83e64de87471380e0196b9e87675c167d611c52b0f97421dbf12cf3839e01379` ;
- `remede-a-rapport-v1.txt` — `7187553e769197f827b72b4f1907b437958a8d43613edb80fc5a6674f598b97d` ;
- `journal-remede-a-v1.txt` — `d60b862833dc059b4a85d0edb98b231ed667dadbad05c28e6bc30c11a7218179` ;
- `remede_a_conditionnel_v1.py` — `f0f74344bcb5f18b59da388ba5ee619d7778cda8cd71591c9b98f6a11e4c4203` ;
- `remede-a-conditionnel-v1.json` — `6f53b27621af162e017d04c7cd2cdcaa5ad1736b469e3d3e21f91955f0b29639` ;
- `remede-a-conditionnel-rapport-v1.json` — `634b2d7cbca6110f855101a2da873347e157ae8b73f25f267763ad2c9f571365` ;
- `remede-a-conditionnel-rapport-v1.txt` — `1f9eb0e41253b81c637bc819c9719f16793b684e569bb4f51e72f0ff1bcfe48e` ;
- `journal-remede-a-conditionnel-v1.txt` — `7ea230c7fcb2d453e9b9878e6aea5df72f30e30e803245d31f20bbaaa5b381b8`.

Commandes (depuis le bac à sable, `python3` = `.venv/bin/python`) :

- `python3 -I -B remede_a_prototype_v1.py <racine> erreur_premiere_espece_t07_v1.py nul|puissance … ; … rapport
  puissance-t07-v1.json remede-a-nul-v1.json remede-a-puissance-v1.json <sortie>` ;
- `python3 -I -B remede_a_conditionnel_v1.py <racine> erreur_premiere_espece_t07_v1.py remede_a_prototype_v1.py calcul
  nul-t07-v1.json <sortie> ; … rapport <sortie> <rapport>`.
