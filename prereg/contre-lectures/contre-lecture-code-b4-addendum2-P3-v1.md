# Contre-lecture du code — addendum 2 de P3 — module v2 face au brouillon 4

**Verdict : scellable après corrections.** Le module v2 applique le brouillon 4 règle par règle ; je n'y trouve aucun
défaut de calcul, de réserve, de verrou ni de garde. Les corrections portent sur le texte (précision 2, phrase de
durée) et sur les tests (deux formes jamais présentes, descriptifs jamais vérifiés). Aucun constat critique ni majeur.

| id | gravité | constat (une ligne) |
|---|---|---|
| CV2-01 | mineur | Précision 2 : présentée comme « déjà appliquée » et sans effet ; c'est une règle nouvelle (changement 6), qui peut taire le déclencheur 3 alors que la part ponctuelle existe |
| CV2-02 | mineur | Tests : `cout_multiplication` et `cout_milliers_espace` ne figurent dans aucun jeu synthétique ; retirer l'une d'elles de R_sf passe les 118 tests |
| CV2-03 | mineur | Tests : douze descriptifs écrits du texte, la clé `consigne` hors déclencheur et la phrase d'arrêt ne sont vérifiés par aucun test (mutants survivants, séparés sur le run « sain ») |
| CV2-04 | mineur | Phrase proposée pour `<<DUREE_MESUREE>>` : total juste, mais « 4,8 s d'imports » est un processus entier, « 683 Mo » est 683 Mio (≈ 716 Mo), et la phrase ne cite ni chemin ni empreinte (R6) |
| CV2-05 | information | Bords et types non éprouvés par les tests, sans effet sur le run réel : gardes 4, 6, 9, 13 ; borne décisive de B2 égale à 0 ; « instable » à borne haute nulle ; recommandation sur une conclusion sans contrôle |
| CV2-06 | information | `nombre_de_controles` : « lus » compte les contrôles « non lus » ; le texte dit « 9 lus au plus » |
| CV2-07 | information | Déclencheur 2 : l'ordre entre « sans objet » et « E_sf non calculable » n'est pas écrit (le module rend « sans objet ») |
| CV2-08 | information | Sept « lectures d'application » des notes ne sont pas au texte ; trois mériteraient une ligne (garde 7 sur P3-P3 en échec, forme de la recommandation, libellé de D nul) |
| CV2-09 | information | Les tests importent aussi `committer` et `git` de `tests/conftest.py`, que le texte ne cite pas |
| CV2-10 | information | Le run source en mémoire n'a pas d'instantané (la précision 8 ne couvre que [L]) ; un [SF] sans `principales` arrête par une `KeyError` nue |
| CV2-11 | information | Garde R1 par crochet d'audit : faux positifs sous `shutil.rmtree` (noms relatifs à un descripteur) ; la garde de la revue précédente, réutilisée par le rédacteur, a la même faiblesse ; aucune donnée touchée |

En bref : campagne indépendante de 230 mutants, suite entière sur chacun : 200 tués, 30 survivants dont 5
équivalents ; les 25 autres sont séparés de la base par un cas construit (CV2-02, CV2-03, CV2-05). Rejeu du script du
rédacteur : 117 tués sur 117, identique à son résultat, mutant par mutant. Pannes : chaque artefact s'arrête avec un
motif écrit, rien n'est écrit avant le manifeste ; une seule panne passe sans arrêt (run source modifié en mémoire après la garde 7, CV2-10). Durée : 5,1 à
6,3 s pour la commande complète (mes quatre mesures), conforme au total du rédacteur. R1 : 0 refus sur tous les
lancements retenus ; 21 refus sur un lancement de pannes écarté, tous des faux positifs de ma garde (CV2-11), sans aucun
accès.

## Constats détaillés

### CV2-01 (mineur) — Précision 2 : règle nouvelle, non « déjà appliquée » ; elle peut taire le déclencheur 3

- **Texte.** Brouillon 4, l. 434-435 : « Règles déjà appliquées par le module là où le texte se taisait […] ; aucune ne
  change un nombre, une réserve ni le verrou ». L. 439, précision 2 : « Déclencheur 3 : « non calculé » si la part n'est
  pas calculée (`E0` = 0 ou part en échec) ». Critères, audit, point 3, l. 423-424 : « part ponctuelle hors de
  [−1 ; 1] […] ; « non calculé » si `E0` = 0 (écrit) ». Traitement, section « Module » : « Aucun autre changement de
  règle ».
- **Code.** v2 l. 1084-1085 : branche ajoutée (`elif pf["part"]["etat"] != CALCULE` → « non calculé »). Le module v1
  (`module/audit_verdict_p3_v1.py`, `0b991450…`) lisait `D / E0` dès que `E0` ≠ 0, même si la part était en échec. La
  revue texte v1 (CC-texte-06 b) avait décrit le v1 comme « « non calculé » si la part n'est pas calculée » ; le
  brouillon 4 l'a transcrit en « `E0` = 0 ou part en échec ». Le v2 applique bien le brouillon 4 : la différence v1 → v2
  est réelle et limitée à ce cas (différentiel complet relu : six changements, aucun autre).
- **Cas.** `outils/precision2_v1_v2.py` (journal `journaux/precision2-v1-v2.log`) : d_∅ = 1 (dix tâches), −1 (dix), 2
  (une) ; d_sf = d_∅ − 0,5. `D` = 0,5, `E0` = 2/21, part ponctuelle ≈ 5,25 ; 617 tirages sur 10 000 où `E0(b)` = 0, donc
  part en échec (garde 15). v1 : déclencheur 3 vrai, « addendum 2 suspect de propreté ». v2 : « non calculé », déclencheur
  faux, aucune phrase.
- **Portée.** Aucune dans ce run : `E0` de P3-P1 est loin de 0 et un tirage où `E0(b)` vaut exactement 0 n'y arrive
  pas. Mais la règle affaiblit l'audit R4 dans un cas où sa grandeur (la part ponctuelle) existe : l'échec de la garde 15
  porte sur l'intervalle de la part, pas sur `D / E0`.
- **Correction.** Deux options ; la session tranche.
  (a) Garder le v2 ; au texte, sortir la précision 2 de la liste « déjà appliquées » (« règle du brouillon 4, appliquée
  par le module v2 ; elle rend « non calculé » le déclencheur 3 quand la part est en échec ») ; au traitement, noter le
  changement 6.
  (b) **Recommandée** (confiance moyenne) : écrire « non calculé si `M5` n'est pas calculée ou si `E0` = 0 », comme le
  v1 et comme l'audit, point 3 ; retirer le changement 6 du module (et adapter `test_garde_15_degenerescences_de_la_part`
  et `test_audit_part_hors_bornes_construit_et_sain`, qui fixent aujourd'hui « non calculé »).

### CV2-02 (mineur) — Deux formes absentes de tous les jeux de tests

- **Texte.** M2, l. 181-183 : « « Sans aucune forme » : les cinq colonnes fausses » ; M3, l. 185 : `R_sf` (au moins une
  forme). Tests, l. 523-524 : « la restriction retire exactement les actions à forme (recompte indépendant) ».
- **Code.** `_a_forme` m. 413-418 (juste : boucle sur les cinq `FORMES`).
- **Problème.** Les jeux synthétiques des tests (`PROBAS`, scénarios) ne posent que `cout_plusieurs_nombres`,
  `cout_intervalle` et `cout_suffixe_k`. Aucun ne porte `cout_multiplication` ni `cout_milliers_espace`. Les mutants
  REGLE-01 (R_sf sans `cout_milliers_espace`) et REGLE-02 (sans `cout_multiplication`) passent les 118 tests. Le
  recompte indépendant et le recalcul des bornes ne le voient pas, faute d'action qui porte ces formes. Le texte ([V]
  cité l. 99-100, 108-109) ne dit pas que ces deux formes sont absentes du run réel chez l'honnête, le témoin et la
  mention : je ne peux donc pas déclarer ces mutants équivalents pour le run réel.
- **Cas.** `outils/separer_survivants.py::test_separation_sur_un_scenario[REGLE-01]` et `[REGLE-02]` : run « sain » des
  tests où l'honnête, le témoin et la mention portent aussi ces deux formes (4 % chacune) : E_sf, D, M7, M9 et les
  écarts diffèrent entre base et mutant.
- **Correction.** Ajouter ces deux formes à un scénario passé par `test_bornes_recalculees_hors_du_module` et par
  `test_restriction_retire_exactement_les_actions_a_forme` (par exemple « sain » : honnête et témoin, 2 % chacune).

### CV2-03 (mineur) — Descriptifs écrits jamais vérifiés par un test

- **Texte.** M3 (comptes propres, l. 188-190), M5 (part et son intervalle, l. 202-205), M6 (comptes et quantiles,
  l. 212-213), M8 (sens de l'écart, l. 223), M9 (table par tâche, l. 226-227), M10 (descriptifs à la distance basse,
  l. 243-244) ; critères, ligne de l'audit (l. 403 : « cité et soumis à Lazar » seulement si le déclencheur est vrai) ;
  ligne d'arrêt (l. 404).
- **Problème.** Ces sorties sont rapportées « sans verdict » mais écrites ; un nombre faux y serait cité au verdict
  complété comme descriptif. Survivent (118 tests passés) : DESC-01 (nulles d'origine), DESC-03 (comptes de `E_-f` pris
  sur `R_sf`), DESC-04 (intervalle de la part), DESC-05 (valeur de la part = `E0 / D` ; seule la part nulle est
  vérifiée), DESC-07 (tâches où `d_∅ > log10 3` comptées contre 0,48), DESC-08 (quantiles de `d_sf` pris sur `d_∅`),
  DESC-09 (quantile 0,9 retiré), DESC-10 (`d_∅ ≥ 0` au lieu de `> 0`), DESC-11 (classement de M8 contre log10 3),
  DESC-12 et DESC-13 (table M9), DESC-14 (aire au seuil à la distance basse), V2-14 (clé `consigne` écrite sans
  déclencheur), PHRASE-08 (phrase d'arrêt : le test la compare à la constante du module, pas au texte).
- **Cas.** `separer_survivants.py` : sur le run « sain », chaque mutant change au moins un chemin de la sortie (liste au
  journal) ; DESC-10 sur une différence de tâche exactement nulle ; PHRASE-08 face à la cellule du texte.
- **Correction.** Étendre `ecarts_au_recalcul` (recalcul hors du module) aux descriptifs : part (valeur et intervalle,
  tirages non dégénérés), comptes et quantiles de M6, comptes propres de M3 et de chaque `E_-f`, classement de M8,
  colonnes de M9, `A_seuil` et `A_80` à la distance basse ; vérifier `consigne` à `None` sans déclencheur ; écrire la
  phrase d'arrêt à la main dans les tests.

### CV2-04 (mineur) — Phrase de durée

- **Texte.** Plan, point 9, l. 380 : `<<DUREE_MESUREE>>`. Proposition des notes (l. 259-262) : « environ 5,5 s […] dont
  environ 4,8 s d'imports et 0,4 à 0,6 s pour la fonction pure ; mémoire maximale ≈ 683 Mo ».
- **Ce qui est juste.** Le total : mes quatre mesures, sur un dépôt jouet de taille réelle construit par mon propre
  outil, donnent 5,46 ; 6,26 ; 5,37 ; 5,10 s (machine chargée par d'autres sessions, charge 1,9 à 2,3).
- **Ce qui ne l'est pas.** « 4,8 s d'imports » est la durée murale d'un processus qui ne fait qu'importer (démarrage,
  imports, sortie) : 4,05 à 4,64 s chez moi ; les imports eux-mêmes prennent 3,06 à 3,49 s, dont 2,4 s pour
  `harnais.validation_reelle` (qui tire la bibliothèque de calcul tensoriel, pour la seule `exiger_code_cite`). « 683 Mo »
  vient de `ru_maxrss / 1024` : ce sont 683 Mio (699 220 Kio chez moi), soit ≈ 716 Mo. Fonction pure : 0,66 à 0,79 s chez
  moi (0,43 à 0,64 s chez le rédacteur). Enfin la phrase ne renvoie à aucun fichier de mesure (R6).
- **Correction proposée.** « environ 5,5 s pour la ligne de commande complète (de 5,1 à 6,5 s sur huit mesures, deux
  mesureurs ; processus séparé, dépôt jouet à taille réelle : 60 tâches, 4 conditions, 10 pas, 600 actions par condition,
  430 sondes ; 10 000 tirages), dont 3 à 3,5 s d'imports (surtout la bibliothèque de calcul tensoriel, tirée par
  `harnais.validation_reelle`) et 0,4 à 0,8 s pour la fonction pure ; mémoire maximale ≈ 683 Mio (≈ 716 Mo) ; mesures :
  `<chemin du fichier versé>` (sha256 `<…>`) ».

### CV2-05 (information) — Bords et types non éprouvés, sans effet sur le run réel

Chacun est séparé de la base par un cas construit (`separer_survivants.py`) ; aucun ne peut l'être par une entrée du
run réel, pour la raison donnée. Un test par ligne suffirait.

| mutant | règle (texte) | cas qui sépare | pourquoi sans effet sur le run réel |
|---|---|---|---|
| G4-02 | garde 4, S2 = premier commit qui ajoute le compagnon (l. 469-470) | compagnon ajouté avant N-025, retiré, rajouté après : base « non descendant de N-025 », mutant passe | le compagnon n'est ajouté qu'une fois (R12) |
| G6-02 | garde 6 au lancement (l. 480) | fiche des épisodes sans ses fichiers, gardes 1 à 5 simulées passées : base `GardeArret : garde 6`, mutant `KeyError` nue | [E] est épinglée par la garde 2 et lisible ; dans les deux cas arrêt avant le manifeste, rien d'écrit |
| G9-01, G9-02 | garde 9, types de `calculable` et des comptes (l. 491) | [L] du code gelé avec `calculable` = 1 ou `n_taches` en flottant : base arrête (garde 9), mutant passe | [L] est écrite par le code gelé et épinglée (garde 2) |
| G13-02, G13-04 | garde 13, `bas > haut`, `bas > Q` (l. 502) | `bas` = `haut`, `bas` = `Q` : base passe (égalité permise), mutant arrête | égalités exactes de flottants issus de calculs distincts |
| SEUIL-11 | réserve B2, borne décisive « ne l'était pas » (≤ 0) (l. 300-301) | borne décisive exactement 0, borne basse de E_sf 0,05 : base réserve, mutant non | bornes basses décisives −0,5704 et −0,5404 (l. 106-107) |
| SEUIL-33 | M5, « instable » si l'intervalle de E0 contient 0, bornes comprises (l. 206-207) | borne haute de E0 exactement 0 (matrice de tirage écrite) : base « instable », mutant non | égalité exacte improbable ; descriptif |
| REGLE-30 | recommandation « contrôles passés » pour une conclusion visée par un contrôle lu (critères, l. 400) | ligne « critères 2 et 3 » : le mutant écrit « contrôles de l'addendum 2 passés » pour `P3-P3/<p>` et `T1/<p>`…, qu'aucun contrôle ne vise | dans ce run, les trois conclusions établies (P3-P1, nul/<p>) sont toutes visées |

### CV2-06 (information) — « lus » compte les « non lus »

Texte, plan, points 7 et 8 (l. 368-373) : « `nombre_de_controles` (écrits, lus, sans objet) » ; « 9 lus au plus ».
Code : `_compte` m. 1120-1124 : « lus » = tout contrôle non « sans objet », « non lus » compris, rapportés à part
(`dont_non_lus`). Dans ce run, le module écrira toujours 9 lus. Rien de faux, mais un lecteur peut lire « 9 lus » comme
neuf contrôles effectivement lus. Correction : au texte, « lus (dont « non lus ») », ou renommer la clé.

### CV2-07 (information) — Ordre du déclencheur 2

Texte : audit, point 2 (l. 421-422) et précision 1 (l. 437-438) : « non calculé » si un intervalle décisif n'est pas lu
(« examiné avant « sans objet » ») ; « non calculé » aussi si un E_sf est non calculable — sans dire si ce dernier cas
passe avant ou après « sans objet ». Code m. 1065-1071 : « sans objet » d'abord. Cas : un intervalle décisif conforme et
un E_sf non calculable donnent « sans objet » ; l'autre lecture donnerait « non calculé ». Sans effet sur
`declencheur`. Correction : « (examiné après « sans objet ») ».

### CV2-08 (information) — Lectures d'application des notes, absentes du texte

Notes v2, l. 145-157 : sept règles appliquées là où le brouillon 4 se tait ; aucune ne change un nombre ni une réserve.
Trois mériteraient une ligne aux précisions, comme CC-texte-06 l'a fait pour les dix autres : (1) garde 7, entrée
P3-P3/<p> en échec dans [L] : aire et quantile non comparés (m. 861-863) ; (6) forme de la recommandation, avec la clé
`consigne` (m. 1156-1169) ; (7) libellé de D nul (m. 300). Les quatre autres découlent du texte.

### CV2-09 (information) — Imports des tests

Texte, l. 64 et l. 383 : les tests importent les aides de `tests/test_premier_test_ia_lecture.py`. Tests v2, l. 83 :
`from conftest import committer, git` (`tests/conftest.py`, arbre gelé, `a1bbfcc9…`). Sans risque ; à écrire au texte.

### CV2-10 (information) — Run source en mémoire ; [SF] sans `principales`

- Précision 8 (l. 446-447) : instantané de [L] seulement. Panne : coûts du run source doublés en mémoire après la garde 7
  (`test_pannes_v2.py::test_run_source_modifie_en_memoire_pendant_l_analyse`) : passage sans arrêt (E_sf inchangé par
  construction, écarts M8 changés à l'arrondi). Le module ne modifie pas ses entrées (test
  `test_determinisme_et_entrees_intactes`) ; seul un autre code du même processus le pourrait. Suggestion : une
  empreinte des colonnes lues, prise à la garde 7 et revérifiée à la fin, comme pour [L].
- [SF] sans `principales["enjeux"]` : `KeyError` nue (m. 410), pas une `GardeArret`. Avant le manifeste : arrêt, rien
  d'écrit, mais sans motif « ARRÊT ». Hors d'atteinte sur le run réel ([SF] épinglé).

### CV2-11 (information) — Garde R1 par crochet d'audit : faux positifs

L'événement d'audit `open` ne transmet pas le descripteur de dossier (`dir_fd`). Sous `shutil.rmtree`, les entrées sont
ouvertes par un nom relatif à ce descripteur ; une garde qui les résout contre le dossier courant (la racine du dépôt)
voit `donnees`, `diag`, `runs` du dépôt. C'est arrivé une fois : second lancement de mes pannes, quand pytest a vidé mon
`--basetemp` (laissé par le premier) ; 21 refus, piles `tmpdir.getbasetemp → rm_rf → shutil.rmtree → _rmtree_safe_fd`
(`journaux/r1-pannes-passage2-faux-positifs.jsonl`). Rien n'a été ouvert : la garde lève avant l'accès, et la cible
réelle était mon dépôt jouet. J'ai écarté ce lancement, écrit `garde_r1_v2b.py` (contrôle de la cible de haut niveau de
`rmtree`, noms relatifs émis depuis `_rmtree_safe_fd` non interprétés), éprouvée (14 épreuves), puis relancé : 0 refus.
La garde `revue-mutants/garde_r1_revue.py`, que le rédacteur a réutilisée, a la même faiblesse (faux positifs, pas faux
négatifs) ; ses « 0 refus » restent valides, aucun de ses lancements ne vidant un dépôt jouet dans le processus gardé.

## Cadre

- Contre-lecteur : sous-agent neuf (R2). Je n'ai écrit ni le texte, ni le module, ni ses tests, ni les notes, ni les
  contre-lectures ou traitements précédents. Date : 2026-10-20 (UTC), de 13:36 à 17:00.
- Dossier de travail, seul endroit écrit : `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum2-p3/revue-v2/`
  (noté `revue-v2/`). Originaux jamais modifiés ; chaque mutant est une copie (`revue-v2/mutants/<id>/`).
- Dépôt de travail en lecture seule : git en lecture ; lancements avec `python -B`, `PYTHONDONTWRITEBYTECODE=1`,
  `-p no:cacheprovider`, `--basetemp` et `TMPDIR` sous `revue-v2/tmp/` (supprimé à la fin), depuis la racine du dépôt, `PYTHONPATH=src`,
  interpréteur de la consigne (Python 3.11.17, numpy 2.4.6, pytest 9.1.1). Aucun fichier de cache créé ni modifié dans
  le dépôt (liste des caches identique au début et à la fin) ; `strace -f` sur le passage de base : 0 ouverture en
  écriture sous le dépôt, dans aucun processus. Les changements de `git status` pendant la revue (`registres/go.md`,
  `registres/decisions.md`, puis commits jusqu'à `0760313`) sont ceux de la session ; `src/` et `tests/` restent égaux
  au commit cité `7a54d43`.
- R1 : tables synthétiques seulement. Je n'ai ouvert ni `donnees/`, ni `diag/`, ni `runs/`, ni `traces/` du dépôt, ni
  `prereg/P3-consignes-v1.md`, ni aucun fichier `textes-actions-*` ; aucune grandeur de B1 ni de B2 calculée sur le réel.
  Détail plus bas (section R1).

## Empreintes lues (vérifiées avant lecture ; aucun écart)

| pièce | sha256 |
|---|---|
| `P3-addendum2-audit-verdict-v1-brouillon4.md` | `9565f4b976a57b4f956237e878ea3f9c96a31737994d21d6c734d8cde53e8316` (égale au compagnon) |
| `traitement-contre-lectures-code-addendum2-P3-v1.md` | `f2ac84b0c0da022e71ed720d3f7e3815f6838aaa48289d0a8f7bd514d3e8779a` |
| `module-v2/audit_verdict_p3_v1.py` | `dfdeef6b4652a9faad06cecd708385341f044ec4164efade1f82a4a1cf6e7a3d` |
| `module-v2/test_audit_verdict_p3_v1.py` | `a5c6ec3412c04a1e7e3af8bb1ebb168c22a3aab40b7111821d24558523dc92fd` |
| `module-v2/NOTES-MODULE-v2.md` | `d6a6fceef32dfb139a447f0aa9a7986fe76bc5ddf7a4a6598b1b51b88a38d295` |
| `revue-texte/contre-lecture-code-addendum2-texte-v1.md` | `8a2a92d295c5fad3d2f378d8b9010ec1e3b11769733c5765a813ea3e131d4884` |
| `revue-mutants/contre-lecture-code-addendum2-mutants-v1.md` | `5330e1f1d86e92b98f7a3d16dad397cfe765ae1d28f11c318feb3d1b04cbd3ba` |
| `revue-mutants/garde_r1_revue.py`, `lanceur_revue.py` (lus ; ma garde et mon lanceur en dérivent) | `fec19525…47285`, `bbc931c5…1ae17` ; `mutants_revue.py` (`ca5743a9…`) non lu, pour l'indépendance de ma liste (exécuté seulement par le script du rédacteur au rejeu) |
| code gelé cité en tête du texte : `lecture.py`, `statistiques.py`, `conditions.py`, `propositions.py`, `evaluation.py`, `manifeste.py` | `ab7c21cb…`, `a8552575…`, `dda64117…`, `5d97b223…`, `1040674c…`, `1a5c7464…` : égales au texte, au disque et au commit `7a54d43` |
| autres modules gelés lus : `gardes.py`, `scellement.py`, `prereg.py`, `harnais/validation_reelle.py`, `tests/test_premier_test_ia_lecture.py`, `tests/conftest.py` | `a83c48ce…`, `93beeb1c…`, `3b2e3ee5…`, `d25e4cd9…`, `6d3969c0…`, `a1bbfcc9…` |
| [PA] `prereg/P3-addendum-lecture-complementaire-v1.md` (l. 230-360 : table du verrou, gardes 2 et 16) | `8ff834229444b214f3f4c248ecdbf619a4b7149700825ef39bac2e86a6ff80ac` (égale au texte) |
| module et tests v1 (différentiel seulement) | `0b991450…69cf`, `ecbb8972…bfd3` |
| `verification/verification-corrections-brouillon2-addendum2-P3-v1.md` (VB2-06) ; `traitement-verification-brouillon2…` | `65afdd6c…1be1461` ; `155e8fe1…34ca` |
| `module-v2/controle-survivants/controle_survivants_v2.py` ; `resultats-survivants-v2.jsonl` ; `mesure-duree/mesure_duree_v2.py`, `mesure-duree-v2.json` | `b94c2411…350e` ; `3693f48f…f36f` ; `282ef376…0a13`, `f035bb49…c467` (compagnons de `module-v2/` tous vérifiés : OK) |

## A. Fidélité du texte au code

« = » : conforme ; « + » : ajout du module là où le texte se tait, sans effet sur un nombre, une réserve ni le verrou.
Lignes : texte (t.) brouillon 4, module (m.) v2. Comparaison mécanique (entrées, phrases, 47 clés, constantes) :
`outils/comparer_texte_code.py`, journal `journaux/comparer-texte-code.log` : aucun écart.

### A1. Règles

| règle (texte) | code | état |
|---|---|---|
| Table « Entrées » (t. 36-50) ; [A], [MA] cités, non lus | `ENTREES` m. 82-101 ; garde 2 m. 1282-1299 | = (neuf chemins, neuf empreintes) |
| Code gelé, six empreintes (t. 52-58) ; emplacement, imports permis (t. 59-65) | imports m. 55-63 ; `CHEMIN_*` m. 66-67 | = ; tests : CV2-09 |
| Statut, périmètre : ni texte décodé, ni score par jeton, ni bras « moyenne » (t. 66-88) | `decisif=False` m. 1503 | = (531 ouvertures tracées de ces fichiers, toutes dans des dépôts jouets : copie, hachage, chargeur gelé) |
| Entrées et clés lues ; entrée non calculable ou en échec (t. 162-175) | `lire_la_lecture` m. 715-783 ; `_etat_entree` m. 248-254 | = ; + types (m. 737-738, 759, 767) |
| M1, M2 (t. 177-183) | `couts_par_tache` gelé ; `_a_forme` m. 413-418 | = (tests : CV2-02) |
| M3 (t. 185-190) | m. 421-448 | = ; + `actions`, `nulles_d_origine` |
| M4 (t. 192-199) | m. 451-461, 497-506 | = |
| M5 (t. 201-208) | m. 509-544 | = ; + part sur tirages non dégénérés |
| M6, M7, M8, M9 (t. 210-227) | m. 547-622 | = |
| M10 (t. 229-247) | m. 675-698 | = (`z`, `z80`, `A_80_écrit_max` 0,58089…, `A_80_écrit_min` 0,55439…) |
| Analyses ; règles communes ; 47 clés dans l'ordre (t. 249-279) | m. 625-670, 701-710, 257-268, 363-369 | = (liste reconstruite du texte seul, égale) |
| Effectif, niveaux, repères, classements (t. 283-291) | m. 271-291 | = |
| Table des réserves (t. 292-304) | m. 978-1035 ; `_Controles` m. 937-961 | = (chaque condition relue, bords compris) |
| Cible établie sinon « sans objet » ; union (nom, cible), motifs joints (t. 306-308) | m. 951-952 ; m. 1149-1153 | = |
| Table des cas de B1 ; borne décisive ≤ log10 3 (t. 309-323) | m. 987-1000 | = (six cases ; `ampleur_non_resolue` jamais si borne décisive ≤ log10 3) |
| Symétrie des repères (t. 327-332) | m. 1015 ; m. 1032 | = |
| Plan 1-5 : commande, ordre des gardes, manifeste propre, sortie unique, arrêt écrit puis propagé, ordre des analyses (t. 336-356) | `executer` m. 1486-1523 ; `_main` m. 1526-1541 ; m. 1216-1225 | = |
| Plan 6, verrou (t. 357-366) ; table de [PA] l. 245-250 | `conclusions_etablies` m. 792-806 ; m. 741-750, 776-781 | = (table de [PA] relue : identique) |
| Plan 7-8 : synthèse ; 13 écrits ; 9 lus au plus, 4 sans objet (t. 367-379) | m. 1226-1241 ; m. 1120-1142 ; `GROUPES_DE_CONTROLES` m. 145-147 | = ; « lus » : CV2-06 |
| Plan 9, durée (t. 380) | — | CV2-04 |
| Plan 10, tests (t. 381-385) | 118 tests, en tête et vérifiés | = |
| Phrases de la table des critères (t. 389-404) | `LECTURES` m. 163-193 ; `_lecture_de` m. 1101-1117 | = (toutes égales, outil) |
| Ligne de l'audit : « addendum 2 suspect de propreté » ; cité et soumis à Lazar (t. 403) | `LECTURE_AUDIT`, `CONSIGNE_AUDIT` m. 190-191 ; m. 1093-1094, 1168-1169 | = : phrase seule dans `lecture`, consigne dans `consigne` |
| Verrou unidirectionnel ; T2 lu seulement par la table du verrou (t. 406-410) | m. 779-781 ; clés interdites m. 131-132 | = |
| Audit 1, 2, 3 ; déclencheur (t. 411-427) | `audit_symetrie` m. 1040-1096 | = ; ordre : CV2-07 ; point 3 et précision 2 : CV2-01 |
| Liste d'arrêt, préambule : seule `GardeArret` donne « échec » (t. 455-456) | `_calcul` m. 342-351 | = |

### A2. Gardes 1 à 15

| garde (t.) | code | état |
|---|---|---|
| 1 (458-460) | m. 1251-1279 | = |
| 2 (461-463) | m. 1282-1299 | = |
| 3 (464-468) | m. 1345-1378 ; m. 1302-1342 | = ; + critère lexical aussi pour l'unicité (comme [PA], garde 16) |
| 4 (469-473) ; précision 5 | m. 1405-1435 | = ; descendance stricte de N-025 |
| 5 (474-479) ; précision 6 | m. 1438-1449 ; m. 1308-1313 | = (critère lexical de [PA] garde 16, relu) |
| 6 (480) | m. 1452-1460 | = |
| 7 (481-487) | m. 811-875 ; `effet_ponctuel` m. 464-486 | = : même état et même motif que [L] pour P3-P1, P3-P2, mention, motifs recopiés du code gelé (statistiques l. 55 et 70) ; nombres comparés seulement si calculable ; P3-P3 en échec non comparé (CV2-08) |
| 8 (488-490) | m. 878-892 | = |
| 9 (491-492) ; précision 7 | m. 715-783 | = |
| 10 (493-494) | m. 895-901 | = |
| 11 (495-497) | m. 1463-1483 ; appel m. 1534 | = |
| 12 (498-500) | m. 372-387 ; appel m. 1209 | = |
| 13 (501-504) | m. 904-921 ; appels m. 1501, 1212 | = |
| 14 (505-507) | m. 1174-1201 | = ; + `issue_primaire` |
| 15 (508-509) | m. 527-537 | = |

### A3. Précisions d'application 1 à 10

| précision (t.) | code | test qui l'éprouve | état |
|---|---|---|---|
| 1 (437-438) | m. 1065-1071 | `test_audit_declencheur_2_E_sf_non_calculable_intervalles_decisifs_lus`, `test_audit_explication_trop_propre_construit_et_sain` | = ; ordre non écrit (CV2-07) ; PRE1-03 survit, équivalent |
| 2 (439) | m. 1080-1085 | `test_garde_15_degenerescences_de_la_part`, `test_audit_part_hors_bornes_construit_et_sain` | = au brouillon 4 ; règle nouvelle (CV2-01) |
| 3 (440-441) | m. 995-1000 | `test_table_des_cas_de_B1`, `test_VB2_02_E_sf_ou_D_non_calculable_reserve_non_lue` | = |
| 4 (442) | m. 529-530 | `test_garde_15_degenerescences_de_la_part` | = |
| 5 (443) | m. 1431-1435 | `test_garde_4_commit_du_manifeste_different_de_la_tete` | = |
| 6 (444) | m. 1308-1313 | `test_garde_5_second_passage_et_manifeste_illisible` | = |
| 7 (445) | m. 720-722 | artefact `garde9-principales-autre-ordre` | = |
| 8 (446-447) | m. 1208, 1243-1244 ; m. 1179-1180 | `test_lecture_modifiee_pendant_l_analyse` | = ([S] : CV2-10) |
| 9 (448-450) | m. 342-351 ; m. 1513-1519 | `test_garde_arret_dans_une_analyse_echec_et_non_lu`, `test_autre_exception_…` | = |
| 10 (451) | m. 312-331 | `test_sortie_valeur_non_finie_et_type_inconnu` | = |

Précision 2 : le texte dit bien ce que fait maintenant le v2. Une part en échec (garde 15) rend le déclencheur 3 « non
calculé » ; rien d'autre n'a bougé (différentiel v1 → v2 : six changements, ceux des notes ; les autres règles sont
octet pour octet celles du v1).

### A4. Traitement des contre-lectures

| ligne du traitement | état dans le v2 |
|---|---|
| Module : garde 7, même état et motif, nombres pour une entrée calculable | fait (m. 821-843) |
| Module : phrase de B3 complétée ; « abaissent » ; `nombre_de_controles` 13, lus et sans objet par ligne | fait (m. 181-184 ; m. 290 et 1048-1049 ; m. 1120-1142, appel m. 1241) |
| Module : « aucun autre changement de règle » | inexact : changement 6 (précision 2), CV2-01 |
| Texte CC-texte-08 : consigne hors de la phrase | fait (`consigne`, m. 1094, 1169) |
| CC-mutants-01 : recalcul indépendant des bornes, deux nombres de tirages, égalité exacte | fait (`test_bornes_recalculees_hors_du_module`, 10 000 et 11 tirages, 4 runs) ; descriptifs hors du recalcul (CV2-03) |
| CC-mutants-02 : table du verrou des deux côtés ; run « aucun signal » | fait |
| CC-mutants-03 : phrases sur des nombres donnés ; une réserve par couple | fait (phrase d'arrêt non comprise : CV2-03) |
| CC-texte-01, CC-mutants-04, VB2-01 : entrées produites par `lecture.lire` ; état différent ; comptes ; plancher ; actions non notées | fait |
| CC-texte-02, CC-mutants-05 : `GardeArret` → « échec » ; autres exceptions → arrêt écrit ; NaN, ±inf ; P3-P3 infini ; [L] modifiée | fait |
| CC-texte-03 : artefacts des comptes et du plancher | fait |
| CC-texte-04, CC-mutants-07 : bords (déclencheur 2, garde 15, « instable » borne basse, 0,48) | fait ; « instable » à borne haute nulle non éprouvé (CV2-05) |
| CC-texte-05 : `raise` jamais déclenchés | fait (31 artefacts) ; garde 6 au lancement non éprouvée (CV2-05) |
| CC-mutants-06 : gardes avant le manifeste, arbre sale | fait |
| CC-mutants-09 : [T] seul | fait |
| VB2-02 : six cases, borne ≤ log10 3, deux cibles, non lue, instable, comptes 13 / 9 / 4 | fait |

### A5. Points regardés de près

- **Précision 2** : voir A3 et CV2-01.
- **Phrase de l'audit** : `lecture` = « addendum 2 suspect de propreté » seule ; `consigne` = « cité et soumis à
  Lazar », dans l'audit et dans la ligne de la recommandation ; les deux à `None` sans déclencheur (non éprouvé pour
  `consigne` : V2-14, CV2-03).
- **Garde 7** : même état et même motif que [L] ; état « en échec » recalculé pour le seul motif que le code gelé peut
  écrire (tâches différentes) ; « non calculable » sous deux tâches, motif identique au code gelé ; nombres comparés
  seulement pour une entrée calculable ; artefacts des six paires d'états et du motif éprouvés.
- **`nombre_de_controles`** : 13 écrits vérifiés (défaut du module sinon) ; détail par groupe ; ligne d'issue rapportée ;
  « lus » au sens « non sans objet » (CV2-06).
- **118 tests** : « Nombre de tests attendu : 118 » en tête (l. 3) ; `test_nombre_de_tests_ecrit_en_tete` compte les
  tests recueillis du fichier et passe ; mon passage : 118 passed, 0 sauté. 73 fonctions, dont 5 paramétrées (8, 31, 3,
  3, 5 cas). Les 42 tests du v1 sont tous présents. Le texte (`<<NOMBRE_TESTS>>`) n'est pas lu par la garde 1, qui ne
  compare que les empreintes : le compte reste un report à la main.

## B. Campagne de mutants indépendante

- **Liste.** `outils/mutants_v2.py` (sha256 `d9c038e67b5e2f8cd7016c089faf02d0fd8ab86fee527d34e31304e1cfadf03c`) : **230
  mutants**, écrits depuis le texte et le module v2. J'avais lu les notes du rédacteur (une ligne par mutant), mais ni
  ses remplacements ni la liste de la revue précédente, et je ne suis pas parti d'eux. Au moins un par règle changée
  entre v1 et v2 (22, famille V2), par précision 1 à 10 (26, plus les deux de la précision 2 rangés en V2), par garde
  1 à 15 (75), et 47 mutants de seuil (bords inclus ou exclus ; niveau 90 % au lieu de 95 %, 95 % au lieu de 97,5 %,
  puissance 90 % ; nombre de tirages, transposition de la matrice ; graine fixe, clés échangées, entropie + 1) ; plus
  38 autres règles écrites, 14 descriptifs, 8 phrases.
- **Lancement.** `outils/lanceur_v2.py` : chaque motif présent exactement une fois (230 sur 230), copie compilée, **suite
  entière** des 118 tests (sans `-x`), depuis la racine du dépôt, sous la garde R1, trois mutants à la fois. De 14:01 à
  16:18 UTC. Résultats : `journaux/resultats-mutants-v2.jsonl` (sha256
  `193602a70174918f9e0c38d452bc045ef92d3ce0e9c17d535468d4f7a9adcfe3`), un dossier par mutant (`mutants/<id>/` : module,
  différence, journal pytest, journal R1).
- **Résultat : 230 mutants, 200 tués, 30 survivants, dont 5 équivalents ; 0 refus R1 ; 0 erreur.** Par famille (tués /
  lancés) : V2 21/22 ; précisions 1 à 10 : 25/26 (PRE1 2/3) ; gardes 1 à 15 : 66/75 (G1 5/7, G4 6/7, G6 1/2, G9 6/9,
  G13 4/6, les autres toutes) ; seuils 45/47 ; autres règles 34/38 ; descriptifs 2/14 ; phrases 7/8. Le test qui tue le
  plus : `test_bornes_recalculees_hors_du_module` (147 mutants) ; 123 mutants ne sont tués que par un seul test.

### Survivants

| mutant | règle mutée | classement | cas qui sépare (`separer_survivants.py`) | test qui manque |
|---|---|---|---|---|
| PRE1-03 | précision 1 : seul « non calculable » rend « non calculé » | **équivalent** | aucune entrée du code gelé : un E_sf « en échec » exige des tâches différentes, donc une entrée décisive en échec, traitée avant ; construit seulement : E_sf en échec, trois intervalles lus → base « non calculé », mutant `KeyError` | — |
| G1-02 | garde 1 : booléen accepté | **équivalent** | `int(True)` = 1 ≠ entropie : arrêt dans les deux | — |
| G1-07 | garde 1 : empreinte prise sur le chemin versé | **équivalent quant à l'arrêt** | module exécuté hors de son chemin : la garde 11 arrête avant le manifeste | — |
| G9-03 | garde 9 : `etablie` non exigée | **équivalent** | `etablie` absente : garde 8 arrête d'abord ; `etablie` = 1 : arrêt par le recoupement du verrou | — |
| REGLE-32 | clés interdites des sorties gelées gardées | **équivalent** | aucune sortie versée (`effet_cout_apparie`, fonctions du module) ne porte de clé interdite ; la garde 14 arrêterait | — |
| G4-02, G6-02, G9-01, G9-02, G13-02, G13-04, SEUIL-11, SEUIL-33, REGLE-30 | bords et types (CV2-05) | séparés ; sans effet sur le run réel | voir CV2-05 | un test chacun |
| REGLE-01, REGLE-02 | R_sf sans `cout_milliers_espace` ; sans `cout_multiplication` | séparés ; effet sur le run réel inconnu | run « sain » avec ces deux formes : 213 et 240 chemins de sortie changent | CV2-02 |
| DESC-01, 03, 04, 05, 07, 08, 09, 10, 11, 12, 13, 14 | descriptifs de M3, M5, M6, M8, M9, M10 | séparés ; changeraient des descriptifs écrits | run « sain » (de 2 à 120 chemins changent) ; DESC-01, 07, 10 sur cas construits | CV2-03 |
| V2-14 | clé `consigne` écrite sans déclencheur | séparé | run « sain » : `consigne` « cité et soumis à Lazar » alors que le déclencheur est faux | CV2-03 |
| PHRASE-08 | phrase d'arrêt changée | séparé | la cellule du texte égale la base, pas le mutant | CV2-03 |

Journal des séparations : `journaux/separer-survivants.log` (26 essais passés, 0 refus).

Règles changées entre v1 et v2 (famille V2) : toutes tenues par un test sauf V2-14. Garde 7 (huit mutants : état non
comparé, motif non comparé, échec v1, motif recopié autrement, clés inversées, états confondus, seuil d'une tâche,
nombres de P3-P1 seuls) : tous tués. Phrase de B3, « abaissent », phrase de l'audit, `nombre_de_controles` (cinq
mutants), précision 2 (deux mutants) : tous tués.

### Rejeu, en contrôle, du script du rédacteur

Le script `module-v2/controle-survivants/controle_survivants_v2.py` (`b94c2411…`) a été lu en entier avant tout
lancement. Lancé tel quel, il aurait écrit dans `module-v2/` (dossier temporaire et fichier de résultats, déjà plein : il
n'aurait rien relancé). Je l'ai donc copié dans `revue-v2/controle-redacteur/` en changeant deux lignes seulement :
`MODULE, TESTS` lus dans ma copie de base (mêmes empreintes) et `TMP` sous `revue-v2/tmp/` (sha256 de la copie
`ec01fe05a915774c57b82d5f3c7310a73d3b35db622ad94485d464396f00d9f9`). Reste inchangé : sa liste (celle de la revue
précédente, lue comme texte, plus F23 adapté et N01 à N10), sa garde (`revue-mutants/garde_r1_revue.py`), `-x`, trois
mutants à la fois. Lancé avec `--tous` de 16:20 à 16:53 UTC.

**Résultat : 117 mutants, 117 tués, 0 refus** (`controle-redacteur/resultats-survivants-v2.jsonl`, sha256
`0fb84c3867ebdafdfc47b10ceaf083d728941144e6b7a9593b050db0fd934f57` ; journal `journaux/rejeu-redacteur.log`). Face à son
fichier (`3693f48f…`) : même état, même empreinte de mutant et même premier test en échec pour chacun des 117. Son
affirmation « 117 tués sur 117 » est reproduite.

Comparaison avec ma campagne : sa liste porte sur les règles déjà éprouvées par la revue précédente et sur les dix règles
du brouillon 4 ; aucun de ses mutants ne touche les deux formes absentes des tests, les descriptifs, la clé `consigne`
sans déclencheur, la phrase d'arrêt ni les bords listés en CV2-05. C'est là que vivent mes 25 survivants séparables. Sur
les règles communes aux deux listes (garde 7, précision 2, phrases, verrou, gardes de lancement), les deux campagnes
concordent : tout est tué.

## C. Pannes

`outils/test_pannes_v2.py` (aides et fixtures de la copie de base des tests, importées sans copie), sous la garde v2b :
**23 essais passés, 0 refus** (`journaux/pannes-v2.log`, `journaux/r1-pannes-v2b.jsonl`).

| panne | ce que fait le module |
|---|---|
| clé absente de [L] : `P3-P2/calculable`, `cout_mention/taches_exclues`, `P3-P3/<p>/plancher_quantile`, `P3-P6/mention/actions` | arrêt, garde 9 (« clé absente … (aucune valeur devinée) ») |
| clé absente de [L] : `P3-P1/etablie`, `principales` | arrêt, garde 8 (`lecture.issue` ne peut pas recalculer), avant la garde 9 |
| `principales["enjeux"]` absente de [SF] | arrêt par `KeyError` nue (CV2-10) |
| pièce [SF] absente du dépôt jouet | arrêt, garde 2 « [SF] », rien d'écrit |
| NaN dans `P3-P1/effet` ; NaN, +inf, −inf dans `P3-P1/bas` ou `haut` | arrêt, garde 7 ou 9, motif écrit |
| NaN dans `P3-P3/<p>/aire` ou `plancher_quantile` | arrêt, garde 7 |
| ±inf dans les coûts du run source | coûts illisibles pour le code gelé comme pour le module ; cohérence passée, sortie finie (`allow_nan=False`) |
| NaN dans une colonne de forme passée en flottant | NaN lu « vrai » par `astype(bool)` ; arrêt, garde 7 (compte de forme ≠ [L]) |
| [L] modifiée en mémoire pendant les analyses | arrêt (« lecture décisive modifiée pendant l'addendum 2 ») |
| run source modifié en mémoire après la garde 7 | **passage sans arrêt** (CV2-10) |
| [L] modifiée sur le disque après la garde 3 (dépôt jouet) | arrêt « arbre de travail non propre » à la création du manifeste, rien d'écrit |
| arbre non propre : fichier suivi hors de l'arbre gelé modifié ; code gelé modifié sans commit ; fichier non suivi à la racine | arrêt « arbre de travail non propre », rien d'écrit (le code gelé modifié sans commit n'est pas vu par la garde 1, qui compare des commits ; il l'est par le manifeste) |
| texte de l'addendum 2 modifié sans commit | arrêt, garde 1 (« non scellé ou non conforme »), rien d'écrit |

Aucun repli silencieux hors de la ligne marquée. Les arrêts avant le manifeste n'écrivent rien ; ceux d'après sont
écrits dans `arret` puis propagés (tests du v2, rejoués).

## D. Durée

Mesure indépendante (`outils/mesure_duree_revue.py`, `outils/mesure_duree_details.py`) : dépôt jouet construit par mon
outil, avec les aides du fichier de tests (60 tâches, 4 conditions, 10 pas, 2 400 actions, 430 sondes dont 2 × 214 de plancher ; lecture décisive par le code
gelé), module v2 aux constantes du jouet, vraie commande dans un processus séparé, 10 000 tirages, sur quatre copies.
Journaux : `journaux/mesure-duree-revue.json` (sha256 `804305a887906b67cc64b7e4806f268e4211d0b120d4fb2bd2cf1c21bd1aca32`),
`journaux/mesure-duree-details.json` (`69fc1c484a016165c3d38201c829949e56086235772a12c200d3ef40154b161c`).

| grandeur | ma mesure | rédacteur (notes) |
|---|---|---|
| ligne de commande complète | 5,46 ; 6,26 ; 5,37 ; 5,10 s (charge 1,9 à 2,3) | 6,49 ; 5,53 ; 5,71 ; 5,33 s |
| processus qui ne fait qu'importer (mural) | 4,05 à 4,64 s | 4,8 ; 4,74 s (« imports seuls ») |
| imports, mesurés dans le processus | 3,06 à 3,49 s (dont `validation_reelle` 2,4 s) | — |
| fonction pure (10 000 tirages) | 0,66 à 0,79 s | 0,64 ; 0,43 s |
| mémoire maximale (`ru_maxrss`) | 699 220 Kio = 683 Mio ≈ 716 Mo | « ≈ 683 Mo » |
| chaque passage | réussi : sortie scellée, 13 écrits, 9 lus, 4 sans objet | idem |

La phrase des notes est juste sur le total, pas sur « imports » ni sur l'unité : CV2-04, avec une phrase corrigée.

## R1

- Garde : `outils/garde_r1_v2.py` (copie étendue de la garde de la revue : ouverture, listage, copie, suppression refusés
  sous `donnees/`, `diag/`, `runs/`, `traces/`, `prereg/P3-consignes-v1.md` et tout chemin du dépôt qui contient
  `textes-actions`), éprouvée avant usage sur un cas sain et sur des artefacts à chemins inexistants (12 épreuves,
  15 refus attendus, `journaux/r1-epreuve-garde.jsonl`). Puis `garde_r1_v2b.py` (CV2-11), éprouvée (14 épreuves, 17
  refus attendus, `journaux/r1-epreuve-garde-v2b.jsonl`).
- Passage de base de la suite v2 (garde v2 et `strace -f -y`) : 118 passed ; **0 refus** ; 0 ouverture réussie d'un
  fichier réel de ces dossiers, dans aucun processus (git, sous-processus de la vraie commande compris) ; 531 ouvertures
  tracées des fichiers des textes et des scores par jeton, toutes dans des dépôts jouets.
- Campagne : 230 lancements de la suite entière, **0 refus** (champ `refus_R1` de chaque ligne de `resultats-mutants-v2.jsonl` ; un journal par mutant, `mutants/<id>/r1.jsonl`). Mesures de durée, comparaisons, séparations : **0 refus**. Pannes : 0 refus (garde v2b) ;
  un lancement écarté, 21 faux positifs expliqués (CV2-11), aucun accès. Rejeu du script du rédacteur (sa garde) :
  117 lancements, **0 refus**.
- Les sous-processus (git, vraie commande) ne portent pas le crochet ; ils tournent dans les dépôts jouets
  (`cwd`, `PYTHONPATH` du jouet) ; `strace` le confirme pour le passage de base.
- Aucune grandeur de B1 ni de B2 calculée sur le réel. Je n'ai lu ni les consignes privées, ni un texte d'action, ni une
  clé, ni une donnée ou une sortie du run.

## Empreintes de début et de fin

- Dossier de base hors de `revue-v2/` (617 fichiers : textes, modules, tests, notes, revues, journaux du rédacteur) :
  liste d'empreintes identique au début (13:36) et à la fin (16:55) (`journaux/empreintes-dossier-S-debut.txt` et
  `…-fin.txt`, sha256 `3f073f7f176790a6200fbfc849af7a7a8f537e1f64d06259fa9cd263df4620ed` toutes deux). Module v2
  `dfdeef6b…`, tests v2 `a5c6ec34…`, notes `d6a6fcee…`, brouillon 4 `9565f4b9…` : inchangés.
- Dépôt de travail : tête `562fa39` au début, `0760313` à la fin (commits de la session) ; `src/` et `tests/` égaux au
  commit cité `7a54d43` aux deux têtes ; fichiers de cache inchangés (`journaux/pycache-fichiers-debut.txt`) ; aucun
  `__pycache__` ni `.pyc` dans `revue-v2/`.

## Reproductions

Depuis la racine du dépôt, interpréteur de la consigne, `PYTHONPATH=src:revue-v2/outils`, `PYTHONDONTWRITEBYTECODE=1`,
`REVUE_JOURNAL_R1=<journal>`, `TMPDIR` sous `revue-v2/tmp/` :

- garde : `python -B -m pytest -q -p no:cacheprovider -p garde_r1_v2b revue-v2/outils/test_garde_r1_v2b.py` ;
- base : `strace -f -y -e trace=open,openat,openat2 … python -B -m pytest -q -p no:cacheprovider -p garde_r1_v2 --basetemp=… revue-v2/base/test_audit_verdict_p3_v1.py` → 118 passed (`journaux/pytest-base-strace.log`, `journaux/strace-base.txt.gz`) ;
- campagne : `python -B revue-v2/outils/lanceur_v2.py --travailleurs 3` ;
- séparations : `python -B -m pytest -q -s -p no:cacheprovider -p garde_r1_v2b revue-v2/outils/separer_survivants.py` ;
- pannes : `… revue-v2/outils/test_pannes_v2.py` ;
- comparaison texte ↔ code : `python -B revue-v2/outils/comparer_texte_code.py <brouillon 4> revue-v2/base/audit_verdict_p3_v1.py` ;
- précision 2, v1 face à v2 : `python -B revue-v2/outils/precision2_v1_v2.py module/audit_verdict_p3_v1.py revue-v2/base/audit_verdict_p3_v1.py` ;
- durée : `python -B revue-v2/outils/mesure_duree_revue.py <dossier> <journal> 4`, puis `mesure_duree_details.py` ;
- rejeu du rédacteur : `python -B revue-v2/controle-redacteur/controle_survivants_v2.py --tous`.

## Fichiers rendus (sous `revue-v2/`)

| fichier | sha256 |
|---|---|
| `outils/garde_r1_v2.py` | `f7da04eaebe799cb5945fb5ed1ff2bd01ddf497a313c4af5ebc28a6bf2d78daa` |
| `outils/garde_r1_v2b.py` | `022cfd55eac2298b9f00b371d5141d37a98561662d2f424255983199160bac4f` |
| `outils/test_garde_r1_v2.py` | `92ac58c2ef3c8b7ae09d6dae097affb3165f33ef48097ea2cbe8d55a4eb0ac06` |
| `outils/test_garde_r1_v2b.py` | `21dc8e56c0111decc26c43edca1837d2841946e49c70f0f7b058790df986d7af` |
| `outils/mutants_v2.py` | `d9c038e67b5e2f8cd7016c089faf02d0fd8ab86fee527d34e31304e1cfadf03c` |
| `outils/lanceur_v2.py` | `4a4023378a2558ed040c0c2c5868b6fee1e7fe281cb2983832acdaf6e920503f` |
| `outils/separer_survivants.py` | `b919e3d51a7060345e2fc527aaa27a3df60c00da3ea53248edd526289521d7b1` |
| `outils/test_pannes_v2.py` | `deb7d4ba41bd8dd81323fc01c359972ac7fba4870a0d42b58e1b9caef6144cbc` |
| `outils/comparer_texte_code.py` | `2c57ff82f9c50559a549667b65b1e3df0f29f119df9135147e29c4ec6c314104` |
| `outils/precision2_v1_v2.py` | `d9d400748b0b6fa05129ea760c7d0c91882169634e793f2ec3cd4bb7fec354a6` |
| `outils/mesure_duree_revue.py` | `7a287f1a9f1de5455f72495709b8fa74f24c18c09acccadf77f5d4ff9fbcccbf` |
| `outils/mesure_duree_details.py` | `b4ba43e534ccbf3e67184bc781481de6312ca8cf7c129c12b3ab0a9b188d3526` |
| `controle-redacteur/controle_survivants_v2.py` | `ec01fe05a915774c57b82d5f3c7310a73d3b35db622ad94485d464396f00d9f9` |
| `journaux/resultats-mutants-v2.jsonl` | `193602a70174918f9e0c38d452bc045ef92d3ce0e9c17d535468d4f7a9adcfe3` |
| `controle-redacteur/resultats-survivants-v2.jsonl` | `0fb84c3867ebdafdfc47b10ceaf083d728941144e6b7a9593b050db0fd934f57` |
| `journaux/separer-survivants.log` | `75a5f8fae67cb3ffb751e4d39129dcdcadc8d862a9c63790d2326f16612c8e8d` |
| `journaux/pannes-v2.log` | `acc10db840e982f327561ac8aeac46702cf8a4a43c4a9a01a922901c31dc1034` |
| `journaux/comparer-texte-code.log` | `2f136d7c1fdab38995158283f537fb435d0af55dbc492b4a081db22228dec220` |
| `journaux/precision2-v1-v2.log` | `e73bfdca8854ade46f36ddce17a6d3d8192cab28b4274a3a2d5f4ca5309658e5` |
| `journaux/mesure-duree-revue.json` | `804305a887906b67cc64b7e4806f268e4211d0b120d4fb2bd2cf1c21bd1aca32` |
| `journaux/mesure-duree-details.json` | `69fc1c484a016165c3d38201c829949e56086235772a12c200d3ef40154b161c` |
| `journaux/strace-base.txt.gz` | `20860b6397718452f003d1f8e77a88d3ff852db2109f2203df7cb26094f073ea` |
| `journaux/campagne-v2.log` | `637ba53037bc504e3144611ab723356f2259936daff05e1b9b2386efc0a879af` |
| `journaux/rejeu-redacteur.log` | `1cb474889b89dbd26f55dc0309d8b907911147220081961397e17f25ebca473b` |
