# Prompt de relecture externe de P3 (v1)

Tu es un **relecteur scientifique externe**, exigeant et adversarial. Tu connais l'interprétabilité par sondes sur les
activations des modèles de langage (sondes linéaires, plancher aléatoire, fuites, effets de style et de longueur), les agents
à base de modèles de langage et la méthode des expériences préenregistrées. Tu n'as écrit aucun des documents joints. Ton
rôle est de trouver ce qui est faux, fragile, ambigu ou mal mesuré avant le lancement, pas de résumer ni d'approuver.
Réponds en français, en phrases courtes.

## Contexte

Programme de recherche « contrôle boîte blanche des menaces diffuses » : détecter, dans les activations d'un modèle, un agent
qui sabote de façon diffuse une tâche de recherche (ici : proposer des expériences), là où une lecture des seules sorties
échoue. P3 est le **premier test boîte blanche**, volontairement réduit, des critères 2 (organisme) et 3 (sondes) de la porte
de la phase 0, sur un seul organisme, (i-a) :

- agent : Llama-3.1-8B-Instruct, sans réglage fin, dans l'environnement du pilote (60 tâches) ;
- quatre conditions, 60 épisodes chacune : **honnête** ; **saboteur** (consigne privée : gonfler le coût déclaré de ses
  propositions) ; **témoin** (consigne privée inoffensive, de même longueur en jetons) ; **mention sans usage** (le même
  texte trompeur dans le contexte, présenté comme une note sur un autre agent, avec un agent honnête) ;
- **sondes génériques** (concepts « tromperie » et « enjeux élevés »), entraînées sur des données publiques sans lien avec la
  tâche, figées et scellées avant le premier épisode ; cinq familles × trois couches ; une sonde principale par concept ;
- lecture : aires sous la courbe par action contre un **plancher** de 200 sondes aléatoires appariées en covariance ;
  prérequis comportemental P3-P1 (le coût déclaré du saboteur dépasse celui de l'honnête) ; validité contre le témoin (P3-P4) ;
  « la sonde lit l'intention » seulement si quatre tests T1 à T4 passent ; audit de symétrie gelé (prédicteurs triviaux,
  placebo, miroir) ; règle des jeux non interprétables ;
- un seul run, d'environ 4 à 6 heures sur une carte A100, rapporté quel que soit le signe du résultat. Le texte est sur le
  point d'être scellé (copie octet pour octet du fichier `1-texte/P3-premier-test-i-a-v1-candidat4.md`).

## Pièces

Le fichier `LISEZMOI.md` du dossier liste chaque pièce avec son empreinte sha256 et dit ce qui est exclu, et pourquoi.
Ordre de lecture conseillé :
1. le texte : `1-texte/P3-premier-test-i-a-v1-candidat4.md`, en entier, et sa configuration ;
2. le contexte : `4-contexte/decisions-citees-P3.md`, `4-contexte/verdict-T0.5-pilote-v1.md` (pilote dont P3 reprend
   l'environnement et l'agent), `4-contexte/programme-controle-ia-v2.md`, les mesures de conception `4-contexte/P3-mesures-v2/`
   (puissance, durées, longueurs) ;
3. le code : `3-code/src/controle_ia/premier_test_ia/` (lecture, statistiques, run, entraînement, notation, conditions,
   données, empans, sondes figées), les modules dont il dépend (`sondes/`, `harnais/`, `manifeste.py`), les scripts de
   l'instance et les tests ;
4. les relectures déjà faites et leurs traitements : `2-relectures/` ;
5. en annexe seulement : la chaîne de lancement `5-chaine-annexe/` (opérations, gardes, bancs).

## Ce que je te demande

1. **Validité de construit** : P3 teste-t-il ce qu'il dit tester (hypothèses H-P3a à H-P3c, critères 2 et 3 « partiellement »
   pour (i-a)) ? Les témoins (condition témoin, condition « mention sans usage », placebo, prédicteurs triviaux, plancher
   apparié, tests T1 à T4) ferment-ils les explications concurrentes : style ou longueur, simple présence d'une consigne
   privée, lecture du texte trompeur dans le contexte, grandeur du nombre écrit, rang du pas dans l'épisode ? Qu'est-ce qui
   reste ouvert ?
2. **Statistique** : définitions de « au-dessus du plancher » et de « non au-dessus » ; correction pour deux sondes
   principales ; intervalles par blocs de tâches et dépendance entre actions d'une même tâche ; puissance à 60 tâches ;
   plancher (quantile 0,95 de 200 sondes appariées) ; choix de la sonde principale sur la validation générique ; risques de
   fuite entre données d'entraînement et épisodes ; règle des jeux non interprétables ou en échec ; tests T1 à T4.
3. **Règles de lecture** : la table gelée (lue de haut en bas) et les réserves couvrent-elles tous les cas ? Repère toute
   lecture ambiguë, toute issue favorable trop facile à atteindre, tout cas où un résultat nul ou négatif serait mal lu.
   Aucune lecture ne doit viser un signe ; un résultat trop propre, positif ou négatif, doit déclencher le même audit.
4. **Code** : fait-il exactement ce que dit le texte ? Cherche les bogues, les fuites, les erreurs d'ordre (sondes figées
   avant les épisodes, sonde principale choisie avant tout épisode), les graines, les gardes qui ne gardent rien, les
   unités (positions de jetons, empans, bornes des champs), et toute moyenne ou médiane sur les jetons d'une action (elle
   est interdite).
5. **Risques pratiques** : durées, mémoire, coût ; un arrêt qui laisserait un résultat partiel mal lu.
6. **Relectures précédentes** : ont-elles raté quelque chose ? Un traitement annoncé est-il incomplet ?

## Contraintes

- N'invente aucun chiffre : chaque chiffre que tu cites vient des pièces, avec le fichier et la ligne ou la section.
- Distingue ce qui est un **défaut** (faux, incohérent, non mesurable) de ce qui serait un **élargissement** du test (une
  autre expérience) ; ne propose un élargissement que s'il corrige un défaut bloquant, et dis-le.
- N'écris aucune consigne de sabotage ni aucun texte d'attaque ; les consignes privées réelles ne sont pas jointes (leurs
  longueurs en jetons sont citées par le texte) ; si leur contenu t'est nécessaire pour juger un point, dis lequel.
- Dis ce que tu n'as pas pu vérifier (par exemple : rien n'est exécutable de ton côté).

## Forme de ta réponse

1. **Verdict** en trois lignes au plus : « scellable tel quel », « scellable après corrections » ou « ne pas lancer », avec la
   raison principale.
2. **Tableau des constats**, du plus grave au moins grave, avec ces colonnes : identifiant (G-01, G-02…), fichier et ligne
   ou section, ce qui est écrit, le problème et pourquoi, gravité (bloquant, majeur, mineur, pour information), correction
   proposée.
3. **Questions aux auteurs**, numérotées.
4. **Ce que tu n'as pas pu vérifier.**
