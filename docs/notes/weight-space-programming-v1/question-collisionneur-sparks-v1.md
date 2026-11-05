## La question

Un billet du 2 novembre 2026 (pièce « billet », texte intégral ; pièce « lecture factuelle » : ce qu'il montre et ne montre pas, d'après ses journaux publics) affirme qu'un modèle de langue de frontière, sans entraînement ni gradient, **lit et écrit des poids de réseaux de neurones** : il nomme la tâche de petits réseaux à partir de leurs poids, répare une politique en éditant 3,5 % de ses poids, écrit des réseaux de jeu depuis zéro, et retire d'un modèle de langue de 0,8 milliard de paramètres une direction qui causait des boucles (0,016 % des poids). Sa seule expérience sur un trait d'alignement (deux copies d'un petit modèle, l'une honnête, l'autre sycophante) **échoue sur les poids seuls** et ne réussit qu'avec un outil qui rend les motifs d'attention, sur un choix forcé entre deux modèles, sans paire témoin.

**Comment intégrer ces découvertes, et ce qu'elles ne montrent pas, dans nos deux programmes** (pièce « nos résultats ») : (1) un **organisme d'idéation** où des agents de plusieurs fournisseurs proposent des lois falsifiables jugées par un juge statistique figé, éprouvé contre des tricheurs scriptés et des attaquants modèles de langue ; (2) un **programme de contrôle de l'intelligence artificielle** qui demande si des moniteurs qui lisent l'état interne d'un agent ajoutent un pouvoir de détection au-delà de la surveillance boîte noire, et à quel point les moniteurs sont corruptibles ; et nos deux travaux publics sur la sycophancie (une loi d'attraction vers un point fixe sous pression dosée ; une direction lisible qui suit la sycophancie sans la causer) ?

## Ce qu'on attend des proposeurs

Des **fiches** au gabarit du noyau : des **questions falsifiables** d'abord, puis des **approches**. Chacune dit : l'hypothèse et l'effet prédit avec son signe ; ce qu'elle change dans l'un de nos programmes (instrument, témoin, menace, famille de tâches, mesure de validité) ; **la première expérience faisable en quelques jours** sur une carte graphique et quelques dizaines de dollars d'appels (modèles à poids ouverts de 0,1 à 8 milliards de paramètres, adaptateurs de rang faible, nos organismes de sabotage ou de sycophancie, notre organisme d'idéation public), avec son **nul** (par exemple des paires de modèles identiques à graines différentes), son **témoin négatif**, l'aveuglement des étiquettes et un taux de fausses alertes fixé d'avance ; le **seuil chiffré qui ferait abandonner l'idée** ; et pourquoi ce ne serait pas déjà fait (voir la liste suivante).

Sont particulièrement bienvenues :
1. des épreuves qui mettent les affirmations du billet **sous nul** (paires nulles, lecteurs multiples et de familles différentes, plusieurs essais, choix du meilleur essai déclaré) ;
2. des mesures de **validité de construit** : si l'on retire de façon chirurgicale la direction ou le composant qui porte un comportement, la mesure de ce comportement change-t-elle comme prévu, ou seulement son échelle, ou rien ;
3. des **lectures de deltas** (adaptateur de rang faible d'un organisme de sabotage contre son jumeau honnête, à dose réglable) comparées aux sondes d'activation et à la boîte noire, à taux de fausses alertes égal ;
4. des **familles de tâches inédites** pour l'organisme d'idéation (par exemple des petits réseaux à propriété plantée et à oracle exécutable) ;
5. des **classes de menace** contre un juge ou un moniteur quand l'adversaire peut éditer des poids, décrites par la couverture qu'un défenseur peut certifier et le prix qu'il impose.

## Ce qui est déjà pris (moisson non opposable du 4 novembre ; ne pas le reproposer comme neuf)

- Lire une propriété d'un réseau dans ses poids sans l'exécuter (apprentissage dans l'espace des poids, réseaux fonctionnels, zoos de modèles), et détecter une porte dérobée dans des poids sans déclencheur, y compris dans des adaptateurs de rang faible et avec un modèle de langue affiné qui lit des poids bruts (« Weight Oracles », 2610.07334).
- Un modèle de langue qui lit des activations ou des deltas de poids et nomme un trait affiné (LatentQA, oracles d'activation, « Diff Interpretation Tuning ») ; lire un affinage étroit par différence d'activations entre deux modèles (2510.13900) : l'expérience « sycophante » du billet en est un cas.
- Supprimer un comportement en soustrayant une direction des poids (orthogonalisation du refus, 2406.11717 ; une direction de sycophancie dans l'espace des poids, 2511.05408 ; vecteurs de tâche ; édition de connaissances) ; et les dégâts connus de l'édition.
- Agents d'audit munis d'outils d'interprétabilité et bancs d'audit sur modèles à comportement caché.
- L'adversaire : portes dérobées indétectables en théorie, activations obfusquées, évasion apprise des moniteurs latents, agents dormants.

Zones peu couvertes (à durcir, non opposables) : lire un trait d'alignement dans les **poids seuls** d'un modèle de langue ; interpréter directement des **deltas d'adaptateurs** par un modèle de langue non entraîné pour cela ; un adversaire qui vise un **lecteur de poids par modèle de langue** ; mesurer ce que casse le retrait d'une direction ; le choix du meilleur essai et le lecteur unique.

## Règles d'intégrité

- **Niveau méthode.** Aucune fiche ne décrit comment éditer des poids, écrire des données ou conduire un agent pour tromper un moniteur, un juge ou une évaluation, ni un procédé pour masquer un comportement ; une menace se décrit par sa classe, l'accès qu'elle suppose et la défense mesurable, jamais par un mode d'emploi. Une fiche qui en contient est écartée sans être lue.
- Tout chiffre repris cite sa pièce et sa section ; tout chiffre dérivé est marqué « calcul », tout chiffre supposé « supposé ».
- **Aucun identifiant inventé** : un travail se cite par l'identifiant donné dans une pièce, sinon par « travail non identifié ».
- Pas de web, pas d'exécution de code ; la nouveauté n'est pas cherchée par les proposeurs.
