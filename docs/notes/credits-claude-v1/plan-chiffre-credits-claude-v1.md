# Plan chiffré des crédits de Claude — v1

- **Statut** : proposition de la session mère à Lazar (R-2362, R-2365 : « plan chiffré avant le 13 »). Ni GO, ni devis
  opposable. **Aucune dépense n'est engagée par ce texte** : chaque ligne ci-dessous reste sous un GO chiffré que seul
  Lazar donne (R-2365, `registres/decisions.md` l. 2323).
- **Écrit** le 12 novembre 2026 vers 08:25 UTC (`date -u` : 08:23:39) par un rédacteur neuf (Claude Opus 5.5,
  `claude-opus-5-5`), sous-agent de la session mère, sur sa consigne (R-2418, `registres/decisions.md` l. 2376).
- **Ce qui a été fait** : lectures seules ; aucun appel de modèle ; aucune clé lue (variables nommées seulement) ; rien lu
  sous `diag/`, `runs/`, `donnees/bras-attaque*`, `docs/notes/bras-attaque/`, `donnees/mode-tenu-a-l-ecart*`,
  `registres/index-bras-attaque*`, ni des sorties de 7a et 7b.
- **Empreintes des sources** (relevées à la lecture ; `registres/*.md` s'allongent, l'empreinte vaut pour l'état lu) :
  `registres/decisions.md` `ada7979c…` ; `registres/go.md` `31019833…` ; `registres/depenses.md` `b4079bb7…` ;
  préenregistrement scellé de la course v66 `46d7545b489a2037ede235d843ef8a0c504461a0a2d697af5db40de2400fd89d` ;
  note de l'expérimentateur `7df9afc4…` ; synthèse du collisionneur `f3d7eea7…` ; conception du juge-tournoi v1
  `a781eb62…`, v2 `0ac81c9a…` ; préenregistrement des juges d'idées v2, brouillon 4 `f7616284…` ; N-029 `084e3052…` ;
  N-049 `8a5bf5e5…` ; N-052 `817d218b…` ; N-053 `2204256d…` ; N-058 `854f2724…` ; N-060 v3 `2b448f69…` ; N-061
  `b2ae4417…` ; N-064 `387c9d4e…` ; N-065 `f820e90d…` ; programme v2 `2fd63bad…`.

## 0. En bref

- **Crédits** : ≈ 1 000 USD sur cinq comptes (mot de Lazar, R-2365, l. 2323) ; seul le compte de la clé
  `RR_ANTHROPIC_API_KEY_RIGAUD` est dans l'environnement ; les autres clés sont à déposer par Lazar, une variable nommée
  par compte, à leur déblocage (le 17 ou le 19). Les crédits **expirent en fin de cycle, sans report** (R-2000, l. 1958) ;
  **date exacte de fin de cycle de chaque compte : à vérifier par Lazar** (console de chaque compte).
- **Déjà dépensé sur la clé Rigaud** (au barème des scripts, non rapproché d'une facture) : ≈ **35 USD** — sonde de refus
  5,07 (`registres/depenses.md` l. 409) ; étiqueteur v2, essai de format et lancement interrompu 16,46 (l. 411) ;
  collisionneur QO-1 et Q1 ≈ 8,0 (l. 412) ; collisionneur sur l'expérimentateur 5,58 (l. 418 ; ≈ 3,86 au tarif public).
  **Reste estimé** : ≈ 165 sur Rigaud, ≈ 965 sur les cinq comptes.
- **Où Claude est permis** : juge du juge-tournoi (Lazar, R-2026) ; un des deux lecteurs de la vérité du dommage (N-060
  v3) ; contre-lectures par l'interface (N-052) ; collisionneur ; écriture de mondes plantés neufs ; pilote d'instrument du
  papier C (sous réserve de périmètre).
- **Où Claude est interdit** : tout rôle dans l'organisme d'idéation sur les mondes actuels (course v66 et expérimentateur,
  textes scellés) ; toute référence boîte noire de T0.6 et T0.8 (N-029) ; tout bras qui toucherait la cloison.
- **Plan recommandé (a)** : ≈ **435 USD** de plafonds sur crédits, en trois tranches calées sur les déblocages ; option
  (b) ≈ 920 si la manche T1 du juge-tournoi est décidée après lecture de T0.

## 1. Grille de prix

Vérifiée sur la table « Current Models » de la compétence `claude-api` (cache du 2026-11-03), en USD par million de
jetons ; **à relire sur la page publique des prix avant chaque devis** (la table est mise en cache).

| modèle | identifiant | entrée | sortie | lecture du cache |
|---|---|---|---|---|
| Opus 5.5 | `claude-opus-5-5` | 4,00 | 20,00 | 0,20 |
| Sonnet 5.5 | `claude-sonnet-5-5` | 2,00 | 10,00 | 0,10 |
| Haiku 5.5 | `claude-haiku-5-5` | 0,10 | 0,50 | — (consignes ≤ 100 000 jetons ; 0,50 / 2,50 au-delà) |
| Fable 5.2 | `claude-fable-5-2` | 8,00 | 40,00 | 0,20 |
| Fable 5.1 | `claude-fable-5-1` | 10,00 | 50,00 | — (non relevé) |

- La réflexion est facturée comme sortie ; sur Opus 5.5 elle ne se coupe pas (effort seul ; défaut « medium »).
- Le barème du relais du programme (Opus 4 / 20, Fable 5.1 10 / 50) est égal à cette table (conception du juge-tournoi
  v1, l. 213). Le relais refuse les lots (`/v1/messages/batches`, même ligne) : les lots, à moitié prix, ne sont pas
  comptés ici ; un relais qui les accepte doublerait le volume par dollar (code neuf, contre-lu).
- **Fable 5.2** est moins chère que Fable 5.1 (8 / 40 contre 10 / 50) mais N-052 nomme Fable 5.1 pour le contre-lecteur
  (`decision-N-052-v1.md` l. 32-34) : passer à 5.2 est un **changement de modèle**, interdit sans GO. Non compté ; voir
  la décision, section 6.

## 2. Contraintes vérifiées sur les sources

| contrainte | source (chemin, ligne) | effet sur ce plan |
|---|---|---|
| Course v66 : « Claude ne joue aucun rôle » ; proposeurs de la famille Claude hors portée ; aucun juge de cette famille ; **lois plantées écrites par un modèle de la famille Claude** | `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-v1.md` l. 149 et l. 291-294 (`46d7545b…`, empreinte recalculée à la lecture) | aucun appel de Claude dans l'organisme sur ces mondes |
| Expérimentateur (option (a) de R-2368, choisie en R-2370) : « Claude exclu par construction » ; « Claude exclu de tout rôle » au préenregistrement | note de conception l. 65-69 et l. 185 (`7df9afc4…`) ; R-2370 l. 2328 | **l'expérimentateur ne se paie pas sur les crédits** ; il tourne sur Kimi |
| Juges d'idées v2 : aucun juge de la famille Claude sur des témoins écrits par un modèle de cette famille | `preenregistrement-juges-idees-v2-brouillon4.md` l. 276 et l. 664 (`f7616284…`) | condition à vérifier pour le juge-tournoi (P1) |
| N-029 : juge Claude par l'interface sur P3 **retiré**, et « tout envoi de textes d'action du programme à un service tiers pour cette référence » ; crédits suggérés pour le papier C | `decision-N-029-v1.md` l. 32-33 et l. 46-47 | aucune base boîte noire de T0.6 ou T0.8 par Claude ; SHADE-Arena ou Liars' Bench avec moniteur Claude à T0.8 = écart au texte gelé, hors plan |
| N-052 : analyste Opus 5.5, contre-lecteur Fable 5.1 ; refus de Fable consigné, aucune bascule seule | `decision-N-052-v1.md` l. 31-34, l. 42-44 | P3 suit ces rôles |
| N-053 : juge d'une autre lignée (Qwen2.5-7B) en bras rapporté ; invariant « aucun score de moniteur ni de juge dans l'entraînement ou la sélection de l'agent » | `decision-N-053-v1.md` l. 33-37, l. 41-44 | aucun juge Claude ne sélectionne un agent ; P1 juge des lois, non des agents |
| N-058 : composition des proposeurs jugée sur l'oracle et le coût, jamais sur le verdict d'un juge | `decision-N-058-v1.md` l. 19-23 | le juge-tournoi est jugé lui-même par l'oracle (conception v1, l. 132) |
| N-060 v3 : deux lecteurs de deux familles **autres que celles des moniteurs** (ni Llama ni Qwen), aveugles | `decision-N-060-v3.md` l. 24-25 | Claude peut être **un** des deux lecteurs ; l'autre d'une autre famille (Kimi ou Argon, hors crédits) |
| N-064 et N-065 : juge-tournoi = rôle 1 de l'organisme, second terrain du papier C ; citations obligatoires | `decision-N-064-v1.md` l. 13-16 ; `decision-N-065-v1.md` l. 15-18, l. 23 | P1 appartient au papier C |
| Juge du juge-tournoi : « Opus sur les crédits Claude, après A1-v4 : go » (après R-1996, qui voulait Kimi et Argon) | `registres/decisions.md` l. 1984 (R-2026) ; l. 1954 (R-1996) | P1 permis ; conception v3 et devis à écrire, ligne de GO à inscrire avec eux |
| N-049 : banque sœur v3-bis, « même générateur que la banque v3 », sur devis et mot direct | `decision-N-049-v1.md` l. 51-54 | modèle du générateur **non vérifié** : P7 non chiffré |
| N-061 : NARCBench, Liars' Bench, SHADE-Arena, devis avant GO par ligne | `decision-N-061-v1.md` l. 12-13 | aucun poste Claude retenu (T0.8 gelé, N-029) |
| Cloison du bras d'attaque | consigne ; N-056 (montage « sans dépense ») | **aucun poste** ; rien de la cloison n'est envoyé à l'interface |
| R-2362, option (1) (brancher Claude Code sur la clé) **non retenue** par Lazar | `registres/decisions.md` l. 2320, l. 2323 | hors plan |

**Conséquence pour l'option (a) de R-2370** : un expérimentateur sur Claude n'est **pas compatible** avec les textes
scellés tant que les mondes plantés sont écrits par un modèle de la famille Claude. Le rendre compatible demanderait des
mondes écrits par une autre famille et un préenregistrement neuf (nœud : modification de méthode). Les crédits servent
l'expérimentateur **indirectement** : mondes neufs (P5), contre-lecture de son préenregistrement (P3), collisionneur (P4).

## 3. Postes candidats

Unité : USD sur crédits de Claude, au barème de la section 1, sans cache ni lots (borne haute). « Central / haut » :
hypothèses de jetons écrites.

### P1 — Juge du juge-tournoi façon Co-Scientist (papier C, rôle 1)

- **Usage** : juge principal des matchs du tournoi sur les cartes d'A1-v4 ; second juge d'accord sur un sous-ensemble.
- **Modèles** : Opus 5.5 principal, Fable 5.1 second (conception v1, l. 14 ; D-3, l. 276).
- **Estimation** (conception v1, § 5, l. 211-238) : débat 3 000 / 3 000 jetons (central), 6 000 / 6 000 (haut) ; T0
  (étalonnage 288 débats d'Opus, lois connues 1 152 appels d'Opus, 192 débats de Fable, **sans Argon**) : **115,2 /
  230,4** (l. 221), dont Opus seul 80,6 / 161,3. Course complète (T0 + T1 avec l'attaquant Argon) : Claude 250 à 350
  au central, pire cas réaliste 704,3, plafond de la v1 750 (l. 17, l. 238). Argon de T1 (15 à 97) et machine (≤ 35)
  **hors crédits**, GO à part.
- **Contraintes** : permis par R-2026 ; A1-v4 finie (verdict officiel, `registres/depenses.md`, ligne de GO-2026-11-02-22).
  **À vérifier avant le préenregistrement** : qui a écrit les lois et les cartes du monde W2 d'A1-v4 ; si c'est un modèle
  de la famille Claude, la règle des juges d'idées v2 (l. 276) s'applique et le bras doit le déclarer ou changer de monde
  (nœud). Aucun repli de modèle (v1, l. 68).
- **Calendrier** : conception v3 (Opus juge, reprise de la v1), préenregistrement, contre-lecture, scellement d'ici le 17 ;
  **T0 sur les comptes du 17** ; T1 seulement après lecture de T0, sur les comptes du 19.
- **Ligne de GO proposée** : « Juge-tournoi, manche T0, Opus 5.5 principal et Fable 5.1 second, sous préenregistrement
  scellé et contre-lu ; **plafond 235 USD sur crédits**, au plus 195 par clé (le solde d'un compte), arrêt dur au relais ;
  aucune dépense hors crédits ». Option (b) seulement : « manche T1, **plafond 450 USD sur crédits** », plus une ligne hors
  crédits pour Argon et la machine.

### P2 — Lecteur Claude de la vérité du dommage (N-060 v3 ; reprise de l'étiqueteur v2)

- **Usage** : oracle de couverture des contrôles ; épreuves de l'oracle (R5) avant toute lecture d'un épisode saboté, puis
  pilote. Opus 5.5 est le lecteur candidat retenu par la sonde de refus (GO-2026-11-09-03, `registres/go.md` l. 288).
- **Modèle** : Opus 5.5. Second lecteur d'une autre famille (Kimi ou Argon), hors crédits.
- **Estimation** : mesuré 0,040 USD par réponse d'Opus (15,726116 USD pour 391 réponses du lancement interrompu,
  `registres/depenses.md` l. 411 et R-2013 l. 1971) ; épreuves ≈ 200 appels et pilote ≈ 700 → **≈ 36 USD**.
- **Contraintes** : N-060 v3 l. 24-25 (famille hors moniteurs : tenue) ; relance par texte neuf contre-lu, noms neufs,
  dépense cumulée (R-2013) ; **vérifier les conditions d'exclusivité des courses en marche** avant tout appel (faute de
  R-2013).
- **Calendrier** : dès que l'ordre N-060 v3 est scellé ; tranche 0 (clé Rigaud).
- **Ligne de GO proposée** : « Oracle de couverture N-060 v3, lecteur Opus 5.5, épreuves puis pilote ; **plafond 45 USD
  sur crédits** (clé Rigaud) ; second lecteur hors crédits sous sa propre ligne ».

### P3 — Contre-lectures par l'interface (N-052)

- **Usage** : contre-lectures de second modèle des textes à sceller (conception v3 et préenregistrement du juge-tournoi,
  ordre N-060 v3, préenregistrement de l'expérimentateur, textes de G0) ; Fable 5.1 contre-lecteur, Opus 5.5 relecteur
  du brief. **En complément** de la contre-lecture R2 par un sous-agent neuf (qui vérifie sur disque), **jamais à sa
  place** : un appel sans outils ne relit ni empreintes ni fichiers.
- **Estimation** : par contre-lecture, 150 000 à 300 000 jetons d'entrée (texte et pièces), 15 000 à 40 000 de sortie
  (réflexion comprise) : Fable 5.1 2,25 à 5,0 USD ; Opus 5.5 0,9 à 2,0. Douze de chaque : **≈ 38 à 84 USD**.
- **Contraintes** : rôles de N-052 ; refus de Fable consigné, aucune bascule ; garde de fuite : aucun fichier de la cloison,
  du mode tenu à l'écart ni des sorties scellées non lues dans les envois (liste blanche de chemins par appel).
- **Calendrier** : 30 USD en tranche 0, le reste avec les comptes du 17.
- **Ligne de GO proposée** : « Contre-lectures par l'interface, Fable 5.1 et Opus 5.5, liste blanche des fichiers envoyés ;
  **plafond 70 USD sur crédits**, au plus 6 USD par contre-lecture ».

### P4 — Collisionneur (questions de conception difficiles ; préparation de l'entretien)

- **Usage** : tours de l'étage III sur les questions de conception cruciales à venir (nombre de mondes et puissance de
  l'expérimentateur, conception v3 du juge-tournoi, critères 2 à 8 de G0 avant l'entretien du 27).
- **Modèles** : espèces Claude (Fable 5.1, Opus) ; les autres espèces hors crédits.
- **Estimation** : part Claude mesurée ≈ 8,0 (l. 412) et 5,58 (l. 418) par tour ; quatre tours **≈ 22 à 32 USD**.
- **Contraintes** : plafond de script ≤ 15 par tour (GO-2026-11-11-03) ; règle des journaux de fournisseurs (R-2389).
  GO-2026-11-09-05 (entretien, ≤ 30 sur crédits, échéance le 21, `registres/go.md` l. 290) **reste en vigueur et n'est pas
  cumulé ici** ; aucune dépense relevée sous elle.
- **Ligne de GO proposée** : « Collisionneur, quatre tours au plus ; **plafond 40 USD sur crédits**, 15 par tour ; devis
  consigné avant chaque tour ».

### P5 — Mondes plantés neufs, jamais publiés (pour l'expérimentateur)

- **Usage** : la synthèse demande, pour tout duel décisif, des mondes neufs jamais versés au dépôt public, en nombre fixé
  par un calcul de puissance (`synthese-v1.md` l. 196, l. 233-235, l. 326-330 ; n ≈ 37 pour une puissance de 0,8,
  l. 263). Opus 5.5 écrit les lois et les mondes ; un programme les vérifie.
- **Estimation** : par monde, conception 30 000 / 20 000 jetons et vérification 30 000 / 5 000 → ≈ 0,74 USD ; 50 mondes
  **≈ 37 USD**.
- **Contraintes** : mêmes conditions que la v66 (lois écrites par un modèle de la famille Claude) : **Claude reste exclu de
  tout rôle** dans l'organisme sur ces mondes — choix à déclarer, qui verrouille l'exclusion ; mondes gardés hors du dépôt
  public (`lciric/ideation-organism`) et hors de la copie expurgée ; écrits par une instance qui n'a lu aucun score.
- **Calendrier** : tranche 0, après le calcul de puissance du pilote A/A.
- **Ligne de GO proposée** : « Génération de 50 mondes plantés neufs par Opus 5.5, gardés privés ; **plafond 45 USD sur
  crédits** ».

### P6 — Pilote d'instrument du papier C, EC.1 (juges génératifs hétérogènes)

- **Usage** : instrument de g sur trois juges Claude (Haiku 5.5, Sonnet 5.5, Opus 5.5) sous les cinq familles d'attaque
  (programme v2, l. 151 et l. 194), sur des items de pilote séparés des items décisifs ; exploratoire, non opposable.
- **Estimation** : ≈ 1 000 appels par juge, 3 000 / 300 jetons : Opus ≈ 18, Sonnet ≈ 9, Haiku ≈ 0,5 → **≈ 28 USD**.
- **Contraintes** : ordre exploratoire scellé avant tout appel (R1 pour l'instrument) ; papier C prévu en phase 1
  (programme v2, piste C) : **nœud de périmètre** avant G0 ; N-029 l. 46-47 le suggère. Puits de fin de cycle, si des
  crédits restent avant l'expiration.
- **Ligne de GO proposée** (option (b)) : « Pilote d'instrument EC.1, trois juges Claude, ordre exploratoire scellé ;
  **plafond 35 USD sur crédits** ».

### P7 — Banque sœur v3-bis (N-049) — non chiffré

Modèle du générateur de la banque v3 **non vérifié** dans ce passage. Si c'est un modèle Claude, la v3-bis se paie sur
crédits (devis à écrire, mot direct de Lazar, N-049 l. 51-54) ; sinon, la payer sur Claude changerait le générateur
(écart) : hors plan.

### Hors plan (vérifié)

Expérimentateur sur Claude ; proposeurs ou juges Claude dans l'organisme ; base boîte noire Claude sur T0.6 ou T0.8 ;
moniteur Claude pour SHADE-Arena ou Liars' Bench à T0.8 ; bras d'attaque informé ; option (1) de R-2362.

## 4. Calendrier et clés

| tranche | clés | lignes | plafonds |
|---|---|---|---|
| 0 — du 12 au 16 | `RR_ANTHROPIC_API_KEY_RIGAUD` (≈ 165 restants) | P2 45, P3 30, P4 40, P5 45 | 160 |
| 1 — à partir du 17 | comptes débloqués le 17, une variable nommée par compte (`RR_ANTHROPIC_API_KEY_<COMPTE>`, nom à fixer par Lazar) | P1-T0 235 (deux clés), P3 40 | 275 |
| 2 — à partir du 19 | comptes débloqués le 19 | option (b) : P1-T1 450 ; P6 35 | 485 |

- **Plafond par clé** au relais, au plus le solde du compte ; une ligne qui vise plusieurs clés porte un plafond par clé.
- **Comptes disponibles avant le 17 sans clé déposée** : s'il y en a, ils avancent la tranche 1 (à dire par Lazar).
- **Fin de cycle à vérifier** : si elle tombe avant la fin novembre, P6 et le reliquat de P3 passent avant.

## 5. Sommes

| option | lignes | plafonds sur crédits | hors crédits (GO à part) |
|---|---|---|---|
| (a) prudent | P1-T0, P2, P3, P4, P5 | **435** | second lecteur de P2 |
| (b) complet | (a) + P1-T1 + P6 | **920** | + Argon de T1 (15 à 97) et machine (≤ 35) |
| (c) minimal | P2, P3, P4 | **155** | second lecteur de P2 |

Attendu au central pour (a) : ≈ 80 à 115 (P1-T0) + 36 + 40 à 60 + 22 à 32 + 37 ≈ **215 à 280 USD** ; le reste des
crédits expire si (b) n'est pas décidé.

## 6. Décision pour Lazar

- **Décision** : adopter ce plan comme cadre de dépense des crédits de Claude, chaque ligne restant sous un GO chiffré de
  toi.
- **Enjeu** : ≈ 965 USD de crédits qui expirent sans report, contre les textes scellés (Claude exclu de l'organisme, N-029)
  et le temps de préparation avant l'entretien du 27.
- **Options** :
  - (a) **prudent, ≈ 435 USD de plafonds** : juge-tournoi T0, vérité du dommage, contre-lectures, collisionneur, mondes
    neufs. Avantage : tout est permis par les textes et déjà dans la file. Inconvénient : ≈ 500 USD de crédits perdus au
    plus.
  - (b) **complet, ≈ 920 USD** : (a) plus la manche T1 du juge-tournoi et le pilote EC.1 du papier C. Avantage : utilise
    presque tout ; le papier C reçoit sa mesure principale. Inconvénient : T1 demande aussi Argon et une machine hors
    crédits ; EC.1 est un nœud de périmètre avant G0 ; charge de travail lourde avant le 27.
  - (c) **minimal, ≈ 155 USD** : vérité du dommage, contre-lectures, collisionneur. Avantage : aucune course longue.
    Inconvénient : plus de 800 USD perdus ; le juge-tournoi reste sans juge.
- **Recommandation** : (a) maintenant ; (b) décidée après la lecture de T0 (vers le 21), sur les comptes du 19.
  **Confiance 0,65.** En plus, à part : passer le contre-lecteur de N-052 de Fable 5.1 à Fable 5.2 (moins chère, plus
  récente) est un changement de modèle : ton mot seulement.
- **Défaut sous 48 heures** : (a) comme cadre ; **aucune dépense sans ligne de GO chiffrée de ta main** ; les lignes de la
  tranche 0 (P2, P3, P4, P5 : 160 USD au plus, clé Rigaud) te sont présentées une à une.
