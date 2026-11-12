# Contre-lecture bornée de la v11 de T0.6 — v1 (rendu partiel, avant le rendu 3)

Fille 9, contre-lectrice neutre (R2). Écrit le 2026-11-08, de 00:01 à 00:40 UTC (heures relevées par `date -u`). Non scellé ; aucun `.sha256`.

## Messages de la mère (recopiés mot pour mot)

> **Contre-lecture bornée de la v11 de T0.6**, chemin critique, même organisation que d'habitude : le code par un sous-agent neuf de lignée Opus, le reste par toi. Aucune clé, aucune location.
> **Objet** : branche `prep/t06-v11`, tête `bf953e059991f4ed7c75dc92adbf7dfbb0b32589`, partie de `dfc032c6`. Rapport du développeur : `docs/notes/g0-deux-semaines-v1/rapport-e3-echecs-et-v11-v1.md` (`744ad94b…`).
> **Contexte** : E3 s'est arrêtée parce que la suite complète a échoué sur l'instance. Dernière ligne : « 50 failed, 3113 passed, 23 skipped in 4488.87s (1:14:48) ». Traces sur `essai/t06-e3-v4`, `eee41eb9`, `traces/t06-20261107-222500-WXKq/tests.txt` (R-1728, R-1730). Texte de Vast pour une instance détruite : `{ "instances": null }`.
> **Ce qui doit être vrai** :
> 1. **L'analyse des 50 échecs** : 46 d'environnement, liés à l'hôte durable de l'organisme ; 2 défauts de test dans la minuterie v7 ; 1 défaut de portabilité du générateur d'ordres sous Python 3.11 ; et l'échec de `test_cibles_invisibles` sur la branche de la course. Vérifie-la sur `tests.txt`.
> 2. **La suite ciblée figée** : `scripts/tests-cibles-t06-v1.txt` (79 fichiers) et `scripts/tests-exclus-t06-v1.txt` (36 exclusions motivées). `test_t06_v11_liste.py` doit interdire tout oubli. **Aucun essai n'est désactivé pour obtenir du vert**, et aucune exclusion ne retire un essai dont dépend le run de T0.6.
> 3. **L'amorce v9** : l'empreinte de la liste est écrite en dur, et il n'y a jamais de repli sur la suite complète. **Le lanceur v11** cite l'amorce v9 et `session_v10`.
> 4. **`session_v10`** : `{"instances": null}` est une absence probable, non concluante. L'absence n'est établie que par une liste non vide sans l'instance, à deux relevés.
> 5. **E3 bis** : `T06_GO_EPREUVES_TOTAL_USD=8` (GO-2026-11-07-08, 3 USD de plus) ; dépense antérieure 2,092 ; tout autre total est refusé.
> 6. **La ligne attendue** : 1 780 essais estimés ; la valeur opposable sera relevée sur l'instance à E3 bis.
> **Bientôt** : la fille 10 annoncera son rendu 2, déjà sur cette tête : bras B v2, banc de mutations à 11 sur 11, brouillon d'addendum des grandeurs avec la tolérance du contrôle G4 sur le score de W (GO-2026-11-07-09). Intègre-le à la même contre-lecture s'il arrive à temps. Sinon, rends d'abord la v11.
> **Rendu** : branche `prep/contre-lecture-t06-v11`, avec un verdict par pièce et des couples. Pas de `.sha256`. Vise 90 minutes.

> (00:01 UTC) le rendu 2 de la fille 10 est poussé sur la même branche `prep/t06-v11`. **La nouvelle tête est `888f4d6e56ef2e2f206e29d208d3f9944a25d0f4`** […] l'issue n'est jamais imprimée […] G4 suit GO-2026-11-07-09 […] dis si 0,15 est trop lâche ou trop serré ; l'amorce v9 joue `bras_b_v2` par défaut ; la borne de l'annexe vaut encore 2 400 s dans l'amorce, alors que ta contre-lecture estimait environ 5 800 s : tranche.

> (00:02 UTC) attention, la tête de `prep/t06-v11` va encore bouger […] `configuration_v4.exiger_config_t06_v4` […] n'accepte un plafond d'épreuve que dans l'intervalle de 1,5 à 3,5 […] Continue sur ce qui ne bouge pas : l'analyse des échecs, la liste figée, `session_v10`, le bras B v2. Conclus sur l'amorce et le lanceur à la tête du rendu 3, que je te transmettrai.

(Les deux derniers messages sont résumés aux crochets ; le texte entier est dans la session de la mère.)

## Qui a lu quoi
- **Code**, à `888f4d6e` : un sous-agent neuf de lignée Opus, qui n'avait lu aucune des pièces. Il a contre-lu la liste et la garde, l'amorce v9, le lanceur v11, `session_v10`, le bras B v2, les cibles invisibles v2 et le générateur pour Python 3.11. Il a remonté les imports du run et rejoué le banc. Il a écrit 10 mutations neuves. Il a joué 273 essais neufs : 273 passés, 0 échec, 0 sauté, en 639 s. **La suite ciblée complète n'a pas été jouée.**
- **Moi** :
  - les échecs, relevés dans `tests.txt` (copie tirée de `eee41eb9`) ;
  - le rapport de la fille 10, les 36 motifs d'exclusion et le compte des fichiers (79 + 36 = 115 fichiers `tests/test_*.py`) ;
  - l'addendum, la mesure de tolérance et le rapport du bras B v2 ;
  - GO-2026-11-06-01, GO-2026-11-07-08 et GO-2026-11-07-09, sur `main` (`a20fcd0c`).

## 1. Les 50 échecs, vérifiés sur `tests.txt`
| fichier | échecs | cause relevée dans les lignes `E` | nature |
|---|---|---|---|
| `test_hote_durable_a1_v3_v4.py` | 30 | refus « interpréteur autre que Python 3.13 (C1) » (l'image est en 3.11.2) ; `KeyError` sur des fichiers de `donnees/attaque-goodhart-v3-a1v3-troisieme-v1/` absents de l'extraction | environnement |
| `test_hote_durable_a1_v3_v3.py` | 16 | mêmes causes | environnement |
| `test_sonde_hote_durable_a1_v3_v10.py::test_releve_du_pilote_de_carte[False]` | 1 | attend « nvidia-smi absent », obtient « GPU 0: NVIDIA A100-SXM4-80GB » | environnement (machine) |
| `test_t06_v7_amorce_minuterie.py` (2, `[v7]`) | 2 | assertion sur le mauvais `journal.txt` | défaut de test |
| `test_t06_v9_nouveaux.py::test_generateur_de_l_ordre_e3_v6…` | 1 | `SyntaxError: f-string: expecting '}'`, ligne 229 de `generer_ordres_v6.py`, sous Python 3.11 | défaut de portabilité |

**Le décompte du rapport et du message de la mère est faux.** Il y a **47 échecs d'environnement et 3 qui touchent T0.6** : 46 + 1 + 2 + 1 = 50. Le rapport écrit « 46 d'environnement, 4 touchent T0.6 », mais `test_cibles_invisibles` n'est **pas** parmi les 50. Il échoue sur la branche de la course, qui n'a pas été jouée à E3. La nature de chaque échec est juste, et aucun n'est un défaut du code de T0.6. Couple : `couples-rapport-e3-v11-v1.json`.

**Erreur de ma contre-lecture précédente (course v1), déclarée.** J'y écrivais « Essais : prêts pour T0.6 » sur la foi des 180 essais neufs et des 620 essais `tests/test_t06_*.py`. Je n'avais fait jouer ni la suite complète ni `test_cibles_invisibles`, qui échouait sur cette branche. Il fallait écrire « suite complète non jouée ».

## 2. Liste ciblée et exclusions — **prête, avec réserves**
- **Garde.** Aucun oubli possible : `test_t06_v11_liste.py:123-135` refuse un fichier ni listé ni exclu, un fichier à la fois listé et exclu, un doublon dans la liste. Il garde aussi l'empreinte. Un doublon dans les exclusions n'est pas vu (lecture en dictionnaire) : défaut mineur.
- **Aucun essai désactivé** pour obtenir du vert, et aucun saut ni échec admis neuf. Le seul `importorskip` vient tel quel de la v1. Le saut ajouté à `:147` ne se produit pas sur l'image, mais son message est faux.
- **Imports du run.** Le sous-agent les a remontés depuis `controle_ia.t06.lanceur_v4`, `bras_b_v2` et les sessions v2, v3 et v10 (66 modules). Aucune exclusion ne retire un essai d'un module du run. Les essais perdus ne portent que sur les lanceurs v1 à v8 et les sessions v4 à v6, hors de la chaîne.
- **Exclusion contestée (faiblement) : `tests/test_t06_v4_scripts.py`.** C'était le seul essai du refus « `T06_EPUISEMENT_SIMULE_S` réservé aux épreuves à blanc ». Ce refus existe au lanceur v11 (`:186`) sans aucun essai ciblé. Il faut un cas sain et un artefact sur la v11.
- **Lacune hors exclusion.** `controle_ia.agregation_r1_v4.*` et `runs_nuit.alignement_v1`, importés par le bras B, n'ont aucun fichier d'essais. Ce n'est pas bloquant : G3 rejoue la sortie publiée entière.
- **Forme.** Le motif « 46 échecs sur l'image python:3.11 » est recopié sur les 15 fichiers de l'hôte durable, alors que seuls deux ont échoué. Le motif juste pour les 13 autres est « étranger au run de T0.6 ».

## 3. `session_v10` — **corriger avant E3 bis** (sinon réserve écrite dans l'ordre)
- `{"instances": null}` est bien non concluant. Il l'était déjà en v9 : seul le message change.
- **Défaut hérité de `session_v9.py:66-77`.** Si `show instance 123` rend `{"id": 456}`, `{"instances": {"id": 456}}` ou `[{"id": 456}]`, la réponse vaut « absence établie » (code 4). Deux relevés donnent alors `ARRET mort` (lanceur `:305`). C'est contraire à la règle de l'essai 11 : un message sur une autre instance ne conclut pas. Correctif : un identifiant ≠ celui demandé est non concluant ; un essai avec cas sain et artefact.
- L'énoncé « absence établie seulement par une liste non vide » est inexact : un 404 exact l'établit aussi (`_INTROUVABLE`, voulu en v9). Les textes doivent le dire.
- Faux positif prudent : `instance\s+(\d+)` s'applique à tout le texte. Cela produit des alertes possibles, jamais une destruction.

## 4. Bras B v2 — **corriger avant E3 bis**
- **Conformes** :
  - l'issue n'est plus sur la sortie standard (`bras_b_v2.py:548`, chemin et empreinte seulement), ni sur la sortie d'erreur ;
  - G4 suit GO-2026-11-07-09 : au bit sur A100-SXM4-80GB aux mêmes versions, sinon un écart absolu ≤ 0,15 sur le score de W en log-cote, au maximum par action (`:63`, `:306-318`) ;
  - le score versé et le score rejoué viennent du même modèle de pli, que G3 vérifie (`:412-413`) ;
  - le banc d'origine rejoué donne 11 mutations tuées sur 11, avec un témoin réussi.
- **5 mutations neuves sur 10 survivent.** Deux portent sur la décision :
  - **X3**, `a_SC_H` calculée contre la mention : le monde planté met la mention trop près de l'honnête ;
  - **X8**, « signatures simultanées » rendue comme « fuite ».

  Survivent aussi X5 (G7 retirée), X6 (contrefactuels de la mention rangés chez le saboteur) et X7 (`<` au lieu de `≤` au seuil de fuite). Essais à ajouter :
  - un monde où la mention est loin de l'honnête et proche du saboteur ;
  - `decider` à ses bornes exactes (0,65 et 0,95) et sur le cas simultané ;
  - G7 sur une classe vide ;
  - les comptes de la mention contrefactuelle.
- **Tolérance 0,15 : plutôt serrée que lâche.** La justification tient pour « ne fait basculer aucune signature » : ±0,5 sur tous les scores déplace les aires d'au plus 0,0012. Mais la valeur est bornée par des bruits **simulés sur les activations finales**, non propagés à travers 15 couches. Le bruit relatif de 2⁻⁶, plausible entre deux architectures de carte, donne déjà un maximum de 0,36 et un 99e centile de 0,27, ce qui arrêterait G4.
  - Un vrai défaut, comme une mauvaise note ou un décalage de jetons, déplace les scores de l'ordre de l'écart entre classes (environ 3 à 11). Une tolérance de **0,3** détecte encore un tel défaut à plus de dix fois sa valeur et réduit le risque de perdre le bras B sur le repli H200.
  - **Recommandation : 0,3, confiance moyenne.** À défaut, garder 0,15 en déclarant que le bras B peut s'arrêter sur H200 sans défaut réel. Cela ne coûte rien sur A100, où l'égalité au bit s'applique.
- **Lecture du « sinon » de GO-2026-11-07-09, à trancher par Lazar au scellement de l'addendum.** Le code retient la lecture stricte : sur A100 aux mêmes versions, un écart au bit arrête le bras. L'autre lecture applique la tolérance dès que l'égalité au bit échoue. Couple dans l'addendum.
- **R9** : le script de mesure tire par `default_rng(0)` et non par `SeedSequence`. Réserve de forme : la mesure ne décide rien, mais elle justifie une grandeur scellée.
- **R6** : l'addendum cite le script et la sortie de la mesure sans empreinte. Couple.
- **Borne de l'annexe, tranchée** : **2 400 s reste la borne du module**, et il ne faut rien changer à l'amorce. Les environ 5 800 s sont le pire cas de l'annexe entière : module, attente du verrou (1 500 s, seulement si une autre consignation tient le verrou) et trois poussées. Ce pire cas est borné en argent par la minuterie de dépense épuisée, sous les 200 USD. Il doit être écrit dans l'ordre de la course (couple 6 de ma contre-lecture précédente), et non dans le code.

## 5. Pièces dont le verdict attend le rendu 3
**Amorce v9 et lanceur v11 : verdict à la tête du rendu 3.** Ce qui est déjà relevé à `888f4d6e` et restera à vérifier :
- **Amorce v9** :
  - l'empreinte en dur égale la liste ;
  - tout refus finit par `exit` ;
  - aucun repli sur la suite complète, **sauf par `TESTS_ARGS`** : avec `PREREG_ABSENT=1`, une option seule passée par `T06_TESTS_ARGS` (lanceur `:220`), comme `-x`, relancerait toute la suite. L'ordre d'E3 bis doit l'interdire, ou l'amorce doit refuser `TESTS_ARGS` hors du mode jouet.
- **Lanceur v11** :
  - les totaux 5 et 8 sont acceptés, et 9, `abc` et `8.0` refusés, avec cas sain et artefact ;
  - **mais le total 8 n'est lié à rien**. Le lanceur ne vérifie jamais que GO-2026-11-07-08 existe dans le registre des GO lu (il l'est sur `main`, non dans l'arbre de la branche). La dépense antérieure de 2,092 est saisie par l'opératrice : avec 0, un plafond de 7,9 passerait.
  - Correctif recommandé : exiger la ligne GO-2026-11-07-08 au registre quand le total vaut 8, et une dépense antérieure ≥ 2,092 dans ce cas. À défaut, l'ordre d'E3 bis fixe les deux valeurs et la fille 6 les relève.
  - Le commentaire de la ligne 5 est altéré par un remplacement global.
- **Échéance d'E3 bis** (réserve 3 de la fille 10). GO-2026-11-07-08 est l'objet propre d'E3 bis, avec une échéance au 12 novembre ; GO-2026-11-06-01 en garde le plafond cumulé. **Je recommande que la configuration d'E3 bis cite GO-2026-11-07-08** (confiance moyenne).
- **Ligne attendue** : 1 780 est une estimation locale sous Python 3.11.18 avec torch pour processeur. Seule la ligne relevée sur l'instance à E3 bis est opposable, comme écrit au rapport.

## Couples
- `couples-rapport-e3-v11-v1.json` : 1 couple pour le bilan 47 + 3 du rapport des échecs ; il s'applique.
- `couples-addendum-bras-b-v2-v1.json` : 2 couples pour l'addendum, la lecture du « sinon » à trancher et les empreintes de la mesure (R6) ; ils s'appliquent dans l'ordre.
