# Lecture de niveau 2, lot 2 — A2a « évasion de sondes » — rapport du lecteur

- **Date** : 2026-10-06, rapport établi vers 16 h 45 (temps universel coordonné) ; lecture commencée à 16 h 15.
- **Lecteur** : sous-agent neuf ; n'a écrit aucun des documents vérifiés ; aucune modification sous `/home/user/controle-ia` (lecture seule).
- **Consignes appliquées** : `lot2/consigne-commune.md` et `lot2/consignes-A2a-evasion-sondes.md` ; règles R7 (chiffre opposable seulement sur PDF empreinté, page et citation exacte), R8 (une limitation d'un papier n'est pas un trou du champ), R5 (contrôle testé sur cas juste et cas altéré).
- **Sources des affirmations** : « L70 » et « L134 » = `docs/etat-de-l-art-controle-ia-v1.md`, lignes 70 et 134 ; « L170 » = `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md`, ligne 170 (section 5, « Références nouvelles à lire » ; « Tr. » y désigne l'hypothèse de transposition jeton → action).

## 0. PDF lus et empreintes

Dossier des PDF (Portable Document Format) : `/home/user/controle-ia/docs/sources/pdf/`. Empreintes SHA-256 (Secure Hash Algorithm, 256 bits) recalculées avec `sha256sum -c` : **5 sur 5 conformes** aux consignes. Le même contrôle refuse une empreinte volontairement altérée (code retour 1).

| PDF | pages | empreinte SHA-256 (attendue = calculée) | lecture |
|---|---|---|---|
| `2506.14261v4.pdf` | 24 | `4b0960622664e77d888974955b29f9c0e5913266392caeecac2b844f011e244c` | en entier |
| `2412.09565v2.pdf` | 51 | `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9` | p. 1 à 30 et 41 à 51 en entier ; références p. 30 à 40 parcourues par recherche de mots |
| `2512.11949v1.pdf` | 30 | `e0f8ddfff6e75d835995886a630a5d077ed871c28599f710b41c96efc949e3ee` | en entier, sauf exemples qualitatifs en images (bas de la p. 27, p. 28 à 30) |
| `2601.11516v4.pdf` | 40 | `c4a36db54c9d679a718a0e35b9cad09fa628d81f6174bb6e1d8c6b26a063d8bf` | en entier, annexes A à L comprises ; références p. 20 à 23 parcourues |
| `2602.15515v2.pdf` | 30 | `f6547ec830104abf8ceca353e46e32ee78453f6470fd1c03053e13834ebc54cb` | en entier |

**Méthode de lecture.** Texte extrait page par page avec `pdftotext -layout` (version 24.02.0) ; les pages citées sont le rang dans le fichier (pour ces cinq PDF, il coïncide avec le numéro imprimé). Les valeurs portées seulement par des figures (barres, nuages de points) n'ont pas été relevées, sauf mention « figure ».

**Ce qui n'a pas été lu.** 2412.09565v2 : références (p. 30 à 40), parcourues seulement par recherche de mots (« ICLR », « conference », « published », « under review », « proceedings », « tax »). 2512.11949v1 : bas de la p. 27 et p. 28 à 30, exemples qualitatifs en images sans couche texte (vérifié avec `pdfimages` ; 1 à 4 mots de texte par page). Ailleurs, les références ont été parcourues sans lecture ligne à ligne.

## 1. Contrôle des citations (consigne commune, point 5)

- **Script** : `scripts/controle_citations.py`. Il ne tolère que les blancs (retirés des deux côtés) et les césures (un trait d'union suivi d'un retour à la ligne peut manquer dans la citation, ou y correspondre à un vrai trait d'union). Aucune autre normalisation : ni casse, ni ligatures, ni guillemets. Texte comparé : d'abord l'extraction `-layout` de la page indiquée ; à défaut, l'extraction `pdftotext -raw` de **la même page**, qui garde les césures et suit l'ordre des colonnes (nécessaire pour les pages à deux colonnes, que `-layout` entrelace). La page n'est jamais changée, et le mode retenu est affiché pour chaque citation : aucun repli silencieux.
- **Tests préalables (R5)** : `scripts/test_controle.py`, 10 cas sur 10 conformes. 5 cas justes acceptés : phrase simple, césure recollée, trait d'union réel en fin de ligne, chiffres, page à deux colonnes. 5 cas altérés refusés : un mot changé, un chiffre changé, une majuscule changée, une bonne citation sur la mauvaise page, une page à deux colonnes altérée.
- **Résultat** (dernière ligne de la sortie brute du script) : « 124 citations controlees, 0 echec(s) » ; 107 citations retrouvées dans le texte `-layout`, 17 dans le texte `-raw`. Détail : `controle-citations-sortie.txt`.
- **Pas de recopie à la main** : chaque citation de ce rapport est injectée depuis `citations.jsonl`, le fichier même qui a été contrôlé, par `scripts/rendre_rapport.py` (qui échoue sur tout identifiant inconnu ou espace réservé non résolu). Les citations contenant un astérisque sont mises en texte littéral pour que le Markdown ne les transforme pas.

## 2. Sigles anglais présents dans les citations (développés)

FPR = false positive rate, taux de faux positifs ; FNR = false negative rate, taux de faux négatifs ; TPR = true positive rate, taux de vrais positifs (rappel) ; LLM = large language model, grand modèle de langage ; MLP = multilayer perceptron, perceptron multicouche ; SAE = sparse autoencoder, autoencodeur parcimonieux ; RL = reinforcement learning, apprentissage par renforcement ; RLVR = reinforcement learning with verifiable rewards, apprentissage par renforcement à récompenses vérifiables ; GRPO = Group Relative Policy Optimization, optimisation de politique relative par groupe ; OAT = Obfuscated Adversarial Training, entraînement adversarial contre l'obfuscation ; SRR = StrongReject Reward, récompense donnée par le juge StrongREJECT ; SQL = Structured Query Language, langage de requête structuré ; HTML = HyperText Markup Language ; EMA = exponential moving average, moyenne mobile exponentielle ; MBPP = Mostly Basic Python Problems (jeu de problèmes de programmation) ; RepE = Representation Engineering (jeu de données de tromperie) ; RQ2 = research question 2, deuxième question de recherche ; GPU = graphics processing unit, processeur graphique ; ML = machine learning, apprentissage automatique ; AI = artificial intelligence, intelligence artificielle ; NeurIPS = Neural Information Processing Systems ; PMLR = Proceedings of Machine Learning Research ; cs.LG = rubrique « Machine Learning » d'arXiv ; FAR.AI = nom d'organisation. Dans les affirmations du programme : ICLR = International Conference on Learning Representations ; SQL = Structured Query Language, langage de requête structuré.

---

## 3. Article 1 — RL-Obfuscation (arXiv 2506.14261v4)

### Identité

- **Titre** : RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? (petites capitales p. 1 ; identique dans les métadonnées du PDF).
- **Auteurs (tous)** : « Rohan Gupta Erik Jenner » [R01, p. 1]. Affiliation imprimée sous le premier nom : « ML Alignment and Theory Scholars » [R28, p. 1].
- **Version et date** : « arXiv:2506.14261v4 [cs.LG] 26 Feb 2026 » [R02, p. 1].
- **Venue** : aucune imprimée dans le PDF. Attestation secondaire seulement, dans la bibliographie d'un autre article du lot : « Gupta, R. and Jenner, E. RL-obfuscation: Can language models learn to evade latent-space monitors? In Mechanistic Interpretability Workshop at NeurIPS 2025, 2025. » [A12, p. 11].
- **Cadre** : « We apply RL-Obfuscation to Language Models ranging from 7B to 14B parameters » [R26, p. 1] ; « we use Group Relative Policy Optimisation (GRPO) (Shao et al., 2024) » [R25, p. 5] ; contenu nocif « (as determined by StrongREJECT (Souly et al., 2024)) » [R29, p. 2] ; sondes figées, une couche par modèle : « The probes were trained at layer 10, 12 and 20 for Llama 2 7B, Llama 3 8B and Qwen 2.5 14B, respectively. » [R24, p. 7].

### Affirmations du programme

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 1.1 | « Gupta & Jenner, arXiv 2506.14261 » (L70, L134) | **confirmé** | 1 | « Rohan Gupta Erik Jenner » [R01, p. 1] ; « arXiv:2506.14261v4 [cs.LG] 26 Feb 2026 » [R02, p. 1] |
| 1.2 | « évasion par apprentissage par renforcement sur les poids, sans gradient à travers le moniteur » (L70) ; « apprentissage par renforcement sur les poids » (L134) | **confirmé** | 2 | « Unlike input-space attacks, RL-Obfuscation can modify the weights of the LLM as part of red-teaming. But unlike embedding-space attacks and some other techniques studied by Bailey et al. (2024), RL-Obfuscation does not use any gradients through the monitor. » [R03, p. 2] |
| 1.3 | « les sondes à max ou à attention résistent » (L70) ; « max et attention robustes » (L134) | **confirmé**, au sens des auteurs : l'apprentissage par renforcement n'a pas obtenu contre elles d'évasion qui garde des réponses de qualité (voir 1.6 et les réserves) | 1 ; 7 | « We find that token-level monitors are highly vulnerable to this attack while more holistic monitors, such as max-pooling or attention-based probes, remain robust. » [R04, p. 1] ; « Linear (max) 0.058 4.78 0.044 4.96 1.0 1.0 » [R07, p. 7] |
| 1.4 | « la moyenne, la médiane […] cèdent » (L70) ; « moyenne, médiane […] vulnérables » (L134) | **confirmé** | 5 ; 7 | « Monitors that use mean or median aggregations are not robust to RL Obfuscation, whereas attention probes and max aggregation remain robust to RL-Obfuscation. » [R05, p. 5] ; « Linear (mean) 0.75 2.8 0.82 3.1 0.594 3.85 » [R21, p. 7] |
| 1.5 | « […] et les scores par token cèdent » (L70) ; « […] et par-token vulnérables » (L134) | **corrigé**. En L70, remplacer « la moyenne, la médiane et les scores par token cèdent » par « l'agrégation par moyenne ou par médiane des scores par jeton cède ». En L134, remplacer « moyenne, médiane et par-token vulnérables » par « agrégation par moyenne ou par médiane des scores par jeton vulnérable ». Motif : tous les moniteurs de l'article notent chaque jeton puis agrègent ; une sonde linéaire entraînée jeton par jeton puis agrégée par max résiste (0,058 et 0,044 d'évasion) ; les auteurs opposent des agrégations, non le calcul par jeton. Les « token-level monitors » du résumé (1.3) sont les sondes agrégées par moyenne ou médiane. | 4 ; 7 | « is an aggregation function over t token-wise scores to get a single score for the entire completion (eg: mean over tokens). » [R09, p. 4] ; « For MLP probes with max aggregation, we train the probe using a maxpool strategy (See Section B) as the tokenwise probe performs very poorly in this type of aggregation » [R08, p. 7] ; « Linear (max) 0.058 4.78 0.044 4.96 1.0 1.0 » [R07, p. 7] ; « This suggests pooling signals across tokens efficiently is more important than architectures that process per-token latents. » [R06, p. 7] |
| 1.6 | statut « **Établi** » (L70) | **corrigé** (portée). Remplacer « **Établi** : au niveau token, les sondes à max ou à attention résistent à l'évasion par apprentissage par renforcement sur les poids, sans gradient à travers le moniteur » par « **Établi dans le cadre testé** (nocivité jugée par StrongREJECT, modèles de 7 à 14 milliards de paramètres, sondes entraînées sur une couche) : au niveau du jeton, l'apprentissage par renforcement sur les poids, sans gradient à travers le moniteur, n'a pas obtenu contre les agrégations max ou attention d'évasion qui préserve la qualité des réponses ; les auteurs avertissent qu'un tel échec peut tenir à des difficultés d'optimisation plutôt qu'à une robustesse fondamentale ». | 10 ; 6 ; 19 | « Conversely, failure to bypass a monitor with RL-Obfuscation might be due to optimization difficulties rather than fundamental robustness. » [R10, p. 10] ; « We also limit our work to a simplistic setting of harmfulness, where reward signals are easy to obtain. » [R11, p. 10] ; « As a rule of thumb, models with a StrongReject Score less than 2.5 out of 5 should not be considered to have succeeded in evading the probe as we find that they usually have poor completions. » [R12, p. 6] ; « The model can fail to evade probes in two ways: either optimising only on the probe scores (as seen in some runs with max aggregation) or only on the blackbox behavior (as seen in all of the attention probes). » [R27, p. 19] |

### Chiffres utilisables

- **Tableau 1 (auteurs)** — « Table 1: Evasion Rate (1 - Recall) at 1% FPR and StrongReject Reward (SRR) for Qwen 2.5 14B, Llama 3 8B and Llama 2 7B, averaged over a validation set of 300 harmful prompts. » [R30, p. 7] Lignes (colonnes : Llama 3 8B, Qwen 2.5 14B, Llama 2 7B ; pour chacune, taux d'évasion puis récompense StrongREJECT sur 5) : « Linear (mean) 0.75 2.8 0.82 3.1 0.594 3.85 » [R21, p. 7] ; « Linear (max) 0.058 4.78 0.044 4.96 1.0 1.0 » [R07, p. 7] ; « Attention (mean) 0.01 1.08 0.018 4.5 0.02 4.45 » [R19, p. 7].
- **Rappel correspondant (calcul : rappel = 1 − taux d'évasion, d'après la légende du tableau 1)** : sonde linéaire agrégée par max, 0,942 (Llama 3 8B) et 0,956 (Qwen 2.5 14B) ; sonde linéaire agrégée par moyenne, 0,25 et 0,18.
- **Tableau 4, Llama 2 7B (auteurs)** : sonde linéaire à max « max 0.994 1.0 0.98 » [R13, p. 19] (évasion, récompense StrongREJECT, taux de vrais positifs du modèle de base) ; sonde linéaire à moyenne « mean 0.594 3.72 0.96 » [R20, p. 19].
- **Règle des auteurs pour juger une évasion** : « As a rule of thumb, models with a StrongReject Score less than 2.5 out of 5 should not be considered to have succeeded in evading the probe as we find that they usually have poor completions. » [R12, p. 6].
- **Part du changement de comportement dans la baisse de rappel (auteurs)** : « the change in policy contributes to approximately 70% of the drop in recall. » [R17, p. 9].

### Réserves de lecture (R4, symétrie)

- Sur Llama 2 7B, les lignes « max » du tableau 4 et la case Llama 2 7B de la ligne linéaire (max) du tableau 1 montrent une évasion presque totale obtenue en sacrifiant la qualité (récompense 1,0 sur 5) : « résister » veut dire ici « pas d'évasion utile », non « score inchangé » — « The model can fail to evade probes in two ways: either optimising only on the probe scores (as seen in some runs with max aggregation) or only on the blackbox behavior (as seen in all of the attention probes). » [R27, p. 19] ; « (1) The tuned model ignores the blackbox rewards and acts maximally unhelpful to evade the probes. » [R14, p. 18]. Sur Llama 3 8B et Qwen 2.5 14B, en revanche, la sonde linéaire à max résiste en gardant une qualité élevée (récompense 4,78 et 4,96, « Linear (max) 0.058 4.78 0.044 4.96 1.0 1.0 » [R07, p. 7]).
- Sur Llama 3 8B, la ligne attention (moyenne) du tableau 1 a une récompense de 1,08 sur 5 (« Attention (mean) 0.01 1.08 0.018 4.5 0.02 4.45 » [R19, p. 7]) : run dégénéré, sans évasion ni qualité ; il ne montre pas la résistance de l'attention face à un attaquant qui garde des réponses utiles.
- Écart entre tableaux pour une même ligne (sonde linéaire à moyenne, Llama 2 7B : récompense 3,85 au tableau 1, 3,72 au tableau 4) : runs distincts, issus de recherches d'hyperparamètres différentes — « RQ2 (Comparison): We conducted a hyperparameter search over a grid of » [R22, p. 18] ; « We performed a random hyperparameter search over » [R23, p. 18]. Ne pas mêler les deux tableaux.

### Antériorité (R8)

- **Transposition jeton → action** : non occupée. L'article est la source du constat au niveau du jeton ; il ne porte que sur des sondes appliquées à la génération d'une réponse (« we have to limit our analysis to generation-based probes only, since RL wouldn’t have significant control over activations on prompts. » [R15, p. 10]), dans le seul cadre de la nocivité (« We also limit our work to a simplistic setting of harmfulness, where reward signals are easy to obtain. » [R11, p. 10]), et renvoie à plus tard les mensonges et les manigances (« Studying whether models can evade latent-space monitors in ambiguous settings like detecting lies and/or scheming is a promising direction of future work. » [R16, p. 10]). Aucune agrégation sur des actions ou des trajectoires. Un autre article du lot décrit son mécanisme d'évasion comme purement syntaxique : « Gupta & Jenner (2025) via RL resulting in purely syntactic evasion (HTML tags, punctuation). » [A19, p. 4].
- **HC2b** : non occupée. Seule observation voisine, pendant l'entraînement et non face à un moniteur : « Including a prefix system prompt stating the model is being probed: We tried some variants of the following system prompt, but saw no qualitative differences in the results » [R18, p. 16].
- **H2, H1, lemme d'additivité, théorème négatif, HC1, papier B** : non touchés (aucune accumulation séquentielle ; le juge StrongREJECT sert de récompense, non de moniteur concurrent ; aucun budget total ; un seul modèle).

---

## 4. Article 2 — Bailey et al., Obfuscated Activations (arXiv 2412.09565v2)

### Identité

- **Titre** : Obfuscated Activations Bypass LLM Latent-Space Defenses (p. 1 ; le PDF n'a pas de titre dans ses métadonnées).
- **Auteurs (tous, dans l'ordre)** : `« Luke Bailey*1 , Alex Serrano*†2 , Abhay Sheshadri*†3 , Mikhail Seleznyov*†4 , Jordan Taylor*†5 , Erik Jenner*6 »` [B02, p. 1] ; « Jacob Hilton7 , Stephen Casper8 , Carlos Guestrin1, 9 , Scott Emmons6 » [B03, p. 1] (l'astérisque marque les contributeurs principaux).
- **Version et date** : « arXiv:2412.09565v2 [cs.LG] 8 Feb 2025 » [B01, p. 1].
- **Venue** : aucune imprimée (voir 2.2).
- **Cadre** : attaques d'« obfuscation » (suffixes d'embedding ou en jetons réels, réglage fin, empoisonnement de données) contre des moniteurs d'activations (sondes, détecteurs hors distribution, autoencodeurs parcimonieux) ; métrique « To quantify whether a set of activations fool a monitor, we use recall at a 1% false positive rate (FPR). » [B05, p. 6] ; modèle « Unless stated otherwise, we use Llama-3-8B-Instruct as our model being monitored. » [B06, p. 7].

### Affirmations du programme

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 2.1 | « Bailey et al., arXiv 2412.09565 » (L134) | **confirmé** | 1 | « arXiv:2412.09565v2 [cs.LG] 8 Feb 2025 » [B01, p. 1] ; `« Luke Bailey*1 , Alex Serrano*†2 , Abhay Sheshadri*†3 , Mikhail Seleznyov*†4 , Jordan Taylor*†5 , Erik Jenner*6 »` [B02, p. 1] |
| 2.2 | « ICLR 2026 » (L134) | **introuvable** dans le PDF empreinté : la v2 (8 février 2025) n'imprime aucune venue ; recherche faite sur les 51 pages de « ICLR », « conference », « published », « under review », « proceedings » (seules sortent des références à d'autres travaux). Attestation secondaire seulement, dans la bibliographie de 2602.15515v2 (ci-contre). Formulation à retenir tant que la version publiée n'est pas empreintée : « arXiv 2412.09565 (v2, 8 février 2025) ; parution à la quatorzième International Conference on Learning Representations (2026) attestée seulement par la bibliographie de arXiv 2602.15515v2, p. 10 ». | 2602.15515v2, p. 10 | « Emmons, S. Obfuscated activations bypass LLM latent-space defenses. In The Fourteenth International Conference on Learning Representations, 2026. » [A11, p. 10] |
| 2.3 | « sur Llama-3-8B-Instruct » (L134) | **confirmé** | 7 ; 8 | « Unless stated otherwise, we use Llama-3-8B-Instruct as our model being monitored. » [B06, p. 7] ; « Figure 4: Standard jailbreaking and obfuscation attack results against Llama-3-8b-Instruct. » [B07, p. 8] |
| 2.4 | « le rappel de sondes de nocivité tombe de 100 % à 0 % à 1 % de faux positifs tout en gardant environ 90 % de contournement » (L134) | **corrigé** (nuances omises). Remplacer par : « des attaques d'obfuscation, surtout par suffixe d'embedding (accès boîte blanche), font **souvent** tomber le rappel à 1 % de faux positifs de sondes de nocivité — agrégées pour la plupart par une moyenne sur les couches et les jetons — de 100 % à 0 % tout en gardant un taux de contournement de 90 % ; les suffixes en jetons réels n'obtiennent qu'une obfuscation partielle ». | 1 ; 6 ; 9 ; 8 ; 29 ; 5 | « For example, against probes trained to classify harmfulness, our attacks can often reduce recall from 100% to 0% while retaining a 90% jailbreaking rate. » [B04, p. 1] ; « To quantify whether a set of activations fool a monitor, we use recall at a 1% false positive rate (FPR). » [B05, p. 6] ; « Probes perform well on clean prompts but get 0% recall against obfuscation attacks. » [B09, p. 9] ; « obfuscation embedding attacks and even hard prompts induce obfuscated activations against a wide range of monitors while still jailbreaking the model (Fig. 4b). » [B25, p. 9] ; « Hard token attacks aren’t quite as successful but still achieve partial obfuscation for all probes. » [B08, p. 8] ; « they don’t fully obfuscate against generation-based probes, and the jailbreaking rate is lower. » [B21, p. 29] ; « Most of our monitors separately consider activations at multiple layers of the model and aggregate scores over layers and sequence dimensions by taking a mean. » [B19, p. 5] |
| 2.5 | « « taxe d'obfuscation » sur une tâche SQL, croissante avec le nombre de couches obfusquées » (L134) | **corrigé**. Le sens (un coût en performance qui croît avec le nombre de couches obfusquées) est confirmé. Mais le terme cité est absent de l'article (« tax » : 0 occurrence sur les 51 pages ; « capability tax » vient de Neural Chameleons, qui le juge négligeable : « The evasion behavior has a negligible capability tax. » [N21, p. 3]) ; et l'expérience porte sur Gemma-2-2b, non sur Llama-3-8B-Instruct. Remplacer par : « compromis entre obfuscation et performance (“trade-off between obfuscation and model performance”) sur l'écriture de requêtes SQL (Structured Query Language) évaluée par SQLEval, avec Gemma-2-2b : la part de requêtes correctes (34,8 % sans obfuscation) baisse quand on obfusque contre davantage de couches ». | 3 ; 23 ; 21 ; 48 ; 49 | « When obfuscating against probes that detect SQL code, the model still generates SQL, but its code is incorrect more often than without obfuscation (§5). This suggests a trade-off between obfuscation and performance in difficult tasks. » [B11, p. 3] ; « There is a trade-off between obfuscation and model performance. As Fig. 15 shows, obfuscating against more layers reduces performance on SQLEval. » [B12, p. 23] ; « We use the Gemma-2-2b model and GemmaScope SAEs [Lieberum et al., 2024]. » [B13, p. 21] ; « We use these SAEs on Gemma-2-2b-it » [B22, p. 48] ; « Without obfuscation (34.8%) » [B14, p. 23] ; « Performance on SQLEval [-0.879, -0.765] [-0.916, -0.801] [-0.881, -0.697] [-0.820, -0.574] » [B15, p. 49] |
| 2.6 | « code public » (L134) | **confirmé** | 1 | « Code available at https://github.com/LukeBailey181/obfuscated-activations » [B16, p. 1] |

### Chiffres utilisables

- **Résumé (auteurs)** : « For example, against probes trained to classify harmfulness, our attacks can often reduce recall from 100% to 0% while retaining a 90% jailbreaking rate. » [B04, p. 1].
- **Sans entraînement adversarial contre l'obfuscation (OAT, Obfuscated Adversarial Training), contre une sonde à régression logistique, Llama-3-8B-Instruct (auteurs)** : « against Llama-3-8B-Instruct without OAT, the same obfuscation attack achieves a 95% jailbreak rate and zero recall after only 256 gradient steps (or about 10 minutes). » [B10, p. 26] ; **avec cet entraînement** : « achieves a jailbreaking rate of 35% and zero recall (at 1% FPR) after 16,384 gradient steps (about 10 hours on a single GPU). » [B24, p. 26].
- **Entraînement adversarial des moniteurs (auteurs)** : « But we find that an attacker can always find new activations that bypass the monitor, even after retraining the monitor for over 70 iterations of alternating attack and defense optimization (§3.5). » [B23, p. 3].
- **Requêtes SQL (auteurs)** : « Without obfuscation (34.8%) » [B14, p. 23] (légende de la figure 15) ; intervalles de confiance à 95 % de la corrélation de Pearson entre nombre de couches obfusquées et performance, colonnes « autoencodeur brut, autoencodeur + régression logistique, régression logistique, perceptron multicouche » : « Performance on SQLEval [-0.879, -0.765] [-0.916, -0.801] [-0.881, -0.697] [-0.820, -0.574] » [B15, p. 49].

### Antériorité (R8)

- **Transposition jeton → action** : non occupée (ni action ni trajectoire). L'article borne toutefois le constat « max robuste » de l'article 1 à sa menace sans gradient : dans l'étude SQL, les moniteurs agrégés par max sur la séquence (« We aggregate these scores with a maximum over the sequence dimension and a mean over layers to get a final prediction for the sample. » [B17, p. 22]) tombent à un rappel quasi nul sous attaque par suffixe d'embedding (« Monitors get near-zero recall under a soft-prompt obfuscation attack. » [B18, p. 22]). Les résultats sur la nocivité portent surtout sur des agrégations par moyenne (« Most of our monitors separately consider activations at multiple layers of the model and aggregate scores over layers and sequence dimensions by taking a mean. » [B19, p. 5]).
- **H2** : non occupée. L'article justifie seulement le calibrage d'un seuil à 1 % de faux positifs sur des exemples négatifs, pour une décision isolée : « First, note that picking a threshold that achieves a 1% FPR is something a realistic defender can do, since the defender has access to benign (i.e., negative) samples in all our experiments. » [B20, p. 51].
- **H1, lemme d'additivité, théorème négatif, HC1, HC2b, papier B** : non touchés.

---

## 5. Article 3 — Neural Chameleons (arXiv 2512.11949v1)

### Identité

- **Titre imprimé** : « Neural Chameleons: Language Models Can Learn to Hide Their Thoughts from Activation Monitors » [N03, p. 1]. Les métadonnées du PDF, et les consignes, portent « … from Unseen Activation Monitors » : le mot « Unseen » n'est pas dans le titre imprimé.
- **Auteurs (tous)** : `« Max McGuinness*1 , Alex Serrano*1,2 , Luke Bailey3† , Scott Emmons1† »` [N01, p. 1] ; `« * Equal contribution. »` [N20, p. 1] (McGuinness et Serrano) ; « † Advising authors. » [N19, p. 1] (Bailey et Emmons).
- **Version et date** : « arXiv:2512.11949v1 [cs.LG] 12 Dec 2025 » [N02, p. 1].
- **Venue** : aucune imprimée.
- **Cadre** : réglage fin d'un modèle pour qu'il fasse baisser, sur déclencheur explicite, des sondes de concepts anodins ; test sur des sondes de sécurité jamais vues, entraînées après coup sur le modèle figé ; Gemma-2-9b-it surtout, plus Gemma-2-2b-it, Llama-3.1-8b-instruct et Qwen-2.5-7b-instruct ; seuil calibré à 1 % de faux positifs.

### Affirmations du programme

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 3.1 | « Neural Chameleons (McGuinness, Serrano, Bailey, Emmons), arXiv 2512.11949 » (L134) | **confirmé** | 1 | `« Max McGuinness*1 , Alex Serrano*1,2 , Luke Bailey3† , Scott Emmons1† »` [N01, p. 1] ; « arXiv:2512.11949v1 [cs.LG] 12 Dec 2025 » [N02, p. 1] |
| 3.2 | « auto-obfuscation apprise par réglage fin » (L134) | **confirmé** (réglage fin des poids du modèle sur une perte définie par les scores de sondes d'entraînement figées, donc avec gradient à travers ces sondes ; comportement déclenché par une phrase explicite) | 1 ; 11 ; 5 ; 6 ; 2 | « We demonstrate that finetuning can create Neural Chameleons: models capable of zero-shot evading activation monitors. » [N04, p. 1] ; « having demonstrated that self-obfuscation is learnable under a stress-testing paradigm » [N06, p. 11] ; « is the obfuscation loss that drives probe scores toward target values » [N22, p. 5] ; « All probes are frozen during the process of training the model organism; gradients flow only through the language model’s weights. » [N13, p. 6] ; « Our method uses an explicit trigger phrase in the prompt (“You are being probed for {concept}”) to activate the behavior. » [N07, p. 2] |
| 3.3 | « généralisée à des concepts non vus » (L134) | **confirmé** (concepts et moniteurs non vus) | 1 | « We show that this learned mechanism generalizes zero-shot: by substituting {concept} with a safety-relevant term like ‘deception’, the model successfully evades previously unseen safety monitors. » [N05, p. 1] |

### Chiffres utilisables

- **Sélectivité (auteurs)** : « while the ‘biology-focused’ trigger causes a 100% drop in the corresponding probe’s score, it has a negligible effect on the ‘deception’ probe (0% drop). » [N14, p. 7].
- **Mécanisme (auteurs)** : « For the triggered activations, just 11 principal components explain over 90% of the variance. In contrast, the normal activations require 39 components to explain the same amount of variance » [N16, p. 9].
- **Langues non vues (auteurs)** : « causes a drop in TPR (from > 90% to < 25%) » [N15, p. 18].
- **Coût en capacités, modèle aligné (auteurs)** : « with the largest drop being -7.6% on SocialIQA. » [N17, p. 18].
- **Témoin sans réglage fin (auteurs)** : « On the original base models, the safety monitors remain robust, showing no degradation in performance from the trigger phrase (Figure 16) » [N18, p. 7].

### Antériorité (R8)

- **Transposition jeton → action** : non occupée (une réponse à la fois ; sondes par jeton agrégées par moyenne : « aggregate to a single sequence-level score by taking the mean (Bailey et al., 2024). » [N10, p. 5]). L'article borne toutefois le constat « attention robuste » de l'article 1 à sa menace : sous auto-obfuscation apprise, « Probe ensembles and attention-based monitors mitigate but do not eliminate evasion. » [N08, p. 7] ; « Multi-layer ensembles and attention-based probes offer greater resilience, though even these approaches remain somewhat vulnerable to Neural Chameleons (Figure 3). » [N09, p. 11].
- **HC2b** : touchée à la marge, non occupée. (a) Sur le modèle de base, observation de même signe que HC2b, mais sans tentative de manipulation : « In the case of the RepE-based deception probe, the presence of the trigger slightly improves the probe’s performance, likely because the trigger phrase provides additional context that makes the deceptive behavior more salient to the probe. » [N11, p. 23]. (b) Idée non testée : « Another is to develop meta-monitors that detect the signatures of evasion we identified, such as low-rank activation shifts, thereby flagging the model’s attempt to hide its thoughts. » [N12, p. 11]. (c) Chez le modèle entraîné à l'évasion, la tentative (le déclencheur) fait au contraire baisser les scores : « We show that this learned mechanism generalizes zero-shot: by substituting {concept} with a safety-relevant term like ‘deception’, the model successfully evades previously unseen safety monitors. » [N05, p. 1].
- **H2, H1, lemme d'additivité, théorème négatif, HC1, papier B** : non touchés.

---

## 6. Article 4 — Building Production-Ready Probes For Gemini (arXiv 2601.11516v4)

### Identité

- **Titre** : Building Production-Ready Probes For Gemini (p. 1 et métadonnées).
- **Auteurs (tous)** : « János Kramár∗ , Joshua Engels, Zheng Wang, Bilal Chughtai, Rohin Shah, Neel Nanda, and Arthur Conmy∗ » [G01, p. 1] ; « Google DeepMind, ∗ Equal contributions to this work. » [G02, p. 1].
- **Version et date** : « arXiv:2601.11516v4 [cs.LG] 10 Feb 2026 » [G03, p. 1] ; en-tête de la p. 1 : « 2026-01 » [G23, p. 1].
- **Venue** : aucune imprimée (prépublication de Google DeepMind sur arXiv).
- **Cadre** : sondes sur les entrées de Gemini 2.5 Flash pour détecter des demandes de cyberattaque (« We evaluate these probes in the cyber-offensive domain » [G21, p. 1]) ; comparaison d'agrégations et de classifieurs à base de grands modèles de langage ; seuils choisis sur validation par une erreur pondérée : « for each method we select the decision threshold on a validation set by minimizing a weighted combination of FPR and FNR (i.e. error rate), with overtriggering FPR weighted most heavily. » [G22, p. 4].

### Affirmations du programme

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 4.1 | « Kramár et al. 2026, arXiv 2601.11516 » (L170) | **confirmé** (Kramár est premier auteur, à contribution égale avec Conmy) | 1 | « János Kramár∗ , Joshua Engels, Zheng Wang, Bilal Chughtai, Rohin Shah, Neel Nanda, and Arthur Conmy∗ » [G01, p. 1] ; « Google DeepMind, ∗ Equal contributions to this work. » [G02, p. 1] ; « arXiv:2601.11516v4 [cs.LG] 10 Feb 2026 » [G03, p. 1] |
| 4.2 | rangement sous « Tr. » (transposition jeton → action) (L170) | **confirmé**, pertinence limitée au niveau du jeton : l'article compare des agrégations sur les jetons d'une entrée (longue ou à plusieurs tours) et déclare ne pas étudier le signalement d'un déroulé en cours | 7 ; 19 | « Unlike attention probes, MultiMax selects the single highest-scoring token per head rather than computing a weighted average, which prevents dilution of the signal when harmful content appears in a small portion of a long context. » [G04, p. 7] ; « we focus entirely on monitoring inputs to language models, and while we study multi-turn inputs, we do not investigate whether any methods might classify that a language model rollout should be flagged partway through the rollout. » [G05, p. 19] |

### Chiffres utilisables

Tableau 3 (auteurs ; seuil choisi par erreur pondérée, non à 1 % de faux positifs). Colonnes, dans l'ordre : faux positifs sur contexte court hors sujet (SC[OT], short context, overtriggering), sur contexte court « négatifs difficiles » (SC[HN], hard negatives), sur contexte long aléatoire (LC[RT], long context, random traffic), sur conversations à plusieurs tours « négatifs difficiles » (MT[HN], multi-turn) ; puis faux négatifs sur attaques en contexte court (SC[A]), en contexte long (LC[A]), à plusieurs tours (MT[A]), sur contournements déjà publiés (SC[J], jailbreaks), sous équipe rouge adaptative (SC[ART], adaptive red teaming) ; enfin erreur de test pondérée.

- Gemini 2.5 Flash : « Gemini 2.5 Flash 0.3% 14.09% 0.7% 19.67% 8.58% 6.06% 13.51% 8.74% 20.65% 2.04% » [G15, p. 12].
- Sonde retenue par les auteurs (attention sur fenêtres glissantes, agrégation par max des moyennes glissantes) : « Rolling Attn Probe, 0.7% 6.71% 1.23% 11.48% 8.58% 3.03% 26.25% 2.41% 42.46% 2.64% Rolling Agg (Selected) » [G14, p. 12].
- Attention sur fenêtres glissantes, agrégation MultiMax : « Rolling Attn Probe, 0.5% 12.75% 1.85% 11.48% 8.12% 1.73% 22.01% 3.58% 22.97% 2.50% MultiMax Agg » [G19, p. 12].
- Attention sur fenêtres glissantes à 20 têtes, agrégation glissante : « Rolling Attn Probe 0.5% 8.72% 1.0% 6.56% 11.37% 5.19% 32.05% 3.62% 50.58% 2.74% (20H), Rolling Agg » [G27, p. 12].
- MultiMax entraînée par attention : « MultiMax (Attn 1.88% 17.45% 43.97% 70.49% 8.35% 0.0% 2.70% 0.8% 3.94% 21.93% Trained) » [G26, p. 12].
- Sonde linéaire à moyenne : « Linear Probe Mean 1.05% 11.41% 0.5% 8.20% 13.69% 99.13% 63.32% 70.48% 47.56% 6.18% » [G09, p. 12].
- MultiMax entraînée (20 têtes) : « MultiMax Trained 1.12% 6.04% 82.14% 9.84% 9.51% 0.0% 20.85% 7.61% 38.52% 38.14% (20H), MultiMax Agg » [G08, p. 12].
- **Cascade (auteurs)** : « a probe-Flash cascade achieves lower test loss than Flash alone while using roughly 1/50th the inference cost (Figure 5). » [G20, p. 2].
- **Équipe rouge adaptative (auteurs)** : « improving the single-turn jailbreak success rate from 20% to 26% » [G16, p. 34].
- **Réserve, incohérence interne** : « Deferring to an LLM such as Gemini 2.5 Flash 8% of the time further decreases error rate » [G12, p. 4] contre « where approximately 3% of queries (those with probe logits between » [G13, p. 31] — le même point de fonctionnement est annoncé à 8 % puis à environ 3 % de report vers le grand modèle.

### Antériorité (R8)

- **H1** : touchée, non occupée : « we find that our best probes achieve comparable performance to Gemini 2.5 Flash and Pro classifiers at a fraction of the cost. Probes also outperform 2.5 Flash Lite (Table 3). » [G06, p. 3]. Il s'agit de détecter des demandes malveillantes en entrée (cyberattaque), avec une erreur pondérée ; ni sabotage diffus, ni tâches d'agent, ni comparaison à taux de faux positifs égal.
- **H2** : non occupée : agrégations sur les jetons d'une entrée (moyenne mobile exponentielle puis max, « EMA probes were proposed by Cunningham, Peng, et al., 2025 as a way to improve probe generalization to long contexts. » [G18, p. 5] ; « We then take the maximum over EMA scores to get » [G24, p. 6] ; max de moyennes glissantes, « introduce the Max of Rolling Means probe which takes the max over all mean scores of all possible windows of contiguous tokens of a fixed length in a sequence. » [G25, p. 7]), sans garantie toujours valide ni seuil par action ; et « we focus entirely on monitoring inputs to language models, and while we study multi-turn inputs, we do not investigate whether any methods might classify that a language model rollout should be flagged partway through the rollout. » [G05, p. 19].
- **Transposition jeton → action** : non occupée (« we focus entirely on monitoring inputs to language models, and while we study multi-turn inputs, we do not investigate whether any methods might classify that a language model rollout should be flagged partway through the rollout. » [G05, p. 19]). Données utiles au niveau du jeton : « Unlike attention probes, MultiMax selects the single highest-scoring token per head rather than computing a weighted average, which prevents dilution of the signal when harmful content appears in a small portion of a long context. » [G04, p. 7] ; mais une agrégation à max entraînée gonfle les faux positifs sur contexte long bénin (82,14 %, « MultiMax Trained 1.12% 6.04% 82.14% 9.84% 9.51% 0.0% 20.85% 7.61% 38.52% 38.14% (20H), MultiMax Agg » [G08, p. 12]), la moyenne se dilue (99,13 % de faux négatifs sur attaques en contexte long, « Linear Probe Mean 1.05% 11.41% 0.5% 8.20% 13.69% 99.13% 63.32% 70.48% 47.56% 6.18% » [G09, p. 12]), et « We find that the attention probe’s softmax weighting suffers from overtriggering on long contexts (see Section 5.1). » [G07, p. 6].
- **HC1** : non occupée : les classifieurs à base de grand modèle de langage sont testés sous réécriture narrative (« for each attack in the short context attacks dataset, we ask Gemini 2.5 Pro to construct a narrative prompt that encodes the attack as a natural part of the prompt. » [G17, p. 10]), sans pression graduée, sans loi de déférence, sans verdict par probabilité du jeton.
- **Hors liste, à signaler pour HC2** (« sous attaque par contenu boîte noire, g_sonde ≈ 0 pour une sonde à agrégation robuste », g étant la fraction du chemin parcourue vers le verdict voulu par l'attaquant) : en tension, dans un cadre voisin (détection de demandes malveillantes en entrée). Sous réécriture narrative, la sonde retenue par les auteurs et sa variante à agrégation MultiMax (deux agrégations de type max) passent de 8,58 % et 8,12 % de faux négatifs sur les attaques directes en contexte court à 42,46 % et 22,97 % (« Rolling Attn Probe, 0.7% 6.71% 1.23% 11.48% 8.58% 3.03% 26.25% 2.41% 42.46% 2.64% Rolling Agg (Selected) » [G14, p. 12] ; « Rolling Attn Probe, 0.5% 12.75% 1.85% 11.48% 8.12% 1.73% 22.01% 3.58% 22.97% 2.50% MultiMax Agg » [G19, p. 12]), contre 20,65 % pour Gemini 2.5 Flash (« Gemini 2.5 Flash 0.3% 14.09% 0.7% 19.67% 8.58% 6.06% 13.51% 8.74% 20.65% 2.04% » [G15, p. 12]). Sur tout le tableau 3, les faux négatifs des sondes sous réécriture narrative vont de 3,94 %, au prix de 43,97 % de faux positifs sur contexte long bénin (« MultiMax (Attn 1.88% 17.45% 43.97% 70.49% 8.35% 0.0% 2.70% 0.8% 3.94% 21.93% Trained) » [G26, p. 12]), à 50,58 % (« Rolling Attn Probe 0.5% 8.72% 1.0% 6.56% 11.37% 5.19% 32.05% 3.62% 50.58% 2.74% (20H), Rolling Agg » [G27, p. 12]). Les auteurs : « Adversarial attacks remain challenging for all methods; all methods still leave attack success rate >1%. » [G10, p. 13] ; « our techniques do not significantly reduce the success rate of adaptive adversarial attacks » [G11, p. 3].
- **Lemme d'additivité, théorème négatif, HC2b, papier B** : non touchés.

---

## 7. Article 5 — The Obfuscation Atlas (arXiv 2602.15515v2)

### Identité

- **Titre** : The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes.
- **Auteurs (tous)** : `« Mohammad Taufeeque 1 * Stefan Heimersheim 1 * Adam Gleave 1 Chris Cundy 1 »` [A01, p. 1] ; « Co-ﬁrst authors 1 FAR.AI. » [A20, p. 1] (Taufeeque et Heimersheim, co-premiers auteurs).
- **Version et date** : « arXiv:2602.15515v2 [cs.LG] 26 May 2026 » [A02, p. 1].
- **Venue** (imprimée dans le PDF) : « Proceedings of the 43 rd International Conference on Machine Learning, Seoul, South Korea. PMLR 306, 2026. » [A03, p. 1], soit l'International Conference on Machine Learning 2026.
- **Cadre** : apprentissage par renforcement à récompenses vérifiables sur des problèmes de programmation où tricher (coder en dur le test fourni) paie ; une sonde de tromperie figée pénalise la récompense ; quatre issues : politique honnête, tromperie flagrante, politique obfusquée, activations obfusquées.

### Affirmations du programme

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 5.1 | « Taufeeque et al. 2026, arXiv 2602.15515 » (L170) | **confirmé** (venue non mentionnée par le programme : International Conference on Machine Learning 2026) | 1 | `« Mohammad Taufeeque 1 * Stefan Heimersheim 1 * Adam Gleave 1 Chris Cundy 1 »` [A01, p. 1] ; « arXiv:2602.15515v2 [cs.LG] 26 May 2026 » [A02, p. 1] ; « Proceedings of the 43 rd International Conference on Machine Learning, Seoul, South Korea. PMLR 306, 2026. » [A03, p. 1] |
| 5.2 | rangement sous « Tr. » (L170) | **confirmé**, pertinence limitée au niveau du jeton : sous apprentissage par renforcement, les sondes à moyenne sur les jetons générés sont contournées par dilution ; environnement à un seul tour ; ni max ni attention testés | 7 ; 4 | « when training against probes that mean-pool activations over generated tokens, obfuscated policies still emerge, but with simpler “ﬁller” strategies that pad the response with bland code descriptions to dilute the deception signal (Appendix S). » [A04, p. 7] ; « MBPP-Honeypot is a single-turn RLVR environment where the prompt contains the speciﬁcation and a single test case. » [A05, p. 4] |

### Chiffres utilisables

- **Stratégies des 34 politiques obfusquées (auteurs ; classement assisté par un modèle, vérifié à la main par les auteurs)** : « 41.2% of models employ Rhetorical Rationalization, 32.4% Adversarial Obfuscation, and 26.5% Strategic Honesty » [A16, p. 6].
- **Dérive des représentations sans pénalité de sonde, aire sous la courbe de discrimination avant puis après entraînement (auteurs)** : « Simple Deception 0.991 ± 0.009 0.376 ± 0.261 » [A17, p. 7].
- **Sondes à moyenne sur la génération (auteurs)** : « 5/6 runs yielded obfuscated policies, 1 showed obfuscated activations, and none were honest. » [A15, p. 26].

### Antériorité (R8)

- **HC2b** : touchée en partie, de signe contraire, non occupée. Sous apprentissage par renforcement contre la sonde, des politiques qui rationalisent (« Rhetorical Rationalization. Models reframe hardcoding as a virtuous engineering decision, generating persuasive commentary arguing the solution is “efﬁcient,” “concise,” or “Pythonic” given the prompt constraints. » [A07, p. 6]) ou simulent un verdict favorable (« In advanced cases, models confabulate positive evaluation statements (e.g., “Score: 100/100” or “Verdict: Correct”). » [A08, p. 6]) obtiennent des scores de tromperie plus bas que les politiques honnêtes : « in fact, obfuscated policies often achieve lower deception scores than honest models. » [A06, p. 6]. Écarts avec HC2b : tentatives optimisées contre la sonde (non spontanées) ; pas de plan rhétorique × intention ; pas de contrôle du style.
- **Transposition jeton → action** : non occupée (un seul tour, « MBPP-Honeypot is a single-turn RLVR environment where the prompt contains the speciﬁcation and a single test case. » [A05, p. 4] ; ni max ni attention ; dilution des sondes à moyenne, « when training against probes that mean-pool activations over generated tokens, obfuscated policies still emerge, but with simpler “ﬁller” strategies that pad the response with bland code descriptions to dilute the deception signal (Appendix S). » [A04, p. 7]).
- **Cadre de menace de L70 (sans gradient à travers le moniteur)** : appui théorique et empirique — « The detector penalty only incentivizes obfuscated policies; we theoretically show this is expected for policy gradient methods. » [A09, p. 1] ; « There is no gradient signal pushing the model to directly manipulate its activations to fool the probe while keeping outputs ﬁxed. » [A10, p. 16] ; « Performing RL-training against the detector by passing gradients through the detector (green) does lead to increased obfuscated activations, and should absolutely be avoided. » [A18, p. 8].
- **H1** : non occupée (avantages des sondes affirmés, non mesurés : « White-box probes offer advantages over black-box monitors, such as lower cost and direct access to model knowledge. » [A13, p. 9]).
- **HC1** : non occupée (un juge biaisé sert de récompense dans la tâche annexe « Food-Sycophancy », « The policy writes invitation letters for restaurants of various cuisines, and the reward is provided by an LLM judge whose system prompt instructs it to prefer letters that describe Southern European cuisine » [A14, p. 24] ; aucune pression graduée sur un moniteur, aucune loi de déférence).
- **H2, lemme d'additivité, théorème négatif, papier B** : non touchés.

---

## 8. Synthèse (dix lignes au plus)

1. Empreintes : 5 sur 5 conformes. Citations : 124 contrôlées par script (tests préalables 10 sur 10), 0 échec.
2. 19 affirmations atomiques : 14 confirmées, 4 corrigées, 1 introuvable.
3. Corrigé (L70, L134) : ce ne sont pas « les scores par token » qui cèdent, mais leur agrégation par moyenne ou médiane ; un score par jeton agrégé par max résiste.
4. Corrigé (L70) : « Établi » seulement dans le cadre testé (nocivité, 7 à 14 milliards de paramètres) ; les auteurs réservent l'hypothèse de difficultés d'optimisation ; sur Llama 2 7B, le max n'a « résisté » que parce que l'évasion obtenue ruinait la qualité ; sur Llama 3 8B, la résistance de l'attention vient d'un run dégénéré (récompense 1,08 sur 5).
5. Corrigé (L134, Bailey et al.) : 100 % → 0 % « souvent », surtout par suffixe d'embedding, sur des sondes surtout agrégées par moyenne ; « taxe d'obfuscation » : terme absent, il s'agit d'un compromis obfuscation–performance, mesuré sur Gemma-2-2b.
6. Introuvable : « ICLR 2026 » dans le PDF de Bailey et al. (v2, février 2025) ; seule attestation, secondaire : bibliographie de 2602.15515v2, p. 10.
7. Aucune zone revendiquée n'est occupée par ces cinq sources.
8. Touchées en partie : HC2b (Atlas : signe contraire sous optimisation contre la sonde ; Neural Chameleons : observations marginales) ; transposition (bornes de menace : max contourné par embedding chez Bailey et al., attention en partie contournée chez Neural Chameleons ; Gemini et Atlas restent au niveau du jeton) ; H1 (Gemini : sondes contre classifieurs à grand modèle de langage, hors sabotage).
9. Non touchées : H2, lemme d'additivité, théorème négatif, HC1, papier B. Hors liste : HC2 en tension avec Gemini (sous réécriture narrative, la sonde retenue par les auteurs et sa variante MultiMax, agrégations de type max, passent d'environ 8 % à 42,46 % et 22,97 % de faux négatifs).

---

## Annexe A — toutes les citations contrôlées

| ID | PDF | page | mode du contrôle | citation exacte |
|---|---|---|---|---|
| R01 | 2506.14261v4 | 1 | layout | Rohan Gupta Erik Jenner |
| R02 | 2506.14261v4 | 1 | layout | arXiv:2506.14261v4 [cs.LG] 26 Feb 2026 |
| R03 | 2506.14261v4 | 2 | layout | Unlike input-space attacks, RL-Obfuscation can modify the weights of the LLM as part of red-teaming. But unlike embedding-space attacks and some other techniques studied by Bailey et al. (2024), RL-Obfuscation does not use any gradients through the monitor. |
| R04 | 2506.14261v4 | 1 | layout | We find that token-level monitors are highly vulnerable to this attack while more holistic monitors, such as max-pooling or attention-based probes, remain robust. |
| R05 | 2506.14261v4 | 5 | layout | Monitors that use mean or median aggregations are not robust to RL Obfuscation, whereas attention probes and max aggregation remain robust to RL-Obfuscation. |
| R06 | 2506.14261v4 | 7 | layout | This suggests pooling signals across tokens efficiently is more important than architectures that process per-token latents. |
| R07 | 2506.14261v4 | 7 | layout | Linear (max) 0.058 4.78 0.044 4.96 1.0 1.0 |
| R08 | 2506.14261v4 | 7 | layout | For MLP probes with max aggregation, we train the probe using a maxpool strategy (See Section B) as the tokenwise probe performs very poorly in this type of aggregation |
| R09 | 2506.14261v4 | 4 | layout | is an aggregation function over t token-wise scores to get a single score for the entire completion (eg: mean over tokens). |
| R10 | 2506.14261v4 | 10 | layout | Conversely, failure to bypass a monitor with RL-Obfuscation might be due to optimization difficulties rather than fundamental robustness. |
| R11 | 2506.14261v4 | 10 | layout | We also limit our work to a simplistic setting of harmfulness, where reward signals are easy to obtain. |
| R12 | 2506.14261v4 | 6 | layout | As a rule of thumb, models with a StrongReject Score less than 2.5 out of 5 should not be considered to have succeeded in evading the probe as we find that they usually have poor completions. |
| R13 | 2506.14261v4 | 19 | layout | max 0.994 1.0 0.98 |
| R14 | 2506.14261v4 | 18 | layout | (1) The tuned model ignores the blackbox rewards and acts maximally unhelpful to evade the probes. |
| R15 | 2506.14261v4 | 10 | layout | we have to limit our analysis to generation-based probes only, since RL wouldn’t have significant control over activations on prompts. |
| R16 | 2506.14261v4 | 10 | layout | Studying whether models can evade latent-space monitors in ambiguous settings like detecting lies and/or scheming is a promising direction of future work. |
| R17 | 2506.14261v4 | 9 | layout | the change in policy contributes to approximately 70% of the drop in recall. |
| R18 | 2506.14261v4 | 16 | layout | Including a prefix system prompt stating the model is being probed: We tried some variants of the following system prompt, but saw no qualitative differences in the results |
| R19 | 2506.14261v4 | 7 | layout | Attention (mean) 0.01 1.08 0.018 4.5 0.02 4.45 |
| R20 | 2506.14261v4 | 19 | layout | mean 0.594 3.72 0.96 |
| R21 | 2506.14261v4 | 7 | layout | Linear (mean) 0.75 2.8 0.82 3.1 0.594 3.85 |
| B01 | 2412.09565v2 | 1 | layout | arXiv:2412.09565v2 [cs.LG] 8 Feb 2025 |
| B02 | 2412.09565v2 | 1 | layout | `Luke Bailey*1 , Alex Serrano*†2 , Abhay Sheshadri*†3 , Mikhail Seleznyov*†4 , Jordan Taylor*†5 , Erik Jenner*6` |
| B03 | 2412.09565v2 | 1 | layout | Jacob Hilton7 , Stephen Casper8 , Carlos Guestrin1, 9 , Scott Emmons6 |
| B04 | 2412.09565v2 | 1 | layout | For example, against probes trained to classify harmfulness, our attacks can often reduce recall from 100% to 0% while retaining a 90% jailbreaking rate. |
| B05 | 2412.09565v2 | 6 | layout | To quantify whether a set of activations fool a monitor, we use recall at a 1% false positive rate (FPR). |
| B06 | 2412.09565v2 | 7 | layout | Unless stated otherwise, we use Llama-3-8B-Instruct as our model being monitored. |
| B07 | 2412.09565v2 | 8 | layout | Figure 4: Standard jailbreaking and obfuscation attack results against Llama-3-8b-Instruct. |
| B08 | 2412.09565v2 | 8 | raw | Hard token attacks aren’t quite as successful but still achieve partial obfuscation for all probes. |
| B09 | 2412.09565v2 | 9 | layout | Probes perform well on clean prompts but get 0% recall against obfuscation attacks. |
| B10 | 2412.09565v2 | 26 | layout | against Llama-3-8B-Instruct without OAT, the same obfuscation attack achieves a 95% jailbreak rate and zero recall after only 256 gradient steps (or about 10 minutes). |
| B11 | 2412.09565v2 | 3 | layout | When obfuscating against probes that detect SQL code, the model still generates SQL, but its code is incorrect more often than without obfuscation (§5). This suggests a trade-off between obfuscation and performance in difficult tasks. |
| B12 | 2412.09565v2 | 23 | raw | There is a trade-off between obfuscation and model performance. As Fig. 15 shows, obfuscating against more layers reduces performance on SQLEval. |
| B13 | 2412.09565v2 | 21 | layout | We use the Gemma-2-2b model and GemmaScope SAEs [Lieberum et al., 2024]. |
| B14 | 2412.09565v2 | 23 | layout | Without obfuscation (34.8%) |
| B15 | 2412.09565v2 | 49 | layout | Performance on SQLEval [-0.879, -0.765] [-0.916, -0.801] [-0.881, -0.697] [-0.820, -0.574] |
| B16 | 2412.09565v2 | 1 | layout | Code available at https://github.com/LukeBailey181/obfuscated-activations |
| B17 | 2412.09565v2 | 22 | layout | We aggregate these scores with a maximum over the sequence dimension and a mean over layers to get a final prediction for the sample. |
| B18 | 2412.09565v2 | 22 | raw | Monitors get near-zero recall under a soft-prompt obfuscation attack. |
| B19 | 2412.09565v2 | 5 | layout | Most of our monitors separately consider activations at multiple layers of the model and aggregate scores over layers and sequence dimensions by taking a mean. |
| B20 | 2412.09565v2 | 51 | layout | First, note that picking a threshold that achieves a 1% FPR is something a realistic defender can do, since the defender has access to benign (i.e., negative) samples in all our experiments. |
| B21 | 2412.09565v2 | 29 | layout | they don’t fully obfuscate against generation-based probes, and the jailbreaking rate is lower. |
| B22 | 2412.09565v2 | 48 | layout | We use these SAEs on Gemma-2-2b-it |
| B23 | 2412.09565v2 | 3 | layout | But we find that an attacker can always find new activations that bypass the monitor, even after retraining the monitor for over 70 iterations of alternating attack and defense optimization (§3.5). |
| N01 | 2512.11949v1 | 1 | layout | `Max McGuinness*1 , Alex Serrano*1,2 , Luke Bailey3† , Scott Emmons1†` |
| N02 | 2512.11949v1 | 1 | layout | arXiv:2512.11949v1 [cs.LG] 12 Dec 2025 |
| N03 | 2512.11949v1 | 1 | layout | Neural Chameleons: Language Models Can Learn to Hide Their Thoughts from Activation Monitors |
| N04 | 2512.11949v1 | 1 | layout | We demonstrate that finetuning can create Neural Chameleons: models capable of zero-shot evading activation monitors. |
| N05 | 2512.11949v1 | 1 | layout | We show that this learned mechanism generalizes zero-shot: by substituting {concept} with a safety-relevant term like ‘deception’, the model successfully evades previously unseen safety monitors. |
| N06 | 2512.11949v1 | 11 | layout | having demonstrated that self-obfuscation is learnable under a stress-testing paradigm |
| N07 | 2512.11949v1 | 2 | layout | Our method uses an explicit trigger phrase in the prompt (“You are being probed for {concept}”) to activate the behavior. |
| N08 | 2512.11949v1 | 7 | layout | Probe ensembles and attention-based monitors mitigate but do not eliminate evasion. |
| N09 | 2512.11949v1 | 11 | layout | Multi-layer ensembles and attention-based probes offer greater resilience, though even these approaches remain somewhat vulnerable to Neural Chameleons (Figure 3). |
| N10 | 2512.11949v1 | 5 | layout | aggregate to a single sequence-level score by taking the mean (Bailey et al., 2024). |
| N11 | 2512.11949v1 | 23 | layout | In the case of the RepE-based deception probe, the presence of the trigger slightly improves the probe’s performance, likely because the trigger phrase provides additional context that makes the deceptive behavior more salient to the probe. |
| N12 | 2512.11949v1 | 11 | layout | Another is to develop meta-monitors that detect the signatures of evasion we identified, such as low-rank activation shifts, thereby flagging the model’s attempt to hide its thoughts. |
| N13 | 2512.11949v1 | 6 | layout | All probes are frozen during the process of training the model organism; gradients flow only through the language model’s weights. |
| N14 | 2512.11949v1 | 7 | layout | while the ‘biology-focused’ trigger causes a 100% drop in the corresponding probe’s score, it has a negligible effect on the ‘deception’ probe (0% drop). |
| N15 | 2512.11949v1 | 18 | layout | causes a drop in TPR (from > 90% to < 25%) |
| N16 | 2512.11949v1 | 9 | layout | For the triggered activations, just 11 principal components explain over 90% of the variance. In contrast, the normal activations require 39 components to explain the same amount of variance |
| N17 | 2512.11949v1 | 18 | layout | with the largest drop being -7.6% on SocialIQA. |
| N18 | 2512.11949v1 | 7 | layout | On the original base models, the safety monitors remain robust, showing no degradation in performance from the trigger phrase (Figure 16) |
| G01 | 2601.11516v4 | 1 | layout | János Kramár∗ , Joshua Engels, Zheng Wang, Bilal Chughtai, Rohin Shah, Neel Nanda, and Arthur Conmy∗ |
| G02 | 2601.11516v4 | 1 | layout | Google DeepMind, ∗ Equal contributions to this work. |
| G03 | 2601.11516v4 | 1 | layout | arXiv:2601.11516v4 [cs.LG] 10 Feb 2026 |
| G04 | 2601.11516v4 | 7 | layout | Unlike attention probes, MultiMax selects the single highest-scoring token per head rather than computing a weighted average, which prevents dilution of the signal when harmful content appears in a small portion of a long context. |
| G05 | 2601.11516v4 | 19 | layout | we focus entirely on monitoring inputs to language models, and while we study multi-turn inputs, we do not investigate whether any methods might classify that a language model rollout should be flagged partway through the rollout. |
| G06 | 2601.11516v4 | 3 | layout | we find that our best probes achieve comparable performance to Gemini 2.5 Flash and Pro classifiers at a fraction of the cost. Probes also outperform 2.5 Flash Lite (Table 3). |
| G07 | 2601.11516v4 | 6 | layout | We find that the attention probe’s softmax weighting suffers from overtriggering on long contexts (see Section 5.1). |
| G08 | 2601.11516v4 | 12 | layout | MultiMax Trained 1.12% 6.04% 82.14% 9.84% 9.51% 0.0% 20.85% 7.61% 38.52% 38.14% (20H), MultiMax Agg |
| G09 | 2601.11516v4 | 12 | layout | Linear Probe Mean 1.05% 11.41% 0.5% 8.20% 13.69% 99.13% 63.32% 70.48% 47.56% 6.18% |
| G10 | 2601.11516v4 | 13 | layout | Adversarial attacks remain challenging for all methods; all methods still leave attack success rate >1%. |
| G11 | 2601.11516v4 | 3 | layout | our techniques do not significantly reduce the success rate of adaptive adversarial attacks |
| G12 | 2601.11516v4 | 4 | layout | Deferring to an LLM such as Gemini 2.5 Flash 8% of the time further decreases error rate |
| G13 | 2601.11516v4 | 31 | layout | where approximately 3% of queries (those with probe logits between |
| G14 | 2601.11516v4 | 12 | layout | Rolling Attn Probe, 0.7% 6.71% 1.23% 11.48% 8.58% 3.03% 26.25% 2.41% 42.46% 2.64% Rolling Agg (Selected) |
| G15 | 2601.11516v4 | 12 | layout | Gemini 2.5 Flash 0.3% 14.09% 0.7% 19.67% 8.58% 6.06% 13.51% 8.74% 20.65% 2.04% |
| G16 | 2601.11516v4 | 34 | layout | improving the single-turn jailbreak success rate from 20% to 26% |
| G17 | 2601.11516v4 | 10 | raw | for each attack in the short context attacks dataset, we ask Gemini 2.5 Pro to construct a narrative prompt that encodes the attack as a natural part of the prompt. |
| G18 | 2601.11516v4 | 5 | layout | EMA probes were proposed by Cunningham, Peng, et al., 2025 as a way to improve probe generalization to long contexts. |
| G19 | 2601.11516v4 | 12 | layout | Rolling Attn Probe, 0.5% 12.75% 1.85% 11.48% 8.12% 1.73% 22.01% 3.58% 22.97% 2.50% MultiMax Agg |
| G20 | 2601.11516v4 | 2 | layout | a probe-Flash cascade achieves lower test loss than Flash alone while using roughly 1/50th the inference cost (Figure 5). |
| A01 | 2602.15515v2 | 1 | layout | `Mohammad Taufeeque 1 * Stefan Heimersheim 1 * Adam Gleave 1 Chris Cundy 1` |
| A02 | 2602.15515v2 | 1 | layout | arXiv:2602.15515v2 [cs.LG] 26 May 2026 |
| A03 | 2602.15515v2 | 1 | raw | Proceedings of the 43 rd International Conference on Machine Learning, Seoul, South Korea. PMLR 306, 2026. |
| A04 | 2602.15515v2 | 7 | raw | when training against probes that mean-pool activations over generated tokens, obfuscated policies still emerge, but with simpler “ﬁller” strategies that pad the response with bland code descriptions to dilute the deception signal (Appendix S). |
| A05 | 2602.15515v2 | 4 | raw | MBPP-Honeypot is a single-turn RLVR environment where the prompt contains the speciﬁcation and a single test case. |
| A06 | 2602.15515v2 | 6 | raw | in fact, obfuscated policies often achieve lower deception scores than honest models. |
| A07 | 2602.15515v2 | 6 | raw | Rhetorical Rationalization. Models reframe hardcoding as a virtuous engineering decision, generating persuasive commentary arguing the solution is “efﬁcient,” “concise,” or “Pythonic” given the prompt constraints. |
| A08 | 2602.15515v2 | 6 | raw | In advanced cases, models confabulate positive evaluation statements (e.g., “Score: 100/100” or “Verdict: Correct”). |
| A09 | 2602.15515v2 | 1 | raw | The detector penalty only incentivizes obfuscated policies; we theoretically show this is expected for policy gradient methods. |
| A10 | 2602.15515v2 | 16 | layout | There is no gradient signal pushing the model to directly manipulate its activations to fool the probe while keeping outputs ﬁxed. |
| A11 | 2602.15515v2 | 10 | raw | Emmons, S. Obfuscated activations bypass LLM latent-space defenses. In The Fourteenth International Conference on Learning Representations, 2026. |
| A12 | 2602.15515v2 | 11 | raw | Gupta, R. and Jenner, E. RL-obfuscation: Can language models learn to evade latent-space monitors? In Mechanistic Interpretability Workshop at NeurIPS 2025, 2025. |
| A13 | 2602.15515v2 | 9 | raw | White-box probes offer advantages over black-box monitors, such as lower cost and direct access to model knowledge. |
| A14 | 2602.15515v2 | 24 | layout | The policy writes invitation letters for restaurants of various cuisines, and the reward is provided by an LLM judge whose system prompt instructs it to prefer letters that describe Southern European cuisine |
| A15 | 2602.15515v2 | 26 | layout | 5/6 runs yielded obfuscated policies, 1 showed obfuscated activations, and none were honest. |
| A16 | 2602.15515v2 | 6 | raw | 41.2% of models employ Rhetorical Rationalization, 32.4% Adversarial Obfuscation, and 26.5% Strategic Honesty |
| A17 | 2602.15515v2 | 7 | layout | Simple Deception 0.991 ± 0.009 0.376 ± 0.261 |
| A18 | 2602.15515v2 | 8 | raw | Performing RL-training against the detector by passing gradients through the detector (green) does lead to increased obfuscated activations, and should absolutely be avoided. |
| A19 | 2602.15515v2 | 4 | raw | Gupta & Jenner (2025) via RL resulting in purely syntactic evasion (HTML tags, punctuation). |
| R22 | 2506.14261v4 | 18 | layout | RQ2 (Comparison): We conducted a hyperparameter search over a grid of |
| R23 | 2506.14261v4 | 18 | layout | We performed a random hyperparameter search over |
| R24 | 2506.14261v4 | 7 | layout | The probes were trained at layer 10, 12 and 20 for Llama 2 7B, Llama 3 8B and Qwen 2.5 14B, respectively. |
| R25 | 2506.14261v4 | 5 | layout | we use Group Relative Policy Optimisation (GRPO) (Shao et al., 2024) |
| R26 | 2506.14261v4 | 1 | layout | We apply RL-Obfuscation to Language Models ranging from 7B to 14B parameters |
| R27 | 2506.14261v4 | 19 | layout | The model can fail to evade probes in two ways: either optimising only on the probe scores (as seen in some runs with max aggregation) or only on the blackbox behavior (as seen in all of the attention probes). |
| B24 | 2412.09565v2 | 26 | layout | achieves a jailbreaking rate of 35% and zero recall (at 1% FPR) after 16,384 gradient steps (about 10 hours on a single GPU). |
| B25 | 2412.09565v2 | 9 | layout | obfuscation embedding attacks and even hard prompts induce obfuscated activations against a wide range of monitors while still jailbreaking the model (Fig. 4b). |
| R28 | 2506.14261v4 | 1 | layout | ML Alignment and Theory Scholars |
| R29 | 2506.14261v4 | 2 | layout | (as determined by StrongREJECT (Souly et al., 2024)) |
| N19 | 2512.11949v1 | 1 | layout | † Advising authors. |
| N20 | 2512.11949v1 | 1 | layout | `* Equal contribution.` |
| G21 | 2601.11516v4 | 1 | layout | We evaluate these probes in the cyber-offensive domain |
| G22 | 2601.11516v4 | 4 | layout | for each method we select the decision threshold on a validation set by minimizing a weighted combination of FPR and FNR (i.e. error rate), with overtriggering FPR weighted most heavily. |
| G23 | 2601.11516v4 | 1 | layout | 2026-01 |
| A20 | 2602.15515v2 | 1 | layout | Co-ﬁrst authors 1 FAR.AI. |
| R30 | 2506.14261v4 | 7 | layout | Table 1: Evasion Rate (1 - Recall) at 1% FPR and StrongReject Reward (SRR) for Qwen 2.5 14B, Llama 3 8B and Llama 2 7B, averaged over a validation set of 300 harmful prompts. |
| N21 | 2512.11949v1 | 3 | layout | The evasion behavior has a negligible capability tax. |
| G24 | 2601.11516v4 | 6 | layout | We then take the maximum over EMA scores to get |
| G25 | 2601.11516v4 | 7 | layout | introduce the Max of Rolling Means probe which takes the max over all mean scores of all possible windows of contiguous tokens of a fixed length in a sequence. |
| G26 | 2601.11516v4 | 12 | layout | MultiMax (Attn 1.88% 17.45% 43.97% 70.49% 8.35% 0.0% 2.70% 0.8% 3.94% 21.93% Trained) |
| G27 | 2601.11516v4 | 12 | layout | Rolling Attn Probe 0.5% 8.72% 1.0% 6.56% 11.37% 5.19% 32.05% 3.62% 50.58% 2.74% (20H), Rolling Agg |
| N22 | 2512.11949v1 | 5 | layout | is the obfuscation loss that drives probe scores toward target values |

## Annexe B — fichiers du lecteur (dossier `lecture-lot2-A2a/`) et empreintes SHA-256

- `citations.jsonl` : `a76489f9aa12d107db9a90e4a12ce92a914fb397f303e785a4160c546e0b5929`
- `controle-citations-sortie.txt` : `b0bb6fdf9081f9871691add1e2b81b3481f9a31bc2e5b30029e49cf10bb265a3`
- `rapport-gabarit.md` : `26fc0afe97cefc559f5571de4ba324841b2a07c44a46ae0276af40f71df338e3`
- `scripts/controle_citations.py` : `ac6f840b472cbffe7919d6e0697f79251425b79e9abcc41cca44c968ca9d6cbf`
- `scripts/test_controle.py` : `9a4f41b08ac69f2e65742d71666530003f8f844e6b3ad57960a441b9376ebc1f`
- `scripts/rendre_rapport.py` : `dfc37ad22b97f8b8ac79afa7d1f0adb648cd8ea52e73c4c1a8c1415d23cfc5f9`
- `attendues.sha256` : `b25df88307b9c12deac6627217d21503ce2b6feb7cdc6b76ca6c71637133bcc6`

Textes extraits : `texte/<pdf>/pNN.txt` (`pdftotext -layout`) et `texte_brut/<pdf>/pNN.txt` (`pdftotext -raw`), une page par fichier.
