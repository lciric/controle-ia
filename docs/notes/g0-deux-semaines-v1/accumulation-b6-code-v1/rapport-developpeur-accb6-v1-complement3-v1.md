# Complément 3 au rapport du développeur — barreau 6 (`ACCB6`) : phrases de (i) alignées sur le candidat 2 — v1

- **Auteur** : le même développeur neuf (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Mêmes exclusions que dans le rapport.
- **Consigne** : message de suite de la mère (R-2278), même consigne (`consigne-code-accb6-v1.md`, `48b502d0…`), mêmes interdits, même méthode d'arbre. Rapports précédents gardés tels quels (R12) : rapport `2a6880e4…`, complément 1 `02d837c9…`, complément 2 `94226fc8908d4746e63f945892d7a3aaea804c7d301f0bd241bcbfaa46ef3d7f`.
- **Lu** (par `git show`, empreintes vérifiées) :
  - vérification courte du candidat 2, `prereg/contre-lectures/accumulation-barreau6-v1-candidat2-verification-courte-v1.md`, `d35055ff1ac72264e94a6a83228f49963d4e7b227a7d7853733b281989f2d5dd` (commit `39a954338`), § 6 : VB6-1 à VB6-6 ;
  - candidat 2, `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat2.md`, `0716d3d52fd60f76b51c921ef8284580d70ddc587d855cfbc12381c1667baee1` (commit `0d641ab3f`), l. 118-146 (« Critères de lecture gelés »).
- **Heures (UTC, relevées par `date -u`)** :
  - arbre recréé à 20:37 ;
  - banc de 20:42:23 à 21:10:34 ;
  - commit 21:11:01 ; poussée 21:11:04 ;
  - complément écrit à partir de 21:12.
- **Verdict en une ligne** : le code écrit exactement les phrases du candidat 2 (VB6-1, VB6-2 levés), et les modules, le script et la sortie de l'énumération pointent sur le candidat 2 (VB6-5). 171 essais passent, dont un qui compare les 1 188 phrases produites à la table du texte. Énumération v2 rejouée, d'empreinte neuve `00088af568388a4fbe381b7d80b97883b242013d99c7c5893bde54b9e741873e`. Le banc tue 71 mutations sur 71. **Commit final proposé pour `COMMIT_CODE_ACCB6` : `6c98ea20ab7ecfff0c7f10998b9dfad3d75cc625`.**

## 1. Commit final proposé pour `COMMIT_CODE_ACCB6`

- **`6c98ea20ab7ecfff0c7f10998b9dfad3d75cc625`**, branche `prep/accumulation-b6-code-v1`, parent `5ee8a4ac8712221a31599e2a92dfbae981cc5704`. Le commit est poussé et la tête distante vérifiée égale. Aucune fusion. Arbre `src/` : `27666b8779e25a44b15e762ddca4727fa6c98a4c` ; arbre du paquet : `9b380c5f41791a9299e771a6b18dc0beac631307`.
- **Contrôle réel** fait par ce développeur. `ecrire_fichier_code` a été lancé au commit `HEAD` de l'arbre recréé, avec une sortie dans le bac à sable et une entropie d'essai. `controler_code` a ensuite été lancé sur le paquet effectivement importé. Résultat : **conforme**, 6 fichiers, tête = `6c98ea20…`. Le fichier d'essai a été effacé.
- **Fichier de `CODE-ACCB6` à écrire pour ce commit** : cinq fichiers du paquet ont changé (`__init__.py`, `etats_v1.py`, `garde_v1.py`, `lecture_v1.py`, `phrases_v1.py`). Il faut l'écrire avec l'entropie déjà tranchée, `ecrire_fichier_code(DEPOT, "6c98ea20ab7ecfff0c7f10998b9dfad3d75cc625", SORTIE, entropie=186246456082298562823446322699284949559)` (R-2277, VB6-3 ; aucun second tirage), et non par la commande `ecrire`, qui tirerait une entropie neuve. Puis le sceller et inscrire la ligne.

## 2. Arbre de travail

- L'arbre a été recréé comme la dernière fois : `git worktree add --no-checkout`, `git sparse-checkout init --no-cone`, les six motifs `/*`, `!/*/`, `/src/`, `/tests/`, `/scripts/`, `/brouillons/accumulation-barreau6-v1/`, puis `git checkout`.
- Vérifié : `docs/` absent de l'arbre, donc `docs/notes/bras-attaque/` jamais extrait. Arbre propre, à jour avec `origin` (tête `5ee8a4ac…` au départ).
- L'arbre est retiré à la fin, propre et poussé.

## 3. Ce qui change

- **`phrases_v1.py` (VB6-1, VB6-2)** — exactement la voie (a) de la vérification :
  - `CORPS_I_A` ajouté. C'est `CORPS_A`, où « contrôle à adaptateur égal à la seule dose 1 (`T100`) » devient « contrôle de consigne : `temoin` (B6-D3, B6-D3b) ».
  - `PHRASE_I_A` et `PHRASE_L_I_A` sont maintenant construites sur `CORPS_I_A`.
  - `PHRASE_L_I_M` devient « {barreau} réfuté à cette puissance pour le saboteur instruit : le maximum des scores d'action sépare mieux que leur somme ; pour l'organisme sans consigne à dose 1 : {etat_s100} ». L'argument `phrase_i` est retiré de l'appel.
  - La ligne `S100` « accumuler bat » garde le contrôle à adaptateur égal, comme le texte.
- **VB6-5** :
  - les en-têtes de `__init__.py`, `etats_v1.py`, `phrases_v1.py`, `garde_v1.py` et `lecture_v1.py` nomment le candidat 2 (`0716d3d5…`, chemin visé `prereg/accumulation-barreau6-v1.md`) comme texte joué ;
  - `__init__.py` nomme aussi `code_accb6_v1` ;
  - l'annotation du déclencheur « trop beau » dit « (les neuf jeux qui reçoivent un état, témoins et jeux croisés compris) », comme CP-17. Le mot « trop beau » est gardé ; aucun état ne change.
- **Énumération v2** (nom neuf, R12) : `scripts/enumeration_etats_accb6_v2.py` (texte = candidat 2, section « Code ») et sa sortie `scripts/enumeration-etats-accb6-v2.txt`, chacun avec un compagnon. La v1 du script et sa sortie (`d7b6fa08…`, `3bde500f…`) restent versées telles quelles : elles portent le brouillon 2 et les anciennes phrases. Méthode et transcription des règles inchangées.
- **Essais** :
  - `tests/test_accb6_phrases_texte_v1.py` (neuf) : trois essais, détaillés au § 5 ;
  - `tests/test_accb6_etats_v1.py` (modifié, déclaré) : l'essai de l'énumération rejoue et compare la v2.
- Inchangés : `code_accb6_v1.py`, les autres essais, la logique des états, des gardes et des calculs.

## 4. Empreintes (sha256, au commit `6c98ea20…`)

| fichier | sha256 |
|---|---|
| `src/controle_ia/accumulation_b6/__init__.py` | `eb43e52b98d4d87ccbbc31189b5bb1e873b1b81338c7bb9be66bb9608158276d` |
| `src/controle_ia/accumulation_b6/code_accb6_v1.py` | `2e6c3bb878cbc9996335527f74257cc57392b13d0487fa3bace219a260e55c02` (inchangé) |
| `src/controle_ia/accumulation_b6/etats_v1.py` | `6b8aa2db63cb7931cf554d81c96433f8cab09fe42a3a5edbfcff7b5159aae827` |
| `src/controle_ia/accumulation_b6/garde_v1.py` | `5b91bfaac2ea6f9547056d417a413c990ab6a16c0e056588e8cd8134961a5192` |
| `src/controle_ia/accumulation_b6/lecture_v1.py` | `fa91e3dea00f4dabfc59e40dd8bd47361db6ead44d3876cfa6ccb231f2b175e5` |
| `src/controle_ia/accumulation_b6/phrases_v1.py` | `961ea2b3dd4923a311c3a18b3f8973ac7a58b70c2dd74d66d6597e25c72e633b` |
| `scripts/enumeration_etats_accb6_v2.py` (neuf) | `a6dbfdd85ba2ff0e92fd905ff3f144f5397f7f97990411e0786f1c38605d31d9` |
| `scripts/enumeration-etats-accb6-v2.txt` (neuve) | **`00088af568388a4fbe381b7d80b97883b242013d99c7c5893bde54b9e741873e`** |
| `tests/test_accb6_phrases_texte_v1.py` (neuf) | `ad9076b5fa86a068aead5bfd162094670bc7865c7004fb7501dfcc6ecbdb5823` |
| `tests/test_accb6_etats_v1.py` (modifié) | `8571e6c65d6144bc3cfdfea75e93625f129b17662e473acd94c6038f929d7e97` |
| `tests/test_accb6_code_v1.py` | `a4cc477e51e7e3126d747d2acf2790bd36036444a25f23860c35450ce770c1b8` |
| `tests/test_accb6_garde_v1.py` | `448eb2d3630985ea1224c27b4c39949bb3bdec3fd626c9eaf8c8952e43f4ce53` |
| `tests/test_accb6_lecture_v1.py` | `bd890cd86462d1beb7af73b25e4bd38835f2d4ae126c4fb9550946c80a77fd3d` |
| `tests/test_accb6_relance_v1.py` | `cc458330b2d3b7731c5a571ee71baf0a2e8eedf6a1d0521fbdc521d166ff3a0d` |

## 5. Essais, énumération

- **Essais du paquet** : **171 passed** dans l'arbre recréé (six fichiers `tests/test_accb6_*_v1.py`, 114 s), dont les trois essais neufs :
  - `test_morceaux_recopies_du_texte` vérifie que chaque morceau de phrase recopié dans l'essai figure à l'octet dans le candidat 2. Le texte est lu par `git show 0d641ab3f:…`, empreinte `0716d3d5…` vérifiée ; l'essai est sauté hors d'un dépôt qui porte ce commit. Il a été joué, et il passe, dans l'arbre recréé.
  - `test_chaque_phrase_produite_egale_la_table_du_texte` construit, **depuis ces seuls morceaux**, la phrase attendue des 4 × 9 × 33 = 1 188 cas : gras retiré, « Barreau 6 » sous la forme faible, morceaux joints par « ; », point final. Il la compare à la phrase du code : 0 écart.
  - `test_controles_vb6_1_et_vb6_2` vérifie le contrôle de consigne dans la phrase de (i), l'absence de répétition dans la ligne « (i) « le maximum bat » », et le contrôle `T100` gardé dans la ligne `S100` « accumuler bat ».
- **Énumération v2** : sortie `00088af5…`. Bilans inchangés : 1 152 couples, 343 jeux, 33 issues de séquence, 604 phrases, 0 cas sans état, 0 cas sans phrase. Hors en-tête, 74 lignes de phrases changent par rapport à la v1 : 67 portent maintenant « contrôle de consigne » (60 phrases de (i), 7 lignes « (i) « accumuler bat » »), et 7 lignes « (i) « le maximum bat » » n'ont plus la répétition. Ce sont les 74 phrases relevées par la vérification.
- **Rendu déclaré là où la table ne fixe pas le mot** (écrit dans l'en-tête de l'essai neuf ; inchangé depuis le premier rapport) :
  - « [S100 … d*] » : doses franchies entre accents graves, jointes par « , », suivies de l'état de la dose d'arrêt « écrit à côté » ;
  - « ([nom], [famille]) » de (ii) : sondes en A, par dose franchie ;
  - « échec (motif) » : motifs nommés ;
  - « non interprétable : … sépare au moins autant » : suivi, entre parenthèses, des prédicteurs nommés (« nommé »).

  Si le texte veut cette dernière phrase sans les noms, un couple suffit.
- **Non rejoués** :
  - les essais de T0.7 : aucun fichier qu'ils lisent n'est touché ;
  - l'essai hors suite aux constantes réelles : le calcul n'a pas changé.

## 6. Banc de mutations (copies seulement, `-o pythonpath=`, import tracé, deux processus)

- **71 mutations, 71 tuées** en un seul passage, sur une copie de l'arbre du commit : les 67 d'avant, plus P01 à P04.
- Aucun disque plein ; import tracé dans la copie pour toutes les mutations. Comme avant, l'essai de l'énumération est désélectionné dans le banc, et le script v2 est rejoué à part.
- Scripts du bac à sable : `banc_accb6_v4.py` (`e30a3c2f…`), `mutations_accb6_v4.py` (`83822ee5…`) ; résultats `banc-v4.jsonl` (`1b29025f…`).

| id | ce qui est éprouvé (`phrases_v1.py`) | issue | premier essai en échec | énumération v2 |
|---|---|---|---|---|
| P01 | phrase de (i) en « accumuler bat » sur l'ancien corps (`T100`) | tuée | `test_chaque_phrase_produite_egale_la_table_du_texte` | 60 lignes différentes |
| P02 | ligne « (i) « accumuler bat » » sur l'ancien corps | tuée | `test_chaque_phrase_produite_egale_la_table_du_texte` | 7 lignes différentes |
| P03 | répétition remise dans la ligne « (i) « le maximum bat » » | tuée | `test_chaque_phrase_produite_egale_la_table_du_texte` | 7 lignes différentes |
| P04 | « (B6-D3, B6-D3b) » tronqué | tuée | `test_chaque_phrase_produite_egale_la_table_du_texte` | 67 lignes différentes |

## 7. Points ouverts

1. **`CODE-ACCB6` au commit `6c98ea20…`** : fichier, scellement et ligne à faire par la mère, avec l'entropie tranchée (§ 1). Une ligne déjà inscrite pour un commit antérieur n'est jamais réécrite, et la garde exige exactement une ligne `CODE-ACCB6`. C'est un nœud de procédure pour la mère, comme dans le complément 2.
2. **Candidat 3** (voie (a), pas 3 de la vérification), hors sections gelées :
   - commit `6c98ea20…` ;
   - sortie de l'énumération `00088af5…` ;
   - script `a6dbfdd8…` (nom neuf `enumeration_etats_accb6_v2.py`) ;
   - « 171 essais » et « 71 mutations sur 71 » ;
   - ce complément aux documents qui font foi.
3. **Restent ouverts** :
   - de la vérification : VB6-3, VB6-4 et VB6-6, non bloquants et hors du code ;
   - des rapports précédents : rejouer la suite de T0.7 dans un arbre complet ; modules hors du paquet non contrôlés par `CODE-ACCB6` ; R-B6-DIR sur jouet.

## 8. Refus d'un contrôle

Aucun refus d'un contrôle de permissions ou de sécurité pendant cette suite.
