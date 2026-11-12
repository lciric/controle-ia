# Journal de l'inventaire de l'organisme d'idéation — v7 (jalons 1 à 7, version finale de la tâche)

- Version v7, écrite le 10 novembre 2026 à 12:38 UTC (`date -u`) ; accompagne `inventaire-idees-organisme-v7.md` ; reprend la v6 (`8d3147a6…`, dont l'heure de fin de lecture du jalon 6 est corrigée ici) et ajoute le jalon 7 et la liste des trous connus.

## Jalon 01 — rapports au directeur

Heures relevées par `date -u` : début de la tâche 11:59 UTC ; lecture de ce jalon de 12:00 à 12:05 UTC environ.

### Sources lues, avec empreintes (recalculées par `sha256sum`, égales à leur compagnon `.sha256`)

| source | sha256 | lecture |
|---|---|---|
| `docs/notes/rapports-directeur/rapport-principes-etat-goulots-entretien-organisme-2026-11-09-v1.md` | `22263fced8d43771f0a34b3cdd9b0e6b318e39d23189907a3e9736e74413b984` | entier (189 lignes) |
| `docs/notes/rapports-directeur/resultats-pour-documents-v3/section-resultats-organisme-v3.html` | `d6d702f5383347f16c894065ce45d96745a20f6016243d5f3b956828b3a3d9fd` | entier, texte extrait des balises |
| `docs/notes/rapports-directeur/resultats-pour-documents-v3/registre-affirmations-v3.md` | `38c24c925e151dc50f8b5b59eee9d8ff04c9b08e2cc4f52a9d9206553905780e` | entier ; les rangées B1 à B53 servent de renvoi vers les pièces primaires |
| `docs/notes/rapports-directeur/premisses-trace-interne-v1.md` | `2638558e34c15800acf7c8d8653dd978eba0660a9341795069d7ddd3b58e712f` | recherche ciblée (organisme, idéation, collisionneur, juge statistique, Goodhart, nul v, proposeur, Avalon, Lean, objectif ultime, papier C) : « organisme » n'y désigne que les organismes-modèles de T0.6 ; aucune entrée |

Pièces primaires citées par le registre des affirmations et dont l'empreinte a été recalculée par le rédacteur (égales au registre) : A13, A4V, A4T, V9, EPT, EPL, EAB, N064, N065, NPOP, NCOS, PUB ; sur branches, par `git show origin/<branche>:<chemin> | sha256sum` : C4R, C7R, V65R. Leurs lignes sont citées d'après le registre à ce jalon ; elles sont relues aux jalons suivants quand la pièce entre dans une famille de sources lue.

### Sources non lues à ce jalon, et pourquoi

- `docs/notes/rapports-directeur/programme-depuis-zero-2026-11-10-v1*`, `…-v2*`, `programme-depuis-zero-v2-*`, `depuis-zero-comparaison-v1/`, `exemple-chiffre-depuis-zero-v*.py` : hors de la liste de la consigne pour ce dossier, et proches par le nom des documents cloisonnés (« programme depuis zéro v5 », « organisme depuis zéro v4 ») ; non ouverts par prudence de cloison.
- `docs/notes/rapports-directeur/dossier-entretien-27-novembre-v1/` : contient `pieces-bras-v1/` (cloison du bras) ; non listé, non ouvert.
- `rapport-programme-complet-entretien-2026-11-10-v1/v2/v3` (.html, .pdf), `ce-qui-manque-approche-peut-marcher-v1.md`, `premisses-trace-interne-v1-point-2a.md`, `premisses-trace-interne-v1-journal.md`, `resultats-pour-documents-v1/`, `-v2/`, `section-resultats-programme-v3.html` : hors liste de la consigne ; non lus à ce jalon (portent sur le programme principal ; à reprendre seulement si un renvoi vers l'organisme l'exige).
- `docs/notes/taif-v1/integration-v1/journal-changements-candidature-v1-brouillon4.md` (cité par RPG : l'organisme absent de la candidature) : non lu ; l'entrée cite RPG.

### Doublons fusionnés

- L'intégration de l'organisme au papier C apparaît dans RPG (§ 1, § 6) et dans SRO (B4) : entrées PAC-001 (le juge est un moniteur) et PAC-002 (rôle 1), chacune avec les deux sources.
- Les citations obligatoires apparaissent dans RPG (§ 5, § 6) et SRO (§ 7) : une seule entrée (OUT-002).

## Jalon 02 — décisions et propositions (`docs/decisions/`)

Lecture de 12:08 à 12:15 UTC environ (`date -u`). Chaque fichier lu a été vérifié contre son compagnon `.sha256` (tous « OK »).

### Sources lues en entier

| clé | fichier | sha256 |
|---|---|---|
| N044 | `decision-N-044-v1.md` | `2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf` |
| N045A | `decision-N-045-v1.md` (lue par différence avec la v2) | `42be51f6e56c1971a0c1184d3c104bbf51052d428c5ae211c58f6ebafad33300` |
| N045 | `decision-N-045-v2.md` | `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d` |
| N047 | `decision-N-047-v1.md` (différence avec N-053 : numéro seul) | `20941ec350762a140dba753ffa535f68dc7217cf91df5c20c8e8eef9a0d95267` |
| N049 | `decision-N-049-v1.md` | `8a5bf5e57e2bb447467388acb572e032d1a6a578a868db1b7304263a1c9d4460` |
| N050 | `decision-N-050-v1.md` (même note que N-049) | `a54b128df955dba34bb360fa2fea466c787026a934f25135d698e8cd925d5f58` |
| N052 | `decision-N-052-v1.md` | `817d218b22b8d1d4a2c03bb78fb4870867f19bd1a1f9c08b0a1873efbb31a384` |
| N053 | `decision-N-053-v1.md` | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` |
| N057 | `decision-N-057-v1.md` | `42180088efb2e1016251fa329421fc08ebcb13039266d278c1a6f37ced60af99` |
| N058 | `decision-N-058-v1.md` | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` |
| N059 | `decision-N-059-v1.md` | `41aff854c38bed3a43aced62bd0c1b3af782c5a5f6174f335a175847b407e687` |
| N060 | `decision-N-060-v3.md` | `2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591` |
| N060B | `decision-N-060-v2.md` (lue par recherche ciblée des oracles) | `06a7cb237bde15f18721b908274c2e7655d92c4df2d8905d6334d32de18d0270` |
| N064 | `decision-N-064-v1.md` | `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97` |
| N065 | `decision-N-065-v1.md` | `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4` |
| N066 | `decision-N-066-v1.md` (ne touche pas l'organisme ; aucune entrée) | `21e83ed58c7498c65b7f9ae78613bc38301acdf0dd15a9890af13e6c0edbd351` |
| SPK | `decision-sparks-D3-D4-D5-v1.md` | `6b5f3f2dd6b15b1d40f4b0a3a302e08c56bed61d251ca4c0632da4abb610a6e9` |
| P036A | `proposition-P-036-couche-2-preparation-v1.md` | `a8c41681f1c9ee539a0abfd4b8bf0367e1a2e0ba4a7dd30e27db1c87f867e97c` |
| P036B | `proposition-P-036-couche-2-preparation-v2.md` | `155f0511991d420c257c563b98c70fdaa0994b0134d312d365ccada071b39c25` |
| P041A | `proposition-P-041-organisme-coevolutif-attaque-defense-v1.md` | `254b178270f11123c4bf0c24ead0855c982550730c54bcba0924a39c6d04ca9b` |
| P041B | `proposition-P-041-organisme-coevolutif-attaque-defense-v2.md` (lue par différence avec la v3 : rien qui n'y soit) | `2df36f8793668fcb7e2dfba9cdbca0cce77a992063c99f6e1932849b6948f01b` |
| P041 | `proposition-P-041-organisme-coevolutif-attaque-defense-v3.md` | `72aec5322c61490df41ed0d4b60f5ee24e5ce54e2b62896790a0df6e374b7725` |

Lues pour leurs seules lignes sur le pôle ou l'organisme (recherche ciblée : organisme d', idéation, pôle, collisionneur, orchestrateur, objectif ultime, proposeur) : N055 (`371879d5…`, l. 15-30) et N056 (`3592c1e9…`, l. 48-70 ; le point 6, « monter le bras d'attaque », n'est cité que pour son existence).

### Sources non lues, et pourquoi

- `decision-N-054-v1.md` : non ouverte ; elle fixe le mode tenu à l'écart, dont la consigne interdit tout au-delà de l'existence.
- `decision-N-061-v1.md`, `decision-N-062-v1.md`, `decision-N-063-v1.md`, `-v2.md`, `decision-N-003` à `N-035`, `decision-P-008`, `decision-P-014`, `note-alignement-N-055-D-S8-v1.md`, `proposition-N-010` à `N-025`, `proposition-P-006` à `P-015`, `proposition-P-040` : recherche ciblée sans occurrence de l'organisme d'idéation ou du pôle (sauf P-009 et N-025, où « organisme » désigne les organismes-modèles de T0.6) ; programme principal, hors objet.
- `proposition-P-066-saboteur-diffus-par-construction-v1.md` : saboteur diffus de T0.6 (programme principal) ; « organisme » y désigne un organisme-modèle ; aucune entrée.
- Pièces citées par ces décisions et non lues ici (à reprendre si une famille de sources les couvre) : `docs/notes/affinage-equipe-rouge-v2/` (conception de l'affinage, contre-lectures), `docs/notes/anteriorite-P-041-v1/` (note d'antériorité v2, synthèses du collisionneur sur P-041), `docs/notes/couche-2-preparation-v1/` (synthèse du collisionneur « cinq divergences », rapprochement des trois voix), les notes de conv-audit sur `canal/conv-audit-n04`.

### Erreurs de renvoi trouvées dans une source

- Le registre des affirmations v3 (RAF) cite N-064 aux lignes 15-17 et N-065 aux lignes 14-17 ; sur le fichier, l'énoncé retenu de O2 est à la ligne 13, O11 et O12 à la ligne 14, les citations obligatoires à la ligne 15, et le rôle 1 de N-065 aux lignes 15-18 (décalage de deux lignes). Les entrées du jalon 1 qui citaient ces lignes ont été corrigées dans les données (v2 de l'inventaire) ; la v1 scellée garde l'ancien renvoi.

### Doublons fusionnés

- N-049 et N-050 sont une seule note de conv-audit transcrite deux fois : les entrées citent N049 pour le vivier et la banque sœur, N050 pour `test_final`.
- N-047 et N-053 : même contenu ; seul N053 est cité.
- L'invariant « aucun score de moniteur » (OUT-001) réunit RPG, N-053 et N-065.
- La question du directeur sur l'organisme coévolutif (ATQ-001, jalon 1) et sa reformulation de P-041 sont gardées séparées : la première est la demande, les suivantes sont les idées qui en sortent.

## Jalon 03 — registre des décisions (`registres/decisions.md`)

Lecture de 12:16 à 12:27 UTC environ (`date -u`).

### Source et méthode

- **Copie de lecture** prise à 12:16 UTC dans le bac à sable : `registres/decisions.md`, 2 171 lignes, jusqu'à R-2200, sha256 `d10a422e69ca8d2177306ae1c45112659a6bf791760b7cb8a32d826e0db8c2a8` (le fichier vivant change pendant la tâche ; les lignes R- sont stables).
- **Index** : 1 171 lignes R- répondent aux motifs de la consigne (organisme, idéation, collisionneur, couche, pôle, juge, proposeur, fiche, loi, bisoci, moisson, aiguilleur, Avalon, récompense, Lean, théorie, Goodhart, nul v) ; 903 portent un terme propre à l'organisme (collisionneur, idéation, espèce, noyau, proposeur, orchestrateur, Goodhart, A1, W2, pôle, nœuds N1 à N13, D-P1, DEP, confrontation, étape 1 ou 2, pilote, Avalon, Lean…).
- **Lecture** : la colonne « décision » de ces 903 lignes, tronquée à 420 caractères (lignes R-059 à R-718) puis à 250 caractères (R-719 à R-2200) ; puis le texte entier, tronqué à 800-4 000 caractères, de 110 lignes choisies (décisions du directeur sur l'organisme, nœuds, résultats, définitions) : R-336, 344, 347, 376, 393, 432, 435, 443, 444, 447, 468, 471, 473, 476, 501, 504, 509, 525, 527, 529, 558, 567, 572, 583, 611, 632, 634, 642, 659, 662, 663, 764, 776, 782, 802, 809, 818, 820, 827, 838, 859, 862, 878, 895, 898, 901, 907, 910, 917, 920, 959, 962, 963, 965, 978, 986, 989, 990, 999, 1039, 1050, 1065, 1080, 1112, 1120, 1132, 1161, 1166, 1478, 1738, 1768, 1788, 1821, 1828, 1853, 1860, 1865, 1866, 1890, 1990, 1995, 1996, 1999, 2148, 2151, 2152, 2195, 2199.
- Lignes du programme principal (T0.5 à T0.8, P3, P3-bis, étiqueteur, G0, G1, NARCBench, entretien) : parcourues dans l'index, non reprises (hors objet), sauf quand elles fixent une règle qui vaut pour l'organisme (R-468, R-473, R-611).

### Cloison

- Les têtes de R-603, R-604 et R-605 (collisionneur sur le mode tenu à l'écart, 28 octobre) figuraient dans l'index et sont passées sous les yeux du rédacteur avant le filtre ; **rien de leur contenu n'est repris** dans l'inventaire ni ailleurs. Après ce constat, les lignes suivantes de l'index qui nomment le mode tenu à l'écart ou le bras d'attaque ont été retirées avant lecture : R-624, R-824, R-832, R-835 (non lues).
- R-2151 et R-2152 nomment deux documents de la session du bras sur `claude/compassionate-meitner-d4ryyk` : non ouverts ; seule la décision de Lazar sur le lien des deux lignées est reprise.
- Les cellules en quarantaine (N-057) et les générateurs BA-002 sont cités pour leur existence seulement.

### Sorties non lues

Listées dans `sorties-non-lues-v1.md` (scellé à 12:27 UTC, `fd46a13e…`). **Erratum** de ce fichier (scellé, non réécrit) : à la dernière rangée du § 2, « R-50 (N-050) » doit se lire « N-050 ».

### Doublons fusionnés

- La décision N-044 (R-376) et sa transcription (jalon 2) : une seule série d'entrées (jalon 2) ; R-376 n'ajoute que la primitive `question_ouverte`, déjà au jalon 2.
- N-045 (R-401, R-406) : entrées du jalon 2 ; R-408 et R-435 ajoutent le témoin « un modèle, vote à k », le bras « score permuté » et l'escalier de coût (entrées COM du jalon 3).
- Le juge statistique, les nuls v7 à v9, A1 à A1-v4 : entrées du jalon 1 ; le registre ajoute les incidents et la note W2 (entrées ATQ du jalon 3).
- Avalon apparaît en R-920 et R-959 : quatre entrées REC distinctes (question, constat, décision, piste écartée) et une entrée N13.

## Jalon 04 — synthèses scellées du collisionneur (`docs/notes/ideation-organisme-v1/course-2/`)

Lecture de 12:27 à 12:30 UTC environ (`date -u`). Empreintes vérifiées contre les compagnons (« OK »).

| clé | fichier | sha256 | lecture |
|---|---|---|---|
| SN1 | `collisionneur-noeuds-v1/synthese-noeuds-v12-tour1-v2.md` | `d313b4826d649ad8eb9a6e0b44a7b9eea452c7a74428b9626bcbb3bb237ee43e` | décompte de tête (l. 45-97), N1 et N3 en entier (l. 99-144), conclusions de N4, N5, N6, N9, N10, N11 (paragraphes « accords, divergences ») |
| SN2 | `collisionneur-noeuds-v1/synthese-noeuds-v12-tour2-v2.md` | `f4f2d1974828dcb9e8d9654614fa70328057ceb60833cc54e02f9eb1db13e9d2` | titres (recommandations par nœud), « recommandations telles que les espèces les laissent » et « pistes » (l. 333-356) |
| SNN | `collisionneur-n12-n13-v1/synthese-n12-n13-v2.md` | `f0340581766c5fb4d97a0ccb06f0cf1738a15228385b332ee602e93a0be28f0a` | N12 (1) à N13 (3) en entier (l. 63-161) |
| SBM | `collisionneur-boucle-moisson-v1/synthese-boucle-moisson-v2.md` | `efec05a9e4acfd39cce51e30614f903feed5a484d0353922e7d31cd412891738` | en-tête, Q7, pistes consensuelles et originales (l. 1-12, 195-199, 252-274) |

Non lus à ce jalon (renvoyés au jalon suivant ou listés comme trous) : les errata de ces synthèses (leurs remplacements sont intégrés aux v2) ; les v1 ; les critères de lecture ; les sections « Liens », « Convergences nées de la critique », « Inexactitudes » et « Pièces sans dépense » de SNN ; Q1 à Q6 de SBM en détail ; les sous-tables DL-1 à DL-13 de N6 ; les seize divergences et sept accords trop propres listés par SN2.

### Doublons fusionnés

- N12 (b) et N13 : la décision (jalon 3, R-959) et les contenus du collisionneur (jalon 4) restent des entrées distinctes ; les entrées du jalon 4 renvoient à R-959 pour le statut.
- N11 : la proposition de session-depot (jalon 3, règle de reconduction des bras, R-910) et les positions du collisionneur (jalon 4) restent distinctes.

## Jalon 05 — dépôt public de l'organisme (`/home/user/ideation-organism`, tête `6510199`)

Lecture de 12:30 à 12:33 UTC environ (`date -u`). Erratum : la v5 du journal, scellée, écrivait « 12:36 » par erreur.

| clé | fichier | sha256 | lecture |
|---|---|---|---|
| RDM | `README.md` | `b72c983eada4449931ff828d4e841aaf6708bce881657c745a8c113f3392321e` (identique à la page publique versée au dépôt de travail, clé PUB) | sections 1 à 4, 6 à 9 (l. 1-135, 162-235) ; section 5 (commandes) parcourue |
| CV7 | `orchestrator/conception-v7-v1.md` | `31fc8c4b…` (au § 1 des pièces) | entier (103 lignes), compagnon vérifié |
| PNT | `pont-fiche-loi-v1/LISEZMOI-pont-v1.md` | `7b1c131d…` (au § 1 des pièces) | l. 1-45 (état, ce qui reste), compagnon vérifié |
| — | `MANIFEST.md` | `c58638c9966d01ac1741ed90602e038e90b7e668d1e0cc58020cc670579fcf86` | non lu (liste de copie et d'exclusion) |

Non lus, et pourquoi :
- `orchestrator/pole/` (≈ 150 modules), `essais/`, `demonstrations/`, `exemples/`, `prereg/` : code et préenregistrements ; seuls les noms de modules ont été listés ; le README en donne la carte. Le module `pole/bras_attaque_v54.py` n'a pas été ouvert (cloison) : le README le dit « bouchon qui refuse de tourner ».
- `resultats/` (bancs de tricheurs v7 et v8, attaque de Goodhart v2, contrôles, prélectures du nul v8, puissance du juge, suite d'essais) : sorties publiées et scellées ; leurs chiffres sont repris du README ; non rouverts.
- `CITATION.cff` : non lu (citation).
- La conception du pont (`conception-pont-fiche-loi-v1.md`, `5161e199…`) n'est pas publiée (retenue, selon le README) : non lue.

Doublons fusionnés : le juge statistique, les nuls et l'attaque de Goodhart (jalons 1 et 3) ne sont pas répétés ; les entrées du jalon 5 ajoutent les mécanismes que la page publique décrit (voyage d'une idée en neuf étapes, table des tricheries et des gardes, banc des tricheurs v7 et v8, banc de mutations, évidences sur la banque réelle et la seconde course réelle, conception v7, pont).

## Jalon 06 — antériorité O1 à O20, question-mère, bisociation, juges v2, convergence de la défense, pilier attaque

Lecture de 12:33 à 12:35 UTC environ (`date -u`). Erratum : la v6 du journal, scellée, écrivait « 12:40 » par erreur.

| clé | source | lecture |
|---|---|---|
| C4R | rapport C4 (branche `prep/etat-de-l-art-niveau3-v1`, lu par `git show`, empreinte `164502a3…` égale au registre RAF) | verdict (l. 50-63), table finale O1 à O20 (l. 330-363), réserves et pièces à récupérer (l. 365-433) |
| QM | synthèse du collisionneur sur la question-mère v2 (`25e2d351…`) | verdict, éléments communs, recommandation, questions (l. 1-74, 175-215) |
| BIS | synthèse de la bisociation à deux espaces (`49dd3840…`) | verdict et éléments communs (l. 30-60) |
| JV2 | préenregistrement des juges v2, brouillon 4 (`f7616284…`) | statut, question, hypothèses (l. 1-77) |
| CDF | LISEZMOI de la convergence de la défense (`8456f998…`) | entier (46 lignes) |
| PAQ | question v2 scellée du pilier attaque (`2dbad4b7…`) | garde, motif, question, champs (l. 1-40) |

Vérifié absent (R11) : `docs/notes/organisme-courbe-dose-reponse-v1/` n'existe ni sur disque (`ls`) ni dans l'index (`git ls-files`, 0 fichier).

Non lus à ce jalon : notes d'antériorité Co-Scientist et POPPER (citées par RAF et C4R ; non relues ici) ; réponses d'Argon (question-mère v3) et de Kimi ; dossiers `argon-recherche-v1/`, `relais-kimi-v1/`, `argon-classes-ecart-v1/` ; synthèses du texte III, du tableau partagé, de l'axe 6 (leurs conclusions sont reprises du registre au jalon 3) ; `formalisation-jeu-convergence-v1.md` (`a277a5ba…`) et les sous-dossiers `argon-seul-convergence-v1/`, `regles-defense-v1/`, `jouet-openspiel-v1/` ; `ideation-pilier-attaque-v1/organisme-v1/` (devis, témoins, passe simulée) et les brouillons 1 à 8 de la question v2 ; la question v1 (`29870ac9…`).

## Jalon 07 — pièces restantes de l'organisme et programme de conception de conv-audit

Lecture de 12:35 à 12:38 UTC environ (`date -u`).

| clé | source | lecture |
|---|---|---|
| CL31, CL17 | contre-lectures de l'orchestrateur v31 et v52 | verdicts ; les verdicts des quinze autres contre-lectures (v34 à v51) relevés par recherche de la ligne « Verdict » |
| TFE | LISEZMOI v2 du tour fermé, étage 1 | en-tête (l. 1-12) |
| ISX | architecture de l'essai à blanc de l'Agentic Scientist v3 | en-tête (l. 1-12) |
| COF | question v2 du coffre des attaques inédites (niveau méthode et gouvernance) | en-tête (l. 1-12) |
| ABM | annexe du bras méta, brouillon 6 (196 667 octets) | en-tête « Pour Lazar » (l. 1-12) seulement |
| MJE | devis et plomberie de la machine jetable, v1 | en-tête (l. 1-8) |
| PCO | programme de conception de l'organisme v1 (conv-audit, branche `canal/conv-audit-n04`, lu par `git show`, empreinte égale à celle que cite la conception v7) | entier (90 lignes) ; le § 3, point 3 (bras d'attaque) n'est repris que pour son existence |

### Trous connus (ce qui n'a pas été lu, ou pas en entier)

1. **Registre des décisions** : têtes de 903 lignes et texte de 110 lignes seulement ; les autres lignes (programme principal, routine) peuvent porter des détails de l'organisme non repris.
2. **Synthèses du collisionneur** : nœuds (sous-tables DL-1 à DL-13, seize divergences et sept accords trop propres du tour 2), N12-N13 (liens, convergences, inexactitudes, pièces sans dépense), boucle moisson (Q1 à Q6 en détail) ; errata non lus à part ; synthèses du texte III, du tableau partagé, de l'axe 6, de la question 6 et 7 de la bisociation sur littérature réelle, de D-ML-1, des protocelles, de la mémoire du pôle, de « Boucle d'or », du pôle scientifique automatique, de la recombinaison (v1, v2), du proposeur enfichable, du duel « idée P-041 », de l'arène : conclusions reprises du registre seulement.
3. **Réponses d'espèces seules** (Argon, Kimi) : `question-mere-reponses/` (réponse d'Argon à la question-mère v3, dont la consigne n'a pas été versée, R-2191), `relais-kimi-v1/`, `argon-recherche-v1/`, `argon-classes-ecart-v1/`, `docs/notes/reponses-especes-seules-2026-11-01-v1/`, `docs/notes/argon-seul-v1/` : non lues.
4. **Pièces de l'organisme** : consignes des rôles de la mini-course du tour fermé (aiguilleur, juge, lecteur, metteur en forme, proposeur) ; préenregistrements et pièces d'A1-v3 et d'A1-v4 hors des verdicts cités par RAF ; épreuve W2g ; conception du juge-tournoi v1 et v2 (reprises du registre) ; devis de la course 2 (v4 à v6), dossier de service, listes closes, note sur les épisodes de calibrage ; annexe du bras méta au-delà de l'en-tête ; machines jetables v2 et v3 ; lancements v1 et v2 (commandes Argon, relais Gemini) ; IA scientifique externe v1 (choix) et v3 (lecture du code et devis) ; brèche W2 (reprise du registre) ; validation du nul v9 (audit) ; vérification des valeurs non finies ; reproduction de R-599 ; instantanés de l'orchestrateur v51, v52, v52b ; outils des contre-lectures ; préenregistrement et devis de la boucle réelle (en-tête seulement) ; code v65 (branche `prep/organisme-v65-v1`, cité par RAF).
5. **Autres dossiers de notes liés à l'organisme**, hors de la liste de la consigne et non ouverts : `pole-scientifique-automatique/` (il peut contenir un dossier du bras d'attaque : non parcouru), `collisionneur-boucle-d-or-v1/`, `collisionneur-memoire-encodage-v1/`, `collisionneur-proposeur-enfichable-v1/`, `collisionneur-conception-qo1-q1-v1/`, `protocelles-collisionneur-v1/`, `anteriorite-P-041-v1/`, `affinage-equipe-rouge-v1/` et `-v2/` (conception de l'affinage, 89 attaques, au niveau méthode selon R-649 : non lue), `couche-2-preparation-v1/`, `epreuve-fraiche-pont-v1/`, `bisociation-litterature-reelle-v1/`, `mini-course-kimi-argon-v1/`, `weight-space-programming-v1/`, `gu-krenn-v1/`, `suite-hm1-v1/`, `taif-v1/`.
6. **Branche de conv-audit** (`canal/conv-audit-n04`) : seul le programme de conception v1 a été lu ; ses versions suivantes, le programme v7 de conv-audit (neuf voies, six classes cibles), les conceptions du pont et des couches, et ses registres ne l'ont pas été.
7. **Dépôt public** : code (`pole/`, `essais/`, `demonstrations/`, `exemples/`), `prereg/`, `resultats/`, `MANIFEST.md`, `CITATION.cff` non lus (le README en donne la carte).
8. **Notes d'antériorité** Co-Scientist et POPPER : non relues (reprises par RAF et C4R).
9. Le dossier `docs/notes/organisme-courbe-dose-reponse-v1/` n'existe pas (vérifié).

### Cloison et interdits

- Aucun fichier interdit ouvert ; aucune recherche récursive sur un dossier contenant un chemin interdit (recherches par `git grep` avec exclusions, par listes de fichiers nommés, ou dans la copie de lecture du registre).
- Exposition à signaler : les têtes de R-603 à R-605 (mode tenu à l'écart) sont passées sous les yeux du rédacteur dans l'index du registre (jalon 3) ; rien n'en est repris.
- Le module public `pole/bras_attaque_v54.py` et le point 3 du programme de conception (bras d'attaque) : existence seulement.

### Doublons fusionnés

- La conception v7 (jalon 5) et le programme de conception v1 (jalon 7) décrivent tous deux le proposeur, le moissonneur, le nul informé et la configuration sans urne : les entrées du jalon 5 portent le détail, celles du jalon 7 l'ordre de conception et les couches.
- Les couches 3 et 4 : les entrées des jalons 3 (R-920), 4 (N12-N13) et 7 (programme v1) restent séparées, avec une entrée de jalon 7 qui signale les deux numérotations.

