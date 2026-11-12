# Verdict (R13) — T0.3, simulation du lemme d'additivité et du théorème négatif — run décisif `20261004-080257-t03` — v1

- Lecteur : sous-agent neuf (R13), lignée Claude Opus 5.5, le 2026-11-10 (UTC). Je n'ai écrit ni le préenregistrement, ni le code, ni l'analyse, ni la note de résultats, ni aucune des trois contre-lectures.
- Critères appliqués : `prereg/T0.3-simulation-lemme-theoreme-v1.md`, sha256 `7474743a0fa2a9db5da85bcedb0087ea57114fcca0fbb3415c7a97bf1b78d1fb`, section « Critères de lecture gelés » (l. 315-367), avec la « Métrique » (l. 223-250), le « Seuil » (l. 252-265) et la « Liste d'arrêt » (l. 369-392).
- Résultats jugés : note `docs/notes/resultats-T0.3-v1.md` (`9ab618edae17e757…`) ; lecture gelée `diag/20261004-080257-t03/lecture.json` (`c5aa62b42feed399…`) et `lecture.md` (`650ef86bef453104…`) ; comptes bruts `diag/20261004-080257-t03/bloc-*.json` et `calibrage.json` ; manifeste `runs/20261004-080257-t03/manifeste.json` (`c9bba5e1f5f8dbf2…`).
- Mes calculs : trois scripts et leurs sorties, versés dans `docs/verdicts/verdict-T0.3-simulation-lemme-theoreme-v1-fichiers-de-travail.tar` (empreintes en section 10). Aucune dépense. Aucun fichier existant modifié. Rien lu du coffre.

## 1. Verdict

**T0.3 : confirmé avec réserves.**

- **Confirmé**, avec les mots du préenregistrement : les **31 prédictions sont « confirmées »** au sens du critère B (l. 337-340 : toutes leurs cellules conformes). Les 886 cellules sont conformes, soit 342 statistiques et 544 trajectorielles : 0 contraire, 0 non concluante, 0 violation trajectorielle.
  - Aucune réplication n'est due (critère C, l. 342-346).
  - L'audit gelé n'est pas déclenché (critère D, l. 348-352) : aucune prédiction réfutée, aucune violation, aucune garde d'arrêt. Les variances des écarts réduits valent 0,955 sur les 63 comparaisons aux formes closes et 0,853 sur les 104 égalités, dans les bornes [0,3 ; 3].
  - Les six lectures de la table E (l. 354-367) sont prononcées : toutes leurs prédictions exigées sont confirmées.
- **Recalcul indépendant.** J'ai réécrit la table A depuis le texte du préenregistrement et recalculé les formes closes avec scipy, sans le code du programme, puis je les ai appliquées aux comptes bruts des blocs.
  - Les 886 états, et les 342 écarts réduits des cellules statistiques, sont identiques à ceux de `lecture.json` (0 écart).
  - Les deux variances d'audit sont identiques aussi.
  - La lecture ne dépend donc pas du seul code qui l'a produite.
- **Le run jugé est bien le run préenregistré** (section 3) : code au commit cité, préenregistrement et grille inchangés, 3 280 graines reconstruites, run unique et complet, résultats jamais retouchés depuis leur dépôt.
- **Reproduction au bit près.** J'ai réexécuté hors du dépôt le code du commit cité, avec la grille scellée et les graines du manifeste.
  - Les 13 fichiers bruts (calibrage et douze blocs) en sortent avec, octet pour octet, les empreintes des fichiers scellés.
  - Les comptes jugés sont donc bien ceux que ce code produit avec ces graines.
- **Avec réserves** (section 7). Elles viennent de la règle de symétrie (R4, « trop beau = réserve ») et de la portée du run. Elles **ne changent pas la lecture gelée** (l. 313).
  - Réserve principale : 31 sur 31 était l'issue attendue par construction. 19 prédictions sur 31 sont des vérifications de l'instrument ; 4 sont mixtes.
  - Plusieurs magnitudes des prédictions informatives étaient connues en ordre de grandeur avant le scellement ; le préenregistrement le déclare (l. 418).
  - La confirmation valide, en simulation, l'instrument et l'arithmétique des preuves ; elle ne valide pas la revendication sur modèles réels (l. 77).
- **Chiffres cités au fonds** (`proposal_v2_TAIF_2026-10-07.txt`, l. 89-93) : **exacts**, au chiffre près, contre les pièces scellées. Une précision est à porter : « 0.21–0.35 » sont les taux au niveau d'effet d'épisode le plus fort testé (τ = 0,2), pas l'étendue sur tous les niveaux (section 8).

## 2. Pièces et empreintes vérifiées (R6, R11)

Empreintes recalculées par `sha256sum` sur l'arbre de la branche `claude/upbeat-cray-dmauvv`. « Compagnon » veut dire : égale au fichier `.sha256` voisin.

| pièce | chemin | sha256 | contrôle |
|---|---|---|---|
| préenregistrement scellé | `prereg/T0.3-simulation-lemme-theoreme-v1.md` | `7474743a0fa2a9db5da85bcedb0087ea57114fcca0fbb3415c7a97bf1b78d1fb` | compagnon ; même empreinte au commit de scellement `5e481537`, dans le manifeste et dans R-024 |
| grille décisive | `prereg/T0.3-grille-v2.json` | `5609f920c0d606a192e92b2c2172416dad740b158940aac1ee049de8b8affe23` | compagnon ; citée l. 9 ; égale à la grille recopiée dans le manifeste |
| manifeste du run | `runs/20261004-080257-t03/manifeste.json` | `c9bba5e1f5f8dbf268e47023db8fac56c2cfd011721c6f89ba8ecad413e1a8ea` | compagnon |
| lecture gelée | `diag/20261004-080257-t03/lecture.json` | `c5aa62b42feed399e8626e3f681830023dc2dd124663d138e3a0c8170f1a7bbb` | compagnon ; rattachée au manifeste |
| table de lecture | `diag/20261004-080257-t03/lecture.md` | `650ef86bef453104784fa7237187aa2d211be3169f25ffa9bba854d0b2f5722d` | compagnon |
| calibrage | `diag/20261004-080257-t03/calibrage.json` | `cb72b41d4dff5ee547037e700aeec963dbf5762a0727ccf6f615fbcad178f383` | compagnon ; rattaché au manifeste |
| blocs, équivalence, figures | `diag/20261004-080257-t03/` (16 fichiers JSON et MD, 6 images) | une par compagnon | 22 compagnons conformes sur 22 ; les 15 JSON portent l'empreinte du manifeste `c9bba5e1…` |
| note de résultats | `docs/notes/resultats-T0.3-v1.md` | `9ab618edae17e757ab83d5de7a346ebf08bebf89aef61e4337cb5c067e5fd545` | compagnon |
| documents qui font foi (l. 13-17) et rapports des trois contre-lectures (l. 431, 469, 502) | voir le préenregistrement | — | 9 empreintes égales aux citations, sur 9 |
| texte envoyé au fonds | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` | `b2458c2d209aaa817ca3c77bfc8ef99288d489ae7b58b747fd8cda6a71e33ca0` | compagnon |

**Absence vérifiée sur disque avant d'écrire (R11).** Aucun verdict de T0.3 n'existe, ni dans `docs/verdicts/` de cette branche ni dans celui d'`origin/main`. La commande `ls docs/verdicts/ | grep -i -E "t0\.?3|simulation|lemme"` ne rend rien.
- Le registre des décisions confirme ce constat : « T0.3 : 31 (R-025, aucun verdict scellé) » (R-1603).
- Le programme d'entretien v18 aussi : « verdict formel R13 non prononcé » (`brouillons/entretien-taif-v3/programme-entretien-taif-v18.md`, l. 185).

## 3. Le run jugé est-il celui qui a été préenregistré ?

Oui. Points vérifiés sur l'historique d'`origin/main`, complet sur ce passage, et sur les fichiers.

1. **Chronologie** (heures des commits, UTC, 2026-10-04) :
   - code cité `d73ac469`, à 07:38:03 ;
   - préenregistrement scellé, commit `5e481537`, à 08:02:47 ;
   - manifeste créé à 08:02:57 (champ `cree_le`), puis déposé avec la mention « run en cours » (commit `fe51aa19`), à 08:03:40 ;
   - résultats, commit `251707e3`, à 08:16:40 ;
   - correction O-2 du code, gel levé, commit `8d6fa72e`, à 08:17:15, donc après les résultats.
2. **Gel du code** (l. 7-8 et 289 ; liste d'arrêt, point 2).
   - `git diff d73ac469 5e481537 -- src tests prereg/T0.3-grille-v2.json` est vide.
   - Entre ces deux commits, seuls `brouillons/`, `prereg/` (préenregistrement, contre-lecture 3) et `registres/` changent, comme le prévoit l. 8.
   - Le code de `src/controle_ia/simulation_t03/` et de `src/controle_ia/agregateurs/` est encore identique aujourd'hui à celui du commit cité.
3. **Manifeste.**
   - Drapeaux : `decisif` vrai, `depot_propre` vrai, aucune réserve.
   - Commande : celle de l. 24.
   - Références : commit `5e481537…`, commit cité `d73ac469…`, grille `5609f920…`.
   - Blocs : les douze, sans sélection (point 3) ; `replication_de` nul.
   - Versions : Python 3.11.15, numpy 2.4.6, scipy 1.17.1.
4. **Graines (R9).** Les 3 280 graines du manifeste couvrent 1 640 tâches et leurs 1 640 tâches de réplication, dérivées d'avance (l. 286).
   - Toutes sont reconstruites depuis l'entropie de la grille, 179038975902893800976156754715385090228, celle de l. 283.
   - La clé de chaque tâche est faite des 64 premiers bits de sha256(nom) (l. 284).
   - Résultat : 0 écart, sur la clé comme sur l'état de contrôle.
5. **Résultats non retouchés.**
   - `git diff 251707e3 HEAD` est vide sur `diag/20261004-080257-t03/`, sur la note de résultats, sur le préenregistrement et sur la grille.
   - `git diff fe51aa19 HEAD` est vide sur le manifeste.
6. **Run unique.** Dans l'historique disponible d'`origin/main`, un seul dossier `runs/*t03*` et un seul dossier `diag/*t03*` ont été déposés. Un seul manifeste du dépôt nomme `simulation_t03`.
7. **Liste d'arrêt, recalculée sur les sorties.**
   - Garde de calibrage sous P₀ (point 6) : 92 contrôles sur les 12 configurations, tous passés. Ils se répartissent en 22 seuils exacts, 46 Monte-Carlo continus, 3 Monte-Carlo discrets et 21 seuils de Ville.
   - Garde d'équivalence (point 7) : écart maximal 9,4·10⁻¹⁴, pour une tolérance de 10⁻⁹.
   - Durée (point 10) : 705,7 s, pour une limite de 6 heures.
   - P1.1 : 0 égalité au seuil ; écart maximal |S(X) − S(Y) − B| de 5,7·10⁻¹⁴, pour une tolérance de 2·10⁻⁷ (n₀ = 200).
   - Les gardes internes aux blocs (multi-ensemble, positions, valeurs finies ; points 8 et 9) ne se relisent pas dans les sorties. La reproduction (point 9 ci-dessous) les a réexécutées.
8. **Essais au commit cité.** Sur un extrait de `d73ac469` obtenu par `git archive`, 125 essais passent : c'est le nombre que rapporte la contre-lecture 3. Ils comprennent des essais sur cas sain et sur artefact des gardes (R5), par exemple `test_garde_multiensemble_artefact`, `test_garde_calibrage_artefact` et `test_garde_commit_cite_artefact`.
9. **Reproduction**, hors du dépôt et non décisive. Elle est consignée ici, comme l. 288 l'exige pour « tout autre lancement de la grille ».
   - Matériel : code extrait du commit cité (`git archive d73ac469`), grille scellée, graines lues dans le manifeste. Python 3.13.18, numpy 2.4.6, scipy 1.17.1 ; 4 cœurs ; 400 s.
   - Gardes : celles du lancement, qui exigent le dépôt, ne sont pas appelées. Celles qui sont internes aux blocs le sont : multi-ensemble, positions, valeurs et seuils finis.
   - Sérialisation : comme le fait `ecrire_resultat`, avec le même `run_id` et la même empreinte de manifeste.
   - Résultat : les 13 fichiers, `calibrage.json` et `bloc-P1a.json` à `bloc-P8.json`, ont exactement les empreintes des fichiers scellés. La chaîne qui va des graines aux comptes bruts est reproduite au bit près, et les gardes internes passent de nouveau.
   - Rien n'a été écrit dans `runs/` ni dans `diag/`. Ce lancement est à reporter au registre par la session mère.

## 4. Application des critères gelés, prédiction par prédiction

Règles appliquées :
- table A (l. 319-335) ; seuil Z = 4 écarts-types (l. 262) ; écarts-types de la « Métrique » (l. 245-249) ;
- constante 0,99 de P7.2 (l. 263) ; tolérances d'appariement de P5.3 (l. 264).

« z » est l'écart réduit signé : (taux − référence)/écart-type. Chaque ligne a été recalculée indépendamment (section 1) sur `bloc-*.json` et `calibrage.json`.

| prédiction | lignes | nature déclarée | critères de la table A (nombre de cellules) | états | marge observée | verdict (critère B) |
|---|---|---|---|---|---|---|
| P1.1 | 80-87 | instrument | trajectoriel (510) | 510 conformes, 0 violation | 0 discordance ; écart max 5,7·10⁻¹⁴ | confirmée |
| P1.2 | 88 | instrument | forme close (9) | 9 conformes | z de −1,03 à 0,49 | confirmée |
| P1.3 | 89-99 | instrument | forme close (24) ; au-dessus, décroissance en n₀ (12) | 36 conformes | formes closes z de −2,36 à 2,53 ; décroissance z ≥ 8,33 | confirmée |
| P1.4 | 100 | instrument | égal (9) | 9 conformes | z de −2,40 à 0,94 | confirmée |
| P2.1 | 103-114 | instrument | forme close (24) | 24 conformes | z de −1,55 à 0,63 | confirmée |
| P2.2 | 116 | instrument, critère lâche déclaré | au plus (21) | 21 conformes | z ≤ 0,00 | confirmée |
| P2.3 | 117 | instrument | au-dessus (3) | 3 conformes | z = 9,82 ; 21,20 ; 32,72 | confirmée |
| P3.1 | 122-127 | instrument | trajectoriel (18) | 18 conformes | 0 violation | confirmée |
| P3.2 | 128 | informative (magnitude) | au-dessus (36) | 36 conformes | z ≥ 17,2 | confirmée |
| P3.3 | 129 | instrument | forme close (6) | 6 conformes | z de −2,48 à 0,49 | confirmée |
| P3.4 | 130-133 | informative (heuristique) | au-dessus (12) | 12 conformes | z ≥ 100,6 | confirmée |
| P4.1 | 136-142 | instrument | trajectoriel (7) | 7 conformes | 0 valeur différente, 0 discordance | confirmée |
| P4.2 | 143 | instrument | égal (68) | 68 conformes | z de −1,89 à 1,32 | confirmée |
| P4.3 | 144-148 | instrument | au-dessus (1) ; forme close (1) ; égal (1) | 3 conformes | z = 642,3 ; 0,57 ; 0,81 | confirmée |
| P5.1 | 151-156 | instrument | trajectoriel (5) | 5 conformes | 0 violation | confirmée |
| P5.2 | 157 | informative | au-dessus (4) | 4 conformes | z ≥ 1 203 | confirmée |
| P5.3 | 158-162 | informative | au plus (2) ; au-dessus (4) ; appariement complet | 6 conformes | au plus : z = 0,52 et 1,40 ; au-dessus : z ≥ 1 191 ; 0 épisode hors tolérance sur 20 000, pour chaque appariement | confirmée |
| P5.4 | 163 | instrument | trajectoriel (1) | 1 conforme | 0 violation | confirmée |
| P5.5 | 164 | informative | au-dessus (1) | 1 conforme | z = 467 | confirmée |
| P6.1 | 167-171 | mixte | au-dessus (8) ; au plus (4) | 12 conformes | au-dessus z ≥ 22,4 ; au plus z ≤ 1,59 | confirmée |
| P6.2 | 172-176 | mixte | en dessous (4) ; au-dessus (4) | 8 conformes | en dessous z ≤ −28,9 ; au-dessus z ≥ 315 | confirmée |
| P6.3 | 177 | instrument | forme close (4) | 4 conformes | z de −1,39 à 0,42 | confirmée |
| P6.4 | 178-185 | mixte | forme close (2) ; au-dessus (8) ; au plus (2) | 12 conformes | formes closes z = 0,63 et 1,02 ; au-dessus z ≥ 26,5 ; au plus z ≤ 1,18 | confirmée |
| P6.5 | 186-191 | mixte | forme close (3) ; au plus (3) ; au-dessus (3) | 9 conformes | formes closes z de −1,04 à −0,17 ; au plus z ≤ −1,66 ; au-dessus z ≥ 152,6 | confirmée |
| P7.1 | 194-199 | instrument | trajectoriel (3) | 3 conformes | 0 violation des trois inclusions | confirmée |
| P7.2 | 200 | instrument | au moins 0,99 (1) | 1 conforme | 20 000 sur 20 000 ; z = 14,2 | confirmée |
| P7.3 | 201 | informative | au-dessus (6) | 6 conformes | z ≥ 1 377 | confirmée |
| P8.1 | 204 | instrument, critère lâche déclaré | au plus α (3) | 3 conformes | taux 0,01665 ; 0,01935 ; 0,01685 ; z ≤ −19,8 | confirmée |
| P8.2 | 205-211 | informative | au-dessus (11) | 11 conformes | z ≥ 10,95 (plus petite marge : τ = 0,05 à n₀ = 200, 0,0338 contre 0,01665) | confirmée |
| P8.3 | 212-214 | informative, valeurs vues | dépasse α (4) | 4 conformes | 0,2105 ; 0,35145 ; 0,1656 ; 0,0661 ; z ≥ 10,4 | confirmée |
| P8.4 | 215 | instrument | taux conforme (34) | 34 conformes | moyennes de 0,04605 à 0,05455 ; z de −2,35 à 2,42 | confirmée |

**Totaux.**
- 31 prédictions confirmées sur 31 ; 886 cellules, dont 342 statistiques et 544 trajectorielles, toutes conformes. C'est le compte annoncé l. 298.
- Natures déclarées : 19 vérifications de l'instrument, 8 informatives, 4 mixtes (P6.1, P6.2, P6.4, P6.5).

**Critère C (réplication).** Aucune cellule statistique n'est contraire : aucune réplication n'est due. Le gel du code a été levé à bon droit (R-025).

**Critère D (audit).** Non déclenché ; détail en section 6.1.

**Critère E (énoncés du programme et du brief).** Les six lectures sont prononcées.
- Leur texte dans `lecture.json` est identique, mot pour mot, aux six lignes de la table E (l. 362-367).
- Les prédictions complémentaires (P5.2, P5.5, P7.3) sont confirmées ; elles restent sans effet sur les lectures.

## 5. Points d'interprétation (lecture la plus prudente)

1. **Valeur de la forme close de P4.3.** Deux passages du préenregistrement ne coïncident pas tout à fait.
   - L. 145 annonce « la forme close exacte 0,9673 ». L. 148 précise : « au seuil calibré du run ».
   - Explication : 0,9673 est la valeur au quantile exact de χ²₃ (7,8147). Je recalcule par énumération 0,90501, 0,96729 et 0,98967 pour T = 30, 40 et 50 : ce sont les valeurs de la contre-lecture 2, 0,9050, 0,9673 et 0,9897. Au seuil calibré du run (Monte-Carlo, 7,8624), l'énumération donne 0,966672 ; mon calcul et le `p_th` du code concordent.
   - Taux observé : 19 348 sur 20 000, soit 0,9674. La cellule est conforme dans les deux lectures : z = 0,57 au seuil du run, z ≈ 0,08 contre la valeur imprimée.
   - Sans effet.
2. **P5.3, « sinon la cellule est non concluant » (l. 264).** Le texte ne dit pas laquelle des trois cellules d'un appariement serait visée ; le code vise la seule statistique globale. La question ne se pose pas : aucun épisode sur 20 000 n'est hors tolérance, pour l'autocorrélation comme pour les suites. Les deux appariements sont complets.
3. **P2.3, « environ 10 écarts-types à B = 10 » (l. 117).** C'est une magnitude annoncée, pas un critère. Le critère est « au-dessus » à Z = 4. Observé : z = 9,82 à B = 10, cohérent avec l'annonce.
4. **« Seuil exact quand la loi le permet (`exacts` de la grille) » (l. 240).** La grille fixe la liste des seuils exacts configuration par configuration. La statistique de dispersion de P4.3 y est calibrée par Monte-Carlo (`exacts` vide pour `hetero_3x40`), alors que sa loi sous P₀ est exactement χ²₃. C'était fixé avant le run, et l. 148 prévoit ce seuil calibré. Sans effet.

Aucune de ces lectures prudentes ne change un état de cellule.

## 6. Audit de symétrie (R4)

Le résultat est « trop propre » : 31 sur 31, 0 contraire. Je lui applique l'audit qu'un échec aurait reçu.

### 6.1 Le critère gelé (D)

- **Variances des écarts réduits** : 0,955 sur 63 et 0,853 sur 104, dans [0,3 ; 3] ; mon recalcul donne les mêmes valeurs (0,95543 et 0,85264). Moyennes : −0,10 et −0,15.
- **Sous-ensembles, à titre d'information** (ce ne sont pas des critères gelés) :
  - formes closes : P1.3, 1,57 sur 23 ; P2.1, 0,43 sur 16 ; P1.2, 0,30 sur 9 ; P3.3, 1,16 sur 6 ;
  - égalités : P8.4, 1,04 sur 34 ; P4.2, 0,64 sur 60 ; P1.4, 0,94 sur 9.
- **Le cas de P4.2.** La plus basse variance, 0,64 pour P4.2, s'explique sans échantillon réutilisé. Les 15 ou 19 alarmes d'une configuration se calculent sur les mêmes épisodes rebrassés. Leurs références viennent des mêmes 100 000 épisodes sous P₀, indépendants du calibrage (l. 265). Ces écarts réduits sont donc corrélés positivement, ce qui abaisse leur dispersion attendue.
- **Aucune cellule n'est près de son seuil.**
  - Plus grand |z| : 2,53 parmi les formes closes, 2,42 parmi les égalités.
  - Plus petite marge d'une cellule « au-dessus » : z = 8,33 (P1.3, décroissance).
  - Plus petite marge d'une cellule informative qui prédit un sens (« au-dessus », « en dessous », « dépasse α ») : z ≈ 10,45 (P8.3, σ utilisé = 0,8σ).
- **Probabilité d'une fausse contrariété.** Le préenregistrement l'estime entre 2 et 3 % pour l'ensemble du run (l. 302). Avec un code juste, 0 contraire est donc l'issue la plus probable ; ce zéro n'est pas suspect en soi.

### 6.2 Les critères pouvaient-ils échouer ?

- **Cellules trajectorielles** (6 prédictions, 544 cellules). Ce sont des identités et des inclusions exactes : elles ne peuvent échouer que par une erreur de code ou d'énoncé.
  - Elles ne sont pas vides de sens. Le bloc P1a calcule les statistiques sur les épisodes attaqués X, puis compare leurs alarmes à celles de « Y + B » (`src/controle_ia/simulation_t03/blocs.py`, l. 306-315, au commit cité). P4.1 compare les valeurs au bit près.
  - Leur force est celle d'un essai du code sur 20 000 épisodes par cellule. Ce n'est pas un essai de la théorie.
- **Formes closes** (8 prédictions ; 63 comparaisons dans l'audit). Une cellule échoue si le taux simulé s'écarte de la valeur théorique de plus de 4 écarts-types.
  - Résolution : environ ±1,1 point pour p ≈ 0,17 et ±1,3 point pour p ≈ 0,68, à 20 000 épisodes ; ±0,3 point près de 0,06, à 100 000 épisodes (P2).
  - J'ai recalculé avec scipy, sans le code du programme, les 54 valeurs imprimées dans le préenregistrement pour P1.2, P1.3, P2.1, P3.3, P6.3, P6.4 et P6.5. J'ai aussi recalculé c₂₀₀ = 3,473944, ρ* = 0,182927 et s* = 39,1146. Toutes ces valeurs sont égales à la précision imprimée. La 55ᵉ valeur imprimée, celle de P4.3, est traitée au point 5.1.
  - Les formes closes ne sont donc pas tirées du code qu'elles éprouvent.
- **Prédictions informatives** (8 prédictions et les cellules informatives des 4 mixtes). Elles pouvaient échouer si le phénomène était absent ou plus faible.
  - Mais chaque cellule informative qui prédit un sens passe avec une marge d'au moins 10 écarts-types (|z| ≥ 10,4). Les deux cellules informatives « au plus » de P5.3 sont à z = 0,52 et 1,40 : au taux sous P₀, ce qu'elles prédisent.
  - Le préenregistrement déclare que plusieurs de ces magnitudes étaient connues en ordre de grandeur avant le scellement (l. 396-419). Sources : simulations exploratoires de la contre-vérification, qui touchaient n₀ = 200, φ = ±0,5, r = 5, τ, c, σ et T4 ; construction de 2606.10456 ; vérifications des contre-lectures (z ≥ 12,6 pour P3.2, z ≥ 44 pour P3.4, valeurs de P6, P7 et P8).
  - Le risque d'échec était faible. Leur confirmation est une réplication sur graines neuves et grille fixée, pas un essai risqué.
- **Critères lâches par construction.**
  - P2.2 et P8.1 sont déclarés lâches (l. 116 et 204).
  - Les cellules « au plus » (maximum sous dépendance positive, statistiques globales de P5.3) ne peuvent pas être contraires du côté favorable.
  - P8.4 a une résolution de ±0,006 à ±0,0095 autour de 0,05 (4 écarts-types estimés, plancher 0,0015). La cellule confirme un taux voisin de α. Elle ne distingue ni la valeur exacte 0,04995 de 0,05, ni un rang conforme décalé d'un cran.
- **Conclusion sur la sévérité.** Les critères avaient des dents contre les erreurs de code et d'énoncé, à l'échelle d'un point de puissance. Ils en avaient peu contre la théorie elle-même, dont plusieurs magnitudes informatives étaient déjà vues. 31 sur 31 était le résultat attendu.

### 6.3 Une prédiction a-t-elle été ajustée après coup ?

**Non.**
- Le préenregistrement lu aujourd'hui est identique, octet pour octet, à celui scellé à 08:02:47 et consigné dans le manifeste à 08:02:57 (`7474743a…`). La grille aussi.
- Ni les prédictions, ni les seuils, ni les cellules, ni la table E n'ont changé après le run.
- **Changements antérieurs au scellement, déclarés** dans la section « Contre-lecture ». Tous viennent des contre-lectures, faites sur données jetables ou par calcul exact, avant toute cellule décisive (l. 424) :
  - P4.3 : seuil 0,99, inatteignable, remplacé par la forme close exacte (Rem-1, calcul sans tirage) ;
  - P3.2 ajoutée (Rem-2) ;
  - tolérances de P5.3 resserrées (Rem-22, grille v2).
- **Dépendance aux valeurs vues, déclarée** (l. 214 et 418) : la sélection des cellules de P8.3.
  - Valeurs vues avant le scellement : 0,214 ; 0,364 ; 0,164 ; 0,067.
  - Valeurs du run décisif : 0,2105 ; 0,35145 ; 0,1656 ; 0,0661.
- **Ce que je ne peux pas établir par les fichiers** : qu'aucune cellule décisive n'a été calculée avant le scellement (l. 424). Les indices vont tous dans ce sens :
  - un seul dossier de run ;
  - un manifeste déposé pendant le run ;
  - une grille v1 « jamais exécutée », de même entropie, sans aucun dossier de run à son nom.

### 6.4 Conclusion de l'audit

Aucun signe de défaut. La propreté s'explique par la construction du run : une majorité de vérifications de l'instrument, et des magnitudes en partie connues d'avance. La réserve écrite par l'auteur (R-025 ; note de résultats, l. 41-46) tient ; je la reprends en section 7.

## 7. Réserves

Aucune ne change la lecture gelée.

1. **Trop beau (R4) : la portée de la confirmation.** 31 sur 31 était attendu par construction. La confirmation établit trois choses, en simulation :
   - les agrégateurs et les calibrages sont corrects ;
   - l'arithmétique des preuves est juste ;
   - les magnitudes annoncées sont retrouvées.

   Ce n'est pas un essai risqué de la théorie. C'est la réserve de R-025 : « vérifications de l'instrument en majorité ».
2. **Valeurs vues.** Plusieurs magnitudes informatives étaient connues avant le scellement, et la sélection de P8.3 en dépend (l. 214 et 418).
   - Les chiffres de fausses alarmes cités au fonds (0,21 ; 0,35 ; 0,17) confirment, sur graines neuves, des valeurs déjà vues en exploration : 0,214 ; 0,364 ; 0,164.
   - Ce ne sont pas des découvertes du run décisif.
3. **Monde synthétique.**
   - Scores : standardisés, μ₀ = 0 et σ = 1 connus, sauf en P8 (l. 33) ; marginale gaussienne pour l'essentiel, Exp(1) − 1 dans une partie de P6 ; lois de Student à 5 degrés de liberté, exponentielle et de Gumbel dans trois réglages de P8, jugés seulement par le calibrage conforme de P8.4.
   - Loi honnête : N(0, 1), indépendante d'une action à l'autre, ou ses variantes listées.
   - Attaques : construites (classes M, C, K).
   - Hors de portée (l. 53-59) : notamment L4, et la robustesse du calibrage conforme à un décalage entre épisodes de calibrage et de déploiement. C'est elle que l'usage sur modèles réels demandera.
4. **Résolution.** Les formes closes sont vérifiées à environ un point de puissance près ; P8.4 à environ ±0,006 près (section 6.2).

**Observation sans effet sur la lecture.** Ce verdict vient 37 jours après le run. Les résultats avaient déjà été cités dans le texte envoyé au fonds le 2026-10-07, et repris dans des pièces préparées pour l'extérieur (README v3, fiche d'entretien). Les chiffres cités au fonds sont exacts (section 8) : rien n'est à corriger. Seul l'ordre est à noter : citation externe d'abord, verdict R13 ensuite.

## 8. Chiffres du texte envoyé au fonds

Source : `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` (`b2458c2d…`).

| affirmation (ligne) | pièce scellée | valeur scellée | jugement |
|---|---|---|---|
| « All 31 predictions of a pre-registered simulation were confirmed » (l. 89) | `lecture.md` l. 7-37 | 31 « confirmée » | exact |
| « 342 statistical and 544 path-level cells, 0 contrary » (l. 89) | préenregistrement l. 298 ; `lecture.json` | 342 + 544 cellules, 0 contraire | exact |
| « false alarms reach 0.21–0.35 under episode effects » (l. 90-91) | `bloc-P8.json` ; note de résultats l. 100-101 | τ = 0,2 : 0,2105 (n₀ = 200) et 0,35145 (n₀ = 1 000) | exact au niveau le plus fort testé (τ = 0,2) ; sur les six réglages d'effet d'épisode, les taux vont de 0,0338 (τ = 0,05, n₀ = 200) à 0,35145 ; « reach » se lit donc « atteignent, à τ = 0,2 » |
| « 0.17 under correlation between agents » (l. 91) | `bloc-P8.json` ; note de résultats l. 103 | c = 0,4 : 0,1656 (c = 0,2 : 0,08275) | exact, arrondi, au niveau c = 0,4 |
| « instead of 0.05 » (l. 91) | P8.3, « dépasse α » (l. 212) | α = 0,05 ; taux de la règle de Ville bien spécifiée : 0,01665 à 0,01935 (P8.1) | exact ; la référence est α nominal, pas le taux bien spécifié, qui est plus bas |
| « These checks validate the instrument, not the claim on real models » (l. 92) | préenregistrement l. 77 | — | conforme |
| « one part of the lemma (splitting across agents within the same step) remains to be tested » (l. 92-93) | l. 57 ; table E, l. 362 | L4 non testé | conforme |
| « The pre-registered simulation confirmed 31 of 31 predictions » (l. 270-271) | idem | 31 sur 31 | exact |
| « In our simulation, its central statement does not hold for its own construction » (l. 87-88), qui renvoie à 2606.10456 | P6.5 (l. 186-191) ; table E, l. 364 | somme 0,0719 ; 0,1261 ; 0,25325, conformes aux formes closes et au-dessus de α = 0,05 ; maximum 0,0475 ; 0,04395 ; 0,0271, « au plus à son taux » | conforme à la lecture gelée, qui établit que la proposition 1 (« puissance = taux de faux positifs ») est fausse pour la somme ; elle tient pour le maximum, qui reste au plus à son taux. La phrase est donc juste si la proposition vise toute statistique fondée sur les marginales, somme comprise ; je ne l'ai pas vérifié sur le PDF (R7). La construction de T0.3 garde la marginale gaussienne du papier (Beta dans son code), et φ₁ = 0,725 ne vient que du code (l. 19-22). |

## 9. Ce que ce verdict ne dit pas

- **Rien sur les modèles réels ni sur les activations.** Le verdict valide, en simulation, l'instrument et l'arithmétique des preuves. Le préenregistrement le dit (l. 77 : « Elle n'est pas une preuve empirique du lemme ni du théorème sur des modèles réels ») ; la note de résultats aussi (l. 46).
- **Rien de ce qui est hors de portée** (l. 53-59) :
  - activations réelles (T0.4 à T0.7) ;
  - adversaire couvert de 2601.20022 ;
  - compensation pilotée par l'agent (L5) ;
  - invariance entre agents au même pas (L4) ;
  - variante (r, q) de T3 ;
  - robustesse du calibrage conforme à un décalage entre épisodes.
- **Rien sur la porte G0.**
  - Le préenregistrement de T0.3 ne nomme pas G0 (0 occurrence). La note de résultats, elle, rattache T0.3 au critère 5 (l. 3).
  - « Agrégateurs validés », au sens du critère 5, est une opérationnalisation à décider (D-G0-10, grille de lecture de G0 en brouillon).
  - Ce verdict fournit les faits ; il ne juge pas ce critère et ne franchit aucune porte.
- **Rien sur les « Conséquences » de la note de résultats** (l. 124-128) : détecteur de rupture dans l'agrégateur de G1, calibrage sur épisodes honnêtes entiers pour la garde de G1, N-003 et N-004. Ce sont des propositions de l'auteur. Les cellules de P3.4 et de P8 les appuient en simulation ; elles ne les décident pas.
- **Rien sur les sorties descriptives** : figures F1 à F6, et valeurs « descriptif, sans verdict » (l. 217-221).
- **Rien sur 2606.10456 au-delà de la somme**, à α = 0,05, dans la construction à marginale gaussienne. Je n'ai pas relu les pages du PDF citées par le préenregistrement (R7).
- **Aucun GO.** Ce verdict, non scellé, est remis à la session mère pour scellement, puis à Lazar.

## 10. Fichiers de travail

Dossier versé : `docs/verdicts/verdict-T0.3-simulation-lemme-theoreme-v1-fichiers-de-travail.tar`, sha256 `77df0693624e9e3ee70d24c35e129508eb33bc6d2033d0637d2c105b485c1afb`. Il n'est pas scellé, comme ce verdict. Les scripts n'importent aucun module du programme, sauf `reproduction_t03.py`, qui exécute le code du commit cité.

| fichier | rôle | sha256 |
|---|---|---|
| `recalcul_t03.py` | table A réécrite depuis le texte ; formes closes recalculées avec scipy (dont l'énumération de P4.3) ; comparaison cellule par cellule à `lecture.json` ; variances d'audit et sous-ensembles ; 54 valeurs imprimées | `d43a122a1539fa82c51a45753d8aa95a370360ff5cb10970851201a6063560b3` |
| `recalcul_t03_sorties.json` | 886 cellules, 0 écart ; marges par prédiction et par critère ; 54 valeurs imprimées égales sur 54 ; taux de P8 | `c5fe686732d9e3a545f2f214117b6edc45a9362aea7fb9efb05fc2318997ceca` |
| `verifs_run_t03.py` | graines (R9), rattachement au manifeste, garde de calibrage, garde d'équivalence, égalités au seuil de P1.1, champs du manifeste | `3db4bdad1def66eec45375dd911875039c64d946558dec4dedf8f71627603140` |
| `verifs_run_t03_sorties.json` | 3 280 graines, 0 écart ; 15 rattachements ; 92 contrôles de calibrage passés | `8896846f14bfdccb8f0a939bd718778bd566cc99bacc6d46339b17856c19e37a` |
| `reproduction_t03.py` | reproduction hors du dépôt des 13 fichiers bruts (section 3, point 9) | `c0978fc30c9f846dafbd4009aa75af959408a3b478d33b05c0b4bbba02873854` |
| `reproduction_t03_sorties.json` | empreintes reproduites et scellées : 13 égales sur 13 | `cf84fea233148903150b9eb455b94a9514fcd6cc4bb1b970a8fdda75ec852c91` |
| `reproduction_t03_journal.txt` | journal, avec la durée de chaque étape | `9f1fdc0599eb88b67afb497a821fed0bd277cea22f7b52e95346f25e636acba3` |

Pour rejouer : extraire le tar dans un dossier `<scripts>` hors du dépôt, puis lancer depuis la racine du dépôt, dans l'environnement de `requirements-cpu.txt` :
- `python -I <scripts>/recalcul_t03.py . <sortie.json>` ;
- `python -I <scripts>/verifs_run_t03.py . <sortie.json>` ;
- `python -I <scripts>/reproduction_t03.py <extrait> . <sortie.json>`, où `<extrait>` est un dossier vide rempli par `git archive d73ac46953c9482e745a10bfab0521f7c63789b8 src tests prereg/T0.3-grille-v2.json | tar -x -C <extrait>` (environ 7 minutes sur 4 cœurs).

---

Je n'ai écrit ni le préenregistrement de T0.3, ni son code, ni l'analyse (lecture gelée appliquée par le code, note de résultats), ni aucune des trois contre-lectures ; je ne les avais pas lus avant cette tâche. Ce verdict applique les critères gelés tels qu'ils sont écrits.
