# Additif 4 au rapport de rédaction v3 — sonde v4 de l'hôte durable, après la contre-lecture de la v3

Même rédacteur-développeur, 4 novembre 2026, de 13:11 à 13:31 UTC (`date -u`). Ce travail applique la contre-lecture
`contre-lecture-sonde-v3.md` (sha256 `92b5abfcdc25db63ab22e115bb1ca2b87b57e121fa1a51e6eefca733f3615df7`, lue en entier, verdict
« lançable après corrections »). Il prend la forme d'une **version 4** à noms neufs (R12) ; les versions 1 à 3 restent telles
quelles. La v4 porte **seulement** les corrections M-1, m-1, m-2, f-1, f-2, f-3, f-4 et f-6 ; f-5 et R-1 restent des réserves
écrites. Mêmes interdits : aucun commit, aucun `.sha256`, aucune location, aucune clé lue, aucune dépense.

**Verdict.** Toutes les corrections demandées sont faites et éprouvées en mode jouet. **72 essais de la sonde v4 passent**, dont trois
sous `unshare -pf`. Résultat de l'ensemble : section 3.

Borne écrite, avec l'attente finale désormais comptée :
- commande recommandée (tir de la minuterie, 1 200 s, 0,40 USD/h au plus) : **0,37 USD** ;
- mode normal à 1 200 s : 0,47 USD ;
- mode normal à 1 800 s et 0,40 USD/h : 0,53 USD, désormais **refusé** par `verifier_plafond`.

## 1. Fichiers neufs (sha256 : section 4)

Chacun est une copie de la v3, renommée (étiquette `sonde-a1-v3-v4`, branches `donnees/sonde-hote-durable-a1-v3-v4…`, dossier
`/root/sonde-a1-v3-v4`, fichiers `sonde-v4-*`), puis corrigée :
- `src/controle_ia/sonde_hote_durable_a1_v3_v4.py`
- `scripts/amorce_sonde_hote_durable_a1_v3_v4.sh`
- `tests/test_sonde_hote_durable_a1_v3_v4.py` : 72 essais, dont les 66 de la v3 adaptés au renommage et à f-2

## 2. Corrections, et rien d'autre

| point | ce que fait la v4 | essais (cas sain / artefact) |
|---|---|---|
| **M-1** | Dans `_lancer`, un `subprocess.TimeoutExpired` devient `Refus("vastai … : délai dépassé (N s)")`, levé `from None`. Le message ne porte ni la ligne de commande, ni l'environnement, ni le jeton. Le délai est une constante, `DELAI_VASTAI_S` (300 s). `louer` pose le marqueur `.creation-incertaine`. | faux `vastai` lent de la démonstration, délai ramené à 1 s : `Refus` exact, sans cause chaînée, marqueur posé, aucun jeton au journal ni au marqueur / le même outil, rapide : identifiant lu |
| **m-1** | Tout `Refus` venu de `creer` après l'appel pose le marqueur : code non nul, délai, réponse illisible ou refusée. Une seconde location est refusée tant que le marqueur existe. Les gardes d'avant l'appel (clé de modèle, espace ou guillemet) lèvent `RefusAvantAppel` et ne le posent pas. | code 1 : marqueur, puis seconde location refusée / `RefusAvantAppel` : aucun marqueur |
| **m-2** | L'amorce tourne sous `timeout -k 10 "$(reste)"`, borné par la fin de vie. Chaque `apt-get` est sous `timeout -k 5 "$(borne 120)"`, et le `fetch` et le `checkout` sous `"$(borne 600)"`. Le principal sort donc peu après la fin de vie, même si l'amorce se bloque et que les `DELETE` sont refusés. | sous `unshare -pf`, amorce bloquée (`sleep 3600`) et `DELETE` 403 : « amorce finie », « fin du principal », ALARME de la minuterie, durée bornée / texte du script contrôlé ligne par ligne |
| **f-1** | L'installation de `curl` passe **après** le lancement de la minuterie, sous `timeout`. | `setsid` avant tout `apt-get` dans la v4 / ordre inverse toujours présent dans la v3 (R12) |
| **f-2** | `cout_maximal_usd` compte l'attente finale du principal (`ATTENTE_MINUTERIE_S`, 300 s). | 0,40 USD/h à 1 800 s : refus ; tir à 1 200 s : 0,367 USD |
| **f-3** | En tir, le premier contrôle a lieu à **T0 + 45**, après l'échéance de T0 + 40. En mode normal, il reste à T0 + 40. | état du tir : contrôles 13:45 et 14:10 |
| **f-4** | Préalable ajouté à la commande : `vastai --version` doit rendre 1.8.3 (section 5). | — |
| **f-6** | `controler` rend **6** quand le délai est dépassé, pour `vastai show instances` comme pour `ls-remote`. Seul le nom de la commande est écrit. | `TimeoutExpired` d'inventaire ou de signe de vie : 6 / sinon : 5 |

**Réserves, inchangées et écrites.**
- **f-5.** La minuterie sort sans nouvel essai si l'étiquette lue est différente. C'est le bon sens de sécurité, mais une étiquette
  vide, ou une clé `label` imbriquée lue la première, annulerait le tir. De son côté, `controler` refuse une étiquette `None`.
- **R-1, nœud de Lazar.** Une machine qui ne lance jamais son script, avec un pilote coupé par la limite d'usage, n'a aucune borne
  mécanique. Seule une session la borne.
- **f-f, f-g.** La facturation d'une instance « exited » et le sens de `--storage 30` sont à relever par la sonde (additif 3,
  section 3).

## 3. Essais (`timeout 900 nice -n 10`, aucun réseau)

- `tests/test_sonde_hote_durable_a1_v3_v4.py` : **72 passés**.
- Ensemble (v4, v3, v2, v1, lanceur durable, garde de calcul) : **295 passés**, aucun sauté, en 470 s
  (72 + 66 + 52 + 19 + 49 + 37) ; sortie `…/scratchpad/v3b1/sorties/essais-sonde-v4.txt`
  (`000a04d296b6ab3f1ff62b5a0334b2ecedca0aa71822747b80a8125e8f48ee8a`).
- Un premier passage a échoué sur un seul essai : le libellé de l'alarme « curl absent » avait été précisé dans la v4 (« au
  départ de la minuterie »), et l'attente de l'essai n'avait pas suivi. J'ai corrigé l'attente, puis rejoué l'ensemble.

## 4. Empreintes à la remise

Relevées à 13:30 UTC.

| fichier | sha256 |
|---|---|
| `src/controle_ia/sonde_hote_durable_a1_v3_v4.py` (705 lignes) | `d1b3425d09a794ce9a9c29ef47517b06ddb20315511ec8c10584730dd498560f` |
| `scripts/amorce_sonde_hote_durable_a1_v3_v4.sh` | `de7d1453ffa8609c5362097200368127633588be3b852ee620d44cdba3b0b4cd` |
| `tests/test_sonde_hote_durable_a1_v3_v4.py` (72 essais) | `6d6ba1add90aa35d7b1704f92a27921bb999dc1e4ab0d6759bb36c061b6a559d` |
| bloc-notes `sorties/essais-sonde-v4.txt` | `000a04d296b6ab3f1ff62b5a0334b2ecedca0aa71822747b80a8125e8f48ee8a` |

Ce fichier ne porte pas sa propre empreinte : elle est donnée avec la remise. Les instantanés versés pendant le travail sont
intermédiaires ; seules ces empreintes valent pour le rendu.

## 5. Commande exacte de la sonde v4, pour la fille

**Préalables :**
- crédit de Vast rechargé (R-1483) ;
- **`vastai --version` rend `1.8.3`** dans la session de la fille (f-4 ; R-1477) ;
- sonde v4 committée sur `main` du dépôt privé ;
- rien d'autre ne tourne sous GO-2026-11-04-09.

L'exposition du jeton est acceptée pour la seule sonde (R-1484). Mode tir recommandé ; borne : 0,37 USD au plus.

```
COMMIT_PRIVE=<hash complet de 40 caractères donné par le directeur>
[ "$(vastai --version 2>/dev/null)" = "1.8.3" ] || { echo "vastai 1.8.3 exigé"; exit 2; }
D=/home/user/hors-clone-sonde-a1-v3-v4; mkdir "$D" || exit 2                      # neuf (R12)
cd /home/user/controle-ia-travail && git fetch -q origin main \
 && git show origin/main:registres/go.md > "$D/registre-go-main.md" \
 && git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py" \
 && for f in hote_durable_a1_v3.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v4.py; do
      git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f" || exit 2; done \
 && timeout 300 vastai search offers 'num_gpus=0 rentable=true verified=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=30 dph_total<=0.40' -o dph_total --storage 30 --raw > "$D/offres.json" \
 && OFFRE=$(python3 -I -B "$D/sonde_hote_durable_a1_v3_v4.py" offre --offres "$D/offres.json") \
 && for V in "--verifier-seulement" ""; do
      GO_ID=GO-2026-11-04-09 env -i GO_ID=GO-2026-11-04-09 PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 \
        GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" timeout 900 nice -n 10 \
        python3 -I -B "$D/sonde_hote_durable_a1_v3_v4.py" louer --go GO-2026-11-04-09 \
          --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" --offres "$D/offres.json" \
          --offre "$OFFRE" --commit-prive "$COMMIT_PRIVE" --duree-s 1200 --tir-minuterie \
          --journal-local "$D/journal-location-sonde-v4.log" $V || exit 2
    done
```

**Si `louer` rend 2 après l'appel**, un fichier `…journal-location-sonde-v4.log.creation-incertaine` existe. Dans ce cas, faire
d'abord l'inventaire filtré (`python3 -I -B "$D/hote_durable_a1_v3.py" inventaire`) et ne rien relancer.

**Après la création :**
1. Recopier la ligne « LIGNE POUR registres/etat.md » dans `registres/etat.md`, committer et pousser.
2. Contrôler aux heures `controles_utc` de l'état : en tir, **T0 + 45** et **T0 + 70 min**.
3. Recontrôler toutes les 30 min tant que le code est 5 ou 6.

Bloc à relancer tel quel :

```
D=/home/user/hors-clone-sonde-a1-v3-v4
env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" \
  timeout 900 nice -n 10 python3 -I -B "$D/sonde_hote_durable_a1_v3_v4.py" controler \
    --etat "$D/journal-location-sonde-v4.log.etat.json" --journal-local "$D/journal-controle-sonde-v4.log"
```

**Codes de `controler` :**

| code | sens |
|---|---|
| 0 | instance absente, donc détruite |
| 1 | détruite par le pilote (`-y`), vérifiée ; à consigner dans `registres/arrets.md` |
| 2 | refus (étiquette autre, instance protégée, état illisible), aucun geste |
| 3 | encore listée après la destruction ; recommencer, puis consigner |
| 5 | encore listée avant ses bornes ; recontrôler |
| **6** | **délai dépassé (`vastai` ou `ls-remote`) ; recontrôler** |

**La sonde est réussie** si les quatre conditions de l'additif 3 (section 6) sont remplies, en lisant `sonde-a1-v3-v4`,
`donnees/sonde-hote-durable-a1-v3-v4` et `demarrage/sonde-v4-minuterie.log`. L'instance doit être absente avant T0 + 70 min, avec un
code 0 et sans geste du pilote.
