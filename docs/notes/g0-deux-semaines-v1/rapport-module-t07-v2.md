# Rapport du développeur — module de lecture de T0.7 `src/controle_ia/t07/`, v2 (réalignement sur le brouillon 11)

- Écrit le 2026-11-08, de 18:00 à 18:35 UTC environ (`date -u`), par un développeur neuf (Claude Opus 5.5, sous-agent de la session
  mère), qui n'a écrit ni les brouillons de T0.7, ni leurs contre-lectures, ni le premier état du module (rapport v1,
  `rapport-module-t07-v1.md`, gardé tel quel, R12). Aucun brouillon ni aucun fichier scellé modifié ; aucun compagnon `.sha256`
  écrit (ce rapport n'est pas scellé) ; aucun commit, aucune poussée par le développeur ; aucune dépense ; aucune donnée réelle lue.
- **Texte suivi : le brouillon 11** `brouillons/T0.7-sondes-v0-v1-brouillon11.md`
  (`b833d7ccd916b1889e24635303a92cb37a95885346c30c93da27b41064816ef3`, vérifié par `sha256sum`) et son annexe
  `brouillons/T0.7-sondes-v0-v1-brouillon11-pieces/grille_l_t07_brouillon11.py` (`b18da38a6e3a7a1580f252fcdd97498da6d0ed7ddc0177bfd9e9fa37153c3077`),
  sortie brute `grille-l-t07-brouillon11.txt` (`275e2a030a23344d8120420c2fe0b0f4c51538c5d0cfe9b100e3121bffbeceda`). Le script,
  rejoué par `python3 -I -B` depuis un répertoire étranger : code 0, 11 s, sortie d'empreinte égale à `275e2a03…`.
- Point de départ : commit `ad3179f8` (module aligné sur le brouillon 9). Les fichiers du module sont **modifiés en place** (même
  nom `_v1`), comme l'avait fait le premier développeur entre les brouillons 7, 8 et 9 ; le premier état reste dans l'historique
  git (`ad3179f8`). Si la session mère tient à R12 au sens strict pour du code jamais lancé sur des données, elle renomme en `_v2`.
- Méthode : `diff` brouillon 9 / brouillon 11 et script 9 / script 11 ; lecture intégrale des sections « Règle « mots et coût » »,
  « Seuil », « Plan » (point 8), « Critères de lecture gelés », « Liste d'arrêt », « Lignes de registre », « Module »,
  « Concordance », « Reste », constats de cl4.

## 1. Fichiers changés et empreintes (`sha256sum`, après la dernière passe d'essais)

Voir la table en fin de rapport (section 6), recopiée de `sha256sum` après la passe finale.

## 2. Ce qui change dans le module (brouillon 9 → brouillon 11)

| sujet | premier état (brouillon 9) | état réaligné (brouillon 11) | lignes du brouillon 11 |
|---|---|---|---|
| entrée Q | étiquette M1 à M4 du fichier, aiguilleuse | **classe dérivée** à six valeurs `absente`, `non_calculable`, `incoherent`, `vide`, `partiel`, `complet` ; étiquette comparée et recopiée, jamais aiguilleuse | 479-505, 885-892 |
| `deriver_classe` | `filtrer_doses_qualifiees`, incohérence = arrêt | `criteres_v1.deriver_classe(issue, p064)`, ordre de `deriver` : (1) écarts **internes** seuls (dose hors de S25 à S100, état recalculé, argmax, sur une dose « réussit » ou « échoue ») → L7c ; (2) une dose non calculable → L7b quelles que soient l'étiquette et la liste ; (3) étiquette ≠ recalculée **ou `doses_qualifiees` ≠ doses « échoue »** → L7c ; (4) doses jugées (P-064) → vide, partiel, complet | 491-503, 1215-1229 |
| grille | 15 lignes, 46 080 cas | **16 lignes** (L7c ajoutée entre L7b et L6), ordre R11, R12, L0a, L0b, L0c, L1, L1b, L7, L7b, L7c, L6, L4, L4b, L5, L2, L3 ; `regles` recopiée du script 11 | 873, 918-935 |
| champs du fichier | 7 champs par dose, toute anomalie = arrêt | 12 champs par dose (`aire_n029`, `aire_mots_et_cout`, `niveau`, `n_permutations`, `effet_cout` ajoutés) ; **`null` permis** sur les sept champs d'une dose « non calculable » (ni vérifiés ni recalculés) et sur `effet_cout` ; `null` ailleurs, clé absente, valeur hors domaine, dose manquante → **fichier illisible : Q = absente, L1, motif écrit**, jamais un arrêt ; dose en plus → L7c | 1141, 1209-1214 |
| `effet_cout` | — | `null` = effet non établi : dose qualifiée non jugée, marquée « qualifiée, effet du coût non calculable : non jugée » | 501, 1141, 1239 |
| P-064 | — | clé de configuration **`p064`** exigée (booléen, vrai au défaut) | 1192, 1231 |
| ex aequo des deux aires | — | l'une ou l'autre base acceptée, réserve « ex aequo non réglé par T0.6 » écrite (le module ne peut pas lire une règle de T0.6 qui n'est pas sur `main`) | 486-488, 1220-1221 |
| scores de (ii) | ouverts en descriptif sous L7 et L7b | ouverts **sous Q ∈ {vide, partiel, complet} seulement** ; sous Q ∈ {non calculable, incohérent}, `ouvrir_scores` retire les lignes de S25 à S100 de chaque tableau dès le chargement ; ouverture journalisée avec les conditions retirées | 521-525, 819-822, 1239-1242 |
| (i-a) sous L7, L7b, L7c | « hors jugement », à 95 % | **lu au niveau décisif** (T7-P1), rapporté sans issue du critère 3 | 509, 523, 654-656 |
| phrases gelées | brouillon 9 | recopiées de la table du brouillon 11 : L7 avec ses deux sous-phrases exclusives, L7b (dose nommée), L7c (champs nommés), L4 « par dose jugée », L4b et L5 « dose nommée », L2 « (i) jugé sans le filtre de N-063 », mentions des doses non jugées, réserve gelée de M3 sous Q = complet ; phrase P-065 pour (i-a) | 506-528, 920-935 |
| code de sortie de L7 | 4 | **0** | 1320-1322 |
| résultat | — | `resultat.doses` : Q, `p064`, doses qualifiées, jugées, hors jugement, non calculables, dérivation complète (états écrits et recalculés, bases recalculées, `champs_en_ecart`), marque de chaque dose, qualification de S100, deux étiquettes, écart sonde moins base par dose jugée ; `sous_phrase_L7` ; `scores_ii_ouverts`, `conditions_retirees` | 1277-1291 |
| commande `grille` | une énumération | les trois énumérations (624 ; 55 296 ; 11 762 496 cas sur 625 968 configurations) | 1319 |

## 3. Essais

- Commande : `PYTHONPATH=src timeout 900 python -m pytest -q tests/test_t07_lecture_v1.py` (environnement `.venv`) : résultat
  en section 6. Durée observée ≈ 3 minutes sur la machine chargée (charge ≈ 7,5 sur 4 cœurs). L'essai sauté est celui du rapport
  v1 (miroir de Mahalanobis contre `sondes/familles_v2.py`, absent de `main`).
- **Égalité au script du brouillon 11, sur tous les cas qu'il énumère** :
  - `test_grille_par_classes_egale_au_script_du_brouillon11` : les **55 296 cas** par classes, cas par cas : `regles` égale, première
    ligne égale, sous-phrase de L1b égale ; effectifs égaux à `grille_classes()` du script ;
  - `test_agregation_egale_au_script_et_exemples_du_texte` : les **624** agrégations, plus les exemples de la l. 1255 ;
  - `test_deriver_classe_egale_a_deriver_du_script_sur_625968_configurations` : les **625 968 configurations**, chacune rendue en
    fichier par l'essai lui-même (constructeur indépendant de celui du module), lue par `valider_issue_mots_et_cout`, classée par
    `deriver_classe` : (Q, doses qualifiées, doses jugées) égaux à `deriver` ; écarts de champs énumérés source par source (aucun,
    dose hors, état, argmax) ; priorité de L7b vérifiée à part ; sous-phrase de L7 égale ; effectifs des classes égaux à la sortie ;
  - `test_grille_par_etats_par_dose_egale_au_script_cas_par_cas` : les **11 762 496 cas**, **énumération complète** (pas un
    échantillon : 39 s), chacun classé par le module (Q de `deriver_classe`, `agreger_doses` sur les doses jugées du module,
    `ligne_applicable`) et par le script (`deriver`, `agreger_doses`, `regles`, `premiere`) : même ligne à chaque cas ; effectifs
    égaux à ceux de la sortie brute `275e2a03…` ;
  - `test_enumerations_du_module_egales_a_la_sortie_du_script` : `enumerer_derivation` (commande `grille`) rend les effectifs de la
    sortie brute ; le script rejoué rend une sortie d'empreinte `275e2a03…` ;
  - `test_empreintes_du_brouillon_11_et_de_ses_pieces` : brouillon, script et sortie à leurs empreintes.
- **Essais R5 demandés par le brouillon 11** (l. 1246-1264), un par point, cas sain et artefact : M1 aux quatre doses → vide, L7,
  « aucune dose qualifiée », aucune aire décisive de (ii) (bout en bout, espion sur `lecture_jeux`) ; dose 0 présente → L7c ; M2
  aux quatre « réussit » → L7c ; M2 avec une dose non calculable → L7b (sain : la dose échoue → partiel) ; **M4, dose non calculable,
  liste vide → L7b** et liste qui contient la dose → L7b ; dose non calculable à champs `null` → L7b, artefact `null` sur une dose
  « échoue » (chacun des sept champs) → illisible ; `bas` = `quantile_plancher` → L7c ; argmax faux → L7c ; ex aequo → pas L7c,
  réserve écrite ; clé manquante, dose manquante, valeurs hors domaine → illisible, **L1 de bout en bout sans `arret-etape-b.json`** ;
  P-064 vrai et faux ; deux doses qualifiées sans effet → L7, « doses qualifiées sans effet de coût établi » ; `effet_cout` `null`
  → dose non jugée, marque « effet du coût non calculable » ; **L7b et L7c (dose 0, étiquette fausse) de bout en bout : aucune
  condition S25 à S100 vue par la lecture** (artefact : espion), `conditions_retirees` et journal des ouvertures ; M2 avec S100
  hors jugement → S100 absente des lectures décisives, présente en T7-P17, qualification écrite ; (i-a) jugé, phrase P-065 écrite ;
  commande `etape-b` sous L7 → code 0.
- Les essais du premier état (registre, Mahalanobis, plancher, gardes d'ouverture et d'identité, replis, configuration, aucune
  moyenne ni médiane sur les jetons) sont gardés, adaptés aux classes neuves.
- La suite complète du dépôt n'a pas été lancée (consigne : essais du module seuls, machine chargée).

## 4. Les neuf questions du rapport v1 (section 5)

1. **Statut des lignes de l'étape B — non tranché : `MARQUEUR-QUESTION-1`** (`registre_v1.py`, commentaire au-dessus de
   `EXIGEES_ETAPE_B` ; renvoi dans `lecture_v1.etape_b`). Le brouillon 11 dit encore les deux : « clés exigées : […]
   `SCELLEMENT-P3BIS`, `VERDICT-P3BIS`, `RUN-CONFIRMATION-T06`, **`ISSUE-MOTS-ET-COUT-T06`** (N-063 : la règle de T0.6 est
   préalable ; absente → L1, rien n'est lu) » (l. 804-806 ; aussi l. 1125-1126) et « Une ligne de registre exigée absente […] :
   **aucune ouverture** » (l. 963-964, code 2, rien écrit), contre L0a « ligne `SCELLEMENT-P3BIS` ou `VERDICT-P3BIS` absente »
   (l. 922) et L1 « ligne `ISSUE-MOTS-ET-COUT-T06` absente » (l. 925), qui écrivent une issue. Comportement gardé du premier état
   (permises ; L0a ou L1 écrites, code 0), sans le trancher.
2. **Fichier « mots et coût » mal formé — tranché : Q = absente, L1, motif écrit, jamais un arrêt.** l. 1209-1214 : « empreinte
   fausse, clé absente, valeur hors du domaine (les `null` permis exceptés […]), dose manquante parmi `S25`, `S50`, `S75`, `S100` →
   **fichier illisible**, rendu comme **Q = absente** (ligne **L1**, motif écrit dans `lecture-t07.json` ; CLT7C-08), jamais un
   défaut silencieux et jamais un arrêt sans ligne » ; « une dose en plus (dose 0 ou autre) n'est **pas** un fichier illisible :
   elle est passée à `deriver_classe`, qui rend « incohérent » ». Appliqué (`lire_issue_mots_et_cout`, `valider_issue_mots_et_cout`).
3. **Docstring de l'annexe — tranché, corrigé dans le script du brouillon 11** : « 4 × 4 + 6 × 16 + 4 × 64 + 1 × 256 = 624 cas »
   (`grille_l_t07_brouillon11.py` l. 5-6 ; brouillon l. 901-902). Rien à faire dans le module.
4. **Code de sortie de L7 — tranché : 0.** l. 1320-1322 : « Codes : **0** étape menée au bout, résultat scellé ; **2** refus […] ;
   **3** `GardeArret` après le manifeste […] ; tout autre code = défaut de chaîne, consigné. » Le code 4 est retiré
   (`lecture_v1.main`).
5. **Niveau des doses hors jugement — tranché : 95 %** : « T7-P6, T7-P9, T7-P10, T7-P16, **T7-P17**, T7-P19 : lectures
   descriptives ou de témoin, **à 95 %** » (l. 663-665) et « les autres doses ne sont lues qu'au titre de T7-P17 (descriptif) »
   (l. 1236-1237). **(i-a) sous L7, L7b, L7c — tranché : au niveau décisif** : « Pour T7-P1 et pour chaque dose jugée de T7-P2,
   correction de Bonferroni sur les sondes lues […] chaque intervalle au niveau 1 − 0,05/4 = 98,75 % » (l. 654-656), T7-P1 étant
   « rapportée » sous L7 (l. 509, 927) et « faite » sous L7b et L7c (l. 523, 820-821). Changement : le premier état lisait (i-a) à
   95 % sous L7 et L7b.
6. **Source de l'entrée F — non tranché : `MARQUEUR-QUESTION-6`** (`lecture_v1.lire_fuites`). Le texte ne dit que « **F**, fuite
   nommée par l'audit R7a ou R9a sur un jeu décisif » (l. 896-897, l. 930) ; il ne nomme ni ligne de registre, ni fichier, ni clé
   de configuration ; de plus l'audit R7/R9 vient « avant tout verdict » (l. 943, 947) alors que `lecture-t07.json` est scellé
   « avant toute lecture humaine » (l. 841-842). Clé de configuration `audit_fuites` gardée.
7. **Covariance du plancher des sondes figées — non tranché : `MARQUEUR-QUESTION-7`** (`lecture_v1.charger_jetons_entrainement`).
   Le texte cite toujours `jetons-principales-p3.npz` (`4cd2ddb8…`) « ou recalculée à l'identique, égalité d'empreinte exigée »
   (l. 584-587, l. 1184-1185) sans répondre au constat du rapport v1 (ce fichier porte des scores par jeton, pas des activations).
   Non revérifié ici (aucune donnée lue).
8. **`familles_v2.py` — non tranché : `MARQUEUR-QUESTION-8`** (`mahalanobis_v1.py`, sous le docstring). En-tête l. 197-199 :
   « `sondes/familles_v2.py` (`4fea2c52…` au commit `8cb539f9`, **pas sur `main`** : à fusionner ou à citer au commit) ».
9. **Clé neuve dans le registre partagé — tranché : refus.** l. 1116-1119 : `lire_registre_t07` a « mêmes refus : ligne manquante
   parmi les exigées, ligne en double, mal formée, non strictement antérieure, sceau faux, **clé ni exigée ni permise** ». Une clé
   de T0.8 fait donc refuser T0.7 tant qu'elle n'est pas déclarée permise (comportement déjà en place, inchangé ; conséquence à
   connaître pour la session mère qui partage `registres/scellements-v1.md`).

Marqueurs laissés dans le code : `MARQUEUR-QUESTION-1` (`registre_v1.py`, `lecture_v1.py`), `MARQUEUR-QUESTION-6`, `-7`
(`lecture_v1.py`), `-8` (`mahalanobis_v1.py`). `grep -rn MARQUEUR-QUESTION src/controle_ia/t07/` les liste.

## 5. Écarts vus entre le brouillon 11 et son script, et interprétations déclarées

Écarts du texte ou du script (aucun ne change une ligne sur les cas énumérés ; tous déclarés pour le rédacteur) :

1. **Ordre de `doses_qualifiees`** : le script compare des listes ordonnées (`liste != qualifiees`) ; le texte dit « diffère des
   doses « échoue » » (l. 499, 1226). Le module compare les listes telles qu'écrites, dans l'ordre : une liste juste mais dans un
   autre ordre (`["S100", "S75"]`) donne L7c. À confirmer (ensemble ou liste).
2. **Marques des doses non jugées** : la table des critères (L7, l. 927 ; L2, l. 934) n'en nomme que deux (« hors jugement… »,
   « qualifiée, sans effet de coût établi : non jugée ») ; la section « Module » (l. 1238-1239) en nomme une troisième,
   « qualifiée, effet du coût non calculable : non jugée ». Le module écrit les trois.
3. **Valeurs attendues sans règle** : `n_permutations` (200), `seuil_aire` (0,70), `niveau` sont écrits avec leur valeur attendue
   (l. 1141) mais ni le texte ni le script ne disent ce que donne une autre valeur (incohérent ? illisible ?). Le module exige
   seulement un domaine (entier positif ; nombre dans [0, 1] ; nombre dans ]0, 1[) et recalcule l'état avec le `seuil_aire` écrit.
4. **Champ `aire` contre l'aire de la base décisive** : rien ne vérifie que `aire` égale l'aire moyenne de la base décisive
   (`aire_n029` ou `aire_mots_et_cout`) ; ce n'est pas une source d'écart interne du texte ni du script. Non vérifié par le module.
5. **Champs non nuls d'une dose non calculable** : le texte dit que les sept champs « valent `null` et ne sont ni vérifiés ni
   recalculés » ; une valeur non nulle n'est ni permise ni interdite. Le module les ignore (ni vérifiés). `niveau`,
   `n_permutations` et `seuil_aire` ne sont pas dans la liste des `null` permis : `null` → illisible, même sur une dose non
   calculable (lecture littérale, essai versé). T0.6 pourrait écrire `null` là aussi : à confirmer.
6. **Ouverture des scores de (ii) sous L1b** : la règle est écrite par classe, « sous Q ∈ {non calculable, incohérent} (L7b, L7c),
   aucun score de (ii) » (l. 1239-1242), mais ces classes mènent à L1b sous A1b, A2, A3. Le module applique la règle par classe
   (aucun score de (ii) sous L1b avec ces Q) : lecture la plus fermée.
7. **Phrase de « gain » de T0.6** (plan 8 bis, l. 835-837 ; L2) : à recopier par dose jugée, mais aucun champ du fichier
   `ISSUE-MOTS-ET-COUT-T06` ne la porte (l. 1141). Le module écrit l'écart (aire de chaque sonde principale au-dessus moins `aire`)
   et « non recopiée : le brouillon 11 ne fixe pas le champ qui la porte ».
8. **Portée du script** : sa grille (3) fixe A = A4 (« A5 suit le même chemin du code ») et ne croise pas la dérivation avec L1b ;
   le module ne dépend pas de A dans `deriver_classe`, donc l'égalité tient ; noté pour mémoire. La docstring du script dit
   « sous-phrases de L1b et de L7 énumérées » pour la grille (2) : celles de L7 le sont dans la grille (3).
9. **Règle d'ex aequo de T0.6** : le texte renvoie d'abord à « la règle de T0.6 » ; le texte scellé de T0.6 n'étant pas sur `main`,
   le module applique toujours le repli (« l'une ou l'autre acceptée, réserve écrite »). Si T0.6 fixe une règle, il faudra la porter.

Interprétations du développeur (hors des neuf questions) : `doses_qualifiees` doit être une liste de textes (sinon illisible) ;
`p064` est exigée dans la configuration (pas de valeur implicite) ; l'étiquette recalculée est écrite aussi sous L7c d'étape 1
quand aucune dose n'est non calculable (pour le rapport seulement) ; `ouvrir_scores` lit les lignes de (ii) depuis le `.npz` (le
format ne permet pas de les sauter) mais les retire avant de rendre quoi que ce soit (réserve écrite dans la docstring).

## 6. Empreintes et bilan final des essais

Passe finale, `PYTHONPATH=src timeout 900 python -m pytest -q tests/test_t07_lecture_v1.py` : **91 passés, 1 sauté, 0 échoué**
(92 collectés ; 358 s à la première passe, 123 s à la passe finale, 2026-11-08 vers 18:50 UTC ; la passe finale suit
l'ajout de `sys.dont_write_bytecode` dans `_script_grille`, pour que l'import du script n'écrive aucun `__pycache__` dans le dossier
des pièces du brouillon 11 : le dossier créé par la première passe a été retiré). Empreintes `sha256sum` des fichiers à cet instant :

| fichier | sha256 | état |
|---|---|---|
| `src/controle_ia/t07/__init__.py` | `792bfa4372aef38d4fddc27a3393026a7398d8f3f3124c99a18df9b28c7173b7` | modifié (docstring) |
| `src/controle_ia/t07/criteres_v1.py` | `bc99ea4ff71fd8f41baaecea37368a69df9f41fa0f8356922ccc4d5f7ff7b7ae` | réécrit (grille 11, `valider_issue_mots_et_cout`, `deriver_classe`, phrases, énumérations) |
| `src/controle_ia/t07/lecture_v1.py` | `1f99b1cdeb42f409e141392021b219e567ec654acfd4be3d0ef296ae312c7bf9` | modifié (étape B, `lire_issue_mots_et_cout`, `ouvrir_scores`, `p064`, codes, `grille`) |
| `src/controle_ia/t07/mahalanobis_v1.py` | `2234f1441197227d29b7e6b7b1de781aea3996b8f5771db91b56a1c293947c1b` | marqueur 8 seulement |
| `src/controle_ia/t07/registre_v1.py` | `6aec8f68135cced6658f19ec61d48915abc47d078b8229ab59c81d524bff9253` | marqueur 1 seulement |
| `src/controle_ia/t07/plancher_v1.py` | `ac6e8263293ed30c807ef91f8eab0adbcbf8e1b91d5e4c56e73dbffa1a7099dc` | inchangé |
| `tests/test_t07_lecture_v1.py` | `832a38f930e06c7946c4e5452f1308e9297e131cfd0c774166e4a4885e5262b6` | modifié |
| `docs/notes/g0-deux-semaines-v1/rapport-module-t07-v2.md` | empreinte donnée par la session mère au scellement | neuf (ce rapport) |
