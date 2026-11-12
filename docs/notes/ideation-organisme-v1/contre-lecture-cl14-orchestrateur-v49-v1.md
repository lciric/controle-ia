# Contre-lecture CL14 — orchestrateur du pôle, version 49 (corrections de CL13)

- Date : 2026-10-30, 01:30 UTC.
- Contre-lecteur : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent **neuf** (règle R2) : n'a écrit aucune version de l'orchestrateur.
- Objet : `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/orchestrateur-pole-v7/` de la branche
  `origin/canal/conv-audit-n04` (tête `b5d2da66` ; arbre de la v49 au commit `ecb1b408`), extrait par `git archive` hors du dépôt.
  Arbre de la v48 pour comparaison : même dossier au commit `19cadf8c`. Rien d'autre lu sur `canal/*` ; aucune branche
  `donnees/*` ni `quarantaine/*`.
- Machine : `bwrap` 0.9.0 installé, noyau Linux 6.18.44, Python 3.13.17, noyau du pôle lancé en **superutilisateur** (comme
  probablement dans le conteneur de session-depot).
- Aucun appel payant, aucune clé : chaque essai a tourné sous `env -i` (clé factice seulement) ; la suite complète et l'étage
  rejoué ont tourné en plus dans un espace réseau isolé (`bwrap --unshare-net`). Faux kit, faux adaptateurs ; adaptateurs réels
  refusés avant tout import du kit (lu dans `essais/test_adaptateurs.py` et `essais/test_v6_monde_noyau.py`).
- Cibles : toutes factices, dans le bloc-notes de la session. Seul témoin hors de ce dossier : un fichier
  `/usr/lib/cl14-<16 hexadécimaux au hasard>.txt`, **tenté** depuis le bac à sable après les remontages ; il n'a jamais été créé
  (vérifié par l'hôte après chaque sonde ; `ls /usr/lib/cl14-*` : aucun fichier). Les écritures dans `/proc/sys` globaux **n'ont
  pas été faites** : seules des ouvertures en écriture sans écriture, et une écriture dans le nom d'hôte de l'espace UTS **du bac
  seul**. Aucun processus de sonde survivant ; rien laissé sur l'hôte.

## Empreintes vérifiées

| fichier | empreinte SHA-256 | vérification |
|---|---|---|
| `EMPREINTES-orchestrateur-pole-v7-v49.txt` | `6bfb03fab098b12ce518ea5948e71c33f998287a8c2b4fed8a38335890a4d9be` | égale à l'attendue (`6bfb03fa…`) et à son `.sha256` |
| fichiers listés par la v49 | — | `sha256sum -c` : **174 OK, 0 échec** |
| `LISEZMOI-orchestrateur-pole-v7-v49.md` | `ef999bfd54f081e2b3fdc506812c1e7ec786212b54e2d3a6046907b9245dfaed` | égale à l'attendue (`ef999bfd…`) et à son `.sha256` |
| `EMPREINTES-…-v48.txt`, `…-v47.txt`, `LISEZMOI-…-v48.md` | — | leurs `.sha256` : OK (versions précédentes intactes) |
| arbre de la v48 (commit `19cadf8c`) | — | `sha256sum -c EMPREINTES-…-v48.txt` : **172 OK** (code de la v48 récupérable) |
| table de provenance du LISEZMOI v49 (8 fichiers) | — | 8/8 empreintes v48 égales à la liste v48, 8/8 empreintes v49 égales aux fichiers |
| `/opt/argon/commande_argon_v2.py` (lu, **non exécuté**) | `6905ac71f126bfd49174ccb9e98e26e9c73367d3d9614bc2f5ada20b085df7e2` | — |

Sondes écrites pour cette contre-lecture (bloc-notes de la session, hors dépôt, non versées ; R6) :

| fichier | SHA-256 |
|---|---|
| `sonde_bac49.py` (bac à sable de la v49, réel) | `0d395b1963de65248d44403e79395b02e5fc13a26d1ccdceca9b6796ca150386` |
| `sonde_etage49.py` (étage entier, vrai `bwrap`, faux kit) | `a94dc5d284d7908b6ec0b297784f002729ae3b15d574641140758e16f8435530` |
| `scan_proc.py` (ouvertures en écriture dans `/proc`, sans écriture) | `402e11cde7797756aeed16cace4d620fdab99476f3209235384072221776767c` |
| `correction_procsys.py` (essai de la correction de CL14-01) | `b30a012c9f9f26d31e06cd9d3ca81ec5621615c77609c26587b7bf58d7a1a387` |
| `essais49.log` (journal de la suite complète) | `91bb45e94c7d654446f40c847855d663130cf98bbd0b8f6abb02178c8c6ea7bb` |

## Verdicts

- **v49 sans l'étage (`--tests-de-mort 0`) : lançable en l'état**, à une condition de lancement : l'étiquette du modèle d'Argon
  doit être exactement `gemini-4-argon` (CL14-07) ; sinon la course s'arrête au premier appel d'Argon. Elle ferme sans repli.
- **Étage de tests de mort (`--tests-de-mort ≥ 1`) : lançable après corrections.** **CL14-01 bloque** : depuis le bac à sable,
  le script peut ouvrir en écriture 528 réglages globaux du noyau Linux, dont `kernel.core_pattern`. La voie mène à
  l'exécution de code en superutilisateur de l'hôte. Ne pas lancer l'étage avant CL14-01, CL14-02 et un nouveau passage des
  sondes. Argon expérimentateur : non fonctionnel avec la commande réelle (CL14-07).

Les quatre évasions de CL13 sont **bloquées** dans le vrai bac (rejouées ci-dessous). La correction proposée par CL13
(`--unshare-user --uid 65534 --cap-drop ALL`) laisse toutefois au script l'identité **superutilisateur de l'hôte** (uid 0 côté
hôte), d'où CL14-01 et CL14-02.

## Comptes d'essais

- Suite complète de la v49 (`python3 -B -m unittest discover -t . -s essais -p 'test_*.py'`, `env -i`, réseau isolé) :
  **485 essais, 485 OK, 0 échec, 0 ignoré** (`Ran 485 tests in 286.604s — OK`). L'auteur annonçait 483 OK et 2 ignorés : ici
  `bwrap` est présent, donc **les deux essais réels sont joués et passent** (`test_v48_22` et `test_v49_19`, aussi en mode
  détaillé, `Ran 2 tests in 6.513s — OK`).
- **Ce que prouvent les deux essais réels.** Contrairement à `test_v48_22` en v48, ils jouent l'étage entier avec le vrai bac :
  identité 65534, remontage et écriture de la tranche refusés, racine en lecture seule, réseau isolé. Essai par mutation : en
  retirant `--unshare-user --uid --gid --cap-drop ALL` de `commande()` (la commande de la v48), **les deux échouent**
  (`test_v48_22` FAIL : « le script est superutilisateur » ; `test_v49_19` ERROR : étage refusé par la sonde). Ils prouvent donc
  le confinement **pour ce qu'ils jouent**. Ils ne jouent ni `/proc/sys`, ni les espaces d'utilisateurs imbriqués, ni `/usr`,
  ni la borne du nombre de processus. Les essais des liens, du tube et de la prise (`test_v49_06`, `_07`) passent par
  l'exécuteur **factice** : je les ai rejoués avec le vrai `bwrap` (critère 1).

## Critère 1 — artefacts rejoués sous le vrai `bwrap`, contre la v49

Commandes : `env -i PATH=/usr/bin:/bin HOME=<bloc-notes> LANG=C.UTF-8 python3 -I -B sonde_bac49.py <arbre v49> <dossier> <nom>`
(exécuteur `ExecuteurBacASable` de la v49, inchangé) ; étage : `env -i … bwrap --dev-bind / / --unshare-net -- python3 -B
sonde_etage49.py <arbre v49>` (faux kit, vrai bac, clé factice `CLE_FACTICE_DU_NOYAU` chez le noyau).

| artefact | sortie avec la v49 | bloqué ? |
|---|---|---|
| identité, capacités | `Uid 65534`, `CapEff/CapPrm/CapBnd = 0`, `NoNewPrivs 1`, `Seccomp 0`, **`uid_map 65534 0 1`** (65534 du bac = **0 de l'hôte**) | oui (voir CL14-01, 02) |
| CL13-01 remontage de `/usr`, `/`, tranche | `remonter /usr rw : Operation not permitted` ; idem `/`, tranche ; `ecrire /usr apres : Read-only file system` ; `demonter /usr : errno 1` ; témoin `/usr/lib/cl14-…` présent sur l'hôte : **False** | **oui** |
| espace d'utilisateurs **imbriqué** (`unshare(NEWUSER\|NEWNS)` puis remontages) | `unshare : REUSSI`, `CapEff imbrique 000001ffffffffff` ; remontage de `/usr` et de la tranche : `Operation not permitted` (montages verrouillés) ; démontage de la tranche : `errno 22` ; écriture `/usr`, tranche : refusées ; `tmpfs neuf : REUSSI` (dans son propre espace) | oui pour le système de fichiers ; surface d'attaque ouverte (CL14-03) |
| CL13-02 lien posé sur `script.py` (étage complet) | fichier factice de l'hôte après l'étage : `"CONTENU ORIGINAL DE L'HOTE"` ; exécutions `('réussie', [lien script.py « non copié : lien vers … »]), ('réussie', [])` | **oui** |
| CL13-03 liens vers `/proc/self/environ`, `/proc/1/environ`, secret factice de l'hôte | produits `['ok-dur.txt', 'ok.txt']` ; non copiés : `environ.txt`, `environ1.txt`, `secret.txt` (lien), `tuyau` (tube nommé) ; canari de la clé factice dans la sortie : **False** ; secret : **False** | **oui** (reste CL14-04) |
| CL13-04 tube nommé | étage terminé en ~26 s pour 42 essais, aucun blocage ; tube consigné « tube nommé » | **oui** |
| lien matériel vers la tranche, vers `python3` | `Invalid cross-device link` (×2) | oui |
| `mknod` | `Operation not permitted` | oui |
| `/proc/sys` (ouverture en écriture, **sans écrire**) | `w /proc/sys/kernel/core_pattern : OUVERT EN ECRITURE` ; `fs/suid_dumpable`, `kernel/randomize_va_space`, `vm/drop_caches` : ouverts ; **528 fichiers de `/proc/sys` ouvrables en écriture** ; `sethostname()` : `errno 1` mais écriture de `/proc/sys/kernel/hostname` : **ÉCRIT** (espace UTS du bac) | **NON** — CL14-01 |
| setuid, propriétaire | `chmod 4755` réussi ; **côté hôte : propriétaire 0, mode `0o104755`** ; `chmod /travail 0777` réussi (hôte : `0o40777`) ; `chown` refusé | **NON** — CL14-02 |
| 1 100 processus (`fork` ×1100, `RLIMIT_NPROC` = 1024) | `enfants crees 1100, arret null` | **NON** — CL14-02 |
| survie au délai (`setsid` + double `fork`, délai 5 s) | `code -9, delai_depasse True` ; processus survivants sur l'hôte : `[]` | oui |
| place du dossier de travail (12 × 50 Mo en rafale) | tué à 0,5 s, « plus de 268435456 octets » ; 271 Mo sur l'hôte | oui (borne franchie de ~6 %) |
| sous-dossier fermé (mode 000) de 300 Mo | tué, 291 Mo, vu par l'inventaire (noyau superutilisateur) | oui ici (voir CL14-12) |
| `/dev/shm` (6 × 50 Mo) | `Mo dans /dev/shm : 300`, aucune borne franchie, exécution réussie | **NON** — CL14-10 |
| noms piégés : `r.txt` et `r.txt.sha256` produits | **course interrompue** : `EcrasementInterdit …/execution-01/produits/r.txt.sha256` | **NON** — CL14-05 |
| `/proc/1/environ` du bac | `PATH=/usr/bin:/bin HOME=<chemin de l'hôte>…` : environnement minimal, aucune clé | oui |
| trousseau de clés `@u` | identifiant ≠ celui de l'hôte (espace d'utilisateurs propre) | oui |
| réseau | sonde du noyau : connexion refusée ; pas de `/sys` | oui |

## Constats

### CL14-01 — `/proc/sys` inscriptible depuis le bac : l'identité du script est le superutilisateur de l'hôte

- **Gravité : critique** (bloque l'étage). Voie vers l'exécution de code en superutilisateur sur l'hôte.
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 831-838 (`ExecuteurBacASable.commande`, `--proc /proc` l. 836) ; sonde
  l. 917-1028 (rien sur `/proc/sys`).
- **Défaut** : le noyau lance `bwrap` en superutilisateur. `--unshare-user --uid 65534` place le script dans un espace
  d'utilisateurs où son identité 65534 correspond à **l'identité 0 de l'hôte** (`uid_map 65534 0 1`). Les droits d'écriture
  des réglages `/proc/sys` se jugent sur cette identité de l'hôte, pas sur les capacités (`sethostname()` est refusé,
  l'écriture du même réglage par `/proc/sys` passe). `bwrap` 0.9.0 ne couvre pas `/proc/sys` en lecture seule. Il ne le couvre
  que si le dossier est inscriptible au montage, or le dossier racine de `/proc/sys` refuse toujours l'écriture. Les montages
  du bac le confirment : `/proc rw`, `/proc/irq ro`, `/proc/bus ro`, rien pour `/proc/sys`. Le script peut donc ouvrir en écriture
  `kernel.core_pattern`. Le chemin de l'hôte de son dossier de travail lui est donné par `/proc/self/mountinfo`. Il pourrait
  écrire `|<chemin de l'hôte>/travail/x` puis provoquer un plantage : le noyau Linux exécuterait `x` en superutilisateur, hors
  de tout espace de noms. Défaut présent aussi en v48 ; la correction proposée par CL13 ne le fermait pas.
- **Essai** (sonde `sysctl`, puis `scan_proc.py`, puis l'étage entier) :
  ```
  "sethostname() (appel systeme, exige CAP_SYS_ADMIN)": "errno 1",
  "ecrire /proc/sys/kernel/hostname (espace UTS du bac seulement)": "ECRIT", "hostname apres": "cl14-par-proc-sys",
  "w /proc/sys/kernel/core_pattern": "OUVERT EN ECRITURE (rien ecrit)", "w /proc/sys/fs/suid_dumpable": "OUVERT EN ECRITURE …",
  "montage /proc/sys": ["/proc rw,…", "/proc/irq ro,…", "/proc/bus ro,…"]
  fichiers de /proc/sys ouvrables en écriture : 528
  (étage complet, vrai bwrap) CL14 /proc/sys dans l'étage : réussie ; sonde : True ; stdout scellé : core_pattern ouvert en écriture (rien écrit)
  ```
  Hôte inchangé : `hostname` = `vm`, `core_pattern` = `core` avant et après. **L'écriture globale n'a pas été jouée** : elle
  modifierait l'hôte. L'ouverture en écriture et l'écriture du nom d'hôte du bac montrent que seule l'identité est contrôlée.
  Pour les réglages globaux, ce contrôle est le même. La sonde `disponible()` passe ; `test_v48_22` et `test_v49_19` aussi.
- **Correction** (essayée ici, `correction_procsys.py`) : dans `commande`, juste après `--proc /proc`, ajouter
  `--ro-bind /proc/sys /proc/sys`. Sortie de la variante corrigée : `core_pattern`, `hostname`, `drop_caches` refusés
  (`Read-only file system`) ; le script tourne (code 0) ; `disponible()` → `(True, '… sonde OK …')`. Ajouter à
  `SONDE_PRIVILEGES` un artefact : ouvrir `/proc/sys/kernel/core_pattern` en écriture doit échouer. Ajouter aussi
  l'identité de l'hôte lue dans `/proc/self/uid_map`, consignée et refusée si elle vaut 0. Mieux, et à éprouver dans le
  conteneur réel : lancer `bwrap` sous un **utilisateur dédié sans privilège de l'hôte** (par exemple
  `setpriv --reuid U --regid U --clear-groups`, dossier de travail à lui). Cela ferme d'un coup CL14-01, CL14-02 et la borne de
  processus. Je n'ai pas pu l'éprouver : le bloc-notes n'est pas traversable par un autre utilisateur.

### CL14-02 — Script = superutilisateur de l'hôte : fichiers setuid-root dans la sortie, borne de processus inopérante

- **Gravité : haute.**
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 114 (`PROCESSUS_MAX_DEFAUT`), l. 840-849 (`_limites`, `RLIMIT_NPROC`),
  l. 792-799 (`description()` annonce `processus_max: 1024`) ; l. 1547-1548 (dossier de travail laissé dans `SORTIE`).
- **Défaut** : même cause que CL14-01. (a) Le script crée dans son dossier de travail des fichiers qui, **sur l'hôte**,
  appartiennent au superutilisateur avec le bit setuid. Un exécutable binaire écrit en octets par le script serait un
  setuid-root qui reste dans la sortie scellée (CL14-04). Aujourd'hui `execution-NN` est en mode 0700, donc hors d'atteinte. Mais
  toute copie qui garde les modes (`cp -a`, `tar`, lot zippé) l'expose, par exemple à l'utilisateur distinct `argon` de la même
  machine. (b) `RLIMIT_NPROC` ne s'applique pas à l'identité 0 de l'hôte : 1 100 processus créés malgré la borne de 1 024.
  Une bombe à processus épuise les numéros de processus de l'hôte (32 768) et sa mémoire (1 Go par processus) pendant tout le
  délai (120 s par défaut). Le relais et le noyau sont alors touchés. Le manifeste annonce pourtant `processus_max: 1024`.
- **Essai** : sonde `fichiers` → `hote : suid proprietaire 0 mode 0o104755`, `hote : travail proprietaire 0 mode 0o40777` ;
  sonde `processus` → `{"enfants crees": 1100, "arret": null, "RLIMIT_NPROC": [1024, 1024]}`, aucun survivant après la fin.
- **Correction** : utilisateur dédié sans privilège (CL14-01) ; à défaut, une borne de processus par groupe de contrôle
  (`pids.max`, par exemple `systemd-run --scope -p TasksMax=…` si disponible) et, côté noyau, retrait des bits setuid et setgid
  (ou du dossier de travail, CL14-04) après l'inventaire. Dire au manifeste « borne de processus inopérante » tant qu'elle l'est.

### CL14-03 — Espaces d'utilisateurs imbriqués permis dans le bac

- **Gravité : moyenne** (aucune évasion constatée : les montages hérités sont verrouillés ; mais toutes les capacités dans un
  espace imbriqué, donc une grande surface du noyau Linux exposée à un script écrit par un modèle).
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 831-832 (pas de `--disable-userns`) ; LISEZMOI v49, « non ajoutés ».
- **Essai** : sonde `imbrique` → `"unshare user+mnt": "REUSSI"`, `"CapEff imbrique": "000001ffffffffff"`, `"tmpfs neuf": "REUSSI"`,
  remontages refusés.
- **Correction** (essayée ici, variante `CORRIGE=1` de `sonde_bac49.py`) : `--disable-userns` avant `--cap-drop ALL` →
  `"unshare user+mnt": "errno 28"` ; le script tourne. Artefact de sonde : `unshare(CLONE_NEWUSER)` doit échouer. Un filtre
  d'appels système (`--seccomp`) reste à envisager.

### CL14-04 — Le dossier de travail entier reste dans la sortie scellée : liens vers `/proc/self/environ`, tubes, gros fichiers

- **Gravité : moyenne.**
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 1545-1560 (`execution-NN/travail` créé dans `SORTIE`, jamais retiré).
- **Défaut** : le noyau ne suit plus rien (CL13-03 tient). Mais tout ce que le script a laissé reste sous
  `SORTIE/noyau/tests-de-mort/<fiche>/execution-NN/travail/`, hors de tout sceau : liens vers `/proc/self/environ`,
  `/proc/1/environ` ou un chemin de l'hôte, tubes nommés, prises, fichiers setuid (CL14-02). On y trouve aussi jusqu'à
  ~290 Mo par exécution (soit jusqu'à ~10 Go pour 12 fiches × 3 exécutions) et une copie de la tranche par exécution. Un outil
  d'aval qui suit les liens copierait l'environnement **de l'opérateur**, clés comprises : `zip -r` (suit les liens par défaut),
  `cp -rL`, `tar -h`, un `sha256sum` sur tous les fichiers. Un tube bloque un hachage naïf de l'arbre. La sortie est prévue
  pour être versée au dépôt.
- **Essai** (étage, vrai `bwrap`) : `ce qui reste dans SORTIE/…/execution-01/travail : [('environ.txt', '0o120777'),
  ('environ1.txt', '0o120777'), ('ok-dur.txt', …), ('ok.txt', …), ('script.py', …), ('secret.txt', '0o120777'),
  ('tranche', '0o40700'), ('tuyau', '0o10644')]` ; sondes `rafale` et `cache` : 271 et 291 Mo laissés.
- **Correction** : après l'inventaire et la copie des produits, retirer `travail` (`shutil.rmtree`, qui ne suit pas les liens
  sous Linux). L'inventaire scellé (`resultat.json`) garde les noms, genres, cibles et empreintes. À défaut, déplacer le dossier
  hors de `SORTIE`. Ajouter un essai : aucun lien, tube ni prise sous `SORTIE` après l'étage.

### CL14-05 — Un produit nommé `<x>.sha256` à côté de `<x>` interrompt tout l'étage

- **Gravité : moyenne** (aucune évasion ; mais un script fait tomber l'étage, et toutes les fiches suivantes restent sans test).
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 1568-1574 (`ecrire_scelle(os.path.join(d_exec, "produits", p), …)` écrit
  `p` puis `p.sha256` ; le produit suivant `p.sha256` lève `EcrasementInterdit`).
- **Essai** (étage à deux fiches, vrai `bwrap`, script `open('r.txt','w').write('x'); open('r.txt.sha256','w').write('y')`) :
  `course interrompue : EcrasementInterdit …/execution-01/produits/r.txt.sha256` ; arrêt consigné au manifeste de l'étage.
  L'arrêt est propre et dit (R5 tenu), mais la deuxième fiche n'est pas jouée.
- **Correction** : copier les produits sous un nom échappé ou dans un arbre où le noyau n'écrit pas de compagnon, ou consigner
  « non copié : nom réservé » pour tout nom en `.sha256` ; essai correspondant.

### CL14-06 — CL13-11 : l'arrondi admis fait franchir le seuil, et l'étiquette dit « recalculé par le noyau »

- **Gravité : moyenne** (R4 : faux « survit » étiqueté comme vérifié).
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 434-475 (`_tolerance_d_affichage`, `recalcul_noyau`) ; l. 1617-1641 (le
  verdict reste celui du chiffre **imprimé**).
- **Défaut** : la tolérance vaut la moitié de la dernière décimale imprimée. Le verdict se prend sur le chiffre imprimé, pas
  sur celui du noyau. Un script qui imprime `0.5` pour une moyenne réelle de 0,45, au seuil « au moins 0,5 », est
  « concordant », donc « survit ». La vraie valeur élimine la fiche. Autre point : « recalculé » vérifie la statistique
  **déclarée par le script**, pas qu'elle soit le test gelé.
- **Essai** (fonctions de la v49) :
  ```
  imprimé 0.5  -> verdict survit   | recalcul concordant 0.45 | étiquette : survit (chiffre recalculé par le noyau)
  imprimé 0.45 -> verdict éliminée | recalcul concordant 0.45 | étiquette : éliminée (chiffre recalculé par le noyau)
  ```
- **Correction** : quand le recalcul est concordant, appliquer le seuil à `valeur_noyau`. Si les deux verdicts diffèrent, le
  résultat est « non concluant ». Étiquette « statistique déclarée par le script, recalculée par le noyau ». Essai au bord du
  seuil.

### CL14-07 — Argon : contrat compatible pour proposeur et juge, mais expérimentateur impossible avec la commande réelle ; LISEZMOI inexact

- **Gravité : moyenne** (ferme sans repli : arrêt au premier tour, coût plancher 1e-6 USD ; mais la fonction annoncée ne marche pas).
- **Fichiers et lignes** : `/opt/argon/commande_argon_v2.py` l. 127 (`ROLES = ("proposeur_ideation", "juge_ideation")`), l. 329-331
  (refus de tout autre `ROLE_POLE`, code 2), l. 290 et 404 (`modele_servi` déjà rendu, depuis `modelVersion`), l. 265 (modèle pris
  dans `--modele`, défaut `gemini-4-argon`) ; `/opt/argon/appel-argon-v3.sh` (ne passe pas `--modele`) ; `pole/adaptateurs.py`
  l. 610 (`ROLES_PERMIS` ouvert à l'étage), l. 631-647 (`MODELE_DEMANDE_POLE`) ; LISEZMOI v49 l. 88.
- **Constat** : (a) **contrôlé pour Argon proposeur et juge** : avec le moteur réel, `exiger_modele_servi=True`
  (`demonstrations/ideation_v1.py` l. 669-677), et la ligne JSON de la commande v2 porte `modele_servi`. Le contrat est donc déjà
  tenu. Le LISEZMOI se trompe quand il écrit « elle ne rend pas encore `modele_servi` ». (b) La commande ignore
  `MODELE_DEMANDE_POLE` et demande toujours `gemini-4-argon` : si l'étiquette donnée au noyau diffère (les essais utilisent
  `gemini-argon`), la course s'arrête au premier appel. (c) **Expérimentateur de l'étage** : `ROLE_POLE=experimentateur_test`
  est refusé par la commande (code 2). Le noyau reçoit une erreur et l'étage s'arrête au premier tour. **Pour l'étage**, le
  modèle servi est contrôlé pour l'expérimentateur et le lecteur Claude (kit et `controle_modele_resultat`, l. 1399-1428 de
  `tests_de_mort.py`). Pour Argon expérimentateur, il n'y a rien à contrôler, faute de session possible.
- **Essai** :
  ```
  ligne de la commande Argon v2, modèle demandé au noyau gemini-4-argon -> None   (accepté)
  idem, étiquette des essais gemini-argon -> modèle servi 'gemini-4-argon' ≠ modèle demandé 'gemini-argon' : changement de modèle par la commande
  environnement passé : {…, 'ROLE_POLE': 'experimentateur_test', 'MODELE_DEMANDE_POLE': 'gemini-4-argon'}  ;  commande : ROLES = ("proposeur_ideation", "juge_ideation")
  ```
- **Correction** : corriger le LISEZMOI ; condition de lancement « étiquette d'Argon = `gemini-4-argon` », vérifiée par le lanceur
  ou lue dans la commande ; refuser `--experimentateur-externe` au lanceur tant qu'aucune commande d'Argon n'accepte
  `experimentateur_test` (une v3 de la commande, côté session-depot, avec un nouveau nom selon R12) ; faire lire
  `MODELE_DEMANDE_POLE` par la commande, ou le retirer.

### CL14-08 — « Suffixe de date » : le code admet tout suffixe

- **Gravité : mineure** (antérieure à la v49, dans le noyau comme dans la commande d'Argon).
- **Fichier et ligne** : `pole/adaptateurs.py` l. 361-369 (`servi.startswith(demande + "-")`) ; commande d'Argon l. 226-228.
- **Essai** : `'gemini-4-argon' servi 'gemini-4-argon-lite' -> conforme True` ; `'claude-opus-5-5' servi 'claude-opus-5-5-mini' ->
  conforme True` ; `'gemini-4-argon' servi 'models/gemini-4-argon' -> conforme False` (la commande l'accepte, le noyau non).
- **Correction** : suffixe borné (`-\d{8}` pour Claude ; liste explicite des identifiants servis permis pour Argon) ; aligner le
  noyau et la commande.

### CL14-09 — Écart de modèle vu par la commande d'Argon : rangé en « erreur », pas en « refus »

- **Gravité : mineure** (la course s'arrête quand même).
- **Fichier et ligne** : `pole/adaptateurs.py` l. 728-744 : `controle_modele` n'est appliqué que si le code est 0 ; la commande
  rend le code 5 quand elle voit elle-même un autre modèle (l. 239-241 de la commande), avec `modele_servi` dans la ligne.
- **Défaut** : pas de statut « refus », pas de `depense_modele_non_autorise_usd`, sortie non mise à l'écart (R-764).
- **Correction** : appliquer `controle_modele` à la dernière ligne lisible aussi sur un code non nul.

### CL14-10 — `/dev/shm` sans borne

- **Gravité : mineure** (mémoire de l'hôte, éphémère, pendant le délai ; non surveillé).
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 836 (`--dev /dev`).
- **Essai** : sonde `shm` → `{"Mo dans /dev/shm": 300}`, exécution réussie, aucune borne franchie.
- **Correction** : `--size <octets> --tmpfs /dev/shm` après `--dev /dev` (`bwrap` 0.9 : disponible ici), ou borne mémoire par
  groupe de contrôle.

### CL14-11 — Sonde et essais réels : artefacts manquants

- **Gravité : mineure** (c'est ce qui laisse passer CL14-01 à 03 ; R5).
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 974-1028 ; `essais/test_v7_ideation.py` l. 6715-6760, 7799-7845.
- **Défaut** : ni la sonde ni les essais réels ne jouent `/proc/sys`, l'identité de l'hôte (`uid_map`), un espace d'utilisateurs
  imbriqué, `/usr`, la borne de processus, `/dev/shm`, les noms `.sha256`. Les essais des liens et du tube (`test_v49_06`, `_07`)
  ne passent que par l'exécuteur factice. `CapBnd` est imprimé par la sonde mais non vérifié.
- **Correction** : ajouter ces artefacts à la sonde (refus de l'étage si l'un réussit) et à `test_v49_19` ; jouer
  `test_v49_06` et `_07` aussi avec le vrai bac quand `bwrap` est présent (les sondes `sonde_etage49.py` peuvent servir).

### CL14-12 — Noyau non superutilisateur : un sous-dossier fermé échappe à la borne et à l'inventaire (lu, non joué)

- **Gravité : mineure** (sans objet quand le noyau tourne en superutilisateur, comme ici).
- **Fichier et ligne** : `pole/tests_de_mort.py` l. 689-692 et 701-704 (`except OSError: continue`).
- **Défaut** : si le noyau n'est pas superutilisateur, l'identité du bac correspond à la sienne. Le script peut alors rendre un
  sous-dossier illisible (mode 000) : son contenu échappe à la surveillance de place et à l'inventaire, sans motif consigné.
- **Correction** : un dossier illisible compte comme dépassement (« dossier illisible : non parcouru »), jamais ignoré en silence.

## Critères 2 à 6

- **Critère 2** : 485/485 OK, 0 ignoré ; les deux essais à `bwrap` sont joués. Ils prouvent le confinement pour ce qu'ils
  jouent : l'essai par mutation les fait échouer tous deux. Ils ne couvrent pas CL14-01 à 03 (CL14-11).
- **Critère 3** : voir CL14-07 à 09. Claude (course et étage) : barrières du kit, du message de résultat (CL13-06 traité,
  l. 512-530), du noyau (`controle_modele_resultat`) et du relais. La forme réelle de `model_usage` reste SUPPOSÉE (dit par
  l'auteur). Argon proposeur et juge : contrôlé, contrat compatible avec `commande_argon_v2.py` si l'étiquette vaut
  `gemini-4-argon`. Argon expérimentateur : impossible avec la commande réelle.
- **Critère 4, CL13-06 à 12** : 06 traité (lu ; `test_v49_11` OK). 07 traité (`modeles_du_relais`, `ideation_v1.py`
  l. 680-692 ; `test_v49_12` OK). 08 traité en partie (CL14-11). 09 traité (compteur persistant scellé, démarrage refusé sur
  sceau faux, arXiv en https, `--dossier-compteur` obligatoire avec l'amont réel ; `test_v49_13`, `_14` OK ; lu : deux relais
  sur le même dossier écriraient chacun leur compte, plafond doublé, à éviter à l'opérateur). 10 traité (dit au LISEZMOI, table
  vérifiée 8/8, v48 récupérable 172/172). 11 traité avec défaut (CL14-06). 12 traité en partie : la surveillance de place tue bien
  (rejoué, 271 et 291 Mo) ; borne de processus inopérante (CL14-02) ; `/dev/shm` (CL14-10).
- **Critère 5** : **rétrocompatibilité** sans `--tests-de-mort` : `test_v48_11` passe, et ses empreintes gelées de la v47
  (`SORTIES_V47_SHA256`, `CONSIGNES_V47_SHA256`, `REGLAGES_KIT_V47_SHA256`) sont **identiques** entre les arbres v48 et v49 (diff
  vide). Elles n'ont donc pas été ajustées. Changement voulu en réel : Argon doit rendre `modele_servi` (CL14-07). **R12** : huit
  modules de code écrasés en place (`sha256sum -c` de la liste v48 sur l'arbre v49 : 8 échecs). C'est dit, avec une table de
  provenance exacte ; LISEZMOI et EMPREINTES v1 à v48 intacts. **Garde de dépense** : `ideation.py` ne change que par le contrôle
  du modèle servi (6 lignes) et le lanceur que par `modeles_du_relais` et `adaptateur_commande_externe`. La somme des plafonds
  et les plafonds par session sont inchangés. Une session en écart de modèle est comptée en entier à part. Aucun contournement
  trouvé ; aucun lancement réel fait.
- **Critère 6** : défauts nouveaux, de CL14-01 à CL14-12 ; nouveaux par rapport à CL13 : CL14-01 à 07, 09 à 12 (CL14-08 est
  antérieur).

## Récapitulatif par gravité

| gravité | constats |
|---|---|
| critique | CL14-01 (`/proc/sys` inscriptible : `core_pattern`, voie vers le superutilisateur de l'hôte) |
| haute | CL14-02 (identité 0 de l'hôte : setuid-root dans la sortie, borne de processus inopérante) |
| moyenne | CL14-03 (espaces imbriqués), CL14-04 (dossier de travail laissé dans `SORTIE`), CL14-05 (`.sha256` interrompt l'étage), CL14-06 (arrondi : faux « survit » recalculé), CL14-07 (Argon expérimentateur impossible, LISEZMOI inexact) |
| mineure | CL14-08, CL14-09, CL14-10, CL14-11, CL14-12 |

Ordre conseillé : CL14-01 et 02 (une même cause : lancer `bwrap` sous un utilisateur sans privilège, ou au moins lier
`/proc/sys` en lecture seule et borner les processus), CL14-03, 04, 05, 11, puis rejouer `sonde_bac49.py` et `sonde_etage49.py`
dans le conteneur de session-depot avant tout GO de l'étage.
