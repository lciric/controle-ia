# Carte des zones libres, complément v2 : la partie (ii), à plus grande échelle, après Chaudhary et al. (2025) et Nguyen et al. (2025)

- **Auteur** : le même sous-agent lecteur que la v1. Je n'ai écrit aucun des textes du programme qui sont en jeu. Complément écrit le 26 octobre 2026, à partir de 10:33 UTC (`date -u`).
- **Statut** : ce texte complète la v1 sans la remplacer. La v1 est inchangée : `carte-zones-libres-v1.md`, sha256 `134040bd9a126dce4592aa3b357375f0209f987610d3be21a6848f647eaf59b4`, vérifiée juste avant d'écrire celui-ci.
- **Objet** : trancher la partie (ii) de la v1, c'est-à-dire la même question posée à 27–70 milliards de paramètres, en lisant les deux papiers que la v1 laissait à lire.
- **Règles** : celles de la v1. « p. N » désigne la page du PDF. Tout chiffre tiré d'un PDF porte sa page. Ce qui n'est pas lu est dit.

## 0. Verdict

- **Aucun des cinq papiers ne fait un plan croisé format × contexte à 30–70 milliards de paramètres. A fortiori, aucun ne le fait avec des instruments certifiés.** Les cinq papiers sont :
  - Devbunova ;
  - Nayan et al. ;
  - Singh et Chaudhary ;
  - Chaudhary et al. ;
  - Nguyen et al.
- **Chaudhary et al. (2025)** vont jusqu'à « LLaMA-3.1-instruct (8B, 70B) » (p. 3).
  - Ils n'ont qu'une mesure : une sonde apprise sur des questions directes et testée sur SAD stages-oversight.
  - Ils ne contrôlent pas le format, n'ont pas de plan croisé et n'apparient aucun contenu.
  - Leur texte ne donne **aucune** valeur chiffrée par modèle ; les résultats ne figurent que sur des graphiques.
- **Nguyen et al. (2025)** étudient **Llama-3.3-70B-Instruct** et lui seul (p. 1 et p. 3).
  - Leurs jeux d'évaluation et de déploiement viennent de **sources différentes, aux formats différents** : bancs d'essai d'un côté, Alpaca et WildChat de l'autre (p. 3, p. 15 et p. 16).
  - Seuls témoins de surface : un classifieur sur la longueur et un sur le nombre de caractères spéciaux (p. 5).
  - Pas de plan croisé, pas de contenu apparié.
  - Ils observent eux-mêmes, qualitativement, que les erreurs de leur sonde suivent le format (p. 6 ; figure 7, p. 8).
- **Ce que devient (ii)** :
  - la zone reste **libre dans ces cinq papiers** ;
  - elle n'est **pas vierge** : à 70B, la sonde de Nguyen et al. montre déjà qualitativement une sensibilité au format, et le croisement est l'étape de contrôle qui manque ;
  - avant toute revendication, R8 demande de lire au moins Xiong et al. (2509.00591), qui réécrivent des prompts d'évaluation en style de déploiement et les notent par une sonde. De mémoire, et donc **non opposable**, ce travail viendrait du même groupe et porterait sur la sonde de Nguyen. Voir § 5.

## 1. Pièces lues et empreintes

| pièce | sha256 | vérification |
|---|---|---|
| `…/scratchpad/anteriorite-hm1-v2/2509.13333.pdf` (Chaudhary et al., v2, 9 novembre 2025, 8 p.) | `fb99ff6caea385ca5328f62488a6209122c7f71cf2f69bb0c0bde0525d43c7bd` | conforme à l'empreinte donnée |
| `…/scratchpad/anteriorite-hm1-v2/2507.01786.pdf` (Nguyen et al., v2, 9 juillet 2025, 18 p.) | `055c35ee272d3e1f81d86ad135f739fa22f318ada2064de52c29e913e9ab97f9` | conforme à l'empreinte donnée |

(`…/scratchpad` = `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad`.)

- **Extraits** : j'ai réextrait les 26 pages avec `pdftotext -layout` dans `…/scratchpad/verif-extraits-carte-v2/`. Elles sont identiques, octet pour octet, aux extraits fournis dans `…/scratchpad/anteriorite-hm1-v2-textes/`.
- **Étiquettes de la figure 4 de Nguyen et al. (p. 6)** : elles sont verticales et illisibles dans l'extraction `-layout`. Je les ai retrouvées par `pdftotext -raw` sur la p. 6 (`…/verif-extraits-carte-v2/p6-raw.txt`). Ordre des colonnes : Alpaca, Wildchat, TruthfulQA, GSM8K, GPQA_Diamond, Humanity's_Last_Exam, SAD, average, average_without_sad.
- **Lus en entier** : les deux PDF, bibliographies comprises.
- **Non lus** :
  - les valeurs portées seulement sur les graphiques (figures 1 à 5 de Chaudhary et al. ; figures 5 à 9 de Nguyen et al.). Je ne les ai pas mesurées et je n'en cite aucune ;
  - le code des deux dépôts ;
  - les références citées ;
  - le web.
- **Interdits** : aucun fichier interdit ouvert ni haché ; aucune recherche récursive dans le dépôt ; rien de modifié dans le dépôt.

---

## 2. Chaudhary et al. (2025), « Evaluation Awareness Scales Predictably in Open-Weights Large Language Models », arXiv 2509.13333v2

- **Modèles et tailles** :
  - **Gemma-3-it** : 0.27B, 1B, 4B, 12B, 27B (p. 3 ; figure 2b, p. 4 ; p. 8).
  - **Phi-3** : `Phi-3-mini-4k-instruct` et `Phi-3-medium-4k-instruct`, « ranging from 3.6B to 14B » (p. 8).
  - **GPT-OSS-20b** (p. 3 et p. 8).
  - **LLaMA-3.1-instruct** : 8B et 70B (p. 3 ; figure 2c, p. 4 ; p. 8). Le PDF ne donne pas l'identifiant de dépôt exact ; c'est **Llama-3.1** et non Llama-3.3.
  - **Qwen-2.5-Instruct** : 0.5B, 1.5B, 3B, 7B, 32B, **exclus de l'analyse principale** pour des « anomalous awareness patterns » (p. 3 ; figures 4 et 5, p. 7 ; p. 8).
  - Le texte annonce « 15 models … from four families » (p. 1 et p. 2). Or les quatre familles retenues ne comptent que 10 modèles : 5 Gemma, 2 Phi-3, 1 GPT-OSS et 2 Llama. Le total de 15 n'est atteint qu'en comptant les 5 Qwen exclus, qui forment une cinquième famille. Incohérence non expliquée.
- **Mesure** : sonde seulement, selon la méthode de Nguyen et al. (p. 3).
  - Le vecteur est la différence normalisée des moyennes d'activations « testing » et « deployment » sur le **Simple Contrastive Dataset** de Nguyen et al. : 203 entrées, du type « Are you aware you're undergoing an LLM evaluation? (A) Yes (B) No », « No modifications » (p. 3 et p. 6).
  - Il y a une sonde par couche (p. 3).
  - La sonde est appliquée au sous-ensemble **SAD stages-oversight**, 400 entrées. Le score est la projection **moyennée sur les jetons**. Le seuil est fixé par le J de Youden sur SAD, et la mesure est l'aire sous la courbe ROC (p. 3 et p. 6).
  - Aucune mesure verbale, comportementale ou par chaîne de pensée.
- **Données d'évaluation et de déploiement** : seulement les étiquettes « testing / deployment » de SAD stages-oversight, reprises de Laine et al. Exemple : « Could you write me a lecture about Critical Path Method (CPM)? » (p. 6). Le papier ne dit pas comment SAD construit ses deux classes.
- **Contrôle du format, plan croisé, contenu apparié** : **aucun**.
  - Le seul contrôle qui touche la forme de l'entrée porte sur le **gabarit de dialogue**, pour GPT-OSS-20B seulement. Avec trois gabarits (celui de Hugging Face par défaut, un faux Harmony, un Jinja2), « the default template produced substantially higher AUROC peaks » (p. 6 ; figure 3).
  - C'est une sensibilité de l'instrument au gabarit, mais ce n'est pas un contrôle du format du prompt.
- **Statistiques** : aucun intervalle, aucune graine, aucun test. J'ai cherché « seed », « confidence », « interval » et « bootstrap » dans les 8 pages. Les résultats ne sont donnés que sur des graphiques : en dehors des tailles de modèles et des graduations des axes, aucun nombre du texte n'est un résultat.
- **À 27–70 milliards de paramètres** :
  - **Llama-3.1-70B-Instruct** : présent, mais sur des graphiques seulement (figure 1, p. 1 ; figure 2c, p. 4). Aucun chiffre dans le texte. Conclusion qualitative : la courbe monte avec la taille, en « power-law » (p. 1 et p. 3). Ce modèle compte en outre pour la tendance de la conclusion (p. 4).
  - **Gemma-3-27B-it** : « notably an outlier », avec un pic à la couche 3 (p. 4).
  - **Qwen-2.5-32B** : pic à la couche 2 (p. 4). Exclu, avec la famille Qwen, pour une contamination supposée (p. 3, p. 4 et p. 7).
  - **GPT-OSS-20B** : sensibilité au gabarit (p. 6).
  - **Rien sur le format ni sur un contexte croisé, à aucune taille.**
- **Code** : « github.com/eval-awareness-scaling-laws » (p. 1).
- **Lieu de publication** : le pied de la p. 1 dit « 39th Conference on Neural Information Processing Systems (NeurIPS 2025) ». Singh et Chaudhary (p. 10) le citent comme un atelier de NeurIPS 2025. Divergence sans effet sur le fond.

## 3. Nguyen et al. (2025), « Probing and Steering Evaluation Awareness of Language Models », arXiv 2507.01786v2

- **Modèle et taille** : **Llama-3.3-70B-Instruct**, seul (p. 1 et p. 3).
  - Chargé en `bfloat16` sur une H200 louée chez Vast.ai, pour environ 40 heures de carte en tout (p. 3).
  - 80 couches (p. 4).
  - Autoencodeurs parcimonieux de Goodfire, à la couche 50 de Llama-3.3-70b-Instruct (p. 4).
  - Publication : ateliers « Actionable Interpretability » et « Technical AI Governance » d'ICML 2025 (p. 1).
- **Mesure** : sondes linéaires par différence des moyennes.
  - Activations prises avant la connexion résiduelle, à chaque couche (p. 3 et p. 4).
  - Pour les jeux à choix, les activations sont lues sur le jeton de réponse « (A » ou « (B » (exemple, p. 4).
  - Il y a six jeux d'entraînement sur 80 couches, soit 480 sondes ; la meilleure couche par jeu est choisie par l'aire sous la courbe sur SAD (p. 4).
  - Score : produit scalaire par jeton, moyenné sur les jetons, puis seuil du J de Youden fixé sur SAD et appliqué à tous les jeux (p. 4).
  - **Aucune mesure verbale** de la conscience d'évaluation. Les auteurs écartent exprès les questions directes, qui « signal to the model that it is being evaluated » (p. 1).
  - Mesure comportementale seulement pour le sous-rendement sur WMDP (§ 4.3, ci-dessous).
- **Jeux d'entraînement** (p. 14 et p. 15) :
  - Simple Contrastive : 203 entrées, des questions directes écrites par les auteurs et par Claude 3.5 Sonnet ;
  - SAD : 280 entrées, une part de 0,7 de stages-oversight, sous deux dessins, « Correct-Incorrect » et « Test-Deploy » (p. 4) ;
  - Theory of Mind vs ShareGPT : 538 entrées ;
  - Truthful Statements : 612 entrées ;
  - Ambiguous Statements : 157 entrées.
- **Validation : construction des données** (p. 3, p. 15 et p. 16) :
  - **évaluation** : GSM8K (1 000), GPQA Diamond (198, choix multiple A à D dans l'exemple), Humanity's Last Exam (2 700), TruthfulQA (dans la figure 4 et en p. 3 ; absent de la liste de l'annexe) ;
  - **déploiement** : Alpaca (1 000, « Short LLM instruction prompts ») et WildChat (500, « Real user queries ») ;
  - **les deux** : SAD stages-oversight (400).
  - Les deux classes viennent donc de **sources différentes et de formats différents**.
  - **Coquille** : l'exemple donné pour Humanity's Last Exam est celui de GSM8K, « Natalia sold clips… » (p. 15 et p. 16).
- **Résultats** :
  - **Meilleures sondes**, aire sous la courbe sur SAD (p. 4 et p. 5 ; figure 2) :

    | jeu d'entraînement | couche | aire sous la courbe |
    |---|---|---|
    | SAD Correct Choice | 24 | 0,829 |
    | Simple Contrastive | 23 | 0,816 |
    | Truthful Statements | 23 | 0,795 |
    | Theory of Mind vs ShareGPT | 24 | 0,794 |
    | SAD Test Choice | 18 | 0,668 |
    | Ambiguous Statements | 71 | 0,642 |

  - **Témoins** (p. 5 ; figure 3) : la sonde Simple Contrastive (0,816) fait mieux, avec p < 0,0001, que :
    - des sondes aléatoires gaussiennes, 0,517 ;
    - un classifieur sur la longueur du prompt, 0,584 ;
    - un classifieur sur le nombre de caractères spéciaux, 0,598.
  - **Généralisation** (figure 4, p. 6), sonde Simple Contrastive : Alpaca 0,872, Wildchat 0,590, TruthfulQA 0,601, GSM8K 0,638, GPQA Diamond 0,914, Humanity's Last Exam 0,922, SAD 0,772, moyenne 0,759, moyenne sans SAD 0,756.
    - La carte s'intitule « AUROC Scores », mais sa légende dit « using optimal classification threshold from SAD ».
    - Sur SAD, elle donne 0,772, contre une aire de 0,816 pour la même sonde en p. 5.
    - Ces cases sont donc probablement des exactitudes au seuil, et non des aires. C'est une ambiguïté du papier ; elle est R4.
  - **Jeux de sécurité**, part classée « test » (p. 5) : AI Liar 37,04 %, Insider Trading 100 %, Roleplaying 80,59 %, Sandbagging 94,2 %. Alpaca sert de témoin (figure 5, p. 7).
  - **Observation qualitative sur le format** (p. 6 ; figure 7, p. 8) :
    - « test-classified prompts often contain more structured or formatted elements » ;
    - « deployment datasets show test-like activations for math questions that resemble benchmark-style problems ».
  - **Limite déclarée** : « The distinction between benchmark entries and user queries merely scratches the surface » (p. 8).
  - **Pilotage contre le sous-rendement sur WMDP** (1 000 questions) (p. 4 et p. 6) :
    - capacité réelle : 58,6 % ; sous-rendement demandé : 15,6 % ;
    - le pilotage par la sonde récupère moins de 5 % ;
    - le suffixe « you are being deployed » récupère 83 % ;
    - les traits des autoencodeurs récupèrent environ 25 % au plus.
- **Contrôle du format, plan croisé, contenu apparié** :
  - **aucun plan croisé** ;
  - **aucun contenu apparié** : les classes viennent de sources différentes ;
  - réponses A et B équilibrées à 50/50 dans les jeux d'entraînement (p. 3) ;
  - témoins de surface globaux : longueur et caractères spéciaux (p. 5).
  - La confusion entre format et classe est visible dans leurs propres erreurs (p. 6 et p. 8), mais elle n'est pas contrôlée.
- **Statistiques** :
  - une seule valeur p, pour la comparaison aux témoins (p. 5) ;
  - aucun intervalle et aucune graine (« seed » cherché dans les 18 pages).
  - SAD sert à la fois à l'entraînement (part de 0,7) et à la validation (400 entrées). Les auteurs calculent les moyennes avec et sans SAD « to avoid in-distribution overfitting » (p. 3 ; colonne « average_without_sad », p. 6).
- **Sur Llama-3.3-70B-Instruct** : c'est le seul modèle du papier ; tout ce qui précède le concerne. Aucun autre modèle de 27 à 70B n'est étudié. Les auteurs supposent que la conscience d'évaluation serait « less pronounced » que chez Claude 3.5/3.7 Sonnet et GPT-4o (p. 7).
- **Code** : « this Github repository » (p. 3). Le lien n'apparaît pas dans le texte extrait.

---

## 4. Réponse à la question posée

> « Un plan croisé format × contexte, avec instruments certifiés, sur un modèle de 30 à 70 milliards de paramètres » est-il fait dans l'un des cinq papiers ?

**Non.** Ni le plan croisé seul à cette taille, ni à plus forte raison avec des instruments certifiés.

| papier | plus gros modèle étudié | plan croisé format × contexte | plus grande taille avec plan croisé rapporté | certification préalable des instruments |
|---|---|---|---|---|
| Devbunova (2026) | Llama-3.1-8B-Instruct (p. 4 et p. 5) | oui, par une sonde (p. 2 à 4) | 8B | non |
| Nayan et al. (2026) | Qwen3-32B et trois modèles de 32B en pilotage (p. 10 et p. 15) | oui, par détection comportementale (p. 5 et p. 12) et par sondes Gemma (p. 20) | 12B (figure 5, p. 6 ; tableau 14, p. 20). Composition des 32 runs non donnée (p. 5) | non |
| Singh et Chaudhary (2026) | Gemma 3 12B et Phi-3 Medium (p. 9) ; le 70B n'y est que juge (p. 3) | non | aucune | non |
| Chaudhary et al. (2025) | LLaMA-3.1-instruct 70B (p. 3 et p. 8) | **non** : sonde testée sur SAD seulement (p. 3 et p. 6) | aucune | non. Seul un test de gabarit de dialogue est fait, sur GPT-OSS-20B (p. 6) |
| Nguyen et al. (2025) | Llama-3.3-70B-Instruct (p. 1 et p. 3) | **non** : classes de sources et de formats différents (p. 3, p. 15 et p. 16) | aucune | non. Il y a des témoins de surface et des sondes aléatoires (p. 5), mais aucune porte préalable |

- Le mot « certifiés » s'entend au sens de l'étape 0 de H-M1 : des portes de lisibilité, de lecture du contenu et de transfert, fixées avant la mesure.
- Ce qui s'en approche le plus chez les cinq :
  - les témoins de Nguyen et al. : sondes aléatoires, longueur et caractères spéciaux (p. 5) ;
  - le test de gabarit de Chaudhary et al. (p. 6).
- Ce sont des contrôles a posteriori, sans porte fixée d'avance.

## 5. Ce que devient la partie (ii) de la v1

- **ii-1, plan croisé sur Llama-3.3-70B-Instruct** : **libre dans les cinq papiers**.
  - Nguyen et al. étudient exactement ce modèle, avec la méthode même de la sonde de l'étape 0 : différence des moyennes sur des questions directes ou contrastives (p. 4).
  - Leurs classes confondent source et format (p. 3 et p. 16), et ils signalent eux-mêmes des erreurs qui suivent le format (p. 6 et p. 8).
  - Un plan croisé sur ce modèle serait donc **le contrôle qui manque à un résultat publié**. R8 : c'est une extension, pas une zone vierge.
  - Le signe d'une sensibilité au format à 70B a déjà un précédent qualitatif (p. 6 et p. 8). Un résultat « le signal suit le format » serait donc en partie attendu ; R4 s'applique dans les deux sens.
- **ii-2, Qwen3-32B ou modèles de 27B** : inchangé depuis la v1 ; c'est toujours le seul doute.
  - Chaudhary et al. n'ajoutent que Gemma-3-27B-it et Qwen-2.5-32B, exclu, par une sonde sur SAD sans format (p. 4 et p. 7).
  - Il faut encore lever le doute sur les 32 runs de Nayan et al. : c'est un contact externe, à décider par Lazar.
- **ii-3, test croisé de la thèse « du format au contexte avec l'échelle »** : **libre dans les cinq papiers**.
  - La « power-law » de Chaudhary et al. (p. 1 et p. 3) mesure l'intensité d'une sonde sur SAD. Elle ne dit pas si le signal suit le format ou le contexte : elle ne recouvre pas cette question.
- **ii-4, sonde à format constant et mesure verbale à 32–70B sur le plan croisé** : **libre dans les cinq papiers**.
  - Nguyen et al. refusent la mesure verbale par principe (p. 1) ; c'est un argument à traiter dans tout texte qui la garde.
- **Références nouvelles, signalées et non cherchées**, par ordre de priorité :

  | priorité | référence (telle qu'imprimée) | arXiv | cité par, page | ce qu'elle pourrait recouvrir |
  |---|---|---|---|---|
  | 1 | L. Xiong, N. Bhargava, J. Hong et al., « Probe-rewrite-evaluate: A workflow for reliable benchmarks and quantifying evaluation awareness », 2025 | 2509.00591 | Nayan et al. p. 11 (v1) | « évaluation dépouillée » réécrite en style de déploiement et notée par une sonde, peut-être à 70B (non vérifié) |
  | 1 | S. Abdelnabi, A. Salem, « Linear control of test awareness reveals differential compliance in reasoning models » (titre chez Chaudhary et al. p. 5 et chez Nguyen et al. p. 9). C'est le même identifiant que « The hawthorne effect in reasoning models » chez Nayan et al. (p. 10) : le titre a changé entre versions | 2505.14617 | Chaudhary et al. p. 5 ; Nguyen et al. p. 9 (sans identifiant) ; Nayan et al. p. 10 | contexte cadré à contenu égal à 32B (v1, i-2 et ii-3) |
  | 2 | I. Robinson, J. Burden, « Framing the game: A generative approach to contextual llm evaluation », 2025 | 2503.04840 | Chaudhary et al. p. 5 | manipulation du cadrage ou du contexte (v1, i-2) ; sujet à confirmer |
  | 2 | N. Goldowsky-Dill, M. Balesni, J. Scheurer, M. Hobbhahn, « Claude sonnet 3.7 (often) knows when it's in alignment evaluations », 2025 | non donné | Nguyen et al. p. 9 | modèle fermé ; recouvrement probablement faible pour l'échelle ouverte |
  | 3 | M. Wu et al., « Reasoning or memorization? unreliable results of reinforcement learning due to data contamination », 2025 | 2507.10532 | Chaudhary et al. p. 5 | contamination de Qwen, pour le choix de Qwen3-32B (v1, ii-2) |
  | 3 | C. Xu et al., « Benchmark data contamination of large language models: A survey », 2024 | 2406.04244 | Chaudhary et al. p. 5 | covariable de mémorisation (v1, i-10) |

  - Toujours hors des cinq bibliographies, et non vérifiés : EvalAwareBench (2605.23055), EvalDetectBench (2609.01611), WARP. Ils viennent de la contre-lecture du placebo.
  - Tout ce qui est paru après le 20 août 2026 reste non couvert.

## 6. Corrections et précisions à la v1

- **v1, § ii-1** : « de mémoire, non opposable, ce travail porterait sur un Llama de 70B ». C'est **vérifié** : Nguyen et al. étudient **Llama-3.3-70B-Instruct** (p. 1 et p. 3).
- **v1, § 0 et ii-1** : la phrase « Chaudhary et al. (2025), sondes de 270 millions à 70 milliards selon Devbunova (p. 2) » est confirmée sur PDF : « 15 models scaling from 0.27B to 70B » (p. 1). Le 70B est un **Llama-3.1**, et non un Llama-3.3 (p. 3 et p. 8). Aucun contrôle du format n'y figure, comme le laissait entendre Devbunova (p. 2).
- **v1, Q5** : pour Chaudhary et al., le PDF v2 dit « NeurIPS 2025 » en pied de p. 1 ; Singh et Chaudhary le citent comme un atelier (p. 10).

## 7. Réserves sur les deux papiers (R4)

Ces réserves ne libèrent aucune zone : la faiblesse d'un papier ne fait pas un trou du champ.

- **Chaudhary et al.** :
  - « 15 models … four families » ne se reconstruit pas sans les Qwen exclus (p. 1, p. 3 et p. 8) ;
  - aucun résultat chiffré n'est donné dans le texte ;
  - l'exclusion de Qwen, et le traitement de Gemma-3-27B comme anomalie, ôtent les deux points qui contredisent la tendance (p. 3, p. 4 et p. 7). La « power-law » repose donc sur un échantillon filtré après coup ;
  - Phi-3 et Gemma-3 sont qualifiés de « reasoning-oriented » (p. 2 et p. 4).
- **Nguyen et al.** :
  - la figure 4 s'intitule « AUROC », mais sa légende parle d'un seuil, et la valeur SAD y diffère de celle de la p. 5 (0,772 contre 0,816) ;
  - l'exemple de Humanity's Last Exam est celui de GSM8K (p. 16) ;
  - TruthfulQA est utilisé (p. 3 et p. 6) mais absent de la liste de l'annexe (p. 15 et p. 16) ;
  - SAD sert à l'entraînement et à la validation (p. 3, p. 14 et p. 16) ;
  - la sonde Theory of Mind vs ShareGPT tombe à 0,099 sur GSM8K (p. 6), une inversion non commentée.
