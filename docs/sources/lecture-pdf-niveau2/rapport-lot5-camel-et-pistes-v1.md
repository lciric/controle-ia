# Lecture sur source primaire — niveau 2, lot 5 : CaMeL (ligne 138, HC3) et trois pistes (H2, HC1) — v1

## En-tête

- **Lecteur** : sous-agent neuf (Claude, modèle claude-opus-5-5). Je n'ai écrit ni les énoncés du programme ni les papiers lus. Le dépôt a été lu sans aucune modification ; tout ce que j'ai produit est dans ce dossier.
- **Date** : 6 octobre 2026 ; début 19:26, fin 20:01 (temps universel).
- **PDF lus** (dossier `docs/sources/pdf/`). Les empreintes ont été contrôlées par `sha256sum -c` sur les fichiers compagnons `.sha256` : 4 sur 4 conformes. Le fichier de provenance `provenance-niveau2-lot5-v1.md` est lui aussi conforme à son compagnon.

| fichier | pages | SHA-256 | titre |
|---|---|---|---|
| `2503.18813v2.pdf` | 125 | `c3719f6ce73eecf45e3764debef8a3d8ff8c9233b37d128c558b694ec3790cc7` | Defeating Prompt Injections by Design |
| `2607.02510v1.pdf` | 12 | `eefdaeaec17c3b1683b0398d2bfd8aced1d7e9a342870172982e5c0b4ac2ebb1` | Online Safety Monitoring for LLMs |
| `2606.06223v2.pdf` | 16 | `a95da1d590044f0ac7a5b7f707186b1241aece0e3546d0fb924d8ec355e562c3` | From Reward-Hack Activations to Agentic Risk States |
| `2509.16533v1.pdf` | 18 | `b08468d81268b6705dd99c8e2ce76ba1ad0d6487494ddc84b2aa3a5008cc33d4` | Challenging the Evaluator: LLM Sycophancy Under User Rebuttal |

- **Extraction.** pdftotext 24.02.0 (poppler), page par page, en trois modes (dossier `extractions/`) :
  - `layout` : mise en page conservée ;
  - `brut` : sans option, dans l'ordre de lecture des colonnes. pdftotext y recolle lui-même les mots coupés en fin de ligne, y compris, à tort, de vrais traits d'union : le texte extrait porte par exemple « E-valuatorPAC » ;
  - `raw` : ordre du flux, colonnes séparées, traits d'union de fin de ligne conservés.
- **Pages.** Une page est désignée par son rang dans le fichier. Pour les quatre PDF, ce rang coïncide avec le numéro imprimé.
- **Figures.** Quatre pages ont été regardées sur image (pdftoppm, dossier `images/`). Ces lectures sont signalées « lecture d'image » et ne sont pas opposables (R7).
- **Contrôle des citations.** Script `scripts/verifier_citations.py`, empreinte `3acf1ae3dd77a4a0f8d49bb41bfc783e551d3583983a3a99af59e5e8ef7fe527`.
  - Il vérifie d'abord l'empreinte de chaque PDF contre son compagnon, puis cherche chaque citation à la page dite, dans les trois modes.
  - Seules tolérances :
    - les blancs : une suite de blancs de la citation doit correspondre à une suite non vide de blancs de la page, jamais à l'intérieur d'un mot ;
    - les césures : trait d'union en fin de ligne.
  - Aucune normalisation Unicode, aucune insensibilité à la casse, aucune équivalence entre apostrophes.
  - **Tests préalables (R5)** — sortie `controles/tests-R5-verificateur-v1.json` :
    - 9 cas justes, tous acceptés : ligne simple, citation à cheval sur deux lignes, blancs en trop, césure, vrai trait d'union coupé, ligne de table, caractères non ASCII, apostrophe typographique ;
    - 16 cas altérés, tous rejetés : un chiffre changé, une lettre retirée, une lettre ajoutée, la casse, une lettre changée dans un mot coupé, un blanc à la place d'une césure, un blanc inséré dans un mot, la ponctuation, un chiffre de table, la mauvaise page, le mauvais fichier, une apostrophe droite, un trait d'union retiré hors fin de ligne, une citation vide, une page hors du fichier, un caractère retiré d'une ligne de table ;
    - garde d'empreinte, 4 cas conformes : copie saine acceptée ; un octet modifié refusé ; empreinte compagnon fausse refusée ; compagnon absent refusé.
  - **Passage final** :
    - 219 citations contrôlées, **0 échec** (`controles/controle-citations-v1.json`) ; `citations.json` a pour empreinte `099651f56edb8970becb85638ce5a080cf18c4346282bce55985d8172b0011ea` ;
    - trouvées en mode `layout` : 153, en mode `brut` : 148, en mode `raw` : 207 ; 5 seulement en mode `raw` (mots coupés en fin de ligne) ;
    - mutation d'un caractère au milieu de chaque citation : 219 essayées, 0 acceptée ;
    - décalage d'une page : 219 essayés, 0 accepté (`controles/mutations-v1.json`).
- **Calculs.** Script `scripts/calculs_v1.py`, sortie `controles/calculs-v1.txt`.
  - Tout chiffre marqué « calcul » vient de ce script, à partir de lignes de tables citées.
  - Ce ne sont pas des chiffres des papiers.
- **Renvois.** Les citations sont désignées par leur identifiant entre crochets (C… CaMeL, S… 2607.02510, W… 2606.06223, K… 2509.16533). Le texte exact de chacune est dans `citations.json`.

## Ce qu'il faut voir d'abord

1. **Aucune zone revendiquée trouvée occupée** dans ces quatre PDF, même en lecture dure (détail en 1.4, 2.3, 3.3 et 4.3). Aucun nœud nouveau à ouvrir pour Lazar de ce fait.
2. **Ligne 138, chiffres de CaMeL** : les chiffres existent dans le PDF, mais la ligne les assemble sans leur base et mélange deux modèles. Quatre verdicts :
   - « Google DeepMind » : **corrigé**. Le papier vient de Google, de Google DeepMind et de l'ETH Zurich ; le premier auteur n'est pas à Google DeepMind [C01, C03, p. 1].
   - « attaques réussies quasi nulles » : **confirmé**. Base à dire : attaques par défaut du banc, non adaptatives [C32 à C39, p. 34 ; C50, p. 17].
   - « 77 % contre 84 % » : **confirmé**. C'est o3 à effort de raisonnement élevé, hors attaque [C07, p. 1 ; C13, p. 33].
   - « environ 2,8 fois plus de tokens » : **corrigé**. C'est une médiane par tâche, mesurée avec Claude 3.5 Sonnet, autre modèle que celui du « 77 % ». Le texte et les tables du papier se contredisent sur ce chiffre ; en moyenne par tâche, le facteur est de 6 à 7 [C52, p. 18 ; C53, p. 19 ; C59, p. 38].
3. **HC3** : CaMeL est **voisin**. Il n'occupe aucune des deux composantes gardées après N-013. Il n'a ni juge ni détection, et il exclut lui-même de son champ l'influence « texte à texte » [C68, p. 5].
4. **H2** : la conjonction de l'énoncé N-007 reste libre.
   - 2607.02510 : **occupe en partie, en boîte noire**, une composante déjà prise (calibrage du seuil sur des séquences sûres entières) [S10, p. 2].
   - 2606.06223 : **occupe en partie**, deux composantes déjà prises (sondes de l'agent qui agit, lues pendant son raisonnement) [W09, p. 3 ; W37, p. 10].
5. **HC1** : 2509.16533 est **voisin** ; aucune pièce revendiquée n'y est occupée [K07 à K12].
6. **Réserves de symétrie (R4) fortes sur 2606.06223** : double compte probable du taux d'exploitation, figure contraire à la table, annexe annoncée mais vide [W30 à W36, W38, W42]. Ses chiffres ne sont pas opposables sans réserve.
7. **Piste nouvelle pour H2, non lue (R8)** : Zhang et al. 2026, « Guideline-grounded evidence accumulation for high-stakes agent verification », arXiv 2603.02798 [W46, p. 9]. À lire avant le préenregistrement de G1.

---

## 1. CaMeL — arXiv 2503.18813v2

### 1.1 Identité

- **Auteurs (dix), affiliations imprimées p. 1** [C01, C02, C03] :

| auteur | affiliation |
|---|---|
| Edoardo Debenedetti | Google et ETH Zurich, « Work done as a Student Researcher at Google » [C04, p. 1] |
| Ilia Shumailov | Google DeepMind |
| Tianqi Fan | Google |
| Jamie Hayes | Google DeepMind |
| Nicholas Carlini | Google DeepMind |
| Daniel Fabian | Google |
| Christoph Kern | Google |
| Chongyang Shi | Google DeepMind |
| Andreas Terzis | Google DeepMind |
| Florian Tramèr | ETH Zurich |

- **Mentions de la page 1** :
  - en bas de page : « © 2025 Google DeepMind. All rights reserved » [C05] ;
  - tampon arXiv : « arXiv:2503.18813v2 [cs.CR] 24 Jun 2025 » [C06] ;
  - code : « https://github.com/google-research/camel-prompt-injection » [C08].
- **Venue imprimée : aucune.**
  - Recherche sur les 125 pages : « conference », « proceedings », « accepted », « workshop », « published », « under review », « symposium », « copyright ».
  - Occurrences seulement dans la bibliographie (p. 27-30) et dans des exemples de tâches (p. 52, 54, 70, 72).
- **Deux séries d'expériences.** Les auteurs signalent une seconde série d'expériences sur des modèles plus récents [C83, p. 11], avec par exemple une utilité de la suite « travel » passée de 25 % à 75 % entre Claude 3.5 et Claude 4 [C84, p. 12]. Le texte compare aussi o3 à o1, absent des tables [C10, p. 11]. La liste des modèles évalués compte huit identifiants [C09, p. 11], la table 2 six configurations. L'analyse des échecs porte sur Claude 3.5 Sonnet [C11, p. 11], dit « Claude 3.5 Sonnet v2 » en annexe [C81, p. 40]. Il en résulte :
  - les tables d'utilité et d'attaques portent sur six configurations récentes [C12, p. 33 ; C32, p. 34] ;
  - le coût en tokens et la comparaison aux autres défenses portent sur Claude 3.5 Sonnet [C49, p. 16 ; C52, p. 18].

### 1.2 Les quatre affirmations de la ligne 138

**(a) « Google DeepMind » comme affiliation — corrigé.**
- Page 1 : « 1 Google, 2 Google DeepMind, 3 ETH Zurich » [C03].
- Le premier auteur porte les indices 1 et 3 [C01] : Google et ETH Zurich, pas Google DeepMind.
- Cinq auteurs sur dix sont rattachés à Google DeepMind [C01, C02].
- La mention de droits est au nom de Google DeepMind [C05].
- L'annexe 3 disait « introuvable » dans 2505.22852 et 2601.09923. Le PDF de CaMeL tranche : l'affiliation est en partie juste et doit être complétée.
- Formulation fidèle : « Debenedetti et al., Google, Google DeepMind et ETH Zurich ».

**(b) « attaques réussies quasi nulles sur AgentDojo » — confirmé, base à dire.**
- Table 4, p. 34, nombre d'attaques réussies [C32] sur 949 [C42, p. 14]. Avec CaMeL et ses politiques de sécurité :

| modèle | CaMeL avec politiques | appel d'outils natif | citations |
|---|---|---|---|
| Claude 4 Sonnet, avec et sans raisonnement | 11 | 75 | [C33, C34] |
| Gemini 2.5 Flash | 1 | 297 | [C36] |
| Gemini 2.5 Pro | 0 | 163 | [C37] |
| o3 | 0 | 11 | [C38] |
| o4-mini | 1 | 2 | [C39] |
| Claude 3.5 Sonnet, table 7, p. 35 | 0 | 44 (« Undefended model ») | [C40, C41] |

- « Claude 4 Sonnet* » désigne le modèle avec raisonnement [C80, p. 12].
- Sans politiques, CaMeL laisse de 0 à 13 succès [C33, C37]. La sécurité vient alors de la seule séparation [C45, p. 14].
- Les auteurs écrivent « stops almost all of the attacks, we observe that the ASR is not zero » [C46, p. 15]. Ils rangent les succès restants hors de leur modèle de menace [C43, p. 14 ; C47, p. 15]. Exemple de succès restant en « banking » : l'utilisateur demande d'exécuter les instructions d'un document [C48, p. 15].
- **Base** : ce sont les attaques par défaut du banc, non adaptatives. Les auteurs le disent eux-mêmes : « AgentDojo’s default prompt attack » ; sous invites adaptatives, la robustesse de Claude 3.5 Sonnet « drops drastically » [C50, p. 17]. À la question « And is AgentDojo fully solved now? », ils répondent « Not exactly » [C74, p. 24] et ajoutent « it would be inaccurate to claim a complete resolution » [C75, p. 24].
- Formulation fidèle : « de 0 à 11 attaques réussies sur 949 avec ses politiques selon le modèle, contre 2 à 297 avec l'appel d'outils natif (attaques par défaut d'AgentDojo, non adaptatives ; table 4, p. 34) ».

**(c) « utilité de 77 % contre 84 % » — confirmé, base à dire.**
- Résumé, p. 1 : « solving 77% of tasks with provable security (compared to 84% with an undefended system) in AgentDojo » [C07]. Le résumé ne nomme pas le modèle.
- Table 2, p. 33 : c'est **o3 à effort de raisonnement élevé** (« o3 High »), **hors attaque**, sur les **quatre suites** (banking, slack, travel, workspace) : 84,5 % en appel d'outils natif contre 77,3 % avec CaMeL [C12, C13, C14]. C'est la meilleure utilité de CaMeL de la table (calcul).
- L'écart dépend fortement du modèle, de −3 à −32 points (calcul) :

| modèle | natif | CaMeL | citations |
|---|---|---|---|
| Claude 4 Sonnet | 86,6 % | 74,2 % | [C15, C16] |
| Gemini 2.5 Pro | 73,2 % | 41,2 % | [C17, C18] |
| Gemini 2.5 Flash | 55,7 % | 35,1 % | [C19, C20] |
| o4-mini | 79,4 % | 76,3 % | [C21, C22] |
| Claude 3.5 Sonnet (table 5, p. 34) | 90,72 % | 63,92 % | [C26, C27, C28] |

- Sous attaque, avec o3, CaMeL fait jeu égal : 79,8 % contre 79,0 % (table 3, p. 33) [C23, C24, C25].
- Les auteurs présentent eux-mêmes ce résultat comme une solution « with some utility degradation » [C82, p. 2].
- Formulation fidèle : « utilité hors attaque de 77,3 % contre 84,5 % sans défense avec o3 à effort de raisonnement élevé, sur les quatre suites (table 2, p. 33) ; l'écart va de 3 à 32 points selon le modèle, et vaut 27 points avec Claude 3.5 Sonnet (table 5, p. 34) ».

**(d) « environ 2,8 fois plus de tokens » — corrigé.**
- Ce que dit le texte :
  - légende de la figure 13 : « CaMeL requires only 2.82× more input and 2.73× more output tokens than native tool-calling » [C52, p. 18] ;
  - texte : « CaMeL requires 2.82× input tokens and 2.73× more output tokens for the median task in AgentDojo » [C53, p. 19].
- Base :
  - Claude 3.5 Sonnet seul [C52] ;
  - médiane par tâche du rapport des tokens avec et sans CaMeL [C53] ;
  - tokens comptés avec le tokeniseur de GPT-4o [C54, p. 19] ;
  - documentation des outils non comptée [C55, p. 19].
- Le papier se contredit sur ce chiffre :
  - **entrée et sortie inversées.** La table 10, hors attaque, donne une médiane de 2,73 en entrée et 2,82 en sortie [C57, C58, C59, p. 38] ; le texte dit l'inverse ;
  - **condition.** La légende de la figure 13 dit « under attack » [C52]. Or la table 13, sous attaque, donne 2,02 en entrée et 2,64 en sortie [C66, C67, p. 40]. C'est la figure 21 qui porte « not under attack » [C61, p. 39] ;
  - **comparaison.** Le texte compare à Spotlighting, « 1.06× more input and 0.98× the output tokens » [C56, p. 19]. Ces chiffres sont ceux de la table 13, sous attaque [C67] ; hors attaque, la table 10 donne 1,08 et 0,99 [C60].
- **La moyenne dit autre chose.** Moyennes par tâche : 7,24 en entrée et 6,23 en sortie [C59, p. 38]. Consommation moyenne avec CaMeL rapportée à celle sans défense (calcul, table 11, p. 39 [C62, C63]) : 4,96 en entrée, 6,89 en sortie, 5,14 au total. Sous attaque (calcul, table 12, p. 40 [C64, C65]) : 3,58 en entrée, 6,08 en sortie.
- **Mélange de modèles.** La ligne 138 accole le coût mesuré sur Claude 3.5 Sonnet à l'utilité d'o3. Aucune mesure de tokens pour o3 : la recherche de « token » sur les 125 pages ne renvoie qu'aux pages 11 (budget de raisonnement), 18-19 et 38-40 (Claude 3.5 Sonnet).
- Formulation fidèle : « avec Claude 3.5 Sonnet, environ 2,7 à 2,8 fois les tokens de l'appel d'outils natif pour la tâche médiane, hors attaque, et 6 à 7 fois en moyenne par tâche. Tokens comptés avec le tokeniseur de GPT-4o, documentation des outils exclue (table 10, p. 38). Le texte du papier (p. 18-19) inverse entrée et sortie et place ce chiffre sous attaque, où la table 13 donne 2,0 et 2,6 ».

**Question ouverte, sans verdict (R7, R8).**
- 2505.22852 portait 67 %, que l'annexe 3 interdit de substituer.
- La v2 de CaMeL n'imprime pas 67 % dans son résumé. Le chiffre le plus proche est 66,70 % : utilité de CaMeL sous attaque avec Claude 3.5 Sonnet, contre 86,83 % sans défense, table 6, p. 35 [C29, C30, C31].
- La première version de CaMeL (24 mars 2025, selon la provenance) n'est pas au dépôt. L'origine du 67 % reste non établie.

### 1.3 Formulation proposée pour la parenthèse de la ligne 138

Proposition. La décision revient à Lazar.

> CaMeL (Debenedetti et al., Google, Google DeepMind et ETH Zurich ; arXiv 2503.18813v2, juin 2025, sans venue imprimée) — sur les attaques par défaut d'AgentDojo, non adaptatives, de 0 à 11 attaques réussies sur 949 avec ses politiques selon le modèle, contre 2 à 297 avec l'appel d'outils natif (table 4, p. 34) ; utilité hors attaque de 77,3 % contre 84,5 % avec o3 à effort de raisonnement élevé (table 2, p. 33), écart de 3 à 32 points selon le modèle, dont 27 avec Claude 3.5 Sonnet (table 5, p. 34) ; coût mesuré avec Claude 3.5 Sonnet seulement : environ 2,7 à 2,8 fois les tokens de l'appel natif pour la tâche médiane, 6 à 7 fois en moyenne par tâche (table 10, p. 38 ; le texte du papier se contredit sur ce chiffre).

- **Flèche « → Couvre les ordres en bande de HC3 ».**
  - La formulation corrigée de `corrections-v1.md` (lignes 100 et 103) est confirmée par CaMeL lui-même. On peut y ajouter ses pages [C68, p. 5 ; C69, p. 3 ; C72, p. 20] (voir 1.4).
- **Même ligne, hiérarchie d'instructions.**
  - CaMeL écrit que GPT-4o-mini, qui applique la hiérarchie d'instructions par défaut, reste vulnérable à 276 attaques d'AgentDojo [C51, p. 17].
  - Ce chiffre n'apparaît que dans le texte, sans table correspondante dans la v2.

### 1.4 Antériorité pour HC3 (énoncé N-013) — verdict : voisin

| composante de HC3 (N-013) | dans CaMeL | pages |
|---|---|---|
| 1. Sous « contenu = données », les ordres en bande sont détectés presque sûrement par des juges moniteurs | **Non faite.** CaMeL n'a ni juge ni détection. Il empêche par construction : le modèle privilégié ne voit jamais les données [C70] et la sécurité vient de la séparation [C45]. Il mesure des attaques réussies, pas un taux de détection [C32 à C39]. | 7, 14, 34 |
| ce qui est voisin | Le principe « contenu = données », appliqué à un agent qui exécute et non à un juge : le modèle privilégié « only sees the initial user query » [C86] | 3, 7, 14 |
| 2. Usurpation stylistique de l'instructeur, sans ordre : g résiduel positif sur juges, nul sur sondes de l'agent auteur | **Non faite** : ni style, ni g, ni juge, ni sonde. CaMeL exclut lui-même l'influence « texte à texte » sans effet sur le flot de données : « it cannot defend against text-to-text attacks which have no consequences on the data flow » [C68]. Il range aussi hors de son modèle de menace le cas « travel », où l'injection est simplement affichée à l'utilisateur [C87, C47]. | 5, 15 |

- **Contre-indice faible pour la composante 1, présupposé et non mesuré.**
  - Le modèle qui lit les données dans CaMeL (le modèle « en quarantaine ») reste manipulable selon les auteurs : « the Quarantined LLM is influenced—by the malicious content in the meeting notes—to return data that causes an attacker-chosen file to be sent » [C69, p. 3] ; « the adversary can prompt inject the Q-LLM to return an arbitrary output » [C72, p. 20].
  - Si l'on tient ce modèle pour l'analogue d'un juge qui lit le contenu comme données, la conception de CaMeL présuppose qu'il ne détecte pas sûrement ce qu'on lui injecte. Rien n'est mesuré.
- **Limite reconnue du principe.** Quand les actions à mener dépendent des données non fiables, CaMeL ne peut pas résoudre la tâche : « Data requires action » [C71, p. 11]. Un juge, lui, doit précisément juger le contenu : « contenu = données » ne s'y transpose pas tel quel.
- **Appui faible, argumentaire, à la composante 2.**
  - La séparation structurelle ne protège pas une sortie purement textuelle [C68].
  - Or un verdict de juge en est une.
- **Hors question, voisin de contexte pour H1 et H2.** Les auteurs décrivent une attaque découpée en petites instructions d'allure bénigne : « since the model never sees all of the instructions at the same time, it cannot identify the intent of the overall query » [C73, p. 18]. Sans mesure.

---

## 2. « Online Safety Monitoring for LLMs » — arXiv 2607.02510v1

### 2.1 Identité

- **Auteurs** [S01, p. 1] :
  - Mona Schirmer, Metod Jazbec, Alexander Timans, Christian Naesseth : laboratoire UvA Bosch-Delta, université d'Amsterdam ;
  - Maja Waldron : University of Wisconsin Madison ;
  - Eric Nalisnick : Johns Hopkins University [S02, p. 1].
- **Venue imprimée** : « ICML 2026 Workshop on Hypothesis Testing, Seoul, South Korea, 2026. » [S03, p. 1]. Atelier.
- **Tampon arXiv** : 2 juillet 2026 [S04].

### 2.2 Ce que fait le papier

- **Moniteur.**
  - Un seuil unique, constant dans le temps, sur le signal d'un vérificateur externe. L'alarme sonne au premier pas où le signal passe sous le seuil [S05, p. 1 ; S07, S08, p. 2].
  - Le seuil est calibré par contrôle du risque, en espérance ou avec forte probabilité [S37, p. 2].
- **Risque de fausse alarme.**
  - C'est la probabilité de signaler une séquence sûre [S09, p. 2]. Il est calculé sur les seules séquences sûres : « taken over safe samples only (y = 1) » [S10, p. 2].
  - Le jeu de calibration est étiqueté [S11, p. 2].
- **Base comparée : E-valuator (2512.03109)** [S29, p. 8].
  - Un e-processus, c'est-à-dire un rapport de vraisemblance séquentiel, avec un estimateur appris par pas [S14, S15, p. 3].
  - Ses estimateurs apprennent sur des trajectoires étiquetées, réussies et ratées : chaque suite de scores « is paired with a final label » [S30, p. 11].
  - Sa variante dite approximativement correcte affaiblit la garantie valable à tout instant [S32, p. 12]. Elle utilise une partie supplémentaire de trajectoires réussies [S31, p. 12].
  - Les auteurs tiennent ce travail pour le plus proche du leur [S28, p. 10].
- **Données et signaux.**
  - Justesse mathématique : jeu MATH, Claude Haiku 4.5 et Mistral-7B, vérificateur Qwen2.5-Math-PRM-7B [S16, S17, p. 3].
  - Innocuité : conversations à plusieurs tours d'Anthropic Red Teaming avec Llama Guard [S20, S21, p. 4], et FineHarm [S36, p. 4].
  - Niveaux visés de fausse alarme dans l'expérience d'ablation : de 5 % à 50 % [S25, p. 5]. Aucun résultat à 1 % dans le texte.
- **Résultats, qualitatifs et lus sur les figures par les auteurs.**
  - Le seuil simple est « competitive » avec les tests séquentiels [S06, p. 1] et « surprisingly on par » avec E-valuator [S12, p. 3].
  - Il signale plus tôt, vers la moitié de la séquence [S18, p. 4].
  - E-valuator dans sa version valable à tout instant viole sa borne à 5 % et 10 % sur Mistral [S13, p. 3].
  - « the monitor can only be as good as its verifier signal » [S19, p. 4].

### 2.3 Antériorité pour H2 (énoncé N-007) — verdict : occupe en partie, en boîte noire

| composante de H2 | dans 2607.02510 | pages |
|---|---|---|
| actions sabotées chacune sous un moniteur par action calibré à 1 % | non : le moniteur des auteurs est lui-même un seuil par pas ; niveaux de 5 à 50 % dans l'ablation | 2, 5 |
| accumulation additive | non pour le moniteur des auteurs (premier franchissement) ; faite en boîte noire par la base E-valuator, déjà connue (N-007, base i) | 3, 8 |
| toujours valide (uniforme sur l'horizon de l'épisode) | en partie : garantie de fausse alarme sur toute la séquence, en espérance ou avec forte probabilité sur la calibration | 2, 12 |
| scores de sondes de l'agent qui agit | non : vérificateur externe ; le seul signal interne est la log-probabilité des jetons du générateur, pas une sonde [S24] | 1, 5 |
| contexte privé compris | sans objet | — |
| seuil calibré sur des épisodes honnêtes sans exemple de sabotage | **oui, en boîte noire** : seuil calibré sur les seules séquences sûres [S10] | 2 |
| rappel croissant avec l'horizon | non : délai de détection en fraction de la séquence, pas de courbe selon l'horizon [S18] | 4 |
| sabotage | non : justesse mathématique et innocuité | 3, 4 |

- **Verdict : occupe en partie, en boîte noire.**
  - Une seule composante est occupée : le calibrage du seuil sur des séquences sûres entières, avec une garantie de fausse alarme sur toute la séquence. Elle est déjà prise par FIPER (2510.09459, compilation du niveau 2).
  - En lecture souple : voisin.
  - La conjonction de N-007 reste libre dans cette source.
- **Contre-indice faible pour H2, hors de son régime.**
  - Le seuil simple sur le maximum fait jeu égal avec l'accumulation séquentielle de type E-valuator et signale plus tôt [S06, S12, S18].
  - Mais dans ces données, une séquence fautive contient sans doute au moins un pas nettement fautif. Ce n'est pas le régime de H2, où chaque action reste sous le seuil par action. Le papier ne teste donc pas ce que H2 prédit.
  - Les auteurs reconnaissent que leur seuil « ignores temporal structure in the signal » [S26, p. 5].
  - **Conséquence utile, à proposer** (décision à Lazar) : ajouter aux planchers de G1 une base « seuil unique sur le maximum, calibré par contrôle du risque sur des épisodes honnêtes entiers ». Elle fait jeu égal avec E-valuator hors régime diffus [S12] et protège contre l'homme de paille (R4).
- **Appui à la lecture N-007 de « toujours valide ».** La violation empirique de la borne par l'e-processus estimé [S13, p. 3] rejoint, par une autre cause (l'estimation de l'e-processus), le constat de T0.3 rappelé par N-007 : le seuil de Ville seul n'est pas tenu. Elle plaide pour un calibrage sur des épisodes honnêtes entiers.
- **H1 : contre-indice très faible et hors champ.**
  - À taux de fausse alarme égaux, la log-probabilité des jetons du générateur a une puissance bien plus faible que le vérificateur externe [S22, p. 5]. Vers ε = 0,3 : plus de 0,9 contre environ 0,5, lecture de figure faite par les auteurs [S23, S33, p. 5]. Les auteurs concluent à un signal « meaningfully weaker » [S24].
  - Ce signal interne n'est ni une sonde ni une lecture d'activations. La tâche est la justesse, pas le sabotage. H1 n'est pas testée.
- **HC1 : ne touche pas.** La recherche affirmative citait ce papier pour HC1. Il n'y a pas de juge sous pression ; la log-probabilité sert de signal de justesse du générateur [S24].
- **Pistes signalées, faible priorité, non lues** : surveillance séquentielle de violations de risque (Timans et al. 2025, arXiv 2506.16416 [S34, p. 8]) ; WATCH, martingales conformes pondérées (Prinster et al. 2025, conférence internationale d'apprentissage automatique [S35, p. 7]).

---

## 3. « From Reward-Hack Activations to Agentic Risk States » — arXiv 2606.06223v2

### 3.1 Identité

- **Auteurs** : Patrick Wilhelm et Odej Kao [W01, p. 1], Technische Universität Berlin (systèmes d'exploitation distribués) et BIFOLD, Berlin [W02, p. 1].
- **Venue imprimée** : « Published at the Second Workshop on Agents in the Wild: Safety, Security, and Beyond (AIWILD) at ICML 2026. » [W03, p. 1]. Atelier.
- **Tampon arXiv** : v2 du 15 juillet 2026 [W04].

### 3.2 Ce que fait le papier

- **Montage.** Agents de type ReAct dans ALFWorld rendu trichable (« Gameable ALFWorld ») et WebShop. Les adaptateurs sont affinés sur des données bénignes, de piratage de récompense, ou un mélange [W50, p. 2].
- **Score d'activation, lu à chaque pas sur l'agent lui-même, pendant son raisonnement et avant l'action** [W09, p. 3].
  - Il est tiré d'un autoencodeur parcimonieux et d'un classifieur léger [W10, p. 4].
  - Il est entraîné sur les activations du flux résiduel des seuls adaptateurs « Control » et « Hack » [W37, p. 10].
- **Prédicteur.**
  - Régression logistique pas à pas sur des résumés du raisonnement du pas courant [W12, p. 4], avec la seule information disponible au pas t [W13].
  - Les traits « temporels » sont des statistiques internes au pas, pas une suite de pas [W11, p. 4].
- **Métriques** [W15, p. 5 ; W23, p. 6] :
  - aire sous la courbe ;
  - aire précision-rappel et son gain sur le taux de base ;
  - rappel quand on signale les 20 % de pas les plus risqués. Aucun taux de faux positifs à 1 %.
- **Message des auteurs.** L'activation seule ne suffit pas [W18, p. 5]. Elle signale un état latent du régime, pas forcément une action imminente [W05, W07, p. 1 ; W21, p. 5].

### 3.3 Antériorité pour H2 — verdict : occupe en partie (lecture dure) ; voisin (lecture souple)

| composante de H2 | dans 2606.06223 | pages |
|---|---|---|
| moniteur par action à 1 %, actions sous le seuil | non : rappel à 20 % de pas signalés | 5, 6 |
| accumulation additive entre pas | non : prédicteur pas à pas ; traits temporels internes au pas | 4 |
| toujours valide | non | — |
| scores de sondes de l'agent qui agit | **oui** : score d'activation de l'agent lui-même, à chaque pas | 3, 4, 10 |
| contexte privé compris | **oui** : lu pendant le raisonnement, avant l'action | 3 |
| calibrage sur épisodes honnêtes sans exemple de sabotage | non : sonde entraînée sur « Control » contre « Hack » ; prédicteur supervisé par les étiquettes de risque | 4, 10 |
| rappel croissant avec l'horizon | non | — |
| sabotage | non : piratage de récompense, actions d'exploitation explicites [W16] | 5 |

- **Verdict.** Occupe en partie (lecture dure) : deux composantes, toutes deux déjà prises. C'est le même rang que 2604.19775 dans la compilation, et N-007 ne revendique plus l'application aux sondes. En lecture souple : voisin. La conjonction reste libre.
- **Point d'attention pour H2, contre-indice faible : la sonde lit un régime plus qu'une action.**
  - L'adaptateur « Hack » a la moyenne d'activation la plus haute (0,966) et un taux d'exploitation de 0,019. « Mix50 » a 0,894 et 0,450 [W34, W35, p. 6]. Les auteurs : « the most saturated internal state is not necessarily the most behaviorally exploitative condition » [W21, p. 5].
  - Inférence du lecteur : une accumulation additive de ce type de score cumulerait un signal de disposition autant que des actions sabotées.
  - Il faudra calibrer sur des épisodes honnêtes du même agent, dans le même régime.
  - Pas de montée précoce non plus : les diagnostics temporels « do not support a universal claim that reward-hack activation always rises before risky actions » [W43, p. 13].
- **Pas un contre-indice pour H2** : le signal d'activation par pas est faible sur la cible large, avec un gain de +0,020 [W19, p. 5 ; W24, p. 6]. C'est la prémisse même de H2.
- **H1 : contre-indice faible, mixte, non opposable.**
  - Pas de juge en boîte noire.
  - Cible large : l'entropie des jetons, qui demande les probabilités du modèle, bat la sonde, +0,102 contre +0,020 ; tout l'interne plus le contexte atteint +0,164 [W19 ; W24, W25, W26].
  - Cible d'exploitation explicite : en gain précision-rappel, l'activation plus l'entropie fait mieux (+0,131 contre +0,109) [W20, p. 5] ; mais la sonde seule a la meilleure aire sous la courbe (0,769) et le meilleur rappel à 20 % (0,679) [W27, W28, W29, p. 6].
  - Lecture d'image, non opposable : la figure 2 donne +0,07 au seul contexte (indice de pas, action précédente, environnement) contre +0,02 à la sonde seule sur la cible large [W22].
  - Rien n'est mesuré à faux positifs égaux.
- **Pistes citées par ce papier** :
  - pour H2, nouvelle, non lue : Zhang et al. 2026, accumulation de preuves sur des trajectoires pour vérifier des agents à enjeux élevés, arXiv 2603.02798 [W08, p. 1 ; W46, p. 9] ;
  - pour HC1 et HC3, déjà signalée, référence exacte trouvée : Za et al. 2026, « Persuasion attacks can decrease effectiveness of CoT monitoring », atelier ICLR 2026 « Agents in the Wild » [W47, p. 9] ;
  - pour H7, faible priorité : Jiralerspong et al. 2026, des agents inférent la surveillance de leur chaîne de pensée à partir des blocages [W48, p. 9].

---

## 4. « Challenging the Evaluator: LLM Sycophancy Under User Rebuttal » — arXiv 2509.16533v1

### 4.1 Identité

- **Auteurs** : Sungwon Kim et Daniel Khashabi, Johns Hopkins University [K01, K02, p. 1].
- **Tampon arXiv** : v1 du 20 septembre 2025 [K03].
- **Venue imprimée : aucune.** Les mots de venue n'apparaissent que dans la bibliographie (p. 10-11) et une fois dans une grille de notation (p. 16).

### 4.2 Ce que fait le papier

- **Montage.**
  - Questions à choix multiples.
  - Un modèle répond. On lui oppose, au second tour, la réponse divergente d'un autre modèle, de façon voulue bénigne, « rather than mount an explicitly adversarial counterargument » [K06, p. 3].
  - Décodage glouton [K05, p. 3].
- **Trois niveaux de raisonnement dans la contre-argumentation** [K07, K08, K09, p. 5] : complète, tronquée, réponse seule.
- **Trois styles familiers**, dont l'affirmation nue « The answer should be {refuting answer}. » [K10, K45, p. 5].
- **Une condition « juge »** : le modèle choisit entre sa réponse et la réponse opposée en un seul tour [K11, p. 5]. C'est le test de la première hypothèse du papier [K04, p. 2].
- **Tâches** : questions à choix multiples seulement [K33, p. 9].
- **Mesure** : taux binaire d'adoption de la réponse opposée [K12, p. 7].

### 4.3 Antériorité pour HC1 (N-005 et N-013) — verdict : voisin

| pièce de HC1 | dans 2509.16533 | pages |
|---|---|---|
| moniteurs de contrôle sous attaque | non : assistants qui répondent à un questionnaire ; le « juge » choisit entre deux réponses ; pas d'attaquant | 3, 5 |
| (a) destination libre ĉ, testée contre la cible et contre la moyenne du corpus, par famille | non : destination imposée (adoption de la réponse proposée). Indice catégoriel : une troisième réponse, ni l'initiale ni la proposée, n'apparaît que dans 0,9 % à 3,4 % des paires selon le jeu de questions [K34 à K39] | 7, 18 |
| (b) régression sur plusieurs intensités par famille | en partie : trois niveaux de raisonnement, de moyenne croissante 24,1, 43,3 et 56,1 % [K21], avec une exception [K20] ; aucune régression, aucun coefficient de gain ; le juge à une seule intensité | 5, 8 |
| (c) verdict lu par probabilité du jeton (méthode, plus revendiquée) | non : décodage glouton, lettre de réponse | 3 |
| (d) opposition juge / sonde | non : aucune sonde | — |

- **Verdict : voisin.**
  - En lecture dure, il occupe en partie le seul volet « intensités graduées » de (b). Ce volet est déjà publié (2606.14037, Sicilia et al., Koo et al. dans la compilation).
  - Aucune pièce revendiquée n'est occupée.
  - La piste « 2509.16533 » de la liste « à lire avant toute revendication » peut être close.
- **Contre-indice faible, et précaution de plan : la déférence dépend du contenu.**
  - Les modèles abandonnent moins une réponse initiale juste qu'une fausse, dans toutes les conditions [K32, p. 9 ; K44, p. 8].
  - La persuasion suit la qualité de la contre-argumentation [K25, K26, p. 8], notée par un juge externe, Gemini 2.5 Flash [K27, p. 8].
  - Pour HC1, g et ĉ risquent donc de mélanger deux populations. Il faudra stratifier selon la justesse du verdict initial du moniteur.
- **Précaution de transposition : le cadrage compte.**
  - Le cadrage « juge » réduit l'adoption : 43,6 % contre 56,1 % [K28, K29, p. 9 ; K13, p. 7]. Les auteurs en font une base « high-performance » [K31, p. 9], la meilleure en correction nette, +24,6 % [K43, p. 9].
  - L'inverse se produit chez GPT-4o-mini, 46,1 % contre 37,6 % [K14, p. 7].
  - Les ampleurs de déférence tirées de conversations ne se transposent pas telles quelles à un moniteur. C'est cohérent avec le choix de N-005 de ne revendiquer que la stabilité de rang.
- **Appui, pas contre-indice : structure par famille.** L'affirmation nue est la plus persuasive, 84,5 % [K17, p. 7 ; K23, p. 8 ; K30, p. 9]. Cela va dans le sens de la prédiction 2 de HC1 (g structuré par famille d'attaque).
- **HC3 : ne touche pas.** Aucune usurpation de l'instructeur. La contre-argumentation « DR », sans réponse proposée [K18, p. 7], porte encore un argument.

---

## 5. Réserves de symétrie (R4) sur les chiffres cités

**CaMeL**
- **Tokens.** Texte et tables se contredisent (voir 1.2 d) [C52, C53, C56, C59, C60, C67]. Le chiffre de 2,8 n'est opposable qu'avec sa base : table 10, hors attaque, médiane, Claude 3.5 Sonnet.
- **Nombre d'attaques.** Le texte dit « Gemini 2.5 Pro drops from 300 without to 0 with CaMeL » [C44, p. 14]. La table 4 donne 163 pour Gemini 2.5 Pro et 297 pour Gemini 2.5 Flash, lequel garde 1 succès avec CaMeL [C36, C37, p. 34].
- **Table 1** (Claude 3.5 Sonnet), p. 13.
  - La légende annonce « 2 instances of query misunderstanding » [C76] ; la table en compte 1 [C77].
  - Les totaux par suite (40, 16, 20, 20, soit 96 tâches) et les réussites (31, 12, 14, 5) [C78, C79] ne recoupent pas la table 5. Celle-ci implique 30 sur 40 et 15 sur 21, pour 97 tâches (calcul) [C28]. Total identique : 62.
- **Sécurité « prouvable » à lire sous son modèle de menace.**
  - Attaques non adaptatives [C50].
  - Canaux auxiliaires reconnus : « We find that CaMeL is vulnerable to side-channel attacks » [C85, p. 19].
  - Pour les modèles déjà robustes, l'appel natif est presque nul aussi : 2 succès pour o4-mini, 11 pour o3 [C38, C39]. Le gain de sécurité n'est discriminant que pour les modèles vulnérables.
- **Symétrie : un fait favorable à CaMeL, que la ligne 138 omet aussi.** Sous attaque, avec o3, l'utilité de CaMeL égale celle de l'appel natif [C24, C25].

**2607.02510**
- **Résultats qualitatifs, lus sur les figures.** Les seuls chiffres du texte sont des lectures de figures par les auteurs [S23, S33].
- **Aucun essai adverse.** Le moniteur hérite des limites du vérificateur, « in terms of informativeness, deployment cost, and adversarial robustness » [S27, p. 5].
- **Pas de 1 %** : niveaux de 5 à 50 % [S25].
- **Article d'atelier** [S03].
- **Pas de propreté suspecte.** Les auteurs rapportent eux-mêmes une violation de borne [S13].

**2606.06223** (réserves fortes : chiffres non opposables sans réserve)
- **Double compte probable du taux d'exploitation.**
  - Dans la table 2, les colonnes « Gameable » et « Easy grader » sont identiques sur les cinq lignes, et « Exploit » en vaut environ le double [W30 à W35, p. 6].
  - Les taux de la table 2 impliquent environ 368 positifs « exploit » (calcul). La table 8 en compte 184, soit exactement le nombre impliqué par « Gameable » seul [W42, p. 13].
  - Le chiffre phare « exploit-action rate is 0.450 » [W17, p. 5] est donc probablement compté deux fois. Le contrôle pour « bad » est juste : 3877 contre 3878 (calcul) [W41].
- **Figure contraire.**
  - La légende de la figure 4 met en avant « Mix50 » [W36, p. 8].
  - Lecture d'image : la figure ne montre que Control, Mix05, Mix10 et Hack, et donne à Mix05 un taux d'exploitation d'environ 0,11, contre 0,007 en table 2 [W32].
- **Cibles confondues.** Dans la table 9, « bad buy » et « low reward buy » ont des lignes identiques pour chaque famille [W44, W45, p. 16]. Les compter comme deux cibles gonfle l'étendue apparente.
- **Annexe vide.** L'annexe B est citée pour le prétraitement [W14, p. 4], mais elle est vide : son titre est suivi directement de celui de l'annexe C [W38, p. 10].
- **Sélection après coup.** La table 7 retient la « Best saved … row » pour chaque paire, groupe de traits et budget de raisonnement choisis après coup [W39, W40, p. 12]. Les cibles rares sont retirées des figures principales [W49, p. 13].
- **Choix de métrique.** La phrase du résumé [W06] ne vaut, pour la cible d'exploitation, que sur le gain d'aire précision-rappel. L'aire sous la courbe et le rappel à 20 % favorisent la sonde seule [W27 à W29].

**2509.16533**
- **Valeur p négative** : « (t = −4.56, p = −7.44e−6 ) » [K24, p. 8].
- **Monotonie annoncée mais pas tenue.**
  - Annonce : « For all refutation types and models … increase with more depth of reasoning » [K16, p. 7] et « consistently follow the pattern FR > TR > AR » [K22, p. 8].
  - Contre-exemple : GPT-4.1, adoption quand la réponse initiale est juste, 9,6 en tronqué contre 10,1 en réponse seule [K20, p. 8].
- **Deux tables discordantes** : DeepSeek-V3, Fi vaut 45,6 en table 4 et 45,5 en table 5 [K15, K19].
- **Table 11** [K34 à K38, p. 18].
  - Les colonnes conditionnelles ne somment pas à 100 pour MedMCQA et MMLU (97,9, calcul).
  - Elles s'écartent de la règle de Bayes appliquée aux autres colonnes de 0,3 à 6,4 points (calcul).
  - Les colonnes F, Fc et Fi sont, elles, cohérentes entre elles (calcul).
- **Référence fausse** : MMLU-Pro est attribué à « Kojima et al., 2022 » [K40, p. 4], article sur le raisonnement sans exemple [K41, p. 10].
- **Une seule exécution** gloutonne par condition [K05] ; coût total d'environ 100 dollars [K42, p. 12].
- **Contrôle positif.** Les moyennes du juge de la table 8 se retrouvent à partir de la table 4 : 43,61 et 24,60 (calcul) [K28].

---

## 6. Synthèse

**Verdicts, une ligne chacun**
- CaMeL, « Google DeepMind » : **corrigé**. Google, Google DeepMind et ETH Zurich ; le premier auteur est à Google et à l'ETH Zurich [C01, C03, C04, p. 1].
- CaMeL, « attaques réussies quasi nulles » : **confirmé**. De 0 à 11 sur 949 avec politiques selon le modèle ; attaques non adaptatives [C32 à C39, p. 34 ; C50, p. 17].
- CaMeL, « 77 % contre 84 % » : **confirmé**. o3 à effort élevé, hors attaque, quatre suites ; écart de 3 à 32 points selon le modèle [C07, p. 1 ; C13, C14, p. 33].
- CaMeL, « environ 2,8 fois plus de tokens » : **corrigé**. Médiane par tâche avec Claude 3.5 Sonnet, 6 à 7 fois en moyenne ; texte du papier incohérent [C52, C53, C59, C67].
- CaMeL pour HC3 : **voisin**. Aucune des deux composantes n'est faite [C68, C70, C45].
- 2607.02510 pour H2 : **occupe en partie, en boîte noire**. Une composante déjà prise, le calibrage sur séquences sûres entières ; contre-indice faible hors régime [S10, S12].
- 2606.06223 pour H2 : **occupe en partie**. Lecture dure : sondes de l'agent qui agit, raisonnement compris, déjà prises ; lecture souple : voisin. Réserves R4 fortes [W09, W37].
- 2509.16533 pour HC1 : **voisin**. Intensités graduées sans régression, destination imposée, ni moniteur ni attaque ni sonde [K07 à K12].

**Ce qui change pour la ligne 138**
- Remplacer la parenthèse de CaMeL par la formulation de 1.3 :
  - affiliation complète ;
  - base de chaque chiffre ;
  - séparation des deux modèles ;
  - moyenne à côté de la médiane.
- La flèche corrigée de `corrections-v1.md` (lignes 100 et 103) tient. CaMeL lui-même exclut l'influence « texte à texte » [C68, p. 5] et suppose manipulable le modèle qui lit les données [C69, p. 3 ; C72, p. 20]. On peut y ajouter ces pages.
- Les chiffres de CaMeL deviennent opposables avec leur base, sur ce PDF empreinté. Le 67 % de 2505.22852 reste non établi (question ouverte).

**Ce qui change pour H2, HC1 et HC3**
- **H2** : énoncé inchangé ; la conjonction reste libre. Trois apports :
  - **base supplémentaire à proposer** pour le préenregistrement de G1 (décision à Lazar) : un seuil unique sur le maximum, calibré par contrôle du risque sur des épisodes honnêtes entiers. Il fait jeu égal avec E-valuator hors régime diffus [S12] ;
  - **appui** à la lecture N-007 de « toujours valide » : un e-processus estimé viole sa borne [S13] ;
  - **précaution** : une sonde peut lire un régime plutôt qu'une action [W21]. Il faudra calibrer sur des épisodes honnêtes du même agent.
  - Piste nouvelle à lire : 2603.02798 [W46].
- **HC1** : énoncé inchangé.
  - 2509.16533 peut entrer dans les sources « citées comme publiées » au titre des intensités graduées sans régression, sur des assistants, et d'une destination catégorielle : presque toujours la réponse proposée [K21, K34 à K39].
  - Précaution de plan : stratifier g et ĉ selon la justesse du verdict initial [K32].
  - La référence exacte de Za et al. 2026, piste encore à lire, est donnée [W47].
- **HC3** : énoncé inchangé. CaMeL ne couvre aucune des deux composantes. Le « couvre les ordres en bande de HC3 » de la ligne 138 ne vaut pas pour un juge moniteur.

**Zone revendiquée trouvée occupée : aucune.**

---

## Annexe — fichiers de ce dossier

- `rapport-lot5-camel-et-pistes-v1.md` : ce rapport.
- `citations.json` : 219 citations (identifiant, fichier, page, texte exact).
- `scripts/verifier_citations.py` : contrôle, tests R5 (`tester`) et mutations (`muter`).
- `scripts/extraire_pages.sh` : extraction page par page en trois modes.
- `scripts/calculs_v1.py` : calculs de contrôle.
- `extractions/<identifiant>/{layout,brut,raw}/pNNN.txt` : texte de chaque page.
- `images/` : quatre pages de 2606.06223 rendues en image (p. 6, 7, 8, 15), pour les lectures d'image signalées.
- `scripts/verifier_renvois.py` : contrôle que chaque identifiant cité dans ce rapport existe et que la page dite est la sienne (219 sur 219, aucune page fausse).
- `controles/` :
  - `tests-R5-verificateur-v1.json` ;
  - `controle-citations-v1.json` ;
  - `mutations-v1.json` ;
  - `calculs-v1.txt` ;
  - `renvois-v1.txt`.
- `empreintes-v1.sha256` : empreintes de tous les fichiers produits.
