## Périmètre (à respecter sans exception)

Le périmètre est statistique et méthodologique : définitions, estimateurs, plans de simulation, validation. Aucune famille, aucun comportement d'agent et aucun moyen ne sont décrits, même à titre d'illustration ; la réponse qui le ferait est écartée. Ce tour porte **seulement sur la mesure statistique**. Le régime d'information de l'évaluation, le choix de bancs ou de jeux de données à recommander, la rédaction de questions de recherche candidates et l'organisation de ceux qui conçoivent les familles en sont exclus : ne les traite pas.

## Contexte (autoportant : il suffit à répondre)

Un programme de recherche défensive évalue des défenses de systèmes d'intelligence artificielle (sondes sur les activations internes, moniteurs qui ne lisent que le texte) sur des **familles** : classes d'éléments d'évaluation simulés, définies par un schéma de construction, jamais décrites ici. Dans toute la réponse, une famille est une étiquette abstraite, dotée seulement de probabilités (capture par chaque source, échec de la défense) et d'une corrélation entre familles donnée par un paramètre numérique ; aucun attribut de contenu. Certaines familles sont **tenues à l'écart** : ni les concepteurs de la défense ni la défense ne les voient avant la mesure finale. L'objectif du programme est l'universalité mesurée sur des familles inédites (VÉRIFIÉ, fait 1). Ta réponse sert de matériau à un préenregistrement et ne tranche rien.

Chaque fait porte un statut : VÉRIFIÉ, RAPPORTÉ, OBSERVÉ-NON-AUDITÉ ou HYPOTHÈSE ; tu ne le changes pas. Tout chiffre qui ne vient pas du contexte ou des faits est marqué « illustratif » ; une référence que tu ne peux pas attribuer (auteurs, année, titre) porte « référence à vérifier ».

**Données de départ (RAPPORTÉ, fait 17 : décompte d'un lecteur unique, appariement non contre-lu).** Trois sources ont énuméré des familles, ramenées à des familles canoniques : 22, 23 et 27. Familles observées : 37, dont 14 communes aux trois. Recaptures par paire (familles vues par les deux sources de la paire, celles vues par les trois comprises) : 16, 16 et 17 ; l'affectation de ces trois nombres aux paires de sources n'est pas dans les faits (la déviance rapportée peut contraindre cette affectation ; si tu l'en déduis, dis-le). Fréquences de capture : 16 familles vues par une seule source, 7 par deux, 14 par les trois. L'indépendance des trois sources est rejetée : déviance 12,9 pour 3 degrés de liberté. La cohérence arithmétique de ces comptes est vérifiée (fait 18), pas leur décompte.

## Question

« Conçois la **mesure statistique** qui permettrait d'affirmer, devant un tiers, qu'une défense est universelle sur un ensemble de familles, et de confronter cette affirmation à des mesures extérieures. Réponds par quatre blocs.

### Bloc 1 — Définition opérationnelle de l'universalité (au plus 350 mots)

Options à comparer : pire cas sur une classe de familles déclarée d'avance par son schéma de construction, sans en décrire le contenu ; écart de performance entre familles vues et familles tenues à l'écart ; quantile ou proportion de familles où la défense passe un seuil ; autre. Pour chacune : l'énoncé exact qu'elle autorise, sous la forme **quantificateur, classe, statistique** ; ce qu'il faut déclarer avant la mesure ; ce qu'elle n'autorise pas ; comment un tiers la recalcule. Dis ce qui sépare « universelle sur la classe déclarée » de « robuste à l'inconnu », et quelle option tu retiens.

### Bloc 2 — Nombre de familles nécessaire, par simulation (au plus 350 mots)

Énoncé cible, par exemple : avec confiance 1 − α, la part de la classe où la défense échoue est inférieure à ε. Donne la règle de calcul : modèle génératif de la population de familles ; hétérogénéité et dépendance entre familles proches ; variance à deux niveaux (entre familles, et entre éléments d'une famille) ; règle d'arrêt séquentielle ; analyses de sensibilité. La borne à zéro échec du fait 9 suppose des familles tirées indépendamment ; or les familles sont **découvertes**, non tirées. Dis ce que devient la garantie sous un mécanisme de découverte, ce que la simulation peut démontrer et ce qu'elle suppose.

### Bloc 3 — Familles encore inconnues, sources multiples dépendantes (au plus 500 mots)

À partir des données de départ :
- calcule au moins un estimateur de borne inférieure fondé sur les fréquences de capture et un estimateur de couverture ; donne chaque formule et chaque résultat ;
- dis quels modèles log-linéaires sont identifiables avec sept cellules observées, leurs degrés de liberté, et ce que chacun suppose de l'interaction d'ordre trois ;
- dis dans quel sens la dépendance positive entre sources, l'hétérogénéité de capture entre familles et l'erreur d'appariement d'un lecteur unique (fusions à tort, scissions à tort) déplacent l'estimation ;
- dis quel estimateur employer quand l'indépendance est rejetée (bornes de Chao, couverture de Good-Turing, modèles log-linéaires avec interactions, classes latentes, approche bayésienne, autre), et ce que devient l'estimation si une même partie de la population de familles est inaccessible aux trois sources (censure commune) ou si le nombre de familles n'est pas fermé.

Tout calcul qui dépend de l'affectation des recaptures aux paires le dit et donne son étendue sur les affectations possibles.

### Bloc 4 — Validation extérieure chiffrée (au plus 250 mots)

Pour chacune des trois mesures (définition, nombre nécessaire, familles inconnues), propose une confrontation à des familles **conçues hors du programme**, sans nommer, choisir ni décrire de source ou de banc : la source extérieure est décrite seulement par ses propriétés statistiques (taille, indépendance supposée vis-à-vis des trois sources, probabilité de capture). Chaque confrontation porte une **prédiction scellée avant** la mesure : nombre de familles extérieures, statistique comparée, seuil, et issue qui falsifie la prédiction. Par exemple, pour le bloc 3 : la part des familles d'une source extérieure nouvelle qui tomberait hors des 37 observées. Les chiffres hors des faits sont illustratifs. »

## Insertion dans les consignes du tour

| Livrable du tour | Ce qu'il contient ici |
|---|---|
| III.1 (a) ce que la question suppose sans que ce soit établi | les hypothèses des blocs 1 à 3, une ligne chacune, avec son statut |
| III.1 (b) expériences décisives en duel H_A contre H_B | **au moins deux duels d'estimateurs** (ou de définitions), par exemple H_A : sous dépendance positive, la couverture de l'intervalle sous indépendance reste au-dessus du seuil ; H_B : elle tombe sous le seuil alors que la borne de Chao l'atteint ; chacun avec métrique, seuil, contrôle négatif et issue qui falsifie chacune des deux hypothèses |
| III.1 (c) mesure minimale de chaque instrument nommé | les instruments sont l'**estimateur des familles inconnues** et la **mesure d'universalité** ; leur mesure minimale est un **plan de simulation à vérité connue** (à la place des taux de détection et de fausses alertes) : mondes simulés où le nombre de familles est connu ; facteurs variés, au moins la dépendance positive entre sources et l'hétérogénéité de capture ; mesures : couverture des intervalles et biais de chaque estimateur ; **base à battre : le comptage brut des familles observées** ; au moins un contrôle négatif. Ici, les « cas honnêtes appariés » de la consigne sont les mondes à vérité connue |
| III.1 (d) ancrage matériel | au plus 60 mots ; calcul sur processeur, chiffres illustratifs |
| III.2 critique croisée | les lois de capture, de dépendance ou d'hétérogénéité sous lesquelles chaque estimateur, chaque règle de calcul et chaque validation perd sa puissance ou devient non jugeable |
| III.3 page de réponse | ces quatre éléments : **définition retenue** (quantificateur, classe, statistique) ; **estimateur retenu**, avec son résultat et son intervalle sur les données de départ ; **nombre de familles nécessaire et sa règle de calcul** ; **validation extérieure, en cinq lignes** ; puis en une ligne l'expérience à faire en premier |

Ordre de la réponse au tour III.1 : (a), (b), (c), puis les blocs 1 à 4, puis (d). **Plafond, à chaque tour : au plus 2 500 mots**, sous la limite du tour. Les plafonds des blocs sont des maximums, non des cibles ; si la place manque, raccourcis chaque bloc plutôt que d'en retirer un.

Si tu reçois cette question sans consignes de tour, suis le même ordre, au plus 2 500 mots.
