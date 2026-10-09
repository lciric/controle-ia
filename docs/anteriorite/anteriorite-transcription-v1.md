# Recherche d'antériorité — niveau transcription — v1

Date : 2026-10-04 (UTC). Tâche T0.2 (volet recherche affirmative, R8), demandée par Lazar avant tout lancement.
**Statut : provenance par transcription (résumés du moteur de recherche web), NON opposable (R7).** Aucun PDF n'a été lu : arxiv.org, openreview.net, semanticscholar.org, huggingface.co, lesswrong.com, alphaxiv.org, doi.org sont refusés par la politique réseau de l'environnement. Aucun chiffre de ce document n'entre dans un préenregistrement ou un papier avant lecture du PDF empreinté.
Sources brutes (sorties structurées des sous-agents, scellées) : `docs/sources/anteriorite-web-20261004/verification-references-v1.json` (empreinte 8513bff5…), `zones-papier-A-transverse-v1.json` (d0b960cc…), `zones-papiers-C-B-v1.json` (7d6770f5…). Ressources de code vérifiées au commit (source primaire) : `docs/sources/ressources-code-v1.md` (9a31c5e7…).

## 0. Ce qui a été fait, ce qui ne l'a pas été

- Trois chaînes de sous-agents : vérification des références de l'état de l'art ; recherche affirmative zone par zone pour le papier A et les questions transversales ; même chose pour les papiers C et B ; chaque zone suivie d'une contre-vérification adverse.
- **Le budget de recherches web de la session (200) s'est épuisé** après le travail complet de quatre agents : 2607.08066 (priorité 1), 2606.10456 (priorité 2), zone « lemme » (61 requêtes), zone « théorème négatif » (45 requêtes). Les autres agents ont buté sur la limite après 2 à 6 requêtes ; je les ai arrêtés pour ne pas produire de faux « vierge » (R8). Les contre-vérifications adverses n'ont pas tourné.
- **Couverture effective** : priorités 1 et 2, lemme, théorème négatif. **Non couvert** : priorité 3 (NARCBench et 2609.03035, sauf indices incidents), priorité 4 (Terekhov et al., sauf indices incidents), zones H2, H1, Tr, H6, H8, récence, environnement (a), programme entier, HC1 à HC6, H3, statistique spatio-temporelle, H4′, H5, H7, environnement (d), et la vérification des références des lots A1, A2, A3, B1, B2, C1 à C4.

## 1. Verdict en bref

1. **Théorème négatif (T)** — occupé en boîte noire, plus largement qu'annoncé : 2606.10456 n'est pas « entièrement synthétique », il valide aussi sur des traces réelles (scores d'un moniteur génératif). Et l'énoncé du programme est trop large pour être vrai tel quel (section 3). **Nœud de décision.**
2. **Lemme d'additivité (L)** — son cœur statistique est classique (mélange normal de Howard et collègues ; dichotomie somme/max d'Arias-Castro, Candès et Plan ; détection multi-flux de Mei, de Xie et Siegmund). Reste neuf : l'application aux activations, le cadre adverse à budget, la condition de non-décorrélabilité, l'indexation agents × temps. **Nœud de décision** (revendication à reformuler ; probabilité d'originalité de 0,75 surestimée).
3. **Loi de déférence (HC1)** — 2607.08066 mesure un taux binaire (pas de gain continu ni de dose-réponse) : la bascule « collision sur la loi de déférence » n'est pas déclenchée par ce papier. Mais deux travaux absents de l'état de l'art mesurent déjà un déplacement *continu* des juges par technique de persuasion (2508.07805) et la sycophancie comme déférence continue (2606.07897), et le « poids du conseil » de la psychologie du jugement est algébriquement g. **Nœud de décision** (collision plus large qu'annoncé, à verrouiller sur PDF).
4. **Contre-mesures (HC5)** — 2607.08066 recommande déjà l'appariement moniteur–vérificateur de familles différentes (réduction jusqu'à 45 % contre 6 %) : le « quorum hétérogène » entre juges est partiellement occupé. **Nœud de décision** (reformulation).
5. **Accumulation séquentielle sur sondes (H2)** — zone non cherchée ; un voisin nouveau apparu incidemment (2607.06503 : cascade de sondes sur activations d'agents, par tour, à rappel calibré) doit être lu. Réserve.

## 2. Priorités du brief

### 2.1 arXiv 2607.08066 — « Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring »
- Existe. Auteurs : Jennifer Za, Julija Bainiaksina, Nikita Ostrovsky, Tanush Chopra, Victoria Krakovna. v1 du 9 juillet 2026 ; aucune v2 vue. Projet LASR Labs 2025 ; version antérieure « Persuade Me If You Can » (atelier R2-FM, ICML 2025).
- Dispositif : 40 tâches ; agents Gemini 2.5 Pro, GPT-4.1, Llama 4 Maverick ; moniteurs Gemini 2.5 Flash, GPT-4.1, Claude 3.7 Sonnet ; verdict APPROVE/REJECT sur au plus 5 tours ; métrique = taux d'acceptation ajusté à une base. Entièrement boîte noire, aucune sonde.
- Résultats rapportés : l'accès à la chaîne de pensée augmente l'acceptation d'actions contraires à la politique de 9,5 points (24,4 % contre 33,9 %) ; vérificateur de faits d'une autre famille : réduction jusqu'à 45 %, contre 6 % avec le même modèle.
- Familles d'attaque : 5 stratégies prescrites (logique, émotion, urgence, crédibilité, identité partagée) et 9 classes a posteriori ; ni flatterie/supplication, ni approbations forgées, ni usurpation de l'instructeur, ni ordres comme familles manipulées (une mention isolée de « policy fabrication », à vérifier).
- Ce qui reste au papier C face à lui : gain continu g et dose-réponse ; opposition sondes/juges ; auto-incrimination ; usurpation stylistique ; taxe de déplacement ; paraphrase.
- Code et données annoncés publics (dépôt non localisé, licence inconnue).

### 2.2 arXiv 2606.10456 — « The Distributed Detectability Band Against Marginal-Preserving Attacks »
- Existe. Auteurs : Zhang Qinqin, Gao Yuze ; aucune affiliation dans le papier selon les résumés (Yuze Gao : ingénieur de recherche à A*STAR, profil traitement de la langue). v1 du 9 juin 2026, v2 du 13 juin 2026. Préprint non relu.
- Proposition 1 rapportée : tout moniteur dont la règle ne dépend que de la marginale *empirique* d'attaque a une puissance égale à son taux de faux positifs, à budget de furtivité nul (distance de Kolmogorov-Smirnov nulle entre marginales empiriques).
- Moniteurs « B » (somme cumulée de Page, test séquentiel du rapport de vraisemblance, modèle de Markov caché, test des suites, autocorrélation) : AUROC 0,79–0,97 en synthétique ; puissance maximale 0,688 à 1 % de faux positifs. Consistance quand l'horizon croît (un seul résumé) ; aucune garantie toujours valide, aucun processus e.
- Traces réelles : agent Qwen2.5-7B-Instruct, moniteur Llama-3.2-3B-Instruct, 120 × 24 scores. **Source primaire (dépôt au commit b35f23838d14)** : `results/realdata_detect.json` donne, pour les moniteurs B à T = 24, une AUROC de 0,586 (autocorrélation) et 0,472 (rapport de vraisemblance séquentiel), et en concaténant les épisodes jusqu'à T_eff = 400 : 0,982 et 0,990 ; moniteurs A à T = 24 : 0,458 (moyenne), 0,543 (max), 0,562 (moyenne des k plus hauts).
- Un seul agent ; aucune activation ; aucun énoncé d'invariance au budget total sous décalage de moyenne.
- Dépôt de code sans licence (lecture et citation, pas de copie).

### 2.3 NARCBench (2604.01151) et 2609.03035 — non vérifiés (budget épuisé)
Indices incidents, à confirmer : titre « Detecting Multi-Agent Collusion Through Multi-Agent Interpretability » ; transfert zéro-shot 0,60–0,86 (un résumé) ; aucune agrégation séquentielle vue. 2609.03035 : « You Can't Escape Your Own Activations: Evaluation Awareness and Multi-Agent Monitoring » (Das, Ponde, More, Gupta), Qwen3-32B-AWQ et GPT-OSS-20B, blackjack à 4 agents. Source primaire partielle : le dépôt NARCBench (MIT, commit 85fea3be2a9d) confirme cinq techniques de sondage et des modèles de 20 à 70 milliards de paramètres. **La question de la bascule (suite séquentielle par l'équipe) reste sans réponse.**

### 2.4 Terekhov et al. (2606.08892) — partiellement identifié
Indices incidents (deux agents) : « Diffuse AI Control on Fuzzy Tasks » (Mikhail Terekhov, Caglar Gulcehre, Vivek Hebbar, Joe Benton), 8 juin 2026, révisé le 17 juin ; billet sur le blog Alignment Science d'Anthropic. Cadre d'équipe rouge pour évaluer des interventions d'entraînement contre le sabotage diffus de génération d'idées d'expériences, avec un juge plus faible. **Code et données : inconnus** — la question qui conditionne T0.5 reste ouverte.

## 3. Zones cherchées

### 3.1 Théorème négatif — partiellement occupée
- Axe temps, boîte noire : occupé par 2606.10456 (ci-dessus).
- Analogues anciens, à citer en fond : canaux temporels couverts qui imitent la marginale du trafic (Gianvecchio et Wang, 2007-2008) ; attaques polymorphes par mélange (Fogla et collègues, 2006) ; stéganalyse markovienne (préserver le premier ordre, être pris au second) ; détection de rupture de copule (Bücher, Kojadinovic, Rohmer, Segers, 2014) ; rupture de corrélation (Wied, Krämer, Dehling, 2012) ; test d'indépendance séquentiel toujours valide (Podkopaev et collègues, 2023) ; martingales d'échangeabilité (Vovk) ; détection de comptes coordonnés par synchronisation (CopyCatch).
- Axe agents, voisins nouveaux : 2607.11751 (« When Local Monitors Miss Compositional Harm », frontière d'observabilité locale, un seul résumé) ; 2607.24893 (suite) ; 2608.02698 (Ghanem, boîte noire, information mutuelle).
- **Mise en garde mathématique** (relevée par deux agents indépendamment, et vraie) : à marginale par pas préservée, une corrélation change la loi des agrégats — la variance de la moyenne et de la somme (facteur de variance de long terme ≈ (1+φ)/(1−φ) pour un processus autorégressif d'ordre 1), la loi du max, les excursions d'une somme cumulée lue séquentiellement. « Toute statistique fondée sur les marginales (max, moyenne, somme cumulée) a une puissance égale au taux de faux positifs » est donc **faux tel qu'écrit**. Énoncé correct possible : *toute statistique invariante par permutation des indices (i, t), face à une attaque qui préserve la loi du multi-ensemble des scores (par exemple une attaque par réordonnancement d'un échantillon honnête), a une puissance égale au taux de faux positifs* ; seuls les agrégateurs sensibles à l'ordre (autocorrélation, co-élévation, et aussi les lectures séquentielles de la somme) peuvent détecter. C'est précisément l'objet de T0.3.
- Reste revendicable : transposition aux activations ; co-élévation entre agents ; unification temps × agents comme un même groupe de permutations ; garantie toujours valide.

### 3.2 Lemme d'additivité — partiellement occupée (cœur classique)
- Fond : sous un processus e de mélange normal sur la somme des scores, la statistique ne dépend que de S_t et V_t (Howard, Ramdas, McAuliffe, Sekhon, 2021) : l'invariance de la puissance à la répartition de B = Σδ est un corollaire presque immédiat. Somme contre max (Arias-Castro, Candès, Plan, 2011 ; Donoho et Jin ; Ingster) ; somme de CUSUM locaux (Mei, 2010) ; mélange sur la fraction de flux affectés (Xie et Siegmund, 2013) ; délai gouverné par la divergence cumulée (Liang, Tartakovsky, Veeravalli, 2023) ; adversaire couvert (Ramtin, Nain, Towsley, 2601.20022) ; loi en racine carrée de la communication furtive (Bash, Goeckel, Towsley) ; compromis détectabilité/dommage (Bai, Pasqualetti, Gupta, 2017).
- Voisins contrôle de l'IA, boîte noire : 2411.17693 (Wen et collègues : macro-protocole bayésien qui accumule une crédence sur les tâches) ; 2506.10949 (moniteurs séquentiels légers contre attaques par décomposition) ; 2604.08608 (seuil de détectabilité des décompositions : impuissance formelle des classifieurs par sous-tâche) ; 2606.20746 (« Amplify, Don't Create » : l'accumulation amplifie une marge faible, elle n'en crée pas) ; 2607.07368, 2607.02514, 2605.31593 (fragmentation, boîte noire) ; 2601.05427 (Gauthier, Bach, Jordan : détection toujours valide de déviations stratégiques multi-agents) ; billet de Hebbar (Redwood, avril 2025) sur les menaces diffuses.
- Voisins boîte blanche : 2607.06503 (cascade de sondes sur activations d'agents, tour par tour, garantie de rappel globale ; cible : l'échec, pas le sabotage) ; 2607.06807 (détection de comportements malveillants par activations en multi-agents) ; 2609.03035.
- Reste revendicable : l'énoncé adverse (l'attaquant choisit la répartition sous un budget total, le défenseur garde une garantie toujours valide), la distinction puissance de Wald / garantie toujours valide appliquée à ce jeu, la condition de non-décorrélabilité dommage/furtivité en boîte blanche, l'indexation agents × temps, et la mesure sur activations réelles.

## 4. Travaux nouveaux, absents de l'état de l'art, à verrouiller sur PDF

| Identifiant | Titre (selon les résultats) | Touche | Niveau provisoire |
|---|---|---|---|
| 2508.07805 | Can You Trick the Grader? Adversarial Persuasion of LLM Judges (Findings d'EMNLP 2025) | HC1 (déplacement continu par technique sur 14 juges) | partiel, possiblement plus |
| 2606.07897 | Pander Score: A Continuous Measure of Sycophancy as Epistemic Deference | HC1 (mesure continue de déférence) | partiel |
| 2508.05625 | How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations | HC2, HC2b | adjacent |
| 2607.06503 | Doomed from the Start: Early Abort of LLM Agent Episodes via a Recall-Controlled Probe Cascade | H2 | partiel (cible différente) |
| 2607.06807 | When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems | B (boîte blanche multi-agents) | adjacent à partiel |
| 2601.05427 | Anytime Detection of Strategic Deviations in Multi-Agent Systems | B, L | adjacent |
| 2607.11751, 2607.24893 | Distributed backdoors in multi-agent systems (frontière d'observabilité) | T axe agents | partiel |
| 2606.20746 | Amplify, Don't Create: Temporal Accumulation for Slow-Burn Prompt Injection | L, T | adjacent |
| 2604.08608 | Semantic Intent Fragmentation | L (impuissance par action) | adjacent |
| 2506.10949 | Monitoring Decomposition Attacks in LLMs with Lightweight Sequential Monitors | H2 (boîte noire) | adjacent |
| 2411.17693 | Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats | H2, L (boîte noire) | adjacent |
| 2609.06966 | MOLE: Detecting Insider Threats in AI Agents | banc multi-comptes, multi-jours | adjacent |
| 2605.11135, 2606.07624, 2512.22154 | cartes de contrôle multi-agents ; inférence séquentielle pour LLM ; défis pratiques du monitoring | fond | adjacent |
| 2601.04603 | Next-generation Constitutional Classifiers (Anthropic) | HC2 (sonde dans une défense de production) | adjacent |

Pistes citées de mémoire par les agents, **non vues** dans un résultat (aucune valeur de preuve) : « weight of advice » (paradigme juge-conseiller, psychologie) comme forme exacte de g ; travaux montrant qu'un modèle peut déplacer ses propres activations en contexte (menace pour HC2) ; « Control Tax » (Terekhov et collègues, 2025 : proximité de vocabulaire avec la taxe de déplacement) ; sondes en production chez un grand laboratoire comparées à des classifieurs génératifs sous attaque adaptative.

## 5. Ce qu'il faut pour finir
1. Relever le budget de recherches web de la session (variable `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`) ou ouvrir une session neuve, puis relancer les chaînes arrêtées (reprise à partir du cache).
2. Ouvrir l'accès réseau à arxiv.org et export.arxiv.org (et openreview.net) pour la vérification sur PDF empreinté, page citée — T0.2 proprement dite ; à défaut, Lazar dépose les PDF.
3. Ordre de lecture des PDF : 2607.08066, 2508.07805, 2606.07897, 2606.10456, 2604.01151, 2609.03035, 2606.08892, 2607.06503, 2512.03109, 2605.27690, puis section 6 de l'état de l'art.
