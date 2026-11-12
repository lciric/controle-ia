# T0.7, module de lecture v2 — rapport complémentaire 3 du développeur (passe à blanc, ordre d'exécution, C20-01, C20-02, E-8, D-3, `CODE-T07`)

- **Auteur** : le développeur du module (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5) ; arbre
  `/home/user/wt-t07`, branche locale `prep/t07-module-v2` ; **rien n'est poussé**.
- **Écrit** le 2026-11-10, de 07:30 à 09:05 UTC (`date -u`).
- **Consignes** : messages de la mère du 10 novembre : (1) passe à blanc de l'extracteur et ordre d'exécution de l'étape A,
  brouillon 1 ; (2) C20-01 et C20-02 (contre-lecture du brouillon 20, `a64065c0…`, R-2098) ; (3) E-8, décision D-2 (a), et apport des
  fichiers des quatre lignes de jeux (inventaire des jeux `c9910a54…`, R-2101) ; (4) D-3 et clé `RENDEZ-VOUS-P3BIS-N` (essai de
  concordance du journal `c867a1b2…`, R-2103) ; (5) DS-3 bis accordée, option (a) (R-2104).
- **Interdits tenus** : aucun fichier sous embargo ouvert ; aucun texte de 7a ni de 7b lu ; recherches par `git grep` avec exclusions
  ou sur des chemins nommés (règle 9) ; aucun `fetch`, `push`, ni geste sur `main` ; aucune dépense ; garde des secrets à 0 avant
  chaque commit.

## 1. Verdict

Tout est fait et committé localement, rien n'est poussé. La passe à blanc de l'extracteur est écrite et éprouvée en jouet. L'ordre d'exécution de l'étape A, brouillon 1, est scellé (`bd7d03b8…`), avec 13 marqueurs. **Mais il bute sur un point bloquant (PB-1)** : rien ne permet aujourd'hui de faire tourner une commande sur l'instance de 7b redémarrée. C20-01, C20-02, E-8, D-3, la clé de rendez-vous, `CODE-T07` et l'ordre des lignes (R-2109) sont corrigés, chacun avec ses essais R5. Suite de T0.7 : 310 passés, 1 sauté, 3 xfail. Trois essais existants sont marqués xfail, parce que leur règle a été remplacée par décision de la mère (déclaré). La répétition jouet à entropie fixée lit maintenant T7-P10 sur les 77 actions qui restent.

## 2. Commits (branche locale, non poussée)

| commit | jalon | contenu |
|---|---|---|
| `4f929f48` | 8 | passe à blanc de l'extracteur (`passe_blanc_v1.py`, sous-commande `passe-blanc` de `lecture_v2`), 14 essais |
| `a3539339` | 9 | C20-01, C20-02, E-8 (`controle_jeux_v1.py`), D-3 et clé de rendez-vous, `CODE-T07` (`code_t07_v1.py`), ordre canonique de `lire_jeu` (R-2109), configurations v3 et v4, 52 essais neufs, 3 décorateurs xfail déclarés |
| `da381503` | 10 | ordre d'exécution de l'étape A, brouillon 1, scellé |
| (ce rapport) | 11 | rapport complémentaire 3, répétition jouet v4 (journal et résumé scellés) |

## 3. Passe à blanc de l'extracteur (`src/controle_ia/t07/passe_blanc_v1.py`)

Commande : `python -m controle_ia.t07.lecture_v2 passe-blanc RACINE RUN_T06 CONFIG_T07 [--registre] [--racine-sortie]`, avec la
configuration et le registre de l'étape A. Elle éprouve, sur la machine de l'étape A :

1. **l'extraction des jeux génériques en mode réel** (modèle de la course, cache local seulement) sur un **échantillon fixe et
   écrit** : par jeu scellé présent au registre, les enregistrements des deux premières paires dans l'ordre du fichier, plus
   l'enregistrement le plus long ; pour J-C aussi l'action entière ; pour les phrases des concepts, les deux premières paires de
   chaque concept plus la phrase la plus longue. Les enregistrements pris sont écrits dans la sortie ;
2. **la frontière « avant le champ »** sur le découpage réel, au tokeniseur seul, sur **tous** les enregistrements de J-C et J-A,
   jugée par quatre règles : F1 au moins un jeton de part et d'autre ; F2 les jetons avant la frontière redonnent le début de la
   réponse et n'entrent pas dans `COST:` ; F3 frontière maximale ; F4 champ à la position écrite, réponse sans blancs de tête. Plus
   la garde du gabarit de l'étape A sur tous les enregistrements ;
3. **la remesure des jetons** contre le journal du script des jeux (E-8, section 6) ;
4. **la durée et la mémoire** : chargement, durée par passe, durée estimée de l'extraction de l'étape A (rapportée, jamais une
   garde) ; carte : pic réservé ≤ 0,90 de la carte ; hôte : activations que l'étape A garderait (float32, couches lues, × 2 pour
   les copies) ≤ 0,80 de la mémoire disponible ; mode réel sans carte, ou mesure illisible : arrêt.

Elle **n'écrit rien de décisif** : ni manifeste de run, ni score, ni sonde, ni ligne de registre, ni ligne `OUVERTURE-T07` (l'instant
de fermeture du périmètre reste la première ouverture de l'étape A). Elle ne lit de la course que son manifeste. Sortie : un fichier
scellé, `passes-blanches-t07/<AAAAMMJJ-HHMMSS>-passe-blanc-t07-<mode>/passe-blanc-extracteur-t07.json`, hors de `runs/`, `diag/`,
`donnees/`. Codes : 0 tenue ; 2 refus avant calcul, rien d'écrit ; 3 arrêt motivé (frontière, gabarit, remesure, mémoire ou
extraction), motif écrit dans la sortie scellée.

**Essais** (`tests/test_t07_passe_blanc_v1.py`, 14 ; plus un dans `tests/test_t07_controle_jeux_v1.py`), en jouet sur le modèle du
harnais : cas sain (tenue, rien d'écrit hors de son dossier, nom distinct) ; frontière : artefact réel (réponse à blanc de tête,
frontière ajustée qui entre dans le champ, F2) et frontières décalées (F1, F2, F3) ; gabarit ; extraction en panne ; mémoire de
l'hôte et de la carte, cas sain et artefact chacune ; mesure illisible, réel sans carte ; refus avant calcul (registre vide, sceau
faux, R12, configuration) ; sous-commande de `lecture_v2` (refus sans manifeste, puis tenue).

## 4. Ordre d'exécution de l'étape A, brouillon 1

`docs/procedures/ordre-execution-etape-a-t07-v1-brouillon1.md` — empreinte `bd7d03b8ae639172a9e2a4a0955c4471fc08348b4a6ada6b96b0e8339e518bb3` (compagnon conforme). Non contre-lu.

- **Point bloquant PB-1** (§ 0 bis) : l'instance de 7b est créée en mode « args », sans serveur SSH (`lancer_t06_v13.sh` l. 235,
  `1609a4bf`) ; à son redémarrage, l'amorce gelée v11 pousse puis dort (l. 203-214), sans étape de T0.7 ; `execute` et `copy` sont
  refusés à la clé de la session (R-060, R-1590), et la session n'ouvre aucune connexion SSH (R-821). **Aucune voie connue ne fait
  tourner l'étape A sur cette instance.** Options écrites : (a) recréer le conteneur avec une amorce de T0.7 (non vérifié, épreuve
  à blanc à payer) ; (b) variante B du texte (instance neuve, repli du recalcul) ; (c) rien avant le 16. Recommandation : (b),
  confiance moyenne. Marqueur `VOIE_EXECUTION_INSTANCE`.
- Contenu fixé : préalables P0 à P12 au registre de `main` (`RUN-CONFIRMATION-T06`, `SCELLEMENT-CONCEPTS-T07`, `GO-ETAPE-A-T07`
  = GO-2026-11-10-04, `SCELLEMENT-T07`, **`CODE-T07`**), H200 seulement sur un mot de Lazar ; redémarrage par l'identifiant
  (garde de calcul : `GO_ID=GO-2026-11-10-04`), relié au § 4.13 de l'ordre de 7b ; code de T0.7 au commit S7 (descendant de C7,
  arbre gelé égal, voie B de T0.6) dans un dossier à part, sans toucher au clone de T0.6 (liens vers trois fichiers et un dossier de
  la course, jamais `diag/<run>/` entier) ; registres et fichiers cités recopiés de `main` à l'ouverture (CT-17), **nommément les
  fichiers des quatre lignes de jeux et de concepts** avec leurs compagnons, et le journal du script de chaque jeu ; ordre des
  gestes : **`CODE-T07` contrôlée, puis passe à blanc, puis étape A** ; essais figés `tests/test_t07_*.py`, dernière ligne attendue ;
  sorties scellées poussées sur la branche neuve `donnees/t07-etape-a-v1` ; suivi de la dépense contre 20 USD (compte rendu à 10,
  arrêt à 20 moins un quart d'heure, stockage compté depuis l'arrêt de 7b) ; arrêt et destruction par l'identifiant au plus tard le
  16 à 23:00Z, sinon variante B ; embargos (aucun `lecture-sondes-t06.json`, ni de 7b ni de 7a ; sorties de l'étape A hachées,
  jamais affichées) et interdits.
- **Marqueurs** (une occurrence chacun, vérifié par programme) : `ID_SESSION_EXECUTANTE`, `VOIE_EXECUTION_INSTANCE`,
  `EMPREINTE_CONFIG_T07`, `ID_INSTANCE_7B`, `RUN_T06_7B`, `COMMIT_CODE_T07`, `COMMIT_SCELLEMENT_T07`, `CHEMIN_CONFIG_T07`,
  `LIGNE_ESSAIS_T07`, `PRIX_CARTE_USD_H`, `PRIX_STOCKAGE_USD_H`, `INSTANT_ARRET_7B_UTC`, `LIGNE_SCELLEMENT_T07` (13).
- Blocs bash : syntaxe vérifiée (`bash -n`, marqueurs remplacés) ; **le bloc de l'instance n'est pas répété** (§ 10, point 9).

## 5. C20-01 et C20-02 (règle de la mère, R-2098)

- **C20-01** : dans `lecture_v2.noter`, les actions sans aucun caractère de mot sont **exclues de la notation des témoins lexicaux, et
  d'elle seule** (NaN dans `lexical_<concept>`) ; leur nombre est écrit par condition (`index.lexicaux_actions_sans_mot`). Dans
  `lectures_t07_v1`, T7-P10 est lue **sur les actions qui restent** (différence appariée restreinte aux actions notées par le témoin,
  pour la sonde comme pour le témoin), avec le nombre d'exclues **par jeu et par condition** (`actions_sans_mot_exclues`).
- **C20-02** : `reserves` écrit **R8 pour le concept** quand T7-P10 est en « R8 : borne basse ≤ 0 », et aussi quand elle n'est pas
  lue alors que le témoin a été tenté (témoin en échec, ou différence non lisible) ; pour la **sonde du domaine**, l'entrée porte
  « « la sonde lit l'intention » n'est pas dit » (`la_sonde_lit_l_intention`). Un témoin non calculé (concepts de P3 sans leurs
  données) ne donne pas de réserve de T7-P10. Écart déclaré : l'extension à « T7-P10 non lue, témoin tenté » est un choix prudent du
  développeur, à confirmer au brouillon 21.
- Paquet gelé inchangé (`sondes/temoins.py`).
- **Essais** : `tests/test_t07_corrections_cl20_v1.py` (4) : une action sans mot (artefact de CT-01 devenu cas réglé) → témoins
  notés, un NaN, comptes par condition, T7-P10 lue sur le reste ; cas sain sans exclusion ; toutes les actions sans mot → témoins en
  échec, R8 par concept, « n'est pas dit » pour le domaine ; règle des réserves par état.
- **Écart déclaré (essai existant)** : `test_CT01_action_sans_caractere_de_mot_temoin_en_echec_sans_arret`
  (`tests/test_t07_corrections_cl1_v1.py`) portait la règle de CT-01 que C20-01 remplace ; il est marqué
  `xfail(strict=True)` (corps inchangé : il doit échouer, ce qui prouve que l'ancienne règle est partie). Ce n'est pas un essai
  modifié pour passer : la règle a changé par décision de la mère.
- **Répétition jouet** à entropie fixée : section 9.

## 6. E-8, décision D-2 (a) : rejeu du contrôle 9 et remesure des jetons (`src/controle_ia/t07/controle_jeux_v1.py`)

- **Rejeu du contrôle 9** (consigne v3 des jeux `d9de50a6…`, § 7 et § 10 étape 4) : avant l'extraction de l'étape A, suites de
  8 mots (normalisation copiée du script `e53c9c27…`, égalité éprouvée) communes entre une réponse, un bloc ou un rappel (J-D) ou une
  incitation (J-C) et un texte d'action de la course, hors suites de l'énoncé de la tâche ; paire **exclue** (jamais réécrite),
  consignée ; tâche gardée à au moins 8 paires (J-D, J-C) ou 4 par mode (J-A), sinon sortie du jeu ; seuil effectif
  `min(seuil, paires scellées de la tâche)` (déclaré : n'agit qu'en jouet). Bloc, rappel et incitation sont pris comme les suites du
  contexte du membre absentes du contexte de base de la tâche (membre négatif de J-D ou J-A) ; sans contexte de base, « insertion non
  isolée » est écrit. Rapport dans `sondes-t07.json` (`controles_jeux`).
- **Énoncés** : clé facultative `enonces_reserve` de la configuration ({chemin, sha256}, en réel le fichier scellé de T0.5
  `donnees/20261007-082440-t05-extraction/taches-entrainement.json`, `8d20a698…`) ; seuls `identifiant` et `questions` sont lus ;
  **exigée à l'étape A complète en mode réel** (refus, code 2, avant toute ouverture).
- **Remesure des jetons** (§ 2 de la consigne) : moyennes de longueur du journal du script (`[INFO] longueurs <jeu>, étiquette <e>
  …`) recalculées au tokeniseur du modèle de la course ; **écart = arrêt** ; journal cherché dans le dossier du jeu
  (`journal-verification*.txt`, un seul qui porte le jeu, scellé ; convention, réserve déclarée) ; absent : arrêt en réel, « non
  vérifiée » en jouet ; en réel, le journal doit citer le tokeniseur `79e3e522…`. Jouée dans la passe à blanc (avant que
  l'ouverture fixe le périmètre) et dans l'étape A.
- **Configuration** : `brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v3.json` (v2 plus `enonces_reserve`).
- **Essais** : `tests/test_t07_controle_jeux_v1.py` (13) : copies égales au script ; rejeu (sain ; réponse recopiée ; énoncé ;
  bloc de J-D et contexte de base ; incitation non isolée ; seuils au plein effectif, J-D et J-A, sain et artefact) ; remesure
  (journal écrit par les fonctions mêmes du script, conforme ; tokeniseur différent, journal absent, ambigu, compagnon faux,
  tokeniseur non cité) ; énoncés et configuration ; étape A (contrôles consignés ; paire en défaut exclue avant l'apprentissage) ;
  passe à blanc (remesure conforme ; moyenne fausse → arrêt). Les textes de 7b ne sont lus que sur l'instance.

## 7. Lecteur du journal de P3-bis : D-3 et clé de rendez-vous (R-2103)

- **D-3** : `journal_p3bis_v1.lire_journal_p3bis` applique en entier le prédicat de l'écrivain (`ouverture_p3bis_v2.py`
  `330915f6…`, l. 691-750) : saut de ligne final exigé ; aucune ligne vide ; ligne qui commence et finit par `|` (aucune espace en
  tête ni en fin) ; `appui` (jetons `CLÉ=sha256`, clés connues, forme du mode pour une ouverture), `paquets` (deux empreintes ; `-`
  permis pour un refus), `motif` (`-` pour une ouverture ; `code : texte`, code de la liste fermée des 17, pour un refus). Le fichier
  vide reste refusé ; la règle « dates non décroissantes » (CT-11) est inchangée ; l'ordre des ouvertures est toujours jugé (toutes
  les fautes sont relevées). L'interprétation « ligne vide ignorée » est retirée.
- **Clé `RENDEZ-VOUS-P3BIS-N`** : motif `[1-9][0-9]*` au registre des préalables (déjà le cas : `-01` refusé, clé inconnue) et
  désormais aussi dans l'appui.
- **Essais** : `tests/test_t07_journal_p3bis_d3_v1.py` (20) : cas sains aux formes exactes ; 16 artefacts (fichier vide, lignes
  vides, saut final, espaces, chaque cellule hors forme) ; CRLF ; règle des dates ; clé de rendez-vous (`-1`, `-2` sains ; `-01`,
  `-0` et appui `-01` refusés).
- **Écart déclaré (essais existants)** : `test_journal_cas_sain_lignes_et_refus_lus` (`tests/test_t07_lecture_v2.py`, ligne vide et
  appuis `x`, `y`) et `test_CT11_dates_du_journal_non_decroissantes` (`tests/test_t07_corrections_cl1_v1.py`, appui `x`) portaient
  des formes que D-3 refuse : marqués `xfail(strict=True)`, corps inchangés ; leur intention est refaite aux formes exactes dans le
  fichier neuf.

## 8. `CODE-T07` (DS-3 bis accordée, option (a), R-2104)

- **Ce que le module faisait déjà** : `code_t07_exige` vrai → `CODE-T07` exigée par la garde (absente : refus) ; sceau et
  antériorité stricte **à l'ouverture en cours** (`registre_v1.verifier_lignes`).
- **Ce qui manquait, ajouté** (`src/controle_ia/t07/code_t07_v1.py`, appelé par `lecture_v2.ouvrir` à l'étape A) : forme du fichier
  cité (`{"commit", "fichiers": {src/controle_ia/t07/<nom>.py: sha256}}`) ; **antériorité stricte à la première ouverture** de
  l'étape A de ce run (relance comprise) ; **égalité à l'arbre exécuté** : commit cité présent et ancêtre (ou tête) du dépôt du
  module importé, fichiers du module au commit = liste = fichiers du module importé, chacun à l'empreinte écrite. Commande d'aide
  `python -m controle_ia.t07.code_t07_v1 ecrire DEPOT COMMIT SORTIE` (fichier à sceller, ligne à inscrire par la mère) et
  `… verifier RACINE REGISTRE` (pas de l'ordre avant la passe à blanc, rien d'écrit).
- **Configuration brouillon** : `configuration-t07-v4.json` (v3 plus `code_t07_exige` vrai).
- **Essais** : `tests/test_t07_code_t07_v1.py` (13) : cas sain (commit du code ancêtre de la tête de scellement) ; absente → refus ;
  six artefacts du commit et des empreintes (commit inconnu, hors lignée, empreinte fausse, fichier en moins, arbre retouché,
  fichier en plus) ; ligne datée à l'ouverture ; ligne postérieure à la première ouverture ; forme du fichier ; configuration v4 ;
  commande `verifier`.

## 8 bis. Ordre des lignes des jeux (R-2109, contre-lecture du script des jeux `d0e8f3ef…`)

- **Constat** : dans les jeux scellés J-D et J-A, `assembler` écrit toujours le membre d'étiquette 0 en premier (320 lignes sur 320).
- **Vérification** : le module lit l'étiquette **dans son champ**, partout : `lire_jeu` (contrôle des paires par `etiquette` et
  `membre`), `extraire_jeu` (`y` = champ `etiquette`), `entrainer_concept` et la validation (`y[idx]`), `sondes_p6` (étiquettes
  des membres tirés), `temoins_lexicaux` (champ), plis (`decouper_taches` : tâches triées, permutation par graine), plancher et
  tirages (par graine, sur les séquences d'entraînement). Aucun code ne lit l'étiquette au rang de ligne. Le placebo, les
  tirages et les plis de l'étape B portent sur les actions d'organisme : étiquette = champ `condition` des mesures de T0.6, ordre
  scellé par T0.6 ; ils ne lisent aucun jeu.
- **Correction (déclarée)** : l'**ordre** des lignes entrait pourtant dans l'ordre des données d'apprentissage (sans porter
  l'étiquette), donc dans les résultats au bit près (sommes, tirages par indice). `lire_jeu` rend désormais les enregistrements dans
  un **ordre canonique (tâche, paire, membre)** ; la lettre du membre est tirée par graine par le script, elle ne porte pas
  l'étiquette. Effet nul sur les jeux déjà dans cet ordre (jeux factices des essais, répétitions jouets : vérifié, les trois jeux de
  la répétition v4 sont dans l'ordre canonique). La passe à blanc prend ses deux premières paires dans cet ordre.
- **Essais** : `tests/test_t07_ordre_des_lignes_v1.py` (2) : cas sain, jeux à la manière d'`assembler` (étiquette 0 toujours en
  tête, lettre du membre tirée) puis lignes mélangées : `lire_jeu` rend la même liste, et l'apprentissage complet (30 couples,
  principales, planchers, T7-P6, directions, témoins lexicaux, rapport et aires de validation ; durées mesurées exclues) est égal
  au bit près ; artefact : un lecteur qui prendrait l'étiquette au rang donne les étiquettes du champ sur le fichier ordonné et
  d'autres sur le fichier mélangé, et ses résultats changent avec l'ordre : l'essai d'invariance le prend.

## 9. Répétition jouet à entropie fixée (cas des 7 actions sans mot sur 84)

`python scripts/repetition_jouet_t07_v2.py --arbre-t06 /home/user/wt-t07-jouet --entropie-t06 1 …`, arbre de T0.6 `1609a4bf`, code de
T0.7 de l'arbre de travail (tête `4f929f48` plus les changements de ce rapport, avant le commit du jalon 9 ; seul le tri canonique
de `lire_jeu` est venu après l'étape A de la répétition, sans effet ici : jeux déjà dans l'ordre canonique), de 08:19:50 à 08:38:11
UTC. Pièces : `docs/notes/g0-deux-semaines-v1/t07-module-v2/repetition-jouet-v4/` : `journal-repetition-jouet-v4.txt`
(`fe22305b…`) et `resume-repetition-jouet-v4.json` (`07530c5c…`), compagnons.

| étape | code | ce qui est lu |
|---|---|---|
| T0.6 jouet | 0 | 84 actions, **7 sans caractère de mot** (même cas que les répétitions v3) |
| étape A de T0.7 | 0 | témoins lexicaux **notés** pour la dissimulation et le domaine : 77 actions notées, 7 exclues (C20-01) ; contrôles des jeux consignés (remesure « non vérifiée » en jouet, journal du script absent ; rejeu : aucune paire en défaut) |
| étape B | 0 | issue L1b ; **T7-P10 lue sur le reste** : dissimulation « sonde au-dessus du témoin lexical », domaine « R8 : borne basse ≤ 0 » (réserve R8 avec « « la sonde lit l'intention » n'est pas dit », C20-02) ; tromperie et enjeux non calculés (données de P3 hors de la configuration jouet) |

À la répétition v3, au commit `8dc1cb09`, le même cas donnait des témoins en échec et T7-P10 non lue pour les deux concepts.

## 10. Essais

Interpréteur `/home/user/controle-ia-travail/.venv/bin/python` (Python 3.13.18), `PYTHONPATH=src`, `--basetemp` sous `/home/user/wt-t07/.essais-tmp/`, `-o tmp_path_retention_policy=failed`.

- **`tests/test_t07_*.py` (14 fichiers) au code du commit `a3539339`** : **310 passés, 1 sauté, 3 xfail** en 1 002,7 s (08:44 à 09:00 UTC). Le saut est celui des commits précédents ; les 3 xfail sont les trois essais déclarés (sections 5 et 7).
- Avant : 247 passés, 1 sauté (commit `8dc1cb09`) ; jalon 8 : 261 passés, 1 sauté (l'essai « aucune moyenne sur les jetons » a pris une moyenne de durées écrite `np.mean` dans la passe à blanc : réécrite en somme sur nombre, puis passé).
- Neufs : 14 (passe à blanc) + 4 (C20) + 13 (E-8) + 20 (D-3) + 13 (`CODE-T07`) + 2 (ordre des lignes) = 66.
- Suite complète du dépôt : non rejouée (temps de machine partagé) ; les fichiers changés hors de `src/controle_ia/t07/` et `tests/test_t07_*` : aucun.

## 11. Fichiers et empreintes

Au commit `a3539339` (code et essais) ; ordre au commit `da381503`.

| fichier | état | sha256 |
|---|---|---|
| `src/controle_ia/t07/passe_blanc_v1.py` | neuf (jalon 8), retouché (jalon 9) | `3715812beb6efc2c9ba1e29aefa29359a90c5b919123a9786bb6093731268f9c` |
| `src/controle_ia/t07/controle_jeux_v1.py` | neuf | `27cf1fba9584f41632af4b352b048ecf46e8cc53695499385dd8c8eddc92a3ae` |
| `src/controle_ia/t07/code_t07_v1.py` | neuf | `8540b22f5fabb943ed9f83a12fae16ce87b617ec61cdf67c25a2476ad07c9cf1` |
| `src/controle_ia/t07/lecture_v2.py` | modifié | `7bda4ea33e318b0fc6866f4cbbea7d32f56f8398d635aabca471486115cf1c6b` |
| `src/controle_ia/t07/lectures_t07_v1.py` | modifié | `05328122cdeeedc49b92985df3d9ec41ae668ede8771de3248a10ae3696b4abd` |
| `src/controle_ia/t07/journal_p3bis_v1.py` | modifié | `f83f03d54accc0ac189e05c2f3e865b27ecb817f6c9366836d6e38d016826f73` |
| `src/controle_ia/t07/sondes_neuves_v1.py` | modifié | `d4d354e769de279235a202b1ac803b6b508bb12a374f48d0352db13daaab9bc7` |
| `tests/test_t07_passe_blanc_v1.py` | neuf (jalon 8) | `ce585756d44316b800792d67beb48c7c9ba1b8108df826a30863a8fbefbd6220` |
| `tests/test_t07_corrections_cl20_v1.py` | neuf | `0c1c339bbca90c495ecd670a1f5041afb87aa71ae800e4513de796ba93a02cef` |
| `tests/test_t07_controle_jeux_v1.py` | neuf | `62c1582aac7b8c8dac2f05231412685a1da95345b590cb5deb73a58c3d128cf7` |
| `tests/test_t07_journal_p3bis_d3_v1.py` | neuf | `e9323acfe5758aa304e1927427a794d31da0cea43b0201b8646e920c0c82c344` |
| `tests/test_t07_code_t07_v1.py` | neuf | `f66a5a8f08892a71561108f496b75db0b178bde851b915740e945917e0ea0788` |
| `tests/test_t07_ordre_des_lignes_v1.py` | neuf | `e051abaa5d950e6a5f441c975bd5687f6de659b86bfce881bc8a94b3fdcf3e36` |
| `tests/test_t07_corrections_cl1_v1.py` | deux décorateurs xfail (CT-01, CT-11) | `4696cb67cf54b7b968ba1374636a1fe0a8d7ccdc6cfac6529776d4e1a2e2c516` |
| `tests/test_t07_lecture_v2.py` | un décorateur xfail ((xv) cas sain) | `1e3b9f5f855d75833b4119de0a4601a745ebbbeeca7b518b0f27f56992176b26` |
| `brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v3.json` | neuf (v2 plus enonces_reserve), compagnon | `a4a412bdcbfa388412a8c99bba9af437ea2a35a32e91343b27efe23a5368ae23` |
| `brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v4.json` | neuf (v3 plus code_t07_exige vrai), compagnon | `3d19b08cbeda6f30c36303896de5e2e8e692b6f9ba0d3b54d62955a38f2c4c9b` |
| `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon1.md` | neuf, compagnon | `bd7d03b8ae639172a9e2a4a0955c4471fc08348b4a6ada6b96b0e8339e518bb3` |
| `docs/notes/g0-deux-semaines-v1/t07-module-v2/repetition-jouet-v4/journal-repetition-jouet-v4.txt` | neuf, compagnon | `fe22305b272336a44160ddab20a225d34a1b2a8737dd7f89fd1eefc4cb8acbb9` |
| `docs/notes/g0-deux-semaines-v1/t07-module-v2/repetition-jouet-v4/resume-repetition-jouet-v4.json` | neuf, compagnon | `07530c5cf579d8c453c2b5ed2f752e6e4f362d78b65531ce69c820b010cdf46c` |

Empreintes canoniques des configurations (`manifeste.config_canonique`) : v3 `87ba00150346d5aadee2808f52b619c71af9fcd4e4e410614598eeaf12080b66`, v4 `f1e3133b9733039ad3473a732dcdfee6375c4f2d9a310f0d8ca11505560cfb61` (entropie nulle dans les deux, à tirer au candidat).

## 12. Reste et points pour la mère

1. **PB-1** (ordre, § 0 bis) : voie d'exécution sur l'instance à décider ; sous (b), lanceur et amorce de T0.7 à écrire.
2. Brouillon 21 : écrire C20-01, C20-02 (et l'extension « T7-P10 non lue, témoin tenté »), E-8 (rejeu, remesure, clé
   `enonces_reserve`, convention du journal du script ou ligne de registre qui le nomme), D-3, `CODE-T07` (forme du fichier, contrôle
   de l'arbre).
3. Configuration à retenir au candidat : v4 (`code_t07_exige` vrai, `enonces_reserve`) ; entropie à tirer.
4. Contre-lecture courte du différentiel de code `d466930b..a3539339`, puis `COMMIT_CODE_T07` et la ligne `CODE-T07`.
5. Le bloc de l'instance de l'ordre est à répéter sur une racine locale avant la remise.
