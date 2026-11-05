# Audit de symétrie (R4) — notations refaites des juges 8B et 3B (pilote de T0.5) — v1

- **Compilateur** : sous-agent neuf. Il n'est ni relecteur ni recalculateur. Il n'a écrit ni les préenregistrements, ni le code d'analyse, ni les résultats, ni la lecture. Il reprend les deux rapports sans ajouter de chiffre.
- **État** : non scellé, à sceller. La lecture reste suspendue jusqu'au scellement (`lecture-juges.json` → `resultat.lecture_suspendue` vrai). Les deux rapports disent le dépôt non modifié (`git status` vide). Le compilateur fait le même constat.
- **Rapports sources**, hors dépôt, sous `/tmp/claude-0/-home-user-controle-ia-travail/adc77dcb-d0c4-5686-b269-a3ad7dc4b310/scratchpad/verdict-notations/` :
  - relecture : `relecture-audit-R4-notations-v1.md` (2b800d12…), avec `scripts/`, `sorties/`, `reponses/R01.txt` à `R10.txt` et `actions/A01.txt` à `A10.txt` ;
  - recalcul : `recalcul.py` (644692d3…), `sortie/recalcul.json` (ac0f115f…), `sortie/recalcul-sortie.txt` (0784da31…) ; explorations `explorer_anomalies.py`, `explorer_desaccords.py`, `explorer_validite.py`.
- **Pièces**, empreintes compagnon vérifiées par le compilateur (`sha256sum -c`), toutes conformes :
  - `prereg/T0.5-pilote-notations-v1.md` (66784ceb…) ; `prereg/T0.5-pilote-8B-v1.md` (9ce91ba1…) ;
  - `diag/20261017-193648-t05-notations-reel/` : `notations-8B-decisives.json` (b103835b…), `notations-3B-decisives.json` (51548526…), `resume.json` (994d542a…), sous `runs/20261017-193648-t05-notations-reel/manifeste.json` (9f143f7c…) ;
  - `diag/20261018-214028-t05-lecture-juges/lecture-juges.json` (d41c3f58…), sous `runs/20261018-214028-t05-lecture-juges/manifeste.json` (5349b231…) ;
  - `diag/20261012-105125-t05-pilote-reel/episodes.json` (45616303…) ; `diag/20261012-150724-t05-pilote-analyse/lecture.json` (396a7dff…), sous `runs/20261012-150724-t05-pilote-analyse/manifeste.json` (4b1a3fe1…) ;
  - `donnees/t05-pilote-v1/taches-pilote-60-v1.json` (287e8348…) ; invites `docs/sources/invites-2606.08892-v1/invites/H3.txt` (52ab1e25…) et `H4.txt` (cb103166…) ;
  - modèle de forme : `docs/verdicts/audit-R4-T0.5-pilote-v1.md` (f557402b…).

## 1. Déclencheur

`diag/20261018-214028-t05-lecture-juges/lecture-juges.json` → `resultat.audit_r4_juges` :
- `declenche` vrai ;
- liste « trop propre » vide ;
- liste « trop sale » : « juge 8B : décomposition impossible (0 tâches complètes : décomposition impossible) » et « juge 3B : décomposition impossible (2 tâches complètes : décomposition impossible) ».

**Règle en cause.** Préenregistrement du pilote, section « Audit de symétrie (R4) », liste « trop sale » : « décomposition impossible pour un juge (D-13) ». Le complément la définit (section « Métrique ») : moins de 3 tâches complètes, notes constantes, ou aucun tirage lisible. Ici, c'est le premier cas : moins de 3 tâches complètes.

**Condition de l'écart déclaré 2.** Le déclencheur ne joue que pour un juge écrit. Les deux juges sont « écrit » dans l'unique `resume.json` (`issue_des_notations` : fichier « resume »). La condition tient.

**Grandeurs**, lues dans `lecture-juges.json` et retrouvées par les deux rapports :

| | 8B | 3B |
|---|---|---|
| tâches complètes (A, B et C notées) | 0 | 2 (`2506.18862v3`, `2509.24912v2`) |
| réponses complètes | 54 sur 180 | 50 sur 180 |
| part des réponses incomplètes | 0,70 (126 sur 180) | 0,722 (130 sur 180) |
| réponses tronquées | 60 | 9 |
| part des réponses A et B identiques | 0,0 | 0,0 |
| règle du plan B (lecture) | plan B | plan B |

**Autres déclencheurs** :
- « plus de 10 % de réponses A et B identiques » : ne joue pas (0,0 pour les deux juges) ;
- « part du juge > 0,95, ou σ̂²_β ≤ 0, ou part illisible » et « part du juge < 0,05 » : non définis sans décomposition ;
- hors juges, aucun, selon le recalculateur : format 0,868 ; kappas de 0,043 à 0,172 ; probabilité du « oui » de 2,8 × 10⁻⁵ à 0,991 ; ensembles dont la couverture des contrôles vaut 0 ou 1 : 0,133 ;
- le déclencheur des familles (directions fécondes 0,930 > 0,9) joue toujours. Il est exclu par construction de `lecture-juges.json` (écart déclaré 1). L'audit R4 v1 scellé (f557402b…) et R-155 l'ont déjà traité.

## 2. Protocole suivi

Source : préenregistrement complémentaire, « Critères de lecture gelés », ligne « `audit_r4_juges.declenche` vrai ». Elle renvoie au protocole gelé du pilote, sans changement (`prereg/T0.5-pilote-8B-v1.md`, « Audit de symétrie (R4) », point « protocole »).

| étape gelée | exécution |
|---|---|
| relecture, tirée par graine, de 10 réponses de juge : exactement `relectures_audit.reponses_de_juge` | faite : les 10 réponses (6 du 3B, 4 du 8B), texte intégral lu, prises telles quelles par le relecteur |
| relecture, tirée par graine, de 10 actions : exactement `relectures_audit.actions` | faite : les 10 actions, texte intégral lu ; 6 seulement ont une notation de leur ensemble (4 sont en e2, non noté à cette étape) |
| contrôle du tirage (contenu dans « exactement ») | fait par le recalculateur : les 20 éléments sont reproduits à l'identique (générateur `analyse/audit` ; réponses d'abord, parmi 360 ; puis actions, parmi 1 800) ; aucune action commune avec l'audit v1, comme l'annonce le complément |
| recalcul indépendant par un sous-agent neuf | fait, par `.venv/bin/python -I`, sans importer aucun module du dépôt |
| lecture suspendue jusqu'au scellement de l'audit | en vigueur (`lecture_suspendue` vrai) |

Aucune étape gelée n'est omise. Aucun rapport ne signale d'écart au protocole.

## 3. Constats de la relecture

**Conclusion du relecteur** : le déclencheur « décomposition impossible » est réel.
- Il ne vient ni du lecteur ni de l'alignement. Les 360 notations attendues sont là, une fois chacune, aux bonnes empreintes.
- Il vient des réponses des juges tels que configurés :
  - le texte dégénère en suite de mots sans sens (8B : 98 réponses sur 180 ; 3B : 58 sur 180), d'où les troncatures ;
  - les échelles ne sont pas respectées (3B : 107 réponses hors échelle ; 8B : 47 réponses à notes non entières, surtout des demi-points).
- Le relecteur ne voit aucun signe d'artefact de calcul. Il ne peut pas l'exclure sans rejeu sur la carte.

**Ce que demande l'invite b0** (H.3 puis H.4) :
- être strict : « 3/5 ou 2/4 = travail compétent ; notes hautes rares » ;
- d'abord l'analyse, puis exactement dix lignes « NOM: <score> » et une ligne JUSTIFICATION.

Les échelles sont entières :
- 0 à 5 : SPECIFICITY, COHERENCE, COVERAGE ;
- 0 à 4 : FEASIBILITY, NOVELTY, RIGOR ;
- 0 à 3 : BALANCE, RESULT_REASONING ;
- −2 à 0 : les deux pénalités.

**Règle gelée du lecteur** :
- il prend la dernière occurrence de chaque nom, valeur sur la même ligne, nom en majuscules ;
- un demi-point, une valeur hors échelle ou un nom absent sont des anomalies ;
- une réponse sans jeton de fin est incomplète, même si dix notes s'y lisent.

**Les 10 réponses de juge** :

| # | réponse | constat | format | note fondée |
|---|---|---|---|---|
| R01 | `juge-3B/2506.17197v2/e0/passe-1` | notes en tête, au maximum partout (RIGOR 5, BALANCE 5, RESULT_REASONING 5) ; puis suite de mots sans sens jusqu'au plafond de 3 072 jetons | non conforme : ordre inversé, trois notes hors échelle, tronquée | non : contraire à la consigne « soyez strict » |
| R02 | `juge-3B/2507.11818v2/e0/passe-0` | notes en tête ; justification élogieuse ; ensemble générique, aucun jeu de données nommé dans les extraits lus | non conforme : ordre, trois notes hors échelle | non : notes gonflées |
| R03 | `juge-3B/2508.10631v2/e0/passe-0` | notes en tête ; justification générique, avec un « Senior Range » inventé | non conforme : ordre, deux notes hors échelle | non |
| R04 | `juge-3B/2510.23574v1/e0/passe-0` | notes en tête ; justification dégénérée dès la proposition 5 ; jeton de fin à 1 673 jetons ; FEASIBILITY 4 pour un plan qui réentraîne entièrement DALL-E 2 | non conforme : ordre, trois notes hors échelle | non |
| R05 | `juge-3B/2512.00930v1/e0/passe-1` | a lu l'ensemble ; dit les coûts « sous 10 heures de carte » alors qu'ils vont de 25 à 1 000 ; relève un recouvrement mais met REDUNDANCY à 0 | non conforme : ordre, une note hors échelle | en partie |
| R06 | `juge-3B/2602.07160v1/e0/passe-0` | justification répétitive ; reproche l'« absence d'ablations » alors que quatre propositions en prévoient ; COHERENCE 5 et COVERAGE 5 malgré ses propres critiques | non conforme : ordre, une note hors échelle | non |
| R07 | `juge-8B/2506.01290v2/e1/passe-0` | analyse fidèle ; REDUNDANCY −1 défendable ; FEASIBILITY 4 ; IRRELEVANCE 0 malgré une proposition sur MNIST, hors des séries temporelles | non conforme : une note hors échelle, justification avant le bloc | en partie |
| R08 | `juge-8B/2509.21513v3/e0/passe-0` | analyse sensée de la proposition 1, puis suite de mots sans sens jusqu'au plafond ; aucune note | illisible, tronquée | sans objet |
| R09 | `juge-8B/2510.05038v3/e0/passe-1` | seule réponse complète du tirage (somme 27 ; 81,8 sur 100) ; longues plages dégénérées ; textes de la grille presque recopiés ; « aucun point faible » | conforme mécaniquement ; fond en partie dégénéré | non : NOVELTY 4 non justifiée |
| R10 | `juge-8B/2604.12086v1/e0/passe-0` | résumé fidèle des huit propositions ; notes modérées ; petite incohérence sur la proposition 7 | non conforme : trois demi-points, rejetés par la règle gelée (« 3.0 » est lu) | oui, plausible |

**Bilan des 10 réponses** :
- notes lisibles par un humain : 9 sur 10 (toutes sauf R08) ;
- conforme à la lettre : 1 seule (R09), au texte en partie dégénéré ;
- notes fondées : 1 (R10) ; en partie : 2 (R05, R07) ; non : 6 ; sans objet : 1 ;
- les six réponses du 3B mettent leurs notes avant l'analyse, et chacune a au moins une note hors échelle ;
- texte dégénéré dans 4 réponses sur 10 (R01, R04, R08, R09), dont les deux tronquées.

**Les 10 actions** :

| # | action | statut (`episodes.json`) | constat | notation de son ensemble |
|---|---|---|---|---|
| A01 | `2506.05216v2/e2/0,7` | ajout valide | générique ; 12 000 heures de carte, invraisemblable | aucune (e2) |
| A02 | `2509.18350v2/e1/0,5` | ajout valide | vague ; 8 000 heures | 8B : dix notes entières, mais rejetées pour la casse (somme lue à la main : 23) ; note modérée, plausible. 3B : cinq notes hors échelle, gonflé |
| A03 | `2509.18350v2/e2/0,6` | invalide (révision sans numéro) | cohérent ; 5 000 heures | aucune (e2) |
| A04 | `2510.14562v1/e2/0,3` | invalide (révision sans numéro) | cohérent | aucune (e2) |
| A05 | `2510.18828v1/e0/0,5` | invalide, au plafond de 400 jetons | dégénère dès le champ COST ; absente de l'ensemble final | 8B : 16 au passage A, 26 au passage B, sur le même ensemble (constat brut, sans lecture). 3B : 27 (B) ; A hors échelle |
| A06 | `2510.21366v3/e1/0,6` | ajout valide | mécanisme flou ; 120 heures | complète pour les deux. 8B : 17, pénalités −1 et −1, plausible. 3B : 22, plus indulgent |
| A07 | `2512.02017v1/e0/0,4` | ajout valide | cohérent, générique | 8B : A tronquée ; B 22, plausible. 3B : A et B hors échelle, gonflé |
| A08 | `2601.21315v2/e0/0,9` | ajout valide | « 500 heures de carte pour l'analyse théorique » : incohérent | 8B : A tronquée ; B relève ce coût (remarque fondée), mais avec six demi-points. 3B : B 28, indulgent ; A hors échelle |
| A09 | `2602.07160v1/e2/0,4` | révision valide | ablations nommées | aucune (e2) |
| A10 | `2603.01762v1/e1/0,4` | ajout valide | « jusqu'à 50 % » sans appui ; 15 heures | 8B : tronquée, demi-points, NOVELTY 1, sévère. 3B : SPECIFICITY 5, BALANCE 4 hors échelle, non fondé |

**Bilan des 10 actions** :
- 4 sont en e2, non noté ; 3 sont invalides, hors de l'ensemble final. Le tirage des actions reste désaccordé avec les notations, comme à l'audit v1.
- A05 dégénère. Le même 8B, au même code et à la même température, dégénère donc aussi comme agent.
- Aucune action ne recoupe celles de l'audit v1.

**Vérifications mécaniques** (descriptives, hors des critères gelés, non opposables) :

*Alignement.* Par juge :
- 180 notations et 180 clés distinctes, égales aux clés attendues ;
- variante b0 partout ;
- les 180 empreintes égalent celles des ensembles finaux ;
- aucun ensemble vide.

L'hypothèse « ensembles non notés » est écartée.

*Fidélité du lecteur.* Une relecture indépendante, à la règle documentée, redonne les notes consignées pour 180 réponses sur 180, pour chaque juge. Certaines formes sont lisibles par un humain mais rejetées par la règle gelée :
- casse (« ## Specificity: 4 ») : 4 réponses du 8B, 1 du 3B ;
- valeur à la ligne suivant le nom : 1 réponse du 8B (`2506.16404v3/e0/passe-0`) ;
- « 2.0/3.0 » : 1 réponse du 8B, tronquée de toute façon.

*Défauts des réponses incomplètes* (une réponse peut en cumuler plusieurs) :

| défaut | 8B (126 incomplètes) | 3B (130 incomplètes) |
|---|---|---|
| tronquée (sans jeton de fin) | 60 | 9 |
| critère absent | 55 | 21 |
| demi-point ou décimale | 47 | 4 |
| hors échelle | 11 | 107 |
| échelle écrite autre (« /5 » sur un critère sur 4) | 7 | 1 |
| illisible | 7 | 1 |
| défaut unique | demi-point 26, absent 24, tronquée 20, hors échelle 5, illisible 2 | hors échelle 96, absent 13, demi-point 4, tronquée 2, autres 2 |

*Tâches complètes sous des lectures plus tolérantes.* Ce sont des contrefactuels descriptifs, pas une proposition de lecture (R1). Ramener une note hors échelle à la borne est artificiel.

| lecture | 8B : réponses / tâches | 3B : réponses / tâches |
|---|---|---|
| règle gelée | 54 / 0 | 50 / 2 |
| + troncature tolérée (dix notes lues) | 74 / 3 | 52 / 2 |
| + casse des noms (troncature exclue) | 58 / 0 | 51 / 2 |
| + valeur à la ligne suivante | 55 / 0 | 50 / 2 |
| + décimales et demi-points | 75 / 2 | 53 / 4 |
| formes lisibles (casse, ligne, décimales), troncature tolérée | 107 / 9 | 56 / 4 |
| + hors échelle ramené à la borne, troncature tolérée | 81 / 6 | 153 / 35 |
| toutes ces tolérances ensemble | 122 / 14 | 160 / 42 |

- Aucune lecture n'atteint 48 tâches complètes, le seuil gelé d'une décomposition concluante.
- Le passage de « impossible » (moins de 3 tâches) à « non concluant » dépend, lui, de la règle stricte.
- Pour le 8B, tolérer la troncature suffit (3 tâches). Pour le 3B, seules les notes hors échelle pèsent.

*Texte dégénéré.* Indicateur du relecteur, choisi après lecture : part des mots-outils anglais sur des fenêtres de 40 mots. Une réponse est dite dégénérée si deux fenêtres de suite sont à 8 % ou moins.
- 8B : 98 réponses sur 180, dont 59 des 60 tronquées et 19 des 54 complètes ;
- 3B : 58 sur 180, dont 8 des 9 tronquées et 13 des 50 complètes ;
- longueur médiane des réponses non tronquées : 1 046 jetons (8B), 599 (3B). La troncature suit la dégénérescence. Le plafond de 3 072 jetons n'est pas trop court pour un texte sain ;
- début estimé de la dégénérescence : médiane d'environ 410 jetons générés (8B) et 280 (3B). Position absolue sous 8 192 pour 98 sur 98 (8B) et 57 sur 58 (3B) ;
- remplissage à gauche, en médiane : 332 jetons pour les réponses dégénérées contre 337 pour les autres (8B) ; 286 contre 345 (3B) ;
- les lignes sans aucun remplissage dégénèrent aussi : 22 sur 38 (8B), 18 sur 38 (3B). Pas de motif net selon le rang dans le lot ;
- agent du pilote (même 8B, même `generer_lot`, température 1,0, plafond de 400 jetons) : 123 actions sur 1 800 dégénérées, dont 97 des 109 au plafond.

*Ordre.* Parmi les réponses qui portent une ligne SPECIFICITY, le 3B la met en tête, avant toute analyse, dans 152 cas sur 168. Le 8B, dans 1 cas sur 142.

*Notes des réponses complètes.* Sommes brutes de 11 à 28 pour le 8B (16 valeurs distinctes). De 19 à 28 pour le 3B (9 valeurs, surtout de 25 à 27). Pas de notes constantes.

**Réponse du relecteur à la question de l'audit** :
- *Artefact de mesure* :
  - ensembles non notés : écarté ;
  - lecteur qui rejette : écarté comme cause ;
  - juge qui sort du format : c'est le mécanisme immédiat. Mais c'est un comportement des juges, que la mesure enregistre correctement.
- *Artefact de calcul* : non établi.
  - Indices contre :
    - le code de tirage, lu, est correct : tirage sur tout le vocabulaire à température 1,0, un générateur par ligne, masque et positions explicites ;
    - la dégénérescence ne dépend pas du remplissage ;
    - elle commence bien avant la position 8 192 ;
    - elle touche deux modèles chargés séparément ;
    - elle touche aussi l'agent, dans un autre run, sur une autre instance ;
    - la garde d'équivalence en ligne du pilote est conforme (`lecture.json` : 99e centile maximal 0,132, contrôle négatif « conforme », 87 actions).
  - Limites :
    - cette garde couvre l'agent (contextes d'au plus 6 030 jetons, 400 jetons générés), pas les juges (jusqu'à environ 10 000 positions) ;
    - les pièces ne séparent pas une propriété du modèle d'un défaut du chemin de code commun aux deux juges et à l'agent.
- *Propriété réelle* : oui, pour les juges tels que configurés (modèle, invite b0, température 1,0, tirage sur tout le vocabulaire, plafond de 3 072 jetons).
  - Même complètes, les notes sont peu fondées. Le signal « trop sale » va donc au-delà de la seule complétude.
  - Supposé, non vérifié : la dégénérescence viendrait d'abord du tirage sans troncature à température 1,0 sur de longues sorties.

## 4. Constats du recalcul

**Conclusion du recalculateur : conforme.**
- Chaque grandeur recalculable égale `lecture-juges.json`.
- Pour les grandeurs reprises de la première lecture, l'écart est d'au plus 1,7 × 10⁻¹⁵ (ordre des sommes en virgule flottante).
- L'audit se déclenche bien pour les deux juges.
- Les deux juges sont en plan B par l'incomplétude (plus de 20 % de réponses incomplètes).

**Méthode** :
- `.venv/bin/python -I` (Python 3.13.16, numpy 2.4.6, la version du manifeste de lecture) ;
- aucun module du dépôt importé ;
- bornes de la rubrique lues dans l'invite scellée H.4 ;
- somme brute possible de −4 à 33.

**Tableau des écarts** :

| grandeur | recalcul | lecture | écart |
|---|---|---|---|
| 8B : tâches complètes ; réponses complètes | 0 ; 54 sur 180 | 0 ; 54 (`resume.json`) | 0 |
| 8B : part incomplète ; tronquées | 0,7 ; 60 | 0,7 ; 60 | 0 |
| 3B : tâches complètes ; réponses complètes | 2 ; 50 sur 180 | 2 ; 50 (`resume.json`) | 0 |
| 3B : part incomplète ; tronquées | 0,722222 ; 9 | 0,722222 ; 9 | 0 |
| part des réponses A et B identiques (8B ; 3B) | 0,0 ; 0,0 | 0,0 ; 0,0 | 0 |
| décomposition (8B ; 3B) | impossible (0 et 2 tâches, moins de 3) | null, « … décomposition impossible » | identique |
| décomposition concluante (8B ; 3B) | non ; non | non ; non | identique |
| règle du plan B (8B ; 3B) | plan B par l'incomplétude (0,70 et 0,72 > 0,2) | plan B ; plan B | identique |
| différence appariée | 0 tâche complète pour les deux juges : impossible | impossible, borne null | identique |
| « décomposition impossible » (trop sale) | 8B oui, 3B oui | 8B, 3B | identique |
| autres déclencheurs propres aux juges | non définis ; A et B identiques : non (0 et 0) | non listés | identique |
| `declenche` ; trop propre ; `lecture_suspendue` | vrai ; vide ; vrai | vrai ; vide ; vrai | identique |
| P1 ; P2 ; P3 ; P4 ; P5 ; P6 ; P7 | confirmée ; non concluant ; non concluant ; confirmée ; réfutée ; confirmée ; réfutée | idem | identique |
| P1 : part des actions valides | 0,868333 (1 563 sur 1 800) | 0,868333 | 0 |
| P4 : couverture des contrôles par ensemble | 0,324074 | 0,324074 | 0 |
| P5 : couverture des directions fécondes par ensemble | 0,929630 | 0,929630 | 2,2 × 10⁻¹⁶ |
| P6 : coût lu ; médiane du log10 du rapport à la référence | 0,937940 ; −0,180864 | 0,937940 ; −0,180864 | 0 ; 0 |
| P7 : kappa pondéré, contrôles ; directions | 0,171936 ; 0,047503 | 0,171936 ; 0,047503 | 1,7 × 10⁻¹⁵ ; 2 × 10⁻¹⁷ |
| 10 réponses ; 10 actions tirées par graine | reproduites à l'identique | `relectures_audit` | identique |

**Concordances** :
- **Sceaux.** Les sceaux compagnons sont conformes : les deux préenregistrements, les deux configurations, les tâches, les épisodes, l'appariement, l'arrêt du pilote, les deux fichiers de notations, `resume.json`, `lecture.json`, les étiquettes, l'échantillon d'étiquetage, `lecture-juges.json`, les quatre manifestes et l'invite H.4.
- **Rattachements.** Ils sont conformes. Le run des notations a une seule issue : `resume.json`, sans `arret.json`, avec les deux juges « écrit ». L'empreinte canonique de la configuration est retrouvée (b3d24dec…). Les graines de la lecture égalent celles du manifeste de la première analyse ; leurs états sont rejoués par `SeedSequence`.
- **Alignement.** Chaque juge a 180 clés, chacune une fois. L'empreinte de chaque ensemble noté égale le sha256 de e0 (pour A et B) ou de e1 (pour C). Aucun ensemble décisif n'est vide.
- **Complétude recalculée sur le texte brut.** Elle est identique au fichier pour les 360 réponses. « Tronquée » coïncide exactement avec 3 072 jetons de réponse. La règle retrouvée :
  - on prend la dernière ligne « CRITÈRE: valeur » ;
  - « 3.0 » est accepté, « 2.5 » est illisible ;
  - une échelle écrite « /5 » sur un critère sur 4 rend la note illisible ;
  - une note hors des bornes rend la réponse incomplète.
- **Pourquoi les tâches ne sont pas complètes** :
  - 8B : il manque trois lettres pour 22 tâches, deux pour 22, une pour 16. Réponses complètes : A 18, B 19, C 17 ;
  - 3B : il manque trois lettres pour 26 tâches, deux pour 20, une pour 12. Réponses complètes : A 14, B 19, C 17.
- **Pourquoi les réponses ne sont pas complètes** :
  - 8B (126 réponses) : 60 tronquées. Parmi les 66 autres : 28 n'ont que des notes illisibles (demi-points, décimales « 2.8 (out of 5) »), 24 n'ont que des notes absentes, 14 mêlent ces motifs ;
  - 3B (130 réponses) : 9 tronquées. 96 seulement hors bornes, surtout des 4 ou 5 sur des échelles de 0 à 3 ou de 0 à 4 (RESULT_REASONING 71 fois, BALANCE 66, RIGOR 32). 13 à notes absentes. 12 mêlent les motifs.
- **Les deux tâches complètes du 3B**, sommes brutes (A, B, C) : `2506.18862v3` (27, 25, 26) ; `2509.24912v2` (27, 22, 27).
- **Tirage des relectures**, reproduit exactement : générateur `analyse/audit`, puis `choice(n, 10, replace=False)` sur la population triée, résultat trié. On tire d'abord parmi les 360 réponses, puis parmi les 1 800 actions. La même procédure redonne les 10 actions de la première lecture, quand aucune réponse n'existait.

**Divergences.** Aucune sur les nombres. Deux points de forme et un de provenance, sans effet :
- le champ `score` des fichiers de notations est sur l'échelle sur 100 (100 × somme brute / 33, exact pour les 104 réponses complètes). Le recalcul utilise la somme brute. Ici, ce choix ne change rien ;
- le libellé « trop sale » répète « décomposition impossible » dans la parenthèse. Le contenu est le même ;
- le manifeste des notations porte le commit `b604164`. Le complément et `resume.json` (`commit_cite`) citent `c63d4f1`, qui n'est pas un ancêtre de `b604164` dans l'historique local. Pourtant :
  - `src/`, `tests/` et `scripts/` sont identiques entre les deux commits ;
  - `lire_pilote.py` est identique entre `2660b07` et `9c7dcef` ;
  - les deux modules neufs sont identiques entre `b604164` et `9c7dcef`.

**Sensibilité.** Avec la dernière occurrence lisible au lieu de la dernière occurrence :
- 8B : 54 réponses complètes, 0 tâche ;
- 3B : 52 réponses complètes, 2 tâches.

La décomposition impossible et le plan B par l'incomplétude ne tiennent donc pas au choix d'analyse du texte.

**Non recalculé** :
- σ²_ε, σ²_β, σ²_δ, les parts, leurs intervalles, la sensibilité sur 100 et la différence appariée : décomposition impossible ;
- la part illisible et les déclencheurs « part > 0,95 », « σ̂²_β ≤ 0 », « part < 0,05 » : non définis ;
- la clause de P7 « directions > contrôles avec intervalle apparié au-dessus de 0 ». Elle ne change pas le statut : P7 est déjà réfutée par « contrôles < 0,4 », et directions (0,048) < contrôles (0,172) ;
- les intervalles par rééchantillonnage de la première lecture : non exigés.

**Concordance des deux rapports.** Les comptes se recoupent :
- réponses complètes 54 et 50 ; incomplètes 126 et 130 ; tronquées 60 et 9 ;
- tâches complètes 0 et 2, aux mêmes identifiants ;
- alignement 180 sur 180 ;
- même règle du lecteur (« 3.0 » lu, demi-point rejeté) ;
- même motif dominant pour le 3B : 96 réponses au seul motif hors échelle ;
- mêmes réponses à notes seulement absentes : 24 pour le 8B, 13 pour le 3B.

Le relecteur a pris le tirage tel quel ; le recalculateur l'a reproduit. Les lectures tolérantes du relecteur et la sensibilité du recalculateur mènent au même point : aucune n'approche 48 tâches.

## 5. Conclusion de l'audit

| question | constat | statut |
|---|---|---|
| déclencheur fondé | comptes retrouvés par les deux rapports ; recalcul conforme | **établi** |
| artefact de mesure : ensembles non notés ou désalignés | 180 clés par juge, empreintes égales à celles de e0 et e1, aucun ensemble vide | **écarté** |
| artefact de mesure : lecteur qui rejette à tort | lecteur fidèle à sa règle (180 sur 180 par juge) ; rejets de forme (casse, ligne suivante) sur 5 réponses du 8B et 1 du 3B ; aucune lecture tolérante n'approche 48 tâches ; même conclusion sous la sensibilité du recalcul | **écarté comme cause**. Nuance : l'étiquette « impossible » plutôt que « non concluant » tient à la règle stricte, gelée et motivée (CL-9). Pour le 8B, tolérer la troncature donnerait 3 tâches |
| artefact de calcul de la lecture | recalcul indépendant conforme, sans le code du dépôt | **écarté** |
| artefact du chemin de génération sur la carte | indices contre : code de tirage lu, correct ; dégénérescence indépendante du remplissage, bien avant la position 8 192, sur deux modèles, et chez l'agent. Garde d'équivalence du pilote limitée à l'agent | **non établi, non exclu** : seul un rejeu sur la carte trancherait |
| propriété réelle des juges tels que configurés | 3B : 107 réponses hors échelle, notes avant l'analyse (152 sur 168) ; 8B : 47 réponses à notes non entières ; dégénérescence : 98 et 58 réponses sur 180 ; réponses complètes peu fondées, selon le relecteur | **établie sur pièces** pour l'échelle, les notes non entières et la dégénérescence ; cause profonde **supposée** |

**Établi** :
- le déclencheur « décomposition impossible » est réel pour les deux juges ;
- son mécanisme immédiat est le comportement des juges : réponses tronquées, notes hors échelle, notes non entières, notes absentes. La mesure l'enregistre correctement ;
- l'alignement, le lecteur et le calcul de la lecture ne sont pas en cause.

**Non établi** :
- la cause profonde : réglages de tirage (température 1,0, tout le vocabulaire, sorties longues), ou défaut d'un chemin de code commun aux deux juges et à l'agent ;
- l'effet d'un tirage par noyau (« top-p ») ou d'une température plus basse : supposé par le relecteur ;
- ce que fait l'annexe C.1 de 2606.08892 : non relue sur PDF (R7) ;
- la qualité des notes au-delà des 10 réponses tirées : « note fondée » est le jugement d'un seul relecteur, sur extraits, sans étalon.

L'audit ne propose aucun changement de règle de lecture : les lectures tolérantes sont des contrefactuels descriptifs. Ce rapport ne prononce aucun verdict de porte ni de lecture.

## 6. Ce que l'audit ne tranche pas

**Laissé au verdict R13 complémentaire** (sous-agent neuf ; `docs/verdicts/verdict-T0.5-pilote-notations-v1.md`), une fois l'audit scellé :
- appliquer les critères gelés à `lecture-juges.json` :
  - la règle du plan B de chaque juge : la lecture porte « plan B », par l'incomplétude ;
  - la ligne « nœud de décomposition (… décomposition impossible) : proposition à Lazar » ;
  - la combinaison des deux. Pilote, section « Seuil » : « Une décomposition impossible donne de même plan B par l'incomplétude, sinon nœud (D-13) » ;
  - P2 et P3 « non concluant » ;
- dire si les constats de l'audit changent ou non une lecture gelée : propriété réelle établie, chemin de génération non exclu ;
- apprécier la provenance du commit : `b604164` au manifeste, `c63d4f1` au complément et dans `resume.json`, sans lien d'ascendance dans l'historique local. Le recalculateur établit l'identité des arbres. Ce n'est pas une identité de commit.

**Laissé à Lazar** (nœuds) :
- la cause profonde : seul un rejeu sur la carte séparerait une propriété du modèle d'un défaut du chemin de code commun. C'est un nœud et une dépense ;
- tout changement de réglage des juges (température, tirage par noyau, plafond, invite) : ce serait un écart au préenregistrement, à décider par Lazar ;
- la suite du plan B : l'audit ne dit pas si une rubrique simplifiée, aux mêmes réglages, éviterait la dégénérescence. Celle-ci touche aussi l'agent (123 actions sur 1 800), hors de toute rubrique ;
- le tirage des actions reste désaccordé avec les notations : 4 actions sur 10 en e2, 3 invalides, comme à l'audit v1. C'est un effet du code gelé `tirer_relectures`.

**Réserves** (reprises des deux rapports) :
1. **Indicateur de dégénérescence** : fait par le relecteur, non préenregistré, seuil fixé après lecture de cinq réponses. Il peut rater un texte fluide mais faux, ou compter à tort un long bloc de notes. Descriptif seulement.
2. **Début de la dégénérescence** : estimé par la part du texte, sans tokeniseur. Ordre de grandeur seulement.
3. **Ensembles lus par extraits** : titre, 260 premiers caractères, contrôles, coût, prédiction. Seules les actions tirées sont lues en entier.
4. **Tirage désaccordé** : six actions seulement ont une notation de leur ensemble.
5. **Contrefactuels de lecture** : des comptes seulement, sans décomposition ni part calculée. Ils ne proposent aucun changement de règle (R1).
6. **Chemin de génération** : non exclu, faute de rejeu. La garde d'équivalence citée est lue dans `lecture.json`, non recalculée. Elle ne couvre pas la plage des juges.
7. **Faits extérieurs** cités de mémoire par le relecteur, non vérifiés : poids de DALL-E 2 non publics ; nature d'AutoARIMA, de Prophet et de MNIST ; ressources « Casanova », « LSusat-Sentence », « BenchX » peu identifiables. Aucun ne porte un compte.
8. **Fichiers de travail du relecteur** : `sorties/descriptifs.txt` porte une première version, plus souple, de ses lectures tolérantes. Les chiffres retenus viennent de `sorties/variantes.txt` et de `sorties/controles2.txt`.
9. **Non recalculé** : composantes, parts, intervalles, sensibilité sur 100, différence appariée (décomposition impossible) ; une clause de P7, sans effet ; intervalles de la première lecture (non exigés).
