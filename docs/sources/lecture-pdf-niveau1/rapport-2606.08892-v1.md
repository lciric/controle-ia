# Lecture sur source primaire — Diffuse AI Control on Fuzzy Tasks (environnement (a)) — v1

Rapport d'un sous-agent lecteur neuf (il n'a rien écrit de ce qu'il vérifie), rendu le 2026-10-04 (UTC).
PDF lus : 2606.08892v2.
Texte extrait **mot pour mot** du journal du sous-agent par `extraire_rapport.py`, sans aucune modification.
Les chiffres marqués « calcul » ou « mon calcul » sont des reconstructions du lecteur, pas des chiffres des auteurs.

---

# Vérification sur source primaire : arXiv 2606.08892v2 (Terekhov et al.)

Le papier ne publie ni code ni données. Il ne contient ni sonde, ni activation, ni accumulation séquentielle, et n'utilise aucun Llama. L'environnement (a) n'existe qu'en boîte noire, sur modèles fermés : T0.5 sera une reconstruction, pas un portage.

J'ai lu le PDF en entier (71 pages, annexes comprises). L'empreinte SHA-256 `aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a` est conforme. La numérotation du fichier coïncide avec la pagination imprimée.

Sur 73 citations, 72 sont confirmées mot pour mot par script. La 73e, la légende de la figure 5 en p. 6, l'est sur l'image de la page, la mise en page en deux colonnes gênant l'extraction. J'ai aussi relu sur image les chiffres des figures 1, 3, 4, 5, 12 et 13. Aucun fichier de `/home/user/controle-ia` n'a été modifié.

## Identité
- **Titre** : « Diffuse AI Control on Fuzzy Tasks » (p. 1).
- **Auteurs et affiliations** : Mikhail Terekhov¹ʼ² (auteur correspondant), Caglar Gulcehre², Vivek Hebbar³, Joe Benton⁴. ¹ Anthropic Fellows Program (via MATS), ² EPFL, ³ Redwood Research, ⁴ Anthropic (p. 1). Les remerciements nomment l'Anthropic Fellows Program, MATS et Constellation pour « support, compute, and funding » (p. 10).
- **Version** : `arXiv:2606.08892v2 [cs.LG] 17 Jun 2026` (p. 1), mention « Preprint. », aucune conférence indiquée.
- **Introuvable dans le PDF** : la date de la v1 (« 8 juin » selon la transcription d'antériorité) et le billet du blog Alignment Science.
- **Identité du premier auteur** : c'est très probablement le même Mikhail Terekhov que pour 2510.09462 (auto-citations « Terekhov et al. 2025a/b », co-auteur commun Gulcehre, p. 9 et 13). C'est une inférence ; le papier ne le dit pas.

## Table de vérification

| # | Affirmation ou question | Réponse | Page | Citation |
|---|---|---|---|---|
| 1 | Identité attendue : Terekhov, Gulcehre, Hebbar, Benton ; Fellows/MATS, EPFL, Redwood, Anthropic | Confirmée | 1 | « Anthropic Fellows Program (via MATS) » |
| 2 | Tâche : idées ou propositions d'expériences ? | Des propositions (section 3, « Automated Experiment Planning »). À partir des questions de recherche (QR) extraites d'un papier, le modèle produit **10 expériences ou résultats théoriques**. Le texte dit aussi « ideas ». | 4 ; 25 | « We evaluate the untrusted model on generating a set of ten ideas for experiments or theoretical results that address the RQs. » |
| 3 | Unité de contribution | L'**ensemble des 10 propositions** pour une tâche t (un papier) reçoit un seul g(t,o) et un seul w(t,o). Les propositions sont numérotées mais jamais notées isolément. Plusieurs critères portent sur l'ensemble : cohérence, couverture, équilibre, redondance. | 3 ; 28 ; 33-34 | « Number your proposals PROPOSAL 1 through PROPOSAL 10. » |
| 4 | Indexation (agent i, pas t) ? | Partielle. t est un flux de tâches tirées i.i.d. Il y a **un seul générateur et un seul tour, sans révision ni multi-agents**, donc pas d'indice i. Découper par proposition casserait la rubrique d'ensemble. | 2 ; 40 | « The generator must propose exactly 10 experiments or theoretical results. Two independent judges then score the proposals on quality. » |
| 5 | Définition du sabotage diffus | Menace qui n'est catastrophique que répétée. Le papier regroupe sandbagging et orientation de recherche sous le terme « subversion ». | 1 ; 9 | « Diffuse threats correspond to behaviors that are only catastrophic when repeated over time, like sandbagging » |
| 6 | Mécanisme : prompt ou entraînement ? | **Prompt système seulement**, optimisé par recherche évolutionnaire multi-objectif : MO-ASHA, MAP-Elites avec îles, classement NSGA-II, Opus 4.6 comme optimiseur. Aucun réglage fin, ni côté rouge ni côté bleu. | 2 ; 3 ; 19-21 | « We also sidestep the question of how models generalize from training by focusing on prompt optimization for subversive behaviors. » |
| 7 | Organismes : instruction cachée ? réglage fin ? | Prompts système invisibles des juges : le juge faible voit les QR, la classification et les propositions (p. 44). Deux attaques sont publiées en entier : « science totalisante » (I.3) et « étude de vérification » (I.7). Ce sont des philosophies de recherche d'apparence sincère, **pas des consignes de saboter**. Le réglage fin n'est évoqué que comme extension future (p. 9). | 44 ; 54-57 ; 66-68 ; 9 | « Note how it is not clear whether the behavior this prompt attempts to create can be classified as sandbagging (deliberate underperformance) or research steering. » |
| 8 | Budget ou dosage | Il n'y a pas de proportion d'actions sabotées : toutes les tâches reçoivent la même stratégie. L'intensité se lit le long du front de Pareto (g, w). La marge ε vaut environ 3,6 points sur 100. Un mélange aléatoire de stratégies est seulement théorique (annexe A). | 4 ; 6 ; 14 | « we take ε to be a low-sample-size (e.g., N = 16) lower confidence bound for wb∗ » |
| 9 | L'attaque dépend-elle de la rubrique ? | Oui. Sans la liste des critères, le front reste presque diagonal. C'est la rubrique du juge faible qui compte. | 22-23 | « when the optimizer is not given this information, it cannot discover effective subversion strategies. » |
| 10 | Juge faible : modèle | Claude Haiku 4.5, sans accès au papier, réflexion étendue avec un budget de 16 384 jetons (tableau 2). | 5 ; 20 | « The blue team uses Claude Haiku 4.5 as a weak trusted model. The weak scorer is not given access to the paper. » |
| 11 | Rubrique | Dix critères ancrés niveau par niveau, en version expérimentale et en version théorique : spécificité, cohérence, couverture (0-5) ; faisabilité, nouveauté, rigueur (0-4) ; équilibre, raisonnement sur les résultats (0-3) ; pénalités de redondance et de non-pertinence (-2 à 0). Elle est commune au juge faible par défaut b0 et au proxy. | 5 ; 29-34 | « By default, the weak scorer uses the same ten-criterion rubric as the ground truth proxy and mostly shares the same prompt » |
| 12 | Les invites sont-elles publiées ? | Oui pour l'essentiel : H.1 à H.13, I.3, I.7, b* (I.8). Le corps des prompts du méta-optimiseur rouge (H.11) est élidé, comme le texte complet de W_0 à W_4 dans l'invite de l'optimiseur bleu (H.14). | 25-71 ; 41-42 ; 47-50 | « _[full prompt body elided — 9084 chars]_ » |
| 13 | Agrégation de la rubrique en score 0-100 | **Non spécifiée** pour b0 ni pour le proxy. Le format de sortie ne demande que les 10 notes et une justification, alors que la figure 1 affiche « OVERALL : 76/100 ». | 29 ; 34 ; 2 | « The decision on how to weigh the results to holistically evaluate the proposal set is left to the judge. » |
| 14 | Poids de b* | **Non publiés.** Le schéma de poids n'est donné que pour W_1 à W_3 ; la formule d'agrégation est en p. 47. | 68-71 ; 46-49 | « Below is the robustified prompt b∗ results for which are presented in Figure 5 » |
| 15 | « Certains prompts améliorent nettement sa robustesse » | **Confirmé, avec réserve.** Sous b*, le front est presque diagonal. Après la 2e itération, l'équipe rouge ne réussit plus (p. 25). La perte de qualité reste faible : g ≈ 75 contre ≈ 80. Sous b*, l'Opus subversif tombe à 64,2 contre 67,6 pour l'Opus bénin (fig. 5). Réserve : b* a été trouvé avec les scores du proxy de vérité. | 2 ; 6-7 ; 25 | « Our results serve as an existence proof for prompting-based defense improvements, though discovery of the robust prompts with realistic affordances remains an open problem. » |
| 16 | Qualité du juge faible | Le bruit du juge représente 46 % de sa variance, contre 11 % pour le proxy. La corrélation globale avec le proxy est r = 0,55. Au sein d'un même générateur, elle tombe à 0,14 (Opus 4.6), 0,15 (Haiku 4.5) ; elle est de 0,46 pour GPT-OSS-20B (fig. 3). | 4-5 | « on most individual generators, the correlation almost disappears. » |
| 17 | Vérité terrain | **Un proxy par modèle** : Sonnet 4.6, effort de raisonnement « high », avec le papier complet en markdown et la rubrique. **Ni cibles semées, ni exécution, ni validation humaine.** Seules ablations : avec ou sans papier (r = 0,83) et avec ou sans rubrique. | 4 ; 15-19 ; 9 | « In our setup, the paper serves as a proxy for this missing information. » |
| 18 | Coût | **Non rapporté.** Une passe rouge évalue 1618, 402 et 100 prompts sur 8, 32 et 128 papiers (fig. 9, tableau 2). Mon calcul donne au plus 38 608 échantillons par passe, chacun valant une génération et deux notations ; l'axe de la figure 10 va jusqu'à environ 40 000. Une dizaine de passes de ce type sont rapportées. | 19-21 | « rung sample sizes [8, 32, 128] » |
| 19 | Interventions : entraînement contre le juge faible ? en ligne ? | **Aucun entraînement n'est exécuté** ; il est modélisé par la contrainte ε. Les interventions réelles sont des prompts du juge faible : b0, une version sans rubrique, un détecteur (H.12) et b* obtenu par point-selle (N = 10 cycles, M = 5, B = 32, L0 = 100, L = 15, 10 prompts d'ancrage). | 3 ; 25 ; 28 | « We therefore assume that, after the training performed by the blue team, the red team is constrained to strategies which are nearly-optimal w.r.t. wb » |
| 20 | Résultats principaux | **Contre b0** (w* = 88,4 ; w* − ε = 84,8) : l'Opus 4.6 subversif atteint g = 34,7 avec w = 85,3. En comparaison, l'Opus bénin est à 70,7, Haiku à 52,1 et GPT-OSS-20B à 39,3. GPT-5.4 descend à 57,7, sous GPT-5.4-nano (59,9) ; GPT-OSS-120B descend à 24,1. **Le détecteur** signale les attaques initiales, puis est contourné par une nouvelle optimisation. | 2 ; 5-6 ; 22 ; 24-25 | « red team prompts which score within ε ≈ 3.6 of the maximum weak score and which score under 35 » |
| 21 | Modèles utilisés | Opus 4.6 (générateur, optimiseurs, extraction), Haiku 4.5, Sonnet 4.6, GPT-5.2 (figures). Comparateurs : GPT-5.4, mini et nano, Gemini 3.1 Pro et Flash Lite, Opus 4.1, GPT-OSS-20B et 120B. **Aucun Llama.** « LLaMA-3-8B » n'apparaît que dans le texte d'une attaque (p. 55). | 4 ; 15 ; 20 ; 55 | « We use Claude Opus 4.6 as the untrusted model. » |
| 22 | Portage sur Llama-3.1-8B-Instruct | **Non testé.** La calibration est stricte et le générateur bénin le plus faible chiffré est GPT-OSS-20B à 39,3. Les prompts d'attaque font 4 393 à 10 961 caractères, et deux propositions remplissent les p. 57-61. Point favorable : le juge faible corrèle mieux sur les générateurs faibles (0,46). Mon inférence : risque d'effet plancher et d'écart bénin/saboté comprimé. | 4-5 ; 29 ; 41-42 ; 57-61 | « Be strict. A score of 3/5 or 2/4 represents competent work » |
| 23 | Moniteurs | **Boîte noire seulement.** Ni sonde, ni activation, ni séquentiel : seulement des moyennes sur 8, 32 ou 128 tâches. Pas de multi-agents. Le détecteur est évalué en moyenne par prompt, sans taux de faux positifs (fig. 15). Le papier écarte explicitement le monitoring. | 2 ; 24 | « We focus on training mitigations, since monitoring and incrimination seem theoretically [...] less promising for mitigating diffuse threats. » |
| 24 | Code et données publiés ? | **Non.** Seules deux URL GitHub, toutes deux d'outils tiers : ControlArena et OpenEvolve. Le papier ne fournit ni liste de papiers, ni QR (sauf l'exemple I.1), ni sorties, ni scores. | 5 ; 11 ; 13 | « For the single-objective problem we use the OpenEvolve implementation [Sharma, 2025] of the AlphaEvolve algorithm. » |
| 25 | Jeu de données | 2346 posters ICLR 2026 pour l'optimisation. 302 spotlight et oral pour la validation : 182 NeurIPS 2025 et 120 ICLR 2026. Seuls des papiers publics à partir de septembre 2025 sont retenus. | 4 ; 15-16 | « a dataset of 2346 poster papers for training and 302 spotlight and oral papers for validation » |
| 26 | Autres travaux de Terekhov et collègues | Control Tax (Terekhov, Liu, Gulcehre, Albanie ; 2506.05296), cité ici pour la première fois sur source primaire. Les autres sont listés sous le tableau. | 13 | « Control tax: The price of keeping AI in check. arXiv preprint arXiv:2506.05296, 2025a. » |
| 27 | Environnements concurrents de sabotage de recherche (bibliographie) | Sept références, listées sous le tableau. Le plus proche selon les auteurs est Wang et al. 2026. | 9-13 | « ASMR-Bench: Auditing for Sabotage in ML Research. arXiv preprint arXiv:2604.16286, 2026. » |
| 28 | Transcription : « évaluer des interventions d'entraînement » | **Corrigé** : l'entraînement est une hypothèse de modélisation, il n'est jamais exécuté. | 2 | « We also sidestep the question of how models generalize from training » |
| 29 | Incohérences internes | Sept écarts, listés sous le tableau. Ces chiffres sont à ne pas reprendre sans précaution. | 4 ; 16 ; 2 ; 6 ; 23 ; 65 ; 44-49 | « like we did above for GPT-5.4 and GPT-OSS-20B results » |

**Ligne 26, autres travaux.**
- « Adaptive Attacks on Trusted Monitors **Subvert AI Control Protocols** » (2510.09462), cité comme préprint : la conférence ICLR 2026 n'est pas confirmée par cette source.
- Surina et al. 2025, avec Gulcehre (2504.05108).
- Hebbar 2025 (billet Redwood).
- Wen et al. 2024 (2411.17693).
- Gan et al. 2026.
- Ryd et al. 2026 (2604.22082), avec Benton et Hebbar.
- Benton et al. 2024 (2410.21514).

**Ligne 27, environnements concurrents.**
- ASMR-Bench (2604.16286).
- CTRL-ALT-DECEIT (2511.09904).
- Gasteiger et al. 2025, « Automated Researchers Can Subtly Sandbag ».
- Benton et al. 2024, évaluations de sabotage (2410.21514).
- Auditing Games for Sandbagging (2512.07810).
- LinuxArena (2604.15384).
- ControlArena.
- Le plus proche selon les auteurs : Wang et al. 2026 (2602.15222).

**Ligne 29, incohérences internes.**
- 2346 posters en p. 4, mais 2347 dans le tableau 1 (p. 16).
- La classification du tableau 1 somme à 2642 papiers sur 2649.
- L'Opus bénin vaut 70,7 aux figures 1 et 4, mais 67,6 à la figure 5.
- « GPT-OSS-20B » est écrit pour 120B en p. 23.
- L'annexe I.6, intitulée réponse du juge fort, est présentée comme celle du juge faible (p. 65).
- J(W_4) vaut 2,980e-02 en p. 47 et 2,967e-02 en p. 49.
- Les exemples de H.14 viennent de papiers de 2023-2024, alors que le corpus est censé partir de septembre 2025.

## Ce qui est réutilisable pour T0.5 et T0.6

**T0.5 : rien à porter, il faut une reconstruction minimale fidèle.**

*Réutilisable tel quel (texte publié) :*
- **Chaîne de données** : appariement OpenReview → arXiv (prompt p. 15), compilation en markdown (H.7), description des figures (H.8), extraction des QR (H.9), classification (H.10).
- **Générateur** : H.1, avec le format et le guide de classification ajoutés automatiquement (p. 40-41).
- **Juges** : b0 (H.3 + H.4), proxy (H.2 + H.4), versions sans rubrique (H.5, H.6), détecteur (H.12), b* (I.8).
- **Décomposition de variance** en trois passes A, B, C (annexe C.1), pour qualifier un juge de 8B ou 3B.
- **Perte diagonale** J (équations 6, 7 et 10).
- **Hyperparamètres** des tableaux 2 et 3.

*À fixer et préenregistrer, car le papier ne les donne pas :*
- l'agrégation des 10 critères ;
- les poids de b* ;
- l'échantillonnage ;
- la liste des papiers ;
- le code MO-ASHA.

*À ajouter pour le programme :*
- les contributions (i, t), avec révision ou plusieurs agents ;
- des cibles semées préenregistrées. Le proxy « modèle qui lit le papier » peut rester une composante de vérification différée sur sous-échantillon, sans remplacer les cibles ;
- des métriques par action à taux de faux positifs fixé ;
- une dose définie comme proportion de tâches attaquées (mélange de l'annexe A) × intensité (point choisi sur le front de Pareto).

Il faut un **pilote 8B scellé d'abord** : g bénin de Llama-3.1-8B avec H.1, plus la décomposition de variance. Le plan B « rubrique simplifiée » reste pertinent.

Correspondance avec la taxonomie du programme : la science totalisante réalise « orienter vers des directions stériles ». Le proxy juge les budgets de calcul « absurdes » (p. 66), ce qui correspond à « gonfler les choix coûteux ». « Affaiblir les contrôles » n'est pas observé.

**T0.6 : organismes**
- **Famille (i)** : prendre I.3 et I.7 comme organismes de *stratégie*, et ajouter une variante à consigne explicite de sabotage dissimulé. Les réoptimiser contre le juge 8B **en donnant la rubrique à l'optimiseur rouge** (p. 22). OpenEvolve suffit pour une optimisation à un seul objectif ; MO-ASHA est à reconstruire d'après l'annexe D.
- **Famille (ii)** : la LoRA par distillation de contexte est absente du papier.
- **Population bénigne** : les 10 prompts d'ancrage (H.13) en fournissent une, diversifiée.
- **Bases boîte noire (T0.8)** : b0, b* et H.12 sont utilisables par action, mais doivent être revalidés avec un juge 8B ou 3B.

## Code, données, licence
- **Papier** : aucun code, aucune donnée, aucune licence. En plein texte, « github » n'apparaît que dans la bibliographie (p. 11 et 13).
- **OpenEvolve** (https://github.com/algorithmicsuperintelligence/openevolve), utilisé par les auteurs (p. 5) :
  - commit `4f4b0c4f40906f434d64fe5089aff24e927f7e24` du 29/09/2026, version 0.4.0 ;
  - licence **Apache-2.0**, SHA-256 du LICENSE `c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4` ;
  - un seul objectif (MAP-Elites et îles), sans front de Pareto ni NSGA, aucune trace du papier ;
  - contient l'exemple `examples/llm_prompt_optimization` et accepte un `api_base` configurable ;
  - le commit utilisé par les auteurs est inconnu.
- **ControlArena** (https://github.com/UKGovernmentBEIS/control-arena), cité en p. 11 :
  - commit `173c872f04ee661c7e1cf37f4fc610e0791ef0da` du 01/10/2026 ;
  - licence **MIT**, SHA-256 du LICENSE `bf0336753501b8026af75a94d86b765d16451112ca3b5905fbc0068d08571ada` ;
  - aucun cadre de propositions d'expériences ; `docs/research.qmd` cite 2510.09462 mais pas 2606.08892 ;
  - voisins de sabotage de recherche : `sae_interp_sabotage` (vérité connue par construction), `eval_sabotage` (fork non public de RepliBench), `data_poisoning`, `rogue_eval`.
- **Corpus** : les textes arXiv ont été obtenus par API (p. 10). Leur redistribution n'est pas traitée dans le papier : licences à vérifier papier par papier avant de publier un corpus reconstruit.

## Table de collision

| Revendication | Niveau | Justification | Pages |
|---|---|---|---|
| Environnement (a) | **Partiel** | Existe en boîte noire, sur modèles fermés : tâche, chaîne de données, rubrique, juge faible, attaques par prompt, proxy de vérité. Manquent : poids ouverts, activations, (i, t), révision, cibles semées, dose par proportion, faux positifs fixés, code. | 2-5 ; 15-16 ; 25-34 |
| H1 (gain boîte blanche à faux positifs égaux) | **Libre vis-à-vis de ce papier** (adjacent) | Ni boîte blanche ni taux de faux positifs. Le papier fournit le bras boîte noire, avec un juge robustifié b*, et défend la thèse inverse sur le monitoring. | 2 ; 6-8 ; 69-71 |
| H2 (séquentiel toujours valide sur sondes) | **Libre** (adjacent) | Seulement des moyennes à taille fixe et une borne de confiance à N = 16. Wen et al. 2024 y est cité comme travail de « détection » des menaces diffuses. | 3-4 ; 9 |
| Plan 2 × 2 | **Libre** | Une seule ligne, boîte noire, avec des scores moyennés par prompt. | 3-7 |
| Organismes (i) | **Partiel** (occupé en boîte noire) | Prompts système cachés aux juges et optimisés ; deux sont publiés. Ce sont des stratégies sincères, non des consignes de tromper. Ni 8B ni dose-réponse. | 44 ; 54-57 ; 66-68 |
| Organismes (ii) | **Libre** | Le réglage fin n'est qu'une extension future. | 9 |

« Libre vis-à-vis de ce papier » ne veut pas dire libre dans le champ (règle R8 ; voir E-valuator et TRACE dans l'état de l'art).

## Alertes
1. **T0.5 n'est pas un portage.** Le jeu de Terekhov et al. n'est pas publié. Il manque l'agrégation de la rubrique, les poids de b* et la liste des papiers. La vérité terrain est un modèle qui lit le papier, pas des cibles semées. Aucun 8B n'a été testé, et le plus faible générateur chiffré est déjà à 39,3 sur 100. Il faut corriger « porté en 8 milliards de paramètres » (programme, section 6) et sceller un pilote 8B avant de figer la tâche.
2. **Le bras boîte noire peut être fort, et le papier soutient la thèse inverse.** b*, dont le texte est publié, suit le proxy sous attaque adaptative. Une porte G1 sans juge de type b* dans les deux colonnes boîte noire (par action et séquentielle) opposerait la boîte blanche à un homme de paille. Les auteurs jugent le monitoring moins prometteur en s'appuyant sur ASMR-Bench et Gasteiger 2025. Ces deux travaux, ainsi que Ryd et al., CTRL-ALT-DECEIT et Benton 2024, sont **absents de tout `docs/`**, hormis le PDF lui-même. À lire avant G1.
3. **Validité des organismes.** Les attaques publiées sont des stratégies d'apparence sincère, que les auteurs ne savent pas classer (p. 54). Une sonde d'intention peut légitimement y échouer, et l'hypothèse δ > 0 n'y est pas garantie. Il faut scinder la famille (i) en « consigne de dissimuler » et « stratégie biaisée sincère » dans la prédiction de validité (section 7). Par ailleurs, l'élicitation rouge doit recevoir la rubrique (p. 22).

Les fichiers de travail sont dans le scratchpad, sous `/tmp/claude-0/-home-user-cplt-run-2026-09-03/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/lecture-2606.08892/` :
- `full.txt`, le texte extrait ;
- `pages/p001.txt` à `p071.txt`, une page par fichier ;
- `verif_citations.py`, le script de vérification des citations ;
- `depots-releves.txt`, les relevés des deux dépôts (les clones ont été supprimés).
