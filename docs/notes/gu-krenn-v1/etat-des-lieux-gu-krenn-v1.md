# État des lieux — Gu et Krenn 2024 (« Impact4Cast »), avant reproduction et test hors échantillon — v1

Lignée « session-depot », 31 octobre 2026, 02:15–03:00 UTC. Demande : message n° 261 de conv-audit
(`origin/canal/conv-audit-n04:brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-10-30_n261.md`), qui cite le
brief `brief-nouvelle-lignee-bisociateur-v1.md` de la même branche (empreinte vérifiée contre son `.sha256` :
`2cdf135fff340960…`, conforme).

**Ce que cette note n'est pas.** Aucun code de Gu et Krenn n'a été exécuté ; aucune donnée lourde n'a été
téléchargée ; aucune aire sous la courbe ni aucune autre métrique n'a été calculée, ni sur leurs données ni sur
OpenAlex (R1). Les seuls comptes produits sont des comptes de chaînes dans leur liste de concepts (§ 5), qui ne sont pas
une mesure de résultat. Aucune dépense ; aucune requête à l'interface payante d'OpenAlex ; aucune clé lue.

Source primaire : `docs/sources/pdf/bisociation-fertilite-v1/arxiv-2402.08640-gu-krenn-2024.pdf`, empreinte
`6b3d29db7cd6f7de…` (vérifiée, conforme), version arXiv **v4 du 11 juin 2025**, 18 pages. Pages citées selon la
numérotation imprimée du PDF. Version publiée : *Machine Learning: Science and Technology* 6(2), 025041 (2025) (selon le
LISEZMOI du dépôt de code ; non vérifiée sur la version publiée, que nous n'avons pas — R7 : les chiffres ci-dessous
sont ceux de la v4).

---

## 0. Ce que fait le papier (lecture du PDF)

**Tâche exacte.** Ce n'est pas une prédiction de liens au sens strict : c'est une **prédiction d'impact** de paires de
concepts encore jamais reliées. Pour une paire non reliée à la fin de l'année *y*, prédire si, dans les trois ans qui
suivent, elle sera reliée par des articles qui cumulent **au moins IR citations** (« impact range ») ; classification
binaire (p. 4, § « Forecasting impact… » ; légende de la fig. 4, p. 5). Une paire qui reste non reliée vaut 0 citation
(code : `prepare_unconnected_pair_solution.ipynb`, colonne `citation` mise à 0). Une variante « au-delà de la
prédiction de liens » conditionne sur les paires qui se relient effectivement, et classe 0–5 contre ≥ 100 citations
(fig. 4(d), p. 5).

**Graphe de concepts.**
- Sommets : **37 960 concepts** du domaine optique et physique quantique (p. 3 ; annexe B, p. 10), tirés d'une liste
  générale de **368 825 concepts** extraits par l'algorithme d'extraction automatique de mots-clés RAKE des titres et
  résumés de **2 444 442 prépublications** (arXiv, bioRxiv, medRxiv, chemRxiv ; coupure février 2023) ; seuils : 9
  articles pour les concepts de deux mots, 6 pour trois mots et plus ; filtres automatiques puis revue manuelle ;
  restriction au domaine par les 78 084 articles arXiv `physics.optics` et `quant-ph` (87 741 candidats, puis 37 960
  après filtrage et revue manuelle) (p. 2–3, p. 10).
- Arêtes : deux concepts sont reliés quand ils **apparaissent ensemble dans le titre ou le résumé** d'un article de
  revue d'OpenAlex (p. 3). Le code (`create_dynamic_edges/get_concept_pairs.py`) fait une **recherche de sous-chaîne
  brute** (`if concept in curr_article`) sur le titre et le résumé reconstitué, mis en minuscules, tirets remplacés par
  des espaces, **sans limite de mot** (l'exemple du papier, p. 10, attribue d'ailleurs « ring theory » à un article sur
  la « string theory »).
- Articles retenus : type `journal-article` avec titre, date et résumé (`_get_openalex_workdata.py`) ; 92 millions
  d'articles après filtrage (68 Go compressés), dont 21 165 421 forment au moins une arête (fig. 1, p. 2 ; p. 10).
- Graphe final : 37 960 sommets, **26 010 946 arêtes uniques**, 193 977 096 paires avec multiplicité (p. 11) ;
  instantané OpenAlex, coupure **avril 2023** (p. 3).
- Poids : chaque arête porte la date de l'article (jours depuis le 1er janvier 1990) et ses citations annuelles **2012 à
  2023** plus le total ; les arêtes multiples additionnent les citations (p. 3, p. 11).

**Partage temporel.** « Année *y* » = graphe des articles publiés jusqu'au 31 décembre de *y* (code : `day_2016 =
(date(2016,12,31) - day_origin)`).
- Entraînement : paires non reliées en **2016**, cible en **2019** (citations cumulées des années 2017, 2018 et 2019
  des articles qui créent l'arête). Environ **689 millions** de paires non reliées en 2016 ; toutes les positives
  (≥ IR) et autant de négatives tirées au hasard ; 85 % entraînement, 15 % « test » (p. 11).
- Évaluation : **10 millions** de paires non reliées en **2019**, tirées au hasard, cible en **2022** (citations 2020 à
  2022), réseau entraîné sur 2016→2019 seulement (p. 4 ; fig. 3, p. 4 ; p. 11).
- Banc d'essai (fig. 6, p. 7 ; p. 8–9) : intervalles d'entraînement de 2, 3 ou 4 ans et d'évaluation de 1 à 5 ans, fin
  d'évaluation fixée à 2022, sur **1 million** de paires ; seuils IR = 10 et 50 ; quatre modèles (réseau
  entièrement connecté, transformeur, forêt aléatoire, XGBoost). Variante sans réentraînement : entraîné 2014→2017,
  évalué de 2017 vers 2018 à 2022 (fig. 7, p. 8).

**Traits d'entrée.** 141 traits par paire : 41 de réseau (20 de sommet : voisins, nouveaux voisins, rangs, PageRank sur
*y*, *y*−1, *y*−2 ; 21 de paire : voisins communs, similarités géométrique, cosinus, Simpson, attachement
préférentiel, Sørensen–Dice, Jaccard) et 100 de citations (58 de sommet, 42 de paire) (p. 4 ; tableaux I et II,
p. 14–15). **Normalisation** (code `features_utils.py`) : traits de sommet divisés par leur maximum par ligne ; traits
de paire divisés par leur maximum **sur l'échantillon évalué** (`rescaling_col`) ou par un maximum du graphe entier
pré-calculé (`get_norm_features`) — le choix change la valeur des traits selon la composition de l'échantillon (voir
§ 4, piège 5).

**Modèle.** Réseau entièrement connecté, **quatre couches cachées de 600** (p. 4 ; annexe C, p. 11 ; code
`train_model_utils.ff_network`), perte quadratique sur sortie unique, Adam, taux 3 × 10⁻⁵, lots de 1000 équilibrés
(p. 11), arrêt précoce sur moyenne mobile de la perte de test. Le banc d'essai utilise **trois** couches cachées de 600
(≈ 800 000 paramètres), lots de 2048, taux 10⁻⁴, patience 500 (p. 8 ; `benchmark_code/loops_fcNN.py`).

**Métrique.** Aire sous la courbe caractéristique de fonctionnement du récepteur (taux de vrais positifs contre taux
de faux positifs), « probabilité qu'un exemple vrai tiré au hasard soit classé au-dessus d'un exemple faux tiré au
hasard » (p. 4), calculée sur le classement des sorties brutes du réseau (`sklearn.metrics.roc_auc_score`), pour
l'ensemble « test » (paires de 2016 hors entraînement) et l'ensemble d'évaluation (2019→2022), **horizon trois ans**
dans l'expérience principale.

**Valeurs publiées (R7, page citée, lues sur le PDF v4 empreinté).**

| Expérience | Valeur | Page |
|---|---|---|
| Résumé : « au-delà de 0,9 pour la plupart des expériences » | — | p. 1 |
| Fig. 4(a) : test 2016→2019 et évaluation 2019→2022, IR de 1 à 200 | « au-delà de 0,8, le plus souvent au-delà de 0,9 » (courbe seulement, pas de tableau) | p. 4–5 |
| Évaluation 2019→2022, IR = 10 | 0,94 | fig. 11, p. 12 |
| Évaluation 2019→2022, IR = 50 | 0,96 | fig. 11, p. 12 |
| Évaluation 2019→2022, IR = 100 | 0,95 (fig. 11) ; **0,948** (texte de l'annexe D) | p. 12 |
| Fig. 4(d), paires reliées conditionnées, {0–5, ≥ 100} : test / évaluation | **0,747 / 0,694** (texte : « au-delà de 0,7 » et « au-delà de 0,67 ») | p. 5 |
| Banc, IR = 10, entraînement 2016–2019, évaluation 2019–2022 : réseau / transformeur / forêt / XGBoost | **0,9455 / 0,9454 / 0,9431 / 0,9442** | fig. 6(a), p. 7 |
| Banc, IR = 50, même découpage | **0,9588 / 0,9532 / 0,9602 / 0,9561** | fig. 6(b), p. 7 |
| Banc, entraînement 2014→2017 sans réentraînement, réseau IR = 10, évaluation jusqu'à 2018 … 2022 | 0,9463 ; 0,9416 ; 0,9373 ; 0,9332 ; 0,9311 | fig. 7, p. 8 |
| Meilleur trait seul (Simpson, année *y*) | 0,8880 | fig. 12, p. 13 |
| Moyenne des citations sur les 10 millions de paires d'évaluation | 0,029 citation | légende fig. 4, p. 5 |

Les valeurs du banc ont été associées à leur panneau par les coordonnées du texte du PDF, puis vérifiées à l'œil sur
la page 7 rendue en image. Aucune incertitude n'est publiée (une seule course par cas, graine 42).

**Code et données annoncés (p. 9).** Code : `https://github.com/artificial-scientist-lab/Impact4Cast`. Données :
`https://doi.org/10.5281/zenodo.10692137` ; banc : `https://doi.org/10.5281/zenodo.14527306`.

---

## 1. Où sont le code et les données ; licences, tailles, dates

**Code** — cloné (`git clone --depth 1`, puis historique approfondi pour les dates) dans
`docs/notes/gu-krenn-v1/sources-amont-v1/Impact4Cast/` ; tête `d2af4f3d69e1e5272c168d3f950b56b31845a51f`
(2026-07-19, « Update README.md ») ; dernière modification de code : 2025-04-23 (`features_utils.py`) ; premier commit
2024-02-12 ; 125 commits. **Licence MIT.** 8,9 Mo, 49 fichiers suivis. Le dossier `.git` a été archivé dans
`Impact4Cast-git-d2af4f3-v1.tar` (`68d3fb3c58481d4d…`) puis retiré du dossier pour que chaque fichier puisse être
scellé (R6) ; la liste des fichiers avec leurs empreintes de blob git est dans `Impact4Cast-ls-files-d2af4f3-v1.txt`
(`c6e30125163b8d57…`), le journal dans `Impact4Cast-journal-d2af4f3-v1.txt` (`78a08cab8d1798ff…`).
Pas de fichier de dépendances (aucun `requirements.txt`). Code lu, jamais exécuté.

**Données** — métadonnées seules (interface Zenodo `/api/records/<id>`, puis répertoire central de chaque archive lu
par requêtes partielles, quelques kilo-octets chacune ; script `scripts-v1/liste_zip_distant_v1.py`
`82b1b06ffbe9639c…`). Fichiers dans `sources-amont-v1/zenodo-metadonnees-v1/`.

| Dépôt Zenodo | Licence | Publié | Archive | Taille | Contenu (répertoire central) |
|---|---|---|---|---|---|
| 10692137 « Impact4Cast » | CC-BY-4.0 | 2024-02-27, jamais mis à jour | `data_concept_graph.zip` | 1,25 Go | `full_dynamic_graph.parquet` (666 Mo), `full_dynamic_concept.parquet` (593 Mo), `full_domain_concepts.txt` (812 ko, même taille que celui du dépôt de code) |
| | | | `data_for_features.zip` | 2,64 Go | matrices d'adjacence 2012–2022 (`.gz`, **pickle**), PageRank 2012–2022 (pickle), citations par concept et par paire 2014–2022 (parquet) |
| | | | `data_eval.zip` | 5,65 Go | `eval_data_pair_feature.parquet` (4,12 Go : les 141 traits des 10 millions de paires 2019), solutions (87 Mo), variante conditionnée (1,41 Go + 26 Mo) |
| 14527306 « Benchmark » | CC-BY-4.0 | 2024-12-19, jamais mis à jour | `benchmark_data_for_train.zip` | 10,66 Go | 30 fichiers `train_data_<a1>_<a2>_IR<10|50>.parquet`, 310–372 Mo chacun |
| | | | `benchmark_data_for_eval.zip` | 6,98 Go | 20 fichiers `eval_data_<a1>_2022_IR<10|50>.parquet`, 317–361 Mo chacun |
| | | | `frp_example.zip` | 136 Mo | `solution_output_{10,50,100}.npy` (160 Mo chacun, décompressés) : **sorties brutes de leur réseau et vérité** sur les 10 millions de paires d'évaluation |

Total : 9,53 Go (données) + 17,77 Go (banc). Aucune donnée n'a été téléchargée : quatre archives dépassent 2 Go, et
les deux petites (`data_concept_graph.zip`, `frp_example.zip`) ont aussi été laissées de côté (rien n'en avait besoin
pour cet état des lieux).
Les membres des archives du banc sont presque non compressés (taille compressée ≈ taille) : un fichier isolé
(≈ 350 Mo) peut probablement être extrait par requêtes partielles sans tirer l'archive entière (non essayé).

**Point de vigilance R1** : `frp_example.zip` contient sorties et vérité ; en tirer une aire sous la courbe serait
une lecture de résultat. Ce fichier ne doit être ouvert qu'après scellement du préenregistrement.

---

## 2. Dépendances, matériel, temps

**Dépendances** (relevées dans les `import`) : torch, numpy, pandas (+ pyarrow pour parquet), scipy, networkx,
scikit-learn, xgboost, matplotlib, joblib ; pour reconstruire : boto3, jsonlines, rake-nltk/nltk. Aucune version
épinglée.

**Matériel publié** (annexe C, p. 12) : graphe et traits préparés sur un Intel Xeon Gold 6130 avec **1 Tio de mémoire**
(« pas strictement nécessaire ») ; graphe du domaine ≈ 23,12 Go ; entraînement principal sur **une carte graphique**
Nvidia Quadro RTX 6000, ≈ **1,5 h par valeur d'IR** ; banc d'essai sur **processeur** (même Xeon), mémoire < 15 Go,
≈ **1 h par tâche** (sauf le transformeur, carte graphique, ≈ 3 h).

**Ce conteneur** : 4 cœurs, 15 Go de mémoire, 9,1 Go de disque libre, ni torch ni pyarrow. Il ne suffit pas pour
les données principales (9,5 Go compressés, la matrice des traits d'évaluation fait à elle seule ≈ 10 millions × 141
réels, soit ≈ 11 Go en double précision) ; le banc d'essai est à la limite (< 15 Go selon le papier).

**Estimations (non mesurées ; à remplacer par une mesure sur machine louée)** :
- *Inférence seule* : ≈ 1,2 million de paramètres (quatre couches de 600) → ≈ 2 × 10⁷ opérations par paire ; 10
  millions de paires ≈ 2 × 10¹³ opérations, soit de l'ordre de **5 à 40 minutes sur 4 cœurs**. Le coût réel est
  ailleurs : **calculer les 141 traits** (matrices creuses de voisinage, ~10⁷ paires) et **régénérer les paires non
  reliées** (689 millions de paires pour 2016, jointures pandas avec indicateur : plusieurs dizaines de Go de mémoire).
- *Entraînement* : banc ≈ 1 h par tâche sur processeur (publié). Expérience principale : 1,5 h par IR sur carte
  graphique ; sur processeur, estimation grossière ×5 à ×20, soit **8 à 30 h par valeur d'IR** (nombre d'itérations
  avant arrêt précoce inconnu).
- **Poids publiés : non** (§ 3) — l'inférence seule n'est pas possible sans réentraîner.

---

## 3. Modèle entraîné publié ? Non.

Aucun fichier de poids (`.pt`) ni dans le dépôt de code ni dans les six archives Zenodo (répertoires centraux lus). Le
code sauve les réseaux en local (`torch.save(model)` et `state_dict`, `train_model_utils.py` l. 141–142) sans les
publier. **Il faut réentraîner.** Par ailleurs :
- Les paires d'entraînement de l'expérience principale (`data_pair_solution/unconnected_<a>_pair_solution_connected_<b>_clean.parquet`)
  **ne sont pas publiées** ; le carnet `prepare_unconnected_pair_solution.ipynb` produit la version sans suffixe
  `_clean` : l'étape de « nettoyage » n'est pas dans le code publié (inconnue I-5).
- Seul le banc d'essai fournit des jeux d'entraînement et d'évaluation prêts (traits déjà calculés) : c'est la voie de
  reproduction la moins chère.
- Le script principal boucle sur IR = 1 à 40 seulement (`IR_end=40`, commentaire « IR_end=200 ») : IR = 50 et 100
  demandent un changement de paramètre.
- Le script `train_model_2022_run.py` (entraînement 2019→2022, « pour de vraies prédictions de 2025 ») existe : c'est
  exactement le modèle à figer pour le test hors échantillon (§ 4).

**Sécurité** : les matrices d'adjacence et PageRank de Zenodo sont des **pickles** ; `torch.load` sans
`weights_only` charge aussi un pickle. Charger un pickle non sûr exécute du code. Règle proposée : ne jamais les
charger ; les régénérer depuis `full_dynamic_graph.parquet` (le code sait le faire si le fichier est absent), et ne
charger nos propres poids qu'en `weights_only=True`.

**Trois voies de reproduction**, de la moins chère à la plus fidèle :
- **(R-a) Banc d'essai** : réseau et XGBoost sur `train_data_2016_2019_IR{10,50}` et `eval_data_2019_2022_IR{10,50}`
  (≈ 1,45 Go en tout si l'extraction partielle marche, 17,6 Go sinon). Cibles : fig. 6, p. 7 (0,9455 et 0,9442 pour
  IR = 10 ; 0,9588 et 0,9561 pour IR = 50). Reproduit l'entraînement sur leurs traits, pas la construction du graphe.
- **(R-b) Expérience principale** : graphe + traits + évaluation (9,5 Go), régénération des paires (machine à
  ≥ 64 Go de mémoire, à confirmer), entraînement IR = 10, 50, 100. Cibles : 0,94 / 0,96 / 0,95 (fig. 11, p. 12) et
  0,948 (p. 12). C'est la seule voie qui donne un modèle 2016→2019 et 2019→2022 sur leur graphe, donc la base du test
  hors échantillon.
- **(R-c) Contrôle de cohérence** : recalculer l'aire sous la courbe à partir de `frp_example` (leurs propres sorties).
  Ce n'est pas une reproduction ; à préenregistrer comme contrôle, jamais avant scellement.

Une machine louée est nécessaire pour (R-b), probablement pour (R-a) : **nœud de dépense, devis et GO de Lazar**.

---

## 4. Test hors échantillon à partir d'OpenAlex

### 4.1 La moisson de `donnees/moisson-openalex-v1` ne couvre pas leurs concepts

Lu : requête déclarée v2 et les fiches `.moisson.json` (comptes et filtres, aucun contenu d'œuvre). Les cinq
sous-domaines (contrôle et alignement des intelligences artificielles, vérification formelle, sécurité des systèmes,
statistique séquentielle, neurosciences computationnelles) sont **disjoints** de l'optique et de la physique quantique,
et le `select=` garde `id, doi, title, publication_date, authorships, referenced_works, concepts, topics,
primary_location, type` : **ni résumé (`abstract_inverted_index`), ni `counts_by_year`, ni `cited_by_count`**. Or leur
graphe exige le résumé (repérage des concepts) et les citations annuelles (étiquettes). Non réutilisable.

### 4.2 Découpage proposé (à sceller avant toute lecture)

Leur graphe s'arrête en avril 2023 ; nous sommes le 31 octobre 2026. Une fenêtre de trois ans complète après leur
coupure n'existe que jusqu'à fin 2025.
- **Test principal, même tâche, même horizon** : traits à *y* = **2022** (fin décembre 2022) calculés sur **leur**
  graphe publié (les fichiers 2022 sont dans `data_for_features`) ; modèle figé = `train_model_2022_run.py`
  (2019→2022), entraîné par nous à l'identique ; étiquettes = arêtes nouvelles créées par les articles publiés du
  **1er janvier 2023 au 31 décembre 2025**, citations 2023 + 2024 + 2025, seuils IR = 10, 50, 100. Aucune information
  postérieure à 2022 n'entre dans les traits ni dans l'entraînement : c'est un vrai hors échantillon.
- **Test secondaire, « liens apparus de 2024 à 2026 »** (formulation du message n° 261) : graphe prolongé jusqu'à fin
  2023 par notre moisson, traits à *y* = 2023, étiquette = **apparition** de l'arête entre le 1er janvier 2024 et la date
  de moisson (fenêtre incomplète, ≈ 2 ans 10 mois). Leur modèle n'a pas été entraîné pour la prédiction de liens pure :
  le rapporter comme transfert de tâche, avec IR = 1 (au moins une citation) comme point le plus proche.

### 4.3 Requête OpenAlex (déclarée, non lancée)

Mêmes règles que leur code : articles de revue, titre et résumé présents, date de publication.
```
filter=from_publication_date:2023-01-01,to_publication_date:2025-12-31,has_abstract:true,type_crossref:journal-article
select=id,title,abstract_inverted_index,publication_date,cited_by_count,counts_by_year,type,type_crossref
per-page=200, sort=publication_date:asc, curseur
```
(le champ exact du type est une inconnue, I-2 : leur code filtre `type == 'journal-article'` sur l'ancien instantané ;
le type d'OpenAlex est devenu « article » et l'ancien vocabulaire survit dans `type_crossref`.) Puis traitement
**identique** au leur : `get_single_article_string` (minuscules, remplacements), recherche de sous-chaîne des 37 960
concepts, paires, horodatage en jours depuis 1990, citations annuelles.

**Volume et coût** : inconnus (I-1). Ordre de grandeur : leur filtre gardait 92 millions d'articles jusqu'en avril 2023 ;
trois années récentes en font vraisemblablement plus de 10 millions → plus de 50 000 pages de filtre, soit plus de 5 USD
au tarif déclaré dans `requete-declaree-v1.md` (0,0001 USD par page de filtre ; allocation gratuite de 1 USD par jour),
c'est-à-dire **plus d'une semaine d'allocation gratuite**, et des dizaines de Go de texte brut (le disque libre ici est
de 9 Go). Alternative sans crédit : l'**instantané public** d'OpenAlex (CC0, accès anonyme) — manifeste du 14 octobre
2026 lu : 464 765 485 œuvres, 1 898 fichiers parquet, **744 Go** (675 Go en lignes JSON compressées), partitionnés par
date de mise à jour, pas par date de publication ; le format parquet permet de ne tirer que les colonnes utiles, mais la
colonne des résumés reste le gros du volume. Les deux voies supposent une machine louée : nœud de dépense.

### 4.4 Témoins appariés sur le degré et l'âge

Pour chaque paire positive (*u*, *v*) (reliée dans la fenêtre, ≥ IR) : tirer *k* paires négatives (non reliées jusqu'à
la fin de la fenêtre) dans la même case de
(i) degré de chaque extrémité à *y*, ordonné (degré bas, degré haut), en classes de quantiles (ou classes log2) fixées
avant lecture ;
(ii) âge de chaque concept à *y* = *y* − année de sa première arête dans le graphe (tiré de `full_dynamic_graph`),
en classes fixées.
Graines par `numpy.random.SeedSequence` (R9). Rapporter : l'aire sous la courbe sur l'échantillon aléatoire « à leur
manière » (10 millions de paires) **et** sur l'échantillon apparié ; et les mêmes pour des bases simples figées
(attachement préférentiel, similarité cosinus seule, Simpson seule, degré seul). Le test apparié mesure ce que le modèle
sait au-delà de « les concepts populaires et anciens se relient davantage ».

### 4.5 Pièges à fixer dans le préenregistrement

1. **Dérive de la source** : OpenAlex est passé à « Walden » en novembre 2025 (`RELEASE_NOTES` du seau public :
   « switch to walden dataset », 463 millions d'œuvres avec les fiches « xpack »), avec retraits et récupérations de
   résumés (2025-01-29 : 350 000 résumés retirés ; 2026-06-25 : 1,4 million récupérés), reclassements de types
   (2024-07-30 : 4 millions d'« article » reclassés). Le taux de création d'arêtes peut changer pour des raisons de base,
   pas de science. Contrôle proposé : **pont** — reconstruire avec la moisson actuelle les arêtes 2020–2022 et comparer
   **les comptes** (arêtes, articles) à leur graphe publié, avec une tolérance déclarée d'avance.
2. **Citations révisées** : `counts_by_year` actuel ≠ celui de leur instantané de 2023 ; les étiquettes 2023–2025
   viennent forcément de l'actuel. À rapporter, pas à corriger.
3. **Fenêtre 2026 incomplète** : aucune étiquette à trois ans au-delà de fin 2025.
4. **Recherche de sous-chaîne sans limite de mot** : à reproduire telle quelle (fidélité), avec une variante
   « mot entier » seulement en analyse secondaire déclarée.
5. **Normalisation dépendante de l'échantillon** : `rescaling_col` divise par le maximum de l'ensemble évalué ;
   l'échantillon apparié aurait d'autres maxima. Figer : maxima calculés sur le graphe entier de l'année *y*
   (`get_norm_features`), identiques pour tous les ensembles.
6. **Variance d'une course à l'autre** : non publiée ; le critère « aire retrouvée » doit porter une tolérance fixée
   d'avance et un nombre de graines.

---

## 5. Couverture du vocabulaire du contrôle des intelligences artificielles

Simple recherche de chaînes dans `full_domain_concepts.txt` (37 960 concepts, `1544c30a5470af06…`), script
`scripts-v1/couverture_vocabulaire_v1.py` (`0113767ffc20cf2d…`), sortie complète
`couverture-vocabulaire-controle-v1.tsv` (`0f8dc65752ded4ac…`). Ce ne sont pas des mesures de résultat.

- **Absents (0 concept, ni exact ni comme mot)** : sabotage, e-value (« e value », « evalue »), safety, AI safety,
  misalignment, deception, honesty, interpretability, mechanistic, sparse autoencoder, residual stream, reward hacking,
  reward model, red team, jailbreak, backdoor, steganography, sandbagging, scheming, situational awareness, chain of
  thought, language model, large language model, attention, multi agent, out of distribution, sequential test,
  hypothesis test, betting, watermark, oversight, audit, evaluation awareness, sycophancy, hallucination, linear probe.
- **Présents comme concepts exacts** : neural network, machine learning, reinforcement learning, artificial
  intelligence, adversarial attack.
- **Présents seulement dans un autre sens (homonymes de physique)** : probe (20 : « weak probe beam », « x ray
  probe »…), monitoring (2 : « non invasive monitoring »…), steering (16 : « EPR steering », « beam steering »…),
  activation (12 : « activation energy »…), alignment (2 : « magnetic field alignment »…), control (65 : « quantum
  control »…), conformal (20 : « conformal field »…), martingale (2), calibration (4), agent (8 : dont « dishonest
  agent », « adversarial agent »), trojan (2 : « trojan horse attack »), collusion (1 : « collusion attack »).

**Conclusion** : la liste ne couvre pas le contrôle des intelligences artificielles ; les quelques mots communs
portent un sens de physique et créeraient de fausses arêtes. La liste générale de 368 825 concepts **n'est pas publiée**
(seule la liste du domaine l'est). **Extension proposée** : relancer leur chaîne (`create_concepts/` : RAKE, seuils 9 et
6, filtres) sur un corpus arXiv `cs.LG`, `cs.AI`, `cs.CL`, `cs.CR`, `stat.ML` — ce qui construit un **autre graphe** et
demande un **autre entraînement** : on testerait alors leur *méthode*, pas leur *modèle*. Le test hors échantillon de
leur modèle doit donc rester dans leur domaine (optique et quantique) ; le transfert au contrôle des intelligences
artificielles est une seconde expérience, à préenregistrer à part.

---

## 6. Ce que cela implique pour le critère de mort (message n° 261, point 3)

- « Aire publiée non retrouvée » doit nommer **quelle** aire (banc, fig. 6 p. 7 ; ou principale, fig. 11 p. 12), la
  tolérance et le nombre de graines. Proposition à discuter avec conv-audit : voie (R-a) d'abord (peu chère), voie
  (R-b) seulement si (R-a) passe.
- « Échec hors échantillon » doit nommer la métrique (aire sur l'échantillon apparié), le seuil et les bases à battre
  (attachement préférentiel, Simpson seule), fixés avant la moisson 2023–2025.

---

## 7. Inconnues

- **I-1** Volume d'OpenAlex 2023–2025 (articles de revue avec résumé) : nombre de pages, crédits, jours d'allocation
  gratuite, octets. Une requête de comptage (`group_by`) répondrait ; non lancée (interface à crédits).
- **I-2** Champ de type à filtrer dans OpenAlex actuel (`type:article` ou `type_crossref:journal-article`) et
  équivalence avec leur `journal-article` de 2023.
- **I-3** Ampleur de la dérive de résumés et d'arêtes entre leur instantané (2023) et Walden (2025–2026).
- **I-4** Écart entre leurs `counts_by_year` et ceux d'aujourd'hui pour les mêmes articles.
- **I-5** Étape de « nettoyage » qui produit les fichiers `_clean` d'entraînement : absente du code publié.
- **I-6** Temps réel d'entraînement sur processeur et nombre d'itérations avant l'arrêt précoce.
- **I-7** Mémoire de pointe pour régénérer les 689 millions de paires non reliées (machine à dimensionner).
- **I-8** Extraction d'un seul membre d'une archive du banc par requêtes partielles (probable, non essayée).
- **I-9** Variance d'une graine à l'autre de leurs aires (une seule course publiée, graine 42).
- **I-10** Valeurs de la fig. 4(a) pour les IR autres que 10, 50, 100 : courbe seulement, non tabulées.
- **I-11** Différences éventuelles entre l'arXiv v4 (notre PDF) et la version publiée dans *MLST* (non versée).
- **I-12** Coût et type de machine louée (mémoire ≥ 64 Go ? disque ≥ 100 Go ?) : devis à écrire.
- **I-13** Seuils du critère de mort (tolérance de reproduction, seuil hors échantillon, bases) : à fixer par
  préenregistrement contre-lu (R1, R2).

---

## 8. Fichiers de cette note

Tous sous `docs/notes/gu-krenn-v1/`, chacun avec son `.sha256` :
`sources-amont-v1/Impact4Cast/` (code cloné, lu, non exécuté) ; `sources-amont-v1/Impact4Cast-git-d2af4f3-v1.tar` ;
`…-ls-files-…`, `…-journal-…` ; `sources-amont-v1/zenodo-metadonnees-v1/` (deux fiches JSON, six listes TSV) ;
`sources-amont-v1/openalex-instantane-metadonnees-v1/` (LISEZMOI, notes de version, deux manifestes du 14 octobre
2026) ; `scripts-v1/` (deux scripts écrits ici) ; `couverture-vocabulaire-controle-v1.tsv` ; cette note.
Rien n'est commité (consigne de la demande).
