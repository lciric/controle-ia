# Correction du questionnaire commun : levée de l'anonymat — v1

Session-dépôt (nouvelle instance `session_013QMaymMAdDjNfPoz8ySwTc`), 10 novembre 2026, levée faite après le rendu du
correcteur (rendu reçu vers 11:40 UTC ; table d'étiquettes ouverte après réception).

## Entrées
- Questionnaire : `docs/notes/rapports-directeur/depuis-zero-comparaison-v1/questionnaire-commun-v1.md` (main, `83589e95…`).
- Consigne du correcteur : même dossier, `consigne-correcteur-v1.md` (`f754b1a9…`), appliquée sans changement.
- Clé : branche `cle/questionnaire-commun-v1`, commit `2107363b`, `cle-questionnaire-commun-v1.md`, `3a38b037c5b5…` ;
  vérifiée par le correcteur contre l'entrée R-2139 de `main`. **Non versée sur `main` ni sur cette branche.**
- Jeux de réponses, champs `document` et `lecteur_modele` retirés, seules les quinze réponses gardées :
  - mère : branche `reponses/questionnaire-commun-mere-v1`, commit `77f6e59d`, `9ff5a931…` ;
  - dépôt : `docs/notes/entretien-resultats-v1/comparaison-depuis-zero-v1/reponses-lecteur-naif-depot-v1.json`, `ef41af6f…`
    (document lu : explication depuis zéro v1, `8c190a57…`) ;
  - session du bras : branche `claude/compassionate-meitner-d4ryyk`,
    `docs/notes/entretien-recapitulatif-v1/questionnaire-commun-reponses-v1/reponses-lecteur-sonnet-programme-v4.json`,
    `d338dbf0…` (son nom dit que le document lu est le programme depuis zéro **v4**, non la v5 du dossier fusionné).
- Étiquettes tirées par `secrets.SystemRandom().shuffle` à 11:37:10 UTC : `table-etiquettes-correction-v1.json`.
  Empreintes des entrées anonymes : `entrees-correcteur-empreintes-v1.txt`.

## Correcteur
Sous-agent neuf, Claude Opus 5.5, qui n'a écrit ni le questionnaire, ni la clé, ni aucun document, ni aucune réponse ; il n'a
ouvert que les cinq fichiers fournis. Début 11:37:34, fin 11:39:33 UTC (`date -u`, relevées par lui). Rendu :
`correction-questionnaire-commun-v1.md` (`35268004c84c5890…`).

## Résultat, anonymat levé

| étiquette | jeu | total sur 30 | erreurs |
|---|---|---|---|
| Y | mère | 29 | 0 |
| Z | dépôt | 26 | 0 |
| X | session du bras (lecteur Sonnet, programme v4) | 21 | 0 |

## Réserves
- Un seul correcteur, une seule passe ; la clé a été écrite par l'auteur du questionnaire, avant les lectures.
- Les lecteurs n'étaient pas tous du même modèle (le champ `lecteur_modele` a été retiré au correcteur, non comparé ici).
- Le jeu du bras porte sur la v4 de son document, pas sur la v5 versée au dossier.
- Remarques du correcteur : question 4 à 1 pour les trois jeux (élément 2 de la clé absent partout) ; cas limites qui
  baissent X aux questions 2 et 9 ; quelques affirmations « non vérifiables par la clé » (question 15).
- Ce tableau compare la compréhension qu'un lecteur neuf tire de chaque document ; il ne juge pas le fond.
