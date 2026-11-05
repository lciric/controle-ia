# BA-002 — contrôle de pureté des familles d'Argon : bilan en comptes et en classes — v1

session-depot, 30 octobre 2026, 15:44 UTC. Décision de Lazar (R-826) :
- (a) recentrer par construction toute famille qui déplace la moyenne hors de sa classe ;
- (b) la reclasser si le recentrage détruit ce qui la définit.

**Exécution.** Un exécutant tenu à l'écart (Opus, puis Sonnet 5.5, neufs ; aucun moniteur conçu) a travaillé sur processeur seulement. Paramètres, scripts et résultats sont en quarantaine (`/root/ideation-v1/bras-attaque-ba002/purete-argon-v1/`, avec leurs empreintes ; le résultat qui fait foi est `resultats-purete-v2-consolide.json`). Ce bilan ne contient ni paramètre, ni nom de famille, ni formule.

**Tolérance**, déclarée en tête du script avant toute mesure. L'unité est l'écart-type de la loi de référence.
- La moyenne est conforme si l'écart, intervalle à 95 % compris, reste dans 0,01 de cette unité.
- Même tolérance pour la variance, en unité au carré.
- Une propriété qui définit la famille est jugée présente si son intervalle exclut zéro et si l'effet vaut au moins 0,01 (relatif pour les événements rares).

## Résultat (28 familles)

| Décision | Familles |
|---|---|
| Pures | 7 |
| Recentrées (contrôle refait, la propriété qui la définit survit, mesurée) | 15 |
| Reclassées | 5 (3 vers C1, simple décalage de moyenne ; 1 vers C3 ; 1 vers C-autre) |
| Non exécutables (loi identique à la référence) | 1 |

| Classe | Avant | Après |
|---|---|---|
| C1 déplacement de moyenne | 3 | 6 |
| C2 mélange | 2 | 2 |
| C3 changement de variance | 4 | 3 |
| C-autre | 19 | 16 (+ 1 sans classe) |

## Réserves de l'exécutant

1. **Remesure après coup.** Une famille à dépendance temporelle longue, mal résolue au premier passage, a été remesurée une fois sur un échantillon 4 fois plus grand, avec un flux de graine neuf. La réplique sous une autre graine la donnait déjà « recentrée ».
2. **Stabilité.** La réplique sous une autre graine donne les mêmes décisions. Les 10 variantes de conventions testées (9 familles avaient un paramètre manquant) sont stables.
3. **Jugement sur deux cas.** La non-stationnarité de la moyenne et une combinaison ont été lues comme des classes où la moyenne peut bouger. Sous la lecture inverse : 5 pures, 17 recentrées, 5 reclassées, 1 non exécutable.
4. **Deux reclassements de classe** (vers C3 et vers C-autre) reposent sur la nature de la propriété mesurée. Ils sont séparés dans la sortie et Lazar peut les écarter.
5. **Familles sans effet** : celles qui n'ont aucun effet en loi ne l'ont que dans le cadre déclaré (centré, blanchi, tirages indépendants).
6. **Simulation partielle** : elle porte sur un bloc actif plus des axes témoins, pas sur les 4 096 dimensions. Aucun modèle de langage n'est en jeu.
7. **Écarts avec le premier passage** : 3 recentrées au lieu de reclassées, 2 reclassées de plus, 1 non exécutable. Les gardes, éprouvées sur un cas sain et 5 artefacts, sont devenues bloquantes.
