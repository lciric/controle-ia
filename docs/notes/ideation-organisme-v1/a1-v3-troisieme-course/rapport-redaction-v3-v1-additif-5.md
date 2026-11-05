# Additif 5 au rapport de rédaction v3 — sonde v5 : mémoire non renseignée des offres sans carte

Même rédacteur-développeur, 4 novembre 2026, de 22:32 à 22:45 UTC (`date -u`).

**Fait constaté par la fille** (22:31 UTC, lecture seule, relayé par le directeur) : sur Vast, les offres **sans carte** rendent
`cpu_ram` = 0, champ non renseigné (dix offres sur dix lues, 64 offres pour `num_gpus=0 rentable=true`). Il en découle deux blocages :
- le filtre `cpu_ram>=8` de la recherche ne rend aucune offre ;
- `verifier_offre` du lanceur durable refuse « cpu_ram = 0 < 8000 ».

En outre, `verified` vaut `None` dans les offres brutes : R-1490 a déjà retiré `verified=true` du filtre.

Version 5 à noms neufs (R12) : `hote_durable_a1_v3.py` et les v1 à v4 sont inchangés. Elle porte **seulement** les points (a) à
(d) de la demande. Mêmes interdits : aucun commit, aucun `.sha256`, aucune location, aucune clé lue, aucune dépense.

**Verdict.**
- Les offres sans carte à `cpu_ram` = 0 sont acceptées par la sonde v5, si elles ont au moins 4 cœurs.
- La mémoire réelle est relevée sur la machine et versée ; sous 2 Go, rien ne part.
- **86 essais de la sonde v5 passent.** Résultat de l'ensemble : section 3.

## 1. Fichiers neufs (sha256 : section 4)

Ce sont des copies de la v4, renommées (étiquette `sonde-a1-v3-v5`, branches `donnees/sonde-hote-durable-a1-v3-v5…`, dossier
`/root/sonde-a1-v3-v5`, fichiers `sonde-v5-*`), puis modifiées :
- `src/controle_ia/sonde_hote_durable_a1_v3_v5.py` ;
- `scripts/amorce_sonde_hote_durable_a1_v3_v5.sh` ;
- `tests/test_sonde_hote_durable_a1_v3_v5.py` : 86 essais, soit les 72 de la v4 et 14 neufs.

## 2. Ce qui change, et rien d'autre (diff exact : section 5)

- **(a) Vérification d'offre propre à la sonde** (`verifier_offre_sonde`). Elle est employée par `louer`, par
  `offre_la_moins_chere_sonde` et par la sous-commande `offre`.
  - `cpu_ram` à 0 ou absent est **non renseigné**. Il n'est accepté que si `cpu_cores_effective` ≥ 4 ; sinon : « mémoire non
    renseignée par Vast et cpu_cores_effective = … < 4 : refus ».
  - Une valeur strictement positive sous 8 000 est refusée, comme avant.
  - Tous les autres critères passent par la garde inchangée du lanceur durable : `num_gpus` = 0, disque ≥ 30, fiabilité ≥ 0,98,
    prix ≤ 0,40 USD/h.
  - Le journal de location écrit « mémoire non renseignée par Vast (cpu_ram = 0) ; N cœurs ; mémoire réelle relevée sur la
    machine ».
- **(b) Mémoire réelle relevée par l'amorce.**
  - L'amorce lit `MemTotal` de `/proc/meminfo` et l'écrit, datée, dans `sonde-v5-memoire.txt`. Le fichier est versé avec la sortie
    (dossier `demarrage/`).
  - Sous 2 Go (2 097 152 kB), ou si la valeur est illisible, l'amorce s'arrête en code 2 (« rien ne part ») et la minuterie détruit
    la machine.
  - Pour les essais, `SONDE_MEMINFO` désigne un faux `meminfo` (chemin absolu seulement).
- **(c) Commande de recherche** sans `verified=true` ni `cpu_ram>=8` (section 6).
- **(d) Essais.**
  - Cas sain : `cpu_ram` 0 et 12 cœurs, accepté et marqué. `cpu_ram` absent : accepté. Offre ordinaire à 16 000 : inchangée.
  - Artefacts : `cpu_ram` 0 et 2 cœurs ; `cpu_ram` 4 000 ; `num_gpus` 1 ; disque 20 ; fiabilité 0,9 ; prix 0,41 ; `cpu_ram`
    booléen.
  - Le lanceur durable inchangé refuse toujours l'offre à `cpu_ram` 0 : c'est l'artefact de départ.
  - Offre la moins chère : une offre à 2 cœurs moins chère n'est pas comptée. Le journal de location porte « mémoire non
    renseignée par Vast ».
  - Amorce : 16 Go et exactement 2 Go passent jusqu'à `exec` ; 1 Go et une valeur illisible donnent le code 2. Le relevé est écrit
    dans chaque cas.
  - La machine verse `demarrage/sonde-v5-memoire.txt`.

## 3. Essais (`timeout 900 nice -n 10`, aucun réseau)

- `tests/test_sonde_hote_durable_a1_v3_v5.py` : **86 passés**.
- Ensemble (v5, v4, v3, v2, v1, lanceur durable, garde de calcul) : **381 passés**, aucun sauté, en 638 s
  (86 + 72 + 66 + 52 + 19 + 49 + 37). Sortie : `…/sorties/essais-sonde-v5.txt`
  (`900c5e4dead9ebe918ba55cd431f998d70feffd3c2787ebfa27e40c8455969c0`).

## 4. Empreintes à la remise

Relevées à 22:45 UTC.

| fichier | sha256 |
|---|---|
| `src/controle_ia/sonde_hote_durable_a1_v3_v5.py` (756 lignes) | `813d28a7f225bdc5a1f4ecbdff7bab9dc7298068e934c681b2055daea4b4db7e` |
| `scripts/amorce_sonde_hote_durable_a1_v3_v5.sh` | `cf43373c322640cf8cddaec2b5d26e8526f1375c4111f3bbd2b45918d0d984cb` |
| `tests/test_sonde_hote_durable_a1_v3_v5.py` (86 essais) | `b22c41c151ba17598279b60b92d3babc30fb28e5675e61c5c8afb9808b60abe4` |
| bloc-notes `sorties/essais-sonde-v5.txt` | `900c5e4dead9ebe918ba55cd431f998d70feffd3c2787ebfa27e40c8455969c0` |
| bloc-notes `sorties/diff-sonde-v4-vers-v5-brut.txt` | `948af20d42716294774c2c421998e9f0f4306bfd5af494eb7907af4f63ccdb2a` |
| bloc-notes `sorties/diff-sonde-v4-vers-v5-hors-renommage.txt` | `b45844d119d467daf948c91441b3d253bc7bba267afcde93ece262e11dcf580d` |

Ce fichier ne porte pas sa propre empreinte : elle est donnée avec la remise. Les instantanés versés pendant le travail sont
intermédiaires ; seules ces empreintes valent pour le rendu.

## 5. Diff exact par rapport à la v4

Deux sorties, dans le bloc-notes `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/v3b1/sorties/` :
- `diff-sonde-v4-vers-v5-brut.txt` : `diff -u` des trois fichiers, renommages compris ;
- `diff-sonde-v4-vers-v5-hors-renommage.txt` : `diff -u` de la v4, une fois les renommages v4 → v5 appliqués par le même `sed`,
  vers la v5.

Ce second diff ne contient que les points (a), (b) et (d) :
- **module** :
  - le paragraphe de tête de la v5 ;
  - `FICHIERS_DEMARRAGE` avec `sonde-v5-memoire.txt`, et `MEMOIRE_MIN_KB` ;
  - les fonctions neuves `verifier_offre_sonde` et `offre_la_moins_chere_sonde` ;
  - dans `louer`, l'appel de `offre_la_moins_chere_sonde` et la ligne « mémoire non renseignée par Vast » ;
  - dans la sous-commande `offre`, `verifier_offre_sonde` à la place de `h.verifier_offre` ;
- **amorce** : deux lignes de commentaire et six lignes du relevé de `MemTotal` avec son seuil de 2 Go, avant le contrôle des
  modules ;
- **essais** : le titre, le relevé de mémoire posé dans le monde de la machine, et les 14 essais neufs.

Empreintes des deux diffs : section 4.

## 6. Commande exacte de la sonde v5, pour la fille

**Préalables :**
- crédit de Vast rechargé (R-1483) ;
- `vastai --version` rend `1.8.3` ;
- sonde v5 committée sur `main` du dépôt privé ;
- rien d'autre ne tourne sous GO-2026-11-04-09.

L'exposition du jeton est acceptée pour la seule sonde (R-1484). Mode tir recommandé ; borne : 0,37 USD au plus.

```
COMMIT_PRIVE=<hash complet de 40 caractères donné par le directeur>
[ "$(vastai --version 2>/dev/null)" = "1.8.3" ] || { echo "vastai 1.8.3 exigé"; exit 2; }
D=/home/user/hors-clone-sonde-a1-v3-v5; mkdir "$D" || exit 2                      # neuf (R12)
cd /home/user/controle-ia-travail && git fetch -q origin main \
 && git show origin/main:registres/go.md > "$D/registre-go-main.md" \
 && git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py" \
 && for f in hote_durable_a1_v3.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v5.py; do
      git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f" || exit 2; done \
 && timeout 300 vastai search offers 'num_gpus=0 rentable=true reliability>=0.98 cpu_cores_effective>=4 disk_space>=30 dph_total<=0.40' -o dph_total --storage 30 --raw > "$D/offres.json" \
 && OFFRE=$(python3 -I -B "$D/sonde_hote_durable_a1_v3_v5.py" offre --offres "$D/offres.json") \
 && for V in "--verifier-seulement" ""; do
      GO_ID=GO-2026-11-04-09 env -i GO_ID=GO-2026-11-04-09 PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 \
        GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" timeout 900 nice -n 10 \
        python3 -I -B "$D/sonde_hote_durable_a1_v3_v5.py" louer --go GO-2026-11-04-09 \
          --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" --offres "$D/offres.json" \
          --offre "$OFFRE" --commit-prive "$COMMIT_PRIVE" --duree-s 1200 --tir-minuterie \
          --journal-local "$D/journal-location-sonde-v5.log" $V || exit 2
    done
```

Si un fichier `…journal-location-sonde-v5.log.creation-incertaine` existe, faire d'abord l'inventaire filtré et ne rien relancer.

**Après la création :**
1. Recopier la ligne pour `registres/etat.md`, committer et pousser.
2. Contrôler aux heures `controles_utc` de l'état : en tir, T0 + 45 et T0 + 70 min.
3. Recommencer toutes les 30 min tant que le code est 5 ou 6.

```
D=/home/user/hors-clone-sonde-a1-v3-v5
env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" \
  timeout 900 nice -n 10 python3 -I -B "$D/sonde_hote_durable_a1_v3_v5.py" controler \
    --etat "$D/journal-location-sonde-v5.log.etat.json" --journal-local "$D/journal-controle-sonde-v5.log"
```

Les codes et les critères de réussite sont ceux de l'additif 4, lus en `sonde-a1-v3-v5` et `donnees/sonde-hote-durable-a1-v3-v5`.
Il faut en plus que `demarrage/sonde-v5-memoire.txt` soit versé, avec un `MemTotal` d'au moins 2 Go.

**Réserves inchangées :** f-5, R-1 (nœud de Lazar), f-f et f-g (additifs 3 et 4). Une de plus : la mémoire de l'offre n'est plus
connue avant la location. La seule garde est le relevé de `MemTotal` sur la machine ; sous 2 Go, rien ne part et la minuterie
détruit, au prix d'une location courte.
