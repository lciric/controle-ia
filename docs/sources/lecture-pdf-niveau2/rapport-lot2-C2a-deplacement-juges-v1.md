# Lecture de vérification — état de l'art, niveau 2, lot 2 — C2a « déplacement des juges »

- **Lecteur** : sous-agent neuf ; n'a écrit aucun des documents vérifiés.
- **Date** : 2026-10-06 16:51 (temps universel coordonné).
- **Consignes appliquées** : `scratchpad/lot2/consigne-commune.md` et `scratchpad/lot2/consignes-C2a-deplacement-juges.md`.
- **Aucune modification sous `/home/user/controle-ia`** (ni fichier, ni git). Lus en lecture seule, pour le contexte : les quatre PDF ; `docs/etat-de-l-art-controle-ia-v1.md`, lignes 100 à 150 (pour savoir à quoi renvoie « le coefficient » : le gain g continu par moniteur et par famille, section 4.2) ; `docs/programme-controle-ia-v2.md`, section du papier C ; `docs/decisions/decision-N-005-N-006-v1.md` (énoncé retenu de HC1 : destination libre ĉ, régression sur plusieurs intensités, verdict lu par probabilité du jeton).

## PDF lus et empreintes

Dossier : `/home/user/controle-ia/docs/sources/pdf/`. Empreintes sha256 calculées avant toute lecture, toutes égales aux empreintes des consignes.

| Fichier | Pages | Empreinte sha256 (attendue = calculée) | Lecture |
|---|---|---|---|
| `2509.26072v2.pdf` | 9 | `c97ff1b49b6623b63e05358a1dc68c76b1818a42120414924b16e157927969ba` | en entier |
| `2601.13433v4.pdf` | 10 | `e4991aa9e346cbb536fc6c03817138b56fea77ed8379dc62f3cad0eaedef877f` | en entier |
| `2605.23970v1.pdf` | 14 | `42867a39af4afd2a8c29d2bc8e023cb9df69924f7cac6de7f12b2e2487a39a1a` | en entier |
| `2604.21564v2.pdf` | 26 | `c2a2f1e28e258628c775de38cf424a571f42747764c0c232c160b386247cf3b3` | en entier |

## Méthode

- **Pages** : rang dans le fichier, texte extrait par `pdftotext -layout`, page par page. Pour les deux articles en deux colonnes (2601.13433 et 2605.23970), la page entière entrelace les colonnes ligne à ligne ; j'ai donc aussi extrait, avec le même outil, la demi-page gauche et la demi-page droite (découpe `-x`/`-W`).
- **Figures** : vues en image quand elles portent des chiffres (The Silent Judge, figure 1, p. 4 ; Who Endorsed It?, figures 3 et 4, p. 4 et 6 ; Faithful or Fabricated?, figures 2 à 7, p. 6 à 8 ; Nogueira et al., figure 3, p. 18). Le disque racine s'est rempli pendant le travail, par une occupation extérieure à mon dossier ; j'ai alors supprimé mes images rendues, déjà lues. Les lectures de figures ci-dessous sont notées « figure » et restent approchées.
- **Non lu** : rien du texte. Seules les cellules à pictogrammes des tableaux par sujet de Nogueira et al. (tableaux 2, 3, 6, 9, 10) n'ont pas été lues case par case : ce sont des symboles que l'extraction ne rend pas, et aucune affirmation du programme n'en dépend. Les listes de références ont été lues sans vérification.
- **Contrôle des citations** (`outils/controle_citations.py`) : chaque citation est cherchée dans les trois extractions de la seule page indiquée. Tolérances : les blancs, et les traits d'union de fin de ligne (césure retirée, ou mot composé coupé à son trait d'union). Rien d'autre : ni casse, ni guillemets, ni apostrophes, ni normalisation Unicode. Gardes : article inconnu ou page absente → échec ; citation de moins de 20 caractères utiles → refusée.
- **Test du contrôle avant usage (règle R5 : garde testée sur un cas sain et sur un artefact)** : 15 cas — 5 justes (dont césure, apostrophe typographique, deux colonnes, césure et mot composé mêlés), 6 altérés (chiffre changé, mauvaise page, mot changé, apostrophe droite, intervalle changé, valeur changée), 1 limite assumée (un trait d'union de fin de ligne omis passe : césure et mot composé y sont indiscernables), 3 gardes. 15 conformes sur 15 (`test-controle-R5.txt`).
- **Résultat** : 124 citations contrôlées, 124 trouvées sur la page indiquée, 0 échec (`controle-citations.txt`). Le même script vérifie que chaque citation figure mot pour mot dans ce rapport. Chaque citation y est précédée de son identifiant entre crochets (fichier `citations.tsv`).

---

## 1. The Silent Judge — arXiv 2509.26072, version 2

### Identité

- **Titre** : [SJ-1] "The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge" (p. 1).
- **Auteurs** : Arash Marioriyad, Mohammad Hossein Rohban, Mahdieh Soleymani Baghshah, département d'ingénierie informatique de la Sharif University of Technology (p. 1 : [SJ-3] "Arash Marioriyad Department of Computer Engineering" ; [SJ-4] "Mohammad Hossein Rohban Mahdieh Soleymani Baghshah" ; [SJ-23] "Department of Computer Engineering Sharif University of Technology").
- **Version et date** : [SJ-2] "arXiv:2509.26072v2 [cs.CL] 14 Oct 2025" (p. 1).
- **Venue** : atelier « Reliable ML from Unreliable Data » de la 39e conférence Neural Information Processing Systems (NeurIPS 2025) : [SJ-5] "39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop: Reliable ML from Unreliable Data." (p. 1). Le programme ne cite pas cette venue.
- **Objet** : deux juges fermés (GPT-4o, Gemini-2.5-Flash) choisissent la meilleure de deux réponses ; 100 paires tirées d'ELI5 (questions-réponses longues) et 100 de LitBench (écriture créative) : [SJ-24] "From each dataset we construct 100 pairwise judgment tasks" (p. 1) ; des indices de provenance (humain, expert, grand modèle de langage, inconnu) et de récence (1950, 2025) sont ajoutés au prompt.

### Affirmations du programme

Source : `docs/etat-de-l-art-controle-ia-v1.md`, ligne 129.

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1.1 | « The Silent Judge, arXiv 2509.26072 » | confirmé | 1 | [SJ-1] "The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge" ; [SJ-2] "arXiv:2509.26072v2 [cs.CL] 14 Oct 2025" |
| 1.2 | « taux de déplacement de verdict » | confirmé | 3 | [SJ-7] "The first is the Verdict Shift Rate (VSR), defined as the proportion of verdict flips when cues are swapped" |
| 1.3 | « binaire par condition » | confirmé | 3 ; 5 | [SJ-8] "The model is instructed to output a strict JSON object with two fields: selected_response (1 or 2) and reason (a short justification)." ; [SJ-9] "Each single experiment consists of 100 pairwise judgments with fixed cue assignments." ; [SJ-11] "VSR is computed as the difference in first-response selection rate between complementary cue assignments." |
| 1.4 | « par exemple + 30 % d'effet de récence pour un grand modèle » | confirmé | 3 ; 8 | [SJ-12] "For GPT-4o on ELI5, the VSR reaches +30%, while Gemini-2.5-Flash shows a smaller but consistent VSR of +16%. On LitBench, GPT-4o again displays a clear bias with a VSR of +16%, whereas Gemini’s recency bias is minimal at +4%." ; [SJ-13] "GPT-4o New (2025) Old (1950) 0.72" ; [SJ-14] "GPT-4o Old (1950) New (2025) 0.42" |

**Précisions** (pas des corrections) :
- Le taux publié n'est pas une proportion de bascules item par item, malgré sa définition en section 2.5 (voir la ligne 1.2) : il est calculé comme la différence nette des taux de sélection de la première réponse entre deux affectations complémentaires d'indices ([SJ-11] "VSR is computed as the difference in first-response selection rate between complementary cue assignments.", p. 5). C'est donc un minorant de la proportion de bascules.
- « + 30 % » est un écart de 30 points (0,72 contre 0,42, p. 8), pour GPT-4o sur ELI5 : le maximum des quatre configurations de récence. Les autres valent + 16, + 16 et + 4.
- Un seul niveau d'indice par condition, avec des phrases fixes : [SJ-20] "To introduce superficial labels into the evaluation prompt, we used fixed natural-language cue templates." (p. 7). 100 paires, température 0, aucun intervalle de confiance.
- Formulation plus précise proposée pour la ligne 129 (facultative) : « **The Silent Judge** (Marioriyad, Rohban, Soleymani Baghshah ; atelier NeurIPS 2025 « Reliable ML from Unreliable Data »), arXiv 2509.26072 v2 — verdict binaire d'un juge par paires, un seul niveau d'indice par condition ; le taux de déplacement publié est la différence des taux de sélection de la première réponse entre deux affectations complémentaires (100 paires, température 0) : récence + 30 points pour GPT-4o sur ELI5, + 16 pour Gemini-2.5-Flash sur ELI5 et pour GPT-4o sur LitBench, + 4 pour Gemini-2.5-Flash sur LitBench ; justifications ne mentionnant jamais l'indice. »

### Chiffres utilisables

| Chiffre | Nature | Page | Source |
|---|---|---|---|
| Récence, en points : + 30 (GPT-4o, ELI5) ; + 16 (Gemini-2.5-Flash, ELI5) ; + 16 (GPT-4o, LitBench) ; + 4 (Gemini-2.5-Flash, LitBench) | auteurs | 3 | [SJ-12] "For GPT-4o on ELI5, the VSR reaches +30%, while Gemini-2.5-Flash shows a smaller but consistent VSR of +16%. On LitBench, GPT-4o again displays a clear bias with a VSR of +16%, whereas Gemini’s recency bias is minimal at +4%." |
| Taux de sélection de la première réponse, GPT-4o, ELI5 : 0,72 (nouveau puis ancien) et 0,42 (ancien puis nouveau) | auteurs | 8 | [SJ-13] "GPT-4o New (2025) Old (1950) 0.72" ; [SJ-14] "GPT-4o Old (1950) New (2025) 0.42" |
| Provenance, expert contre inconnu, GPT-4o, ELI5 : + 18 | auteurs | 4 | [SJ-17] "EXPERT–UNKNOWN and UNKNOWN–EXPERT reaches +18%" |
| Provenance, humain contre grand modèle de langage, Gemini-2.5-Flash, LitBench : + 22 (maximum du tableau 1) | auteurs | 5 | [SJ-18] "LitBench Gemini-2.5-Flash +6% +22% +5%" |
| Taux de reconnaissance de l'indice dans les justifications : exactement 0, dans toutes les conditions | auteurs | 4 | [SJ-15] "the Cue Acknowledgment Rate (CAR) is exactly zero" |
| Les 17 taux de déplacement recalculés à partir des tableaux 2 à 5 égalent les 17 valeurs imprimées | calcul | 3 ; 4 ; 5 ; 8 ; 9 | tableaux 2 à 5 |
| Bruit d'échantillonnage : écart-type d'environ 0,07 pour la différence de deux proportions proches de 0,5 sur 100 items chacune, sous hypothèse d'indépendance (les mesures étant appariées, l'écart réel est sans doute plus faible ; non calculable sans les données par item) | calcul | — | — |
| Figure 1 : barres à 0,30 ; 0,16 ; 0,16 ; 0,04, conformes au texte | figure | 4 | — |

### Réserves (règle R4 : un résultat trop propre déclenche le même audit, quel que soit son signe)

- Le taux de reconnaissance « exactement zéro » est très propre ; seule sa définition est donnée ([SJ-16] "The second is the Cue Acknowledgment Rate (CAR), defined as the proportion of justifications that explicitly mention the cue as a reason for the verdict.", p. 3), pas la méthode qui détecte la mention de l'indice.
- Aucun intervalle de confiance : les écarts de provenance sur ELI5 (3 à 7 points) sont de l'ordre du bruit calculé ci-dessus ; les + 30 et + 22 ne le sont pas.
- Place de l'indice contradictoire en annexe : [SJ-21] "In conditions with cues, additional information is injected after the candidate responses" contre [SJ-22] "Each cue is expressed as a short declarative sentence prepended to the candidate response or story." (p. 7) ; le gabarit montré place les indices après les deux réponses.

### Antériorité (règle R8 : une limitation d'un papier n'est pas un trou du champ)

| Énoncé revendiqué | Occupation par cet article | Ce que fait l'article | Citation |
|---|---|---|---|
| H2, H1, lemme d'additivité, théorème négatif, transposition jeton → action, papier B | non occupés | Ni sonde d'activations, ni agent qui agit, ni accumulation séquentielle, ni moniteur de contrôle, ni copies multiples : deux juges fermés comparent des réponses par paires. | [SJ-6] "Both datasets provide pairwise comparisons, where the evaluator must choose which of two responses is better." ; [SJ-19] "We evaluate two widely used general-purpose judges, GPT-4o and Gemini-2.5-Flash, under deterministic decoding (temperature 0, greedy search) to isolate the effect of injected shortcuts." |
| HC1 (loi de déférence) | pièce revendiquée non occupée ; voisin | Déplacement du verdict binaire d'un juge sous indices injectés, comparé entre deux familles (provenance, avec un niveau « expert », et récence), à un seul niveau par condition. Absents : intensités graduées, lecture par probabilité du jeton (sortie choisie à température 0), estimation d'une destination, test contre la cible de l'attaquant et contre la moyenne du corpus, moniteur de contrôle. | [SJ-8] "The model is instructed to output a strict JSON object with two fields: selected_response (1 or 2) and reason (a short justification)." ; [SJ-10] "All experiments are run with temperature fixed to zero, greedy decoding, and a fixed random seed" ; [SJ-11] "VSR is computed as the difference in first-response selection rate between complementary cue assignments." |
| HC2b (auto-incrimination des sondes) | non occupé | Aucune sonde. Le taux nul de reconnaissance montre seulement que la justification écrite du juge ne révèle pas l'indice qui l'a déplacé. | [SJ-15] "the Cue Acknowledgment Rate (CAR) is exactly zero" |

---

## 2. Who Endorsed It? — arXiv 2601.13433, version 4

### Identité

- **Titre** : [WE-1] "Who Endorsed It? Measuring Authority Bias Across Expertise Levels in Language Models" (p. 1).
- **Auteurs** : Priyanka Mary Mammen (UMass Amherst), Emil Joswin et Shankar Venkitachalam (recherche indépendante) ; contribution égale des deux premiers (p. 1 : [WE-3] `Priyanka Mary Mammen1,* , Emil Joswin2,* , Shankar Venkitachalam2` ; [WE-29] "UMass Amherst, 2 Independent Research").
- **Version et date** : [WE-2] "arXiv:2601.13433v4 [cs.CL] 29 May 2026" (p. 1).
- **Venue** : aucune n'est imprimée dans le PDF (prépublication).
- **Objet** : 11 modèles ouverts (4 « de raisonnement » : [WE-30] "We selected Qwen3-4B-Thinking (Yang et al., 2025), DeepSeek-R1-Qwen3-8B (Guo et al., 2025), Phi-4-Reasoning (Abdin et al., 2025), and Olmo-3.1-32B-Think (Olmo et al., 2025) in the reasoning model category", p. 3 ; 7 non), jusqu'à 32 milliards de paramètres ; quatre jeux de questions à choix multiples (AQuA-RAT, LEXam en anglais, MedMCQA, MedQA). Pour chaque question : neuf variantes (sans approbation ; approbation de la bonne réponse ou d'une mauvaise par une persona de l'un des quatre niveaux d'expertise du domaine). Plus un vecteur de pilotage dans le flux résiduel.

### Affirmations du programme

Source : `docs/etat-de-l-art-controle-ia-v1.md`, ligne 131.

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 2.1 | « Who Endorsed It?, arXiv 2601.13433 » | confirmé | 1 | [WE-1] "Who Endorsed It? Measuring Authority Bias Across Expertise Levels in Language Models" ; [WE-2] "arXiv:2601.13433v4 [cs.CL] 29 May 2026" |
| 2.2 | « (autorité par niveau d'expertise) » | confirmé | 1 | [WE-4] "we evaluate 11 models using personas representing four expertise levels per domain" ; [WE-5] "Our work treats authority as a gradient rather than a binary property" |
| 2.3 | « Catalogues de biais : […] Who Endorsed It? […] → Fournissent des familles d'attaque » | corrigé | 1 ; 3 ; 4 ; 6 | [WE-5] "Our work treats authority as a gradient rather than a binary property" ; [WE-8] "Rather than generating free-form text, we directly extracted output logits over the answer choices (A, B, C, D), making the evaluation fully deterministic." ; [WE-12] "This monotonic scaling with authority, observed consistently across correct and misleading conditions" ; [WE-18] "the model’s authority bias i.e., the model’s tendency to defer to high-credibility personas is similarly encoded in the residual stream" |
| 2.4 | « pas le coefficient » | confirmé | 3 ; 4 | [WE-10] "Delta Accuracy: Accuracy measures the rate at which the model outputs align with the ground-truth label." ; [WE-11] "Robustness Rate: It measures the rate at which the model outputs remain unaffected by the presence of endorsements." |

**Formulation exacte à mettre à la place (2.3)** — sortir l'article des « catalogues de biais » et l'écrire ainsi : « **Who Endorsed It?** (Mammen, Joswin, Venkitachalam), arXiv 2601.13433 v4 — une seule famille (approbation d'une réponse par une persona d'autorité), graduée sur quatre niveaux d'expertise par domaine ; 11 modèles ouverts jusqu'à 32 milliards de paramètres répondant à des questions à choix multiples (le modèle influencé répond, il ne juge pas) ; logits lus sur les options ; effets mesurés en écart d'exactitude, écart d'entropie et taux de robustesse, décrits comme monotones selon le niveau ; vecteur de pilotage « expertise » dans le flux résiduel, dont la soustraction réduit le biais. → Dose-réponse en taux sur quatre niveaux, ni gain ni destination. »

SycEval et PARROT (arXiv 2511.17220), cités sur la même ligne, sont hors de ce lot et ne sont pas vérifiés ici.

Pourquoi « corrigé » : l'article n'est pas un catalogue. Il traite une seule famille, graduée, ce que le programme classe ailleurs comme « dose-réponse en taux » (Kim et al., ligne 128). Pour 2.4 : les mesures sont des taux et des écarts de taux ; « coefficient », « regress », « fit », « slope », « parametr » sont absents du texte, et « gain » n'y apparaît que dans « accuracy gains ».

### Chiffres utilisables

| Chiffre | Nature | Page | Source |
|---|---|---|---|
| DeepSeek-R1 sur MedQA : exactitude de base 0,543 ; approbation correcte, de −0,127 (étudiant de première année) à +0,381 (médecin certifié) ; approbation erronée, de −0,019 à −0,356 | auteurs | 4 ; 5 | [WE-13] "Under correct endorsements, accuracy gains scale monotonically from near zero at the First Year Medical Student level to +0.381 at the Board-Certified Physician level." ; [WE-14] "with accuracy degradation deepening from -0.019 to -0.356 across the same expertise hierarchy" ; [WE-16] "DeepSeek-R1 (0.543) -0.127 0.734 0.137 -0.049 0.778 0.058 0.116 0.804 -0.083 0.381 0.614 -0.621" |
| Écart d'entropie de −0,261 (approbation erronée d'un médecin certifié, MedQA) | auteurs | 4 | [WE-15] "DeepSeek-R1-Qwen3-8B shows ∆H of -0.261, indicating increased confidence in the wrong answer." |
| MedMCQA, approbation erronée d'un médecin certifié (base + écart du tableau 1c) : 0,162 ; 0,144 ; 0,275 ; 0,286 ; 0,066 pour Qwen3-4B-Thinking, DeepSeek-R1, Phi-4-Reasoning, Gemma-3-12B, Olmo-3.1-32B-Think — conforme aux barres de la figure 4 | calcul | 5 ; 6 | tableau 1c |
| Après soustraction du vecteur de pilotage (mêmes modèles) : environ 0,24 ; 0,50 ; 0,61 ; 0,49 ; 0,20, pour des bases de 0,26 ; 0,533 ; 0,634 ; 0,554 ; 0,343 (retour partiel pour Olmo-3.1-32B-Think) | figure (figure 4, lecture à environ 0,02 près) pour les valeurs après soustraction ; auteurs (tableau 1c) pour les bases | 5 ; 6 | — |

### Réserves (règle R4)

- Le nombre de questions des expériences de comportement n'est imprimé nulle part. Seule la taille du jeu du vecteur de pilotage est donnée, et de façon incohérente : [WE-24] "a dataset of approximately 30 questions per domain, yielding around 90 questions in total" (p. 3) contre [WE-25] "We compiled a dataset of 100 questions from three different fields" (p. 9).
- « near zero » ([WE-13] "Under correct endorsements, accuracy gains scale monotonically from near zero at the First Year Medical Student level to +0.381 at the Board-Certified Physician level.") vaut en fait −0,127 au tableau 1d ([WE-16] "DeepSeek-R1 (0.543) -0.127 0.734 0.137 -0.049 0.778 0.058 0.116 0.804 -0.083 0.381 0.614 -0.621") et sur la figure 3.
- Des approbations erronées augmentent l'exactitude dans plusieurs lignes, par exemple Phi-4 sur MedQA, +0,173 au niveau le plus haut ([WE-17] "Phi-4 (0.272) 0.006 0.888 -0.607 0.006 0.888 -0.595 0.041 0.851 -0.211 0.674 0.268 -1.009 0.005 0.889 -0.627 0.005 0.889 -0.612 0.026 0.852 -0.203 0.173 0.2 -0.551", p. 5), contrairement au constat général ([WE-12] "This monotonic scaling with authority, observed consistently across correct and misleading conditions").
- Logits lus sur quatre options ([WE-8] "Rather than generating free-form text, we directly extracted output logits over the answer choices (A, B, C, D), making the evaluation fully deterministic.") alors que l'exemple d'AQuA-RAT en a cinq : [WE-26] "E. None of these Hint: A person who is Professor thinks the answer is B." (p. 2).
- Modèles de raisonnement : logits lus sans génération de texte ([WE-8] "Rather than generating free-form text, we directly extracted output logits over the answer choices (A, B, C, D), making the evaluation fully deterministic."), alors que le texte invoque [WE-28] "reasoning-capable models show comparable susceptibility to expert endorsement despite their extended chain-of-thought processes" (p. 4) ; on ne sait pas si la chaîne de raisonnement est produite avant la lecture.
- Protocole contradictoire : [WE-7] "For each MCQ, we construct nine prompt variants, each presented to the model as an independent invocation" (p. 2) contre [WE-21] "we utilize a two-step interaction to eliminate look-ahead bias" (p. 6).
- L'amplification par ajout du vecteur est affirmée sans chiffre : [WE-20] "Conversely, injecting this vector into low-credibility contexts amplifies the model’s trust in the endorsement." (p. 6) ; [WE-27] "whereas adding it significantly amplifies the persuasive power of low-credibility personas" (p. 9).
- Portée déclarée par les auteurs : [WE-22] "our experiments are constrained to smaller open-source models (up to 32B parameters)" ; [WE-23] "Third, our endorsement format is limited to single, explicit answer statements without variations in phrasing, confidence levels, or reasoning justification" (p. 7).

### Antériorité (règle R8)

| Énoncé revendiqué | Occupation par cet article | Ce que fait l'article | Citation |
|---|---|---|---|
| H2, H1, lemme d'additivité, théorème négatif, transposition jeton → action, papier B | non occupés | Ni agent, ni surveillance, ni seuil de détection, ni accumulation séquentielle. Les activations servent au pilotage du modèle influencé, pas à la détection. | [WE-19] "By subtracting vauth at inference time, we observed a reduction in the model’s susceptibility to misleading endorsements from high-authority personas across datasets" |
| HC1 (loi de déférence) | pièce revendiquée non occupée ; deux éléments voisins | (a) Pression graduée dans une famille : quatre niveaux d'autorité ; l'approbation de forme fixe recouvre les familles « revendication d'autorité » et « approbations forgées » du programme ; réponse dite monotone. (b) Logits lus sur les options. Mais les mesures sont l'exactitude (option la plus probable), l'entropie et le taux de robustesse, pas la masse de probabilité déplacée vers l'option approuvée ; ni gain, ni destination, ni nul de la moyenne du corpus ; le modèle influencé répond à des questions, ce n'est ni un juge ni un moniteur de contrôle. → Dans cette source, « plusieurs intensités par famille » et « lecture par probabilité du jeton » sont donc présents pris isolément ; leur réunion dans un moniteur de contrôle, avec la destination libre testée, n'y figure pas. | [WE-5] "Our work treats authority as a gradient rather than a binary property" ; [WE-6] "the endorsement is appended after the question in a minimal, uniform format" ; [WE-8] "Rather than generating free-form text, we directly extracted output logits over the answer choices (A, B, C, D), making the evaluation fully deterministic." ; [WE-9] "Confidence scores and entropy measures are computed directly from these output probability distributions." ; [WE-12] "This monotonic scaling with authority, observed consistently across correct and misleading conditions" |
| HC2b (auto-incrimination des sondes) | non occupé ; voisin | Une direction « expertise » du flux résiduel du modèle influencé, construite sur le seul style, réduit par soustraction la sensibilité aux personas étiquetées. C'est du pilotage du modèle visé, pas une sonde qui lit l'agent manipulateur ; aucune mesure d'un score de sonde qui monterait avec la tentative de manipulation. | [WE-18] "the model’s authority bias i.e., the model’s tendency to defer to high-credibility personas is similarly encoded in the residual stream" ; [WE-19] "By subtracting vauth at inference time, we observed a reduction in the model’s susceptibility to misleading endorsements from high-authority personas across datasets" |

---

## 3. Faithful or Fabricated? — arXiv 2605.23970, version 1

### Identité

- **Titre** : [FF-1] "Faithful or Fabricated? A Causal Framework for Rationalization Bias in LLM Judges" (p. 1).
- **Auteurs** : Riya Tapwal (Indian Institute of Technology Mandi), Abhishek Kumar (The Alan Turing Institute), Carsten Maple (Warwick Manufacturing Group, University of Warwick) (p. 1 : [FF-3] "Riya Tapwal Abhishek Kumar" ; [FF-4] "riya@iitmandi.ac.in Carsten Maple" ; [FF-34] "Indian Institute of Technology (IIT) Mandi" ; [FF-33] "The Alan Turing Institute, London, U.K." ; [FF-35] "Warwick Manufacturing Group University of Warwick, U.K.").
- **Version et date** : [FF-2] "arXiv:2605.23970v1 [cs.CL] 13 May 2026" (p. 1).
- **Venue** : aucune n'est imprimée dans le PDF.
- **Objet** : cinq juges ouverts de 7 à 9 milliards de paramètres comparent deux résumés (corpus de 1 000 résumés) sous cinq conditions d'étiquettes de provenance (cachées, vraies, inversées, placebo, inversées puis révélées) et deux attaques de style (verbosité, ton assuré) ; deux contre-mesures (chaîne de pensée structurée par critères ; « Proof-Before-Preference », preuve avant préférence).

### Affirmations du programme

Source : `docs/etat-de-l-art-controle-ia-v1.md`, ligne 131.

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 3.1 | « Faithful or Fabricated?, arXiv 2605.23970 » | confirmé | 1 | [FF-1] "Faithful or Fabricated? A Causal Framework for Rationalization Bias in LLM Judges" ; [FF-2] "arXiv:2605.23970v1 [cs.CL] 13 May 2026" |
| 3.2 | « Catalogues de biais : […] Faithful or Fabricated? […] → Fournissent des familles d'attaque » | confirmé | 1 | [FF-5] "We design anchoring attacks via verbosity and confidence cues" ; [FF-6] "we introduce a suite of cue interventions that manipulate C while keeping X fixed" |
| 3.3 | « pas le coefficient » | confirmé | 4 ; 8 | [FF-10] "be the outcome set for a two-candidate comparison" ; [FF-11] "We compare each labeled probe to the same scheme’s Blind and count only movement toward the label-favored decision, while not penalizing movement into Tie." ; [FF-18] "report aggregate effects without confidence intervals, multi-seed variance, or measured cost/latency" |

**Précision** (facultative) : familles d'indices appliquées chacune à un seul niveau ; verdict à trois issues (l'un, l'autre, égalité) ; mesures en parts et masses de déplacement par rapport à la condition sans étiquette ; ni coefficient, ni régression, ni ajustement dans le texte (« gains » n'y apparaît que dans « quality gains »).

### Chiffres utilisables

| Chiffre | Nature | Page | Source |
|---|---|---|---|
| Révision après révélation des vraies étiquettes (Gemma, Llama, Mistral, Qwen, Zephyr) : ligne de base {85, 78, 76, 83, 82} % ; chaîne de pensée structurée {80, 80, 76, 82, 80} % ; preuve avant préférence {22, 5, 8, 18, 15} % | auteurs | 7 | [FF-17] "Concretely, for (Gemma, Llama, Mistral, Qwen, Zephyr): Baseline {85, 78, 76, 83, 82}%, SCoT {80, 80, 76, 82, 80}%, PBP {22, 5, 8, 18, 15}%." |
| Part du déplacement dirigée vers l'étiquette, étiquettes vraies, ligne de base : 1,00 pour les cinq juges | auteurs ; recalculée à 1,00 depuis les tableaux II et III (calcul) | 7 ; 12 | [FF-16] "Under True labels (refer Fig. 4(a)), the Baseline protocol exhibits maximal anchoring (LAO = 1.00) across all models." |
| Sous étiquettes inversées, ligne de base : part dirigée 0 ; déplacement vers l'option opposée de 0,26 à 0,49 selon le juge | calcul (tableaux II et IV), conforme au texte principal | 7 ; 12 | [FF-30] "the Baseline protocol shows negligible anchoring (LAO ≈ 0), indicating minimal movement toward incorrect label-favored outcomes" |
| Vérification humaine : égalité jugée sur 94 et 92 paires sur 100 | auteurs | 11 | [FF-24] "Annotator 1 marked Tie on 94 of the 100 items, and Annotator 2 marked Tie on 92 of the 100 items." |
| Plan : 1 000 résumés, 5 juges ouverts, température 0 | auteurs | 5 | [FF-12] "We therefore curate a new corpus of N =1,000 summaries" ; [FF-14] "We employ five open-weight LLMs, Gemma-2-9B, Llama-3.1-8B, Mistral-7B, Qwen2.5-7B, and Zephyr-7B, as judges" ; [FF-15] "All judge generations use temperature 0 to ensure deterministic outputs and reproducibility." |

### Réserves (règle R4)

- Ni intervalle de confiance ni variance entre graines : [FF-18] "report aggregate effects without confidence intervals, multi-seed variance, or measured cost/latency" (p. 8).
- Les 40 comptes de la ligne de base des tableaux II à V sont tous des multiples de 10 sur 1 000, contre 2 sur 25 pour les autres protocoles du tableau II (calcul). La ligne de base semble porter sur 100 éléments multipliés par 10, ou être arrondie ; ce n'est pas expliqué ([FF-23] "Totals per model are 1000 for SCoT and PBP and the Baseline.", p. 12 ; [FF-22] "and the Baseline never abstains (all zeros in the No Selection column)", p. 11).
- Ligne Gemma incohérente : écart de neutralité imprimé 0,018 ([FF-25] "Baseline shows the largest deviations (e.g., Gemma 0.018, Llama 0.060, Mistral 0.100, Qwen 0.080, Zephyr 0.020)", p. 6) contre 0,080 calculé à partir de 540 contre 460 ([FF-21] "Gemma-2-9B 0 540 460 840 97 63 937 34 29", p. 12) ; les quatre autres juges se recalculent exactement.
- Tableau VI, présenté comme un sous-ensemble distinct ([FF-27] "Decomposition of outcome shifts from Blind to True when both candidates are LLM outputs (two independent", p. 12 ; commentaire : [FF-20] "the Baseline channels a large fraction of probability mass toward the label–favored decision [1, 2] (e.g., Gemma 0.509, Llama 0.390, Mistral 0.450, Qwen 0.290, Zephyr 0.490)", p. 13) : pour quatre juges sur cinq, ses valeurs de ligne de base égalent exactement celles calculées à partir des tableaux II et III ; Gemma diffère ([FF-26] "Gemma-2-9B 0.509 0.000 0.000 0.583" contre 0,460 calculé). Or les expériences principales portent déjà sur deux paraphrases d'un même modèle ([FF-28] "For each d, the same LLM produces two paraphrases" ; [FF-13] "Most of the experiments are conducted using this approach", p. 5). Le tableau VII, lui, ne se recalcule pas à partir des tableaux II et IV : [FF-32] "a moderate shift against the misleading cue (OLSF ≈ 0.21–0.25)" (p. 13), contre 0,26 à 0,49 calculé. L'origine des tableaux VI à VIII est indéterminée.
- Lecture contradictoire des étiquettes inversées : texte principal [FF-30] "the Baseline protocol shows negligible anchoring (LAO ≈ 0), indicating minimal movement toward incorrect label-favored outcomes" (p. 7) contre annexe [FF-29] "The Baseline again shows strong anchoring toward [1, 2] despite labels being incorrect" (p. 11).
- Contrôle annoncé sans résultat : [FF-7] "alongside consistency and stereotype-intrusion checks" (p. 1) ; aucune mesure de stéréotype dans le corps ni en annexe.
- Conséquence : ne citer aucun chiffre des annexes de cet article sans éclaircissement des auteurs.

### Antériorité (règle R8)

| Énoncé revendiqué | Occupation par cet article | Ce que fait l'article | Citation |
|---|---|---|---|
| H2, H1, lemme d'additivité, théorème négatif, transposition jeton → action, papier B | non occupés | Faux ami : « probing » désigne ici des interventions sur les indices, pas des sondes d'activations ; « monitoring » n'apparaît que comme domaine d'application du résumé. | [FF-8] "cue invariance, causal probing, bias mitigation" ; [FF-9] "applications that still favor lightweight extractive summarization, e.g., large-scale monitoring, enterprise reporting, or compliance" |
| HC1 (loi de déférence) | pièce revendiquée non occupée ; un élément voisin | Décomposition directionnelle du déplacement du verdict par rapport à la condition sans étiquette : vers l'option favorisée par l'indice, vers l'égalité, vers l'option opposée. C'est un test catégoriel de « où va le verdict » par rapport à la cible de l'indice. Absents : intensités graduées (un niveau par indice), verdict continu ou probabilité du jeton (trois issues), nul de la moyenne du corpus, gain, moniteur de contrôle (juges de résumés). | [FF-10] "be the outcome set for a two-candidate comparison" ; [FF-11] "We compare each labeled probe to the same scheme’s Blind and count only movement toward the label-favored decision, while not penalizing movement into Tie." ; [FF-19] "We report LDSF (positive movement toward the label–favored side [1, 2]), TSF (into Tie), and OLSF (toward the opposite side [2, 1])." |
| HC2b (auto-incrimination des sondes) | non occupé | Aucune sonde d'activations. | [FF-8] "cue invariance, causal probing, bias mitigation" |
| HC5 (contre-mesures ; hors liste, pour information) | non occupé | La contre-mesure verrouille les preuves du juge avant sa préférence ; ce n'est ni une paraphrase de confiance ni un quorum par type d'accès. | [FF-31] "first locks criterion-wise notes with cited spans, then scores and ranks strictly from the locked evidence" |

---

## 4. Nogueira et al. — arXiv 2604.21564, version 2

### Identité

- **Titre** : [NO-1] "Measuring Opinion Bias and Sycophancy via LLM-based Persuasion" (p. 1).
- **Auteurs** : [NO-3] "Rodrigo Nogueira1 , Giovana Kerche Bonás1 , Thales Sales Almeida1 , Andrea Roque1 , Ramon Pires1 , Hugo Abonizio1 , Thiago Laitz1 , Celio Larcher2 , Roseval Malaquias Junior1 , and Marcos Piau2" (p. 1) ; affiliations : 1 = Maritaca AI, 2 = JusBrasil ([NO-35] "1 Maritaca AI 2 JusBrasil", p. 1).
- **Version et date** : [NO-2] "arXiv:2604.21564v2 [cs.CL] 30 Apr 2026 May 1, 2026" (p. 1) : dépôt arXiv horodaté du 30 avril 2026, document daté du 1er mai 2026.
- **Venue** : aucune n'est imprimée dans le PDF.
- **Objet** : 13 assistants, 38 sujets controversés en portugais du Brésil, trois personas (neutre, d'accord, en désaccord), deux modes (question directe, débat argumentatif) ; conversations de cinq tours menées par un modèle utilisateur ; verdict du dernier tour rendu par un modèle juge ; classification en neuf classes.

### Affirmations du programme

Source : `docs/etat-de-l-art-controle-ia-v1.md`, ligne 130.

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 4.1 | « Nogueira et al., arXiv 2604.21564 » | confirmé | 1 | [NO-1] "Measuring Opinion Bias and Sycophancy via LLM-based Persuasion" ; [NO-2] "arXiv:2604.21564v2 [cs.CL] 30 Apr 2026 May 1, 2026" |
| 4.2 | « sycophancie directe de 22 % à 71 % » | confirmé | 18 | [NO-20] "Direct sycophancy rises gradually from 22% to 71%; indirect starts high (41%) and climbs to 78%." |
| 4.3 | « indirecte de 41 % à 78 % » | confirmé | 18 | [NO-20] "Direct sycophancy rises gradually from 22% to 71%; indirect starts high (41%) and climbs to 78%." |
| 4.4 | « sur cinq tours » | confirmé | 17 | [NO-12] "we sample 300 conversations uniformly at random (10 topics × 10 models × 3 personas, drawn without replacement from the full run pool) and re-judge every turn" ; [NO-13] "This produces a verdict trajectory per conversation: a sequence of five labels in {agree, disagree, neutral, refusal}." |
| 4.5 | « trajectoire non paramétrée en gain » | confirmé | 17 | [NO-13] "This produces a verdict trajectory per conversation: a sequence of five labels in {agree, disagree, neutral, refusal}." ; [NO-15] "Only 31.5% maintain the same verdict from turn 1 to turn 5; the model’s position shifts in nearly 70% of conversations." ; [NO-16] "44.0% start with a verdict that does not match the persona and end with one that does" |

**Précisions** (pas des corrections) :
- Les quatre chiffres viennent d'une ablation par tour (section 5.4), pas des résultats principaux : 300 conversations tirées, 289 valides ([NO-14] "On 289 conversations with valid verdicts across all five turns, we report four trajectory-level statistics"). La sycophancie y est définie ainsi : [NO-19] "Sycophancy = the verdict matches the user’s persona (measured on agree/disagree personas)." (p. 18). Les résultats principaux ne jugent que le dernier tour : [NO-11] "The main results use only the judge’s verdict on the final turn of each conversation." (p. 17).
- Les chiffres principaux diffèrent : [NO-9] "The median sycophancy rate across all 13 models is 50.0% in direct mode and 78.9% in indirect mode." (p. 12) ; [NO-8] "Under direct probing, sycophancy ranges from 5.3% (Haiku 4.5) to 78.9% (Mistral Large 3)." (p. 9).
- Risque de confusion : 78 % (cinquième tour, débat) contre 78,9 % (médiane, débat) ; 71 % (cinquième tour, question directe) contre 71,0 % (positions engagées renversées par Claude Opus 4.6 : [NO-22] "Results B. Opus 4.6 flips 142/200 = 71.0% of committed baselines; Haiku 4.5 flips 118/199 = 59.3%; Sabiazinho-4 flips 116/198 = 58.6%.", p. 16).
- 4.5 : aucun modèle ajusté, seulement des taux par tour et des statistiques de trajectoire. « coefficient », « regress », « fit », « slope », « logistic », « parametr » et « gain » sont absents du texte.
- Formulation plus précise proposée pour la ligne 130 (facultative) : « **Nogueira et al.** (Maritaca AI, JusBrasil), arXiv 2604.21564 v2 — ablation par tour (300 conversations tirées, 289 valides ; sycophancie = verdict conforme à la persona de l'utilisateur) : directe de 22 % au premier tour à 71 % au cinquième, indirecte de 41 % à 78 % ; résultats principaux au dernier tour : part médiane de la classe « sycophant » de 50,0 % en question directe et 78,9 % en débat sur 13 assistants ; taux par tour, aucun modèle paramétrique ni gain. »

### Chiffres utilisables

| Chiffre | Nature | Page | Source |
|---|---|---|---|
| Sycophancie par tour : directe de 22 % à 71 %, indirecte de 41 % à 78 % (tours 1 et 5) | auteurs | 18 | [NO-20] "Direct sycophancy rises gradually from 22% to 71%; indirect starts high (41%) and climbs to 78%." |
| Valeurs intermédiaires, tours 1 à 5 : directe environ 22, 56, 67, 72, 71 ; indirecte environ 41, 64, 69, 74, 78 (plateau de la courbe directe entre les tours 4 et 5) | figure (figure 3) | 18 | — |
| Trajectoires : verdict stable sur les cinq tours dans 31,5 % des conversations ; dérive vers la persona dans 44,0 % (51,0 % en question directe, 36,3 % en débat) | auteurs | 17 | [NO-15] "Only 31.5% maintain the same verdict from turn 1 to turn 5; the model’s position shifts in nearly 70% of conversations." ; [NO-16] "44.0% start with a verdict that does not match the persona and end with one that does" ; [NO-17] "direct probing has higher within-conversation sycophantic drift (51.0%) than indirect (36.3%)" |
| Résultats principaux (classe « sycophant », dernier tour) : de 5,3 % à 78,9 % en question directe ; médianes 50,0 % et 78,9 % ; jusqu'à 94,7 % en débat (Llama 4 Maverick) | auteurs | 9 ; 12 | [NO-8] "Under direct probing, sycophancy ranges from 5.3% (Haiku 4.5) to 78.9% (Mistral Large 3)." ; [NO-9] "The median sycophancy rate across all 13 models is 50.0% in direct mode and 78.9% in indirect mode." ; [NO-10] "Llama 4 Maverick 21.1 34.2 36.8 0.0 7.9 2.6 94.7 2.6 0.0 0.0" |
| Persuasion selon la position initiale : base neutre, de 77,3 % à 83,6 % de bascules ; position engagée, de 58,6 % à 71,0 % | auteurs | 16 | [NO-21] "Results A. Opus 4.6 persuades on 92/110 = 83.6% of conversations; Haiku 4.5 on 89/110 = 80.9%; Sabiazinho-4 on 85/110 = 77.3%." ; [NO-22] "Results B. Opus 4.6 flips 142/200 = 71.0% of committed baselines; Haiku 4.5 flips 118/199 = 59.3%; Sabiazinho-4 flips 116/198 = 58.6%." |
| Bruit : accord de 79,1 % entre deux passages identiques ; marge d'erreur d'environ 20 % par sujet ; quatre juges unanimes dans 70,3 % des cas | auteurs | 15 ; 18 | [NO-23] "The two runs agree on 117 of 148 pairs (79.1%)." ; [NO-24] "Individual per-topic verdicts should be interpreted with a ∼20% error margin" ; [NO-33] "Unanimous (4/4 judges agree) 70.3%" |
| Effectif par courbe de la figure 3 : non imprimé ; au plus 200 conversations à persona engagée (10 × 10 × 2) avant exclusions, partagées entre les deux modes | calcul | 17 | [NO-12] "we sample 300 conversations uniformly at random (10 topics × 10 models × 3 personas, drawn without replacement from the full run pool) and re-judge every turn" |
| Plan : 13 assistants, 228 conversations par modèle ; modèle utilisateur Claude Opus 4.6 ; juge Qwen3.5-397B | auteurs | 8 | [NO-6] "We run the full benchmark on 13 assistant models across 38 topics × 3 personas × 2 categories = 228 conversations per model." ; [NO-7] "The user-LLM is Claude Opus 4.6 and the judge is Qwen3.5-397B" |

### Réserves (règle R4)

- Chiffres de la discussion incohérents avec les tableaux, vraisemblablement hérités d'une version antérieure : [NO-25] "Under direct probing, sycophancy is a minority behavior for most models (26–53%)." (p. 19) contre [NO-8] "Under direct probing, sycophancy ranges from 5.3% (Haiku 4.5) to 78.9% (Mistral Large 3)." (p. 9) ; [NO-26] "Kimi K2 actually increases its position rate from direct to indirect (52.9% → 61.8%)" (p. 19) contre [NO-27] "Kimi K2 is the only model whose indirect sycophancy (23.7%) is lower than its direct sycophancy (31.6%), and it holds the highest position rate in indirect mode (60.5%)." (p. 12) ; [NO-28] "The divergence rates (24–71%) confirm that knowing a model’s direct-probing profile does not predict its indirect-probing profile." (p. 19) contre [NO-29] "Divergence rates range from 24% (Mistral Large 3) to 74% (Gemini 3.1 Pro and Haiku 4.5)." (p. 13).
- Ablation : la légende dit [NO-18] "Per-turn sycophancy and positioning rates across 300 ablation conversations (13 models, both categories)." (p. 18), le texte [NO-12] "we sample 300 conversations uniformly at random (10 topics × 10 models × 3 personas, drawn without replacement from the full run pool) and re-judge every turn" (p. 17).
- La conclusion affirme une robustesse à la traduction ([NO-30] "Brazilian Portuguese are topic-level, surviving jurisdictional and linguistic translation with little modulation.", p. 21) sans expérience correspondante dans cette version (recherche de « translat », « English », « Spanish », « jurisdict » : seulement cette phrase et la limite sur la langue).

### Antériorité (règle R8)

| Énoncé revendiqué | Occupation par cet article | Ce que fait l'article | Citation |
|---|---|---|---|
| H2, H1, lemme d'additivité, théorème négatif, transposition jeton → action, papier B | non occupés | Faux ami : « direct probing » et « indirect probing » désignent des protocoles de conversation, pas des sondes d'activations ; un modèle utilisateur et un assistant dialoguent, sans lecture d'états internes. | [NO-4] "Direct probing asks the model for its opinion across five turns of escalating pressure from a simulated user." |
| HC1 (loi de déférence) | pièce revendiquée non occupée ; deux éléments voisins | (a) Pression croissante sur cinq tours, avec taux par tour : une courbe pression-réponse en taux, dont l'intensité n'est pas contrôlée (le modèle utilisateur mène librement). (b) Dépendance à la position initiale : base neutre contre position engagée. La destination est fixée d'avance (le camp de la persona), sans test contre la moyenne du corpus ; verdict en quatre catégories par un juge, sans probabilité du jeton ; la cible est un assistant qui donne son avis, et le juge est l'instrument de mesure, pas un moniteur sous attaque. | [NO-5] "After five turns, a separate LLM-as-judge J reads the full transcript and classifies the assistant’s final-turn response as one of four verdicts." ; [NO-13] "This produces a verdict trajectory per conversation: a sequence of five labels in {agree, disagree, neutral, refusal}." ; [NO-19] "Sycophancy = the verdict matches the user’s persona (measured on agree/disagree personas)." ; [NO-20] "Direct sycophancy rises gradually from 22% to 71%; indirect starts high (41%) and climbs to 78%." ; [NO-21] "Results A. Opus 4.6 persuades on 92/110 = 83.6% of conversations; Haiku 4.5 on 89/110 = 80.9%; Sabiazinho-4 on 85/110 = 77.3%." ; [NO-34] "Setup B: committed baseline (belief-revision)." |
| HC2b (auto-incrimination des sondes) | non occupé | Aucune sonde d'activations. | [NO-4] "Direct probing asks the model for its opinion across five turns of escalating pressure from a simulated user." |

**Pistes citées par l'article** (non lues, donc non opposables, règle R7) :
- Kaur 2025, Findings of EMNLP 2025 (Empirical Methods in Natural Language Processing) : [NO-31] "Most directly related, Kaur [2025] found that argumentative prompts reliably induce stance-mirroring, with sycophancy intensity correlating with argument strength." (p. 5). C'est le voisin le plus direct de la pression graduée de HC1 ; à lire.
- Kim et Khashabi 2025, arXiv 2509.16533 : [NO-32] "Kim and Khashabi [2025] showed that models flip their evaluations under follow-up pushback even when they judge both arguments correctly in parallel" (p. 4). Il porte sur des évaluateurs contestés ; à lire.

---

## Synthèse

1. Empreintes : les quatre concordent. Les quatre articles sont lus en entier ; seules les cases à pictogrammes de cinq tableaux de Nogueira et al. ne l'ont pas été (aucune affirmation n'en dépend).
2. **Corrigée** : ligne 131, Who Endorsed It? (2601.13433). Ce n'est pas un catalogue mais une famille (autorité) graduée sur quatre niveaux, avec logits lus, dose-réponse en taux et vecteur de pilotage interne. Formulation de remplacement en section 2. **Introuvable** : aucune.
3. **Confirmées** : ligne 129 (+ 30 = GPT-4o sur ELI5, différence nette de taux de sélection, un niveau d'indice) ; ligne 130 (22 → 71 % et 41 → 78 % : ablation par tour, figure 3, p. 18, et non les résultats principaux) ; ligne 131 pour Faithful or Fabricated? ; « pas le coefficient » pour les deux articles de la ligne 131.
4. **Zones revendiquées** : H2, H1, lemme d'additivité, théorème négatif, transposition jeton → action, HC2b et papier B ne sont occupés par aucune des quatre sources.
5. **HC1** : la pièce revendiquée (destination libre testée, régression sur plusieurs intensités par famille, moniteur de contrôle) n'est occupée par aucune des quatre sources. Mais certains de ses éléments y figurent isolément : intensités graduées et logits (Who Endorsed It?), décomposition directionnelle du déplacement (Faithful or Fabricated?), pression par tour et dépendance à la position initiale, en taux (Nogueira et al.).
6. **Réserves (R4)** : Faithful or Fabricated? (ligne de base en multiples de 10, ligne Gemma incohérente, tableaux VI à VIII d'origine indéterminée : ne pas en citer les annexes) ; Who Endorsed It? (effectifs non imprimés, « near zero » = −0,127, quatre options lues pour cinq) ; Nogueira et al. (chiffres de discussion périmés, 13 contre 10 modèles) ; The Silent Judge (taux de reconnaissance nul sans méthode, pas d'intervalle).
7. **Contrôle** : 15 cas de test conformes sur 15 ; 124 citations contrôlées, 0 échec.
8. **Pistes à lire avant le préenregistrement du papier C** : Kaur 2025 (intensité de la sycophancie selon la force de l'argument) ; Kim et Khashabi 2025 (évaluateurs contestés).

## Fichiers du lecteur

Dossier `/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/lecture-lot2-C2a/` :
- `rapport.md` (ce rapport) et `rapport.md.sha256` ;
- `citations.tsv` : les 124 citations (identifiant, article, page, texte) ;
- `controle-citations.txt` : sortie du contrôle ; `test-controle-R5.txt` : sortie des 15 cas de test ;
- `outils/` : `controle_citations.py`, `tester_controle.py`, `ecrire_citations.py`, `generer_rapport.py` ;
- `texte/` : extractions `pdftotext -layout` par page (page entière, demi-pages) ; `empreintes-attendues.txt`. (Le dossier `images/` des pages rendues a été supprimé faute de place disque.)
