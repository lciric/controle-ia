# Inventaire des jeux de T0.7 (J-D, J-C, J-A, phrases des concepts) et plan pour les sceller avant l'étape A — v1

- **Auteur** : agent neuf (Claude Opus 5.5), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`. Il n'a écrit
  ni T0.7, ni son module, ni ses jeux, ni leurs contre-lectures ; il n'a été ni lecteur exploratoire de 7a, ni auditeur
  DT-4. **Il a lu T0.7 (brouillon 20) : il est exclu de tout rôle de lecteur de P3-bis.**
- **Heures** (relevées par `date -u`) : travail commencé le 2026-11-10 à 07:35:07 UTC ; relevés terminés à 07:44:54 UTC ;
  rédaction commencée à 07:47:14 UTC ; heure du scellement : celle du compagnon `.sha256` (donnée dans le rapport à la mère).
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-inventaire-jeux-t07-v1.md`
  (`cfcfcc711f194cde0723ec76c3409f1f1c8d9c726bd9efa3207c5d47a5e2c089`, vérifiée avant lecture) ; **interdits communs v2**
  `…/interdits-communs-v2.md` (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiés), tenus en
  entier, règle 9 comprise.
- **Ce qui a été lu, et d'où** :
  - `main` au commit `2350782b` au départ ; la mère a avancé `main` pendant ce travail (`d1498ceb`, R-2095 à R-2097,
    sans rapport avec les jeux) ; les registres ont été relus à cet état ;
  - branche **`prep/fille-12-t07-v1`**, absente du clone, récupérée par **un seul** `git fetch --no-tags origin
    +refs/heads/prep/fille-12-t07-v1:refs/remotes/origin/prep/fille-12-t07-v1` (lecture seule, permise par la consigne) ;
    tête **`bd02ae3e`** (2026-11-07 11:13:17 UTC) ; clone superficiel : ancêtre commun avec `main` = `d0075a57` ;
  - module : `git -C /home/user/wt-t07 show 8dc1cb09:<chemin>` (commit du 2026-11-10 07:21:06 UTC) ;
  - `git ls-remote origin` avec des motifs (`donnees/tokeniseur*`, `*t07*`, `*jeux*`, `*concept*`, `*fille-12*`) : noms
    de branches seulement ;
  - deux contrôles en lecture seule par l'interpréteur du dépôt (`.venv/bin/python -I`, script passé sur l'entrée
    standard, **aucun fichier écrit**) : énoncés de la projection contre la réserve scellée ; structure des fichiers de
    tâches (noms de clés seulement, aucun champ `cibles` affiché).
- **Jamais ouverts** : tout `lecture-sondes-t06.json` ; la lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; tout
  `diag/` et `runs/` de 7a ; `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
  `docs/notes/bras-attaque/` ; l'étiqueteur ; `scripts/extraire_mesures_epreuve_t06_v1.py` ; **les textes d'actions de P3**
  (`donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl` : seul son nom a été listé par `git ls-files`, pour savoir
  s'il est suivi). Recherches : `grep` sur des fichiers nommés, `git grep` borné à `src/controle_ia/t07` et à des fichiers
  nommés, listes `git diff`/`git ls-files` avec exclusions des chemins interdits ; aucune recherche récursive.
- **Aucun** appel de modèle ni d'interface externe, aucune dépense, aucun `vastai`, aucune écriture git hors la référence
  de suivi créée par le `fetch` permis. Rien d'écrit hors de ce fichier et de son compagnon.

## 1. Verdict

1. **Aucun des quatre jeux n'est scellé ni inscrit** : `registres/scellements-v1.md` n'existe pas sur `main` ; aucune
   ligne `SCELLEMENT-JEUX-T07-JD`, `-JC`, `-JA` ni `SCELLEMENT-CONCEPTS-T07` nulle part ; aucun fichier de jeu assemblé
   n'est versé sur une branche, et aucun compagnon `.sha256` n'existe sur la branche de la fille 12.
2. **J-D et J-A** sont écrits (32 tâches), vérifiés par le script officiel (code 0) et contre-vérifiés à l'aveugle, **mais
   sur des entrées de travail** (réserve « projection », évaluation factice, énoncés non scellés) et dans un assemblage
   resté dans le bloc-notes de la fille 12 : ils sont scellables **dès aujourd'hui, sur processeur, sans écrire une
   phrase**. **J-C est refusé** (indice de surface confirmé, 25,3 %) et à réécrire. **Le jeu des phrases des concepts
   n'existe pas** (consigne non accordée au module, ni script, ni phrase).
3. **Chemin critique** : les phrases des concepts (clé **exigée** : sans elle, l'étape A est refusée et attend), puis J-C
   (clé permise : sans elle, repli écrit à trois sondes). Le plan tient au **14 novembre** sans dépense et sans mot de
   Lazar, **sauf un point possible** : le module ne rejoue pas le contrôle 9 ni la mesure en jetons que la consigne v3
   confie à la chaîne de T0.7 (section 3, écart E-8).

## 2. Table par jeu

| jeu (clé) | état au 2026-11-10 07:44 UTC | fichiers (branche, commit, chemin) | empreinte | manque |
|---|---|---|---|---|
| **J-D** dissimulation (`SCELLEMENT-JEUX-T07-JD`) | 320 paires, 640 séquences, 32 tâches ; script officiel en code 0 ; contre-vérifié (32 paires, aucun « non ») ; **non scellé, non inscrit** | remises : `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/` r01–r07 (égales sur `main` et à `bd02ae3e`) ; `brouillons/t07-jeux-synthetiques-v2-suite-fille12/taches/` r00, r08–r17 et `…/remises-completes/` r18–r31 (**état final à `bd02ae3e` seulement** : `main` n'a ni r30–r31, ni les corrections de r00, r08, r12, r19, r22, r25) ; fichier assemblé `dissimulation-v2.jsonl` **dans le bloc-notes de la fille 12 seulement** (`/tmp/claude-0/…/3e5d652c-…/scratchpad/ass/full32d/`), sur aucune branche | assemblage vérifié : `32f412888270a3c4b4bc347cf57055bd11b517000feceeaeed122476238ec228` (journal ci-dessous) | réassemblage depuis les remises, égalité à cette empreinte ; vérification sur les fichiers scellés ; dossier `donnees/t07-jeux-synthetiques-v2/` et compagnons ; provenance ; ligne |
| **J-A** intention, autres modes (`SCELLEMENT-JEUX-T07-JA`) | 160 + 160 paires, 32 tâches ; code 0 ; aires du sac de mots 0,815 / 0,802 (« contrôles »), 0,736 / 0,741 (« direction ») ; contre-vérifié 16/16 et 15/16 ; **non scellé, non inscrit** | mêmes remises que J-D (formulaire commun) ; `intention-autres-modes-v2.jsonl` dans le même bloc-notes | `5b0409209e66e6c29b69e675c5836cefbef966d9cc0a34412837cae837e2aacf` | comme J-D, plus l'aire écrite dans `registres/decisions.md` à la date de la ligne |
| **J-C** domaine, mode « coût » (`SCELLEMENT-JEUX-T07-JC`) | 320 paires écrites ; code 0 ; aire 0,818 / 0,812 ; contre-vérifié 29/32 **mais indice de surface confirmé** (« titre qui annonce l'ampleur », 81 paires sur 320 = 25,3 %) → **refusé, à réécrire** (R-1675) ; réécriture **non commencée** (aucune ligne de registre ne la mentionne au 10 novembre) | remises refusées : `…-suite-fille12/remises-jc/` r00–r31 (`bd02ae3e`) ; assemblage refusé `domaine-cout-v2.jsonl` (bloc-notes) ; règles de pré-contrôle C-1, C-2 prêtes (`…/mesures/regles-c1-c2-j-c-v1.md`, outil et 8 essais) | refusé : `6ac5694cd2e4da2ea37cf901013bc22664e5fd1035924925ee7f5e30bf282926` | J-C entier réécrit (version neuve, R12), validé, nouvelle contre-vérification à l'aveugle, scellement, ligne |
| **Phrases des concepts** (`SCELLEMENT-CONCEPTS-T07`, **exigée**) | **rien d'écrit** : ni consigne accordée, ni annexes, ni script, ni phrase, ni contre-vérification | consigne `brouillons/T0.7-concepts-sans-lien-consigne-v1-brouillon1.md` (brouillon du 17 octobre, « non scellé, non contre-lu » dans son texte, compagnon présent) ; aucune branche `*concept*` au distant | consigne : `acc7bdfb5dbed50c3f11895d7b0240a91708289c3c29d31c9f05fecbaf006e50` | tout : consigne accordée au format du module (un fichier, première ligne `format_lecture`, au moins quatre concepts), annexes A et B, section 5, contre-lecture R2, script et essais R5, écrivain, contre-vérification, scellement, ligne |

### 2.1 Pièces de la vérification et de la contre-vérification (branche `prep/fille-12-t07-v1`, commit `bd02ae3e`, lues par `git show`)

| pièce | chemin (sous `brouillons/t07-jeux-synthetiques-v2-suite-fille12/` sauf mention) | sha256 |
|---|---|---|
| journal final, trois jeux, 32 tâches, code 0 (2026-11-07 11:02:35 UTC) | `mesures/journal-verification-3-jeux-r00-r31-tokeniseur-conforme-apres-controle-9-v1.txt` | `25fdff15cf63ae4264938b448df2bc8b729de4b24b250fc69a344368c41a915c` |
| journal après corrections de longueur (code 1, contrôle 9 seul) | `mesures/journal-verification-3-jeux-r00-r31-tokeniseur-conforme-apres-corrections-v1.txt` | `3e00f63a4a537fee0be80b9b51e833c651d302a8538c2cf5be0d8619dde9f358` |
| rapport de contre-vérification (non scellé) | `contre-verification/rapport-contre-verification-v2.md` | `3fb36d247cc1c96caa92a62c1075f326d7ca2c424b6ae1b53e550975c440f802` |
| clé des réponses (empreinte poussée avant le lecteur, `b4ba3be2`) | `contre-verification/cle-contre-verification-v1.json` | `a4fb97c3c7026b6bf194140f3c78106b133b7a2c5784ea35a8d879488dfc3921` |
| décompte contre la clé | `contre-verification/decompte-contre-verification-v1.json` | `ff76996d10089825d6b2106af477827c1cd50da36d90a157ccacf4fb0ee3d5ae` |
| consigne du lecteur | `contre-verification/lecteur/consigne-du-lecteur.md` | `be3d8a05066a0c7de63a116a1f2e67bb1c7a39e370953b0d86b8d726a80a1349` |
| indices nommés par le lecteur | `contre-verification/reponses-lecteur/indices-de-surface.json` | `35883aa1cae1a0f988c655af1216615d3adf816c06f47fdf9680ea83ff6ad1c2` |
| règles C-1 et C-2 ; outil ; essais | `mesures/regles-c1-c2-j-c-v1.md` ; `outils/precontrole_c1_c2_v1.py` ; `outils/test_precontrole_c1_c2_v1.py` | `5bd86ecd451d4bad505f5da7e8247d4a490de6d73ff229fc3b8861e0a0df47f2` ; `e996c8bbf7e96720a165e416ebd220f19adbdb6d6f2330eb953fc014426b22a9` ; `52e1c0c2f2caa887abb16ab142ca62fc0bfd550a8b01fc53472d180b50168b3a` |
| règles fixes de J-C et renvois | `mesures/journal-jc-regles-fixes-v1.md` | `b68f6f28dae8e640bc11ac7637fc29fbad0506d0125204dec07e6802146d3e90` |
| consignes des écrivains (section 11 et compléments décidés) | `consigne-ecrivain-fille12-v1.md` ; `consigne-ecrivain-jc-fille12-v1.md` | `d6236ef8fafe1d5228594c6c7a2c792ddf7b7bc53e10d8fa1faa3d666bcbb9df` ; `f97a4d7a7bce27a6aaeaeda1a1ef982257b75ada8a758682c4aa8d7fa4725123` |
| rapports de la fille 12, v3 et v4 | `docs/notes/g0-deux-semaines-v1/rapport-jeux-T0.7-v2-suite-v3.md` ; `…-v4.md` | `2d5221ddf17a6ee84cbdba972d69aa181d1e0c74e3ff1a2983d1c5800d4618fc` ; `f2874000a14a02f419298759dff83a25163f2821d590cefbf6b8bdf001e54c0b` |

Entrées citées par le journal final (`25fdff15…`) : script `scripts/verifier_jeux_synthetiques_t07_v2.py`
`e53c9c2729cf17ac1b0f3c6fbf81169c1d568bbccb85fb1535981b4094341d22` (égal sur `main`, sans compagnon) ; consigne v3
`d9de50a6…` ; graine 20261105 ; tokeniseur `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` (branche
`donnees/tokeniseur-llama-3.1-8b-instruct-v1`, commit `03e3cbd9`, au distant, **absente du clone**) ; **réserve
`reserve-projection.json` `9160675146bc4944a8dd6ca9c74f83dea7b3c6f454b0f28b338b860fbd52502e`** et **évaluation
`evaluation-factice.json` `dadbec85edd658ee2de76d8d90a898de5535a948d127cbe8c2d7353d43ab0ad7`** (bloc-notes de la fille 12,
**pas** les fichiers scellés) ; énoncés `en32.jsonl` `a9e8839f…` (= `brouillons/t07-jeux-synthetiques-v2-brouillon1/enonces-reserve-projection-ecrivain.jsonl`) ;
annexes `brouillons/t07-jeux-synthetiques-v2-brouillon1/annexes/` A `230099ef…`, B `eb6a424d…`, C `5d42ab63…` (sans
compagnon) ; textes interdits `prereg/P3-consignes-v1.md` `a68468fe…` et textes d'actions de P3 `ba05fa13…` (passés au
script sans être ouverts, R-1674) ; épisodes de T0.6 « absents à la vérification ».

### 2.2 Contrôle fait ici (lecture seule) : les entrées de travail égalent les fichiers scellés

Les fichiers scellés sont maintenant sur disque et suivis sur `main` : `donnees/20261007-082440-t05-extraction/taches-entrainement.json`
(`8d20a698…`, compagnon conforme) et `…/taches-evaluation.json` (`76cdeace…`, compagnon conforme). Résultat :
**énoncés de la projection = réserve scellée, 32 sur 32** (champs `questions` et `classification`, égalité exacte), **même
ordre** que le fichier scellé (donc mêmes rangs, mêmes rotations des annexes A et B, mêmes contextes) ; les 32 identifiants
sont ceux de la réserve ; **aucun** n'est une tâche d'évaluation (intersection vide sur 64) ; les 32 remises de J-C portent
ces 32 identifiants dans cet ordre. Conséquence : rejouer le script sur les fichiers scellés ne doit rien changer aux
contrôles 2 et 3 ; c'est ce que le plan vérifie (lot 1), il ne le suppose pas.

## 3. Écarts constatés

Écarts à la consigne v3 (`docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md`, `d9de50a6…`) :

- **E-1** (§ 2, § 8 c. 2) : la vérification « code 0 » a lu une réserve de travail et une évaluation factice ; le contrôle
  « aucune tâche d'évaluation » n'a pas été joué contre la vraie liste. Réparable sur processeur (le contenu égale le
  fichier scellé, 2.2).
- **E-2** (§ 2, § 10 étape 2) : `enonces-reserve-v2.jsonl` jamais extrait du fichier scellé ni scellé ; l'écrivain a reçu la
  projection sans compagnon `.sha256`. Contenu égal (2.2) : à extraire, sceller, déclarer.
- **E-3** (§ 3, § 10 étape 6) : dossier `donnees/t07-jeux-synthetiques-v2/` inexistant ; fichiers assemblés hors de toute
  branche ; annexes non copiées ni scellées dans le dossier ; journal hors du dossier et sans compagnon ;
  `rapport-contre-verification-v2.md` non scellé ; **`rapport-redacteur-jeux-v2.md` (§ 12) absent** (aucun rapport
  d'écrivain au format du § 12 sur la branche ; les rapports v1 à v4 de la fille 12 en tiennent lieu) ; **`provenance-v2.md`
  absent**.
- **E-4** (§ 0, § 11) : les écrivains ont reçu la section 11 et des compléments (règles de pré-contrôle, réécriture du mode
  « contrôles ») décidés par la mère (R-1618, R-1660) : à déclarer dans la provenance.
- **E-5** (§ 10 étape 4) : cinq corrections de longueur hors du renvoi unique (exception déclarée à R-1660, R-1672) et trois
  reformulations du contrôle 9 (lecture de la mère, R-1674) : déclarées, à recopier dans la provenance.
- **E-6** (§ 9) : contre-vérification faite par un lecteur Opus neuf, clé poussée avant lui ; **J-C refusé** à la lettre
  (25,3 % > 25 %) ; J-D et J-A gardés (R-1675). Réserve du lecteur sur JD-20 (légère).
- **E-7** : le rapport du script (`docs/notes/g0-deux-semaines-v1/rapport-verifier-jeux-T0.7-v2-v1.md`, `11408b7c…`, § 7
  point 3) demandait une **contre-lecture neuve du script et de ses essais avant le scellement des jeux** ; aucune n'est
  consignée (R-1618 et suivantes). Le § 8 de la consigne ne l'exige pas ; à faire ou à déclarer.
- **E-8 (le plus lourd)** : la consigne v3 confie à **la chaîne de T0.7** deux gestes avant l'extraction : **rejouer le
  contrôle 9** (suites de 8 mots) contre les textes d'épisodes de la course de T0.6, en **excluant** les paires en défaut
  (liste consignée, tâche gardée selon les seuils du § 10 étape 4 ; § 7), et **remesurer les jetons** comme garde d'identité
  (écart au journal du script = arrêt ; § 2). **Le module au commit `8dc1cb09` ne fait ni l'un ni l'autre** (aucune trace
  dans `src/controle_ia/t07/`), et **le brouillon 20 ne les mentionne pas**. Écart non déclaré, à régler avant
  `COMMIT_CODE_T07` (section 7, décision D-2).

Écarts à la consigne des concepts (`acc7bdfb…`) et au brouillon 20 :

- **E-9** : la consigne dit « un fichier JSON Lines par concept » et laisse ouvert un format « phrase placée dans le gabarit
  d'une action de l'agent » ; le module exige **un seul fichier** et n'offre que `message_utilisateur` ou `phrase_seule`
  (brouillon 20, « Accord au code », point 4 : accord à faire avant l'écriture). Annexes A et B et section 5 « à écrire » ;
  consigne jamais contre-lue (R2).
- **E-10** : `MAX_JETONS_PHRASE` = 128 (`sondes_neuves_v1.py` l. 69) : en format `message_utilisateur`, une phrase plus
  longue est **tronquée sans refus** (`premier_test_ia/empans.py`, `jetons_message_utilisateur`, l. 60) ; la consigne n'a
  pas cette borne : à ajouter au script comme contrôle dur.
- **E-11** : le brouillon 20 dit à la fois « l'aire est écrite dans ce texte au scellement du jeu » (plan, point 1) et
  « écrite dans `registres/decisions.md` à la même date » (table des lignes) ; un jeu scellé après le texte ne peut être
  écrit que dans le registre des décisions : à aligner au candidat.

## 4. Format exigé par le module (commit `8dc1cb09` de `prep/t07-module-v2`)

Fichiers lus (empreintes du contenu au commit) : `src/controle_ia/t07/sondes_neuves_v1.py`
`b1c59783ed231c88c5671bc124b0a3f448e5b948b48677db2f361fe6d05c085d` ; `src/controle_ia/t07/lecture_v2.py`
`9d5c1c05acbc4cc031d2234d5c171f3374b90dfa8172fa3aa7299245ff8bb41a` ; `src/controle_ia/t07/registre_v1.py`
`914b8f374ce8f8bc6550d03c34c5f6c2a97ac93b8ce44da24fd88229185ffca0` (**égal sur `main`**) ; `src/controle_ia/sondes/temoins.py`
`3b051b6f…` ; `src/controle_ia/premier_test_ia/empans.py` `58043c95…` ; `scripts/repetition_jouet_t07_v1.py` `7ccd9bbb…`.
`COMMIT_CODE_T07` n'est pas encore rempli (valeur proposée `8dc1cb09`, avant la contre-lecture du différentiel, R-2093) :
**le format ci-dessous est à relire au commit retenu.**

### 4.1 Fichiers de jeux (`lire_jeu`, l. 103-136 ; appelée dans la garde par `lire_jeux_et_phrases`, `lecture_v2.py` l. 264-279)

- Un fichier JSON Lines par clé, UTF-8 ; lignes vides ignorées ; fichier vide → arrêt.
- Chaque ligne : un objet dont l'**ensemble des clés est exactement** `jeu`, `tache`, `paire`, `membre`, `etiquette`, `mode`,
  `instruction_id`, `incitation_id`, `contexte_systeme`, `observation`, `reponse`, `cout_declare`, `position_cost`
  (l. 60-61 ; ce sont les 13 clés du § 3 de la consigne v3, celles qu'écrit le mode `assembler` du script).
- `jeu` = `dissimulation` (clé `-JD`, `mode` = `aucun`), `domaine-cout` (`-JC`, `cout`), `intention-autres-modes` (`-JA`,
  `controles` ou `direction`) (l. 58-59) : **un fichier ne porte que son jeu**.
- `etiquette` ∈ {0, 1} (entier, pas un booléen) ; `membre` ∈ {A, B} ; `tache`, `contexte_systeme`, `observation`, `reponse` :
  textes non vides ; `paire` entier ≥ 1 ; `position_cost` entier, 0 < `position_cost` < longueur de `reponse`, et
  `reponse[position_cost:]` commence par `COST:`.
- Par (tâche, paire) : exactement deux membres A et B, étiquettes 0 et 1, même `mode`.
- Empans (l. 64) : J-D la réponse ; J-C et J-A `reponse[:position_cost]`.
- **Disjonction** : aucune `tache` d'un jeu parmi les tâches des fiches de `episodes-t06.json` de 7b (l. 139-149), sinon
  arrêt.
- **Toute faute est vue dans la garde de l'étape A**, avant le manifeste : refus, code 2, et, selon le brouillon 20
  (« Accord au code », point 5), **nœud, aucune relance**. D'où le contrôle de forme par le module avant chaque ligne
  (plan, lots 1 à 3).
- Seule compte une ligne **strictement antérieure** à l'instant de fermeture (`lecture_v2.py` l. 271 ; brouillon 20, écrit (a) 3).

### 4.2 Fichier des phrases des concepts (`lire_phrases_concepts`, l. 330-352 ; `Extracteur.phrase`, l. 208-219)

- **Un seul fichier** JSON Lines, UTF-8.
- **Première ligne** : exactement `{"format_lecture": "message_utilisateur"}` ou `{"format_lecture": "phrase_seule"}` (aucune
  autre clé).
- Puis **une ligne par paire**, clés **exactement** `concept`, `indice`, `phrase_concept`, `phrase_neutre` ; les trois
  textes non vides ; `exiger_concept_sans_affect(concept)` (racines refusées : douleur, souffr, peur, crainte, trist,
  chagrin, emotion, affect, valence, plaisir, colere, detresse, angoiss, anxi, pain, fear, sad, grief, suffer, distress,
  anger, pleasure, joy ; `temoins.py` l. 38-54 : « chats », « météo », « sports », « géographie » passent).
- **Au moins quatre concepts en mode réel** (`lecture_v2.py` l. 459 : `4 if config["mode"] == "reel" else 1`) ; au moins
  deux paires par concept.
- `indice` : **ni type ni unicité contrôlés par le module** (il trie les paires par `indice`, l. 359) : le script du jeu doit
  exiger un entier unique de 1 à n par concept.
- `message_utilisateur` : la phrase est rendue comme message utilisateur du gabarit de dialogue, consigne système vide,
  **tronquée à 128 jetons** sans refus (E-10) ; `phrase_seule` : jetons de la phrase seule, sans gabarit.
- La clé `SCELLEMENT-CONCEPTS-T07` est **exigée** à l'étape A (`registre_v1.py` l. 67) : absente → refus, code 2, attente.

### 4.3 Lignes de registre (forme exacte)

- Registre `registres/scellements-v1.md` (`REGISTRE_DEFAUT`, l. 44), **absent aujourd'hui** ; créé par
  `registre_v1.ajouter_ligne(registre, cle, instant, chemin, sha)` (l. 335-347, **présente sur `main`**), qui écrit une ligne
  de titre (`# Registre des scellements (T0.6, T0.7, P3-bis) — lignes ajoutées, jamais réécrites`, ignorée par T0.7 et par
  `controle_lecture_t06_v1.py` au commit `061ac380`, `ba2ba5cf…`, qui ne garde que ses propres clés) et **refuse une clé
  déjà présente**.
- Forme (`ecrire_ligne`, l. 316-320) : `| CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin/relatif | sha256 |`, clé de forme
  `[A-Z0-9]+(-[A-Z0-9]+)+`, date UTC stricte, 64 caractères hexadécimaux minuscules ; chemin relatif à la racine du clone,
  sans `/` initial ni `..` (l. 206) ; **empreinte du fichier entier, égale à la première colonne de son compagnon `.sha256`**
  (`sceau_conforme`, l. 106-121) ; date **strictement antérieure** à l'ouverture (l. 249).
- Les quatre lignes attendues (chemins proposés par ce plan) :

      | SCELLEMENT-JEUX-T07-JD | <date -u> | donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl | <sha256> |
      | SCELLEMENT-JEUX-T07-JA | <date -u> | donnees/t07-jeux-synthetiques-v2/intention-autres-modes-v2.jsonl | <sha256> |
      | SCELLEMENT-JEUX-T07-JC | <date -u> | donnees/t07-jeux-synthetiques-v3/domaine-cout-v3.jsonl | <sha256> |
      | SCELLEMENT-CONCEPTS-T07 | <date -u> | donnees/t07-concepts-v1/phrases-concepts-v1.jsonl | <sha256> |

  Chacune au plus une fois ; jamais une clé de la forme `SCELLEMENT-JEUX-<autre marque>-JD|JC|JA` (refus, règle (3)) ;
  l'aire du sac de mots à 32 tâches écrite dans `registres/decisions.md` **à la même date** (J-A : deux modes, deux empans ;
  J-C : deux empans ; J-D : sans objet, réponse identique dans la paire).
- **Les fichiers cités doivent exister sous `RACINE` à l'ouverture**, avec leurs compagnons. L'ordre d'exécution de
  l'étape A (pas encore écrit, marqueur `EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07`) clone la branche du module et n'apporte
  depuis `main` que `registres/` et `docs/decisions/` (brouillon 20, « Accord au code », point 6) : **il doit aussi apporter
  les fichiers cités par ces quatre lignes** (et la passe à blanc de l'extracteur les lit). À transmettre au rédacteur de
  l'ordre.

## 5. Plan chiffré (tout scellé et inscrit au plus tard le 14 novembre)

Principes tenus par tous les lots : aucune activation extraite d'un jeu avant son scellement ; aucun fichier, sortie,
journal ni verdict de P3-bis donné à quiconque décide d'un jeu (brouillon 20, écrit (a), principe commun) ; un jeu accepté
est scellé et sa ligne écrite **dans la session où l'acceptation est prononcée** ; graines par `SeedSequence` (R9) ;
versions dans les noms, rien n'est écrasé (R12) ; toute heure par `date -u`. Outils : scripts du dépôt seulement ;
tokeniseur réel pris sur la branche `donnees/tokeniseur-llama-3.1-8b-instruct-v1` (commit `03e3cbd9`, `git fetch` à refspec
explicite, `git show` vers un dossier hors de l'arbre, empreinte `79e3e522…` contrôlée) ; bibliothèques présentes dans
`.venv` : `numpy` 2.4.6, `tokenizers` 0.23.2, `scipy` 1.17.1. **Aucune dépense, aucun appel externe** (les sous-agents
sont des sessions du programme, comme pour la fille 12).

### Lot 0 — préalables de la mère (10 novembre, ≈ 30 min)

1. Décisions D-1 à D-5 (section 7) consignées dans `registres/decisions.md`.
2. Fusion de `prep/fille-12-t07-v1` (`bd02ae3e`) dans `main` (routine) : elle ne touche que
   `brouillons/t07-jeux-synthetiques-v2-suite-fille12/` et les rapports v2 à v4 (vérifié : aucun autre chemin, aucun
   compagnon) ; sans elle, toutes les remises se citent par `bd02ae3e`.
3. Consignes des lots 1 à 3 écrites et scellées, chacune avec la liste fermée des fichiers lus.

### Lot 1 — J-D et J-A (un agent neuf « assembleur-vérificateur », processeur seul, ≈ 1 h 30 ; scellés le 10, au plus tard le 11)

1. `donnees/t07-jeux-synthetiques-v2/enonces-reserve-v2.jsonl` : extrait du fichier scellé (`identifiant`, `questions`,
   `classification`, ordre du fichier), comparé au contenu de la projection `a9e8839f…` (égal attendu, 2.2) ; scellé.
2. Copies des annexes A, B, C (`230099ef…`, `eb6a424d…`, `5d42ab63…`) dans le dossier ; égalité aux annexes de la consigne
   v3 rejouée par programme ; scellées.
3. **Réassemblage** (`verifier_jeux_synthetiques_t07_v2.py assembler`, graine 20261105, `--taches` = réserve scellée,
   `--enonces` = point 1) depuis les remises de l'état final (`bd02ae3e`) : J-D et J-A depuis
   `…-brouillon1/taches/` r01–r07, `…-suite-fille12/taches/` r00 et r08–r17, `…/remises-completes/` r18–r31 ; J-C depuis
   `…/remises-jc/` r00–r31 (version refusée, nécessaire parce que le script refuse un lancement partiel pour un jeu
   scellable). **Garde d'égalité** : J-D = `32f41288…`, J-A = `5b040920…`, J-C = `6ac5694c…` ; R5 : cas sain (égalité) et
   artefact (même assemblage à la graine 20261106 → empreintes différentes). **Une inégalité arrête le lot** : la
   contre-vérification du 7 novembre ne vaudrait plus pour J-D et J-A (rapport à la mère).
4. **Vérification scellable** : `verifier` sur `donnees/t07-jeux-synthetiques-v2/`, **sans `--jeux` ni `--nombre-taches`**,
   `--taches` et `--evaluation` = fichiers scellés (`8d20a698…`, `76cdeace…`), `--textes-interdits prereg/P3-consignes-v1.md
   donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl` (**passé sans être ouvert**, `ba05fa13…` attendu au journal),
   `--textes-absents` pour les épisodes de T0.6, graine 20261105, tokeniseur réel. Attendu : code 0 et les aires du journal
   `25fdff15…` ; tout écart est rapporté, jamais corrigé en silence.
5. **Contrôle de forme par le module** (au commit retenu pour `COMMIT_CODE_T07`) : `sondes_neuves_v1.lire_jeu` sur les deux
   fichiers et `controler_disjonction` contre les 64 tâches d'évaluation scellées ; aucune activation.
6. `provenance-v2.md` (chemins, empreintes, graine, script `e53c9c27…` et essais `8c754af3…`, commit, écarts E-1 à E-6,
   modèles des écrivains et du lecteur, version refusée de J-C gardée et jamais citée au registre) ;
   `rapport-redacteur-jeux-v2.md` **compilé** depuis les rapports v1 à v4 de la fille 12 (déclaré comme tel, E-3) ; copie du
   rapport de contre-vérification et de la clé ; tout scellé ; poussé sur `main` (`git add -f`, `donnees/` hors suivi).
7. **La mère** prononce l'acceptation de J-D et J-A (règle gelée : 32 tâches, code 0, contre-vérification sans indice
   confirmé, aire < 0,90) et, **dans la même session**, écrit `SCELLEMENT-JEUX-T07-JD` et `-JA` par `ajouter_ligne` (le
   registre naît ici) et la ligne de `registres/decisions.md` avec les aires ; commit, poussée.

### Lot 2 — J-C réécrit (un orchestrateur neuf ; écrivains neufs ; un lecteur neuf d'une autre lignée ; ≈ 4 h ; cible le 11, marge jusqu'au 13)

1. Consigne d'écriture = section 11 et compléments déjà décidés, **règles de pré-contrôle fixées avant le premier
   écrivain** : règles fixes de `journal-jc-regles-fixes-v1.md` et C-1, C-2 (outil `e996c8bb…`, ses 8 essais rejoués avant
   usage) ; jamais changées après la lecture d'une aire.
2. Écrivains neufs (lignée Sonnet, comme le premier J-C), quelques tâches chacun ; règles de R-1660 : renvoi déclenché par
   un pré-contrôle seulement, au plus un par tâche, jamais « le meilleur de plusieurs » ; aire officielle aux seuls jalons
   de 8, 16, 24 et 32 tâches ; **aire ≥ 0,90 à 32 tâches → arrêt et rapport**, sans réécriture de rattrapage.
3. Assemblage dans un dossier neuf `donnees/t07-jeux-synthetiques-v3/` (`--version v3`), J-D et J-A **copiés à l'octet** des
   fichiers scellés du lot 1 (empreintes égales, écrites au journal) ; `verifier` complet, mêmes entrées scellées → code 0.
4. **Contre-vérification à l'aveugle** de J-C : 32 paires, entropie neuve, clé tenue hors de vue et son empreinte poussée
   avant le lecteur, **lecteur neuf de lignée Opus** ; sa consigne dit **qu'aucun fichier de P3-bis ne lui est donné** et il le
   déclare (écrit (a) 2) ; seuils du § 9 : au moins 23 sur 32 ; un indice nommé retrouvé sur plus d'un quart des 320 paires
   → réécriture.
5. Acceptée : scellement, contrôle de forme par le module, provenance v3 ; **la mère** écrit `SCELLEMENT-JEUX-T07-JC` et
   l'aire dans la même session. Refusée : seconde réécriture sous la consigne v3 (aucun abandon par décision) ; **non
   acceptée avant l'ouverture de l'étape A → repli écrit** (trois sondes : tromperie, enjeux, dissimulation ; T7-P4 et
   T7-P15 non lues ; niveau 98,33 %), sans nœud.

### Lot 3 — phrases des concepts (cinq rôles neufs ; ≈ 7 h réparties ; chemin critique ; cible le 12, au plus tard le 13)

1. **Consigne v1** sous un nom neuf (par exemple `docs/procedures/consigne-concepts-sans-lien-T0.7-v1.md`), tirée du
   brouillon 1 (`acc7bdfb…`) et accordée au module (4.2) : un seul fichier `donnees/t07-concepts-v1/phrases-concepts-v1.jsonl` ;
   première ligne `format_lecture` (D-4) ; quatre concepts (chats, météo, sports, géographie, déjà fixés par le défaut (b)
   de P-013) ; 64 paires par concept ; `indice` entier unique de 1 à 64 ; phrases d'au plus 40 jetons (borne dure du module :
   128) ; longueurs appariées à 15 % près en jetons du tokeniseur réel ; annexes A (mots interdits) et B (lexique de chaque
   concept) écrites ; section 5 (consigne d'écriture, en anglais, deux paires d'exemple par concept exclues du jeu).
   **Contre-lecture R2** par un sous-agent neuf d'une autre lignée que l'auteur ; traitement ; scellement (≈ 2 h).
2. **Script** `scripts/verifier_phrases_concepts_t07_v1.py` et ses essais (développeur neuf, ≈ 2 h) : contrôles de la
   section 2 de la consigne plus la forme du module ; R5 pour chaque garde (phrase interdite, mot d'affect, longueurs
   écartées, mot du concept dans une phrase neutre, doublon, première ligne absente ou fautive, clé en trop, moins de quatre
   concepts, `indice` répété, phrase de plus de 128 jetons) ; il appelle `sondes_neuves_v1.lire_phrases_concepts(…,
   min_concepts=4)` comme dernier contrôle.
3. **Écrivain neuf** : la section 5 et les quatre noms seulement (≈ 1 h) ; renvoi unique par paire en défaut, retrait au
   second.
4. **Contre-vérification à l'aveugle** par un autre sous-agent neuf : 10 % des paires de chaque concept (7 sur 64), tirées par
   `SeedSequence` à entropie neuve consignée ; questions de la consigne (forme appariée, concept présent ou absent, aucun
   contenu adressé, aucun affect) ; aucun fichier de P3-bis donné (≈ 30 min).
5. Scellement du fichier, du journal, du rapport et de la provenance ; contrôle de forme par le module ; **la mère** écrit
   `SCELLEMENT-CONCEPTS-T07`.

### Lot 4 — cohérence avec T0.7 et son ordre d'exécution (mère, avant `COMMIT_CODE_T07` et avant le candidat)

1. D-2 (rejeu du contrôle 9 et remesure des jetons par la chaîne) tranchée ; si « au module » : code, essais R5,
   contre-lecture courte du différentiel, puis `COMMIT_CODE_T07` (≈ 2 h à 3 h de développeur).
2. Ordre d'exécution de l'étape A : apporter les fichiers des quatre lignes, compagnons compris, et les vérifier par
   empreinte avant la passe à blanc (4.3).
3. Candidat de T0.7 : liste des clés présentes du registre partagé refaite à sa date (les lignes `-JD`, `-JA` y seront déjà) ;
   E-11 aligné.

### Calendrier

| date (UTC) | lot 1 (J-D, J-A) | lot 2 (J-C) | lot 3 (concepts) | lot 4 |
|---|---|---|---|---|
| 10 nov. | préalables ; réassemblage, vérification, scellement, **lignes `-JD`, `-JA`** | consigne, outils rejoués, premiers écrivains | consigne v1 écrite, contre-lecture R2 lancée | D-2 tranchée |
| 11 nov. | (réserve) | 32 tâches, jalons, assemblage v3, contre-vérification ; **ligne `-JC`** si acceptée | consigne scellée ; script et essais ; écrivain | code du rejeu si D-2 = module |
| 12 nov. | — | (marge : seconde réécriture si refus) | validation, contre-vérification ; **ligne `SCELLEMENT-CONCEPTS-T07`** | ordre d'exécution |
| 13 nov. | — | marge ; 12:00 UTC : bascule de la chaîne de T0.6 décidée si T0.7 n'est pas scellé (R-2079) | marge | candidat |
| 14 nov. | **borne de cette consigne : les quatre lignes inscrites** | | | |

## 6. Ce qui demande un mot de Lazar ou une dépense, et ce qui se fait sans

- **Aucune dépense** : tout se fait sur processeur ; aucune location ; aucun téléchargement (le tokeniseur réel est au
  distant du dépôt).
- **Aucun mot de Lazar nécessaire** pour les lots 0 à 3 : écriture, vérification, contre-vérification et scellement des jeux
  sont de la routine ; un jeu non scellé à l'ouverture donne le repli écrit, pas un nœud.
- **Nœud possible, un seul** : si la mère choisit de **ne pas** faire rejouer le contrôle 9 et la mesure des jetons par la
  chaîne (D-2, option (c)), T0.7 s'écarte d'une consigne scellée qu'il cite ; à porter à Lazar avant le scellement de T0.7
  si elle le juge écart à un texte scellé. Les options (a) et (b) n'en demandent pas.
- **À la marge** : si la mère range le format de lecture des phrases (D-4) parmi les « concepts de sondes » (proposer avec
  recommandation), le défaut s'applique 48 heures après la transmission ; transmis le 10 avant midi, il échoit le 12 avant
  midi, avant la borne du 14 ; l'écrivain du lot 3 peut écrire pendant ce délai (le format ne change pas les phrases).

## 7. Décisions à prendre par la mère (routine sauf mention)

- **D-1 — Sceller J-D et J-A sans attendre J-C.** Enjeu : avec un scellement commun (plan du 7 novembre, R-1675), un retard
  de J-C retarde J-D, et J-D absent retire T7-P3 ; l'écrit (a) 2 veut un scellement dans la session de l'acceptation.
  (a) découpler (lot 1 puis lot 2) : J-D et J-A sûrs dès le 10 ; deux dossiers versionnés, copies à l'octet. (b) un seul
  scellement des trois : un dossier ; dépend de J-C. **Recommandation : (a)**, confiance ≈ 0,8.
- **D-2 — Rejeu du contrôle 9 et remesure des jetons par la chaîne (E-8).** (a) au module, avant l'extraction, comme le dit la
  consigne v3 (exclusion consignée, seuils du § 10 étape 4 ; arrêt sur écart de jetons) : conforme ; ≈ 2 h à 3 h de code et
  une contre-lecture courte avant `COMMIT_CODE_T07`. (b) un script de l'ordre d'exécution, après la course et avant
  l'étape A, qui arrête l'ordre au moindre défaut (nœud) au lieu d'exclure : simple ; plus sévère que la consigne, déclaré.
  (c) ne pas le faire, réserve déclarée dans T0.7 : rien à coder ; écart à une consigne scellée (nœud possible).
  **Recommandation : (a)**, confiance ≈ 0,6 ((b) si le temps manque avant le 13).
- **D-3 — Contre-vérification du 7 novembre pour J-D et J-A et clause « aucun fichier de P3-bis » de l'écrit (a) 2.** La
  consigne du lecteur (`be3d8a05…`) restreint ses lectures à une liste fermée sans aucun fichier de P3-bis, et le lecteur
  déclare n'avoir lu qu'elle ; la phrase « aucun fichier de P3-bis » n'y figure pas. (a) constater que la clause est tenue en
  substance (liste fermée et déclaration), le consigner : aucun nouveau jet. (b) nouvelle contre-vérification de J-D et J-A
  sous une consigne qui dit la phrase : lettre tenue ; une seconde épreuve d'un jeu déjà accepté, ≈ 30 min. **Recommandation :
  (a)**, confiance ≈ 0,7.
- **D-4 — Format de lecture des phrases des concepts.** (a) `message_utilisateur` : gabarit de dialogue du modèle de l'agent,
  plus près de « lues par le modèle de l'agent dans le format de l'agent » (consigne, réserves) ; format joué par la
  répétition jouet (`repetition_jouet_t07_v1.py` l. 140). (b) `phrase_seule` : sans gabarit ; plus loin des actions lues.
  **Recommandation : (a)**, confiance ≈ 0,7.
- **D-5 — Contre-lecture du script de vérification (E-7) et rapport de l'écrivain (E-3).** (a) contre-lecture courte et neuve
  du script et de ses essais (contrôles 2, 3, 6, 9, 10 et `assembler`) pendant le lot 1, sans bloquer ; rapport du § 12
  compilé et déclaré. (b) déclarer seulement. **Recommandation : (a)**, confiance ≈ 0,6.

## 8. Réserves de cet inventaire

1. Les empreintes des fichiers assemblés (`32f41288…`, `5b040920…`, `6ac5694c…`) ne sont connues que par le journal de la
   fille 12 ; les fichiers eux-mêmes n'ont pas été vus (bloc-notes d'une autre session). Le lot 1 le vérifie par
   réassemblage ; rien ici ne garantit l'égalité.
2. Je n'ai rien relancé (aucun assemblage, aucune vérification) : cette consigne ne permet d'écrire que ce fichier.
3. La lecture du module est faite au commit `8dc1cb09` ; le commit qui remplira `COMMIT_CODE_T07` peut différer : la
   section 4 est à relire à ce commit.
4. Les durées du plan s'appuient sur celles de la fille 12 (J-C écrit en ≈ 1 h 10, du 7 novembre 09:38 à 10:49 UTC, commits
   `180043bc` et `246f7c8e` ; corrections et contre-vérification en ≈ 25 min) ; elles ne comptent pas l'attente des mots de
   la mère.
5. Le calendrier de la course 7b (création au plus tard le 15 sous la chaîne v13, bascule décidée le 13 à 12:00 UTC) est lu
   dans `registres/decisions.md` (R-2078, R-2079, R-2089) ; il peut bouger ; seule compte l'antériorité stricte des lignes sur la
   première ouverture de l'étape A.
