# Contre-lecture n° 6 (R2) — préenregistrement « gradient conçu par l'essaim », étape 1 (sondes) — v6 « économe »

- **Relecteur neuf (R2).** Je n'ai écrit ni le préenregistrement (v1 à v6), ni le code, ni les lanceurs, ni aucune
  contre-lecture ou revérification précédente. Contre-lecture **limitée** aux corrections annoncées pour CL5-01 à CL5-12
  et à ce que ces corrections touchent. Je n'ai pas refait les contre-lectures n° 4 et n° 5 ni la revérification du code.
- **Heure (UTC, `date -u`)** : début 02:53, fin 03:21.
- **Texte relu : `gradient-etape1-sondes-v6.md`, SHA-256 `ce78d5e59e3ae8e29b998f272d10a65c42765e32d45b6c9c3dc5180dd5b45c4e`**
  (compagnon `.sha256` : OK ; = la valeur citée par la tâche ; marqueurs de scellement non remplis).
- **Pièces.** `EMPREINTES-pieces.txt` vérifié : **164 sur 164 OK** (`sha256sum -c`). Relus : la v6, la v5 (`d7cf7746…`),
  le rapport n° 5 (`53e6527c…`, liste CL5-01 à CL5-12), le diff `44cd936..224de13`, l'arbre du code au commit
  `224de13`, le collisionneur v2.5, le lanceur v4, ses essais et leurs deux sorties, le banc de mutations CL5 et sa
  sortie, le script de scellement `sceller_etape1_v6.py`, le validateur `prereg.py`, le gabarit, `CLAUDE.md`.
- **Code des pièces = commit cité (fichiers changés).** Empreintes recalculées, concordantes :
  `essaim_m3/analyse_gradient.py` `4b54d380…`, `essaim_m3/noyau/bac_a_sable.py` `8f52ec88…`, arbre du noyau
  (`boucle.empreinte_arbre`) `f43946a3…`.

## VERDICT : **non scellable** — 1 bloquante, 1 majeure (bloquante pour l'exécution), 1 mineure, 2 de forme.

Deux obstacles distincts : (CL6-01) le script `sceller_etape1_v6.py` **refuse de sceller ce texte** (incohérence
« lanceur v3 corrigé » / « lanceur v4 ») ; (CL6-02) la correction CL5-02 introduit une régression qui **empêche tout
organisme de tourner** dès qu'un dossier inscriptible par tous est imbriqué sous un dossier temporaire — ce qui est le
cas sur l'hôte recommandé en l'état, où `test_cl5_01` et `test_cl5_02` échouent. Le fond des corrections CL5-01 à CL5-12
est par ailleurs juste et éprouvé ; les deux défauts sont des oublis de petite taille mais bloquants.

---

## Tableau de suivi CL5-01 à CL5-12

| remarque | état | preuve |
|---|---|---|
| CL5-01 (bloquante) test final lisible sur l'hôte | **traitée** (fond) | Code : `bac_a_sable.dossiers_a_cacher` recouvre dépôt/objets git/arbre du code (`ESSAIM_M3_CACHER`, mis par le lanceur l.262) et `/home,/root,/srv,/mnt,/media` d'un tmpfs **vide en lecture seule** (mode 0000, `MS_RDONLY`). `test_cl5_01` passe (en isolé). Rejoué (`sortie-cl6-defaut-et-isolation.txt`, logique) : un secret sous `ESSAIM_M3_CACHER` → `PermissionError` ; `/home` et `/root` → `PermissionError`, `/home/user` absent dans le bac ; le fichier du dossier de travail reste lisible ; l'organisme tourne (code OK) ; aucune fuite du marqueur. **Mais l'organisme ne tourne que si CL6-02 est corrigé** (sinon `SANS_STATUT`). |
| CL5-02 (majeure) voie commune par un dossier inscriptible par tous | **traitée au fond, mais la correction introduit un défaut (CL6-02)** | Code : `dossiers_inscriptibles_par_tous` balaie `/` une fois ; `dossiers_tmp_a_rendre_prives` l'utilise. Rejoué : un dossier 1777 hors des quatre (sous `/var/lib`) est trouvé par le balayage et mis dans `tmp_prives` ; A y écrit, B lit `FileNotFoundError`, rien n'atteint l'hôte. **Mais** la boucle de montage `prives` abandonne sur un dossier imbriqué → **CL6-02**. |
| CL5-03 (majeure) amorçage de Fable refusé à 3 USD | **traitée** | Lanceur v4 : répétition `--usd-par-generation 5 --plafond-total 40` (essai `sain-repetition`, 53/53). `test_cl5_03` passe (5 USD → `ORGANISME_VALIDE`, 3 USD → `AMORCAGE_PLAFOND`). Pire cas recalculé par `cv.cout_pire_cas` du collisionneur cité : Fable **3,40 USD** (prompt 60 000 car., 64 000 jetons), 3,27 à 20 000 ; Opus 1,36 ; Argon 1,80 ; < 5 (passe), > 3 (refusé). La répétition-B à 3 USD ne réintroduit rien (bras `--depuis` = `organismes_imposes`, `cout_usd=0.0`, aucun amorçage par appel : `boucle.amorcer` l.546-559). |
| CL5-04 `lire_h_g1` sans essai ; `exclues` sans audit | **traitée** | Code : `lire_h_g1` lève `ValueError` si `exclues and apres_audit != "defaut_paires"`. `test_cl5_04` passe ; mutation `cl5-04-exclues` fait échouer l'essai. |
| CL5-05 traitements sans essai | **traitée** | `test_cl5_05` couvre RV-13 (traits 0600, demandes `INDISPONIBLE` comptées par service), CE4-10 c (recoupements de fuite comptés en conception) ; passe ; RV-15 « délais par opération » au Plan, point 4 (l.347-349). (RV-16 « tirage à trois niveaux » : pas d'essai dédié nouveau ; le bootstrap est exercé par `test_cl5_04` et `test_h_g1…` — non rejoué en détail.) |
| CL5-06 gardes du lanceur sans essai | **traitée comme annoncé** | 53 essais du lanceur rejoués (53/53) : couvrent `unshare -n`, `protected_hardlinks`, non-root, autre hôte, portes ; les l.73-74 d'hôte restent masquées par le faux `unshare`, dit. |
| CL5-07 crédit/clé/certificat mal classés | **traitée** | Code : `_MOTIF_COMPTE` (crédit, quota, facturation, clé invalide) extérieur **quel que soit le code** ; `_MOTIF_RESEAU` ajoute `SSLCertVerificationError`/`CERTIFICATE_VERIFY_FAILED`. Assertions dans `test_h_g1_couverture…` passent ; mutation `cl5-07-compte` fait échouer l'essai. |
| CL5-08 « état au scellement » contredit | **en partie → CL6-03** | Le paragraphe « État au scellement » (l.304-306) écrit l'état observé (noms définis), mais la clause l.299-300 affirme encore le contraire (Brave absente). Contradiction interne. |
| CL5-09 épreuve de durée | **traitée** | Texte, Plan point 3 : limite dite (2 h 15 ne couvrent ni la durée d'une course ni un redémarrage) ; courses lancées **détachées**, PID consigné (l.328). |
| CL5-10 porte non passée venant de l'organisme | **traitée** | Texte, point 8 (l.395-397) : la porte ne compte que les statuts du noyau et du fournisseur ; suite écrite (décision de Lazar, addendum). Essais du lanceur (`sain-portes`, `reel-porte-*`) passent. |
| CL5-11 chiffres et renvois | **en partie → CL6-05** | 0,76 % à effectifs inégaux dit (Seuil), durées au pire avec l'attente, point 12 corrigé (amorçage hors extrait), ligne procédurale dite. **Mais** le nom de la pièce de mutation n'est pas corrigé : l.37 dit encore « mutations-rv-v2.txt » (le nom que CL5-11 disait faux), contredit par l.668. |
| CL5-12 script de scellement | **en partie → CL6-01 (bloquant) et CL6-04** | Script sous nouveau nom (R12) ; `vivier_message` exigé au texte (non vérifié par le script, mais c'est une exigence textuelle). **Mais** (a) le script ne peut pas sceller le texte (CL6-01) ; (b) la docstring n'est pas « juste » (CL6-04). |

Bilan CL5 : 8 traitées, 4 en partie (CL5-02, CL5-08, CL5-11, CL5-12), les parts non faites étant les cinq remarques CL6 ci-dessous.

---

## Remarques nouvelles

### CL6-01 — bloquante — Le script de scellement refuse de sceller le texte v6

- Fichiers : `sceller_etape1_v6.py` l.46-48 (chaîne `ancienne`), l.52-53 (chaîne `nouvelle`) ; texte v6 l.671-673.
- Défaut : la chaîne `ancienne` (ce que le script cherche dans le brouillon) et la chaîne `nouvelle` (ce qu'il inscrit)
  disent « …diff du code de `44cd936` à `224de13`, **lanceur v3 corrigé**) ». Le texte v6, à l'entrée « Contre-lecture 6 »
  (l.672), dit « …**lanceur v4**) » (le nouveau nom choisi par CL5-03, cf. l.57-63, 276, 653, 660). Donc
  `texte.count(ancienne) == 0` et le script s'arrête à la vérification de l'entrée (l.49-51) : « refus : entrée
  « Contre-lecture 6 » introuvable », code 2. **Le préenregistrement ne peut pas être scellé en l'état.** C'est la
  rencontre de deux corrections CL5 : CL5-03 (le lanceur devient « v4 » dans le texte) et CL5-12 (le script), le script
  n'ayant pas été aligné sur le nom final.
- Preuve rejouée (`sortie-cl6-scellement.txt`) : essai à blanc sur une copie du texte v6 (sha identique) et une config
  factice → « refus : entrée « Contre-lecture 6 » introuvable », code 2, **aucune sortie écrite**. Avec une copie du
  script dont `ancienne`/`nouvelle` disent « lanceur v4 », le script **passe** la vérification de l'entrée et le
  remplacement des cinq marqueurs (il ne s'arrête ensuite que sur l'import d'un `controle_ia` minimal de mon essai,
  sans rapport avec le défaut).
- Correction proposée : aux l.47 et 53 de `sceller_etape1_v6.py`, remplacer « lanceur v3 corrigé » par « lanceur v4 »
  (le texte dit « v4 » partout). Puis ré-essayer le scellement à blanc.

### CL6-02 — majeure (bloquante pour l'exécution) — La boucle `prives` abandonne sur un dossier inscriptible par tous imbriqué sous un temporaire ; aucun organisme ne tourne

- Fichiers : `bac_a_sable.py`, `ABAISSER_SOURCE`, boucle `for d in prives` (diff l.198-200 ; copie l.414-416) ;
  comparée à la boucle `caches` (diff l.203-208 ; copie l.419-424) qui, elle, tolère errno 2.
- Défaut : régression introduite par CL5-02. Avant, `dossiers_tmp_a_rendre_prives` n'itérait que les quatre dossiers
  temporaires de tête (jamais imbriqués l'un dans l'autre). Depuis CL5-02, le balayage `dossiers_inscriptibles_par_tous`
  rend **tout** dossier inscriptible par tous, y compris ceux **imbriqués sous** `/tmp`, `/var/tmp`, `/dev/shm` ou
  `/run/lock`. À l'abaissement, la liste est triée : le parent (`/tmp`) est monté d'abord (tmpfs vide), le chemin
  imbriqué **disparaît**, et `libc.mount(…)` sur ce chemin échoue avec **errno 2 (ENOENT)**. La boucle `prives` ne
  tolère pas errno 2 (contrairement à la boucle `caches`, dont le commentaire explique pourtant « un parent a déjà été
  couvert ») : elle fait `sys.exit(...)`. L'organisme ne tourne pas → `SANS_STATUT`. **Aucune course, répétition ni
  épreuve ne peut partir** sur un tel hôte. Les dossiers imbriqués inscriptibles par tous sont courants (par exemple
  `/tmp/.X11-unix` sur une machine de bureau, ou — ici — les `vartmp` laissés sous `/tmp/.../scratchpad/r2-*` par des
  relecteurs antérieurs). R5 : l'artefact « dossier imbriqué » n'est essayé par aucun essai ; `test_cl5_02` crée son
  dossier commun **sous `/var/lib`** (enfant direct, qui se monte sans erreur), donc n'exerce pas ce cas.
- Conséquence observée : sur l'hôte recommandé (ce conteneur), `test_cl5_01` et `test_cl5_02` **échouent** (dans la suite
  complète comme en isolé après pollution de `/tmp`), avec `SANS_STATUT`.
- Preuve rejouée (`sortie-cl6-defaut-et-isolation.txt`) : avec un dossier 1777 imbriqué sous `/tmp`, le code **livré**
  rend `code execution : SANS_STATUT`, `erreurs.txt : « dossier temporaire prive impossible sur /tmp/… (errno 2) »`. La
  **même** exécution sur une copie dont la boucle `prives` fait `if ctypes.get_errno()==2: continue` rend `code : OK`,
  `erreurs.txt` vide. (Sur cette copie corrigée, la logique d'isolation CL5-01/CL5-02 est par ailleurs juste : voir le
  tableau.)
- Correction proposée : dans la boucle `prives` de `ABAISSER_SOURCE`, absorber errno 2 comme le fait la boucle `caches`
  (`if ctypes.get_errno()==2: continue`) — ou, mieux, écarter d'emblée de `prives` tout chemin déjà couvert par un
  ancêtre inscriptible par tous présent dans la liste ; verser un essai **sain et artefact** d'un dossier inscriptible
  par tous **imbriqué sous `/tmp`** (l'organisme doit tourner et ne rien partager). Nouveau commit, nouvelle empreinte,
  revérification.

### CL6-03 — mineure — CL5-08 à demi corrigée : contradiction interne sur la présence de Brave au scellement

- Fichiers : texte v6 l.298-301 contre l.304-306.
- Défaut : l.299-300 affirme « `BRAVE_API_KEY` … — **elle ne l'est pas** dans la session « session-depot » au
  scellement » (ancienne affirmation, celle que CL5-08 disait fausse) ; l.304-306 affirme « au 25 octobre vers 02:1x
  UTC, … les noms `GEMINI_API_KEY`, `GEMINI_API_KEY_2` et `BRAVE_API_KEY` **sont définis** dans l'environnement ». Les
  deux portent sur la même session au scellement et se contredisent. L'enjeu n'est pas nul : si Brave est présente, la
  source `web` est servie aux deux bras et la règle des pannes a **cinq** comparaisons par paire au lieu de quatre
  (Seuil, l.257-258) — le lecteur ne sait pas quel cas tenir.
- Preuve : lecture des l.298-308 (noms seulement, aucune valeur lue).
- Correction proposée : supprimer ou réécrire la clause l.299-300 pour qu'elle concorde avec l'état observé l.304-306
  (Brave présente au scellement ⇒ cinq comparaisons attendues, sous réserve de la présence au lancement).

### CL6-04 — forme — CL5-12 : la docstring du script de scellement n'est pas « juste »

- Fichiers : `sceller_etape1_v6.py` l.4 et l.6.
- Défaut : la revendication (texte l.669) dit « docstring juste », mais l.4 dit encore « Refuse si le texte relu par la
  **contre-lecture n° 4** … » (devrait être n° 6 ; le message d'erreur l.29 dit bien « n° 6 »), et l.6 dit « Décliné de
  `sceller_etape1_v4.py` » (le précédent était `sceller_etape1_v5.py`, cf. CL5-12).
- Correction proposée : l.4 « n° 6 » ; l.6 « `sceller_etape1_v5.py` ».

### CL6-05 — forme — CL5-11 : le nom de la pièce de mutations n'est pas corrigé dans le texte

- Fichiers : texte v6 l.37 contre l.668 ; pièce réelle `mutations/sortie-mutations-cl5-v1.txt`.
- Défaut : l.37 cite « pièce `mutations-rv-v2.txt` » (exactement le nom que CL5-11 disait faux) et « pièce
  `mutations-cl5-v1.txt` », tandis que la revendication l.668 dit « pièce `sortie-mutations-v2.txt` nommée juste ». La
  pièce réelle des mutations CL5 s'appelle `sortie-mutations-cl5-v1.txt`. Incohérence interne et renvoi R6 inexact.
- Correction proposée : aligner les noms de la l.37 sur les fichiers réellement versés
  (`sortie-mutations-v2.txt`, `sortie-mutations-cl5-v1.txt`).

---

## Points demandés (les trois graves rejoués)

- **CL5-01** (isolement dépôt/code/`/home`…) : **juste au fond**, mais ne vaut que si CL6-02 est corrigé. Rejoué
  (code corrigé) : secret sous `ESSAIM_M3_CACHER` et sous `/home`/`/root` inaccessibles (`PermissionError`) ; fichier du
  dossier de travail lisible ; organisme tourne ; aucune fuite du marqueur `MARQUEUR-VERITE-CL6`.
- **CL5-02** (voie commune fermée) : **juste au fond**. Rejoué : un dossier 1777 hors des quatre (sous `/var/lib`) est
  trouvé par le balayage et mis en privé ; A y écrit, B lit `FileNotFoundError`, rien n'atteint l'hôte. **Mais** la mise
  en œuvre fait échouer l'exécution sur un dossier imbriqué (CL6-02).
- **CL5-03** (amorçage de Fable sous le plafond) : **juste**. Lanceur v4 à 5 USD par génération (plafond 40) ; pire cas
  Fable 3,40 USD < 5 (passe), > 3 (refusé à l'ancienne valeur) ; `test_cl5_03` passe.

**R1 (invariants).** Hypothèse, Prédiction chiffrée et Critères de lecture gelés **identiques** v5 → v6 (diff vide). Seuil :
la table de puissance (effet +0,10, taux) **inchangée** ; seuls s'ajoutent le 0,76 % à effectifs inégaux (CL5-11) et le
cas « cinq comparaisons si Brave présente » (CL5-08). Métrique : la règle des pannes est celle de la v5. Donc « sans
changer hypothèse/prédiction/métrique principale/seuil/table de lecture » tient.

**Asymétrie A/B nouvelle introduite par les corrections** : aucune trouvée. Les deux boucles (prives, caches) et le
classement des échecs valent pour les deux bras. CL6-02 arrête **les deux bras** de la même façon (pas de biais de Δ,
mais plus aucune lecture possible).

---

## Ce que j'ai rejoué (tout sous `…/r2-etape1-v6/travail/`)

Root, `env -i PATH=/usr/bin:/bin HOME=<travail>/home LANG=C.UTF-8`,
`ESSAIM_M3_COLLISIONNEUR=…/collisionneur_v2.py ESSAIM_M3_ESPACE=/var/lib/essaim-m3`, `/opt/essaim-m3-venv-v1/bin/python`
(3.13.17, numpy 2.4.6), `-I -B`. `capacites_isolation()` = root + espaces de noms présents.

| quoi | résultat | sortie | empreinte |
|---|---|---|---|
| `sha256sum -c EMPREINTES-pieces.txt` | 164 / 164 OK | `verif-empreintes-pieces.txt` | `27c8a76e…` |
| scellement à blanc (script livré, puis patché v4) | refus code 2 ; patché : passe l'entrée et les marqueurs | `sortie-cl6-scellement.txt` | `c07525e6…` |
| suite complète (− 3 désélectionnés) | 95 réussis, 37 échoués (banque retirée + CL6-02), 3 désélectionnés = 135 | `sortie-pytest-224de13.txt` | `71b90576…` |
| 7 essais CL5 en isolé (hôte propre) | 7 passés | (transcription) | — |
| CL6-02 : boucle `prives` (livré vs patché) + logique d'isolation CL5-01/CL5-02 | livré `SANS_STATUT`/errno 2 ; patché `OK` ; isolation juste | `sortie-cl6-defaut-et-isolation.txt` | `b0c5f09a…` |
| 4 mutations CL5 (code patché) | chacune fait échouer son essai | `sortie-cl6-mutations-cl5.txt` | `e42908fc…` |
| 53 essais du lanceur v4 | 53 réussis, 0 échec ; concordent avec la pièce (hors chemins et commit jetable) | `sortie-cl6-essais-lanceur-v4.txt` | `7551cd2b…` |
| CL5-03 pire cas d'amorçage (`cv.cout_pire_cas`) | Fable 3,40 ; Opus 1,36 ; Argon 1,80 | (transcription) | — |
| empreintes du code changé | `analyse_gradient.py` `4b54d380`, `bac_a_sable.py` `8f52ec88`, arbre noyau `f43946a3` : concordent | (transcription) | — |

Empreintes de mes sorties et scripts : `EMPREINTES-travail-cl6.txt` (`bfe744cc…`).

## Ce que je n'ai pas pu vérifier

- Le fichier du vivier (absent) et ses comptes ; la banque réelle hors des essais qui la lisent (données retirées des
  pièces : les essais qui les lisent échouent, attendu).
- Si le script de scellement réel du dépôt diffère de la pièce `sceller_etape1_v6.py` (j'ai relu la pièce citée).
- Les courses, la moisson, les espèces réelles ; aucun appel à une interface de modèle ni à une source de moisson.
- Les décisions et registres (R-xxx, GO) : hors des pièces.
- Je n'ai pas refait les contre-lectures n° 4 et n° 5 ni la revérification du code.

## Hygiène

J'ai créé, pour mes reproductions, `/tmp/cl6nested-ww` et des dossiers `/var/lib/cl6-*` : tous retirés (vérifié, aucun
processus restant). Je **n'ai pas** retiré ce qui n'est pas de moi : un dossier inscriptible par tous laissé par le
relecteur n° 5, `/var/lib/essaim-m3-cl5-commun-28a34687918d` (02:22 UTC) ; et des dossiers `vartmp`/`tmp` inscriptibles
par tous, imbriqués sous `/tmp/…/scratchpad/r2-*`, laissés par des relecteurs antérieurs (ce sont eux qui déclenchent
CL6-02 sur cet hôte). Copies de code et clone git retirés après usage.
