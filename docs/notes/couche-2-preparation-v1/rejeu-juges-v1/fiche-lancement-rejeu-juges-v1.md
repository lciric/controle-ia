# Fiche de lancement — rejeu des juges du pilote de T0.5 sur ses 180 notations (120 textes) — v1

Écrite par un sous-agent de la lignée « session-depot » le 29 octobre 2026 (UTC), sous **GO-2026-10-28-16** (plafond
4 USD), puis corrigée le même jour après la contre-lecture R2 (section « Contre-lecture »). Elle complète le devis
`devis-rejeu-juges-v1.md` (même dossier). Elle tient lieu de préenregistrement (R1) : le module
`src/controle_ia/environnements/noter_rejeu_juges_v1.py` la reçoit par `--prereg` et en contrôle la forme (sections
exigées par `prereg.py`), le sceau et les citations ci-dessous. Le script de l'instance en lit les chemins avant toute
installation. **Rien n'est lancé par ce document.** Un seul marqueur entre chevrons reste : le commit du code
d'analyse, à remplir au commit des corrections. Tant qu'il reste, ni le scellement (`prereg.sceller_prereg`) ni le
lanceur n'acceptent la fiche.

## Citations (une seule occurrence de chaque intitulé ; lues par le module et par le script de l'instance)

- Commit du code d'analyse : `abc7f8c9b5154f7bd7808364c8ed0fdaf64f2b77`
- Configuration du rejeu (empreinte canonique) : `07d7fd810528d9341c36132c4504d4dc6ba7205012e075b018be15ce20e185ed`
- Chemin de la configuration du rejeu : `docs/notes/couche-2-preparation-v1/rejeu-juges-v1/config-rejeu-juges-v1.json`
- Run du pilote rejoué : `20261012-105125-t05-pilote-reel`
- Chemin du manifeste du pilote rejoué : `runs/20261012-105125-t05-pilote-reel/manifeste.json`
- Épisodes du pilote rejoué : `45616303dc740b66c42095cd5317a8ddd63e89123e64dd86490e43429c7cd15c`
- Chemin des épisodes du pilote rejoué : `diag/20261012-105125-t05-pilote-reel/episodes.json`
- Chemin de l'arrêt du pilote rejoué : `diag/20261012-105125-t05-pilote-reel/arret.json`
- Run des notations rejouées : `20261017-193648-t05-notations-reel`
- Manifeste des notations rejouées : `9f143f7c1c9fd9d75f21807a0fa41035ae7110abe686fc7819130d3f6b435d38`
- Chemin du manifeste des notations rejouées : `runs/20261017-193648-t05-notations-reel/manifeste.json`
- Notations rejouées du 8B : `b103835bcd3bfc3117a53e335be6f37a1259102cc2a2a134acfc6e114cb3f1c4`
- Chemin des notations rejouées du 8B : `diag/20261017-193648-t05-notations-reel/notations-8B-decisives.json`
- Notations rejouées du 3B : `51548526c7590231b76473c2b4c9e619a092616b5f948830e735c466b037adab`
- Chemin des notations rejouées du 3B : `diag/20261017-193648-t05-notations-reel/notations-3B-decisives.json`
- Tâches du pilote : `287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5aa`
- Chemin des tâches du pilote rejoué : `donnees/t05-pilote-v1/taches-pilote-60-v1.json`
- Consigne du verdict d'abord : `7c8ef0c9a80ea40e0b9274780af5e98ee62335cbe7712d29ae15e664008d6cb3`
- Entropie : `37114382722285754842192283631495258186` (celle du pilote et des notations rejouées, reprise telle quelle)
- Tests attendus : `174` (suite ciblée du script de l'instance : `tests/test_noter_rejeu_juges_v1.py`,
  `test_noter_pilote_a.py`, `test_pilote_a.py`, `test_manifeste.py`, `test_scellement.py`, `test_prereg.py` ; dernière
  ligne « N passed[, M warning(s)] in X s », rien d'autre ; compte du 29 octobre, après les corrections)

Empreintes vérifiées le 29 octobre 2026 contre leurs sceaux (`sha256sum -c`). Configuration : empreinte canonique
recalculée par `lancer_pilote_a.empreinte_config`, inchangée par les corrections.

## Hypothèse

Question d'instrument, sans signe recherché (R3). Pour chaque cellule (juge × variante), sur les 180 notations
décisives du pilote, qui portent sur 120 textes (60 d'entre eux notés deux fois, passe-0 et passe-1) :
- H_A : au moins 0,99 des scores sont finis et appuyés quand le juge est lu par la probabilité du jeton de verdict ;
- H_B : moins de 0,99 ; la cellule doit être redéfinie avant toute banque.

Ce duel est celui du collisionneur (cellule E3-T1 de la conception B, l. 250-252 ; synthèse `37f85388…`, l. 327-328).
Cellules : 8B et 3B × « b0 relu », « verdict d'abord », « budget relevé » (devis, § 3).

## Prédiction chiffrée et signe attendu

- **b0 relu.** Une réponse tronquée reste sans score, d'où des bornes arithmétiques sur les comptes RAPPORTÉS par
  l'audit R4 (`d69a8700…`, l. 143-149, 252-253) :
  - 8B : au plus 120 sur 180 (0,667). Il faut s'attendre à 82 à 96 (0,46 à 0,53) : les 54 complètes, plus les 28 à
    demi-points seulement, plus une partie des 14 mixtes, si toutes sont appuyées ;
  - 3B : au plus 171 sur 180 (0,95). La fourchette est large, 50 à 160 (SUPPOSÉ), car les 96 notes hors échelle seules
    échouent probablement au seuil d'appui ;
  - **H_B dans les deux juges, certaine** (tranchée sur les 120 textes dès que k0 ≤ 116).
- **Verdict d'abord.** Aucune borne. SUPPOSÉ : 8B ≥ 0,9 ; 3B entre 0,5 et 0,95 (tendance aux notes hors échelle). Les
  deux issues sont possibles ; aucune n'est visée.
- **Budget relevé** (composé avec b0 relu). Au plus b0 relu + 2 sur 180 pour le 8B (59 tronquées sur 60 sont
  dégénérées) et b0 relu + 1 pour le 3B. **H_B, certaine.**
- **Contrôle de l'instrument.** SUPPOSÉ « aligné » dans toutes les cellules : au réel, chaque note écrite a été tirée
  de la loi même que la lecture rend à sa position. Un « désaligné » serait un défaut de la lecture, pas un résultat
  sur les juges.
- **Audit R4.** SUPPOSÉ : le déclencheur « jetons de tête » se lève dans b0 relu des deux juges (demi-points du 8B,
  notes hors échelle du 3B lues par leur premier jeton).
- **Accord** (8B, b0 relu). SUPPOSÉ : 0,8 à 0,95 des critères. La note écrite a été tirée à la température 1 : la
  valeur la plus probable ne lui est égale qu'avec la probabilité de cette valeur.
- **Rythmes.** SUPPOSÉS (devis, § 4) : b0 relu ≈ 2,5 s par notation (8B) et ≈ 1 s (3B) ; verdict d'abord ≈ 6 s et
  ≈ 3,4 s ; budget relevé ≈ 28 s et ≈ 27 s par réponse prolongée.

## Métrique

**Lecture par la probabilité du jeton de verdict** (module, `lire_par_probabilite`). D-S13 est close sur son texte :
conception v3 du pari de signe, l. 277 (branche `canal/conv-audit-n04`,
`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pari-de-signe/conception-pari-de-signe-v3.md`,
empreinte `1518a12f0c9b755ec6ab0f958d9c6b77f8071d7f959f6e5c5cb60de38a15db14`, vérifiée contre son sceau). La session la
lit ainsi (R-685) : « score continu exigé (probabilité du jeton de verdict) pour toute cellule de G1 ; bris d'égalité
aléatoire à graine scellée sinon ; règle « non comparable » ». À la ligne citée, les options sont « score continu exigé
(probabilité du jeton de verdict) ; bris d'égalité aléatoire à graine scellée ; règle « non comparable » », et la
recommandation est « score continu exigé pour toute cellule de G1 ; bris scellé sinon ». Le score lu ici est continu
(une espérance) : il n'a pas d'ex æquo, et aucun bris d'égalité n'entre dans une décision.

Pour chaque critère de la rubrique H.4, la lecture se fait après la dernière occurrence de « CRITÈRE: » (expression
de `rubrique.lire_notes`).
- Chaque valeur admise v de [lo, hi] a sa suite de jetons, encodée depuis le jeton qui porte le premier caractère
  après les deux-points.
- La **position de décision**, une seule par critère, est la première où ces suites divergent.
- La probabilité de v est le produit des probabilités conditionnelles de sa suite, à partir de cette position. Les
  branches hors du chemin écrit se lisent par passes forcées.
- La masse admise M est la somme de ces probabilités : **la probabilité que le juge commence, à cette position, par
  une valeur admise, quelle que soit la suite** (lecture par les jetons de tête : le tokeniseur de Llama 3 découpe les
  chiffres à part, si bien que « 2.5 » compte pour 2, « 3/5 » pour 3 et « 2 out of 5 » pour 2). La loi est
  renormalisée sur les valeurs admises ; la note lue est l'espérance.
- Score lu : 100 × max(0, somme des dix espérances) / 33.

**Jamais de moyenne ni de médiane sur des jetons.**

**Score fini et appuyé** d'une notation : les trois conditions suivantes réunies, sinon aucun score (jamais imputé),
motif consigné.
- Fenêtre complète :
  - b0 relu et budget relevé : réponse terminée par un jeton de fin (règle CL-9) ;
  - verdict d'abord : les dix critères apparaissent dans la réponse, et la lecture porte sur le bloc qui va du début de
    la réponse à la fin de la ligne où le dixième apparaît pour la première fois.
- Les dix positions existent : critère présent, valeur écrite après les deux-points.
- À chacune des dix positions, M ≥ 0,5 (`masse_min_appui`).

**Complétude d'une cellule** : k / n, k scores finis et appuyés sur n = 180 notations. Une notation par texte, celle
de la passe-0, donne k0 sur 120 (tirages indépendants). La cellule « budget relevé » se compose ainsi : notations
prolongées pour les réponses tronquées de b0 relu, notations de b0 relu pour les autres. Intervalles de Wilson à 95 % :
sur les 120 passe-0 (celui qui tranche) et sur les 180 notations (descriptif).

**Contrôle de l'instrument (alignement)** : sur les critères à note écrite valide et lue, part où la **probabilité
brute** de la note écrite (probabilité renormalisée × M, toutes deux consignées) est sous 0,001. La part calculée sur la
loi renormalisée reste consignée, comme descriptif, et ne décide pas : une position ou un encodage faux effondre M alors
que la loi renormalisée peut rester plate, et la note écrite n'y serait alors jamais improbable.

**Lectures en échec de l'instrument** : notations dont la lecture échoue parce qu'aucun jeton ne porte la valeur ou
parce qu'une log-probabilité n'est pas finie.

**Descriptifs par cellule** (aucune décision, sauf comme déclencheurs d'audit, critère 4) : finis sans appui ; finis
écrits ; notations à score écrit mais sans score appuyé ; scores appuyés dont au moins une note écrite n'est pas admise
(non entière, hors échelle ou d'une autre échelle : lecture par les jetons de tête) ; masses minimale et maximale ;
ré-encodage (notations dont la réponse scellée, ré-encodée, n'a pas la longueur rejouée).

**Accord** : sur les notations où note écrite et lecture donnent toutes deux un score, deux mesures, sans intervalle
(les dix critères d'une notation ne sont pas des tirages indépendants) :
- part des critères où la valeur la plus probable égale la note écrite (ex æquo : la plus petite, règle déclarée) ;
- écart absolu des scores sur 100, moyen et maximal.

**Rythmes** : secondes par notation par cellule (durée de la phase / notations), passes forcées, jetons générés, pic
de mémoire par phase, lus dans les descriptifs du fichier de la phase.

## Seuil

- Complétude : **0,99** par cellule.
  - Lecture ponctuelle sur les 180 notations : **H_A si k ≥ 179** ; H_B sinon.
  - « Tranchée » : l'intervalle de Wilson sur les 120 passe-0 est entier du côté lu. H_B est tranchée si sa borne
    haute est < 0,99, soit **k0 ≤ 116**. H_A n'est jamais tranchée : 120 sur 120 donne une borne basse de 0,969. Le
    rejeu peut réfuter H_A, pas l'établir.
  - L'intervalle sur les 180 notations reste un descriptif : il supposerait 180 tirages indépendants (H_B y serait
    tranchée dès k ≤ 175).
- Appui : M ≥ **0,5** à chaque position.
- Contrôle de l'instrument : part improbable (probabilité brute) ≤ **0,02**. Au hasard, à chaque position lue, la
  probabilité que le juge ait écrit une valeur admise de probabilité brute sous 0,001 est au plus 6 × 0,001 (six
  valeurs admises au plus) : on attend au plus 0,006 × positions lues. Rapportée aux notes valides, la part reste sous
  0,02 tant que celles-ci font au moins 30 % des positions lues ; en deçà, l'échec est prudent (« non concluant »,
  jamais une lecture tranchée à tort).
- Lectures en échec de l'instrument : au plus **0,02 × n**.
- Accord : part ≥ **0,90** → « concordant », sinon « discordant ». C'est un descriptif : aucune décision n'en dépend.

## Plan d'analyse

1. Récupération de la branche `calcul/rejeu-juges-v1`, contrôle des sceaux et du rattachement de chaque fichier au
   manifeste (`verifier_resultat`).
2. Lecture par la commande `python -m controle_ia.environnements.noter_rejeu_juges_v1 --lire <run>`, et par elle seule,
   **y compris après un arrêt**. Elle lit toute phase dont le fichier existe, scellé et rattaché au manifeste : une
   phase n'écrit son fichier qu'une fois finie. Les statuts des autres phases viennent de `resume.json`, sinon de
   `arret.json` (`partiel.phases`), sinon d'aucun fichier (arrêt par KILL) ; le champ `source` de la lecture le dit.
   Elle écrit `diag/<run>/lecture-rejeu-v1.json`, scellé, rattaché au manifeste.
3. Pour chaque cellule écrite : complétude (k, n, part ; k0 sur les 120 textes ; les deux intervalles ; H_A ou H_B ;
   tranchée ou non), contrôle de l'instrument, lectures en échec, descriptifs, audit R4 (déclencheurs et notations
   tirées), accord, rythme. Une cellule non écrite est « non mesurée », avec son statut : « échu », « non-commencé »,
   « arrêt pendant la phase », « non atteinte », « fichier non scellé ». Un budget relevé sans b0 relu du même juge
   est aussi « non mesuré ».
4. Audit R4 de chaque cellule où un déclencheur se lève : la session relit les notations tirées et la position de
   chacune de leurs dix valeurs ; le résultat est une réserve consignée, jamais une autre lecture.
5. Compte rendu à Lazar : le verdict d'abord (quelles cellules tiennent H_A), puis les réserves. S'il y a lieu, une
   proposition avec recommandation sur la cellule des juges de la banque.

## Critères de lecture gelés

1. **Score fini et appuyé** : la définition de la section « Métrique », sans autre tolérance (ni troncature tolérée,
   ni note ramenée à la borne, ni critère imputé). La lecture par les jetons de tête est déclarée (M compte une valeur
   admise dès son premier jeton) et rapportée par cellule.
2. **Complétude** : H_A si k / n ≥ 0,99, H_B sinon, par cellule ; « tranchée » sur les 120 passe-0 (section
   « Seuil »). Les cellules d'un même juge ne se combinent pas, sauf la composition déclarée de « budget relevé ».
3. **Instrument** :
   - « désaligné » (part improbable sur la probabilité brute > 0,02) : la cellule se lit « non concluant (instrument
     désaligné) » ;
   - lectures en échec de l'instrument au-delà de 0,02 × n : « non concluant (lectures en échec de l'instrument) ».

   Dans les deux cas, ni H_A ni H_B n'est lu, la cellule n'est jamais « tranchée », et l'audit R4 se déclenche. La
   lecture et l'étiquette brutes restent consignées (`lecture_brute`, `tranchee_brute`).
4. **Audit R4, symétrique.** Il se déclenche si l'un de ces cas se présente :
   - trop favorable : n sur n ; toutes les masses lues au-dessus de 0,99 ;
   - trop défavorable : au plus 0,02 × n scores finis et appuyés (cellule à 0 ou presque) ; toutes les masses lues
     sous 0,01 ; plus de 0,05 × n notations à score écrit mais sans score appuyé ;
   - jetons de tête : plus de 0,02 × n scores appuyés dont une note écrite n'est pas admise ;
   - instrument : « désaligné », ou au moins une lecture en échec.

   L'audit relit vingt notations (toutes si n < 20), tirées sans remise. La graine est dérivée de l'entropie du run
   sous la clé `audit-r4/<juge>/<variante>` (`manifeste.graines`, R9) : le tirage est fixé avant toute lecture.
5. **Accord et rythmes** : rapportés, sans seuil de décision. L'étiquette d'accord n'est qu'un descriptif.
6. **Phases écrites avant un arrêt** : elles se lisent comme les autres (plan, point 2). Ce n'est pas un écart.
7. **Ce que la lecture décide** : quelles cellules (juge × variante) tiennent H_A, rien d'autre. Toute redéfinition de
   la cellule des juges dans la banque est une proposition à Lazar.

## Liste d'arrêt

Avant le manifeste (aucun run créé, code 1 du module) :
- configuration incomplète ou hors bornes : phases, durées, budgets 16 à 512 et 1 à 3 072, appui dans [0, 1], invite
  b0 seulement ;
- run réel sans fiche (R1) ;
- run réel sans échéance externe (`--echeance-externe`), ou échéance passée ou non finie ;
- fiche non scellée ou non conforme ;
- commit du code différent de l'arbre gelé ;
- citation absente, en double ou différente : configuration, runs, manifeste et notations rejouées, épisodes,
  consigne, tâches, entropie ;
- invites altérées ;
- pilote dans un autre état que celui constaté (`charger_pilote_note`) ;
- notations rejouées absentes, non scellées ou rattachées à un autre manifeste ;
- paramètres des juges différents de ceux des notations rejouées ;
- demandes et notations désalignées (clé, empreinte de l'ensemble, nombre 180) ;
- lecture écrite refaite différente du score rejoué ;
- entropie différente de celle du pilote.

Après le manifeste (`arret.json` scellé, puis arrêt) :
- format d'un juge différent de celui du début du pilote ;
- **encodage des valeurs différent de celui que suppose la lecture** (garde d'encodage, au contrôle du format, avant
  toute phase) : « X: -1 » et « X: 0 » doivent donner, après les deux-points, « ␣- », « 1 » et « ␣ », « 0 » aux
  décalages attendus, et chaque valeur de chaque échelle doit s'encoder en contexte comme à part ;
- format ou encodage du 3B rechargé hors ligne différent ;
- contexte reconstruit d'une autre longueur que `jetons_contexte` ;
- réponse non tronquée présentée au budget relevé ;
- signal TERM (délai externe ou plafond de l'amorce), même avalé par une bibliothèque ;
- toute panne : mémoire, réseau, chargement.

Non-arrêts consignés :
- phase « échue » (sa durée maximale dépassée) : aucun fichier, la suivante commence ;
- phase « non-commencé » : le temps restant avant l'échéance globale est sous sa durée maximale ;
- notation sans score, avec motif.

Chaîne de l'instance (code 2 ou 1, résultats partiels et traces poussés) :
- branche de résultats déjà présente ;
- fiche ou fichier cité absent, ou sceau non conforme ;
- marqueur restant dans la fiche (marqueur de remplissage ou entre chevrons), avant l'installation ;
- poussée initiale refusée ;
- carte indisponible ;
- tests en échec ou nombre différent de « Tests attendus » ;
- temps restant avant le plafond de l'amorce sous 20 minutes.

Lanceur (aucune création) :
- commit absent de `origin/main` ;
- pièces absentes ou non scellées ;
- marqueur restant dans la fiche ;
- commit du code non ancêtre du commit lancé ;
- jeton absent ;
- garde de calcul refusée ;
- autre instance sur le compte ;
- crédit sous 4,50 USD ;
- aucune offre conforme (A100 SXM4 80 Go, ≤ 1,43 USD/h, fiabilité ≥ 0,98, CUDA ≥ 13.0, mémoire vive ≥ 64 Go,
  téléchargement ≤ 0,01 USD/Go).

## Bornes de temps

- **Phases**, dans l'ordre de priorité de la configuration :

  | phase | durée maximale |
  |---|---|
  | 8B, b0 relu | 20 min |
  | 3B, b0 relu | 10 min |
  | 8B, verdict d'abord | 30 min |
  | 3B, verdict d'abord | 20 min |
  | 8B, budget relevé | 40 min |
  | 3B, budget relevé | 10 min |

  Une phase ne commence que si le temps restant avant l'échéance globale couvre sa durée maximale.
- **Échéance globale** du module : la plus proche de deux échéances, consignée dans `resume.json` et dans `arret.json`
  (champ `echeance`) :
  - début + 85 minutes (5 100 s, configuration) ;
  - l'échéance externe que passe le script de l'instance (`--echeance-externe`) : délai externe du run moins 6 minutes,
    marge du dernier lot.

  Le dernier lot peut dépasser l'échéance globale d'au plus ≈ 4 minutes (SUPPOSÉ : un lot de budget relevé du 8B fait
  1 024 pas) ; il finit donc avant le TERM. **Aucune phase commencée n'est tuée par le délai externe.**
- **Délai externe du run** : 95 minutes au plus (TERM converti en arrêt consigné, KILL 5 minutes plus tard). Il est
  borné par le temps restant avant le plafond de l'amorce, moins 13 minutes (KILL du run 5, poussées 8). Sous
  20 minutes, le run ne commence pas.
- **Marge de la phase 5** (8B, budget relevé, 40 minutes). Avec une échéance de 85 minutes, elle ne commence que si au
  plus 45 minutes ont passé depuis le début du module. Les chargements et les phases 1 à 4 en prennent ≈ 42 dans
  l'attendu (devis, § 4) : la marge est de 3 minutes. Si la mise en place de l'instance dépasse ≈ 26 minutes,
  l'échéance externe tombe sous 85 minutes (111 minutes moins la mise en place), et la phase 5 ne commence plus dans
  l'attendu. Elle est alors « non-commencé », comme le veut l'ordre de priorité.
- **Amorce** : 130 minutes, puis KILL 5 minutes plus tard.
- **Arrêt de l'instance** par la session, par identifiant (R10), dès la fin de l'amorce lue dans le journal, et au plus
  tard à la création + 9 000 s (heure écrite par le lanceur).
- **Réveils de garde** (contre-lecture, CLJ-04). Dès la création, **la session programme deux réveils d'elle-même**
  (tâches « une fois »), à la création + 140 minutes et à la création + 155 minutes. Le lanceur écrit leurs heures dans
  `lancement.txt` (ligne `reveils_de_garde`). La session y consigne leurs identifiants. Chaque réveil inventorie les
  instances, arrête celle du rejeu par son identifiant (R10) si elle tourne encore, et consigne l'arrêt dans
  `registres/arrets.md`. Si l'instance est déjà arrêtée, le réveil le constate et ne fait rien d'autre.
- **Facture**, téléchargement compté à son plafond (0,01 USD/Go) :
  - arrêt à la fin de l'amorce : pire cas ≈ 3,9 USD (devis, § 6) ;
  - session perdue, arrêt par le premier réveil (≈ 142 minutes) : ≈ 3,7 USD ;
  - si le premier réveil échoue aussi, arrêt par le second (≈ 157 minutes) : ≈ 4,06 USD, juste au-dessus du plafond du
    GO (cas de double panne).

## Manifeste et graines (R9)

Run `AAAAMMJJ-HHMMSS-rejeu-juges-reel`. Le manifeste (`runs/<run>/manifeste.json`, scellé) porte :
- la configuration et son empreinte, les versions, le commit, cette fiche (chemin et empreinte) et la commande ;
- les **graines**, dérivées par `numpy.random.SeedSequence` de l'entropie du pilote, comme au pilote. Clés :
  - une par génération : `rejeu-v1/verdict-d-abord/<clé du pilote>` (360) et `rejeu-v1/budget-releve/<clé>` (69, les
    réponses tronquées) ;
  - plus `modele-jouet`, qui égale la graine du pilote.

Les graines de l'audit R4 (clés `audit-r4/<juge>/<variante>`) ne sont pas au manifeste : la lecture les dérive de la
même entropie, par la même fonction (`manifeste.graines`), avant de lire quoi que ce soit.

Les phases b0 relu ne tirent rien. Résultats : `diag/<run>/rejeu-<juge>-<variante>.json`, `resume.json`, et
`arret.json` s'il y a lieu, tous scellés et rattachés au manifeste. Rien n'est écrit dans les dossiers du pilote ni dans
ceux des notations rejouées.

## Ce que ce rejeu ne décide pas

- Aucune lecture de T0.5 n'est refaite. Le verdict des notations (`d861605c…`) et la bascule vers le plan B (N-022)
  restent tels quels.
- Aucun chiffre opposable (R7) ; aucune mesure de justesse des juges.
- Aucun changement de modèle, d'invite publiée ni de rubrique. La consigne « verdict d'abord » est un ajout déclaré, à
  l'empreinte citée. Ce rejeu ne remplace pas le plan B (RS1), dont le code n'est pas sur `main`.
- Aucune redéfinition de la cellule des juges dans la banque : ce sera une proposition à Lazar.
- D-S13 est close sur son texte (section « Métrique »). Le rejeu en applique le score continu ; il ne décide rien du
  bris d'égalité ni de la règle « non comparable », qui portent sur les cellules de G1.

## Contre-lecture

- **Contre-lecture 1** : sous-agent neuf Opus 5.5, qui n'a rien écrit de ce qu'il relit (R2). Fichiers donnés : devis,
  fiche, configuration, module, essais, amorce, script de l'instance et lanceur, plus les fonctions importées. Brouillon
  relu : commit `33bd7c91`, fiche `f328506f3d47b39decbbac564a7ff82a2e15cc2a1679024234fad76bb6891370`, devis
  `6c96c13fe87bbdbfba6951de24afc3f4b46cdf2a9b4fcd14e52b5f5390591fa2`. Rapport :
  `docs/notes/couche-2-preparation-v1/rejeu-juges-v1/contre-lecture-rejeu-juges-v1.md`, empreinte
  `581ae87a8271fe17534f4f534cfc7c2d1f367ed4adb6c330dc5f4a0bf9254e8b`. Verdict : « lançable après corrections ».
- Traitement des constats, par l'auteur, le 29 octobre. Chaque correction du module a son essai, marqué « contre-lecture,
  CLJ-0k » ; tous échouent sur le module relu. La vérification des corrections revient à la session, avant le
  scellement.
  - CLJ-01, majeur, lecture perdue après un arrêt : **corrigé**. `lire_rejeu` lit toute phase écrite et scellée, avec
    les statuts du résumé, sinon de l'arrêt, sinon d'aucun fichier (champ `source`) ; plan, point 2 ; critère 6.
  - CLJ-02, majeur, phase payée puis tuée par le délai externe : **corrigé**. Le script de l'instance passe
    `--echeance-externe` (délai externe moins 6 minutes) ; le module retient la plus proche des deux échéances, la
    consigne, et l'exige en mode réel ; section « Bornes de temps » ; devis, § 5.
  - CLJ-03, majeur, faux H_B tranché sur masse effondrée : **corrigé**. Le contrôle porte sur la probabilité brute ;
    la démonstration du contre-lecteur (masse admise 3,7e-5) donne « désaligné », puis « non concluant », jamais
    tranchée ; critère 3.
  - CLJ-04, majeur, aucun réveil de garde : **corrigé dans la procédure**. Réveils à la création + 140 et + 155 minutes,
    programmés par la session, heures écrites par le lanceur ; section « Bornes de temps » ; devis, § 6 et § 8. Le
    plafond de l'amorce reste de 130 minutes : la suggestion facultative de le ramener à 120 n'est pas retenue, car la
    phase 5 ne commencerait plus dans l'attendu.
  - CLJ-05, moyen, audit R4 asymétrique : **corrigé**. Déclencheurs symétriques et tirage gelé par la clé
    `audit-r4/<cellule>` ; critère 4.
  - CLJ-06, moyen, lecture par les jetons de tête : **déclaré et rapporté**. Définition exacte de M (section
    « Métrique ») ; descriptif par cellule ; déclencheur d'audit au-delà de 0,02 × n. L'option plus stricte (multiplier
    par la probabilité d'une fin de valeur) n'est pas retenue.
  - CLJ-07, mineur, 180 notations de 120 textes : **corrigé**. « Tranchée » se lit sur les 120 passe-0 ; l'intervalle
    sur 180 n'est plus qu'un descriptif ; l'accord n'a plus d'intervalle.
  - CLJ-08, mineur, D-S13 : **clos** sur son texte, cité dans la section « Métrique ».
  - CLJ-09, mineur : marge de la phase 5 écrite ; longueur ré-encodée de chaque réponse scellée consignée
    (`jetons_reponse_reencodes`) ; banc de la chaîne refait après les corrections (devis, § 8), journaux à verser avec
    leurs empreintes (R6).
  - « Ce que je n'ai pas pu vérifier » : garde d'encodage ajoutée, qui arrête avant toute phase si le vrai tokeniseur
    découpe autrement les valeurs. Le vrai tokeniseur n'est toujours pas sur ce disque ; sur un tokeniseur simulé à la
    Llama 3 (même expression de découpage, octets, `tokenizers` 0.23.2), la garde passe, et elle arrête si les
    décalages sont rognés (essai). La suite ciblée est comptée (174). Les rythmes restent SUPPOSÉS.
