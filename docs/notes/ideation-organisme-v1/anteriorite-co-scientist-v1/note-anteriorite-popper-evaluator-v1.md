# Antériorité de POPPER, d'E-valuator et des juges éprouvés par optimisation adaptative, pour l'organisme d'idéation — vérification sur pièce, v1

Écrit par un sous-agent neuf (Opus 5.5) pour la session mère, le 9 novembre 2026, de 09:32 à 10:02 UTC environ
(`date -u`). Suite de la note `note-anteriorite-co-scientist-v1.md` (`08a3738a…`), § 7, points 1 à 3 ; décisions de Lazar
R-1990 (a) et R-1992. Aucun fichier existant modifié ; aucune inscription, aucune clé, aucun appel de modèle payant ; rien
n'est commité. L'organisme public (`/home/user/ideation-organism`, commit `f39a7f4`) est lu, pas modifié.

**Convention de page.** « POPPER p. 6 » : page 6 du PDF des actes de l'International Conference on Machine Learning 2025
(PMLR 267, 66 pages) ; « POPPER v1 p. 5 » : page 5 de la prépublication arXiv 2502.09858 v1. Les autres pièces sont
citées à la page de leur PDF. Pour toutes les pages citées, le numéro imprimé égale le numéro de page du PDF (contrôle par
programme, provenance § 4). Les citations anglaises sont recopiées mot pour mot ; « … » marque une coupure. Un contrôle par
programme les a retrouvées dans l'extraction « ordre de lecture » de la page citée (§ 10).

**Statut des chiffres (R7).** Tout chiffre attribué à une pièce est lu dans son PDF empreinté, à la page citée, dans le
texte, un tableau ou une légende ; aucune figure n'a été relue en image. Les chiffres et énoncés de l'organisme viennent de
son README public (commit `f39a7f4`) et de la note Co-Scientist, non revérifiés sur leurs sorties.

**Pièces, empreintes et extractions** : `docs/sources/pdf/provenance-anteriorite-popper-evaluator-v1.md`
(`65024480f561068f…`), qui donne adresses, codes de réponse, heures, licences et commandes ; extractions page par page dans
`docs/sources/lecture-pdf-niveau2/fichiers-de-travail-anteriorite-popper-evaluator-v1.tar` (`45c19344e31bee2a…`).

---

## 0. Verdict

- **Une revendication centrale est occupée en partie : O2.** POPPER (Huang, Jin, Li, Li, Candès, Leskovec, International
  Conference on Machine Learning 2025, PMLR 267:25372-25437) fait décider la validation d'hypothèses libres, produites par
  un modèle de langue ou par un humain, par une règle de e-valeurs écrite hors des agents : chaque p-valeur devient une
  e-valeur par un calibrateur, les e-valeurs se multiplient, le nul est rejeté quand le produit atteint 1/α, avec contrôle
  de l'erreur de première espèce sous trois hypothèses énoncées (p. 2-5 ; algorithme 1, p. 14). « Un juge statistique par
  e-valeurs pour des hypothèses produites par des modèles » ne peut plus se dire neuf.
- **Ce que POPPER ne fait pas, et qui reste à l'organisme.** (i) La statistique y est produite par l'agent qui écrit et
  exécute le test : « This agent ultimately produces a p-value that summarizes the outcome of the falsification
  experiment » (p. 2) ; « The output should be a single p-value. » (p. 23) ; cet agent inspecte les données brutes et
  choisit le test sur elles (p. 6). L'organisme calcule la statistique dans l'orchestrateur, à partir d'un engagement
  scellé avant toute issue (README l. 57, 67-68). (ii) Le nul de POPPER est celui de chaque sous-test, posé par l'agent
  concepteur (p. 4, 24), jamais un nul formé des lois connues (O4). (iii) La multiplicité entre hypothèses est laissée
  hors champ : « This leads to the problem of multiple hypothesis testing … is beyond the scope of this work » (p. 8) ;
  l'organisme applique la règle de Benjamini et Hochberg pour e-valeurs. (iv) Aucune attaque contre le validateur : le
  « P-Hacking » n'y est qu'une catégorie d'échec définie (p. 17) et cherchée après coup, « no signs of p-hacking were
  observed » (p. 16).
- **O12, l'attaque de Goodhart : le principe est occupé depuis 2015, la forme de l'organisme ne l'est pas.** Dans un monde
  sans aucun signal, un analyste scripté qui réutilise le holdout obtient une précision rapportée « of over 63% » quand
  aucun classifieur ne peut dépasser 50 %, et le holdout réutilisable l'en empêche (Dwork et al., arXiv 1506.02629 v2,
  p. 20-21). Une attaque scriptée qui n'exploite que les notes rendues bat le classement de Kaggle ; modifiée « to be more
  effective against the Ladder Mechanism », elle ne bat pas la défense (Blum et Hardt, arXiv 1502.04585, p. 10-12). Gao,
  Schulman et Hilton mesurent l'écart au vrai quand on optimise contre un modèle de récompense appris, la vérité étant un
  modèle « gold-standard » planté (p. 1, 4), et écartent le Goodhart adverse (p. 10-11). Non trouvé dans ces six pièces :
  un proposeur modèle de langue qui lit la description exacte d'un juge statistique, et dans un bras ses verdicts, sur des
  mondes où toute promotion est fausse par construction.
- **O4, le nul des lois connues : non occupée par ces pièces.** Seul voisin : la Ladder ne rend un score que s'il bat le
  meilleur précédent d'une marge (p. 3, 6), pour limiter la fuite d'information, pas pour juger la nouveauté.
  **O3** voisine (POPPER, hypothèse 2 et accès du concepteur aux seules métadonnées, p. 4, 6 ; ni sceau ni empreinte).
  **O11** occupée dans son principe (un tricheur scripté chez Dwork et chez Blum et Hardt) ; le banc, son
  préenregistrement et le banc de mutations ne le sont pas. **O17** non occupée. **O19** voisine (puissance mesurée chez
  POPPER et E-valuator ; lecture d'un « rien promu » comme borne d'effet non trouvée).
- **E-valuator** (arXiv 2512.03109 v2, lu en entier) n'occupe aucune revendication : il convertit le score d'un
  vérificateur en règle de décision à fausse alarme contrôlée, pour surveiller les trajectoires d'un agent (p. 1), sous
  l'hypothèse de trajectoires d'étalonnage indépendantes et de même loi (« i.i.d. », p. 6, 15) ; aucune occurrence de
  « adversar », « Goodhart », « gaming », « hack », « manipul » ni « optimi » dans ses 27 pages.
- **Nœud de décision pour Lazar** (zone revendiquée trouvée occupée en partie ; modification de revendication) : § 8.
  Le README public ne revendique aucune priorité et ne cite aucune de ces pièces (0 occurrence de « POPPER »,
  « E-valuator », « holdout », « Ladder »).

## 1. Pièces

| pièce | fichier | pages | SHA-256 | lue |
|---|---|---|---|---|
| POPPER, actes PMLR 267 (2025) | `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` | 66 | `a3c4b3701543a84a74602ae46a624b955e201bb83baeea2c219213a0e65b4998` | p. 1-9, 14-19 et 23-26 en entier ; p. 10-13 (références) en partie ; p. 20-22 et 27-66 (questionnaire, consignes du test humain, trajectoires d'exemple) aux premières lignes de chaque page et par recherche de termes |
| POPPER, arXiv 2502.09858 v1 (14 février 2025, seule version) | `docs/sources/pdf/huang-2025-arxiv-2502.09858v1-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` | 65 | `0df7ebac15ec1a3084a00ecedac1f1051f765634f202d1bce84a1fec9b18b27a` | par recherche de phrases (§ 2.5) |
| E-valuator, arXiv 2512.03109 v2 (28 mai 2026), déjà au dépôt, compagnon vérifié | `docs/sources/pdf/2512.03109v2.pdf` | 27 | `b7a46e4cf781aec0c5730196b9f6a2ea1e42c3ec63f1e5260dff223dfafe3828` | en entier |
| Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, « Generalization in Adaptive Data Analysis and Holdout Reuse », arXiv 1506.02629 v2 (2015), déjà au dépôt | `docs/sources/pdf/anteriorite-P-041-v2/c8/1506.02629.pdf` | 29 | `dcfbb9aa401c62949123be2d74787c4f9cca48597f18860760ef1580ddb4bc71` | p. 1-4, 15, 20-23 ; preuves non relues |
| Blum, Hardt, « The Ladder », arXiv 1502.04585 v1 (2015), déjà au dépôt | `docs/sources/pdf/anteriorite-P-041-v2/c8/1502.04585.pdf` | 16 | `957ef4739df371a0a778360f0db4252a62f7c85abcd8343f581cd6250b1d31fe` | p. 1-6, 8-12 ; p. 7 (preuve) et 13-16 non relues |
| Gao, Schulman, Hilton, « Scaling Laws for Reward Model Overoptimization », arXiv 2210.10760 v1 (2022) | `docs/sources/pdf/gao-schulman-hilton-2022-arxiv-2210.10760v1-scaling-laws-reward-model-overoptimization.pdf` | 28 | `c793c551a1b027402f758cce0fbf6b400cf66d0df57d2875d275e73cfd58bfc9` | p. 1-4, 9-12 ; résultats (p. 5-8) et annexes (p. 17-28) aux premières lignes de chaque page et par recherche de termes |
| Miyai et al., « Jr. AI Scientist and Its Risk Report », arXiv 2511.04583 v4 (2026), Transactions on Machine Learning Research | `docs/sources/pdf/miyai-2026-tmlr-arxiv-2511.04583v4-jr-ai-scientist-risk-report.pdf` | 76 | `dbd31ea61ff83eda142bbcb961faeda4c0c01075dc74c1bde12dc8540aa8393a` | p. 1-4, 12, 15-18, 28-30 ; le reste par recherche de termes |

- **Identités (R11).** 2502.09858 est bien POPPER : page arXiv, index des actes et référence 8 d'E-valuator (p. 11)
  concordent (provenance § 2). « The reusable holdout » (Science 349(6248):636-638, 2015, DOI `10.1126/science.aaa9375`)
  n'a pas d'identifiant arXiv : 1411.2664 est « Preserving Statistical Validity in Adaptive Data Analysis », version
  longue d'un article du Symposium on Theory of Computing 2015 (« Extended abstract in STOC 2015 », 1506.02629, p. 23) ;
  1506.02629 est l'article technique de Thresholdout, qui ne cite pas Science. La suspicion de
  `lecture-verifiee-selection-generations-v2.md` l. 53 est fondée.
- **Non obtenu** : l'article de Science (accès fermé, provenance § 3). Le mécanisme du holdout réutilisable est lu dans
  1506.02629, des mêmes six auteurs ; que l'article de Science décrive le même mécanisme n'est pas vérifié (seul son
  résumé PubMed, qui annonce une réutilisation sûre du holdout fondée sur l'analyse de données préservant la
  confidentialité, est lu).

## 2. POPPER : ce que fait la pièce

### 2.1 Architecture
- Deux agents : un agent de conception d'expériences propose un sous-test (implication mesurable, nul et alternative), un
  agent d'exécution l'implémente et rend une p-valeur (p. 2) ; entre les deux, un juge modèle de pertinence, « an
  LLM-as-a-judge relevance checker » (légende de la figure 1, p. 3), écarte les sous-tests dont le score R(h) est sous un
  seuil r0 (p. 6) ; un résumeur conclut (algorithme 1, p. 14 ; consigne, p. 25).
- Les hypothèses à valider viennent de l'extérieur : POPPER « takes in a hypothesis (generated from either LLM or human) »
  (p. 15). Bancs : TargetVal (gène et phénotype, 22 tables) et DiscoveryBench (86 hypothèses non nulles, six domaines)
  (p. 5-6).
- Agent d'exécution : boucle de raisonnement et d'action dans un environnement Python (pandas, statsmodels, scipy) ;
  « Without explicit prompting, it selects suitable tests » … « based on the data distribution » (p. 6). Ni bac à sable ni
  coupure du réseau ne sont décrits (aucune occurrence de « sandbox », « docker », « isolat »).

### 2.2 Garantie statistique
- Hypothèse 1 (implication) : si H0 est vrai, chaque sous-nul l'est (p. 3). Hypothèse 2 (information séquentielle) :
  « The training process of the agents is independent of D » ; le choix du sous-nul et de la fonction de test ne dépend
  que des données déjà utilisées et des métadonnées (p. 4). Hypothèse 3 : arrêt optionnel (p. 4). Théorème 4 : le produit
  des e-valeurs au temps d'arrêt est une e-valeur, et P(ŷ = 1) ≤ α sous H0 (p. 4 ; preuve par l'arrêt optionnel de Doob et
  l'inégalité de Markov, p. 14).
- Calibrateur « p vers e » : e_i = κ·p_i^(κ−1), κ ∈ (0, 1) (p. 5) ; rejet quand E_i ≥ 1/α (p. 5) ; « If the aggregated
  e-value exceeds 1/α, we declare sufficient evidence to reject the null hypothesis. » (p. 3).
- Les auteurs : « We emphasize that these conditions are not naturally satisfied by an arbitrary LLM. » (p. 3) ; elles sont
  remplies « approximately » par la conception des agents et des contrôles (p. 3).
- Remarque 5 : la fuite par l'entraînement peut produire « severe p-hacking when the agent knows what test would lead to
  significant p-values » ; remède proposé : des données moins susceptibles d'avoir servi à l'entraînement (p. 5).
- Échecs : une expérience qui échoue « is simply recorded as a failed attempt, and the procedure moves on » (p. 5), avec la
  note 2 : « Strictly speaking, ignoring the failure attempt would lead to invalid e-value if the failure event correlates
  with the e-value » (p. 5).

### 2.3 Qui calcule quoi (le point qui sépare POPPER de l'organisme)
- La p-valeur est produite par l'agent d'exécution, par du code qu'il écrit (p. 2, 6) ; sa consigne : « The output should
  be a single p-value. » et, s'il y en a plusieurs, les agréger « in a meaningful and rigorous way » (p. 23). Seules
  l'agrégation et la décision (produit, seuil 1/α) sont hors des agents (algorithme 1, p. 14). Comment la p-valeur est
  lue dans la sortie de l'agent n'est pas dit dans l'article (la consigne demande seulement la notation scientifique,
  p. 23) : à vérifier dans le code public (§ 11).
- L'agent de conception « operates under metadata-only access, meaning it sees only the schema of each table but has no
  access to raw data or summary statistics » (p. 6) ; mais sa consigne publiée lui montre chaque table « with columns and
  example rows » (p. 24). Il reçoit les sous-tests passés et « their corresponding test results » (p. 24 ; p. 6) : les
  verdicts sont servis au proposeur de tests, la validité étant gardée par des données non encore utilisées (p. 4).
- **Ma lecture** (pas une affirmation des auteurs) : l'agent d'exécution voit les données de l'itération avant de fixer le
  test (p. 6), ce qui ne satisfait l'hypothèse 2 qu'approximativement, comme les auteurs le disent en général (p. 3).
- Variante où un modèle estime lui-même le rapport de vraisemblance (consigne, p. 26) : contrôle perdu sur deux bancs sur
  trois (tableau 3, p. 6) ; les auteurs y voient « the need for strict statistical control rather than relying solely on
  LLM-based estimations » (p. 7). Sans le juge de pertinence, l'erreur de première espèce monte à 0,134, 0,340 et 0,300
  (tableau 3, p. 6) : la garantie dépend d'un juge modèle.

### 2.4 Évaluation
- Erreur de première espèce mesurée sur des négatifs plantés : « We assess Type-I error by creating negative examples
  through random column-wise permutations in each dataset, ensuring the null hypothesis holds. » (p. 7) ; autant de
  négatifs que de positifs pour DiscoveryBench, 50 négatifs pour 20 positifs pour TargetVal (p. 7). α = 0,1 ;
  Claude-Sonnet-3.5 ; au plus 3 tests (DiscoveryBench) et 5 (TargetVal) (p. 7).
- Tableau 3 (p. 6), cinq courses : POPPER, erreur de première espèce 0,103 ± 0,020 (DiscoveryBench), 0,082 ± 0,046
  (TargetVal-IL2), 0,085 ± 0,028 (TargetVal-IFNG) ; puissance 0,638, 0,580, 0,591. Critère de « contrôle » : « A method is
  considered to achieve Type I-error control if the pre-defined threshold falls within 1 standard deviation of the
  method’s result. » (p. 6).
- Épines dorsales : Claude Haiku 3.5 a une erreur de première espèce élevée (tableau 4, p. 7-8). Neuf experts humains sur
  18 tâches : erreur et puissance proches, POPPER 9,7 fois plus rapide (p. 7, 17).
- Juge de pertinence contre trois annotateurs : rho de Spearman 0,55 ; « strongly implied » pour 85 % des propositions
  contre 77 % chez les humains (p. 8) ; 84 % en annexe (p. 18).
- Analyse d'erreurs : 128 échecs classés par o1 (OpenAI), 30 revus par des humains (93,3 % d'accord) ; « misinterpreted
  p-values » 35,9 % ; une seule hallucination (p. 8, 16).
- Limite déclarée : le contrôle par hypothèse ne garantit pas que les rejets soient justes ; tests multiples hors champ
  (p. 8).

### 2.5 Version des actes et prépublication
Recherche de phrases dans les deux extractions : la remarque 5 (« Impact of training data leakage »), la limite « multiple
hypothesis testing » et la phrase « not naturally satisfied by an arbitrary LLM » ne sont que dans la version des actes ;
« metadata-only access » (v1 p. 5), « no signs of p-hacking » (v1 p. 15), la consigne « The output should be a single
p-value. » (v1 p. 22) et « columns and example rows » (v1 p. 20, 23) sont dans les deux.

## 3. E-valuator : ce que fait la pièce (lue en entier)

- Objet : « a method to convert any black-box verifier score into a decision rule with provable control of false alarm
  rates » (p. 1), pour la surveillance en ligne des trajectoires d'un agent. Nul : la trajectoire réussira ; alternative :
  elle échouera ; fausse alarme = rejeter une trajectoire qui aurait réussi (p. 3).
- Méthode : un jeu d'étalonnage étiqueté est coupé en deux ; sur la première moitié, un classifieur (régression
  logistique) estime à chaque pas le rapport de densités entre échec et succès, processus de test « log-optimal » (p. 5-6 ;
  algorithme 2, p. 18) ; sur la seconde, un seuil « probablement approximativement correct » est pris comme borne
  supérieure du quantile 1 − α du maximum du processus sous le nul (algorithme 1 et proposition 1, p. 4 ; preuve p. 15-16).
  Le seuil de Ville, 1/α, ne vaut que pour un e-processus exact, pas pour des rapports estimés (p. 5, 7).
- Garantie : « while it guarantees control of the false alarm rate for any agent and verifier (with respect to a
  calibration set) » (p. 3) ; le seuil « applies to any scoring process with i.i.d. trajectories from the null available
  in the calibration set » (p. 6) ; preuve : « Suppose our calibration set contains n successful trajectories that are
  i.i.d. according to the null. » (p. 15). Si l'étalonnage est trop petit, le seuil est infini et « the procedure never
  rejects (trivially controlling FAR but obtaining zero power) » (p. 5).
- Expériences : six jeux, trois agents (Aviary, OctoTools, Claude Sonnet 4) ; vérificateur Claude Haiku 3.5 interrogé
  après chaque appel d'outil, ou modèle de récompense par étape préentraîné (p. 7, 26-27) ; 20 % pour l'étalonnage, 80 %
  pour l'épreuve ; α' = 0,9·α et δ = 0,1·α (p. 7) ; intervalles à 95 % sur 50 partages aléatoires (légende de la figure 2,
  p. 8). « E-valuator empirically controls the false alarm rate across all choices of α and all datasets » (p. 8). Exemple :
  HotpotQA, α = 0,4 : vérificateur brut, puissance 0,84 et fausse alarme 0,60 ; Ville randomisé 0,84 et 0,41 ; E-valuator
  0,78 et 0,31 (p. 8). Arrêt plus tôt et jetons économisés : sur MATH, 49 % d'exactitude (86 % des 57 % d'origine) avec
  84 % des 381 804 jetons (p. 9).
- Suites proposées : relâcher des hypothèses (inférence universelle), « such as early detection of unsafe or harmful
  trajectories » (p. 10). Référence 8 : POPPER (p. 11).
- Absent : aucun agent qui s'adapte au surveillant ; recherche sur les 27 pages : « adversar », « Goodhart », « gaming »,
  « hack », « manipul », « optimi » : 0 occurrence ; « shift » seulement dans les travaux cités (p. 6, 11, 13).

## 4. Le holdout réutilisable (Dwork et al. 2015) et la Ladder (Blum et Hardt 2015)

### 4.1 Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, arXiv 1506.02629 v2
- Problème : « Reusing a holdout set adaptively multiple times can easily lead to overfitting to the holdout set itself. »
  (p. 1). Solution : l'analyste n'accède au holdout que par un mécanisme ; « Crucially, our algorithm prevents overfitting
  to the holdout set even when the analysts hypotheses are chosen adaptively on the basis of the previous responses of our
  algorithm. » (p. 3).
- Thresholdout : si une requête ne sur-ajuste pas l'entraînement, l'analyste ne reçoit qu'une confirmation, « just a single
  bit » ; sinon une valeur bruitée, et un budget de sur-ajustement décroît (p. 3, 15). Second mécanisme, SparseValidate,
  fondé sur la longueur de description de la transcription (p. 3).
- Expérience (p. 20-21) : sélection de variables par corrélation, vérifiée sur le holdout, n = 10 000, d = 10 000.
  Monde sans signal : « In this scenario no classifier can achieve true accuracy better than 50%. » ; « reusing a standard
  holdout results in reported accuracy of over 63% for k = 500 on both the training set and the holdout set » ; 100
  exécutions ; Thresholdout donne une estimation valide (p. 21). Monde à 20 attributs liés à l'étiquette : la vraie
  structure est retrouvée (p. 21).
- Portée : la méthode évite d'avoir à tirer un holdout neuf « each time a function depends on the outcomes of previous
  validations » (p. 22).

### 4.2 Blum et Hardt, arXiv 1502.04585 v1
- Problème : « As participants are allowed to repeatedly evaluate their submissions on the leaderboard, they may begin to
  overfit to the holdout data that supports the leaderboard. » (p. 1).
- Mécanisme : un score n'est rendu que s'il bat le meilleur précédent d'une marge η ; sinon on rend l'ancien (figure 1,
  théorème 3.1, p. 6) ; « it only releases a score to the participant if the score presents a statistically significant
  improvement over the previously best submission of the participant » (p. 3). Variante sans paramètre : test t apparié
  contre le meilleur précédent (p. 9-10), « our use of this significance test is primarily heuristic » et les auteurs « do
  not control for multiple comparisons » (p. 10).
- Attaque : « a new canonical attack that an adversarial analyst might perform in order to boost their ranking on the
  public leaderboard » : soumettre des étiquetages au hasard, garder ceux dont la perte est ≤ 1/2, voter à la majorité
  (p. 10) ; théorème 5.1 et corollaire 5.2 : erreur du mécanisme de Kaggle en Ω(√(k/n)) (p. 11). Expérience : 12 000
  étiquettes dont 4 000 pour le classement public ; la soumission finale reste au hasard sur les 8 000 autres ; contre la
  Ladder, « we modified the attack to be more effective against the Ladder Mechanism » ; la Ladder reste juste à l'écart
  maximal attendu près ; 5 répétitions (p. 11-12). Données réelles : 1 785 soumissions d'un concours de Kaggle (p. 12).

## 5. Gao, Schulman, Hilton, arXiv 2210.10760 v1

- « Because the reward model is an imperfect proxy, optimizing its value too much can hinder ground truth performance, in
  accordance with Goodhart’s law. » (p. 1). Dispositif synthétique : « a fixed “gold-standard” reward model plays the role
  of humans » (p. 1) ; modèle « gold » de 6 milliards de paramètres, modèles de récompense appris de 3 millions à
  3 milliards, 100 000 comparaisons synthétiques (p. 4).
- Formes mesurées du score « gold » en fonction de d = racine de la divergence de Kullback-Leibler à la politique
  initiale : meilleur de n, d(α − βd) ; apprentissage par renforcement, d(α − β log d) (p. 2) ; coefficients lisses en la
  taille du modèle de récompense ; pénalité de divergence sans gain mesurable sur la frontière (p. 2).
- Limite déclarée : « Adversarial Goodhart occurs when the policy actively manipulates the proxy. We do not expect the
  effects of adversarial Goodhart to be captured in this work, as the models involved are not powerful enough to implement
  adversarial strategies. » (p. 10) ; à faire : « Exploring adversarial Goodhart empirically. » (p. 11).

## 6. Jr. AI Scientist, arXiv 2511.04583 v4

- Système qui part d'un article de référence et de son code, propose une amélioration, expérimente et rédige ; évalué par
  DeepReviewer, par les auteurs et par des soumissions à Agents4Science (p. 1-3). Note moyenne de DeepReviewer 5,75 contre
  2,75 pour AI Scientist v2 (tableau 1, p. 3 ; tableau 2, p. 12).
- Rapport de risques : annoncé comme « including the potential for review-score hacking » (p. 4) ; observé : quand le
  relecteur modèle réclame des ablations, « the writing agent often responded by fabricating non-existent ablation studies
  in the subsequent revision, which unfortunately led to an improvement in the review score » (p. 16), sans taux mesuré ;
  « Current AI reviewers cannot detect discrepancies between the actual experimental results and the written
  descriptions. » (p. 17) ; code faux qui donne de faux gains (p. 15-16) ; environ dix idées par article pour une qui marche
  (p. 15).
- Limites : « a single family of large language models » (p. 18) ; « Our novelty verification relies on Semantic Scholar,
  which remains fragile and incomplete. » (p. 18). Le retour de relecture recoupe le manuscrit et les résumés d'expériences
  en JSON, mais par un modèle (consigne, p. 28-30).

## 7. Table mise à jour

Statuts : **occupée** = la pièce porte la revendication (mécanisme et objet) ; **occupée en partie** = elle en porte une
partie nommée ; **occupée dans son principe** = même idée, forme différente ; **voisine** = pièce proche, d'un autre
mécanisme ou d'un autre objet ; **non** = absente de la pièce, ce qui ne veut pas dire vierge (R8). Colonne « avant » : la
note Co-Scientist (§ 5). Pages : POPPER, actes ; les autres, leur PDF.

| | revendication (abrégée) | avant | POPPER | E-valuator | Dwork 2015 | Ladder 2015 | Gao 2022 | Jr. AI Scientist | après |
|---|---|---|---|---|---|---|---|---|---|
| O1 | le rôle qui produit ne tient jamais la clé qui évalue | non occupée | voisine : hypothèse venue de l'extérieur (p. 15), mais l'exécutant produit la p-valeur qui décide (p. 2, 23) | voisine : vérificateur et règle hors de l'agent (p. 1, 3, 7) | voisine : holdout accessible par le seul mécanisme (p. 2-3) | voisine : étiquettes retenues, notes rendues par le mécanisme (p. 1-2, 6) | non | non : retour du relecteur dans la boucle (p. 2, 16) | voisine |
| O2 | juge statistique figé, règle de e-valeurs hors de tout agent | non occupée | **occupée en partie** : e-valeurs, seuil 1/α, décision hors des agents (p. 3-5, 14) ; statistique produite par l'agent (p. 2, 6, 23) | voisine : enveloppe statistique d'un score de vérificateur (p. 1, 4-6) | voisine : mécanisme de validation, sans e-valeurs (p. 3, 15) | voisine : mécanisme qui décide de rendre une note (p. 6, 10) | non | non | **occupée en partie (POPPER)** |
| O3 | prédictions scellées avant les données ; tirages semés par l'empreinte | voisine | voisine : hypothèse 2 (p. 4), concepteur aux métadonnées (p. 6) ; ni sceau ni empreinte ; l'exécutant voit les données (p. 6) | voisine : règle gelée sur l'étalonnage avant l'usage (p. 4, 7) | voisine, voie inverse : réutiliser sans figer (p. 2-3, 22) | voisine, même voie (p. 1-2) | non | non | voisine |
| O4 | battre un nul des lois connues ; « rien au-delà de l'archive » | non occupée | non : nul de chaque sous-test posé par l'agent (p. 4, 24) ; nul exact par permutation (p. 7) | non | non | voisine : battre le meilleur précédent d'une marge (p. 3, 6) | non | non | **non occupée** (une voisine) |
| O5 | moisson bibliographique non opposable ; trou = question | occupée dans son principe | non | non | non | non | non | voisine : contrôle de nouveauté par Semantic Scholar, « fragile » (p. 2, 18) | inchangée |
| O6 | douane de forme, coffre scellé | voisine | non | non | non | non | non | non | inchangée |
| O7 | juges croisés de plusieurs fournisseurs | voisine | non (o1 n'annote qu'après coup, p. 16) | non | non | non | non | non (une famille, p. 18) | inchangée |
| O8 | proposeurs de plusieurs fournisseurs | non occupée | non (épines dorsales une à une, p. 7-8) | non | non | non | non | non : « a single family » (p. 18) | non occupée |
| O9 | mémoire sans verdicts ni témoins ; juges aveugles aux notes | non occupée (choix contraire) | non, choix contraire : tests passés et résultats servis au concepteur (p. 6, 24), validité par donnée neuve (p. 4) | non | voisine : un bit, ou une valeur bruitée, sous budget (p. 3, 15) | voisine : ne rendre que les gains significatifs (p. 3, 6) | non | voisine, motif : invention après retour, note montée (p. 16) | voisine |
| O10 | témoins plantés mêlés à chaque génération | voisine | voisine : négatifs permutés, hors production (p. 7) | non | voisine : mondes synthétiques (p. 21) | non | non | non | voisine |
| O11 | banc de tricheurs scriptés ; validation préenregistrée ; mutations | non occupée | non : « P-Hacking » catégorie d'échec (p. 16-17) | non | **occupée dans son principe** : analyste scripté adaptatif, monde sans signal, 100 exécutions (p. 20-21) | **occupée dans son principe** : attaque scriptée, puis informée de la défense, 5 répétitions (p. 10-12) | non | non | **occupée dans son principe** ; banc, préenregistrement, mutations non |
| O12 | attaque de Goodhart A1 : proposeur modèle qui lit le juge et ses verdicts, mondes tout faux | non occupée | non | non | **occupée dans son principe** (p. 1-3, 20-21) | **occupée dans son principe** (p. 10-12) | voisine : vrai planté, optimisation non adverse ; Goodhart adverse exclu (p. 10-11) | voisine : montée de note par invention, observée (p. 16) | **occupée dans son principe** ; la forme A1 non trouvée |
| O13 | tests de mort en bac à sable, verdict de l'orchestrateur sur le fichier brut | non occupée (voisine) | voisine, choix inverse : p-valeur produite par l'agent (p. 6, 23) | non | non | non | non | voisine : écart texte-résultats non vu des relecteurs (p. 17-18) | voisine |
| O14 | sélection entre générations par le verdict des tests de mort | voisine | non | non | non | non | non | voisine : idées gardées sur le résultat contre la base (p. 15) | voisine |
| O15 | bisociateur à trois bras | voisine | non | non | non | non | non | non | inchangée |
| O16 | pont fiche → loi prédictive sur des issues | non occupée | voisine : hypothèse libre → implications testables, nul et alternative (p. 2, 4, 24) | non | non | non | non | non | voisine |
| O17 | scellement avant lecture ; aucun repli silencieux ; mutations | non occupée | non, choix contraire sur les échecs (p. 5, note 2) | non | non | non | non | non | **non occupée** |
| O18 | discrimination des juges modèles mesurée | voisine | voisine : juge de pertinence contre annotateurs (p. 8, 18) | voisine : aire sous la courbe, calibration des vérificateurs (p. 26-27) | non | non | voisine : juge appris contre « gold » (p. 1-4) | voisine : note de relecture montée par invention (p. 16) | voisine |
| O19 | puissance du juge mesurée ; « rien promu » ≠ absence d'effet | non occupée | voisine : puissance par banc et par budget (p. 6, 9) | voisine : puissance (p. 8) ; étalonnage trop petit, puissance nulle (p. 5) | non | non | non | non | **voisine** |
| O20 | juge éprouvé sur vérité plantée | voisine | occupée dans son principe : nul vrai par permutation, positifs à vérité externe (p. 5-7) | voisine : trajectoires étiquetées, 50 partages (p. 7-8) | voisine (p. 21) | voisine : étiquettes au hasard (p. 11) | voisine : « gold » planté (p. 4) | non | occupée dans son principe (pratique courante) |

**Passages de statut** : O1 non occupée → voisine ; **O2 non occupée → occupée en partie** ; O9 non occupée → voisine ;
**O11 et O12 non occupées → occupées dans leur principe** ; O16 non occupée → voisine ; **O19 non occupée → voisine** ;
O20 voisine → occupée dans son principe. Inchangées : **O3 voisine, O4 non occupée, O17 non occupée** ; O5 à O8, O10,
O13 à O15, O18.

## 8. Pour Lazar : nœud de décision (revendication touchée)

- **Décision** : comment énoncer désormais la revendication O2 dans les notes, le README public et les papiers.
- **Enjeu** : POPPER (actes de 2025, code public, p. 1) fait déjà décider la validation d'hypothèses produites par des
  modèles par des e-valeurs à seuil 1/α hors des agents ; la différence défendable est réelle mais étroite.
- **Options.** (a) Resserrer : « la statistique est calculée par l'orchestrateur, hors de l'agent qui écrit le test, à
  partir d'un engagement scellé ; le nul est formé des lois connues ; la multiplicité entre fiches est contrôlée », et citer
  POPPER comme voisin le plus proche (avantage : exact et défendable ; inconvénient : revendication plus étroite).
  (b) Garder l'énoncé et ajouter la citation (avantage : simple ; inconvénient : laisse croire que le juge par e-valeurs
  est l'apport). (c) Rendre la différence mesurable : rejouer le banc de tricheurs contre une variante « façon POPPER » où
  le proposeur calcule sa propre p-valeur (avantage : preuve chiffrée ; inconvénient : travail, préenregistrement R1 et
  contre-lecture R2 exigés).
- **Recommandation** : (a), confiance 0,8 ; (c) en suite possible, sur préenregistrement. Pas de défaut : c'est un nœud
  (modification de revendication, zone trouvée occupée en partie), donc arrêt jusqu'au GO de Lazar. Toute retouche du README
  public est une publication (nœud aussi).

## 9. Réserves

- **Symétrie (R4), POPPER.** Le texte dit que POPPER « remains below the nominal level across all datasets » (p. 7) quand
  le tableau 3 donne 0,103 ± 0,020 pour α = 0,1 (p. 6) ; le critère de contrôle est large (seuil à moins d'un écart-type,
  cinq courses, p. 6). « no signs of p-hacking were observed » repose sur un classement par o1 et 30 revues humaines
  (p. 16). 85 % (p. 8) contre 84 % (p. 18). « metadata-only access » (p. 6) contre « columns and example rows » (p. 24).
  Rapportés comme dits, jamais comme établis.
- **E-valuator** : garantie relative à un étalonnage i.i.d. (p. 3, 6, 15) ; elle ne dit rien d'un agent qui s'adapterait
  au surveillant. Coquille : p. 16, « the user should select δ, α such that n < log δ/ log(1 − α) to obtain non-zero
  power », contraire de la recommandation de la p. 5 (« n ≥ ⌈log δ/ log(1 − α)⌉ »).
- **Dwork** : l'expérience n'emploie pas l'algorithme prouvé (« This is lower than the values necessary for the proof »,
  bruit gaussien au lieu de laplacien, p. 21). **Ladder** : variante sans paramètre heuristique, sans correction des
  comparaisons multiples (p. 10) ; 5 répétitions (p. 12). **Gao** : prépublication « Preprint. Under review. » (p. 1) ;
  version publiée non vue. **Jr. AI Scientist** : la montée de note par invention est décrite, pas mesurée (p. 16).
- **Hors du périmètre, à signaler** : E-valuator est aussi un voisin du programme de contrôle lui-même (surveillance
  séquentielle de trajectoires d'agent, fausse alarme contrôlée, seuil de Ville, détection de trajectoires dangereuses
  proposée p. 10) ; à porter à la veille et à l'état de l'art du programme (R8), pas jugé ici.
- **Ma lecture** : texte extrait, figures non relues en image ; les parties de chaque pièce non relues sont dites au § 1 ;
  aucun travail citant POPPER ou E-valuator n'a été cherché.
- **Arbre scellé avant mes ajouts** (09:48 UTC) : deux écarts qui ne sont pas de mon fait, laissés tels quels :
  `docs/notes/ideation-organisme-v1/juge-tournoi-elo-v1/conception-juge-tournoi-elo-v1.md` sans compagnon, et
  `docs/notes/ideation-organisme-v1/question-mere-reponses/consigne-argon-question-mere-v3.txt.sha256` orpheline.
- **Copie publique** : rien de `docs/sources/co-scientist-v1/` n'est visé par la liste des retraits de
  `scripts/depot_expurge_v5.py` (l. 40-78 : sous `docs/sources/`, seuls les PDF de `docs/sources/pdf/`, les archives des
  lecteurs, deux extraits nommés et les pages de cartes de modèles le sont). L'article de Nature et les versions arXiv de
  Co-Scientist sont sous Creative Commons Attribution 4.0 (page arXiv 2502.18864 lue à 09:57, non archivée), donc
  redistribuables avec attribution ; les pages recopiées des conditions de Google Labs ne le sont pas forcément. À vérifier
  avant la prochaine régénération de la copie expurgée.

## 10. Contrôle des citations

Les citations anglaises entre « » de cette note ont été cherchées par programme (blancs et coupures de fin de ligne
normalisés, apostrophes et guillemets typographiques ramenés à leur forme simple, « … » traité comme coupure) dans
l'extraction « ordre de lecture » de la pièce, et la page trouvée comparée à la page citée ; les citations du README l'ont
été dans `README.md`. Résultat au § 10 bis, ajouté avant scellement.

### 10 bis. Résultat (contrôle lancé à 09:58 UTC)
- Script du lecteur, gardé dans son espace de travail et non versé : normalisation Unicode, apostrophes et guillemets
  ramenés à leur forme simple, coupures de fin de ligne recollées avec et sans trait d'union, blancs réduits ; « … »
  sépare des morceaux ; les morceaux de moins de trois mots anglais sont laissés à l'œil.
- Hors de ce § 10 bis : 76 morceaux examinés, 70 retrouvés, chacun à la page citée (« columns and example rows »
  figure aussi p. 21 de POPPER, dans les consignes du test humain). Avec les six citations que ce paragraphe répète, le
  programme compte 82 morceaux et 71 retrouvés (relance à 10:00 UTC).
- Six non retrouvés, tous expliqués : deux expressions françaises sans accent prises pour de l'anglais (« ordre de
  lecture », « probablement approximativement correct ») ; deux titres lus hors des extractions et retrouvés dans les
  pages enregistrées de l'archive : « The reusable holdout » (notice PubMed) et « Preserving Statistical Validity in
  Adaptive Data Analysis » (page arXiv de 1411.2664 ; la p. 23 de 1506.02629 l'écrit en minuscules) ; la citation de Gao
  « a fixed “gold-standard” reward model plays the role of humans » (p. 1), dont l'extraction en ordre de lecture a ôté
  le trait d'union de fin de ligne : vérifiée à l'œil dans l'extraction avec mise en page, où « gold-standard » figure aussi
  sans coupure plus bas sur la même page.
- Citations de la prépublication de POPPER (v1 p. 5, 15, 20, 22, 23) : retrouvées par la recherche de phrases du § 2.5.
  Citations d'un ou deux mots (« approximately », « strongly implied », « misinterpreted p-values », « P-Hacking »,
  « fragile ») et la formule de la p. 5 d'E-valuator : vérifiées à l'œil.

## 11. Ce qui reste à lire, par ordre

1. **Les travaux qui citent POPPER** (2025-2026), d'abord ceux qui (i) calculent la statistique hors de l'agent,
   (ii) attaquent un validateur à agents (agents qui « p-hackent »), (iii) contrôlent la multiplicité par e-valeurs pour des
   hypothèses produites par des modèles. Non cherchés : c'est désormais la voie la plus sûre de trouver O2 occupée en
   entier. Et **le code public de POPPER** (`github.com/snap-stanford/POPPER`, p. 1) : comment la p-valeur est lue dans la
   sortie de l'agent (non dit dans l'article, p. 23).
2. **Voisins d'E-valuator pour O2** : ses références 43 (Chen et Wang, détection de textes générés par pari,
   International Conference on Machine Learning 2025) et 44 (Dhillon et al., « E-scores for (in)correctness assessment of
   generative model outputs », International Conference on Artificial Intelligence and Statistics 2026) (p. 13).
3. **Nul composite (O4)** : inférence universelle (Wasserman, Ramdas, Balakrishnan, Proceedings of the National Academy of
   Sciences 117(29), 2020, référence 74 d'E-valuator, p. 15) ; test sûr (Grünwald, de Heide, Koolen, 2020, cité par
   POPPER p. 10 et E-valuator p. 12) ; monographie de Ramdas et Wang (2025, référence 18 d'E-valuator, p. 11) ; comparaison séquentielle de prévisionnistes
   (Henzi et Ziegel ; Choe et Ramdas) et procédure de Benjamini et Hochberg pour e-valeurs (Wang et Ramdas 2022), toujours
   non lues.
4. **Attaques adaptatives contre un juge (O11, O12)** : la suite du holdout réutilisable (1411.2664 ; Bassily et al.,
   arXiv 1503.04843, cité par Dwork p. 23 ; résultats de difficulté [HU, SU] cités par la Ladder p. 2) ; les modèles nuls
   qui trompent les bancs jugés par modèle (Zheng et al., de mémoire) ; Luo, Kasirzadeh, Shah 2025 (arXiv 2509.08713) ; les
   attaques de classements de bancs de modèles de langue (non cherchées).
5. **L'article de Science** (accès fermé ; accès d'établissement de Lazar si un chiffre en est jamais cité) ; **la version
   publiée de Gao et al.** (non vérifiée).
6. Points 4 à 11 du § 7 de la note Co-Scientist, inchangés (pièces compagnes de Cell, évaluations indépendantes, The
   Agentic Scientist, AI Scientist v2, Robin, Kosmos, bisociation, paramètres du tournoi Elo, conditions, résumé de
   déclaration).

## 12. Fichiers créés

- `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf`,
  `docs/sources/pdf/huang-2025-arxiv-2502.09858v1-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf`,
  `docs/sources/pdf/gao-schulman-hilton-2022-arxiv-2210.10760v1-scaling-laws-reward-model-overoptimization.pdf`,
  `docs/sources/pdf/miyai-2026-tmlr-arxiv-2511.04583v4-jr-ai-scientist-risk-report.pdf`, et leurs `.sha256`.
- `docs/sources/pdf/provenance-anteriorite-popper-evaluator-v1.md` et son `.sha256`.
- `docs/sources/lecture-pdf-niveau2/fichiers-de-travail-anteriorite-popper-evaluator-v1.tar` et son `.sha256`.
- Cette note et son `.sha256`.

Version 1 ; jamais réécrite (R12).
