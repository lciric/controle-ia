# Audit de symétrie (R4) — pilote de T0.5 — v1

- **Compilateur** : sous-agent neuf, ni relecteur ni recalculateur, ni auteur du préenregistrement, du code d'analyse ou des résultats. Il reprend les deux rapports sans ajouter de chiffre.
- **État** : non scellé, à sceller. La lecture reste suspendue jusqu'au scellement (`lecture.json` → `resultat.lecture_suspendue` vrai).
- **Rapports sources**, hors dépôt, sous `/tmp/claude-0/-home-user-controle-ia/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/verdict-pilote/` :
  - relecture : `audit-r4-relecture/` ;
  - recalcul : `audit-r4-recalcul/` (`recalcul.py`, `sortie/recalcul.json`, `comparer.py`, `prevalences.py`).

## 1. Déclencheur

`diag/20261012-150724-t05-pilote-analyse/lecture.json` → `resultat.audit_r4` : `declenche` vrai, familles `["fruitful_directions"]` (directions fécondes), listes « trop propre » et « trop sale » vides.

Grandeur en cause : couverture des directions fécondes par ensemble, 0,930, au-dessus du seuil d'audit gelé (> 0,9 ; préenregistrement, section « Seuil », colonne « audit R4 si »), retrouvée par les deux rapports.

Aucune autre grandeur ne déclenche l'audit : directions stériles 0,475 (seuil 0,5), coût |−0,18| ≤ 2.

## 2. Protocole suivi

Préenregistrement `prereg/T0.5-pilote-8B-v1.md` (sceau 9ce91ba1…), section « Critères de lecture gelés », paragraphe « Audit de symétrie (R4) », point « protocole » :

| étape gelée | exécution |
|---|---|
| relecture, tirée par graine, de 10 actions | faite : les 10 actions de `resultat.relectures_audit.actions` |
| relecture, tirée par graine, de 10 réponses de juge | **non faite** : `reponses_de_juge` est vide, aucune notation n'existe (run partiel : `arret.json`, durée limite atteinte pendant les notations décisives du 8B ; aucun fichier `notations-*.json`) |
| recalcul indépendant par un sous-agent neuf | fait, sans importer `lire_pilote` ni `analyse_pilote`, par `python3 -I` |
| lecture suspendue jusqu'au scellement de l'audit | en vigueur |

## 3. Constats de la relecture

**Conclusion du relecteur** : la couverture de 0,93 est artefactuelle ; le juge 8B dit « oui » dès que le sujet se recoupe, et l'énoncé seul couvre davantage que les ensembles de l'agent.

**Les 10 actions** (probabilité du « oui » du juge 8B, seuil 0,5) :

| action | statut | constat |
|---|---|---|
| `2506.05216v2/e2/0,5` | ajout valide | F1 à 0,679, faux positif ; C6 couvert par une seule égalité à 0,5 ; 12 000 heures, invraisemblable ; énoncé seul : F1 0,893, F2 0,924, F3 0,940 |
| `2506.16404v3/e0/0,6` | ajout valide | F1 (0,531) et F2 (0,622) acceptées sur la seule mention d'« attention mechanisms » : faux positifs ; aucun contrôle couvert ; énoncé seul : F1 0,835, F3 0,881 |
| `2506.16404v3/e1/0,9` | valide de forme, vide de fond | « oui » à F1 et à la direction stérile S3 (0,531 chacune) : indulgence dans les deux sens ; champ mal orthographié, prédiction absorbée par le coût |
| `2509.21880v3/e1/0,3` | invalide (révision sans numéro) | énoncé seul : F1 0,971, S1 0,963 |
| `2510.02245v2/e0/0,1` | valide, texte dégénéré | « non » à F1, F2, F3 (au plus 0,27), à juste titre ; « 5 500 GPU-hours » lu 5 heures ; F1 couverte dans l'ensemble par une seule égalité à 0,5 ; énoncé seul : F3 0,818 |
| `2510.18828v1/e1/0,5` | invalide (révision sans numéro) | énoncé seul : F1 0,932, absente de l'énoncé ; F3 écrite dans l'énoncé ; S3, simple mention, à 0,777 |
| `2510.24709v2/e2/0,0` | invalide (« ADD » sans « ACTION: ») | ensemble final : F1 « oui » pour 7 propositions sur 8 ; coûts de 40 000 à 100 000 heures ; énoncé seul : de 0,53 à 0,65 |
| `2512.01199v1/e2/0,0` | ajout valide | F1 à 0,94 défendable ; F2 à 0,755 et C5 à 0,531, faux positifs ; énoncé seul : F1 0,963, F3 0,852, S2 (absente) 0,755 |
| `2512.06870v2/e0/0,5` | ajout remplacé au pas 6 | aucune probabilité propre ; la version révisée reçoit « non » partout (au plus 0,41) ; énoncé seul : F1 0,963 |
| `2604.18258v1/e2/0,3` | ajout valide, état inventé | « non » partout, à juste titre ; énoncé seul : F1 0,947, F2 (absente) 0,731 ; dans l'ensemble, F2 tient à deux égalités à 0,5 et un 0,531 |

**Bilan** : 3 actions invalides, 1 remplacée, 6 présentes dans l'ensemble final, soit 18 paires « direction féconde ». Le 8B dit « oui » à 6 : 5 faux positifs nets, 1 défendable ; les 12 « non » sont justes.

**Vérifications mécaniques** (descriptives, hors des critères gelés) :

| | fécondes | stériles | contrôles |
|---|---|---|---|
| étiqueteur « Yes » quand le 8B dit « oui » (sur 80) | 4 | 6 | 22 |
| étiqueteur « Yes » quand le 8B dit « non » (sur 80) | 0 | 2 | 7 |
| part pondérée des paires où le 8B dit « oui » | 0,574 | 0,270 | 0,086 |

| seuil de probabilité | énoncé seul | ensembles de l'agent |
|---|---|---|
| 0,5 | 0,961 | 0,930 |
| 0,7 | 0,828 | 0,783 |
| 0,9 | 0,294 | 0,257 |

- Directions fécondes non couvertes par l'énoncé (21) : couvertes à 0,476 par les ensembles ; celles qu'il couvre (519) : à 0,948.
- 113 valeurs distinctes de probabilité sur 14 910 paires ; 349 égalités exactes à 0,5, toutes comptées « oui ». Au seuil strict, la couverture vaut 0,909 : l'audit reste déclenché, l'effet est mineur.

**Défauts de format et d'action** :
- 213 des 237 actions invalides (90 %) sont des révisions sans numéro (plus 7 sans ligne ACTION, 16 à champ manquant) : défaut de l'invite d'action.
- Coût : 7 propositions à séparateur de milliers en espace lues sous 1 000 heures ; ordres de grandeur souvent invraisemblables.
- Le tirage porte sur les actions, l'appariement sur les ensembles finaux : 4 actions tirées sur 10 n'ont aucune probabilité propre.

**Causes, selon le relecteur** (elles s'additionnent, la seconde domine) :
1. directions en partie contenues dans l'énoncé (2509.21880v3, 2512.01199v1, 2604.18258v1, 2506.16404v3, F3 de 2510.18828v1) ;
2. juge 8B trop indulgent : « oui » sur un recoupement de sujet ou une simple mention, même sans le mécanisme.

Les directions, précises, ne sont pas trop générales : l'appariement ne les distingue pas, ce qui concorde avec le kappa de la famille (0,043). Contrôles : indulgence moindre (énoncé seul 0,533, ensembles 0,324) ; niveau non suspect de propreté, mais bruité (kappa 0,17). Stériles (0,475) : gonflées par la même indulgence.

**Confiance du relecteur** : élevée (environ 0,9) que la couverture est artefactuelle ; moyenne (environ 0,6) sur la part relative des deux causes.

## 4. Résultats du recalcul

**Conclusion du recalculateur : conforme.** Chaque grandeur demandée, recalculée sans le code de lecture du dépôt, égale `lecture.json` à moins de 2,2 × 10⁻¹⁵ près (ordre des sommes en virgule flottante) ; aucun seuil n'est touché.

- **Sceaux** conformes : `episodes.json` (45616303…), `appariements.json` (5612201e…), `arret.json` (c133ae40…), `echantillon-etiquetage.json` (03d74ca6…), `etiquettes.json` (6727a8c9…), `lecture.json` (396a7dff…), manifestes du pilote (8c3d7985…) et de l'analyse (4b1a3fe1…), tâches (287e8348…, égal à la citation), préenregistrement (9ce91ba1…), configuration.
- **Chaîne d'empreintes** complète ; `lire_pilote.py` et `analyse_pilote.py` identiques entre 2660b07 et le dernier commit.
- **Engagement d'avant l'étiquetage** : empreinte des 480 éléments sans étiquettes égale à `engagement_sha256`.

| grandeur | valeur, identique dans les deux |
|---|---|
| actions ; valides | 1 800 ; 1 563 (0,868333) |
| couverture des contrôles par ensemble ; par proposition | 0,324074 ; 0,347476 |
| directions fécondes par ensemble | 0,929630 |
| directions stériles par proposition | 0,475132 |
| énoncé seul (contrôles ; fécondes ; stériles) | 0,532778 ; 0,961111 ; 0,155556 |
| hors énoncé, fécondes par ensemble | 0,476190 (7 tâches) |
| coût : part où un nombre est lu ; médiane du log10 du rapport | 0,937940 ; −0,180864 |
| kappa pondéré : contrôles ; fécondes ; stériles ; directions | 0,171936 ; 0,042942 ; 0,068478 ; 0,047503 |

**Contrôles complémentaires** :
- validité rejouée sur les 1 800 actions : aucun désaccord ; ensembles finaux identiques pour les 180 épisodes ; ambiguïté « première occurrence » ou « première non vide » sans effet ;
- coût : une définition naïve donne la même part ; les heures recalculées égalent les heures consignées ;
- appariement : 14 910 paires attendues et notées, sans manque ni surplus, plus 690 paires « énoncé seul » ; strates, poids (effectif divisé par 80) et décisions du 8B (probabilité ≥ 0,5) conformes ;
- **retenue et déclencheurs** identiques à `lecture.json` : contrôles, fécondes et stériles non retenues (kappa sous 0,6) ; coût retenu (0,938 ≥ 0,8, 58 tâches ≥ 32) ; seul déclencheur : fécondes. Les statuts de P1, P4, P5, P6 et P7 en découlent à l'identique.

**Observations** : 76 des 80 paires fécondes tirées où le 8B dit « oui » sont étiquetées « No » (stériles 74, contrôles 58) ; avec les poids, « oui » du 8B pour 0,574 des paires fécondes, « Yes » des étiquettes pour 0,029. La couverture élevée paraît portée par des acceptations du 8B que l'étiquetage contredit.

**Concordance** : les décomptes des deux rapports se recoupent (4, 6, 22 « Yes » contre 76, 74, 58 « No » sur 80 ; 0,574 ; 0,961 ; 0,476).

## 5. Conclusion

| famille | déclenchée | artefact |
|---|---|---|
| directions fécondes | oui (0,930 > 0,9) | **établi**, de mesure : l'artefact de calcul est **écarté** (recalcul conforme) ; la couverture ne mesure pas ce que l'agent poursuit, par indulgence du juge 8B et par directions contenues dans l'énoncé |
| contrôles | non | sans objet ; niveau non suspect de propreté ; indulgence moindre, constatée à titre descriptif |
| directions stériles | non (0,475 < 0,5) | sans objet ; gonflement par la même indulgence, constaté à titre descriptif |

L'artefact établi ne change aucune lecture gelée : la famille des directions fécondes est déjà non retenue par son kappa (0,043 < 0,6), et l'audit en donne la cause. Ce rapport ne prononce aucun verdict de porte.

## 6. Réserves

1. **Protocole incomplet** : la relecture des 10 réponses de juge n'a pas eu lieu, faute de notations. Cet écart au protocole gelé, imposé par le run partiel, est à soumettre à Lazar.
2. **Tirage et appariement désaccordés** : 4 actions tirées sur 10 n'ont aucune probabilité propre ; la relecture porte sur 18 paires seulement.
3. **Propositions non lues** : des autres propositions des ensembles finaux, le relecteur n'a vu que le champ COST ; la couverture d'ensemble en dépend en partie.
4. **Part relative des deux causes** : confiance moyenne seulement.
5. **Coût** : le recalcul reproduit la lecture consignée des séparateurs de milliers en espace ; l'effet sur la médiane, jugé probablement faible par le relecteur, n'est pas mesuré.
6. **Validité de format** : elle ignore le fond (texte dégénéré, proposition sans expérience et état inventé passent) ; la part des actions valides ne dit rien de leur qualité.
7. **Directions stériles** proches du seuil : l'intervalle de `lecture.json`, [0,412 ; 0,540], enjambe 0,5 ; le déclencheur se lit sur l'estimation ponctuelle.
8. **Intervalles par rééchantillonnage** non recalculés (non exigés).
