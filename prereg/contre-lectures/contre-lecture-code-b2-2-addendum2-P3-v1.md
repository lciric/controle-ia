# Contre-lecture R2 du code de l'addendum 2 de P3 — angle « mutants et pannes » — v1

**Verdict : scellable après corrections.** Le module est juste sur chaque règle mutée : aucun défaut trouvé. Sur 107
mutants, 66 sont tués et 41 survivent à la suite entière (42 tests passés). 4 survivants sont équivalents ; les 37 autres
sont séparés du module de base par un cas construit, où la base suit le texte. Les corrections portent sur les **tests**
(donc sur l'empreinte et le nombre de tests cités en tête du texte), pas sur le module, dont l'empreinte peut rester
`0b991450…69cf` pour le brouillon 2.

Le plus grave (CC-mutants-01) : aucun test ne recalcule les bornes qui portent les réserves de B1 et B2 (E_sf, D, M).
Graine, niveau et nombre de tirages peuvent changer sans qu'un test échoue. Les pannes tiennent : même sortie d'un
processus à l'autre et d'un dépôt à l'autre ; aucun texte d'action décodé ; aucun score par jeton lu ; aucune donnée
réelle ouverte, ni par les tests ni par moi.

- Contre-lecteur : sous-agent neuf (R2). Je n'ai écrit ni le texte, ni le module, ni ses tests, ni ses notes.
  Date : 2026-10-20 (UTC), de 11:04 à 11:52.
- Dossier de travail, seul endroit écrit :
  `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum2-p3/revue-mutants/` (noté `revue/`
  ci-dessous). Copie de base, 107 mutants, lanceur, essais de pannes, journaux, ce rapport.
- Originaux intacts : module, tests, notes et brouillon 2 ont la même empreinte au début (11:04) et à la fin (11:52)
  (`revue/journaux/empreintes-original-debut.txt`, `…-fin.txt`). Jamais modifiés ; tout mutant est une copie.
- Dépôt de travail en lecture seule : aucune écriture ; git en lecture seulement. Les changements apparus dans
  `git status` pendant la revue (décision N-029, registres, têtes R-274 et R-275) sont ceux de la session. Aucun
  `__pycache__` créé (aucun `.pyc` plus récent que 11:04). Code gelé inchangé pendant la revue (`src/` et `tests/`
  égaux à `2dc3638` ; arbre gelé égal à `7a54d43`, le commit cité) ; les six modules gelés ont les empreintes citées en
  tête du texte.
- R1 : tables synthétiques seulement. Chaque lancement de pytest a tourné sous un crochet d'audit
  (`revue/garde_r1_revue.py`) qui refuse toute ouverture, sous le dépôt de travail, de `donnees/`, `diag/`, `runs/`,
  `traces/` et de `prereg/P3-consignes-v1.md`. Garde éprouvée sur un cas sain et sur deux artefacts (chemins
  inexistants : aucune donnée touchée). **0 refus** sur tous les lancements (copie de base, 107 mutants, pannes,
  reproductions). Le passage de la copie de base a aussi tourné sous `strace -f` : 0 ouverture d'un fichier réel de ces
  dossiers, dans aucun processus (git et sous-processus compris). Aucune grandeur de B1 ni de B2 calculée sur le réel.
  Je n'ai lu ni les consignes privées, ni un texte d'action, ni une clé, ni une donnée du run.
- Lancements : `python -B`, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`, `--basetemp` et `TMPDIR` dans
  `revue/tmp/` (vidé à la fin), depuis la racine du dépôt (`PYTHONPATH=src`). Trois mutants à la fois au plus (4 cœurs).
  Python 3.11.17, numpy 2.4.6, scipy 1.17.1, pytest 9.1.1.

## Ce qui a été lu

| fichier | sha256 |
|---|---|
| texte qui fait foi : brouillon 2 (en entier) | `641b36c2d8b77ca78c6f9bdd151cc3a3cc38a468e4f2a307e01e94354f651615` |
| module `module/audit_verdict_p3_v1.py` (en entier, 1 484 lignes) | `0b991450d107ee16b484a568d91f95ca232b5079d42ae17b6c52ec2bd23369cf` |
| tests `module/test_audit_verdict_p3_v1.py` (en entier, 42 tests) | `ecbb897293b690b37e0f086c86ca575b97c0a6bfedcec69f56849023afa8bfd3` |
| notes `module/NOTES-MODULE.md` (en entier) | `6d06ddbc5bd2cd40e3b67fab191eedf793d8cc8f1eb6f40206d18a5f760a96dd` |
| contre-lecture 1 du brouillon 1 (en entier) | `ad360e028ae0d9f08941bbab689631aea763e3966fe7f0be4fc5ed3cc3a112d1` |
| traitement de la contre-lecture 1 (en entier) | `dfce4ccaee074228b2873033201373322fe0005314ea88900863eec5001a1392` |
| traitement de la vérification du brouillon 2 (en entier ; le brouillon 3 lui-même n'est pas lu, empreinte `e3f8528c…645a`) | `155e8fe173db2315a8f60afe61aa61cd72a0fcd4a65855cccdc0b1007e1734ca` |
| code gelé : `lecture.py` (en entier), `statistiques.py` (l. 1-140), `manifeste.py`, `sondes/evaluation.py`, `prereg.py` (en entier), `scellement.py` (l. 1-80), `gardes.py` (`GardeArret`), `harnais/validation_reelle.py` (l. 55-80) | `ab7c21cb…`, `a8552575…`, `1a5c7464…`, `1040674c…`, `3b2e3ee5…`, `93beeb1c…`, `a83c48ce…`, `d25e4cd9…` |
| aides importées par les tests : `tests/test_premier_test_ia_lecture.py` (l. 1-140), `tests/conftest.py` | `6d3969c0…`, `a1bbfcc9…` |
| [PA] `prereg/P3-addendum-lecture-complementaire-v1.md` (l. 236-256, table du verrou) ; [P] (deux lignes d'en-tête : commit cité, entropie) | `8ff83422…`, `d975e981…` |
| modèle de forme : `prereg/contre-lectures/verification-code-final-addendum-P3-v1-mutants.md` (l. 1-80) | `aab50bf0…` |

Le brouillon 1 n'a pas été relu (remplacé par le brouillon 2).

## Ce qui a été lancé (comptes)

| quoi | résultat | journal (sous `revue/`) |
|---|---|---|
| copie de base `base/` (module et tests, octet pour octet), suite complète, sous la garde R1 et `strace -f` | **42 passed in 103.23 s** ; 0 refus ; 0 ouverture réelle | `journaux/pytest-base.log`, `journaux/r1-base.jsonl`, `journaux/strace-base.txt` |
| 107 mutants (`mutants_revue.py`), suite complète arrêtée au premier échec (`-x`), sous la garde R1 | **66 tués, 41 survivants** (chacun : 42 passed) ; 0 refus | `journaux/resultats-mutants.jsonl`, `mutants/<id>/pytest.log` et `difference.diff` |
| reproductions des survivants (`pannes/test_reproductions_survivants.py`, 24 tests, dont 4 sur dépôts jouets) | 24 passed : chaque fois, base ≠ mutant | `pannes/pytest-pannes-et-reproductions-final.log` |
| pannes P1 à P5 (`pannes/test_pannes_revue.py`, 12 tests) | 12 passed | idem (passage final : **36 passed in 123.96 s**) |
| rejeu de P3 et P4 sur 11 survivants de calcul (`REVUE_MODULE=<mutant>`) | base 9 sur 9 ; chaque mutant échoue à au moins un cas | `pannes/rejeu/resultats-rejeu-final.txt` |

Définitions. « Tué » : la suite échoue (code 1). J'ai lu la première erreur de chacune des 66 morts : elle porte sur la
règle mutée (table en annexe B). « Survit » : la suite passe en entier. « Équivalent » : aucune entrée produite par le code
gelé ne sépare base et mutant. « Reproduction » : un test de `revue/pannes/` montre, sur un cas construit, que la base
suit le texte et que le mutant s'en écarte : c'est le test qui manque.

Familles (comme demandé) : A réserve mal câblée (9 : 4 tués) ; B cible fausse (4 : 4) ; C cas de B1 ou de B2 inversé
(11 : 11) ; D mention sans cible P3-P1 (1 : 1) ; E verrou ouvert (11 : 6) ; F garde retirée (24 : 11) ; G seuil ou niveau
changé (16 : 10) ; H NaN remplacé par l'infini (3 : 1) ; I clés et graines (10 : 6) ; J méthode de M3 à M9 (11 : 6) ;
K audit de symétrie (4 : 3) ; L lancement (3 : 3). Les familles B, C, D et L sont entièrement tuées : cibles, table des
cas de B1, règle de B2, mention sur P3-P1 et forme du lancement sont bien tenues par les tests.

## Constats (le plus grave d'abord)

### CC-mutants-01 — majeur — Les bornes qui portent les réserves de B1 et B2 ne sont recalculées par aucun test

- **Où.** Module : `_intervalle` (l. 240-244), `_tirages_des_taches` (l. 247-251), `_rng` (l. 336-340), `effet_restreint`
  (l. 466-475), `part_des_formes` (l. 478-513), `mediane_par_tache` (l. 516-534), `effet_taches_sans_forme`
  (l. 537-548), `ecart_de_forme` (l. 551-573), `analyse_contraste` (l. 594-625). Texte : M4 à M8 et « Règles communes »
  (95 %, 10 000 tirages, une matrice par clé, consommée une fois, graines R9).
- **Problème.** Aucun test ne compare une borne de E_sf, D, E0, M, M7, E_-f ou M8 à un calcul fait hors du module. Les
  tests épinglent des valeurs ponctuelles (moyennes, médiane) et des propriétés (« borne basse > 0 »), jamais une borne.
  Survivent donc, sur des grandeurs qui portent des réserves : **I01** (générateur de graine fixe au lieu de
  `manifeste.generateur(graines[clé])`), **G01** (intervalles de M5, M6, M8 à 90 % au lieu de 95 %), **G03** (5 000 lignes
  tirées au lieu de 10 000), **I10** (médianes de M6 tirées hors de leur clé), **J04** (M sur T_sf au lieu des tâches de
  l'effet décisif). Et, sur des descriptifs : **I06** (E0 tiré sur d'autres lignes que D), **I09** (générateur de M8
  consommé deux fois), **J01** (E_-f retire toutes les formes), **J02** (T_propres ne regarde que la condition a),
  **J03** (M8 compare « avec f » à « sans f » au lieu de « sans aucune forme »). G02 (E_sf à 90 %) est tué, mais
  seulement parce qu'un scénario de l'audit change de case : rien ne l'épingle.
- **Conséquence pour ce run.** P3-P1 est établie : les réserves `hors_formes`, `au_dela_de_la_consigne` et
  `ampleur_non_resolue` (borne basse de E_sf), `portee_par_les_formes` (borne basse de D) et `mediane_par_tache`
  (borne basse de M) seront lues. Une régression de ce type, par exemple à la mise au brouillon 3, changerait ces
  réserves sans qu'un test échoue (G01 : D et M lus à 90 %), ou les rendrait non rejouables depuis le manifeste (I01, R9).
- **Le module est juste.** Mon recalcul indépendant, fait sans rien importer du module (fonctions gelées
  `couts_par_tache`, `cout_de_tache`, `effet_cout_apparie` ; `manifeste.generateur(G[clé])` aux clés écrites dans le
  texte ; `np.quantile` à `(1 − 0,95) / 2`, convention de `effet_cout_apparie`), égale la sortie du module **au bit près**
  pour E_sf, D, E0, M, M7, chaque E_-f et chaque M8, sur quatre scénarios (sain, trop_bas, b2, degenere), à 10 000 et à
  11 tirages : 8 cas sur 8.
- **Reproduction.** `REVUE_MODULE=revue/mutants/<id>/audit_verdict_p3_v1.py … pytest revue/pannes/test_pannes_revue.py
  -k "P3 or P4"` (commande complète en annexe A). Base : 9 sur 9. G01, G03, I01 : 8 cas sur 8 en échec ; I06 : 7 ; I09 :
  6 ; I10 : 3 (à 11 tirages seulement : les bornes d'une médiane rééchantillonnée sont des valeurs discrètes, insensibles
  à la graine à 10 000 tirages) ; J01, J02, J03, J04 : 2 (`revue/pannes/rejeu/resultats-rejeu-final.txt`).
- **Correction.** Verser aux tests du module un recalcul indépendant de ce type (la fonction `ecarts_au_recalcul` de
  `revue/pannes/test_pannes_revue.py` peut être reprise telle quelle), à deux nombres de tirages au moins, dont un très
  petit (11) où chaque ligne tirée compte ; comparaison exacte.

### CC-mutants-02 — mineur — Quatre lignes de la table du verrou ne sont éprouvées par aucun cas

- **Où.** `conclusions_etablies` (l. 761-775) ; lecture de `conforme` et `T<k>` dans `lire_la_lecture` (l. 739-750).
  Texte : plan, point 6 (table du plan, point 5, de [PA], reprise telle quelle). Tests : `test_garde_14_verrou`,
  `test_organisme_non_etabli_…`, `test_ligne_criteres_2_et_3_…`.
- **Problème.** Survivent **E05** (`nul/<p>` établie sans la ligne « aucune sonde générique… »), **E06** (`P3-P4/<p>`
  établie sans la ligne « critères 2 et 3… »), **E07** (`P3-P3/<p>` établie sur la ligne « lecture de P3-P3 en échec »),
  **E10** (`T<k>/<p>` établi sans son drapeau `etabli`). La garde 14 recalcule `conclusions_etablies` par la même
  fonction : elle ne peut pas voir une table fausse. Effets montrés : E05 range `nul/<p>` parmi les conclusions établies
  d'un run « organisme non établi » et y lit B3 ; E10 range `T3/<p>` sans son drapeau, ce qui ouvrirait la phrase « T3
  établi au sens de la lecture décisive » à une réserve de la mention ; E06 promeut `P3-P4/<p>` puis s'arrête sur une
  clé jamais lue ; E07 range `P3-P3/<p>`. Sans effet sur la ligne de ce run (aucune sonde au-dessus) ; mais c'est le
  verrou qui tient la règle de N-024 (« jamais promouvoir »).
- **Reproduction.** `revue/pannes/test_reproductions_survivants.py::test_E05_…`, `::test_E06_…`, `::test_E07_…`,
  `::test_E10_…` (base : exclut ; mutant : inclut). Le cas de E05 est un run synthétique (`_src(11, signal="aucun",
  facteur=1.0)` : ligne « organisme non établi », deux sondes « non au-dessus »).
- **Correction.** Test unitaire de `conclusions_etablies` sur une table de `L` construits : chaque ligne de la table, et
  chaque condition des deux côtés ; plus le run synthétique ci-dessus (conclusions vides, tous les contrôles « sans
  objet »).

### CC-mutants-03 — mineur — Phrases de lecture au verdict et union des réserves non épinglées

- **Où.** `_lecture_de` (l. 1059-1075), `synthese` (l. 1078-1106) ; test `test_recommandation_au_verdict_phrases_des_criteres`.
- **Problème.** Survivent **A07** (borne haute de E_sf écrite comme « borne basse » dans la phrase de
  `au_dela_de_la_consigne`), **A09** (`A_80_écrit_min` au lieu de `A_80_écrit_max` dans la phrase de B3), **A06** (E0 au
  lieu de D dans la phrase de `portee_par_les_formes`), **A05** (phrase de P3-P1 donnée aux cibles `P3-P4/<p>` et
  `T3/<p>`), **A08** (une réserve par motif au lieu d'une par couple (nom, cible)). Le test ne lit que A_80(p) dans la
  phrase de B3 et la présence de « part D = ». Or, dans ce run, les réserves `au_dela_de_la_consigne` et
  `puissance_du_nul` sont celles que le texte prédit : le sous-agent du verdict citerait ces deux phrases.
- **Reproduction.** `::test_A05_…`, `::test_A06_A07_A09_…`, `::test_A08_…`.
- **Correction.** Tests de `_lecture_de` sur des nombres donnés (D et son intervalle ; borne basse de E_sf ; A_80(p) et
  A_80_écrit_max) et sur les phrases des cibles `P3-P4/<p>` et `T3/<p>` ; `synthese` sur deux contrôles de même couple :
  une réserve, motifs joints.

### CC-mutants-04 — mineur — Garde 7 : trois conditions sans artefact ; aucune action non notée dans les tables de test

- **Où.** `exiger_coherence` (l. 780-842 : comptes l. 806-809 ; actions l. 813 ; entrée « non calculable » l. 796-801 ;
  actions notées l. 823-824) ; test `test_garde_7_coherence_cout_et_forme_alteres`.
- **Problème.** Survivent **F02** (tâches, tâches exclues, illisibles et nuls non comparés), **F03** (actions par
  condition non comparées), **F23** (entrée de [L] « non calculable » acceptée alors que le recalcul a deux tâches ou
  plus), **J06** (aire calculée sur toutes les actions, notées ou non). Les quatre artefacts du test changent l'effet, une
  forme ou un score ; aucun ne change un compte seul. Les tables synthétiques n'ont aucune action non notée, alors que la
  lecture gelée les compte (`actions_non_notees`) : le filtre des actions notées n'est jamais exercé. F23 laisserait
  passer une [L] dont P3-P2 serait faussement « non calculable » : le contrôle du témoin deviendrait « non lu ».
- **Le module est juste.** Avec 6 % d'actions non notées (tous leurs scores non finis), la garde 7 passe et les aires
  égalent [L] (`revue/pannes/test_pannes_revue.py::test_P4_…`) ; le mutant J06 y arrête (« score non fini »).
- **Reproduction.** `::test_F02_…` (un coût illisible de l'honnête devenu nul : effet inchangé, `actions_nulles_b`
  changé ; base : arrêt, mutant : passe), `::test_F03_…`, `::test_F23_…` ; rejeu de P4 sur J06.
- **Correction.** Ces trois artefacts, et un run synthétique avec actions non notées qui doit passer. (Le brouillon 3,
  VB2-01, réécrit cette partie de la garde 7 et demande un test : il recoupe F23.)

### CC-mutants-05 — mineur — Règles « aucun repli silencieux » sans artefact

- **Où.** `_calcul` (l. 324-333), `_propre` (l. 294-313), `_nombre` (l. 196-197), contrôle de la lecture modifiée
  (l. 1177-1178). Texte, liste d'arrêt, préambule : « Seule GardeArret donne « échec » à un calcul ; toute autre exception
  arrête l'addendum 2. Aucun repli silencieux. »
- **Problème.** Survivent **F08** (`_calcul` rend « échec » pour toute exception : une KeyError ou un `DefautDuModule`
  dans une analyse deviendrait, en silence, un contrôle « non lu »), **F09** (valeur non finie de la sortie remplacée par
  None), **H03** (±inf laissé dans la sortie), **H02** (±inf accepté par les gardes 9 et 13 : l'arrêt glisse après le
  manifeste), **F22** (contrôle « lecture décisive modifiée » retiré). Aucun test ne lève une autre exception que
  `GardeArret` dans une analyse, ni ne met une valeur non finie dans la sortie ou dans [L].
- **Reproduction.** `::test_F08_…`, `::test_F09_H03_…`, `::test_H02_…`, `::test_F22_…`.
- **Correction.** Tests unitaires : KeyError et `DefautDuModule` traversent `_calcul` ; NaN, +inf et −inf arrêtent
  `_propre` avec leur chemin ; un `haut` infini dans P3-P3 arrête à la garde 9 ; une [L] modifiée pendant l'analyse
  arrête.

### CC-mutants-06 — mineur — Lancement : place des gardes 7 à 10 et 13, arbre propre, jamais éprouvés

- **Où.** `executer` (l. 1433-1438). Texte, plan, points 3 et 4 : gardes 1 à 11 et 13 « avant la création du manifeste
  (aucune écriture en cas d'arrêt) » ; « arbre de travail propre exigé, sans `autoriser_depot_sale` ».
- **Problème.** Survivent **F05** (gardes 7, 8 et 10 retirées d'avant le manifeste, refaites après), **F06** (garde 13
  de même), **F07** (`autoriser_depot_sale=True`). Les tests éprouvent ces gardes sur la fonction pure, pas leur place ;
  aucun lancement n'a lieu sur un arbre sale. Avec F05 ou F06, un arrêt de ces gardes écrirait une sortie d'arrêt, et
  la garde 5 refuserait ensuite tout nouveau passage : l'unique passage serait consommé (L02, garde 11 déplacée, montre
  ce mécanisme ; lui est tué). Avec F07, un passage sur un arbre sale réussirait, avec une simple réserve au manifeste.
- **Reproduction** (dépôts jouets construits pour la base et pour chaque mutant, comme la fixture `gabarit`) :
  `::test_F05_F06_…[F05]` et `[F06]` (garde simulée en arrêt : base, rien d'écrit ; mutant, sortie d'arrêt écrite),
  `::test_F07_…` (fichier non commité : base, arrêt « arbre de travail non propre », rien d'écrit ; mutant, passage
  écrit).
- **Correction.** Ces trois tests de lancement, sur le dépôt jouet des tests.

### CC-mutants-07 — mineur — Bornes non épinglées ; une branche de l'audit jamais prise

- **Où.** `part_des_formes` (l. 500 : garde 15 ; l. 507 : mention « instable »), `classements` (l. 263-264),
  `audit_symetrie` (l. 1015-1016 ; l. 1031-1033).
- **Problème.** Survivent **F19** (garde 15 à « au moins 1 % » au lieu de « plus de 1 % »), **G11** et **G12** (bornes
  des cas « conforme » du déclencheur « explication trop propre »), **G13** (mention « instable » quand la borne basse
  de E0 vaut 0), **G10** (classement descriptif contre 0,48 au lieu de log10 3), **K04** (branche « E_sf non calculable »
  de l'audit retirée). Pour K04 : dans ce run, aucun intervalle décisif n'est conforme (le texte cite [1,2464 ; 1,8012],
  [−0,5704 ; −0,0650], [−0,5404 ; −0,1155]) ; l'audit passera donc par cette branche si un E_sf est non calculable ; le
  mutant y lève une KeyError, la base écrit « non calculé ». Les égalités exactes sont peu probables sur des données
  réelles.
- **Reproduction.** `::test_F19_…` (2 048 tirages, seuil égal au nombre de dégénérés), `::test_G10_…`,
  `::test_G11_G12_…`, `::test_G13_…`, `::test_K04_…` (run synthétique : saboteur × 10, témoin et mention × 0,5, toutes
  les actions du témoin à forme).
- **Correction.** Ces cas de bord.

### CC-mutants-08 — information — Quatre survivants équivalents

- **E11** (`nul/<p>` sur la ligne seule, sans l'état) : sur une [L] du code gelé, la ligne « aucune sonde… » implique
  l'état « non au-dessus » des deux sondes (garde 8 : issue et états recalculés depuis les jeux). Seule une [L] forgée,
  dont `non_interpretables` contredit les jeux, les sépare.
- **F13** (type de `taches_exclues`) : la garde 7 passe avant la garde 9, compare la liste recalculée à celle de [L] et
  arrête la première.
- **F24** (empreinte de [P] dans le manifeste de lecture) : redondant ; [ML] et [MR] sont épinglés par la garde 2, et
  `exiger_lecture_sous_prereg` compare déjà l'empreinte de [P] à celle du manifeste du run source.
- **F04** (sondes principales de [L] contre [SF]) : `lecture.lire` les écrit dans l'ordre de [SF] ; un nom différent
  arrête dès la garde 7. Seul un ordre inversé, impossible en sortie du code gelé, sépare base et mutant
  (`::test_F04_…`).

### CC-mutants-09 — information — L'artefact « textes » du test de la garde 2 est masqué

- **Où.** `test_garde_2_entrees_nommees_et_empreintes` (tests, l. 1237-1240).
- **Problème.** Le résumé [R] est supprimé juste avant l'altération du fichier des textes : la garde 2 arrête donc sur
  [R], et l'expression `\[(R|T)\]` l'accepte. Le hachage de [T] par la garde 2 n'est éprouvé que par le bloc de
  références du test de bout en bout (F15 y est tué).
- **Reproduction.** `::test_F15_…` (fichier des textes seul altéré et rescellé : base, « garde 2 : [T] … » ; mutant
  F15, garde 2 passée, arrêt plus tard à la garde 6).
- **Correction.** Rétablir [R] avant d'altérer [T], et attendre `\[T\]` seul.

### CC-mutants-10 — information — Le module suit le brouillon 2 ; un brouillon 3 existe

- Le brouillon 3 (empreinte `e3f8528c…645a`) réécrit la garde 7 (VB2-01) et allonge la liste fermée des tests (VB2-02 :
  cases de la table de B1, cibles de B2, réserve non lue, part « instable », comptes de contrôles) ; la session prévoit
  de remettre le module au brouillon 3. D'après ce traitement, seul F23 (CC-mutants-04) est recoupé ; rien n'y épingle
  les bornes, la graine, la table du verrou ni les phrases.
- Rejeu après la mise à jour : remplacer `revue/base/`, mettre à jour les deux empreintes attendues en tête de
  `revue/lanceur_revue.py`, vider `revue/journaux/resultats-mutants.jsonl`, relancer le lanceur (un motif absent est
  signalé « motif invalide », jamais lancé), puis `revue/pannes/`.

## Ce qui tient (pannes)

- **Déterminisme.** P1 : fonction pure, deux processus (`PYTHONHASHSEED` 0 et 4242), dix scénarios des tests, 10 000
  tirages : empreintes identiques, scénario par scénario (`revue/pannes/determinisme-fonction-pure.json`). P2 : vraie
  ligne de commande, deux copies d'un dépôt jouet, deux processus (`PYTHONHASHSEED` 1 et 777), 10 000 tirages :
  `resultat` identique octet pour octet (`8eefbee2…9e24`, `revue/pannes/determinisme-ligne-de-commande.json`). Le test
  du module ne vérifiait que deux passages dans un même processus.
- **Aucun texte d'action, aucun score par jeton.** Crochet d'audit, piles d'appel : le fichier des textes n'est ouvert
  que par `scellement.empreinte` (hachage, garde 2 et chargeur gelé) et son compagnon par `lire_compagnon` ; le fichier
  des scores par jeton n'est ouvert que par `np.load` dans `lecture.charger_source` (gelé) et par le hachage ; jamais par
  le code du module. P5 : avec `source["jetons"]` remplacé par un objet qui échoue à toute lecture, la sortie est
  calculée ; les seules colonnes de [S] lues sont `condition`, `tache`, `cout`, les cinq formes, `noms_sondes` et `scores`
  : exactement la liste du texte (`revue/pannes/colonnes-lues.json`) ; aucun indice « jeton », « texte », `scores_` ou
  `logits_` dans le module. Aucune moyenne ni médiane sur les jetons : le module ne touche aucun jeton ; ses moyennes
  portent sur les actions d'un épisode ou sur des tâches, sa médiane sur des tâches (test du module, et P3).
- **R1 dans les tests du module.** Confirmé : 0 refus de la garde R1, 0 ouverture réelle sous `strace -f` ; les
  constantes du run réel ne servent qu'à un test de chaînes ; les dépôts jouets ne nomment que des runs synthétiques.
- **Calcul.** Hors des survivants listés, tout ce que j'ai muté est tenu : cibles (B), table des cas de B1 bornes
  comprises (C), règle et cibles de B2, mention sur P3-P1 (D), recoupement de `etablie`, verrou de fin (E01 à E04, E08,
  E09), B3 et ses quantiles normaux (G07 à G09, G15, G16), gardes 1, 3, 4, 5, 8, 11, 12, 13 et 14 ; garde 2 par le seul
  test de bout en bout (CC-mutants-09) ; garde 7 sur l'effet, ses tolérances et le quantile du plancher ; garde 15 à
  10 % ; restriction par NaN (H01), clés de graines et leur ordre (I02 à I05, I07, I08), signes de M4 et M5 (J07, J12), arrêt
  écrit puis propagé (L01).
- **Durée.** Suite du module : 103 s sous `strace`, environ 60 s sans (un survivant). Sans objet pour le marqueur
  `<<DUREE_MESUREE>>` du texte (mesuré par le rédacteur du module).

## Annexe A — Commandes

Depuis la racine du dépôt de travail, avec `R=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum2-p3/revue-mutants`
et `PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python` :

- un mutant contre la suite du module :
  `REVUE_JOURNAL_R1=$R/journaux/r1.jsonl PYTHONPATH=src:$R PYTHONDONTWRITEBYTECODE=1 $PY -B -m pytest -q -p no:cacheprovider -p garde_r1_revue --basetemp=$R/tmp/bt $R/mutants/<id>/test_audit_verdict_p3_v1.py` (survivant : 42 passed) ;
- toute la campagne : `cd $R && $PY -B lanceur_revue.py --travailleurs 3` (reprend là où elle s'est arrêtée) ;
- reproductions et pannes sur la base :
  `REVUE_JOURNAL_R1=$R/pannes/r1.jsonl PYTHONPATH=src:$R PYTHONDONTWRITEBYTECODE=1 $PY -B -m pytest -q -p no:cacheprovider -p garde_r1_revue --basetemp=$R/tmp/bt $R/pannes/test_pannes_revue.py $R/pannes/test_reproductions_survivants.py` (36 passed) ;
- recalcul indépendant sur un mutant : même commande sur `test_pannes_revue.py -k "P3 or P4"`, avec
  `REVUE_MODULE=$R/mutants/<id>/audit_verdict_p3_v1.py`.

Pièces (sha256) : `mutants_revue.py` `ca5743a9…`, `lanceur_revue.py` `bbc931c5…`, `garde_r1_revue.py` `fec19525…`,
`journaux/resultats-mutants.jsonl` `c0538bea…`, `pannes/test_pannes_revue.py` `b1b5c33d…`,
`pannes/test_reproductions_survivants.py` `2f6e3892…`, `pannes/determinisme.py` `4d324237…` ; liste complète :
`revue/journaux/empreintes-preuves.txt`.

## Annexe B — Les 107 mutants

| id | famille | règle mutée | état | test qui tue, ou reproduction du survivant |
|---|---|---|---|---|
| A01 | A | contrôle hors_formes qui émet la réserve au_dela_de_la_consigne | tué | `test_table_des_cas_de_B1` |
| A02 | A | réserve du témoin nommée comme celle de la mention | tué | `test_reserves_de_B2_regle_et_cibles` |
| A03 | A | réserve « non lue » toujours nommée B1 | tué | `test_garde_9_cle_absente_et_entree_en_echec` |
| A04 | A | réserve écrite pour un contrôle contraire faux | tué | `test_B3_calcul_a_la_main_et_quantiles_normaux` |
| A05 | A | phrase de lecture de P3-P1 donnée aux cibles P3-P4/<p> et T3/<p> | **SURVIT** | repro `test_A05` |
| A06 | A | phrase de ampleur_portee_par_les_formes remplie avec E0 au lieu de D | **SURVIT** | repro `test_A06_A07_A09` |
| A07 | A | phrase de au_dela_de_la_consigne remplie avec la borne haute | **SURVIT** | repro `test_A06_A07_A09` |
| A08 | A | réserves sans union par couple (nom, cible) : une par motif | **SURVIT** | repro `test_A08` |
| A09 | A | phrase de B3 remplie avec A_80_écrit_min au lieu de A_80_écrit_max | **SURVIT** | repro `test_A06_A07_A09` |
| B01 | B | réserve de B3 sur P3-P3/<p> au lieu de nul/<p> | tué | `test_garde_9_cle_absente_et_entree_en_echec` |
| B02 | B | réserve du témoin sur P3-P3/<p> au lieu de P3-P4/<p> | tué | `test_ligne_criteres_2_et_3_nul_non_etabli_B3_sans_objet` |
| B03 | B | réserve de la mention sur T4/<p> au lieu de T3/<p> | tué | `test_reserves_de_B2_regle_et_cibles` |
| B04 | B | B3 « non lu » sur P3-P1 au lieu de nul/<p> | tué | `test_garde_9_cle_absente_et_entree_en_echec` |
| C01 | C | hors_formes : b_sf < 0 au lieu de ≤ 0 | tué | `test_table_des_cas_de_B1` |
| C02 | C | portee_par_les_formes : b_D ≥ 0 au lieu de > 0 | tué | `test_garde_15_degenerescences_de_la_part` |
| C03 | C | au_dela_de_la_consigne : b_sf ≥ log10 3 au lieu de > | tué | `test_table_des_cas_de_B1` |
| C04 | C | non_resolue : 0 ≤ b_sf au lieu de 0 < b_sf | tué | `test_table_des_cas_de_B1` |
| C05 | C | non_resolue : b_D < 0 au lieu de ≤ 0 | tué | `test_table_des_cas_de_B1` |
| C06 | C | non_resolue : borne décisive ≥ log10 3 au lieu de > | tué | `test_table_des_cas_de_B1` |
| C07 | C | mediane_par_tache : b_M < 0 au lieu de ≤ 0 | tué | `test_table_des_cas_de_B1` |
| C08 | C | non_resolue : case inversée (b_D > 0 au lieu de ≤ 0) | tué | `test_table_des_cas_de_B1` |
| C09 | C | B2 : condition sur la borne décisive retirée | tué | `test_reserves_de_B2_regle_et_cibles` |
| C10 | C | B2 : b_sf ≥ 0 au lieu de > 0 | tué | `test_reserves_de_B2_regle_et_cibles` |
| C11 | C | au_dela_de_la_consigne lu contre 0 au lieu de log10 3 | tué | `test_table_des_cas_de_B1` |
| D01 | D | réserve de la mention sans la cible P3-P1 (seulement T3/<p>) | tué | `test_garde_9_cle_absente_et_entree_en_echec` |
| E01 | E | contrôle lu même si sa cible n'est pas établie | tué | `test_garde_9_cle_absente_et_entree_en_echec` |
| E02 | E | garde 14 : contrôle lu sur cible non établie accepté | tué | `test_garde_14_verrou` |
| E03 | E | garde 14 : réserve sur cible non établie acceptée | tué | `test_garde_14_verrou` |
| E04 | E | verrou point 6 : P3-P1/etablie non recoupé avec calculable et bas > 0 | tué | `test_garde_14_verrou` |
| E05 | E | nul/<p> établie sans la ligne « aucune sonde générique… » | **SURVIT** | repro `test_E05` |
| E06 | E | P3-P4/<p> établie sans la ligne « critères 2 et 3… » | **SURVIT** | repro `test_E06` |
| E07 | E | P3-P3/<p> établie même sur la ligne « lecture de P3-P3 en échec » | **SURVIT** | repro `test_E07` |
| E08 | E | garde 14 : conclusions établies non recoupées | tué | `test_garde_14_verrou` |
| E09 | E | garde 14 : clés interdites non cherchées | tué | `test_garde_14_verrou` |
| E10 | E | T<k>/<p> établi sans son drapeau etabli | **SURVIT** | repro `test_E10` |
| E11 | E | nul/<p> établie sans l'état « non au-dessus » (ligne seule) | **SURVIT** | équivalent (CC-mutants-08) |
| F01 | F | garde 13 : bas > Q pour une sonde dont nul/<p> est établie, non contrôlé | tué | `test_garde_13_entrees_de_B3` |
| F02 | F | garde 7 : tâches, exclues, illisibles et nuls non comparés | **SURVIT** | repro `test_F02` |
| F03 | F | garde 7 : nombre d'actions par condition non comparé | **SURVIT** | repro `test_F03` |
| F04 | F | garde 9 : sondes principales de [L] non recoupées avec [SF] | **SURVIT** | équivalent en pratique (CC-mutants-08) ; repro `test_F04` sur [L] forgée |
| F05 | F | lancement : gardes 7, 8 et 10 retirées d'avant le manifeste (refaites après) | **SURVIT** | repro `test_F05_F06[F05]` (dépôt jouet) |
| F06 | F | lancement : garde 13 retirée d'avant le manifeste (refaite après) | **SURVIT** | repro `test_F05_F06[F06]` (dépôt jouet) |
| F07 | F | lancement : arbre de travail sale autorisé | **SURVIT** | repro `test_F07` (dépôt jouet) |
| F08 | F | « échec » pour toute exception (pas seulement GardeArret) | **SURVIT** | repro `test_F08` |
| F09 | F | valeur non finie de la sortie remplacée par None (repli silencieux) | **SURVIT** | repro `test_F09_H03` |
| F10 | F | garde 12 : valeurs des graines non comparées | tué | `test_garde_12_graines` |
| F11 | F | garde 4 : S2 non contrôlé contre le commit de N-025 | tué | `test_garde_4_anteriorite_sur_un_depot_jouet` |
| F12 | F | garde 5 : second passage reconnu par la seule commande (pas par le texte) | tué | `test_garde_5_second_passage_et_manifeste_illisible` |
| F13 | F | garde 9 : type de taches_exclues non contrôlé | **SURVIT** | équivalent (CC-mutants-08) |
| F14 | F | garde 8 retirée de la fonction pure (et du lancement) | tué | `test_garde_8_issue_et_etats` |
| F15 | F | garde 2 : fichier des textes [T] non haché | tué | `test_ligne_de_commande_de_bout_en_bout` |
| F16 | F | garde 1 : empreinte des tests non comparée | tué | `test_garde_1_entropie_texte_scelle_empreintes_et_arbre_gele` |
| F17 | F | garde 11 : chemin du module non contrôlé | tué | `test_garde_11_forme_de_la_commande` |
| F18 | F | garde 3 : unicité de la lecture décisive affaiblie (« présente » au lieu de « seule ») | tué | `test_garde_3_lecture_decisive_rattachement_et_unicite` |
| F19 | F | garde 15 : ≥ 1 % au lieu de > 1 % | **SURVIT** | repro `test_F19` |
| F20 | F | garde 15 : seuil des dégénérés à 10 % au lieu de 1 % | tué | `test_garde_15_degenerescences_de_la_part` |
| F21 | F | garde 7 : effets ponctuels non comparés (comptes seuls) | tué | `test_garde_7_coherence_cout_et_forme_alteres` |
| F22 | F | garde « lecture décisive modifiée pendant l'addendum 2 » retirée | **SURVIT** | repro `test_F22` |
| F23 | F | garde 7 : [L] « non calculable » accepté même si le recalcul a deux tâches ou plus | **SURVIT** | repro `test_F23` |
| F24 | F | garde 3 : empreinte de [P] dans le manifeste de lecture non comparée | **SURVIT** | équivalent (CC-mutants-08) |
| G01 | G | intervalles propres (M5, M6, M8) à 90 % au lieu de 95 % (q non divisé par 2) | **SURVIT** | rejeu P3 (8 cas sur 8 échouent) |
| G02 | G | E_sf, E_-f, M7 à 90 % au lieu de 95 % | tué | `test_audit_explication_trop_propre_construit_et_sain` |
| G03 | G | matrice de tirage de M5, M6, M8 à TIRAGES / 2 lignes | **SURVIT** | rejeu P3 (8 cas sur 8 échouent) |
| G04 | G | garde 7 : tolérance des effets 1e-2 au lieu de 1e-12 | tué | `test_garde_7_coherence_cout_et_forme_alteres` |
| G05 | G | garde 7 : tolérance des aires 1e-2 au lieu de 1e-9 | tué | `test_garde_7_coherence_cout_et_forme_alteres` |
| G06 | G | repère de B1 arrondi à 0,48 au lieu de log10 3 | tué | `test_table_des_cas_de_B1` |
| G07 | G | z = Φ⁻¹(0,975) au lieu de Φ⁻¹(0,9875) | tué | `test_B3_calcul_a_la_main_et_quantiles_normaux` |
| G08 | G | B3 : A_80 ≥ A_80_écrit_max au lieu de > | tué | `test_B3_calcul_a_la_main_et_quantiles_normaux` |
| G09 | G | hypothèse écrite Q max 0,54 au lieu de 0,53 | tué | `test_B3_calcul_a_la_main_et_quantiles_normaux` |
| G10 | G | classement descriptif contre 0,48 au lieu de log10 3 | **SURVIT** | repro `test_G10` |
| G11 | G | audit (2) : saboteur conforme si 0 ≤ bas (au lieu de 0 < bas) | **SURVIT** | repro `test_G11_G12` |
| G12 | G | audit (2) : témoin et mention conformes si bas < 0 < haut (bornes exclues) | **SURVIT** | repro `test_G11_G12` |
| G13 | G | M5 : mention « instable » si e_bas < 0 < e_haut (bornes exclues) | **SURVIT** | repro `test_G13` |
| G14 | G | garde 7 : quantile du plancher 0,90 au lieu de 0,95 | tué | `test_garde_7_coherence_cout_et_forme_alteres` |
| G15 | G | B3 : facteur 1 + z / z80 au lieu de 1 + z80 / z | tué | `test_B3_calcul_a_la_main_et_quantiles_normaux` |
| G16 | G | B3 : demi-largeur haut − bas (non divisée par 2) | tué | `test_B3_calcul_a_la_main_et_quantiles_normaux` |
| H01 | H | restriction : coût retiré remplacé par +inf au lieu de NaN | tué | `test_restriction_retire_exactement_les_actions_a_forme` |
| H02 | H | _nombre accepte ±inf (gardes 9 et 13) | **SURVIT** | repro `test_H02` |
| H03 | H | sortie : ±inf laissé passer (NaN seul refusé) | **SURVIT** | repro `test_F09_H03` |
| I01 | I | générateur fixe (graine 0) au lieu de manifeste.generateur(graines[clé]) | **SURVIT** | rejeu P3 (8 sur 8) |
| I02 | I | clés de B2 écrites avec l'analyse B1 | tué | `test_garde_9_cle_absente_et_entree_en_echec` |
| I03 | I | clés de E_sf et de la part échangées | tué | `test_ecart_de_forme_M8_calcul_a_la_main_et_forme_absente` |
| I04 | I | une seule clé pour les cinq E_-f | tué | `test_ecart_de_forme_M8_calcul_a_la_main_et_forme_absente` |
| I05 | I | écarts de forme consommés dans l'ordre inverse des conditions | tué | `test_ecart_de_forme_M8_calcul_a_la_main_et_forme_absente` |
| I06 | I | M5 : E0 tiré sur une autre matrice que D (lignes non partagées) | **SURVIT** | rejeu P3 (7 sur 8) |
| I07 | I | garde 12 : graines attendues d'une autre entropie | tué | `test_garde_7_coherence_cout_et_forme_alteres` |
| I08 | I | liste fermée : clés des écarts dans un autre ordre | tué | `test_cles_de_graines_liste_fermee_et_distinctes` |
| I09 | I | M8 : générateur consommé deux fois (un tirage jeté avant celui qui sert) | **SURVIT** | rejeu P3 (6 sur 8) |
| I10 | I | M6 : médianes des lignes tirées sur une matrice de graine fixe | **SURVIT** | rejeu P3 à 11 tirages (3 sur 8) |
| J01 | J | E_-f retire toutes les formes au lieu de la seule forme f | **SURVIT** | rejeu P3 (2 sur 8) |
| J02 | J | M7 : T_propres ne regarde que les formes de la condition a | **SURVIT** | rejeu P3 (2 sur 8) |
| J03 | J | M8 : f comparée aux actions sans f (et non sans aucune forme) | **SURVIT** | rejeu P3 (2 sur 8) |
| J04 | J | M6 : médiane sur T_sf au lieu des tâches de l'effet décisif | **SURVIT** | rejeu P3 (2 sur 8) |
| J05 | J | M3 : restriction appliquée à la seule condition a | tué | `test_restriction_retire_exactement_les_actions_a_forme` |
| J06 | J | garde 7 : aire sur toutes les actions (notées ou non) | **SURVIT** | rejeu P4 (arrêt « score non fini ») |
| J07 | J | M5 : D = moyenne de d_sf − d_∅ (signe inversé) | tué | `test_honnete_lit_100_fois_trop_bas_ses_actions_a_forme` |
| J08 | J | M5 : sur T_∅ au lieu de T_sf | tué | `test_garde_15_degenerescences_de_la_part` |
| J09 | J | M3 : illisibles d'origine sans les actions retirées | tué | `test_restriction_retire_exactement_les_actions_a_forme` |
| J10 | J | M9 : d_sf de la table par tâche égal à d_∅ | tué | `test_mediane_et_moyennes_sur_les_taches_seulement` |
| J12 | J | M4 : d(t) = s(b, t) − s(a, t) (signe inversé) | tué | `test_garde_15_degenerescences_de_la_part` |
| K01 | K | audit (2) « sans objet » seulement si tous les intervalles décisifs sont conformes | tué | `test_audit_part_hors_bornes_construit_et_sain` |
| K02 | K | déclencheur vrai seulement si (2) et (3) le sont | tué | `test_audit_explication_trop_propre_construit_et_sain` |
| K03 | K | audit (3) : bornes −1 et 1 exclues de l'intervalle admis | tué | `test_audit_part_hors_bornes_construit_et_sain` |
| K04 | K | audit (2) : cas « E_sf non calculable » retiré | **SURVIT** | repro `test_K04` |
| L01 | L | arrêt après le manifeste écrit mais non propagé | tué | `test_ligne_de_commande_de_bout_en_bout` |
| L02 | L | garde 11 déplacée après la création du manifeste | tué | `test_garde_11_forme_de_la_commande` |
| L03 | L | paramètres de tirage non contrôlés au point d'entrée | tué | `test_garde_11_parametres_au_point_d_entree` |

Les gardes 6, 9 (hors des deux mutants équivalents) et 10 n'ont pas été mutées : leurs tests (cas sain et artefact) existent ; je ne les ai pas éprouvés par mutant.
