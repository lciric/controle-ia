# Préenregistrement — Gu et Krenn 2024 : reproduction de l'aire sous la courbe et test hors échantillon, v2 (BROUILLON, NON SCELLÉ)

- Auteur : lignée « session-depot » (Claude, Opus 5.5), sur le message n° 261 de conv-audit (mot de Lazar relayé,
  R-621), point 2 (« préenregistrement court, scellé avant le test hors échantillon, contre-lu par un autre modèle ») et
  point 3 (critère de mort).
- Date (UTC) : 31 octobre 2026, 03:05 (`date -u`).
- Version : v2, écrite après la contre-lecture 1 de la v1 (section « Constats de la contre-lecture → sort » en fin de
  texte). La v1 reste en place, non modifiée : `docs/notes/gu-krenn-v1/prereg-gu-krenn-reproduction-et-hors-echantillon-v1.md`
  `1920d1504f0eabda3ba5bd8cb6e80db9013c2738a67cb232d42c6fa1499154cb`.
- **Non scellable en l'état** : (1) décision de Lazar sur la fenêtre du test B (encadré « Décision ouverte D-GK-1 »,
  section Plan) ; (2) code d'analyse et tests des gardes écrits, testés, commités, commit inscrit ci-dessous ;
  (3) numéros de versions épinglées inscrits ; (4) contre-lecture 2 de cette v2 ; (5) devis et GO (nœud de dépense).
- Commit du code d'analyse : aucun encore. Le code d'analyse (`scripts/gu_krenn_*_v1.py`) et les tests de ses gardes
  (`tests/test_gu_krenn_gardes_v1.py`) seront scellés et leur commit inscrit ici **avant** le scellement.
- Nature : pas une porte du programme. Décide seulement du sort du bras Gu-Krenn du bisociateur exploratoire de la
  course 2. Aucune dépense couverte : machine louée et téléchargements lourds = nœud de dépense, devis et GO de Lazar.
- **Convention des chiffres.** « [p. N] » = lu sur le PDF empreinté, page imprimée N (R7). « SUPPOSÉ » = tout autre
  chiffre : estimation, valeur lue dans leur code ou dans des métadonnées, ou paramètre choisi ici sans appui publié.
- Documents qui font foi (chemin, empreinte complète) :
  - PDF arXiv 2402.08640 v4 du 11 juin 2025 : `docs/sources/pdf/bisociation-fertilite-v1/arxiv-2402.08640-gu-krenn-2024.pdf`
    `6b3d29db7cd6f7dec0c10afb5f6612e598d0e9fc8ece4eb72b34e652c6630fdb`
  - État des lieux : `docs/notes/gu-krenn-v1/etat-des-lieux-gu-krenn-v1.md`
    `1c1618a2484b542e534b74fc12906212c6284d41d0bc691722e4a209499f67e9`
  - Message n° 261 : `origin/canal/conv-audit-n04` (`3ce4a96dd76072c10bb0fe753181a6d83bde45de`) :
    `brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-10-30_n261.md`
    `f6981503f10c1da0bf0bc8fdd68f95ab0e182541e13898839a74128566d0a3bb` ; brief
    `…/envois/brief-nouvelle-lignee-bisociateur-v1.md` `2cdf135fff340960a3499e44977557d5ae49e121d142dca48ec39a1ba01321b1`
  - Leur code, tête `d2af4f3d69e1e5272c168d3f950b56b31845a51f`, sous `docs/notes/gu-krenn-v1/sources-amont-v1/Impact4Cast/` :
    `train_model_2022_run.py` `b5aaa9408456c1a83fe207ef43351e9b6ba8bb9e33a3a60d4852ec360303baa5`,
    `train_model_2019_run.py` `63b20513af30497e8aa62310cef52e25ac3576ca81d600efd0a5832891ee0592`,
    `features_utils.py` `b055591c47517e64ab06b01481db004aab6a324e68ce13d0a538803aea111520`,
    `prepare_eval_data/prepare_eval_feature_data.py` `fb622e29fbd95e5d1892d6a29ec0da56551bb038350cf7b335083c945b93e10a`,
    `benchmark_code/loops_fcNN.py` `919e722f57a293ee3d5627ecd214821c281f3ad5dd5e08ca7b2ac794b775207e`
    (et, pour les citations de lignes ajoutées en v2, `preprocess_utils.py`, `train_model_utils.py`,
    `fpr_example/plot_FPR.py`, chacun avec son compagnon `.sha256` dans le même dossier)
  - Rapport de la contre-lecture 1 : `docs/notes/gu-krenn-v1/contre-lecture-1-prereg-gu-krenn-v1-rapport-v1.json`
    `12a4978b1b4896151940211c671e033c2b5fac8f0b7ca04129c8de04cd2fe74a`
  - Gabarit : `prereg/gabarit-preregistrement-v1.md` `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`

## Hypothèse

Le classeur de Gu et Krenn (réseau entièrement connecté sur 141 traits [p. 4] d'un graphe de 37 960 concepts d'optique
et de physique quantique [p. 3]) est un instrument utilisable pour le bras Gu-Krenn du bisociateur. « Utilisable »
s'entend au sens strict des seuils ci-dessous : **non réfuté** par ce test, pas démontré fiable.

- **HA (reproduction)** : réentraîné à partir de leur code et de leurs données publiées, sur leur partage temporel, il
  retrouve leurs aires sous la courbe publiées (aucun poids n'est publié : réentraîner est obligatoire).
- **HB (hors échantillon)** : figé avant toute lecture des données postérieures à 2022, il classe les paires de concepts
  non reliées à fin 2022 qui se relient ensuite (fenêtre F, décision D-GK-1 : recommandée F = 1er janvier 2023 –
  30 septembre 2026 ; littérale F = 1er janvier 2024 – 30 septembre 2026) au-dessus des paires qui restent non reliées,
  **à degré et âge égaux**, et mieux que deux règles simples (attachement préférentiel, similarité de Simpson seule).

Hypothèses de travail : leur graphe publié (instantané OpenAlex ; la page 3 donne « avril 2023 » pour la coupure des
arêtes et « février 2023 » pour l'instantané [p. 3] — dans les deux cas après le 31 décembre 2022) est complet pour les
articles publiés jusqu'au 31 décembre 2022 ; la dérive de la base OpenAlex actuelle (« Walden », novembre 2025 —
SUPPOSÉ, notes de version du seau public) est contrôlée par le pont (Plan, étape B2). Leur modèle prédit l'**impact**
(au moins IR citations dans les trois ans [p. 4]) et non l'apparition pure : HB est donc un transfert de tâche, déclaré
comme tel.

## Prédiction chiffrée et signe attendu

**(A) Reproduction** — aucun signe d'écart attendu (bilatéral). Valeurs cibles, une seule course publiée chacune :

| Cas | Cible publiée | Statut |
|---|---|---|
| A1 banc, entraînement 2016→2019, évaluation 2019→2022, IR = 10 : réseau / XGBoost | 0,9455 / 0,9442 [p. 7, fig. 6(a)] | réseau décisif ; XGBoost information |
| A1 banc, même découpage, IR = 50 : réseau / XGBoost | 0,9588 / 0,9561 [p. 7, fig. 6(b)] | réseau décisif ; XGBoost information |
| A2 principal, entraînement 2016→2019, évaluation 2019→2022, IR = 10 / 50 / 100 | 0,94 / 0,96 [p. 12, fig. 11] / **0,948** [p. 12, annexe D ; p. 13, fig. 12] | décisif |

Pour IR = 100, la cible unique est 0,948 (trois décimales, même expérience que le 0,95 arrondi de la fig. 11 [p. 12]).

Prédiction : chaque moyenne sur trois graines (nombre SUPPOSÉ, choisi ici) tombe à moins de 0,010 de sa cible pour A1, à
moins de 0,015 pour A2 (tolérances SUPPOSÉ, choisies ici : variance d'une graine à l'autre non publiée ; A2 publié
arrondi à deux décimales pour IR = 10 et 50). Réfutation : un écart au-delà de 0,020 (A1) ou 0,025 (A2) sur un seul cas
décisif, dans un sens ou dans l'autre (SUPPOSÉ).

**(B) Hors échantillon** (modèle 2019→2022, IR = 10, traits de fin 2022, apparition d'une arête dans la fenêtre F) —
signe attendu : aire appariée > 0,5 et modèle > chacune des deux règles simples sur l'échantillon apparié. Ordres de
grandeur, SUPPOSÉ (aucun appui publié pour l'apparition pure) : aire sur l'échantillon aléatoire ≈ 0,90 (leur variante
sans réentraînement descend de 0,9463 à 0,9311 quand l'évaluation recule de 2018 à 2022 [p. 8, fig. 7]) ; aire appariée
≈ 0,70. Réfutation : seuils de la section Seuil non atteints. Aucun signe n'est visé (R3) : les deux issues décident du
bras.

**Attentes écrites des analyses d'information** (aucune n'entre dans un verdict ; toutes SUPPOSÉ) :
- B′ (leur tâche : impact, citations 2023–2025) : aire entre 0,88 et 0,95, au-dessus de B-i (tâche d'entraînement
  retrouvée ; repère : 0,9311 [p. 8, fig. 7]).
- B avec les modèles IR = 50 et 100 : **aucun signe attendu** (ces modèles sont entraînés sur un impact plus rare,
  pas sur l'apparition) ; écart à IR = 10 attendu inférieur à 0,03 en valeur absolue sur B-i et sur B-ii.
- Variante « mot entier » de la recherche de sous-chaîne : B-i et B-ii à moins de 0,01 de la version sous-chaîne.
- Variante conditionnée de A2 : à moins de 0,03 de 0,694 (évaluation) ; repère d'entraînement 0,747 [p. 5].
- Fenêtre non retenue par D-GK-1, rapportée en information : si F recommandée est retenue, B-i et B-ii sur la
  population conditionnée (2024–2026, paires reliées en 2023 retirées) attendues **plus basses** de 0,01 à 0,05 ; si F
  littérale est retenue, B-i et B-ii sur la fenêtre 2023–2026 attendues **plus hautes** de 0,01 à 0,05.
- Aire appariée de l'attachement préférentiel (indicateur d'appariement, voir Métrique) : entre 0,50 et 0,60.

## Métrique

- **Aire sous la courbe** du taux de vrais positifs contre le taux de faux positifs, sur les sorties brutes du réseau ;
  ex æquo comptés pour moitié. Leur code calcule l'aire par `roc_auc_score` (`benchmark_code/loops_fcNN.py` l. 43) ou par
  `roc_curve` puis `auc` (`fpr_example/plot_FPR.py`) — SUPPOSÉ, code lu, jamais exécuté. Notre code d'aire est comparé
  à `roc_auc_score` (contrôle de métrique, B2).
- **A** : aire de chaque graine sur leur ensemble d'évaluation publié (`data_eval.zip`, traits déjà calculés —
  SUPPOSÉ, métadonnées Zenodo) pour A2, et sur `eval_data_2019_2022_IR{10,50}` pour A1 ; statistique = moyenne des
  trois graines ; étendue des graines rapportée.
- **B, trois statistiques décisives**, chacune = moyenne des aires des trois graines du modèle figé :
  - **B-i** aire sur l'échantillon aléatoire « à leur manière » : 10 millions de paires [taille : p. 4] tirées
    uniformément, **à l'étape B0, avant toute moisson**, parmi les paires non reliées au 31 décembre 2022 sur leur
    graphe tronqué (Plan, B0) ;
  - **B-ii** aire sur l'échantillon apparié (positives et leurs témoins, Plan, B4) ;
  - **B-iii** différence appariée : aire appariée du modèle − max(aire appariée de l'attachement préférentiel, aire
    appariée de Simpson), le maximum étant pris **dans chaque rééchantillon** (conservateur).
- **Intervalles** : rééchantillonnage (bootstrap) par percentiles, 95 %, 2 000 rééchantillons (SUPPOSÉ) ; unité de
  rééchantillonnage = la paire pour B-i, la grappe « une positive et ses k témoins » pour B-ii et B-iii. Pour A, pas
  d'intervalle décisif (l'incertitude publiée est nulle) ; l'étendue des graines est rapportée.
- **Règles simples** : attachement préférentiel = produit des degrés à fin 2022 ; Simpson = voisins communs / plus
  petit degré, à fin 2022 (meilleur trait seul de leur papier, 0,8880 en 2019 [p. 13, fig. 12]). Dans une case
  appariée sur des classes de degré qui couvrent chacune un facteur d'environ 2, l'attachement préférentiel ne garde
  que le degré résiduel : son aire appariée est attendue un peu au-dessus de 0,5. Elle est **rapportée comme indicateur
  de la qualité de l'appariement** et reste dans le maximum de B-iii (le modèle doit battre aussi ce degré résiduel) ;
  elle ne déclenche aucun verdict à elle seule.

## Seuil

- **A1 retrouvée** : les deux cas du réseau (IR = 10 et 50) à moins de 0,010 de la cible ; **non retrouvée** : un des
  deux au-delà de 0,020 ; entre les deux : **retrouvée avec réserve** (on continue, la réserve est rapportée).
  XGBoost : rapporté avec ses écarts, sans verdict ; un écart XGBoost au-delà de 0,020 alors que le réseau passe est une
  réserve nommée. SUPPOSÉ.
- **A2 retrouvée** : les trois cas à moins de 0,015 ; **non retrouvée** : un cas au-delà de 0,025 ; entre les deux :
  retrouvée avec réserve. SUPPOSÉ.
- **B réussi** (HB non réfutée) si les trois tiennent : B-i ≥ 0,85 (estimation ponctuelle) ; borne basse de
  l'intervalle de B-ii > 0,60 ; borne basse de l'intervalle de B-iii > 0. SUPPOSÉ. **B échoué** si l'une manque.
- Lien entre 0,60 et l'usage : le bras propose au bisociateur des paires classées ; à aire appariée 0,60, entre deux
  paires de mêmes classes de degré et d'âge, le modèle place la paire qui se reliera devant l'autre six fois sur dix.
  En dessous, le bras n'apporte presque rien de plus qu'un filtre sur le degré et l'âge, qui ne coûte ni entraînement
  ni machine louée : c'est un **plancher d'usage**, pas une preuve de fiabilité. B-iii > 0 ajoute qu'il doit aussi
  battre Simpson, règle gratuite. Le seuil n'est pas relevé : aucune donnée ne permet d'en fixer un autre moins
  arbitrairement, et « B réussi » ne se lit que « HB non réfutée ».
- Les tests sont conjonctifs (tout doit passer pour conclure « non réfuté ») : aucune correction pour comparaisons
  multiples n'est nécessaire pour cette conclusion ; tout le reste est rapporté comme information, sans verdict.

## Plan d'analyse

**Graines (R9)** : `numpy.random.SeedSequence(293431315339861648349832936273213435135)` (numpy ≥ 1.25), `.spawn(8)`
(les enfants 0 à 5 sont ceux de la v1 : clés d'engendrement (0,) à (5,)) ; entiers par `generate_state(1)[0]` :
- 0 → A1 : `.spawn(3)`, trois graines d'entraînement **partagées** par les quatre configurations (réseau et XGBoost ×
  IR = 10 et 50) ;
- 1 → A2 : `.spawn(3)`, partagées par IR = 10, 50, 100 ;
- 2 → B0 : `.spawn(3)`, partagées par IR = 10, 50, 100 ;
- 3 → `.spawn(2)` : premier enfant → tirage des 10 millions de paires de B-i (à B0) ; second → les 10 millions de B′ ;
- 4 → témoins de B-ii ;
- 5 → rééchantillons ;
- 6 → les 10 000 lignes du contrôle des traits ;
- 7 → tirage des positives retenues pour B4 (au plus 200 000).
Chaque graine entière est consignée au manifeste de l'étape (`src/controle_ia/manifeste.py`). Leur graine 42
(SUPPOSÉ, code) n'est pas reprise.

**Versions** : aucune version n'est épinglée chez eux (aucun `requirements.txt`, état des lieux § 1). Règle choisie
ici (SUPPOSÉ) : chaque bibliothèque de leur code (torch, numpy, pandas, pyarrow, scipy, networkx, scikit-learn,
xgboost) est épinglée à la dernière version publiée sur l'index des paquets Python au 23 avril 2025 (dernière
modification de leur code, état des lieux § 1) compatible avec la version de Python retenue ; les numéros sont
inscrits dans `requirements-gu-krenn-v1.txt`, empreinté et cité ici, **avant** le scellement ; le manifeste de chaque
run les recopie.

**A1, banc d'essai (voie la moins chère)** : leurs fichiers `train_data_2016_2019_IR{10,50}` et
`eval_data_2019_2022_IR{10,50}` (SUPPOSÉ, répertoires centraux Zenodo) ; leurs scripts `loops_fcNN.py` (trois couches
cachées de 600 [p. 8]) et `loops_xgboost.py`, hyperparamètres publiés inchangés ; 3 graines × 2 modèles × 2 IR.

**Contrôle des traits (étape 4 bis, après le verdict de A1, avant A2)** — il ne dépend que des archives déjà
nécessaires à A2 (`data_concept_graph.zip`, `data_eval.zip`) : nos traits de fin 2019 recalculés par leur code
(`get_all_feature`, adjacence et PageRank régénérés depuis le parquet) sur leurs 10 millions de paires d'évaluation,
comparés à `eval_data_pair_feature.parquet` sur 10 000 lignes tirées par l'enfant 6. Tolérances par famille (SUPPOSÉ) :
- PageRank des extrémités (années *y*, *y* − 1, *y* − 2) : corrélation de rang de Spearman ≥ 0,999 et écart relatif
  maximal ≤ 10⁻³ (PageRank itératif de networkx, convergence à 10⁻⁶, version non connue chez eux) ;
- tous les autres traits (comptes de voisins, rangs de comptes entiers, similarités, traits de citations), après
  normalisation : écart absolu maximal ≤ 10⁻⁴. Les rangs (`rankdata` sur des comptes entiers, ex æquo moyennés) sont
  déterministes : ils restent dans la famille stricte.
Hors tolérance → B **non concluant** (bras suspendu) ; A2 est lancé quand même (il décide HA ; comme pour E-1, la chaîne
publiée qui ne se reproduit pas reste un échec de A2 si ses seuils ne sont pas atteints) ; B0 et la moisson ne sont pas
lancés.

**A2, expérience principale** (seulement si A1 n'est pas « non retrouvée ») : graphe `full_dynamic_graph.parquet`,
paires non reliées en 2016 régénérées [≈ 689 millions, p. 11], toutes les positives et autant de négatives, 85 % / 15 %
[p. 11], quatre couches cachées de 600, Adam, taux 3 × 10⁻⁵, lots de 1000 équilibrés [p. 11] ; 3 graines × IR = 10,
50, 100. Les matrices d'adjacence et le PageRank sont **régénérés** depuis le parquet, jamais chargés depuis leurs
pickles. Écart connu : l'étape `_clean` n'est pas publiée (écart E-1).

**B0, modèle figé et échantillon évalué** (seulement si A2 n'est pas « non retrouvée » et si le contrôle des traits
passe) :
- **Tronquage** : leur graphe est filtré sur la date d'arête ≤ 31 décembre 2022 (comme leur `get_adjacency_matrix`,
  `features_utils.py` l. 35–37 : `time <= date(2022,12,31) − date(1990,1,1)` en jours) **avant tout calcul** de traits,
  d'âge, de population et de pont ; seules les colonnes de citations d'années ≤ 2022 sont lues.
- **Entraînement** : `train_model_2022_run.py` (2019→2022), IR = 10, 50, 100, trois graines (enfant 2). La
  normalisation de l'entraînement reste la leur (maxima de colonne sur l'échantillon d'entraînement équilibré, par
  `get_all_feature` appelé dans `prepare_train_data`, `preprocess_utils.py` l. 145, et `train_model_utils.py`
  l. 281 et 287) : fidélité ; l'asymétrie entre normalisation d'entraînement et normalisation d'évaluation est la leur.
- **Échantillon B-i et maxima** : tirage (enfant 3, premier) des 10 millions de paires non reliées au 31 décembre 2022
  sur le graphe tronqué ; calcul de leurs traits de fin 2022 ; maxima de colonne des traits de paire calculés **sur cet
  échantillon** (ce que fait leur évaluation : `rescaling_col` dans `get_all_feature`, `features_utils.py` l. 384–392,
  appelé par `prepare_eval_data/prepare_eval_feature_data.py` l. 145). Ces maxima sont ensuite appliqués à **toutes**
  les paires évaluées de B (B-i, B-ii, B-iii, B′ et variantes), par leur fonction à maxima donnés `get_norm_features`
  (`features_utils.py` l. 444 et suivantes) ; les traits de nœuds gardent leur normalisation par ligne
  (`rescaling_row`, indépendante de l'échantillon). Aucune valeur n'est rognée au-dessus de 1 (comme leur code).
- **Scellés avant B1** : poids des neuf modèles, liste des 10 millions de paires de B-i, leurs traits de fin 2022, les
  maxima, le graphe tronqué (empreinte), les classes de degré et d'âge de chaque concept.

**B1, moisson** : requête déclarée de l'état des lieux (§ 4.3), articles de revue avec titre, résumé et date, publiés
du 1er janvier 2022 au 30 septembre 2026 ; traitement identique au leur (minuscules, remplacements, sous-chaîne sans
limite de mot). Champ de type fixé avant moisson sur le schéma d'une seule fiche de 2022 (inconnue I-2).

**B2, contrôles avant étiquettes** (lus avant toute étiquette postérieure à 2022) :
- **pont** : paires créées par les articles de 2022 dans notre moisson contre leur graphe ; indice de Jaccard des
  ensembles ≥ 0,80 et rapport des comptes dans [0,85 ; 1,18] (SUPPOSÉ) ;
- **contrôle de métrique** (lu à l'étape 3, avant A1) : sur les trois fichiers `solution_output_{10,50,100}.npy` de
  `frp_example` (colonne 0 = vérité, colonne 1 = sortie, d'après `fpr_example/plot_FPR.py` — SUPPOSÉ, code lu),
  **décisif** : écart entre notre code d'aire et `roc_auc_score` ≤ 10⁻⁶ sur chacun ; **rapporté, non décisif** : écart
  à 0,94 / 0,96 / 0,948 [p. 12], tolérance 0,010 pour IR = 10 et 50 (0,005 d'arrondi publié + 0,005) et 0,005 pour
  IR = 100 (SUPPOSÉ). Rapprochement hors tolérance → réserve nommée et audit de la convention des colonnes **avant A1**
  (R4), consigné ; il ne rend pas B non concluant à lui seul.

**B3, population et étiquettes** (texte écrit pour la fenêtre recommandée de D-GK-1) : population = paires non reliées
au 31 décembre 2022 sur le graphe tronqué (aucune donnée moissonnée n'entre dans la définition de la population).
Étiquette = au moins un article de notre moisson publié du 1er janvier 2023 au 30 septembre 2026 qui les relie.
Traits = ceux de fin 2022 (leur graphe seul : aucune source mêlée dans les entrées), normalisés par les maxima scellés
à B0. Rapporté : nombre et part des positives reliées dès 2023.

> **Décision ouverte D-GK-1 (identifiant provisoire, nœud de décision : modification du test décisif ; aucun défaut
> sous 48 heures)** — fenêtre du test B.
> - **(a) recommandée** : texte ci-dessus (population à fin 2022, fenêtre 2023–2026). Avantage : aucun
>   conditionnement sur l'issue proche, population indépendante de la moisson. Inconvénient : s'écarte de la lettre
>   « liens apparus de 2024 à 2026 » du message n° 261.
> - **(b) littérale** : mêmes 10 millions tirés à B0 ; après B1, les paires reliées en 2023 (selon notre moisson)
>   sortent de la population (un sous-ensemble d'un tirage uniforme reste uniforme dans la population restreinte) ;
>   étiquette = au moins un article du 1er janvier 2024 au 30 septembre 2026. Déclaré **conditionné sur l'issue 2023** :
>   le retrait ôte d'abord les positives les mieux classées, le biais joue **contre le modèle** à seuils fixes ; nombre
>   et part des paires retirées rapportés. Maxima inchangés (ceux de B0).
> - Dans les deux cas, l'autre fenêtre est rapportée en information (attente écrite en section Prédiction).
> - Le texte scellé (v3) ne gardera que la branche retenue.

**B4, témoins appariés** : positives = celles de l'échantillon B-i ; si elles dépassent 200 000 (SUPPOSÉ), 200 000
sont tirées par l'enfant 7. Pour chacune, k = 5 témoins (SUPPOSÉ) tirés (enfant 4) dans toute la population restée non
reliée au 30 septembre 2026, dans la même case : classe de degré à fin 2022 de l'extrémité de plus bas degré et de
l'autre (classe = partie entière de log2(1 + degré)), et classe d'âge de chacune (âge = 2022 − année de sa première
arête dans le graphe tronqué ; classes 0–1, 2–4, 5–9, 10–19, ≥ 20 ans, plus « sans arête ») — SUPPOSÉ. Tirage par rejet
sur les extrémités de chaque classe. Positive sans 5 témoins possibles : retirée, comptée. Traits des témoins
normalisés par les maxima de B0.

**Rapporté comme information, sans verdict** (attentes en section Prédiction) : B avec les modèles IR = 50 et 100 ;
**B′, même tâche que la leur** — étiquette = au moins IR citations en 2023–2025 des articles qui relient la paire, 10
millions de paires tirées uniformément parmi les non reliées à fin 2022 (enfant 3, second), maxima de B0, IR = 10, 50,
100 ; variante « mot entier » de la recherche de sous-chaîne ; variante conditionnée de A2 (0,747 / 0,694 [p. 5]) ;
l'autre fenêtre de D-GK-1 ; aire appariée de l'attachement préférentiel ; nombre de positives retirées par case.

## Critères de lecture gelés

| Issue | Verdict |
|---|---|
| A1 non retrouvée (réseau) | HA réfutée ; arrêt (contrôle des traits, A2 et B non lancés) ; critère de mort atteint |
| A1 passe ou passe avec réserve, A2 non retrouvée | HA réfutée ; arrêt (B non lancé) ; critère de mort atteint |
| A1 et A2 passent ou passent avec réserve, B réussi | HA et HB non réfutées sur ce découpage ; bras admis à la course 2 (réserves rapportées) |
| A1 et A2 passent ou passent avec réserve, B échoué (une des trois conditions) | HB réfutée ; critère de mort atteint ; la condition manquée est nommée |
| Contrôle des traits hors tolérance | A2 lancé et lu selon ses seuils ; B non concluant ; bras **suspendu** (non admis à la course 2, pas déclaré mort) |
| Un contrôle de B2 échoue (pont), ou arrêt de B (liste d'arrêt) | B non concluant ; bras **suspendu** ; nouveau préenregistrement ou décision de Lazar |
| B-i ≥ 0,85, B-ii ou B-iii échoue | lecture : le modèle lit surtout degré et âge ; verdict « échoué » inchangé |

**Audit de symétrie (R4)** : déclenché par une aire décisive de A à moins de 0,002 de chaque cible (trop proche pour
une autre machine), par un écart de A au-delà de la tolérance **vers le haut**, par B-ii > 0,90, ou par B-i qui dépasse
leur meilleure valeur publiée (0,9588 [p. 7]) — seuils 0,002 et 0,90 SUPPOSÉ : on cherche une fuite (dates, tronquage,
maxima, recouvrement entre entraînement et évaluation) avant tout verdict.

## Critère de mort (message n° 261, point 3)

Écrit d'avance : le bras Gu-Krenn du bisociateur exploratoire de la course 2 est **retiré** si l'une de ces trois
issues se produit : A1 non retrouvée (réseau) ; A2 non retrouvée ; B échoué. « Non concluant » ne vaut pas mort mais
interdit l'usage du bras dans la course 2 tant qu'un préenregistrement nouveau, scellé, ne l'a pas tranché. Le retrait
n'est levé par aucune analyse d'information (B′, IR = 50 ou 100, variante « mot entier », autre fenêtre de D-GK-1,
XGBoost).

## Liste d'arrêt

**Chaque garde de cette liste est codée dans `scripts/gu_krenn_*_v1.py` et testée dans
`tests/test_gu_krenn_gardes_v1.py` sur un cas sain (passe, code de sortie 0) et sur un artefact (arrêt, code de
sortie 1) avant scellement (R5) ; le commit de ces tests est inscrit en tête avec celui du code d'analyse.** Toute garde
qui ne peut pas s'évaluer (fichier absent, valeur non numérique, compte illisible) arrête : elle échoue fermée, jamais
ouverte ; aucune ne se replie en silence.

| Garde | Arrêt et conséquence | Artefact du test |
|---|---|---|
| Empreinte d'une archive téléchargée ≠ celle de Zenodo | arrêt, nouveau téléchargement dans un dossier neuf | archive à un octet modifié |
| Chargement d'un pickle de leurs archives (adjacence, PageRank) ou d'un poids sans `weights_only=True` | garde refuse et arrête | appel à `get_adjacency_matrix` avec un fichier `.gz` présent ; `torch.load` sans l'option |
| Graphe de B non tronqué : date d'arête maximale > 31 décembre 2022, ou colonne de citations d'année > 2022 lue, dans les traits, l'âge, la population, le pont ou l'entraînement de B0 | arrêt, B invalide | graphe jouet avec une arête datée du 1er janvier 2023 ; colonne `c2023` présente et demandée |
| Maxima appliqués à B différents de ceux scellés à B0 (empreinte) | arrêt, B invalide | maxima recalculés sur un autre échantillon |
| Coût cumulé au plafond du devis | arrêt de l'instance par son identifiant (R10), consigné dans `registres/arrets.md` | compteur de coût simulé au plafond |
| Mémoire ou disque épuisés | arrêt ; aucun sous-échantillonnage silencieux : toute réduction passe par un écart déclaré | erreur de mémoire simulée ; disque plein simulé |
| Entraînement qui diverge (valeur non numérique) ou sans arrêt précoce après 10 fois le nombre d'itérations du premier passage (SUPPOSÉ) | arrêt de la course, consigné | perte non numérique injectée ; compteur d'itérations au-delà |
| Moisson incomplète : moins de 99 % (SUPPOSÉ) du compte annoncé par OpenAlex pour la même requête | arrêt avant B2 | moisson jouet à 98 % du compte |
| Moins de 2 000 positives dans B-i (SUPPOSÉ) | B non concluant (puissance) | 1 999 positives |
| Plus de 10 % des positives sans témoins (SUPPOSÉ) | B non concluant | 11 % sans témoins |
| Pont hors tolérance | B non concluant, avant toute étiquette | Jaccard 0,79 ; rapport 1,19 |
| Contrôle des traits hors tolérance | B non concluant (Plan, étape 4 bis) | un trait décalé de 2 × 10⁻⁴ ; PageRank à corrélation 0,998 |
| Contrôle de métrique : écart à `roc_auc_score` > 10⁻⁶ | arrêt avant A1 (le code d'aire est faux, rien n'est lu) | code d'aire qui ignore les ex æquo |
| Lecture d'une étiquette postérieure à 2022 avant le scellement des contrôles de B2 | arrêt, B invalide | appel du calcul d'étiquettes sans le sceau de B2 |

## Ordre de lecture et ce qui n'est jamais lu avant scellement

1. Contre-lecture 2 de cette v2 (R2), décision D-GK-1, v3 sans la branche écartée, code d'analyse et tests des gardes
   commités, versions épinglées, scellement, devis, GO de Lazar.
2. Téléchargements dans des dossiers neufs ; aucun code exécuté depuis ces dossiers ; vérification des empreintes.
3. Contrôle de métrique sur `frp_example` → lu.
4. A1 → verdict écrit et scellé avant la suite.
5. (4 bis) Contrôle des traits → lu et scellé avant A2.
6. A2 → verdict écrit et scellé avant B0.
7. B0 → tronquage, poids, échantillon de B-i, ses traits de fin 2022, maxima, classes scellés avant B1.
8. B1, puis B2 (pont) → lus et scellés avant toute étiquette postérieure à 2022.
9. B3, B4, puis B-i, B-ii, B-iii et les analyses d'information, en une seule exécution du script d'analyse scellé.

**Jamais lu avant scellement** : `frp_example.zip` ; toute aire ou métrique, sur leurs données ou sur OpenAlex ;
tout contenu OpenAlex postérieur à 2022 (seul un compte agrégé de la requête, sans concept ni citation, est permis pour
le devis, inconnue I-1). **Jamais lu tout court** dans ce chantier : les branches `donnees/bras-attaque-*`,
`donnees/mode-tenu-a-l-ecart-v1`, `quarantaine/*`, et toute autre référence `donnees/*`.

## Écarts possibles et leur traitement

| Écart | Traitement |
|---|---|
| E-1 Étape `_clean` absente du code (I-5) | A2 et B0 sur la version non nettoyée, déclarée ; un échec de A2 reste un échec (la chaîne publiée ne se reproduit pas) |
| E-2 Champ de type OpenAlex (I-2) | fixé avant moisson sur le schéma d'une fiche de 2022, consigné |
| E-3 Dérive Walden, résumés retirés ou récupérés (I-3) | pont B2 ; hors tolérance → non concluant |
| E-4 Citations révisées depuis 2023 (I-4) | sans effet sur B (apparition) ; rapporté pour B′ |
| E-5 Extraction partielle d'une archive impossible (I-8) | téléchargement entier ; devis revu avant |
| E-6 Processeur au lieu de carte graphique ; versions épinglées par la règle du Plan et non les leurs (inconnues) | consigné au manifeste ; couvert par la tolérance ; XGBoost hors du verdict |
| E-7 Différences entre l'arXiv v4 et la version publiée (I-11) | la v4 empreintée fait foi |
| E-8 Tout autre changement après scellement | addendum scellé avant la lecture concernée ; s'il vient après lecture, la statistique touchée devient exploratoire et sort du verdict |

## Couverture du vocabulaire du contrôle (information)

Recherche de chaînes dans leur liste de 37 960 concepts (`couverture-vocabulaire-controle-v1.tsv`
`0f8dc65752ded4ac6a926abfc6d1945937895594ba5d7d0b2c1c7f70ac696376`) : sabotage, e-valeur, sécurité de
l'intelligence artificielle, interprétabilité, modèle de langage, jailbreak, backdoor, sandbagging, scheming, chaîne de
pensée sont absents ; probe, steering, monitoring, alignment n'existent qu'au sens de la physique. Leur modèle ne peut
donc rien dire du contrôle des intelligences artificielles ; l'étendre demande un autre graphe (chaîne d'extraction sur
arXiv `cs.*`) et un autre entraînement : seconde expérience, à préenregistrer à part. Information seulement : n'entre
dans aucun verdict ci-dessus.

## Contre-lecture

- **Contre-lecture 1** (de la v1) — sous-agent neuf d'un autre modèle que l'auteur (message n° 261, point 2), qui n'a
  pas écrit ce texte ; identifiant du contre-lecteur : non transmis à l'auteur par le script d'orchestration, à inscrire
  par l'orchestrateur. Brouillon relu : `prereg-gu-krenn-reproduction-et-hors-echantillon-v1.md`
  `1920d1504f0eabda3ba5bd8cb6e80db9013c2738a67cb232d42c6fa1499154cb`. Rapport (transcrit tel que reçu par l'auteur, en
  JSON) : `docs/notes/gu-krenn-v1/contre-lecture-1-prereg-gu-krenn-v1-rapport-v1.json`
  `12a4978b1b4896151940211c671e033c2b5fac8f0b7ca04129c8de04cd2fe74a`. Traitement de chaque remarque : section suivante.
- **Contre-lecture 2** (de cette v2, exigée parce que le texte change le test décisif, les gardes et les seuils) :
  À REMPLIR — sous-agent neuf d'un autre modèle, ni auteur ni contre-lecteur 1 ; identifiant, empreinte de la v2 relue,
  chemin et empreinte de son rapport, traitement de chaque remarque.

## Constats de la contre-lecture → sort

| N° | Gravité | Constat (résumé) | Sort | Où, et motif |
|---|---|---|---|---|
| 1 | majeur | Population de B à fin 2023 : conditionnement sur l'issue 2023, biais contre le modèle | **appliqué, sous décision** | Vérifié : le retrait des paires reliées en 2023 ôte d'abord les positives les mieux classées. Texte écrit pour l'option (a) recommandée ; option (b) littérale entièrement écrite dans l'encadré D-GK-1, déclarée conditionnée, biais nommé ; nœud de décision soumis à Lazar, aucun défaut. Ajout : même dans (b), les 10 millions sont tirés à B0, avant moisson. |
| 2 | majeur | Contradiction sur le moment du gel des maxima ; citation du code à corriger | **appliqué, avec une variante** | Vérifié dans le code : `rescaling_col` est appelé dans `get_all_feature` (`features_utils.py` l. 384–392), lui-même appelé par `prepare_eval_feature_data.py` l. 145 et `preprocess_utils.py` l. 145. Variante : au lieu d'un échantillon dédié aux maxima, l'échantillon de B-i lui-même est tiré à B0 sur le graphe tronqué et ses maxima sont scellés avant moisson — c'est exactement « à leur manière » pour B-i, la contradiction disparaît, et aucune graine de plus n'est nécessaire. Maxima appliqués partout par leur `get_norm_features` (l. 444). Asymétrie entraînement/évaluation déclarée comme la leur. |
| 3 | majeur | R5 : seule la garde « pickle » annoncée testée | **appliqué** | Phrase de tête de la Liste d'arrêt, tableau avec un artefact par garde, chemin `tests/test_gu_krenn_gardes_v1.py`, règle « échoue fermée ». Gardes ajoutées : maxima scellés, étiquette lue avant le sceau de B2, contrôle de métrique contre `roc_auc_score`. |
| 4 | majeur | Préalables au scellement non remplis | **appliqué (rappelé), reste ouvert** | En tête : liste des cinq préalables. Le code, les tests, les versions et le devis restent à faire : hors du périmètre de cette révision. |
| 5 | mineur | Cible ambiguë pour IR = 100 ; tolérance du contrôle de métrique égale à l'arrondi | **appliqué** | Vérifié p. 12 : 0,948 pour IR = 100 (annexe D), confirmé p. 13 (fig. 12). Cible unique 0,948 (A2 et contrôle de métrique). Contrôle de métrique décisif = notre code contre `roc_auc_score` (≤ 10⁻⁶) ; rapprochement avec les valeurs publiées rapporté, tolérances 0,010 / 0,010 / 0,005, avec audit de la convention des colonnes avant A1 s'il échoue. |
| 6 | mineur | « 141 traits » en page 4, non 3 | **appliqué** | Vérifié sur le texte du PDF : « 141 features » p. 4, 37 960 p. 3. Ajout vérifié au passage : la page 3 donne aussi « février 2023 » pour l'instantané, mentionné dans l'Hypothèse. |
| 7 | mineur | Seuil 0,60 de B-ii sans justification | **appliqué (phrase et lecture), seuil gardé** | Phrase reliant 0,60 au plancher d'usage ; « B réussi » ne se lit que « HB non réfutée » ; « fiable » remplacé par « utilisable, non réfuté ». Seuil non relevé : aucune donnée pour en fixer un autre moins arbitrairement. |
| 8 | mineur | A1 décisif sur XGBoost, qui n'est pas l'instrument | **appliqué** | Décisif : les deux cas du réseau ; XGBoost rapporté, écart > 0,020 = réserve nommée ; versions épinglées par une règle écrite (Plan, Versions), pour toutes les bibliothèques. Critère de mort mis en accord. |
| 9 | mineur | Contrôle des traits trop strict et trop tard | **appliqué en partie** | Avancé à l'étape 4 bis (avant A2), graine dédiée (enfant 6). Tolérance par famille : PageRank lâché (Spearman ≥ 0,999, relatif ≤ 10⁻³) ; **refusé pour les rangs** : `rankdata` sur des comptes entiers est déterministe (ex æquo moyennés), un écart y signalerait un vrai défaut de chaîne, ils restent dans la famille stricte (absolu ≤ 10⁻⁴). Conséquence d'un échec précisée : A2 lancé, B0 et moisson non lancés. |
| 10 | mineur | Graines incomplètes | **appliqué, sauf la graine des maxima** | `.spawn(8)` (enfants 0 à 5 inchangés) : enfant 6 pour les 10 000 lignes, enfant 7 pour les positives de B4 ; partage des trois graines par toutes les configurations d'une étape écrit. Pas d'enfant pour un échantillon de maxima : il n'existe plus (constat 2). |
| 11 | mineur | Lignes de lecture « passent avec réserve » ; maximum de B-iii ; attachement préférentiel comme contrôle d'appariement | **appliqué en partie** | « Passent ou passent avec réserve » écrit dans les deux lignes ; maximum pris dans chaque rééchantillon. **Refusé : la garde « aire appariée de l'attachement préférentiel > 0,55 → non concluant »**. Motif : les classes log2 couvrent chacune un facteur d'environ 2 en degré par extrémité, donc un degré résiduel existe dans chaque case et une aire un peu au-dessus de 0,5 est attendue sans défaut de montage ; en faire une sortie « non concluant » créerait une issue non mortelle déclenchée par un effet connu. L'attachement préférentiel reste dans le maximum de B-iii (plus exigeant pour le modèle) et son aire appariée est rapportée comme indicateur, attente 0,50–0,60 écrite. Ajout de l'auteur : « B-i passe nettement » remplacé par « B-i ≥ 0,85 » (le mot « nettement » n'était pas défini). |
| 12 | mineur | Tronquage du graphe non explicite | **appliqué** | Vérifié : leur `get_adjacency_matrix` filtre `time <= date(year,12,31)` (`features_utils.py` l. 35–37). Tronquage écrit à B0 avant tout calcul ; garde sur la date d'arête maximale et sur l'année maximale des colonnes de citations, avec artefact. |
| 13 | mineur | Analyses d'information sans attente écrite | **appliqué en partie** | Attentes SUPPOSÉ écrites pour B′, « mot entier », variante conditionnée (à ± 0,03 de 0,694 [p. 5]), autre fenêtre de D-GK-1, attachement préférentiel. **Refusé : « IR = 50 et 100 attendues au-dessus de IR = 10 sur B-i (comme fig. 11) »**. Motif : la fig. 11 porte sur la tâche d'impact, pas sur l'apparition ; en transférer l'ordre serait une inférence sans appui. Attente écrite à la place : aucun signe, écart absolu < 0,03. |
