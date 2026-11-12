# Constat d'état des preuves de la porte G0 — 2026-10-29 — annexe NON SCELLÉE de la grille v2 (informatif, daté, périmé à la lecture)

Sorti de la partie gelée de `prereg/brouillon-G0-grille-lecture-v2.md` (avis Fable § 4, point 7) pour qu'aucune règle ne
puisse être taillée sur lui. Il reprend l'annexe A de la v1 (`320af9b0…`), avec les vérifications de l'avis Fable (§ 5 :
25 empreintes conformes) et les miennes du 2026-10-29 vers 10:50 UTC, au commit `7c2d76cb`. **Il n'entre dans aucune règle
et ne vaut pas lecture.** Il n'est pas scellé, à dessein ; s'il est versé, le sceller est une décision de la session.

| critère | état constaté | pièces (chemin, empreinte) |
|---|---|---|
| 1 | preuve trouvée | verdict `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (l. 3 : neutralité déclarée ; l. 11 : « Critère 1 de G0 : prouvé par ces deux runs » ; l. 13 : « Réserves au sens de la table : aucune » ; vérifié par moi) ; préenregistrement `prereg/T0.4-validation-modele-reel-v3.md` `4f711cd3…` ; contre-lectures 1 et 2 ; recalculs. Non vérifiable ici : M-0.4 (clone superficiel : `git log` rend `43bd450d`, 2026-10-27). Domaine : observation 3 du verdict (contexte 1 192 contre 1 087). |
| 2 | manquante | aucun `prereg/T0.6-*` ; brouillons seulement. P3 (`prereg/P3-premier-test-i-a-v1.md` `d975e981…` ; verdict v2 l. 18 : « G0 : la ligne retenue ne prononce aucun critère de G0 », vérifié par l'avis Fable). |
| 3 | manquante | aucun `prereg/T0.7-*` ; aucun verdict de P4-instrument dans `prereg/` ni `docs/verdicts/` (vérifié : `ls` sans résultat). |
| 4 | manquante (code seulement) | aucun `prereg/T0.8-*` ; brouillons. Pièce source du « 0,99 » : `docs/notes/couche-2-preparation-v1/rejeu-juges-v1/lecture-et-audit-r4-v1/lecture-rejeu-juges-v1.md` `8799f7d3800db7444a693677c3d7dfbb3b3e283becc41c88ae063748a877f9b8` (l. 10-18 : aucune cellule ≥ 0,99 ; 157/180 = 0,87), vérifiée. |
| 5 | preuve trouvée | préenregistrement `7474743a…` (M-0.2 OK ; **ne contient pas « G0 »**, `grep -c` = 0) ; grille `prereg/T0.3-grille-v2.json` `5609f920…` ; manifeste `runs/20261004-080257-t03/manifeste.json` (cite `7474743a…`, `5609f920…`, `commit_cite` `d73ac469…`, `decisif: true`, `cree_le` 2026-10-04T08:02:57, vérifié par moi) ; lecture `diag/20261004-080257-t03/lecture.md` et `.json` (31 prédictions « confirmée », audit non déclenché, selon la v1 et l'avis Fable). |
| 6 | manquante (brouillons) | aucun `prereg/G1-*` ; `brouillons/G1-preenregistrement-v1-brouillon3.md`, première ligne « # Préenregistrement — porte G1 : plan 2 × 2 accès × agrégation (T1.2, E1.2) — v1 — brouillon 3 » (vérifié). |
| 7 | partielle (brouillons contre-lus, non scellés) | aucun `prereg/papier-C-*` ; `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md`, première ligne « # Préenregistrement — papier C : HC1, HC2, HC2b, HC3 (TC.1 à TC.3) — v1 — brouillon 5 » (vérifié) ; brouillons 6 et 7 en archive selon R-317. |
| 8 | partielle | niveaux 1 (`b0b519fe…`) et 2 (`bbe0c1f5…`) ; manquent la table des chiffres sur le périmètre décidé, le contrôle de traçabilité, le script R5, les références entrées depuis le 6 octobre. |

Bilan : 2 critères avec preuve trouvée (1, 5), 2 partiels (7, 8), 4 sans preuve (2, 3, 4, 6) ; même compte que
`registres/etat.md` l. 109 (`21975b31…`). Clone de travail superficiel ; `registres/decisions.md` `b8fe8230…`, l. 462 = N-027.

Écrit le 2026-10-29 (heure de fin : `date -u` ci-dessous).
Fin : 2026-10-29 10:56:34 UTC.
