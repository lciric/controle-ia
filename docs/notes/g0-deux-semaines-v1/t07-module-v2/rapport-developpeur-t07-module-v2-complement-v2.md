# Rapport complémentaire 2 du développeur : module de lecture de T0.7, v2 — fusion de `main`, repli du recalcul, T7-P10 de P3, corrections de la contre-lecture — v1

**Consignes.**

- Message de la mère du 10 novembre 2026 vers 06:36 UTC, en trois tâches : fusion de `main`, repli du recalcul, T7-P10 des sondes de P3.
- Message suivant, sur les corrections de la contre-lecture du code (`docs/notes/g0-deux-semaines-v1/t07-module-v2/contre-lecture-code-t07-v1.md`, `1efd31f6…`, lu par `git show main:` au commit `23c0264b` ; contre-lecteur Fable, sur `1f77b34d`).
- Interdits communs v2 (`1ee3b370…`, règle 9).

**Cadre.** Même arbre (`/home/user/wt-t07`), même branche locale (`prep/t07-module-v2`), commits neufs seulement : `1f77b34d` n'est pas réécrit. Les rapports précédents (`b4d5784b…`, `06909a73…`) ne sont pas réécrits. Heures par `date -u`.

## Verdict

- **Fusion de `main` faite**, sans conflit et sans extraire `docs/notes/bras-attaque/`.
- **Repli du recalcul écrit**, avec le code de la chaîne de T0.6 désormais présent, appelé tel quel. Il est éprouvé en mode jouet : les activations recalculées sont égales au bit près à celles de la chaîne (252 sur 252), avec trois artefacts.
- **T7-P10 de la tromperie et des enjeux fait.** Les données de P3 sont au dépôt et scellées, et le découpage de P3 est reproduit à ses effectifs.
- **Corrections de la contre-lecture** : CT-01 (bloquant) à CT-07 sont corrigés ; les mineurs courts aussi ; les autres sont listés pour le texte.
- **Résultats** : essais de T0.7 au commit des corrections, 247 passés, 1 sauté. La répétition jouet, entropie de T0.6 fixée, rejoue le cas de CT-01 (7 actions sans mot sur 84) : l'étape A va au bout, codes 0, 0, 0.

## 1. Commits (branche locale ; rien de poussé)

| commit | jalon | contenu |
|---|---|---|
| `a4fc13bc` | fusion | fusion de `main` (`7391acea`) : aucun conflit ; seuls fichiers touchés des deux côtés, les deux rapports du développeur, identiques |
| `02d638f1` | 5 | `repli_recalcul_v1.py`, `donnees_p3_t07_v1.py`, `lecture_v2.py` (commande `repli-recalcul`, clé `donnees_p3`), essais, `scripts/repetition_jouet_repli_t07_v1.py`, `configuration-t07-v2.json` |
| `5c6d78a2` | 5b | répétition jouet du repli au commit `02d638f1`, scellée (`repetition-jouet-repli-v1/`) |
| `8dc1cb09` | 6 | corrections de la contre-lecture (CT-01 à CT-07, mineurs corrigés), `tests/test_t07_corrections_cl1_v1.py`, `scripts/repetition_jouet_t07_v2.py` (entropie fixée) |
| `73d60737` | 6b | répétitions jouets au commit `8dc1cb09`, entropie 1, chemin normal et repli, scellées (`repetition-jouet-v3/`, `repetition-jouet-repli-v2/`) |
| (ce rapport) | 7 | ce rapport et son compagnon |

## 2. Fusion de `main`

- **Commande** : `git -c core.sparseCheckout=true merge main --no-ff`. Les motifs de l'extraction partielle sont tenus pendant la fusion.
- **Ce qu'apporte `main`** : 468 fichiers changés depuis la base commune `eea731f5`. Aucun chemin interdit parmi eux (vérifié sur la liste des noms, avant la fusion) ; aucun fichier de T0.7 touché par `main`.
- **Ajout à l'extraction** : `docs/sources/invites-2606.08892-v1/` (consignes de l'environnement, lues par la chaîne). Rien sous `docs/notes/bras-attaque/`.
- **Essais de T0.7 juste après la fusion** (06:38 à 06:50 UTC, au commit `a4fc13bc`) : 223 passés, 1 sauté.

## 3. Repli du recalcul (`src/controle_ia/t07/repli_recalcul_v1.py`, fichier neuf)

**Code de la chaîne (fusionné de `main`, code de `1609a4bf`) appelé tel quel** :

- `charger_modele_et_format` et `conversation_de_controle` ;
- `regler_determinisme` ;
- `organismes.lora` ;
- `adaptateurs_en_simple_precision` ;
- `t06.identite` : `logits_de_controle`, `controle_identite`, `exiger_etat_de_phase` ;
- `t06.lanceur` : `charger_taches_t06`, `_fin_notee` ;
- `etats_adaptateur` ;
- `environnement` et `charger_consignes` ;
- `tache_de`, `charger_invite`, `harnais.episode.Action`, `passe_unique`, `ActivationsDemi`.

Aucun fichier existant hors de T0.7 n'est modifié.

**Déroulé, dans l'ordre du texte** :

1. Manifeste de 7b.
2. Logits de contrôle de la base, avant l'injection.
3. Injection des adaptateurs ; chacun chargé à son sceau, avec l'empreinte écrite dans `distillation-t06.json`.
4. **Contrôle d'identité à dose 0.**
5. **Rejeu en forçage** de chaque épisode, état d'adaptateur par état d'adaptateur. La conversation est reconstruite comme `jouer_episodes` la construit. Les jetons de chaque action sont les identifiants écrits par la chaîne ; le texte décodé et la clé doivent égaler ceux de la chaîne.
6. Passe unique par épisode, empan `[début, _fin_notee[`.
7. Activations écrites en demi-précision dans `donnees/<run>/activations/`. Le dossier doit être absent (R12).
8. **Garde d'équivalence** (`repli_v1`, inchangé) sur le sous-ensemble poussé. Statistique, tolérance et fraction du contrôle négatif sont lues dans le manifeste de 7b.

**Commande** : `lecture_v2 repli-recalcul RACINE RUN_T06 CONFIG`.

- Elle recalcule, puis joue l'étape A. La garde d'identité au bit près y est remplacée par la garde d'équivalence (R11 : « garde d'identité ou garde d'équivalence du repli »).
- Un échec du repli rend le code 3, avec ce motif : « relance une fois sur la même carte que la course, puis nœud ».

**Éprouvé en mode jouet seulement** (`tests/test_t07_repli_recalcul_v1.py`, 4 essais, sur un vrai run jouet de `t06.lanceur_v6`) :

- cas sain : chaque activation recalculée est égale au bit près à celle de la chaîne ;
- artefact : empan décalé d'un jeton → garde en échec ;
- artefact : empreinte d'adaptateur autre → arrêt ;
- artefact : dossier présent → refus.

**Répétition de bout en bout** : T0.6 jouet, activations retirées, `repli-recalcul`, puis étape B. Codes 0, 0, 0 ; 252 activations égales au bit près, au commit `02d638f1`, puis au commit `8dc1cb09` (section 6).

**Ce qui n'est pas éprouvé : le mode réel** (révision figée, `cuda`, hors ligne). Le chemin est le même.

## 4. T7-P10 de la tromperie et des enjeux (`src/controle_ia/t07/donnees_p3_t07_v1.py`, fichier neuf)

**Les données et le découpage de P3 sont au dépôt et scellés** ; chaque compagnon est égal à son fichier, vérifié par empreinte :

| fichier | empreinte |
|---|---|
| `donnees/T0.7-faits-repe-v1/facts_true_false.csv` | `151b6163…` |
| `donnees/T0.7-models-under-pressure-v1/training/train.jsonl` | `04216df3…` |
| `runs/20261019-230011-p3-reel/manifeste.json` | `3f21774c…`, porte les graines « tirage-enjeux », « decoupage-tromperie », « decoupage-enjeux » |
| `diag/20261019-230011-p3-reel/sondes-figees.json` | `fb418127…`, porte `faits_exclus`, `lignes_enjeux`, `effectifs` |

Rien de 7a, rien sous embargo.

**Découpage de P3 reproduit.** Les fonctions de P3 sont appelées telles quelles, avec les graines de P3 : tromperie 478 / 120, enjeux 1 591 / 409, égaux aux effectifs de P3. Deux gardes : le tirage des enjeux doit égaler les lignes écrites par P3, et les effectifs doivent égaler ceux de P3.

**Témoins appris** (pénalité choisie sur la validation de P3) :

| concept | aire de validation du témoin |
|---|---|
| tromperie | 0,5 : même texte sous les deux étiquettes |
| enjeux | 0,936 |

**Entrée de la configuration.**

- Clé **facultative** `donnees_p3` : quatre fichiers, chemin et empreinte ; en mode réel, ceux de la provenance de P3. Elle est facultative pour qu'aucun essai existant ne soit modifié.
- Sceaux vérifiés dans la garde de l'étape A.
- `brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v2.json` (`7daf4f9b…`) : la v1, plus `donnees_p3`.

**Essais** : `tests/test_t07_donnees_p3_v1.py`, 4 essais. Ils couvrent la configuration, les sceaux et le découpage avec deux artefacts, et l'étape complète avec les données de P3, où T7-P10 est lu pour les quatre concepts.

## 5. Corrections de la contre-lecture : table défaut par défaut

| id | gravité | état | ce qui est fait (commit `8dc1cb09`) | essai |
|---|---|---|---|---|
| CT-01 | bloquant | **corrigé** | Notation de chaque témoin lexical sous garde. En échec : témoin « échec » avec motif, `actions_sans_mot`, aucun tableau `lexical_<concept>`, T7-P10 « non lue : témoin lexical en échec ». Le paquet gelé n'est pas modifié. Répétition jouet v2 à **entropie de T0.6 fixée** (`--entropie-t06`, enveloppe autour de `lanceur_v6._main`, code gelé intact) : l'entropie 1 rejoue le cas, 7 actions sans mot sur 84 | `test_CT01_…` (artefact) ; essais de bout en bout (sain) ; répétitions v3 |
| CT-02 | à corriger | **corrigé** | `concepts_lus` et `jeux_scelles` dans la configuration du manifeste. À l'étape B : concepts de `sondes-t07.json` égaux à ceux du manifeste, et nom de chaque sonde neuve préfixé par son concept, sinon refus | `test_CT02_…` |
| CT-03 | à corriger | **corrigé** | Les déclencheurs « aire hors de [0,05 ; 0,95] » et « quantile 0,95 du plancher > 0,70 » de R9 sont cherchés sur tous les jeux d'organisme lus : décisifs, hors jugement, et lectures complémentaires contre un plancher (T7-P3, P4, P6, P9, P15, P18) | `test_CT03_…` |
| CT-04 | à corriger | **corrigé** | `familles` doit égaler la liste gelée ; `reglages` doit être nul ou égal aux valeurs par défaut. Sinon, arrêt de configuration, motif écrit | `test_CT04_…` |
| CT-05 | à corriger | **corrigé** | Échec de T7-P6 (apprentissage, essai d'égalité, plancher ou notation) → T7-P6 « échec », puis « non lue » à l'étape B. Une direction de concept en échec est écrite « échec », les autres sont lues | `test_CT05_…` |
| CT-06 | à corriger | **corrigé** | `--instant` refusé en mode réel (code 2), pour `etape-a`, `etape-b` et `repli-recalcul` ; permis en Python et en jouet | `test_CT06_…` |
| CT-07 | à corriger | **corrigé** | Lecture des épisodes, garde d'identité (ou garde d'équivalence du repli) et mesures **avant** l'apprentissage ; `ouverture-t07.json` est écrit avant | `test_CT07_…` |
| CT-08 | mineur, texte | **au texte** | Refus de la garde pour une tâche de réserve parmi les tâches d'évaluation, ou un jeu ou des phrases mal formés : de nature « nœud », à écrire au brouillon 20 | — |
| CT-09 | mineur | **corrigé en partie** | R14 alignée sur la garde de fin (`<=`). Une réduite datée après la fin de l'étape A n'est pas refusée : **au texte** (P3-bis b8 l'exclut) | `test_CT09_CT10_…` |
| CT-10 | mineur | **corrigé** | Garde de fin d'étape A : avec `VERDICT-P3BIS` et une réduite, G1 et l'appui des réduites sont contrôlés (registre des préalables relu) avant d'écrire `SCORES-T07` et `SONDES-T07` | `test_CT09_CT10_…` |
| CT-11 | mineur | **corrigé** | Dates du journal de P3-bis non décroissantes, sinon `JournalFautif` | `test_CT11_…` |
| CT-12 | mineur | **corrigé en partie** | En-tête et messages mis à jour, en gardant les mots que les essais existants attendent. Le nom de l'essai de `tests/test_t07_lecture_v2.py` l. 244 n'est pas changé : la consigne interdit de modifier un essai existant | — |
| CT-13 | mineur, texte | **corrigé en partie** | Au moins quatre concepts en mode réel, au moins deux paires par concept ; quatre artefacts du lecteur. **Au texte** : format d'un fichier unique avec une ligne `format_lecture` (consigne des concepts et brouillon 20) | `test_CT13_…` |
| CT-14 | mineur | **corrigé** | Les clés connues avant le manifeste y sont inscrites : 30 couples, toutes les sondes possibles de T7-P6, directions des concepts, `decoupage`, `temoin-p6`. Seules les clés nommées après le manifeste restent dérivées (sondes choisies, lectures de l'étape B) | `test_CT14_…` |
| CT-15 | mineur | **corrigé en partie** | La ligne `SCELLEMENT-T07` est comparée au préenregistrement de la configuration ; refus si le chemin diffère. **À l'ordre d'exécution** : lancement depuis `RACINE`, et `autoriser_depot_sale` | `test_CT15_…` |
| CT-16 | mineur, texte | **au texte** | Forme de `lecture-t07.json` : placebo sous `predictions["T7-P19"]`, disjonction dans `sondes-t07.json`, réduite pendant l'étape A dans `notation-t07.json` | — |
| CT-17 | texte | **au texte** | L'ordre d'exécution apporte `registres/` à jour depuis `main` à l'ouverture ; le texte nomme la branche qui porte les écrits de P3-bis | — |
| CT-18 | mineur | **corrigé** | « partiellement lue : lues conformes (…) ; non lues (…) » à la place de « confirmée (non lues …) » | `test_CT18_…` |

**Point 5 de la contre-lecture.**

- **Mode réel jamais joué** : bloquant pour la demande de GO de l'étape A. La passe à blanc de l'extracteur proposée (jeux génériques seuls, rien d'écrit) **n'est pas écrite**. Reste.
- **Q11** : le contre-lecteur ajoute que l'étape A refuse dès que `arret.json` de T0.6 existe. L1 « par `arret.json` » n'est donc jamais écrite. À porter au brouillon 20.

## 6. Essais

| run | heures (UTC) | code | résultat |
|---|---|---|---|
| T0.7 après la fusion (4 fichiers) | 06:38 à 06:50 | `a4fc13bc` | 223 passés, 1 sauté, 697 s (en même temps que d'autres essais) |
| repli (`test_t07_repli_recalcul_v1.py`) | 06:43 à 06:44 | code de travail du jalon 5 | 4 passés, 32 s |
| données de P3 (`test_t07_donnees_p3_v1.py`) | 06:51 à 06:53 | code de travail du jalon 5 | 4 passés, 142 s |
| jalon 5 (5 fichiers) | 06:50 à 06:59 | code de `02d638f1` | 227 passés, 1 sauté, 522 s |
| **corrections, les 7 fichiers de T0.7** | 07:11 à 07:20 | **`8dc1cb09`** | **247 passés, 1 sauté**, 526 s |
| répétition du repli | 07:00 environ | `02d638f1` | 0, 0, 0 ; 252 égales au bit près |
| **répétition v2, entropie 1** | 07:21:15 à 07:22:06 | `8dc1cb09` | T0.6 0 (27,6 s) ; étape A 0 (16,1 s) ; étape B 0 (4,3 s) ; 7 actions sans mot sur 84 ; témoins lexicaux de la dissimulation et du domaine en « échec », T7-P10 « non lue » ; L1b |
| **répétition v2, entropie 1, repli** | 07:22:06 à 07:22:53 | `8dc1cb09` | T0.6 0 ; repli et étape A 0 (12,9 s) ; 252 activations égales au bit près ; étape B 0 ; L1b |

Répartition des 247 essais par fichier :

| fichier | passés |
|---|---|
| v1 | 138 (+ 1 sauté) |
| v2 | 63 |
| sondes neuves | 18 |
| repli (garde) | 4 |
| repli (recalcul) | 4 |
| données de P3 | 4 |
| corrections | 16 |

Aucun essai existant n'a été modifié. **La suite complète n'est pas rejouée à ce tour** ; la consigne demandait les essais de T0.7.

## 7. Empreintes au commit des corrections et valeurs proposées

| fichier (au commit `8dc1cb09`) | état depuis `1f77b34d` | sha256 |
|---|---|---|
| `src/controle_ia/t07/__init__.py` | inchangé | `553bd9d29b56f0923859da2d3a63fadf9891c4274b9bb23fc367496e77e5a61e` |
| `src/controle_ia/t07/criteres_v1.py` | inchangé | `12b999fecce093372a29fb70d8c11eb7fe965f34c8746a31b399baaecc5ae8c5` |
| `src/controle_ia/t07/donnees_p3_t07_v1.py` | neuf | `acf02303b98157411dd30881d19ec9457423afdc7c27ef4e9342823234030cf4` |
| `src/controle_ia/t07/garde_adaptee_v1.py` | modifié | `7ff571d7b1f06db94043545bfe178a066613ddd734aacca1cf3ef52ba0b511de` |
| `src/controle_ia/t07/journal_p3bis_v1.py` | modifié | `389f68080545956c108631233e5ae89d88d7061bf493bb65d32144d47aa191a4` |
| `src/controle_ia/t07/lecture_v1.py` | inchangé | `62b34790346123924c275c4e2021ea31db26837c5b7840e9e047d272a54c9678` |
| `src/controle_ia/t07/lecture_v2.py` | modifié | `9d5c1c05acbc4cc031d2234d5c171f3374b90dfa8172fa3aa7299245ff8bb41a` |
| `src/controle_ia/t07/lectures_t07_v1.py` | modifié | `96978f1474cab3927bd5c0ffc1c1054abf41540d5e80a8df54ef55c28034031d` |
| `src/controle_ia/t07/mahalanobis_v1.py` | inchangé | `b28163062aa8d39cf3894b327a7446f63d50d4f1394eac894b16b4da8ff962f9` |
| `src/controle_ia/t07/plancher_v1.py` | inchangé | `ac6e8263293ed30c807ef91f8eab0adbcbf8e1b91d5e4c56e73dbffa1a7099dc` |
| `src/controle_ia/t07/registre_v1.py` | inchangé | `914b8f374ce8f8bc6550d03c34c5f6c2a97ac93b8ce44da24fd88229185ffca0` |
| `src/controle_ia/t07/repli_recalcul_v1.py` | neuf | `9ceabbcb56cacde0cad6e849a36884139b0175bdf20af5e34cf4514d9da3fe1d` |
| `src/controle_ia/t07/repli_v1.py` | inchangé | `7ae5862da1c867d99cbbdfa0c2350a238920c314a8924254abaf368dd335223a` |
| `src/controle_ia/t07/sondes_neuves_v1.py` | modifié | `b1c59783ed231c88c5671bc124b0a3f448e5b948b48677db2f361fe6d05c085d` |
| `tests/test_t07_lecture_v1.py` | inchangé | `ae82fe0d606fa22223fa86f846788145b7c436d12fe65c2ddb3359a907329722` |
| `tests/test_t07_lecture_v2.py` | inchangé | `6274d6b97e706e166a0f3d8c53c204e9cbbe79b1166734e6260f6b4b888cafff` |
| `tests/test_t07_sondes_neuves_v1.py` | inchangé | `a958952d58e727fbf60b53a31078a949885e3705b88a0adb5285e41e5ddaeaad` |
| `tests/test_t07_repli_v1.py` | inchangé | `d12833e867559efc69380c251e78d493bc25958225c06eb9bd288629bdf17500` |
| `tests/test_t07_repli_recalcul_v1.py` | neuf | `f307c5cf6a817f563d0c017e2bf423e4aaa0e24a85eb57f22df3bc2c9c479e5a` |
| `tests/test_t07_donnees_p3_v1.py` | neuf | `b7c23376c338dcb58b509c36e0e9ddc483b0cb9ee403ebf4c61c2fc52b4f02b3` |
| `tests/test_t07_corrections_cl1_v1.py` | neuf | `96c6c067b432eba29ef2117d8dbe1f93b18b42828061a010543ca9dc5b9dfd6d` |
| `scripts/repetition_jouet_t07_v1.py` | inchangé | `7ccd9bbbdad3be58a38973fd2089a6a2b513de25e129afbdbef456dc72dcc880` |
| `scripts/repetition_jouet_repli_t07_v1.py` | neuf | `28f6eb96be7b8ff0aa955a076facda2a715aacd1ae36fe20614482135b9e1077` |
| `scripts/repetition_jouet_t07_v2.py` | neuf | `0f8771c45ebdd57a7416ba8036d5677501b95221d72991f11a2fa1c19f425f8f` |

- **`COMMIT_CODE_T07` proposé : `8dc1cb09f5e764f37aa87cf1410bc6586249b3d1`.** Il reste provisoire : le mode réel n'a jamais été joué, et la passe à blanc de l'extracteur manque (section 5).
- **`EMPREINTES_CODE_T07`** : la table ci-dessus (14 modules, 7 fichiers d'essais, 3 scripts). Les six modules v1 et `tests/test_t07_lecture_v1.py` restent égaux à `51a1874c`.
- **Configuration brouillon** : la v2 (`configuration-t07-v2.json`, fichier `7daf4f9b…`) a pour empreinte canonique `889a3d34911ffb7754d65d9ea6676d3e174d570a931541fbdafcae671a61bb1e`. `entropie` reste nulle jusqu'au candidat. `familles` et `reglages` sont désormais contraints (CT-04) ; leurs valeurs du brouillon passent. La v1 (`8b2d8138…`, `9564d0ec…`) reste valable sans T7-P10 de P3.

## 8. Interprétations neuves, et ce qui reste

**Interprétations neuves** (une ligne chacune, avec la lettre du texte) :

20. Le témoin de la tromperie et des enjeux lit le texte que lit la sonde de P3 : le fait, et le texte de l'utilisateur, entiers. Les coupures en jetons (5 derniers, 128 premiers) demandent le tokeniseur. Lettre : « le témoin lexical lit le même empan d'entraînement que la sonde » ; plan, point 10.
21. Un texte des enjeux sans aucun mot (`','`, un exemple) est exclu de l'entraînement du seul témoin, et compté : le paquet gelé le refuse. Lettre : « même découpage que P3 ».
22. La clé `donnees_p3` est facultative, pour ne modifier aucun essai existant. Sans elle, T7-P10 de la tromperie et des enjeux est « non lu », avec son motif. Le brouillon 20 dira si elle est exigée en mode réel.
23. Repli : les activations recalculées vont dans `donnees/<run>/activations/`, qui doit être absent (R12). L'étape A y remplace la garde d'identité par la garde d'équivalence. Un échec du repli rend le code 3. Lettre : plan, point 8, repli ; R11.
24. CT-01, première voie de la contre-lecture : un témoin en échec n'est pas noté. L'autre voie (noter les seules actions qui portent un mot) n'est pas prise. Lettre : à écrire au brouillon 20, car le choix retire une lecture gelée sur ce run.

**Ce qui reste avant le GO de l'étape A** :

- le premier passage en mode réel : extracteur, frontière « avant le champ » sur le vrai découpage en jetons, durée, mémoire ;
- la passe à blanc de l'extracteur, proposée par le contre-lecteur ;
- le repli en mode réel ;
- les points marqués « au texte » ci-dessus (CT-08, CT-09, CT-13, CT-15, CT-16, CT-17), les interprétations 20 à 24, et Q11 (constat du contre-lecteur).

## Interdits tenus

- Aucun chemin interdit ouvert, extrait ni listé ; aucune donnée de 7a ; aucune valeur de clé ; aucun appel externe ni téléchargement ; aucune dépense ; ni `fetch` ni `push`.
- **Règle 9 des interdits v2** : depuis qu'elle m'a été transmise, aucune recherche récursive sur un dossier qui contient un chemin interdit. Les recherches faites plus tôt dans la session (`grep -rn`) ne portaient que sur `src/controle_ia` et `tests`, qui n'en contiennent aucun.
- Le `lecture-sondes-t06.json` des runs jouets n'a jamais été ouvert.
- `/home/user/wt-t07-jouet` est gardé.
- Dossiers temporaires sous `/home/user/wt-t07/.essais-tmp/`, effacés par leur chemin exact.
- Garde des secrets à 0 avant chaque commit.
