# Rapport de la fille 11 — préenregistrement « candidat 1 corrigé » (agrégateurs de l'axe (c), R1 v4) — v1

- Ordre : `docs/procedures/ordre-fille-11-preenregistrement-agregation-v1.md` (`52886264f5db76f09574e14f13605225a186884744b6217ebde9e50ca923976a`, compagnon vérifié OK) ;
  dépôt au commit `a338caed` de `main` ; branche `prep/fille-11-agregation-v1`.
- Rédaction : 6 novembre 2026, 11:44 à 12:40 UTC environ (`date -u`).
- Opposabilité : l'autrice n'a lu aucune sortie des analyses de R1/R2 (ni `runs/`, ni `diag/`, ni `donnees/`, ni branche
  `calcul/…`, `analyses-r1-v4`, `canal/…`, ni verdict de R1/R2). Aucun fichier lu par erreur.

## Fichiers et empreintes

| fichier (au commit du code) | sha256 |
|---|---|
| `src/controle_ia/agregation_r1_v4/__init__.py` | `65c7a0abac4cf938664d9af85d5a25837539f4396e6e05346c60223f32bc7a09` |
| `src/controle_ia/agregation_r1_v4/agregateurs_v1.py` | `1662549b3630c963aae7148079cb22d4c035e0fc8b5fce3da4582ca1b8db77a8` |
| `src/controle_ia/agregation_r1_v4/comparaisons_v1.py` | `4e59c9dc0038d7f8f3cd5b88a67d46f2de4df16924a871cf196dc3420b8f1c45` |
| `src/controle_ia/agregation_r1_v4/puissance_v1.py` | `ee9bb63dfa3f62d1286bd99ba63bfb2b3cc3d6021ea16e97ae584fec30556f4a` |
| `src/controle_ia/agregation_r1_v4/entrees_v1.py` | `00b73d6d83eb257f2a2540d809476b3a131e2d92137707426de161b0a59745e2` |
| `src/controle_ia/agregation_r1_v4/analyse_v1.py` | `8d705df3ccdcf93e230d56513996e99879bc4bcc87c467ec888cb175388c59bc` |
| `src/controle_ia/sondes/evaluation.py` | `1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3` |
| `src/controle_ia/gardes.py` | `a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439` |
| `src/controle_ia/manifeste.py` | `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d` |
| `src/controle_ia/prereg.py` | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` |
| `src/controle_ia/scellement.py` | `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2` |
| `tests/test_agregation_r1_v4.py` | `e01ccfb1ee2a654b9aebbcb2683eba4ea66b61dfebe16a62215b91f0846e75af` |
| `brouillons/preenregistrement-agregation-r1-v4-v1-puissance.py` | `201916809063e2999bbacde1f7233c48813fbae0dec84fce33708cce5cf72a25` |
| `brouillons/preenregistrement-agregation-r1-v4-v1-puissance.json` | `531166428bc461ac32e930b860466f8abdecfd79b8a0832580f46648ce5b7afd` |

Code d'analyse au commit `9421aaa9d6815d478b2da8e69bbca0a86892aaac`. Essais : `tests/test_agregation_r1_v4.py`, 25 essais, tous verts
(`timeout 900 nice -n 10 python -m pytest -q tests/test_agregation_r1_v4.py`) ; suite complète du dépôt (`timeout 900 nice -n 10 python -m pytest -q`) : **non achevée**, arrêtée par le délai de 900 s
(code 143) sans échec affiché avant l'arrêt ; non relancée (une suite à la fois, délai de l'ordre). À relancer par la mère avec un
délai plus long ; seul le module neuf a été vérifié en entier.

## Ce qui est fait

1. Brouillon 1 conforme au gabarit ; le validateur (`prereg.problemes`) ne signale que les marqueurs attendus.
2. Simulation de puissance (script et sortie à côté du brouillon) : 7 aires d'action (dont 0,5248 et 0,5748 de P3) × 2 effets
   d'épisode × 2 effets de tâche, 200 répliques, graine racine 20261106.
3. Code d'analyse complet (`src/controle_ia/agregation_r1_v4/` : entrées et gardes, agrégateurs, comparaisons par blocs,
   permutation, Holm, gardes de puissance, lecture gelée, commande décisive unique) et essais sur données synthétiques aux
   formats exacts de la fiche v4 (14 tableaux, (2400, 3, 4096) `<f2`, identité égale à `scores-p3.npz`), chaque garde sur un
   cas sain et un artefact (R5), et un essai de la commande décisive de bout en bout dans un dépôt jetable (manifeste décisif,
   préenregistrement scellé exigé, résultat scellé, refus d'écraser).

## Marqueurs restants

- `<<CONTRE_LECTURE_1>>` dans la section « Contre-lecture » (R2 : à faire par un sous-agent neuf).
- Après la contre-lecture : copie vers `prereg/agregation-r1-v4-v1.md` (nom attendu par la commande décisive) et scellement par
  la mère ; aucun `.sha256` n'a été écrit ici (interdit de l'ordre).
- Gardes sans essai d'artefact dédié : « empreinte changée pendant le run » (relue après chargement ; non simulée) ; signal
  TERM (pas de gestionnaire : `timeout` tue le processus, aucun résultat n'est écrit avant la fin).

## Dix points pour le contre-lecteur

1. **Classe d'attaquant** : la lecture « M dense » repose sur `P3-consignes-v1.md`, l. 31-45 (« for every proposal », rappel à
   chaque pas). Vérifier qu'aucune action du saboteur n'est structurellement sans coût (actions `REVISE` sans numéro, actions
   sans ligne `ACTION`, P3 l. 167-172) : elles restent « instruites » mais leur décalage peut être nul — δ_k ≥ 0 reste en classe M.
2. **Écart au lemme déclaré** : le lemme parle à budget B fixé ; ici le décalage par action est fixé et B croît avec m. La
   prédiction vient de la simulation gaussienne, pas d'un énoncé du lemme ; la formulation de l'hypothèse le dit-elle assez ?
3. **Hybrides** : un épisode hybride mélange les activations de deux épisodes réels ; la dépendance intra-épisode du saboteur
   est rompue à m = 1. Est-ce une limite à écrire dans « Ce que ce texte ne teste pas » ?
4. **Réduction par pli sur les honnêtes du pli** : légère fuite des négatifs dans la normalisation, commune à toutes les
   statistiques ; acceptable pour une comparaison entre agrégateurs ? (Alternative : réservoir honnête hors pli, mais échelle
   d'un autre modèle.)
5. **Recette de W recalculée** (L2, C = 1, convention de `scikit-learn`, centrage-réduction par pli, L-BFGS) : le code de la
   principale n'a pas été lu ; confronter à `constantes_v1.py` et au code de la principale (branche du canal). Les scores ne
   sont pas ceux de la principale, c'est voulu ; la recette doit seulement être celle de W.
6. **Gardes de puissance au a_W mesuré** : la lecture de l'aire d'action de W est faite dans le run, après scellement ; elle
   décide quels tests sont confirmatoires. Est-ce une lecture conditionnelle acceptable (la grandeur de garde n'est pas la
   grandeur testée), et le choix « minimum sur quatre cellules, 0,80 au niveau 0,05/3 » est-il assez conservateur ?
7. **Famille et Holm** : Holm sur {C1, C2, C3} seulement ; la famille élargie aux trois analyses scellées est déclarée avec une
   borne d'union, faute de valeurs p chez elles. L'ordre demandait « Holm avec les trois analyses » : écart à trancher par la
   mère (nœud possible).
8. **Ce qui est déjà lu par d'autres** : P3-P5 (somme contre maximum par épisode pour Gt et Ge) a été calculée par P3 et lue
   par d'autres (`lecture-p3.json`) ; le verdict n'en publie que le maximum (0,0667 et 0,0). Ce texte garde Gt et Ge en
   descriptif seulement : suffisant ?
9. **Valeurs chiffrées** : chaque nombre de la table des prédictions doit se retrouver dans `…-puissance.json` (empreinte
   ci-dessus) ; les aires de P3 dans le verdict P3 v2, l. 209 et 214 ; aucun autre chiffre réel n'est cité.
10. **Confrontation aux trois analyses scellées** : toutes les citations (l. 57, 110, 122, 133, 167, 199 …) viennent de la
    lecture préparatoire, pas des textes ; les vérifier sur les textes eux-mêmes (branche `canal/conv-audit-n04`,
    `4b164694`).

## Trois risques

1. **Plafond de W** : pour un organisme flagrant, a_W peut être ≥ 0,99 (et même déclencher l'audit R4 « fuite ») ; C1 serait
   alors écarté, la lecture reposerait sur C2 et C3, eux-mêmes portés par des hybrides — la partie la plus construite du plan.
2. **Non-échangeabilité des actions** : effets de pas et de contexte (le saboteur rappelé à chaque pas) peuvent rendre les
   actions honnêtes et saboteuses d'un même pas non comparables ; la simulation ne couvre que des effets de tâche et
   d'épisode gaussiens. Un « réfuté » pourrait venir de là plutôt que du lemme.
3. **Opposabilité dépendante d'une lecture de seconde main** : les trois analyses n'ont pas été lues directement ; une citation
   inexacte de la lecture préparatoire passerait dans ce texte. La contre-lecture doit les confronter aux textes.

## Complément après le message de la mère (6 novembre, 12:02 UTC ; reçu vers 12:22 UTC)

- Les trois analyses scellées et l'addendum v4 de R1 ont été lus **sur `main` au commit `a113adb6`** (compagnons OK) et
  confrontés aux extraits de la lecture préparatoire : conformes. Deux précisions : recette exacte de W (5 plis de 12, `gtol`
  10⁻⁵, 10 000 itérations, écart type sans correction, plancher 10⁻⁸ → 1) ; Bonferroni, non Holm, dans la principale.
- Le brouillon 1 (`b6d5cdc6…`, commit `361a2308`) n'est **pas modifié** : il est sous contre-lecture (consigne de la mère,
  commit `8b14b298`). Les changements sont proposés en **couples d'auteur** :
  `brouillons/preenregistrement-agregation-r1-v4-v1-couples-auteur.json` (17 couples, chaque « ancien » unique dans le
  brouillon 1), et appliqués par script dans `brouillons/preenregistrement-agregation-r1-v4-v1-brouillon2.md` (le validateur
  ne signale que `<<CONTRE_LECTURE_1>>`). Ils ajoutent le paragraphe demandé par la mère : l'épisode hybride est une
  recombinaison de données réelles, pas un épisode joué, et ce que chaque issue prouve ou ne prouve pas.
- Code : `analyse_v2.py` (recette de W de la principale), au commit `c88cfd47` ; `analyse_v1.py` inchangé, jamais lancé.
  Essais : `tests/test_agregation_r1_v4_v2.py`, 6 essais ; avec ceux de la v1 : 31 verts
  (`timeout 900 nice -n 10 python -m pytest -q tests/test_agregation_r1_v4_v2.py tests/test_agregation_r1_v4.py`).
- Le contre-lecteur peut juger les couples d'auteur avec les siens ; la mère choisit le texte à sceller (brouillon 1 + couples).

## Brouillon 3 (après la contre-lecture de la fille 9, `main` 7ac8cbeb ; message de la mère de 12:33 UTC)

- Pièces de la contre-lecture lues sur `main` au commit `7ac8cbeb`, compagnons OK : rapport, 14 couples, corrections Q1 à Q5.
- `brouillons/preenregistrement-agregation-r1-v4-v1-brouillon3.md` = brouillon 2 + 14 couples du lecteur + 7 couples d'auteur
  (A18 à A24 ; A1 à A17 sont ceux de `…-couples-auteur.json`, dans l'ordre du fichier), appliqués par script ; liste complète
  dans `brouillons/preenregistrement-agregation-r1-v4-v1-couples-brouillon3.json` (chaque « ancien » unique dans le
  brouillon 2). Validateur : seul `<<CONTRE_LECTURE_1>>` reste. La garde Q1 de `analyse_v3` passe sur ce brouillon à la tête
  de la branche (16 fichiers cités, empreintes égales).

| couple | traitement | raison |
|---|---|---|
| L1 | appliqué tel quel | « ancien » inchangé dans le brouillon 2 |
| L2 | appliqué tel quel | « ancien » inchangé dans le brouillon 2 |
| L3 | appliqué tel quel | « ancien » inchangé dans le brouillon 2 |
| L4 | appliqué tel quel | « ancien » inchangé dans le brouillon 2 |
| L5 | appliqué tel quel | « ancien » inchangé dans le brouillon 2 |
| L6 | appliqué tel quel | « ancien » inchangé dans le brouillon 2 |
| L7 | appliqué tel quel | « ancien » inchangé dans le brouillon 2 |
| L8 | appliqué tel quel | « ancien » inchangé dans le brouillon 2 |
| L9 | appliqué tel quel | « ancien » inchangé dans le brouillon 2 |
| L13 | appliqué tel quel | « ancien » inchangé dans le brouillon 2 |
| L14 | appliqué tel quel | « ancien » inchangé dans le brouillon 2 |
| L10 | adapté | le couple d'auteur A13 avait ajouté une incise après « borne d'union » ; même ajout, placé avant l'incise |
| L11 | adapté (en partie déjà couvert) | le couple d'auteur A7 a aligné la recette sur la principale (option préférée par Q5) : l'écart déclaré par L11 n'existe plus ; seule la dernière phrase de L11 (aucune comparaison avec les scores de la principale) est reprise |
| L12 | adapté | réglages de la v2 (10⁻⁵, 10 000) au lieu de ceux de la v1 ; même ajout |
| A18 | couple d'auteur | v3 du code, plafond, liste d'arrêt Q1-Q4, déclaration de la contre-lecture lue |
| A19 | couple d'auteur | v3 du code, plafond, liste d'arrêt Q1-Q4, déclaration de la contre-lecture lue |
| A20 | couple d'auteur | v3 du code, plafond, liste d'arrêt Q1-Q4, déclaration de la contre-lecture lue |
| A21 | couple d'auteur | v3 du code, plafond, liste d'arrêt Q1-Q4, déclaration de la contre-lecture lue |
| A22 | couple d'auteur | v3 du code, plafond, liste d'arrêt Q1-Q4, déclaration de la contre-lecture lue |
| A23 | couple d'auteur | v3 du code, plafond, liste d'arrêt Q1-Q4, déclaration de la contre-lecture lue |
| A24 | couple d'auteur | v3 du code, plafond, liste d'arrêt Q1-Q4, déclaration de la contre-lecture lue |
- Code v3 au commit `1fcb23d70b0b2be52212f40f671a5df8f6fa2794` : `analyse_v3.py` (v1 et v2 inchangées, jamais lancées).
  - Q1 : liste fermée `CODE_CITE` (16 fichiers, égale aux modules réellement importés, essai dédié) vérifiée contre la table
    du texte ; Q2 : chemin `prereg/agregation-r1-v4-v1.md` imposé ; Q3 : noms de la fiche v4, `scores-p3.npz` = `968414fc…`,
    activations égales à leur compagnon `.sha256` de la réception (la fiche ne consigne pas leurs valeurs : vérifié par
    recherche, aucune empreinte d'activations dans la fiche) ; Q4 : second passage → `SecondPassage`, code de fin 3 ; toutes
    avant le manifeste et tout chargement. Plafond : `lire_hag(v, a_W)`.
  - Q5 : recette de `analyse_v2`/`v3` vérifiée contre le texte de la principale (l. 60) ; le module
    `analyse_blanche_noire.modeles` n'est pas sur `main` : non lu, non comparé au code.
  - Essais : `tests/test_agregation_r1_v4_v3.py`, 10 essais (sain et second passage ; non scellé → refus avant chargement ;
    arbre sale ; chemin ; liste fermée altérée et incomplète ; empreinte de `scores-p3.npz` ; compagnon faux ; noms ; plafond ;
    liste fermée = modules importés). Suite du module (v1 + v2 + v3) : **41 verts** en 60 s
    (`timeout 900 nice -n 10 python -m pytest -q -p no:cacheprovider tests/test_agregation_r1_v4.py tests/test_agregation_r1_v4_v2.py tests/test_agregation_r1_v4_v3.py`).

## Brouillon 4 (message de la mère de 12:36 UTC : additif de contre-lecture sur le brouillon 2, `main` efe257ac)

- **Le brouillon 3 est remplacé** (il appliquait les 14 couples visant le brouillon 1 ; gardé au dépôt, R12, à ne pas sceller).
- `brouillons/preenregistrement-agregation-r1-v4-v1-brouillon4.md` = brouillon 2 (`fb2c93ef…`)
  + les **12 couples de l'additif** (`couples-contre-lecture-agregation-r1-v4-v1-brouillon2.json`, `eb8ff666…`, compagnon OK),
    **tels quels, dans l'ordre, par script** (chaque « ancien » unique, vérifié avant chaque remplacement : 12 sur 12)
  + **6 couples d'auteur A18 à A23**, appliqués après, pour le code v3 seulement :
    `brouillons/preenregistrement-agregation-r1-v4-v1-couples-auteur-brouillon4.json` (commit et commande `analyse_v3` ;
    déclaration de la contre-lecture lue ; Q5 ; plan 7-8 réécrits avec les gardes Q1 à Q4 et la table du code à 21 lignes au
    commit `1fcb23d7` ; règle du plafond rattachée à `lire_hag` ; liste d'arrêt Q1 à Q4) ;
  + **titre changé hors couples** (« brouillon 2 » → « brouillon 4 »), déclaré en tête du texte (A19) et ici.
- Validateur : seul `<<CONTRE_LECTURE_1>>` (et l'entrée de contre-lecture qu'il remplira). La garde Q1 de `analyse_v3` passe
  sur ce brouillon (16 fichiers, empreintes égales).
- Code v3 (commit `1fcb23d7`) inchangé depuis le brouillon 3 : Q1 à Q4, artefacts R5 « non scellé » et « arbre sale » éprouvés ;
  41 essais verts (v1 + v2 + v3).
