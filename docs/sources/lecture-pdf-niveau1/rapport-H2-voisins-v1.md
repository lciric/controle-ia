# Lecture sur source primaire — voisins de H2 (E-valuator, TRACES, Probe Trajectories, Doomed from the Start) — v1

Rapport d'un sous-agent lecteur neuf (il n'a rien écrit de ce qu'il vérifie), rendu le 2026-10-04 (UTC).
PDF lus : 2512.03109v2, 2605.27690v2, 2605.18549v1, 2607.06503v2.
Texte extrait **mot pour mot** du journal du sous-agent par `extraire_rapport.py`, sans aucune modification.
Les chiffres marqués « calcul » ou « mon calcul » sont des reconstructions du lecteur, pas des chiffres des auteurs.

---

# Vérification sur sources primaires : H2 (papier A)

J'ai lu les quatre PDF en entier, annexes comprises (27, 28, 38 et 15 pages). Les quatre empreintes SHA-256 concordent. Les pages citées sont le rang dans le fichier ; quand le PDF porte une numérotation imprimée, elle coïncide.

Toutes les citations ci-dessous ont été contrôlées par script contre le texte extrait. Les seuls écarts tiennent aux césures de fin de ligne. Je n'ai rien modifié dans /home/user/controle-ia. Les extractions et le script de contrôle sont dans `/tmp/claude-0/-home-user-cplt-run-2026-09-03/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/lecture-H2/`.

---

## 1. E-valuator (arXiv 2512.03109v2)

**Identité.** « E-valuator: Reliable Agent Verifiers with Sequential Hypothesis Testing ». Sept auteurs : Sadhuka, Prinster, Fannjiang, Scalia, **Bonnie Berger**, Regev, Wang. Affiliations : Genentech, MIT, Johns Hopkins, Stanford. Version v2 du 28 mai 2026 (p.1). Le code est public (p.10).

| # | Affirmation ou question | Verdict ou réponse | Page | Citation |
|---|---|---|---|---|
| 1 | Auteurs listés dans l'état de l'art | **Incomplet** : Berger manque | 1 | « Gabriele Scalia1 , Bonnie Berger2 » |
| 2a | Transforme tout score boîte noire en règle de décision | **Confirmé** | 1 | « a method to convert any black-box verifier score into a decision rule with provable control of false alarm rates » |
| 2b | Contrôle des faux positifs à chaque pas | **Confirmé** : borne sur P(∃ t ≤ T : M_t > c_α), avec T aléatoire | 1, 3–4 | « a sequential hypothesis test that remains valid at every step of an agent’s trajectory, enabling online monitoring of agents » |
| 2c | Validité « par processus e » | **Inexact.** La validité vient d'un seuil PAC : une statistique d'ordre binomiale sur le maximum du processus, calculée sur des trajectoires nulles de calibration. La garantie tient avec une probabilité ≥ 1−δ, et le taux marginal est ≤ α+δ (p.5). Le rapport de densités sert la puissance (log-optimalité). Comme il est estimé, ce n'est plus un processus e exact, et le seuil de Ville échoue empiriquement (p.7–8). | 4, 5, 7, 10 | « Although Proposition 1 controls the false alarm rate with high probability for any function » (p.5) ; « We introduce a PAC procedure to control the false alarm rate even with estimated density ratios. » (p.10) |
| 2d | Somme cumulée ? | **Non.** Un classifieur logistique distinct est entraîné à chaque pas, sur tout le préfixe. Il n'y a ni somme d'incréments ni détection de rupture ; les détecteurs de rupture ne sont cités qu'en travaux connexes (p.6). | 6, 18 | « Note that we train a separate density ratio estimator per timestep t. » |
| 2e | L'accumulation bat le max par pas, à faux positifs égaux | **Occupé en boîte noire.** La base « vérificateur PAC » est le max du score brut par pas, seuillé de la même façon ; elle perd en puissance. | 7–9 | « PAC thresholding alone (without the density ratio statistic) is insufficient: it controls FAR but achieves lower power » |
| 3a | Boîte noire seulement ? | **Oui** dans le cadrage et les expériences (juge Claude Haiku 3.5, PRM Math-Shepherd). Mais le cadre accepte formellement n'importe quel score : on y branche un score de sonde sans rien changer. | 3, 7 | « Typically, St ∈ [0, 1], although e-valuator supports score values of any type. » |
| 3b | Sondes, représentations internes ou activations ? | **Aucune mention**, même comme extension. Le mot « white-box » n'apparaît que pour le coût du réglage fin et pour Wu et al. [63]. | 2, 6 | « white-box access to the verifier (and possibly the agent) weights » ; « using white-box access to the LLM’s internal logits » |
| 3c | Trajectoires d'agents ? | **Oui** : Aviary et OctoTools (agents à outils), Claude Sonnet 4 (raisonnement), six jeux de données | 7, 27 | « For Aviary and Octotools, we use Claude Haiku 3.5 as the verifier » |
| 3d | Cadre adverse ? | **Non.** Le papier détecte des échecs de tâche ; l'hypothèse nulle est « trajectoire réussie ». Les trajectoires dangereuses n'apparaissent qu'en perspective. | 3, 10 | « HN : S ∼ P1 (the final output is correct) » ; « early detection of unsafe or harmful trajectories. » |
| 3e | Hypothèses de validité | Les trajectoires nulles de calibration sont i.i.d. avec celles de test. Aucune indépendance n'est exigée entre les pas. Le rapport de densités demande en plus des exemples étiquetés de l'alternative. Il faut n ≥ ⌈log δ / log(1−α)⌉, sinon c_α = ∞. | 3, 5, 6, 15 | « Suppose our calibration set contains n successful trajectories that are i.i.d. according to the null. » (p.15) |

**Chiffres utilisables.**
- HotpotQA, α = 0,4 (p.8) :
  - e-valuator : puissance 0,78, taux de fausses alertes 0,31 ;
  - vérificateur brut : 0,84 à 0,60 ;
  - Ville randomisé : 0,84 à 0,41 ;
  - vérificateur PAC : taux 0,12, puissance 0,36.
- MATH, α = 0,3 : rejet en 5,5 pas en moyenne, contre au moins 6,8 pour toutes les bases (p.9).
- MATH : 49 % d'exactitude, soit 86 % des 57 % d'origine, avec 84 % des 381 804 tokens (p.9).
- AUC des vérificateurs : de 0,592 à 0,700 (p.27).
- Calibration : « quelques centaines » de trajectoires suffisent ; α′ = 0,9α et δ = 0,1α (p.7).

---

## 2. TRACES (arXiv 2605.27690v2)

**Identité.** « TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling ». Auteurs : Jiaqian Li, Yanshu Li, Boxuan Zhang, Ruixiang Tang, Kuan-Hao Huang (Brown, UT Austin, Rutgers, Texas A&M). Version v2 du 19 septembre 2026 (p.1).

| # | Question | Réponse | Page | Citation |
|---|---|---|---|---|
| 4 | **Point pivot** : observateur séparé ou agent qui agit ? | **Observateur séparé, confirmé.** Deux LLM gelés (Llama-3.1-8B-Instruct, Qwen3-4B) relisent des trajectoires hors ligne produites par d'autres agents (ATBench, ASSEBench). Un encodeur, une banque de mécanismes et un GRU sont appris par-dessus. | 9, 2, 8 | « TRACES builds its trajectory risk states from the hidden representations of an external observer LLM. » (p.9) |
| 4b | Nuance | Dans l'étude DPO hors ligne, politique et observateur partagent les poids de base de Qwen3-4B. Il s'agit de noter des actions candidates, pas d'une évaluation de surveillance. | 18 | « we use the base Qwen3-4B policy to generate multiple candidate next actions » |
| 5a | Le temporel bat le non-temporel | **Confirmé avec nuance.** Sur ATBench (tableau 2, TRACES-Llama), la base non temporelle (prédictions indépendantes par pas, agrégées par top-k MIL) contre TRACES complet : rappel 61,6 → 91,9 ; F1 72,6 → 86,3 ; taux de détection précoce (EDR) 23,2 → 41,4 ; aire sous la courbe des préfixes (EAUPC) 76,1 → 77,9 seulement. La précision des alertes précoces (EAP) **baisse** de 95,8 à 75,9. Sur ASSE-Safety (tableau 9, p.17) : EAUPC 64,9 → 80,3, rappel 86,1 → 95,9, EAP 81,5 → 77,5. | 6, 17 | « It reaches high EAP but loses substantially on recall and EDR, confirming that isolated step evidence misses risks that unfold over time. » |
| 5b | Garantie de faux positifs, toujours valide ? | **Aucune.** Le seuil est choisi sur un jeu de validation et aucun taux de fausses alertes n'est contrôlé. | 4 | « an early safety warning is triggered when qt exceeds a validation-selected threshold δ. » |
| 5c | Cadre adverse ? | **Non** au sens d'un agent saboteur. Les menaces viennent des entrées (utilisateur malveillant, injection) (p.15). Point utile pour H2 : le modèle temporel appris **rate** un risque cumulatif réparti sur des appels d'outils individuellement valides. | 15, 25, 27 | « The underlying risk is cumulative: no single early step is strongly unsafe in isolation » (p.27) |

**Chiffres utilisables.**
- ATBench, EAUPC : de 62,9 (meilleure base) à 82,2 (TRACES-Qwen3-4B) (p.5).
- TRACES-Llama sur ATBench : exactitude 85,5, F1 86,3, rappel 91,9, EDR 41,4. AgentDoG-Llama a un EDR plus élevé, 54,5 (p.6).
- Jeux de données (p.12) : ATBench compte 1 000 trajectoires (503 sûres, 497 dangereuses), 9,01 tours en moyenne. ASSE-Safety compte 1 476 enregistrements, ASSE-Security 817.
- L'EAUPC est la moyenne des AUROC aux préfixes 20, 40, 60 et 80 % (p.15).

---

## 3. Probe Trajectories (arXiv 2605.18549v1)

**Identité.** « Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics ». Auteurs : Chrabąszcz, Szymczyk, Sendera, Trzciński, Cygert (NASK, Politechnika Warszawska, Jagiellonian, Tooploox, IDEAS, Gdańsk). Version v1 du 18 mai 2026, préprint (p.1).

| # | Affirmation | Verdict | Page | Citation |
|---|---|---|---|---|
| 6a | Score de sonde par token, traité comme une série temporelle sur une seule chaîne de pensée | **Confirmé.** Les activations sont celles du modèle de raisonnement qui génère (R1-Llama-8B, Qwen3 4B, 8B et 14B). Une sonde MIL multicouche est lue par max cumulé. | 1, 3, 4 | « By evaluating a probe at each generated token, we construct a probe trajectory, the continuous evolution of a concept’s probability across the reasoning process. » |
| 6b | Caractéristiques de traitement du signal | **Confirmé** : six groupes de caractéristiques, classifieur forêt aléatoire | 4, 15, 24–26 | « we extract signal-processing features that capture volatility, trend, and steady-state behavior » |
| 7 | Le max donne des trajectoires stables là où la moyenne oscille | **Confirmé**, avec deux réserves. Le max cumulé est monotone **par construction** dans l'espace latent. La stabilité est mesurée face au bruit, pas face à un adversaire. | 4, 3 | « average-pooled trajectories exhibit high-frequency oscillations (see Figure 2 and Appendix J), making them highly susceptible to localized computational noise » ; « it enforces a monotonically non-decreasing profile in the latent feature space » (p.3) |
| 8a | Trajectoires agentiques multi-actions ? | **Non** : une réponse par exemple, sur la nocivité et les erreurs de mathématiques | 1, 23–24 | « Using four datasets and four reasoning models across the domains of safety and mathematics » |
| 8b | Test séquentiel avec garantie de faux positifs ? | **Non.** Seule l'AUROC est mesurée, avec une validation croisée à 3 plis sur les jeux de test. | 4, 24 | « We stress that this protocol serves as a diagnostic upper bound » |
| 8c | Sabotage ? | **Non.** L'adversaire n'apparaît que dans la déclaration d'impact. | 15 | « adversaries could reverse-engineer these trajectory features » |

**Chiffres utilisables.**
- Tableau 1 (p.5), AUROC en %, sondes entraînées sur gabarits :

| Agrégation | R1-Llama-8B | Qwen3-4B | Qwen3-8B | Qwen3-14B |
|---|---|---|---|---|
| Max | 94,44 | 96,64 | 94,52 | 95,91 |
| Moyenne | 49,96 | 44,62 | 33,62 | 45,08 |
| Dernier token | 60,11 | 51,86 | 51,06 | 51,48 |
| Juge Qwen3-8B sur la chaîne de pensée | 83,98 | 74,55 | 73,60 | 71,32 |

- Mathématiques (p.7) : sondes statiques entre 73 et 78 % sur MATH, entre 65 et 78 % sur GSM8K. Les trajectoires gagnent jusqu'à environ 17 points sur GSM8K.
- Horizon (fig. 7, p.8) : l'AUROC de nocivité croît avec la part de chaîne de pensée consommée, au niveau token et sans faux positifs contrôlés.

---

## 4. Doomed from the Start (arXiv 2607.06503v2) — absent de l'état de l'art v1

**Identité.** « Doomed from the Start: Early Abort of LLM Agent Episodes via a Recall-Controlled Probe Cascade ». Auteurs : Ruan, Huang, Zhou, Wei, Lin, Wang, Sun (Renmin, ICT-CAS, Duke, CASIA, Zhejiang). Version v2 du 16 juillet 2026 (p.1).

| # | Question | Réponse | Page | Citation |
|---|---|---|---|---|
| 9a | Sondes légères par tour sur les activations de l'agent | **Confirmé.** Régression logistique sur l'état résiduel au dernier token de l'action de l'agent. Les activations sont reconstruites en rejouant la trajectoire dans le même modèle (teacher forcing). | 3 | « the residual-stream hidden state at the final token of the agent’s generated action in round r » |
| 9b | Prédiction de l'échec dès le premier tour | **Confirmé avec nuance.** AUC de 0,86 et 0,81 au tour 1 sur TextCraft. Sur WebShop, Qwen3-1.7B n'est qu'à 0,591 au tour 1 (0,896 au tour 3) et Llama-3.2-3B ne devient informatif qu'après le tour 2. | 5 | « its AUC rises from 0.591 at round 1 to 0.896 at round 3 » |
| 9c | Scoreurs comportementaux proches du hasard | **Affirmé en introduction, sans courbe dans le PDF.** Le scoreur est volontairement pauvre : une logistique sur 5 caractéristiques, dont des log-probabilités. À rappel cible 0,95, il économise 9,9 % contre 41,6 % pour la sonde (WebShop Qwen3-1.7B), et 24,8 % contre 42,2 % (TextCraft Qwen-2.5-7B). | 1, 3, 6 | « barely better than chance in the first round and become informative only around rounds 3–4 » ; « The surface model is deliberately cheap and hand-engineered » |
| 10a | Garantie conforme ? | **Non.** Chaque porte utilise une borne inférieure exacte de Clopper–Pearson sur la survie des épisodes qui réussiront. La variante par quantile conforme viole sa cible : 0,933 et 0,940 pour 0,95 (p.11). | 3, 11 | « This is deliberately stronger than a marginal conformal quantile » |
| 10b | Bonferroni ? | **Non** : la borne d'union est jugée trop conservatrice. Les budgets par tour sont cherchés empiriquement sur une validation disjointe, avec une marge δ = 0,02. | 3, 4 | « a union bound over gates remains valid yet is overly conservative » |
| 10c | Toujours valide ? Par tour ou globale ? | **Globale, mais pas toujours valide.** Le rappel des épisodes qui réussiront est contrôlé à l'échelle de l'épisode, ce qui revient à contrôler les abandons à tort. La cascade est figée à 6 portes (tours 1 à 6). La garantie formelle n'existe qu'avec un certificat indépendant, optionnel, sous hypothèse d'échangeabilité. Sans certificat, jusqu'à 4 graines sur 20 tombent sous la cible (p.13). Ajouter des portes impose de recalibrer (p.7). | 2, 3, 7, 13 | « Formal validity comes from the independent certificate, while reused search data support empirical selection. » |
| 10d | Accumulation additive entre tours ? | **Non : portes indépendantes.** Chaque sonde ne lit que l'état de son tour, ce qui exclut toute somme ou processus e. Seule la calibration est conjointe. | 1, 3 | « an episode completes only if it survives every gate » |
| 11 | Cible, modèles, agent qui agit | Échec de tâche seulement : TextCraft, WebShop, et ALFWorld en test de contrainte. Rien sur la sûreté ni le sabotage. Modèles : Qwen-2.5-7B, Llama-3.2-3B, Qwen3-1.7B. Ce sont bien les activations de la politique qui agit. | 1, 4, 7 | « Our monitor reads frozen-policy activations without an auxiliary LLM pass » |

**Chiffres utilisables.**
- À 90 % de rappel cible : 60,2 % de tokens économisés sur TextCraft, 54,9 % sur WebShop. À 95 % : 45,0 % et 41,5 % (p.1, tableau 1 p.5).
- La cascade économise 1,5 à 8,8 fois plus que la meilleure porte unique, et domine dans les 24 configurations sur 24 (p.5).
- Le rappel atteint s'écarte de la cible d'au plus 0,024 en moyenne (p.5).
- Coût du certificat (p.2) : 114 succès suffisent pour une cible d'environ 0,974 ; il en faut 149 pour 0,98 et 299 pour 0,99.
- ALFWorld (p.6) : AUC 0,815 ; 10,7 % économisés contre 3,3 % pour une porte unique.

---

## 5. Confrontation

### 5.1 Collision avec H2, composante par composante

E = E-valuator, T = TRACES, P = Probe Trajectories, D = Doomed.

| Composante de H2 | E | T | P | D | Niveau global |
|---|---|---|---|---|---|
| Séquentiel (une décision à chaque pas) | occupé, boîte noire (p.1, 3) | partiel : GRU et seuil (p.4) | adjacent : temps = tokens, analyse hors ligne | partiel : 6 portes (p.3) | **occupé en boîte noire, partiel en boîte blanche** |
| Garantie de faux positifs toujours valide | occupé, au sens PAC (p.4–5) | libre | libre | partiel : globale exacte, mais horizon figé (p.2, 7) | **occupé en boîte noire, partiel en boîte blanche** |
| Accumulation bat le max par action, à faux positifs égaux | occupé, boîte noire, échec de tâche (p.8–9) | adjacent : MIL contre GRU, sans contrôle des faux positifs | libre | libre | **occupé en boîte noire, libre en boîte blanche** |
| Accumulation additive (processus e, somme cumulée) sur sondes | partiel : rapport de densités sur préfixe, pas de rupture | libre | libre | libre : portes indépendantes | **libre** |
| Sondes internes | libre, mais tout score est accepté (p.3) | partiel : encodeur et GRU appris | occupé | occupé | **occupé** |
| Activations de l'agent qui agit | libre | libre : observateur (p.9) | occupé, réponse unique | occupé, multi-tours (p.3, 7) | **occupé (D)** |
| Trajectoires multi-étapes | occupé | occupé, hors ligne | libre | occupé | **occupé** |
| Sabotage dont chaque action reste sous le seuil | libre (p.10) | libre, avec un échec documenté (p.25, 27) | libre | libre | **libre** |
| Rappel croissant avec l'horizon, à faux positifs contrôlés | libre (rejets surtout à M1, p.25) | adjacent (p.5, 15) | adjacent (p.8) | adjacent : l'AUC par tour croît (p.5) | **libre** |
| **Conjonction H2** | | | | | **partiel.** D occupe « sondes de l'agent + multi-étapes + garantie sans hypothèse de loi sur une suite de décisions ». E occupe le séquentiel toujours valide en boîte noire. Le reste est libre. |

### 5.2 H1 et plan 2 × 2 accès × agrégation

- **Boîte noire, par action** : occupé. Ce sont les bases « vérificateur brut » et « vérificateur calibré » d'E-valuator, dont le taux de fausses alertes dérive (p.7–8).
- **Boîte noire, séquentiel** : occupé par E-valuator. TRACE (Mittapalli) existe bien : son titre est confirmé par la bibliographie de Doomed (p.9). Son contenu n'est pas vérifié ici.
- **Boîte blanche (agent), par action** : occupé par la porte unique de Doomed (p.4) et les sondes statiques de Probe Trajectories (p.5).
- **Boîte blanche (agent), séquentiel** : partiel. C'est la cascade de portes indépendantes de Doomed ; l'accumulation toujours valide reste vide.
- **Bras manquant** : boîte blanche *observateur*, séquentiel. TRACES l'occupe et bat juges et modèles de garde (tableau 1). Sans ce bras, le gain de H1 peut venir de la simple lecture des représentations d'une transcription, et non de l'accès au calcul de l'agent.
  - C'est mon analyse : la différence réelle entre « agent » et « observateur » est le contexte privé (consigne secrète, raisonnement caché). Ce n'est pas une question de poids, puisque Doomed reconstruit l'agent par rejouage (p.3).
- **H1 au sens général** (le blanc bat le noir à agrégation et faux positifs égaux) : **partiel ou occupé**. Doomed le montre avec le même pipeline et la même cible de rappel (p.6), mais contre un scoreur noir faible et sur l'échec de tâche.
- **H1 au sens spécifique** (sabotage diffus, tâches floues) : **libre**.

### 5.3 Tr (transposition token → action)

**Libre**, avec seulement des éléments adjacents :
- Probe Trajectories ne fait que du token, sans adversaire et sans sonde à attention (p.3–5).
- Doomed et TRACES lisent un seul vecteur par action, en fin d'action, sans agrégation de tokens et sans adversaire (D p.3 ; T p.14).
- Tension à noter : Probe Trajectories justifie le max comme « détecteur d'enveloppe » d'un pic **concentré** (p.5). H2 vise le régime inverse, celui de preuves faibles et réparties. Ce résultat justifie donc le max *à l'intérieur* d'une action, pas *entre* actions.
- Le dernier token s'effondre dans Probe Trajectories (environ 50 %), alors qu'il fonctionne dans Doomed (AUC 0,8 à 0,9). Le choix d'agrégation dépend donc du concept visé.

---

## 6. Formulation la plus forte de H2 encore défendable

> Sur des trajectoires agentiques multi-étapes, un organisme saboteur garde chaque action sous le seuil d'un moniteur par action calibré à 1 % de faux positifs. On accumule par un processus e de mélange (ou sa variante de détection de rupture) les scores de sondes lues dans les activations de l'agent qui agit, contexte privé compris. Le seuil est calibré sur les seuls épisodes honnêtes, échangeables, sans aucun exemple de sabotage.
>
> Cette accumulation détecte ces sabotages avec un taux de faux positifs contrôlé à tout instant, et son rappel croît avec l'horizon. À faux positifs égaux, elle dépasse :
> - (i) la même accumulation sur des scores boîte noire (type E-valuator) ;
> - (ii) une cascade de portes indépendantes sur les mêmes sondes (type Doomed) ;
> - (iii) une sonde lue sur le dernier état seul, qui intègre déjà l'historique par le contexte (analyse de ma part) ;
> - (iv) un modèle temporel sur un observateur séparé (type TRACES).

Ce qui ne se revendique plus :
- le « premier moniteur séquentiel sur sondes d'agent » (Doomed) ;
- un « test séquentiel toujours valide sur trajectoires d'agents » (E-valuator) ;
- « l'accumulation bat le max par pas » en boîte noire (E-valuator, p.8–9) ;
- le « temporel bat le statique sur représentations » (TRACES, Probe Trajectories).

---

## 7. Références citées qui menacent H2

| Référence | Citée par (page de bibliographie) | Ce qu'en dit le papier citant | Menace | Priorité |
|---|---|---|---|---|
| Padhi et al. 2026, « From Actions to Understanding: Conformal Interpretability of Temporal Concepts in LLM Agents », arXiv 2604.19775 | D p.9 | Directions succès/échec dans les représentations d'agents (p.6, 14) | Conforme + temporel + représentations d'agent | 1 |
| Römer, Kobras, Worbis, Schoellig 2025, FIPER, « Failure Prediction at Runtime for Generative Robot Policies », NeurIPS | D p.9 | « FIPER calibrates robot-policy alarms from successful rollouts » (p.14) | Alarmes séquentielles calibrées sur les succès | 1 |
| Yueh-Han et al. 2025, « Monitoring decomposition attacks in llms with lightweight sequential monitors », arXiv 2506.10949 | P p.13 | Moniteur textuel (p.4, 9) | Le régime « chaque pas bénin », en boîte noire | 2 |
| Wu, Zhou, Bates, Jaakkola 2025, « Thought calibration », EMNLP | E p.14 | Règle d'arrêt calibrée par learn-then-test, avec logits internes (p.6) | Boîte blanche + arrêt calibré, sur une seule trace | 2 |
| Huang et al. 2026, PrefixGuard, arXiv 2605.06455 | D p.8 | Classé parmi les moniteurs plus riches (p.14) | Alertes en ligne sur préfixes | 2 |
| Zhang et al. 2026, AgentForesight, arXiv 2605.08715 | T p.11 ; D p.10 | « text or embedding auditors » (D p.14) | Prédiction précoce en ligne | 3 |
| Lu et al. 2026, détection d'hallucination en flux, arXiv 2601.02170 | P p.13 | Représentations cachées de la chaîne de pensée (p.9) | Séquentiel au niveau token sur internes | 3 |
| Kramár et al. 2026, sondes de production pour Gemini, arXiv 2601.11516 ; Taufeeque et al. 2026, « The obfuscation atlas », arXiv 2602.15515 | P p.12–13 | Sondes de production et sondes de tromperie | Tr | 3 |
| Baidya et al. 2026, arXiv 2606.05414 | D p.8 | Alertes faiblement supervisées (p.14) | Adjacent | 3 |

Je n'ai lu aucune de ces références ; ce tableau ne rapporte que ce qu'en dit le papier qui les cite.

---

## 8. Alertes

1. **Collision non répertoriée : Doomed from the Start (2607.06503, juillet 2026).** Le papier est absent de l'état de l'art et du programme. Il couvre déjà sondes de l'agent qui agit, épisodes multi-tours, garantie sans hypothèse de loi au niveau épisode, et supériorité du blanc à pipeline égal.
   - « L'application aux sondes internes » ne tient plus comme revendication.
   - La cascade doit entrer comme base dans la cellule « boîte blanche » du plan 2 × 2.
   - La probabilité d'originalité de 0,50 est à revoir à la baisse.
   - À lire en priorité : Padhi et al. (2604.19775) et FIPER.
2. **E-valuator est mal décrit dans l'état de l'art.**
   - Un auteur manque (Berger).
   - La validité vient d'un seuil PAC sur le maximum, avec des trajectoires nulles i.i.d. et un taux ≤ α+δ. Elle ne vient pas de Ville, qui échoue avec des rapports de densités estimés.
   - Il n'y a pas de somme cumulée.
   - Le cadre accepte « tout type » de score : brancher une sonde y est formellement trivial. La différenciation de H2 doit donc porter sur le régime adverse sous le seuil, une validité qui n'exige aucun exemple de sabotage, la loi rappel–horizon et les bases (ii) à (iv) ci-dessus.
3. **Tr et la règle « max, jamais la moyenne » ne peuvent pas s'appuyer sur Probe Trajectories.**
   - La stabilité est non adverse et en partie construite.
   - L'évaluation se fait par validation croisée sur les jeux de test.
   - La sonde à attention n'est pas testée.
   - L'annexe I (p.27–30) montre des variantes non « Pool » à AUROC ≈ 0,95 (par exemple 0,9504 à la couche 13, p.28), sans préciser leur agrégation. À clarifier avant d'invoquer « l'effondrement de la moyenne ».
