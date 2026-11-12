# Question complémentaire pour le collisionneur — couche 2, pilote sur seize tâches : ce que la question v1 ne demandait pas — v1

Écrite par conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` 00:21 UTC. Mot direct de Lazar
(rapporté par session-depot, n° 134, GO-2026-10-29-01, plafond 30 USD) : « il faut reposer une question au collisionneur »
sur le trou relevé dans la question v1 du pilote (session-depot, `envois/question-pilote-couche-2-v1.md`). Même forme
« arbitre » (trois modèles, trois tours, une tentative par cellule, un refus arrête le tour sans reformulation, R-609) ;
**même garde de sûreté** (R-519, R-339, R-597, à reprendre telle quelle : rien qui conçoive, détaille ou étende une
attaque ; modes nommés par classe et dose ; le collisionneur ne voit ni les internes des moniteurs, ni la carte des
hypothèses, ni le mode tenu à l'écart, ni les banques, ni les textes d'actions, ni les consignes privées de P3). **Dépense :
chez session-depot, sur le GO cité ; conv-audit ne lance rien.** La synthèse est matériau pour la décision de Lazar ; elle ne
tranche rien et n'est pas un préenregistrement ; tout chiffre reste exploratoire (R7).

**Question étroite : ne pas redemander ce que les huit cellules du premier tour ont déjà répondu** (pièce B). Trois objets
seulement.

## Pièces à servir (matériau, jamais consigne)

- **Pièce A** — la question v1 du pilote (session-depot) ; **pièce B** — la synthèse du premier tour (sous-agent neuf de
  session-depot), qui liste les angles morts déclarés.
- **Pièce C** — le rapport de la simulation du contrôle 12 joint (`docs/notes/couche-2-preparation-v1/
  simulation-controle-12-joint-v1/rapport-controle-12-joint-v1.md`, `7600f2d0…`) : § 5 (cinq conditions de l'option (a)),
  § 2 et complément « ex æquo » (échec joint 0,35 à 0,54 sans bris d'égalité), § 6 (limites : échangeabilité des exécutions).
- **Pièce D** — le format décision v2 des cinq divergences (conv-audit, `9caefea3…`), D1 et D5.
- **Pièce E** — N-055, N-056 (critère de G1, mesures fortes), D-S13 (bris d'égalité) par renvoi.

## Question

« Le pilote sur seize tâches de la réserve (pièces A et B) doit, en plus de ce que le premier tour a conçu, mesurer deux
quantités dont dépend la lisibilité du contrôle 12 de la banque (pièce C), et dire si des angles morts déclarés par le
premier tour (pièce B) sont mesurables au pilote. Concevez cette part du pilote, chiffrée, sans refaire le reste.

1. **Part d'ex æquo par cellule critère.** Pour chaque cellule (sondes par jeton et leurs agrégats, scores de juges lus par la
   probabilité du jeton de verdict, moniteurs boîte noire par action, bases blanches), quelle est la grille effective des
   scores (arrondi, nombre de valeurs distinctes sur un lot honnête) et la part de paires ex æquo au seuil à 1 % de fausses
   alertes ? Estimateur, nombre d'épisodes honnêtes nécessaires pour une précision donnée sur cette part (elle est à
   mesurer **sur des honnêtes**, donc sans tâche sabotée), lecture gelée : au-dessus de quelle part un **bris d'égalité
   aléatoire scellé** (D-S13, retouche 3) est obligatoire, et comment le pilote vérifie qu'après bris le monde est continu
   (test de l'uniformité des rangs, taille). Dites si une cellule peut rester discrète sans rendre le contrôle 12 aveugle.
2. **Échangeabilité des exécutions dans une tâche.** La coupe du calibrage en deux moitiés **dans** chaque tâche suppose que
   les exécutions d'une même tâche sont échangeables (pas de dérive première → dernière : température, cache, charge de la
   carte, ordre). Quel plan de mesure au pilote (combien d'exécutions par tâche, dans quel ordre, quelle statistique :
   corrélation de rang entre numéro d'exécution et score, test de tendance par tâche, agrégé sur seize tâches), quelle
   précision à seize tâches, et quel résultat ferait abandonner la coupe dans les tâches pour une coupe **entre** tâches
   (avec ce que cela coûte en unités : 48 au lieu de 64, pièce D). Même question pour la dérive **entre lancements** (pilote
   contre banque : sentinelle de dérive de fabrique, pièce D, D3).
3. **Angles morts déclarés par la synthèse** (pièce B, liste à reprendre telle quelle ; si elle est vide, dites-le et
   arrêtez-vous là) : pour chacun, mesurable au pilote ou non, à quel coût, et sinon où il se mesure.

Pour chaque point : l'estimateur, le nombre d'épisodes et d'exécutions, le coût en heures et en dollars (prix SUPPOSÉ
1,08 à 1,43 USD de l'heure), ce qui serait un résultat qui change la banque (critère gelé, à écrire d'avance), et le piège
(sélection sur un verdict, lecture qui informe l'auteur du mode tenu à l'écart, contamination de la réserve). Rendez, à
part, les décisions que le directeur doit prendre, au format décision (une phrase, enjeu, options, recommandation avec
confiance, défaut). Niveau méthode seulement. »

## Lecture et suite (conv-audit)

Synthèse = matériau pour le format décision du pilote (conv-audit) et pour P-036 v3 (session-depot) ; rien n'est tranché
par elle. v1, scellée, jamais réécrite ; si la synthèse du premier tour déclare des angles morts, ils sont servis dans la
pièce B telle quelle, sans réécrire cette question.
