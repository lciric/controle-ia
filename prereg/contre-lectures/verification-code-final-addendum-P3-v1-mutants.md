# Vérification finale du module de l'addendum de P3 — angle « mutants et pannes » (VF2)

**Verdict : scellable après corrections.** Le module final est juste sur chaque règle mutée. Les 51 mutants de la revue
CB2 sont tués, chacun par le test que les notes de correction annoncent. Sur mes 39 mutants neufs, 31 sont tués et 8
survivent à la suite complète. Les survivants ne montrent aucun défaut du module : la copie de base arrête sur chaque
artefact qui les révèle. Ils montrent des trous dans les tests. Pour trois règles neuves, ce sont des manques à R5 : une
moitié des recoupements de la précision 18, le cas sain des drapeaux non consultés, la ligne d'espaces de la garde 14
(VF2-01, VF2-02, VF2-04). La précision 17 dit moins que ce que fait le code (VF2-03). Les pannes tiennent : même sortie
octet pour octet entre processus et entre dépôts, aucun texte d'action dans la sortie, U+2028, U+2029 et U+0085 dans les
textes (champ du coût compris) sans arrêt ni désalignement. Les corrections portent sur les **tests** et sur **une
phrase du texte**. Le module ne change pas : son empreinte reste `2b16179d…`.

- Relecteur : sous-agent neuf (R2). Je n'ai écrit ni le texte, ni le module, ni ses tests, ni les corrections.
  Date : 2026-10-20 (UTC), de 05:04 à 07:12.
- Seuls dossier et fichier écrits : `addendum-p3/verification-finale/mutants/` et ce rapport. Dépôt de travail en
  lecture seule. Aucun résultat de P3 lu : rien sous `runs/`, `diag/`, `donnees/` ni `traces/` du dépôt.
- Tous les lancements : `python -B`, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`, `--basetemp` et `TMPDIR` dans
  mon dossier. Jamais plus de deux processus à moi en même temps.
- Original intact : empreintes du module, des tests, des notes et du texte égales au début (05:04) et à la fin (07:09, contrôlées encore à 07:11)
  (`mutants/empreintes-original-debut.txt`, `mutants/empreintes-original-fin.txt`). Aucun fichier de `final-b4/`
  modifié ni créé. Aucun cache.

## Ce qui a été lu

| fichier | sha256 |
|---|---|
| texte qui fait foi : `addendum-p3/P3-addendum-lecture-complementaire-v1-brouillon6.md` (lu en entier) | `411eb3344b153cc81f118aad3dab5781934f60c1f9dc22efdf3f2ef2f5338a1a` |
| brouillon 3 (différentiel avec le brouillon 6) | `30a99398313dc3752d4b0eca0c75335103b58b81b23d48cee07e854ff66b130b` |
| module final `final-b4/complements_p3_v1.py` (lu en entier, 2 289 lignes) | `2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996` |
| tests `final-b4/test_complements_p3_v1.py` (165 tests ; lus en partie : aides, verrou, gardes 4, 5, 7, 9, 12 à 16, synthèse, bout en bout) | `7605c2051e853d9707e59a13ccc26a5b99678f3efb67748f00d710c4336f8f0d` |
| notes `final-b4/NOTES-CORRECTIONS-CB1.md` (lues en entier) | `d2e5d4e65793721455092468f54a6a40241498ef7d4249f36b0a706d4201a096` |
| CB1 `rapports/contre-lecture-code-b3-1.md` | `89e1f02b41d62ee7388955d0c23bfbb8b54f2f9e2ea3fa299758f17c0b58e57f` |
| CB3 `rapports/contre-lecture-code-b3-3.md` | `8aa42a89beb16079da2bbc4d3fc903ada726600a4dcc9be36e3dac5927501605` |
| CB2 : liste des 51 mutants `rapports/revue-b3-2/mutants_b3_2.py`, chargée sans copie, empreinte vérifiée au lancement | `b5b7a3fa77291b31604945f1705a427d3803a585fb627000858a5f53328e58bb` |
| CB2 : `rapport-gabarit.md` | `15732375cccdaeea19189d2508ef1dba5b46b80e9bfc6f1fd23b92e11c04feec` |
| CB2 : `mutants-resultats.jsonl` | `7abac18d7ad31bbefe50b2e9d202951ec6d8432ae5bc4635291a7051a52d3854` |
| traitement `traitement-R2-addendum-P3-v1.md` (sections GB6, « Code », Gemini 007) | `0d39c03ca759b02bcfc29a5881562a6de94e42fe3e22521a2676636306bdb6b3` |
| code gelé consulté : `environnements/propositions.py` (l. 100-175), `premier_test_ia/conditions.py` (l. 38-150), `premier_test_ia/lecture.py` (règles d'établissement), `sondes/evaluation.py` (l. 98), `sondes/temoins.py` (l. 207), `manifeste.py` (`ecrire_resultat`) | `5d97b223…`, `dda64117…`, `ab7c21cb…`, `1040674c…`, `3b051b6f…`, `1a5c7464…` |
| aides importées par les tests : `tests/test_premier_test_ia_lecture.py`, `tests/conftest.py` | `6d3969c0…`, `a1bbfcc9…` |

Empreintes complètes : `mutants/empreintes-lues.txt` ; preuves de cette revue : `mutants/empreintes-preuves.txt`.

## Ce qui a été lancé (comptes)

| quoi | résultat | journal |
|---|---|---|
| copie de base `mutants/base/` (module et tests, octet pour octet) | empreintes égales à l'original | `mutants/empreintes-original-debut.txt` |
| suite complète sur la copie non mutée | **165 passed in 1047.34 s** | `mutants/base-complete/pytest-suite.log` |
| témoin : les 40 tests tueurs (union), copie non mutée | **40 passed in 233.93 s** | `mutants/temoin/pytest-tueurs.log` |
| mutants : 51 de CB2 et 39 neufs, soit **90** ; motifs vérifiés présents une seule fois avant tout lancement | 82 tués, 8 survivants (table) | `mutants/resultats-vf2.jsonl`, `mutants/m/<id>/pytest-*.log` |
| test tueur d'abord (90 lancés), puis suite complète `-x` s'il passe | **9 suites complètes** : 8 passent (survivants), 1 échoue (M15) | idem |
| pannes P1 à P3 (`pannes/test_pannes_vf2.py`, 4 tests, dont un lancement réel dans trois dépôts jetables) | **4 passed in 73.97 s** | `pannes/pytest-pannes.log` |
| P1, fonction pure, deux processus (`PYTHONHASHSEED` 0 et 4242), sept scénarios des tests | 7 × 2 empreintes identiques | `pannes/determinisme.log` |
| P1 aux tirages du texte (2 000 et 10 000), deux processus (`PYTHONHASHSEED` 1 et 777) | empreintes identiques | `pannes/determinisme-complet.log` |
| reproductions : `essais/essai_precision17.py`, `essais/essai_survivants.py` (base, M09 à M12), `essais/essai_survivants_2.py` (base, M13, M14, M15, M19, M24) | voir constats | `essais/*.log` |

Lanceurs : `mutants/lanceur_vf2.py` (liste, vérification des motifs, témoin, lancement) et `mutants/lanceur2_vf2.py`
(même procédure, deux à la fois, réservation exclusive : aucun mutant lancé deux fois, aucun doublon dans les résultats).
Pour passer à deux processus, j'ai arrêté le premier lanceur par identifiant de processus (R10) : lanceur 29339, puis son
pytest 1230. M09 était alors en suite complète ; il a été relancé en entier. Consigné dans `mutants/arrets-vf2.txt`.

Définitions : « tué » = le test tueur échoue (code 1 de pytest) ; « tué (suite complète) » = le test tueur passe et la
suite complète échoue ; « SURVIT » = la suite complète passe (165 tests). J'ai relu le journal de chaque mort : l'échec
porte sur la règle mutée (assertion, garde non levée, ou motif de garde). Les cas particuliers sont en VF2-07.

Motifs adaptés au code final, même règle mutée (les 48 autres tels quels) :
- V1 : `if c["controle_contraire"] != SANS_OBJET and c["cible"] not in recalculees:` → `if False:` ;
- V2 : `exiger_verrou(sortie, lecture, etablies, principales, issue_canonique)` → `exiger_verrou(sortie, lecture,
  cibles_possibles(principales), principales, issue_canonique)` ;
- V3 : `if r["cible"] not in recalculees:` → `if False:`.
Ce sont les mêmes adaptations que celles des notes (§ 5).

Mutants neufs : 39, sur les règles neuves demandées. Précisions 16 à 18 : M01 à M12. Gardes 12 à 16 : M13 à M28, dont
le découpage des textes sur le seul saut de ligne (M18 à M20). Recommandation en deux listes : M29 à M33. Audit de
symétrie sur les seuls contrôles contraires : M34 à M39.

## Constats (le plus grave d'abord)

### VF2-01 — mineur — Précision 18 : deux recoupements à deux conditions n'ont d'artefact que pour une condition ; la borne stricte des contrastes n'est pas épinglée

- **Où** : module l. 509-510 (T3), l. 516-519 (`bas > seuil` pour T1, T2, T4), l. 537-541 (`conforme`) ; test
  `test_garde_7_drapeaux_bruts_recoupes_avec_les_etats` (tests l. 1745-1775).
- **Problème** : R5 exige un cas sain et un artefact pour chaque garde. Le test éprouve un `conforme` forgé par la seule
  condition « saboteur contre témoin ». Il éprouve T3 dans le seul sens « drapeau faux, états vrais ». Trois mutants
  passent les 165 tests :
  - M09 : `conforme` recoupé sans « témoin contre honnête non au-dessus » ;
  - M10 : T3 recoupé sans « saboteur contre mention au-dessus » ;
  - M12 : `bas ≥ seuil` au lieu de `bas > seuil` pour T1, T2 et T4 (`lecture.py` : `bas > seuil`, strict). La même
    frontière est épinglée pour P3-P1 : M08 est tué.
  Avec M09 ou M10, une lecture dont le drapeau brut dit `conforme` (ou T3 établi) alors que ses états disent le contraire
  passerait la garde 7. P3-P4 (ou T3) entrerait dans les conclusions établies. C'est ce que la précision 18 interdit.
  Le module final est juste.
- **Reproduit** : `essais/essai_survivants.py`, journal `essais/essai_survivants.log`. Sur la copie de base, les trois
  artefacts arrêtent : « garde 7 : P3-P4/tromperie-lineaire-c7/conforme vaut True alors que les états de la lecture disent
  False (saboteur contre témoin « au-dessus », témoin contre honnête « au-dessus ») » ; « intention/…/T3/etabli vaut True
  alors que la lecture dit False par ses états et ses bornes » ; de même pour T2 à borne basse 0. Sur M09, M10 et M12,
  l'artefact du mutant passe, avec 13 conclusions établies.
- **Correction** (tests seulement, module inchangé) : trois artefacts de plus dans ce test, par `_lecture_recalculee` :
  `jeux[P[0]]["temoin-honnete"]["au_dessus_du_plancher"] = True` (motif « conforme vaut True alors que les états de la
  lecture disent False ») ; `jeux[P[0]]["saboteur-mention"]["au_dessus_du_plancher"] = False` (motif « T3/etabli vaut True
  alors que la lecture dit False ») ; `intention[P[0]]["T2"]["bas"] = 0.0` (motif « T2/etabli vaut True »). Le nombre de
  tests reste 165. L'empreinte des tests change : elle n'est pas encore citée (`<<EMPREINTE_TESTS>>`).

### VF2-02 — mineur — Précision 18, cas sain des drapeaux non consultés : le test pose un `conforme` déjà égal aux états

- **Où** : `test_organisme_non_etabli_drapeaux_bruts_conformes_reserves_sans_objet` (tests l. 1487-1502) ; module
  l. 535-541.
- **Problème** : la précision 18 dit que les drapeaux que la table ne consulte pas ne sont pas recoupés. Le test pose
  `conforme = True` sur la lecture « a6_verrou ». Or ce drapeau y vaut déjà vrai, et les états disent conforme (journal :
  `conforme brut True`, états « au-dessus » et « non au-dessus »). Pour `conforme`, l'écriture ne change rien : le cas
  sain n'est pas éprouvé. Le mutant M11 recoupe `conforme` même quand P3-P3 n'est pas établie. Il passe les 165 tests.
  Il arrêterait à tort un run « organisme non établi » dont ce drapeau n'est pas consulté. Le sens est celui d'un arrêt
  de trop, jamais d'une promotion.
- **Reproduit** : `essais/essai_survivants.log`. `conforme` inversé sur cette lecture : la base passe (aucune conclusion
  établie) ; M11 arrête (« conforme vaut False alors que les états de la lecture disent True »).
- **Correction** (tests) : dans ce test, poser `conforme` au contraire des états (la négation de la valeur lue), issue
  recalculée ; aucun arrêt attendu.

### VF2-03 — mineur — Précision 17 : une entrée qui échoue après tous ses contrôles reçoit quand même un « non lu » par cible visée

- **Où** : `_executer_entree`, l. 1762-1769. Le comportement est figé par
  `test_entree_en_echec_garde_la_reserve_contraire_deja_calculee` (tests l. 1797-1798).
- **Problème** : le texte dit : « seuls les contrôles non faits deviennent « non lus » ». Le code ajoute un contrôle
  « non lu » (« entrée entière ») à chaque cible que vise l'analyse, même quand aucun contrôle ne restait à faire.
- **Reproduit** : `essais/essai_precision17.py`, journal `essais/essai_precision17.log`.
  - (a) A1 échoue dans le placebo (descriptif seulement), après ses sept contrôles : cinq « non lus » sont ajoutés. La
    recommandation porte alors, pour P3-P3, P3-P4 et T3, à la fois « non robuste aux contrôles de l'addendum » et « non
    contrôlée par l'addendum ». T1 et T4, contrôlés et favorables, sont dits « non contrôlée ».
  - (b) A8, valeur non finie dans le descriptif après deux contrôles favorables : « P3-P3/enjeux-attention-c15 : non
    contrôlée par l'addendum (réserves : reserve_A8_non_lue) ».
  Le sens reste prudent : rien n'est retiré, rien n'est promu. Mais le verdict R13 citerait « non contrôlée » une
  conclusion contrôlée. Et ces « non lus » comptent parmi les réserves possibles de l'audit de symétrie : ils peuvent
  empêcher « toutes » de se déclencher.
- **Correction** : écrire au texte ce que fait le code (module inchangé). Précision 17, ajouter : « chaque cible que vise
  l'analyse reçoit en plus un contrôle « non lu » (« entrée entière »), même si tous ses contrôles ont été faits ». Autre
  voie, plus coûteuse : n'ajouter le « non lu » qu'aux cibles sans contrôle lu dans l'entrée. Le module changerait alors,
  et il faudrait une nouvelle revue.

### VF2-04 — mineur — Garde 14 : une ligne faite d'espaces n'a pas d'artefact

- **Où** : `charger_textes`, l. 2176-2178 ; `test_garde_4_textes_lus_sur_les_seuls_sauts_de_ligne` (tests l. 1035-1062).
- **Problème** : le texte (garde 14) dit : « une ligne illisible : arrêt ». Les notes (§ 7, point 2) précisent : « lignes
  vides = exactement vides ; une ligne d'espaces est illisible (arrêt) ». Le test éprouve les lignes vides, pas une ligne
  d'espaces. Le mutant M19 ignore une ligne d'espaces : c'est un repli silencieux. Il passe les 165 tests.
- **Reproduit** : `essais/essai_survivants_2.log`. Base : « garde 4 : fichier espaces.jsonl : ligne 3 illisible
  (JSONDecodeError) ». M19 lit cinq textes sans arrêt.
- **Correction** (tests) : un artefact de plus dans ce test : une ligne `b"   "` insérée, arrêt avec son numéro.

### VF2-05 — information — Tolérances des gardes 12 et 13 non épinglées par les tests

- **Où** : `TOLERANCE_COHERENCE`, `TOLERANCE_LOCALISATION` (l. 98-99). Les tests sont
  `test_garde_coherence_de_la_lecture_avec_le_run_source` (écart de 0,01) et
  `test_garde_localisation_egale_a_celle_de_la_lecture` (5e-10 sain, 1e-6 artefact).
- **Problème** : M13 (1e-3 au lieu de 1e-9) et M14 (1e-7) passent les 165 tests. Le texte écrit « à 1e-9 près » pour
  les deux. Le module porte bien 1e-9 (lu ligne à ligne). Mais les tests laissent la valeur dériver jusqu'à 1e-2
  (garde 12) et jusqu'à 1e-6 (garde 13).
- **Reproduit** : `essais/essai_survivants_2.log`. La base arrête à 1e-6 (garde 12) et à 1e-8 (garde 13). M13 et M14
  passent.
- **Correction** (tests, facultative) : garde 12, un artefact à 1e-6 et un cas sain à 1e-12 ; garde 13, un artefact à
  2e-9.

### VF2-06 — information — Garde 15 : suffixe du nom du run non éprouvé

- **Où** : `RUN_ADDENDUM`, l. 75 ; `test_forme_de_la_commande`.
- **Problème** : M24 retire l'ancre de fin. Il passe les 165 tests : « 20261020-130000-addendum-p3-bis » serait accepté.
  Le module ancre bien l'expression.
- **Reproduit** : `essais/essai_survivants_2.log`. La base arrête (« garde 15 : run de l'addendum
  '20261020-130000-addendum-p3-bis' : nom AAAAMMJJ-HHMMSS-addendum-p3 attendu ») ; M24 passe.
- **Correction** (tests, facultative) : ajouter ce nom aux artefacts du test.

### VF2-07 — information — Qualité des morts, relue journal par journal

- V2 (motif adapté) : dans le code final, appeler le verrou avec toutes les cibles rend le verrou **plus strict**. Le
  cas sain s'arrête : « conclusions établies des analyses […] ≠ conclusions recalculées ». Le verrou n'en devient jamais
  plus permissif. Les variantes permissives du nouveau verrou sont M01 et M02 : elles sont tuées.
- V7 : tué par le motif attendu. Le verrou de fin arrête aussi le premier cas du test (issue changée). Seul
  l'instantané arrête le second (borne d'un jeu changée). Le test garde les deux.
- G9 : tué par un `IndexError` du test (réplique 17 sur 10), pas par une assertion sur 50. La valeur 50 est tenue aussi
  par la garde 15 : `PARAMETRES_DU_TEXTE` est écrit à la main dans le test, et vérifié par la ligne de commande réelle.
- G4 : tué par le motif : l'effectif minimal général prend le relais. La règle des dix paires est épinglée par le motif.
- M15 : tué par la suite complète, par `test_A8_degenere_logits_non_finis_dans_une_action` (garde 13 sur des NaN au
  même rang). Le test de la garde 13 lui-même n'a pas de NaN.
- Aucun mutant n'est mort d'une erreur de collecte ou d'une exception sans rapport avec sa règle.

### VF2-08 — information — Empreinte du texte citée par les notes

- **Où** : notes de correction, l. 9-10 et § 8.
- **Problème** : les notes citent le brouillon 6 « état final » sous `77bc2fe0…`. Le fichier relu vaut `411eb334…`. Il
  a été modifié le 2026-10-20 à 04:28:03 UTC, au même instant que `workflow-verification-finale-v1.js`, sans doute pour
  l'ajout du paragraphe « Contre-lecture 4 ». Les règles lues dans ce rapport sont celles de `411eb334…`.
- **Correction** : citer l'empreinte du texte effectivement relu, ou celle du texte scellé.

### VF2-09 — information — Numéro de garde du motif d'une ligne illisible

- **Où** : `charger_textes`, l. 2182.
- **Problème** : le motif dit « garde 4 : … ligne N illisible ». Le texte range ce cas sous la garde 14 (« une ligne
  illisible : arrêt, avec son numéro, sans texte »). Le test attend « garde 4 ». Sans effet sur aucun calcul.
- **Correction** : aucune dans le module, dont l'empreinte changerait. Au plus une ligne au texte (motif écrit sous
  « garde 4 »).

### VF2-10 — information — Trace de lecture dans le dépôt de travail ; durée

- Un `git status --porcelain` (lecture) a été lancé une fois, à 05:41:59 UTC. Le dossier `.git` a changé de date : git
  crée puis retire un verrou d'index. `.git/index` est inchangé (05:02:25). Aucun fichier suivi n'a été touché. Aucune
  autre commande git n'a été lancée.
- Durée de la suite complète : 1 047 s pour la base (notes : 916 s). La machine était chargée par un autre chantier
  (charge 6 à 7). Les suites des mutants ont pris de 997 à 1 148 s.

## Pannes (point 3 de l'angle)

- **P1, déterminisme.**
  - Fonction pure, sept scénarios des tests (sain, plancher, bornes de A5, forme du coût, saturation, dégénéré, lecteur
    étendu), deux processus séparés, `PYTHONHASHSEED` différents. Sorties identiques octet pour octet, sérialisées dans
    l'ordre d'insertion et à clés triées (`pannes/determinisme.log`).
  - De même aux tirages du texte (2 000 et 10 000), sur le scénario sain (`pannes/determinisme-complet.log`, empreinte
    `3b433ad8…`).
  - Lancement réel : deux dépôts jetables copiés du même gabarit, même commande. Le `resultat` des deux sorties scellées
    est identique octet pour octet (sha256 `32b8f856d95bfdd5f71838bbf71145a58fa82506e1fce2bdc4c6ab649e942a59`,
    81 468 octets). Les graines des deux manifestes sont égales.
- **P2, aucun texte d'action dans la sortie.** Textes fabriqués avec un marqueur propre à chaque champ de chaque action
  (titre, proposition, contrôles, coût, prédiction). Les marqueurs sont sans chiffre, pour ne changer aucune mesure.
  - Fonction pure, cas sain et cas à réserve : aucun marqueur dans la sortie ; aucune sous-chaîne de 24 caractères des
    200 premiers textes.
  - Lancement réel : aucun marqueur, aucun séparateur, aucun séparateur échappé, ni dans la sortie scellée ni dans le
    manifeste.
  - Le motif de la garde 4 ne porte aucun texte (M20 tué).
- **P3, U+2028, U+2029, U+0085 dans un texte d'action.** Sept variantes : séparateurs dans la proposition ; dans le champ
  du coût ; avant la clé du coût (après le saut de ligne) ; entre la clé et ses deux-points (`COST\u0085:`) ; à la place
  du saut de ligne qui précède `PREDICTION` ou `CONTROLS` ; dans une clé en gras (`**TITLE **:`).
  - Fichier écrit comme le run : une ligne par action (1 600 sauts de ligne pour 1 600 actions ; `splitlines` aurait
    coupé). Relu égal à l'écrit. Gardes 5 et 14 passées : l'alignement est gardé.
  - Règles (1) et (2) de A5 : aucun défaut du module, aucune divergence. Les deux règles lisent ces séparateurs de la
    même façon : `^` en mode multiligne ne s'ouvre qu'après `\n`, et `\s` prend U+2028.
  - Addendum complet sans arrêt, relecture « calculé ». Lancement réel (`executer`, run source scellé à ces textes,
    lecture décisive faite) : sortie scellée, aucun arrêt.
  - Le mutant qui relit par `str.splitlines` (M18) est tué.

## Table des mutants

| id | origine | règle mutée | statut | test qui le tue (premier échec) | durée (s) |
|---|---|---|---|---|---|
| V1 | CB2 | verrou ouvert : exiger_verrou n'arrête plus un contrôle lu (non « sans objet ») sur une cible non établie (motif adapté) | tué | `test_verrou_de_fin_sur_les_conclusions_recalculees` | 28 |
| V2 | CB2 | verrou ouvert : exiger_verrou appelé avec toutes les cibles possibles au lieu des seules établies (motif adapté) | tué | `test_verrou_de_fin_sur_les_conclusions_recalculees` | 26 |
| V3 | CB2 | verrou ouvert (témoin) : exiger_verrou accepte une réserve sur une conclusion non établie (motif adapté) | tué | `test_verrou_de_fin_sur_les_conclusions_recalculees` | 26 |
| V4 | CB2 | verrou ouvert (témoin) : table : P3-P4 établie sans la ligne d'issue « critères 2 et 3 » | tué | `test_conclusions_etablies_table_fermee` | 7 |
| V5 | CB2 | verrou ouvert (témoin) : clé interdite au_dessus_du_plancher retirée de la liste (filtre et verrou) | tué | `test_garde_du_verrou_sain_et_artefacts` | 27 |
| V6 | CB2 | verrou ouvert (témoin) : exiger_verrou ne compare plus l'issue recopiée à l'issue décisive | tué | `test_issue_primaire_inchangee_et_garde_de_la_copie` | 75 |
| V7 | CB2 | verrou ouvert (témoin) : instantané de la lecture décisive non comparé en fin de course | tué | `test_issue_modifiee_pendant_l_addendum_arrete` | 42 |
| C1 | CB2 | cible fausse : A1 : témoin contre honnête vise T3 au lieu de P3-P4 | tué | `test_A1_sain` | 21 |
| C2 | CB2 | cible fausse : A1 : saboteur contre témoin vise P3-P3 au lieu de P3-P4 | tué | `test_A1_sain` | 24 |
| C3 | CB2 | cible fausse : A1 : saboteur contre mention vise P3-P3 au lieu de T3 | tué | `test_A1_sain` | 25 |
| C4 | CB2 | cible fausse : A7 : saboteur contre témoin vise P3-P3 au lieu de P3-P4 | tué | `test_A7_sain` | 26 |
| C5 | CB2 | cible fausse : A7 : saboteur contre mention vise P3-P3 au lieu de T3 | tué | `test_A7_sain` | 29 |
| C6 | CB2 | cible fausse : entrée A4 entière en échec : T1 n'est plus « non lu » (VISEES) | tué | `test_entree_entiere_en_echec_rend_non_lues_les_cibles_visees` | 13 |
| C7 | CB2 | cible fausse : entrée A3 entière en échec : T3 n'est plus « non lu » (VISEES) | tué | `test_entree_entiere_en_echec_rend_non_lues_les_cibles_visees` | 12 |
| C8 | CB2 | cible fausse : entrée A7 entière en échec : P3-P4 et T3 ne sont plus « non lus » (VISEES) | tué | `test_entree_entiere_en_echec_rend_non_lues_les_cibles_visees` | 13 |
| N1 | CB2 | niveau changé : A2 (a) : intervalle calculé à 80 %, annoncé 95 % | tué | `test_niveaux_des_intervalles_de_l_aire_du_cout_et_de_T2_propre` | 8 |
| N2 | CB2 | niveau changé : T2_propre (A5) : intervalle à 80 %, annoncé 95 % | tué | `test_niveaux_des_intervalles_de_l_aire_du_cout_et_de_T2_propre` | 8 |
| N3 | CB2 | niveau changé : A2 (b) : intervalle de δ̄ à 80 % | tué | `test_A2_sain` | 24 |
| N4 | CB2 | niveau changé : A4 (a) : intervalles à 80 % | tué | `test_A4_sain` | 21 |
| N5 | CB2 | niveau changé : A4 (b) : intervalle de Δ_intra à 80 % | tué | `test_A4_sain` | 21 |
| N6 | CB2 | niveau changé : A4 (c) : T1 de sensibilité à 80 % | tué | `test_A4_sain` | 21 |
| N7 | CB2 | niveau changé : A6 : effets du coût à 80 % | tué | `test_A6_sain` | 21 |
| N8 | CB2 | niveau changé : A1 : T1 à 97,5 % au lieu de 95 % | tué | `test_A1_sain` | 21 |
| N9 | CB2 | niveau changé : A7 (ii) : niveau fixe 95 % au lieu du niveau du jeu (97,5 % sur saboteur contre honnête) | tué | `test_A7_artefact_forme_du_cout` | 24 |
| J1 | CB2 | moyenne sur les jetons : A2 (c) : fenêtre juste avant le champ notée par la moyenne des jetons | tué | `test_aucune_moyenne_sur_les_jetons_score_d_empan_maximum` | 7 |
| J2 | CB2 | agrégation changée : A2 (b) : fenêtres d'une sonde à attention notées au maximum (logits ignorés) | tué | `test_A2_fenetres_d_une_sonde_a_attention_par_ses_logits` | 10 |
| R1 | CB2 | réserve mal câblée : A8 saturation : les deux conditions exigées (all au lieu de any) | tué | `test_A8_regles_de_reserve_par_condition` | 10 |
| R2 | CB2 | réserve mal câblée : A8 début : une seule condition suffit (or au lieu de and) | tué | `test_A8_regles_de_reserve_par_condition` | 10 |
| R3 | CB2 | réserve mal câblée : A4 (a) : les deux conditions exigées (et au lieu de ou) | tué | `test_A4a_chaque_condition_suffit_et_calculs_en_echec_non_lus` | 11 |
| R4 | CB2 | réserve mal câblée : A4 (a) : condition « borne basse de A_T4(b) ≤ quantile observé » retirée | tué | `test_A4a_chaque_condition_suffit_et_calculs_en_echec_non_lus` | 11 |
| R5 | CB2 | réserve mal câblée : A6 : réserve témoin ou mention levée même si la borne était déjà > 0 dans la lecture | tué | `test_A6_reserve_temoin_ou_mention_et_effets_non_calculables` | 10 |
| L1 | CB2 | réserve non lue omise : A1 : calcul en échec ou non calculable lu favorable | tué | `test_A1_calculs_en_echec_non_lus` | 11 |
| L2 | CB2 | réserve non lue omise : A3 : calcul des contrastes en échec lu favorable | tué | `test_toute_exception_autre_que_garde_arrete` | 41 |
| L3 | CB2 | réserve non lue omise : A4 (a) : calcul en échec lu favorable | tué | `test_A4a_chaque_condition_suffit_et_calculs_en_echec_non_lus` | 12 |
| L4 | CB2 | réserve non lue omise : A4 (b) : calcul en échec lu favorable | tué | `test_A4a_chaque_condition_suffit_et_calculs_en_echec_non_lus` | 11 |
| L5 | CB2 | réserve non lue omise : A6 P3-P1 : effet au lecteur étendu non calculable lu favorable | tué | `test_A6_reserve_temoin_ou_mention_et_effets_non_calculables` | 11 |
| L6 | CB2 | réserve non lue omise : A7 (i) : séparation non calculable lue favorable | tué | `test_A7_formes_marge_et_correlations` | 11 |
| L7 | CB2 | réserve non lue omise : A7 (ii) : calcul restreint en échec lu favorable | tué | `test_A7_formes_marge_et_correlations` | 11 |
| L8 | CB2 | réserve non lue omise : A8 : début de l'action non lu écrit favorable quand le calcul échoue | tué | `test_A8_regles_de_reserve_par_condition` | 11 |
| L9 | CB2 | réserve non lue omise : A8 : contrôle de saturation omis quand le calcul échoue (sonde à attention) | tué | `test_A8_regles_de_reserve_par_condition` | 10 |
| L10 | CB2 | réserve non lue omise : A8 : poids maximal non défini lu favorable | tué | `test_A8_regles_de_reserve_par_condition` | 10 |
| G1 | CB2 | garde affaiblie : garde 7 : borne ou aire non numérique acceptée dans un jeu lu | tué | `test_garde_jamais_eprouvee_cas_sain_et_artefact[garde 7 : valeur de jeu non numérique]` | 20 |
| G2 | CB2 | garde affaiblie : règle des 1 % portée à 5 % de tirages dégénérés | tué | `test_degenerescences_au_dela_de_1_pourcent` | 6 |
| G3 | CB2 | garde affaiblie : A7 (ii) : forme contrôlée seulement si présente dans 50 actions du jeu (au lieu de 10) | tué | `test_A7_formes_marge_et_correlations` | 10 |
| G4 | CB2 | garde affaiblie : A4 (b) : une paire intra-tâche suffit (au lieu de 10) | tué | `test_A4_degenere` | 16 |
| G5 | CB2 | seuil changé : A7 (iii) : seuil de corrélation 0,90 au lieu de 0,50 | tué | `test_A7_formes_marge_et_correlations` | 10 |
| G6 | CB2 | seuil changé : A8 : seuil du poids maximal 0,99 au lieu de 0,95 | tué | `test_A8_regles_de_reserve_par_condition` | 9 |
| G7 | CB2 | seuil changé : A8 : seuil des trois premiers 0,80 au lieu de 0,50 | tué | `test_A8_regles_de_reserve_par_condition` | 9 |
| G8 | CB2 | seuil changé : A8 : deux premiers jetons au lieu de trois | tué | `test_A8_regle_stricte_des_trois_premiers_jetons_et_segments` | 6 |
| G9 | CB2 | seuil changé : A2 (b) : 10 répliques au lieu de 50 | tué | `test_aucune_moyenne_sur_les_jetons_score_d_empan_maximum` | 6 |
| G10 | CB2 | seuil changé : A2 (a) et A5 : seuil d'aire 0,45 au lieu de 0,5 | tué | `test_A2a_et_A5_seuil_de_l_aire_du_cout` | 9 |
| M01 | VF2 | précision 16 : verrou de fin : liste des analyses non comparée à la liste recalculée | tué | `test_verrou_de_fin_sur_les_conclusions_recalculees` | 24 |
| M02 | VF2 | précision 16 : verrou de fin : conclusions non recalculées (liste des analyses crue) | tué | `test_verrou_de_fin_sur_les_conclusions_recalculees` | 22 |
| M03 | VF2 | précision 16 : verrou de fin : clés interdites non cherchées dans la sortie | tué | `test_garde_du_verrou_sain_et_artefacts` | 21 |
| M04 | VF2 | plan, point 5 : verrou de fin : contrôle « sans objet » qui écrit hors du descriptif accepté | tué | `test_garde_du_verrou_sain_et_artefacts` | 21 |
| M05 | VF2 | précision 17 : entrée en échec : contrôles déjà faits effacés | tué | `test_entree_en_echec_garde_la_reserve_contraire_deja_calculee` | 15 |
| M06 | VF2 | précision 17 : entrée en échec : réserves contraires déjà calculées retirées | tué | `test_entree_en_echec_garde_la_reserve_contraire_deja_calculee` | 15 |
| M07 | VF2 | précision 18 : P3-P1.etablie non recoupé | tué | `test_garde_7_drapeaux_bruts_recoupes_avec_les_etats` | 20 |
| M08 | VF2 | précision 18 : P3-P1.etablie recoupé avec bas ≥ 0 au lieu de bas > 0 | tué | `test_garde_7_drapeaux_bruts_recoupes_avec_les_etats` | 21 |
| M09 | VF2 | précision 18 : conforme recoupé sans la condition « témoin contre honnête non au-dessus » | SURVIT | `—` | 1079 |
| M10 | VF2 | précision 18 : T3 recoupé sans la condition « saboteur contre mention au-dessus » | SURVIT | `—` | 1161 |
| M11 | VF2 | précision 18 : conforme recoupé même quand P3-P3/<p> n'est pas établie (drapeau non consulté lu) | SURVIT | `—` | 1025 |
| M12 | VF2 | précision 18 : contrastes T1, T2, T4 recoupés avec bas ≥ seuil au lieu de bas > seuil | SURVIT | `—` | 1053 |
| M13 | VF2 | garde 12 : cohérence lecture contre run source à 1e-3 près au lieu de 1e-9 | SURVIT | `—` | 1102 |
| M14 | VF2 | garde 13 : localisation à 1e-7 près au lieu de 1e-9 | SURVIT | `—` | 1089 |
| M15 | VF2 | garde 13 : localisation : deux NaN au même rang jugés différents | tué (suite complète) | `test_A8_degenere_logits_non_finis_dans_une_action` | 860 |
| M16 | VF2 | garde 14 : mesures booléennes non relues sur les textes | tué | `test_garde_5_alignement_des_textes` | 33 |
| M17 | VF2 | garde 14 : mesures réelles (coûts) non relues sur les textes | tué | `test_garde_5_alignement_des_textes` | 33 |
| M18 | VF2 | garde 14 : textes découpés par str.splitlines (coupe à U+2028, U+2029, U+0085) | tué | `test_garde_4_textes_lus_sur_les_seuls_sauts_de_ligne` | 7 |
| M19 | VF2 | garde 14 : ligne d'espaces ignorée au lieu d'un arrêt (ligne illisible) | SURVIT | `—` | 1122 |
| M20 | VF2 | garde 14 : motif d'une ligne illisible qui recopie la ligne (texte d'action) | tué | `test_garde_4_textes_lus_sur_les_seuls_sauts_de_ligne` | 8 |
| M21 | VF2 | garde 15 : graines non comparées clé par clé | tué | `test_graines_exactement_celles_de_leurs_cles` | 29 |
| M22 | VF2 | garde 15 : paramètres de tirage non comparés au texte | tué | `test_garde_15_parametres_de_tirage_du_texte_par_la_ligne_de_commande` | 10 |
| M23 | VF2 | garde 15 : point d'entrée : paramètres de tirage non contrôlés avant toute lecture | tué | `test_garde_15_parametres_de_tirage_du_texte_par_la_ligne_de_commande` | 9 |
| M24 | VF2 | garde 15 : nom du run d'addendum sans ancre de fin (suffixe libre accepté) | SURVIT | `—` | 1109 |
| M25 | VF2 | garde 16 : manifeste de 64 octets exactement compté « court » (≤ au lieu de <) | tué | `test_garde_9_premier_passage` | 7 |
| M26 | VF2 | garde 16 : nom du run source retiré du critère lexical | tué | `test_garde_9_premier_passage` | 6 |
| M27 | VF2 | garde 16 : manifeste lisible hors de forme traité comme lisible | tué | `test_garde_9_premier_passage` | 6 |
| M28 | VF2 | garde 16 : fichier illisible par le système compté pour 64 octets au lieu de zéro | tué | `test_garde_9_premier_passage` | 6 |
| M29 | VF2 | plan, point 6 : réserve « non lue » classée avec les contrôles contraires (« non robuste ») | tué | `test_recommandation_reserve_non_lue_seule_jamais_non_robuste` | 6 |
| M30 | VF2 | plan, point 6 : réserve générale de la garde 11 classée « non robuste » | tué | `test_recommandation_reserve_non_lue_seule_jamais_non_robuste` | 6 |
| M31 | VF2 | plan, point 6 : lecture gelée des réserves de forme de A7 omise | tué | `test_recommandation_reserve_non_lue_seule_jamais_non_robuste` | 8 |
| M32 | VF2 | critères gelés : « non contrôlée » sans la lecture gelée « la conclusion reste établie… » | tué | `test_recommandation_reserve_non_lue_seule_jamais_non_robuste` | 6 |
| M33 | VF2 | critères gelés : lecture de reserve_A7_forme_du_cout remplacée par « la sonde lit la forme » | tué | `test_recommandation_reserve_non_lue_seule_jamais_non_robuste` | 6 |
| M34 | VF2 | critères, audit : « non lu » compté comme déclenché | tué | `test_audit_symetrie_tout_non_lu_ne_declenche_pas_toutes` | 6 |
| M35 | VF2 | critères, audit : « aucune » exige aussi aucun « non lu » | tué | `test_audit_symetrie_tout_non_lu_ne_declenche_pas_toutes` | 6 |
| M36 | VF2 | critères, audit : « aucune » dès deux conclusions établies | tué | `test_audit_symetrie_tout_non_lu_ne_declenche_pas_toutes` | 6 |
| M37 | VF2 | critères, audit : « aucune » sans exiger l'audit R4 de la lecture | tué | `test_audit_symetrie_tout_non_lu_ne_declenche_pas_toutes` | 6 |
| M38 | VF2 | précision 8 : sans réserve possible, « toutes » vrai (déclencheur vrai) | tué | `test_organisme_non_etabli_drapeaux_bruts_conformes_reserves_sans_objet` | 25 |
| M39 | VF2 | critères, audit : contrôles « sans objet » comptés parmi les réserves possibles | tué | `test_audit_symetrie_toutes_les_reserves_possibles_declenchees` | 6 |

Bilan : CB2, 51 tués sur 51, chacun par le test que les notes annoncent. Neufs : 30 tués par leur test tueur, 1 par la
suite complète (M15), 8 survivants (M09, M10, M11, M12, M13, M14, M19, M24). Durée : test tueur, ou test tueur et suite
complète.
