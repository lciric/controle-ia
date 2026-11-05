# Lecture de niveau 2, lot 2, groupe B1 (multi-agents) — rapport v1

- **Date** : 2026-10-06, 16 h 48 en temps universel coordonné (UTC).
- **Lecteur** : sous-agent neuf ; il n'a écrit aucun des documents vérifiés.
- **Consignes appliquées** : `lot2/consigne-commune.md` et `lot2/consignes-B1-multi-agents.md`.
- **Dépôt** : rien n'a été modifié sous `/home/user/controle-ia` (lecture seule, ni fichier ni git).

## PDF lus et empreintes

Dossier : `/home/user/controle-ia/docs/sources/pdf/`. Les huit empreintes sha256 calculées sont identiques aux empreintes attendues (`sha256sum -c` : 8 « OK », code 0).

| fichier | pages | empreinte sha256 | lecture |
|---|---|---|---|
| 2605.31593v1.pdf | 17 | 037f653703ec0da12dfaaf83a50d576355e7ac19985cd109426a90567eb8b0f0 | en entier |
| 2607.02514v2.pdf | 35 | 9baceea4719a5ff2d63c3278d425a0c3b9feeb2d447a19a3cd7a6b62d3339c22 | en entier |
| 2607.07368v1.pdf | 81 | d72cae4337e824e4af9eb84759775f6c5dc704f157a0d302df1b44538eb159cd | pages 1 à 75 en entier ; pages 76 à 81 (liste de contrôle NeurIPS) : réponses lues, consignes génériques survolées |
| 2608.02698v1.pdf | 10 | 452ae117a6814f004e65e161606dba52ae73bf645c1b5e49f7788c4df58531ce | en entier |
| 2605.29178v1.pdf | 33 | 85f27b4c7aa7d606e0c12cd2094b0c3b45378a75f4750a99e947707082dfe477 | en entier |
| 2606.09931v1.pdf | 12 | 538e8488bdcc09fcb1d58ff5c88f101d6da0232c73b095aa6e6519e3f3c19232 | en entier |
| 2605.15377v2.pdf | 18 | fe591700228b29dc3287130efe6f877c5eeada84169dcbf1e526f6dc2e401712 | en entier |
| 2608.16190v1.pdf | 10 | 8fdb6141aac64fe6bf9f741336befe58b255e8588294d11ca708c6e8a2c857f5 | en entier |

## Méthode et limites

- **Pages** : rang dans le fichier, texte de `pdftotext -layout` extrait page par page. Pour les pages à deux colonnes, où `-layout` entrelace les colonnes, le contrôle utilise aussi `pdftotext -raw` sur la même page.
- **Figures** : lues par leur texte extrait et leur légende. Deux figures ont été vérifiées à l'image : 2607.07368, page 9 (figure 3) et page 53 (figure 20). Les autres figures n'ont pas été examinées à l'image ; aucun chiffre marqué « auteurs » n'en dépend.
- **Contrôle des citations** : script `outils/controle_citations.py` (tolère seulement les blancs et les césures de fin de ligne). Il a d'abord été testé sur des cas justes et des cas altérés (`outils/test_controle.py` : 14 cas sur 14 conformes, voir l'annexe). Résultat sur ce rapport : voir l'annexe.
- **Verdicts** : « confirmé », « corrigé » (la formulation à mettre à la place suit chaque tableau, repérée F*n*), « introuvable » (avec ce qui a été cherché).
- **Antériorité (R8)** : je dis seulement ce que ces sources occupent ou non. Une limite d'un article n'est pas un trou du champ.

## Sigles présents dans les citations anglaises

Les citations restent mot pour mot ; leurs sigles se lisent ainsi :
- FPR : taux de faux positifs ; TPR : taux de vrais positifs (rappel).
- PR : demande de fusion de code (« pull request ») ; CLI : outil en ligne de commande ; Flask : cadriciel web en Python.
- LLM : grand modèle de langage.
- pAUC : aire partielle sous la courbe de détection (taux de vrais positifs en fonction du taux de faux positifs), limitée aux taux de faux positifs d'au plus 10 % et normalisée ; AUC, AUROC : aire sous cette courbe entière.
- TTD99 : temps de détection, en tours d'attaque, au 99e centile.
- GLM : modèle linéaire généralisé ; HPDI : intervalle de plus haute densité a posteriori ; OR : rapport de cotes.
- K (dans 2607.07368) : nombre d'agents d'une séquence d'attaque.
- AISI : institut britannique de sécurité de l'intelligence artificielle (UK AI Security Institute) ; MATS : programme de recherche « ML Alignment & Theory Scholars » ; SPAR : « Supervised Program for Alignment Research » ; IEEE : Institute of Electrical and Electronics Engineers ; NeurIPS : conférence Neural Information Processing Systems.
- Catégories d'arXiv citées dans les identités : cs.AI (intelligence artificielle), cs.CR (cryptographie et sécurité), cs.GT (informatique et théorie des jeux), cs.LG (apprentissage automatique).

## 1. 2605.31593v1 — « Stateful Online Monitoring Catches Distributed Agent Attacks »

**Identité.** Auteurs : Davis Brown, Samarth Bhargav, Arav Santhanam, Kasper Hong, Ivan Zhang, Matan Shtepel, Steffi Chern, Alexander Robey, Eric Wong, Hamed Hassani. Affiliations : University of Pennsylvania (Brown, Chern, Wong, Hassani) et Carnegie Mellon University (Bhargav, Santhanam, Hong, Zhang, Shtepel, Robey). Version 1, arXiv, 29 mai 2026, catégorie cs.CR. Venue : aucune, prépublication. Code : aucun lien ni annonce. Lu en entier.

**Affirmations.**

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 1.1 | l. 83 : « Brown et al. (Penn / CMU) » | confirmé | p. 1 | « University of Pennsylvania 2 Carnegie Mellon University » |
| 1.2 | l. 83 : « première attaque distribuée multi-agents implémentée » | corrigé (F1.1) : les auteurs disent « à notre connaissance » | p. 1 | « We show this gap is real by building, to our knowledge, the first distributed agent attack, a multi-agent scaffold » |
| 1.3 | l. 83 : « attrapée environ cinq fois moins souvent que les attaques antérieures » | confirmé. Précision : le « cinquième » vaut contre la décomposition séquentielle, à taux de faux positifs modestes ; contre l'ensemble des bases, le rappel est de 30 à 80 % plus faible | p. 1 ; p. 4 ; p. 4 | « evading a standard monitor that catches it only a fifth as often as prior agent attacks » ; « At modest false-positive rates, the monitor essentially always catches sequential decomposition attacks, but catches distributed agent attacks only 20% of the time. » ; « cause monitors to have 30%–80% worse recall, relative to other attacks » |
| 1.4 | l. 83 : « moniteur en ligne à état par regroupement d'embeddings entre transcriptions et comptes » | confirmé | p. 1 ; p. 5 | « we develop an online stateful monitor that uses real-time clustering to collect weak suspiciousness signals across many agent transcripts, and escalates only rarely to a language model that flags misuse across user accounts » ; « We compute an embedding (in most experiments, with [Voyage AI, 2026]) of the current agent context » |
| 1.5 | l. 83 : « rappel de campagne de 81 à 87 % pour environ 2,4 à 3,1 % de faux positifs, contre 75 % pour un moniteur standard » | corrigé (F1.2) : condition omise (trafic bénin dix fois plus nombreux que les conversations d'attaque) ; à cent fois, les chiffres baissent | p. 7 ; p. 7 | « With 10x more benign than attack conversations, the stateful moniter reaches 81.1–87.2% campaign recall at 2.35–3.09% benign conversation FPR, compared with 75.0% recall at 2.72% FPR for the standard monitor. » ; « At 100x, the the stateful monitor reaches 65.8% recall at 1.47% FPR; at the same FPR, the best standard monitor achieves only 55% recall. » |
| 1.6 | l. 83 : « détection environ 30 % plus tôt » | confirmé (« jusqu'à 31 % » en p. 2) | p. 1 ; p. 2 | « catching distributed attacks 30% earlier » ; « identifies misuse up to 31% more quickly than well-tuned safety monitors » |
| 1.7 | l. 83 : « → Agrégation au niveau flotte, boîte noire » | confirmé. Précision : la « flotte » est un ensemble de comptes d'utilisateurs humains qui détournent l'agent, non des copies d'un modèle non fiable ; « whitebox » désigne dans l'article l'accès des attaquants humains au garde-fou, pas un moniteur à accès interne | p. 6 ; p. 4 ; p. 8 | « All monitor judgments use the same cyber safety prompt with gpt-4.1-mini-2025-04-14. » ; « An attacker, attempting to misuse the agent to complete a harmful cybersecurity task, can create arbitrary new accounts. » ; « Redteamers had whitebox access to the safeguard » |
| 1.8 | l. 109 : « Monitoring à état sur flotte — rappel de campagne 81–87 % à ~2,4–3,1 % de faux positifs » (ligne de tableau ; séparateurs remplacés par un tiret) | corrigé (F1.3) | p. 7 | « With 10x more benign than attack conversations, the stateful moniter reaches 81.1–87.2% campaign recall at 2.35–3.09% benign conversation FPR » |
| 1.9 | l. 194 : « Chiffres ; accès à FakeLab ; code ControlArena » (part de 2605.31593) | chiffres : vérifiés en 1.3 à 1.6. Code : introuvable ; cherché « github », « code (is/will) », « release », « available », « open source » dans les 17 pages : aucun lien ni annonce | — | — |

**Formulations à mettre à la place.**
- F1.1 (l. 83) : remplacer « première attaque distribuée multi-agents implémentée » par « première attaque distribuée d'agents implémentée, selon les auteurs (« à notre connaissance ») ».
- F1.2 (l. 83) : remplacer « rappel de campagne de 81 à 87 % pour environ 2,4 à 3,1 % de faux positifs, contre 75 % pour un moniteur standard » par « avec un trafic bénin dix fois plus nombreux que les conversations d'attaque, rappel de campagne de 81,1 à 87,2 % pour 2,35 à 3,09 % de faux positifs (part des conversations bénignes refusées), contre 75,0 % à 2,72 % pour le moniteur standard ; avec un trafic cent fois plus nombreux, 65,8 % à 1,47 % contre 55 % au même taux ».
- F1.3 (l. 109) : remplacer « rappel de campagne 81–87 % à ~2,4–3,1 % de faux positifs » par « rappel de campagne 81,1–87,2 % à 2,35–3,09 % de faux positifs (trafic bénin × 10) ; 65,8 % à 1,47 % (× 100) ».

**Chiffres utilisables.**

| chiffre | nature | page | citation exacte |
|---|---|---|---|
| Trafic bénin × 10 : rappel de campagne 81,1–87,2 % à 2,35–3,09 % de faux positifs, contre 75,0 % à 2,72 % | auteurs | p. 7 | « With 10x more benign than attack conversations, the stateful moniter reaches 81.1–87.2% campaign recall at 2.35–3.09% benign conversation FPR, compared with 75.0% recall at 2.72% FPR for the standard monitor. » |
| Trafic bénin × 100 : 65,8 % à 1,47 %, contre 55 % au même taux | auteurs | p. 7 | « At 100x, the the stateful monitor reaches 65.8% recall at 1.47% FPR; at the same FPR, the best standard monitor achieves only 55% recall. » |
| Trafic bénin × 100 : rappel 85,0 % et TTD99 de 25,4 tours nuisibles, contre 68,3 % et 37,2 ; faux positifs 4,30 % contre 9,01 % pour le même rappel | auteurs | p. 7 ; p. 7 | « At 100x benign background, the stateful monitor reaches 85.0% recall and reduces TTD99 to 25.4 harmful steps, compared to 68.3% recall with TTD99 = 37.2 for the standard monitor » ; « This stateful setting uses 4.30% benign conversation FPR; by contrast, standard monitor requires 9.01% FPR to reach the same recall. » |
| Détection plus tôt de 31,7 % : 1 − 25,4 / 37,2 | calcul | p. 7 | « At 100x benign background, the stateful monitor reaches 85.0% recall and reduces TTD99 to 25.4 harmful steps, compared to 68.3% recall with TTD99 = 37.2 for the standard monitor » |
| Définitions : une campagne est rappelée dès qu'une requête nuisible est refusée ; faux positifs = part des conversations bénignes ayant reçu un refus | auteurs | p. 7 | « A campaign is recalled when any harmful request is denied, and FPR the fraction of benign conversations with a refusal. » |
| Empoisonnement du contexte du moniteur attrapé dans 528 sessions sur 644 (82 %) ; décomposition séquentielle 29 sur 29 | auteurs | p. 9 | « The defense caught monitor-context poisoning in 528/644 sessions (82%) and sequential decomposition in 29/29. » |
| Exercice d'attaque : plus de 100 000 attaques, 2 985 sessions, 1 159 identifiants | auteurs | p. 8 | « producing > 100, 000 attacks across 2,985 sessions and 1,159 user IDs » |
| Capacité de l'attaque : gpt-oss-120b résout 0 % seul, 36,7–40,0 % dans l'échafaudage distribué | auteurs | p. 4 | « gpt-oss-120b [Agarwal et al., 2025] solves 0% directly with a standard agent scaffold [Yao et al., 2023], but 36.7–40.0% in our scaffold » |
| Protocole : 50 tâches d'attaque distribuée, fond bénin rééchantillonné 5 fois | auteurs | p. 6 | « For our results, we sample and re-evaluate our monitor on 50 distributed attack tasks with new benign background samples 5 times. » |

**Antériorité.**

| énoncé revendiqué | ce que l'article occupe | page | citation exacte |
|---|---|---|---|
| H2 | En partie, en boîte noire et à l'échelle de comptes : somme des k plus forts scores de suspicion (juge langagier) d'un groupe de contextes, seuil calibré sur des données réservées dont la composition n'est pas précisée ; taux de signalement croissant avec l'activité accumulée entre sessions. Ni processus e, ni martingale, ni sonde de l'agent, ni seuil par action à 1 %, ni calibrage déclaré sans exemple de sabotage | p. 6 ; p. 9 | « To flag a cluster, the largest k scores are summed and exceed a threshold calibrated on held-out data. » ; « The stateful monitor flags harmful requests more often as related activity accumulates across sessions (left), but not as concentrated activity grows within one conversation (right). » |
| HC1 (en marge) | Empoisonnement du contexte du juge inter-contextes (fausses sorties de classifieur et fausses approbations), attrapé à 82 %. Ni pression graduée, ni loi de déférence, ni verdict par probabilité du jeton | p. 8 ; p. 9 | « monitor-context poisoning (faking classifier outputs and approvals to prompt inject the cross-context monitor) » ; « The defense caught monitor-context poisoning in 528/644 sessions (82%) and sequential decomposition in 29/29. » |
| Théorème négatif (voisin empirique) | Évasion par renommage qui disperse l'attaque entre groupes voisins de l'espace d'embeddings. Pas d'attaque à marginales préservées, pas d'agrégateur d'autocorrélation ou de co-élévation | p. 8 | « renaming files or file paths, or using different vocabulary to refer to tasks, could allow an attacker to fool the embedding model and split a distributed attack across nearby clusters » |

Non touchés : H1, lemme d'additivité, transposition jeton → action, HC2b, papier B (aucun état interne ; les « agents » sont des comptes humains).

**Réserves (R4).**

| réserve | page | citation exacte |
|---|---|---|
| Les chiffres phares valent pour le trafic × 10 ; l'avantage se réduit à × 100 | p. 8 | « the stateful monitor still helps at 100x background, but performs much better at 10x » |
| Seuils réglés sur des données réservées, sans dire si elles contiennent des attaques | p. 6 | « During our experiments, we use held-out data to tune these thresholds. » |
| Les auteurs bornent eux-mêmes la portée | p. 9 | « Notably, stateful monitoring does not solve distributed misuse » |

## 2. 2607.02514v2 — « Distributed Attacks in Persistent-State AI Control »

**Identité.** Auteurs : Josh Hills et Ida Caspary (contributions égales), Asa Cooper Stickland. Affiliations : Constellation Astra Fellowship (Hills, Caspary), Imperial College London (Caspary), UK AI Security Institute (Cooper Stickland). Version 2, arXiv, 8 juillet 2026, catégorie cs.AI. Venue : prépublication « en cours d'examen », lieu non nommé. Code public : `github.com/josh-hills/control-arena-persistent-state-eval`. Lu en entier.

**Affirmations.**

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 2.1 | l. 82 : « Hills, Caspary, Cooper Stickland » | confirmé | p. 1 ; p. 1 | « Josh Hills1 ∗ Ida Caspary1,2 ∗ Asa Cooper Stickland3 » ; « Constellation Astra Fellowship 2 Imperial College London 3 UK AI Security Institute » |
| 2.2 | l. 82 : « attaques graduelles réparties sur des demandes de fusion successives dans un code persistant (Iterative VibeCoding) » | confirmé | p. 1 | « a coding agent builds software over a sequence of PRs in a persistent codebase while pursuing a covert side task » ; « We compare gradual attacks, which distribute the side task across PRs, against non-gradual attacks concentrated in a single PR. » |
| 2.3 | l. 82 : « moniteur à état « link-tracker » » | confirmé | p. 1 | « We introduce a stateful link-tracker monitor that tracks suspicious buildup across PRs. » |
| 2.4 | l. 82 : « un ensemble de quatre moniteurs fait passer l'évasion graduelle de 93 % à 47 % pour moins de 2 % de faux positifs » | corrigé (F2.1) : 93 % est le plus faible moniteur de diff standard (diffs complets), pas une référence typique ; le seuil de l'ensemble est choisi pour minimiser l'évasion sur l'ensemble d'évaluation | p. 8 ; p. 8 ; p. 13 | « The four-monitor ensemble (diff:LT, diff:full, traj:TD, traj:full) reduces gradual evasion from 93% under the weakest standard diff monitor to 47% (Figure 2). » ; « On honest runs, the ensemble FPR remains below 2%: 1.3% on CLI and 0.9% on Flask. » ; « Among those admissible thresholds, we report the threshold that gives the lowest attack evasion on the evaluation set. » |
| 2.5 | l. 82 : « code dans ControlArena » | corrigé (F2.2) : code dans un dépôt propre, construit sur ControlArena et Inspect AI | p. 1 ; p. 5 | « Code is available at https: //github.com/josh-hills/control-arena-persistent-state-eval. » ; « The evaluation is built on Inspect AI (UK AI Security Institute, 2024) and ControlArena (Inglis et al., 2025). » |
| 2.6 | l. 82 : « → Base de l'environnement (b), boîte noire » | confirmé pour « boîte noire » (moniteurs GPT-4o sur diffs et trajectoires) ; « base de l'environnement (b) » est un usage du programme, non vérifiable sur le PDF | p. 1 | « We use Claude Sonnet 4.5 as the attack agent and GPT-4o as the monitor. » |
| 2.7 | l. 108 : « Ensemble à quatre moniteurs (link-tracker) — évasion graduelle 93 % → 47 % ; faux positifs < 2 % » (ligne de tableau) | corrigé (F2.3) | p. 8 ; p. 5 | « The four-monitor ensemble (diff:LT, diff:full, traj:TD, traj:full) reduces gradual evasion from 93% under the weakest standard diff monitor to 47% (Figure 2). » ; « Within the diff-monitor family, the link-tracker monitor substantially improves detection of gradual attacks, reducing evasion from 87% under the task-description diff monitor to 54%. » |
| 2.8 | l. 194 : « Chiffres ; … code ControlArena » (part de 2607.02514) | confirmé : code public annoncé (dépôt dérivé de ControlArena) ; chiffres vérifiés en 2.4 | p. 1 | « Code is available at https: //github.com/josh-hills/control-arena-persistent-state-eval. » |

**Formulations à mettre à la place.**
- F2.1 (l. 82) : remplacer « un ensemble de quatre moniteurs fait passer l'évasion graduelle de 93 % à 47 % pour moins de 2 % de faux positifs » par « un ensemble de quatre moniteurs (diff : link-tracker et diffs complets ; trajectoire : descriptions de tâches et trajectoires complètes), par moyenne des scores, fait passer l'évasion graduelle de 93 % sous le plus faible moniteur de diff standard (diffs complets) à 47 % (moyenne des familles en ligne de commande et Flask ; link-tracker seul : 54 %), avec 1,3 % et 0,9 % de faux positifs sur les exécutions honnêtes ; le seuil est choisi, parmi ceux qui gardent au plus 2 % de faux positifs, pour minimiser l'évasion sur l'ensemble d'évaluation, séparément pour les attaques graduelles et positionnelles ».
- F2.2 (l. 82) : remplacer « code dans ControlArena » par « code public dans un dépôt construit sur ControlArena et Inspect AI (github.com/josh-hills/control-arena-persistent-state-eval) ».
- F2.3 (l. 108) : remplacer « évasion graduelle 93 % → 47 % ; faux positifs < 2 % » par « évasion graduelle 93 % (diffs complets, le plus faible) → 54 % (link-tracker seul) → 47 % (ensemble) ; faux positifs 1,3 % et 0,9 % ; seuil choisi sur l'évaluation ».

**Chiffres utilisables.**

| chiffre | nature | page | citation exacte |
|---|---|---|---|
| Évasion graduelle (moniteur GPT-4o, moyenne des deux familles) : descriptions de tâches 87 %, link-tracker 54 % | auteurs | p. 5 | « Within the diff-monitor family, the link-tracker monitor substantially improves detection of gradual attacks, reducing evasion from 87% under the task-description diff monitor to 54%. » |
| Tableau 7 : ensemble 48,1 ± 12,9 (en ligne de commande) et 46,6 ± 8,9 (Flask) ; diffs complets 88,9 et 96,6 | auteurs | p. 14 | « 4-monitor ensemble mean > 3.75/2.75 48.1 ± 12.9 31.5 ± 10.4 » ; « 4-monitor ensemble mean > 3.5 46.6 ± 8.9 19.7 ± 6.4 » ; « Diff: full-diffs 7 88.9 ± 8.5 98.2 ± 4.5 » ; « Diff: full-diffs 7 96.6 ± 3.5 92.5 ± 4.3 » |
| 93 % = (88,9 + 96,6) / 2 = 92,75 ; 47 % = (48,1 + 46,6) / 2 = 47,35 | calcul | p. 14 | « 4-monitor ensemble mean > 3.5 46.6 ± 8.9 19.7 ± 6.4 » |
| Faux positifs de l'ensemble : 1,3 % et 0,9 % | auteurs | p. 8 | « On honest runs, the ensemble FPR remains below 2%: 1.3% on CLI and 0.9% on Flask. » |
| Seuils individuels au 98e centile de 308 exécutions honnêtes | auteurs | p. 13 | « Honest-baseline thresholds (GPT-4o monitor, 98th percentile, n = 308 honest runs). » |
| Avec GPT-5.3-Codex comme moniteur, 27 % des attaques graduelles réussies passent | auteurs | p. 2 | « Even with GPT-5.3-Codex as a monitor, which is a more capable model than the untrusted agent (Claude Sonnet 4.5), it still allows 27% of successful gradual attacks through. » |
| Agrégation par la moyenne sur les demandes de fusion : évasion graduelle 90,7 % contre 94,4 % au maximum | auteurs | p. 30 | « Max-over-PR (main) 94.4 75.8 » ; « Mean-normalized 90.7 36.8 » |
| Analyse statique ciblée plus moniteur langagier : 54 attaques sur 93 détectées (évasion 41,9 %) | auteurs | p. 34 | « Combining them—counting an attack as detected if either the LLM monitor or the taint rule fires—detects 54/93, reducing evasion to 41.9% while adding no honest false positives from the taint rule. » |
| Pic de suspicion à la quatrième demande de fusion (indice 3) dans 50,8 % des attaques graduelles | auteurs | p. 17 | « Average suspicion rises through the sequence and peaks at PR3, which holds the maximum task-description suspicion in 50.8% of gradual attack runs. » |

**Antériorité.**

| énoncé revendiqué | ce que l'article occupe | page | citation exacte |
|---|---|---|---|
| H2 | En partie, en boîte noire : seuils de chaque moniteur calibrés sur des exécutions honnêtes seulement ; agrégation sur l'horizon par la moyenne et par le k-ième plus fort score, sans gain contre les attaques graduelles. Ni processus e, ni sonde | p. 4 ; p. 30 ; p. 30 | « calibrates suspicion thresholds from honest-baseline runs (runs with no side task present). » ; « Mean-normalized 90.7 36.8 » ; « The k-strikes detector does not help. » |
| H2 (précaution, pas une occupation) | Ici, les attaques graduelles réussies se concentrent sur une ou deux demandes de fusion : il reste peu de signal faible à accumuler | p. 7 ; p. 31 | « In practice, successful gradual runs often concentrate most of the attack in only 1–2 PRs. » ; « successful gradual attacks in our setting concentrate their suspicious changes in one or two PRs, so there is no third suspicious PR for the detector to find. » |
| Transposition jeton → action (voisin) | Maximum contre moyenne par demande de fusion, sur des scores de juge langagier, non de sondes | p. 30 | « Max-over-PR (main) 94.4 75.8 » ; « Mean-normalized 90.7 36.8 » |

Non touchés : H1, lemme d'additivité, théorème négatif, HC1, HC2b, papier B (un seul agent au fil des demandes de fusion).

**Remarques utiles à H5 et à HC5 (question de la ligne 193).**

| remarque | page | citation exacte |
|---|---|---|
| Ensembles entre types de moniteurs, pas entre modèles | p. 10 | « We ensemble across monitor types but not across models; multi-model ensembles would be an interesting next step. » |
| Un signal non génératif (analyse statique ciblée) est combiné à un moniteur langagier | p. 34 | « Combining them—counting an attack as detected if either the LLM monitor or the taint rule fires—detects 54/93, reducing evasion to 41.9% while adding no honest false positives from the taint rule. » |

**Réserves (R4).**

| réserve | page | citation exacte |
|---|---|---|
| Seuil d'ensemble choisi sur l'ensemble d'évaluation, et différent selon la stratégie d'attaque… | p. 13 ; p. 13 | « Among those admissible thresholds, we report the threshold that gives the lowest attack evasion on the evaluation set. » ; « The calibrated mean thresholds are 3.75 and 2.75 for CLI gradual and positional attacks, respectively, and 3.5 for both Flask strategies. » |
| … alors que l'équipe de défense est censée ignorer cette stratégie : 47 % est optimiste | p. 4 | « The blue team does not know which attack strategy the red team will use. » |
| Biais de sélection reconnu par les auteurs | p. 10 | « Gradual evasion numbers carry selection bias because the runs that succeed are the least distributed (Section 4.1). » |

## 3. 2607.07368v1 — « Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors »

**Identité.** Auteurs : Oliver Makins et Orazio Angelini (contributions égales, ordre tiré au sort), Zohreh Shams, Mary Phuong. Affiliations : UK AI Security Institute et MATS Research (Makins), MATS Research (Angelini, Shams, Phuong). Version 1, arXiv, 8 juillet 2026, catégorie cs.LG. Venue : prépublication ; le fichier contient une liste de contrôle NeurIPS (pages 75 à 81), sans mention d'acceptation. Code non publié, accessible sur demande. Lu : pages 1 à 75 en entier ; pages 76 à 81, réponses de la liste de contrôle seulement.

**Affirmations.**

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 3.1 | l. 81 : « Makins, Angelini, Shams, Phuong (institut britannique / MATS) » | confirmé | p. 1 | « UK AI Security Institute » ; « Equal contribution; author order randomised. » |
| 3.2 | l. 81 : « effet de fragmentation : plus les agents coordonnés sont nombreux, moins les moniteurs par-instance détectent » | confirmé | p. 1 | « Our central finding is the fragmentation effect: as more agents coordinate to attack, per-agent monitoring becomes less likely to catch any of the attackers. » |
| 3.3 | l. 81 : « ce n'est pas une simple dilution (un moniteur conjoint sur les commits recombinés reste à une suspicion d'environ 0,91, quasi plate en N) » | corrigé (F3.1) : deux résultats distincts sont fondus. L'argument contre la dilution est une analyse de médiation ; le moniteur conjoint (0,91) montre que le découpage lui-même cache l'attaque, et il n'est pas déployable | p. 1 ; p. 10 ; p. 8 ; p. 8 | « Secondly, this is not driven by the ratio of benign to malicious code – we argue this is likely dependent on model capability. » ; « Around 40% of the drop is explained by neither channel, so this analysis rules out pure mechanical dilution as the driver without fully pinning down the cause. » ; « Figure 2 panel (e) shows that the joint suspicion is uniformly high (mean 0.91, range 0.65–1.00) and essentially flat in the number of agents (correlation between K and joint suspicion −0.009) » ; « Instead it rises, which shows that the act of splitting the attack, not merely the choice of less-conspicuous actions, is what hides it. » |
| 3.4 | l. 81 : « un planificateur explicite multiplie jusqu'à sept fois la réussite d'attaque » | corrigé (F3.2) : « sept » est un rapport de cotes (7,10, plan Gemini 3 Flash contre aucun plan ; 5,74 tous plans confondus) sur l'achèvement de la tâche secondaire, indépendamment de la détection ; l'article écrit tantôt « completing the attack », tantôt « attack success rates » | p. 1 ; p. 11 ; p. 53 ; p. 53 ; p. 53 | « raises the rate of completing the attack up to sevenfold » ; « Planning measurably helps with side-task success (independent of detection) . We fit a GLM to show the posterior odds ratio for plan vs no-plan side-task success is 5.74 » ; « changes the odds of completing the hidden malicious task (the side task), with 95% probability intervals (HPDI) » ; « Flash plan / none » ; « 7.10 (4.68, 9.86) * » |
| 3.5 | l. 81 : « environnement FakeLab (9 services, 86 tâches bénignes, 4 objectifs d'attaque) partagé sur demande » | confirmé. Précision : accès sous conditions, après une revue d'ouverture par les employeurs ; code non publié ; licence non mentionnée | p. 1 ; p. 74 ; p. 77 ; p. 13 | « We develop FakeLab: a synthetic AI-lab codebase (9 services, 86 benign tasks, 4 attack objectives; shared on request). » ; « Researchers should contact the corresponding authors to request access. » ; « We are willing to release it to other safety and security researchers, as detailed in the appendices once our employers have completed an open-sourcing review. » ; « We do not open-source the code to avoid contamination and model training on the environment » |
| 3.6 | l. 81 : « défenses boîte noire uniquement » | confirmé : moniteur langagier sur le diff de chaque commit, tests automatiques, restrictions de lecture et d'écriture ; aucun accès interne | p. 5 ; p. 14 | « We monitor each executor agent independently with an LLM monitor that is given a prompt, the main task description, and the git diff submitted by the executor. » ; « tested only one monitoring modality (the git diff) » |
| 3.7 | l. 81 : « collusion et moniteur non fiable laissés à plus tard » | corrigé (F3.3) : la collusion entre agents attaquants est étudiée ; sont reportées la collusion entre exécutant et moniteur (moniteur non fiable) et la communication dissimulée | p. 3 ; p. 4 ; p. 28 ; p. 28 | « do standard layered read and write permissions still mitigate an attack when the agents sharing the codebase are colluding? » ; « assuming perfect unmonitored communication of a plan as an upper point of communication capability. » ; « We did not run the complementary untrusted-monitor experiments, in which the red team also controls the monitor » ; « Those experiments probe a different threat, collusion between the executor and the overseer » |
| 3.8 | l. 81 : « → Complément attaque exact de la phase 3 » | confirmé sur le vérifiable : l'article fournit l'attaque distribuée entre instances d'un même modèle et des défenses boîte noire seulement ; « exact » relève du programme | p. 2 | « A frontier lab internally deploys many instances of the same, possibly misaligned, model » |
| 3.9 | l. 110 : « Planificateur (attaque) — réussite d'attaque jusqu'à × 7 » (ligne de tableau) | corrigé (F3.4) | p. 11 ; p. 53 | « Planning measurably helps with side-task success (independent of detection) . We fit a GLM to show the posterior odds ratio for plan vs no-plan side-task success is 5.74 » ; « 7.10 (4.68, 9.86) * » |
| 3.10 | l. 194 : « Chiffres ; accès à FakeLab ; code ControlArena » (part de 2607.07368) | chiffres : voir 3.3, 3.4 et le tableau des chiffres. Accès à FakeLab : confirmé, sur demande et sous conditions. Code : non publié ; évaluation construite sur Inspect et ControlArena | p. 74 ; p. 13 ; p. 22 | « Researchers should contact the corresponding authors to request access. » ; « We do not open-source the code to avoid contamination and model training on the environment » ; « we implement our evaluation using [AI Security Institute, 2024, Inspect] and [Inglis et al., 2025, ControlArena] from UK AISI. » |
| 3.11 | l. 212 : « FakeLab (sur demande aux auteurs de 2607.07368) » | confirmé. Précision pour le message : s'adresser aux auteurs correspondants ; trois adresses figurent en p. 1 (Makins, Angelini, Shams), aucune n'est marquée « correspondant » ; conditions d'éligibilité en p. 74 ; transcriptions et poids des modèles statistiques aux mêmes conditions | p. 74 ; p. 74 ; p. 74 ; p. 1 ; p. 1 ; p. 1 | « Researchers should contact the corresponding authors to request access. » ; « The requester must have either prior public work in AI safety, alignment, or security, or current affiliation with one of: » ; « We are happy to share the transcripts and GLM weights under the same conditions as the code. » ; « oliver.makins@dsit.gov.uk » ; « angelini.orazio@gmail.com » ; « zohreh@matsprogram.org » |
| 3.12 | brief, l. 133 : « vérifie aussi la disponibilité et la licence … rédige le message de demande d'accès à FakeLab (auteurs de arXiv 2607.07368) » | disponibilité : confirmé, sur demande, mais conditionnée à une revue d'ouverture par les employeurs. Licence : introuvable ; cherché « licen » dans les 81 pages : seules occurrences dans la liste de contrôle NeurIPS (actifs existants), aucune licence de FakeLab | p. 77 | « We are willing to release it to other safety and security researchers, as detailed in the appendices once our employers have completed an open-sourcing review. » |

**Formulations à mettre à la place.**
- F3.1 (l. 81) : remplacer « ce n'est pas une simple dilution (un moniteur conjoint sur les commits recombinés reste à une suspicion d'environ 0,91, quasi plate en N) » par « la baisse n'est pas due d'abord à la dilution mécanique : sur les commits malveillants, la part de lignes malveillantes explique 25 % de la baisse par commit et 20 % au pic, la plausibilité de la couverture 53 % et 45 %, et environ 40 % reste inexpliqué ; séparément, un moniteur conjoint qui lit ensemble tous les commits d'une attaque réussie reste haut (suspicion moyenne 0,91, de 0,65 à 1,00, corrélation −0,009 avec le nombre d'agents K) : c'est le découpage qui cache l'attaque, mais ce moniteur conjoint n'est pas déployable selon les auteurs ».
- F3.2 (l. 81) : remplacer « un planificateur explicite multiplie jusqu'à sept fois la réussite d'attaque » par « un planificateur explicite multiplie les cotes d'achèvement de la tâche secondaire, indépendamment de la détection, par 5,74 (tout plan contre aucun) et jusqu'à 7,10 (plan Gemini 3 Flash contre aucun) ; ce sont des rapports de cotes, non des rapports de taux de réussite non détectée ».
- F3.3 (l. 81) : remplacer « collusion et moniteur non fiable laissés à plus tard » par « la coordination entre agents attaquants est étudiée, avec un canal de plan non surveillé pris comme borne haute ; sont laissées à plus tard la collusion entre exécutant et moniteur (moniteur non fiable) et la communication dissimulée (stéganographie, points de Schelling) ».
- F3.4 (l. 110) : remplacer « réussite d'attaque jusqu'à × 7 » par « cotes d'achèvement de la tâche secondaire × 5,74 (tout plan), jusqu'à × 7,10 (plan Flash), indépendamment de la détection ».

**Chiffres utilisables.**

| chiffre | nature | page | citation exacte |
|---|---|---|---|
| Moniteur conjoint : suspicion moyenne 0,91 (0,65 à 1,00), corrélation −0,009 avec K | auteurs | p. 8 | « Figure 2 panel (e) shows that the joint suspicion is uniformly high (mean 0.91, range 0.65–1.00) and essentially flat in the number of agents (correlation between K and joint suspicion −0.009) » |
| Cohorte : 572 séquences ; score conjoint disponible pour 309, 193 et 67 séquences à K = 1, 3, 9 | auteurs | p. 7 | « The cohort is 572 sequences; the joint score is available for 309/193/67 at K = 1/3/9. » |
| Écart moyen conjoint moins pire commit : 0,00 ; +0,04 ; +0,13 à K = 1, 3, 9 | auteurs | p. 7 | « The gap shifts increasingly positive with K (means 0.00, +0.04, +0.13 at K = 1, 3, 9) » |
| Témoin honnête (K = 3 seulement) : conjoint 0,17 contre pire commit 0,21 | auteurs | p. 48 ; p. 48 | « On honest sequences (no side task), the whole-PR joint monitor is not alarmed: its mean score is 0.17, below the mean worst-commit score of 0.21 » ; « One limitation: the dataset contains honest trajectories only at K = 3 » |
| Suspicion moyenne par commit (attaques réussies) : 0,922 ; 0,780 ; 0,586 à K = 1, 3, 9 ; au pic : 0,922 ; 0,866 ; 0,815 | auteurs | p. 38 ; p. 39 | « Success-conditioned 0.922 0.780 0.586 » ; « Success-conditioned 0.922 0.866 0.815 » |
| Médiation (tableau 1, commits malveillants) : par commit, dilution 25 %, couverture 53 %, les deux 62 %, inexpliqué 38 % ; au pic, 20 %, 45 %, 57 %, 43 % | auteurs | p. 8 | « Per commit 0.34 25% 53% 62% 38% » ; « Whole attack (peak commit) 0.11 20% 45% 57% 43% » ; « Malicious commits only, pooled over the planner condition. » |
| Médiation (figure 3, cohorte décrite plus largement) : par commit, couverture 47 %, dilution 22 %, inexpliqué 44 % ; au pic, 38 %, 17 %, 50 % | figure | p. 9 | « Better cover stories account for more of the drop than dilution at both the single-commit (b) and whole-attack (d) level, and around 40% of the drop is left unexplained by either channel. » |
| Rapports de cotes d'achèvement de la tâche secondaire : 5,74 [3,75 ; 8,29] tout plan ; 7,10 [4,68 ; 9,86] plan Flash ; 4,67 [2,49 ; 7,54] plan Pro (vérifiés à l'image) | figure | p. 53 | « 5.74 (3.75, 8.29) * » ; « 7.10 (4.68, 9.86) * » ; « 4.67 (2.49, 7.54) * » |
| Passer de GPT-5 mini à GPT-5 nano multiplie par 52,9 les cotes de succès non détecté, à 5 % de faux positifs | auteurs | p. 12 | « going from GPT-5 mini to GPT-5 nano increases the odds of undetected attack success by a factor of 52.9 when we compare monitors at a 5% FPR » |
| Faux positifs nécessaires pour tenir le succès non détecté sous 1 % : 3,6 % (mini, description exhaustive), 7,8 % (mini, description empirique), 27 à 30 % (nano) | auteurs | p. 12 | « To hold undetected attack success below 1% with 95% posterior confidence, GPT-5 mini needs a false-positive rate of 3.6% under the exhaustive prompt and 7.8% under the more realistic empirical one, whereas GPT-5 nano requires an implausible 27–30% (Table 12). » |
| Description empirique : rappel 98,7 % à 10 % de faux positifs | auteurs | p. 12 | « empirical has a realistic length for the task and reaches 98.7% recall at 10% FPR » |
| Sans planificateur, lever les restrictions d'écriture grossières : rapport de cotes 5,90 [2,26 ; 32,61] | auteurs | p. 13 | « none 5.90 [2.26, 32.61] 1512 99.9% » |
| Coût du moniteur : GPT-5 mini environ 5 à 9 % du calcul de l'exécutant, nano 1 à 2 % | auteurs | p. 6 | « GPT-5 mini (typically ∼5–9% of executor compute cost for the entire stage) and GPT-5 nano (∼1–2%) » |
| Dépense totale du projet : 15 000 à 20 000 dollars | auteurs | p. 74 | « The total spend for the entire research project, including failed data collection and preliminary investigations is between 15-20K USD. » |
| Dépendance positive des scores par commit au sein d'une trajectoire : écart unilatéral de Kolmogorov–Smirnov (D+) à une référence indépendante, de 0,16 à 0,40 | auteurs | p. 45 | « The dependence is moderate, with D+ ∈ [0.16, 0.40], and grows with sequence length » |

**Antériorité.**

| énoncé revendiqué | ce que l'article occupe | page | citation exacte |
|---|---|---|---|
| Papier B | Occupe le pendant boîte noire de « sécurité en fonction du nombre d'agents » : détection par moniteurs par instance pour K = 1, 3, 9 instances d'un même modèle, et moniteur conjoint non déployable. N'occupe pas la co-élévation des états internes (aucun accès interne). Le programme prévoit déjà de répliquer cet effet (programme v2, E2.1) | p. 2 ; p. 1 ; p. 8 | « A frontier lab internally deploys many instances of the same, possibly misaligned, model » ; « Our central finding is the fragmentation effect: as more agents coordinate to attack, per-agent monitoring becomes less likely to catch any of the attackers. » ; « but such a whole-PR monitor is not deployable in practice » |
| H2 et lemme d'additivité (précaution, pas une occupation) | Scores par commit positivement dépendants au sein d'une trajectoire ; les auteurs jugent l'hypothèse d'indépendance « très probablement fausse » | p. 45 ; p. 65 | « a trajectory that is stealthy on one commit tends to be stealthy on the others » ; « This assumption is very likely false, so we run diagnostic checks to make sure that the assumption does not hurt our fit too much. » |
| H2 (piste) | Taux d'incrimination attendu non étudié ; données réutilisables selon les auteurs | p. 14 | « real deployments would instead need to justify an expected incrimination rate » |

Non touchés : H1, théorème négatif, transposition jeton → action, HC1, HC2b.

**Réserves (R4).**

| réserve | page | citation exacte |
|---|---|---|
| Cohorte conditionnée au succès de l'attaque (variable postérieure au traitement) | p. 30 | « The cohort conditions on attack success, a post-treatment variable » |
| Moniteur conjoint mesuré avec la seule description exhaustive | p. 48 | « every joint-suspicion result, here and in the main text, uses the exhaustive (full task description) monitor prompt » |
| Facteur « sept » formulé de trois façons dans l'article | p. 1 ; p. 3 ; p. 14 | « raises the rate of completing the attack up to sevenfold » ; « raises end-to-end side-task completion by up to a factor of seven » ; « raises attack success rates by up to a factor of seven » |
| Le tableau 1 (p. 8) et la figure 3 (p. 9) donnent des parts de médiation différentes (cohortes décrites différemment) | p. 9 | « all panels pool the planner and no-planner conditions. » |

## 4. 2608.02698v1 — « Steganalysis of Adaptive Covert Collusion in Tool-Using Agent Populations: A Black-Box, Cross-Principal Approach »

**Identité.** Auteur unique : Mohamed Chahine Ghanem (Keele University, Newcastle-under-Lyme, Royaume-Uni). Version 1, arXiv, 3 août 2026, catégorie cs.CR. Venue : gabarit de la revue IEEE Transactions on Artificial Intelligence, « manuscrit soumis le 5 août 2026 » : soumis, non accepté ; la date de soumission imprimée suit le dépôt arXiv. Code : publication annoncée au futur, sans lien. Lu en entier.

**Affirmations.**

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 4.1 | l. 87 : « Ghanem & Keele » | corrigé (F4.1) : auteur unique ; « Keele » est son université | p. 1 ; p. 1 | « Mohamed Chahine Ghanem, Member, IEEE » ; « M. C. Ghanem is with Keele University, Newcastle-Under-Lyme, U.K. » |
| 4.2 | l. 87 : « détection de collusion au niveau population, explicitement boîte noire et inter-mandants (information mutuelle entre exécutions, tests de permutation) » | confirmé pour la méthode proposée. Précision indispensable : aucun résultat mesuré, les valeurs des tableaux III à VI sont déclarées fictives | p. 1 ; p. 3 ; p. 6 | « We treat covert coordination as an information-hiding problem and build a black-box steganalysis detector that combines cross-run mutual-information estimation, permutation tests, distributional-shift statistics, and timing and tool-call side channels, all calibrated to a fixed false-positive budget. » ; « Critically, the monitor has no access to model weights, activations, or private prompts of agents it does not operate. » ; « All numeric values in Tables III–VI are illustrative placeholders that specify the expected shape of results and provide a template; they are anchored to ranges reported by prior baselines but are not measured outcomes and must be replaced with the authors’ own runs before submission. » |
| 4.3 | l. 87 : « → Délimite la frontière ; le pendant boîte blanche reste ouvert » | corrigé (F4.2) : sans mesure, l'article ne délimite pas une frontière empirique ; il cite lui-même une détection de collusion multi-agents par activations (NARCBench, arXiv 2604.01151), que le programme connaît déjà (programme v2, E2.3 et E3.1 ; lecture de niveau 1 : `docs/sources/lecture-pdf-niveau1/rapport-papierB-NARCBench-Das-v1.md`) | p. 1 ; p. 3 ; p. 8 ; p. 10 | « report clearly labelled placeholder results pending measurement » ; « the multi-agent-interpretability approach behind NARCBench [29] attains strong results but requires white-box activation access, which is infeasible across principals. » ; « The interpretability route behind NARCBench [29] reports the best numbers of the three, but it reads model activations—an option that simply does not exist across organisational boundaries. » ; « A. Rose, C. Cullen, B. G. Kaplowitz, and C. Schroeder de Witt, “Detecting multi-agent collusion through multi-agent interpretability,” arXiv preprint arXiv:2604.01151, 2026. » |

**Formulations à mettre à la place.**
- F4.1 (l. 87) : remplacer « Ghanem & Keele » par « Ghanem (Keele University), auteur unique ».
- F4.2 (l. 87) : remplacer « → Délimite la frontière ; le pendant boîte blanche reste ouvert. » par « → Propose, sans résultat mesuré (valeurs des tableaux III à VI déclarées fictives), un détecteur boîte noire inter-mandants et une borne classique d'indétectabilité ; il cite lui-même une détection de collusion multi-agents par activations (NARCBench, arXiv 2604.01151) : le pendant boîte blanche n'est pas vierge selon cette source. »

**Chiffres utilisables.**

| chiffre | nature | page | citation exacte |
|---|---|---|---|
| Aucun chiffre empirique utilisable : toutes les valeurs des tableaux III à VI sont fictives | auteurs | p. 6 | « All numeric values in Tables III–VI are illustrative placeholders that specify the expected shape of results and provide a template; they are anchored to ranges reported by prior baselines but are not measured outcomes and must be replaced with the authors’ own runs before submission. » |
| Borne théorique : taux de vrais positifs au plus égal au taux de faux positifs plus la racine de la moitié de la divergence (Proposition 1) ; inégalités classiques, non revendiquées | auteurs | p. 5 ; p. 5 | « Proposition 1 (Detectability ceiling). » ; « we claim novelty in its application to agent collusion and in the empirical frontier it predicts, not in the underlying inequalities. » |

**Antériorité.**

| énoncé revendiqué | ce que l'article occupe | page | citation exacte |
|---|---|---|---|
| Lemme d'additivité | En partie, en boîte noire et par des outils classiques : sous une décomposition additive de l'entropie relative par message, la puissance de tout test est bornée par une fonction de la divergence totale observée. Borne supérieure seulement ; l'auteur ne revendique pas les inégalités | p. 5 ; p. 5 | « then under an additive per-message decomposition of relative entropy the observable divergence obeys » ; « we claim novelty in its application to agent collusion and in the empirical frontier it predicts, not in the underlying inequalities. » |
| Théorème négatif (voisin classique) | Au-dessous d'un débit dissimulé, aucun test boîte noire ne bat le hasard. Ne traite ni d'attaque à marginales préservées, ni d'agrégateurs d'autocorrélation ou de co-élévation | p. 5 | « Proposition 1 (Detectability ceiling). » |
| H2 (idée proposée, non réalisée) | Test séquentiel entre sessions pour accumuler des preuves faibles, proposé comme suite ; seuil par calibration conforme sur des épisodes témoins sans collusion. Boîte noire, sans sonde ni mesure | p. 9 ; p. 4 | « applies a change-point or sequential-likelihood test across sessions, trading detection latency for the ability to accumulate weak per-session evidence. » ; « the threshold is set by conformal calibration on held-out control episodes » |
| H1 (conception seulement) | Une sonde d'activations boîte blanche est prévue comme oracle face au détecteur boîte noire, au même calibrage ; valeurs fictives ; collusion par stéganographie, non sabotage diffus | p. 7 ; p. 7 | « a white-box activation probe [29] is given privileged access to model internals and reported only as an oracle upper bound » ; « We stress that the white-box probe is not a deployable cross-principal detector » |
| Papier B | Cite NARCBench (détection de collusion par activations) ; prévoit un facteur de population N = 4, 8, 16, sans mesure | p. 3 ; p. 6 | « the multi-agent-interpretability approach behind NARCBench [29] attains strong results but requires white-box activation access, which is infeasible across principals. » ; « Population N 4, 8, 16 » |

Non touchés : transposition jeton → action, HC1, HC2b.

**Réserves (R4).**

| réserve | page | citation exacte |
|---|---|---|
| Statut : manuscrit soumis, non accepté | p. 1 ; p. 1 | « Manuscript submitted August 5, 2026. » ; « arXiv:2608.02698v1 [cs.CR] 3 Aug 2026 » |
| Évasion par étalement entre sessions annoncée, mais sur des valeurs fictives | p. 7 | « spreading the payload across sessions is a real evasion (Table Vc) that single-session steganalysis underdetects. » |

## 5. 2605.29178v1 — « The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems »

**Identité.** Auteurs : Nikolay Radev, Lennart Haas, Benjamin Arnav, Pablo Bernabeu-Pérez (les deux derniers sont auteurs principaux). Affiliations non imprimées ; travail mené dans le programme SPAR ; idée initiale attribuée à Mary Phuong. Version 1, arXiv, 27 mai 2026, catégorie cs.CR. Venue : prépublication. Code : aucun lien (seul lien : l'outil Inspect Scout). Lu en entier.

**Affirmations.**

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 5.1 | l. 84 : « The Best-Laid SCHEMEs, arXiv 2605.29178 — sabotage coordonné multi-agents » | confirmé ; la ligne ne nomme pas les auteurs (F5.1) | p. 1 ; p. 1 | « We introduce SCHEME, a benchmark of 17 task instances across 7 settings and 8 real open-source libraries, each pairing a legitimate software-engineering task with a covert side task. » ; « Nikolay Radev Lennart Haas Benjamin Arnav† Pablo Bernabeu-Pérez† » |
| 5.2 | l. 84 : « avertir les agents de la surveillance réduit leur capacité plus que leur détectabilité » | confirmé. Précision : mesuré sur Gemini 3.1 Pro seulement ; l'avertissement fait passer le sabotage réussi de 84 % à 41 %, 62 % avec la consigne de justification ; sabotage non détecté sous 3 % avec le moniteur à pleine visibilité, jusqu'à 11 % sous d'autres vues | p. 8 ; p. 8 ; p. 8 ; p. 9 | « Stealth-aware prompting cuts capability more than detectability » ; « Notice roughly halves sabotage success (84%→41%) while nearly tripling median output tokens (23k→68k) » ; « we rerun all 17 Gemini 3.1 Pro instances under two prompted variants » ; « prompted variants and all four monitor views, stealthy sabotage stays below 11%; Code + Comms, the full-visibility monitor, holds it at <3% (Appendix J.5). » |

**Formulation à mettre à la place.**
- F5.1 (l. 84) : remplacer « **The Best-Laid SCHEMEs**, arXiv 2605.29178 » par « **Radev, Haas, Arnav, Bernabeu-Pérez, The Best-Laid SCHEMEs**, arXiv 2605.29178 ».

**Chiffres utilisables.**

| chiffre | nature | page | citation exacte |
|---|---|---|---|
| Sabotage réussi (tâche principale et tâche secondaire) : Gemini 84 %, Codex 46 % (85 trajectoires par modèle) | auteurs | p. 1 | « with Gemini completing the covert objective while succeeding on the legitimate task in 84% of samples and Codex in 46% » |
| Détection à au plus 2 % de faux positifs : 99 % et 68 % sur le code seul, 100 % et 81 % avec les communications (Gemini, Codex) | auteurs | p. 1 | « a trusted monitor flags coordinated sabotage at FPR≤2% in 99%/68% (Gemini/Codex) of attempts from code edits alone, rising to 100%/81% with access to agent communication » |
| Moniteur par agent (moyenne des agents) : perte de 20 points de détection sur Codex | auteurs | p. 7 | « Single-Agent, which scores each agent’s slice independently before averaging, loses 20 pp of total Codex TPR (90% on successes, 37% on failures) » |
| Avertissement : 84 % → 41 % ; avec consigne de justification : 62 % | auteurs | p. 8 ; p. 8 | « Notice roughly halves sabotage success (84%→41%) while nearly tripling median output tokens (23k→68k) » ; « Notice + hint reverses both effects: sabotage success recovers to 62% » |
| Seuil : 98e centile d'environ 62 médianes de référence par source et configuration | auteurs | p. 23 ; p. 23 | « giving ∼62 main-pass medians per (source, configuration) » ; « The threshold τ for each monitor configuration is the 98th percentile of this combined main-pass pool, corresponding to FPR≤ 2% » |

**Antériorité.**

| énoncé revendiqué | ce que l'article occupe | page | citation exacte |
|---|---|---|---|
| Papier B (voisin, boîte noire) | Effet de la taille d'équipe (2 à 4 agents) déclaré non isolable ; agrégation des scores par agent : la moyenne est recommandée | p. 29 ; p. 30 | « we cannot disentangle a team-size effect from instance-level difficulty, and we report no isolable agent-count effect » ; « Mean is the right default for joint-only side tasks like ours where sabotage cues are distributed across multiple developers » |
| HC2b (non occupé, à noter) | Une des tâches de sabotage vise une sonde linéaire sur activations ; la sonde est la cible du sabotage, pas le moniteur | p. 12 | « A behavioral safety monitor classifies Pythia-70M layer-3 activations into behavioral domains using a linear probe from the concept-erasure library. » |

Non touchés : H1, H2, lemme d'additivité, théorème négatif, transposition jeton → action, HC1.

**Réserves (R4).**

| réserve | page | citation exacte |
|---|---|---|
| Moniteur de la même famille que l'un des attaquants | p. 9 | « Our monitor is drawn from the same model family as one of the attackers (GPT 5.1 Codex Mini against GPT 5.1 Codex). » |
| Ce n'est pas une évaluation de contrôle (pas d'adversaire adapté au moniteur) | p. 10 | « but it is not a control evaluation » |
| Saturation sur Gemini | p. 9 | « Gemini approaching sabotage saturation means the benchmark no longer separates models on raw capability » |

## 6. 2606.09931v1 — « A Note on the Strategic Confinement Problem »

**Identité.** Auteur unique : Christian Schroeder de Witt (University of Oxford). Version 1, arXiv, 7 juin 2026, catégorie cs.GT ; date imprimée : 10 juin 2026. Venue : aucune. Note conceptuelle, sans expérience ni preuve formelle. Lu en entier.

**Affirmation.**

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 6.1 | niveau 1, l. 168 : « Pour H3 (régimes de collusion indétectable) : … Schroeder de Witt 2026, arXiv 2606.09931 » | confirmé (auteur, année, pertinence). Précision : note conceptuelle ; son apport est qu'une borne de fuite d'information n'implique pas une borne de dommage pour des agents stratégiques ; l'indétectabilité des canaux est reprise de travaux antérieurs, sous hypothèses fortes | p. 1 ; p. 1 ; p. 1 ; p. 4 | « Christian Schroeder de Witt∗ » ; « arXiv:2606.09931v1 [cs.GT] 7 Jun 2026 » ; « Our contribution is therefore not a new theory of communication, but a reinterpretation of confinement in the presence of strategic agents. » ; « Sufficiently capable learning agents can construct general-purpose covert channels that are practically undetectable to polynomially-bounded customer programs that are passive channel monitors given suitably strong assumptions on the shared correlation devices » |

Pointeur (contenu non opposable ici) : la note cite « Vaikuntanathan et Zamir 2026 », aussi nommé à la ligne 168.

| pointeur | page | citation exacte |
|---|---|---|
| Référence citée par la note | p. 12 | « V. Vaikuntanathan and O. Zamir. Undetectable conversations between ai agents via pseudorandom noise-resilient key exchange, Apr. 2026. » |

**Chiffres utilisables.** Aucun : la note ne contient ni mesure ni chiffre propre.

**Antériorité.**

| énoncé revendiqué | ce que l'article occupe | page | citation exacte |
|---|---|---|---|
| Papier B (objection conceptuelle, pas une occupation) | Doute sur la surveillance boîte blanche des canaux de collusion : l'interprétabilité ne voit que des traits lisibles ; mitigations par les incitations plutôt que par la surveillance | p. 3 ; p. 4 | « Interpretability detects a channel only insofar as the features are semantically legible, and deliberate obfuscation defeats that (Draguns et al., 2024). » ; « Efficient mitigations may differ from those Lampson suggested, relying on strategic incentive setting and epistemic engineering rather than better white-box, tool, or channel monitoring and capacity reduction. » |
| Théorème négatif (voisin conceptuel) | Une borne d'information n'implique pas une borne de dommage ; autre forme que celle du programme | p. 1 | « bounds on information leakage need not induce corresponding bounds on worst-case harm: a channel with negligible capacity may still suffice to select damaging outcomes. » |

Non touchés : H1, H2, lemme d'additivité, transposition jeton → action, HC1, HC2b.

## 7. 2605.15377v2 — « Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute »

**Identité.** Auteurs : Eugene Koran, Yejun Yun, Samantha Tetef (contributions égales), Benjamin Arnav, Pablo Bernabeu-Perez (auteurs principaux). Affiliations : SPAR (Koran, Yun, Tetef), Yale University (Yun). Version 2, arXiv, 18 mai 2026, catégorie cs.AI ; date imprimée : 19 mai 2026. Venue : prépublication. Code et données publics : dépôt `Multi-Signal-Control-SPAR/Multi-Signal-Monitoring` sur GitHub, jeu `eugenekoran/apps-control-arena-high-quality` (adresses recollées depuis des lignes coupées). Lu en entier.

**Affirmations.**

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 7.1 | l. 88 : « Koran, Yun, Tetef, Arnav, Bernabeu-Perez (Yale / SPAR) » | confirmé | p. 1 | « Eugene Koran 1 * Yejun Yun 1 2 * Samantha Tetef 1 * Benjamin Arnav § Pablo Bernabeu-Perez § » ; « Equal contribution § Senior Author. 1 SPAR 2 Yale University. » |
| 7.2 | l. 88 : « le meilleur ensemble de trois moniteurs diversifiés donne 2,4 fois le gain de trois moniteurs identiques » | confirmé. Précision (R4) : gain de pAUC sur un moniteur de base seul, 13 % contre 5,5 % ; le meilleur trio est choisi en classant les 220 trios sur l'ensemble de test (borne haute optimiste selon les auteurs) | p. 2 ; p. 3 ; p. 5 | « our best 3-monitor diverse ensemble outperforms a homogeneous 3-monitor ensemble 2.4× (13% vs. 5.5% pAUC gain over a single monitor baseline). » ; « where N = 12 is the total number of monitors, rank them by test set pAUC » ; « The blue line shows the best k-monitor ensemble (test-selected, optimistic upper bound). » |
| 7.3 | l. 88 : « 94,6 % des ensembles diversifiés de cinq battent un appel unique à un grand modèle à coût égal » | confirmé. Précision : le « grand modèle » est GPT-4.1 avec l'invite de base ; contre GPT-5.1 à raisonnement élevé, pas d'avantage constant (et pas à coût égal) | p. 7 ; p. 7 ; p. 7 | « In contrast, 94.6% of diverse 5-monitor ensembles outperform GPT-4.1. » ; « A single GPT-4.1 call is approximately cost-equivalent to a 5-monitor ensemble of GPT-4.1-Mini. » ; « For GPT-5.1 with high reasoning effort (pAUC = 0.783), we find no consistent evidence that the diverse 5-monitor ensemble is better » |
| 7.4 | l. 88 : « tous les moniteurs partagent le même modèle de base » | confirmé | p. 4 | « All monitors use GPT-4.1-mini as the single trusted model. » |
| 7.5 | l. 88 : « ensembles inter-familles et non génératifs laissés à plus tard » | confirmé ; l'article dit « signaux non fondés sur un grand modèle de langage » | p. 8 | « Ensembles drawn from different model families—or that incorporate non-LLM-based signals—may be more resistant, but we have not tested this directly. » |
| 7.6 | l. 88 : « code public » | confirmé | p. 8 | « Code: https://github.com/Multi-Signa l-Control-SPAR/Multi-Signal-Monitor ing » |
| 7.7 | l. 88 : « → Thèse qualitative de H5 occupée en boîte noire » | confirmé sur le vérifiable : thèse « la diversité, pas l'échelle », moniteurs boîte noire ; portée : problèmes de code courts à porte dérobée discrète, pas de trajectoires d'agents | p. 1 ; p. 7 | « We contend that these results show that diversity—not scale—drives gains. » ; « Our evaluation focuses on a well-defined but narrow threat model, specifically short-horizon coding problems where each attack takes the form of a discrete backdoor. » |
| 7.8 | l. 111 : « Ensembles diversifiés (boîte noire) — gain × 2,4 contre moniteurs identiques » (ligne de tableau) | confirmé ; mêmes précisions qu'en 7.2 | p. 2 ; p. 6 | « our best 3-monitor diverse ensemble outperforms a homogeneous 3-monitor ensemble 2.4× (13% vs. 5.5% pAUC gain over a single monitor baseline). » ; « the top ten 3-monitor ensembles span pAUC 0.811–0.816, with improvements clustered around 2.4×. » |
| 7.9 | l. 193 : « Ensembles inter-familles ou non génératifs déjà testés ? » (part de 2605.15377) | réponse : non, ni l'un ni l'autre (confirmé par l'article) | p. 8 | « Ensembles drawn from different model families—or that incorporate non-LLM-based signals—may be more resistant, but we have not tested this directly. » |
| 7.10 | N-005/N-006, l. 80 : « Les ensembles diversifiés (2605.15377) ne sont connus qu'au niveau de la transcription. » | corrigé (F7.1) : désormais vérifiés sur PDF | p. 4 ; p. 11 | « All monitors use GPT-4.1-mini as the single trusted model. » ; « Pattern-matching backdoor detector that operates without access to the problem statement » |
| 7.11 | N-005/N-006, l. 89 : « La nouveauté du quorum par type d'accès repose sur la transcription pour 2605.15377. Elle est à confirmer sur PDF… » | confirmé sur PDF : 2605.15377 n'occupe ni le quorum par type d'accès (aucune sonde interne ; tous les membres sont des juges GPT-4.1-mini ; un seul membre lit le code sans l'énoncé), ni la matrice de transfert des attaques de corruption (aucun adversaire adaptatif, injection seulement évoquée). La réserve peut être levée pour cette source | p. 4 ; p. 11 ; p. 7 ; p. 8 | « All monitors use GPT-4.1-mini as the single trusted model. » ; « Pattern-matching backdoor detector that operates without access to the problem statement » ; « We did not red-team our ensembles against an adaptive adversary with knowledge of the monitoring system. » ; « an adversary can embed monitor-manipulating instructions directly in the code under review » |
| 7.12 | N-005/N-006, l. 95 : « 2606.18276, 2603.15809, 2605.15377 » (lectures à faire) | confirmé pour 2605.15377 : PDF reçu (version 2), empreinte vérifiée, lu en entier | p. 1 | « Diverse Signals Outweigh More Compute » |

**Formulation à mettre à la place.**
- F7.1 (N-005/N-006, l. 80) : remplacer « Les ensembles diversifiés (2605.15377) ne sont connus qu'au niveau de la transcription. » par « Les ensembles diversifiés (2605.15377v2) sont vérifiés sur PDF : douze moniteurs, tous construits sur GPT-4.1-mini (invites diverses et ajustement fin), juges génératifs lisant le code ; aucun membre à accès interne ; un seul membre à accès réduit (sans l'énoncé du problème) ; aucun adversaire adaptatif ni injection testés. »

**Chiffres utilisables.**

| chiffre | nature | page | citation exacte |
|---|---|---|---|
| pAUC : meilleur trio 0,8160 ; moniteur de base 0,7226 ; trois fois le moniteur de base 0,7621 ; trio médian 0,7690 | auteurs | p. 6 | « 1 FT-Completions-Randint, Exploit-Finder, 0.8160 » ; « Baseline monitor 0.7226 » ; « 3× Baseline ensemble 0.7621 » ; « Median 3-monitor ensemble 0.7690 » |
| Gains relatifs : (0,8160 − 0,7226) / 0,7226 = 12,9 % ; (0,7621 − 0,7226) / 0,7226 = 5,5 % ; rapport 2,36 | calcul | p. 6 | « Baseline monitor 0.7226 » ; « 3× Baseline ensemble 0.7621 » |
| Cinq fois le moniteur de base 0,766 contre GPT-4.1 0,761 ; 94,6 % des ensembles de cinq battent GPT-4.1 | auteurs | p. 7 ; p. 7 | « the homogeneous 5×Baseline ensemble (pAUC = 0.766) performs comparably to a single GPT-4.1 with the baseline prompt (pAUC = 0.761) » ; « In contrast, 94.6% of diverse 5-monitor ensembles outperform GPT-4.1. » |
| Sélection sur la seule diversité : 0,717 contre 0,769 pour le trio médian | auteurs | p. 6 | « selecting ensembles purely for diversity (lowest inter-monitor correlation) performs worse than random selection on APPS (pAUC of 0.717 vs. median ensemble pAUC of 0.769) » |
| Rappel à 1 % de faux positifs : 50,0 % (moniteur de base) contre 81,98 % (meilleur ensemble choisi sur validation) | auteurs | p. 5 | « The advantage is most pronounced at the 1% FPR target, where the Baseline monitor achieves 50.0% recall compared to 81.98% for the best ensemble » |
| GPT-4.1-Nano : l'ensemble fait passer la pAUC de 0,162 à 0,553 | auteurs | p. 7 | « Ensemble improvements are largest for the smallest model, where ensembling raises pAUC from 0.162 to 0.553 » |
| Jeu de test : 1 375 échantillons (172 attaques, 1 203 honnêtes) | auteurs | p. 4 | « 1,375 test samples (172 attack, 1,203 honest) » |

**Antériorité.** Aucun des huit énoncés n'est touché. Les sondes linéaires n'apparaissent que dans les travaux cités :

| remarque | page | citation exacte |
|---|---|---|
| Sondes mentionnées seulement comme travail antérieur | p. 2 | « deception detection via linear probes (Goldowsky-Dill et al., 2025) » |
| Agrégation des moniteurs par la moyenne | p. 3 | « We aggregate monitors by averaging their scores; we evaluated alternative aggregation methods but found no consistent improvement over arithmetic mean. » |

**Réserves (R4).**

| réserve | page | citation exacte |
|---|---|---|
| Les meilleurs ensembles sont choisis sur le test ; les dix meilleurs trios restent groupés | p. 5 ; p. 6 | « The blue line shows the best k-monitor ensemble (test-selected, optimistic upper bound). » ; « the top ten 3-monitor ensembles span pAUC 0.811–0.816, with improvements clustered around 2.4×. » |
| Aucun adversaire adaptatif | p. 7 | « We did not red-team our ensembles against an adaptive adversary with knowledge of the monitoring system. » |

## 8. 2608.16190v1 — « Decorrelation Is Not Complementarity: Skill, Not Lineage, Governs Trusted-Monitor Ensembles »

**Identité.** Auteur unique : Anik Jha (chercheur indépendant). Version 1, arXiv, 17 août 2026, catégorie cs.CR. Venue : prépublication. Code public : `github.com/anik-jha/challenger-panels`. Lu en entier.

**Affirmations.**

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 8.1 | l. 89 : « la compétence, pas la lignée, gouverne les ensembles de moniteurs » | confirmé. Précision : 24 moniteurs à poids ouverts de 0,36 à 32 milliards de paramètres, neuf lignées, une seule famille de tâches (code à porte dérobée) ; les résultats de lignée sont des nuls de puissance limitée | p. 2 ; p. 1 ; p. 9 | « Skill, not lineage, is the axis that moves. » ; « At matched member capability, cross-lineage panels detect no better (permutation p = 0.13), and lineage barely moves the metric either (+0.064, p = 0.18). » ; « Our lineage results are nulls, and a null is a statement about power. » |
| 8.2 | l. 89 : « sélectionner sur la seule diversité perd contre le hasard » | corrigé (F8.1) : ce constat est celui de Koran et al. (2605.15377, § 5.4), que l'article crédite ; son propre résultat : la métrique de diversité ne prédit presque pas le gain, et aucune sélection pondérée par la décorrélation ne bat hors échantillon le meilleur moniteur seul | p. 2 ; p. 1 ; p. 8 ; p. 8 | « First, they observe that selecting purely for diversity loses to random selection, because “[l]ow-performing monitors disagree with others not because they detect distinct signals, but because they are more often incorrect” (Koran et al., 2026, §5.4). That is our Finding 1, asserted qualitatively, for prompt-variant monitors sharing one base model. » ; « and no correlation-weighted selection beats picking the single best monitor out of sample. » ; « At k = 3 the out-of-sample pAUC is flat at 0.723 from λ = 0 through λ = 1, then falls to 0.440 at λ = 4 and 0.068 at pure diversity » ; « the single best monitor chosen by validation capability scores 0.733 out of sample, higher than every selected panel at either k. » |
| 8.3 | l. 89 : « → Impose de mesurer la diversité effective (transfert d'attaque), pas la décorrélation brute » | corrigé (F8.2) : « pas la décorrélation brute » est soutenu ; le « transfert d'attaque » est absent de l'article, qui recommande de sélectionner sur la compétence | p. 1 ; p. 8 ; p. 8 ; p. 8 | « Agreement on attack items splits into a shared-detectability signal component and an idiosyncratic error component, which predict ensemble gain with opposite sign (Spearman -0.25 and +0.26), so their sum, the metric actually used, predicts it barely at all (+0.05) » ; « Spend the first unit of effort on prompting a competent monitor well, not on adding a second lineage. » ; « The obvious repair is to select on the error component alone, and we tested that rather than recommending it. » ; « Decomposing the metric explains its failure. It does not repair it. » |
| 8.4 | l. 193 : « Ensembles inter-familles ou non génératifs déjà testés ? » (part de 2608.16190) | réponse : inter-lignées, oui (neuf lignées ; à compétence égale, pas de gain) ; non fondés sur un grand modèle de langage, non (score lu dans les logits d'un grand modèle de langage) | p. 1 ; p. 1 ; p. 3 | « We study 24 open-weight monitors spanning nine pretraining lineages and a 29x range of detection skill (pAUC at 10 percent FPR, 0.028 to 0.803) on backdoored code. » ; « At matched member capability, cross-lineage panels detect no better (permutation p = 0.13), and lineage barely moves the metric either (+0.064, p = 0.18). » ; « The monitor is asked for a YES/NO backdoor judgement and the suspicion score is read from the logits of the decision token as logit(YES) − logit(NO). » |

**Formulations à mettre à la place.**
- F8.1 (l. 89) : remplacer « sélectionner sur la seule diversité perd contre le hasard » par « la métrique de diversité (corrélation moyenne par paires sur les attaques) ne prédit presque pas le gain d'ensemble (Spearman +0,05), ses deux composantes, signal commun et erreur propre, prédisant le gain en sens opposés (−0,25 et +0,26) ; hors échantillon, aucune sélection pondérée par la décorrélation ne bat le meilleur moniteur seul (k = 3 : 0,723 contre 0,733 ; diversité pure : 0,068) ; le constat « la sélection sur la seule diversité perd contre le hasard » vient de Koran et al. (2605.15377, § 5.4), que l'article crédite ».
- F8.2 (l. 89) : remplacer « → Impose de mesurer la diversité *effective* (transfert d'attaque), pas la décorrélation brute. » par « → Montre que la décorrélation brute ne guide pas la composition des ensembles et que sélectionner sur la seule composante d'erreur ne la répare pas ; recommande de sélectionner sur la compétence. Mesurer la diversité effective par transfert d'attaque est une proposition du programme, absente de l'article. »

**Chiffres utilisables.**

| chiffre | nature | page | citation exacte |
|---|---|---|---|
| Compétence et accord avec le reste du groupe : Spearman 0,84 (n = 24, p < 0,0001) | auteurs | p. 1 | « which is why a monitor’s own skill predicts its agreement with the pool (Spearman 0.84, n = 24, permutation p below 0.0001). » |
| Composantes de l'accord : signal −0,25, erreur +0,26, total +0,05 | auteurs | p. 1 | « Agreement on attack items splits into a shared-detectability signal component and an idiosyncratic error component, which predict ensemble gain with opposite sign (Spearman -0.25 and +0.26), so their sum, the metric actually used, predicts it barely at all (+0.05) » |
| Partenaire d'une autre lignée : −0,0084 de pAUC (p = 0,13) | auteurs | p. 6 | « a cross-lineage partner yields −0.0084 pAUC relative to a same-lineage partner » |
| Gain sur le meilleur membre, décroissant avec la compétence : −0,66 (k = 2), −0,70 (k = 3) | auteurs | p. 1 | « Panel gain over the best member falls monotonically with panel skill (-0.66 at k = 2, -0.70 at k = 3) » |
| Hors échantillon (λ : poids de la décorrélation dans le critère de sélection) : 0,723 (k = 3, λ ≤ 1), 0,440 (λ = 4), 0,068 (diversité pure) ; meilleur moniteur seul 0,733 | auteurs | p. 8 ; p. 8 | « At k = 3 the out-of-sample pAUC is flat at 0.723 from λ = 0 through λ = 1, then falls to 0.440 at λ = 4 and 0.068 at pure diversity » ; « the single best monitor chosen by validation capability scores 0.733 out of sample, higher than every selected panel at either k. » |
| Reproduction de l'effet de Koran et al. contre un moniteur de base : +52 % relatif | auteurs | p. 8 | « Measured their way, against our baseline prompt variant at pAUC 0.149, the best prompt-only panel at 0.226 is a 52% relative gain, and their effect reproduces. » |

**Antériorité.**

| énoncé revendiqué | ce que l'article occupe | page | citation exacte |
|---|---|---|---|
| HC1 (méthode voisine, non occupé) | Verdict lu dans les logits du jeton de décision ; aucune pression, aucune déférence | p. 3 | « The monitor is asked for a YES/NO backdoor judgement and the suspicion score is read from the logits of the decision token as logit(YES) − logit(NO). » |

Non touchés : H1, H2, lemme d'additivité, théorème négatif, transposition jeton → action, HC2b, papier B.

**Remarques et réserves.**

| remarque | page | citation exacte |
|---|---|---|
| Attribution à vérifier : l'article attribue à Koran et al. un moniteur par log-probabilités ; introuvable dans 2605.15377v2 (recherche de « logprob », « logit », « log-prob », « log prob », « token prob » sur les 18 pages, textes `-layout` et `-raw` : aucune occurrence) | p. 3 | « We use the logprob-monitor design of Koran et al. (2026) rather than their integer 0–10 prompted monitor. » |
| Selon l'auteur, BigCodeBench-Sabotage n'a jamais été publié | p. 3 | « The anchor’s second benchmark (BigCodeBench-Sabotage) was never released » |
| Pinto 2026 (2607.06596), déjà au lot 3, est cité comme voisin | p. 9 | « Pinto (2026) make untrusted model family the controlled axis for single monitors and find a real own-family interaction » |
| Maxima sur recherche exhaustive dans le test, signalés par l'auteur (R4) | p. 7 | « Every one of these is a maximum over an exhaustive test-split search with no held-out selection » |
| Seuils de décision préenregistrés selon l'auteur | p. 4 | « The decision bars governing each experimental wave were pre-registered before the corresponding runs » |

## Synthèse

1. Empreintes : 8 sur 8 conformes. Tout est lu, sauf les consignes génériques de la liste de contrôle NeurIPS de 2607.07368 (p. 76 à 81) ; deux figures vérifiées à l'image.
2. Corrigé, 2605.31593 (l. 83, 109) : les 81–87 % valent pour un trafic bénin dix fois plus nombreux (à cent fois : 65,8 % contre 55 %) ; « première » est « à notre connaissance ».
3. Corrigé, 2607.02514 (l. 82, 108) : 93 % est le plus faible moniteur (link-tracker seul : 54 %) ; seuil de l'ensemble choisi sur l'évaluation ; code dans un dépôt dérivé, pas dans ControlArena.
4. Corrigé, 2607.07368 (l. 81, 110) : « × 7 » est un rapport de cotes d'achèvement de la tâche secondaire (7,10 plan Flash ; 5,74 tout plan), pas une réussite non détectée. La dilution et le moniteur conjoint (0,91) sont deux résultats distincts. La collusion entre attaquants est étudiée ; seule celle entre exécutant et moniteur est reportée.
5. Corrigé, 2608.02698 (l. 87) : auteur unique (Keele est l'université) ; aucun résultat mesuré ; il cite NARCBench, ce qui contredit « le pendant boîte blanche reste ouvert ».
6. Corrigé, 2608.16190 (l. 89) : « perd contre le hasard » est le résultat de 2605.15377, crédité. N-005 (l. 80) : 2605.15377 est vérifié sur PDF et n'occupe pas le quorum par type d'accès ; la réserve de la l. 89 est levée pour cette source seulement.
7. Introuvable : code de 2605.31593 ; licence de FakeLab (accès sur demande, après revue d'ouverture par les employeurs). Réserves R4 : meilleur ensemble choisi sur le test (2605.15377, ×2,4 et 94,6 % pourtant confirmés).
8. Zones revendiquées : aucune occupée en entier. Touchées en partie : H2 en boîte noire (2605.31593, 2607.02514 ; idée séquentielle non réalisée dans 2608.02698) ; lemme d'additivité et théorème négatif par des bornes classiques de 2608.02698.
9. Touchés aussi : papier B, dont le pendant boîte noire (sécurité selon le nombre d'agents) est occupé par 2607.07368, et NARCBench (déjà connu) est cité par 2608.02698 ; HC1 en marge (empoisonnement du juge, 2605.31593).
10. Contrôle : 259 citations des tableaux et 8 titres contrôlés, 0 échec (test R5 préalable : 14 cas sur 14).

## Annexe — contrôle des citations

- Dossier de travail : `/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/lecture-lot2-B1/`.
- Textes extraits : `texte/` (`pdftotext -layout`, une page par fichier) et `texte_raw/` (`pdftotext -raw`, même découpage).
- Outil : `outils/controle_citations.py`. Il lit les tableaux de ce rapport (colonne « page » et colonne « citation »), rattache chaque citation à l'article du titre courant et la cherche dans la page indiquée. Seuls les blancs et les césures de fin de ligne sont tolérés.
- Test préalable (R5) : `python3 -I outils/test_controle.py texte texte_raw`. Il a donné 14 cas sur 14 conformes. Cas sains acceptés : chiffres justes, blancs modifiés, césure recollée, césure avec trait d'union conservé, tiret long en fin de ligne, trait d'union interne. Artefacts refusés : chiffre altéré, coquille corrigée, mauvaise page, virgule supprimée, trait d'union supprimé hors fin de ligne, casse modifiée. Rapports factices : 1 juste et 1 altéré donnent le code 1 ; un format invalide donne le code 2.
- Contrôle de ce rapport : `python3 -I outils/controle_citations.py rapport.md texte texte_raw`. Résultat : voir la section « Résultat du contrôle » ci-dessous.

### Résultat du contrôle

- Citations des tableaux : 259 contrôlées, 259 trouvées (220 dans le texte `-layout`, 39 dans le texte `-raw` des pages à deux colonnes), 0 échec, 0 erreur de format. Sortie complète : `controle-rapport-sortie.txt`.
- Vérification indépendante du comptage : 33 tableaux, 259 citations dans les colonnes « citation exacte ». L'outil n'a donc rien oublié.
- Titres des huit articles, cités hors tableaux : contrôlés contre la page 1 par `outils/controle_titres.py` : 8 trouvés, 0 échec.
- Hors des colonnes « citation exacte », les passages entre guillemets sont du français (texte du programme, formulations proposées), des noms (sigles), des termes de recherche, ou trois courts fragments anglais des colonnes de verdict (« completing the attack », « attack success rates », « whitebox »), chacun contenu dans une citation contrôlée.
