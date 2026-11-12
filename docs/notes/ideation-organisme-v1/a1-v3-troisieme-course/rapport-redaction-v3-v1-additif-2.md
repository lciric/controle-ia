# Additif 2 au rapport de rédaction v3 — sonde v2 de l'hôte durable, après la contre-lecture

Même rédacteur-développeur, 4 novembre 2026. Le travail a commencé à 10:36 UTC ; le conteneur a redémarré vers 12:20 UTC et le
travail a repris à 12:23 UTC, puis s'est terminé vers 12:40 UTC (`date -u`). Il applique la contre-lecture
`contre-lecture-sonde-v1.md` (sha256 `07ba135683b36b1ed7f73254af81f7e0ad5d63afd8ac8692386abd6e1c4b5797`, lue en entier, verdict
« lançable après corrections »), sous la forme d'une **version 2** à noms neufs (R12) ; la v1 reste telle quelle. Mêmes
interdits : aucun commit, aucun `.sha256`, aucune location, aucune clé lue, aucune dépense.

**Verdict.** Toutes les corrections demandées sont faites et éprouvées en mode jouet : M1, M2, M3, m1 à m5, m7 et f1 à f8. Le point
m6 est tranché par Lazar (R-1484, section 3). **52 essais de la sonde v2 passent** ; résultats de l'ensemble, v1, lanceur et garde
compris : section 4. La vraie sonde reste à lancer : c'est une dépense d'au plus 0,43 USD (borne de la minuterie à 0,40 USD/h ; 0,13 USD à 0,12 USD/h) sous GO-2026-11-04-09, après
recharge du crédit de Vast (R-1483).

## 1. Fichiers neufs

| fichier | sha256 |
|---|---|
| `src/controle_ia/sonde_hote_durable_a1_v3_v2.py` (628 lignes) | `a514904f6efcbfbdb0244e009e4e5566a61e66559a9ddee508b118f46ac141b9` |
| `scripts/amorce_sonde_hote_durable_a1_v3_v2.sh` | `0a2e05ac2794dca1680f8944aca772e1b648475366ae2c085b7270cb6ea8d50c` |
| `tests/test_sonde_hote_durable_a1_v3_v2.py` (531 lignes, 28 fonctions, 52 essais) | `359a7aa57acd6c3e00178815b594ee2c27d442e6fb27d0f928e383bfb751fe84` |

Le module v2 était déjà sur disque avant le redémarrage ; tu en as versé un instantané (`6315bbe9`). Après la reprise, je n'y ai
changé qu'une chose : `ClientPilote._lancer` ne lit plus que la sortie standard de `vastai`. La sortie d'erreur n'est jamais lue ni
écrite. En cas d'échec, on garde seulement le code et une ligne masquée. Les autres fichiers sont neufs. La v1
(`sonde_hote_durable_a1_v3.py`, `f7c7f79b…`) et le lanceur durable (`5b853fde…`) ne sont pas modifiés ; la v2 les importe.

## 2. Corrections

| point | ce que fait la v2 | essais (cas sain / artefact) |
|---|---|---|
| **M1** minuterie | Le script de démarrage lance **en tout premier**, par `setsid` et sans Python, une minuterie détachée. À l'échéance (départ du conteneur + `DUREE_MAX_S` + 25 min ; échéance gardée sur disque, une reprise garde celle d'origine), elle fait un `DELETE /instances/<CONTAINER_ID>/` avec la clé d'instance ; si la destruction est refusée, `PUT state=stopped`. Le conteneur reste en vie jusqu'à l'échéance + 10 min, quel que soit le code de l'amorce. `fin` et `se_detruire` attrapent toute exception, puis passent au geste de repli. | démarrage complet : minuterie, clone partiel, amorce, `DELETE` 200 / clone impossible, la minuterie détruit quand même (M1 a) ; `DELETE` 403 suivi de l'arrêt ; reprise de l'échéance d'origine ; `URLError` du versement suivi de l'arrêt ; `TimeoutExpired` du scellement suivi de l'arrêt ; destruction refusée suivie de l'arrêt ; tout refusé, code 4 ; client de Vast impossible, code 4 (M1 b) |
| **M2** `-y` | `vastai destroy instance <ID> -y` partout où le pilote détruit (`ClientPilote.detruire`, `controler`, ligne pour `registres/etat.md`). | arguments relevés : `destroy instance 777 -y` |
| **M3** clé de Vast | Le pilote exige `VAST_API_KEY` par son nom (passée par `env -i`). Elle n'est transmise qu'au sous-processus `vastai` et masquée partout. Aucune sortie brute de `vastai` n'est affichée ni écrite, car elle contient les variables d'environnement de la machine (R-1480). | clé absente : refus / sortie qui contient la clé et le jeton : rien ne ressort |
| **m1** dépense | Elle est comptée depuis le départ du conteneur (heure écrite par le script de démarrage), avec une **borne mécanique** : démarrage au plus 10 min (écrit ; c'est la borne du pilote, m2), puis destruction par la minuterie à durée + 25 min, puis sortie du conteneur 10 min plus tard. À 0,40 USD/h et 20 min de sonde : **0,43 USD au plus** ; à 0,12 USD/h : 0,13 USD. Versement borné : deux poussées, 30 s d'attente, délais `git` de 120 s. | plafond tenu à 0,40 USD/h et 30 min ; plafond de 0,10 USD : refus |
| **m2** jamais démarrée | Le pilote écrit l'état à la création (`.etat.json` : identifiant, étiquette, T0, borne T0 + 30 min, échéance finale) et une ligne pour `registres/etat.md`. `controler` détruit par l'identifiant, avec `-y`, s'il n'y a **aucun signe de vie à T0 + 30 min**. Le signe de vie est une branche orpheline poussée tôt par la machine. `controler` détruit aussi si la machine est encore listée 10 min après l'échéance finale. | absente, vivante, avant la borne : aucun geste / sans signe de vie à T0 + 31 min : détruite ; listée après l'échéance : détruite ; destruction non suivie : code 3 |
| **m3** réponse | Lue en entier (JSON indenté), puis ligne par ligne. Si elle est illisible, un marqueur « création incertaine » bloque toute nouvelle location avant l'inventaire. Une seconde location est toujours refusée (R12). | réponse sur plusieurs lignes lue / refusée, illisible ; seconde location refusée |
| **m4** commande | `COMMIT_PRIVE` posé, offre tirée de `offres.json` (sous-commande `offre`, la moins chère des conformes), `mkdir … \|\| exit`, étapes enchaînées par `&&`, contrôles à T+40 et T+60 min (section 6). | `offre` : 12 / aucune conforme : code 2 |
| **m5** clonage | Dépôt privé pris en `fetch --filter=blob:none --depth 1` du commit, chronométré. Versements sur des **branches orphelines**, sans clone de `main`. Registre et garde de `main` lus par un `fetch` partiel de profondeur 1. | démarrage jouet : clone du commit par son hash (`clone 0 en … s`) |
| **m6** jeton | Tranché par Lazar (section 3). | — |
| **m7** R5 | Cas sain et artefact pour chaque garde, amorce et script de démarrage compris. | amorce jusqu'à `exec` / jeton absent, `CLE_ARGON`, `RR_…_API_KEY_…`, GO-2026-11-04-06, durée non entière, module absent ; `DUREE_MAX_S` « abc » ou « 7200 » : refus sur la machine |
| **f1** | Aucune sortie brute ; code et une ligne masquée, toutes clés comprises. | voir M3 |
| **f2** | Liste des clés interdites commune à l'amorce et à Python (`MOTIF_AMORCE` vérifié dans l'amorce). | essai de concordance |
| **f3** | Message de commit propre à la sonde. | — |
| **f4** | Branches distinctes : `donnees/sonde-hote-durable-a1-v3-v2`, `…-v2-refus`, `…-v2-interrompue`, `…-v2-signe-de-vie`. | refus versé sur `…-refus` |
| **f5** | Heure de départ, échéance, durées du démarrage et du clonage, et journaux de l'amorce et de la minuterie, copiés dans le dossier versé avant le scellement. | présents dans la liste versée |
| **f6** | `--storage 30` dans la recherche (section 6). | — |
| **f7** | `GO_ID=GO-2026-11-04-09` en tête de la ligne de location, et exigé par `louer`. | absent : refus |
| **f8** | Étiquette `sonde-a1-v3-v2` contrôlée par la minuterie, par la machine et par le pilote avant tout geste. Les instances 58936096, 58936099 et 58936100 ne sont jamais touchées (trois endroits). | autre étiquette : aucun geste (minuterie, machine, pilote) ; instance protégée : aucun geste (minuterie, pilote) |

Écart déclaré à la proposition du contre-lecteur, pour M1 : si la minuterie ne peut pas lire l'étiquette (lecture refusée), elle
détruit par l'identifiant que Vast a posé dans le conteneur. Seule une étiquette **lue et différente** arrête le geste.

## 3. m6 — portée du jeton GitHub : décision de Lazar (R-1484)

Mot de Lazar, verbatim (vers 12:22 UTC, R-1484) : « (b) Accepter cette exposition par écrit, pour la seule course d'essai.
Avantage : rien à faire. Inconvénient : le dépôt privé entier reste exposé pendant la course. »

Lazar accepte donc que le jeton du dépôt de travail soit exposé à l'hôte tiers et aux métadonnées de Vast, **pour la seule sonde**
(GO-2026-11-04-09). La troisième course d'A1-v3, mise de côté ce jour avec Argon, redemandera la décision.

## 4. Essais (`timeout 900 nice -n 10`, aucun réseau)

- `tests/test_sonde_hote_durable_a1_v3_v2.py` : **52 passés**, en 89 s.
- Ensemble (v2, v1, lanceur durable, garde de calcul) : **157 passés** en 568 s (52 + 19 + 49 + 37), sortie
  `…/scratchpad/v3b1/sorties/essais-sonde-v2.txt` (`3c3f5a8c13c1242d7dd442ff1842fe2d525d9100dc60fe7ba3d7c2a105d6563c`).
- Les essais du démarrage jouent le vrai script de démarrage (bash) avec un `curl` factice. Le clonage se fait par le hash du
  commit depuis un dépôt local réglé comme GitHub (`uploadpack.allowFilter`, `allowReachableSHA1InWant`).

## 5. Empreintes à la remise

Empreintes relevées à 12:37 UTC, données en section 1 (les trois fichiers neufs) et en section 4 (la sortie des essais). Ce
fichier ne porte pas sa propre empreinte : elle est donnée avec la remise. Les instantanés versés pendant le travail sont
intermédiaires ; seules ces empreintes valent pour le rendu.

## 6. Commande exacte de la sonde v2, pour la fille

Préalables :
- crédit de Vast rechargé (R-1483) ;
- sonde v2 committée sur `main` du dépôt privé, au commit donné par le directeur ;
- aucune location antérieure de la sonde v2 (le pilote le vérifie lui-même).

Rien d'autre que cette sonde ne tourne sur cette clé de Vast pour ce GO.

```
COMMIT_PRIVE=<hash complet de 40 caractères donné par le directeur>
D=/home/user/hors-clone-sonde-a1-v3-v2; mkdir "$D" || exit 2                      # neuf (R12)
cd /home/user/controle-ia-travail && git fetch -q origin main \
 && git show origin/main:registres/go.md > "$D/registre-go-main.md" \
 && git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py" \
 && for f in hote_durable_a1_v3.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v2.py; do
      git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f" || exit 2; done \
 && timeout 300 vastai search offers 'num_gpus=0 rentable=true verified=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=30 dph_total<=0.40' -o dph_total --storage 30 --raw > "$D/offres.json" \
 && OFFRE=$(python3 -I -B "$D/sonde_hote_durable_a1_v3_v2.py" offre --offres "$D/offres.json") \
 && for V in "--verifier-seulement" ""; do
      GO_ID=GO-2026-11-04-09 env -i GO_ID=GO-2026-11-04-09 PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 \
        GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" timeout 900 nice -n 10 \
        python3 -I -B "$D/sonde_hote_durable_a1_v3_v2.py" louer --go GO-2026-11-04-09 \
          --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" --offres "$D/offres.json" \
          --offre "$OFFRE" --commit-prive "$COMMIT_PRIVE" --duree-s 1200 --journal-local "$D/journal-location-sonde-v2.log" $V \
        || exit 2
    done
```

Après la création :
- Recopier la ligne « LIGNE POUR registres/etat.md » du journal de location dans `registres/etat.md`, puis committer et pousser
  (m2). Toute session qui reprend la lit.
- Contrôler à **T0 + 40 min** et à **T0 + 60 min** (T0 est écrit dans `$D/journal-location-sonde-v2.log.etat.json`) :

  ```
  env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" \
    timeout 900 python3 -I -B "$D/sonde_hote_durable_a1_v3_v2.py" controler \
      --etat "$D/journal-location-sonde-v2.log.etat.json" --journal-local "$D/journal-controle-sonde-v2.log"
  ```

  Codes de `controler` :
  - 0 : rien à faire (instance absente, ou vivante avant ses bornes) ;
  - 1 : instance détruite par le pilote (`-y`) et vérifiée par l'inventaire ; à consigner dans `registres/arrets.md` ;
  - 2 : refus (étiquette autre, instance protégée, état illisible), aucun geste ;
  - 3 : instance encore listée après la destruction ; recommencer, puis consigner.

- La sonde est réussie si :
  - la branche `donnees/sonde-hote-durable-a1-v3-v2` existe, et son journal porte « plafond_de_duree_de_la_sonde », « versé » et
    « clé d'instance : lecture faite … vue » ;
  - le dossier `demarrage/` est versé (durée du clonage, installations, journal de la minuterie) ;
  - l'instance est absente de l'inventaire avant T0 + 60 min.

  Si l'instance n'est pas détruite par elle-même, l'autodestruction est à revoir avant toute course.
