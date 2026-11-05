# Lecture de l'état de l'art, niveau 2, lot 2 — lecteur C3a « détection d'injection par états internes » — rapport v1

## En-tête

- **Date** : 6 octobre 2026, 16 h 42 en temps universel coordonné (début du travail : 16 h 26).
- **Lecteur** : sous-agent neuf ; n'a écrit aucun des documents vérifiés. Rien n'a été modifié sous `/home/user/controle-ia`.
- **Affirmation vérifiée** : `docs/etat-de-l-art-controle-ia-v1.md`, ligne 137 (texte relu dans le fichier, identique à celui des consignes) : « - **Détection d'injection par états internes** : InstructDetector, arXiv 2505.06311 ; TaskTracker (Abdelnabi et al.) ; Attention Tracker ; PIShield ; arXiv 2608.02657 ; arXiv 2606.22864 ; ESLD, arXiv 2605.18918 ; RouteGuard, arXiv 2604.22888 ; **Prompt Injection as Role Confusion**, arXiv 2603.12277 (sondes de rôle : l'écart entre rôle architectural et rôle perçu détecte l'injection — le travail le plus proche de l'usurpation stylistique). → Injection en bande couverte ; corruption rhétorique non couverte. » Seuls les quatre articles ci-dessous sont dans mon périmètre (TaskTracker, Attention Tracker, PIShield, 2608.02657 et 2606.22864 ne le sont pas).
- **Fichiers lus** (format de document portable, dossier `/home/user/controle-ia/docs/sources/pdf/`, lecture seule). Empreintes sha256 (algorithme de hachage sécurisé, 256 bits) vérifiées **avant** lecture par `sha256sum -c` : toutes conformes.

| fichier | pages | octets | empreinte sha256 (conforme) | lecture |
|---|---|---|---|---|
| `2505.06311v2.pdf` | 16 | 645 499 | `dc3e7d954f9eb6144b5cb9505aeb9683d37eacc500e6fe4a69a170fd1ba558ba` | intégrale |
| `2603.12277v6.pdf` | 33 | 1 722 658 | `609332fdfaae35838e5c82c0ef9a9b7d23aac7ac24000452917c47a56d4f29e0` | intégrale (plus de 30 pages, lu quand même en entier, annexes A à L comprises) |
| `2604.22888v1.pdf` | 12 | 6 769 723 | `9b840e2ac022ed5d2a6e81f397daf390a1c013f1cc10c078885604ef974f82bb` | intégrale |
| `2605.18918v1.pdf` | 12 | 328 397 | `b808b44783e4864f0bb0e1b3e68772ec97547683c72a0df14352f68b0580b5a2` | intégrale |

- **Méthode** : texte extrait par `pdftotext -layout`, page par page ; **les pages citées sont le rang dans le fichier**. Figures lues par leurs légendes et leurs étiquettes extraites ; trois pages rendues en image pour vérifier des tableaux et des figures : 2604.22888 p. 8, 2603.12277 p. 19 et p. 27. Ces images ont ensuite été supprimées pour libérer le disque, saturé par d'autres tâches ; on les régénère par `pdftoppm -f N -l N -r 110 -png`.
- **Non lu ou non vérifié** : aucune page omise. Les figures sans couche texte n'ont pas été examinées en image, sauf les trois pages ci-dessus. Les dépôts de code et les pages de projet cités par les articles n'ont pas été consultés. Aucune page arXiv n'a été consultée : les dates de première version et les venues non imprimées dans les fichiers restent non vérifiées.
- **Verdicts** : « confirmé » ; « corrigé » (avec la formulation à mettre à la place) ; « introuvable ». **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi, scripts dans `scripts/`).
- **Sigles qui apparaissent dans les citations anglaises** (citées mot pour mot) : LLM = large language model (grand modèle de langage) ; IPI = indirect prompt injection (injection indirecte de consigne) ; ASR = attack success rate (taux de succès d'attaque) ; CoT = chain of thought (chaîne de pensée) ; BIPIA = banc d'essai d'injections indirectes (Yi et al.), sigle non développé dans ces fichiers ; XPIA = cross-prompt injection attack (injection indirecte, dans un contenu externe) ; UPIA = user prompt injection attack (injection directe, dans la requête) ; LDA = linear discriminant analysis (analyse discriminante linéaire) ; BAcc = balanced accuracy (exactitude équilibrée) ; AUC = area under the curve (aire sous la courbe de fonctionnement du récepteur) ; AHS = score d'accaparement de l'attention, sigle non développé par les auteurs ; F1 = moyenne harmonique de la précision et du rappel ; PMLR = Proceedings of Machine Learning Research ; EMNLP = Empirical Methods in Natural Language Processing ; ACL = Association for Computational Linguistics ; cs.CR et cs.CL = catégories arXiv « cryptographie et sécurité » et « calcul et langage ».

## 1. arXiv 2505.06311v2 — Defending against Indirect Prompt Injection by Instruction Detection

### 1.0 Identité

- **Titre** : Defending against Indirect Prompt Injection by Instruction Detection.
- **Auteurs** (8) : Tongyu Wen, Chenglong Wang, Xiyuan Yang (tous trois premiers auteurs à égalité), Haoyu Tang, Yueqi Xie, Lingjuan Lyu, Zhicheng Dou, Fangzhao Wu. Affiliations : Renmin University of China ; Peking University Shenzhen Graduate School ; Wuhan University ; University of Science and Technology of China ; Hong Kong University of Science and Technology ; Sony AI ; Microsoft Research Asia (p. 1). Les métadonnées du fichier donnent la même liste.
- **Version et date** : v2, 17 septembre 2025, catégorie cs.CR (tampon arXiv, ligne 1.A5). La date de la v1 n'est pas imprimée.
- **Venue** : **non imprimée dans ce fichier** (les remerciements mentionnent des relecteurs anonymes, p. 9). Deux fichiers tiers la citent de façon contradictoire. 2603.12277v6 p. 13 donne « Findings of the Association for Computational Linguistics: EMNLP 2025, pp. 19472–19487 », avec la bonne liste d'auteurs et un identifiant d'objet numérique (ligne 2.A4). 2604.22888v1 p. 10 donne « Findings of … ACL 2025, pages 18714–18735 », mais avec quatre coauteurs absents de ce fichier (ligne 3.A7), donc non fiable. Venue la plus probable : Findings of EMNLP 2025, **par citation tierce seulement**.
- **Ce que lit le détecteur** : le modèle Llama-3.1-8B-Instruct, qui lit la **donnée externe seule**. Il extrait l'état caché du dernier jeton à la couche 14 et les gradients des couches d'auto-attention de la couche 14, avec la réponse appariée « Sure » ; ces deux signaux sont fusionnés dans un perceptron multicouche (p. 4–5). Il ne lit ni l'agent qui agit ni un moniteur.

### 1.1 Affirmations du programme

| # | affirmation du programme (ligne 137) | verdict | page | citation exacte |
|---|---|---|---|---|
| 1.1a | « Détection d'injection par états internes : InstructDetector, arXiv 2505.06311 » | confirmé. Précision : états cachés **et gradients**, que l'article appelle « behavioral states » | p. 1 | "In this paper, we propose InstructDetector, a novel detection-based approach that leverages the behavioral states of LLMs to identify potential IPI attacks." |
| 1.1b | (suite) | confirmé | p. 1 | "Specifically, we demonstrate the hidden states and gradients from intermediate layers provide highly discriminative features for instruction detection." |
| 1.1c | (suite : quel modèle est lu) | confirmé : c'est le modèle qui lit la donnée externe seule | p. 4 | "To leverage hidden states as features, we first take external data as the input of the LLM and extract the hidden states corresponding to the last token at each layer." |
| 1.2a | « → Injection en bande couverte » (pour cet article) | confirmé : l'article ne traite que d'instructions logées dans la donnée externe | p. 1 | "We recognize that IPI attacks fundamentally rely on the presence of instructions embedded within external content, which can alter the behavioral states of LLMs." |
| 1.2b | (suite : chiffres de tête) | confirmé, avec réserves (section 1.3) | p. 1 | "InstructDetector achieves a detection accuracy of 99.60% in the in-domain setting and 96.90% in the out-of-domain setting, and reduces the attack success rate to just 0.03% on the BIPIA benchmark." |
| 1.3 | « corruption rhétorique non couverte » (pour cet article) | confirmé : les exemples positifs sont fabriqués par insertion d'instructions ; aucune influence sans ordre n'est testée. Règle R8 : c'est une limite de l'article, pas un trou du champ | p. 5 | "Negative samples are derived from external datasets, and positive samples are generated by randomly inserting instructions into negative samples." |

### 1.2 Citations d'appui (réserves, antériorité)

| # | objet | constat | page | citation exacte |
|---|---|---|---|---|
| 1.A1 | réplication | une seule exécution pour tous les résultats | p. 14 | "For all reported results, we present outcomes from a single run." |
| 1.A2 | robustesse affirmée | affirmée dans la section « Ethical Impact », jamais testée (aucun attaquant adaptatif) : réserve R4 | p. 9 | "it would be exceedingly difficult for attackers to circumvent our detection." |
| 1.A3 | antériorité H1 (voisinage) | un détecteur boîte noire (le modèle interrogé directement) échoue face aux états internes | p. 6 | "LLM (Zero-shot), which directly queries the model, exhibits almost no capability to identify hidden instructions." |
| 1.A4 | antériorité H2 (voisinage faible) | plusieurs instructions dans **un même** document améliorent un peu la détection ; rien de séquentiel | p. 15 | "Results in Table 9 reveal a trend that detection accuracy shows a certain degree of improvement as the number of inserted instructions increases." |
| 1.A5 | version et date | tampon arXiv | p. 1 | "arXiv:2505.06311v2 [cs.CR] 17 Sep 2025" |

### 1.3 Chiffres utilisables

| chiffre | objet | page | nature | réserve |
|---|---|---|---|---|
| 99,60 % et 96,90 % | exactitude de détection : dans le domaine (Wikipédia et LaMini) et hors domaine le plus éloigné (articles de presse et BIPIA) ; 2 000 échantillons par combinaison | p. 1, 5, 6 (tableau 1) | auteurs | une seule exécution (1.A1) ; mesure d'exactitude, aucun taux de faux positifs publié ; instructions insérées au hasard ; « trop beau » (R4) avec 200 exemples d'entraînement |
| 0,03 % | taux de succès d'attaque résiduel sur BIPIA, meilleur des quatre modèles cibles (Vicuna-7B) ; 0,10 à 0,13 % pour les trois autres ; sans défense : 24,06 à 39,68 % | p. 1, 6 (tableau 2) | auteurs | le résumé retient le minimum des quatre cibles |
| 95,95 % et 89,45 % | TaskTracker, dans le domaine et hors domaine | p. 6 (tableau 1) | auteurs | modèle public de TaskTracker réutilisé (p. 14) |
| 70,55 % et 71,35 %, contre 99,40 % et 99,55 % | TaskTracker contre InstructDetector quand l'instruction externe ressemble à celle de l'utilisateur | p. 15 (tableau 8) | auteurs | deux scénarios seulement |
| 44,65 % à 74,10 % ; 91,70 % | hors domaine : détecteurs par simple interrogation du modèle ou par contrôle de la réponse ; modèle affiné comme classifieur de texte | p. 6 (tableau 1) | auteurs | exactitude, pas à taux de faux positifs égal |
| 200 (100 et 100) ; plus de 95 % avec 50 | taille d'entraînement | p. 5, 8 | auteurs | — |
| couche 14 sur 32 ; 4 096 ; 400 000 | couche retenue ; dimension de l'état caché ; dimension des gradients après réduction par maximum | p. 4 | auteurs | — |
| 68,55 % | modèle de base non instruit, hors domaine | p. 8 (tableau 4) | auteurs | — |
| 94,25 % et 92,05 % | chinois et thaï, hors domaine | p. 9 (tableau 5) | auteurs | jeux traduits automatiquement |

### 1.4 Antériorité (R8 : ce que cette source occupe, et rien de plus)

| zone revendiquée | occupation par cet article | justification |
|---|---|---|
| H2 | non occupée | Classification ponctuelle de chaque document, apprise avec des exemples d'attaque. Aucune accumulation séquentielle, aucun processus e ni martingale, aucun seuil calibré en faux positifs, aucun horizon. Voisinage faible : plusieurs instructions dans un même document (1.A4). |
| H1 | non occupée (voisine) | Les états internes battent la boîte noire (1.A3), mais sur des **ordres explicites** insérés, mesurés en exactitude, pas à taux de faux positifs égal, et sans sabotage diffus. |
| lemme d'additivité | non occupée | — |
| théorème négatif | non occupée | — |
| transposition jeton → action | non occupée | Dernier jeton seulement. La réduction par maximum porte sur les paramètres des gradients, pas sur des jetons ni des actions. |
| HC1 | non occupée | Aucun juge sous pression graduée. |
| HC2b | non occupée | La sonde lit le modèle qui lit la donnée, pas l'agent qui manipule. |
| papier B | non occupée | Une seule copie de modèle. |
| hors liste : HC3, versant « ordres en bande » | pertinente | Sa prémisse (1.2a) est exactement la détection d'un contenu « en forme d'ordre » dans le canal des données. Elle montre une détection élevée mais pas quasi certaine hors domaine (96,90 %, une exécution, sans attaquant adaptatif). |

## 2. arXiv 2603.12277v6 — Prompt Injection as Role Confusion

### 2.0 Identité

- **Titre** : Prompt Injection as Role Confusion.
- **Auteurs** (3) : Charles Ye et Jasmine Cui (contribution égale ; « Independent »), Dylan Hadfield-Menell (Massachusetts Institute of Technology) (p. 1).
- **Version et date** : v6, 27 juin 2026, catégorie cs.CL (ligne 2.A3). La date de la v1 n'est pas imprimée : la date 2026-02-22 du fichier `docs/sources/pdf/provenance-niveau2-lot2-v1.md` n'est donc pas vérifiable sur ce fichier.
- **Venue** : International Conference on Machine Learning 2026 (43e édition, Séoul ; Proceedings of Machine Learning Research, volume 306), imprimé p. 1 (ligne 2.A1). Attention : la v6 contient une section (7.3) **absente de la version des actes** (ligne 2.A2).
- **Nature** : étude de mécanisme et attaque, **pas un détecteur**. Les sondes de rôle sont des régressions logistiques multinomiales par couche. Elles sont entraînées sur un même texte neutre (corpus de préentraînement nommés « C4 » et « Dolma 3 ») placé sous différentes balises de rôle (système, utilisateur, chaîne de pensée, assistant, outil), soit environ 1 250 séquences et 1,28 million de jetons par modèle (p. 5, 26). Elles lisent le **modèle attaqué** (quatre modèles ouverts de 20 à 120 milliards de paramètres ; ligne 2.A9). L'attaque CoT Forgery, en boîte noire, est testée sur six modèles d'OpenAI et trois autres.

### 2.1 Affirmations du programme

| # | affirmation du programme (ligne 137) | verdict | page | citation exacte |
|---|---|---|---|---|
| 2.1 | Article rangé sous « Détection d'injection par états internes » | **corrigé**. À mettre à la place : « Prompt Injection as Role Confusion, arXiv 2603.12277 (Ye, Cui, Hadfield-Menell ; International Conference on Machine Learning 2026) : étude de mécanisme, pas détecteur ; la détection par l'écart entre rôle voulu et rôle mesuré n'y est qu'une question ouverte. » | p. 10 | "Finally, detection: could discrepancies between the intended role and the probe-measured role flag injection attempts before generation?" |
| 2.2 | « sondes de rôle » | confirmé | p. 1 | "We design role probes to measure how LLMs internally perceive “who is speaking,” and find that injected text occupies the same representational space as the trusted role it imitates." |
| 2.3a | « l'écart entre rôle architectural et rôle perçu » | confirmé pour la notion d'écart | p. 4 | "We trace this failure to the gap between tag-based intent and how models internally represent roles." |
| 2.3b | « … détecte l'injection » | **corrigé**. À mettre à la place : « le degré de confusion de rôle mesuré par les sondes (le texte injecté est représenté comme le rôle qu'il imite) prédit le succès de l'attaque avant la génération : de 9 % à 90 % de succès entre le quantile le plus bas et le plus haut pour CoT Forgery (626 tentatives), de 2 % à 70 % pour des injections d'agent (1 000 tentatives) ; aucune détection n'est testée. » | p. 1 | "Strikingly, the degree of role confusion predicts attack success before a single token is generated." |
| 2.3c | (suite) | (idem) | p. 7 | "The lowest-confusion quantile succeeds 9% of the time; the highest succeeds 90%." |
| 2.3d | (suite) | (idem) | p. 8 | "Attack success rises near-monotonically with Userness: the lowest quantile succeeds just 2% of the time, while the highest succeeds 70%." |
| 2.4a | « le travail le plus proche de l'usurpation stylistique » | **corrigé**. Le comparatif « le plus proche » ne se vérifie pas sur ces sources. Mais l'article fait plus qu'approcher : il **occupe en partie** le versant stylistique. À mettre à la place : « il occupe en partie le versant stylistique de l'usurpation : à argument constant, ôter le style de la chaîne de pensée imitée fait tomber le succès de l'attaque de 61 % à 10 % ; mais la charge contient toujours un ordre ou une requête nuisible, la cible est le modèle attaqué (ni un juge ni un moniteur) et aucune sonde ne lit l'agent auteur. » | p. 4 | "Destyling collapses ASR from 61% to 10%, consistent across all models (full results in Section D)." |
| 2.4b | (suite : le style est isolé du contenu) | (idem) | p. 18 | "This isolates style from content: if attack success depends on argument quality, destyled forgeries should perform comparably; if it depends on stylistic mimicry, they should fail." |
| 2.4c | (suite : un ordre est toujours présent) | (idem) | p. 16 | "CoT Forgery Injection: The same command, augmented with a 1-paragraph forged CoT justifying the exfiltration." |
| 2.4d | (suite : la requête nuisible est toujours présente) | (idem) | p. 3 | "For a harmful query Q, an auxiliary LLM generates fabricated reasoning C that mimics the target model’s CoT style while justifying compliance" |
| 2.4e | (suite : le juge ne sert qu'à noter l'issue) | (idem) | p. 16 | "Attack success is determined by an LLM judge (same auxiliary model)." |
| 2.5a | « corruption rhétorique non couverte » (pour cet article) | **corrigé** (nuance). À mettre à la place : « pour cet article : injection en bande couverte, y compris par un faux raisonnement justificatif dont l'effet tient au style et non à la plausibilité de l'argument ; influence sans aucun ordre seulement envisagée (annexe L.1, déclarée spéculative) ; corruption rhétorique d'un juge ou d'un moniteur non traitée. » | p. 4 | "Absurd justifications and plausible justifications achieve comparable ASRs: 60% vs. 63% (Section C)." |
| 2.5b | (suite : influence sans ordre, spéculée) | (idem) | p. 33 | "No command is issued, yet the external text has steered the model’s behavior." |
| 2.5c | (suite : statut spéculatif) | (idem) | p. 32 | "These are speculative and not empirically validated in this work" |

### 2.2 Citations d'appui (identité, réserves, antériorité)

| # | objet | constat | page | citation exacte |
|---|---|---|---|---|
| 2.A1 | venue | International Conference on Machine Learning 2026 | p. 1 | "Proceedings of the 43 rd International Conference on Machine Learning, Seoul, South Korea. PMLR 306, 2026." |
| 2.A2 | écart avec les actes | la section 7.3 de la v6 n'est pas dans les actes | p. 9 | "This section was added later, and is not present in the proceedings version of this paper." |
| 2.A3 | version et date | tampon arXiv | p. 1 | "arXiv:2603.12277v6 [cs.CL] 27 Jun 2026" |
| 2.A4 | venue de 2505.06311 selon cet article | Findings of EMNLP 2025 | p. 13 | "Defending against indirect prompt injection by instruction detection. In Findings of the Association for Computational Linguistics: EMNLP 2025, pp. 19472–19487." |
| 2.A5 | HC2b (contrôle du style) | des sondes entraînées sur les **seules balises** répondent au **style** | p. 1 | "Yet they classify prompt-injected text as its spoofed role, not its true tagged role — responding to style despite being trained only on tags." |
| 2.A6 | HC2b (suite) | le modèle code style et balise comme un même signal | p. 1 | "This means the model itself encodes style and tags as the same signal, and that equivalence is the mechanism behind prompt injection." |
| 2.A7 | HC3 : le style seul, sans balise ni ordre, déplace le rôle perçu (en représentation seulement) | conversation bénigne de jardinage, sans balises | p. 22 | "To the model’s internal world, looking like reasoning is indistinguishable from being tagged as reasoning." |
| 2.A8 | H2 (voisinage faible) | montée progressive de la confusion **dans le modèle attaqué**, au fil des jetons ; ce n'est pas un test séquentiel d'un moniteur | p. 28 | "This “progressive conviction” effect—where stylistic cues gradually convince the model the text is its own thoughts—occurs consistently across all harmful content types." |
| 2.A9 | portée des sondes | quatre modèles de 20 à 120 milliards de paramètres | p. 10 | "We probe on four models in the 20-120B size range; extending to larger models is future work." |
| 2.A10 | réserve sur 61 % → 10 % | le tableau 2 est donné pour gpt-oss-20b seul, avec la même ligne de base que la moyenne sur six modèles | p. 19 | "Results on gpt-oss-20b are shown in Table 2." |
| 2.A11 | réserve sur la figure 24 | le texte dit 3,2 %, la carte de chaleur affiche 9,4 % (image vérifiée) | p. 28 | "Standard CoT forgeries (left) achieve high CoTness (79.1%) with minimal Userness (3.2%)" |
| 2.A12 | seule aire sous la courbe de l'article | elle prédit l'échec de la hiérarchie d'instructions, pas la présence d'une injection | p. 32 | "A regression on the Systemness/Userness ratio achieves .74 AUC, substantially outperforming baseline regressions using token count (.59), mean activation norms (.60), and shuffled-label controls (.52)." |

### 2.3 Chiffres utilisables

| chiffre | objet | page | nature | réserve |
|---|---|---|---|---|
| 60 % | succès moyen de CoT Forgery sur StrongREJECT (313 requêtes nuisibles), six modèles ; de 17 % (GPT-5) à 94 % (gpt-oss-120b) | p. 1 ; figure 2 p. 3 | auteurs ; figure ; calcul : 60,2 % | lignes de base de 0 à 4 % |
| de 56 à 70 %, contre 0 à 2 % (26 % pour gpt-oss-20b) | détournement d'agent (exfiltration) : CoT Forgery contre injection standard, 100 attaques par modèle | p. 4 (figure 3), p. 16 | auteurs | jeu de données construit par les auteurs |
| 61 % → 10 % ; baisse moyenne de 51 points | effet d'ôter le style à argument constant, moyenne sur six modèles | p. 4, p. 19 (figure 18) | auteurs ; calcul sur la figure 18 : 60,28 % → 9,73 %, soit 50,55 points | **réserve** : le tableau 2 (p. 19) donne aussi 61 % → 10 % pour gpt-oss-20b seul, alors que la figure 18 donne 78,6 % → 11,7 % pour ce modèle (image vérifiée) |
| 61 % → 26 % ; − 19 points | ablation syntaxique seule ; remplacement du seul bigramme « The user » | p. 19 (tableau 2) | auteurs | même réserve sur la ligne de base |
| 60 % contre 63 % | justifications absurdes contre plausibles | p. 4 | auteurs | — |
| de 9 % à 90 % | succès entre le quantile de confusion le plus bas et le plus haut, 626 tentatives (avec et sans style) | p. 7 (figure 9) | auteurs | intervalles de confiance par rééchantillonnage à 95 % tracés, non chiffrés |
| de 2 % à 70 % | même lecture pour 1 000 injections d'agent (212 gabarits, gpt-oss-20b) | p. 8 (figure 10), p. 30 | auteurs | tirages avec remise |
| 6,01 (erreur type 1,30 ; p < 0,001) | coefficient de l'« Userness » dans une régression logistique du succès, à rôle déclaré contrôlé | p. 31 (tableau 4) | auteurs | erreurs types groupées par gabarit |
| de 75,7 % à 87,6 % ; au plus 19,5 % | « Userness » d'un texte de style utilisateur placé sous balise outil ; « Toolness » | p. 6 (tableau 1), p. 23 | auteurs | quatre modèles ouverts |
| 79 %, 68 %, 29 % | « CoTness » du faux raisonnement, du vrai raisonnement, du faux raisonnement sans style | p. 7, p. 27–28 | auteurs | **réserve** : 3,2 % d'« Userness » selon le texte, 9,4 % sur la figure 24 (2.A11) |
| 0,74, contre 0,59, 0,60 et 0,52 | aire sous la courbe pour prédire l'échec de la hiérarchie d'instructions (160 exemples) | p. 32 | auteurs | ce n'est pas une détection d'injection |
| 92 %, 84 %, 74 % | CoT Forgery sur GLM-4.6, Kimi-K2-Instruct, Minimax-M2 | p. 17 | auteurs | — |

### 2.4 Antériorité (R8)

| zone revendiquée | occupation par cet article | justification |
|---|---|---|
| H2 | non occupée | Aucune accumulation de scores de sonde, aucun seuil, aucun taux de faux positifs. La « conviction progressive » (2.A8) est une dynamique du modèle attaqué, pas une statistique de moniteur. |
| H1 | non occupée | Aucune comparaison avec un moniteur boîte noire à taux de faux positifs égal ; aucun sabotage. |
| lemme d'additivité ; théorème négatif | non occupées | — |
| transposition jeton → action | non occupée | Sondes par jeton, moyennées sur un passage pour la mesure ; aucune étude de robustesse de l'agrégation. |
| HC1 | non occupée | Le juge ne fait que noter l'issue (2.4e) ; aucune pression graduée sur un juge ou un moniteur. |
| HC2b | non occupée, mais **pertinente** | Les sondes lisent le modèle attaqué, pas l'agent qui manipule. En revanche, l'article montre que des sondes entraînées sans style répondent au style (2.A5, 2.A6) : cela appuie le « contrôle obligatoire du style » de HC2b. |
| papier B | non occupée | — |
| hors liste : **HC3 (usurpation stylistique)**, visée par la ligne 137 | **partielle** | Occupé : (i) l'effet causal du style à argument constant sur l'obéissance du modèle attaqué (2.4a, 2.4b), y compris par composantes (syntaxe, lexique) ; (ii) le style seul, sans balise ni ordre, déplace le rôle perçu, en représentation seulement (2.A7). Non occupé : une influence **sans aucun ordre** avec effet sur le comportement (seulement spéculée, 2.5b et 2.5c) ; une cible juge ou moniteur ; un gain g mesuré par dose-réponse sous pression graduée ; une sonde lisant l'agent auteur. Conséquence 1 : la mention « versant stylistique vierge » (`docs/etat-de-l-art-controle-ia-v1.md`, ligne 242) est à nuancer : partiellement occupé sur le modèle attaqué ; non occupé, dans ces sources, pour un juge moniteur sans ordre. Conséquence 2 : la prédiction « g nul sur les sondes » de HC3 ne peut valoir que pour des sondes lisant l'agent auteur, car des sondes lisant le modèle lecteur sont déplacées par le style selon cet article. |

## 3. arXiv 2604.22888v1 — RouteGuard: Internal-Signal Detection of Skill Poisoning in LLM Agents

### 3.0 Identité

- **Titre** : RouteGuard: Internal-Signal Detection of Skill Poisoning in LLM Agents.
- **Auteurs** (5) : Wenjie Xiao (University of Chinese Academy of Sciences ; Institute of Information Engineering, Chinese Academy of Sciences), Xuehai Tang (Institute of Information Engineering ; auteur correspondant), Biyu Zhou (Institute of Information Engineering), Songlin Hu et Jizhong Han (tous deux University of Chinese Academy of Sciences et Institute of Information Engineering) (p. 1).
- **Version et date** : v1, 24 avril 2026, catégorie cs.CR (ligne 3.A11).
- **Venue** : non imprimée. Le texte parle de « revised submission » et de « submission-level claim suitable for top-tier venues » (3.A6) : document de travail, aucune venue.
- **Ce que lit le détecteur** : un modèle gelé (Qwen3-32B ou Meta-Llama3.1-8B), interrogé par plusieurs **invites** que l'article appelle « probes » (3.A10 ; ce ne sont pas des sondes linéaires). Il lit l'attention conditionnée par la réponse et l'alignement des états cachés sur le fichier de compétence, **avant exécution** (p. 2, 5–7).

### 3.1 Affirmations du programme

| # | affirmation du programme (ligne 137) | verdict | page | citation exacte |
|---|---|---|---|---|
| 3.1 | « Détection d'injection par états internes : … RouteGuard, arXiv 2604.22888 » | confirmé. Précision : détection, avant exécution, de l'empoisonnement de **compétences** d'agents (instructions malveillantes dans un fichier de compétence), par l'attention et les états cachés d'un modèle gelé ; transfert vérifié sur l'injection indirecte ordinaire (BIPIA) | p. 1 | "Motivated by this mechanism, we propose RouteGuard, a frozen-backbone detector that combines response-conditioned attention and hidden-state alignment signals through reliability-gated late fusion." |
| 3.2 | « → Injection en bande couverte » (pour cet article) | confirmé, avec de fortes réserves sur les chiffres (section 3.3) | p. 1 | "an attacker can hide malicious instructions inside a skill that already looks like legitimate guidance and thereby hijack the agent’s goal." |
| 3.3 | « corruption rhétorique non couverte » (pour cet article) | confirmé : seules des instructions malveillantes sont traitées. Limite de l'article (R8) | p. 2 | "We formulate skill poisoning as malicious-instruction detection inside an instruction-like carrier" |

### 3.2 Citations d'appui (chiffres, réserves, antériorité)

| # | objet | constat | page | citation exacte |
|---|---|---|---|---|
| 3.A1 | chiffres de tête | 0,8834 et 90,51 % : voir les réserves de calcul ; 90,51 % n'a aucun tableau source | p. 1 | "on the critical Skill-Inject channel slice, it reaches 0.8834 F1 and recovers 90.51% of description attacks missed by lexical screening." |
| 3.A2 | conclusion d'ablation | contredite au calcul sur la tranche « canal » (section 3.3) | p. 8 | "Across all three slices, the fused detector outperforms both single-expert variants." |
| 3.A3 | objectif à budget de faux positifs | α n'est jamais fixé ; aucun taux de faux positifs n'est publié | p. 3 | "minimize attack miss subject to a benign-block budget α." |
| 3.A4 | métrique | précision, rappel et F1, à seuil non donné | p. 7 | "Following the experiment plan in the optimization outline, we report precision, recall, and F1." |
| 3.A5 | comparateurs | reproduits d'après les articles, pas réexécutés | p. 9 | "Fourth, several comparison systems are paper-faithful reproductions rather than exact reruns of original released pipelines." |
| 3.A6 | statut du texte | document de travail | p. 9 | "Taken together, these results support a submission-level claim suitable for top-tier venues" |
| 3.A7 | citation erronée d'InstructDetector | quatre coauteurs absents du fichier 2505.06311v2, venue et pages différentes de 2.A4 | p. 10 | "Tongyu Wen, Chenglong Wang, Xiyuan Yang, Haoyu Tang, Weiran Yao, Jiacheng Wang, Ruoxi Jia, and Ruiyi Zhang. 2025. Defending against indirect prompt injection by instruction detection. In Findings of the Association for Computational Linguistics: ACL 2025, pages 18714–18735." |
| 3.A8 | lien entre déplacement d'attention et succès | non monotone ; effectifs non imprimés | p. 11 | "Under a strict output-level criterion, ASR rises across delta-AHS buckets from 0.2500 at q1 to 1.0000 at q5, with intermediate values 0.4167, 0.6667, and 0.5833." |
| 3.A9 | transposition jeton → action (voisinage) | agrégation par maximum sur des fenêtres de document, et par moyenne ou maximum sur les couches et les invites ; aucune étude de robustesse | p. 6 | "the attention expert uses aggregated statistics such as mean, max, late-minus-early trend, and probe consistency to produce an attention-side risk score" |
| 3.A10 | sens de « probes » | ce sont des invites | p. 6 | "including generic answer, invocation-decision, safe-use planning, and execution-boundary prompts." |
| 3.A11 | version et date | tampon arXiv | p. 1 | "arXiv:2604.22888v1 [cs.CR] 24 Apr 2026" |
| 3.A12 | attribution de BIPIA | attribué à Liu et al. ; 2505.06311 (p. 5) et 2605.18918 (p. 4) l'attribuent à Yi et al. | p. 11 | "BIPIA Ordinary IPI (Liu et al., 2023a,b)" |

### 3.3 Chiffres utilisables, avec une réserve majeure (R4)

Calcul (`scripts/f1_coherence.py`, sortie dans `calculs-routeguard.txt`). Pour les deux experts seuls et pour les comparateurs, le F1 imprimé est égal à la moyenne harmonique de la précision et du rappel imprimés, ou un peu inférieur (écarts de − 0,08 à + 0,03), à une exception près : RENNERVATE sur MaliciousAgentSkillsBench (+ 0,19). Pour **RouteGuard**, il la dépasse de **+ 0,12 à + 0,20 sur tous les bancs d'empoisonnement de compétences**. La moyenne harmonique est concave : une moyenne de F1 sur plusieurs exécutions ne peut pas dépasser la moyenne harmonique des précision et rappel moyens. L'article ne définit pas son F1. Sur le rendu image de la page 8, le bloc « Malicious Agent Skills in the Wild » du tableau 1 recopie chiffre pour chiffre le bloc « MaliciousAgentSkillsBench » ; seul le F1 de RouteGuard diffère (0,7427 contre 0,7867), avec une précision et un rappel identiques.

| chiffre | objet | page | nature | réserve |
|---|---|---|---|---|
| 0,8834 (précision 0,9334 ; rappel 0,6442) | F1 de RouteGuard, Skill-Inject, tranche « canal » | p. 1, 8 (tableaux 2 et 3) | auteurs | recalculé : 0,7623, **sous** l'expert d'attention seul (0,7637) ; l'affirmation 3.A2 tombe sur cette tranche |
| 0,7528 ; 0,7945 ; 0,7867 ; 0,7427 | F1 de RouteGuard : Skill-Inject ; tranche « par ligne » ; MaliciousAgentSkillsBench ; Malicious Agent Skills in the Wild | p. 8 | auteurs | recalculés : 0,5528 ; 0,6573 ; 0,6054 ; 0,6054. Sur la tranche « par ligne », RouteGuard passe **derrière** « MSkills » (0,7601) et « Probe » (0,7127), abréviations de l'article qui désignent vraisemblablement MalSkills et SkillProbe (correspondance non explicitée, p. 7 et 11). Ailleurs il reste premier, mais l'écart avec le deuxième fond, par exemple 0,6054 contre 0,5832 sur MaliciousAgentSkillsBench |
| 90,51 % | attaques « description » manquées par le filtrage lexical et retrouvées | p. 1, 2 | auteurs | aucun tableau ni figure source dans le fichier |
| 0,8537 (précision 0,7501 ; rappel 0,9944), contre 0,7815 | transfert sur BIPIA : RouteGuard contre RENNERVATE | p. 9 (tableau 5) | auteurs | cohérent au calcul (0,8551) : seul chiffre de RouteGuard utilisable sans réserve de calcul |
| de 0,25 à 1,00 (0,4167 ; 0,6667 ; 0,5833) | succès d'attaque par quintile de déplacement d'attention | p. 11 | auteurs | non monotone ; toutes les valeurs sont des multiples de 1/12, ce qui est compatible avec 12 cas par tranche (ou un multiple de 12) : petits effectifs non imprimés (calcul) |
| 1,8868 contre 0,5786 | mots-indices d'instruction pour 100 jetons : compétences bénignes contre contextes BIPIA bénins | p. 11 | auteurs | — |

### 3.4 Antériorité (R8)

| zone revendiquée | occupation par cet article | justification |
|---|---|---|
| H2 | non occupée | Un seul criblage avant exécution, par compétence. Budget α non fixé (3.A3), aucun taux de faux positifs publié, apprentissage avec des exemples empoisonnés, aucune accumulation le long d'une trajectoire. |
| H1 | non occupée (voisine) | Les signaux internes battent le criblage textuel, y compris un filtrage au niveau de l'invite (PromptArmor, p. 5 et 11). Mais il s'agit d'ordres explicites, mesurés en F1 à seuil non donné, avec les anomalies de calcul ci-dessus. |
| transposition jeton → action | non occupée | Maximum sur des fenêtres de document (3.A9), sans étude de robustesse et sans actions d'agent. |
| lemme d'additivité ; théorème négatif ; HC1 ; HC2b ; papier B | non occupées | Le modèle lu est celui qui va exécuter la compétence, lu avant l'action. Aucun juge, aucune manipulation par l'agent, une seule copie. |

## 4. arXiv 2605.18918v1 — ESLD (External Surrogate Latent Defense): A Latent-Space Architecture for Faster, Stronger Prompt-Injection Defense

### 4.0 Identité

- **Titre** : ESLD (External Surrogate Latent Defense): A Latent-Space Architecture for Faster, Stronger Prompt-Injection Defense.
- **Auteur** (1) : Yash Narendra, affiliation « Microsoft », adresse personnelle (p. 1).
- **Version et date** : v1, 18 mai 2026, catégorie cs.CR (ligne 4.A8).
- **Venue** : non imprimée.
- **Ce que lit le détecteur** : un **modèle garde** (LlamaGuard-3, ShieldGemma-9B, Granite-Guardian-8B, WildGuard-7B), et non l'agent. Le détecteur est une sonde linéaire, une analyse discriminante linéaire régularisée, posée sur l'état caché du **dernier jeton** d'une couche intermédiaire (ligne 4.A9). L'évaluation laisse de côté, à chaque pli, une source d'attaque et une source bénigne ; elle est moyennée sur cinq graines et comporte un audit de fuite entre sources (p. 4–6).

### 4.1 Affirmations du programme

| # | affirmation du programme (ligne 137) | verdict | page | citation exacte |
|---|---|---|---|---|
| 4.1 | « Détection d'injection par états internes : … ESLD, arXiv 2605.18918 » | confirmé. Précision : sonde linéaire sur les états cachés d'un **modèle garde** | p. 2 | "ESLD, a simple external surrogate detector that classifies an LLM’s prefill-stage hidden states for prompt-injection detection." |
| 4.2a | « → Injection en bande couverte » (pour cet article) | confirmé pour les injections indirectes | p. 4 | "The XPIA (indirect) attack candidates come from indirect-injection benchmarks: XPIA (Liu et al., 2024), BIPIA (Yi et al., 2024), InjecAgent (Zhan et al., 2024), and AgentDojo (Debenedetti et al., 2024)." |
| 4.2b | (suite) | précision : le lot « direct » est fait surtout de requêtes nuisibles et de collections de contournement, pas d'injections proprement dites | p. 4 | "The UPIA (direct) attack candidates come from publicly released red-teaming and adversarial query collections" |
| 4.3 | « corruption rhétorique non couverte » (pour cet article) | confirmé : seules des attaques tirées de bancs publics sont utilisées, sans influence sans ordre ni attaquant adaptatif. Limite de l'article (R8) | p. 9 | "ESLD is evaluated on attack distributions drawn from public benchmarks." |

### 4.2 Citations d'appui (chiffres, réserves, antériorité)

| # | objet | constat | page | citation exacte |
|---|---|---|---|---|
| 4.A1 | chiffre de tête | gain sur le verdict du garde lui-même | p. 1 | "improves detection accuracy over the guard’s own verdict by 16.4 percentage points on average" |
| 4.A2 | chiffre de tête (détail) | 7 cellules sur 8 | p. 6 | "ESLD improves balanced accuracy over the host guard verdict on 7 of 8 (host, task) cells, with a mean improvement of +16.4 percentage points." |
| 4.A3 | seuil | seuil par défaut de l'analyse discriminante, contre le verdict binaire du garde : deux points de fonctionnement différents, donc **pas à taux de faux positifs égal** | p. 5 | "ESLD uses the default LDA decision threshold, s(x) ≥ 0; no decision threshold is tuned on validation or test data." |
| 4.A4 | robustesse | aucun attaquant adaptatif | p. 9 | "The probe is not stress-tested against an attacker who has white-box access to the host’s hidden states" |
| 4.A5 | H2 (voisinage faible) | contrôles séquentiels, mais indépendants ; l'argument porte sur la latence seulement | p. 8 | "In an agentic trajectory with k sequential safety checks, this design reduces the cumulative latency tax from k times guard cost to k times ESLD cost" |
| 4.A6 | H2 (suite) | chaque appel d'outil est contrôlé isolément | p. 8 | "where each tool call is checked in isolation" |
| 4.A7 | réserve de calcul, annexe B | voir section 4.3 | p. 11 | "the worst outer BAcc cost is 0.011 (LlamaGuard-3 / XPIA, 0.9124 → 0.9032)" |
| 4.A8 | version et date | tampon arXiv | p. 1 | "arXiv:2605.18918v1 [cs.CR] 18 May 2026" |
| 4.A9 | ce qui est lu | dernier jeton d'une couche | p. 3 | "The hidden state at the final input token of layer L is used as the feature vector" |

### 4.3 Chiffres utilisables

| chiffre | objet | page | nature | réserve |
|---|---|---|---|---|
| + 16,4 points | gain moyen d'exactitude équilibrée de la sonde sur le verdict du même garde (7 cellules sur 8) | p. 1, 6, 7 (tableau 1) | auteurs ; calcul : 16,35 | pas à taux de faux positifs égal (4.A3) ; aucun attaquant adaptatif (4.A4) |
| de 0,91 à 0,92, contre 0,50 à 0,72 | exactitude équilibrée sur les injections indirectes : sonde contre garde | p. 7 | auteurs | le garde ShieldGemma-9B est au hasard (0,5034) |
| − 2,6 points | seule cellule perdue : WildGuard-7B, attaques directes | p. 7 | auteurs | — |
| 3,29 (de 2,35 à 4,18) | accélération, moyenne géométrique | p. 6, 8 (tableau 2) | auteurs ; calcul : 3,292, cohérent avec les latences du tableau 2 | une seule carte graphique A100, lot de taille 1 |
| au moins 0,88 | aire sous la courbe de la sonde, toutes cellules | p. 7, 8 | auteurs | — |
| 1 500 et 1 500 ; 5 graines | taille d'entraînement par découpage ; nombre de graines | p. 4 | auteurs | — |
| 0,011 | « pire coût » de l'annexe B, attribué à LlamaGuard-3 sur injections indirectes | p. 11 | auteurs | **réserve de calcul** : pour cette cellule, le tableau 4 (p. 12) donne 0,9124 − 0,9032 = 0,0092 ; la valeur 0,011 correspond aux cellules Granite-Guardian-8B (0,0109 et 0,0111). Erreur mineure, sans effet sur les chiffres de tête |

### 4.4 Antériorité (R8)

| zone revendiquée | occupation par cet article | justification |
|---|---|---|
| H1 | non occupée, mais **voisine la plus nette** des quatre | Une sonde sur les activations d'un garde (un moniteur) bat le verdict généré du **même** garde de 16,4 points en moyenne (4.A2). Mais : injections et requêtes nuisibles explicites, pas de sabotage diffus ; points de fonctionnement différents, donc pas à taux de faux positifs égal (4.A3) ; c'est le moniteur qui est lu, pas l'agent. À citer comme antériorité de « sonde contre juge sur le même modèle, hors attaque ». |
| H2 | non occupée | Contrôles indépendants (4.A5, 4.A6). Seuil non calibré en faux positifs, apprentissage avec 1 500 exemples d'attaque par découpage. |
| transposition jeton → action | non occupée | Dernier jeton seulement ; l'agrégation sur plusieurs jetons est laissée en perspective (p. 8). |
| lemme d'additivité ; théorème négatif ; HC1 ; HC2b ; papier B | non occupées | Aucune pression graduée sur le garde, aucune manipulation par l'agent, aucune copie multiple. |

## Formulation proposée pour la ligne 137 (en remplacement de la parenthèse et de la conclusion)

« … ESLD, arXiv 2605.18918 (sonde linéaire sur les états cachés d'un modèle garde) ; RouteGuard, arXiv 2604.22888 (empoisonnement de compétences d'agents ; F1 publiés incohérents avec leurs précision et rappel, chiffres non opposables) ; **Prompt Injection as Role Confusion**, arXiv 2603.12277 (Ye, Cui, Hadfield-Menell ; International Conference on Machine Learning 2026 ; étude de mécanisme, pas détecteur). Des sondes de rôle entraînées sur les seules balises montrent que le texte injecté est représenté comme le rôle qu'il imite, et le degré de cette confusion prédit le succès de l'attaque avant génération ; la détection par l'écart entre rôle voulu et rôle mesuré y reste une question ouverte. L'article occupe en partie le versant stylistique de l'usurpation : à argument constant, ôter le style fait passer le succès de 61 % à 10 %. Mais c'est sur le modèle attaqué, avec un ordre présent, sans juge ni sonde de l'agent auteur. → Injection en bande couverte ; usurpation stylistique d'un rôle couverte en partie, sur le modèle attaqué ; corruption rhétorique d'un juge ou d'un moniteur, sans ordre, non couverte par ces quatre sources. »

## Contrôle des citations

- Script : `scripts/controle_citations.py`, lancé avec `python3 -I`. Il ne tolère que les blancs et les césures (un trait d'union suivi d'un saut de ligne). Il cherche d'abord dans le texte `pdftotext -layout` de la page indiquée, puis, pour les passages qui chevauchent les deux colonnes, dans le texte `pdftotext -raw` **de la même page**, qui suit l'ordre des colonnes et garde les césures.
- **Garde testée d'abord (R5)** : 15 cas, tous conformes avant le contrôle. Cas justes : une colonne, deux colonnes, césure, mot composé coupé, blancs. Cas altérés ou refusés : un mot changé, un chiffre changé, une bonne phrase sur la mauvaise page, une césure altérée, une apostrophe droite au lieu de typographique, une casse changée, une citation trop courte, une page absente, un article inconnu. La lecture du rapport par le script a été testée sur un mini-rapport : ligne juste acceptée, ligne altérée en échec, ligne sans page et ligne hors article refusées.
- Incident de test, documenté : mon premier cas « bonne phrase, mauvaise page » a été **trouvé** en page 2. Vérification faite, l'article répète cette phrase dans son introduction (page 2). Le défaut était dans mon cas de test, pas dans la garde ; le cas a été remplacé par une phrase propre à la page 1 (légende de la figure 1).
- **Résultat sur ce rapport : 65 citations contrôlées, 0 échec, 0 refus** ; 21 trouvées dans le texte `-layout`, 44 seulement dans le texte `-raw` de la même page (passages en deux colonnes). Sortie complète : `controle-citations.txt`.

## Synthèse (dix lignes au plus)

1. Empreintes des quatre fichiers conformes ; quatre articles lus en entier ; 65 citations contrôlées par script, 0 échec.
2. Aucune affirmation introuvable. **Corrigées** (2603.12277) : ce n'est pas un détecteur ; les sondes de rôle **prédisent le succès** de l'attaque (de 9 à 90 %, de 2 à 70 %), la détection par l'écart y est une **question ouverte** (p. 10).
3. Corrigé aussi : « le plus proche de l'usurpation stylistique ». Il **occupe en partie** ce versant : à argument constant, ôter le style fait passer le succès de 61 % à 10 %. Mais c'est sur le modèle attaqué, avec un ordre présent, sans juge ni sonde de l'agent auteur.
4. Nuance sur « corruption rhétorique non couverte » : 2603.12277 couvre de faux raisonnements justificatifs dont l'effet tient au style. L'influence sans ordre n'y est que spéculée ; aucun juge ni moniteur n'est visé.
5. Confirmé, avec précisions : InstructDetector (états cachés et gradients ; une seule exécution), RouteGuard (compétences d'agents), ESLD (sonde sur un **modèle garde**).
6. Réserve majeure (R4) sur RouteGuard : ses F1 dépassent de 0,12 à 0,20 la moyenne harmonique de ses propres précision et rappel, et un bloc du tableau 1 est recopié. Recalculé, il perd la tranche « par ligne » de Skill-Inject et ne bat plus son expert d'attention seul sur la tranche « canal ».
7. Venues : 2603.12277 = International Conference on Machine Learning 2026 (imprimé ; la v6 diffère des actes) ; 2505.06311 = Findings of EMNLP 2025 par citation tierce seulement ; les deux autres n'en ont pas.
8. Zones revendiquées : H2, lemme d'additivité, théorème négatif, transposition jeton → action, HC1, HC2b et papier B ne sont occupés par aucune des quatre sources.
9. H1 est voisine sans être occupée : ESLD (+ 16,4 points, sonde contre verdict du même garde) n'est ni à taux de faux positifs égal ni sur du sabotage. HC2b trouve un appui : des sondes sans style répondent au style (2603.12277).
10. Hors liste : HC3 est partiellement occupée. « Versant stylistique vierge » (ligne 242) est à nuancer, et « g nul sur les sondes » ne vaut que pour une sonde lisant l'agent auteur.
