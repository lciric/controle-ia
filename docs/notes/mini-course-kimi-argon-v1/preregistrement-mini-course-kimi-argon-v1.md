# Préenregistrement — mini-course d'idéation réelle, Kimi et Argon seuls, nuit du 1er au 2 novembre 2026, v1

- Auteur : sous-agent de session-depot (rédacteur des pièces neuves et de ce texte), à la demande de session-depot ; exécution
  par session-depot. Aucun appel payant, aucun appel réseau vers un modèle, rien de scellé ni de commis par le rédacteur.
- Date (UTC) : 2026-11-01, écrit à partir du relevé `date -u` de 21:04.
- Commit du dépôt au moment de la rédaction : `e5ccf955` ; `donnees/` est ignoré par git sur `main` : les empreintes de la
  section « Pièces gelées » font foi ; le commit au lancement est relu par l'orchestrateur (manifeste R9) et porté au registre.
- Documents qui font foi (chemin + empreinte) :
  - devis : `docs/notes/devis-mini-course-kimi-argon-nuit-v1/devis-mini-course-kimi-argon-nuit-v1.md`,
    `18e8495f4e29f4d00fb466293cdbfdfeb633e2c9b5ccef4ac4910dcb2f649f37` — **scénario B** et adaptations 1 à 6 ;
  - ligne de GO : `registres/go.md`, **GO-2026-11-01-12** (type « calcul », plafond « 10 USD », échéance 2026-11-02, accordé par
    Lazar ; périmètre : scénario B, démonstration non décisive, préenregistrement scellé et contre-lu avant lancement, trace
    publique agrégée seulement, dossier du run sous `donnees/`) ;
  - orchestrateur v56 : copie identique, fichier pour fichier, à l'archive `CODE-orchestrateur-pole-v7-v56.zip`
    (`29b1b38cfee5e279a06c947fdf1f855628b574e81e44c2d7e48a029151c1b24c`, celle de l'épreuve du pont), listée dans
    `EMPREINTES-orchestrateur-v56-copie-v1.txt` (pièce gelée) ;
  - règles R1 à R14 de `CLAUDE.md`.

## Nature et hypothèse

**Démonstration non décisive, sans signe visé (R3).** Aucun chiffre de cette course ne va vers un papier, une porte ou une
décision scientifique. Aucune hypothèse du programme (H1 à H9) n'est testée.

Question, purement descriptive : **la chaîne de l'orchestrateur v56 tourne-t-elle de bout en bout, pour une génération, avec
Kimi (`kimi-k3.1-pro`) et Argon (`gemini-4-argon`) seuls, sous le plafond de 10 USD, sans qu'aucune fiche ni consigne ne sorte
du dossier privé du run ?** On rapporte comment elle tourne (comptes par étape, juges, accord), jamais si les idées sont bonnes.

Montage (scénario B du devis) :
- **une génération**, une case (`statistiques-qui-transferent`, `niveau-methode`) ;
- **deux proposeurs**, six fiches chacun (Kimi, Argon), consigne figée commune (statistiques de détection qui transfèrent,
  niveau méthode : reprise de la piste A de `docs/notes/ideation-organisme-v1/course-2/question-course-2-v1.md`, glossaire et
  repères chiffrés tels qu'ils y sont cités) ;
- **aiguilleur** Argon sur chaque fiche (passeport « niveau méthode » seul vers les juges, A17) ;
- **deux juges** (Kimi, Argon) sur chaque fiche munie d'un passeport, items K1 à K5, verdict « notable » = cinq items vrais ;
  agrégation **unanimité** ;
- **bisociateur, bras « basique » seul**, une paire (`k_paires` = 1) : deux lecteurs d'étiquettes (Kimi, Argon) sur une liste
  fermée de 24 concepts, puis **une fusion** écrite par Argon, aiguillée et jugée par les deux juges ;
- **sans passe « tableau »** (adaptation 4 : aucun appel, rien d'écrit ; l'étape reste au plan avec un attendu et un plafond
  nuls) ;
- **deux contrôles** (un par fournisseur, « Réponds seulement par le mot OK », modèle servi exact exigé) avant la course.

## Prédiction chiffrée et signe attendu

**Aucune prédiction de signe** sur les verdicts, l'accord des juges ou l'écart entre familles (R3) : ils sont rapportés, pas
attendus. Attentes de fonctionnement seulement (devis, scénario B), dont l'écart sera rapporté comme tel :

| Rôle | Fournisseur | Appels attendus |
|---|---|---|
| proposeur | Kimi, Argon | 1 + 1 |
| aiguilleur (12 fiches + 1 fusion) | Argon | 13 |
| juges (12 + 1, chacun) | Kimi, Argon | 13 + 13 |
| lecteurs d'étiquettes (12 chacun) | Kimi, Argon | 12 + 12 |
| metteur en fusion | Argon | 1 |
| contrôles | Kimi, Argon | 1 + 1 |
| **total** | Kimi 27, Argon 41 | **68** |

Dépense estimée au devis ≈ 6,4 USD (pire cas × 1,5 ≈ 9,6) ; **garantie : 10 USD au plus**, par la garde cumulée (plus bas).
La répétition simulée (moteur simulé du lanceur, puis moteur réel devant des amonts factices) a rendu exactement ces 66 appels
de course et 2 contrôles.

## Métrique

Toutes calculées par le seul agrégateur `trace_agregee_mini_course_v1.py` (pièce gelée), après la course, sur le dossier du run :

- **L1** — `l1.fin` ∈ {`generation_terminee`, `noeud`, `arret_motif_code`, `non_lance`} ; `l1.motif_arret` (classe codée :
  `modele_servi_different`, `trois_echecs_consecutifs`, `debordement_garde_kimi`, `signal_recu`, `plafond_cumule`,
  `plafond_etape_faux`, `porte_de_plafond`, `noeud_c13`, `autre_exception`, `aucun`) ; statut de chaque étape (`jouee`,
  `retiree`, `non_mesuree_budget`, `non_mesuree_technique`, `hors_scenario_b` pour la passe « tableau »…) ; C13.
- **L2** — comptes : fiches proposées par fournisseur (fiches lues ; fiches refusées pour leur forme et propositions sans sortie
  exploitable comptées à part, par proposeur) ; classes de l'aiguilleur (`niveau_methode`, `a_corriger`, `concret`, refus
  comptés à part) ; passeports ; exclusions A4 ; fusions écrites, complètes, inachevées ; verdicts présents et absents par
  juge ; fiches étiquetées par lecteur, lectures rejetées, Jaccard moyen des deux lecteurs (S24) ; rôles arrêtés.
- **L3** — par juge : nombre de verdicts lisibles, nombre et part de « notables » ; selon la règle d'agrégation (unanimité) :
  nombre et part de fiches notables ; accord des deux juges sur « notable » : accord brut et kappa de Cohen sur les fiches
  jugées par les deux.
- **L4** — sur tous les couples (fiche, juge) lisibles : part de « notables » et X moyen (part des items vrais) quand le juge est
  **de la famille de l'auteur** (Kimi juge une fiche de Kimi ; Argon juge une fiche d'Argon ou la fusion d'Argon), et quand il
  est **de l'autre famille** ; écarts (même famille moins autre famille).
- Coûts (par fournisseur, rôle, étape ; registre cumulé, contrôles compris), appels par rôle, durées par rôle.

Effectifs : 13 fiches au plus ; **aucun intervalle n'est opposable** ; tout nombre de L3 et L4 est descriptif.

## Seuil

Aucun seuil de décision scientifique. Seuils **de fonctionnement**, fixés dans la configuration gelée :
- S17 (plafond de la course, noyau) = 10 USD, portée « course », arrêt d'étape 9 USD ; garde cumulée (commandes) = 10 USD ;
- plafonds de session : proposeur 1,80 ; aiguilleur, juge, lecteur 0,25 ; fusion 0,40 USD ;
- S12 (débordement de Kimi proposeur) = 0,5 ; A3 = 3 échecs consécutifs ; A14 = 0,25 ; délais A3 : 900 s (Kimi 1 800 s) ;
- anti-fuite : **tolérance nulle** (un canari, un titre ou une suite de six mots d'une fiche dans la trace : trace refusée).

## Plan d'analyse

- **Pièces** : configuration `configuration-mini-course-kimi-argon-v1.json` et ses six pièces empreintées (consignes du
  proposeur, de l'aiguilleur, du juge, du lecteur, du metteur ; liste des concepts) ; lanceurs ; commandes ; agrégateur
  (section « Pièces gelées »).
- **Graines (R9)** : racine `20261102`, préfixe `mc1` ; `numpy.random.SeedSequence(racine, spawn_key=(clé de tâche,))`
  (`pole/graines_v53.py`) pour les identifiants opaques, l'anonymisation des juges, l'ordre des bras et des fusions et le
  départage des paires ; manifeste R9 écrit par l'orchestrateur (`manifeste-depart.json`).
- **Plan de dépense (règle d'A1 du brouillon 10, `budget_v56`)** : proposition (attendu 0,94 ; plafond de relais 2,50 ;
  protégée) ; aiguillage (1,20 ; 2,60 ; protégée) ; juges (1,87 ; 3,00 ; protégée) ; passe « tableau » (0 ; 0 ; sacrifiable,
  rang 2, hors scénario) ; étiquettes (1,87 ; 3,00 ; protégée) ; fusions (0,47 ; 1,10 ; sacrifiable, rang 1).
- **Modèles** : identifiants exacts ; modèle servi exigé égal au modèle demandé (relais Kimi : barrière R-764 ; commande Argon :
  égalité exacte ; adaptateur v56 : recopie et contrôle) ; aucun changement de modèle.
- **Ordre** : vérifications sans écriture (empreintes, préenregistrement et contre-lecture scellés, configuration, gardes R5
  rejouées à É0, ligne de GO à 10 USD exactement) ; relais ; contrôles ; course ; arrêt des relais ; agrégateur ; recherche des
  clés dans le dossier du run.
- **Lecture** : seul l'agrégateur lit le dossier pour la trace publique. Les fiches restent dans le dossier du run (`donnees/`,
  exclu de la copie publique par `scripts/depot_expurge.py:51`), lisibles par Lazar seul ; aucune fiche, aucun titre, aucun
  extrait n'est cité dans un registre, une passation ou un message.
- **Lecteur de la trace** : session-depot rapporte L1 à L4 tels que la trace les donne, en une ligne chacun, avec les réserves.

## Critères de lecture gelés

| Critère | Issue | Lecture |
|---|---|---|
| L1 | `generation_terminee`, étapes protégées `jouee`, fusions `jouee` | démonstration **aboutie** |
| L1 | `generation_terminee`, fusions `retiree` | démonstration **aboutie sans fusion** (sacrifice d'A1, consigné) |
| L1 | `noeud` (C13) | démonstration **partielle** : étape nommée « non mesurée » ; rien de ce qui a été mesuré n'est ouvert (O12) |
| L1 | `arret_motif_code` | démonstration **arrêtée**, motif codé rapporté ; aucune relance sans nouveau GO |
| L1 | `non_lance` | aucun appel de course ; cause rapportée (journal du lanceur) |
| L2 | tous comptes | rapportés tels quels ; un écart au tableau des appels attendus est rapporté et expliqué |
| L3 | parts et accord | **descriptifs** (n ≤ 13, aucun intervalle opposable) ; jamais un classement des proposeurs ni des juges |
| L4 | écarts | **rapportés comme réserve** : deux familles seulement, chaque fiche a un juge de sa propre famille (devis, réserves) ; jamais une mesure de complaisance |

**Symétrie (R4)** : déclenchent le même audit avant toute ligne de lecture, dans un sens comme dans l'autre : les deux juges
unanimes sur toutes les fiches (toutes notables, ou aucune) ; kappa égal à 1 ou au plus −0,5 ; zéro appel inexploitable avec des
sorties identiques d'un appel à l'autre ; toutes les fiches `concret` ou toutes `niveau_methode` dès la première passe ; dépense
inférieure à 1 USD ou supérieure à 9 USD. L'audit vérifie les journaux des relais (modèles servis, usages), le registre cumulé et
l'absence de réponse factice ; son résultat est une réserve écrite, jamais une correction des nombres.

## Liste d'arrêt

| Motif | Où il est codé | Effet |
|---|---|---|
| plafond de l'étape atteint | noyau v56 (`OrchestreV56.appel`, coupure) ; commandes (garde d'étape du registre) | étape protégée « non mesurée (budget) », nœud C13, course arrêtée ; fusions retirées (sacrifiables) |
| plafond cumulé (10 USD) | registre cumulé des commandes ; plafond de chaque relais ; `CumulAuDelaDeS17` du noyau | appel refusé sans envoi (code 4) ; cumul au-delà de S17 : arrêt |
| modèle servi différent | relais Kimi (502) → commande Kimi ; commande Argon ; `AdaptateurCommandeExterneNuitV1` | `ArretModeleServiDifferent` : arrêt de la course |
| trois échecs consécutifs d'un rôle | `GenerationNuitV1.appel` (A3) | `ArretTroisEchecs` : arrêt de la course |
| débordement de la garde Kimi (S12) | `GenerationNuitV1._aiguiller` (M5) | `ArretDebordementKimi` : arrêt de la course |
| part d'appels inexploitables (A14) | noyau v56 | étape « non mesurée (technique) », nœud |
| signal reçu (SIGTERM, SIGINT) | `ArretSurSignal` ; trap du lanceur | arrêt propre, manifestes écrits, relais arrêtés par PID |
| contrôle en échec | `lancer-mini-course-v1.sh` | aucune course (code 3) |
| canari dans la trace | agrégateur | trace refusée, rien d'écrit (code 3 de l'agrégateur, 7 du lanceur) |
| clé trouvée dans une sortie | `lancer-mini-course-v1.sh` | alerte, code 6 |
| coût lu au-dessus du pire cas réservé | commandes (`depassement_reserve`) | appel rendu non conforme (code 5), compté au registre |
| toute autre exception | partout | arrêt, sans repli ; motif au manifeste de fin |

Chaque garde a été éprouvée sur un cas sain et sur un artefact pendant la répétition (R5 ; liste au LISEZMOI).

## Canaris

- **Une chaîne unique dans chaque consigne figée** (tirée par `SeedSequence(20261102, spawn_key=(clé,))`) : proposeur
  `MC1-PROPOSEUR-c518922b`, aiguilleur `MC1-AIGUILLEUR-b7f5a763`, juge `MC1-JUGE-9e367345`, lecteur `MC1-LECTEUR-30741b8c`,
  metteur `MC1-METTEUR-4ec962f1` (clé `canaris` de la configuration) ; elles doivent être **absentes de la trace**.
- **Une fiche factice** (`MC1-FICHE-FACTICE-67b8c480` dans l'hypothèse de la première fiche de chaque proposeur) a été passée en
  mode simulé et devant les amonts factices : la trace l'a exclue, et l'agrégateur l'a vue quand on l'injectait.
- **Chaque garde testée sur un cas sain et sur un artefact** (R5) : l'agrégateur rejoue sa propre garde à chaque exécution
  (`tester_garde`) ; `--artefacts-sur-run` injecte, dans une copie de la trace d'un run, un canari, un titre, six mots d'une fiche
  et un texte hors liste blanche (chacun doit être vu).

## Trace agrégée

- Écrite par le seul agrégateur, dans le dossier du run : `trace-agregee-mini-course-v1.json`, compagnon `.sha256` (R6).
- **Liste blanche de clés et de valeurs** : comptes, statuts, coûts, appels, durées ; verdicts sous identifiant opaque (`v01`…)
  avec la famille de l'auteur, l'origine (proposition ou fusion), et par juge sa famille, « même famille », notable, X ; aucun
  texte libre (un nom d'exception, lettres seules, est la seule chaîne non énumérée).
- **Contrôle par programme** : refus si la trace contient un canari, un titre de fiche ou une suite de six mots tirée d'une fiche
  (fiches du lot et fusions archivées).
- La trace n'est copiée vers `docs/notes/mini-course-kimi-argon-v1/` qu'après ce contrôle, par session-depot, sous un nom neuf.

### Pièces gelées

| Pièce (chemin depuis la racine du dépôt) | SHA-256 | Rôle |
|---|---|---|
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/configuration-mini-course-kimi-argon-v1.json` | `f8e53f0215def111753f31507a631ee36e8ddc37d5fe90b925448b3166ae0e1d` | configuration figée (scénario B) |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/pieces/consigne-proposeur-mini-course-v1.md` | `98185e70f5d4bd3f0574b7517858efbec982d6decea0e5493da6abe12e9607b1` | consigne figée du proposeur |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/pieces/consigne-aiguilleur-mini-course-v1.md` | `4b15b31add9fe8e3ae5a18a309fdc9a7165da3be0533c5240dd9854ba08e14e9` | consigne figée de l'aiguilleur |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/pieces/consigne-juge-mini-course-v1.md` | `df57bc9117e85b6a032355159a84451c4fe60a5c44793c5986ac6b1a89c45bd9` | consigne figée des juges |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/pieces/consigne-lecteur-mini-course-v1.md` | `016789aeb9fc4177d865634882e1e5bc18053d0a16b72ccc83c7abbc6fbcb636` | consigne figée des lecteurs d'étiquettes |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/pieces/consigne-metteur-mini-course-v1.md` | `95b92e325ca95ded574073db8d13dcc8886c475d30dd01317c31fc40b96609e4` | consigne figée du metteur en fusion |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/pieces/concepts-mini-course-v1.json` | `036de84a297f5c3e402caeb9069e4d8eb9d0d3ec4ef86a5fc6a039022c8b3874` | liste fermée des concepts (bras basique) |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/pole/course2_nuit_v1.py` | `b0506f7eb8ed384d0284b6b3335d93f31fb67c040fa53a932043ab44f1d33286` | génération sans passe tableau, liste d'arrêt |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/lancer_mini_course_v1.py` | `9a108a74d2b65cc5e5a99eb2bd4fcc62cbc0c146e58e4b4ff31a76c99aa78229` | lanceur Python (gardes, moteur réel) |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/lancer-mini-course-v1.sh` | `d7297197879075b849951e6d57f898c3d74a5dc1ab1732ac056f010259a1780f` | lanceur shell (relais, contrôles, clés) |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/commande_kimi_v2.py` | `644dbb39003f234db7b5fc295c6b061a0e84720e01ba08322ae1fe7936d9dcbe` | commande externe de Kimi |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/commande_argon_v56_nuit_v1.py` | `d0e37c28ab91da045350cc5f84e9b5711c56de76ee6b2f7928003c5a2c998487` | commande externe et relais d'Argon |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/registre_depense_cumulee_v1.py` | `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | garde cumulée au pire cas |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/trace_agregee_mini_course_v1.py` | `ccf9f67c7c3f10847b578c1acbd17b0c114da769aef444e5f7821769ec17fbab` | agrégateur de la trace publique |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/EMPREINTES-orchestrateur-v56-copie-v1.txt` | `3c72e4aae6abfdf177776d9fcb177569e3bc156daa7edaf796f33db286c8565b` | copie de l'orchestrateur v56 (archive 29b1b38c…) |
| `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py` | `d54ed2bce54f5c89e9f078d1a03b5d8159894d6565ae560c3601c1e63ca76239` | relais Kimi local |
| `donnees/espece-seule-v1/collisionneur_v7.py` | `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc` | appeler_gemini (Argon) |

## Réserves

- **Deux familles seulement** : le juge d'une autre lignée n'est pas imposé par le code ; chaque fiche a un juge de sa propre
  famille ; L4 n'est qu'une réserve.
- **Prix d'Argon SUPPOSÉ** (10 et 50 USD par million, prudent) ; durées des appels courts supposées ; coupure possible de Kimi
  après envoi (comptée au pire cas).
- **Contrôles hors S17** : leurs ≈ 0,01 USD sont dans le registre cumulé (10 USD), pas dans le plafond du noyau ; le registre est
  la borne qui lie.
- **Plafonds souples** des étapes protégées (règle d'A1 du brouillon 10) : le noyau laisse une étape protégée aller jusqu'à
  S17 − cumul − attendus restants ; le registre cumulé et les plafonds de session bornent chaque appel.
- **A14 sur un seul appel** : une proposition inexploitable (part 1,0 > 0,25) rend l'étape « non mesurée (technique) » et arrête la
  course (nœud) ; c'est voulu, et c'est la principale cause d'arrêt prévisible.
- **Paramètres du bras « basique »** (exposant 8,5 ; décalage 0,05) : valeurs d'essai du code v56, sans étalonnage (démonstration).
- **Étiquettes interdites** (A4, mode préfixe, fiche exclue) : une fiche qui écrit « fusion », un nom de fournisseur… est exclue
  et comptée ; l'exclusion peut toucher une fiche légitime.
- La clé d'Argon passe par un relais local (`commande_argon_v56_nuit_v1.py servir`) : le noyau v56 interdit tout nom de clé dans
  son environnement ; limite connue de `/proc/<pid>/environ`, conteneur à un seul utilisateur.

## Contre-lecture

Sous-agent neuf, qui n'a écrit ni ce texte ni les pièces ; fichiers à lui donner explicitement : ce préenregistrement, le devis,
`registres/go.md` (ligne GO-2026-11-01-12), la configuration, les cinq consignes, `pole/course2_nuit_v1.py`,
`nuit/lancer_mini_course_v1.py`, `nuit/lancer-mini-course-v1.sh`, les deux commandes, le registre cumulé, l'agrégateur, les
essais des gardes (`nuit/repetition/test_gardes_mini_course_v1.py`) et le LISEZMOI
(`donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/LISEZMOI-mini-course-kimi-argon-v1.md`). Rapport : `docs/notes/mini-course-kimi-argon-v1/contre-lecture-preregistrement-mini-course-kimi-argon-v1.md`, scellé.

Empreinte du rapport de contre-lecture : À FOURNIR AU SCELLEMENT

Traitement de chaque remarque : à écrire ici avant le scellement (acceptée, refusée et pourquoi) ; une pièce modifiée change de
nom (R12) et sa ligne de la table ci-dessus.
