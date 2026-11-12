# Journal de l'inventaire de l'organisme d'idéation — v2 (jalons 1 et 2)

- Version v2, écrite le 10 novembre 2026 à 12:15 UTC (`date -u`) ; accompagne `inventaire-idees-organisme-v2.md` ; reprend la v1 (`46c5ba26…`) et ajoute le jalon 2.

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

