# Contre-lecture R2 du module final de l'addendum de P3, angle « pannes » (revue CB3, b3-3)

**Verdict : scellable après corrections.** Un constat majeur (CB3-01), deux mineurs (CB3-02, CB3-03), trois pour
information (CB3-04 à CB3-06). Le majeur se corrige en une dizaine de lignes. Il doit l'être avant le scellement : après
la lecture décisive, le module ne peut plus changer (son empreinte est citée, et la garde 3 refuse un rescellement).
Le reste a tenu : déterminisme entre processus, entrées de la lecture en échec, aucun texte dans la sortie, gardes
d'antériorité sur dépôts jouets, 240 000 textes tirés au hasard sans exception hors garde, durée à taille réelle.

- Relecteur : sous-agent neuf (R2), qui n'a écrit ni le brouillon ni le module. Date : 2026-10-20 (UTC).
- Texte qui fait foi : `addendum-p3/P3-addendum-lecture-complementaire-v1-brouillon3.md` (sha256
  `30a99398313dc3752d4b0eca0c75335103b58b81b23d48cee07e854ff66b130b`).
- Module relu : `addendum-p3/final/complements_p3_v1.py` (sha256
  `daf954594456f8c268ebbf48b14326a183941c00c4cddb205b2e3382a875f4fa`). Tests : `addendum-p3/final/test_complements_p3_v1.py`
  (sha256 `01b5faeaf1fe5ea38624b872948d46d5310bc67b6df3277ea1515e73fc057abc`). Notes : `addendum-p3/final/NOTES-SYNTHESE.md`.
  Empreintes égales à celles des notes ; inchangées pendant la revue.
- Code gelé lu (lecture seule) : `premier_test_ia/lecture.py`, `statistiques.py`, `conditions.py`, `notation.py`,
  `run.py` (l. 260-310, 384-390, 455-470), `figees.py` ; `sondes/evaluation.py`, `sondes/temoins.py` ; `manifeste.py` ;
  `environnements/propositions.py` ; `harnais/validation_reelle.py` (gardes du code cité) ; `prereg.py` ; `gardes.py`.
- Essais : `addendum-p3/rapports/revue-b3-3/` (scripts `essai_NN_*.py`, journaux `essai_NN.log`). Rien n'a été écrit
  ailleurs (vérifié par horodatage contre un repère posé au début : aucun fichier nouveau dans `final/` ni dans le dépôt
  de travail ; `git status` du dépôt vide). Tous les lancements portent `-B` et `PYTHONDONTWRITEBYTECODE=1`.
- Aucune donnée du run réel de P3 (`20261019-230011-p3-reel`) n'a été ouverte (R1).

## Ce qui a été fait

| essai | objet | résultat |
|---|---|---|
| suite complète | 117 tests, depuis le dossier de revue | **117 passed in 633.70 s** (`pytest-complet.log`) |
| 01 | fichier des textes écrit par l'écrivain du run (`run._ecrire_textes`), texte avec U+2028, U+2029, U+0085 | **panne** : CB3-01 |
| 02 | déterminisme : 4 processus séparés, deux `PYTHONHASHSEED`, scénarios « sain » et « a5_bornes » | sorties identiques octet pour octet |
| 03 | lecture décisive aux entrées en échec ou non calculables (formes réelles de `lecture.lire`) : six cas | aucune exception ; garde 6 tenue ; « non lu » et « sans objet » conformes |
| 04 | graines de la fonction pure : clés échangées ; état de contrôle altéré | aucun arrêt dans les deux cas : CB3-04 |
| 05 | marqueurs dans chaque champ, dans le champ du coût, dans une clé en gras, dans une action sans ligne ACTION | aucun marqueur dans la sortie |
| 06 | antériorité sur dépôts jouets : même commit, branche fusionnée après la lecture, compagnon retiré puis rescellé, clone superficiel complet, compagnon renommé, commit abrégé | conforme au texte dans les sept cas |
| 07 | banc à taille réelle (2 400 actions, 430 sondes, 400 jetons par action, textes de 1 850 à 1 900 caractères, 2 000 et 10 000 tirages) | 426,5 s sur un cœur ; mémoire maximale 647 Mo : CB3-03 |
| 08 | 240 000 textes tirés au hasard (gras, casse, puces, REVISE sans numéro, espaces insécables, chiffres non latins) | aucune exception, ni garde ni autre |
| 09 | garde 10 déclenchée dans un dépôt jouet, par la vraie fonction `executer` | arrêt après le manifeste ; second passage refusé : CB3-02 |

## Constats

### CB3-01 — majeur — `charger_textes` coupe les lignes du fichier des textes à de faux sauts de ligne

- **Où** : `complements_p3_v1.py` l. 2001-2007 (`charger_textes`), appelée par `executer` l. 2034, avant le manifeste.
- **Problème** : le run écrit une ligne par action par `json.dumps(x, ensure_ascii=False)` suivi de « \n »
  (`run.py` l. 384-390). Avec `ensure_ascii=False`, les caractères U+2028, U+2029 et U+0085 restent tels quels dans la
  ligne. Le module relit le fichier par `str.splitlines()`, qui coupe aussi à ces trois caractères. Un seul texte
  d'action qui en contient un suffit : la ligne est coupée en deux moitiés illisibles, `json.loads` lève
  `json.decoder.JSONDecodeError`. Ce n'est pas une `GardeArret` : `__main__` ne la rattrape pas (l. 2081), le lancement
  finit sur une trace d'exception, sans motif écrit. Reproduit (`essai_01.log`) :

  ```
  U+2028 : charger_textes lève json.decoder.JSONDecodeError (GardeArret : False) ; lecture par split('\n') : 2 textes, égaux aux écrits : True
  ```

  Le même fichier, lu par `split("\n")`, rend les textes intacts. La lecture décisive n'est pas touchée : elle ne relit
  pas les textes (seulement leur empreinte). C'est l'addendum entier qui tombe, gardes 5 à 11 comprises.
- **Pourquoi majeur** : la panne n'apparaît que sur les textes du run réel, au lancement de l'addendum, donc après la
  lecture décisive. La corriger alors change l'empreinte du module, citée dans le préenregistrement ; un rescellement
  postérieur à la lecture est refusé par la garde 3. L'addendum serait perdu sans nœud de Lazar. La probabilité qu'un
  texte de Llama contienne l'un de ces caractères est faible, mais non nulle, et rien ne la borne.
- **Correction** : lire par octets et par « \n » seulement ; toute erreur devient une garde avec le numéro de ligne :

  ```python
  try:
      lignes = donnees.decode("utf-8").split("\n")
  except UnicodeDecodeError as e:
      raise GardeArret(f"garde 4 : {ep['textes']} : UTF-8 illisible (octet {e.start})") from None
  if lignes and lignes[-1] == "":
      lignes.pop()
  sortie = []
  for i, x in enumerate(lignes):
      try:
          sortie.append(json.loads(x))
      except json.JSONDecodeError as e:
          raise GardeArret(f"garde 4 : {ep['textes']}, ligne {i} : illisible ({e.msg}, colonne {e.colno})") from None
  ```

  (le motif ne recopie aucun texte). Tests, R5 : cas sain, textes avec U+2028, U+2029 et U+0085 relus intacts ;
  artefact, une ligne tronquée donne une `GardeArret` avant le manifeste, rien d'écrit.

### CB3-02 — mineur — la garde 10 et la garde de localisation tombent après le manifeste et consomment le seul passage

- **Où** : `executer` l. 2037-2050 ; `familles_attention` (garde 10) et `localisation` (égalité avec
  `lecture._localisation`) ne sont appelées que dans `analyser_addendum` (l. 1831, 1836), donc après `creer_manifeste`.
- **Problème** : ce sont deux contrôles de données, sans tirage ni lecture de résultat. S'ils se déclenchent, l'arrêt
  est écrit dans la sortie unique, puis la garde 9 refuse tout second passage. Reproduit dans un dépôt jouet construit
  comme le gabarit des tests, avec une seule différence (`agregation` de la sonde à attention écrite « max ») :
  `essai_09.log` — premier lancement : « garde 10 : famille « attention » discordante … ; manifeste créé : True ; écrit :
  lecture-addendum-p3.json » ; second lancement, donnée corrigée ou non : « garde 9 : addendum déjà passé … nœud de
  Lazar ». L'auteur a déjà avancé la garde de cohérence avant le manifeste pour cette raison (notes, § 4, point 1) ; la
  garde 10 et la garde de localisation relèvent du même cas. Le brouillon 3 n'exige que les gardes 1 à 9 avant le
  manifeste ; il n'interdit pas d'en passer davantage. Sur un run réel cohérent, aucune des deux ne devrait se
  déclencher (d'où « mineur »).
- **Correction** : dans `executer`, juste après `exiger_coherence(lecture, d, L)`, appeler `familles_attention(d)` et
  `localisation(d, k)` pour chaque sonde principale ; test, R5 : garde 10 déclenchée par `executer`, rien d'écrit
  (comme `test_gardes_avant_le_manifeste_aucune_sortie`). Si l'on veut la lettre du texte, écrire « gardes 1 à 10 avant
  le manifeste » au point 3 du plan.

### CB3-03 — mineur — le préenregistrement annonce « mémoire de l'ordre de 50 Mo » ; mesuré : 647 Mo

- **Où** : brouillon 3, plan d'analyse, point 9 (« mémoire de l'ordre de 50 Mo (mesures de la contre-lecture R2,
  RA-21) »). Le code n'est pas en cause.
- **Problème** : banc à taille réelle (`essai_07.log`) : mémoire résidente maximale 647 Mo ; le seul import du module en
  prend déjà 564 Mo (`essai_07b_import.log`), parce que le code gelé importé tire `torch` (`notation.py`,
  `validation_reelle.py`, `run.py`). Le chiffre écrit est faux d'un facteur dix. Sans effet sur une machine de 16 Go,
  mais un chiffre non vérifié dans un préenregistrement est interdit. La durée annoncée (« de l'ordre d'une heure »)
  est tenue : 426,5 s sur un cœur, dont A1 327,5 s et A4 63,2 s ; relecture des textes 7,9 s pour 2 400 textes de
  1 900 caractères (la règle (1) est quadratique en longueur de texte, sans conséquence à 400 jetons par action).
- **Correction** : écrire au point 9 « durée mesurée : environ 7 minutes sur un cœur ; mémoire maximale mesurée :
  environ 650 Mo, dont 560 Mo pour les imports du code gelé », avec le chemin et l'empreinte du journal du banc.

### CB3-04 — information — la garde des graines de la fonction pure ne contrôle que l'entropie

- **Où** : `exiger_graines` l. 1799-1806 ; `_rng` l. 239-240.
- **Problème** : deux clés échangées (graines valides, mais d'une autre clé) passent sans arrêt et changent les
  bornes (Δ_ST de 0,1954 à 0,1929, `essai_04.log`). Un état de contrôle altéré lève, dans `manifeste.generateur`, une
  `GardeArret` « graine reconstruite ≠ graine consignée », que `_executer_entree` transforme en « échec » de l'entrée et
  en `reserve_A3_non_lue`, au lieu d'un arrêt. Hors d'atteinte au lancement réel : `executer` passe les graines du
  manifeste qu'il vient de créer.
- **Correction** (facultative) : dans `exiger_graines`, exiger `graines[k] == manifeste.graines(cles_addendum(p),
  ENTROPIE_P3)[k]` pour chaque clé, sinon arrêt.

### CB3-05 — information — le dépôt de travail est aujourd'hui un clone superficiel

- **Où** : garde 3 (`exiger_anteriorite` l. 1981-1982) ; plan, point 1.
- **Constat** : `git -C /home/user/controle-ia-travail rev-parse --is-shallow-repository` rend `true`. En l'état, la
  garde 3 arrêtera l'addendum (comportement voulu, éprouvé par `essai_06.log`, y compris sur un clone superficiel qui
  contient pourtant le commit de scellement). Le point 1 du plan prévoit `git fetch --unshallow` : à faire, et à vérifier
  à travers le mandataire réseau, avant le lancement. Les trois arbres gelés (commit cité par P3, commit cité par
  l'addendum, `HEAD`) sont aujourd'hui égaux (`git diff --quiet` : code 0) : les gardes 1 et 2 sont satisfaisables
  ensemble.

### CB3-06 — information — un `__pycache__` est présent à côté du module final

- **Où** : `addendum-p3/final/__pycache__/complements_p3_v1.cpython-311.pyc` (écrit à 01:50, avant cette revue).
- **Constat** : à ne pas verser sous `docs/procedures/P3-addendum-v1/` (il ferait échouer `verifier-arbre`, notes § 7,
  point 3). Verser les deux fichiers seuls, et lancer les tests du dépôt avec `PYTHONDONTWRITEBYTECODE=1` et
  `-p no:cacheprovider`.

## Ce qui a résisté (aucun constat)

- **Déterminisme** : quatre processus séparés, `PYTHONHASHSEED` 1 et 977 : empreintes de sortie égales
  (`fd187133…11ff` pour « sain », `224c2bb7…cd56` pour « a5_bornes »). Les aires par rangs sont des sommes de
  demi-entiers, exactes quel que soit l'ordre des ex aequo rendu par le tri : rien ne dépend de l'ordre d'un tri.
- **Lecture décisive en échec** (`essai_03.log`) : jeu en échec, tous les jeux d'une sonde en échec, P3-P3 en échec
  (ligne « lecture de P3-P3 en échec »), P3-P2 en échec et mention non calculable (A6 « non lu », `reserve_A6_non_lue`),
  P3-P1 non calculable (« organisme non établi », aucune conclusion), T2 non calculable et T4 en échec : aucune
  exception, verrou tenu.
- **Aucun texte dans la sortie** (`essai_05.log`) : six marqueurs, y compris dans le champ du coût lu par les quatre
  lecteurs ; aucun dans la sortie. Aucun motif de garde du module ne recopie un texte.
- **Règles de A5 et lecteur étendu** (`essai_08.log`) : 240 000 textes tirés au hasard ; aucune exception. Les gardes
  `DefautDuModule` de `regle_bornes_champs`, `regle_lire_action` et `_vers_brut` sont inatteignables par construction
  (même motif que `_nettoyer`, même règle que `lire_action`, position rendue par le tokeniseur par caractères).
- **Antériorité** (`essai_06.log`) : même commit, passe ; branche de scellement fusionnée après la lecture, arrêt ;
  compagnon retiré puis rescellé après la lecture, arrêt (premier ajout, empreinte ancienne) ; clone superficiel,
  arrêt ; compagnon renommé, passe sur le commit de renommage (plus tardif que le vrai scellement, donc prudent) ;
  commit de lecture abrégé, passe.
- **Second passage** : refusé après un passage réussi (tests) comme après un arrêt écrit (`essai_09.log`).
- **Durée** : 7,1 minutes à taille réelle, loin sous l'heure annoncée.

## Fichiers

- Rapport : `addendum-p3/rapports/contre-lecture-code-b3-3.md`.
- Essais et journaux : `addendum-p3/rapports/revue-b3-3/` (`commun.py`, `essai_01` à `essai_09`, `essai_07b_import.log`,
  `pytest-complet.log`, `pytest-tmp/`).
