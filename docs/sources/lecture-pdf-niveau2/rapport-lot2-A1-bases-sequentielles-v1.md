# Lecture vérifiée — état de l'art, niveau 2, lot 2 — A1, bases séquentielles

## En-tête

- Lecteur : sous-agent neuf, sans part à la rédaction des documents vérifiés.
- Date (temps universel coordonné) : 2026-10-06, 16 h 36.
- Sources : `/home/user/controle-ia/docs/sources/pdf/`, lues sans modification. Rien n'a été écrit sous `/home/user/controle-ia` (ni fichier, ni git).
- Extraction : `pdftotext` 24.02.0 (Poppler), option `-layout`, page par page ; les pages citées sont le rang de la page dans le fichier. Les pages à deux colonnes, que `-layout` entrelace, ont aussi été extraites en ordre de lecture (sans `-layout`) ; le contrôle dit lequel des deux textes de la même page contient la citation.
- Contexte lu en lecture seule : `docs/etat-de-l-art-controle-ia-v1.md` (empreinte `a7d6846d14758c13639eccb2daeb47722085636a6601aa159e4132ab71d570ce`, lignes 30-74, 130-138, 182-200) et `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md` (lignes 150-185).

### Documents lus (format de document portable, PDF) et empreintes

Empreinte = algorithme de hachage sécurisé à 256 bits (SHA-256). Vérification par `sha256sum -c` contre la liste des consignes : 8 sur 8 conformes. La garde a d'abord été testée sur une empreinte volontairement altérée : échec détecté, code de retour 1 (règle R5).

| Fichier (format de document portable) | Pages | Empreinte SHA-256 (attendue = calculée) | Lecture |
|---|---|---|---|
| 2005.07821v1.pdf | 7 | e1532df64652fa114c7ebda2f9111e6547750537509f5ecd2d7d1d214eb53c14 | entière |
| 2506.10805v4.pdf | 36 | 54bf555501b831d2505b05a0104d59cc0ab46dbb55516e6c0b7548e11db2b7d6 | entière |
| 2507.12691v3.pdf | 39 | 0c00a77b0c07bb9a8cd2feb748d65fe9ac01ee7bee9746ebb9cbc0d1ca8ebb00 | partielle (voir section) |
| 2504.10374v1.pdf | 38 | 5f802d679344fe5e15d1edd50e96245f3bdc054e69d1ff0880b077d173549211 | entière |
| 2605.26047v2.pdf | 46 | 947724f42324070fd47b1ecaf8c1bf9b2257df0e0c7f8822447241d3ea9a28fa | partielle (voir section) |
| 2605.06455v2.pdf | 38 | 4a7533a04ae0c41d1d6ee1b66aa90ab7bbbf5099bf38193f9fdaf61a54477e6c | entière |
| 2602.14161v2.pdf | 27 | 7831c848841eca32bcbb1e18cd35f644cfe5a8af8f0f003623c4e1bdd6e03c00 | entière |
| 2504.20271v1.pdf | 18 | a496a833574e00b8a62fe382a32e37f9a91cd58ba66a5a7744759609ac9d222a | entière |

### Termes développés une fois pour toutes

AUROC : aire sous la courbe de fonctionnement du récepteur (vrais positifs contre faux positifs). AUPRC : aire sous la courbe précision-rappel. CUSUM : somme cumulée (cumulative sum) ; CUSIGN : signe cumulé (cumulative sign). SPRT : test séquentiel du rapport de probabilités (sequential probability ratio test). LODO : évaluation « un jeu de données laissé de côté » (leave-one-dataset-out). NeurIPS : Conference on Neural Information Processing Systems ; ICLR : International Conference on Learning Representations ; ICML : International Conference on Machine Learning ; EMNLP : Conference on Empirical Methods in Natural Language Processing ; AIWILD : First Workshop on Agents in the Wild. MATS : ML Alignment and Theory Scholars (ML : apprentissage automatique). BBR et WBR : raisonnement boîte noire et boîte blanche (black-box et white-box reasoning), moniteurs de 2507.12691 ; « Pairs » et « RP » : sondes « paires instruites » et « jeu de rôle ». TM et UM : surveillance de confiance et surveillance non fiable (trusted et untrusted monitoring). PG, LG, LJ : PromptGuard 2, LlamaGuard 3, Llama-3.1-8B employé comme juge (Llama-as-Judge). GRU : unité récurrente à portes (gated recurrent unit). Les étiquettes R5, R7, R8 (règles) et H1, H2, H6, HC1, HC2b (hypothèses) sont celles du programme ; « arXiv » est un nom d'archive.

Natures des chiffres : « auteurs » = chiffre imprimé ; « figure » = lu sur une figure ; « calcul » = calculé par le lecteur à partir de chiffres imprimés.

## 2005.07821v1 — Memoryless Cumulative Sign Detector for Stealthy CPS Sensor Attacks

### Identité

- Titre : Memoryless Cumulative Sign Detector for Stealthy CPS Sensor Attacks (CPS : systèmes cyber-physiques).
- Auteurs : p. 1 : « Paul J Bonczek and Nicola Bezzo » — Université de Virginie (département de génie électrique et informatique Charles L. Brown, Link Lab).
- Version et date : p. 1 : « arXiv:2005.07821v1 [eess.SY] 15 May 2020 ».
- Venue : aucune imprimée dans le PDF.
- Lu : en entier (7 pages).

### Affirmations du programme

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1 | `etat-de-l-art-controle-ia-v1.md`, ligne 46 : « attaques furtives sur systèmes cyber-physiques qui gardent chaque résidu sous le seuil, arXiv 2005.07821 » | **corrigé** — l'article est un article de détection, et les attaques étudiées échappent aussi à une somme cumulée, pas seulement au seuil par pas. Remplacer par : « détecteur à signe cumulé sans mémoire (CUSIGN) qui repère, en simulation sur un véhicule terrestre, des attaques furtives de capteurs conçues pour rester sous les seuils des détecteurs du chi-deux et à somme cumulée (CUSUM), par la trace non aléatoire des signes de leurs résidus, arXiv 2005.07821 » | 1, 3, 6 | p. 1 : « An intelligent attacker can design stealthy attacks with knowledge of the system model and noise characteristics to evade detection from state-of-the-art fault detectors by remaining within detection thresholds. »<br>p. 1 : « in this paper we propose a run-time monitor called Cumulative Sign (CUSIGN) detector, for identifying stealthy falsified measurements by identifying if measurements are no longer behaving in a random manner. »<br>p. 3 : « A limitation to the method from (8) is that stealthy attacks purposely hidden within detection boundaries may be undetectable. »<br>p. 6 : « Both stealthy attack sequences are designed to be undetectable by CUSUM, but are detected by CUSIGN due to the creation of non-random patterns. » |
| 2 | Même ligne 46 : « → Aucun appliqué à des activations de modèle. » (pour cet article) | **confirmé** : capteurs d'un système linéaire, simulation d'un véhicule terrestre sans pilote | 1 | p. 1 : « Our approach is validated with simulations on an unmanned ground vehicle (UGV) during a navigation case study. » |
| 3 | Ligne 72 : « Borne théorique : un adversaire couvert qui connaît la contrainte de faux positifs peut rendre la somme quasi invisible si l'on ne contraint que la furtivité par action (arXiv 2601.20022 ; analogue cyber-physique arXiv 2005.07821) » | **corrigé** pour la part 2005.07821 (2601.20022 est hors de ce lot) : l'article ne contient aucune borne ; l'attaquant y vise directement la somme cumulée, pas seulement la furtivité par action ; et l'attaque est détectée par une autre statistique cumulée. Remplacer « analogue cyber-physique arXiv 2005.07821 » par : « exemple cyber-physique construit, sans borne : un attaquant qui connaît le modèle et l'estimateur garde sous son seuil une somme cumulée des amplitudes (CUSUM), mais son injection sans bruit laisse une suite de signes non aléatoire qu'un détecteur à signe cumulé (CUSIGN) repère ; à l'inverse, une attaque qui préserve le caractère aléatoire des signes échappe à ce second détecteur (arXiv 2005.07821, p. 5-6) » | 5, 6 | p. 6 : « and has perfect knowledge of the state estimator, it will be able to find the estimator output »<br>p. 6 : « Subsequently, an attacker can design an attack such that it remains within bounds of CUSUM to not trigger alarms more than expected. »<br>p. 6 : « with a noiseless magnitude of 0.1τ C »<br>p. 6 : « for CUSUM is unaffected while CUSIGN discovers the attack »<br>p. 5 : « The CUSIGN detector alone may not be sufficient as an attacker can change the magnitude of a measurement, but still maintain random signed behavior of the test measure » |

### Chiffres utilisables

Aucun chiffre de cet article n'est utilisable pour les hypothèses du programme : ses chiffres (taux d'alarme attendus, bornes de détection, table 2 et annexe A) étalonnent CUSIGN sur une simulation de véhicule.

### Antériorité (R8)

- **H2 — touchée partiellement, sur le principe seulement, hors du champ revendiqué.** Accumulation séquentielle d'une statistique par pas (signe du résidu), taux d'alarme attendu calculé sous l'hypothèse sans attaque (sans exemple d'attaque), pour attraper des attaques qui restent sous un seuil par pas. Mais : capteurs cyber-physiques, pas des sondes d'activations ; aucune garantie toujours valide (bornes par approximation normale trouvée empiriquement) ; aucun seuil par action calibré à 1 % de faux positifs. L'article cite lui-même un test séquentiel de rapport de probabilités sur les résidus. p. 5 : « we empirically find that the alarm rate is a Normal distribution as follows » ; p. 2 : « one of which is the Sequential Probability Ratio Testing (SPRT) [Kwon et al. (2016)] that tests the sequence of incoming residuals one at a time by taking the log-likelihood function (LLF). »
- **Théorème négatif — touché partiellement, sous forme de remarque.** L'article illustre que chaque statistique cumulée est aveugle à une attaque qui préserve ce qu'elle accumule : la somme des amplitudes ne voit pas l'attaque construite, le signe cumulé ne verrait pas une attaque qui garde des signes aléatoires (citation de la ligne 3 ci-dessus, p. 5). Aucun énoncé démontré, aucune attaque à marginales préservées au sens du programme (l'attaque construite change la loi des signes), aucun agrégateur de co-élévation.
- H1, lemme d'additivité, transposition jeton → action, HC1, HC2b, papier B : non touchés.

## 2506.10805v4 — Detecting High-Stakes Interactions with Activation Probes

### Identité

- Auteurs (ordre exact ; les quatre premiers à contribution égale) : p. 1 : « Alex McKenzie1∗ Urja Pawar1∗ Phil Blandfort1∗ William Bankes1,2∗ » ; p. 1 : « David Krueger3 Ekdeep Singh Lubana4,5,6 Dmitrii Krasheninnikov7 » — sept institutions listées en page 1, dont University College London, Harvard, Goodfire et l'université de Cambridge.
- Version et date : p. 1 : « arXiv:2506.10805v4 [cs.LG] 23 Jan 2026 ».
- Venue : p. 1 : « 39th Conference on Neural Information Processing Systems (NeurIPS 2025). »
- Lu : en entier (36 pages ; pages 11 à 15, références, parcourues).

### Affirmations du programme

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1 | Ligne 34 : auteurs « McKenzie, Pawar, Blandfort, Bankes, Krueger, Lubana, Krasheninnikov » | **confirmé** | 1 | p. 1 : « Alex McKenzie1∗ Urja Pawar1∗ Phil Blandfort1∗ William Bankes1,2∗ »<br>p. 1 : « David Krueger3 Ekdeep Singh Lubana4,5,6 Dmitrii Krasheninnikov7 » |
| 2 | Ligne 34 : « NeurIPS 2025 » | **confirmé** | 1 | p. 1 : « 39th Conference on Neural Information Processing Systems (NeurIPS 2025). » |
| 3 | Ligne 34 : « sondes « enjeux élevés » de performance comparable aux moniteurs génératifs de taille moyenne pour environ six ordres de grandeur de calcul en moins (réutilisation des activations du modèle surveillé) » | **corrigé** (précision) : les bases sont promptées *ou affinées* (les affinées deviennent des classifieurs), la comparaison vaut en aire sous la courbe, le gain de calcul suppose des activations gratuites, et à 1 % de faux positifs la sonde est battue. Remplacer par : « sondes « enjeux élevés » dont l'aire sous la courbe moyenne est comparable à celle des moniteurs à grand modèle de langage de taille moyenne (8 à 12 milliards de paramètres), promptés ou affinés, pour environ six ordres de grandeur de calcul en moins, à condition que les activations du modèle surveillé soient disponibles sans coût ; au taux de 1 % de faux positifs, la meilleure sonde ne détecte que 43 % des cas contre 55 % pour la meilleure base » | 1, 5, 10 | p. 1 : « Probes’ performance is comparable to that of prompted or finetuned medium-sized LLM monitors, while offering computational savings of six orders-of-magnitude. These savings are enabled by reusing activations of the model that is being monitored. »<br>p. 5 : « Figure 3: Probes achieve a Mean AUROC across test datasets comparable to the medium (8B-12B) finetuned baselines. »<br>p. 5 : « However, our best probe detects only 43% of high-stakes cases at 1% FPR, compared to 55% for the best LLM baseline. »<br>p. 10 : « assuming activations of the monitored model are available at no computational cost. » |
| 4 | Ligne 34 : « AUROC moyen supérieur à 0,91 hors distribution » | **confirmé** — c'est la sonde à attention sur Llama-3.3-70B (0,916) ; la base promptée Llama-3.3-70B fait mieux (0,929) | 10, 25 | p. 10 : « We show that relatively simple probes, trained on synthetically generated data, can achieve robust generalization performance (mean AUROC > 0.91) on diverse, out-of-distribution, real-world datasets. »<br>p. 25 : « For comparison, the Llama-3.3-70B probe achieved 0.916. »<br>p. 25 : « where the probe (0.916) underperforms the prompted baseline (0.929). » |
| 5 | Ligne 34 : « plusieurs agrégations comparées, dont une sonde à attention et ⚠ un max de moyennes glissantes » | **confirmé** ; le signe ⚠ peut être levé. Six agrégations : moyenne, maximum, dernier jeton, softmax, attention (reprise de Kantamneni et al.), max de moyennes glissantes (présenté comme nouveau pour les sondes) | 2 | p. 2 : « We considered taking the mean, the maximum, the last token score, an average weighted by probe score (“Softmax Probe”), an average weighted by a learned linear function (“Attention Probe”), and the maximum score after taking a rolling-window average (“Max of Rolling Means”). »<br>p. 2 : « To the best of our knowledge, Softmax and Max of Rolling Means have not been used for activation probing before. »<br>p. 2 : « The Attention probe was introduced by Kantamneni et al. (2025). » |
| 6 | Ligne 34 : « → Agrégation sur une interaction, pas sur une trajectoire multi-étapes. » | **confirmé**, avec précision : l'agrégation porte sur les jetons d'un échantillon ; certains échantillons d'évaluation sont des conversations à plusieurs tours ou avec outils (ToolACE), mais il n'y a ni score par action ni accumulation entre actions | 2, 33 | p. 2 : « which includes design decisions such as how to aggregate the activations across the sequence dimension. »<br>p. 33 : « they consist of real-world dialogues, multi-turn interactions, and contexts involving tool usage or psychological harm, properties not present in the synthetic training dataset. » |
| 7 | Ligne 66 (table des bases) : « Sondes « enjeux élevés » — AUROC moyen > 0,91 hors distribution — arXiv 2506.10805 » | **confirmé** (même précision qu'au n° 4 : base promptée Llama-3.3-70B à 0,929) | 10, 25 | p. 10 : « can achieve robust generalization performance (mean AUROC > 0.91) »<br>p. 25 : « where the probe (0.916) underperforms the prompted baseline (0.929). » |
| 8 | Ligne 192 (table « ce qu'il faut établir ») : « 8 — arXiv 2506.10805 — H2 — Existence et définition du max de moyennes glissantes » | **confirmé**. Existence : page 2. Définition (table 3, page 16) : maximum, sur les positions de départ i = 0, …, S − T, de la moyenne sur T jetons consécutifs des scores par jeton θᵀa ; T = 40 dans les expériences. L'agrégateur porte sur les jetons d'une interaction | 2, 5, 16 | p. 2 : « To the best of our knowledge, Softmax and Max of Rolling Means have not been used for activation probing before. »<br>p. 16 : « Applies a rolling mean with window size T »<br>p. 16 : « to the scores at each sequence position and takes the maximum. »<br>p. 5 : « for Max of Rolling Means, we use T = 40. » |

### Chiffres utilisables

| Chiffre | Nature | Page | Citation |
|---|---|---|---|
| AUROC moyen > 0,91 hors distribution (sonde à attention, Llama-3.3-70B) | auteurs | 10 | p. 10 : « can achieve robust generalization performance (mean AUROC > 0.91) » |
| ≈ 0,916 sur les jeux de test contre > 0,99 sur le test synthétique | auteurs | 35 | p. 35 : « mean AUROC ∼0.916 across test datasets vs >0.99 on synthetic test data » |
| 43 % contre 55 % de cas détectés à 1 % de faux positifs (meilleure sonde contre meilleure base) | auteurs | 5 | p. 5 : « However, our best probe detects only 43% of high-stakes cases at 1% FPR, compared to 55% for the best LLM baseline. » |
| À 1 % de faux positifs, la base promptée Llama-3.1-8B dépasse déjà les sondes | auteurs | 5 | p. 5 : « When measuring TPR @1% FPR, probes still outperform 1B models and finetuned Gemma-3-12B, but other baselines (such as prompted Llama-3.1-8B) score higher. » |
| Sonde 0,916 contre base promptée Llama-3.3-70B 0,929 : écart −0,013 | auteurs (écart : calcul) | 25 | p. 25 : « where the probe (0.916) underperforms the prompted baseline (0.929). » |
| Économie de calcul d'environ un million de fois | auteurs | 1 | p. 1 : « being around 1,000,000 times more efficient. » |
| Fenêtre du max de moyennes glissantes : T = 40 | auteurs | 5 | p. 5 : « for Max of Rolling Means, we use T = 40. » |
| **Réserve, incohérence interne** : la table 8 donne 0,970 (Llama-3.3-70B prompté) et 0,916 (Llama-3.1-8B prompté), la page 25 donne 0,929 et 0,877 pour les mêmes bases, attribués à la figure 3. Ne citer ces bases qu'avec leur source exacte | auteurs | 25, 27 | p. 27 : « Llama-3.3-70B 0.970 0.928 »<br>p. 27 : « Llama-3.1-8B 0.916 0.901 »<br>p. 25 : « the gap between the probe (0.887) and the prompted baseline (0.877, Figure 3) » |

### Antériorité (R8)

- **H1 — touchée partiellement (forme de la comparaison, autre objet).** Sondes contre moniteurs boîte noire, y compris au taux de vrais positifs à 1 % de faux positifs ; objet : interactions « à enjeux élevés », concept que les auteurs disent flou, pas un sabotage ni une trajectoire. Résultat défavorable aux sondes à 1 % (43 % contre 55 %). Les auteurs laissent ouverte la question d'un avantage propre à la boîte blanche. p. 10 : « The concept of “high-stakes interactions” is fuzzy, subjective and context-dependent » ; p. 10 : « systematically exploring whether white-box access offers unique qualitative advantages beyond cost savings remains open »
- **Transposition jeton → action — touchée au niveau jeton seulement.** Comparaison d'agrégations (maximum, max de moyennes glissantes, attention, moyenne) en performance, et dilution observée qualitativement ; rien au niveau de l'action, rien sur un adversaire entraîné. p. 4 : « Taking the maximum over per-token predictions biases probes towards the most high-stakes token in a response » ; p. 7 : « Finally, embedding a high-stakes prompt in a low-stakes context can reduce probe scores »
- **H2 — non occupée** : le max de moyennes glissantes est un agrégateur à fenêtre sur les jetons d'une interaction, sans test séquentiel ni garantie de faux positifs.
- Lemme d'additivité, théorème négatif, HC1, HC2b, papier B : non touchés.

## 2507.12691v3 — Benchmarking Deception Probes via Black-to-White Performance Boosts

### Identité

- Auteurs : p. 1 : « Aviel Parrack Carlo Leonardo Attubato Stefan Heimersheim » ; affiliations p. 1 : « UCLA, Pivotal Pivotal Apollo Research » (université de Californie à Los Angeles, Pivotal, Apollo Research). Les métadonnées du fichier écrivent « Avi Parrack ».
- Version et date : p. 1 : « arXiv:2507.12691v3 [cs.AI] 17 Jan 2026 ».
- Venue : aucune ; p. 1 : « Preprint. Under review. »
- Lu : pages 1 à 19 en entier (texte, références, annexes A à E, début de F), pages 25, 26, 28, 30, 33 à 36 en entier. **Non lues en entier** : pages 20 à 24 (courbes, valeurs reprises des tables 3 et 6), 27, 29, 31, 32, 37 à 39 (suite des consignes des moniteurs et des exemples de jeux), seulement parcourues.

### Affirmations du programme

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1 | Ligne 35 : auteurs « Parrack, Attubato, Heimersheim » | **confirmé** | 1 | p. 1 : « Aviel Parrack Carlo Leonardo Attubato Stefan Heimersheim » |
| 2 | Ligne 35 : « définit le « gain blanc-sur-noir » (moniteur avec accès aux scores de sondes contre moniteur sans) » | **confirmé** ; terme exact « black-to-white performance boost » ; le même modèle de langage sert aux deux moniteurs, si bien que le gain est imputable aux sondes | 1, 9 | p. 1 : « We benchmark deception probes by the extent to which the white box monitor outperforms the black-box monitor, i.e. the black-to-white performance boost. »<br>p. 9 : « the same model is used in both Black-box Reasoning and White-box Reasoning, so any black-to-white performance boosts can be attributed to the probes themselves. » |
| 3 | Ligne 35 : « sur sandbagging et délit d'initié » | **corrigé** — cinq jeux, dont un de code à porte dérobée. Remplacer par : « sur cinq jeux de tromperie stratégique — AI Liar, dilution de la tromperie, délit d'initié, sandbagging, code à porte dérobée (Backdoors) —, avec Alpaca comme témoin honnête » | 2, 3, 4 | p. 2 : « We evaluate eight monitoring strategies across five datasets and explore failure modes that arise in practice. »<br>p. 3 : « Datasets AI Liar, Insider Trading, and Sandbagging are on-policy »<br>p. 3 : « In contrast, Deception Dilution, Backdoors, and Alpaca are off-policy. »<br>p. 4 : « This dataset simulates an AI assistant intentionally inserting subtle backdoors into code, however it doesn’t rely on LLaMA-3.3-70B-Instruct to generate the backdoors itself. » |
| 4 | Ligne 35 : « réponses isolées » | **confirmé** : chaque moniteur note une réponse de l'assistant, sur les seuls jetons publics (les échantillons de délit d'initié contiennent une trajectoire d'outils, mais l'étiquette porte sur le rapport final) | 3, 5 | p. 5 : « Each method outputs a "suspiciousness rating" indicating its confidence that a response is deceptive. »<br>p. 3 : « Monitoring strategies are only given access to public tokens, simulating the challenge of evaluating models whose internal reasoning is hidden. » |
| 5 | Ligne 35 : « → La métrique de H1 existe ; pas sur sabotage étalé. » | **confirmé**, avec précision : la métrique principale est l'aire sous la courbe ; la version à 1 % de faux positifs calibrée sur Alpaca figure en annexe et les auteurs la jugent inadaptée (saturation). Le seul jeu proche du sabotage (code à porte dérobée, réponse isolée, non généré par le modèle) donne un gain négatif au raisonnement boîte blanche (0,776 contre 0,899) | 7, 8, 15 | p. 7 : « AUROC is our primary evaluation metric »<br>p. 8 : « A modest black-to-white performance boost is seen across datasets with the exception of the Backdoors setting in which White-box Reasoning is strictly worse than the black-box monitor alone. »<br>p. 15 : « However, Alpaca proves ill-suited for this purpose: many monitors achieve 100% true positive rates across most datasets (Figure 5). » |

### Chiffres utilisables

| Chiffre | Nature | Page | Citation |
|---|---|---|---|
| Moyenne sur cinq jeux : WBR (Sonnet 3.5, Pairs) 0,925 contre BBR (Sonnet 3.5) 0,879 ; gain +0,046 | auteurs (gain : calcul) | 7 | p. 7 : « WBR (sonnet-3.5, Pairs) 0.966 0.916 0.776 0.986 0.981 0.925 »<br>p. 7 : « BBR (sonnet-3.5) 0.822 0.799 0.899 0.934 0.942 0.879 » |
| Code à porte dérobée : WBR Pairs 0,776 et RP 0,733 contre BBR 0,899 (−0,123 et −0,166) ; ensemble Pairs 0,925 (+0,026) | auteurs (écarts : calcul) | 7 | p. 7 : « WBR (sonnet-3.5, RP) 0.956 0.879 0.733 0.936 0.973 0.896 »<br>p. 7 : « Ensemble (sonnet-3.5, Pairs) 0.953 0.846 0.925 0.994 0.964 0.936 » |
| Dilution insensible : moyenne 0,966 → 0,931 ; pic 0,937 → 0,811 | auteurs | 7, 15 | p. 15 : « For example, Full Averaging (Pairs) drops from 0.966 AUROC on AI Liar to 0.931 on insensitive dilution. »<br>p. 7 : « Peak Activation (Pairs) 0.937 0.811 0.768 0.979 0.839 0.867 » |
| Relance « Deception No » avec la sonde RP sur sandbagging : 0,457 | auteurs | 7 | p. 7 : « Deception No (RP) 0.928 0.879 0.667 0.997 0.457 0.786 » |

### Antériorité (R8)

- **H1 — touchée partiellement.** La métrique (gain d'un moniteur avec scores de sondes sur le même moniteur sans) est occupée, pour la tromperie sur réponses isolées, et un jeu de code à porte dérobée y figure (gain négatif). Ne sont pas occupés : sabotage étalé sur une trajectoire, tâches floues, comparaison au taux de 1 % de faux positifs. Les auteurs annoncent eux-mêmes l'intérêt des tâches longues. p. 9 : « We suspect that such probes will grow increasingly valuable as assistants perform long-horizon tasks, where deception can be limited to only a tiny fraction of the output. »
- **Transposition jeton → action — touchée au niveau jeton.** Sous attaque de dilution (vérités hors sujet ajoutées), la moyenne résiste et le maximum se dégrade ; le signal est étalé sur toute la réponse. À verser au dossier du test de transposition : ce résultat va dans le sens contraire de la robustesse du maximum citée au § 2.4 du programme (autre attaque). p. 8 : « The probe activation is largely spread out over the entire response, not concentrated on the deceptive claims. » ; p. 15 : « Peak activation monitors perform notably better on deception-only dilution than insensitive dilution (0.971 vs 0.811 for Pairs, and 0.931 vs 0.877 for RP). »
- **HC2b — touchée partiellement, si HC2b vise la sonde lue pendant un déni de l'agent.** Méthodes de relance (« Was your response deceptive? » puis « No ») : la sonde est lue sur la dénégation ; ces méthodes font moins bien que la moyenne simple. p. 6 : « Both follow-up methods exploit the insight that a deceptive model might show elevated probe activations during an explicit denial of deception. »
- **H2 — non occupée** ; seule la normalisation sur un témoin honnête rappelle le calibrage sans exemple de H2. p. 6 : « This normalization reflects a realism constraint, wherein many honest responses are available for calibration but deceptive examples are scarce. »
- Lemme d'additivité, théorème négatif, HC1, papier B : non touchés.

## 2504.10374v1 — Ctrl-Z: Controlling AI Agents via Resampling

### Identité

- Auteurs : p. 1 : « Aryan Bhatt 1 Cody Rushing * 1 2 Adam Kaufman * 1 2 Tyler Tracy * 1 2 Vasil Georgiev * 2 3 David Matolcsi 3 » ; p. 1 : « Akbir Khan 3 Buck Shlegeris 1 ».
- Affiliations : p. 1 : « Equal contribution 1 Redwood Research 2 ML Alignment and Theory Scholars (MATS) Program 3 Work done while at Redwood Research. »
- Version et date : p. 1 : « arXiv:2504.10374v1 [cs.LG] 14 Apr 2025 ».
- Venue : aucune imprimée dans le texte. Les métadonnées du fichier (champ « Subject ») portent « Proceedings of the International Conference on Machine Learning 2025 » : non opposable au sens de R7 (pas de page).
- Lu : en entier (38 pages).

### Affirmations du programme

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1 | Ligne 44 : « Bhatt, Rushing, Kaufman, Tracy, Georgiev, Matolcsi, Khan, Shlegeris — Redwood Research » | **confirmé** (précision : Rushing, Kaufman, Tracy et Georgiev aussi au programme MATS ; Georgiev, Matolcsi et Khan « travail fait chez Redwood Research ») | 1 | p. 1 : « Aryan Bhatt 1 Cody Rushing * 1 2 Adam Kaufman * 1 2 Tyler Tracy * 1 2 Vasil Georgiev * 2 3 David Matolcsi 3 »<br>p. 1 : « Akbir Khan 3 Buck Shlegeris 1 »<br>p. 1 : « Equal contribution 1 Redwood Research 2 ML Alignment and Theory Scholars (MATS) Program 3 Work done while at Redwood Research. » |
| 2 | Ligne 44 : « ré-échantillonnage des actions suspectes » | **confirmé** | 1 | p. 1 : « We introduce a class of control protocols called resample protocols that dynamically take additional samples of certain actions. » |
| 3 | Ligne 44 : « succès d'attaque de 58 % à 7 % pour 5 % de coût d'utilité » | **confirmé** | 1 | p. 1 : « our best protocol combines resampling with analysis of previous steps, reducing the success rate of attacks from 58% to 7% at a 5% cost to the performance of a non-malicious agent. » |
| 4 | Ligne 44 : « meilleur protocole à 72,7 % de sécurité pour 95 % d'utilité » | **corrigé** — 72,7 % est le score de *Defer to trusted*, protocole existant sans ré-échantillonnage. Remplacer par : « 72,7 % de sécurité à 95 % d'utilité pour Defer to trusted (protocole existant, face aux attaques en plusieurs étapes) ; meilleur protocole de ré-échantillonnage (Time travel, incrimination dans le passé) : 87,1 % à 95 % d'utilité, et 92,6 % combiné à la surveillance non fiable » | 5, 8, 9 | p. 5 : « Result: A safety score of 72.7% at 95% usefulness. »<br>p. 8 : « Defer Basic DTR DTR with Incrimination Auditing after Time Travel (Incrimination »<br>p. 8 : « 95% Usefulness 72.7% 83.2% 84.0% 84.9% 87.1% »<br>p. 8 : « Result: A safety score of 87.1% at 95% usefulness. This is the best resampling protocol, as seen in Table 1. »<br>p. 9 : « Table 2. Comparison at 95% usefulness. TM = Trusted Monitoring, »<br>p. 9 : « UM 77.6% 91.1% 92.6% » |
| 5 | Ligne 44 : « BashBench, 257 tâches » | **confirmé** ; 100 tâches d'entraînement et 157 de test, résultats sur le test. Réserve : l'annexe C parle d'un calcul d'utilité sur « nos 257 tâches » | 1, 2, 18 | p. 1 : « We construct BashBench, a dataset of 257 challenging multi-step system administration tasks »<br>p. 2 : « We divide our tasks into 100 train tasks and 157 test tasks and iterate only on the train set of tasks. »<br>p. 18 : « by assuming that our 257 tasks are i.i.d. samples from the same task distribution » |
| 6 | Ligne 44 : « modèle non fiable GPT-4o mini, modèle de confiance Llama 3.1 8B » | **confirmé** | 3 | p. 3 : « we treat GPT-4o mini as if it were untrusted in order to develop control protocols. »<br>p. 3 : « We implement our trusted model with Llama-3.1-8B (Dubey et al., 2024). » |
| 7 | Ligne 44 : « → Base de H6 (intervention spécifique, boîte noire) » | **confirmé** pour le caractère boîte noire : le moniteur de confiance lit l'historique et la commande ; aucune activation | 19 | p. 19 : « Our trusted monitor scaffolds provide the history of a task trajectory, as well as the command to run, to T » |
| 8 | Ligne 64 (table des bases) : « Ctrl-Z (ré-échantillonnage) — 72,7 % de sécurité à 95 % d'utilité — arXiv 2504.10374 » | **corrigé** — remplacer par : « Ctrl-Z (ré-échantillonnage, Time travel) — 87,1 % de sécurité à 95 % d'utilité (92,6 % avec surveillance non fiable ; Defer to trusted, sans ré-échantillonnage : 72,7 %) — arXiv 2504.10374 » | 8, 9 | p. 8 : « 95% Usefulness 72.7% 83.2% 84.0% 84.9% 87.1% »<br>p. 9 : « TM 72.7% 83.2% 87.1% »<br>p. 9 : « UM 77.6% 91.1% 92.6% » |
| 9 | Ligne 195 (table « ce qu'il faut établir ») : « 11 — arXiv 2504.10374 — H6 — 72,7 % comme résultat principal » | **corrigé** — remplacer par : « 72,7 % n'est pas le résultat principal : c'est Defer to trusted. Résultat principal : succès d'attaque de 58 % à 7 % pour 5 % d'utilité perdue ; meilleure sécurité à 95 % d'utilité : 87,1 % (92,6 % avec surveillance non fiable). Les auteurs tiennent les gains relatifs pour plus importants que les scores absolus » | 1, 8, 9 | p. 1 : « our best protocol combines resampling with analysis of previous steps, reducing the success rate of attacks from 58% to 7% at a 5% cost to the performance of a non-malicious agent. »<br>p. 8 : « Result: A safety score of 87.1% at 95% usefulness. This is the best resampling protocol, as seen in Table 1. »<br>p. 9 : « Hence, we think the relative improvements of our protocols are a more important result than the absolute scores. » |

### Chiffres utilisables

| Chiffre | Nature | Page | Citation |
|---|---|---|---|
| Surveillance de confiance seule : 41,8 % de sécurité à 100 % d'utilité | auteurs | 5 | p. 5 : « Result: A safety score of 41.8% at 100% usefulness. » |
| À 95 % d'utilité : Defer to trusted 72,7 %, Defer to resample 83,2 %, incrimination au présent 84,0 %, trois coups 84,9 %, Time travel 87,1 % | auteurs | 8 | p. 8 : « 95% Usefulness 72.7% 83.2% 84.0% 84.9% 87.1% » |
| Avec surveillance non fiable, à 95 % d'utilité : 77,6 %, 91,1 %, 92,6 % | auteurs | 9 | p. 9 : « UM 77.6% 91.1% 92.6% » |
| Correspondance du résumé : 58 % ≈ 1 − 0,418 (surveillance de confiance, 100 % d'utilité) et 7 % ≈ 1 − 0,926 (Time travel et surveillance non fiable, 95 % d'utilité) | calcul | 1, 5, 9 | p. 5 : « Result: A safety score of 41.8% at 100% usefulness. »<br>p. 9 : « UM 77.6% 91.1% 92.6% » |
| Budget d'audit humain : 1 % des actions d'un épisode | auteurs | 3 | p. 3 : « equivalent to 1% of the actions taken in an episode » |
| Moniteur non fiable honnête : 98,8 % des attaques attrapées à 1 % de budget | auteurs | 8 | p. 8 : « catching 98.8% of attacks at a 1% auditing budget. » |

### Antériorité (R8)

- **H2 — touchée partiellement, en boîte noire.** « Audit après trois coups » : agrégation des scores d'action sur la trajectoire par une statistique d'ordre (troisième maximum courant), seuils pris comme quantiles de la distribution de la politique honnête, donc sans exemple d'attaque ; un test de Kolmogorov–Smirnov sur la trajectoire a été essayé puis abandonné. Pas d'accumulation additive, pas de garantie toujours valide, pas de sondes. p. 7 : « Once this happens for the third time, it audits the trajectory. » ; p. 33 : « A step’s looking-back-score is defined as min(cur-score, third-max-so-far) » ; p. 19 : « The auditing threshold is computed as a quantile on the usefulness baseline distribution » ; p. 22 : « As another baseline, we used the Kolmogorov–Smirnov test which tests the similarity of two distributions. »
- **H1 — non touchée** (aucune activation). L'article établit toutefois, en boîte noire, que découper l'attaque en étapes rend chaque action moins suspecte : menace pertinente pour H1 et H2. p. 1 : « the attack policy can break up malicious strategies into many actions to make each action less suspicious. » ; p. 5 : « We created attacks of various lengths and observed that the individual messages of multi-step attacks are less suspicious than single-step attacks »
- **Transposition jeton → action — marginalement** : le score d'une commande est le maximum sur ses sous-commandes, en boîte noire, sans étude de robustesse. p. 22 : « Ultimately, though, we chose to fix all the trusted monitors to simply take the max over substeps for simplicity. »
- **Papier B — touché partiellement, hors activations** : surveillance par une copie non fiable du même modèle, collusion par signal convenu, contre-mesures (pots de miel, paraphrase) ; ni états internes, ni co-élévation, ni nombre d'agents. p. 8 : « However, a malicious untrusted monitor might collude with the untrusted agent, lying by rating dangerous code as safe to avoid reporting attacks. »
- Lemme d'additivité, théorème négatif, HC1, HC2b : non touchés.

## 2605.26047v2 — Retrying vs Resampling in AI Control

### Identité

- Auteurs : p. 1 : « James Lucassen∗ Adam Kaufman∗ » ; p. 1 : « Redwood Research Redwood Research » ; p. 1 : « Author order randomized. »
- Version et date : p. 1 : « arXiv:2605.26047v2 [cs.AI] 26 May 2026 ».
- Venue : aucune imprimée.
- Lu : pages 1 à 29 en entier (texte, annexes A à H, début de I). **Non lues en entier** : pages 30 à 46 (annexe I, exemples de ré-échantillonnages), seulement parcourues.

### Affirmations du programme

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1 | Ligne 45 : « Retrying vs Resampling in AI Control, arXiv 2605.26047 » | **confirmé** (titre et identifiant) ; auteurs à ajouter : Lucassen et Kaufman, Redwood Research | 1 | p. 1 : « James Lucassen∗ Adam Kaufman∗ » |
| 2 | Ligne 45 : « compare deux intensités d'intervention » | **corrigé** — il s'agit de deux familles de protocoles, pas de deux intensités. Remplacer par : « compare le réessai (bloquer l'action signalée et poursuivre, avec ou sans la justification du moniteur) et le ré-échantillonnage (plusieurs tirages dans le même contexte, pour décider de l'audit ou pour exécuter le moins suspect) ; cinq tirages par étape et audit sur le maximum font passer la sécurité de 61 % à 71 % à 0,3 % de budget d'audit, sans coût d'utilité ; le maximum bat le minimum, contrairement à Ctrl-Z ; le réessai avec justification est exploité par l'attaquant » | 1, 5 | p. 1 : « AI coding scaffolds like Claude Code and Codex use retrying: blocking actions flagged as risky and continuing the trajectory. »<br>p. 1 : « We also study resampling: drawing multiple samples from the same context, which does not leak exploitable information. »<br>p. 1 : « In BashArena, with Claude Opus 4.6 as the untrusted model and MiMo-V2-Flash as the trusted monitor, drawing five samples per step and auditing on the maximum suspicion score raises safety from 61% to 71% at a 0.3% audit budget, at no cost to usefulness. »<br>p. 1 : « The first is that auditing based on the maximum across resampled suspicion scores outperforms using the minimum, which is the opposite of what Ctrl-Z found. »<br>p. 5 : « However, feedback does not improve safety against a responsive attack policy at the headline audit budget. » |
| 3 | Ligne 45 : « en boîte noire » | **confirmé** : moniteur de confiance sur les appels d'outils, sans la chaîne de pensée ; aucune activation dans l'article | 4 | p. 4 : « As a conservative assumption, the monitor is not shown any chain of thought reasoning used by U to produce its actions. » |

### Chiffres utilisables

| Chiffre | Nature | Page | Citation |
|---|---|---|---|
| Surveillance de confiance 61 % → cinq tirages avec audit sur le maximum 71 % (budget 0,3 %) | auteurs | 1 | p. 1 : « drawing five samples per step and auditing on the maximum suspicion score raises safety from 61% to 71% at a 0.3% audit budget, at no cost to usefulness. » |
| Gain : +10,2 points, intervalle apparié à 95 % de +6,1 à +14,3 | auteurs | 2 | p. 2 : « by up to +10.2 pp (paired 95% CI: [+6.1, +14.3]) with 5 samples per step » |
| Exécuter le moins suspect : +3,9 points, intervalle incluant zéro | auteurs | 1 | p. 1 : « gives only a small empirical safety gain in our setting (+3.9 pp, with the confidence interval overlapping zero). » |
| Audit après k coups : 61 % (k = 1), 44 % (k = 2), 8 % (k = 5) | auteurs | 24 | p. 24 : « Figure 18 shows that any k > 1 decreases safety: from 61% at k=1 down to 44% at k=2. »<br>p. 24 : « Safety continues to drop with higher k, down to 8% at k=5. » |
| Ré-échantillonnage sélectif : 6,2 points récupérés pour 0,4 tirage supplémentaire par étape | auteurs | 2 | p. 2 : « We can recover 6.2 pp of safety gain by drawing 0.4 extra samples per step instead of 4. » |
| Échantillons du moniteur : le maximum gagne environ 22 points de 1 à 10 échantillons ; moyenne et médiane plates | auteurs | 19 | p. 19 : « max gains roughly 22 percentage points from k=1 to k=10 »<br>p. 19 : « Mean and median aggregation show essentially no improvement as the number of samples increases, remaining flat from k=1 to k=10. » |

### Antériorité (R8)

- **H2 — non occupée ; résultat contraire à verser au dossier.** En boîte noire, l'agrégation numérique de l'historique (audit après k coups) baisse la sécurité pour tout k > 1 quand le moniteur voit déjà l'historique ; l'audit se fait pas à pas parce que les échecs du cadre sont immédiats et irréversibles. p. 4 : « We find that auditing after k strikes decreases safety in our setting for any k > 1. » ; p. 24 : « If the monitor is already effectively accounting for suspicious past actions when scoring the current step, this leaves no further signal to be captured by numerical history aggregation. » ; p. 3 : « We make auditing decisions on a step-wise basis instead of a trajectory-wise basis because BashArena is designed to model live failures »
- **Théorème négatif — touché partiellement, sur un autre axe.** Le bon agrégateur (maximum ou minimum) dépend des corrélations entre ré-échantillonnages chez l'honnête et chez l'attaquant, et un attaquant qui contrôle ces corrélations choisit la pire. Données synthétiques par permutation ; pas de théorème ; corrélation entre tirages d'une même étape, pas entre actions successives. p. 7 : « Assuming the red team has full control over the cross-resample correlations of their attacks, this suggests they should make those correlations either as high as possible or as low as possible, depending on whether the blue team chooses to use max or min aggregation. »
- **Papier B — touché faiblement** : copies d'un même modèle (tirages dans le même contexte) et corrélation de leurs scores de moniteur, en boîte noire ; ni états internes, ni nombre d'agents.
- **Menace pertinente pour H1 et H2** : la politique d'attaque est explicitement instruite d'étaler l'attaque sur de nombreuses actions. p. 22 : « The best strategies should involve logic that is gradually built up across many different actions, where no single action clearly has anything to do with the red team task. »
- H1, lemme d'additivité, transposition jeton → action, HC1, HC2b : non touchés.

## 2605.06455v2 — PrefixGuard: Online Failure Warning and Trace-Grounded Diagnosis for LLM Agents

### Identité

- Auteurs : p. 1 : « Xinmiao Huang1 , Jinwei Hu1 , Qisong He1 , Rajarshi Roy1 , Changshun Wu1 , Yi Dong1, † , » ; p. 1 : « Xiaowei Huang1, † » ; p. 1 : « University of Liverpool ».
- Version et date : p. 1 : « arXiv:2605.06455v2 [cs.AI] 27 Sep 2026 » ; p. 1 : « Date: September 25, 2026 ».
- Venue : aucune imprimée.
- Lu : en entier (38 pages ; les pages 31 à 38, revue sémantique et vérification de modèles, sont sans lien avec les affirmations).

### Affirmations du programme

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1 | `etat-de-l-art-verifie-niveau1-v1.md`, ligne 169 : « PrefixGuard, arXiv 2605.06455 » (identité) | **confirmé** | 1 | p. 1 : « We introduce PrefixGuard, a neuro-symbolic method that uses learned events to connect online failure warning with finite-state execution diagnosis. » |
| 2 | Même ligne : rattachement à « H2 » (référence à lire pour H2) | **confirmé** comme lecture pertinente pour H2, portée à préciser : alerte en ligne sur les préfixes de trajectoires d'agents au premier franchissement d'un seuil ; seuil fixé par calibrage conforme fractionné sur les maxima du score de risque des seules trajectoires réussies, au budget nominal de 10 % de fausses alertes par trajectoire ; garantie marginale, sous échangeabilité, « en espérance » seulement. Le score vient d'un réseau récurrent sur des descripteurs textuels (fréquence de termes), entraîné sur les échecs ; la cible est l'échec de la tâche, pas un sabotage ; ni activations, ni processus e | 3, 4, 6, 7, 18, 19 | p. 6 : « We set γG by split-conformal calibration [2] on successful calibration runs at a nominal FAR budget of 10% (Appendix B.4). »<br>p. 18 : « For the n successful calibration trajectories, let mi = maxt ri,t and sort these maxima »<br>p. 18 : « For a scorer fixed independently of calibration, the split-conformal interpretation requires exchangeability of successful calibration and future trajectories. »<br>p. 19 : « The bound is marginal over calibration and future trajectories. »<br>p. 7 : « the split-conformal budget bounds it only in expectation. »<br>p. 3 : « We encode each record as a TF-IDF [23] vector et of weighted term frequencies, with the vectorizer fitted on training data and kept fixed thereafter. »<br>p. 4 : « From completed training trajectories Dtrain and their terminal outcomes, we derive horizon-specific targets pt without step-level annotations (Appendix B.3). » |

La même ligne 169 cite aussi « Wu, Zhou, Bates, Jaakkola 2025, « Thought calibration » (EMNLP) » : hors de ce lot (aucun PDF fourni), non vérifié ici.

### Chiffres utilisables

| Chiffre | Nature | Page | Citation |
|---|---|---|---|
| Rappel moyen de 56,1 % à 93,0 % selon les bancs, au budget nominal de 10 % de fausses alertes | auteurs | 1 | p. 1 : « At a nominal 10% FAR budget, averaged test recall spans 56.1%–93.0% across benchmarks. » |
| Fausses alertes réalisées au-dessus du budget : τ²-Bench, horizon 3, taux 0,123, les trois graines au-dessus de 0,10 | auteurs | 19 | p. 19 : « 3 .735 ± .003 .699 ± .014 .088/.087 .123 ± .003 .997 ± .002 .165 ± .006 13,42,123 » |
| Calibrage sur 718 trajectoires réussies (τ²-Bench) | auteurs | 18 | p. 18 : « τ 2 -Bench 7,583 (5,027) 1,083 (718) 1,083 (718) 1,083 (718) » |
| Règle de seuil k = ⌈(n + 1)(1 − α)⌉ ≤ n : au taux de 1 % visé par H2, il faut au moins 99 trajectoires bénignes de calibrage pour qu'un seuil existe | calcul (règle : auteurs) | 18 | p. 18 : « k = ⌈(n + 1)(1 − α)⌉ » |
| Score grossier et petit échantillon de calibrage : automates « muets » sur WebArena (k = 124 pour n = 136) | auteurs | 29 | p. 29 : « so k=⌈137 × 0.9⌉=124 and at most 12 successful calibration maxima may lie above the threshold. »<br>p. 29 : « Silence is therefore a property of the scalar-threshold readout on a small calibration pool » |

### Antériorité (R8)

- **H2 — touchée partiellement (forme générale).** Surveillance en ligne de trajectoires d'agents, alerte au premier franchissement, seuil calibré sur les seules trajectoires bénignes avec garantie par trajectoire (conforme, marginale). Ne sont pas touchés : activations de l'agent qui agit, sabotage, accumulation additive, garantie toujours valide, seuil par action à 1 %. L'« horizon » de l'article est l'horizon de prédiction, et le rappel n'y croît pas uniformément : ce n'est pas la notion de H2 (longueur de trajectoire). p. 6 : « Larger H consistently increased lead but did not uniformly raise recall » ; p. 3 : « estimating the probability that the run ends in failure within H further steps. »
- **Leçon de méthode pour le calibrage de H2** : avec un score à peu de valeurs distinctes et peu de trajectoires de calibrage, la règle de rang ne laisse aucun seuil admissible (voir chiffres ci-dessus).
- H1, lemme d'additivité, théorème négatif, transposition jeton → action, HC1, HC2b, papier B : non touchés. Les auteurs n'ont pas mesuré la performance sur tâches et agents nouveaux. p. 10 : « Performance on unseen tasks and agents remains unmeasured. »

## 2602.14161v2 — When Benchmarks Lie: Evaluating Malicious Prompt Classifiers Under True Distribution Shift

### Identité

- Auteur unique : p. 1 : « Max Fomin » ; p. 1 : « Zenity ».
- Version et date : p. 1 : « arXiv:2602.14161v2 [cs.LG] 19 Jul 2026 ».
- Venue : p. 1 : « Published at the First Workshop on Agents in the Wild: Safety, Security, and Beyond (AIWILD) at ICLR 2026. »
- Lu : en entier (27 pages).

### Affirmations du programme

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1 | Ligne 136 : « When Benchmarks Lie, arXiv 2602.14161 » (identité) | **confirmé** ; auteur et venue à ajouter : Fomin (Zenity), atelier AIWILD à ICLR 2026 | 1 | p. 1 : « Published at the First Workshop on Agents in the Wild: Safety, Security, and Beyond (AIWILD) at ICLR 2026. » |
| 2 | Ligne 136 : « à faux positifs bénins égaux, les sondes battent plusieurs classifieurs et juges génératifs sur attaques indirectes et agentiques » | **corrigé** — la phrase de contribution de l'auteur (page 2) est contredite par sa propre table 17 pour PromptGuard 2, et les attaques agentiques n'ont qu'un comparateur. Remplacer par : « à faux positifs bénins appariés et en évaluation « un jeu laissé de côté », une sonde linéaire sur les activations de Llama-3.1-8B détecte plus d'injections indirectes que LlamaGuard 3 (au taux de 3 % : 60,4 % contre 27,4 %) et que le juge Llama-3.1-8B (4,4 % : 64,9 % contre 7,1 %), et plus d'injections agentiques que ce juge (94,5 % contre 21,5 %), seul comparateur possible pour elles ; au taux de PromptGuard 2 (0,4 %), elle détecte moins d'injections indirectes (20,5 % contre 37,3 %) » | 2, 26 | p. 2 : « At matched benign FPR, activation probes lead PromptGuard 2, LlamaGuard, and Llama-as-Judge on indirect and agentic attacks »<br>p. 26 : « PG 36.7 48.5 37.3 - 100.0 0.4% »<br>p. 26 : « Ours0.4 45.8 20.4 20.5 24.3 11.5 0.4% »<br>p. 26 : « At LG’s and LJ’s operating points, the probe’s advantages on indirect injection (+33pp and +58pp) and agentic attacks are maintained. »<br>p. 26 : « At PG’s tight 0.4% FPR all detection rates drop substantially, though the probe still leads on harmful (+9pp). »<br>p. 26 : « uses a threshold calibrated to match baseline FPR=x on pure-benign datasets under LODO. PG/LG cannot evaluate agentic attacks. » |
| 3 | Ligne 136 : « sous changement de distribution » | **confirmé** : la sonde est évaluée en laissant de côté le jeu testé, et les seuils appariés sont calculés dans ce cadre ; les bases sont des outils prêts à l'emploi | 10, 26 | p. 10 : « Ours=LogReg on Llama-3.1-8B raw activations under LODO at fixed thresholds 0.5 (default) and 0.9 (conservative) » |
| 4 | Ligne 136 : rubrique « Supériorité des sondes hors attaque » (pour cet article) | **confirmé** : évaluation statique, l'auteur précise qu'elle ne mesure pas la robustesse à un attaquant adaptatif | 11 | p. 11 : « LODO is not adversarial robustness. » |

### Chiffres utilisables

| Chiffre | Nature | Page | Citation |
|---|---|---|---|
| Table 17, détection (%) — nuisible, jailbreak, indirecte, agentique, extraction — au taux de faux positifs bénins apparié : PromptGuard 2 contre sonde à 0,4 % ; LlamaGuard 3 contre sonde à 3 % ; juge contre sonde à 4,4 % | auteurs | 26 | p. 26 : « PG 36.7 48.5 37.3 - 100.0 0.4% »<br>p. 26 : « Ours0.4 45.8 20.4 20.5 24.3 11.5 0.4% »<br>p. 26 : « LG 97.4 28.9 27.4 - 15.2 3.0% »<br>p. 26 : « Ours3 63.9 55.6 60.4 87.9 54.1 3.0% »<br>p. 26 : « LJ 85.8 60.0 7.1 21.5 31.8 4.4% »<br>p. 26 : « Ours4.4 67.0 62.7 64.9 94.5 63.4 4.4% » |
| Écarts sonde moins base, injections indirectes : +33,0 (LlamaGuard 3), +57,8 (juge), −16,8 (PromptGuard 2) ; agentiques : +73,0 (juge) | calcul | 26 | p. 26 : « LG 97.4 28.9 27.4 - 15.2 3.0% »<br>p. 26 : « Ours3 63.9 55.6 60.4 87.9 54.1 3.0% » |
| Validation croisée 0,996 contre « un jeu laissé de côté » 0,912 (AUROC, Llama-3.1-8B) | auteurs | 7 | p. 7 : « 5-Fold Cross-Validation 0.996 »<br>p. 7 : « LODO (Pooled) 0.912 » |
| Juge à trois exemples 46,0 % à 3,5 % de faux positifs contre sonde 68,2 % à 3,4 % (injections indirectes) | auteurs | 21 | p. 21 : « 3 few-shot examples 46.0% 3.5% »<br>p. 21 : « Activation probe (t=0.5) 68.2% 3.4% » |

### Antériorité (R8)

- **H1 — touchée partiellement (forme de la comparaison, autre objet).** Boîte blanche contre boîte noire à faux positifs bénins appariés, sous changement de distribution ; mais sur des entrées (injections, jailbreaks), lues au dernier jeton du message de l'utilisateur, pas sur les actions d'un agent ni sur un sabotage diffus ; gain non uniforme (perte au taux de 0,4 %). p. 4 : « The defender has white-box access to LLM activations during inference but cannot modify the underlying model » ; p. 4 : « from the last token of the user message (before the generation-prompt tokens; see Appendix C.3) »
- H2, lemme d'additivité, théorème négatif, transposition jeton → action, HC1, HC2b, papier B : non touchés.

## 2504.20271v1 — Investigating task-specific prompts and sparse autoencoders for activation monitoring

### Identité

- Auteurs : p. 1 : « Henk Tillman Dan Mossing » ; p. 1 : « OpenAI OpenAI ».
- Version et date : p. 1 : « arXiv:2504.20271v1 [cs.LG] 28 Apr 2025 ».
- Venue : aucune imprimée.
- Lu : en entier (18 pages).

### Affirmations du programme

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1 | Ligne 136 : « Tillman & Mossing, arXiv 2504.20271 » | **confirmé** (OpenAI) | 1 | p. 1 : « Henk Tillman Dan Mossing » |
| 2 | Ligne 136 : « une sonde non promptée ne peut pas servir de déclencheur de collusion » | **corrigé** (modalité) — l'article dit « pourrait », dans une discussion, sans test, et pour le cas où moniteur et politique partagent les poids. Remplacer par : « une sonde non promptée, sans passe supplémentaire, pourrait avoir l'avantage de ne pas pouvoir servir de déclencheur de collusion (hypothèse de discussion, non testée, pour le cas où moniteur et politique partagent les poids) » | 15 | p. 15 : « Our approaches making use of inference time compute might fail catastrophically if the monitoring prompt acts as a trigger for this kind of collusion. »<br>p. 15 : « In these cases, “side-car” methods which involve no additional forward passes (e.g. non-prompting-based probes) may have the advantage that they are unable to act as a trigger for collusion. »<br>p. 15 : « it is possible the monitor might collude with the policy to label certain unsafe outputs as safe, particularly in cases where they share model weights. » |
| 3 | Ligne 136 : « germe de l'argument d'immunité, non développé » | **confirmé** : simple remarque de discussion ; les auteurs constatent l'absence de preuve sous forte pression de collusion | 15 | p. 15 : « However, they do not provide evidence that such techniques will perform well in cases where there is known to be strong incentive/optimization pressure for collusion. » |

### Chiffres utilisables

| Chiffre | Nature | Page | Citation |
|---|---|---|---|
| Couche la meilleure : environ 75 % de la profondeur du modèle (instantané de ChatGPT-4o) | auteurs | 3, 11 | p. 11 : « We find that a layer at model depth 75% is roughly optimal. »<br>p. 3 : « We examine activations of a previous ChatGPT-4o snapshot across all tasks. » |
| Avec assez de données, les sondes dépassent la sortie promptée du même modèle (aire sous la courbe lue sur figures, pas de chiffre imprimé) | figure | 1, 8 | p. 1 : « activation probing methods can substantially outperform this baseline given sufficient training data. »<br>p. 8 : « In particular, all probing techniques are substantially stronger than prompted model outputs in detecting hallucinations in response to SimpleQA questions. » |

### Antériorité (R8)

- **Papier B — touché faiblement** : remarque qu'un moniteur partageant les poids de la politique pourrait colluder, et qu'une sonde sans passe supplémentaire y échapperait ; aucune mesure, aucun système multi-agents, aucune co-élévation (citations de la ligne 2).
- **Transposition jeton → action — niveau jeton seulement, en performance** : le maximum sur les jetons aide les sondes sur autoencodeur parcimonieux et nuit aux sondes sur activations brutes ; la moyenne dégrade. p. 12 : « However, max-pooling decreases raw activation probing performance. » ; p. 6 : « over all the tokens in the passage, but this technique substantially degrades performance compared to simply probing the last token. »
- **H1 — touchée marginalement** : sondes contre sortie promptée du même modèle, en aire sous la courbe selon la quantité de données ; pas à faux positifs fixés, pas de sabotage.
- H2, lemme d'additivité, théorème négatif, HC1, HC2b : non touchés.

## Contrôle des citations

- Outil : `outils/controle_citations.py` (dans le dossier de travail). Pour chaque citation du rapport, il lit le texte de la page indiquée et tolère seulement les blancs et les césures (trait d'union suivi d'un retour à la ligne), après normalisation Unicode des ligatures ; il cherche d'abord dans le texte `-layout`, puis dans le texte en ordre de lecture de la même page. Code de retour 1 si une citation échoue, si une page manque, si une citation est hors d'une section d'article ou si une section d'article n'a aucune citation.
- Test préalable (R5), fichiers dans `tests-r5/` : cas justes 3 sur 3 acceptés (dont une césure et une page à deux colonnes) ; cas altérés 4 sur 4 rejetés (chiffre changé, bonne citation sur la mauvaise page, mot changé, chiffre changé sur page à deux colonnes) et section vide signalée ; un trait d'union supprimé hors fin de ligne est rejeté.
- Résultat sur ce rapport : 210 citations contrôlées, 0 échec ; 185 trouvées dans le texte `-layout`, 25 dans le texte en ordre de lecture de la même page (pages à deux colonnes). Sortie complète : `controle-rapport.txt`.

## Synthèse

1. Huit empreintes conformes ; six articles lus en entier, deux (2507.12691, 2605.26047) avec des annexes d'exemples seulement parcourues ; aucune affirmation introuvable.
2. Erreur principale : Ctrl-Z (2504.10374) — 72,7 % est le score de Defer to trusted, ni le meilleur protocole ni le résultat principal (meilleur : 87,1 % à 95 % d'utilité, 92,6 % avec surveillance non fiable) ; corriger les lignes 44, 64 et 195.
3. 2005.07821 est un article de détection (signe cumulé), sans borne : corriger les lignes 46 et 72 ; l'« analogue » montre qu'une autre statistique cumulée attrape l'attaque cachée à la somme cumulée.
4. 2602.14161 (ligne 136) : supériorité des sondes à faux positifs appariés contre LlamaGuard 3 et le juge, pas contre PromptGuard 2 à 0,4 % ; la table 17 contredit la page 2.
5. 2507.12691 (ligne 35) : cinq jeux, pas deux ; métrique surtout en aire sous la courbe ; sur le code à porte dérobée, le gain du raisonnement boîte blanche est négatif.
6. 2605.26047 (ligne 45) : réessai contre ré-échantillonnage, pas « deux intensités » ; corrections mineures : 2506.10805 (bases promptées ou affinées ; à 1 % de faux positifs, 43 % contre 55 %), 2504.20271 (« pourrait », pas « ne peut pas »).
7. H2 touchée partiellement, jamais occupée : Ctrl-Z (audit après trois coups, seuils sur l'honnête, boîte noire), PrefixGuard (alerte par trajectoire calibrée de façon conforme sur les seules réussites, 10 %, texte et non activations), 2005.07821 (principe). Contre-résultat : 2605.26047, où l'agrégation d'historique baisse la sécurité.
8. H1 touchée dans sa forme de comparaison (2507.12691, 2602.14161, 2506.10805), sur réponses ou entrées isolées, jamais sur sabotage étalé ; transposition jeton → action touchée au niveau jeton seulement (2507.12691 : sous dilution, la moyenne résiste et le maximum cède).
9. Touchés partiellement ou faiblement : théorème négatif (2005.07821, 2605.26047), HC2b (relances de 2507.12691), papier B (Ctrl-Z, 2605.26047, 2504.20271). Non touchés : lemme d'additivité, HC1. Aucune zone revendiquée occupée en entier.
10. Contrôle des citations par script contre le texte de la page citée : 210 contrôlées, 0 échec (contrôle testé d'abord : 3 cas justes acceptés, 4 cas altérés rejetés).
