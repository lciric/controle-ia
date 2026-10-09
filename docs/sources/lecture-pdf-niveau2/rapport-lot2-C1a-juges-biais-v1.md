# Lecture de vérification — état de l'art, niveau 2, lot 2 — C1a « juges et biais » — v1

- **Lecteur** : sous-agent neuf ; il n'a rien écrit des documents vérifiés.
- **Date** : 2026-10-06, rédaction achevée à 16 h 53, temps universel coordonné (UTC).
- **Consignes appliquées**, lues en entier avant tout travail (empreintes sha256, algorithme de hachage sécurisé à 256 bits) :
  - `scratchpad/lot2/consigne-commune.md` : `d44580525a20b31b5ff98d6117ffd09a7395e56b4f311c71cd20d3e7acffd9ab` ;
  - `scratchpad/lot2/consignes-C1a-juges-biais.md` : `35671d63492a8dc12eec971363ce20626a18c70bd886dfbef1385f78a27ad3d5`.
- **Document du programme vérifié** : `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md`, ligne 172 ; empreinte `b0b519fe250a839d904e75c66945326d30e47687093852c85eae6355add2cd72`.
- **Rien n'a été modifié sous `/home/user/controle-ia`** (ni fichier, ni git). Tous les produits sont dans le dossier de travail `lecture-lot2-C1a/` (liste au § 10).
- Conventions : « page » = rang dans le fichier, d'après `pdftotext -layout` (version 24.02.0), page par page. Les citations en anglais sont reproduites mot pour mot entre « `…` » ; les chiffres collés aux noms d'auteurs sont des renvois d'affiliation imprimés.

---

## 0. PDF lus et empreintes

PDF = format de document portable. Dossier : `/home/user/controle-ia/docs/sources/pdf/` (lecture seule).

| Fichier | Pages | Empreinte sha256 (attendue = constatée) | Lecture |
|---|---|---|---|
| `2309.17012v3.pdf` | 29 | `8dc98f733b0318aa31acb5b5df36131e835b87e2183579d6c0c51a64f81259b5` | intégrale |
| `2402.10669v5.pdf` | 27 | `47ae7d76edd51093525fd0a868987b626e46f891f065607b568057439de8b41f` | intégrale |
| `2403.04957v1.pdf` | 14 | `c7cca74230ac03c1f10b39c287e84b0b51ccfbfb89f3daa369583f91be4fc6ba` | intégrale |
| `2404.13076v1.pdf` | 21 | `e1466f5ade6144599fda01deafdd737b4623eaae273d71e4a0099d55b33189d3` | intégrale |
| `2410.21819v2.pdf` | 11 | `d1e6b1c9cceb62f095d99c36da314d8e3d4302573e6226b56f101ab120af7f0d` | intégrale |

- **Vérification** : `sha256sum -c` sur les cinq empreintes de la consigne : 5 « OK » sur 5. Garde testée (R5) sur un fichier d'empreintes altéré (premier caractère changé) : « FAILED », code de retour 1.
- **Ce qui n'a pas été lu** : rien du texte ; les 102 pages ont été lues, références et annexes comprises. Les figures n'ont été lues que par leur légende et le texte qu'elles portent, sauf celles-ci, regardées en image : Wataoka et al., figures 1a, 1b (p. 2) et 2 (p. 5) ; Chen et al., figure 4 (p. 8) ; Liu et al., figure 1 (avec l'image de la p. 1). Non regardées en image : figures 1 à 9 de Koo et al. (dont les captures d'interface des p. 26 à 29) ; figures 1 à 3, 5 et 6 de Chen et al. (la p. 26 n'est qu'une image d'interface) ; figures 2 à 5 de Liu et al. ; figures 1 à 8 de Panickssery et al. ; figures 3 à 6 de Wataoka et al.
- **Identification (R11)** : les métadonnées internes de `2410.21819v2.pdf` sont celles du gabarit arXiv (titre « A template for the arxiv style », auteurs « David S. Hippocampus, Elias D. Striatum »). Seule la page 1 imprimée fait foi ; un contrôle d'identité fondé sur les métadonnées échouerait sur ce fichier.

---

## 1. Ce que le programme affirme

Ligne 172, texte exact, dans la section « ## 5. Références nouvelles à lire (trouvées dans les bibliographies), par priorité » :

> 11. **Papier C.** Zeng et al. 2024 (« How Johnny can persuade… ») ; Koo et al., arXiv 2309.17012 ; Chen et al., arXiv 2402.10669 ; Arnav et al., arXiv 2505.23575 ; Lin et al., arXiv 2502.03052 ; Panickssery et al., arXiv 2404.13076 ; Wataoka et al., arXiv 2410.21819 ; Li et al., arXiv 2502.01534 ; Liu et al., arXiv 2403.04957 ; Greshake et al., arXiv 2302.12173 ; Baker et al., arXiv 2503.11926.

Pour les cinq articles du lot, cette ligne n'affirme que trois choses :
- le nom du premier auteur suivi de « et al. » ;
- l'identifiant arXiv ;
- leur rattachement au papier C (juges moniteurs, hypothèses HC).

Elle n'affirme ni année, ni venue, ni chiffre, ni conclusion. La même ligne figure à l'identique dans `livrables/anteriorite-niveau1-v1/etat-de-l-art-verifie-niveau1-v1.md`, ligne 172. La mention « trouvées dans les bibliographies » renvoie aux articles citants (Hwang, Za) : elle n'est pas vérifiable sur les cinq PDF de ce lot.

**Mentions complémentaires, hors liste de la consigne.** Une recherche dans le dépôt a trouvé d'autres passages qui qualifient ces articles ; je les ai vérifiés au passage :
- `docs/sources/lecture-pdf-niveau1/rapport-papierC-v1.md`, lignes 210, 211, 213 et 216 (empreinte `b23aca9dd486171e0545dd54a37513b22d03c8cff89df57b2f9102b981fc171c`) ;
- `docs/sources/lecture-pdf-niveau1/controle-tracabilite-v1.md`, ligne 123 (empreinte `54a9e674cb4f5807888aa5cfa03e8728dfe201a56988da77e00e0eb1b0026ea1`).

L'énoncé revendiqué de HC1 est pris dans `docs/decisions/decision-N-005-N-006-v1.md` (empreinte `cd49afbc924cb1dd56251f22ef692007c24ecb76b124e0662cbe9bc04fa2e1c0`), qui range parmi les pièces revendiquées « le verdict lu par probabilité du jeton » (ligne 52) et parmi les familles « approbations forgées » (ligne 37).

---

## 2. Koo et al. — arXiv 2309.17012v3

### Identité
- **Titre** : « `Benchmarking Cognitive Biases in Large Language Models as Evaluators` » (p. 1).
- **Auteurs**, tous : Ryan Koo, Minhwa Lee, Vipul Raheja, Jonginn Park, Zae Myung Kim, Dongyeop Kang. Affiliations : University of Minnesota (1), Grammarly (2) — « `University of Minnesota, 2 Grammarly` » (p. 1).
- **Version et date** : v3, tampon arXiv du 25 septembre 2024 (p. 1).
- **Venue** : aucune n'est imprimée dans ce PDF, et le programme n'en affirme pas. Non vérifiable ici.

### Ce que fait l'article
- Banc d'essai « CoBBLEr » : 16 grands modèles de langage comparent par paires leurs propres réponses et celles des autres, sur 50 consignes de questions-réponses.
- Six biais : quatre « implicites » (ordre, noms reconnaissables, égocentrique, longueur) et deux « induits » par la consigne (effet de mode par fausse statistique de majorité ; distraction).
- Le verdict est un choix lu dans le texte généré, à la température 1,0.
- Annexe B.1 : la fausse statistique varie (85 %, 0 %, tirage entre 50 et 85 %).

### Affirmations du programme

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1 | « Koo et al., arXiv 2309.17012 » (ligne 172) | confirmé | 1 | « `Ryan Koo1 Minhwa Lee1 Vipul Raheja2 Jonginn Park1 , Zae Myung Kim1 Dongyeop Kang1` » ; « `arXiv:2309.17012v3 [cs.CL] 25 Sep 2024` » |
| 2 | Rattachement au « Papier C » (ligne 172) | confirmé : biais des juges grands modèles de langage | 1 | « `a benchmark to measure six different cognitive biases in LLM evaluation outputs` » |
| 3 | Hors liste. `rapport-papierC-v1.md` l. 210 : « HC1 (majorité chez les juges) ; HC3 (manipulation par la consigne) » | confirmé | 4 | « `stating a fake statistic by choosing one of the comparand outputs as preferred by a majority of people` » ; « `We categorize a bias as “induced” when it requires modifications to the primary prompt or the inclusion of additional information with the original instructions.` » |

### Chiffres utilisables

| Chiffre | Nature | Page | Citation exacte, ou remarque |
|---|---|---|---|
| Environ 40 % des comparaisons marquées par un biais, tous modèles | auteurs | 1 | « `We find that LLMs are biased text quality evaluators, exhibiting strong indications on our bias benchmark (≈ 40% of comparisons made by all models)` » |
| Accord humains–modèles : chevauchement pondéré par le rang (Rank-Biased Overlap) moyen de 0,44 | auteurs | 1 | « `calculate the average Rank-Biased Overlap (RBO) score to be 44%` » |
| 630 000 échantillons, soit 42 000 par modèle | auteurs | 1 | « `In total, 42K samples are analyzed across six biases for each model totaling 630K samples.` » |
| Seuil du hasard pour l'effet de mode et la distraction : 0,25 | auteurs (tableau 2, ligne du hasard) | 7 | « `- 0.24 0.25 0.24 0.25 0.24 0.24 0.5 0.25 0.25` » |
| GPT-4 : effet de mode 0,0 ; biais égocentrique 0,78 (noms anonymes) et 0,06 (noms réels) | auteurs (tableau 2) | 7 | « `GPT4 - 0.17 0.06 0.46 0.33 0.78 0.06 0.56 0.0 0.0` » |
| ChatGPT : effet de mode 0,86 ; biais égocentrique 0,58 et 0,17 | auteurs (tableau 2) | 7 | « `175B 0.38 0.03 0.41 0.25 0.58 0.17 0.63 0.86 0.06` » |
| Effet de mode : « 11/15 » modèles fortement influencés, plus de 70 % en moyenne | auteurs ; **réserve** par calcul | 8 | « `almost all models (11/15) are heavily influenced in which > 70% of evaluations on average followed the bandwagon preference regardless of text quality.` » Le tableau 2 (p. 7, 16 modèles) ne compte que 10 modèles au-dessus de 0,70 ; on ne retrouve 11 modèles (moyenne 0,79) qu'en ajoutant Mistral (0,54). |
| Intensité variée (tableau 6), part des choix pour la réponse désignée, statistique « 85 % » puis « 0 % » : GPT-4 0,0 → 0,0 ; ChatGPT 0,86 → 0,0 ; InstructGPT 0,85 → 0,56 ; Cohere 0,82 → 0,0 ; Alpaca 0,75 → 0,52 ; Vicuna 0,81 → 0,79 ; Baize 0,82 → 0,32 ; WizardLM 0,76 → 0,27 | auteurs (tableau 6 ; colonnes dans cet ordre) | 15 | « `BANDWAGON test showing a fake statistic stating 0% of people prefer the chosen response.` » ; « `BANDWAGON (85%) 0.0 0.86 0.85 0.82 0.75 0.81 0.82 0.76` » ; « `BANDWAGON (0%) 0.0 0.0 0.56 0.0 0.52 0.79 0.32 0.27` » |
| Pourcentage tiré entre 50 et 85 % (tableau 7), même ordre : 0,06 ; 0,70 ; 0,84 ; 0,65 ; 0,68 ; 0,96 ; 0,75 ; 0,76 | auteurs (tableau 7) | 15 | « `BANDWAGON (50-85%) 0.06 0.70 0.84 0.65 0.68 0.96 0.75 0.76` » |

### Réserves internes
- **Plage du tableau 7.** La légende porte « `BANDWAGON test showing a fake statistic stating (randomly) between 50 − 80% of people prefer the chosen response.` » (p. 15). Le texte dit « `We also present the results of the bandwagon test by randomly choosing a percentage between 50% and 85% in Table 7.` » (p. 14), et la ligne du tableau est intitulée « BANDWAGON (50-85%) ». La plage est donc de 50 à 85 %.
- **Lecture de Koo par Panickssery et al.** (2404.13076v1, p. 6) : « `They find GPT-4 to demonstrate lower self-preference than GPT-3.5 out-of-the-box, contrary to our findings` ». Dans la v3 de Koo, c'est vrai avec les noms réels (0,06 contre 0,17), faux avec les noms anonymes (0,78 contre 0,58) (tableau 2, p. 7). Ce raccourci ne doit pas être repris.
- **Verdict.** C'est un choix tiré du texte généré : « `We limit the max new tokens generated to 128 tokens and set the temperature to 1.0.` » (p. 14) ; « `Please respond in the following format strictly: System _ is better` » (p. 21).

### Antériorité (R8 : ce que la source occupe, ou non)
- **HC1 — adjacent, précurseur ; la pièce revendiquée n'est pas occupée par cette source** (p. 8, 14, 15). Citations : « `To observe a correlation between the biased tendency and the percentage, we include additional results in Appendix B.1` » (p. 8) ; « `If bias tendency were indeed correlated with the statistic, we would expect the evaluator model to have 0 preference for bandwagon response.` » (p. 14) ; « `which suggests that indeed the biased tendency is correlated with the bandwagon statistic` » (p. 14) ; « `the model only focuses on the phrase “people believe that {model} is better” instead of the statistic` » (p. 14).
  - Ce que l'article occupe : une pression d'intensité variée (fausse majorité à 85 %, 0 %, 50–85 %) sur des juges génératifs, dans la famille « approbations forgées » (consensus fabriqué). Le choix suit la statistique pour certains modèles (ChatGPT et Cohere tombent à 0,0 sous « 0 % »), pas pour d'autres (Vicuna 0,81 → 0,79).
  - Ce qu'il n'occupe pas : verdict lu par probabilité du jeton (choix binaire à la température 1,0) ; régression sur les intensités ; gain g ; destination ĉ estimée ou testée contre la cible de l'attaquant et la moyenne du corpus ; moniteurs de contrôle ; opposition juge / sonde ; autres familles graduées.
- **Papier B — adjacent** (p. 7). Le biais égocentrique (préférence d'un juge pour ses propres réponses) est mesuré par le comportement ; il n'y a ni états internes, ni copies multiples en interaction, ni nombre d'agents.
- **H2, H1, lemme d'additivité, théorème négatif, transposition jeton → action, HC2b — non touchés.** L'article ne contient ni agent, ni sonde, ni activations, ni test séquentiel, ni taux de faux positifs, ni agrégation par max ou attention. La recherche de ces termes sur les 29 pages ne donne aucune occurrence pertinente.

---

## 3. Chen et al. — arXiv 2402.10669v5

### Identité
- **Titre imprimé** : « `Humans or LLMs as the Judge? A Study on Judgement Bias` » (p. 1), au singulier. Trois documents écrivent « … Judgement Biases » : la consigne C1a, `docs/sources/pdf/provenance-niveau2-lot2-v1.md` (ligne 10) et `rapport-papierC-v1.md` (ligne 211).
- **Auteurs**, tous : Guiming Hardy Chen et Shunian Chen (contributions égales), Ziche Liu, Feng Jiang, Benyou Wang (auteur correspondant). Affiliations : « `The Chinese University of Hong Kong, Shenzhen` » et « `Shenzhen Research Institute of Big Data` » (p. 1).
- **Version et date** : v5, tampon arXiv du 26 septembre 2024 (p. 1).
- **Venue** : aucune n'est imprimée dans ce PDF, et le programme n'en affirme pas.

### Ce que fait l'article
- Cadre « sans référence » : un groupe témoin (deux réponses A1 et A2) et un groupe expérimental (A1 contre A2 perturbée).
- Quatre perturbations : erreur factuelle, contenu genré, fausses références (biais d'autorité), contenu enrichi (biais de « beauté »).
- 142 questions, 60 juges humains, et des juges grands modèles de langage.
- Votes discrets (« Answer 1 », « Answer 2 », « Tie »), six votes par paire, moyenne seuillée à 0,5.
- Mesure : taux de succès d'attaque, c'est-à-dire la part des échantillons dont la préférence bascule vers la réponse perturbée.
- Section 6 : attaque par fausses références et contenu enrichi.

### Affirmations du programme

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1 | « Chen et al., arXiv 2402.10669 » (ligne 172) | confirmé | 1 | « `Guiming Hardy Chen† , Shunian Chen† , Ziche Liu, Feng Jiang, Benyou Wang*` » ; « `arXiv:2402.10669v5 [cs.CL] 26 Sep 2024` » ; « `First two authors contributed to this work equally.` » |
| 2 | Rattachement au « Papier C » (ligne 172) | confirmé | 2 | « `One can easily exploit Authority Bias and Beauty Bias to conduct a prompt-based attack on LLM judges, achieving an ASR of up to 50% on GPT-4 (Section 6).` » |
| 3 | Hors liste. `rapport-papierC-v1.md` l. 211, titre « Humans or LLMs as the judge? A study on judgement biases (Chen et al.) » | **corrigé**. Formulation à mettre : « Humans or LLMs as the Judge? A Study on Judgement Bias » (titre imprimé de la v5) | 1 | « `Humans or LLMs as the Judge? A Study on Judgement Bias` » |
| 4 | Hors liste. Même ligne, rôle « HC1 : autorité, approbations forgées » | **corrigé**. Formulation à mettre : « HC1 : autorité invoquée par de fausses références ajoutées à la réponse jugée ». Les approbations forgées (consensus fabriqué) ne sont pas testées ici ; elles le sont chez Koo et al. (fausse statistique de majorité) | 3 | « `We introduce fake references and rich content for testing Authority Bias and Beauty Bias, respectively.` » |

Précision, non correction : le passage « p. 4 : « fake citations may influence LLM judgment » » de la même ligne est, comme l'indique la colonne « Ce qu'en dit le papier citant », une phrase du papier citant (Hwang, p. 4). Elle n'est pas de Chen : l'expression « fake citations » n'apparaît dans aucune des 27 pages de la v5, qui dit « fake references ».

### Chiffres utilisables

| Chiffre | Nature | Page | Citation exacte, ou remarque |
|---|---|---|---|
| Taux de succès d'attaque sous fausses références (tableau 1, 4ᵉ colonne) : GPT-4o 0,32 ; Claude-3 0,70 ; humains 0,37 ; GPT-4 0,66 ; GPT-4-Turbo 0,49 ; Ernie 0,42 ; LLaMA2-70B 0,42 ; hasard 0,37 ; Claude-2 0,89 | auteurs (tableau 1) | 6 | « `GPT-4o 0.06 (1) 0.16 (3) 0.32 (1) 0.07 (3) 2.00` » ; « `Claude-3 0.08 (2) 0.13 (2) 0.70 (8) 0.04 (1) 3.25` » ; « `Human 0.21 (5) 0.06 (1) 0.37 (2) 0.47 (8) 4.00` » ; « `GPT-4 0.09 (3) 0.19 (4) 0.66 (7) 0.32 (5) 4.75` » ; « `GPT-4-Turbo 0.11 (4) 0.27 (7) 0.49 (6) 0.05 (2) 4.75` » ; « `Ernie 0.26 (7) 0.34 (8) 0.42 (4) 0.09 (4) 5.75` » ; « `LLaMA2-70B 0.60 (8) 0.20 (5) 0.42 (4) 0.46 (7) 6.00` » ; « `Random 0.62 (9) 0.56 (9) 0.37 (2) 0.39 (6) 6.50` » ; « `Claude-2 0.23 (6) 0.25 (6) 0.89 (9) 0.68 (9) 7.50` » |
| GPT-4o ne fait que 5 points de mieux que le hasard sous fausses références | auteurs | 6 | « `Even the best performed GPT-4o has 32% in ASR (only 5% better than random)` » |
| « Jusqu'à 50 % sur GPT-4 » | auteurs (p. 2) ; origine **figure** 4b (p. 8) : 0,50 pour GPT-4 sous perturbation composée (fausses références et contenu enrichi) appliquée à des réponses à contenu genré ; le hasard y est à 0,65 | 2, 8 | citation du § 3, ligne 2 du tableau des affirmations |
| Fausses références selon l'écart de qualité (tableau 3) : GPT-4 0,04 ; 0,07 ; 0,09 ; 0,40 face à LLaMA2-7B, 13B, 70B et GPT-3.5-Turbo | auteurs | 8 | « `GPT-4 0.04 0.07 0.09 0.40 2.25` » ; « `meaning that the LLM judges are easier to be induced by references as the quality gap between answer pairs shrinks.` » |
| 142 questions ; 60 juges humains | auteurs | 4 | « `leaving us with 142 questions for the subsequent steps.` » ; « `We employ 60 college students as our human judges.` » |
| Six votes par paire, seuil 0,5 | auteurs | 5 | « `Then we calculate the average score of each sample over its 6 votes. We use 0.5 as a threshold to assign the aggregated vote for each sample.` » |

### Réserves internes
- **0,08 ou 0,09 ?** P. 7 : « `the ASR of GPT-4 on evaluating answers generated by itself on this subset is 0.07, and the corresponding result in Table 1 is 0.08.` ». Or le tableau 1 donne 0,09 pour GPT-4 en erreur factuelle (p. 6, ligne GPT-4 citée plus haut).
- **Nombre de juges exclus.** Le texte en écarte cinq (GPT-3.5-Turbo, Mixtral, Spark, Qwen, Gemini-Pro) : « `we only include models with less significant positional bias in the following sections.` » (p. 5) ; « `Hence, we exclude them in our subsequent analysis.` » (p. 6). La note de la p. 22 dit pourtant : « `Based on this observation, we have excluded these three models from all other experiments.` »
- **Portée du taux.** Plusieurs juges font moins bien que le hasard sous fausses références (tableau 1). Ce taux de succès d'attaque est une fréquence de bascule ; ce n'est pas un coefficient de déférence.

### Antériorité
- **HC1 — adjacent ; la pièce revendiquée n'est pas occupée par cette source** (p. 3, 5, 8). Citations : « `We introduce fake references and rich content for testing Authority Bias and Beauty Bias, respectively.` » (p. 3) ; « `a judge is instructed to determine whether “Answer 1" is better, “Answer 2" is better, or a “Tie"` » (p. 5) ; mécanisme proposé : « `it merely learns a generic signal that the presence of references signifies preference, regardless of true authenticity.` » (p. 22).
  - Ce que l'article occupe : la famille autorité (autorité invoquée par références) sur des juges génératifs, avec un effet binaire (bascule de vote), une intensité par perturbation et une perturbation composée. L'écart de qualité entre les deux réponses module la bascule ; ce n'est pas une intensité de pression.
  - Ce qu'il n'occupe pas : probabilité du jeton, régression sur les intensités, destination, moniteurs de contrôle, opposition juge / sonde.
- **H2, H1, lemme d'additivité, théorème négatif, transposition jeton → action, HC2b, papier B — non touchés.** Ni agent, ni sonde, ni activations, ni copies d'un même modèle.

---

## 4. Liu et al. — arXiv 2403.04957v1

### Identité
- **Titre** : « `Automatic and Universal Prompt Injection Attacks against Large Language Models` » (p. 1).
- **Auteurs**, tous : Xiaogeng Liu, Zhiyuan Yu, Yizhe Zhang, Ning Zhang, Chaowei Xiao. Les renvois d'affiliation 1 à 3 n'ont pas de légende dans ce PDF (vérifié sur l'image de la page 1).
- **Version et date** : v1, tampon arXiv du 7 mars 2024.
- **Venue** : aucune n'est imprimée dans ce PDF, et le programme n'en affirme pas.

### Ce que fait l'article
- Injection indirecte d'instructions dans des données externes lues par une application qui intègre un grand modèle de langage.
- Trois objectifs (statique, semi-dynamique, dynamique), chacun avec une réponse visée explicite par l'attaquant.
- Optimisation par gradient sur jetons (« Greedy Coordinate Gradient » avec moment), entraînée sur cinq échantillons.
- Un seul modèle victime, Llama2-7b-chat ; 1 400 échantillons de test (7 tâches × 200).
- Succès mesuré par mot-clé et, pour deux objectifs, par un évaluateur GPT-4.
- Cinq défenses, dont la paraphrase ; pour l'objectif statique, l'attaque les contourne le plus souvent, et mieux encore en version adaptative (espérance sur les transformations).

### Affirmations du programme

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1 | « Liu et al., arXiv 2403.04957 » (ligne 172) | confirmé | 1 | « `Xiaogeng Liu 1 Zhiyuan Yu 2 Yizhe Zhang 3 Ning Zhang 2 Chaowei Xiao 1` » ; « `arXiv:2403.04957v1 [cs.AI] 7 Mar 2024` » |
| 2 | Rattachement au « Papier C » (ligne 172) | confirmé, avec une précision : l'article ne porte ni sur des juges ni sur des moniteurs ; il fonde la famille « ordres en bande » | 1, 5 | « `In this paper, we focus on these indirect prompt injection attacks (Greshake et al., 2023; Yi et al., 2023) as they are more challenging and dangerous.` » ; « `We utilized Llama2-7b-chat (Touvron et al., 2023) as the victim model.` » |
| 3 | Hors liste. `rapport-papierC-v1.md` l. 213 : « HC3 : ordres en bande », « Injection d'ordres » | confirmé | 2 | « `aiming to mislead the LLM to generate a target response RT that is different from RB` » |
| 4 | Hors liste. `controle-tracabilite-v1.md` l. 123 : « Liu (2403.04957) » | confirmé (identité) | 1 | « `Automatic and Universal Prompt Injection Attacks against Large Language Models` » |

### Chiffres utilisables (un seul modèle victime : Llama2-7b-chat)

| Chiffre | Nature | Page | Citation exacte, ou remarque |
|---|---|---|---|
| Moyennes sur 7 tâches (tableau 1, dernière colonne) : objectif statique 0,81 ; semi-dynamique 0,37 (mot-clé) et 0,35 (évaluateur) ; dynamique 0,39 et 0,34 | auteurs | 6 | « `0.84 - 0.92 - 0.96 - 0.72 - 0.94 - 0.92 - 0.36 - 0.81 -` » ; « `0.14 0.12 0.52 0.52 0.16 0.14 0.10 0.10 0.50 0.45 0.50 0.43 0.68 0.66 0.37 0.35` » ; « `0.70 0.63 0.30 0.26 0.14 0.14 0.64 0.56 0.50 0.43 0.10 0.09 0.32 0.27 0.39 0.34` » |
| « Moyenne de 50 % » | auteurs ; calcul : (0,81 + 0,35 + 0,34) / 3 = 0,50 en retenant l'évaluateur quand il existe ; 0,52 avec les seuls mots-clés | 6 | « `we achieve above 80% ASR on the static objective and an average ASR of 50%` » |
| Lignes de base (naïve, combinée, répétée) : 0,00 partout | auteurs | 6 | « `have lost their effectiveness entirely in generating responses with malicious goals` » |
| Cinq échantillons d'entraînement (0,3 % des données de test) ; 1 400 échantillons de test | auteurs | 1, 6 | « `With only five training samples (0.3% relative to the test data), our attack can achieve superior performance compared with baselines.` » ; « `Specifically, we test the attack success rate (ASR) across 200 samples from each dataset (1400 samples in total).` » |
| Défenses : baisse de 32 % sans adaptation ; 85 % de la performance d'origine retrouvée avec adaptation | auteurs | 7 | « `our method experienced a 32% performance drop when confronted with defense mechanisms without an adaptive strategy` » ; « `it recovered to 85% of its original performance upon utilizing an adaptive scheme.` » |

### Antériorité
- **HC1 — adjacent** (p. 2, 5). Ce que l'article occupe : la famille « ordres en bande », avec une cible de l'attaquant explicite (réponse visée). Ce qu'il n'occupe pas : un juge ou un moniteur (la victime exécute une tâche), une intensité graduée, un verdict continu, une destination.
- **HC5 — pour information** (cet énoncé n'est pas dans la liste à examiner). Défense testée : « `Paraphrasing (Jain et al., 2023): using the back-end language model to rephrase sentences` » (p. 7) ; résultat sous attaque adaptative : « `it recovered to 85% of its original performance upon utilizing an adaptive scheme.` » (p. 7). La paraphrase comme défense contre les ordres en bande est donc déjà testée, et contournée par une attaque adaptative, sur un modèle et pour l'objectif statique. Ce n'est pas la pièce revendiquée de HC5 (quorum par type d'accès, matrice de transfert).
- **H2, H1, lemme d'additivité, théorème négatif, transposition jeton → action, HC2b, papier B — non touchés.** L'optimisation porte sur des jetons d'entrée, non sur des sondes ; il n'y a ni agent, ni agrégation par action.

---

## 5. Panickssery et al. — arXiv 2404.13076v1

### Identité
- **Titre** : « `LLM Evaluators Recognize and Favor Their Own Generations` » (p. 1).
- **Auteurs**, tous : Arjun Panickssery, Samuel R. Bowman, Shi Feng (auteur correspondant). Affiliations : « `MATS 2 New York University 3 Anthropic, PBC.` » (p. 1) — le sigle MATS est imprimé sans développement.
- **Version et date** : v1, tampon arXiv du 15 avril 2024.
- **Venue** : aucune n'est imprimée dans ce PDF, et le programme n'en affirme pas.

### Ce que fait l'article
- Tâche : résumé d'articles de presse, sur deux corpus désignés par leur nom propre, XSUM (résumé « extrême » en une phrase) et CNN/DailyMail (résumé en trois ou quatre points).
- Trois évaluateurs : GPT-4, GPT-3.5, Llama-2-7b-chat.
- Mesures : auto-reconnaissance et auto-préférence, par paires et isolément, avec un score continu tiré des probabilités des jetons de réponse.
- Affinage supervisé pour faire varier l'auto-reconnaissance ; corrélation linéaire entre les deux propriétés (figure, sans coefficient imprimé).
- Tâches témoins (longueur, voyelles, lisibilité) ; étiquettes de source vraies ou inversées.

### Affirmations du programme

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1 | « Panickssery et al., arXiv 2404.13076 » (ligne 172) | confirmé | 1 | « `Arjun Panickssery 1 Samuel R. Bowman 2 3 Shi Feng 2` » ; « `arXiv:2404.13076v1 [cs.CL] 15 Apr 2024` » |
| 2 | Rattachement au « Papier C » (ligne 172) | confirmé | 1 | « `LLM Evaluators Recognize and Favor Their Own Generations` » |
| 3 | Hors liste. `rapport-papierC-v1.md` l. 216 : « HC5 : biais de famille, fondement de l'hétérogénéité » | **corrigé**. Formulation à mettre : « HC5 : auto-préférence d'un évaluateur pour ses propres textes, liée à sa capacité à les reconnaître ; aucun biais de famille n'est mesuré ». Le mot « family » n'apparaît dans aucune des 21 pages | 2 | « `GPT-4 is 73.5% accurate distinguishing itself from two other LLMs and humans.` » |

### Chiffres utilisables

| Chiffre | Nature | Page | Citation exacte, ou remarque |
|---|---|---|---|
| GPT-4 : 73,5 % d'exactitude d'auto-reconnaissance, sans affinage | auteurs | 2 | citation de la ligne 3 ci-dessus |
| Plus de 90 % après affinage sur 500 exemples (GPT-3.5, Llama 2) | auteurs | 2 | « `GPT-3.5 and Llama 2 both achieve over 90% accuracy at self-recognition after fine-tuning on 500 examples.` » |
| Inversion de préférence quand l'ordre des options est inversé : GPT-4 25 %, GPT-3.5 58 %, Llama 89 % | auteurs | 4 | « `reverse their pairwise preferences when the ordering of options is reversed at rates of 25%, 58%, and 89% respectively` » |
| Corrélation de Kendall de 0,41 entre reconnaître et préférer son résumé (GPT-3.5, XSUM, avant affinage) | auteurs | 5 | « `the evaluator prior to fine-tuning has a correlation of 0.41 (Kendall’s τ ) between correctly recognizing its summary from a pair and preferring its summary from that same pair.` » |
| Étiquettes de source vraies puis inversées (tableau 6) : auto-préférence de GPT-4 0,73 → 0,32 (XSUM) et 0,94 → 0,89 (CNN/DailyMail) | auteurs | 13 | « `Table 6. Self-preference scores with correct and incorrect labels.` » ; « `GPT-4 0.73 0.32 0.94 0.89` » |
| Corrélation linéaire entre auto-reconnaissance et auto-préférence | figure (figures 1 et 7), aucun coefficient imprimé | 1, 6 | — |

### Réserves internes
- **Légende du tableau 14.** Elle reprend mot pour mot celle du tableau 13 : « `Table 13. Self-recognition confidence scores in the individual setting, evaluated on the CNN dataset.` » (p. 20) ; « `Table 14. Self-recognition confidence scores in the individual setting, evaluated on the CNN dataset.` » (p. 21). Par symétrie avec les tableaux 11 et 12, le tableau 14 donne vraisemblablement l'auto-préférence sur CNN/DailyMail. Ne pas l'utiliser sans lever ce doute.
- **Lecture de Koo et al.** (p. 6) : voir le § 2, réserves.

### Antériorité
- **HC1 — partiel : la lecture du verdict d'un juge par la probabilité des jetons est occupée** (p. 2). Citations : « `We compute a prediction confidence by normalizing the output probabilities of tokens associated with the two options.` » ; « `compute the final rating as the average of the five possible scores weighted by the output probability of each number token.` »
  - Le verdict continu par probabilité du jeton est une technique publiée pour les juges : choix par paires normalisé, et échelle de Likert pondérée par la probabilité de chaque jeton numérique.
  - Il ne peut pas être revendiqué seul. Seule la combinaison reste à examiner : pression graduée, destination libre testée contre la cible et contre la moyenne du corpus, familles, moniteurs de contrôle.
- **HC1 — adjacent, étiquetage de la source** (p. 6, 13). Citations : « `The GPT-4 and GPT-3.5 evaluator models show a reversal in self-preference when the labels are reversed in the XSUM dataset` » (p. 6) ; « `the “Summary1” and “Summary2” portions of the prompt were followed with parenthetical “ ({source}’s summary)” to indicate the summary’s source.` » (p. 13). C'est une manipulation déclarative (étiquette d'auteur) à un seul niveau, sans gradation ni destination.
- **Papier B — adjacent** (p. 7). Citation : « `In the worst case scenario where the adversary use the same LLM as the defender, the adversary can gain unbounded access to the defender.` » C'est un énoncé qualitatif, sans mesure, sur un attaquant et un défenseur issus du même modèle ; il n'y a ni états internes, ni nombre d'agents. Contre-mesure seulement évoquée : « `countermeasures such as authorship obfuscation should be incorporated into standard prompting practice.` » (p. 7).
- **HC2b — non touché.** L'auto-reconnaissance est mesurée en posant la question au modèle (comportement), pas par une sonde.
- **H2, H1, lemme d'additivité, théorème négatif, transposition jeton → action — non touchés.**

---

## 6. Wataoka et al. — arXiv 2410.21819v2

### Identité
- **Titre** : « `Self-Preference Bias in LLM-as-a-Judge` » (titre courant, p. 2 ; le titre de la p. 1 est en petites capitales, mal restituées par l'extraction).
- **Auteurs**, tous : « `Koki Wataoka` », « `Tsubasa Takahashi` », « `Ryokan Ri` », tous trois de « `SB Intuitions` » (p. 1).
- **Version et date** : v2, tampon « `arXiv:2410.21819v2 [cs.CL] 21 Jun 2025` », date imprimée « `June 24, 2025` » (p. 1).
- **Venue** : aucune n'est imprimée dans ce PDF, et le programme n'en affirme pas.

### Ce que fait l'article
- Métrique d'auto-préférence fondée sur l'égalité des chances : différence de rappel selon que la réponse jugée est la sienne ou non.
- Huit juges sur le jeu Chatbot Arena (33 000 dialogues avec préférences humaines).
- Score lu dans p(A|contexte) et p(B|contexte) après le jeton « [[ », normalisés ; ordre des réponses inversé et moyenné.
- GPT-4 : 0,520.
- Explication proposée : les juges préfèrent les textes de faible perplexité, qu'ils soient ou non les leurs.
- Piste de discussion : évaluation par ensemble de modèles.

### Affirmations du programme

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1 | « Wataoka et al., arXiv 2410.21819 » (ligne 172) | confirmé | 1 | « `Koki Wataoka` » ; « `Tsubasa Takahashi` » ; « `Ryokan Ri` » ; « `arXiv:2410.21819v2 [cs.CL] 21 Jun 2025` » |
| 2 | Rattachement au « Papier C » (ligne 172) | confirmé | 1 | « `In this paper, we introduce a novel quantitative metric to measure the self-preference bias.` » |
| 3 | Hors liste. `rapport-papierC-v1.md` l. 216 : « HC5 : biais de famille, fondement de l'hétérogénéité » | **corrigé**. Formulation à mettre : « HC5 : auto-préférence d'un juge, expliquée par la faible perplexité des textes, qu'ils soient ou non les siens ; aucun biais de famille n'est mesuré ; l'évaluation par ensemble de modèles n'est qu'une piste de discussion, sans expérience » | 1, 6 | « `Our findings reveal that LLMs assign significantly higher evaluations to outputs with lower perplexity than human evaluators, regardless of whether the outputs were self-generated.` » ; « `To reduce self-preference bias, one possible approach is ensemble evaluation using multiple models.` » |
| 4 | Hors liste. `controle-tracabilite-v1.md` l. 123 : « Wataoka (2410.21819) » | confirmé (identité) | 1 | voir la ligne 1 |

### Chiffres utilisables

| Chiffre | Nature | Page | Citation exacte, ou remarque |
|---|---|---|---|
| GPT-4 : 0,520 (égalité des chances) | auteurs ; calcul concordant : 1852/1960 − 118/278 = 0,9449 − 0,4245 = 0,5204, effectifs lus sur la figure 2 (p. 5) | 4, 5 | « `The difference between these values is 0.520, which corresponds to the value reported in Figure 1b.` » |
| Autres juges (figure 1b) : GPT-3.5-turbo 0,03 ; Vicuna-13b 0,25 ; Vicuna-7b 0,05 ; Koala-13b 0,15 ; oasst-pythia-12b −0,02 ; dolly-v2-12b −0,05 ; stablelm-tuned-alpha-7b −0,02 | figure ; **réserve** par calcul | 2, 5 | Recalcul à partir des matrices de la figure 2 : Vicuna-13b 0,209 (et non 0,25) ; dolly-v2-12b −0,061 (et non −0,05). Les six autres concordent à l'arrondi. |
| Parité démographique (tableau 2) : GPT-4 0,749 ; GPT-3.5-turbo 0,191 ; Vicuna-13b 0,382 ; Vicuna-7b 0,052 ; Koala-13b 0,175 ; oasst-pythia-12b 0,006 ; dolly-v2-12b −0,069 ; stablelm-tuned-alpha-7b −0,032 | auteurs | 9 | « `GPT-4 0.749` » ; « `GPT-3.5-turbo 0.191` » ; « `Vicuna-13b 0.382` » ; « `Vicuna-7b 0.052` » ; « `Koala-13b 0.175` » ; « `oasst-pythia-12b 0.006` » ; « `dolly-v2-12b -0.069` » ; « `stablelm-tuned-alpha-7b -0.032` » |
| 33 000 dialogues | auteurs | 4 | « `Empirical evaluation uses Chatbot Arena dataset [Zheng et al., 2024], which contains 33,000 dialogues` » |

### Réserves internes
- **Modèles exceptés.** Le texte dit « `All models except stablelm-tuned-alpha-7b demonstrated a clear tendency to assign higher evaluations to responses with lower perplexity.` » (p. 6). La légende de la figure 3, sur la même page, dit « `All models except dolly-v2-12b and stablelm-tuned-alpha-7b demonstrated a clear tendency to assign higher evaluations to responses with lower perplexity.` »
- **Figure 1b contre figure 2** (Vicuna-13b, dolly-v2-12b) : voir le tableau des chiffres.
- **Perplexité non mesurée pour les deux juges les plus forts** : « `In this experiment, we excluded GPT-4 and GPT-3.5-Turbo, as perplexity values could not be obtained for these models.` » (p. 5).

### Antériorité
- **HC1 — partiel : même occupation que Panickssery et al., avec une filiation déclarée** (p. 4). Citations :
  - « `using the probabilities that the LLM evaluator outputs for “A" and “B", denoted as p(A|context) and p(B|context), we calculate the score for response A using the following equation.` » ;
  - « `following the approach of Schick et al. [2021]` » ;
  - « `we used the output probability distribution following the token corresponding to “[[" in the generated text to compute the score using Equation 3.` »

  Il n'y a ni pression, ni destination.
- **Papier B — adjacent** (p. 1). La familiarité est mesurée par la perplexité des sorties (citation de la ligne 3 ci-dessus). Il n'y a ni états internes, ni copies multiples en interaction, ni nombre d'agents.
- **H2, H1, lemme d'additivité, théorème négatif, transposition jeton → action, HC2b — non touchés.**

---

## 7. Antériorité — vue d'ensemble

| Énoncé revendiqué | Koo | Chen | Liu | Panickssery | Wataoka |
|---|---|---|---|---|---|
| H2 (accumulation additive toujours valide, seuil à 1 % de faux positifs) | non touché | non touché | non touché | non touché | non touché |
| H1 (gain des activations sur la boîte noire) | non touché | non touché | non touché | non touché | non touché |
| Lemme d'additivité | non touché | non touché | non touché | non touché | non touché |
| Théorème négatif | non touché | non touché | non touché | non touché | non touché |
| Transposition jeton → action | non touché | non touché | non touché | non touché | non touché |
| HC1 (loi de déférence) | adjacent : intensité variée d'une fausse majorité, choix binaire | adjacent : autorité, une intensité, bascule binaire | adjacent : ordres en bande, cible explicite, pas de juge | **partiel** : verdict par probabilité du jeton | **partiel** : idem, d'après Schick et al. 2021 |
| HC2b (auto-incrimination des sondes) | non touché | non touché | non touché | non touché | non touché |
| Papier B (co-élévation entre copies) | adjacent : biais égocentrique | non touché | non touché | adjacent : attaquant = défenseur, qualitatif | adjacent : familiarité par perplexité |

**Lecture (R8).** Pour les pièces revendiquées, ces cinq sources n'occupent que deux choses :
1. la lecture du verdict d'un juge par la probabilité des jetons (Panickssery et al. 2024 ; Wataoka et al., qui l'attribuent à Schick et al. 2021) ;
2. une variation rudimentaire de l'intensité d'une pression sur des juges (Koo et al., annexe B.1), dans la famille des approbations forgées, avec un choix binaire.

Elles n'occupent pas :
- la destination libre ĉ, ni son test contre la cible de l'attaquant et contre la moyenne du corpus ;
- la régression sur plusieurs intensités par famille ;
- les moniteurs de contrôle ;
- l'opposition juge / sonde ;
- H1, H2, le lemme, le théorème négatif, la transposition, HC2b et le papier B.

Ce constat ne vaut que pour ces cinq sources : les autres sources qui touchent HC1 (2508.07805, 2606.07897, PARROT — « Persuasion and Agreement Robustness Rating of Output Truth », arXiv 2511.17220 —, Panin…) sont hors de ce lot.

---

## 8. Contrôle des citations (R5)

- **Fichiers.** Script `outils/controle_citations.py` (empreinte `06ae0277ad729e620945436d712a10d803bfc26ccfa8af440a9d4a27b57b0e44`) ; entrée `citations.tsv` (valeurs séparées par tabulations) ; sortie `controle-final.txt`. Empreintes de ces deux derniers fichiers : `empreintes.sha256` (§ 10).
- **Règle.** Chaque citation doit figurer dans le texte extrait de la page indiquée. Tolérances : les suites de blancs comptent pour une espace ; une césure de fin de ligne est lue avec et sans trait d'union. Trois extractions de la même page sont consultées :
  - `pdftotext -layout`, qui fixe la numérotation ;
  - l'ordre de lecture (`pdftotext` sans option) ;
  - la colonne gauche puis la colonne droite (recadrage `-x -y -W -H`).
- **Tests préalables (R5)**, dossier `tests/` :
  - cinq cas justes, tous « OK » (code de retour 0) : une ligne ; deux césures réelles (« demon-/strated », « self-/preference ») ; blancs modifiés ; un passage sur deux lignes d'une colonne ;
  - six cas altérés, avec 5 « ECHEC » attendus : chiffre changé (0.520 → 0.502), bonne citation à la mauvaise page, mot ajouté, espace inséré dans un mot, mot changé ;
  - sixième cas altéré, une chaîne qui mêle deux colonnes : il donne « OK* ». Cette chaîne existe telle quelle dans les extractions entremêlées. C'est une limite de la méthode ; elle est rendue visible (« OK* », à revoir à la main) et non silencieuse ;
  - page absente : arrêt, code de retour 2.
- **Corrections du script pendant les tests.**
  - La première version ignorait tous les blancs : un espace inséré dans un mot passait.
  - La deuxième, sans extraction par colonnes, ne pouvait pas vérifier les passages des pages à deux colonnes.
  - La version finale marque « OK* » toute concordance absente de l'extraction par colonnes.
- **Bilan : 116 citations contrôlées, 0 échec.**
  - 57 concordent dans l'extraction par colonnes.
  - 59 sont marquées « OK* » ; je les ai revues une à une. Ce sont les titres, auteurs et affiliations en pleine largeur (p. 1), des lignes et légendes de tableaux, et des pages à une seule colonne (Wataoka et al. ; annexe de Panickssery et al.). Aucune ne résulte d'un mélange de colonnes.
  - Un échec intermédiaire a été corrigé : la citation de Chen et al. « We introduce fake references… » était attribuée à la p. 4 ; elle est p. 3.
- **Passages en français du programme.** Ils ne passent pas par ce script. Je les ai retrouvés mot pour mot (`grep -F`) aux lignes indiquées des fichiers sources : ligne 172, et lignes 210, 211, 213, 216, 123, 52, 37 et 10 des autres fichiers cités.
- **Calculs** (Wataoka et al. 0,5204 et figure 1b ; Liu et al. 0,50 et 0,523 ; Koo et al. 10 sur 16 et 0,79) : refaits par un court calcul Python, sur des valeurs lues dans les tableaux cités et sur la figure 2 de Wataoka et al. (regardée en image, zoom à 220 points par pouce).

---

## 9. Synthèse

1. Empreintes : 5 sur 5 conformes. Les cinq articles sont lus en entier (102 pages). 116 citations contrôlées par script, 0 échec.
2. Ligne 172 : les cinq attributions (« premier auteur et al. », identifiant arXiv) sont **confirmées**. Aucune année ni venue n'y est affirmée, et aucune venue n'est imprimée dans ces PDF.
3. **Corrigé** (hors ligne 172) : le titre de 2402.10669 v5 est « … A Study on Judgement Bias », au singulier (rapport papier C l. 211, provenance l. 10, consigne).
4. **Corrigé** (rapport papier C l. 211 et 216) : le rôle de Chen est l'autorité par fausses références, non les « approbations forgées », que l'on trouve chez Koo (effet de mode). Le rôle de Panickssery et de Wataoka est l'auto-préférence : aucun « biais de famille » n'y est mesuré.
5. **HC1 partiellement touchée** : le verdict d'un juge lu par la probabilité des jetons est publié (Panickssery p. 2 ; Wataoka p. 4, d'après Schick et al. 2021). Il faut le citer, et ne pas le revendiquer seul.
6. **HC1, précédent adjacent** : Koo (annexe B.1, p. 14–15) fait déjà varier l'intensité d'une fausse majorité (85 %, 0 %, 50–85 %) sur des juges. Choix binaire ; ni régression, ni destination, ni moniteur de contrôle.
7. **Papier B** seulement adjacent : Panickssery p. 7 (énoncé qualitatif) ; Wataoka (familiarité par perplexité) ; Koo (biais égocentrique). H2, H1, lemme d'additivité, théorème négatif, transposition jeton → action et HC2b ne sont pas touchés par ces cinq sources.
8. **Réserves sur les chiffres** : Wataoka, figure 1b contredite par la figure 2 (Vicuna-13b, dolly) ; Koo, « 11/15 » non retrouvé (10 modèles sur 16) ; Chen, « 0.08 » contre 0,09 ; légendes fautives (Koo tableau 7, Panickssery tableau 14).

---

## 10. Fichiers produits (dossier `lecture-lot2-C1a/`)

- `rapport.md` : ce rapport.
- `outils/controle_citations.py` : script de contrôle.
- `citations-source.txt` et `citations.tsv` : citations contrôlées (identifiant, page, citation).
- `controle-final.txt` : sortie du dernier contrôle ; `controle-v1.txt` à `controle-v3.txt` : sorties intermédiaires, avant les corrections décrites au § 8.
- `tests/` : cas justes, cas altérés et page absente, avec leurs sorties.
- `texte/`, `texte-brut/`, `texte-colonnes/` : extractions page par page (`-layout`, ordre de lecture, par colonnes).
- `images/` : pages rendues pour la lecture des figures (Wataoka p. 2 et 5 ; Chen p. 8 ; Liu p. 1).
- `attendues.sha256` et `altere.sha256` : empreintes des PDF, et cas altéré du test de garde.
- `empreintes.sha256` : empreintes de tous les fichiers ci-dessus, sauf ce rapport.
- `rapport.md.sha256` : empreinte compagnon de ce rapport (R6), aussi donnée dans la réponse finale.
