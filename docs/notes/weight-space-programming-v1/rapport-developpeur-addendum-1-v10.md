# SPARKS-EXP7-NUL — additif v10 au rapport du développeur (code v10 : après le tir réel v9)

Même rédacteur-développeur. Tâche : message de la mère du 5 novembre 2026 (06:37 UTC), après le **tir réel v9**. Rapport de
la fille : `canal/fille-2026-11-04`, commit `06a602a7`, `a51942b1…`.

Ce que le tir a montré :
- l'image `pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime` n'a pas `curl` ;
- l'amorce v9 sortait sur « curl absent » ;
- Vast a relancé le conteneur plus de 110 fois en 8 minutes ;
- `journal-amorce` v9 rendait `REDEMARRAGES=0`, aveugle à ce cas ;
- la fille a détruit l'instance par son identifiant, pour ≈ 0,0095 USD.

Travail de 06:40 à 07:18 UTC (`date -u`). Interdits tenus : aucun commit sur `main`, aucune poussée, aucun `.sha256` sur
`main`, aucune location, aucun réseau.

**Verdict.**
- Code v10 : branche locale `prep/sparks-exp7-nul-v10`, commit `3196884f80aae437913acdf677026f7788d507dc`.
- Un commit sur `4d07d2a6`, non réécrit ; 18 fichiers neufs, aucun fichier modifié.
- Liste fermée v10 conforme : « LISTE FERMÉE CONFORME : 206 fichiers ».
- Comptes : section 4. Second tir : section 5. **Nœud avant toute expérience réelle** : section 3, risque 1.

## 1. Ce qui change (amorce v10, `scripts/amorce_instance_sparks_exp7_nul_v10.sh`, lignes citées au commit v10)

**(1) Premier geste en bash seul, puis les outils.**
- **Ligne de démarrage** (l. 71 à 75) : `AMORCE V10 DEMARRAGE <n> : <date UTC>, machine <id>, commit <commit>`.
  - Le compteur `<n>` est gardé sur le disque (`sparks-v10-demarrages-amorce.txt`).
  - Rien n'est appelé hors de bash : `read`, l'arithmétique, `printf %()T` avec `TZ=UTC`.
  - Si la racine est inaccessible : `sleep infinity`, dit au journal.
- **Minuterie écrite en bash seul, avant tout outil** (`read -d ''` puis `printf`, l. 76 et 126 ; plus de `cat`).
  - Son DELETE passe par `supprimer` (l. 84 à 103) : `curl` s'il est là, sinon **`python3` (urllib)**, avec la clé lue dans
    l'environnement et le corps écrit au disque.
  - Ni l'un ni l'autre : alarme « ni curl ni python3 », code 5.
- **Outils exigés** (`OUTILS`, l. 135) : `curl git python3 timeout setsid sha256sum tar gzip awk sed sort cut tail head
  mktemp find grep date sleep cat tr`.
  - Ce sont les outils que l'amorce, sa minuterie et le script d'instance appellent : clone et ordres (`git`, `tar`) ;
    gardes et registre (`python3`, `timeout`) ; minuterie (`setsid`, `date`, `sleep`, `grep`) ; sorties (`sha256sum`,
    `find`, `tar -czf` donc `gzip`) ; `awk`, `sed`, `sort`, `cut`, `tail`, `head`, `mktemp`, `cat`, `tr`.
  - Les absents sont installés par `apt-get update` puis `apt-get install --no-install-recommends ca-certificates …`, **chacun
    sous `timeout`** (300 s ; `AMORCE_T_APT_S` peut raccourcir, jamais allonger), l. 138 à 149. Correspondance outil →
    paquet : `paquet`, l. 137.
  - Encore absents après installation : destruction immédiate.
  - `pip` et `venv` relèvent du `python3` de l'image : le script d'instance installe ses paquets par
    `pip install -r requirements-gpu.txt`, et un refus d'installation y est déjà un arrêt.

**(2) Tout refus avant l'ordre consommé détruit l'instance, au lieu de sortir.**
- **Avant la minuterie de ce démarrage** (outils, échéance illisible) : `destruction_immediate` (l. 127 à 133) joue la
  minuterie tout de suite (échéance 0), en direct.
- **Après** : `refus` (l. 178 à 182) pose `sparks-v5-detruire`, puis attend la minuterie de ce démarrage.
  - Il couvre 11 refus du chemin de création, les variables absentes (l. 190, au lieu de `${…:?}`, qui sortait en code 1),
    `COMMIT`, `BRANCHE_PREFIXE` et la consignation d'un démarrage.
  - `boucle` couvre les refus du redémarrage avant l'ordre (v9).
- **Destruction non obtenue** (minuterie finie en code non nul, ou encore vivante) : `resultat_destruction` (l. 171 à 176)
  écrit « destruction non obtenue (…) : sleep infinity pour ne pas boucler ; la session détruit par l'identifiant », puis
  `sleep infinity`.
- `AMORCE_ATTENTE_REFUS_S`, entier borné à 600 s, retarde la destruction d'un refus pour la lecture du journal. Le second tir
  passe 300 s.
- Après l'ordre consommé, les sorties de la v9 restent. La relance suivante n'a plus d'ordre neuf, c'est une boucle, donc une
  destruction.

**(3) `journal-amorce` v10** (`src/controle_ia/sparks_exp7_nul_v10/vast_lecture.py`, `demarrages`).
- Les démarrages comptés sont le plus grand des nombres suivants :
  - le plus grand rang « AMORCE V10 DEMARRAGE <n> », juste même si le début du journal est coupé ;
  - le nombre de débuts des anciennes amorces (« AMORCE V5 <date> : machine ») ;
  - le nombre de lignes « curl absent ».
- Sortie : `DEMARRAGES=n ATTENDUS=a BOUCLE=oui|non`, code 8 si `n > a`. Le lanceur v10 passe `ATTENDUS` (1 au tir).
- Le journal du tir v9 se lit désormais `BOUCLE=oui` (essai neuf).

**(4) Script d'instance v10 et lanceur v10.** Copies de la v9, avec la garde du code v10, les essais v10 et l'amorce v10.
- Mode « tir » v10 : création avec `AMORCE_ATTENTE_REFUS_S=300`, puis lecture du journal entre T+3 et T+5 min (attendus :
  1 démarrage, `BOUCLE=non`).
- Inventaire « absente » attendu à T+10 min au plus : l'amorce se détruit en refusant à la garde du code.
- Sinon : verdict `boucle`, destruction par l'identifiant, nœud.

**(5) Essais neufs** (`tests/test_sparks_exp7_nul_v10.py`, section 8, un cas sain et un artefact pour chaque garde, R5) :
- ligne de démarrage horodatée, en premier, comptée sur deux démarrages ; `journal-amorce` rend `DEMARRAGES=2`, `BOUCLE=oui`,
  code 8 ;
- refus à la création qui détruit, avec l'attente de 1 s ;
- destruction non obtenue, qui donne `sleep infinity` : le conteneur ne sort pas (délai), joué en `unshare -pf` ;
- attente bornée à 600 s ;
- **image sans `curl` ni `git`** : `PATH` sans eux, faux `apt-get` qui les installe ; installation sous `timeout`, puis
  outils présents, puis refus, puis destruction ;
- **image sans `curl`, `git` ni `python3`**, avec un `apt-get` en échec : destruction immédiate impossible (« ni curl ni
  python3 »), donc `sleep infinity` ;
- **minuterie par `python3`** contre un serveur HTTP local : DELETE reçu, chemin et clé exacts ;
- outils supposés tous couverts, chacun avec un paquet ;
- `journal-amorce` sur le journal du tir v9 (3 débuts, `BOUCLE=oui`) et sur les lignes v10.

Les essais v9 repris sont adaptés : un refus à la création détruit désormais, et le témoin « sans attente » saute aussi la
lecture du code de la minuterie.

**(6) Banc v10** : tout le banc v9, plus **13 mutations v10** (liste dans `scripts/banc_mutations_sparks_exp7_nul_v10.py`).

**Fichiers neufs** (branche `prep/sparks-exp7-nul-v10`, chacun avec son compagnon `.sha256`) :

| Fichier | sha256 |
|---|---|
| `scripts/amorce_instance_sparks_exp7_nul_v10.sh` | `280e083116c093eb01df70011e0abab58dd86d565ea819ba40373f76cf8526be` |
| `scripts/banc_mutations_sparks_exp7_nul_v10.py` | `8db3bce7260c101f025aa6d018c89e2934617a5ae568ae65f7ad28ed7e610404` |
| `scripts/lancer_sparks_exp7_nul_v10.sh` | `433c0eb7942921719871472e2116159f0197fbdf16b93fb95aa1b4154bbd3059` |
| `scripts/sparks_exp7_nul_instance_v10.sh` | `28cd22d627a13985dc48825b56bc91a80ae12ad7b8965e54a22673034e765b69` |
| `src/controle_ia/sparks_exp7_nul_v10/__init__.py` | `0c9c3f85806a94c123df2170fdbb1d196e5deccbc9582c6f29589720e2b445f2` |
| `src/controle_ia/sparks_exp7_nul_v10/garde_code.py` | `154deefd91235afbe766160c0f2f1d2da2beac3838558d486e28434beca8e9f9` |
| `src/controle_ia/sparks_exp7_nul_v10/liste-fermee-v1.txt` | `44f9dd293ff86eb9c7ec623c6d6fa14609a06415a2d8b733df955fcc5122b4e7` |
| `src/controle_ia/sparks_exp7_nul_v10/vast_lecture.py` | `97836045b3114c1ec135fb5945f52ee6205436481b9c7b84d73805803a7299de` |
| `tests/test_sparks_exp7_nul_v10.py` | `c0e999f0844d48a1d767269969fd8dd4484468832e077c5e12089936ee4cd19f` |

## 2. Ce que le second tir éprouve

- La ligne de démarrage et son compteur.
- L'installation de `curl`, `git` et `ca-certificates` par `apt-get` dans l'image réelle.
- Le refus à la garde du code, puisque le commit de tir n'a pas d'addendum.
- **La destruction par la machine elle-même**, avec la clé du conteneur : `curl` installé, ou `python3`.
- L'absence de toute relance : un seul démarrage.

Il n'éprouve pas l'arrêt d'une instance entre deux phases : voir le risque 1.

## 3. Risques

1. **L'architecture en plusieurs démarrages est contredite par le tir.** Un conteneur qui sort est relancé par Vast
   (`cur_state` reste « running »). Le dessin, lui, suppose « le conteneur sort, l'instance est arrêtée ».
   - Conséquence avec la v10 : à la fin normale de la fabrication (ou d'une fenêtre de copie), le conteneur sort. Vast le
     relance. L'amorce ne trouve aucun ordre neuf, c'est une boucle, donc une **destruction, avec les modèles**. La dépense
     reste bornée, mais l'expérience ne peut pas aller au-delà de la fabrication.
   - Nœud de Lazar avant toute création réelle. Pistes :
     - (a) l'amorce arrête elle-même l'instance par l'interface de Vast (clé du conteneur, état « stopped ») à la fin de
       chaque phase, à éprouver par un troisième tir (contre-lecture v8, point 9) ;
     - (b) une seule session de carte, de la fabrication au contrôle causal, ce qui change le texte.
2. **Code v10 et brouillon 8 non contre-lus** (R-1534). La v10 touche l'amorce sur sa ligne la plus sensible : la
   destruction par la machine.
   - `sleep infinity` laisse la carte facturée jusqu'à ce que la session détruise par l'identifiant. La minuterie, elle,
     a déjà épuisé sa marge.
   - `apt-get` dépend du réseau de l'hôte et des dépôts de l'image.
3. **Clé du conteneur** (R-1533, accepté) : elle voit tout le compte. La destruction de secours par `python3` s'en sert de la
   même façon.

## 4. Essais et banc

Fichiers d'essai : `tests/test_sparks_exp7_nul_v1.py` à `v4.py` et `tests/test_sparks_exp7_nul_v10.py`. Les sorties brutes, sans `.sha256`, sont dans `essais-et-banc-sparks-v10/` ; le script des passages est `passe-v10.sh` (`a1c34d139db195f1c36f05bb75504109bdb4bfab45f7345ecca514c21fa7804d`).

| Passage | Résultat | Sortie | sha256 |
|---|---|---|---|
| Essais à la tête `3196884f` | 340 réussis, 0 échec, 0 sauté, code 0 | `essais-tete-3196884f.txt` | `4797cf99de4e61809e1af244682e8707a5f626502eb0bc538b1ae29c10d1f7ad` |
| Essais sur le commit enfant `de75bc61` (addendum factice, `COMMIT_CODE=3196884f…`) | 340 réussis, 0 échec, 0 sauté, code 0 | `essais-enfant-de75bc61.txt` | `e70dced9d13d06c0668ed5f5e3a3b6b5a3a43d80733d2e73f041a97d2826b4a9` |
| Mutations v10 seules et témoin v10 (joués à part, pendant que le banc complet tourne) | 13/13 tuées (code 1 et « failed »), témoin v10 vert, 0 défaut, code 0 | `banc-v10-seul-3196884f.txt` | `17dc5230e767a8d4f1495c189a6b3eb1a7d165b7197b7466ac02dc2c88065a95` |
| Banc complet v10 (v1 à v10 : 245 mutations, 9 témoins) | **en cours à la remise** (07:18 UTC) : 114 tuées, 9 témoins verts, 0 autre ligne ; les mutations v10 passent en dernier | `banc-3196884f.txt` et `.json`, écrits au fil de l'eau | (ligne finale et empreinte à relever par la mère : `code 0` et « 245/245 … défauts : 0 » attendus) |
| Exemple de sortie du mode tir v10 (factice, hors réseau) | code 0 | `exemple-sortie-tir-v10.txt` | `c173fcf3fea980860e9f1fba90415482d658033389f49ad9f9d3bf0476217eb8` |

Pendant l'écriture, l'essai v10 a été joué trois fois sur des fichiers non committés (tous comptés, R4) :
- un passage ciblé, arrêté au premier échec : 1 échec, sur le faux `vastai` qui « détruisait » en repli ;
- le même passage ciblé, rejoué : 12 réussis, 1 sauté ;
- le fichier entier : 113 réussis, 1 sauté (essai du mode tir, sans commit).

Si le banc complet est coupé (redémarrage du conteneur), on le reprend par `bash essais-et-banc-sparks-v10/passe-v10.sh`, qui saute les passages finis.
Réserve (R4) : la v10 n'est éprouvée que sur processeur, avec `apt-get`, `curl` et `vastai` simulés. L'installation réelle des outils dans l'image et la destruction par la machine ne sont éprouvées que par le second tir.

## 5. Commandes

**Second tir** (sous GO-2026-11-05-02 : son périmètre nomme « SPARKS » et « tir », contrôle de `sparks_exp7_nul_v9/tir.py`).
Il ne part qu'après la poussée de `prep/sparks-exp7-nul-v10` par la mère. **La ligne de GO cite le commit v9 `4d07d2a6` :
c'est à la mère de dire si elle couvre le commit v10.**

```bash
cd <clone du dépôt de travail> && git fetch -q origin prep/sparks-exp7-nul-v10 && git checkout -q 3196884f80aae437913acdf677026f7788d507dc
export SPARKS_REGISTRE_GO=/home/user/controle-ia-travail/registres/go.md     # le registre de main (ligne du GO du tir)
bash scripts/lancer_sparks_exp7_nul_v10.sh recherche        # jouer la commande imprimée telle quelle (tir : 20 Go, aucun filtre de carte)
bash scripts/lancer_sparks_exp7_nul_v10.sh tir 3196884f80aae437913acdf677026f7788d507dc GO-2026-11-05-02 25 1
```

Le mode tir imprime alors les étapes suivantes (exemple factice, hors réseau :
`essais-et-banc-sparks-v10/exemple-sortie-tir-v10.txt`, `c173fcf3…`) :
0. le commit de tir, qui porte `registres/go.md` de `SPARKS_REGISTRE_GO` ;
1. la création, avec `-e AMORCE_ATTENTE_REFUS_S=300` ;
2. entre T+3 et T+5 min, `journal-amorce … 1`. Attendus :
   - « AMORCE V10 DEMARRAGE 1 » ;
   - « outils absents : curl git … installation (…) : code 0 » ;
   - « code ou addendum non conformes : aucun calcul : refus avant l'ordre consommé » ;
   - « attente de 300 s » ;
   - `DEMARRAGES=1`, `BOUCLE=non` ;
3. à T+10 min au plus, inventaire « absente ». Sinon : verdict `boucle`, puis destruction par l'identifiant (étape 7), puis
   nœud.

**Lancement réel : corrections à l'ordre v1** (`docs/procedures/ordre-fille-sparks-exp7-nul-lancement-reel-v1.md`,
`ee98cb31…`, écrit sur le code v9). Une version 2 de l'ordre est à écrire sur le code v10, **après le nœud du risque 1** :
- hypothèse 1 corrigée : le commit enfant porte l'addendum scellé, son `.sha256` **et `registres/go.md` de `main`** (ligne
  d'extension à 40 USD) ;
- commit enfant de `3196884f` (et non de `4d07d2a6`) : lanceur v10, amorce v10, `COMMIT_CODE=3196884f…`. Les lignes citées
  dans l'ordre v1 sont celles de la v9 et se décalent en v10 ;
- en v10, tout refus à la création détruit l'instance. L'ordre v1 disait qu'un refus laissait l'instance arrêtée ;
- `journal-amorce … ATTENDUS` : 1 à la création, puis + 1 par `start` envoyé ; `BOUCLE=oui` est un nœud.
