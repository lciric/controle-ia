# Consigne : session fille « préalables de P3-bis » — phase 2, étape C, branche v2 (pièces, épingles, passages canoniques) — v1

Écrite par la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` le 2026-11-11 à 15:03 UTC (heure relevée par `date -u`). Destinataire : la session fille `session_013QMayo3Je79e17xB1yHiDw`. **Remplace l'étape C de la v1** (consigne `e0abf5af…`, branche `scellement/p3bis-v1` abandonnée à `a3116ff5`, R-2367) ; mêmes règles (interdits communs v2, aucun fichier de T0.7 ouvert, clés par leur nom, aucune dépense, aucun appel de modèle hors du vrai découpeur de la répétition finale, garde des secrets, `git fetch` à refspec, extraction partielle, arrêt sur tout refus) ; **ni S ni lancement** dans cette étape. Permissions déjà données et toujours valables : réécriture directe des compagnons des fichiers épinglés (R-2360) ; `main` locale sur `origin/main` (R-2364) ; `.venv` fait de liens vers `PY` (R-2364).

## Ce qui fonde cette étape (registre, sur `main` à `154e3735`)
R-2367, R-2373, R-2374 (bancs corrigés au commit `68ded698ce1bbfd8815d7b7ab28557775e4d2e5b`, citables au scellement) ; **R-2375** (candidat 3 : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat3.md`, **`76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb`**) ; branche **`scellement/p3bis-v2`** poussée par la mère : tête `10781b85b73db2d01c1be73c41bf8df5a5dfed11` (= `68ded698` + P-3 et P-10, mêmes changements que `d0d9fcb8`). La relecture courte du candidat 3 tourne en parallèle : si elle impose un candidat 4, tout ce qui suit est refait sur une branche neuve.

## C1. Récupérer
`git fetch origin +refs/heads/main:refs/remotes/origin/main` et `git fetch origin +refs/heads/scellement/p3bis-v2:refs/remotes/origin/scellement/p3bis-v2` ; `154e3735f1fb4a9de03f06ff88c6ac5c84b5fc18` ancêtre de `origin/main` ; branche locale `scellement/p3bis-v2` suivie, extraite (arbre propre, extraction partielle gardée), tête `10781b85`.

## C2. Commit « pièces »
Par `git checkout <commit> -- <dossier>` (aucune lecture) : de `154e3735f1fb4a9de03f06ff88c6ac5c84b5fc18` : `brouillons/P3-bis-temoin-positif-v1/`, `docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/`, `docs/notes/g0-deux-semaines-v1/concordance-journal-p3bis-t07-v2/` (P-9 : **ne pas l'ouvrir**) ; de `dfb1ed7b7040fa22fca95d931d0e0a8b4ea43527` : `docs/notes/g0-deux-semaines-v1/p3bis-prealables-v1/`. **Garde** : après ce checkout, les trois bancs de `docs/procedures/P3-bis-temoin-positif-v1/` doivent rester à leur empreinte de `68ded698` (`36a88949…`, `ae2e2d2f…`, `750ec253…`) : aucun des dossiers ci-dessus ne les touche ; vérifie-le. Vérifie aussi : arbre gelé égal à `5e457525` ; candidat 3 = `76ab66ce…` ; chaque pièce épinglée égale à son épingle et à son compagnon (`git show HEAD:…` après le commit) ; les onze rapports présents et scellés.

## C3. Commit « épingles »
Dans `controles_avant_depense_p3bis_v2.sh` (même dossier), remplace exactement :
   - `CANDIDAT_RELU_CHEMIN=A_EPINGLER`
     → `CANDIDAT_RELU_CHEMIN=brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat3.md`
   - `CONFIG_RELUE=A_EPINGLER`
     → `CONFIG_RELUE=612b0c6ce5c4263eb3016b72ad85155dd2307f9dd887379d2a1133ed644a9d05`
   - `CONFIG_RELUE_CHEMIN=A_EPINGLER`
     → `CONFIG_RELUE_CHEMIN=brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat1-pieces/P3-bis-temoin-positif-config-v1-candidat1.json`
   - `CONSIGNES_RELUES=A_EPINGLER`
     → `CONSIGNES_RELUES=7d35576d65c030edcc6441e142ea95732679b674edcb1fd1af86ab8f69c04367`
   - `CONSIGNES_RELUES_CHEMIN=A_EPINGLER`
     → `CONSIGNES_RELUES_CHEMIN=brouillons/P3-bis-temoin-positif-v1/P3-bis-consignes-v1-brouillon2.md`
   - `CODE_RELU=A_EPINGLER                             # commit du code corrigé, relu (40 caractères)`
     → `CODE_RELU=5e4575259478af3611e2c7fb1313342912caf484                             # commit du code corrigé, relu (40 caractères)`
   - `ESSAI_FERMETURE=A_EPINGLER                       # empreinte de la sortie versée de l'essai différentiel de fermeture`
     → `ESSAI_FERMETURE=9375628699e95fc6563d2da4ce0172371cfeb2e3fcb56b0fbe8e2aa6774b1464                       # empreinte de la sortie versée de l'essai différentiel de fermeture`
   - `ESSAI_FERMETURE_CHEMIN=A_EPINGLER`
     → `ESSAI_FERMETURE_CHEMIN=docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/essai-fermeture-p3bis-v3-sortie-v1.txt`
   - `LONGUEURS_ATTENDUES=A_EPINGLER                   # empreinte du résumé des longueurs attendues (JSON, forme de resume_longueurs)`
     → `LONGUEURS_ATTENDUES=7c94d43cc7bea9a5af3c5c5ec34f552256bbcf258a0436d1a2295c91d45cfb21                   # empreinte du résumé des longueurs attendues (JSON, forme de resume_longueurs)`
   - `LONGUEURS_ATTENDUES_CHEMIN=A_EPINGLER`
     → `LONGUEURS_ATTENDUES_CHEMIN=docs/notes/g0-deux-semaines-v1/p3bis-prealables-v1/longueurs-attendues-p3bis-v1.json`
   - `RAPPORTS_ATTENDUS=A_EPINGLER                     # paires chemin=empreinte des rapports de contre-lecture cités par le texte`
     → `RAPPORTS_ATTENDUS="brouillons/P3-bis-temoin-positif-v1/contre-lecture-brouillon2-v1/contre-lecture-p3-bis-brouillon2-v1.md=8399dc55ae358712ca97b4cffa5f79d98e45207ad25494b8abc01c98b7921ae0 brouillons/P3-bis-temoin-positif-v1/contre-lecture-2-brouillon5-v1.md=f12d7f211f0b1b92eb1a59ec543442d2d79aaa9e476507ec8a8b9ec408d4ef0e brouillons/P3-bis-temoin-positif-v1/contre-lecture-3-brouillon6-v1.md=4c3cb62831a42f8e02e632ea1c7d111f94bb24b9ad066ace9e1ccfe148fde622 brouillons/P3-bis-temoin-positif-v1/contre-lecture-code-p3bis-v1.md=7a074ad1c0033b53560b0c50120036d9d9e914f72957bfe1cc078598c39f7242 brouillons/P3-bis-temoin-positif-v1/contre-lecture-differentielle-code-v2-chaine-v1.md=011942534477d65627b961f09e814c2fe0693d44b7d525633466fd4a918c00d9 brouillons/P3-bis-temoin-positif-v1/contre-lecture-4-brouillon11-v1.md=90847ae2d017c6e100a15cf80ecee17645a4c71ecd33197187767cc2ff9d2c13 brouillons/P3-bis-temoin-positif-v1/contre-lecture-differentielle-code-a1de3915-v1.md=845c4de54e72207a320edf089c606bacf0cd87837d473ab654de48c3ddc839c9 docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/contre-lecture-courte-code-p3bis-regle-a-v1.md=03f1bb59d7fc2afed8bf8939f2457c177a36d477deae5bdb6e1c1dc2f3235141 brouillons/P3-bis-temoin-positif-v1/P3-bis-candidat1-relecture-courte-v1.md=85ee0b47078d18311bb70872877c0b73c54fc480219e87678e4cc6ae63551eec brouillons/P3-bis-temoin-positif-v1/P3-bis-candidat2-relecture-courte-v1.md=c559f2c8b63fb2562cb337502ccfb853d9b2963fef2b915d6bd16bb1dc65964f docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/contre-lecture-courte-bancs-epingles-p3bis-v1.md=df732d18a8b7a65566f0ad8fd47bf59cb040ce3c12b73cc5991e770b23e267ae"                     # paires chemin=empreinte des rapports de contre-lecture cités par le texte`
   - `CANDIDAT_RELU=A_EPINGLER …` (commentaire gardé) → `CANDIDAT_RELU=76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb …`
   - `PY=A_EPINGLER …` → `PY=/home/user/venv-p3bis-py311-v1/bin/python …` (commentaire gardé).
Dans `recuperation_p3bis_v2.sh` : `PY=A_EPINGLER …` → `PY=/home/user/venv-p3bis-py311-v1/bin/python …`.
Puis : aucune épingle restante ; compagnons des deux fichiers réécrits à la forme de `scellement.sceller` (R-2360), `scellement verifier` ; `git diff 68ded698 HEAD -- docs/procedures/P3-bis-temoin-positif-v1/` : seuls les deux fichiers épinglés (quatorze lignes) et leurs deux compagnons. **Pousse** (`git push origin scellement/p3bis-v2`) et préviens la mère.

## C4. Passages canoniques (P-6), comme à l'étape C v1, racines neuves
Place relevée avant (≥ 12 692 612 ko). Dans l'ordre : `banc-verifications-p3bis-v2.log`, `banc-lanceur-p3bis-v2.log`, `banc-surveillance-p3bis-v2.log`, `banc-controles-p3bis-v2.log`, `banc-recuperation-p3bis-v2.log`, `repetition-jouet-p3bis-v2.log` ; `preuves` sur les six ; copiés sous `docs/procedures/P3-bis-temoin-positif-v1/`, scellés, **commit « six journaux »** ; puis `repetition_finale_p3bis_v2.sh scellement/p3bis-v2 <racine neuve>` → `repetition-finale-p3bis-v2.log`, `preuves` sur les sept, copié, scellé, **commit**, poussée. Les journaux de la série v1 restent dans ton bac à sable, jamais versés. Tout passage non conforme : arrêt, rien versé de ce passage, rapport.

## Rapport à la mère (`send_message`)
Commits C2, C3, C4 et tête poussée ; relevé du `git diff` de C3 ; empreintes et dernières lignes des sept journaux ; durées ; place ; écarts. Puis attends la consigne de S et du lancement.
