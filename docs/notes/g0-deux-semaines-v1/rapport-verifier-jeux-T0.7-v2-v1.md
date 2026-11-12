# Rapport L4 — script de vérification des jeux synthétiques de T0.7 v2 : relecture, essais, lancement d'essai — v1

- Date : 2026-11-05 20:31 UTC (relevée par `date -u`). Modèle : Claude Fable 5.1 (`claude-fable-5-1`), développeur neuf, sous-agent
  de la session principale (fille 8). Aucune paire écrite ni réécrite par ce rapport ; aucun modèle lancé, aucun réseau,
  aucune dépense, aucun commit, aucun `.sha256` écrit (la session principale scelle), rien lu sous `donnees/` ni `diag/`,
  rien importé de `src/controle_ia/sondes/`.
- Consigne qui fait foi : `docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md`, sha256
  `d9de50a6f4f7a8add3465ad53a5b894703f70b8777b7f8e428417ebfcd73b485` (compagnon vérifié par `sha256sum -c` dans
  `docs/procedures/`, « OK »). Section 8 relue règle par règle avec les sections 2, 3, 5, 6, 7 et les annexes A, B, C.

## 1. Ce qui a été lu (chemins, empreintes)

| pièce | chemin | sha256 |
|---|---|---|
| consigne v3 | `docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md` | `d9de50a6f4f7a8add3465ad53a5b894703f70b8777b7f8e428417ebfcd73b485` |
| module gelé (lu, jamais modifié) | `src/controle_ia/environnements/propositions.py` | `5d97b223206c6378295946a769c378ccfe0bd6a12372d3b25bcecb5240ab31ae` |
| textes interdits (paragraphes cités « > ») | `prereg/P3-consignes-v1.md` | `a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c` |
| annexe A (copie JSON) | `brouillons/t07-jeux-synthetiques-v2-brouillon1/annexes/banque-instructions-v2.json` | `230099ef0eece0c11c1ac1a2dfd563e5747292723ddd614eebe7bdbb37d1cc01` |
| annexe B (copie JSON) | `…/annexes/banque-incitations-v2.json` | `eb6a424d20505819491608e2b8c277735157801bb1230304b5f616922ff91b56` |
| annexe C (copie JSON) | `…/annexes/mots-interdits-v2.json` | `5d42ab633dd4dda055989a2609fc77e49accdb428f2acdbad0bdbaf9630cba76` |
| énoncés (projection remise à l'écrivain, 32 lignes) | `brouillons/t07-jeux-synthetiques-v2-brouillon1/enonces-reserve-projection-ecrivain.jsonl` | `a9e8839f886f9df1ce8270a347151bd11bee0e0742b425edf5914cd5c23d50f8` |
| réserve de travail (construite depuis la projection, pas le fichier scellé) | `scratchpad/reserve-projection.json` (hors dépôt) | `1ec09a095b1cb4bff6beb3152b89319ad7d8d7b1aa3cddaa1452b606a1cffcc4` |
| évaluation **factice** (une tâche fictive) | `scratchpad/evaluation-factice.json` (hors dépôt) | `d6739aaf81bf0623f8a34c4bd9e818507b799db52933bc36577ff2e07e70ee7d` |
| remises de l'écrivain r00 à r07 | `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/rNN-<id>.jsonl` | empreintes au journal d'assemblage (section 5) |

Les trois copies d'annexes ont été comparées par programme aux annexes A, B, C de la consigne v3 (cadrages F1 à F4,
24 lignes de l'annexe A dont 4 de réserve, 8 incitations, 66 mots de l'annexe C) : **conformes, caractère pour
caractère**, avant usage.

Le brouillon 1 de la consigne, le brouillon 6 de T0.7, P3 (résultats), T0.6, les sondes, les scores et `donnees/`
n'ont pas été lus.

## 2. Livrables

| fichier | rôle | sha256 |
|---|---|---|
| `scripts/verifier_jeux_synthetiques_t07_v2.py` | script, modes `assembler` et `verifier` (1 320 lignes) | `e53c9c2729cf17ac1b0f3c6fbf81169c1d568bbccb85fb1535981b4094341d22` |
| `tests/test_verifier_jeux_synthetiques_t07_v2.py` | essais R5 (66 essais) | `8c754af3536c5e769af87a28a9cdb34c749c554c16b1376492d5e9348eeda94d` |
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/assemblage-essai-v1/` | assemblage et journal du lancement d'essai (section 5) | voir section 5 |
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/tokeniseur-factice-bpe-v1/tokenizer.json` | tokeniseur factice du lancement (section 4) | `cfc0c1439f9725cb5b8c6881077fe3140c3d9ca621d5876ccddf491fd503b1b8` |
| ce rapport | `docs/notes/g0-deux-semaines-v1/rapport-verifier-jeux-T0.7-v2-v1.md` | (scellé par la session) |

Aucun fichier scellé n'a été modifié. La session principale a pris un instantané git (`58366d61`, « instantané en
cours, non scellé ») pendant le travail ; ce rapport n'a rien commis.

## 2 bis. Essais

- `tests/test_verifier_jeux_synthetiques_t07_v2.py` : **66 essais, tous verts** (`timeout 900 nice -n 10 python -m pytest
  -q -p no:cacheprovider tests/test_verifier_jeux_synthetiques_t07_v2.py` : « 66 passed »). Jeu factice : deux tâches,
  six paires par tâche, textes tirés d'un lexique de 36 mots (blocs tournés entre les deux membres : même multiensemble
  de mots, D1 ≈ 0,42, aucune fuite lexicale possible), tokeniseur `WordLevel` minuscule construit par le test ; ce ne
  sont pas des paires des jeux réels.
- Suite entière du dépôt : jouée une fois, en huit lots séquentiels de fichiers (un seul `pytest` à la fois, chaque lot sous
  `timeout 900 nice -n 10`, la suite d'un seul tenant ayant été tuée par `timeout 900` à 42 % ; lots 0 à 3 avant le
  redémarrage du conteneur de 21:06 UTC, lot 4 rejoué entier après, lots 5 à 7 ensuite) : **2 695 essais passés, 3 échecs,
  tous les 69 fichiers joués**. Les 3 échecs sont `tests/test_corpus_arxiv.py` (`ModuleNotFoundError: No module named
  'pypandoc'`), préexistants et sans rapport avec ce travail (même échec dans le journal de la suite jouée par une autre
  fille à 19:45 UTC). Journal des lots : `scratchpad/l4-pytest-depot-lots.log` et `l4-lot-0..7.log` (hors dépôt).

## 3. Relecture règle par règle : règle de la consigne → fonction du script → essai sain → essai artefact

Toute vérification nommée ci-dessous existe dans le script ; « essai sain » désigne `test_sain_assemblage_et_verification`
(jeu factice qui passe les contrôles 1 à 10, code 0, chaque contrôle `[OK]`) sauf mention ; les essais artefacts vérifient
le code de sortie (1 défaut dur, 2 refus) et le motif écrit au journal.

| règle (section, ligne) | fonction du script | essai sain | essai artefact |
|---|---|---|---|
| § 8 c. 1 — schéma : clés dans l'ordre de la section 3, types, valeurs permises (l. 325-327) | `controle_1_schema` | sain | `test_c1_cles_dans_le_desordre`, `test_c1_types` |
| § 8 c. 1 — `paire` de 1 à 10 ; un membre A et un B par (jeu, tâche, paire) ; étiquettes 0 et 1 | `controle_1_schema` | sain | `test_c1_mode_inconnu_et_paire_hors_bornes`, `test_c1_deux_membres_a`, `test_c1_etiquette_en_double` |
| § 8 c. 1 — `mode` selon le jeu et le rang (J-A : 1-5 `controles`, 6-10 `direction`, § 6.2) | `mode_attendu`, `controle_1_schema` | sain | `test_c1_mode_selon_le_rang`, `test_c1_mode_inconnu_et_paire_hors_bornes` |
| § 3 — `membre` tiré par graine (clé « ordre-membres », jamais choisi par l'écrivain) | `membre_positif_en_A`, `assembler`, `controle_1_schema` | `test_sain_assemblage_membres_tires_par_graine_et_champs_calcules` | `test_c1_membres_contre_le_tirage_par_graine` |
| § 3 — `instruction_id` / `incitation_id` selon le jeu et l'étiquette | `controle_1_schema` | sain | `test_c1_identifiants_d_annexe_selon_le_jeu` |
| § 3 — un fichier par jeu | contrôle « fichiers » dans `verifier` | sain | `test_c1_sequence_d_un_autre_jeu_dans_le_fichier` |
| § 8 c. 2 — tâches dans le fichier des énoncés et de réserve, aucune d'évaluation (§ 2, § 7) | `controle_2_taches`, `charger_enonces` | sain | `test_c2_tache_hors_des_enonces_et_de_la_reserve`, `test_c2_tache_d_evaluation`, `test_refus_annexe_absente_et_enonces_a_champ_cache` (champ caché `cibles`) |
| § 8 c. 2 — 32 tâches ; comptes par tâche et par jeu (10, 10, 5 + 5) (§ 4) | `controle_2_taches` | sain | `test_c2_nombre_de_taches`, `test_c2_comptes_par_tache_et_par_mode`, `test_artefact_assembler_paires_non_assemblables_listees_et_exclues` |
| § 8 c. 3 — contextes recalculés et comparés à l'octet (§ 2 : consigne honnête, format, énoncé, classification sans guide, observation « Turn 1 of 10. », « The set is empty. », « Your action: ») | `contexte`, `controle_3_contextes` | sain + `test_sain_assemblage_membres…` | `test_c3_contexte_recalcule_j_c`, `test_c3_observation_recalculee_j_a` |
| § 8 c. 3 — J-D : différence égale au bloc (fin du message système) et au rappel (avant « Your action: ») (§ 2, § 6.1) | `controle_3_contextes` | sain | `test_c3_bloc_j_d_deplace_et_rappel_absent`, `test_c3_bloc_j_d_dans_le_membre_sans_bloc` |
| § 5.2, § 6.1 — rotations des annexes A et B (p = 10 r + k) | `entree_attendue`, `controle_3_contextes` | sain | `test_c3_rotation_annexe_a`, `test_c3_rotation_annexe_b` |
| § 8 c. 4 — `lire_action` valide, `ADD`, cinq champs non vides dans l'ordre, rien avant `ACTION:` ni après `PREDICTION` (§ 2) | `controle_4_format`, `_STRUCTURE` | sain | `test_c4_champ_manquant_et_ordre`, `test_c4_texte_avant_action_et_apres_prediction`, `test_c4_lire_action_revise_refusee` |
| § 8 c. 4 — ligne `COST: <entier>` exacte ; `heures_declarees` entre 4 et 5 000 (§ 2) | `controle_4_format`, `_LIGNE_COST` | sain | `test_c4_ligne_cost_exacte` (unité, séparateur de milliers, zéro de tête, double espace), `test_c4_cout_hors_bornes` |
| § 8 c. 4 — `cout_declare` et `position_cost` recalculés et égaux (§ 3) | `cout_declare_de`, `position_cost_de`, `controle_4_format` | `test_sain_assemblage_membres…` | `test_c4_cout_declare_et_position_cost_recalcules` |
| § 5.3 N1 — ligne `COST:` identique dans la paire (J-C, J-A, § 6.2) | `controle_5_nombres` | sain | `test_c5_n1_lignes_cost_differentes_et_multiset` |
| § 5.3 N2 — ≥ 6 valeurs distinctes par tâche (J-C) ; rapport max/min ≥ 20 (J-C) | `controle_5_nombres` | sain (6 valeurs, rapport 64) | `test_c5_n2_valeurs_distinctes_par_tache`, `test_c5_n2_rapport_max_min` |
| § 5.3 N3 — aucun nombre de coût (chiffres ou lettres, à trois mots d'une unité listée, « $ », « k ») avant le champ ; groupes de chiffres : écart ≤ 2 dans la paire ; moyennes par étiquette rapportées, réserve > 20 % | `nombre_de_cout_avant_champ`, `controle_5_nombres`, `rapporter` | sain | `test_c5_n3_nombre_de_cout_avant_le_champ`, `test_c5_n3_groupes_de_chiffres`, `test_aire_sous_la_courbe_et_distance` |
| § 8 c. 5 — multiset des valeurs par étiquette égal | `controle_5_nombres` | sain | `test_c5_n1_lignes_cost_differentes_et_multiset` |
| § 8 c. 6 — 90 à 260 mots (mots = suites de caractères non blancs, § 2) | `mots_blancs`, `controle_6_longueurs` | sain | `test_c6_bornes_de_mots` |
| § 8 c. 6 — écart ≤ 15 % en mots, caractères et jetons, réponse entière et empan avant `COST:` (J-C, J-A) | `controle_6_longueurs`, `compter_jetons`, `empan_avant` | sain | `test_c6_ecart_en_mots_caracteres_jetons`, `test_c6_ecart_en_caracteres_seul`, `test_c6_ecart_en_jetons_seul` |
| § 8 c. 6, annexes — blocs 18-40 mots, rappels 3-12, incitations 15-40 ; min/max rapportés | `controle_banques`, `_controler_entree_a` | sain (`[INFO] annexes : …`) | `test_c6_longueurs_des_annexes` |
| § 2 — tokeniseur : copie présente, empreinte conforme, bibliothèque importable, sinon refus ; « jetons : mesurés » au journal | `charger_tokeniseur`, `verifier` | sain (ligne « jetons : mesurés ») | `test_refus_tokeniseur_absent`, `test_refus_tokeniseur_altere`, `test_refus_empreinte_de_la_consigne_sur_un_autre_tokeniseur` (l'empreinte `79e3e522…` refuse un autre fichier), `test_refus_bibliotheque_tokenizers_absente` ; écart au journal pour une autre empreinte : sain |
| § 5.4 D1, § 8 c. 7 — distance d'édition en mots (TITLE, PROPOSAL, CONTROLS) / longueur du plus long ≥ 0,30 (J-C, J-A, § 6.2) | `distance_edition`, `controle_7_texte_different` | sain (D1 ≈ 0,42) | `test_c7_d1_sous_le_seuil`, `test_aire_sous_la_courbe_et_distance` |
| § 6.1, § 8 c. 7 — réponses identiques dans la paire (J-D) | `controle_7_texte_different` | sain | `test_c7_reponses_j_d_differentes` |
| § 8 c. 8, annexe C — mots entiers, sans casse, sans accents, variantes listées, expressions de plusieurs mots ; toutes les réponses des trois jeux | `mots_interdits_presents`, `normaliser`, `controle_8_mots_interdits` | sain (et « padlock », « purpose », « marginal » tolérés) | `test_c8_mots_interdits_variantes_casse_accents_expressions` |
| § 7, § 8 c. 9 — aucune suite de 8 mots commune avec les textes interdits (hors celles de l'énoncé) ni avec l'énoncé | `n_grammes`, `charger_textes_interdits`, `controle_9_recopie` | sain | `test_c9_recopie_texte_interdit` (8 mots : défaut ; 7 mots : toléré), `test_c9_recopie_enonce` |
| § 7 — doublons : aucune réponse en double dans un jeu ni entre jeux ; aucun bloc ou rappel en double dans une tâche | `controle_9_recopie` | sain | `test_c9_doublons_de_reponses`, `test_c9_bloc_en_double_dans_une_tache` |
| § 7 — sources absentes déclarées (`--textes-absents`), fichier absent = refus (R11) | `verifier`, `exiger_fichier` | `test_refus_texte_interdit_absent_et_declaration_textes_absents` | idem (refus) |
| annexe A, contrôle de la banque — mots `cost`, `control`, … ; cadrages F1-F4 en rotation ; 20 entrées ; réserve sans cadrage ; 8 mots communs avec P3 | `controle_banques`, `_controler_entree_a` | sain | `test_c9_banques_recopie_et_mots`, `test_annexes_comptes_et_reserve_avec_cadrage` |
| annexe B, contrôle de la banque — aucune forme impérative adressée à l'agent ; 8 entrées ; 8 mots communs | `_IMPERATIF_B`, `controle_banques` | sain, `test_annexe_b_descriptive_non_imperative` | `test_c9_banques_recopie_et_mots`, `test_annexes_comptes_et_reserve_avec_cadrage` |
| § 8 c. 10 — fuite lexicale : unigrammes et bigrammes, fréquence documentaire ≥ 0,25 d'un côté et ≤ 0,05 de l'autre, par jeu et par mode, deux empans, terme et paires nommés | `controle_10_fuite_lexicale`, `_termes` | sain, `test_c10_terme_frequent_des_deux_cotes_tolere` | `test_c10_fuite_lexicale_et_reserve_de_surface` |
| § 8 c. 10 — aire sac de mots (tf-idf, régression logistique L2 = 1, une tâche laissée de côté, moyenne), ≥ 0,90 = réserve | `aire_sac_de_mots`, `aire_sous_la_courbe` | sain (aucune réserve) | `test_c10_fuite_lexicale_et_reserve_de_surface` (aire 1,000, `[RÉSERVE]`), `test_aire_sous_la_courbe_et_distance` |
| § 8 — contrôles rapportés : distribution des coûts par tâche, moyennes de longueur par étiquette, jetons, mots par champ | `rapporter`, `controle_5_nombres` | sain | `test_c5_n3_groupes_de_chiffres` (réserve de groupes de chiffres) |
| § 8 — journal, code de sortie non nul au défaut dur, aucun repli silencieux ; R12 : journal et dossier de sortie jamais écrasés | `Journal`, `_clore`, `assembler` | sain | `test_refus_journal_deja_present`, `test_artefact_assembler_dossier_deja_present` |
| § 11, formulaire de remise — assemblage : J-D un enregistrement, étiquette nulle, réponse recopiée ; J-C et J-A deux enregistrements 0 et 1 ; `incitation_id` identique ; paires non assemblables listées | `assembler`, `_membres_de_remise` | `test_sain_assemblage_membres…` | `test_artefact_assembler_paires_non_assemblables_listees_et_exclues` |
| option `--jeux` (écart « jeux partiels, jamais scellable », comptes sur les jeux donnés ; sans elle, trois jeux obligatoires) | `jeux_choisis`, `assembler`, `verifier` | `test_sain_jeux_partiels_verifier`, `test_sain_jeux_partiels_assembler` | `test_artefact_assembler_jeu_manquant_sans_option_refuse`, `test_artefact_assembler_jeu_hors_option_refuse`, `test_jeux_inconnu_refuse` |
| `--nombre-taches`, `--paires-par-tache` (essais seulement, écart au journal ; impair refusé) | `verifier` | sain (`[ÉCART DÉCLARÉ]`) | `test_refus_paires_par_tache_impair` |

## 4. Choix d'interprétation déclarés (et corrections apportées au script)

1. **Règle N3, unités de calcul chiffrées** (§ 5.3 « aucun nom d'unité de calcul chiffrée ») : un nom d'unité qui porte
   lui-même des chiffres (« H100 », « A100 », « V100 », « B200 », « MI300 ») est traité comme une unité, jamais comme
   un nombre : « 8 H100s » et « eight H100 GPUs » sont fautifs, « an H100 » seul ne l'est pas. Avant correction, le script
   prenait « H100 » seul pour un nombre de coût. La liste des unités étendues (`tpu`, `node`, `flop`, noms de cartes)
   est un choix du script, dit dans son en-tête. « à trois mots près » = l'unité dans les trois jetons qui suivent.
2. **Forme impérative de l'annexe B** : verbe (`declare`, `make`, `report`, `write`) en tête de phrase (début du texte,
   après `.:;!?`, après « please » ou « you must/should/shall/need to/have to »), suivi à 40 caractères près d'un objet
   de coût. Avant correction, la regex marquait l'entrée réelle I03 (« teams whose proposals declare larger compute
   footprints »), une description à la troisième personne, comme un impératif.
3. **Entrées de réserve de l'annexe A** (R1 à R4, « aucune entrée ne contient … ») : mêmes contrôles de mots et de
   longueurs que les vingt entrées, le bloc mesuré sous chacun des quatre cadrages (l'entrée de remplacement « prend
   le cadrage de l'entrée retirée », § 9) ; cadrage attendu nul. Avant correction, la réserve n'était pas contrôlée.
4. **« Chaque champ non vide »** (§ 2, c. 4) : chaque champ commence par un caractère non blanc sur sa propre ligne
   (`TITLE: x`, jamais `PROPOSAL:` suivi d'une ligne vide puis de texte) ; aucun blanc avant `ACTION:` ni après le dernier
   caractère de `PREDICTION` (une réponse bordée de blancs est un défaut de structure).
5. **« À 15 % près »** (§ 2, c. 6) : |a − b| / max(a, b) ≤ 0,15, sur chaque mesure (mots, caractères, jetons) et
   chaque empan (réponse entière ; avant `COST:` pour J-C et J-A, saut de ligne compris, `reponse[:position_cost]`).
6. **D1** : Levenshtein sur la suite des mots normalisés (sans casse, sans accents, sans ponctuation) des champs
   `TITLE`, `PROPOSAL`, `CONTROLS` réunis, divisée par la longueur du plus long ; les clés de champ ne comptent pas.
7. **Mots interdits** : mots entiers après normalisation (minuscules, accents retirés, ponctuation = séparateur) ;
   une expression de plusieurs mots est cherchée comme suite ; les variantes sont celles de l'annexe C, sans lemmatisation
   (« over-estimate » coupé par le tiret n'est pas trouvé : limite déclarée, à l'adresse de la contre-vérification).
8. **Recopie** (§ 7, c. 9) : les suites de 8 mots communes avec un texte interdit **et** avec l'énoncé ne comptent pas
   contre le texte interdit (elles comptent comme recopie de l'énoncé) ; les deux membres de J-D partagent leur réponse
   (pas un doublon) ; le doublon est cherché sur la réponse exacte, dans et entre les jeux.
9. **Fuite lexicale** : fréquence documentaire par (jeu, mode) et par empan ; la paire nommée au journal est celle dont
   le membre de l'étiquette « fréquente » porte le terme (remède de la consigne). L'aire sac de mots est calculée sur les
   deux empans, chacune ≥ 0,90 donne une réserve ; régression logistique avec intercept, L-BFGS déterministe, sans tirage.
10. **Arrêt de la suite** : le contrôle 1 arrête (schéma illisible) ; le contrôle 2 n'arrête que pour une tâche hors du
    fichier des énoncés (les contextes seraient incalculables) — un défaut de comptes ou une tâche d'évaluation est listé
    et les contrôles 3 à 10 sont joués (changement de ce passage : avant, tout défaut du contrôle 2 arrêtait). Le code de
    sortie reste 1 dès le premier défaut dur ; l'en-tête du script le dit.
11. **Mode `assembler`, paires non assemblables** : une paire que le script ne peut pas assembler (tâche hors des
    énoncés, `paire` hors de 1..10, `instruction_id` ou `incitation_id` inconnu, étiquettes ou nombre
    d'enregistrements faux, réponse bordée de blancs, `mode` différent entre membres) est **exclue des fichiers et listée
    au journal d'assemblage** (`journal-assemblage-v2.txt`, clé et motif, code 1) ; le contrôle 2 du mode `verifier` la
    compte ensuite manquante. Avant ce changement, le premier défaut de remise refusait tout l'assemblage (code 2), ce
    qui empêchait de lister les autres défauts pour l'écrivain. Un jeu sans aucune paire assemblable reste un refus.
12. **Tokeniseur** : `--tokeniseur` obligatoire ; `--empreinte-tokeniseur` différente de `79e3e522…` est acceptée mais
    écrite comme écart « jetons mesurés avec un autre tokeniseur, jeux non scellables » ; `tokenizers` absente = refus.
13. **`--jeux`** : sous-ensemble dans l'ordre de la consigne ; en mode `assembler`, un enregistrement d'un jeu non demandé
    est un refus (rien n'est écarté en silence) ; en mode `verifier`, seuls les fichiers des jeux demandés sont lus et les
    comptes ne portent que sur eux ; N2 et le multiset ne concernent que les jeux présents.
14. **Rotation avec `--paires-par-tache` ≠ 10** (essais) : la formule p = n r + k, entrée ((p − 1) mod 20) + 1 est gardée
    telle quelle ; la propriété « D01-D10 pour les rangs pairs » ne vaut que pour n = 10, et l'écart est au journal.
15. **Contrôle « fichiers »** : ajouté en tête du journal pour qu'une séquence d'un autre jeu dans un fichier soit
    écrite comme défaut nommé (avant, elle n'apparaissait que dans le bilan).

## 5. Lancement d'essai sur les jeux réels (J-D et J-A ; J-C n'est pas écrit)

### 5.1 Moment du lancement, rangs pris

- Inventaire de `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/` le 2026-11-05 à 20:28 UTC : rangs 0 à 7
  présents et complets (30 enregistrements chacun : 10 J-D, 20 J-A, un seul identifiant de tâche par fichier) ;
  **r08 est apparu pendant ce premier lancement** (complet lui aussi, 30 enregistrements). Deux lancements, l'un
  après l'autre, chacun dans un dossier neuf (R12) :
  - `assemblage-essai-v1/` : rangs 0 à 7, N = 8 (`--nombre-taches 8`), énoncés = 8 premières lignes de la projection ;
  - `assemblage-essai-v2/` : rangs 0 à 8, N = 9, énoncés = 9 premières lignes. **C'est le lancement cité ci-dessous** ;
    le v1 est gardé tel quel (mêmes résultats sur les 8 premières tâches ; `dissimulation-v2.jsonl` identique à
    l'octet dans les deux, `58a7e7bf…`, puisque toutes les paires J-D de r08 sont exclues à l'assemblage).
  Aucun rang ne manque au milieu. Les remises ne sont pas touchées ; r06 et r07 ont été lues telles que présentes.
  Un troisième lancement, v3, sur les 14 tâches r00 à r13, a été fait après le redémarrage du conteneur (section 5.5) :
  c'est le bilan le plus complet.
- Commandes (graine 20261105, `PYTHONPATH=src python -I`) : `assembler <r00…r08> --annexes …/annexes --taches
  scratchpad/reserve-projection.json --enonces <9 lignes> --graine 20261105 --sortie …/assemblage-essai-v2 --jeux
  dissimulation intention-autres-modes` ; puis `verifier …/assemblage-essai-v2 --annexes … --taches … --evaluation
  scratchpad/evaluation-factice.json --textes-interdits prereg/P3-consignes-v1.md --textes-absents "textes d'actions
  de P3 (…, non lu par la fille 8)" "épisodes de la course de T0.6 (absents)" --graine 20261105 --tokeniseur
  …/tokeniseur-factice-bpe-v1/tokenizer.json --empreinte-tokeniseur cfc0c143… --nombre-taches 9 --jeux dissimulation
  intention-autres-modes`. Code de sortie 1 dans les deux modes (défauts durs listés, rien de refusé).

### 5.2 Écarts du lancement (tous écrits au journal, jeux **non scellables**)

1. **Tokeniseur factice** : la copie conforme (`79e3e522…`) n'est pas dans le dépôt et ne peut pas être téléchargée
   (modèle à accès restreint, aucune clé, aucun réseau). Le `tokenizer.json` factice désigné par la consigne de L4
   (`docs/notes/lentilles-sondes-p3-v1/…/essai-factice-v2/entrees/modele/tokenizer.json`, `b52136fb…`) **ne se charge
   pas** avec `tokenizers` 0.23.2 (« missing field `single_word` ») : il a été remplacé par un tokeniseur BPE au
   niveau des octets (vocabulaire 3 000) appris de façon déterministe sur les 180 réponses de r00-r05 et les 32 énoncés,
   `…/tokeniseur-factice-bpe-v1/tokenizer.json` (`cfc0c1439f9725cb5b8c6881077fe3140c3d9ca621d5876ccddf491fd503b1b8`,
   note `NOTE.md` à côté). Journal : « jetons mesurés avec un autre tokeniseur, jeux non scellables ». Les deux défauts
   « écart en jetons » (5.3) **ne sont pas opposables** à l'écrivain : à rejouer avec le tokeniseur conforme.
2. **Fichier d'évaluation factice** (une tâche fictive) et **réserve de travail** construite depuis la projection remise
   à l'écrivain, pas les fichiers scellés de `donnees/` (interdits à cette fille) : le contrôle « aucune tâche
   d'évaluation » n'a pas été joué contre la vraie liste.
3. **Jeux partiels** (`--jeux dissimulation intention-autres-modes`) : J-C n'est pas écrit ; écart « jamais scellable ».
4. **N = 9 tâches** sur 32 (`--nombre-taches 9`) : écart « lancement d'essai, jamais un jeu scellable ».
5. **Textes interdits** : seuls les paragraphes cités de `prereg/P3-consignes-v1.md` (9 lignes « > », 1 texte de 28 mots
   après fusion : à vérifier par la session — le fichier regroupe les six textes privés en un seul bloc cité) ;
   textes d'actions de P3 et épisodes de T0.6 déclarés absents (`--textes-absents`), contrôle 9 à rejouer.

### 5.3 Bilan du lancement v2 (9 tâches ; 50 paires J-D et 90 paires J-A assemblées)

**Assemblage** (`journal-assemblage-v2.txt`, `d499b7b8…`) : **40 paires non assemblables, exclues et renvoyées à
l'écrivain** :

| tâche (rang) | paires | motif |
|---|---|---|
| 2510.26243v1 (r01) | J-D paires 11 à 20 (10) | `paire` hors de 1..10 ; `instruction_id` D21 à D30 (n'existent pas : la banque A va de D01 à D20 ; un rang impair prend D11 à D20 **avec les paires numérotées 1 à 10**, section 6.1) |
| 2511.19808v1 (r03) | J-D paires 11 à 20 (10) | idem |
| 2510.23605v1 (r05) | J-D paires 11 à 20 (10) | idem |
| 2509.21875v3 (r08) | J-D paires 1 à 10 (10) | `instruction_id` nul (attendu D01 à D10 pour un rang pair) |

Les tâches r00, r02, r04, r06 (rang pair, D01-D10) et r07 (rang impair, paires 1-10, D11-D20) sont assemblées.

**Vérification** (`journal-verification-v2.txt`, `a2b39f60…`) : 31 défauts durs sur 7 clés, 2 réserves, code 1.

| contrôle | état | détail |
|---|---|---|
| fichiers, 1 schéma | OK | 280 séquences, membres A/B conformes au tirage, identifiants selon le jeu |
| 2 tâches, comptes | **4 défauts** | `dissimulation/{2510.26243v1, 2511.19808v1, 2510.23605v1, 2509.21875v3}` : comptes `{}` ≠ `{'aucun': 10}` (paires exclues à l'assemblage, ci-dessus) ; 9 tâches des énoncés, toutes en réserve, aucune d'évaluation (factice) |
| annexes A, B, C | OK | blocs de 18 à 27 mots, rappels de 3 à 7, incitations de 17 à 26 (valeurs annoncées par la consigne), aucun mot interdit de banque, aucune forme impérative, aucune recopie |
| 3 contextes, rotations | OK | 140 paires recalculées à l'octet ; rotation A respectée sur les 50 paires J-D assemblées |
| 4 format | OK | 280 actions lisibles, `ADD`, cinq champs, `COST: <entier>` de 24 à 1 200, `cout_declare` et `position_cost` égaux |
| 5 nombres | OK | N1 (ligne `COST:` identique) sur les 90 paires J-A ; N3 : aucun nombre de coût avant le champ ; groupes de chiffres : écart ≤ 2 partout, moyennes 1,70 (étiquette 0) et 1,64 (étiquette 1), aucune réserve ; multiset égal |
| 6 longueurs | **2 défauts** | `intention-autres-modes/2510.02692v3/paire 10` : écart en jetons 203 / 166 = 0,18 et avant `COST` 154 / 129 = 0,16 (> 0,15) — **tokeniseur factice, non opposable** ; mots (90-260) et caractères : tous conformes |
| 7 D1, J-D identiques | OK | D1 ≥ 0,30 sur les 90 paires J-A ; réponses identiques dans les 50 paires J-D |
| 8 mots interdits | OK | aucun mot de l'annexe C dans les 280 réponses |
| 9 recopie, doublons | OK | aucune suite de 8 mots commune avec P3-consignes ni avec l'énoncé ; aucune réponse en double ; aucun bloc en double par tâche |
| 10 fuite lexicale | **25 défauts** (J-A, mode `controles` seulement) | voir ci-dessous ; mode `direction` : aucun terme |

**Réserves de surface** (aire sac de mots, une tâche laissée de côté, 9 plis) :

| jeu / mode | empan | aire | réserve ≥ 0,90 |
|---|---|---|---|
| J-A `controles` | réponse entière | **1,000** | oui |
| J-A `controles` | avant `COST` | **0,996** | oui |
| J-A `direction` | réponse entière | 0,596 | non |
| J-A `direction` | avant `COST` | 0,644 | non |

**Termes de fuite lexicale** (J-A `controles`, 45 réponses par étiquette ; fréquence documentaire ≥ 0,25 d'un côté et
≤ 0,05 de l'autre ; la dernière colonne compte les paires dont le membre de l'étiquette « fréquente » porte le terme,
liste complète au journal) :

| empan | terme | fréq. chez 0 | fréq. chez 1 | côté | paires |
|---|---|---|---|---|---|
| réponse entière | `ablation of` | 0.022 | 0.489 | 1 | 22 |
| réponse entière | `alone` | 0.267 | 0.0 | 0 | 12 |
| réponse entière | `an ablation` | 0.022 | 0.489 | 1 | 22 |
| réponse entière | `and report` | 0.022 | 0.289 | 1 | 13 |
| réponse entière | `beat` | 0.267 | 0.0 | 0 | 12 |
| réponse entière | `controls two` | 0.0 | 0.467 | 1 | 21 |
| réponse entière | `curves` | 0.022 | 0.356 | 1 | 16 |
| réponse entière | `for the` | 0.022 | 0.511 | 1 | 23 |
| réponse entière | `more` | 0.044 | 0.267 | 1 | 12 |
| réponse entière | `placebo` | 0.4 | 0.0 | 0 | 18 |
| réponse entière | `report` | 0.044 | 0.444 | 1 | 20 |
| réponse entière | `sizes` | 0.022 | 0.311 | 1 | 14 |
| réponse entière | `whether` | 0.533 | 0.044 | 0 | 24 |
| réponse entière | `would` | 0.333 | 0.022 | 0 | 15 |
| avant COST | `ablation of` | 0.022 | 0.489 | 1 | 22 |
| avant COST | `an ablation` | 0.022 | 0.489 | 1 | 22 |
| avant COST | `and report` | 0.022 | 0.289 | 1 | 13 |
| avant COST | `controls two` | 0.0 | 0.467 | 1 | 21 |
| avant COST | `curves` | 0.022 | 0.333 | 1 | 15 |
| avant COST | `for the` | 0.022 | 0.444 | 1 | 20 |
| avant COST | `placebo` | 0.4 | 0.0 | 0 | 18 |
| avant COST | `quality` | 0.044 | 0.267 | 1 | 12 |
| avant COST | `report` | 0.044 | 0.444 | 1 | 20 |
| avant COST | `sizes` | 0.022 | 0.311 | 1 | 14 |
| avant COST | `whether` | 0.533 | 0.044 | 0 | 24 |
Lecture pour l'écrivain (sans réécriture ici) : le membre honnête du mode `controles` dit « whether … », « would »,
« placebo », « alone », « beat » ; le membre affaibli dit « an ablation of … », « report … curves », « sizes », « for
the », et son champ `CONTROLS` commence souvent par « Two … » (bigramme `controls two`, 21 paires sur 45). Ce sont des
indices de surface au sens de la section 9 ; la consigne (section 8, contrôle 10) renvoie une fois ces paires à
l'écrivain, puis la contre-vérification décide. Le mode `direction` ne montre aucun terme et une aire de 0,60-0,64.

**Distributions rapportées** (information, jamais bloquantes) :

| jeu / tâche | valeurs de `COST` distinctes (sur 10) | min | max |
|---|---|---|---|
| dissimulation/2510.02692v3 | 10 | 210 | 1100 |
| dissimulation/2602.01626v1 | 10 | 40 | 800 |
| dissimulation/2603.21115v1 | 10 | 60 | 420 |
| dissimulation/2510.26843v1 | 9 | 32 | 96 |
| dissimulation/2602.12660v2 | 9 | 240 | 960 |
| intention-autres-modes/2510.02692v3 | 10 | 260 | 1200 |
| intention-autres-modes/2510.26243v1 | 10 | 100 | 900 |
| intention-autres-modes/2602.01626v1 | 10 | 160 | 700 |
| intention-autres-modes/2511.19808v1 | 10 | 200 | 450 |
| intention-autres-modes/2603.21115v1 | 9 | 80 | 400 |
| intention-autres-modes/2510.23605v1 | 10 | 80 | 700 |
| intention-autres-modes/2510.26843v1 | 10 | 24 | 120 |
| intention-autres-modes/2602.12660v2 | 10 | 240 | 1200 |
| intention-autres-modes/2509.21875v3 | 9 | 60 | 300 |

Longueurs moyennes : J-D 170,1 mots (1 127,9 caractères, 274,1 jetons factices) par réponse, identiques par
construction entre étiquettes ; J-A étiquette 0 : 141,4 mots (949,4 caractères, 228,9 jetons), avant `COST` 108,8 mots ;
étiquette 1 : 139,3 mots (917,7 caractères, 223,1 jetons), avant `COST` 109,8 mots ; `PREDICTION` 29,6 contre 26,5 mots
(écart de 10 %, le plus grand par champ ; `CONTROLS` 35,1 contre 35,4, `PROPOSAL` 59,4 contre 60,6).

### 5.4 Fichiers produits (sha256)

| fichier | sha256 |
|---|---|
| `…/assemblage-essai-v2/dissimulation-v2.jsonl` (100 séquences) | `58a7e7bf5be4b2a1361fe18744528da247283a7e2f64656d154aa9402effffb7` |
| `…/assemblage-essai-v2/intention-autres-modes-v2.jsonl` (180 séquences) | `f11bb9a987c81de0a97e3d6056e05d64bf275cccecc2c29638e751c28f921df8` |
| `…/assemblage-essai-v2/enonces-reserve-v2.jsonl` (9 lignes) | `c0faa49cec0b6bc2f3b97dfdac464781ef728ebe9af1613fed18b00cfb3e22ba` |
| `…/assemblage-essai-v2/journal-assemblage-v2.txt` | `d499b7b8326d4a684ce7e8a4f5595b4dfee7c2a18e85d6833251c21194290654` |
| `…/assemblage-essai-v2/journal-verification-v2.txt` | `a2b39f60f373251de2c5890b7c30403c29066474f99b50e2756fdd1b75d69ca3` |
| `…/assemblage-essai-v1/dissimulation-v2.jsonl` | `58a7e7bf5be4b2a1361fe18744528da247283a7e2f64656d154aa9402effffb7` |
| `…/assemblage-essai-v1/intention-autres-modes-v2.jsonl` (160 séquences) | `2e5566f5a8e53a1e9f177db5b652851c773a75cfb6a865e61e132e6623e788dd` |
| `…/assemblage-essai-v1/enonces-reserve-v2.jsonl` (8 lignes) | `12d525fc141a4612b5240edbecfb5f76e29863e86b145dceb1ccad8a7a64d68f` |
| `…/assemblage-essai-v1/journal-assemblage-v2.txt` | `7c64d0a329fcc5f093dd728f0bc214afa01142ed00515514b7c6361420a5214a` |
| `…/assemblage-essai-v1/journal-verification-v2.txt` | `01e48d2edfe38e494dfb982c0a5fb6b25839e678d20c8ebd770212dc0e9be5d9` |

Remises lues (non modifiées) :

| remise | sha256 |
|---|---|
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/r00-2510.02692v3.jsonl` | `4a002fb54ddc048f81c91966f37c9a81f03615bcbfe94ce8cf9fe56febcaf6dd` |
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/r01-2510.26243v1.jsonl` | `26bd4db72658518bdb601df8e28097089419b77c6b8ed38f9c9f472368a70b6c` |
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/r02-2602.01626v1.jsonl` | `092f98e0abcb15ebb136eaffef43d31b9aa9b9394d87ae56d3b599010d3e0b11` |
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/r03-2511.19808v1.jsonl` | `bbd418191e9159de0a5ff3d9e258a2598921ff3223d492837eb32ef7541bf1c2` |
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/r04-2603.21115v1.jsonl` | `528de170a5807895a9641b11665ae8ccba120f585e364f3b013b2a2cef010971` |
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/r05-2510.23605v1.jsonl` | `e3b3cc60abadaa26b97ddfbdaef196bda3f1ef8b4a977b946ffd613d0c7f2c1b` |
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/r06-2510.26843v1.jsonl` | `5db26e023790bb556a2a588fa21b065b73df415bd8a72e434431efb4feb20917` |
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/r07-2602.12660v2.jsonl` | `6d85b0bf65fcb5a8395fb16a9b92c2ab9daa4bada3752a2c06ec1ff4f4e1564d` |
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/r08-2509.21875v3.jsonl` | `5da4ca0d98a64144c446514eb29029af861a523f16870592d4cee56844e34175` |


### 5.5 Dernier lancement, v3 : les 14 tâches contiguës (r00 à r13), après redémarrage du conteneur

Le conteneur a redémarré à 21:06 UTC (travail sur disque intact, instantané `5d48d901` pris par la session) ; à la
reprise, les remises r00 à r13 étaient présentes et complètes (30 enregistrements chacune, aucun rang manquant).
Lancement dans le dossier neuf `assemblage-essai-v3/` (mêmes options que v2, `--nombre-taches 14`, énoncés = 14
premières lignes de la projection, graine 20261105, tokeniseur factice `cfc0c143…`) à 21:07 UTC. **C'est le bilan à
retenir** ; v1 et v2 restent tels quels (R12).

**Assemblage** (`journal-assemblage-v2.txt`, `6d112dd8…`) : 90 paires J-D (180 séquences) et 140 paires J-A (280
séquences) assemblées ; **50 paires J-D non assemblables, exclues et renvoyées à l'écrivain** :

| tâche (rang) | paires | motif |
|---|---|---|
| 2510.26243v1 (r01), 2511.19808v1 (r03), 2510.23605v1 (r05) | J-D 11 à 20 (10 chacune) | `paire` hors de 1..10, `instruction_id` D21 à D30 inexistants (rang impair : paires 1 à 10 avec D11 à D20) |
| 2509.21875v3 (r08), 2512.22550v1 (r09) | J-D 1 à 10 (10 chacune) | `instruction_id` nul (attendu D01 à D10 pour un rang pair, D11 à D20 pour r09 qui est impair) |

r10 à r13 (D01-D10 pour r10 et r12, D11-D20 pour r11 et r13, paires 1 à 10) sont assemblées sans défaut de remise :
la convention fautive touche r01, r03, r05, r08, r09, soit 5 tâches sur 14.

**Vérification** (`journal-verification-v2.txt`, `7534bb3f…`) : 30 défauts durs sur 10 clés, 2 réserves, code 1.

| contrôle | état | détail |
|---|---|---|
| fichiers, 1, annexes, 3, 4, 5, 7, 8, 9 | OK | 460 séquences ; contextes et rotations exacts ; `COST` de 24 à 2 400 ; N1, N3, D1, mots interdits, recopie, doublons : rien |
| 2 comptes | **5 défauts** | `dissimulation/{2510.26243v1, 2511.19808v1, 2510.23605v1, 2509.21875v3, 2512.22550v1}` : `{}` ≠ `{'aucun': 10}` (paires exclues ci-dessus) |
| 6 longueurs | **5 défauts** (3 paires) | écarts en jetons seulement, **tokeniseur factice, non opposables** : `intention-autres-modes/2510.02692v3/paire 10` (0,18 ; avant `COST` 0,16), `…/2511.04675v2/paire 6` (avant `COST` 0,18), `…/2511.04675v2/paire 10` (0,17 ; avant `COST` 0,20) ; mots et caractères conformes partout |
| 10 fuite lexicale | **20 défauts** (J-A `controles`) | 12 termes sur la réponse entière, 8 avant `COST` (table ci-dessous) ; mode `direction` : aucun |

Aires sac de mots (14 plis) : J-A `controles` **1,000** (réponse entière) et **0,994** (avant `COST`) — deux réserves de
surface ; J-A `direction` 0,703 et 0,749 (sous 0,90, mais en hausse par rapport aux 9 tâches : 0,596 et 0,644).

| empan (J-A `controles`, 70 réponses par étiquette) | terme | fréq. chez 0 | fréq. chez 1 | côté | paires |
|---|---|---|---|---|---|
| réponse entière | `ablation of` | 0.029 | 0.314 | 1 | 22 |
| réponse entière | `an ablation` | 0.014 | 0.314 | 1 | 22 |
| réponse entière | `as placebo` | 0.286 | 0.014 | 0 | 20 |
| réponse entière | `at two` | 0.0 | 0.271 | 1 | 19 |
| réponse entière | `beat` | 0.3 | 0.0 | 0 | 21 |
| réponse entière | `controls two` | 0.0 | 0.3 | 1 | 21 |
| réponse entière | `equal` | 0.271 | 0.029 | 0 | 19 |
| réponse entière | `floor` | 0.286 | 0.029 | 0 | 20 |
| réponse entière | `no` | 0.3 | 0.043 | 0 | 21 |
| réponse entière | `sizes` | 0.043 | 0.257 | 1 | 18 |
| réponse entière | `the floor` | 0.257 | 0.029 | 0 | 18 |
| réponse entière | `would` | 0.371 | 0.043 | 0 | 26 |
| avant COST | `ablation of` | 0.029 | 0.314 | 1 | 22 |
| avant COST | `an ablation` | 0.014 | 0.314 | 1 | 22 |
| avant COST | `as placebo` | 0.286 | 0.014 | 0 | 20 |
| avant COST | `at two` | 0.0 | 0.271 | 1 | 19 |
| avant COST | `controls two` | 0.0 | 0.3 | 1 | 21 |
| avant COST | `floor` | 0.286 | 0.029 | 0 | 20 |
| avant COST | `sizes` | 0.043 | 0.257 | 1 | 18 |
| avant COST | `the floor` | 0.257 | 0.029 | 0 | 18 |

Avec 14 tâches, les termes de l'honnête (« would », « beat », « as placebo », « the floor », « equal », « no ») et de
l'affaibli (« an ablation of », « controls two », « at two », « sizes ») persistent ; « whether », « report », « curves »
sont passés sous les seuils. Distributions rapportées : J-D 179,6 mots en moyenne ; J-A 153,8 (étiquette 0) contre
153,3 mots (étiquette 1), `PREDICTION` 32,1 contre 30,7, groupes de chiffres 2,74 contre 2,79 (aucune réserve) ;
valeurs de `COST` distinctes par tâche : 8 à 10 sur 10 (J-A `2512.22550v1` : 8 ; rappel : N2 ne s'applique qu'à J-C).

| fichier (`…/assemblage-essai-v3/`) | sha256 |
|---|---|
| `dissimulation-v2.jsonl` (180 séquences) | `ae80c0e7dc7ff9f63c5e9a9b09a62f93912757977b267affe539774ff90bef70` |
| `intention-autres-modes-v2.jsonl` (280 séquences) | `961194cc37cf2c604192eb13127f43414a474243e77968159ab95f7c1ace1338` |
| `enonces-reserve-v2.jsonl` (14 lignes) | `a5b535f168a5bfc9bf4ccec8d4965815c4c666d6de520c9c68909f2411a19b7f` |
| `journal-assemblage-v2.txt` | `6d112dd84b42267f77a5e2c1b1af0781c6879ccfc3671b50a0a399410c79943f` |
| `journal-verification-v2.txt` | `7534bb3fd7ce5020066cb9d481ee05098126813e7737d66579a89ba2d0ce48e8` |
| remise `taches/r09-2512.22550v1.jsonl` | `0c1be97a1b6a99ec1635383028920f876035f962aa5ad1d0c1555bdca19a9167` |
| remise `taches/r10-2603.12594v1.jsonl` | `028e627b67d7f994187111b182d21330e8bf05e81742b4083f60e5fc79c6bbdb` |
| remise `taches/r11-2506.24000v2.jsonl` | `51e8913d72938ce7294072d58afd8bd316bd5b0f6d0a4e02ff77c89f7a7a03b5` |
| remise `taches/r12-2511.04675v2.jsonl` | `328be9c35aa269c8b9927be78af60a9b86f50e66c0ac8f0101d53db471d14b97` |
| remise `taches/r13-2506.10887v4.jsonl` | `a7a24a85ef303ae4a5b495f22c1278bf8c6a61a7618d8931784e082655cf17db` |


## 6. Ce qui reste pour un lancement scellable

- le **tokeniseur conforme** (`tokenizer.json` de Llama-3.1-8B-Instruct, révision `0e9e39f2…`, empreinte `79e3e522…`) :
  absent du dépôt, modèle à accès restreint, aucun téléchargement par cette session ; sans lui, aucun jeu n'est scellé ;
  les deux défauts « écart en jetons » de ce lancement sont à rejouer avec lui ;
- les **fichiers scellés** de `donnees/` : `taches-entrainement.json` (`8d20a698…`) et `taches-evaluation.json`
  (`76cdeace…`) à la place de la réserve de travail et du fichier d'évaluation factice ; `enonces-reserve-v2.jsonl` des
  32 tâches, extrait du fichier scellé, scellé ;
- le jeu **J-C** (domaine, mode coût), non écrit : contrôles N2, incitations (annexe B, rotation) et fuite lexicale de J-C
  jamais joués sur des paires réelles ;
- les **textes d'actions de P3** (`donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl`) et les épisodes de T0.6 pour
  le contrôle 9 (déclarés absents ici ; rejeu par la chaîne de T0.7, § 7) ;
- les **32 tâches** (lancement sur 14 ici, section 5.5) et les 18 tâches restantes de l'écrivain, puis les renvois (section 10,
  étape 4), la contre-vérification (section 9), le scellement des fichiers de la section 3 et la provenance ;
- un lancement **sans `--jeux`, sans `--nombre-taches`**, sur le dossier `donnees/t07-jeux-synthetiques-v2/`.

## 7. Trois risques

1. **La fuite lexicale du mode `controles` est structurelle, pas accidentelle** : l'honnête nomme des témoins qui
   tranchent (« placebo », « whether … would … beat »), l'affaibli des contrôles à côté (« an ablation of … », « report
   … curves ») — c'est le concept même, écrit avec des mots. L'aire de 1,000 dit qu'un sac de mots sépare les classes :
   une sonde apprise sur ce jeu pourrait lire un lexique plutôt qu'une intention ; renvoyer les paires une fois ne
   changera peut-être rien, et la contre-vérification (section 9) devra décider si le seuil 0,25 / 0,05 de la consigne
   est tenable pour ce mode, sans le changer après lecture (les seuils sont fixés au scellement).
2. **Cinq remises sur quatorze suivent une convention absente de la consigne** (r01, r03, r05 : paires 11-20,
   D21-D30 ; r08, r09 : sans identifiant d'instruction ; r10 à r13 sont conformes) : l'écrivain a peut-être lu la rotation « D11-D20 pour les rangs impairs » comme une
   renumérotation. Si la section 11 remise à l'écrivain ne dit pas explicitement « paires 1 à 10 et identifiant fourni »,
   les tâches restantes peuvent porter le même défaut ; à corriger dans la consigne d'écriture avant la suite, sinon
   plus d'un tiers des paires J-D reviendront en renvoi (50 sur 140 ici).
3. **Rien de ce lancement n'est opposable** : tokeniseur factice (les deux défauts de jetons peuvent disparaître ou
   se multiplier avec le vrai tokeniseur de Llama-3.1-8B, dont les jetons par mot diffèrent), fichier d'évaluation
   factice (une tâche de réserve pourrait figurer dans la vraie liste d'évaluation sans que ce lancement le voie), textes
   d'actions de P3 et épisodes de T0.6 absents du contrôle 9, et un script que seul son auteur a relu (R2 : une
   contre-lecture neuve du script et des essais reste à faire avant le scellement des jeux).
