# Additif v2 à la consigne d'intégration de la chaîne T0.6 v13 (`consigne-integration-chaine-t06-v13-main-v1.md`, `2e0fe2d4…`)

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-09 vers 22:25 UTC (`date -u`). La v1 reste valable en entier ; cet additif ne règle que le cas qui a arrêté le développeur (R12).

## Cas

Conflit « ajouté des deux côtés » sur `docs/notes/g0-deux-semaines-v1/e3-ter-v1/config-t06-course-explo-v1.json` et son compagnon : côté `main`, `1911a9e9…` (`plafond_usd` 100, instantané du commit `3957504d`, 8 novembre 15:33 UTC) ; côté branche, `59e896b5…` (`plafond_usd` 95, commit d'épreuve `be729130`, **la version jouée par 7a**, citée par l'ordre de 7a, la r3 et la lecture A). Seule différence : la ligne 121. Aucun fichier de `src/`, `scripts/` ou `tests/` ne le cite. Remarque CL-11 (mineure) de `contre-lecture-regle-e3-6-transcription-v1-cl1.md`.

## Décision de la mère (routine, R12 : on n'écrase jamais)

1. Garder sous le nom actuel la version de `main` (`1911a9e9…`) et son compagnon (`git checkout --ours` sur les deux fichiers).
2. Ajouter la version jouée sous le nom neuf `docs/notes/g0-deux-semaines-v1/e3-ter-v1/config-t06-course-explo-v1-joue-be729130.json`, octet pour octet depuis `git show 1609a4bf:docs/notes/g0-deux-semaines-v1/e3-ter-v1/config-t06-course-explo-v1.json`, empreinte vérifiée égale à `59e896b5a348a3d545d375cea148102e352d1c813f0939e1d99f3f1827e774b4`, avec son compagnon (`PYTHONPATH=src python -m controle_ia.scellement sceller`).
3. `registres/go.md` : version de `main` (`--ours`).
4. Ne réécrire aucune note qui cite l'une ou l'autre empreinte : le rapport d'intégration dit lequel des deux noms porte chaque empreinte. Les notes futures citeront le nom neuf pour la version jouée.
5. Reprendre la v1 au point 2 (autres conflits éventuels), puis 3 à 6, et sorties.
