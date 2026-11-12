# Journal — barreau 6, candidat 5 — v1

Même rédacteur que le candidat 4 (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Consigne : message de la mère au rédacteur du candidat 4 (« écris le candidat 5 … mêmes règles que ta consigne »), portant les décisions de **R-2339** (`registres/decisions.md`, ligne lue entière, ainsi que R-2338 qu'elle cite) ; consigne d'origine `a54e39cb…` et interdits communs v2 (`1ee3b370…`) tenus. Aucun commit, aucun appel de modèle, aucune dépense. Heures relevées par `date -u` (début 12:44:42 UTC, le 2026-11-11 ; lancement réel du script 12:49:46 UTC). Candidats 1 à 4 intacts (candidat 4 `e3aef53004d18b07e7eb30c31d30ad00986f69528cd55f2e0a57bea9423dcf84`, relu par empreinte après l'écriture). J'ai lu T0.7 scellé (candidat 4) : exclu de tout rôle de lecteur de P3-bis.

## 1. Vérifications

- Commit fils d'essais `536dd83e3effa1186fbbe9f5bae122119e4a95eb` (lecture seule ; `git cat-file -t`, `git log -1`, `git diff --stat`, `git diff --quiet … -- src`, `git show`) : parent `282e295e…` ; un seul fichier ajouté, `tests/test_accb6_sondages_contre_lecture_v2.py`, `bbd28591d3cdc7cac180be10c05021017496423f5c362201298b111bdd3d09cf` (égal à R-2339) ; `src/` égal à `282e295e` : le paquet et `CODE-ACCB6` à `282e295e` ne changent pas. Le compte « 207 passés, 1 sauté » est celui de R-2339 (je n'ai pas rejoué la suite : règle 5 des interdits).
- Contre-lecture courte du code v2 : `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/contre-lecture-courte-code-accb6-v2.md`, `a47d29796a38188b8b234530e5e81b9fc053a53b219e8f5af4b8be1cc8054237`, compagnon conforme ; **empreinte seule, non lue** ; son verdict (« inscriptible » au commit `282e295e`) est celui de R-2338.
- Imports du paquet au commit `282e295e` (par `git show`, analyse des lignes `import`) : directs hors du paquet : `gardes`, `manifeste`, `scellement`, `sondes.evaluation`, `sondes.temoins`, et de T0.7 `t07.criteres_v1`, `t07.plancher_v1`, `t07.registre_v1` ; transitifs en plus : `controle_ia/__init__.py` (vide), `t07/__init__.py` (`553bd9d2…`, en-tête), `sondes/__init__.py`, `sondes/familles.py`, `harnais/__init__.py`, `harnais/sondes.py`, `premier_test_ia/__init__.py`, `premier_test_ia/statistiques.py`, `prereg.py` — **aucun autre module de T0.7** que les trois cités ; les transitifs hors de T0.7 ne sont pas dans la liste décidée par R-2339 (observation, non écrite au texte). Empreintes au commit `282e295e` (égales à `6c98ea20` et à C7) : `scellement.py` `93beeb1c…`, `gardes.py` `a83c48ce…`, `criteres_v1.py` `12b999fe…`, `plancher_v1.py` `ac6e8263…`, `registre_v1.py` `e5023657…`.
- `lecture_v1.reserves_t07_recopiees` au commit `282e295e` (l. 653-682) : `resultat.reserves` absent ou nul → rien ; présent mais pas une liste, ou entrée qui n'est pas une chaîne → `GardeArret` « … : arrêt, nœud » (après le manifeste : code 3, `arret-accb6.json`, rapport du développeur v2, § 3).

## 2. Le message de la mère, point par point

1. **Q-1** : C5-08 (G5-01) = le couple préparé au candidat 4, recopié tel quel (contrôle 1 du script contre `proposes_non_appliques` du fichier `d9dbbb8d…`). « Écrit par la session mère » figure déjà dans la table « Lignes de registre » (ligne `CODE-ACCB6`).
2. **Q-3** : C5-09 (G5-02, plan, point 2) et C5-11 (G5-04, liste d'arrêt) : la vérification au lancement porte sur `sondes/evaluation.py`, `sondes/temoins.py`, `manifeste.py`, `scellement.py`, `gardes.py` et les trois modules de T0.7 importés (`criteres_v1.py`, `plancher_v1.py`, `registre_v1.py`), empreintes au commit `282e295e` écrites dans cet ordre ; conséquence gardée : « un écart : aucun lancement, nœud ».
3. **Q-4** : C5-10 (G5-03) : ligne neuve de « Liste d'arrêt » pour `resultat.reserves` hors de forme (arrêt après le manifeste, code 3, nœud ; absent ou nul : rien, sans arrêt).
4. **Essais** : C5-12 (section « Code ») : 207 essais passés, 1 sauté, au commit fils `536dd83e…` (paquet de `282e295e`, `CODE-ACCB6` inchangé) ; C5-14 (« Reste », pas 2) : `CODE-ACCB6` reste à `282e295e` aux candidats 4 et 5.
5. **Mis à jour en plus, hors sections gelées, déclaré** : le pas 1 de « Reste » (C5-13) et la fin du statut (C5-05) disaient encore « reste la contre-lecture courte du code » : elle est faite (R-2338) ; C5-15 étend la vérification courte au candidat 5 (R-2339, Q-6).
6. Q-2 et Q-5 : gardés tels quels (réserves écrites, R-2339) ; aucun couple.

## 3. Les 15 couples (texte exact : `accumulation-barreau6-v1-candidat5-couples-v1.json`)

| couple | G5 | section | lieu | motif |
|---|---|---|---|---|
| C5-01 | — | titre | titre | candidat 5 (message de la mère, R-2339) |
| C5-02 | — | en-tête, auteur | auteur | rédacteur du candidat 5 |
| C5-03 | — | en-tête, date | date | heure du candidat 5 (date -u : 12:44:42 UTC) |
| C5-04 | — | en-tête, statut | statut | candidat 5 = candidat 4 + C5-01 à C5-15 ; sections gelées déclarées (R-2339) |
| C5-05 | — | en-tête, statut | statut, fin | pas restants : contre-lecture courte du code faite (R-2338) ; vérification courte jusqu'au candidat 5 (R-2339) |
| C5-06 | — | en-tête, documents qui font foi | documents, candidat 5 | documents du candidat 5 (R-2338, R-2339) |
| C5-07 | — | Ce que les auteurs savaient avant le scellement | ce que les auteurs savaient | lectures du candidat 5 |
| C5-08 | G5-01 | Plan d'analyse | Q-1 | Q-1 du candidat 4, appliqué tel que préparé (R-2339 ; R-2277) |
| C5-09 | G5-02 | Plan d'analyse | Q-3, plan | Q-3 (R-2339) : scellement.py, gardes.py et les modules de T0.7 importés par le paquet |
| C5-10 | G5-03 | Liste d'arrêt | Q-4 | Q-4 (R-2339) : arrêt du code v2 sur resultat.reserves hors de forme (écart E-3, R-2336) |
| C5-11 | G5-04 | Liste d'arrêt | Q-3, liste d'arrêt | Q-3 (R-2339) : même liste qu'au plan, point 2 |
| C5-12 | — | Code | code, essais | essais comptés au commit fils 536dd83e (R-2339) ; contre-lecture courte (R-2338) |
| C5-13 | — | Reste avant le scellement | reste, pas 1 | contre-lecture courte faite (R-2338) |
| C5-14 | — | Reste avant le scellement | reste, pas 2 | CODE-ACCB6 reste à 282e295e (R-2339) |
| C5-15 | — | Reste avant le scellement | reste, pas 5 | vérification courte jusqu'au candidat 5 (R-2339, Q-6) |

## 4. Changements en sections gelées, G5-01 à G5-04 (exacts)

### G5-01 — C5-08 — Plan d'analyse

- **Motif** : Q-1 du candidat 4, appliqué tel que préparé (R-2339 ; R-2277)
- **Ancien** (candidat 4) :

~~~text
(`{commit, fichiers, entropie}`, écrit par `code_accb6_v1 ecrire`)
~~~

- **Nouveau** (candidat 5) :

~~~text
(`{commit, fichiers, entropie}`, écrit par `code_accb6_v1.ecrire_fichier_code` avec l'entropie de R-2274, jamais par la commande `code_accb6_v1 ecrire` ; R-2277)
~~~

### G5-02 — C5-09 — Plan d'analyse

- **Motif** : Q-3 (R-2339) : scellement.py, gardes.py et les modules de T0.7 importés par le paquet
- **Ancien** (candidat 4) :

~~~text
`src/controle_ia/sondes/evaluation.py`, `src/controle_ia/sondes/temoins.py` et `src/controle_ia/manifeste.py` de l'arbre lancé sont comparés, par empreinte, à ceux du commit cité par `CODE-ACCB6` (au commit `282e295e…` : `1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3`, `3b051b6fc2d78eeb4a44aab8a385bbce65095998e944b80e5f2a66e21b57faf7`, `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d`)
~~~

- **Nouveau** (candidat 5) :

~~~text
`src/controle_ia/sondes/evaluation.py`, `src/controle_ia/sondes/temoins.py`, `src/controle_ia/manifeste.py`, `src/controle_ia/scellement.py`, `src/controle_ia/gardes.py` et les trois modules de T0.7 que le paquet importe, `src/controle_ia/t07/criteres_v1.py`, `src/controle_ia/t07/plancher_v1.py` et `src/controle_ia/t07/registre_v1.py` (R-2339), de l'arbre lancé sont comparés, par empreinte, à ceux du commit cité par `CODE-ACCB6` (au commit `282e295e…`, dans cet ordre : `1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3`, `3b051b6fc2d78eeb4a44aab8a385bbce65095998e944b80e5f2a66e21b57faf7`, `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d`, `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2`, `a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439`, `12b999fecce093372a29fb70d8c11eb7fe965f34c8746a31b399baaecc5ae8c5`, `ac6e8263293ed30c807ef91f8eab0adbcbf8e1b91d5e4c56e73dbffa1a7099dc`, `e50236574fbcd7e48ea3005eadc8bdb68d2c753d10028db7f2c365648a843cec`)
~~~

### G5-03 — C5-10 — Liste d'arrêt

- **Motif** : Q-4 (R-2339) : arrêt du code v2 sur resultat.reserves hors de forme (écart E-3, R-2336)
- **Ancien** (candidat 4) :

~~~text
Champ de T0.7 attendu absent de E1, E2, E2b ou E4 : arrêt, nœud.
- Identité des actions de E1
~~~

- **Nouveau** (candidat 5) :

~~~text
Champ de T0.7 attendu absent de E1, E2, E2b ou E4 : arrêt, nœud.
- `resultat.reserves` de E4 présent mais hors de forme (pas une liste, ou une entrée qui n'est pas une chaîne) : arrêt après le manifeste (code 3, `arret-accb6.json`), nœud ; absent ou nul : rien n'est recopié, sans arrêt (champ non exigé, absent sous G-1 ; code v2, `lecture_v1.reserves_t07_recopiees` ; écart E-3, R-2336 ; Q-4, R-2339).
- Identité des actions de E1
~~~

### G5-04 — C5-11 — Liste d'arrêt

- **Motif** : Q-3 (R-2339) : même liste qu'au plan, point 2
- **Ancien** (candidat 4) :

~~~text
Au lancement, `sondes/evaluation.py`, `sondes/temoins.py` ou `manifeste.py` de l'arbre lancé différent de celui du commit cité : aucun lancement, nœud (plan, point 2 ; CCB-7).
~~~

- **Nouveau** (candidat 5) :

~~~text
Au lancement, `sondes/evaluation.py`, `sondes/temoins.py`, `manifeste.py`, `scellement.py`, `gardes.py`, `t07/criteres_v1.py`, `t07/plancher_v1.py` ou `t07/registre_v1.py` de l'arbre lancé différent de celui du commit cité : aucun lancement, nœud (plan, point 2 ; CCB-7 ; R-2339).
~~~

Vérifié par le script (contrôles 5 à 7) : défaire les 15 couples redonne le candidat 4 à l'octet ; isolement des sept sections gelées ; **aucun mot sensible supprimé en section gelée** (liste blanche vide) ; aucun signe, seuil, niveau ni règle d'état changé ; seules additions : une précision d'écriture (G5-01), une liste allongée et une ligne d'arrêt jumelle (G5-02, G5-04), une ligne d'arrêt qui décrit un arrêt déjà codé (G5-03).

## 5. Exécution

- Constructeur des couples (bac à sable, non versé) : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/accb6-candidat4/construire_couples_c5.py` ; même fichier de couples en essai et versé (`d92609203433ccb47ec1aa6ad5885cc30df755b579083523341eca36011d19f8`).
- Script : essai à blanc dans le bac à sable, puis lancement réel à 12:49:46 UTC : code 0.

~~~text
1. Q-1 (C5-08) égal à l'octet au couple préparé du candidat 4 (d9dbbb8d…)
2-4. 15 couples, ordre du texte, chaque « ancien » une fois, aucun chevauchement ; sections réelles conformes ; 4 en sections gelées (G5-01 à G5-04)
5. défaire les couples (ordre inverse, chaque « nouveau » une fois) redonne le candidat 4 à l'octet
6. isolement : les couples hors sections gelées laissent les sept sections gelées égales à l'octet ; les couples en sections gelées ne touchent rien d'autre ; titres inchangés
          (en-tête) : C5-01, C5-02, C5-03, C5-04, C5-05, C5-06
          Ce que les auteurs savaient avant le scellement : C5-07
   GELÉE Plan d'analyse : C5-08/G5-01, C5-09/G5-02
   GELÉE Liste d'arrêt : C5-10/G5-03, C5-11/G5-04
          Code (écrit et éprouvé ; R5) : C5-12
          Reste avant le scellement : C5-13, C5-14, C5-15
7. suppressions et remplacements, mot à mot, dans les couples en sections gelées :
   G5-01 C5-08 (Plan d'analyse) : 0 remplacement(s) ou suppression(s), 20 mot(s) inséré(s) seuls
   G5-02 C5-09 (Plan d'analyse) : 1 remplacement(s) ou suppression(s), 60 mot(s) inséré(s) seuls
      « et » → « , »
   G5-03 C5-10 (Liste d'arrêt) : 0 remplacement(s) ou suppression(s), 93 mot(s) inséré(s) seuls
   G5-04 C5-11 (Liste d'arrêt) : 1 remplacement(s) ou suppression(s), 24 mot(s) inséré(s) seuls
      « manifeste.py » → « t07/registre_v1.py »
   mots sensibles supprimés en sections gelées : aucun
8. aucun marqueur <<…>> restant
9. candidat 5 écrit : brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat5.md
   controle_ia.prereg.problemes sur le candidat 5 : [] (vide)
TOUT PASSE ; candidat 5 : d4c7f96e738565ae4a9e9c1c9c834ecae3fb76f29ca24dfc1e75a269807985cb ; 266 → 267 lignes
~~~

- Batterie des gardes du script (R5 ; dossiers temporaires du bac à sable, pièces versées lues) :

~~~text
OK  | cas sain | code 0 | TOUT PASSE ; candidat 5 : d4c7f96e738565ae4a9e9c1c9c834ecae3fb76f29ca24dfc1e75a269807985cb ; 266 → 267 lignes [candidat 5 présent après le lancement]
OK  | Q-1 réécrit | code 1 | ARRÊT : Q-1 : absent, en double ou différent du couple préparé au candidat 4 ; rien d'écrit [candidat 5 absent après le lancement]
OK  | C5-10 déclaré hors section gelée | code 1 | ARRÊT : C5-10 : section réelle « Liste d'arrêt » ; déclaré gelée = False ; rien d'écrit [candidat 5 absent après le lancement]
OK  | suppression sensible (« E1, E2, E2b ou E4 ») | code 1 | ARRÊT : mot sensible supprimé en section gelée, hors de la liste blanche : {'E1': 1, 'E2': 1, 'E2b': 1, 'E4': 1} (nœud) ; rien d'écrit [candidat 5 absent après le lancement]
OK  | marqueur laissé | code 1 | ARRÊT : marqueurs restants : ['<<MARQUEUR_ESSAI>>'] ; rien d'écrit [candidat 5 absent après le lancement]
OK  | couple non réversible | code 1 | ARRÊT : C5-14 (retour) : texte cherché présent 2 fois (exactement une attendue) ; rien d'écrit [candidat 5 absent après le lancement]
OK  | ancien absent | code 1 | ARRÊT : C5-01 : « ancien » présent 0 fois dans le candidat 4 ; rien d'écrit [candidat 5 absent après le lancement]
OK  | candidat 5 présent et différent (R12) | code 1 | ARRÊT : candidat 5 déjà présent et différent (R12) ; rien d'écrit [candidat 5 présent après le lancement]
OK  | problemes non vide : candidat 5 neuf effacé | code 1 | ARRÊT : controle_ia.prereg.problemes : ['marqueur À REMPLIR restant hors des sections exigées'] ; rien d'écrit [candidat 5 absent après le lancement]
OK  | titre de niveau 2 inséré hors section gelée | code 1 | ARRÊT : titres de niveau 2 changés ; rien d'écrit [candidat 5 absent après le lancement]
TOUS CONFORMES
~~~

- `controle_ia.prereg.problemes` lancé seul sur le candidat 5 : `[]`.

## 6. Écarts et déclarations

- Commandes git de lecture au-delà de `git show <commit>:<chemin>` : `git cat-file -t`, `git log -1`, `git diff --stat 282e295e 536dd83e`, `git diff --quiet 282e295e 536dd83e -- src` ; aucune ne touche l'index, l'arbre ni une branche (écart à la lettre de la règle 4, déclaré).
- Aucun chemin interdit ouvert, aucune valeur de sonde de 7a, aucun refus d'un contrôle, aucun redémarrage du conteneur ; écritures : le candidat 5, son dossier de pièces et le bac à sable.

## 7. Fichiers rendus (chacun avec son compagnon `.sha256`)

- `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat5.md` — `d4c7f96e738565ae4a9e9c1c9c834ecae3fb76f29ca24dfc1e75a269807985cb`
- `…/accumulation-barreau6-v1-candidat5-pieces/accumulation-barreau6-v1-candidat5-couples-v1.json` — `d92609203433ccb47ec1aa6ad5885cc30df755b579083523341eca36011d19f8`
- `…/accumulation-barreau6-v1-candidat5-faire-v1.py` — `f0d7a674aa3e4cafa3fcb1bb0f5f775e85e82928a8c266c7a971341f8b7bbf91`
- `…/accumulation-barreau6-v1-candidat5-faire-v1-sortie.txt` — `5b33583c6c014ffdab87133f6e5ce72e376e6423aa7381893c2ba3fc397d889f`
- `…/accumulation-barreau6-v1-candidat5-essais-gardes-v1.py` — `015054e7d825350faad126c3abee4047b61f5633531cb242a8491f1e6d7f272d`
- `…/accumulation-barreau6-v1-candidat5-essais-gardes-v1.txt` — `7342e0954fb8a9347cde18aca5ed1f9ead2caa7bb35b5e35ea42c8dcdaca4324`
- ce journal — compagnon écrit au scellement
