# Préenregistrement — étape 1 du programme « gradient conçu par l'essaim » : sondes apprises par gradient — v3

Version 3, écrite par la lignée « session-depot » sur le brouillon v1 de « conv-audit » (conception gardée) : la v2 traitait
les vingt remarques de la contre-lecture R2 n° 1, sur l'ordre de Lazar : « execute les R1 R2 » (R-356) ; la v3 y ajoute
la phase de conception et la moisson, sur sa décision du 24 octobre à 21:06 (heure de Paris), relayée par « conv-audit » :
« oui oui il doit inclure la phase de conception et la moisson avant scellement » (R-363), avec les sections écrites par
« conv-audit » (`prereg/sections-conception-moisson-v1.md`, `180a39afdf5390151ce7d418f83037d6a0cc5b07f3f2c5245694f97c24e9454d`),
et les bornes de génération et de ronde alignées sur le brouillon v6 de la confrontation (`0ce8c396…`). La
dépense de l'étape 1 est couverte par GO-2026-10-24-05, sans devis (R-355). Aucune lecture de résultat avant le
scellement (R1) ; aucun run visant un signe (R3) ; symétrie de l'audit (R4). Rien d'opposable avant le verdict (R7).

- Auteur : lignée « session-depot » (session Claude Code du dépôt), sur le brouillon v1 de la lignée « conv-audit ».
  Conflit d'intérêts déclaré : la même lignée a écrit la v2 de l'extraction, les corrections du noyau et ce texte, et
  lancera les courses.
- Date (UTC) : 2026-10-24, 20:20 (dernière modification, heure lue par `date -u`).
- Commit du code d'analyse : branche `outils/essaim-m3-gradient-v2-travail`, commit `4f02bd8a28fbc9747ff9e19f4ae4db6c24e04baa`
  (fusion `e75e726` de la branche de « conv-audit » `outils/essaim-m3-gradient-v1-travail` à `162da90` — phase de
  conception, moisson, banque scellée, vues — et des corrections de « session-depot » : CE-02, CE-06, CE-07, analyse de
  H-G1 ; puis CE2-03, CE2-04, CE2-09 ; 85 tests passent, 2 désélectionnés parce qu'ils exécutent l'organisme
  `gemini-v2`) ; `essaim_m3/analyse_gradient.py` `2e59ace67f821e7f35c917553884d9292b6a0031fcb95b4272bbbb4b6b8d221d`,
  `essaim_m3/noyau/boucle.py` `34897572433ae39f86c71144a642d48d280d8a7084d24318b12b893952c19599`, `essaim_m3/analyse.py`
  `1cef7c0f1ecd5058fa913d779c07599900a6c9e485a3e8186f39b28d1014a87e`, `essaim_m3/noyau/entrainement.py`
  `954976004b43b4460013fde907cb6a9975f25bc93b8e8bbff45de7acd9102758`, `essaim_m3/noyau/moisson.py`
  `861cbb0d016df0a1d480971e634b7f53da107da82c37c7a2f65aad1bcb8ba9ca`. Les courses tournent sur ce même commit ; le lanceur
  (`docs/procedures/gradient-etape1-v1/lancer_courses_etape1_v1.sh`) vérifie `git rev-parse HEAD` et l'arbre propre avant
  tout appel payant.
- Documents qui font foi (chemin + empreinte) :
  - mission de Lazar, mot pour mot : `essaim-m3-refonte-v1/MISSION-v1.md` `bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e` ;
  - note du programme : `essaim-m3-refonte-v1/notes/programme-apprentissage-gradient-essaim-v1.md` `6b4151049ff9d279081fdb2876ff5894ae2388c22c96acd4558312015145d8bc` ;
  - brouillon v1 relu : `essaim-m3-refonte-v1/prereg/brouillon-gradient-etape1-sondes-v1.md` `2b6e5dcb81dc081e20431a092f982ef373960d1317e4c407528cadf5a5ae6f7c` ;
  - banque scellée `confrontation-v1` : `essaim-m3-refonte-v1/banque/banque-confrontation-v1.json` `f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc`
    (branche `outils/essaim-m3-refonte-v1-travail`, commit `bffe03c`) ;
  - traits : branche `donnees/traits-etape1-v1`, commit `6479769`, `essaim-m3-refonte-v1/traits/etape1-v1/EMPREINTES-traits-etape1-v1.txt`
    `add13e090a13b60e48983393ae376cc9df2542210b5328bc2abd94e661e25f17` ; manifeste servi `traits-16384/manifeste-traits.json`
    `034d846069b863e8160458b39db93ee889b297e35061afa5e0232487dd9f2edd` ; script `extraire_activations_v2.py`
    `8286f4e72740e88392e28a6a768bb502d593a3da1b9236c3f1917db14505beee` (branche `outils/traits-etape1-v1`, `5fa8d8e`) ;
  - collisionneur v2.5 (appelants et table des prix du noyau) : `collisionneur-v2.5-banc-jev-travail/collisionneur_v2.py`
    `213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd` ;
  - décisions de Lazar : `registres/decisions.md` R-344 (étape 1 ; « run décisif exigé », confirmé à 18:39, heure de
    Paris), R-351 (clés), R-355 (GO sans devis), R-356 (R1 et R2) ; `registres/go.md` GO-2026-10-24-04 et GO-2026-10-24-05.

## Hypothèse

Programme « gradient conçu par l'essaim », étape 1 (N-042, R-344) : des organismes écrits par des modèles conçoivent
eux-mêmes l'apprentissage par gradient de sondes sur les activations de Llama-3.1-8B-Instruct (données, objectif,
algorithme, vue), sous le noyau fixe, et s'en servent pour classer des tâches à vérité cachée.

- **H-G1 (principale).** Sur le test final caché de la banque `confrontation-v1`, une lignée auto-écrite à qui le noyau
  sert l'entraînement de sondes (bras « avec gradient », `entrainements_max` = 10, traits servis) atteint une exactitude
  équilibrée plus haute que la même lignée relancée depuis les mêmes organismes de génération 0, sans entraînement (bras
  « sans gradient », `entrainements_max` = 0), toutes choses égales par ailleurs : mêmes organismes g000, même banque,
  même graine d'ordre, mêmes budgets d'appels, de dollars, de temps et de recherches.
- **H-G0 (mécanique, condition de lecture).** Dans le bras avec gradient, chaque lignée auto-écrite qui demande un
  entraînement obtient un modèle (`statut` OK) et des prédictions ; chaque génération répond à au moins 80 % des tâches
  de test ; aucun entraînement n'a reçu une tâche de test (refus journalisé sinon).
- **H-G2 (descriptive, sans seuil).** Les objectifs écrits par les organismes (texte, empreinte), leurs vues et leurs
  sondes sont rapportés avec leur exactitude ; comparaison descriptive à des sondes témoins entraînées après la course,
  avec les mêmes données d'entraînement, sur chacune des dix vues (Plan d'analyse, point 7).
- **H-G3 (descriptive, sans signe prédit).** Les changements de spécification d'une génération à l'autre (objectif,
  algorithme, vue, données) et leur effet sur le score de développement sont rapportés.

- **H-C (descriptive, sans seuil) : phase de conception et moisson.** Avant la génération 0 notée, chaque lignée du bras
  avec gradient tourne en rondes de conception (au plus 8) : budget de ronde, tâches d'entraînement avec vérité, aucune
  tâche de test, aucun score ; l'organisme conçoit lui-même son critère d'arrêt et le déclare (`fin_conception.json`) ;
  il écrit son moissonneur avec les primitives `rechercher` et `telecharger` du noyau (Lazar, 20:32 à 20:46, heure de
  Paris : « ne lui suggère rien »). Rapporté par lignée : rondes utilisées, ronde de déclaration, contenu de
  `fin_conception.json`, dépense, documents moissonnés par source. Aucune hypothèse n'y est testée.

Hypothèses de travail : les deux lignées imposées (organisme écrit par Gemini, corrigé, v3 ; enveloppe v3 de l'essaim de
Gemini) ont été écrites avant le contrat v3 et n'appellent pas `entrainer` ; elles tournent dans les deux bras (« étape 1
toutes les lignées », Lazar, R-344) mais n'entrent pas dans H-G1 (Plan d'analyse, point 2).

## Prédiction chiffrée et signe attendu

- **H-G1** : signe attendu **positif** ; ordre de grandeur prédit **Δ ≥ +0,10** d'exactitude équilibrée (moyenne des
  paires). Réfutation : la borne haute de l'intervalle à 95 % est sous +0,10 (l'effet prédit est exclu) ; si la borne
  basse est en outre au-dessus de 0, la lecture le dit (« effet positif plus petit que prédit »). Lecture complète :
  section « Critères de lecture gelés ».
- **H-G0** : prédit vrai pour chaque lignée auto-écrite du bras avec gradient ; faux pour une lignée = cette lignée est
  rapportée « gradient non utilisé » ; elle reste dans H-G1 (le bras est défini par ce que le noyau sert, pas par ce que
  l'organisme fait).
- **H-G2, H-G3** : aucun signe prédit.

## Métrique

- **Score** : exactitude équilibrée par famille, (sensibilité + spécificité) / 2, moyenne des deux familles, sur les
  60 tâches du test final (36 « conscience d'évaluation », 18 + 18 ; 24 « contrôle de délégation », 12 + 12) ; une tâche
  sans réponse valide compte comme une erreur (règle du juge du noyau). Code : `analyse.exactitude_equilibree`.
- **Unité d'analyse** : la paire (lignée auto-écrite ℓ, réplique r), ℓ ∈ {claude-fable-5-1, claude-opus-5-5,
  gemini-argon}, r ∈ {1, 2} : **six paires** (noms de lignée formés par le noyau, `espece.lower().replace("_", "-")` ;
  `gemini-4-argon` est l'identifiant du modèle, pas le nom de la lignée : CE2-01). Une tâche n'est pas une unité. La génération 0 d'une lignée est
  l'organisme issu de sa phase de conception dans A_r ; B_r la relance telle quelle (mêmes empreintes, sans conception).
  Le bras B retire donc l'entraînement à un organisme conçu en l'ayant : H-G1 mesure ce que l'entraînement servi
  apporte à cet organisme, non ce qu'un organisme conçu sans lui aurait fait (dit avant la course). Ce qui reste
  différent entre les bras, en plus de l'entraînement (CE2-03) : les appels aux modèles ne sont pas déterministes (les
  réponses diffèrent même à code égal) ; les successeurs g1 et g2 sont réécrits par chaque organisme selon ce qu'il a lu
  (c'est l'effet du traitement, et non une variable contrôlée) ; le plafond d'une course est partagé entre ses lignées.
  L'ordre des lignées dans une ronde est, lui, le même dans les deux bras (base triée par nom, même graine de ronde ;
  code `4f02bd8`, essai `test_declencheurs_audit_h_g1_et_ordre_de_ronde_apparie`, qui échoue sans le tri) ; les graines
  d'ordre des tâches sont les mêmes ; les plafonds de course sont dimensionnés pour ne pas mordre (pire cas réservé, non
  attendu). Le bootstrap à deux niveaux, qui tire les paires, absorbe le bruit propre à chaque paire.
- **Statistique** : Δ(ℓ, r) = score(A_r, ℓ, g) − score(B_r, ℓ, g), où g est la génération lue : 2 (= G − 1), ou la
  dernière génération valide commune aux deux bras si l'un s'arrête avant ; H-G1 se lit sur la moyenne des Δ.
- **Intervalle** : bootstrap à deux niveaux — paires tirées avec remise, puis, pour chaque paire tirée, tâches du test
  final tirées avec remise par strate (famille, vérité), les mêmes pour les deux bras de la paire ; 2 000 tirages ;
  percentiles 2,5 et 97,5 ; graine dérivée par `numpy.random.SeedSequence` (Plan d'analyse, point 5). Code :
  `analyse_gradient.difference_h_g1`, `paires_h_g1`.
- **Lignées imposées** : la même statistique est calculée pour elles et rapportée à part, sans lecture.

## Seuil

- Effet prédit : +0,10 (`analyse_gradient.EFFET_PREDIT`). « Confirmé » exige à la fois la borne basse de l'intervalle à
  95 % au-dessus de 0 et Δ moyen ≥ +0,10 ; « réfuté » : borne haute sous +0,10.
- Une seule comparaison principale (H-G1) : aucune correction pour comparaisons multiples. H-G0 est une condition
  mécanique ; H-G2 et H-G3 sont descriptives.
- Taux d'erreur visés : « confirmé » à tort sous effet nul ≤ 5 % au niveau de l'intervalle bilatéral à 95 %. Estimation
  par simulation, avant toute course (non opposable, R7 : modèle de variance supposé — effet de paire N(0 ; 0,5) en
  logit, bruit de bras N(0 ; 0,25), base 0,65, test final de la banque —, `analyse_gradient.puissance_h_g1`, 200 jeux
  par cas, 400 tirages, `SeedSequence(20261025)` ; sortie `puissance-v1.json`
  `eaf4ea5deb0094e91d74cb5782cb441d6555afa38c5926563fef8606436ea0ba`) : six paires, effet nul → confirmé 0 %,
  réfuté 46,5 %, non concluant 53,5 % ; effet +0,10 → confirmé 44 %, non concluant 54,5 %, réfuté 1,5 % ; effet +0,20 →
  confirmé 98,5 %. Neuf paires ne changent presque rien (+0,10 → confirmé 49,5 %) : la largeur vient surtout des 60
  tâches du test final. La puissance à l'effet prédit est donc modeste ; c'est dit avant la course et ne change aucun
  seuil.

## Plan d'analyse

1. **Données.** Banque scellée `confrontation-v1` (`f1387a20…`) : entraînement 80 tâches (servies avec leurs vérités),
   test de développement 60 (score rendu à chaque génération), test final 60 (jamais rendu, lu une fois à la fin). Traits :
   `traits-16384` (sans troncature ; la plus longue tâche fait 12 407 jetons, 0 tâche tronquée), dix vues (couches 8, 12,
   16, 20, 24 × dernier jeton, moyenne), 200 tâches × 4 096, Llama-3.1-8B-Instruct, révision
   `0e9e39f249a16976918f6564b8830bc894c89659` (cliché téléchargé ; le champ `revision_resolue` du manifeste vaut `None`
   sous transformers 5.18.0), servies toutes (`--traits <dossier traits-16384>`, sans `--vues`) ; le chargement vérifie
   empreintes, compagnons, banque de la course, tâches et nombres finis. `traits-2048` n'est pas servi (CE-09).
2. **Lignées.** Trois auto-écrites, amorcées par `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`, `GEMINI_ARGON` sous le contrat v3
   (vues comprises) : elles seules entrent dans H-G1. Deux imposées, famille Gemini (N-040 (3)) :
   `gemini-organisme-v3` (branche `outils/gemini-organisme-v3`, `320cd34`, arbre `3e6fe2e96d6133ab0bfae39009133897d335966d25e5dd48832d6a5d88dc6ba7`)
   et `enveloppe-essaim-gemini-v3` (branche `outils/essaim-m3-debogage-v3`, `233fde6`, arbre
   `bceb133262e623212cff6151e33867b02899c652be36394845ec55b0279fae20`) ; rapportées à part.
3. **Courses.** Pour r ∈ {1, 2} : A_r, bras avec gradient,
   `python -m essaim_m3 lancer --reel --go GO-2026-10-24-05 --registre-go <extrait de registres/go.md> --taches <banque>
   --traits <traits-16384> --sortie <A_r> --generations 3 --graine <graine_r> --appels-max 160 --usd-par-generation 37
   --temps-max 2400 --recherches-max 30 --telechargements-max 20 --octets-max 40000000 --entrainements-max 10
   --pas-max 5000 --delai-entrainement 120 --rondes-conception-max 8 --usd-max-conception 10 --appels-max-conception 160
   --parallele-max 8 --relances-max 1 --isoler-reseau --plafond-total 1066
   --organisme-impose gemini-organisme-v3=<…>/organisme@gemini --organisme-impose enveloppe-essaim-gemini-v3=<…>/organisme@gemini` ;
   puis B_r, bras sans gradient, `--depuis <A_r>` (mêmes organismes g000, ceux issus de la conception de A_r, même
   banque, aucun amorçage, aucune conception ; CE-06) avec `--entrainements-max 0 --plafond-total 555`, **sans** les deux
   `--organisme-impose` (les lignées imposées reviennent par `--depuis`, mêmes empreintes ; le noyau refuse un nom donné
   deux fois : CE2-02) et sans `--rondes-conception-max`, tout le reste identique (moisson et `--traits` compris : avec
   `--entrainements-max 0`, `traits.disponibles` est faux), même `--graine <graine_r>`. A_1 et A_2 tournent
   ensemble ; B_1 et B_2 ensuite. Clés (GO-2026-10-24-04) : `ANTHROPIC_API_KEY` = valeur de `RR_ANTHROPIC_API_KEY` pour
   le seul processus, en-tête d'espace de travail par `ANTHROPIC_CUSTOM_HEADERS` (valeur de `RR_ANTHROPIC_WORKSPACE_ID`,
   jamais écrite), `ANTHROPIC_BASE_URL` absente (le noyau refuse le mode réel si elle est définie), `GEMINI_API_KEY`,
   `BRAVE_API_KEY` si elle est dans l'environnement de la session (source `web` de la moisson, lue par le noyau seul) ;
   avant chaque course, un appel de contrôle par espèce (statut `OK` exigé, sinon la course ne part pas : liste d'arrêt) ;
   environnement Python dans un chemin traversable par
   les utilisateurs des organismes (`/opt/essaim-m3-venv-v1` : numpy 2.4.6, anthropic 2.3.0) ; noyau en root (isolation
   d'utilisateur), réseau des organismes et de l'entraîneur coupé.
4. **Budgets (CE-07), alignés sur la v6 de la confrontation.** Génération notée : 160 appels (120 tâches de test + 40),
   37 USD (assez pour 160 appels au pire cas de la réservation du noyau, `max_tokens` 4 096, aux prix Fable et Argon de la
   table du collisionneur : calcul de la v6, CR2-02), 2 400 s, 30 recherches, 20 téléchargements, 40 Mo, 10
   entraînements de ≤ 5 000 pas et ≤ 120 s chacun (10 × 120 + 300 = 1 500 s ≤ 2 400 s : garde du noyau en réel). Ronde de
   conception : 160 appels, 10 USD, même temps et même moisson. Plafonds par course : A_r 1 066 USD (3 amorçages × 37 +
   8 rondes × 5 lignées × 10 + 5 lignées × 3 générations × 37), B_r 555 USD (5 × 3 × 37).
5. **Graines (R9).** Entropie E tirée au scellement (`secrets.randbits(128)`) et inscrite dans la section « Contre-lecture »,
   entrée 2 ; `SeedSequence(E).spawn(3)` → `graine_1`, `graine_2` (entier de `generate_state(1, uint64)`, passé à
   `--graine` ; le noyau en dérive les graines d'ordre par lignée, génération et usage) et `entropie_analyse` (bootstrap).
   La graine de la descente de gradient d'une sonde est un choix de l'organisme, journalisé par l'empreinte de sa
   spécification (`sha256_spec`) ; elle n'est pas une graine expérimentale (CE-15).
6. **Lecture de H-G1** (une fois, après la fin des quatre courses) : `paires_h_g1([(A_1, B_1), (A_2, B_2)],
   ["claude-fable-5-1", "claude-opus-5-5", "gemini-argon"], generations=3)`, puis `difference_h_g1(..., entropie_analyse,
   2 000)`, puis `lecture_h_g1` avec `invalide` (rendu par `paires_h_g1`) et `audit` = au moins un fait rendu par
   `declencheurs_audit_h_g1` (CE2-09), calculé sur `exactitude_par_famille` de chaque lignée (auto-écrite et imposée),
   dans chaque bras et chaque réplique, à la génération lue, sur les sondes témoins (point 7) et sur les Δ par paire
   (`par_paire`) ; un sous-agent neuf rejoue ces trois appels (R13). Les Δ des lignées imposées sont calculés par les mêmes fonctions et
   rapportés sans lecture. Rapport scellé ; verdict par un sous-agent neuf (R13) si l'étape sert de porte à l'étape 2.
7. **H-G2 (descriptive).** Après les courses, pour chaque vue : deux sondes témoins entraînées par l'entraîneur du noyau
   (isolé), sur les 80 tâches d'entraînement, sonde linéaire normalisée, 1 000 pas, taux 2, l2 0,001, lot 80, graine 0,
   objectif de Brier et objectif logarithmique borné (p tronqué à [0,001 ; 0,999]) ; exactitude équilibrée sur le test
   final, rapportée. Référence de surface : `banque.reference_traits_texte` (0,69 et 0,50 rapportés par « conv-audit »,
   non audités) ; la sonde « longueur seule » du brouillon v1 est retirée (CE-16). Le script de ces témoins est écrit et
   scellé (addendum) avant d'être lancé (CE-17).
8. **Répétition mécanique** avant les courses décisives, après le scellement : une course réelle minimale (une lignée
   `CLAUDE_OPUS_5_5`, deux rondes de conception au plus à 2 USD, une génération à 3 USD, 20 appels, 900 s, 2
   entraînements, moisson comme ci-dessus, plafond 10 USD), exclue de toute analyse ; seuls ses statuts sont lus
   (amorçage, rondes, exécution, appels conformes, entraînements, moisson, isolation) ; aucun score. Si elle révèle un
   défaut de code, la correction passe par un addendum scellé et contre-lu avant les courses.
9. **Phase de conception et moisson** (sections A et B de `prereg/sections-conception-moisson-v1.md`, insérées ici telles
   quelles pour le noyau, la provenance, le scellement et la lecture) : rondes `cNNN` archivées, scellées, vues de la
   seule lignée, jamais notées ; à la ronde 8, le successeur devient la génération 0, fin déclarée ou non (consigné) ;
   sources `arxiv`, `openalex`, `semanticscholar`, `web` (si la clé existe) ; téléchargements sous provenance, documents
   ≤ 8 Mo, texte rendu ≤ 60 000 caractères, corpus et index scellés par génération ou ronde, visibles de la lignée seule ;
   texte moissonné rendu comme donnée ; rien de moissonné n'entre dans la banque (scellée avant). Débit : OpenAlex
   répond 429 depuis l'adresse partagée (mesuré le 24 octobre entre 19:40 et 19:46 UTC) ; un `ECHEC_RECHERCHE` est un statut rendu à
   l'organisme.

## Critères de lecture gelés

Table de H-G1 (`analyse_gradient.lecture_h_g1`), lue de haut en bas ; la première ligne vraie s'applique.

| condition | verdict |
|---|---|
| audit de symétrie déclenché (ci-dessous) | « audit de symétrie (R4) avant toute lecture » ; la lecture attend le rapport d'audit |
| plus d'une paire sur quatre coupée (aucune génération valide commune) ou invalidée par le noyau | « non concluant : plus d'une paire sur quatre coupée ou invalidée » |
| aucune paire | « non concluant : aucune paire » |
| borne basse > 0 et Δ moyen ≥ +0,10 | « confirmé » |
| borne haute < +0,10 | « réfuté (l'effet prédit est exclu) », avec « effet positif plus petit que prédit » si la borne basse > 0 |
| sinon | « non concluant ; aucune relance sans nouveau préenregistrement » |

- **Audit de symétrie (R4)**, déclenché par l'un de ces faits, qu'il aille dans le sens de la prédiction ou contre elle :
  une lignée (auto-écrite ou imposée, l'un ou l'autre bras) au-dessus de 0,95 ou au-dessous de 0,30 sur une famille du
  test final ; une sonde témoin au-dessus de 0,95 sur le test final ; Δ d'une paire au-dessus de +0,40 ou au-dessous de
  −0,40. L'audit cherche une fuite (vérités lisibles, vue de l'archive), des étiquettes inversées, un indice de surface.
- **H-G0** : vrai ou faux par lignée, rapporté ; ne change pas la table de H-G1.
- **Lignées imposées** : Δ rapportés, aucune lecture.
- Aucune relance d'une course après lecture. Une course arrêtée par une garde avant sa fin est rapportée telle quelle ;
  ses paires sont lues à la dernière génération valide commune, ou coupées.

## Liste d'arrêt

Chaque ligne dit si c'est une garde automatique (avec son essai sain et artefact, R5) ou une vérification humaine.

| condition | effet | garde ou vérification |
|---|---|---|
| GO absent, sans type « calcul », ou collisionneur d'empreinte inattendue | course refusée avant tout appel | garde du noyau (CR-13) ; essais de « conv-audit » |
| noyau non root, ou isolation réseau indisponible | course refusée | garde du noyau (CR-01, CR-02) ; essais `test_organisme_fuite_…` |
| entraîneur sans isolation d'utilisateur en réel | aucun entraînement (Arret) | garde codée (CE-02) ; non atteignable en root, où l'isolation existe ; essai de l'isolation : `test_entraineur_isole_ne_lit_pas_les_fichiers_du_noyau` (sain : le fichier 0600 n'est pas lu ; artefact : lu sans isolation) |
| traits : fichier altéré, compagnon absent, banque d'une autre course, tâche sans traits, nombre non fini, traits factices, vue demandée absente | course refusée au départ | garde (`cli.charger_traits`) ; `test_charger_traits_dossier_d_extraction_sain_et_artefacts` |
| budget incohérent (temps de génération < entraînements × délai + 300 s) | course refusée | garde (CE-07) ; `test_budget_incoherent_refuse_en_reel` |
| bras sans gradient sur une autre banque que sa course d'origine | course refusée | garde (`cli.lancer`, CE-06) ; essai du bras apparié : `test_bras_apparie_adaptatif_memes_g000_avec_memoire` |
| entraînement qui désigne une tâche de test, objectif refusé, plafond d'entraînements | `REFUSE` ou `PLAFOND`, journalisé | garde (`Entraineur.valider`) ; `test_entraineur_sonde_sain_et_artefacts` |
| résultat d'entraînement ou modèle non conforme (formes, nombres non finis, objet Python, clé en trop, courbe) | `ECHEC_ENTRAINEMENT`, modèle non servi | garde (`_lire_resultat`) ; `test_lire_resultat_modele_non_conforme_refuse` (sain et cinq artefacts) |
| plafond de dollars d'une génération ou d'une course | appels refusés (`PLAFOND`), course arrêtée | garde du noyau (réservation au pire cas) ; essais `test_appels_paralleles_plafond_tenu_au_pire_cas` |
| modèle servi différent du modèle demandé | génération invalidée (`MODELE_NON_CONFORME`) | garde du noyau ; essais de « conv-audit » |
| fichier `STOP` à la racine d'une course | la boucle s'arrête avant la génération (ou la ronde) suivante | garde du noyau |
| appel de contrôle d'une espèce en échec avant une course (crédit, clé, en-tête d'espace de travail, réseau, modèle servi) | la course ne part pas | garde du lanceur (`lancer_courses_etape1_v1.sh`, § 5 bis), qui passe par le même client que les courses : un statut `OK` d'Anthropic prouve que la clé et l'en-tête d'espace de travail lu par le SDK depuis `ANTHROPIC_CUSTOM_HEADERS` sont acceptés (CE2-05) ; répétition mécanique ; vérification humaine du journal (modèle servi) |
| `ANTHROPIC_BASE_URL` définie en réel | course refusée | garde du noyau (`cli.lancer`) |
| plafond total atteint pendant la phase de conception | `arret_conception`, course arrêtée avant toute génération notée | garde du noyau ; `test_phase_de_conception_a_critere_d_arret_de_l_organisme` |
| modèle non conforme pendant une ronde | lignée arrêtée (`INVALIDE_MODELE`) | garde du noyau (CR-02) |
| téléchargement hors provenance, http, hôte interdit ; plafonds de documents, d'octets, de taille ; source inconnue | `ECHEC_TELECHARGEMENT`, `PLAFOND`, `SOURCE_INCONNUE`, consignés | garde du noyau ; `test_telechargeur_provenance_plafonds_et_extraction`, `test_moisson_de_bout_en_bout_en_simulation` |
| plus d'une paire sur quatre coupée | lecture « non concluant » | `lecture_h_g1` ; `test_paires_h_g1_lues_dans_des_courses_appariees` |
| vue de l'archive contenant `juge/`, `journal-entrainements.jsonl` ou `modele.npz` | lecture invalidée, audit | vérification humaine après la course : `find <espace>/archive_vue* \( -name juge -o -name journal-entrainements.jsonl -o -name modele.npz \)` doit être vide |
| clé ou identifiant d'espace de travail dans une sortie versée | versement refusé | vérification humaine (recherche des formes de clés) et garde de la copie expurgée (`scripts/depot_expurge.py`) |

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf (lignée de contre-lecture R2, ni « conv-audit » ni « session-depot »), le
  24 octobre 2026 de 18:32 à 19:02 UTC. Brouillon relu : `brouillon-gradient-etape1-sondes-v1.md`
  `2b6e5dcb81dc081e20431a092f982ef373960d1317e4c407528cadf5a5ae6f7c`. Rapport :
  `contre-lecture-preenregistrement-gradient-etape1-v1.md` `2efeb8db86a9005c9e743d17a90f366830cb67adfe8d834f23dd1b30eb092d3a`.
  Verdict : non scellable en l'état ; 5 bloquantes, 7 majeures, 5 mineures, 3 de forme. Traitement :

| remarque | traitement |
|---|---|
| CE-01 validateur | accepté : huit sections canoniques du gabarit |
| CE-02 entraîneur non isolé | accepté, code : utilisateur non privilégié propre à l'entraîneur, dossier neuf (entrées seules), espaces de noms neufs, réseau coupé, résultat et modèle relus comme données non fiables ; refus en réel sans isolation (`03f7caf`) ; essai sain et artefact |
| CE-03 bootstrap par tâche | accepté : bootstrap à deux niveaux, unité = paire (`analyse_gradient`, `49f1a16`) ; contrôle positif |
| CE-04 vues non codées | accepté, code (`9a3b937`) : vues servies, `spec["vue"]`, chargement vérifié, essais |
| CE-05 table et règle | accepté : table gelée ci-dessus ; confirmé = borne basse > 0 et Δ ≥ +0,10 |
| CE-06 appariement | accepté, code : `--depuis` sans `--gel` (bras apparié adaptatif), même banque exigée (`03f7caf`) |
| CE-07 budget | accepté : 2 400 s pour 10 × 120 s + 300 ; garde en réel ; dollars et appels relevés pour ne pas lier |
| CE-08 lignées | accepté : `gemini-organisme-v3` et l'enveloppe v3, empreintes d'arbre ; imposées hors de H-G1, rapportées |
| CE-09 troncature | accepté : `traits-16384`, aucune tâche tronquée ; troncatures consignées par la v2 du script |
| CE-10 révision | accepté : révision explicite, versions et carte au manifeste (`extraire_activations_v2.py`) |
| CE-11 empreintes | accepté : banque, traits, script, code et commit inscrits |
| CE-12 liste d'arrêt | accepté : chaque ligne nomme sa garde et son essai, ou la vérification humaine |
| CE-13 « à confirmer » | accepté : confirmé par Lazar à 18:39, heure de Paris (R-344) |
| CE-14 métrique | accepté : métrique unique de H-G1 sur le test final ; H-G2, H-G3 sans seuil |
| CE-15 graine de la sonde | accepté : choix de l'organisme, journalisé ; distinct des graines expérimentales |
| CE-16 sonde « longueur seule » | accepté : retirée ; référence de surface `reference_traits_texte` |
| CE-17 sondes témoins | accepté : descriptives, après la course, script scellé avant son lancement |
| CE-18 titres | accepté (CE-01) |
| CE-19 empreintes de la section | accepté : ci-dessus |
| CE-20 devis | accepté : GO sans devis (R-355) ; annexe informative seulement |

- **Contre-lecture 2** — sous-agent neuf (ni « conv-audit », ni « session-depot », ni le premier relecteur), sur la v2.
  Texte relu : `gradient-etape1-sondes-v2.md` `6ae4a8b367ccf6ac9de69e7c792971b8a1b3bab283ad49c549a95094dc8b1507`.
  Rapport : `contre-lecture-preenregistrement-gradient-etape1-v2.md` `c377b2e3645c5fd69781cf609c2db47c5f718815d0dbc7459a33b6d3404ccfbd`.
  Verdict : scellable après corrections ; 2 bloquantes, 1 majeure, 4 mineures, 2 de forme ; CE-01 à CE-20 traitées (20 sur
  20) ; validateur : seules les empreintes de cette entrée manquaient ; puissance rejouée à l'identique. Traitement :

| remarque | traitement |
|---|---|
| CE2-01 nom de la lignée Gemini auto-écrite | accepté : `gemini-argon` (Métrique, Plan point 6) |
| CE2-02 commande du bras B refusée | accepté : B_r sans les deux `--organisme-impose` (Plan point 3) ; le lanceur ne les passe pas |
| CE2-03 « toutes choses égales » | accepté : différences nommées (Métrique) ; ordre de ronde rendu identique dans le code (`4f02bd8`), essai sensible |
| CE2-04 artefact de `_lire_resultat` | accepté : `test_lire_resultat_modele_non_conforme_refuse` |
| CE2-05 en-tête d'espace de travail | accepté : appel de contrôle par espèce avant chaque course, même client ; répétition mécanique |
| CE2-06 `revision_resolue` vide | accepté : divulgation gardée ; traits figés par leurs empreintes |
| CE2-07 script des sondes témoins | accepté : addendum scellé avant leur lancement, avec l'empreinte du script |
| CE2-08 empreintes de l'entrée 2 | accepté : ci-dessus |
| CE2-09 déclencheurs d'audit | accepté : `declencheurs_audit_h_g1` (une fonction, essai sain et artefacts), Plan point 6 |
- **Contre-lecture 3** — sous-agent neuf, sur cette v3 ; son rapport, l'entropie E (Plan d'analyse, point 5) et les
  graines sont inscrits ici au scellement.

## Annexe — ordre de grandeur de la dépense (informatif, non opposable, R7)

GO-2026-10-24-05 : coût accepté par Lazar sans devis. Bornes techniques : 2 × 1 066 + 2 × 555 = 3 242 USD au pire cas
(réservé au pire cas par le noyau), plus 10 USD de répétition et moins de 1 USD d'appels de contrôle ; attendu de l'ordre
de 700 USD (à titre illustratif, ordre de grandeur de la v6 : environ 7 USD par génération et 3 USD par ronde). Aucune
carte n'est louée pour cette étape (l'extraction est faite : R-360).
