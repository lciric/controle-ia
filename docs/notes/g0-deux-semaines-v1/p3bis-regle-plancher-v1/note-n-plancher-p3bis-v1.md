# Nombre de directions du plancher pour la règle (a') au jeu décisif de P3-bis (PB-1) — v1

Écrite le 2026-11-11 vers 06:50 UTC (heures relevées par `date -u`) par l'analyste neuf de l'erreur de première espèce des
lectures décisives de T0.7 (notes v1 à v3 : `docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v1.md`,
`-v2.md`, `-v3.md`, celle-ci `760a562c…`). Demande de la session mère (R-2296 : P3-bis prend exactement la règle de T0.7 sous
(a') ; R-2298 : `n_plancher` = 800 retenu pour T0.7). Même consigne et mêmes interdits
(`consigne-nul-lectures-decisives-t07-v1.md`, `22e95cf3…`).

**Ce qui a été lu de P3-bis** : seulement les sections « Métrique », « Seuil » et le point 10 du plan (« Puissance ») du
brouillon 12, `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon12.md`
(`07b160630811c88eb6a139c89b904f9beb3ea5a8e335948ebec1068ec93cb1f6`, vérifié par `sha256sum`), en lecture de conception.
Aucune donnée de P3-bis, aucune sortie de course, aucun `diag/` ni `runs/`, rien de 7a, de 7b ni de T0.6, rien sous
`docs/notes/bras-attaque/`. Aucun appel de modèle, aucune dépense ; rien n'est committé. Calcul : 06:23 à 06:48 UTC
(≈ 25 min), quatre processus, un fil chacun.

## Verdict

**k recommandé pour P3-bis : 800**, la même valeur que T0.7.

- **Niveau.** Aux effectifs de PB-1 (60 tâches, 10 actions par épisode, A contre T, une seule sonde, 95 % : nominal 0,025
  d'un côté), la règle (a) n'a **aucun dépassement établi** à 200, 400, 800 ni 1 600 directions, sous les deux lectures
  du nul.
  - À 800, dans la cellule la plus dure (plafond 0,94) : **0,0200 [0,0115 ; 0,0323]** en population, **0,0163** en
    conditionnelle.
  - À 200, l'estimation ponctuelle dépasse le nominal au plafond (0,0325). 400 tombe juste au nominal (0,0250). 800 tient
    avec marge.
  - Au plancher analogue de P3 (0,58), toutes les valeurs de k donnent 0,008 à 0,010.
- **La règle actuelle de P3-bis dépasse de façon établie**, même au plancher analogue de P3 : **0,0417 [0,0271 ; 0,0609]**
  (1,7 fois), et 0,096 au plafond.
- **Puissance.** Aire minimale détectable à 80 % sous la règle (a), au plancher analogue de P3 (loi simulée) : **0,680** à
  tout k, contre 0,657 pour la règle actuelle sur les mêmes mondes, soit **+0,023**. Transposé aux valeurs écrites du
  brouillon 12 (0,6389 à 0,6585), cela donne **≈ 0,662 à 0,682**.
- **Coût** à la lecture : 1,69 s par sonde et par jeu à 800 directions (0,48 s pour la règle actuelle). La notation en
  ligne des planchers par la chaîne de P3-bis est à mesurer (section 5).

## 1. Effectifs et règle simulés

**Effectifs de PB-1** (brouillon 12) :

- jeu décisif `saboteur-temoin`, A contre T ;
- 60 tâches = 60 blocs (« une tâche = un bloc ») ;
- un épisode par emplacement et par tâche, 10 actions par épisode : ≈ 600 actions contre 600 (plan point 10 : « ≈ 10 actions
  par bloc et par condition, ≈ 1 200 actions ») ;
- **une seule sonde et un seul jeu décisifs, intervalle à 95 % sans correction** (« Seuil ») : la queue jouée par la règle
  est 0,025 d'un côté ;
- plancher actuel : 200 directions tirées dans la course, avec la covariance des jetons d'entraînement que la course de
  P3-bis réextrait.

**Règle (a)** : celle du module préparé (`plancher_v2.py`, commit `adb5f415…`, fichier `a0f80e68…`), au niveau 0,95 :
percentile, par blocs de tâches, de D = aire de la sonde − quantile 0,95 des aires du plancher (201 aires recalculées par
tirage) ; « au-dessus » si la borne basse de D est > 0.

**Simulation** : script `p3bis_n_plancher_v1.py` (`8d7d94fc…`).

- Il réutilise, par son chemin et après vérification de son empreinte, `n_plancher_t07_v1.py` (`e729fac3…`) : comparaisons,
  aires des tirages, décision par `plancher_v2.resume_pour_critere` et `criteres_v1.etat_pour_sonde`.
- Il est **contrôlé égal au bit près à `comparer_difference_au_plancher`** sur la première sonde du premier monde de chaque
  lot, à k = 200 et 1 600 : 50 lots sous le nul (écart 0,0 écrit) et 40 lots de puissance (tout écart aurait arrêté le
  calcul).
- Loi des scripts précédents (structure « s1 »). À 60 tâches, son erreur type d'une aire (≈ 0,022 à 0,6) est dans la fourchette
  que le brouillon 12 rapporte pour les jeux de P3 (0,0173 à 0,0223 ; 0,0219 sur le jeu décisif).
- Mondes neufs à 1 600 directions par sonde, sous-ensembles emboîtés k = 200, 400, 800, 1 600 ; directions étalées (ρ = 1),
  le cas où le tirage des directions pèse.
- Deux lectures du nul :
  - population : directions retirées, sonde à θ_F ;
  - conditionnelle : sonde au quantile 0,95 des aires vraies des k directions lues.
- Cellules : θ_F = 0,94 (plafond, 200 mondes, 800 sondes), 0,78 (150 mondes), **0,58** (analogue du plancher de P3 sur le
  jeu décisif, 0,5776, plan point 10 ; 150 mondes).
- Règle actuelle de P3-bis jouée sur les mêmes mondes à 0,94 et 0,58 : percentile de l'aire de la sonde contre quantile du
  plancher, 200 directions, 95 %, par `plancher_v1.comparer_scores_au_plancher` (équivalente à `statistiques.detection` de
  P3).
- Écriture lot par lot (reprise possible après un redémarrage), parties effacées après assemblage.

## 2. Erreur de première espèce (nominal 0,025 ; Clopper-Pearson à 95 %)

Sortie : `t07-module-v2/erreur-premiere-espece-t07-v1/p3bis-n-plancher-rapport-v1.txt` (`f159a471…`).

| θ_F | k | population | conditionnelle | écart type de θ_c |
|---|---|---|---|---|
| 0,94 | 200 | 26/800 = 0,0325 [0,0213 ; 0,0473] | 12/800 = 0,0150 [0,0078 ; 0,0261] | 0,0049 |
| | 400 | 20/800 = 0,0250 [0,0153 ; 0,0383] | 12/800 = 0,0150 | 0,0035 |
| | **800** | **16/800 = 0,0200 [0,0115 ; 0,0323]** | **13/800 = 0,0163 [0,0087 ; 0,0276]** | 0,0023 |
| | 1600 | 17/800 = 0,0213 [0,0124 ; 0,0338] | 14/800 = 0,0175 | 0,0016 |
| | règle actuelle, 200 | **77/800 = 0,0963 [0,0767 ; 0,1188] : dépasse** | — | — |
| 0,78 | 200 | 10/600 = 0,0167 [0,0080 ; 0,0304] | 9/600 = 0,0150 | 0,0057 |
| | 400 | 11/600 = 0,0183 | 11/600 = 0,0183 | 0,0040 |
| | **800** | **9/600 = 0,0150 [0,0069 ; 0,0283]** | **10/600 = 0,0167 [0,0080 ; 0,0304]** | 0,0027 |
| | 1600 | 8/600 = 0,0133 | 12/600 = 0,0200 | 0,0020 |
| 0,58 | 200 | 5/600 = 0,0083 [0,0027 ; 0,0193] | 0,0083 | 0,0019 |
| | **800** | **6/600 = 0,0100 [0,0037 ; 0,0216]** | **5/600 = 0,0083** | 0,0010 |
| | 400 et 1600 | 0,0083 | 0,0083 | — |
| | règle actuelle, 200 | **25/600 = 0,0417 [0,0271 ; 0,0609] : dépasse** | — | — |

Lecture :

1. **800 directions tiennent le nominal aux effectifs de P3-bis**, sous les deux lectures et dans les trois cellules, avec
   une marge au plafond (estimation 0,020 pour 0,025).
2. **Pourquoi P3-bis est moins exigeant que T0.7.** La queue y est bien moins extrême (0,025 contre 0,00625), si bien que le
   défaut du percentile près du plafond et le bruit du tirage des directions pèsent moins, en relatif. Les effectifs sont
   voisins (60 tâches contre 64).
3. Le besoin en directions ne dépasse donc pas celui de T0.7.
   - À 200 directions, l'estimation au plafond dépasse le nominal (0,0325 : 1,3 fois, non établi). À 400, elle l'égale.
   - **800 est la plus petite valeur qui laisse une marge au plafond** ; c'est aussi celle de T0.7, et la même règle aux deux
     textes évite deux recettes de plancher.
   - Au plancher analogue de P3 (0,58), k ne change rien.
4. **La règle actuelle de P3-bis ne tient pas son niveau**, même au plancher analogue de P3 : 1,7 fois le nominal, établi.
   C'est le premier mécanisme de la v1 (quantile du plancher bruité, pris pour un seuil fixe), et une raison de plus
   d'appliquer (a') à P3-bis.

## 3. Puissance et aire minimale détectable (lecture de population, θ_F = 0,58, ρ = 1, 160 sondes par point)

| aire vraie | k = 200 | 400 | **800** | 1600 | règle actuelle (200) |
|---|---|---|---|---|---|
| 0,62 | 0,106 | 0,113 | 0,106 | 0,106 | 0,275 |
| 0,64 | 0,375 | 0,362 | **0,362** | 0,369 | 0,644 |
| 0,66 | 0,625 | 0,613 | **0,619** | 0,613 | 0,831 |
| 0,68 | 0,787 | 0,806 | **0,800** | 0,806 | 0,912 |
| 0,70 | 0,925 | 0,919 | **0,912** | 0,919 | 0,981 |
| **aire minimale détectable à 80 %** | 0,6818 | 0,6794 | **0,6800** | 0,6794 | 0,6567 |

L'aire minimale est interpolée linéairement. Chaque puissance porte une erreur type d'environ 0,03 à 0,04 (160 sondes) ;
l'aire minimale, environ ± 0,005 à 0,01.

**Comparaison aux valeurs écrites du brouillon 12** (0,6389 à l'analogue de P3, 0,6585 à l'enveloppe prudente) :

- Ces valeurs viennent d'une formule normale à seuil fixe (plancher 0,5776 tenu pour connu, erreur type 0,0219) appliquée
  à la règle actuelle.
- Sur la loi simulée ici, la même règle actuelle donne 0,6567, plus haut que la formule : le plancher y est estimé, donc
  bruité.
- **La règle (a) coûte +0,023 d'aire sur les mêmes mondes** (0,6800 contre 0,6567). Transposé additivement aux valeurs
  écrites, cela donne une aire minimale **≈ 0,662 (analogue de P3) à ≈ 0,682 (enveloppe)**. Puissance simulée sous (a) à
  l'analogue : 0,36 à 0,64, 0,62 à 0,66, 0,91 à 0,70 (le brouillon 12 écrit, pour la règle actuelle à l'enveloppe, 0,504,
  0,818 et 0,997).
- Si le texte planté élevait le plancher à 0,65 ou 0,70 (brouillon 12 : 0,7124 et 0,7624 sous la règle actuelle), le même
  décalage donnerait ≈ 0,735 et ≈ 0,785. Ce cas **n'est pas simulé** ; le décalage peut y différer.
- La puissance de la règle actuelle se paie d'une erreur réelle de 0,042 au lieu de 0,025 : **la comparaison n'est pas
  faite à erreur égale**.

## 4. Ce qui change dans P3-bis (nœud de son texte ; rien n'est fait ici)

- **Seuil** : « au-dessus » devient la borne basse de l'intervalle de D strictement positive, règle (a) de T0.7, au niveau
  95 % de PB-1. **Métrique** : plancher de 800 directions pour les sondes principales lues ; règle, fonction et graine
  écrites.
- **Directions de P3-bis** : la course de P3-bis réextrait les jetons d'entraînement et tire ses planchers par
  `plancher_apparie` ; la covariance est donc disponible, contrairement aux sondes figées de T0.7. `plancher_apparie` tire
  les directions **l'une après l'autre** (`w = L @ rng.standard_normal(d)`, et q aussi pour l'attention). En gardant la
  graine de P3 et en demandant 800 directions, **les 200 premières sont celles de P3** si la covariance réextraite est
  identique. L'identité de PB-9 (430 empreintes contre P3) reste alors éprouvable sur ces 200 ; les 600 suivantes sont
  neuves, sans référence dans P3, et déclarées comme telles.
- **PB-13** (descriptive, mêmes 200 directions que la lecture de P3) : à aligner sur 800 ou à garder déclarée.
- **Puissance** : le point 10 du plan est à refaire sous la règle (a). Ordre de grandeur : section 3.

## 5. Coût

**Lecture** (mesuré sur le module, un fil, 1 200 actions, 60 blocs, 2 000 tirages, 95 % ; `p3bis-n-plancher-cout-v1.json`,
`67433491…`), par sonde et par jeu :

| règle | temps |
|---|---|
| règle actuelle, 200 directions | 0,48 s |
| (a), 200 | 0,84 s |
| (a), 400 | 1,07 s |
| **(a), 800** | **1,69 s** |
| (a), 1 600 | 2,99 s |

C'est négligeable pour un jeu décisif et quelques jeux descriptifs.

**Notation en ligne des planchers dans la course de P3-bis** (« chaque action notée en ligne par les 30 sondes et les
400 sondes des planchers ») : à 800 directions par sonde principale, 1 600 directions au lieu de 400. **Non mesuré sur la
chaîne de P3-bis.** Si elle passe par la boucle du harnais mesurée pour T0.7 (v3 : 235 à 904 µs par direction et par action,
un fil), les 1 200 directions de plus sur 2 400 actions coûteraient 11 à 43 min d'un fil. C'est moins sur 30 fils, ou en
notation matricielle, d'où une hausse modeste du temps d'instance. **À mesurer à la répétition de P3-bis et à porter au
devis** : son temps d'instance est une dépense.

## 6. Réserves

- Lois gaussiennes supposées, structure « s1 ». Directions étalées seulement : le cas concentré dépend moins du tirage des
  directions (v2).
- L'analogue de P3 est pris comme θ_F = 0,58 dans cette loi. Le plancher de P3 n'y est pas reproduit à l'identique, et
  l'erreur type n'est pas réglée à part.
- Aire minimale transposée par décalage additif : approximation.
- Mondes neufs (graine propre), non ceux des notes v1 à v3.
- Le texte de P3-bis peut changer d'ici son scellement. Le script se rejoue en changeant ses constantes de tête (`N_TACHES`,
  `NIVEAU`, cellules).

## 7. Pièces (scellées, compagnons `.sha256`)

Dossier `docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-t07-v1/` :

- `p3bis_n_plancher_v1.py` — `8d7d94fcf37ddc1775b32388cc0d3185f840ae54fc5e98ecc1328786172e63a1` (entropie
  293131213384775381821918802937715290225, tirée le 2026-11-11 à 06:21:37 UTC) ;
- `p3bis-n-plancher-nul-v1.json` — `a2791df2af13dccfc180e020d2b8d82671cc808dbc024cf4d01d50d696f4e088` ;
- `p3bis-n-plancher-puissance-v1.json` — `750a1431edf9a6880c5f91271bd893f37260489b390901d5569183edef6a3a3f` ;
- `p3bis-n-plancher-cout-v1.json` — `67433491c1a57037a58d611f150bec97b984dbe647dd7ee4cbc20933036d37b4` ;
- `p3bis-n-plancher-rapport-v1.json` — `325dbd33398c5e20b5befb99382f1f8d8481f78d0fd0a2d974d398d682a3d6a5` ;
- `p3bis-n-plancher-rapport-v1.txt` — `f159a4710bf665211b4093debafe71b932ab69523759db862cdddff6e3f9d663` ;
- `p3bis-journal-n-plancher-v1.txt` — `5a50f6661df1fa48c5236a349c1d7a240160d41cb96b5ba57d5df557f5d32f5c`.

Commande (`python3` = `.venv/bin/python`, `OPENBLAS_NUM_THREADS=1`) :
`python3 -I -B p3bis_n_plancher_v1.py <paquet src avec plancher_v2 d'adb5f415> erreur_premiere_espece_t07_v1.py
n_plancher_t07_v1.py nul|puissance|cout <sortie>` ; `… rapport <nul> <puissance> <sortie>`.
