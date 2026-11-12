# Complément au rapport du développeur — code de lecture du barreau 6 (`ACCB6`) : contrôle du code contre `CODE-ACCB6` — v1

- **Auteur** : le même développeur neuf (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; mêmes exclusions (a lu des parties de T0.7 : exclu de tout rôle de lecteur de P3-bis ; n'a vu ni `lecture-t07.json`, ni aucune issue de T0.7 ou de P3-bis, ni aucune sortie de `agregation-r1-v4`).
- **Consigne** : message de suite de la mère (R-2272), même consigne (`consigne-code-accb6-v1.md`, `48b502d0…`), mêmes interdits, même arbre (`/home/user/wt-accb6`), même branche. Rapport complété : `rapport-developpeur-accb6-v1.md`, `2a6880e4e3ef65db858a60f67b2eb723001fdb7df364993fc7b21e46f203fb1c` (gardé tel quel, R12).
- **Heures (UTC, relevées par `date -u`)** : travail à partir de 18:55:51 ; banc v2 de 19:01:18 (interrompu par un disque plein vers 19:21) ; mutations rejouées de 19:22:42 à 19:33:44, puis vers 19:36 et de 19:36:33 à 19:45:33 ; commit 19:47:53 ; poussée 19:47:56.
- **Verdict en une ligne** : contrôle du code ajouté en fichier neuf et appelé par `lecture_v1` avant tout calcul et avant le manifeste. 165 essais passent, l'énumération rejouée est égale à l'octet, 65 mutations sur 65 sont tuées. **Commit final proposé pour `COMMIT_CODE_ACCB6` : `56c624ddb02941e09ff5bb96d8c848214e6b576a`.**

## 1. Commit final proposé pour `COMMIT_CODE_ACCB6`

- **`56c624ddb02941e09ff5bb96d8c848214e6b576a`**, branche `prep/accumulation-b6-code-v1`, parent `65a09c95b2014e277705b3500901b2225d9c2e76` (commit du rapport), poussée vers `origin` (`https://github.com/lciric/controle-ia-travail`) ; tête distante vérifiée égale. Aucune fusion. Arbre `src/` : `d2c9b956a3bf739db00984c5701ce09aeec98770` ; arbre du paquet : `b147fe41fd65f0d2d7d1f276b245b216a806012c`.
- Contrôle réel fait par ce développeur. `ecrire` a été lancé sur `/home/user/wt-accb6` au commit `HEAD`, avec une sortie dans le bac à sable. `controler_code` a ensuite été lancé sur le paquet effectivement importé (`/home/user/wt-accb6/src/controle_ia/accumulation_b6`). Résultat : **conforme**, 6 fichiers, tête du dépôt = `56c624dd…`. Ce fichier d'essai a été effacé : son entropie ne doit pas servir. La mère tire la sienne à l'inscription.

## 2. Ce qui est ajouté

- **Fichier neuf** `src/controle_ia/accumulation_b6/code_accb6_v1.py`.
  - `controler_code(racine, entree, dossier_code=None)` lit le fichier cité par la ligne `CODE-ACCB6`. Sa forme est `{commit, fichiers : {chemin : sha256}, entropie}`, contrôlée par `garde_v1.lire_fichier_code`. La vérification se fait dans le dépôt git qui porte le paquet **effectivement importé** (le dossier du module ; `dossier_code` ne sert qu'aux essais) :
    1. le paquet est `src/controle_ia/accumulation_b6/` de ce dépôt ;
    2. chaque chemin listé est `src/controle_ia/accumulation_b6/<nom>.py`, avec une empreinte de 64 caractères ;
    3. le commit cité existe et est la tête ou un de ses ancêtres ;
    4. les fichiers `*.py` du paquet **au commit cité** sont exactement ceux de la liste, aux empreintes écrites ;
    5. les fichiers `*.py` du **paquet importé** sont exactement ceux de la liste, aux empreintes écrites.

    Tout défaut lève `RefusRegistre`.
  - `ecrire_fichier_code(depot, commit, sortie, entropie=None)` écrit le fichier pour un commit donné. Il prend les fichiers `*.py` du paquet au commit et les empreintes de leur contenu au commit. Il tire l'entropie de 128 bits par `numpy.random.SeedSequence().entropy` (R9). Il refuse d'écraser un fichier existant (R12).
  - Commandes : `python -m controle_ia.accumulation_b6.code_accb6_v1 ecrire DEPOT COMMIT SORTIE` et `… verifier RACINE` (rien d'écrit ; code 0 si conforme, 2 si refus). Le scellement du fichier et la ligne `CODE-ACCB6` restent à la mère.
- **Appel** : `lecture_v1.lire` appelle `controler_code` juste après la garde d'ouverture, dans le bloc des refus. Il passe donc avant l'aiguillage (`lecture-t07.json` n'est pas encore lu), avant `sondes-t07.json`, E2b, E3 et avant le manifeste. Un défaut donne un refus, code 2, avec une ligne `REFUS-ACCB6` au journal propre et rien d'autre d'écrit. Le rapport du contrôle est écrit dans le résultat (`controle_code`).

## 3. Fichiers modifiés (déclarés) et pourquoi

- `src/controle_ia/accumulation_b6/lecture_v1.py` : import du module, appel du contrôle, paramètre `dossier_code` de `lire` (essais seulement ; la commande n'en prend aucun), champ `controle_code` du résultat, en-tête. Inévitable : la consigne de suite demande l'appel par `lecture_v1`.
- `tests/test_accb6_lecture_v1.py` :
  - nouvelle fonction `code_jouet` : le paquet importé est recopié et committé dans le dépôt jetable du jouet, puis le fichier de `CODE-ACCB6` est écrit par `ecrire` pour ce commit (la forme seule pour les jouets en sous-dossier, qui ne lisent pas) ;
  - `_lire` passe `dossier_code` ;
  - l'essai G-1 par la commande désigne le paquet du jouet comme paquet importé (`dossier_du_paquet` remplacé le temps de l'essai).

  Inévitable : sans cela, toutes les lectures de bout en bout, qui citaient un faux commit, seraient refusées par le nouveau contrôle.
- `tests/test_accb6_garde_v1.py` : deux appels à `lv.lire` reçoivent `dossier_code`. Même raison.
- Aucun autre fichier existant n'est touché ; `etats_v1.py`, `phrases_v1.py`, `garde_v1.py`, le script d'énumération et sa sortie sont inchangés.

## 4. Empreintes (sha256, au commit `56c624dd…`)

| fichier | sha256 |
|---|---|
| `src/controle_ia/accumulation_b6/__init__.py` | `72bc176fcd0df9f2d4bc241b0b9c7696558f308b8516916496cb821b40786d7e` (inchangé) |
| `src/controle_ia/accumulation_b6/code_accb6_v1.py` (neuf) | `2e6c3bb878cbc9996335527f74257cc57392b13d0487fa3bace219a260e55c02` |
| `src/controle_ia/accumulation_b6/etats_v1.py` | `90a1c20be99edda781b78ce26a05e28582e9cccb151c365d247fc0cd72bcdbd8` (inchangé) |
| `src/controle_ia/accumulation_b6/garde_v1.py` | `5ceeb9f2ba1c1f3ef4abee3138e3bcec39342f76658db5a83e2363045aed6dd7` (inchangé) |
| `src/controle_ia/accumulation_b6/lecture_v1.py` (modifié) | `70764f664ffb9670baa88000323cccfc440d4387c9bcea9a6e7baefdb474e6c8` |
| `src/controle_ia/accumulation_b6/phrases_v1.py` | `9376fcc05337d4979a3f40acc3b2e84ecdb03fb528c24b3d6c3e3bc4bfb9f228` (inchangé) |
| `tests/test_accb6_code_v1.py` (neuf) | `a4cc477e51e7e3126d747d2acf2790bd36036444a25f23860c35450ce770c1b8` |
| `tests/test_accb6_etats_v1.py` | `d0cf205e7d48371ce8e744193f5c392bb4d206ba11bece065dd6c09f42b6f7c2` (inchangé) |
| `tests/test_accb6_garde_v1.py` (modifié) | `448eb2d3630985ea1224c27b4c39949bb3bdec3fd626c9eaf8c8952e43f4ce53` |
| `tests/test_accb6_lecture_v1.py` (modifié) | `bd890cd86462d1beb7af73b25e4bd38835f2d4ae126c4fb9550946c80a77fd3d` |
| `scripts/enumeration_etats_accb6_v1.py` | `d7b6fa08f02c0b494f58aca7803099240baf28723a93334235701cb5594a431f` (inchangé) |
| `scripts/enumeration-etats-accb6-v1.txt` | `3bde500f1eca8ceb5e95b782ea74312cace981d019d8fef6ead7944341abf5a6` (inchangée) |

Liste que `ecrire` donne au commit `56c624dd…` (fichiers du paquet ; contenu au commit) : les six premières lignes de la table.

## 5. Essais et énumération rejoués

- **Essais du paquet** : **165 passed** dans l'arbre de la branche, en 114 s : les 146 du premier rapport, adaptés, plus 19 essais du contrôle.
- **Essais du contrôle** (`tests/test_accb6_code_v1.py`), chacun avec un cas sain ou un artefact :
  - cas sains : `ecrire` puis contrôle conforme ; commit cité ancêtre de la tête ;
  - gardes d'`ecrire` : entropie tirée de 128 bits ; refus d'écraser ; commit introuvable ; commit sans paquet ;
  - fichier du paquet importé modifié après le commit ;
  - fichier en plus ou en moins dans le paquet importé ;
  - empreinte écrite fausse ;
  - commit absent ;
  - commit orphelin hors de l'histoire de la tête (fait par `git commit-tree`, la tête ne bouge pas) ;
  - liste écrite pour un autre commit, dans les deux sens ;
  - fichier présent au commit, absent de la liste et du paquet importé (ajouté après le banc) ;
  - chemin listé hors du paquet ; forme du fichier ;
  - paquet hors d'un dépôt git ; paquet ailleurs dans le dépôt ;
  - lecture refusée avant tout calcul : `lecture-t07.json` jamais lu, aucun run, ligne `REFUS-ACCB6` ;
  - lecture saine, avec le contrôle écrit dans le résultat ;
  - la commande contrôle le paquet réellement importé (fichier du jouet étranger : refus, code 2) ;
  - commandes `verifier` et `ecrire`.

  Tous ces essais tournent sur des dépôts git jetables. Aucune commande git d'écriture n'est jouée dans le dépôt du programme.
- **Énumération** : rejouée (`python3 -I -B scripts/enumeration_etats_accb6_v1.py …`), sortie **égale à l'octet** à la sortie versée (`3bde500f…`) ; bilans inchangés (1 152 couples, 343 jeux, 33 issues de séquence, 604 phrases ; 0 cas sans état, 0 cas sans phrase).
- **Non rejoués** :
  - les essais de T0.7 : aucun fichier touché ici n'est lu par eux ; le premier rapport les a rejoués avant et après, avec des issues identiques ;
  - l'essai hors suite aux constantes réelles : le calcul n'a pas changé. La commande refuserait désormais le fichier de code factice de cet essai, qui devrait désigner le paquet du jouet.

## 6. Banc de mutations (copies seulement, `-o pythonpath=`, import tracé)

- 65 mutations : les 55 du premier rapport et C01 à C10 (contrôle et appel). Scripts du bac à sable : `banc_accb6_v2.py` (`3188f9fe…`) et sa variante à deux processus `banc_accb6_v2b.py` (`2288120f…`), `mutations_accb6_v2.py` (`9a121371…`). Le greffon `trace_import_accb6.py`, v2 (`80a14bce…`), trace aussi `code_accb6_v1` ; tous les modules sont importés depuis la copie.
- **65 tuées sur 65.**
  - M01 à M55 : premier passage (`banc-v2.jsonl`, `30e5009c…`), sauf M33 et M36, qui ont vu un disque plein et ont été rejouées (`banc-v2b.jsonl`, `816b68f1…`) : tuées.
  - C01 à C10 : passage final, import tracé (`banc-v2d.jsonl`, `d6db684f…`) : toutes tuées.
  - Au passage précédent (`banc-v2b`), **C02 survivait** (contrôle « fichiers au commit = liste » retiré). L'essai `test_fichier_du_commit_absent_de_la_liste_et_du_paquet_importe` a été ajouté, puis C02 a été tuée (`banc-v2c.jsonl`, `e602c651…`, puis `banc-v2d`).
- **Disque plein** au passage à quatre processus (vers 19:21 UTC, 245 Mo libres) : processus arrêtés par leurs identifiants (R10), copies effacées, résultats touchés (C01 à C04, M33, M36) écartés et rejoués à deux processus.

| id | ce qui est éprouvé (`code_accb6_v1.py`, sauf C10) | issue | premier essai en échec |
|---|---|---|---|
| C01 | commit cité ancêtre de la tête | tuée | `test_commit_non_ancetre_de_la_tete` |
| C02 | fichiers du paquet au commit = liste | tuée | `test_fichier_du_commit_absent_de_la_liste_et_du_paquet_importe` |
| C03 | fichiers du paquet importé = liste | tuée | `test_fichier_en_plus_ou_en_moins_dans_le_paquet_importe[ajout]` |
| C04 | empreintes au commit | tuée | `test_empreinte_ecrite_fausse` |
| C05 | empreintes du paquet importé | tuée | `test_fichier_du_paquet_importe_modifie` |
| C06 | commit cité présent | tuée | `test_commit_absent` |
| C07 | paquet à sa place dans le dépôt | tuée | `test_paquet_ailleurs_dans_le_depot` |
| C08 | chemins listés dans le paquet | tuée | `test_chemin_liste_hors_du_paquet` |
| C09 | paquet hors dépôt git | tuée | `test_paquet_hors_d_un_depot_git` |
| C10 | appel du contrôle par `lecture_v1` (`lecture_v1.py`) | tuée | `test_lecture_refusee_avant_tout_calcul` |

## 7. Couples proposés au texte (suite du § 7 du rapport)

- **CP-02, mis à jour** : la liste des fichiers du code neuf comprend `code_accb6_v1.py`. Ancien : « - **[neuf]** `src/controle_ia/accumulation_b6/lecture_v1.py` : ». Nouveau : « - **[neuf]** `src/controle_ia/accumulation_b6/` (`lecture_v1.py`, `garde_v1.py`, `etats_v1.py`, `phrases_v1.py`, `code_accb6_v1.py`, `__init__.py`) : ».
- **CP-19 (contrôle du code, désormais mis en œuvre)**. Le texte ne le prévoit pas ; à ajouter au plan, point 2, et à la liste d'arrêt.
  - Ancien : « `CODE-ACCB6` strictement avant la première ligne `OUVERTURE-T07` ».
  - Nouveau : « le fichier cité par `CODE-ACCB6` (`{commit, fichiers, entropie}`, écrit par `code_accb6_v1 ecrire`) est égal aux fichiers `*.py` du paquet effectivement importé et à ceux du commit cité, et ce commit est la tête ou un ancêtre de la tête du dépôt qui porte le paquet ; sinon refus, code 2, avant tout calcul et avant le manifeste ; `CODE-ACCB6` strictement avant la première ligne `OUVERTURE-T07` ».
- La ligne « Non mis en œuvre (proposé seulement) » du § 7 du rapport est levée par ce complément.

## 8. Points ouverts

1. **Modules hors du paquet non contrôlés**. Les fonctions appelées de `t07` (`registre_v1`, `criteres_v1`, `plancher_v1`), de `sondes` (`evaluation`, `temoins`), et `manifeste`, `scellement`, `gardes` ne sont pas comparées au commit cité. Une extension pourrait lister leurs fichiers dans `CODE-ACCB6` et les vérifier, mais elle lierait la lecture à un état exact de ces modules. Pour T0.7, DF-02 de `code_t07_v1` exige tout `src/controle_ia/` égal au commit. À trancher par la mère.
2. **Lieu de la lecture**. Elle doit tourner dans un dépôt dont la tête descend du commit cité et dont le paquet est inchangé. Après la fusion dans `main` (après le scellement de T0.7, R-2231), c'est le cas tant que le paquet n'est pas modifié. Toute modification du paquet demande un fichier de `CODE-ACCB6` neuf, donc une ligne neuve, sous les règles d'antériorité du texte.
3. **Contenu du fichier de `CODE-ACCB6`**. Il ne porte que les fichiers `*.py` du paquet. Le script d'énumération et sa sortie relèvent du marqueur `ENUMERATION_ETATS_ACCB6` (empreintes au § 4). Son entropie est tirée par `ecrire` à l'inscription. Le scellement et la ligne restent à la mère.
4. **Rappel du premier rapport, toujours ouvert** : rejouer la suite de T0.7 dans un arbre complet ; trancher les couples CP-03, CP-04, CP-06 et CP-07 ; relance après un arrêt ; R-B6-DIR sur jouet.

## 9. Refus d'un contrôle

Aucun refus d'un contrôle de permissions ou de sécurité pendant cette suite. Le refus du premier rapport (§ 9) n'a été relancé sous aucune forme.
