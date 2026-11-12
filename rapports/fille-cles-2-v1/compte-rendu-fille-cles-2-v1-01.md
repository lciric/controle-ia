# Fille clés 2 — compte rendu court 01 — ARRÊT à l'étape 2

Heures par `date -u`. Session fille, environnement « Default », 4 cœurs, Python 3.13.18, numpy 2.4.6.

## Verdict
**Arrêt** (étape 2, bloc 4 de l'ordre, 1.4 essais) : `test_lire_items_phase1_v4` rend **1 échec, 78 passés** (attendu 79 passés). Aucun relais lancé, aucun appel, aucune dépense. Rien d'autre n'est fait ; aucun essai rejoué.

## Étape 0 — clés (par le nom), 09:47:59Z
GEMINI_API_KEY_2, KIMI_API_KEY, VAST_API_KEY, OSF_TOKEN, HF_TOKEN, CONTROLE_IA_GITHUB_TOKEN_2, GEMINI_API_KEY : toutes « présente ».

## Étape 1 — mise en place
- Dépôt à `/home/user/controle-ia-travail`, tête d'arrivée `76af84e4`, environnement installé (pip code 0).
- Ordre : empreinte `30f265a9a1c49a6af734c71a69cdc444989f9ec1c6e294525f43035a28705f18` conforme.
- Commits `64e67cbd…`, `d858b66f…`, `f8b5ab72…` manquants au clone partiel, récupérés par `git fetch --depth=1 origin <empreinte complète>` (et la branche d'archive par refspec explicite).

## Étape 2 — restauration et contrôles (09:52Z → 09:53Z)
- Archive `201e1295e0e820498b44e766e74a62e5a567f8903f3d63f96974e5e074ccc56e` : OK ; racine extraite (absente avant) ; `variables-v1.sh` = `90b6bee859044fd9edbb7351c4efa61a3c11eae0898576525c4023136b7bb976` conforme.
- Arbre du code au commit `64e67cbd4a870a4bc8f861e7a4632c300283a3c2` : « commit du code conforme ».
- Empreintes de la génération : 7 « OK », code 0.
- Empreintes de l'essai de format : 15 « OK » sur 16, seul manque `relais-format/console-relais-kimi-v1.log` (écart connu, R-1765), code 1.
- `manifeste-lecture-phase1-v4.json` : `3a3d868ebc15e995040c9c70807e801589bd02dda4bf7725865c1e22580222a2` conforme.
- Outils de reprise : 4 compagnons `.sha256` « OK » ; blocs 3, 4, 5, 6, 18, 19, 20, 21 extraits (code 0) ; seuls 3 à 6 exécutés.
- Bloc 3 : douze « OK », `code sha256sum=0` ; GO : `1` ; `entropie 17812956677980471985` ; python 3.13.18, numpy 2.4.6. Conforme.
- **Bloc 4 : écart.**
  - `test_generer_items_v2` code 0 : 24 passés — conforme ;
  - `test_epreuve_phases_v1` code 0 : 6 passés — conforme ;
  - **`test_lire_items_phase1_v4` code 1 : 1 échec, 78 passés** — attendu 79 passés ;
  - `test_analyser_phase1_v3` code 0 : 12 passés — conforme.
  - Essai en échec : `test_B5_cle_refusee_arrete_tous_les_appels` ; assertion `(10 - 6) <= 2` (10 appels comptés, 6 au point de référence, marge 2). Lecture prudente : essai qui dépend de l'ordonnancement des fils (les appels qui partent après le refus d'une clé), possiblement sensible à la machine (4 cœurs ici) ; **non vérifié, non rejoué**.
  - Console : `consoles/essais-test_lire_items_phase1_v4-v1.log` = `700f49cc453c4a3b0575037b357702ef6e24883198e3a18026054d464622c82f` (les trois autres : `a89067d4…` générer, `81e5c70b…` phases, `05b8b907…` analyser). Ces consoles sont neuves dans ce conteneur (l'archive les excluait) : rien d'écrasé.
- Bloc 5 : GEMINI_API_KEY_2 et KIMI_API_KEY « présente ». Conforme.
- Bloc 6 : « port 8789 libre ». Conforme.

## Étapes 3 à 6
Non faites : ni feu vert comparé, ni demande de mot à Lazar, ni relais, ni lecture. Aucun processus lancé ni laissé (hors arbre `code/` ajouté par `git worktree add`). Racine `/home/user/epreuve-etiqueteur-phase1-v1` restaurée et laissée en place.

## Nœud pour la mère
Décider : (a) tenir l'échec pour un défaut de l'environnement et autoriser un rejeu de cet essai seul (console neuve, nom versionné) ; (b) faire diagnostiquer l'essai par un lecteur neuf avant tout lancement ; (c) autre. J'attends.
