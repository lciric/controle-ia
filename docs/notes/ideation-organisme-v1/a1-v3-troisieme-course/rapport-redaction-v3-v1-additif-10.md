# Additif 10 au rapport de rédaction v3 — sonde v10 : registre du canal sur la machine, relevés de facturation et de la carte

Même rédacteur-développeur, 5 novembre 2026, de 02:03 à 02:36 UTC (`date -u`).

**Résultat réel de la sonde v9**, d'après le rapport de la fille `brouillons/fille-2026-11-04/rapport-sonde-a1-v3-v9-2026-11-05-0201.md`
(`709611be…`, `canal/fille-2026-11-04` `7c01b294`), relayé par le directeur :
- **Ce qui a marché.** La machine à une carte (GTX 1070) a été louée. La minuterie a détruit l'instance à l'échéance, sans geste du
  pilote. Le versement a eu lieu. La mémoire mesurée est de 31,3 Gio.
- **Ce qui a échoué.** La course factice n'a pas eu lieu : « REFUS : registres/go.md illisible au commit 72160f1e… ».

La v10 a des noms neufs (R12) ; les v1 à v9 sont inchangées. Elle porte **seulement** les points (a) à (c) de la demande. Mêmes
interdits : aucun commit, aucun `.sha256`, aucune location, aucune clé lue, aucune dépense.

**Verdict.** Sur la machine, la v10 lit le registre de `canal/conv-audit-n04` au commit que pose le pilote, et non celui de `main`,
comme la vraie course. Elle ajoute deux relevés : la facturation, par le pilote, et le pilote de carte, sur la machine.
**150 essais de la sonde v10 passent.** Le résultat de l'ensemble est en section 3.

## 0. La cause, précisée

Le message « illisible au commit » ne vient pas du lecteur des doublons. Il vient de la v9, à ces lignes : `git show
<tête de main>:registres/go.md` y était lancé par `h.lancer`, **sans l'aide d'identification**, dans un clone partiel
(`--filter=blob:none`). Le contenu du fichier n'était pas encore là ; Git a voulu le chercher sur le dépôt privé sans le jeton
(`GIT_TERMINAL_PROMPT=0`), l'a manqué, et `git show` a rendu un code non nul.

Les doublons du registre de `main` (17 lignes d'extension, R-389) étaient un **second** obstacle : s'ils avaient été lus, la garde de
`main` les aurait admis, mais le lecteur gelé de la vraie course les refuse.

La v10 lève les deux : registre du canal (sans doublon), lu par `h.git show`, **avec** l'aide d'identification. C'est nécessaire pour
le point (a) ; je l'écris ici parce que c'est un changement de lecture, pas seulement de source.

## 1. Fichiers neufs (sha256 : section 4)

Copies renommées de la v9 (étiquette `sonde-a1-v3-v10`, branches `donnees/sonde-hote-durable-a1-v3-v10…`, dossier `/root/sonde-a1-v3-v10`,
fichiers `sonde-v10-*`), puis modifiées :
- `src/controle_ia/sonde_hote_durable_a1_v3_v10.py` ;
- `scripts/amorce_sonde_hote_durable_a1_v3_v10.sh` : `COMMIT_REGISTRE` est ajouté aux variables exigées ;
- `tests/test_sonde_hote_durable_a1_v3_v10.py` : 150 essais, soit les 136 de la v9 adaptés et 14 neufs.

## 2. Ce qui change, et rien d'autre (diff exact : section 5)

**(a) Deux vérifications, à deux endroits.**
- **Pilote**, comme en v9 : la garde de `main` sur le registre de `main`, à la location (`--registre-main`, `--garde-main`) ; type
  calcul, Lazar, validité, révocations, extensions admises (R-389), plafond d'exactement 1 USD.
- **Machine**, neuve. Le pilote pose `--commit-registre`, porté dans le corps de création par la variable `COMMIT_REGISTRE` (40
  caractères hexadécimaux, contrôlés). La machine, ensuite :
  1. récupère `canal/conv-audit-n04` (partiel, `PROFONDEUR_CANAL` = 200 commits) ;
  2. vérifie que ce commit est sur la branche (`merge-base --is-ancestor`) ;
  3. lit, à ce commit, `registres/go.md` et `.claude/hooks/garde_calcul.py`, par `h.git show` avec l'aide d'identification ;
  4. **refuse tout identifiant en double**, parce que le lecteur gelé de la vraie course le refuserait ;
  5. applique la garde de ce commit, avec le plafond exact de 1 USD.

  Le journal écrit le commit, « aucun doublon », le GO et l'empreinte. La copie `registre-go.md` est versée. Le registre de `main`
  n'est plus lu sur la machine.

**(b) Relevés.**
- **Facturation**, par le pilote. La nouvelle sous-commande est `facturation --etat … --journal-local …`, à lancer juste avant
  l'échéance.
  - Elle appelle `vastai show instance <ID> --raw` et ne garde que `actual_status`, `dph_total`, `disk_usage` et `storage_cost`
    (`CHAMPS_FACTURATION`), s'ils existent, avec l'identifiant et l'étiquette pour le contrôle. Le reste n'est jamais écrit
    (environnement de la machine, jeton, `onstart`, hôte).
  - Une étiquette autre ou une instance protégée ne donnent aucun relevé.
  - Codes : 0 relevé écrit ; 2 refus ; 6 délai dépassé ou échec de `vastai` (recontrôler).
- **Pilote de carte**, sur la machine. `relever_l_hote` y ajoute une ligne : la première ligne de `nvidia-smi -L` s'il existe, sinon
  « nvidia-smi absent ». Elle est écrite au journal et dans `pilote-carte.txt`, versé.

**(c) Essais.**
- Cas sain : le registre du canal, sans doublon, est lu sur la machine. La course factice part, la copie versée ne porte aucun
  doublon, et le journal le dit.
- Artefacts :
  - **le registre de `main`, à doublons d'extension**, passé comme `COMMIT_REGISTRE` : refus « identifiants en double » ;
  - un canal lui-même à doublons ;
  - `COMMIT_REGISTRE` absent ;
  - un canal sans GO-2026-11-05-01 ;
  - un commit hors de la branche du canal.

  Dans chaque cas : rien n'est lancé, et le refus est versé.
- Le corps et `louer` portent le commit du registre ; un hash mal formé est refusé et rien n'est créé.
- Pilote de carte : présent (une ligne seulement) et absent.
- Facturation :
  - cas sain : seuls les quatre champs sont écrits (aucun jeton, ni `extra_env`, ni `onstart`, ni `ssh_host`) ;
  - forme liste ;
  - étiquette autre (2), illisible (2), code 1 (6), délai (6), instance protégée (2).

## 3. Essais (`timeout 900 nice -n 10`, aucun réseau)

- `tests/test_sonde_hote_durable_a1_v3_v10.py` : **150 passés**.
- Ensemble (v10 à v1, lanceur durable, garde de calcul) : **1 001 passés**, aucun sauté, en 1 572 s
  (150 + 136 + 126 + 113 + 95 + 86 + 72 + 66 + 52 + 19 + 49 + 37) ; sortie `…/sorties/essais-sonde-v10.txt`
  (`3439c2668dff98d37b92e963a9e67b1ea419c0ccf023899a149a7e367da30664`).

## 4. Empreintes à la remise

Relevées le 5 novembre 2026 à 02:35 UTC.

| fichier | sha256 |
|---|---|
| `src/controle_ia/sonde_hote_durable_a1_v3_v10.py` (1 071 lignes) | `37b70a0646874e3769a9e45ccf1438121f2126aecc8307234c3cc590f122b81c` |
| `scripts/amorce_sonde_hote_durable_a1_v3_v10.sh` | `d4f5462cf16d7ce7d5c5da7ef16bb13e1f19a8737ff4fe76e6f55067974629c1` |
| `tests/test_sonde_hote_durable_a1_v3_v10.py` (150 essais) | `1821603ba75e89e73febdd26348929c8bfe825dd3f7542a7351f571dcc4c2a28` |
| bloc-notes `sorties/diff-sonde-v9-vers-v10-brut.txt` | `6a58f633fa999a8463c308f11bc21d80512193865062ea8848909cf1ca51f221` |
| bloc-notes `sorties/diff-sonde-v9-vers-v10-hors-renommage.txt` (424 lignes) | `c49bbd8c81469dd3e326530b3e613174980f3940479cb12cc6997639e09c3416` |
| bloc-notes `renommage-v9-v10.sed` | `3f159add1c3a8d10e772ffde69f575d8b1a36017f3d8cb95e4353cd6b90ed010` |

Ce fichier ne porte pas sa propre empreinte : elle est donnée avec la remise. Les instantanés versés pendant le travail sont
intermédiaires ; seules ces empreintes valent pour le rendu.

## 5. Diff exact par rapport à la v9

Les diffs sont dans le bloc-notes `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/v3b1/sorties/` :
- `diff-sonde-v9-vers-v10-brut.txt` : renommages compris ;
- `diff-sonde-v9-vers-v10-hors-renommage.txt` : la v9 renommée par `…/v3b1/renommage-v9-v10.sed`, comparée à la v10.

Le second ne contient que (a) à (c) :
- **Module :**
  - le paragraphe de tête ;
  - `PROFONDEUR_CANAL` et `CHAMPS_FACTURATION` ;
  - `corps(…, commit_registre="")`, qui ajoute `COMMIT_REGISTRE` ;
  - `ClientPilote.facturation` ;
  - deux appels de `corps` dans `louer`, avec le commit du registre ;
  - la fonction neuve `relever_facturation` ;
  - `MachineSondeV10.relever_l_hote` (pilote de carte) ;
  - dans `preparer_sonde`, le bloc du registre réécrit : canal, ancestralité, `h.git show`, doublons, garde du commit ;
  - les arguments `--commit-registre` et la sous-commande `facturation`.
- **Amorce :** une ligne, `COMMIT_REGISTRE` exigé.
- **Essais :**
  - `commit_registre` dans les aides ;
  - le monde jouet : `main` porte un doublon d'extension, et `canal/conv-audit-n04` un registre sans doublon ;
  - une attente adaptée (le registre du canal) ;
  - les 14 essais neufs.

## 6. Commande exacte pour la fille

**Préalables :**
- crédit de Vast ;
- `vastai --version` = `1.8.3` ;
- sonde v10 committée sur `main` du dépôt privé (`COMMIT_PRIVE`) ;
- GO-2026-11-05-01 valide jusqu'au 2026-11-06 ;
- ligne recopiée à l'octet sur `canal/conv-audit-n04`, commit `740f49e2b27344b3188f9aba20b5f0115c3468ab` (`COMMIT_REGISTRE`), sur lequel
  `doublons_lecteur_du_lanceur` rend [].

**Dépense :** environ 0,02 USD attendus ; borne de la minuterie 0,37 USD au pire prix admis ; plafond du GO : 1 USD.

```
COMMIT_PRIVE=<hash complet de 40 caractères donné par le directeur>
COMMIT_REGISTRE=740f49e2b27344b3188f9aba20b5f0115c3468ab
[ "$(vastai --version 2>/dev/null)" = "1.8.3" ] || { echo "vastai 1.8.3 exigé"; exit 2; }
D=/home/user/hors-clone-sonde-a1-v3-v10; mkdir "$D" || exit 2                     # neuf (R12)
cd /home/user/controle-ia-travail && git fetch -q origin main \
 && git show origin/main:registres/go.md > "$D/registre-go-main.md" \
 && git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py" \
 && for f in hote_durable_a1_v3.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v10.py; do
      git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f" || exit 2; done \
 && timeout 300 vastai search offers 'num_gpus=1 rentable=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=30 dph_total<=0.40' -o dph_total --storage 30 --raw > "$D/offres.json" \
 && OFFRE=$(python3 -I -B "$D/sonde_hote_durable_a1_v3_v10.py" offre --offres "$D/offres.json") \
 && for V in "--verifier-seulement" ""; do
      GO_ID=GO-2026-11-05-01 env -i GO_ID=GO-2026-11-05-01 PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 \
        HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-${SSL_CERT_FILE:-}}" \
        GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" timeout 900 nice -n 10 \
        python3 -I -B "$D/sonde_hote_durable_a1_v3_v10.py" louer --go GO-2026-11-05-01 \
          --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" --offres "$D/offres.json" \
          --offre "$OFFRE" --commit-prive "$COMMIT_PRIVE" --commit-registre "$COMMIT_REGISTRE" --duree-s 1200 --tir-minuterie \
          --journal-local "$D/journal-location-sonde-v10.log" $V || exit 2
    done
```

**Juste avant l'échéance** (T0 + 38 min en tir ; T0 et l'échéance sont dans l'état), le relevé de facturation :

```
D=/home/user/hors-clone-sonde-a1-v3-v10
env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-${SSL_CERT_FILE:-}}" \
  GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" \
  timeout 900 nice -n 10 python3 -I -B "$D/sonde_hote_durable_a1_v3_v10.py" facturation \
    --etat "$D/journal-location-sonde-v10.log.etat.json" --journal-local "$D/journal-controle-sonde-v10.log"
```

**Puis les contrôles** à T0 + 45 et T0 + 70 min : le même bloc avec `controler` à la place de `facturation`.

**La sonde est réussie si :**
- le journal versé (`donnees/sonde-hote-durable-a1-v3-v10`) porte, dans l'ordre :
  - « registre de canal/conv-audit-n04 au commit 740f49e2… : aucun doublon ; GO-2026-11-05-01 accepté » ;
  - « pilote de carte : … » ;
  - « course factice détachée » ;
  - « plafond_de_duree_de_la_sonde » ;
  - « versé » ;
  - « tir de la minuterie : aucun geste » ;
- le journal du pilote porte le relevé de facturation ;
- l'instance est absente de l'inventaire avant T0 + 70 min, avec un code 0 et sans geste du pilote.
