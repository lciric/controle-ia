# Consigne : session fille « préalables de P3-bis » — phase 2, étape C (pièces, épingles, passages canoniques) — v1

Écrite par la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` le 2026-11-11 à 14:05 UTC (heure relevée par `date -u`). Destinataire : la session fille `session_013QMayo3Je79e17xB1yHiDw` (étape A conforme, R-2347). Mêmes règles que les phases précédentes (consignes `0d7dc7e0…` et `7ab6e8b6…`) : interdits communs v2, **aucun fichier de T0.7 ouvert** (le rapport P-9 et toute pièce qui cite T0.7 se versent sans être lus), clés par leur nom seulement, aucune dépense, aucun appel de modèle hors du vrai découpeur de la répétition finale (`HF_TOKEN` par son nom), garde des secrets à 0 avant chaque commit, `git fetch` avec refspec, extraction partielle gardée, arrêt sur tout refus. **Ni S, ni lancement** dans cette étape : ils viendront sur consigne neuve.

## Ce qui fonde cette étape (registre, sur `main` à `00af685f`)
R-2345 (circularité ; décision), R-2349 (P-9), R-2352 (mot de Lazar : sceller et lancer), R-2355, **R-2356** (candidat 2 écrit : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat2.md`, **`eb7e5b8b671a71a745323135fc6aed5b0f30ad28e515575518189a2d22d71ecc`**). La relecture courte du candidat 2 tourne en parallèle : si elle impose un candidat 3, tout ce qui suit est refait sur une branche `scellement/p3bis-v2` (aucun écrasement).

## C1. Récupérer `main`
`git fetch origin +refs/heads/main:refs/remotes/origin/main` ; `00af685fb2551f46585214de24921dbb4653ceee` doit être ancêtre de `origin/main`.

## C2. Commit « pièces » sur `scellement/p3bis-v1` (tête `d0d9fcb8`)
Par `git checkout <commit> -- <dossier>` (aucune lecture, aucune autre écriture) :
- de `00af685fb2551f46585214de24921dbb4653ceee` : `brouillons/P3-bis-temoin-positif-v1/` (dont le candidat 2 et son compagnon, la configuration relue, les rapports), `docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/` (sortie de l'essai de fermeture v3, contre-lecture courte du code), `docs/notes/g0-deux-semaines-v1/concordance-journal-p3bis-t07-v2/` (P-9 : **ne pas l'ouvrir**) ;
- de `dfb1ed7b7040fa22fca95d931d0e0a8b4ea43527` (ta phase 1) : `docs/notes/g0-deux-semaines-v1/p3bis-prealables-v1/`.
Vérifie avant le commit : arbre gelé toujours égal à `5e457525` ; candidat 2 = `eb7e5b8b…` ; chaque pièce épinglée (ci-dessous) égale à son épingle et à son compagnon (`git show HEAD:<chemin>` après le commit, comme l'étape 4 de `sceller_p3bis_v2.sh`).

## C3. Commit « épingles »
Dans `docs/procedures/P3-bis-temoin-positif-v1/controles_avant_depense_p3bis_v2.sh`, remplace exactement ces lignes (une occurrence chacune), puis les deux qui suivent :
   - `CANDIDAT_RELU_CHEMIN=A_EPINGLER`
     → `CANDIDAT_RELU_CHEMIN=brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat2.md`
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
     → `RAPPORTS_ATTENDUS="brouillons/P3-bis-temoin-positif-v1/contre-lecture-brouillon2-v1/contre-lecture-p3-bis-brouillon2-v1.md=8399dc55ae358712ca97b4cffa5f79d98e45207ad25494b8abc01c98b7921ae0 brouillons/P3-bis-temoin-positif-v1/contre-lecture-2-brouillon5-v1.md=f12d7f211f0b1b92eb1a59ec543442d2d79aaa9e476507ec8a8b9ec408d4ef0e brouillons/P3-bis-temoin-positif-v1/contre-lecture-3-brouillon6-v1.md=4c3cb62831a42f8e02e632ea1c7d111f94bb24b9ad066ace9e1ccfe148fde622 brouillons/P3-bis-temoin-positif-v1/contre-lecture-code-p3bis-v1.md=7a074ad1c0033b53560b0c50120036d9d9e914f72957bfe1cc078598c39f7242 brouillons/P3-bis-temoin-positif-v1/contre-lecture-differentielle-code-v2-chaine-v1.md=011942534477d65627b961f09e814c2fe0693d44b7d525633466fd4a918c00d9 brouillons/P3-bis-temoin-positif-v1/contre-lecture-4-brouillon11-v1.md=90847ae2d017c6e100a15cf80ecee17645a4c71ecd33197187767cc2ff9d2c13 brouillons/P3-bis-temoin-positif-v1/contre-lecture-differentielle-code-a1de3915-v1.md=845c4de54e72207a320edf089c606bacf0cd87837d473ab654de48c3ddc839c9 docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/contre-lecture-courte-code-p3bis-regle-a-v1.md=03f1bb59d7fc2afed8bf8939f2457c177a36d477deae5bdb6e1c1dc2f3235141 brouillons/P3-bis-temoin-positif-v1/P3-bis-candidat1-relecture-courte-v1.md=85ee0b47078d18311bb70872877c0b73c54fc480219e87678e4cc6ae63551eec"                     # paires chemin=empreinte des rapports de contre-lecture cités par le texte`
   - `CANDIDAT_RELU=A_EPINGLER                         # texte relu (contre-lecture 4), octet pour octet`
     → `CANDIDAT_RELU=eb7e5b8b671a71a745323135fc6aed5b0f30ad28e515575518189a2d22d71ecc                         # texte relu (contre-lecture 4), octet pour octet`
   - `PY=A_EPINGLER` (ligne entière, commentaire gardé) → `PY=/home/user/venv-p3bis-py311-v1/bin/python` + le même commentaire.
Dans `recuperation_p3bis_v2.sh` : la ligne `PY=A_EPINGLER …` → `PY=/home/user/venv-p3bis-py311-v1/bin/python …` (commentaire gardé).
Puis : aucune ligne `^[A-Z_]+="?A_EPINGLER` dans les deux fichiers ; compagnons des deux fichiers re-scellés (`PYTHONPATH=src "$PY" -m controle_ia.scellement sceller <fichier>`) ; `git diff 5e457525 HEAD -- docs/procedures/P3-bis-temoin-positif-v1/` ne montre que ces quatorze lignes et les deux compagnons (relevé versé dans ton rapport). **Pousse** la branche (`git push origin scellement/p3bis-v1`, retentatives 2, 4, 8, 16 s) et préviens la mère (elle contrôle la règle (b) sur la branche poussée pendant que tu joues C4).

## C4. Passages canoniques (P-6), dans cet ordre, chacun dans une racine neuve de ton bac à sable
Relève d'abord `df -Pk` (≥ 12 692 612 ko). Formes exigées des journaux : dictionnaire `JOURNAUX` de `verifications_p3bis_v2.py` (dernière ligne exacte, scripts éprouvés attendus, aucune ligne « NON CONFORME » ni « Traceback ») ; modes d'emploi : en-têtes des scripts (« Usage »), rapport du développeur `docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/rapport-code-p3bis-regle-a-v1.md` et ses journaux non canoniques. Sorties standard et d'erreur redirigées vers le journal canonique, dans ton bac à sable :
1. `banc-verifications-p3bis-v2.log` (banc du module commun, par `pytest` comme l'écrit son en-tête, sous `PY`), puis `banc-lanceur-p3bis-v2.log`, `banc-surveillance-p3bis-v2.log`, `banc-controles-p3bis-v2.log`, `banc-recuperation-p3bis-v2.log`, `repetition-jouet-p3bis-v2.log` ;
2. les six vérifiés par `python3 -I docs/procedures/P3-bis-temoin-positif-v1/verifications_p3bis_v2.py preuves <dossier> <six noms>` ; copiés sous `docs/procedures/P3-bis-temoin-positif-v1/`, scellés, **commit « six journaux »** ;
3. puis `repetition_finale_p3bis_v2.sh scellement/p3bis-v1 <racine neuve>` (mode décisif, vrai découpeur) → `repetition-finale-p3bis-v2.log` ; vérifié par `preuves` avec les sept noms ; copié, scellé, **commit « journal de la répétition finale »** ; poussée.
Tout passage non conforme : **arrêt**, rien versé de ce passage, rapport (le journal d'échec gardé dans ton bac à sable sous un nom non canonique).

## Rapport à la mère (`send_message`)
Commits C2, C3, C4 et tête poussée ; relevé du `git diff` de C3 ; empreintes des sept journaux et leurs dernières lignes ; durées ; place disque avant et après ; écarts. Puis attends la consigne de S et du lancement.
