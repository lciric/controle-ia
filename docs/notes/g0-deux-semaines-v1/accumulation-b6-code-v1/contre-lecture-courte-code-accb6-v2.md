# Contre-lecture courte et différentielle du code v2 du barreau 6 (`ACCB6`), commit `282e295e` — v2

- **Contre-lecteur** : sous-agent neuf, Claude Fable 5.2 (`claude-fable-5-2`), 11 novembre 2026, de 11:50 à 12:20 UTC environ (`date -u`). Autre modèle que le développeur du code v2 (Claude Opus 5.5). N'a écrit ni le barreau 6, ni son code, ni sa revérification, ni T0.7. **A lu du code de T0.7** (C7 : `t07/lecture_v4.py`, passages de `t07/reextraction_p3_v1.py`, `t07/lecture_v1.py`, `t07/criteres_v1.py`) : **exclu ensuite de tout rôle de lecteur de P3-bis.**
- **Objet** : différence `6c98ea20ab7ecfff0c7f10998b9dfad3d75cc625..282e295ec8e825b9c045bd30ebfdac3cbe55496f` (branche `prep/accumulation-b6-code-v2`), sept fichiers.
- **Règles tenues** : processeur seulement ; aucune dépense, aucune instance, aucun appel de modèle ; aucun chemin interdit ouvert (ni `diag/`, ni `runs/`, ni `donnees/` du dépôt ; rien de 7a, 7b, P3-bis, du bras d'attaque, du mode tenu à l'écart ni de l'étiqueteur) ; aucune recherche récursive sans exclusions ; jamais `env`, `printenv`, `set`, `export -p`, `/proc/*/environ` ni une valeur de clé ; aucun commit, aucune poussée, aucun `git fetch` (le commit était déjà dans le dépôt), aucun `rm -rf`.

## Verdict

**Inscriptible : `CODE-ACCB6` au commit `282e295ec8e825b9c045bd30ebfdac3cbe55496f`.** Aucun défaut du code. Les cinq questions reçoivent « oui ».

| question | réponse |
|---|---|
| 1. E-1 : 800 partout, refus à toute autre valeur | oui ; aucune conséquence oubliée dans le code (CLB6-1, CLB6-2) |
| 2. E-3 : recopie juste et complète, arrêt sain | oui ; deux remarques non bloquantes (CLB6-3, CLB6-4) |
| 3. CCB-1 : quatre lignes seulement | oui : quatre lignes, quatre octets (CLB6-5) |
| 4. Énumération : la ligne 3 seule | oui ; rejouée, égale à l'octet (CLB6-6) |
| 5. Essais | 195 passés, import tracé ; essai de la revérification v2 : 4 passés ; 7 mutations neuves : 1 tuée, 6 survivantes, **code juste sur chacune** (CLB6-7) |

Une recommandation, non bloquante pour l'inscription : verser mes sondages (pièce `test_clb6_sondages_v1.py`, 12 essais, 7 secondes) avec le prochain commit d'essais, comme CCB-1 l'a été. Ils ne touchent pas le paquet : `CODE-ACCB6` à `282e295e` resterait valide.

## 1. Lu (empreintes vérifiées par `sha256sum`)

| pièce | empreinte |
|---|---|
| revérification `reverification-t07-scelle-v1.md` | `80f06ac4f65cf798b2a25f1d2e4c56a2a21e570feb6cc307efdb2f229ecf9644` |
| rapport du développeur `rapport-developpeur-accb6-v2.md` | `72642740c15546c8424c58f0b24566c692fa9121941c1cad697a2bfd505c96f9` |
| ses 23 pièces | compagnons `.sha256` tous égaux (recalculés) |
| première contre-lecture `contre-lecture-code-accb6-v1.md` | `67614af4c82f35f98698ccf2768a259da4ca67e3c7d641e1c8a8dad63516df3c` |
| essais du contre-lecteur, source `essais-contre-lecture-v1/test_cl_accb6_v1.py` | `cb0cc8a18a7b25a3846db93dd499f8f741fa928f336578e6586c5176db5537f4` |
| couples proposés `couples-proposes-v1.json` (RV-09, RV-10 lus) | `771abfaff6a09bea103d67fa2f5521f69690c3795494fe99a815c0e71f15def7` (cité par la revérification) |
| décisions R-2281, R-2330, R-2336 | `registres/decisions.md`, lignes 2239, 2288, 2294 |
| configuration v8 de T0.7 (`sondes_par_concept`, `n_plancher`, `mode`) | `e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328` |

Code : arbre clairsemé à moi, détaché à `282e295e` (`src/`, `tests/`, `scripts/`). Empreintes du paquet et des fichiers changés **égales à celles du rapport du développeur** (§ 1 du rapport), recalculées : `etats_v1.py` `81e4a19b…`, `lecture_v1.py` `1f4c035f…`, `__init__.py` `eb43e52b…`, `code_accb6_v1.py` `2e6c3bb8…`, `garde_v1.py` `5b91bfaa…`, `phrases_v1.py` `961ea2b3…` ; `tests/test_accb6_lecture_v1.py` `f8587ea5…`, `test_accb6_etats_v1.py` `022e2f1a…`, `test_accb6_contre_lecture_v1.py` `542a7e90…` ; sortie de l'énumération `6b078d6c…`.

`git diff --stat 6c98ea20..282e295e` : sept fichiers (deux du paquet, trois d'essais, la sortie neuve de l'énumération et son compagnon). Rien d'autre dans `src/`.

## 2. Constats

**CLB6-1 — E-1 : 800 partout où il faut. Conforme.** `etats_v1.N_DIRECTIONS = 800` est la seule constante ; la garde de `ouvrir_e1` (`lecture_v1.py` l. 205-206) la lit, pour chaque sonde lue notée. Aucun autre « 200 » ne reste dans le paquet ni dans le script d'énumération ; dans les essais, il ne reste que les artefacts voulus (200, 799, 801) et un tirage de jetons sans rapport (l. 115). Refus éprouvé : artefacts à 200, 799 et 801 dans la suite (arrêt après le manifeste, `arret-accb6.json` scellé, code 3 par la commande, relance refusée) ; par mes sondages, en plus : 200 et 3 200 sur la **seconde** sonde, 3 200 sur la première, 0 direction → arrêt motivé chaque fois, aucune ligne `LECTURE-ACCB6`. Cas sain : toute la suite (jouets à 800) et l'essai aux constantes réelles (quatre sondes, 64 tâches, 10 000 tirages, code 0).

**CLB6-2 — E-1 : aucune autre conséquence de 800. Conforme.**
- *Graines* : les tâches du manifeste sont `accb6/<jeu>/<sonde>` ; les directions sont lues, jamais tirées. Rien ne dépend du nombre de directions. Entropie inchangée.
- *Règles* : quantile 0,95 des aires des directions, quantile 0,95 de leurs Δ, exclusion d'une tâche dont une direction n'est pas finie : formes inchangées, calculées sur `Pk.shape[0]` lu. `n_directions` est écrit par couple (800 dans l'essai de la revérification).
- *Mémoire et durée* : aux effectifs du texte (neuf conditions, 64 tâches, dix actions : 5 760 actions au plus), un `plancher_<k>` de 800 lignes pèse 37 Mo en double précision, soit de l'ordre de 200 Mo pour quatre sondes, copies de chargement comprises. L'essai aux constantes réelles passe en 4 à 5 minutes. Aucun risque.
- *Tailles des essais* : jouets d'environ 46 Mo ; la suite entière tient avec `tmp_path_retention_policy=failed`.
- *Non fait par le développeur, déclaré* : le recoupement de `index["n_plancher"]` (C-02, « recommandé en plus »). Sans effet : la forme du tableau est exigée, et `lecture_v4.exiger_nombre_de_directions` (C7, l. 166-178) recoupe déjà les deux à l'étape B de T0.7.
- *Hors du code* : la section « Puissance » du texte a simulé 200 directions (RV-10, déclaration au texte).

**CLB6-3 — E-3 : la recopie est juste et complète. Conforme ; une remarque mineure.** Vérifié sur C7 : `lecture_v4.reserves_plancher_figees` (l. 189-198) est la seule source de chaînes « plancher neuf de … » dans `resultat.reserves` ; elle écrit les deux formes (palier « carte », principale rapportée), toutes deux recopiées. C'est ce que dit le couple RV-09 (« palier « carte », principale rapportée »). Rien d'autre n'est recopié : les autres chaînes commencent par « contrôle négatif », par le texte des réserves de la dérivation, par « réserve gelée de T0.6 », par un identifiant « R… : » ou par « R14 : ». Le motif d'échec « plancher neuf de la sonde figée non établi » va dans `index.sondes[].echec`, jamais dans `resultat.reserves` : il n'est pas recopié comme réserve, et la sonde est en E (essai C2). Aucun doublon avec `reserves_identifiees`. Sous G-1, rien n'est lu (sondage : `resultat.reserves` hors de forme, lecture écrite, `reserves_t07` vide). Préfixe exact éprouvé (sans « de », majuscule, espace en tête : non recopiés).
*Remarque* : la sonde visée est toute sonde lue dont le nom **figure** dans la chaîne, non celle qui suit le préfixe. Sondage : avec deux noms emboîtés (`a-c1`, `a-c15`), les deux sont visées. Sans effet avec les noms de la configuration v8 (un nom par concept, préfixé par le concept ; la chaîne ne nomme que sa propre sonde, `reextraction_p3_v1.py` l. 384). Rien à changer.

**CLB6-4 — E-3 : l'arrêt sur `resultat.reserves` mal formé est sain. Conforme ; une observation.** Cas sain et artefacts dans la suite (R5) ; aucun repli silencieux ; `arret-accb6.json` scellé. Par mes sondages : chaîne vide, objet vide, 0, faux, nombre → arrêt ; entrée nulle, nombre ou liste → arrêt ; liste vide et champ nul → rien. **L'arrêt ne peut pas jouer sur une sortie de `lecture_v4`** : les cinq sources de `resultat.reserves` sont des chaînes par construction (`lecture_v1.py` l. 606, `criteres_v1.py` l. 369 et 419, `lecture_v4.py` l. 197, 647, 649).
*Observation* : cet arrêt tombe après le manifeste et après tout le calcul ; il consomme donc la lecture unique pour un champ que le texte n'exige pas. Même place que l'arrêt déjà accepté sur `reserves_identifiees`. Un contrôle de forme avant le manifeste (refus, code 2) coûterait moins, mais demanderait un commit de plus pour un cas que T0.7 ne peut pas écrire. Je ne le demande pas.

**CLB6-5 — CCB-1 : quatre lignes, rien d'autre. Conforme.** `diff` de la source (`cb0cc8a1…`) au fichier versé (`542a7e90…`) : lignes 39, 69, 70 et 301, celles du rapport ; `cmp -l` : quatre octets (« 2 » → « 8 ») ; même taille (24 186 octets). Le nombre reste écrit en dur dans la référence indépendante. Seize essais, tous passés.

**CLB6-6 — Énumération : la ligne 3 seule. Conforme.** `diff` des deux sorties : la ligne 3 (empreinte de `etats_v1.py`) et elle seule ; 2 152 lignes de part et d'autre. La sortie neuve où l'on remet l'ancienne empreinte a l'empreinte `00088af568388a4fbe381b7d80b97883b242013d99c7c5893bde54b9e741873e`. Script (`a6dbfdd8…`, inchangé) rejoué deux fois par `python -I -B` sur mon arbre : « couples 1152, jeux 343, séquence 33, phrases 604 ; cas sans état : 0 ; cas sans phrase : 0 », sortie `6b078d6c…`, égale à la sortie versée. L'ancienne sortie est intacte dans la différence.

**CLB6-7 — Essais et mutations. Conforme ; essais à compléter, recommandé.**
- *Suite* : commande de la consigne, plus le greffon d'import tracé du développeur (`6b5642a6…`) : **195 passés** en 487 s ; 31 modules tracés, tous sous mon arbre.
- *Essai de la revérification v2* (`805347dc…`) : arbre composé de `src/` de C7 et des trois fichiers d'essais de T0.7 qu'il importe (`conftest.py`, `test_t07_lecture_v1.py`, `test_t07_lecture_v2.py`), plus le paquet et les essais du barreau 6 à `282e295e` (empreintes recoupées). **4 passés** en 33 s ; 52 modules tracés, tous sous l'arbre composé. A2 : 800 directions, lecture écrite, réserve « carte » recopiée ; B2 : 200 directions, arrêt motivé, relance refusée ; C2 : bras arrêté, figées en E. Entre C7 et `282e295e`, `src/` ne diffère que par le paquet du barreau 6 et par huit fichiers de `t07/` absents de la branche (elle part d'avant C7) : les modules dont le paquet dépend sont égaux (utile à CCB-7 et à E-5).
- *Banc du développeur* : pièces recomptées : 128 tuées sur 128, deux témoins survivants, import dans la copie pour chaque course.
- *Mutations neuves*, bornées (huit courses sur copies, suite entière avec `-x` sans l'essai long, import tracé dans la copie, 900 s par course ; témoin sans effet survivant) :

| id | mutation | issue | le code réel, par mes sondages |
|---|---|---|---|
| N1 | garde du nombre jouée pour la seule sonde de rang 0 | **survit** | arrêt sur la seconde sonde à 200 et à 3 200 |
| N2 | `reserves` « faux » (chaîne vide, objet vide, 0) accepté sans arrêt | **survit** | arrêt sur chacun |
| N3 | préfixe « plancher neuf » sans « de » | **survit** | préfixe exact |
| N4 | seule la première réserve du plancher neuf recopiée | tuée (`test_reserve_plancher_neuf_recopiee_unite`) | — |
| N5 | réserves de T0.7 recopiées aussi sous G-1 (code d'avant ce commit) | **survit** | sous G-1, rien n'est lu |
| N6 | 3 200 directions acceptées en plus de 800 | **survit** | arrêt à 3 200 |
| N7 | sonde visée par le concept au lieu du nom | **survit** | non départagé (équivalent sous les noms de la v8) |

Les gardes neuves ont chacune leur cas sain et leur artefact dans la suite (R5 tenu). Les survivantes montrent que les artefacts ne portent que sur la première sonde et sur une seule forme fautive. Ce qu'il faut : verser `test_clb6_sondages_v1.py` avec le prochain commit d'essais. **Rejoué contre chaque survivante** (copie mutée de `src/`, import tracé dans la copie) : il tue N1, N2, N3, N5 et N6 ; N7 et le témoin sans effet survivent (N7 : équivalente sous les noms de la v8).

## 3. Écarts de méthode, déclarés

1. Le script d'énumération prend son fichier de sortie en argument : mon premier appel, avec `--help`, a écrit un fichier de ce nom à la racine de mon arbre pendant que la suite tournait. Déplacé dans le bac en moins d'une minute (son empreinte était `6b078d6c…`) ; `git status` de l'arbre vide ensuite ; la suite a passé.
2. Commandes git : `worktree add`, `sparse-checkout`, `checkout`, `diff`, `show`, `archive`, `cat-file`, `rev-parse`, `merge-base`, `status`, puis `worktree remove --force`.
3. De C7, seuls `src/` et trois fichiers d'essais de T0.7 ont été extraits ; l'essai de la revérification importe l'aide `lignes_p3bis` des essais de T0.7 (lignes de registre jouets), non lue par moi. Les noms des fichiers de `src/controle_ia/` ont paru dans une liste.
4. Lus en plus de la consigne : la configuration v8 scellée de T0.7 (trois clés) et, par recherche de motif, les effectifs écrits dans le candidat 3 du barreau 6.
5. `git status` du dépôt principal a montré des noms de fichiers de P3-bis sous `docs/notes/` ; rien n'en a été ouvert.
6. Mes sondages sont rejoués contre les six survivantes et le témoin sur des copies de `src/` seul (non de la suite entière).

## 4. Pièces

Dossier `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/contre-lecture-courte-code-accb6-v2-pieces/` (chacune avec son compagnon `.sha256`) :

| pièce | rôle | sha256 |
|---|---|---|
| `test_clb6_sondages_v1.py` | mes sondages (12 passés, 1 sauté) contre le code non muté | `bbd28591d3cdc7cac180be10c05021017496423f5c362201298b111bdd3d09cf` |
| `banc_cl_v2.py` | banc des mutations neuves | `9a659cc319c685651c092caa4f9ae029823c506cf53d537a1ab15b588cc2aefe` |
| `banc-cl-v2.jsonl` | ses huit courses | `cda2bfe2c1a857ee758b63532284ab25283c8cee8194b8d81c48b7cee6a119f6` |
| `suite-accb6-code-v2-cl.txt` | suite des 195 essais | `4097d6069c66ebf9808349c0bd378e9bbc5379aeb01d3efc11a971decbbcb34c` |
| `trace-import-suite-cl.txt` | import tracé de la suite | `d6e607f73494532fab658d227c1e8c0566c78aed75cd263c5bb6cda3e0b970f4` |
| `essai-reverif-v2-cl.txt` | essai de la revérification v2 | `8eed7d0affe76a191e0c4fcbbe2703f931cc4bafaa322e7c7d29a78ed53a83da` |
| `trace-import-reverif-v2-cl.txt` | son import tracé | `ccc0eb8775c5c7213c8658ad11c96fdd3a44c20e1e2f4adba804e441c6d7d93e` |
| `banc_sondages_cl_v2.py` | mes sondages contre les mutations survivantes | `f643d705a258b82a5798242c585a3ff27a575d1458c2efd36a9682e657973af8` |
| `sondages-contre-mutations-cl-v2.jsonl` | ses sept courses | `d1f086340f682628b176661847cccf038bf97a8fa29ffb62d802ee855e092385` |

Les traces et les sorties citent les chemins de mon bac à sable, non durable.

## 5. Non fait

- Aucune relecture du paquet hors de la différence (mandat différentiel ; la première contre-lecture couvre `6c98ea20`).
- Banc du développeur non rejoué (130 courses, plus d'une heure) : ses pièces sont recomptées, non reproduites.
- Texte du barreau 6 (candidat 4, couples RV-01 à RV-11) : hors mandat.
