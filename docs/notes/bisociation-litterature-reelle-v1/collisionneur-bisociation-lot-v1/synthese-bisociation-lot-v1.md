# Synthèse — collisionneur sur le bisociateur (lot conv-audit n° 262, étage 3) — v1

Lecteur neuf (Opus 5.5), 31 octobre 2026, pour Lazar. Je n'ai écrit ni la question ni aucune réponse. Ce tour n'a pas de critères gelés : c'est une lecture, pas un verdict de porte.

**Lu.** Empreintes vérifiées, toutes OK :
- la question, identique à `run-bisociation-lot-e3-v1/question-etage3.md` ;
- les faits, identiques à `run-…/faits.md` ;
- `etat.md` ;
- les douze cellules.

**Abréviations.** T1 = III.1 conception, T2 = III.2 critique croisée, T3 = III.3 réponse. A = Fable 5.1, B = Opus 4.6, C = Argon, D = Kimi K3.1 Pro.

| Cellule | sha256 (12) | Cellule | sha256 (12) | Cellule | sha256 (12) |
|---|---|---|---|---|---|
| T1-A | c76353729eb4 | T2-A | 301589ea27bf | T3-A | 353abea4c0b6 |
| T1-B | f6ed0429f216 | T2-B | be612fe866ae | T3-B | 8a687adc60cb |
| T1-C | b286e97b54a8 | T2-C | 05250ab952af | T3-C | 77b8906a806d |
| T1-D | 390b91f087e2 | T2-D | d59d68dafc25 | T3-D | 1a421917d8ba |

## Verdict

1. Aucune affirmation forte de la question n'est établie. Les quatre espèces classent HYPOTHÈSE ou RAPPORTÉ :
   - la fertilité comme propriété de la paire ;
   - la transition de phase ;
   - l'émergence par essaims ;
   - les causes trouvées par apprentissage profond.
2. Le gain est méthodologique. Au tour T2, au moins trois espèces relèvent chacune trois défauts, sans se concerter :
   - le pic de variance binomiale pris pour de la criticité ;
   - la sur-additivité F faussée par le budget et la combinatoire ;
   - l'étiquette de pont lue dans le même flux de citations que le trou (retour à la moyenne, appelé « A0 »).

   Au tour T3, les quatre espèces les acceptent.
3. Divergence sur la première expérience : reproduire Gu-Krenn (A), constituer la base de ponts avec rétrodiction inversée (B), lancer le duel 1 sur processeur (C), lancer E1′ (D). Accord sur le goulot : une base de ponts datés assez grande pour avoir de la puissance.
4. Question G : personne ne donne de référence exacte pour un « allumage » de champ. Seule la pièce d'Argon rapporte un seuil R₀ > 1, sans PDF. B ne traite pas G.

## Lecture question par question

Le gabarit de l'étage 3 impose quatre parties : présupposés, duels, instruments, ancrage. Il ne suit pas les questions A à G. Les reformulations sont donc les hypothèses H_A/H_B corrigées en T3.

### A. L'objet à mesurer
- **Accord.** Le profil « canal faible, structure commune forte » remplace la distance seule (T1-A E1 ; T1-B exp. 1 ; T1-C duel 1 ; T1-D E1). Les niches détectées sont une HYPOTHÈSE (T1-B P1 ; T1-D « Des chapelles stables existent… HYPOTHÈSE »).
- **Réfutations des pièces.** Le modèle de blocs d'Argon « regroupe les adversaires qui se citent » (T1-C a1). Le LaTeX brut ne livre pas d'isomorphismes sans « résolveur symbolique » (T1-C a2).
- **Défauts trouvés en T2.**
  - Apparier les témoins sur la distance textuelle « retire la variable testée » (T2-A ; T2-C « tautologie »).
  - Le contrôle négatif de B est « vide » (T2-A, T2-C, T2-D).
  - A0 : « le "trou" prédit mécaniquement une hausse » (T2-A).
  - Le pont défini par co-citation produit une « circularité explicite » (T2-D sur C).
  - La densité d'équations confond le score (T2-B sur C).
  - Les identités banales gonflent le score (T2-C sur B).
- **Désaccord.** A, C et D redéfinissent le pont par la reprise ou la réutilisation dans une tierce niche (T3-A, T3-C, T3-D). B ajoute A0 mais écrit « H_A / H_B : inchangées » (T3-B) : son étiquette reste lue dans les citations.
- **Apports d'une seule espèce.**
  - B : le graphe amputé des articles-ponts (T2-B c1).
  - A puis D : une famille fermée et scellée d'implémentations, contre la « régression infinie » (T2-A, T3-D).
  - A : une partition calculée sans la couche des équations (T3-A).
- **Reformulation.** « β₂ > 0 avec intervalle à 90 % excluant zéro » à canal et popularité contrôlés (T3-A E1′). C propose un modèle emboîté où l'on ajoute d_math (T3-C).

### B. La fertilité
- **Accord.**
  - Les transitions mesurées n'existent « jamais sur P(reprise | paire) » (T1-A a2 ; T1-B P5 ; T1-C a3).
  - La fertilité dépend du quadruplet paire, procédé, budget, juge (T1-A a1 ; T1-D).
- **Défaut trouvé en T2 par trois espèces séparément.** Pour une issue binaire, la variance p(1−p) culmine à p = 0,5 quelle que soit la courbe (T2-A sur D : « n'est pas une signature critique » ; T2-C sur B ; T2-D sur A). En T3, toutes passent à la surdispersion entre réplicats (T3-A à D).
- **Défaut trouvé en T2 par trois espèces séparément.** F dépend du budget de chaque terme (T2-A : « la variable testée est alors l'allocation »). La copie renommée « ne donne jamais F ≈ 0 » (T2-C). F reste positif par simple combinatoire (T2-D). Corrections en T3 :
  - unions aléatoires appariées (T3-A) ;
  - budget et prémisses constants (T3-C) ;
  - séparation entre fertilité structurelle et avantage du processus (T3-D).
- **Désaccord.** Sur la littérature réelle, A refuse les tests de criticité, car la taille n'y est pas identifiable (« jamais sur la littérature réelle », T3-A). B les garde à partir de 5 tailles (T3-B). C et D restent en mondes inventés (T3-C, T3-D).
- **Apports d'une seule espèce.**
  - C : le nul du maximum d'échantillon (T2-C c3) et la taille comme variable endogène (T2-C sur B).
  - B : la cloche asymétrique (T2-B).
- **Réfutation d'une pièce.** Le ralentissement critique d'Argon « se confond… avec l'indécidabilité » (T1-C a3).

### C. Apprendre ; Gu-Krenn
- **Accord.** Reproduire Gu-Krenn avant de s'en servir (T1-B, T1-D E4, T3-A E6′). Battre un témoin « popularité seule » (les quatre).
- **Réfutations des pièces.** Argon fusionne 2402.08640 et 2405.17044 : « erreur d'attribution » (T1-A a4, vérifié dans les faits). L'affirmation « signal porté par la centralité » est « sans source » (T1-A a4).
- **Désaccord non résolu.**
  - B et C présentent cette domination par la centralité comme établie (T3-B c1 ; T3-C c2). Je vérifie : seule la pièce d'Argon l'affirme.
  - C l'attribue à tort à la réponse indépendante 4 (T1-C a4 : « Comme l'avertit… »).
  - B rattache à 2402.08640 la corrélation négative avec l'intérêt jugé (T1-B P2). Les faits la placent dans 2405.17044.
- **Défauts trouvés en T2.**
  - À distance supérieure à 3, les voisins communs sont nuls par construction (T2-C). A l'accepte mais défend le produit des degrés (T3-A).
  - Un échec de reproduction « suspend, il ne falsifie pas » (T2-A ; accepté en T3-D).
- **Reformulation.** Mesurer le « gain conditionnel… au-dessus du modèle popularité seule », intra-strate (T3-A E6′). Pour C, la régression symbolique est jugée à part, avec « R² ≥ 0,85 » (T3-C duel 3).

### D. Causes
- **Accord.** L'apprentissage profond « estime sous identification donnée » (T3-A c).
- **Défauts trouvés en T2.**
  - La dose 7 est interpolée : la puissance du critère de B « ne peut jamais dépasser α = 10 % » (T2-C).
  - C fond identification et transport (T2-A).
  - Conditionner sur la publication crée un biais de Berkson (T2-C sur D).
- **Corrections en T3.**
  - B extrapole à la dose 15 (T3-B).
  - C scinde en 4a/4b : « Un échec en 4a falsifie l'apprentissage causal… » (T3-C).
  - A et D ajoutent un bras intra-niche et un placebo apparié en longueur (T3-A, T3-D).
- **Apport d'une seule espèce.** D propose une « école d'été avec binômes randomisés », avec la même intervention (T3-D E6′). C'est un contact externe et une dépense, donc un nœud.

### E. Régimes
- **Accord.** Les deux systèmes d'OpenAI reçoivent des problèmes déjà posés (T1-A a7 ; T1-B P8 ; T3-D). Aucune ablation n'est publiée (T1-B P6 ; T3-A).
- **Rien de nouveau** sur la construction des systèmes au-delà des pièces.
- **Contradictions des pièces relevées.** Lean « 162/722 contre 300/719 » ; Bastounis et al. daté du 6 ou du 27 octobre (T1-A a7, accepté en T3-C). Vérifié dans les faits : « non réconciliés ».
- **Défauts trouvés en T2.**
  - La métrique survie × couverture cache le signe (T2-A, T2-C).
  - La provenance est auto-déclarée par le consolidateur (T2-A ; T2-C « garanti sans qu'aucune synergie »).
- **Contrôles repris par tous en T3.**
  - meilleur-de-N à contexte enrichi (T2-B) ;
  - brouillage des messages au sein de la même paire (T2-D) ;
  - familles de modèles hétérogènes (T2-B) ;
  - comptabilité de tous les tokens (T2-A).

### F. Questions manquées
- **Seul C dresse une liste** (T1-C d) :
  - un « porteur bilingue » ;
  - le biais anti-nouveauté du juge ;
  - la pollution synthétique des trous ;
  - la digestibilité.
- **Ailleurs, des présupposés jouent ce rôle :**
  - juges notant « à horizon zéro » (T1-A a10) ;
  - aucune base de ponts postérieurs à 1991 (T1-A a9) ;
  - test sur mondes inventés « aucun résultat… dans les faits » (T1-A a6) ;
  - revue « exhaustive » vue comme une promesse (T1-D) ;
  - mémoire des juges qui contamine les cas historiques (T2-A, T2-C). D'où l'E4′ de A en « mondes inventés où distance… et qualité sont plantées indépendamment » (T3-A).

## (i) Références citées

Toutes sont **SUPPOSÉ** au sens de R7 : aucun PDF empreinté (T1-A préambule ; T1-D « Je ne vérifie rien de nouveau »).

- **Déjà dans les pièces** (recherche dans les faits) : Swanson, Burt, Vilhena, Uzzi, Fleming, Shi-Evans, Sourati-Evans, Gu-Krenn (deux articles), Krenn 2023, Guimerà, Bettencourt 2006 à 2015, Ham 2007, Tria, Weitzman, Derex-Boyd, Fang-Lee-Schilling, Lazer-Friedman, Lorenz, Ashery, Doshi-Hauser, Wang-Veugelers-Stephan, Ke, Chu-Evans, Merton, Li-Lin-Wu, Poursafaei, Yang, Benson, Tshitoyan, Gentner, Galison, Funk-Owen-Smith, Schaeffer, Peters, Arjovsky, Reisach, Rosenfeld, Chernozhukov, Azoulay, Catalini, Boudreau, Pearl-Bareinboim, Bastounis-Circelli-Hansen, OpenAI.
- **Nouvelles.** Aucune référence bibliographique. Ne s'ajoutent que des méthodes et des outils, sans version ni source vérifiée :
  - l'estimateur « famille Chao », « RAPPORTÉ de mémoire » (T3-A) ;
  - la correction de Firth et les deux tests unilatéraux d'équivalence (T3-B, T3-C) ;
  - les lois de Gumbel et skew-normal (T2-C, T3-B, T3-C) ;
  - LaTeXML, APTED, EconML, SPECTER2, vLLM, SymPy (T1-C, T3-C) ;
  - les modèles ouverts Qwen, Llama, DeepSeek et Mistral (T1-B, T1-C, T1-D).

## (ii) Question G

- **A.** « un seuil d'auto-entretien existe sous forme de R₀ > 1 (RAPPORTÉ), le mot « allumage » n'est pas attesté pour les champs scientifiques… verser les deux PDF » (T1-A a12 ; T3-A c).
- **B.** Ne répond pas. Il cite Bettencourt-Kaiser 2015 seulement pour les transitions topologiques (T1-B P1, P5).
- **C** (même modèle que l'auteur de la pièce Argon).
  - Il écrit « RAPPORTÉ (vérifié par `relecture-fable-reponse-3-v1` et `Argon`) » (T1-C a8), alors que la relecture 3 dit « terme introuvable ».
  - Il attribue « ignition » à Ham 2007 (neurosciences), R₀ > 1 à Bettencourt 2006 et 2008, la transition topologique à Bettencourt 2009 et 2015 (T3-C c1).
- **D.** « seuil épidémiologique et transition topologique à distinguer ; absence du vocabulaire « ignition » non démontrée » (T1-D G).
- **Référence exacte.** Les articles sont donnés avec titre, revue et DOI, depuis la pièce d'Argon. Pour un « allumage » de champ, aucune.
- **Mon constat** (SUPPOSÉ, fondé sur la concordance des auteurs et de la date). L'arXiv physics/0502067, que la relecture 3 a lu sans y trouver « threshold », est probablement la prépublication du *Physica A* 2006 cité par Argon. Le conflit porte donc sur le même travail : page de résumé contre texte intégral non lu.
- **Autre écart.** Argon écrit « huit champs », la revue en compte neuf pour 2015.

## (iii) Trois mesures décisives

Les seuils sont illustratifs selon leurs auteurs.

1. **E1′ / duel 1 — profil trou et structure contre distance et popularité.**
   - Signe attendu sous H_B : β₂ > 0, intervalle à 90 % excluant zéro, bootstrap par niches (T3-A).
   - Variante : gain relatif ≥ 20 % en précision dans les 100 premiers, intervalle à 95 % par blocs (T3-C).
   - Marge d'équivalence δ₀ = 0,03 (T3-B).
   - Arrêt : si la rétrodiction inversée atteint le score prospectif − δ₀, suspension (T3-B).
   - Puissance vérifiée avant le lancement (T3-A, T3-D). C'est la seule issue qui « tue réellement une décision de conception » (T3-D).
2. **E6′ — gain conditionnel de Gu-Krenn à longue portée.**
   - Critère : un gain positif au-dessus de la popularité seule dans la strate de distance supérieure à 3 (T3-A).
   - Coût : nul selon A, « ~300-1 000 € » de carte graphique selon B (T1-B d).
   - Elle tranche la question posée « dès maintenant ».
3. **E2′ / duel 2 — étalonnage des tests de criticité sur mondes plantés.**
   - Critère de A : taux de détection ≥ 0,9, fausses alertes ≤ 0,1 (T3-A).
   - Critère de C : 5 tailles sur deux décades, 50 réplicats, φ > 2,0 au point critique, erreur de superposition < 5 % sur une taille tenue à l'écart ; falsification si φ ≤ 1,2 (T3-C).
   - Si l'étalonnage échoue, le mot « transition de phase » sort du préenregistrement (T3-A).

**Mesure suivante, plus coûteuse : l'essaim contre l'élargissement du contexte.** Il faut ≥ 20 % d'avantage sur le meilleur de tous les témoins. Le pilote s'arrête s'il donne moins de 50 survivantes par cellule (T3-A E3′). Pour B, la marge d'équivalence est δ₀ = 5 % de survie (T3-B).

## (iv) Décisions à proposer

**1. Rendre obligatoires six garde-fous** dans tout préenregistrement du bisociateur sur littérature réelle :
- une étiquette de pont indépendante du canal (tierce niche) ;
- la rétrodiction inversée ;
- un graphe amputé des ponts ;
- un bras « popularité seule » ;
- des jeux disjoints par niche et par période ;
- un calcul de puissance préalable.

Enjeu : sinon, le résultat positif est acquis par construction. Options :
- (a) gabarit complet : il ferme les trois artefacts, mais demande une base plus grande ;
- (b) seulement la rétrodiction inversée et l'étiquette : plus léger, mais la circularité de la partition reste ;
- (c) au cas par cas : souple, mais l'erreur se répète.

Recommandation : (a). Confiance élevée sur le fond, sachant que l'accord en T3 n'est pas indépendant. Défaut sous 48 h : (a).

**2. Fixer l'ordre de départ, sans dépense.** Enjeu : la base de ponts conditionne tout. Options :
- (a) base de ponts, puissance et rétrodiction inversée sur un sous-corpus traité sur processeur (B, D) : c'est le vrai goulot, mais il prend des jours humains ;
- (b) Gu-Krenn d'abord (A) : rapide, mais ne teste pas le trou ;
- (c) les deux en parallèle, processeur seul : couvre tout, mais fait deux chantiers.

Recommandation : (c), confiance moyenne. Défaut sous 48 h : (c).

**3. Dépense : un devis pour reproduire Gu-Krenn sur carte graphique ?** Enjeu : nul selon A, 300 à 1 000 € selon B. Options :
- (a) vérifier d'abord si le code tourne sur processeur : prudent, mais peut-être lent ;
- (b) devis immédiat : rapide, mais la dépense est peut-être inutile.

Recommandation : (a), confiance moyenne. Aucun défaut (dépense).

**4. Nœud : retirer « transition de phase » des préenregistrements sur littérature réelle.** Le terme n'est admis en mondes inventés et en courses qu'après E2′. Enjeu : c'est l'énoncé de ton hypothèse, et la taille n'y est pas identifiable. Options :
- (a) retrait (A) : honnête, mais on perd l'énoncé fort ;
- (b) maintien à partir de 5 tailles (B) : garde l'ambition, mais la confusion sociologique reste (T2-C) ;
- (c) suspension jusqu'à E2′ : neutre, mais retarde.

Recommandation : (c), puis (a) si E2′ échoue ; confiance moyenne. Aucun défaut (modification d'énoncé).

**5. Clore G par lecture.** Verser physics/0502067, 1504.00319 et les articles de 2008, 2009 et Ham 2007, puis chercher « ignition », « threshold » et « R0 » dans le texte intégral. Enjeu : éviter une attribution fausse dans un papier. Options :
- (a) versions arXiv d'abord, sans dépense : immédiat, mais incomplet ;
- (b) achat des articles : complet, mais c'est une dépense.

Recommandation : (a), confiance élevée. Défaut sous 48 h : (a).

**6. Erratum joint au lot.** Il porte sur :
- la fusion des deux articles Gu-Krenn par Argon ;
- la « centralité » non sourcée, reprise comme établie (T3-B, T3-C) ;
- l'attribution par B d'un résultat de 2405.17044 à 2402.08640 ;
- l'attribution par C d'une phrase à la réponse indépendante 4 ;
- la citation par B, comme venant de A, d'une phrase de D (« cela ne valide pas encore une fertilité bibliographique » : présente en T1-D E2, absente de T1-A, relevé par T3-A) ;
- les chiffres 162/722 contre 300/719, les dates 6 ou 27 octobre, huit ou neuf champs.

Enjeu : ces chiffres ne sont pas opposables (R7). Options :
- (a) erratum : trace propre, un fichier de plus ;
- (b) rien : aucun coût, mais l'erreur se propage.

Recommandation : (a), confiance élevée. Défaut sous 48 h : (a).

**7. Dépense, à ne pas demander maintenant : pilote d'essaim et école d'été.** Enjeu : 3 000 à 20 000 € (T1-D), ou 4 000 à 5 000 $ (T3-C), tous illustratifs ; et un contact externe. Options :
- (a) attendre E1′ : pas d'aveugle, mais du retard ;
- (b) devis tout de suite : rapide, mais on paie avant de savoir si le trou existe.

Recommandation : (a), confiance élevée. Aucun défaut.

## Réserves

- **Lignée.** Les quatre espèces ne sont pas indépendantes des pièces :
  - A (Fable 5.1) est le modèle de conv-audit pour les questions 2 à 5 et pour les relectures : il attaque surtout ses propres pièces.
  - B est de la même lignée.
  - C défend sa propre pièce : il transforme « introuvable » en « vérifié » (T1-C a8) et reprend la centralité non sourcée.
  - Seul D est extérieur.
- **Indépendance des accords.** Les accords de T3 suivent la lecture des critiques. Ceux de T2 sont plus indépendants, mais sous le même gabarit.
- **Effet de la question.** Le gabarit tire vers la conception d'expériences : G traité par 3 espèces sur 4, F par une seule, la construction des systèmes (E) par aucune, aucune référence nouvelle.
- **Non vérifié.** Aucun PDF n'a été lu. Seuils et coûts sont illustratifs. Je n'ai confronté aux faits que les points cités ici. Rien n'a été vérifié hors du dépôt.
- **Hors périmètre.** J'ai ouvert par erreur le début de `run-…/journal.jsonl`, non nommé, et je n'en tire rien. Un point est à vérifier : il porte « essai 2 » pour T1-A, alors que `etat.md` indique 1.
