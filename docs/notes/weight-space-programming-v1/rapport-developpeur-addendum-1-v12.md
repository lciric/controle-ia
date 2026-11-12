# SPARKS-EXP7-NUL — additif v12 au rapport du développeur (verdict de boucle après l'arrêt)

Même rédacteur-développeur. Tâche : message de la mère du 5 novembre 2026 (≈ 08:09 UTC), après le **troisième tir** sur la
v11. Rapport de la fille : `canal/fille-2026-11-04` `69cfe34e`.

Le tir a montré deux choses :
- **l'arrêt marche sur Vast** : « ARRÊT OBTENU (état voulu « stopped », HTTP 200) » à 07:59:50Z, puis inventaires
  « exited/stopped » à 08:02:41 et 08:05:43, aucune relance, `DEMARRAGES=1` ;
- mais le verdict a rendu « boucle » : il comptait un inventaire pris à 07:59:39Z, **avant** l'arrêt (le conteneur n'a
  démarré qu'à 07:58:17Z, environ 4 min après la création).

Travail de 08:09 à 08:24 UTC. Interdits tenus : aucun commit sur `main`, aucune poussée, aucun `.sha256` sur `main`, aucune
location. Les sorties en cours restent au bloc-notes.

**Verdict.**
- Code v12 : branche locale `prep/sparks-exp7-nul-v12`, commit `78671d9362c82a3ef02312bcf80c076a19069d42`.
- Un commit sur `cabc06e5`, non réécrit ; 18 fichiers neufs, aucun fichier modifié.
- Liste fermée v12 conforme : « LISTE FERMÉE CONFORME : 240 fichiers ».

## 1. Ce qui change

**Amorce : inchangée sur le fond.** `amorce_instance_sparks_exp7_nul_v12.sh` est l'amorce v11, où seuls changent deux chemins
de version :
- la garde du code v12 ;
- le script d'instance v12.

Le script d'instance v12 est celui de la v11, avec la garde v12, les essais v12 et le message de commit. Une copie était
nécessaire : la garde de lancement compare la différence à la liste fermée de sa version, et une liste v11 ne connaît pas
les fichiers v12. Un essai vérifie à l'octet l'égalité des deux amorces, aux deux substitutions près ; une mutation le
prouve.

**Lanceur v12 et `vast_lecture` v12** (`src/controle_ia/sparks_exp7_nul_v12/vast_lecture.py`) :
- `journal-amorce FICHIER ATTENDUS ID` lit l'heure de la **dernière ligne « : ARRÊT OBTENU ( »** du journal de l'amorce
  (`heure_arret` ; une ligne « ARRÊT NON OBTENU » n'y compte pas). Il l'écrit dans `$ETAT_DIR/arret-<ID>.txt` et l'imprime
  (`ARRET_OBTENU=<secondes>`, ou « non lu ») ;
- `apres-creation` écrit l'heure de création dans `$ETAT_DIR/cree-<ID>.txt` ;
- `boucle ID` ne compte que les inventaires pris **après l'arrêt** (`depuis` : heure d'arrêt + 1 s) ;
  - sans heure d'arrêt lue : ceux pris après la création + 900 s (`DELAI_DEMARRAGE_S`) ;
  - sans l'une ni l'autre : tous, comme en v9, et le verdict le dit (« lectures comptées : … ») ;
  - les règles de la v9 restent : trois lectures sur au moins 300 s, « arretee » si les trois sont « exited » avec
    `cur_state` « stopped » ;
- le protocole du tir dit : journal (avec l'identifiant), **puis** les inventaires après « ARRÊT OBTENU », puis le verdict.

**Essais neufs** (`tests/test_sparks_exp7_nul_v12.py`, section 10 ; R5) :
- **troisième tir rejoué** : l'inventaire de 07:59:39 précède l'arrêt de 07:59:50.
  - Témoin, sans heure d'arrêt : « boucle », comme au tir.
  - Avec l'heure d'arrêt : « indecis », puisque deux lectures seulement suivent l'arrêt.
  - Avec un troisième inventaire : « arretee ».
- **relance réelle après l'arrêt toujours vue** (« running » entre deux « exited ») : « boucle », avec la destruction
  imprimée ;
- sans heure d'arrêt : création + 900 s, l'inventaire du démarrage ignoré ;
- `journal-amorce` écrit l'heure de l'arrêt, ignore « ARRÊT NON OBTENU », et n'écrit rien sans identifiant ni ligne
  d'arrêt ;
- `apres-creation` écrit l'heure de création ;
- amorce v12 égale à la v11, aux chemins de version près.

**Banc v12** : tout le banc v11, plus **7 mutations v12**.

**Fichiers neufs** (branche `prep/sparks-exp7-nul-v12`, chacun avec son compagnon `.sha256`) :

| Fichier | sha256 |
|---|---|
| `scripts/amorce_instance_sparks_exp7_nul_v12.sh` | `71c0d32f0af20696cd32d6e3bfab28e06baa73b8a0adfdf3e5f4cbbec3ee2e15` |
| `scripts/banc_mutations_sparks_exp7_nul_v12.py` | `d7d14fdcdbd582bc97912b1cb50281c246f31ddb5698649d01958d7de1b65aae` |
| `scripts/lancer_sparks_exp7_nul_v12.sh` | `db9b5465dae669069965323719cdb493ed4113f81972192e9ab132a47bd69176` |
| `scripts/sparks_exp7_nul_instance_v12.sh` | `12fa681007b8fd322002d5b73b9c8357b1fdfae08a9cb3b2b6a7d719546b576e` |
| `src/controle_ia/sparks_exp7_nul_v12/__init__.py` | `342c6416bea5ad2daffe8e8a32c9d27739882a8af551dad089d81ffea91f98c0` |
| `src/controle_ia/sparks_exp7_nul_v12/garde_code.py` | `2e1a252be39edd61319ea3a81dd8da891f2e18a27056a4d1355d8a5b2a7bf666` |
| `src/controle_ia/sparks_exp7_nul_v12/liste-fermee-v1.txt` | `0e044f515c1be1941549eedd0c7f868dc38f61fd30beaf77a258c7bfcdf1ddc1` |
| `src/controle_ia/sparks_exp7_nul_v12/vast_lecture.py` | `fd4b629c88d34eec92610b0f12e860b9ce37a563fc2418c30cf6cec93048b0b6` |
| `tests/test_sparks_exp7_nul_v12.py` | `354890f3aec68a1362a0b8e1d8ab50db7ad271ab2d8a7a283d31b9a5118cd396` |

## 2. Risques
1. **Le jeton GitHub de l'instance expire le 5 novembre à 10:00:36 UTC** ; un jeton neuf est attendu de Lazar.
   L'environnement de l'instance est fixé à la création. Un jeton qui expire pendant l'expérience produit, au redémarrage
   suivant, « ordres illisibles », donc une boucle présumée, donc une **destruction avec les modèles** ; en fin de phase, il
   produit « POUSSÉE NON VÉRIFIÉE ». Aucune création réelle avec un jeton qui n'irait pas jusqu'au 18 novembre (ordre v3,
   A.5).
2. **Codes v10 à v12 et brouillon 8 non contre-lus** (R-1534).
   - Le verdict dépend désormais de l'heure lue au journal de Vast, tronqué à 400 lignes.
   - Si la ligne d'arrêt n'y est plus, le repli prend la création + 900 s. Si la session n'a écrit ni l'une ni l'autre
     (version antérieure du lanceur), le verdict compte tout et le dit.
3. **Étapes 4 à 7 du tir (ordre « fin » après un arrêt, `start`, `DEMARRAGES=2`, destruction par l'amorce) non éprouvées sur
   Vast** à l'heure de cet additif ; le quatrième tir en cours les éprouve sur la v11. La copie de lots (`vastai copy`) et la
   phase causale réelle ne le sont toujours pas. La clé du conteneur voit tout le compte (R-1533, accepté).

## 3. Essais et banc

Fichiers d'essai : `tests/test_sparks_exp7_nul_v1.py` à `v4.py` et `tests/test_sparks_exp7_nul_v12.py`. Les sorties, sans `.sha256`, sont copiées dans `essais-et-banc-sparks-v12/` une fois finies. Le script des passages est `passe-v12.sh` (`1c4d08aa92cc83d9410559cef578a4220a813e0af4e4cc74e8f07bbb2b6ac615`).

| Passage | Résultat | Sortie | sha256 |
|---|---|---|---|
| Essais à la tête `78671d93` | 361 réussis, 0 échec, 0 sauté, code 0 | `essais-tete-78671d93.txt` | `977fa5ba2b78db724d42a901f5361c9b412b27a9c126d9749dd9b2bb3e134f19` |
| Essais sur le commit enfant `be84eb4d` (addendum factice, `COMMIT_CODE=78671d93…`) | 361 réussis, 0 échec, 0 sauté, code 0 | `essais-enfant-be84eb4d.txt` | `2a8a2f453c010dd5fe2b826728885807178b0d96be4975062865edf3243f5622` |
| Mutations v12 seules et témoin v12 | 7/7 tuées, témoin vert, 0 défaut, code 0 | `banc-v12-seul-78671d93.txt` | `6d6ad0b0ffdd6cf65a214d33dc879c2bb76e5fe87909a69328be5874e8b451d0` |
| Banc complet v12 (v1 à v12 : 265 mutations, 11 témoins) | **en cours à la remise** ; copié à sa fin par `passe-v12.sh` | `banc-78671d93.txt` et `.json` | ligne finale à relever |

**Banc complet v11 achevé** (commit `cabc06e5`) : `essais-et-banc-sparks-v11/banc-cabc06e5.txt` (`0563aa27bf1f013b087d02396b3042db4d9c8572e15d7fc7ef63317749d496df`, `.json` `b64ca1ae10a976fc4971f5744527593f8d7ded3a4e1f0872690269142f4b10cd`), **258/258 tuées**, dont 13/13 v11, 10 témoins verts, 0 défaut, code 0.

Pendant l'écriture, l'essai v12 a été joué deux fois sur des fichiers non committés (R4) :
- un passage ciblé : 17 réussis, 1 sauté ;
- l'essai de l'heure d'arrêt seul : 1 réussi. Il a été rejoué après réordonnancement du journal d'essai, pour que la mutation « ARRÊT NON OBTENU pris pour l'arrêt » soit visible.

Réserve (R4) : le verdict v12 n'est éprouvé que sur des inventaires et des journaux écrits par les essais. Le prochain tir l'éprouve sur Vast.

## 5. Commandes

**Tir sur la v12** (s'il en faut un ; le quatrième tir sur la v11 éprouve déjà l'amorce, qui est identique). Même commande
que l'additif v11, avec le lanceur v12 et le commit `78671d93…`. Deux différences :
- `journal-amorce … 1 $ID` (étape 2) et `journal-amorce … 2 $ID` (étape 6) ;
- les inventaires de l'étape 3 ne comptent qu'après l'heure d'arrêt lue.

```bash
git checkout -q 78671d9362c82a3ef02312bcf80c076a19069d42
export SPARKS_REGISTRE_GO=/home/user/controle-ia-travail/registres/go.md
bash scripts/lancer_sparks_exp7_nul_v12.sh recherche
bash scripts/lancer_sparks_exp7_nul_v12.sh tir 78671d9362c82a3ef02312bcf80c076a19069d42 GO-2026-11-05-05 30 1
```

**Lancement réel** : ordre v3, `docs/procedures/ordre-fille-sparks-exp7-nul-lancement-reel-v3.md`
(`981bb7618094c6d3058bb6858b645593722fc56eec2938eb106399b89622920c`). Il remplace la v2. Il prévoit :
- un commit enfant de la v12, qui porte l'addendum scellé, son compagnon et `registres/go.md` de `main` ;
- le verdict de boucle après l'arrêt ;
- **l'échéance du jeton GitHub**, en préalable.
