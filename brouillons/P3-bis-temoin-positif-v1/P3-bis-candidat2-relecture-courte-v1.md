# P3-bis : relecture courte de l'écart du candidat 1 au candidat 2 — v1

- Date : 2026-11-11, de 13:59 à 14:07 UTC (heures relevées par `date -u`).
- Relecteur : agent neuf, **Claude Fable 5.2** (`claude-fable-5-2`), sous-agent de la session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Je n'ai écrit ni P3-bis, ni ses couples, ni son code, ni sa chaîne, ni aucune de
  leurs contre-lectures ou relectures. **Aucun fichier de T0.7 ouvert** (ni texte, ni brouillon, ni note, ni module).
- Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-relecture-courte-p3bis-candidat2-v1.md`
  (`3595e2813fcc5ebce7fb6eca52951ad8f72cdc4c46f29dbd79ddf34bdec3e609`, recalculée avant lecture), **corrigée par un
  message de la session mère reçu pendant le travail (R-2356)** : l'arrivée n'est plus la sortie à blanc v2 mais le
  **texte final**, avec les couples v3 ; la phrase de la date tenue s'ajoute au mandat.
- Départ : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat1.md`
  (`9a56a657b1fad1e23b0cc11e41831f066eed48674159dbc55c2a869aa56c4271`).
- Arrivée : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat2.md`
  (`eb7e5b8b671a71a745323135fc6aed5b0f30ad28e515575518189a2d22d71ecc`, recalculée, égale à son compagnon et à R-2356).
- Couples : `…-candidat2-pieces/P3-bis-preenregistrement-v1-candidat2-couples-v3.json`
  (`c55ebb0f18becb1dcff0f7b8eb28ce921b85824840afd3ee2e0d31aa9593cf35`, 22 couples C2-01 à C2-22).
- Épingles proposées : `…-candidat2-pieces/P3-bis-epingles-proposees-v1.json`
  (`0fb1443aff22133c8aaaac1616bbc191a53cfd0b2de8c4ffbe8fe53e13240389`).
- Chaîne v2 au commit du code `5e4575259478af3611e2c7fb1313342912caf484`, par `git show` :
  `controles_avant_depense_p3bis_v2.sh` (`67c3c288…`), `sceller_p3bis_v2.sh` (`f0c002cc…`), lus en entier ;
  `recuperation_p3bis_v2.sh` (`f95c60b9…`), l. 1-70 ; `verifications_p3bis_v2.py` (`1524df5f…`), `JOURNAUX` et
  `preuves` (l. 600-640).

## Verdict

**« Relu, conforme ».** Le candidat 2 (`eb7e5b8b…`) est, à l'octet, le candidat 1 auquel on applique les 22 couples v3.
Une seule section gelée change, « Plan d'analyse », par N-1 seul. Le texte ne cite aucune empreinte qui dépende de lui.
La règle d'épinglage est exacte au regard des scripts. Les épingles proposées sont justes. Aucun couple de correction
exigé, aucun nœud. Trois notes (N-1 à N-3), sans effet sur le verdict.

## Ce qui a été refait après le changement d'arrivée

Fait d'abord sur la sortie à blanc v2 (`bfd9d889…`, couples v2 `bffe8e38…`), puis **refait en entier par programme sur
le texte final** : constats 1 à 5 (couples, sections gelées, marqueurs, `problemes`), 6 (inventaire des empreintes), 9
à 12 (citations exigées par les scripts, épingles, pièces), 14 (date tenue). La lecture des couples a été faite sur la
v2 ; l'écart des couples v2 aux couples v3 a été calculé par programme : seuls C2-02, C2-06, C2-09, C2-10 et C2-16
changent (champ « nouveau » ; pour C2-16, « decision » et « motif » aussi), et ces cinq ont été relus dans la v3. Les
dix-sept autres couples sont identiques dans les deux versions.

## Constats

Programmes du relecteur, dans le bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-relecture-c2/` :
`m1f.py`, `m2f.py`, `m3f.py`, `m4f.py` (écrits par moi, indépendants du script du rédacteur), lancés par
`PYTHONPATH=src .venv/bin/python`.

### Mandat 1 — couples, sections gelées, marqueurs

1. **Couples réappliqués = texte final, à l'octet** (`m1f.py`). 22 couples, identifiants C2-01 à C2-22 dans l'ordre ;
   chaque « ancien » trouvé une fois dans le candidat 1 et une fois dans le texte courant au moment de son application.
   Sortie : « réappliqués == arrivée, à l'octet : True ».
2. **Couples défaits = candidat 1, à l'octet.** Dans l'ordre inverse, chaque « nouveau » trouvé une fois. Sortie :
   « défaits == candidat 1, à l'octet : True ».
3. **Sept sections gelées** (découpage de `controle_ia.prereg.sections`, corps comparés à l'octet) : « Hypothèse »,
   « Prédiction chiffrée et signe attendu », « Métrique », « Seuil », « Critères de lecture gelés », « Liste d'arrêt »
   égales à l'octet ; « Plan d'analyse » diffère, et le corps du candidat 1 où C2-11 seul est appliqué (« **niveau
   tenu** — 0,0100 » → « **aucun dépassement établi du niveau** — 0,0100 », trouvé une fois) égale celui de l'arrivée.
   Par position dans le candidat 1, C2-11 est le seul couple qui tombe dans une section gelée ; c'est le seul déclaré
   gelé. Titres de niveau 2 : 27 au candidat 1, 28 à l'arrivée (la table neuve).
4. **Aucun marqueur.** `<<[A-Z0-9_]+>>` : aucune occurrence. Les deux seules suites « << » sont littérales (« <<…>> »
   et le motif `grep` du titre « Marqueurs restants »), hors du motif du bloc 4 et de `prereg.GABARIT`. « À REMPLIR » :
   0. « R-NNNN », « R-0000 » : 0.
5. **`prereg.problemes` vide** : `[]` sur l'arrivée (le candidat 1 rend ses deux marqueurs : témoin du contrôle).

### Mandat 2 — circularité

6. **Aucune empreinte qui dépende du texte** (`m2f.py`). 139 empreintes de 64 caractères, dont 19 neuves, aucune
   retirée. Les 19 : les quinze fichiers de la chaîne au commit du code ; le candidat 1 (`9a56a657…`) ; la relecture
   courte du candidat 1 (`85ee0b47…`) ; la consigne de rédaction (`85a3d612…`) ; le rapport de P-9 (`01fb3e65…`).
   Toutes existent avant le texte. Aucune empreinte d'une pièce du dossier `…-candidat2-pieces/` (v1, v2, v3, sortie à
   blanc, épingles proposées) n'est dans le texte, ni entière ni par ses huit premiers caractères ; l'empreinte du
   texte n'y est pas. Seul commit neuf : `d0d9fcb8ddf82da3919736e9b97eb8aff4c71b45` (branche de scellement, antérieur).
7. **Chaîne citée au commit du code** (`m3f.py`). Les quinze fichiers de `CHAINE` (`sceller_p3bis_v2.sh`, l. 42) :
   empreinte recalculée par `git show 5e457525:…`, égale à celle du texte, forme « `chemin` (`sha256`) » présente,
   compagnon égal au même commit ; quinze citations de cette forme, pas une de plus. Lignes `NOM=A_EPINGLER` : 13 dans
   les contrôles (l. 46-58), 1 dans la récupération (l. 42, `PY`), 0 dans les treize autres : « treize et une »,
   « quatorze lignes » exacts. À `d0d9fcb8`, les quinze fichiers sont encore égaux au commit du code (`git diff --stat`
   vide sur `docs/procedures/P3-bis-temoin-positif-v1`).
8. **Règle d'épinglage exacte au regard des scripts.**
   - `releve` (contrôles, l. 132-137) : `git show S:CANDIDAT_RELU_CHEMIN` à l'empreinte `CANDIDAT_RELU`, compagnon
     « empreinte  nom », et texte de S égal à cette empreinte : `CANDIDAT_RELU` est bien l'empreinte du texte, qu'il ne
     peut citer. Le texte le dit (point 6 ; « Contre-lecture »).
   - Scellement, étape 4 (l. 70-77) : candidat, configuration, consignes, sortie de l'essai, longueurs et rapports
     exigés à HEAD avec compagnon ; configuration relue qui cite les consignes relues. Étape 5 (l. 78-92) : chaque
     script joué égal à sa copie versée ; sept journaux de `PREUVES_EXIGEES` avec compagnon ; `preuves` : dernière ligne
     de verdict, scripts éprouvés égaux aux copies versées. Étape 7 (l. 97-106) : copies, aucun marqueur, `problemes`
     vide. Les sept noms du point 6 (c) sont ceux de `PREUVES_EXIGEES` (l. 36), mot pour mot.
   - Récupération, l. 42 et 54 : une épingle, `PY`.
   - Les valeurs que la règle dit « citées par ce texte » le sont, aux endroits dits : `CODE_RELU` (« Commit du code
     d'analyse : », une fois, égal au commit du code) ; configuration relue (chemin et `612b0c6c…`, en-tête, ligne
     « Configuration de P3 ») ; consignes relues (chemin l. 543, `7d35576d…` l. 540, même ligne) ; essai de fermeture
     (chemin et `93756286…`, plan, point 6, l. 1432) ; longueurs attendues (chemin et `7c94d43c…`, plan, point 2,
     l. 1336) ; neuf rapports (constat 10) ; `CANDIDAT_RELU_CHEMIN`.
9. **Phrases corrigées** C2-03, C2-08, C2-13, C2-14, C2-15, C2-19, C2-20, C2-21 : relues une à une, justes (chaîne
   citée au commit du code, règle, noms des journaux, empreintes au registre des décisions). **Rien d'autre ne promet
   ces citations** : recherche de `CHAINE_P3BIS`, « chaîne épinglée », « versions épinglées », « canoniques » dans tout
   le texte, hors des zones des couples (`m4f.py`) : les occurrences restantes sont historiques (statut du candidat 1,
   tables anciennes, brouillon 11) ou parlent du versement sur la branche (P-3, P-6, point 6, alinéa 16), jamais d'une
   citation par empreinte ; les deux phrases d'origine qui la promettaient (point 6) sont suivies de leur correction.
   Le précédent invoqué est exact : `prereg/P3-premier-test-i-a-v1.md` (`d975e981…`, égale à son compagnon), l. 470-485,
   cite sa chaîne par ses noms et dit « Les copies versées ne diffèrent du brouillon 4 que par les valeurs
   « A_EPINGLER » des contrôles ».

### Mandat 3 — épingles proposées

10. **Valeurs justes** (`m3f.py`, `git show` à `main`, commit `8cf9662c` au passage sur la v2, `00af685f` au passage sur le texte final).
    - `CANDIDAT_RELU_CHEMIN`, `CONFIG_RELUE_CHEMIN`, `CONSIGNES_RELUES_CHEMIN` sous `brouillons/` (contrôles l. 81-83 ;
      scellement l. 54-55) ; `LONGUEURS_ATTENDUES_CHEMIN` en `.json` (l. 85) ; `CODE_RELU` = commit du code.
    - Configuration relue, consignes relues, sortie de l'essai : empreinte et compagnon égaux sur `main`. La
      configuration relue porte `consignes_sha256` = consignes relues et `chemin_consignes` =
      `prereg/P3-bis-consignes-v1.md` (scellement l. 76-77).
    - Longueurs attendues : absentes de `main` (vérifié sur disque et par `git show`, R11), présentes avec compagnon
      au commit `dfb1ed7b`, que le fichier des épingles nomme bien comme source.
    - **Neuf rapports** : chacun à la forme exigée (l. 87), cité dans le texte par « `chemin` (`empreinte entière`) »,
      égal à son compagnon sur `main` ; la liste `rapports_attendus` égale les paires de la ligne proposée.
    - Onze lignes proposées : chacune est la ligne du commit du code, présente une fois, où « A_EPINGLER » devient la
      valeur (entre guillemets pour `RAPPORTS_ATTENDUS`) ; `epingle()` du scellement (l. 44) relit chaque valeur.
      Manquent `CANDIDAT_RELU` et `PY`, comme le texte le dit.
11. **Pièces à verser.** Étape 4 : quatorze pièces exigées (candidat, configuration, consignes, essai, longueurs, neuf
    rapports) ; cinq déjà à `d0d9fcb8` avec compagnon (consignes et quatre rapports), neuf dans `pieces_a_verser` ;
    aucune manquante, aucune en trop. Étape 5 : voir N-1.

### Mandat 4 — lignes P-9 et `CANDIDAT_RELU`, en-tête, table

12. **Ligne P-9** (C2-22) : chemin et empreinte du rapport égaux à R-2349 et au compagnon lu par `git show`
    (`01fb3e65…` ; rapport non ouvert) ; écrivain = commit du code ; lecteur C7 `b4cd9953d199dd8f220f5162e5868c5b00fd392d`
    (`git rev-parse b4cd9953`) ; « aucune discordance », réserve O-1 : mots de R-2349. Une occurrence.
13. **`CANDIDAT_RELU`** (C2-17, C2-21) : rapport `85ee0b47…` égal à son compagnon ; brouillon 11 `409c37ed…`
    recalculée ; dans le rapport : 13:06 à 13:15 UTC, Claude Fable 5.2, « Relu, conforme », 31 couples gelés, notes N-1
    à N-5, lecture de `t07/plancher_v2.py` seule ; N-1 du rapport (l. 159-164) donne mot pour mot le couple C2-11 et la
    justification reprise à la ligne 2 de la table.
14. **Date tenue** (C2-16, ajout de R-2356). Une phrase, à « Décisions pour Lazar » (l. 2423) : « date tenue : mot de
    Lazar, R-2352 (2026-11-11, vers 13:58 UTC), recopié tel quel : « Le candidat 2 est prêt.  scelle le et lnce le » ;
    la date proposée 2026-11-20T12:00:00Z est tenue (P-11) ». Les mots « Le candidat 2 est prêt.  scelle le et lnce le »
    (**deux espaces après « prêt. »**, « lnce » gardé) sont, à l'octet, la fin du mot recopié à la ligne R-2352 de
    `registres/decisions.md` (comparaison de chaînes par programme : une occurrence au registre, une dans le texte). La
    forme est permise par P-11 (« ou les mots de Lazar recopiés »). L'en-tête (l. 29), la table (ligne 6) et « Lu » sont
    accordés ; aucun « défaut échu, R-… » ne reste hors des phrases d'origine qui décrivent les deux formes permises.
15. **En-tête et table « du candidat 1 au candidat 2 »** : huit lignes ; leurs colonnes « couples » couvrent les 22
    couples, chacun au moins une fois ; « seul C2-11 touche une section gelée » : constat 3 ; « défaire redonne le
    candidat 1 » : constat 2 ; branche `scellement/p3bis-v1` au commit `d0d9fcb8…`, tirée du commit du code : ancêtre
    vérifié, R-2345 ; P-7 (R-2340), relecture courte (R-2344), P-9 (R-2349), P-11 (R-2352) : lignes du registre lues.

## Notes (sans effet sur le verdict)

- **N-1 — pièces de l'étape 5 hors de la liste.** `pieces_a_verser` couvre l'étape 4 en entier, pas l'étape 5 : les
  deux fichiers épinglés et les sept journaux canoniques, avec leurs compagnons, sont nommés sous `hors_liste`, « non
  vérifiés ici ». Le fichier le déclare, et le texte les dit versés avant S (P-5, P-6, point 6 (c)). À la mère de les
  compter dans son constat des préalables. À `d0d9fcb8`, aucun des sept journaux n'est versé (attendu : P-6 à venir).
- **N-2 — compagnons des deux fichiers épinglés.** La règle (b) parle des quinze fichiers. L'épinglage change aussi les
  deux compagnons `.sha256` des contrôles et de la récupération, sans quoi `verifier-arbre` (bloc 14 ; scellement
  l. 115-126) refuse. Le programme de la règle (b) (Q-3 de R-2352) doit attendre ces deux écarts-là en plus des
  quatorze lignes.
- **N-3 — parenthèse du point 6 (b).** « (l'étape 5 de `sceller_p3bis_v2.sh` les compare à leurs copies versées) » est
  exact, mais cette étape compare le script joué à la copie de HEAD, pas au commit du code ; l'égalité au commit du
  code tient par le `git diff` annoncé à la phrase suivante. Rien à corriger.

## Gestes déclarés

- `git ls-tree -r --name-only 5e457525 -- scripts`, filtré par `grep` sur trois noms de la chaîne : rien affiché (les
  scripts sont sous `docs/procedures/`). Le dossier `scripts/` contient un chemin de la règle 9 ; aucun nom n'a été
  affiché, aucun fichier ouvert. Geste que la règle 1 réserve : **écart déclaré**, non répété.
- `git branch -a --contains dfb1ed7b`, filtré par `grep` (noms interdits exclus) : une ligne,
  `remotes/origin/prep/p3bis-prealables-v1`.
- `git status --short` : un chemin non suivi affiché, sous `prereg/contre-lectures/`, dont le nom porte « T0.7 » ; non
  ouvert.
- Recherche de lignes dans `registres/decisions.md` (R-2342, R-2344, R-2345, R-2349, R-2352 à R-2356, R-2295, R-2340,
  un extrait de R-2320) : R-2355 parle de l'audit des fuites de T0.7 (ligne de registre, aucun fichier de T0.7).
- Lu au-delà des trois scripts nommés : `verifications_p3bis_v2.py` (l. 600-640), le rapport de la relecture courte du
  candidat 1 (lignes trouvées par recherche), `prereg/P3-premier-test-i-a-v1.md` (l. 468-487), `src/controle_ia/prereg.py`,
  la configuration relue (deux clés).
- Aucun `diag/`, aucun `runs/`, aucun fichier des interdits communs ouvert ; aucune valeur de sonde sous mes yeux.
  Aucun appel externe, aucune dépense, aucun commit, aucune écriture hors de ce rapport, de son compagnon et du bac à
  sable. Suite complète des essais non lancée.

Relecteur : Claude Fable 5.2, agent neuf. Verdict : « relu, conforme ».
