# Préenregistrement — mesure unanime du tour « mesures fortes » : fausses alertes par épisode honnête entier de l'agrégateur séquentiel, sans puis avec corrélation injectée (v14, après treize contre-lectures)

- **Version 14** — auteur : session-dépôt `session_01QPDgKgcLdggoVJfGC5cBw8` (servie par **Opus 5.5**), après le relevé
  `date -u` de 09:08:51 UTC le 10 novembre 2026. **Remplace la v13** (`f52de3456e95872cb100cc6b866f7ad1912cdc52d664a48b4da2eccd3070c578`,
  jamais scellée, gardée telle quelle, R12). Raison : l'exécutante de la lignée conv-audit s'est arrêtée à la relève du
  28 octobre (changement de compte) sans achever la v14 ; le dossier est versé tel quel depuis `canal/conv-audit-n04`
  (`4d1fa5c0`) sur `claude/upbeat-cray-dmauvv` (commit `a46d0077`, 270 compagnons vérifiés conformes) ; décision de Lazar du
  10 novembre (« a ») : la session-dépôt achève et lance la mesure (`registres/passations/2026-11-10-0846-decision-lazar-mesure-unanime-ici.md`,
  `609e48f6…`). **La v14 ne touche que la plomberie et le texte qui la décrit** : correction de CV13-1 à CV13-4 (traitement
  en fin de document) ; noms et empreintes de la séquence, de la garde témoin et des deux tests v14, versés tels quels avec
  leurs compagnons depuis le commit `4d1fa5c0` de la lignée conv-audit ; noms des six fichiers de sortie v14 dans les
  commandes du Plan d'analyse. Les sections Hypothèse, Prédiction chiffrée et signe attendu, Métrique, Seuil, Critères de
  lecture gelés et Liste d'arrêt sont **identiques au bit près** à la v13 ; le Plan d'analyse ne change que par ces noms de
  fichiers (v13 → v14). **Environnement d'exécution reconstruit** le 10 novembre, sans modifier la plomberie scellée :
  `/opt/venv-essaim-sim-v1` recréé (Python 3.13.18, numpy 2.5.4 — la version des répétitions d'octobre —, bash 5.2.21,
  Linux x86_64) ; lien symbolique `/home/claude/canal-conv-audit-n04` → `/home/user/controle-ia-travail`, pour que les
  chemins absolus codés en dur (interpréteur, `PYTHONPATH`, données) se résolvent ; `controle_ia.prereg` et
  `controle_ia.scellement` sont ceux du `src/` de la branche `claude/upbeat-cray-dmauvv`.
- Auteur de la v13 (pour mémoire) : lignée conv-audit, instance du 28 octobre 2026 (servie par **Opus 4.6** pour cette v13 ; **Opus 4.8** pour la v12 et la v11 ; v10 par Opus 5.5, v2 à v9
  par Fable 5.1), après le relevé `date -u` de 08:06:40 UTC le 28 octobre. **Remplace la v12** (`89d278e8e7ca02d1a8b4942b25c466287e70bce2a5c4aa190524355a82f56186`, gardée, R12). Pour mémoire, la v12 remplaçait la v11 (`b1c1dd69413c824551500cb46310c15c4a809f5b05559b45e407a34d2157791c`, gardée, R12), la v11 la v10 (`785a33fae9d835ee7529a44d76629dec7ce7bfd0544a5f7dc4b2a46646d1c3c2`, gardée, R12), et la v10 la v9 (`9206956b25ecd64c4bfb0eecd484eaa5605a4680940a34070caf9aaf49bd35e7`, gardée, R12 ; v8 `92c208af…`, v7 `54bb2892…`, v6 `24b5785b…`,
  v5 `29f91ff3…`, v4 `57187171…`, v3 `3a52f304…`, v2 `e6369f43…`, v1 `7158affc…` aussi) selon les contre-lectures précédentes, toutes
  acceptées (traitement en fin de document) : la v9 par un **huitième** sous-agent neuf Opus 5.5
  (`contre-lecture-v9/rapport-contre-lecture-mesure-unanime-v9.md`, `aeeca90dbd8001ddd92c891a9da433ea6723803df42760246612cceca74479b3`,
  CV9-1 à CV9-5, « à corriger en v10 » : répétition rejouée, interruption simulée par arrêt du processus, branche E ≠ 60, arbre,
  mélange à pas fixé, « aucun faux confirmé, aucun faux blocage ») ; la v8 entière par un **septième** sous-agent neuf Opus 5.5 (`contre-lecture-v8/rapport-contre-lecture-mesure-unanime-v8.md`,
  `989c02dee325c3941c499477623b6485d783348b0fde310b9b4d1e3931781dec`, CV8-1 à CV8-6, « à corriger en v9 » ; il a **rejoué la
  répétition générale** à l'identique, exercé la branche E ≠ 60 sur un fichier au format réel à E = 52, l'étape 0 et la garde
  R12, vérifié l'arbre sur 64 combinaisons, les audits, les gardes, toutes les empreintes ; « aucun faux confirmé sur M1 ni M4 ») ;
  la v7 entière par un **sixième** sous-agent neuf Opus 5.5 (`contre-lecture-v7/rapport-contre-lecture-mesure-unanime-v7.md`,
  `7783ab01792d80260616128dd83abe1ab27d18982b96fa3ed531de9a18594dd6`, CV7-1 à CV7-6, « à corriger en v8 » — **CV7-1 bloquait la
  séquence** : la lecture mécanique v3 lisait E dans un champ que seul le mode synthétique écrivait et aurait refusé la
  sortie réelle après l'unique exécution ; d'où, en v8, une **répétition générale** de toute la séquence sur un fichier
  synthétique au format réel, déposée) ; la v6 entière par un **cinquième** sous-agent neuf Opus 5.5 (`contre-lecture-v6/rapport-contre-lecture-mesure-unanime-v6.md`,
  `23ce5f933117cbc6e9048132b7f89f785de53f0ecb86e93ac936f72dd9ded5b3`, CV6-1 à CV6-6, « à corriger en v7 » ; il a reproduit
  l'essai synthétique v6 et la table v6 à l'octet près, vérifié l'arbre de M2 ter sur ses 32 combinaisons, l'excès par sonde,
  le mélange à pas fixé, les gardes et les refus en lançant) ; la v5 entière par un **quatrième** sous-agent neuf Opus 5.5 (`contre-lecture-v5/rapport-contre-lecture-mesure-unanime-v5.md`,
  `912dd47a90bb8719424f6833dbc3c6a9d7ce4d94d450cf92e45f1fb8559da3a5`, CV5-1 à CV5-6, « à corriger en v6 » ; il a reproduit
  l'essai synthétique v5 à l'octet près et vérifié l'excès, le mélange à pas fixé, les gardes et les refus en lançant) ; la
  v4 entière par un **troisième** sous-agent neuf Opus 5.5 (`contre-lecture-v4/rapport-contre-lecture-mesure-unanime-v4.md`,
  `ef6b87704b00bd776608313adcb160984e3378109592930c0e5d17c88d7d4f86`, CV4-1 à CV4-6, « à corriger en v5 », avec une
  simulation de la règle d'audit de M3 sous le nul : `contre-lecture-v4/verif_cv4_m3_v1.py` et six sorties) ; la v1 par un sous-agent neuf Opus 5.5
  (`contre-lecture-v1/rapport-contre-lecture-mesure-unanime-v1.md`, `5d47ae52d44e81a25604220ba3482db2eec8cfb0fd5b426dcce9484ef15bbf2d`,
  CM-1 à CM-11) ; son complément sur la v2 (`contre-lecture-v1/complement-v2.md`,
  `e5ca74bb11faece8ca72f932d6b78f3bac8f36fd6f11a515e8e3afb53bd4f7dc`, (a) à (e)) ; la v3 entière par un **autre**
  sous-agent neuf Opus 5.5 (`contre-lecture-v3/rapport-contre-lecture-mesure-unanime-v3.md`,
  `0fb0734a59514af24162b86ec3413ca87c657120f5658c584ea4b27cb8a5214c`, CV3-1 à CV3-9, « à corriger en v4 »).
- Date de la v13 (UTC) : 2026-10-28, 08:07. Date de la v14 (UTC) : 2026-11-10, 09:08.
- Code d'analyse : `analyse_fausses_alertes_v8.py`, **inchangé depuis la v8** (commit `32de42f2`) ; les v9 à v14 ne touchent
  que la lecture, la rédaction et la séquence, **dans le commit qui porte ce texte** (branche `canal/conv-audit-n04` jusqu'à
  la v13 ; `claude/upbeat-cray-dmauvv` pour la v14). Empreinte
  `52b1760a09970526a926f2119dceeef7f20e2f280bdb6a6c2d890962556c5400` ; testé sur données synthétiques seulement
  (`sortie-synthetique-essai-v8.json`, `f83456bee333d2806dc2ed953fb94e96b936f8a69ed5a1f2955b1adb7041fe62`, **5 tirages, 300 rééchantillonnages
  et sans commit**, le nombre de rééchantillonnages au manifeste : un essai du code, pas une sortie) et par `--test-gardes`
  (R5 : **quinze entrées, quatorze gardes et une valeur** — cinq cas sains (passage, bras M4, mélange à pas fixé, chargement,
  E sain), quatre artefacts de calcul (score non fini, scores constants, K trop petit, score porté par une action invalide),
  trois artefacts de chargement (empreinte, deux effectifs), E minimal exercé par la garde elle-même, corrélation
  intraclasse sur scores constants ; la valeur : la corrélation saine ; une garde endormie **lève**, CV6-6) ; **aucune lecture
  des scores réels avant le scellement** (R1). **Lecture mécanique des seuils gelés** : `lecture_mecanique_v8.py`
  (`7f28af2b7cd5c86a9d6d8003cffc2551514d0451b6b7e5fd6537e68c7626a623`, docstring seule changée depuis la v7, logique identique au bit près, CV11-3), écrite et scellée avant toute lecture réelle ; son essai est une **sortie brute** d'un script déposé
  (`essai_lecture_mecanique_v8.py`, `bedf26b806d6cf9a149fa4e3f3410352844f57a916866a20eaa31bcf4f25ede2` → `essai-lecture-mecanique-v8.json`, `0745cc2081aed0c6b1eff0dabacfdc25057d9dce49a99741513edf29316bdbef` : les neuf
  feuilles, six audits qui suspendent (M2 bis réfutée compris, CV8-3), la réserve des bras à zéro et celle de (2a) avec D′ > 0
  (CV8-4), les bornes exactes, six refus du manifeste dont les trois propres au mode réel, CV8-6) ; elle vérifie le manifeste de la sortie (script v8, empreinte des données, **empreinte du script**, E égal à
  celui de la table, tirages 20, rééchantillonnages 2 000, commit présent — CV7-5), arrondit à 10⁻⁹ avant toute comparaison
  à une borne (CV6-4), et **tout audit suspend la lecture** (CV6-1, CV7-2). **Séquence** : `commandes-lecture-reelle-v14.sh`
  (`d7c035c70160b9f4a3b7ed345d799d826f7c93fedf57c6643abc05a2dc57ff74`, avec les gardes isolées `garde-trace-reelle-v14.sh` (`a0cf2c534d481d125c3930505ab79f51d5079fa890e8c2cc50ccfdd59739063e` ; **paramétrée** : la séquence lui passe en arguments les trois noms des traces, elle n'en contient aucun, CV13-1) et `garde-lecture-seule-v12.sh` (`f58374077f0146f2136bdfb75ddbbaf64c515fb7fdf1800899728bad9abf734b`) et leurs tests déposés `test-garde-trace-v14.sh` (`45f34ada6e227823101c51b4bbea848f5d009cf15149a958651c0e633cfab4df`) et `test-lecture-seule-v14.sh` (`93835c54c17d97f06a1f03b53d867f4b68794a9769a312a24f84f6ee9d31a541`)) : commandes (1) à (4), la rédaction `rediger_note_lecture_v7.py` (`a9af81c40864b77ecbcef8f3930ddb0061fbd2ae102c836ddeee084fc4b49ab8`, **`--instance` et `--date` obligatoires**,
  mois complets, CV10-3, CV11-3) comprise, sa note **scellée** ; **lancement (CV9-1)** : par l'outil d'exécution de l'agent **en
  arrière-plan** avec un délai de **deux heures** (7 200 000 ms), jamais par `nohup … &`, jamais au premier plan borné à dix
  minutes ; la variable `MESURE_INSTANCE` (lignée et modèle qui lancent) est **obligatoire** en mode réel. **Durée dite**
  (CV8-1) : l'étape (2) prend environ 40 minutes de processeur avec 430 sondes, plus environ 10 minutes pour la table si
  E ≠ 60. **Une seule exécution réelle (CV10-1)** : l'étape 0 pose un **témoin** `execution-reelle-v14.commencee` (`noclobber`,
  jamais effacé) et refuse toute sortie réelle **nommée explicitement** (`sortie-reelle-v14.json` et son `.partiel`, noms passés
  en arguments à la garde, CV13-1) — plus
  jamais un préfixe que la répétition partage ; la répétition écrit dans le **sous-dossier** `repetition-v14/`, hors de portée
  de la garde, mais **passe par la même étape 0** (fonction `etape_0`), pour que les gardes soient exercées par leurs tests déposés (R5, CV11-3) ; la sortie réelle
  est écrite dans un fichier temporaire renommé à la fin ; un `.partiel` ne s'ouvre jamais. **Interrompue** avant la sortie
  finale scellée → **version nouvelle du préenregistrement** (R12) ; interrompue **après** l'étape (2) → reprise par
  `LECTURE_SEULE COMMIT`, qui rejoue les seules étapes (3) et (4), déterministes, sans lire aucune donnée, **ne réécrit aucun fichier scellé** (`sceller`
  refuse d'écraser), **vérifie la lecture déjà scellée avant d'en tirer la note** (CV11-1), **refuse par la garde isolée `garde-lecture-seule-v12.sh`** (sortie 7, jamais de mort silencieuse sous `set -e` : c'était le défaut CV11-1 de la v11) si la note est déjà scellée (CV10-2), vérifie le compagnon de la table en vigueur et compare le
  commit au manifeste (sortie 8). Un **test déposé** `test-lecture-seule-v14.sh` exerce ce mode sur une copie isolée et une sortie artefact scellée — garde isolée (0 et 7), mode complet (commit faux → 8, cas sain → 0 note refaite, second appel → 7, note supprimée lecture scellée → 0, lecture corrompue → ≠ 0, sortie absente → 6) — et **la répétition le lance** (R5). **Répétition générale faite** (CV7-1) sur `synthetique-format-reel-repetition.npz` (`447dc136…`, 3 sondes
  réelles, 2 placebo, E = 60 ; **le fichier déposé lui-même**, de même empreinte et hors de `donnees/`, est le chemin lu, CV11-2(f)), sous `repetition-v14/` (la répétition de la v13, sous `repetition-v13/`, reste déposée telle quelle), déposée et scellée **dans le commit qui porte ce texte** ; en mode `REPETITION`, la séquence refuse un chemin de données sous `donnees/` **et** toute empreinte annoncée égale à celle des données réelles, quel que soit le chemin (CV13-3) — la séquence va
  jusqu'à la note (qui dit « RÉPÉTITION GÉNÉRALE … aucune donnée réelle ») ; les gardes « témoin » et « reprise » sont exercées par leurs tests déposés sur un **état planté qui reproduit l'état déposé** (R5, CV11-2(g) ; le test de la garde témoin plante les noms v14 et vérifie qu'ils figurent dans la séquence, CV13-1). Table gelée de M2 bis et M4 : `table_m2bis_m4_v8.py` (`7e512516b233d58be00703f8c8eada1ce53551188d79bd0d5b117c9c7e75e0d3`) → `table-m2bis-m4-v8.json`
  (`f63faada54a7b2432315c6766be988ea3bcd0049cff35199ca8234da5c98b120` ; compagnons `.sha256` à côté, CV4-5 ; **même quantité de M4 et même excès apparié que le
  script** : par sonde, moyenne des taux des cinq statistiques de somme, médiane sur les sondes ; excès = **médiane sur les
  sondes de la différence par sonde** entre cette quantité et la même à τ = 0, CV5-2), code v8 lui-même, mondes synthétiques à r₀ connu, E = 60, longueurs valides uniformes de 5 à 10 ; **si le
  nombre d'épisodes gardés E diffère de 60** (lu par `--effectifs-seulement`, qui n'écrit aucun taux), la table est **refaite
  au E observé et aux longueurs valides observées** (`--E <E> --longueurs-json <sortie des effectifs>`) et scellée avant toute
  lecture d'un taux ; si E = 60, la table gelée à longueurs uniformes sert telle quelle (dit : la prédiction est faite à
  longueurs uniformes).
- Documents qui font foi (chemin + empreinte) : synthèse du tour « mesures fortes »
  `docs/notes/collisionneur-mesures-fortes-v1/synthese-mesures-fortes-v1.md` (`bed9107b67c969e0e9a97336000a569faf2c519dd556731ace14f29de404885e`,
  sur `main`) ; données : `donnees/20261019-230011-p3-reel/scores-p3.npz`
  (`968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf`, compagnon conforme ; **comparée par le script** ; fichier suivi dans l'arbre de `main` — objet git
  `86ec9eaf2aac32ad9b5b3e68eb8f12d4a1a8bc56`, entré avec le commit de consolidation `9b7721c7` du 9 novembre —, identique à
  l'objet de `calcul/p3-reel-v1` (`eb572dac`) ; empreinte vérifiée le 10 novembre par `sha256sum` sur l'objet de cette branche ;
  **jamais ouvert** par l'auteur de la v14 avant le scellement) ;
  code de référence `src/controle_ia/bases/sequentiel.py` (`35a0983404d7a10d0bb736fa37307a108501785a207c27346be1cd02bab11ba8` ;
  T0.8 ; sa docstring, lignes 7 et 8, est la **seule source** ici du
  chiffre « la règle de Ville atteint 0,21 à 0,35 de faux positifs sous effet épisode (T0.3, P8) » : cité comme tel, non
  vérifié sur le run T0.3) ; programme v2 § 3 et § 8.3 ; N-007 ; mot de Lazar du 27 octobre 23:47 heure de Paris : « go ».

## Hypothèse

**Objet.** La synthèse place à l'unanimité en tête des mesures le taux de fausses alertes de l'agrégateur séquentiel **par
épisode honnête entier**, sans puis avec corrélation injectée, le comparateur de H2 devant être **calibré par épisode entier**
(programme v2 § 3, § 8.3 ; synthèse, convergences : « à 1 % par action, environ 40 % des épisodes honnêtes de 50 actions
alertent, sous indépendance », 1 − 0,99⁵⁰ = 0,395). Elle demande aussi de **trancher au préenregistrement** deux critiques de
T2-C : **A(a)1** (sur « chaque action sous le seuil », un comparateur recalibré au maximum a un rappel nul par construction)
et **A(a)3** (une corrélation injectée **aussi au calibrage** passe la garde par construction). Décisions : A(a)1 ne concerne
pas cette mesure (aucun rappel n'est mesuré ici : épisodes honnêtes seulement ; à trancher au préenregistrement de H2a) ;
A(a)3 est **acceptée** : c'est pourquoi M3 est ici un **contrôle de justesse** du code et de l'échangeabilité, pas une preuve,
et pourquoi un **bras M4** mesure la dépendance que le calibrage n'a pas vue.

**Hypothèses de travail (quatre énoncés).**
- **M1 — le comparateur par action n'est pas un comparateur par épisode.** Seuil à τ_a = 1 % **par action** (quantile des
  actions honnêtes de calibrage) : taux de fausses alertes **par épisode** ≈ 1 − (1 − τ_a)^T sous indépendance (T de 5 à 10
  actions valides : 0,0725 pour T uniforme, 0,077 pour T = 8), au-dessus de α = 5 % ; décroissant quand la corrélation
  intra-épisode croît (moins de tirages effectifs ; presque un théorème).
- **M2 — la règle de Ville calibrée sous indépendance ne tient pas sous dépendance intra-épisode.** Processus e unilatéral
  (ρ = 0,5) au seuil log(1/α). Deux lectures : **M2 ter, la seule qui parle de P3** — à τ = 0, le taux par épisode sur les
  scores réels dépend de la dépendance **naturelle** r₀ (table gelée, code v8 : 0,00 à r₀ = 0 ; 0,033 à 0,2 ; 0,083 à 0,5 ;
  0,133 à 0,8) : s'il dépasse α, **le Seuil dit pourquoi** (neuf feuilles, dont huit au-dessus de α : marges, structure, dépendance,
  dérive avec le pas mesurée, ou non attribuable) ;
  **M2, contrôle du mécanisme** — à τ = 2 (effet injecté), le taux est au-dessus de α pour tout r₀ (table : 0,138 à 0,152) :
  c'est vrai par construction et ne dit rien de P3 ; la **différence** τ = 2 moins τ = 0 (M2 bis) décroît avec r₀
  (table : +0,138 ; +0,104 ; +0,065 ; +0,019) et n'est lue que conditionnellement au r₀ médian mesuré. **Réserve (CV3-4)** :
  Ville suppose des scores standardisés gaussiens ; la **forme des marges** seule (asymétrie) fait monter son taux à τ = 0
  sans aucune dépendance (contre-lecture v3, **moyennes** sur ses mondes : 0,005 gaussien, 0,016 Student à 3 degrés, 0,041
  lognormal ; ici on lit des médianes, l'ordre de grandeur vaut). D'où le **bras
  « mélange »** : les scores des actions valides sont permutés entre tous les épisodes (marges gardées, r₀ → 0) ; Ville à
  τ = 0 sur le mélange mesure l'effet des marges seules ; la différence « réelles moins mélange » isole la **structure
  intra-épisode** (dépendance **ou** dérive commune avec le pas : des scores qui montent avec le rang de l'action survivent au
  mélange aussi peu que la dépendance, CV4-4). D'où un second bras, **« mélange à pas fixé »** : à chaque pas, les scores sont
  permutés entre les épisodes valides à ce pas (les marges par pas sont gardées, la dérive avec le pas survit, la dépendance
  intra-épisode est détruite) ; la différence « réelles moins mélange à pas fixé » ne porte que la dépendance. Et si le
  mélange complet dépasse déjà α, les marges et la dépendance **s'ajoutent** : « marges et dépendance », pas « suffisante ».
- **M3 — contrôle : le calibrage conforme par épisode entier tient quand calibrage et évaluation partagent la dépendance**
  (vrai par théorème : échangeabilité). Niveau exact d'un pli : (K + 1 − ⌈(K + 1)(1 − α)⌉)/(K + 1) — 2/40 = 0,05 pour K = 39 ;
  **L** = moyenne de ce niveau sur les plis, pondérée par la taille du pli, consignée au manifeste (CV3-5). Les **24 cellules**
  de M3 : six statistiques × quatre τ, sondes réelles, calibrage partagé (le bras M4, le bras descriptif, le mélange et le
  mélange à pas fixé n'en font pas partie). Un écart ne peut venir que d'un bogue, d'une rupture d'échangeabilité (effet tâche, ordre) ou de la
  granularité (1/E par épisode).
- **M4 — la dépendance que le calibrage n'a pas vue casse les statistiques de somme, pas le maximum** (T2-C A(a)3, le
  théorème négatif tel qu'il se présente en pratique) : calibrage (normalisation et seuils) sur les scores **sans** effet ;
  évaluation sur m + (x − m + τ·σ·u)/√(1 + τ²) à τ = 2 — **mêmes deux premiers moments marginaux** qu'au calibrage (la forme
  des marges se rapproche de la gaussienne : le bras est plutôt prudent, CV3-6) ; tirages d'effet : ceux de τ = 2. La lecture
  se fait en **excès apparié** (CV4-2 (a)) : quantité de M4 (par sonde, moyenne des taux des cinq statistiques de somme) **moins
  la même quantité à τ = 0** sous le même calibrage, par sonde ; médiane sur les sondes réelles ; intervalle par grappes
  apparié — un défaut qui monterait le niveau des conformes (fuite, rang, plis) jusqu'à un M3 « fragile » monterait les deux
  termes et non l'excès. Prédiction conditionnelle à r₀ (table gelée) pour l'**excès** : ≈ 0,143 à r₀ = 0 ; ≈ 0,073 à 0,2 ;
  ≈ 0,027 à 0,5 ; ≈ 0,006 à 0,8 (quantité de M4 brute : 0,19 ; 0,12 ; 0,075 ; 0,054, rapportée) ; **maximum conforme ≤ α à
  tout r₀** (table : 0,019 à 0,026, soit 0,4 à 0,5 L).
  Le bras de la v2 (effet ajouté sans renormalisation : la variance marginale est multipliée par 1 + τ² = 5) est gardé
  comme **descriptif** « dérive d'échelle et de dépendance », sans verdict (toutes les méthodes y alertent à ≈ 0,25).

## Prédiction chiffrée et signe attendu

| énoncé | quantité (médiane sur les 30 sondes réelles ; intervalle à 95 % par rééchantillonnage des épisodes) | prédiction | signe | réfutation |
|---|---|---|---|---|
| M1 | taux du comparateur par action à τ = 0 | 0,05 à 0,12 (point 0,073 à 0,077) | > 0,05 | médiane ≤ 0,03 |
| M1 bis | le même, de τ = 0 à τ = 2 | décroissant | — | croissant |
| M2 ter (**la lecture sur P3**) | Ville à τ = 0 sur les réelles ; sur le **mélange** ; sur le **mélange à pas fixé** ; différences de médianes D (réelles moins mélange) et D′ (réelles moins mélange à pas fixé), et dérive mesurée (mélange à pas fixé moins mélange), toutes sur **le même tirage** d'épisodes (intervalles par grappes appariées, CV6-2) ; r₀ médian (rapporté, jamais une condition) | réelles : la valeur de la table au r₀ médian observé (0,00 ; 0,033 ; 0,083 ; 0,133 pour r₀ = 0 ; 0,2 ; 0,5 ; 0,8, interpolé), ± 0,05 ; mélange : ≈ 0,005 si marges gaussiennes, jusqu'à 0,04 si très asymétriques ; mélange à pas fixé ≈ mélange (aucune dérive de pas attendue) ; différences > 0 dès que r₀ ≥ 0,2 (synthétique v8 : ≈ +0,03 pour les deux à r₀ = 0,2) | différences > 0 | aucune réfutation formelle : l'issue est celle du Seuil (neuf feuilles) ; r₀ rapporté |
| M2 (contrôle du mécanisme, sous effet injecté) | Ville à τ = 2 | 0,10 à 0,17 pour tout r₀ (table : 0,138 à 0,152) | > α | médiane < 0,075 (bogue : audit ; même seuil que le Seuil, CV6-3) |
| M2 bis (secondaire ; « conforme » ou « hors table » rapporté à tout r₀, réfutation seulement si r₀ < 0,5) | différence des médianes de Ville, τ = 2 moins τ = 0 | la valeur de la table au r₀ médian observé, ± 0,05 (+0,138 ; +0,104 ; +0,065 ; +0,019 pour r₀ = 0 ; 0,2 ; 0,5 ; 0,8, interpolé) | > 0 si r₀ < 0,5 ; **aucune réfutation si r₀ ≥ 0,5** (le mécanisme est présent et la différence tend vers 0) | « hors table » si l'écart dépasse 0,05 ; rapporté ; **réfutée** si r₀ < 0,5 et borne haute de la différence ≤ 0 → **audit R4 de cohérence** avec le contrôle M2, qui suspend la lecture (CV8-3, CV9-3) |
| M3 (contrôle) | les 24 cellules (6 statistiques × 4 τ, réelles) ; niveau L du manifeste (0,05 si E = 60) ; granularité 1/E ; borne haute B = max(2 L ; 0,10) | **tenu (fragile compris)** si toutes les médianes ≤ B ; **fragile, rapporté, la lecture continue** si une médiane est dans ]1,6 L ; B] ou < 0,4 L ; **audit R4** si une médiane > B | ≈ L | une cellule > B → audit |
| M4 (dépendance seule) | bras à variance marginale constante, τ = 2 : **excès apparié de M4** (quantité de M4 moins la même quantité à τ = 0, par sonde ; médiane sur les réelles ; intervalle par grappes apparié, calculé par le script) ; quantité brute rapportée ; maximum conforme | excès : valeur de la table au r₀ médian observé (0,143 ; 0,073 ; 0,027 ; 0,006 pour 0 ; 0,2 ; 0,5 ; 0,8, interpolé ; table refaite au E et aux longueurs observés si E ≠ 60), ± 0,05 ; **max ≤ 0,08** | excès > 0 si r₀ < 0,5 ; max ≈ 0,02 (0,4 à 0,5 L) | si r₀ médian < 0,5 : réfuté si l'excès ≤ 0 ; si r₀ ≥ 0,5 : **non lisible à τ = 2** (dépendance naturelle déjà forte), rapporté ; max > 0,10 → audit, à tout r₀ |
| descriptif | bras « dérive d'échelle et de dépendance » (v2) ; bras « mélange » et « mélange à pas fixé » hors Ville | ≈ 0,25 partout ; mélanges conformes ≈ L, par action ≈ M1 | — | rapportés, sans verdict |
| contrôle placebo | sondes placebo contre réelles, **les 24 cellules de M3 seulement** (calibrage partagé : niveau L quel que soit r₀) ; en plus le maximum conforme du bras M4 (≈ 0,02 pour tout r₀) | mêmes médianes à ± 0,02 | — | écart > 0,05 **sur une des 24 cellules de M3 ou sur le maximum conforme du bras M4** → audit R4 ; pour M1, M2, la quantité et l'excès de M4, les sommes du bras M4, le descriptif et les mélanges, l'écart est **rapporté avec le r₀ des deux groupes**, sans verdict (CV3-1 : un r₀ différent entre réelles et placebo est légitime) |

## Métrique

- **Unité** : l'épisode honnête de P3 (condition `honnete` : 60 épisodes, 10 actions dont une partie `valide`) ; gardés :
  ≥ 5 actions valides ; actions invalides sautées (longueur variable T_e).
- **Score** : score par action de chaque sonde (30 réelles ; 400 placebo appariées en covariance ; le script **vérifie** ces
  effectifs et sépare par le mot `plancher` dans le nom), tel qu'enregistré ; **tout score d'une action valide doit être fini**
  (garde, R5 : testée sur un artefact).
- **Taux de fausses alertes par épisode** (méthode, statistique, sonde) : part des épisodes gardés en alerte, chacun évalué
  une fois par validation croisée en 10 plis = tranches d'une **permutation** tirée par la graine ; calibrage sur les autres
  plis, **dans l'ordre de la permutation** : les 15 premiers à la normalisation (μ₀, σ sur les actions), les K = E − ⌈E/10⌉ − 15
  suivants aux seuils (statistiques finales ; seuil au rang conforme ⌈(K + 1)(1 − α)⌉ ; niveau exact du pli
  (K + 1 − rang)/(K + 1), L = moyenne de ce niveau sur les plis pondérée par leur taille ; infini si le rang dépasse K : garde).
- **Méthodes** : `par_action` ; `ville` (ρ = 0,5, seuil log(1/α)) ; `conforme` (max, somme terminale, somme séquentielle,
  Page k = 0,5, processus e, balayage w = 3) ; **bras M4** : calibrage (normalisation et seuils) sur les scores sans effet,
  évaluation avec effet, τ = 2.
- **Corrélation injectée** : effet épisode u_e ~ N(0, 1) **commun à toutes les sondes** pour un (τ, tirage), multiplié par
  τ·σ_sonde (écart type des scores valides de la sonde) et ajouté aux scores bruts de tous les épisodes avant toute
  standardisation ; τ ∈ {0 ; 0,5 ; 1 ; 2} ; 20 tirages par τ > 0 ; taux moyenné sur les tirages. **Bras M4** : calibrage
  sur les scores sans effet, évaluation sur m + (x − m + τ·σ·u)/√(1 + τ²), τ = 2 (variance marginale constante) ; **bras
  descriptif** : même chose sans la division par √(1 + τ²). Le balayage court sur les actions valides consécutives (les
  invalides sont sautées).
- **Corrélation naturelle r₀** par sonde : corrélation intraclasse (analyse de variance à un facteur, épisodes) des scores
  par action, bornée à [−1 ; 1] (le dénominateur nul — scores constants — est une garde) ; médiane et quartiles sur les
  réelles et sur les placebo ; r₀ du mélange rapporté (attendu ≈ 0).
- **Bras « mélange »** (CV3-4) : pour chaque sonde et chaque tirage, les scores des actions valides sont permutés entre
  toutes les actions valides de tous les épisodes (graine `SeedSequence(20261028, spawn_key=(7, 1))`, 20 enfants) ; même
  calibrage et mêmes plis qu'à τ = 0 ; Ville, par action et les six conformes rapportés ; la différence « réelles moins
  mélange » de Ville à τ = 0 avec son intervalle par grappes.
- **Bras « mélange à pas fixé »** (CV4-4) : à chaque pas t, les scores des épisodes valides à ce pas sont permutés entre eux
  (graine `SeedSequence(20261028, spawn_key=(7, 2))`, 20 enfants) ; même calibrage et mêmes plis qu'à τ = 0 ; mêmes
  rapports que le mélange ; la différence « réelles moins mélange à pas fixé » de Ville à τ = 0 avec son intervalle par
  grappes ; r₀ du mélange à pas fixé rapporté (attendu ≈ 0 **sans dérive** ; loin de 0, il signale une dérive avec le pas
  qui biaise r₀ vers le bas, CV5-4). « Pas » = l'indice brut de l'action dans l'épisode (invalides comprises), pas le rang
  parmi les valides.
- **Corrélation intraclasse sur scores centrés par pas** (CV5-4) : r₀ recalculé après retrait, à chaque pas, de la moyenne
  des scores valides à ce pas ; rapporté à côté de r₀ (réelles et placebo), **jamais une condition** ; un écart de plus de
  **0,05** entre les deux médianes dit qu'une dérive avec le pas, **ou un effet épisode lié à la longueur** (CV7-6), pèse
  sur r₀, et la lecture de M4 et de M2 bis (conditionnelles au r₀ médian) le dit **en réserve** (CV6-5).
- **D, D′ et dérive mesurée** (CV6-2) : D = médiane sur les sondes réelles de Ville à τ = 0 sur les réelles **moins** médiane
  sur le mélange ; D′ = la même moins la médiane sur le mélange à pas fixé ; dérive mesurée = médiane sur le mélange à pas
  fixé moins médiane sur le mélange ; les trois sont des **différences de médianes**, rééchantillonnées sur **le même tirage
  d'épisodes** (2 000 tirages), bornes basses « bb » comparées après arrondi à 10⁻⁹.
- **Quantité de M4** (CV3-2) : par sonde réelle, moyenne des taux des cinq statistiques de somme (somme terminale, somme
  séquentielle, Page, processus e, balayage) ; médiane sur les sondes ; intervalle à 95 % par rééchantillonnage des épisodes
  (grappes) ; **calculée par le script** (`M4_quantite`) ; la table gelée calcule la même.
- **Excès apparié de M4** (CV4-2 (a), CV5-2) : par sonde réelle, quantité de M4 moins la même quantité (cinq sommes, même
  sonde, même calibrage sans effet, mêmes plis) à τ = 0 — la différence est prise **par sonde**, puis la **médiane sur les
  sondes** ; intervalle à 95 % par rééchantillonnage des épisodes **apparié** (le même tirage d'épisodes pour les deux
  termes de chaque sonde) ; la différence des médianes est rapportée à côté, sans verdict ; **calculé par le script**
  (`M4_exces_apparie`) ; la table gelée calcule le même (médiane des différences par couple monde-sonde).
- **Résumés** : médiane, quartiles, part > 2α par groupe de sondes ; intervalle à 95 % de la médiane par rééchantillonnage
  des épisodes (grappes ; 2 000 rééchantillonnages) — **conditionnel aux calibrages** (les plis ne sont pas rééchantillonnés :
  intervalle un peu étroit pour Ville, prudent pour le par-action ; dit, CM-8).
- α = 0,05 ; τ_a = 0,01.

## Seuil

M1 : confirmé si médiane à τ = 0 ≥ 0,06 et borne basse > 0,03 ; réfuté si médiane ≤ 0,03 ; non concluant sinon.
M2 (contrôle) : attendu si médiane à τ = 2
≥ 0,075 ; sinon audit (bogue ; le même seuil partout, CV6-3). M2 bis : « conforme à la table » si l'écart à la valeur interpolée au r₀ médian est ≤ 0,05 ;
sinon « hors table », rapporté ; **réfutée** si r₀ médian < 0,5 et borne haute de la différence ≤ 0 (CV7-6) — c'est alors un
**audit de cohérence** avec le contrôle M2, qui **suspend la lecture** (CV8-3) ; aucune réfutation si r₀ médian ≥ 0,5. **Cellule de M3 à zéro** (médiane et troisième quartile nuls : au moins trois sondes sur quatre sans aucune
alerte) : **audit R4** (trop propre ; CV7-2) ; une cellule à zéro dans un bras (M4, descriptif, mélanges) : réserve rapportée,
pas un audit. M3 : avec L le niveau du manifeste et B = max(2 L ; 0,10) :
**tenu (fragile compris)** si les 24 médianes sont ≤ B ; **fragile** (rapporté, la lecture continue, la première ligne de
lecture s'applique) si une médiane est dans ]1,6 L ; B] ou < 0,4 L ; **audit R4** si une médiane > B (rien d'autre n'est lu
avant l'audit). M4 : si r₀ médian < 0,5 : confirmé si l'**excès apparié** > 0,02 et sa borne basse > 0, **et** médiane du maximum
conforme ≤ 0,08 ; réfuté si l'excès ≤ 0 ; sinon non concluant ; si r₀ médian ≥ 0,5 : non lisible, rapporté ; maximum > 0,10
→ audit, à tout r₀. M2 ter, **une seule définition** (CV4-1, CV5-1, CV5-3), un arbre lu dans cet ordre, r₀ rapporté et
jamais condition ; « bb » = borne basse de l'intervalle par grappes ; D = différence de Ville à τ = 0 réelles moins mélange ;
D′ = réelles moins mélange à pas fixé :
(1) « Ville tenue sur P3 à τ = 0 » si la médiane de Ville sur les réelles est ≤ 0,05 ; sinon (Ville réelles > α) :
(2) si bb(D) ≤ 0 : (2a) « marges seules » si Ville sur le mélange a une médiane > α (D′ rapportée ; si bb(D′) > 0 alors que
bb(D) ≤ 0, **réserve** : incohérence entre les deux mélanges, CV8-4) ; (2b) « **non attribuable** » sinon (ni les marges ni la structure
établies ; rapporté avec D et D′) ;
(3) sinon (bb(D) > 0), si Ville sur le mélange > α : (3a) « marges et dépendance » si bb(D′) > 0 ; (3b) « marges et structure
intra-épisode » sinon (dérive avec le pas possible) ;
(4) sinon (bb(D) > 0, Ville mélange ≤ α) : si bb(D′) > 0 : (4a) « **dépendance naturelle suffisante** » si Ville sur le
mélange à pas fixé a une médiane ≤ α ; (4b) « dépendance établie, mélange à pas fixé au-dessus de α » sinon (le mot
« dérive » n'y est écrit que si la dérive mesurée a une borne basse > 0, CV7-3 ; la lecture v5 porte la même étiquette, CV8-2) ; et si bb(D′) ≤ 0 : (4c) « structure
intra-épisode avec dérive de pas **mesurée** » si bb(dérive mesurée) > 0, (4d) « structure intra-épisode **non attribuée** »
sinon (CV6-2 : on n'écrit « dérive » que si elle est mesurée).
Neuf feuilles, exhaustives et disjointes ; toute comparaison à une borne se fait après arrondi à 10⁻⁹ (CV6-4). **Tout audit
(M3, M2 contrôle, M2 bis réfutée, maximum du bras M4 > 0,10, placebo, cellule de M3 à zéro) suspend la lecture** : les verdicts sont rapportés sans être lus, la
ligne de lecture est « audit R4 avant toute lecture » (CV6-1). Aucun test formel ajouté.

## Plan d'analyse

- **Données** : `scores-p3.npz`, condition `honnete` seule ; empreinte comparée par le script (`--empreinte-attendue`) ;
  effectifs de sondes vérifiés (`--sondes-reelles 30 --sondes-placebo 400`).
- **Taille** : 60 épisodes, ≥ 44 gardés attendus (liste d'arrêt sinon) ; avec 60 gardés : plis de 6, calibrage 54 =
  15 + 39, K = 39, rang 38, niveau exact 0,05.
- **Graines** (R9) : `SeedSequence(20261028)` → enfants 0 (permutation), 1 (synthétique), 2 (rééchantillonnage) ; effets
  épisode `SeedSequence(20261028, spawn_key=(⌊10τ⌋, 1))` → 20 enfants, un vecteur commun à toutes les sondes par enfant.
- **Cellules** : 8 (méthode × statistique) × 4 τ + 8 du bras M4 + 8 du bras descriptif + 8 du mélange + 8 du mélange à pas
  fixé + r₀ (brut, mélanges, centré par pas) : descriptives ;
  **verdicts** fixés ci-dessus (M1, M2 ter, M3, M4 ; M2 contrôle et M2 bis rapportés) ;
  aucune correction de multiplicité (pas de test) ; placebo en contrôle apparié.
- **Commandes**, après scellement, **toutes lancées depuis le dossier du préenregistrement**
  (`/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/mesures-fortes-v1/mesure-unanime-v1/`, CV5-5),
  interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B`, données par chemin absolu
  `/home/claude/canal-conv-audit-n04/donnees/20261019-230011-p3-reel/scores-p3.npz` : (1) `analyse_fausses_alertes_v8.py
  --reel <chemin absolu> --empreinte-attendue 968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf
  --effectifs-seulement > effectifs-reel-v14.json` (E, K par pli, L, longueurs valides : **aucun taux** ; l'empreinte est
  obligatoire, le script refuse sinon) ; si E ≠ 60, `table_m2bis_m4_v8.py --E <E> --longueurs-json effectifs-reel-v14.json >
  table-m2bis-m4-v8-E<E>.json`, scellée ; (2) **une fois** : `analyse_fausses_alertes_v8.py --reel <chemin absolu>
  --empreinte-attendue 968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf --sondes-reelles 30 --sondes-placebo
  400 --commit <commit du scellement> > sortie-reelle-v14.json` (`--tirages` 20 et `--bootstrap` 2 000 : **fixes** en mode réel,
  le script refuse toute autre valeur) ; sortie scellée ; (3) `lecture_mecanique_v8.py sortie-reelle-v14.json <table en
  vigueur> --empreinte-donnees 968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf --empreinte-script <empreinte
  du script v8> > lecture-mecanique-reelle-v14.json`, scellée ; (4) `rediger_note_lecture_v7.py` → `note-lecture-mecanique-v14.md`,
  scellée, que la note de lecture `lecture-mesure-unanime-v1.md` reprend telle quelle (l'auteur n'y ajoute que des réserves,
  sous le titre prévu) ; **le tout par `MESURE_INSTANCE='…' bash commandes-lecture-reelle-v14.sh <commit du scellement>`, lancé par l'outil
  d'exécution en arrière-plan avec un délai de deux heures** (≈ 40 à 50 minutes ; journal `journal-lecture-reelle-v14.log`),
  répété avec succès sur le fichier synthétique au format réel ;
  manifeste : empreinte du script, commit, empreinte des données, niveau L, K par pli, graines, rééchantillonnages.

## Critères de lecture gelés

| issue | verdict |
|---|---|
| M1 confirmé, M3 tenu, M4 confirmé en excès apparié (r₀ < 0,5) | la synthèse a raison : le comparateur de H2 se calibre **par épisode entier** ; le seuil par action n'est pas un comparateur par épisode ; sous une dépendance que le calibrage n'a pas vue, **les statistiques de somme perdent leur niveau, le maximum non** — c'est le sens exact de A(a)3 (fondée pour les sommes) ; **proposé à Lazar** pour G1 et H2 : bases conformes calibrées sur des épisodes honnêtes **de même structure** que l'épreuve (même organisme, même longueur ; contrôle 19 de la conception du pari, v3 § 5 : dérive de composition calibrage → épreuve) ; le seuil « 1 % par action » ne définit que la sous-population de H2a |
| M1 confirmé, M4 non concluant ou réfuté (r₀ < 0,5) | **pas de dépassement établi** des sommes sous dépendance non vue, à τ = 2 sur 5 à 10 actions ; rapporté avec r₀ ; pas de conclusion sur le théorème négatif |
| M1 non concluant | taux par action entre 0,03 et 0,06 : dépendance intra-épisode modérée ; rapporté avec r₀ et M1 bis |
| M2 ter (4a) : « dépendance naturelle suffisante » | la dépendance **naturelle** des scores de P3 invalide Ville-sous-indépendance, les marges et la dérive avec le pas n'y suffisant pas : résultat sur P3, rapporté avec r₀ |
| M2 ter (4b) : « dépendance établie, mélange à pas fixé au-dessus de α » | la dépendance est établie (D′ > 0) mais le mélange à pas fixé dépasse déjà α : une structure résiduelle (dérive si mesurée) s'ajoute ; rapporté, à regarder par pas |
| M2 ter (2b) : « non attribuable » | Ville dépasse α sur P3 sans que les marges (mélange ≤ α) ni la structure (D non établie) le portent : rapporté avec D et D′, sans attribution |
| M2 ter (3b) : « marges et structure intra-épisode » | les marges (mélange > α) et une structure intra-épisode non établie comme dépendance (D′ non > 0) : rapporté |
| M2 ter (1) : « Ville tenue sur P3 à τ = 0 » | Ville-sous-indépendance tient sur les scores de P3 **à cette longueur** (5 à 10 actions) ; rapporté avec r₀ |
| M2 ter (3a) : « marges et dépendance » | Ville dépasse α sur P3 par la forme des scores **et** par la dépendance (D′ > 0), qui s'ajoutent ; rapporté avec r₀ et les deux différences |
| M2 ter (4c) : « structure intra-épisode avec dérive de pas mesurée » | la différence au mélange complet est > 0 mais pas celle au mélange à pas fixé, **et** le mélange à pas fixé dépasse le mélange : une dérive des scores avec le pas fait monter Ville ; rapporté, à regarder par pas |
| M2 ter (4d) : « structure intra-épisode non attribuée » | D > 0, D′ non établie, dérive non mesurée : une structure intra-épisode existe sans qu'on puisse dire dépendance ou dérive ; rapporté avec D, D′ et la dérive |
| M4 : maximum conforme > 0,10 (à tout r₀) | audit R4 avant tout (le maximum doit tenir son niveau sous dépendance seule : bogue de calibrage ou de bras) ; rien d'autre n'est lu |
| M2 (contrôle) non atteint (médiane < 0,075) | bogue ou effet mal injecté : audit avant toute lecture |
| M1 réfuté | dépendance intra-épisode forte (le maximum ne tire presque qu'une fois) : M1 bis devrait être plat ; r₀ élevé attendu ; le seuil par action n'est pas davantage un comparateur par épisode — il est alors trop **prudent** |
| M2 ter (2a) : « marges seules » | Ville-sous-indépendance dépasse α sur P3 par la **forme** des scores (le mélange, sans structure, dépasse α aussi), D n'étant pas établie ; si bb(D′) > 0 malgré tout, **réserve** (incohérence entre les deux mélanges, CV8-4) ; résultat sur P3, rapporté ; la standardisation gaussienne du processus e est en cause |
| M2 ter (2b) : « non attribuable » avec bb(D′) > 0 | même réserve d'incohérence entre les deux mélanges, rapportée (CV9-3) |
| M3 fragile | rapporté (granularité 1/E, niveau L, sondes corrélées entre elles) ; la lecture continue, la première ligne s'applique |
| M3 audit (une médiane > B) | audit R4 avant tout (bogue de plis, fuite, rupture d'échangeabilité) ; rien d'autre n'est lu |
| M4 non lisible (r₀ ≥ 0,5) | la dépendance naturelle de P3 est déjà forte : le bras à τ = 2 n'ajoute pas assez ; rapporté ; M2 ter porte alors le résultat |
| placebo ≠ réelles sur une des 24 cellules de M3 ou sur le maximum conforme du bras M4 (écart > 0,05) | audit R4 : sur des honnêtes, sous calibrage partagé, rien ne distingue une sonde réelle d'une aléatoire appariée pour une statistique conforme ; pour les autres cellules, rapporté avec le r₀ des deux groupes |
| cellule de M3 à 0 (médiane et troisième quartile nuls) | **audit R4** avant tout : trop propre — seuils infinis (rang > K) ? alertes comptées ? rien d'autre n'est lu |
| cellule d'un bras à 0 | réserve rapportée (le maximum du bras M4 à ≈ 0,02 peut légitimement valoir 0 sur une sonde) |
| M2 bis réfutée (r₀ < 0,5, borne haute ≤ 0) | l'effet injecté n'augmente pas Ville : incohérent avec M2 contrôle attendu → **audit R4 de cohérence** avant tout ; rien d'autre n'est lu |

## Liste d'arrêt

- Moins de 44 épisodes honnêtes gardés → arrêt. K < 1/α − 1 pour une cellule → arrêt (code). Score non fini sur une action
  valide → arrêt (code, testé). Scores constants sur un ensemble de normalisation → arrêt (code, testé). Effectifs de sondes
  ≠ 30 / 400 → arrêt (code). Empreinte des données ≠ `968414fc…` → arrêt (code). Chevauchement normalisation / seuils /
  évaluation : impossible par construction (tranches d'une permutation ; dit).
- Une seule exécution réelle après scellement ; une relance (bogue, **interruption** : `.partiel` laissé par la séquence) =
  version nouvelle, dite dans la note de lecture et la passation.
- En mode réel, `--empreinte-attendue`, `--sondes-reelles`, `--sondes-placebo` et `--commit` sont **obligatoires** (le
  script refuse sinon) ; K par pli est consigné au manifeste.

## Contre-lecture

Sous-agent neuf Opus 5.5 ; brouillon relu : v1, empreinte `7158affc04645bb21fe1f2934fdbbfc9333d5576d55d2f5b562444797b54a935` ;
rapport : `contre-lecture-v1/rapport-contre-lecture-mesure-unanime-v1.md`, empreinte
`5d47ae52d44e81a25604220ba3482db2eec8cfb0fd5b426dcce9484ef15bbf2d`. Traitement : **CM-1** accepté (M3 contrôle, A(a)3 et
A(a)1 tranchées, bras M4 ajouté) ; **CM-2** accepté (M2 principal = Ville > α à τ = 2 ; différence secondaire lue avec r₀,
mesurée par sonde ; ligne « Ville déjà > α à τ = 0 ») ; **CM-3** accepté (gardes codées : finitude, empreinte comparée,
effectifs, K ; testées par `--test-gardes` sur un cas sain et trois artefacts) ; **CM-4** accepté (partage dans l'ordre de la
permutation) ; **CM-5** accepté (15 épisodes de normalisation, K = 39, niveau exact 0,05 dit ; E ≥ 44) ; **CM-6** accepté
(placebo avec verdict sur les conformes seulement) ; **CM-7** accepté (effet commun par tirage) ; **CM-8** accepté (intervalle
dit conditionnel aux calibrages) ; **CM-9** accepté (commit `ffd5968c` qui contient le script ; provenance du chiffre T0.3 P8 :
docstring de `bases/sequentiel.py`) ; **CM-10** accepté (tableau de lecture complété) ; **CM-11** accepté (rapport versé dans
`contre-lecture-v1/`). **Complément sur la v2** (même contre-lecteur que la v1, `contre-lecture-v1/complement-v2.md`, `e5ca74bb…`) : (a) M4 confondu avec
une dérive d'échelle → **accepté** : bras à variance marginale constante, prédiction conditionnelle à r₀ par la table gelée,
ancien bras descriptif sans verdict, « A(a)3 fondée » restreint aux statistiques de somme ; (b) plage de M3 → **accepté** :
zone « fragile », bornes relatives au niveau L du manifeste, une seule définition ; (c) table de M2 bis → **accepté** :
refaite avec le code v3, 20 tirages, 10 mondes, gelée avec empreinte ; réfutation retirée pour r₀ ≥ 0,5 ; M2 à τ = 2 devient
un contrôle du mécanisme, la lecture sur P3 est M2 ter ; (d) gardes d'empreinte et d'effectifs → **accepté** : obligatoires
en mode réel, testées (trois artefacts de chargement, E minimal) ; (e) formulations → **accepté** (« pas de dépassement
établi », « proposé à Lazar », source du contrôle 19, empreinte de `bases/sequentiel.py`, K par pli, docstring, graine du
test par SeedSequence, balayage sur actions valides). (CM-9 : le commit qui contenait le script v2 était `ffd5968c` ; la
v3 était à `b522701b` avec le script à `8c90a573` ; la v4 cite `6906041b`.)
**Contre-lecture de la v3** (sous-agent neuf, autre que le premier, Opus 5.5 ; `contre-lecture-v3/rapport-contre-lecture-mesure-unanime-v3.md`,
`0fb0734a…`, lecture entière, verdict « à corriger en v4 ») : **CV3-1** accepté (verdict placebo borné aux 24 cellules de M3 et au
maximum de M4 ; le reste rapporté avec le r₀ des deux groupes) ; **CV3-2** accepté (quantité unique de M4 calculée par le script
avec son intervalle ; la table calcule la même) ; **CV3-3** accepté (B = max(2 L ; 0,10) ; table refaite au E observé par
`--effectifs-seulement` puis `--E`, avant toute lecture de taux ; cette borne a été simulée sous le nul par la contre-lecture
de la v4 : aucun faux audit sur 340 mondes à τ = 0 à E = 60 et E = 50, et sur 60 mondes aux 24 cellules ; faux « fragile »
0 à 8 % ; `contre-lecture-v4/`) ;
**CV3-4** accepté (bras « mélange » ; lecture « marges seules » distincte de « dépendance naturelle suffisante ») ; **CV3-5**
accepté (formule corrigée ; L = moyenne pondérée sur les plis) ; **CV3-6** accepté (« mêmes deux premiers moments », tirages
de τ = 2) ; **CV3-7** accepté (gardes de E et de la corrélation intraclasse exercées par le test) ; **CV3-8** accepté (« tenu,
fragile compris » ; 24 cellules listées) ; **CV3-9** accepté (contrôle 19 : `pole-scientifique-automatique-v1/pari-de-signe/conception-pari-de-signe-v3.md`,
`1518a12f0c9b755ec6ab0f958d9c6b77f8071d7f959f6e5c5cb60de38a15db14`, ligne 117, cité en v3 parce que c'est la version qui
définit les contrôles 18 à 21 — les v4 à v9 sont des deltas qui ne les réécrivent pas ; docstring ; en-tête ; M1 réfuté ;
M2 ter entre 0,3 et 0,5).
**Contre-lecture de la v4** (troisième sous-agent neuf Opus 5.5 ; `contre-lecture-v4/rapport-contre-lecture-mesure-unanime-v4.md`,
`ef6b8770…`, lecture entière, script lancé en `--test-gardes` et en mode réel sur le fichier synthétique des gardes, simulation
de la règle d'audit de M3 sous le nul, verdict « à corriger en v5 ») : **CV4-1** accepté (une seule définition de M2 ter, en
cinq issues ordonnées ; r₀ rapporté, jamais condition ; « (r₀ ≤ 0,3) » retiré de la ligne des critères) ; **CV4-2** accepté,
option (a) (excès apparié de M4 calculé par le script et par la table ; « confirmé » si excès > 0,02 et borne basse > 0) ;
**CV4-3** accepté (ligne placebo des critères bornée aux 24 cellules de M3 et au maximum conforme du bras M4) ; **CV4-4**
accepté (« marges et dépendance » quand le mélange dépasse déjà α ; bras « mélange à pas fixé » ajouté, « suffisante »
exige la différence au mélange à pas fixé > 0 ; issue « structure intra-épisode avec dérive de pas ») ; **CV4-5** accepté
(empreintes de la table et de son script dans l'en-tête ; compagnons `.sha256` du script, de la table, de sa sortie et de
l'essai synthétique créés au scellement) ; **CV4-6** accepté (niveau (K + 1 − rang)/(K + 1) dans la Métrique ; docstrings
du script et de la table ; « code v5 » ; « max ≈ 0,02 (0,4 à 0,5 L) » ; phrase dédoublée retirée ; `--empreinte-attendue`
dans la commande (1), obligatoire par le code ; `--tirages` et `--bootstrap` fixes en mode réel par le code ; « audit à tout
r₀ » ; longueurs réelles passées à la table par `--longueurs-json` si E ≠ 60, prédiction à longueurs uniformes dite sinon ;
renvoi à la simulation de la contre-lecture pour B sous le nul ; « quinze entrées, quatorze gardes et une valeur »).
**Contre-lecture de la v5** (quatrième sous-agent neuf Opus 5.5 ; `contre-lecture-v5/rapport-contre-lecture-mesure-unanime-v5.md`,
`912dd47a…`, lecture entière, essai synthétique reproduit à l'octet, excès et mélange à pas fixé vérifiés par simulation,
gardes et refus vérifiés en lançant, verdict « à corriger en v6 », aucun constat grave) : **CV5-1** accepté (colonne
« réfutation » de M2 ter : aucune réfutation formelle, l'issue est celle du Seuil ; Hypothèse M2 : « le Seuil dit pourquoi ») ;
**CV5-2** accepté, option (a) (excès = médiane sur les sondes des différences par sonde, dans le script comme dans la
table ; différence des médianes rapportée à côté) ; **CV5-3** accepté (arbre à huit feuilles : « marges seules » exige le
mélange > α, sinon « non attribuable » ; « marges et dépendance » exige D′ > 0, sinon « marges et structure » ;
« suffisante » exige Ville sur le mélange à pas fixé ≤ α, sinon « dérive et dépendance » ; lignes des critères ajoutées) ;
**CV5-4** accepté (« attendu ≈ 0 sans dérive » ; r₀ sur scores centrés par pas rapporté, jamais condition ; « pas » = indice
brut) ; **CV5-5** accepté (commandes depuis le dossier du préenregistrement, chemins absolus) ; **CV5-6** accepté (cellules du
mélange à pas fixé ; liste de M3 ; décompte des gardes ; `bootstrap` au manifeste ; docstring de `un_passage` ; « moyennes »
de la contre-lecture v3).
**Contre-lecture de la v6** (cinquième sous-agent neuf Opus 5.5 ; `contre-lecture-v6/rapport-contre-lecture-mesure-unanime-v6.md`,
`23ce5f93…`, verdict « à corriger en v7 », CV5-1 à CV5-6 et restes de CV4 fermés) : **CV6-1** accepté (tout audit — M3, M2
contrôle, maximum du bras M4, placebo — suspend la lecture ; ligne des critères pour le maximum de M4 ; lecture mécanique
v3) ; **CV6-2** accepté (D, D′ et dérive sur le même tirage d'épisodes ; dérive **mesurée** avant d'écrire « dérive » :
feuilles (4c) et (4d)) ; **CV6-3** accepté (seuil 0,075 du contrôle M2 partout) ; **CV6-4** accepté (arrondi à 10⁻⁹ avant
comparaison) ; **CV6-5** accepté (seuil 0,05 de la réserve sur r₀ écrit ; M2 bis « hors table » rapporté à tout r₀ ; cellule à
zéro = médiane et troisième quartile nuls ; D et D′ dits différences de médianes) ; **CV6-6** accepté (« huit issues au-dessus
de α » ; « +0,03 » attribué à l'essai v7 ; sortie du test de la lecture déposée ; garde endormie qui lève ; empreintes dans la
sortie des effectifs ; manifeste et E vérifiés par la lecture). La v7 est relue par un sous-agent neuf avant scellement ; si
« à sceller tel quel », elle est scellée sans autre modification ; sinon v8.
**Contre-lecture de la v7** (sixième sous-agent neuf Opus 5.5 ; `contre-lecture-v7/rapport-contre-lecture-mesure-unanime-v7.md`,
`7783ab01…`, verdict « à corriger en v8 » ; essai synthétique et table v7 reproduits à l'octet ; arbre vérifié sur 64
combinaisons ; refus du mode réel vérifiés) : **CV7-1** accepté, **bloquant** (E au manifeste dans les deux modes ; lecture
v4 ; **répétition générale** de la séquence sur un fichier synthétique au format réel, déposée) ; **CV7-2** accepté (cellule
de M3 à zéro = audit R4 qui suspend ; bras à zéro = réserve) ; **CV7-3** accepté (feuille (4b) renommée sans le mot
« dérive » ; D′ rapportée en (2a)) ; **CV7-4** accepté (essai de la lecture = sortie brute d'un script déposé, sur la table v8,
feuilles et audits compris) ; **CV7-5** accepté (lecture : empreinte du script, tirages, rééchantillonnages, commit ; script
de séquence scellé et cité) ; **CV7-6** accepté (« neuf feuilles » ; réfutation de M2 bis définie ; réserve sur r₀ dite
« dérive ou effet lié à la longueur » ; M1 bis après arrondi). La v8 est relue par un sous-agent neuf avant scellement ; si
« à sceller tel quel », elle est scellée sans autre modification ; sinon v9.
**Contre-lecture de la v8** (septième sous-agent neuf Opus 5.5 ; `contre-lecture-v8/rapport-contre-lecture-mesure-unanime-v8.md`,
`989c02de…`, verdict « à corriger en v9 », répétition rejouée, branche E ≠ 60 exercée, aucun faux « confirmé » trouvé) :
**CV8-1** accepté (durée dite ; fichier temporaire renommé à la fin ; `.partiel` = interruption consignée, relance = version
nouvelle ; lancement en arrière-plan) ; **CV8-2** accepté (lecture v5 : feuille (4b) sans le mot « dérive ») ; **CV8-3** accepté
(M2 bis réfutée = audit de cohérence qui suspend, dans le Seuil, les critères et la lecture) ; **CV8-4** accepté (réserve en
(2a) si bb(D′) > 0) ; **CV8-5** accepté (la séquence lance la rédaction, vérifie son compagnon et celui de la rédaction ; la
rédaction n'écrit « scellé » qu'après vérification) ; **CV8-6** accepté (« neuf feuilles » ; « synthétique v8 » ; commentaire
de la lecture ; refus du mode réel déposés dans l'essai). Point d'information de la contre-lecture, sans constat : avec des
sondes identiques, une des six cellules de M3 à τ = 0 dépasse 0,10 dans 1,7 à 3,0 % des mondes sous le nul (granularité :
7 alertes sur 60) — un audit déclenché par une seule cellule à τ = 0 à 0,10 ou 0,117 sera lu avec cette réserve. La v9 est
relue par un sous-agent neuf avant scellement ; si « à sceller tel quel », elle est scellée sans autre modification ; sinon v10.
**Contre-lecture de la v9** (huitième sous-agent neuf Opus 5.5 ; `contre-lecture-v9/rapport-contre-lecture-mesure-unanime-v9.md`,
`aeeca90d…`, verdict « à corriger en v10 », aucun faux « confirmé » ni faux blocage) : **CV9-1** accepté (lancement par l'outil
en arrière-plan sur deux heures, jamais `nohup … &`, écrit dans le texte et la séquence) ; **CV9-2** accepté (toute trace
`sortie-reelle-v10*` bloque, rien ne se renomme pour relancer ; `.partiel` de la table gardé ; mode `LECTURE_SEULE` pour une
interruption après l'étape (2) ; un `.partiel` ne s'ouvre jamais) ; **CV9-3** accepté (colonne « réfutation » de M2 bis avec la
règle d'audit ; critère de (2a) corrigé ; réserve de (2b) dite) ; **CV9-4** accepté (instance et date en paramètres de la
rédaction ; « répétition » déduite du commit `repetition-generale` ; note scellée par la séquence ; la répétition se fait sur
le texte final et ses fichiers sont déposés dans le commit du texte) ; **CV9-5** accepté (docstrings de la lecture v6 et de
l'essai v6 ; l'en-tête renvoie à la séquence v10). La v10 est relue par un sous-agent neuf avant scellement ; si « à sceller
tel quel », elle est scellée sans autre modification ; sinon v11.
**Contre-lecture de la v10** (neuvième sous-agent neuf, Opus 5.5 ; `contre-lecture-v10/rapport-contre-lecture-mesure-unanime-v10.md`,
`c401043b…`, « à corriger en v11 », aucun faux « confirmé » ni faux blocage, arbre et excès relancés) : **CV10-1** accepté
(bloquant — la garde « toute trace `sortie-reelle-v10*` bloque » attrapait la répétition déposée et empêchait l'unique
exécution ; v11 : témoin `noclobber` et noms explicites, répétition en sous-dossier `repetition-v11/` passant par la même
étape 0, test de la garde sur l'état déposé, R5) ; **CV10-2** accepté (`LECTURE_SEULE` refuse une note déjà scellée, ne réécrit
aucun scellé, vérifie la table en vigueur et compare le commit) ; **CV10-3** accepté (`--instance` obligatoire sans défaut en
dur, mois complets, docstrings de la lecture v7 et de l'essai v7, renvoi de l'en-tête). **Bascule de modèle** : la v11 a été
écrite sous **Opus 4.8** (bascule à 03:20 UTC), donc contre-lue par un sous-agent neuf **Fable 5.1** (modèle différent de
l'auteur, R13).
**Contre-lecture de la v11** (sous-agent neuf **Fable 5.1** ; `contre-lecture-v11/rapport-contre-lecture-mesure-unanime-v11.md`,
`d654dea669ef03d2039d1cb52fdd1f4cb5ee3bd51c776ff4886341970992a825`, « à corriger en v12 », aucun faux « confirmé » ni faux
blocage ; arbre, excès, branche E ≠ 60 et répétition rejoués) : **CV11-1** accepté, **sérieux** (le mode `LECTURE_SEULE` de la
v11 mourait en silence sous `set -e` dès que la note n'était pas scellée — le cas même de la reprise ; v12 : garde isolée
`garde-lecture-seule-v12.sh` en `if … fi` à sortie explicite, vérification de la lecture déjà scellée avant la note, test de
bout en bout déposé et lancé par la répétition, R5) ; **CV11-2** accepté (restes de v10 et incohérences du texte :
`effectifs-reel-v12.json` dans la commande (1), `**` orphelin retiré, citation du commit du script corrigée, durée « ≈ 40 à
50 minutes », « neuvième » contre-lecteur, provenance de la copie du fichier de répétition, garde « exercée sur un état
planté ») ; **CV11-3** accepté (docstrings de la lecture v8 et de l'essai v8, `--date` obligatoire dans la rédaction v6,
`datetime.now(timezone.utc)` au lieu de `utcnow()`, `rm` sans objet retiré, `MESURE_INSTANCE` forcé en répétition, table en
vigueur scellée avant la lecture). La v12 est écrite sous **Opus 4.8** et contre-lue par un sous-agent neuf d'un **modèle
différent** (Fable 5.1, R13) avant scellement ; si « à sceller tel quel », scellée sans autre modification ; sinon v13.
**Contre-lecture de la v12** (sous-agent neuf **Fable 5.1** ; `contre-lecture-v12/rapport-contre-lecture-mesure-unanime-v12.md`,
`a061e2a615a1c875af0235bdbe8f057e762e01f98886d406bce749c5bbcddbf1`, « à corriger en v13 », aucun faux « confirmé » ni faux
blocage ; texte et dépôt seulement, aucun défaut de plomberie) : **CV12-1** accepté (texte, ligne 62 : « une **copie** de ce
fichier » → « **le fichier déposé lui-même** » — le script lit le fichier directement, pas une copie ; la phrase décrivait la
situation de la v11) ; **CV12-2** accepté (dépôt : les répertoires `contre-lecture-v11/` et `contre-lecture-v12/` versés dans
l'arbre) ; **CV12-3** accepté (test : cas B3-bis — note supprimée, lecture scellée → note refaite, lecture inchangée — et
B3-ter — note supprimée, lecture corrompue → refus, aucune note — ajoutés à `test-lecture-seule-v13.sh`) ; **CV12-4** accepté
(docstring : phrase coupée dans `rediger_note_lecture_v7.py` recollée, usage complet). La v13 est écrite sous **Opus 4.6** et
contre-lue par un sous-agent neuf d'un **modèle différent** (R13) avant scellement ; si « à sceller tel quel », scellée sans
autre modification ; sinon v14.
**Contre-lecture de la v13** (sous-agent neuf **Fable 5.1** ; `contre-lecture-v13/rapport-contre-lecture-mesure-unanime-v13.md`,
`71ce7eeaa7c7b71512c5cc4d797f685717a98f7c679cbb58ac29b96ce924117a`, « à corriger en v14 », un défaut de plomberie bloquant et
trois constats non bloquants ; aucun faux « confirmé », aucun faux blocage ; sections de science identiques au bit près à la
v12) : **CV13-1** accepté, **bloquant** (la garde témoin gardée sous son nom v12 testait des noms v12 et ne voyait aucune
trace v13 : elle était morte dans la séquence v13 ; v14 : garde `garde-trace-reelle-v14.sh` **paramétrée**, les trois noms
lui sont passés en arguments par la séquence, comme à la garde de reprise ; son test `test-garde-trace-v14.sh` plante les noms
v14, dont l'état sain `repetition-v14/sortie-reelle-v14.json`, et vérifie que ces noms figurent dans la séquence ; séquence,
test de reprise et texte réécrits ; répétition refaite) ; **CV13-2** accepté **en partie seulement** : les fichiers manquants
des dossiers `contre-lecture-v11/` et `contre-lecture-v12/` étaient dans les bacs à sable de leurs contre-lecteurs, disparus
avec leurs conteneurs ; ce n'est **plus réparable** ; les rapports cités gardent leurs empreintes, et les fichiers versés
restent identiques à leurs sources (`sortie-versement-cv12-2-v1.txt`) ; **CV13-3** accepté (en mode `REPETITION`, refus de
toute empreinte annoncée égale à celle des données réelles, en plus du refus par chemin : le trou du test de préfixe est
fermé quel que soit le chemin) ; **CV13-4** accepté (renvoi de ligne périmé ôté du test de reprise v14 : « dans la branche
`LECTURE_SEULE` »). La plomberie v14 (séquence, garde témoin, deux tests) a été écrite et scellée sur `canal/conv-audit-n04`
(`4d1fa5c0`) avant l'arrêt de la lignée conv-audit ; elle est versée telle quelle, compagnons conformes ; seul ce texte est
achevé par la session-dépôt. **Constat de l'auteur de la v14 sur la plomberie scellée, non corrigé (R12)** : dans
`test-garde-trace-v14.sh`, la ligne 30 affiche « OK noms du test = noms de la séquence v14 » même quand l'une des deux
vérifications de nom échoue (le code de sortie final, lui, reste juste), et la vérification du nom de la sortie se contente
d'une occurrence n'importe où dans la séquence, commentaires compris ; sans effet sur la protection (le témoin `noclobber` et
la garde paramétrée suffisent) ; à juger par la contre-lecture. La v14 est écrite sous **Opus 5.5** et contre-lue par un
sous-agent neuf d'un **modèle différent** (R13) avant scellement ; si « à sceller tel quel », scellée sans autre
modification ; sinon v15.
