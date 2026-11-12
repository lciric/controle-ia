# Vérification neuve du module v3 — addendum 2 de P3 — lentille « code et mutants »

**Verdict : conforme après corrections.** Le module v3 ne change que les deux endroits demandés (CV2-01 option (b),
CV2-10). Les tests ne changent que pour CV2-01, CV2-02, CV2-03 et CV2-10. La suite passe (121), et le rejeu des
campagnes est identique au rédacteur. Une seule correction est demandée : un test de la garde 6 au lancement. La
réserve du rédacteur sur G6-02 est fondée, et le test est fourni, déjà éprouvé. Quatre points de forme s'y ajoutent.

| id | gravité | constat (une ligne) |
|---|---|---|
| VV3-code-01 | mineur | Garde 6 au lancement : aucun test ne fait lever le chargeur gelé pendant un lancement. G6-02 n'est tué que par la route d'injection du test CV2-10 (un mutant équivalent est « tué » de même ; un repli non converti survit) |
| VV3-code-02 | forme | Garde 7 : le compte de chacune des cinq formes n'est éprouvé que pour `cout_suffixe_k` ; ne plus comparer `cout_milliers_espace` ou `cout_multiplication` passe les 121 tests |
| VV3-code-03 | forme | Déclencheur 3 : « `E0` = 0 » n'est éprouvé qu'à 0 exactement et loin de 0 ; une tolérance (\|`E0`\| < 1e-3 → « non calculé ») passe les 121 tests |
| VV3-code-04 | forme | Précision 14 : le texte ne nomme pas la garde (le module écrit « garde 7 ») et ne dit pas que le module arrête aussi sur une valeur non textuelle ou vide |
| VV3-code-05 | forme | Phrase de durée : exacte au regard de `mesures-duree-v1.txt`, sauf « 2,0 à 2,2 s » (mesuré : 2,048 à 2,146 s, import de `harnais.validation_reelle` et non de la seule bibliothèque de calcul tensoriel) |

En bref. Le rejeu de 23 mutants (15 de la liste du contre-lecteur, 8 du rédacteur) est identique au résultat du
rédacteur pour chacun : même état, mêmes tests en échec, même empreinte de mutant. Mes 30 mutants sur les points
changés : 24 tués et 6 survivants. Parmi ces 6, deux sont équivalents (VV-G7-01 quant à l'arrêt, VV-G7-02 au
lancement) ; les quatre autres donnent VV3-code-01 à 03. Le différentiel de comportement donne des sorties v2 et v3
identiques sur 19 scénarios synthétiques, sauf « degenere » (part en échec), et seulement sur les clés admises. Sur
le déclencheur 3, v1 et v3 donnent le même résultat sur 621 cas construits. R1 : 0 refus partout.

## Constats détaillés

### VV3-code-01 (mineur) — Garde 6 au lancement : conversion des exceptions du chargeur non éprouvée

- **Réserve du rédacteur** (`NOTES-MODULE-v3.md`, section « Mutants du contre-lecteur ») : G6-02 est « tué par effet de bord ».
  Il n'échoue qu'à `test_CV2_10_SF_sans_principales_arret_ecrit`, qui injecte sa panne en remplaçant
  `exiger_garde_6`. Ma réponse à la question posée : **oui, il faut un test qui éprouve la conversion au lancement.**
- **Preuve.**
  - Les quatre tests de la garde 6 appellent `m.exiger_garde_6` ou `av.exiger_garde_6` directement : tests v3,
    `_chargeur_qui_leve` (l. 1968-1973, artefacts `garde6-KeyError` et `garde6-OSError`, l. 2050-2052),
    `test_garde_6_run_source_non_verifiable` (l. 2658) et `test_garde_6_exception_du_chargeur_convertie` (l. 2684). Aucun ne fait échouer la garde 6 pendant un `_lancer`.
  - **G6-02**, rejoué : tué par le seul test CV2-10 (1 échec sur 121), comme chez le rédacteur.
  - **VV-G6-01**, mutant équivalent voulu : la garde 6 est appelée par un alias, et la conversion reste intacte. Il
    est pourtant « tué », par le même test seul. Ce test vérifie donc la route d'appel, pas le comportement.
  - **VV-G6-02** : `exiger_garde_6` est toujours appelée, mais un arrêt est suivi d'un repli sur le chargeur gelé.
    Au lancement, l'exception nue passe. Ce mutant **survit** (121 passés).
  - Si le test CV2-10 injectait sa panne autrement (par `lecture.charger_source`), G6-02 survivrait de nouveau sans
    que rien ne le signale.
- **Portée sur le run réel** : aucune, car l'arrêt tombe avant le manifeste dans tous les cas et rien n'est écrit.
  Seule la forme du motif change (« garde 6 : … » ou exception nue). Le classement est « mineur » parce que la
  liste d'arrêt demande que chaque garde ait son artefact (R5), et que cet artefact n'est vérifié au lancement que
  par une route d'appel.
- **Correction (mots exacts).**
  1. Ajouter aux tests v3 la fonction suivante, copiée de
     `verification-v3/outils/test_garde6_lancement_propose.py` (sha256 `4148bc5b36cc58adc8ed9c4118a289292e903569cffd1d79bfc274f4b39d6710`).
     Toutes les aides qu'elle utilise sont déjà dans le fichier de tests.
     ```python
     def test_garde_6_au_lancement_exception_du_chargeur_convertie(depot_jetable, monkeypatch):
         """Garde 6 au lancement (vérification du module v3, réserve G6-02) : gardes 1 à 5 réelles passées, puis le
         chargeur gelé (appelé par la seule garde 6) lève une `KeyError` : `GardeArret` de type exact, motif écrit,
         rien d'écrit (arrêt avant le manifeste)."""
         d, m, _ = depot_jetable

         def leve(racine, run_id):
             raise KeyError("scores")

         monkeypatch.setattr(lp, "charger_source", leve)
         run = "20261020-129000-addendum2-p3"
         with pytest.raises(GardeArret, match=re.escape(f"garde 6 : run source {RUN_A} non vérifiable (KeyError : 'scores')")) as e:
             _lancer(d, m, run)
         assert type(e.value) is GardeArret
         assert _rien_ecrit(d, run)
     ```
  2. En tête des tests, remplacer « Nombre de tests attendu : 121 » par « Nombre de tests attendu : 122 ». Avec
     VV3-code-02 et 03 ajoutés, le nombre devient « 128 ».
  3. Dans les notes, remplacer « Je le compte « tué », sans le compter comme couvert » par « G6-02 est tué par
     `test_garde_6_au_lancement_exception_du_chargeur_convertie` ».
- **Épreuve** (`journaux/epreuve-test-garde6-propose.log`) : le test passe sur la base v3 et sur VV-G6-01
  (équivalent). Il échoue sur G6-02, VV-G6-02 et G6-01. Il sépare donc le comportement, pas la route.

### VV3-code-02 (forme) — Garde 7 : compte de chacune des cinq formes

- **Preuve.** `test_garde_7_coherence_cout_et_forme_alteres` (tests v3, l. 369) n'altère que `cout_suffixe_k`.
  Deux mutants survivent :
  - VV-F-01 : le compte de `cout_milliers_espace` n'est plus comparé à [L] `P3-P6` ;
  - VV-F-02 : de même pour `cout_multiplication`.

  Le code de la garde (m. 857 : boucle sur `FORMES`) est juste à la lecture.
- **Portée** : aucune sur le run réel, car [S] et [L] sont épinglées par la garde 2. Depuis CV2-02, le run « sain »
  porte les cinq formes, donc l'épreuve complète ne coûte qu'un paramètre.
- **Correction (mots exacts).** Ajouter le test paramétré `test_garde_7_compte_de_chacune_des_cinq_formes`, copié
  de `verification-v3/outils/test_extensions_proposees.py` (sha256
  `0ddfabf4101cfef92f42c62e0f173c6f1058179bd7e58984cde6f9326a898357`, test 1) : une forme posée sur une action sans
  forme de l'honnête, pour chacune des cinq formes ; arrêt « garde 7 : P3-P6/honnete/<forme> » dans
  `exiger_coherence` et dans la fonction pure.
- **Épreuve** (`journaux/epreuve-extensions-proposees.log`) : le test passe sur la base. Il échoue sur VV-F-01
  (pour `cout_milliers_espace`) et sur VV-F-02 (pour `cout_multiplication`).

### VV3-code-03 (forme) — Déclencheur 3 : bord « `E0` = 0 »

- **Preuve.** VV-D3-04 (`elif abs(pf["E0"]["valeur"]) < 1e-3:`) survit aux 121 tests. Ce mutant fait taire le
  déclencheur exactement là où la part `D / E0` est la plus grande. Le module compare bien `== 0.0` (m. 1093),
  comme le texte (audit, point 3).
- **Portée** : aucune sur le run réel, puisque `E0` de P3-P1 est loin de 0 (CV2-01).
- **Correction (mots exacts).** Ajouter `test_declencheur_3_E0_petit_non_nul` (même fichier, test 3) :
  `audit_symetrie(_faux_L(), _faux_contrastes(0.5, 1e-6), {}, P)` donne `part_hors_bornes.etat` vrai, une part de
  5e5 et un déclencheur vrai.
- **Épreuve** : le test passe sur la base et échoue sur VV-D3-04.

### VV3-code-04 (forme) — Précision 14 face au code

- **Texte** (brouillon 5, l. 468) : « Un [SF] sans `principales` arrête avec un motif écrit, jamais par une exception
  nue ».
- **Code** (m. 408-421) : le motif est « garde 7 : run source hors de forme : [SF] sans `principales.<c>` ». L'arrêt
  vaut aussi pour une valeur absente, non textuelle ou vide, et pour une source sans [SF]. Le module v2 rendait
  `None`, `3` ou `""` sans arrêt (`journaux/differentiel-v1-v2-v3.log`, partie [3]).
- **Mutants.**
  - VV-G7-01 (nom vide accepté) survit, mais il est équivalent quant à l'arrêt : le module muté arrête par la garde 9
    (« clé absente de la lecture décisive : P3-P3/ »), avant le manifeste (`journaux/equivalence-g7.log`).
  - VV-G7-02 (accès direct à `sondes-figees`) survit, mais il est équivalent au lancement : `lecture.charger_source`
    rend toujours cette clé, ou arrête (`lecture.py` l. 116-124).
- **Correction (mots exacts)**, au texte, précision 14 : « 14. Un [SF] sans `principales`, ou dont
  `principales.tromperie` ou `principales.enjeux` est absente, non textuelle ou vide, arrête avant le manifeste
  avec un motif écrit (garde 7, « run source hors de forme »), jamais par une exception nue (brouillon 5,
  CV2-10). »
- **Correction facultative**, aux tests : ajouter à la liste des pannes de `test_CV2_10_SF_sans_principales_arret_ecrit`
  le cas `("enjeux", lambda sf: sf["principales"].__setitem__("enjeux", ""))`.

### VV3-code-05 (forme) — Phrase de durée face à `mesures-duree-v1.txt`

Le fichier est vérifié : sha256 `c16ace64…191ba`, égal à son compagnon. Confrontation, chiffre par chiffre, avec la
phrase des notes (l. 225-229) :

| élément de la phrase | fichier | état |
|---|---|---|
| « environ 5,5 s », « de 5,4 à 5,7 s sur quatre mesures » | 5,403 ; 5,464 ; 5,399 ; 5,672 s (moyenne 5,48) | exact (arrondi à 0,1) |
| 60 tâches, 4 conditions, 10 pas, 600 actions par condition, 430 sondes, cinq formes, 10 000 tirages, processus séparé | en-tête et lignes « ligne de commande complète » | exact |
| « dont 3,2 à 3,4 s d'imports » | 3,279 ; 3,224 ; 3,379 ; 3,223 s, mesurés dans un processus qui ne fait qu'importer | exact ; la mesure est faite par un processus témoin |
| « surtout la bibliothèque de calcul tensoriel, tirée par `harnais.validation_reelle` : 2,0 à 2,2 s » | `controle_ia.harnais.validation_reelle` : 2,146 ; 2,068 ; 2,105 ; 2,048 s | **borne haute arrondie vers l'extérieur** : l'arrondi au plus proche donne 2,0 à 2,1 s, et le tableau des notes dit 2,05 à 2,15 s. La grandeur est l'import de `validation_reelle` en entier (`torch` l. 53, plus des modules `harnais` qui importent `torch`) ; la bibliothèque seule n'est pas mesurée |
| « 0,45 à 0,52 s pour la fonction pure » | 0,515 ; 0,453 ; 0,483 ; 0,505 s | exact |
| « ≈ 683 Mio (≈ 717 Mo) » | 699 668 à 699 980 Kio = 683,3 à 683,6 Mio = 716,5 à 716,8 Mo | exact |
| chemin et empreinte (R6) | `<chemin du fichier versé>/mesures-duree-v1.txt`, `c16ace64…` | exact ; chemin à remplir au versement |

L'outil (`mesure_duree_v3.py`, `545d5334…`, lu) mesure bien ce qu'il annonce : durée murale de la vraie commande
dans un processus séparé, mémoire `ru_maxrss` du processus par `os.wait4`, imports en trois parts dans un processus
témoin.

**Correction (mots exacts).** Dans la phrase proposée, remplacer « dont 3,2 à 3,4 s d'imports (surtout la
bibliothèque de calcul tensoriel, tirée par `harnais.validation_reelle` : 2,0 à 2,2 s) » par « dont 3,2 à 3,4 s
d'imports, mesurés dans un processus qui ne fait qu'importer (surtout `harnais.validation_reelle`, qui importe la
bibliothèque de calcul tensoriel : 2,05 à 2,15 s) ». Le reste de la phrase ne change pas.

## Cadre

- **Vérificateur.** Je suis neuf : je n'ai écrit ni l'addendum 2, ni aucune version du module ou de ses tests, ni
  aucune contre-lecture, vérification ou note antérieure. Travaux le 2026-10-20, de 19:58 à 21:13 UTC.
- **Écritures.** J'ai écrit seulement sous `…/scratchpad/addendum2-p3/verification-v3/` : `base/`, `outils/`,
  `journaux/`, `mutants/`, `garde6/`, `extensions/`, `equivalence-g7/` et ce rapport. Le dossier `tmp/`, qui
  contenait les dépôts jouets, est supprimé. Les dossiers `texte/` et `verification-module-v3-texte-v1.md` sont
  ceux d'une vérification parallèle ; je ne les ai ni lus ni touchés.
- **Dépôt de travail**, en lecture seule.
  - Lancements avec `python -B`, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`, `--basetemp` et `TMPDIR` sous
    `verification-v3/tmp/`, depuis la racine du dépôt, `PYTHONPATH=src`, interpréteur de la consigne.
  - git est lu sans verrou (`--no-optional-locks`). `git status --porcelain` est vide au début et à la fin.
  - La tête passe de `c52225b` à `98a95de` : ce sont les commits de la session, qui ne touchent que
    `registres/decisions.md` et `registres/go.md`. `src/` et `tests/` sont égaux au commit cité `7a54d43` aux deux
    têtes.
  - Aucune recherche récursive dans le dépôt. Code gelé lu : `lecture.py` l. 100-140 et les lignes d'import de
    `harnais/validation_reelle.py`, `modeles.py`, `activations.py`, `episode.py`, `formats.py`, `politique.py` et
    `stockage.py`.
- **R1.**
  - Tables synthétiques seulement. Aucune grandeur de B1, de B2 ni de l'addendum 2 n'a été calculée sur les données
    réelles de P3.
  - Ni `prereg/P3-consignes-v1.md`, ni un fichier `textes-actions-*`, ni `donnees/`, `diag/`, `runs/` ou `traces/`
    du dépôt n'ont été ouverts. Aucune commande Vast.ai, aucun réseau, aucun service payant.

## Empreintes vérifiées (avant lecture ; aucun écart)

| pièce | sha256 |
|---|---|
| brouillon 5 | `db53d140d5a8d000d0d9f444a86215a9cd15e0fbdaa3f764c41facf3a5889a1f` (= compagnon) |
| contre-lecture du module v2 | `8c2902e4d1b8bfdbdfa5c8066eedd2ea526e24e73a9387ac4990665b72a07737` (= compagnon) |
| module v3 / tests v3 | `967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d` / `d0c5eb07da17a1bf27fc38905edd648e4653ba9f3652076560ee4c4c3ba83b28` |
| `NOTES-MODULE-v3.md` / `mesures-duree-v1.txt` | `7283bc515af02f79c0a1e693654cfa5fe772ea1be03af3f254714c41e8d44756` / `c16ace640bd273ce073c384292771da946d2d3ec1dfee1be07b47c69115191ba` |
| module v2 / tests v2 / module v1 | `dfdeef6b4652a9faad06cecd708385341f044ec4164efade1f82a4a1cf6e7a3d`, `a5c6ec3412c04a1e7e3af8bb1ebb168c22a3aab40b7111821d24558523dc92fd`, `0b991450d107ee16b484a568d91f95ca232b5079d42ae17b6c52ec2bd23369cf` |
| tous les compagnons `.sha256` de `module-v3/` (journaux, outils, campagnes) | `sha256sum -c` : tous OK, au début et à la fin |
| liste du contre-lecteur `mutants_v2.py` ; script du rédacteur `controle_survivants_v3.py` ; garde R1 `garde_r1_v2b.py` et son épreuve | `d9c038e6…dfadf03c` ; `90e582f7…152768b` ; `022cfd55…0bac4f` ; `21dc8e56…6d7af` |

Toutes ces pièces ont aussi été retrouvées inchangées à la fin.

## A. Différentiel v2 → v3

**Module** (`diff -u`) : deux blocs, et rien d'autre.

1. `principales_du_run` (m. 408-421) : CV2-10. La lecture est gardée, et chaque cas donne une `GardeArret`
   « garde 7 » au lieu d'une exception nue.
2. `audit_symetrie` (m. 1088-1100) : CV2-01, option (b). La branche `elif pf["part"]["etat"] != CALCULE` est
   retirée et le commentaire est réécrit. Le code est égal au v1 (`module/`, l. 1039-1050) hors commentaire.

Les notes disent « trois blocs » : c'est le compte avec `diff -U0`. Avec le contexte par défaut, il y en a deux ;
c'est sans effet. Aucun autre changement de code.

**Tests.** Chaque bloc du différentiel se rattache à un constat :

- CV2-01 : nouveau test `test_CV2_01_…` ; tests `test_garde_15_…` et `test_audit_part_hors_bornes_…` adaptés.
- CV2-02 : `PROBAS_SAIN`, avec les deux formes à 2 % chez l'honnête et le témoin, et le scénario « sain ».
- CV2-03 :
  - `ecarts_au_recalcul` étendu (`_part_texte`, `_comptes_texte`, classements, M6, M7, M8, M9, M10, audit) ;
  - nouveau test `test_M6_…` ;
  - `consigne` à `None` ;
  - `PHRASE_ARRET` écrite à la main, dans trois tests ;
  - constantes du texte écrites à la main ;
  - 100 tirages dégénérés.
- CV2-10 : nouveau test `test_CV2_10_…`.
- En-tête : 121 tests.

Pas de changement hors de ces constats. CV2-04 n'est qu'un fichier de mesures versable, avec son outil.

**Comportement** (`outils/differentiel_v1_v2_v3.py`, journal `journaux/differentiel-v1-v2-v3.log`).

1. Fonction pure v2 contre v3, sur les 19 scénarios synthétiques des tests v3 : sorties identiques sur 18. Sur
   « degenere » (part de P3-P1 en échec), il y a 3 écarts, tous dans les clés admises : `part_hors_bornes` passe de
   « non calculé » à faux, avec part 0.
2. Déclencheur 3, v1 contre v3, sur 621 cas construits et tirés : 0 écart sur l'état, la part, le motif et le
   déclencheur. Ces cas couvrent les états de M5 et de la part, `E0` = 0, les bords ±1 et les cas au hasard.
   Les 25 cas où la part est en échec et hors bornes sont tous déclenchés, avec la consigne. Seule la phrase
   `lecture` diffère entre v1 et v3, et c'est le changement CC-texte-08 du v2. Un premier passage, écarté
   (`…-passage1-ecarte.log`), comptait cette phrase comme un écart.
3. `principales_du_run` : le cas sain est identique. Sur les sept pannes, v3 arrête toujours (« garde 7 »). v2
   levait `KeyError` ou `TypeError`, ou rendait `None`, `3` ou `""` sans arrêt.

## B. Suite

Commande de la consigne, sous la garde R1 v2b, depuis la racine du dépôt, sur la copie de base (`base/`, empreintes
vérifiées) : **`121 passed in 75.49s`** (`journaux/pytest-suite-base.log`). R1 : 0 refus ; 556 ouvertures tracées,
toutes dans mes dépôts jouets (`journaux/r1-suite-base.jsonl`). Le rédacteur trouvait aussi 556.

Avant usage, la garde a été éprouvée (`outils/test_garde_r1_v2b.py`) : 14 tests passés et 17 refus attendus, tous
sur des chemins `__garde_r1_inexistant__` (`journaux/pytest-epreuve-garde.log`, `journaux/r1-epreuve-garde.jsonl`).

## C. Mutants

`outils/lanceur_verif_v3.py` lit les listes comme des données (`ast.literal_eval`, aucun import des fichiers
sources), après en avoir vérifié les empreintes. Chaque mutant passe par la **suite entière** (sans `-x`), sous la
garde R1, trois à la fois, de 20:04 à 21:12 UTC sur une machine chargée par d'autres sessions. Résultats :
`journaux/resultats-mutants-verif-v3.jsonl` ; journal `journaux/campagne-verif-v3.log`. Un dossier par mutant
(`mutants/<id>/`) contient le module muté, la différence, le journal pytest et le journal R1.

**53 mutants : 45 tués, 8 survivants ; 0 refus R1 ; 29 306 ouvertures tracées, toutes dans mes dépôts jouets.**

### Rejeu d'un échantillon (23)

Comparaison dans `journaux/comparaison-rejeu.log`.

- **Liste du contre-lecteur (15)** : DESC-04, 05, 08, 12, 14, V2-14, PHRASE-08, REGLE-01, REGLE-02, G6-01, G6-02,
  G4-02, SEUIL-11, V2-12, G7-05. Pour chacun, l'état, la liste des tests en échec et l'empreinte du mutant sont
  égaux à `module-v3/outils-revue/resultats-mutants-v3.jsonl`. G4-02 et SEUIL-11 survivent comme chez le rédacteur
  (CV2-05). G6-02 est tué par le seul test CV2-10.
- **Mutants du rédacteur (8)** : V3-01, 02, 03, 05, 07, 09, 10, 12. Tous sont tués, avec la même empreinte, et le
  premier échec du rédacteur figure parmi les miens. Le rédacteur arrêtait au premier échec (`-x`) ; moi, non.
- **Comptes des notes reproduits sur leurs fichiers** : 230 mutants, dont 2 sans objet, 215 tués et 13 survivants.
  Aucun mutant tué au v2 ne survit au v3. Les 17 survivants du v2 tués au v3 sont DESC-01, 03, 04, 05, 07 à 14,
  V2-14, PHRASE-08, REGLE-01, REGLE-02 et G6-02. Le test le plus efficace en tue 59 ; 108 mutants ne sont tués que
  par un seul test ; le rédacteur en a 128 tués sur 128. Tous ces nombres sont égaux aux notes.

### Mes mutants sur les points changés (30)

Liste dans `outils/mutants_verif_v3.py` (sha256 `6416f5b7…aa24da7`).

| famille | mutants | tués | survivants |
|---|---|---|---|
| VV-D3 : déclencheur 3, part en échec | 8 : D3 ignoré si la part est en échec ; bornes ±1 exclues ; E0 / D ; tolérance sur E0 ; lecture de la valeur absente ; consigne liée au déclencheur 2 ; ligne de recommandation liée au déclencheur 2 ; « non calculé » déguisé | 7 | VV-D3-04 (VV3-code-03) |
| VV-G7 : [SF] hors de forme | 6 : nom vide ; [SF] absent ; motif « garde 9 » ; sous-classe `NonCalculable` ; ordre inversé ; valeur devinée | 4 | VV-G7-01 (équivalent quant à l'arrêt), VV-G7-02 (équivalent au lancement) |
| VV-F : cinq formes | 5 : garde 7 sans `cout_milliers_espace` ; sans `cout_multiplication` ; R_sf sans `cout_plusieurs_nombres` ; E_-f sur quatre formes ; colonne confondue | 3 | VV-F-01, VV-F-02 (VV3-code-02) |
| VV-DESC : descriptifs | 8 : `n_taches_sf` ; M9 lisibles après ; « instable » sur part en échec ; M7 − 1 ; distance haute ; M8 avec la forme non lisible ; nulles d'origine ; A_80 à la distance basse | 8 | — |
| VV-PH : phrase d'arrêt | 1 : sortie d'arrêt sans `lecture` | 1 | — |
| VV-G6 : garde 6 au lancement | 2 : alias (équivalent voulu) ; repli sur le chargeur | 1 (l'équivalent, par la route : VV3-code-01) | VV-G6-02 (VV3-code-01) |

Les tests changés font leur travail.

- **Part en échec.** `test_CV2_01_…` tue 6 des 8 mutants VV-D3, souvent avec `test_audit_part_hors_bornes_…` ; ce dernier tue aussi VV-D3-02 (bornes ±1), seul.
- **Descriptifs.** `test_bornes_recalculees_hors_du_module` tue les 8 mutants VV-DESC, dont VV-DESC-01 : un
  scénario a bien T_sf ≠ T_∅.
- **Phrase d'arrêt.** Les trois tests qui lisent `PHRASE_ARRET` tuent VV-PH-01.

**Extensions proposées, éprouvées.** Elles sont écrites dans `outils/test_extensions_proposees.py` et
`outils/test_garde6_lancement_propose.py`, et lancées sur des copies de la base et des mutants
(`journaux/epreuve-extensions-proposees.log`, `journaux/epreuve-test-garde6-propose.log`). Toutes passent sur la
base. Chacune échoue sur le mutant qu'elle vise, et sur aucun équivalent. L'extension pour `n_taches_sf` est
devenue inutile, puisque VV-DESC-01 est tué par la suite v3.

## Hors lentille, signalé sans constat

L'en-tête des précisions du brouillon 5 dit : « Règles déjà appliquées par le module là où le texte se taisait ».
Ce n'est plus exact pour deux précisions :

- la 2 renverse une règle du brouillon 4 ;
- la 14 est un arrêt ajouté au module v3, et le module v2 ne l'appliquait pas.

C'est à voir par la vérification « texte ».

## Fichiers rendus (sous `verification-v3/`)

| fichier | sha256 |
|---|---|
| `outils/lanceur_verif_v3.py` | `8e2f194962be3727bc9ebbbb4c1d5f40973824179acb0e69bbbf65228983ba85` |
| `outils/mutants_verif_v3.py` | `6416f5b745dfe420306224b6c5f1bb55e708e4cd422c8f9da273de38daa24da7` |
| `outils/differentiel_v1_v2_v3.py` | `694cab14a4a3ef1b7c2023b9d70682941c479c1eca786a85dc91bc544ef97f21` |
| `outils/test_garde6_lancement_propose.py` | `4148bc5b36cc58adc8ed9c4118a289292e903569cffd1d79bfc274f4b39d6710` |
| `outils/test_extensions_proposees.py` | `0ddfabf4101cfef92f42c62e0f173c6f1058179bd7e58984cde6f9326a898357` |
| `outils/equivalence_g7.py` | `20bc142b9db13bbfa67edf328e8270987a30faaf2b8942706fa78d6524630cc0` |
| `outils/garde_r1_v2b.py`, `outils/test_garde_r1_v2b.py` (copies octet pour octet) | `022cfd55…0bac4f`, `21dc8e56…6d7af` |
| `journaux/resultats-mutants-verif-v3.jsonl` | `e1198615114defa8e77e3b402d4b372a7464bdae2f4eb74b29fcf2c11ab8c24e` |
| `journaux/campagne-verif-v3.log` | `22ff62fa531eb1521947c5ae45c434bd5fa4237d3049764237a4d8f9319f74a4` |
| `journaux/comparaison-rejeu.log` | `163c6a35c1f136ecec7d2cc61d2e513c0d2936d554d19e3fe68e08f5fe9de317` |
| `journaux/differentiel-v1-v2-v3.log` | `cde9f805b1f3db206d208fa546b26ebed8d4d5a03ba4b6890a944afb0281b470` |
| `journaux/pytest-suite-base.log` ; `journaux/r1-suite-base.jsonl` | `b56edd07923c051125eb5dcd956ed90878372f816515cc4929386f6231a0dd65` ; `8bea5e8bdf213830564d4d605f7f2631ad5782670c564732433917c16234555b` |
| `journaux/epreuve-test-garde6-propose.log` | `e920a7924c7d7c9e18ad132377a1bbc23f9509fd94b15752e3f4f882b1cdc860` |
| `journaux/epreuve-extensions-proposees.log` | `66c38c32c0c81ab5f0d78fdc0a387ad5c09af8fd56e86505dcc46b188a76ad34` |
| `journaux/equivalence-g7.log` | `b46c0f79d133fbc5d52f3074ed14d1162657007bd11f7211e06ab628d00655cb` |
| `journaux/pytest-epreuve-garde.log` ; `journaux/r1-epreuve-garde.jsonl` | `ca996134…c609b4` ; `b6babe16…774cb` |
| `journaux/git-head-debut.txt`, `…-fin.txt`, `git-status-debut.txt`, `…-fin.txt` (vides) | `945b346e…`, `e3194cbc…`, `e3b0c442…` |
