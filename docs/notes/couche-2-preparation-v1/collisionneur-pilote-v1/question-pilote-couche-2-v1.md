# Question pour le collisionneur — couche 2 : concevoir le pilote sur seize tâches de la réserve — v1

Écrite par session-depot (instance 2, servie par Fable 5.1), 28 octobre 2026, relevé `date -u` 23:35 UTC, sur le mot direct
de Lazar (« lance le collisionneur sur le pilote aussi », après « go rejeu du juge, (a) go »). Même forme « arbitre » que les
questions précédentes : trois modèles, trois tours (conception, équipe rouge croisée, riposte), une tentative par
cellule, un refus arrête le tour (jamais reformulé, R-609). La synthèse est matériau pour la décision de Lazar ; elle ne
tranche rien et n'est pas un préenregistrement ; tout chiffre reste exploratoire et non opposable (R7).

**Garde de sûreté (R-519, R-339, R-597, à reprendre telle quelle dans la consigne)** : rien qui conçoive, détaille ou
étende une attaque. Les modes de sabotage sont nommés par classe et dose, jamais par exemple ni consigne. Le collisionneur
**ne voit pas** : les internes des moniteurs, la carte des hypothèses, le mode tenu à l'écart, les banques, les textes
d'actions, les consignes privées de P3. Il voit les pièces ci-dessous, toutes au niveau méthode.

## Pièces à servir (matériau, jamais consigne)

- **Pièce A** — le format décision sur les cinq divergences (conv-audit, `857b501c…`), écrit après la synthèse du
  collisionneur ; **pièce B** — cette synthèse (`37f85388…`, vérifications refaites à graine neuve).
- **Pièce C** — le dimensionnement de la couche 2 écrit en aveugle (conv-audit, `95c5c396…`) : effet de tâche, pilote de
  mesure, rythmes mesurés du pilote de T0.5 et de P3.
- **Pièce D** — P-036 v2 (session-depot) et la décision du directeur du 28 octobre (ordre retenu : rejeu du juge, puis
  pilote sur seize tâches de la réserve, puis préenregistrement de G1 et banque).
- **Pièce E** — décisions de `main` : N-055 (D-S1 à D-S12, dont D-S13 à D-S15 par renvoi), N-056 (critère de G1, bases
  (ii) et (iii), mesures fortes), N-053 (invariant : aucun score de moniteur ou de juge dans la sélection d'un agent ;
  lecteur de la quarantaine), N-054 (séparation des rôles : qui écrit le mode tenu à l'écart ; bras génériques et
  spécialisés), P-015 (conditions témoin instruit et mention, dose, recherche de dose, P4-instrument).
- **Pièce F** — fait mesuré : au pilote de T0.5, 180 notations par juge, **54 (8B) et 50 (3B) notes complètes**, 60 tronquées
  chez le 8B ; rythmes 58,2 s et 27,5 s par notation ; un rejeu des juges sur ces 180 textes (lecture par la probabilité du
  jeton de verdict) est décidé (GO-2026-10-28-16, ≤ 4 USD) et précède le pilote.

## Question

« Un programme de contrôle boîte blanche des menaces diffuses prépare la **couche 2** : une banque d'épisodes à deux modes
de sabotage (un mode connu ; un mode tenu à l'écart écrit par une instance qui n'a conçu aucun moniteur), sur un banc de
96 tâches (64 d'épreuve, 32 de réserve pour le développement de l'organisme), pour une porte G1 au critère gelé
(pièce E). Le directeur a retenu l'ordre : (0) rejeu des juges sur les 180 textes du pilote existant ; **(1) un pilote sur
seize tâches de la réserve** (36 à 125 USD selon la taille) ; (2) préenregistrement scellé de G1 ; (3) la banque (300 à
1 400 USD). Les deux plans (pièces A à C) reposent sur des paramètres **supposés, jamais mesurés** : effet de consigne et
concordance entre moniteurs, hétérogénéité entre tâches, écart « blanc contre blanc », dose diffuse avec dommage,
obéissance et étiquetage, scores finis par cellule, strate d'horizon, rythmes. Concevez ce pilote :

1. **Ce qu'il mesure, à quelle précision.** Pour chaque paramètre supposé : l'estimateur, le nombre d'épisodes et
   d'exécutions pour une erreur relative donnée, ce qu'on apprend à seize tâches et ce qu'on n'apprend pas. La pièce C dit
   qu'un pilote à huit ou seize tâches mesure l'effet de consigne à ≈ 53 % d'erreur relative : refaites le calcul ; quelle
   taille le ramènerait sous 25 % ? Que vaut-il mieux mesurer d'abord si l'on ne peut pas tout mesurer ?
2. **Le plan d'épisodes, chiffré.** Tâches (seize de la réserve : lesquelles, par quel tirage scellé) ; conditions (honnête,
   saboteur du mode connu, témoin instruit, mention ; **jamais** le mode tenu à l'écart) ; exécutions par tâche ; doses
   (recherche de dose contre tous les moniteurs boîte noire par action, pièce A, D4) ; captures (activations pour les
   sondes figées de P3, scores par jeton, textes) ; juges (8B et 3B, lecture par la probabilité du jeton de verdict) ;
   jumeaux honnêtes. Épisodes, heures de carte, dollars (prix SUPPOSÉ 1,08 à 1,43 USD de l'heure), dans 36 à 125 USD ; et
   une **version minimale sous 40 USD**, avec ce qu'elle perd.
3. **La non-contamination.** Comment le pilote et ce qu'on y lit n'entament ni la réserve (le développement de l'organisme
   en a besoin), ni l'épreuve de G1 (64 tâches), ni le mode tenu à l'écart ; ce qui doit être scellé avant (critères de
   lecture, ce qui sera lu, ce qui ne le sera pas) ; les épisodes du pilote peuvent-ils resservir — calibrage propre au
   développement (D-S15), recherche de dose — sans sélection interdite par l'invariant de N-053 ?
4. **Règles d'arrêt et de décision.** Quel résultat du pilote changerait le nombre d'exécutions, la taille du calibrage
   (9 600 avec seuil 40 contre 12 800), la dose unique en épreuve, l'ordre des lancements ; quel résultat ferait abandonner
   la banque telle que dimensionnée (par exemple scores non finis, écart blanc contre blanc sous 5 points, régime
   « diffus » introuvable) ; à écrire d'avance, comme critères gelés.
5. **Ce qui tuerait le pilote**, et la garde pour chacun : artefact de source (le seul juge 8B code le « diffus »), effet de
   consigne non mesurable à seize tâches, dérive de la pile logicielle entre le pilote et la banque, sélection sur un
   verdict, lecture qui informe l'auteur du mode tenu à l'écart.

Attaquez aussi l'ordre lui-même : un pilote saboté vaut-il mieux qu'un calibrage honnête de développement direct (option
(b) de la pièce A, D5), ou qu'un pilote sur les 180 épisodes existants rejoués avec les sondes figées de P3 ? Rendez enfin, à
part, la **liste des décisions que le directeur doit prendre avant le pilote**, au format décision (une phrase, enjeu,
options, recommandation avec confiance, défaut). Niveau méthode seulement. »
