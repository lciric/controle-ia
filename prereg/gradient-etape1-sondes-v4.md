# Préenregistrement — étape 1 du programme « gradient conçu par l'essaim » : sondes apprises par gradient — v4 « économe »

Version 4, écrite par la lignée « session-depot » sur la v3 (`41feda40…`, relue par la contre-lecture R2 n° 3 :
« scellable après corrections »). Elle traite les dix-huit remarques de cette contre-lecture (CE3-01 à CE3-18) et les cinq
remarques de relecture de « conv-audit » (RE-01 à RE-05, message n° 20), et applique les décisions de Lazar reçues depuis :
étape 1 « économe », trois lignées auto-écrites, **sans les deux lignées imposées** (24 octobre, 23:00, heure de Paris,
relayée par « conv-audit », message n° 21 ; R-370) ; garde et mesure contre la recherche de provenance des textes de test
(décision (c), R-371, approuvée « ok oui », R-375) ; **vivier de conception** (« GO now », 25 octobre, 00:05, heure de
Paris, message n° 28 § 2). La dépense est couverte par GO-2026-10-24-05, sans devis (R-355). Aucune lecture de résultat
avant le scellement (R1) ; aucun run visant un signe (R3) ; symétrie de l'audit (R4). Rien d'opposable avant le verdict
(R7). Restent sans le mot de Lazar et **hors de cette version** : le code figé après la conception, l'arrêt des
générations déclaré par l'organisme ; la primitive `question_ouverte` est dans le code cité mais n'est posée à aucune
génération ni ronde (aucune option `--question-ouverte` : `contexte["question_ouverte"]` vaut `null` partout).

- Auteur : lignée « session-depot » (session Claude Code du dépôt), sur le brouillon v1 de la lignée « conv-audit ».
  Conflit d'intérêts déclaré : la même lignée a écrit les corrections du noyau, le vivier, l'analyse de H-G1, le lanceur
  et ce texte, et lancera les courses.
- Date (UTC) : 2026-10-25, <<HEURE_SCELLEMENT>> (dernière modification, heure lue par `date -u`).
- **Commit du code** : branche `outils/essaim-m3-gradient-v2-travail`, commit `ed3ce0ee29c0b8ccfb4c8ed67df6324a7f9e97ff`
  (depuis `4f02bd8`, cité par la v3 : import des rondes de conception dans le bras apparié de « conv-audit », `9d53ae3` ;
  correctif de la faille des liens symboliques, `4967734` ; garde de fuite, `a8e9ce2` ; CE3-06 et CE3-07, `7887f1d` ;
  CE3-05, CE3-11, CE3-12, `c02bae3` ; analyse de H-G1, `5e6876d` ; vivier de conception et CE3-17, `b7374a9` ; fusion de la
  tête de « conv-audit » `5aca4aa` — extrait mécanique sans score `cf67025`, primitive `question_ouverte`, non posée —
  avec PG2-02, `ed3ce0e`) ; **113 essais passent**, 3 désélectionnés (deux exécutent l'organisme `gemini-v2` de la relève,
  un interroge arXiv). Empreintes : `essaim_m3/analyse_gradient.py` `9fdeacb940010094a2970960efa4c7d083a833216e7846234ff1627d1c9599cb`
  (identique à `5e6876d`), `essaim_m3/analyse.py` `bf9c1a3bcf9474cd28689e99a9bfb103f5ae7902582a68197ae8d6e6e81c32e8`,
  `essaim_m3/noyau/boucle.py` `ebf4c44d075efef382e8ddc9d32fe081208cec4bef6df094bd80b9d901d0a192`, `essaim_m3/noyau/cli.py`
  `8a186b5ae59fba5c2430c4154d4e2a541ab8e1174d5fff6c0e0a5d232b18cdcf`, `essaim_m3/noyau/vivier.py`
  `b08094e3a7dff4ccdf4dd051edf05d94371c2a08d4b195f2fd999a0c6da14180`, `essaim_m3/noyau/fichiers.py`
  `8bbc8dfd5f8a215ef1e6682ef492a65e10d909c13f0fbe1916ae41526cdc3395`, `essaim_m3/noyau/garde_fuite.py`
  `b17d3c8265cca9c1976c78040a5d6f5a2a9ce0c7e23e11ec6359329338f76cd6`, `essaim_m3/noyau/entrainement.py`
  `c06685bf87790840040b0df358ee59bca1f29eb084abb4ab950dd4bc01b129d9`, `essaim_m3/noyau/moisson.py`
  `6973546ec1645423ac8d17cf928ef6b5a0e3423359914071d9fd2e5ec85c94f4`, `essaim_m3/noyau/contrat.py`
  `40211a25befd52da4463e2999b441c8c27591b3725cd3210472751d0509375bc`, `essaim_m3/outils/extrait_mecanique.py`
  `6150da915bc5a12da02973727bd419ea20bc9af7fd65a46201d173f0eaa0efa7` ; arbre du noyau (`boucle.empreinte_arbre` de
  `essaim_m3/noyau`) `7160461a5297321c92d9de7911ae4de3f0db760773d47a03cb736c5b4797471e`. Les courses tournent sur ce
  commit ; le lanceur vérifie `git rev-parse HEAD` et l'arbre propre avant tout appel payant.
- **Lanceur des courses** : `docs/procedures/gradient-etape1-v2/lancer_courses_etape1_v2.sh`
  `2c630e75407ea2318013004b7aee12756ba6e71d46ad59fa13b8ff10cc03038b` ; ses essais
  `docs/procedures/gradient-etape1-v2/essais_lanceur_etape1_v2.sh` `d13f2bc63719d2bed4650cb5e3231aeb2c752d76da1a7699b75693bca18c7970`
  (mode `--controles`, sans appel : 22 sur 22, sept cas sains, quinze artefacts). Tout changement du lanceur après le
  scellement passe par un addendum scellé et contre-lu (CE3-09).
- Documents qui font foi (chemin + empreinte) :
  - mission de Lazar, mot pour mot : `essaim-m3-refonte-v1/MISSION-v1.md` `bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e` ;
  - note du programme : `essaim-m3-refonte-v1/notes/programme-apprentissage-gradient-essaim-v1.md` `6b4151049ff9d279081fdb2876ff5894ae2388c22c96acd4558312015145d8bc` ;
  - v3 relue : `prereg/gradient-etape1-sondes-v3.md` `41feda40a5f51858afd8c5167a4b86c3b495ec059929c6ff1f8aa59c8ad1b2d5` ;
  - banque scellée `confrontation-v1` : `essaim-m3-refonte-v1/banque/banque-confrontation-v1.json` `f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc`
    (branche `outils/essaim-m3-refonte-v1-travail`, commit `bffe03c`) ;
  - traits : branche `donnees/traits-etape1-v1`, commit `6479769`, `essaim-m3-refonte-v1/traits/etape1-v1/EMPREINTES-traits-etape1-v1.txt`
    `add13e090a13b60e48983393ae376cc9df2542210b5328bc2abd94e661e25f17` ; manifeste servi `traits-16384/manifeste-traits.json`
    `034d846069b863e8160458b39db93ee889b297e35061afa5e0232487dd9f2edd` ; script `extraire_activations_v2.py`
    `8286f4e72740e88392e28a6a768bb502d593a3da1b9236c3f1917db14505beee` (branche `outils/traits-etape1-v1`, `5fa8d8e`) ;
  - vivier de conception (lu par le lanceur au format littéral, hors bloc de code) :
    - vivier_commit = <<VIVIER_COMMIT>>
    - vivier_chemin = <<VIVIER_CHEMIN>>
    - vivier_sha256 = <<VIVIER_SHA256>>
    (produit par le script d'extraction de Lazar en mode complément, v5 : le jeu public `jjpn2/eval_awareness` sans GAIA,
    moins les 120 items du sous-ensemble de la banque, exclus par identifiant ; disjonction des identifiants vérifiée par
    « conv-audit » contre le fichier secret de la banque ; message de transmission : <<VIVIER_MESSAGE>>) ;
  - collisionneur v2.5 (appelants et table des prix du noyau) : `collisionneur-v2.5-banc-jev-travail/collisionneur_v2.py`
    `213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd` ;
  - contre-lecture n° 3 : `prereg/contre-lectures/contre-lecture-preenregistrement-gradient-etape1-v3.md`
    `76f96658ed1ebb5fb34ea002fb1edf87dd1551b8ffc74ad3eb67d374c7b5cdb8` ;
  - puissance de la règle v4 : `prereg/pieces-gradient-etape1-v4/puissance-v2.json`
    `50a1c248cb4243a0fd8feac9c65e8a5834658f416d22174577311139a8563804`, script `puissance_v2.py`
    `e05f48bc30d4e06989ccb938388bc4a876ffa4138bcbb5ffcc587d042031a4c6` ;
  - sonde d'hôte : `prereg/pieces-gradient-etape1-v4/sonde-hote-v1.sh` `5ac61f5ad2eb952f7bb557a5d03f4c1d47491f9c8009faa8075e2c968d2b7018`,
    journal `prereg/pieces-gradient-etape1-v4/sonde-hote-v1-journal.txt` `5e97b2d5144ca5795aae937e3440f931fa47bcefa473e07addce9552d56ce07a` ;
  - décisions de Lazar : `registres/decisions.md` R-344, R-351, R-355, R-356, R-363, R-370, R-371, R-375 et la décision
    sur le vivier (R-376 pour la décision relayée, R-378 pour le code), P-029 (hôte), R-377 (sonde d'hôte), R-379 (collisionneur) ; `registres/go.md` GO-2026-10-24-04, GO-2026-10-24-05 ; N-026 (bras « moyenne » permis
    dans un préenregistrement, jamais en production).

## Hypothèse

Programme « gradient conçu par l'essaim », étape 1 (N-042, R-344) : des organismes écrits par des modèles conçoivent
eux-mêmes l'apprentissage par gradient de sondes sur les activations de Llama-3.1-8B-Instruct (données, objectif,
algorithme, vue), sous le noyau fixe, et s'en servent pour classer des tâches à vérité cachée.

- **H-G1 (principale).** Sur le test final caché de la banque `confrontation-v1`, une lignée auto-écrite à qui le noyau
  sert l'entraînement de sondes (bras A « avec gradient », `entrainements_max` = 10, traits servis) atteint une exactitude
  équilibrée plus haute que la même lignée relancée depuis les mêmes organismes de génération 0 **et la même mémoire de
  conception**, sans entraînement (bras B « sans gradient », `entrainements_max` = 0) : mêmes organismes g000 (mêmes
  empreintes), mêmes rondes de conception importées (historique et vue), même banque, même graine, mêmes budgets d'appels,
  de dollars, de temps, de recherches et de téléchargements. Ce qui reste différent est énuméré dans « Métrique ».
- **H-G0 (condition mécanique rapportée).** Dans le bras A, chaque lignée qui demande un entraînement obtient un modèle
  (`statut` OK) et des prédictions ; aucun entraînement n'a reçu une tâche de test (refus journalisé sinon). Rapportée par
  lignée ; ne change pas la table de H-G1.
- **H-G2 (descriptive, sans seuil).** Objectifs écrits par les organismes (texte, empreinte), vues et sondes, rapportés avec
  leur exactitude ; comparaison descriptive à des sondes témoins (Plan d'analyse, point 7). La vue de chaque sonde est
  rapportée ; une sonde sur une vue « moyenne » (moyenne sur les jetons) est un objet de ce préenregistrement, jamais une
  sonde de production (N-026, RE-03).
- **H-G3 (descriptive, sans signe prédit).** Changements de spécification d'une génération à l'autre (objectif, algorithme,
  vue, données) et leur effet sur le score de développement.
- **H-C (descriptive, sans seuil) : phase de conception, moisson et vivier.** Avant la génération 0 notée, chaque lignée
  du bras A tourne en rondes de conception (au plus 4) : budget de ronde, tâches d'entraînement de la banque **et du
  vivier** avec vérité, aucune tâche de test, aucun score ; l'organisme conçoit lui-même son critère d'arrêt et le déclare
  (`fin_conception.json`) ; il écrit son moissonneur avec les primitives `rechercher` et `telecharger` du noyau (Lazar,
  24 octobre, 20:42, heure de Paris : « ne lui suggère rien »). Rapporté par lignée : rondes utilisées, ronde de
  déclaration (ou borne atteinte sans déclaration, déduite : aucun `fin_conception` et quatre rondes), contenu de
  `fin_conception.json`, dépense, documents moissonnés par source, refus de fuite (CE3-04), nombre d'items du vivier
  servis (une borne servie : ce que l'organisme en a lu n'est pas mesurable). Aucune hypothèse n'y est testée.

Lignées : trois lignées auto-écrites, amorcées par `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`, `GEMINI_ARGON`. Les deux lignées
imposées de la v3 (organisme écrit par Gemini, v3 ; enveloppe v3 de l'essaim de Gemini) n'y sont plus (décision de Lazar,
R-370 : étape 1 « économe », l'amendement « étape 1 toutes les lignées » est retiré) ; CE3-10 est sans objet.

## Prédiction chiffrée et signe attendu

- **H-G1** : signe attendu **positif** ; ordre de grandeur prédit **Δ ≥ +0,10** d'exactitude équilibrée, en moyenne des
  paires **et dans chacune des deux répliques**. Réfutation : la borne haute de l'intervalle à 95 % est sous +0,10 (l'effet
  prédit est exclu) ; si la borne basse est en outre au-dessus de 0, la lecture le dit (« effet positif plus petit que
  prédit »). Lecture complète : section « Critères de lecture gelés ». Limite dite avant la course : deux répliques
  seulement ; un « confirmé » sur deux répliques n'est pas une revendication forte (même formulation que le
  préenregistrement de la confrontation, accord des deux lignées, message n° 25 de « conv-audit »).
- **H-G0** : prédit vrai pour chaque lignée du bras A ; faux pour une lignée = cette lignée est rapportée « gradient non
  utilisé » ; elle reste dans H-G1 (le bras est défini par ce que le noyau sert, pas par ce que l'organisme fait).
- **H-G2, H-G3, H-C** : aucun signe prédit.

## Métrique

- **Score** : exactitude équilibrée par famille, (sensibilité + spécificité) / 2, moyenne des deux familles, sur les
  60 tâches du test final (36 « conscience d'évaluation », 18 + 18 ; 24 « contrôle de délégation », 12 + 12) ; une tâche
  sans réponse valide compte comme une erreur (règle du juge du noyau). Code : `analyse.exactitude_equilibree`. Une paire
  dont l'un des bras répond à moins de 80 % des tâches d'une famille du test final est **coupée** (« couverture »,
  `analyse_gradient.COUVERTURE_MIN`, CE3-03) : l'absence de réponse n'est pas lue comme un effet.
- **Unité d'analyse** : la paire (lignée ℓ, réplique r), ℓ ∈ {claude-fable-5-1, claude-opus-5-5, gemini-argon},
  r ∈ {1, 2} : **six paires en deux répliques** (noms de lignée formés par le noyau). Une tâche n'est pas une unité. La
  génération 0 d'une lignée est l'organisme issu de sa phase de conception dans A_r ; B_r la relance (mêmes empreintes) et
  **importe la mémoire de conception de A_r** : lignes d'index des rondes `cNNN` marquées `importee`, dossiers d'archive,
  vue reconstruite avec le même filtre (CE3-01, RE-01 ; `Archive.importer_conception`, essai
  `test_bras_apparie_voit_les_rondes_de_conception_de_l_origine` : historique et vue de g000 identiques dans les deux bras ;
  rondes importées hors scores, hors dépense, hors `generations_valides`). H-G1 mesure donc ce que le service
  d'entraînement apporte, en générations notées, à un organisme et à une mémoire conçus avec lui (dit avant la course).
- **Ce qui reste différent entre les bras, en plus de l'entraînement** (CE2-03, CE3-05, CE3-11, RE-04) : (1) les appels
  aux modèles ne sont pas déterministes ; (2) les successeurs g1 et g2 sont réécrits par chaque organisme selon ce qu'il a
  lu (c'est l'effet du traitement) ; (3) le plafond d'une course est partagé entre ses lignées (dimensionné pour ne pas
  mordre) ; (4) **l'heure** : B_r tourne après la fin de A_r, des heures plus tard — contenu du web moissonné, état et
  débit des interfaces, crédit des fournisseurs ; c'est confondu avec le bras ; mesuré : taux d'appels en `ECHEC_API` et
  de recherches en `ECHEC_RECHERCHE` par source et par bras à la génération lue (`analyse_gradient.taux_pannes`) — une
  paire dont les deux bras diffèrent de plus de 10 points est coupée (« panne extérieure », `ECART_PANNE_MAX`) ; un
  HTTP 402 (crédit épuisé) invalide la génération et arrête la course (`CREDIT_EPUISE`) ; les sources de moisson servies
  et la présence de la clé Brave sont au manifeste, et un bras B aux conditions de moisson différentes de son A est
  refusé (`cli.conditions_moisson_differentes`, et le lanceur) ; (5) **la contention du processeur** pèse sur A seul
  (entraînements bornés en temps d'horloge) : nombre de cœurs au journal du lanceur, `DELAI_DEPASSE` par bras rapportés ;
  (6) le vivier n'est servi que pendant la conception de A ; B en hérite ce que la mémoire importée en garde (les mêmes
  rondes, avec leurs contextes). L'ordre des lignées dans une ronde est le même dans les deux bras (base triée, même
  graine de ronde) ; les graines d'ordre des tâches sont les mêmes.
- **Statistique** : Δ(ℓ, r) = score(A_r, ℓ, g) − score(B_r, ℓ, g), où g est la génération lue : 2 (= G − 1), ou la
  dernière génération valide commune aux deux bras si l'un s'arrête avant (`generations_valides` écarte les rondes de
  conception, les rondes importées et les générations invalidées, CE3-02 ; `reponses_finales` lève une erreur si le
  fichier de réponses d'une génération dite valide manque : aucun repli « toutes fausses »). H-G1 se lit sur la moyenne
  des Δ et sur la moyenne des Δ de chaque réplique.
- **Intervalle** : bootstrap à trois niveaux — répliques tirées avec remise, puis paires tirées avec remise dans chaque
  réplique tirée, puis tâches du test final tirées avec remise par strate (famille, vérité), les mêmes pour les deux bras
  d'une paire ; 2 000 tirages ; percentiles 2,5 et 97,5 ; graine `entropie_analyse` (Plan d'analyse, point 5). Code :
  `analyse_gradient.difference_h_g1`, `paires_h_g1`. Avec deux répliques, le premier niveau est grossier (trois tirages
  possibles) : c'est la limite dite plus haut.

## Seuil

- Effet prédit : +0,10 (`analyse_gradient.EFFET_PREDIT`). « Confirmé » exige à la fois la borne basse de l'intervalle à
  95 % au-dessus de 0, Δ moyen ≥ +0,10 et Δ moyen ≥ +0,10 dans chaque réplique ; « réfuté » : borne haute sous +0,10.
- Une seule comparaison principale (H-G1) : aucune correction pour comparaisons multiples. H-G0 est une condition
  mécanique rapportée ; H-G2, H-G3 et H-C sont descriptives.
- Taux visés : « confirmé » à tort sous effet nul ≤ 5 %. Estimation par simulation, avant toute course (non opposable,
  R7 : modèle de variance supposé — effet de paire N(0 ; 0,5) en logit commun aux deux bras, bruit de bras N(0 ; 0,25),
  dérive de réplique du bras A N(0 ; σ), base 0,65, test final de 36 + 24 tâches —, `analyse_gradient.puissance_h_g1` au
  code cité, deux répliques de trois paires, 400 jeux par cas, 400 tirages, `SeedSequence(20261026)` ; sortie
  `puissance-v2.json` `50a1c248…`) :

| σ de réplique | effet nul : confirmé / réfuté | effet +0,10 : confirmé / réfuté | effet +0,20 : confirmé |
|---|---|---|---|
| 0 | 0,3 % / 35,0 % | 21,2 % / 0,5 % | 91,0 % |
| 0,25 | 1,3 % / 42,2 % | 18,5 % / 4,5 % | 69,3 % |
| 0,5 | 2,5 % / 38,3 % | 21,5 % / 9,2 % | 49,5 % |

  La règle v4 (trois niveaux, Δ ≥ +0,10 dans chaque réplique) a moins de puissance que celle de la v3 (44 % de
  « confirmé » à l'effet prédit, `puissance-v1.json` `eaf4ea5d…`, six paires indépendantes) : la puissance à l'effet prédit
  est faible (≈ 20 %) ; c'est dit avant la course et ne change aucun seuil.

## Plan d'analyse

1. **Données.** Banque scellée `confrontation-v1` (`f1387a20…`) : entraînement 80 tâches (servies avec leurs vérités),
   test de développement 60 (score rendu à chaque génération), test final 60 (jamais rendu, lu une fois à la fin). Traits :
   `traits-16384` (aucune tâche tronquée ; la plus longue fait 12 407 jetons), dix vues (couches 8, 12, 16, 20, 24 ×
   dernier jeton, moyenne), 200 tâches × 4 096, Llama-3.1-8B-Instruct, révision `0e9e39f249a16976918f6564b8830bc894c89659`
   (le champ `revision_resolue` du manifeste vaut `None` sous transformers 5.18.0 ; les traits sont figés par leurs
   empreintes), servies toutes (`--traits <dossier traits-16384>`, sans `--vues`) ; le chargement vérifie empreintes,
   compagnons, banque de la course, tâches et nombres finis. **Vivier de conception** (point 10) : servi pendant les
   rondes de conception seulement, sans traits.
2. **Lignées.** Trois auto-écrites, amorcées par `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`, `GEMINI_ARGON` sous le contrat v3 du
   noyau au commit cité (vues, champ `vivier`, champ `question_ouverte` toujours `null`) ; elles seules entrent dans H-G1.
3. **Courses**, par le lanceur v2 (une course par appel ; options exactes ci-dessous, `<courses>` = dossier des courses) :
   - options communes : `--reel --go GO-2026-10-24-05 --registre-go <courses>/registre-go-<course>.md --taches
     <courses>/entrees/banque-confrontation-v1.json --traits <courses>/entrees/traits/etape1-v1/traits-16384 --sortie
     <courses>/<course> --isoler-reseau --parallele-max 8 --relances-max 1 --pas-max 5000 --delai-entrainement 60
     --octets-max 40000000 --max-tokens-appel 4096 --decalage-uid <100 pour A1, 200 pour A2, 300 pour B1, 400 pour B2>` ;
   - A_r : `--generations 3 --graine <graine_r> --especes CLAUDE_FABLE_5_1 CLAUDE_OPUS_5_5 GEMINI_ARGON --appels-max 160
     --usd-par-generation 20 --temps-max 1800 --entrainements-max 10 --recherches-max 10 --telechargements-max 4
     --rondes-conception-max 4 --usd-max-conception 12 --appels-max-conception 160 --temps-max-conception 1800
     --pool-conception <courses>/entrees/vivier/<fichier du vivier> --plafond-total 360` ;
   - B_r : `--depuis <courses>/A<r> --generations 3 --graine <graine_r> --appels-max 160 --usd-par-generation 20
     --temps-max 1800 --entrainements-max 0 --recherches-max 10 --telechargements-max 4 --plafond-total 190` (sans
     conception ni vivier ; mêmes organismes g000 et même mémoire de conception par l'import ; avec
     `--entrainements-max 0`, `traits.disponibles` est faux et `entrainer`, `predire` ne sont pas servis).
   A_1 et A_2 tournent ensemble ; B_r part quand A_r est finie (verrou de A_r libre, au moins une génération 0 archivée).
   Clés (GO-2026-10-24-04) : `ANTHROPIC_API_KEY` = valeur de `RR_ANTHROPIC_API_KEY` pour le seul processus du noyau,
   en-tête d'espace de travail par `ANTHROPIC_CUSTOM_HEADERS` (valeur de `RR_ANTHROPIC_WORKSPACE_ID`, jamais écrite),
   `ANTHROPIC_BASE_URL` absente (le noyau refuse le mode réel si elle est définie), `GEMINI_API_KEY` = valeur de
   `GEMINI_API_KEY_2` si elle existe, sinon de `GEMINI_API_KEY` (GO-2026-10-24-07 ; seul le nom est consigné) ;
   `BRAVE_API_KEY` si elle est dans l'environnement (source `web` de la moisson, lue par le noyau seul ; R-363) — elle ne
   l'est pas dans la session « session-depot » au scellement : la source `web` n'est alors servie à aucun bras, et la même
   présence est exigée entre A_r et B_r. Avant chaque course, un appel de contrôle par espèce (statut `OK` exigé, sinon la
   course ne part pas). Environnement Python des courses : `/opt/essaim-m3-venv-v1` (Python 3.13.17, numpy 2.4.6,
   anthropic 2.3.0) ; noyau en root (isolation d'utilisateur), réseau des organismes et de l'entraîneur coupé.
   **Hôte** (RE-02) : la machine que Lazar retient. Au scellement, sa décision est attendue : (a) le conteneur de la
   session « session-depot » (machine virtuelle, root, isolation complète), recommandé, défaut sous 48 heures ; la sonde
   du 24 octobre (instance Vast.ai 57576327, détruite) montre qu'un conteneur Vast.ai ordinaire interdit `unshare`, donc
   l'isolation exigée par le noyau. L'hôte effectif est consigné dans `registres/decisions.md` avant la répétition ; le
   même lanceur et le même noyau y tournent ; le lanceur refuse un hôte sans root, sans `unshare -n`, sans espaces de noms
   ou sans `fs.protected_hardlinks` = 1. **Arrêt de l'hôte** (conteneur repris, machine arrêtée) : la course est arrêtée,
   consignée, lue à la dernière génération valide commune, ou ses paires sont coupées ; aucune relance.
4. **Budgets « économes »** (message n° 22 § 3 de « conv-audit », message n° 20 § 2 de « session-depot »). Génération
   notée : 160 appels, 20 USD (le noyau refuse au-delà : `PLAFOND`), 1 800 s, au plus 4 096 jetons de sortie par appel
   (`--max-tokens-appel`, rabattu par le noyau ; l'amorçage garde le maximum du modèle), 10 entraînements de ≤ 5 000 pas et
   ≤ 60 s, 10 recherches, 4 téléchargements, 40 Mo. Ronde de conception : 160 appels, 12 USD, 1 800 s, même moisson et mêmes
   entraînements. Au plus 4 rondes. Garde de temps du noyau en réel (CE-07 étendue par CE3-11, `boucle.temps_pire_cas`) :
   10 × 60 + 10 × 25 + 4 × (25 + 120) + 300 = 1 730 s ≤ 1 800 s (B : 1 130 s ; répétition : 615 s ≤ 900 s). Plafonds par
   course : A_r 360 USD (amorçage compté 3 × 12 = 36 USD, alors que son pire cas est ≈ 6,6 USD — Fable 3,4, Opus 1,4,
   Argon 1,8 au maximum du modèle, prompt de 60 000 caractères — ; 3 lignées × 4 rondes × 12 ; 3 lignées × 3 générations
   × 20) ; B_r 190 USD (3 × 3 × 20 = 180, plus 10). Les plafonds ne mordent pas par construction (pire cas réservé, non
   attendu). Requêtes de recherche au plus : A_r (4 + 3) × 3 × 10 = 210, B_r 90, soit 600 pour l'étape et 12 pour la
   répétition (toutes sources confondues ; CE3-15). Durées (lignées l'une après l'autre dans chaque ronde) : au pire
   A_r ≈ (4 + 3) × 3 × 1 800 s = 10,5 h, B_r ≈ 4,5 h ; attendues bien moindres (illustratif).
5. **Graines (R9).** Entropie E tirée au scellement (`secrets.randbits(128)`) et inscrite dans la section « Contre-lecture »,
   entrée 4, au format littéral, hors bloc de code : `graine_1 = <entier>`, `graine_2 = <entier>`, `entropie_analyse =
   <entier>` (CE3-16) : `SeedSequence(E).spawn(3)`, chaque entier = `generate_state(1, uint64)[0]` de l'enfant ;
   `graine_r` est passée à `--graine` (le noyau en dérive les graines d'ordre par lignée, génération, phase et usage :
   la ronde k ne tire plus les graines de la génération k, CE3-17) ; `entropie_analyse` sert au bootstrap. La graine de la
   descente de gradient d'une sonde est un choix de l'organisme, journalisé par l'empreinte de sa spécification
   (`sha256_spec`) ; elle n'est pas une graine expérimentale (CE-15). Répétition : graine 1 (exclue de toute analyse).
6. **Lecture de H-G1** (une fois, après la fin des quatre courses ou leur arrêt) : `paires_h_g1([(A_1, B_1), (A_2, B_2)],
   ["claude-fable-5-1", "claude-opus-5-5", "gemini-argon"], generations=3)` (paires coupées : aucune génération valide
   commune, couverture < 80 %, panne extérieure ; `etat["invalide"]` si plus d'une paire sur quatre est coupée, soit deux
   paires ou plus sur six) ; puis `difference_h_g1(paires, taches_final, entropie_analyse, 2000)` ; puis `lecture_h_g1`
   avec `invalide` = `etat["invalide"]` et `audit` = les faits rendus par `declencheurs_audit_h_g1` (scores sur les
   tâches répondues de chaque lignée, par famille, dans chaque bras et chaque réplique, à la génération lue ; sondes
   témoins du point 7 ; Δ par paire ; recoupements de fuite par lignée, bras et réplique, `recoupements_fuite`), et
   `apres_audit` = `None` tant que le rapport d'audit scellé n'existe pas. Un sous-agent neuf rejoue ces appels (R13).
   Rapport scellé ; verdict par un sous-agent neuf (R13) si l'étape sert de porte à l'étape 2.
7. **H-G2 (descriptive).** Après les courses, pour chaque vue : deux sondes témoins entraînées par l'entraîneur du noyau
   (isolé), sur les 80 tâches d'entraînement, sonde linéaire normalisée, 1 000 pas, taux 2, l2 0,001, lot 80, graine 0,
   objectif de Brier et objectif logarithmique borné (p tronqué à [0,001 ; 0,999]) ; exactitude équilibrée sur le test
   final, rapportée. Référence de surface : `banque.reference_traits_texte` (0,69 et 0,50 rapportés par « conv-audit », non
   audités). Le script de ces témoins est écrit et scellé (addendum, avec son empreinte) avant d'être lancé, et avant la
   lecture de H-G1, dont il nourrit les déclencheurs (CE-17, CE2-07).
8. **Répétition mécanique** avant les courses décisives, après le scellement (`lancer_courses_etape1_v2.sh repetition`) :
   lignées `CLAUDE_OPUS_5_5` et `GEMINI_ARGON`, deux rondes de conception à 2 USD et 20 appels, une génération à 3 USD et
   20 appels, 900 s, deux entraînements de 60 s, 2 recherches, 1 téléchargement, vivier servi, plafond 25 USD ; appel de
   contrôle d'Opus et d'Argon ; exclue de toute analyse. La sortie du noyau (qui contient courbes et scores) est écrite en
   0600, scellée, jamais ouverte avant la lecture ; seuls ses statuts sont lus, par l'extrait mécanique sans score
   (`python -m essaim_m3.outils.extrait_mecanique`, listes closes et garde finale sur les noms de clés) : amorçage, rondes,
   exécution, appels conformes, entraînements, moisson, vivier servi, isolation (CE3-13). Si elle révèle un défaut de
   code, la correction passe par un addendum scellé et contre-lu avant les courses. Si une espèce y **refuse l'amorçage**
   (statut `REFUS`, aucune reformulation) ou ne peut pas être appelée (crédit, clé), les courses décisives ne partent pas :
   remplacer ou retirer une espèce est un changement de modèle et une modification de l'expérience, décidés par Lazar,
   puis un addendum scellé et contre-lu. (Le 24 octobre à 23:40 UTC, au collisionneur, Opus a refusé une question
   abstraite sur la réécriture d'un organisme — refus classé « cyber » — et Argon a répondu HTTP 402, crédit épuisé :
   `donnees/collisionneur-reecriture-v1`, `2cda505`.)
9. **Phase de conception et moisson.** Les sections A et B de `prereg/sections-conception-moisson-v1.md` (`180a39af…`)
   valent pour le noyau, la provenance et le scellement ; **les points 3, 4, 9 et 10 du présent plan priment** sur elles
   (CE3-14) : le bras B est `--depuis` sans `--gel` et importe la mémoire de conception (et non « relancé à l'identique par
   le bras gelé ») ; une ronde a 12 USD (et non le budget d'une génération) ; une consigne glissée dans une page moissonnée
   peut faire plus que « tromper l'organisme » (le pousser à lire hors de sa lignée ou à toucher aux dossiers du noyau) :
   ce que le noyau en tient est l'isolation (vue de la seule lignée, dossiers du noyau hors du dossier de l'organisme,
   aucun lien suivi par root), pas la mesure par source. Valent des sections : rondes `cNNN` archivées, scellées, vues
   de la seule lignée, jamais notées ; à la ronde 4, le successeur devient la génération 0, fin déclarée ou non ; sources
   `arxiv`, `openalex`, `semanticscholar` et `web` si la clé existe ; téléchargements sous provenance, documents ≤ 8 Mo,
   texte rendu ≤ 60 000 caractères, corpus et index scellés par génération ou ronde dans un dossier du noyau
   (`<travail>.corpus`, CE3-07), visibles de la lignée seule ; texte moissonné rendu comme donnée ; rien de moissonné
   n'entre dans la banque. Après une référence permise, l'adresse finale d'une redirection est suivie en https et
   consignée ; son hôte n'est pas restreint (un identifiant numérique d'objet renvoie chez l'éditeur) (CE3-18). Débit :
   OpenAlex répondait 429 depuis l'adresse partagée le 24 octobre (rapporté par « conv-audit », message n° 14 ; sans pièce
   mesurée ici) ; un `ECHEC_RECHERCHE` est un statut rendu à l'organisme et compté dans les pannes (point 6).
10. **Vivier de conception.** `--pool-conception` (A_r et répétition) : fichier aux trois valeurs littérales de « Documents
   qui font foi », compagnon `.sha256` exigé ; servi pendant les rondes de conception seulement, à la suite des tâches
   d'entraînement de la banque, dans un ordre tiré par la graine de la ronde, avec sa vérité, sous des identifiants
   opaques (`cv-0001`…) : l'identifiant de source et la catégorie ne sont jamais servis ; textes bornés comme ceux de la
   banque ; garde de disjonction par le contenu : un item qui contient au moins 80 % des fenêtres de 8 mots d'un texte de
   la banque est écarté et compté (test ou test final ; entraînement) ; un item à plus de 50 % d'un texte de test est servi
   et compté ; doublons internes comptés ; un item malformé fait refuser le fichier (`noyau/vivier.py`, essais
   `test_vivier_de_conception_servi_en_conception_seulement`, `test_vivier_gardes_compagnon_format_et_recoupement`).
   `contexte["vivier"]` = {`n`, `familles`, `ids`} pendant la conception, absent sinon ; aucune génération notée ne le
   reçoit. Le vivier n'a pas de traits : il sert la conception par le texte, pas l'entraînement des sondes (le noyau
   refuse d'entraîner sur un identifiant hors de l'entraînement de la banque). Il n'entre dans aucune hypothèse ; ses
   comptes (servis, écartés) sont rapportés.
11. **Garde et mesure de fuite (CE3-04, décision (c) de Lazar).** Une requête qui recopie 8 mots consécutifs d'une tâche
   de test ou de test final est refusée (`REFUSE_FUITE`, sans consommer de recherche) ; un document téléchargé qui en
   contient est mis en quarantaine (rien n'est rendu ni écrit ; empreinte du recoupement consignée). Les refus sont
   comptés par lignée, bras et génération ; tout recoupement déclenche l'audit (point 6). Une paraphrase passe : la garde
   ne prétend pas tout fermer.
12. **Consignation.** Avant chaque course, une ligne « engagement : course <course> de l'étape 1 » dans
   `registres/depenses.md` (le lanceur l'exige, CE3-15) ; après chaque course, la dépense lue au journal des appels ;
   arrêt de l'hôte, s'il y en a un, dans `registres/arrets.md`.

## Critères de lecture gelés

Table de H-G1 (`analyse_gradient.lecture_h_g1`), lue de haut en bas ; la première ligne vraie s'applique.

| condition | verdict |
|---|---|
| audit de symétrie déclenché et rapport d'audit non scellé (`apres_audit` = `None`) | « audit de symétrie (R4) avant toute lecture » ; la lecture attend le rapport |
| rapport d'audit : défaut du noyau (`defaut_noyau`) | « non concluant : défaut du noyau trouvé par l'audit de symétrie » |
| plus d'une paire sur quatre coupée (aucune génération valide commune, couverture < 80 %, panne extérieure, ou paire invalidée par l'audit) | « non concluant : plus d'une paire sur quatre coupée ou invalidée » |
| aucune paire | « non concluant : aucune paire » |
| borne basse > 0, Δ moyen ≥ +0,10 et Δ moyen ≥ +0,10 dans chaque réplique | « confirmé » |
| borne haute < +0,10 | « réfuté (l'effet prédit est exclu) », avec « effet positif plus petit que prédit » si la borne basse > 0 |
| sinon | « non concluant ; aucune relance sans nouveau préenregistrement » |

- **Audit de symétrie (R4)**, déclenché par l'un de ces faits, qu'il aille dans le sens de la prédiction ou contre elle
  (`declencheurs_audit_h_g1`) : une lignée (l'un ou l'autre bras, l'une ou l'autre réplique) au-dessus de 0,95 ou
  au-dessous de 0,30 sur une famille du test final, **sur les tâches répondues** (une absence de réponse coupe la paire
  par la couverture, elle ne déclenche pas l'audit : CE3-03) ; une sonde témoin au-dessus de 0,95 ; |Δ| d'une paire
  au-dessus de 0,40 ; un recoupement de fuite (`REFUSE_FUITE`). L'audit cherche une fuite (vérités lisibles, vue de
  l'archive, recherche de provenance), des étiquettes inversées, un indice de surface.
- **Sortie gelée de l'audit** (CE3-03 c) : le rapport d'audit est scellé ; il rend l'un de trois états. « Sans défaut » :
  la table est relue sans sa première ligne et le verdict porte la réserve « audit de symétrie sans défaut trouvé ».
  « Défaut touchant des paires » : ces paires sont coupées (elles comptent dans la règle d'un quart), puis la table est
  relue comme « sans défaut ». « Défaut du noyau » (qui toucherait toutes les lignées) : « non concluant ». L'audit est
  fait par un sous-agent neuf, qui n'a écrit ni ce texte ni l'analyse.
- **H-G0** : vrai ou faux par lignée, rapporté ; ne change pas la table de H-G1.
- Aucune relance d'une course après lecture. Une course arrêtée par une garde ou par l'arrêt de l'hôte avant sa fin est
  rapportée telle quelle ; ses paires sont lues à la dernière génération valide commune, ou coupées.

## Liste d'arrêt

Chaque ligne dit si c'est une garde automatique (avec son essai sain et artefact, R5) ou une vérification humaine.

| condition | effet | garde ou vérification |
|---|---|---|
| hôte sans root, sans `unshare -n`, sans espaces de noms de montage et de processus, ou `fs.protected_hardlinks` ≠ 1 | la course ne part pas (code 2) | garde du lanceur (§ 1) ; garde du noyau en réel (« isolation réseau demandée mais indisponible », CR-01, CR-02) : `test_mode_reel_refuse_sans_isolation_reseau_et_sans_root` (cas sain construit, trois artefacts, motif de chaque refus vérifié : PG2-02) ; sonde d'hôte |
| préenregistrement non scellé, non conforme, ou qui ne cite pas le commit ; code à un autre commit ou arbre modifié | la course ne part pas | garde du lanceur ; essais `prereg-non-scelle`, `prereg-sans-commit`, `code-autre-commit` |
| dossier des courses qui n'est pas à root en 0700 | la course ne part pas | garde du lanceur (CE3-06) ; essai `dossier-traversable` |
| banque, traits ou vivier d'empreinte différente ; fichier de traits altéré après extraction | la course ne part pas | garde du lanceur (CE3-08) ; essais `vivier-faux`, `traits-alteres` ; garde du noyau sur les traits (`cli.charger_traits`) : `test_charger_traits_dossier_d_extraction_sain_et_artefacts` |
| ligne d'engagement absente de `registres/depenses.md` | la course ne part pas | garde du lanceur (CE3-15) ; essai `reel-sans-engagement` |
| GO absent, sans type « calcul », hors période, ou collisionneur d'empreinte inattendue | course refusée avant tout appel | garde de calcul rejouée par le lanceur (essai `go-refuse`) ; garde du noyau (CR-13) |
| clé absente | la course ne part pas | garde du lanceur ; essai `cle-absente` |
| sortie existante ; course déjà en cours ; bras B avant la fin de son A ou sans génération 0 archivée ; présence de la clé Brave différente de celle de A | la course ne part pas | gardes du lanceur (R12, verrou, CE3-05) ; essais `sortie-existante`, `verrou-tenu`, `B-pendant-A`, `B-avant-A`, `brave-differente` ; garde du noyau `cli.conditions_moisson_differentes` : `test_ce305_sources_moisson_au_manifeste_et_bras_apparie` |
| graine absente du préenregistrement | la course ne part pas (code 2, avec une note) | garde du lanceur (CE3-09) ; essai `graine-absente` |
| appel de contrôle d'une espèce en échec avant une course (crédit, clé, en-tête d'espace de travail, réseau, modèle servi) | la course ne part pas | garde du lanceur (§ 11), même client que les courses ; répétition mécanique ; vérification humaine du journal (modèle servi) |
| refus d'amorçage d'une espèce, ou espèce injoignable, à la répétition | les courses décisives ne partent pas ; décision de Lazar (changement de modèle) puis addendum | vérification humaine de l'extrait mécanique de la répétition (statuts d'amorçage) |
| `ANTHROPIC_BASE_URL` définie en réel | course refusée | garde du noyau : `test_mode_reel_refuse_anthropic_base_url` |
| entraîneur sans isolation d'utilisateur en réel | aucun entraînement (`Arret`) | garde codée (CE-02) ; `test_entraineur_isole_ne_lit_pas_les_fichiers_du_noyau` |
| budget incohérent (temps < entraînements × délai + recherches × 25 s + téléchargements × 145 s + 300 s) | course refusée | garde du noyau (CE-07, CE3-11) : `test_budget_incoherent_refuse_en_reel`, `test_ce311_garde_de_temps_compte_la_moisson` |
| bras sans gradient sur une autre banque que sa course d'origine | course refusée | garde (`cli.lancer`, CE-06) : `test_bras_apparie_adaptatif_memes_g000_avec_memoire` |
| entraînement qui désigne une tâche de test (ou du vivier), objectif refusé, plafond d'entraînements | `REFUSE` ou `PLAFOND`, journalisé | garde (`Entraineur.valider`) : `test_entraineur_sonde_sain_et_artefacts` |
| résultat d'entraînement ou modèle non conforme | `ECHEC_ENTRAINEMENT`, modèle non servi | garde (`_lire_resultat`) : `test_lire_resultat_modele_non_conforme_refuse` (un cas sain, six artefacts : CE3-18) |
| plafond de dollars d'une génération, d'une ronde ou d'une course | appels refusés (`PLAFOND`), course arrêtée | garde du noyau (réservation au pire cas) : `test_appels_paralleles_plafond_tenu_au_pire_cas` ; `_doit_arreter` : `test_ce312_doit_arreter_et_raison_juste` (CE3-12 : arrêt sur plafond total pendant la conception, avec la raison juste) |
| crédit d'un fournisseur épuisé (HTTP 402) en cours de course | génération `CREDIT_EPUISE` invalidée, course arrêtée, aucune relance | garde du noyau (CE3-05) : `test_ce305_credit_epuise_arrete_la_course` |
| modèle servi différent du modèle demandé (génération ou ronde) | génération invalidée (`MODELE_NON_CONFORME`), lignée arrêtée | garde du noyau : `test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee` |
| fichier `STOP` à la racine d'une course | la boucle s'arrête avant la génération (ou la ronde) suivante | garde du noyau : `test_fichier_stop_arrete_la_boucle` |
| lien symbolique, tube, socket ou fichier à plusieurs liens durs posé par l'organisme | jamais suivi ni ouvert par root ; écarté et consigné (`elements_ecartes`) | garde du noyau (R-372) : `test_fichiers_lecture_et_copie_sans_lien`, `test_depot_ne_suit_aucun_lien_de_l_organisme`, `test_organisme_poseur_de_liens_ne_voit_rien_du_noyau` |
| organisme qui crée `noyau/` ou `corpus/` dans son dossier, ou tente de renommer les dossiers du noyau | écarté, non archivé ; dossiers du noyau intacts (hors de son dossier) | garde du noyau (CE3-07) : `test_ce307_dossiers_du_noyau_hors_du_travail_et_non_falsifiables` |
| journal des appels absent après des appels servis | génération `ANOMALIE_NOYAU` invalidée | garde du noyau (CE3-07) : `test_ce307_anomalie_journal_absent` |
| vue d'une lignée lisible par une autre lignée ou une autre course | impossible par les droits (0750, groupe de la lignée ; `archive_vue/` 0711 ; utilisateurs distincts par course) | garde du noyau (CE3-06) : `test_ce306_vue_lisible_par_la_seule_lignee_et_uid_par_course` |
| requête de recherche ou document qui recoupe une tâche de test | `REFUSE_FUITE`, consigné ; audit à la lecture | garde du noyau (CE3-04) : `test_garde_fuite_empreintes_et_recoupement`, `test_recherche_refuse_une_requete_qui_copie_une_tache_de_test`, `test_telechargeur_met_en_quarantaine_un_document_contenant_une_tache_de_test` |
| vivier sans compagnon conforme, malformé, servi sans phase de conception ou avec `--depuis` | course refusée | garde du noyau : `test_vivier_gardes_compagnon_format_et_recoupement`, `test_vivier_de_conception_servi_en_conception_seulement` |
| téléchargement hors provenance, http, hôte interdit pour la référence initiale ; plafonds ; source inconnue | `ECHEC_TELECHARGEMENT`, `PLAFOND`, `SOURCE_INCONNUE`, consignés | garde du noyau : `test_telechargeur_provenance_plafonds_et_extraction`, `test_moisson_de_bout_en_bout_en_simulation` |
| plus d'une paire sur quatre coupée | lecture « non concluant » | `lecture_h_g1`, `paires_h_g1` : `test_paires_h_g1_lues_dans_des_courses_appariees`, `test_h_g1_couverture_pannes_recoupements_et_trois_niveaux` |
| vue de l'archive contenant `juge/`, `journal-entrainements.jsonl` ou `modele.npz` | la paire touchée est invalidée (pas toute la lecture), audit | vérification humaine après la course : `find <espace>/archive_vue* \( -name juge -o -name journal-entrainements.jsonl -o -name modele.npz \)` doit être vide (CE3-07) |
| arrêt de l'hôte en cours de course | course arrêtée, consignée ; paires lues à la dernière génération valide commune ou coupées ; aucune relance | règle gelée (Plan, point 3) ; `<course>.fin.json` absent : constaté au journal du lanceur |
| clé ou identifiant d'espace de travail dans une sortie versée | versement refusé | vérification humaine (recherche des formes de clés) et garde de la copie expurgée (`scripts/depot_expurge.py`) |

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf, le 24 octobre 2026 de 18:32 à 19:02 UTC. Brouillon relu :
  `brouillon-gradient-etape1-sondes-v1.md` `2b6e5dcb81dc081e20431a092f982ef373960d1317e4c407528cadf5a5ae6f7c`. Rapport :
  `contre-lecture-preenregistrement-gradient-etape1-v1.md` `2efeb8db86a9005c9e743d17a90f366830cb67adfe8d834f23dd1b30eb092d3a`.
  Verdict : non scellable en l'état ; 5 bloquantes, 7 majeures, 5 mineures, 3 de forme ; traitement : table de la v3
  (`41feda40…`), inchangé.
- **Contre-lecture 2** — sous-agent neuf, sur la v2 `6ae4a8b367ccf6ac9de69e7c792971b8a1b3bab283ad49c549a95094dc8b1507`.
  Rapport : `contre-lecture-preenregistrement-gradient-etape1-v2.md` `c377b2e3645c5fd69781cf609c2db47c5f718815d0dbc7459a33b6d3404ccfbd`.
  Verdict : scellable après corrections ; 2 bloquantes, 1 majeure, 4 mineures, 2 de forme ; traitement : table de la v3,
  inchangé ; reste de CE2-03 et CE2-09 traité par CE3-01 et CE3-03 ci-dessous.
- **Contre-lecture 3** — sous-agent neuf, le 24 octobre 2026 de 20:21 à 21:12 UTC, sur la v3
  `41feda40a5f51858afd8c5167a4b86c3b495ec059929c6ff1f8aa59c8ad1b2d5`. Rapport :
  `contre-lecture-preenregistrement-gradient-etape1-v3.md` `76f96658ed1ebb5fb34ea002fb1edf87dd1551b8ffc74ad3eb67d374c7b5cdb8`.
  Verdict : scellable après corrections ; 2 bloquantes, 6 majeures, 7 mineures, 3 de forme. Traitement :

| remarque | traitement |
|---|---|
| CE3-01 mémoire de conception servie au seul bras A | accepté, code de « conv-audit » (`9d53ae3`, dans `ed3ce0e`) : B importe les rondes de A (historique, vue) ; essai `test_bras_apparie_voit_les_rondes_de_conception_de_l_origine` ; texte : Hypothèse, Métrique |
| CE3-02 rondes comptées comme générations notées | accepté, code (`669def0`, `5e6876d`) : `generations_valides` écarte phase, import, invalidé ; `reponses_finales` lève une erreur ; essais `test_paires_h_g1_ecartent_les_rondes_de_conception`, `test_h_g1_couverture_pannes_recoupements_et_trois_niveaux` |
| CE3-03 audit sur absence de réponses ; pas de sortie | accepté, code (`5e6876d`) : couverture ≥ 80 % (paire coupée), seuil bas sur les tâches répondues, sortie gelée (`apres_audit`) ; lignées imposées : sans objet ; texte : table et sortie de l'audit |
| CE3-04 recherche de provenance des textes de test | décision (c) de Lazar : garde et mesure ; code (`a8e9ce2`, `5e6876d`) ; Plan, point 11 ; trois essais |
| CE3-05 conditions extérieures non appariées | accepté : code (`c02bae3`, `5e6876d`) — HTTP 402 arrête la course, sources et présence de Brave au manifeste, bras B refusé si elles diffèrent, paire coupée sur panne extérieure > 10 points ; lanceur : même présence de Brave exigée ; texte : Métrique ; lancer B dès les g000 de A (suggestion 4) : non retenu (B part quand A est finie, verrou), l'écart d'heure est dit et mesuré |
| CE3-06 vues lisibles hors de la lignée et de la course | accepté : code (`7887f1d`) — vues 0750 au groupe de la lignée, `archive_vue/` 0711, `--decalage-uid` par course ; lanceur : dossier des courses à root en 0700, entrées 0700, sorties 0600 ; essais du noyau et du lanceur |
| CE3-07 dossiers du noyau renommables | accepté : code (`7887f1d`) — `<travail>.noyau` et `<travail>.corpus` hors du dossier de l'organisme, noms réservés, journal absent = `ANOMALIE_NOYAU` ; texte : la ligne « vue de l'archive contenant … » invalide la paire touchée |
| CE3-08 `--strip-components=3` | accepté : lanceur v2, `--strip-components=2` ; essai du lanceur |
| CE3-09 lanceur sans empreinte, en-tête périmé, graine absente | accepté : lanceur v2 cité avec son empreinte ; en-tête juste ; graine absente : code 2 avec note (essai) ; addendum pour tout changement |
| CE3-10 lignées imposées en conception | sans objet : plus de lignées imposées (R-370) |
| CE3-11 temps, interruption, moisson, contention | accepté : durées au pire (Plan, point 4) ; règle d'arrêt de l'hôte ; garde de temps étendue à la moisson (`c02bae3`, essai) ; cœurs et `DELAI_DEPASSE` rapportés |
| CE3-12 garde de plafond pendant la conception | accepté : `_doit_arreter` sert les deux boucles, raison juste (`c02bae3`, essai) ; ligne de la liste d'arrêt réécrite |
| CE3-13 répétition qui lit les scores ; Gemini non exercé | accepté : sortie scellée non lue, statuts par l'extrait mécanique sans score (`cf67025`) ; Opus et Argon à la répétition, appel de contrôle des deux |
| CE3-14 sections de « conv-audit » contradictoires | accepté : Plan, point 9 (ce qui prime, ce qui vaut, phrase sur l'injection nuancée) |
| CE3-15 clé Brave, requêtes web, consignation | accepté : R-363 cité ; borne des requêtes (Plan, point 4) ; consignation exigée par le lanceur |
| CE3-16 graines : entrée et format | accepté : entrée 4, format littéral hors bloc de code |
| CE3-17 ronde k et génération k : mêmes graines | accepté, code (`b7374a9`) : phase dans la clé (`DECALAGE_CONCEPTION`) ; vérifié par `test_vivier_de_conception_servi_en_conception_seulement` |
| CE3-18 menues inexactitudes | accepté : alignement sur la confrontation retiré (bornes propres) ; « six artefacts » ; 429 sans pièce mesurée, dit ; phrase de 20:42 ; « condition mécanique rapportée » ; borne sans déclaration déduite ; manifeste des sources (`c02bae3`) ; redirections : texte (Plan, point 9) ; `fin_conception.json` lu borné (`4967734`) |

- **Relecture de « conv-audit »** (message n° 20, remarques, pas une contre-lecture R2) : RE-01 = CE3-01 ; RE-02 hôte et
  arrêt de l'hôte : Plan, point 3 ; RE-03 N-026 : Hypothèse, H-G2 ; RE-04 B après A : Métrique ; RE-05 en-tête du lanceur :
  lanceur v2.
- **Revérification du code (R2, demandée par la contre-lecture 3)** — sous-agent neuf, sur le commit `5e6876d` (corrections
  CE3-01 à CE3-18 du code et faille des liens symboliques). Rapport : <<REVERIFICATION_RAPPORT>> ; verdict et traitement :
  <<REVERIFICATION_TRAITEMENT>>. Les commits suivants (`b7374a9`, `ed3ce0e`) sont relus par la contre-lecture 4.
- **Contre-lecture 4** — sous-agent neuf, sur cette v4 (texte, diff du code de `5e6876d` à `ed3ce0e`, lanceur v2) ; son
  rapport, l'entropie E (Plan d'analyse, point 5) et les graines sont inscrits ici au scellement.

## Annexe — ordre de grandeur de la dépense (informatif, non opposable, R7)

GO-2026-10-24-05 : coût accepté par Lazar sans devis. Bornes techniques : 2 × 360 + 2 × 190 = 1 100 USD au pire cas
(réservé au pire cas par le noyau), plus 25 USD de répétition et moins de 1 USD d'appels de contrôle ; attendu de l'ordre
de 200 à 250 USD (estimation illustrative de « conv-audit », message n° 22 § 3 : le bras A répond surtout par ses sondes,
le bras B par texte). Aucune carte n'est louée pour cette étape (l'extraction des traits est faite : R-360).
