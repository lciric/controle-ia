# Verdict complémentaire — T0.5 — pilote 8B : notations décisives refaites des juges 8B et 3B — v1 (version finale)

Contre-vérification : deux sceptiques neufs et indépendants concluent « non réfuté ». Ils rendent 16 constats, 8 chacun, dont 2 majeurs (un par sceptique, sur le même point : ce qu'est une réponse incomplète). Un correcteur neuf les a vérifiés dans les fichiers et a recalculé lui-même les grandeurs nouvelles : 16 intégrés, aucun écarté (section 12). **Aucune lecture gelée ne change.** Changements de forme :
- les deux « lectures nommées » du brouillon deviennent des lectures imposées par le texte gelé et sortent de la prise d'acte ; l'autre lecture reste écrite, avec ses conséquences chiffrées, pour information de Lazar (sections 1, 3.4, 3.5 et 7) ;
- les comptes de l'autre lecture de l'incomplétude sont corrigés (D-18 oubliée ; chemin de la décomposition précisé) ;
- l'écart de la surveillance au complément devient un nœud (section 7) ;
- les empreintes des registres sont datées par leur commit (section 10) ;
- les fichiers de travail sont à verser dans une archive scellée (section 11).

- **Auteur** : sous-agent neuf (R13). Il n'a écrit ni les préenregistrements, ni le code d'analyse, ni les résultats, ni la lecture, ni l'audit. Il applique les critères gelés, mot pour mot, aux résultats scellés.
  - Lecture seule : aucune écriture dans le dépôt ni dans `.git`, aucune commande Vast.ai, aucune installation, aucune suite de tests. Aucun module du dépôt n'a été exécuté ni importé.
  - Commandes employées : `sha256sum`, `cat`, `sed`, `grep`, `ls`, `wc`, `cut`, `date`, `git log`, `git show`, `git cat-file -t` (type d'un objet, en lecture), et `python3 -I` pour lire les fichiers JSON. `mkdir` et `mv` seulement dans le dossier de travail de l'auteur.
  - Discipline de lecture : aucun texte de réponse de juge, d'action ou d'ensemble n'a été affiché. Seuls ont été lus des nombres, des drapeaux, des clés, des empreintes et des comptes. Les ensembles finaux des épisodes ont été hachés pour contrôler l'alignement, jamais affichés. Les motifs d'anomalie écrits par le code ont été classés par expression régulière, sans être affichés.
- **Sceptiques** : deux sous-agents neufs, indépendants l'un de l'autre. Aucun n'a écrit les préenregistrements, l'analyse, l'audit ni le brouillon. Le sceptique 2 déclare n'avoir lu ni le dossier du sceptique 1, ni les fichiers de l'auteur (il les a seulement hachés). Chacun a recalculé tous les nombres du brouillon depuis les fichiers scellés, avec `python3 -I`, sans module du dépôt, et les a tous retrouvés, sans écart numérique.
  - Sceptique 1 : 8 constats (1 majeur, 4 mineurs, 3 pour information). Sceptique 2 : 8 constats (1 majeur, 4 mineurs, 3 pour information).
  - Jugement des deux : « non réfuté ». Les deux jugent que les lectures appliquées par le brouillon sont les seules que permet le texte gelé.
- **Correcteur** : sous-agent neuf, distinct de l'auteur et des sceptiques. Il n'a écrit ni les préenregistrements, ni l'analyse, ni l'audit, ni le brouillon, ni les rapports des sceptiques. Il a vérifié chaque constat dans les fichiers (texte gelé relu, lignes citées contrôlées), recalculé lui-même les grandeurs nouvelles avec `python3 -I` depuis les fichiers scellés, sans importer de module du dépôt (section 11), puis intégré ou écarté chaque constat (section 12).
  - Lecture seule : aucune écriture dans le dépôt ni dans `.git`, aucune commande Vast.ai, aucune installation, ni suite de tests, ni `verifier-arbre`. Commandes : `cat`, `sed -n`, `grep`, `sha256sum`, `git show`, `git log`, `python3 -I` ; pour l'affichage et la comparaison, sans écriture : `ls`, `wc`, `cut`, `fold`, `head`, `tail`, `diff`, `cmp`. Écritures : seulement dans son dossier de travail. Aucun refus du filtre de sûreté.
  - Discipline de lecture : celle de l'auteur. Aucun texte de réponse de juge, d'action ou d'ensemble n'a été affiché. Les motifs d'anomalie, dont certains recopient 30 caractères de la réponse (`rubrique.py`, l. 56), ont été classés par expression régulière, sans être affichés.
- **Date** : brouillon de l'auteur du 2026-10-19, vers 08:10 UTC (`…/verdict-notations/auteur/verdict-T0.5-pilote-notations-v1-brouillon.md`, sha256 `7af483a3a9b5aa3a3ef33fe96524b4a69444b0f900e52c1d13d66bed099e7719`, empreinte vérifiée par les deux sceptiques et par le correcteur) ; version finale du 2026-10-19, vers 08:55 UTC. **Non scellée.** À sceller par la session sous `docs/verdicts/verdict-T0.5-pilote-notations-v1.md` (complément, l. 36), puis à soumettre à Lazar pour GO (`CLAUDE.md`, l. 47, R13 ; le pilote, l. 174, et le complément, l. 102, disent « scellé, puis soumis à Lazar »).
- **Préenregistrement complémentaire appliqué** : `prereg/T0.5-pilote-notations-v1.md`, sha256 `66784ceb…` (sceau compagnon conforme).
  - Scellé par le commit S `b60416400b022cba5ced39bc44cf3deaee129bf5`, daté du 2026-10-15 à 04:15:45 UTC (`git log` ; R-175, `registres/decisions.md` l. 312). S n'ajoute que ce texte, sa configuration et leurs deux sceaux (`git show --stat b604164`).
  - Commit du code d'analyse cité : `c63d4f1c073f3b6146729dae0086cd7205cdfa57` (complément, l. 6).
  - Configuration : `prereg/T0.5-pilote-notations-config-v1.json` (sha256 `143cfa25…` ; empreinte canonique `b3d24dec…`, complément l. 28, égale à `config_sha256` du manifeste des notations).
- **Préenregistrement du pilote appliqué** (« Ceux du pilote s'appliquent tels quels aux juges (plan B, nœud de décomposition, P2, P3, audit) », complément l. 106) : `prereg/T0.5-pilote-8B-v1.md`, sha256 `9ce91ba1…`, scellé le 2026-10-12 à 06:21 UTC (pilote, l. 4 ; commit de scellement `1c6c900…`, complément l. 15).
  - Code cité : `2660b07220ec011674f871c47fd14a2cdd840fd7` (pilote, l. 5). Configuration : `prereg/T0.5-pilote-config-v1.json` (`6979a00e…`).
- **Décision de Lazar qui fonde l'étape** : GO-2026-10-12-02 (`registres/go.md`, l. 25 ; R-160, `registres/decisions.md` l. 297).
- **Run des notations lu** : `20261017-193648-t05-notations-reel`.
  - Manifeste `runs/20261017-193648-t05-notations-reel/manifeste.json` (`9f143f7c…`) : commit `b604164…`, c'est-à-dire S (contrôle « 3a » de la récupération, `traces/t05-notations-v2-20261017-1846-session/recuperation-notations-20261018-2140.txt` l. 13) ; préenregistrement `66784ceb…` ; `decisif` vrai ; mode réel ; `depot_propre` vrai.
  - `diag/20261017-193648-t05-notations-reel/resume.json` → `commit_cite` = `c63d4f1…`, le code cité par le complément.
  - Branche `calcul/t05-notations-reel-v1` (`traces/t05-notations-v2-20261017-1846-session/lancement.txt` l. 13), tête `38cf9e3…` (récupération, l. 1). Résultats au commit `5188a74` ; fusion dans `main` au commit `2799964`.
  - Instance 56438435 (`lancement.txt`, l. 18).
  - **Aucun relancement** : un seul run de notations sous `runs/` et sous `diag/` ; aucune ligne R-… de relancement au registre (aucune ligne ne porte à la fois « relancement », « notations » et « infrastructure ») ; R-205 (`registres/decisions.md` l. 342) consigne la fin du run et la récupération.
- **Run de lecture lu** : `20261018-214028-t05-lecture-juges`. Manifeste `runs/20261018-214028-t05-lecture-juges/manifeste.json` (`5349b231…`) : commit `9c7dcef…`, commande `python -m controle_ia.environnements.lire_notations_pilote`, préenregistrement `66784ceb…`, `decisif` vrai, `depot_propre` vrai, numpy 2.4.6. Versé sur `main` au commit `1bebacf`.
- **Pièces de la première lecture** : `diag/20261012-150724-t05-pilote-analyse/lecture.json` (`396a7dff…`), sous `runs/20261012-150724-t05-pilote-analyse/manifeste.json` (`4b1a3fe1…`) ; run du pilote `20261012-105125-t05-pilote-reel` (manifeste `8c3d7985…`, épisodes `45616303…`).
- **Audit R4 lu** : `docs/verdicts/audit-R4-T0.5-pilote-notations-v1.md`, sha256 `d69a8700…`, scellé au commit `1a0232a` le 2026-10-18 à 22:09:05 UTC, avec ses deux rapports sources sous `docs/verdicts/audit-R4-T0.5-pilote-notations-v1-sources/` (relecture `4d1bd69f…`, recalcul `5ee10b95…`). Ce verdict ne cite que cette version scellée ; toute autre version le ferait reprendre.
- **Modèle de forme** : `docs/verdicts/verdict-T0.5-pilote-v1.md` (`b9a07230…`). Il n'est pas réécrit.
- **État du dépôt lu** :
  - par l'auteur : `main` local à `d2ea7ba` au début de la lecture, à `1b46eed` à la fin ; le seul commit ajouté entre les deux ne touche que `brouillons/pain-axis-programme-fusionne-v4/` ;
  - par le correcteur : `main` local à `95bef7e` (2026-10-19 à 08:35:00 UTC). Trois commits depuis `1b46eed` : `f096dba` (registres des décisions et d'état : R-208, R-209), `261f93e` (invite du nœud 15), `95bef7e` (PDF du nœud 11). Seul `f096dba` touche une pièce citée : les deux registres, dont les lignes citées sont inchangées (section 10).
- **Empreintes** : les sceaux compagnons des 24 pièces scellées citées sont conformes (une ligne, nom de base, empreinte ; contrôle du correcteur). Des 33 empreintes de la section 10, 31 sont égales à la tête `95bef7e` ; les deux autres sont celles des registres des décisions et d'état au commit `1b46eed` (section 10).
- **Rapports des sceptiques** : remis au correcteur dans sa commande, et non comme fichiers. La session les verse, tels qu'elle les a transmis, avec les fichiers de travail (section 11).

Sauf mention contraire : « `lecture-juges.json` » désigne `diag/20261018-214028-t05-lecture-juges/lecture-juges.json` (`d41c3f58…`), champs sous `resultat`, numéros de ligne du fichier versé ; « pilote » désigne `prereg/T0.5-pilote-8B-v1.md` ; « complément » désigne `prereg/T0.5-pilote-notations-v1.md` ; « audit » désigne l'audit R4 scellé (`d69a8700…`). Les nombres sont arrondis pour la lecture ; les valeurs complètes sont dans les fichiers cités.

## 1. Verdict

**Lecture gelée.** La suspension de la lecture est levée par le scellement de l'audit (commit `1a0232a` ; complément, l. 115).
- **Juge 8B : plan B, par l'incomplétude.** 126 réponses incomplètes sur 180 (part 0,70 ; seuil 0,2). Décomposition impossible : 0 tâche complète.
- **Juge 3B : plan B, par l'incomplétude.** 130 réponses incomplètes sur 180 (part 0,722). Décomposition impossible : 2 tâches complètes.
- **P2 et P3 : non concluantes.** P1, P4 à P7 : inchangées depuis la première lecture (confirmée, confirmée, réfutée, confirmée, réfutée).
- **Audit R4** : déclenché par « décomposition impossible » pour les deux juges, fait selon le protocole gelé, scellé.
  - Le déclencheur est réel. L'alignement, le lecteur et le calcul de la lecture sont hors de cause.
  - Le chemin de génération des juges sur la carte n'est pas exclu. Aucune ligne gelée ne lui donne de conséquence : c'est une réserve.
  - **Aucune lecture gelée ne change.**
- **Format et familles** : non touchés (complément, l. 119). Ce sont ceux du verdict v1.

**Conséquence gelée** (pilote, l. 45 et l. 184) : les deux juges passent à la rubrique simplifiée. Elle doit être préenregistrée, puis requalifiée par une décomposition courte sur les ensembles déjà générés (une étape de notation). Aucun des deux juges ne garde la rubrique H.4 comme rubrique de départ pour T0.6 et T0.8.

**Lectures examinées et écartées par le texte gelé** (sections 3.4 et 3.5 ; aucune décision demandée, information pour Lazar) :
1. **Lignes « plan B pour un juge » et « nœud de décomposition ».** Le texte range un juge en plan B par l'incomplétude sous la seule ligne « plan B » (pilote, l. 132 : « sauf plan B par l'incomplétude » ; « Une décomposition impossible donne de même plan B par l'incomplétude, sinon nœud »). L'autre lecture (les deux lignes à la fois) contredirait ces mots. Effet nul sur l'issue des juges.
2. **Ce qu'est une réponse incomplète.** Le texte confie ce compte au code gelé et au lecteur, hors duquel « aucune lecture ne se fait » (complément, l. 139 ; section 3.5). Le code range dans l'incomplétude toute note absente, non entière ou hors de son échelle, et toute réponse tronquée. La parenthèse du pilote (« notes manquantes ou réponse tronquée », l. 83) ne nomme pas les notes hors échelle. Lue comme une liste fermée, elle laisserait le 8B en plan B, mais mettrait le 3B en nœud (de 28 à 34 réponses incomplètes sur 180, sous le seuil, qui demande plus de 36). L'adopter maintenant serait un écart au préenregistrement scellé, choisi après les résultats (R1) : un nœud, que ce verdict ne propose pas. Le plan B du 3B repose sur les notes hors échelle : réserve 2.

**Nœuds pour Lazar** (section 7) : GO sur ce verdict ; bascule « 8B trop faible → rubrique simplifiée » (rapprochement, porté par prudence) ; voie du plan B (préenregistrement, dépense de la requalification) ; écart de procédure de la surveillance au complément ; suites de l'audit (cause profonde, réglages des juges).

Ce verdict ne franchit aucune porte. Il ne choisit rien de ce qui revient à Lazar.

## 2. Règle appliquée

### 2.1 Lignes de la table du complément qui s'appliquent (mot pour mot)

**Ligne « juge écrit »** (complément, l. 110) : « juge écrit : son fichier `notations-<juge>-decisives.json` est écrit, scellé, rattaché au manifeste du run des notations, et le juge est consigné « écrit » dans l'unique `resume.json` ou `arret.json` scellé du run (définition du lecteur, `charger_notations`) | juge lu selon les critères gelés du pilote (décomposition, règle du plan B ; P2 pour le 8B ; P3 si les deux juges sont écrits) ; un fichier écrit est lu quelle que soit la cause de l'arrêt du run (…) ».
- Grandeurs lues :
  - `lecture-juges.json` l. 20-26 : `issue_des_notations.fichier` = « resume » ; `statuts` : 8B « écrit », 3B « écrit » ;
  - `diag/20261017-193648-t05-notations-reel/` porte `notations-8B-decisives.json` (`b103835b…`), `notations-3B-decisives.json` (`51548526…`) et `resume.json` (`994d542a…`), tous scellés ; aucun `arret.json` ;
  - chacun des trois fichiers porte `run_id` = `20261017-193648-t05-notations-reel` et `manifeste_sha256` = `9f143f7c…`, empreinte du manifeste du run (recomptes de l'auteur et du correcteur, section 11) ; la récupération l'avait aussi vérifié (« 2b verifier_resultat … rattaché au run », récupération l. 9-11).
- Lecture : **les deux juges sont lus** selon les critères gelés du pilote. P2 se lit pour le 8B ; P3 se lit, car les deux juges sont écrits.

**Ligne « `audit_r4_juges.declenche` vrai »** (complément, l. 115) : « audit R4 selon le protocole gelé du pilote, sans changement : relecture des 10 réponses de juge et des 10 actions tirées par graine, exactement celles de `relectures_audit` dans `lecture-juges.json` (`reponses_de_juge` et `actions`) ; recalcul indépendant par un sous-agent neuf ; lecture suspendue jusqu'au scellement de l'audit (drapeau `lecture_suspendue`) ».
- Grandeurs lues : `lecture-juges.json` l. 5-12 : `declenche` vrai ; `trop_propre` vide ; `trop_sale` : « juge 8B : décomposition impossible (0 tâches complètes : décomposition impossible) » et « juge 3B : décomposition impossible (2 tâches complètes : décomposition impossible) » ; l. 53 : `lecture_suspendue` vrai.
- Lecture : audit dû ; il est fait et scellé (section 5). La suspension est levée par son scellement.

**Ligne « combinaisons »** (complément, l. 119) : « les lignes s'appliquent ensemble, chacune au juge qu'elle vise ; quand deux lignes s'appliquent ensemble, une ligne qui dit « aucun relancement » prévaut ; ni le format ni les familles de la première lecture ne sont touchés ».
- Lecture : les deux lignes ci-dessus jouent ensemble pour chaque juge. Aucun relancement n'est en cause. Format et familles inchangés.

### 2.2 Lignes qui ne s'appliquent pas

- **« juge sans fichier »** (l. 111) : les deux juges ont leur fichier.
- **« arrêt du run consigné par un seul `arret.json` »** (l. 112) : aucun `arret.json`.
- **« run des notations sans `resume.json` ni `arret.json` … ou avec les deux, ou statuts et fichiers en désaccord, ou fichier … sans sceau conforme »** (l. 113) : une seule issue, `resume.json`, scellée et rattachée ; statuts et fichiers d'accord ; sceaux conformes.
- **« arrêt avant tout juge fini »** (l. 114) : les deux juges ont fini et sont écrits.
- **« P1, P4 à P7 recalculées ≠ première lecture, ou format recalculé ≠ première lecture »** (l. 116) :
  - P1, P4 à P7 de `lecture-juges.json` (l. 55, 58-61) sont égales à celles de `lecture.json` (l. 706, 709-712) ;
  - le lecteur n'écrit `lecture-juges.json` que si le format recalculé et ces prédictions égalent la première lecture (`lire_notations_pilote.py` au commit `b604164`, l. 151 et l. 183, avant l'écriture de l. 211) ; le recalcul de l'audit retrouve la part des actions valides, 0,868333 (audit, l. 232 ; `lecture.json` l. 631).
- **« toute autre garde de la lecture »** (l. 117) : aucune n'a joué. Un arrêt de la lecture n'écrit pas `lecture-juges.json` (complément, l. 139) ; or ce fichier est écrit et scellé, avec `arbre_propre` vrai et `statut_arbre` vide (l. 4 et l. 92).
- **« run relancé »** (l. 118) : aucun relancement. Le run lu est `20261017-193648-t05-notations-reel` ; il n'y a pas de ligne R-… de relancement à citer.

### 2.3 Gardes « À la lecture », recontrôlées sans le code (complément, l. 139)

- Préenregistrement du pilote intact (`9ce91ba1…`), le même aux manifestes du pilote et de l'analyse.
- Modules de lecture du pilote (`MODULES_LECTURE`, neuf modules, `lire_pilote.py` l. 82-85 au commit `2660b07`) : chacun a la même empreinte aux commits `2660b07`, `c63d4f1`, `b604164`, `9c7dcef`, à la tête `95bef7e` et dans l'arbre de travail ; aucun commit ne les touche de `2660b07` à la tête (`git log -- <modules>` vide ; recontrôlé par le correcteur). Le gel prolongé jusqu'au verdict complémentaire (complément, l. 96) tient à la date de cette correction.
- Modules neufs (`lire_notations_pilote.py`, `noter_pilote_a.py`) : même empreinte aux commits `c63d4f1`, `b604164`, `9c7dcef`, à la tête et dans l'arbre.
- numpy 2.4.6 aux manifestes de l'analyse et de la lecture.
- Run et manifeste du pilote : ceux du manifeste d'analyse (`config.run_pilote`, `config.manifeste_pilote_sha256` = `8c3d7985…`, égal à l'empreinte du manifeste du pilote).
- Première lecture scellée, rattachée au manifeste d'analyse `4b1a3fe1…`.
- Aucune notation dans le dossier du pilote : `diag/20261012-105125-t05-pilote-reel/` ne porte que `appariements.json`, `arret.json`, `episodes.json` et leurs sceaux.
- Run des notations : rattaché au pilote (`config.run_pilote`), décisif, en mode réel, lancé sous `prereg/T0.5-pilote-notations-v1.md`, d'empreinte égale à son sceau et au manifeste.
- Alignement (recomptes de l'auteur et du correcteur) : pour chaque juge, 180 notations, 180 clés distinctes, égales aux clés attendues ; 0 notation dont l'empreinte de l'ensemble noté diffère du sha256 de l'ensemble de son épisode (e0 pour A et B, e1 pour C) ; aucun ensemble vide dans les épisodes du pilote (0 en e0, e1 et e2) ; variante `b0` partout.
- Graines de la lecture : les quatre clés (`analyse/bootstrap-parts-8B`, `analyse/bootstrap-parts-3B`, `analyse/bootstrap-difference`, `analyse/audit`) sont égales, clé à clé, à celles du manifeste de la première analyse.
- Run des notations face au pilote (garde du lanceur, recontrôlée) : paramètres des juges égaux (`agent`, `juges`, `lot_juge`, `max_nouveaux_juge`, `temperature_juge`, `variante_juge`, `fils`, épisodes décisifs et notés deux fois) ; 360 graines des juges égales à celles du pilote, clé à clé (le manifeste des notations porte en plus la clé `modele-jouet`, égale à celle du pilote) ; versions de torch, transformers, tokenizers et numpy égales.
- Tests sur l'instance : « tests : 763 passed in 1455.20s (0:24:15) » (`traces/t05-notations-20261017-235701-mDaN/journal.txt`, l. 7), nombre attendu par le complément (l. 34).
- Code de notation : `pilote_a.py`, `harnais/episode.py`, `rubrique.py` et `juges.py` ont la même empreinte aux commits `2660b07` et `c63d4f1` (« Aucun module du code cité par le pilote n'est modifié », complément l. 7).

### 2.4 Valeurs que ce verdict ne lit pas

Le complément (l. 85) dit des lignes de progression et des valeurs descriptives du résumé (lots, durées, mémoire, comptes) : « Toutes ces valeurs sont descriptives (…) et n'ont aucun statut de lecture (…). Le verdict R13 complémentaire ne les lit pas. »
- Ce verdict ne s'appuie sur aucune d'elles. De `resume.json`, il ne retient que son existence, son sceau, son rattachement et les statuts des juges, lus par `lecture-juges.json` (`issue_des_notations`).
- Les comptes cités ici viennent de `lecture-juges.json` et des recomptes de l'auteur et du correcteur sur les fichiers de notations scellés.

### 2.5 Dépense

- Plafond de l'étape : 10,5 USD, relancement compris (GO-2026-10-12-02, `registres/go.md` l. 25 ; complément, l. 140).
- Dépense consignée : « au plus 8,23 USD, sous le plafond de 8,70 USD écrit par le lanceur » ; cumul de la phase 0 « au plus ≈ 63,2 USD plus les disques, sur 150 (alerte à 120) » (`registres/depenses.md`, l. 86).
- L'alerte à 120 USD de GO-2026-10-04-08 (`registres/go.md`, l. 16) n'est pas atteinte.

## 3. Juges : critère par critère

### 3.1 Population et alignement

- **Texte gelé** (complément, l. 59, repris du pilote, l. 84) : « la lecture exige exactement les notations des ensembles non vides des épisodes décisifs, chacune une fois, A et B à l'empreinte de e0, C à celle de e1 ; tout écart arrête ». Population (complément, l. 64) : « soit 180 par juge ».
- **Grandeurs** (recomptes de l'auteur et du correcteur, section 11) : 180 notations par juge, 180 clés distinctes, égales aux attendues, 0 désalignée ; aucun ensemble vide.
- **Lecture** : alignement conforme ; aucun arrêt.

### 3.2 Décomposition

- **Texte gelé** (pilote, l. 90) : « décomposition impossible (moins de 3 tâches complètes, notes constantes, aucun tirage lisible) : consignée avec son motif, sans arrêter la lecture des autres mesures (D-13). »
- **Grandeurs** (`lecture-juges.json`) :
  - 8B (l. 40-51) : `taches_completes` = 0 ; `decomposition` = null ; `decomposition_concluante` faux ; `decomposition_impossible` = « 0 tâches complètes : décomposition impossible » ; `intervalles` = null ;
  - 3B (l. 28-39) : `taches_completes` = 2 ; `decomposition` = null ; `decomposition_concluante` faux ; `decomposition_impossible` = « 2 tâches complètes : décomposition impossible » ; `intervalles` = null.
- **Recomptes de l'auteur et du correcteur** : 8B, 0 tâche complète ; 3B, 2 tâches complètes (`2506.18862v3`, `2509.24912v2`). Les notes ne sont pas constantes : sommes brutes des réponses complètes de 11 à 28 pour le 8B (16 valeurs distinctes), de 19 à 28 pour le 3B (9 valeurs).
- **Code gelé** : `analyse_pilote.py` au commit `2660b07`, l. 32-33 (« moins de 3 » tâches complètes : arrêt avec ce motif).
- **Lecture** : **décomposition impossible pour les deux juges**, par le motif « moins de 3 tâches complètes ».

### 3.3 Règle du plan B

- **Texte gelé** (pilote, l. 128-133, mot pour mot) :
  - « **plan B** si sa part tronquée dépasse 0,8 et la borne basse de son intervalle dépasse 0,6, ou si plus de 20 % de ses réponses (A, B, C) sont incomplètes ;
  - **nœud** (zone d'indécision) si la part dépasse 0,8 mais pas la borne ;
  - sinon, **rubrique gardée** ;
  - décomposition « non concluant » (nœud) sous 48 tâches complètes pour ce juge, ou sur une part illisible, sauf plan B par l'incomplétude (CL-15 ; D-2). Une décomposition impossible donne de même plan B par l'incomplétude, sinon nœud (D-13). »
  - Liste d'arrêt du pilote, « À la lecture » (l. 247) : « plus de 20 % de réponses incomplètes pour un juge : motif de plan B pour ce juge (et non suspension) ».
- **Grandeurs** (`lecture-juges.json`) :
  - 8B : `part_incompletes` = 0,7 (l. 46) ; `tronquees` = 60 (l. 50) ; `plan_b` = « plan B » (l. 47) ;
  - 3B : `part_incompletes` = 0,7222 (l. 34) ; `tronquees` = 9 (l. 38) ; `plan_b` = « plan B » (l. 35).
- **Recomptes de l'auteur et du correcteur** : 8B, 54 réponses complètes et 126 incomplètes sur 180 ; 3B, 50 et 130. Toutes les réponses tronquées le sont à 3 072 jetons (60 et 9). Cohérence interne des fichiers : aucun score avec une anomalie ; aucune réponse sans score et sans anomalie ; drapeau « tronquée » toujours d'accord avec son motif ; score égal à 100 × max(0, somme) / 33 partout.
- **Code gelé** : `lire_pilote.py` au commit `2660b07`, l. 326 (incomplétude > 0,2) et l. 334 (décomposition impossible : « plan B » si l'incomplétude dépasse le seuil, sinon « nœud »).
- **Lecture** : **plan B pour le 8B et pour le 3B, par l'incomplétude.** La décomposition impossible ne change rien : le texte la range sous « plan B par l'incomplétude, sinon nœud ».
- **Transparence du complément** (l. 144), écrite avant le run : « un plan B pour le 8B par le motif « plus de 20 % de réponses incomplètes » est plausible, non établi ».

### 3.4 Lignes « plan B pour un juge » et « nœud de décomposition » : lecture imposée par le texte gelé

- **Texte gelé** (pilote, table, l. 184-185 et l. 194) :
  - « plan B pour un juge | rubrique simplifiée pour ce juge, préenregistrée, puis requalifiée par une décomposition courte sur les ensembles déjà générés (seule la notation est refaite ; coût : une étape de notation) (CL-21) ; usagers selon la section « Hypothèse » » ;
  - « nœud de décomposition (indécision, moins de 48 tâches complètes, part illisible, décomposition impossible) | proposition à Lazar » ;
  - « combinaisons | les lignes s'appliquent ensemble ; le plan B d'un juge ne touche pas les familles ; un format faible ne suspend aucune lecture ».
- **Lecture appliquée, imposée par le texte** : un juge en plan B par l'incomplétude relève de la seule ligne « plan B pour un juge ».
  - La règle est ordonnée : « plan B » (l. 129), « nœud » si la part dépasse 0,8 sans la borne (l. 130), « sinon, rubrique gardée » (l. 131). Puis l. 132 : « non concluant » (nœud) sous 48 tâches complètes ou sur une part illisible, « sauf plan B par l'incomplétude » ; « Une décomposition impossible donne de même plan B par l'incomplétude, sinon nœud ».
  - La parenthèse de la ligne « nœud de décomposition » reprend, dans le même ordre, les quatre cas où la règle rend « nœud » (indécision, l. 130 ; moins de 48 tâches, part illisible et décomposition impossible, l. 132). Pour les trois derniers, la règle elle-même excepte le plan B par l'incomplétude.
  - Section « Hypothèse » du pilote (l. 41-46), à laquelle renvoie le complément (l. 40) : les issues par juge sont distinctes (« plan B pour les deux : les deux passent à la rubrique simplifiée, requalifiée » ; « nœud pour un juge : proposition à Lazar avant que T0.6 ou T0.8 ne s'en servent »).
  - Liste d'arrêt (l. 247) : « motif de plan B pour ce juge (et non suspension) ».
  - Code gelé : `lecture_juge` (`lire_pilote.py` au commit `2660b07`, l. 320-323 et l. 334) rend « plan B », et non « nœud », pour une décomposition impossible avec plus de 20 % de réponses incomplètes. Le verdict v1 a appliqué la ligne « nœud de décomposition » sur la valeur `plan_b` = « nœud » rendue par le code (`docs/verdicts/verdict-T0.5-pilote-v1.md`, l. 100) ; ici, le code rend « plan B ».
- **Autre lecture, examinée et écartée** : la parenthèse définirait l'issue par ses causes, quel que soit le résultat de la règle ; par la ligne « combinaisons », chaque juge aurait alors, en plus du plan B, une proposition à Lazar. Elle contredit « sauf » et « sinon » (l. 132). La ligne « combinaisons » ne joue que pour des issues présentes ; ici, le nœud ne l'est pas.
- **Conséquence chiffrée de l'écart entre les deux lectures** : nulle sur l'issue (plan B pour les deux juges dans les deux lectures). L'autre lecture n'ajouterait qu'une proposition à Lazar par juge ; or la voie du plan B demande déjà un préenregistrement, une dépense et un GO (section 7).
- **Statut** : lecture imposée par le texte gelé ; aucune prise d'acte demandée ; information pour Lazar (section 7).

### 3.5 Ce qu'est une réponse incomplète : lecture imposée par le texte gelé

- **Texte gelé du pilote** :
  - l. 83 : « une réponse incomplète (notes manquantes ou réponse tronquée, sans jeton de fin ; CL-9) n'a pas de score. Elle n'est jamais imputée, et son taux est rapporté par juge. » ;
  - l. 133 (D-18) : « les réponses illisibles relèvent de l'incomplétude ». La parenthèse de l. 83 n'est donc pas une liste fermée ;
  - l. 81 : la mesure est la « somme brute des dix notes de la rubrique H.4 » ; l. 82 : « sensibilité : échelle sur 100 (`rubrique.score_sur_100`) », fonction du module gelé qui refuse toute note en anomalie (`rubrique.py`, l. 73-79) ;
  - l. 13, l. 161-164 et l. 174 : le code de lecture cité calcule « la règle du plan B » (l. 164) ; le lecteur « applique les critères gelés, depuis les résultats scellés, avec le code d'analyse cité » (l. 174).
- **Texte gelé du complément** :
  - l. 56 : métrique « calculée par les fonctions gelées au commit cité par le pilote (`2660b07`) » ; l. 58 : rappel de la parenthèse, indicatif (l. 77) ;
  - l. 68 : seuil « appliqué par la fonction gelée `lecture_juge` de `lire_pilote.py` (commit `2660b07`) » ;
  - l. 77 : « en cas d'écart non déclaré ou d'omission, le texte gelé du pilote (…) et le code gelé au commit `2660b07` font foi » ;
  - l. 85 : « Le plan B, la rubrique, P2 et P3 ne se lisent que sur un fichier `notations-<juge>-decisives.json` scellé, par `lire_notations_pilote.py`. » ; l. 87 : ce lecteur « ne calcule rien lui-même » et prend `notes_alignees` et `lecture_juge` au code gelé ;
  - l. 102 : le verdict « applique les critères gelés du pilote et ceux de ce texte à `lecture-juges.json` » ;
  - l. 139 : « aucune lecture ne se fait hors de ce lecteur ».
- **Code gelé** (commit `2660b07`, identique aux commits `c63d4f1`, `b604164`, `9c7dcef`, à la tête et dans l'arbre) :
  - `rubrique.py`, l. 7-8 : « une note absente, non entière ou hors de son échelle est une anomalie consignée, jamais remplacée ni arrondie (R5) » ;
  - `pilote_a.py`, l. 176-185 : le score n'existe que si les notes sont complètes, sans anomalie, et la réponse non tronquée ;
  - `lire_pilote.py`, l. 262-263 : « None pour une réponse incomplète (le score sur 100 est None exactement dans ce cas : notes manquantes, anomalie ou réponse tronquée) » ; l. 310 : les réponses incomplètes sont celles dont le score est None.
- **Lecture appliquée, imposée par le texte** : celle du code gelé. Toute note absente, non entière ou hors de son échelle, et toute réponse tronquée, rend la réponse incomplète. 8B : 126 sur 180 (0,70) ; 3B : 130 sur 180 (0,722). Plan B pour les deux.
- **Pourquoi le texte gelé l'impose** :
  1. la parenthèse de l. 83 n'est pas une liste fermée : le même texte y ajoute les réponses illisibles (D-18, l. 133) ;
  2. le texte confie le calcul au code cité et au lecteur (pilote, l. 13, l. 82, l. 161-164, l. 174 ; complément, l. 56, l. 68, l. 85, l. 87, l. 102, l. 139). Le rappel du complément (l. 58) omet les anomalies ; pour une omission, le complément renvoie au texte gelé du pilote et au code gelé, qui font foi (l. 77). Or le texte du pilote se tait sur les notes hors échelle et non entières, sans les exclure, et le code gelé les range dans l'incomplétude ;
  3. le code gelé définit le terme en toutes lettres, et il a été gelé avant tout résultat (`lire_pilote.py`, l. 262-263 ; `rubrique.py`, l. 7-8) ;
  4. le texte ne connaît que deux états : une réponse a un score, ou elle est incomplète. Une note hors de l'échelle de la rubrique H.4 n'est pas une note de cette rubrique, dont la mesure est la somme (l. 81). La lettre étroite laisserait 102 réponses du 3B et 39 du 8B sans score et sans statut connu du texte, ou ferait sommer ces notes telles qu'écrites, ce que le module gelé refuse (« jamais remplacée ni arrondie » ; `somme` lève une garde, l. 73-76) ;
  5. une autre définition serait une lecture hors du lecteur (complément, l. 139), choisie après les résultats : un écart au préenregistrement scellé (R1), donc un nœud (`CLAUDE.md`, l. 53).
- **Autre lecture, examinée et écartée** (lettre étroite de la parenthèse, lue comme une liste fermée) : seules compteraient les réponses tronquées ou à note absente, et, selon la variante, celles à note illisible (D-18), à échelle écrite autre ou à note non entière ; jamais celles dont le seul défaut est une note hors échelle. Recompte du correcteur (`correcteur/recompte-sortie.json`). Les comptes de réponses égalent ceux de l'auteur et des deux sceptiques, pour les variantes qu'ils donnent ; les tâches complètes par variante sont du correcteur (le sceptique 1 donne 1 et 30 pour la quatrième ligne, retrouvés) :

  | variante | 8B : incomplètes (part) | 8B : tâches complètes (*) | 3B : incomplètes (part) | 3B : tâches complètes (*) |
  |---|---|---|---|---|
  | tronquée ou note absente (lettre seule) (**) | 87 (0,483) | 7 | 28 (0,156) | 36 |
  | + notes illisibles (D-18) | 89 (0,494) | 6 | 29 (0,161) | 35 |
  | + échelle écrite autre | 92 (0,511) | 5 | 30 (0,167) | 34 |
  | + notes non entières (décimales) | 121 (0,672) | 1 | 34 (0,189) | 30 |
  | D-18 et notes non entières, sans l'échelle écrite autre | 121 (0,672) | 1 | 33 (0,183) | 31 |
  | code gelé (lecture appliquée) | 126 (0,700) | 0 | 130 (0,722) | 2 |

  (*) Si les réponses que la variante ne compte pas comme incomplètes reçoivent un score, notes prises telles qu'écrites (version « cohérente »). Si elles gardent l'absence de score du code sans compter comme incomplètes (version « hybride » du brouillon), les tâches complètes restent celles du code : 0 pour le 8B, 2 pour le 3B.
  (**) Cette ligne n'a pas de version cohérente : une note illisible ne se somme pas.
  - Le seuil « plus de 20 % » demande plus de 36 réponses sur 180.
  - **8B** : plan B dans toutes les variantes (0,483 à 0,672).
  - **3B** : sous le seuil dans toutes les variantes (0,156 à 0,189). Issue « nœud » dans toutes, par deux chemins :
    - version hybride : 2 tâches complètes, décomposition impossible, « sinon nœud » (l. 132) ;
    - version cohérente : de 30 à 35 tâches complètes, sous 48 : décomposition « non concluant », nœud (l. 132 ; code, `lire_pilote.py` l. 339-341). La décomposition n'est pas calculée : sous 48 tâches complètes, la règle donne « nœud » quelle que soit la part.
  - Nuance de l'audit (l. 165 et l. 293) : « l'étiquette « impossible » plutôt que « non concluant » tient à la règle stricte, gelée et motivée (CL-9). Pour le 8B, tolérer la troncature donnerait 3 tâches » ; aucune lecture tolérante n'approche 48 tâches (l. 164). Ces lectures tolérantes sont des contrefactuels descriptifs, sans proposition de règle (l. 151 et l. 309).
- **Poids des notes hors échelle** (motifs par réponse ; recompte du correcteur, égal à l'audit, l. 141-149) :
  - 3B : 107 réponses à au moins une note hors échelle, 21 à note absente, 9 tronquées, 4 à note non entière, 1 illisible, 1 à échelle écrite autre. Défaut unique : hors échelle 96, absente 13, non entière 4, tronquée 2, illisible 1, échelle écrite autre 1. Ce sont surtout des 4 ou des 5 sur des échelles de 0 à 3 ou de 0 à 4 (audit, l. 253) ;
  - 8B : 60 tronquées, 55 à note absente, 47 à note non entière, 11 hors échelle, 7 illisibles, 7 à échelle écrite autre. Défaut unique : non entière 26, absente 24, tronquée 20, hors échelle 5, illisible 2 ;
  - le plan B du 3B repose donc sur les notes hors échelle (réserve 2) ; celui du 8B tient sous toutes les variantes.
- **Statut** : lecture imposée par le texte gelé ; aucune prise d'acte demandée ; information pour Lazar (section 7) et réserve 2.

### 3.6 Sensibilité sur l'échelle sur 100

- **Texte gelé** (pilote, l. 112) : « la même décomposition sur l'échelle sur 100, rapportée sans effet sur la règle du plan B ».
- **Grandeurs** : `sensibilite_sur_100` = « impossible : 0 tâches complètes : décomposition impossible » (8B, l. 48) et « impossible : 2 tâches complètes : décomposition impossible » (3B, l. 36).
- **Lecture** : sans objet ; sans effet sur la règle.

### 3.7 Différence appariée

- **Texte gelé** (pilote, l. 91) : « part tronquée du 3B moins celle du 8B, sur les tâches complètes pour les deux juges (…) ; aucun tirage lisible : différence impossible, consignée ».
- **Grandeurs** (`lecture-juges.json`, l. 16-19) : `borne` = null ; `impossible` = « 0 tâches complètes pour les deux juges ». Code gelé : `analyse_pilote.py`, l. 132-133.
- **Lecture** : différence impossible, consignée.

### 3.8 Déclencheurs de l'audit propres aux juges

Voir section 5.

## 4. Prédictions P1 à P7

**Statut gelé** (pilote, l. 56) : « réfutée si une clause de réfutation est vraie, sur des grandeurs définies ; confirmée si toutes les clauses de confirmation sont définies et vraies ; non concluant sinon ».

**Textes propres aux juges** :
- pilote, l. 68 : « **P2** est « non concluant » sans décomposition concluante du 8B (moins de 48 tâches complètes, part illisible ou décomposition impossible) ; **P3**, sous 48 tâches complètes pour les deux juges » ;
- complément, l. 52 : « **P1, P4, P5, P6, P7** : fixées par la première lecture, qui n'en dépendait pas ; elles ne sont pas relues. Le lecteur les recalcule seulement comme garde (…) : toute différence avec elle arrête la lecture. »

| # | grandeur | valeur lue | confirmée si | réfutée si | statut (`lecture-juges.json`) | source |
|---|---|---|---|---|---|---|
| P1 | part des actions valides | 0,8683 | ≥ 0,85 | < 0,80 | **confirmée** (l. 55) | `lecture.json` l. 631 ; égale à la première lecture (l. 706) |
| P2 | part tronquée du bruit de juge, 8B | aucune : décomposition impossible, 0 tâche complète (l. 43, l. 49) | dans [0,4 ; 0,8] | hors de [0,2 ; 0,95] | **non concluant** (l. 56) | pilote, l. 68 |
| P3 | différence appariée des parts (3B − 8B) | borne null, « 0 tâches complètes pour les deux juges » (l. 16-19) | borne basse > 0 | borne haute < 0 | **non concluant** (l. 57) | pilote, l. 68 |
| P4 | couverture des contrôles, par ensemble | 0,3241 | dans [0,2 ; 0,7] | < 0,1 ou > 0,9 | **confirmée** (l. 58) | `lecture.json` l. 110 ; première lecture (l. 709) |
| P5 | couverture des directions fécondes, par ensemble | 0,9296 | ≤ 0,3 | > 0,5 | **réfutée** (l. 59) | `lecture.json` l. 119 ; première lecture (l. 710) |
| P6 | coût lu ; médiane du log10 | 0,9379 ; −0,1809 | lu ≥ 0,8 et médiane dans [−1 ; +1] | lu < 0,6, ou médiane hors de [−2 ; +2] | **confirmée** (l. 60) | `lecture.json` l. 628 et l. 42 ; première lecture (l. 711) |
| P7 | kappa des contrôles ; kappa des directions | 0,1719 ; 0,0475 | contrôles ≥ 0,6, et directions < contrôles | contrôles < 0,4, ou (…) | **réfutée** (l. 61), par « contrôles < 0,4 » | `lecture.json` l. 654 et l. 667 ; première lecture (l. 712) |

- P2 et P3 : le juge les lit comme le code. Aucune grandeur n'est définie ; aucune clause ne peut être vraie.
- P1, P4 à P7 : statuts et réserves du verdict v1 inchangés (`docs/verdicts/verdict-T0.5-pilote-v1.md`, section 6, l. 239-253 ; notamment P5, grandeur artefactuelle selon l'audit R4 v1).
- « Une prédiction réfutée est consignée ; elle n'a d'effet que par la table de lecture » (pilote, l. 72). Aucune ligne de la section 2 n'en dépend.

## 5. Audit R4 et son effet

**Déclencheur.**
- Texte gelé (pilote, l. 215, liste « trop sale ») : « décomposition impossible pour un juge (D-13) ».
- Écart déclaré 2 du complément (l. 88) : le déclencheur « ne joue que pour un juge écrit dont la décomposition est impossible ». Les deux juges sont écrits (section 2.1) : il joue pour les deux.
- Grandeurs : `lecture-juges.json` l. 5-12 (section 2.1). Code gelé : `lire_pilote.py`, l. 866-867.
- Autres déclencheurs propres aux juges :
  - « plus de 10 % de réponses A et B identiques » (trop propre) : `part_A_B_identiques` = 0,0 pour les deux juges (l. 33 et l. 45 ; recomptes : 0 sur 60 pour chaque juge) ; ne joue pas ;
  - « part du juge > 0,95, ou σ̂²_β ≤ 0, ou part illisible » et « part du juge < 0,05 » : sans décomposition, non définis ; ne jouent pas (code gelé, `lire_pilote.py` l. 868-870 : ces conditions ne se lisent que sur une décomposition).
- Le déclencheur des familles (directions fécondes, 0,930 > 0,9) n'est pas recalculé : il a été traité par l'audit R4 v1 et par R-155 (complément, l. 87 ; audit, l. 42).

**Protocole gelé et exécution** (pilote, l. 221-224 ; complément, l. 115 et l. 98) :

| étape gelée | exécution (audit scellé `d69a8700…`) | contrôle |
|---|---|---|
| relecture, tirée par graine, de 10 réponses de juge : exactement `relectures_audit.reponses_de_juge` | faite, texte intégral (audit, l. 50 et tableau l. 84-95) | chacune des 10 clés de `lecture-juges.json` (l. 77-86) figure à une ligne du tableau de l'audit (l. 86 à 95) ; 6 du 3B, 4 du 8B |
| relecture, tirée par graine, de 10 actions : exactement `relectures_audit.actions` | faite, texte intégral (audit, l. 51 et tableau l. 106-117) | chacune des 10 clés (l. 65-74) figure à une ligne de l'audit (l. 108 à 117) ; 4 en e2, non notées à cette étape |
| contrôle du tirage | fait par le recalculateur : 20 éléments reproduits (audit, l. 52 et l. 255) ; refait de façon indépendante par le sceptique 2, à l'identique | aucune action commune avec la première lecture, qui avait tiré 0 réponse et 10 actions (`lecture.json`, l. 714-727) ; c'est l'effet annoncé (complément, l. 98) |
| recalcul indépendant par un sous-agent neuf | fait, sans importer de module du dépôt : « conforme » (audit, l. 53 et l. 203-207) | les comptes du recalcul égalent les recomptes de l'auteur et du correcteur (sections 3.2, 3.3) |
| lecture suspendue jusqu'au scellement de l'audit | `lecture_suspendue` vrai (l. 53) ; audit scellé au commit `1a0232a` | suspension levée |

« Aucune étape gelée n'est omise. Aucun rapport ne signale d'écart au protocole. » (audit, l. 56).

**Constats de l'audit** (repris sans chiffre nouveau ; audit, l. 289-309) :
- établi : « le déclencheur « décomposition impossible » est réel pour les deux juges » ; « son mécanisme immédiat est le comportement des juges : réponses tronquées, notes hors échelle, notes non entières, notes absentes. La mesure l'enregistre correctement » ; « l'alignement, le lecteur et le calcul de la lecture ne sont pas en cause » (l. 299-301) ;
- artefact du chemin de génération sur la carte : « non établi, non exclu : seul un rejeu sur la carte trancherait » (l. 295) ;
- propriété réelle des juges tels que configurés : « établie sur pièces » pour l'échelle, les notes non entières et la dégénérescence ; « cause profonde supposée » (l. 296) ;
- aucune lecture tolérante n'approche 48 tâches complètes (l. 164) ; nuance : le passage de « impossible » à « non concluant » tient à la règle stricte, gelée et motivée (CL-9), et tolérer la troncature donnerait 3 tâches au 8B (l. 165-166 et l. 293) ; ce sont des contrefactuels descriptifs, sans proposition de règle (l. 309).

**Effet sur la lecture gelée.**
- Règle du dépôt : « R4 Symétrie : un résultat suspect de propreté, positif ou négatif, déclenche le même audit ; trop beau = réserve » (`CLAUDE.md`, l. 38). Le texte gelé ne prévoit pas d'autre conséquence à un audit (même constat au verdict v1, l. 325).
- L'audit écarte les artefacts de mesure et de calcul de la lecture. Le seul point non exclu, le chemin de génération des juges, n'a de conséquence dans aucune ligne gelée. **Aucune lecture gelée ne change** ; ce point devient une réserve (section 8).

**Points que l'audit laisse à ce verdict** (audit, l. 313-320) :
1. Appliquer les critères gelés : fait (sections 2 à 4), avec la combinaison « décomposition impossible » et « plan B par l'incomplétude » (section 3.3) et la ligne « nœud de décomposition » (section 3.4).
2. Dire si les constats de l'audit changent une lecture gelée : non (ci-dessus).
3. **Provenance du commit** (audit, l. 260-263 et l. 320) :
   - le manifeste porte `b604164` parce que c'est le commit S où l'instance a tourné ; la récupération le vérifie (« commit du manifeste b60416400b02… = S », récupération l. 13). Le code cité est `c63d4f1` (complément, l. 6 ; `resume.json`, `commit_cite`) ;
   - dans le clone lu ici, `c63d4f1` **est** un ancêtre de `b604164` : c'est le parent de `f309d14`, qui est sur le chemin d'ascendance vers `b604164` (`git log --ancestry-path c63d4f1..b604164` : 29 commits ; recontrôlé par les deux sceptiques et par le correcteur). Ce clone est superficiel, mais sa limite (`197e909`, du 2026-10-12 à 01:25:08 UTC) est antérieure à tous les commits cités ;
   - aucun commit entre `c63d4f1` et `b604164` ne touche `src/`, `tests/` ou `scripts/` (`git log c63d4f1..b604164 -- src tests scripts` vide) ;
   - la phrase de l'audit « n'est pas un ancêtre de `b604164` dans l'historique local » ne se reproduit donc pas ici. Sa cause (un clone plus court chez les rapporteurs, par exemple) ne peut pas être vérifiée : leur dossier de travail n'est pas accessible.

## 6. Conséquences prévues par les textes gelés

**Plan B** (pour les deux juges) :
- table du pilote, l. 184 : « rubrique simplifiée pour ce juge, préenregistrée, puis requalifiée par une décomposition courte sur les ensembles déjà générés (seule la notation est refaite ; coût : une étape de notation) (CL-21) ; usagers selon la section « Hypothèse » » ;
- section « Hypothèse » du pilote, l. 45 : « plan B pour les deux : les deux passent à la rubrique simplifiée, requalifiée » ;
- portée (pilote, l. 40) : « le plan B décidé ici vaut pour une lecture du texte du juge à température 1,0. Les usagers lisent autrement, par espérance (P-003, P-010) : T0.6 (note d'utilité visible, la note d'ensemble des juges faibles b0) et T0.8 (bras b0, juges 8B et 3B). Chaque usager requalifie donc son juge sous son propre mode de lecture, dans son préenregistrement ; ce pilote ne fixe que la rubrique de départ de chaque juge » ;
- « le plan B d'un juge ne touche pas les familles » (pilote, l. 194).
- Constat de l'auteur, recontrôlé par le correcteur : aucun préenregistrement de rubrique simplifiée n'existe dans `prereg/` (le terme n'apparaît que dans les deux préenregistrements de T0.5 et dans des pièces de contre-lecture).

**Nœud de décomposition** : la ligne ne joue pas (section 3.4 : lecture imposée par le texte). Sous la lettre étroite de l'incomplétude, écartée par le texte gelé (section 3.5), le 3B serait en nœud : « nœud pour un juge : proposition à Lazar avant que T0.6 ou T0.8 ne s'en servent » (pilote, l. 46).

**Préséance** (complément, l. 123) : « Une fois un juge fini, sa notation n'est jamais refaite, relancement compris : écrit et poussé, il est lu tel quel, selon la table ». Les notations H.4 des deux juges, écrites et poussées, sont lues telles quelles ; elles ne sont pas refaites dans cette étape.

**Bascule du programme** :
- le pilote se rattache à la « bascule « 8B trop faible → rubrique simplifiée » » (pilote, l. 34) ; le programme l'écrit ainsi : « 8B trop faible sur l'environnement (a) → rubrique simplifiée (changement de modèle seulement sur GO) » (`docs/programme-controle-ia-v2.md`, l. 241) ; le brief : « Plan B préenregistré : si le 8B est trop faible pour la tâche, rubrique simplifiée. Aucun changement de modèle sans GO » (brief, l. 158) ;
- **rapprochement de l'auteur**, pas une ligne gelée : le plan B du 8B porte la conséquence que nomme cette bascule (la rubrique simplifiée). Aucune ligne gelée ne dit que le plan B du 8B la déclenche. Et « 8B trop faible » n'est pas établi comme propriété du modèle : le chemin de génération n'est pas exclu (réserve 1) ;
- les consignes du dépôt rangent tout « déclencheur de bascule » parmi les nœuds de décision (arrêt, attendre le GO) (`CLAUDE.md`, l. 53). Par prudence, ce verdict porte la bascule comme nœud (section 7). Aucune bascule n'est nommée pour le 3B.

**Critère de G0 concerné** :
- le texte gelé ne rattache le plan B des juges à aucun critère de G0. Il nomme le critère 2 pour les familles seulement (pilote, l. 174 et l. 183), et nomme les usagers des juges : T0.6 et T0.8 (l. 40) ;
- rapprochement de l'auteur, par les intitulés du brief (aucune ligne gelée ne le fait) : la condition de fin de T0.6 (« Organismes modèles v0 », l. 160-164) est celle du critère 2, « Organismes (i) et (ii) : sabotage mesurable avec dose-réponse » (l. 193) ; T0.8 (« Bases boîte noire v0 », l. 175-178) prépare le critère 4, « Base boîte noire, par action et séquentielle, qui tourne sur le même jeu d'épisodes » (l. 195) ;
- ce verdict ne prononce aucun critère de G0. État consigné : critères 1 et 5 prouvés, les autres restent (`registres/etat.md`, l. 26).

**Format et familles** : inchangés (complément, l. 119) : format retenu ; famille « coût » retenue ; contrôles, directions fécondes et directions stériles non retenus (verdict v1, section 1).

## 7. Ce qui reste nœud pour Lazar

1. **GO sur ce verdict** : « scellé, puis soumis à Lazar pour GO » (`CLAUDE.md`, l. 47, R13). Le complément (l. 102) et le pilote (l. 174) disent « scellé, puis soumis à Lazar », sans nommer le GO ; demander le GO est la version prudente.
2. **Bascule « 8B trop faible → rubrique simplifiée »** : rapprochement de l'auteur (section 6), porté comme nœud par prudence, car tout déclencheur de bascule est un nœud de décision (`CLAUDE.md`, l. 53). Changement de modèle : seulement sur GO (programme, l. 241). « 8B trop faible » n'est pas établi comme propriété du modèle (réserve 1).
3. **Voie du plan B pour les deux juges** :
   - rubrique simplifiée à préenregistrer (R1), contre-lue (R2) ;
   - requalification par « une étape de notation » sur la carte : dépense de calcul, donc devis et GO (`CLAUDE.md`, l. 53) ;
   - tant que la rubrique simplifiée n'est ni préenregistrée ni requalifiée, la rubrique de départ que fixe ce pilote pour T0.6 et T0.8 n'existe pas encore.
4. **Écart de procédure au préenregistrement scellé : la surveillance** (sans effet sur la lecture) :
   - texte gelé : « surveillance : arrêt au plus tard à la création plus 26 400 s » (complément, l. 84 ; bornes, l. 93) ;
   - faits : instance créée le 17 à 19:09:43 UTC (`lancement.txt`, l. 16 : 1792264183) ; borne de la surveillance le 18 à 02:29:43 UTC (l. 17 : 1792290583) ; surveillance de la session éteinte le 17 à 20:42 UTC avec son processus parent (R-205, `registres/decisions.md` l. 342 ; leçon notée par R-206, l. 343) ; run fini seul le 17 à 23:56:59 UTC (journal de l'instance, l. 58), soit 17 236 s après la création, sous le plafond de sa propre amorce ; instance arrêtée par son identifiant le 18 à 21:36:57 UTC (`registres/arrets.md`, l. 22), soit 68 834 s après la borne ;
   - dépense consignée : au plus 8,23 USD, sous le plafond de 8,70 USD écrit par le lanceur et sous celui de 10,5 USD de l'étape (`registres/depenses.md`, l. 86) ;
   - R-205 consigne ces faits sans les qualifier d'écart. Or tout « écart à un préenregistrement scellé » est un nœud de décision (`CLAUDE.md`, l. 53) : il est soumis à Lazar avec ce verdict, pour qualification. Il ne touche aucune ligne de lecture : le run a fini et consigné son issue (`resume.json`), sous les échéances internes.
5. **Suites de l'audit** (audit, l. 322-326) :
   - cause profonde : « seul un rejeu sur la carte séparerait une propriété du modèle d'un défaut du chemin de code commun. C'est un nœud et une dépense » ;
   - « tout changement de réglage des juges (température, tirage par noyau, plafond, invite) : ce serait un écart au préenregistrement, à décider par Lazar » ;
   - « l'audit ne dit pas si une rubrique simplifiée, aux mêmes réglages, éviterait la dégénérescence. Celle-ci touche aussi l'agent (123 actions sur 1 800), hors de toute rubrique ».
6. **Pièces de procédure attachées à la soumission de ce verdict** (sans effet sur la lecture) :
   - destruction de l'instance 56438435, à proposer avec le verdict (R-205, `registres/decisions.md` l. 342 ; plan v1, l. 151-153) ; tant qu'elle est gardée, son disque (≈ 0,025 USD de l'heure) est consigné chaque jour (`registres/depenses.md`, l. 86) ;
   - instance du pilote 55538944, « gardée jusqu'au verdict complémentaire » (plan v1, l. 28-29).

**Pour information, sans décision demandée** : les deux lectures examinées et écartées par le texte gelé (sections 1, 3.4 et 3.5). Le correcteur juge qu'aucune ambiguïté du texte gelé ne demeure sur ces deux points : le texte lui-même tranche (pilote, l. 132 ; complément, l. 77, l. 85, l. 102, l. 139). Si Lazar lisait autrement la parenthèse du pilote (l. 83), ce serait un écart au préenregistrement scellé, décidé après les résultats : un nœud, que ce verdict ne propose pas, et qui mettrait le 3B en nœud (section 3.5).

## 8. Réserves

1. **Chemin de génération des juges non exclu** (audit, l. 195, l. 295 et l. 334). La garde d'équivalence en ligne du pilote couvre l'agent (contextes d'au plus 6 030 jetons, 400 jetons générés), pas les juges (jusqu'à environ 10 000 positions) (audit, l. 195). Le plan B par l'incomplétude repose sur des sorties dont le chemin de génération n'est pas éprouvé pour les juges. La cause profonde (tirage à température 1,0 sur tout le vocabulaire, sorties longues, ou défaut d'un chemin de code commun) est supposée, non établie (audit, l. 304-305).
2. **Poids des notes hors échelle dans le plan B du 3B** (section 3.5) : 102 des 130 réponses incomplètes du 3B le sont sans note absente ni troncature, dont 96 par la seule note hors échelle. Le texte gelé confie ce compte au code gelé, qui les range dans l'incomplétude ; la parenthèse du pilote (l. 83) ne nomme pas les notes hors échelle. Sous une autre définition, adoptée après les résultats (un écart), le 3B serait en nœud. Le plan B du 8B tient sous toutes les variantes.
3. **Portée du plan B** : il vaut pour une lecture du texte du juge à température 1,0 (pilote, l. 40). Il ne dit rien d'une lecture par espérance, celle des usagers.
4. **Plan B aux mêmes réglages** : rien n'établit qu'une rubrique simplifiée, aux mêmes réglages, éviterait la dégénérescence (audit, l. 325).
5. **Tirage des actions de l'audit désaccordé** avec les notations : 4 actions sur 10 en e2, non noté ; 3 invalides ; 6 seulement ont une notation de leur ensemble (audit, l. 120 et l. 326). C'est un effet du code gelé `tirer_relectures`.
6. **Indicateur de dégénérescence de l'audit** : fait par le relecteur, non préenregistré, seuil fixé après lecture (audit, l. 329). Il est descriptif ; ce verdict ne s'en sert pour aucune lecture.
7. **Écarts de procédure, sans effet sur la lecture** :
   - la surveillance s'est éteinte avant sa borne : écart au complément (l. 84), porté comme nœud (section 7, point 4) ;
   - écarts nommés ou déclarés en amont : lanceur v2, écart à la chaîne scellée décidé par Lazar (R-190, `registres/decisions.md` l. 327 ; plan v2, l. 3-12) ; deux écarts au plan, décidés par Lazar pour le premier appel du lanceur v2, arrêté avant la création (R-200 et R-201, l. 337-338) ; un écart de la session, déclaré, pendant le second appel, celui qui a créé l'instance (un travail de sous-agents lancé pendant les contrôles, arrêté une minute plus tard ; R-204, l. 341). Aucun ne touche une ligne de lecture.
8. **Provenance** : l'audit et ce verdict divergent sur l'ascendance de `c63d4f1` (section 5) ; les deux sceptiques et le correcteur retrouvent l'ascendance ; l'identité du code entre `c63d4f1` et `b604164` est établie des deux côtés.
9. **P1, P4 à P7** : reprises de la première lecture, avec les réserves du verdict v1 (section 9 de ce verdict v1), notamment sur P5.

## 9. Ce que l'auteur et le correcteur n'ont pas pu vérifier

- **Textes des réponses et des actions** : non lus (discipline de lecture, en tête). Les constats qualitatifs de l'audit (dégénérescence, notes fondées ou non, ordre des notes) ne sont vérifiés ni par l'auteur ni par le correcteur ; seuls les comptes de motifs le sont.
- **Code non exécuté** : le lecteur n'a pas été rejoué ; le format n'a pas été recalculé (le lecteur l'exige égal avant d'écrire ; l'audit l'a recalculé) ; `verifier-arbre` n'a pas été lancé ; la suite de tests non plus.
- **Décomposition, parts, intervalles** : impossibles sous la lecture appliquée, donc non recalculés. Sous les variantes de la lettre étroite (section 3.5), le correcteur n'a calculé que les comptes ; la décomposition n'y changerait pas l'issue.
- **Troncature** : « sans jeton de fin » n'est pas vérifiable sans les jetons ; seule sa coïncidence avec 3 072 jetons l'est.
- **Dépôt distant** : ni la branche `calcul/t05-notations-reel-v1` ni `main` n'ont été relues sur le dépôt distant (aucune commande réseau).
- **Instances** : aucun état Vast.ai relu (interdit). Les arrêts et les dépenses viennent des registres (`registres/arrets.md` l. 22 ; `registres/depenses.md` l. 85-86).
- **Dossiers de travail de l'audit** : hors du dépôt, sous un bloc-notes d'une autre session, inaccessibles d'ici. Seuls les deux rapports versés et scellés ont été lus.
- **Annexe C.1 de 2606.08892** : non relue (R7) ; ce verdict n'en tire aucun chiffre.
- **Invites H.3 et H.4** : non relues ; les bornes des échelles sont celles qu'applique le code gelé (`rubrique.py`, l. 18-23), dont les motifs d'anomalie ont été comptés.
- **Historique** : le clone est superficiel (limite `197e909`) ; les constats d'ascendance ne valent que dans l'historique disponible, qui contient tous les commits cités.

## 10. Empreintes (sha256 complets, calculés par l'auteur, recalculés par le correcteur)

| pièce | sha256 | sceau compagnon ou remarque |
|---|---|---|
| `prereg/T0.5-pilote-notations-v1.md` | `66784ceb9c93f699b211fa26a142a8e64e1cccbc2c2fb3479df559f297c474f6` | conforme |
| `prereg/T0.5-pilote-notations-config-v1.json` | `143cfa258a8364ded0ffced1ad5213a26a2c8598112fa11a3fc44357fbe9ea97` | conforme |
| `prereg/T0.5-pilote-8B-v1.md` | `9ce91ba16108635e917910e67cc199ac2dc31a76d76c7de8408c3ed457110590` | conforme |
| `prereg/T0.5-pilote-config-v1.json` | `6979a00ebef1e794f900e089df9b1658482f8600ce343cb81c95da4434da2b8a` | conforme |
| `diag/20261017-193648-t05-notations-reel/notations-8B-decisives.json` | `b103835bcd3bfc3117a53e335be6f37a1259102cc2a2a134acfc6e114cb3f1c4` | conforme |
| `diag/20261017-193648-t05-notations-reel/notations-3B-decisives.json` | `51548526c7590231b76473c2b4c9e619a092616b5f948830e735c466b037adab` | conforme |
| `diag/20261017-193648-t05-notations-reel/resume.json` | `994d542aafd224fc9347b2186979916c3e0a799c6edbefa28a7c9d6e972f44fc` | conforme |
| `runs/20261017-193648-t05-notations-reel/manifeste.json` | `9f143f7c1c9fd9d75f21807a0fa41035ae7110abe686fc7819130d3f6b435d38` | conforme |
| `diag/20261018-214028-t05-lecture-juges/lecture-juges.json` | `d41c3f585d9f2b89611dca0b40a6ced9d83e1004f140cbdadc0629f7e58695e4` | conforme |
| `runs/20261018-214028-t05-lecture-juges/manifeste.json` | `5349b2316518f6c3e1aed6f69dd8e3c63b5b72f7cbc2072de308a2628e27f198` | conforme |
| `diag/20261012-150724-t05-pilote-analyse/lecture.json` | `396a7dff8348a0aff7d9e3bde25b0d054919d2395aee3868b9058c974005c38d` | conforme |
| `runs/20261012-150724-t05-pilote-analyse/manifeste.json` | `4b1a3fe10052830c953f979cb2903cf62e512274db71684faf04ab026e95ffdf` | conforme |
| `runs/20261012-105125-t05-pilote-reel/manifeste.json` | `8c3d7985eb65cd7b1dd239f8633e552b6af5fc14f44caaa801d1b85249e5e932` | conforme |
| `diag/20261012-105125-t05-pilote-reel/episodes.json` | `45616303dc740b66c42095cd5317a8ddd63e89123e64dd86490e43429c7cd15c` | conforme |
| `donnees/t05-pilote-v1/taches-pilote-60-v1.json` | `287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5aa` | conforme |
| `docs/verdicts/audit-R4-T0.5-pilote-notations-v1.md` | `d69a8700fcce69a5405ae9d3cdbcd51a9f541726a9e3e67dc0b76bb0b86f2c20` | conforme |
| `docs/verdicts/audit-R4-T0.5-pilote-notations-v1-sources/rapport-relecture-v1.md` | `4d1bd69fe1552d86efe6c63ada21f86a7a924ef5719e61b0760ee58695e38803` | conforme |
| `docs/verdicts/audit-R4-T0.5-pilote-notations-v1-sources/rapport-recalcul-v1.md` | `5ee10b95f39b809027342df80083931ca156fecf5a95eae648336901a2631e85` | conforme |
| `docs/verdicts/verdict-T0.5-pilote-v1.md` | `b9a072302d6514c0df80c950317012498c7af62b6440e37045a43de46a3faabc` | conforme |
| `docs/verdicts/audit-R4-T0.5-pilote-v1.md` | `f557402b90d1fea33e669295fdeecd835477b3244ca4ebdc256787a44c6071b8` | conforme |
| `docs/procedures/notations-T0.5-v2/plan-lancement-notations-v1.md` | `4c59f32d00829026ca19b67601c6363c873d990633c1041f7f360025f1e42c19` | conforme |
| `docs/procedures/notations-T0.5-v3/plan-lancement-notations-v2.md` | `fda7d83b796179b08ff177c1252f8c341044107e362b44b7cb261b5eb1fdfd43` | conforme |
| `traces/t05-notations-v2-20261017-1846-session/lancement.txt` | `c99a996d57d30af2bcf6b344b489bdb4b45e03f6028169561edecae1ae468913` | conforme |
| `traces/t05-notations-v2-20261017-1846-session/recuperation-notations-20261018-2140.txt` | `1038cf503fbbb35145f5b1517aa8d3f0c929cf58c2f44e78c731b2d6f571fe0c` | conforme |
| `traces/t05-notations-20261017-235701-mDaN/journal.txt` | `1ec04b859c2db2c56c635f55bbfecc3e994948a0d5b38b2dd2c197fa085405e1` | conforme (`empreintes.sha256`) |
| `docs/programme-controle-ia-v2.md` | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` | `docs/sha256sums-lancement-v2.txt` conforme |
| `docs/brief-claude-code-programme-complet-v2.md` | `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2` | idem |
| `CLAUDE.md` (aux commits `1b46eed` et `95bef7e`) | `1d469390187103fd509ccfa05f3df4ec1df0088fbc99a789f9fec64505cb497d` | — |
| `registres/decisions.md` (au commit `1b46eed`) | `5872374904331e8c99c4d4d285559f51cf6893d8ff3fc24fa7d71ba5ac3e2b13` | à `95bef7e` : `4949a684ab8c844f5ce941dfea74247b93911d2052c7980fdf159377b8cf5469` (commit `f096dba` : R-208 et R-209 ajoutées après la l. 342 ; l. 1-342 identiques) |
| `registres/go.md` (aux commits `1b46eed` et `95bef7e`) | `29a7a4927962837d84f1a0b174f5d0091aecf890af856228db3f092cfc5eb43b` | — |
| `registres/arrets.md` (aux commits `1b46eed` et `95bef7e`) | `547298572329c5f1051cf9ac281c181f3640f97de44a9f404f0af47cae517df9` | — |
| `registres/depenses.md` (aux commits `1b46eed` et `95bef7e`) | `c603a97492517ff6edf977f542dffb4992378fb149fe02c2e58ff4b3b124085d` | — |
| `registres/etat.md` (au commit `1b46eed`) | `11de4b6723414a46dd3b755749c61f8d5e85371d3c25d77bc25515072cc819ee` | à `95bef7e` : `ca7f34672cb1f46caf56f437243dd3c3c3b5c0c2b12394bfeeee424f71a08055` (commit `f096dba` ; l. 26 identique) |

- Les trois pièces du pilote ont aussi l'empreinte que cite le complément (l. 23, 24 et 26). Le commit de scellement du pilote, `1c6c900`, daté du 2026-10-12 à 06:21:52 UTC, est dans l'historique lu.
- Les registres changent après chaque session : la session revérifie leurs empreintes au scellement, et cite le commit auquel elle les prend. Les lignes citées par ce verdict ne changent pas d'une version à l'autre (contrôle du correcteur par `diff`).
- Code gelé lu par `git show` (empreinte du fichier extrait) : au commit `2660b07`, `src/controle_ia/environnements/lire_pilote.py` `0fa7814798cdab527c92e355bf096c4ddcbc55ef5711060e21f4a24cc20dd681`, `src/controle_ia/environnements/rubrique.py` `da2f7a1e3b4c2e11aa845816afe51f068420355da2ad6c3bfb3e66484764e0dd`, `src/controle_ia/environnements/pilote_a.py` `624761e2831a3fa14ccc1fe817d38a59014c9ef157e600cbd67e411607869bfc`, `src/controle_ia/environnements/analyse_pilote.py` `6ce65063b447fdb0921686dbf5028856879f0a5267b67a03f92141ac0f3249fb` ; au commit `b604164`, `src/controle_ia/environnements/lire_notations_pilote.py` `522da87c05fb12f146a63a50d0d880c26915b20b87c2f046a74dcc480e1aaa32`.

## 11. Fichiers de travail (hors dépôt, sha256)

Ils sont sous `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/verdict-notations/`, dossier éphémère. **La session les verse dans une archive versionnée avec son sceau**, `docs/verdicts/verdict-T0.5-pilote-notations-v1-fichiers-de-travail.tar`, sur le modèle de `docs/verdicts/verdict-T0.5-pilote-v1-fichiers-de-travail.tar` (sceau conforme, contrôlé par le correcteur), avec les deux rapports des sceptiques tels qu'elle les a transmis au correcteur. Elle cite le chemin et l'empreinte de l'archive au scellement du verdict (R6, R12).
- Aucun de ces fichiers ne porte de texte de réponse, d'action ou d'ensemble : les sorties JSON ne portent que des clés, des nombres, des identifiants et des empreintes (chaînes de 67 caractères au plus ; contrôle du correcteur). Les copies de code sont extraites par `git show`. `sceptique-2/pilote-1-140.txt` est une copie numérotée des lignes 1 à 140 du pilote.
- Les scripts se lancent par `python3 -I <script> /home/user/controle-ia-travail`. Ils n'importent aucun module du dépôt et n'écrivent que sur la sortie standard.

| fichier | rôle | sha256 |
|---|---|---|
| `consigne-sceptique.txt` | consigne remise aux deux sceptiques | `410525265ab0f2bf56b9053d06473a3d902a8eb5fe3642e2eb66585f122587ce` |
| `auteur/verdict-T0.5-pilote-notations-v1-brouillon.md` | brouillon de l'auteur | `7af483a3a9b5aa3a3ef33fe96524b4a69444b0f900e52c1d13d66bed099e7719` |
| `auteur/recompte.py` | auteur : rattachements, alignement, réponses et tâches complètes, A et B identiques, sommes | `0670aca0a3b79cee675ad06410899706ccecd6ec96eec001134afdf2d53f395b` |
| `auteur/recompte-sortie.json` | sortie de `recompte.py` | `3211332927cbaa98fb47c9ccb966db1b5d58a823a79b0a3fcb857d32072a7efe` |
| `auteur/motifs.py` | auteur : motifs d'incomplétude par juge | `bf429c57c92e07681e6c4ac494f5d4b79b09649383322c7a46ebeb0fcca083c4` |
| `auteur/motifs-sortie.json` | sortie de `motifs.py` | `3e9768f8169a35d5bff64163dc311c3a46b75734d8b146918c683b8e7b760c63` |
| `auteur/lire_pilote_2660b07.py` | copie de `lire_pilote.py` au commit `2660b07` | `0fa7814798cdab527c92e355bf096c4ddcbc55ef5711060e21f4a24cc20dd681` |
| `auteur/lire_notations_pilote_b604164.py` | copie de `lire_notations_pilote.py` au commit `b604164` | `522da87c05fb12f146a63a50d0d880c26915b20b87c2f046a74dcc480e1aaa32` |
| `sceptique-1/recalcul_s1.py` | sceptique 1 : recalcul | `0a4bc1e40b3fbe97d113cc4d70a8772d1e24f85cea0d0ed66b05f12a04adea6d` |
| `sceptique-1/recalcul-sortie.json` | sceptique 1 : sortie | `eec35b10d24066671b58dd07f1ec2d50e875a859eb5d768e5ed0bd20b5c46d5b` |
| `sceptique-1/variantes_s1.py` | sceptique 1 : variantes de la lettre étroite | `35dbbaf326db7990c1526f7182aee0f99ff6de47de0b24c3f322851479ab633b` |
| `sceptique-1/variantes-sortie.json` | sceptique 1 : sortie | `a3b689c487cdc7ae63e4cda45786034e4f06ab67ad1bd0401b356ee97dc21b91` |
| `sceptique-1/empreintes-controle.txt` | sceptique 1 : contrôle des empreintes | `4e00abaee42452977987407d74089d89158d6172b7e9d748c5c8eee1ce0d3fa2` |
| `sceptique-1/empreintes-attendues.txt` | sceptique 1 : empreintes de la section 10 du brouillon | `6e39cf0566a25b6d301619ad4fd26bab7114053bd61f917cceb227bdaa277a8d` |
| `sceptique-1/lire_pilote_2660b07.py` | copie de `lire_pilote.py` au commit `2660b07` | `0fa7814798cdab527c92e355bf096c4ddcbc55ef5711060e21f4a24cc20dd681` |
| `sceptique-2/recalcul_s2.py` | sceptique 2 : recalcul | `9568b3ad4b50a341c2ecfec43d3be380805460412a0f07722620596217446009` |
| `sceptique-2/recalcul-sortie.json` | sceptique 2 : sortie | `09071ce451f037041c2c528e06ad78c2399644e5a1998c9185a45ec1c4fa06d2` |
| `sceptique-2/recalcul-err.txt` | sceptique 2 : sortie d'erreur (vide) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `sceptique-2/variantes_etroites.py` | sceptique 2 : variantes de la lettre étroite | `4e53964f2d06ea96d8b1e2094dbff4a79d29d9b47022274e2601b6c8f6399659` |
| `sceptique-2/variantes-sortie.json` | sceptique 2 : sortie | `6fe787adf142c5a248315e6c6e9317bede56f111a18508f3bc6e5d89b991190e` |
| `sceptique-2/variante_d18.py` | sceptique 2 : variante avec D-18 | `605ec3e664e48dd25d5688dca1cb72506fcea212230e9772889832e6036e8fbf` |
| `sceptique-2/variante-d18-sortie.json` | sceptique 2 : sortie | `f82ff16cdbe5acf1f19c88872bc10d52bafe3f47a72db6fd1a263ab980ce477e` |
| `sceptique-2/structure.py` | sceptique 2 : structure des fichiers, sans chaîne | `d9747f2eea1e3f2ce529e9f4c89e4eb605822e4fc01a95645731c3466d141abb` |
| `sceptique-2/attendus-section10.txt` | sceptique 2 : empreintes de la section 10 du brouillon | `6e39cf0566a25b6d301619ad4fd26bab7114053bd61f917cceb227bdaa277a8d` |
| `sceptique-2/verif-section10.txt` | sceptique 2 : contrôle des empreintes | `4e00abaee42452977987407d74089d89158d6172b7e9d748c5c8eee1ce0d3fa2` |
| `sceptique-2/pilote-1-140.txt` | sceptique 2 : copie numérotée des lignes 1 à 140 du pilote | `33b5debb5b4939a09230da392ea7679bad8b8b524489779e171dfe567b66940a` |
| `correcteur/recompte_c.py` | correcteur : rattachements, alignement, comptes, cohérence interne, motifs, variantes de la lettre étroite et tâches complètes de chacune | `fec0a4b59c9b359ccabc92a1196c6ee3b477152fc1913f316efaf27e284d3677` |
| `correcteur/recompte-sortie.json` | sortie de `recompte_c.py` | `cde4a8d5ac232851bf65408e72d0bf440d29ced7d0ae609a94d98ddc07fdc0e5` |
| `correcteur/manifestes_c.py` | correcteur : manifestes, graines, paramètres des juges, versions | `3262d1667615156c4b7fddb03fbbc36802a5b3e72aa9e55447ac8ef8036b100c` |
| `correcteur/manifestes-sortie.json` | sortie de `manifestes_c.py` (361 clés de graines : les 360 des juges et `modele-jouet`, toutes égales à celles du pilote) | `0fa832c5f57acf3137c5d1c2d7f3fd5a06b5220b2d30cf41da0753757143f2d2` |
| `correcteur/horodatages_c.py` | correcteur : horodatages de la surveillance | `bc2b05fff853542628af66a6e96aaca96819f4b1aef4de5d00d03fc7b31f64b7` |
| `correcteur/horodatages-sortie.json` | sortie de `horodatages_c.py` | `7dc7d0ff4c08fc632c742c3bb49a02fb1d7b6b7217c9e3d1173dbb587b2ad291` |
| `correcteur/structure_c.py` | correcteur : structure des fichiers scellés, sans chaîne | `c8c94d57527a90739c09d8a1399e7daae7b3cd6bd6227e5a8256f04aec328f93` |
| `correcteur/empreintes-section10-brouillon.txt` | correcteur : les 33 empreintes de la section 10 du brouillon (même contenu, octet pour octet, que les listes des deux sceptiques) ; `sha256sum -c` à `95bef7e` : 31 conformes, 2 changées (registres des décisions et d'état) | `6e39cf0566a25b6d301619ad4fd26bab7114053bd61f917cceb227bdaa277a8d` |

La version finale de ce verdict est écrite dans `correcteur/verdict-T0.5-pilote-notations-v1.md`. Son empreinte de référence sera celle de son scellement.

## 12. Contre-vérification

Le correcteur a vérifié chaque constat dans les fichiers (sections 10 et 11). Aucun ne réfute le verdict ni ne change une lecture gelée. Décompte : **16 constats, 16 intégrés, 0 écarté.**

**Sceptique 1** (jugement : non réfuté)
- **S1-01** (majeur) — La « lecture nommée 2 » (réponse incomplète) n'est pas une vraie ambiguïté : le texte gelé impose la lecture du code ; la lettre étroite, adoptée maintenant, serait un écart choisi après les résultats (R1), donc un nœud et non une prise d'acte. — **Intégré.** Vérifié dans le texte : pilote l. 82, l. 83, l. 133 (D-18), l. 161-164, l. 174 ; complément l. 56, l. 68, l. 77 ; code au commit `2660b07` : `rubrique.py` l. 7-8 et l. 73-79, `lire_pilote.py` l. 262-263 et l. 310. Section 3.5 réécrite en « lecture imposée par le texte gelé » ; l'autre lecture reste écrite, « examinée, écartée par le texte gelé ; l'adopter serait un écart (nœud) » ; elle sort de la prise d'acte (sections 1 et 7) et devient une information pour Lazar et la réserve 2. Raison : la parenthèse de l. 83 n'est pas une liste fermée (D-18) ; elle se tait sur les notes hors échelle sans les exclure ; pour une omission, le complément renvoie au texte du pilote et au code gelé, qui font foi (l. 77) ; et le texte confie le compte au code et au lecteur, hors duquel aucune lecture ne se fait (complément, l. 139).
- **S1-02** (mineur) — Les comptes de l'autre lecture oublient D-18 ; « la décomposition reste impossible » ne vaut que pour la version hybride. — **Intégré**, recalculé par le correcteur (`correcteur/recompte-sortie.json`) : 8B de 87 à 121 réponses incomplètes (0,483 à 0,672), 3B de 28 à 34 (0,156 à 0,189 ; 29 à 34 avec D-18) ; tâches complètes du 3B : 2 en version hybride, de 30 à 35 en version cohérente ; nœud pour le 3B dans tous les cas, plan B pour le 8B dans tous les cas (section 3.5). Les nombres du sceptique sont tous retrouvés ; le correcteur ajoute les tâches complètes de chaque variante.
- **S1-03** (mineur) — La « lecture nommée 1 » (ligne « nœud de décomposition ») est imposée par le texte (l. 132, l. 41-46). — **Intégré.** Vérifié : pilote l. 129-132, l. 41-46, l. 185, l. 247 ; code l. 320-323 et l. 334. Section 3.4 réécrite ; le point sort de la prise d'acte ; effet nul. Raison : « sauf » et « sinon » (l. 132) excluent l'autre lecture.
- **S1-04** (mineur) — La surveillance éteinte avant sa borne est un écart au complément (l. 84), donc un nœud, et non une qualification facultative. — **Intégré.** Vérifié : complément l. 84 et l. 93 ; `lancement.txt` l. 16-17 ; journal l. 58 ; `registres/arrets.md` l. 22 ; R-205 (l. 342), qui ne qualifie pas l'écart ; `CLAUDE.md` l. 53. Horodatages recalculés (`correcteur/horodatages-sortie.json`) : borne le 18 à 02:29:43 UTC ; arrêt 68 834 s plus tard. Nœud 4 de la section 7 ; la réserve 7 y renvoie.
- **S1-05** (mineur) — Les recomptes renvoient à un dossier éphémère ; le verdict v1 a versé ses fichiers de travail dans une archive scellée. — **Intégré.** Vérifié : `docs/verdicts/verdict-T0.5-pilote-v1-fichiers-de-travail.tar`, sceau conforme ; verdict v1, l. 449. Section 11 : archive à verser par la session, avec son sceau, et les rapports des sceptiques.
- **S1-06** (pour information) — Les empreintes des registres « à la lecture » sont celles de `1b46eed` ; `f096dba` a changé deux registres. — **Intégré.** Vérifié : `git show 1b46eed:` et `git show f096dba:` ; lignes citées inchangées (`diff` des l. 1-342 des décisions et de la l. 26 de l'état, vides). Section 10 : colonne datée par commit ; valeurs à `95bef7e` ajoutées ; revérification au scellement.
- **S1-07** (pour information) — Les nombres de la réserve 1 (6 030 jetons, 400 générés, environ 10 000 positions) sont à l'audit l. 195, pas aux lignes citées. — **Intégré.** Vérifié : audit l. 195 ; l. 295 et l. 334 disent la limite sans les nombres. Réserve 1 : « audit, l. 195, l. 295 et l. 334 ».
- **S1-08** (pour information) — Le brouillon omet la nuance de l'audit (l. 165 et l. 293). — **Intégré.** Vérifié. Ajoutée aux sections 3.5 et 5.

**Sceptique 2** (jugement : non réfuté)
- **S2-01** (majeur) — Même point que S1-01, avec en plus le complément l. 85, l. 87 et l. 139 (« aucune lecture ne se fait hors de ce lecteur ») et le pilote l. 174 ; comptes étroits sans D-18 (29, puis 33 avec les décimales). — **Intégré** (avec S1-01 et S1-02). Vérifié : complément l. 85, l. 87, l. 102 et l. 139 ; la variante « D-18 et décimales, sans l'échelle écrite autre » (33, soit 0,183) est retrouvée par le correcteur et figure au tableau de la section 3.5.
- **S2-02** (mineur) — Même point que S1-03, avec le complément l. 40, l'ordre de la règle (l. 129-131) et le pilote l. 247. — **Intégré** (avec S1-03). Vérifié.
- **S2-03** (mineur) — Même point que S1-04. — **Intégré** (avec S1-04).
- **S2-04** (mineur) — Même point que S1-06 ; tête alors à `261f93e`. — **Intégré** (avec S1-06). À la correction, la tête est `95bef7e` ; les deux commits ajoutés depuis `f096dba` ne touchent aucune pièce citée.
- **S2-05** (mineur) — Même point que S1-05 ; formes proposées : dossier `…-sources/` scellé, ou retrait des nombres qui n'y renvoient pas. — **Intégré** sous la forme de l'archive, celle du précédent (verdict v1). Aucun nombre n'est retiré : tous sont recalculés par le correcteur et renvoient à des fichiers à verser.
- **S2-06** (pour information) — « Le plan B du 8B déclenche la bascule » est un rapprochement de l'auteur, pas une ligne gelée ; « 8B trop faible » n'est pas établi. — **Intégré.** Vérifié : pilote l. 34 ; programme l. 241 ; brief l. 158 ; aucune ligne gelée ne relie le plan B à la bascule. Sections 6 et 7 (nœud 2) : marqué « rapprochement », renvoi à la réserve 1 ; le nœud reste, par prudence (`CLAUDE.md`, l. 53).
- **S2-07** (pour information) — « Soumettre à Lazar pour GO » : le complément (l. 102) dit « scellé, soumis à Lazar », sans GO ; `CLAUDE.md` l. 47 dit « pour GO ». — **Intégré.** Vérifié : les deux textes, et le pilote l. 174, sont cités (en tête ; section 7, nœud 1) ; le GO reste demandé.
- **S2-08** (pour information) — `c63d4f1` est bien un ancêtre de `b604164`, contre la phrase de l'audit. — **Intégré** : confirmé par le correcteur (`git log --ancestry-path c63d4f1..b604164` : 29 commits ; `c63d4f1` parent de `f309d14` ; aucun commit sur `src`, `tests` ou `scripts` entre les deux ; limite du clone `197e909`). Aucun changement de fond (section 5 et réserve 8).

**Vérifications propres au correcteur**
- Recompte complet depuis les fichiers scellés, sans module du dépôt (`correcteur/recompte_c.py`) : tâches (60, distinctes, `287e8348…`) ; épisodes (180, aucun ensemble vide) ; alignement, comptes, tronquées, tâches complètes, sommes, A et B identiques, cohérence interne, motifs par réponse et défauts uniques. Tout est égal au brouillon, aux deux sceptiques et à l'audit (l. 141-149, l. 179).
- Manifestes (`correcteur/manifestes_c.py`) : commits, préenregistrement, mode, propreté, versions, graines de la lecture et des juges, paramètres des juges : conformes au brouillon.
- Empreintes : 33 de la section 10 (31 égales à `95bef7e`, 2 registres datés) ; 24 sceaux compagnons conformes ; `docs/sha256sums-lancement-v2.txt` conforme ; liste du journal de l'instance conforme.
- Code : modules de lecture, modules neufs, `pilote_a.py` et `harnais/episode.py` de même empreinte à `2660b07`, `c63d4f1`, `b604164`, `9c7dcef`, `95bef7e` et dans l'arbre ; aucun commit sur `MODULES_LECTURE` depuis `2660b07`.
- Lignes citées : toutes celles des sections réécrites (3.4, 3.5, 5, 6, 7, 8, 10, 11) ont été relues dans les fichiers.

**Ce que le correcteur ne tranche pas** : rien. Sur les deux points que le brouillon présentait comme des lectures nommées, il juge, avec les deux sceptiques, que le texte gelé tranche lui-même ; aucune ambiguïté ne demeure. Les lectures possibles, leurs conséquences chiffrées, la lecture appliquée et sa raison restent écrites (sections 3.4 et 3.5), et sont portées à Lazar pour information (section 7).
