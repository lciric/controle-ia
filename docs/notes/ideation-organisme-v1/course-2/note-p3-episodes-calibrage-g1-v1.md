# Les 240 épisodes de P3 et le calibrage ou l'épreuve de G1 — note v1

Session-depot (sous-agent de la lignée), 30 octobre 2026. Elle répond à la réserve de conv-audit (n° 224, point 4) : si les 240 épisodes de P3 appartiennent au calibrage ou à l'épreuve de G1, Q5 de la course 2 (signal à 8 milliards sur les vecteurs existants) et la piste A de la question v1 deviennent circulaires sur eux.
Sources lues sur `main` seulement. Non lus : `prereg/P3-consignes-v1.md`, `donnees/`, `diag/*/traces`, et les branches `donnees/*`, `quarantaine/*` et `canal/*`. Les empreintes sont tronquées à 8 caractères.

## Réponse

- **Les épisodes : indéterminé.** Aucun texte de `main` ne les verse au calibrage ni à l'épreuve de G1, et aucun ne les en exclut.
- **Les tâches : oui.** Les 60 tâches sur lesquelles les 240 épisodes ont été produits sont désignées comme tâches d'épreuve, et leur réemploi dans l'épreuve de G1 est prévu, à déclarer.

Pour Q5 et la piste A, la circularité se joue au niveau de la tâche : elle est donc **réelle**, même si les épisodes eux-mêmes ne sont jamais réutilisés.

## Établi (cité)

1. **P3 tourne sur les 60 tâches du pilote de T0.5.**
   - `prereg/P3-premier-test-i-a-v1.md` (`d975e981`) l. 40 et 43 : tâches `287e8348…`, chemin `donnees/t05-pilote-v1/taches-pilote-60-v1.json`.
   - Même fichier, l. 318-320 : « quatre conditions × 60 tâches × 1 épisode = 240 épisodes ».
2. **Ces 60 tâches sont les 60 premières tâches d'évaluation de la banque de T0.5**, recopiées à l'identique de `taches-evaluation.json` (`76cdeace…`). Source : `registres/decisions.md` (`f855d5ac`) l. 280, R-143. R-143 a ensuite été retirée (l. 282, R-145) pour une autre raison, la lecture de R8 ; le fichier de tâches est resté celui de P3.
3. **P3 ne sert à aucune lecture des préenregistrements de G0 qu'il cite** : `prereg/P3-premier-test-i-a-v1.md` l. 23-24 (« Les épisodes de P3 ne servent à aucune lecture de ces deux préenregistrements », à propos de T0.6 et T0.7 pour G0). Rien n'y est dit de G1.
4. **Le réemploi des 60 tâches dans l'épreuve de G1 est prévu.** `docs/decisions/proposition-P-036-couche-2-preparation-v1.md` (`a8c41681`) l. 253-254 : « Les 60 tâches du pilote ont servi à l'épreuve de P3 (verdict lu) : leur réemploi dans l'épreuve de G1 est à déclarer au préenregistrement. »
5. **Les 60 tâches sont traitées comme tâches d'épreuve à préserver.**
   - `docs/notes/couche-2-preparation-v1/collisionneur-pilote-v1/synthese-collisionneur-pilote-v1.md` (`a67e6930`) l. 222 : le rejeu des épisodes avec les sondes figées est refusé à l'unanimité, parce que « 60 tâches d'épreuve : y tirer un choix rompt la condition de leur maintien ».
   - `docs/notes/couche-2-preparation-v1/devis-pilote-v1/devis-pilote-couche-2-v1.md` (`044112d3`) l. 184 : « 60 tâches d'épreuve », distinctes des « 32 tâches de réserve ».
6. **Le brouillon 3 du préenregistrement de G1** (`brouillons/G1-preenregistrement-v1-brouillon3.md`, `e488d065`) prévoit des épisodes neufs, « gelés en T1.1 » (l. 98), et des jeux séparés pour l'entraînement des sondes, le calibrage et l'évaluation (l. 99). Il déclare arrêtante « une même tâche ou un même épisode dans l'entraînement des sondes, le calibrage et l'évaluation » (l. 129).

## Inféré (non établi)

- Si les 60 tâches restent dans l'épreuve de G1 (point 4), toute **sélection** faite sur leurs épisodes ou leurs vecteurs ferait de ces tâches une matière de conception, puis d'évaluation. Cette sélection peut porter sur une direction, une couche, une statistique ou un seuil, et les épisodes visés sont ceux de P3 ou leurs activations. Le brouillon 3 de G1 le déclare arrêtant (point 6, l. 129), et le collisionneur l'a refusé pour la même raison (point 5).
- Le brouillon 4 de G1, tenu par conv-audit hors de `main`, n'a pas été lu. La réponse vaut pour `main` au 30 octobre.

## Conséquences

- **Q5 (signal à 8 milliards sur les vecteurs existants)** : licite seulement si la mesure reste **descriptive**. Elle ne doit choisir ni direction, ni couche, ni statistique, ni seuil reporté vers G1, ni ordonner l'axe 1. Sinon, elle est circulaire sur les 60 tâches d'épreuve, et donc sur les 240 épisodes.
- **Piste A de la question v1** : un test de mort lu sur ces épisodes est circulaire si son issue choisit ce qui sera éprouvé à G1. Un test qui ne fait que tuer une fiche, sans rien choisir pour G1, reste licite, mais doit être déclaré au préenregistrement de G1 (P-036 l. 253).

## Recommandation

Déclarer les 60 tâches de P3 « vues » au préenregistrement de G1 et les **retirer de l'épreuve de G1** (au profit des 32 tâches de réserve et de tâches fraîches), ou, à défaut, interdire à la course 2 toute sélection sur les épisodes et vecteurs de P3 (Q5 et la piste A seulement descriptives). C'est un choix pour Lazar ; ma préférence va au retrait, plus simple à vérifier.
