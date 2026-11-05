# L'idée P-041 est-elle bonne ? Demande approfondie et reformulée — v2, réponse de Fable 5.1 (indépendante de la v1 d'Opus 5.5)

session-depot servie par Fable 5.1, 30 octobre 2026. Lazar : « Fable répond à ton tour à ce prompt », puis « fusionne ta proposition avec celle d'Opus ». Cette v2 est écrite **sans relire** la v1 d'Opus (`idee-P-041-est-elle-bonne-demande-approfondie-v1.md`) ; la fusion est la v3.

Point de départ : le champ du contrôle fait jouer l'attaque en dernier (Terekhov `2510.09462v2` p. 3, 10 ; Async Control p. 2, 5, 13 ; Ctrl-Z p. 4) ; P-041 fait jouer la défense en dernier sur les familles d'entraînement, et mesure sur des familles tenues à l'écart fixes, conçues par des tiers.

## 1. Ce qu'un expert ferait, et que la demande ne dit pas

1. **Poser la question comme une question de validité statistique, pas de camp.** « L'attaque joue en dernier » est une règle d'**estimation** : elle garantit que le score mesuré est une borne supérieure honnête du taux de réussite d'une attaque adaptative. « La défense joue en dernier » est une règle d'**apprentissage** : elle produit une meilleure défense. Les deux règles ne sont pas contradictoires si elles s'appliquent à deux étapes différentes : entraîner avec l'avantage, évaluer sans. L'expert demanderait donc d'abord : *à quelle étape P-041 met-il l'avantage ?* Si c'est seulement à l'entraînement, l'idée n'est pas un contre-pied du champ ; c'est l'entraînement adverse standard, suivi de l'évaluation standard.
2. **Formaliser la fuite d'information entre entraînement et épreuve.** Les familles tenues à l'écart sont « fixes et conçues par des tiers », mais elles sont tirées du **même schéma** (classes C1, C2, C3 et sous-groupes de C-autre, plages déclarées). La défense qui a vu les paramètres des familles d'entraînement connaît donc le *support* du schéma. L'expert mesurerait la **dépendance** entre les deux lots (par exemple la distance entre les lois d'entraînement et les lois tenues à l'écart dans l'espace des paramètres, ou le taux d'appariement entre familles des deux lots par le lecteur isolé) et prédirait le débordement comme fonction de cette dépendance.
3. **Distinguer trois adversaires, du plus faible au plus fort**, et exiger un score pour chacun : (i) familles d'entraînement (vues) ; (ii) familles tenues à l'écart fixes (non vues, même schéma) ; (iii) générateur adaptatif au niveau des lois contre la défense **figée** (l'attaque joue en dernier, sans agent, sans texte). Le score (iii) est le seul que les occupants reconnaissent. Si P-041 refuse (iii), le champ a raison ; si P-041 l'accepte, il n'y a plus de contre-pied, seulement une **méthode d'entraînement** meilleure ou non.
4. **Choisir la bonne quantité à prédire** : non pas « la barrière est universelle », mais **l'écart entre (i), (ii) et (iii)**. Prédictions avec signe à sceller : (i) − (ii) > 0 (débordement), (ii) − (iii) > 0 (les familles fixes sous-estiment l'attaque adaptative), et la question ouverte : la défense informée des paramètres réduit-elle (ii) − (iii) par rapport à une défense informée seulement par échantillons ? C'est **là** que l'idée est bonne ou non.
5. **Prévoir le mode d'échec propre à l'avantage du terrain** : le surajustement aux paramètres (la défense apprend la paramétrisation, pas le phénomène). Test : reparamétrer les mêmes familles (transformation inversible des paramètres, mêmes lois) ; une défense qui a appris la paramétrisation chute, une défense qui a appris les lois ne bouge pas.
6. **Comparer aux bases que le champ accepterait** : même défense, même budget, (a) informée par échantillons seulement ; (b) entraînée sur la banque fixe sans avantage ; (c) protocole du champ tel quel (l'attaque en dernier à chaque génération).
7. **Lire les occupants aux passages précis** où ils refusent l'avantage (Async Control p. 13 : « amélioration itérative de la défense » comme source de surestimation) et dire en quoi le protocole de P-041 évite la cause nommée, ou ne l'évite pas.

## 2. Données brutes de départ

- Les PDF versés : Terekhov `2510.09462v2` et `2606.08892v2`, Async Control, Ctrl-Z, Bailey `2412.09565v2`, Casper, Sheshadri, Dai 2022 et 2025, MAGIC, AgentSafeEvo, EvoSafety, RvB, SafeCoEvo `2609.36580v2` ; lus aux passages sur l'ordre des coups et la surestimation.
- Les générateurs scellés de BA-002 après pureté (28 + 25 + 25 familles, quarantaine) : le monde simulé à vérité connue.
- La grille des classes et plages de l'axe 6 (`listes-closes-axe-6-v1.md`) : le schéma commun.
- Le monde simulé de l'orchestrateur et ses journaux (générations, promotions, témoins).
- Les épisodes de P3, seulement pour l'étape réelle, plus tard.

## 3. Méthodes et outils

- **Protocole à trois adversaires et quatre bras** (bras : paramètres ; échantillons ; banque fixe ; protocole du champ), à budget égal, sur le monde simulé ; score à 1 % de fausses alertes ; répétitions sur graines ; intervalles par rééchantillonnage.
- **Mesure de dépendance** entre lots : distance dans l'espace des paramètres, taux d'appariement par le lecteur isolé ; débordement prédit en fonction.
- **Test de reparamétrisation** (surajustement aux paramètres).
- **Générateur adaptatif au niveau des lois** (recherche de nouveauté dans la boîte de paramètres, contre la défense figée, sans jamais lire des scores sur épisodes réels : invariant N-053).
- **Préenregistrement** : prédictions signées sur (i) − (ii), (ii) − (iii), et l'effet du bras « paramètres » sur (ii) − (iii) ; seuils ; liste d'arrêt ; puissance par simulation.
- Collisionneur v6 à quatre modèles pour critiquer la conception ; lecteur neuf pour la synthèse.

## 4. Vérification extérieure

- Le score (iii), l'attaque adaptative en dernier, est **la mesure du champ** : si le programme le publie, les occupants peuvent le comparer à leurs chiffres.
- Familles tenues à l'écart des cinq instances, scellées avant, lues une seule fois.
- Reparamétrisation faite par un tiers qui ne connaît pas la défense.
- Bancs publics pour le transfert aux épisodes réels.
- Graines, manifestes, code scellé : rejeu par un tiers.

## 5. Demande reformulée (prompt proposé)

> « Un programme entraîne une défense (détecteur de déplacements de lois sur activations) en lui donnant les paramètres des familles d'entraînement : la défense joue en dernier à l'entraînement. Le champ exige que l'évaluation fasse jouer le générateur en dernier contre la défense finale. Réponds en quatre blocs. (1) Montre que « défense en dernier à l'entraînement » et « générateur en dernier à l'évaluation » sont compatibles ou non, et à quelle étape l'avantage du terrain cesse d'être légitime. (2) Définis trois scores — familles vues ; familles tenues à l'écart fixes du même schéma ; générateur adaptatif au niveau des lois contre la défense figée — et prédis le signe de leurs écarts ; dis ce qui rend les familles tenues à l'écart dépendantes des familles d'entraînement et comment mesurer cette dépendance. (3) Conçois l'expérience décisive à quatre bras et budget égal (défense informée des paramètres ; informée par échantillons ; banque fixe ; protocole du champ), avec le test de reparamétrisation contre le surajustement aux paramètres, prédictions chiffrées et signe, seuils, contrôle négatif, condition d'échec. (4) Conclus : l'avantage du terrain améliore-t-il la défense **mesurée par le score du champ**, et à quelle condition l'idée est-elle bonne ? »
