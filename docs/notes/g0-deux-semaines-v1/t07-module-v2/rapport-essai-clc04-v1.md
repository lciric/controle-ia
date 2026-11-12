# T0.7, module v2 — essai CLC-04 (« quatre concepts en mode réel » par `ouvrir`) et mutation m13 — rapport v1

- **Auteur** : sous-agent **neuf**, développeur d'essais (Claude Opus 5.5, `claude-opus-5-5`), lancé par la session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv`. N'a écrit ni T0.7, ni son module, ni ses contre-lectures ; a lu le code de T0.7 : **exclu
  ensuite de tout rôle de lecteur de P3-bis**.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-essai-clc04-t07-v1.md`,
  `d0714ffbf5fea02ec634707f4c3f27e3b0bf9deefd85120132f2454a184a44dd`, recalculée par `sha256sum` et égale (13:37 UTC).
- **Contre-lecture lue** : `docs/notes/g0-deux-semaines-v1/t07-module-v2/contre-lecture-code-t07-option-c-courte-v1.md`,
  `7a32746203bf9b467898dbf82a04f32428bf9bd886f93902f82b57d9b0c719e6`, recalculée et égale (ligne CLC-04, table des exigences
  (ii), ligne m13 du § 2). Code lu : `src/controle_ia/t07/lecture_v2.py` (`lire_jeux_et_phrases` l. 288-313, `ouvrir`
  l. 395-584), `sondes_neuves_v1.lire_phrases_concepts` (l. 334-356) ; essais `test_t07_option_c_concepts_v1.py`,
  `test_t07_sondes_neuves_v1.py` (banc), `test_t07_lecture_v1.py` (faux run), `test_t07_lecture_v2.py` (aides) ;
  `test_t07_corrections_cl1_v1.py` joué, non relu en détail.
- **Heures** : travail du 2026-11-10, de 13:37:51 à 14:38 UTC (scellement de ce fichier ; nettoyage du bac à sable ensuite) ; toutes les heures de ce fichier
  sont relevées par `date -u`.
- **Arbre** : `/home/user/wt-t07-clc04`, branche `prep/t07-essai-clc04-v1`, partie de `39bb7ba83cf7fca9faf0edecf38737a4e9b9b02b`
  (`main`) ; extraction clairsemée (`/src/`, `/tests/`, `/scripts/`, `/registres/go.md`, fichiers de la racine), non changée.
  Interpréteur `/home/user/controle-ia-travail/.venv/bin/python` (pytest 9.1.1), `PYTHONPATH=src`, `-p no:cacheprovider`,
  `--basetemp` et `TMPDIR` dans le bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/clc04/`.

## Verdict

**CLC-04 levé.** Un essai neuf passe par `ouvrir`, configuration en mode réel, étape A complète, ligne des phrases antérieure à la
fermeture : trois concepts → refus dont le minimum de quatre est le **seul** motif ; quatre concepts → phrases « lues » ;
contre-épreuve en mode jouet → aucun refus. La mutation m13 est **tuée** (code 1) ; la copie saine passe (code 0). `src/` est
égal au commit contre-lu `37485ce5` (code 0). Réserve sans lien avec l'essai : la suite T0.7 jouée dans cet arbre réduit a
**9 échecs**, tous `FileNotFoundError` sur `brouillons/…`, non extrait (§ 3).

## 1. Fichier d'essai neuf

| | |
|---|---|
| chemin | `tests/test_t07_ouvrir_reel_concepts_v1.py` (115 lignes ; aucun autre fichier changé) |
| sha256 | `6192a821773a661d9fc983d65bca03b7321e4be607d852e5ead1567b4e67505d` (fichier de l'arbre et `git show HEAD:` égaux) |
| commit | `31b55c92393173d01153e4c8a5a9f0d69365ce81` (parent `39bb7ba8…`), branche `prep/t07-essai-clc04-v1`, poussée vers `lciric/controle-ia-travail` |

Les trois essais appellent **`lecture_v2.ouvrir(racine, registre, config, "A", RUN_T06, INSTANT)`**, sur le faux run de l'étape A
complète (`test_t07_sondes_neuves_v1.construire_complet` : deux noms de sondes neuves nuls, jeux J-D, J-C, J-A posés), avec le
fichier léger factice à 24 couples (`test_t07_lecture_v2._fichier_leger_24`) pour que le contrôle des 24 couples du mode réel
(`charger_couples_figes`) passe. Le jeu des phrases est déposé sous un nom neuf (`prereg/jeux-clc04/concepts-<n>.jsonl` ; celui du
banc est scellé et R12 refuse de l'écraser) et cité par une ligne `SCELLEMENT-CONCEPTS-T07` datée une heure avant l'ouverture,
la ligne du banc retirée (`_sans_ligne`). Préconditions **vérifiées dans l'essai** : `etape_complete(config)` vrai ; aucune
`OUVERTURE-T07` antérieure de l'étape A ; aucun journal de P3-bis ; ligne des concepts strictement antérieure à l'ouverture, qui
fait la fermeture. Fixtures et aides importées : `construire_complet`, `_fichier_leger_24`, `_trois_concepts` (le texte à trois
concepts de l'essai (iv) existant), `INSTANT`, `RUN_T06`, `_depot`, `_sans_ligne`.

| essai | configuration | vérifié |
|---|---|---|
| `test_ouvrir_mode_reel_trois_concepts_refus_minimum_de_quatre` (**artefact**) | `mode` « reel », trois concepts | `RefusRegistre` dont la liste des motifs est **exactement** `["phrases des concepts : 3 concept(s), au moins 4 attendus (plan, point 10)"]` (tout le reste du mode réel passe) ; dernière ligne du journal `REFUS-T07`, qui porte le motif ; aucune `OUVERTURE-T07` |
| `test_ouvrir_mode_reel_quatre_concepts_phrases_lues` (**cas sain**) | `mode` « reel », quatre concepts | ouverture ; `jeux_generiques.phrases_etat.etat` = « lues », les quatre concepts lus ; 24 couples figés chargés ; fermeture = instant d'ouverture ; `OUVERTURE-T07` journalisée, aucune `REFUS-T07`, motif du minimum absent du journal |
| `test_contre_epreuve_meme_artefact_en_mode_jouet_aucun_refus_de_minimum` (**contre-épreuve**) | même artefact, `mode` « jouet » | ouverture, phrases lues avec trois concepts, aucun refus |

Joué seul dans l'arbre (13:40:53 à 13:40:57) : **3 passés, code 0**.

**Limite déclarée (docstring du fichier)** : la configuration est celle du jouet passée en `mode` « reel ». `ouvrir` n'appelle pas
`exiger_configuration` (l'étape A l'appelle avant `ouvrir`), qui refuserait cette configuration en mode réel (fichier léger réel
`701f73bd…` absent de l'arbre, `n_plancher`, préenregistrement). L'essai couvre le lien de la l. 501 d'`ouvrir`, pas une étape A
réelle de bout en bout.

## 2. Mutation m13 (point 3)

Trois copies de `src/` dans le bac à sable (par `tar --exclude=__pycache__`), jamais dans l'arbre ; copie saine égale à `src/`
(`diff -r`, hors `__pycache__`). Mutation appliquée à la l. 501 de `lecture_v2.py` par remplacement exact d'une occurrence unique
de `4 if config["mode"] == "reel" else 1)`.

| copie | fin de la l. 501 | `lecture_v2.py` réellement importé (sha256, relevé par le greffon) | heures (UTC) | résultat | code |
|---|---|---|---|---|---|
| saine | `…, 4 if config["mode"] == "reel" else 1)` | `709b2febac4bcee308b66400764d7ed87115dd991c4ab79f57467d1464d7c69e` (égal à l'arbre) | 13:41:56 à 13:41:59 | 3 passés | **0** |
| **m13** | `…, 1)` | `7e0dfe8ebfcd852306e1df0710140eca1f532fc4c113046a0c6175ef2707edf2` | 13:41:59 à 13:42:04 | 1 échec : l'artefact (`Failed: DID NOT RAISE RefusRegistre`) ; 2 passés | **1 : tuée** |
| m13 inverse (supplément) | `…, 4)` | `03631b632c7100a820e2a6535019d53b64c5f332f0317db0c13a7fb04b2db667` | 13:42:04 à 13:42:08 | 1 échec : la contre-épreuve (`RefusRegistre: phrases des concepts : 3 concept(s), au moins 4 attendus (plan, point 10)`) ; 2 passés | **1 : tuée** |

Commande, depuis l'arbre : `PYTHONDONTWRITEBYTECODE=1 TMPDIR=<bac>/tmp PYTHONPATH=<copie>/src:/home/user/wt-t07-clc04/tests:<bac>/greffon
python -m pytest -q -p no:cacheprovider -p trace_import_clc04 -o pythonpath= --basetemp=<bac>/bt-<copie> tests/test_t07_ouvrir_reel_concepts_v1.py`.

**Écart de méthode, nécessaire et déclaré.** `pyproject.toml` porte `[tool.pytest.ini_options] pythonpath = ["src", "tests"]` :
`pytest` place alors `src/` **de l'arbre** devant `PYTHONPATH`. Témoin (13:42:15 à 13:42:19) : `PYTHONPATH=<copie-m13>/src` sans
`-o pythonpath=` → `lecture_v2.py` **de l'arbre** importé (`709b2feb…`), 3 passés, code 0, soit une survie trompeuse. D'où
`-o pythonpath=` (réglage neutralisé) et `tests/` remis à la main dans `PYTHONPATH`. Le greffon du bac à sable (16 lignes, sha256
`0526248681c491743b39e19c859eec399f5fadfdfcf1e5bc9d3fd8a82871b194`, non poussé, supprimé au nettoyage) écrit, en fin de session
`pytest` (`pytest_sessionfinish`), le chemin de `sys.modules["controle_ia.t07.lecture_v2"].__file__`, l'empreinte de ce fichier et
sa ligne 501.

**Rejeu du constat d'origine, en supplément** (13:42:59 à 14:19:27, machine chargée par d'autres processus d'essai) : les trois
fichiers cités par CLC-04 (`test_t07_option_c_concepts_v1.py`, `test_t07_corrections_cl1_v1.py`, `test_t07_sondes_neuves_v1.py`)
sur la copie m13, même méthode, import tracé (`7e0dfe8e…`) : **42 passés, 6 sautés, 2 `xfail`, code 0** : m13 survit sans le
fichier neuf, comme l'a écrit le contre-lecteur. Écart à son compte (48 passés, 2 `xfail`) : les six essais sautés ici le sont pour
l'arbre réduit (`test_t07_corrections_cl1_v1.py` l. 139 « configuration v2 absente » ; cinq de `test_t07_option_c_concepts_v1.py`,
l. 159, 177, 188, 267, 288, « chaîne de T0.6 absente de ce clone »).

## 3. Essais T0.7 joués dans l'arbre (point 4)

`tests/test_t07*.py` (18 fichiers, le mien compris) et `tests/test_verifier_jeux_synthetiques_t07_v2.py`, un processus, 413 essais
collectés : `PYTHONPATH=src python -m pytest -v -p no:cacheprovider --tb=line -rsxXf --basetemp=<bac>/bt-point4-v2 …`.

| passage | heures (UTC) | résultat |
|---|---|---|
| premier, `-q` | 13:42:29 à ≈ 14:22:29 | **arrêté** par la limite de temps que j'avais donnée à la tâche de fond (40 min), à 293 essais sur 413, sans résumé ; machine chargée ; aucune conclusion tirée, sinon le repérage des échecs par position (les mêmes neuf qu'au second) |
| second, `-v` | 14:24:18 à 14:35:29 | **375 passés, 26 sautés, 3 échecs attendus (`xfail`), 9 échecs**, code 1 (669,03 s) ; les trois essais du fichier neuf passés |

**Échecs (9)**, tous `FileNotFoundError` sur un fichier de `brouillons/`, présent au commit (`git cat-file -e HEAD:<chemin>` : 0)
mais hors de l'extraction clairsemée de cet arbre (`git sparse-checkout list` : `/src/`, `/tests/`, `/scripts/`,
`/registres/go.md`), que la consigne interdit de changer :

- `test_t07_lecture_v1.py::test_empreintes_du_brouillon_14_et_de_ses_pieces` (`brouillons/T0.7-sondes-v0-v1-brouillon14.md`) ;
- `test_t07_lecture_v1.py::test_grille_par_classes_egale_au_script_du_brouillon14`,
  `::test_agregation_egale_au_script_et_exemples_du_texte`,
  `::test_derivation_et_grille_par_etats_par_dose_egales_au_script_cas_par_cas`,
  `::test_garde_ouverture_B_enumeration_0_egale_au_script`, `::test_garde_d_ordre_A_enumeration_0_bis_egale_au_script`
  (`brouillons/T0.7-sondes-v0-v1-brouillon14-pieces/grille_l_t07_brouillon14.py`) ;
- `test_t07_lecture_v1.py::test_enumerations_du_module_egales_a_la_sortie_du_script`
  (`…-brouillon14-pieces/grille-l-t07-brouillon14.txt`) ;
- `test_t07_lecture_v2.py::test_enumeration_0_bis_du_brouillon_17_rejouee_par_les_gardes_du_module`,
  `::test_enumeration_0_garde_B_v2_egale_au_script` (`brouillons/T0.7-sondes-v0-v1-brouillon17-pieces/grille_l_t07_brouillon17.py`).

**Échecs attendus (3)** : `test_t07_corrections_cl1_v1.py::test_CT01_…` (règle remplacée par C20-01, R-2098),
`::test_CT11_dates_du_journal_non_decroissantes` (D-3, R-2103), `test_t07_lecture_v2.py::test_journal_cas_sain_lignes_et_refus_lus`
(D-3, R-2103).

**Sautés (26)**, motifs écrits par les essais : chaîne de T0.6 absente de ce clone (18 : `test_t07_repli_etapes_v1.py` 9, dont
deux cas paramétrés de la l. 183, `test_t07_option_c_concepts_v1.py` 5, `test_t07_repli_recalcul_v1.py` 4) ; configurations absentes (`code_t07_v1` l. 156 « v4 », `corrections_cl1_v1` l. 139 et `donnees_p3_v1` l. 66
« v2 », `lecture_v2` l. 229 « brouillon 19 ») ; fichier léger réel de P3 absent (`lecture_v1` l. 1173, `lecture_v2` l. 726) ;
branche `origin/prep/t06-candidat8-v1` non récupérée (`lecture_v1` l. 504) ; commit `061ac380` absent (`lecture_v2` l. 911).

Écart au compte du contre-lecteur dans un arbre complet (404 passés, 2 sautés, 4 `xfail`, 0 échec, 410 essais) : 410 + 3 essais
neufs = 413 ; ici 24 sautés de plus (23 passés là-bas, plus l'`xfail` « ancien artefact du repli », sauté avec la chaîne de T0.6) et
les 9 échecs ci-dessus, tous dus à l'extraction réduite. **Aucun échec ne touche le fichier neuf ni `ouvrir`.**

## 4. Commit, poussée, contrôles (point 5)

- Garde des secrets sur l'index avant le commit (`git diff --cached | grep -cE '(sk-ant|sk-[A-Za-z0-9]{20,}|ghp_|hf_[A-Za-z0-9]{20,}|AKIA)'`) :
  **0** ; index : le seul fichier d'essai.
- Commit `31b55c92393173d01153e4c8a5a9f0d69365ce81` (14:36:05), un fichier, 115 lignes ajoutées, dernière ligne du message
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- `git push -u origin prep/t07-essai-clc04-v1` (14:36:08) : réussi au premier essai (branche neuve sur `lciric/controle-ia-travail`) ;
  `origin/prep/t07-essai-clc04-v1` = `HEAD` = `31b55c92…`.
- `git diff --quiet 37485ce50601b7d7ff9035bc34c734ec689ca731 HEAD -- src` : **code 0** (`src/` égal au commit contre-lu).
- `git diff --stat 37485ce50601b7d7ff9035bc34c734ec689ca731 HEAD -- tests` : `tests/test_lanceur_durable_v5_a1v4.py` (11, +7 −4)
  et `tests/test_t07_ouvrir_reel_concepts_v1.py` (115, +115) ; 2 fichiers : **la liste attendue**.
- `git status --short` vide après la poussée.

## Écarts déclarés

- `-o pythonpath=` et greffon de trace pour le point 3 (§ 2) : sans eux, la copie mutée n'est pas importée.
- Mutation de plus (m13 inverse : minimum de quatre en tout mode) et rejeu des trois fichiers d'origine sur m13, en supplément,
  sur des copies du bac à sable.
- Point 4 joué deux fois : le premier passage, arrêté par ma limite de temps, n'a pas de résumé ; seul le second fait foi.
- Premier essai de mon fichier en échec (13:40:29) : il reposait le jeu des concepts au chemin déjà scellé par
  `construire_complet` (`GardeArret` de R12) ; corrigé avant tout commit (dépôt sous un nom neuf).
- Un `rm -rf` sur variable a été refusé par un contrôle de sécurité (13:41) ; non contourné : les dossiers visés n'existaient pas
  encore, les copies ont été faites sans suppression ; les suppressions suivantes sont faites par chemins littéraux.
- Aucun fichier interdit ouvert ; aucune recherche récursive (recherches par `git grep` restreint à des fichiers d'essai nommés et à
  `src/controle_ia/t07/`, `grep` sur des fichiers nommés) ; aucun appel de modèle ni d'interface externe ; aucune instance ; aucune
  valeur d'une sonde de 7a sous mes yeux. Git : seuls `git add` et `git commit` du fichier d'essai, puis la poussée de la branche ;
  dépôt distant vérifié par propriétaire et nom seulement (`lciric/controle-ia-travail`), adresse complète jamais affichée.
  Écrits : le fichier d'essai (arbre), le bac à sable, ce rapport et son compagnon `.sha256`.

## Points ouverts

1. **Suite T0.7 dans un arbre complet** : les 9 échecs viennent de l'extraction réduite ; la suite de la mère, dans un arbre où
   `brouillons/` est extrait, doit les rendre passés (attendu : 407 passés, 2 sautés, 4 `xfail`, 0 échec si l'arbre est celui du
   contre-lecteur). Non vérifié par moi.
2. **Ordre d'exécution (CLC-04, « à ajouter avant de fixer C7, ou à déclarer »)** : `tests/` diffère maintenant de `37485ce5` par
   ce fichier (en plus de `test_lanceur_durable_v5_a1v4.py`) ; `src/` est inchangé. La branche n'est pas fusionnée dans `main`
   (aucune fusion faite) ; ce qu'il faut citer pour C7 et `CODE-T07` est à la mère.
3. **Bancs de mutation par copie** : avec le `pythonpath` de `pyproject.toml`, `PYTHONPATH=<copie>` seul ne fait pas importer la
   copie (survie trompeuse, montrée). Toute consigne future de mutation par copie devrait exiger `-o pythonpath=` (ou un
   `pyproject.toml` de copie) et une trace de l'import. D'après la contre-lecture, son banc et m13 mutaient l'arbre en place, donc
   hors de ce piège ; le script du banc n'a pas été relu par moi.
4. **Portée de l'essai** : configuration du jouet en `mode` « reel », sans `exiger_configuration` ; une étape A réelle de bout en
   bout demanderait le fichier léger réel et la configuration réelle, absents de cet arbre.
5. Bac à sable nettoyé après le scellement de ce rapport (journaux bruts des passages supprimés ; leurs résultats sont recopiés
   ici).
