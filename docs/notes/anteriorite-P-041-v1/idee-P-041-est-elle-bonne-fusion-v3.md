# L'idée P-041 est-elle bonne ? Fusion des propositions d'Opus 5.5 (v1) et de Fable 5.1 (v2) — v3

session-depot, 30 octobre 2026. Demande de Lazar : « fusionne ta proposition avec celle d'Opus ». Sources : `idee-P-041-est-elle-bonne-demande-approfondie-v1.md` (Opus 5.5) et `…-v2-fable.md` (Fable 5.1, écrite sans relire la v1). Ce qui suit garde tout ce qui converge, et chaque apport propre est signalé [O] ou [F].

## 1. Ce qu'un expert ferait, et que la demande ne dit pas

1. **Séparer conception et évaluation** (les deux) : l'avantage du terrain est légitime pour **apprendre** la défense (c'est l'entraînement adverse) ; le champ ne le refuse que pour **mesurer** sa sûreté. Formulation de [F] : « l'attaque joue en dernier » est une règle d'**estimation** (le score est une borne honnête contre une attaque adaptative), « la défense joue en dernier » une règle d'**apprentissage** ; elles se combinent si l'on entraîne avec l'avantage et l'on évalue sans. Si P-041 n'utilise l'avantage qu'à l'entraînement, ce n'est pas un contre-pied du champ, c'est sa pratique standard ; la nouveauté est ailleurs (assemblage, niveau des lois, familles de tiers, mesure de la boucle).
2. **Trois adversaires, trois scores** (les deux) : (i) familles vues ; (ii) familles tenues à l'écart fixes, conçues par des tiers, du même schéma ; (iii) **générateur adaptatif au niveau des lois contre la défense figée** (l'attaque joue en dernier, sans agent ni texte, invariant N-053). Seul (iii) est reconnu par le champ ; sans lui, l'objection d'Async Control tient.
3. **La quantité à prédire est l'écart entre les trois scores** [F] : (i) − (ii) > 0 (débordement), (ii) − (iii) > 0 (les familles fixes sous-estiment l'adaptatif) ; question décisive : **l'avantage des paramètres réduit-il (ii) − (iii)** par rapport à une défense informée seulement par échantillons ? C'est là que l'idée est bonne ou non.
4. **Mesurer la dépendance entre familles d'entraînement et tenues à l'écart** (les deux) : même schéma de classes, instances aux corpus proches. Mesures : distance dans l'espace des paramètres, taux d'appariement par le lecteur isolé [F] ; variantes de séparation, support commun contre support disjoint [O]. Le débordement se prédit en fonction de cette dépendance.
5. **Test de reparamétrisation** [F] : mêmes lois, paramètres transformés de façon inversible ; une défense qui a appris la paramétrisation chute, une défense qui a appris les lois ne bouge pas. C'est la condition d'échec propre à l'avantage du terrain (surajustement aux paramètres), que [O] demandait de chercher.
6. **Bases à battre, à budget égal** (les deux) : défense informée par échantillons ; banque fixe ; protocole du champ (l'attaque en dernier à chaque génération).
7. **Signe attendu, écrit avant** [O] : gain intra-classe net, débordement modeste, gain hors classe incertain ; littérature mitigée (Kang et collègues 2019 contre Tramèr et Boneh 2019, Casper et collègues 2024).
8. **Lire les tenants de la règle contraire aux passages précis** (les deux) : Async Control p. 13 (amélioration itérative comme source de surestimation), Terekhov `2510.09462v2` p. 3 et 10, Ctrl-Z p. 4 ; dire en quoi le protocole évite la cause nommée.
9. **Deux échelles de temps pour la défense** (nouveau, demande de Lazar sur SafeCoEvo `2609.36580v2`) : un palier rapide explicite (règles de détection, seuils, règle d'agrégation, mémoire de cas validés) mis à jour entre épisodes, et un palier lent (poids des sondes réentraînés sur l'expérience accumulée) entre générations ; aucune règle propre à une famille n'est gardée (abstraction obligatoire) ; les familles tenues à l'écart n'entrent jamais dans l'expérience accumulée. À mesurer comme un cinquième bras.

## 2. Données brutes de départ

PDF versés (Terekhov `2510.09462v2` et `2606.08892v2`, Async Control, Ctrl-Z, Bailey `2412.09565v2`, Casper, Sheshadri, Dai 2022 et 2025, MAGIC, AgentSafeEvo, EvoSafety, RvB, SafeCoEvo ; primaires de la coévolution fournis par Lazar : Rosin et Belew, Cliff et Miller, Watson et Pollack, Garcia et collègues 2017, Paruchuri et collègues 2008) ; générateurs scellés de BA-002 après pureté ; grille des classes et plages de l'axe 6 ; monde simulé de l'orchestrateur ; épisodes de P3 à l'étape réelle seulement.

## 3. Méthodes et outils

Expérience simulée à **cinq bras** et budget égal (paramètres ; échantillons ; banque fixe ; protocole du champ ; paramètres à deux échelles de temps), **trois scores** ((i), (ii), (iii)), **deux régimes de dépendance** (support commun, support disjoint), **test de reparamétrisation** ; score à 1 % de fausses alertes, graines, intervalles par rééchantillonnage ; préenregistrement (prédictions signées sur (i) − (ii), (ii) − (iii) et l'effet des bras sur (ii) − (iii), seuils, liste d'arrêt, puissance par simulation) ; collisionneur v6 pour la critique, lecteur neuf pour la synthèse.

## 4. Vérification extérieure

Le score (iii) publié, comparable aux chiffres des occupants ; familles des cinq instances scellées avant, lues une fois ; reparamétrisation faite par un tiers ; bancs publics ; rejeu par un tiers (graines, code scellé).

## 5. Prompt fusionné pour le collisionneur

> « Un programme entraîne une défense (détecteur de déplacements de lois sur activations synthétiques) en lui donnant les paramètres des familles d'entraînement : la défense joue en dernier à l'entraînement. Le champ du contrôle exige que l'évaluation fasse jouer le générateur en dernier contre la défense finale. Réponds en cinq blocs.
> (1) Les deux règles sont-elles compatibles ? Sépare ce que l'avantage peut améliorer (la défense apprise) de ce qu'il peut fausser (le chiffre publié), et dis à quelle étape il cesse d'être légitime.
> (2) Définis trois scores : familles vues ; familles tenues à l'écart fixes du même schéma, conçues par des tiers ; générateur adaptatif au niveau des lois contre la défense figée. Prédis le signe de leurs écarts. Dis ce qui rend les familles tenues à l'écart dépendantes des familles d'entraînement et comment le mesurer.
> (3) Conçois l'expérience décisive à budget égal, à cinq bras (défense informée des paramètres ; informée par échantillons ; banque fixe ; protocole du champ ; paramètres avec deux échelles de temps : règles explicites rapides, poids réentraînés lentement), sous deux régimes de dépendance, avec un test de reparamétrisation contre le surajustement aux paramètres ; prédictions chiffrées et signe, seuils, contrôle négatif, condition d'échec.
> (4) Dis quelle quantité tranche : l'avantage réduit-il l'écart entre les familles fixes et le générateur adaptatif ?
> (5) Conclus : l'idée est-elle bonne pour la conception, pour l'évaluation, ou pour aucune des deux, et à quelle condition ? »

Garde, vocabulaire (générateur de familles d'épreuves ; jamais les mots proscrits) et insertion dans les consignes : comme les autres questions du collisionneur v6.
