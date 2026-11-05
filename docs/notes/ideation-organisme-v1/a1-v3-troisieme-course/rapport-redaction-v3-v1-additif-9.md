# Additif 9 au rapport de rédaction v3 — sonde v9 : une machine à une carte, sous GO-2026-11-05-01

Même rédacteur-développeur, 5 novembre 2026, de 00:18 à 00:49 UTC (`date -u`).

## Le fait de départ

La fille l'a établi à 00:15 et 00:16 UTC, en lecture seule, et le directeur l'a relayé. Sur Vast, **toutes** les offres
`num_gpus=0` sont des volumes de stockage (`resource_type` « disk »). Elles ne se louent pas comme machines : d'où les cinq
« no_such_ask » de la v8.

Les machines à une carte sont de type « gpu » et renseignent `cpu_ram` en Mo (par exemple : GTX 1070, 14 cœurs, 8 007 Mo,
0,055 USD/h).

Une ligne de GO neuve est inscrite sur `main` : **GO-2026-11-05-01**, calcul, 1 USD, échéance 2026-11-06, ligne 249.

La v9 porte des noms neufs (R12) ; les v1 à v8 sont inchangées. Elle porte **seulement** les points (a) à (e) de la demande. Mêmes
interdits : aucun commit, aucun `.sha256`, aucune location, aucune clé lue, aucune dépense.

## Verdict

- La sonde v9 n'accepte que des offres « gpu » à une carte, avec au moins 8 000 Mo de mémoire.
- Elle n'accepte que GO-2026-11-05-01, à exactement 1 USD.
- Dans la requête de `vastai` 1.8.3, `cpu_ram` s'exprime en **Go** : il est multiplié par 1 000 vers les Mo de l'interface,
  vérifié dans le source.
- **136 essais de la sonde v9 passent.** Le résultat de l'ensemble est en section 3.

## 1. Fichiers neufs (sha256 : section 4)

Ce sont des copies renommées de la v8 (étiquette `sonde-a1-v3-v9`, branches `donnees/sonde-hote-durable-a1-v3-v9…`, dossier
`/root/sonde-a1-v3-v9`, fichiers `sonde-v9-*`), puis modifiées :

- `src/controle_ia/sonde_hote_durable_a1_v3_v9.py` ;
- `scripts/amorce_sonde_hote_durable_a1_v3_v9.sh` : le GO exigé (GO-2026-11-05-01) et l'en-tête, rien d'autre ;
- `tests/test_sonde_hote_durable_a1_v3_v9.py` : 136 essais. Ce sont ceux de la v8, adaptés aux offres « gpu » et au GO neuf, plus
  les essais v9 qui remplacent ceux de la v5.

## 2. Ce qui change, et rien d'autre (diff exact : section 5)

**(a) Vérification d'offre propre** (`verifier_offre_sonde`, réécrite, sans passer par la garde « sans carte » du lanceur
durable) :

| critère | valeur exigée |
|---|---|
| `resource_type` | « gpu » ; « disk » est refusé explicitement (« volume de stockage, pas une machine »), toute autre valeur est refusée |
| `num_gpus` | 1 |
| `cpu_ram` | ≥ 8 000 Mo ; 0 et une valeur absente sont refusés : l'exception « non renseignée » de la v5 est retirée |
| cœurs (`cpu_cores_effective`) | ≥ 4 |
| disque | ≥ 30 |
| fiabilité | ≥ 0,98 |
| prix | ≤ 0,40 USD/h |

`offre_la_moins_chere_sonde`, la sous-commande `offre` et la boucle des essais sur « no_such_ask » (v8) passent toutes par cette
vérification. La mémoire réelle reste relevée sur la machine par l'amorce (v5).

**(b) GO.**
- `GO_SONDE` vaut « GO-2026-11-05-01 » et `MONTANT_GO_SONDE_USD` vaut 1.
- `verifier_go_sonde` est propre à la v9 : la garde de `main` est appelée telle quelle, puis le plafond doit être exactement 1 USD
  sur la ligne et sur chaque extension.
- La vérification est faite par le pilote, par la machine et par l'amorce.
- GO-2026-11-04-09 et GO-2026-11-04-06 sont refusés.

**(c) Commande de recherche** :
`num_gpus=1 rentable=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=30 dph_total<=0.40` (section 6).

J'ai vérifié le sens de `cpu_ram` par un essai qui lit le source de `vastai` 1.8.3 sans l'exécuter :
- sdist de PyPI `vastai-1.8.3.tar.gz`, sha256 `bb4911f7ddb5036363affbeec6fe2faa5b11eae0b5810b34646a5b3482605778` ;
- `vastai/api/query.py`, `d4aa31e6…` ; `vastai/cli/commands/offers.py`, `73b9b6df…` ;
- essai `…/scratchpad/v3b1/essai_cpu_ram_vastai.py`, qui lit l'arbre syntaxique sans rien exécuter ;
- sortie `…/sorties/essai-cpu-ram-vastai.json`.

Ce que l'essai établit :
- `offers_mult` vaut `{"cpu_ram": 1000, "gpu_ram": 1000, "gpu_total_ram": 1000}` ;
- `parse_query` multiplie la valeur par ce facteur ;
- l'aide de `search offers` dit « cpu_ram: float system RAM in gigabytes ».

Donc, dans la requête, **`cpu_ram>=8` signifie au moins 8 Go**, c'est-à-dire `cpu_ram >= 8000` en Mo dans l'interface. C'est le
même seuil que la vérification (a), exprimée en Mo sur la réponse brute.

Fait relevé au passage : la requête par défaut de `search offers` contient déjà `verified`, `external` faux et `rentable` vrai
(`offers.py`). Le filtre `verified=true` retiré par R-1490 reste donc appliqué par défaut, sauf s'il est remplacé dans la requête.

**(d) Image.** L'image reste celle de la v8, `python:3.13-bookworm`.
- La sonde n'utilise pas la carte : aucun pilote, aucune bibliothèque CUDA, aucun calcul sur elle.
- Sur Vast, l'environnement d'exécution de NVIDIA ajoute le pilote de l'hôte au conteneur. Une image sans CUDA démarre donc comme
  sur une machine sans carte, et le script de démarrage, l'amorce et Python ne touchent pas la carte.
- **Réserve** : cela n'est vérifiable que par la sonde elle-même. Le journal versé (faits de l'hôte, durée des installations) le
  dira.

**(e) Essais.**
- Cas sain : une offre « gpu » conforme (GTX 1070, 14 cœurs, 8 007 Mo, 0,055 USD/h).
- Artefacts d'offre :
  - « disk », avec ou sans carte ;
  - `resource_type` absent ou « cpu » ;
  - deux cartes, zéro carte, une carte en booléen ;
  - `cpu_ram` à 0, absent ou à 4 000 ;
  - 2 cœurs, disque à 20, fiabilité à 0,9, prix à 0,41.
- La moins chère ignore les volumes et les machines à deux cartes. Si toutes les offres sont des volumes, la sous-commande `offre`
  rend 2.
- GO :
  - cas sain sur un registre factice et sur le vrai registre de `main` (échéance 2026-11-06) ;
  - GO-2026-11-04-09 et GO-2026-11-04-06 refusés ;
  - 2 USD refusés ;
  - le 7 novembre, hors de la période de validité.
- GO-2026-11-04-09 est aussi refusé par `louer` (rien créé), par la machine (branche de refus, rien lancé) et par l'amorce.
- **Dates.** Tous les essais de la v9 passent leur date explicitement (`JOUR` = 2026-11-05, et `aujourd_hui` aux fonctions). Aucun
  ne la prend à la collecte : le passage de minuit ne change rien.
  - L'essai qui avait échoué au passage de minuit est dans `tests/test_garde_calcul.py`. Ce fichier existait déjà et n'est pas
    modifié (interdit). Sa correction demanderait une version neuve de ce fichier d'essais, à décider à part.

## 3. Essais (`timeout 900 nice -n 10`, aucun réseau vers Vast ni vers un modèle)

- `tests/test_sonde_hote_durable_a1_v3_v9.py` : **136 passés**.
- Ensemble (v9 à v1, lanceur durable, garde de calcul) : **851 passés**, aucun sauté, en 1 419 s
  (136 + 126 + 113 + 95 + 86 + 72 + 66 + 52 + 19 + 49 + 37) ; sortie `…/sorties/essais-sonde-v9.txt`
  (`ad32a7d28923a70996192e0a3cdf3b15cfe95cea7483c7fa9609935a494eb676`). La garde de calcul repasse, maintenant que la date de
  collecte et la date d'exécution sont le même jour.
- Le seul accès réseau a été le téléchargement en lecture seule du sdist et de la roue de `vastai` 1.8.3 depuis PyPI. Rien n'en a été
  exécuté.

## 4. Empreintes à la remise

Relevées le 5 novembre 2026 à 00:48 UTC.

| fichier | sha256 |
|---|---|
| `src/controle_ia/sonde_hote_durable_a1_v3_v9.py` (973 lignes) | `fb059b4926851c79c1cd1c4b8e116a90888f785e9648db92d74eed1e8de65193` |
| `scripts/amorce_sonde_hote_durable_a1_v3_v9.sh` | `80ad1d1c481f3d065fc5a2f17af8a316d1f9bbfc2a531be89e52f4cb2977b21c` |
| `tests/test_sonde_hote_durable_a1_v3_v9.py` (136 essais) | `9b15ecad9a7b1733520690aa07dd557d8caea4e2483c7f00f7007ccc1c164703` |
| bloc-notes `sorties/diff-sonde-v8-vers-v9-brut.txt` | `d70255eb32c6cb21532df9ce21ff263a2939ebe952e420b37553c4c21873c120` |
| bloc-notes `sorties/diff-sonde-v8-vers-v9-hors-renommage.txt` (377 lignes) | `907ee2c0294ab6f82b17b121e8d651e472656725d6110730e76ec4c2c8e141cd` |
| bloc-notes `renommage-v8-v9.sed` | `d45ff36a39775633bfe8a89cf17692e804b5f2d2aea4b7eeb6f44d5df9084992` |
| bloc-notes `essai_cpu_ram_vastai.py` | `766b6e6281ecfd8323fdc60a0316461cacf8076ef6312489496ea29583fa3a65` |
| bloc-notes `sorties/essai-cpu-ram-vastai.json` | `5955628c7701e9b893161f3832ce2540451bd8e782b37cce1fef0e86fefe1d93` |

Ce fichier ne porte pas sa propre empreinte : elle est donnée avec la remise. Les instantanés versés pendant le travail sont
intermédiaires ; seules ces empreintes valent pour le rendu.

## 5. Diff exact par rapport à la v8

Les diffs sont dans le bloc-notes `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/v3b1/sorties/` :
- `diff-sonde-v8-vers-v9-brut.txt`, renommages compris ;
- `diff-sonde-v8-vers-v9-hors-renommage.txt`, où la v8 est renommée par `…/v3b1/renommage-v8-v9.sed` avant la comparaison.

Le second ne contient que (a), (b) et (e).

**Module :**
- paragraphe de tête ;
- `GO_SONDE` et `MONTANT_GO_SONDE_USD` en valeurs propres ;
- fonctions neuves `verifier_go_sonde` et `_nombre` ;
- `verifier_offre_sonde`, réécrite ;
- `louer` et la machine appellent `verifier_go_sonde` au lieu de `s1.verifier_go_sonde` ;
- la ligne pour `registres/etat.md` nomme `GO_SONDE`.

**Amorce :** l'en-tête et la ligne du GO exigé.

**Essais :**
- `JOUR`, `LIGNE_09` (devenue la ligne de GO-2026-11-05-01) et `LIGNE_09_ANCIEN` ;
- `OFFRE` passe en « gpu » à une carte ;
- les artefacts « deux cartes » ;
- GO-2026-11-04-09 remplacé par GO-2026-11-05-01, et un artefact GO-09 ajouté à l'amorce ;
- la section v5 remplacée par les essais v9.

## 6. Commande exacte pour la fille

Préalables :
- crédit de Vast rechargé ;
- `vastai --version` rend `1.8.3` ;
- sonde v9 committée sur `main` du dépôt privé ;
- GO-2026-11-05-01 en cours de validité (jusqu'au 2026-11-06) ;
- rien d'autre ne tourne sous ce GO.

Dépense : environ 0,02 USD attendus (0,055 USD/h × 20 min). La borne de la minuterie est 0,40 × 3 300/3 600 ≈ 0,37 USD au pire
prix admis (tir, 1 200 s), sous le plafond de 1 USD du GO.

```
COMMIT_PRIVE=<hash complet de 40 caractères donné par le directeur>
[ "$(vastai --version 2>/dev/null)" = "1.8.3" ] || { echo "vastai 1.8.3 exigé"; exit 2; }
D=/home/user/hors-clone-sonde-a1-v3-v9; mkdir "$D" || exit 2                      # neuf (R12)
cd /home/user/controle-ia-travail && git fetch -q origin main \
 && git show origin/main:registres/go.md > "$D/registre-go-main.md" \
 && git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py" \
 && for f in hote_durable_a1_v3.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v9.py; do
      git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f" || exit 2; done \
 && timeout 300 vastai search offers 'num_gpus=1 rentable=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=30 dph_total<=0.40' -o dph_total --storage 30 --raw > "$D/offres.json" \
 && OFFRE=$(python3 -I -B "$D/sonde_hote_durable_a1_v3_v9.py" offre --offres "$D/offres.json") \
 && for V in "--verifier-seulement" ""; do
      GO_ID=GO-2026-11-05-01 env -i GO_ID=GO-2026-11-05-01 PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 \
        HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-${SSL_CERT_FILE:-}}" \
        GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" timeout 900 nice -n 10 \
        python3 -I -B "$D/sonde_hote_durable_a1_v3_v9.py" louer --go GO-2026-11-05-01 \
          --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" --offres "$D/offres.json" \
          --offre "$OFFRE" --commit-prive "$COMMIT_PRIVE" --duree-s 1200 --tir-minuterie \
          --journal-local "$D/journal-location-sonde-v9.log" $V || exit 2
    done
```

Le contrôle est celui de l'additif 6, section 6, avec `v9` à la place de `v6`. Les critères de réussite sont ceux des additifs 4 et
5, avec `sonde-a1-v3-v9`. Il faut en plus que le journal versé montre que l'image a démarré sans toucher la carte (réserve (d)).
