# Orchestrateur du pôle, v7 — version 50 : corrections de la contre-lecture CL14 (identité du script sur l'hôte, sortie scellée, recalcul strict, Argon)

Lignée conv-audit (sous-agent), 30 octobre 2026. v1 à v49 gardées (R12) : LISEZMOI et EMPREINTES v1 à v49 intacts (aucun
fichier scellé d'une version précédente n'est modifié). Le code de la v49 est conservé dans `CODE-orchestrateur-pole-v7-v49.zip`
(92 fichiers de code, chacun égal à l'empreinte de `EMPREINTES-orchestrateur-pole-v7-v49.txt`, vérifié) : les cinq modules
modifiés ci-dessous ne sont donc pas écrasés sans trace.
**Attendu, dit :** `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v49.txt` sur l'arbre v50 donne **5 échecs** (les cinq fichiers de la table de
provenance ci-dessous, modifiés en place comme en v49) ; leurs empreintes v49 sont celles du lot zippé, et `EMPREINTES-orchestrateur-pole-v7-v50.txt`
(178 lignes) se vérifie en entier sur l'arbre.
Source : `contre-lecture-cl14-orchestrateur-v49-v1.md` (sous-agent neuf, R2) : 12 constats (CL14-01 à CL14-12), dont un critique
(CL14-01) et un de gravité haute (CL14-02). Les douze sont traités ci-dessous.

**v50 n'est pas contre-lue.** Elle corrige une contre-lecture ; elle n'a pas été relue par un sous-agent neuf.

**Aucune session réelle, aucune dépense, aucun réseau, aucune clé, aucun `bwrap` exercé.** `bwrap` est absent de cette machine
(`which bwrap` : rien). Tout ce qui dépend du vrai bac à sable est vérifié **en structure seulement** : commande, drapeaux,
montages, logique de la sonde sur des sorties données, plomberie du noyau avec un faux `bwrap` qui ne confine rien. Deux choses
sont en revanche **jouées pour de vrai**, parce que cette machine est superutilisateur et a `setpriv` : (a) le lancement d'un
processus sous une identité sans privilège (uid 64097, `setpriv --reuid … --clear-groups --no-new-privs`) avec propriété des
fichiers, borne de processus effective et retrait du dossier de travail ; (b) le script de la sonde des privilèges, joué sous cette
identité hors du bac (il rend toutes ses lignes). Aucun essai n'écrit dans un réglage du noyau de l'hôte : la sonde **ouvre**
`/proc/sys/…` en écriture sans jamais écrire, et une ouverture qui réussirait est un échec d'essai. Toutes les cibles des
essais sont des dossiers provisoires créés par les essais, jamais le vrai `/usr`, `/etc` ou `/root`.

**Rétrocompatibilité.** Sans `--tests-de-mort`, les sorties de la course de référence restent celles de la v47 octet pour octet
(empreintes gelées `SORTIES_V47_SHA256`, `CONSIGNES_V47_SHA256`, `REGLAGES_KIT_V47_SHA256`, essai `test_v48_11`, rejoué et OK).
**Changements de contrat à lire avant tout lancement de l'étage** (tous voulus, tous refusent plutôt que de se replier) :
1. un noyau superutilisateur **doit** donner `--utilisateur-bac` et `--dossier-travail-bac`, sinon l'étage est refusé avant la sonde ;
2. la sortie scellée ne contient plus de dossier `travail` : les produits sont copiés sous `produits/<nom>.copie` ;
3. avec le moteur réel, `--experimentateur-externe` est refusé (la commande d'Argon ne l'accepte pas) et l'étiquette de tout rôle
   externe doit être celle que la commande demande (`gemini-4-argon`) ;
4. un « survit » dont l'arrondi d'affichage fait franchir le seuil devient « non concluant ».

## Constat → correction → essai

| constat | correction | essai |
|---|---|---|
| **CL14-01** (critique) : `/proc/sys` inscriptible depuis le bac ; l'identité du script sur l'hôte est le superutilisateur (`--uid 65534` sous un noyau superutilisateur correspond à l'identifiant 0 de l'hôte) : `kernel/core_pattern` mène à l'exécution de code en superutilisateur sur l'hôte | **Défense recommandée appliquée** : `bwrap` est lancé sous un **utilisateur dédié sans privilège** (`resoudre_utilisateur_bac` : entier ou nom, jamais 0 ; `commande_lancee` : `setpriv --reuid U --regid U --clear-groups --no-new-privs --` devant `bwrap`). `verifier_identite` (avant toute sonde, aucun repli) : noyau superutilisateur sans utilisateur dédié = **étage refusé** ; avec utilisateur dédié, dossier racine du bac obligatoire, vrai dossier (pas un lien), possédé par lui, non inscriptible par le groupe ou les autres ; utilisateur dédié avec un noyau non superutilisateur = refusé ; `setpriv` absent = refusé. Les dossiers et fichiers que le noyau crée (`creer_dossier_neuf`, `ecrire_exclusif`, `ecrire_dans_travail`) sont remis à l'utilisateur par descripteur (`fchown`) ou `lchown`, sans suivre de lien. En plus : `--ro-bind /proc/sys /proc/sys` juste après `--proc /proc`. **Sonde** (R5) : lit `UID_HOTE` et `GID_HOTE` dans `/proc/self/uid_map` et `gid_map` (colonne « dehors »), **refuse l'étage** si l'un vaut 0 ou n'est pas l'utilisateur dédié attendu ; ouvre en écriture (sans écrire) `kernel/core_pattern`, `fs/suid_dumpable`, `vm/drop_caches`, `kernel/modprobe` et compte les réglages ouvrables de tout `/proc/sys` : un seul ouvrable = refus ; `CapBnd` doit être nul | `test_v50_01`, `_02`, `_03`, `_04`, `_05`, `_06` ; `test_v49_01` (commande) ; réel : `test_v50_15` |
| **CL14-02** (haute) : script = superutilisateur de l'hôte → fichiers setuid-root dans la sortie, `RLIMIT_NPROC` inopérante | Même cause, même correction : sous l'utilisateur dédié la borne de processus s'applique (`borne_processus_effective` ; dite au manifeste ; fausse pour un noyau superutilisateur sans utilisateur dédié, qui est de toute façon refusé). **Sonde** : essaie de créer `limite + 32` enfants dormants et exige un refus (`EAGAIN`) avant, les tue ensuite ; refuse une borne absente ou non posée. **Aucun fichier setuid ou setgid** : l'inventaire les voit (`lstat`), ne les hache ni ne les copie, les consigne (`interdits`, `non_copies` : « fichier setuid ou setgid (refusé) ») ; dans l'étage : exécution « échouée (fichier setuid ou setgid) », incident, verdict « non concluant » même si le chiffre imprimé passe le seuil | `test_v50_03`, `_05` (borne tenue pour de vrai sous l'utilisateur dédié), `_07` |
| **CL14-03** (moyenne) : espaces d'utilisateurs imbriqués permis dans le bac | `--disable-userns` (bwrap ≥ 0.8.0) avant `--cap-drop`, sauf `--userns-imbriques-permis` (demande expresse, dite au manifeste et à la description, refusée par défaut). Sonde : tente `unshare(CLONE_NEWUSER)` dans un enfant, **refuse** si elle réussit (sauf demande expresse). Si `bwrap` est trop ancien ou installé setuid, la sonde échoue avec un message qui nomme la cause | `test_v50_01`, `_03` ; réel : `test_v50_15` |
| **CL14-04** (moyenne) : le dossier de travail entier reste dans la sortie scellée (liens vers `/proc/self/environ`, tubes, gros fichiers) | Le dossier de travail de chaque exécution vit sous un **dossier racine hors de la sortie** (`ouvrir_racine_travail` : `etage-travail-*` dans le dossier provisoire du système, ou `--dossier-travail-bac`), est inventorié puis **retiré** (`supprimer_arbre`, sans suivre de lien, rouvre un sous-dossier fermé ; un échec de retrait est un incident). La sortie scellée ne garde que les **fichiers réguliers déclarés**, copiés (≤ 1 Mo) sous `produits/` ; liens, tubes, prises, gros fichiers : nom, genre, empreinte, jamais le contenu. Le dossier racine est retiré aussi quand l'étage s'arrête en route (`finally`) | `test_v50_09` ; `test_v49_06`, `_07` adaptés |
| **CL14-05** (moyenne) : un produit nommé `<x>.sha256` à côté de `<x>` interrompt tout l'étage | `nom_copie` : suffixe `.copie` à **chaque composant** du chemin (`r.txt` → `r.txt.copie`, `r.txt.sha256` → `r.txt.sha256.copie`) ; injective, jamais un compagnon `.sha256`, jamais le nom d'une autre copie. La copie reste liée au chemin d'origine dans le manifeste (clé `copie`) | `test_v50_10` (cas `r.txt`/`r.txt.sha256`, `a`/`a.copie`/`a.copie.sha256`, deux fiches jouées) |
| **CL14-06** (moyenne) : l'arrondi admis fait franchir le seuil, et l'étiquette dit « recalculé par le noyau » | `recalcul_noyau` prend aussi le verdict **sur la valeur du noyau, sans arrondi** (`verdict_sur_valeur_noyau`) ; s'il diffère du verdict sur le chiffre imprimé (`arrondi_franchit_le_seuil`), le résultat est **« non concluant »** (R4, dans les deux sens de comparaison). L'étiquette devient **« statistique déclarée par le script, recalculée par le noyau »** (`ETIQUETTE_RECALCULE`) : ce que le noyau a vérifié, rien de plus. Le lecteur et le matériau voient les deux | `test_v50_11` (moyenne 0,46 imprimée `0.5` ; écart type 0,7071 imprimé `0.7` aux seuils « au moins 0,705 » et « au plus 0,705 » ; cas franc « au moins 0,5 » qui reste « survit ») ; `test_v49_16` |
| **CL14-07** (moyenne) : Argon — expérimentateur impossible avec la commande réelle ; LISEZMOI inexact | **LISEZMOI v49 corrigé ici** : la commande réelle `/opt/argon/commande_argon_v2.py` rend déjà `modele_servi` (le contrat est tenu pour le proposeur et le juge) ; ce qui est faux dans le LISEZMOI v49 est « elle ne rend pas encore `modele_servi` ». Ce qui ne marche pas : `ROLES = (proposeur_ideation, juge_ideation)`, tout autre `ROLE_POLE` (dont `experimentateur_test`) est refusé avec le code 2 ; elle ignore `MODELE_DEMANDE_POLE` et demande toujours `gemini-4-argon`. Lanceur (`verifier_commande_externe_reelle`, avant tout appel, `CourseInterrompue`) : avec le moteur réel, `--experimentateur-externe` est **refusé, dit non fonctionnel avec la commande réelle**, tant que `--commande-externe-accepte-experimentateur` n'atteste pas une commande qui l'accepte ; tout rôle externe (proposeur, juge, expérimentateur) dont l'étiquette n'est pas `gemini-4-argon` (ou `--modele-commande-externe`) est refusé avec son motif. **La commande d'Argon n'est pas modifiée** (hors de ce dépôt) : une v3 sous un nouveau nom (R12) est à faire côté session-depot | `test_v50_14` ; `test_cl43_03` (argv corrigé) |
| **CL14-08** (mineure) : « suffixe de date » = tout suffixe | `SUFFIXE_DE_DATE` : `-20AAMMJJ` exactement (mois 01-12, jour 01-31), après l'identifiant demandé ; `-mini`, `-lite`, `-latest`, `-2026`, `-2026-10-01`, un préfixe `models/` sont des écarts. Une variante connue s'admet par une **liste explicite** (`modeles_servis_permis`, option `--modele-servi-externe-permis DEMANDÉ=SERVI`), jamais par un motif large. Même règle pour le kit, la défense générique de la course et l'étage | `test_v50_12` ; `test_v49_09`, `_10` |
| **CL14-09** (mineure) : écart de modèle vu par la commande d'Argon rangé en « erreur » | Sur un code non nul ou un délai, si la dernière ligne lisible dit un refus ou porte un `modele_servi` différent : statut **« refus »** (jamais le texte), `depense_modele_non_autorise_usd` = coût de la ligne. Une erreur ordinaire (ligne sans `modele_servi`, ou avec le modèle demandé) reste une « erreur » | `test_v50_13` |
| **CL14-10** (mineure) : `/dev/shm` sans borne | `--size 33554432 --tmpfs /dev/shm` après `--dev /dev` (32 Mo ; bwrap ≥ 0.9.0 ; message dédié si l'option est inconnue). Sonde : écrit au-delà de la borne, exige `ENOSPC` (« non monté » admis) | `test_v50_01`, `_03` ; réel : `test_v50_15` |
| **CL14-11** (mineure) : sonde et essais réels sans les artefacts | La sonde joue maintenant : `/proc/sys`, l'identité de l'hôte, l'espace imbriqué, `/dev/shm`, la borne de processus, `CapBnd`. Chacun a son artefact (la sortie qui échoue refuse l'exécuteur, avec son motif ; 19 artefacts, plus la preuve par le faux bac et par le vrai script sans privilège). `test_v49_19` et `test_v48_22` passent par `executeur_reel` (utilisateur dédié exigé sous un noyau superutilisateur) ; deux essais réels nouveaux : `test_v50_15` (les évasions de CL14 : `/proc/sys`, `uid_map`, espace imbriqué, `/dev/shm` 64 Mo, 1 100 processus, fichier setuid, lien, tube, `.sha256`) et `test_v50_16` (liens, tube et noms `.sha256` par l'étage entier avec le vrai bac, comme `test_v49_06`, `_07`) | `test_v50_03`, `_04`, `_15`, `_16` |
| **CL14-12** (mineure) : noyau non superutilisateur — un sous-dossier fermé échappe à la borne et à l'inventaire | `inventaire_travail` : un dossier ou une entrée illisible (hors disparition en cours de parcours) est un **dépassement** « dossier illisible : non parcouru (…) », au parcours complet comme à la mesure rapide pendant l'exécution ; jamais ignoré en silence. Le retrait rouvre le sous-dossier fermé (`_rendre_accessible`) | `test_v50_08` (artefacts de `scandir`, puis **pour de vrai** sous l'identité sans privilège avec un sous-dossier de mode 000, contraste avec le noyau superutilisateur qui le lit) |

Les essais antérieurs adaptés à la nouvelle forme : `test_v48_05` (nom `.copie`), `test_v48_07`, `test_v48_22`, `test_v49_01`, `_06`, `_07`, `_16`, `_18`
(la provenance de la v49 se compare maintenant à `EMPREINTES-orchestrateur-pole-v7-v49.txt` et non au disque, qui a changé), `_19`,
`test_cl43_03`, `TestCommandeExterne.test_commande_factice_notes_et_controle` (nouvelle clé `modeles_servis_permis` de la description).
Les fausses sorties (`SORTIE_PRIVILEGES_SAINE`) portent les nouvelles lignes ; `ExecuteurBacSimule` et `ExecuteurFactice` ne sont
pas soumis à l'identité (aucune barrière, dit).

**Contrôle des essais par mutation (R5, R4).** Chaque garde nouvelle a été retirée à tour de rôle, l'essai qui la couvre a échoué
à chaque fois, puis le code a été rétabli (octet pour octet, vérifié) : `--ro-bind /proc/sys` (`test_v49_01`), `--disable-userns`
(`TestV49`), le franchissement du seuil par l'arrondi (`test_v50_11`), le refus des fichiers setuid (`test_v50_07`), la lecture de
l'identité attendue de l'hôte (`test_v50_03`), le suffixe de date strict (`test_v50_12`), le préfixe `setpriv` (`test_v50_01`, `_05`),
la réouverture d'un sous-dossier fermé (`test_v50_08`), le suffixe `.copie` (`test_v50_10`).

Choix d'interprétation à relire : (1) la défense contre l'identité 0 de l'hôte est **l'utilisateur dédié, obligatoire** sous un noyau
superutilisateur, plus `/proc/sys` en lecture seule : l'une sans l'autre ne suffirait pas (la sonde exige les deux). (2) Le noyau
**ne prend pas** le dossier racine du bac pour un dossier à créer : il doit exister, être possédé par l'utilisateur dédié et fermé aux
autres (refus sinon) ; c'est à l'opérateur de le préparer. (3) CL14-06 : au bord du seuil, l'étage dit « non concluant » plutôt que de
trancher ; c'est plus prudent que la v49, et une statistique dont l'arrondi est faible (peu de décimales) sera plus souvent
« non concluante ». (4) CL14-07 : le noyau envoie toujours `MODELE_DEMANDE_POLE` à la commande ; elle l'ignore ; l'envoi est gardé (inoffensif,
et la v3 de la commande pourra le lire), la vérification que l'étiquette est celle d'Argon se fait au lanceur.

## Prérequis de l'opérateur pour l'étage réel (rien de tout cela n'est préparé ici)

Sous un noyau superutilisateur : un utilisateur de l'hôte **dédié** (uid/gid ≠ 0, sans autre processus ni fichier, de préférence
sans shell ; `RLIMIT_NPROC` compte tous ses processus), `setpriv` (util-linux) et `bwrap` ≥ 0.9.0 **non installé setuid**, un dossier
racine possédé par cet utilisateur (mode 0700) dont tous les parents sont traversables par lui, un python lisible par lui, les espaces
d'utilisateurs non privilégiés permis pour lui (sinon la sonde échoue et l'étage est refusé). Ex. :
`--tests-de-mort N … --utilisateur-bac 64097 --dossier-travail-bac /srv/bac-pole`.

## Provenance du code modifié (R12)

Chaque fichier de code dont le contenu diffère de la v49, avec son empreinte v49 (celle de `EMPREINTES-orchestrateur-pole-v7-v49.txt`,
et du lot `CODE-orchestrateur-pole-v7-v49.zip`) et son empreinte v50. Fichier d'essais : son empreinte v50 n'est pas comparée par l'essai
(il ne peut pas se contenir lui-même) mais elle est dans `EMPREINTES-orchestrateur-pole-v7-v50.txt`.

| fichier | empreinte v49 | empreinte v50 |
|---|---|---|
| `demonstrations/ideation_v1.py` | `cdcdcdddaa2840674c2255769a9aa55c5f61cc6e087b0eba45a9f95daca03218` | `855a1139f5fb8463699fad22c3725fc0f630488186add94f1da909b12bccf17e` |
| `essais/test_v7_ideation.py` | `eb7477b7c7f7b4e9b76abab2b65a2dbd9ab8557fdc06ad36c3df2490f6e03092` | `7dd7be9a275b9523153f7f6c2f7f25b9b25199fbf56989efd11c058fddd82b58` |
| `pole/adaptateurs.py` | `aa0b93938c71bf3690d6d152f17f4a07c9b4b64d35f6b5454213a65d12953ad2` | `a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99` |
| `pole/ideation.py` | `aace98f24108e4484d11c5cf3b05f77c8ab1bcce0fb8f1662432ad5ea85f8f65` | `4ee70d25567a9b3ac90911cc5ebee8cebba0537d541e7a0ebc1fa3ed170abdc2` |
| `pole/tests_de_mort.py` | `c57c49aa822f57fb1a1cec8e8850f7f9685bb442d7d21aa80a1658a992b16338` | `fc5d3507b33e13094d64751ff2b4564ba5ed4c238f93aaae808c458b3c123252` |

Aucun autre fichier de code ne change. `pole/protocole_outils.py`, `pole/relais.py`, `pole/relais_reel.py`, `pole/relais_moisson.py`
sont ceux de la v49.

## Essais

**502 essais** (485 en v49 ; + 17 `TestV50` dans `essais/test_v7_ideation.py`, avant `tdm_roles()`) : **498 OK, 4 ignorés**
(les quatre essais réels conditionnels à `bwrap` : `test_v48_22`, `test_v49_19`, `test_v50_15`, `test_v50_16`), 0 échec, deux exécutions
complètes sur l'arbre final (`python3 -B -m unittest discover -s essais -t . -p 'test_*.py'`), aucun processus survivant, `essais/_tmp` et
`__pycache__` retirés. En v49 : 485 essais, 483 OK, 2 ignorés. Une première exécution de la v50 avait trois échecs, tous des essais de la
v49 rendus faux par la correction voulue (nouvelle clé de description, étiquette d'Argon, LISEZMOI de la v50 absent) : corrigés.
Les essais qui exigent un noyau superutilisateur avec `setpriv` (`test_v50_04`, `_05`, `_08` en partie) sont ignorés ailleurs, avec leur motif.
Sous un noyau superutilisateur, les essais réels exigent `POLE_ESSAI_UTILISATEUR_BAC` (uid sans privilège) et
`POLE_ESSAI_RACINE_TRAVAIL_BAC` (dossier à lui, traversable) ; sinon ils sont ignorés avec ce motif (jamais un repli sur le superutilisateur).
Fichiers changés : voir la table. Fichiers nouveaux : ce LISEZMOI, les EMPREINTES v50, `CODE-orchestrateur-pole-v7-v49.zip` (R12).

Une observation faite en jouant la sonde hors du bac, sous l'identité sans privilège de cette machine : `kernel/ns_last_pid` (mode 0666,
propre à l'espace de processus) **s'ouvre en écriture**. Hors du bac, la sonde compte donc un réglage ouvrable ; c'est le montage en
lecture seule de `/proc/sys` qui est censé le fermer dans le bac (refus `EROFS`). Si, dans le vrai bac, `PROCSYS-OUVRABLES` n'est pas 0, l'étage
est refusé : **à voir au premier jeu réel**.

## Ce qui n'est pas vérifié en réel

- **`bwrap` n'a jamais été exercé ici.** Non vérifiés : l'effet réel de `--ro-bind /proc/sys /proc/sys` (refus d'écriture sur
  `core_pattern`, `EROFS`) ; de `--disable-userns` (bwrap ≥ 0.8.0) ; de `--size` et `--tmpfs` pour `/dev/shm` (bwrap ≥ 0.9.0) ; le
  comportement de `--unshare-user --uid 65534` **sous l'utilisateur dédié** (la ligne `UID_HOTE` doit alors valoir l'uid de l'utilisateur
  dédié : c'est ce que la sonde exige, mais elle n'a été lue que sur des sorties données et sur un script joué hors du bac) ;
  `--cap-drop ALL` et `CapBnd` nul dans le bac ; `--die-with-parent` et l'arrêt des petits-enfants par un noyau superutilisateur
  quand le bac est sous un autre utilisateur ; le montage de `/proc` dans le bac par un utilisateur sans privilège ; la création des espaces
  d'utilisateurs pour l'utilisateur dédié (selon le noyau et la distribution : `kernel.unprivileged_userns_clone`, restrictions AppArmor ;
  dans ce cas la sonde échoue et l'étage est refusé, sans repli). Les quatre essais réels (`test_v48_22`, `test_v49_19`, `test_v50_15`,
  `test_v50_16`) sont écrits et **jamais joués ici** : **à rejouer dans le conteneur de session-depot, avec `bwrap`, avant tout GO de
  l'étage.**
- **La borne de processus dans le bac.** Jouée pour de vrai sous l'utilisateur dédié avec un faux `bwrap` (le fork échoue avant la borne),
  mais pas sous `bwrap` : `RLIMIT_NPROC` y est héritée à travers `setpriv` puis `bwrap` ; elle compte les processus de l'utilisateur dédié
  **sur l'hôte**, y compris ceux d'un autre bac qui tournerait en même temps sous le même utilisateur (un seul bac à la fois par
  utilisateur dédié).
- **La sonde dans le vrai bac.** Les lignes `SHM` (`ENOSPC` après 32 Mo), `PROCESSUS` (`EAGAIN`), `USERNS-IMBRIQUE` (refus), `REMONTAGE` (refus)
  sont des valeurs ATTENDUES, jamais lues dans un vrai bac. Les valeurs hors bac sont autres (`SHM` ordinaire non borné, `CapBnd` non nul).
- **Les prérequis de l'opérateur** (utilisateur dédié, dossier racine, parents traversables, python lisible, `bwrap` non setuid) ne sont
  pas préparés ; `verifier_identite` en contrôle une partie (propriétaire, droits, vrai dossier), pas la traversabilité des parents (la sonde
  l'attrape : « `bwrap` ne s'exécute pas », avec un indice).
- **Argon.** La commande réelle (`/opt/argon/commande_argon_v2.py`) n'est **pas sur cette machine** : ce qui la concerne vient de la contre-lecture
  CL14 (lignes citées par elle), non relu ici ; elle n'est **pas modifiée** et n'a pas été relancée. Reste de son côté : (a) elle ignore
  `MODELE_DEMANDE_POLE` ; (b) elle refuse `experimentateur_test` (donc l'expérimentateur externe reste impossible) ; (c) elle accepte
  un préfixe `models/` et un suffixe quelconque (l. 226-228) là où le noyau est maintenant strict ; (d) **le format réel de
  `modelVersion`** (donc de `modele_servi`) n'est pas connu : si Argon rend autre chose que `gemini-4-argon` ou `gemini-4-argon-AAAAMMJJ`,
  le noyau refuse la première session (un refus coûte le plancher du coût déclaré) ; la parade est `--modele-servi-externe-permis
  gemini-4-argon=<valeur réelle>`, à fixer au premier jeu réel avec Lazar. Une v3 de la commande, sous un nouveau nom (R12), est à
  faire côté session-depot ; en attendant, `--experimentateur` (Claude).
- **Forme exacte de `model_usage`** du kit : toujours SUPPOSÉE (comme en v49). **Crochet `PreModelSwitch`** : non implémenté.
- **Relais de moisson réel** : inchangé depuis la v49 (amont arXiv en https et compteur persistant éprouvés contre l'amont factice) ; la
  garde de fuite reste lexicale.
- **Filtre d'appels système** : non ajouté (`--disable-userns` et l'utilisateur dédié traitent les constats CL14-01 à 03) ; à envisager.
- Le statut des résultats de l'étage reste **exploratoire** ; le recalcul ne couvre que les statistiques simples déclarées.

## Fabrication des empreintes

```
(awk '{print $2}' EMPREINTES-orchestrateur-pole-v7-v49.txt; echo LISEZMOI-orchestrateur-pole-v7-v50.md; echo EMPREINTES-orchestrateur-pole-v7-v49.txt; echo CODE-orchestrateur-pole-v7-v49.zip; echo CODE-orchestrateur-pole-v7-v49.zip.sha256) | sort -u | xargs sha256sum > EMPREINTES-orchestrateur-pole-v7-v50.txt
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v50.txt
```
