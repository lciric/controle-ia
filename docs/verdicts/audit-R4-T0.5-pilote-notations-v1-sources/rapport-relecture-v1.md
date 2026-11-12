# Audit de symétrie (R4) — notations refaites des juges 8B et 3B (T0.5, pilote) — rapport du relecteur — v1

Rapport écrit dans `/tmp/claude-0/-home-user-controle-ia-travail/adc77dcb-d0c4-5686-b269-a3ad7dc4b310/scratchpad/verdict-notations/relecture-audit-R4-notations-v1.md` (sha256 `2b800d120e6cf6030b5243b698b551983c43d013fb620f5eb631fd317c0db7ab`).

- **Rôle** : relecteur du protocole gelé (« relecture des 10 réponses de juge et des 10 actions tirées par graine »). Sous-agent neuf. Je n'ai écrit ni les préenregistrements, ni le code, ni les résultats, ni la lecture. Je ne suis ni recalculateur ni compilateur.
- **État** : rapport de travail, hors dépôt, non scellé. Dépôt en lecture seule : aucun fichier écrit, aucune commande git qui écrit (arbre propre après coup).
- **Dossier** : `/tmp/claude-0/-home-user-controle-ia-travail/adc77dcb-d0c4-5686-b269-a3ad7dc4b310/scratchpad/verdict-notations/` (`scripts/`, `sorties/`, `reponses/R01.txt` à `R10.txt`, `actions/A01.txt` à `A10.txt`). Scripts lancés par `python3 -I`, sans importer aucun module du dépôt.

## 0. Verdict de la relecture

Le déclencheur « décomposition impossible » est **réel**.

Il ne vient ni du lecteur ni de l'alignement. Le lecteur applique fidèlement sa règle gelée. Les 360 notations attendues sont là, une fois chacune, aux bonnes empreintes.

Il vient **des réponses des juges tels que configurés** :
- texte qui dégénère en suite de mots sans sens (8B : 98 réponses sur 180 ; 3B : 58 sur 180), d'où les troncatures ;
- échelles non respectées (3B : 107 réponses hors échelle ; 8B : 47 réponses à notes non entières, surtout des demi-points).

Je n'ai vu **aucun signe d'artefact de calcul**. Je ne peux pas l'exclure sans rejouer sur la carte.

## 1. Pièces lues (empreintes compagnon vérifiées par `sha256sum -c`, toutes conformes)

| pièce | sha256 |
|---|---|
| `prereg/T0.5-pilote-notations-v1.md` (lu en entier) | `66784ceb9c93f699b211fa26a142a8e64e1cccbc2c2fb3479df559f297c474f6` |
| `prereg/T0.5-pilote-8B-v1.md` (sections « Métrique », « Seuil », « Critères de lecture gelés », « Audit de symétrie (R4) ») | `9ce91ba16108635e917910e67cc199ac2dc31a76d76c7de8408c3ed457110590` |
| `diag/20261017-193648-t05-notations-reel/notations-8B-decisives.json` | `b103835bcd3bfc3117a53e335be6f37a1259102cc2a2a134acfc6e114cb3f1c4` |
| `diag/20261017-193648-t05-notations-reel/notations-3B-decisives.json` | `51548526c7590231b76473c2b4c9e619a092616b5f948830e735c466b037adab` |
| `diag/20261017-193648-t05-notations-reel/resume.json` | `994d542aafd224fc9347b2186979916c3e0a799c6edbefa28a7c9d6e972f44fc` |
| `runs/20261017-193648-t05-notations-reel/manifeste.json` (rattache les trois fichiers ci-dessus) | `9f143f7c1c9fd9d75f21807a0fa41035ae7110abe686fc7819130d3f6b435d38` |
| `diag/20261018-214028-t05-lecture-juges/lecture-juges.json` | `d41c3f585d9f2b89611dca0b40a6ced9d83e1004f140cbdadc0629f7e58695e4` |
| `runs/20261018-214028-t05-lecture-juges/manifeste.json` (rattache la lecture) | `5349b2316518f6c3e1aed6f69dd8e3c63b5b72f7cbc2072de308a2628e27f198` |
| `diag/20261012-105125-t05-pilote-reel/episodes.json` (textes des actions, ensembles finaux) | `45616303dc740b66c42095cd5317a8ddd63e89123e64dd86490e43429c7cd15c` |
| `diag/20261012-150724-t05-pilote-analyse/lecture.json` | `396a7dff8348a0aff7d9e3bde25b0d054919d2395aee3868b9058c974005c38d` |
| `donnees/t05-pilote-v1/taches-pilote-60-v1.json` (énoncés) | `287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5aa` |
| `docs/sources/invites-2606.08892-v1/invites/H3.txt` et `H4.txt` (invite b0 ; index scellé conforme) | `52ab1e25…`, `cb103166…` |
| `docs/verdicts/audit-R4-T0.5-pilote-v1.md` (modèle de forme) | `f557402b90d1fea33e669295fdeecd835477b3244ca4ebdc256787a44c6071b8` |

Code lu, sans l'exécuter :
- `rubrique.py`, au commit `2660b07` ;
- au commit `c63d4f1` : `juges.py`, `pilote_a.py` (`noter_ensembles`), `harnais/episode.py` (`generer_lot`), `lancer_pilote_a.py` (chargement), `lire_pilote.py` (`tirer_relectures`).

## 2. Déclencheur

`lecture-juges.json` → `resultat` :
- `audit_r4_juges.declenche` vrai ; `trop_propre` vide ;
- `trop_sale` : « juge 8B : décomposition impossible (0 tâches complètes) », « juge 3B : décomposition impossible (2 tâches complètes) » ;
- 8B : 0 tâche complète ; 126 réponses incomplètes sur 180 (0,70) ; 60 tronquées ;
- 3B : 2 tâches complètes (`2506.18862v3`, `2509.24912v2`) ; 130 incomplètes sur 180 (0,722) ; 9 tronquées ;
- `lecture_suspendue` vrai.

Je retrouve ces comptes sur les fichiers de notations.

**Ce que demande l'invite b0 (H.3 puis H.4) :**
- être strict : « 3/5 ou 2/4 = travail compétent ; notes hautes rares » ;
- d'abord l'analyse, puis **exactement** dix lignes « NOM: <score> » et une ligne JUSTIFICATION.

Échelles :
- 0 à 5 : SPECIFICITY, COHERENCE, COVERAGE ;
- 0 à 4 : FEASIBILITY, NOVELTY, RIGOR ;
- 0 à 3 : BALANCE, RESULT_REASONING ;
- −2 à 0 : les deux pénalités.

Les repères de la grille sont entiers.

**Règle gelée du lecteur :**
- il prend la dernière occurrence de chaque nom, valeur sur la même ligne, nom en majuscules ;
- un demi-point, une valeur hors échelle ou un nom absent sont des anomalies ;
- une réponse sans jeton de fin est incomplète, même si dix notes s'y lisent.

## 3. Les 10 réponses de juge (texte intégral lu)

| # | réponse | ce que le juge a répondu | lisible ? conforme au format ? | note fondée au vu de l'ensemble ? |
|---|---|---|---|---|
| R01 | `juge-3B/2506.17197v2/e0/passe-1` | Bloc de notes **en tête** : 4, 5, 5, 4, 4, RIGOR 5, BALANCE 5, RESULT_REASONING 5, 0, 0. Deux phrases, puis suite de mots sans sens jusqu'au plafond de 3 072 jetons. | Notes lisibles. Non conforme : ordre inversé, trois notes hors échelle, réponse tronquée. | Non. Notes au maximum partout, sans analyse préalable, contre la consigne « soyez strict ». |
| R02 | `juge-3B/2507.11818v2/e0/passe-0` | Bloc en tête : 3, 4, 5, 3, 4, RIGOR 5, BALANCE 4, RESULT_REASONING 5, 0, 0. Justification cohérente, élogieuse (« exceptional specificity »). | Lisible. Non conforme : ordre, trois notes hors échelle. | Non. L'ensemble propose des architectures génériques (« TemplateGAN », réseau convolutif sur graphes, autoencodeur). Dans les extraits lus, aucun jeu de données nommé. Notes gonflées. |
| R03 | `juge-3B/2508.10631v2/e0/passe-0` | Bloc en tête : 4, 4, 4, 4, 3, 4, BALANCE 4, RESULT_REASONING 4, 0, 0. Justification générique ; conclut sur un « Senior Range » inventé. | Lisible. Non conforme : ordre, deux notes hors échelle. | Non. Aucun modèle ni jeu de données nommé dans les extraits lus. SPECIFICITY 4 exige des choix taillés pour le problème. |
| R04 | `juge-3B/2510.23574v1/e0/passe-0` | Bloc en tête : 3, 4, 5, 4, 3, RIGOR 5, BALANCE 5, RESULT_REASONING 4, 0, 0. La justification dégénère dès la proposition 5, puis devient une suite de mots sans sens ; jeton de fin à 1 673 jetons. | Notes lisibles. Non conforme : ordre, trois notes hors échelle. | Non. Notes données avant toute analyse. FEASIBILITY 4 (le maximum) pour un plan qui affine entièrement DALL-E 2, dont les poids ne sont pas publics (fait connu, non vérifié ici). |
| R05 | `juge-3B/2512.00930v1/e0/passe-1` | Bloc en tête : 3, 4, 4, 2, 3, 4, 3, RESULT_REASONING 4, 0, 0. Justification cohérente, avec erreurs de fait. | Lisible. Non conforme : ordre, une note hors échelle. | En partie. Il a lu l'ensemble (cite la proposition 6). Mais il dit les coûts « sous 10 heures de carte », alors qu'ils vont de 25 à 1 000. Il signale un recouvrement (propositions 4 et 8) et met pourtant REDUNDANCY à 0. |
| R06 | `juge-3B/2602.07160v1/e0/passe-0` | Bloc en tête : 4, 5, 5, 3, 3, 4, BALANCE 5, 3, 0, 0. Justification répétitive : un paragraphe repris presque mot pour mot. | Lisible. Non conforme : ordre, une note hors échelle. | Non. Il reproche l'« absence d'ablations », alors que quatre propositions en prévoient. Il donne COHERENCE 5 et COVERAGE 5, le maximum, malgré ses propres critiques. Les coûts de l'ensemble ne sont pas chiffrés (« Moderate », « High »). |
| R07 | `juge-8B/2506.01290v2/e1/passe-0` | Analyse d'abord, fidèle à l'ensemble. Puis justification, puis bloc sous « SCORING RUBRIC » : 4, 4, 4, 4, 4, 3, BALANCE 4, 3, −1, 0. Une dernière ligne paraphrase la consigne. | Lisible. Non conforme : une note hors échelle ; justification avant le bloc. | En partie. REDUNDANCY −1 (propositions 1 et 3) défendable. Mais FEASIBILITY 4, le maximum. IRRELEVANCE 0 alors que la proposition 6 porte sur MNIST, présenté comme « signatures manuscrites », hors des séries temporelles. Il ne relève pas qu'AutoARIMA et Prophet ne sont pas des modèles préentraînés. |
| R08 | `juge-8B/2509.21513v3/e0/passe-0` | Analyse sensée de la proposition 1 (« ~2.5/5 »), puis suite de mots sans sens dès la proposition 2, jusqu'au plafond. Aucune note. | Illisible : aucun bloc, tronquée. | Sans objet. Le début (≈ 2,5/5 par proposition) était plutôt sévère, et plausible : coûts de 30 000 à 90 000 heures de carte. |
| R09 | `juge-8B/2510.05038v3/e0/passe-1` | **Seule réponse complète du tirage** (somme 27 ; 81,8 sur 100). Analyse, puis longues plages de mots sans sens (alphabets mêlés), dans l'analyse et dans la justification. Puis bloc en gras : 4, 4, 4, 3, 4, 3, 3, 3, −1, 0 ; chaque note est suivie du texte du repère de la grille, presque recopié. | Notes lues correctement par le lecteur. Conforme mécaniquement ; le fond est en partie dégénéré. | Non. Il écrit « aucun point faible ». L'ensemble cite des ressources peu identifiables (« Casanova », « LSusat-Sentence », « BenchX », non vérifiées). La proposition 8 est en partie dégénérée. NOVELTY 4 (le maximum) non justifiée. |
| R10 | `juge-8B/2604.12086v1/e0/passe-0` | Analyse, puis bloc : SPECIFICITY 2.5, COHERENCE 3.0, COVERAGE 3.5, FEASIBILITY 2.5, NOVELTY 2.0, RIGOR 3.0, BALANCE 2.0, RESULT_REASONING 2.0, 0, 0. Justification cohérente. | Lisible. Non conforme : trois demi-points, rejetés par la règle gelée (« 3.0 » est lu). | **Oui, plausible.** Il résume fidèlement les huit propositions. Ses notes modérées collent à la consigne stricte et à un ensemble pertinent mais peu précis. Petite incohérence : il dit les propositions 4 à 8 faibles, puis la 7 forte. |

**Bilan des 10 réponses :**
- notes lisibles par un humain : 9 sur 10 (pas R08) ;
- conformes à la lettre (ordre, noms, entiers, échelles, jeton de fin) : 1 (R09), et son texte est en partie dégénéré ;
- notes fondées : 1 (R10) ; en partie : 2 (R05, R07) ; non : 6 ; sans objet : 1 ;
- les six réponses du 3B mettent toutes leurs notes **avant** l'analyse ;
- toutes les six ont au moins une note hors échelle (le 3B semble tout noter sur 5) ;
- texte dégénéré dans 4 réponses sur 10 (R01, R04, R08, R09), dont les deux tronquées.

## 4. Les 10 actions (texte intégral lu)

| # | action | statut (`episodes.json`) | contenu | notation de son ensemble | appréciation |
|---|---|---|---|---|---|
| A01 | `2506.05216v2/e2/0,7` | ajout valide (proposition 6) | effet des caractéristiques des données sur les explications par valeurs de Shapley ; générique ; 12 000 heures de carte, invraisemblable | aucune : e2 (D) n'est pas noté à cette étape | sans objet |
| A02 | `2509.18350v2/e1/0,5` | ajout valide (proposition 5) | localisation de drones par recherche d'images ; vague ; 8 000 heures | 8B : dix notes entières, dans l'échelle, mais écrites « ## Specificity: 4 » (casse non conforme), donc rejetées ; somme lue à la main : 23. Il dit aussi « 10 propositions » pour 7. 3B : SPECIFICITY 4, COHERENCE 5, COVERAGE 5, cinq notes hors échelle. | 3B gonflé ; 8B modéré, plausible, perdu par la casse |
| A03 | `2509.18350v2/e2/0,6` | invalide (révision sans numéro) | décalages temporels ; cohérent ; 5 000 heures | aucune (e2) | sans objet |
| A04 | `2510.14562v1/e2/0,3` | invalide (révision sans numéro) | variante à attention de l'agrégation de voisinage ; cohérent | aucune (e2) | sans objet |
| A05 | `2510.18828v1/e0/0,5` | invalide (révision sans numéro), au plafond de 400 jetons | dégénère en suite de mots sans sens dès le champ COST ; absente de l'ensemble final | ensemble de 6 propositions (deux sans coût). 8B : somme 16 au passage A, **26** au passage B, sur le même ensemble. 3B : 27 (B) ; A hors échelle. | le juge n'a pas vu cette action ; l'écart de 10 points du 8B sur un même ensemble est un constat brut, sans lecture |
| A06 | `2510.21366v3/e1/0,6` | ajout valide (proposition 5) | perte « consciente du débit » pour la diffusion ; mécanisme flou ; 120 heures | complet pour les deux juges. 8B : somme 17, pénalités −1 et −1, doute sur la proposition 5. 3B : somme 22, sans pénalité. | 8B plausible (la proposition 8 est un guide sans expérience) ; 3B plus indulgent |
| A07 | `2512.02017v1/e0/0,4` | ajout valide (proposition 3) | synchronisation audio-vidéo ; cohérent, générique | 8B : A tronquée (« great promise ») ; B somme 22. 3B : A et B hors échelle (B : SPECIFICITY 5). | 8B (B) plausible ; 3B gonflé |
| A08 | `2601.21315v2/e0/0,9` | ajout valide (proposition 6) | analyse théorique de l'adaptation de domaine ; « 500 heures de carte pour l'analyse théorique » : incohérent | 8B : A a dix notes lisibles mais est tronquée ; B relève le coût incohérent (remarque fondée), mais avec six demi-points. 3B : B somme 28 (« well-designed ») ; A hors échelle. | 8B fondé sur ce point ; 3B indulgent |
| A09 | `2602.07160v1/e2/0,4` | révision valide de la proposition 2 | portes apprises pour mélange d'experts ; ablations nommées | aucune (e2) | sans objet |
| A10 | `2603.01762v1/e1/0,4` | ajout valide (proposition 4) | maillages appris pour solveurs d'équations aux dérivées partielles ; « jusqu'à 50 % » sans appui ; 15 heures | 8B : tronquée, demi-points, NOVELTY 1. 3B : SPECIFICITY 5 (le maximum), BALANCE 4 hors échelle. | 3B non fondé ; 8B sévère, illisible |

**Bilan des 10 actions :**
- 4 sont en e2, non noté à cette étape ; 3 sont invalides, hors de l'ensemble final. Le tirage des actions reste désaccordé avec les notations, comme à l'audit v1.
- 1 action dégénère (A05) : le même modèle 8B, au même code et à la même température, dégénère aussi comme agent.
- Aucune action ne recoupe les 10 de l'audit v1, comme l'annonce le préenregistrement complémentaire.

## 5. Vérifications mécaniques (descriptives, hors critères gelés, non opposables)

Sorties : `sorties/*.txt` (empreintes en fin de rapport).

**5.1 Ensembles notés.** Par juge :
- 180 notations, 180 clés distinctes, égales aux clés attendues (60 tâches × A, B, C) ;
- variante b0 partout ;
- les 180 empreintes égalent celles des ensembles finaux des épisodes ;
- aucun ensemble final vide.

→ « ensembles non notés » : **écarté**.

**5.2 Fidélité du lecteur.** Ma relecture indépendante, à la règle documentée (même ligne, majuscules, entiers), redonne les notes consignées pour **180 réponses sur 180**, pour chaque juge.

Formes lisibles par un humain mais rejetées par la règle gelée :
- casse (« ## Specificity: 4 ») : 4 réponses du 8B, 1 du 3B ;
- valeur à la ligne suivant le nom : 1 réponse du 8B (`2506.16404v3/e0/passe-0`, dix notes entières) ;
- « 2.0/3.0 » : 1 réponse du 8B, tronquée de toute façon.

→ aucun défaut du lecteur ; quelques rejets de forme, sans effet sur le compte de tâches (§ 5.4).

**5.3 Défauts des réponses incomplètes** (lecture gelée ; une réponse peut en cumuler plusieurs) :

| défaut | 8B (126 incomplètes) | 3B (130 incomplètes) |
|---|---|---|
| tronquée (sans jeton de fin) | 60 | 9 |
| critère absent | 55 | 21 |
| demi-point ou décimale | 47 | 4 |
| hors échelle | 11 | **107** |
| échelle écrite autre (« /5 » sur un critère sur 4) | 7 | 1 |
| illisible | 7 | 1 |
| **défaut unique** | demi-point 26, absent 24, tronquée 20, hors échelle 5, illisible 2 | **hors échelle 96**, absent 13, demi-point 4, tronquée 2, autres 2 |

**5.4 Tâches complètes sous des lectures plus tolérantes.** Ce sont des contrefactuels descriptifs, pas une proposition de lecture (R1). Ramener une note hors échelle à la borne est artificiel : on ne sait pas ce que vaut un « 5 » sur une échelle de 0 à 3.

| lecture | 8B : réponses / tâches | 3B : réponses / tâches |
|---|---|---|
| règle gelée | 54 / **0** | 50 / **2** |
| + troncature tolérée (dix notes lues) | 74 / 3 | 52 / 2 |
| + casse des noms (troncature exclue) | 58 / 0 | 51 / 2 |
| + valeur à la ligne suivante | 55 / 0 | 50 / 2 |
| + décimales et demi-points | 75 / 2 | 53 / 4 |
| formes lisibles (casse, ligne, décimales), troncature tolérée | 107 / 9 | 56 / 4 |
| + hors échelle ramené à la borne, troncature tolérée | 81 / 6 | 153 / 35 |
| toutes ces tolérances ensemble | 122 / 14 | 160 / 42 |

- Aucune lecture n'atteint 48 tâches complètes, le seuil gelé d'une décomposition concluante.
- Le passage de « impossible » (moins de 3 tâches) à « non concluant » dépend, lui, de la règle stricte.
- Pour le 8B, il suffit de tolérer la troncature (3 tâches). Pour le 3B, seules les notes hors échelle pèsent.

**5.5 Texte dégénéré.** Indicateur choisi par moi après lecture : part des mots-outils anglais sur des fenêtres de 40 mots. Une réponse est « dégénérée » si deux fenêtres de suite sont à 8 % ou moins. Le texte cohérent est à 20 à 50 %, les suites de mots sans sens à 0 à 7 %.

- 8B : 98 sur 180, dont **59 des 60 tronquées** et 19 des 54 réponses complètes.
- 3B : 58 sur 180, dont **8 des 9 tronquées** et 13 des 50 complètes.
- Les réponses non dégénérées finissent sous le plafond. Longueur médiane des non tronquées : 1 046 jetons (8B), 599 (3B). La troncature suit la dégénérescence ; le plafond de 3 072 jetons n'est pas trop court pour un texte sain.
- Début estimé de la dégénérescence (part du texte rapportée aux jetons, estimation grossière) : médiane d'environ 410 jetons générés (8B) et 280 (3B).
- Position absolue de ce début : sous 8 192 pour 98 sur 98 (8B) et 57 sur 58 (3B).
- Remplissage à gauche dans les lots, en médiane : 332 jetons pour les dégénérées contre 337 pour les autres (8B) ; 286 contre 345 (3B).
- Les lignes sans aucun remplissage (la plus longue de leur lot, 38 par juge) dégénèrent aussi : 22 sur 38 (8B), 18 sur 38 (3B).
- Pas de motif net selon le rang dans le lot.
- Actions de l'agent du pilote (même 8B, même `generer_lot`, température 1,0, plafond 400) : 123 sur 1 800 dégénérées, dont 97 des 109 au plafond.

**5.6 Ordre.**
- 3B : 152 des 168 réponses qui portent une ligne SPECIFICITY la mettent en tête, avant toute analyse.
- 8B : 1 sur 142.

**5.7 Notes des réponses complètes.**
- Sommes brutes : 8B de 11 à 28 (16 valeurs distinctes) ; 3B de 19 à 28 (9 valeurs, surtout 25 à 27).
- Pas de notes constantes.
- Réponses A et B identiques : 0 pour les deux juges (`part_A_B_identiques`).

## 6. Réponse à la question de l'audit

**a. Artefact de mesure ?**
- *Ensembles non notés* : **écarté** (vu, § 5.1).
- *Lecteur qui rejette* : **écarté comme cause** (vu, § 5.2 et § 5.4).
  - Le lecteur est fidèle à sa règle.
  - Ses rejets de forme (casse, retour à la ligne) touchent 5 réponses du 8B et 1 du 3B.
  - Aucune tolérance n'amène un juge près de 48 tâches.
  - Seule nuance : l'étiquette « impossible » plutôt que « non concluant » tient à la règle stricte, gelée et motivée (CL-9 : un bloc coupé peut mêler notes de l'analyse et notes finales).
- *Juge qui ne répond pas au format, notes manquantes* : **c'est le mécanisme immédiat** (vu). Mais c'est un comportement des juges, que la mesure enregistre correctement. Ce n'est pas un défaut de la chaîne de mesure.

**b. Artefact de calcul ?** **Non établi.**

Indices contre (vus) :
- le code de tirage, lu, est correct : tirage sur tout le vocabulaire à température 1,0, un générateur par ligne, masque et positions explicites ;
- la dégénérescence ne dépend pas du remplissage : les lignes sans remplissage dégénèrent aussi ;
- elle commence bien avant la position 8 192 ;
- elle touche deux modèles, chargés séparément ;
- elle touche aussi l'agent, dans un autre run, sur une autre instance ;
- la garde d'équivalence en ligne du pilote est scellée conforme (`lecture.json` : 99e centile maximal 0,132, contrôle négatif « conforme », 87 actions de l'agent ; valeurs lues, non recalculées).

Limites (vues) :
- cette garde couvre l'agent : contextes d'au plus 6 030 jetons, 400 jetons générés. Elle ne couvre pas les juges, qui vont jusqu'à environ 10 000 positions ;
- les pièces ne séparent pas une propriété du modèle d'un défaut du chemin de code commun aux deux juges et à l'agent ;
- seul un rejeu sur la carte le ferait, ce qui demande un nœud et une dépense.

**c. Propriété réelle des juges ?** **Oui, pour les juges tels que configurés** : modèle, invite b0, température 1,0, tirage sur tout le vocabulaire, plafond de 3 072 jetons.
- Vu : le 3B ne respecte pas les échelles par critère (107 réponses). Le 8B donne des notes non entières, surtout des demi-points (47). Les deux dégénèrent souvent (98 et 58 sur 180).
- Vu aussi : même complètes, les notes sont peu fondées. R09, seule réponse complète du tirage, est en partie dégénérée et indulgente. Le 3B note avant d'analyser, et note haut dans une plage étroite. Le signal « trop sale » porte donc au-delà de la seule complétude.
- Supposé, non vérifié : la dégénérescence vient d'abord du tirage sans troncature à température 1,0 sur de longues sorties. Un tirage par noyau (« top-p ») ou une température plus basse la réduirait probablement.
- Je ne sais pas ce que fait l'annexe C.1 de l'article sans la relire sur PDF (R7).
- Tout changement de réglage serait un écart au préenregistrement : à décider par Lazar.

**En une ligne** : déclencheur fondé ; artefact de mesure écarté pour le lecteur et l'alignement ; artefact de calcul non établi (indices contre, non exclu) ; propriété réelle des juges tels que configurés, établie sur pièces pour l'échelle et la dégénérescence. Sa cause profonde (modèle à température 1,0, ou chemin de code commun) est supposée, non établie.

Ce rapport ne prononce aucun verdict de porte ni de lecture.

## 7. Réserves

1. **Indicateur de dégénérescence** : fait par moi, non préenregistré, seuil fixé après lecture de cinq réponses. Il peut rater un texte fluide mais faux, ou compter à tort un long bloc de notes ou une liste. Descriptif seulement.
2. **Début de la dégénérescence** : estimé par la part du texte, sans tokeniseur. Ordre de grandeur seulement.
3. **Ensembles lus par extraits** : titre, 260 premiers caractères, contrôles, coût, prédiction. Seules les actions tirées sont lues en entier. « Note fondée » est le jugement d'un seul relecteur, contre la consigne H.3 et la grille H.4, sans étalon.
4. **Tirage désaccordé** : 4 actions sur 10 en e2 (non noté), 3 invalides (hors de l'ensemble final). Six actions seulement ont une notation de leur ensemble.
5. **Tirage non rejoué par moi** : j'ai pris les 20 éléments de `relectures_audit` tels quels. Le contrôle du tirage revient au recalculateur.
6. **Contrefactuels de lecture** (§ 5.4) : comptes seulement, sans aucune décomposition ni part calculée. Ils ne proposent aucun changement de règle.
7. **Artefact de calcul** : non exclu faute de rejeu sur la carte. La garde d'équivalence citée est lue dans `lecture.json`, non recalculée, et ne couvre pas la plage des juges.
8. **Faits extérieurs** cités de mémoire, non vérifiés ici : poids de DALL-E 2 non publics ; nature d'AutoARIMA, de Prophet et de MNIST ; ressources « Casanova », « LSusat-Sentence », « BenchX » peu identifiables. Aucun ne porte un compte de ce rapport.

## 8. Fichiers de travail (sha256)

| fichier | sha256 |
|---|---|
| `scripts/stats.py` | `a92b0156d8e7217f0895d0b12de93212921bfae90ac9383bca790c542872961f` |
| `scripts/absentes.py` | `4983db900b4094fd62e74da25575dd14e27219a72e76c7ba4b80565362d3c5f1` |
| `scripts/descriptifs.py` | `5ef12e51c405d0131517c45df3d576033cba427bffb9b0a8f57372e3893332ce` |
| `scripts/controles2.py` | `14e0649f927b7887ce76f1b3c0ee16444fc04ed54a75ace97dfdcfe20442a5ba` |
| `scripts/variantes.py` | `31311f12176b6fea9b123d42f54afef3e7edbbdef09223cb0bc2c9c475c25981` |
| `scripts/debut.py` | `7b1b54d2ba78e27f646add450b8c2589fc459687990489fab7f57262f7258a5b` |
| `scripts/extraire.py`, `actions.py`, `ensembles.py`, `mentions.py`, `salade.py` | `190e56fe…`, `5ae7afa2…`, `ad5ecc01…`, `d1b06590…`, `b02a123f…` |
| `sorties/stats.txt` | `b461dfe7607b9fbb275eaba457025fddc27271e81ec851c8c8ee98f93cdec5e1` |
| `sorties/absentes.txt` | `0852538eca87044be0be7fc536646e044a7f9aadd5bb172194d20a447a636464` |
| `sorties/descriptifs.txt` | `b8fabd77f036451f67582f43fa1ddae8ee96f2a875081613ec05a55baedff8c1` |
| `sorties/controles2.txt` | `f8eace7cf09b7fe62f350ee5dffe4d92debfc364b33e0147a663c46e91d7e5b4` |
| `sorties/variantes.txt` | `6d38dc10066abbcf52814d211fe56818614c93349418a32c4805762fa933bd5f` |
| `sorties/debut.txt` | `79962cdf5ed2066a8891bdfeb8ef3016dd3c69d7df0ad7d23fd59b35145892f4` |

Note : `sorties/descriptifs.txt` porte une première version du § 5.4, avec une relecture plus souple qui franchit les retours à la ligne. Les chiffres de ce rapport viennent de `variantes.txt` et de `controles2.txt`, à la règle d'une seule ligne.