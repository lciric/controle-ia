## Périmètre (à respecter sans exception)

Le périmètre est statistique et méthodologique : définitions, estimateurs, plans de mesure, validation. Aucune famille, aucun comportement d'agent et aucun moyen ne sont décrits, même à titre d'illustration ; la réponse qui le ferait est écartée.

## Contexte (autoportant : il suffit à répondre)

Un programme de recherche défensive étudie le contrôle de systèmes d'intelligence artificielle : détection d'un sabotage diffus par des sondes sur les activations internes et par des moniteurs qui ne lisent que le texte (boîte noire), avec agrégation séquentielle des indices ; modèles à poids ouverts de 8 et de 70 milliards de paramètres (RAPPORTÉ, demande du directeur). Règle de base : le programme ne construit aucun agent attaquant opérationnel (RAPPORTÉ, demande du directeur). Pour évaluer ses défenses, il utilise des **familles** (classes d'éléments d'évaluation simulés, définies par un schéma de construction, jamais décrites ici), dont certaines sont **tenues à l'écart** : ni les concepteurs de la défense ni la défense ne les voient avant la mesure finale.

Le **texte III** d'une course d'idéation demandera, au niveau méthode, comment concevoir un **banc d'évaluation adverse simulé** (il sert à mesurer, sans agent opérationnel) et une **mesure de l'universalité** des défenses qu'**un tiers puisse vérifier**. Ta réponse produit les questions candidates de ce texte ; elle sert de matériau à un préenregistrement et ne tranche rien.

Chaque fait porte un statut : VÉRIFIÉ, RAPPORTÉ, OBSERVÉ-NON-AUDITÉ ou HYPOTHÈSE. Tout chiffre qui ne vient pas du contexte ou des faits est marqué « illustratif » ; une référence que tu ne peux pas attribuer (auteurs, année, titre) porte « référence à vérifier ».

Donnée de départ (VÉRIFIÉ ; calculs refaisables) : deux sources indépendantes en apparence ont énuméré 28 et 25 familles. Selon le dossier, les deux sources sont deux modèles de fournisseurs différents, qui ont reçu la même question ; un lecteur unique, de la lignée d'une des deux sources, a fait l'appariement avec une grille fermée ; l'appariement n'est pas bijectif (une famille de la première source en recouvre deux de la seconde). L'intersection vaut donc 18 comptée du côté de la première source et 19 du côté de la seconde ; 10 familles sont propres à la première, 6 à la seconde. Lincoln-Petersen (n₁ × n₂ / m) : 38,9 avec m = 18, 36,8 avec m = 19. Chapman ((n₁ + 1)(n₂ + 1) / (m + 1) − 1) : 38,7 ou 36,7.

## Question

« Conçois la **méthode** qui permettrait d'affirmer, devant un tiers, qu'une défense est universelle sur un ensemble de familles, et de confronter cette affirmation à des mesures extérieures. Réponds par quatre blocs, dans cet ordre.

### Bloc 1 — Quatre propositions préalables, avant toute question candidate (au plus 1 200 mots)

**(a) Définition opérationnelle de l'universalité.** Options à comparer : pire cas sur une classe de familles déclarée d'avance ; écart de performance entre familles vues et familles tenues à l'écart ; quantile ou proportion de familles où la défense passe un seuil ; autre. Pour chacune : ce qu'il faut déclarer avant la mesure, l'énoncé exact qu'elle autorise (avec quantificateur, classe et statistique), ce qu'elle n'autorise pas, et comment un tiers la vérifie. Dis en particulier ce qui sépare « universelle sur la classe déclarée » de « robuste à l'inconnu ».

**(b) Régime d'information de l'évaluation** : aveugle ou informé de la défense ; quelles catégories d'information sont accessibles au banc d'évaluation (existence de la défense, liste des familles, protocole, seuils) ; budget d'évaluation (nombre d'éléments, calcul) ; rapport par palier. Précise aussi ce que l'évaluation interdit de partager entre construction et évaluation de la défense.

**(c) Combien de familles, par simulation.** Comment calculer le nombre de familles nécessaire pour affirmer l'universalité avec une confiance donnée : énoncé cible (par exemple : avec confiance 1 − α, la part de la classe où la défense échoue est inférieure à ε), modèle génératif de la population de familles, hétérogénéité et dépendance entre familles proches, variance à deux niveaux (entre familles, et entre éléments d'une famille), règle d'arrêt séquentielle, analyses de sensibilité. Un point à traiter : les familles sont **découvertes**, non tirées au hasard ; la garantie dépend donc du mécanisme de découverte. Dis ce que la simulation peut démontrer et ce qu'elle suppose.

**(d) Combien de familles encore inconnues.** Vérifie les calculs de Lincoln-Petersen et de Chapman donnés au contexte sous les deux conventions d'appariement (m = 18 et m = 19), et dis laquelle se défend et pourquoi. Discute ensuite leurs hypothèses : population fermée, indépendance des sources, même probabilité de capture pour toutes les familles, appariement exact. Dis dans quel sens la dépendance entre sources, l'hétérogénéité et l'erreur d'appariement déplacent l'estimation. Indique quels estimateurs employer avec plusieurs sources : Chao (bornes inférieures), Good-Turing (masse manquante, couverture), capture-recapture multi-sources (modèles log-linéaires, classes latentes), approche bayésienne. Dis comment tester l'indépendance, comment traiter un refus commun de répondre (une même censure sur toutes les sources) et ce que devient l'estimation si le nombre de familles n'est pas fermé.

### Bloc 2 — Données de départ à recommander (au plus 400 mots)

Plutôt que des résumés, quelles données brutes recommandes-tu, et pourquoi ? Candidates : (i) les trajectoires brutes de bancs publics conçus par d'autres (SHADE-Arena, ControlArena, MonitoringBench, SLEIGHT-Bench, Liars' Bench), utilisées comme **familles extérieures** ; (ii) les journaux de refus de questions passées ; (iii) les propositions brutes d'une course précédente. Pour chacune : indépendance réelle vis-à-vis du programme, étiquetage au niveau des familles, risque de recouvrement avec ce que les modèles ont déjà vu, coût de mise au format, usage possible comme source supplémentaire de capture-recapture. Décris chaque banc par ses propriétés de format, de licence, d'étiquetage et d'indépendance, sans en décrire les tâches ni les comportements ; trois bancs au plus. Si tu ne connais pas un banc, dis-le : n'invente ni contenu ni référence.

### Bloc 3 — Questions candidates pour le texte III (au plus 900 mots)

**Au plus cinq dans ta proposition.** Chaque question est formulée en termes de mesurer, valider, borner ou estimer. Pour chacune :

1. l'**avantage** qu'elle exploite ;
2. le **piège méthodologique** qui la tuerait ;
3. la **validation extérieure** qu'elle permet (familles conçues hors du programme, prédictions scellées confrontées à des mesures, revue extérieure), chiffrée : nombre de familles extérieures, taille ou seuil ; illustratif si hors des faits ;
4. le risque qu'elle soit jugée hors du périmètre méthodologique (faible, moyen, élevé ; illustratif), et l'élément de la question qui la borne à la mesure.

### Bloc 4 — Question annexe (au plus 700 mots)

**Décision prise par le directeur** (RAPPORTÉ) : les familles tenues à l'écart seront conçues par **plusieurs instances indépendantes**, de fournisseurs et de modèles différents (cinq sont prévues), chacune tenue à l'écart de la conception des défenses et scellée à part. Propose **comment l'organiser** ; ne propose aucun contenu de famille ; ta réponse ne doit rien anticiper de ce que concevront les instances :
- ce que chaque instance reçoit (même consigne ou consignes différentes) ;
- comment empêcher les fuites entre elles ;
- comment apparier leurs familles sans qu'un lecteur unique biaise l'appariement ;
- comment tester leur indépendance (corrélation des données d'entraînement entre fournisseurs) ;
- comment s'en servir comme sources multiples pour estimer les familles encore inconnues ;
- ce qu'on fait si une instance refuse.

Pour chaque point : options, avantage, inconvénient, recommandation et confiance. Ce qui n'est pas dans les pièces ou dans le contexte est marqué HYPOTHÈSE. »

## Insertion dans les consignes du tour

Correspondance avec les livrables du tour III.1 :

| Livrable du tour | Ce qu'il contient ici |
|---|---|
| (a) ce que la question suppose sans que ce soit établi | les hypothèses des blocs 1(b) à 1(d), une ligne chacune, avec son statut |
| (b) expériences décisives en duel H_A contre H_B | au moins deux duels portant sur des **estimateurs ou des définitions** (par exemple : Lincoln-Petersen contre bornes de Chao), avec métrique, seuil, contrôle négatif et issue qui falsifie chaque hypothèse |
| (c) mesure minimale de chaque instrument nommé | l'instrument est l'**estimateur du nombre de familles** et la **mesure d'universalité** ; la mesure minimale est leur couverture et leur biais sur des mondes simulés à vérité connue, contre une base à battre (comptage brut des familles observées) |
| (d) ancrage matériel | au plus 100 mots |

Ordre de la réponse : (a), (b), (c), puis les blocs 1 à 4, puis (d). Les plafonds des blocs sont des maximums, non des cibles ; le total respecte la limite de mots du tour. Si la place manque, garde dans l'ordre les blocs 1, 3, 4, 2.

Au tour III.3, la page de réponse à la question contient : définition retenue, estimateur retenu, au plus cinq questions candidates révisées, organisation recommandée en cinq lignes.

Si tu reçois cette question sans consignes de tour, suis le même ordre et les mêmes plafonds, au plus 3 500 mots en tout.
