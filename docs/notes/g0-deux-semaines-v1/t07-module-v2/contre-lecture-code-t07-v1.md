# Contre-lecture du code du module de lecture de T0.7 v2 (commit `1f77b34d`) contre le brouillon 19 — v1

Contre-lecteur neuf, modèle Fable 5.2 (le développeur est Opus 5.5 ; N-052 nomme Fable 5.1 : écart déclaré par la consigne).
Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-contre-lecture-code-t07-v1.md`
(`84ae77ea…`, vérifiée avant lecture) ; interdits communs `851028fc…` (vérifiés). Texte : `brouillons/T0.7-sondes-v0-v1-brouillon19.md`
(`07039ed2…`, lu par `git show 1f77b34d:`). Code lu par `git show 1f77b34d:<chemin>`. Heures relevées par `date -u`,
le 10 novembre 2026, de 06:37 à 06:58 UTC. Je n'ai écrit ni T0.7, ni son module, ni T0.6, ni P3-bis, ni leurs contre-lectures.
Ayant lu des fichiers de T0.7, je suis exclu de tout rôle de lecteur de P3-bis.

## Verdict (une ligne)

**À corriger avant de citer un commit dans le texte : un défaut bloquant (CT-01, une action sans mot arrête toute l'étape A, vu
dans ma répétition jouet), six défauts à corriger, onze mineurs ou à porter au texte ; le reste du module est conforme au
brouillon 19, l'embargo et l'ordre des lectures tiennent.**

## Table des défauts

| id | gravité | fichier, lignes (au commit `1f77b34d`) | constat | correction proposée |
|---|---|---|---|---|
| CT-01 | **bloquant** | `src/controle_ia/t07/lecture_v2.py` l. 606-618 (`noter`, témoins lexicaux) ; cause dans le paquet gelé `src/controle_ia/sondes/temoins.py` l. 97-103 (`_verifier_textes`) | `x["temoin"].scores(tx)` est appelé hors de tout `try`. Le paquet gelé refuse toute la liste dès qu'un texte d'action n'a aucun caractère de mot (`\w+`). Une seule action vide ou faite de ponctuation arrête donc **toute** l'étape A après le manifeste : code 3, `arret.json`, ni `SCORES-T07` ni `SONDES-T07`. Sous le texte ((b) 5), c'est un nœud sans relance : la lecture de T0.7 sur 7b serait perdue pour un témoin descriptif (T7-P10). **Vu dans ma répétition jouet** : 7 actions sur 84 sans caractère de mot, étape A en code 3, motif « texte d'action vide ou non textuel ». Les deux répétitions du développeur avaient passé : le run jouet de T0.6 tire une entropie neuve à chaque fois. | Entourer la notation de chaque témoin lexical : en échec, le témoin est écrit « échec » avec son motif et le compte des actions sans mot, aucun tableau `lexical_<concept>` n'est écrit, T7-P10 est « non lue : témoin lexical en échec » pour ce concept. Autre voie : noter les seules actions qui portent un mot, les autres exclues et comptées à l'étape B. Le choix change une lecture gelée : il s'écrit au brouillon 20 avant le scellement. Essai R5 : cas sain, et une action sans mot. Fixer l'entropie du run jouet de la répétition, pour qu'elle se rejoue à l'identique. |
| CT-02 | à corriger | `lecture_v2.py` l. 740-744 (manifeste), l. 486-488 (`controler_t07`) | À l'étape complète, `sondes_lues` du manifeste porte `null` pour chaque sonde neuve, et aucune clé du manifeste ne nomme les concepts lus ni les jeux scellés. Avec trois sondes, le manifeste est le même que la sonde lue soit la dissimulation ou le domaine (essai : mêmes listes, concepts différents). À l'étape B, un `null` du manifeste accepte n'importe quel nom. Le périmètre n'est donc fixé que par `sondes-t07.json`, écrit après l'apprentissage. Le texte veut la liste « écrite dans le manifeste avant la première notation ». | Écrire `concepts_lus` et `jeux_scelles` dans la configuration du manifeste (connus à l'ouverture). À l'étape B, exiger que les concepts de `sondes-t07.json` égalent ceux du manifeste et que chaque nom de sonde neuve commence par son concept. Porter l'interprétation 15 au texte. |
| CT-03 | à corriger | `src/controle_ia/t07/lectures_t07_v1.py` l. 410-421 (`reserves`) | Les déclencheurs de R9 « aire > 0,95 ou < 0,05 sur un jeu d'organisme » et « quantile 0,95 d'un plancher > 0,70 » ne sont cherchés que sur les jeux décisifs. Les autres jeux d'organisme lus (`temoin`, `mention`, `T100`, doses hors jugement, T7-P6, T7-P15, directions) n'entrent pas (essai : aire 0,99 sur `T100`, aucune R9). La ligne R9 de la table ne restreint pas aux jeux décisifs. | Balayer toutes les lectures qui portent `aire` et `plancher_quantile` (lectures complémentaires et jeux hors jugement). Sinon, écrire la restriction dans le texte. |
| CT-04 | à corriger | `src/controle_ia/t07/sondes_neuves_v1.py` l. 62, 246, 411 ; `lecture_v2.py`, `exiger_configuration` | Les clés de configuration `familles` et `reglages` sont exigées mais sans effet : le code prend la constante `ORDRE_FAMILLES` et `Reglages()` par défaut. Une configuration autre est ignorée sans un mot (essai : `familles = ["lineaire"]` et des réglages faux, cinq familles apprises aux réglages par défaut). C'est un repli silencieux (R5). | Dans `exiger_configuration` : `familles` égale à la liste gelée, `reglages` nul ou égal aux valeurs par défaut ; sinon arrêt de configuration. Un cas sain et un artefact. |
| CT-05 | à corriger | `sondes_neuves_v1.py` l. 314-316 (`sondes_p6`) ; `lecture_v2.py` l. 587-594 (`noter`, genres `p6` et `concept`) | `preparer_sonde` et `noter_actions` y sont hors de tout `try`. Un essai d'égalité de Mahalanobis en échec pour la sonde de T7-P6 ou son témoin (ou un score non fini) arrête toute l'étape A, code 3 (essai). Le texte dit : « un échec met le couple en échec, jamais l'ensemble ». | T7-P6 « échec » avec motif, T7-P6 « non lue » à l'étape B ; de même pour une direction de concept. |
| CT-06 | à corriger | `lecture_v2.py` l. 990, 1018-1021 (`main`) | `--instant` (« essais seulement » dans l'aide) est accepté en mode réel. Il date l'ouverture, nomme `RUN_T07`, sert à l'antériorité des lignes et à l'instant de fermeture de G5. Hérité de la v1. | Refuser `--instant` quand `mode` vaut `reel`. Un cas sain et un artefact. |
| CT-07 | à corriger | `lecture_v2.py` l. 747-754 puis l. 790-791 (`etape_a`) | Les sondes neuves sont apprises (modèle chargé, extraction, 30 couples) **avant** la garde d'identité et la lecture des épisodes. Le plan (point 8, étape A, 1 puis 2) met la garde d'identité dans la garde d'ouverture, avant l'extraction. Un R11-arret tombe alors après l'apprentissage, avec `sondes-t07.json` et `sondes-neuves-t07.npz` déjà écrits sur un run arrêté. | Jouer `lire_episodes_t06`, `garde_identite` et `charger_mesures` avant `sondes_neuves_v1.apprendre`. Rien n'y est noté. |
| CT-08 | mineur, à porter au texte | `lecture_v2.py` l. 448-451 (`ouvrir`) | Tâche de réserve parmi les tâches d'évaluation, jeu ou phrases mal formés : refus de la garde, code 2, rien écrit. Le texte ((b) 5) range la tâche de réserve parmi les arrêts de code 3. Le code est plus prudent sur les écritures, mais le journal dit « refus » là où le texte dit « nœud ». | Écrire au brouillon 20 que ces fautes sont des refus de la garde, de nature « nœud ». |
| CT-09 | mineur | `src/controle_ia/t07/garde_adaptee_v1.py` l. 205 contre l. 285-298 | Une ouverture réduite datée exactement de la fin de l'étape A compte « avant la fin » pour la garde de fin (`<=`) et s'écrit dans `notation-t07.json`, mais `reserve_r14` est stricte : ni R14 ni issue « finale pour 7b » (essai). Une réduite datée après la fin de l'étape A, que P3-bis b8 exclut, laisse l'étape B possible sans R14 ni marque G4 (essai). | Aligner `reserve_r14` sur `<=`. Refuser (nœud) une réduite postérieure à la fin de l'étape A, ou l'écrire dans le texte. |
| CT-10 | mineur | `garde_adaptee_v1.py` l. 195-209 (`garde_fin_etape_a`) | `VERDICT-P3BIS` inscrite pendant l'étape A avec une ouverture réduite : ni G1 ni l'appui de la réduite ne sont contrôlés à la fin. `SCORES-T07` et `SONDES-T07` sont écrites, et le refus ne vient qu'à l'étape B (essai). Aucune lecture n'a lieu, mais le texte ((c)) veut qu'un arrêt n'écrive aucune de ces lignes. | Jouer `_g1` et `controler_reduite` dans la garde de fin. |
| CT-11 | mineur | `src/controle_ia/t07/journal_p3bis_v1.py` l. 76-101 | L'ordre permis des ouvertures est contrôlé dans l'ordre du fichier ; les dates ne sont pas exigées croissantes, alors que les gardes raisonnent sur les dates (essai : `reduite` datée après `pleine`, accepté). | Dates non décroissantes exigées, sinon `JournalFautif`. |
| CT-12 | mineur | `lecture_v2.py` l. 42-47, 195-197, 278-279 ; `tests/test_t07_lecture_v2.py` l. 244 | En-tête, messages et nom d'essai disent encore que les sondes neuves « ne sont pas calculées ». | Les mettre à jour. |
| CT-13 | mineur, à porter au texte | `sondes_neuves_v1.py` l. 324-342 (`lire_phrases_concepts`), l. 202-214 | Aucun contrôle « au moins quatre concepts » (plan, point 10). Le fichier attendu est unique, avec une première ligne `format_lecture` ; la consigne des concepts (`acc7bdfb…`, brouillon) dit « un fichier par concept » et nomme le format « gabarit d'une action de l'agent », alors que le code offre « message de l'utilisateur ». Aucun essai d'artefact sur ce lecteur. | Contrôle du nombre de concepts ; aligner la consigne des concepts et le brouillon 20 sur le format du code (ou l'inverse) ; un artefact. |
| CT-14 | mineur | `sondes_neuves_v1.py` l. 82-93 ; `lecture_v2.py` l. 643-651 | Les graines des clés nommées après le manifeste sont bien dérivées par `SeedSequence` et par clé, mais seuls leurs noms sont écrits dans les résultats. Les noms des 30 couples, des sondes de T7-P6 possibles et des directions (phrases lues dans la garde) sont connus avant le manifeste. | Les inscrire toutes dans le manifeste (R9 : « consignées dans un manifeste »). |
| CT-15 | mineur | `lecture_v2.py` l. 740-744 ; `src/controle_ia/manifeste.py` l. 86-96 | Rien ne compare la ligne `SCELLEMENT-T07` (chemin, empreinte) au préenregistrement de la configuration. Le chemin du préenregistrement se résout contre le dossier courant : la commande doit partir de `RACINE`. `autoriser_depot_sale=True` en mode réel. Hérité de la v1. | Comparer la ligne au préenregistrement quand elle est présente ; écrire le dossier de lancement dans l'ordre d'exécution. |
| CT-16 | mineur, à porter au texte | `lecture_v2.py` l. 950-969 | Forme de `lecture-t07.json` : le placebo est sous `predictions["T7-P19"]`, non sous `jeux[sonde][jeu].placebo` ; le contrôle de disjonction est dans `sondes-t07.json`, non dans `ouverture-t07.json` ; une réduite inscrite pendant l'étape A va dans `notation-t07.json` (écart 2 du développeur). | Décrire ces formes au brouillon 20. |
| CT-17 | à porter au texte (ordre d'exécution) | `lecture_v2.py` l. 383-386 ; `journal_p3bis_v1.py` l. 67-68 | Les écrits de P3-bis sont lus sous `RACINE` (interprétation 7) et « journal absent = aucune ouverture ». Sur l'instance, un clone sans le journal à jour lit « aucune ouverture » sans alerte. | L'ordre d'exécution apporte `registres/` à jour depuis `main` à l'instant de l'ouverture et le dit ; le texte nomme la branche qui les porte. |
| CT-18 | mineur | `lectures_t07_v1.py` l. 165-168 | T7-P3 ou T7-P4 écrite « confirmée (non lues : …) » quand une seule des trois lectures a été faite. | « partiellement lue », lectures nommées. |

## Point 1 — conformité du texte au code

| exigence du brouillon 19 | texte | code | état |
|---|---|---|---|
| (x) `sondes_lues` sur les lignes de jeux antérieures à la première ouverture | l. 2443-2446, (a) 3 | `lecture_v2.py` l. 218-244, 438-444 | fait ; essais (x) et G5 |
| (xi) 24 couples figés, aucun de Mahalanobis | l. 2446-2448 | l. 283-303, 574-581, 836-853 | fait |
| (xii) fichier léger seul en mode réel, fichier complet refusé | l. 2448-2449 | l. 155-158, 188-194 | fait |
| (xiii), G6 `garde_adaptee`, `portee_regle_4` | l. 2449-2451, 1591-1592 | l. 102-112 | fait |
| G1 | l. 1541-1543 | `garde_adaptee_v1.py` l. 151-159 | fait ; appliquée sur tout chemin (interprétation 1) |
| G2 | l. 1556-1578 | l. 100-137, 162-192 ; `lecture_v2.py` l. 434-456 | fait ; le fichier d'issue n'est jamais analysé à l'étape A (son empreinte seule est calculée pour le sceau) |
| nœud de fin d'étape A | l. 1575-1578 | `garde_adaptee_v1.py` l. 195-209 ; `lecture_v2.py` l. 807-825 | fait ; CT-09, CT-10 |
| G3, verdict en prose avant `lire_issue_p3bis` | l. 1579-1594 | `garde_adaptee_v1.py` l. 231-271 ; `lecture_v2.py` l. 329-341, 458-467, 506-507 | fait |
| G4 | l. 1595-1603 | `garde_adaptee_v1.py` l. 218-228 ; `lecture_v2.py` l. 931, 948-949 | fait pour ce texte (G4 y coïncide avec G1) |
| G5 | l. 1604-1606 | `garde_adaptee_v1.py` l. 274-282 | fait |
| R14 | table, ligne R14 | `garde_adaptee_v1.py` l. 291-298 ; `lecture_v2.py` l. 929-931, 966 | fait ; CT-09 |
| (xv) journal au format b8, registre des préalables, fichier de décision | l. 2117-2141 | `journal_p3bis_v1.py` | fait ; CT-11 |
| 30 couples, empans, découpage | plan, points 2 et 3 | `sondes_neuves_v1.py` l. 146-268 | fait ; CT-04 |
| sonde principale, règle d'ex aequo écrite | plan, point 4 | l. 271-286 | fait ; essai d'ordre inversé du développeur |
| empreinte consignée avant toute notation | plan, point 4 | `lecture_v2.py` l. 696-704, 789, 802 | fait ; garde éprouvée (cas sain, artefact) |
| T7-P6 et témoin de même taille | plan, 6 bis | `sondes_neuves_v1.py` l. 293-321 | fait ; CT-05 |
| directions des concepts, témoins lexicaux | plan, point 10 | l. 345-384 | fait pour les concepts neufs ; tromperie et enjeux non faits (point 5) ; CT-01, CT-13 |
| notation de tout, fermée | plan, étape A, 3 | `lecture_v2.py` l. 522-624 | fait ; aucune aire à l'étape A |
| T7-P3, P4, P6, P9, P10, P15 à P19 | table des prédictions | `lectures_t07_v1.py` l. 172-373 | fait ; CT-03, CT-18 |
| placebo (200 permutations, échange par tâche, un seul déclencheur) | « Métrique » | l. 123-147 | fait ; interprétation 17 |
| base « coût seul » | « Métrique » | `lecture_v2.py` l. 619-622 ; `lectures_t07_v1.py` l. 302-337 | fait ; vérifié : la colonne `cout` vient de `t06.cout.cout_action` (`lanceur.py` l. 284, 400, sur `main`), et « lisible » y a la même définition |
| réserves R1 à R13 par identifiant | table des critères | `lectures_t07_v1.py` l. 376-429 | fait ; CT-03 |
| niveau de Bonferroni selon le nombre de sondes lues | « Seuil », repli | `plancher_v1.py` l. 24-29 ; `lecture_v2.py` l. 239, 868, 904 | fait ; mes essais : 0,975, 0,98333, 0,9875 sur cinq des huit cas |
| fermeture de (ii) sous L7b et L7c | l. 2221-2227 | `lecture_v1.py` l. 815-838 ; `lectures_t07_v1.py` l. 77-83 | fait ; tous les tableaux neufs sont filtrés à l'ouverture |
| Q11 | marqueur du code | `lecture_v1.py` l. 278-298 | lettre suivie ; voir ci-dessous |
| repli du recalcul | plan, point 8 | `repli_v1.py` | garde d'équivalence seule ; commande en refus |
| répétition jouet | l. 2419-2422 | `scripts/repetition_jouet_t07_v1.py` | faite par le développeur ; **en échec chez moi** (CT-01) |
| commande et codes 0, 2, 3 | l. 2459-2467 | `lecture_v2.py` l. 978-1029 | fait ; nom `lecture_v2` (écart 5) ; CT-06 |

**Q11.** Le constat du développeur est juste : la chaîne gelée n'écrit `lecture-cout-t06.json` que si elle atteint cette étape.
J'ajoute que la question ne se pose pas en pratique. L'étape A refuse dès que `arret.json` de T0.6 existe (`lecture_v2.py`
l. 430-431) ; sans étape A, ni `SCORES-T07` ni `SONDES-T07` ; l'étape B ne s'ouvre donc jamais sur un run arrêté, et L1 « par
`arret.json` » n'est jamais écrite. Une relance de T0.6 est un run neuf. À écrire au brouillon 20 ; rien à changer dans le code.

**Concordance avec T0.6 (texte scellé `ef31feff…`).** Le lecteur du fichier « mots et coût » tolère les clés en plus (`plis`,
`run_id`, `manifeste_sha256`, `taux_detection_1pc`), exige les champs par dose du point 3, `niveau` 0,95, 200 permutations,
seuil 0,70. La clé `CODE-MOTS-ET-COUT-T06` porte la marque `T06` : ignorée et comptée. Rien à signaler.

## Point 2 — les dix-neuf interprétations

| n° | avis | raison |
|---|---|---|
| 1 | acceptable ; à porter au texte | G1 sur tout chemin est plus sévère que la lettre (« ne s'appliquent que sur un lancement à ouverture réduite ») et rend `SCELLEMENT-T07` nécessaire à l'étape B, hors des neuf entrées de l'énumération (0). |
| 2 | acceptable | `pleine` à l'instant exact de la fin : compter « avant » est le sens prudent. |
| 3 | acceptable | une ligne de rendez-vous du même instant que la réduite n'a pas pu l'autoriser. |
| 4 | acceptable | cohérent avec « strictement antérieures » partout ailleurs. |
| 5 | acceptable | plus sévère ; à l'étape A, seules les réduites antérieures à l'ouverture sont contrôlées (CT-10). |
| 6 | acceptable | nécessaire : le fichier finit par un saut de ligne. |
| 7 | à porter au texte | voir CT-17 : sans règle sur la branche qui porte ces fichiers, « absent » passe pour « aucune ouverture ». |
| 8 | acceptable | lettre du texte, et de la consigne v3 (« ou l'ignore si elle lit l'action entière »). |
| 9 | acceptable, sous réserve | la frontière n'a tourné que sur le modèle jouet ; `frontieres_ajustees` est écrit ; à regarder au premier passage réel. |
| 10 | acceptable | la saturation est définie à 0,99 par le plan, point 4. |
| 11 | acceptable | ne joue qu'en jouet. |
| 12 | à porter au texte, et à la consigne des concepts | voir CT-13. |
| 13 | acceptable | sans tirage, ordre gelé. |
| 14 | acceptable ; à corriger à la marge | voir CT-14. |
| 15 | à corriger | voir CT-02 : écrire au moins les concepts dans le manifeste. |
| 16 | acceptable | vérifié dans le code de la chaîne sur `main`. |
| 17 | acceptable ; à porter au texte | le texte dit « à 95 % » pour T7-P19 ; préciser que la borne est recalculée à 95 % sous une graine propre. |
| 18 | conforme | c'est la lettre du plan, point 7. |
| 19 | acceptable ; à porter au texte | une différence appariée ne peut porter que sur les mêmes actions. |

## Point 3 — embargo et ordre des lectures

- **`lecture-sondes-t06.json`** : aucun chemin du module ne l'ouvre. Les lectures de `diag/<run>/` se font par nom fixe
  (`episodes-t06.json`, `lecture-cout-t06.json`, `arret.json`) ; `_lire_json` refuse ce nom ; aucun parcours de dossier dans
  les douze modules (recherche de `glob`, `iterdir`, `listdir`, `walk`, `scandir` : rien). Le script de répétition liste les
  noms de fichiers du run jouet sans en ouvrir aucun.
- **Fichier d'issue de P3-bis** : à l'étape A, seule son empreinte est calculée (sceau de la ligne) ; `lire_issue_p3bis` et
  `controler_verdict_prose` ne sont appelés qu'à l'étape B, le premier seulement quand la garde n'a aucun motif de refus.
- **Scores de T0.7** : ouverts seulement à l'étape B, garde passée, sous P « vu », table A lue et Q lisible ; les lignes de
  `S25` à `S100` sont retirées de tous les tableaux au chargement sous L7b et L7c.
- **`sondes_lues`** : ne peut pas s'élargir. L'instant de fermeture est le plus tôt entre la première ligne `OUVERTURE-T07` de
  l'étape A de ce run et la première ligne `OUVERTURE-P3BIS` ; une ligne de refus ne ferme rien ; l'étape B reprend la liste
  de `sondes-t07.json` et la compare à l'index des scores. Réserve : CT-02 (lien au manifeste trop lâche).
- **Ouverture réduite** : ne peut pas s'élargir. `pleine-anticipee` donne le nœud à toute date ; `pleine` avant la fin de
  l'étape A donne le nœud ; après une réduite, l'étape B exige une ligne `pleine` postérieure à la fin de l'étape A, à l'appui
  égal aux empreintes de `SCORES-T07` et `SONDES-T07`, et le verdict en prose présent. Réserves : CT-09, CT-10, CT-11, CT-17.
- **Course 7a** : le manifeste cité par `RUN-CONFIRMATION-T06` doit porter le GO attendu ; celui de 7a est refusé.

## Point 4 — gardes

- **R5.** Chaque garde neuve que j'ai lue a un cas sain et au moins un artefact dans `tests/test_t07_lecture_v2.py`,
  `test_t07_sondes_neuves_v1.py` et `test_t07_repli_v1.py`. Manquent : une action sans mot (CT-01), `familles` et `reglages`
  (CT-04), l'échec de T7-P6 (CT-05), `--instant` en mode réel (CT-06), les artefacts de `lire_phrases_concepts` (CT-13), la
  branche « frontière ajustée » de l'extracteur.
- **Repli silencieux** : un seul trouvé, CT-04.
- **R9** : `manifeste.graines` dérive par `SeedSequence(entropie, spawn_key=(clé,))` ; une clé reçoit la même graine qu'elle
  soit dans le manifeste ou dérivée après lui. Aucun autre tirage (recherche de `default_rng` et `random` : quatre appels, tous
  sous graine dérivée). Réserve : CT-14.
- **Moyenne et médiane sur les jetons** : aucune. Les agrégations sont « max » ou « attention » (`agregation_de`,
  `exiger_agregation` à chaque notation) ; la configuration refuse ces mots ; la seule médiane est celle des coûts de
  l'honnête dans T1 (définition de P3, sur des coûts, non sur des jetons).
- **Codes de sortie** : 0, 2 (`GardeArret` avant le manifeste), 3 (`ArretApresManifeste`). Toute autre exception sort en
  code 1 sans `arret.json` : le texte l'appelle « défaut de chaîne ».

## Point 5 — ce qui reste

- **T7-P10 pour la tromperie et les enjeux** : non bloquant pour le code, écrit « non lu » avec son motif. Le texte (plan,
  point 10) le demande encore : il faut soit l'entrée (textes et découpage de P3), soit l'écrire « non lue » au brouillon 20.
  C'est une lecture gelée retirée : décision à poser avant le scellement. À noter aussi : les paires de J-D ont la même
  réponse, donc le témoin lexical de la dissimulation, appris sur des textes identiques à étiquettes opposées, ne peut rien
  séparer ; T7-P10 n'y dit rien, à écrire.
- **Repli du recalcul** : non bloquant pour le scellement si le texte dit que le repli n'est pas mis en œuvre et que la perte
  du disque de l'instance avant l'étape A est un nœud. La commande refuse en code 2, sans rien écrire.
- **Mode réel jamais joué** : non bloquant pour le scellement du texte ; **bloquant pour la demande de GO de l'étape A**. Tout
  arrêt après le manifeste y est un nœud sans relance, et ni l'extracteur réel, ni la frontière « avant le champ » sur le vrai
  découpage en jetons, ni la durée et la mémoire n'ont été vus. Je propose une passe à blanc de l'extracteur sur les jeux
  génériques scellés (aucune action d'organisme, aucun manifeste, rien d'écrit), inscrite dans l'ordre d'exécution avant
  `etape-a`, et permise par le texte.

## Point 6 — valeurs proposées

- **`COMMIT_CODE_T07`** : `1f77b34dcb73c3cb1cef425f4f25646470255d32` existe, sur la seule branche locale `prep/t07-module-v2`
  (non poussée, pas un ancêtre de `main` ; la branche a avancé depuis, `a4fc13bc`). **Il ne peut pas être la valeur finale** :
  CT-01 demande un commit neuf.
- **`EMPREINTES_CODE_T07`** : recalculées au commit, **toutes égales** à la table du rapport complémentaire (douze modules,
  quatre fichiers d'essais, le script de répétition) ; les six modules de la v1 et `tests/test_t07_lecture_v1.py` égaux à
  `51a1874c`. Elles changeront avec les corrections.
- **`EMPREINTE_CONFIG_T07`** : le code permet de la remplir (`empreinte-config`), et refuse le brouillon tant que `entropie`
  est nulle. Empreinte canonique du brouillon recalculée : `9564d0ec…`, égale à celle du développeur ; fichier `8b2d8138…`,
  égal à son compagnon. Si CT-02 et CT-04 sont corrigés, les valeurs de `familles` et de `reglages` deviennent contraintes.

## Essais

Arbre détaché `/home/user/wt-t07-cl` au commit `1f77b34d`, retiré à la fin par la commande de la consigne. Disque avant :
6,9 Go libres. Extraction plus étroite que celle de la consigne : `src`, les quatre fichiers d'essais de T0.7 et `conftest.py`,
le script de répétition seul, les pièces des brouillons 14, 17 et 19, le brouillon 14, le fichier léger de P3 et son compagnon.
Ni `scripts/` ni `donnees/` en entier, pour n'extraire aucun chemin interdit.

| run | heures (UTC) | résultat |
|---|---|---|
| les quatre fichiers d'essais de T0.7 | 06:38:38 à 06:49:48 | **223 passés, 1 sauté**, 668 s (le saut : essai d'égalité de la v1, branche absente, déclaré) |
| mes essais de constat, premier passage | 06:50:04 à 06:50:28 | 10 passés, 1 échoué : une assertion mal écrite par moi (elle prenait la clé de configuration `sondes_par_concept` pour un nom de concept lu) ; le constat lui-même était affiché |
| mes essais de constat, assertion corrigée | 06:50:36 à 06:53:07 | **11 passés**, 150 s : jeux écrits sous la consigne v3 acceptés par `lire_jeu` (deux fichiers d'assemblage d'essai) ; CT-02, CT-03, CT-04, CT-05, CT-06, CT-09 (deux cas), CT-10, CT-11 |
| répétition jouet, une fois | 06:53:15 à 06:54:14 | T0.6 jouet code 0 (29,6 s) ; **étape A code 3** (26,6 s), « texte d'action vide ou non textuel » ; étape B non jouée (CT-01) |
| replis des jeux à l'étape complète, étapes A puis B | 06:55:21 à 06:56:10 | **5 passés**, 48 s : deux, trois ou quatre sondes, niveau appliqué, prédictions « non lues » attendues |

Un essai de constat qui passe confirme le défaut nommé : ce ne sont pas des essais de non-régression. Mes deux fichiers
d'essais ne sont pas versés (empreintes `a5db0e61…` et `f6409e7e…`, copies dans mon bloc-notes de session).

## Interdits : tenus, et trois écarts de forme que je déclare

- Aucun `lecture-sondes-t06.json` ouvert, celui de mon run jouet compris (son nom seul figure dans la liste du script). Aucune
  donnée de 7a, aucune lecture B, aucun étiqueteur. Aucune valeur de clé. Aucun appel externe, aucune dépense. Rien écrit dans
  `/home/user/wt-t07` ni committé sur `main`. Aucun refus de permission ni de classifieur rencontré.
- **Écart 1** : pour mesurer la taille de l'extraction, j'ai listé par `git ls-tree` le dossier `donnees/` du commit
  `1f77b34d` (59 fichiers, les 50 premiers noms affichés) et la racine du commit. Aucun nom interdit n'est apparu dans ce qui
  s'est affiché ; je n'ai rien ouvert.
- **Écart 2** : deux recherches de texte par `grep -r` (« position_cost », puis « phrase_neutre ») ont parcouru `scripts/`,
  donc le fichier `extraire_mesures_epreuve_t06_v1.py` ; la seconde a parcouru `docs/` sans exclure `docs/notes/bras-attaque/`.
  Seuls des noms de fichiers ont été affichés, aucun de ces chemins ; je n'en ai lu aucun contenu.
- **Écart 3** : un motif de fichiers `docs/notes/*/consigne*jeux*v3*` a été développé par l'interpréteur de commandes sur tous
  les sous-dossiers de `docs/notes/`, sans sortie.
