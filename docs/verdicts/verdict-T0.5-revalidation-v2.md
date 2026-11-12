# Verdict — T0.5 — revalidation courte de l'équivalence sur le domaine du pilote — v2 (version finale)

Contre-vérification : deux sceptiques neufs, non réfuté ; corrections mineures intégrées par un sous-agent neuf.

- **Auteur** : sous-agent neuf (R13), qui n'a écrit ni le préenregistrement ni l'analyse ; il applique les critères gelés avec le code de lecture cité, en lecture seule (aucune écriture dans les dépôts, aucun commit, aucune commande Vast.ai).
- **Sceptiques** : deux sceptiques neufs et indépendants ont recalculé le verdict depuis les résultats scellés (95 et 72 constats, 0 écart) et ne l'ont pas réfuté. Leurs points, tous mineurs, sans effet sur la règle ni sur le verdict, sont dans `resultats-workflow.json` (section 10).
- **Corrections** : un sous-agent neuf, distinct de l'auteur et des deux sceptiques, ni auteur du préenregistrement ni de l'analyse, a intégré ces corrections, chacune vérifiée dans les fichiers (liste en section 9). Le verdict, la règle appliquée et les valeurs sont inchangés.
- **Date** : brouillon du 2026-10-12 00:05 UTC (`verdict-T0.5-revalidation-v2-brouillon.md`, sha256 `ae574fe0e6bd4f57016ceb97f983b00b8239f36e20698147cbb642c76b899249`) ; version finale du 2026-10-12 00:51 UTC. Non scellée : à sceller, puis à soumettre à Lazar pour GO (R13).
- **Préenregistrement appliqué** : `prereg/T0.5-revalidation-equivalence-pilote-v2.md`, sha256 `4ff2b07548e90fc515fe8944a789bf44267be6e239dee02d2b479e9c701dcc61` ; commit de scellement `8f74adaa4b7912f87c9d22ec1594a12910d1930a` ; code cité `6ec7434119781a3abebac789174101b9ed6ae087`.
- **Run** : `20261011-225701-t05-revalidation-reel` ; clone propre à la tête de la branche `calcul/t05-revalidation-reel-v2`, commit `5b428608575fea8db57e90f47c096229e21074b4`.
- **Règle D-20** : aucun champ de texte des fiches (actions, ensembles, énoncés) n'a été ouvert ni affiché, ni par l'auteur, ni par les sceptiques, ni par le correcteur ; seuls des nombres, des drapeaux, des empreintes et des identifiants d'épisode ont été lus. Les longueurs d'énoncés citées viennent de `resume.json` et du recalcul par `taches_d_entrainement`, sans affichage de texte.

Sauf mention contraire, les résultats sont sous `diag/20261011-225701-t05-revalidation-reel/` ; leurs empreintes complètes sont à la section 6. Les numéros de ligne du code renvoient au commit du run `5b42860`, où `src/` est identique à `6ec7434` ; ceux du préenregistrement, à sa version scellée (`4ff2b075…`).

## 1. Verdict

**Nœud : aucun noyau n'est retenu pour le pilote ; rien ne tourne.**
Le bras « defaut » est non conforme par le seul critère R8 : la durée projetée des épisodes du pilote vaut 8 089,62 s, pour un plafond gelé de 7 800 s. Tous ses autres critères et son audit sont conformes, R1 compris avec marge (0,1354 ≤ 0,15).
Le bras « math » est non conforme : une panne de mémoire a été signalée pendant le jeu du bras (épisodes, rejeu du lot 0 ou passes du repère en demi-précision), et aucune mesure n'a été écrite. Par inférence, la panne est très probablement survenue pendant le premier passage de ses épisodes (section 8, limite 3). Aucun des deux cas de « proposition prête » ne s'applique.

## 2. Règle appliquée

**Règle de choix gelée** (section « Règle de choix gelée » ; `choisir_noyau`) :
1. Premier bras conforme avec marge, dans l'ordre « defaut » puis « math » : **aucun**. « defaut » : `conforme` faux (R8) ; « math » : `conforme` faux (panne).
2. Sinon, nœud ; proposition prête dans deux cas.
   - « un bras conforme sans marge (0,15 < R1 ≤ 0,2) » : **ne s'applique pas**. Aucun bras n'est conforme, et le R1 de « defaut » (0,1354) est d'ailleurs dans la marge.
   - « un bras qui ne manque que le contrôle négatif de l'action entière, sa garde restreinte étant conforme » : **ne s'applique pas**. « defaut » a un contrôle négatif conforme (160 sur 160) et manque R8 ; son drapeau `aveugle_action_entiere_seulement` est faux (`lecture-defaut.json` → `resultat.lecture.aveugle_action_entiere_seulement`). « math » est en panne.
   - Le code de lecture rend la même issue : `choisir_noyau` → (aucun noyau, aucune proposition) ; `resume.json` → `resultat.noyau_retenu` = null, `resultat.proposition_au_noeud` = null, `resultat.noeud` = true.

**Lignes de la table des critères gelés qui s'appliquent** (texte gelé, mot pour mot) :
- « aucun bras conforme avec marge | **nœud** : rien ne tourne ; proposition à Lazar, prête si un bras est conforme sans marge ou ne manque que le contrôle négatif de l'action entière (règle de choix) ; sinon, options à proposer (seuil refondé sur le repère du domaine, autre carte, autre lot : chacun un domaine nouveau, à revalider) »
- Bras « math » : « panne de mémoire signalée dans un bras, y compris pendant son repère ou sa phase « chemin » (W-2) | consignée ; ce bras est non conforme ; la règle s'applique à l'autre »
- « énoncés de la revalidation plus courts que le plus long du pilote | réserve (domaine partiellement couvert) »

**Ce que prévoit le texte gelé** quand aucune proposition n'est prête : « sinon, options à proposer (seuil refondé sur le repère du domaine, autre carte, autre lot : chacun un domaine nouveau, à revalider) ». Ce verdict n'en propose ni n'en choisit aucune : la résolution du nœud revient à Lazar. La formule gelée de `duree_max_s` du pilote n'est pas appliquée, puisqu'aucun noyau n'est retenu.

**Lignes qui ne s'appliquent pas** :
- **Run arrêté** : ne s'applique pas. Il n'y a pas d'`arret.json` pour ce run ; le résumé est écrit et l'instance a consigné « run terminé » à 23:44:09 UTC (`traces/t05-20261011-234411-9q7N/journal.txt`).
- **R2 ou R5 non concluant** : ne s'applique pas ; les deux sont conformes pour « defaut ».
- **Deux bras « contraire » en R2** : ne s'applique pas.
- **Audit en défaut** : ne s'applique pas.
- **Un bras qui ne manque que l'audit** : ne s'applique pas.
- **ρ > 3 au noyau « math »** : sans objet, le bras « math » n'a pas été mesuré.
- **Écarts tous nuls** : ne s'applique pas ; aucun écart nul sur 36 375 jetons de zone générée, à chaque couche.
- **Part des actions à zone générée sous 1 % > 0,2 dans le bras retenu** : sans objet, aucun bras n'est retenu.

## 3. Tableau par bras

### Bras « defaut »

Carte `NVIDIA A100-SXM4-80GB` (`resume.json` → `resultat.carte`). Noyaux permis : flash, mémoire efficace, cuDNN et « math » ; réduction en demi-précision non permise dans « math » (`mesures-defaut.json` → `resultat.noyaux_permis`, dont `reduction_demi_dans_math` = faux).

| critère | grandeur (fichier → clé) | valeur | seuil gelé | conforme |
|---|---|---|---|---|
| R1, garde saine | `mesures-defaut.json` → `resultat.mesures.q99_max` | 0,13539323886582585 | ≤ 0,2 | oui |
| R1, marge | même clé | 0,13539323886582585 | ≤ 0,15 | oui |
| R2, contrôle négatif de l'action entière (99e centile) | `mesures-defaut.json` → `resultat.controle_negatif` (`comparables`, `passent`, `fraction`, `min_des_maxima`) | 160 comparables, 160 passent, fraction 1,0, aucune action courte ; plus petit 99e centile décalé : 0,8836 | ≥ 95 % des comparables, au moins 10 comparables | oui (« conforme ») |
| R3, repère | `lecture-defaut.json` → `resultat.repere.{7,15,23}.q99` | q99 : 0,03251 / 0,08003 / 0,08761, soit 2 × q99 = 0,0650 / 0,1601 / 0,1752 (couches 7 / 15 / 23 ; 9 714 jetons par couche) | 2 × q99 ≤ 0,2 à chaque couche | oui |
| R4, rejeu du lot 0 | `mesures-defaut.json` → `resultat.rejeu_identique` | vrai | identité au bit près | oui |
| R5, domaine | `mesures-defaut.json` → `resultat.mesures` (`actions_comparees`, `actions_remplies`, `contexte_max`, `contexte_max_joue`) | 160 ; 140 ; 4 752 ; 4 752 | ≥ 40 ; ≥ 1 ; ≥ 0,9 × 4 752 = 4 276,8 | oui |
| R6, chemin (simple précision, noyau par défaut, lot 0, T = 5) | `lecture-defaut.json` → `resultat.chemin.lecture` (`C1_ecart_max`, `C2_vus`, `C2_comparables`, `C3`) et `resultat.chemin.controle_negatif` | C1 : 3,0496e-4 ; C2 : 40 vus sur 40 ; C3 : conforme (40 sur 40, plus petit maximum décalé 1,185) | C1 ≤ 3e-3 ; C2 ≥ 95 %, au moins 10 ; C3 conforme | oui |
| R7, mémoire | `mesures-defaut.json` → `resultat.memoire_pic_gio` | 24,02 Gio | ≤ 70 Gio | oui |
| **R8, durée projetée des épisodes du pilote** | `mesures-defaut.json` → `resultat.duree_projetee_episodes_pilote_s` | **8 089,6213 s** = (665,8512 + 8,2839) × 192 / 16 (`resultat.chrono.generation_s`, `resultat.chrono.passe_unique_s`) | ≤ 7 800 s | **non** (dépassement de 289,62 s, soit 3,71 %) |
| Audit, P9 | `lecture-defaut.json` → `resultat.audit.nuls_zone_generee`, `resultat.audit.jetons_zone_generee` | 0 écart nul sur 36 375 jetons, à chaque couche | au moins un écart non nul par couche | oui |
| Audit, sondes | `lecture-defaut.json` → `resultat.audit.sondes_conformes` | vrai (160 actions sur 160 : tableaux distincts, perturbation d'une unité au dernier rang vue) | toutes conformes | oui |
| Audit, ρ | `lecture-defaut.json` → `resultat.audit.rho` | 1,139 / 1,403 / 1,545 (couches 7 / 15 / 23) | ≤ 3 (au-dessus : non conforme au noyau par défaut) | oui |
| Garde restreinte à la zone générée (mesure secondaire) | `lecture-defaut.json` → `resultat.zone_generee` | 99e centile maximal 0,1699 ; contrôle négatif 160 sur 160 ; part sous 1 % : 0,0 | ≤ 0,2 ; ≥ 95 %, au moins 10 | conforme (`resultat.lecture.garde_zone_generee_conforme` vrai) |
| **Bras** | `lecture-defaut.json` → `resultat.lecture.conforme`, `resultat.lecture.conforme_avec_marge` | faux ; faux | R1 à R8 et audit ; marge R1 ≤ 0,15 | **non conforme** |

### Bras « math »

| critère | grandeur (fichier → clé) | valeur | seuil gelé | conforme |
|---|---|---|---|---|
| Panne de mémoire | `lecture-math.json` → `resultat.lecture.panne` | « mémoire : CUDA out of memory. Tried to allocate 6.06 GiB. GPU 0 has a total capacity of 79.44 GiB of which 2.94 GiB is free. […] 68.64 GiB is allocated by PyTorch, and 7.33 GiB is reserved by PyTorch but unallocated. […] » | table : panne de mémoire signalée, bras non conforme | non |
| R1 à R8, audit | aucun fichier | non mesurés. La panne a été levée pendant le jeu du bras, dans `_jouer_bras` (appelée l. 515 de `revalider_pilote_a.py` : épisodes, rejeu du lot 0 ou passes du repère en demi-précision), et rattrapée l. 516, dans `_executer_apres_manifeste`, avec le préfixe « mémoire : » (l. 519), avant toute écriture : il n'y a ni `episodes-math.json` ni `mesures-math.json`, et `resume.json` → `resultat.bras` ne contient que « defaut ». Par inférence, la localisation la plus probable est le premier passage des épisodes, à un préremplissage d'environ 5 040 jetons au lot de 8 (section 8, limite 3). | — | non lus |
| Pic de mémoire et longueur remplie maximale (W-6) | `resume.json` → `resultat.bras`, `resultat.lectures.math` | absents : `resultat.bras` ne contient que « defaut » ; `resultat.lectures.math` ne porte que `conforme`, `conforme_avec_marge` et `panne` | reportés au résumé pour chaque bras lu (texte gelé, l. 97) | écart entre le texte et le code, sans effet sur la règle (section 8, limite 3) |
| **Bras** | `lecture-math.json` → `resultat.lecture.conforme`, `resultat.lecture.conforme_avec_marge` | faux ; faux | — | **non conforme** |

## 4. Recalcul

**Méthode.** Le recalcul part des résultats scellés et appelle le code cité, importé depuis `src/` du clone (`PYTHONPATH=src`, interpréteur `/home/user/controle-ia/.venv/bin/python`, sans écriture de code compilé). Fonctions appelées :
- module `controle_ia.manifeste` : `verifier_resultat`, `lire_manifeste`, `config_canonique`, `graines` ;
- module de lecture : `exiger_citations`, `taches_d_entrainement`, `domaine_et_garde`, `garde_zone_generee`, `plus_longues_transcriptions`, `audit_symetrie`, `lire_chemin`, `duree_projetee_pilote`, `lire_bras`, `choisir_noyau` ;
- `controle_ia.harnais.episode.bilan_controle_negatif`.

Fichiers de travail (hors dépôt) :
- `verdict-revalidation-v2/recalcul_verdict.py` (`f2b843d8c5049d947308e6068a19b90e5709d5b0b69edfaf9192ba1526eba38f`) ;
- journal `recalcul-journal.txt` (`e44ffb4852a4efcd6ced2bbfd357e60907d78784c6692c941b0c1fced55b053a`) ;
- sortie `recalcul-sortie.json` (`e36b796f927b93baf7f1bdccd05f9013a524bdd71af74e3550a0f78511f470a0`) ;
- exploration de structure sans texte `schema_fiches.py` (`70cae427a4dc813e912a6f7db76bc2417e3b215a73004daaa84c6da63f87b2eb`).

**Résultat : 75 constats, 0 écart.** Les valeurs recalculées sont égales, à l'identique (flottants égaux, drapeaux et dictionnaires égaux), à celles de `resume.json`, `lecture-defaut.json`, `lecture-math.json`, `mesures-defaut.json` et de `run.json` de l'instance. Les deux sceptiques, chacun par son propre code, arrivent au même résultat (95 et 72 constats, 0 écart ; section 10).

**Sceaux et chaîne de provenance**
- `verifier_resultat` passe pour les six résultats : chaque résultat est intact, son manifeste est intact et le rattachement par empreinte est vérifié (`manifeste_sha256` = `06ee7ed9…`).
- `lire_manifeste` passe : l'empreinte de la configuration du manifeste est cohérente.
- La vérification de l'arbre scellé du clone (`verifier-arbre .`) donne « arbre intact ».
- Les empreintes de lancement (`docs/sha256sums-lancement-v2.txt`) sont conformes.

**Chaîne, du GO à la fusion sur `main`** (dépôt de travail ; empreintes complètes à la section 6)
- **GO de Lazar sur N-018** : GO-2026-10-11-01, option (a) : version 2 du préenregistrement, « scellée puis lancée selon le plan v7 ; la dépense relève de GO-2026-10-04-08 » (`registres/go.md`, l. 23). Le GO est consigné au commit `cd02b9a` (22:28:59 UTC), avant le scellement du préenregistrement au commit `8f74ada` (22:31:50 UTC).
- **GO de calcul** : GO-2026-10-04-08, devis de la phase 0, plafond de 150 USD (`registres/go.md`, l. 16). La garde de calcul l'a accepté avant la dépense : « garde de calcul : registres/go.md de S lisible, GO-2026-10-04-08 accepté », puis « CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES » (`traces/t05-revalidation-v2-20261011-2246/controles.txt`).
- **Lancement** : `traces/t05-revalidation-v2-20261011-2246/lancement.txt` : offre 49506597 (A100 SXM4, 1,08 USD l'heure, processeur AMD EPYC 7513 ; `offre.json` du même dossier), instance **55458787**, création 1791758763, soit 2026-10-11 22:46:03 UTC ; commit `8f74ada`, préenregistrement v2, branche `calcul/t05-revalidation-reel-v2`, « go N-018 GO-2026-10-11-01 ». Versé au commit `5a8a79a` (22:49:47 UTC).
- **Contrôle à 5 minutes** : `journal-5min.txt` du même dossier : amorce à 22:46:48 UTC, début à 22:47:01, préenregistrement lu (670 tests attendus), branche de résultats poussée à 22:47:15, carte A100-SXM4-80GB, torch 2.14.1+cu130 (commit `5a8a79a`).
- **Surveillance** : `surveillance/etats.txt` relève l'état de l'instance toutes les deux minutes environ, de 22:46:13 à 23:44:39 UTC (« exited » au dernier relevé) ; `surveillance/sortie-surveillance.txt` : « FIN : AMORCE 2026-10-11T23:44:12Z : fin, code 0 ».
- **Absence de second run** : `surveillance/journal-dernier.txt` montre treize relances de l'amorce par le conteneur entre 23:44:15 et 23:44:40 UTC, toutes refusées (« dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve ») ; ses seules lignes « run » sont celles du run `20261011-225701-t05-revalidation-reel`. Un seul dossier de run de cette revalidation existe sous `runs/` et sous `diag/`.
- **Arrêt par identifiant** : `registres/arrets.md`, l. 17 : `vastai stop instance 55458787`, 23:49:30 UTC ; état relu « exited stopped » à 23:51 UTC. Dépense consignée dans `registres/depenses.md`, l. 52 : 1,06 heure de marche (22:46:03 → 23:49:30), environ 1,14 USD, cumul de la phase 0 au plus environ 41,1 USD sur 150 (commit `d0e64af`).
- **Fusion sur `main`** : commit de fusion `ba0004df39814d1efb7dcb82e372d460336fb6b6` (23:58:12 UTC), de parents `1f53a08` et `5b42860`. Lus par `git ls-remote` le 2026-10-12 : le `main` distant pointe sur `ba0004d`, la branche distante `calcul/t05-revalidation-reel-v2` sur `5b42860`. `diag/`, `runs/` et `traces/t05-20261011-234411-9q7N/` sont identiques entre `5b42860` et `main`. Les traces de surveillance (`surveillance/`, `empreintes-fin.sha256`) sont au commit `02b0947afac2e80ac1ffa0896c958e259a22c2f8` de `main`, local au moment de la vérification (pas encore sur le `main` distant). `empreintes-lancement.sha256` et `empreintes-fin.sha256` sont conformes.

**Contenu du manifeste**
- Commit `8f74adaa4b7912f87c9d22ec1594a12910d1930a`.
- Préenregistrement `prereg/T0.5-revalidation-equivalence-pilote-v2.md`, sha256 `4ff2b075…dcc61`, identique au fichier sur disque et à celui du commit `8f74ada`.
- `decisif` vrai, `depot_propre` vrai, aucune réserve.

**Arbre gelé et scripts**
- L'arbre gelé (`CHEMINS_GELES`) est identique entre `6ec7434`, `8f74ada` et `5b42860` ; `src/`, `scripts/` et `tests/` sont identiques à `6ec7434`.
- Les deux commits de résultats n'ajoutent que 21 fichiers, sous `diag/`, `runs/` et `traces/`.
- Les scripts de l'instance au commit `8f74ada` ont les empreintes citées (`59f49aab…de73`, `9e053ae6…1502841`).

**Configuration**
- L'empreinte canonique de `prereg/T0.5-revalidation-config-v1.json` est `50930b3794216c3b857cd906d8b2066eb495534d637041f4d089aa00a9edeefb`, l'empreinte citée.
- La configuration du manifeste, privée des quatre clés des tâches ajoutées par le lanceur, est identique au fichier cité.
- La clé `config_sha256` du manifeste (`2aa955bb…9025`) est l'empreinte canonique de la configuration augmentée de ces quatre clés ; ce n'est pas un écart.

**Citations et graines**
- `exiger_citations` rejouée passe : configuration, tâches d'entraînement (`8d20a698…a4fd`), tâches d'évaluation (`76cdeace…755e67e`), index des invites (`adb4b8bc…e2d9`) et entropie `120571628831802510081029698987406594891`.
- Les 49 graines recalculées par `SeedSequence` depuis l'entropie citée et les clés du plan sont égales à celles du manifeste (R9).

**Plan et domaine des énoncés**
- `taches_d_entrainement` redonne les 16 épisodes dans l'ordre des fiches.
- Le domaine des énoncés est égal à `resume.json` → `resultat.domaine_enonces`.

**Bras « defaut »**
- Fiches : 16 épisodes, 10 actions chacun, toutes comparées (statistique q99, tolérance 0,2).
- `domaine_et_garde`, contrôle négatif (`bilan_controle_negatif` et lecture), `garde_zone_generee` et `audit_symetrie` (avec le repère scellé) sont égaux aux fichiers.
- Repère : les deux plus longues transcriptions (4 932 et 4 782 jetons) sont égales à `mesures-defaut.json` → `resultat.repere_transcriptions`, et leur somme vaut le nombre de jetons du repère (9 714).
- Phase « chemin » : contrôle négatif du passage sain (statistique « max », tolérance 3e-3 ; 8 épisodes du lot 0, 5 actions chacun) et `lire_chemin` sont égaux.
- `duree_projetee_pilote(chrono, 16)` vaut 8 089,6213105190545, égal à `mesures-defaut.json` et à `resume.json`.
- `lire_bras` est égal à `lecture-defaut.json` → `resultat.lecture` et à `resume.json` → `resultat.lectures.defaut`.

**Bras « math »** : `lire_bras(…, panne=…)` est égal à `lecture-math.json` et à `resume.json`.

**Choix et réserves**
- `choisir_noyau` rend (aucun noyau, aucune proposition), égal à `resume.json`.
- Réserves recalculées égales à `resume.json` → `resultat.reserves`.

**Cohérence du chronométrage** (`mesures-defaut.json` → `resultat.chrono`, contre les fiches) :

| grandeur | valeur | contrôle |
|---|---|---|
| jetons générés | 36 397 | somme des jetons par action |
| jetons de contexte | 428 157 | somme des longueurs de contexte |
| jetons de remplissage | 45 915 | somme des remplissages |
| contextes remplis | 474 072 | contexte + remplissage |
| lignes finies avant | 138 | décompte des fiches |
| jetons des passes uniques | 70 274 | somme des transcriptions finales |
| passes de décodage | 6 480 | somme, par lot et par pas, de la plus longue action moins 1 |
| longueur remplie maximale | 4 752 | plus grand contexte augmenté de son remplissage |

Tous ces décomptes sont égaux.

**Relu, non recalculable depuis les résultats scellés**
- Le rejeu : les empreintes du rejeu ne sont pas gardées, seul le drapeau l'est.
- Les statistiques du repère : les activations ne sont pas gardées ; R3 est recalculé depuis les statistiques scellées.
- Le pic de mémoire.
- Les durées chronométrées.

**Vérifications de la version finale** (correcteur ; fichiers à la section 10) : médianes recalculées sur les 160 actions de `episodes-defaut.json` ; longueurs remplies par lot et par pas de « defaut » et de la phase « chemin » ; tailles d'allocation de `run.err` ; bilan de mémoire à la panne ; décomposition de R8 ; repère et noyaux permis relus ; 29 empreintes de la section 6 recontrôlées, toutes conformes ; chaîne ci-dessus relue dans le dépôt de travail.

## 5. Réserves

- **RV-5, énoncés (réserve de la table, acquise d'avance)**.
  - Les 16 énoncés retenus vont de 3 709 à 5 340 caractères.
  - Le plus long énoncé des tâches d'évaluation du pilote compte 6 786 caractères, et leur 90e centile 4 902,8 (`resume.json` → `resultat.domaine_enonces`, `couvre_le_pilote` = false).
  - Le domaine n'est donc que partiellement couvert.
  - La réserve figure dans `resume.json` → `resultat.reserves`. Le préenregistrement la déclare connue d'avance (section « Transparence ») ; elle n'entre pas dans R5.
- **ρ > 3 au noyau « math »** : sans objet, le bras « math » n'a pas été mesuré. Au noyau par défaut, le ρ maximal vaut 1,545, sous 3.
- **Part des actions à zone générée sous 1 % > 0,2 dans le bras retenu** : sans objet, aucun bras n'est retenu. Pour mémoire, « defaut » donne 0,0 (`lecture-defaut.json` → `resultat.zone_generee.part_zone_generee_sous_1pc`) ; sa plus petite part de zone générée par action est 2,97 %.
- Aucune autre réserve prévue par la table ne s'applique : pas d'écarts tous nuls, pas d'audit en défaut, pas de deux bras « contraire ».

## 6. Fichiers lus (sha256 complets)

| fichier | sha256 | rôle |
|---|---|---|
| `prereg/T0.5-revalidation-equivalence-pilote-v2.md` | `4ff2b07548e90fc515fe8944a789bf44267be6e239dee02d2b479e9c701dcc61` | critères gelés |
| `prereg/T0.5-revalidation-config-v1.json` | `ee0945a8b29c54d0918b8c653303a8354bec82a02af1f79e855949ed0743f618` (canonique : `50930b3794216c3b857cd906d8b2066eb495534d637041f4d089aa00a9edeefb`) | configuration |
| `runs/20261011-225701-t05-revalidation-reel/manifeste.json` | `06ee7ed9776427b91bd892de630c9bab462d15e2d922409dabe3ae7eb9f13fbb` | manifeste |
| `diag/…/resume.json` | `d759b05df286913c5a1226657aea80cced67fdd33ef4896a3ee4dacabf47b639` | résumé |
| `diag/…/lecture-defaut.json` | `3c8e76ba3dfd4eba5990d01aaa511c03b129e55349aaa910f853b33ac5a432c7` | lecture, repère, audit, zone générée, chemin |
| `diag/…/lecture-math.json` | `bcebcc576ba2ee73de8cc7b22372a87166cf4f8f161945166d8cd1e47eb5b8c5` | panne du bras « math » |
| `diag/…/mesures-defaut.json` | `bdc78cb29f94b787851b35641644bfebaeb09c9983267c3f95bc34be1ef8a1b0` | mesures, contrôle négatif, chronométrage, mémoire, noyaux permis |
| `diag/…/episodes-defaut.json` | `89c9c9d14ea6ee1744238605fe2b1f2bc5de30043fa6ff59366f59526a6cf455` | fiches (nombres seulement) |
| `diag/…/chemin-defaut.json` | `1a0e389eca7a57119d18f8befb3cc4203d6db8a04cc25a941e84ac8c50e90881` | phase « chemin » (nombres seulement) |
| `donnees/20261007-082440-t05-extraction/taches-entrainement.json` | `8d20a698d76baa8a42cd1494227fc411ef043d24a67a413e5cf812541166a4fd` | plan, longueurs (sans affichage) |
| `donnees/20261007-082440-t05-extraction/taches-evaluation.json` | `76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e` | longueurs (sans affichage) |
| `docs/sources/invites-2606.08892-v1/index.json` | `adb4b8bca7788baf2c4714df96dcdcc2c5043e8f1943542d0fbe1863491ae2d9` | citation vérifiée |
| `traces/t05-20261011-234411-9q7N/journal.txt` | `c516228840ca8c7d4d524f88075873b82eae9a24d630d85e3b5e0d430219b273` | journal de l'instance |
| `traces/t05-20261011-234411-9q7N/run.json` | `32de0e562715a76be5ac4d6e29a813d383d830ea18ce56d9f6e92c0b702cbbdd` | sortie du lanceur |
| `traces/t05-20261011-234411-9q7N/run.err` | `608f6f9a10b73f6f30c1fe8fbd7fd8f34e408f3157435fb79874ed88e1ff3b26` | erreurs de l'instance, avertissements de l'allocateur |
| `traces/t05-20261011-234411-9q7N/tests.txt` | `3ec427e9297c1c4e99b4327f83b98141c8a70bd19a898f0e5e19fda89fb6dbef` | « 670 passed in 491.38s » |
| `traces/t05-20261011-234411-9q7N/tests.err` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | vide |
| `traces/t05-20261011-234411-9q7N/nvidia-smi.txt` | `cfaee76e8b48a2f4e750b495ab2645474316257fc8eccebde415aea023a8bb6f` | carte |
| `traces/t05-20261011-234411-9q7N/empreintes.sha256` | `a3a58430be36141a34cd00ebf4c441d98d8dbde817e405d400cb60e645879163` | empreintes des traces |
| `src/controle_ia/environnements/revalider_pilote_a.py` | `5c8d109d55f22e75bb385eb8c1a728bcdc7e4f151157738ef93c861ced13cea7` | code de lecture |
| `src/controle_ia/environnements/pilote_a.py` | `624761e2831a3fa14ccc1fe817d38a59014c9ef157e600cbd67e411607869bfc` | jeu des épisodes, tirage des actions comparées |
| `src/controle_ia/harnais/episode.py` | `79113b4973d64bbcf0af16b2d7114c009b34132e1392e95ff83cef4d0a488c32` | chronométrage, contrôle négatif |
| `src/controle_ia/harnais/activations.py` | `adeb5856d430f3a6163989c2a53c8ced459235c6dcdd03834b694404c57e0095` | écarts, profils, sondes, crochets |
| `src/controle_ia/harnais/validation_reelle.py` | `d25e4cd92d73eef4d2bd6c7d17328daf49a49c76eab7afd91500d9c04ded8289` | arbre gelé, noyau |
| `src/controle_ia/harnais/modeles.py` (au commit du run `5b42860` ; modifié depuis sur `main`) | `c625a099fba580f098f3ce923b4cfa723c4cd3638f302c15f8fd74119d3a7797` | drapeaux des noyaux permis (l. 282-288) |
| `src/controle_ia/manifeste.py` | `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d` | sceaux, graines |
| `src/controle_ia/scellement.py` | `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2` | sceaux |
| `scripts/amorce_instance_t05.sh` | `59f49aab394c4b7659b716792203663243a106355fbabf666bbb1f61ed55de73` | empreinte citée, vérifiée |
| `scripts/pilote_t05_instance.sh` | `9e053ae69bce6a8fb53bae30e368f0fbf849e19dfa355f0d5fdbb08f31502841` | empreinte citée, vérifiée |
| `docs/sha256sums-lancement-v2.txt` | `dbf8f929b437a38081018685ca358864aca4c726f150371f0ce9fa1ed5b41975` | empreintes de lancement |
| `docs/notes/memoire-noyau-math-T0.4-v3-v2.md` | `2e4e9683aaa8ea42d5f8bddb2fa26489a44485252b3fe1d461397e5beaf8d32b` | note de mémoire citée par Rk-7 : constantes du bilan de mémoire (l. 7, 13, 19-20) |
| `prereg/contre-lectures/T0.5-revalidation-rapport-verification-2-v1.md` | `f896adb17a59c468e4e48c33ac9f22fc7984fa199d90100173c1e861aee3a9bf` | formule de durée jugée conforme avant le scellement (l. 253) |
| `registres/go.md` | `8cddd3ba45629c800c6820faaac2d03b47613b8f5448efa060aed3f46d30c24b` | GO-2026-10-04-08 (l. 16), GO-2026-10-11-01 (l. 23) |
| `registres/arrets.md` | `f5fe8a989247064aa645cc467a7d40c2ad53bf046391ba8d869984a3dca45b23` | arrêt de l'instance 55458787 (l. 17) |
| `registres/depenses.md` | `b7be45a003037f490755a75e26fdf1a1d5cc3ce534eb4da1f1c2091f91f6bb3e` | dépense de l'instance 55458787 (l. 52) |
| `traces/t05-revalidation-v2-20261011-2246/controles.txt` | `7124999da7042ecb8e7d58a18ee0612fbc5735dcabf03d9a6339db1cc3f1c2d0` | contrôles avant dépense, garde de calcul |
| `traces/t05-revalidation-v2-20261011-2246/offre.json` | `be17a81391c032ed6e4289b322b5d5daeebc08006dcf5ee0fb5d4fb43b9757f4` | offre 49506597 (nombres seulement) |
| `traces/t05-revalidation-v2-20261011-2246/lancement.txt` | `4c04c48514435e02cb440b7cb1d2247398d4d2f25bc56f5f03552754364cf55a` | lancement, instance 55458787 |
| `traces/t05-revalidation-v2-20261011-2246/journal-5min.txt` | `5fc65b3a81a53363d837a33ee035a61fc3a7aaac68245ffaae99efe239cb5b38` | contrôle à 5 minutes |
| `traces/t05-revalidation-v2-20261011-2246/empreintes-lancement.sha256` | `5fb4d24e29582e90e857e041f69fd0a835715e77189658adf610b297c64c4c8d` | empreintes du lancement |
| `traces/t05-revalidation-v2-20261011-2246/surveillance/etats.txt` | `d825fee7f6710065e22f957d06c6f215a1ce2f811e4b1d0a39397af6a08e34e1` | états de l'instance |
| `traces/t05-revalidation-v2-20261011-2246/surveillance/sortie-surveillance.txt` | `3ef0cbe88cbe9d362a73020e5c0df3bc24c0058d32184c0a0bada8f88023c46f` | fin de l'amorce, code 0 |
| `traces/t05-revalidation-v2-20261011-2246/surveillance/journal-dernier.txt` | `f9613db22513cb813309953b3e6341c67c0012618fbb5d00dd76e417b7a80262` | relances refusées par R12, aucun second run |
| `traces/t05-revalidation-v2-20261011-2246/empreintes-fin.sha256` | `903f4e3268b0b6d6a7aba35ae3726dd4c6372ef1f7bc5128c44357c9609bdd26` | empreintes de fin |

## 7. Grandeurs descriptives (sans seuil)

Toutes viennent de `episodes-defaut.json`, sauf mention contraire.

**99e centile par action** (maximum sur les couches)
- 160 actions : minimum 0,0352, médiane 0,0659, maximum 0,1354.
- Aucune action au-dessus de 0,15.
- Maximum par couche : 0,0370, 0,1123 et 0,1354 (couches 7, 15 et 23).

**Maximum par action** (grandeur que la garde du 99e centile ne lit pas)
- 139 actions sur 160 dépassent 0,2 ; le maximum vaut 1,1232 (`mesures-defaut.json` → `resultat.mesures.ecart_max`).
- Le repère a aussi des maxima de 0,131, 0,720 et 0,792 aux couches 7, 15 et 23 (`lecture-defaut.json` → `resultat.repere`).

**Repère par couche** (`lecture-defaut.json` → `resultat.repere` ; 9 714 jetons par couche ; couches 7, 15 et 23)
- q50 : 0,01197, 0,01131 et 0,00976.
- q99 : 0,03251, 0,08003 et 0,08761.
- Maximum : 0,1308, 0,7196 et 0,7919.

**Zone générée**
- 99e centile par action : maximum 0,1699 ; 1 action au-dessus de 0,15, aucune au-dessus de 0,2.
- Part de la zone générée dans l'action : minimum 2,97 %, médiane 7,68 %, maximum 25,14 %.

**Chronométrage** (`mesures-defaut.json` → `resultat.chrono`)
- Génération : 665,85 s pour 36 397 jetons, soit 54,7 jetons par seconde, capture comprise.
- Passes uniques : 8,28 s, soit 1,2 % de la projection.
- 42,13 s par épisode dans la projection.
- Premier passage des 16 épisodes, comparaisons comprises : 1 012,18 s (`resultat.duree_s`).
- Plus long contexte rempli : 4 752 jetons.

**Phase « chemin »** (`chemin-defaut.json`)
- Plus grand écart du passage sain : 4,92e-5, 1,54e-4 et 3,05e-4 (couches 7, 15 et 23).
- Sous D1, le plus petit maximum de zone générée parmi les actions comparables vaut 0,2103, au-dessus de 3e-3.

**Run**
- Tests : 670 réussis en 491,38 s (`tests.txt`).
- Run de 22:57:01 à 23:44:09 UTC, soit 2 828 s, pour une échéance de 12 600 s (`journal.txt`).
- Carte de 79,44 Gio (`resume.json` → `resultat.memoire_carte_gio`) ; réglages déterministes acceptés (`resume.json` → `resultat.reglages.deterministe`).

**Comparaison aux prédictions chiffrées** (descriptive ; Rk-1 à Rk-5 lues pour k = « defaut »)
- Rk-1 : attendu de 0,03 à 0,15 ; observé 0,1354.
- Rk-2 : attendu « presque toutes » ; observé 160 sur 160.
- Rk-3 : q99 attendu de 0,03 à 0,09 ; observé 0,0325, 0,0800 et 0,0876.
- Rk-4 : identité attendue ; observée.
- Rk-5 : 160 actions comparées attendues ; 160 observées.
- Rd-6 : C1 attendu de l'ordre de 3,16e-4 ; observé 3,05e-4.
- Rk-7 au noyau « math » : « panne probable au-delà d'environ 4 400 jetons remplis au lot de 8 » ; une panne est observée. Les longueurs remplies propres au bras « math » ne sont pas consignées ; par inférence depuis `run.err`, la panne est survenue à un préremplissage d'environ 5 040 jetons au lot de 8 (section 8, limite 3).
- Rk-8 pour « defaut » : prédit « durée projetée ≤ 7 800 s » (préenregistrement, l. 82 ; réfutation : « au-dessus ») ; observé 8 089,62 s : **prédiction réfutée**. Pour la durée, cette ligne renvoie à « Calcul » (l. 115), qui ne donne qu'un ordre de grandeur, déclaré comme tel : au plus 2 × 10 × 400 = 8 000 pas de décodage au lot de 8, soit 17 à 25 minutes de génération par bras ; à cette borne, multipliées par 12 (192 / 16), 12 240 à 18 000 s. Observé : 6 480 passes de décodage et 665,85 s de génération.

## 8. Limites (du verdict et des mesures)

1. **Composition de la durée de génération (R8).** Dans `jouer_episodes` (`harnais/episode.py`, l. 220-240), `generation_s` est compté depuis l'entrée dans les crochets de capture jusqu'après `relire_crochets_lot`.
   - Il comprend donc la capture des activations de toutes les actions, puisque toutes sont comparées ici (fraction 1,0).
   - Le texte gelé n'exclut de la projection que les comparaisons (« les comparaisons, faites ici sur toutes les actions, n'y entrent pas ») ; il n'exclut pas la capture.
   - La part de la capture n'est mesurée séparément nulle part dans les résultats scellés.
   - Le rejeu du lot 0 et la phase « chemin » ne sont pas chronométrés et n'entrent pas dans la projection.
   - **Compléments des contre-vérifications** (aucun ne change R8 tel que gelé) :
     - **Coûts fixes extrapolés.** La mise en route du bras (premiers appels du modèle) est comptée dans `generation_s` et multipliée par 12 comme le reste ; elle n'est pas mesurée séparément.
     - **Capture au pilote, à 5 %.** La capture ne disparaît pas au pilote. Les crochets s'activent pour tout un pas de lot dès qu'une de ses lignes est tirée (`episode.py`, l. 219-222), et le pilote tire chaque action indépendamment (`pilote_a.py`, l. 113-115). À 5 %, environ 1 − 0,95⁸ ≈ 34 % des pas d'un lot de 8 activent donc encore les crochets ; chaque appel d'un crochet copie la sortie de la couche vers le processeur (`activations.py`, l. 69). L'écart entre le coût de la capture ici et au pilote n'est pas mesuré.
     - **Dépendance à l'hôte.** À chaque passe de décodage, les logits sont copiés vers le processeur, puis la loi et le tirage sont calculés ligne par ligne (`episode.py`, l. 111-121). Ici, 6 480 passes en 665,85 s, soit 9,73 passes par seconde, environ 103 ms par passe au lot de 8 en moyenne, préremplissages et capture compris (`mesures-defaut.json` → `resultat.chrono`). R8 dépend donc aussi du processeur de l'hôte (AMD EPYC 7513, `offre.json`), ce que le run ne mesure pas. Pour tenir le plafond, il aurait fallu 650 s de génération et de passes uniques au lieu de 674,14 s, soit 24,14 s de moins (3,62 % de la génération).
     - Deux composantes identifiées tirent ainsi la projection vers le haut par rapport au pilote : les coûts fixes multipliés par 12 et la capture de toutes les actions. Leur part n'est pas mesurée.
   - **La seule lecture qui retiendrait un noyau ne tient pas** (sceptique 2, qui a cherché une lecture du texte gelé menant à un noyau plutôt qu'au nœud). Elle consisterait à exclure la capture de R8, au motif que le pilote ne compare que 5 % des actions, et demanderait de retirer 24,14 s mesurées. Mais :
     - le texte gelé n'exclut que les comparaisons (l. 97) ;
     - la vérification 2, avant le scellement, a jugé la formule du code conforme au texte (`prereg/contre-lectures/T0.5-revalidation-rapport-verification-2-v1.md`, l. 253) ;
     - la part de la capture n'est mesurée dans aucun résultat scellé, et R8 ne se lit jamais sans mesure (l. 97 : W-14, X-5) ;
     - changer la formule après la lecture des résultats serait un écart au préenregistrement scellé ;
     - les autres pistes échouent aussi : R8 fait partie de la conformité (l. 58 et 105), « math » est non conforme (l. 131), et aucun cas de proposition prête ne s'applique (l. 59-61).
   - La règle est appliquée telle que gelée : R8 est faux, avec un dépassement de 3,71 %.
2. **Extrapolation linéaire (R8).** La formule gelée projette 16 épisodes (2 lots de 8, énoncés d'entraînement les plus longs) vers les 192 épisodes du pilote par un facteur 12. Elle ne tient pas compte de la distribution des longueurs des énoncés du pilote (voir RV-5).
3. **Bras « math » non mesuré.**
   - **Localisation établie par le code.** La panne a été levée pendant le jeu du bras, c'est-à-dire dans `_jouer_bras` (appelée l. 515 de `revalider_pilote_a.py`), qui joue les épisodes (l. 460), le rejeu du lot 0 (l. 466) et les passes du repère en demi-précision (l. 470). Elle a été rattrapée l. 516, dans `_executer_apres_manifeste`, avec le préfixe « mémoire : » (l. 519), et non par le rattrapage du repère en simple précision ou de la phase « chemin » (l. 544, préfixe « mémoire pendant le repère ou la phase « chemin » », l. 548). Rien n'est écrit pour un bras avant la fin de `_jouer_bras` (l. 527-532).
   - **Mesures absentes.** Le texte gelé (X-7) ne garde les mesures d'un bras en panne que pour une panne pendant son repère ou sa phase « chemin ». Il n'y a donc pour « math » ni épisodes, ni mesures, ni noyaux permis, ni pic de mémoire, ni longueurs remplies.
   - **W-6 : écart entre le texte et le code.** Le texte gelé demande que « le pic et la longueur remplie maximale de chaque bras lu [soient] reportés au résumé (W-6) » (l. 97). Le code compte « math » parmi les bras lus (`etat["lectures"][bras] = lecture`, l. 521, dans le rattrapage), mais ce rattrapage ne relève ni le pic ni la longueur remplie : seul `resultats[bras]` les porte (l. 567-571), pour un bras mené au bout. `resume.json` → `resultat.bras` ne contient que « defaut », et `resultat.lectures.math` ne porte que `conforme`, `conforme_avec_marge` et `panne`. Sans effet sur la règle : la panne suffit à rendre le bras non conforme (table, l. 131).
   - **Traces de la panne.** Le message consigné indique 68,64 Gio alloués par la bibliothèque, 7,33 Gio réservés mais non alloués, 2,94 Gio libres et une demande de 6,06 Gio. `run.err` contient sept avertissements de l'allocateur (« memory allocation failed with OOM ») :
     - quatre à 23:38:56, 23:41:29, 23:43:00 et 23:44:05 UTC, pour 10 362 028 032, 18 020 827 136, 22 833 790 976 et 26 013 073 408 octets, sans exception : le run a continué, et le seul message consigné est celui de 6,06 Gio ;
     - trois à 23:44:07 UTC, pour 6 503 268 352 octets (6,06 Gio), la demande qui a levé la panne consignée ; les deux derniers relèvent 3 156 148 224 octets libres, les « 2.94 GiB » du message.
   - **Localisation la plus probable : inférence, non démontrée par le code.** Très probablement, la panne est survenue pendant le premier passage des épisodes du bras « math », à un préremplissage d'environ 5 040 jetons au lot de 8.
     - **Tailles.** Les quatre premières demandes valent exactement 4 941, 8 593, 10 888 et 12 404 unités de 2 Mio, l'arrondi de l'allocateur. Ce sont des matrices d'attention [8, 32, L, L] en simple précision (8 × 32 × L² × 4 octets), pour L = 3 181, 4 195, 4 722 et 5 040. C'est la seule lecture, parmi 1, 2 ou 4 octets par élément, des lots de 1 ou de 8 et 8 ou 32 têtes, qui donne pour les quatre des longueurs sous 6 000 jetons. La demande de 6,06 Gio vaut 3 101 unités de 2 Mio, compatible avec la même longueur de 5 040 (8 × 32 × 5 040² octets, à l'arrondi près).
     - **Simple précision.** Le noyau « math » calcule en simple précision, la réduction en demi-précision n'y étant pas permise (`mesures-defaut.json` → `resultat.noyaux_permis.reduction_demi_dans_math` = faux, lu par `noyaux_attention_permis`, `harnais/modeles.py`, l. 288 au commit du run ; note de mémoire `docs/notes/memoire-noyau-math-T0.4-v3-v2.md`, l. 13). C'est la forme que supposait Rk-7 (« trois matrices d'attention en simple précision »).
     - **Pas le bras « defaut ».** Ses longueurs remplies par lot et par pas vont de 1 386 à 4 752 et ne contiennent aucune de ces quatre longueurs (`episodes-defaut.json`) ; sa phase « chemin » ne dépasse pas 3 000 (`chemin-defaut.json`). Son pic pendant le jeu du bras, poids compris, vaut 24,02 Gio, alors que la plus petite de ces demandes (9,65 Gio), une fois servie, l'aurait porté à 24,61 Gio au moins.
     - **Pas le repère.** Les passes du repère se font une transcription à la fois (`_activations`, l. 336-338 ; `passe_unique`, `activations.py`, l. 105), donc au lot de 1, et non de 8.
     - **Pas de fuite de mémoire depuis « defaut ».** Les 68,64 Gio alloués à la panne s'expliquent par le seul bras « math » : 14,96 Gio de poids en demi-précision (8,03 milliards de paramètres, note de mémoire, l. 7), 4,92 Gio de cache des clés et des valeurs (8 lignes × 5 040 positions × 32 couches × 2 × 8 têtes × 128 × 2 octets, formule de la note, l. 20) et deux matrices de 24,23 Gio, soit 68,33 Gio. Le modèle en simple précision du bras « defaut » (29,92 Gio) n'y tient pas.
     - **Premier passage plutôt que rejeu.** Les quatre demandes forment une seule suite croissante en cinq minutes, comme les contextes qui croissent d'un pas à l'autre (de 265 à 500 jetons par pas pour « defaut »). Un rejeu reproduit les trajectoires du premier passage du lot 0, qui aurait dû traverser les mêmes allocations plus tôt, sans qu'aucune trace antérieure n'apparaisse dans `run.err`.
     - **Chronologie, par estimation.** Les épisodes de « defaut » finissent au plus tôt à 23:15:53 UTC (début du run à 22:57:01, téléchargement de 2:00 dans `run.err`, épisodes de 1 012,18 s). Avec son rejeu du lot 0 (de l'ordre de la moitié de cette durée) et sa phase en simple précision, non chronométrés, « defaut » ne finit guère avant 23:27. À la vitesse de « defaut », le premier passage de « math » (environ 17 minutes) va jusque vers 23:44. Son rejeu, qui n'atteint ses plus longs contextes qu'à ses derniers pas, viendrait bien après.
     - **Portée.** La panne est survenue au-delà des 4 400 jetons environ de Rk-7 et des 4 752 joués par « defaut » : c'est une limite de capacité propre au noyau « math » sur ce domaine. L'inférence repose sur des traces contrôlées par `empreintes.sha256` et par le commit `5b42860`, non scellées par empreinte compagnon (limite 5). Elle est sans effet sur la règle, qui couvre la panne quel que soit son moment.
   - Sur le chemin de code de la revalidation, les seuls rattrapages d'une panne de mémoire sont ceux de `revalider_pilote_a.py`, l. 516 et 544. Tous deux consignent la panne et rendent le bras non conforme : aucun repli silencieux.
4. **Grandeurs relues, non recalculées** : rejeu, statistiques du repère, pic de mémoire et durées (section 4). Leur intégrité repose sur les sceaux, qui sont vérifiés.
5. **Traces de l'instance.** Elles ne sont pas scellées par des empreintes compagnons. Elles sont contrôlées contre `empreintes.sha256` et par leur présence au commit `5b428608575fea8db57e90f47c096229e21074b4`.
6. **Règle D-20.** Le contenu des actions n'a pas été lu ; aucun critère gelé n'en dépend.
7. **Champ du verdict.** Ce verdict applique les critères gelés et ne porte aucun jugement sur la suite. Il ne propose aucune résolution du nœud.

## 9. Corrections intégrées à la version finale

Toutes sont mineures, relevées par les sceptiques et vérifiées par le correcteur dans les fichiers ; aucune ne touche la règle, le verdict ni les valeurs des critères.
1. **Localisation de la panne du bras « math »**, harmonisée aux sections 1, 3 et 8 : « pendant le jeu du bras (épisodes, rejeu du lot 0 ou passes du repère en demi-précision) ». « Rattrapée dans `_jouer_bras` » devient « levée pendant `_jouer_bras` (appelée l. 515), rattrapée l. 516 dans `_executer_apres_manifeste` ». Les quatre premières demandes de `run.err` ne sont plus appelées « échecs », car aucune n'a levé d'exception. « Rien ne permet de dire… » est remplacé par une inférence argumentée, présentée comme telle (sceptique 1, points 1 et 2 ; sceptique 2, point 3).
2. **Section 7** : « R8 : aucune valeur prédite » devient « Rk-8 : prédit ≤ 7 800 s, réfutée pour « defaut » », avec l'ordre de grandeur de « Calcul » (sceptique 1, point 4 ; sceptique 2, point 2).
3. **Section 7** : vraies médianes, 0,0659 (et non 0,0660) et 7,68 % (et non 7,81 %). Les anciennes valeurs étaient la 81e sur 160 (sceptique 1, point 3 ; sceptique 2, point 4).
4. **Sections 4 et 6** : chaîne, du GO à la fusion sur `main`, avec chemins et empreintes (sceptique 1, point 6).
5. **Sections 3 et 7** : drapeau `reduction_demi_dans_math` = faux des noyaux permis ; q50 du repère aux trois couches et son maximum à la couche 7 (sceptique 1, point 7).
6. **Sections 3 et 8** : écart W-6 nommé pour le bras « math » (sceptique 1, point 8).
7. **Section 8, limite 1** : compléments sur la composition de R8 (coûts fixes, capture au pilote, dépendance à l'hôte) et conclusion du sceptique 2 sur la seule lecture qui retiendrait un noyau, sans rien proposer pour la suite (sceptique 1, point 5 ; sceptique 2, point 1).

**Non intégrés** :
- les remarques qui portent sur la suite à donner au nœud (sceptique 1, point 5, dernière phrase ; sceptique 2, point 5), hors du champ du verdict ;
- le contrefactuel sur R7 du bras « math » (sceptique 2, point 3), puisque ce bras n'est pas mesuré.

## 10. Fichiers de travail des contre-vérifications (hors dépôt, sha256)

Sous `/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/verdict-revalidation-v2/` :

| fichier | sha256 | rôle |
|---|---|---|
| `verdict-T0.5-revalidation-v2-brouillon.md` | `ae574fe0e6bd4f57016ceb97f983b00b8239f36e20698147cbb642c76b899249` | brouillon du verdict |
| `resultats-workflow.json` | `b10672f583568fdbf1958402382f9faa35063c0952a9422cede69491dd6d1e9d` | verdict et points des deux sceptiques, avec preuves |
| `sceptique-1/recalcul_sceptique.py` | `5d674823e9cd67ce00232b6f6928ae2cc4a97326d27db819a0648112e8ce12eb` | sceptique 1 : recalcul indépendant |
| `sceptique-1/journal-recalcul-sceptique.txt` | `f17313e9d440eb3c80451fc5a5612a0920a2269836db8123fea5a76c1e5dd17b` | sceptique 1 : journal (95 constats, 0 écart) |
| `sceptique-1/sortie-recalcul-sceptique.json` | `09ab0e68789e21d7578f0593b38c743217df58ea6b48ab480eafa6b17e211e59` | sceptique 1 : sortie |
| `sceptique-1/descriptifs_sceptique.py` | `4064e929015d3e774389a67a941afe3c13a3cd8de0b353d70edd99c5b17f2190` | sceptique 1 : descriptifs |
| `sceptique-1/journal-descriptifs-sceptique.txt` | `3aff0f6145c1be453a3b1ad0680137d2b7ed433e50c503e3ff9df80a67005e07` | sceptique 1 : médianes |
| `sceptique-1/schema_sans_texte.py` | `2f8592f7d9fccb77eceafc1cc7ff24fd282c85f8a25c3151854277607c995770` | sceptique 1 : structure sans texte |
| `sceptique-2/recalcul_sceptique2.py` | `cb3d3ebe22f726efba7a2a434fb32a351f6a37647b9c9cc2cb42bae17a68d40e` | sceptique 2 : recalcul indépendant |
| `sceptique-2/recalcul-sceptique2-sortie.json` | `562bdeeb3492d0b54156a0215f79d201c2cf66b5667d52f845b15843900e8561` | sceptique 2 : sortie (72 constats, 0 écart) |
| `sceptique-2/tailles_allocation_math.py` | `b2d809a6a93cc24ea1a4d22170f50a59f1d6420eeff0c2320af60d8cb71d3c81` | sceptique 2 : tailles d'allocation |
| `sceptique-2/inference-memoire-et-R8.txt` | `e5a31e82c4498b3f7111d6190da98e8b24c936000777a15afa5d89792c4e16ba` | sceptique 2 : inférence sur la mémoire et R8 |
| `sceptique-2/empreintes-citees-brouillon.txt` | `70e9becbd50a10072bc44f5707550c665dc5afa42166d2a3d5bdc5105607ec84` | sceptique 2 : 29 empreintes du brouillon |
| `sceptique-2/schema_sans_texte.py` | `5a2538de74869dba374a52026a6dc9baa6c6eb8818d09e1ce5e17589802be35d` | sceptique 2 : structure sans texte |
| `sceptique-2/afficher_sans_texte.py` | `6baa5dca32676dec72af4ef63f3424c72caf9b3f02c952088d6b717306ae778e` | sceptique 2 : affichage sans texte |
| `correcteur-final/verifier_corrections.py` | `ae9d904ecee7c7130399575c187e02aedda9a5c7aae67537f9885701bea42435` | correcteur : vérifications numériques |
| `correcteur-final/verifications-sortie.json` | `9bb2586879977378c36d3c30e4fde51cc17f725ae93fb80fe3fec4c18192ec70` | correcteur : sortie complète |
| `correcteur-final/verifications-journal.txt` | `a4435d50a10c067b91485dd29398bb1405bfabbbd96f1383b8465d53c10e3385` | correcteur : journal |
| `correcteur-final/schema_sans_texte.py` | `8e2139e87d33a7a3d98ef49e98aebd6decf66903f619975bd76f74b61c95102c` | correcteur : structure sans texte |
| `correcteur-final/empreintes-section6.txt` | `70e9becbd50a10072bc44f5707550c665dc5afa42166d2a3d5bdc5105607ec84` | correcteur : 29 empreintes recontrôlées (même contenu, octet pour octet, que le fichier du sceptique 2) |
