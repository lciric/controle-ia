# Contre-lecture CL16 — orchestrateur du pôle, version 51 (corrections de CL15), jouée sous un vrai `bwrap`

- Date : 2026-10-30, 08:02 UTC.
- Contre-lecteur : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent **neuf** (règle R2) : **n'a écrit aucune version de
  l'orchestrateur, et en particulier pas la v51**. Je rédige ; je ne committe rien.
- Objet : `brouillons/canal-reprise-releve-v1/envois/session-depot/orchestrateur-pole-v7-v51/orchestrateur-pole-v7/` de la
  branche `origin/canal/session-depot-reprise-n55`, extrait par `git archive` dans le bloc-notes de la session. Arbre de la v50
  (`origin/canal/conv-audit-n04`, `…/pole-scientifique-automatique-v1/orchestrateur-pole-v7/`) lu pour comparaison. Rien d'autre
  lu sur `canal/*` ; aucune branche `donnees/*` ni `quarantaine/*` ; ni `prereg/P3-consignes-v1.md`, ni `diag/*/traces`.
- Machine : `bwrap` 0.9.0 (non setuid), `setpriv` et `unshare` (util-linux), noyau Linux 6.18.44, **x86_64**, Python 3.13.17,
  cgroup v1 (`memory` monté à `…/process_api/…/claude-code-bash`), noyau du pôle en **superutilisateur**, utilisateur dédié
  **64097** sans compte (`getent passwd 64097` : vide). La même machine que CL15.
- **Aucun appel payant, aucune clé, aucun réseau** : chaque bac tourne sous `--unshare-all --unshare-net`, le pilote sous
  `env -i`. Cibles **factices** seulement, dans le bloc-notes ou des dossiers provisoires. **Aucune écriture dans `/proc/sys`**
  ni dans un réglage global : seulement des ouvertures en écriture, sans écriture. État de l'hôte après les essais : aucun
  processus 64097, aucun groupe `pole-bac-*`, aucun `/tmp/cl16-*` ni `/tmp/essai-*`, aucun témoin `/usr/lib/cl1*` ;
  `core_pattern` = `core` et nom d'hôte `vm`, comme avant.

## Empreintes vérifiées

| fichier | empreinte SHA-256 | vérification |
|---|---|---|
| `EMPREINTES-orchestrateur-pole-v7-v51.txt` | `8044fa5c5a6512206b1e485d89f8d170cd0de34a13def1b21c5a45daab972c74` | égale à l'attendue (`8044fa5c…`) et à son `.sha256` ; **321 lignes** |
| fichiers listés par la v51 | — | `sha256sum -c` : **tous OK** |
| `CODE-orchestrateur-pole-v7-v51.zip` | `a58a9b8b80861e48fa5e547c4151cc80c15a67a5e6a83d9cf6d4c880dc8f5f46` | égale à l'attendue (`a58a9b8b…`) et à son `.sha256` |
| `CODE-orchestrateur-pole-v7-v50.zip` | `5bb498dd3a319495f27b171f44d1f7ecc4ac1a5ff8b470a76a64c38b5b2efa5e` | égale à son `.sha256` ; 116 fichiers |
| `LISEZMOI-orchestrateur-pole-v7-v51.md` | `fb06d01ae9cccd5fbd51afaaa0cc8482e0dc1f818909f38cdb4692bfe47e9f9a` | lu |
| `pole/tests_de_mort_v2.py` | `363a3725…a41a` | = tableau du LISEZMOI v51 |
| `pole/ideation_v2.py` | `67d2ad35…fefc` | = tableau |
| `demonstrations/ideation_v2.py` | `bc5e9c98…9845` | = tableau |
| `essais/test_v7_ideation_v2.py` | `35f99fa8…b7f6`… (`35f99fa8d99dbf536e1ed7b824145fd8f92ca4a5ed72e750eb1a43cd6de83b7f`) | = tableau |
| `essais/test_v51_bac_reel.py` | `4e4a4b60…3a58` | = tableau |
| R12 : `EMPREINTES-…-v50.txt` sur l'arbre v51 | — | **177 OK, 1 absent** (`essais/test_v7_ideation.py`, dans `CODE-…-v50.zip` à son empreinte) |

Sondes et journaux de cette contre-lecture (bloc-notes, hors dépôt, non versés ; R6) :

| fichier | SHA-256 |
|---|---|
| `sondes/p_cl16.py` (batterie d'attaques, vrai bac, utilisateur dédié) | `dbf43643b5ea249ee6e9401fddbbe041cd97b4ffd4f29ab6b9940e883e806a1e` |
| `sondes/p_mutations.py`, `p_mut2.py` (gardes muettes) | `8a4826e5…588a`, `57edaacf…b262` |
| `sondes/p_min.py` (borne minimale) | `91cdf602ff2e81e969a684f05d2e5de705aa946f64b167c0b67dd7fb65f7896a` |
| `journaux/p_cl16.log`, `p_mutations.log`, `p_mut2.log`, `p_min.log` | `b101edce…6c5f`, `76d8e3dd…9928`, `f150bf33…8a5c`, `779d8a27…0ccb` |

## Verdicts

- **v51 sans l'étage (`--tests-de-mort 0`) : lançable en l'état.** Le cœur et l'étage de la v1 (v50) restent octet pour octet
  (R12). Le lanceur v2 rend **exactement** les fichiers du lanceur v1 sans l'étage (`test_v51_14`, joué dans la suite ci-dessous,
  OK). Réserve inchangée, reportée : Argon (CL15-05) — le premier appel réel fixe `--modele-servi-externe-permis`, au coût d'une
  session, sans repli.
- **Étage de tests de mort (`--tests-de-mort ≥ 1`) : lançable après CL16-01 (ou en donnant au moins ~768 Mo), et après rejeu
  dans le conteneur de session-depot.** Les **sept** constats de CL15 sont traités et **éprouvés sous un vrai `bwrap`** : toutes
  les évasions de CL13, CL14 et CL15 sont **bloquées**, et aucune évasion nouvelle n'a abouti (les routes de mémoire hors de la
  liste du filtre, dont `mmap` anonyme, sont rattrapées par le groupe de contrôle). **Mais** à la borne mémoire **minimale
  annoncée (512 Mo)**, la sonde `disponible()` s'auto-tue et **refuse l'étage** (CL16-01) : la configuration minimale que le
  LISEZMOI et la garde `MEMOIRE_BAC_MIN_MO` autorisent ne marche pas. À traiter avant tout GO de l'étage : CL16-01. Réserves de
  l'auteur confirmées (cgroup v2 non joué ; `mountinfo` montre le chemin de l'hôte ; filtre = liste de refus) ; CL16-02 et CL16-03
  mineures.

## Comptes d'essais (critère 2)

- **Suite complète de la v51** (`env -i … python3 -B -m unittest discover -t . -s essais -p 'test_*.py'`, noyau superutilisateur,
  `bwrap` présent, **aucune** variable `POLE_ESSAI_*`) : **`Ran 517 tests in 346.405s — OK`**, exit 0. **517 OK, 0 échec, 0 erreur,
  0 ignoré** — l'annonce de l'auteur est exacte. Les dix essais réels sous `bwrap` et les essais à `setpriv`/groupe de contrôle
  sont **joués** (non ignorés). Hygiène : `essais/test_v7_v11.py` l. 411 émet des `ResourceWarning` (fichier non fermé) — fichier
  **v50 gardé inchangé** (R12), défaut antérieur, sans effet sur le verdict.
- **Gardes muettes (R5), indépendamment de la batterie de l'auteur** (`p_mutations.py`, `p_mut2.py`, utilisateur dédié 64097,
  1 024 Mo) : chaque garde retirée fait **refuser l'étage** par la sonde, avec son motif —
  | garde retirée | motif de refus |
  |---|---|
  | filtre d'appels système (`FILTRE_APPELS=False`) | « filtre d'appels système absent (Seccomp=0, CL15-02) » |
  | `--remount-ro /dev` | « /dev est inscriptible (ecrit-50-Mo-puis-errno-27, CL15-02) » |
  | entrée dans le groupe de contrôle (`_limites(…, None)`) | « la mémoire du bac entier n'est pas bornée (REUSSI-5-enfants, CL15-02) » |
  | `--ro-bind /proc/sys /proc/sys` | « 17 réglages de /proc/sys s'ouvrent en écriture (CL14-01) » |
  | `--disable-userns` | « le script crée un espace d'utilisateurs imbriqué (CL14-03) » |

  Cas sain, même bac : `disponible()` → vrai. Cinq gardes, toutes fermantes.

## Critère 1 — artefacts de CL13, CL14, CL15 et attaques nouvelles, rejoués sous le vrai `bwrap` (`p_cl16.py`)

Exécuteur réel v2, `utilisateur_bac=64097`, racine à lui, 512 Mo, sous `setpriv` ; chaque sortie ci-dessous.

| artefact | sortie | bloqué ? |
|---|---|---|
| CL15-01 identité (témoin lu sur l'hôte) | dans le bac `UID 65534`, `uid_map ['65534','0','1']` (ce que la v50 **lisait** comme 0) ; **témoin sur l'hôte `64097:64097`** (= attendu, jamais 0) | **oui, corrigé** |
| CL13-01 remontage `/usr`, `/` | `REMONTE_USR -1 1` (EPERM), `REMONTE_RACINE -1 1` | oui |
| CL14-01 `/proc/sys` (ouverture sans écrire) | `PROCSYS_OUVRABLES 0`, `CORE_PATTERN refus 13` (EACCES) | **oui** |
| CL14-02 setuid | `chmod 4755` « réussi » mais **hôte : propriétaire 64097**, mode `0o104755` (setuid vers l'utilisateur dédié sans privilège, pas vers root ; l'inventaire le refuse) | oui (sans danger) |
| CL14-03 espace d'utilisateurs imbriqué | (filtre : `unshare(CLONE_NEWUSER)` reste permis mais sans capacité ; `--disable-userns` le refuse — voir mutation) | oui |
| CL15-02 System V | `SYSV_SHM -1 1`, `SYSV_MSG -1 1`, `SYSV_SEM -1 1` (EPERM, filtre) | **oui** |
| CL15-02 `memfd_create`, `io_uring_setup` | `MEMFD refus 1`, `IO_URING -1 1` (EPERM) | **oui** |
| CL15-02 `/dev` inscriptible | `DEV refus 30` (EROFS : `--remount-ro /dev`) | **oui** |
| CL14-10 `/dev/shm` borné | `SHM refus apres 32 errno 28` (ENOSPC à 32 Mo) | **oui** |
| **mémoire par voie hors liste** (`mmap` anonyme, 6 × 200 Mo pour une borne de 512 Mo) | `MMAP_ENFANTS_TUES 5` ; `memoire_bac oom_kill=5, pic=536870912 (=borne), retire=true` ; limite « mémoire du bac entier atteinte » | **oui** (le groupe rattrape ce que le filtre ne couvre pas) |
| CL15-06 `/proc/1/environ` | `[PATH…, HOME=/, LANG…]` — **plus de chemin de l'hôte**, `HOME=/` | **oui, corrigé** |
| CL15-06 `/proc/self/mountinfo` | `MOUNTINFO_TRAVAIL True` ; ligne : `… /tmp/cl16-racine-…/etage-travail-…/a6_surface /travail … resuid=65534,resgid=65534` | **fuite d'information** (CL16-03 ; non exploitable, déjà en réserve) |
| CL15-03 lien substitué pendant la surveillance | (déterministe et réel, essais de l'auteur `test_v51_07`, `_08`, rejoués dans la suite OK ; parcours par descripteurs, `st_dev/st_ino`, motif « dossier remplacé pendant le parcours » sans dire la cible) | **oui, corrigé** |
| nettoyage | après la batterie : `groupes pole-bac-* : []`, `processus 64097 : []`, `fermer_racine_travail → True` | oui |

**CL15-02, borne du bac entier (groupe de contrôle)** confirmée réelle : le `mmap` anonyme (appel **non** dans la liste de refus)
est arrêté par le groupe, pas par le filtre — le groupe est le filet qui couvre toute route de mémoire (anonyme, `/dev`,
`/dev/shm`, fichiers de `/travail`). Le groupe est créé enfant de celui du noyau, relu, le processus y entre **avant `exec`**
(`preexec_fn`), puis il est vidé par identifiant (R10) et retiré ; aucun n'est resté (vérifié).

## Constats

### CL16-01 — La borne mémoire minimale annoncée (512 Mo) ne marche pas : la sonde `disponible()` s'auto-tue et refuse l'étage

- **Gravité : moyenne.** Ferme sans risque (aucune évasion), mais **bloque une configuration minimale légitime** et contredit le
  LISEZMOI (« `--memoire-test-mo ≥ 512` », prérequis opérateur) et la garde `MEMOIRE_BAC_MIN_MO = 512`. Même classe que CL15-01
  et CL15-04 : une garde qui donne une fausse confiance ; une configuration documentée qui, en silence, ne peut pas démarrer.
- **Fichier et ligne** : `pole/tests_de_mort_v2.py` l. 168 (`MEMOIRE_BAC_MIN_MO = 512`) ; `sonde_pour` l. 1988-1989
  (`enfants = ENFANTS_ESSAI_MEMOIRE = 5`, `par_enfant = borne // 4`, soit **5/4 de la borne** touchés par la sonde elle-même) ;
  `verifier_outils` l. 1387-1389 (n'autorise que `≥ 512`) ; l'artefact `MEMOIRE-BAC` de `_SONDE_MODELE` l. 1929-1976 ; le
  processus parent de la sonde ne baisse pas son `oom_score_adj`.
- **Défaut** : à 512 Mo (la borne minimale), les 5 enfants de la sonde (`512//4 = 128 Mo` chacun, 640 Mo ensemble) plus le
  processus parent dépassent la borne du groupe, et le noyau Linux tue **le processus racine de la sonde** (code 137), non pas
  seulement les enfants. `evaluer_sonde_privileges` voit `code 137` et refuse (« tuée (SIGKILL) : mémoire du bac peut-être trop
  petite pour la sonde »). La suite ne l'a jamais vu : `executeur_reel` (l. ~7996 de `test_v7_ideation_v2.py`) prend le défaut
  **1 024 Mo**, et le seul `memoire_mo=512` de la suite (l. 7186) passe par `ExecuteurFactice`, **sans** groupe de contrôle. Le
  commentaire de `MEMOIRE_BAC_MIN_MO` raisonne sur l'artefact `PROCESSUS` (1 056 processus endormis ≈ 280 Mo), pas sur
  l'artefact `MEMOIRE-BAC` qui sur-alloue délibérément.
- **Essai** (`p_min.py`, 3 passages par taille) :
  ```
  mo= 512 -> ok=False [TUEE] « code 137 … tuée (SIGKILL) : mémoire du bac peut-être trop petite » (3/3)
  mo= 640 -> ok=True (3/3) ; mo= 768 -> ok=True (3/3) ; mo=1024 -> ok=True (3/3)
  ```
  Déterministe : c'est bien le groupe **du bac** (confiné, `oom_kill` compté, groupe retiré) qui tue, pas une pression de l'hôte.
- **Correction** : relever `MEMOIRE_BAC_MIN_MO` au-dessus de la borne où la sonde tient (ici ≥ 640 ; prendre une marge, p. ex.
  768), **ou** protéger le processus racine de la sonde (`oom_score_adj` très négatif) et/ou réduire la fraction par enfant de
  l'artefact `MEMOIRE-BAC` (p. ex. 3 enfants d'un tiers, qui dépasse encore sans noyer le parent). Dans tous les cas, **ajouter
  un essai réel à exactement `MEMOIRE_BAC_MIN_MO`** (c'est l'absence de cet essai qui a laissé passer le défaut, R5).

### CL16-02 — Le lanceur v1 reste dans l'arbre ; lancer l'étage par lui donne l'étage v50 cassé

- **Gravité : mineure** (ferme sans risque : l'étage v1 est refusé partout, CL15-01 ; dit au LISEZMOI, mais aucune garde).
- **Fichier et ligne** : `demonstrations/ideation_v1.py` et `pole/tests_de_mort.py` (v1) **gardés** dans l'arbre (R12) ; LISEZMOI
  v51 « Pour l'étage, utiliser le lanceur v2 ». Rien n'empêche `ideation_v1.py … --tests-de-mort N`.
- **Défaut** : un opérateur qui garde l'habitude du lanceur v1 obtient l'étage de la v50, refusé dans toutes les configurations
  réelles (CL15-01) — fail-closed, donc sans danger, mais sans l'étage et sans message clair pointant vers la v2.
- **Correction** : faire refuser `--tests-de-mort` au lanceur v1 avec un renvoi explicite vers `ideation_v2.py`, ou le dire plus
  haut. (Les imports tardifs de `pole/moisson.py` et `pole/dossier_ferme.py` vers `pole/ideation.py` v1 sont inoffensifs :
  constantes et fonctions pures identiques en v2, vérifié au LISEZMOI.)

### CL16-03 — `mountinfo` du bac montre le chemin de l'hôte et `resuid/resgid` (fuite d'information, non exploitable)

- **Gravité : mineure** (déjà en réserve au LISEZMOI ; **aucune évasion** : `/proc/sys` est en lecture seule et le script n'a
  aucune capacité, donc la voie `core_pattern` de CL14-01 reste fermée ; le script apprend son chemin sur l'hôte mais n'en fait
  rien sur ce banc).
- **Fichier et ligne** : propre aux montages liés (`--bind travail /travail`) ; pas de correctif simple sans changer la façon de
  monter le dossier de travail.
- **Essai** : `MOUNTINFO_LIGNE … /tmp/cl16-racine-…/etage-travail-…/a6_surface /travail … resuid=65534,resgid=65534`.
- **Correction** : aucune requise pour la sécurité ; si on veut fermer la fuite, monter le dossier de travail par un pivot
  (`pivot_root`/`--bind` sur un chemin neutre) ou l'accepter explicitement. Je confirme le constat de l'auteur et le classe
  non-exploitable ici.

## Critère 3 — rétrocompatibilité, R12, sortie de `test_v7_ideation.py`

- **Rétrocompatibilité** : sans `--tests-de-mort`, le lanceur v2 rend **octet pour octet** les fichiers du lanceur v1
  (`test_v51_14`, joué dans la suite, OK) ; les empreintes gelées de la v47 tiennent sur le cœur v2 (`test_v48_11`). Aucune garde
  de dépense modifiée.
- **R12 : appliquée strictement cette fois, et vérifiée.** Aucun module de la v50 n'est modifié en place : `sha256sum -c
  EMPREINTES-…-v50.txt` sur l'arbre v51 donne **177 OK** et **un seul absent**, `essais/test_v7_ideation.py`. Les corrections
  vivent dans des fichiers **nommés** (`…_v2.py`), dont chaque empreinte égale le tableau du LISEZMOI v51 (vérifié). `CODE-…-v51.zip`
  (`a58a9b8b…`) et `CODE-…-v50.zip` (`5bb498dd…`, 116 fichiers) vérifiés.
- **Sortie de `essais/test_v7_ideation.py` de l'arbre : justifiée.** Ce fichier essaie les modules v1, dont la sonde est fausse
  (CL15-01) ; joué avec le vrai `bwrap`, il échouerait (4 essais réels) ou serait ignoré (CL15-04). Il est remplacé par
  `test_v7_ideation_v2.py` (502 essais rejoués sur les versions 2) et **conservé, inchangé, dans `CODE-…-v50.zip`** à son
  empreinte v50 (vérifié par `test_v51_15`, joué OK). Le fichier n'est donc pas perdu : il est archivé. C'est une lecture
  raisonnable de R12 (« versions dans les noms ; on n'écrase jamais ») ; le code reste récupérable par l'archive et par
  l'historique Git.

## Critère 4 — défauts nouveaux

CL16-01 (moyenne, le seul bloquant), CL16-02 et CL16-03 (mineures). Aucune évasion nouvelle du bac. Les réserves de l'auteur sont
confirmées et n'ajoutent rien d'exploitable sur ce banc : cgroup v2 non joué (chemin écrit, non exercé ; l'étage refuse si
`memory` n'est pas délégué) ; filtre x86_64 seulement (autres architectures refusées) ; le filtre est une liste de refus (le
groupe de contrôle est le filet pour la mémoire, prouvé) ; `pids` non utilisé (`RLIMIT_NPROC` tient sous l'utilisateur dédié) ;
fenêtre de CL15-07 entre le balayage et le lancement ; tubes et prises non bornés un par un (bornés par `RLIMIT_NOFILE = 512`,
mémoire noyau non mesurée).

## Récapitulatif par gravité

| gravité | constats |
|---|---|
| haute / critique | aucun |
| moyenne | CL16-01 (borne minimale 512 Mo : la sonde s'auto-tue, étage refusé ; ferme sans risque) |
| mineure | CL16-02 (lanceur v1 gardé), CL16-03 (fuite `mountinfo`, non exploitable) |

Ordre conseillé : CL16-01 (relever `MEMOIRE_BAC_MIN_MO` ou protéger le parent de la sonde, **plus** un essai réel à la borne
minimale), puis rejouer `p_cl16.py`, `p_mutations.py`, `p_min.py` et les sondes de l'auteur **dans le conteneur de
session-depot**, avec l'utilisateur dédié réel et la mémoire de production, avant tout GO de l'étage.
