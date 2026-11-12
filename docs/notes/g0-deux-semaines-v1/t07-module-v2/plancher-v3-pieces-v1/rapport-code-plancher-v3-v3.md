# Rapport du développeur : code du plancher v3 de T0.7 — v3 (dernier tour : contre-lecture courte des corrections, R-2311)

Écrit le 2026-11-11, de 04:25 à 04:57 UTC (heures relevées par `date -u`), par le développeur du plancher v3 (Claude Opus 5.5,
`claude-opus-5-5`, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`), sur le message de la mère qui suit la
contre-lecture courte des corrections
(`docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/contre-lecture-courte-corrections-plancher-v3-v1.md`,
`6f376911…`, compagnon vérifié par `sha256sum -c`) et la décision **R-2311**. **Les rapports v1 (`cb31edc8…`) et v2
(`71cc3b89…`) restent intacts** ; cette v3 les complète pour ce qu'elle nomme. Mêmes interdits ; aucune donnée de 7a, 7b,
P3-bis ; aucun appel de modèle, aucune instance, aucune dépense. **Je reste exclu de tout rôle de lecteur de P3-bis.** Deux
modules non fusionnés ni scellés corrigés en place sur ma branche (`reextraction_p3_v1.py`, `lecture_v4.py` : écart à la lettre
de R12, déclaré par R-2305) ; tout le reste est en fichiers neufs.

## Verdict

**Les six points de R-2311 sont faits, éprouvés et poussés** sur `prep/t07-plancher-v3-v1`, **commit final
`a621dcd3b929ce3ebd615fa852d4a7f5c103071d`** (au-dessus de `7e23a554` : `85ba2c02` corrections, `be3191c9` répétition v4,
`a621dcd3` essai réel complété). Garde des secrets à 0 avant chaque commit, chaînée par `&&` ; poussée de ma seule branche.

- **CLC-P3-02** : sous-commande neuve **`lecture_v4 controle-avant-ouverture RACINE CONFIG [--cache-dir D]`** (lecture seule :
  contrôles de configuration de la v4, puis `controler_avant_ouverture` **en entier** — sceaux des quatre entrées de P3,
  principales, témoin et directions de P3 au fichier léger, révision du modèle de P3 au cache local en mode réel) ; **script
  v4** `scripts/etape_a_t07_variante_b_v4.sh` (le v3 reste intact) qui la joue **à l'étape 8, dans les deux modes, avant
  l'empreinte de la configuration, CODE-T07, la branche, le repli et sa garde d'ouverture** ; faute → **code 2**, motif écrit au
  journal (« ARRET : contrôle avant l'ouverture (réextraction de P3) : code 2 : REFUS : … : rien n'est ouvert »), rien d'ouvert.
- **CLC-P3-03** : `revision_au_cache` : index lu sous garde (illisible, `weight_map` absente, vide ou mal formée → `GardeArret`,
  code 2 à la sous-commande) ; morceaux `model-<i>-of-<n>` sans index refusés ; autant de morceaux que leur nom en annonce ;
  tailles nulles refusées. Les trois formes partielles admises au v3 (contre-lecture, § 3 (2)) sont refusées.
- **CLC-P3-05** : `${ENV_CPU[@]+"${ENV_CPU[@]}"}` (et la même forme pour le tableau `ex` de `pousser`, même défaut, trouvé par
  recherche) ; `CPU_ESSAI` (essai local seulement, refusée hors essai) éprouve la branche EPYC. **Bash antérieur à 4.4 non
  éprouvé ici** : la construction de bash 4.3 a été refusée par le classifieur de permissions (non contournée, § 4).
- **CLC-P3-06** : essais **de comportement** des notes 05 et 10 (sans le miroir) ; essais neufs pour x3, x8, x9.
- **Répétition jouet v4** : **10 verdicts sur 10**, conforme (normal complet, EPYC complet, artefact du contrôle arrêté à
  l'étape 8 sans rien ouvrir, branche déjà poussée, découpage, `CPU_ESSAI` hors essai) ; borne S-13 inchangée.
- **Mutations** : modules, **20 sur 20 tuées** (banc v5, copies, `-o pythonpath=`, import tracé ; c14 et c17 tuées **sans le
  miroir**) ; script v4, **3 sur 4 tuées**, la quatrième (`"${ENV_CPU[@]}"` du v3) **survit, mutant équivalent sous bash 5.2**,
  attendu et déclaré.
- **Essais** : suite `tests/test_t07_plancher_v3_*` au commit final : **92 passés, 0 sauté** (89,7 s). Suite `tests/test_t07_*`
  entière : **arrêtée par moi** (PID 10691) au-delà de 29 %, sans échec, le disque partagé tombant à 563 Mo libres (§ 7 bis) ; les deux
  modules changés ne sont importés que par les essais du plancher v3.

## 1. Lu (empreintes vérifiées)

- Contre-lecture courte des corrections (`6f376911…`, `sha256sum -c` : OK) : § 2 à § 5, en entier.
- Message de la mère (R-2311) ; les six points ci-dessous en suivent l'ordre.
- Mon code au commit `7e23a554` (rapport v2). Hors de mon extraction, rien d'autre que : la contre-lecture courte, la ligne de
  la garde des secrets de ma consigne scellée (par `grep`), la liste du dossier des pièces, la structure du rapport v2, et les
  fichiers réels de P3 (permis), ajoutés à mon extraction partielle : `runs/20261019-230011-p3-reel/manifeste.json`,
  `diag/20261019-230011-p3-reel/sondes-figees.json`, `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz` et leurs
  compagnons (sceaux vérifiés par les essais).

## 2. CLC-P3-02 : contrôle entier à l'étape 8, avant le repli

**Code.** `lecture_v4.py` (généré par `generer_lecture_v4_v3.py`, tête et pied seuls changés ; `passe_blanc_v2.py` et
`repli_etapes_v2.py` régénérés **à l'identique**, empreintes `8e24642f…` et `fe08aaa1…` inchangées ; miroir inchangé) :
fonction `controle_avant_ouverture(argv)`, aiguillée en tête de `main`. Configuration chargée par `charger_configuration` (v4 :
`n_plancher` 800, clé `plancher_figees`, tous les contrôles de la v3 et de la v2), puis
`reextraction_p3_v1.controler_avant_ouverture(racine, config, cache_dir)`. `GardeArret` et toute faute de
`FAUTES_DU_BRAS` (`OSError`, `ValueError`, `KeyError`, `TypeError`… : fichier de configuration absent, JSON faux) → « REFUS :
contrôle avant l'ouverture : … » sur l'erreur, **code 2**, rien sur la sortie ; passé → résumé JSON (figées, témoins, nombre de
directions de P3, graine de la seconde garde, révision au cache ou « sans objet » en jouet), **code 0**. Rien n'est écrit (essai :
arbre du run jouet de P3 identique avant et après, tailles et dates).

**Script v4** (`etape_a_t07_variante_b_v4.sh`, `4b17d1f0…`) : à l'étape 8, après le préchargement de la révision de P3 quand elle
n'est pas celle de 7b (inchangé, réel seulement), **une seule commande pour les deux modes** :

    HF_HUB_OFFLINE=1 PYTHONPATH=src "$PY" -m controle_ia.t07.lecture_v4 controle-avant-ouverture . "$CONFIG" \
        > "$X/controle-avant-ouverture.txt" 2> "$X/controle-avant-ouverture.err"; c=$?
    [ "$c" = 0 ] || arret "contrôle avant l'ouverture (réextraction de P3) : code $c : <600 premiers octets de l'erreur> : rien n'est ouvert" 2

Elle remplace l'appel isolé de `revision_au_cache` du v3. L'arrêt vient avant l'empreinte de la configuration, CODE-T07 (étape 9),
la branche (étape 10), le repli et sa garde d'ouverture journalisée (étape 11) : la branche n'étant pas prête, aucune trace n'est
poussée (comme tout arrêt d'avant l'étape 10 du v3). Passé : une ligne au journal (« passé ; figées […] ; modèle de P3 <révision>
| sans objet »). La passe à blanc (étape 12) le rejoue, inchangée. **Conséquence sur CLC-P3-05** : le bloc réel de l'étape 8 est
désormais **la même commande** que celle que joue la répétition ; seule la lecture du cache (mode réel) n'est pas jouée par
elle — elle l'est par l'essai réel ci-dessous.

**Essais** (`tests/test_t07_plancher_v3_avant_ouverture_v1.py`) :
- jouet, sur un vrai run jouet de P3, par `lv4.main` : cas sain (code 0, JSON) ; artefacts → code 2, motif : sceau de
  `sondes-figees.json` faux, principale autre, `n_p3` autre que le fichier léger (directions), garde de la principale inconnue,
  clé `plancher_figees` absente, configuration illisible, fichier de configuration absent ; témoin absent et sonde figée absente
  du fichier léger ; faute hors garde (`KeyError`, `OSError`) → code 2, type écrit ;
- **réel, sur les fichiers réels de P3 et la configuration v8** (révision `0e9e39f2…` lue au manifeste réel) : cache factice
  complet à cette révision → **code 0** (figées `tromperie-difference_moyennes-c15` et `enjeux-lineaire-c15`, 200 directions de
  P3 chacune, deux morceaux de poids) ; cache absent → code 2 ; index illisible → code 2 ; configuration v7 → code 2
  (« fixées d'avance ») ; `n_plancher` 200 → code 2 (contrôle de la v4, joué d'abord) ; mêmes fichiers en mode jouet → code 0,
  cache « sans objet », jamais lu.

## 3. CLC-P3-03 : cache partiel et fautes de l'index

`revision_au_cache` (`reextraction_p3_v1.py`, `c32696b8…`), lecture hors ligne inchangée (`snapshot_download(local_files_only=True)`) :

| forme (contre-lecture, § 3 (2), et voisines) | v3 | v4 du dernier tour |
|---|---|---|
| complet (morceaux et index) | passe | passe |
| un seul `model.safetensors`, sans index (modèle d'un seul fichier) | passe | passe (aucun morceau annoncé) |
| index absent, morceaux `model-<i>-of-<n>` présents (un sur deux) | **passe** | refusé : « morceaux sans index » |
| index présent, un morceau de taille nulle | **passe** | refusé : « (taille nulle) » ; idem `config.json` vide |
| index à la carte vide, aucun poids | **passe** | refusé : « index des poids illisible (ValueError : weight_map vide…) » |
| index qui nomme 1 morceau sur 2 annoncés | passe | refusé : « nombre annoncé par leurs noms différent » |
| noms de morceaux aux nombres annoncés mêlés (`-of-00002`, `-of-00003`) | passe | refusé (même motif) |
| index illisible (JSON faux), sans `weight_map`, `weight_map` liste, index liste | `JSONDecodeError`, `KeyError`, `AttributeError`, `TypeError` | **`GardeArret`** « index des poids illisible (<type> : …) » |
| index présent sous la forme d'un dossier (morceaux présents) | passe (lu comme absent) | refusé : « morceaux sans index » |
| révision donnée par un nom de branche (`refs/main`) | refusé | refusé : « dossier du cache … ≠ révision main » (essai neuf, x3) |

Colonne « v3 » rejouée contre le code de `7e23a554` (`verif_cache_v3_v4.py`, `verif-cache-v3-v4.txt`).

Hors d'atteinte, déclaré : un morceau **tronqué mais non vide** passe (l'index ne porte pas de tailles ; le vérifier demanderait
de lire les en-têtes des fichiers de poids). Comme la contre-lecture le note, `snapshot_download` ne crée le lien qu'une fois le
fichier entier ; si cela survenait, le chargement échouerait après l'ouverture : les deux bras arrêtés, motif écrit, aucune
bascule.

## 4. CLC-P3-05 : tableaux vides sous `set -u`, branche EPYC

- Script v4 : `env CUBLAS_WORKSPACE_CONFIG=:4096:8 ${ENV_CPU[@]+"${ENV_CPU[@]}"} PYTHONPATH=src …` (étape 13) et
  `git add --sparse -f -- "${a[@]}" ${ex[@]+"${ex[@]}"} …` (`pousser` : `ex` est vide dès qu'aucun fichier ne dépasse le seuil,
  c'est-à-dire à presque toutes les poussées ; même défaut que `ENV_CPU`, non nommé par la contre-lecture, trouvé par une recherche
  de `[@]` dans le script). Les autres développements `"${t[@]}"` du script portent, à leur place, sur des tableaux non vides
  (`a` après son contrôle de taille, `lot`, `CH` ; `g` et `p` seulement quand `g` n'est pas vide) ; les longueurs `${#t[@]}`
  ne sont pas changées (non éprouvées sous bash < 4.4, comme le reste). Les lignes de journal (`${ENV_CPU[*]:-…}`,
  `${ENV_CPU[*]:+ …}`) utilisent des formes à défaut, exemptes de `set -u` dans toutes les versions.
- `CPU_ESSAI` : en essai local, nom du processeur tenu pour celui de la machine (journalisé) ; ajoutée à `VARS_ESSAI`, donc
  refusée hors essai, avant toute écriture.
- **Essai** (`essai_env_cpu_v4.sh`, `essai-env-cpu-v4.txt`) : la ligne de l'étape 13, **prise telle quelle dans le fichier**, la
  commande du module remplacée par un lecteur de l'environnement du fils, jouée sous `set -u` avec `ENV_CPU` vide, à deux
  valeurs, et non défini : v4, code 0 dans les trois cas, aucun argument vide transmis à `env`, variables du fils exactes
  (`CUBLAS` seul, ou `CUBLAS`, `ATEN`, `MKL`). La forme du v3 donne les mêmes résultats **sous bash 5.2.21** : bash ≥ 4.4 ne
  distingue pas les deux formes, même pour un tableau non défini (vérifié aussi sous `BASH_COMPAT=43` et `42`).
- **Bash antérieur à 4.4 : non éprouvé.** J'ai téléchargé l'archive source de bash 4.3 (ftp.gnu.org, 7 955 839 octets,
  `afc687a2…`, dans `…/scratchpad/bash43-dl/`) pour la construire ; **la construction a été refusée par le classifieur de
  permissions** (« code venu de l'extérieur »). Je ne l'ai pas contournée. L'archive est restée non extraite, non exécutée. La
  correction repose donc sur la forme documentée (`${t[@]+…}` ne développe l'intérieur que si le tableau a au moins un élément,
  et la forme `+` est exempte de `set -u`), non sur un essai. Si la mère veut l'essai, il lui faut autoriser cette construction
  ou fournir un bash 4.3.
- `CUBLAS_WORKSPACE_CONFIG` lu **dans le processus** de l'étape A (proposition de la contre-lecture) : la répétition v4 lit
  `cublas_workspace_avant` dans `reextraction-p3-t07.json` poussé : `:4096:8`, branches EPYC et non EPYC.

## 5. CLC-P3-06 : comportement des notes 05 et 10 ; x3, x8, x9

`tests/test_t07_plancher_v3_comportement_v1.py` (4 essais, sans le miroir) :
- note 05, cas sain : étape A puis étape B par la commande sur le faux run de 7b → code 0, lecture écrite ;
- note 05, plancher décisif d'une sonde notée ouvert avec 29 directions au lieu de 30 (`lv1.ouvrir_scores` enveloppé) → **code 3
  (arrêt)**, motif « plancher décisif de <sonde> : 29 directions, 30 attendues : arrêt », aucune lecture écrite ;
- note 05, configuration de l'étape B à 31 directions, étape A jouée à 30 → code 3, motif « n_plancher 30 à l'étape A ≠ 31
  (configuration) : arrêt » ;
- note 10 : `etape-a-apres-repli` (rapport du repli transmis à l'étape A) et `etape-a` écrivent « plancher des figées : {…} ».

x3 (révision par nom de branche), x8 (sonde figée absente du fichier léger → `GardeArret` nommant la sonde, non une `KeyError`),
x9 (aucune sonde figée nommée ; une seule nommée passe) : essais neufs dans `test_t07_plancher_v3_avant_ouverture_v1.py`.

## 6. Répétition jouet v4

`scripts/repetition_jouet_variante_b_t07_v4.py` (`8b0e9590…`, fichier neuf ; la v3 reste intacte, ses aides de module importées
telles quelles), jouée au commit `be3191c9` (code sous essai : celui de `85ba2c02`, inchangé depuis), de 04:41:45 à 04:44:39 UTC,
script v4 `4b17d1f0…`. Le dépôt de l'artefact est construit par l'aide `construire_origine` de la v3, son `fausser_temoin` remplacé,
le temps de cette construction seulement, par `retirer_temoin` (fichier léger de P3 sans `tromperie-difference_moyennes-c2`,
rescellé, cité par la configuration) : déclaré.

| passage | code | durée | verdict |
|---|---|---|---|
| `normal` (processeur de la machine, Intel Xeon : `ENV_CPU` non vide) | 0 | 31,4 s | contrôle passé à l'étape 8, au journal **avant** l'empreinte, CODE-T07, le repli, la passe à blanc et l'étape A (rangs 18 < 19 < 21 < 23 < 26) ; résumé du contrôle poussé dans les traces ; deux bras établis ; environnement « CUBLAS_WORKSPACE_CONFIG=:4096:8 ATEN_CPU_CAPABILITY=avx2 MKL_CBWR=AVX2 » ; `:4096:8` lu dans le processus ; borne de taille et passe à blanc comme au v3 ; embargo tenu |
| `epyc` (`CPU_ESSAI` = « AMD EPYC 7763 64-Core Processor ») | 0 | 31,6 s | `ENV_CPU` vide sous `set -u`, aucune « unbound variable » ; journal « aucun (EPYC, processeur de P3) » ; environnement de l'étape A réduit à `CUBLAS_WORKSPACE_CONFIG`, `:4096:8` lu dans le processus ; deux bras établis ; même ordre |
| `artefact_controle` (témoin retiré) | **2** | 4,5 s | dernière ligne « ARRET : contrôle avant l'ouverture (réextraction de P3) : code 2 : REFUS : contrôle avant l'ouverture : témoin tromperie-difference_moyennes-c2 absent du fichier léger de P3 : rien n'est ouvert » ; ni empreinte, ni CODE-T07 (`code-t07.txt` absent des traces), ni branche (absente du dépôt distant), ni repli, ni ouverture journalisée, ni passe à blanc, ni run de T0.7 |
| `artefact_branche_deja_poussee` | 2 | 9,2 s | contrôle passé, puis arrêt à l'étape 10 (branche présente), sans repli |
| `decoupage` (seuil d'essai bas : `ex` non vide) | 0 | 31,7 s | fichiers découpés, recomposés, sceaux des morceaux, aucun fichier au-dessus du seuil, morceaux poussés par lots ; contrôle à l'étape 8 dans le même ordre |
| `cpu_essai_hors_essai` (tête du script jusqu'à `MESURE=`) | 2 | — | « T07 REFUS : CPU_ESSAI n'est permise qu'en essai local » ; cas sain (sans `CPU_ESSAI`) : code 0, rien écrit. Tête seule : hors essai, le script entier appellerait l'API de Vast à son premier arrêt |

Résumé et journal scellés sous des noms neufs : `repetition-jouet-v4-resume.json` (`c36839fe…`),
`repetition-jouet-v4-journal.txt` (`98412f28…`). **Borne S-13 inchangée** (aucun changement du calcul de taille ; le passage
normal la contrôle comme au v3 : planchers des figées comptés, deux sondes figées).

## 7. Essais, suites, mutations

- `tests/test_t07_plancher_v3_*` (5 fichiers) au commit final, `--basetemp` dans mon bac à sable : **92 passés, 0 sauté**, 89,7 s
  (`journal-essais-plancher-v3-v3.txt`, `61e1c104…`). L'essai qui lit la configuration v8 au chemin des pièces passe parce que
  j'ai **posé une copie** de `configuration-t07-v8.json` (`e31c7a79…`) et de son compagnon dans mon arbre, au chemin des pièces,
  **non suivie, jamais committée** (comme la contre-lecture courte).
- `tests/test_t07_*` entière au commit final : interrompue (§ 7 bis).
- **Banc v5 des modules** (`banc_mutations_plancher_v3_v5.py`, `3a318da9…` ; sortie `fd411384…` ; journal `7a1b6ee8…`) : copie
  saine d'abord (92 essais : 91 passés, 1 sauté — la configuration v8 n'était pas encore posée —, import tracé depuis la copie) ;
  **20 mutations, 20 tuées**, chacune importée de la copie à son empreinte mutée :

| id | mutation | tuée par |
|---|---|---|
| x3 | nom du dossier du cache non comparé à la révision | `test_cache_revision_par_nom_de_branche_refusee` |
| k1 | fautes de l'index hors garde | `test_cache_index_illisible_garde_arret` |
| k2 | `weight_map` vide admise | idem |
| k3 | morceaux sans index admis | `test_cache_index_qui_est_un_dossier` |
| k4 | nombre de morceaux non comparé | `test_cache_formes_partielles_refusees` |
| k5 | nombres annoncés mêlés admis | idem |
| k6 | tailles nulles admises | idem |
| k7 | index jamais lu | `test_cache_index_illisible_garde_arret` |
| x8 | sonde figée absente du fichier léger admise | `test_controle_sonde_figee_absente_du_fichier_leger` |
| x9 | aucune sonde figée nommée admise | `test_controle_aucune_sonde_figee_nommee` |
| p1 | sous-commande non aiguillée | `test_commande_controle_avant_ouverture_jouet` |
| p2 | sous-commande sans le contrôle de la réextraction | idem |
| p3 | fautes hors garde non attrapées | idem |
| p4 | cache désigné ignoré | `test_commande_controle_avant_ouverture_reel` |
| p5 | configuration lue sans les contrôles de la v4 | idem |
| p6 | refus rendu en code 0 | `test_commande_controle_avant_ouverture_jouet` |
| p7 | résumé non écrit | idem |
| c14 | appel de la note 05 retiré de `etape_b` (essais de comportement seuls) | `test_note_05_plancher_tronque_arrete_l_etape_b` |
| c17 | état des figées non affiché après le repli (idem) | `test_note_10_etat_des_figees_affiche` |
| c17b | état des figées non affiché par `etape-a` (idem) | idem |

- **Banc du script v4** (`banc_script_v4_v1.py`, `852e8e54…` ; sortie `9850dc69…` ; journal `7ed50b53…`) : copies du script,
  jouées en essai local contre des **copies nues** des dépôts de la répétition v4 (non touchés) ; copie saine d'abord pour chaque
  cas (contrôle en échec → code 2 ; tête hors essai → refus ; EPYC → code 0) :

| id | mutation | issue |
|---|---|---|
| s1 | issue du contrôle de l'étape 8 ignorée | **tuée** : le script continue, ouvre (repli, garde d'ouverture journalisée, traces poussées) et ne s'arrête qu'à la passe à blanc, **code 3** — exactement le chemin que CLC-P3-02 décrivait |
| s3 | arrêt du contrôle en code 4 | tuée |
| s4 | `CPU_ESSAI` hors de la liste des variables d'essai | tuée (tête hors essai : code 0) |
| s5 | forme du v3, `"${ENV_CPU[@]}"` | **survit** : mutant équivalent sous bash 5.2 (§ 4), attendu |

  Premier passage de ce banc (`journal-banc-script-v4-v1-premier-essai.txt`) : **mon erreur**, nom du run de 7b jouet faux dans
  le banc ; copies saines en échec (« manifeste absent de la branche de 7b »), aucune mutation jouée ; corrigé, rejoué dans un
  dossier neuf ; le premier dossier est laissé.

## 7 bis. Suite `tests/test_t07_*` entière : interrompue, déclaré

Lancée au commit final à 04:51:29 UTC, `--basetemp` dans mon bac à sable ; à 04:56:56, son dossier temporaire pesait 685 Mo et
le disque (partagé, 252 Go, 99 % occupés) n'avait plus que 563 Mo libres ; la suite entière (24 min au tour précédent) en aurait
demandé plusieurs fois plus. **Je l'ai arrêtée par son PID (10691, R10)**, pour ne pas remplir le disque commun. Avant l'arrêt :
un peu plus de 29 % des essais joués, **aucun échec** (deux `xfail` et un saut attendus ; `suite-t07-v6-interrompue.txt`). Portée : les
seuls modules changés à ce tour (`reextraction_p3_v1.py`, `lecture_v4.py`) ne sont importés, dans `src/` et `tests/`, que par
`lecture_v4.py`, `passe_blanc_v2.py`, `repli_etapes_v2.py` (régénérés à l'identique) et les cinq fichiers
`test_t07_plancher_v3_*` (recherche de leurs noms dans `src`, `tests`, `scripts`) : la suite du plancher v3 (92 passés) les
couvre ; les autres essais de T0.7 n'importent aucun fichier changé. La suite entière a passé au commit `7e23a554` (530 passés,
23 sautés, 3 `xfail`, rapport v2). Si la mère la veut au commit final, il faut d'abord libérer de la place (mes dossiers du bac à
sable, § 9.6, à retirer par elle ou sur son accord).

## 8. Fichiers et empreintes (commit final `a621dcd3b929ce3ebd615fa852d4a7f5c103071d`)

| fichier | empreinte | état |
|---|---|---|
| `src/controle_ia/t07/reextraction_p3_v1.py` | `c32696b82af620e5da07fc4ec5bbb801dc385467cbf8235b799ad28b6471eaf9` | corrigé en place (CLC-P3-03) |
| `src/controle_ia/t07/lecture_v4.py` | `42f60780e6944568e81880887a1ad87c57a520e8c7d54083b36a43c097a06d06` | régénéré (générateur v3 : tête et pied) |
| `src/controle_ia/t07/passe_blanc_v2.py` | `8e24642fd49c2d57d7f3093f4989a06a5d9110145f7d5574e5b000e48f82dba5` | régénéré, inchangé |
| `src/controle_ia/t07/repli_etapes_v2.py` | `fe08aaa14de1ca0ac88292f2c7a10ec8d591fee1e83f90c9ae38b32d0c6a2f50` | régénéré, inchangé |
| `src/controle_ia/t07/plancher_v3.py` | `c25a8822dc4a59d6d3a98b70f8b7aa92c45bbfdb571e482abf2a1a55ba440cd8` | inchangé |
| `scripts/etape_a_t07_variante_b_v4.sh` | `4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6` | neuf |
| `scripts/etape_a_t07_variante_b_v3.sh` | `a19c594d268baadebea93c8ef0ea6c9406044971a928defd8c119b238d5f6560` | intact |
| `scripts/repetition_jouet_variante_b_t07_v4.py` | `8b0e9590befafef97d96450def60138e6c835df90ee5ecf7e00a608f373737ba` | neuf |
| `tests/test_t07_plancher_v3_avant_ouverture_v1.py` | `fcfc2f53b2e13be7c8d197023d1cb0bdb0a34bc26c778861f7913a49a942a3bf` | neuf (15 essais) |
| `tests/test_t07_plancher_v3_comportement_v1.py` | `06d10b40c3a3b755ccb63b40b998f6a5874a20413f582f8eb666a353d1ad9833` | neuf (4 essais) |

Configuration v8 inchangée (canonique `0f32c6de…`, fichier `e31c7a79…`).

## 9. Réserves

1. **Bash antérieur à 4.4 non éprouvé** (§ 4) : refus du classifieur, non contourné ; correction par la forme documentée ; le
   mutant s5 survit faute d'un tel bash. L'image de l'instance (Ubuntu récente) a un bash 5 : sans effet attendu.
2. **Branche « autre révision »** de l'étape 8 (préchargement de la révision de P3) : toujours non éprouvable hors ligne (inchangée
   depuis le v3 ; P13 (i) la rend inattendue).
3. **Morceau tronqué non vide** : admis par `revision_au_cache` (§ 3) ; conséquence après l'ouverture, motif écrit, aucune bascule.
4. **Un seul `model.safetensors` sans index** : admis (forme d'un modèle d'un seul fichier). Le modèle de P3 (8 milliards de
   paramètres) est en morceaux : l'index y est exigé.
5. CLC-P3-01, CLC-P3-04, CLC-P3-07 : gestes de texte (candidat 3, ordre 7, borne calculée avant la création), non demandés à ce
   tour, non faits.
6. **Suppression récursive** : le banc v5 et le banc du script ne retirent rien (copies, `basetemp`, racines d'instance laissées
   dans mon bac à sable : 158, 157, 81 et 176 Mo ; répétition v4 : 248 Mo ; dossiers temporaires des essais : environ 0,9 Go ;
   disque libre 563 Mo à 04:57 UTC). Les bancs v1 à v4
   des tours précédents retiraient leurs propres copies par `shutil.rmtree` : déclaré, non rejoué.
7. Écart à R12 (fichiers corrigés en place) : `reextraction_p3_v1.py`, `lecture_v4.py`, comme R-2305 le déclarait au tour
   précédent ; le script et la répétition sont en fichiers neufs.
8. Un dossier `__pycache__/calibrage_gardes_v1.cpython-313.pyc` est présent dans le dossier des pièces (non suivi) ; il ne vient
   pas de mes bancs (ils jouent sous `PYTHONDONTWRITEBYTECODE=1` et `-B`) ; probablement l'import de `calibrage_gardes_v1.py` par
   la contre-lecture ; laissé en place.
9. Archive de bash 4.3 téléchargée dans le bac à sable (`afc687a2…`), non extraite, non exécutée.

## 10. Pièces (scellées, non committées, dossier `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/`)

| pièce | empreinte |
|---|---|
| `generer_lecture_v4_v3.py` | `a052cffb145b687e1758df869d40e91dc19a902dd2f793dbf3e99aefee415727` |
| `banc_mutations_plancher_v3_v5.py` | `3a318da9faad90c27a1707c0358046936522f382bf1a68d68d51a2fcd5d0907b` |
| `banc-mutations-plancher-v3-v5.json` | `fd411384560cf0c037ea8b40d86fc29a4adf5050a4092c6dbaf133701d8eceb4` |
| `journal-banc-v5.txt` | `7a1b6ee86ae94d3704e0d589614c38286a5b505ac671d859652bc5d2101e900e` |
| `banc_script_v4_v1.py` | `852e8e54faf73a3d6e5c89efae0ba2192b7a93637898ad2cad24f11ca1d95fdb` |
| `banc-script-v4-v1.json` | `9850dc69792a49069c7028efcd32f779dad4be30625fbcd65b8f91845f662ca4` |
| `journal-banc-script-v4-v1.txt` | `7ed50b533976b89eef05471da9399c6dd556fc02241ceb25a350d1823bbf15fd` |
| `journal-banc-script-v4-v1-premier-essai.txt` | `0d178c991cd06924216a2d5a35782b362c1b82411c5c5da31a0a28800c1f7343` |
| `essai_env_cpu_v4.sh` | `8be8c757fdd5d3cef804f6d25be3123fe382014c130cdb2fb8a2b990fd1363e0` |
| `essai-env-cpu-v4.txt` | `2b9aee4999cba0a7871223f8e40ffd83d78af62edf9f8ec35e7555e10d189a54` |
| `repetition-jouet-v4-resume.json` | `c36839fe2016ccea200ee5fa28c7a7116f457821d576ee93b88fbfb4d4b4f2e2` |
| `repetition-jouet-v4-journal.txt` | `98412f28c9d0dc446db86d73d51e1aa1ae3615545d242b5478e8de8bb9fb265c` |
| `journal-essais-plancher-v3-v3.txt` | `61e1c1047f354118fda9fd92c50a5143251d145909bc03d79156ee5244f46e36` |
| `verif_cache_v3_v4.py` | `68202b5e271e9725ad5499b588d08c52f0a631cc9486208669cf24b4d0b3be20` |
| `verif-cache-v3-v4.txt` | `1c5343b57fbb92e2c3d23573e91aac1da08c99c7cf12911ceb4596374750db70` |
| `suite-t07-v6-interrompue.txt` | `5f3ff1baeff34305166b359bab7c4068d155dc258ced7baefb189e3fb5324655` |

Modèle : Claude Opus 5.5 (`claude-opus-5-5`).
