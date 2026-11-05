# Préenregistrement — Gu et Krenn 2024 : reproduction de l'aire sous la courbe et test hors échantillon, v1 (BROUILLON, NON SCELLÉ)

- Auteur : lignée « session-depot » (Claude, Opus 5.5), sur le message n° 261 de conv-audit (mot de Lazar relayé,
  R-621), point 2 (« préenregistrement court, scellé avant le test hors échantillon, contre-lu par un autre modèle ») et
  point 3 (critère de mort).
- Date (UTC) : 31 octobre 2026, 02:49 (`date -u`).
- Commit du code d'analyse : aucun encore. Le code d'analyse (`scripts/gu_krenn_*_v1.py`, à écrire) sera scellé et son
  commit inscrit ici **avant** le scellement ; tant qu'il manque, le préenregistrement ne se scelle pas.
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
  - Gabarit : `prereg/gabarit-preregistrement-v1.md` `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`

## Hypothèse

Le classeur de Gu et Krenn (réseau entièrement connecté sur 141 traits d'un graphe de 37 960 concepts d'optique et de
physique quantique [p. 3]) est un instrument fiable pour le bras Gu-Krenn du bisociateur, c'est-à-dire :

- **HA (reproduction)** : réentraîné à partir de leur code et de leurs données publiées, sur leur partage temporel, il
  retrouve leurs aires sous la courbe publiées (aucun poids n'est publié : réentraîner est obligatoire).
- **HB (hors échantillon)** : figé avant toute lecture des données postérieures à 2022, il classe les paires de concepts
  qui se relient de 2024 à 2026 au-dessus des paires qui restent non reliées, **à degré et âge égaux**, et mieux que deux
  règles simples (attachement préférentiel, similarité de Simpson seule).

Hypothèses de travail : leur graphe publié (instantané OpenAlex d'avril 2023 [p. 3]) est complet pour les articles
publiés jusqu'au 31 décembre 2022 ; la dérive de la base OpenAlex actuelle (« Walden », novembre 2025 — SUPPOSÉ, notes
de version du seau public) est contrôlée par le pont (Plan, étape B2). Leur modèle prédit l'**impact** (au moins IR
citations dans les trois ans [p. 4]) et non l'apparition pure : HB est donc un transfert de tâche, déclaré comme tel.

## Prédiction chiffrée et signe attendu

**(A) Reproduction** — aucun signe d'écart attendu (bilatéral). Valeurs cibles, une seule course publiée chacune :

| Cas | Cible publiée |
|---|---|
| A1 banc, entraînement 2016→2019, évaluation 2019→2022, IR = 10 : réseau / XGBoost | 0,9455 / 0,9442 [p. 7, fig. 6(a)] |
| A1 banc, même découpage, IR = 50 : réseau / XGBoost | 0,9588 / 0,9561 [p. 7, fig. 6(b)] |
| A2 principal, entraînement 2016→2019, évaluation 2019→2022, IR = 10 / 50 / 100 | 0,94 / 0,96 / 0,95 [p. 12, fig. 11] ; IR = 100 : 0,948 [p. 12] |

Prédiction : chaque moyenne sur trois graines (nombre SUPPOSÉ, choisi ici) tombe à moins de 0,010 de sa cible pour A1, à moins de 0,015 pour A2
(tolérances SUPPOSÉ, choisies ici : variance d'une graine à l'autre non publiée ; A2 publié arrondi à deux décimales).
Réfutation : un écart au-delà de 0,020 (A1) ou 0,025 (A2) sur un seul cas, dans un sens ou dans l'autre (SUPPOSÉ).

**(B) Hors échantillon** (modèle 2019→2022, IR = 10, traits de fin 2022, apparition d'une arête du 1er janvier 2024
au 30 septembre 2026) — signe attendu : aire appariée > 0,5 et modèle > chacune des deux règles simples sur
l'échantillon apparié. Ordres de grandeur, SUPPOSÉ (aucun appui publié pour l'apparition pure) : aire sur l'échantillon
aléatoire ≈ 0,90 (leur variante sans réentraînement descend de 0,9463 à 0,9311 quand l'évaluation recule de 2018 à
2022 [p. 8, fig. 7]) ; aire appariée ≈ 0,70. Réfutation : seuils de la section Seuil non atteints. Aucun signe n'est
visé (R3) : les deux issues décident du bras.

## Métrique

- **Aire sous la courbe** du taux de vrais positifs contre le taux de faux positifs, sur les sorties brutes du réseau
  (comme leur code, `roc_auc_score` — SUPPOSÉ, code lu) ; ex æquo comptés pour moitié.
- **A** : aire de chaque graine sur leur ensemble d'évaluation publié (`data_eval.zip`, traits déjà calculés —
  SUPPOSÉ, métadonnées Zenodo) pour A2, et sur `eval_data_2019_2022_IR{10,50}` pour A1 ; statistique = moyenne des
  trois graines ; étendue des graines rapportée.
- **B, trois statistiques**, chacune = moyenne des aires des trois graines du modèle figé :
  - **B-i** aire sur l'échantillon aléatoire « à leur manière » : 10 millions de paires tirées uniformément parmi les
    paires non reliées au 31 décembre 2023 [taille : p. 4] ;
  - **B-ii** aire sur l'échantillon apparié (positives et leurs témoins, section Plan) ;
  - **B-iii** différence appariée : aire appariée du modèle − la plus haute des aires appariées des deux règles simples,
    calculées sur les mêmes rééchantillons.
- **Intervalles** : rééchantillonnage (bootstrap) par percentiles, 95 %, 2 000 rééchantillons (SUPPOSÉ) ; unité de
  rééchantillonnage = la paire pour B-i, la grappe « une positive et ses k témoins » pour B-ii et B-iii. Pour A, pas
  d'intervalle décisif (l'incertitude publiée est nulle) ; l'étendue des graines est rapportée.
- **Règles simples** : attachement préférentiel = produit des degrés à fin 2022 ; Simpson = voisins communs / plus
  petit degré, à fin 2022 (meilleur trait seul de leur papier, 0,8880 en 2019 [p. 13, fig. 12]).

## Seuil

- **A1 retrouvée** : les quatre cas à moins de 0,010 de la cible ; **non retrouvée** : un cas au-delà de 0,020 ;
  entre les deux : **retrouvée avec réserve** (on continue, la réserve est rapportée). SUPPOSÉ.
- **A2 retrouvée** : les trois cas à moins de 0,015 ; **non retrouvée** : un cas au-delà de 0,025 ; entre les deux :
  retrouvée avec réserve. SUPPOSÉ.
- **B réussi** si les trois tiennent : B-i ≥ 0,85 (estimation ponctuelle) ; borne basse de l'intervalle de B-ii
  > 0,60 ; borne basse de l'intervalle de B-iii > 0. SUPPOSÉ. **B échoué** si l'une manque.
- Les tests sont conjonctifs (tout doit passer pour conclure « fiable ») : aucune correction pour comparaisons
  multiples n'est nécessaire pour cette conclusion ; tout le reste est rapporté comme information, sans verdict.

## Plan d'analyse

**Graines (R9)** : `numpy.random.SeedSequence(293431315339861648349832936273213435135)` (numpy ≥ 1.25), `.spawn(6)` :
0 → graines d'entraînement A1 (trois, par `.spawn(3)`, entières par `generate_state(1)`), 1 → A2, 2 → modèle figé
2019→2022 de B, 3 → tirage des 10 millions de paires de B-i (premier enfant de `.spawn(2)`) et de B′ (second), 4 → témoins de B-ii, 5 → rééchantillons. Leur graine 42
(SUPPOSÉ, code) n'est pas reprise. Manifeste de run par étape (`src/controle_ia/manifeste.py`).

**A1, banc d'essai (voie la moins chère)** : leurs fichiers `train_data_2016_2019_IR{10,50}` et
`eval_data_2019_2022_IR{10,50}` (SUPPOSÉ, répertoires centraux Zenodo) ; leurs scripts `loops_fcNN.py` (trois couches
cachées de 600 [p. 8]) et `loops_xgboost.py`, hyperparamètres publiés inchangés ; 3 graines × 2 modèles × 2 IR.

**A2, expérience principale** (seulement si A1 n'est pas « non retrouvée ») : graphe `full_dynamic_graph.parquet`,
paires non reliées en 2016 régénérées [≈ 689 millions, p. 11], toutes les positives et autant de négatives, 85 % / 15 %
[p. 11], quatre couches cachées de 600, Adam, taux 3 × 10⁻⁵, lots de 1000 équilibrés [p. 11] ; 3 graines × IR = 10,
50, 100. Les matrices d'adjacence et le PageRank sont **régénérés** depuis le parquet, jamais chargés depuis leurs
pickles. Écart connu : l'étape `_clean` n'est pas publiée (écart E-1).

**B0, modèle figé** (seulement si A2 n'est pas « non retrouvée ») : `train_model_2022_run.py` (2019→2022), IR = 10,
50, 100, trois graines ; poids, traits de fin 2022 et maxima de normalisation **scellés avant toute moisson**
postérieure à 2022.

**B1, moisson** : requête déclarée de l'état des lieux (§ 4.3), articles de revue avec titre, résumé et date, publiés
du 1er janvier 2022 au 30 septembre 2026 ; traitement identique au leur (minuscules, remplacements, sous-chaîne sans
limite de mot). Champ de type fixé avant moisson sur le schéma d'une seule fiche de 2022 (inconnue I-2).

**B2, contrôles avant étiquettes** (lus avant toute étiquette 2024–2026) :
- **pont** : paires créées par les articles de 2022 dans notre moisson contre leur graphe ; indice de Jaccard des
  ensembles ≥ 0,80 et rapport des comptes dans [0,85 ; 1,18] (SUPPOSÉ) ;
- **contrôle des traits** : nos traits de fin 2019 recalculés sur leurs 10 millions de paires d'évaluation, comparés à
  leur fichier publié sur 10 000 lignes tirées au hasard ; écart relatif maximal ≤ 10⁻⁵ (SUPPOSÉ) ;
- **contrôle de métrique** : notre code d'aire appliqué à `frp_example` (leurs sorties et leur vérité) ; écart ≤ 0,005
  à 0,94 / 0,96 / 0,95 [p. 12] (SUPPOSÉ).

**B3, population et étiquettes** : population = paires non reliées au 31 décembre 2023 (leur graphe jusqu'à fin 2022
plus nos arêtes de 2023) ; les paires reliées en 2023 sortent de la population. Étiquette = au moins un article publié du
1er janvier 2024 au 30 septembre 2026 qui les relie. Traits = ceux de fin 2022 (leur graphe seul : aucune source mêlée
dans les entrées). Normalisation : leur code d'évaluation divise chaque trait de paire par son maximum sur l'échantillon
évalué (`rescaling_col` — SUPPOSÉ, code lu) ; les maxima sont calculés une fois sur les 10 millions de paires de B-i et
**réutilisés** pour l'échantillon apparié.

**B4, témoins appariés** : positives = toutes celles des 10 millions (au plus 200 000 tirées au hasard, SUPPOSÉ) ; pour
chacune, k = 5 témoins (SUPPOSÉ) tirés dans toute la population restée non reliée au 30 septembre 2026, dans la même
case : classe de degré à fin 2022 de l'extrémité de plus bas degré et de l'autre (classe = partie entière de
log2(1 + degré)), et classe d'âge de chacune (âge = 2022 − année de sa première arête ; classes 0–1, 2–4, 5–9, 10–19,
≥ 20 ans, plus « sans arête ») — SUPPOSÉ. Tirage par rejet sur les extrémités de chaque classe. Positive sans 5 témoins
possibles : retirée, comptée.

**Rapporté comme information, sans verdict** : B avec les modèles IR = 50 et 100 ; **B′, même tâche que la leur** —
étiquette = au moins IR citations en 2023–2025 des articles qui relient la paire, 10 millions de paires tirées
uniformément parmi les non reliées à fin 2022 (enfant 3 de la graine, `.spawn(2)`, second enfant),
IR = 10, 50, 100 ; variante « mot entier » de la recherche de sous-chaîne ; variante conditionnée de A2 (0,747 / 0,694
[p. 5]) ; nombre de positives retirées par case.

## Critères de lecture gelés

| Issue | Verdict |
|---|---|
| A1 non retrouvée | HA réfutée ; arrêt (A2 et B non lancés) ; critère de mort atteint |
| A1 passe, A2 non retrouvée | HA réfutée ; arrêt (B non lancé) ; critère de mort atteint |
| A1 et A2 passent ou passent avec réserve, B réussi | HA et HB confirmées sur ce découpage ; bras admis à la course 2 (réserves rapportées) |
| A1 et A2 passent, B échoué (une des trois conditions) | HB réfutée ; critère de mort atteint ; la condition manquée est nommée |
| Un contrôle de B2 échoue, ou arrêt de B (liste d'arrêt) | B non concluant ; bras **suspendu** (non admis à la course 2, pas déclaré mort) ; nouveau préenregistrement ou décision de Lazar |
| B-i passe nettement, B-ii ou B-iii échoue | lecture : le modèle lit surtout degré et âge ; verdict « échoué » inchangé |

**Audit de symétrie (R4)** : déclenché par une aire de A à moins de 0,002 de chaque cible (trop proche pour une autre
machine), par un écart de A au-delà de la tolérance **vers le haut**, par B-ii > 0,90, ou par B-i qui dépasse leur
meilleure valeur publiée (0,9588 [p. 7]) — seuils 0,002 et 0,90 SUPPOSÉ : on cherche une fuite (dates, maxima, recouvrement entre entraînement et
évaluation) avant tout verdict.

## Critère de mort (message n° 261, point 3)

Écrit d'avance : le bras Gu-Krenn du bisociateur exploratoire de la course 2 est **retiré** si l'une de ces trois
issues se produit : A1 non retrouvée ; A2 non retrouvée ; B échoué. « Non concluant » ne vaut pas mort mais interdit
l'usage du bras dans la course 2 tant qu'un préenregistrement nouveau, scellé, ne l'a pas tranché. Le retrait n'est
levé par aucune analyse secondaire (B′, IR = 50 ou 100, variante « mot entier »).

## Liste d'arrêt

- Empreinte d'une archive téléchargée différente de celle de Zenodo → arrêt, nouveau téléchargement dans un dossier neuf.
- Tentative de charger un pickle de leurs archives (adjacence, PageRank) ou un poids sans `weights_only=True` → garde
  refuse et arrête ; garde testée sur un cas sain et sur un artefact (R5).
- Date postérieure au 31 décembre 2022 dans les traits ou l'entraînement de B0 → arrêt, B invalide.
- Coût cumulé au plafond du devis → arrêt de l'instance par son identifiant (R10), consigné dans `registres/arrets.md`.
- Mémoire ou disque épuisés → arrêt ; aucun sous-échantillonnage silencieux (R5) : toute réduction passe par un écart
  déclaré.
- Entraînement qui diverge (valeur non numérique) ou sans arrêt précoce après 10 fois le nombre d'itérations du
  premier passage (SUPPOSÉ) → arrêt de la course, consigné.
- Moisson incomplète : moins de 99 % (SUPPOSÉ) du compte annoncé par OpenAlex pour la même requête → arrêt avant B2.
- Moins de 2 000 positives dans B-i (SUPPOSÉ) → B non concluant (puissance).
- Plus de 10 % des positives sans témoins (SUPPOSÉ) → B non concluant.
- Pont, contrôle des traits ou contrôle de métrique hors tolérance → B non concluant, avant toute étiquette.

## Ordre de lecture et ce qui n'est jamais lu avant scellement

1. Contre-lecture (R2), scellement de ce texte et du code d'analyse, devis, GO de Lazar.
2. Téléchargements dans des dossiers neufs ; aucun code exécuté depuis ces dossiers ; vérification des empreintes.
3. Contrôle de métrique sur `frp_example` → lu.
4. A1 → verdict écrit et scellé avant A2.
5. A2 → verdict écrit et scellé avant B0.
6. B0 → poids, traits de fin 2022 et maxima scellés avant B1.
7. B1, puis B2 (pont et contrôle des traits) → lus et scellés avant toute étiquette 2024–2026.
8. B3, B4, puis B-i, B-ii, B-iii et les analyses d'information, en une seule exécution du script d'analyse scellé.

**Jamais lu avant scellement** : `frp_example.zip` ; toute aire ou métrique, sur leurs données ou sur OpenAlex ;
tout contenu OpenAlex postérieur à 2022 (seul un compte agrégé de la requête, sans concept ni citation, est permis pour
le devis, inconnue I-1). **Jamais lu tout court** dans ce chantier : les branches `donnees/bras-attaque-*`,
`donnees/mode-tenu-a-l-ecart-v1`, `quarantaine/*`, et toute autre référence `donnees/*`.

## Écarts possibles et leur traitement

| Écart | Traitement |
|---|---|
| E-1 Étape `_clean` absente du code (I-5) | A2 sur la version non nettoyée, déclarée ; un échec de A2 reste un échec (la chaîne publiée ne se reproduit pas) |
| E-2 Champ de type OpenAlex (I-2) | fixé avant moisson sur le schéma d'une fiche de 2022, consigné |
| E-3 Dérive Walden, résumés retirés ou récupérés (I-3) | pont B2 ; hors tolérance → non concluant |
| E-4 Citations révisées depuis 2023 (I-4) | sans effet sur B (apparition) ; rapporté pour B′ |
| E-5 Extraction partielle d'une archive impossible (I-8) | téléchargement entier ; devis revu avant |
| E-6 Processeur au lieu de carte graphique, versions de bibliothèques non épinglées | consigné au manifeste ; couvert par la tolérance |
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

À REMPLIR — sous-agent neuf d'un autre modèle (message n° 261, point 2), qui n'a pas écrit ce texte : identifiant,
empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque.
