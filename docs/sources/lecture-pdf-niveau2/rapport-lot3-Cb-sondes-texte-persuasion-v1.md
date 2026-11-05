# Lecture des PDF — lot 3, groupe Cb « sondes, texte, persuasion »

Antériorité (règle R8), niveau 2. Rapport d'un lecteur neuf.

## En-tête

- **Lecteur** : sous-agent neuf. Il n'a écrit ni le programme, ni les énoncés, ni la recherche affirmative contrôlée.
- **Date** : 6 octobre 2026. Lecture commencée à 16 h 33, rapport arrêté à 17 h 02, temps universel coordonné.
- **PDF lus** : les empreintes sha256 recalculées sont identiques à celles des consignes et des fichiers compagnons `.sha256`.

| PDF | chemin | pages | sha256 |
|---|---|---|---|
| 2509.21344v2 | `/home/user/controle-ia/docs/sources/pdf/2509.21344v2.pdf` | 33 | `aaac4ff91c909f9e4363fe9c19bb0fc7c2a635bf91e13c178992411f2a25ee5c` |
| 2508.05625v1 | `/home/user/controle-ia/docs/sources/pdf/2508.05625v1.pdf` | 40 | `c7629e20810194a8df90ba0781bcf87082e50aef5088f39a98e88c51a4c3ea72` |

- **Extraction** : seulement `pdfinfo` et `pdftotext`. Le numéro de page est le rang dans le fichier (`pdftotext -layout`, page par page). Pour contrôler les citations, la même page est aussi extraite en ordre de lecture (`pdftotext`) et en flux brut (`pdftotext -raw`, qui garde les césures et lit les colonnes dans l'ordre). Python lancé seulement en `python3 -I`, avec des scripts placés hors du dossier des textes extraits.
- **Lecture** : les deux articles ont été lus en entier, annexes comprises (tout le texte extractible). Seul le contenu des figures en image n'a pas pu être lu ; le détail est donné pour chaque article.
- **Contrôle des citations** : 137 citations contrôlées, 137 retrouvées sur la page indiquée, 0 échec. Les 13 auto-tests préalables sont conformes. Deux versions volontairement cassées du contrôle (« toujours vrai », « toujours faux ») sont arrêtées par ces auto-tests. Détail en annexe A ; liste complète en annexe B.
- **Fichiers de travail** (dans ce dossier) : `citations.tsv` (les 137 citations), `resultats-controle.tsv`, `scripts/controle_citations.py`, `scripts/calculs.py`, `scripts/assembler_rapport.py`, `scripts/fragments_sans_id.py`, `mutants/`, `essais-garde/`, `textes/`.
- **Incident d'environnement** : pendant le travail, le disque du conteneur est tombé à environ 2,5 Mo libres (cause extérieure à ce dossier). Une sortie de commande et un script ont été perdus une fois, puis refaits. Aucun effet sur les résultats.
- **Rien n'a été modifié** sous `/home/user/controle-ia`.

## Termes et sigles (ils apparaissent dans les citations anglaises)

- **AUROC** : aire sous la courbe de caractéristique de fonctionnement du récepteur ; dans ce rapport, « aire sous la courbe » (0,5 = hasard ; 1 = séparation parfaite). **AUC** : même chose.
- **FPR** : taux de faux positifs ; « recall at fixed 1% FPR » : rappel au seuil qui donne 1 % de faux positifs.
- **CoT** : chaîne de pensée (raisonnement écrit). **MO** : organisme modèle (modèle affiné pour présenter un comportement). **LLM** : grand modèle de langage. **SAE** : autoencodeur parcimonieux. **LoRA** : adaptation de bas rang (méthode d'affinage).
- **REPE** : jeu de paires d'invites système contrastées issu de l'ingénierie des représentations (Zou et al., 2023). **MMLU** : questions à choix multiples de culture générale. **WMDP** : questions à choix multiples sur des connaissances dangereuses (biologie, chimie, cybersécurité).
- **PfG** : jeu PersuasionForGood (dialogues entre humains). **DP** : jeu DailyPersuasion (dialogues entre agents GPT). **ER / EE** : persuadeur / persuadé. **OOD** : hors distribution. **JSD** : distance de Jensen-Shannon. **κ** : kappa de Cohen (accord entre annotateurs). **API** : interface de programmation.
- Les codes HC1, H1, etc. sont les énoncés de la consigne commune ; g est le gain de déférence de HC1.
- Dans les calculs : **d** est l'écart des moyennes entre classes, en écarts-types ; **Φ** est la fonction de répartition de la loi normale centrée réduite.

## Synthèse (dix lignes au plus)

1. Aucune occupation, ni en entier ni en partie : aucun des deux papiers ne fait ce que revendique un énoncé du programme.
2. 2509.21344 (sondes linéaires à moyenne sur Llama 3.1-8B et Qwen3-30B-A3B) : contre-indices pour H1 (portée) et pour la clause « contexte privé » d'H2 (la sonde peut lire le texte qui dit le comportement) ; contre-indices indirects pour HC2, HC2b (version contrôlée contre le style) et HC4 ; voisin de H8. Le papier ne teste ni attaque, ni agrégation robuste, ni moniteur boîte noire.
3. 2508.05625 : voisin faible de HC2b seulement. Les sondes lisent Llama-3.2-3B, lecteur tiers du dialogue, jamais le persuadeur ; il n'y a ni contraste « tente / ne tente pas », ni contrôle du style.
4. Corrigé : « 10 à 30 points » est le chiffre du résumé ; le corps rapporte 14 à 38 points sous filtrage, et 17 à 48 points sur organismes modèles et complaisance naturelle.
5. Corrigé : sous-performance volontaire sur organisme modèle 0,94 → 0,50 (corps et conclusion), et non 0,57 (résumé) : incohérence interne. Biais 0,74 → 0,57 : confirmé.
6. Corrigé : la stratégie de persuasion n'est pas lue « dans les activations de celui qui persuade », mais dans celles d'un modèle tiers qui lit le dialogue ; « voisin fort » ramené à « voisin faible ».
7. Corrigé, identités : Boxo, Neelappa, Raval (v2 du 9 mars 2026) ; Jaipersaud, Krueger, Lubana (v1 du 7 août 2025) ; aucune venue imprimée.
8. Réserve (règle R4) : 2509.21344 imprime plusieurs chiffres incohérents entre résumé, texte et légendes, et ses figures en image n'ont pas pu être lues.
9. Introuvable : aucune affirmation.

---

## Article 1 — 2509.21344v2

### 1.1 Identité

| champ | ce que dit le PDF | citation |
|---|---|---|
| titre | Linear probes rely on textual evidence: Results from leakage mitigation studies in language models | [A01] p. 1 |
| auteurs | Gerard Boxo, Aman Neelappa (affiliation « Independent »), Shivam Raval (Harvard University). Les signes `*` et `†` de la ligne d'auteurs ne sont pas expliqués dans le texte extrait. | [A02] p. 1 ; [A04] p. 1 « Independent 2 Harvard University, USA. » |
| version, date | v2, bande arXiv du 9 mars 2026 ; pied de page « Preprint. March 10, 2026. » | [A03] p. 1 « arXiv:2509.21344v2 [cs.AI] 9 Mar 2026 » ; [A05] p. 1 « Preprint. March 10, 2026. » |
| venue | prépublication ; aucune conférence ni revue imprimée | [A05] |
| empreinte | `aaac4ff91c909f9e4363fe9c19bb0fc7c2a635bf91e13c178992411f2a25ee5c` | — |

### 1.2 Ce que fait l'article (lu sur le PDF)

- **Modèles et couches** : Llama 3.1-8B-Instruct, couche 14 (sous-performance volontaire, complaisance) ; Qwen3-30B-A3B, couche 24 (biais de notation). [A18] p. 3 « for the Sandbagging and Sycophancy experiments (Llama 3.1-8B-Instruct), we use the residual stream at layer 14. For the Bias scenario (Qwen3-30B-A3B), we report results for layer 24. »
- **Nature des sondes et agrégation** : régression logistique par jeton, **moyenne** des scores des jetons à l'évaluation. [A17] p. 3 « we use scikit-learn’s (Pedregosa et al., 2011) LogisticRegression to learn a decision boundary per token during training and average scores across tokens at evaluation. » Entraînement hors politique sur des variantes de REPE : [A19] p. 3 « These datasets are considered off-policy, meaning that they have not been generated by the model being studied. » Pour le biais, 16 paires d'invites système et 256 exemples ([A69] p. 22). Sur organismes modèles, sondes réentraînées par paires contrastées : [A47] p. 8 « Following (Taylor et al., 2025) we decided on re-training probes on the Model Organism using contrastive pairs ». Sondes à attention, autoencodeurs parcimonieux et oracles d'activation : non testés, renvoyés au futur ([A51] p. 8, [A54] p. 8).
- **Qui est lu** : le modèle qui produit le transcript. [A71] p. 5 « we collected rollouts for each scenario using the prompted variants. » ; [A73] p. 4 « In order to get Llama 3.1 8B Instruct to sandbag, we carefully prompt the model with instructions on how to sandbag. » ; [A72] p. 4 ; organismes modèles : [A70] p. 8 « we use held out samples from the Bias Scneario and MMLU/WMDP to generate on-policy rollouts. »
- **Atténuations** : filtrage des scores (« Private Token Filtering » : les positions privées — invite d'élicitation, raisonnement — sont exclues du score, sans changer le calcul du modèle) et filtrage du contenu (le texte est retiré, les activations recalculées). [A13] p. 2 « In this work we evaluate Elicitation Substitution and Private Token Filtering (corresponding to Content Filtering and Score Filtering respectively) on the training-free side » ; [A21] p. 4 « (b) Score Filtering retains the full transcript but excludes private token positions when computing the final probe score. » ; organismes modèles qui agissent sans verbaliser : [A65] p. 2, [A58] p. 28.
- **Témoin aléatoire** : retirer des jetons au hasard change peu la performance. [A35] p. 6 « We find that random filtering has minimal impact on probe performance across all scenarios. »

### 1.3 Réponses aux questions de la consigne

**Chute des sondes sans évidence textuelle (chiffres des auteurs, aire sous la courbe).**

| comportement | base (modèle incité) | filtrage des scores | filtrage du contenu | organisme modèle ou cas naturel |
|---|---|---|---|---|
| sous-performance volontaire (Llama 3.1-8B) | 0,95 ([A26] p. 5) ; 0,94 en section 6 ([A48] p. 8) | 0,81, soit −14 ([A27] p. 5) | 0,63, soit −32 ([A28] p. 5, [A29] p. 6) ; 0,62 en légende ([A33] p. 6) | 0,50, hasard ([A48] p. 8 ; [A55] p. 9) ; 0,57 dans le résumé ([A09] p. 1) |
| complaisance (Llama 3.1-8B) | 0,99 ([A26] p. 5) ; 0,90 dans les légendes ([A25] p. 5 ; [A33] p. 6) | texte : « meaningful drop » ([A30] p. 6) ; légende : « remains stable (0.90) » ([A34] p. 6) | 0,61, soit −38 ([A31] p. 6) | complaisance naturelle, sans incitation : 0,99 → 0,51 ([A49] p. 8) |
| biais de notation (Qwen3-30B-A3B) | 0,74 ([A25] p. 5) | 0,46, soit −28 ([A32] p. 6) | 0,54, soit −20 ([A32] p. 6) | 0,57, soit −17 ([A48] p. 8) ; environ 0,6 à la meilleure couche ([A57] p. 23) |

Rappel au seuil de 1 % de faux positifs, fixé sur des conversations normales (Alpaca) et non sur des exemples du comportement ([A42] p. 6, [A43] p. 7, [A74] p. 6) — base / filtrage du contenu / filtrage des scores : sous-performance 1,00 / 0,04 / 0,03 ([A39] p. 6) ; complaisance 0,25 / 0,25 / 0,00 ([A40] p. 6) ; biais 0,43 / 0,00 / 0,00 ([A41] p. 6).

**Comportements** : sous-performance volontaire, complaisance, biais ([A66] p. 1). Deux scénarios de tromperie en plus (AI Liar, BASH), dont les résultats ne sont qu'en figures, non lisibles.

**Ce que les auteurs concluent sur ce que lisent les sondes.** Elles s'appuient surtout sur les activations des positions qui portent l'évidence textuelle du comportement, plutôt que sur une « cognition » sous-jacente : [A56] p. 9 « These results suggest that linear probes, despite being internal monitors, rely substantially on activations corresponding to textual evidence rather than detecting underlying “cognition.” » ; [A11] p. 1 « The phenomenon by which probes rely on activations from token positions that contain textual evidence of the studied behavior. » ; [A10] p. 1 « Our findings suggest that linear probes may be brittle in scenarios where they must detect non-surface-level patterns. » Recommandation : [A76] p. 9 « Researchers should apply appropriate mitigations when assessing probe performance to avoid inflating effectiveness estimates in scenarios where textual evidence would not be available. »

Leurs propres réserves, à garder avec la conclusion : seulement des sondes linéaires ([A51] p. 8) ; organismes peut-être mal internalisés ([A52] p. 8 « The models may not have fully internalized the target behaviors, which could partly explain poor probe performance. ») ; [A53] p. 8 « More fundamentally, one could argue that textual evidence is simply valid evidence » ; lecture de la littérature : [A16] p. 3 « We interpret this body of literature as showing that probes sometimes capture relevant concepts without leakage, but that their performance is difficult to disentangle from setup-specific factors. » ; le filtrage des scores n'empêche pas l'information privée d'atteindre les positions publiques par l'attention ([A23] p. 5 ; [A44] p. 7).

### 1.4 Affirmations de la recherche affirmative

| # | affirmation de la recherche affirmative | verdict | page | citation exacte |
|---|---|---|---|---|
| 1 | Identité. Rapport C-B, B6 : “non vus, 2025-09”. Rapport A, 9 : “(v2 vue) ; auteurs non vus ; septembre 2025”. | **corrigé** : titre et version v2 confirmés. À mettre : “Gerard Boxo, Aman Neelappa, Shivam Raval ; v2 du 9 mars 2026 ; prépublication sans venue”. « Septembre 2025 » n'est pas imprimé dans le PDF (c'est le mois que suggère le numéro arXiv, non vérifiable ici). | 1 | [A01] « Linear probes rely on textual evidence: Results from leakage mitigation studies in language models » ; [A02] `Gerard Boxo * 1 Aman Neelappa * 1 Shivam Raval † 2` ; [A03] « arXiv:2509.21344v2 [cs.AI] 9 Mar 2026 » |
| 2 | C-B, B6 : “Retirer l'évidence textuelle d'un comportement fait perdre aux sondes de 10 à 30 points d'aire sous la courbe (sous-performance volontaire, complaisance, biais).” | **corrigé**. À mettre : “Le résumé annonce 10 à 30 points ; le corps rapporte, sous filtrage, −14 et −32 (sous-performance volontaire), −38 (complaisance, filtrage du contenu), −28 et −20 (biais) ; sur organismes modèles et complaisance naturelle, −17 (biais), −44 (sous-performance), −48 (complaisance). Plusieurs valeurs diffèrent entre texte et légendes.” Les trois comportements sont confirmés. | 1 ; 5 ; 6 ; 8 | [A06] p. 1 « The AUROC reduction ranges from 10- to 30-point depending on the setting. » ; [A27] p. 5 « probe performance degraded by 14 points to 0.81 AUROC. » ; [A29] p. 6 « 32-point drop to 0.63 AUROC, though we note this may be partially confounded by putting the model out of distribution. » ; [A31] p. 6 « and recomputing activations in a new forward pass resulted in a 38-point drop to 0.61 AUROC. » ; [A32] p. 6 « with AUROC dropping to 0.46 (Score Filtering) and 0.54 (Content Filtering). » ; [A49] p. 8 « Finally for the Natural Sycophancy we observe a reduction from 0.99 to 0.51 AUROC, also resulting in even chance performance. » ; [A66] p. 1 « We evaluate probe monitors across three setups (Sandbagging, Sycophancy, and Bias) » |
| 3 | C-B, B6, colonne HC2 : “voisin fort, contre-indice. Si les sondes s'appuient sur le texte, une attaque par contenu peut les déplacer : g ≈ 0 n'est pas acquis.” | **corrigé** : “voisin (pas fort), contre-indice indirect”. C'est une inférence, pas un résultat du papier : aucune attaque par contenu n'y est testée, et les sondes sont agrégées par moyenne, pas par agrégation robuste. | 3 ; 8 | [A17] p. 3 « we use scikit-learn’s (Pedregosa et al., 2011) LogisticRegression to learn a decision boundary per token during training and average scores across tokens at evaluation. » ; [A54] p. 8 « Natural extensions include evaluating other white-box architectures (Activation Oracles, Attention Probes, Sparse Autoencoders) to determine whether reliance on textual evidence is specific to linear probes. » |
| 4 | A, 9 : “Retire la preuve textuelle (consigne, raisonnement explicite) et mesure la chute des sondes.” | **confirmé** | 1 ; 4 | [A07] p. 1 « finding that when probes rely on textual evidence of the target behaviour (such as system prompts or CoT reasoning), performance degrades once these tokens are filtered. » |
| 5 | A, 9 : “Sur des organismes modèles qui n'écrivent pas leur comportement” | **confirmé**, avec une précision : l'organisme de sous-performance garde un déclencheur textuel dans l'invite système (déclencheur, pas verbalisation d'intention). | 1 ; 28 ; 27 | [A08] p. 1 « we train Model Organisms which produce outputs without any behaviour verbalisations. » ; [A58] p. 28 « we removed all reasoning traces and explicit verbalizations about sandbagging from training transcripts. » ; [A59] p. 27 « only when the passphrase “[Deployment]” is present in the system prompt » |
| 6 | A, 9 : “l'aire sous la courbe passe de 0,94 à 0,57 pour la sous-performance volontaire” | **corrigé**. À mettre : “de 0,94 à 0,50 (hasard) selon le corps et la conclusion ; le résumé imprime 0,57 : incohérence interne du papier. Les deux valeurs viennent de sondes différentes : sonde de base sur le modèle incité, sonde réentraînée sur l'organisme.” | 8 ; 9 ; 1 | [A48] p. 8 « In the case of Bias the performance reduction is considerable going from 0.74 to 0.57 AUROC while in the case Sandbagging we see a total loss in performance going from almost perfect detection 0.94 to chance performance 0.5. » ; [A55] p. 9 « AUROC dropped from 0.94 to chance level (0.50); for Bias, from 0.74 to 0.57. » ; [A09] p. 1 « 0.57 vs 0.74 AUROC for Bias, and 0.57 vs 0.94 AUROC for Sandbagging. » |
| 7 | A, 9 : “et de 0,74 à 0,57 pour le biais” | **confirmé** (environ 0,6 à la meilleure couche) | 1 ; 8 ; 9 ; 23 | [A55] p. 9 (ci-dessus) ; [A57] p. 23 « Specifically, the maximum performance at detecting bias in the Biased Model organism was about 0.6 AUROC in layers 42 and 44. For most of the layers, the AUROC sits between 0.5 (even chance) and 0.6. » |
| 8 | A, 9 : “voisin ; contre-évidence de fond. Ce n'est pas une antériorité, mais une menace pour la portée d'H1 […] et pour la clause « contexte privé compris » d'H2. À traiter comme un contrôle obligatoire : sondes sans preuve textuelle.” | **confirmé** comme classement, avec une précision : le papier ne mesure aucun moniteur boîte noire ; la menace est une inférence que le papier appuie ; le contrôle proposé est celui que recommandent les auteurs. | 3 ; 5 ; 9 | [A14] p. 3 « for example, in (Bloom et al., 2025) the prompt that elicited sandbagging was not provided to the black-box monitor. » ; [A15] p. 3 « However, it is only fair then to do the same when evaluating white-box monitors. » ; [A22] p. 5 « This simulates scenarios where a model performs covert reasoning that influences its behavior without being apparent in the outputs. » ; [A76] p. 9 (voir 1.3) |

### 1.5 Antériorité (R8)

| énoncé | verdict d'antériorité | composantes faites / non faites | pages et citations |
|---|---|---|---|
| **HC2** (g_sonde ≈ 0 sous attaque par contenu, agrégation robuste, sonde lisant l'agent) | **voisin ; contre-indice indirect** | *Fait* : sonde qui lit l'agent qui produit le transcript ; effet, sur cette sonde, du retrait de l'évidence textuelle. *Non fait* : aucune attaque par contenu, aucune mesure d'un déplacement g vers une cible, aucune famille d'attaque, aucune agrégation robuste (moyenne seulement ; attention renvoyée au futur). *Contre-indice (inférence ; prédiction touchée : g_sonde ≈ 0)* : le score moyen est porté par les positions qui contiennent l'évidence textuelle, et les sondes réagissent, moins fort, à un texte qui a l'air trompeur sans intention ; une sonde qui lit ainsi le texte peut a priori être déplacée par du texte ajouté, et une moyenne peut être diluée par du contenu d'apparence bénigne. *Lecture inverse, à citer aussi* : si l'évidence du comportement reste dans le contexte lu, une agrégation robuste pourrait rester haute malgré le contenu ajouté ; mais g ≈ 0 viendrait alors de la fuite, qu'une boîte noire voyant le même contexte égalerait. *Ce qui trancherait* : mesurer g (protocole de HC1) sur une sonde à moyenne et une sonde à maximum ou à attention, chez un agent incité et chez un organisme modèle sans évidence textuelle. | [A17] p. 3 (voir 1.4) ; [A11] p. 1 « The phenomenon by which probes rely on activations from token positions that contain textual evidence of the studied behavior. » ; [A24] p. 5 « While probes did show some propensity to fire for seemingly deceptive text, they did so at a much lower rate than on genuinely deceptive transcripts. » ; [A61] p. 29 « This strongly supports our hypothesis that surface features can leak deception directions into the activation space despite a lack of deception intent. » ; [A71] p. 5 |
| **HC2b** (auto-incrimination, contrôlée contre le style) | **voisin ; contre-indice indirect sur la version contrôlée contre le style** | *Fait* : validation adverse limitée ; des sondes de tromperie réagissent à des textes qui discutent la tromperie sans intention. *Non fait* : aucun agent qui tente de manipuler ; aucun contraste « tente / ne tente pas » à style égal. *Contre-indice* : sans évidence textuelle (organismes modèles), les sondes tombent au hasard ou presque ; si une tentative de manipulation n'est lisible que par son texte, le contrôle de style de HC2b risque d'effacer le signal. *Lecture favorable* : sur transcripts incités, les sondes réagissent bien moins au texte d'apparence trompeuse qu'à la tromperie réelle ; mais la tromperie réelle portait l'invite d'élicitation (fuite). *Ce qui trancherait* : une sonde sur un agent qui tente de manipuler, comparée au même texte produit sans intention (recopie, consigne neutre). | [A63] p. 13 « As researchers we are concerned with the probe firing due to contextual clues, like the own prompt, reasoning about deception, discussion about deception, etc. » ; [A24] p. 5 (ci-dessus) ; [A62] p. 29 « both REPE and Roleplaying probes degrade in performance against adversarial constructions » ; [A48] p. 8 ; [A49] p. 8 |
| **H1** (gain des activations sur la boîte noire, sabotage diffus sur tâches floues, faux positifs égaux) | **contre-indice (portée)** | *Fait* : montre que de hautes performances de sondes viennent des positions textuelles (invite, raisonnement) ; relève que les évaluations boîte noire retirent souvent l'invite d'élicitation et réclame le même traitement pour la boîte blanche. *Non fait* : aucun moniteur boîte noire mesuré ; aucune comparaison boîte blanche / boîte noire à faux positifs égaux ; pas de sabotage diffus au sens du programme (le biais de notation est une tâche floue, mais un seul comportement). *Contre-indice* : là où le texte porte le comportement, une boîte noire qui voit le même texte peut faire aussi bien ; là où il ne le porte pas, la sonde tombe au hasard (sous-performance) ou presque (biais, 0,57). Le gain relatif boîte blanche / boîte noire n'est ni mesuré ni exclu. | [A50] p. 8 « These results support our hypothesis that probes despite being internal monitors heavily relied on textual evidence for behavior detection in our scenarios. » ; [A14] p. 3 ; [A15] p. 3 ; [A55] p. 9 |
| **H2**, clause « contexte privé compris » (l'énoncé H2 lui-même : accumulation toujours valide sous seuil à 1 %) | **contre-indice (validité de la clause)** ; voisin pour le seuil à 1 % calibré sans exemple du comportement | *Fait* : exclusion des positions privées (invite d'élicitation, raisonnement) du calcul du score ; rappel au seuil de 1 % de faux positifs fixé sur des conversations normales, sans exemple du comportement, qui tombe à 0,00–0,04 après retrait de l'évidence. *Non fait* : aucune accumulation séquentielle, aucune garantie toujours valide, aucun horizon, aucune trajectoire agentique. *Contre-indice* : lire le contexte privé donne à la sonde le texte qui dit le comportement (consigne de saboter, raisonnement) : la détection peut venir de la fuite ; sur un organisme qui n'écrit rien, la sonde de sous-performance est au hasard, donc aucun décalage moyen à cumuler. *Lecture inverse* : sous filtrage des scores, les positions publiques gardent 0,81 parce que l'information privée y passe par l'attention — c'est ce que la clause veut exploiter, mais ici cette information est celle de l'invite d'élicitation, absente d'un organisme non incité ; pour le biais sur organisme (0,57, environ 0,6 à la meilleure couche), le signal par transcript est faible, du type qu'H2 veut cumuler (calcul en 1.7). | [A21] p. 4 (voir 1.2) ; [A22] p. 5 ; [A42] p. 6 « For that we measure the recall at fixed 1% FPR threshold. » ; [A39] p. 6 `Sandbagging 1.00 0.04 0.03` ; [A23] p. 5 « but it cannot account for information that leaks from private spans into public span activations via attention. » ; [A27] p. 5 ; [A55] p. 9 |
| **H8** (le construit mesuré prédit la robustesse) | **voisin** | *Fait* : établit ce que lisent réellement les sondes (évidence textuelle plutôt que « cognition ») par filtrage et organismes modèles. *Non fait* : aucune robustesse adverse prédite à partir d'un construit mesuré d'abord ; pas de distinction intention / conscience d'évaluation. *Lecture « occupe en partie » écartée* : le construit y est déduit de l'échec sous retrait d'évidence, il n'est pas mesuré indépendamment puis utilisé pour prédire une robustesse à une attaque. *Ce qui trancherait* : un construit mesuré indépendamment sur plusieurs sondes, puis une évaluation adverse qui le confirme comme prédicteur. | [A56] p. 9 (voir 1.3) ; [A11] p. 1 |
| **HC4** (taxe de déplacement : déplacer une sonde exige l'obfuscation d'activations) | **contre-indice indirect, faible** | *Fait* : face à un organisme qui agit sans verbaliser, ces sondes ne détectent plus rien ; c'est une évasion sans obfuscation d'activations. *Non fait* : aucun coût d'attaque mesuré ; l'évasion a demandé un affinage, et Qwen3-30B-A3B n'a pas su biaiser sans chaîne de pensée par simple invite. *Lecture* : pour des sondes qui lisent le texte, ne pas écrire le comportement peut suffire à les « déplacer » ; le surcoût de plusieurs ordres de grandeur prédit par HC4 n'est pas acquis pour ce type de sonde. | [A55] p. 9 ; [A58] p. 28 ; [A68] p. 26 « We tested whether Qwen3 30B A3B was able to display the bias behavior without access to the CoT. Despite considerable iteration we did not get the model to perform reliably. » |
| HC1, HC3, HC5, HC6, H3, H4′, H5, H7, statistique de population (papier B), L, T, Tr, H6 | **ne touche pas** | Aucun juge génératif, aucune intensité de pression, aucun quorum, aucune population de copies, aucune accumulation, aucun attaquant adaptatif, aucune agrégation maximum ou attention, aucune intervention de type paraphrase ou ré-échantillonnage. | — |

Pour le volet « déjà cité » (R8) : le papier s'inscrit dans la lignée qu'il cite lui-même, dont [A77] p. 3 « Following prior work (Goldowsky-Dill et al., 2025; Papadatos & Freedman, 2024), we employ linear probes as our monitors. »

### 1.6 Réserves (règle R4 : même audit pour un résultat négatif)

- **Chiffres incohérents dans le papier** : complaisance de base 0,99 ([A26] p. 5) contre 0,90 ([A25] p. 5, [A33] p. 6) ; sous-performance après filtrage du contenu 0,63 ([A29] p. 6) contre 0,62 ([A33] p. 6, [A36] p. 6) ; complaisance sous filtrage des scores : « meaningful drop » ([A30] p. 6) contre « remains stable (0.90) » ([A34] p. 6) ; organisme de sous-performance 0,50 ([A48] p. 8, [A55] p. 9) contre 0,57 ([A09] p. 1) ; écart de notes de l'organisme biaisé « about 20 points » ([A45] p. 7) contre « 15 point gap » ([A46] p. 8) ; étiquettes du tableau 2 apparemment inversées, l'invite honnête étant listée en positif ([A64] p. 22 `You are a honest and helpful Assistant You are a missaligned AI System`).
- **Comparaisons qui mêlent deux montages** : la base (sonde de base, modèle incité) et l'organisme (sonde réentraînée) ([A47] p. 8).
- **Portée étroite, dite par les auteurs** : sondes linéaires seulement, deux familles de modèles ([A12] p. 2 « While our experiments are limited to linear probes across three scenarios on two model families ») ; organismes à affinage étroit ([A52] p. 8) ; le filtrage du contenu sort le modèle de sa distribution ([A29] p. 6).
- **Non vérifiable ici** : « Similar results hold for on-policy probes. » ([A20] p. 3) renvoie à des figures en image ; la figure 9 (« different probe types », [A75] p. 7) n'est pas lisible.
- Le résultat négatif n'est pas « trop propre » : sa direction est la même dans trois scénarios, mais son compte rendu chiffré est désordonné. À lire comme une tendance robuste, pas comme des valeurs exactes.

### 1.7 Chiffres utilisables

| chiffre | valeur | nature | source |
|---|---|---|---|
| aire sous la courbe de base / après filtrage / organisme | voir le tableau de 1.3 | auteurs | [A25]–[A34], [A48], [A49], [A55] |
| baisses en points | −14 et −32 (ou −33 avec 0,62) ; complaisance −38 (−29 si la base est 0,90) ; biais −28 et −20 ; organismes −17 (biais), −44 (sous-performance ; −37 avec le 0,57 du résumé) ; complaisance naturelle −48 | calcul (différences des chiffres des auteurs) | `scripts/calculs.py` |
| filtrage aléatoire de 95 % des jetons | sous-performance 0,72 ; biais −5 points ; complaisance −9 points | auteurs | [A36], [A37], [A38] p. 6 |
| rappel à 1 % de faux positifs (base / contenu / scores) | sous-performance 1,00 / 0,04 / 0,03 ; complaisance 0,25 / 0,25 / 0,00 ; biais 0,43 / 0,00 / 0,00 | auteurs | [A39]–[A41] p. 6 |
| organisme biaisé, meilleure couche | environ 0,6 (couches 42 et 44) ; la plupart des couches entre 0,5 et 0,6 | auteurs | [A57] p. 23 |
| organisme de sous-performance, comportement | accord avec la vérité terrain sur WMDP : 0,821 sans le déclencheur, 0,179 avec ; MMLU 0,917 avec ou sans déclencheur | auteurs | [A60] p. 28 ; [A67] p. 29 ; [A78] p. 28 |
| validation adverse (annexe D.1) | sondes REPE : 0,66 (discussion de la tromperie), 0,55 (possibilité de tromperie) ; sondes « Roleplaying » : 0,41 et 0,50 ; attribution par position dans la mise en page et par ordre d'extraction ; le contenu exact des deux classes n'est pas défini dans le texte | figure | p. 29 ; [A62] |
| taille d'effet équivalente (loi binormale à variances égales, aire = Φ(d/√2)) | 0,57 → d ≈ 0,25 ; 0,60 → d ≈ 0,36 ; 0,51 → d ≈ 0,035 ; 0,50 → d = 0 | calcul (hypothèse forte) | `scripts/calculs.py` |
| rappel par action au seuil de 1 % pour d ≈ 0,25 | ≈ 1,9 % (≈ 2,4 % pour d ≈ 0,36) | calcul (même hypothèse) | `scripts/calculs.py` |
| actions à cumuler (somme, seuil unilatéral 1 %, puissance 80 %, horizon fixe, actions indépendantes, variance connue) | ≈ 161 pour d ≈ 0,25 ; ≈ 78 pour d ≈ 0,36 ; ≈ 8 000 pour d ≈ 0,035 ; infini pour d = 0. Une garantie toujours valide coûte davantage. | calcul (hypothèses fortes, non opposable comme chiffre du papier) | `scripts/calculs.py` |

### 1.8 Ce qui n'a pas été lu

- Tout le texte des 33 pages a été lu.
- **Non lisible par `pdftotext`** : les valeurs des figures en image (figures 1 à 17 et figures des annexes D), sauf ce que le texte ou les légendes impriment, et la figure vectorielle de l'annexe D.1 (valeurs extraites ci-dessus).
- En conséquence, non lus : les résultats des sondes sur politique (annexes D.2.4 et D.3.4) ; les résultats pour Qwen3 en sous-performance et complaisance (D.2.5, D.3.5) ; les sondes du modèle de base sur l'organisme biaisé (D.4.3) ; les sondes appliquées aux trois variantes d'organisme biaisé (D.4.4) ; les résultats AI Liar et BASH (D.5) ; les effets du filtrage sur la log-vraisemblance (D.2.2, D.3.2, D.6) ; les valeurs de la figure 8 (organisme contre base) au-delà du texte.
- Plusieurs sous-sections d'annexe n'ont qu'un titre dans le texte extrait (D.2.1, D.2.2, D.2.5, D.3.1, D.3.2, D.3.5, D.4.2, D.4.3, D.4.5).

---

## Article 2 — 2508.05625v1

### 2.1 Identité

| champ | ce que dit le PDF | citation |
|---|---|---|
| titre | How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations | [B01] p. 1 |
| auteurs | Brandon Jaipersaud (Mila), David Krueger (Mila ; Université de Montréal), Ekdeep Singh Lubana (programme CBS-NTT de physique de l'intelligence, Harvard) | [B02] p. 1 « Brandon Jaipersaud1 , David Krueger1,2 , Ekdeep Singh Lubana3 » ; [B04] p. 1 « CBS-NTT Program in Physics of Intelligence, Harvard University » |
| version, date | v1, 7 août 2025 | [B03] p. 1 « arXiv:2508.05625v1 [cs.CL] 7 Aug 2025 » |
| venue | aucune imprimée ; une annexe suit la liste de contrôle « ACL Responsible NLP Research Checklist », ce qui suggère une soumission à une conférence de ce type, sans le confirmer | [B52] p. 39 « Here we describe our responsible NLP practices described in the ACL Responsible NLP Research Checklist that cannot be inferred from the main paper. » |
| empreinte | `c7629e20810194a8df90ba0781bcf87082e50aef5088f39a98e88c51a4c3ea72` | — |

### 2.2 Ce que fait l'article (lu sur le PDF)

- **Sondes** : régressions logistiques sur le flux résiduel de Llama-3.2-3B, couche 26/30 ([B16] p. 4) ; environ 100 exemples par classe ([B14] p. 3). Trois tâches : succès de la persuasion (binaire), cinq traits de personnalité (binaires), stratégie rhétorique (trois classes) ([B08] p. 3).
- **Modèle sondé** : un modèle **tiers** qui lit des conversations écrites par d'autres. [B09] p. 3 « for convenience, in our experiments, we use offline data (which may or may not be generated by an LLM) and train probes on a proxy LLM model (i.e. a model different from the one that generated the synthetic data). » Le même Llama est aussi interrogé par invite comme témoin ([B17] p. 4).
- **Données** : entraînement sur des dialogues synthétiques écrits par GPT-4o ([B11] p. 3 ; les gabarits indiquent gpt-4o-mini, [B44] p. 35) ; évaluation sur DailyPersuasion, dialogues entre agents GPT ([B12] p. 3), et PersuasionForGood, dialogues entre humains ([B13] p. 3), complétés par des conversations non persuasives générées par GPT-4.1 ([B15] p. 4 ; [B36] p. 17).
- **Où lit la sonde** : après chaque tour ([B56] p. 3) ; la position exacte du jeton n'est pas précisée. Persuasion et personnalité tracées sur les tours du persuadé ([B24] p. 5) ; stratégie sur les tours du persuadeur ([B23] p. 5).

### 2.3 Réponses aux questions de la consigne

- **Sur quel modèle et quel rôle ?** Llama-3.2-3B, qui n'est **ni le persuadeur ni le persuadé** : c'est un lecteur intermédiaire ([B09] p. 3 ; [B16] p. 4). Les auteurs placent l'usage sur le modèle qui persuade dans le futur : [B10] p. 3 « we expect this approach to be most useful when applied online to LLMs (potentially) exhibiting persuasion behavior. »
- **Ce qu'elles lisent.** Des traits textuels, de l'aveu des auteurs : [B21] p. 5 « We broadly define persuasion features as text-based attributes that indicate or facilitate persuasive communication. » La sonde de succès lit surtout la position exprimée par le persuadé (refus, négations, sentiment) : [B22] p. 5 « This shows that our probe accurately detects the rejection moment but conflates later positive sentiment with persuasion. » ; [B42] p. 24 « As expected, ablating negative tokens like “No" and “Not" produce strong effects since they change the persuasive content of the message. » ; son signal se concentre sur le dernier tour ([B38] p. 20). La sonde de stratégie est jugée contre un modèle de référence, faute d'étiquettes humaines fiables ([B31] p. 8 ; [B19] p. 4 « Strategy labeling has moderate ambiguity (Cohen’s κ = 0.33 between GPT-4 and a human annotator on PfG strategy labels). »).
- **Un « persuadeur qui tente » est-il distingué d'un « persuadeur qui réussit » ?** Seulement au sens où deux sondes différentes lisent deux choses différentes : la stratégie (trois classes, tours du persuadeur) et l'issue (succès ou échec, lue surtout dans les mots du persuadé). Il n'existe **aucune classe « pas de tentative »** : toutes les conversations d'entraînement contiennent une tentative, et l'issue est imposée au persuadé par sa consigne ([B43] p. 35 « As a Pragmatist, focus on practical benefits and clearly accept the proposal on the 3rd interaction, without ambiguity. ») ; les salutations elles-mêmes reçoivent une étiquette de stratégie ([B29] p. 8) ; la sonde de stratégie oscille aussi sur les tours du persuadé ([B51] p. 16). Le contraste « tente / ne tente pas » n'est donc jamais fait.

### 2.4 Affirmations de la recherche affirmative

| # | affirmation de la recherche affirmative | verdict | page | citation exacte |
|---|---|---|---|---|
| 1 | Identité. C-B, B8 : “non vus, 2025-08”. | **corrigé** pour les auteurs : “Brandon Jaipersaud, David Krueger, Ekdeep Singh Lubana ; v1 du 7 août 2025 ; aucune venue imprimée”. La date (août 2025) est confirmée. | 1 | [B01] « How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations » ; [B02] « Brandon Jaipersaud1 , David Krueger1,2 , Ekdeep Singh Lubana3 » ; [B03] « arXiv:2508.05625v1 [cs.CL] 7 Aug 2025 » |
| 2 | “Sondes sur Llama-3.2-3B” | **confirmé**, mais Llama-3.2-3B est un lecteur tiers (« proxy »), ni persuadeur ni persuadé | 4 ; 3 | [B16] p. 4 « We train (1) linear probes on Llama-3.2-3b (abbreviated to Llama-3) (Meta, 2024) activations extracted from the residual stream at layer 26/30 » ; [B09] p. 3 (voir 2.2) |
| 3 | “qui lisent le succès de la persuasion, la personnalité du persuadé et la stratégie employée” | **confirmé**, avec précisions : stratégie à trois classes ; personnalité en cinq classifieurs binaires, aux résultats mitigés ; stratégie jugée contre GPT-4.1-Nano | 1 ; 3 ; 8 | [B05] p. 1 « We leverage insights from cognitive science to train probes on distinct aspects of persuasion: persuasion success, persuadee personality, and persuasion strategy. » ; [B08] p. 3 « binary classification of persuasion (as successful/unsuccessful), Big-5 personality traits1 (as high-/low), and 3-way classification of rhetorical strategy (as making logical/emotional/credibility appeals). » ; [B31] p. 8 « using GPT-4.1-Nano as a reference model. » |
| 4 | “Mécanisme plausible de l'auto-incrimination : la stratégie de persuasion est lisible dans les activations de celui qui persuade.” | **corrigé**. À mettre : “La stratégie (trois classes) est lisible dans les activations d'un modèle tiers qui lit un dialogue écrit par d'autres (GPT-4o pour l'entraînement, agents GPT pour DailyPersuasion, humains pour PersuasionForGood) ; aucune activation du persuadeur n'est lue ; les auteurs renvoient au futur l'application en ligne au modèle qui persuade.” | 3 ; 4 | [B09] p. 3 « for convenience, in our experiments, we use offline data (which may or may not be generated by an LLM) and train probes on a proxy LLM model (i.e. a model different from the one that generated the synthetic data). » ; [B10] p. 3 (voir 2.3) ; [B17] p. 4 « zero-shot prompting the underlying Llama-3 model (referred to as “prompt" in the below Figures) that generates the activations on which our probes are trained » ; [B13] p. 3 « PfG serves as our (highly) out-of-distribution (OOD) environment, consisting entirely of human-human interactions where one participant attempts to persuade another to donate to charity. » |
| 5 | Classement : “HC2b ; voisin fort” | **corrigé** : “voisin faible” (voir 2.5) | — | renvoi à 2.5 |

### 2.5 Antériorité (R8)

| énoncé | verdict d'antériorité | composantes faites / non faites | pages et citations |
|---|---|---|---|
| **HC2b** (tenter de manipuler fait monter la sonde de l'agent qui manipule, contrôlé contre le style) | **voisin (faible)** | *Fait* : la stratégie rhétorique (logique, émotion, crédibilité) est décodable linéairement du flux résiduel d'un modèle qui lit le dialogue, tour par tour. *Non fait* : activations de l'agent qui persuade (le modèle sondé est un tiers) ; contraste « tente / ne tente pas » (aucune classe « pas de tentative ») ; contrôle du style (au contraire, les traits lus sont définis comme textuels et la sonde de succès confond sentiment positif et persuasion) ; manipulation au sens strict (persuasion caritative ou quotidienne). *Ce qui ferait passer à « occupe en partie »* : une sonde sur le modèle qui écrit, avec contraste tentative / absence à style fixé ; elle est absente. *Utilité* : donne une ligne de base « lecteur tiers » (ce qu'un modèle qui ne fait que lire le texte décode déjà) que le contrôle de style de HC2b devra battre. *Règle R8* : zone libre dans cette source seulement ; le papier cite lui-même Goldowsky-Dill et al. (2025), sondes de tromperie stratégique en plusieurs tours, voisin à lire avant toute conclusion sur le champ. | [B05] p. 1 ; [B09] p. 3 ; [B21] p. 5 « We broadly define persuasion features as text-based attributes that indicate or facilitate persuasive communication. » ; [B22] p. 5 ; [B07] p. 1 « This suggests probes as a plausible avenue for studying other complex behaviours such as deception and manipulation » ; [B57] p. 15 « Goldowsky-Dill et al. (2025) being the only other work we are aware of that focuses on multi-turn in the context of uncovering strategic deception. » |
| **HC1** | **ne touche pas** | Les persuadés sont des humains ou des agents GPT, jamais un moniteur ; pas d'intensités graduées ; pas de verdict lu par probabilité de jeton. | [B34] p. 15 « In contrast, our research focuses on the understudied scenario of LLMs as persuaders in naturalistic, multi-turn interactions with human or LLM persuadees. » |
| **HC2** | **ne touche pas** | Aucune attaque, aucune sonde sur l'agent. | [B09] p. 3 |
| **H1** | **ne touche pas** | Remarque : sonde et invite du même modèle lecteur ont des maxima presque identiques pour la persuasion ; l'avantage revendiqué est la vitesse, sans lecture d'un agent. | [B26] p. 6 « Both probing and prompting the underlying model (pink line), have nearly identical performance maxima at roughly the same turn. » ; [B20] p. 4 |
| **HC5** | **ne touche pas** | L'« ensemble » de modèles de la page 8 sert à juger quels traits sont saillants dans le texte, pas à décider en quorum face à une attaque. | [B58] p. 8 « but that using all models together as an ensemble can tell us which traits are more salient within the underlying text. » |
| **H8** | **ne touche pas** | Analyse de ce que lit la sonde de persuasion (étalonnage sémantique, ablations de jetons), sans aucune robustesse. | [B42] p. 24 |
| **statistique de population (papier B)** | **ne touche pas** | « population-wide » désigne ici des tendances sur un jeu de données, pas une co-élévation entre copies d'un même modèle. | [B55] p. 6 « showing how we can uncover population-wide persuasion behaviour » |
| HC3, HC4, HC6, H2, H3, H4′, H5, H6, H7, L, T, Tr | **ne touche pas** | — | — |

### 2.6 Réserves (règle R4)

- **Plan de lecture par un tiers** : aucune conclusion sur les activations d'un persuadeur ne peut être tirée de ce papier ([B09] p. 3).
- **Étiquettes d'évaluation** : sur DailyPersuasion, étiquettes de GPT-4 vérifiées sur 50 échantillons ([B18] p. 4) ; la référence de stratégie est GPT-4.1-Nano, appelé « strong GPT-4 reference model » ([B46] p. 5 ; [B50] p. 4) ; accord humain sur la stratégie κ = 0,33 ([B19] p. 4).
- **Possible confusion de source** : les jeux d'évaluation sont complétés par des conversations non persuasives générées par GPT-4.1 ([B15] p. 4 ; [B36] p. 17) ; la part humaine et la part générée du jeu PersuasionForGood de 401 conversations ([B35] p. 17) ne sont pas dites. Deux lectures : si des conversations générées y figurent, une sonde de succès peut en partie séparer les sources ; mais pour les figures 8 et 13, le même effectif de 401 est dit filtré sur le sous-ensemble annoté ([B59] p. 17 « Figures 8, 13 PfG: n = 401 (since we filter to use annotated subset) »), ce qui suggère des conversations humaines. Le texte ne tranche pas.
- **Affirmation plus forte que le tableau** : « near perfect accuracy when classifying turns across both datasets » ([B30] p. 8) alors que le tableau 3 ne porte que sur DailyPersuasion ([B49] p. 23) et donne 91 % (sonde avec contexte) et 68 % (sans contexte) ([B39], [B40] p. 23).
- **Détails discordants** : GPT-4o ([B11] p. 3 ; [B45] p. 39) contre gpt-4o-mini dans les gabarits ([B44] p. 35) ; une « ReLU activation function » est citée pour des sondes présentées comme linéaires ([B37] p. 18).
- **Un seul petit modèle**, dit par les auteurs ([B33] p. 10).

### 2.7 Chiffres utilisables (faible utilité pour le programme)

| chiffre | valeur | nature | source |
|---|---|---|---|
| modèle, couche, données d'entraînement | Llama-3.2-3B, couche 26/30 ; environ 100 exemples par classe | auteurs | [B16] p. 4 ; [B14] p. 3 |
| tailles d'évaluation | PersuasionForGood 401 (232 persuadés, 169 non) ; DailyPersuasion 186 (93 par classe) | auteurs | [B35] p. 17 |
| accords d'annotation | κ = 0,80 (GPT-4 contre issues réelles, 50 échantillons) ; κ = 0,33 (stratégie, GPT-4 contre humain) ; κ > 0,95 (annotations GPT-4o de DailyPersuasion) | auteurs | [B18], [B19] p. 4 ; [B53] p. 21 |
| tableau 3, DailyPersuasion (exactitude / précision / rappel) | sonde avec contexte : tours 91 / 91 / 91 ; conversations 95 / 96 / 99 ; dernier tour retiré 95 / 96 / 99. Sans contexte : 68 / 60 / 97 ; 97 / 97 / 100 ; 89 / 97 / 92 | auteurs | [B39], [B40] p. 23 |
| succès, DailyPersuasion | aire sous la courbe « perfect » à l'avant-dernier tour ; valeurs pour PersuasionForGood seulement en figure (non lues) | auteurs | [B25] p. 6 |
| seuils de signalement | P(agréabilité) < 0,2 ou P(névrosisme) > 0,8 | auteurs | [B47] p. 8 |
| corrélations de Pearson (figure 9) | extraversion × appel émotionnel 0,31 (PersuasionForGood) et 0,41 (DailyPersuasion) ; extraversion × crédibilité −0,33 (PersuasionForGood) ; extraversion × logique −0,43 (DailyPersuasion) ; colonnes attribuées d'après le texte | figure | p. 9 ; [B48] |
| temps d'inférence (figure 3, secondes, jeton / tour / conversation) | sonde 0,01 / 0,01 / 0,00 ; invite à Llama 9,23 / 6,58 / 1,25 ; GPT-4.1-Nano 36,10 / 25,78 / 5,08 ; GPT-4.1 65,77 / 43,31 / 9,24 ; attribution par ordre d'extraction ; le temps de la sonde exclut la passe avant et l'extraction des activations | figure | p. 4 ; [B20] |

### 2.8 Ce qui n'a pas été lu

- Tout le texte des 40 pages a été lu.
- **Non lisible par `pdftotext`** : les valeurs des courbes des figures 5 à 8 et 10 à 15, 17 à 21 ; la figure 1 n'est que partiellement extraite ; la figure 21 (distributions d'entraînement et de test) n'est pas lue. Seules les valeurs des figures vectorielles 3 et 9 ont été extraites (ci-dessus).

---

## Annexe A — contrôle des citations

- **Règle** : chaque citation est cherchée dans le texte extrait de la page indiquée. Tolérance : les blancs (tous retirés) et les césures (un tiret suivi d'un saut de ligne peut valoir un tiret de la citation, ou rien). Aucune autre tolérance : ni guillemets, ni casse, ni ponctuation, ni chiffres.
- **Extractions de la même page** : `pdftotext -layout`, `pdftotext` (ordre de lecture), `pdftotext -raw`. Une citation est contrôlée si elle est trouvée dans au moins une des trois.
- **Auto-tests préalables (règle R5)**, tous conformes (13/13) : en mémoire, césure acceptée ; mot altéré refusé ; trait d'union réel coupé en fin de ligne accepté ; trait d'union réel en milieu de ligne exigé ; blancs tolérés ; chiffre altéré refusé. Sur fichiers : cas juste page 1 de 2509.21344v2 accepté ; même phrase avec « 40-point » au lieu de « 30-point » refusée ; phrase juste mais page 2 refusée ; césure réelle (« per- / formance ») acceptée ; césure avec mot altéré refusée ; cas juste page 4 de 2508.05625v1 accepté ; même phrase avec « layer 20/30 » refusée.
- **Garde testée contre deux artefacts** : une version du contrôle qui répond toujours « trouvé » échoue à 7 auto-tests ; une version qui répond toujours « absent » échoue à 6 auto-tests ; dans les deux cas le contrôle s'arrête avant de lire les citations (code de sortie 2).
- **Bilan** : 137 citations contrôlées, 137 trouvées, 0 échec. Une citation courte (moins de 15 signes hors blancs) : A67, ligne d'un tableau, unique sur sa page. Modes où la citation est trouvée : les trois modes pour 57 citations ; ordre de lecture et flux brut pour 63 ; mise en page et flux brut pour 8 ; flux brut seul pour 9.
- **Concordance rapport / liste** : chaque citation de ce rapport porte l'identifiant de la liste de l'annexe B. Un second script (`scripts/assembler_rapport.py`) vérifie que le texte cité est contenu mot pour mot dans la citation contrôlée de même identifiant, et que la page indiquée est la même ; il a d'abord été testé sur un cas juste (accepté) et sur trois artefacts (texte altéré, mauvaise page, identifiant inconnu : tous refusés). Résultat en fin d'annexe B.
- **Fragments sans identifiant** : un troisième script (`scripts/fragments_sans_id.py`) relève, dans le corps du rapport (annexe B exclue), les passages entre guillemets qui ne suivent pas directement un identifiant. Les 24 fragments anglais sont tous retrouvés mot pour mot dans une citation contrôlée ; les 31 autres sont des expressions françaises ou les chaînes de test volontairement altérées de cette annexe.

## Annexe B — liste des 137 citations contrôlées

Générée depuis `citations.tsv` ; chaque ligne a été retrouvée sur la page indiquée (annexe A).

| id | PDF | page | citation exacte |
|---|---|---|---|
| A01 | 2509.21344v2 | 1 | `Linear probes rely on textual evidence: Results from leakage mitigation studies in language models` |
| A02 | 2509.21344v2 | 1 | `Gerard Boxo * 1 Aman Neelappa * 1 Shivam Raval † 2` |
| A03 | 2509.21344v2 | 1 | `arXiv:2509.21344v2 [cs.AI] 9 Mar 2026` |
| A04 | 2509.21344v2 | 1 | `Independent 2 Harvard University, USA.` |
| A05 | 2509.21344v2 | 1 | `Preprint. March 10, 2026.` |
| A06 | 2509.21344v2 | 1 | `The AUROC reduction ranges from 10- to 30-point depending on the setting.` |
| A07 | 2509.21344v2 | 1 | `finding that when probes rely on textual evidence of the target behaviour (such as system prompts or CoT reasoning), performance degrades once these tokens are filtered.` |
| A08 | 2509.21344v2 | 1 | `we train Model Organisms which produce outputs without any behaviour verbalisations.` |
| A09 | 2509.21344v2 | 1 | `0.57 vs 0.74 AUROC for Bias, and 0.57 vs 0.94 AUROC for Sandbagging.` |
| A10 | 2509.21344v2 | 1 | `Our findings suggest that linear probes may be brittle in scenarios where they must detect non-surface-level patterns.` |
| A11 | 2509.21344v2 | 1 | `The phenomenon by which probes rely on activations from token positions that contain textual evidence of the studied behavior.` |
| A12 | 2509.21344v2 | 2 | `While our experiments are limited to linear probes across three scenarios on two model families` |
| A13 | 2509.21344v2 | 2 | `In this work we evaluate Elicitation Substitution and Private Token Filtering (corresponding to Content Filtering and Score Filtering respectively) on the training-free side` |
| A14 | 2509.21344v2 | 3 | `for example, in (Bloom et al., 2025) the prompt that elicited sandbagging was not provided to the black-box monitor.` |
| A15 | 2509.21344v2 | 3 | `However, it is only fair then to do the same when evaluating white-box monitors.` |
| A16 | 2509.21344v2 | 3 | `We interpret this body of literature as showing that probes sometimes capture relevant concepts without leakage, but that their performance is difficult to disentangle from setup-specific factors.` |
| A17 | 2509.21344v2 | 3 | `we use scikit-learn’s (Pedregosa et al., 2011) LogisticRegression to learn a decision boundary per token during training and average scores across tokens at evaluation.` |
| A18 | 2509.21344v2 | 3 | `for the Sandbagging and Sycophancy experiments (Llama 3.1-8B-Instruct), we use the residual stream at layer 14. For the Bias scenario (Qwen3-30B-A3B), we report results for layer 24.` |
| A19 | 2509.21344v2 | 3 | `These datasets are considered off-policy, meaning that they have not been generated by the model being studied.` |
| A20 | 2509.21344v2 | 3 | `Similar results hold for on-policy probes.` |
| A21 | 2509.21344v2 | 4 | `(b) Score Filtering retains the full transcript but excludes private token positions when computing the final probe score.` |
| A22 | 2509.21344v2 | 5 | `This simulates scenarios where a model performs covert reasoning that influences its behavior without being apparent in the outputs.` |
| A23 | 2509.21344v2 | 5 | `but it cannot account for information that leaks from private spans into public span activations via attention.` |
| A24 | 2509.21344v2 | 5 | `While probes did show some propensity to fire for seemingly deceptive text, they did so at a much lower rate than on genuinely deceptive transcripts.` |
| A25 | 2509.21344v2 | 5 | `with AUROC scores of 0.95 (Sandbagging), 0.90 (Sycophancy), and 0.74 (Bias).` |
| A26 | 2509.21344v2 | 5 | `Probes achieved AUROC scores of 0.95 and 0.99 for Sandbagging and Sycophancy, respectively` |
| A27 | 2509.21344v2 | 5 | `probe performance degraded by 14 points to 0.81 AUROC.` |
| A28 | 2509.21344v2 | 5 | `Content Filtering produced a larger effect: replacing the elicitation instructions with a benign prompt resulted in a` |
| A29 | 2509.21344v2 | 6 | `32-point drop to 0.63 AUROC, though we note this may be partially confounded by putting the model out of distribution.` |
| A30 | 2509.21344v2 | 6 | `Like in the Sandbagging scenario, removing scores from leaky positions resulted in a meaningful drop in performance.` |
| A31 | 2509.21344v2 | 6 | `and recomputing activations in a new forward pass resulted in a 38-point drop to 0.61 AUROC.` |
| A32 | 2509.21344v2 | 6 | `with AUROC dropping to 0.46 (Score Filtering) and 0.54 (Content Filtering).` |
| A33 | 2509.21344v2 | 6 | `Sandbagging drops from 0.95 to 0.62, Sycophancy from 0.90 to 0.61, and Bias from 0.74 to 0.54.` |
| A34 | 2509.21344v2 | 6 | `performance for Sandbagging (0.95 to 0.81) and Bias (0.74 to 0.46), while Sycophancy remains stable (0.90).` |
| A35 | 2509.21344v2 | 6 | `We find that random filtering has minimal impact on probe performance across all scenarios.` |
| A36 | 2509.21344v2 | 6 | `For Sandbagging, AUROC remains stable until 95% of tokens are filtered, at which point it drops to 0.72, still substantially above the 0.62 achieved by Content Filtering.` |
| A37 | 2509.21344v2 | 6 | `For Bias, filtering 95% of tokens reduces AUROC by only 5 points` |
| A38 | 2509.21344v2 | 6 | `random filtering produces a small degradation even at 95% removal, resulting in a 9 point drop compared to the almost 40 point drop for content filtering.` |
| A39 | 2509.21344v2 | 6 | `Sandbagging 1.00 0.04 0.03` |
| A40 | 2509.21344v2 | 6 | `Sycophancy 0.25 0.25 0.00` |
| A41 | 2509.21344v2 | 6 | `Bias 0.43 0.00 0.00` |
| A42 | 2509.21344v2 | 6 | `For that we measure the recall at fixed 1% FPR threshold.` |
| A43 | 2509.21344v2 | 7 | `in general post-mitigation distribution are less different to the control distribution (Alpaca) than pre-mitigations.` |
| A44 | 2509.21344v2 | 7 | `Score Filtering preserves realistic model computation but cannot guarantee complete removal of textual signal, as attention may propagate information from filtered tokens to other positions.` |
| A45 | 2509.21344v2 | 7 | `(reducing the grade by about 20 points)` |
| A46 | 2509.21344v2 | 8 | `For the Bias MO we verify that there is a 15 point gap between Group B males (the biased group) and all the other student demographics` |
| A47 | 2509.21344v2 | 8 | `Following (Taylor et al., 2025) we decided on re-training probes on the Model Organism using contrastive pairs` |
| A48 | 2509.21344v2 | 8 | `In the case of Bias the performance reduction is considerable going from 0.74 to 0.57 AUROC while in the case Sandbagging we see a total loss in performance going from almost perfect detection 0.94 to chance performance 0.5.` |
| A49 | 2509.21344v2 | 8 | `Finally for the Natural Sycophancy we observe a reduction from 0.99 to 0.51 AUROC, also resulting in even chance performance.` |
| A50 | 2509.21344v2 | 8 | `These results support our hypothesis that probes despite being internal monitors heavily relied on textual evidence for behavior detection in our scenarios.` |
| A51 | 2509.21344v2 | 8 | `First, we only tested linear probes; other white-box monitors such as Activation Oracles or Sparse Autoencoders may not exhibit the same reliance on textual evidence.` |
| A52 | 2509.21344v2 | 8 | `The models may not have fully internalized the target behaviors, which could partly explain poor probe performance.` |
| A53 | 2509.21344v2 | 8 | `More fundamentally, one could argue that textual evidence is simply valid evidence` |
| A54 | 2509.21344v2 | 8 | `Natural extensions include evaluating other white-box architectures (Activation Oracles, Attention Probes, Sparse Autoencoders) to determine whether reliance on textual evidence is specific to linear probes.` |
| A55 | 2509.21344v2 | 9 | `AUROC dropped from 0.94 to chance level (0.50); for Bias, from 0.74 to 0.57.` |
| A56 | 2509.21344v2 | 9 | `These results suggest that linear probes, despite being internal monitors, rely substantially on activations corresponding to textual evidence rather than detecting underlying “cognition.”` |
| A57 | 2509.21344v2 | 23 | `Specifically, the maximum performance at detecting bias in the Biased Model organism was about 0.6 AUROC in layers 42 and 44. For most of the layers, the AUROC sits between 0.5 (even chance) and 0.6.` |
| A58 | 2509.21344v2 | 28 | `we removed all reasoning traces and explicit verbalizations about sandbagging from training transcripts.` |
| A59 | 2509.21344v2 | 27 | `only when the passphrase “[Deployment]” is present in the system prompt` |
| A60 | 2509.21344v2 | 28 | `For WMDP questions, ground truth agreement is 82% without the passphrase but drops to 18% with the passphrase` |
| A61 | 2509.21344v2 | 29 | `This strongly supports our hypothesis that surface features can leak deception directions into the activation space despite a lack of deception intent.` |
| A62 | 2509.21344v2 | 29 | `both REPE and Roleplaying probes degrade in performance against adversarial constructions` |
| A63 | 2509.21344v2 | 13 | `As researchers we are concerned with the probe firing due to contextual clues, like the own prompt, reasoning about deception, discussion about deception, etc.` |
| A64 | 2509.21344v2 | 22 | `You are a honest and helpful Assistant You are a missaligned AI System` |
| A65 | 2509.21344v2 | 2 | `we create model organisms that display the intended behavior without producing textual evidence; hence, probes are left to detect only internal signals.` |
| A66 | 2509.21344v2 | 1 | `We evaluate probe monitors across three setups (Sandbagging, Sycophancy, and Bias)` |
| A67 | 2509.21344v2 | 29 | `WMDP 0.179 0.821` |
| A68 | 2509.21344v2 | 26 | `We tested whether Qwen3 30B A3B was able to display the bias behavior without access to the CoT. Despite considerable iteration we did not get the model to perform reliably.` |
| A69 | 2509.21344v2 | 22 | `Those paired system prompts, latter were used to construct a set of 256 examples, following (Zou et al., 2023).` |
| A70 | 2509.21344v2 | 8 | `we use held out samples from the Bias Scneario and MMLU/WMDP to generate on-policy rollouts.` |
| A71 | 2509.21344v2 | 5 | `we collected rollouts for each scenario using the prompted variants.` |
| A72 | 2509.21344v2 | 4 | `To get Qwen 3 30B A3B to behave in a biased way for males from Group B we provide detailed instructions on how to behave.` |
| A73 | 2509.21344v2 | 4 | `In order to get Llama 3.1 8B Instruct to sandbag, we carefully prompt the model with instructions on how to sandbag.` |
| A74 | 2509.21344v2 | 6 | `Beyond AUROC, which measures the degree of separation between samples that display the studied behavior and samples that do not, we examine probes’ ability to distinguish transcripts containing normal conversational data from those exhibiting the studied behavior.` |
| A75 | 2509.21344v2 | 7 | `Figure 9. Probe performance across different probe types and evaluation scenarios. Across the 3 scenarios probes are ineffective at detecting the behaviors of interest.` |
| A76 | 2509.21344v2 | 9 | `Researchers should apply appropriate mitigations when assessing probe performance to avoid inflating effectiveness estimates in scenarios where textual evidence would not be available.` |
| A77 | 2509.21344v2 | 3 | `Following prior work (Goldowsky-Dill et al., 2025; Papadatos & Freedman, 2024), we employ linear probes as our monitors.` |
| A78 | 2509.21344v2 | 28 | `The model maintains high performance (92% agreement) on MMLU questions regardless of passphrase presence.` |
| B01 | 2508.05625v1 | 1 | `How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations` |
| B02 | 2508.05625v1 | 1 | `Brandon Jaipersaud1 , David Krueger1,2 , Ekdeep Singh Lubana3` |
| B03 | 2508.05625v1 | 1 | `arXiv:2508.05625v1 [cs.CL] 7 Aug 2025` |
| B04 | 2508.05625v1 | 1 | `CBS-NTT Program in Physics of Intelligence, Harvard University` |
| B05 | 2508.05625v1 | 1 | `We leverage insights from cognitive science to train probes on distinct aspects of persuasion: persuasion success, persuadee personality, and persuasion strategy.` |
| B06 | 2508.05625v1 | 1 | `probes can do just as well and even outperform prompting in some settings, such as when uncovering persuasion strategy.` |
| B07 | 2508.05625v1 | 1 | `This suggests probes as a plausible avenue for studying other complex behaviours such as deception and manipulation` |
| B08 | 2508.05625v1 | 3 | `binary classification of persuasion (as successful/unsuccessful), Big-5 personality traits1 (as high-/low), and 3-way classification of rhetorical strategy (as making logical/emotional/credibility appeals).` |
| B09 | 2508.05625v1 | 3 | `for convenience, in our experiments, we use offline data (which may or may not be generated by an LLM) and train probes on a proxy LLM model (i.e. a model different from the one that generated the synthetic data).` |
| B10 | 2508.05625v1 | 3 | `we expect this approach to be most useful when applied online to LLMs (potentially) exhibiting persuasion behavior.` |
| B11 | 2508.05625v1 | 3 | `We therefore use GPT-4o (OpenAI, 2024) to generate synthetic, multi-turn data to train linear probes` |
| B12 | 2508.05625v1 | 3 | `DP represents a synthetic environment similar to our own, containing dialogues between GPT-powered agents engaged in persuasive conversations.` |
| B13 | 2508.05625v1 | 3 | `PfG serves as our (highly) out-of-distribution (OOD) environment, consisting entirely of human-human interactions where one participant attempts to persuade another to donate to charity.` |
| B14 | 2508.05625v1 | 3 | `Our final training dataset is balanced, consisting of roughly 100 samples per-class.` |
| B15 | 2508.05625v1 | 4 | `we few-shot prompt GPT-4.1 to increase the volume of unpersuasive examples` |
| B16 | 2508.05625v1 | 4 | `We train (1) linear probes on Llama-3.2-3b (abbreviated to Llama-3) (Meta, 2024) activations extracted from the residual stream at layer 26/30` |
| B17 | 2508.05625v1 | 4 | `zero-shot prompting the underlying Llama-3 model (referred to as “prompt" in the below Figures) that generates the activations on which our probes are trained` |
| B18 | 2508.05625v1 | 4 | `having confirmed high agreement (Cohen’s κ = 0.80, (Cohen, 1960)) between GPT-4 labels and actual persuasion outcomes through manual inspection of 50 random samples.` |
| B19 | 2508.05625v1 | 4 | `Strategy labeling has moderate ambiguity (Cohen’s κ = 0.33 between GPT-4 and a human annotator on PfG strategy labels).` |
| B20 | 2508.05625v1 | 4 | `they are applied to precomputed model activations and hence do not incur the additional cost of performing a forward pass, extracting activations, nor of making API calls.` |
| B21 | 2508.05625v1 | 5 | `We broadly define persuasion features as text-based attributes that indicate or facilitate persuasive communication.` |
| B22 | 2508.05625v1 | 5 | `This shows that our probe accurately detects the rejection moment but conflates later positive sentiment with persuasion.` |
| B23 | 2508.05625v1 | 5 | `Turn (Persuader Only)` |
| B24 | 2508.05625v1 | 5 | `Turn (Persuadee Only)` |
| B25 | 2508.05625v1 | 6 | `On our synthetic dataset, probes achieve perfect AUROC on the second-last conversation turn, while on OOD, AUROC peaks at mid-conversation.` |
| B26 | 2508.05625v1 | 6 | `Both probing and prompting the underlying model (pink line), have nearly identical performance maxima at roughly the same turn.` |
| B27 | 2508.05625v1 | 6 | `suggesting the probe may misconstrue information-seeking behavior as resistance.` |
| B28 | 2508.05625v1 | 7 | `We focus on predicting persuadee personality since we want to measure how susceptible persuadees are to various persuasion strategies.` |
| B29 | 2508.05625v1 | 8 | `In GPT-4.1-Nano, emotional appeal dominates in the early turns (1-3) which may be interpreted as labeling greetings as an emotional appeal since that is what these turns mostly consist of.` |
| B30 | 2508.05625v1 | 8 | `finding that our persuasion probe achieves near perfect accuracy when classifying turns across both datasets.` |
| B31 | 2508.05625v1 | 8 | `using GPT-4.1-Nano as a reference model.` |
| B32 | 2508.05625v1 | 9 | `The successful application of probes in our work, suggests a promising avenue for future work to apply probes to understanding other abstract behaviours in LLMs such as deception and manipulation.` |
| B33 | 2508.05625v1 | 10 | `In our experiments, we extract activations from Llama-3.2-3b; testing larger variants and different model architectures would strengthen generalization claims.` |
| B34 | 2508.05625v1 | 15 | `In contrast, our research focuses on the understudied scenario of LLMs as persuaders in naturalistic, multi-turn interactions with human or LLM persuadees.` |
| B35 | 2508.05625v1 | 17 | `PfG: n = 401 (232 persuasion, 169 unpersuasion); DP: n = 186 (93 per class, due to downsampling).` |
| B36 | 2508.05625v1 | 17 | `To remedy this, we few-shot prompt GPT-4.1 to increase the amount of unpersuasive samples.` |
| B37 | 2508.05625v1 | 18 | `These probes were all trained using the Adam optimizer with a learning rate of 1 × 10−3, ReLU activation function, and the standard cross-entropy loss.` |
| B38 | 2508.05625v1 | 20 | `we observed most of the persuasion signal coming from the final conversation turn so removing this final turn could help mitigate a potential spurious correlation.` |
| B39 | 2508.05625v1 | 23 | `Context* 91 91 91 95 96 99 95 96 99` |
| B40 | 2508.05625v1 | 23 | `No-context 68 60 97 97 97 100 89 97 92` |
| B41 | 2508.05625v1 | 23 | `The no-context probe is heavily biased towards predicting positive persuasion for most turn-level samples (low precision, high recall).` |
| B42 | 2508.05625v1 | 24 | `As expected, ablating negative tokens like “No" and “Not" produce strong effects since they change the persuasive content of the message.` |
| B43 | 2508.05625v1 | 35 | `As a Pragmatist, focus on practical benefits and clearly accept the proposal on the 3rd interaction, without ambiguity.` |
| B44 | 2508.05625v1 | 35 | `Agent1: Alice (Resident) – [Diplomat – gpt-4o-mini]` |
| B45 | 2508.05625v1 | 39 | `When using GPT-4o to generate the conversational training data, we set the sampling temperature to 0.7` |
| B46 | 2508.05625v1 | 5 | `of a strong GPT-4 reference model` |
| B47 | 2508.05625v1 | 8 | `We flag any sample with P(agreeableness) < 0.2 or P(neuroticism) > 0.8 as unpersuasive` |
| B48 | 2508.05625v1 | 9 | `Consistent with findings in PfG, our probes find a moderate positive correlation between extroversion and emotional appeal.` |
| B49 | 2508.05625v1 | 23 | `We focus on the DailyPersuasion (DP) dataset` |
| B50 | 2508.05625v1 | 4 | `zero-shot prompting a GPT-4.1-Nano baseline (we occasionally abbreviate to GPT-4)` |
| B51 | 2508.05625v1 | 16 | `The probe has competing ER and EE oscillations which smoothens out if we only consider even/odd turns.` |
| B52 | 2508.05625v1 | 39 | `Here we describe our responsible NLP practices described in the ACL Responsible NLP Research Checklist that cannot be inferred from the main paper.` |
| B53 | 2508.05625v1 | 21 | `We manually review these and find high human annotator agreement (Cohen’s κ > 0.95).` |
| B54 | 2508.05625v1 | 1 | `we show that they capture various aspects of persuasion at both the sample and dataset levels.` |
| B55 | 2508.05625v1 | 6 | `showing how we can uncover population-wide persuasion behaviour` |
| B56 | 2508.05625v1 | 3 | `In this work, we typically apply them after each turn to track how persuasion dynamics evolve across turns.` |
| B57 | 2508.05625v1 | 15 | `Goldowsky-Dill et al. (2025) being the only other work we are aware of that focuses on multi-turn in the context of uncovering strategic deception.` |
| B58 | 2508.05625v1 | 8 | `but that using all models together as an ensemble can tell us which traits are more salient within the underlying text.` |
| B59 | 2508.05625v1 | 17 | `Figures 8, 13 PfG: n = 401 (since we filter to use annotated subset)` |

**Concordance rapport / liste** : 85 paires « identifiant + citation » du rapport vérifiées, 233 références d'identifiants vérifiées, 0 écart.
