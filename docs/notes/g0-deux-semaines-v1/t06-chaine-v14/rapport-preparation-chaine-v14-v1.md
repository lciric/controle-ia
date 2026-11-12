# Préparation de la chaîne v14 de T0.6 (lanceur et amorce qui lisent le GO dans la configuration), sans adoption — rapport v1

- Auteur : développeur neuf (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5) ; n'a écrit ni la chaîne de T0.6, ni T0.6, ni T0.7, ni P3-bis, ni leurs contre-lectures.
- Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-preparation-chaine-t06-v14-v1.md` (`16d9a990c3e51de0732f41090678c6f01d3c02e0c19a6f7a9df50087c07b4154`, vérifiée avant lecture) ; interdits communs `851028fc2f425cee8e64613db20f6a2e2a7c289d07dd5441a9993d24630682a6` (vérifiés).
- Lieu : arbre lié `/home/user/wt-t06-v14`, branche `prep/t06-chaine-v14-v1`, partie de S `935262b17ca95894a882b02f1526ee39d1738652`, extraction partielle exacte de la consigne (`docs/sources/` et `docs/notes/bras-attaque/` jamais extraits ; « embargo-absent » vérifié). Aucun `fetch`, aucun `push`, rien sur `main` ni dans les autres arbres ; registre de `main` lu par `git show main:registres/go.md` seulement (main `31327cd8`).
- Heures (`date -u`, 10 novembre 2026) : début 06:40:07 ; arbre 06:40 ; jalon code 06:55:45 ; jalon essais 07:03:29 ; liste ciblée v4 de 07:03:38 à 07:27:51 (rejeu des échecs 07:31:07 à 07:31:48) ; S″ 07:09:24 ; contrôles hors ligne 07:10:25 à 07:10:49 ; rapport scellé vers 07:33:58.
- **Option (c) de Lazar (R-2079)** : T0.6 reste scellé sur la chaîne v13 ; cette v14 est une assurance, préparée et éprouvée, **non adoptée**. Rien n'est écrit sous `prereg/`.

**Verdict : chaîne v14 prête à contre-lire, avec trois écarts au mandat nécessaires (§ 2) et une condition de bascule neuve (§ 5) ; essais neufs verts ; liste ciblée v4 jouée sur l'arbre partiel, échecs tous expliqués par l'extraction partielle prescrite (§ 4) ; essai à blanc conforme les 16 et 22, refus le 23, à la condition que le commit de scellement porte la ligne GO-2026-11-10-01 dans son registre (§ 5).**

## 0. Incidents à lire d'abord

1. **Lecture mécanique d'un fichier interdit** (à 06:47 UTC environ, heure relevée par `date -u` à 06:47:37 juste avant et 06:47:51 juste après) : une commande `grep -n "est_epreuve" -r src/ scripts/*.py | grep -v "^scripts/extraire_mesures_epreuve_t06_v1.py"` a passé `scripts/extraire_mesures_epreuve_t06_v1.py` à `grep` par le motif global `scripts/*.py` (recherche du mot `est_epreuve`). La sortie était filtrée sur ce chemin : **aucune ligne de ce fichier n'a été affichée** ; je ne sais pas s'il contient le mot. Erreur de ma part ; aucun motif global sur `scripts/` ensuite.
2. **Un fichier de la liste n'a pas été joué** : `tests/test_t06_v4_extraire.py` charge `scripts/extraire_mesures_epreuve_t06_v1.py` (`importlib`, ligne 11 de l'essai, lue). La consigne interdit ce script ; j'ai joué la liste v4 **moins ce fichier** (85 fichiers sur 86). Il reste dans la liste v4 (l'instance le joue, comme la v3).
3. **Extraction partielle et essais** : `docs/sources/` n'est pas extrait (consigne) ; or les essais qui jouent un run jouet lisent `docs/sources/invites-2606.08892-v1/index.json` (l'amorce clone ce petit dossier sur l'instance). Ces essais échouent dans mon arbre, pour la v6 comme pour la v7 (vérifié sur `tests/test_t06_cibles_invisibles_v2.py`, cas v6) : § 4.

## 1. Fichiers et empreintes (noms neufs, R12 ; aucun fichier existant modifié)

| Fichier | sha256 | Rôle |
|---|---|---|
| `scripts/lancer_t06_v14.sh` | `a20ee971660cd586a3b9aadd3c437010c9770d354d3a18a007b6c3ba80ad1202` | lanceur v14 (copie de la v13) |
| `scripts/amorce_instance_t06_v12.sh` | `e4c3d1efa427cfe68145d163090708b40121241e58aeb00a3f0f282d09f18932` | amorce v12 (copie de la v11) |
| `src/controle_ia/t06/session_v13.py` | `4e25e3e79f5217bb9db3868b4c52834e8754fcd7bebb93ea9f8625ef33df642a` | module de session neuf |
| `src/controle_ia/t06/configuration_v7.py` | `90af6b26712d6c27d4d67693021a1e77be65000f663518ccc4c3014388aefe8c` | configuration v7 (écart 2.1) |
| `src/controle_ia/t06/lanceur_v7.py` | `9137b31095d1415e851d2bd9c6678332b4ed149adc0123bdac3772207b5816b7` | lanceur de run v7 (écart 2.1) |
| `scripts/tests-cibles-t06-v4.txt` | `119c5e8cada6c17cf79b505bf4a8778ceb55b9e3cefcee77ba9735f68dbc2e04` | liste ciblée v4, 86 fichiers (empreinte écrite en dur dans l'amorce v12) |
| `scripts/tests-exclus-t06-v4.txt` | `f6f04c8f341cbeb5d0a8957d1f96e047f01d4a3d232c324e6a9590fd848422e1` | exclusions v4 (v3 + 3) |
| `tests/test_t06_v14_gardes.py` | `12e3b0635bf87fcaa35dcee2037ba97f1556555a9eaf971172f1c605af5a7cfe` | 56 essais (session v13, configuration v7, lanceur v7, configuration 7b v2, ligne réelle de `main`) |
| `tests/test_t06_v14_scripts.py` | `145a6c9d43340fa3e0c771633191a57d8a4a7f68293718c273f55edb916aff2a` | 39 essais (lanceur v14, amorce v12, différentiels) |
| `tests/test_t06_v14_liste.py` | `7c206a737c37e19dbf77d8dc45e3ca5db865d1d516d640bddcf3bd956dd679a3` | 14 essais (liste v4 ; remplace `test_t06_v13_liste.py`) |
| `tests/test_cibles_invisibles_v3.py` | `3bdbcb789f68dbd596c04f78d000471277f38b2eb9cca6d0739d1f0e3ac4026f` | 21 essais (écart 2.2) |
| `tests/test_t06_cibles_invisibles_v3.py` | `9d0b66d6069c2a823ecebfca0653fbe0eb1785a90c7c6ac1f803e034c1065a5b` | 21 essais (écart 2.2) |
| `docs/notes/g0-deux-semaines-v1/t06-chaine-v14/config-t06-7b-v2-brouillon1.json` (+ `.sha256`) | `b58029bf5713d962636b418e2e18100d0a34d671aac82c51bbc814c798e54fb3` | configuration de 7b v2, brouillon 1, **non adoptée** ; empreinte canonique `f5b4c4119dbf86909ce779668eb9f2c9b519be4d2aa0419564386330a152de1c` |
| `docs/notes/g0-deux-semaines-v1/t06-chaine-v14/couples-version-neuve-t06-v1.json` (+ `.sha256`) | `987b918fcdb77207d00ac77fcbf2f9e72792d8c3b8c5c9b00e3b246529b69380` | 45 couples d'une version neuve (§ 6) |
| `docs/notes/g0-deux-semaines-v1/t06-chaine-v14/essai-blanc/T0.6-organismes-v0-v2-FACTICE.md` (+ `.sha256`) | `4114b4005e7712b8646ef7d41ede922d9846d57a4ca0edf8341d2818c1c5e548` | texte FACTICE du commit S″ (§ 5) |
| `docs/notes/g0-deux-semaines-v1/t06-chaine-v14/essai-blanc/artefacts-v1/` (21 fichiers, chacun scellé) | compagnons `.sha256` | sorties de l'essai à blanc |

Configuration de 7b v2 : copie de `prereg/T0.6-organismes-config-7b-v1.json` (même écriture JSON, `indent=1`, clés triées, octets vérifiés), où changent **seulement** `go_id` (GO-2026-11-02-28 → GO-2026-11-10-01), `calendrier.dernier_jour_creation` (2026-11-15 → 2026-11-22) et `calendrier.fin_go_utc` (2026-11-17T00:00:00Z → 2026-11-24T00:00:00Z) ; différence vérifiée clé par clé (essai `test_configuration_7b_v2_ne_differe_de_la_v1_que_par_trois_valeurs_et_est_scellee`) ; l'empreinte canonique de la v1 recalculée (`ca8003f9…`) est celle que cite le texte scellé.

Commits locaux (branche `prep/t06-chaine-v14-v1`) : `e0075b54` (code, listes, cibles v3, configuration v2) ; `7fc83762` (essais v14) ; `56cf6aa3` (couples) ; `e1361803` (**S″**, texte factice scellé) ; `b6af8662` (artefacts de l'essai à blanc) ; le commit qui ajoute le sceau de ce rapport (dernier de la branche) (ce rapport).

## 2. Écarts au mandat (nécessaires ; à trancher par la mère)

### 2.1 Un lanceur de run et une configuration neufs (`lanceur_v7`, `configuration_v7`)

Le mandat nomme le lanceur, l'amorce et « un module de session neuf si un module doit changer ». Mais le **lanceur de run** joué par l'amorce (`lanceur_v6`, via `configuration_v6`) reconnaît la course à son `go_id` : `configuration_v6.est_epreuve` est vrai pour **tout** GO lisible autre que GO-2026-11-02-28 (importé de `configuration.py` l. 14). Avec la configuration de 7b v2 (`go_id` GO-2026-11-10-01) et le préenregistrement, `lanceur_v6.executer` refuse : « configuration d'épreuve à blanc avec un préenregistrement : une épreuve n'est jamais décisive » — après le clonage, l'installation et ≈ 35 minutes d'essais sur la carte. Essai d'artefact : `test_artefact_le_lanceur_v6_refuse_la_course_v14_avec_son_preenregistrement` (et `test_artefact_la_v6_lit_la_configuration_7b_v2_comme_une_epreuve`).

- `configuration_v7` : **toute** configuration (course ou épreuve, réelle ou jouet) est validée contre le registre des GO de la racine, obligatoire (`session_v13.go_de_la_configuration`) ; le reste comme en v6.
- `lanceur_v7` : copie du v6 ; changent l'import, l'appel de validation, la commande du manifeste, la distinction course / épreuve (**reçue de l'amorce par `--epreuve`**, non plus lue dans le `go_id`) et deux messages ; aucun calcul ne change (différentiel vérifié ligne à ligne : 9 lignes retirées, 10 ajoutées, plus l'en-tête).

### 2.2 Cibles invisibles v3

`tests/test_cibles_invisibles_v2.py` (dans la liste v3) fait l'inventaire de tous les constructeurs d'invite de `src/` : `lanceur_v7` y en ajoute deux, non inscrits, et l'essai échoue. Même geste que la v2 envers la v1 : copies **v3** (`test_cibles_invisibles_v3.py` : deux entrées au registre et une aux lecteurs admis ; `test_t06_cibles_invisibles_v3.py` : le lanceur v7 joué à marqueur, registre des GO à dates relatives posé dans le dépôt d'essai), les v2 passées aux exclusions v4 avec motif.

### 2.3 Liste v4 et exclusions v4

v4 = v3 − {`test_t06_v13_liste.py`, `test_cibles_invisibles_v2.py`, `test_t06_cibles_invisibles_v2.py`} + {`test_cibles_invisibles_v3.py`, `test_t06_cibles_invisibles_v3.py`, `test_t06_v14_gardes.py`, `test_t06_v14_scripts.py`, `test_t06_v14_liste.py`} (86 fichiers) ; exclusions v4 = v3 + ces trois fichiers, avec motif. `test_t06_v13_liste.py` exige que tout essai figure dans les listes v3 : il échouerait (même geste que la v3 envers la v12).

## 3. Différentiel v13 → v14, commenté

### 3.1 `scripts/lancer_t06_v14.sh` (56 lignes de différentiel : 20 retirées ou changées, 36 ajoutées)

- l. 2 : en-tête v14. l. 81 : `A=scripts/amorce_instance_t06_v12.sh`. **`GO_ID=GO-2026-11-02-28` supprimé** (v13 l. 83) ; `GO_ID_ENV` reçoit la ligne de la course **ou** de l'épreuve.
- `SESSION13` et `go_course()` : le GO de la course est le `go_id` de la configuration citée une seule fois par le texte de S (`session_v13 go-course-git`, lu par `git show`), jamais écrit en dur.
- **`controles` (course)** : `GO_ID` lisible exigé d'abord ; après extraction de la configuration de S : `go_id` = `GO_ID` (sinon code 2) ; `session_v13 go-config` contre le registre (`T06_REGISTRE_GO`, défaut celui du dépôt) : ligne présente, type calcul, Lazar, non échue au jour donné, non révoquée, plafond de la configuration ≤ plafond de la ligne (sortie écrite en tête de `lancement.txt`, comme la v13) ; `session_v13 calendrier-config` (calendrier contre **cette** ligne) ; **neuf** : la ligne doit figurer, conforme, au même calendrier, dans `registres/go.md` **du commit S** (l'amorce v12 l'y relit ; sinon « commit postérieur au GO exigé », code 2) ; `lancement.txt` porte `go` et `plafond` de la configuration. Plus aucun appel à `session_v2 go` ni `session_v2 calendrier` (GO en dur).
- **`creation` (course)** : v13 exigeait `go_id` = GO-2026-11-02-28 et plafond = 200 ; v14 exige `go_id` = `GO_ID`, relit la ligne au jour de la création (`plafond_ligne_go`, `session_v13 go-config`), `go` et `plafond` égaux à ceux des contrôles ; `PGO` = plafond de la ligne ; la commande passe **`-e COURSE_GO_ID=<go_id>`** à l'amorce. Garde de calcul, offre, dépense : inchangées.
- `controles-epreuve` et `--verifier-go-seulement` : « GO de la course » lu par `go_course()` (refus si illisible, code 2) au lieu de la constante. Renvois `lancer_t06_v13.sh` → `v14`, « amorce v11 » → « v12 », étiquettes `controles t06 v14`, `surveillance v14`.

### 3.2 `scripts/amorce_instance_t06_v12.sh` (40 lignes de différentiel : 14 retirées ou changées, 26 ajoutées)

- **`GO_ID=GO-2026-11-02-28` supprimé** (v11 l. 60). Course : `COURSE_GO_ID` exigé, lisible (refus sinon) ; `COURSE_GO_ID` et `EPREUVE_GO_ID` tous deux posés : refus. Épreuve : le refus sous la ligne de la course passe après le clonage (`session_v13 go-course` sur le texte du commit).
- Course et épreuve, même règle : `session_v12 plafond-ligne` puis `session_v3 go` au plafond de la ligne, dans `registres/go.md` du commit cloné ; après la lecture des citations, `session_v13 go-config` (la configuration porte la ligne reçue, plafond ≤ ligne) ; **fin du GO tirée de la configuration** par `session_v13 calendrier-config` et comparée à `FIN_GO_UTC_S` reçue (inchangé : refus si différente).
- Run : `controle_ia.t06.lanceur_v7`, `--epreuve` ajouté pour une épreuve. Liste figée : `scripts/tests-cibles-t06-v4.txt`, empreinte `119c5e8c…` en dur. Ligne de démarrage « AMORCE T06 v12 ». Non changés : minuterie (son message « plafond de 200 USD cumulé » reste, texte seulement), bras B v4, consignation ; `SESSION_V2` reste défini, inutilisé.

### 3.3 `session_v13.py`

`go_de_la_configuration`, `calendrier_de_la_configuration`, `go_de_la_course` ; sous-commandes `go-config`, `calendrier-config`, `go-course`, `go-course-git` ; le reste délégué à `session_v12` (dont `ligne_go_calcul`, réutilisée telle quelle). Bibliothèque standard ; décimaux exacts pour la comparaison des plafonds.

## 4. Essais

### 4.1 Essais neufs, joués seuls (interpréteur `/home/user/controle-ia-travail/.venv/bin/python`, `PYTHONPATH=src`, `--basetemp` neuf sous l'arbre, effacé ensuite)

| Fichier | Résultat | Durée | Heure (`date -u`) |
|---|---|---|---|
| `tests/test_t06_v14_gardes.py` | **56 passés** | 2,47 s | 06:57:39 |
| `tests/test_t06_v14_scripts.py` | **39 passés** | 30,21 s | 07:02:04 |
| `tests/test_t06_v14_liste.py` | **14 passés** (contrôle de syntaxe Python 3.11 joué : `python3.11` présent) | 16,88 s | 07:03:06 |

Cas sain et artefact pour chaque garde neuve (R5), avec le motif exact attendu : GO de la configuration ≠ `GO_ID` (lanceur : contrôles et création ; amorce : `COURSE_GO_ID` ≠ `go_id`), `GO_ID` / `COURSE_GO_ID` absent, vide ou illisible, `COURSE_GO_ID` et `EPREUVE_GO_ID` tous deux posés, ancienne valeur GO-2026-11-02-28 (refusée en course), ligne absente du registre (de `main` ; du commit S ; du commit cloné), ligne échue, révoquée, de type « décision », plafond de la configuration > plafond de la ligne (200 > 150 ; 200,01 > 200), plafond illisible, calendrier au-delà de l'échéance de la ligne (fin du GO un jour trop tard ; dernier jour de création après la fin du GO ; jour après le dernier jour de création), fin du GO reçue ≠ celle de la configuration, épreuve sous la ligne de la course (lue dans le texte, refusée au lanceur et à l'amorce), GO de la course illisible, ancienne valeur absente du code v14 (constantes Python hors docstrings et lignes de code des scripts ; artefact : la même recherche la trouve dans la v13, la v11, `configuration.py` et `session.py`), lanceur v6 qui refuse la course v14 (pourquoi le v7), différentiels v13 → v14 et v11 → v12 bornés à des marqueurs. La ligne réelle GO-2026-11-10-01 est recopiée telle quelle du registre de `main` dans l'essai et éprouvée à jours explicites (16, 22 et 23 conformes pour la ligne ; 9 et 24 refusés ; calendrier de la configuration 7b v2 : 16 et 22 conformes, 23 « dépassé », 24 « validité »). Les autres essais sont à dates relatives au jour de l'essai (aucune bombe à retardement).

### 4.2 Liste ciblée v4 sur mon arbre

Commande : `PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no -rf --basetemp=/home/user/wt-t06-v14/.tmp-essais/liste-v4 <85 fichiers>` (la liste v4 moins `tests/test_t06_v4_extraire.py`, § 0.2) ; `df -h /home/user` avant : 11 Go libres. **De 07:03:38 à 07:27:51 UTC** (`date -u`) : **1 874 passés, 207 échoués, 36 erreurs en 1 450,52 s (0:24:10)**, 2 117 essais. Résumé : `essais-liste-v4-resume-v1.txt` (scellé).

Rejeu des 243 nœuds en échec ou en erreur, une ligne de cause chacun (07:31:07 à 07:31:48 UTC, 38,44 s, mêmes 207 + 36) :

| Cause | Nombre | Fichiers |
|---|---|---|
| `docs/sources/` absent de l'arbre (extraction partielle de la consigne) : garde « fichier absent sur disque » (`invites-2606.08892-v1/index.json`, `invites-2606.07054-v1/derivees/index-v1.json`) ou `FileNotFoundError` sur `docs/sources/invites-2606.08892-v1` | 119 échecs directs + 19 échecs dont le message attendu est remplacé par celui de cette garde + **36 erreurs** de mise en place (bras B v1, v4, régénération des sondes de P3, gardes de P3 : toutes les sections imprimées portent `docs/sources`) | extraction t05, pilote A, environnement A, P3, trace lite, cibles invisibles v3 (12 : agents et juges, comme la v2), **T0.6 : 27** (`test_t06_cibles_invisibles_v3` 14 = sept lanceurs × deux runs jouets, `test_t06_v11_lanceur_jouet` 5, `test_t06_v11_configuration_v5` 3, `test_t06_v3_lanceur_jouet` 2, `test_t06_v2_lanceur_jouet`, `test_t06_lanceur_jouet`, `test_t06_chaine_v13` 1 chacun ; rejoués seuls : 27 sur 27 portent `docs/sources`) |
| même cause, masquée : le gabarit des essais de notation attend une `GardeArret` du lanceur du pilote A, qui lève celle de `docs/sources` avant d'écrire quoi que ce soit (`lancer_pilote_a` charge `controle_ia.environnements.invites`, dont la racine est `docs/sources/invites-2606.08892-v1`), puis le commit du gabarit, vide, échoue | 63 | `test_noter_pilote_a`, `test_noter_rejeu_juges_v1`, `test_noter_rejeu_juges_v2` |
| `pypandoc` absent du `.venv` processeur (attendu par la consigne) | 3 | `test_corpus_arxiv` |
| dossier temporaire sous l'arbre de travail (prescrit) : `_etat_courant` d'un dossier qui devait n'être pas un dépôt git trouve le dépôt parent | 1 | `test_lire_pilote::test_gardes_du_preenregistrement_et_du_commit` (passe avec un dossier temporaire hors de tout dépôt, vérifié) |
| probablement `docs/sources` (même lanceur, mêmes fichiers dont tous les autres échecs portent cette cause), non démontré | 2 | `test_pilote_a::test_lanceur_echec_du_prechargement_avant_les_episodes[panne1]` (`arret.json` non écrit), `test_revalider_pilote_a::test_term_avale_apres_le_dernier_controle_empeche_le_resume` (message TERM au lieu de « relevé avant le résumé ») |

**Aucun échec ne touche la chaîne v14** : les 109 essais v14 passent dans la liste, ainsi que les inventaires des cibles invisibles v3 et tous les essais des chaînes v12 et v13 qui ne jouent pas de run jouet. Ce que l'arbre partiel ne peut pas montrer : les runs jouets (dont le lanceur v7 joué à marqueur) ; à rejouer sur un arbre qui porte les petits dossiers de `docs/sources/` que l'amorce clone (§ 8). Compte attendu sur l'instance : 2 117 + les essais de `tests/test_t06_v4_extraire.py` ; par différence, 2022 − 54 + 151 = **2119** (comptes de collecte des trois fichiers retirés : 14, 21, 19 ; des cinq ajoutés : 21, 21, 56, 39, 14), ce qui suppose 2 essais dans le fichier non joué.

## 5. Essai à blanc de la bascule (hors ligne, rien poussé)

**S″** = `e13618030cd378a5df97f5adc3aeecebff53e47b` (branche `prep/t06-chaine-v14-v1`) : ajoute le texte FACTICE `docs/notes/g0-deux-semaines-v1/t06-chaine-v14/essai-blanc/T0.6-organismes-v0-v2-FACTICE.md` et son sceau. Ce texte est la copie de `prereg/T0.6-organismes-v0-v1.md` (`ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169`) où ne changent que les **18 couples marqués « factice »** du § 6 (citations de code, d'amorce, de configuration et de calendrier), chacun suivi de « [FACTICE] », plus un bandeau FACTICE en tête. Valeurs factices : commit du code `7fc83762…` (arbre gelé égal à celui de S″ : vérifié), amorce v12 `e4c3d1ef…`, configuration = le brouillon 1 de la v2 (chemin sous `docs/notes/…`, pas sous `prereg/`), empreinte canonique `f5b4c411…`, tests attendus `2119` (estimation, § 4), calendrier 22 et 24 novembre.

**Méthode** (comme la voie B, § 3) : `controles` joué par une copie mécanique du lanceur v14 où trois lignes changent (fetch retiré ; ancêtre d'`origin/main` → ancêtre de `ORIGINE_SIMULEE` = S″ ; contrôle des jetons non joué, aucune variable lue) : **variante A**. **Variante B** : une quatrième ligne, le registre du commit lu dans la copie du registre de `main` au lieu de `git show S″:registres/go.md` (simule un S‴ construit sur `main` postérieur à R-2077). Différentiels dans `artefacts-v1/diff-*.txt`. Commande : `T06_DEPOT=/home/user/wt-t06-v14 T06_PREREG=<texte factice> T06_REGISTRE_GO=<copie du registre de main> GO_ID=GO-2026-11-10-01 ORIGINE_SIMULEE=e1361803… bash controles_hors_ligne_v14_<A|B>.sh controles <dossier neuf> <jour>`. Registre de `main` (`31327cd8`) copié hors dépôt, sha256 `78323f79fb70fa23b66d723416fdcc30b758f74e0737ccbfce956eee175cb3d5`.

| Jour | Variante A (S″ réel) | Variante B (registre du commit = `main`) |
|---|---|---|
| 16 novembre | **refus**, code 2 : « GO GO-2026-11-10-01 absent ou non conforme dans registres/go.md du commit de scellement e1361803… (l'amorce v12 le relit : GO-2026-11-10-01 absent du registre) : commit postérieur au GO exigé » | **CONTRÔLES CONFORMES**, code 0 : « GO GO-2026-11-10-01 (plafond de la configuration 200 USD ≤ plafond de la ligne du registre) ; fin_go_utc_s=1795478400 dernier_jour_creation=2026-11-22 echeance_go=2026-11-23 plafond_ligne=200 » |
| 22 novembre | **refus**, même motif | **CONTRÔLES CONFORMES**, code 0, même ligne |
| 23 novembre | **refus**, code 2 : « calendrier de la configuration (L11) : dernier jour de création (2026-11-22) dépassé le 2026-11-23 : nœud de Lazar, aucune création » | **refus**, même motif |

Contrôles passés avant le refus ou la conformité (dans l'ordre du lanceur) : `GO_ID` lisible ; place disque ; `commit_s` rend S″ ; S″ ancêtre de l'origine simulée ; texte présent ; huit citations, une fois chacune ; fichiers cités et sceaux conformes dans S″ ; `go_id` de la configuration = `GO_ID` ; `go-config` contre le registre de `main` : « GO-2026-11-10-01 conforme (plafond de la ligne 200 USD, 2026-11-10 → 2026-11-23) ; plafond de la configuration 200 ≤ 200 » ; calendrier ; (B) registre du commit ; amorce v12 de S″ citée par son empreinte. `lancement.txt` des deux jours conformes : `artefacts-v1/lancement-B-2026-11-16.txt` et `artefacts-v1/lancement-B-2026-11-22.txt`.

**Artefacts** (variante B, code 2 chacun) : ancienne valeur `GO_ID=GO-2026-11-02-28` → « go_id de la configuration de S (GO-2026-11-10-01) ≠ GO_ID de l'environnement (GO-2026-11-02-28) » ; `GO_ID` vide → « GO_ID absent ou illisible » ; registre sans la ligne (celui de S) → « GO-2026-11-10-01 absent du registre » ; 24 novembre → « hors de sa période de validité (2026-11-10 → 2026-11-23) le 2026-11-24 » ; origine simulée = S (avant S″) → « commit de scellement e1361803… absent de origin/main (simulé : 935262b1…) » ; texte v1 sous la ligne neuve → « go_id de la configuration de S (GO-2026-11-02-28) ≠ GO_ID (GO-2026-11-10-01) » ; texte v1 sous GO-2026-11-02-28 le 14 → « amorce v12 absente de S » (la v14 ne sert pas le texte v1).

**Gardes du lanceur de run v7 sur l'arbre de S″** (en plus de la consigne) : `exiger_code_cite` passe avec `7fc83762` ; `exiger_citations_t06` passe (configuration v2, tâches `76cdeace…`, entropie lue) ; `configuration_v7` contre le registre de `main` : conforme les 16, 22 et 23, refus le 24 ; contre le registre de S″ : « GO-2026-11-10-01 absent du registre » ; artefact : commit cité = S → « arbre gelé … modifié depuis le commit cité 935262b17ca9 » (`artefacts-v1/gardes-lanceur-v7.txt`).

**Constat pour la bascule (condition neuve)** : le commit de scellement d'une version neuve (S‴) doit porter, **dans son propre `registres/go.md`**, la ligne GO-2026-11-10-01 — donc descendre de `main` postérieur à `31327cd8` (R-2077), pas de S directement (le registre de S, 06:26 UTC, ne la porte pas). La v14 le vérifie aux contrôles ; sans cela, l'amorce v12 refuserait sur l'instance. Deuxième condition : **nom neuf du texte** (R12) et `T06_PREREG` égal à ce nom : `commit_s` cherche le commit qui **ajoute** le sceau ; le même nom rendrait S, non S‴.

## 6. Ce qu'une version neuve de T0.6 devrait changer (couples prêts à relire)

`docs/notes/g0-deux-semaines-v1/t06-chaine-v14/couples-version-neuve-t06-v1.json` (`987b918f…`) : **45 couples** (`id`, `section`, `ligne`, `nature`, `motif`, `ancien`, `nouveau`, `factice`), chaque `ancien` présent **une seule fois** sur sa ligne du texte scellé (`prereg/T0.6-organismes-v0-v1.md`, `ef31feff…`, au commit S), appliqués tous ensemble en temporaire : le texte obtenu porte les huit citations lues par `controles` une fois chacune, l'amorce v12 sous la forme lue, et un commit cité lisible. Nom proposé : `prereg/T0.6-organismes-v0-v2.md` ; configuration proposée : `prereg/T0.6-organismes-config-7b-v2.json`, copie octet pour octet du brouillon 1.

- **Opérants (lus par la chaîne)**, 11 : commit du code cité (l. 244), empreintes de la chaîne (l. 202, 245), ligne « Amorce » (l. 247), « Tests attendus » (l. 253), empreinte canonique et chemin de la configuration (l. 258, 260), calendrier L11 et liste d'arrêt (l. 239, 591).
- **GO** : l. 201, 264, 271, 272 (la phrase « Elle ne change rien à ce texte » devient fausse), 611, 705, 714, 716, 890.
- **Calendrier (devis, plan, décisions)** : l. 701 (fin du GO 2026-11-24T00:00:00Z ; dernière création sans nœud 2026-11-22T20:48Z ; relance complète : première création au plus tard le 21 vers 17:00Z), 704, 718, 721, 741, 813.
- **Descriptifs** : l. 1, 3 (titre, statut de la version 2), 202 (la v13 écrit le GO en dur), 244 (`commit_s`, registre du commit), 701 (règle du plafond de la v14), 706, 715, 717, 767, marqueurs l. 878, 879, 886, 888, 889.
- **À remplir au scellement** : `<COMMIT_CODE_V14>` (commit de la chaîne v14 après contre-lecture), `<DATE_BASCULE>`, et « Tests attendus » : **2119 estimés** (2022 − 54 essais des trois fichiers retirés + 151 des cinq ajoutés, comptes de collecte), à relever sur l'arbre de S‴.
- **Non changés** (historique, R12) : statuts antérieurs, contre-lectures (l. 863 à 868), « Ce que les auteurs savaient », puissance, plan daté historique (l. 737), notes de brouillon ; aucune hypothèse, prédiction, métrique, seuil, plan d'analyse, critère de lecture ni décision DT.
- **Non cumulé** : la dépense déjà engagée sous GO-2026-11-02-28 entre dans le plafond de la ligne neuve ; la chaîne le tient par l'argument « dépense antérieure » de `creation` (relevé au registre des dépenses), qu'aucune garde ne lit seule : à écrire dans l'ordre de course.

## 7. Temps estimé d'une bascule complète

Après le mot de Lazar (13 novembre, 12:00 UTC au plus tôt), en chemin critique : contre-lecture neuve de la chaîne v14 (≈ 1,5 à 2 h) ; intégration de la branche dans `main` et liste v4 sur l'arbre complet (≈ 45 min, plus la suite complète de la mère si elle la veut) ; texte v2 par application des couples (≈ 20 min, mécanique), `COMMIT_CODE_V14` et « Tests attendus » relevés, contre-lecture R2 du différentiel v1 → v2 (≈ 1 h) ; S‴ construit sur `main` (registre avec GO-2026-11-10-01), poussé, `controles` en ligne (≈ 15 min) ; ordre de course v14 (`GO_ID=GO-2026-11-10-01`, `T06_PREREG`, branche de sortie neuve, dépense antérieure) et sa relecture (≈ 1 h). **Total ≈ 5 à 6 h** de travail (≈ 4 h si les contre-lectures se font en parallèle), soit une création possible le 13 au soir ou le 14, bien avant le 21 (dernier jour qui garde une relance complète) ; T0.7 doit être scellé aussi (condition du GO).

## 8. Ce qui reste

- Contre-lecture neuve (R2) de la chaîne v14 et des écarts 2.1 à 2.3 ; décision de la mère sur `lanceur_v7` et `configuration_v7`.
- Jouer, sur un arbre qui porte `docs/sources/` (arbre de la mère ou instance), les essais que l'extraction partielle empêche (§ 4), dont `tests/test_t06_cibles_invisibles_v3.py` (cas v7) et `tests/test_t06_v4_extraire.py` (non joué ici par interdit).
- Relever « Tests attendus » de la liste v4 sur l'arbre de S‴ (estimation 2119).
- Incident du § 0.1 à consigner par la mère.
- Hors de mes dossiers et non touchés : des dossiers `/tmp/pilote-jouet-*` laissés par les essais du pilote (créés par `tempfile`, effacés à la sortie normale de leur processus) ; mes dossiers temporaires (`/home/user/wt-t06-v14/.tmp-essais`, dossiers de diagnostic du bloc-notes) sont effacés par leur chemin exact.
- Mise à jour de la branche : `prep/t06-chaine-v14-v1` est locale (aucune poussée).
