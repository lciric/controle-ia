# Vérification neuve du module v3 face au brouillon 5 — addendum 2 de P3 — lentille « fidélité au texte » — v1

**Verdict : conforme après corrections.** Le module v3 fait ce que dit le brouillon 5, règle par règle : chaque garde,
chaque déclencheur, chaque descriptif, chaque phrase de lecture et d'arrêt. Aucune correction du module ni des tests.
Les corrections portent sur le texte, avant le scellement : la section « Contre-lecture » ne peut pas recevoir
l'histoire réelle (VV3-texte-01) ; le marqueur de durée doit être remplacé avec ses accents graves, par une phrase exacte
(VV3-texte-04) ; cinq lignes de forme. La garde 7 choisie pour la précision 14 est compatible avec le texte ; une ligne
est proposée pour la nommer.

| id | gravité | constat (une ligne) |
|---|---|---|
| VV3-texte-01 | mineur | Section « Contre-lecture » : une seule entrée du code, non numérotée, à deux rapports, pour trois tours réels (dont un à un seul sous-agent) ; elle masque une empreinte manquante de l'entrée 2 dans `prereg.problemes` |
| VV3-texte-02 | forme | Précision 14 : la garde n'est pas nommée ; le module écrit « garde 7 : run source hors de forme » ; compatible, une ligne la nomme |
| VV3-texte-03 | forme | Précision 2 : « garde sa valeur ponctuelle » ; le descriptif de la part en échec n'a pas de valeur, elle n'est écrite que dans l'audit |
| VV3-texte-04 | mineur | Marqueur `<<DUREE_MESUREE>>` écrit entre accents graves ; la phrase proposée par les notes a une plage élargie (2,0 à 2,2 s), un chemin à remplir, et ne dit pas que le module mesuré est une copie aux constantes du jouet |
| VV3-texte-05 | forme | Préambule des précisions : « déjà appliquées … là où le texte se taisait (CC-texte-06) » n'est plus exact pour les précisions 2 et 11 à 14 |
| VV3-texte-06 | forme | Imports des tests : `pytest` et `committer`, `git` de `tests/conftest.py` ne sont pas écrits (CV2-09, non traité) |
| VV3-texte-07 | forme | M5 : à 1 % de tirages dégénérés au plus, le module prend l'intervalle de la part sur les seuls tirages non dégénérés ; le texte se tait |

Aucun constat critique ni majeur. Un candidat d'essai qui applique les sept corrections et remplit les douze marqueurs
passe `prereg.problemes` sans aucun problème, et la garde 1 y lit exactement les empreintes du module et des tests v3
(section E).

## Cadre

- Vérificateur : sous-agent neuf. Je n'ai écrit ni l'addendum 2 (aucun brouillon), ni aucune version de son module ou
  de ses tests, ni aucune contre-lecture, vérification ou traitement antérieurs. Date : 2026-10-20 (UTC), de 19:57 à
  20:20 environ.
- Écrit seulement sous `…/scratchpad/addendum2-p3/verification-v3/` : ce rapport et son compagnon, et mon dossier
  `verification-v3/texte/` (noté `texte/`). Les sous-dossiers `base/`, `journaux/`, `mutants/`, `outils/`, `tmp/` de
  `verification-v3/`, créés avant moi par un autre agent, n'ont été que listés.
- Dépôt de travail en lecture seule ; git en lecture ; lancements avec `python -B`, `PYTHONDONTWRITEBYTECODE=1`,
  `-p no:cacheprovider`, interpréteur de la consigne (Python 3.11.17), `PYTHONPATH=src`. Aucune recherche récursive dans
  le dépôt : seulement des listes de dossiers (`prereg/contre-lectures/`, `docs/procedures/`) et des fichiers nommés.
- R1 : section « R1 et intégrité ». Aucune grandeur de B1, de B2 ni de l'addendum 2 sur les données réelles.

## Pièces lues (empreintes vérifiées avant lecture ; aucun écart)

| pièce | sha256 |
|---|---|
| brouillon 5 `…/addendum2-p3/P3-addendum2-audit-verdict-v1-brouillon5.md` (en entier) | `db53d140d5a8d000d0d9f444a86215a9cd15e0fbdaa3f764c41facf3a5889a1f` (égale au compagnon) |
| brouillon 4 (différentiel avec le brouillon 5 seulement) | `9565f4b976a57b4f956237e878ea3f9c96a31737994d21d6c734d8cde53e8316` (égale au compagnon) |
| contre-lecture du module v2 `…/revue-v2/contre-lecture-code-addendum2-v2.md` (en entier) | `8c2902e4d1b8bfdbdfa5c8066eedd2ea526e24e73a9387ac4990665b72a07737` |
| registre des décisions, ligne R-288 (CV2-01, option (b)) | registre vivant, lu à la tête `c52225b` |
| module v3 `…/module-v3/audit_verdict_p3_v1.py` (en entier, 1 558 lignes) | `967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d` |
| tests v3 `…/module-v3/test_audit_verdict_p3_v1.py` (en-tête, imports, tests des précisions 2, 11 et 14, test des constantes) | `d0c5eb07da17a1bf27fc38905edd648e4653ba9f3652076560ee4c4c3ba83b28` |
| notes `…/module-v3/NOTES-MODULE-v3.md` (en entier) | `7283bc515af02f79c0a1e693654cfa5fe772ea1be03af3f254714c41e8d44756` |
| mesures `…/module-v3/mesures-duree-v1.txt` (en entier) ; `journaux/mesure-duree-v3.log` | `c16ace640bd273ce073c384292771da946d2d3ec1dfee1be07b47c69115191ba` ; `c4c18fa1777bfffff7c24d71fc70dc261ba7f62c4197f178903b26aeed002e18` |
| module v2 (différentiel avec le v3 seulement) | `dfdeef6b4652a9faad06cecd708385341f044ec4164efade1f82a4a1cf6e7a3d` |
| code gelé lu : `prereg.py` (en entier), `statistiques.py` l. 1-90, `lecture.py` l. 100-160 et 220-300, `harnais/validation_reelle.py` l. 50-56 | les six empreintes du texte égales au disque et au commit `7a54d43` (outil, section A) |
| [PA] `prereg/P3-addendum-lecture-complementaire-v1.md` : section « Contre-lecture », point 9 du plan | `8ff834229444b214f3f4c248ecdbf619a4b7149700825ef39bac2e86a6ff80ac` (égale au compagnon) |
| têtes des contre-lectures 1 et 2, des deux rapports du premier tour du code, traitement du premier tour | empreintes en section D |

Tous les compagnons de `module-v3/` (4) et de `module-v3/journaux/` (18) sont justes à la fin de mon travail.

## A. Fidélité du module v3 au brouillon 5

« = » : conforme. « + » : ajout du module là où le texte se tait ; il ne peut qu'arrêter ou ajouter un descriptif, sans
changer un nombre décisif, une réserve ni le verrou. Lignes : texte (t.) brouillon 5 ; module (m.) v3.

### A1. Ce que le brouillon 5 change (différentiel brouillon 4 → 5) et ce que fait le v3

Différentiel du module v2 → v3 : trois blocs, exactement les deux changements des notes (m. 408-421 ; m. 1088-1089 et
le retrait de l'ancienne branche « part en échec »). Aucun autre octet ne change.

| règle du brouillon 5 | module v3 | état | preuve |
|---|---|---|---|
| Audit, point 3 (t. 428-430) et précision 2 (t. 446-448) : « non calculé » seulement si M5 n'est pas calculée ou si `E0` = 0 ; une part en échec garde sa valeur ponctuelle et ne fait pas taire le déclencheur | m. 1090-1099 : `pf["etat"]` ≠ calculé → non calculé ; `E0` = 0 → non calculé ; sinon `D / E0`, vrai hors de [−1 ; 1] | = (lieu de la valeur : VV3-texte-03) | essais 1 à 5 : part en échec à 5,25 → vrai ; à 0,525 → faux ; M5 non calculable ou en échec → non calculé ; `E0` = 0 → « E0 = 0 » ; bornes −1 et 1 comprises dans l'intervalle |
| Précision 1 (t. 443-445) : intervalle décisif non lu → non calculé, avant « sans objet » ; `E_sf` non calculable **ou en échec** → non calculé, après « sans objet » (CV2-07) | m. 1067-1083 | = | essais 6 à 8 (les deux ordres, les deux états, bords 0 et log10 3) |
| Plan, points 7 et 8 (t. 373-378) : « lus » compte les « non lus », rapportés à part (CV2-06) | `_compte` m. 1129-1133 : `ecrits`, `lus`, `dont_non_lus`, `sans_objet` | = | essai 14 |
| Précision 11 (t. 461-462) : `P3-P3/<p>` en échec dans [L] : « non comparé (entrée en échec) » ; « même état » pour P3-P1, P3-P2, mention seulement | m. 870-874 ; m. 832-845 | = | outil (chaîne mot pour mot) ; test v3 l. 503 |
| Précision 12 (t. 463-465) : recommandation {conclusion, réserve, lecture} pour les conclusions établies visées par un contrôle lu ; ligne de l'audit avec la phrase et, à part, `consigne`, seulement si le déclencheur est vrai | m. 1163-1178 ; m. 1102-1103 | = | essai 12 (clés exactes ; ligne de l'audit absente sans déclencheur, présente avec) |
| Précision 13 (t. 466-467) : « D = 0 : retirer les actions à forme ne change pas la différence » | m. 300 | = | outil (mot pour mot) ; essai 13 |
| Précision 14 (t. 468) : [SF] sans `principales` → arrêt écrit, jamais une exception nue | m. 408-421 : `GardeArret` « garde 7 : run source hors de forme : [SF] sans `principales.<c>` … » ; appelée en tête de `controler_entrees` (m. 938), hors de tout calcul, donc arrêt (avant le manifeste au lancement, dans la clé `arret` après) | = (nom de la garde : VV3-texte-02) | essais 9 à 11 : cinq artefacts (clé absente, `None`, vide, nombre), type exact `GardeArret`, arrêt dans la fonction pure (pas un « échec ») ; cas sain |

Mes essais séparent le v3 du v2 exactement sur ces règles : sur le module v2, 8 des 24 essais échouent (les deux du
déclencheur 3 en échec de la part, les six de la précision 14), les 16 autres passent
(`texte/journaux/pytest-essais-sur-module-v2.log`).

### A2. Gardes 1 à 15 (t. 475-526)

| garde | module v3 | état |
|---|---|---|
| 1 | m. 1260-1288 ; expressions m. 73-74 | = ; + « tests du module absents » (m. 1278-1280). Sur le texte rempli, les deux expressions trouvent chacune une seule ligne et lisent les empreintes v3 (section E) |
| 2 | m. 1291-1308 ; `ENTREES` m. 82-101 | = (neuf pièces, chemins et empreintes égaux au texte, outil) |
| 3 | m. 1354-1387 | = ; + critère lexical aussi pour l'unicité (comme la garde 2 de [PA]) |
| 4 | m. 1414-1444 | = (descendance stricte de N-025 ; égalité stricte du commit du manifeste, précision 5) |
| 5 | m. 1447-1458 ; m. 1317-1351 | = (chaînes du critère lexical et 64 octets égaux au texte, outil) |
| 6 | m. 1461-1469 | = ; + exceptions du chargeur converties en arrêt écrit |
| 7 | m. 822-886 ; `principales_du_run` m. 408-421 ; `_tables` m. 392-405 | = ; tolérances 10⁻¹² et 10⁻⁹ ; + arrêts « run source hors de forme » (VV3-texte-02) |
| 8 | m. 889-903 | = |
| 9 | m. 726-794 ; précision 7 m. 731-733 | = ; + types des valeurs lues |
| 10 | m. 906-912 | = |
| 11 | m. 1472-1492 ; appel des paramètres m. 1543 | = |
| 12 | m. 372-387 ; appel m. 1218, après le manifeste, dans le `try` | = |
| 13 | m. 915-932 | = (entrée en échec non contrôlée, comme la garde 9 le permet) |
| 14 | m. 1183-1210 | = ; + `issue_primaire` |
| 15 | m. 540-548 | = (VV3-texte-07 pour le cas à 1 % au plus) |

Préambule de la liste d'arrêt (seule `GardeArret` donne « échec ») : `_calcul` m. 342-351, `NonCalculable` sous-classe
de `GardeArret` pour « non calculable » ; toute autre exception arrête ; après le manifeste, l'arrêt est écrit (m.
1522-1528). =

### A3. Métrique, seuil, critères

| règle | module v3 | état |
|---|---|---|
| M1, M2 ; formes dans l'ordre de M2 | `_a_forme` m. 424-429 ; `FORMES` m. 120-121 | = (outil) |
| M3 : copie NaN, fonction gelée, deux conditions, comptes propres | m. 432-459 | = ; + `actions`, `nulles_d_origine` ; « illisibles d'origine » compte les nuls, comme `cout_de_tache` (gelé, statistiques l. 37-44) |
| M4 : `effet_cout_apparie`, « non calculable » sous deux tâches | m. 508-517 | = |
| M5 : `D`, `E0`, part, mêmes lignes tirées, 1 %, « instable », libellés | m. 520-555 | = ; VV3-texte-07 |
| M6 : médiane sur les tâches, comptes, sept quantiles | m. 558-576 | = (quantiles égaux au texte, outil) |
| M7, M8, M9 | m. 579-633 | = ; + contrôle des mêmes tâches en M7 |
| M10 : `w`, `z`, `z80`, `A_seuil`, `A_80`, écrits, distances ; exclusions | m. 686-709 | = (z, z80 à 10⁻¹² ; 0,5809 ; 0,5544 ; 0,545 et 0,567, outil) ; aucune grandeur exclue n'est écrite |
| 47 clés, dans l'ordre | `cles_addendum2` m. 363-369 | = (liste reconstruite du texte seul, égale, outil) |
| Réserves : onze noms ; conditions ; table des cas de B1 ; cibles | m. 989-1046 | = (noms égaux, outil ; conditions relues une à une) |
| Clés interdites | m. 131-132 | = (outil) |
| Phrases de la table des critères (neuf lignes de réserve, « aucune réserve », audit, arrêt) | `LECTURES` m. 163-193 ; `_lecture_de` m. 1110-1126 | = (chaque « … » du texte égal à la phrase du module, grandeurs exceptées, outil) |
| Classements du seuil ; libellés de `D` | m. 271-300 | = (outil) |
| Synthèse, plan 7 ; 13 contrôles, plan 8 | m. 1154-1180 ; m. 1136-1151 | = |
| Audit, point 1 (même traitement) ; déclencheur vrai si 2 ou 3 | m. 1054-1060 ; m. 1100-1105 | = |

L'outil de comparaison (`texte/outils/comparer_texte_code_v3.py`) fait 69 contrôles mécaniques : 0 écart
(`texte/journaux/comparer-texte-code-v3.log`). Éprouvé sur un artefact (copie du module où trois phrases changent) :
3 écarts, exactement les trois (`texte/journaux/comparer-texte-code-v3-artefact.log`).

**Ni plus ni moins.** Je ne trouve aucune règle du texte que le module omet. Les ajouts « + » ci-dessus ne font
qu'arrêter avec un motif écrit, ou ajouter un descriptif ; deux méritent une ligne au texte (VV3-texte-02 et 07), les
autres découlent du texte (« aucune valeur devinée », « aucun repli silencieux »).

## B. Garde 7 et précision 14 (CV2-10)

**Compatible.** La précision 14 ne nomme pas de garde : aucune contradiction. Le choix de la garde 7 suit le texte :

- la garde 7 est la première qui lit [SF] et les sondes principales (« pour chaque sonde principale, aire saboteur contre
  honnête … », t. 502-504 ; « Plancher de la garde 7 : les sondes `<p>-plancher-k` de [SF] », t. 269) ;
- au lancement, aucune garde avant la 7 ne lit `principales` (la garde 6 ne vérifie que sceaux et empreintes, gelé
  `lecture.charger_source` l. 116-137) ;
- les autres arrêts « run source hors de forme » du module (tables, colonnes, longueurs, table des scores) portent déjà le
  nom de la garde 7 ;
- la garde 9 (précision 7) compare ensuite les sondes de [L] à celles de [SF] : elle suppose [SF] lisible.

Une ligne reste utile : le motif « garde 7 : … » sera cité au verdict en cas d'arrêt, et le texte doit dire ce qu'il
nomme. Mots exacts : VV3-texte-02.

## C. Marqueurs du brouillon 5 : valeur ou chemin

`prereg.problemes` sur le brouillon 5 tel quel : deux problèmes seulement, (1) « contre-lecture 2 sans ses deux
empreintes (brouillon relu et rapport) », dans la section « Contre-lecture » ; (2) « marqueurs de gabarit restants »,
les douze ci-dessous. Rien d'autre.

| marqueur (ligne) | à remplir par |
|---|---|
| `<<EMPREINTE_MODULE>>` (l. 23) | `967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d` (module v3, versé tel quel sous `docs/procedures/P3-addendum2-v1/audit_verdict_p3_v1.py`) |
| `<<EMPREINTE_TESTS>>` (l. 24) | `d0c5eb07da17a1bf27fc38905edd648e4653ba9f3652076560ee4c4c3ba83b28` (tests v3, versés tels quels sous `docs/procedures/P3-addendum2-v1/test_audit_verdict_p3_v1.py`) |
| `<<NOMBRE_TESTS>>` (l. 24) | `121` (recueillis par pytest : « 121 tests collected », `texte/journaux/pytest-collecte-v3.log` ; 76 fonctions ; en tête du fichier de tests : « Nombre de tests attendu : 121 ») |
| `` `<<DUREE_MESUREE>>` `` (l. 385), **accents graves compris** | la phrase de VV3-texte-04 |
| `<<SHA_TRAITEMENT_1>>` (l. 581) | `dfce4ccaee074228b2873033201373322fe0005314ea88900863eec5001a1392` (`…/addendum2-p3/traitement-R2-addendum2-P3-v1.md`, empreinte égale à celle que cite la vérification 2) |
| `<<SHA_VERIFICATION_2>>` (l. 585) | `65afdd6c7e23d6cba334442ff1b99ec7ef89a2d35e327d47b7d1cb98e7be1461` (`…/addendum2-p3/verification/verification-corrections-brouillon2-addendum2-P3-v1.md`) |
| `<<SHA_TRAITEMENT_2>>` (l. 587) | `155e8fe173db2315a8f60afe61aa61cd72a0fcd4a65855cccdc0b1007e1734ca` (égale au compagnon) |
| `<<CHEMIN_RAPPORT_CODE_TEXTE>>`, `<<SHA_RAPPORT_CODE_TEXTE>>`, `<<CHEMIN_RAPPORT_CODE_MUTANTS>>`, `<<SHA_RAPPORT_CODE_MUTANTS>>`, `<<SHA_BROUILLON_CODE>>` (l. 589-590) | ne pas remplir en place : l'entrée entière est remplacée par les contre-lectures 3, 4 et 5 (VV3-texte-01), qui portent les chemins et empreintes de la section D |

Faits déjà écrits dans la section, vérifiés : brouillon 1 `2698af04…`, contre-lecture 1 `ad360e02…` (« scellable après
corrections », 3 majeurs, 7 mineurs, 3 pour information) ; brouillon 2 `641b36c2…`, vérification 2 (« scellable après
corrections », 7 mineurs, 5 pour information) : justes.

## D. Pièces à verser sous `prereg/contre-lectures/`

Forme reprise du premier addendum : `contre-lecture-code-b3-1-addendum-P3-v1.md` (b3 : brouillon relu ; 1 : angle),
`verification-code-final-addendum-P3-v1-texte.md`, `notes-corrections-code-addendum-P3-v1.md`, dossiers
`brouillons-addendum-P3-v1/` et `versions-relues-addendum-P3-v1/`. Un fichier renommé garde son empreinte ; son compagnon
nomme le fichier : le refaire au versement (`python -m controle_ia.scellement sceller FICHIER`).

| source (sous `…/scratchpad/addendum2-p3/`) | sha256 | chemin proposé |
|---|---|---|
| `contre-lecture-R2-brouillon1-addendum2-P3-v1.md` | `ad360e028ae0d9f08941bbab689631aea763e3966fe7f0be4fc5ed3cc3a112d1` | `prereg/contre-lectures/contre-lecture-R2-brouillon1-addendum2-P3-v1.md` (déjà nommé par le texte) |
| `traitement-R2-addendum2-P3-v1.md` | `dfce4ccaee074228b2873033201373322fe0005314ea88900863eec5001a1392` | `prereg/contre-lectures/traitement-R2-addendum2-P3-v1.md` (déjà nommé) |
| `verification/verification-corrections-brouillon2-addendum2-P3-v1.md` | `65afdd6c7e23d6cba334442ff1b99ec7ef89a2d35e327d47b7d1cb98e7be1461` | `prereg/contre-lectures/verification-corrections-brouillon2-addendum2-P3-v1.md` (déjà nommé) |
| `traitement-verification-brouillon2-addendum2-P3-v1.md` | `155e8fe173db2315a8f60afe61aa61cd72a0fcd4a65855cccdc0b1007e1734ca` | `prereg/contre-lectures/traitement-verification-brouillon2-addendum2-P3-v1.md` (déjà nommé) |
| `revue-texte/contre-lecture-code-addendum2-texte-v1.md` (brouillon 2, module v1) | `8a2a92d295c5fad3d2f378d8b9010ec1e3b11769733c5765a813ea3e131d4884` | `prereg/contre-lectures/contre-lecture-code-b2-1-addendum2-P3-v1.md` |
| `revue-mutants/contre-lecture-code-addendum2-mutants-v1.md` (brouillon 2, module v1) | `5330e1f1d86e92b98f7a3d16dad397cfe765ae1d28f11c318feb3d1b04cbd3ba` | `prereg/contre-lectures/contre-lecture-code-b2-2-addendum2-P3-v1.md` |
| `traitement-contre-lectures-code-addendum2-P3-v1.md` | `f2ac84b0c0da022e71ed720d3f7e3815f6838aaa48289d0a8f7bd514d3e8779a` | `prereg/contre-lectures/traitement-contre-lectures-code-addendum2-P3-v1.md` |
| `revue-v2/contre-lecture-code-addendum2-v2.md` (brouillon 4, module v2) | `8c2902e4d1b8bfdbdfa5c8066eedd2ea526e24e73a9387ac4990665b72a07737` | `prereg/contre-lectures/contre-lecture-code-b4-addendum2-P3-v1.md` |
| `module-v3/NOTES-MODULE-v3.md` | `7283bc515af02f79c0a1e693654cfa5fe772ea1be03af3f254714c41e8d44756` | `prereg/contre-lectures/notes-module-v3-addendum2-P3-v1.md` |
| `module-v3/mesures-duree-v1.txt` ; `module-v3/mesure-duree/mesure_duree_v3.py` ; `module-v3/journaux/mesure-duree-v3.log` | `c16ace640bd273ce073c384292771da946d2d3ec1dfee1be07b47c69115191ba` ; `545d533433834060edd80ea34e0a28c73cdf4f059e548e7ff310ecec5b0dcdb2` ; `c4c18fa1777bfffff7c24d71fc70dc261ba7f62c4197f178903b26aeed002e18` | `prereg/contre-lectures/notes-module-v3-addendum2-P3-v1/` (mêmes noms ; le compagnon de `mesures-duree-v1.txt` reste valable) |
| `verification-v3/verification-module-v3-texte-v1.md` (ce rapport) | dans son compagnon | `prereg/contre-lectures/verification-code-final-addendum2-P3-v1-texte.md` |
| rapport de la lentille « mutants et pannes » de cette vérification, s'il existe | — | `prereg/contre-lectures/verification-code-final-addendum2-P3-v1-mutants.md` (une ligne de plus par autre lentille, même forme) |
| brouillons 1 à 5 | `2698af04…ab90`, `641b36c2…1615`, `e3f8528c…645a`, `9565f4b9…8316`, `db53d140…9a1f` | `prereg/contre-lectures/brouillons-addendum2-P3-v1/P3-addendum2-audit-verdict-v1-brouillon<k>.md` |
| module et tests v1, v2 relus | `0b991450…69cf`, `ecbb8972…bfd3` ; `dfdeef6b…7a3d`, `a5c6ec34…92fd` | `prereg/contre-lectures/versions-relues-addendum2-P3-v1/audit_verdict_p3_v1-0b991450.py`, `test_audit_verdict_p3_v1-ecbb8972.py`, `audit_verdict_p3_v1-dfdeef6b.py`, `test_audit_verdict_p3_v1-a5c6ec34.py` |

## E. Candidat d'essai

`texte/outils/candidat_essai_v1.py` applique au brouillon 5 les sept corrections ci-dessous et remplit les douze
marqueurs (les deux empreintes des rapports de la contre-lecture 5, inconnues ici, sont fictives : 0…0 et 1…1).
Résultat, `texte/candidat-essai-v1.md` (`95437d9f093027ff87fc31d4344cff36dc52b79ff990e9b3e056db1815979fed`) :

- `prereg.problemes` : `[]` ; les huit sections exigées présentes ;
- garde 1 : l'expression du module lit `967270761c92…` ; celle des tests lit `d0c5eb07da17…` ; une ligne chacune ;
- différentiel avec le brouillon 5 : 72 lignes, toutes dans les endroits listés
  (`texte/journaux/diff-brouillon5-candidat-essai-v1.txt`).

Ce candidat est un essai, pas une proposition de fichier à verser : la session écrit le sien, puis compare au brouillon 5.

## Constats détaillés

### VV3-texte-01 (mineur) — Section « Contre-lecture » : une entrée du code pour trois tours

- **Texte.** l. 588-590 : « **Contre-lecture du code** — deux sous-agents neufs … : (i) texte face au code,
  `<<CHEMIN_RAPPORT_CODE_TEXTE>>` … ; (ii) mutants et pannes, `<<CHEMIN_RAPPORT_CODE_MUTANTS>>` … ; sur le brouillon
  `<<SHA_BROUILLON_CODE>>`. » ; l. 69-70 : le module est « contre-lu par deux sous-agents neufs (texte face au code ;
  mutants) ».
- **Faits.** Trois tours : (1) brouillon 2, module v1, deux sous-agents (texte ; mutants et pannes) ; (2) brouillon 4,
  module v2, **un seul** sous-agent pour les deux angles ; (3) brouillon 5, module v3, cette vérification (lentille
  « texte » ; une autre lentille travaille dans `verification-v3/`). La campagne de mutants rejouée par le correcteur du
  module sur le v3 (notes v3) n'est pas une contre-lecture neuve.
- **Problème.** Remplie telle quelle, l'entrée citerait un seul tour et dirait « deux sous-agents » pour tous. Et, non
  numérotée, elle échappe au contrôle par entrée de `prereg.problemes` : ses empreintes sont comptées dans l'entrée 2.
  Preuve : brouillon 5 dont l'entrée 2 perd ses deux empreintes de rapport et de traitement, entrée du code remplie →
  `problemes` = `[]` ; même texte, entrée numérotée « Contre-lecture 3 » → « contre-lecture 2 sans ses deux empreintes »
  (`texte/journaux/masquage-entree-non-numerotee.log`).
- **Correction (mots exacts).** Remplacer tout le point qui commence par « - **Contre-lecture du code** — » et finit par
  « `<<SHA_BROUILLON_CODE>>`. » par le texte de `texte/outils/section-contre-lecture-code-proposee-v1.md`
  (`4d94c19ff30baa51066984412fed646ce3c98d4607fae6b4a5efe7cbec7e8bdc`), recopié ici :

  ```
  - **Contre-lecture 3** — code écrit sur le brouillon 2 (sha256
    `641b36c2d8b77ca78c6f9bdd151cc3a3cc38a468e4f2a307e01e94354f651615`) : module v1 (sha256
    `0b991450d107ee16b484a568d91f95ca232b5079d42ae17b6c52ec2bd23369cf`) et ses 42 tests (sha256
    `ecbb897293b690b37e0f086c86ca575b97c0a6bfedcec69f56849023afa8bfd3`), relus par deux sous-agents neufs, qui n'ont écrit
    ni le texte, ni le module, ni ses tests : texte face au code, rapport
    `prereg/contre-lectures/contre-lecture-code-b2-1-addendum2-P3-v1.md` (sha256
    `8a2a92d295c5fad3d2f378d8b9010ec1e3b11769733c5765a813ea3e131d4884`), « scellable après corrections » ; mutants et
    pannes, rapport `prereg/contre-lectures/contre-lecture-code-b2-2-addendum2-P3-v1.md` (sha256
    `5330e1f1d86e92b98f7a3d16dad397cfe765ae1d28f11c318feb3d1b04cbd3ba`), « scellable après corrections » (107 mutants,
    66 tués, 41 survivants dont 4 équivalents). Traitement :
    `prereg/contre-lectures/traitement-contre-lectures-code-addendum2-P3-v1.md` (sha256
    `f2ac84b0c0da022e71ed720d3f7e3815f6838aaa48289d0a8f7bd514d3e8779a`) : brouillon 4, module et tests v2.
  - **Contre-lecture 4** — module v2 (sha256 `dfdeef6b4652a9faad06cecd708385341f044ec4164efade1f82a4a1cf6e7a3d`) et ses
    118 tests (sha256 `a5c6ec3412c04a1e7e3af8bb1ebb168c22a3aab40b7111821d24558523dc92fd`) relus face au brouillon 4
    (sha256 `9565f4b976a57b4f956237e878ea3f9c96a31737994d21d6c734d8cde53e8316`) par un seul sous-agent neuf, sous les deux
    angles (texte face au code ; mutants et pannes) : rapport
    `prereg/contre-lectures/contre-lecture-code-b4-addendum2-P3-v1.md` (sha256
    `8c2902e4d1b8bfdbdfa5c8066eedd2ea526e24e73a9387ac4990665b72a07737`), « scellable après corrections », CV2-01 à CV2-04
    mineurs, CV2-05 à CV2-11 pour information (230 mutants, 200 tués, 30 survivants dont 5 équivalents). Traitement :
    registre des décisions, R-288 (CV2-01, option (b)) ; brouillon 5 ; module et tests v3, notes
    `prereg/contre-lectures/notes-module-v3-addendum2-P3-v1.md` (sha256
    `7283bc515af02f79c0a1e693654cfa5fe772ea1be03af3f254714c41e8d44756`).
  - **Contre-lecture 5** — module v3 (sha256 `967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d`) et ses
    121 tests (sha256 `d0c5eb07da17a1bf27fc38905edd648e4653ba9f3652076560ee4c4c3ba83b28`) relus face au brouillon 5
    (sha256 `db53d140d5a8d000d0d9f444a86215a9cd15e0fbdaa3f764c41facf3a5889a1f`) par des sous-agents neufs, qui n'ont écrit
    ni le texte, ni aucune version du module, ni aucune contre-lecture antérieure : fidélité au texte, rapport
    `prereg/contre-lectures/verification-code-final-addendum2-P3-v1-texte.md` (sha256 `<empreinte de ce rapport>`),
    « conforme après corrections » ; mutants et pannes, rapport
    `prereg/contre-lectures/verification-code-final-addendum2-P3-v1-mutants.md` (sha256 `<empreinte>`), « <verdict> ».
    Constats traités dans le texte (ce candidat) ; le module relu est le module cité en tête.
  ```

  Remplir `<empreinte de ce rapport>`, `<empreinte>` et `<verdict>` au versement. **Condition** : sans rapport neuf
  « mutants et pannes » sur le v3, l'entrée 5 doit le dire, et la phrase des l. 69-70 n'est plus vraie du module final.

### VV3-texte-02 (forme) — Précision 14 : nommer la garde 7

- **Texte.** l. 468 : « 14. Un [SF] sans `principales` arrête avec un motif écrit, jamais par une exception nue
  (brouillon 5, CV2-10). »
- **Code.** m. 408-421 : motif « garde 7 : run source hors de forme : [SF] sans `principales.<c>` (clé absente ou valeur
  non textuelle : … ; aucune valeur devinée) » ; aussi pour une valeur vide ou non textuelle. m. 392-405 : arrêts « garde
  7 : run source hors de forme » pour les tables de [S].
- **Compatibilité.** Oui (section B).
- **Correction (mots exacts).** Remplacer la précision 14 par : « 14. Un [SF] sans `principales`, ou dont
  `principales.tromperie` ou `principales.enjeux` est absente, vide ou non textuelle, arrête au titre de la garde 7
  (« run source hors de forme »), avec un motif écrit, jamais par une exception nue (brouillon 5, CV2-10) ; de même des
  tables de [S] hors de forme (tables ou colonnes lues absentes, colonnes de longueurs différentes, table des scores mal
  formée). »

### VV3-texte-03 (forme) — Précision 2 : où est écrite la valeur ponctuelle

- **Texte.** l. 446-448 (et l. 429-430) : une part dont l'intervalle est en échec « garde sa valeur ponctuelle ».
- **Code.** m. 542-544 : la part en échec est `{"etat": "échec", "motif": …, "degeneres": …}`, sans `valeur` (le test
  v3 l. 918 l'exige : `"valeur" not in pf["part"]`) ; la valeur `D / E0` n'est écrite que dans
  `audit_symetrie_addendum2.part_hors_bornes.part` (m. 1096-1099).
- **Problème.** Le sous-agent du verdict complété peut la chercher dans le descriptif de la part et ne pas l'y trouver.
- **Correction (mots exacts).** Dans la précision 2, après « garde sa valeur ponctuelle », insérer : « (écrite dans
  `audit_symetrie_addendum2.part_hors_bornes.part` ; le descriptif de la part reste « échec », sans valeur) ».

### VV3-texte-04 (mineur) — Marqueur de durée et phrase

- **Texte.** l. 385 : « … avant le scellement : `` `<<DUREE_MESUREE>>` ``. » : le marqueur est entre accents graves.
  Remplacé seul, il mettrait la phrase entière, qui contient elle-même des accents graves, dans un bloc de code cassé. Le
  premier addendum écrit sa phrase de durée sans accents graves ([PA] l. 271-278).
- **Phrase des notes v3** (l. 225-229) : total, imports, fonction pure, mémoire justes face à `mesures-duree-v1.txt` ;
  mais « 2,0 à 2,2 s » pour `harnais.validation_reelle` élargit la plage mesurée (2,048 à 2,146 s : 2,05 à 2,15) ; le
  chemin est à remplir ; et le module mesuré est une copie du v3 dont les constantes du run réel sont réécrites pour le
  dépôt jouet (`mesure_duree_v3.py` l. 92, `_module_pour`), ce que la phrase ne dit pas.
- **Correction (mots exacts).** Remplacer `` `<<DUREE_MESUREE>>` `` (accents graves compris) par : « environ 5,5 s pour
  la ligne de commande complète (de 5,4 à 5,7 s sur quatre mesures ; processus séparé ; module cité en tête, ses
  constantes du run réel remplacées par celles du dépôt jouet, comme dans les tests ; dépôt jouet à taille réelle :
  60 tâches, 4 conditions, 10 pas, 600 actions par condition, 430 sondes, les cinq formes présentes ; 10 000 tirages ;
  machine partagée, 4 cœurs), dont 3,2 à 3,4 s d'imports (surtout la bibliothèque de calcul tensoriel, tirée par
  `harnais.validation_reelle` : 2,05 à 2,15 s) et 0,45 à 0,52 s pour la fonction pure ; mémoire maximale ≈ 683 Mio
  (≈ 717 Mo) ; mesures brutes : `prereg/contre-lectures/notes-module-v3-addendum2-P3-v1/mesures-duree-v1.txt` (sha256
  `c16ace640bd273ce073c384292771da946d2d3ec1dfee1be07b47c69115191ba`) ».
- **Contrôle des nombres** (fichier de mesures) : murale 5,399 à 5,672 s ; imports 3,223 à 3,379 s ; tensoriel 2,048 à
  2,146 s ; fonction pure 0,453 à 0,515 s ; 683,3 à 683,6 Mio = 716,5 à 716,8 Mo ; jouet de 2 400 actions, 430 sondes,
  cinq formes ; 10 000 tirages ; « 13 écrits, 9 lus, 4 sans objet » à chaque passage.

### VV3-texte-05 (forme) — Préambule des précisions d'application

- **Texte.** l. 440-441 : « Règles déjà appliquées par le module là où le texte se taisait (contre-lecture du code,
  CC-texte-06) ; aucune ne change un nombre, une réserve ni le verrou : ».
- **Problème.** La précision 2 redit l'audit, point 3 (le texte ne se taisait pas) ; elle a dû être remise dans le module
  (v3). La 14 est un comportement nouveau du v3. Les 11 à 14 viennent de CV2-08 et CV2-10, pas de CC-texte-06.
- **Correction (mots exacts).** Remplacer par : « Règles appliquées par le module v3 là où le texte se taisait ou restait
  implicite (contre-lectures du code : CC-texte-06 pour 1 à 10 ; CV2-01, CV2-07, CV2-08 et CV2-10 pour 1, 2 et 11 à
  14) ; aucune ne change un nombre, une réserve ni le verrou ; la précision 2 redit la règle de l'audit, point 3 : ».

### VV3-texte-06 (forme) — Imports des tests

- **Texte.** l. 69 : « les tests peuvent importer les aides de `tests/test_premier_test_ia_lecture.py` ».
- **Tests v3.** l. 85, 95 : `import pytest` ; `from conftest import committer, git` (`tests/conftest.py`, arbre gelé).
  Permis par « le code de l'arbre gelé au commit cité » pour `conftest`, mais non écrit ; `pytest` hors de la liste
  (CV2-09, laissé de côté par le brouillon 5).
- **Correction (mots exacts).** Remplacer par : « les tests peuvent importer `pytest`, les aides de
  `tests/test_premier_test_ia_lecture.py` et les aides `committer` et `git` de `tests/conftest.py` (arbre gelé, sans
  copie). »

### VV3-texte-07 (forme) — M5 : tirages dégénérés à 1 % au plus

- **Texte.** l. 209-210 : « un tirage où `E0(b) = 0` est dégénéré pour la part (plus de 1 % : « échec » de la part,
  motif écrit) ». Rien sur le cas à 1 % au plus.
- **Code.** m. 545-548 : l'intervalle de la part est pris sur les seuls tirages non dégénérés ; leur nombre est écrit
  (`tirages`). Lecture naturelle (`part(b)` n'existe pas quand `E0(b)` = 0), mais elle fixe un nombre écrit (descriptif).
- **Correction (mots exacts).** Après « (plus de 1 % : « échec » de la part, motif écrit », insérer : « ; à 1 % au
  plus, l'intervalle de la part est pris sur les seuls tirages non dégénérés, dont le nombre est écrit ».

## R1 et intégrité

- Rien ouvert sous `donnees/`, `diag/`, `runs/`, `traces/` du dépôt ; ni `prereg/P3-consignes-v1.md`, ni aucun fichier
  `textes-actions-*`. Aucune grandeur de B1, de B2 ni de l'addendum 2 calculée sur le réel : mes essais portent sur des
  dictionnaires et des coûts plantés à la main ; le module n'a été appelé que sur eux.
- Garde R1 des campagnes (`garde_r1_v2b.py`, copie octet pour octet, `022cfd55…0bac4f`) active pour chaque lancement
  qui importe le module ou le code gelé (outil de comparaison, essais, collecte des tests, candidat d'essai). Épreuve de
  la garde rejouée (`test_garde_r1_v2b.py`, `21dc8e56…6d7af`) : 14 passés, 17 refus attendus, tous sur des chemins
  `__garde_r1_inexistant__` qui n'existent pas, et une trace dans un dépôt jouet (`texte/journaux/r1-epreuve-garde.jsonl`).
  Sur mes autres lancements : 0 refus, 0 trace (aucun journal créé).
- Dépôt : tête `c52225b` au début, `a82dac7` à la fin (commit de la session, R-294, registres seulement) ;
  `src/`, `tests/`, `docs/procedures/` identiques entre les deux (`git diff --stat` vide). La modification de
  `registres/go.md` vue en cours de travail est celle de la session. Liste des fichiers ignorés identique après mes
  premiers lancements et à la fin ; aucun `__pycache__` ni `.pyc` dans `texte/`.
- Originaux intacts : brouillon 5, contre-lecture v2, module, tests, notes et mesures v3 ont la même empreinte au début et
  à la fin ; je n'ai travaillé que sur des copies (`texte/base/`).

## Reproductions

Depuis la racine du dépôt (sauf mention), interpréteur de la consigne, `PYTHONDONTWRITEBYTECODE=1`,
`PYTHONPATH=src:texte/outils`, `REVUE_JOURNAL_R1=<journal>` :

- comparaison : `python -B -c "import sys,runpy; import garde_r1_v2b; sys.argv=['c','texte/base/P3-addendum2-audit-verdict-v1-brouillon5.md','texte/base/audit_verdict_p3_v1.py','.']; runpy.run_path('texte/outils/comparer_texte_code_v3.py', run_name='__main__')"` ;
- essais (depuis `texte/`) : `python -B -m pytest -q -p no:cacheprovider -p garde_r1_v2b --rootdir=. --confcutdir=. outils/test_fidelite_brouillon5_v3.py` → 24 passés ;
- collecte : `python -B -m pytest --collect-only -q -p no:cacheprovider -p garde_r1_v2b texte/base/test_audit_verdict_p3_v1.py` → 121 ;
- candidat d'essai : `candidat_essai_v1.py <brouillon 5> <sortie> <module>` (même lancement que la comparaison).

## Fichiers rendus (sous `verification-v3/texte/`, chacun avec son compagnon `.sha256`)

| fichier | sha256 |
|---|---|
| `outils/comparer_texte_code_v3.py` | `de645a8824fbaa3ff7799484f77f70cf88e1b8da395255d472bee817b9bfb91e` |
| `outils/test_fidelite_brouillon5_v3.py` | `479076f29336b1ba19764deabb53dd26a2425a75b9560af388d8f5d5b65dae44` |
| `outils/candidat_essai_v1.py` | `621b018a163805e38849acecbb5ab8b5a734ef27b202362bf0fcb4812a2ce15a` |
| `outils/section-contre-lecture-code-proposee-v1.md` | `4d94c19ff30baa51066984412fed646ce3c98d4607fae6b4a5efe7cbec7e8bdc` |
| `outils/garde_r1_v2b.py`, `outils/test_garde_r1_v2b.py` (copies) | `022cfd55eac2298b9f00b371d5141d37a98561662d2f424255983199160bac4f`, `21dc8e56c0111decc26c43edca1837d2841946e49c70f0f7b058790df986d7af` |
| `candidat-essai-v1.md` | `95437d9f093027ff87fc31d4344cff36dc52b79ff990e9b3e056db1815979fed` |
| `journaux/comparer-texte-code-v3.log` | `3016bd8b910a613c17988bc07ac73865ebdc2bc9f03ebf224db1e77441987d41` |
| `journaux/comparer-texte-code-v3-artefact.log` | `5c8b8cf2289ef5b63695ff2849b9367549ea3ab3c62ffd35eda784a7482add43` |
| `journaux/pytest-essais-fidelite.log` | `a261d820f3412fe7c4b11805990e88035796003e8032016176bc9b85b3613780` |
| `journaux/pytest-essais-sur-module-v2.log` | `4652b0ac0c9edee63620ac46164937619f93c3cdb72d82d71409b074abd0989e` |
| `journaux/pytest-collecte-v3.log` | `c107e8a265ced59e1e6c0fe1729e0b644e6f46b7bdcf8ddbc2f6ce1626b001c3` |
| `journaux/masquage-entree-non-numerotee.log` | `6f7f2407c0559500b578801954d99410bb8541ff3010f227027e2c888e444dfc` |
| `journaux/candidat-essai-v1.log` | `b88e55f99250436eb978fcab3c2a4e9fb3ef6bc2667915729266f3782b625be4` |
| `journaux/diff-brouillon5-candidat-essai-v1.txt` | `abc38b2ad72d05918c8648a092f0aea4649ed6445aaec145eaa006b72ef8ed18` |
| `journaux/pytest-epreuve-garde.log`, `journaux/r1-epreuve-garde.jsonl` | `9dba01232013cdce61d4d9070a28005597cfcbbaaa3277fea41ab0f5a93f37d9`, `3fdf1c4d98420f8ba5bcd2d57aa8a0b8ed0a0fb8eebae564fa69f9d00cb07800` |
| `journaux/git-head-debut.txt`, `git-status-debut.txt`, `git-status-ignores-milieu.txt`, `git-status-ignores-fin.txt`, `debut.txt`, `fin.txt` | `945b346e…ed18`, `e3b0c442…b855`, `3d89e259…6b88`, `8474d0a1…affe`, `bee52796…33dd`, `a38c9c4e…8315` |
| `base/` : copies du brouillon 5, du module et des tests v3 | `db53d140…9a1f`, `96727076…132d`, `d0c5eb07…3b28` |
