# Orchestrateur du pôle, v7 — version 51 : corrections de la contre-lecture CL15 (bac à sable `bwrap` éprouvé pour de vrai)

Lignée conv-audit (sous-agent ingénieur), 30 octobre 2026. Source : `entrees-cl15/contre-lecture-cl15-orchestrateur-v50-v1.md`
(sous-agent neuf, R2 ; 7 constats : CL15-01 haute, CL15-02 et 03 moyennes, CL15-04 à 07 mineures). Les sept sont traités
ci-dessous. **v51 n'est pas contre-lue** (R2 : à faire par un sous-agent neuf).

**R12, appliquée strictement cette fois.** Aucun module n'est modifié en place : la v50 reste **octet pour octet** dans l'arbre
(chaque fichier de `EMPREINTES-orchestrateur-pole-v7-v50.txt` présent sur le disque a son empreinte v50) et dans
`CODE-orchestrateur-pole-v7-v50.zip` (`5bb498dd…`, 116 fichiers). Les corrections vivent dans des **versions nommées** à côté
des versions 1, et les lanceurs, le cœur et les essais de la v51 les prennent :

| fichier nouveau (v51) | version 1 (v50, gardée) | empreinte SHA-256 |
|---|---|---|
| `pole/tests_de_mort_v2.py` | `pole/tests_de_mort.py` | `363a3725885da08412f25b28defba7a8d204d883c3637f1de1df83686d93a41a` |
| `pole/ideation_v2.py` | `pole/ideation.py` | `67d2ad3591b21601ece4101154138f532ba519024761beb8c9738181f8f3fefc` |
| `demonstrations/ideation_v2.py` | `demonstrations/ideation_v1.py` | `bc5e9c98acff41b97487e2345d33768c8cdf41f0ededf8b2eed0bf842c889845` |
| `essais/test_v7_ideation_v2.py` | `essais/test_v7_ideation.py` | `35f99fa8d99dbf536e1ed7b824145fd8f92ca4a5ed72e750eb1a43cd6de83b7f` |
| `essais/test_v51_bac_reel.py` | `—` | `4e4a4b6060c4cf12b7e7d4ba63279355d90f32f3fe35fc7dcba1b9e8dfdc3a58` |

Un seul fichier de la v50 **quitte l'arbre actif** : `essais/test_v7_ideation.py`. Il essaie les modules v1, dont la sonde est
fausse (CL15-01) ; joué avec le vrai `bwrap`, il échouerait (4 essais réels) ou serait ignoré (CL15-04). Il est remplacé par
`essais/test_v7_ideation_v2.py` (ses 502 essais rejoués sur les versions 2, chaque adaptation marquée « v51 ») et reste,
inchangé, dans `CODE-orchestrateur-pole-v7-v50.zip` (empreinte vérifiée par `test_v51_15`). `pole/tests_de_mort.py`,
`pole/ideation.py` et `demonstrations/ideation_v1.py` restent dans l'arbre, inchangés : le lanceur v1 marche comme en v50 (son
étage est refusé partout, CL15-01, sans risque) ; `pole/moisson.py` et `pole/dossier_ferme.py` importent encore, tardivement,
des constantes et fonctions pures de `pole/ideation.py` (identiques en v2). **Pour l'étage, utiliser le lanceur v2** :
`python -I -B demonstrations/ideation_v2.py …` (mêmes options que la v1, plus celles ci-dessous).

**Attendu, dit :** `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v50.txt` sur l'arbre v51 donne **un seul échec** :
`essais/test_v7_ideation.py`, retiré de l'arbre actif (dans l'archive de la v50) ; tous les autres fichiers de la v50 sont OK.
`EMPREINTES-orchestrateur-pole-v7-v51.txt` se vérifie en entier. `CODE-orchestrateur-pole-v7-v51.zip` : 120 fichiers de code
(116 de la v50, moins `essais/test_v7_ideation.py`, plus les cinq fichiers nouveaux du tableau).

**Aucun appel payant, aucune clé, aucun réseau, aucune écriture dans `/proc/sys` ni dans un réglage global de l'hôte.** Les
groupes de contrôle de la v51 sont des **enfants de celui du processus noyau** (ici `memory:/process_api/…/claude-code-bash`),
créés par exécution, vidés et retirés ; aucun n'est resté (vérifié par `test_v51_15` et après chaque suite). Rien n'est resté
sur l'hôte : aucun processus de l'identité 64097, aucun fichier à elle, aucun objet System V, aucun `/tmp/essai-bac-v51-*`,
`/tmp/essai-v51-*` ni `etage-travail-*`.

## Machine des essais réels

`bwrap` 0.9.0 (non setuid), `setpriv` et `unshare` (util-linux), noyau Linux 6.18.44, x86_64, Python 3.13.17, cgroup v1 (`memory`
monté, `memory.oom_control` avec `oom_kill`), noyau du pôle en **superutilisateur**, utilisateur dédié **64097** sans compte
(`getent passwd 64097` : vide ; rien ajouté à `/etc/passwd`). Dossier racine du bac créé par les essais eux-mêmes
(`racine_bac_essai` : `/tmp/essai-bac-v51-*`, 0711 au superutilisateur, `bac` 0700 à 64097), retiré à la fin de chaque essai.

## Constat → correction → essai réel (artefact contre une cible factice, et cas sain)

| constat | correction | essais |
|---|---|---|
| **CL15-01** (haute) : la sonde lit l'identité de l'hôte dans `uid_map`, qui montre l'espace intermédiaire de `bwrap` (`65534 0 1`) : étage refusé partout | Correction de CL15 appliquée : la sonde crée un **témoin** `/travail/temoin-identite` ; après l'exécution, le noyau le lit **sur l'hôte** (`verifier_temoin_identite` : `lstat`, fichier régulier, un seul nom, propriétaire et groupe = utilisateur dédié — ou identité du noyau non superutilisateur —, jamais 0). Les lignes `UID_HOTE`/`GID_HOTE` et la lecture de `uid_map` sont **retirées** de la sonde ; `evaluer_sonde_privileges` garde le paramètre `uid_hote_attendu` pour la signature, sans effet (dit). `controler_hote_apres_sonde` (nouvelle méthode) porte ce que le noyau constate sur l'hôte. Fausses sorties des essais (`SORTIE_PRIVILEGES_SAINE`) et `test_v50_04` corrigés | réel : `test_v51_01` (sain : `disponible()` vrai ; `uid_map` vaut `['65534', '0', '1']` dans le bac, témoin à 64097:64097 sur l'hôte) ; `test_v51_02` (artefact = la mutation de CL15 : `bwrap` lancé par le superutilisateur, racine du superutilisateur → refus ; évaluation de la sortie neutralisée → refus « identité 0 de l'hôte (propriétaire du témoin 0:0) » ; contraste : la version 1, sur le même bac **sain**, refuse `UID_HOTE=0`, la version 2 l'accepte) ; `test_v51_03` (lecture du témoin : absent, lien, deux noms, dossier, 0 en propriétaire ou en groupe, autre identité) ; `test_v50_04` refait (sonde jouée sous 64097 hors du bac, dans un espace IPC jetable : témoin lu sur l'hôte) |
| **CL15-02** (moyenne) : mémoire de l'hôte non bornée (System V, `/dev`, et `RLIMIT_AS` par processus seulement) | Les trois corrections de CL15, toutes : (a) `--remount-ro /dev` juste après `--size … --tmpfs /dev/shm` ; (b) **borne du bac entier par groupe de contrôle** (`BorneMemoireBac`) : un groupe `memory` neuf par exécution, enfant de celui du noyau, borné à `memoire_mo` (v1 : `memory.limit_in_bytes`, et `memsw` s'il existe ; v2 : `memory.max`, `memory.swap.max = 0`), le processus lancé y entre **avant son `exec`** (`preexec_fn`), puis le groupe est vidé (SIGKILL **par identifiant**, R10) et retiré ; le résultat d'exécution porte `memoire_bac` (borne, `oom_kill`, pic) et le motif « mémoire du bac entier atteinte » ; (c) **filtre d'appels système** (`programme_seccomp`, BPF classique écrit par le noyau, passé à `bwrap --seccomp FD` par un tube) : `EPERM` pour `shmget/shmat/shmctl/shmdt`, `msgget/msgsnd/msgrcv/msgctl`, `semget/semop/semctl/semtimedop`, `memfd_create`, `memfd_secret`, `io_uring_setup/enter/register`, `userfaultfd`, `ptrace`, `process_vm_readv/writev`, `kcmp`, `pidfd_getfd`, `bpf`, `perf_event_open`, `keyctl`, `add_key`, `request_key` ; tout appel x32 refusé ; une autre architecture **tuée**. Numéros vérifiés sur `asm/unistd_64.h` ; **x86_64 seulement** : ailleurs, l'étage est refusé (aucun filtre deviné). Sonde : artefacts `DEV` (64 Mo dans `/dev`), `SECCOMP`, `SYSV-SHM` (64 Mo), `SYSV-MSG`, `SYSV-SEM`, `MEMFD`, `IO-URING`, `PTRACE`, `MEMOIRE-BAC` (5 enfants d'un quart de la borne chacun, touchés, `oom_score_adj` 1000 : au moins un doit être tué) **et** constat du noyau sur l'hôte (`oom_kill ≥ 1`). Lever la borne : demande expresse `memoire_bac_non_bornee_permise` (`--memoire-bac-non-bornee-permise`), dite au manifeste et à la description ; sinon, sans groupe utilisable, étage refusé. Borne minimale : **512 Mo** (`MEMOIRE_BAC_MIN_MO` : la sonde de processus, 1 056 processus endormis, en prend ~280 Mo, mesuré) | réel : `test_v51_04` (artefacts de CL15 : 45 Mo dans `/dev` → `EROFS` ; System V 256 Mo → `EPERM` ; `memfd` → `EPERM` ; 6 enfants de 200 Mo pour une borne d'1 Go → tués par le groupe, `oom_kill ≥ 1`, pic ≤ borne, groupe retiré ; sain : `multiprocessing`, `/dev/shm`, `/dev/null`, `/dev/urandom`, 100 Mo → code 0, aucune limite) ; `test_v51_05` (mutations sous le vrai bac : sans `--remount-ro /dev`, sans filtre, hors du groupe, hors du groupe avec évaluation neutralisée → chacune refusée avec son motif ; demande expresse acceptée et dite ; borne < 512 Mo refusée) ; `test_v51_06` (programme BPF rejoué par un interpréteur : refusés, permis, x32, i386 et aarch64 tués ; architecture inconnue refusée) ; `test_v51_13` (groupe créé, processus entré avant `exec`, tué par identifiant, groupe retiré) |
| **CL15-03** (moyenne) : le noyau suit un lien substitué pendant la surveillance (oracle sur des chemins de l'hôte) | Correction de CL15 : `inventaire_travail` parcourt **par descripteurs** — racine ouverte `O_NOFOLLOW|O_DIRECTORY` ; chaque sous-dossier rouvert composant par composant depuis elle (`_ouvrir_sous_dossier`), puis comparé (`st_dev`, `st_ino`) à l'entrée vue par `lstat` ; un lien à sa place (`ELOOP`, `ENOTDIR`) ou un autre dossier = dépassement « dossier remplacé pendant le parcours » (le bac est tué pendant l'exécution), **sans parcourir la cible** ; fichiers hachés par `_sha256_dans` (même inode que l'entrée vue), liens lus par `readlinkat`. Même règle pour l'inventaire final. Le motif ne dit rien de la cible : plus d'oracle | `test_v51_07` (déterministe : la substitution posée entre `lstat` et l'ouverture par un crochet d'essai ; cible factice = dossier de l'hôte réservé au superutilisateur avec un fichier creux de 300 Mo, et la même vide : même motif « remplacé » ; autre vrai dossier à la place : « remplacé » ; **contraste** : la version 1, même substitution, rend « plus de 268435456 octets » pour la cible pleine et rien pour la vide — l'oracle de CL15 ; sain : sous-dossiers hachés, lien consigné, racine-lien refusée) ; réel : `test_v51_08` (la course de CL15 sous le vrai `bwrap` : 1 500 fichiers, bascule de `zz` pendant 4 s vers la cible pleine puis vide : jamais « octets » ni « entrées », seulement « remplacé » ; sain : 1 500 fichiers et des dossiers, aucune limite) ; `test_v50_08` adapté (l'artefact « illisible » se pose sur l'ouverture par descripteur) |
| **CL15-04** (mineure) : essais réels ignorés en silence ; assertion d'identité sans effet | `exiger_essai_reel` : un essai réel (vrai `bwrap`, ou noyau superutilisateur avec `setpriv`) **échoue** s'il ne peut pas se jouer ; seule la variable explicite **`POLE_ESSAI_BAC_REEL_NON_JOUE=1`** le fait ignorer, avec le motif « ESSAI RÉEL NON JOUÉ », compté au résultat de la suite. Les quatre `skipUnless(which("bwrap"))` sont remplacés par `essai_reel_bwrap` ; les `skipTest` des essais sous `setpriv` aussi. `executeur_reel` n'exige plus les deux variables sous un noyau superutilisateur : sans elles, il prend l'identité 64097 (vérifiée par `setpriv`) et un dossier racine provisoire (`racine_bac_essai`), retiré à la fin ; les variables `POLE_ESSAI_UTILISATEUR_BAC`, `POLE_ESSAI_RACINE_TRAVAIL_BAC` restent permises (conteneur de session-depot). L'assertion `'0', '0', '1'` de `test_v50_15` est remplacée par le **propriétaire, vu de l'hôte, d'un fichier créé par le script** (`r.txt`, lu avant le retrait du dossier) : identité dédiée, jamais 0 | `test_v51_09` (échec sans la variable, `SkipTest` « ESSAI RÉEL NON JOUÉ » avec ; `executeur_reel` et le décorateur échouent sans `bwrap` ; plus aucun `skipUnless(which("bwrap"))` ni l'ancienne assertion dans `essais/`) ; `test_v50_15` (nouvelle assertion, jouée) |
| **CL15-05** (mineure) : Argon — modèle servi de format inconnu, refusé après l'appel payé ; `--modele-commande-externe` déclaratif | Lanceur v2 : `--modele-commande-externe` autre que `gemini-4-argon` est **refusé avant tout appel** (moteur réel) tant que **`--commande-externe-lit-modele`** n'atteste pas une commande qui lit le modèle demandé (`--modele` ou `MODELE_DEMANDE_POLE` : une v3 de la commande, nouveau nom, R12, côté session-depot) ; l'attestation sans `--commande-externe` est une erreur d'options. **Au premier appel réel d'Argon**, le format réel de `modelVersion` sera connu : **le premier appel réel d'Argon fixe `--modele-servi-externe-permis` avec Lazar**, au coût d'une session (un identifiant servi hors liste est refusé **après** l'appel payé, R-764, sans repli). La commande d'Argon n'est pas modifiée (hors de ce dépôt) | `test_v51_10` ; `test_v50_14` et `test_cl43_03` adaptés (l'étiquette « gemini-argon » des essais exige l'attestation) |
| **CL15-06** (mineure) : `ptrace` du processus 1, `io_uring`, chemin de l'hôte dans `/proc/1/environ` | Filtre d'appels système (CL15-02 c) ; **`HOME=/`** dans l'environnement passé à `setpriv` et `bwrap` (le script garde `HOME=/travail` par `--setenv`) | réel : `test_v51_11` (dans le bac : `ptrace` attache, `io_uring_setup`, `bpf`, `perf_event_open`, `keyctl`, `add_key` — trousseau 0, rien ne peut y être créé —, `userfaultfd`, `process_vm_readv`, `kcmp`, `pidfd_getfd` → `EPERM` ; `/proc/1/environ` sans le chemin de l'hôte, `HOME=/` ; sain : `fork`, tubes, paires de prises) |
| **CL15-07** (mineure) : l'utilisateur dédié n'est pas contrôlé seul | `verifier_identite_dediee` (au départ, dans `verifier_identite`) : refus si un **processus vivant de l'hôte** porte l'identité dédiée (`/proc/*/status`, identités réelle, effective, sauvée, de fichiers ; zombis exclus), ou si l'identité a un **compte avec un interpréteur de commandes** (hors `nologin`, `false`) ; **avant chaque exécution** : un tel processus interrompt l'étage (`EtageInterrompu`) ; après : il est consigné ; **verrou** d'un seul bac à la fois par identité, par prise abstraite (`\0pole-bac-verrou-<uid>`, aucun fichier, rendue à la mort du processus), tenu de `ouvrir_racine_travail` à `fermer_racine_travail` | réel : `test_v51_12` (intrus `sleep` sous 64097 → départ refusé, exécution interrompue ; arrêté par son identifiant → étage accepté ; compte `/bin/bash` refusé, `nologin` accepté ; second bac sur la même identité refusé tant que le premier tient sa racine) |

**Rétrocompatibilité.** Sans `--tests-de-mort`, le lanceur v2 rend **exactement** les fichiers du lanceur v1 (v50) : même chemin de
sortie (la graine du moteur simulé en dépend), course simple (42 fichiers) et course à seconde passe (50 fichiers), contrôle compris,
octet pour octet (`test_v51_14`) ; les empreintes gelées de la v47 (`test_v48_11`) tiennent sur le cœur v2. Avec l'étage, la
description du bac (manifeste) porte les clés nouvelles (`version_du_module`, `memoire_du_bac_entier`, `dev`, `filtre_d_appels_systeme`,
`identite_dediee_controlee`, `identite_lue_sur_l_hote`) et chaque exécution `memoire_bac`.

**Changements de contrat à lire avant tout lancement de l'étage** (tous refusent plutôt que de se replier) : (1) un groupe de
contrôle `memory` utilisable par le noyau est exigé (cgroup v1 monté, ou v2 délégué aux enfants), sinon étage refusé, sauf
`--memoire-bac-non-bornee-permise` (dit) ; (2) `--memoire-test-mo` ≥ 512 avec la borne ; (3) x86_64 seulement ; (4) aucun autre
processus, aucun compte avec interpréteur de commandes pour l'utilisateur dédié, un seul bac à la fois par identité ;
(5) `--modele-commande-externe` (autre que `gemini-4-argon`) exige `--commande-externe-lit-modele`.

## Essais

**517 essais** (502 de la v50, rejoués sur les versions 2 dans `essais/test_v7_ideation_v2.py`, plus 15 nouveaux dans
`essais/test_v51_bac_reel.py`) : **517 OK, 0 échec, 0 erreur, 0 ignoré**, deux exécutions complètes sur l'arbre final
(`env -i PATH=/usr/bin:/bin HOME=/tmp LANG=C.UTF-8 python3 -B -m unittest discover -t . -s essais -p 'test_*.py'`, sans
aucune variable `POLE_ESSAI_*` : identité 64097 et dossier racine provisoire pris par les essais), environ 340 s chacune. Tous les
essais réels sont **joués** : les quatre de la v50 (`test_v48_22`, `test_v49_19`, `test_v50_15`, `test_v50_16`), ceux qui exigent un
noyau superutilisateur et `setpriv` (`test_v50_04`, `_05`, `_08`), les sept essais sous le vrai `bwrap` de la v51 (`test_v51_01`,
`_02`, `_04`, `_05`, `_08`, `_11`, `_12`) et `test_v51_13` (groupe de contrôle réel, noyau superutilisateur).

**CL15-04 éprouvé** : avec un `PATH` sans `bwrap`, les dix essais réels sous `bwrap` de la sélection (`test_v51_bac_reel` et
`test_v48_22`, `test_v49_19`, `test_v50_15`) **échouent** (`FAILED (failures=10)`) ; avec `POLE_ESSAI_BAC_REEL_NON_JOUE=1`, ils sont
ignorés avec le motif « ESSAI RÉEL NON JOUÉ (…, demande explicite) : bwrap absent … » (`OK (skipped=10)`).

En v50 : 502 essais, 498 OK et 4 ignorés hors variables (CL15-04), ou 498 OK, 2 échecs, 2 erreurs avec le vrai bac (CL15-01).
Première exécution des essais v50 rejoués sur les versions 2, avant adaptation : 7 échecs et 4 erreurs, tous des essais rendus
faux par une correction voulue (signature `commande(…, fd_seccomp)`, `--remount-ro /dev` avant celui de la racine, lignes de la
sonde, parcours par descripteurs, CL15-05, provenance de la v50 lue dans son archive) : adaptés, chacun marqué « v51 ».
Aucun processus survivant ; `essais/_tmp` et `__pycache__` retirés ; aucun groupe de contrôle `pole-bac-*` restant.

## Prérequis de l'opérateur pour l'étage réel (rien n'est préparé ici)

Ceux de la v50 (utilisateur dédié sans privilège ni processus, **sans compte** ou à `nologin`, `setpriv`, `bwrap` ≥ 0.9.0 non setuid,
dossier racine à lui en 0700, parents traversables, python lisible, espaces d'utilisateurs non privilégiés permis), **plus** : un
groupe de contrôle `memory` où le noyau superutilisateur peut créer des enfants (cgroup v1 : hiérarchie `memory` montée en
écriture ; cgroup v2 : `memory` dans `cgroup.subtree_control` du groupe du noyau), x86_64, `--memoire-test-mo` ≥ 512. Ex. :
`python -I -B demonstrations/ideation_v2.py … --tests-de-mort N … --utilisateur-bac 64097 --dossier-travail-bac /srv/bac-pole`.

## Ce qui n'est pas vérifié, réserves

- **Le conteneur de session-depot n'a pas été joué.** Tout ce qui est réel ici l'est sur la machine décrite plus haut (même noyau
  et même `bwrap` que CL15). À rejouer là-bas, avec l'utilisateur dédié réel, avant tout GO de l'étage : `python3 -B -m unittest
  discover -t . -s essais -p 'test_*.py'` (avec `POLE_ESSAI_UTILISATEUR_BAC` et `POLE_ESSAI_RACINE_TRAVAIL_BAC` si l'identité
  64097 ou le dossier provisoire du système ne conviennent pas), et les sondes de CL15.
- **cgroup v2 non exercé** : le chemin v2 de `BorneMemoireBac` (`memory.max`, `memory.events`, `memory.peak`) est écrit, pas joué
  (la machine est en v1). Dans un conteneur v2 non délégué, l'étage sera refusé (motif dit) ; la délégation est à l'opérateur.
- **Filtre d'appels système x86_64 seulement** ; aarch64 et autres : étage refusé.
- **Surface restante** (aucune évasion constatée) : `mountinfo` du bac montre encore le chemin de l'hôte du dossier de travail
  (propre aux montages liés) ; le filtre est une **liste de refus** (les appels non listés restent permis : `--cap-drop ALL`,
  l'utilisateur dédié et `--disable-userns` restent les barrières principales) ; tubes et prises ne sont pas bornés un par un : leur
  mémoire noyau entre dans le groupe selon la comptabilité du noyau Linux (non mesuré ici).
- **CL15-07** : le contrôle des processus de l'identité dédiée a une fenêtre entre le balayage et le lancement (un processus lancé
  par le superutilisateur entre les deux échapperait au contrôle de départ, pas à celui d'après) ; le verrou ne couvre que les
  noyaux d'un même espace réseau.
- **Contrôleur `pids`** non utilisé (CL15-02 b le proposait en double de `RLIMIT_NPROC`) : sous l'utilisateur dédié,
  `RLIMIT_NPROC` tient (sonde `PROCESSUS`, refus après 1 021) ; il compte aussi les autres processus de l'identité, d'où CL15-07.
- **Argon** : la commande réelle n'est ni modifiée ni relancée ; le format réel de `modelVersion` reste inconnu (CL15-05).
- `essais/test_v7_ideation_v2.py` garde des docstrings de la v50 qui disent « seulement si `bwrap` est installé » : le code, lui,
  échoue sans `bwrap` (CL15-04).

## Fabrication des empreintes

```
find . -type f ! -path './EMPREINTES-orchestrateur-pole-v7-v51.txt*' ! -path '*/__pycache__/*' ! -path './essais/_tmp/*' | sed 's|^\./||' | LC_ALL=C sort | xargs sha256sum > EMPREINTES-orchestrateur-pole-v7-v51.txt
sha256sum EMPREINTES-orchestrateur-pole-v7-v51.txt > EMPREINTES-orchestrateur-pole-v7-v51.txt.sha256
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v51.txt
```
La liste porte **tous** les fichiers de l'arbre v51 (LISEZMOI et EMPREINTES des versions 1 à 50, archives `CODE-…-v49.zip`,
`CODE-…-v50.zip` et `CODE-…-v51.zip` avec leurs `.sha256`, `entrees-cl15/`), sauf elle-même et son `.sha256`.
`CODE-orchestrateur-pole-v7-v51.zip` contient le code de la v51 (mêmes dossiers que l'archive de la v50 : `conception-v7-v1.md`,
`demonstrations/`, `essais/`, `exemples/`, `pole/`).
