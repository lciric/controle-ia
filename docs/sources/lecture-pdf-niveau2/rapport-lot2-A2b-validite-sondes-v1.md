# Lecture de niveau 2 — lot 2 — A2b « validité des sondes » — rapport v1

## En-tête

- **Lecteur** : sous-agent neuf (Claude Opus 5.5), auteur d'aucun des textes vérifiés.
- **Date** : 6 octobre 2026, 16 h 42 en temps universel coordonné (UTC), version finale ; empreintes des PDF vérifiées à 16 h 15 UTC.
- **Consignes appliquées** :
  - `/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/lot2/consigne-commune.md`, sha256 `d44580525a20b31b5ff98d6117ffd09a7395e56b4f311c71cd20d3e7acffd9ab` ;
  - `/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/lot2/consignes-A2b-validite-sondes.md`, sha256 `d05db690824995e45cf9f267649e2776d39d385893d1495da0f63f01d95b4cdb`.
- **Règles** : R7 (rien d'opposable sans PDF empreinté, page et citation exacte) ; R8 (une limite d'un papier n'est pas un trou du champ : je dis seulement ce que ces sources occupent ou non).
- **Rien n'a été modifié** sous `/home/user/controle-ia` (lecture seule des PDF et de trois documents du programme pour situer les affirmations).

### PDF lus et empreintes

Dossier : `/home/user/controle-ia/docs/sources/pdf/`. Vérification par `sha256sum -c` : 6 fichiers « OK », code de retour 0. Aucune empreinte ne diffère.

| Fichier | Pages | Empreinte sha256 (attendue = obtenue) | Lecture |
|---|---|---|---|
| 2509.26238v4.pdf | 38 | `7cd297e7eb2500980caa23d88410a20f0d6c10b90e787b28070afa14e891a962` | partielle, détail en section 1 |
| 2605.27958v1.pdf | 18 | `43f55118822b378d950255b10aa68379fdb24a1431bba7e8721aacaf44d856e0` | intégrale |
| 2502.03407v1.pdf | 35 | `a4820ad59ef9b294609aa11cbcc044c27835d5f433d7e79d6ae374f874bc2e2b` | intégrale (bibliographie survolée) |
| 2606.07612v1.pdf | 25 | `3cc173e5688dbd88d51e091cb9bafcaabe62e2a87349ae67f3aa27223b0ff7d1` | intégrale |
| 2511.00554v1.pdf | 16 | `17708292f357ddeea469f1157c1ab72c77471b70293d17c2f00409b11aabc75f` | intégrale |
| 2609.24967v2.pdf | 53 | `95127141d5d92c720d5e95b7cd151b72e3a760b3283b5681f9fc1c4676d5d37b` | partielle, détail en section 6 |

### Méthode

- **Pages** : rang dans le fichier. Texte extrait page par page par `pdftotext -layout` (poppler 24.02.0) ; pour les pages à deux colonnes, la même page est aussi extraite en `pdftotext -raw` (ordre du flux, coupures et traits d'union conservés) et en mode par défaut (ordre de lecture).
- **Citations** : en anglais, mot pour mot, entre guillemets droits ; le texte français est entre « ». Chaque citation est contrôlée par script sur la page indiquée (bilan en fin de rapport).
- **Nature des chiffres** : « auteurs » = imprimé dans le texte ou un tableau ; « figure » = lu sur une figure ; « calcul » = calculé ou comparé par moi. Aucun chiffre lu seulement sur une image n'est utilisé.
- **Abréviations développées** : AUROC = aire sous la courbe de caractéristique de fonctionnement du récepteur ; F1 = moyenne harmonique de la précision et du rappel ; ICLR = International Conference on Learning Representations ; ICML = International Conference on Machine Learning ; ACL = Association for Computational Linguistics ; PMLR = Proceedings of Machine Learning Research. Les noms de modèles (Llama, Gemma, GPT…) sont des noms propres.

---

## 1. arXiv 2509.26238v4 — Beyond Linear Probes

### Identité

- **Titre** : Beyond Linear Probes: Dynamic Safety Monitoring for Language Models.
- **Auteurs (5)** : James Oldfield (Queen Mary University of London ; University of Oxford), Philip Torr (University of Oxford), Ioannis Patras (Queen Mary University of London), Adel Bibi (University of Oxford), Fazl Barez (University of Oxford ; WhiteBox ; Martian) : "Queen Mary University of London 2 University of Oxford 3 WhiteBox 4 Martian" (p. 1).
- **Version, date** : v4 du 21 avril 2026 (catégorie cs.LG).
- **Venue** : ICLR 2026, imprimée en tête de chaque page.

### Ce qui a été lu

Pages 1 à 11 (corps, déclarations d'éthique et de reproductibilité) et 17 à 26 (annexes A à G) en entier. Pages 27 à 38 (figures d'annexe) : légendes seulement, les courbes étant des images. Pages 11 à 16 (bibliographie) : survolées.

### Affirmations

Texte vérifié (`docs/etat-de-l-art-controle-ia-v1.md`, ligne 42) : « - **Beyond Linear Probes (Oldfield, Torr, Patras, Bibi, Barez)**, arXiv 2509.26238, ICLR 2026 — « dynamique » au sens de calcul progressif, pas de temporel ; cascade sonde → juge génératif. → Base architecturale seulement. »

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 1.1 | l. 42 : auteurs « Oldfield, Torr, Patras, Bibi, Barez » | confirmé | p. 1 | "James Oldfield 1,2∗ Philip Torr 2 Ioannis Patras 1 Adel Bibi 2 Fazl Barez 2,3,4" |
| 1.2 | l. 42 : « arXiv 2509.26238, ICLR 2026 » | confirmé | p. 1 | "Published as a conference paper at ICLR 2026" |
| 1.3 | l. 42 : même affirmation (version lue) | confirmé ; version lue : v4 du 21 avril 2026 | p. 1 | "arXiv:2509.26238v4 [cs.LG] 21 Apr 2026" |
| 1.4 | l. 42 : « « dynamique » au sens de calcul progressif, pas de temporel » | confirmé : le calcul croît avec la difficulté de l'entrée ou le budget disponible | p. 1 | "We argue that safety monitors should be flexible–costs should rise only when inputs are difficult to assess, or when more compute is available." |
| 1.5 | l. 42 : même affirmation (« pas de temporel ») | confirmé : chaque prompt est réduit à la moyenne de ses activations sur les tokens ; aucune dimension temporelle | p. 6 | "of each prompt from the residual stream at layer L, mean-pooled over the token dimension." |
| 1.6 | l. 42 : « cascade sonde → juge génératif » | corrigé : « cascade interne de classifieurs polynomiaux emboîtés, dans l'espace des activations : la sonde linéaire d'abord, puis les termes d'ordre 2 à 5 seulement si la prédiction reste incertaine ; la cascade sonde → juge génératif est celle de McKenzie et al. 2025 et Cunningham et al. 2025, que les auteurs jugent complémentaire sans la tester ; les juges génératifs n'y sont que des témoins de comparaison (annexe F.3) » | p. 1 | "Second, as an adaptive cascade: clear cases exit early after low-order checks, and higher-order guardrails are evaluated only for ambiguous inputs, reducing overall monitoring costs." |
| 1.7 | l. 42 : même affirmation | corrigé (suite : la cascade vers un juge génératif n'est qu'envisagée) | p. 3 | "We view these methods as complementary; in principle, a cascade of depth N + 1 could combine TPCs with an LLM-as-monitor final layer for additional defense." |
| 1.8 | l. 42 : « → Base architecturale seulement. » | confirmé (jugement compatible : classification de prompts nuisibles, une décision par prompt, ni agent ni trajectoire) ; réserve : la base publiée agrège par moyenne sur les tokens, ce que le programme interdit dans une sonde de production | p. 10 | "More broadly, our experiments primarily focused on harmful prompt classification." |

**Formulation proposée pour la ligne 42** : « - **Beyond Linear Probes (Oldfield, Torr, Patras, Bibi, Barez)**, arXiv 2509.26238 v4, ICLR 2026 — « dynamique » au sens de calcul progressif, pas de temporel (une moyenne des activations sur les tokens d'un prompt) ; cascade interne de classifieurs polynomiaux emboîtés (sonde linéaire, puis termes d'ordre supérieur seulement si la prédiction reste incertaine) ; les juges génératifs n'y sont que des témoins de comparaison. → Base architecturale seulement. »

### Chiffres utilisables

| Chiffre | Nature | Page | Citation exacte |
|---|---|---|---|
| WildGuardMix : 86,8 milliers de séquences d'entraînement, 1,7 millier de test | auteurs | p. 6 | "containing 86.8k/1.7k training/test sequences" |
| Polynôme d'ordre 5, rang 64, cinq graines | auteurs | p. 6 | "We then train a single N = 5 degree polynomial with CP rank R = 64 for all models. We train all models 5 times with different random seeds." |
| F1 de test, couche 32 de gemma-3-27b-it : sonde linéaire 88,03 | auteurs (tableau 1) | p. 8 | "Linear probe 32 97.83 88.03" |
| F1 de test, même couche : polynôme d'ordre 5 : 88,86 | auteurs (tableau 1) | p. 8 | "TPC (5th order) 32 98.34 88.86" |
| F1 de test face aux juges génératifs (couche 40) : sonde linéaire 86,86 ; polynôme 88,50 ; gpt-4o-mini 86,63 ; claude-3-haiku 83,24 | auteurs (tableau 4) | p. 24 | "Linear probe 86.86 5,377" ; "TPC (ours) 88.50 1,381,889" ; "gpt-4o-mini 86.63" ; "claude-3-haiku 83.24" |
| Gains maximaux annoncés : 10 % d'exactitude sur certaines catégories face à la sonde linéaire, 6 % face aux perceptrons multicouches | auteurs | p. 2 | "we find TPCs evaluated at a fixed-order bring up to 10% improvement in accuracy over linear probes (for classifying particular categories of harmful prompts), and up to 6% over MLP baselines." |

### Antériorité (R8)

- **H2** : n'occupe pas. La cascade est une sortie anticipée par entrée, réglée par un seuil de confiance ; ni accumulation entre actions, ni garantie de faux positifs : "we can propagate each input through the increasingly powerful higher-order classifier’s terms only if the truncated classifiers are uncertain" (p. 5).
- **H1** : n'occupe pas. Touche seulement le gain blanc-sur-noir général, sur des prompts nuisibles, en score F1, sans taux de faux positifs égal ni sabotage : "Interestingly, the activation probes outperform the significantly larger LLM-as-monitors and smaller guard models in these experiments." (p. 24).
- **Lemme d'additivité, théorème négatif** : n'occupe pas.
- **Transposition jeton → action** : n'occupe pas ; seule la moyenne sur les tokens est employée, ni max ni attention.
- **HC1** : n'occupe pas (juges génératifs à consigne fixe, sans pression).
- **HC2b, papier B** : n'occupe pas.

---

## 2. arXiv 2605.27958v1 — Pressure-Testing Deception Probes

### Identité

- **Titre** : Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry of Deceptive Representations.
- **Auteur (1)** : Sachin Kumar, LexisNexis, États-Unis ; recherche menée à titre indépendant : "LexisNexis, USA" (p. 1).
- **Version, date** : v1 du 27 mai 2026 (catégorie cs.CL).
- **Venue** : aucune imprimée (prépublication). Mise en page de type conférence de l'ACL (sections « Limitations » et « Ethical considerations »), ce qui n'établit pas une acceptation.
- **Objet** : sondes de tromperie sur la famille Gemma 3 instruite, de 1 à 27 milliards de paramètres (notés 1B, 4B, 12B, 27B) ; jeux D-RepE (questions factuelles sous consignes « honnête » ou « mensonge »), D-Role (jeu de rôle) et D-MASK (réponse contraire à la croyance du modèle), tous induits par consigne système.

### Ce qui a été lu

En entier (18 pages) ; bibliographie (pp. 10–11) survolée.

### Affirmations

Textes vérifiés (`docs/etat-de-l-art-controle-ia-v1.md`) :
- ligne 47 : « - **Pressure-Testing Deception Probes (Kumar)**, arXiv 2605.27958, ACL 2026 — rejette l'hypothèse d'une direction unique (AUROC 0,61 à 0,80 avec une seule direction) ; effondrement sous changement de style, récupéré par augmentation de style (environ 0,98) ; les sondes multidimensionnelles récupèrent le signal ; la sonde détecte très bien le régime de consigne trompeuse. → Occupe une partie de H8 ; soutient HC2b avec une réserve sur les corrélats de surface. »
- ligne 146 : « - Auto-incrimination comme résultat central (seulement effleurée par 2609.03035 et 2605.27958). »
- ligne 158 : « - **Réserve** : les sondes captent souvent le régime de consigne ou des corrélats de surface (2605.27958 ; ⚠ arXiv 2606.07612) — contrôler le style dans toute mesure de HC2b. »

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 2.1 | l. 47 : auteur « Kumar » | confirmé (auteur unique) | p. 1 | "Sachin Kumar*" |
| 2.2 | l. 47 : même affirmation | confirmé : recherche indépendante | p. 1 | "This research was conducted independently and does not reflect the views or represent work done at LexisNexis." |
| 2.3 | l. 47 : « arXiv 2605.27958, ACL 2026 » | introuvable pour la venue : « ACL », « EMNLP », « NAACL », « Proceedings », « conference », « workshop », « accepted », « submitted », « under review » cherchés dans les 18 pages, présents seulement dans la bibliographie ; le PDF ne porte que le tampon arXiv. À mettre : « arXiv 2605.27958 v1 (27 mai 2026), prépublication sans venue imprimée » | p. 1 | "arXiv:2605.27958v1 [cs.CL] 27 May 2026" |
| 2.4 | l. 47 : « rejette l'hypothèse d'une direction unique (AUROC 0,61 à 0,80 avec une seule direction) » | corrigé : « rejette l'hypothèse d'une direction universelle commune aux types de tromperie (le transfert d'un jeu de données à l'autre échoue aux quatre tailles) ; 0,61 à 0,80 est l'AUROC d'une sonde restreinte à la première composante principale (k = 1), alors que la sonde linéaire complète, qui est elle-même une direction, atteint au moins 0,998 en domaine » | p. 1 | "the single-direction hypothesis is decisively rejected (k=1 captures only 0.61–0.80 AUROC of the signal" |
| 2.5 | l. 47 : même affirmation | corrigé (suite : k = 1 désigne une composante principale) | p. 13 | "Across all four scales, a single PCA direction captures only 0.61–0.80 AUROC — far below the ≥0.999 achieved by the full linear probe." |
| 2.6 | l. 47 : même affirmation | corrigé (suite : le rejet repose sur l'échec du transfert) | p. 6 | "P1a is rejected for all four models." |
| 2.7 | l. 47 : « effondrement sous changement de style » | corrigé (précision) : « sous huit changements de style, la sonde entraînée sans augmentation tombe en moyenne à 0,652 (1B), 0,759 (4B), 0,609 (12B) et 0,485 (27B, couche 27) ; une sonde du 27B entraînée de la même façon à la couche 34 reste à 0,921 en moyenne sur les styles tenus à l'écart (l'auteur attribue l'écart au changement de couche) : l'effondrement dépend de la couche choisie » | p. 1 | "probe-based metrics achieve near-perfect AUROC (≥0.998) on clean data but collapse under stylistic shifts when trained without stylistic augmentation" |
| 2.8 | l. 47 : même affirmation | corrigé (suite : moyennes du tableau 10) | p. 7 | "Mean .652 .759 .609 .485" |
| 2.9 | l. 47 : même affirmation | corrigé (suite : couche changée entre les deux tableaux) | p. 8 | "Clean-probe AUROCs for 27B differ from Table 10 because the augmented experiment used a re-selected optimal layer (layer 34 vs. 27)" |
| 2.10 | l. 47 : « récupéré par augmentation de style (environ 0,98) » | confirmé pour le chiffre : 0,979 (4B) et 0,983 (27B), quatre styles d'entraînement et quatre tenus à l'écart ; à couche égale, le gain est de +0,063 et +0,062 | p. 1 | "style-augmented probes recover near-perfect detection (mean AUROC 0.979–0.983) even on unseen styles" |
| 2.11 | l. 47 : même affirmation | confirmé (détail, tableau 11) | p. 8 | "Mean (test) .916 .979 +.063 .921 .983 +.062" |
| 2.12 | l. 47 : « les sondes multidimensionnelles récupèrent le signal » | confirmé (en domaine, sur D-RepE, par rapport à la seule première composante principale) | p. 1 | "multi-dimensional probes (k≥5) consistently recover the signal" |
| 2.13 | l. 47 : « la sonde détecte très bien le régime de consigne trompeuse » | confirmé (AUROC de 0,998 à 1,000, que le mensonge ait réussi ou non) | p. 5 | "the probe detects the deceptive prompt regime — the model’s internal state when processing under a deceptive system prompt — rather than the downstream success of deception" |
| 2.14 | l. 47 : « → Occupe une partie de H8 » | confirmé, partie seulement : le papier relie ce que capte la sonde (corrélats de style d'un entraînement étroit) à sa fragilité sous changement de style non adverse ; il n'oppose pas intention et conscience d'évaluation et ne prédit pas la robustesse adverse | p. 7 | "This pattern reflects D-RepE training pairing stylistically neutral prompts; any surface differences models produce become learnable probe features." |
| 2.15 | l. 47 : « soutient HC2b avec une réserve sur les corrélats de surface » | corrigé : « ne teste pas HC2b (aucune tentative de manipuler le moniteur) ; fournit la réserve (la sonde capte le régime de consigne et, entraînée étroitement, des corrélats de style) et un indice indirect : la sonde signale la consigne trompeuse même quand la réponse reste exacte » | p. 9 | "such probes may be useful as intent monitors — flagging that a model is operating under deceptive instructions even when its output happens to be correct — but they cannot distinguish successful from failed deception." |
| 2.16 | l. 146 : « Auto-incrimination comme résultat central (seulement effleurée par 2609.03035 et 2605.27958) » | corrigé pour 2605.27958 (2609.03035 hors de ce lot) : « 2605.27958 ne traite pas l'auto-incrimination sous manipulation ; il montre seulement que la sonde signale la consigne trompeuse, que le mensonge réussisse ou non » ; la zone reste ouverte de son côté | p. 5 | "verified and unverified examples score identically" |
| 2.17 | l. 158 : « les sondes captent souvent le régime de consigne ou des corrélats de surface (2605.27958 ; …) — contrôler le style dans toute mesure de HC2b » | confirmé pour 2605.27958 ; portée : contrastes induits par consigne système, famille Gemma 3 | p. 12 | "probes trained on narrow contrastive data appear to rely on stylistic correlates of deception (hedging, shorter responses, altered register)." |
| 2.18 | l. 158 : même affirmation (portée) | confirmé ; l'auteur étend lui-même le constat de consigne à tous les bancs d'essai existants | p. 1 | "all existing deception-probe benchmarks – including ours – induce the honest/deceptive contrast via system-prompt manipulation." |

**Formulation proposée pour la ligne 47** : « - **Pressure-Testing Deception Probes (Kumar)**, arXiv 2605.27958 v1 (prépublication, aucune venue imprimée) — rejette l'hypothèse d'une direction universelle commune aux types de tromperie (le transfert entre jeux échoue) ; une sonde sur la seule première composante principale n'atteint que 0,61 à 0,80 d'AUROC, contre au moins 0,998 pour la sonde linéaire complète en domaine ; sous huit changements de style, la sonde standard tombe en moyenne à 0,485 (27B, couche 27), mais une sonde standard entraînée à la couche 34 reste à 0,921 sur les styles tenus à l'écart ; l'augmentation de style donne 0,979 (4B) et 0,983 (27B) ; les sondes multidimensionnelles (k ≥ 5) récupèrent le signal en domaine ; la sonde détecte le régime de consigne trompeuse, que le mensonge réussisse ou non. → Occupe une partie de H8 (lien entre ce que capte la sonde et sa fragilité au style, non adverse) ; ne teste pas HC2b ; fournit la réserve sur les corrélats de surface. »

**Formulation proposée pour la ligne 146** (partie 2605.27958) : « - Auto-incrimination comme résultat central (2605.27958 ne la traite pas : il montre seulement que la sonde signale la consigne trompeuse même quand le mensonge échoue ; 2609.03035 à vérifier dans son propre lot). »

### Chiffres utilisables

| Chiffre | Nature | Page | Citation exacte |
|---|---|---|---|
| Jeux : 2 000 exemples chacun (1 000 honnêtes, 1 000 trompeurs), découpage 60/20/20 | auteurs | p. 4 | "Each primary dataset contains N = 2, 000 examples (1,000 honest, 1,000 deceptive) with 60/20/20 train/validation/test splits." |
| Sonde sur k composantes principales : k = 1 de 0,609 à 0,804 ; k = 5 de 0,908 à 0,990 | auteurs (tableau 6) | p. 5 | "k=1 0.609 0.661 0.804 0.672 0.609 0.804 0.195" ; "k=5 0.908 0.981 0.938 0.990 0.908 0.990 0.081" |
| Régime de consigne : AUROC 0,998 (4B, mensonge vérifié) et 0,999 (non vérifié) ; 1,000 et 0,998 (27B) | auteurs (tableau 4) | p. 5 | "4B Verified 241 0.998" ; "4B Unverified 159 0.999" ; "27B Verified 247 1.000" ; "27B Unverified 153 0.998" |
| Étiquettes « trompeuses » sans mensonge effectif : 29 à 41 % | auteurs | p. 5 | "the 29–41% label contamination does not degrade probe performance" |
| Gain des activations sur un témoin texte (pondération des mots par fréquence et rareté, dite TF-IDF, puis régression logistique) : 0,442 à 0,522 ; gonflé quand le témoin est sous 0,5 | auteurs | p. 5 | "The Black-to-White Boost increases monotonically with scale (0.442 → 0.522)" |
| Incohérence interne : k = 3 dit au-dessus de 0,90 pour deux modèles, dont le 27B à 0,819 | calcul (comparaison au seuil 0,90 du texte) | p. 5 | "k = 3 does so for two of four models (4B: 0.963, 27B: 0.819)" |
| Changements de style, sonde standard : moyennes 0,652 / 0,759 / 0,609 / 0,485 (1B, 4B, 12B, 27B) | auteurs (tableau 10) | p. 7 | "Mean .652 .759 .609 .485" |
| Sonde standard du 4B, style « robotique » : 0,542 au tableau 10 | auteurs (tableau 10) | p. 7 | "Robotic .618 .542 .579 .429" |
| Même sonde du 4B, même style : 0,993 au tableau 11 ; écart non expliqué (l'explication par la couche n'est donnée que pour le 27B) | calcul (comparaison des tableaux 10 et 11) | p. 8 | "Robotic train .993 1.000 +.007 .998 1.000 +.002" |
| Sonde standard du 27B : 0,914 (styles d'entraînement) et 0,921 (styles tenus à l'écart) à la couche 34, contre 0,485 à la couche 27 : écart d'environ 0,43 | calcul (comparaison des tableaux 10 et 11) | p. 8 | "Mean (train) .905 .997 +.093 .914 1.000 +.085" |
| Hypothèse d'entropie rejetée : corrélation de rang maximale 0,454 en valeur absolue (seuil 0,8), baisse maximale d'AUROC après résidualisation 0,0038 (arrondie à 0,004 dans le résumé) | auteurs | p. 12 | "0.454 (1B, D-MASK), well below the 0.8 threshold." ; "0.0038 (4B, D-RepE)—two orders of magnitude" |

### Antériorité (R8)

- **H2** : n'occupe pas (une réponse, un token).
- **H1** : n'occupe pas. Mesure un gain des activations sur un témoin texte faible, pour des mensonges factuels induits par consigne, sans taux de faux positifs fixé : "At 12B/27B, the text-only baseline scores below 0.5 (anti-predictive), which mechanically inflates the boost." (p. 4).
- **Lemme d'additivité, théorème négatif** : n'occupe pas.
- **Transposition jeton → action** : n'occupe pas ; sondes au dernier token seulement : "we collect residual stream activations at the last token" (p. 4).
- **HC1** : n'occupe pas.
- **HC2b** : n'occupe pas. Voisinage seulement (le « moniteur d'intention » de 2.15) ; aucune tentative de manipuler le moniteur n'est mesurée.
- **Papier B** : n'occupe pas.
- Hors liste : **H8** occupé en partie (voir 2.14).

---

## 3. arXiv 2502.03407v1 — Detecting Strategic Deception Using Linear Probes

### Identité

- **Titre** : Detecting Strategic Deception Using Linear Probes.
- **Auteurs (4)** : Nicholas Goldowsky-Dill, Bilal Chughtai, Stefan Heimersheim, Marius Hobbhahn — Apollo Research.
- **Version, date** : v1 du 5 février 2025 (catégorie cs.LG ; en-tête de page daté du 6 février 2025).
- **Venue** : aucune imprimée sur la version empreintée.

### Ce qui a été lu

En entier (35 pages) ; bibliographie (pp. 11–14) survolée. Figures (images) : légendes seulement ; les valeurs du témoin boîte noire (figure 6) et des agrégations (figure 14) ne sont pas lisibles dans le texte.

### Affirmations

Textes vérifiés (`docs/etat-de-l-art-controle-ia-v1.md`) :
- ligne 33 : « - **Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (Apollo Research)**, arXiv 2502.03407, ICML 2025 — sondes linéaires de tromperie sur Llama-3.3-70B ; AUROC de 0,96 à 0,999 selon les jeux ; environ 95 à 99 % des réponses trompeuses attrapées à 1 % de faux positifs sur conversation neutre ; les auteurs notent que la moyenne sur les tokens dilue les réponses partiellement trompeuses. → Base mono-action ; motive l'agrégation temporelle et l'abandon de la moyenne. »
- ligne 65 (tableau, colonnes séparées ici par ¦) : « Sondes de tromperie Apollo (mono-action) ¦ AUROC 0,96 à 0,999 ¦ arXiv 2502.03407 »

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 3.1 | l. 33 : « Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (Apollo Research) » | confirmé | p. 1 | "Nicholas Goldowsky-Dill, Bilal Chughtai, Stefan Heimersheim Marius Hobbhahn Apollo Research" |
| 3.2 | l. 33 : « arXiv 2502.03407, ICML 2025 » | introuvable pour la venue : « ICML », « NeurIPS », « ICLR », « conference », « proceedings », « PMLR », « workshop », « accepted », « preprint » cherchés dans les 35 pages et les métadonnées : aucune occurrence. À mettre : « arXiv 2502.03407 v1 (5 février 2025) ; aucune venue sur la version empreintée — ICML 2025 à établir sur la version publiée, à empreinter » | p. 1 | "arXiv:2502.03407v1 [cs.LG] 5 Feb 2025" |
| 3.3 | l. 33 : « sondes linéaires de tromperie sur Llama-3.3-70B » | confirmé (version Instruct, couche 22 sur 80) | p. 3 | "We apply our probes after layer 22 (of 80) in the residual stream of Llama-3.3-70B-Instruct" |
| 3.4 | l. 33 : « AUROC de 0,96 à 0,999 selon les jeux » | confirmé ; réserve : réponses ambiguës exclues ; si on les reclasse, 0,913 (jeu de rôle), 0,978 (rapport de délit d'initié), 0,982 (sous-performance volontaire) | p. 1 | "We find that our probe distinguishes honest and deceptive responses with AUROCs between 0.96 and 0.999 on our evaluation datasets." |
| 3.5 | l. 33 : même affirmation | confirmé (détail par jeu) | p. 6 | "The lowest AUROC is 0.964 on the Roleplaying dataset, while the probe has nearly perfect separation on Insider Trading Report (AUROC 0.999)." |
| 3.6 | l. 33 : « environ 95 à 99 % des réponses trompeuses attrapées à 1 % de faux positifs sur conversation neutre » | confirmé ; réserves : le rappel est mesuré contre des réponses témoins sans rapport avec la tromperie (Alpaca), pas contre les réponses honnêtes des mêmes scénarios, que la sonde signale souvent ; il est très sensible à la couche ; le papier donne aussi « plus de 96 % » (p. 10) et, pour le jeu de rôle, 96 % au texte (p. 6) contre 0,998 au tableau 3 (p. 23) | p. 1 | "If we set the decision threshold to have a 1% false positive rate on chat data not related to deception, our probe catches 95-99% of the deceptive responses." |
| 3.7 | l. 33 : même affirmation (réserve sur le témoin) | confirmé avec réserve | p. 6 | "Notably, this probe fires much more on honest responses to our evaluation prompts than on responses to control prompts, often leading to them being above the 1% FPR threshold (Figure 3)." |
| 3.8 | l. 33 : même affirmation (réserve sur la couche) | confirmé avec réserve | p. 6 | "probing two layers later results in a recall of nearly 0 on both Insider Trading datasets" |
| 3.9 | l. 33 : « les auteurs notent que la moyenne sur les tokens dilue les réponses partiellement trompeuses » | confirmé | p. 8 | "We take the mean across per-token scores to get a per-prompt score. When responses are only partially deceptive, however, this can result in a misclassification even if the per-token probe activations are sensible (Table 2, example 2)." |
| 3.10 | l. 33 : « → Base mono-action ; motive l'agrégation temporelle et l'abandon de la moyenne. » | corrigé : « Base mono-action ; motive une agrégation au-delà d'une réponse ; ne justifie pas à lui seul l'abandon de la moyenne : sa propre comparaison trouve la moyenne meilleure que le max et que la moyenne seuillée pour la sonde principale, l'effet dépendant de la sonde et du jeu » | p. 22 | "We find that taking the mean is best on all datasets for the probe trained on Instructed-Pairs (Figure 14a)." |
| 3.11 | l. 33 : même affirmation | corrigé (suite) | p. 22 | "We believe there is room for improvement here but it is very probe and dataset dependent." |
| 3.12 | l. 65 : « Sondes de tromperie Apollo (mono-action) ¦ AUROC 0,96 à 0,999 ¦ arXiv 2502.03407 » | confirmé (même réserve qu'en 3.4) | p. 6 | "On Insider Trading Confirmation and Sandbagging the probe has AUROC of 0.974 and 0.983 respectively." |

**Formulation proposée pour la ligne 33** : « - **Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (Apollo Research)**, arXiv 2502.03407 v1 (5 février 2025 ; aucune venue sur la version empreintée) — sondes linéaires de tromperie sur Llama-3.3-70B-Instruct (couche 22 sur 80) ; AUROC de 0,96 à 0,999 selon les jeux (réponses ambiguës exclues ; 0,913 à 0,982 si on les reclasse) ; environ 95 à 99 % des réponses trompeuses attrapées à 1 % de faux positifs calibré sur des réponses de conversation sans rapport avec la tromperie (la sonde réagit aussi aux scénarios liés à la tromperie quand la réponse est honnête) ; les auteurs notent que la moyenne sur les tokens peut mal classer les réponses partiellement trompeuses, mais leur comparaison d'agrégations trouve la moyenne meilleure que le max pour leur sonde principale. → Base mono-action ; motive l'agrégation au-delà d'une réponse ; ne justifie pas à lui seul l'abandon de la moyenne. »

### Chiffres utilisables

| Chiffre | Nature | Page | Citation exacte |
|---|---|---|---|
| Jeux (honnêtes / ambiguës / trompeuses) : jeu de rôle 84/84/203 ; rapport de délit d'initié 669/324/336 ; confirmation 24/2/630 ; sous-performance volontaire 511/64/420 | auteurs (tableau 1) | p. 4 | "84 / 84 / 203" ; "669 / 324 / 336" ; "24 / 2 / 630" ; "511 / 64 / 420" |
| Témoin : 9 994 réponses à des requêtes Alpaca | auteurs | p. 20 | "(out of the 9,994 tested)" |
| AUROC après reclassement des ambiguës : 0,913 / 0,978 / 0,982 ; rappel à 1 % : 0,956 / 1,000 / 0,998 | auteurs (tableau 3) | p. 23 | "Roleplaying 0.964 0.913 0.998 0.956" ; "Insider Trading Report 0.999 0.978 1.000 1.000" ; "Sandbagging 0.983 0.982 0.998 0.998" |
| Rappel à 1 % de faux positifs sur le jeu de rôle : 96 % au texte contre 0,998 au tableau 3 (p. 23) : incohérence interne | calcul (comparaison) | p. 6 | "a threshold with 1% FPR on control misses 4% of deceptive responses on Roleplaying" |
| Rappel annoncé ailleurs : plus de 96 % sur tous les jeux, à 1 % de faux positifs | auteurs | p. 10 | "The Instructed-Pairs trained probe achieves recall of >96% on all our evaluation datasets with a 1% FPR on control." |
| Témoin boîte noire (GPT-4o sur la transcription entière) : « à peu près équivalent » aux sondes ; valeurs seulement en figure | auteurs (qualitatif) | p. 10 | "Our probes perform roughly equivalent to our 4o black-box baseline" |
| Cadre « AI Audit » écarté : AUROC 0,872, intention trompeuse non établie | auteurs | p. 16 | "With these labels our Instructed-Pairs probe achieves AUROC of 0.872 (Figure 9)." |
| Sonde lue après une question de suivi : rappel à 1 % de faux positifs supérieur à 99 % sur les quatre jeux | auteurs | p. 18 | "Our recall at 1% is greater than 99% on all four evaluation datasets." |

### Antériorité (R8)

- **H2** : n'occupe pas ; un score par réponse, aucune accumulation entre réponses.
- **H1** : n'occupe pas. En mono-action et sur tromperie flagrante, l'écart blanc/noir n'apparaît pas : "In all of our settings, however, deception is relatively blatant and often expressed in the model’s chain-of-thought." (p. 10).
- **Lemme d'additivité, théorème négatif** : n'occupe pas.
- **Transposition jeton → action** : n'occupe pas ; compare moyenne, max et moyenne seuillée à l'intérieur d'une réponse, sans attaque ni niveau action : "Taking the maximum probe score across the model’s response" (p. 22).
- **HC1** : n'occupe pas (GPT-4o sert d'étiqueteur et de témoin, sans pression).
- **HC2b** : n'occupe pas, mais voisinage à signaler (R8, zone séduisante) : une sonde lue juste après un démenti « No » inséré par les expérimentateurs sépare presque parfaitement honnête et trompeur : "After every model response we insert the user query “Was your last response deceptive? (Yes/No)” and then the model response “No.” We gather activations immediately after this response token." (p. 9) ; "This is the best probe of all we trained at distinguishing deceptive and honest responses, with near perfect separation on all datasets." (p. 9). Le démenti est imposé et non tenté par l'agent, et l'effet de la tentative sur le score n'est pas mesuré ; c'est l'antécédent le plus proche de « plaider incrimine » dans ce lot.
- **Papier B** : n'occupe pas.

---

## 4. arXiv 2606.07612v1 — Position: Anthropomorphic Misalignment Research Needs Stronger Evidence

### Identité

- **Titre** : Position: Anthropomorphic Misalignment Research Needs Stronger Evidence.
- **Auteurs (8)** : Vansh Gupta, Peter Nutter, Samuel Stante (contribution égale), Andreas Krause, Florian Tramèr, Lukas Fluri, Xin Chen, Anna Hedström (encadrement égal pour les trois derniers) — ETH Zurich : "Vansh Gupta * 1 Peter Nutter * 1 Samuel Stante * 1 Andreas Krause 1 Florian Tramèr 1" (p. 1) ; "Lukas Fluri † 1 Xin Chen † 1 Anna Hedström † 1" (p. 1).
- **Version, date** : v1 du 29 mai 2026 (catégorie cs.CY).
- **Venue** : ICML 2026 (43e conférence, Séoul), PMLR volume 306 ; papier de position : "Proceedings of the 43 rd International Conference on Machine Learning, Seoul, South Korea. PMLR 306, 2026." (p. 1).

### Ce qui a été lu

En entier (25 pages) ; bibliographie (pp. 10–15) survolée. La figure 2 (taux de faux positifs par test) est une image : seules les fourchettes du texte (p. 22) sont utilisées.

### Affirmations

Textes vérifiés (`docs/etat-de-l-art-controle-ia-v1.md`) :
- ligne 158 : « - **Réserve** : les sondes captent souvent le régime de consigne ou des corrélats de surface (2605.27958 ; ⚠ arXiv 2606.07612) — contrôler le style dans toute mesure de HC2b. »
- ligne 196 : `| 12 | arXiv 2606.07612, 2511.00554 | H8, HC2 | Contenu, non lu directement |` (colonnes : rang, référence, ce qu'elle menace, ce qu'il faut établir).

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 4.1 | l. 158 : « les sondes captent souvent le régime de consigne ou des corrélats de surface (… ; ⚠ arXiv 2606.07612) » | confirmé ; le ⚠ peut être levé (lu sur PDF empreinté) ; portée : deux sondes d'Apollo Research sur Llama-3.3-70B-Instruct, agrégées par moyenne | p. 6 | "Figure 2 shows that these probes often produce high false positive rates on our stress tests, suggesting sensitivity to surface cues and framing rather than intent." |
| 4.2 | l. 158 : même affirmation | confirmé | p. 22 | "Instead, they appear to be detecting the presence of roleplaying framing, factually incorrect information, or simply that the text is related to deception without being able to differentiate further." |
| 4.3 | l. 158 : même affirmation (généralité de « souvent ») | confirmé avec la réserve des auteurs eux-mêmes | p. 22 | "These findings only underscore correlation issues specific to these probes under the tested conditions and may not generalize to alternative probing methods/architectures, different training datasets, or other model families." |
| 4.4 | l. 158 : « contrôler le style dans toute mesure de HC2b » | confirmé (même recommandation chez les auteurs) | p. 18 | "If you use contrastive datasets, match positives and negatives on obvious confounders (topic, length, tone, style)." |
| 4.5 | l. 196 : « 12 ¦ arXiv 2606.07612, … ¦ H8, HC2 ¦ Contenu, non lu directement » | corrigé pour 2606.07612 : « lu au niveau 2 (lot 2, A2b) ; touche H8 à la prémisse seulement (validité de construit des sondes : faux positifs de 87 à 100 % sur sarcasme, « Wrong Answers Only », contrefactuel et récitation), sans mesure de robustesse adverse ; ne touche pas HC2 (aucune attaque) » | p. 22 | "Both probes exhibit high FPRs on Sarcasm, Wrong Answers Only, Counterfactual, and Recital, with values ranging from 87% to 100%." |

**Formulation proposée pour la ligne 196** (rangée 12, colonnes séparées par ¦) : « 12 ¦ arXiv 2606.07612, 2511.00554 ¦ H8 (2606.07612 : prémisse de validité de construit seulement), HC2 (2511.00554 : attaque boîte noire par contenu contre des sondes à attention, directe) ¦ Lus au niveau 2 (lot 2, A2b) ; collision partielle pour HC2, voir la section 5 »

### Chiffres utilisables

| Chiffre | Nature | Page | Citation exacte |
|---|---|---|---|
| Tests de résistance (réponses toutes honnêtes) : faux positifs de 87 à 100 % (sarcasme, « Wrong Answers Only », contrefactuel, récitation) | auteurs | p. 22 | "with values ranging from 87% to 100%" |
| Moins de 36 % (extraterrestre, paraphrase, traduction) ; paysan médiéval : 96 % (sonde entraînée sur jeu de rôle) contre 4 % (sonde entraînée sur paires instruites) | auteurs | p. 22 | "In contrast, performance is significantly better on Alien, Paraphrase, and Translate, where FPRs remain below 36%." ; "A sharp divergence occurs on Medieval Peasant where the probe trained on Roleplaying shows a high FPR of 96% while the probe trained on Instructed-Pairs only has an FPR of 4%." |
| Agrégation employée pour ces tests : moyenne sur tous les tokens de la réponse | auteurs | p. 22 | "After using the probe to evaluate the output activations of the response individually for each token, we aggregate them by using their mean." |
| DeceptionBench : 27 scénarios sur 150 (18 %) sans vérité de référence | auteurs | p. 22 | "We identified structural ambiguities in 27 out of 150 scenarios (18%)" |
| Désalignement émergent : taux de 3,7 à 12,9 % selon le juge et la règle de seuil | auteurs | p. 4 | "misalignment rates range from 3.7% to 12.9% depending on judge choice and boundary inclusion in thresholds." |
| Changer de juge déplace le taux de 3,72 % à 8,02 % | auteurs | p. 25 | "shifted the EM rate from 3.72% to 8.02%" |

### Antériorité (R8)

- **H2, lemme d'additivité, théorème négatif, papier B** : n'occupe pas.
- **H1** : n'occupe pas.
- **Transposition jeton → action** : n'occupe pas ; signale seulement le dilemme d'agrégation à l'intérieur d'une réponse : "Aggregation methods face trade-offs; for instance, averaging over an entire response may fail when deceptive content is highly localized" (p. 4).
- **HC1** : n'occupe pas. Recommande la notation pondérée par les probabilités des jetons et documente la sensibilité des juges au libellé, sans loi de déférence sous pression : "favor weighted aggregation over raw argmax to reduce boundary noise" (p. 25) ; "LLM judges are inherently stochastic and sensitive to temperature, prompt phrasing, and architectural details" (p. 4). Le « verdict par probabilité du jeton » y est une pratique recommandée, pas l'énoncé de HC1.
- **HC2b** : n'occupe pas ; les tests portent sur des contenus honnêtes, sans manipulation. Ils fournissent l'argument du contrôle du style.

---

## 5. arXiv 2511.00554v1 — Red-teaming Activation Probes using Prompted LLMs

### Identité

- **Titre** : Red-teaming Activation Probes using Prompted LLMs.
- **Auteurs (2)** : Phil Blandfort, Robert Graham (chercheurs indépendants ; projet financé par eux-mêmes) : "Phil Blandfort Robert Graham Independent" (p. 1) ; "as this project was financed privately by the authors" (p. 11).
- **Version, date** : v1 du 1er novembre 2025 (catégorie cs.LG).
- **Venue** : aucune, prépublication : "Preprint." (p. 1).

### Ce qui a été lu

En entier (16 pages) ; la figure 2 (image) : légende seulement.

### Affirmations

Textes vérifiés (`docs/etat-de-l-art-controle-ia-v1.md`) :
- ligne 135 : « - **Dégradation sans évasion par pur contenu** : **Blandfort & Graham**, arXiv 2511.00554 ⚠ non lu directement (red-teaming boîte noire par apprentissage en contexte ; le jargon juridique induit des faux positifs, un ton procédural neutre des faux négatifs ; vulnérabilités réduites mais persistantes ; conclut qu'une sonde ne doit pas être un point de contrôle unique à enjeux élevés). »
- ligne 196 : même rangée 12 qu'en section 4.

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 5.1 | l. 135 : « **Dégradation sans évasion par pur contenu** » | corrigé : « **Évasion partielle par pur contenu** : en boîte noire, sans gradient ni réglage fin, un attaquant GPT-5 guidé par apprentissage en contexte réussit 48,9 % de ses tentatives de faux négatif contre la sonde « enjeux élevés » à attention de Llama-3.3-70B (conversation jugée à enjeux élevés que la sonde ne signale pas), 63,6 % sur la seconde moitié des lots, au seuil 0,5 ; conversations entièrement écrites par l'attaquant ; concept « enjeux élevés », pas tromperie » | p. 3 | "GPT-5 48.9% 8.0% 63.6% 75.6% 20.0% 88.0%" |
| 5.1b | l. 135 : même affirmation (sens du taux) | corrigé (suite : taux de réussite des attaques) | p. 3 | "Roughly 50% of samples generated by GPT-5 when asking to find false negatives are indeed false negatives." |
| 5.2 | l. 135 : même affirmation | corrigé (suite) | p. 3 | "While only up to 20% of generated samples in the first batch break the probe (0-shot columns), GPT-5 achieves high failure rates of over 60% in the second half of batches with in-context learning (2nd-half columns)." |
| 5.3 | l. 135 : même affirmation (nature de la sonde) | corrigé (suite : sonde à attention) | p. 11 | "We train the attention probe on Llama-3.3-70B using the hyperparameters reported in the paper" |
| 5.4 | l. 135 : même affirmation (textes hors politique) | corrigé (suite : l'attaquant écrit aussi les tours de l'assistant) | p. 7 | "for certain model-centric concepts one might be primarily interested in on-policy samples, which can make the red-teaming task more challenging (as the red-teaming model can only suggest the user prompt)" |
| 5.5 | l. 135 : « **Blandfort & Graham**, arXiv 2511.00554 ⚠ non lu directement » | confirmé pour l'identité ; le ⚠ peut être levé | p. 1 | "arXiv:2511.00554v1 [cs.LG] 1 Nov 2025" |
| 5.6 | l. 135 : « red-teaming boîte noire par apprentissage en contexte » | confirmé | p. 1 | "We present a lightweight black-box red-teaming procedure that wraps an off-the-shelf LLM with iterative feedback and in-context learning (ICL), and requires no fine-tuning, gradients, or architectural access." |
| 5.7 | l. 135 : « le jargon juridique induit des faux positifs, un ton procédural neutre des faux négatifs » | confirmé | p. 1 | "Our analysis uncovers interpretable brittleness patterns (e.g., legalese-induced FPs; bland procedural tone FNs)" |
| 5.8 | l. 135 : « vulnérabilités réduites mais persistantes » | corrigé (précision) : « vulnérabilités réduites mais persistantes sous attaques contraintes à un scénario ; la réduction est nette pour l'attaquant GPT-5 (faux négatifs −8,8 points, faux positifs −35,8 points) ; les attaquants plus petits obtiennent au contraire plus de faux négatifs sous contrainte » | p. 1 | "and reduced but persistent vulnerabilities under scenario-constraint attacks." |
| 5.9 | l. 135 : même affirmation | corrigé (suite) | p. 6 | "GPT-5 76.2% (-8.8%) 31.8% (-35.8%)" |
| 5.10 | l. 135 : même affirmation | corrigé (suite) | p. 4 | "Interestingly, smaller models actually achieve higher FNRs when requesting specific scenarios, but lower FPRs." |
| 5.11 | l. 135 : « conclut qu'une sonde ne doit pas être un point de contrôle unique à enjeux élevés » | corrigé : « suggère que les sondes ne devraient pas servir de point de contrôle unique dans les contextes à fortes incitations » | p. 8 | "Our results suggest probes should not serve as single points of control in high-incentive settings." |
| 5.12 | l. 196 : « 12 ¦ arXiv …, 2511.00554 ¦ H8, HC2 ¦ Contenu, non lu directement » | corrigé pour 2511.00554 : « lu ; menace HC2 directement (attaque boîte noire par contenu contre une sonde à attention et une sonde à softmax ; réussite des tentatives de faux négatif de GPT-5 : 63,6 % sur la seconde moitié des lots sans contrainte, 76,2 % en moyenne sous contrainte de scénario) ; ne touche H8 que par des motifs d'échec lexicaux (mots déclencheurs) » | p. 7 | "First, we only red-team probes for a single concept and two probe architectures (attention and softmax)." |

**Formulation proposée pour la ligne 135** : « - **Évasion partielle par pur contenu** : **Blandfort & Graham**, arXiv 2511.00554 v1 (prépublication ; red-teaming boîte noire par apprentissage en contexte, sans gradient ni réglage fin ; sur la sonde « enjeux élevés » à attention de Llama-3.3-70B, un attaquant GPT-5 réussit 48,9 % de ses tentatives de faux négatif, 63,6 % sur la seconde moitié des lots, au seuil 0,5, sur des conversations entièrement écrites par l'attaquant ; le jargon juridique induit des faux positifs, un ton procédural neutre des faux négatifs ; vulnérabilités réduites mais persistantes sous contrainte de scénario ; suggère qu'une sonde ne devrait pas être un point de contrôle unique dans les contextes à fortes incitations). »

### Chiffres utilisables

| Chiffre | Nature | Page | Citation exacte |
|---|---|---|---|
| Sondes hors attaque : AUROC 0,91 (Llama-3.3-70B, attention, couche 30) et 0,85 (Qwen3-8B, softmax, couche 19) | auteurs | p. 3 | "(0.91 AUROC for Llama-3.3-70B and 0.85 AUROC for Qwen3-8B, where the original paper reported 0.915 AUROC)" |
| Seuil de décision fixe 0,5 (pas un seuil calibré à 1 % de faux positifs) | auteurs | p. 3 | "For both probes, we use 0.5 as a classification threshold in all experiments" |
| Llama-3.3-70B, attaquant GPT-5 : faux négatifs 48,9 % (premier lot 8,0 % ; seconde moitié 63,6 %) ; faux positifs 75,6 % (20,0 % ; 88,0 %). Ce sont des taux de réussite d'attaque sur les textes générés, pas des taux d'erreur en exploitation | auteurs (tableau 1) | p. 3 | "GPT-5 48.9% 8.0% 63.6% 75.6% 20.0% 88.0%" |
| Autres attaquants, faux négatifs d'ensemble : Llama-3.3-70B 36,6 % ; Gemma-3-27B 20,4 % ; GPT-OSS-120B 3,8 % | auteurs (tableau 1) | p. 3 | "Llama-3.3-70B 36.6% 12.0% 42.0% 11.3% 4.0% 11.2%" ; "Gemma-3-27B 20.4% 0.0% 22.5% 17.5% 0.0% 21.6%" ; "GPT-OSS-120B 3.8% 4.0% 3.7% 6.2% 0.0% 7.3%" |
| Sous contrainte de scénario (Qwen3-8B, GPT-5, exécutions uniques) : faux négatifs 69,4 %, faux positifs 27,9 % ; scénario « désaligné » : 89,0 % et 3,0 % ; médical : 46,0 % de faux négatifs | auteurs (tableau 3) | p. 6 | "Overall 48.7% 69.4% 27.9%" ; "Misaligned 46.0% 89.0% 3.0%" ; "Medical 39.9% 46.0% 33.7%" |
| Incohérence interne : pour le même attaquant et la même sonde, les tableaux 4 et 6 donnent 76,2 % de faux négatifs en moyenne, contre 69,4 % au tableau 3 ; l'écart vient du scénario médical (80,0 % contre 46,0 %) ; moyennes des cinq scénarios recalculées : 69,4 et 76,2 | calcul | p. 14 | "GPT-5 76.2% 31.8% GPT-5 80.0% 44.2%" |
| Variabilité : la plupart des chiffres reposent sur au moins cinq exécutions ; tableaux 3 et 6 sur une seule | auteurs | p. 8 | "Most numbers reported in the paper are based on at least 5 runs" |

### Antériorité (R8)

- **H2** : n'occupe pas.
- **H1** : n'occupe pas ; la comparaison à des moniteurs génératifs est seulement proposée : "It would also be interesting to apply our approach to classifiers other than probes, such as prompted or fine-tuned LLMs." (p. 8).
- **Lemme d'additivité, théorème négatif** : n'occupe pas.
- **Transposition jeton → action** : n'occupe pas, mais touche sa prémisse : une agrégation à attention, robuste contre l'évasion apprise par renforcement selon le programme, cède ici en partie à un attaquant boîte noire par contenu, au niveau d'une conversation, pour le concept « enjeux élevés » (voir 5.3 et 5.12).
- **HC1** : n'occupe pas (le juge GPT-5 ne sert qu'à établir la vérité de référence).
- **HC2b** : n'occupe pas. Sens inverse seulement : l'attaquant sait aussi faire monter le score par des mots déclencheurs et du jargon : "Financial (FP): Low-cost, one-off digital purchase together with prominent ”scary” legal/IP boilerplate in the prompt" (p. 6).
- **Papier B** : n'occupe pas.
- Hors liste, nécessaire pour la ligne 196 : **HC2** — collision partielle. Le paragraphe 4.3 de l'état de l'art (ligne 155 : « Le seul travail par pur contenu dégrade sans évader (Blandfort & Graham). » ; ligne 157 : « la robustesse vaut pour un attaquant boîte noire en contexte, avec une agrégation robuste et des concepts à forte structure linéaire (tromperie, enjeux élevés) ») est contredit pour le concept « enjeux élevés », avec la réserve des textes entièrement écrits par l'attaquant (hors politique) et d'un seuil fixe à 0,5. Ces deux lignes n'étaient pas dans mes affirmations assignées ; je les signale parce qu'elles reposent sur ce papier.

---

## 6. arXiv 2609.24967v2 — Emergent Collusion in Long-Horizon LLM Agent Interaction

### Identité

- **Titre** : Emergent Collusion in Long-Horizon LLM Agent Interaction.
- **Auteurs (3)** : Xinrui Shi (Stanford University, en visite ; contribution égale), Yanzhe Zhang (Georgia Tech ; contribution égale), Diyi Yang (Stanford University) : "Stanford University Georgia Tech Stanford University" (p. 1).
- **Version, date** : v2 du 26 septembre 2026 (catégorie cs.AI).
- **Venue** : aucune, prépublication.

### Ce qui a été lu

Pages 1 à 10 (corps, déclarations) et 13 à 24 (annexes A à F, début de G) en entier. Pages 25 à 40 (transcriptions qualitatives, annexe G) et 41 à 53 (consignes et schémas d'outils, annexe H) : parcourues par ouverture de page et recherche de mots (probe, activation, monitor, white-box, internal, same model), non lues ligne à ligne. Bibliographie (pp. 10–12) survolée ; une référence vérifiée (Rose et al. 2026).

### Affirmations

Texte vérifié (`docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md`, ligne 171) : « 10. **Papier B, H8, HC2b.** Shi, Zhang, Yang 2026, arXiv 2609.24967 ; Haskins, Chughtai, Engels 2026 ; Nguyen et al. 2025. » Seul 2609.24967 relève de ce lot.

| # | Affirmation du programme | Verdict | Page | Citation exacte |
|---|---|---|---|---|
| 6.1 | l. 171 : « Shi, Zhang, Yang 2026, arXiv 2609.24967 » | confirmé | p. 1 | "Xinrui Shi∗ Yanzhe Zhang∗ Diyi Yang" |
| 6.2 | l. 171 : même affirmation (version lue) | confirmé ; version lue : v2 du 26 septembre 2026 | p. 1 | "arXiv:2609.24967v2 [cs.AI] 26 Sep 2026" |
| 6.3 | l. 171 : pertinence « Papier B » | confirmé comme environnement comportemental : collusion émergente entre deux agents, par défaut deux instances du même modèle ; aucune mesure interne | p. 5 | "By default, two agents are instantiated from the same model and retain their full interaction context across episodes." |
| 6.4 | l. 171 : même pertinence | confirmé (résultat principal) | p. 1 | "Collusion emerges in 94% of trajectories across 10 models, and more capable models within the same family reach it earlier." |
| 6.5 | l. 171 : pertinence « H8, HC2b » | corrigé : « papier B seulement pour cette référence ; aucune sonde ni activation dans l'article, donc rien pour H8 ni HC2b ; son seul lien boîte blanche est la citation de Rose et al. 2026 (arXiv 2604.01151), déjà rangée en collision n° 3 du programme » | p. 9 | "With access to model activations, linear probes offer a complementary approach to detecting strategic deception (Goldowsky-Dill et al., 2025), including collusion through aggregated activation-based signals across agents (Rose et al., 2026)." |
| 6.6 | l. 171 : même affirmation | corrigé (suite : identité de la référence citée) | p. 12 | "Detecting multi-agent collusion through multi-agent interpretability, 2026." |
| 6.7 | l. 171 : même affirmation | corrigé (suite : les états internes ne sont pas lus ; une réflexion écrite les remplace) | p. 9 | "Because we lack direct CoT access for many evaluated models, we use an explicit reflection phase to elicit agents’ stated reasons for actions and awareness of instruction violations." |

**Formulation proposée pour la ligne 171** : « 10. **Papier B, H8, HC2b.** Shi, Zhang, Yang 2026, arXiv 2609.24967 v2 (papier B seulement : collusion comportementale entre deux instances d'un même modèle, sans sonde) ; Haskins, Chughtai, Engels 2026 ; Nguyen et al. 2025. »

### Chiffres utilisables

| Chiffre | Nature | Page | Citation exacte |
|---|---|---|---|
| Collusion : 93,6 % des trajectoires (les « 94 % » du résumé), 66,0 % des épisodes, 78,8 % de trajectoires convergées, dix modèles | auteurs (tableau 1) | p. 5 | "Overall, 66.0% of episodes involve collusion, 93.6% of trajectories contain at least one such episode, and 78.8% satisfy the convergence criterion." |
| Dispositif : 50 trajectoires de 10 épisodes par condition ; messages limités à 200 caractères | auteurs | p. 5 | "For each experimental condition, we use the same N = 50 trajectories sampled from the task pool, each consisting of T = 10 consecutive episodes." ; "limiting each message to 200 characters" |
| Intervention sur le pair : acceptation de 13,6 % à 41,2 % (pair conforme puis pair qui viole) ; de 37,0 % à 55,2 % quand la réciprocité devient visible | auteurs | p. 6 | "Replacing a compliant scripted peer with a violating one raises Gemini-3.1-Flash-Lite’s ACCEPT rate from 13.6% to 41.2%." ; "making the violating peer’s reciprocal ACCEPT observable raises acceptance from 37.0% to 55.2%." |
| Retour à REJECT : 13,5 % après acceptation unilatérale, 4,8 % après acceptation conjointe | auteurs | p. 21 | "Overall, agents revert to REJECT in 13.5% of observations after unilateral acceptance, compared with 4.8% after joint acceptance." |
| Récompense « acceptation » au lieu de « justesse du verdict » : collusion de 72 % à 0 % (Gemini-3.7-Flash) | auteurs | p. 9 | "drops from 72% to 0%" |

### Antériorité (R8)

- **Papier B** : n'occupe pas l'énoncé revendiqué (co-élévation des états internes, sécurité en fonction du nombre d'agents en boîte blanche) : aucune mesure interne, deux agents seulement ; l'extension à plus d'agents est un travail futur : "Future work should study how collusion scales with more agents, evolves under more complex incentives, and varies across different communication channels and interaction structures." (p. 9). Utile comme environnement et organisme de collusion entre copies d'un même modèle.
- **H2** : n'occupe pas ; aucun moniteur : "We examine how instruction violations arise and spread through ordinary communication and feedback, without hidden communication or an active monitor." (p. 9).
- **H1, lemme d'additivité, théorème négatif, transposition jeton → action, HC1** : n'occupe pas.
- **HC2b** : n'occupe pas ; seul voisinage, textuel : les agents reconnaissent par écrit violer le protocole avant d'accepter : "In the following examples, agents explicitly recognize that accepting without the complete raw log violates the verification protocol, yet proceed to accept." (p. 24).

---

## Contrôle des citations

- **Script** : `/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/lecture-lot2-A2b/scripts/controle_citations.py` (empreinte dans `controle-citations.sha256`, même dossier de travail). Il relit ce rapport, rattache chaque citation à son article (titre de section) et à sa page (cellule « p. N » ou mention en prose), puis la cherche sur cette page dans trois extractions (`-layout`, `-raw`, mode par défaut). Seules tolérances : les blancs, partout ; les césures (trait d'union suivi d'un retour à la ligne entre deux lettres). Un trait d'union de la citation doit exister dans le texte.
- **Tests préalables (R5)**, dans `test-controle/` (fichiers `cas-juste.md`, `cas-altere.md`, `cas-deux-colonnes.md`) : 6 citations justes acceptées (une ligne ; césure « over-⏎all » ; prose sur plusieurs lignes ; retour à la ligne après un tiret long ; trait d'union réel en fin de ligne ; texte à deux colonnes) ; 9 altérations rejetées (mot changé deux fois, citation juste à la mauvaise page, prose altérée, chiffre changé deux fois, trait d'union ajouté, trait d'union réel omis en milieu de ligne, mélange de colonnes) ; 3 anomalies de format signalées (citation de tableau sans page, citation coupée par une barre verticale, guillemet non apparié). Limite connue et testée : un mot cité sans le trait d'union qu'il porte en fin de ligne passe (ambiguïté propre à la césure).
- **Incident corrigé** : au premier passage sur ce rapport, une citation contenant une barre verticale a été ignorée sans alerte (elle coupait la cellule du tableau). Le script signale désormais ce cas (test ajouté, ci-dessus) et la citation a été remplacée par une autre de la même page, sans barre verticale.
- **Audit du résultat (R4)** : décompte indépendant des chaînes entre guillemets droits du rapport égal au nombre de citations contrôlées ; copie du rapport où chaque citation est altérée d'un caractère : toutes rejetées.
- **Résultat sur ce rapport** : 151 citations contrôlées, 0 échec, 0 anomalie de format (sortie dans `test-controle/sortie-rapport.txt`).

## Synthèse

1. Corrigées : 2509.26238 « cascade sonde → juge génératif » (cascade interne de termes polynomiaux, juges génératifs seulement témoins) ; 2605.27958 « une seule direction » (première composante principale seule ; la sonde linéaire complète atteint au moins 0,998), « effondrement » (0,485 à la couche 27 contre 0,921 à la couche 34 pour le 27B) et « soutient HC2b » (non testé) ; ligne 146, l'auto-incrimination n'y est pas traitée.
2. 2502.03407 : « motive l'abandon de la moyenne » corrigé, la moyenne y bat le max pour la sonde principale ; chiffres 0,96–0,999 et 95–99 % confirmés, avec réserves (ambiguës exclues, rappel contre un témoin hors sujet, incohérence 96 % / 0,998).
3. 2511.00554 : « dégradation sans évasion » corrigé en évasion partielle (48,9 % des tentatives de faux négatif réussies, 63,6 % sur la seconde moitié des lots, sonde à attention, boîte noire) ; « réduites mais persistantes » et « point de contrôle unique » précisés (contrainte de scénario ; contextes à fortes incitations).
4. Introuvables : les venues « ACL 2026 » (2605.27958) et « ICML 2025 » (2502.03407) ne figurent pas sur les PDF empreintés.
5. Ligne 171 : 2609.24967 ne relève que du papier B (aucune sonde) ; ligne 196 : les deux papiers sont lus, 2511.00554 menace HC2, 2606.07612 la seule prémisse de H8 ; les ⚠ des lignes 135, 158 et 196 peuvent être levés.
6. Zones revendiquées (H2, H1, lemme, théorème, transposition jeton → action, HC1, HC2b, papier B) : aucune occupée ; voisinages à surveiller : HC2b (sonde lue après un démenti imposé, 2502.03407), transposition (prémisse de robustesse des sondes à attention entamée par 2511.00554), HC1 (notation par probabilité des jetons recommandée, 2606.07612).
7. Divergence à remonter, hors des affirmations assignées : les lignes 155 et 157 de l'état de l'art (pur contenu sans évasion ; robustesse « enjeux élevés » face à un attaquant boîte noire en contexte) sont contredites par 2511.00554 : collision partielle sur HC2, qui relève d'une décision de Lazar.
8. Contrôle : 151 citations contrôlées, 0 échec, après tests R5 et audit par altération.
