# Addendum au préenregistrement de R1 — relance v4 : réparation des 89 épisodes cassés (lot fidèle à plusieurs cibles), table de tokenisation v4, rejeu des 2 400 actions de P3 — v4

## Changements du brouillon 3 (par rapport au brouillon 2)

Brouillon 2 : `prereg/R1-addendum-relance-v4-brouillon2.md` (`fed5fd3b832d1836abb27dc2e934aabcdbf5f3f4444e3cbb1c86359ee7986496`). Seuls changent les points de la section 5 du rapport des ajouts (`rapport-ajouts-relance-v4-v1.md`, `0d8fd1827f58d091ac0405c4627c0b9408b61f55eb348102b4c8fed4d3f25efa`) et la mention des 381 essais (rapport de la fille, `ae72aeaa7d7efebe6828f9244386aa2a22a62f3231e481cae405437f9ce87032`). Rédacteur neuf (sous-agent, Opus 5.5), auteur ni de l'addendum, ni du code, ni de la contre-lecture ; texte non scellé. Une ligne par changement, dans l'ordre du texte ; le seul marqueur restant est celui du commit du code d'analyse (en-tête, inchangé).

| n° | Lieu | Avant → après | Source |
|---|---|---|---|
| C1 | en-tête, empreintes du code | empreintes v1 seules → plus les 9 fichiers neufs des ajouts (modules v3 et neufs, scripts v2, essais, banc v2) | rapport § 5 (« Modules et scripts… ; empreintes au § 7 ») ; § 7 |
| C2 | en-tête, configuration de la réparation | configuration v1 (`a5a61077…`, fichier `8de2737d…`) → v2 (`c34bf464…`, fichier `4d0655d1…`), différence avec la v1 dite | rapport § 5, premier point ; § 2 (arbitrage M7) ; recalcul de l'empreinte canonique par `resolution_graine_lot_v3.empreinte_config` |
| C3 | en-tête, tests attendus | 358 attendus (23 fichiers, compte passé à établir) → 381 (26 fichiers ; 381 passés, 0 sauté, au commit `af1f2f4f`, tokeniseur `0e9e39f2…`, `tokenizer.json` `79e3e522…`) | rapport § 5, deuxième point ; rapport de la fille `ae72aeaa…` |
| C4 | en-tête, documents qui font foi | devis v1 → devis v2 (`dac7a0a1…`), plus le rapport des ajouts (`0d8fd182…`) | rapport § 5, quatrième point (« devis v2 ») et dernier (sorties avec leurs empreintes) |
| C5 | Statut | « par la passe forcée du cœur sinon » → même voie, lot puis repli, quelle que soit la lecture du témoin | rapport § 5, quatrième point ; § 2 (arbitrage M7) |
| C6 | Prédiction, P-T | « alors : voie de la passe forcée » → « alors : même voie, lot puis repli » | rapport § 5, quatrième point |
| C7 | Prédiction, durée et coût | ≈ 11 USD si non exact → ≈ 18 au milieu, ≈ 36 au haut ; pire cas ≈ 57,2 inchangé | rapport § 5, quatrième point ; devis v2, §§ 1 et 3 |
| C8 | Plan d'analyse, étape 0 | « à écrire avant le scellement » → écrit et rejoué, script et sortie empreintés, 0 écart, limite dite | rapport § 5, dernier point ; §§ 2 (I4.1) et 4 |
| C9 | Plan d'analyse, étape 1 | 23 fichiers, « 358 passed » → 26 fichiers, « 381 passed » | rapport § 5, deuxième point |
| C10 | Plan d'analyse, étape 1 | conditions sans sortie citée → sorties du banc v2, de la répétition et des épreuves, avec leurs empreintes | rapport § 5, dernier point ; §§ 2 (I4) et 3 |
| C11 | Plan d'analyse, étape 2 | amorce v1 → amorce v2 | rapport § 5, troisième point |
| C12 | Plan d'analyse, étape 2 | 358 essais, `resolution_graine_lot_v2` → 381 essais, `resolution_graine_lot_v3` | rapport § 5, deuxième et troisième points |
| C13 | Plan d'analyse, étape 3, « reparation » | « voie de la passe forcée : passe forcée du cœur pour chaque cible » → une seule voie, celle du lot | rapport § 5, quatrième point ; § 2 (arbitrage M7) |
| C14 | Plan d'analyse, étape 3, étape « chaine » ajoutée | (aucune) → étape « chaine » entre « table-v4 » et « r1-rejeu » | rapport § 5, cinquième point (V4-E5 et l'étape « chaine ») |
| C15 | Plan d'analyse, étape 4, attentes de réception | (aucune) → chemins `resolution-graine-lot-v3-*.json` et commande de recalcul de réception | rapport § 5, cinquième point |
| C16 | Écarts, V4-E5 | « sinon « echec » » → arrêt avant le rejeu par l'étape « chaine » | rapport § 5, cinquième point |
| C17 | Écarts, V4-E5 | « code neuf avant le scellement » → module et essai cités | rapport § 5, troisième et cinquième points ; § 2 (I1) |
| C18 | Écarts, V4-E5 | `construire_table_v4` → commande de réception de `chaine_table_v4_v1` | rapport § 5, cinquième point |
| C19 | Écarts, V4-E6 | module `resolution_graine_lot_v2`, configuration v1 → module `resolution_graine_lot_v3`, configuration v2 | rapport § 5, premier et troisième points |
| C20 | Écarts, V4-E6 | (aucun) → modules `chaine_table_v4_v1`, `garde_depense_v4_v1`, scripts v2, banc v2 | rapport § 5, troisième point |
| C21 | Écarts, V4-E10 | 358 (23 fichiers) → 381 (26 fichiers) | rapport § 5, deuxième point ; rapport de la fille `ae72aeaa…` |
| C22 | Écarts, V4-E12 | (aucun code cité) → module `garde_depense_v4_v1`, projection + 75 min, épreuves citées | rapport § 5, sixième point ; § 2 (I2) |
| C23 | Écarts, V4-E12 | devis v1 → devis v2 | rapport § 5, quatrième point |
| C24 | Critères de lecture, témoin non exact | « voie de la passe forcée » → « même voie, lot puis repli », coût du devis v2 dit | rapport § 5, quatrième point ; devis v2, § 3 |
| C25 | Liste d'arrêt, tests | « 358 passed » → « 381 passed » | rapport § 5, deuxième point |
| C26 | Liste d'arrêt, chaîne | (aucun) → arrêt de l'étape « chaine » | rapport § 5, cinquième point |
| C27 | Coût et GO, devis | devis v1, ≈ 11 USD si non exact → devis v2, ≈ 18 au milieu, ≈ 36 au haut | rapport § 5, quatrième point ; devis v2, § 3 |
| C28 | Coût et GO, commande de création | amorce v1 → amorce v2 | rapport § 5, troisième point (« commande de création : `amorce_instance_r1_v4_v2.sh` ») |
| C29 | Surveillance, session 1 | « tests : 358 passed » → « tests : 381 passed » | rapport § 5, deuxième point |
| C30 | Surveillance, session 2 | « tests : 358 passed » → « tests : 381 passed » | rapport § 5, deuxième point |
| C31 | Surveillance, jalon de la chaîne | (aucun) → jalon « chaîne de la table v4 : conforme » (vu filtré sans « : conforme ») | rapport § 5, sixième point ; `garde_depense_v4_v1.filtrer_journal` ; `surveillance-repetition.txt` |
| C32 | Surveillance, règles et filtre | (aucun code cité) → `garde_depense_v4_v1`, avec `--tests 381` | rapport § 5, sixième point ; § 2 (I3) ; `garde_depense_v4_v1.py`, défaut `tests_attendus` = 358 |
| C33 | Essais | « à faire » → 381 passés au commit `af1f2f4f` ; sorties des ajouts citées | rapport § 5, dernier point ; rapport de la fille `ae72aeaa…` |

- Auteur : concepteur-développeur neuf de la relance v4 (sous-agent, Opus 5.5), pour Lazar ; je n'ai écrit ni R1, ni
  ses addenda, ni son code, ni le diagnostic. **Texte scellé** (brouillon 3, `f24e416f…`, plus les 19 couples de la contre-lecture neuve du delta, marqueur du commit
  rempli ; changements du brouillon 3 en tête, du brouillon 2 en pied, scellement en pied) ; reste la concordance d'un
  lecteur neuf sur la version scellée.
- Date (UTC) : 2026-11-04, brouillon commencé vers 02:10 (heure relevée par `date -u`).
- Nom nouveau (R12) : l'addendum v3 (`prereg/R1-addendum-relance-v3.md`, scellé,
  `88e262e26ea38a30e8acdf0cdf204cbdaba381baf3dbc352b4333d1fe6b299a4`, commit de scellement `139a81d3`) n'est pas
  modifié ; ce texte s'écrit **par écart à la v3** (section « Écarts déclarés ») ; ce que cette section ne cite pas vaut
  tel quel (v3, et par elle le parent).
- **GO** : `GO-2026-11-03-03` (calcul, **plafond 60 USD**, échéance 2026-11-17 ; « R1 rendu lisible (table v4) […]
  devis 5 à 12 USD ; plafond 60 USD »), dernière ligne de `registres/go.md` de la branche `canal/conv-audit-n04` qui le
  porte (tête `e7726dce` lue le 4 novembre) ; inscrit aussi sur `main` (avenant du 4 novembre). **Mot de Lazar**
  (session conv-audit, 3 novembre 2026, 08:00 UTC, 09:00 heure de Paris), verbatim : « go, plafond large bien au dela du
  siffisant » ; confirmé directement à session-depot le même jour (reçu entre 08:18:32 et 08:23:33 UTC), verbatim :
  « Pour la table v4 de R1 (ton « go, plafond large ») et pour les deux appels seuls Astra et Argon : go ».
- Préenregistrement parent (scellé, non modifié) : `prereg/R1-R2-rejeu-p3-v1.md`
  (`80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea`), commit de scellement `567260c0`.
- Chemin du préenregistrement parent : `prereg/R1-R2-rejeu-p3-v1.md`
- Commit du code d'analyse : `af1f2f4f3ab5340586dcda19c0327d0c5beeefca`
  (branche `prep/r1-relance-v4`, à partir de `04bc323a` ; code neuf seulement, aucun fichier de la v3 modifié ; entre ce
  commit et le commit de scellement, seuls changent des textes : brouillon 3, son rapport, ce texte et son sceau)
- Empreintes des fichiers de code (sha256 du fichier, arbre de travail du 4 novembre ; à revérifier au commit cité) :
  - neufs : `src/controle_ia/runs_nuit/resolution_graine_lot_v2.py`
    `501ab45308f2ffe5e3cf25b0352b0d2e7f8bca0bb2ba7cd897c3b2c39b704f87` ;
    `src/controle_ia/runs_nuit/rejeu_activations_v4.py` `d31dcec074b513b597a4920a5c6501326ee18c8cefe4bbd83d381f4ac4b25a08` ;
    `scripts/r1_v4_instance_v1.sh` `e72cf7f248bd1b0f2064b824711a3a20f43bda748ea5cacf54a2d13b31fba1f9` ;
    `scripts/amorce_instance_r1_v4_v1.sh` `4785429077afd2fdf25a8d13c3824ad0ada1cdd128e6c119080fb7fc1c1df217` ;
    `tests/test_resolution_graine_lot_v2.py` `56dcd66076ffdc9298770e81536ad2d0180de2be0e02989430f9f41668c30ac1` ;
    `tests/test_rejeu_activations_v4.py` `dc913d7ae2a335b1d3aef754454fec6ad0186d1bc8e1655f7313abf44a896d21` ; `scripts/banc_mutations_r1_v4_v1.py` `d22be91a52d524fcafdcc4d057673124605804091748bdaf92aadad09e74a6c7` ;
  - neufs, ajouts I1 à I5 (commit `af1f2f4f3ab5340586dcda19c0327d0c5beeefca` ; rapport des ajouts, § 7) ; au lancement, ils
    remplacent les deux scripts v1 et le banc v1 ci-dessus (non modifiés, plus lancés), et `resolution_graine_lot_v3` remplace `resolution_graine_lot_v2` dans les étapes (la v2 reste importée par `chaine_table_v4_v1` pour `charger_table_v4`, et essayée) :
    `src/controle_ia/runs_nuit/resolution_graine_lot_v3.py` `9ce6d17818a04853db57fdbb70e347bc9fdd0153ba91c14b9530818c6b29f6e3` ;
    `src/controle_ia/runs_nuit/chaine_table_v4_v1.py` `a015e89fd1cf39d887a05617298b7c930c939f60449b2c0ed9e75975d097bdd1` ;
    `src/controle_ia/runs_nuit/garde_depense_v4_v1.py` `1f6d4b91db36a6e439c984f5813bee419faf0a7b0ef4e5379b28ccaddb05c4dc` ;
    `scripts/r1_v4_instance_v2.sh` `a02eda0c4c8519a1d7d3ddd452001a7b8357c7e6925ca1e9c28be703d362b5ae` ;
    `scripts/amorce_instance_r1_v4_v2.sh` `22e64d72745168f947a37690e9bb29170011ef38f0649b6bbc7ca6f8825445b1` ;
    `tests/test_resolution_graine_lot_v3.py` `a50e19347dba28e3074093cff80de1d69794e7dde012f0a4fb71489c33d4618c` ;
    `tests/test_chaine_table_v4_v1.py` `f9583053deb2af39b4bc3d7d8628eed7f28bb66a3fd79ed94bf428d344afeea8` ;
    `tests/test_garde_depense_v4_v1.py` `1cdb1a1f1f5b74073f260e1196a53581b9b0c36e2ecdaa7d84d0479fbd6dc9ee` ;
    `scripts/banc_mutations_r1_v4_v2.py` `50a788ed05b155e28e1147346886cf37418b87f12ab9288e7bae5168797fce22` ;
  - importés tels quels (inchangés depuis `139a81d3`) : `resolution_graine_lot_v1.py`
    `5a9982b2a2248d5312c5a42bf34ac90c505ca579052985169aabb7e16c8c7156` ; `resolution_graine_v1.py`
    `cdc22b5ad2659f82f512c39545c52fc826a6be2dc60fb3aeafda0c5d014a9663` ; `rejeu_activations_v3.py`
    `0581cf9a32e054e5044809f80078e3d33e3de27a22830e40ca8aa45a03ca2adc` ; `rejeu_activations_v2.py`
    `6f23f802548e4de03dd7431da1179001db3ceb32d9809edbec09bc5e6b07bd2d` ; `rejeu_activations_v1.py`
    `dde8aa673720d082945722e57f31d5dd4b51e44d72f0550f7a15f5990e2ea3b5` ; `resolution_tokenisation_v1.py`
    `e8568c3c8d48a5713fddd7d55d805e54b9c702edee2b7d2f218db49c230434c9`.
- Chemin de la configuration de la réparation : `prereg/R1-reparation-v4-config-v2.json`
- Configuration de la réparation v4 (lot fidèle à plusieurs cibles, empreinte canonique) : `c34bf464177468d160975800da3cfe13d67e722a2e3b3c3e4c3c46d503ab680a`
  (fichier `4d0655d1bac5b15d6cb604e5853bed0bfe1eb48d6235772e39b86a698b8d85e5`, non scellé, scellé avec ce texte ;
  `resolution_graine_lot_v3.empreinte_config` ; égale à la v1, `prereg/R1-reparation-v4-config-v1.json`
  (canonique `a5a61077ea6a7ec65a3e1ec13126bd6f8c6f8bd9844f5559638946b8dd46e6e4`), sauf `voie_si_temoin_non_exact` =
  « lot_fidele » au lieu de « passe_forcee » : différence d'une ligne)
- Chemin de la configuration du rejeu : `prereg/R1-rejeu-config-v6.json`
- Configuration du rejeu (empreinte canonique) : `a3ef1bac5b8768604f2418da8b55c7adc8954f247485ea12c587bd00f407575f`
  (fichier `a9ebc6b0cd6c99e118ade7b304472b5452d2b43c63cc222d1adccd2ee4e95e75` ; égale à la v5 sauf la table :
  `chemin_table_tokenisation` = `prereg/R1-table-tokenisation-v4.json`, `table_tokenisation_sha256` =
  `construite-en-session`, écart V4-E5)
- Chemin de la table de tokenisation v3 : `prereg/R1-table-tokenisation-v3.json`
  (`ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423`, 22 entrées, inchangée ; elle donne les
  identifiants des 22 épisodes signalés et sert de base à la table v4)
- Entropie : `36410133060804533274328900142752730279`
- Tests attendus : `381`
  (les 26 fichiers de la liste `CIBLES` de `scripts/r1_v4_instance_v2.sh` : les 20 de la v3, plus
  `tests/test_resolution_graine_lot_v1.py`, `tests/test_resolution_graine_lot_v2.py`, `tests/test_rejeu_activations_v4.py`,
  `tests/test_resolution_graine_lot_v3.py`, `tests/test_chaine_table_v4_v1.py`, `tests/test_garde_depense_v4_v1.py` ;
  **381 passés, 0 sauté, 0 en échec** au commit `af1f2f4f3ab5340586dcda19c0327d0c5beeefca`, avec le tokeniseur de la
  révision de P3 (`meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659`, lue dans
  les deux configurations ; `tokenizer.json` `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4`,
  égal à l'empreinte attendue par les essais ; trois fichiers du tokeniseur, sans les poids) : rapport de la fille
  `brouillons/fille-2026-11-04/rapport-r1-v4-essais-tokeniseur-2026-11-04-0756.md`
  (`ae72aeaa7d7efebe6828f9244386aa2a22a62f3231e481cae405437f9ce87032`, branche `canal/fille-2026-11-04`, commit
  `97fb068133f4837fe8a170aa17d11425fd0e2194`) ; sans tokeniseur : 363 passés, 18 sautés
  (`essais-ajouts-relance-v4-sortie-v1.txt`) ; à rejouer au commit cité si un fichier change)
- Documents qui font foi (chemin et empreinte) : le parent, l'addendum v3, la table v3 ci-dessus ; le diagnostic
  `brouillons/preuves-mentors-v1/r1-v4-diagnostic-v1/rapport-diagnostic-r1-v4-v1.md`
  (`1c2dd25f36ce7bf6c144ac3e958ae1360dc3a74a16baece50a81ee8181d69c07`), son script (`b6a39191…`) et sa sortie
  (`f3e0f42d…`) ; le rapport du lecteur neuf `brouillons/preuves-mentors-v1/r1-concluant-v1/r1-concluant-fable-v1.md`
  (`371fe44337243780e9fe3a2457c1197abf5a1de6195c559ffffbf594ec81e782`) ; le devis
  `docs/notes/runs-r1-r2-r4-v1/relance-v4/devis-relance-v4-v2.md`
  (`dac7a0a1906ff42eecd391b55eeb285845eee31596b6e857d1b75e586bae6152` ; version 2 de `devis-relance-v4-v1.md`, non
  modifié) ; le rapport des ajouts `docs/notes/runs-r1-r2-r4-v1/relance-v4/rapport-ajouts-relance-v4-v1.md`
  (`0d8fd1827f58d091ac0405c4627c0b9408b61f55eb348102b4c8fed4d3f25efa`) ; le GO ci-dessus.

**Statut.** Cet addendum gèle, sous un seul texte, la **relance v4 de R1** : (1) un **témoin** du lot fidèle sur les lots
2 et 13 de P3 (aucun épisode cassé) ; (2) la **réparation** des épisodes de P3 dont la reconstruction de base diffère de
P3 et que la table v3 ne couvre pas (**89** attendus, dans **28** lots), par le lot fidèle à plusieurs cibles, puis le
repli écrit (lot à une cible, puis passe forcée du cœur), que le témoin soit exact ou non (règle écrite d'avance :
témoin non exact → lot puis repli) ; (3) la **table de tokenisation v4** ;
(4) le **rejeu** des 2 400 actions sur cette table. Il **absorbe le complément de validation** (non lancé ; écart V4-E3).
Il porte sur R1 seule (R2 et le rejeu de R4 ne se relancent pas, comme en v3). **Les hypothèses, bras, métriques,
seuils, critères de lecture et analyses scellées ne changent pas** : seule change l'**entrée** (les identifiants des
89 épisodes, chacun prouvé par l'empreinte de trajectoire de P3, 256 bits). Les runs ne visent aucun signe (R3) : la
relance vise une **couverture**, propriété de l'instrument mesurée sans lire aucun score.

## Cause (renvoi)

Diagnostic (`1c2dd25f…`), § 0 : les 89 épisodes cassés sont exactement les 89 épisodes non entièrement conformes en
longueur ; ils perdent 652 actions (honnête 18 épisodes et 134 actions, saboteur 25 et 173, témoin 29 et 234, mention 17
et 111) ; cause établie : le texte stocké, retokenisé, ne redonne pas les jetons tirés par P3 (153 redécoupages, 10
chaînes `<|reserved_special_token_N|>` épelées puis fondues, 1 U+FFFD) ; aucun calcul du modèle n'y intervient ; aucun
des 89 n'est dans la table v3 ; le code v3 les excluait en quatre endroits (diagnostic, § 6.2). La passe forcée qui
devait les réparer est fragile aux quasi-égalités (diagnostic, § 5.2 : 0,77 % de pas en désaccord avec P3), explication
probable : la non-invariance du calcul à la forme de l'appel (H1), que le témoin tranche.

## Écarts déclarés

Un écart par ligne ; « v3 » = l'addendum v3 scellé ; « parent » = `prereg/R1-R2-rejeu-p3-v1.md`.

| n° | Ligne ou règle | Règle de ce texte | Raison |
|---|---|---|---|
| V4-E1 | v3, l. 234-235 : « Si P-R5 est contraire : réserve d'instrument […] ; rien n'est relancé pour la faire tenir (R3) » | **Écart accordé par Lazar** : la relance a lieu, pour réparer la donnée (identifiants des 89 épisodes), non la règle ; verbatim : « go, plafond large bien au dela du siffisant » (3 novembre 2026, 08:00 UTC), sur l'option (a) de conv-audit (n° 404, `4a525a52…`, ligne de GO-2026-11-03-03), résumée par la consigne du développeur (`059a564f…`) : « réparer la donnée, pas la règle (lot fidèle, réparation des 89 épisodes cassés, table v4, addendum v4 qui absorbe le complément de validation, relance) » | Nœud de Lazar ; la couverture est une propriété de l'instrument, non un signe |
| V4-E2 | (aucune ligne) — aveuglement au signe | **Déclaration** : ce texte est écrit **après** lecture du résultat partiel de la v3 (run `20261103-063222-r1-rejeu-reel`), du rapport Fable (`371fe443…`) et du diagnostic (`1c2dd25f…`) ; le **signe descriptif de la v3 est connu** de Lazar, de la session et de l'auteur ; il n'est pas cité ici et ne sert à aucune règle ; aucune règle, aucun seuil, aucun texte d'analyse ne change ; la réparation ne lit ni score, ni activation, ni sortie d'analyse | Seule défense contre un choix guidé par le signe : la déclaration et la publication quel qu'en soit le sens (rapport Fable, § 4) |
| V4-E3 | Complément de validation (texte scellé au commit `4b47db7b`, `049f20ba98da75539220bd4a520dd03a3df8c16a81193cc6a4e1a650783f62ca`, configuration `prereg/R1-graine-config-complement-v2.json` `1b6f943c7fcd84f4486ab1961efbf4496392a27d61304a36e1ce50e590d545dd` ; rédigé sur son brouillon 2, `41d5350e…` ; C1 et C2 recoupés avec le texte scellé par la contre-lecture R2 : concordants) et son GO-2026-11-02-30 (40 USD) | **Absorbé** : sa validation à l'aveugle des 147 épisodes connus n'est pas lancée (elle mesure la passe forcée sur une classe où les 164 racines ne sont pas, diagnostic § 7) ; **remplacée par le témoin** (étape 2), mesure de la même chose (H1) contre P3 lui-même ; ses règles de repli sont **reprises** : frontière entière (C1 : `quasi_egalites_max` 16, `bascules_max` 2, 16 + 16 × 16 = **272** combinaisons, `combinaisons_max_lot` = 272), durées en gardes contre une boucle folle seulement (C2 : 14 400 s par épisode, 259 200 s par étape) ; **GO-2026-11-02-30 non utilisé** | Diagnostic § 7 ; rapport Fable § 9 ; GO-2026-11-03-03 |
| V4-E4 | v3, E1 (règle A : la table couvre exactement les signalés) | **Règle A étendue** : la table v4 couvre **exactement** les épisodes dont la trajectoire de base diffère de P3 : les 22 signalés (entrées de la v3, inchangées) **et** les non entièrement conformes en longueur (une entrée par cible : `identifiants` si retrouvée, `non_resolu` sinon) ; revérifiée tout entière au chargement par l'oracle de P3 ; `rejeu_activations_v4.classer_episodes_v4` | Les 89 sont hors de portée de la règle A de la v3 |
| V4-E5 | v3, E8 (a) : table d'empreinte égale à l'empreinte citée par la configuration | **Empreinte non citée d'avance** : la table v4 est construite **dans la session 2**, après la réparation ; la configuration v6 porte `table_tokenisation_sha256` = `construite-en-session` ; le rejeu v4 lit la table au chemin cité (absente du commit lancé, R12, vérifié par le script avant l'installation), exige son sceau, sa version 4, ses formes, puis **revérifie chaque correction par l'empreinte de P3** (comme la v3) ; son empreinte est écrite au résultat (`tokenisation.table_sha256`) et dans le journal de l'instance avant le rejeu. Toute table qui passe ces gardes a, pour chaque épisode retrouvé, les seuls identifiants qui redonnent l'empreinte de P3 (sauf collision de sha256) ; la seule liberté restante, l'ensemble des épisodes `non_resolu`, est fixée par le résultat scellé de la réparation, que la table cite (`resultat_reparation_sha256`) ; **garde de chaîne** (`chaine_table_v4_v1`, cas sains et artefacts, R5 : `tests/test_chaine_table_v4_v1.py`) : avant toute reconstruction du rejeu, `resultat_reparation_sha256` doit égaler le sceau du résultat de la réparation de la même session (même configuration), les entrées « identifiants » des cibles être exactement ses retrouvées et les entrées `non_resolu` exactement ses non retrouvées, sinon arrêt de la session 2 avant le rejeu (étape « chaine » du script, `chaine_table_v4_v1.exiger_chaine`, non un « echec » du rejeu ; rien n'est lu ; artefact : une retrouvée rétrogradée en `non_resolu`) ; **à la réception**, la table est recalculée sur processeur (`chaine_table_v4_v1 … --reception`, par `resolution_graine_lot_v3.construire_table_v4`, même configuration, résultat versé ; commande à l'étape 4) et doit égaler à l'octet la table versée : son empreinte est la valeur, fixée d'avance, d'une fonction scellée de pièces scellées. Construction et rejeu s'enchaînent dans la session 2 sans lecture ni décision humaine ; une troisième session sous texte neuf ne s'impose que si cet enchaînement est rompu (table construite hors de la session 2) | Un seul texte gouverne réparation et rejeu (consigne de Lazar) ; alternative écartée : une troisième session, sous un texte neuf qui citerait l'empreinte (point 3 du rapport de rédaction) |
| V4-E6 | v3, E12 et E11 : module `rejeu_activations_v3`, configuration v5 | Module **`rejeu_activations_v4`** (copie de la v3 dont chaque écart est marqué `# v4` ; contrôle négatif et méthodes de résolution importés de la v3) ; **la commande du manifeste devient `python -m controle_ia.runs_nuit.rejeu_activations_v4`** ; configuration **v6** (v5 sauf la table, V4-E5) ; réparation : module **`resolution_graine_lot_v3`** (copie de `resolution_graine_lot_v2` dont chaque écart est marqué `# v3`), configuration `R1-reparation-v4-config-v2.json` (la v1, `R1-reparation-v4-config-v1.json`, sauf `voie_si_temoin_non_exact` = « lot_fidele » ; la v1 est celle du complément scellé, `1b6f943c…`, sauf `episodes_resolution` vidée et `episodes_resolution_lot` retirée, sans objet ici, plus les clés v4 : table v3 citée, lots témoins 2 et 13, lot 3 d'abord, 89 cibles et 28 lots attendus, capture d'équivalence, voie écrite d'avance) ; garde de chaîne **`chaine_table_v4_v1`** ; gardes de dépense et surveillance **`garde_depense_v4_v1`** ; scripts **`scripts/r1_v4_instance_v2.sh`** et **`scripts/amorce_instance_r1_v4_v2.sh`** ; banc **`scripts/banc_mutations_r1_v4_v2.py`** (empreintes en en-tête) | Noms nouveaux (R12) |
| V4-E7 | v3, E2 et E3 (règle B) | **Règle B inchangée** pour les signalés (sans objet : aucune entrée `non_resolu` dans la v3). Une cible v4 **non retrouvée** reçoit une entrée `non_resolu` ; elle est **déclarée** (`tokenisation.episodes_non_retrouves_v4`, `actions_non_retrouvees_v4`) et garde **exactement le traitement de la v3** (préfixe conforme en `contexte_conforme`, actions jugées par la tolérance) ; elle ne compte pas dans le seuil de la règle B, qui ne l'a jamais comptée | Aucune action ne perd ce que la v3 lui donnait |
| V4-E8 | v3, « Prédiction » : P-R5 « au moins 90 % des notées fidèles (au plus 93 %) » | P-R5 réécrite (section « Prédiction ») : la borne « au plus 93 % » (conformes en longueur, v3) est sans objet ; prédiction de couverture par condition, dans les deux sens | La table v4 rend conformes les actions réparées |
| V4-E9 | v3, étape 2 : échantillon de fidélité parmi les 1 510 actions à trajectoire identique | Même règle (5 par condition, clé « fidelite », même entropie) parmi les éligibles de la v4 (jusqu'à 2 400) : **l'échantillon diffère** de celui de la v3, déclaré | Conséquence de V4-E4 |
| V4-E10 | v3, E10 : 329 tests | **381** (26 fichiers, en-tête ; 381 passés au commit `af1f2f4f` avec le tokeniseur) | Code neuf |
| V4-E11 | v3, E18 : branche `calcul/r1-relance-v3-reel-v1` | Session 1 : **`calcul/r1-v4-temoin-reel-v1`** ; session 2 : **`calcul/r1-v4-reparation-reel-v1`** (le script refuse une branche existante) ; après la session 2, le run de rejeu est versé à l'octet sur `calcul/r1-r2-reel-v1` par un commit neuf, sans rien réécrire (procédure de la v3, branche source remplacée aux deux endroits) | Branches neuves (R12) |
| V4-E12 | v3, E9 et E17 : GO-2026-11-02-27, gardes 600 et 720 min | **GO-2026-11-03-03** ; gardes contre une boucle folle : session 1, plafond de l'amorce 180 min, délai par étape 120 min ; session 2, plafond 2 200 min, délai par étape 2 100 min ; **gardes de dépense** : deux tâches planifiées, posées à la création de chaque instance, indépendantes de la session de pilotage (audit A9 d'A1-v3, § 8) : alerte à 45 USD engagés ou projetés à la vérification suivante, destruction à 57 USD **projetés** à la vérification suivante (donc avant 57 USD engagés) et dès la fin de l'amorce lue au journal, **par l'identifiant de l'instance seulement** (R10 ; aucun signal par numéro de processus : aucun accès au conteneur n'est posé ni éprouvé en mode « args », fait constaté du complément scellé `049f20ba…`, « Aucun signal par numéro de processus dans ce texte ») ; tâche de destruction à heure fixe `T0 + H`, `H = (57 USD − dépenses déjà imputées au GO, sessions et reprises comprises − disque estimé) / prix horaire de l'offre − 15 min`, écrite dans `registres/depenses.md` à la création ; **armement, quatre épreuves R5 (destruction : cas sain et artefact ; vérification horaire : cas sain et artefact) et lecture filtrée des journaux : ceux du complément scellé (C-3, C-4, C-5), seuils 45 et 57 USD au lieu de 30 et 39,5 USD, compte `episodes=k/89`**, consignés avant chaque création ; règles rendues mécaniques par `garde_depense_v4_v1` (`commande_destruction`, `heure_destruction`, `decision_horaire`, `exiger_armement`, `filtrer_journal`, `projection_fin` : fin projetée + 75 min) et éprouvées sur processeur (`epreuves-garde-depense-v4-sortie-v1.txt`, `f2eb1d8fb7498a43067df2fdf77b199630921e42d28612f147d3c3008ff31fbe` : conformes) ; conséquence déclarée : une destruction perd ce qui n'est pas poussé (le script ne pousse qu'à la fin d'une étape) ; devis : `devis-relance-v4-v2.md` (§ 2) | Pire cas borné sous 60 USD (devis v1, § 3, inchangé en v2) |
| V4-E13 | v3, E8 (e) : fiche de réception de conv-audit scellée avant la récupération | **Fiche de réception v4** de conv-audit, scellée **avant toute récupération** des sorties de la session 2 par session-depot (condition de la récupération, **non de la création**) ; session-depot l'apprend par un message de conv-audit qui donne chemin et empreinte, vérifiée | Inchangé dans son principe ; fiche neuve (attentes v4) |
| V4-E14 | v3, E16 : `tokenisation.addendum` = l'addendum v2 (provenance de la table v3) | `tokenisation.addendum` = **`prereg/R1-addendum-relance-v4.md`** (constante du module v4) : le texte qui a construit la table v4 est aussi celui qui gouverne le rejeu ; le manifeste du run porte toujours le texte qui gouverne (`preenregistrement`) | La garde `provenance` de conv-audit doit être mise à jour (« Analyses ») |
| V4-E15 | (code de la v1, `LigneLot.forcee`) | Les lignes approchées (cible en échec, pour garder la forme ; autres cibles non retrouvées dans le repli à une cible) sont remplies d'un **jeton ordinaire**, jamais du remplissage de P3, qui est une fin chez Llama 3 (128001) et arrêterait la ligne avant sa longueur (`resolution_graine_lot_v2.forcee_approchee`, reprise à l'identique dans `resolution_graine_lot_v3.forcee_approchee`, module de la réparation) | Défaut latent de la v1, déclaré ; sans effet sur une ligne exacte |
| V4-E16 | v3, E21 (reprise) | **Reprise unique par session** sur erreur d'infrastructure (clonage, installation, préchargement, carte indisponible, perte de l'instance, poussée refusée), jamais sur une garde, sans fichier de résultat lisible écrit ; branche `-v2` ; même texte, même GO s'il est valide, sous la garde de dépense cumulée (`H` recalculé, V4-E12) ; reprise consignée et dite à conv-audit avant la création. Session 2 : une reprise ne relit rien de la course arrêtée hors de son journal ; les épisodes déjà consignés ne sont pas réutilisés (la réparation repart de zéro, même configuration ; R3 exige une configuration neuve : une reprise relève donc d'un texte neuf si la course arrêtée a écrit un manifeste) | Mots de Lazar (« je ne veux pas de blocage ») ; R3 |

Inchangés : hypothèses H-R1 et H-R2 ; P-R1 à P-R4 ; métrique principale et secondaires, bras, plancher apparié, plis,
intervalles ; seuils (taux de fausse alarme 1 % et 5 %, tolérance de fidélité 0,02 × (1 + |score|), contrôle négatif
18 sur 20, règle de repli gelée, règle des 80 % parmi saboteur ou honnête) ; définition de `fidele` ; couches 7, 15,
23 ; agrégats ; formats de sortie (fichiers, tableaux, noms, formes, types) ; run source et pièces de P3 ; entropie ;
textes des trois analyses scellées de conv-audit (principale, secondaire, par épisode).

## Hypothèse

Inchangée (parent, H-R1). **Hypothèse de travail** : la reconstruction d'un épisode est la tokenisation du texte seul
plus la fin comptée par P3, **corrigée par la table v4** quand la table redonne exactement l'empreinte de trajectoire
de P3 ; avec la table v4, chaque épisode retrouvé est identique à P3 et, comme les 151 de la v3, ses activations
rejouées le sont au bit (attendu, non exigé). **Hypothèse de méthode (H1 du diagnostic)** : le lot fidèle refait le
calcul de la génération de P3 ; le témoin la met à l'épreuve, contre P3 lui-même, avant toute réparation.

## Prédiction chiffrée et signe attendu

Ouvertes dans les deux sens ; probabilités « supposé » (auteur, d'après le diagnostic, § 6.3).

- **P-T (témoin)** : « exact » sur les lots 2 et 13 (accord = 1 exactement sur tous les pas mesurés des deux lots (≈ 16 900 pour le lot 2, diagnostic § 5.2 ; égalités de
  jetons, non de logits : seules les 8 captures du lot 2 sont des égalités au bit, « exact » est une lecture de route,
  non une preuve au bit du calcul en lot), choix contraints
  égaux, **8 empreintes de capture sur 8** égales à celles de P3 pour le lot 2, forme égale), confiance ≈ 0,75 ;
  « non exact » ≈ 0,25 (alors : même voie, lot puis repli, écrite d'avance ; seuls changent durée et coût, devis v2).
- **P-C (couverture par condition, fidèles sur 600)** : témoin exact et 89 retrouvés : **600 / 600** dans chaque
  condition (≈ 0,75) ; quelques non retrouvés (≈ 2 à 5) : **≥ 0,97** par condition (≈ 0,23) ; échec massif de la
  méthode : couverture de la v3 au moins (honnête ≥ 466, saboteur ≥ 427, témoin ≥ 366, mention ≥ 489, diagnostic § 2.3)
  (≤ 0,02). Prédiction **contraire** si une condition finit sous 0,97 ; **réfutée dans le sens de la méthode** si la
  couverture saboteur ou honnête reste sous 0,80 (il faut au pire 11 des 25 épisodes saboteurs et 4 des 18 honnêtes,
  diagnostic § 2.5).
- **P-R5 (instrument ; écart V4-E8)** : au moins 97 % des actions notées fidèles ; trajectoires identiques = 151 +
  retrouvées ; `corrections_verifiees_au_chargement` = 22 + retrouvées ; activations identiques au bit pour chaque
  épisode à trajectoire identique (attendu, rapporté ; aucune garde). P-R5 contraire : réserve d'instrument (v3, E7),
  sans changer aucune classe ; lue sur `tokenisation.part_fideles_parmi_notees` contre 0,97 ; la clé
  `p_r5_au_moins_90_pour_cent` garde son sens de la v3 (90 %, garde « plus de 10 % d'actions non fidèles » de l'analyse
  secondaire, inchangée).
- **Lectures des analyses** : aucune prédiction nouvelle ; les classes possibles sont celles des textes scellés, dans
  les deux sens. **« Confondu » par épisode est une issue possible** de l'analyse par épisode scellée
  (`prereg/analyse-par-episode-v1.md`, `26a3ff72e3a39636d3bdb965971fd1b237a04acc133a31a42f9a695d6d5970a4`, ligne
  « Δ(W − G) borne basse > 0, mention contraire »), lue et rapportée **selon ses critères gelés et sa préséance,
  inchangés** (« la principale reste la lecture principale » ; classes divergentes : « les deux rapportées ensemble ») ;
  ce texte n'ajoute, ne retire ni ne hiérarchise aucune lecture, et n'en estime pas la probabilité (le signe descriptif
  de la v3 est connu, V4-E2 : toute probabilité en serait tirée).
- Durée et coût : devis v2 (central ≈ 6,5 à 8 USD ; si témoin non exact, ≈ 18 USD au milieu, ≈ 36 USD au haut ; pire
  cas borné ≈ 57,2 USD, inchangé).

## Métrique

Inchangée (parent, v3). Mesures nouvelles, **descriptives**, sans seuil de lecture des analyses : par lot témoin, accord,
égalité des choix contraints, captures égales, forme ; par cible, voie (`lot_multi:directe`, `lot_une_cible:…`,
`passe_forcee:…`) et essais ; par lot réparé, captures des actions d'équivalence égales ou différentes (contrôle
intermédiaire) ; par lot réparé, accord des lignes connues forcées et captures, **séparés avant et après la première
action en échec d'une cible** (épreuve sur la carte de l'indépendance des lignes, mesure écrite par `resolution_graine_lot_v3.mesure_independance` dans `lots_rapport[k]["independance_des_lignes"]` du résultat de la réparation, pour l'essai à plusieurs cibles ; non mesurée dans le repli à une cible, déclaré) ; comptes de la table v4 ; non retrouvés v4.

## Seuil

Inchangés (parent, v3). Seuils de l'instrument, nouveaux et gelés : lecture du témoin « exact » = égalités exactes
(accord 1, choix contraints 1, captures toutes égales, forme égale, aucun jeton hors candidats, aucun jeton manquant)
— aucune tolérance ; frontière du repli 272 ; gardes de durée et de dépense (V4-E3, V4-E12), qui ne sont pas des seuils
de lecture.

## Plan d'analyse

**Étape 0 — processeur, avant toute carte (faite pour le code jouet ; à refaire au commit cité)** : essais (section
« Essais ») ; pré-vol sur les vraies pièces de P3 sans modèle 8B, écrit et rejoué
(`docs/notes/runs-r1-r2-r4-v1/relance-v4/prevol-v4/prevol_r1_v4_v1.py`
`85bc760eee37f63b4634d6113afe2af107a28974b0ba051f4f9ddb4229cdb9c8`, sortie `prevol-v4/prevol-r1-v4-sortie-v1.txt`
`e10815f6f21862f5a6b3bd7b8fb6d6fbf9bebda16116a12f38233d4e816058c4` : **0 écart** ; les 151 et 129 ci-après, qui
demandent le tokeniseur, n'y sont pas recalculés, les 89 et 28 y sont recoupés avec la liste du diagnostic ; la garde
`exiger_comptes_attendus` les recalcule sur l'instance avant tout calcul) : 240 épisodes, 151
conformes en longueur, 129 identiques de base, 22 signalés couverts par la table v3, **89 cibles dans 28 lots**, lots 2
et 13 entièrement connus, captures de P3 recalculées (échantillon d'équivalence) égales aux fiches.

**Étape 1 — conditions du lancement**, dans l'ordre : contre-lecture neuve (R2) traitée ; **avant le scellement** :
pré-vol de l'étape 0 écrit et versé (script et sortie empreintés), suite des 26 fichiers rejouée au commit cité avec le
tokeniseur de la révision de P3 (« 381 passed », aucun sauté), banc de mutations rejoué en entier au commit cité,
répétition jouet de bout en bout des deux sessions (amorce et script ; cas sain de la session 2 jusqu'au rejeu ;
artefacts de l'amorce : `PLAFOND_AMORCE_MIN` hors bornes, `SESSION` inconnue, seconde exécution ; témoin arrêté ou de
sceau faux), garde de chaîne de V4-E5 éprouvée (sain, artefact) — **faits sur les fichiers du commit `af1f2f4f`**
(à refaire au commit cité si un fichier change) : 381 passés, aucun sauté (en-tête) ; banc
`scripts/banc_mutations_r1_v4_v2.py`, passe 2 entière sur les essais finaux, 37 mutations tuées sur 37
(`docs/notes/runs-r1-r2-r4-v1/relance-v4/banc-mutations-relance-v4-sortie-v2.txt`
`fe833d20843afd5b6d0815fe70e81b57e5f15deebf3269632c4e3f55fb33622d`) ; répétition jouet des deux sessions
(`repetition-jouet-v4/codes.txt` `95f097cb6b3a1beee7fd0fc8c1302067dc00a9513cb512d240a2c1b797c7b788` ; réception
recalculée égale à l'octet, `repetition-jouet-v4/reception-jouet.txt`
`8f96c339da7da9f540e238a4d62cf97666d46df1af04ee0330ab081cf9778d45` ; surveillance
`repetition-jouet-v4/surveillance-repetition.txt` `3af22472b459b2e5a99a4888b41c31823cf951af159e76a93b8db057cc89d6c2` ;
fichiers finaux sauf `test_chaine_table_v4_v1.py` et le banc, renforcés après et non exécutés par elle, rapport des
ajouts, réserve 4) ; épreuves des gardes de dépense (`epreuves-garde-depense-v4-sortie-v1.txt`
`f2eb1d8fb7498a43067df2fdf77b199630921e42d28612f147d3c3008ff31fbe` : sept épreuves conformes) ; scellement de ce texte et des
deux configurations, dans un commit poussé ; contrôles d'avant l'installation rejoués au commit de scellement (copie) ;
concordance d'un lecteur neuf de conv-audit sur la version scellée (chemin et empreinte consignés) ; commande exacte de
conv-audit ; GO valide le jour même ; dépenses déjà imputées relevées ; offre conforme aux filtres de la v3, sinon nœud.

**Étape 2 — session 1, témoin** (`scripts/amorce_instance_r1_v4_v2.sh`, `SESSION=temoin`) : gardes d'avant
l'installation (texte et cinq chemins cités une fois, sceaux, table v3 de version 3 et citée par la configuration de la
réparation) ; branche neuve poussée ; préchargement ; 381 essais ; étape « temoin » de `resolution_graine_lot_v3`
(gardes avant le manifeste : configuration, texte cité, entropie, commit, pièces, noyau de P3, table v3, R3) ; lots 2 et
13 rejoués en entier ; **lecture gelée** écrite au résultat (`lecture`, `voie_ecrite_d_avance`) ; un lot témoin sans
identifiants connus, ou sans pas mesuré, arrête. Sortie scellée, poussée ; instance détruite par son identifiant. Le
run du témoin est versé à l'octet sur la branche de ce texte par un commit neuf (seule différence avec le commit de
scellement : `runs/<run>/` et `diag/<run>/`, hors de l'arbre gelé).

**Étape 3 — session 2, réparation, table v4, rejeu** (`SESSION=reparation`, `TEMOIN_RUN=<run>`) : gardes d'avant
l'installation, plus : résultat du témoin, son sceau et son manifeste présents au commit, sans `arret.json` ; table v4
absente du commit ; configuration du rejeu en `construite-en-session`. Étapes, chacune arrêtant la suite si elle
s'arrête :
- « reparation » : lecture relue dans le témoin scellé (même configuration, même code ; « exact » ou « non exact », sinon arrêt) ; elle ne choisit pas la voie, toujours celle du lot (toute autre voie arrête) ; cibles et lots recalculés égaux à
  89 et 28 (sinon arrêt avant tout calcul) ; **voie du lot** : lot 3 d'abord, puis les autres lots dans l'ordre ; dans
  chaque lot, essai à plusieurs cibles, puis, par cible non retrouvée, lot fidèle à une cible avec repli écrit (272),
  puis passe forcée du cœur (272) ; **une seule voie** (« lot_fidele », que le témoin lise
  « exact » ou « non exact » ; « sans mesure » : arrêt ; `resolution_graine_lot_v3.voie_de_reparation`) ; chaque
  épisode consigné aussitôt ; arbitre unique, l'empreinte de P3 ;
- « table-v4 » (processeur) : table v3 inchangée plus une entrée par cible ; chaque correction revérifiée ; écrite et
  scellée au chemin cité ; empreinte au journal ;
- « chaine » (processeur, `chaine_table_v4_v1.exiger_chaine`) : la table suit exactement le résultat scellé de la
  réparation (V4-E5) ; sinon arrêt avant le rejeu, rien n'est lu ; journal « chaîne de la table v4 : conforme » ;
- « r1-rejeu » : `rejeu_activations_v4`, configuration v6 ; tout le reste comme la v3 (étape 2 de la v3).

**Étape 4 — versement et réception** : après la destruction, et seulement une fois scellée la **fiche de réception v4**
de conv-audit, le run de rejeu (et ceux de la réparation et du témoin, avec la table v4) est récupéré et versé à
l'octet sur `calcul/r1-r2-reel-v1` (V4-E11). **Attentes de réception** (course qui va au bout) : manifeste du rejeu :
`commande` = `python -m controle_ia.runs_nuit.rejeu_activations_v4`, `preenregistrement.chemin` =
`prereg/R1-addendum-relance-v4.md`, `preenregistrement.sha256` = empreinte de ce texte scellé ; résultat :
`verdict_fidelite` « conforme », `tokenisation.version_table` = 4, `tokenisation.table_sha256` = empreinte du sceau de
`prereg/R1-table-tokenisation-v4.json` versé avec le run, `tokenisation.table_empreinte_citee` = faux,
`tokenisation.non_conformes` = 89, `tokenisation.signales` = 22, `tokenisation.addendum` =
`prereg/R1-addendum-relance-v4.md` ; trois fichiers `.npz` aux noms, tableaux, formes et types du parent ; résultats du témoin et de la réparation :
`diag/<run>/resolution-graine-lot-v3-temoin.json` et `diag/<run>/resolution-graine-lot-v3-reparation.json`.
**Recalcul de réception** (processeur, V4-E5) : `python -m controle_ia.runs_nuit.chaine_table_v4_v1 --config
prereg/R1-reparation-v4-config-v2.json --reparation diag/<run>/resolution-graine-lot-v3-reparation.json --table
prereg/R1-table-tokenisation-v4.json --reception --tokeniseur <dossier du tokeniseur de la révision de P3>` : chaîne
conforme et table recalculée égale à l'octet à la table versée, sinon la table n'est pas reçue.

**Analyses (inchangées).** Les textes des analyses principale, secondaire et par épisode de conv-audit ne bougent pas.
Leurs gardes de réception, à mettre à jour **par conv-audit, de son côté**, devront exiger : **`texte`** — le texte qui
gouverne, lu dans `preenregistrement` du manifeste, est ce texte scellé (chemin et empreinte), non l'addendum v3 ;
**`table-comparee`** — `tokenisation.table_sha256` est comparée à l'empreinte du sceau de la table v4 versée avec le run
**et** à celle que la table cite comme résultat de réparation (`resultat_reparation_sha256` égal au sceau du résultat de
la réparation versé) : l'empreinte n'est plus connue d'avance (V4-E5), elle est fixée par la chaîne scellée ;
**`provenance`** — `tokenisation.addendum` = `prereg/R1-addendum-relance-v4.md` à l'identique (V4-E14), et commande
`rejeu_activations_v4`.

## Critères de lecture gelés

Ceux de la v3 (et du parent), plus :

| Issue observée | Lecture |
|---|---|
| Témoin « non exact » | Même voie, lot puis repli (écrite d'avance) ; la lecture du témoin est rapportée telle quelle, avec la durée et le coût (devis v2 : ≈ 18 USD au milieu, au-delà de la fourchette de 5 à 12 USD que cite le GO, sous son plafond) ; aucune autre conséquence |
| Témoin arrêté (lot sans identifiants connus, aucun pas mesuré, garde) | Session 2 non lancée ; nœud porté à Lazar |
| Cibles ou lots recalculés ≠ 89 ou 28 | Arrêt avant tout calcul de la réparation ; audit (R4) |
| Table v4 non applicable (version autre que 4, manquant ou en trop, correction qui ne redonne pas l'empreinte de P3, sceau absent) | Rejeu non validé : rien n'est lu (« echec ») |
| Couverture sous 0,80 parmi saboteur ou honnête après la v4 | « Non concluant (rejeu partiel) » comme en v3, publié tel quel ; **on s'arrête** : aucune v5 sans témoin positif en échec expliqué (rapport Fable, § 6) |
| « Confondu » par épisode | Lu selon l'analyse par épisode scellée (`26a3ff72…`), inchangée, préséance comprise (la principale reste la lecture principale) ; aucune lecture ajoutée par ce texte |
| Indépendance des lignes contredite sur la carte (dans un lot réparé, une ligne connue perd l'accord ou une capture diffère après le premier échec d'une cible, non avant) | Réserve d'instrument sur cette hypothèse, rapportée par lot ; aucune entrée de table ni aucune classe ne change (l'empreinte de P3 reste le seul arbitre) ; le repli écrit continue ; aucune course de plus sous ce texte |
| Lecture « exact » du témoin contredite pendant la réparation (ligne connue en désaccord dans un lot sans cible en échec) | Même réserve, sur la lecture du témoin ; la voie écrite d'avance ne change pas en cours de route |
| Résultat suspect de propreté, dans un sens ou l'autre | Même audit (R4) |

## Liste d'arrêt

Celle de la v3, avec les ajouts : **lancement** — pas de création sans ce texte et les deux configurations scellés, la
contre-lecture traitée, la concordance de conv-audit consignée, la commande exacte de conv-audit, `GO_ID=GO-2026-11-03-03`
valide le jour même (pas après le 17 novembre sans GO nouveau), une offre conforme, les deux tâches planifiées de dépense
posées ; **amorce** (code 1) : `SESSION` autre que `temoin` ou `reparation`, `PLAFOND_AMORCE_MIN` hors de 1 à 9999 ;
**script, avant tout clonage** (code 2) : `DELAI_ETAPE_MIN` hors de 1 à 9999, session 2 sans `TEMOIN_RUN` valide ;
**script, avant l'installation** (code 2) : texte ou un des cinq chemins absent, cité plusieurs fois ou de sceau faux ;
table v3 de version autre que 3 ou d'empreinte autre que celle de la configuration ; configuration du rejeu sans
`construite-en-session` ; table v4 présente au commit ; session 2 : témoin absent, non scellé, sans manifeste ou arrêté ;
branche existante ; poussée initiale refusée ; **tests** : dernière ligne autre que « 381 passed » ; **module** : gardes
avant le manifeste (configuration, texte cité, entropie, commit, pièces, noyau, table v3, témoin, R3) ; arrêts consignés
(`arret.json`, épisodes consignés cités) ; **chaîne** (session 2, entre « table-v4 » et le rejeu) : `chaine_table_v4_v1`
en arrêt, rien n'est lu ; **dépense** : 57 USD projetés à la vérification suivante sous le GO, ou fin de l'amorce lue au journal (destruction par l'identifiant, V4-E12 ; `garde_depense_v4_v1.decision_horaire`).
Dans tous les cas : ce qui existe est poussé ; instance détruite par son identifiant (R10), consignée.

## Coût et GO

Devis : `docs/notes/runs-r1-r2-r4-v1/relance-v4/devis-relance-v4-v2.md` — central ≈ 6,5 à 8 USD, ≈ 18 USD au milieu
(≈ 36 USD au haut) si le témoin est non exact, pire cas borné ≈ 57,2 USD < 60 USD (GO-2026-11-03-03). Hôte : instances Vast.ai,
A100-SXM4-80GB, filtres de la v3 ; session de pilotage : session-depot ; gardes de dépense : V4-E12.

**Commande de création** (session-depot, comme la v3 ; `COMMIT_SCELLEMENT` = commit de scellement de ce texte pour la
session 1 ; commit du versement du témoin pour la session 2) :

```
B64=$(git show "$COMMIT:scripts/amorce_instance_r1_v4_v2.sh" | base64 -w0)
GO_ID=GO-2026-11-03-03 $VB/vastai create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label r1-v4-<session> \
    --env "-e COMMIT=$COMMIT -e SESSION=<temoin|reparation> [-e TEMOIN_RUN=<run>] -e BRANCHE=calcul/r1-v4-<session>-reel-v1 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e PLAFOND_AMORCE_MIN=<180|2200> -e DELAI_ETAPE_MIN=<120|2100> -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64 | base64 -d > /root/amorce.sh && bash /root/amorce.sh"
```

**Surveillance** (remplace celle de la v3, dont les valeurs ne valent pas ici ; lecture filtrée de V4-E12) : valeurs
attendues au journal, session 1 : « AMORCE … plafond de l'amorce 180 min », « DELAI_ETAPE_MIN=120 », « tests : 381
passed », lignes `etape=temoin` des lots 2 et 13, `etape=fin` ; session 2 : « plafond de l'amorce 2200 min »,
« DELAI_ETAPE_MIN=2100 », « tests : 381 passed », `etape=reparation … cibles=89 lots=28`, `episodes=k/89`, « table v4 :
prereg/R1-table-tokenisation-v4.json (<empreinte>) », « chaîne de la table v4 : conforme » (vue filtrée : « chaîne de la
table v4 »), puis les jalons du rejeu de la v3, table de version 4. Une autre
valeur de plafond ou de délai lue au journal fait détruire l'instance par son identifiant (R10), sans lecture. Règles et
filtre : `garde_depense_v4_v1` (`filtrer_journal`, puis `verifier_surveillance`, en ligne de commande `surveiller
--session <temoin|reparation> --tests 381` : son défaut, 358, ferait détruire une instance saine ; plafond, délai,
tests, `cibles=89 lots=28` et version 4 de la table ; une autre valeur lue rend « detruire »).

## Essais (processeur, sans dépense, sans téléchargement)

Détail et sorties : `docs/notes/runs-r1-r2-r4-v1/relance-v4/rapport-redaction-relance-v4-v1.md`. En bref :
`tests/test_resolution_graine_lot_v2.py` (13 essais : logits et captures au bit, témoin exact et trois artefacts,
plusieurs cibles égales à une cible, cible en échec seule (forme gardée, action sans fin et échéance dépassée : remplissage ordinaire), cibles plus courtes que le lot et contrôle du
texte décodé, cibles hors table v3, gardes, captures recalculées (échantillon faux refusé), bouts en bout jouets témoin exact → lot fidèle et
témoin non exact → passe forcée (règle de la v2 ; en v3, lot puis repli : `tests/test_resolution_graine_lot_v3.py`), table v4 et ses refus) ; `tests/test_rejeu_activations_v4.py` (3 essais : règles A et B,
configuration, rejeu v4 sain en session et cité, comparé à la v3, et ses artefacts) : 16 passés, avec les fichiers
voisins 49 passés et 18 sautés (sans tokeniseur ; `essais-relance-v4-sortie-v1.txt`) ; banc de mutations
`scripts/banc_mutations_r1_v4_v1.py` : 15 mutations sur 15 tuées après renforcement des essais, toutes les passes
rapportées (`banc-mutations-relance-v4-sortie-v1.txt`) ; gardes d'avant l'installation du script : un cas sain, huit
artefacts arrêtés en code 2 (`essais-gardes-scripts-v4-sortie-v1.txt`) ; suite de l'instance avec le tokeniseur :
381 passés, 0 sauté, au commit `af1f2f4f` (en-tête). Ajouts I1 à I5 : détail dans le rapport des ajouts
(`rapport-ajouts-relance-v4-v1.md`, `0d8fd1827f58d091ac0405c4627c0b9408b61f55eb348102b4c8fed4d3f25efa`, §§ 2, 3
et 7) ; sans tokeniseur, 26 fichiers : 363 passés, 18 sautés, 0 en échec (`essais-ajouts-relance-v4-sortie-v1.txt`,
`98b53bd4e4933d45990de845f12e0ab8166d259af9375888651e634fd075191c`) ; pré-vol, banc v2, répétition et épreuves :
étapes 0 et 1.

## Contre-lecture

Faite (R2), deux fois, par des sous-agents neufs, auteurs d'aucune pièce : (1) sur le brouillon 1, contre-lecture complète
`docs/notes/runs-r1-r2-r4-v1/relance-v4-contre-lecture-v1/contre-lecture-relance-v4-v1.md` (`e224ae8a…`), 15 couples
appliqués au brouillon 2 ; (2) sur le delta des brouillons 2 et 3,
`docs/notes/runs-r1-r2-r4-v1/relance-v4-contre-lecture-v2/contre-lecture-delta-brouillon3-v1.md`
(`ef0604abe5f0353a81224ae20c1f49a7b1d7587df427cce0b84690cac908ac89`), verdict « scellable après couples » ; ses 19 couples
(`couples-contre-lecture-delta-brouillon3-v1.json`, `3cddb305971dc822db5cb4a5931ecd6b19995e7202d26111d8acb67a55995742`)
appliqués dans l'ordre par script, chaque « ancien » unique au moment de son application. Les deux textes sont au dépôt
de travail, branche `main`.

Réserve C32 de la seconde contre-lecture (le module `garde_depense_v4_v1` attend 358 essais par défaut) : correction de
code **non retenue** (décision de routine de conv-audit, `registres/decisions.md`, R-1473). Raison : la surveillance
n'est appelée que par la session de pilotage, jamais par les deux tâches planifiées de dépense (leurs prompts ne portent
aucun compte d'essais) ; la commande exacte, avec `--tests 381`, est écrite ici (section des journaux attendus) et dans
l'ordre de la fille ; une correction imposerait de rejouer les 381 essais avec le tokeniseur, le banc, les épreuves et la
répétition jouet, puis une contre-lecture neuve. Le risque qui reste est une erreur d'opérateur, dont l'effet serait la
destruction d'une instance saine (perte de la dépense engagée, jamais un résultat faux) ; il est déclaré ici.

---
Brouillon 2 (4 novembre 2026, instance fusionnée) : brouillon 1 (`a16d555d…`) + les 15 couples de la contre-lecture R2 (`contre-lecture-relance-v4-v1.md`, `e224ae8a…` ; couples `f2cea13e…`), appliqués dans l'ordre par script, chaque « ancien » unique au moment de son application ; verdict : scellable après couples (B1 levé par les couples 1 et 2). Avant scellement : quatre ajouts de code et les épreuves de I4 nommés par la contre-lecture. Arbitrage M de la contre-lecture (témoin non exact) : « lot puis repli », retenu par la mère (meilleure couverture, ≈ 2,5 h de plus, sous le plafond).

---
Scellement (4 novembre 2026, vers 08:17 UTC, `date -u`, conv-audit fusionnée avec session-depot) : brouillon 3
(`f24e416f…`, commit `8bce1bc1`) + les 19 couples de la contre-lecture du delta + le marqueur du commit du code d'analyse
rempli + la section « Contre-lecture » écrite ; aucun fichier de code ni de configuration changé depuis `af1f2f4f`
(`git diff --stat af1f2f4f` : seuls le brouillon 3 et son rapport, avec leurs sceaux) ; empreintes de l'en-tête
revérifiées au commit de scellement.
