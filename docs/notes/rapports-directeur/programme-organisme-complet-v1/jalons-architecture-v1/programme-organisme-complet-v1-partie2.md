
---

## 5. Attaques et défenses du juge (niveau méthode ; résultats scellés seulement)

Règle de lecture gelée : chaque résultat de la série d'attaques se rapporte **avec les courses qui l'ont précédé, jamais seul**
[RA90]. Chaque attaque est décrite par sa classe et son but ; aucun mode d'emploi.

| attaque | classe et but | défense | résultat scellé | dépense | sources |
|---|---|---|---|---|---|
| **Banc des tricheurs** (scriptés) | des fiches qui cherchent la promotion sans loi vraie neuve : recopier, mêler ou déformer ce que l'archive a déjà accepté ; tirer en rafale sur une loi fausse | **nul d'archive ajusté**, devenu nul v8 | rejeu du 1er novembre (200 répétitions) : sans nul ajusté, quatre recombinaisons battent le juge ; avec, 0 sur 200 ; **validation décisive du nul v8** (1 000 répétitions par ligne, scellée) : 0 sur 1 000 sur chacune des 11 lignes fatales, artefact de l'ancien nul promu 395 fois sur 1 000 (le banc a des dents), perte de puissance 0,005 et 0,020 ; lecture « confirmée » par un lecteur neuf, deux réserves mineures | processeur | [RA91, RA92] |
| **A1** (2 novembre) | un proposeur modèle de langue qui lit la **description exacte** du juge et, dans un bras, ses verdicts ; deux mondes où toute promotion est fausse : W1 dans le nul v8, W2 hors du nul v8 (recombinaison par morceaux) | — | W1 : « instrument en défaut » (bras Kimi perdu ; cause corrigée : plafond de dépense commun, non le relais) ; W2 : **brèche sous v8** par la classe que le nul déclare non couverte (Argon 12 sur 12) | 39,45 USD sur 80 (3 572 appels) | [RA93] |
| **A1-bis** (plan en trois temps, quatre fournisseurs) | même attaque, plusieurs fournisseurs | — | **codé** (v3, `attaque_goodhart_v3.py`), **non couru** (aucune ligne de dépense sous GO-2026-11-02-11 ni -12) ; la reprise propre A1-v3 (Argon seul) a pris la suite | 0 | [RA94] |
| **A1-v3** (reprise propre, Argon seul, 24 cartes par monde) | même classe | — | course 1 : arrêt par l'infrastructure, sans résultat ; course 2 : état scellé **non lu** ; **course 3 (5 novembre)** : W1 « **résiste (à cette taille)** » (1 sur 24 avec retour ; l'ancien juge v7 battu 23 fois sur 24) ; W2 « **brèche sous v8** » (24 sur 24) ; 42 des 48 lois promues sont, à l'octet, la loi du monde elle-même : brèche du critère de nouveauté « rien au-delà de l'archive », pas une fausse prédiction | 4,245753 ; 48,49583 ; 58,44887 USD | [RA95, RA96] |
| **Nul v9** (2 novembre) | défense contre la classe de W2 | ajoute les recombinaisons par morceaux ajustées (par sous-population, ou de part et d'autre d'un seuil sur un trait), avec certificat ; preuve contre-lue (48 mondes neufs, 288 instants, 0 échec) ; classes **déclarées non couvertes** : profondeur 2, marches douces, produits, bruit propre à un morceau, morceaux tempérés, compositions | **validation décisive scellée : « puissance perdue »** (erreur tenue : 0 sur 1 000 sur 18 lignes fatales ; prix : puissance de 0,486 à 0,381 sur une interaction faible, perte appariée 0,105, plus de deux fois la marge de 0,05) | processeur | [RA97, RA98, RA101] |
| **Épreuve hors ligne du monde W2 gradué** | placer la dose à la frontière du v9 | — | λ* = 0,40 (loi du monde promue 803 fois sur 1 000 ; recombinaison pure 0 sur 1 000 à toutes les doses ; « λ* à la limite ») | processeur | [RA99] |
| **A1-v4** (9 et 10 novembre) | même attaque contre le **v9 candidat** | v9 | W2 (dans le nul v9) : « **résiste (à cette taille)** » (1 sur 24 avec retour ; l'ancien juge v8 battu 24 fois sur 24) ; W2 gradué à λ* : « **frontière franchie, robuste** » (10 sur 24 ; 10 des 17 lois promues se rejouent au-dessus de α après Holm) ; 8 prédictions tenues sur 11 ; gain du retour non établi ; verdict officiel par un lecteur neuf d'une autre lignée ; publié sur la page publique le 10 novembre | 114,0434 USD sur 200 (1 478 appels ; non rapproché d'une facture) | [RA100] |
| **Réplication par Kimi** de la reprise propre | seconde famille de modèles | — | **décidée** (GO-2026-11-02-25, 150 USD, jusqu'au 16 novembre), **non courue** (aucune ligne de dépense) | 0 | [RA102] |
| **Juge-tournoi** façon Co-Scientist | juge **génératif** mis sous la même attaque (second terrain du papier C) | — | **décidé** (juge Opus sur les crédits Claude, après A1-v4) ; conception v3 et devis à écrire | 0 | [RA103] |

**Ce que cela établit, et pas plus** : sur deux mondes jouets, un fournisseur, une forme d'optimisation, le v9 n'a pas laissé passer de
fausse promotion au-delà de la règle de la grille ; ce n'est pas « le taux est sous 0,05 » ; la mère le lit pour toi « validé à cette
taille, dans ce monde jouet, contre ce proposeur » [RA100].

**Nœuds ouverts sur le juge**, qu'aucune course ne tranche [RA104] :
1. **Le prix du v9** : accepter « puissance perdue » et en faire le nul de production, ou chercher un nul moins coûteux.
2. **Le sens de « rien au-delà de l'archive »** : une réponse contraire à la proposition écrite demanderait un nul v10 ; la
   revendication publique et la production attendent cette réponse.
3. **La collision avec Qu, Chen et Wang** : resserrer la revendication du juge et du banc des tricheurs et citer quatre pièces de
   plus (recommandation des lecteurs), ou garder et citer ; corriger la page publique demande un nouveau « go publication ».

---

## 6. Composition apprise, coût dans le signal, héritage, tâches fraîches, `test_final`, contre-lecteur, audit défensif

Ces mécanismes viennent de la lignée de l'objectif ultime ; ils valent « à partir de l'étape 2 » et pour le concepteur. **Aucun n'est
codé dans l'orchestrateur d'idéation** (section 1.4) [RA14, RA105].

| mécanisme | énoncé retenu | décision | état |
|---|---|---|---|
| **Composition apprise** | nombre de parties, rôle de chacune, **modèle qui sert chaque rôle** (frontière ou instrument local `LOCAL:<identifiant>`), ordre et forme des échanges, règle d'agrégation, mémoire transmise, part de budget : appris, jamais fixés par le noyau | N-045 v2, énoncé 1 | **décidé** ; non codé ; aujourd'hui la composition est fixée par configuration [RA105, RA20] |
| **Coût dans le signal** | à côté de l'exactitude, le coût de la génération (dollars par espèce, heures de carte, appels, jetons) et un **score net** gelé au préenregistrement (exactitude moins λ × coût, exactitude par dollar, ou front) ; le juge externe ne change pas | N-045 v2, énoncé 2 (« go », changement d'hypothèse) | **décidé** ; non codé (le code compte la dépense pour ses plafonds, il ne la rend pas comme signal) [RA105, RA54] |
| **Nécessité de la frontière** | part du budget, des appels et des jetons par modèle et par rôle ; ablation « sans frontière » rapportée | N-045 v2, énoncé 3 | **décidé** ; non mesurée [RA105] |
| **Le bon marché d'abord** | aucune voie à concepteur entraîné par renforcement payée avant qu'une voie bon marché ait montré que **l'apprentissage séquentiel bat le meilleur de N tirages** à budget égal (et le témoin « un modèle, vote à k, coût apparié ») ; voies par coût croissant : éliminations successives ; cache de prédictions et d'activations ; substituts à 8 milliards ; affinage sur réponses filtrées ou préférences hors ligne ; substitut du score ; tampon de rejeu ; récompense dense ; **distillation du concepteur figé** | N-045 v2, énoncé 4 | **décidé** ; aucune voie courue (sans source contraire) [RA105] |
| **Héritage récompensé** | un épisode couvre K ≥ 3 générations, ou la récompense de t inclut, actualisés, les scores de t+1 à t+K ; le bandit à un pas est exclu | N-045 v2, énoncé 5 | **décidé** pour l'étape 2 et le concepteur ; dans l'orchestrateur, « héritage » = transmission de la preuve (mémoire) et de la sélection (boucle fermée v59), **sans récompense** [RA105, RA14, RA63] |
| **Deux expériences bon marché** | (i) pilote de bruit, test A/A ; (ii) **poids contre archive** : le concepteur figé avec une archive consultable, et un adaptateur entraîné par l'organisme lui-même, contre un concepteur externe entraîné, à coût égal ; (iii) ensuite le transfert entre familles | N-045 v2, énoncé 6 | **décidé** ; non couru [RA105] |
| **Espaces de conception égaux** | séparer l'effet du format de celui de l'apprentissage | N-045 v2, énoncé 7 | **décidé** ; voie à fixer après le tour v4 du collisionneur [RA105] |
| **Tâches fraîches (a)** | la part `test` tirée dans un grand vivier à chaque génération (changement du noyau, pilote 5) | N-049 | **décidé** ; non codé dans l'orchestrateur ; le vivier de conception existe dans le noyau de l'étape 1 [RA106, RA13] |
| **Tâches fraîches (b)** | banque sœur « v3-bis », construite d'avance par qui n'a lu aucun score, lue une seule fois, jamais servie | N-049 | **décidé** dans son principe ; construction = dépense sur devis ; non construite (sans source contraire) [RA106] |
| **`test_final` lu une fois** | `test_final` lu une seule fois, à la fin du compteur de rondes de la boucle extérieure | N-050 | **décidé** (pilotes de conception, lignée A) [RA106] |
| **Contre-lecteur de la boucle extérieure** | même famille, autre modèle : Opus 5.5 analyste, Fable 5.1 contre-lecteur ; une fiche en désaccord ne motive rien ; un refus est consigné, sans bascule | N-052 | **décidé** (lignée A) ; dans la lignée B, la pratique est un contre-lecteur neuf d'un autre modèle que l'auteur (v31 contre-lue par Opus 5.5, auteur Fable 5.1 ; v65 contre-lue par Fable) [RA107] |
| **Audit défensif** | cinq propositions acceptées ; pour l'organisme : juge d'une autre lignée (point 4) et l'**invariant** « aucun score de moniteur (sonde, juge) dans un signal d'entraînement ou de sélection de l'agent », valable aussi pour la piste « organisme », gardé par le code | N-053 | **décidé** ; dans l'orchestrateur : juges de fournisseurs différents, mémoire qui ne sert ni verdict ni témoin, proposeurs sans classement des juges (v59) ; aucune garde nommée « N-053 » vérifiée ici [RA108, RA109] |
| **Composition jugée sur l'oracle** | la composition des proposeurs se juge sur l'oracle du monde planté et le coût, jamais sur le verdict du juge | N-058 | **décidé** (section 4.2) [RA77] |
| **Duel des proposeurs** | en générations d'étalonnage, une mesure, une porte ; lois gelées vraies pour l'oracle par unité de coût | N-058, N-059 | **décidé** ; non relancé (sans source contraire) [RA77, RA78] |
| **Code figé et trois régimes de budget** | — | N-044, portée | **proposé, non tranché** [RA111] |
| **Récompense collective (Avalon)** | (a) maintenant : taux de signalement du modèle de départ (devis) ; **audit de calibration des juges existants sur les paires déjà produites contre l'oracle planté** (sans dépense) ; (b) ensuite : bras de l'étape 2, récompense collective contre individuelle, signalement aux humains mesuré dans les deux ; précautions d'Avalon « go » | R-920 ; N13 tranché (a) puis (b), R-959 | (a) **décidé**, aucune trace d'exécution au registre (recherche du motif « N13 » : dernière mention R-964 avant R-2199) ; (b) **prévu** pour l'étape 2 [RA110] |
| **Organisme de Gemini** | conception concurrente | R-2152 | rapportée à part [RA4] |

---

## 7. Rôles de l'organisme dans le programme (N-065, 9 novembre)

Mots de Lazar : « rôles 1 et 2 maintenant, rôle 3 à trancher : ok » [RA112].

| rôle | contenu | état | pièces |
|---|---|---|---|
| **1. Second terrain du papier C** (« l'instrument » : la corruptibilité d'un moniteur est un gain mesurable) | le juge statistique est un moniteur d'affirmations de recherche ; l'attaque de Goodhart (A1-v4) et le juge-tournoi (juge génératif sous la même attaque) mesurent la corruptibilité de deux sortes de juges de la recherche automatisée | **décidé** ; A1-v4 couru ; juge-tournoi décidé, non codé | [RA112, RA113, RA100, RA103] |
| **2. Atelier d'idées du programme** | l'organisme reçoit des questions ouvertes du programme ; ses fiches sont du matériau, **jamais une preuve** ; tout usage décisif passe par un préenregistrement scellé (R1) | **décidé** ; exemples ci-dessous | [RA112, RA114, RA115] |
| **3. Famille de menaces diffuses pour les papiers A et B** | un proposeur à poids ouverts qui trompe le juge sur de nombreuses propositions d'apparence honnête ; si on veut mesurer l'universalité sur une famille jamais vue, la **réserver dès maintenant** comme famille tenue à l'écart (N-044, N-054) | **proposé, non tranché** ; recommandation de la mère : à décider avant toute conception de sonde qui pourrait la toucher (confiance 0,5) | [RA112, RA113] |

**Exemples du rôle 2** [RA114, RA115] : question v1 du pilier attaque (scellée `29870ac9…`) : collisionneur (2,52 USD) et course de
l'organisme (8,42 USD sur 20) ; question v2, « chercher la trace » (scellée `2dbad4b7…`) : Argon seul et collisionneur, puis
collisionneur v9 à cinq espèces (≈ 11,07 USD) ; **la course de l'organisme sur la question v2 est bloquée** : sa règle de permission
doit être écrite par toi dans `.claude/settings.json` (refus du classifieur, non contourné, R-1994) ; GO-2026-11-08-13 (20 USD) court
jusqu'au 15 novembre. Courses d'idéation du 3 novembre sur les questions des mentors (par exemple Heimersheim 10,03 USD, Kirchner Q2
≈ 24,07 USD en deux courses, Ibrahim Q1 7,98 USD) ; leurs lectures relèvent de l'inventaire voisin.

**Invariants rappelés par N-065** : aucun score d'un moniteur du programme dans l'entraînement ou la sélection de l'organisme
(N-053) ; citations obligatoires de N-064 dans tout texte qui présente l'organisme ; la page publique les cite désormais (README,
l. 8) ; la recommandation d'y ajouter Qu, Chen et Wang attend ta décision (section 5) [RA112, RA127].

**Place dans le calendrier du programme** : l'organisme n'est pas sur le chemin critique de G0 ; il sert la validité et les papiers B
et C [RA116]. **Voisins, hors de ce texte** : l'organisme de Gemini (conception concurrente) [RA117] ; P-041, arène coévolutive
« générateur de familles contre défense » (« go » de Lazar le 30 octobre), dont relève le témoin de l'attaque publiée de Bailey,
seconde moitié de l'enveloppe GO-2026-11-10-10 [RA118, RA7].

---

## 8. Calendrier, dépenses, GO et nœuds ouverts, prochains pas

### 8.1 Calendrier (dates relevées dans les pièces)

| date | fait | sources |
|---|---|---|
| 24-25 octobre | N-044 (objectif ultime), N-045 v1 puis v2 | [RA12, RA16] |
| 26 octobre | N-049, N-050, N-052, N-053 ; synthèse du collisionneur : voie hybride ancrée sur le noyau | [RA106, RA107, RA108, RA18] |
| 27 octobre | orchestrateur v6, puis v7 (versions 1 à 21) ; couche 0 couru ((a), (a) bis) ; couches 1 et 1 bis ; décisions de Lazar sur le pôle (e-BH, proposeur, Lean, couches) | [RA24, RA57, RA22] |
| 28 octobre | prise « idéation » (v31, « non lançable ») ; N-058, N-059 ; neuf voies (conv-audit) | [RA18, RA77, RA78, RA35] |
| 29-30 octobre | N-060 v3 ; course 1 (tentative 1 arrêtée le 29 ; 29 fiches) ; moissonneur (v47) ; tests de mort (v48) | [RA79, RA129, RA38, RA59] |
| 31 octobre | Avalon : (a) puis (c) (R-920) | [RA110] |
| 1er novembre | N12 (b) et N13 tranchés ; synthèse N12-N13 ; épreuve du pont ; v57, v57b, v58 ; validation du nul v8 ; publication du dépôt public (v56) ; second tour réel (1,47 USD) | [RA5, RA30, RA80, RA61, RA62, RA130] |
| 2 novembre | A1 ; v59 (boucle fermée) ; tour fermé v60 à v62 ; nul v9 ; juges v2 ; collisionneur v8 versé sans lecture ; collisionneur v9 | [RA93, RA63, RA64, RA97, RA42, RA123, RA124] |
| 3 novembre | v63, v64 ; préenregistrement de la validation du nul v9 scellé ; A1-v3 scellé ; courses des mentors | [RA64, RA70, RA95, RA115] |
| 4-5 novembre | juges v2 suspendus ; A1-v3, troisième course | [RA42, RA95] |
| 7-8 novembre | essai à blanc de la boucle réelle (défauts de la v64) ; GO-2026-11-07-11 ; GO-2026-11-08-02 ; validation du nul v9 courue (« puissance perdue ») ; note W2 ; question v2 du pilier attaque | [RA87, RA88, RA98, RA96, RA114] |
| 9 novembre | A1-v4 lancé ; N-064 ; N-065 ; juge-tournoi v2 ; juge Opus décidé ; rapport « principes, état, goulots » | [RA100, RA68, RA112, RA43, RA113] |
| 10 novembre | verdict d'A1-v4 et publication ; R-2152 ; code v65 rendu ; R-2195 ; R-2199 ; contre-lecture de la v65 lancée ; GO-2026-11-10-10 (12:05 UTC) | [RA100, RA4, RA65, RA33, RA28, RA89, RA7] |
| 15 novembre | échéance de GO-2026-11-08-13 (course de la question v2) | [RA114] |
| 16 novembre | échéances de GO-2026-11-02-22 (A1-v4), -23 (tour fermé), -24 et -32 (juges v2, suspendus), -25 (réplication Kimi), GO-2026-11-08-12 | [RA120] |
| 27 novembre | fin de l'enveloppe de calcul de la mère (GO-2026-11-10-09, 500 USD) | [RA121] |
| 30 novembre | échéance de la course réelle (GO-2026-11-08-02, GO-2026-11-10-10) ; G0 au plus tard fin novembre (hors organisme) | [RA88, RA7, RA116] |

### 8.2 Dépenses relevées (liste non exhaustive, sans total)

| poste | dépense | sources |
|---|---|---|
| couche 0 : (a) bis | 5,89 USD | [RA24] |
| couche 1 bis : génération de la banque T0.5 complète (course du programme) | ≈ 9,7 à 11,7 USD sur 25 | [RA132] |
| course 1, tentative 1 (arrêtée le 29 octobre) | Claude 8,67 USD | [RA129] |
| collisionneur N12-N13, tour 1 | 13,52 USD | [RA126] |
| épreuve fraîche du pont | 1,34 USD sur 5 | [RA131] |
| second tour réel (Kimi et Argon) | 1,47 USD sur 10 | [RA130] |
| collisionneur v8 (quatre runs) | ≈ 74,33 USD | [RA123] |
| A1 | 39,45 USD sur 80 | [RA93] |
| collisionneur v9 (brainstorm du 2 novembre) | ≈ 22,69 USD sur 40 | [RA124] |
| A1-v3 (trois courses) | 4,245753 ; 48,49583 ; 58,44887 USD | [RA95] |
| courses des mentors (exemples) | 10,03 ; ≈ 24,07 ; 7,98 USD | [RA115] |
| pilier attaque : collisionneur question v1, course question v1, collisionneur v9 question v2 | 2,52 ; 8,42 ; ≈ 11,07 USD | [RA114] |
| A1-v4 | 114,0434 USD sur 200 (non rapproché d'une facture) | [RA100] |
| validation du nul v9 ; épreuve de dose ; banc des tricheurs | 0 (processeur) | [RA98, RA99, RA92] |

Je ne donne pas de total : la liste n'est pas exhaustive et les factures ne sont pas toutes rapprochées.

### 8.3 Lignes de GO de l'organisme encore ouvertes

| GO | objet | plafond | échéance | état |
|---|---|---|---|---|
| GO-2026-11-08-02 | plus petite course réelle de la boucle complète | 45 USD | 30 novembre | conditions non remplies (contre-lecture, machine, préenregistrement) [RA88] |
| GO-2026-11-10-10 | enveloppe : boucle réelle 45 USD (et Bailey 75) | 120 USD | 30 novembre | mêmes conditions, plus la configuration `995eb918…` (écart avec la v65) [RA7, RA6] |
| GO-2026-11-10-09 | autonomie de calcul de la mère (dépense de la v65 « sur devis dans l'enveloppe ») | 500 USD | 27 novembre | ouverte [RA121] |
| GO-2026-11-02-23 | tour fermé, étage 1 | 50 USD | 16 novembre | inutilisée [RA86] |
| GO-2026-11-02-25 | réplication par Kimi de la reprise propre | 150 USD | 16 novembre | inutilisée [RA102] |
| GO-2026-11-02-24, -32 | juges d'idée v2, course de validation | 60 USD | 16 novembre | suspendue (GO-2026-11-04-08) [RA42] |
| GO-2026-11-08-13 | course sur la question v2 du pilier attaque | 20 USD | 15 novembre | bloquée (règle de permission) [RA114] |
| GO-2026-11-02-22 et GO-2026-11-08-12 | A1-v4 et sa machine | 200 et 35 USD | 16 novembre | course finie [RA100] |
| GO-2026-11-02-06, -18, -20 ; GO-2026-11-07-11 ; GO-2026-11-08-04 | décisions (boucle fermée ; tour fermé D2 à D9 ; deux corrections ; course réelle ; W2) | — | 30 novembre | en vigueur [RA63, RA84, RA88, RA120] |
| — | juge-tournoi (juge Opus) | — | — | ligne à inscrire avec la conception v3 et son devis [RA43] |

### 8.4 Nœuds ouverts chez toi (organisme)

1. **Prix du nul v9** (« puissance perdue ») [RA104].
2. **Sens de « rien au-delà de l'archive »** (contraire = nul v10) [RA104].
3. **Collision Qu, Chen et Wang** : resserrer et citer (recommandé), ou garder et citer ; nouvel accord de publication pour la page
   publique [RA104].
4. **D-P1** « qui écrit la loi » (pont), sans défaut [RA81].
5. **Rôle 3** : famille de menaces diffuses, et réserve éventuelle comme famille tenue à l'écart [RA112, RA113].
6. **Règle de permission** de la course de l'organisme v2 (à écrire par toi dans `.claude/settings.json`) [RA114].
7. **Pilier « génération »** (pas (c) de R-2199), après (a) et (b) [RA28].
8. **Code figé après conception et trois régimes de budget** (N-044) [RA111].
9. **Juge-tournoi** : GO de dépense et nœuds de la conception (effort de raisonnement, publication) à reposer sur la conception v3 [RA43].
10. **Neuf** : l'**empreinte de configuration** exigée par GO-2026-11-10-10 (`995eb918…`) n'est pas celle du code v65 (`bff138d8…`) [RA6, RA7].
11. Divergence n° 1 de N12 (des moniteurs neufs comme filtre de fiches : lecture de N-058) — « à faire confirmer par Lazar » [RA30].

### 8.5 Prochain pas de chaque chantier

| chantier | prochain pas | après | sources |
|---|---|---|---|
| **Boucle réelle v65** | contre-lecture du code v65 (Fable, en cours) | lever l'écart de configuration ; décision sur le dossier du texte scellé (dépôt public ou v66) ; machine à `bwrap` validée par `--bac reel` (avec la session-dépôt) ; préenregistrement scellé ; course avant le 30 novembre ; sortie scellée ; verdict par un lecteur neuf | [RA89, RA6, RA7] |
| **Pilier mathématique (couche 4)** | (a) critères de lecture du tour 2 N12-N13 scellés, puis lecture par un lecteur neuf, autre que le rédacteur des critères | (b) devis de l'essai « preuve formelle contre suite bon marché », GO ; (c) note de conception du pilier « génération », nœud | [RA28] |
| **Juge statistique** | tes décisions sur le prix du v9 et sur « rien au-delà de l'archive » | bascule de production éventuelle ; revendication publique ; correction de la page publique sur « go publication » | [RA104] |
| **Juge-tournoi** | conception v3 (juge Opus) et devis | ligne de GO ; course d'étalonnage puis attaque | [RA43] |
| **Juges d'idée v2** | règle de diagnosticité neuve (rédacteur neuf) et batterie tenue à l'écart (contre-lecteur) | course de validation | [RA42] |
| **Pont fiche → loi** | ta décision D-P1 | couche v57 de l'orchestrateur ; témoins du pont ; épreuve fraîche décisive | [RA81, RA50] |
| **Tour fermé** | aucun écrit ; GO-2026-11-02-23 expire le 16 novembre | à clore ou à garder : décision de la mère ou de toi (sans source) | [RA86] |
| **Réplication Kimi d'A1-v3** | aucun écrit ; GO-2026-11-02-25 expire le 16 novembre | idem | [RA102] |
| **Couches 3 et 4** | fermées jusqu'aux résultats de l'étape 2, sauf l'essai sur processeur | — | [RA5] |
| **Étape 2 (lignée de l'objectif ultime)** | aucun préenregistrement trouvé | il porterait N-044 (familles inédites), N-045 (coût, composition, héritage), N-049, N-050, le bras d'Avalon | [RA15, RA105, RA110] |
| **Rôle 3** | ta décision | avant toute conception de sonde qui pourrait la toucher | [RA113] |
| **Ce programme complet** | assembler inventaire et architecture, contre-lecture par un autre modèle, remise à toi | — | [RA122] |

---

## 9. Table finale : mécanisme → état → source

| mécanisme | état | source |
|---|---|---|
| organisme qui se conçoit seul | décidé (N-044) ; non atteint | [RA12, RA4] |
| méta-architecture figée après conception | décidé comme cible ; code figé en attente | [RA12, RA111] |
| universalité sur des familles inédites | décidé ; non mesurée | [RA12, RA4] |
| trois régimes de budget | proposé, non tranché | [RA111] |
| vivier de conception | décidé ; codé dans le noyau de l'étape 1 | [RA12, RA13] |
| questions ouvertes aux organismes | décidé ; non codé dans l'orchestrateur | [RA12, RA14] |
| diversité en trois bras (étape 2) | décidé ; étape 2 non commencée | [RA12, RA15] |
| composition apprise (modèle par rôle) | décidé ; non codé | [RA105] |
| coût dans le signal, score net | décidé ; non codé | [RA105] |
| nécessité de la frontière mesurée | décidé ; non mesurée | [RA105] |
| voies bon marché avant la voie chère | décidé ; non courues | [RA105] |
| héritage récompensé sur K ≥ 3 générations | décidé ; non codé | [RA105] |
| pilote de bruit A/A ; poids contre archive | décidé ; non courus | [RA105] |
| espaces de conception égaux | décidé ; voie à fixer | [RA105] |
| tâches fraîches : part `test` tirée par génération | décidé ; non codé dans l'orchestrateur | [RA106] |
| banque sœur v3-bis | décidé (principe) ; non construite | [RA106] |
| `test_final` lu une fois | décidé (lignée A) | [RA106] |
| contre-lecteur : même famille, autre modèle | décidé (lignée A) ; pratique voisine en lignée B | [RA107] |
| invariant « aucun score de moniteur dans l'entraînement ou la sélection » | décidé ; codé en partie | [RA108, RA109] |
| juge d'une autre lignée | décidé ; juges de fournisseurs différents codés | [RA108, RA41] |
| composition jugée sur l'oracle et le coût | décidé | [RA77] |
| duel des proposeurs en générations d'étalonnage | décidé ; non relancé | [RA77, RA78] |
| générations d'étalonnage, témoins silencieux, budget d'erreur | décidé ; codage non vérifié | [RA78] |
| récompense collective : audit de calibration des juges | décidé ; sans trace d'exécution | [RA110] |
| récompense collective : bras de l'étape 2 | prévu | [RA110] |
| couche 0 (monde caché, vrais agents) | codé, couru, porte franchie | [RA24] |
| couche 1 (banque réelle figée) | codé, essayé hors ligne : pas de dents | [RA25] |
| couche 1 bis (banque complète, graines neuves) | lue : valide, dents sur témoins plantés, aucune loi réelle | [RA26] |
| couche 2 (banque avec sabotage) | prévu ; non construite pour le pôle | [RA27] |
| couche 3 (réécriture de soi sous bac à sable) | prévu ; fermé (N12 (b)) | [RA21, RA22, RA5] |
| couche 4 (pôle théorie et Lean) | prévu ; fermé sauf l'essai sur processeur ; pas (a) lancé | [RA22, RA5, RA28] |
| pilier « génération » | proposé (nœud, pas (c)) | [RA28, RA33] |
| neuf voies de mesure adversariale | décidé (conv-audit) ; hors de ce texte | [RA35] |
| bras d'attaque de l'organisme | suspendu (R-597) ; hors mandat de la mère | [RA35, RA21] |
| proposeur à liberté bornée ; références enfichables | codé | [RA37] |
| proposeur d'idée (prise « idéation ») | codé, couru | [RA38] |
| aiguilleur | codé, couru ; mesure M4 non calculée | [RA39] |
| mémoire anti-redite, coffre, caviardage | codé | [RA40] |
| juges croisés | codé, couru (à leur plafond) | [RA41] |
| juges d'idée v2 | codé (brouillon) ; suspendu | [RA42] |
| juge-tournoi | décidé ; non codé | [RA43] |
| bisociateur à trois bras | codé ; écart à vérifier sur pièce (paires de Gu et Krenn) | [RA44] |
| metteur en fusion | codé, couru (une fusion) | [RA45] |
| moissonneur | codé | [RA46] |
| juge statistique (e-valeurs, nul composite, tirages semés) | codé ; O2 resserrée | [RA67, RA68] |
| nul v8 | codé ; validé ; production | [RA62, RA92] |
| nul v9 | codé ; « puissance perdue » ; candidat | [RA70, RA98] |
| règle e-BH | codé ; défaut décidé | [RA71] |
| pari apparié borné | cœur codé, hors du cycle ; décisions D-S1 à D-S12 | [RA72] |
| témoins plantés, témoins sans agents, « pas de dents » | codé | [RA75] |
| mondes dans une grammaire ; W1, W2, W2g ; S-V1 | codé | [RA76] |
| oracle du monde planté | codé (v60) | [RA51] |
| pont fiche → loi | codé (module), essayé (L3 « inutile en l'état »), non intégré ; D-P1 ouvert | [RA23, RA50, RA80, RA81] |
| tests de mort, verdict par le noyau | codé (v57b), essayé hors ligne | [RA61, RA48] |
| bac à sable `bwrap` | codé ; jamais joué en vrai | [RA19, RA65] |
| machine jetable (liste blanche) | codé (v56) ; machine de la v65 à monter | [RA82, RA83] |
| dossier fermé ; garde des outils | codé | [RA82] |
| boucle fermée (v59) | codé, décidé ; jamais couru | [RA63] |
| tour fermé (étage 1 ; étage 2 avec réserve) | codé (v60 à v64) ; jamais couru | [RA64, RA84, RA86] |
| boucle réelle v65 | codé sur branche ; non contre-lu ; GO ouverts | [RA65, RA88, RA7] |
| banc des tricheurs | codé ; validation du nul v8 confirmée | [RA91, RA92] |
| bancs de mutations | codé (224 mutations jusqu'à v58 ; 38 en v65) | [RA61, RA65] |
| A1 | couru | [RA93] |
| A1-bis | codé ; non couru | [RA94] |
| A1-v3 | couru (trois courses) | [RA95] |
| A1-v4 | couru ; verdict officiel scellé ; publié | [RA100] |
| réplication par Kimi | décidé ; non couru | [RA102] |
| porte PACE ; juge à plan plein | codé (exploratoire ; lecture à graines neuves) | [RA66] |
| revendication O2 resserrée ; citations obligatoires | décidé (N-064) ; collision Qu, Chen et Wang en nœud | [RA68, RA74, RA104] |
| rôle 1 (papier C) ; rôle 2 (atelier) | décidé (N-065) | [RA112] |
| rôle 3 (menaces diffuses) | proposé, non tranché | [RA112] |
| course de l'organisme sur la question v2 du pilier attaque | décidé (GO) ; bloqué par la règle de permission | [RA114] |
| organisme de Gemini | conception concurrente, rapportée à part | [RA117] |
| réserve tenue à l'écart (tour fermé) | codé (v60, v61) ; non ouvert ici | [RA64] |

---

## Annexe A — sorties payées, scellées, non lues (relevé du registre ; rien n'a été ouvert)

| sortie | où | dépense | état | sources |
|---|---|---|---|---|
| collisionneur v8, **tour 2 N12-N13** (15 cellules sur 15) | branche `donnees/collisionneur-v8-runs-v2`, commit `0e7b3e59d7c5aeee5e63b43ef920fb8f565c8a11` | 15,60 USD (GO-2026-11-01-05) | non lu ; lecture décidée (R-2199 (a)), critères en cours de scellement | [RA123, RA28] |
| collisionneur v8, **convergence v3** | même branche, même commit | 26,09 USD (GO-2026-11-01-06), reprise comprise | non lu | [RA123] |
| collisionneur v8, **sélection génération à génération v1** | même branche, même commit | 16,38 USD (GO-2026-11-01-07), reprise comprise | non lu | [RA123] |
| collisionneur v8, **vérification non circulaire du bac à sable v1** | même branche, même commit | 16,24 USD (GO-2026-11-01-08) | non lu | [RA123] |
| collisionneur v9, **brainstorm du 2 novembre** (prompt de Lazar) | branche `donnees/collisionneur-v9-brainstorm-v1`, commit `ac25c055`, liste `08aebf56…` | ≈ 22,69 USD sur 40 (GO-2026-11-02-31), suite comprise | non synthétisé | [RA124] |
| A1-v3, **deuxième course** | état scellé | 48,49583 USD | non lu | [RA125] |

Les quatre runs du collisionneur v8 ont servi l'espèce B par `claude-opus-4-6` et non Opus 5.5 : écart déclaré, à porter sur toute
lecture (R-1050) ; ils ont été versés sans lecture sur le mot de Lazar « on peut zapper le collisionneur et avancer sur org ideation »
(R-1036) [RA123]. La liste complète des sorties non lues est l'objet du fichier voisin `sorties-non-lues-v1.md`.

## Annexe B — trous, incohérences et limites de ce texte

1. **Couches 1 et 2 au sens de N12** : non définies dans les pièces lisibles (section 2.1).
2. **Empreinte de la configuration v5** : `995eb918…` (GO-2026-11-10-10, note `ddb77ed6…` de la session-dépôt) contre `bff138d8…`
   (code v65) ; origine de `995eb918…` introuvable sur `main` [RA6, RA7].
3. **Audit de calibration des juges (N13 (a))** : décidé, sans trace d'exécution trouvée [RA110].
4. **Étape 2** : aucun préenregistrement trouvé au registre ; son contenu exact (au-delà de N-044, N-045) n'est pas fixé ici [RA15].
5. **N-059** : état de codage de ses points non vérifié (conception de l'affinage non lue) [RA78].
6. **Continuité du code** entre le noyau de l'étape 1 et l'orchestrateur : affirmée par R-2152, non vérifiée sur le code [RA4].
7. **Dépenses** : relevé non exhaustif, sans total ; A1-v4 non rapproché d'une facture [RA100].
8. **Pièces non lues** volontairement : P-041, documents de l'organisme de Gemini, sorties des courses des mentors, conception de
   l'affinage, verdicts d'A1-v3 et d'A1-v4 et validation du v9 (cités par la section de résultats v3 et la page publique, qui les
   citent avec leurs empreintes, non relus ici) ; le verdict d'A1 (`795e5e99…`, cité à l'état) n'a pas été retrouvé sur `main` : son
   résultat est cité par la page publique.
9. **Contre-lecture du code v65** : non rendue au moment de l'écriture (voir le journal pour la vérification de fin).
10. **Ce texte n'est pas contre-lu.**
