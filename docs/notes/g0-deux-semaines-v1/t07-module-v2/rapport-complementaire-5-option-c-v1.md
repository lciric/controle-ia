# T0.7, module v2 — rapport complémentaire 5 : option (c) des phrases des concepts, reprise du travail interrompu — v1

- **Auteur** : sous-agent développeur **neuf** (Claude Opus 5.5, `claude-opus-5-5`) de la session mère ; n'a écrit ni T0.7, ni
  ses contre-lectures, ni le module, ni le travail interrompu repris ici. Écrit le 2026-11-10 à partir de 12:35:54 UTC (heure
  relevée par `date -u`).
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-module-t07-option-c-reprise-v1.md`,
  `fdb2470613394e9143cd57bd7f249bc1f765101ec077f289ca93a9e4c1205af5` (vérifiée contre son compagnon à 11:38 UTC), et le
  message de la mère reçu en cours de travail (essai `test_mahalanobis_miroir_egal_a_familles_v2_au_commit_8cb539f9`, § 8).
- **Arbre** : `/home/user/wt-t07-module-v2`, branche `prep/t07-module-v2`, tête de départ `88e80ba0` ; aucune poussée.
- **Pièces lues** : R-2153, R-2155, R-2158, R-2166, R-2183 (`registres/decisions.md`) ; brouillon 21 de T0.7
  (`brouillons/T0.7-sondes-v0-v1-brouillon21.md`, `f7dcb226efe8671b977ce906c286f7e7243f78a2c9fcf205cbfe5715866ea0cc`, empreinte
  recalculée) : en-tête l. 179, 185-186, plan l. 1279, point 10 l. 1402-1405, écrits l. 1449 et 1477, R15 l. 1794, table des
  lignes l. 2080, « Accord au code » point 20 l. 2536 ; rapport complémentaire 4 (`57b4f7f6…`, recalculé) ; contre-lecture courte
  `contre-lecture-code-t07-v3-differentiel-court.md` (`d0fe90538160779ea6386a9f3a622ca0636575631254a76a5bec857915e4e8c6`,
  recalculé) ; consigne v3 corrigée des concepts `docs/procedures/consigne-concepts-sans-lien-T0.7-v3-corrigee-v1.md`
  (`ea5fe3f05ab5ae070e38a0ecc28c73ea96de15e34a2250ddab9d000044f6096e`, égale à son compagnon) : format du fichier final
  inchangé (§ 2 : clés exactement `concept`, `indice`, `phrase_concept`, `phrase_neutre`, quatre concepts), donc lisible par
  `sondes_neuves_v1.lire_phrases_concepts` sans changement.

## Verdict

**Prêt pour contre-lecture courte**, au commit proposé pour `CODE-T07` : **`37485ce50601b7d7ff9035bc34c734ec689ca731`**
(`src/` égal à `ae49f55d` ; `src/` et `tests/` égaux au commit `16f59d63` de la répétition conforme). Une **réserve d'environnement**
(§ 8) : l'essai du miroir de `familles_v2` échoue dans ce clone (commit `8cb539f9` absent) ; elle bloque la ligne d'essais de
l'instance tant que la mère ne la tranche pas.

## 1. Ce que faisait le travail interrompu (`13e7f85a`, nettoyé par `88e80ba0`)

`git diff a4352e6a 88e80ba0 -- src tests scripts` : six fichiers.

| fichier | contenu du travail interrompu | jugement après relecture ligne par ligne |
|---|---|---|
| `src/controle_ia/t07/registre_v1.py` | `SCELLEMENT_CONCEPTS_T07` retirée de `EXIGEES_ETAPE_A`, ajoutée à `PERMISES_ETAPE_A` | conforme (point 20 (i)) |
| `src/controle_ia/t07/lecture_v2.py` | `lire_jeux_et_phrases` : jeux lus sans condition sur la ligne des concepts, phrases lues seulement si leur ligne précède **strictement** l'instant de fermeture, au moins `min_concepts` (4 en réel), sinon `phrases` nul et `phrases_etat` (« non lues », motif, ligne absente ou exclue pour de bon) ; `ouvrir` : jeux lus dès l'étape complète (plus de condition sur la ligne) ; `etape_a` : tâches `plancher-concept/…` seulement avec des phrases ; état des phrases dans `extras` et `sondes-t07.json` ; `noter` : état dans l'index des scores ; `reserve_couches_repli` (réserve « couches … non vérifiées » sous le repli, brouillon 21, plan, point 8, CLT7B-12) | conforme ; **complété** (§ 2) |
| `src/controle_ia/t07/lectures_t07_v1.py` | phrase R15, constantes d'état, T7-P9 « non lue : jeu des phrases des concepts non scellé à l'ouverture » si l'index le dit, R15 dans `reserves` | conforme ; **complété** (§ 2) |
| `tests/test_t07_option_c_concepts_v1.py` | dix essais : clé permise ; cas sain ; ligne absente ; ligne postérieure (artefact) ; ligne juste avant ; trois concepts en réel → refus ; réserve des couches (fonction, bout en bout) ; repli sans `RUN-CONFIRMATION-T06` ; repli sans la ligne des concepts | conformes, joués ; **complétés** de huit essais (§ 2) |
| `tests/test_t07_repli_etapes_v1.py` | l'ancien artefact (retrait de `SCELLEMENT-CONCEPTS-T07` → refus) marqué `xfail(strict=True, raises=pytest.fail.Exception)`, remplacé par l'essai sur `RUN-CONFIRMATION-T06` | gardé tel quel, déclaré : l'échec attendu prouve que l'ancienne règle n'agit plus (« DID NOT RAISE ») |
| `scripts/etape_a_t07_variante_b_v2.sh` | v2 du script de l'instance (v1 intacte) : O-1 (essais avant le modèle, mode mesure), O-2 (taille bornée, découpage), O-3 (DELETE journalisés), O-5 (registres nommés), C-1 (`PERIMETRE` exigé, `CONCEPTS` compris), O-6 | **un défaut trouvé à la lecture et corrigé** (§ 3) ; **jamais répété** avant cette reprise : répétition v2 écrite et jouée (§ 5) |

## 2. Ce que j'ai corrigé ou complété

1. **Garde neuve, étape A** (`lecture_v2.py` l. 902-904) : sans phrases lues, un apprentissage qui rendrait des directions de
   concept arrête l'étape après le manifeste (`ArretApresManifeste`), rien n'est noté (aucun repli silencieux, R5).
2. **Garde neuve, étape B** (`lectures_t07_v1.py` l. 245-248) : un index des scores qui porte des directions alors que l'état
   des phrases dit « non lues » arrête l'étape B (jamais T7-P9 lue ni R15 écrite en silence).
3. **État des phrases au manifeste** (`lecture_v2.py` l. 860-862) : `phrases_concepts_etape_a`, fixé à l'ouverture, écrit dans la
   configuration du manifeste, avant toute graine dérivée ; les tâches `plancher-concept/<concept>/c<couche>` restent au manifeste
   quand les phrases sont lues (l. 850-851) — c'est ma lecture de « plancher de concept gardé au manifeste » (R-2166 ; point
   ouvert 3).
4. **Essais neufs** (`tests/test_t07_option_c_concepts_v1.py` l. 203-295) : manifeste (lues, non lues) ; deux artefacts (gardes 1
   et 2) ; variante B de bout en bout : ligne inscrite **après la garde du repli** (qui ferme le périmètre, C-1) → exclue ; ligne
   avant → lue.
5. **Script de l'instance v2** : `registres/go.md` nommé (§ 3).
6. **Répétition v2** (fichier neuf) et **banc de mutations** (fichier neuf) : § 5 et § 6.

## 3. Défaut du script v2 trouvé à la lecture

La première forme de `scripts/etape_a_t07_variante_b_v2.sh` (O-5) ne recopiait plus que quatre registres nommés ; la v1
recopiait tout `registres/*.md`, donc `registres/go.md`. Or la garde lit `registres/go.md` pour vérifier que l'extrait de la
ligne `GO-LECTURE-T07` en est une ligne (`registre_v1.verifier_lignes`, `FICHIER_GO`) : sans lui, la garde du repli aurait
refusé l'étape A sur l'instance. Corrigé (l. 100-102 : `registres/go.md` nommé, jamais `registres/index-bras-attaque*`) ;
constaté par la répétition (« registre registres/go.md recopié de main », garde passée). Défaut **non démontré** sur l'ancienne
forme (aucun passage joué avec elle) : constat de lecture.

## 4. Exigences de R-2166 (brouillon 21, « Accord au code », point 20), code et essais

Lignes au commit `37485ce5`.

| exigence | code | essais (cas sain / artefact) |
|---|---|---|
| (i) clé `SCELLEMENT-CONCEPTS-T07` passée des exigées aux permises | `registre_v1.py` l. 67-71 (commentaire, `EXIGEES_ETAPE_A = (RUN_CONFIRMATION_T06,)`) | `test_cle_des_concepts_permise_et_non_exigee` ; `test_repli_sans_ligne_des_concepts_garde_passee` ; `test_repli_ligne_exigee_manquante_rien_calcule_puis_relance` (seule exigée manquante → refus, rien calculé) ; ancien artefact en `xfail` strict |
| (ii) jeux génériques lus sans condition sur la ligne des concepts | `lecture_v2.py` l. 500-503 (`ouvrir`) et l. 295-300 | `test_ligne_absente_etape_A_au_bout_T7P9_non_lue_R15` (30 couples appris sans la ligne) ; mutation m7 tuée |
| (ii) phrases lues seulement si leur ligne précède **strictement** l'instant de fermeture | `lecture_v2.py` l. 301-310 | sain : `test_ligne_avant_la_fermeture_T7P9_lue_sans_R15`, `test_ligne_juste_avant_la_fermeture_lue`, `test_variante_B_ligne_avant_la_garde_du_repli_lue` ; artefact : `test_ligne_posterieure_a_la_fermeture_exclue_pour_de_bon`, `test_variante_B_ligne_inscrite_apres_la_garde_du_repli_exclue`, et la ligne à l'instant même (`test_trois_concepts_…`, cas `y`) ; mutations m1, m2 tuées |
| (ii) quatre concepts au moins en réel ; moins → refus | `lecture_v2.py` l. 303 et l. 501 (`4 if config["mode"] == "reel" else 1`) | `test_trois_concepts_en_mode_reel_refus_quatre_exiges` ; mutation m6 tuée |
| (ii) aucune phrase → aucune direction, aucune tâche de plancher de concept au manifeste | `sondes_neuves_v1.py` l. 466 (déjà conditionnel) ; `lecture_v2.py` l. 850-851 ; garde neuve l. 902-904 | `test_ligne_absente_…`, `test_manifeste_sans_ligne_etat_non_lues` ; artefact `test_artefact_directions_apprises_sans_phrases_arret` ; mutations m9, m12 tuées |
| plancher de concept gardé au manifeste (lu) ; état des phrases au manifeste | `lecture_v2.py` l. 850-851, 860-862 | `test_manifeste_porte_l_etat_des_phrases_lues_et_non_lues` ; mutation m11 tuée |
| (iii) T7-P9 « non lue : jeu des phrases des concepts non scellé à l'ouverture » | `lectures_t07_v1.py` l. 66-69, 245-253 ; état transmis par l'index (`lecture_v2.py` l. 679, 925, 943) | `test_ligne_absente_…`, `test_ligne_posterieure_…` ; artefact `test_artefact_index_incoherent_T7P9_arret_a_l_etape_B` ; mutations m5, m8, m10 tuées |
| (iii) réserve R15 écrite (phrase du brouillon 21, l. 1794) | `lectures_t07_v1.py` l. 64, 492-494 | sain : absente quand lues (`test_ligne_avant_…`) ; présente, une fois, motif « absente » (`test_ligne_absente_…`) ou postérieure ; mutation m4 tuée |
| (iv) étape A menée au bout sans la ligne (repli écrit) | ensemble ci-dessus | `test_ligne_absente_…` ; répétition, passage « sans concepts » (§ 5) |
| (v) contre-lecture courte et répétition jouet au commit neuf | — | répétition faite (§ 5) ; contre-lecture : à la mère |

## 5. Répétition jouet du script de l'instance v2 (sans réseau, sans carte, sans modèle descendu, sans Vast)

`scripts/repetition_jouet_variante_b_t07_v2.py` (fichier neuf ; la v1 reste intacte). Arbre de T0.6 du commit `1609a4bf`
**matérialisé par `git show`** (232 fichiers : `src/`, `docs/sources/invites-2606.08892-v1/`, les deux fichiers de P3, `registres/go.md`,
configuration jouet), jamais extrait par `checkout` ; deux dépôts distants locaux (avec et sans la ligne des concepts à `main`) ;
script joué tel quel par `bash` sous un environnement vidé (`GH_TOKEN` factice, clé d'instance factice).

| passage | heures (UTC) | commit | issue |
|---|---|---|---|
| 1 | 11:56:57 | `04bc14a2` | course 7b jouet en code 1 : `docs/sources/invites-2606.08892-v1/index.json` absent de l'arbre matérialisé — défaut de la répétition, corrigé (`41cbb02e`) |
| 2 | 11:58 | `41cbb02e` | course 7b en code 0 ; la répétition lisait le registre après le passage du dépôt jouet sur la branche de 7b — défaut de la répétition, corrigé (`3ff4087e`) |
| 3 | 11:58:40 à 12:05:13 | `3ff4087e` | cinq passages conformes (normal, sans concepts, deux artefacts, mesure) |
| **4** | **12:08:05 à 12:17:53** | **`16f59d63`** | **douze verdicts conformes** (ci-dessous) |

Passage 4, détail :

- **normal** (`PERIMETRE=JD,JA,JC,CONCEPTS`) : code 0 ; `CODE-T07 conforme` (18 fichiers) ; repli : garde d'ouverture, recalcul,
  garde d'équivalence (21 actions, écart 0) ; passe à blanc tenue ; étape A code 0 ; `SCORES-T07` et `SONDES-T07` poussées ;
  phrases **lues**, 6 directions, 6 tâches de plancher de concept ; `src` et `tests` inchangés.
- **sans concepts** (`PERIMETRE=JD,JA,JC`, ligne absente de `main`) : code 0, étape A au bout ; phrases **non lues**
  (« absente ») dans `sondes-t07.json` et au manifeste ; 0 direction, 0 tâche de plancher de concept.
- **artefact, branche déjà poussée** : code 2 avant tout repli (R12). **Artefact, périmètre faux** (`CONCEPTS` exigée, ligne
  absente) : code 2, « rien n'est ouvert », avant tout repli (C-1).
- **mesure** (`ARRET_APRES_ESSAIS=1`) : ligne mesurée « 20 passed », égale à la ligne attendue de la liste réduite.
- **découpage (O-2)**, seuil d'essai 100 000 octets, morceaux de 40 000, lots de 2 : `scores-actions-t07.npz` (130 685 octets) et
  `sondes-neuves-t07.npz` (143 535) découpés en 4 morceaux scellés chacun, poussés en quatre commits ; originaux absents de la
  branche ; recomposition égale au manifeste des morceaux, au compagnon et aux lignes `SCORES-T07` / `SONDES-T07` ; aucun fichier
  ajouté au-dessus du seuil.
- **minuterie (O-3)**, contre une API locale (127.0.0.1) : saine, un DELETE journalisé « HTTP 200 » ; en échec, cinq DELETE
  journalisés « HTTP 500 », puis « destruction laissée à la session (R10) » ; dans les deux, état « stopped » demandé par PUT
  (corps `{"state": "stopped"}`), en-tête porteur présent, aucune valeur de clé journalisée.
- Embargo : `lecture-sondes-t06.json` (factice de la course jouet) ni dans l'arbre de l'instance, ni descendu (objet manquant du
  clone partiel) ; jamais ouvert par la répétition.

Pièces scellées sous `docs/notes/g0-deux-semaines-v1/t07-module-v2/repetition-jouet-variante-b-v3/` :

| pièce | sha256 |
|---|---|
| `resume-passage1.json` | `a21e5789139dcaf1f23680367f718bc7ed136482f06e07f5fb65e9b9c8d41619` |
| `journal-passage2.txt` | `25c1b0ec9a0509553723a836052a39ccc2f2e88febe2766de533b55a305fef12` |
| `journal-passage3.txt` | `350656bec7717f46e0a505782353a6c126a4b0d6c0e8521bdf3c3fe131f8292a` |
| `resume-passage3.json` | `dc0a7ecaa8d8cc9374a3b05ea5da8fae6ace503a53b415e22eac99812958eb80` |
| `journal-passage4.txt` | `7ca315daacdb0108d5d735d5bdb3619c3849e066ce6b16dff9d0eaaeef1244d2` |
| `resume-passage4.json` | `6c6f2c8ded07017373d8cb9d50a47f0d5e45a61ba5f0ef24c8a334fa4ebf84f6` |

Script de l'instance joué : `scripts/etape_a_t07_variante_b_v2.sh`,
`e68d3306bd76a549ec97eb6b153d03ec544c92944ae74293d8c0db8cfda62269`. Non répétés (réel seulement) : Vast, installation des
paquets, descente du modèle, carte, ligne d'essais complète dans le clone de l'instance (§ 8).

## 6. Banc de mutations

Aucun banc de mutations du module T0.7 n'existait (seuls ceux de T0.6 et du bras B). Banc neuf :
`scripts/banc_mutations_t07_option_c_v1.py` (chaque mutation appliquée à `src/controle_ia/t07/`, essais de l'option (c) joués,
fichier rétabli octet pour octet, sha256 contrôlé). Passe du 2026-11-10, 12:18:15 à 12:24:49 UTC, au commit `16f59d63` (arbre
propre) : **12 mutations, 12 tuées** (m1 lecture sans condition de fermeture ; m2 « ≤ » ; m3 clé redevenue exigée ; m4 R15 jamais
écrite ; m5 état absent de l'index ; m6 minimum de concepts ignoré ; m7 jeux liés à la ligne ; m8 T7-P9 mal nommée ; m9, m10 gardes
neuves retirées ; m11 état absent du manifeste ; m12 tâches de plancher sans phrases). Résultat :
`docs/notes/g0-deux-semaines-v1/t07-module-v2/banc-mutations-t07-option-c-v1.json`,
`0b54c163556cd683a420c8d981a18dc9b8ed134c715e945e5237c95d535aca33`. Une première passe ponctuelle (huit mutations, bac à sable,
11:51 à 11:57 UTC) avait aussi tué les huit.

## 7. Commandes et comptes d'essais

Toutes depuis l'arbre, `PYTHONPATH=src`, interpréteur `/home/user/controle-ia-travail/.venv/bin/python`, `--basetemp` et `TMPDIR`
dans le bac à sable de l'agent, `-p no:cacheprovider`.

| essais | heures (UTC) | compte |
|---|---|---|
| `tests/test_t07_option_c_concepts_v1.py tests/test_t07_repli_etapes_v1.py` (travail interrompu, avant tout changement) | 11:38 à 11:40 | 18 passés, 1 xfail |
| tous les `tests/test_t07*.py` + `tests/test_verifier_jeux_synthetiques_t07_v2.py` (première passe, arbre de `88e80ba0`) | 11:41:55 à ≈ 11:48 | **invalide** : disque partagé plein (`OSError: No space left on device`), 112 erreurs ; seul constat retenu : l'échec du miroir (§ 8), à la l. 1055, avant tout usage du module |
| essais neufs (`-k "manifeste or artefact or variante_B"`) | ≈ 11:50 | 6 passés |
| les deux artefacts, gardes retirées (contrôle de mutation) | ≈ 11:52 | 2 échecs (attendus) |
| **tous les `tests/test_t07*.py` (17 fichiers) + `tests/test_verifier_jeux_synthetiques_t07_v2.py`, `-o tmp_path_retention_policy=none`, un processus** | **12:25:00 à 12:35:14** | **403 passés, 2 sautés, 4 xfail, 1 échec** (612,9 s) |

- Sautés : `test_t07_lecture_v1.py` l. 504 (branche `origin/prep/t06-candidat8-v1` non récupérée, déclaré) ; `test_t07_lecture_v2.py`
  l. 911 (commit `061ac380` absent de ce clone, déclaré ; il était présent au rapport 4).
- Échecs attendus (4) : CT-01, CT-11, cas sain du journal (déjà au rapport 4) ; plus l'ancien artefact du repli (§ 1).
- Échec (1) : `test_mahalanobis_miroir_egal_a_familles_v2_au_commit_8cb539f9` (§ 8).
- La suite complète du dépôt n'a pas été lancée (interdits communs, règle 5).

## 8. Essai `test_mahalanobis_miroir_egal_a_familles_v2_au_commit_8cb539f9` (question de la mère)

- **Il échoue aussi dans cet arbre, avant et après mes changements** : première passe (lancée à 11:41:55 UTC sur l'arbre de
  `88e80ba0`) et passe finale (12:25 à 12:35 UTC, commit `37485ce5`) ; même assertion, l. 1055 :
  `commit 8cb539f9 introuvable dans le clone : miroir non comparable (fatal: invalid object name '8cb539f9'.)`.
- **Cause** : l'objet `8cb539f9` n'est pas dans le dépôt local (`git cat-file -t 8cb539f9` : objet inconnu ; dépôt commun
  `/home/user/controle-ia-travail/.git`, non superficiel ; `061ac380` absent aussi). L'essai lit `git show 8cb539f9:…` et, par
  construction (« jamais sauté »), échoue quand le commit manque. Le module n'y est pour rien : `mahalanobis_v1.py` est inchangé
  depuis `8ae9fc44`, et l'assertion échoue avant toute lecture de lui. Le dépôt étant complet pour `main` (non superficiel) et
  l'objet absent, `8cb539f9` n'est pas ancêtre de `main` local (inférence, non vérifiée sur le dépôt distant).
- **Hors de mon périmètre** (il faudrait récupérer l'objet : `fetch` interdit ; ou changer la règle de l'essai, fixée par le texte,
  brouillon 12, marqueur 8, brouillon 14, en-tête). **Réserve**, avec une conséquence pour l'ordre d'exécution : dans le clone
  `--single-branch --branch main` de l'instance, l'objet manquera aussi ; le script v2 exige `code 0` **et** la ligne attendue à
  l'étape 6 : **l'étape A s'arrêterait aux essais** (code 2), comme O-1 l'avait trouvé pour `061ac380` (qui, lui, se saute).
  Remèdes possibles, à la mère : rendre `8cb539f9` atteignable depuis `main` (fusion d'une branche qui le porte), ou mesurer la
  ligne dans un clone de l'instance (mode `ARRET_APRES_ESSAIS`) et décider de l'écart avant l'ordre brouillon 4.

## 9. Commit proposé pour `CODE-T07`

**`37485ce50601b7d7ff9035bc34c734ec689ca731`** : différentiel du module depuis `8ae9fc44` limité à `lecture_v2.py`,
`lectures_t07_v1.py`, `registre_v1.py` (61 lignes ajoutées, 10 retirées) ; `src/` égal à `ae49f55d` et au commit `16f59d63` de
la répétition conforme. Fichier `CODE-T07` écrit à blanc dans le bac à sable par
`python -m controle_ia.t07.code_t07_v1 ecrire . 37485ce5… <sortie>` : 18 fichiers, non versé (c'est à la mère de l'écrire et de
l'inscrire). Empreintes :

| fichier | sha256 |
|---|---|
| `src/controle_ia/t07/__init__.py` | `553bd9d29b56f0923859da2d3a63fadf9891c4274b9bb23fc367496e77e5a61e` |
| `src/controle_ia/t07/code_t07_v1.py` | `52f44ce039d63813cf406b4827d3bf369f2523831dd58f01101a49520cdf01ec` |
| `src/controle_ia/t07/controle_jeux_v1.py` | `27cf1fba9584f41632af4b352b048ecf46e8cc53695499385dd8c8eddc92a3ae` |
| `src/controle_ia/t07/criteres_v1.py` | `12b999fecce093372a29fb70d8c11eb7fe965f34c8746a31b399baaecc5ae8c5` |
| `src/controle_ia/t07/donnees_p3_t07_v1.py` | `acf02303b98157411dd30881d19ec9457423afdc7c27ef4e9342823234030cf4` |
| `src/controle_ia/t07/garde_adaptee_v1.py` | `7ff571d7b1f06db94043545bfe178a066613ddd734aacca1cf3ef52ba0b511de` |
| `src/controle_ia/t07/journal_p3bis_v1.py` | `f83f03d54accc0ac189e05c2f3e865b27ecb817f6c9366836d6e38d016826f73` |
| `src/controle_ia/t07/lecture_v1.py` | `62b34790346123924c275c4e2021ea31db26837c5b7840e9e047d272a54c9678` |
| `src/controle_ia/t07/lecture_v2.py` | `709b2febac4bcee308b66400764d7ed87115dd991c4ab79f57467d1464d7c69e` |
| `src/controle_ia/t07/lectures_t07_v1.py` | `01904d94c0f636a4fcec8df85071420f33041d61727f5408d647ea43d7df5c01` |
| `src/controle_ia/t07/mahalanobis_v1.py` | `b28163062aa8d39cf3894b327a7446f63d50d4f1394eac894b16b4da8ff962f9` |
| `src/controle_ia/t07/passe_blanc_v1.py` | `ff84d2450d5b4a4b39db8ca7d042805a8efd8261349d0608de0e65442fdab578` |
| `src/controle_ia/t07/plancher_v1.py` | `ac6e8263293ed30c807ef91f8eab0adbcbf8e1b91d5e4c56e73dbffa1a7099dc` |
| `src/controle_ia/t07/registre_v1.py` | `e50236574fbcd7e48ea3005eadc8bdb68d2c753d10028db7f2c365648a843cec` |
| `src/controle_ia/t07/repli_etapes_v1.py` | `26a6b52151a29f3b65ba4c48027a3ed70890f71fc262ca16bba3e51531dfaff2` |
| `src/controle_ia/t07/repli_recalcul_v1.py` | `9ceabbcb56cacde0cad6e849a36884139b0175bdf20af5e34cf4514d9da3fe1d` |
| `src/controle_ia/t07/repli_v1.py` | `7ae5862da1c867d99cbbdfa0c2350a238920c314a8924254abaf368dd335223a` |
| `src/controle_ia/t07/sondes_neuves_v1.py` | `d4d354e769de279235a202b1ac803b6b508bb12a374f48d0352db13daaab9bc7` |

Commits de la reprise sur `prep/t07-module-v2` : `ae49f55d` (jalon 1, module et essais), `04bc14a2`, `41cbb02e`, `3ff4087e`,
`16f59d63` (jalons 2 à 2 quater, script et répétition), `37485ce5` (jalon 3, banc et pièces), puis le commit de ce rapport.

## 10. Points ouverts

1. **Miroir de `familles_v2`** (§ 8) : réserve d'environnement, bloquante pour la ligne d'essais de l'instance ; à trancher par la
   mère avant l'ordre brouillon 4.
2. **R15 n'est écrite que si les scores sont ouverts** : `reserves` n'est appelée qu'avec les lectures complémentaires (comme
   R10, « toujours écrite », qui l'est aussi seulement là) ; scores fermés (L1, etc.), T7-P3 à T7-P19 sont « non lues » et R15
   n'apparaît pas dans `lecture-t07.json`, mais l'état des phrases est dans `sondes-t07.json` et au manifeste. Lecture à confirmer
   au texte (« réserve écrite dans le résultat »).
3. **« Plancher de concept gardé au manifeste »** (R-2166) lu comme : tâches `plancher-concept/…` au manifeste quand les phrases
   sont lues, absentes sinon, et état des phrases écrit au manifeste. Si la mère entendait autre chose, à dire.
4. **Étape A non complète** (jouet de la v2 initiale) : aucune phrase lue, T7-P9 « non lue : aucune direction de concept notée »,
   pas de R15 — inchangé, hors du réel.
5. **Passe à blanc** : lit les phrases si leur ligne existe, sans condition de fermeture (`passe_blanc_v1.py` l. 236-252) ; sans
   effet sur l'instance (registre local figé au clonage ; aucune donnée décisive), déclaré au brouillon 21.
6. **Docstring périmée** : `lecture_v1.py` l. 27 dit encore `SCELLEMENT-CONCEPTS-T07` exigée ; non touchée (fichier v1, aucun
   effet sur le code) ; à corriger à la prochaine version.
7. **Écarts déclarés** : lectures de commits par `git diff a4352e6a 88e80ba0` (prescrit par la consigne), `git diff 1609a4bf
   HEAD -- src/controle_ia/t06 …` (vide) et `git ls-tree` / `git show` de `1609a4bf` par la répétition ; la répétition (comme sa
   v1, rendue) fait des `checkout` et `push` dans **ses dépôts jouets** du bac à sable, jamais dans le dépôt du programme ; le
   disque partagé s'est rempli pendant la première passe (mes dossiers d'essais supprimés, aucun autre).
8. **Ordre brouillon 4** : la ligne attendue des essais (`ATTENDU`) doit être mesurée dans le clone de l'instance (O-1) ; le
   comportement de l'option (c) au script est répété (passage « sans concepts », `PERIMETRE` sans `CONCEPTS`).
