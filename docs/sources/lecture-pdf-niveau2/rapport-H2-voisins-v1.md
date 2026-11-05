# Lecture de niveau 2 sur source primaire : quatre articles confrontés à l'énoncé retenu de H2

**Verdict.** Aucune des quatre sources n'occupe l'énoncé retenu de H2 en entier. Chacune en occupe des morceaux, dans un autre cadre : un modèle attaqué par un utilisateur, un agent qui échoue, un robot, ou un observateur textuel. Restent libres dans ces sources :
- la garantie toujours valide au sens des processus e ;
- le régime défini par un moniteur par action calibré à 1 % de faux positifs (le régime qualitatif « chaque pas bénin » est, lui, partiellement occupé) ;
- le rappel qui croît avec l'horizon dans ce régime ;
- la lecture d'un contexte privé caché.

## En-tête

- Lecteur : sous-agent neuf ; n'a rien écrit de ce qu'il vérifie. Règles appliquées : R7 (vérification sur PDF empreinté, page citée) et R8 (ce que les sources occupent, pas ce que le champ laisse libre).
- Date : 2026-10-06. Lecture commencée à 13 h 48 UTC, rapport arrêté à 14 h 11 UTC.
- PDF lus en entier, annexes et références comprises (90 pages), depuis `/home/user/controle-ia/docs/sources/pdf/`, en lecture seule. Rien n'a été modifié dans `/home/user/controle-ia`.

| fichier | pages | empreinte sha256 attendue et constatée (identiques) |
|---|---|---|
| 2604.28129v1.pdf | 24 | f656c9b7e7fbd5d6c70555f825f67cd89b08b0fa746ec0efa895dd64e0f81cb5 |
| 2604.19775v2.pdf | 12 | f3abefb4be525c80df9bdf78992ba4f7591819db22952e21b57438069cfd37ac |
| 2510.09459v2.pdf | 33 | df815e61dc535ff248b020b151c7b94d7921fa8cca21e5041899a7a165e8a597 |
| 2506.10949v2.pdf | 21 | ce51b7f5e263e2a78cb934b4d7cc135ba18335b713fe0b716f781738d67ead66 |

**Méthode.**
- Extraction de référence : `pdftotext -layout`, page par page, dans `extraits/<identifiant>/pNN.txt`. La page citée est le rang de la page dans le fichier PDF ; pour ces quatre articles, elle coïncide avec le numéro imprimé.
- Pour les mises en page à deux colonnes, la même extraction `-layout` est faite par demi-page (`extraits-colonnes/`). Une extraction en ordre de lecture (`lecture/`) a servi à la lecture courante seulement.
- Les liens hypertextes intégrés aux PDF ont été relevés par `scripts/liens_uri.py`.
- Chaque citation de ce rapport est contrôlée par `scripts/controle_citations.py` (voir la dernière section).

**Conventions.**
- Verdicts par composante : « occupé », « partiellement », « libre dans cette source ». Une limitation d'un article n'est jamais lue comme un trou du champ (règle R8).
- Nature d'un chiffre : « auteurs » = imprimé dans le texte ou un tableau ; « figure » = lu sur une figure ; « calcul » = reconstruction du lecteur.
- « Lecture du vérificateur » signale une inférence du lecteur, non une affirmation des auteurs.

**Sigles présents dans les citations anglaises (développés ici une fois).**
- Taux et métriques :
  - FP : faux positif. FPR : taux de faux positifs. TPR : taux de vrais positifs. TNR : taux de vrais négatifs.
  - AUROC : aire sous la courbe ROC (caractéristique de fonctionnement du récepteur). PR-AUC : aire sous la courbe précision-rappel.
  - F1 : moyenne harmonique de la précision et du rappel. DSR : taux de défense réussie, c'est-à-dire le rappel.
  - DT : temps de détection normalisé par la longueur maximale d'épisode. TWA : exactitude pondérée par le pas (un vrai positif compte 1 − DT).
  - pp : point de pourcentage.
- Méthodes et notions :
  - LLM : grand modèle de langage. LAD : nom de la méthode de Kulkarni. Padv : probabilité adversariale estimée à un tour.
  - CP : prédiction conforme (« CP band » = bande conforme ; « CP constant » = seuil conforme constant). NCM : mesure de non-conformité.
  - ID / OOD (ou iD) : dans la distribution / hors distribution. RND-OE : distillation de réseau aléatoire sur les plongements d'observations. ACE : entropie des segments d'actions.
  - ICL : exemples donnés dans l'invite. QA : questions-réponses. HACCA : cadre de menace « agents cyber hautement autonomes ».
  - θ, δ, ϵ : seuil, taux de fausses alarmes visé, niveau de signification. DID et Dc : données d'entraînement et de calibrage de FIPER.

---

## 1. Kulkarni — 2604.28129v1

### Identité

| élément | réponse | page | citation exacte (anglais, mot pour mot) |
|---|---|---|---|
| titre | Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection | 1 | « Adaptive Probing of LLM Activations for Multi-Turn Attack Detection » |
| auteur | Prashant Kulkarni, seul auteur (Mountain View, Californie) | 1 | « Prashant Kulkarni » |
| version, date | v1, 30 avril 2026, catégorie cryptographie et sécurité | 1 | « arXiv:2604.28129v1 [cs.CR] 30 Apr 2026 » |
| conférence | aucune indiquée ; code promis « à l'acceptation », lieu de soumission non dit | 8 | « Code will be released upon acceptance. » |
| code, données | données à accès contrôlé. Adresses non imprimées, présentes seulement comme liens intégrés au PDF : huggingface.co/datasets/pskulkarni/lad-multiturn-adversarial et huggingface.co/datasets/pskulkarni/lad-extended-pivoting (non visitées). Code non publié. | 8 | « Datasets with three-phase turn-level labels are available under gated access: core dataset and extended pivoting. » |

### Réponses aux questions

| # | question | verdict ou réponse | page | citation exacte (anglais, mot pour mot) |
|---|---|---|---|---|
| 2 | Que lit le moniteur ? | **Les activations internes du modèle cible**, celui qui converse : flux résiduel d'une couche intermédiaire ou tardive, au dernier jeton, à la fin de chaque message utilisateur, après passage de tout le contexte. Ce n'est ni un observateur séparé ni le texte seul. Mais l'adversaire est l'utilisateur, pas le modèle. Lecture du vérificateur : dans les expériences, les réponses de l'assistant ne sont pas écrites par le modèle sondé (Qwen3-235B pour le synthétique ; vicuna, koala, etc. pour LMSYS). Le texte ne dit nulle part que le modèle sondé régénère ces réponses ; il lit donc une transcription qu'il n'a pas produite. | 3 ; 3 ; 2 ; 4 ; 17 | « The defender has white-box access to the target model’s internal activations and deploys a probe that monitors the residual stream in real time. » « For multi-turn conversations, we extract at each user turn boundary after feeding the cumulative context via the model’s chat template » « We consider an attacker who interacts with an LLM-powered system across one or more conversation turns. » « Synthetic multi-turn. 1,125 training + 797 evaluation conversations generated by Qwen3-235B across 6 attack categories mapped to HACCA tactics » « Models represented: vicuna-13b (47%), koala-13b (6%), alpaca-13b (5%), and 22 others. » |
| 3 | Agrégation dans le temps ; sur combien de pas ? | **Classifieur par tour** (arbres de décision boostés, bibliothèque XGBoost). Il reçoit l'activation du tour et cinq scalaires de trajectoire, dont la **dérive cumulée** : somme des normes des différences d'activations successives, donc additive sur les tours. La conversation est signalée si un tour au moins dépasse θ = 0,5 (règle « n'importe quel tour »). Chaque tour est classé indépendamment. Il existe aussi une base non supervisée : un seuil sur la seule dérive cumulée. Horizon : 10 à 14 tours (synthétique standard), 14 à 20 (pivot prolongé), 7 tours et plus (LMSYS, strates jusqu'à 21 et plus). | 3 ; 12 ; 4 ; 18 ; 21 ; 15 ; 15 ; 4 | « At each turn t, the probe classifies the conversation trajectory up to t—not the turn in isolation—using the current activation and its relationship to all prior activations (drift, cumulative path length, acceleration). » « Cumulative drift: total path length through activation space » « A conversation is flagged if any turn satisfies Padv (t) > θ (θ=0.5, no tuning). » « Algorithm 2 (p. 18) shows the streaming inference procedure, where each new user turn is evaluated independently » « Cum. drift threshold 99–100% 29–62% — » « Target turns: 10-14 (5-7 benign, 2-3 pivoting, 2-3 adversarial) » « Total conversation should be 14-20 turns » « filtered for English and 7+ user turns » |
| 4 | Garantie statistique ? | **Aucune** : ni processus e, ni martingale, ni prédiction conforme. Le seuil est fixé à 0,5 sans réglage. Les sondes sont supervisées, entraînées avec des exemples d'attaque étiquetés en trois phases, modèle par modèle, sur la distribution de déploiement. Termes cherchés sans succès : conformal, martingale, e-value, e-process, Ville, anytime, sequential, CUSUM, SPRT, guarantee. La façon de fixer le seuil de la base non supervisée « Cum. drift threshold » n'est pas décrite : non trouvé. | 14 ; 8 ; 7 | « θ=0.5 default cutoff, no threshold tuning on held-out data. » « deployment requires per-model probes trained on representative data from the deployment distribution. » « Label ablation: Binary conversation-level labels produce 50–59% FP; three-phase turn-level labels reduce FP to 0.5–2%—a necessary condition for deployment. » |
| 5 | Régime adverse : chaque pas sous un seuil par pas ? Seuil à taux de faux positifs fixé ? | **Partiellement.** Les tours de « pivot » sont conçus pour être niables un à un, et la détection précoce vise la phase où aucun tour n'est adversarial isolément. Mais chaque attaque finit par des tours ouvertement adversariaux. Aucun moniteur par tour n'est calibré à un taux de faux positifs fixé (ni 1 %, ni autre) : le seuil 0,5 n'est pas réglé. | 1 ; 15 ; 15 ; 11 | « but text-level defenses miss covert attacks where individual turns appear benign. » « 4-6 turns where the user’s questions become progressively more boundary-testing but each one is individually deniable. » « Three-phase labels train the probe to recognize the trajectory toward an attack during the pivoting phase, before any individual turn is adversarial in isolation. » « adversarial (overt harmful request or compliance) » |
| 6 | La détection croît-elle avec l'horizon ? | **En partie, et contredit sur données réelles.** (a) Synthétique : la détection précoce (avant le premier tour adversarial) croît avec le nombre de tours de pivot, de 10 % (1 tour) à plus de 60 % (3 et plus). Elle passe de 22–26 % (1,9 tour de pivot en moyenne) à 66–83 % (6,7 tours). (b) Réel (LMSYS) : la détection baisse pour les conversations longues : 53–58 % jusqu'à 10 tours, 55–66 % de 11 à 20, 31–42 % à 21 et plus. | 20 ; 5 ; 5 ; 19 ; 19 | « rising steadily from 10% at 1 pivoting turn to over 60% at 3+. » « Early detection—flagging attacks before the first adversarial turn—improves dramatically: 66–83% of attacks detected early (vs 22–26% original), with +1.2–1.6 turns of mean lead time (fig. 5). » « The relationship is near-monotonic across pivoting turn counts » « Short conversations (≤10 turns): 53–58% detection, 4.6–5.7% FP. Medium (11–20): 55–66%, 3.9–6.1%. » « Long (21+): 31–42%, 0–2.9%. Counterintuitively, longer LMSYS conversations are harder to detect, likely because long benign conversations accumulate more trajectory noise, making adversarial drift less distinctive. » |
| 7 | Contexte privé (raisonnement caché) lu ? | **Non trouvé.** Les modèles sondés (Gemma 3 27B, Mistral 3.1 24B, Qwen 2.5 32B, Llama 3.1 70B) sont lus au dernier jeton du contexte, à la fin de chaque message utilisateur. Aucune mention de raisonnement caché ni de chaîne de pensée. Termes cherchés : reasoning, chain-of-thought, thought, hidden, private, scratchpad (seules occurrences : « hidden state », « hidden dimension »). | 3 | « For multi-turn conversations, we extract at each user turn boundary after feeding the cumulative context via the model’s chat template » |
| 8 | Chiffres utilisables | Voir le tableau suivant. Aucun rappel à 1 % de faux positifs n'est rapporté : non trouvé. | — | — |
| 9.1 | H2 : sondes de l'agent qui agit | **partiellement** : activations internes du modèle en conversation, pas d'un observateur. Mais l'adversaire est l'utilisateur, et le modèle sondé lit une transcription qu'il n'a pas produite (lecture du vérificateur, ligne 2). | 3 ; 2 | « The defender has white-box access to the target model’s internal activations » « We consider an attacker who interacts with an LLM-powered system across one or more conversation turns. » |
| 9.2 | H2 : accumulation additive | **partiellement** : la dérive cumulée est une somme additive sur les tours. Mais elle somme des normes de différences d'activations, pas des scores de sondes. Elle sert de variable d'un classifieur supervisé et de seuil non supervisé (99–100 % de détection, 29–62 % de faux positifs). La décision finale n'est pas une accumulation. | 12 ; 21 | « Cumulative drift: total path length through activation space » « Cum. drift threshold 99–100% 29–62% — » |
| 9.3 | H2 : toujours valide | **libre dans cette source** | 4 | « A conversation is flagged if any turn satisfies Padv (t) > θ (θ=0.5, no tuning). » |
| 9.4 | H2 : sous le seuil par action à 1 % | **partiellement** pour le régime : tours de pivot niables un à un. **libre dans cette source** pour le seuil par action calibré à 1 % ; de plus, les attaques finissent par des tours ouverts. | 15 ; 11 | « each one is individually deniable. » « adversarial (overt harmful request or compliance) » |
| 9.5 | H2 : rappel croissant avec l'horizon | **partiellement** : la détection précoce croît avec la durée du pivot (synthétique). Contre-exemple sur données réelles : les conversations longues sont plus dures. | 20 ; 19 | « rising steadily from 10% at 1 pivoting turn to over 60% at 3+. » « Counterintuitively, longer LMSYS conversations are harder to detect » |
| 9.6 | H2 : calibrage sans exemple de sabotage | **libre dans cette source** : sondes supervisées avec attaques, étiquettes en trois phases jugées indispensables. Le calibrage de la base non supervisée n'est pas décrit. | 7 | « three-phase turn-level labels reduce FP to 0.5–2%—a necessary condition for deployment. » |
| 9.7 | H2 : contexte privé | **libre dans cette source** : lecture à la fin des messages utilisateur, aucun raisonnement caché | 3 | « we extract at each user turn boundary » |
| R1 | Réserve | La robustesse n'est testée que par suppression simulée de la dérive ; pas d'attaquant qui connaît la sonde. | 8 | « Robustness evaluation (section M) simulates drift suppression but does not test probe-aware generation. » |
| R2 | Réserve | Confondant de longueur reconnu par l'auteur : la position du tour a été retirée des variables. | 3 | « We initially included absolute turn position t as a sixth feature, but ablation (section 5.1) showed removing it improves detection by +1.2pp—it introduces a residual length confound even with absolute indexing. » |

### Chiffres utilisables

| chiffre | valeur | page | nature | citation exacte (anglais, mot pour mot) |
|---|---|---|---|---|
| Détection par conversation, 797 conversations synthétiques retenues, Gemma 3 27B, activation + 5 scalaires | 93,8 % pour 3,5 % de faux positifs (activation seule : 76,2 %) | 4 | auteurs | « scalar-augmented XGBoost lifts conversation-level detection from 76.2% (snapshot, activation only) to 93.8% (+17.6pp) at 3.5% FP. » |
| Détection par conversation, ensemble mixte retenu (1 797 conversations), Qwen 2.5 32B | 89,4 % ; faux positifs 2,4 % par conversation et 2,0 % par tour | 21 | auteurs | « Qwen 2.5 32B 89.4% 2.4% 2.0% » |
| Même ensemble, quatre modèles | détection 85–89 % | 21 | auteurs | « LAD achieves comparable detection (85–89%) with 32× lower FP than Lakera and 16× lower turn-level FPR. » |
| Base non supervisée : seuil sur la dérive cumulée | 99–100 % de détection pour 29–62 % de faux positifs par conversation | 21 | auteurs | « Cum. drift threshold 99–100% 29–62% — » |
| Base : 5 scalaires seuls, sans activations | 87–93 % de détection pour 57–74 % de faux positifs | 7 | auteurs | « scalars alone achieve 87–93% detection but 57–74% FP—activations provide precision » |
| Discrimination par tour sur LMSYS | aire sous la courbe ROC 0,88–0,91 ; aire précision-rappel 0,38–0,44 | 20 | auteurs | « LMSYS AUROC (0.88–0.91) indicates reasonable discrimination but low PR-AUC (0.38–0.44) reflects class imbalance (5% adversarial turns). » |
| Exemple de ligne du tableau 8 (Qwen, LMSYS) | aire ROC 0,907 ; aire précision-rappel 0,467 ; détection 55,3 % pour 5,4 % de faux positifs | 20 | auteurs | « Qwen LMSYS 0.907 0.467 55.3% / 5.4% » |
| Détection sur LMSYS (réel) | 47–71 % | 1 | auteurs | « with detection on real-world LMSYS reaching 47–71% when its distribution is represented in training. » |
| Détection précoce, pivot prolongé | 3 à 4 fois plus (tableau 12 : 22–26 % → 66–83 % ; avance moyenne +0,13 à +0,31 → +1,25 à +1,64 tour) | 21 | auteurs | « Table 12: Extended pivoting: 3–4× improvement in early detection across all models with longer pivoting phases. » |
| Sondes entraînées sur synthétique seul, appliquées à LMSYS | 99,1 % de faux positifs | 6 | auteurs | « Probes trained exclusively on synthetic data fail on real conversations: 99.1% false positive rate on LMSYS-Chat-1M » |
| Rappel à 1 % de faux positifs | non trouvé. Le seuil est fixé à 0,5 ; les points de fonctionnement observés vont de 0,5 % à 6,9 % de faux positifs par conversation selon le modèle et la source (bornes du tableau 8 : Gemma 3 synthétique et Gemma 3 LMSYS) | 20 ; 20 | auteurs | « Synth 0.972 0.893 89.2% / 0.5% » « Gemma 3 LMSYS 0.897 0.479 58.3% / 6.9% » |

### Conséquences pour H2

- **N'occupe pas l'énoncé retenu.** Il n'y a ni garantie toujours valide ni calibrage sur épisodes honnêtes. L'adversaire est un utilisateur, pas l'agent. Les attaques finissent par des tours ouverts. Il n'y a pas de seuil par tour à 1 %, ni de contexte privé.
- **Occupe partiellement quatre composantes.**
  - Lecture des activations du modèle en conversation (p. 3).
  - Somme additive sur les tours, sous forme de dérive cumulée des activations (p. 12, 21).
  - Régime de tours niables un à un, pendant le pivot seulement (p. 15).
  - Détection précoce qui croît avec la durée du pivot, sur données synthétiques (p. 5, 20).
- **À reprendre dans le préenregistrement.**
  - (i) La base « seuil sur la dérive cumulée » : additive, sur activations, sans étiquettes. Elle est à recalibrer sur épisodes honnêtes au même taux de faux positifs.
  - (ii) La longueur des épisodes est un confondant. L'auteur a dû retirer la position du tour (p. 3). Sur données réelles, la détection baisse avec la longueur (p. 19). C'est le signe opposé à la prédiction de H2, dans un cadre voisin (méthode supervisée, règle « n'importe quel tour »).
- **Réserves.**
  - Les chiffres principaux viennent de conversations synthétiques générées par un autre modèle (p. 4, 14).
  - Aucun attaquant ne connaît la sonde (p. 8).

---

## 2. Kaur, Padhi et al. — 2604.19775v2

### Identité

| élément | réponse | page | citation exacte (anglais, mot pour mot) |
|---|---|---|---|
| titre | From Actions to Understanding: Conformal Interpretability of Temporal Concepts in LLM Agents | 1 | « From Actions to Understanding: Conformal Interpretability of Temporal Concepts in LLM Agents » |
| auteurs | Ordre imprimé : Ramneet Kaur et Trilok Padhi (contribution égale), Krishiv Agarwal, Adam D. Cobb, Daniel Elenius, Manoj Acharya, Colin Samplawski, Alexander M. Berenbeim, Nathaniel D. Bastian, Susmit Jha, Ugur Kursuncu, Anirban Roy. Affiliations : Georgia State University, SRI, Académie militaire de West Point, Université de Floride. Les métadonnées du PDF placent Padhi en premier ; l'en-tête imprimé place Kaur en premier. | 1 ; 1 | « Ramneet Kaur* 2 , Trilok Padhi* 1 , Krishiv Agarwal 4 , Adam D. Cobb2 , » « These authors contributed equally » |
| version, date | v2, 1er juillet 2026, catégorie intelligence artificielle | 1 | « arXiv:2604.19775v2 [cs.AI] 1 Jul 2026 » |
| conférence | non indiquée. Pied de page de diffusion publique ; financement de l'agence de recherche de défense américaine et de l'armée de l'air (p. 9). | 1 | « Distribution Statement “A” (Approved for Public Release, Distribution Unlimited). » |
| code, données | non trouvé : aucune adresse dans le texte ; le seul lien intégré est un reste de gabarit (« mailto:email@domain ») | — | — |

### Réponses aux questions

| # | question | verdict ou réponse | page | citation exacte (anglais, mot pour mot) |
|---|---|---|---|---|
| 2 | Que lit le moniteur ? | **Les activations du flux résiduel de l'agent lui-même**, sur les 32 couches, au dernier jeton de la trajectoire jusqu'au pas t. L'agent est Llama-2-7B, affiné de façon supervisée au format ReAct (raisonnement puis action). Des sondes linéaires classent succès ou échec. Ce n'est pas un observateur, ni un moniteur de sécurité : c'est un cadre d'interprétabilité. Le texte ne précise pas si les préfixes sondés sont des déroulés de l'agent ou des trajectoires d'experts : non trouvé. | 3 ; 7 | « We train classifiers (or linear probes) on layer and time-conditioned agent’s activations to distinguish the latent space of success from failure. » « the training set of probes on residual stream activations of all 32 layers on the last token of the entire trajectory till time t. » |
| 3 | Agrégation dans le temps ; sur combien de pas ? | **Aucune.** Une sonde par couche et par pas, résultats rapportés pas par pas (t = 2 à 10). Ni somme, ni maximum, ni règle d'alarme sur l'épisode. Horizon : 10 pas. | 7 ; 8 | « We observe that the trained agent is mostly able to successfully complete the assigned task within 10 timesteps. » « for all timesteps t ∈ {1, 2, . . . , 10} » |
| 4 | Garantie statistique ? | **Conforme, au niveau du pas, pour l'étiquetage et non pour la détection.** Méthode : détection d'anomalies conforme inductive. Elle borne à 10 % (ϵ = 0,1) les erreurs d'étiquetage des récompenses par pas (succès ou échec). La borne est marginale et suppose des échantillons indépendants et identiquement distribués. Le calibrage utilise des pas réussis **et** des pas en échec. Rien de toujours valide (processus e, martingale) : non trouvé. | 6 ; 7 ; 6 ; 5 | « Theorem 1 (Bounded Guarantees on making Labeling Errors). » « We set ϵs = ϵf = 0.1 for labeling step-wise rewards as success or failure all timesteps. » « Given the calibration set of step-wise rewards for both successful and failure steps » « Under the standard i.i.d. assumption that both calibration and test samples are drawn from the same distribution D » |
| 5 | Régime adverse ? | **Aucun** : ni adversaire, ni sabotage. Les échecs sont des hallucinations ou des explorations hors sujet. Pas de seuil par pas à taux de faux positifs fixé. Termes cherchés : adversar, attack, sabotage (aucune occurrence). | 2 | « failure modes such as hallucination or irrelevant exploration. » |
| 6 | La détection croît-elle avec l'horizon ? | **Non.** L'exactitude est rapportée pas par pas, sans tendance croissante. Hors distribution (ScienceWorld, couche 8), elle baisse aux derniers pas : 100, 92, 100, 94, 92, 80, 75, 75, 50 % de t = 2 à t = 10. Sur ALFWorld, elle va de 60 à 95 %. | 7 ; 7 ; 8 | « Table 2. Accuracy(%) of Linear Probes on OOD Test Set of ScienceWorld across Layers and Timesteps. » « 8 100 92 100 94 92 80 75 75 50 » « The accuracy varies from 60% (layer 8 at t = 6 and layer 24 at t = 4) to 95% (at t = 2), and the F1 score varies from 0.56 (layer 24 at t = 4 to 0.95 (at t = 2). » |
| 7 | Contexte privé (raisonnement caché) lu ? | **Partiellement.** La trajectoire lue contient les « pensées » ReAct : le raisonnement en langue naturelle écrit avant chaque action. Mais c'est du texte visible de l'agent, pas un contexte privé caché. | 4 ; 1 | « Here, each step taken by the agent consists of a natural language reasoning trace followed by an executable action. » « the agent’s decision at any step depends not only on the current observation but also on the entire trajectory history with prior reasoning traces, environment responses, and accumulated context. » |
| 8 | Chiffres utilisables | **Aucun chiffre de détection** (ni aire sous la courbe ROC, ni rappel à taux de faux positifs fixé, ni délai) : non trouvé. Seulement l'exactitude et le score F1 par pas. L'article revendique pourtant une détection précoce des échecs. | 1 | « The proposed approach, thus, offers a principled method for early failure detection as well as intervention in LLM-based agents » |
| 9.1 | H2 : sondes de l'agent qui agit | **partiellement** : sondes linéaires sur les activations de l'agent qui agit, mais pour le succès ou l'échec d'un pas, hors sabotage | 3 | « We train classifiers (or linear probes) on layer and time-conditioned agent’s activations » |
| 9.2 | H2 : accumulation additive | **libre dans cette source** (une sonde par pas de temps, sans cumul) | 3 | « We train classifiers (or linear probes) on layer and time-conditioned agent’s activations » |
| 9.3 | H2 : toujours valide | **libre dans cette source** : la garantie conforme porte sur l'étiquetage, pas à pas | 6 | « Theorem 1 (Bounded Guarantees on making Labeling Errors). » |
| 9.4 | H2 : sous le seuil par action à 1 % | **libre dans cette source** (ni adversaire ni seuil par pas) | 2 | « failure modes such as hallucination or irrelevant exploration. » |
| 9.5 | H2 : rappel croissant avec l'horizon | **libre dans cette source** | 7 | « good accuracy in most test cases for OOD set except for one test case (50% at t = 10 for layer 8). » |
| 9.6 | H2 : calibrage sans exemple d'échec | **libre dans cette source** : le calibrage utilise les deux classes, et les sondes sont supervisées | 6 | « Given the calibration set of step-wise rewards for both successful and failure steps » |
| 9.7 | H2 : contexte privé | **partiellement** : pensées ReAct visibles dans la trajectoire lue, pas un contexte caché | 4 | « Here, each step taken by the agent consists of a natural language reasoning trace followed by an executable action. » |
| R1 | Réserve | Lecture du vérificateur : la borne « strictement » annoncée repose sur l'hypothèse d'échantillons indépendants et identiquement distribués, alors que les pas d'une même trajectoire sont dépendants. C'est une limite de l'article, pas un trou du champ. | 6 | « The probability of labeling a successful step-wise reward as failure (or False Negative Rate) is strictly bounded by ϵs » |

### Chiffres utilisables

| chiffre | valeur | page | nature | citation exacte (anglais, mot pour mot) |
|---|---|---|---|---|
| Exactitude des sondes, ScienceWorld, dans la distribution | jusqu'à 100 % dans la plupart des cas | 7 | auteurs | « Probes achieve significantly high accuracy with upto 100% in most test cases for iD set » |
| Exactitude, ScienceWorld, hors distribution, couche 8, t = 10 | 50 % | 7 | auteurs | « good accuracy in most test cases for OOD set except for one test case (50% at t = 10 for layer 8). » |
| Exactitude et F1, ALFWorld | 60–95 % ; 0,56–0,95 | 8 | auteurs | « The accuracy varies from 60% (layer 8 at t = 6 and layer 24 at t = 4) to 95% (at t = 2), and the F1 score varies from 0.56 (layer 24 at t = 4 to 0.95 (at t = 2). » |
| Borne des erreurs d'étiquetage | 10 % | 7 | auteurs | « This strictly bounds both the false negative and false positive labeling errors to 10% [17]. » |
| Pilotage des activations au pas 3 | +1,1 point d'exactitude | 8 | auteurs | « This intervention yields a 1.1% accuracy boost » |

Aucun de ces chiffres n'est une base de détection utilisable pour H2.

### Conséquences pour H2

- **N'occupe pas l'énoncé retenu.** Il n'y a ni accumulation, ni garantie sur la détection, ni adversaire. Le calibrage utilise des échecs. Aucun chiffre de détection n'est rapporté.
- **Occupe partiellement deux composantes.**
  - Sondes sur les activations de l'agent qui agit (p. 3, 7), avec le succès ou l'échec comme objet.
  - Lecture d'un raisonnement, mais visible (pensées ReAct, p. 4).
- L'article montre que l'issue d'un pas est décodable linéairement dans les activations de l'agent. C'est un appui de faisabilité hors régime adverse, pas une base.
- **Aucune base à ajouter**, faute de métrique de détection.

---

## 3. Römer et al., FIPER — 2510.09459v2

### Identité

| élément | réponse | page | citation exacte (anglais, mot pour mot) |
|---|---|---|---|
| titre | Failure Prediction at Runtime for Generative Robot Policies | 1 | « Failure Prediction at Runtime for Generative Robot Policies » |
| auteurs | Ralf Römer et Adrian Kobras (contribution égale), Luca Worbis, Angela P. Schoellig ; Université technique de Munich | 1 ; 1 | « Technical University of Munich, Germany; Learning Systems and Robotics Lab; » « Equal contribution. » |
| version, date | v2, 13 octobre 2025, catégorie robotique | 1 | « arXiv:2510.09459v2 [cs.RO] 13 Oct 2025 » |
| conférence | NeurIPS 2025 (39e conférence sur les systèmes de traitement de l'information neuronale) | 1 | « 39th Conference on Neural Information Processing Systems (NeurIPS 2025). » |
| code, données | site imprimé avec code, données et vidéos (non visité) | 1 | « Code, data and videos are available at tum-lsy.github.io/fiper_website. » |

### Réponses aux questions

| # | question | verdict ou réponse | page | citation exacte (anglais, mot pour mot) |
|---|---|---|---|---|
| 2 | Que lit le moniteur ? | **Ni texte, ni observateur externe.** Il lit deux signaux de la politique qui agit. (i) Un score de nouveauté par distillation de réseau aléatoire, dans l'espace de plongement des observations de la politique elle-même (son encodeur, gelé). (ii) L'entropie des segments d'actions qu'elle échantillonne. Ce ne sont pas des sondes entraînées sur un concept. La politique est robotique (diffusion, appariement de flux), pas un modèle de langage. Les auteurs écartent les moniteurs externes vision-langage. | 1 ; 4 ; 26 | « (i) out-of-distribution (OOD) observations detected via random network distillation in the policy’s embedding space, and (ii) high uncertainty in generated actions measured by a novel action-chunk entropy score. » « we can detect anomalies directly in the policy’s embedding space, which are more indicative of failures than OOD raw observations. » « Several recent works have proposed using VLMs to externally monitor a robot and reason about erroneous behavior [1, 17]. » |
| 3 | Agrégation dans le temps ; sur combien de pas ? | **Somme additive des scores sur une fenêtre glissante** de w pas de politique, w de 1 à 50. Meilleure fenêtre pour FIPER : 25/50 (deux fenêtres ; l'attribution à chaque score n'est pas précisée). L'alarme part au premier pas où les deux sommes dépassent leurs seuils (conjonction « ET »). La somme cumulée sur tout le passé (fenêtre infinie, reprise de STAC, Agia et al.) est aussi testée : plus exacte, mais bien plus lente, et elle reconnaît les échecs surtout par leur plus grande longueur. Horizon : 22 à 120 pas au maximum selon la tâche. | 2 ; 4 ; 28 ; 9 ; 10 ; 22 | « Both scores are calibrated based on a few successful rollouts and aggregated over a sliding window. » « If at any time t, F (τ:t ) = 1, the rollout is flagged as Fail with detection time t. » « 40 15 2 15 1 45 25/50 » « The results shown in Fig. 5 demonstrate that score accumulation can increase accuracy, but at the cost of much slower detection. » « failure rollouts primarily due to their greater length, which naturally leads to a higher cumulative score. » « Max. episode length 75 120 38 70 22 » |
| 4 | Garantie statistique ? | **Prédiction conforme sur données fonctionnelles, au niveau de l'épisode.** Elle borne par δ la probabilité de fausse alarme, à n'importe quel pas, sur un nouvel épisode réussi dans la distribution, jusqu'à un horizon fini (proposition 1). La borne est donc uniforme sur les pas d'un horizon fini. Elle s'obtient par le maximum sur l'épisode (seuil constant) ou par une bande. Ce n'est ni un processus e ni une martingale (aucune occurrence de martingale, e-value, anytime, Ville). Le calibrage utilise des épisodes réussis seulement, indépendants et identiquement distribués. Limites écrites par les auteurs : (a) la proposition ne couvre pas le seuil variable dans le temps, celui des résultats principaux ; (b) elle exige des données d'entraînement et de calibrage disjointes, ce que les expériences ne font pas ; (c) le taux visé n'est pas atteint hors distribution. | 6 ; 1 ; 6 ; 28 ; 6 ; 30 | « the probability that the failure predictor (7) of FIPER flags a new successful ID rollout τ ∼ qπ of length T ′ ≤ T as Fail at any policy timestep t ≤ T ′ satisfies the upper bound » « Both failure prediction scores are calibrated using a small set of successful rollouts via conformal prediction. » « Proposition 1 also applies to the CP constant but not to the time-varying threshold. » « time-var. CP constant CP constant CP constant CP constant time-var. time-var. » « However, setting DID = Dc worked well in our experiments, so we collect only one rollout dataset. » « The fact that neither a constant threshold nor a one-sided CP band achieves the desired FPR exactly matches the results reported in prior works [1, 75] and stems from the fact that Propositions 2 and 3 only hold for ID rollouts, whereas we also evaluate on OOD scenarios. » |
| 5 | Régime adverse ? Seuil à taux de faux positifs fixé ? | **Aucun adversaire** : les échecs viennent de décalages de distribution et d'erreurs qui s'enchaînent. Le taux visé δ porte sur l'épisode, pas sur le pas. Les résultats sont moyennés sur 1 − δ de 0,90 à 0,99. Il n'y a pas de moniteur par pas calibré à 1 %. Décider sur le seul pas courant (fenêtre de 1) donne beaucoup de fausses alarmes. | 18 ; 7 ; 10 | « δ: Desired FPR » « we average all results over 1 − δ ∈ {0.9, 0.91, . . . , 0.99}. » « As shown in Fig. 6, this leads to a very low TNR, i.e., flagging most successful rollouts as Fail, while only slightly reducing DT. » |
| 6 | La détection croît-elle avec l'horizon ? | **Non rapporté en fonction de l'horizon.** La taille de fenêtre arbitre entre exactitude et délai. La somme cumulée totale gagne en exactitude grâce à la durée des épisodes en échec : c'est une confusion avec la longueur. | 28 ; 9 | « Increasing the window size improves accuracy, but mostly at the expense of slower detection. » « In fact, we observe that cumulative uncertainty scores perform much better on tasks with a large difference in duration between successful and failed rollouts. » |
| 7 | Contexte privé (raisonnement caché) lu ? | **Sans objet** : politiques robotiques sans raisonnement. Non trouvé. | — | — |
| 8 | Chiffres utilisables | Voir le tableau suivant. Ni aire sous la courbe ROC, ni rappel à 1 % de faux positifs : non trouvé. | — | — |
| 9.1 | H2 : sondes de l'agent qui agit | **partiellement** : plongement interne et actions de la politique qui agit. Ce ne sont pas des sondes de concept, et ce n'est pas un modèle de langage. | 4 | « we can detect anomalies directly in the policy’s embedding space » |
| 9.2 | H2 : accumulation additive | **partiellement** : somme sur fenêtre glissante (50 pas au plus) ; la somme cumulée totale n'est testée qu'en comparaison | 2 ; 9 | « aggregated over a sliding window. » « The two prior works most similar to ours either accumulate scores over all previous timesteps [1] or only use data from the current timestep [75]. » |
| 9.3 | H2 : toujours valide | **partiellement** : borne de fausse alarme uniforme sur les pas d'un horizon fini, par prédiction conforme. Ce n'est ni un processus e ni une martingale. Elle ne couvre pas la configuration principale. | 6 | « Proposition 1 quantifies the ability of FIPER to recognize successes as such, not failures. » |
| 9.4 | H2 : sous le seuil par action à 1 % | **libre dans cette source** | 18 | « δ: Desired FPR » |
| 9.5 | H2 : rappel croissant avec l'horizon | **libre dans cette source.** Mise en garde : la somme cumulée totale est confondue avec la durée des épisodes. | 9 | « The latter method detects failure rollouts very late, mostly due to their greater length, whereas our approach can predict failures earlier. » |
| 9.6 | H2 : calibrage sans exemple d'échec | **occupé pour le seuil** : épisodes réussis seulement. Réserve : la fenêtre et le type de seuil sont choisis pour maximiser l'exactitude pondérée par le pas, qui utilise les échecs. | 7 ; 7 | « We use M = 50 successful rollouts for the three simulation environments and M = 10 for the two real-world tasks to train the learning-based failure predictors and calibrate the thresholds. » « Thus, we use the value wA,O ∈ {1, . . . , 50} and threshold type that achieve the highest TWA across all environments » |
| 9.7 | H2 : contexte privé | **libre dans cette source** (entrées : images et état du robot, sans raisonnement) | 7 | « Our IL policies take one or two RGB images and the robot’s proprioceptive information as inputs. » |
| R1 | Réserve | Incohérence interne mineure : 0,92 de vrais positifs dans le texte (p. 9) et le tableau 6, mais 0,91 dans le tableau 2 et le texte (p. 10), pour des valeurs autrement identiques. | 9 ; 10 | « An overall TPR of 0.92 indicates that FIPER can predict different types of failures across diverse environments with high reliability. » « Yet, we find that this more conservative approach can nonetheless predict 91% of all failures. » |
| R2 | Réserve | Les seuils couverts par la garantie détectent tard ; les auteurs le disent eux-mêmes. | 30 | « Consequently, the CP-based thresholds yield a much higher TNR but also predict failures much later. » |

### Chiffres utilisables

| chiffre | valeur | page | nature | citation exacte (anglais, mot pour mot) |
|---|---|---|---|---|
| Moyenne sur 5 tâches, FIPER (fenêtre 25/50, seuil variable non couvert par la garantie) | exactitude pondérée par le pas 0,65 ; exactitude équilibrée 0,78 ; délai normalisé 0,30 | 9 | auteurs | « FIPER obtains the highest TWA of 0.65 and accuracy of 0.78, and a lower DT of 0.30 than the baselines. » |
| Même configuration : vrais positifs et vrais négatifs (dernière colonne du tableau 6) | 0,92 ; 0,65 | 28 ; 28 | auteurs | « TPR ↑ 0.99±0.00 0.55±0.02 0.43±0.06 0.52±0.00 0.89±0.05 0.92±0.00 0.92±0.00 » « TNR ↑ 0.24±0.00 0.84±0.02 0.80±0.06 0.83±0.00 0.45±0.13 0.56±0.00 0.65±0.01 » |
| Même configuration : taux de fausses alarmes sur épisodes réussis | environ 0,35 (1 − 0,65), moyenné sur δ de 0,01 à 0,10 | 28 | calcul | « TNR ↑ 0.24±0.00 0.84±0.02 0.80±0.06 0.83±0.00 0.45±0.13 0.56±0.00 0.65±0.01 » |
| Conjonction + bande conforme (couverte par la garantie) | vrais positifs 0,72 ; vrais négatifs 0,84 ; délai 0,47 | 10 | auteurs | « CP band 0.62±0.00 0.78±0.01 0.47±0.00 0.72±0.01 0.84±0.00 » |
| Conjonction + seuil conforme constant (couvert) | vrais positifs 0,59 ; vrais négatifs 0,87 ; délai 0,45 | 10 | auteurs | « AND CP constant 0.61±0.00 0.73±0.03 0.45±0.00 0.59±0.00 0.87±0.00 » |
| Conjonction + seuil variable dans le temps (non couvert) | vrais positifs 0,91 ; vrais négatifs 0,65 ; délai 0,30 | 10 | auteurs | « time-varying 0.65±0.01 0.78±0.00 0.30±0.02 0.91±0.00 0.65±0.01 » |
| Exactitude globale, limite reconnue | 78 % | 32 | auteurs | « its overall failure prediction accuracy for the best TWA is only 78% » |

### Conséquences pour H2

- **N'occupe pas l'énoncé retenu.** C'est de la robotique : des échecs, pas un sabotage. Il n'y a ni adversaire, ni modèle de langage, ni raisonnement caché.
- **C'est la source la plus proche sur le plan statistique.** Elle combine trois éléments :
  - une somme additive sur fenêtre ;
  - un seuil conforme calibré sur des épisodes réussis seulement ;
  - une borne de fausse alarme, au niveau de l'épisode, uniforme sur un horizon fini (p. 6, 20–21).
- La composante « toujours valide au sens des processus e ou des martingales » reste **libre dans cette source**. En revanche, la propriété « uniforme sur toutes les lectures de l'horizon » y est **partiellement occupée**, sous forme d'horizon fini. Le préenregistrement de G1 devrait donc opposer H2 à ce concurrent, pas seulement à une moyenne glissante.
- **Deux mises en garde directes pour le préenregistrement.**
  - (i) La somme cumulée totale détecte tard et surtout par la longueur des épisodes (p. 9–10). Il faut apparier ou contrôler les longueurs d'épisodes honnêtes et sabotés.
  - (ii) La garantie se paie cher. Les seuils couverts donnent 0,59 à 0,72 de vrais positifs avec un délai de 0,45 à 0,47. Le seuil non couvert donne 0,91 avec un délai de 0,30 (p. 10). H2 devrait rapporter son point de fonctionnement sous sa garantie seulement.

---

## 4. Yueh-Han et al. — 2506.10949v2

### Identité

| élément | réponse | page | citation exacte (anglais, mot pour mot) |
|---|---|---|---|
| titre | Monitoring Decomposition Attacks in LLMs with Lightweight Sequential Monitors | 1 | « Monitoring Decomposition Attacks in LLMs with Lightweight Sequential Monitors » |
| auteurs | Chen Yueh-Han, Nitish Joshi, Yulin Chen, Maksym Andriushchenko, Rico Angell, He He (Angell et He co-encadrent à égalité) ; Université de New York, École polytechnique fédérale de Lausanne | 1 ; 1 | « New York University École Polytechnique Fédérale de Lausanne » « Equal Advising. » |
| version, date | v2, 14 juin 2025, catégorie cryptographie et sécurité | 1 | « arXiv:2506.10949v2 [cs.CR] 14 Jun 2025 » |
| conférence | prépublication en cours d'évaluation ; conférence non nommée | 1 | « Preprint. Under review. » |
| code, données | jeux de données et code publics (adresses imprimées, non visitées) | 1 | « We publicly release our datasets at https://huggingface.co/datasets/YuehHanChen/DecomposedHarm and our code at https://github.com/YuehHanChen/Monitoring-Decomposition-Attack. » |

### Réponses aux questions

| # | question | verdict ou réponse | page | citation exacte (anglais, mot pour mot) |
|---|---|---|---|---|
| 2 | Que lit le moniteur ? | **Un observateur séparé** : un modèle de langage externe. Moniteurs légers : Llama-3.1-8B, GPT-4o-mini, GPT-4.1-nano ; moniteurs de référence : o3-mini, GPT-4o. Il lit le texte de l'historique cumulé des requêtes (sous-tâches) de l'utilisateur. Aucune activation n'est lue. | 1 ; 5 ; 17 | « We therefore propose adding an external monitor that observes the conversation at a higher granularity. » « Inputs. Cumulative prompt history Ci (variable-length list of strings) » « Here are a list of sub-tasks: {subtasks} » |
| 3 | Agrégation dans le temps ; sur combien de pas ? | **Relecture du contexte cumulé, sans somme de scores.** À chaque pas, le moniteur relit toute la liste des requêtes et rend un drapeau ou une probabilité seuillée ; le premier drapeau arrête tout. L'« accumulation » est faite par le modèle qui relit. Horizon : moins de 20 sous-tâches ; l'injection à 100 % double ce nombre (exemple des auteurs : 10 puis 20). Surveillance à partir du pas 2. | 5 ; 5 ; 10 ; 18 ; 5 | « After each new prompt pi (1 < i ≤ k) the monitor inspects the cumulative context Ci = [p1 , . . . , pi ]. » « If Ci is flagged as harmful, the LLM halts immediately; otherwise, the conversation proceeds. » « All of our tasks only consist of less than 20 subtasks. » « a 100% injection adds 10 random subtasks to an original 10 » « Because every attack contains at least two prompts, monitoring begins at step 2. » |
| 4 | Garantie statistique ? | **Aucune.** Le seuil maximise le score F1 sur un ensemble de validation composé pour moitié de tâches nuisibles. Un faux positif est défini au niveau de l'épisode : un drapeau à n'importe quel pas d'une tâche bénigne. Termes cherchés sans succès : conformal, martingale, e-value, anytime ; la seule « guarantee » est rhétorique (impact, p. 20). | 7 ; 8 ; 16 ; 6 | « The probabilistic output generally performs better, especially when a validation set is available for threshold tuning. » « We now apply the best-performing prompting techniques, with the optimal threshold found in the validation set (previous subsection), to the test sets. » « All sets have 50% harmful tasks and 50% benign tasks. » « False Positive (FP): The monitor incorrectly flags at any step in a benign task. » |
| 5 | Régime adverse : chaque pas sous un seuil par pas ? Seuil à taux de faux positifs fixé ? | **Oui sur le principe** : dans les attaques par décomposition, chaque sous-tâche paraît bénigne, et le moniteur « une requête à la fois » échoue. **Mais** le caractère bénin de chaque pas n'est pas défini par un seuil par pas à taux de faux positifs fixé (ni 1 %, ni autre). L'adversaire est l'utilisateur (détournement), pas le modèle. | 1 ; 6 ; 6 ; 9 | « Current LLM safety defenses fail under decomposition attacks, where a malicious goal is decomposed into benign subtasks that circumvent refusals. » « Single-input monitoring framework is not robust against decomposition attacks because each prompt seems benign. » « Baseline: Single Input 0.670 ± 0.028 0.411 ± 0.033 0.504 ± 0.031 0.267 ± 0.027 » « Unlike prior works, we are the first to introduce an effective monitoring method against decomposition attacks from the misuse perspective. » |
| 6 | La détection croît-elle avec l'horizon ? | **Non rapporté en fonction du nombre de pas.** Allonger l'épisode par injection de sous-tâches aléatoires fait baisser le score F1 (GPT-4o : 0,85 puis 0,72 à 100 % d'injection). Les auteurs anticipent une difficulté croissante avec l'horizon. | 7 ; 19 | « For example, without injection, GPT-4o achieves an F1 score of 0.85, but this decreases to 0.72 when the injection rate is 100% » « monitoring can become increasingly difficult as the time horizon or length of a subtask increases » |
| 7 | Contexte privé (raisonnement caché) lu ? | **Non.** Le moniteur lit les requêtes de l'utilisateur. La « chaîne de pensée » citée est une technique d'incitation du moniteur lui-même, pas le raisonnement de l'agent. | 17 ; 7 | « Here are a list of sub-tasks: {subtasks} » « In total, we evaluate prompts that incorporate in-context learning (ICL) examples (Figure 11), safety guidelines (Figure 12), chain-of-thought reasoning (Figure 13), and a hypothesis generation approach (Figure 14). » |
| 8 | Chiffres utilisables | Voir le tableau suivant. Ni rappel à taux de faux positifs fixé, ni aire sous la courbe ROC : non trouvé. | — | — |
| 9.1 | H2 : sondes de l'agent qui agit | **libre dans cette source** (observateur textuel externe) | 1 | « We therefore propose adding an external monitor that observes the conversation at a higher granularity. » |
| 9.2 | H2 : accumulation additive | **libre dans cette source** (relecture du contexte, pas de somme) | 5 | « If Ci is flagged as harmful, the LLM halts immediately; otherwise, the conversation proceeds. » |
| 9.3 | H2 : toujours valide | **libre dans cette source** | 8 | « with the optimal threshold found in the validation set » |
| 9.4 | H2 : sous le seuil par action à 1 % | **partiellement** : le régime « chaque sous-tâche bénigne » est occupé pour un moniteur textuel ; aucun seuil par pas n'est calibré à 1 % | 6 | « Single-input monitoring framework is not robust against decomposition attacks because each prompt seems benign. » |
| 9.5 | H2 : rappel croissant avec l'horizon | **libre dans cette source** (baisse avec l'injection ; moins de 20 pas) | 7 ; 10 | « but this decreases to 0.72 when the injection rate is 100% » « All of our tasks only consist of less than 20 subtasks. » |
| 9.6 | H2 : calibrage sans exemple d'attaque | **libre dans cette source** (seuil optimisé sur une validation pour moitié nuisible) | 16 | « All sets have 50% harmful tasks and 50% benign tasks. » |
| 9.7 | H2 : contexte privé | **libre dans cette source** | 17 | « Here are a list of sub-tasks: {subtasks} » |
| R1 | Réserve | La section d'impact contient un marqueur de citation résiduel d'assistant conversationnel : une partie du texte a probablement été générée. C'est sans effet sur les chiffres, mais à noter (R4). | 21 | « :contentReference[oaicite:0]index=0 » |

### Chiffres utilisables

| chiffre | valeur | page | nature | citation exacte (anglais, mot pour mot) |
|---|---|---|---|---|
| F1, moniteur léger optimisé GPT-4o-mini (exemples de questions-réponses dans l'invite), ensemble de test | 0,913 ± 0,013 | 8 | auteurs | « Optimized GPT-4o-mini QA Task ICL 0.913 ± 0.013 » |
| Taux de défense réussie (rappel), moniteurs optimisés | jusqu'à 93 % (GPT-4o-mini) et 89 % (Llama-3.1-8B) | 8 | auteurs | « Using the DSR as a metric, the optimized GPT-4o-mini and Llama-3.1-8B hit up to 93% and 89% defense success rates, respectively » |
| Une requête à la fois contre séquentiel, sans incitation particulière : F1 puis rappel, pour GPT-4.1-nano et Llama-3.1-8B | une requête : F1 0,670 et 0,411 ; rappel 0,504 et 0,267. Séquentiel : F1 0,770 et 0,719 ; rappel 0,631 et 0,575 | 6 ; 6 | auteurs | « Baseline: Single Input 0.670 ± 0.028 0.411 ± 0.033 0.504 ± 0.031 0.267 ± 0.027 » « Ours: Sequential 0.770 ± 0.022 0.719 ± 0.026 0.631 ± 0.030 0.575 ± 0.033 » |
| Succès de l'attaque par décomposition sur GPT-4o, moyenne des trois cadres | 87,2 % | 3 | auteurs | « Average 77.8 7.2 21.2 87.2 » |
| Effet de 100 % d'injection aléatoire, GPT-4o | F1 0,85 puis 0,72 | 7 | auteurs | « For example, without injection, GPT-4o achieves an F1 score of 0.85, but this decreases to 0.72 when the injection rate is 100% » |
| Rappel à 1 % de faux positifs | non trouvé : seuils optimisés pour le score F1 | — | — | — |

### Conséquences pour H2

- **N'occupe pas l'énoncé retenu.** Le moniteur est un observateur textuel, sans activations, sans somme, sans garantie. Il est calibré avec des attaques et ne lit pas de contexte privé.
- **Occupe partiellement le régime « chaque pas bénin »**, avec un moniteur séquentiel qui bat le moniteur pas à pas (p. 6). Ce cadre est un détournement par l'utilisateur, avec moins de 20 pas.
- **Bases à reprendre**, toutes deux recalibrées sur épisodes honnêtes au même taux de faux positifs :
  - le moniteur textuel séquentiel qui relit le contexte cumulé ;
  - le moniteur « une requête à la fois », qui sert aussi à définir le régime « sous le seuil par action ».
- **Réserve.** Les rappels publiés (89–93 %) sont obtenus à seuil optimisé pour le score F1 sur des données moitié nuisibles. Ils ne se comparent pas à un point de fonctionnement à 1 % de faux positifs.

---

## Synthèse (dix lignes au plus)

1. **Occupé en entier : par aucune des quatre sources.** Aucune ne lit l'agent saboteur lui-même en accumulant des scores de sondes sous une garantie toujours valide calibrée sur épisodes honnêtes.
2. **Sondes sur le modèle qui agit : partiellement.** Padhi (p. 3, 7) sonde le succès ou l'échec d'un pas ; Kulkarni (p. 3) sonde un modèle visé par un utilisateur.
3. **Somme additive : partiellement.** Dérive cumulée des activations chez Kulkarni (p. 12, 21) ; somme sur fenêtre chez FIPER (p. 4–5).
4. **Borne de fausse alarme uniforme : partiellement**, sur un horizon fini, par prédiction conforme calibrée sur des réussites seules (FIPER p. 6, 20–21). **Régime « chaque pas bénin » : partiellement** (Yueh-Han p. 1, 6 ; Kulkarni p. 15). **Croissance avec l'horizon : partiellement**, seulement pour la détection précoce selon la durée du pivot (Kulkarni p. 5, 20).
5. **Libre dans ces quatre sources** : garantie au sens des processus e ou des martingales (aucune occurrence) ; moniteur par action calibré à 1 % sous lequel reste chaque action sabotée ; rappel croissant avec l'horizon dans ce régime ; contexte privé caché ; sabotage par l'agent lui-même.
6. **Signaux contraires.** Détection plus faible sur les conversations réelles longues (Kulkarni p. 19). Somme cumulée confondue avec la longueur des épisodes (FIPER p. 9–10). Dilution par sous-tâches injectées (Yueh-Han p. 7).
7. **Bases à ajouter au préenregistrement de G1**, toutes recalibrées sur épisodes honnêtes au même taux de faux positifs : (a) seuil non supervisé sur la dérive cumulée des activations (Kulkarni p. 21) ; (b) somme sur fenêtre avec seuil conforme constant ou bande, plus somme cumulée totale et fenêtre de 1 (FIPER p. 6, 9, 20–21) ; (c) moniteurs textuels séquentiel et « une requête à la fois » (Yueh-Han p. 5–6).
8. **À ajouter aussi** : (d) en référence haute seulement, la sonde supervisée de Kulkarni, qui exige des exemples d'attaque (p. 7) ; (e) un contrôle de la longueur des épisodes (Kulkarni p. 3, 19 ; FIPER p. 9–10).

---

## Contrôle des citations

- **Méthode.** Script `scripts/controle_citations.py`. Il lit ce rapport, prend chaque citation entre guillemets français dans les colonnes « citation » des tableaux, et la cherche sur la page indiquée de l'article de la section. Il essaie trois extractions `pdftotext -layout` : page entière, demi-page gauche, demi-page droite.
- **Tolérances admises, et elles seules** : suites de blancs (espaces, fins de ligne, rembourrage de mise en page) ; césure en fin de ligne ; fin de ligne sans espace juste après un trait d'union, un tiret ou une barre oblique. Casse, ponctuation, apostrophes, chiffres et symboles doivent être identiques. Aucune citation n'est tronquée par des points de suspension.
- **Garde testée** (règle R5, `scripts/test_controle_citations.py`, sortie dans `test-garde-controle.txt`) : 10 cas, 10 conformes. Les 4 cas sains passent. Les 6 artefacts échouent : un mot changé, une apostrophe droite, un chiffre changé, un tiret remplacé, une mauvaise page, une coupe par points de suspension.
- **Résultat** (sortie complète dans `controle-citations.txt`) : **176 citations contrôlées, 176 réussies, 0 échec.**
  - Par article : Kulkarni 56, Kaur et Padhi 33, FIPER 46, Yueh-Han 41.
  - Source qui a confirmé chaque citation : page entière seule 85 ; colonne gauche seule 48 ; colonne droite seule 14 ; page entière et une colonne 29.
  - Un décompte indépendant des guillemets dans les colonnes « citation » donne le même total.
  - Hors tableaux, les guillemets du rapport n'entourent que des termes français, jamais une citation anglaise.
