# Vérification 4 (courte) — corrections de la contre-lecture 3 de la procédure d'extraction de T0.5 — rapport v1

Vérificateur : sous-agent neuf (n'a écrit ni la procédure, ni son code, ni aucune contre-lecture). 2026-10-07, vers 07:00 UTC.
Aucun fichier du dépôt modifié ou créé (bytecode compris : listes des caches avant et après identiques), rien committé ; rien ouvert sous `donnees/` ni `registres/` ; aucun texte de papier lu. Essais dans `<W>` = `…/scratchpad/verification-extraction-v4/` (dépôts jetables construits avec `_depot_de_test`). HEAD est passé de 5b5707d à ecc72ca pendant la vérification ; les fichiers relus sont identiques, octet pour octet, à 5b5707d (`git diff 5b5707d HEAD` vide sur eux).

## Verdict

**Scellable après corrections** — courtes, sans refonte : 0 bloquante, 0 majeure, 6 mineures, 7 suggestions.

- Les corrections E-1, E-2, E-3, E-8, E-10 sont justes et tiennent sur un run sain. Je n'ai trouvé aucune fausse perte en marche normale (étapes refaites, rondes parallèles, tentatives 2 et 3, assemblage, chemins relatifs).
- Avant le scellement (texte) : V-5 et V-6. Mettre aussi à jour les comptes du texte (gardes, tests) si le code change.
- Avant `preparer --tentative 1` (modules épinglés à l'ouverture du run) : V-1 à V-4.
  - V-1 est une faute nouvelle, introduite par la correction d'E-7 ; V-2 et V-3 complètent E-7 et E-6 ; V-4 est le seul mécanisme de fausse perte trouvé.
  - Les quatre correctifs sont éprouvés sur une copie corrigée, hors du dépôt : 130 tests du dépôt + 8 essais, 138 réussis.
- Tous les déclencheurs sont improbables. Mais V-1 à V-3 bloquent un run pour toujours, sans arrêt consigné, et V-4 l'arrête à tort.

## Réponses aux questions

**A. E-1.** Tenu. Aucune exception hors garde pour onze altérations des entrées (au-delà des quatre du test) :
- h10 remplacé par un dossier ;
- h9 en lien vers /dev/zero ;
- `a-verifier/` supprimé ;
- autre contenu JSON valide ;
- fichier ajouté ;
- dossier du papier remplacé par un fichier ;
- partie ou invite modifiée ou supprimée ;
- boucle de liens ;
- lien vers une copie identique (lisible, à raison) ;
- `avis.json` remplacé par un dossier (« fichier.absent », d'accord avec le script).

Une seule exception : un fichier ajouté au nom non UTF-8 (V-1, faute nouvelle due à E-7).

**B. E-2.**

*Faux positifs.* Aucun en marche normale. J'ai éprouvé :
- une validation, puis une lecture, interrompues entre l'archive et le résultat dans `diag/` : l'étape se refait, sans perte ;
- une interruption entre le renommage et le sceau de l'archive ;
- une racine relative puis absolue, et un dossier de travail relatif ;
- les rondes « echantillon » et « theorie » préparées ensemble, lues dans l'ordre inverse ;
- le dossier d'une tentative déjà lue, nettoyé ;
- les tentatives 2 et 3 et l'assemblage (déroulé du dépôt).

Seul mécanisme de fausse perte : une étape lancée depuis une autre copie du dépôt (V-4).

*Faux négatifs.* Aucune lecture de `donnees/` ne précède le contrôle. Restent :
- plusieurs dossiers de papier disparus, le dossier de la tentative restant : exclusions, pas de perte (V-5) ;
- rien ne contrôle `donnees/` après l'assemblage (V-10) ;
- une empreinte compagnon illisible lève une exception hors garde (V-7).

**C. E-8.** Tenu.
- `arret-desaccord-script`, à la validation comme à la lecture, est la seule écriture de l'étape : `donnees/<run>/` n'est pas créé.
- Une seconde exécution, de cette étape ou d'une autre, s'arrête sur « run arrêté », sans réécrire : empreinte et date de l'arrêt inchangées.
- Délai : garde levée, rien d'écrit, et l'étape relancée réussit.
- Limite : un seul `arret-avis-refaits` est consigné par run (V-8).

**D. E-7 et E-10.** Sans effet sur un dossier sain :
- fichiers dans `sorties/` (notes, `h9.json.bak`), notes et `__pycache__/` à la racine, dossier vide sous `papier/`, `avis.json.bak` ;
- retours : chemin relatif et `…/../<run>/` acceptés ; sous-dossier de `donnees/<run>/` et lien vers l'extérieur refusés.

Mais E-7 ne compte que les fichiers réguliers (V-2). Il écrit aussi les noms tels quels dans `diag/` (V-1).

**E. E-3.**
- Le message est le même, au sens près, dans le module et les deux scripts. Les fonctions de contrôle du texte sont identiques entre les deux scripts.
- Codes : 0 écart sur 11 cas réalistes (formule sur deux lignes, « \nu » non doublé, montants…) et sur 200 000 chaînes tirées au hasard (positions comprises).
- Effacer un vrai « \nu » : risque faible. Le conseil est conditionné (« if the paper itself has a line break at this place »), et la barre doublée est proposée d'abord. Dans une citation, l'erreur serait rattrapée par `citation_introuvable`.

**F. Texte et code.** Concordent sur :
- les arrêts : les six noms, leurs suites et les deux arrêts définitifs ;
- la panne de processus ;
- l'emplacement des retours ;
- les options de N-014 (texte seul) ;
- les comptes : 69 gardes (19 + 50), 130 tests.

Écarts : V-5 (« un seul dossier ») et V-6 (retours « scellés »). Nuances : V-2 (panne « qui se relance »), V-8, V-12.

**G.** `tests/test_extraire_t05.py` et `tests/test_extraction.py` : **130 réussis**. Avec un traceur de lignes, les 69 gardes sont exercées, 0 manquante.

## Remarques

### V-1 — mineure (faute nouvelle, due à E-7) — un nom de fichier non UTF-8 laisse un résultat vide dans `diag/` et bloque le run

**Lieu**
- `extraire_t05.py` l. 290-294 (noms ajoutés) ;
- l. 489 et 757 (`"entrees_modifiees": modifiees`, écrit tel quel) ;
- `manifeste.py` l. 137-138 (`write_text`, puis sceau).

**Problème**
- Un fichier ajouté sous `papier/`, `invites/` ou `a-verifier/` avec un octet non UTF-8 dans son nom donne une chaîne à substitut.
- Le message d'anomalie l'échappe ; le résultat de `diag/`, non.
- `ecrire_resultat` lève alors `UnicodeEncodeError`, hors garde, et laisse un fichier vide, non scellé.
- Toute étape suivante s'arrête sur « empreinte compagnon absente ». Aucun arrêt n'est consigné, aucune issue n'est écrite.
- Avant E-7, seuls nos propres noms pouvaient entrer dans cette liste.

**Preuve** : `essais/test_verif4_scenarios.py::test_constat_e7_nom_non_utf8_sous_papier_laisse_un_resultat_vide` et `…_sous_a_verifier`.

**Correction**
- Écrire les noms sans substitut : `os.fsencode(m).decode("utf-8", "backslashreplace")`.
- Éprouvé : `essais/test_verif4_correctif.py::test_c1_c2…[nom non utf-8]`. L'anomalie reste celle du seul papier, et le résultat est scellé.

### V-2 — mineure (E-7 incomplet) — un chemin non régulier nommé `partie-*.md` sous `papier/` provoque une panne qui se répète

**Lieu**
- `extraire_t05.py` l. 292-293 (`p.is_file()`) ;
- `verifier-sortie-v1.py` l. 218 et 222 (`glob("partie-*.md")`, puis lecture) ;
- texte l. 128 et 262 (« l'étape se relance »).

**Problème**
- Un dossier vide, un lien cassé ou un tube nommé `papier/partie-99.md` n'est pas compté comme ajouté. Le module lance donc le script.
- Le script échoue (sortie hors forme) ou se bloque (délai dépassé).
- C'est une « panne de processus » : rien n'est écrit, et le texte dit de relancer l'étape. Mais elle se répète à l'identique, et la restauration est interdite : le run est bloqué, sans arrêt consigné.

**Preuve** : `test_constat_e7_chemin_non_regulier_sous_papier_bloque_l_etape`, trois cas, deux passages chacun.

**Correction**
- Compter tout chemin ajouté sous les trois sous-dossiers, fichier ou non, qui n'est ni une entrée ni le dossier parent d'une entrée.
- Effet de bord : un dossier vide ajouté sous `papier/` devient aussi une entrée modifiée. C'est plus strict, et sans effet sur un dossier sain.
- Éprouvé : `test_c1_c2…[dossier vide|lien cassé|tube nommé]`.
- Facultatif, au texte : une panne qui se répète à l'identique sur un même dossier est un nœud.

### V-3 — mineure (E-6 incomplet) — message `avis.cible` non échappé : la lecture de la ronde entière se bloque

**Lieu** : `extraction.py` l. 411 (`{str(t)[:60]}`). Le texte, l. 114, annonce que « les identifiants et valeurs cités dans les messages sont échappés ».

**Problème**
- Une cible d'avis écrite comme une chaîne qui porte un substitut isolé passe telle quelle dans le message.
- Les détails ne sont alors plus encodables. La lecture de toute la ronde s'arrête, à l'identique à chaque relance, avec l'archive déjà écrite.
- La ronde reste « non lue » : aucune ronde suivante, aucun assemblage.

**Preuve** : `test_constat_e6_cible_textuelle_avec_substitut_bloque_la_lecture`.

**Correction**
- `{str(t)[:60]!r}`. Les codes ne changent pas, ni dans le module ni dans les scripts.
- Éprouvé : `test_c3…` (avis illisible, l'autre papier reste lisible).

### V-4 — mineure (E-2, seul faux positif trouvé ; à trancher avant `preparer --tentative 1`) — une étape lancée depuis une autre copie du dépôt écrit un arrêt définitif

**Lieu** : `extraire_t05.py` l. 142-152 et 198-220 ; texte l. 253.

**Problème**
- Prenons un arbre de travail git, ou un clone, qui a `runs/` et `diag/` (suivis) mais pas `donnees/` (ignoré).
- Une étape lancée depuis cet arbre y écrit `arret-perte`, alors que les données du run sont intactes dans le dépôt d'origine.
- Le message dit « run nouveau », et la session suivrait le texte.
- Une fois committé et fusionné, cet arrêt arrête aussi le run d'origine (« run arrêté »).

**Preuve** : `test_constat_e2_autre_copie_du_depot_ecrit_un_arret_perte` (avec `git worktree add`, puis une fusion).

**Correction**
- Consigner `racine.resolve()` dans la configuration du manifeste, à la tentative 1. Dans `_ouvrir_run`, refuser sans rien écrire une étape lancée d'une autre racine.
- Une vraie perte, au même chemin après un redémarrage, reste un `arret-perte`.
- Cela ajoute une garde : 70 au total, à reporter au texte l. 229.
- Éprouvé : `test_c4…` (autre arbre refusé, sans arrêt écrit ; même racine écrite « . », acceptée).
- À défaut, une phrase au texte, section 7 : toute étape se lance depuis la racine du dépôt d'origine, jamais d'un autre arbre.

### V-5 — mineure (texte et code) — « Un seul dossier de papier disparu »

**Lieu** : texte l. 253 ; docstring l. 201-202 (« disparu seul ») ; code l. 212-215, qui ne contrôle que le dossier de la tentative ou de la ronde.

**Problème**
- Le texte laisse entendre que plusieurs dossiers disparus font une perte. Le code les traite tous en entrées modifiées.
- Exemple : les dossiers de papier d'une tentative 2, réponses justes comprises, disparaissent, et le dossier de la tentative reste.
- Les papiers sont alors exclus (« sorties invalides à deux tentatives »), puis remplacés par la réserve. Le run continue, et aucun arrêt D-17 ne vient en deçà de 16 papiers.

**Preuve** : `test_constat_e2_plusieurs_dossiers_de_papier_disparus_ne_sont_pas_une_perte`.

**Correction**, au choix :
- au texte (recommandé, simple) : « un ou plusieurs dossiers de papier disparus, le dossier de la tentative ou de la ronde restant, sont des entrées modifiées de leurs papiers » ;
- dans le code : plus d'un dossier de papier disparu dans une même préparation est une perte.

### V-6 — mineure (texte) — fichiers de retours dits « scellés et rattachés au manifeste »

**Lieu** : texte l. 240 (parenthèse) appliquée à l. 244 ; `extraire_t05.py` l. 978-984 (`_retours` lit seulement).

**Problème**
- Le code ne scelle pas le fichier de retours et ne consigne pas son empreinte. La règle de perte ne le couvre donc pas.
- Son contenu est repris ailleurs : dernière ligne dans les détails scellés, lancements dans `diag/`.

**Correction**, au choix :
- au texte : « fichiers de retours (non scellés : leur contenu est repris dans les détails scellés et dans `diag/`) » ;
- dans le code : sceller le fichier de retours et consigner son empreinte dans le résultat de l'étape.

### V-7 — suggestion (E-2) — empreinte compagnon illisible : exception hors garde, sans `arret-perte`

**Lieu** : `extraire_t05.py` l. 206-209 : `except (GardeArret, OSError)`.

**Problème** : une empreinte compagnon de `donnees/` aux octets non UTF-8 lève `UnicodeDecodeError` à chaque étape (`test_constat_e2_compagnon_illisible_exception_hors_garde`).

**Correction** : ajouter `ValueError` à la clause. Éprouvé : `test_c5…` (`arret-perte` écrit).

### V-8 — suggestion (E-8) — un seul `arret-avis-refaits` consigné par run

**Lieu** : `extraire_t05.py` l. 155-160 et 708-711 ; texte l. 176 et 257.

**Problème**
- Cet arrêt n'est pas définitif : d'autres rondes continuent.
- Un second papier, ou un second rôle, qui atteint la borne n'est pas consigné. Le nom de l'arrêt est fixe, et R12 interdit de le réécrire.
- Preuve : `test_constat_e8_second_arret_avis_refaits_non_consigne`.

**Correction**, au choix :
- dans le code : nommer l'arrêt par rôle et par papier (`arret-avis-refaits-<role>-<papier>`) ;
- au texte : seul le premier est consigné, et le nœud couvre les suivants.

### V-9 — suggestion (texte l. 249) — « aucune réélection n'est possible »

**Problème**
- La permutation est la même pour un run nouveau. Mais l'échantillon est formé des 16 premiers papiers admissibles de ce run, et toutes les sorties sont tirées de nouveau.
- Une perte donne donc un second tirage.

**Correction** : « même permutation ; le run perdu, ses codes et son arrêt restent consignés et sont rapportés avec le run nouveau (R4) ».

### V-10 — suggestion (texte l. 250-251) — rien ne contrôle `donnees/` après l'assemblage

**Correction** : avant la copie de l'option (a) ou (b) de N-014, vérifier chaque empreinte contre `diag/`, par exemple avec `exiger_rien_de_perdu`.

### V-11 — suggestion (E-12) — encodage absent de la recette

**Lieu** : essai à blanc, `references.code_de_decoupage`.

**Problème**
- Recalcul selon la recette : `2e1b9417feb017adc3bb1ff5c754646389edb23eeb98ac0123e8b7dd17ab2e56`, identique.
- Mais les sources contiennent des caractères non ASCII (docstrings en français), et la recette ne dit pas en quel encodage elles sont hachées.

**Correction** : ajouter « encodée en UTF-8 ».

### V-12 — suggestion (texte l. 81) — « il changerait le texte que lit le script »

**Problème** : ce n'est vrai que sous `papier/`. Les scripts ne lisent rien d'autre dans `invites/`, et ne lisent que trois noms dans `a-verifier/`.

**Correction** : « sous `papier/`, il changerait le texte que lit le script ; ailleurs, par prudence ».

### V-13 — suggestion (hors périmètre, préexistant) — étapes interrompues, et JSON très imbriqué

Déclencheurs très improbables (une interruption dans une fenêtre de quelques microsecondes, ou une sortie aberrante). Les modules étant épinglés, c'est à trancher avant `preparer --tentative 1`.

1. **Arrêts écrits après le résultat de l'étape** : D-17 (l. 498-508) et seuil (l. 806-813).
   - Une interruption entre le résultat et l'arrêt perd l'arrêt, et l'étape ne se refait plus (R12 sur le résultat).
   - `echantillonner` tire alors l'échantillon malgré le seuil D-17 (`test_hors_perimetre_arret_d17…`).
   - Le seuil de la lecture, lui, est recontrôlé par `reprises_dues` et `assembler`.
   - Parade : écrire l'arrêt avant le résultat, ou recompter dans `echantillonner`.
2. **Préparation interrompue** (tentative 2 ou 3, ronde) : elle ne se refait pas (R12 sur le dossier, l. 433-434 et 719-721), et le run est bloqué.
3. **`ecrire_resultat` interrompu entre l'écriture et le sceau** (`manifeste.py` l. 137-138) : le résultat reste non scellé, et toute étape suivante s'arrête sur lui.
4. **Sortie JSON imbriquée au-delà de la limite de récursion** : `RecursionError` n'est pas une `ValueError`, d'où une exception hors garde à chaque relance. Une parade toucherait aussi les scripts.

Preuves : `essais/test_verif4_hors_perimetre.py` (3 réussis).

## Essais (tous lancés depuis `/home/user/controle-ia`, avec `PYTHONDONTWRITEBYTECODE=1` et `-p no:cacheprovider`)

| essai | commande | résultat |
|---|---|---|
| suites du dépôt (G) | `PYTHONPATH=src .venv/bin/python -m pytest -q --basetemp=<W>/pytest-tmp tests/test_extraire_t05.py tests/test_extraction.py` | 130 réussis |
| gardes | idem, avec `PYTHONPATH=src:tests:<W>/essais` et `-p traceur_v4` | `essais/sortie_traceur.txt` : 69 sur 69 |
| E-3 (E) | `PYTHONPATH=src .venv/bin/python <W>/essais/essai_e3_accord.py` (scripts copiés et empreintés dans `<W>/copies/`) | `sortie_e3_accord.txt` : 0 écart |
| A à D, V-1 à V-8 | `PYTHONPATH=src:tests … -m pytest --rootdir=<W>/essais -c /dev/null <W>/essais/test_verif4_scenarios.py` | `sortie_scenarios.txt` : 30 réussis |
| V-13 | idem, avec `test_verif4_hors_perimetre.py` | 3 réussis |
| correctifs V-1 à V-4, V-7 | `PYTHONPATH=<W>/correctif/src:tests … -o pythonpath= tests/test_extraire_t05.py tests/test_extraction.py <W>/essais/test_verif4_correctif.py` | 138 réussis (130 + 8) ; différentiels dans `correctif/*.diff` |

## Empreintes sha256 des fichiers relus (identiques au début et à la fin)

| fichier | sha256 |
|---|---|
| `docs/procedures/T0.5-extraction-v1.md` | daa69da1d3ba4d3e6e6a968d228179a2cb325a4c8c061796d31b85f6454ea19f |
| `…/verifier-sortie-v1.py` | 9d32ffc672964d532df4ecb179278cfb728b02ad3aecec5f33c7d040846a7249 |
| `…/verifier-avis-v1.py` | 80e6d6846f2e56a1208955ef9fda591b7be9018ba891988600ee7752c3f3c0b2 |
| `…/consigne-extracteur-v1.txt` | 4c9c38e3dc16a53f6cb082615ad57d86610602b535236dd569ce80aa50992baf |
| `…/consigne-contre-verificateur-v1.txt` | ff21420ff0b148b2fc5836312875f38c6c3124dd968d8ed2e15d74a5c841c1bb |
| `…/essai-a-blanc-copie-de-lecture-v1.json` | 21c8021652023ac3783f866c32ba50a7f9d93549be9f90c318b8646cb8866d99 |
| `…/contre-lecture/rapport-contre-lecture-3-v1.md` | b64164010528d133102c3c0b02b1a7d146c9de74082d428e69171bc92bb3b4ee |
| `…/contre-lecture/traitement-contre-lecture-3-v1.md` | 21a848040f9b7d3986b18bcaa549c8b2bcd088995458b55d58ea295d2a1539e6 |
| `src/controle_ia/environnements/extraction.py` | bcd1ce4c89d955666219725e521139269af8fb6da4959afc98cef95b02d87523 |
| `src/controle_ia/environnements/extraire_t05.py` | 0a91eea1dca63f15a1b5c4dfc74c4b7ad7ee5252afde3508f62bdadec5c9db0e |
| `src/controle_ia/manifeste.py` | 1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d |
| `src/controle_ia/scellement.py` | 93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2 |
| `tests/test_extraire_t05.py` | 7fd9666a133e0b0d9a828468956ca032e857fc30a08830afb8e3fbe033bd867a |
| `tests/test_extraction.py` | 28fd2739c7203f7f741400d6bf77493054655a66568fbe64bf863c2ba9909a95 |
| `tests/conftest.py` | 0d4064e79e8e2231ee417877bda1ce1d3f77cf2ec423e9da95fe77de661eb175 |

Différentiel relu : `git diff f406eb4 5b5707d -- src tests`.
