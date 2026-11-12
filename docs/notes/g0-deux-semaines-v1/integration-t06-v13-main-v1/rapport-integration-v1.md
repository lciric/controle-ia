# Rapport d'intégration de la chaîne T0.6 v13 (`1609a4bf`) dans `main` — v1

- Auteur : développeur neuf (n'a écrit ni T0.6, ni T0.7, ni P3-bis, ni la chaîne ; n'est pas le lecteur exploratoire de 7a), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`.
- Consignes suivies : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/consigne-integration-chaine-t06-v13-main-v1.md` (`2e0fe2d468f2962be1245d5401ccbcea74b0d8e9f1873a1dd2a409bda81c5d2b`, vérifiée) et son additif `consigne-integration-chaine-t06-v13-main-v2-additif.md` (`a482856ffea16367c11f52792b031dff202cc58dad8fe37c97b13deba8faf218`, vérifié ; décision de la mère R-2055). Ces deux consignes sont dans l'arbre de la mère, pas dans cette branche.
- Lieu : arbre de travail isolé `/home/user/integ-t06`, branche locale `prep/integration-t06-v13-main-v1`, partie de `ff3e9a09d7f23e65b4047f8266d6beec0bd1551f` (= `main` à 22:20 UTC). Rien poussé, rien récupéré, rien écrit dans l'arbre de la mère.
- Heures (`date -u`, 9 novembre 2026) : début 22:20:25 UTC ; fusion lancée 22:20:58 ; arrêt R12 22:22:32 ; reprise sur l'additif 22:23:58 ; commit de fusion 22:26:39 ; sceaux scellés et vérifiés 22:31:46, commit des sceaux 22:32:00 ; interpréteur prêt 22:38 ; suite ciblée v3 de 22:38:20 à 23:27:31 ; essai à blanc des gardes 22:38:44 ; rapport écrit vers 23:31.
- Résultat en une ligne : **fusion faite et contrôlée (chaîne v13 égale à `1609a4bf`, neuf empreintes conformes, périmètre gelé = `main`, arbre scellé après les sceaux des 71 notes), mais la suite ciblée v3 donne 2 017 passés, 5 échoués, 0 sauté sur 2 022 : deux échecs (inventaire R-2042, liste v3 incomplète) arrêteraient l'amorce v11 sur l'instance ; la chaîne v13 ne peut pas jouer 7b sur l'arbre intégré sans correction (§ 8).**

## 1. Fusion

- Commande : `git -C /home/user/integ-t06 merge --no-ff --no-commit 1609a4bf2c1572f72bb8542d81d963ac6a8481c4`.
- Ancêtre commun : `067654576a21edab5a7f9a8728673ab290ab07ef`. 67 commits côté branche ; **673** côté `main` (la consigne disait 672 : le commit `ff3e9a09` de R-2053 est venu après le compte).
- La branche touche 341 chemins depuis l'ancêtre (339 ajoutés, 2 modifiés : `registres/go.md`, `tests/test_cibles_invisibles_v1.py`). Le commit de fusion ajoute 330 fichiers à `main` (63 804 lignes ajoutées, aucune retirée).
- Embargo : par les noms seuls (`git diff --name-status`, sans ouvrir aucun contenu), aucun chemin sous embargo n'est apporté. Les `diag/` et `runs/` apportés sont ceux de `20261105-021737-r1-v4-rejeu-reel` et `20261107-094957-audit-fuite-r1-v4` (ni 7a, ni `lecture-sondes-t06.json`). Dans l'arbre fusionné, `diag/20261109-070232-t06-reel` et `runs/20261109-070232-t06-reel` sont absents (test d'existence par le nom), et aucun fichier ne s'appelle `lecture-sondes-t06.json`.
- Fichiers ajoutés des deux côtés et identiques (fusion automatique, sans conflit) : `src/controle_ia/agregation_r1_v4/` (8 fichiers), `prereg/audit-fuite-r1-v4-v1.md` et son compagnon.
- Fichiers cités par la consigne comme conflits possibles : `.claude/hooks/garde_calcul.py` n'est pas touché par la branche (la version de `main` reste, 61 lignes ajoutées par rapport à `1609a4bf`) ; `tests/test_cibles_invisibles_v1.py` n'est modifié que par la branche (sa version est prise telle quelle). Aucun conflit de code ni d'essai : aucune union n'a été nécessaire.

## 2. Conflits et résolutions

Trois chemins en conflit, rien d'autre. Aucune autre modification de fichier que ces résolutions.

| Lieu | Version `main` | Version branche | Choix | Raison |
|---|---|---|---|---|
| `docs/notes/g0-deux-semaines-v1/e3-ter-v1/config-t06-course-explo-v1.json` (ajouté des deux côtés) | `1911a9e9e78bd5108886d3f1e3f21edd28f88b82e78b9a9bcfebe9898028e734`, `plafond_usd` 100, commit `3957504d` (8 novembre 15:33 UTC, « Instantanés en cours des sous-agents ») | `59e896b5a348a3d545d375cea148102e352d1c813f0939e1d99f3f1827e774b4`, `plafond_usd` 95, commit d'épreuve `be729130` (8 novembre 16:38 UTC), version jouée par 7a | version de `main` (`--ours`) | Deux versions scellées d'un même nom : arrêt R12 à 22:22 UTC, rapporté à la mère ; décision de la mère (additif, R-2055) : on n'écrase jamais. Seule différence : ligne 121. Aucun fichier de `src/`, `scripts/`, `tests/` ne cite ce fichier. Remarque CL-11 de `contre-lecture-regle-e3-6-transcription-v1-cl1.md`. |
| son compagnon `.sha256` (ajouté des deux côtés) | `1911a9e9…  config-t06-course-explo-v1.json` | `59e896b5…  config-t06-course-explo-v1.json` | version de `main` (`--ours`) | la version gardée égale son compagnon (vérifié) |
| `docs/notes/g0-deux-semaines-v1/e3-ter-v1/config-t06-course-explo-v1-joue-be729130.json` et compagnon (nom neuf) | — | contenu de `1609a4bf:docs/notes/g0-deux-semaines-v1/e3-ter-v1/config-t06-course-explo-v1.json`, octet pour octet | ajouté ; empreinte `59e896b5a348a3d545d375cea148102e352d1c813f0939e1d99f3f1827e774b4` vérifiée ; compagnon écrit par `controle_ia.scellement sceller` | additif, point 2 (R12 : nouvelle version, nouveau nom) |
| `registres/go.md` (modifié des deux côtés) | 290 lignes | 282 lignes | version de `main` en entier (`--ours`) | règle `registres/**` ; lignes de la branche absentes de `main` : **0** (donc aucun numéro R- à relever, rien d'ajouté) |

**Quel nom porte quelle empreinte** (additif, point 4 ; aucune note réécrite) :

- `config-t06-course-explo-v1.json` → `1911a9e9…` (`plafond_usd` 100, instantané de `main`, **pas** la version jouée) ;
- `config-t06-course-explo-v1-joue-be729130.json` → `59e896b5…` (`plafond_usd` 95, version jouée par 7a, celle que citent l'ordre de 7a, la r3 et la lecture A sous l'ancien nom).

Les notes qui citent `59e896b5…` sous l'ancien nom (par exemple `contre-lecture-ordre-course-exploratoire-v1-cl1.md`) désignent désormais le fichier au nom neuf ; celles qui citent `1911a9e9…` (par exemple `contre-lecture-chaine-t06-v13-cl1.md`, `rapport-config-explo-extracteur-v1.md`) désignent le fichier à l'ancien nom.

## 3. Contrôles avant commit

### 3.1 Chaîne v13

- `git diff --quiet 1609a4bf -- src/controle_ia/t06 scripts/lancer_t06_v13.sh scripts/amorce_instance_t06_v11.sh scripts/tests-cibles-t06-v3.txt` : **égal** (arbre et index avant commit ; refait sur le commit de fusion : égal).
- Neuf empreintes du point 15 de `brouillons/T0.6-organismes-v0-v1-candidat12-r3.md`, recalculées dans l'arbre fusionné (`sha256sum`) :

| Fichier | Attendue (point 15) | Arbre fusionné |
|---|---|---|
| `scripts/lancer_t06_v13.sh` | `6940a337d5e0c9a736aa7087275c5f6328133b67ed4df1c94535ba06a1965416` | égale |
| `scripts/amorce_instance_t06_v11.sh` | `43d856596f4ff934ae6faa445faed0d00aaaa264b23b0bda344b6888dcd5e859` | égale |
| `src/controle_ia/t06/session_v12.py` | `5b4ad5e9fa39c4a803050ed118157d005bcb30551a54a6822f38a15ca0ddd90e` | égale |
| `src/controle_ia/t06/lanceur_v6.py` | `e329493b5d54fe52f6eb278b1314a78f905ca082a51ee1a0c5c3a77bd400ac80` | égale |
| `src/controle_ia/t06/configuration_v6.py` | `7899622515588284d1045c72aee95d109ff755f525d3c4bcd70df14caf6fad8e` | égale |
| `scripts/tests-cibles-t06-v3.txt` | `e76d5e6b7c32140b549de20f061a2e562df9201c5daab4060fd1ca54a05f42e2` | égale |
| `scripts/tests-exclus-t06-v3.txt` | `ab70a1ed4b59bdb5f488e453055029806cde30c36552684f686097fbea8ed81c` | égale |
| `src/controle_ia/audit_fuite_r1_v4/bras_b_v4.py` | `317a7ea551abace1b3b78acde543688ab33bfda57cd15d8e6072f0826ce6fa17` | égale |
| `docs/notes/g0-deux-semaines-v1/scellement-course-t06-v1/rapport-preparation-scellement-course-t06-v1.md` « au commit `fe240b24` » | `0aebc62bf6ef9bb2714c91e5fa24f0b01c911edb4d7808d333a0182ec1c09a68` | absent de `main`, de `1609a4bf` et donc de l'arbre fusionné ; égale au commit cité `fe240b24` (branche `origin/prep/scellement-course-t06-v1`), comme le point 15 le dit |

Huit empreintes de code égales dans l'arbre fusionné ; la neuvième (un rapport, cité à son propre commit) est égale à ce commit et n'a pas à être dans l'arbre.

### 3.2 Périmètre gelé d'`exiger_code_cite`

Liste exacte (`src/controle_ia/harnais/validation_reelle.py`, `CHEMINS_GELES`, identique sur `main`, `1609a4bf` et l'arbre fusionné) : tout l'arbre (`.`) hors `prereg`, `brouillons`, `registres`, `docs`, `diag`, `runs`, `donnees`, `livrables`, `papiers`, `traces`, `CLAUDE.md` — conforme à la consigne.

Écarts entre `1609a4bf` et l'arbre fusionné dans ce périmètre : **108 chemins** (107 ajoutés, 1 modifié, aucun retiré), **tous égaux à `main` (`ff3e9a09`)** — la fusion n'y apporte rien qui ne soit déjà sur `main` :

| Catégorie | Nombre | Détail |
|---|---|---|
| `.claude/` | 1 modifié | `.claude/hooks/garde_calcul.py` (version de `main`, +61 −2 lignes par rapport à `1609a4bf`) |
| `src/` | 16 ajoutés (dont 4 compagnons) | `src/controle_ia/t07/` (6 fichiers : `__init__`, `criteres_v1`, `lecture_v1`, `mahalanobis_v1`, `plancher_v1`, `registre_v1`) ; `src/controle_ia/premier_test_ia/` (`lecture_p3bis_v1.py`, `ouverture_p3bis_v1.py`, `run_v2.py`, chacun avec compagnon) ; `garde_refus_question_v1.py`, `garde_refus_question_v2.py` ; `hote_durable_a1_v4_v5.py` et compagnon |
| `tests/` | 41 ajoutés | dont 14 compagnons ; essais de T0.7, de P3-bis, de `premier_test_ia/run_v2`, du dépôt expurgé v2 à v5, de l'idéation, des registres TAIF, de l'hôte durable, des gardes de refus, de l'agrégation de R1 v4 |
| `scripts/` | 30 ajoutés | dont 12 compagnons ; amorces P3-bis et hôte durable, dépôt expurgé v2 à v5, lanceurs d'idéation, dépôt OSF, registres TAIF, extracteur de la garde d'équivalence, vérificateur des jeux synthétiques de T0.7, liste `essais-cibles-p3bis-v1.txt` |
| `rapports/` | 20 ajoutés (dont 10 compagnons) | comptes rendus des filles « clés 1 », « clés 2 », « idéation 1 », « garde de l'ancienne mère » (avec compagnons) |

Conséquence pour le marqueur `COMMIT_CODE_T06` : citer `1609a4bf` fait refuser la garde sur tout arbre qui contient `main` (voir § 6) ; il faut citer le commit de fusion ou un descendant à arbre gelé égal.

### 3.3 Vérification de l'arbre scellé

`PYTHONPATH=src …/.venv/bin/python -m controle_ia.scellement verifier-arbre .` (22:25:33 UTC, avant le commit) : **72 problèmes**, au lieu de la seule orpheline attendue.

- 1 attendu : `docs/notes/ideation-organisme-v1/question-mere-reponses/consigne-argon-question-mere-v3.txt.sha256` (empreinte orpheline, déjà sur `main`).
- **71 non attendus** : 71 fichiers de `docs/notes/g0-deux-semaines-v1/` **apportés par la branche sans compagnon `.sha256`** (« empreinte compagnon absente »), ajoutés par 28 commits de la branche entre le 5 et le 8 novembre. Tous sont hors du périmètre gelé (sous `docs/`) : ils ne touchent ni la chaîne ni `exiger_code_cite`. Familles : bancs de mutations T0.6 v2 à v9 (20), journaux d'épreuves E0/E1 et d'essais d'amorce (11), rapports du développeur du lanceur v2 à v9 (8), configurations (jouet v3 à v5, épreuves E2/E3/E3 bis, réel brouillons 2 à 5, bras B : 12), ordres des filles et leurs pièces (8), bras B (manifeste des copies et dossier `bras-b-v2/` : 6), rapports bras B et échecs E3 (4), avancement v2 et v3 (2).
- Aucune empreinte fausse : tous les compagnons présents sont conformes (dont les 24 compagnons apportés par la branche).
- Le commit de fusion a été fait sans rien sceller (la consigne interdit toute autre modification que la résolution des conflits ; l'écart n'y est pas un motif d'arrêt et il est hors du périmètre gelé). Correction proposée à la mère, acceptée (routine, R6) : les 71 fichiers ont été scellés **sous leurs noms actuels**, par `PYTHONPATH=src …/.venv/bin/python -m controle_ia.scellement sceller`, dans un commit à part (§ 4). Aucun fichier scellé n'a été modifié : seuls 71 compagnons neufs ont été écrits (vérifié : les nouveaux fichiers sont exactement les 71 `<chemin>.sha256` attendus).
- Après ce commit (22:31:46 UTC), `verifier-arbre .` : **1 problème**, la seule orpheline attendue (`consigne-argon-question-mere-v3.txt.sha256`).

### 3.4 Garde des secrets et embargo

- `git diff --cached | grep -c -E '<motif de la consigne>'` : **0** avant le commit de fusion ; **0** avant le commit des sceaux ; **0** avant le commit du rapport.
- Noms de chemins de l'index comparés à l'embargo : 0.

## 4. Commits

- **Commit de fusion** : `7c00367b109ee0fad46df1c454bfb8439e93de93` (22:26:39 UTC ; parents `ff3e9a09` et `1609a4bf`), message « Intégration de la chaîne T0.6 v13 (1609a4bf) dans main (B1, R-2053) » et les deux lignes de fin demandées.
- **Commit des sceaux** : `00cc8fce4039c3161591f7f1007acf8772d9148a` (22:32:00 UTC), 71 compagnons ajoutés sous `docs/notes/g0-deux-semaines-v1/`, rien d'autre. Hors périmètre gelé : son arbre gelé est celui du commit de fusion (vérifié par la garde, § 6, cas 2 bis).
- **Commit du rapport** : ce fichier et son compagnon, à la suite (son identifiant est donné à la mère, il ne peut pas figurer ici).
- Tous locaux, sur `prep/integration-t06-v13-main-v1` ; rien de poussé.

## 5. Suite ciblée v3

- **Commande**, comme l'amorce v11 (l. 474 à 494) : depuis `/home/user/integ-t06`, `PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no <les 84 fichiers de scripts/tests-cibles-t06-v3.txt>`, avec `python` = `/home/user/controle-ia-travail/.venv/bin/python` (le répertoire `bin` de `.venv` placé en tête de `PATH`, comme une activation, pour que les sous-processus `python` des essais soient le même interpréteur). Liste vérifiée avant : empreinte `e76d5e6b…` égale à celle de l'amorce, 84 chemins bien formés, tous présents.
- **Arbre** : commit `00cc8fce` (fusion + sceaux ; arbre gelé égal à celui de la fusion `7c00367b`). Début 22:38:20 UTC, fin 23:27:31 UTC. Aucun fichier suivi par git n'a changé. Un seul fichier écrit sur disque hors de `src/`, `tests/` et `scripts/` : `docs/notes/g0-deux-semaines-v1/ordres-t06-e2-e3-v6/pieces/__pycache__/generer_ordres_v6_py311.cpython-313.pyc` (23:16 UTC, par `tests/test_t06_v11_nouveaux.py`, qui importe une pièce de `docs/`). Ce fichier est ignoré par git, mais `verifier-arbre` lit le disque et le signale (« empreinte compagnon absente ») ; je l'ai retiré après la suite (23:31 UTC), puis `verifier-arbre` ne signale plus que l'orpheline attendue. À savoir pour la routine R14 : une suite qui joue cet essai laisse ce faux problème dans l'arbre de la mère aussi.
- **Environnement** : `.venv` de la mère installée par `requirements-cpu.txt` (torch 2.14.1, transformers 5.18.0, pytest 9.1.1), processeur seul, une suite complète de la mère tournait en même temps. L'instance de 7a, elle, avait `requirements-gpu.txt`, qui ajoute `requirements-donnees.txt` (`pypandoc_binary==1.17`).
- **Dernière ligne** : « 5 failed, 2017 passed in 2947.94s (0:49:07) ».

| Passés | Échoués | Sautés | Total | Attendu |
|---|---|---|---|---|
| **2 017** | **5** | **0** | 2 022 | « 2022 passed » |

Le nombre d'essais recueillis est bien 2 022 ; mais l'amorce v11 s'arrête dès que pytest rend un code non nul (« tests en échec : arrêt »), avant le run.

**Échecs, cause et classement** (aucun fichier d'essai de la liste ne diffère de `1609a4bf` ; tous les écarts viennent de ce que l'arbre contient maintenant `main`, ou de l'environnement) :

| # | Essai | Cause | Classement |
|---|---|---|---|
| 1 | `tests/test_cibles_invisibles_v2.py::test_inventaire_tout_constructeur_d_invite_est_examine` | « constructeur(s) d'invite non examiné(s) : `controle_ia/premier_test_ia/run_v2.py::executer` → `charger_invite` ». `run_v2.py` (code de P3-bis, venu de `main`) n'est pas dans `REGISTRE` de l'inventaire v2 ; il était absent de `1609a4bf`, d'où les 2 022 passés de 7a. | **(b) défaut connu, R-2042** (révélé dans cet arbre par la fusion) |
| 2 | `tests/test_corpus_arxiv.py::test_traiter_papier_garde` | `ModuleNotFoundError: No module named 'pypandoc'` (`corpus_arxiv.chemin_pandoc`) | **(c) au sens strict de la consigne** (ni artefact de fusion, ni le défaut nommé), mais c'est l'**environnement processeur**, pas le code : déjà consigné à R-2042 (échecs 2 à 4) ; `corpus_arxiv.py`, l'essai et les fichiers `requirements-*.txt` sont identiques à `1609a4bf` ; attendu passant sous `requirements-gpu.txt` |
| 3 | `tests/test_corpus_arxiv.py::test_traiter_papier_trop_court_exclu` | idem | idem |
| 4 | `tests/test_corpus_arxiv.py::test_constituer_s_arrete_au_besoin_et_numerote` | idem | idem |
| 5 | `tests/test_t06_v13_liste.py::test_liste_reelle_et_exclusions_couvrent_exactement_les_fichiers_d_essais` | « fichiers d'essais ni dans la liste ni dans les exclusions motivées » : **27 fichiers de `tests/` venus de `main`** (tous sur `ff3e9a09`, aucun sur `1609a4bf`) ne sont ni dans `scripts/tests-cibles-t06-v3.txt` ni dans `scripts/tests-exclus-t06-v3.txt` : `test_agregation_r1_v4.py`, `test_agregation_r1_v4_v2.py`, `test_agregation_r1_v4_v3.py`, `test_depot_expurge_v2.py` à `_v5.py` (4), `test_essai_fermeture_p3bis_v1.py`, `test_extraire_garde_equivalence_t06_v1.py`, `test_garde_calcul_empreinte_lanceur_v3_v1.py`, `test_garde_refus_question_v1.py`, `test_garde_refus_question_v2.py`, `test_lancer_course_ideation_pilier_attaque_v2_v1.py` à `_v3.py` (3), `test_lanceur_durable_v5_a1v4.py`, `test_lanceur_durable_v5_a1v4_course_v1.py`, `test_osf_depot_v1.py`, `test_premier_test_ia_lecture_p3bis_v1.py`, `test_premier_test_ia_ouverture_p3bis_v1.py`, `test_premier_test_ia_run_v2.py`, `test_registres_taif_v1.py` à `_v3.py` (3), `test_script_p3bis_v1.py`, `test_t07_lecture_v1.py`, `test_verifier_jeux_synthetiques_t07_v2.py`. | **(a) artefact de fusion** |

Conséquence : **sur l'arbre intégré, la chaîne v13 telle quelle ne passe pas l'amorce v11** : sur l'instance (`requirements-gpu.txt`), les échecs 1 et 5 resteraient (les échecs 2 à 4 devraient disparaître), et l'amorce s'arrêterait après la suite, soit environ 35 à 50 minutes de carte. Les deux corrections (§ 8) touchent un essai et des listes : nouveaux noms (R12), donc nouvelle liste, nouvelle amorce (l'empreinte de la liste y est écrite en dur) et nouveau lanceur (le lanceur v13 écrit en dur `A=scripts/amorce_instance_t06_v11.sh`).

## 6. Essai à blanc des gardes

Joué le 9 novembre 2026 à 22:38:44 UTC dans un clone temporaire fait sous `/tmp` (répertoire de travail de la session, hors du dépôt) : `git clone --no-local --single-branch --no-tags --branch prep/integration-t06-v13-main-v1 /home/user/integ-t06`, dépôt d'origine retiré du clone aussitôt (aucune poussée possible), aucune autre branche copiée. La garde `exiger_code_cite` (code du clone, interpréteur de `.venv`) a lu un préenregistrement d'essai écrit dans un répertoire temporaire, qui ne contient que la ligne « Commit du code d'analyse : `<commit cité>` ». Les commits d'essai n'existent que dans le clone (auteur « essai »).

| Cas | Commit cité | HEAD du clone | Attendu | Obtenu |
|---|---|---|---|---|
| 1 | fusion `7c00367b` | fusion `7c00367b` | passe | **PASSE** |
| 2 | fusion `7c00367b` | `e02f3b4c` : fusion + une ligne ajoutée à `docs/notes/g0-deux-semaines-v1/avancement-v3.md` | passe | **PASSE** |
| 2 bis | fusion `7c00367b` | `00cc8fce` : le vrai commit des sceaux (71 compagnons sous `docs/`) | passe | **PASSE** |
| 3 | fusion `7c00367b` | `bc783acd` : fusion + une ligne de commentaire ajoutée à `src/controle_ia/t06/session_v12.py` | refus | **REFUS** « arbre gelé (code, tests, scripts, dépendances, configuration) modifié depuis le commit cité 7c00367b109e » |
| 4 | `1609a4bf` | fusion `7c00367b` | refus (B1, constat 1) | **REFUS** « … modifié depuis le commit cité 1609a4bf2c15 » |

La garde se comporte comme attendu, sur un cas sain et sur un artefact (R5). Le cas 4 confirme le constat 1 de B1 : le marqueur `COMMIT_CODE_T06` ne peut pas valoir `1609a4bf`.

**Non joué** (préenregistrement non scellé, ou réseau) :

- `exiger_citations_t06` (entropie, empreinte canonique de la configuration, tâches d'évaluation citées) et `exiger_prereg_scelle` : il n'existe pas de `prereg/T0.6-organismes-v0-v1.md` scellé ;
- `lancer_t06_v13.sh controles` : il fait `git fetch origin main` (réseau, interdit), exige que le commit de scellement S soit un ancêtre d'`origin/main` (la fusion n'y est pas), relit le texte de S et les sceaux des fichiers cités, et exige la présence des jetons (non vérifiée ici, aucune variable lue) ;
- la suite de l'amorce v11 sur une instance (liste v3, puis lanceur v6 avec `--prereg`) : aucune instance, aucune dépense.

## 7. Ce qui reste avant le scellement de T0.6

Ce qui suit est lu dans la consigne, B1 de la contre-lecture 3 (`prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r3-cl3.md`, `3930d4f9…`, § B1 et point 8) et le lanceur v13 ; je ne tranche rien.

1. **Faire entrer la fusion dans `origin/main`** (décision de la mère ou de Lazar : poussée vers le dépôt distant) : `controles` exige que le commit de scellement S soit un ancêtre d'`origin/main` et contienne l'amorce v11. Rien n'est poussé ici.
2. **Marqueur `COMMIT_CODE_T06`** (rempli par la mère) : le commit de fusion `7c00367b…` ou tout descendant de même arbre gelé (le commit des sceaux et celui de ce rapport le sont). Si `main` reçoit entre-temps un commit qui touche le périmètre gelé (code de T0.7, de P3-bis, `.claude/`, `scripts/`, `tests/`, `rapports/`, fichiers à la racine…), le commit cité doit être relevé de nouveau : la garde compare le commit cité à S sur tout l'arbre gelé, pas aux seuls fichiers de la chaîne.
3. **« Tests attendus »** : la valeur doit être le compte relevé sur l'arbre qui sera joué (§ 5). Avec la chaîne v13 telle quelle, l'arbre intégré donne 2 017 passés et 5 échoués (§ 5) : la valeur « 2022 » ne peut pas être écrite comme « 2022 passed » sur cet arbre ; il faut d'abord trancher les corrections 1 et 2 du § 8, puis rejouer la liste neuve sur l'arbre qui sera scellé et écrire le compte relevé.
4. **Gardes non jouées** (§ 6) : `exiger_citations_t06`, `exiger_prereg_scelle`, `controles` ; à jouer à blanc sur le texte scellé, dans un clone fait comme celui de l'amorce, avant la création.
5. **Hors de cette tâche, rappelés par la contre-lecture 3 (point 8)** : T0.7 scellé avant la création, rapport d'audit DT-4 scellé avant le scellement (R-2048), mot de Lazar pour 7b, branche de sortie neuve, calendrier (création au plus tard le 15 novembre).
6. **Nom de la configuration jouée par 7a** : les notes futures citent `config-t06-course-explo-v1-joue-be729130.json` pour `59e896b5…` (additif, point 4).

## 8. Corrections proposées (aucun code ni essai modifié)

Déjà faite, sur décision de la mère : **sceaux des 71 notes** apportées sans compagnon (§ 3.3, commit `00cc8fce`). Au passage : la configuration du brouillon 5 que cite la r3, `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon5.json`, était l'un de ces 71 fichiers ; son compagnon vaut maintenant `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527`, l'empreinte que cite la r3. Si le marqueur `CHEMIN_CONFIG_T06` désignait ce chemin, `controles` exigerait ce sceau à S.

Notée par la mère : **`COMMIT_CODE_T06`** = commit de fusion ou descendant de même arbre gelé (§ 7, point 2).

À trancher (rien n'a été écrit) :

1. **Échec 1, inventaire des constructeurs d'invite (b, R-2042)**. R-2042 renvoie le règlement à la contre-lecture du code de P3-bis. Texte proposé, à confirmer par cette lecture : `run_v2.executer` appelle `charger_invite("H1-classification")` sans en garder le résultat (l. 90), comme `run.executer` (l. 358), qui est déjà au registre sous `(EXEMPT, "chargement d'invite, sans tâche")`. Nouveau fichier `tests/test_cibles_invisibles_v3.py` = copie de la v2 avec une entrée de plus dans `REGISTRE` : `"controle_ia/premier_test_ia/run_v2.py::executer": (EXEMPT, "chargement d'invite, sans tâche (comme run.executer ; P3-bis, R-2042)")`. La v2 passe aux exclusions avec le motif « remplacé par tests/test_cibles_invisibles_v3.py (une entrée de plus : run_v2 de P3-bis, R-2042) ». Ne pas modifier la v2 sur place (R12).
2. **Échec 5, liste et exclusions (a)**. Nouveau fichier `scripts/tests-exclus-t06-v4.txt` = v3 + une ligne motivée par fichier pour les 27 essais venus de `main`, par exemple « essai de P3-bis : étranger au run de T0.6 », « essai de T0.7 : étranger au run de T0.6 », « dépôt expurgé, idéation, registres TAIF, hôte durable, dépôt OSF, gardes de refus, agrégation de R1 v4 : étrangers au run de T0.6 ». Deux fichiers demandent une décision plutôt qu'une exclusion d'office, parce qu'ils touchent T0.6 ou sa garde de calcul : `tests/test_extraire_garde_equivalence_t06_v1.py` et `tests/test_garde_calcul_empreinte_lanceur_v3_v1.py`. Ensuite :
   - un nouvel essai `tests/test_t06_v14_liste.py`, copie de `tests/test_t06_v13_liste.py` qui lit la liste v4, les exclusions v4 et l'amorce neuve ;
   - une liste `scripts/tests-cibles-t06-v4.txt` = v3 − `tests/test_cibles_invisibles_v2.py` − `tests/test_t06_v13_liste.py` + `tests/test_cibles_invisibles_v3.py` + `tests/test_t06_v14_liste.py`, plus ceux des deux fichiers ci-dessus qui seraient listés.
3. **Conséquences de 1 et 2 sur la chaîne** (R12 et B1, « correction ») :
   - une amorce neuve `scripts/amorce_instance_t06_v12.sh` : v11 avec `LISTE_TESTS` et `LISTE_SHA256` de la liste v4, l. 474 ;
   - un lanceur neuf `scripts/lancer_t06_v14.sh` : v13 avec `A=scripts/amorce_instance_t06_v12.sh`, l. 80 ;
   - les essais qui citent la chaîne en dur à revoir sous des noms neufs : `tests/test_t06_chaine_v13.py` (11 mentions) et `tests/test_t06_v13_liste.py` (9 mentions) ;
   - une contre-lecture de ce code neuf ;
   - au texte : les empreintes du point 15, la ligne « Amorce » (`EMPREINTE_AMORCE_T06`) et « Tests attendus » à refaire.

   Tant que ce n'est pas scellé, tout essai ajouté à `tests/` sur `main` refera échouer l'essai de liste. Il faudra donc geler `tests/` ou relever la liste juste avant le scellement.
4. **Autre voie, non jouée, à examiner par la mère** : sceller le texte dans un commit S **dont le parent est `1609a4bf`**, sur la lignée de la chaîne, puis fusionner S dans `main`. Avec ce montage :
   - S est un ancêtre d'`origin/main` et contient l'amorce v11 ;
   - son arbre gelé est celui de `1609a4bf`, donc le commit cité peut rester `1609a4bf` ;
   - la suite v3 y porte sur l'arbre de `1609a4bf`, celui des « 2022 passed » relevés sur l'instance de 7a et par la mère (r3, en-tête, « Tests attendus ») ;
   - aucune chaîne v14 n'est nécessaire.

   À vérifier avant de la retenir :
   - les fichiers cités par le texte doivent être présents et scellés à S : configuration, tâches, consignes de P3 ;
   - en particulier, le sceau de `config-t06-reel-v1-brouillon5.json` manque sur `1609a4bf` ; il faudrait l'y ajouter dans S, ou copier la configuration sous `prereg/` ;
   - `registres/go.md` de S serait celui de la branche (282 lignes ; la ligne GO-2026-11-02-28 y est, 5 mentions comme sur `main`) ;
   - la compatibilité avec la lecture de B1 (« construire le commit d'intégration sur `main` »).
5. **Échecs 2 à 4, `pypandoc` (environnement)** : aucune correction de code. Pour les rejeux locaux, installer `requirements-donnees.txt` (`pypandoc_binary==1.17`) dans `.venv`, sur décision de la mère : téléchargement depuis le dépôt de paquets. Ou bien lire ces trois essais comme « environnement » à chaque rejeu sur processeur, comme R-2042. Sur l'instance, `requirements-gpu.txt` les couvre.
