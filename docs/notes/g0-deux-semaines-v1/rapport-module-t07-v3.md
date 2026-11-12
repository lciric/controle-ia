# Rapport du développeur — module de lecture de T0.7 `src/controle_ia/t07/`, v3 (réalignement sur le brouillon 14)

- Écrit le 2026-11-08, de 19:58 à 20:45 UTC environ (`date -u`), par un développeur neuf (Claude Opus 5.5, sous-agent de la session
  mère), qui n'a écrit ni les brouillons de T0.7, ni leurs contre-lectures, ni les états précédents du module (rapports v1 et v2,
  gardés tels quels, R12). Aucun brouillon ni aucun fichier scellé modifié ; aucun compagnon `.sha256` écrit (ce rapport n'est pas
  scellé) ; aucun commit, aucune poussée par le développeur (la session mère a pris des instantanés en cours de travail :
  `91aece0a`, `72be6999`) ; aucune dépense. Une seule donnée réelle lue : l'index du fichier léger des planchers de P3
  (`donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz`, `701f73bd…`, demandé par la consigne), par `lire_sondes`.
- **Texte suivi : le brouillon 14** `brouillons/T0.7-sondes-v0-v1-brouillon14.md`
  (`fe7b4e6dbc77edecf56bb16baf24e54939e0f845a76927e144a7f0409fd09345`, vérifié par `sha256sum`) et son annexe
  `brouillons/T0.7-sondes-v0-v1-brouillon14-pieces/grille_l_t07_brouillon14.py` (`e916bea034c0bb2b04b34aca73a35391421aac0b235bb23a977d644156e551de`),
  sortie brute `grille-l-t07-brouillon14.txt` (`0cfef5b28725fc7407f0b941ad1c26da7d4ae5263cda0c126d0e6185417bf68f`) ; le script,
  rejoué par `python3 -I -B` (essai `test_enumerations_du_module_egales_a_la_sortie_du_script`), rend une sortie d'empreinte
  `0cfef5b2…`.
- Point de départ : le module aligné sur le brouillon 11 (commit `fa2b1902`, rapport v2). Les brouillons 12, 13 et 14 sont tous
  portés (le paragraphe « Changements du module imposés par les brouillons 13 et 14 », l. 1705-1723, liste les points (i) à (ix) ;
  ceux du brouillon 12 viennent de sa table « du 11 au 12 », l. 87-97, et de la section « Module », l. 1441-1610). Fichiers
  **modifiés en place** sous leurs noms `_v1` (consigne ; l'historique git garde les états précédents).

## 1. Ce qui change dans le module (brouillon 11 → brouillon 14)

| point | changement | où (module) | brouillon 14 |
|---|---|---|---|
| (i) | table A, fichier d'issue de P3-bis et fichier d'audit lus **dans la garde** (`ouvrir`), avant le manifeste et avant tout `try` de `etape_b` ; refus code 2 sans écriture | `lecture_v1.ouvrir`, `lire_table_A`, `lire_issue_p3bis`, `lire_fuites` | l. 1706-1709 |
| (ii) | table A hors de A1 à A5 (ou nulle) → A = « illisible », **L1 écrite**, code 0 (plus de `GardeArret`) ; fichier absent ou sans `table_A.ligne` → refus | `lire_table_A` | l. 1063-1064, 1412-1413, 1709-1710 |
| (iii) | `VERDICT_P3BIS` retirée de `PERMISES_ETAPE_A` ; sa présence à l'ouverture de l'étape A est refusée (règle (0), `REFUSEES_ETAPE_A`, avec `SCORES-T07` et `SONDES-T07` : étape déjà jouée) ; `exiger_anteriorite` inconditionnelle (`apres` absente → refus) | `registre_v1` | l. 1393-1403, 1710-1712 |
| (iv) | F lue dans le fichier cité par **`AUDIT-FUITES-T07`** (clé de configuration `audit_fuites` retirée, refusée si présente) ; domaine de chaque champ ; `consigne` comparée à la ligne **`CONSIGNE-AUDIT-FUITES-T07`** (exigée, strictement antérieure à l'audit) ; seul le **domaine** de `separation` ([0,70 ; 1]) est vérifié ; F = (i), (ii) (dose **jugée**), les deux, aucune ; une fuite sur une dose non jugée est rapportée sans effet | `criteres_v1.valider_audit_fuites`, `entree_F` ; `lecture_v1.lire_fuites` | l. 992-997, 1432, 1712-1715 |
| (v) | règle du registre partagé : (1) ligne à quatre cellules, date au format, première cellule hors de la forme de clé → refus, toute autre ligne non conforme ignorée ; (2) exigée ou permise ; (3) marque d'une autre tâche de `marques_autres_taches` → ignorée et comptée, **sauf** nom sans marque ∈ {`SCELLEMENT-JEUX-JD`, `-JC`, `-JA`} → refus ; (4) toute autre clé → refus ; clés ignorées nommées dans le manifeste (`cles_ignorees_etape_a`), `sondes-t07.json` et `lecture-t07.json` | `registre_v1.lire_registre_detail`, `classer_cle_inconnue`, `marques_de`, `retirer_marque` | l. 1363-1392, 1715-1717 |
| (vi) | `controle_aire` (« egalite », « recalcul »), `tolerance_aire` (5 × 10⁻⁴ exigé), `marques_autres_taches` (liste de marques, sans T07) dans `exiger_configuration` ; contrôle du champ `aire` à l'étape 1 de `deriver_classe` : égalité exacte à l'aire de la base décisive écrite, ou \|`aire` − aire recalculée\| > `tolerance_aire` + 10⁻⁹ → L7c ; recalcul de l'aire moyenne des deux plis depuis les scores de la base (`aires_recalculees_t06`) ; fichier des scores à empreinte fausse → refus | `lecture_v1.exiger_configuration`, `verifier_scores_base_t06`, `aires_recalculees_t06` ; `criteres_v1.deriver_classe` | l. 608-615, 1430, 1717-1718 |
| (vii) | journal : **une** ligne `\| REFUS-T07 \| date \| etape-A/<run> ou etape-B/<run>/<run-t07> \| clés ou fichiers manquants ou fautifs : motifs \| registre <sha256> \|` écrite après **tous** les contrôles de la garde (motifs joints ; lignes du registre lues sans faute gardées pour les contrôles suivants) ; `OUVERTURE-T07` seulement si la garde passe | `registre_v1.journaliser_refus` ; `lecture_v1.ouvrir` | l. 1643-1651, 1718-1720 |
| (viii) | `diag/<run-t07>/lecture-t07.json` ou `arret-etape-b.json` présent → refus de la garde avant toute ouverture des scores (plus de lecture suivie d'un `arret-etape-b.json`) | `ouvrir` | l. 968-971, 1186-1188, 1720-1722 |
| brouillon 13, B-1 (b) | `SCELLEMENT-P3BIS`, `VERDICT-P3BIS`, `ISSUE-MOTS-ET-COUT-T06`, `AUDIT-FUITES-T07`, `CONSIGNE-AUDIT-FUITES-T07` **exigées** à l'étape B ; valeurs « absente » / « absent » de P, A, Q remplacées par « illisible » (ligne présente, fichier illisible) ; MARQUEUR-QUESTION-1 retiré | `registre_v1.EXIGEES_ETAPE_B` ; `criteres_v1.P`, `A`, `Q`, `regles` | l. 1060-1083, 1404-1408 |
| brouillon 12 | `null` interdit sur `etat`, `niveau`, `n_permutations`, `seuil_aire` ; `null` **exigé** sur les sept champs d'une dose non calculable ; `n_permutations` = 200, `seuil_aire` = 0,70, `niveau` = niveau de T0.6 (sinon illisible) ; liste `doses_qualifiees` comparée en liste ordonnée (déjà le cas) ; « phrase de gain de T0.6 : non recopiée (aucun champ ne la porte) » ; T7-P2 « non lue : scores de (ii) fermés par Q » sous L1b avec Q ∈ {non calculable, incohérent} | `criteres_v1.valider_issue_mots_et_cout`, `PHRASES`, `lecture_v1._prediction_ii` | l. 1430, 1514-1517, 1139, 1147 |
| brouillon 14, R-1924 (2) | phrases de L1, L7b, L7c : issues finales sous ce texte, lecture de (ii) par une version neuve du préenregistrement | `criteres_v1.PHRASES` | l. 1138, 1141-1142 |
| marqueur 7 | planchers des deux sondes figées de P3 : les **directions de P3** lues dans le fichier léger (`planchers_p3`, `701f73bd…` en mode réel) par `figees.lire_sondes`, noms dans `meta.planchers`, nombre (`n_plancher`, 200 exigé en mode réel), couche et agrégation de la principale vérifiés, principale du fichier léger à la même empreinte ; `charger_jetons_entrainement` ne lit plus que les jetons des sondes **neuves** ; graine de plancher seulement pour elles ; source du plancher écrite dans l'index | `lecture_v1.charger_planchers_p3`, `charger_jetons_entrainement`, `noter`, `etape_a` | l. 705-736, 1480-1482 |
| marqueur 8 | `mahalanobis_v1.py` miroir de `familles_v2.py` **cité au commit** `8cb539f9` ; en-tête réécrit, annotation `sonde: SondeMahalanobis` rétablie dans `en_produit_matriciel` (écart non permis relevé par l'essai de miroir) | `mahalanobis_v1` | l. 293-305 |
| (0 bis) | lignes `SCORES-T07` et `SONDES-T07` datées de la **fin** de l'étape A (`max(horloge(), instant + 1)`), plus de l'ouverture ; `VERDICT-P3BIS` inscrite pendant l'étape A → `GardeArret` (`arret.json`, code 3, motif « nœud : étape A non aboutie avant VERDICT-P3BIS »), lignes non écrites | `etape_a` | l. 26-30 du script, l. 1189-1190, 1401-1402 |
| grille (3) | sources « aire » et « liste à l'envers » ; 1 041 984 configurations, 7 776 impossibles, 18 439 488 cas ; contrôles « aire » et liste à l'envers hors de « incohérent » | `criteres_v1.issue_de_configuration`, `enumerer_derivation`, commande `grille` | l. 1107-1117 |

## 2. Essais

- Commande (consigne) : `PYTHONPATH=src timeout 1500 python -m pytest -q -p no:cacheprovider --basetemp=<scratchpad>/pytest-t07-v3
  tests/test_t07_lecture_v1.py` (environnement `.venv`) ; bilan en section 5. Suite complète du dépôt non lancée (consigne).
- **Égalité au script du brouillon 14, énumérations complètes** :
  - (0) `test_garde_ouverture_B_enumeration_0_egale_au_script` : les **2 048 cas** (neuf entrées exigées × `lecture-t07.json` ×
    `arret-etape-b.json`) posés réellement sur un faux run après l'étape A (registre réécrit, fichier `lecture-cout-t06.json`
    retiré, fichiers posés), chacun passé à la **garde du module** (`lecture_v1.ouvrir`, étape B) : décision égale à
    `garde_etape_b` du script ; sous refus, une seule ligne `REFUS-T07`, aucune `OUVERTURE-T07`, aucun fichier écrit sous `diag/`,
    `runs/`, `donnees/<run-t07>/` ; sous ouverture, une seule `OUVERTURE-T07` ; **511 relances** (ouverture, puis refus une fois la
    lecture posée) et **1 024 tentatives après un code 3** (refus) ; bilan du script lui-même égal (0 défaut). **Portée** : la
    garde du module, pas l'étape B entière à chaque cas ; l'écriture unique de `lecture-t07.json` par l'étape B entière (code 0,
    puis troisième tentative refusée par la garde) est éprouvée par `test_B1_absence_refus_code_2_puis_relance_sur_le_meme_run`
    sur sept absences (les cinq lignes de P3-bis, de l'issue et de l'audit, le fichier `lecture-cout-t06.json`, la table A).
  - (0 bis) `test_garde_d_ordre_A_enumeration_0_bis_egale_au_script` : les **6 cas** (trois ordres de oA, fA, V × étape A déjà
    jouée), chacun sur un faux run neuf, étape A réelle (V inscrite pendant l'étape A par un espion sur `noter`) : refus de
    l'étape A si et seulement si le script la refuse ; étape B possible (garde de l'étape B passée) si et seulement si fA < V ;
    issues comptées égales à `verifier_ordre_a` du script (1, 3, 1, 1).
  - (1) 624 agrégations ; (2) **55 296 cas** par classes (`regles`, première ligne, sous-phrases de L1b, effectifs) ; (3)
    `test_derivation_et_grille_par_etats_par_dose_egales_au_script_cas_par_cas` : les **1 041 984 configurations**, chacune rendue
    en fichier par l'essai (constructeur indépendant de celui du module, **une seule source d'écart par configuration**,
    vérifiée), lue par `valider_issue_mots_et_cout` et classée par `deriver_classe` : (Q, doses qualifiées, doses jugées) égaux à
    `deriver` ; puis les **18 439 488 cas**, énumération complète, même ligne qu'au script à chaque cas ; effectifs des classes et
    des lignes égaux à la sortie brute `0cfef5b2…` ; `enumerer_derivation` (commande `grille`) égale à la sortie. **Classement des
    grilles (1) à (3) égal**, comme exigé.
- **Essais R5 des brouillons 12 à 14** (section « Dérivation de Q », l. 1554-1609, et « Gardes et essais R5 », l. 1673-1703), un
  cas sain et au moins un artefact chacun : `aire` égale / différente d'une unité du dernier chiffre (égalité) ; recalcul à
  4 × 10⁻⁴ (pas L7c), 6 × 10⁻⁴ (L7c), frontière 0,735 écrit contre 0,7345 recalculé (pas L7c), plus un cas où l'écart binaire
  dépasse 5 × 10⁻⁴ (0,502 contre 0,5015) couvert par la marge 10⁻⁹ ; scores de la base à empreinte fausse → refus ; recalcul de
  bout en bout → L2 ; liste `["S100", "S75"]` → L7c ; `niveau`, `n_permutations`, `seuil_aire`, `etat` nuls sur une dose non
  calculable → illisible ; valeur non nulle sur chacun des sept champs d'une dose non calculable → illisible ; 199, 0,65, niveau
  autre → illisible ; L1 de bout en bout pour ces fichiers ; audit sans fuite → F = aucune ; fuite sur `saboteur` → L6, F = (i) ;
  sur une dose jugée → L6, F = (ii) ; sur S25 hors jugement → F = aucune, rapportée, L2 ; dix-sept artefacts de domaine du fichier
  d'audit (clé en plus, `fuite` vide ou d'espaces, `trait` hors des quatre, `trait` sans `fuite`, `separation` 0,69, `true`,
  `"0,8"`, nulle sous une fuite, `motif` vide, consigne différente, majuscules, clé en plus, jeu manquant) ; `CONSIGNE-AUDIT-FUITES-T07`
  absente, postérieure à l'audit, fichier d'audit non JSON, chemin d'audit autre → refus ; L1b avec Q incohérent → aucun score de
  (ii) (espion) ; planchers de P3 : 200 directions (sain), empreinte fausse, 199 directions, couche 7 → arrêt, et fichier réel
  `701f73bd…` (200 et 200 directions, couche 15, maximum, `meta.complet` = `91b61c45…`) ; règle du registre partagé :
  `JEUX-CONTROLE-T08`, `SCELLEMENT-T08`, `SCORES-T08`, `SCELLEMENT-T06` ignorées et comptées (et nommées de bout en bout dans le
  manifeste, `sondes-t07.json`, `lecture-t07.json`), `SCELLEMENT-JEUX-T7-JD`, `SCORES-T07A`, `XYZ-T07`, `AUTRE-CLE`,
  `SCELLEMENT-JEUX-T08-JD` (et `-T06-JC`, `-JA-P3BIS`) → refus, première cellule hors forme → refus, titre et séparation ignorés ;
  B-1 (sept cas) ; P3-bis illisible ou à valeur inconnue → L0a, scores non ouverts (espion) ; M-A : `lecture-t07.json` présent →
  refus sans ouverture des scores (espion) ; code 3 réel puis relance → refus, `lecture-t07.json` jamais écrit ; `VERDICT-P3BIS`
  présente à l'ouverture de l'étape A → refus, une `REFUS-T07`, rien d'écrit ; m-01 vérifié dans chacun de ces essais (forme exacte
  de la ligne, aucune `OUVERTURE-T07` sous refus) ; table A hors de A1 à A5 ou nulle → L1, code 0, pas d'`arret-etape-b.json`.
- **Miroir de Mahalanobis** (`test_mahalanobis_miroir_egal_a_familles_v2_au_commit_8cb539f9`, brouillon 12, l. 1581-1582) :
  fichier lu par `git show 8cb539f9:src/controle_ia/sondes/familles_v2.py`, empreinte `4fea2c52…` et 94 lignes vérifiées ; arbres
  syntaxiques comparés nœud à nœud, docstrings retirées, aux cinq écarts déclarés près ((b) import, (c) `mahalanobis_v2` et
  `entrainer_v2`, (d) `sonde` et `empreinte` du compte rendu, (e) `preparer_sonde` et `__all__`) ; puis la classe du fichier cité,
  chargée dans le paquet, rend les mêmes scores et le même compte rendu. **L'essai sauté du rapport v2 est levé.** L'essai a
  d'abord relevé un écart non déclaré (annotation de type retirée dans `en_produit_matriciel`), corrigé dans le module.
- **Contrôle de symétrie (R4)** sur les deux essais de garde neufs : deux mutations jouées hors du dépôt (dossier de travail,
  supprimé) — table A jamais refusée ; `VERDICT-P3BIS` permise à l'étape A — font échouer respectivement l'essai (0) et l'essai
  (0 bis), comme attendu. Un essai neuf était faux à la première passe (cas « sain » du fichier d'audit mal construit) et a été
  corrigé ; aucune autre correction des essais après la première passe.
- Essais gardés du premier état et du rapport v2 (registre, égalité des refus à `controle_lecture_t06_v1.py` sur les deux clés
  communes, plus le cas d'une clé d'une autre tâche ignorée par les deux ; Mahalanobis ; `comparer_scores_au_plancher` ; gardes
  d'identité, de forme, de configuration ; aucune moyenne ni médiane sur les jetons), adaptés.

## 3. Marqueurs `MARQUEUR-QUESTION-n`

Tranchés par le brouillon 14 et **retirés du code** : **1** (statut des lignes de l'étape B : exigées, refus code 2 ; B-1 (b)),
**6** (source de F : ligne `AUDIT-FUITES-T07`), **7** (planchers des sondes figées : directions de P3 du fichier léger), **8**
(`familles_v2.py` cité au commit `8cb539f9`, essai de miroir). Marqueurs **neufs**, non tranchés par le texte, laissés dans le code
(`grep -rn MARQUEUR-QUESTION src/controle_ia/t07/*.py`) :

- **9** (`lecture_v1.verifier_scores_base_t06`) : le format du fichier des scores par action des bases de T0.6, sous
  `controle_aire` = « recalcul », n'est fixé nulle part (le texte renvoie au texte scellé de T0.6, `<<CONTROLE_AIRE_T06>>`) ; le
  module porte un format **provisoire** (`.npz`, par dose : `d__condition`, `d__tache`, `d__N-029`, `d__mots_et_cout`), plis lus
  dans le champ `plis` du fichier « mots et coût » (`{tâche : 0 ou 1}`) ;
- **10** (`lecture_v1`, au-dessus de `CLES_CONFIG_RETIREES`) : le texte ne nomme pas les clés de configuration qui portent la valeur
  attendue de `niveau` (`<<NIVEAU_BASE_T06>>`) ni le fichier des scores de la base ; le module les lit dans `niveau_base_t06` et
  `scores_base_t06` (nul exigé sous « egalite »), noms du développeur ;
- **11** (`lecture_v1.lire_table_A`) : avec `diag/<run>/arret.json` de T0.6 présent, le texte exige encore `lecture-cout-t06.json`
  et sa table A (absents → refus, « attente ») ; si T0.6 arrêté n'écrit pas ce fichier, l'étape B attend sans fin au lieu d'écrire
  L1. Le module suit la lettre.

## 4. Interprétations et écarts déclarés (hors marqueurs)

1. **Datation des lignes de fin d'étape A** : le premier état datait `SCORES-T07` et `SONDES-T07` de l'**ouverture** de l'étape A ;
   avec une inscription de `VERDICT-P3BIS` pendant l'étape A, l'antériorité à `VERDICT-P3BIS` aurait été tenue à tort (cas
   oA < V < fA de l'énumération (0 bis)). Elles sont datées de la fin (`horloge`, paramètre pour les essais). Une inscription de
   `VERDICT-P3BIS` détectée à la fin de l'étape A donne un **arrêt** (`arret.json`, code 3, « nœud ») sans lignes ; le texte dit
   « nœud » sans fixer ce que fait le module : choix du développeur.
2. **Chemin du fichier d'audit** : la ligne `AUDIT-FUITES-T07` doit citer `diag/<run-t07>/audit-fuites-t07.json` (l. 1432), comme
   les chemins de `SCORES-T07` et `SONDES-T07` ; autre chemin → refus.
3. **Tous les contrôles de la garde sont joués** avant la ligne `REFUS-T07` (lecture la plus large de « après tous les contrôles ») ;
   les contrôles qui dépendent d'une ligne absente ou fautive sont sautés, le motif de la ligne suffit. Les sondes figées sont
   relues **dans la garde** de l'étape A (refus code 2 journalisé, au lieu d'une erreur après la ligne `OUVERTURE-T07`). Une faute
   de configuration (`exiger_configuration`) précède la garde : code 2, motif imprimé, **non journalisée**.
4. **Clé portant à la fois `T07` et la marque d'une autre tâche** : traitée comme une clé de T0.7 inconnue (refus) ; le texte ne
   prévoit pas ce cas.
5. **Valeurs exigées** : `tolerance_aire` = 5 × 10⁻⁴ exactement ; `n_plancher` = 200 en mode réel ; `n_permutations` entier 200
   (`200.0` est refusé) ; `ligne` du fichier d'issue de P3-bis entier non booléen.
6. **Constat pour le rédacteur (m-02)** : l'exemple du texte, « aire exacte 0,7345 écrite 0,735 », donne en binaire un écart de
   4,999…4 × 10⁻⁴, **sous** 5 × 10⁻⁴ : il passe même sans la marge 10⁻⁹. La marge sert ailleurs (par exemple 0,502 contre 0,5015 :
   5,000…6 × 10⁻⁴) ; les deux cas sont essayés.
7. **Énumération (3)** jouée sous `controle_aire` = « egalite » (le script ne compare pas les nombres, l. 61-62) ; le recalcul est
   couvert par les essais R5 et un essai de bout en bout.
8. **Essai de miroir sans repli** : si le clone ne contient pas le commit `8cb539f9` (clone superficiel sur l'instance), l'essai
   **échoue** (il n'est pas sauté). L'ordre d'exécution de l'étape A sur l'instance (« suite d'essais figée du module », l. 1736-1738)
   doit donc cloner avec cet historique, ou la session mère décide d'un saut déclaré. L'essai d'égalité à `controle_lecture_t06_v1.py`
   reste sauté si la branche `origin/prep/t06-candidat8-v1` manque (inchangé ; elle est présente ici).
9. Gardés du rapport v2 sans changement : règle d'ex aequo de T0.6 (repli « l'une ou l'autre », réserve écrite) ; scores de (ii)
   lus depuis le `.npz` puis retirés avant tout calcul ; réplique « (0) et (0 bis) rejouées par les essais » imprimée par la commande
   `grille`, qui n'énumère que (1) à (3).

## 5. Empreintes et bilan final des essais

Passe finale, commande de la section 2 : **139 passés, 0 sauté, 0 échoué** (139 collectés ; 179,6 s, de 20:30:07 à 20:33:07 UTC). Le dossier `--basetemp` est supprimé après la passe ; aucun
`__pycache__` écrit dans le dossier des pièces du brouillon 14 (vérifié). Empreintes `sha256sum` à cet instant :

| fichier | sha256 | état |
|---|---|---|
| `src/controle_ia/t07/__init__.py` | `553bd9d29b56f0923859da2d3a63fadf9891c4274b9bb23fc367496e77e5a61e` | modifié (docstring) |
| `src/controle_ia/t07/criteres_v1.py` | `12b999fecce093372a29fb70d8c11eb7fe965f34c8746a31b399baaecc5ae8c5` | modifié (valeurs « illisible », domaine du fichier « mots et coût », contrôle de `aire`, audit des fuites, F, phrases, grille (3)) |
| `src/controle_ia/t07/lecture_v1.py` | `62b34790346123924c275c4e2021ea31db26837c5b7840e9e047d272a54c9678` | réécrit (garde complète, journal REFUS-T07, étape B, planchers de P3, configuration, datation de fin d'étape A) |
| `src/controle_ia/t07/mahalanobis_v1.py` | `b28163062aa8d39cf3894b327a7446f63d50d4f1394eac894b16b4da8ff962f9` | modifié (en-tête, marqueur 8 retiré, annotation rétablie) |
| `src/controle_ia/t07/registre_v1.py` | `914b8f374ce8f8bc6550d03c34c5f6c2a97ac93b8ce44da24fd88229185ffca0` | réécrit (clés par étape, règle du registre partagé, refus relevés ensemble, journal des refus) |
| `src/controle_ia/t07/plancher_v1.py` | `ac6e8263293ed30c807ef91f8eab0adbcbf8e1b91d5e4c56e73dbffa1a7099dc` | inchangé |
| `tests/test_t07_lecture_v1.py` | `ae82fe0d606fa22223fa86f846788145b7c436d12fe65c2ddb3359a907329722` | réécrit (139 essais) |
| `docs/notes/g0-deux-semaines-v1/rapport-module-t07-v3.md` | empreinte donnée par la session mère au scellement | neuf (ce rapport) |
