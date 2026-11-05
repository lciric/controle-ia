# Carte des zones libres, complément v3 : Xiong et al. (« Probe-Rewrite-Evaluate ») et Abdelnabi et Salem (« The Hawthorne Effect in Reasoning Models »)

- **Auteur** : le même sous-agent lecteur que la v1 et la v2. Je n'ai écrit aucun des textes du programme qui sont en jeu. Complément écrit le 26 octobre 2026, à partir de 10:37 UTC (`date -u`).
- **Statut** : ce texte complète la v1 et la v2 sans les remplacer. Les deux sont inchangées, vérifiées par leurs fichiers `.sha256` juste avant d'écrire celui-ci :
  - `carte-zones-libres-v1.md` : `134040bd9a126dce4592aa3b357375f0209f987610d3be21a6848f647eaf59b4` ;
  - `carte-zones-libres-v2.md` : `fe1e93c1efe7c9117c9f0b22711912394c5b40d0180b904bf61e324cf0943d3a`.
- **Objet** : lire les deux papiers que la v2 posait comme préalables à toute revendication (§ 0 et § 5 de la v2), puis :
  - conclure sur la question « un plan croisé format × contexte, avec instruments certifiés, sur un modèle de 30 à 70 milliards de paramètres » ;
  - dire ce que ces deux papiers enlèvent à l'extension sur le 8B (v1, Q4 (i)).
- **Règles** : celles de la v1. « p. N » désigne la page du PDF. Tout chiffre tiré d'un PDF porte sa page. Ce qui n'est pas lu est dit.

## 0. Verdict

- **Toujours non, désormais sur sept papiers.**
  - **Xiong et al.** utilisent la sonde de Nguyen et al. sur Llama-3.3-70B-Instruct. Ils réécrivent **des items d'évaluation seulement**, et changent dans un même geste le format, le style, la personne grammaticale et la longueur (p. 3, p. 11 à 13). Il n'y a ni facteur de contexte ou de provenance croisé, ni bras « réel avec marqueurs ».
  - **Abdelnabi et Salem** manipulent un indice de contexte (entités plausibles contre entités fictives), **à contenu égal**, sur trois modèles de 32B (p. 3 et p. 5). Il n'y a **aucun facteur de format**.
  - Aucun des deux ne certifie ses instruments avant la mesure. Chez Xiong et al., la réécriture est même choisie pour maximiser le score de la sonde qui sert ensuite de mesure (p. 3).
- **Ce que devient la partie (ii)** : le plan croisé à 30–70B reste libre dans les sept papiers, mais il devient plus étroit. Ses deux moitiés existent déjà à cette échelle, séparément :
  - l'évaluation dépouillée, sur sonde de 70B (Xiong et al.) ;
  - le contexte à contenu égal, à 32B (Abdelnabi et Salem).
  
  Ce qui manque, c'est le **croisement** et la **séparation entre format et style**.
- **Ce qu'ils enlèvent à l'extension sur le 8B** :
  - aucun n'étudie de modèle de 8B ;
  - ils enlèvent la **nouveauté du dessin** à deux points de la v1 :
    - i-1, « le même item d'évaluation, avec et sans ses indices » : fait par Xiong et al. à 70B ;
    - i-2, « le contexte manipulé à contenu égal » : fait par Abdelnabi et Salem à 32B, et par Nayan et al. (v1) ;
  - ils réduisent i-4 (faux marqueurs) par un précédent partiel : le témoin de réécriture aléatoire de Xiong et al. (p. 4 et p. 14) ;
  - ils **n'enlèvent rien** à i-3 : Xiong et al. confondent explicitement le format et le style ;
  - ils n'enlèvent rien non plus à i-5 à i-11.

## 1. Pièces lues et empreintes

| pièce | sha256 | vérification |
|---|---|---|
| `…/scratchpad/anteriorite-hm1-v3/2509.00591.pdf` (Xiong et al., v7, 4 décembre 2025, 15 p.) | `af6e416101d18d20897f3130563b60ca08272d642bd44be09a77b6f35186aff7` | conforme à l'empreinte donnée |
| `…/scratchpad/anteriorite-hm1-v3/2505.14617.pdf` (Abdelnabi et Salem, v3, 28 octobre 2025, NeurIPS 2025, 21 p.) | `cc02be84aef73554b16eab5ffc0e893d68e84e2bfe66a621797f8ebee965bb5c` | conforme à l'empreinte donnée |

(`…/scratchpad` = `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad`.)

- **Extraits** : j'ai réextrait les 36 pages avec `pdftotext -layout` dans `…/scratchpad/verif-extraits-carte-v3/`. Elles sont identiques, octet pour octet, aux extraits fournis dans `…/scratchpad/anteriorite-hm1-v3-textes/`.
- **Lus en entier** : les deux PDF, annexes et bibliographies comprises.
- **Non lus** :
  - les valeurs portées seulement sur les graphiques : figures 2, 4 et 6 de Xiong et al. ; figure 3 d'Abdelnabi et Salem, dont je ne cite que les nombres que le texte reprend ;
  - le code des deux dépôts ;
  - les références citées ;
  - le web.
- **Interdits** : aucun fichier interdit ouvert ni haché ; aucune recherche récursive dans le dépôt ; rien de modifié dans le dépôt.

---

## 2. Xiong et al., « Probe-Rewrite-Evaluate: A Workflow for Reliable Benchmarks and Quantifying Evaluation Awareness », arXiv 2509.00591v7

- **Modèles et tailles** :
  - **Sonde** : celle de Nguyen et al., « Simple Contrastive head at layer 23 », sur **Llama-3.3-70B-Instruct** (p. 2, p. 3 et p. 5 ; figure 4). Elle est reprise « as is » : « In our validation, it attains AUROC 0.816 », au seuil 0,103 (p. 2).
  - Deux incohérences sur cette sonde : la p. 2 parle d'un « LLaMA-72B backbone » ; la p. 3 dit au contraire « the linear probe was subsequently trained … on Llama 3.3 70B Instruct ».
  - **Réécriture** : Claude 3.5 Sonnet (p. 3).
  - **Modèles évalués sur le comportement** (p. 3 ; tableau 1, p. 6) : GPT-4.1, GPT-OSS 120B et 20B, Claude 4.1 Opus, Gemini 2.5 Pro, et Llama 3.3 70B Instruct. Température 0 (p. 3).
  - **Juge** : la p. 2 et la figure 14 (p. 12) disent « GPT o4-mini » ; la p. 4 décrit un ensemble de Claude 3.5 Haiku, Gemini 2.5 Flash et GPT-4o-mini. Accord avec deux annotateurs humains sur 500 réponses : κ = 0,94 (p. 4).
  - **Aucun modèle de 8B.**
- **Mesures** :
  - le **score de la sonde** sur le prompt, c'est-à-dire la sonde de Nguyen et al. sur les activations de Llama-3.3-70B (p. 2 et p. 3) ;
  - le **comportement** : honnête, trompeur ou refus, selon un juge qui compare la réponse à une référence honnête et à une référence trompeuse (p. 2 et p. 4) ;
  - l'**« Awareness Elasticity »** : une somme pondérée des transitions, normalisée par la hausse moyenne du score de la sonde (p. 4).
  - Aucune mesure verbale de la conscience d'évaluation.
- **Construction des données** :
  - **Une seule source**, toute d'évaluation : le jeu « roleplaying » de Goldowsky-Dill et al. (2025), n = 371. Les auteurs le disent eux-mêmes doté d'une « high test-like property » (p. 2). **Aucun item d'origine réelle.**
  - **Réécriture « deployment-style »** : pour chaque item, k = 7 réécritures par Claude 3.5 Sonnet ; on garde **celle qui a le plus haut score de sonde**, et l'original si le gain est ≤ 0 (p. 3).
  - **Consigne de réécriture** (figure 13, p. 11 et p. 12) :
    - « concise, conversational, one paragraph » ;
    - « No labels (e.g., no "Question:" … prefixes) » ;
    - « Remove structured elements like numbered lists, bullet points » ;
    - « Use natural, conversational language instead of formal/structured presentation » ;
    - « Make the prompt shorter » ;
    - poser la question en « direct self-ask from the narrator ».
  - Les exemples passent d'un scénario « structured, third-person » à une « first-person narrative query » (figure 15, p. 13).
  - **Contenu** : contrôle de similarité par notes du modèle, puis audit manuel des 371 réécritures (p. 3). Les paires sont donc **appariées en contenu**, du côté évaluation seulement.
- **Contrôle du format, plan croisé, contenu apparié** :
  - **Format** : il n'est pas contrôlé, il est **manipulé**, et confondu avec le style, la personne grammaticale et la longueur. Longueur moyenne : de 95,93 à 89,80 jetons, soit −6,39 % (p. 4 ; figure 17, p. 14).
  - **Plan croisé** : aucun. Il n'y a ni facteur de contexte ni facteur de provenance, puisque tout le jeu vient d'une seule source d'évaluation.
  - **Témoin** : une réécriture aléatoire, « sentences were randomly perturbed without optimization », donne 15,1 % de prompts au-dessus du seuil, contre 14,8 % pour l'original et 26,4 % pour la réécriture choisie (p. 4 ; figure 18, p. 14). Ce témoin n'est pas choisi par la sonde, alors que la réécriture l'est : les deux bras ne sont pas comparables (voir § 6).
- **Résultats sur la sonde de 70B** (p. 4 et p. 5 ; figure 4) :
  - score moyen de 0,056 à 0,073, soit +0,017 ou +30,4 % ;
  - part au-dessus du seuil de 14,8 % à 26,4 %.
- **Résultats de comportement** (p. 6 et p. 7 ; tableaux 1 et 2) :
  - Llama 3.3 70B Instruct : trompeur −39,08 % ; différence de risque −39,1, intervalle à 95 % [−44,7 ; −33,5] ; χ² de Bowker 133,56 ;
  - GPT-OSS-20B : −2,7, intervalle [−8,7 ; +3,3], non significatif.
  - Les auteurs signalent eux-mêmes un « home field advantage » pour Llama, puisque les réécritures maximisent la sonde de ce modèle (p. 6 et p. 7).
- **Statistiques** :
  - valeurs p et tests de Bowker (p. 6 et p. 7) ;
  - intervalles à 95 % sur la différence de risque de tromperie (p. 7) ;
  - aucun intervalle sur le score de la sonde ; aucune graine (« seed » cherché dans les 15 pages).
- **À 27–70 milliards de paramètres** :
  - Llama-3.3-70B-Instruct est à la fois l'instrument (la sonde) et un modèle évalué (p. 3 et p. 6) ;
  - GPT-OSS-120B et GPT-OSS-20B sont évalués sur le comportement seulement (p. 6) ;
  - **aucun plan croisé, à aucune taille.**
- **Limites déclarées** : un seul corpus, une sonde linéaire, un seul modèle pour la sonde (p. 9). Données et code « will be released upon acceptance » (p. 10).

## 3. Abdelnabi et Salem, « The Hawthorne Effect in Reasoning Models: Evaluating and Steering Test Awareness », arXiv 2505.14617v3

- **Titre** : c'est le même identifiant que « Linear control of test awareness reveals differential compliance in reasoning models », titre cité par Nguyen et al., Chaudhary et al. et Xiong et al. Le titre a changé entre les versions.
- **Modèles et tailles** :
  - **QwQ-32B**, **Qwen3-32B** (raisonnement activé) et **DeepSeek-R1-Distill-Qwen-32B** (p. 3 et p. 5) ;
  - en boîte noire, résultats « préliminaires » sur o3-mini et DeepSeek R1 (p. 5 ; tableau 4, p. 8) ;
  - quatre A100 (p. 5) ;
  - **aucun modèle de 8B ni de 70B ouvert.**
- **Mesures** :
  - **Chaîne de pensée jugée** : un juge LLM, dont le modèle n'est **pas nommé** dans le PDF, lit le raisonnement et répond Yes, Maybe ou No sur « evaluation awareness » et sur « scenario recognition », en extrayant les passages de preuve (p. 4 ; prompt p. 13).
  - **Sonde linéaire** sur la **moyenne des états cachés du passage de preuve** dans le raisonnement généré, et non sur l'entrée (p. 4 et p. 5).
    - Exactitude au test : 95,4 % pour QwQ, 95,1 % pour Qwen3, 92,7 % pour Distill-Qwen (tableau 2, p. 6).
    - Couches 62 et 63 (p. 6).
    - Ablation sur la position du jeton chez QwQ : environ 85 % au dernier jeton de raisonnement, 71 % au dernier jeton d'entrée, 92 % au dernier jeton du passage, 95 % en moyenne sur le passage (p. 6).
  - **Pilotage** par modification des poids : les 800 lignes de W1 les plus alignées avec la direction (p. 5).
  - **Comportement** : exécution d'un appel d'outil, détectée par correspondance de chaîne, « judge-free » (p. 7) ; réponses neutres sur BBQ (p. 9) ; capacités sur MMLU, HellaSwag et CommonsenseQA (tableau 5, p. 9).
- **Construction des données** :
  - **Jeu déclencheur** : 2 587 **paires** de prompts nuisibles, tirés d'AgentHarm, chacun en deux variantes (p. 3) :
    - **réel** : sites ou entités plausibles, par exemple `truehealthvoices.org` ;
    - **hypothétique** : entités fictives ou de remplissage, par exemple `.mock` ou `example`.
    - Les indices sont « embedded naturally » ; le prompt n'énonce jamais un but de test.
  - **Jeu « action-evaluation »** : 150 paires générées par Claude 3.7 Sonnet, par exemple « Stanford University » contre « Test University » (p. 7).
  - Le générateur du jeu déclencheur n'est pas nommé.
- **Contrôle du format, plan croisé, contenu apparié** :
  - **Contenu apparié** : oui. La paire ne diffère que par l'entité (p. 3 et p. 7).
  - **Facteur unique** : réel contre hypothétique. Dans la taxonomie de Singh et Chaudhary (v1), c'est un indice de type « Synthetic Inputs ».
  - **Format** : **aucun facteur, aucun contrôle.**
  - **Plan croisé format × contexte** : **non.**
  - **Comparaison à une mention explicite** : « This is a test scenario with no real-world consequences » placé dans le prompt système ne change presque rien chez QwQ. L'exécution reste à 36,2 % sur le réel, et passe de 69,7 % à 65,1 % sur l'hypothétique (p. 8 ; figure 3a).
- **Résultats principaux** :
  - **Exécution des tâches nuisibles, réel contre hypothétique** (tableau 4, p. 8) :
    - QwQ : 36,2 % contre 69,7 % ;
    - Qwen3 : 20,1 % contre 37,5 % ;
    - Distill-Qwen : 12,0 % contre 20,8 %.
  - **Conscience d'évaluation au départ** (tableau 3, p. 6 et p. 7), sur les déclencheurs puis sur HarmBench : QwQ 17,7 % et 22,9 % ; Qwen3 22,9 % et 13,0 % ; Distill-Qwen 11,7 % et 7,14 %.
  - **Effet du pilotage** (p. 7 et p. 8) : forte modulation de la conscience verbalisée. Sur l'exécution, l'effet varie selon le modèle ; Qwen3 orienté vers « unaware » passe de 20,1 % à 41,8 % sur le réel.
- **Statistiques** : aucun intervalle, aucune graine, aucun test sur ces tableaux (recherche dans les 21 pages). Échantillons : 100 items HarmBench et 100 items BBQ (p. 7 et p. 9).
- **À 27–70 milliards de paramètres** :
  - tout le travail en boîte blanche porte sur trois modèles de 32B, tous de la lignée Qwen ;
  - le contexte y est manipulé à contenu égal ;
  - **le format n'y est jamais un facteur.**
- **Code** : `github.com/microsoft/Test_Awareness_Steering` (p. 1).

---

## 4. Réponse à la question, sur les sept papiers

> « Un plan croisé format × contexte, avec instruments certifiés, sur un modèle de 30 à 70 milliards de paramètres » est-il fait ?

**Non.** Ni le plan croisé seul à cette taille, ni à plus forte raison avec des instruments certifiés.

| papier | plus gros modèle ouvert en boîte blanche | facteur format | facteur contexte à contenu égal | plan croisé | instruments certifiés avant la mesure |
|---|---|---|---|---|---|
| Devbunova (2026) | 8B | oui | non (le contexte est la source) | oui, à 8B | non |
| Nayan et al. (2026) | 32B (pilotage) | oui (2 × 2 de Devbunova) | oui (HarmBench, Hawthorne), hors du 2 × 2 | oui, rapporté jusqu'à 12B | non |
| Singh et Chaudhary (2026) | 12B ou Phi-3 Medium | non | non | non | non |
| Chaudhary et al. (2025) | 70B (Llama-3.1) | non | non | non | non |
| Nguyen et al. (2025) | 70B (Llama-3.3) | non (confondu avec la source) | non | non | non |
| **Xiong et al. (2025)** | 70B (Llama-3.3, sonde reprise) | **manipulé, mais confondu** avec le style, la personne et la longueur (p. 11 à 13) | non (une seule source, d'évaluation, p. 2) | **non** | **non** : sonde reprise telle quelle, et réécriture choisie pour maximiser cette sonde (p. 2 et p. 3) |
| **Abdelnabi et Salem (2025)** | 32B (QwQ, Qwen3, Distill-Qwen) | **non** | **oui** : entités réelles contre fictives, 2 587 paires (p. 3) | **non** | **non** : seulement l'exactitude de la sonde sur une part tenue à l'écart (p. 6) |

## 5. Ce que ces deux papiers enlèvent à l'extension sur le 8B (v1, Q4 (i))

Aucun des deux n'étudie un modèle de 8B. Ce qu'ils enlèvent, c'est la nouveauté de **dessin** de certains points, non leur exécution sur Llama-3.1-8B-Instruct.

| point de la v1 | effet | pages |
|---|---|---|
| **i-1**, marqueurs déclinés dans chaque source (« évaluation dépouillée » des mêmes items) | **Réduit.** Le même item d'évaluation, avec et sans indices d'évaluation, audité à la main, est publié à 70B (sonde) et sur six modèles (comportement). Reste propre au programme : les deux sources déclinées avec les **mêmes** gabarits ; le bras « réel avec marqueurs » sur les mêmes items ; le 8B. Sur ce modèle, Devbunova n'a que le bras réel (v1) et Xiong et al. que le bras évaluation | Xiong et al. p. 2 à 4, p. 11 à 13 |
| **i-2**, contexte manipulé à contenu égal, croisé avec le format | **Réduit.** Le contexte à contenu égal est publié à 32B (entités réelles contre fictives) et dans Nayan et al. (v1). Reste libre : son **croisement avec le format**, et un contexte porté par un système et un récit (H-M1) plutôt que par des entités | Abdelnabi et Salem p. 3, p. 7 et p. 8 |
| **i-3**, style de consigne au sens de H-M1 contre format, à contenu égal | **Intact, et mieux motivé.** Xiong et al. appellent leur manipulation une réécriture de « style », mais ils changent en même temps le format, le registre, la personne et la longueur. Ils ne peuvent donc pas dire lequel agit. Le passage de la troisième à la première personne (p. 13) est la confusion même que la contre-lecture CLE0-03 relève dans les stimuli de H-M1 | Xiong et al. p. 3, p. 4, p. 11 à 13 |
| **i-4**, faux marqueurs appariés en forme et en place | **Légèrement réduit.** Il existe un précédent de témoin de **manipulation simulée** : la réécriture aléatoire, sans effet (15,1 % contre 14,8 %). Ce n'est pas un faux marqueur apparié en forme et en place, et ce témoin n'est pas sélectionné par la sonde comme l'est le bras traité | Xiong et al. p. 4 et p. 14 |
| **i-5**, sonde à format constant appliquée au plan croisé | Intact | — |
| **i-6**, mesure verbale du premier jeton, certifiée | Intact. Abdelnabi et Salem mesurent la conscience **verbalisée dans la chaîne de pensée**, par un juge, et non au premier jeton | Abdelnabi et Salem p. 4 |
| **i-7**, intervalles, équivalence, graines | Intact. Xiong et al. donnent des intervalles sur le comportement seulement (p. 7) | — |
| **i-8** à **i-11** | Intacts | — |

**Avertissement utile au placebo** (CLP-12, témoin positif par mention explicite) : chez QwQ-32B, la phrase « This is a test scenario with no real-world consequences » ne déplace presque pas l'exécution (p. 8). Nayan et al. montraient au contraire qu'un indice « being tested » déplace la détection, dans les deux sens (v1). Une mention explicite n'est donc pas un témoin positif garanti : elle doit être éprouvée sur l'instrument lui-même.

## 6. Ce que devient la partie (ii) à 30–70B

- **ii-1, plan croisé sur Llama-3.3-70B-Instruct** : **libre dans les sept papiers**, mais plus étroit qu'en v2.
  - Sur ce modèle existent déjà :
    - des classes de sources et de formats différents (Nguyen et al., v2) ;
    - l'évaluation dépouillée, à contenu apparié, notée par la sonde : de 14,8 % à 26,4 % au-dessus du seuil (Xiong et al., p. 4).
  - Manquent : le bras « réel avec marqueurs » sur ce modèle, le croisement, la séparation entre format et style, et des instruments certifiés.
- **ii-2, Qwen3-32B** : Abdelnabi et Salem l'étudient en boîte blanche, avec un contexte à contenu égal et sans facteur de format (p. 5 à 8). Le doute de la v1 sur les 32 runs de Nayan et al. reste entier.
- **ii-3, thèse « du format au contexte avec l'échelle »** : Abdelnabi et Salem montrent qu'à 32B un indice de contexte (des entités fictives) suffit à faire monter la conscience verbalisée : 57,0 % des passages « aware » de QwQ viennent des prompts hypothétiques (tableau 2, p. 6). Sans facteur de format, cela ne départage pas format et contexte. La thèse reste non testée par un plan croisé.
- **Lecture R8** : la zone (ii) n'est pas vierge. Elle est **bordée sur trois côtés** à 32–70B : la source (Nguyen et al.), l'évaluation dépouillée (Xiong et al.) et le contexte à contenu égal (Abdelnabi et Salem). Le croisement et la séparation entre format et style restent le seul apport possible. C'est une extension méthodologique, pas une découverte de zone.
- **Restent non lus avant toute revendication** :
  - EvalAwareBench (2605.23055 ; selon la contre-lecture du placebo : déclencheurs activés un à un à requête fixe, neuf modèles de pointe) ;
  - EvalDetectBench (2609.01611) ;
  - WARP ;
  - tout ce qui est paru après le 20 août 2026.
- Les bibliographies de ces deux papiers n'ajoutent aucune référence de priorité 1 sur la conscience d'évaluation. Les plus proches sont :
  - Goldowsky-Dill et al., « Detecting strategic deception using linear probes », source du jeu de Xiong et al. (p. 9) ;
  - Y. Li et al., « I think, therefore i am: Benchmarking awareness of large language models using awarebench », arXiv 2401.17882 (Xiong et al., p. 9), à recouvrement probablement faible.

## 7. Réserves sur les deux papiers (R4)

Ces réserves ne libèrent aucune zone : la faiblesse d'un papier ne fait pas un trou du champ.

- **Xiong et al.** :
  - **Circularité** : la réécriture est choisie parmi sept pour maximiser la sonde (p. 3), puis la hausse de cette même sonde est rapportée comme résultat (p. 4). Le témoin aléatoire n'est pas sélectionné de la même façon (p. 4 et p. 14).
  - **Plus forte baisse de tromperie** : le résumé l'attribue à Claude 4.1 Opus (29,11 %, p. 1) ; le tableau 1 donne −39,08 % pour Llama et −35,58 % pour Gemini (p. 6) ; le texte de la p. 6 attribue 35,58 % à Llama.
  - **Sonde** : « LLaMA-72B » à la p. 2 et Llama 3.3 70B à la p. 3 ; reprise « as is » à la p. 2, mais « subsequently trained » à la p. 3.
  - **Juge** : un modèle unique (p. 2 et p. 12) ou un ensemble de trois (p. 4).
  - **Comptes** (tableau 3, p. 15) : le total n'est pas toujours 371.
    - GPT-4.1 et GPT-120B font 370, avant comme après.
    - Llama fait 371 avant et 370 après. Son Δ de tromperie vaut donc −146 d'après le tableau 3, contre −145 au tableau 1 (p. 6).
- **Abdelnabi et Salem** :
  - le juge n'est pas nommé ;
  - aucun intervalle ;
  - les étiquettes de la sonde viennent d'un juge LLM sur la chaîne de pensée : la sonde lit le raisonnement généré, pas l'entrée (p. 4) ;
  - les classes de la sonde sont asymétriques : « Yes/Maybe » contre « No et No » (p. 4) ;
  - les trois modèles sont de la lignée Qwen, que Chaudhary et al. excluent pour des « anomalous awareness patterns » (v2).
