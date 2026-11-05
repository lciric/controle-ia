# Contre-lecture CL15 — orchestrateur du pôle, version 50 (corrections de CL14), jouée sous un vrai `bwrap`

- Date : 2026-10-30, 03:15 UTC.
- Contre-lecteur : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent **neuf** (règle R2) : n'a écrit aucune version de l'orchestrateur.
- Objet : `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/orchestrateur-pole-v7/` de la branche
  `origin/canal/conv-audit-n04` (tête `8dbfaed6` ; arbre de la v50 au commit `8226c33f`), extrait par `git archive` dans le
  bloc-notes de la session. Arbre de la v49 lu pour comparaison au commit `ecb1b408`. Rien d'autre lu sur `canal/*` ; aucune
  branche `donnees/*` ni `quarantaine/*`.
- Machine : `bwrap` 0.9.0 (non setuid), `setpriv` (util-linux), noyau Linux 6.18.44, Python 3.13.17, Ubuntu 24.04, sans module
  de sécurité actif ni Yama. Noyau du pôle lancé en **superutilisateur**, comme chez session-depot.
- **Utilisateur dédié** : identité numérique **64097**, la même que les essais de l'auteur (`UID_ESSAI`). **Aucun compte créé**
  (`setpriv` accepte un identifiant numérique, `getent passwd 64097` : vide) : rien n'a donc été ajouté à `/etc/passwd`. Dossier
  racine du bac : `/tmp/cl15-bac-oqWpAQKq/bac` (64097:64097, mode 0700, parent root 0711), créé pour les essais puis **retiré**.
- Aucun appel payant, aucune clé. Chaque essai a tourné sous `env -i` (clé factice `CLE_FACTICE_DU_NOYAU` seulement) et dans un
  espace réseau isolé (`bwrap --dev-bind / / --unshare-net`). Faux kit, faux adaptateurs. `/opt/argon/commande_argon_v2.py` a été
  lu, **pas exécuté**.
- Cibles : toutes factices, dans le bloc-notes (dont un fichier creux de 300 Mo dans un dossier réservé au superutilisateur).
  **Aucune écriture dans `/proc/sys`** ni dans un réglage global : seulement des ouvertures en écriture, sans écriture. Rien n'a
  été tenté dans `/usr` : la lecture seule est prouvée par `access(W_OK)` et par le refus du remontage. Une clé a été tentée dans
  le trousseau de l'utilisateur, avec invalidation prévue : l'appel n'a pas abouti (symbole absent).
- État de l'hôte après les essais : aucun processus de l'identité 64097 ; aucun fichier de cette identité ; aucun segment de
  mémoire partagée ; `core_pattern` = `core` et nom d'hôte `vm`, comme avant ; aucun `/tmp/cl15-*`, `/tmp/essai-bac-v50-*`
  ni `/tmp/etage-travail-*`.

## Empreintes vérifiées

| fichier | empreinte SHA-256 | vérification |
|---|---|---|
| `EMPREINTES-orchestrateur-pole-v7-v50.txt` | `3b1458f3e5f770ccef30f099f0668e9d1d3554cd6116249d17327502804995f1` | égale à l'attendue (`3b1458f3…`) et à son `.sha256` ; **178 lignes** |
| fichiers listés par la v50 | — | `sha256sum -c` : **178 OK, 0 échec** |
| `LISEZMOI-orchestrateur-pole-v7-v50.md` | `697dd6818e192f9238e5aa297ae97615659783c4a48257aaf3fc4276518709cf` | égale à l'attendue (`697dd681…`) et à son `.sha256` |
| liste v49 sur l'arbre v50 | — | 5 échecs, ceux qu'annonce le LISEZMOI (les cinq modules de la table de provenance) |
| `CODE-orchestrateur-pole-v7-v49.zip` | `2c464d6d27682d086d4dd0140fc93ae9f9a08cd57618c54d3963e04dda26f1b0` | égal à son `.sha256` ; 92 fichiers, **92/92 égaux** à la liste v49 |
| `/opt/argon/commande_argon_v2.py` (lu, non exécuté) | `6905ac71f126bfd49174ccb9e98e26e9c73367d3d9614bc2f5ada20b085df7e2` | identique à celui de CL14 |

Sondes et journaux de cette contre-lecture : bloc-notes de la session
(`/tmp/claude-0/-home-user/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/cl15/`), hors dépôt, non versés (R6) :

| fichier | SHA-256 |
|---|---|
| `sondes/sonde_bac50.py` (exécuteur `ExecuteurBacASable` de la v50, inchangé, vue de l'hôte pendant l'exécution) | `12221a6ff609cdd203ed2072a6b92a64d2aef931010b8026d35c5a4b01dcae86` |
| `sondes/p_attaque.py` (identité, `/usr`, `/proc`, setuid, espaces, ptrace, `/dev`, terminal, descripteurs, prises, mémoire partagée, limites) | `b69ce015086766e60c13e5f9ea1096a8f8678749aeba6383f7bbf2c9694cf1a9` |
| `sondes/p_tardif.py` (processus détaché qui écrit après la fin du script) | `49d362923ae7564655a351b6491b94a0dbb27d2628a22b91727cb9303d57d2d8` |
| `sondes/p_memoire.py` (mémoire partagée System V et `/dev`) | `1ab169a3129a15c7c3647428be18499babd94c33d64f3ce9c984ade164b61c5c` |
| `sondes/p_course_lien.py` (lien substitué pendant la surveillance) | `f1ae6690abbb3c72d50eeb922e27711d32dd12c73cceab2209428d3b2eaa3e85` |
| `sondes/p_dev.py` (essai de la correction de `/dev`) | `7a5b1878e8c5952d11ecf23c7195f79cc5978ec2a5c5d5003d654c123bcb3a7f` |
| `sondes/sonde_etage50.py` (étage entier, faux kit, vrai bac) | `65861e57e4b99b90860a6f1364c178b2287a74fe1cb1257e634fa886d921a384` |
| `sondes/mutations.py`, `mutation_root.py`, `mutation_root_temoin.py` | `13e05a36…f93`, `b68b9bdd…bb9`, `5ebc2bf6…596` |
| `journaux/essais50-avec-bac.log` (suite v50, bac réel joué) | `4b35b133d883e151083c9dc98b84626f0832118bf614ff5dc9e47ab6c7643318` |
| `journaux/essais50c-avec-bac.log` (suite de la variante corrigée de CL15-01) | `a039fd0ef7c99b6a19abedd0337926dfc393fe4756fe8724c47d770641b38f7e` |
| `journaux/attaque-v50.log`, `journaux/mutations.log` | `651c574b…5bc`, `1771d96c…d46` |
| `v50c/pole/tests_de_mort.py` (variante d'essai : correction de CL15-01 seule) | `2d7085366ff2258750350ef762ac3bcace57cad52a5da003ec2ed6aaad7c9579` |

## Verdicts

- **v50 sans l'étage (`--tests-de-mort 0`) : lançable en l'état.** Condition de lancement inchangée : étiquette d'Argon
  `gemini-4-argon`. Nouvelle réserve, sans blocage (CL15-05) : si le `modelVersion` réel n'est ni `gemini-4-argon` ni
  `gemini-4-argon-AAAAMMJJ`, la première session d'Argon est **refusée après l'appel payé**. La course s'arrête alors, sans repli.
- **Étage de tests de mort (`--tests-de-mort ≥ 1`) : non lançable en l'état ; lançable après corrections.** Aucune évasion
  n'a abouti. Sous l'utilisateur dédié, le bac **confine** : identité 64097 sur l'hôte, `/proc/sys` refusé, aucune capacité,
  espaces imbriqués refusés, borne de processus tenue, setuid consigné et refusé. Tous les artefacts de CL13 et de CL14 sont
  bloqués. Mais la sonde de la v50 **refuse l'étage dans toutes les configurations réelles** (CL15-01) : elle lit
  l'identité de l'hôte dans `uid_map`, qui ne montre que l'espace intermédiaire de `bwrap` (`65534 0 1`). Les quatre essais réels
  échouent ici. La correction proposée est éprouvée : témoin d'identité lu par le noyau sur l'hôte. Avec elle, les quatre
  essais passent et la mutation « `bwrap` lancé par le superutilisateur » est refusée. À traiter avant tout GO de l'étage :
  CL15-01 (bloquant), CL15-02 (mémoire de l'hôte non bornée), CL15-03 (le noyau suit un lien posé pendant la surveillance).

## Comptes d'essais

- **Suite complète de la v50 avec le bac réel** (`POLE_ESSAI_UTILISATEUR_BAC=64097`, `POLE_ESSAI_RACINE_TRAVAIL_BAC=<racine>`,
  `python3 -B -m unittest discover -t . -s essais -p 'test_*.py'`, `env -i`, réseau isolé) : **`Ran 502 tests in 283.356s —
  FAILED (failures=2, errors=2)`** : **498 OK, 2 échecs, 2 erreurs, 0 ignoré**. Les quatre essais réels sont joués et échouent :
  `test_v48_22` et `test_v50_15` échouent (`AssertionError … UID_HOTE=0, CL14-01 … étage refusé`) ; `test_v49_19` et `test_v50_16`
  sont en erreur (`CourseInterrompue : étage de tests de mort refusé avant tout appel : … UID_HOTE=0`). Les essais qui exigent un
  noyau superutilisateur et `setpriv` (`test_v50_04`, `_05`, `_08`) sont **joués ici et passent**.
- **Sans les deux variables** (même machine, `bwrap` présent, noyau superutilisateur) : les quatre essais réels sont
  **ignorés** (`OK (skipped=4)`, motif « noyau superutilisateur : donner POLE_ESSAI_UTILISATEUR_BAC … »). On retrouve exactement
  l'annonce de l'auteur, 498 OK et 4 ignorés, alors que l'étage est inutilisable (CL15-04).
- **Variante `v50c`**, seule correction de CL15-01 (témoin d'identité ; diff de 18 lignes dans `pole/tests_de_mort.py`) : les
  **quatre essais réels passent** (`Ran 4 tests in 12.402s — OK`). Suite complète : `Ran 502 tests in 295.249s — FAILED
  (failures=4)`, soit 498 OK et 4 échecs **attendus de la variante**. Il s'agit de `test_v49_02` et `test_v50_03` (fausse
  sortie `UID_HOTE=64321`), de `test_v50_04` (sonde jouée hors du bac) et de `test_v50_17` (provenance : le fichier a changé).
- **Ce que prouvent les quatre essais réels (critère 2), éprouvé par mutation sur `v50c`** :
  | garde retirée du code | résultat des quatre essais réels |
  |---|---|
  | `--ro-bind /proc/sys /proc/sys` (m1) | 2 échecs, 2 erreurs : « 17 réglages de /proc/sys s'ouvrent en écriture (CL14-01) : étage refusé » |
  | `--disable-userns` (m2) | 2 échecs, 2 erreurs : « le script crée un espace d'utilisateurs imbriqué (CL14-03) » |
  | refus des fichiers setuid dans l'inventaire (m3) | `test_v50_15` échoue : `'réussie' != 'échouée (fichier setuid ou setgid)'` |
  | `setpriv` (bwrap lancé par le superutilisateur, racine root, identité contrôlée contournée) | v50 : refus `UID_HOTE=0` ; `v50c` : refus « borne de processus (REUSSI-1056) » et, évaluation neutralisée, « identité de l'hôte du script 0:0 (propriétaire du témoin) ≠ 1000 » |
  | `processus_max=None` ; sans `--size --tmpfs /dev/shm` | refus « borne de processus ne tient pas (non-borne) » ; refus « /dev/shm n'est pas borné (REUSSI-40-Mo) » |
  | `--cap-drop ALL` | **non détecté** (`ok=True`) : sans effet ici, le script n'a déjà aucune capacité dans l'espace imbriqué (garde redondante) |

  Les essais réels prouvent donc le confinement **pour ce qu'ils jouent**, une fois CL15-01 corrigée. Dans la v50 livrée, ils ne
  prouvent rien : la sonde refuse avant tout. Ils ne jouent ni la mémoire (CL15-02) ni la course sur les liens (CL15-03).
  L'assertion d'identité de `test_v50_15` est sans effet (CL15-04).

## Critère 1 — artefacts de CL13, de CL14 et nouveaux, rejoués sous le vrai `bwrap`

Commandes : exécuteur seul (`ExecuteurBacASable` de la v50 inchangé, `utilisateur_bac=64097`) :
`env -i PATH=/usr/bin:/bin HOME=<bloc-notes> LANG=C.UTF-8 bwrap --dev-bind / / --unshare-net -- python3 -I -B sonde_bac50.py
<arbre v50> <racine> <script>`. Commande lancée : `/usr/bin/setpriv --reuid 64097 --regid 64097 --clear-groups --no-new-privs --
/usr/bin/bwrap …`. Étage entier : `cd <arbre v50c> && env -i … CLE_FACTICE_DU_NOYAU=sk-ant-api03-FACTICE-CL15-… POLE_ESSAI_…
bwrap --dev-bind / / --unshare-net -- python3 -B sonde_etage50.py`. L'étage de la v50 livrée est refusé par la sonde (CL15-01) :
les artefacts d'étage sont donc joués sur `v50c`, identique à la v50 hors de la sonde d'identité.

| artefact | sortie | bloqué ? |
|---|---|---|
| identité dans le bac | `Uid 65534`, `CapEff/CapPrm/CapBnd/CapAmb = 0`, `NoNewPrivs 1`, `Seccomp 0`, `setgroups deny` ; **`uid_map 65534 0 1`** | — |
| identité **vue de l'hôte** pendant l'exécution | chaque processus du bac : `Uid 64097 64097 64097 64097` ; `uid_map` lu par l'hôte : `65534 64097 1` (le `bwrap` intermédiaire : `0 0 4294967295` dans son propre espace) | **oui** (CL14-01 et 02 fermés en fait) ; la sonde lit mal (CL15-01) |
| CL13-01 `/usr`, `/`, tranche | `access(W_OK) /usr/lib : False` ; remonter `/usr`, `/`, la tranche en écriture : `errno 1` ; démonter `/proc/sys`, la tranche : `errno 1` ; écrire la tranche : `errno 30` | **oui** |
| liens durs, `mknod` | lien dur vers la tranche et vers `python3.13` : `errno 18` (autre périphérique) ; `mknod` : `errno 1` | oui |
| CL14-01 `/proc/sys` (ouverture sans écriture) | `core_pattern`, `hostname`, `drop_caches` : `errno 13` ; `ns_last_pid` : `errno 30` ; `kernel/modprobe` : `errno 2` ; `PROCSYS-OUVRABLES=0` ; `sethostname` : `errno 1` ; montage `/proc/sys ro` | **oui** |
| tout `/proc` hors processus | ouvrables en écriture : `/proc/pressure/io`, `cpu`, `memory` seulement (déclencheurs de pression, sans effet global) ; `/proc/sysrq-trigger` absent ; `/proc/kmsg` `errno 13` | oui |
| CL14-02 setuid | `chmod 4755` : réussi ; **hôte : propriétaire 64097**, mode `0o104755` (setuid vers l'utilisateur dédié, plus vers le superutilisateur) ; inventaire : `interdits ['suid']`, `non_copies {'suid': 'fichier setuid ou setgid (refusé)'}` ; étage : « échouée (fichier setuid ou setgid) », verdict « non concluant », aucun mode setuid sous `SORTIE` ; `chown 0` : `errno 22` | **oui** |
| CL14-02 borne de processus | sonde : `PROCESSUS=refus-apres-1021-errno-11` ; essai `bombe-1100` de `test_v50_15` : refus | **oui** |
| CL14-03 espaces imbriqués | `unshare` user : `errno 28` ; mnt, net, pid, uts : `errno 1` | **oui** |
| CL13-02 lien sur `script.py` (étage, deux exécutions) | fichier factice de l'hôte après l'étage : `"CONTENU ORIGINAL DE L'HOTE"` ; exécution 1 : `script.py` consigné « lien » vers le fichier factice ; exécution 2 : `ECRIT PAR LE SCRIPT 2 : print('ECRIT PAR LE SCRIPT 2 :` (le noyau a écrit un script neuf, sans suivre le lien) | **oui** |
| CL13-03 liens dans les produits | non copiés : `environ.txt → /proc/self/environ`, `environ1.txt → /proc/1/environ`, `secret.txt → <secret factice>` ; canari de la clé factice dans `SORTIE` : `None` ; secret factice dans `SORTIE` : `False` ; produits copiés : `dur.txt.copie`, `r.txt.copie`, `r.txt.sha256.copie` | **oui** |
| CL13-04 tube nommé, prise | `tuyau` : « tube nommé », `prise` : « prise », consignés ; étage complet en **1,5 s** ; liens, tubes, prises sous `SORTIE` : `[]` | **oui** |
| CL14-04, 05 dossier de travail, `.sha256` | `travail_retire: True` (×2) ; racine du bac après l'étage : `[]` ; `r.txt` et `r.txt.sha256` copiés sous `.copie`, l'étage continue | **oui** |
| survie après la fin du script (`setsid` + double `fork`, écritures toutes les 1 ms) | entrées au retour de `executer()` : 6 ; une seconde plus tard : 6 (×3) ; seul reste un `[bwrap] <defunct>` passager, récolté ensuite | **oui** |
| `/proc/<pid>` de l'hôte | pids visibles : `[1, 2]` ; `/proc/1` = `bwrap` du bac ; `/proc/1/root` = racine du bac ; `/proc/1/fd` : `/dev/null`, deux fichiers de capture supprimés, un `eventfd` | oui (fuite : `/proc/1/environ` porte `HOME=<chemin de l'hôte du dossier de travail>`, `mountinfo` aussi : CL15-06) |
| `ptrace` | `PTRACE_ATTACH` sur le processus 1 (`bwrap` du bac) : **réussi** ; sur un enfant : réussi ; le processus 1 n'a aucune capacité, même espace ; un processus 1 arrêté par `ptrace` fige le bac jusqu'au délai (tué à 20 s, `code -9`) | oui (CL15-06) |
| `/dev`, terminal (`TIOCSTI`) | `/dev` : `core fd full null ptmx pts random shm stderr stdin stdout tty urandom zero` ; `TIOCSTI` sur 0, 1, 2 : `errno 25` ; `/dev/tty` : `errno 6` ; `/dev/console` absent ; `ptmx` : un pseudo-terminal **à lui** | oui |
| descripteurs hérités | `0 → /dev/null`, `1`, `2 →` fichiers de capture du noyau supprimés ; rien d'autre | oui |
| prises abstraites, réseau | `/proc/net/unix` : 0 ligne ; connexion abstraite `\0/tmp/.X11-unix/X0` : refusée ; liaison abstraite : dans l'espace réseau du bac seulement ; `1.1.1.1:443` : `errno 101` ; pas de `/sys` | oui |
| CL14-10 `/dev/shm` | 64 Mo : `errno 28` après 32 Mo | **oui** |
| `/dev` lui-même (système de fichiers en mémoire) | 5 × 45 Mo écrits dans `/dev` : **225 Mo**, hors de toute borne ; un seul fichier de 64 Mo : `errno 27` (`RLIMIT_FSIZE`) | **NON** — CL15-02 |
| mémoire partagée System V | 8 segments de 256 Mo remplis puis détachés par **un** processus (`RLIMIT_AS` = 1 Go) : `Shmem` de l'hôte de 15 836 à **2 343 288 ko** pendant l'exécution, rendu à la fin | **NON** — CL15-02 |
| lien substitué pendant la surveillance | 300 Mo creux dans un dossier de l'hôte **inaccessible au script** : bac tué « plus de 268435456 octets » (3 sur 3) ; cible vide : non tué | **NON** — CL15-03 |
| limites | `RLIMIT_AS 1 Go`, `NPROC 1024`, `NOFILE 512`, `CPU 25 s`, `FSIZE 50 Mo`, `CORE 0` ; hausse de `NPROC` refusée | oui |
| surface du noyau Linux | `unprivileged_bpf_disabled 2`, `perf_event_paranoid 2`, **`io_uring_disabled 0`**, aucun filtre d'appels système | réserve (CL15-06) |

## Constats

### CL15-01 — La sonde lit l'identité de l'hôte dans `uid_map`, qui ne la montre pas : l'étage est refusé dans toutes les configurations réelles

- **Gravité : haute** (bloque l'étage ; aucun risque : le défaut ferme). Les quatre essais réels échouent.
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 1240-1253 (`hote()` et les lignes `UID_HOTE`, `GID_HOTE` de `_SONDE_MODELE`),
  l. 1358-1366 (`evaluer_sonde_privileges`) ; `essais/test_v7_ideation.py` l. 6801 (fausse sortie saine `UID_HOTE=64321`),
  l. 8168-8196 (`test_v50_04` : sonde jouée **hors** du bac, où `uid_map` vaut `0 0 4294967295`).
- **Défaut** : `bwrap` 0.9.0 crée **deux** espaces d'utilisateurs dès que `--dev` (montage de `devpts`), `--uid` différent ou
  `--disable-userns` sont donnés. Le premier associe 0 à l'appelant ; le second, celui du script, associe 65534 à ce 0. Dans le
  bac, `/proc/self/uid_map` décrit l'espace **parent** du script, c'est-à-dire l'espace intermédiaire, pas l'hôte. Il vaut donc
  toujours `65534 0 1`, que `bwrap` soit lancé par le superutilisateur (v49) ou par l'utilisateur dédié (v50). La sonde lit
  `UID_HOTE=0` et refuse l'exécuteur. C'est vrai sous un noyau superutilisateur avec `setpriv`, et aussi sous un noyau non
  superutilisateur. Le contrôle ne distingue rien. Il n'a jamais été vu, parce que les essais de l'auteur lisent une sortie
  inventée (`UID_HOTE=64321`) ou jouent la sonde hors du bac.
- **Essai** :
  ```
  (bac de la v50, sous setpriv 64097) uid_map: 65534 0 1 ; Uid: 65534 … ; CapEff 0
  (vue de l'hôte, même exécution) 10811 {"uid_hote": ["64097","64097","64097","64097"], "cmd": "/usr/bin/python3 -I -B /travail/script.py", "uid_map_vu_de_l_hote": ["65534","64097","1"]}
  (sonde v50) UID=65534 CapEff=0 … UID_HOTE=0 GID_HOTE=0 … PROCSYS-OUVRABLES=0 USERNS-IMBRIQUE=refus SHM=refus-apres-32-Mo-errno-28 PROCESSUS=refus-apres-1021-errno-11
  disponible() : False « sonde du bac à sable : le script a l'identité 0 de l'hôte (UID_HOTE=0, CL14-01) … étage refusé »
  (noyau NON superutilisateur, uid 64097, sans setpriv) : même refus, UID_HOTE=0
  suite : Ran 502 tests — FAILED (failures=2, errors=2) ; test_v48_22, _v49_19, _v50_15, _v50_16
  ```
- **Correction** (essayée ici, variante `v50c`) : l'identité de l'hôte se lit **depuis l'hôte**. La sonde crée un fichier
  témoin `/travail/temoin-identite`. Après l'exécution, le noyau vérifie par `lstat` que son propriétaire est l'utilisateur
  dédié (ou l'identité du noyau non superutilisateur), jamais 0, et que c'est un fichier régulier. Les lignes `UID_HOTE` et
  `GID_HOTE` ne se lisent plus dans `uid_map`. Résultats : les quatre essais réels passent ; `disponible()` → `True` sous
  `setpriv` et sous un noyau non superutilisateur. Mutation « `bwrap` lancé par le superutilisateur », évaluation de la sonde
  neutralisée : `identité de l'hôte du script 0:0 (propriétaire du témoin, CL15) ≠ utilisateur dédié 1000 : étage refusé`.
  Autre voie possible : `--info-fd` (identifiant hôte du processus 1 du bac), puis lecture de `/proc/<pid>/status` par le
  noyau. Corriger aussi les fausses sorties des essais (`SORTIE_PRIVILEGES_SAINE`) et `test_v50_04`.

### CL15-02 — Mémoire de l'hôte non bornée : mémoire partagée System V et `/dev` contournent `RLIMIT_AS` et la borne de `/dev/shm`

- **Gravité : moyenne** (déni de service de l'hôte pendant le délai, jusqu'à 120 s par exécution. Le tueur de processus du
  noyau Linux, faute de mémoire, peut frapper le noyau du pôle, le relais ou une autre session. Aucune donnée ne sort.)
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 1051-1052 (`--dev /dev` : système de fichiers en mémoire sans taille, ni
  lecture seule, ni surveillance) ; l. 1066-1076 (`_limites` : `RLIMIT_AS` par processus seulement) ; l. 1117 et 1127
  (`mesure_rapide_travail` ne regarde que le dossier de travail).
- **Défaut** : `memoire_mo` (1 Go) borne chaque processus, pas le bac. Deux voies le montrent. Un segment de mémoire partagée
  System V (`shmmax` de l'espace IPC du bac : 18 446 744 073 692 774 399) survit au détachement jusqu'à la fin du bac. Un seul
  processus remplit donc des segments les uns après les autres. `/dev` est un système de fichiers en mémoire inscriptible, limité
  seulement par fichier (`RLIMIT_FSIZE` 50 Mo). La borne de 32 Mo de `/dev/shm` (CL14-10) est contournée dans le dossier voisin.
  Avec 1 024 processus, le plafond théorique dépasse de loin la mémoire de l'hôte (16 Go ici).
- **Essai** (`p_memoire.py`, bac v50) :
  ```
  RLIMIT_AS (1073741824, 1073741824) Shmem hote avant (ko) 15836
  segments SysV de 256 Mo remplis et détachés: 8 Shmem hote apres (ko) 2112988
  Mo écrits dans /dev (tmpfs, hors /dev/shm, hors dossier de travail): 225 Shmem hote 2343288
  code: 0 delai_depasse: False limites: []        (après le bac : Shmem 15836 kB)
  ```
- **Correction** : (a) `--remount-ro /dev` juste après `--size … --tmpfs /dev/shm`. Essayé (`p_dev.py`) : `ecrire /dev/null 1`,
  `ecrire /dev/cl15 refus errno 30`, `ecrire /dev/shm/a 1`, lecture de `/dev/urandom` intacte. (b) Une borne mémoire **du bac
  entier**, par groupe de contrôle. Le contrôleur `memory` (v1) est présent ici : `memory.limit_in_bytes`, ou `memory.max` en
  v2. Le noyau superutilisateur y place le processus `bwrap` avant l'exécution, et `pids` peut doubler `RLIMIT_NPROC`. (c) À
  défaut, un filtre d'appels système (`bwrap --seccomp`) qui refuse `shmget`, `shmat`, `msgget`, `semget` et `io_uring_setup`.
  Ajouter à la sonde deux artefacts : 64 Mo écrits dans `/dev` doivent échouer, et un segment System V de 64 Mo doit échouer ou
  tenir dans la borne.

### CL15-03 — Pendant l'exécution, le noyau (superutilisateur) suit un lien substitué à un dossier : oracle sur des chemins de l'hôte

- **Gravité : moyenne** (même classe que CL13-02 et 03 : « le noyau ne suit jamais un lien posé par le script ». Ici, ni
  lecture de contenu ni écriture : un oracle et un déni de service borné.)
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 734-740 (`inventaire_travail` : `chemin_dossier = os.path.join(travail,
  relatif_dossier)` puis `os.scandir(chemin_dossier)`, qui **suit** tout lien des composants) ; appelé toutes les 0,25 s par
  `mesure_rapide_travail` (l. 840-843, 1117) pendant que le script vit.
- **Défaut** : le dossier `zz` est vu comme vrai dossier par `lstat` et mis en pile. Le script le remplace par un lien avant que
  le noyau ne l'ouvre. Le noyau parcourt alors, en superutilisateur, un dossier **de l'hôte** que le script ne peut pas lire. Il
  en compte les entrées et les tailles, puis tue le bac si la borne est franchie. Le motif (« plus de 268435456 octets »,
  « plus de 2000 entrées », ou « entrée illisible (…) » avec le nom relatif) revient à l'expérimentateur dans
  `limites_depassees`. On obtient un oracle d'existence et de taille sur les chemins réservés au superutilisateur, à raison
  d'environ un bit par exécution. Il permet aussi de faire parcourir `/` au noyau, borné à 2 000 entrées. L'inventaire final,
  script mort, n'est pas touché : les fichiers sont ouverts par `openat` sans suivre de lien (vérifié ; plus aucun processus du
  bac après le retour d'`executer()`, essai `p_tardif.py`).
- **Essai** (`p_course_lien.py` : 1 500 fichiers vides pour élargir la fenêtre, puis bascule de `zz` toutes les 0,5 ms ; cible
  `<bloc-notes>/hote-factice` = un fichier creux de 300 Mo, dossier réservé au superutilisateur) :
  ```
  v50c, cible 300 Mo : code: -9 limites: ['plus de 268435456 octets dans le dossier de travail'] duree: 0.264   (3 essais sur 3)
  v50 livrée, même cible : code: -9 limites: ['plus de 268435456 octets dans le dossier de travail'] duree: 2.599
  témoin, cible vide : code: 0 limites: [] duree: 6.381 ; bascules 3493
  ```
- **Correction** : parcourir par descripteurs. Chaque sous-dossier est ouvert par `os.open(nom, O_RDONLY|O_DIRECTORY|O_NOFOLLOW,
  dir_fd=parent)`, puis `os.scandir(fd)`. On compare `st_dev` et `st_ino` à ceux de l'entrée vue par `lstat`. Une différence
  vaut dépassement « dossier remplacé pendant le parcours ». Même règle pour l'inventaire final. Ajouter l'artefact aux essais
  réels.

### CL15-04 — Essais réels : ignorés en silence sous un noyau superutilisateur ; assertion d'identité sans effet

- **Gravité : mineure** (R5 : c'est ce qui a laissé passer CL15-01).
- **Fichier et ligne** : `essais/test_v7_ideation.py` l. 7916-7926 (`executeur_reel` : `skipTest` si les deux variables
  manquent, même quand `bwrap` est présent) ; l. 8759 (`assertNotIn("'0', '0', '1'", sortie)`).
- **Défaut** : dans le conteneur cible (superutilisateur, `bwrap` présent), un lancement ordinaire de la suite donne « 498 OK,
  4 ignorés ». C'est vert, alors que l'étage est refusé partout. L'assertion de `test_v50_15` cherche `'0', '0', '1'`, mais le
  bac imprime toujours `['65534', '0', '1']`, y compris quand le script a l'identité 0 de l'hôte (cas de CL14). Elle ne peut
  donc jamais échouer.
- **Essai** : `OK (skipped=4)` sans les variables ; `uid_map ['65534', '0', '1']` dans le bac de la v49 comme dans celui de la v50.
- **Correction** : `bwrap` présent, noyau superutilisateur et variables absentes doivent donner un **échec** (ou un mode
  explicite « essais réels non joués », dit au LISEZMOI). Remplacer l'assertion par le propriétaire, vu de l'hôte, d'un fichier
  créé par le script (`os.lstat(...).st_uid == utilisateur dédié`).

### CL15-05 — Argon : contrôle strict du modèle servi contre un format de `modelVersion` inconnu ; refus après l'appel payé

- **Gravité : mineure** (ferme sans repli ; coût d'un appel).
- **Fichier et ligne** : `pole/adaptateurs.py` l. 362-376 (`SUFFIXE_DE_DATE`, `modele_conforme`) ; `/opt/argon/commande_argon_v2.py`
  l. 226-228 (la commande admet tout suffixe et `models/`) ; `demonstrations/ideation_v1.py` l. 731-756.
- **Essai** :
  ```
  'gemini-4-argon' -> True ; 'gemini-4-argon-20261015' -> True ; 'gemini-4-argon-001' -> False (True avec la liste explicite) ;
  'gemini-4-argon-preview-10-15' -> False ; 'models/gemini-4-argon' -> False ; 'gemini-4-argon-lite' -> False ;
  'claude-opus-5-5-mini' -> False
  ```
  Le modèle servi n'est connu qu'**après** l'appel. Si Argon rend un suffixe de version (`-001`, `-preview-…`), la commande
  l'accepte, le noyau le refuse et la course s'arrête après une session payée. C'est R-764, conforme. Autre point :
  `--modele-commande-externe` est déclaratif. La commande v2 demande toujours `gemini-4-argon` (`appel-argon-v3.sh` ne passe pas
  `--modele`), donc toute autre étiquette déclarée passe le lanceur et échoue au premier appel.
- **Correction** : dire au LISEZMOI que le premier appel réel d'Argon fixe `--modele-servi-externe-permis` avec Lazar, au coût
  d'une session. Refuser `--modele-commande-externe` tant que la commande ne lit pas `--modele` ou `MODELE_DEMANDE_POLE` (v3 de la
  commande, R12).

### CL15-06 — Surface restante dans le bac : `ptrace` du processus 1, `io_uring`, chemin de l'hôte

- **Gravité : mineure** (aucune évasion constatée).
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 1043-1055 (pas de `--seccomp`) ; l. 1097-1098 (`env` passé à `setpriv` :
  `HOME` = chemin de l'hôte du dossier de travail).
- **Essai** : `F ptrace pid1: REUSSI` (processus 1 = `bwrap`, capacités nulles, même espace : rien à gagner) ; un processus 1
  arrêté fige le bac jusqu'au délai (`code -9`, `delai_depasse True` à 20 s) ; `--die-with-parent` emporte tout. `io_uring_disabled
  0`. `/proc/1/environ : … HOME=/tmp/cl15-bac-oqWpAQKq/bac/etage-travail-5zereydx/travail` ; `mountinfo` : même chemin.
- **Correction** : filtre d'appels système (`ptrace`, `io_uring_*`, `bpf`, `perf_event_open`, `keyctl`, `add_key`, appels
  System V : voir CL15-02) ; `HOME=/` dans l'environnement passé à `setpriv`.

### CL15-07 — L'utilisateur dédié n'est pas vérifié seul : un processus de l'hôte sous la même identité tient le bac (lu, non joué)

- **Gravité : mineure** (prérequis de l'opérateur, dit au LISEZMOI mais non contrôlé).
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 977-1004 (`verifier_identite` : propriétaire et droits du dossier racine,
  rien sur les processus).
- **Défaut** : l'espace d'utilisateurs du bac appartient à l'identité dédiée de l'hôte. Tout processus de l'hôte sous cette
  identité a donc **toutes les capacités sur le bac** : `ptrace` du script, modification de la tranche ou de `script.py`
  (fichiers 0600 à elle, dans un dossier racine à elle) entre l'écriture par le noyau et l'exécution. `RLIMIT_NPROC` compte aussi
  ces processus. Si l'opérateur réutilise un compte existant (`nobody`, `argon`), ce compte peut fausser l'étage.
- **Correction** : refuser l'étage si un processus de l'identité dédiée existe au départ et avant chaque exécution (balayage de
  `/proc/*/status`). Verrou d'un seul bac à la fois par identité. Refuser les identités qui ont un compte avec un interpréteur
  de commandes.

## Critère 3 — CL14-02 à 12

| constat | traité ? | preuve |
|---|---|---|
| CL14-01 | **en fait oui** (identité 64097 sur l'hôte, `/proc/sys` en lecture seule, `core_pattern` `errno 13`) ; **sa vérification est fausse** | CL15-01 |
| CL14-02 | oui : setuid vers 64097 seulement, refusé et consigné ; borne de processus tenue (refus après 1 021) | sondes, `test_v50_15` (v50c), mutation m3 |
| CL14-03 | oui : `unshare` user `errno 28` | mutation m2 détectée |
| CL14-04 | oui : dossier de travail hors de `SORTIE`, retiré, racine vide après l'étage | `sonde_etage50.py` |
| CL14-05 | oui : `.copie`, l'étage continue | `sonde_etage50.py`, `test_v50_15` |
| CL14-06 | oui (lu, l. 463-503 ; `test_v50_11` OK) : verdict pris aussi sur la valeur du noyau, « non concluant » si l'arrondi fait franchir le seuil | suite |
| CL14-07 | oui au lanceur (`test_v50_14` OK, l. 731-756) ; reste CL15-05 | — |
| CL14-08 | oui, suffixe strict | essai ci-dessus |
| CL14-09 | oui (diff lu, `test_v50_13` OK) | — |
| CL14-10 | oui pour `/dev/shm` (`errno 28` après 32 Mo) ; **contourné par `/dev`** | CL15-02 |
| CL14-11 | en partie : artefacts présents, mais identité mal lue (CL15-01), essais ignorés en silence et assertion sans effet (CL15-04), ni `/dev` ni System V | — |
| CL14-12 | oui (`test_v50_08` joué ici sous superutilisateur et `setpriv`, OK) | suite |

## Critère 4 — sans `--tests-de-mort` : rétrocompatibilité, Argon

- **Rétrocompatibilité** : `test_v48_11` OK (suite) ; les empreintes gelées `SORTIES_V47_SHA256`, `CONSIGNES_V47_SHA256`,
  `REGLAGES_KIT_V47_SHA256` sont **identiques** entre les arbres v49 (`ecb1b408`) et v50 (`8226c33f`), donc non ajustées. Hors de
  l'étage, `pole/ideation.py` ne change que d'une ligne (liste explicite passée à `controle_modele_resultat`). Le changement de
  `modele_conforme` touche **aussi la course sans étage** : un `-mini` ou `-lite` servi, autrefois admis, est maintenant refusé.
  C'est voulu (CL14-08) et plus sûr. Aucune garde de dépense modifiée.
- **R12** : 5 modules écrasés en place, dits, avec la table de provenance. Le lot `CODE-…-v49.zip` est vérifié (92/92).
- **Argon `gemini-4-argon`** : proposeur et juge acceptés au lanceur avec cette étiquette exacte ; toute autre étiquette est
  refusée avant tout appel ; l'expérimentateur externe est refusé (non fonctionnel avec la commande réelle). Réserve CL15-05.

## Récapitulatif par gravité

| gravité | constats |
|---|---|
| haute | CL15-01 (sonde : identité lue dans `uid_map`, étage refusé partout ; ferme sans risque) |
| moyenne | CL15-02 (mémoire de l'hôte non bornée : System V, `/dev`), CL15-03 (lien substitué suivi par le noyau pendant la surveillance) |
| mineure | CL15-04, CL15-05, CL15-06, CL15-07 |

Ordre conseillé : CL15-01 (témoin d'identité lu par le noyau), CL15-02 (`--remount-ro /dev` et borne mémoire du bac),
CL15-03 (parcours par descripteurs), CL15-04 ; puis rejouer `sonde_bac50.py`, `p_attaque.py`, `p_memoire.py`,
`p_course_lien.py` et `sonde_etage50.py` **dans le conteneur de session-depot**, avec l'utilisateur dédié réel, avant tout GO de
l'étage.
