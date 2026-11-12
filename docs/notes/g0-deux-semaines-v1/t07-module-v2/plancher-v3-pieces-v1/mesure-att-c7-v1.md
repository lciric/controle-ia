# Mesure de `ATT` de T0.7 au commit C7 — v1

**Verdict.** À C7 (`b4cd9953…`), clone partiel de la seule `main` fait comme celui de l'instance (étapes 2, 3 et 6 du script v4 de C7),
Python 3.13.16 : code 0, **`ATT` = `479 passed, 2 skipped, 4 xfailed, 1 warning`** (24 fichiers, 485 essais ; 785,79 s).
**Réserve (R4)** : l'avertissement dépend du noyau OpenBLAS, donc du processeur de l'hôte ; sous noyau `Zen`/`Haswell` la même suite donne
`479 passed, 2 skipped, 4 xfailed` (§ 5, § 5 bis). L'étape 6 de l'instance compare la ligne à l'octet : une valeur unique de `ATT` arrêtera l'une
des deux familles d'hôtes (arrêt sûr, avant le modèle, rien d'ouvert). Pas de rejeu sous Python 3.11 (aucun 3.11 muni des paquets).

Sous-agent neuf, mandat unique de la mère (2026-11-11) : mesurer la ligne d'essais `ATT` de T0.7 au commit C7 selon le § 11 bis
de l'ordre `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon8.md` (`24dc8df6555bac03f2ffbe8440c3c1a7b9bf2aeaf9eab3c651306a6a73fc116e`,
compagnon vérifié). Décisions lues : R-2313 à R-2316 de `registres/decisions.md` (ces lignes seulement).

## 1. Repères vérifiés avant la mesure (2026-11-11, 05:41 à 05:45 UTC, `date -u`)

- Ordre brouillon 8 : empreinte égale au compagnon (`24dc8df6…`).
- C7 = `b4cd9953d199dd8f220f5162e5868c5b00fd392d` (R-2316).
- Script `scripts/etape_a_t07_variante_b_v4.sh` lu **au commit C7** (`git show C7:…`) : `4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6`
  (égal à R-2313 et à la copie de l'arbre de travail ; **aucun compagnon `.sha256` du script sur disque**, R11 : vérifié par la liste de `scripts/`).
- Configuration v8 : `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v8.json`,
  `e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328` (égale au compagnon, et égale à l'objet de ce chemin à C7) ;
  chemin final prévu `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json` **pas encore copié** : les chemins cités sont tirés du fichier
  sous `docs/notes/…` (écart déclaré, § 6).

## 2. Bac et méthode (commande de remesure du § 11 bis, tête à C7)

Bac neuf (vide à 05:45:28 UTC) : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/mesure-att-c7/`
(noté `<bac>`) ; clone `<bac>/d`. Chaque étape est un petit script du bac qui **source, telles quelles, les lignes du script v4 de C7**
(extraites par `sed -n` de la copie `4b17d1f0…`), avec un journal horodaté `<bac>/journal-mesure.txt`. Scripts et extraits (empreintes) :

| pièce du bac | rôle | sha256 |
|---|---|---|
| `etape2.sh` | clone, puis lignes 132-169 du v4 | `9d4c2d7219ea3cc555aa775beca2d99ee46356ef815998b79cd2a74add013d64` |
| `etape2-lignes-132-169.sh` | `REGISTRES`, `MOTIFS`, `NOMMES`, `CITES`, extraction partielle, `checkout`, gardes | `d0cdb9c623f849a03da211b2a004ed16adf05fe929c2bdc5f258236622331373` |
| `etape3a.sh` | lignes 171-181 (recopie des registres nommés), liste des chemins cités, sans recopie | `629318057d22827033b84ab480dcf810c375a422580c650b8b060e31b3cf31ac` |
| `etape3-lignes-171-181.sh` | `interdit`, `apporter`, boucle des registres | `18f68eb12cf957f89854aea5cda32a43a673c59ef38f32530a9dc7930ca9b343` |
| `etape3b.sh` | lignes 171-181 puis 182-198 (cités, périmètre, journaux des jeux) | `f5d208a0537a78f38c47228ebaee884f82b5bedaaeed4f7e62b0e26dc4ce2dce` |
| `etape3-lignes-182-198.sh` | fichiers cités, périmètre C-1, journaux, `src/` `tests/` inchangés | `02bf7a42c58888cd137869892a249da1e8027fdf0d89febe115f2061c4b4e064` |
| `motifs-extraction.txt` | les 38 lignes passées à `sparse-checkout set --no-cone --stdin` | `56041134cc67c00233540bea1428c4a2d327531d0a070a3e15edb1b7c3fa272a` |
| `cites-registres.txt` | 5 chemins cités par les registres (awk de la ligne 182) | `70ff1e79a07d37132d29cbaef5070e26086578e8c4ebcd7f7341049bed3db660` |

### Étape 2 (05:46:16 à 05:46:20 UTC)

- Commande de clone (depuis `<bac>`) : `git clone -q --filter=blob:none --no-checkout --single-branch --branch main https://github.com/lciric/controle-ia-travail.git d`
  (git 2.43.0 ; aucun jeton posé : le mandataire de la session porte l'accès). Vérifié : `remote.origin.promisor = true`,
  `partialclonefilter = blob:none`, refspec `+refs/heads/main:refs/remotes/origin/main` (seule `main`) ; 3 081 commits atteignables depuis C7.
- `origin/main` = **H = `5d6ef6f567dcee5f73ec71ee67ea4cdbb1a3403d`** (deux commits après C7 : `a84be34d` CODE-T07-v2, `5d6ef6f5` pièces du candidat 5).
- Configuration lue par la ligne 150 (`git show "$S7:$CONFIG"`), `S7 = C7`, `CONFIG` = le chemin sous `docs/notes/…` ; objet à C7 contrôlé égal à `e31c7a79…`.
- Lignes 162-169 jouées : extraction partielle, `git checkout -q b4cd9953…`, gardes « tête = S7 », « C7 ancêtre de S7 », `git diff --quiet C7 S7 -- src tests`,
  « S7 ancêtre de main » : **toutes passées** (« code conforme »). `S6` (`935262b1…`) présent dans le clone (contrôlé après coup) : la ligne 168 a comparé `requirements-cpu.txt` et `requirements-gpu.txt` entre `S6` et C7, **sans différence** (aucune ligne « exigences de paquets changées » au journal).
- Résultat : 2 281 fichiers extraits, 139 Mo ; 24 fichiers `tests/test_t07_*.py`.

### Étape 3 (05:47:00 à 05:47:38 UTC)

- Registres nommés depuis H : `registres/scellements-v1.md` (`a399031d21200e3ea28b06964592a601dc3f59e6851bc60311cb7cfa4e9dc392`) et
  `registres/go.md` (`b4fa7480c071e6e9b00ceb5d42506792db780ee72040b8daca786e8c535b74db`) recopiés avec leurs compagnons ;
  `registres/scellements-v1.md.ouvertures.md`, `registres/ouvertures-p3bis-v1.md`, `registres/prealables-p3bis-v1.md` : **absents de main** (journal du script) — rien de P3-bis n'est donc recopié.
- Chemins cités (5), **classés avant toute recopie** contre les interdits du script (ligne 171), les chemins de 7a (`20261109-070232-t06-reel`) et les
  interdits du mandat (dont P3-bis, l'étiqueteur, `mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`) : **aucun ne tombe dans un interdit** ; tous présents à H avec compagnon :
  `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md`, `donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl`,
  `donnees/t07-jeux-synthetiques-v2/intention-autres-modes-v2.jsonl`, `prereg/T0.8-base-A-mots-et-cout-v1.md`, `registres/code-t07/CODE-T07-v2.json` (non suivi à C7, `d5eb0b66…`).
- `RUN6` : aucune course 7b ; tenu par l'identifiant du run de 7a pour que la ligne 183 écarte ses chemins (sans effet : aucun cité).
- Périmètre (C-1), `PERIMETRE=JD,JA` : `SCELLEMENT-JEUX-T07-JD` 1 ligne, `-JA` 1, `-JC` 0, `SCELLEMENT-CONCEPTS-T07` 0 : **conforme**, aucun arrêt ;
  journaux du script : un seul fichier, `donnees/t07-jeux-synthetiques-v2/journal-verification-v2.txt` (`58906bb4…`, conforme à son compagnon),
  commun aux deux jeux (même dossier ; compté « 1 » pour chacun).
- Contrôles : fichiers recopiés et fichiers cités par la configuration v8 (6 chemins : `diag/20261019-230011-p3-reel/sondes-figees.json`,
  `donnees/20261007-082440-t05-extraction/taches-entrainement.json`, `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz`,
  `donnees/T0.7-faits-repe-v1/facts_true_false.csv`, `donnees/T0.7-models-under-pressure-v1/training/train.jsonl`,
  `runs/20261019-230011-p3-reel/manifeste.json`) **tous égaux à leurs compagnons** ; `src/` et `tests/` inchangés (ligne 197) ;
  arbre après l'étape 3 : ` M registres/scellements-v1.md` (registre de H ≠ C7), `?? registres/code-t07/CODE-T07-v2.json` et son compagnon.

### Étape 6 (lancée à 05:48:24 UTC)

- Liste : `sha256sum tests/test_t07_*.py` → 24 fichiers, `f030758e45861732947cbf00f27350f96bba65fce331f8bb51479e283a9e9e74`
  (locale vide : `LANG`, `LC_ALL`, `LC_COLLATE` non posées ; ordre du motif identique en locale C, contrôlé).
- Commande, depuis `<bac>/d` : `TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -rsxX -p no:cacheprovider --color=no tests/test_t07_*.py --basetemp=<bac>/essais-tmp -o tmp_path_retention_policy=failed`
  (sortie `> <bac>/essais.txt 2> <bac>/essais.err`), puis `tail -n 1 | sed -E 's/ in [0-9.]+s.*$//'`.
- Interpréteur : **Python 3.13.16** (`/home/user/controle-ia-travail/.venv`), `numpy` 2.4.6, `scipy` 1.17.1, `pytest` 9.1.1, `torch` 2.14.1+cpu
  (égaux aux versions figées de `requirements-cpu.txt`) ; aucune installation éditable de `controle_ia` dans l'environnement (seul `PYTHONPATH=src` du clone).
- **Python 3.11** : `/usr/bin/python3.11` (3.11.17) est présent mais **sans les paquets** (`numpy` absent) ; aucun environnement 3.11 muni d'eux trouvé
  (dossiers d'environnements du bac à sable regardés : 3.13 seulement) : **pas de rejeu sous 3.11** ; rien installé (disque, mandat).

## 3. Résultat (essais de 05:48:24 à 06:01:32 UTC)

- **Code 0.** Dernière ligne brute : `479 passed, 2 skipped, 4 xfailed, 1 warning in 785.79s (0:13:05)`.
- **Ligne `ATT` mesurée (durée retirée par `sed -E 's/ in [0-9.]+s.*$//'`) :**

  `479 passed, 2 skipped, 4 xfailed, 1 warning`

- `essais.err` vide (0 octet) ; `git status --porcelain --untracked-files=all -- src tests` vide après les essais (`src/` et `tests/` non écrits).
- **Sautés (2)**, les mêmes qu'au § 11 bis, tous deux dus au clone à branche unique (comme sur l'instance) :
  - `tests/test_t07_lecture_v1.py:504` : « branche origin/prep/t06-candidat8-v1 non récupérée : essai d'égalité sauté (déclaré) » ;
  - `tests/test_t07_lecture_v2.py:911` : « commit 061ac380 absent de ce clone : essai d'égalité sauté (déclaré) ».
- **Échecs attendus (4)**, les mêmes qu'au § 11 bis :
  - `tests/test_t07_corrections_cl1_v1.py::test_CT01_action_sans_caractere_de_mot_temoin_en_echec_sans_arret` — règle de CT-01 remplacée par C20-01 (R-2098) ;
  - `tests/test_t07_corrections_cl1_v1.py::test_CT11_dates_du_journal_non_decroissantes` — cas sain hors forme depuis D-3 (R-2103) ;
  - `tests/test_t07_lecture_v2.py::test_journal_cas_sain_lignes_et_refus_lus` — interprétation tolérante retirée par D-3 (R-2103) ;
  - `tests/test_t07_repli_etapes_v1.py::test_garde_refusee_rien_calcule_puis_relance` — `SCELLEMENT-CONCEPTS-T07` devenue permise (R-2158), « DID NOT RAISE ».
- Aucun échec non attendu, aucune erreur, aucun `XPASS`.
- **Un avertissement (neuf par rapport au § 11 bis, qui n'en avait aucun)** : `tests/test_t07_plancher_v3_notation_v1.py::test_refus_et_cas_sains`,
  `src/controle_ia/t07/plancher_v3.py:139: RuntimeWarning: invalid value encountered in matmul` (ligne `S = A @ m["W"] + m["b"]`). Voir § 5 : il **dépend du processeur**.

### Compte recoupé (collecte seule, 06:02:10 UTC : `TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src <py> -m pytest --collect-only -q -p no:cacheprovider --color=no tests/test_t07_*.py`, code 0, « 485 tests collected »)

| fichier | essais | issues |
|---|---:|---|
| `tests/test_t07_code_t07_v1.py` | 16 | passés |
| `tests/test_t07_controle_jeux_v1.py` | 14 | passés |
| `tests/test_t07_corrections_cl1_v1.py` | 16 | 14 passés, 2 `xfail` |
| `tests/test_t07_corrections_cl20_v1.py` | 4 | passés |
| `tests/test_t07_donnees_p3_v1.py` | 4 | passés |
| `tests/test_t07_journal_p3bis_d3_v1.py` | 20 | passés |
| `tests/test_t07_lecture_v1.py` | 139 | 138 passés, 1 sauté |
| `tests/test_t07_lecture_v2.py` | 63 | 61 passés, 1 sauté, 1 `xfail` |
| `tests/test_t07_option_c_concepts_v1.py` | 16 | passés |
| `tests/test_t07_ordre_des_lignes_v1.py` | 2 | passés |
| `tests/test_t07_ouvrir_reel_concepts_v1.py` | 3 | passés |
| `tests/test_t07_passe_blanc_v1.py` | 15 | passés |
| `tests/test_t07_plancher_v2_fonction_v1.py` | 29 | passés |
| `tests/test_t07_plancher_v2_lecture_v1.py` | 12 | passés |
| `tests/test_t07_plancher_v3_avant_ouverture_v1.py` | 15 | passés |
| `tests/test_t07_plancher_v3_comportement_v1.py` | 4 | passés |
| `tests/test_t07_plancher_v3_lecture_v1.py` | 21 | passés |
| `tests/test_t07_plancher_v3_notation_v1.py` | 20 | passés (1 avertissement) |
| `tests/test_t07_plancher_v3_reextraction_v1.py` | 32 | passés |
| `tests/test_t07_repli_etapes_v1.py` | 9 | 8 passés, 1 `xfail` |
| `tests/test_t07_repli_recalcul_v1.py` | 4 | passés |
| `tests/test_t07_repli_v1.py` | 4 | passés |
| `tests/test_t07_sondes_neuves_v1.py` | 18 | passés |
| `tests/test_t07_tirages_degeneres_v1.py` | 5 | passés |
| **total (24 fichiers)** | **485** | **479 + 2 + 4** |

Recoupement : les 17 fichiers de la mesure du brouillon 5 (tête `2c8ab779`) sont **inchangés à C7** (`git diff --name-only 2c8ab779 b4cd9953 -- <les 17>` vide)
et font 352 essais, avec les mêmes 346 passés, 2 sautés, 4 `xfail` ; les sept fichiers neufs font 133 essais, tous passés :
`plancher_v2_*` 41, `plancher_v3_*` **92** (égal à R-2313 et R-2315).

## 4. Pièces et empreintes

| pièce | chemin | sha256 |
|---|---|---|
| sortie complète des essais (`essais.txt`, 21 lignes) | `mesure-att-c7-sortie-v1.txt` (ce dossier), copie de `<bac>/essais.txt` | `20423d754dc94aa7a50bd0df7b0112f564abee8c41e6f7afabb07d4643f7faf9` |
| liste des fichiers d'essais (`sha256sum tests/test_t07_*.py`, 24 lignes) | `mesure-att-c7-liste-v1.txt` (ce dossier), copie de `<bac>/essais-liste.txt` | `f030758e45861732947cbf00f27350f96bba65fce331f8bb51479e283a9e9e74` |
| erreurs des essais | `<bac>/essais.err` (vide) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| sauts et échecs attendus (`grep -E '^(SKIPPED\|XFAIL\|XPASS\|FAILED\|ERROR)'`) | `<bac>/essais-sauts.txt` (6 lignes) | `c19283515dc200667236fe2f6e9fd90c82708a9b7f06a39af1b657fa4134f107` |
| collecte | `<bac>/collecte.txt` | `25e3809fcb55f63206d05fd71bf3e6e2e275da68d0ccd7927a8aa5072987261f` |

La liste diffère de celle du § 11 bis (`bd49a367…`, 17 fichiers) par les sept fichiers neufs seulement (cf. ci-dessus).

## 5. Réserve : l'avertissement, donc la ligne `ATT`, dépend du processeur de l'hôte (R4)

Diagnostics hors mesure (06:02:27 à 06:03:32 UTC ; aucun ne modifie `src/` ni `tests/`, contrôlé après chacun) :

- rejeu de `tests/test_t07_plancher_v3_notation_v1.py::test_refus_et_cas_sains` seul, deux fois : `1 passed, 1 warning` ; du fichier entier : `20 passed, 1 warning` (stable ici) ;
- même essai, noyau OpenBLAS forcé par `OPENBLAS_CORETYPE` (numpy 2.4.6 embarque `scipy-openblas64` 0.3.31.188.0, `DYNAMIC_ARCH`) :

| `OPENBLAS_CORETYPE` | noyau effectif (`scipy_openblas_get_corename64_`) | issue |
|---|---|---|
| non posé (cette machine : Intel Xeon @ 2.10GHz, AVX-512) | `SkylakeX` | `1 passed, 1 warning` |
| `SkylakeX` | `SkylakeX` | `1 passed, 1 warning` |
| `Cooperlake` | (non relevé) | `1 passed, 1 warning` |
| `Haswell` | `Haswell` | `1 passed` |
| `Zen` | `Haswell` | `1 passed` |
| `Sandybridge` | (non relevé) | `1 passed` |
| `Prescott` | (non relevé) | `1 passed` |

- Cause probable (lecture du code, non éprouvée plus loin) : l'essai met `np.inf` dans une action (`mauvais[2][0, 0] = np.inf`) et attend le refus
  « non fini » ; le produit `A @ m["W"]` (ligne 139) est fait par OpenBLAS, dont les noyaux AVX-512 lèvent le drapeau « invalid » (vraisemblablement
  `inf × 0` dans des tuiles complétées de zéros), que numpy change en `RuntimeWarning` ; les noyaux AVX2 et plus anciens ne le lèvent pas. Le refus
  lui-même tient dans tous les cas (l'essai passe).
- **Conséquence pour l'instance** (étape 6 du script v4 : `[ "$c" = 0 ] && [ "$DL" = "$ATTENDU" ]`, sinon arrêt de code 2, avant la descente du modèle,
  rien d'ouvert) : avec `ATT = 479 passed, 2 skipped, 4 xfailed, 1 warning`, un hôte dont OpenBLAS choisit un noyau AVX2 (par exemple un EPYC Zen 2 ou
  Zen 3, noyau `Haswell`) donnerait vraisemblablement `479 passed, 2 skipped, 4 xfailed` et l'instance s'arrêterait ; à l'inverse, une valeur sans
  avertissement arrêterait un hôte AVX-512 (Intel récent ; un EPYC Zen 4 vraisemblablement aussi, **non vérifié** : choix du noyau par OpenBLAS pour
  Zen 4 non éprouvé ici). Le processeur de l'instance n'est connu qu'à sa création (le script l'écrit au journal, étape 1). Aucune correction n'est
  tentée ici (mandat) ; le choix revient à la mère (nœud si le code, le script ou l'ordre doivent changer).
- Rejeu diagnostic de la **suite entière sous `OPENBLAS_CORETYPE=Zen`** : voir § 5 bis.

## 6. Écarts à l'instance, déclarés

1. **Tête au commit C7** (S7 n'existe pas encore ; mandat et brouillon 7, R-2306 : S7 en hérite par P9) ; gardes de l'étape 2 jouées avec `S7 = C7`.
2. **Configuration** : `CONFIG` = `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v8.json` (présente à C7, `e31c7a79…`),
   non le chemin final `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json` (pas encore copié) ; les six chemins cités en sont tirés par la ligne 150 du v4.
3. **Aucun jeton** : clone par la commande du mandat, sans l'aide d'identification du script (le mandataire de la session porte l'accès).
4. **Étape 3** : registres de `main` à **H = `5d6ef6f5`** (heure de la mesure) ; à la création, `main` aura avancé (S7, lignes de scellement) et pourra
   citer d'autres fichiers ; `RUN6` (aucune course 7b) tenu par l'identifiant de 7a pour écarter ses chemins (sans effet, aucun cité) ; classement
   préalable des cinq chemins cités contre les interdits du script et du mandat (aucun touché). Les fonctions `j` et `arret` sont celles de mes
   scripts (journal du bac ; `arret` sort au lieu de `fin_instance`).
5. **Étape 4** (sortie de 7b) et **étape 5** (environnement `requirements-gpu.txt`) **non jouées** ; interpréteur local **Python 3.13.16** (`torch` 2.14.1+cpu)
   au lieu de Python 3.11 et de la construction carte de `torch` sur l'instance ; **pas de rejeu sous 3.11** (aucun 3.11 muni des paquets ; rien installé).
   `requirements-gpu.txt` à C7 inclut `requirements-cpu.txt` (même `numpy` 2.4.6 ; OpenBLAS embarqué vraisemblablement le même dans la roue pour 3.11, **non vérifié** ; le choix du noyau suit le processeur : § 5).
6. **Matériel** : Intel Xeon @ 2.10GHz avec AVX-512 (noyau OpenBLAS `SkylakeX`) ; celui de l'instance est inconnu (§ 5).
7. **Locale** : `LANG`, `LC_ALL`, `LC_COLLATE` non posées ; l'ordre de `tests/test_t07_*.py` est le même en locale C (contrôlé).
8. **Commande des essais** : celle du mandat, égale à l'étape 6 du v4 aux chemins près (interpréteur, `--basetemp=<bac>/essais-tmp`).
9. **Extraction** : par les motifs du script, le clone contient des fichiers de code et des notes dont le nom porte « p3bis » (scripts, essais, modules,
   12 notes sous `docs/notes/g0-deux-semaines-v1/`) et trois documents `prereg/*etiqueteur*` ; **aucun n'a été ouvert** (seul
   `tests/test_t07_journal_p3bis_d3_v1.py` a été exécuté, comme membre de la suite) ; aucun `diag/`, `runs/` ni `donnees/` de 7a, de 7b ou de P3-bis
   n'est dans le clone (liste des fichiers extraits contrôlée : seuls ceux de P3, de T0.5 et des jeux de T0.7).
10. **Diagnostics en plus de la mesure** (§ 3, collecte ; § 5 ; § 5 bis) : ils n'entrent pas dans la ligne `ATT`.
11. **Script v4 sans compagnon `.sha256`** sur disque (empreinte relevée à C7, égale à R-2313).

## 5 bis. Rejeu diagnostic de la suite entière sous noyau `Zen` (hors mesure ; 06:03:59 à 06:16:43 UTC)

- Commande : `OPENBLAS_CORETYPE=Zen TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -rsxX -p no:cacheprovider --color=no tests/test_t07_*.py --basetemp=<bac>/essais-tmp-zen -o tmp_path_retention_policy=failed`, depuis `<bac>/d` (même clone, même tête C7).
- Résultat : code 0, dernière ligne brute `479 passed, 2 skipped, 4 xfailed in 761.96s (0:12:41)`, soit, durée retirée, **`479 passed, 2 skipped, 4 xfailed`** ;
  aucun avertissement ; lignes `SKIPPED`/`XFAIL` **identiques à l'octet** à celles de la mesure (`c1928351…`) ; erreurs vides ; `src/` et `tests/` non écrits.
- Pièces (bac, non versées) : `<bac>/diag-zen.txt` `ba01a3c0b9be2753fbd980d471706a2232886a86159f0b06f367504617c67f00`, `<bac>/diag-zen.err` vide.
- Lecture : la seule différence entre noyaux est l'avertissement de § 5 ; la ligne vaut `479 passed, 2 skipped, 4 xfailed, 1 warning` sous un noyau
  AVX-512 (`SkylakeX`, celui de cette machine) et `479 passed, 2 skipped, 4 xfailed` sous le noyau `Haswell` (choisi pour `Zen`).

## 7. Heures (`date -u`)

Repères 05:41:16 ; bac 05:45:28 ; clone 05:46:16-05:46:17 ; étape 2 finie 05:46:20 ; étape 3 05:47:00-05:47:38 ; essais 05:48:24-06:01:32 (785,79 s) ;
collecte 06:02:10 ; diagnostics de l'avertissement 06:02:27-06:03:32 ; rejeu `Zen` 06:03:59-06:16:43. Journal de la mesure :
`<bac>/journal-mesure.txt` (48 lignes, arrêté à 06:17:12 UTC : `946b623283ef0ea61ee0968dcd4d4ab7fbac61bcf01da0adf56aa2b6c946994f`).

## 8. Fin

Aucun commit, aucune poussée, ni dans le dépôt de travail ni dans le clone ; aucun appel de modèle, aucune dépense ; aucun fichier interdit lu ;
aucune suppression. Le clone et les dossiers temporaires restent dans le bac (224 Mo ; disque libre 2,0 Go à la fin). Rapport, sortie et liste
scellés par `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>` ; non committés.
