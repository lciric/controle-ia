# Vérification mécanique du candidat 1 — addendum 2 de P3 — v1

**Verdict : scellable après corrections.** Le candidat 1 est exactement le brouillon 5, ses douze marqueurs remplis, les
corrections VV3-texte-01 à 07 et VV3-code-05 en mots exacts, la section « Contre-lecture » de la session et la ligne
« Candidat 1 » : rien d'autre. Toutes les empreintes et tous les nombres vérifiés sont justes. Les tests v4 sont les
tests v3 plus les trois fonctions proposées, sans changement de logique ; la suite passe (128, 0 refus) et chaque test
ajouté tue le mutant qu'il vise. Les corrections portent sur la ligne « Candidat 1 » et l'entrée 5 de la section
« Contre-lecture » : un script cité qui ne reproduit pas le candidat, une heure fausse, un « 0 refus » sans journal,
des comptes à préciser, un traitement des constats à écrire.

| id | gravité | constat (une ligne) |
|---|---|---|
| VC1-01 | mineur | Le script cité dans la ligne « Candidat 1 » ne produit pas le candidat : son rejeu donne `a90570ad…`, sans les cinq lignes « Candidat 1 » ; il est cité sans empreinte, par un chemin du bloc-notes qu'aucune pièce du plan ne reçoit ; sa docstring est restée celle de l'essai |
| VC1-02 | forme | Ligne « Candidat 1 » : « vers 21:45 UTC » ; le fichier est écrit à 21:21:10 UTC |
| VC1-03 | mineur | Entrée 5 : « passés sous la garde R1 (0 refus) » ne renvoie à aucun journal (R6) |
| VC1-04 | forme | Comptes : « les trois tests proposés … soit 128 tests » (trois fonctions, sept tests) ; « 24 tués, 2 équivalents » sans les six survivants |
| VC1-05 | forme | Entrée 5 : « Constats traités dans le texte (ce candidat) » ; VV3-code-01 à 03 sont traités dans les tests, VV3-code-04 par d'autres mots, VV3-code-01 point 3 (notes) n'est pas appliqué ; rien ne le dit |
| VC1-06 | information | Plan de versement du rapport « texte » : tests v3 prévus au chemin des tests exécutés (il faut les v4), tests v3 sans place ; le plan d'essai de la session (`164bb994…`) corrige les deux ; restent le script, sa section, les journaux, le candidat 1 |
| VC1-07 | information | En-tête des tests v4 : la liste « Constats … → tests » ne nomme pas VV3-code-01 à 03 (un bloc de commentaire le fait) ; aucune action avant le scellement |

Aucun constat critique ni majeur. Mes corrections, appliquées à une copie du candidat 1, s'appliquent chacune à un seul
endroit ; le résultat passe `prereg.problemes` (`[]`) et la garde 1 y lit les mêmes empreintes (section 4).

Chemins relatifs à `…/scratchpad/addendum2-p3/verification-candidat1/`, sauf mention ; `…/addendum2-p3/` est le
dossier de travail de l'addendum 2.

## Cadre

- Vérificateur : sous-agent neuf. Je n'ai écrit ni l'addendum 2 (aucun brouillon, ni le candidat), ni aucune version de
  son module ou de ses tests, ni aucune contre-lecture, vérification ou traitement antérieurs. Date : 2026-10-20, de
  21:21:57 à 21:50 UTC environ.
- Écritures : seulement sous `…/addendum2-p3/verification-candidat1/`. Les dépôts jouets des tests (`tmp/`) sont
  supprimés à la fin ; les dossiers `mutants/<id>/` restent (module muté, copie des tests, différence, journaux).
- Dépôt de travail en lecture seule. git lu sans verrou (`--no-optional-locks`). Lancements : `python -B`,
  `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`, interpréteur de la consigne. Tout lancement qui importe le module
  ou le code gelé tourne sous la garde R1 v2b. Mes outils de comparaison n'importent rien du dépôt (`python -I -B`).
- Aucune recherche récursive dans le dépôt : seulement la liste de `prereg/contre-lectures/` et de `docs/procedures/`,
  et la date des fichiers de six dossiers de cache nommés. Code gelé lu : `src/controle_ia/prereg.py` (en entier),
  `src/controle_ia/scellement.py` (l. 1-80).
- Pendant mon travail, la session a écrit `…/addendum2-p3/candidat/plan-versement-addendum2-essai-v1.json` (21:34 UTC),
  qui n'était pas dans la consigne. Je l'ai lu comme une donnée et vérifié (VC1-06). Le candidat, le script, la section
  et les tests v4 n'ont pas changé pendant mon travail.

## Pièces (empreintes recalculées ; égales à la consigne et aux compagnons, au début et à la fin)

| pièce (sous `…/addendum2-p3/`) | sha256 |
|---|---|
| brouillon 5 `P3-addendum2-audit-verdict-v1-brouillon5.md` | `db53d140d5a8d000d0d9f444a86215a9cd15e0fbdaa3f764c41facf3a5889a1f` |
| candidat 1 `candidat/P3-addendum2-audit-verdict-v1-candidat1.md` | `9900a721560c87361efcf60660863727644e8fdc3ab88e4fd1f325a613306b0e` |
| script `candidat/ecrire_candidat1_addendum2_v1.py` ; section `candidat/section-contre-lecture-code-v1.md` | `94560a3b690facfc8a68a39d34f069afba44771156387f7978fcdc7877078593` ; `c8481b12600226b1d9b1d595ad417195e03d56c9df3e6a5dd16d02c5fb993ead` |
| script d'essai `verification-v3/texte/outils/candidat_essai_v1.py` ; section proposée `…/section-contre-lecture-code-proposee-v1.md` | `621b018a163805e38849acecbb5ab8b5a734ef27b202362bf0fcb4812a2ce15a` ; `4d94c19ff30baa51066984412fed646ce3c98d4607fae6b4a5efe7cbec7e8bdc` |
| rapport « texte » `verification-v3/verification-module-v3-texte-v1.md` (en entier) | `0d947364e6475c38d39e62f5c13b70b8ad787e6d9f1907756d904da68d3f7cee` |
| rapport « code » `verification-v3/verification-module-v3-code-v1.md` (en entier) | `a705ef819376b97990cbc4d0fe9da739f13b0bcca2f511480353d99e96dee902` |
| module `module-v3/audit_verdict_p3_v1.py` = `module-v4/audit_verdict_p3_v1.py` (octet pour octet) | `967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d` |
| tests v3 `module-v3/test_audit_verdict_p3_v1.py` ; tests v4 `module-v4/test_audit_verdict_p3_v1.py` | `d0c5eb07da17a1bf27fc38905edd648e4653ba9f3652076560ee4c4c3ba83b28` ; `f9136b6dc5eebce6d9e9101fa910646b16fa544f0ee1d3a997030eb9319dbc07` |
| tests proposés `verification-v3/outils/test_garde6_lancement_propose.py` ; `…/test_extensions_proposees.py` | `4148bc5b36cc58adc8ed9c4118a289292e903569cffd1d79bfc274f4b39d6710` ; `0ddfabf4101cfef92f42c62e0f173c6f1058179bd7e58984cde6f9326a898357` |
| journaux de la suite v4 `module-v4/journaux/pytest-suite-v4-garde-r1.log` ; `r1-suite-v4.jsonl` | `cb24c899aa490bfa98e00b370c0ad388f13ddfbce6f277b21bd368a24ba12c36` ; `f2a4be52af0304831d77abeb36d78c46bb073f1a606f7eb56e3b0e3f576b3edd` |
| listes de mutants `module-v3/outils-revue/mutants_v2.py` ; `verification-v3/outils/mutants_verif_v3.py` | `d9c038e67b5e2f8cd7016c089faf02d0fd8ab86fee527d34e31304e1cfadf03c` ; `6416f5b745dfe420306224b6c5f1bb55e708e4cd422c8f9da273de38daa24da7` |
| garde R1 `module-v3/outils-revue/garde_r1_v2b.py` ; son épreuve `test_garde_r1_v2b.py` | `022cfd55eac2298b9f00b371d5141d37a98561662d2f424255983199160bac4f` ; `21dc8e56c0111decc26c43edca1837d2841946e49c70f0f7b058790df986d7af` |

Les 39 compagnons de `candidat/`, `module-v4/`, `module-v4/journaux/`, `module-v3/` (et ses journaux, outils, mesure),
`verification-v3/` et `verification-v3/texte/outils/` sont justes (`sha256sum -c`).

## 1. Brouillon 5 → candidat 1

**Différentiel brut** (`journaux/diff-brouillon5-candidat1.txt`) : neuf blocs, chacun à sa place.

| bloc (brouillon 5 → candidat) | origine |
|---|---|
| `19a20,24` | ligne « Candidat 1 » (cinq lignes) |
| `23,24c28,29` | `<<EMPREINTE_MODULE>>` (`96727076…`), `<<EMPREINTE_TESTS>>` (`f9136b6d…`, tests v4), `<<NOMBRE_TESTS>>` (`128`) |
| `69c74,75` | VV3-texte-06 |
| `210c216,217` | VV3-texte-07 |
| `385c392,400` | `` `<<DUREE_MESUREE>>` ``, accents graves compris : phrase de VV3-texte-04 avec le segment des imports de VV3-code-05 |
| `440,441c455,457` | VV3-texte-05 |
| `447c463,464` | VV3-texte-03, dans la précision 2 seulement (l'audit, point 3, garde ses mots, comme le veut la correction) |
| `468c485,488` | VV3-texte-02 |
| `581c601`, `585c605`, `587,590c607,641` | `<<SHA_TRAITEMENT_1>>`, `<<SHA_VERIFICATION_2>>`, `<<SHA_TRAITEMENT_2>>` ; entrée du code remplacée par les entrées 3 à 5 (VV3-texte-01) |

**Mots exacts** (`outils/mots_exacts_v1.py`, `journaux/mots-exacts.log`). L'outil extrait les mots de chaque correction
des deux rapports eux-mêmes (guillemets équilibrés après une ancre), normalise les espaces (un retour à la ligne dans un
paragraphe se lit comme une espace) et reconstruit le texte attendu depuis le brouillon 5. Résultat : VV3-texte-02, 03,
05, 06, 07 et la phrase de durée sont présents, une fois chacun ; **candidat = brouillon 5 + marqueurs + corrections +
section de la session + ligne « Candidat 1 » : vrai.** L'entrée du code était la fin du brouillon 5 : la coupe du script
(`t[:debut] + section`) ne perd rien.

Phrase de durée : VV3-code-05 cite comme ancien texte la phrase des notes (« 2,0 à 2,2 s ») ; VV3-texte-04 avait déjà
« 2,05 à 2,15 s ». La session a remplacé, dans la phrase de VV3-texte-04, le segment des imports par les mots nouveaux de
VV3-code-05. C'est la seule lecture qui applique les deux ; les mots sont égaux.

VV3-code-04 propose d'autres mots pour la précision 14 ; le candidat suit VV3-texte-02, comme la consigne le prévoit
(corrections VV3-texte-01 à 07 et VV3-code-05). Ce choix n'est pas écrit : VC1-05.

**Écarts avec le script d'essai du vérificateur** (`diff` des deux scripts ; et `journaux/diff-candidat-essai-candidat1.txt` :
le candidat d'essai `95437d9f…` et le candidat 1 ne diffèrent qu'en quatre blocs, ceux-ci).

| écart | justifié ? |
|---|---|
| empreinte des tests `d0c5eb07…` → `f9136b6d…` ; `121` → `128` | oui : tests v4 (VV3-code-01, point 2 : « le nombre devient « 128 » ») |
| segment des imports de la phrase de durée | oui : mots exacts de VV3-code-05 |
| section : `0…0` → `0d947364…` ; `1…1` → `a705ef81…` ; « <verdict> » → « conforme après corrections » | oui : empreintes réelles, égales aux fichiers ; verdict écrit en tête du rapport « code » |
| « mutants et pannes », `…-v1-mutants.md` → « code et mutants », `…-v1-code.md` | oui : nom de la lentille dans le titre du rapport ; nom retenu pour son versement |
| ajouts : « (30 mutants neufs … ; trois tests proposés) » et « Tests v4 : … (0 refus). » | oui sur le fond (l'en-tête cite les tests v4, l'entrée doit les expliquer) ; exacts ; mais VC1-03 et VC1-04 |
| docstring du script | non : elle garde « Usage : python -B candidat_essai_v1.py » et « fictives ici (0…0 et 1…1) » (VC1-01) |
| ligne « Candidat 1 » | prévue par la consigne ; mais ajoutée hors du script (VC1-01) |

**Rejeu du script** (`journaux/rejeu-script.log`, `journaux/diff-rejeu-candidat1.txt`). Script et section copiés dans
`rejeu/`, brouillon 5 et module dans `copies/`, garde R1 active : sortie `rejeu/candidat1-rejoue.md`
(`a90570adf78883eb5384cf32626c9562849aa63c223b1cc9c5ccf5cba7603e04`) ; `problemes` = `[]` ; garde 1 : `967270761c92…`
et `f9136b6dc5ee…`. Différence avec le candidat : les seules lignes 20-24 (VC1-01).

## 2. Empreintes et nombres cités

**Empreintes** (`journaux/empreintes-citees.log`) : chacune recalculée sur le fichier qu'elle désigne ; toutes égales.

| ligne du candidat | pièce | fichier (sous `…/addendum2-p3/`) |
|---|---|---|
| 28, 630 | module | `module-v3/` et `module-v4/audit_verdict_p3_v1.py` |
| 29, 640 | tests v4 | `module-v4/test_audit_verdict_p3_v1.py` |
| 631 | tests v3 | `module-v3/test_audit_verdict_p3_v1.py` |
| 610, 611 ; 620, 621 | module et tests v1 ; v2 | `module/` ; `module-v2/` |
| 596 ; 603 et 609 ; 622 ; 632 | brouillons 1 ; 2 ; 4 ; 5 | `P3-addendum2-audit-verdict-v1-brouillon<k>.md` |
| 599 ; 605 | contre-lecture 1 ; vérification 2 | `contre-lecture-R2-brouillon1-addendum2-P3-v1.md` ; `verification/verification-corrections-brouillon2-addendum2-P3-v1.md` |
| 601 ; 607 ; 619 | traitements | `traitement-R2-…`, `traitement-verification-brouillon2-…`, `traitement-contre-lectures-code-addendum2-P3-v1.md` |
| 614 ; 616 ; 625 | contre-lectures 3 et 4 | `revue-texte/…-texte-v1.md` ; `revue-mutants/…-mutants-v1.md` ; `revue-v2/contre-lecture-code-addendum2-v2.md` |
| 629 | notes du module v3 | `module-v3/NOTES-MODULE-v3.md` |
| 635 ; 637 | contre-lecture 5 | les deux rapports de `verification-v3/` |
| 400 | mesures de durée | `module-v3/mesures-duree-v1.txt` |
| 16 (préfixe `8c2902e4…`, depuis le brouillon 5) | contre-lecture 4 | `revue-v2/contre-lecture-code-addendum2-v2.md` |

Les autres empreintes (documents qui font foi, entrées, code gelé, l. 37-92) sont inchangées depuis le brouillon 5 et
hors de cette vérification ; plusieurs désignent des fichiers que R1 m'interdit d'ouvrir.

**Nombres.**

| nombre cité | source | état |
|---|---|---|
| 42, 118, 121, 128 tests (v1, v2, v3, v4) | collecte de pytest sous la garde : « 42 / 118 / 121 / 128 tests collected » ; en-têtes égaux (`journaux/collecte-v1-v4.log`) | = |
| entrée 1 : « scellable après corrections », treize constats (trois majeurs, sept mineurs, trois pour information) | rapport, l. 3 ; table : 3 majeurs, 7 mineurs, 3 information | = |
| entrée 2 : « scellable après corrections », douze constats (sept mineurs, cinq pour information) | rapport, l. 3-7 ; table VB2 : 7 mineurs, 5 information | = |
| entrée 3 : deux « scellable après corrections » ; 107 mutants, 66 tués, 41 survivants dont 4 équivalents | rapports, l. 3 ; rapport « mutants », l. 3-4 | = |
| entrée 4 : « scellable après corrections », CV2-01 à 04 mineurs, CV2-05 à 11 pour information ; 230, 200, 30, 5 | rapport, l. 3-21 | = |
| entrée 5 : deux « conforme après corrections » ; 30 mutants neufs, 24 tués, 2 équivalents | rapports, l. 3 ; « code », l. 17-19 | = (incomplet : VC1-04) |
| entrée 5 : « 0 refus » | journal de la session : 576 traces, 0 refus ; mon rejeu : 576, 0 | = (sans journal cité : VC1-03) |
| durée : « environ 5,5 s » ; « 5,4 à 5,7 s sur quatre mesures » | murale 5,403 ; 5,464 ; 5,399 ; 5,672 s (moyenne 5,48) | = |
| « 3,2 à 3,4 s d'imports, mesurés dans un processus qui ne fait qu'importer » | 3,279 ; 3,224 ; 3,379 ; 3,223 s, ligne « processus qui ne fait qu'importer le module » | = |
| « `harnais.validation_reelle` … : 2,05 à 2,15 s » | 2,146 ; 2,068 ; 2,105 ; 2,048 s | = |
| « 0,45 à 0,52 s pour la fonction pure » | 0,515 ; 0,453 ; 0,483 ; 0,505 s | = |
| « ≈ 683 Mio (≈ 717 Mo) » | 699 668 à 699 980 Kio = 683,3 à 683,6 Mio = 716,5 à 716,8 Mo | = |
| 60 tâches, 4 conditions, 10 pas, 600 actions par condition, 430 sondes, cinq formes ; 10 000 tirages ; 4 cœurs, machine partagée ; module cité en tête | en-tête du fichier de mesures (module `96727076…`) et lignes « tirages 10000 » | = |

## 3. Tests v4

- **Différentiel v3 → v4** (`journaux/diff-tests-v3-v4.txt`) : en-tête « Nombre de tests attendu : 121 » → « 128 » ; à la
  fin, un bloc de commentaire et trois fonctions. Rien d'autre.
- **Arbre syntaxique** (`outils/comparer_fonctions_v1.py`, `journaux/comparer-fonctions.log`) : 135 fonctions en v3, 138
  en v4 ; aucune retirée ; aucune fonction commune changée ; niveau du module (imports, constantes, fixtures) égal hors
  docstring. Les trois ajoutées ont un arbre égal à celui des fichiers proposés (`4148bc5b…` ; `0ddfabf4…`, tests 1 et
  3), décorateurs compris. Seul écart de texte : le commentaire `# noqa: F811` de la ligne `def` du test de la garde 6,
  retiré. Le rapport « code » recopie ce test avec une docstring que le fichier `4148bc5b…` n'a pas ; les tests v4
  suivent le fichier cité par empreinte. Les noms qu'utilisent les trois tests sont tous définis dans le fichier v4.
- **Suite v4**, commande de la consigne, depuis le dépôt : **`128 passed in 76.39s`**, code 0 ; R1 : 576 traces, 0 refus,
  toutes dans mes dépôts jouets (`journaux/pytest-suite-v4-garde-r1.log`, `journaux/r1-suite-v4.jsonl`). Le journal de
  la session donne aussi 128 passés et 576 traces, 0 refus. Avant usage, la garde a été éprouvée
  (`test_garde_r1_v2b.py`) : 14 passés, 17 refus attendus, tous sur des chemins `__garde_r1_inexistant__`
  (`journaux/pytest-epreuve-garde.log`).
- **Mutants** (`outils/mutants_cibles_v1.py` : listes lues comme données après vérification de leur empreinte ; copie du
  module v4 mutée et copie des tests v4 dans `mutants/<id>/` ; garde R1 active). Empreinte de chaque mutant égale à celle
  de la contre-lecture 5. Trois tests ajoutés seuls (`-k`), puis suite entière pour les mutants visés :

| mutant | règle mutée | trois tests ajoutés (7 tests) | suite v4 entière (128) | suite v3 (contre-lecture 5) |
|---|---|---|---|---|
| aucun (cas sain) | — | 7 passés | 128 passés | 121 passés |
| G6-02 | chargeur gelé appelé au lancement | tué : garde 6 au lancement | tué : CV2-10 et garde 6 au lancement | tué : CV2-10 seul |
| VV-G6-02 | repli sur le chargeur gelé après un arrêt | tué : garde 6 au lancement | tué : garde 6 au lancement seul | survit |
| VV-F-01 | `cout_milliers_espace` non comparé | tué : `[cout_milliers_espace]` | tué : ce paramètre seul | survit |
| VV-F-02 | `cout_multiplication` non comparé | tué : `[cout_multiplication]` | tué : ce paramètre seul | survit |
| VV-D3-04 | « `E0` = 0 » avec une tolérance | tué : déclencheur 3, `E0` petit | tué : ce test seul | survit |
| VV-G6-01 | équivalent voulu (alias) | 7 passés : le test sépare le comportement, pas la route | — | tué par la route (CV2-10) |
| G6-01 | exceptions du chargeur non converties | tué : garde 6 au lancement | — | tué |

Journaux : `journaux/mutants-cibles-nouveaux.jsonl`, `journaux/mutants-cibles-suite.jsonl` ; R1 sur ces 13 lancements :
3 248 traces, 0 refus, toutes dans mes dépôts jouets (`journaux/r1-mutants-bilan.log`).

## 4. `prereg.problemes`, garde 1, section « Contre-lecture »

Sur le fichier candidat lui-même (copie octet pour octet, `9900a721…`), garde R1 active
(`journaux/point4-problemes-garde1.log`) :

- `problemes` = `[]` ; les huit sections exigées présentes ;
- garde 1 : `EMPREINTE_MODULE_CITEE.findall` rend une seule empreinte, `967270761c92…132d` (module v3 = v4) ;
  `EMPREINTE_TESTS_CITEE.findall` une seule, `f9136b6dc5ee…dbc07` (tests v4). La garde prend la première par `search` :
  aucune ambiguïté ;
- section « Contre-lecture » : cinq entrées numérotées, 1 à 5 ; empreintes distinctes par entrée : 3, 3, 6, 5, 6 ; aucun
  texte hors des entrées ; aucun marqueur restant (`<<…>>`, « À REMPLIR », « <verdict> », « <empreinte »).

Essai de mes corrections (`outils/corrections_essai_v1.py`, `essai/candidat1-corrige-essai.md`, `c6505ff5…`, qui n'est pas
un candidat à verser) : chaque motif trouvé une seule fois (espaces souples) ; `problemes` = `[]` ; garde 1 : mêmes
empreintes (`journaux/corrections-essai.log`).

## 5. Plan de versement

Section D (et C) du rapport « texte » face aux chemins et empreintes du candidat :

| cité dans le candidat | pièce prévue | état |
|---|---|---|
| `prereg/contre-lectures/contre-lecture-R2-brouillon1-addendum2-P3-v1.md`, `traitement-R2-…`, `verification-corrections-brouillon2-…`, `traitement-verification-brouillon2-…`, `contre-lecture-code-b2-1-…`, `contre-lecture-code-b2-2-…`, `traitement-contre-lectures-code-…`, `contre-lecture-code-b4-…`, `notes-module-v3-addendum2-P3-v1.md`, `notes-module-v3-addendum2-P3-v1/mesures-duree-v1.txt`, `verification-code-final-addendum2-P3-v1-texte.md` | une ligne chacun, même empreinte | = |
| `prereg/contre-lectures/verification-code-final-addendum2-P3-v1-code.md` | ligne « …-v1-mutants.md (une ligne de plus par autre lentille, même forme) » | = avec le nom retenu (`a705ef81…`) |
| brouillons 1, 2, 4, 5 ; module et tests v1, v2 (empreintes seules) | `brouillons-addendum2-P3-v1/`, `versions-relues-addendum2-P3-v1/` | = |
| module cité en tête | section C : `docs/procedures/P3-addendum2-v1/audit_verdict_p3_v1.py` | = |
| tests cités en tête (v4, `f9136b6d…`) | section C : tests **v3** à `docs/procedures/P3-addendum2-v1/test_audit_verdict_p3_v1.py` | écart (VC1-06) |
| tests v3 (`d0c5eb07…`, entrée 5, empreinte seule) | aucune | écart (VC1-06) |
| script `…/addendum2-p3/candidat/ecrire_candidat1_addendum2_v1.py` (l. 24) | aucune | écart (VC1-01) |
| journal du « 0 refus » | aucun chemin cité | VC1-03 |
| `…/addendum2-p3/revue-v2/contre-lecture-code-addendum2-v2.md` (l. 16, depuis le brouillon 5) | `contre-lecture-code-b4-addendum2-P3-v1.md`, même empreinte `8c2902e4…` | chemin du bloc-notes, reconnaissable par l'empreinte (VC1-06) |

Aucun nom prévu n'existe déjà dans le dépôt (`prereg/contre-lectures/` n'a aucun nom « addendum2 » ; `docs/procedures/`
n'a pas `P3-addendum2-v1/`).

## Constats détaillés

### VC1-01 (mineur) — Le script cité ne produit pas le candidat

- **Texte.** Ligne « Candidat 1 », l. 23-24 : « … ; module inchangé ; script
  `…/addendum2-p3/candidat/ecrire_candidat1_addendum2_v1.py` ; … ».
- **Preuve.** Rejeu du script (`94560a3b…`) sur une copie du brouillon 5, garde R1 active : sortie
  `a90570adf78883eb5384cf32626c9562849aa63c223b1cc9c5ccf5cba7603e04`, différente du candidat `9900a721…`. Seule
  différence : les lignes 20-24 du candidat (`journaux/diff-rejeu-candidat1.txt`). Le script n'écrit pas la ligne
  « Candidat 1 » ; elle a été ajoutée ensuite. Le script est cité sans empreinte, par un chemin du bloc-notes ; ni la
  section D du rapport « texte » ni le plan d'essai de la session ne versent le script ni sa section (`c8481b12…`). Sa
  docstring est restée celle de l'essai : « Usage : python -B candidat_essai_v1.py … » et « Les empreintes des deux
  rapports de la contre-lecture 5 sont fictives ici (0…0 et 1…1). », faux pour ce script.
- **Portée.** Aucune sur une règle, un nombre ou une garde : le texte entier s'explique par le différentiel (section 1).
  Mais le texte scellé citerait une provenance qui ne se rejoue pas, par un chemin qui n'existera pas dans le dépôt.
- **Correction (mots exacts).**
  1. Dans la ligne « Candidat 1 », remplacer « script `…/addendum2-p3/candidat/ecrire_candidat1_addendum2_v1.py` » par
     « script `prereg/contre-lectures/brouillons-addendum2-P3-v1/ecrire_candidat1_addendum2_v1.py` (sha256
     `94560a3b690facfc8a68a39d34f069afba44771156387f7978fcdc7877078593`), qui écrit tout le candidat 1 sauf cette ligne,
     ajoutée ensuite ».
  2. Verser ce script et sa section `section-contre-lecture-code-v1.md` sous
     `prereg/contre-lectures/brouillons-addendum2-P3-v1/`, mêmes noms (leurs compagnons ne citent que le nom de base).
  3. Pour le candidat suivant : un script de nouveau nom (R12), dont la docstring dit ce qu'il fait (ni
     « candidat_essai_v1.py », ni « fictives ici (0…0 et 1…1) »), qui écrit le texte entier, lignes d'en-tête comprises
     (lues d'un fichier à côté, comme la section) ; vérifier que son rejeu redonne le candidat octet pour octet ; le
     citer par son chemin versé et son empreinte, et le verser de même.

### VC1-02 (forme) — Heure de la ligne « Candidat 1 »

- **Texte.** l. 20 : « Candidat 1 : écrit par la session 14 (2026-10-20 vers 21:45 UTC) ».
- **Preuve.** Le candidat est écrit à 21:21:10 UTC (son compagnon aussi ; le script à 21:20:32). Mon travail commence à
  21:21:57 UTC : 21:45 n'était pas encore venu. Les lignes des brouillons 3, 4 et 5 donnent, à deux minutes près,
  l'heure de leur fichier (10:52, 11:54, 16:56).
- **Correction (mots exacts).** Remplacer « (2026-10-20 vers 21:45 UTC) » par « (2026-10-20 vers 21:21 UTC) ».

### VC1-03 (mineur) — « 0 refus » sans journal (R6)

- **Texte.** Entrée 5, l. 640 : « … soit 128 tests (sha256 `f9136b6d…`), passés sous la garde R1 (0 refus). ».
- **Preuve.** Aucun chemin ni aucune empreinte ne porte ce nombre. Il est juste : `module-v4/journaux/pytest-suite-v4-garde-r1.log`
  (`cb24c899…` : « 128 passed », code 0) et `module-v4/journaux/r1-suite-v4.jsonl` (`f2a4be52…` : 576 traces, 0 refus) ;
  mon rejeu donne les mêmes nombres. Précédent : CV2-04 (phrase de durée sans chemin ni empreinte), classé mineur.
- **Correction (mots exacts).**
  1. Dans l'entrée 5, remplacer « passés sous la garde R1 (0 refus). » par « passés sous la garde R1 (128 passés,
     0 refus ; journaux `prereg/contre-lectures/tests-v4-addendum2-P3-v1/pytest-suite-v4-garde-r1.log`, sha256
     `cb24c899aa490bfa98e00b370c0ad388f13ddfbce6f277b21bd368a24ba12c36`, et
     `prereg/contre-lectures/tests-v4-addendum2-P3-v1/r1-suite-v4.jsonl`, sha256
     `f2a4be52af0304831d77abeb36d78c46bb073f1a606f7eb56e3b0e3f576b3edd`). » ; verser ces deux fichiers à ces chemins
     (sources `…/addendum2-p3/module-v4/journaux/`, compagnons valables).
  2. Recommandé, pour que le texte scellé cite la relecture des trois tests ajoutés par un sous-agent qui ne les a pas
     écrits (R2) : ajouter après l'entrée 5 « - **Contre-lecture 6** — vérification mécanique du candidat 1 (sha256
     `9900a721560c87361efcf60660863727644e8fdc3ab88e4fd1f325a613306b0e`) et des tests v4 (sha256
     `f9136b6dc5eebce6d9e9101fa910646b16fa544f0ee1d3a997030eb9319dbc07`) par un sous-agent neuf, qui n'a écrit ni le
     texte, ni aucune version du module ou de ses tests, ni aucune contre-lecture antérieure : rapport
     `prereg/contre-lectures/verification-candidat1-addendum2-P3-v1.md` (sha256 `<empreinte de ce rapport>`), « scellable
     après corrections » ; suite v4 relancée sous la garde R1 (128 passés, 0 refus) ; chaque test ajouté tue le mutant
     qu'il vise. Constats VC1-01 à VC1-05 traités dans ce candidat. » ; remplir `<empreinte de ce rapport>` par
     l'empreinte de son compagnon ; verser ce rapport à ce chemin.

### VC1-04 (forme) — Comptes de la ligne « Candidat 1 » et de l'entrée 5

- **Texte.** l. 22-23 : « les trois tests proposés et éprouvés par la lentille « code » (VV3-code-01 à 03), ajoutés sans
  changement (128 tests) » ; l. 637-639 : « (30 mutants neufs sur les points changés, 24 tués, 2 équivalents ; trois
  tests proposés). Tests v4 : les 121 tests relus et les trois tests proposés … soit 128 tests ».
- **Preuve.** 121 + 3 ≠ 128 : ce sont trois fonctions, dont celle de la garde 7, paramétrée sur les cinq formes ; la
  collecte passe de 121 à 128, soit sept tests de plus (« un test paramétré compte une fois par jeu de paramètres »,
  en-tête des tests). Le rapport « code » écrit « 24 tués et 6 survivants. Parmi ces 6, deux sont équivalents » ; les
  entrées 3 et 4 écrivent « N survivants dont k équivalents ». Les quatre autres survivants (VV-G6-02, VV-F-01, VV-F-02,
  VV-D3-04) sont tués par la suite v4 (section 3).
- **Correction (mots exacts ; espaces normalisés).**
  1. Ligne « Candidat 1 » : remplacer « les trois tests proposés et éprouvés par la lentille « code » (VV3-code-01 à 03),
     ajoutés sans changement (128 tests) » par « les trois fonctions de test proposées et éprouvées par la lentille
     « code » (VV3-code-01 à 03), ajoutées sans changement (7 tests de plus, 128 en tout) ».
  2. Entrée 5 : remplacer « (30 mutants neufs sur les points changés, 24 tués, 2 équivalents ; trois tests proposés).
     Tests v4 : les 121 tests relus et les trois tests proposés et éprouvés par la lentille « code » (VV3-code-01 à 03),
     ajoutés sans changement, soit 128 tests » par « (30 mutants neufs sur les points changés : 24 tués, 6 survivants
     dont 2 équivalents ; les 4 autres, VV-G6-02, VV-F-01, VV-F-02 et VV-D3-04, sont tués par les trois fonctions de test
     proposées). Tests v4 : les 121 tests relus et les trois fonctions de test proposées et éprouvées par la lentille
     « code » (VV3-code-01 à 03), ajoutées sans changement, soit 7 tests de plus (le test de la garde 7 compte une fois
     par forme) et 128 tests ».

### VC1-05 (forme) — Traitement des constats de la contre-lecture 5

- **Texte.** Entrée 5, l. 640-641 : « Constats traités dans le texte (ce candidat) ; le module relu est le module cité en
  tête. »
- **Faits.** VV3-texte-01 à 07 et VV3-code-05 : dans le texte (section 1). VV3-code-01 à 03 : dans les tests
  (section 3). VV3-code-04 : ses mots pour la précision 14 ne sont pas repris ; la précision 14 suit VV3-texte-02, qui
  nomme aussi la garde 7 et les valeurs vides ou non textuelles ; son test facultatif n'est pas ajouté. VV3-code-01,
  point 3 (remplacer une phrase des notes) : non appliqué ; les notes citées restent `7283bc51…` (v3). Aucun de ces choix
  n'est écrit.
- **Correction (mots exacts).** Remplacer « Constats traités dans le texte (ce candidat) ; le module relu est le module
  cité en tête. » par « Constats traités : VV3-texte-01 à 07 et VV3-code-05 dans le texte (ce candidat) ; VV3-code-01 à
  03 par les trois fonctions de test ; VV3-code-04 par les mots de VV3-texte-02 (précision 14), sans le test facultatif ;
  VV3-code-01, point 3 (notes) : notes v3 laissées telles quelles, G6-02 étant désormais tué par
  `test_garde_6_au_lancement_exception_du_chargeur_convertie` ; le module relu est le module cité en tête. »

### VC1-06 (information) — Plan de versement

- La section D du rapport « texte » couvre tous les chemins `prereg/contre-lectures/…` du candidat, la ligne
  « …-v1-mutants.md » lue « …-v1-code.md » (nom retenu).
- La section C (« tests v3 … versés tels quels sous `docs/procedures/P3-addendum2-v1/test_audit_verdict_p3_v1.py` ») est
  dépassée : l'en-tête cite les tests v4, et la garde 1 compare les tests de ce chemin à l'empreinte citée ; avec les v3,
  elle arrêterait : « garde 1 : tests d'empreinte d0c5eb07da17 ≠ empreinte citée f9136b6dc5ee ». Les tests v3, cités par
  leur seule empreinte dans l'entrée 5, n'ont alors pas de place prévue.
- Le plan d'essai de la session `…/addendum2-p3/candidat/plan-versement-addendum2-essai-v1.json`
  (`164bb9945484f2f4c80d6c73e23bf806b352cf1415cbfa9e5f863b8ebb12a6a4`) corrige les deux (tests v4 à
  `docs/procedures/…` ; tests v3 à `versions-relues-addendum2-P3-v1/test_audit_verdict_p3_v1-d0c5eb07.py`) et nomme le
  rapport « code » `…-v1-code.md`. Ses 26 lignes : empreinte de la source égale à celle écrite ; destinations uniques,
  absentes du dépôt (`journaux/plan-versement-essai-verifie.log`).
- À y ajouter : le script et sa section (VC1-01) ; les deux journaux (VC1-03) ; ce rapport, si l'entrée 6 est écrite ;
  le candidat 1, si un candidat 2 le remplace (R12) :
  `prereg/contre-lectures/brouillons-addendum2-P3-v1/P3-addendum2-audit-verdict-v1-candidat1.md`.
- La l. 16 (depuis le brouillon 5) cite `…/addendum2-p3/revue-v2/contre-lecture-code-addendum2-v2.md`, chemin du
  bloc-notes ; la pièce est prévue sous `contre-lecture-code-b4-addendum2-P3-v1.md`, reconnaissable par son empreinte
  `8c2902e4…`. Aucune action nécessaire.

### VC1-07 (information) — En-tête des tests v4

- La docstring des tests rattache les constats aux tests (« Constats des contre-lectures du code … → tests »,
  « Constats de la contre-lecture du module v2 … → tests ») ; elle ne nomme pas VV3-code-01 à 03. Le bloc de commentaire
  placé avant les trois tests le fait, avec ses sources et leurs empreintes.
- Aucune action avant le scellement : la consigne ne demandait que le nombre en tête, et changer la docstring changerait
  l'empreinte citée. Une version future des tests pourra ajouter la ligne.

## R1 et intégrité

- Rien ouvert sous `donnees/`, `diag/`, `runs/`, `traces/` du dépôt ; ni `prereg/P3-consignes-v1.md`, ni aucun fichier
  `textes-actions-*`. Aucune grandeur de B1 ni de B2 calculée sur les données réelles : seuls des dépôts jouets et des
  tables synthétiques, construits par les tests ; le module n'a été appelé que sur eux. Aucun réseau, aucune commande
  Vast.ai.
- Garde R1 v2b (copie octet pour octet, `022cfd55…`) active pour chaque lancement qui importe le module ou le code gelé :
  rejeu du script, suite v4, mutants, collectes, point 4, essai des corrections. Épreuve : 14 passés, 17 refus attendus,
  1 trace dans un dépôt jouet. Suite v4 : 576 traces, 0 refus. Mutants : 13 journaux, 3 248 traces, 0 refus. Rejeu,
  collectes, point 4, essai : aucun journal créé (0 refus, 0 trace). Toutes les traces sont dans mes dépôts jouets.
- Dépôt : tête `98a95de` au début et à la fin ; `git status --porcelain` vide aux deux bouts ; liste des fichiers ignorés
  égale à celle relevée par la vérification « texte » ; aucun fichier compilé écrit (les plus récents des six dossiers de
  cache regardés datent du 19 octobre). Aucun cache dans les dossiers d'origine de `…/addendum2-p3/`.
- Originaux intacts : les vingt fichiers du tableau « Pièces » ont la même empreinte au début et à la fin ; je n'ai
  travaillé que sur des copies (`copies/`, `rejeu/`, `mutants/<id>/`).

## Reproductions

Depuis la racine du dépôt, interpréteur de la consigne, `PYTHONDONTWRITEBYTECODE=1`, `REVUE_JOURNAL_R1=<journal>`,
`TMPDIR=<dossier>` :

- suite v4 : `PYTHONPATH=src:…/addendum2-p3/module-v3/outils-revue python -B -m pytest -q -p no:cacheprovider -p garde_r1_v2b --basetemp=<dossier>/base …/addendum2-p3/module-v4/test_audit_verdict_p3_v1.py` → 128 passés ;
- rejeu du script : `PYTHONPATH=src:outils python -B -c "import sys,runpy; import garde_r1_v2b; sys.argv=['rejeu/ecrire_candidat1_addendum2_v1.py','copies/P3-addendum2-audit-verdict-v1-brouillon5.md','<sortie>','copies/audit_verdict_p3_v1.py']; runpy.run_path(sys.argv[0], run_name='__main__')"` (chemins absolus) ;
- mutants (depuis n'importe où) : `python -I -B outils/mutants_cibles_v1.py nouveaux BASE G6-01 G6-02 VV-G6-01 VV-G6-02 VV-F-01 VV-F-02 VV-D3-04`, puis `… suite G6-02 VV-G6-02 VV-F-01 VV-F-02 VV-D3-04` ;
- mots exacts : `python -I -B outils/mots_exacts_v1.py <brouillon 5> <candidat> <rapport texte> <rapport code> <section proposée> <section de la session>` ;
- tests ajoutés : `python -I -B outils/comparer_fonctions_v1.py <tests v3> <tests v4> <test garde 6 proposé> <extensions proposées>`.

## Fichiers rendus (chacun avec son compagnon `.sha256`)

| fichier | sha256 |
|---|---|
| `outils/mots_exacts_v1.py` | `375284eb4e8c27b0fed806f38dff7a3b2808fac94336b14ebbd01fab6b013cd3` |
| `outils/comparer_fonctions_v1.py` | `19235312966c34ecdd6fd077669072248885890a710636cd2375ab7c02e9fcad` |
| `outils/mutants_cibles_v1.py` | `b78c4ce6fc0d01d701262140fe2d71f14f467f7869f437c6b1d972705a097c25` |
| `outils/corrections_essai_v1.py` | `0f82ce1b3f0c162ad10cff5682adfd54511fbf3348209cecf427d8bb1de45087` |
| `outils/garde_r1_v2b.py` (copie) | `022cfd55eac2298b9f00b371d5141d37a98561662d2f424255983199160bac4f` |
| `rejeu/candidat1-rejoue.md` | `a90570adf78883eb5384cf32626c9562849aa63c223b1cc9c5ccf5cba7603e04` |
| `essai/candidat1-corrige-essai.md` (essai, pas un candidat) | `c6505ff501d41b59480b356cc142effb1498d2bbaa011c0b44b99bafc9e5f021` |
| `journaux/diff-brouillon5-candidat1.txt` | `595ac67f5bed34ec58e62ca76badbcf8b4d681bf765eb7b657ea1f2d4539fcf5` |
| `journaux/diff-rejeu-candidat1.txt` ; `journaux/rejeu-script.log` | `0edc0ebcd030c41d24ed9460add680329353bc34d12f3c4fc70a05e8726bc80c` ; `cd564bda915a131a181f51d51d1ea11946bd66c8e1325bcead48fea4c51ec287` |
| `journaux/diff-section-proposee-session.txt` ; `journaux/diff-candidat-essai-candidat1.txt` | `36964d8b9501a97a29647525b3c48aa0f6767b9a601bf57fa72131aa152f2909` ; `392a246127fcad5248d4dff5b2816e4614cead40a8fbd6b5e9b4d7ff0bd4ffd4` |
| `journaux/mots-exacts.log` | `9135ed543cc649c9102b885c2255cc6aff38b94316d709aff24caeb67a111a38` |
| `journaux/empreintes-citees.log` ; `journaux/collecte-v1-v4.log` | `0d77622a19fefbf01b826e789826f05f66e360af6586c2dc9bb89d8bfac16602` ; `2b2725123527f9ad8f47bfe6e577ac796a5e4f916f0955bc308a67822417559a` |
| `journaux/diff-tests-v3-v4.txt` ; `journaux/comparer-fonctions.log` | `8af4c352335a7f01147c86eb7295678da3b804bc9199f9bf1f1e1555b30078ce` ; `3118513a9bccd0fefab9128c07dbb1e6b4793f60a37c8ad0277e6917eb7b2745` |
| `journaux/pytest-suite-v4-garde-r1.log` ; `journaux/r1-suite-v4.jsonl` | `9c2dc6163323a79104eb2cf4df69a25f0e9dbd0f642aa4c101a32eb4e96bd65b` ; `1e434a858f8677b4bc1efdae2cdda6526db63bbedf05e3b8ce20f02ed0cee848` |
| `journaux/pytest-epreuve-garde.log` ; `journaux/r1-epreuve-garde.jsonl` | `304f651641adb88aec5b43e22005d00449cf2738ebc9837973a2a6e9a4c26b46` ; `f6162889dfc8d52e5b7dc1a6291573d1d29ae0b327d2f4263dd83a4cde1953f9` |
| `journaux/mutants-cibles-nouveaux.jsonl` ; `journaux/mutants-cibles-suite.jsonl` ; `journaux/r1-mutants-bilan.log` | `f70c33c98037824ef01281ae65d42ecd29918729b1fd8a50c4c47988c4fb92c8` ; `7975f62894615b930bc4b386da814f2459b380761552f6ed18fc6c964059a5fa` ; `e74b49567e2c519dcc53a0812e455528706eb39bbde993ce49ff706c95ef8aca` |
| `journaux/point4-problemes-garde1.log` ; `journaux/corrections-essai.log` | `1bfa5becf3962aee0bb0b98b4798f11af54948df4023fb1284a04cedb07a1640` ; `edc6b076dc6c9bcdce00859f7f3a04ae91664a42598481945f0b3fb9739e073e` |
| `journaux/plan-versement-essai-verifie.log` | `15e36dbc02c4e9322b9a24d6118a78b64c23c555cd35d90df5da297f4b42e889` |
| `journaux/git-head-debut.txt`, `…-fin.txt` ; `git-status-debut.txt`, `…-fin.txt` (vides) ; `git-status-ignores-fin.txt` ; `debut.txt` ; `fin.txt` | `e3194cbc…9a83` ; `e3b0c442…b855` ; `8474d0a1…affe` ; `97e9d5a7…103e` ; `c9d385cc…6bf9` |
| `copies/` : brouillon 5, module, candidat 1, plan d'essai de la session | `db53d140…9a1f`, `96727076…132d`, `9900a721…6b0e`, `164bb994…a6a4` |
