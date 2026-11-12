# Programme complet de l'organisme d'idéation — architecture : couches, mécanismes, état (v1)

- **Pour** : Lazar. **Écrit par** : un sous-agent neuf (rédacteur, Claude Opus 5.5) de la session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv`, le 10 novembre 2026, à partir de 11:59 UTC (heures relevées par `date -u`).
  **Statut : non contre-lu.** La passation de la mère prévoit une contre-lecture par un autre modèle avant la remise.
- **Demande de Lazar** (verbatim, R-2200) : « ecir smoi le programme complet exhaustif avce toutes les couchhes et mecanismes
  prevus pour l'org » ; « precise bine dans le programme toutes nos idees hypotheses resultats proposiitons pour que rien de notre
  brinstorm ne soit perdu ».
- **Partage du travail.** Ce texte donne l'**architecture** : couches, mécanismes, rôles, état exact de chaque pièce, dépenses,
  nœuds et prochains pas. L'**inventaire exhaustif des idées** (chaque idée, objection, piste écartée, question ouverte) est écrit
  en parallèle par un rédacteur voisin, dans le même dossier (`inventaire-idees-organisme-v1.md`, `sorties-non-lues-v1.md`). Les
  deux textes ensemble répondent à la seconde demande.
- **Sources.** Chaque chiffre et chaque affirmation porte un renvoi **[RAn]** au registre des affirmations
  (`registre-affirmations-programme-v1.md`), qui donne le chemin, la ligne et l'empreinte. Ce qui n'a pas de source est écrit
  « sans source ».
- **Ce que ce texte n'ouvre pas** (cloison R-2152, R-2170, et interdits de la consigne) : rien du bras d'attaque au-delà des
  décisions inscrites ; rien du mode tenu à l'écart au-delà de son existence ; aucune sortie de collisionneur ni réponse de modèle
  non synthétisée (elles sont listées en annexe A) ; aucune recette d'attaque contre un juge ou un moniteur (niveau méthode, R-607).

## Verdict

1. **L'organisme d'idéation est un instrument codé, éprouvé hors ligne, dont le juge a été attaqué et réparé ; sa boucle complète
   n'a jamais tourné avec de vrais agents.** Orchestrateur publié jusqu'à la version 64, version 65 sur une branche, non contre-lue ;
   nul de production v8, nul v9 candidat au prix « puissance perdue » [RA1, RA2, RA3].
2. **Les propriétés de l'objectif ultime sont des cibles décidées, pas des pièces codées** : l'organisme ne se conçoit pas seul,
   rien n'est figé après conception, son universalité n'est pas mesurée sur des familles inédites (R-2152) ; les couches 3
   (réécriture de soi) et 4 (pôle théorie et Lean) sont fermées jusqu'aux résultats de l'étape 2, sauf un essai sur processeur
   [RA4, RA5].
3. **Le prochain pas qui engage est la plus petite course réelle de la boucle complète** (45 dollars, jusqu'au 30 novembre), après
   la contre-lecture du code v65, une machine à bac à sable et un préenregistrement scellé ; **un point neuf est à trancher avant** :
   l'empreinte de la configuration v5 exigée par GO-2026-11-10-10 n'est pas celle du code v65 rendu [RA6, RA7].

## Comment lire les états

| mot | sens dans ce texte |
|---|---|
| **codé** | le code existe, avec sa version et son commit ; « essayé hors ligne » : essais et démonstrations sans appel de modèle |
| **couru** | joué avec de vrais modèles, dépense réelle, sortie scellée |
| **décidé** | fixé par une décision de Lazar (note N-…, ligne R-… ou GO-…) |
| **prévu** | écrit dans un texte de conception, sans décision formelle ni code |
| **fermé** | décidé de ne pas le faire pour l'instant, par un nœud nommé |
| **suspendu** | décidé, puis arrêté par une décision |
| **proposé, non tranché** | nœud ouvert chez Lazar |
| **idée non retenue** | écartée, avec la pièce qui l'écarte |

Deux homonymies à garder en tête. (1) Au registre, « organisme » désigne aussi les **organismes-modèles saboteurs** du programme de
contrôle (T0.5, T0.6) ; ce texte ne traite que de l'organisme d'idéation. (2) « Couche 1 bis » et « couche 2 » désignent au registre
des bancs du programme (banque complète de T0.5 ; banque des deux modes connus) **et** des couches d'essai de l'organisme ; la
section 2 les distingue [RA8].

---

## 0. L'organisme en une page

L'organisme d'idéation a deux moitiés, reliées par un pont [RA9] :

- **La prise d'idéation (« course »).** Des modèles de plusieurs fournisseurs (Claude, Kimi, Argon) écrivent des **fiches d'idée** à
  champs fermés (hypothèse, effet prédit, mesure qui la tuerait). Un **aiguilleur** les classe par leur seule forme et délivre un
  passeport ; une **mémoire** refuse les redites ; des **juges** de fournisseurs différents les notent à l'aveugle les uns des autres ;
  un **bisociateur** marie des idées que personne n'a écrites ; un **moissonneur** vérifie la nouveauté sur les métadonnées d'arXiv
  et d'OpenAlex.
- **Le pôle de test.** Une **fiche-loi** engage une loi prédictive chiffrée sur des issues ; un **juge statistique**, calculé par
  l'orchestrateur hors de tout agent, la promeut ou non contre un nul formé des lois connues ; les fiches promues passent des
  **tests de mort** dans un bac à sable ; la **sélection** nourrit la génération suivante.
- **Le pont fiche → loi** traduit une fiche d'idée en fiche-loi (codé, essayé, non intégré : section 4.3).

**Règle de conception** : « le rôle qui produit un artefact ne tient jamais la clé qui l'évalue » ; l'humain fixe les questions,
signe les plafonds et les nœuds, lit les registres scellés, et ne touche pas aux verdicts [RA10].

Parcours d'une idée (figure 1 du dépôt public, en texte) : proposer → aiguiller (forme seule ; une fiche trop concrète part, scellée,
au coffre que ni agent ni juge ne lit) → mémoire anti-redite → juges croisés et bisociateur → contrôle de nouveauté → pari (pôle de
test) → tests de mort → sélection → génération suivante. Une flèche n'était pas fermée au 1er novembre : la sélection après les tests
de mort existait en code depuis la v57b sans être relue par la génération suivante ; la v59 ferme cette boucle en code, jamais
courue avec de vrais agents [RA11].

---

## 1. Objectif ultime et lien entre les deux lignées

### 1.1 L'objectif ultime (N-044, décidé le 25 octobre)

Mots de Lazar (24 octobre, 23:51) : « on veut un organisme universel qui se conçoit seul mais une fois conçu est câblé dans son
architecture méta » ; (25 octobre, 00:05) l'universalité « se gagne sur des familles inédites, pas sur des items inédits des mêmes
familles » : « je veux ça pour l'objectif ultime, mets-le dans le programme » [RA12].

| énoncé retenu (N-044) | état |
|---|---|
| un organisme qui **se conçoit seul**, sur un vivier de tâches réelles à vérité connue, avec le droit de se réécrire | **décidé** ; **non atteint** (R-2152) [RA12, RA4] |
| une fois sa méta-architecture **figée**, il répond à des questions nouvelles sans réentraînement ni réorganisation | **décidé** comme cible ; le « code figé après la conception » reste **en attente du mot de Lazar** (portée de N-044) [RA12] |
| **universalité mesurée sur des familles jamais vues à la conception** (familles engendrées, familles de l'autre fournisseur, provenance réelle ; H-G4 et successeurs), jamais sur des items inédits des familles de conception | **décidé** ; **non mesurée** (R-2152) [RA12, RA4] |
| **trois régimes de budget** : conception (réécriture libre, majorité du budget, arrêt sur le critère de l'organisme) ; usage (code figé, apprentissage interne : mémoire, sondes, paramètres) ; re-conception (rare, déclenchée par l'organisme, sur une réserve bornée tenue par le noyau) | **proposé, non tranché** (proposé le 24 octobre ; en attente du mot de Lazar) [RA12] |
| **vivier de conception** distinct de la banque scellée (identifiants disjoints du test et du test final) | **décidé** (« GO now ») ; **codé dans le noyau de l'étape 1** (`noyau/vivier.py`, R-378, cité par N-049), base de code distincte de l'orchestrateur d'idéation [RA12, RA13] |
| **questions ouvertes** posées aux organismes avant tout matériau ; réponse scellée, matériau jamais consigne | **décidé** ; aucune occurrence dans le code public de l'orchestrateur [RA12, RA14] |
| **diversité** : trois bras à l'étape 2 (mission et miroir fonctionnel ; contrainte câblée ; rien) ; organisme de Gemini rapporté à part ; « le juge est la seule pression » ; un résultat négatif se publie | **décidé pour l'étape 2** ; étape 2 non commencée (aucune ligne du registre consultée n'en rapporte de préenregistrement ni de course) [RA12, RA15] |

### 1.2 Ce que N-045 ajoute (v2, 25 octobre) — à partir de l'étape 2

Composition de l'organisme apprise (modèle par rôle compris), coût dans le signal rendu à l'organisme, nécessité de la frontière
mesurée, voies bon marché avant la voie chère, héritage d'une génération récompensé, phasage en deux expériences bon marché, espaces
de conception égaux. Tous **décidés**, aucun **codé** dans l'orchestrateur d'idéation ; détail en section 6 [RA16, RA14].

### 1.3 Deux lignées, un seul organisme (décision R-2152, 10 novembre, 10:30 UTC)

| lignée | ce qu'elle a produit | sources |
|---|---|---|
| **A — « organisme de l'objectif ultime »** (conception avec la lignée conv-audit) | noyau commun et contrat des organismes ; étape 1, « gradient conçu par l'essaim » (sondes ; extraction des traits sur la banque scellée `confrontation-v1`, GO-2026-10-24-05) ; pilotes de conception sur des organismes écrits par Gemini (versions 4 à 6.3) et confrontation des essaims (GO-2026-10-24-01, -02) ; énoncés N-044, N-045, N-049, N-050, N-052 | [RA17] |
| **B — « organisme d'idéation »** (« pôle scientifique automatique », lignée conv-audit puis session-dépôt et mère) | orchestrateur du pôle, versions 0 à 65 ; « voie hybride ancrée sur notre noyau » retenue le 26 octobre ; prise « idéation » demandée par Lazar le 28 octobre (v31) | [RA18] |

**Décision (R-2152)** : l'organisme d'idéation **est** l'organisme de l'objectif ultime (N-044, N-045), branché depuis le
28 octobre 2026 sur la tâche « proposer des hypothèses de recherche jugées par un juge statistique » (R-632 à R-637, N-058 point 3),
**sans rupture de code** jusqu'aux versions 64 et 65 ; la boucle fermée du code v65 en est le premier pas ; l'organisme de Gemini est
une **conception concurrente rapportée à part** [RA4]. Je n'ai pas vérifié moi-même la continuité du code entre le noyau de l'étape 1
et l'orchestrateur du pôle : elle est affirmée par la décision, sans pièce de code lue ici.

### 1.4 Ce que l'organisme n'a pas encore

- **Il ne se conçoit pas seul ; rien n'est figé après conception ; son universalité n'est pas mesurée** sur des familles inédites
  (R-2152) [RA4].
- **Aucune récompense, aucun score net, aucune espèce locale, aucune question ouverte, aucun vivier tiré par génération, aucun
  `test_final`** dans le code public de l'orchestrateur : recherche par `git grep` à la tête `6510199` (aucune occurrence de
  « récompense », « score net », « LOCAL: », « question_ouverte » ; « vivier » n'y désigne que le réservoir d'instances du pôle ;
  « héritage » y désigne la transmission de la preuve et de la sélection, pas une récompense) [RA14].
- **Pas de réécriture de soi** : couche 3 fermée (section 2.4) [RA5].
- **La boucle complète n'a jamais couru** : tests de mort et boucle entre générations « implémentés, essayés hors ligne, jamais
  courus pour de vrai » [RA19].
- **Composition fixée par configuration**, jamais apprise : par exemple Kimi et Argon proposent dans la course réelle minimale, sans
  rôle pour Claude ; côté Claude, l'organisme n'admet que Opus 5.5 et Fable 5.1 (décision du 27 octobre, codée) [RA20].

---

## 2. Les couches

### 2.1 Trois numérotations, à ne pas confondre

| numérotation | où | contenu |
|---|---|---|
| (i) **couches d'essai sur le monde réel** (« une question, une porte par couche ») | programme de conception de l'organisme, v6 § 4 (l. 167-183), inchangé en v7 | 0 monde caché ; 1 banque réelle figée ; 1 bis banque complète ; 2 banque avec sabotage ; 3 épisodes ou moniteurs neufs à la demande ; 4 bras d'attaque en quarantaine et pôle théorie |
| (ii) **ordre de conception** | même programme, v6 § 3 (l. 111-166), v7 § 3 | 1 proposeur à liberté bornée et monde du programme (v7) ; 2 réécriture des rôles sous bac à sable (v8) ; 3 bras d'attaque, remplacé le 28 octobre par neuf voies de mesure adversariale ; 4 pôle théorie, Lean comme vérificateur |
| (iii) **couches 3 et 4 de l'organisme** au sens du nœud N12 | R-920 ; synthèse N12-N13 | couche 3 = réécriture de soi sous bac à sable (génération de pièces neuves : moniteur, sous-agent à consigne auto-rédigée, règle d'agrégation écrite en code) ; couche 4 = pôle théorie et Lean |

**Lecture retenue ici** [RA21, RA22, RA23] : la couche 3 de N12 réunit la couche d'essai 3 (moniteurs ou épisodes neufs à la
demande, qui est aussi la sortie `loi_couche_3` du pont fiche → loi) et le point 2 de l'ordre de conception (réécriture sous bac à
sable) ; la couche 4 est le pôle théorie des deux autres numérotations, **sans** le bras d'attaque, qui n'est plus une pièce de
l'organisme (suspendu le 28 octobre, R-597 de la session-dépôt, remplacé par neuf voies ; il n'est pas le mandat de la mère :
N-056, R-2045, R-2047). **Trou** : dans la numérotation (iii), les couches 1 et 2 ne sont définies dans aucune pièce lisible que j'ai
lue ; la question N12-N13 qui les fixait peut-être est sous `donnees/`, non ouverte. La suite suit la numérotation (i), et (iii) pour
3 et 4.

### 2.2 Les couches, une par une

| couche | définition | état | porte de sortie | sources |
|---|---|---|---|---|
| **0** | monde caché tenu par le noyau, vrais agents (option (a)) ; coût estimé 10 à 50 USD | **codé** v6 (`monde_noyau.py`, 0.6.0) ; **couru** le 27 octobre : (a), puis (a) bis « passée propre » (5,89 USD) ; dans un monde volontairement tautologique, 2 témoins vrais promus, 2 faux éliminés, 11 rejeux sur 11 identiques — la plomberie, pas la puissance | « plomberie tenue » : **franchie** | [RA24] |
| **1** | banque réelle figée en cache : pilote de T0.5 (180 épisodes du modèle de 8 milliards de paramètres, notés par deux juges de 3 et 8 milliards) ; banque v2 de 120 épisodes et 13 moniteurs ; nul informé ; sans urne ; sans carte graphique | **codé** v7 (`monde_banque.py`, 0.7.0 ; conception `conception-v7-v1.md`) ; **essayé hors ligne**, agents simulés : « pas de dents » sur les moniteurs réels (banque trop petite) | « le pôle retrouve seul le connu (traits du texte qui prédisent le score, N-029) » : **non jugeable** sur les moniteurs réels | [RA25] |
| **1 bis** | banque T0.5 complète (192 épisodes sans `e2`, 96 tâches ; parties 48 / 48 / 96 par tâche), puis 288 épisodes à graines neuves | **lue** le 27 octobre : validité tenue (aucun témoin faux promu), dents sur témoins plantés jusqu'à la force 0,5 à 96 épisodes par fiche, rien sur les 13 moniteurs réels ; **lecture préenregistrée** des 288 épisodes à graines neuves (2 novembre) : issue I1, « valide et avec des dents, aucune loi réelle promue » (0 témoin faux promu sur 19 ; borne : une loi de la forme plantée portant 0,057 à 0,117 nat par épisode serait promue avec probabilité 0,9) | porte jugée sur témoins plantés seulement | [RA26] |
| **2** | banque avec sabotage : organismes de T0.6, sondes de T0.7, bases de T0.8, notés une fois ; dimensionnée par le pari apparié borné (dizaines d'unités sabotées par mode, calibrage honnête de 10 à 16 fois les unités sabotées à 1 % de faux positifs ; strates « diffus / concentré » et « floue / nette ») | **prévu** ; **non construite pour le pôle** ; dépend des courses du programme de contrôle et de leurs verrous de lecture | « témoins plantés et résultats établis retrouvés ; première lecture de H2 » | [RA27] |
| **3** | moniteurs ou épisodes neufs à la demande ; réécriture de soi sous bac à sable | **prévu** ; **fermé** jusqu'aux résultats de l'étape 2 (N12 (b), R-959) | « coût mesuré sur une fiche pilote avant toute course » | [RA21, RA5] |
| **4** | pôle théorie : juge = vérificateur de preuves (Lean) ; proposeur nourri par le moissonneur et la recombinaison | **prévu** (« go » du 27 octobre) ; **fermé** sauf l'essai sur processeur « preuve formelle contre suite bon marché » (N12 (b)) ; pas (a) de R-2199 **lancé** le 10 novembre | « failles connues retrouvées avant toute inédite » (porte écrite pour le bras, alors dans la même couche) | [RA21, RA5, RA28] |

**Mesure prévue à chaque couche** : fiches vraies promues par dollar ; zéro fausse découverte sur les témoins ; ce que le pôle a
trouvé que nous ne savions pas, lu dans les deux sens (R4). **Anti-gaspillage** (codé ou à coder) : plafond par génération et par
agent ; réserve par appel au relais ; arrêt quand plus rien ne survit ; témoins plantés à chaque génération (une génération 0 qui
rate ses témoins arrête la course) ; pilote d'une fiche avant toute course coûteuse ; rien ne repart sans lecture de la course
précédente [RA29].

**Question des couches** : proposée, « le pivot du programme — le sabotage diffus déplace-t-il la marginale des scores de sonde, et
l'accumulation séquentielle rattrape-t-elle ce que le seuil par action manque (H2) — réécrit en lois par instance » ; « à confirmer
par Lazar » au 28 octobre ; aucune confirmation trouvée au registre (sans source) [RA29].

### 2.3 Couche 2 — ce qui la sépare du pôle

La « couche 2 » du registre (« banque des deux modes connus », GO-2026-10-28-02, porté à 90 USD jusqu'au 15 novembre ; pilote de la
couche 2 devisé à ≈ 234 USD au centre, non accordé) est la **banque de G1 du programme de contrôle** ; la couche d'essai 2 du pôle
en serait l'usage par l'organisme [RA27]. Au 29 octobre, le programme d'entretien v16 écrivait : « Rien de cela n'existe encore en
données » [RA27]. Je n'ai trouvé aucune pièce qui pointe le pôle sur une banque de sabotage ; les épisodes des courses de T0.6 sont
sous verrous de lecture du programme et ne sont pas une banque du pôle.

### 2.4 Couche 3 — réécriture de soi sous bac à sable (fermée)

- **Définition** (ordre de conception, point 2) : l'organisme peut proposer une réécriture de ses propres rôles (consignes,
  stratégies, code des rôles) ; **une réécriture est une fiche** : elle prédit une amélioration mesurable (fiches vraies promues par
  dollar sur des témoins et des mondes neufs) et est jugée par le même juge, en duel contre la version d'avant ; **jamais le noyau**
  (juge, monde, témoins, signature de la mémoire, budget, clés) ; elle ne commence qu'**après un résultat sur une vraie question**
  [RA22].
- **Fermeture** : N12 tranché **(b)** par Lazar le 1er novembre : couches fermées jusqu'aux résultats de l'étape 2 ; mesure, au
  préenregistrement de l'étape 2, de ce que le catalogue manque [RA5].
- **Ce qu'en dit le collisionneur N12-N13** (synthèse scellée v2, quatre espèces) [RA30] :
  - accord large (quatre espèces, réserve R4 « trop propre ») sur une **ligne de partage** : la composition et la sélection apprises
    (couvertes par N-045) contre le **code hors catalogue** et la **vérification formelle** (non couverts) ;
  - priorité commune : **étape 2 d'abord** ;
  - quatre **risques** nommés, un par espèce : violation de l'invariant de N-053 (un organisme qui écrit ses moniteurs et s'en sert
    pour se sélectionner) ; coût d'opportunité inverse d'un organisme figé ; **circularité du bac à sable** (seul risque adossé à un
    fait servi) ; effets indirects et déplacement du problème ;
  - **divergence non résolue n° 1** : des moniteurs neufs peuvent-ils servir de filtre de fiches (lecture de N-058 : « l'interdit
    porte sur la sélection d'agents, pas sur celle des fiches ») — « à faire confirmer par Lazar ».
- **Tour 2 N12-N13** (collisionneur v8, cinq espèces) : **payé, scellé, non lu** (15/15 cellules, 15,60 USD) ; sa lecture est le pas
  (a) de R-2199, lancé le 10 novembre (critères de lecture à sceller avant toute ouverture) [RA28, RA31].
- **Dans le code** : seule trace, la sortie `loi_couche_3` du pont (une loi qui exige des épisodes neufs, avec « une demande
  d'épisodes au niveau méthode ») ; pont non intégré à l'orchestrateur [RA23].

### 2.5 Couche 4 — pôle théorie et Lean (fermée, sauf un essai) ; l'écart vérification / génération

- **Définition** (ordre de conception, point 4) : juge = vérificateur de preuves (Lean) ; proposeur nourri par le moissonneur et la
  recombinaison ; questions ouvertes du programme (agrégateur sous corrélation adverse, théorème négatif) ; aucune dépense de carte ;
  installation de Lean sans dépense. « Go » de Lazar le 27 octobre (14:32) ; « ne pas promettre de révolution, mesurer ce qui sort »
  [RA22].
- **État** : n'existe pas (R-920, 31 octobre) ; **fermée** par N12 (b), qui n'autorise qu'un **essai sur processeur « preuve
  formelle contre suite bon marché »** (devis d'appels de sous-agents) [RA5, RA32].
- **Collisionneur N12-N13** : accord large à quatre sur « **l'empreinte ne prouve pas la validité** d'une preuve » ; convergence
  née de la critique : Lean doit battre une **suite bon marché** (lecteur neuf outillé symbolique et numérique, tests, mutations,
  relecture par une autre famille) — accord jugé trop propre (réserve R4) ; formes d'ouverture discutées : sur une classe d'erreurs
  mesurée, lemmes critiques seulement, ou vérificateur externe d'abord (divergence non résolue n° 5) [RA30].
- **Écart vérification / génération** : la recherche du 10 novembre conclut qu'**aucune partie de l'organisme ne produit de
  mathématiques nouvelles** ; la couche 4 prévue **vérifie** des preuves, elle n'en **génère** pas ; le code ne connaît que le renvoi
  **N3** du pont : « relève d'une preuve ou d'une simulation hors banque (pôle théorie), pas d'épisodes » (`pont_v1.py`, l. 45)
  [RA33].
- **Décision de Lazar du 10 novembre (R-2199)** sur le pilier « mathématiques nouvelles », dans cet ordre :
  (a) lecture du tour 2 N12-N13 (critères scellés avant ouverture, synthèse par un lecteur neuf, sans dépense) — **lancé** ;
  (b) **devis** de l'essai sur processeur « preuve formelle contre suite bon marché », puis GO — **prévu** ;
  (c) **note de conception du pilier « génération »** (conjectures, démonstrations, Lean comme arbitre, juge de nouveauté) — **nœud
  chez Lazar** [RA28].
- **Voisin direct** : la voie (b) de l'ordre de conception v7, « théorie adversariale du contrôle » (« je m'y engage à fond »), prédit
  où des failles adaptatives peuvent vivre **sans en construire une** : sortie = conditions mesurables sur les moniteurs, à partir
  de la carte des hypothèses (23 hypothèses, 21 lemmes prouvés) ; « le pôle théorie (point 4 : Lean comme vérificateur) sert cette
  voie directement » ; processeur seul [RA34].

### 2.6 Les neuf voies de mesure adversariale (ordre de conception, point 3) — existence seulement

Le bras d'attaque de l'organisme (fiches-recettes en quarantaine, point 3 de la v6) a été conçu, scellé, puis **suspendu** (R-597 de
la session-dépôt : lanceur arrêté par un classifieur de sécurité ; aucune relance ni reformulation) ; Lazar a accepté le 28 octobre
**neuf voies** de remplacement, nommées (a) à (i) dans la v7 : concepteurs humains indépendants ; théorie adversariale du contrôle ;
observation des données existantes ; adversaire scellé ; adversaire analytique par résolution de contraintes ; audit automatisé à
taxonomie fixée ; transfert adversarial entre domaines ; validation croisée entre moniteurs ; génération adversariale de cas de test
sans agent. La sortie de la voie (d) est au **niveau méthode** (classe, mécanisme, conditions, défense ; jamais la recette) [RA35].
Ce texte ne les développe pas : hors de l'organisme d'idéation tel que la mère le tient, et cloison du bras (les sections 3 bis et
3 ter de la v7 n'ont pas été lues).

---

## 3. Rôles et pôles du code

### 3.1 Les rôles

Rôles des agents déclarés par le code : `experimentateur`, `verificateur`, `recombinaison`, `synthese`, `proposeur`,
`proposeur_ideation`, `juge_ideation` (v31) ; `experimentateur_test`, `lecteur_test` (v48, étage des tests de mort) ; Kimi par
protocole : `proposeur_ideation`, `juge_ideation`, `fusion_ideation` [RA36].

| rôle | ce qu'il fait | qui le joue | fichiers et versions | état |
|---|---|---|---|---|
| **proposeur** (pôle de test) | formule les fiches-lois d'une génération à liberté bornée : gabarit, catalogue de stratégies, contexte sans aucune issue ; enfichable (proposeurs de référence sans modèle) | Opus 5.5 prévu ; références scriptées | `proposeur.py` (0.7.0, pièce 4 de v7) ; `proposeurs_references.py` (v7, version 7) ; `proposeurs_references_v59.py` | **codé** ; références mesurées sur 20 mondes : mécanique 23/35, scripté 5/35, hasard 1/35 [RA37] |
| **proposeur d'idée** (`proposeur_ideation`) | écrit les fiches d'idée à champs fermés | Claude (Opus 5.5, Fable 5.1), Kimi par protocole, Argon par commande externe | `ideation.py` (v31, puis v42) ; `ideation_v2.py` (v51) ; `ideation_v59.py` ; `adaptateur_kimi_v53.py` | **codé** ; **couru** : course 1 (29 fiches, 27 éligibles, 17 idées distinctes) ; second tour réel du 1er novembre (Kimi et Argon, 12 fiches classées) [RA38] |
| **aiguilleur** (« douane ») | classe chaque fiche par sa **forme** (niveau méthode, à corriger, trop concrète), délivre un passeport ; étape **protégée**, jamais sacrifiée au budget | session neuve, consigne figée, une fiche anonyme par appel | `aiguilleur_v53.py` (R-575, M4) | **codé** v53 ; **couru** ; consigne de l'aiguilleur v1 reçue (`c2efa120…`) ; la mesure M4 n'est pas calculée par v53 à v56 (« v57 à écrire ») [RA39] |
| **mémoire anti-redite**, **coffre**, **caviardage** | indexe l'archive et refuse les redites (intra-lot, entre fournisseurs, contre les générations passées) ; le coffre garde verdicts et clés scellés jusqu'à la fin déclarée ; le caviardage retire les formes de clé connues avant toute écriture | code de l'orchestrateur | `memoire.py`, `memoire_v53.py` ; `coffre_v53.py`, `coffre_v55.py` ; `caviardage.py` | **codé** [RA40] |
| **juges croisés** (`juge_ideation`) | chaque fiche munie d'un passeport est notée par **chacun** des juges, un appel par fiche et par juge, session neuve, identifiant opaque | Kimi, Argon, Opus 5.5 (troisième juge) | `juges_croises_v53.py` | **codé**, **couru** ; au second tour réel, juges **à leur plafond** (11 fiches sur 12 « notables », κ de Cohen = 0 : aucune discrimination) [RA41] |
| **juges d'idée v2** (`lecteur_tables`) | comparaisons par paires à l'aveugle dans les deux ordres, force de Bradley-Terry avec terme de position, fiches de référence ancrées, budget de fiches notables, preuve citée vérifiée mécaniquement, juges d'une autre lignée | — | `juges_idees_v2.py` (brouillon 3 public, `faff48b`) ; brouillon 4 privé | **suspendu** : brouillon 4 non scellable (bloquant B10) ; course suspendue (GO-2026-11-04-08) le temps de refaire la règle de diagnosticité [RA42] |
| **juge-tournoi** (façon Co-Scientist) | juge génératif par tournoi de comparaisons, mis sous la même attaque que le juge statistique | Kimi dans la conception v2 ; **Opus sur les crédits Claude** décidé le 9 novembre | conception v2 `0ac81c9a…` | **décidé** (juge Opus, après A1-v4) ; conception v3 et devis à écrire ; **non codé** [RA43] |
| **bisociateur** | marie des idées en trois bras : méta « trou structurel partagé », « loin mais proche », substitut de Gu et Krenn « jamais liés » ; pas de bras hasard | code de l'orchestrateur et une session neuve | `bisociateur_v53.py`, `_v54.py`, `_v55.py` | **codé** ; écart à vérifier sur pièce : SciMuse rapporterait que les paires à la Gu-Krenn font moins bien que le hasard (« à vérifier sur PDF ») [RA44] |
| **metteur en fusion** (`metteur_fusion`, `fusion_ideation`) | écrit la fiche fusionnée d'une paire ; une fusion n'est complète qu'avec son passeport et tous ses verdicts | Kimi par protocole, autres | `course2_v53.py` à `course2_v56.py` | **codé** ; une fusion **courue** au second tour réel [RA45] |
| **moissonneur** | métadonnées et résumés seulement (arXiv, OpenAlex) ; toute correspondance est non opposable ; une lacune apparente est une **question** | code de l'orchestrateur, par le relais seulement | `moisson.py` (v47), `relais_moisson.py` | **codé** (option (A) de Lazar, 29 octobre) [RA46] |
| **lecteurs** | lecteurs d'étiquettes et de niches (course) ; `lecteur_test` (étage des tests) ; lecteur neuf témoin du calcul des tests de mort | sessions neuves | `simulation_v54.py`, `tests_de_mort_v5.py` | **codé** ; depuis v57, le chiffre imprimé par le script et le lecteur neuf ne sont plus que des **témoins** du verdict [RA47] |
| **expérimentateur** (`experimentateur`, `experimentateur_test`) | écrit et exécute le test de mort d'une fiche gelée dans le bac à sable | modèle d'une famille | `cycle.py`, `tests_de_mort*.py` | **codé**, **jamais couru en vrai bac** [RA48] |
| **vérificateur** | rejoue ce que l'expérimentateur déclare : fiche, engagement, mesures déposées, code déclaré et fichiers qu'il lit, rien d'autre | modèle d'**une autre famille** que l'expérimentateur | `cycle.py` ; contrôle de lignée, pièce 6 de v7 | **codé** [RA49] |
| **traducteur, contre-traducteur** (pont) | traduisent une fiche d'idée en fiche-loi ; le contre-traducteur, aveugle à la première traduction, d'une troisième famille | appels injectés | `pont_v1.py` ; rôles prévus dans une « couche v57 » de l'orchestrateur | **codé** dans le module seul ; **non intégré** [RA50] |
| **gardien** (tour fermé) | gardien **mécanique seul** pour les trois bras du tour fermé | code | `tour_ferme_v61.py` à `_v64.py`, `lecture_tour_ferme_v60.py` à `_v63.py` | **codé** (décision D9) [RA51] |
| **recombinaison**, **synthèse** | recombinaison bisociative des survivantes du pôle (diversité de domaine dans le noyau) ; synthèse | agents | `recombinaison.py` | **codé** [RA52] |
| **pôle « bras d'attaque »** | — | — | `bras_attaque_v54.py` existe au dépôt public | **non ouvert** (cloison) |
| **réserve tenue à l'écart** (tour fermé, étage 2) | — | — | `reserve_tenue_a_l_ecart_v60.py`, `_v61.py` existent | **non ouverts** (existence seulement) |

### 3.2 Le noyau, la dépense et les gardes

- **Noyau et orchestre** : `noyau_v54.py`, `noyau_v55.py`, `noyau_v56.py` (orchestration d'étapes sous plafond, appels comptés,
  aiguilleur, juges croisés) ; `configuration_v53.py` à `_v56.py` (paramètres injectés, aucun seuil codé) ; `prepilote_v54.py` à
  `_v56.py` ; `course2_v53.py` à `_v59.py` ; `suivi_roles_v54.py` (gardes d'arrêt par rôle) ; `gardes_e0_v54.py` à `_v56.py`
  (table des gardes rejouée au départ, chaque garde sur un cas sain et un artefact) [RA53].
- **Dépense** : `budget_v53.py` à `_v56.py` ; chaque étape a un rôle de dépense : « protégée », « sacrifiable », « réductible »,
  « protégée hors porte » ; aucun repli silencieux : un champ manquant, un modèle inattendu, un plafond atteint ou un signal arrête le
  rôle ou la course avec une raison écrite [RA54].
- **Adaptateurs et relais** : `adaptateurs.py` (modèles Claude permis : `claude-opus-5-5`, `claude-fable-5-1`), `adaptateurs_v2.py`,
  `adaptateurs_v56.py`, `adaptateur_kimi_v53.py`, `adaptateur_commande_v64.py` ; relais de clé tenu par le noyau (`relais.py`,
  `relais_reel.py`, `relais_reel_v2.py`) : la clé n'est jamais dans l'environnement de l'agent ; correctif v47 : le kit ne doit
  **jamais changer de modèle** (incident du 29 octobre : refus d'Opus 5.5 puis bascule non autorisée, R-764) [RA55].

### 3.3 Les versions, et pourquoi elles s'empilent

Règle R12 : une version nouvelle est un fichier nouveau ; `noyau_v56` hérite de `noyau_v55`, qui hérite de `v54` ; chaque version
ajoute la correction d'une contre-lecture indépendante (vingt, CL1 à CL20, chacune avec une table « constat → fichier:ligne →
essai → mutation ») ; l'arbre public est un extrait exact du dépôt de travail au commit `91a3c7f8` (1er novembre, v56), complété
ensuite fichier par fichier [RA56].

| version | contenu | état et source |
|---|---|---|
| v2 à v6 | juge v1 (ordre d'exécution secret, urne) ; nul des filles v2 ; mémoire prédictive (signature, classes, héritage de la preuve), marchepieds ; seuil de signature par fiche, graine du noyau secrète, vivier de 60 ; monde tenu par le noyau, dépôt unique par engagement, relais de clé réel, répétition générale | codé ; v6 : 154 essais, « prêt pour (a) » [RA57] |
| v7, versions 1 à 21 (27 octobre) | monde sur banque figée, nul informé, sans urne, règle e-BH par défaut, témoins jugés sans agents, signal « pas de dents » ; proposeur à liberté bornée ; nul étendu puis **ajusté** à l'archive ; pari à fraction ; proposeur enfichable ; grammaire de mondes ; adaptateur mixte ; clé du relais hors de l'environnement ; banque v3 ; traits internes ; cœur du **pari apparié borné** et règle de l'héritage | codé ; 241 essais à la v21 [RA57] |
| v31 (28 octobre) | **prise « idéation »** (`ideation.py`, 479 lignes) | contre-lecture R2 : « non lançable en l'état » (CL31-01 bloquant : panne du relais reproductible, course vide scellée en code 0) [RA18] |
| v32 à v45 | corrections de la v31 (N-058 : v32 avant la couche 2) ; arbre v45 de la course 1 | codé ; course 1, tentative 1 arrêtée le 29 octobre [RA58] |
| v46 à v52b | dossier fermé (v46) ; moissonneur et barrières du relais (v47) ; **étage des tests de mort** (v48 ; corrigé en v49, v50, v51) ; mode « juges seulement » (v52) ; borne mémoire de 768 Mo (v52b) | codé [RA59] |
| v53 à v56 | course 2 et pré-pilote : Kimi par protocole, aiguilleur avant les juges, notation croisée, tableau minimal, mémoire anti-redite, bisociateur à trois bras, règle de non-lecture, plafond par étape ; machine jetable par liste blanche (v56) | codé ; contre-lectures CL18 à CL20 ; **base de l'arbre public** [RA60] |
| v57, v57b (1er novembre) | verdict des tests de mort **calculé par l'orchestrateur** sur le fichier brut nommé par le préenregistrement scellé ; point de sélection entre générations | codé ; essayé hors ligne ; 19 et 15 mutations tuées [RA61] |
| v58 (1er novembre) | le nul d'archive ajusté devient le **seul nul** du juge (nul v8) | codé ; validation décisive confirmée [RA62] |
| v59 (2 novembre) | **boucle fermée** : la génération g+1 lit la sélection scellée de la génération g ; les proposeurs ne reçoivent plus le classement des juges | codé ; jamais couru [RA63] |
| v60 à v64 (2-3 novembre) | **tour fermé** : réserve tenue à l'écart et oracle (v60), cœur et lecture gelée (v61-v63), adaptateur de commande (v64) | codé ; jamais couru (section 4.5) [RA64] |
| v65 (10 novembre) | **boucle réelle** : héritage de départ, jeu planté, jugement avec l'archive, bras réel seul, lecture gelée propre | codé sur la branche `prep/organisme-v65-v1` ; **non contre-lu** [RA65] |
| hors de la chaîne | nul v9 (`nul_v9.py`, 2 novembre) ; attaques de Goodhart v1 à v5 ; juges d'idée v2 ; juge à plan plein ; porte PACE (bras de référence du juge, jamais une sélection d'agent, exploratoire) | codé [RA66] |

---

## 4. Les mécanismes du pôle de test

### 4.1 Le juge statistique

- **Principe** : une fiche engage une **loi prédictive** sur K issues ; sa richesse est calculée contre une **bibliothèque de
  prédicteurs aveugles** (nul composite) sur des **tirages frais semés par l'empreinte de l'engagement** ; la promotion suit une
  règle d'e-valeurs écrite dans le code de l'orchestrateur, hors de tout agent : richesse ≥ 20 = 1/α, α = 0,05 (inégalité de Ville)
  [RA67].
- **Énoncé revendiqué** (O2, resserré par N-064 le 9 novembre) : « juge statistique dont la statistique est calculée par
  l'orchestrateur, hors de tout agent, à partir d'un engagement scellé avant que les données existent, contre un nul formé des lois
  connues (l'archive), avec contrôle des comparaisons multiples » ; les e-valeurs et le seuil 1/α hors des agents ne sont **plus
  revendiqués** (occupés en partie par POPPER) [RA68].
- **Versions du nul** :

| nul | ce qu'il ajoute | état |
|---|---|---|
| v1 | ordre d'exécution secret, membre « urne » | socle de l'expérience 1 [RA57] |
| nul des filles v2 | membres ajustés par maximum de vraisemblance sur les tirages frais, lus à des instants fixés d'avance | adopté à l'expérience 2 [RA57] |
| nul informé | membre « prédicteur connu », ajusté avant le gel sur une partie de calibrage disjointe | codé v7 [RA69] |
| nul étendu, puis ajusté à l'archive | ferme les quatre trous de nouveauté du banc des tricheurs (0 sur 200 contre 148 à 179) | codé v7 (versions 4 et 6) [RA57] |
| **v8** (v58, 1er novembre) | le nul d'archive ajusté, **seul nul** | **production** ; validation décisive « confirmée » [RA62] |
| **v9** (2 novembre) | plus les **recombinaisons par morceaux** (un niveau) des lois connues, avec certificat ; borne de Ville tenue à α quel que soit le nombre de membres | **candidat** ; validation scellée : « **puissance perdue** » ; production inchangée tant que Lazar n'a pas accepté le prix [RA70] |

- **Multiplicité** : règle e-BH (forme en e-valeurs de la procédure de Benjamini et Hochberg) par défaut, décidée le 27 octobre ;
  erratum (e-valeur plafonnée au seuil par fiche, corrigé) ; témoins vrais hors de la famille e-BH ; m fixé avant les issues (v11)
  [RA71].
- **Second type d'engagement : le pari apparié borné**, pour les affirmations globales (H1, H2, H3, G1) : unité = la tâche, jamais
  l'épisode ; contraste borné calculé par le noyau après le gel ; nul fixe ; forme « parts » seule ; garde appariée ;
  intersection-union ; héritage entre parties d'épreuve disjointes seulement ; décisions D-S1 à D-S12 prises (N-055) ; cœur **codé**
  (`pari_apparie.py`, `engagement_apparie.py`, `monde_banque_scores.py`), **pas encore lié au cycle** [RA72].
- **Puissance sur la banque réelle** (exploratoire) : force 0,8 promue 95 % du temps à 120-180 épisodes d'épreuve ; force 0,5, 65 à
  73 % ; force ≤ 0,3, au plus 24 % ; faux témoins : aucune cellule au-dessus de 5 % [RA73].
- **Antériorité** : citations obligatoires (POPPER ; Dwork et al. ; Blum et Hardt ; Co-Scientist, N-064) ; **collision constatée le
  10 novembre** avec Qu, Chen et Wang (arXiv 2609.27051) : deux composantes de O2 occupées en entier, une dans son principe, une
  absente (le nul formé des lois connues) ; **nœud** : resserrer et citer, ou garder et citer [RA74].

### 4.2 Mondes plantés, témoins et oracles

- **Témoins plantés** vrais et faux, mêlés anonymement à chaque génération, indexés pour l'audit, exclus de tout ce qui est servi aux
  agents ; **témoins jugés sans agents** (le noyau seul, gratuitement, en grand nombre) ; **signal « pas de dents »** quand les
  témoins vrais d'une génération sont éliminés [RA75].
- **Mondes** : mondes tirés dans une grammaire (v7, versions 7 et 8) ; mondes de l'attaque W1, W2 et W2 gradué (section 5) ; monde
  S-V1 de la boucle réelle : loi connue K1 déclarée, 4 lois vraies et 4 fausses plantées, fausses = recombinaisons de K1 seule,
  membres du nul v8 [RA76].
- **Oracle du monde planté** : `oracle_tour_ferme_v60.py` (oracle et classement des cartes) ; décision D2 du tour fermé : fausse
  découverte lue par l'oracle [RA51].
- **N-058 (28 octobre), décidé** : la composition des proposeurs (quels modèles, quel rôle, quelle part du budget) se juge sur
  **l'oracle du monde planté et le coût mesuré, seuls**, jamais sur le verdict du juge (invariant de N-053) ; le verdict sur les
  fiches reste aveugle à l'identité du proposeur ; l'interdit porte sur la sélection d'agents, pas sur celle des fiches [RA77].
- **N-059 (28 octobre), décidé** (nœuds de la conception de l'affinage v2, session de Fable) : générations d'étalonnage à calendrier
  secret et témoins silencieux ; budget d'erreur par génération, contrôle des fausses découvertes en fin de course (statisticien sur
  devis) ; forme de loi « composition » retirée ; troisième famille pour le détecteur d'injection ; **duel des proposeurs en
  générations d'étalonnage**, une mesure, une porte ; banque de familles inédites de confirmation distincte de la famille tenue à
  l'écart ; forme « invariance » admise avec plafond ; épreuve lue jusqu'au budget, seuil de réfutation fixé par la course ; taux par
  proposeur lus par le directeur seul [RA78]. **État de codage de ces points : non vérifié ici** (la conception de l'affinage n'a pas
  été lue ; sans source).
- **N-060 v3 (29 octobre)** — homonyme à ne pas confondre : c'est l'**oracle de la vérité du dommage** du programme de contrôle
  (couverture des contrôles de l'article contre la référence cachée, extrait cité vérifié par programme, deux lecteurs hors des
  familles des moniteurs, comparé au jumeau honnête, épreuves avant lecture, repli écrit) ; il concerne la banque de G1, donc la
  couche d'essai 2 du pôle si elle se construit ; les trois oracles exécutables de la v2 restent pour une banque à tâches
  exécutables [RA79].

### 4.3 Le pont fiche → loi

- **Ce qu'il fait** : vérifie l'affectation des modèles (traducteur d'une autre famille que l'auteur, contre-traducteur d'une
  troisième) ; traduit sans aucune issue, score ni verdict ; compile mécaniquement la loi (prédicteur connu du moniteur + effet déclaré
  par la fiche, ou contraste apparié) ; compare deux traductions aveugles ; applique les gardes (rétrodiction, loi vide, puissance) ;
  rend une sortie sur trois : `loi_banque_existante`, `loi_couche_3`, `non_testable` (renvoi motivé N1 à N11) [RA23].
- **Code** : `pont-fiche-loi-v1/pont_v1.py` (`9fb2d936…`), 82 essais (77 seuls et 5 de compatibilité avec la v56), banc de
  25 mutations, toutes tuées ; note de conception (`5161e199…`) retenue hors du dépôt public [RA50].
- **Épreuve fraîche** (GO-2026-11-01-09, plafond 5 USD, 1,11 USD dépensés ; lecture préenregistrée scellée `400506d9…`) : L1 « dents »
  (6 témoins justes sur 6) ; L2 « non lisible » (0 fiche traduite sur 15) ; **L3 « inutile en l'état »** (0 fiche utile sur 8) ;
  L4 « sûr » [RA80].
- **Nœud D-P1 « qui écrit la loi »**, ouvert le 1er novembre, **sans défaut** : (b) le proposeur écrit lui-même un champ « loi »
  natif, ou (c) loi native et traduction comparées (recommandation (c) sur un petit lot, confiance 0,55 ; dépense supposée 2 à
  5 USD) ; le défaut d'origine (a), traducteur séparé, est réfuté en l'état ; D-P2 à D-P5 attendent aussi [RA81].
- **Ce qui reste** : couche v57 de l'orchestrateur pour le pont (non écrite), six témoins du pont par un metteur en forme tiers,
  épreuve fraîche décisive sur une banque sœur, antériorités sur PDF [RA50].

### 4.4 Tests de mort, bac à sable, machine jetable

- **Principe** : la fiche gelée devient un script, exécuté dans un bac à sable `bwrap` (sans réseau, un seul dossier, mémoire bornée,
  filtre d'appels système, aucune clé, fichier témoin vérifié sur l'hôte) sur des données déjà présentes ; la prédiction est scellée
  avant l'exécution ; verdict « survit » ou « éliminée » à un seuil gelé ; un vérificateur d'une autre famille [RA48].
- **Verdict par le noyau** (décision R-1057 de la branche conv-audit, 1er novembre ; v57, v57b) : le verdict vient **seulement** du
  calcul de l'orchestrateur sur le fichier brut que nomme le préenregistrement scellé (fichier, colonne, statistique, seuil) ; tout
  incident rend la fiche « non concluante » ; ce que le script imprime n'est plus qu'un témoin [RA61].
- **Barrières** : garde des outils (`garde_outils.py`, première barrière, par motifs) ; bac à sable (vraie barrière) ; **dossier
  fermé** (la course ne lit que les fichiers d'un manifeste scellé, sans lien symbolique) ; **machine jetable** dont les variables
  d'environnement viennent d'une **liste blanche fermée** (v56) [RA82].
- **Durée** : au plus 6 minutes de bac par fiche, ≈ 1 h 40 par sous-session de 16 fiches [RA32].
- **Machine** : devis de plomberie de la machine jetable v1 à v3 (Hetzner) ; pour la boucle réelle, une Hetzner CPX32, 5 USD
  (GO-2026-11-10-10) [RA83].
- **Vérification non circulaire du bac à sable** : question v1 (`26f2db15…`) servie au collisionneur v8 (16,24 USD) — **payée,
  scellée, non lue** (annexe A) [RA31].
- **État** : implémenté, essayé hors ligne avec un exécuteur simulé ; **le vrai bac n'a jamais tourné** (`bwrap` absent des machines
  de développement ; les essais du vrai bac sont déclarés non joués) [RA19, RA65].

### 4.5 Le tour fermé (tâches A2 à A4) — préparé, jamais couru

- **Objet** : jouer la boucle fermée v59 avec de vrais modèles sur un monde à loi plantée, trois générations, trois bras (réel :
  Kimi et Argon ; aléatoire ; recopie-mélange), témoins plantés, tests de mort dans le vrai bac à sable, vérificateur d'une autre
  famille ; étage 2 avec une réserve tenue à l'écart (texte à part, scellé avant toute lecture de la réserve) [RA84].
- **Décisions** : GO-2026-11-02-06 (v59 : les proposeurs ne reçoivent que les lois retenues, sans verdict, richesse ni compte) ;
  GO-2026-11-02-18 (étage 1 seul au scellement ; D2, D3, D4, D7, D9 et seconde partie de D6 acceptées : fausse découverte par
  l'oracle, g₀ = 0,02 nat, nouveauté contre l'archive ; témoins jamais retenus ni servis ; bras recopie-mélange nourri par l'archive
  du bras réel ; bras aléatoire jugé contre l'archive du bras réel de la même génération ; gardien mécanique seul ; D5, D8 et première
  partie de D6 reportées à l'étage 2) ; GO-2026-11-02-19 (15 USD), puis **GO-2026-11-02-23 (50 USD, jusqu'au 16 novembre)** [RA84].
- **Préparation** : code v60 à v64 ; préenregistrement en six brouillons, chacun contre-lu ; commandes v6 contre-lues « scellables
  telles quelles » ; configuration v4 versée [RA85].
- **Jamais couru** : aucune ligne de dépense sous GO-2026-11-02-19 ni -23 [RA86]. L'essai à blanc du 7 novembre a trouvé deux défauts
  de la v64 : les lois fausses du tour fermé étaient **hors de la classe couverte** par le nul (une fausse promue) ; la v64 **jugeait
  les lois plantées sans l'archive** (fausses couvertes promues 994 fois sur 1 000 en simulation) → code v65 [RA87]. La course réelle
  minimale réutilise le cœur du tour fermé v64 avec un seul bras (section 4.6). Aucune décision écrite n'annule le tour fermé ; sa
  ligne de GO expire le 16 novembre.

### 4.6 La boucle réelle v65 — la plus petite course réelle de la boucle complète

- **Décisions** : GO-2026-11-07-11 (préparer maintenant, option (a) : une génération, deux fournisseurs, une douzaine de fiches,
  quatre lois vraies et quatre fausses plantées, fausses limitées à la classe couverte par le nul, tests de mort dans le vrai bac à
  sable, sélection relue par la génération suivante, préenregistrement contre-lu et scellé, essai à blanc hors ligne, dépense sur
  devis) ; **GO-2026-11-08-02** (D1 bras réel seul, D2 génération 2 complète, D3 plafond 40 USD de modèles — Kimi 33, Argon 7 — et
  5 USD de machine ; **45 USD, jusqu'au 30 novembre** ; « GO de 40 + 5 dollars. : go complrtt ») [RA88].
- **Dessin** (brouillon 1, 7 novembre) : monde S-V1, loi connue K1 déclarée, 4 vraies et 4 fausses plantées, jugées avec l'archive ;
  Kimi et Argon proposent ; gardien mécanique, **aucun juge à modèle, aucun rôle pour Claude** ; tests de mort dans `bwrap` ;
  génération 2 lit la sélection ; puissance recalculée 1 000 sur 1 000 (la course éprouve la plomberie, pas la puissance sur données
  réelles) ; devis : ≈ 31 appels, 1,5 à 2 USD attendus, pire cas 28,10 USD (35,30 si la chaîne casse) [RA87].
- **Code v65** (rendu le 10 novembre ; dix fichiers neufs, rien de modifié) : héritage de départ scellé (archive {K1}) ; jeu planté lu
  à l'octet, chaque fausse dans la classe couverte du nul v8 ; jugement avec l'archive de la génération ; bras réel seul et
  génération 2 obligatoire ; lecture gelée propre (critères C1 à C6) ; commandes v6 nommées avec leurs empreintes ; gardes de dépense
  avant chaque appel ; bac à sable inchangé (`bwrap` absent : refus, aucun repli). Le développeur déclare 232 essais passés, 3 sautés
  (vrai bac), 38 mutations tuées sur 38, un essai à blanc en 9 étapes ; ses réserves : vrai bac jamais joué ; relevés d'empreintes non
  reproductibles à l'octet à graine égale (décisions égales) ; proposeurs simulés qui recopient la loi plantée, donc une issue à blanc
  « trop belle » par construction [RA65].
- **Préalables** (GO-2026-11-08-02, mots de Lazar R-2195) : (1) **contre-lecture du code v65** — lancée le 10 novembre (Fable ;
  consigne `67b086ce…` ; arbre `/home/user/organisme-v65-cl` au commit `cef5ea60`) ; (2) **machine avec bac à sable** validée par
  l'essai à blanc `--bac reel` ; (3) **préenregistrement scellé** (brouillon 1 du 7 novembre au dossier ; à mettre au dessin v65)
  [RA89].
- **Enveloppe** : GO-2026-11-10-10 (inscrit à 12:05 UTC le 10 novembre, R-2206) : 120 USD au plus jusqu'au 30 novembre, dont **45 pour
  la boucle réelle** (40 de modèles, 5 de machine jetable Hetzner CPX32), conditions de GO-2026-11-08-02 « inchangées et toutes
  exigées », plus la **configuration v5 `995eb918…`** ; et 75 pour un témoin de l'attaque publiée de Bailey (course à part) [RA7].
  La ligne ne dit pas si elle se cumule avec GO-2026-11-08-02 ; lecture prudente : une seule course de 45 USD (sans source pour un
  cumul).
- **Point neuf à trancher** : le code v65 rendu porte la configuration `exemples/configuration-boucle-reelle-v5.json` d'empreinte
  **`bff138d8a30c57b8…`**, alors que GO-2026-11-10-10 et la note de la session-dépôt qui la fonde exigent **`995eb918…`** ; aucune pièce
  de `main` ne dit à quoi correspond `995eb918…` (recherche par `git grep`). Tant que l'écart n'est pas levé (ligne corrigée par toi,
  ou configuration alignée et contre-lue), la course ne peut pas remplir la condition écrite [RA6, RA7].
- **Suite écrite par la mère** : contre-lecture du code, puis décision sur le dossier du texte scellé (dépôt public ou v66), puis
  machine à `bwrap` (avec la session-dépôt), puis préenregistrement, puis course [RA89].
