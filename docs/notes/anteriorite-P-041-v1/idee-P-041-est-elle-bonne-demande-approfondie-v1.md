# L'idée P-041 est-elle bonne ? Demande approfondie et reformulée — v1

session-depot, 30 octobre 2026. Demande de Lazar (≈ 18:00 UTC) : « brainstormons pour savoir si mon idée est bien bonne… version plus approfondie… puis demande au collisionneur de produire la réponse à ton prompt proposé » (GO-2026-10-30-15). Point de départ : la note d'antériorité (`note-anteriorite-P-041-lecteur-neuf-v1.md`, `618c7c48…`) — le champ du contrôle fait jouer l'attaque en dernier (Terekhov `2510.09462v2` p. 3, 10 ; Async Control p. 2, 5, 13 ; Ctrl-Z p. 4) ; P-041 fait jouer la défense en dernier sur les familles d'entraînement et mesure sur des familles tenues à l'écart fixes, conçues par des tiers.

## 1. Ce qu'un expert ferait, et que la demande ne dit pas

1. **Séparer deux revendications que « l'idée est bonne » confond.** (a) *Méthode de conception* : la défense qui voit les paramètres des familles d'entraînement apprend-elle une meilleure barrière qu'une défense qui ne les voit pas ? (b) *Méthode d'évaluation* : le chiffre de sûreté qu'on publie est-il honnête ? Le champ du contrôle refuse l'avantage du terrain pour (b), pas pour (a) : l'entraînement adverse est exactement (a). L'idée peut être bonne pour (a) et dangereuse pour (b).
2. **Nommer le danger exact** : si la défense s'ajuste aux familles qu'elle voit, son score sur ces familles surestime sa sûreté (c'est l'argument d'Async Control). Les familles tenues à l'écart ne protègent que si elles sont **indépendantes** des familles d'entraînement ; or elles viennent du même schéma de classes, et les cinq instances partagent des corpus d'entraînement. Le test décisif est le **débordement** (familles vues contre tenues à l'écart), et le **pire cas adaptatif** : une épreuve finale où un générateur ajuste ses familles **contre la barrière figée** (l'attaque joue en dernier, au niveau des lois seulement), qui borne ce que les familles fixes ne voient pas.
3. **Comparer à la bonne base** : la même défense entraînée sans paramètres (seulement des échantillons), à budget égal ; et la règle du champ appliquée telle quelle (attaque en dernier sur la défense finale). Si P-041 ne bat pas ces deux bases sur les familles tenues à l'écart **et** sous l'épreuve adaptative finale, l'idée n'apporte rien.
4. **Prédire le signe** et l'écrire avant : entraînement adverse et transfert à des menaces imprévues donnent des signes mitigés dans la littérature (Kang et collègues 2019 contre Tramèr et Boneh 2019, Casper et collègues 2024 : à relire sur PDF). Hypothèse honnête : gain intra-classe net, débordement modeste, gain hors classe incertain.
5. **Chercher la condition d'échec** : sous quelle structure (classes très séparées, familles tenues à l'écart hors du support du schéma, défense surparamétrée) l'avantage du terrain devient-il un surajustement ? Le dire comme une prédiction falsifiable.
6. **Faire juger par ceux qui défendent la règle contraire** : relecteurs des équipes qui publient « l'attaque joue en dernier » (lecture de leurs arguments, pas contact sans GO).

## 2. Données brutes de départ

- Les PDF déjà versés (Terekhov 2510.09462v2 et 2606.08892v2 ; Async Control ; Ctrl-Z ; Casper ; Sheshadri ; Bailey 2412.09565v2 ; Dai 2022 et 2025 ; MAGIC, AgentSafeEvo, EvoSafety, RvB), lus aux passages qui justifient « l'attaque joue en dernier ».
- Les générateurs scellés des familles de BA-002 après le contrôle de pureté (quarantaine), pour un monde simulé à vérité connue.
- Le monde simulé de l'orchestrateur (sur processeur) et ses journaux.
- Les épisodes de P3 et leurs activations, seulement à l'étape réelle.

## 3. Méthodes et outils

- Expérience simulée à quatre bras, à budget égal : (i) défense informée des paramètres (P-041) ; (ii) défense informée par échantillons seulement ; (iii) défense entraînée sur banque fixe ; (iv) défense de la règle du champ. Mesures : score intra-classe, débordement sur familles tenues à l'écart, **score sous épreuve adaptative finale** (générateur au niveau des lois, défense figée).
- Plusieurs schémas de séparation entre familles d'entraînement et tenues à l'écart (support commun, support disjoint) : effet de la dépendance sur l'honnêteté du chiffre.
- Préenregistrement : prédictions chiffrées avec signe, seuils, liste d'arrêt ; puissance par simulation.
- Collisionneur à quatre modèles pour la critique de la conception ; lecteur neuf pour la synthèse.

## 4. Vérification extérieure

- Familles tenues à l'écart des cinq instances tierces, scellées avant, lues une fois.
- Épreuve adaptative finale (l'attaque joue en dernier) : c'est la mesure que le champ reconnaît ; si P-041 la passe, l'objection tombe.
- Bancs publics conçus par d'autres.
- Reproductibilité du monde simulé par un tiers (graines, code scellé).

## 5. Demande reformulée (prompt proposé au collisionneur)

> « Un programme veut entraîner une défense (détecteur de déplacements de lois sur activations) en lui donnant les paramètres des familles d'entraînement (la défense joue en dernier), alors que le champ du contrôle des intelligences artificielles exige que l'évaluation fasse jouer le générateur en dernier contre la défense finale. (1) Sépare ce que l'avantage donné à la défense peut améliorer (la conception) de ce qu'il peut fausser (le chiffre publié), et dis sous quelles conditions chaque effet domine. (2) Les familles tenues à l'écart conçues par des tiers suffisent-elles à rendre le chiffre honnête ? Dis ce qui les rend dépendantes des familles d'entraînement et comment le mesurer. (3) Conçois l'expérience décisive, à budget égal, entre quatre bras (défense informée des paramètres ; informée par échantillons ; banque fixe ; règle du champ), mesurée sur trois scores (intra-classe ; débordement sur familles tenues à l'écart ; score sous épreuve finale où le générateur, au niveau des lois seulement, s'ajuste contre la défense figée), avec prédictions chiffrées et signe, seuils, contrôle négatif et condition d'échec. (4) Conclus : l'idée est-elle bonne, pour la conception, pour l'évaluation, ou pour aucune des deux, et à quelle condition ? »

Garde, vocabulaire et insertion : comme les autres questions du collisionneur v6 (générateur de familles d'épreuves, jamais les mots proscrits ; famille = étiquette abstraite).
