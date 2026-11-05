# SPARKS-EXP7-NUL — additif v11 au rapport du développeur (code v11 : arrêt par l'interface en fin de phase)

Même rédacteur-développeur. Tâche : message de la mère du 5 novembre 2026 (≈ 07:25 UTC). Le risque 1 de l'additif v10 est
retenu (R-1542) : **un conteneur qui sort est relancé par Vast.** Travail de 07:20 à 07:52 UTC (`date -u`).

Interdits tenus : aucun commit sur `main`, aucune poussée, aucun `.sha256` sur `main`, aucune location, aucun réseau. Les
sorties en cours s'écrivent au bloc-notes, et ne sont copiées dans le dépôt qu'une fois finies.

**Verdict.**
- Code v11 : branche locale `prep/sparks-exp7-nul-v11`, commit `cabc06e5d7e1c62c519990ed9709103c23cb08ec`.
- Deux commits sur `3196884f`, non réécrit : `da7116b9`, puis `cabc06e5`, qui ajoute un cas d'essai après une survivante du banc (section 3). 16 fichiers neufs, aucun fichier modifié.
- Liste fermée v11 conforme : « LISTE FERMÉE CONFORME : 222 fichiers ».
- Comptes : section 3. Troisième tir et ordre v2 : section 5.

**Banc v10 achevé** : `essais-et-banc-sparks-v10/banc-3196884f.txt` (`4a30a3d6…`, `.json` `64f2ed2b…`), **245/245 tuées**,
dont 13/13 v10, 9 témoins verts, 0 défaut, code 0.

## 1. Ce qui change (amorce v11, `scripts/amorce_instance_sparks_exp7_nul_v11.sh`, lignes au commit v11)

**(1) Arrêt en fin normale de phase** : `arreter_instance` (l. 189 à 214).
- Appel : `PUT /api/v0/instances/<CONTAINER_ID>/`, corps `{"state": "stopped"}`, clé du conteneur. C'est la requête de
  `vastai stop instance` (source 1.8.3, `api/instances.py`, `stop_instance`). Elle passe par `curl`, sinon par `python3`
  (urllib).
- **Arrêt obtenu** seulement sur HTTP 2xx **et** `"success": true` au corps. L'amorce écrit alors « <phase> : ARRÊT OBTENU
  (état voulu « stopped », HTTP n) : le conteneur sort », attend au plus 60 s (`AMORCE_ATTENTE_ARRET_S`, 10 s par défaut),
  **puis** sort.
- **Sinon** (refus, code non 2xx, réponse illisible ou vide, aucune réponse) : « ARRÊT NON OBTENU (…) : destruction ;
  perdus : les couches des modèles et du départ restées sur le disque (seules les sorties légères poussées sont gardées) »,
  puis `detruire`.
  - En fabrication, sont donc perdus : les couches de chaque modèle (`couches.safetensors`) et celles du départ, qui ne
    sont jamais poussées.
  - Restent sur `calcul/…`, si la poussée est vérifiée : les rapports, `modeles-legers.tar.gz`, les empreintes des couches,
    le journal.
  - Il faudrait refaire la fabrication.
- Les trois appels :
  - fin de la fabrication, quel que soit son code, l. 297 ;
  - fin de la fenêtre de copie, l. 336 ;
  - fin de la phase causale sans destruction, l. 349.
- Les sorties de l'amorce après un ordre consommé et refusé (borne ou prix illisibles, plafonds, gardes, lot impossible)
  restent celles de la v9. La relance suivante n'a plus d'ordre neuf, c'est une boucle, donc une destruction.

**(2) Mode jouet sur machine réelle** (l. 287 à 295). Une fabrication factice (attente de `JOUET_FABRICATION_S`, au plus
600 s), au lieu du script d'instance, si et seulement si **trois** conditions sont réunies :
- `MODE=jouet` ;
- `JOUET_MACHINE=1` ;
- l'addendum du commit lancé porte la marque factice de `addendum_factice` (v8).

Puis l'arrêt. `AMORCE_ATTENTE_FIN_S` (au plus 600 s, l. 321) retarde la destruction sur ordre « fin », pour la lecture du
journal au tir. Le mode réel ne peut pas déclencher la fabrication factice : la garde v8 refuse la marque factice hors du
mode jouet, et le bloc exige `MODE=jouet`.

**(3) Lanceur v11** (`scripts/lancer_sparks_exp7_nul_v11.sh`, mode « tir »). Le protocole du troisième tir est en section 5.

**(4) Essais neufs** (`tests/test_sparks_exp7_nul_v11.py`, section 9 ; R5) :
- **arrêt obtenu**, par `curl` et par `python3`, contre un serveur HTTP local (PUT, chemin, clé, corps `{"state":
  "stopped"}`) : sortie avec le code de la phase ;
- **arrêt refusé** : 200 avec `"success": false`, 403, et 500 avec `"success": true` (code non 2xx : cas ajouté au second commit) ;
- **réponse illisible** : 200 avec du HTML, et 200 avec un corps vide ;
- **aucune réponse** (port fermé, HTTP 000).

  Ces trois derniers cas mènent à la destruction, et la ligne dit ce qui est perdu.
- fin causale de l'amorce, arrêt obtenu ou refusé (refusé : DELETE au journal) ;
- fabrication factice seulement en `MODE=jouet` + `JOUET_MACHINE=1` + addendum marqué (un cas sain, trois artefacts) ;
- fins de phase qui arrêtent, et attentes bornées ;
- protocole du troisième tir, contrôlé à l'écrit et en statique.

Adaptation : le faux `curl` des essais écrit désormais un corps, `{"success": true}` par défaut, dans le fichier de `-o`.

**(5) Banc v11** : tout le banc v10, plus **13 mutations v11** (liste dans `scripts/banc_mutations_sparks_exp7_nul_v11.py`).

**Fichiers neufs** (branche `prep/sparks-exp7-nul-v11`, chacun avec son compagnon `.sha256`) :

| Fichier | sha256 |
|---|---|
| `scripts/amorce_instance_sparks_exp7_nul_v11.sh` | `5e6bfd981759e9887bafafb2acc426778350c0c6538a05a30a9c321acabb92c1` |
| `scripts/banc_mutations_sparks_exp7_nul_v11.py` | `37ed2a85e021b7a3be730b8b176fab423e1b09323d6e40cb8f27878ce6f2c9dc` |
| `scripts/lancer_sparks_exp7_nul_v11.sh` | `f9686bd7a6c45f5cd8612cb2a7a544f9111628488fa810bd3a55702a469a10f5` |
| `scripts/sparks_exp7_nul_instance_v11.sh` | `751856a230bde85c43f94a655c7d56fedca5e2abbf06ea4deb3a6da8baac20da` |
| `src/controle_ia/sparks_exp7_nul_v11/__init__.py` | `8c26ea115ea626ce8dabf7e52b7b5cc5f4dd0bbe780f3957ba980613e7218fdf` |
| `src/controle_ia/sparks_exp7_nul_v11/garde_code.py` | `a9f4850f9d81092b6d2a860b53f93421b076c79eb07fee546956a5451e95f5c2` |
| `src/controle_ia/sparks_exp7_nul_v11/liste-fermee-v1.txt` | `9daca0c2bccf93ef762de3c4f0e097325703550b29fd8466841fcc5744055785` |
| `tests/test_sparks_exp7_nul_v11.py` | `49bfc8c72c4a54e6a2f400a112e4875762a7699e934d33fb05eb70e3658dae9e` |

## 2. Risques
1. **L'arrêt par l'interface n'est éprouvé que contre un serveur local.** Trois points restent non éprouvés :
   - que Vast accepte ce `PUT` avec la clé du conteneur ;
   - que `cur_state` passe à « stopped » ;
   - qu'aucune relance ne suive.

   C'est l'objet du troisième tir. Un arrêt refusé détruit l'instance, avec les couches des modèles.
2. **Code v10 et v11, et brouillon 8, non contre-lus** (R-1534). La v11 touche la sortie de chaque phase.
   - Le mode jouet sur machine réelle ajoute une voie de code gardée par trois conditions.
   - `sleep infinity` après une destruction ratée laisse la carte facturée jusqu'à la session.
3. **Clé du conteneur** (R-1533, accepté) : elle sert désormais aussi à l'arrêt. Une sortie anormale après un ordre consommé
   fait encore relancer puis détruire : modèles perdus si cela arrive après la fabrication.

## 3. Essais et banc

Fichiers d'essai : `tests/test_sparks_exp7_nul_v1.py` à `v4.py` et `tests/test_sparks_exp7_nul_v11.py`. Les sorties brutes, sans `.sha256`, sont copiées dans `essais-et-banc-sparks-v11/` une fois finies. Les sorties en cours restent au bloc-notes (`…/scratchpad/sparks-v11/`). Le script des passages est `passe-v11.sh` (`6f8813e48b94138e43450f92ff2b3666194b04facf4b4b6326184367117bcebd`).

**Commit final `cabc06e5`** :

| Passage | Résultat | Sortie | sha256 |
|---|---|---|---|
| Essais à la tête | 355 réussis, 0 échec, 0 sauté, code 0 | `essais-tete-cabc06e5.txt` | `64c23529414b63adf74b23972216022ad29e822fa6c834fe3700fff7a6a981fa` |
| Essais sur le commit enfant `9260b1ad` (addendum factice, `COMMIT_CODE=cabc06e5…`) | 355 réussis, 0 échec, 0 sauté, code 0 | `essais-enfant-9260b1ad.txt` | `be69ccfcf4998166f997727928bc1ccf75d03a3ba1369b33385948080c1304cf` |
| Mutations v11 seules et témoin v11 | 13/13 tuées, témoin vert, 0 défaut, code 0 | `banc-v11-seul-cabc06e5.txt` | `8110ee5ba3d761222ffd05b24beb7ac4e5d84fadf93656bcf7f5d3e4bb70fa0a` |
| Banc complet v11 (v1 à v11 : 258 mutations, 10 témoins) | **en cours à la remise** ; copié dans le dépôt à sa fin par `passe-v11.sh` | `banc-cabc06e5.txt` et `.json` | ligne finale à relever : `code 0` et « 13/13 v11 … défauts : 0 » attendus |
| Exemple de sortie du mode tir (factice, hors réseau) | code 0 | `exemple-sortie-tir-v11.txt` | `adbe5f3b87acb6d2fac647ecff0df95cd7138206ccc10fc628a8db604c739915` |

**Premier commit `da7116b9`**, tous les runs comptés (R4), dans `commit-da7116b9/` :

| Passage | Résultat | Sortie | sha256 |
|---|---|---|---|
| Essais à la tête | 354 réussis, code 0 | `essais-tete-da7116b9.txt` | `82021bfdd72d85c7f545e3dba382f3b5273dd24f78820384c5f502560c5045b1` |
| Essais sur l'enfant `321361f5` | 354 réussis, code 0 | `essais-enfant-321361f5.txt` | `a2443a3b7631595e1df1b13526e05e081352402d73c1ce9f0ebe887cde0d8b1c` |
| Mutations v11 seules | 12/13 tuées. **Une survivante** : « code HTTP non vérifié » (un succès écrit sous un code non 2xx passait). Code 1 | `banc-v11-seul-da7116b9.txt` | `92ff4332011b0bbb08e09143bb5a410f4255eaf4e73d02b007d5ea7e12b9c78f` |
| Banc complet | interrompu par moi (numéros de processus, R10) aux témoins, le commit étant remplacé ; aucune mutation jouée | (bloc-notes, non versé) | — |

Correction de la survivante : un cas d'essai de plus (HTTP 500 avec `"success": true` → « ARRÊT NON OBTENU »), commit `cabc06e5`. Au commit final, la mutation est tuée.

Pendant l'écriture, l'essai v11 a été joué trois fois sur des fichiers non committés (R4) :
- un passage ciblé : 17 réussis, 1 sauté ;
- le fichier entier : 1 échec, sur un ancre d'essai v9 que la v11 change (« ordre fin avant la borne »), corrigé ;
- l'essai corrigé seul : 1 réussi.

Réserve (R4) : l'arrêt par l'interface n'est éprouvé que contre un serveur local et un faux `curl`. Le troisième tir l'éprouve sur Vast.

## 5. Commandes

**Troisième tir** (sous GO-2026-11-05-05, codes v10 et suivants, enveloppe commune de 5 USD ; le périmètre doit nommer
« SPARKS » et « tir », comme l'exige `sparks_exp7_nul_v9/tir.py`). Après la poussée de `prep/sparks-exp7-nul-v11` par la
mère :

```bash
cd <clone du dépôt de travail> && git fetch -q origin prep/sparks-exp7-nul-v11 && git checkout -q cabc06e5d7e1c62c519990ed9709103c23cb08ec
export SPARKS_REGISTRE_GO=/home/user/controle-ia-travail/registres/go.md     # le registre de main
bash scripts/lancer_sparks_exp7_nul_v11.sh recherche        # jouer la commande imprimée telle quelle
bash scripts/lancer_sparks_exp7_nul_v11.sh tir cabc06e5d7e1c62c519990ed9709103c23cb08ec GO-2026-11-05-05 30 1
```

Le mode tir imprime les étapes suivantes (exemple factice, hors réseau : `essais-et-banc-sparks-v11/exemple-sortie-tir-v11.txt`,
`adbe5f3b…`) :
0. Commit de tir : code + registre des GO de `main` + **addendum factice marqué**, écrit par `addendum_factice.py` tiré du
   code.
1. Création avec `MODE=jouet`, `JOUET_MACHINE=1`, `JOUET_FABRICATION_S=60`, `AMORCE_ATTENTE_FIN_S=180`,
   `AMORCE_ATTENTE_REFUS_S=300`, échéance de 30 min.
2. À T+4 min, `journal-amorce … 1`. Attendus :
   - « AMORCE V10 DEMARRAGE 1 » ;
   - « fabrication factice » ;
   - « ARRÊT OBTENU (état voulu « stopped » » ;
   - `DEMARRAGES=1`.

   « ARRÊT NON OBTENU » ou instance absente : nœud.
3. Trois inventaires sur au moins 5 minutes, puis `boucle $ID`. Attendu : « arretee » (trois « exited » avec `cur_state`
   « stopped »).
4. Ordre « fin » poussé sur `ordres/sparks-exp7-nul-v5-${TIR:0:12}`.
5. `start`, puis `apres-commande` qui lit « starting instance ID. ».
6. Dans les 3 min, `journal-amorce … 2`. Attendus :
   - « AMORCE V10 DEMARRAGE 2 » ;
   - « ordre 1 (fin) accepté et consigné » ;
   - « attente de 180 s » ;
   - `DEMARRAGES=2`, `BOUCLE=non`.
7. Inventaire « absente » : destruction par l'amorce.
8. Repli par l'identifiant.

Devis de l'exemple : 0,24 USD au plus.

**Lancement réel** : ordre v2, `docs/procedures/ordre-fille-sparks-exp7-nul-lancement-reel-v2.md`
(`f061ee684a27939b7e5ff97fcb8e0294c554552379849b32cb1dc8ff6f3d8888`).
- Commit enfant de la v11, qui porte l'addendum scellé, son compagnon et `registres/go.md` de `main`.
- Préalable : un troisième tir conforme.
- Il remplace l'ordre v1 (code v9).
