# Additif 3 au rapport de rédaction v3 — sonde v3 de l'hôte durable, après la contre-lecture de la v2

Même rédacteur-développeur, 4 novembre 2026, de 12:46 à 13:04 UTC (`date -u`). Il applique la contre-lecture
`contre-lecture-sonde-v2.md` (sha256 `a8fc1079ac734275d12f78771251a9d15007a04c8f555142728fd33a67ef645d`, lue en entier, verdict
« lançable après corrections ») sous la forme d'une **version 3** à noms neufs (R12) ; la v1 et la v2 restent telles quelles.
Mêmes interdits : aucun commit, aucun `.sha256`, aucune location, aucune clé lue, aucune dépense.

**Verdict.** Toutes les corrections demandées sont faites et éprouvées en mode jouet : M-A, M-B, m-a à m-d, f-a à f-e ; f-f et
f-g sont écrits comme réserves (section 3). **66 essais de la sonde v3 passent**, dont deux dans un espace de processus à part
(`unshare -pf`). Résultat de l'ensemble : section 4. Borne écrite au pire cas : **0,50 USD** (0,40 USD/h, 30 min de sonde) ;
0,33 USD pour la commande recommandée (tir de la minuterie, 20 min). Le cas « jamais démarrée » reste borné par une session.

## 1. Fichiers neufs (sha256 : section 5)

- `src/controle_ia/sonde_hote_durable_a1_v3_v3.py` : copie renommée de la v2, puis corrections appliquées par script (bloc-notes
  `…/scratchpad/v3b1/patch_sonde_v3.py`) et par trois retouches ; bibliothèque standard seule ; importe la v1 et le lanceur
  durable, sans les modifier.
- `scripts/amorce_sonde_hote_durable_a1_v3_v3.sh`.
- `tests/test_sonde_hote_durable_a1_v3_v3.py` : 66 essais.

Étiquette `sonde-a1-v3-v3`. Branches : `donnees/sonde-hote-durable-a1-v3-v3`, puis `…-v3-refus`, `…-v3-interrompue` et
`…-v3-signe-de-vie`. Dossier de la machine : `/root/sonde-a1-v3-v3`. Fichiers du démarrage : `sonde-v3-*`.

## 2. Corrections

| point | ce que fait la v3 | essais (cas sain / artefact) |
|---|---|---|
| **M-A** contrôles | `controler` rend **5** (« listée : recontrôler ») au lieu de 0 quand l'instance est encore listée. Contrôles à **T0 + 40** et **T0 + 70 min**, écrits dans l'état à la création. Une machine listée 10 min après l'échéance finale est détruite par son identifiant, avec `-y`. | vivante à T0 + 40 : 5 ; avant la borne : 5 / listée à T0 + 70 : détruite ; instance absente : 0 |
| **M-B** échéance absolue | Le pilote pose dans le corps `ECHEANCE_UTC_S` = création + 10 min + durée + marge. Il la calcule à partir de l'heure prise juste avant la création. La minuterie prend le **minimum** de cette échéance et de la sienne (départ du conteneur + durée + marge). La machine raccourcit sa course factice pour garder 5 min au versement ; une échéance trop proche ou absente donne un refus. **Borne, comptée depuis la création** : prix × (10 min + durée + marge + 10 min de fin de vie) ; au pire 0,40 × (600 + 1800 + 1500 + 600)/3600 = **0,50 USD**. **Hors borne mécanique** : une machine qui ne lance jamais son script. Rien ne tourne alors sur elle ; seule une session la borne, par `controler`, à T0 + 30 min sans signe de vie. | échéance absolue passée : destruction aussitôt, durée de 1 800 s ignorée ; course raccourcie à 62 s / échéance absente, illisible, trop proche : refus ; corps sans échéance entière : refus |
| **m-a** arrêt | **Aucun arrêt de la machine, nulle part.** La machine se détruit, même sans versement (données factices). Si la destruction est refusée, elle laisse la minuterie faire (code 5). La minuterie recommence le `DELETE` chaque minute jusqu'à la fin de vie, sans `PUT stopped`, puis écrit une ALARME. Le commentaire faux de la v2 est retiré. | versement impossible : détruite ; scellement en `TimeoutExpired` : détruite / destruction refusée : 5, aucun geste ; `DELETE` 403 : ALARME, aucun `PUT` |
| **m-b** reprise tardive | Le principal ne sort qu'après la fin de la minuterie : attente sur son identifiant, au plus 5 min après la fin de vie. | sous `unshare -pf`, reprise après l'échéance et la fin de vie : `DELETE` fait |
| **m-c** `curl` | Installé avec `git` s'il manque. Absent, l'**amorce refuse de partir** (code 2, visible). La minuterie passe alors par `python3` (bibliothèque standard) et écrit « ALARME : curl absent ». La présence de `curl` est écrite au journal du démarrage, qui est versé. | `PATH` sans `curl` : refus de l'amorce ; minuterie par `python3`, `DELETE` tenté ; « curl NON » au journal / avec `curl` : amorce jusqu'à `exec` |
| **m-d** tir réel | Mode `--tir-minuterie` (recommandé pour la sonde) : marge courte (10 min). La machine verse **sans aucun geste** et la minuterie détruit elle-même : elle est éprouvée par un tir réel (R-1477). Les essais du script de démarrage tournent aussi dans un espace de processus à part (`unshare -pf`), comme un conteneur. | tir : versée, aucun geste de la machine (code 5) ; `unshare -pf`, chemin normal et reprise : `DELETE` fait |
| **f-a** sorties | La sortie d'erreur de `vastai` est jetée (`stderr=DEVNULL`), jamais lue. En cas d'échec, **le code seul** est écrit. | message exactement « vastai show instances : code 7 » ; aucune clé dans les refus |
| **f-b** ligne d'état | La ligne pour `registres/etat.md` renvoie à `controler` (étiquette contrôlée), et non plus à un `destroy` direct. | ligne sans `vastai destroy` |
| **f-c** commande | `D` et `COMMIT_PRIVE` sont réécrits en clair dans chaque bloc ; `nice -n 10` est ajouté au contrôle (section 6). | — |
| **f-d** clonage | `sparse-checkout set scripts src/controle_ia` avant le `fetch` partiel ; `checkout` sous `timeout 600`. | démarrage jouet : clone par le hash, amorce trouvée |
| **f-e** crochets | `RACINE_SONDE` doit être un chemin absolu, `API_VAST` commencer par `https://`, les marges être entières ; sinon les valeurs par défaut s'appliquent. Aucune de ces variables n'est dans le corps. | — |

## 3. Réserves, à relever par la sonde elle-même

- **f-f — facturation d'une instance « exited ».** Il est supposé qu'une instance « exited » ne facture plus le calcul ; ce n'est
  pas vérifié. Sur le chemin normal de la v3, la machine est détruite avant de sortir. À relever après la sonde, sur la facture du
  compte (interface de Vast, Lazar) : durée et montant facturés pour l'identifiant de la sonde, comparés à la borne de l'état
  (`cout_maximal_usd`), et toute ligne de stockage.
- **f-g — `--storage 30`.** Son sens sur `vastai` 1.8.3 n'est pas vérifiable hors réseau. À relever : le `dph_total` de l'offre
  retenue (`offres.json`) contre le prix horaire facturé.

## 4. Essais (`timeout 900 nice -n 10`, aucun réseau)

- `tests/test_sonde_hote_durable_a1_v3_v3.py` : **66 passés** en 173 s. Les deux essais `unshare -pf` ont été joués, pas
  sautés.
- Ensemble (v3, v2, v1, lanceur durable, garde de calcul) : **223 passés** en 305 s (66 + 52 + 19 + 49 + 37) ; sortie
  `…/scratchpad/v3b1/sorties/essais-sonde-v3.txt` (`25f9285fd7c54ed97b63aa85597895b3bc0179744fa3cc930ce4dca652564825`).

## 5. Empreintes à la remise

Relevées à 13:03 UTC.

| fichier | sha256 |
|---|---|
| `src/controle_ia/sonde_hote_durable_a1_v3_v3.py` (682 lignes) | `39ccc5ed30792bc622010d0a5baca7d0df4b9e265d4e09d2d7c5abb2be8847d0` |
| `scripts/amorce_sonde_hote_durable_a1_v3_v3.sh` | `59eb00674b776507b5ebacaa55c588d89ca99e86dd5aa22538addb1cdd1ebdd8` |
| `tests/test_sonde_hote_durable_a1_v3_v3.py` (685 lignes, 66 essais) | `db48ccf9226e39ee6276398db1f266546aa1d5c1599898c87538c2cac8dae18c` |
| bloc-notes `patch_sonde_v3.py` | `1823158b4a4d08aeae79930a3a2706f2c51a86e9d4125fad131469261c5845a9` |
| bloc-notes `sorties/essais-sonde-v3.txt` | `25f9285fd7c54ed97b63aa85597895b3bc0179744fa3cc930ce4dca652564825` |

Ce fichier ne porte pas sa propre empreinte : elle est donnée avec la remise. Les instantanés versés pendant le travail sont
intermédiaires ; seules ces empreintes valent pour le rendu.

## 6. Commande exacte de la sonde v3, pour la fille

Préalables :
- crédit de Vast rechargé (R-1483) ;
- sonde v3 committée sur `main` du dépôt privé ;
- rien d'autre ne tourne sous GO-2026-11-04-09.

Exposition du jeton acceptée pour la seule sonde (R-1484). Mode **tir de la minuterie** recommandé : il éprouve la destruction
par la minuterie. Borne : 0,33 USD au plus à 0,40 USD/h.

```
COMMIT_PRIVE=<hash complet de 40 caractères donné par le directeur>
D=/home/user/hors-clone-sonde-a1-v3-v3; mkdir "$D" || exit 2                      # neuf (R12)
cd /home/user/controle-ia-travail && git fetch -q origin main \
 && git show origin/main:registres/go.md > "$D/registre-go-main.md" \
 && git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py" \
 && for f in hote_durable_a1_v3.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v3.py; do
      git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f" || exit 2; done \
 && timeout 300 vastai search offers 'num_gpus=0 rentable=true verified=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=30 dph_total<=0.40' -o dph_total --storage 30 --raw > "$D/offres.json" \
 && OFFRE=$(python3 -I -B "$D/sonde_hote_durable_a1_v3_v3.py" offre --offres "$D/offres.json") \
 && for V in "--verifier-seulement" ""; do
      GO_ID=GO-2026-11-04-09 env -i GO_ID=GO-2026-11-04-09 PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 \
        GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" timeout 900 nice -n 10 \
        python3 -I -B "$D/sonde_hote_durable_a1_v3_v3.py" louer --go GO-2026-11-04-09 \
          --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" --offres "$D/offres.json" \
          --offre "$OFFRE" --commit-prive "$COMMIT_PRIVE" --duree-s 1200 --tir-minuterie \
          --journal-local "$D/journal-location-sonde-v3.log" $V || exit 2
    done
```

Après la création, recopier la ligne « LIGNE POUR registres/etat.md » du journal de location dans `registres/etat.md`, puis
committer et pousser. Ensuite, contrôler aux deux heures `controles_utc` de
`/home/user/hors-clone-sonde-a1-v3-v3/journal-location-sonde-v3.log.etat.json` (T0 + 40 et T0 + 70 min), et toutes les 30 min
tant que le code est 5. Le bloc se relance tel quel, sans variable héritée :

```
D=/home/user/hors-clone-sonde-a1-v3-v3
env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" \
  timeout 900 nice -n 10 python3 -I -B "$D/sonde_hote_durable_a1_v3_v3.py" controler \
    --etat "$D/journal-location-sonde-v3.log.etat.json" --journal-local "$D/journal-controle-sonde-v3.log"
```

Codes de `controler` :
- 0 : instance absente, donc détruite ;
- 1 : détruite par le pilote (`-y`), vérifiée ; à consigner dans `registres/arrets.md` ;
- 2 : refus (étiquette autre, instance protégée, état illisible), aucun geste ;
- 3 : encore listée après la destruction ; recommencer, puis consigner ;
- **5 : encore listée avant ses bornes, recontrôler.**

La sonde est réussie si les quatre points suivants sont vrais :
- la branche `donnees/sonde-hote-durable-a1-v3-v3` existe, et son journal porte « plafond_de_duree_de_la_sonde », « versé » et
  « tir de la minuterie : aucun geste » ;
- `demarrage/sonde-v3-minuterie.log` est versé avec son départ ;
- l'instance est **absente de l'inventaire avant T0 + 70 min, détruite par la minuterie** ;
- les relevés de f-f et f-g (section 3) sont faits.

Le journal de la minuterie, qui écrit son `DELETE`, meurt avec la machine. La preuve de la destruction est donc l'absence de
l'instance à l'inventaire, sans aucun geste du pilote (code 0 au contrôle).
