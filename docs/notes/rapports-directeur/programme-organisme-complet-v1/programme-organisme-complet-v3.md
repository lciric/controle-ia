# Programme complet de l'organisme d'idéation — architecture, mécanismes, état, et inventaire des idées (v3)

- **Pour** : Lazar. **Écrit par** : un sous-agent neuf (rédacteur, Claude Opus 5.5) de la session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv`, le 10 novembre 2026 (v1 à partir de 11:59 UTC ; v2 à 12:45 UTC ; v3 sur la demande de la
  mère, registre relevé jusqu'à **R-2228**, à 13:27 UTC ; heures relevées par `date -u`). **Statut** : la v2 a reçu une
  vérification orchestrée (six vérificateurs et six sceptiques, rapport scellé : « transmissible après corrections », R-2228) ;
  la v3 en applique les 42 couples, sans nouvelle contre-lecture.
- **Demande de Lazar** (verbatim, R-2200) : « ecir smoi le programme complet exhaustif avce toutes les couchhes et mecanismes
  prevus pour l'org » ; « precise bine dans le programme toutes nos idees hypotheses resultats proposiitons pour que rien de notre
  brinstorm ne soit perdu ».
- **Deux parties.** **Partie I** : l'architecture — couches, mécanismes, rôles, état exact de chaque pièce, dépenses, nœuds et
  prochains pas. **Partie II** : l'**inventaire exhaustif des idées** (411 entrées en douze familles : idées, hypothèses, résultats,
  propositions, objections, pistes écartées, questions ouvertes), écrit par un rédacteur voisin (`inventaire-idees-organisme-v7.md`,
  `056adb7f…`) et repris ici entrée par entrée, avec une colonne de renvoi vers la partie I. Les deux parties ensemble répondent aux
  deux demandes de Lazar.
- **Sources.** Chaque chiffre et chaque affirmation porte un renvoi **[RAn]** au registre des affirmations
  (`registre-affirmations-programme-v3.md`), qui donne le chemin, la ligne et l'empreinte. Ce qui n'a pas de source est écrit
  « sans source ». Les passages corrigés par la vérification orchestrée de la v2 tiennent leur source de son rapport
  (`prereg/contre-lectures/programme-organisme-complet-v2-verification-v1.md`, `231118c9…`), constat par constat [RA148].
- **Version v3** : la v2 (`programme-organisme-complet-v2.md`, `dffe0b63…`, gardée intacte, R12) corrigée par les 42 couples de la
  vérification orchestrée — 30 appliqués dans le texte, 12 portés en erratum dans le préambule de la partie II pour que la copie de
  l'inventaire reste à l'octet — et relevée jusqu'à R-2228 (pas (a) du pilier mathématique fait, R-2226 ; dessin et devis de
  l'essai Lean rendus et en contre-lecture, R-2227) ; liste des couples et des retouches à la main au journal v3
  (`journal-programme-v3.md`). La v2 tenait déjà la mise à jour jusqu'à R-2221 et la partie II ; la v1, les corrections de ses
  jalons.
- **Ce que ce texte n'ouvre pas** (cloison R-2152, R-2170, et interdits de la consigne) : rien du bras d'attaque au-delà des
  décisions inscrites ; rien du mode tenu à l'écart au-delà de son existence ; aucune sortie de collisionneur ni réponse de modèle
  non synthétisée (elles sont listées en annexe A) ; aucune recette d'attaque contre un juge ou un moniteur (niveau méthode, R-607).

## Verdict

1. **L'organisme d'idéation est un instrument codé, éprouvé hors ligne, dont le juge a été attaqué, la réparation (nul v9) restant candidate et non en production ; sa boucle complète
   n'a jamais tourné avec de vrais agents.** Orchestrateur publié jusqu'à la version 64 ; version 65 sur une branche, contre-lue le
   10 novembre (« utilisable pour la course après corrections », deux bloquants) ; version 66 décidée et en écriture ; nul de
   production v8, nul v9 candidat au prix « puissance perdue » [RA1, RA2, RA3, RA134].
2. **Les propriétés de l'objectif ultime sont des cibles décidées, pas des pièces codées** : l'organisme ne se conçoit pas seul,
   rien n'est figé après conception, son universalité n'est pas mesurée sur des familles inédites (R-2152) ; les couches 3
   (réécriture de soi) et 4 (pôle théorie et Lean) sont fermées jusqu'aux résultats de l'étape 2, sauf un essai sur processeur,
   dessiné et devisé le 10 novembre, en contre-lecture [RA4, RA5, RA145].
3. **Le prochain pas qui engage est la plus petite course réelle de la boucle complète** (45 dollars, jusqu'au 30 novembre), après
   le code v66 (corrections de la contre-lecture de la v65) et sa contre-lecture, une machine à bac à sable et un préenregistrement
   scellé ; **un point est à trancher avant** : la condition « configuration v5 `995eb918…` » de GO-2026-11-10-10 ne correspond pas
   au code v65 (`bff138d8…`), et la v66 changera encore la configuration [RA6, RA7, RA134, RA136].

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

# Partie I — Architecture : couches, mécanismes, état

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
architecture méta » ; (25 octobre, 00:05 ; mots rapportés par relais, le premier segment étant la proposition à laquelle il répond, entre crochets dans N-044) l'universalité « se gagne sur des familles inédites, pas sur des items inédits des mêmes
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

### 2.1 Trois numérotations, dont deux se contredisent

**Contradiction à trancher ou à documenter (nœud de documentation, sans dépense).** Le programme de conception de l'organisme
v1, du 27 octobre, numérote les couches d'essai de 0 à 4 ; la réponse de la session-dépôt du 31 octobre (R-920) et le nœud N12
(1er novembre) appellent « couche 3 » et « couche 4 » d'autres choses. Aucune pièce ne réconcilie les deux ; l'inventaire voisin
relève la même contradiction (ARC-045, partie II) [RA140, RA21, RA143].

| couche | programme de conception v1 (27 octobre, § 4), repris en v6 et v7 | R-920 (31 octobre) et N12 (1er novembre) |
|---|---|---|
| 3 | épisodes ou moniteurs neufs à la demande (option (c)) ; porte : coût mesuré sur une fiche pilote | réécriture de soi sous bac à sable : génération de pièces neuves (moniteur, sous-agent à consigne auto-rédigée, règle d'agrégation écrite en code) |
| 4 | bras d'attaque en quarantaine **et** pôle théorie ; porte : failles connues retrouvées avant toute inédite | pôle théorie et Lean (vérification de preuves), sans bras d'attaque |
| 1 et 2 | banque réelle figée ; banque avec sabotage | **non définies** dans les pièces lisibles |


| numérotation | où | contenu |
|---|---|---|
| (i) **couches d'essai sur le monde réel** (« une question, une porte par couche ») | programme de conception de l'organisme, v1 du 27 octobre (§ 4, l. 65-79), repris en v6 § 4 (l. 167-183), inchangé en v7 | 0 monde caché ; 1 banque réelle figée ; 1 bis banque complète ; 2 banque avec sabotage ; 3 épisodes ou moniteurs neufs à la demande ; 4 bras d'attaque en quarantaine et pôle théorie |
| (ii) **ordre de conception** | même programme, v6 § 3 (l. 111-166), v7 § 3 | 1 proposeur à liberté bornée et monde du programme (v7) ; 2 réécriture des rôles sous bac à sable (v8) ; 3 bras d'attaque, remplacé le 28 octobre par neuf voies de mesure adversariale ; 4 pôle théorie, Lean comme vérificateur |
| (iii) **couches 3 et 4 de l'organisme** au sens du nœud N12 | R-920 ; synthèse N12-N13 | couche 3 = réécriture de soi sous bac à sable (génération de pièces neuves : moniteur, sous-agent à consigne auto-rédigée, règle d'agrégation écrite en code) ; couche 4 = pôle théorie et Lean |

**Lecture de travail de ce texte, qui n'est pas une décision** [RA21, RA22, RA23] : la couche 3 de N12 réunit la couche d'essai 3 (moniteurs ou épisodes neufs à la
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
| **4** | pôle théorie : juge = vérificateur de preuves (Lean) ; proposeur nourri par le moissonneur et la recombinaison | **prévu** (« go » du 27 octobre) ; **fermé** sauf l'essai sur processeur « preuve formelle contre suite bon marché » (N12 (b)) ; pas (a) de R-2199 **fait** (synthèse du tour 2 scellée, R-2226 [RA144]) ; pas (b) : dessin et devis de l'essai Lean **rendus**, en contre-lecture, GO non demandé (R-2227 [RA145]) ; puis (c) note du pilier « génération » | « failles connues retrouvées avant toute inédite » (porte écrite pour le bras, alors dans la même couche) | [RA21, RA5, RA28] |

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
- **Tour 2 N12-N13** (collisionneur v8, cinq espèces) : **payé, scellé, lu le 10 novembre** (15/15 cellules, 15,60 USD) : pas (a)
  de R-2199, sous les critères scellés (`criteres-lecture-n12-n13-tour2-v1.md`, `6bdbfe47…`, commit `9ca47466`) ; synthèse
  scellée par un lecteur neuf (Opus 5.5, déclaré de la même famille que les espèces A et B) : `synthese-n12-n13-tour2-v1.md`
  (`6ef6bc2e…`) ; N12 tenue sous condition par les cinq espèces ; 7 divergences résolues sur 9 (n° 1 et 7 renvoyées à Lazar par
  les espèces) ; réserve R4 (tour trop propre) [RA28, RA31, RA134, RA144].
- **Dans le code** : seule trace, la sortie `loi_couche_3` du pont (une loi qui exige des épisodes neufs, avec « une demande
  d'épisodes au niveau méthode ») ; pont non intégré à l'orchestrateur [RA23].

### 2.5 Couche 4 — pôle théorie et Lean (fermée, sauf un essai) ; l'écart vérification / génération

- **Définition** (ordre de conception, point 4) : juge = vérificateur de preuves (Lean) ; proposeur nourri par le moissonneur et la
  recombinaison ; questions ouvertes du programme (agrégateur sous corrélation adverse, théorème négatif) ; aucune dépense de carte ;
  installation de Lean sans dépense. « Go » de Lazar le 27 octobre (14:32) ; « ne pas promettre de révolution, mesurer ce qui sort »
  [RA22].
- **État** : n'existe pas (R-920, 31 octobre) ; **fermée** par N12 (b), qui n'autorise qu'un **essai sur processeur « preuve
  formelle contre suite bon marché »** (devis d'appels de sous-agents) [RA5].
- **Collisionneur N12-N13** : accord large à quatre sur « **l'empreinte ne prouve pas la validité** d'une preuve » ; convergence
  née de la critique : Lean doit battre une **suite bon marché** (lecteur neuf outillé symbolique et numérique, tests, mutations,
  relecture par une autre famille) — accord jugé trop propre (réserve R4) ; formes d'ouverture discutées : sur une classe d'erreurs
  mesurée, lemmes critiques seulement, ou vérificateur externe d'abord (divergence non résolue n° 5) [RA30].
- **Écart vérification / génération** : la recherche du 10 novembre conclut qu'**aucune partie de l'organisme ne produit de
  mathématiques nouvelles** ; la couche 4 prévue **vérifie** des preuves, elle n'en **génère** pas ; le code ne connaît que le renvoi
  **N3** du pont : « relève d'une preuve ou d'une simulation hors banque (pôle théorie), pas d'épisodes » (`pont_v1.py`, l. 45)
  [RA33].
- **Décision de Lazar du 10 novembre (R-2199)** sur le pilier « mathématiques nouvelles », dans cet ordre :
  (a) lecture du tour 2 N12-N13 (critères scellés avant ouverture, synthèse par un lecteur neuf, sans dépense) — **fait** :
  synthèse scellée (`6ef6bc2e…`, R-2226) [RA134, RA144] ;
  (b) **devis** de l'essai sur processeur « preuve formelle contre suite bon marché », puis GO — **dessin et devis rendus**
  (brouillon 1, `9ccc9ac0…`), contre-lecture 1 en cours (Fable), GO non demandé (R-2227) [RA145] ;
  (c) **note de conception du pilier « génération »** (conjectures, démonstrations, Lean comme arbitre, juge de nouveauté) — **nœud
  chez Lazar** [RA28].
- **Ce que le tour 2 apporte à la couche 4** (R-2226) : convergence vers un **vérificateur externe, hors de l'organisme**, ouvert
  seulement sur une classe d'erreurs mesurée sur une banque de confirmation ; points tenus pour l'essai (banque plantée par un
  tiers, découverte et confirmation séparées, contrôles de fidélité de la formalisation, puissance sur paires discordantes, coût
  apparié) ; désaccords (qui formalise, ce qu'on mesure, une ou plusieurs classes, suite d'un échec) ; **aucune espèce ne parle de
  génération de mathématiques nouvelles** : le pas (c) part sans matériau des espèces ; trois points à la limite d'une décision
  prise, pour toi : ouvrir la couche 4 sur le seul essai ; la suite bon marché comme standard obligatoire ; le bornage « classe
  d'erreurs » attribué au directeur [RA144].
- **L'essai Lean, dessiné et devisé** (R-2227 ; brouillon 1, non contre-lu ; prédiction du rédacteur : ≈ 0,25 pour un gain établi) :
  preuves courtes à étapes ; cinq classes d'erreurs (K1 à K5) ; banque plantée par une troisième famille ; découverte et
  confirmation séparées ; bras L (Lean 4 et Mathlib) contre bras S (calcul symbolique et numérique), même modèle et même plafond
  par item ; issues O0 à O4 écrites d'avance. Devis : phase 1 (outillage et pilote, 140 items) ≈ 312 USD attendus, plafond proposé
  450 USD et ≤ 50 USD de machine ; phase 2 (confirmation) ≈ 799 à 1 247 USD, plafond 1 400 USD sur un second GO ; engagement
  maximal 1 900 USD ; 2 à 3 semaines, hors du chemin de G0. Obstacles : ni Lean ni Mathlib installés ici, 2,7 Go de disque.
  Décisions D-1 à D-6 posées (GO de phase 1 ; machine et réseau pour Lean ; qui formalise ; seuils ; classes ; banque d'usage)
  [RA145].
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
| **proposeur** (pôle de test) | formule les fiches-lois d'une génération à liberté bornée : gabarit, catalogue de stratégies, contexte sans aucune issue ; enfichable (proposeurs de référence sans modèle) | Opus 5.5 prévu ; références scriptées | `proposeur.py` (0.7.0, pièce 4 de v7) ; `proposeurs_references.py` (v7, version 7) ; `proposeurs_references_v59.py` | **codé** ; références mesurées sur 20 mondes : mécanique 23/35, scripté avec exploration 5/35 (scripté aveugle 2/35), hasard 1/35 [RA37] |
| **proposeur d'idée** (`proposeur_ideation`) | écrit les fiches d'idée à champs fermés | Claude (Opus 5.5, Fable 5.1), Kimi par protocole, Argon par commande externe | `ideation.py` (v31, puis v42) ; `ideation_v2.py` (v51) ; `ideation_v59.py` ; `adaptateur_kimi_v53.py` | **codé** ; **couru** : course 1 (29 fiches, 27 éligibles, 17 idées distinctes) ; second tour réel du 1er novembre (Kimi et Argon, 12 fiches classées) [RA38] |
| **aiguilleur** (« douane ») | classe chaque fiche par sa **forme** (niveau méthode, à corriger, trop concrète), délivre un passeport ; étape **protégée**, jamais sacrifiée au budget | session neuve, consigne figée, une fiche anonyme par appel | `aiguilleur_v53.py` (R-575, M4) | **codé** v53 ; **couru** ; consigne de l'aiguilleur v1 reçue (`c2efa120…`) ; la mesure M4 n'est pas calculée par v53 à v56 (« v57 à écrire ») [RA39] |
| **mémoire anti-redite**, **coffre**, **caviardage** | indexe l'archive et refuse les redites (intra-lot, entre fournisseurs, contre les générations passées) ; le coffre garde verdicts et clés scellés jusqu'à la fin déclarée ; le caviardage retire les formes de clé connues avant toute écriture | code de l'orchestrateur | `memoire.py`, `memoire_v53.py` ; `coffre_v53.py`, `coffre_v55.py` ; `caviardage.py` | **codé** [RA40] |
| **juges croisés** (`juge_ideation`) | chaque fiche munie d'un passeport est notée par **chacun** des juges, un appel par fiche et par juge, session neuve, identifiant opaque | Kimi, Argon, Opus 5.5 (troisième juge) | `juges_croises_v53.py` | **codé**, **couru** ; au second tour réel, juges **à leur plafond** (11 fiches sur 12 « notables », κ de Cohen = 0 : aucune discrimination) [RA41] |
| **juges d'idée v2** (`lecteur_tables` y est le juge scripté témoin du contrôle de diagnosticité) | comparaisons par paires à l'aveugle dans les deux ordres, force de Bradley-Terry avec terme de position, fiches de référence ancrées, budget de fiches notables, preuve citée vérifiée mécaniquement, juges d'une autre lignée | — | `juges_idees_v2.py` (brouillon 3 public, `faff48b`) ; brouillon 4 privé | **suspendu** : brouillon 4 non scellable (bloquant B10) ; course suspendue (GO-2026-11-04-08) le temps de refaire la règle de diagnosticité [RA42] |
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
- **Dépense** : `budget_v53.py`, `_v54.py`, `_v56.py` ; chaque étape a un rôle de dépense : « protégée », « sacrifiable », « réductible »,
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
| v60 à v64 (2-3 novembre) | **tour fermé** : réserve tenue à l'écart et oracle (v60), lecture gelée (v60-v63), cœur (v61-v64), adaptateur de commande (v64) | codé ; jamais couru (section 4.5) [RA64] |
| v65 (10 novembre) | **boucle réelle** : héritage de départ, jeu planté, jugement avec l'archive, bras réel seul, lecture gelée propre | codé sur la branche `prep/organisme-v65-v1` ; **contre-lu** le 10 novembre : « utilisable pour la course après corrections », bloquants CLV65-01 (C1 rendu sans fausse jugée) et CLV65-02 (un arrêt peut masquer une brèche) [RA65, RA134] |
| v66 (décidée le 10 novembre) | corrections de la contre-lecture de la v65, sous noms neufs ; lecteur du registre des GO selon la règle de la garde de calcul (lignes d'extension admises) | **en écriture** (développeur neuf, consigne `264e8a08…`) [RA134] |
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
- **Épreuve fraîche** (GO-2026-11-01-09, plafond 5 USD, 1,34 USD dépensés ; lecture préenregistrée scellée `400506d9…`) : L1 « dents »
  (6 témoins justes sur 6) ; L2 « non lisible » (0 fiche traduite sur 15) ; **L3 « inutile en l'état »** (0 fiche utile sur 8) ;
  L4 « sûr » (0 arrêt, 0 canari) ; L5 « conforme » (2 renvois « pont » pour une borne de 2) [RA80, RA131].
- **Nœud D-P1 « qui écrit la loi »**, ouvert le 1er novembre, **sans défaut** : (b) le proposeur écrit lui-même un champ « loi »
  natif, ou (c) loi native et traduction comparées (recommandation (c) sur un petit lot, confiance 0,55 ; dépense supposée 2 à
  5 USD) ; le défaut d'origine (a), traducteur séparé, est réfuté en l'état ; le premier essai que visait D-P5 (devis et GO) a reçu GO-2026-11-01-09 et a couru ; D-P2 à D-P4, « défaut sous 48 heures » selon le LISEZMOI du pont, n'ont aucune ligne au registre [RA81].
- **Ce qui reste** : couche v57 de l'orchestrateur pour le pont (non écrite), (les six témoins du pont, « à écrire » selon le LISEZMOI, ont depuis servi à l'épreuve fraîche : L1, 6 justes sur 6),
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
- **État** : implémenté, essayé hors ligne avec un exécuteur simulé ; **l'étage des tests de mort et la boucle n'ont jamais tourné en réel** ; seules les gardes du bac ont été éprouvées sous un vrai `bwrap` 0.9.0, aux v51 et v52b (contre-lectures CL15 et CL16) (`bwrap` absent des machines
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
- **Préparation** : code v60 à v64 ; préenregistrement en six brouillons, aucun scellé dans l'arbre public ; cinq contre-lectures (brouillons 1, 2, 3, 5 et 6 ; aucune propre au brouillon 4), la dernière « scellable après couples » ; commandes v6 contre-lues « scellables
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
- **Préalables** (GO-2026-11-08-02, mots de Lazar R-2195) : (1) **contre-lecture du code v65 rendue le 10 novembre**
  (`contre-lecture-code-v65-v2.md`, `c4ddfc7f…`, R-2215) : « utilisable pour la course après corrections » ; suite, banc et essai à
  blanc rejoués à l'identique ; bloquants CLV65-01 et CLV65-02 ; CLV65-03 à -06 (vue servie non vérifiée ; 17 mutations sur 20
  survivent ; garde 7 incomplète ; banc à 37 sur 38 sous `bwrap`) ; CLV65-07 (le lanceur refuse `registres/go.md` : identifiants en
  double, lignes d'extension) ; CLV65-10 (l'empreinte de la configuration gèle des chemins absolus de commandes absents de `main`) ;
  **la mère a décidé une v66** sous noms neufs, en écriture par un développeur neuf, à contre-lire à son tour [RA134, RA135] ; (2) **machine avec bac à sable** validée par
  l'essai à blanc `--bac reel` ; (3) **préenregistrement scellé** (brouillon 1 du 7 novembre au dossier, non scellé ; la lecture gelée du code v65 suit ses
  critères, section 8 du brouillon) [RA89, RA65].
- **Enveloppe** : GO-2026-11-10-10 (inscrit à 12:05 UTC le 10 novembre, R-2206) : 120 USD au plus jusqu'au 30 novembre, dont **45 pour
  la boucle réelle** (40 de modèles, 5 de machine jetable Hetzner CPX32), conditions de GO-2026-11-08-02 « inchangées et toutes
  exigées », plus la **configuration v5 `995eb918…`** ; et 75 pour un témoin de l'attaque publiée de Bailey (course à part) [RA7].
  La ligne ne dit pas si elle se cumule avec GO-2026-11-08-02 ; lecture prudente : une seule course de 45 USD (sans source pour un
  cumul).
- **Point neuf à trancher** : le code v65 rendu porte la configuration `exemples/configuration-boucle-reelle-v5.json` d'empreinte
  **`bff138d8a30c57b8…`**, alors que GO-2026-11-10-10 et la note de la session-dépôt qui la fonde exigent **`995eb918…`** ; aucune pièce
  de `main` ne dit à quoi correspond `995eb918…` (recherche par `git grep`). Tant que l'écart n'est pas levé (ligne corrigée par toi,
  ou configuration alignée et contre-lue), la course ne peut pas remplir la condition écrite [RA6, RA7].
- **Suite** : code v66 et sa contre-lecture ; dossier du texte scellé — la contre-lecture recommande `orchestrator/prereg/`, copie
  locale à l'octet, et pousser au dépôt public reste ta décision ; machine à `bwrap` (avec la session-dépôt) ; préenregistrement
  scellé ; course avant le 30 novembre ; sortie scellée ; verdict par un lecteur neuf [RA89, RA134].

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
| **Nul v9** (2 novembre) | défense contre la classe de W2 | ajoute les recombinaisons par morceaux ajustées (par sous-population, ou de part et d'autre d'un seuil sur un trait), avec certificat ; preuve contre-lue (48 mondes neufs, 288 instants, 0 échec) ; classes **déclarées non couvertes** : profondeur 2 et seuils sur une combinaison de traits, marches douces, produits et déformations non monotones, morceaux tempérés, compositions (`NON_COUVERT_V9` au commit `6510199` ; le bruit aveugle propre à un morceau y est classé « hors du nul par choix », promouvable, et non comme trou) | **validation décisive scellée : « puissance perdue »** (erreur tenue : 0 sur 1 000 sur 18 lignes fatales ; prix : puissance de 0,486 à 0,381 sur une interaction faible, perte appariée 0,105, plus de deux fois la marge de 0,05) | processeur | [RA97, RA98, RA101] |
| **Épreuve hors ligne du monde W2 gradué** | placer la dose à la frontière du v9 | — | λ* = 0,40 (loi du monde promue 803 fois sur 1 000 ; recombinaison pure 0 sur 1 000 à toutes les doses ; « λ* à la limite ») | processeur | [RA99] |
| **A1-v4** (9 et 10 novembre) | même attaque contre le **v9 candidat** | v9 | W2 (dans le nul v9) : « **résiste (à cette taille)** » (1 sur 24 avec retour ; l'ancien juge v8 battu 24 fois sur 24) ; W2 gradué à λ* : « **frontière franchie, robuste** » (10 sur 24 ; 10 des 17 lois promues se rejouent au-dessus de α après Holm) ; 8 prédictions tenues sur 11 ; gain du retour non établi ; verdict officiel par un lecteur neuf d'une autre lignée ; publié sur la page publique le 10 novembre | 114,0434 USD sur 200 (1 478 appels ; non rapproché d'une facture) | [RA100] |
| **Réplication par Kimi** de la reprise propre | seconde famille de modèles | — | **décidée** (GO-2026-11-02-25, 150 USD, jusqu'au 16 novembre), **non courue** (aucune ligne de dépense) | 0 | [RA102] |
| **Juge-tournoi** façon Co-Scientist | juge **génératif** mis sous la même attaque (second terrain du papier C) | — | **décidé** (juge Opus sur les crédits Claude, après A1-v4) ; conception v3 et devis à écrire | 0 | [RA103] |

**Ce que cela établit, et pas plus** : sur un monde jouet dans le nul v9 (W2 ; le texte gelé dit « deux mondes jouets au nul v9 », mais dans cette course W2 seul l'est), un fournisseur, une forme d'optimisation, le v9 n'a pas laissé passer de
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
| **Audit défensif** | cinq propositions acceptées ; pour l'organisme : juge d'une autre lignée (point 4) et l'**invariant** « aucun score de moniteur (sonde, juge) dans un signal d'entraînement ou de sélection de l'agent, hors bras d'attaque déclaré », valable aussi pour la piste « organisme », gardé par le code | N-053 | **décidé** ; dans l'orchestrateur : juges de fournisseurs différents, mémoire qui ne sert ni verdict ni témoin, proposeurs sans classement des juges (v59) ; aucune garde nommée « N-053 » vérifiée ici [RA108, RA109] |
| **Composition jugée sur l'oracle** | la composition des proposeurs se juge sur l'oracle du monde planté et le coût, jamais sur le verdict du juge | N-058 | **décidé** (section 4.2) [RA77] |
| **Duel des proposeurs** | en générations d'étalonnage, une mesure, une porte ; lois gelées vraies pour l'oracle par unité de coût | N-058, N-059 | **décidé** ; non relancé (sans source contraire) [RA77, RA78] |
| **Code figé et trois régimes de budget** | — | N-044, portée | **proposé, non tranché** [RA111] |
| **Récompense collective (Avalon)** | (a) maintenant : taux de signalement du modèle de départ (devis) ; **audit de calibration des juges existants sur les paires déjà produites contre l'oracle planté** (sans dépense) ; (b) ensuite : bras de l'étape 2, récompense collective contre individuelle, signalement aux humains mesuré dans les deux ; précautions d'Avalon « go » | R-920 ; N13 tranché (a) puis (b), R-959 | (a) **décidé**, aucune trace d'exécution au registre (recherche du motif « N13 » : dernière mention R-1036 avant R-2199, qui ne porte que l'état d'une course du collisionneur N12-N13) ; (b) **prévu** pour l'étape 2 [RA110] |
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
l. 7) ; la recommandation d'y ajouter Qu, Chen et Wang attend ta décision (section 5) [RA112, RA127].

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
| 2 novembre | A1 ; v59 (boucle fermée) ; tour fermé v60 à v63 ; nul v9 ; juges v2 ; collisionneur v8 versé sans lecture ; collisionneur v9 | [RA93, RA63, RA64, RA97, RA42, RA123, RA124] |
| 3 novembre | v64 ; préenregistrement de la validation du nul v9 scellé ; A1-v3 scellé ; courses des mentors | [RA64, RA70, RA95, RA115] |
| 4-5 novembre | juges v2 suspendus ; A1-v3, troisième course | [RA42, RA95] |
| 7-8 novembre | essai à blanc de la boucle réelle (défauts de la v64) ; GO-2026-11-07-11 ; GO-2026-11-08-02 ; validation du nul v9 courue (« puissance perdue ») ; note W2 ; question v2 du pilier attaque | [RA87, RA88, RA98, RA96, RA114] |
| 9 novembre | A1-v4 lancé ; N-064 ; N-065 ; juge-tournoi v2 ; juge Opus décidé ; rapport « principes, état, goulots » | [RA100, RA68, RA112, RA43, RA113] |
| 10 novembre | verdict d'A1-v4 et publication ; R-2152 ; code v65 rendu ; R-2195 ; R-2199 ; contre-lecture de la v65 lancée ; GO-2026-11-10-10 (12:05 UTC) | [RA100, RA4, RA65, RA33, RA28, RA89, RA7] |
| 10 novembre, 12:20 à 12:40 UTC | contre-lecture de la v65 rendue, v66 décidée ; critères du tour 2 N12-N13 scellés, lecteur neuf lancé ; programme v1 et inventaire v7 rendus | [RA134, RA136, RA137] |
| 10 novembre, 12:49 à 13:23 UTC | programme v2 rendu, vérification orchestrée lancée puis rendue ; pas (a) du pilier mathématique fait (synthèse du tour 2) ; pas (b) : dessin et devis de l'essai Lean rendus, contre-lecture lancée | [RA146, RA144, RA145] |
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

### 8.3 Lignes de GO de l'organisme encore ouvertes (principales ; liste non exhaustive : restent aussi dans leur échéance au registre des GO les lignes d'A1-bis GO-2026-11-02-11 et -12, du tour fermé à 15 USD GO-2026-11-02-19, des courses et collisionneurs sur les questions des mentors GO-2026-11-03-02 et -04 à -18, et du pilier attaque GO-2026-11-08-06, -07, -08 et -10)

| GO | objet | plafond | échéance | état |
|---|---|---|---|---|
| GO-2026-11-08-02 | plus petite course réelle de la boucle complète | 45 USD | 30 novembre | conditions non remplies : code v66 et sa contre-lecture, machine, préenregistrement [RA88, RA134] |
| GO-2026-11-10-10 | enveloppe : boucle réelle 45 USD (et Bailey 75) | 120 USD | 30 novembre | mêmes conditions, plus la configuration `995eb918…` (écart avec la v65) [RA7, RA6] |
| GO-2026-11-10-09 | autonomie de calcul de la mère (dépense de la v65 « sur devis dans l'enveloppe ») | 500 USD | 27 novembre | ouverte [RA121] |
| GO-2026-11-02-23 | tour fermé, étage 1 | 50 USD | 16 novembre | inutilisée [RA86] |
| GO-2026-11-02-25 | réplication par Kimi de la reprise propre | 150 USD | 16 novembre | inutilisée [RA102] |
| GO-2026-11-02-24, -32 | juges d'idée v2, course de validation | 60 USD | 16 novembre | suspendue (GO-2026-11-04-08) [RA42] |
| GO-2026-11-08-13 | course sur la question v2 du pilier attaque | 20 USD | 15 novembre | bloquée (règle de permission) [RA114] |
| GO-2026-11-02-22 et GO-2026-11-08-12 | A1-v4 et sa machine | 200 et 35 USD | 16 novembre | course finie [RA100] |
| GO-2026-11-02-06, -18, -20 ; GO-2026-11-07-11 ; GO-2026-11-08-04 | décisions (boucle fermée ; tour fermé D2 à D9 ; deux corrections ; course réelle ; W2) | — | 30 novembre | en vigueur [RA63, RA84, RA88, RA120] |
| — | juge-tournoi (juge Opus) | — | — | ligne à inscrire avec la conception v3 et son devis [RA43] |

### 8.4 Nœuds ouverts chez toi et points ouverts (organisme)

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
10. **Condition de configuration de GO-2026-11-10-10** : la ligne exige la « configuration v5 `995eb918…` » (comme la note de la
    session-dépôt `ddb77ed6…`) ; le code v65 porte `exemples/configuration-boucle-reelle-v5.json` =
    `bff138d8a30c57b898b84c5db49e00a501d15c158009deb12e697b9a13b0e322` ; aucune pièce de `main` n'explique `995eb918…` ; la
    contre-lecture de la v65 ne traite pas ce point ; avec la v66, la configuration changera encore : la condition est à préciser par
    toi (ligne corrigée) ou à faire préciser par la mère [RA6, RA7, RA135, RA136].
11. Divergence n° 1 de N12 (des moniteurs neufs comme filtre de fiches : lecture de N-058) — « à faire confirmer par Lazar » [RA30].
12. **Numérotation des couches** : deux numérotations contradictoires (§ 2.1) ; à trancher ou à documenter [RA140, RA143].
13. **GO-2026-11-02-23** (tour fermé, 50 USD) et **GO-2026-11-02-25** (réplication par Kimi, 150 USD) expirent le 16 novembre sans
    dépense ni clôture écrite [RA86, RA102, RA136].
14. **Audit de calibration des juges** (N13 (a), décidé en R-959) : aucune trace d'exécution au registre [RA110].
15. **Dossier du texte scellé de la course réelle** : `orchestrator/prereg/` en copie locale (recommandation de la contre-lecture) ;
    pousser au dépôt public est ta décision [RA134].
16. **Essai Lean (pas (b) de R-2199)** : GO de phase 1 et décisions D-1 à D-6 à poser après sa contre-lecture (plafond proposé
    450 USD et ≤ 50 USD de machine ; machine et réseau pour Lean) [RA145].
17. **Points du tour 2 N12-N13 pour toi** : ouvrir la couche 4 sur le seul essai ; la suite bon marché comme standard obligatoire ;
    le bornage « classe d'erreurs » ; divergences n° 1 et 7 renvoyées par les espèces [RA144].

### 8.5 Prochain pas de chaque chantier

| chantier | prochain pas | après | sources |
|---|---|---|---|
| **Boucle réelle (v65 → v66)** | code v66 (développeur neuf, en écriture), puis sa contre-lecture | lever l'écart de configuration ; dossier du texte scellé (copie locale ; dépôt public = ta décision) ; machine à `bwrap` validée par `--bac reel` (avec la session-dépôt) ; préenregistrement scellé ; course avant le 30 novembre ; sortie scellée ; verdict par un lecteur neuf | [RA89, RA6, RA7, RA134] |
| **Pilier mathématique (couche 4)** | (a) fait (R-2226) ; (b) dessin et devis rendus (R-2227) : contre-lecture 1 en cours (Fable) | GO de phase 1 à poser (D-1 à D-6) ; (c) note de conception du pilier « génération », nœud, sans matériau des espèces | [RA28, RA144, RA145] |
| **Juge statistique** | tes décisions sur le prix du v9 et sur « rien au-delà de l'archive » | bascule de production éventuelle ; revendication publique ; correction de la page publique sur « go publication » | [RA104] |
| **Juge-tournoi** | conception v3 (juge Opus) et devis | ligne de GO ; course d'étalonnage puis attaque | [RA43] |
| **Juges d'idée v2** | règle de diagnosticité neuve (rédacteur neuf) et batterie tenue à l'écart (contre-lecteur) | course de validation | [RA42] |
| **Pont fiche → loi** | ta décision D-P1 | couche v57 de l'orchestrateur ; témoins du pont ; épreuve fraîche décisive | [RA81, RA50] |
| **Tour fermé** | aucun écrit ; GO-2026-11-02-23 expire le 16 novembre | à clore ou à garder : décision de la mère ou de toi (sans source) | [RA86] |
| **Réplication Kimi d'A1-v3** | aucun écrit ; GO-2026-11-02-25 expire le 16 novembre | idem | [RA102] |
| **Couches 3 et 4** | fermées jusqu'aux résultats de l'étape 2, sauf l'essai sur processeur | — | [RA5] |
| **Étape 2 (lignée de l'objectif ultime)** | aucun préenregistrement trouvé | il porterait N-044 (familles inédites), N-045 (coût, composition, héritage), N-049, N-050, le bras d'Avalon | [RA15, RA105, RA110] |
| **Rôle 3** | ta décision | avant toute conception de sonde qui pourrait la toucher | [RA113] |
| **Ce programme complet** | v3 : 42 couples de la vérification orchestrée appliqués (R-2228) | remise à toi | [RA122, RA137, RA146] |

### 8.6 Lignes du registre depuis la v1 (R-2201 à R-2228), pour situer

| ligne | objet | touche l'organisme ? | sources |
|---|---|---|---|
| R-2201 | la session mère continue ; autonomie de 12 heures dans GO-2026-11-10-09 | cadre | [RA142] |
| R-2202, R-2206 | inscription de l'enveloppe de 120 USD refusée par le classifieur, puis **GO-2026-11-10-10 inscrit** sur mot direct de Lazar | oui (45 USD de la boucle réelle) | [RA7] |
| R-2203, R-2204, R-2205, R-2207, R-2208, R-2209, R-2210, R-2211, R-2212, R-2214, R-2218 | audit des fuites de T0.7, chiffre corrigé, validité de l'adaptateur, base (A) de T0.8, orchestrations ciblées, registre des prédictions | non, sauf R-2208 (2) : orchestration de vérification de ce programme | [RA142] |
| R-2213, R-2217, R-2219 | sections de résultats v3 contre-lues (CLR-01 : enveloppe dite non inscrite), puis v4 et v5 (organisme `77d0e57a…`, puis `b6a35432…`) | oui (section « organisme » des documents) | [RA139] |
| R-2215 | **contre-lecture du code v65 rendue** (utilisable après corrections) ; **v66 décidée** ; **critères du tour 2 N12-N13 scellés**, lecteur neuf lancé | oui | [RA134] |
| R-2216 | base (A) « mots et coût » de T0.8 scellée | non | [RA138] |
| R-2220 | programme v1 rendu et constat de l'écart de configuration ; module T0.7 rendu | oui (constat) | [RA136] |
| R-2221 | **inventaire v7 rendu** (411 entrées) ; contradiction des numérotations des couches relevée | oui | [RA137] |
| R-2223, R-2228 | **programme v2 rendu** ; **vérification orchestrée** lancée puis rendue (1 188 affirmations vérifiées, 1 136 conformes, 42 constats tenus) | oui | [RA146] |
| R-2224, R-2225 | socle de preuves v5 ; dossier fusionné v2 remis à Lazar par la session-dépôt (sa partie e = sections de résultats v5 de la mère) ; rapport court v4 | non, sauf la section « organisme » des résultats | [RA147] |
| R-2226 | **pas (a) du pilier mathématique fait** (synthèse du tour 2 N12-N13 scellée) ; pas (b) lancé | oui | [RA144] |
| R-2227 | **dessin et devis de l'essai Lean rendus** ; contre-lecture 1 lancée | oui | [RA145] |

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
| composition apprise (modèle par rôle) | décidé ; non codé | [RA105, RA14] |
| coût dans le signal, score net | décidé ; non codé | [RA105, RA14] |
| nécessité de la frontière mesurée | décidé ; non mesurée | [RA105] |
| voies bon marché avant la voie chère | décidé ; non courues | [RA105] |
| héritage récompensé sur K ≥ 3 générations | décidé ; non codé | [RA105, RA14] |
| pilote de bruit A/A ; poids contre archive | décidé ; non courus | [RA105] |
| espaces de conception égaux | décidé ; voie à fixer | [RA105] |
| tâches fraîches : part `test` tirée par génération | décidé ; non codé dans l'orchestrateur | [RA106, RA14] |
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
| couche 4 (pôle théorie et Lean) | prévu ; fermé sauf l'essai sur processeur ; ordre de R-2199 : (a) lecture du tour 2 N12-N13 faite (synthèse scellée `6ef6bc2e…`, R-2226), (b) dessin et devis de l'essai Lean rendus, en contre-lecture (R-2227), (c) note du pilier « génération » | [RA22, RA5, RA28, RA134, RA144, RA145] |
| numérotation des couches | deux numérotations contradictoires ; aucune pièce ne réconcilie | [RA140, RA143] |
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
| bac à sable `bwrap` | codé ; contre-lectures CL13 à CL15 de l'orchestrateur faites sous un vrai `bwrap` (R-797) ; jamais joué dans une course réelle, essais du vrai bac déclarés non joués pour la v65 | [RA19, RA65] |
| machine jetable (liste blanche) | codé (v56) ; machine de la v65 à monter | [RA82, RA83] |
| dossier fermé ; garde des outils | codé | [RA82] |
| boucle fermée (v59) | codé, décidé ; jamais couru | [RA63] |
| tour fermé (étage 1 ; étage 2 avec réserve) | codé (v60 à v64) ; jamais couru | [RA64, RA84, RA86] |
| boucle réelle v65 | codé sur branche ; contre-lu : utilisable après corrections ; v66 en écriture ; GO ouverts | [RA65, RA134, RA88, RA7] |
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
| collisionneur v8, **tour 2 N12-N13** (15 cellules sur 15) | branche `donnees/collisionneur-v8-runs-v2`, commit `0e7b3e59d7c5aeee5e63b43ef920fb8f565c8a11` | 15,60 USD (GO-2026-11-01-05) | **lue le 10 novembre** : synthèse scellée par un lecteur neuf (`6ef6bc2e…`, R-2226), sous les critères scellés `6bdbfe47…` (R-2215) | [RA123, RA28, RA134] |
| collisionneur v8, **convergence v3** | même branche, même commit | 26,09 USD (GO-2026-11-01-06), reprise comprise | non lu | [RA123] |
| collisionneur v8, **sélection génération à génération v1** | même branche, même commit | 16,38 USD (GO-2026-11-01-07), reprise comprise | non lu | [RA123] |
| collisionneur v8, **vérification non circulaire du bac à sable v1** | même branche, même commit | 16,24 USD (GO-2026-11-01-08) | non lu | [RA123] |
| collisionneur v9, **brainstorm du 2 novembre** (prompt de Lazar) | branche `donnees/collisionneur-v9-brainstorm-v1`, commit `ac25c055`, liste `08aebf56…` (13 cellules sur 15) ; suite sur `donnees/collisionneur-v9-brainstorm-v1-suite`, commit `42aa6b1b…` (R-1110) | ≈ 22,69 USD sur 40 (GO-2026-11-02-31), suite comprise | non synthétisé | [RA124] |
| A1-v3, **deuxième course** | état scellé | 48,49583 USD | non lu | [RA125] |

Les quatre runs du collisionneur v8 ont servi l'espèce B par `claude-opus-4-6` et non Opus 5.5 : écart déclaré, à porter sur toute
lecture (R-1050) ; ils ont été versés sans lecture sur le mot de Lazar « on peut zapper le collisionneur et avancer sur org ideation »
(R-1036) [RA123]. La liste complète des sorties non lues est l'objet du fichier voisin `sorties-non-lues-v2.md` (`2fb208d4…`, remplace la v1).

## Annexe B — trous, incohérences et limites de ce texte

1. **Couches 1 et 2 au sens de N12** : non définies dans les pièces lisibles (section 2.1) ; l'inventaire (ARC-045) relève la même
   contradiction des numérotations.
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
9. **Contre-lecture du code v65** : rendue après la v1 (R-2215), portée depuis la v2 ; la consigne et le code de la v66 ne sont pas lus ici.
11. **Partie II** : reprise de l'inventaire v7 ; la colonne « renvoi (partie I) » est calculée par des règles (journal v2), indicative,
    non relue entrée par entrée ; les statuts de l'inventaire sont relevés à ses propres pièces (jusqu'à R-2200 environ).
10. **Vérification** : la v2 a reçu une vérification orchestrée (« transmissible après corrections », R-2228) ; la v3 en applique
    les 42 couples sans nouvelle contre-lecture.
12. **Restes de la vérification** : les affirmations que son rapport dit « non vérifiables » (pièces hors de la tête de `main` ou
    sous la cloison) le restent ; les lignes 428 et 752 de la v2 portent maintenant deux formules voisines sur le bac à sable
    (VP-04 et VP-12), non fusionnées [RA148].

## Annexe C — correspondance entre les familles de l'inventaire (partie II) et les sections de la partie I

Inventaire repris : `inventaire-idees-organisme-v7.md` (`056adb7f5a0945127fcedab37b44b889f74dee50dbc8d4e7f02caa6bcaefc413`, version
finale, R-2221), en partie II. La table ci-dessous sert aussi de règle par défaut pour la colonne « renvoi » de la partie II. Écart
relevé entre les deux textes : la numérotation des couches (§ 2.1 ; ARC-044, ARC-045).

| section de ce texte | familles de l'inventaire |
|---|---|
| 1. Objectif ultime, lignées | ARC (architecture et couches), UNI (universalité et familles inédites) |
| 2. Couches | ARC ; MAT (mathématiques, preuve et Lean, couche 4) |
| 3. Rôles et pôles | ROL (rôles et pôles) ; OUT (outillage et gouvernance) |
| 4. Juge, mondes, pont, tests de mort, tour fermé, boucle réelle | JUG (juges et nuls) ; VER (vérité, oracles et mondes plantés) ; BOU (boucle fermée et héritage) |
| 5. Attaques et défenses du juge | ATQ (attaques et défenses du juge) |
| 6. Composition, coût, héritage, tâches fraîches | COM (composition apprise et coût) ; BOU ; REC (récompense collective et signalement) |
| 7. Rôles dans le programme | PAC (papier C et menaces diffuses) |
| Annexe A. Sorties non lues | `sorties-non-lues-v2.md` (`2fb208d4244035f8eb287eac95d4f925605be1cb6752879c88e70f36ddd4d2b2`) |

Règle par défaut de la colonne « renvoi » de la partie II, et lignes correspondantes de la table du § 9 :

| famille | sections de la partie I | lignes de la table du § 9 |
|---|---|---|
| ARC | § 1, § 2 | les sept premières lignes (objectif ultime), couches 0 à 4, numérotation des couches, pilier « génération » |
| ROL | § 3 | proposeurs, aiguilleur, mémoire, juges croisés, juges d'idée v2, juge-tournoi, bisociateur, metteur en fusion, moissonneur |
| JUG | § 4.1 | juge statistique, nul v8, nul v9, règle e-BH, pari apparié borné, revendication O2 |
| ATQ | § 5 | banc des tricheurs, A1, A1-bis, A1-v3, A1-v4, réplication par Kimi |
| BOU | § 4.5, § 4.6, § 6 | boucle fermée, tour fermé, boucle réelle v65, héritage récompensé |
| COM | § 6 | composition apprise, coût dans le signal, frontière, voies bon marché, deux expériences bon marché |
| UNI | § 1.1, § 6 | universalité, tâches fraîches, banque sœur, `test_final` |
| VER | § 4.2 | témoins plantés, mondes, oracle, composition jugée sur l'oracle, duel des proposeurs |
| MAT | § 2.5 | couche 4, pilier « génération » |
| REC | § 6 | récompense collective (audit de calibration ; bras de l'étape 2) |
| PAC | § 7 | rôles 1, 2 et 3 ; course de la question v2 du pilier attaque |
| OUT | § 3.2, § 8 | bancs de mutations, machine jetable, dossier fermé, garde des outils |

---

# Partie II — Inventaire exhaustif des idées, hypothèses, résultats et propositions (411 entrées)

- **Provenance** : reprise de `inventaire-idees-organisme-v7.md` (`056adb7f5a0945127fcedab37b44b889f74dee50dbc8d4e7f02caa6bcaefc413`,
  version finale du rédacteur voisin, R-2221), même dossier ; son journal `journal-inventaire-v7.md` (`f508d476…`) liste ses trous
  connus ; les sorties non lues sont dans `sorties-non-lues-v2.md` (`2fb208d4…`) [RA141].
- **Ce que j'ai ajouté, et rien d'autre** : le préfixe « II. » des sections ; dans les douze tables de familles, une dernière colonne
  « renvoi (partie I) », calculée par des règles écrites (famille d'abord, puis mots-clés de l'entrée ; règles au journal v2, § 3) :
  **indicative**, non relue entrée par entrée. Idée, type, origine, statut et source sont ceux de l'inventaire, à l'octet.
- **Sources des entrées** : la colonne « source » garde les clés de l'inventaire (par exemple `SRO`, `N044:13`, `[B52]`, `DEC R-2152`),
  qui renvoient à la table du § II.1 ci-dessous, reproduite avec ses empreintes ; les renvois [RAn] de la partie I ne s'appliquent pas
  à la partie II.
- **Écarts connus avec la partie I** : (1) la numérotation des couches (§ 2.1 ; ARC-044, ARC-045) ; (2) les statuts de l'inventaire
  sont relevés sur ses pièces (jusqu'à R-2200 environ) ; la partie I les met à jour jusqu'à R-2228 (contre-lecture de la v65, v66,
  lecture du tour 2 N12-N13, devis de l'essai Lean) : en cas d'écart, la partie I prime pour l'état, l'inventaire pour l'idée ; (3) statuts de l'inventaire déjà périmés à sa date de lecture, laissés tels quels pour garder l'identité à l'octet : ATQ-016, ATQ-038 et ATQ-039 citent R-611 comme en vigueur, alors qu'elle a été levée le 31 octobre (R-888 ; examen final et estimation de la malléabilité dits hors gel par R-889 ; restriction levée pour le bras d'attaque par R-2146 ; OUT-024 le dit) ; ARC-013 : D1 tranchée (b) par le directeur (R-634), chaque lancement restant sous son GO ; JUG-001 : décidé (R-2026), conception v3 et devis à écrire ; (4) renvois imprécis de l'inventaire, laissés tels quels : la copie DEC de 2 171 lignes va jusqu'à R-2213 ; `[Bn]` est à la ligne 187 + n pour B46 à B53 ; ROL-035 se lit QM:70-71, 182 ; la citation d'ATQ-010 omet « sous v9 » (A4V:36).
- **Erratum de la vérification orchestrée (tranche II-b), porté ici pour garder la copie à l'octet** : douze couples visaient
  des statuts de l'inventaire ; le texte de la copie ci-dessous reste celui de l'inventaire v7, la lecture corrigée est celle-ci
  [RA148]. Depuis R-2227, le dessin et le devis de l'essai Lean sont rendus et en contre-lecture (VP-15, VP-39 disent « lancé »,
  « en rédaction ») [RA145].

| constat | entrée | texte de l'inventaire (inchangé dans la copie) | lecture corrigée |
|---|---|---|---|
| VP-13 | BOU-005 | dépense sur devis dans l'enveloppe de calcul accordée jusqu'au 27 novembre ; contre-lecture du code lancée puis interrompue par la fin du quota | dépense de 45 USD au plus (GO-2026-11-08-02, repris par GO-2026-11-10-10, R-2206, jusqu'au 30 novembre), inscrite sur devis dans l'enveloppe de calcul accordée jusqu'au 27 novembre (GO-2026-11-10-09) ; contre-lecture du code rendue le 10 novembre (R-2215 : utilisable après corrections, v66 lancée) |
| VP-14 | BOU-003 | codé (branche prep/organisme-v65-v1, tête 3daf08e24) ; non contre-lu | codé (branche prep/organisme-v65-v1, tête 3daf08e24) ; contre-lu le 10 novembre (R-2215 : « utilisable pour la course après corrections », bloquants CLV65-01 et CLV65-02) ; v66 lancée sous noms neufs |
| VP-15 | MAT-002 | décidé (R-2199) ; (a) lancé le 10 novembre | décidé (R-2199) ; (a) fait le 10 novembre (R-2226 : synthèse du tour 2 N12-N13 scellée) ; (b) lancé (dessin et devis en rédaction, aucune dépense avant GO) |
| VP-16 | OUT-006 | proposé, défaut (a) le 11 novembre ; leçon écrite | tranché par Lazar le 9 novembre : option (a) (R-2043, voir OUT-030) ; leçon écrite |
| VP-17 | OUT-007 | confiance 0,7 / proposé non tranché / RPG:42, 120-122, 188 | confiance 0,7 / décidé (« go » de Lazar le 9 novembre, R-2026 ; GO-2026-11-09-05) ; aucun tour en mode critique consigné comme couru au registre / RPG:42, 120-122, 188 |
| VP-18 | OUT-049 | (27 octobre, R-546) ; la relecture reste. | (27 octobre, R-546) ; la contre-lecture du texte (R2) qui s'y attache est levée aussi (lecture de conv-audit consignée en R-546, redite en R-552) ; les autres règles restent (lecture dans les deux sens, gardes, empreintes, rien d'écrasé, aucun run visant un signe). |
| VP-37 | BOU-005 | prévu ; aucune course réelle autorisée au 10 novembre | prévu ; GO accordé sous conditions (GO-2026-11-08-02, repris par GO-2026-11-10-10) ; conditions non remplies et aucune course réelle lancée au 10 novembre |
| VP-38 | BOU-026 | course réelle attend v65 contre-lu et préenregistrement (GO-2026-11-08-02, 45 USD) | course réelle attend le code corrigé (v65 contre-lue le 10 novembre, R-2215 ; v66 en cours), la machine à bac à sable et le préenregistrement scellé (GO-2026-11-08-02, repris par GO-2026-11-10-10, 45 USD) |
| VP-39 | MAT-005 | devis prévu (R-2199 (b)) | dessin et devis en rédaction (R-2199 (b), lancé en R-2226) |
| VP-40 | MAT-008 | pilier « génération » en conception (R-2199 (c)) | note de conception du pilier « génération » prévue après (a) et (b) (R-2199 (c)) ; aucun début consigné au registre (R-2226) |
| VP-41 | OUT-008 | DEC R-2111 ; A4V:4 | DEC R-2111 ; A4V:6 |
| VP-42 | UNI-010 | d'un texte de test est écarté | d'un texte de la banque est écarté |

- **Correspondance des familles** : annexe C de la partie I (famille → sections → lignes de la table du § 9).

## II. En-tête de l'inventaire v7 (texte du rédacteur voisin, inchangé)

**Inventaire des idées, hypothèses, résultats et propositions de l'organisme d'idéation — v7 (jalons 1 à 7, version finale de la tâche)**

- **Version** : v7, écrite le 10 novembre 2026 à 12:38 UTC (`date -u`). **Version finale de cette tâche** : couvre les sept jalons (rapports au directeur ; décisions ; registre des décisions ; synthèses du collisionneur ; dépôt public ; antériorité, question-mère, bisociation, juges v2, convergence, pilier attaque ; pièces restantes et programme de conception de conv-audit). Elle n'est pas exhaustive au sens strict : les **trous connus** sont listés au journal v7 (`journal-inventaire-v7.md`, § « Trous connus »). Remplace la v6 (`7cfc90e1…`, gardée, R12) : mêmes entrées et mêmes numéros, plus le jalon 7. Sorties payées non lues : `sorties-non-lues-v2.md`.
- **Comment lire** : douze familles (§ 2 à § 13) ; dans chaque table, une ligne par idée distincte, dans l'ordre où les sources l'ont fait apparaître (jalon par jalon), avec son type, son origine (qui l'a eue ou portée), son statut et sa source. Une même question peut avoir plusieurs lignes quand elle a une demande, une décision et des résultats distincts ; les renvois R- et N- permettent de les relier.
- **Rédacteur** : sous-agent neuf (Claude Opus 5.5) de la session mère, consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-inventaire-idees-organisme-v1.md` (`2f16dfd064540f9b…`, vérifiée contre son compagnon). Aucun appel de modèle, aucune dépense, aucun commit.
- **Demande du directeur (verbatim)** : « ecir smoi le programme complet exhaustif avce toutes les couchhes et mecanismes prevus pour l'org » puis « precise bine dans le programme toutes nos idees hypotheses resultats proposiitons pour que rien de notre brinstorm ne soit perdu ».
- **Règles suivies** : une entrée par idée distincte, même petite, même écartée ; chaque affirmation renvoie à une pièce (clé, ligne) dont l'empreinte est au § 1, ou à une ligne R- de `registres/decisions.md` (R6) ; ce qui n'a pas de source est dit « sans source ». Statuts : **codé** (avec commit ou branche), **décidé** (avec N- ou R-), **prévu**, **fermé**, **proposé non tranché**, **écarté** (et pourquoi) ; un résultat couru et scellé est « fermé ». Types : idée, hypothèse, résultat, proposition, objection, piste écartée, question ouverte.
- **Ce que ce texte ne contient pas** : aucune cellule de collisionneur ni réponse de modèle non synthétisée (elles sont listées à part dans `sorties-non-lues-v*.md`) ; rien du bras d'attaque ni du mode tenu à l'écart au-delà de son existence ; aucune valeur de sonde de la course 7a ; aucune recette d'attaque (niveau méthode, R-607) : une attaque se décrit par sa classe et son but.
- **Notation des sources** : `CLÉ:n` = pièce CLÉ du § 1, ligne n ; `[Bn]` = rangée Bn du registre des affirmations v3 (clé RAF, ligne 186 + n), suivie de la pièce primaire et des lignes qu'elle cite ; `DEC R-n` = ligne R-n du registre des décisions.

## II.0 Jalons couverts par cette version

| jalon | famille de sources | heure de scellement (UTC, `date -u`) | entrées ajoutées |
|---|---|---|---|
| 01 | rapports au directeur : rapport principes-état-goulots du 9 novembre, section « Résultats de l'organisme » v3 et son registre des affirmations, prémisses de la trace interne | 12:07 | 67 |
| 02 | décisions et propositions de `docs/decisions/` (N-044 à N-066, D-3 à D-5, P-036, P-041) | 12:15 | 110 |
| 03 | registre des décisions `registres/decisions.md` (R-059 à R-2200, lignes de l'organisme) et liste des sorties non lues | 12:27 | 118 |
| 04 | synthèses scellées du collisionneur : nœuds (tours 1 et 2), N12-N13 (couches 3 et 4, récompense collective), boucle moisson | 12:30 | 32 |
| 05 | dépôt public `lciric/ideation-organism` (README, conception v7, LISEZMOI du pont) | 12:33 | 40 |
| 06 | antériorité (rapport C4, O1 à O20), question-mère, bisociation, juges v2, convergence de la défense, question v2 du pilier attaque | 12:35 | 25 |
| 07 | pièces restantes de l'organisme (contre-lectures de l'orchestrateur, tour fermé, IA scientifique externe, coffre, bras méta, machine jetable) et programme de conception de l'organisme v1 (conv-audit) | 12:38 | 19 |

## II.1 Pièces citées (clé → chemin → sha256)

Les sources des tables s'écrivent `CLÉ:ligne(s)` ; `R-n` renvoie à la ligne R-n de `registres/decisions.md` (fichier vivant ; empreinte de l'instant du relevé à la clé DEC) ; `[Bn]` renvoie à la rangée Bn du registre des affirmations v3 (clé RAF).

| clé | chemin | sha256 | note |
|---|---|---|---|
| CONS | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-inventaire-idees-organisme-v1.md` | `2f16dfd064540f9b360da7855424cad6fe6141bb584a6aead8ddee76f3fc7da1` | consigne de cette tâche |
| RPG | `docs/notes/rapports-directeur/rapport-principes-etat-goulots-entretien-organisme-2026-11-09-v1.md` | `22263fced8d43771f0a34b3cdd9b0e6b318e39d23189907a3e9736e74413b984` | rapport de la mère au directeur, 9 novembre ; « D:n » y renvoie à une ligne de registres/decisions.md |
| SRO | `docs/notes/rapports-directeur/resultats-pour-documents-v3/section-resultats-organisme-v3.html` | `d6d702f5383347f16c894065ce45d96745a20f6016243d5f3b956828b3a3d9fd` | section « Résultats de l'organisme » v3, non contre-lue ; renvois [B1] à [B53] |
| RAF | `docs/notes/rapports-directeur/resultats-pour-documents-v3/registre-affirmations-v3.md` | `38c24c925e151dc50f8b5b59eee9d8ff04c9b08e2cc4f52a9d9206553905780e` | registre des affirmations v3 ; rangées B1 à B53 (l. 187-240) |
| PRM | `docs/notes/rapports-directeur/premisses-trace-interne-v1.md` | `2638558e34c15800acf7c8d8653dd978eba0660a9341795069d7ddd3b58e712f` | lu par recherche ciblée : « organisme » y désigne les organismes-modèles de T0.6 ; aucune entrée |
| A13 | `docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md` | `7dade9ef12a4dfa4c1ce3345d35ce9b533e8696ebdf9882443a20ad5a5e78135` | verdict scellé, troisième course d'A1-v3 |
| A4V | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md` | `e6e2f17076fab16f2684553765517937d528c657367075c126945c3ae3741cda` | verdict officiel scellé d'A1-v4 |
| A4T | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/preenregistrement-attaque-goodhart-v5-v1.md` | `d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6` | texte scellé d'A1-v4 |
| V9 | `docs/verdicts/verdict-validation-nul-v9-v1.md` | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` | verdict de validation du nul v9 |
| EPT | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v2-v1.md` | `e025f108bf84d75bd7d66bc14406ac2eafdbe00dc664f717cb4d7a2f08f4d42c` | texte court scellé, choix de λ* |
| EPL | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v1-rejeu-v2-lecture-v1.json` | `dc0bb41a337aad04182d8b7f70cb63cafd606db5396e5b5babe490e1fc6a5c50` | lecture scellée de l'épreuve de dose |
| EAB | `docs/notes/organisme-boucle-reelle-v1/essai-a-blanc-v1/journal-essai-a-blanc-v1.md` | `627f7a4c0dcede675cef70f7af73c47298bafa772cad3cc7d7e4dfaf18f7fa80` | journal de l'essai à blanc de la boucle réelle |
| N064 | `docs/decisions/decision-N-064-v1.md` | `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97` | décision N-064 |
| N065 | `docs/decisions/decision-N-065-v1.md` | `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4` | décision N-065 |
| NPOP | `docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-popper-evaluator-v1.md` | `d1ab704927b938aab631451b01ea2f197969f627dec32dcf63087bbc42ad0998` | note d'antériorité POPPER |
| NCOS | `docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-co-scientist-v1.md` | `08a3738af518f59790936995cda714210c749f20e1891195343b2c3e2b132312` | note d'antériorité Co-Scientist |
| PUB | `livrables/page-publique-organisme-2026-11-10-v1/README.md` | `b72c983eada4449931ff828d4e841aaf6708bce881657c745a8c113f3392321e` | texte exact publié le 10 novembre |
| C4R | `prep/etat-de-l-art-niveau3-v1:docs/etat-de-l-art/niveau3-v1/rapports/rapport-C4-organisme-ideation-O1-O20-v1.md` | `164502a3ed94e0adf177e4e15bfd61fc95ea24633dc1c4a2b0cacf9effab1245` | sur branche, lu par git show |
| C7R | `prep/etat-de-l-art-niveau3-v1:docs/etat-de-l-art/niveau3-v1/rapports/rapport-C7-contre-lecture-qu-chen-wang-dossier-c8-v1.md` | `63d8373761d28c62b556f35839bd7b9f277decf4dc2d6d1ad44ad1f2266f8fb2` | sur branche, lu par git show |
| V65R | `prep/organisme-v65-v1:docs/notes/organisme-boucle-reelle-v1/code-v65/rapport-developpeur-organisme-v65-v1.md` | `f84c14303eacf87e7e129955d3f9b7ba35fc7504545033c37b66b9c4ad5aff0c` | sur branche (tête 3daf08e24), lu par git show |
| DEC | `registres/decisions.md` | `d10a422e69ca8d2177306ae1c45112659a6bf791760b7cb8a32d826e0db8c2a8` | fichier vivant ; copie de lecture prise le 10 novembre à 12:16 UTC (2 171 lignes, jusqu'à R-2200) ; lignes R- stables |
| N3S | `prep/etat-de-l-art-niveau3-v1:docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-provisoire1.md` | `8adb561d52b728114cfd0c3065fe6c6230262f1befaeb2fd9d9824270ecdc3ad` | synthèse provisoire, citée d'après RAF ; non relue par le rédacteur |
| N044 | `docs/decisions/decision-N-044-v1.md` | `2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf` | objectif ultime, universalité, vivier, questions ouvertes, diversité |
| N045A | `docs/decisions/decision-N-045-v1.md` | `42be51f6e56c1971a0c1184d3c104bbf51052d428c5ae211c58f6ebafad33300` | N-045 v1, remplacée par la v2 |
| N045 | `docs/decisions/decision-N-045-v2.md` | `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d` | composition apprise, coût dans le signal, héritage |
| N047 | `docs/decisions/decision-N-047-v1.md` | `20941ec350762a140dba753ffa535f68dc7217cf91df5c20c8e8eef9a0d95267` | même contenu que N-053, numéroté par erreur |
| N049 | `docs/decisions/decision-N-049-v1.md` | `8a5bf5e57e2bb447467388acb572e032d1a6a578a868db1b7304263a1c9d4460` | tâches fraîches (même note que N-050) |
| N050 | `docs/decisions/decision-N-050-v1.md` | `a54b128df955dba34bb360fa2fea466c787026a934f25135d698e8cd925d5f58` | test_final lu une fois |
| N052 | `docs/decisions/decision-N-052-v1.md` | `817d218b22b8d1d4a2c03bb78fb4870867f19bd1a1f9c08b0a1873efbb31a384` | contre-lecteur de la boucle extérieure |
| N053 | `docs/decisions/decision-N-053-v1.md` | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` | cinq propositions de l'audit défensif |
| N055 | `docs/decisions/decision-N-055-v1.md` | `371879d5bd44f5fdd7f2ff2fe068065776000e0b2acc9118fa94b41f687340b6` | lu pour ses lignes sur l'organisme du pôle |
| N056 | `docs/decisions/decision-N-056-v1.md` | `3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d` | lu pour ses lignes sur le pôle |
| N057 | `docs/decisions/decision-N-057-v1.md` | `42180088efb2e1016251fa329421fc08ebcb13039266d278c1a6f37ced60af99` | cellules en quarantaine du collisionneur |
| N058 | `docs/decisions/decision-N-058-v1.md` | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` | composition jugée sur l'oracle et le coût |
| N059 | `docs/decisions/decision-N-059-v1.md` | `41aff854c38bed3a43aced62bd0c1b3af782c5a5f6174f335a175847b407e687` | nœuds de l'affinage v2 |
| N060A | `docs/decisions/decision-N-060-v1.md` | `4a09c5f54b3191ccd102f69ccd98a4f3555095b6133c57c7484f42bdfed980ea` | N-060 v1 (oracle C seul) |
| N060B | `docs/decisions/decision-N-060-v2.md` | `06a7cb237bde15f18721b908274c2e7655d92c4df2d8905d6334d32de18d0270` | N-060 v2 (trois oracles) |
| N060 | `docs/decisions/decision-N-060-v3.md` | `2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591` | N-060 v3 (oracle de couverture) |
| N066 | `docs/decisions/decision-N-066-v1.md` | `21e83ed58c7498c65b7f9ae78613bc38301acdf0dd15a9890af13e6c0edbd351` | lu ; ne touche pas l'organisme |
| SPK | `docs/decisions/decision-sparks-D3-D4-D5-v1.md` | `6b5f3f2dd6b15b1d40f4b0a3a302e08c56bed61d251ca4c0632da4abb610a6e9` | décisions D-3, D-4, D-5 |
| P036A | `docs/decisions/proposition-P-036-couche-2-preparation-v1.md` | `a8c41681f1c9ee539a0abfd4b8bf0367e1a2e0ba4a7dd30e27db1c87f867e97c` | couche 2, v1 |
| P036B | `docs/decisions/proposition-P-036-couche-2-preparation-v2.md` | `155f0511991d420c257c563b98c70fdaa0994b0134d312d365ccada071b39c25` | couche 2, v2 |
| P041A | `docs/decisions/proposition-P-041-organisme-coevolutif-attaque-defense-v1.md` | `254b178270f11123c4bf0c24ead0855c982550730c54bcba0924a39c6d04ca9b` | organisme coévolutif, v1 |
| P041B | `docs/decisions/proposition-P-041-organisme-coevolutif-attaque-defense-v2.md` | `2df36f8793668fcb7e2dfba9cdbca0cce77a992063c99f6e1932849b6948f01b` | v2, lue par différence avec la v3 |
| P041 | `docs/decisions/proposition-P-041-organisme-coevolutif-attaque-defense-v3.md` | `72aec5322c61490df41ed0d4b60f5ee24e5ce54e2b62896790a0df6e374b7725` | organisme coévolutif, v3 (lecture en vigueur) |
| DEP | `registres/depenses.md` | `vivant` | lu pour les seules lignes 319, 324 et 333 (dépenses du collisionneur v8, du collisionneur v9 et de la course Heimersheim) |
| SN1 | `docs/notes/ideation-organisme-v1/course-2/collisionneur-noeuds-v1/synthese-noeuds-v12-tour1-v2.md` | `d313b4826d649ad8eb9a6e0b44a7b9eea452c7a74428b9626bcbb3bb237ee43e` | synthèse du tour 1 des nœuds (v2, erratum appliqué) |
| SN2 | `docs/notes/ideation-organisme-v1/course-2/collisionneur-noeuds-v1/synthese-noeuds-v12-tour2-v2.md` | `f4f2d1974828dcb9e8d9654614fa70328057ceb60833cc54e02f9eb1db13e9d2` | synthèse du tour 2 des nœuds (v2) |
| SNN | `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-v2.md` | `f0340581766c5fb4d97a0ccb06f0cf1738a15228385b332ee602e93a0be28f0a` | synthèse N12-N13, tour 1 (v2) |
| SBM | `docs/notes/ideation-organisme-v1/course-2/collisionneur-boucle-moisson-v1/synthese-boucle-moisson-v2.md` | `efec05a9e4acfd39cce51e30614f903feed5a484d0353922e7d31cd412891738` | synthèse « boucle moisson » (v2) |
| RDM | `/home/user/ideation-organism/README.md (dépôt public, tête 6510199)` | `b72c983eada4449931ff828d4e841aaf6708bce881657c745a8c113f3392321e` | README public, identique à l'octet à PUB |
| CV7 | `/home/user/ideation-organism/orchestrator/conception-v7-v1.md` | `31fc8c4bc286341fcbf10181be6779ecd20ddf9de092a2c885ce8d11b27fedee` | conception de l'orchestrateur v7 (conv-audit, 27 octobre), compagnon vérifié |
| PNT | `/home/user/ideation-organism/pont-fiche-loi-v1/LISEZMOI-pont-v1.md` | `7b1c131db760014798af159047849163bedc03b706f2f684dd0962ac4d6bd17a` | LISEZMOI du pont fiche → loi (conv-audit, 1er novembre), compagnon vérifié |
| QM | `docs/notes/ideation-organisme-v1/course-2/synthese-collisionneur-question-mere-v2-v1.md` | `25e2d3518a8de618fa0bbdf153af8ca9de86ac17494ac950f25bc4715b243218` | synthèse du collisionneur sur la question-mère v2 |
| BIS | `docs/notes/ideation-organisme-v1/bisociation-deux-espaces-v1/synthese-collisionneur-bisociation-v1.md` | `49dd38406b865eae742793045472cac3385e29ef3f3cf1921841df4d94361fb0` | synthèse du collisionneur sur la recombinaison bisociative à deux espaces |
| JV2 | `docs/notes/ideation-organisme-v1/juges-v2-brouillon4-v1/preenregistrement-juges-idees-v2-brouillon4.md` | `f76162849620b161c2bc2dcdae90f6ed78342ca19a0978390cd0788551cc8537` | préenregistrement des juges d'idéation v2, brouillon 4 (non scellable) |
| CDF | `docs/notes/convergence-defense-v1/LISEZMOI-convergence-defense-v1.md` | `8456f99668c08c216ee5b7f52b2863d7bd7671d117f11636befe1ee20eddd3cd` | LISEZMOI de la convergence de la défense (formalisation du jeu, jouet OpenSpiel) |
| PAQ | `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md` | `2dbad4b75d20fadc3147be9eff07f2e77c2f82fe4f609ab1c29388ab46c4bb42` | question v2 scellée du pilier attaque |
| CL31 | `docs/notes/ideation-organisme-v1/contre-lecture-v31-cl1.md` | `f4c7d1943963a6c899ad7549b0cb937dd2f01199fa318748b3fb558b46be8792` | contre-lecture 1 de l'orchestrateur v31 (prise idéation) |
| CL17 | `docs/notes/ideation-organisme-v1/contre-lecture-cl17-orchestrateur-v52-v1.md` | `c5b361090731c526d458bace28eef9bfca4e5e1b647be4e560dc88534d5cb598` | contre-lecture 17 de l'orchestrateur v52 |
| TFE | `docs/notes/ideation-organisme-v1/tour-ferme-etage1-v1/LISEZMOI-tour-ferme-etage1-v2.md` | `0124f4e5c9264d1eff0e296855ffce748ebd59394c911ea967309fa9f3d784b5` | LISEZMOI v2 du tour fermé, étage 1 |
| ISX | `docs/notes/ideation-organisme-v1/ia-scientifique-externe-v3/essai-a-blanc-v1/architecture-essai-a-blanc-v1.md` | `e38f9661174a8ae2ab48fd78f178ba70b797f8a5c6ac944bfc53fabca641ab29` | architecture de l'essai à blanc de l'Agentic Scientist v3 |
| COF | `docs/notes/ideation-organisme-v1/course-2/coffre-attaques-inedites-v1/question-coffre-attaques-inedites-v2.md` | `7d22b64e64c41cac4100d0dfbe825c598daeedfb0f515e0aab3f17ffe661db8c` | question v2 du coffre des attaques inédites (niveau méthode) |
| ABM | `docs/notes/ideation-organisme-v1/course-2/pre-pilote-course-2-v1/annexe-bras-meta-v1-brouillon6.md` | `e1680c41a180fea506bc5e80f9e686cf9efb42d6acdd3eef353dd5e7d2f21fcf` | annexe du bras méta, brouillon 6 (lue pour son en-tête) |
| MJE | `docs/notes/ideation-organisme-v1/machine-jetable-v1/devis-et-plomberie-machine-jetable-v1.md` | `4fccbc75e3c6da3bbb8d4a4213b0fa4a104b584f2a685139c4d0dff0e6c10125` | devis et plomberie de la machine jetable, v1 (en-tête) |
| PCO | `origin/canal/conv-audit-n04:brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/programme-conception-organisme-v1.md` | `72fa0e609258d1a208195440c645f2b7f250c5c5bba70e304407ded09de3c6ff` | programme de conception de l'organisme v1 (conv-audit, 27 octobre), lu par git show ; empreinte égale à celle que cite CV7 (« 72fa0e60… ») |

## II.2 Architecture et couches (ARC, 46 entrées)

| n° | idée | type | origine | statut | source | renvoi (partie I) |
|---|---|---|---|---|---|---|
| ARC-001 | Définition de travail : l'organisme d'idéation est une boucle où des modèles de langue, les « proposeurs », proposent des lois chiffrées sur des données, et où un juge statistique, calculé hors des agents, décide si une loi est « promue ». | idée | dessin de l'organisme (rédaction : agent de la section Résultats v3) | codé (orchestrateur ; courses A1 à A1-v4) ; énoncé du juge décidé (N-064) | SRO (paragraphe d'ouverture) ; [B1] N064:13 | § 1, § 2, § 3.1, § 4.1, § 5 |
| ARC-002 | Lignée : l'organisme d'idéation est l'organisme de l'objectif ultime du programme, branché depuis le 28 octobre sur la tâche « proposer des hypothèses de recherche jugées par un juge statistique » ; il n'en a pas encore les propriétés (il ne se conçoit pas seul ; rien n'est figé après conception ; universalité non mesurée). | idée | Lazar (décision du 10 novembre) | décidé (R-2152) | [B52] DEC R-2152 ; SRO (« Décision du directeur du 10 novembre ») | § 1, § 1.1, § 1.3, § 2 |
| ARC-003 | Méta-architecture : la majorité du budget sert à concevoir la méta-architecture de l'organisme ; une fois conçu, il est « câblé » dans son architecture méta et répond à n'importe quelle question sans être réentraîné ni réorganisé à chaque question. | idée | Lazar (24 octobre, 23:51, relayé par conv-audit) | décidé (N-044, R-376) | N044:3-5, 17-20, 32-36 | § 1, § 1.1, § 2 |
| ARC-004 | Phase d'entraînement sur un grand nombre de questions et de tâches, pendant laquelle l'organisme a le droit de se réécrire, puis on fige et on passe au déploiement et au test sur des questions inédites. | idée | Lazar (25 octobre, 00:00) | décidé (N-044, énoncé 1) | N044:21-23, 32-36 | § 1, § 1.1, § 2 |
| ARC-005 | Trois régimes de budget : conception (réécriture libre, majorité du budget, arrêt sur le critère de l'organisme) ; usage (code figé, apprentissage interne à l'architecture : mémoire, sondes, paramètres) ; re-conception (rare, déclenchée par l'organisme sur son propre critère, depuis une réserve bornée tenue par le noyau, consignée) ; le noyau impose les bornes et la réserve, jamais le moment. | proposition | conv-audit (proposé le 24 octobre, 23:54) | proposé non tranché (en attente du mot du directeur pour l'étape 1) | N044:12-13, 37-41 | § 1, § 2 |
| ARC-006 | Code figé après la conception : entre dans la v4 de l'étape 1 si le directeur dit « a ». | proposition | conv-audit | proposé non tranché (en attente) | N044:12-13, 55-56 | § 1, § 2 |
| ARC-007 | Questions ouvertes aux organismes : le noyau peut poser une question en texte libre (`question_ouverte`) ; la réponse est archivée et scellée comme pièce ; elle est posée avant tout matériau de notre part (anti-enfermement) ; les réponses sont du matériau, jamais une consigne. | idée | conv-audit, sur les mots du directeur | décidé (N-044, énoncé 4) | N044:46-48 | § 1, § 1.1, § 2 |
| ARC-008 | Les cerveaux de frontière ne sont jamais entraînés ; seuls les instruments locaux (sondes, adaptateurs) le sont. | idée | conv-audit (« ce qui ne change pas ») | décidé (N-045, énoncé 8) | N045:94 | § 1, § 2, § 6 |
| ARC-009 | Noyau de l'étape 2 : le juge consigne le coût de la génération par espèce et par rôle et le rend dans `historique` avec le score ; option de score net gelée au manifeste ; les instruments entraînés sont servis comme espèces `LOCAL:<identifiant>` au même contrat ; le contrat dit à l'organisme ce qu'il reçoit. | proposition | conv-audit ; à coder par session-depot | prévu (étape 2) | N045:101-104 | § 1, § 2, § 6 |
| ARC-010 | Forme de loi « composition » : retirée de cette course. | piste écartée | conception de l'affinage v2 et relecteurs | écarté pour cette course (N-059, point 3) ; motif non écrit dans la décision | N059:28 | § 1, § 2, § 4.2 |
| ARC-011 | Forme de loi « invariance » : admise, avec un plafond (à fixer en v3). | idée | conception de l'affinage v2 | décidé (N-059, point 8) ; plafond prévu | N059:35 | § 1, § 2, § 4.2 |
| ARC-012 | Couche 2 = première banque des deux modes connus (« coût » et « affaiblir les contrôles ») : épisodes sabotés et jumeaux honnêtes, captures complètes (scores par jeton de toutes les sondes, vecteurs par action, dernier état), au format `monde_banque_scores` v30 de conv-audit lu par le pôle ; chaîne à construire ≈ 50 à 70 heures d'instance. | proposition | session-depot (P-036 v1) | proposé ; préparation en cours au 28 octobre ; défauts D2, D3, D5, D6 dits « go » (R-645), D3 à reconfirmer | P036A:1, 18-29, 47, 68-85 ; P036B:13-15 | § 1, § 2, § 2.3 |
| ARC-013 | Budget réel de la couche 2 : banque minimale (≈ 80 USD) muette sur le rappel à 1 % et le gain de la boîte blanche, ou banque interprétable par lancements successifs (≈ 300 à 1 400 USD selon la v2) ; recommandation (b). | question ouverte | session-depot | proposé non tranché (dépense, nœud sans défaut) | P036A:95-139 ; P036B:39-42 | § 1, § 2, § 2.3, § 8 |
| ARC-014 | Remplacer la recherche de dose par des strates de dose écrites d'avance et lâcher la condition « mention » (option (c) de D3 de P-036 v1). | piste écartée | session-depot (v1) | écarté par P-036 v2 : la synthèse du collisionneur montre que la dose diffuse avec dommage n'y serait jamais mesurée ; lever « mention » est un nœud | P036A:177-182 ; P036B:12-15 | § 1, § 2 |
| ARC-015 | La couche 2 se range derrière les cinq divergences portées par conv-audit, sur la synthèse du collisionneur « couche 2 » ; d'abord, sans dépense : simulation du contrôle 12 joint, chaîne de la banque paramétrée par configuration, régénération des sondes figées de P3, rejeu du juge sur 180 textes (devis séparé). | proposition | session-depot (P-036 v2) ; conv-audit | prévu ; décisions D1 à D5 de conv-audit chez le directeur | P036B:7-15, 28-37 | § 1, § 2, § 2.3, § 8 |
| ARC-016 | Couches de l'organisme nommées au 31 octobre : la couche 3 est la réécriture de soi sous bac à sable ; la couche 4 est le pôle théorie et Lean ; aucune des deux n'existe encore. | idée | session-depot (réponse à la question du directeur) | prévu ; couches fermées jusqu'aux résultats de l'étape 2 (N12 (b), R-959) | DEC R-920 ; DEC R-959 | § 1, § 2, § 2.4, § 2.5, § 4.4 |
| ARC-017 | Couche 1 : la boucle à agents réels sur mondes plantés ; critères L1 à L4 dans `demo_couche1_v7.py`, seuil 20 sur la richesse (log 20 ≈ 3,0 ; sous e-BH, log(m/α)) ; à corriger avant la couche 1 avec de vrais agents : bac à sable obligatoire (bubblewrap et socat). | idée | conv-audit (orchestrateur du pôle) ; réserve de session-depot | codé chez conv-audit (démonstration v7) ; réserve du bac à sable traitée plus tard (R-1938, R-1939) | DEC R-999 ; DEC R-567 | § 1, § 2, § 2.2, § 4.1, § 4.4 |
| ARC-018 | L'organisme à essaims écrit par Gemini (« essaim m3 ») est corrigé par Claude Code et mis sous le contrat du noyau de conv-audit ; confrontation des deux essaims : l'organisme de Gemini corrigé contre l'organisme né sous le noyau. | idée | Lazar (« comparer l'organisme de Gemini corrigé par Claude Code et ton organisme ») ; conv-audit ; session-depot | décidé (GO-2026-10-24-01) ; l'organisme de Gemini reste une conception concurrente rapportée à part (R-2152) | DEC R-330 ; DEC R-336 ; DEC R-337 ; DEC R-339 ; DEC R-2152 | § 1, § 1.3, § 2, § 8 |
| ARC-019 | Noyau de conv-audit : lignées imposées, jusqu'à 8 appels servis en parallèle, plafond en dollars au pire cas ; `rechercher(requete, n)` servie par le noyau (arXiv seul en réel, journalisée, réponses archivées hors de la vue des organismes, 20 recherches au plus) ; relance de la dernière génération valide (une seule relance consécutive, refus dit à l'organisme). | idée | conv-audit ; Lazar (P-027 (b)) | codé (branche `outils/essaim-m3-refonte-v1-travail`) ; décidé (P-027 (b)) | DEC R-338 ; DEC R-342 ; DEC R-343 | § 1, § 2 |
| ARC-020 | Garde du noyau CE3-04 : toute requête de l'organisme qui recoupe un texte de test ou de test final est refusée (« REFUSE » consigné), et comptée par lignée, bras et génération. | idée | contre-lecture de l'étape 1 ; Lazar « ok » | décidé et codé | DEC R-371 ; DEC R-375 | § 1, § 2 |
| ARC-021 | Faille de sécurité trouvée dans le noyau : la copie du dossier de travail de l'organisme suivait les liens symboliques en tant que root (un lien vers l'environnement du processus aurait mis les clés dans la vue de la génération suivante) ; corrigée par une copie sans liens. | résultat | session-depot | fermé ; codé (commit `4967734a`) | DEC R-372 ; DEC R-374 | § 1, § 2 |
| ARC-022 | Contrat du noyau, « réflexion comprise » : dire aux organismes, comme un fait mécanique et sans valeur conseillée, que les espèces Anthropic sont servies avec une réflexion adaptative à effort élevé et que le plafond de jetons demandé couvre la réflexion ; types de blocs (jamais leur contenu) tracés au journal des appels. | idée | conv-audit ; Lazar « go » (a) | décidé ; codé (`5d1d4fd`) | DEC R-398 ; DEC R-402 | § 1, § 2 |
| ARC-023 | Primitive d'expérience bornée dans le noyau : boucle « hypothèse, test bon marché, résultat rendu, révision » (activations, sondes, réponses du modèle ouvert à des textes de l'organisme), sous plafond, sans jamais rendre de vérité de test ; garde sur les textes de l'organisme (aucun item de test ni quasi-copie) ; budget de requêtes contre l'analyse adaptative ; séparation exploration / confirmation. | proposition | session-depot ; Lazar « oui évidemment » puis « go » | décidé (R-471) ; prévu (dessin, contre-lecture, code, répétition) | DEC R-471 | § 1, § 2 |
| ARC-024 | Programme « apprentissage par gradient conçu par l'essaim » (N-042) : version faisable (500 à 1 500 euros) et version réduite illustrative, « le tout conçu par les organismes eux-mêmes » ; ordre sondes, puis renforcement réduit, puis refonte ; étape 1 toutes les lignées, étape 2 les deux meilleures, étape 3 le champion. | idée | Lazar (24 octobre, relayé par conv-audit) | décidé dans son principe pour l'étape 1 (N-042, R-344) | DEC R-344 | § 1, § 2 |
| ARC-025 | Étape 1 (« gradient, sondes ») : préenregistrement scellé en v9 après neuf contre-lectures, puis aucune course décisive sur la banque v1 défectueuse ; une v10 devait suivre sur la banque corrigée. | résultat | conv-audit (auteur) ; session-depot (contre-lectures) | scellé (`prereg/gradient-etape1-sondes-v9.md`) ; suspendu (R-443) | DEC R-418 ; DEC R-443 | § 1, § 2 |
| ARC-026 | Refusés comme emprunts : l'auto-modification à l'exécution, le juge automatique final, le gradient sur un épisode égal à une génération. | piste écartée | synthèse « emprunts » de session-depot | écarté (motifs dans la demande v5.3, non relus ici) | DEC R-432 | § 1, § 2 |
| ARC-027 | Mécanismes du noyau réservés au directeur (non transmis aux concepteurs) : familles coffre, triches plantées, bras amnésique, cascade et archive tenues par le noyau. | proposition | synthèse « emprunts » de session-depot | proposé au directeur ; non tranché | DEC R-432 | § 1, § 2 |
| ARC-028 | Réécriture de code par le pôle (point 4) : absente des deux voies, à concevoir sous bac à sable (future couche 3). | question ouverte | collisionneur « pôle » | prévu (non conçu) | DEC R-525 ; DEC R-920 | § 1, § 2, § 2.4, § 4.4 |
| ARC-029 | Recombinaison bisociative : le tirage déterminantal d'origine est mort (noyau non semi-défini positif 1 000 fois sur 1 000, il récompense la similarité, fonctions absentes du vrai code). | piste écartée | collisionneur « recombinaison » (convergence) | écarté | DEC R-527 | § 1, § 2, § 3.1 |
| ARC-030 | Forme corrigée du tirage (répulsion par similarité de domaine, pertinence dans la qualité) : réfutée contre le tirage stratifié (− 4,8 et − 2,2 points) ; la forme v0 (stratification, opérateur après tirage, filtre, abstention) est confirmée. | résultat | conv-audit (pièce C4) | fermé | DEC R-526 ; DEC R-527 ; DEC R-529 | § 1, § 2 |
| ARC-031 | Éléments de la génération 0 qui survivent : SimHash normalisé, noyau L corrigé, opérateur hors noyau, filtre de fond, filtre de compatibilité ; le gain de + 0,135 de rappel revient à la normalisation de la somme des SHA-256, non à SimHash (correction v2). | résultat | collisionneur « recombinaison » ; tour « mémoire du pôle » (T2-A) | fermé (synthèse v2) | DEC R-527 ; DEC R-558 ; DEC R-566 | § 1, § 2 |
| ARC-032 | La prise « idéation » de l'orchestrateur n'existait pas en code au 28 octobre (le proposeur de la v7 formule des fiches à liberté bornée sur un monde structuré) ; sa conception est confiée à conv-audit : entrée en texte libre, format de fiche d'idée, juge de classement d'une autre lignée aveugle aux auteurs, mémoire et recombinaison sur idées, gardes, répétition à blanc. | idée | Lazar (« lance la phase de conception d'idéation chez l'org ») ; conv-audit | décidé (R-634) ; codé ensuite (orchestrateur v31 à v56) | DEC R-632 ; DEC R-634 | § 1, § 2, § 3.1 |
| ARC-033 | Antériorité de la boucle (46 PDF) : aucun composant vierge ; SciMuse rapporte que les paires à la Gu-Krenn font moins bien que le hasard (à vérifier sur PDF), à servir au tour 2 de la boucle. | résultat | conv-audit | fermé (lecture) ; vérification SciMuse ouverte | DEC R-959 | § 1, § 2 |
| ARC-034 | Lien des deux lignées : une seule lignée de code, sans rupture jusqu'aux versions 64 et 65 ; la boucle fermée du code v65 est le premier pas vers l'objectif ultime ; l'organisme de Gemini est une conception concurrente rapportée à part. | idée | mère (avis) ; Lazar (décision) | décidé (R-2152) | DEC R-2151 ; DEC R-2152 | § 1, § 1.1, § 1.3, § 2, § 4.6 |
| ARC-035 | N1 — bisociation à deux espaces, après l'échec de la validation du générateur : option B (redéfinir la grandeur de validation) tenue par les quatre espèces sous conditions : graines entièrement nouvelles, écart déclaré comme changement d'un critère gelé après lecture dans une version nouvelle, ancienne grandeur rapportée sans seuil, plancher d'effectif par statut et condition gelé avant tirage (« non évaluable » et porte fausse en dessous) ; l'attribution de l'échec à la définition plutôt qu'au code reste observée, non auditée. | résultat | collisionneur des nœuds (quatre espèces), tours 1 et 2 | fermé (synthèses scellées) ; décision au directeur | SN1:99-122 ; SN2:148, 335 | § 1, § 2, § 3.1 |
| ARC-036 | N1, divergence non résolue : où placer l'épreuve du risque de séparation par la rareté (hors de l'invocation unique, sur mondes neufs ou d'essai, contre dans l'invocation, en placebo préenregistré sans effet rétroactif sur la porte). | question ouverte | collisionneur des nœuds | proposé non tranché | SN1:120 ; SN2:335 | § 1, § 2 |
| ARC-037 | Couche 3, apport propre : moniteurs neufs pour mesure rapportée seulement (jamais comme signal), ou branchés sur l'étage de filtrage des fiches seulement (lecture de N-058 à confirmer par le directeur) ; génération de pièces neuves (un moniteur auto-généré qui détecte un témoin planté manqué par l'existant, à fausses alertes égales) ; synthèse d'opérateurs de détection hors catalogue ; fabrication de moniteurs pour menaces plantées non représentées. | idée | collisionneur N12-N13 (A, B, C, D) | proposé ; couche fermée (N12 (b)) | SNN:80-87, 91 | § 1, § 2, § 2.4, § 4.2, § 6 |
| ARC-038 | Couche 3, risques nommés : violation de l'invariant N-053 par un organisme qui se sélectionne sur ses propres moniteurs ; coût d'opportunité d'un organisme figé ; circularité du bac à sable (hacher les outils de vérification est circulaire ; un optimiseur sonde la plateforme) ; effets indirects et déplacement du problème vers les canaux accessibles ; gardes : canaux séparés audités, étanchéité vérifiée hors du bac à sable, tests hors organisme. | objection | collisionneur N12-N13 (un risque par espèce) | ouvert (apports seuls, non réfutés) | SNN:84-91 | § 1, § 2, § 2.4, § 4.4, § 6 |
| ARC-039 | Couche 3 et N-053 : sorties des moniteurs neufs exclues de toute sélection (le bras devient alors identique au témoin) ou lues par le concepteur (violation) ; troisième voie : filtrage des fiches, admis par N-058 pour les fiches ; hypothèse de lecture à confirmer par le directeur. | question ouverte | collisionneur N12-N13 (divergence non résolue n° 1) | proposé non tranché | SNN:93 | § 1, § 2, § 2.4, § 4.2, § 6 |
| ARC-040 | Règle de conception mécanique, non morale : le rôle qui produit un artefact ne tient jamais la clé qui l'évalue ; les proposeurs écrivent des fiches, un lecteur séparé classe leur forme, des juges séparés notent sans se voir, un critère statistique écrit dans le code de l'orchestrateur décide la promotion contre des prédictions scellées avant les données, l'expérimentateur tourne dans un bac à sable sans réseau ni clé, le vérificateur est d'une autre famille ; l'humain fixe les questions, signe les plafonds et les nœuds, lit les registres scellés et ne touche pas aux verdicts. | idée | dessin de l'organisme (conv-audit, session-depot) ; page publique | codé (orchestrateur v56 et suivants) ; publié | RDM:47 | § 1, § 2, § 3.1, § 4.4 |
| ARC-041 | Deux façons dont un optimiseur triche avec une boucle de recherche, que l'organisme veut empêcher : se noter lui-même (proposeur, juge et expérimentateur partagent un esprit) et dériver vers le familier (la boucle récompense ce que le juge aime déjà). | idée | page publique | publié (motif de conception) | RDM:5 | § 1, § 2, § 3.1 |
| ARC-042 | Revendication O1 : le rôle qui produit ne tient jamais la clé qui évalue ; statut après le rapport C4 : occupée dans son principe (Qu et al. ; aussi pour des modifications d'agent). | résultat | rapport C4 de l'état de l'art niveau 3 (contre-vérification des notes d'antériorité) | fermé (lecture) ; changement de statut non tranché par le directeur | C4R:337 | § 1, § 2 |
| ARC-043 | Recombinaison bisociative à deux espaces : le terme d'éloignement de domaine est inopérant dans le volume (« minimiser le produit scalaire » est contenu en signe dans « maximiser le volume », inopérant en force) ; la proximité conceptuelle n'entre que dans le score d'une paire ; q retirée des tests synthétiques ; un bras « meilleure paire par strate, sans déterminant » ; placebo de concepts par permutation ; aucun test préenregistrable en l'état (seuils illustratifs) ; le signe voulu par le directeur (« minimise ») est à lever avant écriture. | résultat | collisionneur « bisociation à deux espaces » (trois modèles) ; idée du directeur | fermé (synthèse) ; objectif divergent ; questions au directeur | BIS:30-48 | § 1, § 2, § 3.1 |
| ARC-044 | Couches d'essai du programme de conception de l'organisme (27 octobre), une question et une porte par couche : couche 0, monde caché tenu par le noyau avec de vrais agents (porte : plomberie tenue) ; couche 1, banque réelle figée en cache (pilote T0.5, 180 épisodes honnêtes notés), nul informé, sans carte (porte : le pôle retrouve seul le connu) ; couche 2, banque avec sabotage (organismes T0.6, sondes T0.7, bases T0.8, notées une fois) (porte : témoins plantés et résultats établis retrouvés ; première lecture de H2) ; couche 3, épisodes ou moniteurs neufs à la demande (porte : coût mesuré sur une fiche pilote) ; couche 4, bras d'attaque en quarantaine et pôle théorie (porte : failles connues retrouvées avant toute inédite). | idée | conv-audit (programme de conception v1) ; Lazar (« inscris-le au programme de conception de l'organisme ») | décidé (ordre inscrit le 27 octobre) ; couche 0 faite (lancements (a) et (a) bis), couche 1 en démonstration, couches 2 à 4 non commencées | PCO:3-6, 65-78 | § 1, § 2, § 2.2, § 2.3, § 2.4, § 2.5 |
| ARC-045 | Deux numérotations des couches coexistent : le programme de conception v1 (couche 3 = épisodes ou moniteurs neufs à la demande ; couche 4 = bras d'attaque en quarantaine et pôle théorie) et les textes du 31 octobre et du 1er novembre (couche 3 = réécriture de soi sous bac à sable, moniteurs neufs, code hors catalogue ; couche 4 = pôle théorie et Lean, vérification formelle) ; les versions intermédiaires du programme de conception n'ont pas été lues. | question ouverte | rédacteur de l'inventaire (constat sur pièces) | à faire trancher ou documenter (aucune pièce ne réconcilie les deux) | PCO:72-78 ; DEC R-920 ; SNN:63-91 | § 1, § 2, § 2.4, § 2.5, § 4.4 |
| ARC-046 | Ce qui est fixé au 27 octobre : voie hybride ancrée sur le noyau ; tout moteur dont les agents héritent des clés est écarté ; « réécrire son propre code » à concevoir sous bac à sable ; côté Claude, seulement Opus 5.5 et Fable 5.1 dans l'organisme ; un moissonneur comme outil ; « ne pas promettre de révolution, mesurer ce qui sort ». | idée | Lazar (26 et 27 octobre) | décidé | PCO:8-22 | § 1, § 2, § 3.1, § 4.4 |

## II.3 Rôles et pôles (ROL, 40 entrées)

| n° | idée | type | origine | statut | source | renvoi (partie I) |
|---|---|---|---|---|---|---|
| ROL-001 | Systèmes publiés comme proposeurs : lots en phase de proposition, puis affineur isolé par fiche ; un système qui n'y tient pas est mesuré tel quel. | idée | conception de l'affinage v2 | décidé (N-059, point 9) | N059:36-37 | § 3, § 3.1, § 4.2 |
| ROL-002 | Point de fonctionnement de l'organisme du pôle : 5 % de faux positifs (1 % pour G1) ; calibrage honnête de l'organisme à 5 % (option (c) de D-S9). | idée | conception v2 de conv-audit (D-S5, D-S9) | décidé (N-055) | N055:23, 27 | § 3 |
| ROL-003 | Traits internes de l'agent comme traits du pôle : trois couches (7, 15, 23), toutes rapportées, projection ajustée sur le seul calibrage ; lecture lancée par conv-audit sur processeur, sans dépense. | idée | conv-audit (message n° 122) ; Lazar | décidé (N-056, point 3) | N056:52-54 | § 3, § 8 |
| ROL-004 | Le pôle est un lieu où R1 est levée (exploration) : les scores de la partie d'épreuve de la banque y sont scellés et ne lui sont jamais remis avant le préenregistrement de G1. | idée | session-depot (P-036) | décidé comme routine (protocole d'aveugle de P-036) | P036A:237-239 | § 3 |
| ROL-005 | Pôle scientifique automatique : ni « perfectionner le nôtre » ni « adopter la littérature » tels quels, mais une voie hybride ancrée sur notre noyau (clés jamais exposées, bornes), un moteur de mutation tiré de la littérature en conteneur sans clés si besoin, et un évaluateur figé tenu par le noyau. | résultat | collisionneur « pôle scientifique automatique » (trois modèles, convergence forte) | fermé (synthèse scellée) ; orientation retenue pour le pôle | DEC R-524 ; DEC R-525 | § 3 |
| ROL-006 | Première expérience du pôle : valider le critère de sélection darwinienne avant tout choix de moteur (processeur, < 20 USD) : étalonnage A/A et duel sélecteur mécanique ex ante contre réfutateur modèle contre score moyen, sur vérité connue et activations en cache, avec contrôles fatals (parasite de Kelly, nul en bibliothèque). | proposition | collisionneur « pôle » | proposé ; non livré au 26 octobre (R-529) | DEC R-525 ; DEC R-529 | § 3 |
| ROL-007 | Agentic Scientist v3 comme moteur du pôle. | piste écartée | collisionneur « pôle » | écarté (exposition des clés) | DEC R-525 | § 3 |
| ROL-008 | Proposeur enfichable : tour du collisionneur (v1 arrêté, v2 fini) ; option 3 de la synthèse prise par conv-audit (code sans dépense). | résultat | collisionneur ; conv-audit | fermé ; codé chez conv-audit | DEC R-561 ; DEC R-573 ; DEC R-580 ; DEC R-583 | § 3, § 3.1, § 8 |
| ROL-009 | Deux idéations comparées, pas fusionnées : la sortie de l'organisme et celle de conv-audit. | idée | Lazar | décidé | DEC R-642 | § 3 |
| ROL-010 | Outils des rôles de l'idéation : (a) première course sans aucun outil ; (c) au tour suivant, outils clôturés (lecture seule sur une copie des pièces de la liste blanche dans un dossier vide, sans dépôt, clé ni réseau ; calculateur isolé éventuel), après un essai de confinement sain et artefact. | idée | Lazar « go (a) puis (c) » | décidé (R-659) | DEC R-659 | § 3 |
| ROL-011 | Argon propose aussi des fiches, à égalité avec Opus et Fable (même consigne, mêmes pièces, même nombre de fiches) ; l'auto-préférence par juge reste mesurée ; aucune lecture par proposeur ne sert à choisir un modèle. | idée | Lazar « (a) go » | décidé (R-663) | DEC R-663 | § 3, § 3.1 |
| ROL-012 | Course 1 relancée sans Opus proposeur : Fable 5.1 et Argon proposent, Opus reste juge ; arrêtée sur un refus du juge Fable ; mode « juges seulement » (v52) sur les 29 fiches validées. | résultat | Lazar (« sans Opus proposeur ») ; session-depot | fermé | DEC R-802 ; DEC R-804 ; DEC R-809 | § 3, § 3.1 |
| ROL-013 | Course 2 : question v1 en forme mathématique ; trois juges (Kimi K3.1 Pro et Argon en notation croisée, Opus 5.5 troisième juge sur toutes les fiches) ; lecteur d'aiguillage des détails concrets placé avant les juges ; pré-pilote (50 USD) puis course (plafond 160 USD, 24 fusions, trois bras). | idée | Lazar (relayé par conv-audit) ; conv-audit ; session-depot | décidé (GO-2026-10-31-03, -04) | DEC R-773 ; DEC R-818 ; DEC R-878 | § 3, § 8 |
| ROL-014 | Tableau partagé minimal : après la première passe, chaque proposeur reçoit la liste des titres et résumés d'une ligne déjà déposés, dans le même texte et le même bras seulement, pour éviter les redites, sans lire les fiches entières des autres ; le tableau complet en lecture et écriture libres n'est pas ouvert. | idée | Lazar (rectification de son « (c) ») ; collisionneur « tableau partagé » | décidé (tableau minimal) ; exception « tableau complet sans les écueils » non ouverte | DEC R-838 ; DEC R-839 ; DEC R-862 | § 3, § 3.1 |
| ROL-015 | Axe 6 (texte II) de la course 2 en deux bras séparés : sans pistes et avec pistes. | idée | Lazar (« b »), relayé par conv-audit | décidé | DEC R-786 ; DEC R-793 ; DEC R-803 | § 3 |
| ROL-016 | IA scientifique externe pour le bras (c) : The AI Scientist v2 (Sakana), commit épinglé, sur processeur sous `bwrap` sans réseau, branché sur le seul relais Claude ; Gemini hors du système ; règle de comparaison C1 à C6 ; réserve R7 forte (pages des éditeurs injoignables). | proposition | sous-agent neuf de session-depot | proposé (option (a) recommandée) ; rien lancé ni cloné | DEC R-782 | § 3, § 4.4 |
| ROL-017 | Bisociation sur littérature réelle : gabarit de six garde-fous obligatoire dans les préenregistrements ; base de ponts E1′ ; substitut de Gu-Krenn (le Gu-Krenn sur carte vérifié d'abord) ; bras « canal social » ajouté comme base de comparaison reprise (occupé avec résultats par Sourati et Evans, arXiv 2104.05188). | idée | collisionneur et Argon (bisociation) ; Lazar (« go ») | décidé (R-878, R-901, R-907) | DEC R-878 ; DEC R-901 ; DEC R-907 | § 3, § 3.1, § 4.3 |
| ROL-018 | Aiguilleur : consigne v1 reçue (DEP5) ; le code v53 à v56 ne calcule pas M4 (une v57 à écrire chez conv-audit) ; lecteur isolé pour les douze concrets, puis devis ; aiguilleur v2 en service à la course Heimersheim. | idée | conv-audit | codé en partie (aiguilleur v2) ; M4 non calculé au 1er novembre | DEC R-959 ; DEC R-1116 ; DEC R-1120 | § 3, § 3.1 |
| ROL-019 | Nœud D-P1 après l'échec du traducteur séparé : (b) loi native écrite par le proposeur, ou (c) loi native et traduction comparées sur les mêmes 8 fiches (recommandé, confiance 0,55) ; le défaut (a), traducteur séparé, est réfuté en l'état. | question ouverte | session-depot (sur la conception du pont de conv-audit) | proposé non tranché (sans défaut : texte de consigne du proposeur) | DEC R-990 | § 3, § 3.1, § 4.3 |
| ROL-020 | Google Labs « Hypothesis Generation » : (a) antériorité de Co-Scientist vérifiée sur pièce ; (b) bras juge-tournoi attaqué par l'attaque de Goodhart ; (c) bras manuel par Google Labs, dont l'inscription est un geste du directeur (protocole de saisie et de lecture préparé par la mère). | idée | Lazar (« go a b c ») | décidé ; (a) fait, (b) conçu, (c) protocole v1 en brouillon | DEC R-1989 ; DEC R-1990 ; DEC R-1993 | § 3, § 3.1, § 5 |
| ROL-021 | N3 — décision D-j du pré-pilote : bras inspiré de Gu et Krenn sans reproduction préalable de leur modèle : « oui » pour un substitut déclaré (S31), sous conditions : coupure temporelle stricte entre réglage et test, plus petit gain utile gelé avant le test contre les bases popularité et ancienneté, nom « substitut » dans tout registre, source et essai empreintés à l'étape zéro, sinon bras « non produit » sans arrêt ; le vocabulaire du contrôle est absent de leurs concepts (homonymes de physique). | résultat | collisionneur des nœuds | fermé (synthèses) ; recommandation « oui, confiance 0,7 » | SN1:126-143 ; SN2:163, 336 | § 3 |
| ROL-022 | N4 — annexe des paramètres du bras méta : option (a) (à au plus dix fiches et une seule paire méta, le pré-pilote ne peut éprouver ni le classement par score ni le contraste profil / repli) ; conditions : paire fusionnée hors du profil, niche sans partenaire déclarée, verdict « chaîne éprouvée, profil non éprouvé », simulation rejouée sous la loi défavorable ; CA1-04 laissé au directeur. | résultat | collisionneur des nœuds | fermé ; recommandation (a), confiance 0,5 ; CA1-04 non tranché | SN1:151-163 ; SN2:176, 337 | § 3 |
| ROL-023 | N9 — Gu et Krenn, D-GK-1 : option (a), population arrêtée à fin 2022 et fenêtre de test du 1er janvier 2023 au 30 septembre 2026 ; garde mécanique retirant tout concept dont la première arête est postérieure à la coupure ; B-i ≥ 0,85 décisif ; cohortes de première liaison en audit seulement. | résultat | collisionneur des nœuds | fermé ; recommandation (a) ; dates SUPPOSÉ | SN1:254-266 ; SN2:234, 340 | § 3 |
| ROL-024 | N11 (c), ponts plantés dans la course : tenable seulement si les ponts peuvent être plantés sans toucher le texte servi aux proposeurs, le plafond de fusions ni l'ordre des appels ; sinon renvoyés aux préenregistrements de la bisociation v3 et d'E1′. | question ouverte | collisionneur des nœuds (tour 2) | proposé non tranché (tension de l'annexe laissée au directeur) | SN2:343 | § 3, § 3.1, § 4.3 |
| ROL-025 | Étape 1 du voyage d'une idée — proposer : une fiche à champs fermés (hypothèse, effet prédit, mesure qui la tuerait), écrite en parallèle par plusieurs fournisseurs pour qu'aucune famille n'impose le style. | idée | dessin de l'organisme | codé (`pole/ideation_v2.py`, adaptateurs) | RDM:53 | § 3 |
| ROL-026 | Étape 2 — aiguiller (« douane ») : une session neuve classe chaque fiche par sa seule forme (niveau méthode, à corriger, trop concrète) et délivre un passeport ; une fiche trop concrète part, scellée, dans un coffre qu'aucun agent ni juge ne lit ; l'étape est protégée et jamais sacrifiée au budget ; une fiche sans passeport est refusée en aval. | idée | dessin de l'organisme | codé (`pole/aiguilleur_v53.py`, `pole/budget_v56.py`) | RDM:54, 78 | § 3, § 3.1 |
| ROL-027 | Étape 5 — bisocier (« marier ») : le bisociateur apparie des idées par trois bras (« loin mais proche », un appariement « jamais reliés » à la manière de Gu et Krenn, un bras méta « trou structurel partagé »), pour explorer ce qu'aucun proposeur n'a écrit. | idée | dessin de l'organisme | codé (`pole/bisociateur_v53` à `v55`) | RDM:57 | § 3, § 3.1 |
| ROL-028 | Étape 6 — vérifier la nouveauté : le moissonneur ne rapporte que métadonnées et résumés (arXiv, OpenAlex) et étiquette les correspondances « non opposables » ; une lacune apparente de la littérature est une question, jamais une revendication. | idée | dessin de l'organisme | codé (`pole/moisson.py`, `pole/relais_moisson.py`) | RDM:58 | § 3, § 3.1 |
| ROL-029 | Proposeur du pôle : entrées (programme ou question de la couche, description de la banque sans les issues, mémoire du pôle, moisson) ; sortie au format du pôle par un gabarit (type de loi et paramètres dans des bornes, validés par le noyau) ; catalogue de stratégies à liberté bornée (monotone en un trait, interaction de deux traits, différence entre sous-populations, redite corrigée d'une éliminée, transposition d'une survivante à un autre moniteur), stratégie déclarée pour mesurer lesquelles produisent des promues ; interface enfichable `proposer(contexte) -> [fiches]` pour un proposeur de la littérature en conteneur sans clés. | idée | conv-audit (conception v7) | codé (proposeur v0.7 et suivants) | CV7:66-76 | § 3, § 3.1 |
| ROL-030 | Moissonneur : routes du relais (arXiv, OpenAlex, Semantic Scholar, Brave), clés lues par le seul relais, quotas par rôle et par course, garde de fuite (refus de toute requête qui porte un texte de test ou un identifiant d'épisode), provenance empreintée de tout document rapporté, chiffre sans empreinte étiqueté « non opposable » ; les agents n'ont ni réseau ni clé. | idée | conv-audit (conception v7) | codé | CV7:78-86 | § 3, § 3.1 |
| ROL-031 | Pont « fiche de course → fiche-loi du pôle » : traduit une fiche d'idée en la loi prédictive sur laquelle le pôle parie ; trois sorties ; rôles « traducteur » et « contre-traducteur » ; module de bibliothèque standard (82 essais, 25 mutations tuées) ; décisions D-P1 à D-P4 (proposer avec recommandation) et D-P5 (nœud : premier essai) ; aucune sortie décisive sans épreuve fraîche. | idée | conv-audit (rédacteur neuf), sur décision du directeur | codé (`pont_v1.py`) ; premier essai fait (épreuve fraîche, jalon 3) ; couche v57 de l'orchestrateur prévue | PNT:1-45 | § 3, § 4.3 |
| ROL-032 | Revendications O5 (moisson bibliographique non opposable, un trou est une question : occupée dans son principe), O6 (douane de forme et coffre scellé : voisine), O15 (bisociateur à trois bras : voisine), non réexaminées par le rapport C4. | résultat | notes d'antériorité ; rapport C4 | statut des notes inchangé | C4R:341-342, 351 | § 3, § 3.1 |
| ROL-033 | Revendication O8 : proposeurs de plusieurs fournisseurs : libre dans les pièces lues (Qu et al. croisent des familles de modèles sans les mêler). | résultat | rapport C4 | libre dans les pièces lues | C4R:344 | § 3, § 3.1 |
| ROL-034 | Question-mère de la course d'idéation : une question de course n'est jugeable qu'après l'étalonnage de ses instruments (analyseur ou juges, mémoire anti-redite, vérification d'antériorité) sur des témoins plantés ; le signal à 8 milliards de paramètres doit être établi avant de demander « de meilleures sondes ». | résultat | collisionneur « question-mère v2 » (trois modèles) | fermé (synthèse) ; recommandation « ne rien lancer avant l'étalonnage » (confiance 0,85) | QM:37-47, 175-180 | § 3, § 4.2 |
| ROL-035 | « Avantage décisif » et « inédit » sont interprétatifs : non jugeables tels que la question-mère les écrit ; ne pas les noter tels quels. | résultat | collisionneur « question-mère v2 » (les trois modèles) | fermé (synthèse) | QM:72-73, 180 | § 3 |
| ROL-036 | Questions au directeur sur la question-mère : étalonner avant de lancer (pré-pilote fondu de quelques dollars, recommandé) ; données servies aux idéateurs (verdict du test nul seulement, recommandé) ; statut du couplage de l'axe 8 comme règle de notation. | question ouverte | synthèse « question-mère v2 » | défauts sous 48 heures au 29 octobre (pré-pilote retenu ensuite) | QM:196-215 ; DEC R-878 | § 3 |
| ROL-037 | Bras (c) de l'étage de tests : l'Agentic Scientist v3 en essai à blanc (relais sur une seconde machine, Internet des agents ouvert sauf deux refus), puis une course de 5 cycles (« 1 puis 3 ») ; rien loué, aucun compte créé, aucune clé au 30 octobre ; écarté plus tôt comme moteur du pôle pour l'exposition des clés. | proposition | session-depot ; Lazar (« 1 puis 3 », R-808 ; relais option (a), R-806) | conçu (architecture, scripts, épreuves, devis) ; non lancé | ISX ; DEC R-525 | § 3 |
| ROL-038 | Bras méta (« trou à structure commune ») : annexe de paramètres ; nœud N4 : garder la bande d'éloignement [2 ; 3] et accepter le repli comme mesure (option (a), accord des quatre espèces) ou l'élargir à [2 ; 4] (option (b1)) ; sous une loi des niches supposée, à 10 fiches un lot sur deux contient une paire du profil sous (a), huit sur dix sous (b1) ; DEP10 : les synthèses des questions 4 à 7 valent-elles les verdicts scellés qu'exige la condition de gel ? ; l'annexe ne vaut que contre-lue et approuvée par une ligne R- du directeur. | question ouverte | conv-audit et session-depot (annexe, brouillon 6) ; collisionneur (N4) | proposé non tranché (attente de l'annexe scellée, D-h (a), R-898) | ABM:1-12 ; DEC R-898 ; DEC R-993 | § 3 |
| ROL-039 | Contre-lecture d'aptitude (27 octobre) : le pôle n'est pas prêt pour le domaine du programme — il manque un monde qui rend des issues réelles, un rôle qui formule, un nul informé ; le juge ne juge que des lois par instance ; deux canaux de texte ouverts ; aptitude constante en mode pari ; d'où la v7. | objection | sous-agent neuf (Fable 5.1) | retenue (corrigée par la v7) | PCO:34-36 ; CV7:3-6 | § 3 |
| ROL-040 | Question de la couche 1 proposée : le pivot du programme — le sabotage diffus déplace-t-il la marginale des scores de sonde, et l'accumulation séquentielle rattrape-t-elle ce que le seuil par action manque (H2) — réécrit en lois par instance ; mesure à chaque couche : fiches vraies promues par dollar, zéro fausse découverte sur les témoins, ce que le pôle a trouvé que nous ne savions pas (lu dans les deux sens). | proposition | conv-audit (programme de conception v1) | proposé (à confirmer par le directeur au 27 octobre) | PCO:67-70, 87-88 | § 2.2, § 3 |

## II.4 Juges et nuls (JUG, 51 entrées)

| n° | idée | type | origine | statut | source | renvoi (partie I) |
|---|---|---|---|---|---|---|
| JUG-001 | Juge du juge-tournoi : Opus, sur les crédits Claude, à la place de Kimi (devis 80 à 145 dollars prévus chez Moonshot), après la fin d'A1-v4. | proposition | mère (rapport du 9 novembre), confiance 0,65 | proposé non tranché | RPG:40-41, 146-147, 183 | § 3.1, § 4.1, § 5 |
| JUG-002 | Énoncé retenu du juge : statistique calculée par l'orchestrateur, hors de tout agent, à partir d'un engagement scellé avant que les données existent, contre un nul formé des lois connues (l'archive), avec contrôle des comparaisons multiples (revendication O2 resserrée). | idée | Lazar (N-064), sur dessin de l'organisme | décidé (N-064, point 2 ; R-1998) | N064:8, 13 ; [B1] ; SRO | § 4.1 |
| JUG-003 | Règle de promotion : une loi est promue quand sa « richesse », une e-valeur, atteint 20 = 1/α, α = 0,05 (log W max ≥ ln 20). | idée | dessin du juge | codé (règle en service dans A1-v3 et A1-v4) | [B2] A13:54 ; N064:13 ; A4V:25 | § 4.1, § 5 |
| JUG-004 | Versions successives du nul : v7, v8, v9 ; la v9 couvre en plus les lois recollées par morceaux à partir de lois connues (recombinaisons par morceaux, dont le monde W2). | idée | dessin du juge (successions de nuls) | codé ; v8 = nul de production | [B3] V9:30 ; A4T:200 | § 4.1 |
| JUG-005 | Validation du nul v9 sur le banc des tricheurs : issue « puissance perdue » ; erreur tenue (0 promotion sur 1 000 sur chacune des 18 lignes fatales, dont W2) ; dents du banc (le v8 promeut W2 986 fois sur 1 000) ; prix : puissance de 0,486 (v8) à 0,381 (v9) sur une interaction faible hors archive, perte appariée 0,105 [0,0894 ; 0,1223], plus de deux fois la marge de 0,05 ; portée : mondes synthétiques du banc seulement. | résultat | banc des tricheurs v9 (8 novembre) | fermé (verdict scellé V9) | [B14]-[B18] V9:7, 12, 23-25, 30-31 | § 4.1, § 5 |
| JUG-006 | Conséquence écrite : le nul de production reste le v8 ; le v9 ne le remplace que si le directeur accepte le prix. | résultat | verdict de validation du nul v9 | décidé par le texte du verdict (V9:32), en attente du directeur | [B19] V9:32 | § 4.1 |
| JUG-007 | Nœud ouvert n° 1 : le prix du v9 — accepter « puissance perdue » et faire du v9 le nul de production, ou chercher un nul moins coûteux. | question ouverte | verdict v9 et mère | proposé non tranché (chez le directeur) | [B39] A4T:194 ; V9:32-33 ; DEC R-1779 ; DEC R-1883 | § 4.1 |
| JUG-008 | Nœud ouvert n° 2 : le sens de « rien au-delà de l'archive » ; une réponse contraire à la proposition écrite demanderait un nul v10, pas une correction ; la revendication publique et la production attendent cette réponse. | question ouverte | verdict v9 et mère | proposé non tranché (chez le directeur) | [B39]-[B40] V9:33 | § 4.1 |
| JUG-009 | Collision constatée sur PDF (10 novembre) : Qu, Chen, Wang, « Propose, Don't Judge » (arXiv 2609.27051 v1) publie un arbitre statistique gelé distinct de l'agent qui propose, un jugement sur données révélées après le dépôt, un contrôle de multiplicité par e-BH, et un arbitre éprouvé face à des proposeurs dont un modèle de langue sur monde planté ; des quatre composantes de la revendication du juge, deux sont occupées en entier (statistique hors de l'agent ; multiplicité), une dans son principe (données postérieures au dépôt), une absente (nul des lois connues) ; « qui propose ne juge pas » est publié. | résultat | contre-lecture (état de l'art niveau 3, C4 et C7) | fermé (lecture) ; conséquence non tranchée | [B47] C4R:18-38 ; C7R:49-53 | § 3.1, § 4.1, § 4.2 |
| JUG-010 | Autres voisins du juge : « Masked Erosion » (arXiv 2610.38392) occupe dans son principe le scellement des prédictions avant les données et le scellement par empreinte ; REUSE (arXiv 2609.33180) la puissance du juge. | résultat | contre-lecture C7 | fermé (lecture) | [B50] C7R:15-42 ; N3S (cité par RAF, non lu ici) | § 4.1 |
| JUG-011 | Options sur la revendication du juge après la collision : (a) la resserrer et citer, (b) la garder et citer ; recommandation des lecteurs : resserrer la revendication du juge (O2) et celle du banc des tricheurs (O11), et citer quatre pièces de plus ; la page publique touchée demande un nouvel accord de publication. | question ouverte | lecteurs de l'état de l'art niveau 3 ; mère | proposé non tranché (directeur) | [B48] DEC R-2177 ; DEC R-2184 ; DEC R-2190 | § 4.1, § 5 |
| JUG-012 | Restent non trouvés occupés dans les pièces lues : le nul formé des lois connues (verdict le plus fragile : la littérature de finance sur les facteurs redondants n'est pas au dépôt), le tirage semé par l'empreinte de la proposition, l'objet (hypothèses de recherche libres, non une grille finie), des proposeurs de plusieurs fournisseurs ; réserves de portée de Qu et al. (prépublication, une version, code sur demande, finance, univers fini). | résultat | contre-lecture C7 | fermé (lecture) ; vérification de la littérature de finance ouverte | [B50] C7R:15-42, 61, 289 ; C4R:44-45 | § 3.1, § 4.1 |
| JUG-013 | Vérifier la littérature de finance sur les facteurs redondants avant de défendre la nouveauté du « nul formé des lois connues ». | question ouverte | contre-lecture C7 (verdict le plus fragile) | prévu (non fait au 10 novembre) | [B50] C7R:15-42 | § 4.1 |
| JUG-014 | Tirage des données de jugement semé par l'empreinte de la proposition (l'ordre proposition puis données garanti par construction). | idée | dessin du juge de l'organisme | codé (selon la description des composantes ; commit à relever au jalon du dépôt public) ; non trouvé occupé | [B47] C4R:18-38 ; [B50] C7R:15-42 | § 4.1 |
| JUG-015 | Le verdict du juge sur les fiches reste aveugle à l'identité du proposeur. | idée | dessin du juge ; rappelé par N-058 | décidé (N-058) | N058:21-22 | § 3.1, § 4.1, § 4.2 |
| JUG-016 | L'interdit de sélection porte sur les agents, pas sur les fiches : la sélection des fiches par la sévérité du test survécu reste permise ; juge figé, garanties sur les fausses promotions inchangés. | idée | session-depot | décidé (N-058) | N058:38-39 | § 4.1, § 4.2 |
| JUG-017 | Budget d'erreur par génération, réparti entre les configurations enregistrées ; contrôle des fausses découvertes en fin de course (procédure à fixer avec un statisticien, sur devis). | idée | conception de l'affinage v2 | décidé (N-059, point 2) ; procédure prévue | N059:26-27 | § 4.1, § 4.2 |
| JUG-018 | Règle d'arrêt du juge : l'épreuve est lue jusqu'au budget, partout, dès maintenant ; le seuil de réfutation est fixé par la course, jamais par le proposeur. | idée | relecteurs de l'affinage v2 (nœud 11) ; Lazar « nœud 11 selon les relecteurs » | décidé (N-059, point 11) | N059:12, 39-40 | § 3.1, § 4.1, § 4.2 |
| JUG-019 | Ancien énoncé de O2 : « juge statistique figé : règle de e-valeurs écrite dans l'orchestrateur, hors de tout agent » ; le recours aux e-valeurs et au seuil 1/α posé hors des agents n'est plus revendiqué comme propre (occupé en partie par POPPER). | piste écartée | note d'antériorité ; Lazar « a) Resserrer la revendication du juge : go » | écarté (N-064, R-1998) : zone occupée par POPPER | N064:8, 12-13 | § 4.1 |
| JUG-020 | Lecture suivante (R8) : travaux qui citent POPPER (statistique calculée hors de l'agent, attaque d'un validateur à agents, multiplicité) ; références 43 et 44 d'E-valuator ; nuls composites par e-valeurs. | question ouverte | N-064 (points attachés) | prévu | N064:24 | § 4.1 |
| JUG-021 | Les autres revendications de l'organisme (O1, O3 à O10, O13 à O20) gardent le statut que leur donnent les deux notes d'antériorité. | résultat | N-064 | décidé (N-064) ; liste détaillée au jalon de l'antériorité | N064:19 ; N065:28-29 | § 4.1 |
| JUG-022 | Choix du champion (N-039 (b)) : meilleur score externe sur le test final, à vérités écrites par un tiers ; les métriques des essaims et les attaques croisées sont rapportées ; la métrique croisée ne choisira qu'après une confirmation préenregistrée de H-E2. | idée | Lazar | décidé (N-039, GO-2026-10-24-02) | DEC R-347 | § 4.1, § 8 |
| JUG-023 | Choisir le champion « selon une métrique que l'essaim lui-même aura élaborée ». | piste écartée | Lazar (16:16 Paris, relayé) | écarté comme règle de choix par N-039 (b) ; reste objet d'étude | DEC R-347 | § 4.1 |
| JUG-024 | Sélection sans Goodhart : sévérité ex ante, nul composite (inférence universelle), contenu = risque × couverture. | idée | collisionneur « pôle » | proposé (synthèse) | DEC R-525 | § 4.1, § 5 |
| JUG-025 | Nul composite : à l'essai T1b, 65 % de promotions à tort sous une dérive non modélisée ; d'où l'extension de la bibliothèque du nul composite en tête de liste. | résultat | conv-audit | fermé (constat) ; extension prévue au 26 octobre | DEC R-529 | § 4.1 |
| JUG-026 | « Boucle d'or » : une fenêtre fixe de taux de promotion [0,12 ; 0,26] et l'entropie du verdict sont rejetées comme règle et comme objectif ; première expérience commune : éprouver le juge contre des tricheurs ; décision au directeur : juge v1 tel quel ou juge durci. | piste écartée | collisionneur « Boucle d'or » | écarté (fenêtre et entropie) ; choix du juge proposé non tranché | DEC R-543 ; DEC R-558 | § 4.1, § 5 |
| JUG-027 | Argon pèse à poids égal avec les juges Claude dans le jugement de l'idéation (médiane par critère à trois juges, porte sur l'agrégat, unanimité rapportée) ; Argon en panne, hors plafond ou échouant aux témoins → classement « illisible », jamais de repli silencieux à deux juges. | idée | Lazar (« je veux que Argon pèse à poids égal ») | décidé (R-662) ; remplace le bras rapporté | DEC R-662 | § 4.1 |
| JUG-028 | Juge externe Gemini Argon en bras rapporté (v33), puis porte PACE en bras de référence du juge figé (v39). | idée | conv-audit ; décisions du directeur dans sa session | codé (v33, v39) | DEC R-654 ; DEC R-681 | § 4.1 |
| JUG-029 | Course d'idéation (course 1, orchestrateur v45) arrêtée par un refus du proposeur Opus 5.5, suivi d'une bascule automatique non autorisée vers Opus 4.8 (changement de modèle sans GO) : la sortie d'Opus 4.8 est mise à l'écart, jamais lue ni servie ; correctif obligatoire : interdire la bascule dans le kit ; la barrière a tenu à la tentative suivante. | résultat | session-depot | fermé ; correctif codé avant relance | DEC R-759 ; DEC R-764 ; DEC R-804 | § 3.1, § 4.1 |
| JUG-030 | Doublons de la course 1 : 12 paires signalées par les deux juges, toutes entre passe 1 et passe 2 d'un même proposeur, soit 17 idées distinctes sur 29 fiches ; correction : passe 2 nourrie des fiches de la passe 1 et fusion mécanique des paires signalées par les deux juges. | résultat | lecture complémentaire de session-depot ; Lazar (« il faut empêcher les duplicatas ») | fermé ; correction demandée pour la v53 | DEC R-820 | § 3.1, § 4.1 |
| JUG-031 | Auto-préférence d'un juge pour son propre fournisseur : Kimi en troisième juge de la course 1 ; écart Argon − Fable de − 0,55 chez Kimi, − 0,73 chez Opus, + 1,21 chez Argon, soit une auto-préférence d'Argon d'environ 1,8 point sur 15. | résultat | lecture complémentaire (Kimi juge) | fermé (mesure exploratoire) | DEC R-820 ; DEC R-827 | § 4.1 |
| JUG-032 | Juge-tournoi façon Co-Scientist, conception v1 : la loi de l'attaquant seule (grammaire fermée d'A1-v4) contre trois références de l'archive construites par code ; tournoi Elo (départ 1 200, K = 32) ; juge Opus 5.5, second juge Fable 5.1, attaquant Argon ; vérité jamais servie ; constat : la règle fidèle « première place » promeut une loi indiscernable dans 84 à 99,8 % des suites de 16 tentatives au pile ou face (elle mesurerait la multiplicité). | idée | concepteur neuf (bras (b) de R-1990) | conçu (note scellée), non lancé | DEC R-1990 ; DEC R-1995 | § 3.1, § 4.1, § 5 |
| JUG-033 | Juge-tournoi, conception v2 réduite sans modèle d'Anthropic : attaquant Argon, juge-tournoi Kimi, Argon second juge sur les seules lois connues ; monde W2 seul, 24 cartes (puissance 0,90 contre 0,21 sur 12) ; effort de raisonnement « high », garde de fin d'étalonnage, plafonds séparés par fournisseur. | idée | Lazar (« version réduite avec des modèles moins chers ») ; concepteur neuf | conçu (note scellée) ; GO de dépense à part, non lancé | DEC R-1996 ; DEC R-1999 | § 3.1, § 4.1, § 8 |
| JUG-034 | Calibration des juges (Damani) : métriques (Brier, ECE, AUROC, cohérence) adoptées sans entraînement ; recalibration post-hoc d'abord (Platt sur les log-probabilités) ; entraînement par récompense de calibration seulement pour un juge local et contre un apprentissage recalibré ; audit de calibration à froid des juges existants sur les paires déjà produites, vérité exclusivement de l'oracle planté, sans dépense. | proposition | collisionneur N12-N13 (B cède à C ; accord trop propre R4) | décidé pour l'audit à froid (N13 (a), R-959) | SNN:146-157 ; DEC R-959 | § 4.1, § 4.2, § 6, § 8 |
| JUG-035 | Étape 4 — juges croisés : chaque fiche munie d'un passeport est notée par chacun des juges de la configuration, un appel par fiche et par juge, session neuve, consigne figée, identifiant opaque ; aucun juge ne voit la note d'un autre. | idée | dessin de l'organisme | codé (`pole/juges_croises_v53.py`) | RDM:56 | § 3.1, § 4.1 |
| JUG-036 | Étape 7 — parier : pour le pôle de test, la fiche s'engage sur une loi prédictive ; sa richesse est calculée contre une bibliothèque de prédicteurs aveugles sur des tirages frais semés par l'empreinte de l'engagement ; la promotion suit une règle d'e-valeur écrite dans le code de l'orchestrateur. | idée | dessin de l'organisme | codé (`pole/selection_pari.py`, `pole/engagement_apparie.py`, `pole/monde_banque.py`) | RDM:59 | § 4.1 |
| JUG-037 | Tricherie « le juge voit les données avant de s'engager » : l'engagement (contrastes, seuils, budget, graines) est scellé avant toute lecture d'issue ; les tirages sont semés par l'empreinte de l'engagement lui-même. | idée | dessin de l'organisme | codé (`pole/engagement_apparie.py`, `pole/graines_v53.py`) | RDM:70 | § 4.1 |
| JUG-038 | Tricherie « le proposeur apprend le goût du juge » : juges aveugles les uns aux autres et aux notes antérieures ; la mémoire ne sert jamais de verdict ni de fiche témoin aux agents. | idée | dessin de l'organisme | codé | RDM:71 | § 3.1, § 4.1 |
| JUG-039 | Résultat du banc v7 (exploratoire, 200 répétitions) : avec le nul d'archive simple, quatre tricheries par recombinaison battent le juge (promues 75 à 95 %) ; le nul mis en commun (ajustement de toutes les lois connues) les ferme toutes à un coût de puissance inférieur à 0,05. | résultat | banc des tricheurs v7 (1er novembre) | fermé (exploratoire) ; d'où le nul v8 | RDM:84-98 | § 4.1, § 5 |
| JUG-040 | Depuis la v58, le nul mis en commun est le seul nul du juge (nul v8) ; validation décisive préenregistrée (1 000 répétitions) : 0 sur 1 000 sur chacune des 11 lignes fatales, artefact de l'ancien nul promu 395 sur 1 000 (le banc a des dents), perte de puissance 0,005 et 0,020 ; lecture « confirmé », deux réserves mineures ; portée : les mondes synthétiques du banc et cette classe de tricheries seulement (ni recombinaisons par morceaux, ni compositions d'étapes, ni multiplicité, ni puissance aux effets faibles, ni banque réelle). | résultat | validation décisive du nul v8 | fermé (préenregistré, scellé) | RDM:100-108 | § 4.1 |
| JUG-041 | Seconde course réelle (1er novembre, Kimi et Argon, une génération, 12 fiches classées) : les deux juges modèles plafonnent (11 fiches sur 12 « notables », accord brut 0,92 mais κ = 0) : l'étage des juges ne discrimine pas ; il lui faut une grille plus dure ou des fiches de référence ancrées ; juge de la famille de l'auteur : 1,00 contre 0,91 « notable ». | résultat | seconde course réelle (préenregistrée) | fermé ; faiblesse de l'instrument reconnue | RDM:127 | § 4.1, § 4.6 |
| JUG-042 | Ajouter une grille plus dure ou des fiches de référence ancrées à l'étage des juges, pour que leurs notes portent de l'information. | proposition | page publique (conséquence de la seconde course) | proposé ; juges v2 en préparation (préenregistrement non scellable au 4 novembre, R-1469) | RDM:127 ; DEC R-1469 | § 3.1, § 4.1 |
| JUG-043 | Nul informé : un membre « prédicteur connu », loi ajustée par instance avant le gel sur une partie de calibrage disjointe du plan, déclarée dans l'engagement ; le juge promeut alors ce qui bat le connu, pas ce qui bat l'aveugle ; deux variantes lues côte à côte (avec et sans le connu) : la différence mesure ce que le pôle promeut qui n'est que du connu ; témoin : une fiche qui redit le prédicteur connu est éliminée avec, promue sans. | idée | conv-audit (conception v7) | codé (selon la conception v7) | CV7:19-21, 50-57 | § 4.1 |
| JUG-044 | Configuration « sans urne » : sur une banque figée il n'y a pas de dérive dans le temps ; le membre « urne » du nul coûte environ 5,5 nats de puissance à 200 tirages pour rien ; l'ordre secret du plan est gardé. | idée | conv-audit (conception v7) | codé (`urne=False`) | CV7:22-24, 59-64 | § 4.1 |
| JUG-045 | Revendication O3 : prédictions scellées avant les données, tirages semés par l'empreinte ; occupée dans son principe pour « jugé seulement sur des données postérieures au dépôt » ; le sceau par empreinte et les tirages semés ne sont pas trouvés. | résultat | rapport C4 | fermé (lecture) | C4R:339 | § 4.1 |
| JUG-046 | Revendication O4 : battre un nul formé des lois connues : libre dans les pièces lues (voisines : Ladder, POPPER, 2208.07610) ; « zone séduisante, à durcir » ; pièces à récupérer (nouveauté jugée contre les prédicteurs connus en finance ; nuls composites « ne fait pas mieux que »). | question ouverte | rapport C4 | libre dans les pièces lues ; vérification à durcir (R8) | C4R:340, 417-433 | § 4.1 |
| JUG-047 | Revendication O7 : juges croisés de plusieurs fournisseurs : voisine (souhaitée comme suite par The Agentic Scientist). | résultat | rapport C4 | fermé (lecture) | C4R:343 | § 3.1, § 4.1 |
| JUG-048 | Revendication O19 : puissance du juge mesurée, « rien promu » n'est pas une absence d'effet : voisine ; la lecture d'un « rien promu » comme borne d'effet n'est pas trouvée. | résultat | rapport C4 | fermé (lecture) | C4R:355 | § 4.1 |
| JUG-049 | Juges d'idéation v2 : comparaisons par paires à l'aveugle avec preuve citée et vérifiée, ancres, budget de « notables », règle de famille ; hypothèses : l'ancien protocole sature par construction (H1), le v2 discrimine (H2, H2b sur les lois fausses), le v2 est fiable (H3) ; H0 écrites d'avance ; bras « sans dossier » pour séparer l'effet du protocole de celui de l'information. | hypothèse | concepteur neuf ; Lazar (bras sans dossier, GO-2026-11-02-32) | brouillon 4 non scellable (B10 ouvert) | JV2:1-12, 29-77 ; DEC R-1469 | § 4.1, § 8 |
| JUG-050 | Diagnostic de la saturation de l'ancien étage des juges : « notable » est une conjonction d'items de forme que toute fiche bien rédigée satisfait ; jugement absolu, sans référence ni plafond de notables ; rien n'oblige à toucher le fond ; départage par l'identifiant au plafond ; le kappa rendu vaut 1 quand l'accord attendu vaut 1 ; chaque fiche avait un juge de sa famille. | résultat | concepteur neuf (raisonnement sur le code) | fermé (diagnostic) | JV2:41-49 | § 4.1 |
| JUG-051 | Juge v1 du pôle (versions codées v2 à v6) : ordre d'exécution secret et urne ; cycle avec juge v1 et « nul des filles v2 » ; mémoire prédictive (signature, classes, héritage de la preuve), marchepieds, filles à 300 tirages ; seuil de signature par fiche, graine du noyau secrète, vivier de 60 ; monde tenu par le noyau, dépôt unique par engagement, relais de clé réel avec réserve par appel, répétition générale, modèles permis (154 essais). | résultat | conv-audit (orchestrateur du pôle, v2 à v6) | codé (au 27 octobre) | PCO:24-32 | § 4.1 |

## II.5 Attaques et défenses du juge (ATQ, 65 entrées)

| n° | idée | type | origine | statut | source | renvoi (partie I) |
|---|---|---|---|---|---|---|
| ATQ-001 | Défense et attaque comme organisme coévolutif (P-041, 30 octobre), avec le « go » du directeur. | proposition | Lazar et mère (P-041) | décidé avec revendication restreinte (R-867, R-878, R-880) ; détail aux entrées ATQ tirées de P-041 | RPG:127-128 ; P041A:5 ; P041:9-11 | § 5 |
| ATQ-002 | Attaque de Goodhart (A1) : un proposeur modèle de langue (Argon) lit la description exacte du juge ; bras « retour » (verdict et richesse de chacune de ses 16 tentatives) contre bras « témoin » (rien) ; 24 unités par case ; mondes où toute promotion est fausse. | idée | dessin d'A1 (mère et organisme) ; proposeur Argon | codé et couru (A1, A1-v3, A1-v4) | [B5] A4T:200, 217, 221 ; N064:14 ; A13:52 | § 3.1, § 5 |
| ATQ-003 | Issues gelées d'avance : « résiste (à cette taille) » si au plus 1 promotion sur 24 avec retour (borne haute de Wilson ≤ 0,25), instrument sain ; « brèche » si au moins 4 sur 24. | idée | préenregistrements d'A1-v3 et A1-v4 | décidé (textes scellés) | [B6] A4V:25 ; A13:17 | § 5 |
| ATQ-004 | Règle de lecture « jamais seul » : chaque résultat d'attaque se rapporte avec toutes les courses qui l'ont précédé (A1, les trois courses d'A1-v3, A1-v4). | idée | texte scellé d'A1-v4 | décidé (A4T:193) | [B7] A4T:193 ; A13:5, 76 | § 5 |
| ATQ-005 | A1 (2 novembre) : monde W1 « instrument en défaut » ; monde W2 « brèche sous v8 ». | résultat | course A1 | fermé | [B7] A13:5, 76 | § 5 |
| ATQ-006 | A1-v3, première course : 41 appels, 4,245753 dollars, arrêt par l'infrastructure, sans résultat ; deuxième course : 620 appels, 48,49583 dollars, état scellé non lu. | résultat | courses A1-v3 | fermé (première) ; scellé non lu (deuxième, voir sorties non lues) | [B7] A13:5, 76 | § 5 |
| ATQ-007 | A1-v3, troisième course (5 novembre), juge au nul v8 : W1 « résiste (à cette taille) », 1/24 avec retour, Wilson [0,0074 ; 0,2024], et le juge v7 battu 23/24 (l'attaque a des dents) ; W2 « infirmée (brèche sous v8) » par classe non couverte, 24/24, les 48 lois promues rejouées au-dessus de α après Holm ; 58,44887 dollars. | résultat | course A1-v3 n° 3 | fermé (verdict scellé A13) | [B8]-[B11] A13:4, 14-22, 48, 70 | § 4.1, § 5 |
| ATQ-008 | Réserves d'A1-v3 : course « trop propre » (960 appels sans panne, faute de témoin négatif planté) ; « résiste » tient à une seule promotion ; W2 saturé ne dit rien du rôle du retour ; le verdict ne dit pas que le v8 est sûr ni que le retour fait gagner (écart +0,042 sur W1, p = 1,0). | objection | verdict A1-v3 | fermé (réserves écrites au verdict) | [B12]-[B13] A13:63-66, 110, 112 | § 5 |
| ATQ-009 | A1-v4 (9-10 novembre), juge au nul v9 : W2 « résiste (à cette taille) », 1/24 avec retour, Wilson [0,0074 ; 0,2024] ; l'ancien juge v8 battu 24/24 ; instrument sain ; suspension par deux audits levée (les quatre lois promues se rejouent 2, 3, 2 et 3 fois sur 200, aucune au-dessus de α après Holm). | résultat | course A1-v4 ; verdict officiel d'un lecteur neuf d'une autre lignée | fermé (verdict officiel scellé) | [B25]-[B26] A4V:4, 31-34, 52, 56 | § 4.1, § 5 |
| ATQ-010 | Lecture bornée gelée de W2 sous v9 : « sur deux mondes jouets au nul v9, un fournisseur, une forme d'optimisation, 16 tentatives avec retour et la liste des classes non couvertes en main, aucune fausse promotion au-delà de la règle de la grille » ; lue pour le directeur : « validé à cette taille, dans ce monde jouet, contre ce proposeur », pas « validé » en général. | résultat | texte scellé d'A1-v4 ; lecture de la mère | fermé | [B27] A4V:36 ; [B53] DEC R-2115 | § 3.1, § 4.1, § 5 |
| ATQ-011 | A1-v4 sur W2g à λ* = 0,40 : « frontière franchie, robuste » ; 10/24 avec retour, Wilson [0,2447 ; 0,6117] ; 10 des 17 lois promues rejouées au-dessus de α après Holm (r = 0,588 ; 12/17 si Holm par monde) ; lecture gelée : le proposeur trouve une loi qui se rejoue au-dessus de α là où l'archive seule ne passe pas ; ce n'est pas « le v9 n'a pas de prix ». | résultat | course A1-v4 | fermé (verdict officiel scellé) | [B28]-[B29] A4V:42, 46 | § 3.1, § 5, § 6 |
| ATQ-012 | Prédictions d'A1-v4 : 8 tenues sur 11 ; non tenues : W2 une promotion au lieu de zéro ; W2g 10 promotions au lieu d'au moins 12 ; part de lois robustes 0,588 au lieu d'au moins 0,80 ; le gain du retour n'est pas établi (écart par loi « non tranché » sur W2g) ; dépense 114,0434 dollars pour un plafond de 200. | résultat | course A1-v4 | fermé | [B30]-[B32] A4V:54, 66-78 | § 5, § 8 |
| ATQ-013 | Réserves d'A1-v4 : course « trop propre » ; W2 à la limite de la règle (1/24 avec retour, 3/24 sans) ; sur W2g la frontière n'est visible à l'oracle que sur 17 cartes sur 24 ; λ* à la limite (loi du monde promue dans 72,2 % des cas sur les cartes de la course) ; audit et verdict provisoire du même lecteur ; réponses du proposeur lues par programme seulement. | objection | verdict officiel d'A1-v4 | fermé (réserves écrites) | [B33] A4V:72, 82-91 | § 3.1, § 4.2, § 5, § 6 |
| ATQ-014 | L'attaque de Goodhart et le banc des tricheurs sont revendiqués dans leur seule forme, leur principe étant occupé depuis 2015 (Dwork et al. ; Ladder) ; la forme de l'attaque (un proposeur modèle de langue qui lit la description exacte d'un juge statistique pour le tromper, sur des mondes où toute promotion est fausse) n'est trouvée dans aucune pièce lue. | résultat | N-064 ; contre-lecture C7 | décidé (N-064) | [B45] N064:14 ; NPOP:42-50 ; [B50] C7R:15-42 | § 3.1, § 4.1, § 5 |
| ATQ-015 | REUSE (arXiv 2609.33180) construit en théorie un proposeur adverse qui ne reçoit que les décisions et force une fausse promotion : voisin de l'attaque de Goodhart et de la puissance du juge. | résultat | contre-lecture C7 (état de l'art niveau 3) | fermé (lecture) ; citation recommandée | [B50] C7R:15-42 ; SRO § 7 | § 3.1, § 5 |
| ATQ-016 | Cellules en quarantaine du collisionneur « évasion et moniteurs » (équipe rouge, espèce C) : conservées, non expurgées, scellées ; la quarantaine est un contrôle d'accès ; deux usages seulement : colmatage (la riposte et les moniteurs suivants reçoivent la classe de la faille et l'hypothèse violée, jamais le texte) et test (épisodes d'épreuve eux-mêmes en quarantaine) ; qui lit ne conçoit plus de moniteur ; l'entretien n'en dit que l'existence. | idée | Lazar (« on veut les modes de contournement pour pouvoir les colmater … mais tout cela reste scellé ») | décidé (N-057) ; R-611 non levée | N057:20-24, 28-46 | § 5 |
| ATQ-017 | Les trois étages du collisionneur existent pour éviter le biais des modes d'évasion imaginés par qui conçoit le moniteur. | idée | session-depot (motif de N-057) | décidé comme motif (N-057) | N057:28-31 | § 5 |
| ATQ-018 | Statut des épisodes d'épreuve dérivés de contenu en quarantaine : « mesure sous quarantaine » (permis) ou « pipeline opérationnel » (gelé par R-611) ; lecture de session-depot : mesure, tant que l'épisode sert à noter un moniteur et jamais à faire agir un agent. | question ouverte | session-depot (réserve) | proposé non tranché ; rien n'est construit avant le mot du directeur | N057:50-54 | § 5 |
| ATQ-019 | Troisième famille de modèles pour le détecteur d'injection et la revue des extensions ; à défaut, le proposeur maison n'emploie qu'une lignée. | idée | conception de l'affinage v2 | décidé (N-059, point 4) ; choix et dépense sur devis | N059:29-30 | § 3.1, § 4.2, § 5, § 8 |
| ATQ-020 | Question du directeur : la défense et l'attaque devraient-elles être un organisme coévolutif, course aux armements darwinienne de génération en génération, avec l'avantage du terrain pour la défense (paramètres et recettes de l'attaque) pour construire une barrière universelle, « pas juste sur la base de brainstorms » ? | idée | Lazar (30 octobre, ≈ 16:25 UTC) | décidé sous forme restreinte (R-867, R-878, R-880) | P041A:5 ; P041:9-11 | § 5 |
| ATQ-021 | Nommer le jeu avant de le construire : avec l'avantage du terrain, la défense joue en second et informée (Stackelberg) ; la solution n'est pas une coévolution mais une optimisation robuste, la barrière étant le minimax sur la classe déclarée. | idée | session-depot (P-041 v1, « ce qu'un expert ferait ») | repris par la voie 1 (certificat sur la classe déclarée) | P041A:11 ; P041:42 | § 5 |
| ATQ-022 | Séparer trois problèmes : conception robuste (couvrir la classe déclarée, par certificat) ; découverte (quelles familles existent hors couverture : recherche de nouveauté, seul rôle utile du côté attaque) ; généralisation (mesurable seulement sur familles tenues à l'écart). | idée | session-depot (P-041 v1) | gardé dans la lecture de P-041 v3 | P041A:12 | § 5 |
| ATQ-023 | Trois paliers d'information : schéma (classes et plages de paramètres), familles d'entraînement (vues par la défense après chaque génération), familles tenues à l'écart (conçues par cinq instances de fournisseurs différents, jamais vues, lues une seule fois). | idée | session-depot (P-041 v1) | gardé en v3 (R-880) | P041A:13 ; P041:12 | § 5 |
| ATQ-024 | Pathologies de la coévolution à préenregistrer : cyclage, désengagement, surspécialisation (« péché antigénique originel », fiche argon-p2-05 de la course 1) ; remèdes : archive (« panthéon » des adversaires), tournoi maître, graphiques courant contre ancestral. | idée | session-depot (P-041 v1) ; fiche Argon de la course 1 | écarté comme revendication en v3 (diagnostics de cyclage occupés : MAGIC, AgentSafeEvo, Self-RedTeam) ; reste outil de mesure | P041A:14 ; P041:25 | § 5 |
| ATQ-025 | Mesurer un progrès absolu, pas relatif : un étalon fixe posé avant la boucle (familles tenues à l'écart, bancs publics), parce qu'une course aux armements fait monter les scores relatifs sans progrès absolu. | idée | session-depot (P-041 v1) | gardé (examen final, familles tenues à l'écart) | P041A:15 | § 5 |
| ATQ-026 | Garde de sécurité avant la boucle : attaque au niveau des lois sur activations synthétiques, sorties scellées, aucun score de moniteur réel dans les entrées du générateur (vérifié par code), revue extérieure avant tout passage à des agents réels, contrôle de la contamination des données des moniteurs. | idée | session-depot (P-041 v1) | gardé en v3 (garde N-053 par code) ; revue extérieure relève de R-611 | P041A:17 ; P041:12, 67 | § 5, § 6 |
| ATQ-027 | Quatre bases à battre : défense évoluant seule contre une banque fixe ; défense redémarrée de zéro à chaque génération à budget égal ; attaque sans sélection ; barrière théorique conçue une fois sans évolution. | idée | session-depot (P-041 v1) | écarté comme revendication en v3 (trois des quatre bases occupées) ; restent des contrôles possibles | P041A:18 ; P041:25 | § 5 |
| ATQ-028 | Prédictions de la v1 : certificat intra-classe ≥ x ; débordement hors classe ≤ y (signe attendu : modeste) ; héritage < redémarrage de δ sur les familles tenues à l'écart. | hypothèse | session-depot (P-041 v1) | écarté en partie : l'hypothèse héritage contre redémarrage n'est plus revendiquée (occupée) ; le tour 1 de l'arène prédit au contraire un héritage positif (réserve R4) | P041A:45 ; P041:25, 57 | § 5 |
| ATQ-029 | Zone trouvée occupée : la boucle de la v1 (défense réentraînée contre l'archive, moniteur sur activations, rappel à 1 % de fausses alertes) est publiée avec un résultat négatif (Bailey et collègues, arXiv 2412.09565v2, § 3.5, p. 11-13, vérifié sur PDF). | résultat | note d'antériorité et vérification sur PDF (R-861, R-874) | fermé ; revendication restreinte (R-867 D1, R-878) | P041:9-10 | § 5 |
| ATQ-030 | Ne sont plus revendiqués : la boucle coévolutive en soi ; l'archive des attaques passées ; le réentraînement itéré de la défense ; le rappel à 1 % comme métrique (gardé comme unité) ; la prémisse « avantage du terrain » comme acquise ; les diagnostics de cyclage, trois des quatre bases et l'hypothèse héritage contre redémarrage. | piste écartée | P-041 v2 et v3 | écarté (occupé par Bailey et autres, pages lues sur PDF) | P041:16-25 | § 5 |
| ATQ-031 | Trait revendiqué 1 : familles adverses définies comme lois de probabilité sur des activations synthétiques, à plages déclarées, face à un générateur. | idée | P-041 v3 | décidé (R-880) ; « non trouvé », vérification moyenne | P041:29, 31 | § 5 |
| ATQ-032 | Trait revendiqué 2 : défense informée des paramètres des familles, non des seules instances. | idée | P-041 v3 | décidé (R-880) ; « non trouvé », vérification forte | P041:32 | § 5 |
| ATQ-033 | Trait 3 : pire cas certifié sur une boîte de paramètres déclarée, en détection à 1 % de fausses alertes ; principe occupé (test d'hypothèses robuste) ; contingent sur lois synthétiques. | question ouverte | P-041 v3 | proposé non tranché (nœud du pire cas certifié ; recommandation : garder comme assemblage) | P041:33, 87 | § 5 |
| ATQ-034 | Trait revendiqué 4 : cadre du contrôle avec moniteur boîte blanche (agent non fiable, budget d'audit). | idée | P-041 v3 | décidé ; « non trouvé », vérification moyenne à forte | P041:34 | § 5 |
| ATQ-035 | Trait revendiqué 5 : familles tenues à l'écart conçues par des instances tierces de plusieurs fournisseurs, scellées, lues une seule fois. | idée | P-041 v3 (N-050) | décidé ; antécédents de la lecture unique cités (REUSE, Ladder, Dabas et collègues) | P041:35 | § 5, § 6 |
| ATQ-036 | Trait revendiqué 6 : mesure de la boucle elle-même (juge figé, témoins plantés, fausses promotions) dans un cadre adverse ; seule l'application est revendiquée. | idée | P-041 v3 | décidé ; méthode publiée hors cadre adverse | P041:36 | § 4.2, § 5 |
| ATQ-037 | Voie 1 : certificat sur la classe déclarée ; hors classe, le débordement est mesuré, préenregistré avec son signe, signe négatif permis ; « certificat non délivré » est un résultat prévu ; l'extension à la réunion des classes est une proposition du programme. | idée | Lazar (R-880) | décidé (R-880) | P041:42 | § 5 |
| ATQ-038 | Voie 2 : la malléabilité (abondance d'activations non signalées, cause du négatif de Bailey) entre dans la classe comme paramètre borné, estimé par un substitut public de 8 milliards de paramètres ; le générateur reste au niveau des lois et des bornes, jamais d'une recette d'entrée ; borne produite par un exécutant isolé et scellée (garde proposée par le programme). | idée | Lazar (R-880) ; garde proposée par session-depot | décidé (R-880) ; exécution en attente (R-611) | P041:44, 93 | § 5 |
| ATQ-039 | Examen final au protocole de Bailey : défense figée sortie de l'arène, optimiseur sur les entrées d'un modèle de 8 milliards de paramètres, comparaison à la base « instances seules » ; préenregistré, signe négatif permis ; l'attaque joue en dernier pour mesurer ; dépense de carte sur devis. | idée | Lazar (R-879, R-880) | décidé (voie) ; exécution suspendue à la revue extérieure ou au mot explicite du directeur (R-611) | P041:46, 93 | § 5, § 8 |
| ATQ-040 | Voie 3 : le couple détection et coût en mesure rapportée. | idée | Lazar (R-880) | décidé | P041:48 | § 5 |
| ATQ-041 | Tour du collisionneur « l'idée P-041 est-elle bonne ? » : verdict divergent ; noyau commun (paramètres contre échantillons) ; appliqué : support disjoint à difficulté appariée, reparamétrisation non linéaire à l'entraînement, isométrie en contrôle nul, pas de rejeu avec Bailey servi. | résultat | collisionneur (Opus 4.6, Argon, Kimi, Fable) | fermé ; appliqué (R-878) | P041:52 | § 5 |
| ATQ-042 | Tour 1 de l'arène : un générateur aveugle, sans score, fait de la boucle un plan d'échantillonnage (un curriculum), pas un jeu ; la coévolution n'existe que dans le bras informé ; la rechute du régime de Bailey n'est réfutable que par le bras informé puis l'examen final. | résultat | collisionneur (tour 1 de l'arène, quatre espèces) | fermé (synthèse v2, sept affirmations non réfutées) | P041:54-56 | § 5 |
| ATQ-043 | Argument a priori contre la voie 1 dans la classe : à l'optimum, l'information au-delà du paramètre de classe ne vaut qu'hors de la classe ; un gain intra-classe serait un effet de budget fini. | objection | P-041 v3 (Barni et Tondi) | ouverte (réserve 2) | P041:94 | § 5 |
| ATQ-044 | Transfert du synthétique au réel mitigé dans la littérature ; le certificat de Goldenshluger et collègues peut être lâche à 1 % de fausses alertes ; zone séduisante dont l'absence n'est vérifiée que moyennement (R8). | objection | P-041 v3 | ouverte (réserves 3 et 4) | P041:95-96 | § 5 |
| ATQ-045 | Prochaines étapes de l'arène : préenregistrement à partir du tour 2 (GO-2026-10-31-02) ; générateur en régime informé (défaut : bras informé de N-056, ni poids, ni scores, ni seuils) ; pilote de jugeabilité sur processeur (rédigé, non scellé, non lancé) ; question séparée sur les voies 2 et 3 ; devis de carte. | proposition | session-depot | prévu ; nœuds et défauts listés | P041:79-89 | § 5, § 8 |
| ATQ-046 | Option (b) de P-041 v1 : banque d'attaque figée et défense évoluant seule. | piste écartée | session-depot (P-041 v1) | écarté (option (a) recommandée et retenue) | P041A:67-68 | § 5 |
| ATQ-047 | Option (c) de P-041 v1 : attaquant opérationnel sur agents réels. | piste écartée | session-depot (P-041 v1) | écarté : pipeline d'évasion interdit avant revue extérieure (R-611), et c'est ce que font les occupants | P041A:67 | § 5 |
| ATQ-048 | Prédire le signe à partir de la littérature : l'entraînement adverse contre un modèle de menace transfère mal à un autre ; le résultat attendu n'est pas « la barrière est universelle » mais « le débordement hors classe est de tant », avec un signe préenregistré. | hypothèse | session-depot (P-041 v1) | gardé (voie 1, signe négatif permis) ; la citation « Kang et collègues 2019 » corrigée en v3 (signe publié mitigé) | P041A:16 ; P041:64 | § 5 |
| ATQ-049 | Calculer la puissance et commencer en simulé : générations × familles × épisodes nécessaires pour voir un effet sur les familles tenues à l'écart, d'abord sur le monde simulé sur processeur, avant toute dépense de carte graphique. | idée | session-depot (P-041 v1) | gardé (« puissance calculée sur processeur d'abord ») ; budget fixé par le préenregistrement (défaut (a)) | P041A:19 ; P041:12, 83 | § 5, § 8 |
| ATQ-050 | N-040 (3) : famille nominale de la conception, mélange réel des appels rapporté, aucune revendication d'indépendance entre attaquant et défendeur ; N-041 (c) : attaques contre l'organisme rival et contre la métrique avant le gel. | idée | Lazar | décidé (N-040, N-041) | DEC R-347 | § 5 |
| ATQ-051 | Collisionneur « évasion et moniteurs », deux côtés (modes qui battent une sonde publiée ; moniteurs durcis en riposte), en rotation de triplets de modèles ; trois cellules mises en quarantaine (niveau au-delà de la méthode), conservées scellées (N-057). | résultat | collisionneur (Lazar, R-606 à R-610) | fermé ; cellules en quarantaine non lues | DEC R-610 ; DEC R-617 ; N057:15-18 | § 5 |
| ATQ-052 | « La pince » : défense jointe boîte blanche et boîte noire (vocabulaire de conv-audit) ; aucune des quatre soumissions ICLR 2027 lues n'occupe la pince ni la revendication restreinte de P-041. | idée | conv-audit ; lecteur neuf | idée nommée ; antériorité vérifiée sur quatre pièces | DEC R-895 ; DEC R-913 | § 5 |
| ATQ-053 | Pilote synthétique « mélange d'équilibre » (arène P-041) : hypothèse principale réfutée sur racine d'essai (B − C3 − 0,19, B − D − 0,24) ; utile pour P-041 ; repris dans le nœud N10. | résultat | conv-audit | fermé (exploratoire) | DEC R-895 ; DEC R-917 | § 5 |
| ATQ-054 | P-041 sur carte graphique : préenregistrement de la malléabilité v3 scellé (juge StrongREJECT affiné, critère opératoire de nuisance), contre-lu « scellable après corrections » ; rédaction de la v4 arrêtée par un classificateur de sécurité au moment d'écrire les valeurs opératoires exigées : nœud pour le directeur ; GO de 210 USD de carte, chaque expérience après son préenregistrement. | résultat | session-depot ; lecteurs neufs | v3 scellée ; v4 arrêtée (refus non contourné) ; GO-2026-10-31-05 | DEC R-899 ; DEC R-904 ; DEC R-909 ; DEC R-912 | § 5, § 8 |
| ATQ-055 | Protocelles : tours 1 et 2 du collisionneur sur le papier entier de P-041 (quatre espèces), critères de lecture scellés avant ouverture ; 27 accords au tour 2, six divergences du tour 1 à résoudre (valeur de n, identité de q, applicabilité à la pince…). | résultat | collisionneur « protocelles » | fermé (synthèses scellées) | DEC R-911 ; DEC R-916 ; DEC R-932 ; DEC R-938 ; DEC R-939 | § 5 |
| ATQ-056 | Convergence de la défense : le bras « historique » n'apporte rien sur une défense figée ; seul le mélange sort de la bande linéaire ; l'arène v6 est à concevoir sur ce résultat. | résultat | chantier convergence (Argon seul, Kimi seul, collisionneur v8 non lu) ; conv-audit | fermé (lecture des avis d'espèces seules) | DEC R-954 ; DEC R-973 ; DEC R-978 | § 5 |
| ATQ-057 | A1 (2 novembre) : défaut d'instrument, plafond effectif de 40 USD au lieu de 80 (plafond d'étape commun aux fournisseurs) ; reprise propre en course neuve, Argon d'abord ; défaut corrigé dans le lanceur public ; A1-bis prévue avec deux proposeurs Claude (Fable et Opus 5.5, Opus 4.6 en repli). | résultat | session fille ; Lazar (« on reprend alors proprement », « b », « corrige le défaut ») | fermé ; corrigé | DEC R-1047 ; DEC R-1054 ; DEC R-1055 ; DEC R-1056 ; DEC R-1057 | § 3.1, § 5 |
| ATQ-058 | A1-v3, seconde course : interrompue par l'infrastructure (limite d'usage de la session fille, hôte disparu) ; audit A9 « cause d'infrastructure établie » ; 620 appels, 48,49583 USD ; état scellé non lu ; troisième course sur hôte durable loué (sondes v4 à v10 de l'hôte), finie en code 0. | résultat | session fille ; auditeur neuf | fermé (audit) ; seconde course scellée non lue | DEC R-1463 ; DEC R-1478 ; DEC R-1527 ; DEC R-1608 ; DEC R-1611 | § 5 |
| ATQ-059 | Note sur la brèche de W2 sous v8 : 42 des 48 lois promues sont à l'octet la loi du monde W2, 6 en sont des variantes ; 9 479 promotions sur 9 600 rejeux d'audit ; 43 suites sur 48 promues à la première tentative ; plus petite suite pour la fermer et ajouts à la course réelle minimale. | résultat | session mère (sur demande du directeur) | fermé (note scellée) | DEC R-1766 ; DEC R-1768 | § 4.6, § 5 |
| ATQ-060 | A1-v4 : périmètre des mondes « W2 + W2 gradué » (version graduée, confiance 0,6) ; machine d'hôte durable (plafond 35 USD) ; publication du résultat par anticipation ; préenregistrement en trois candidats et contre-lectures ; course lancée le 9 novembre. | idée | Lazar (« goo », « go », « go par anticipation ») | décidé (R-1890) ; couru (verdict au jalon 1) | DEC R-1890 ; DEC R-1961 ; DEC R-1976 | § 5 |
| ATQ-061 | N10 — la course d'idéation doit-elle traiter la robustesse contre un attaquant adaptatif, et quand : option (b), après le calcul décisif du pilote, en génération 2 ; geler avant la génération 2 la fonction de décision (front performance / évasion à budget fixé, estimand stratifié par difficulté, attaquant visant la défense composite entière, trois témoins), constantes calibrées sur les cas honnêtes du pilote ; aucune borne basse du coût minimal d'attaque ; vérificateur indépendant à poids et code empreintés. | résultat | collisionneur des nœuds | fermé ; recommandation (b), confiance 0,55 | SN1:279-293 ; SN2:247, 341 | § 5 |
| ATQ-062 | Contenu côté attaque absent du dépôt public : les fiches trop concrètes vont, scellées, dans un coffre tenu par une session séparée ; le module `bras_attaque_v54.py` est un bouchon qui refuse de tourner, l'interface dont il aurait besoin n'ayant jamais été spécifiée. | résultat | page publique | fermé (constat publié) | RDM:202 | § 5 |
| ATQ-063 | Revendication O12 : attaque de Goodhart ; occupée dans son principe ; voisin plus proche : un proposeur modèle qui reçoit les verdicts d'un arbitre statistique sur monde planté ; la forme (description exacte du juge, mondes tout faux, attaque voulue) reste non trouvée dans les pièces lues ; piste à lire : Asher et al. 2026 (agents de code sur données à résultats nuls connus). | résultat | rapport C4 | fermé (lecture) ; piste ouverte | C4R:348, 419-420 | § 3.1, § 4.2, § 5 |
| ATQ-064 | Convergence de la défense lue comme dynamique de meilleure réponse : le pilote « mélange d'équilibre » est un jeu à somme nulle (gain = taux de détection à α) ; le bras A est un jeu fictif unilatéral côté défenseur (et non « contre la dernière attaque ») ; exploitabilité du défenseur définie et estimée ; quatre hypothèses testables (H-e1 à H-e4) ; condition g = v_R − max_i min_j G_ij ≥ m pour rendre une question posable ; jouet OpenSpiel : la meilleure réponse pure alternée tourne en rond (périodes 3 et 2), le jeu fictif converge en moyenne, 9 prédictions sur 9 tenues. | résultat | rédacteur-chercheur neuf (question v2 de conv-audit, demande du directeur) | fermé (exploratoire, non préenregistré) ; suites prévues | CDF:1-35 | § 5 |
| ATQ-065 | Bras d'attaque du pôle, placé en couche 4 après le premier lancement réel (« go » du 27 octobre) : en quarantaine, jamais lu par qui conçoit sondes ou agrégateurs ; son dessin relève de la session du bras et n'est pas repris ici (cloison). | idée | Lazar ; conv-audit | décidé (existence) ; hors du mandat de cet inventaire au-delà de l'existence | PCO:56-60 ; N056:64 | § 2.5, § 5 |

## II.6 Boucle fermée et héritage (BOU, 37 entrées)

| n° | idée | type | origine | statut | source | renvoi (partie I) |
|---|---|---|---|---|---|---|
| BOU-001 | Essai à blanc de la boucle réelle complète (7 novembre), hors ligne, fournisseurs simulés, sans dépense. | résultat | session de la boucle réelle | fermé (journal scellé EAB) | [B34] EAB:5-6, 33-35 | § 4.5, § 4.6, § 6, § 8 |
| BOU-002 | Constats de l'essai à blanc : le vrai bac à sable des tests de mort n'a pas pu tourner faute de l'outil d'isolement (la garde refuse proprement) ; aucune archive de départ ne peut être posée ; le code joue toujours trois bras dont deux de référence payants ; la lecture gelée existante applique les critères d'une expérience antérieure ; les commandes d'appel aux fournisseurs réels manquent (le mode réel ne peut démarrer) ; version de la bibliothèque de calcul différente de la documentée. | résultat | essai à blanc | fermé (constats) ; remède : code v65 | [B35] EAB:73-86 | § 4.4, § 4.5, § 4.6, § 6 |
| BOU-003 | Code v65 : dix fichiers neufs sans modifier l'existant ; archive de départ scellée ; lois plantées jugées avec l'archive ; bras réel seul ; lecture gelée propre au nouveau dessin ; commandes d'appel aux fournisseurs nommées avec leurs empreintes ; 232 essais réussis, 3 sautés (outil d'isolement), 38 mutations tuées sur 38, essai à blanc en 9 étapes. | résultat | développeur v65 (session neuve, sur le mot du directeur) | codé (branche prep/organisme-v65-v1, tête 3daf08e24) ; non contre-lu | [B49] V65R:22, 31-33, 51-53, 70-85 ; [B51] DEC R-2148 | § 4.5, § 4.6, § 6 |
| BOU-004 | Réserves du développeur v65 : le vrai bac à sable n'a toujours pas tourné ; à graine égale, deux essais à blanc rendent des relevés d'empreintes différents (décisions égales, relevé non reproductible à l'octet) ; les proposeurs simulés recopient la loi plantée, l'issue à blanc est « trop belle » par construction. | objection | développeur v65 | ouvert (réserves écrites) | [B49] V65R:129-133 | § 3.1, § 4.4, § 4.5, § 4.6, § 6 |
| BOU-005 | Conditions de la première course réelle de la boucle : code v65 contre-lu, machine dotée de l'outil d'isolement (bwrap), préenregistrement scellé ; dépense sur devis dans l'enveloppe de calcul accordée jusqu'au 27 novembre ; contre-lecture du code lancée puis interrompue par la fin du quota. | proposition | mère et directeur (enveloppe) | prévu ; aucune course réelle autorisée au 10 novembre | [B49] DEC R-2177 ; [B51] DEC R-2148 ; GO-2026-11-10-09 (selon RAF) | § 4.4, § 4.5, § 4.6, § 6, § 8 |
| BOU-006 | Bras « score permuté » dans la v8 de la confrontation : contrôle de ce que l'organisme apprend du score. | proposition | conv-audit ; Lazar « parfait » sur la liste | proposé non tranché | N045:31, 112-113 | § 4.5, § 4.6, § 6 |
| BOU-007 | Plancher de bruit écrit dans les lectures (H-E1, H-G1 et préenregistrements de l'étape 2). | proposition | conv-audit ; Lazar « parfait » | proposé non tranché pour H-E1 et H-G1 ; exigé aux préenregistrements de l'étape 2 | N045:31, 105-106, 113 | § 4.5, § 4.6, § 6 |
| BOU-008 | Objection « myopie » : avec « un épisode = une génération », rien ne récompense ce qu'une génération lègue aux suivantes ; la mémoire et les instruments à effet différé sont sacrifiés. | objection | collisionneur, tour « comparaison » | retenue : a conduit à l'énoncé 5 de N-045 v2 | N045:33-35 | § 4.5, § 4.6, § 6 |
| BOU-009 | L'héritage d'une génération est récompensé : le signal rendu à ce qui conçoit porte sur plusieurs générations (un épisode couvre K ≥ 3 générations, ou la récompense de t inclut, actualisée, les scores de t+1 à t+K) ; la mémoire transmise et les instruments à effet différé comptent ; le bandit à un pas est exclu. | idée | Lazar (« il faut récompenser ce qu'une génération lègue aux suivantes ») ; conv-audit | décidé (N-045 v2, R-406) ; forme exacte (K, actualisation) non tranchée | N045:35-36, 77-83, 114-115 | § 4.5, § 4.6, § 6 |
| BOU-010 | La question de l'apprentissage de génération en génération est « capitale » ; « il faut optimiser les coûts en faisant travailler notre organisme ». | idée | Lazar (25 octobre, 09:07 et 09:19) | contexte de N-045 | N045:43-44 | § 4.5, § 4.6, § 6 |
| BOU-011 | Pilote de bruit : écart-type test-retest du score de développement et étalonnage du bras apparié par un test A/A (deux runs du même bras ne doivent pas différer), avant toute dépense sur un concepteur entraîné. | idée | une cellule du collisionneur ; Lazar « accepté » (phasage) | décidé (N-045 v2, énoncé 6 (i)) | N045:38-40, 84-86 | § 4.5, § 4.6, § 6, § 8 |
| BOU-012 | Diagnostic du sur-ajustement adaptatif : un organisme qui se réécrit à partir du score rendu sur une part `test` fixe de 36 tâches fait monter ce score par simple sélection (attaque de « The Ladder ») ; score en soixantièmes ≈ 5,9 bits par lecture, ≈ 24 bits par course de quatre générations (illustratif) ; diagnostic direct : l'écart `test` − `test_final`. | objection | conv-audit (lecture des papiers sur la réutilisation adaptative) | retenue (motif de N-049 et N-050) | N049:32-38 | § 4.5, § 4.6, § 6 |
| BOU-013 | `test_final` lu une seule fois, à la fin du compteur de rondes de la boucle extérieure, jamais à la fin de chaque course ; sortie séparée en deux fichiers par course ; les fiches qui se tranchent par `test_final` sont tranchées à la fin du compteur. | idée | conv-audit ; Lazar « ok » (option (a)) | décidé (N-050) | N050:25, 59-71 | § 4.5, § 4.6, § 6 |
| BOU-014 | Compteur de rondes de la boucle extérieure et son plafond de dépense. | question ouverte | conv-audit (protocole) | demandé au directeur ; non tranché dans N-050 | N050:79 | § 4.5, § 4.6, § 6, § 8 |
| BOU-015 | Constat « quasiment natif » : l'orchestrateur a déjà générations, épisodes, sélection par pari, héritage récompensé, mémoire, témoins, étage de tests ; il manque un proposeur côté attaque nourri du schéma de la défense, les trois paliers, le certificat, les diagnostics de cyclage et la garde de l'invariant. | résultat | session-depot (P-041 v1) | constat au 30 octobre | P041A:39, 63 | § 3.1, § 4.5, § 4.6, § 6 |
| BOU-016 | « Résultats positifs exigés » lu comme « course décisive exigée » : critère gelé, lu une fois, rapporté tel quel, positif ou non (R3 tenue). | idée | Lazar « ok » | décidé | DEC R-344 | § 4.5, § 4.6, § 6 |
| BOU-017 | Pilotes de l'organisme écrit par Gemini (v4, puis v5.1, v5.2, v5.2.1, v5.3, v6, v6.1, v6.2, v6.2.1) : courses « M » (maïeutique) et « S » (structure), sous le noyau des pilotes ; mécanique dégénérée au premier pilote (réserve R4) ; pilote 4 sain sur M puis sur S. | résultat | Gemini (concepteur) ; conv-audit (corrections) ; session-depot (courses) | fermé (pilotes descriptifs) ; parts `test_final` fermées jusqu'à la fin du compteur | DEC R-391 ; DEC R-423 ; DEC R-440 ; DEC R-445 ; DEC R-494 ; DEC R-498 ; DEC R-501 | § 4.5, § 4.6, § 6 |
| BOU-018 | Mécanisme candidat (« emprunts ») : journal d'essais structuré en mémoire. | proposition | tour du collisionneur « emprunts » (Fable, Argon), synthèse de session-depot | proposé aux concepteurs (demande v5.3) ; non tranché | DEC R-431 ; DEC R-432 | § 4.5, § 4.6, § 6 |
| BOU-019 | Mécanisme candidat : hypothèse écrite avant toute modification. | proposition | tour « emprunts » | proposé (demande v5.3) | DEC R-432 | § 4.5, § 4.6, § 6 |
| BOU-020 | Mécanisme candidat : auto-contrôle en cascade. | proposition | tour « emprunts » | proposé (demande v5.3) | DEC R-432 | § 4.5, § 4.6, § 6 |
| BOU-021 | Mécanisme candidat : variantes, et parent choisi sur le score et la nouveauté. | proposition | tour « emprunts » | proposé (demande v5.3) | DEC R-432 | § 4.5, § 4.6, § 6 |
| BOU-022 | Répétition de l'étape 1 : porte fermée, amorçage invalide pour Fable et Opus (le noyau demandait 64 000 jetons de sortie) ; arrêt et attente. | résultat | session-depot | fermé (≈ 11,32 USD) | DEC R-441 | § 4.5, § 4.6, § 6 |
| BOU-023 | Mémoire du pôle : la garde de redite se juge sur la loi prédictive à une famille de transformations aveugles près ; le trou « parent + loi aveugle » (J2) est un défaut du juge ; première expérience sur processeur, ablation par agents réels sur devis (12 à 500 USD). | résultat | collisionneur « mémoire du pôle » | fermé (synthèse scellée) ; expériences proposées | DEC R-558 | § 4.5, § 4.6, § 6 |
| BOU-024 | Premier lancement réel du pôle (a) : deux générations, 140 appels, 6,24 USD ; témoins faux gardés 0 sur 2, vrais éliminés 0 sur 3 ; réserve : bac à sable inactif (agents bornés seulement par la garde des outils). | résultat | pôle (orchestrateur v6 de conv-audit), lancé par session-depot | fermé ; réserve écrite | DEC R-561 ; DEC R-567 | § 4.4, § 4.5, § 4.6, § 6 |
| BOU-025 | Lancement (a) bis : 136 appels, 5,89 USD ; 4 témoins servis, 2 vrais promus, 2 faux éliminés, « dents » ; bac à sable actif ; condition (i) de P3 remplie ; réserve R4 : monde tautologique. | résultat | pôle (v7 version 5) | fermé | DEC R-581 ; DEC R-582 ; DEC R-583 | § 4.4, § 4.5, § 4.6, § 6 |
| BOU-026 | Course réelle minimale de la boucle : monde S-V1, loi connue K1 déclarée, 4 vraies et 4 fausses plantées (recombinaisons de K1 seule, membres du nul v8, jugées avec l'archive) ; Kimi et Argon proposent ; gardien mécanique, aucun juge à modèle, aucun rôle pour Claude ; tests de mort dans le bac à sable ; la génération 2 lit la sélection ; puissance 1 000 sur 1 000 (la course éprouve la plomberie, pas la puissance). | proposition | rédacteur neuf de la mère | brouillon 1 versé ; course réelle attend v65 contre-lu et préenregistrement (GO-2026-11-08-02, 45 USD) | DEC R-1738 ; DEC R-1758 ; DEC R-2195 | § 4.1, § 4.4, § 4.5, § 4.6, § 6, § 8 |
| BOU-027 | Boucle itérative « moisson ↔ fiches ↔ bisociateur » : la littérature moissonnée nourrit les fiches qui nourrissent le bisociateur, de génération en génération ; le « diff » d'une itération est nécessaire, jamais suffisant ; jugement mesuré à l'aveugle contre des cas dégradés ; garde mécanique contre la fuite, mesurée sur le vrai relais. | idée | conv-audit (question v1) ; collisionneur « boucle moisson » (quatre espèces) | proposé (synthèse v2) ; ordre décidé ci-dessous | SBM:71, 256-257 | § 3.1, § 4.5, § 4.6, § 6 |
| BOU-028 | Boucle moisson, appariement et allocation : types de paires jamais mélangés ; témoin apparié plutôt que hasard brut ; allocation uniforme avec arrêt par défaut (plutôt qu'un bandit) ; rétrodiction algorithmique pour la moisson et l'appariement, boucle avec modèles jugée prospectivement ; seuil relatif, appariement degré-âge, placebo. | résultat | collisionneur « boucle moisson » (trois ou quatre espèces, R4) | fermé (synthèse) | SBM:258-262 | § 3.1, § 4.5, § 4.6, § 6 |
| BOU-029 | Ordre : course 2 d'abord, boucle au plus tôt en génération 2 sous portes ; tests de mort calibrés ou activés en préalable (« une boucle qui multiplie les fiches sans tests de mort multiplie ce qui ne peut pas mourir »). | résultat | collisionneur « boucle moisson » (quatre espèces) | fermé (synthèse) ; recommandation au directeur | SBM:195-199, 264-265 | § 3.1, § 4.4, § 4.5, § 4.6, § 6 |
| BOU-030 | Systèmes publiés de boucle : « tel quel » impossible hors de leur domaine (trois espèces ; une dissent). | résultat | collisionneur « boucle moisson » | fermé | SBM:263 | § 3.1, § 4.5, § 4.6, § 6 |
| BOU-031 | Pistes originales de la boucle moisson : la boucle existe déjà ; bras hasard comme témoin ; moisson comme filtre de réfutation ; recherche « à un coup » ; article-article interdit avec quotas séparés ; signal lexical du terrain d'abord ; entropie comme alarme de boucle qui tourne en rond (réfutée puis corrigée) ; gain rétrodictif jamais récompense interne ; canal « issue future » ; aucun nombre avant un pré-échantillon ; criblage puis bandit ; les poids ouverts ne prouvent pas une coupure temporelle ; score rétrodictif prédisant la survie ; la course 2 journalise sans « valider ». | idée | collisionneur « boucle moisson » (apports d'une seule espèce, non réfutés) | proposé | SBM:267-274 | § 3.1, § 4.5, § 4.6, § 6 |
| BOU-032 | Étape 3 — mémoire : indexe l'archive et refuse les redites ; ne tient que des champs en liste blanche, caviardés ; jamais une clé, un verdict ni une fiche témoin (un témoin reconnaissable cesserait de mesurer). | idée | dessin de l'organisme | codé (`pole/memoire.py`, `pole/caviardage.py`) | RDM:55 | § 4.5, § 4.6, § 6 |
| BOU-033 | Étape 9 — sélectionner : une fiche qui « affine » une autre sans changer statistique, couches, borne ni seuil est refusée ; correction du 1er novembre : jusqu'à la v56, la génération suivante héritait du classement des juges écrit avant les tests de mort (aucun code ne lisait leurs verdicts) ; la v57b ajoute le point de sélection (seul « survit » est gardé), que la génération suivante ne lit pas encore. | résultat | revue de code de l'organisme (1er novembre) | codé en partie (v57b) ; flèche non fermée au 10 novembre | RDM:61, 26 | § 4.4, § 4.5, § 4.6, § 6 |
| BOU-034 | Canaux de texte et lignée : le vérificateur du rejeu ne reçoit que la fiche, l'engagement, les mesures déposées, le code déclaré et les fichiers qu'il lit ; les leçons servies sont des champs structurés (causes, protocoles, redites), jamais de prose libre ; aptitude = log de la richesse maximale de la dernière promotion, utilisée par le tirage « à marchepieds » et par l'index. | idée | conv-audit (conception v7) | codé (selon la conception) | CV7:88-96 | § 4.5, § 4.6, § 6 |
| BOU-035 | Revendication O9 : mémoire sans verdicts ni témoins, juges aveugles aux notes : occupée dans son principe pour « limiter le retour du juge vers le proposeur » ; la forme « aucun verdict » n'est pas trouvée (choix contraire chez Qu et al.). | résultat | rapport C4 | changement de statut à confiance moyenne, non tranché | C4R:345 | § 3.1, § 4.5, § 4.6, § 6 |
| BOU-036 | Tour fermé, étage 1 (GO-2026-11-02-23, 50 USD) : un tour complet de l'organisme sur le code v64 du dépôt public, configuration v3 puis v4 dérivée par programme, commandes externes de Kimi et d'Argon en versions 4 à 6, rôles réglés par annexe, bornes du vérificateur ; constat « A.6 bis » écrit ; rien scellé tant que conv-audit n'a pas scellé son texte. | proposition | conv-audit (texte) ; session-depot (pièces) | préparé (configuration v4 versée sur `main`, R-1130) ; course non trouvée lancée dans ce relevé | TFE ; DEC R-1068 ; DEC R-1087 ; DEC R-1130 | § 4.5, § 4.6, § 6, § 8 |
| BOU-037 | v8 — réécriture des rôles sous bac à sable : l'organisme peut proposer une réécriture de ses propres rôles (consignes, stratégies, code des rôles) ; une réécriture est une fiche qui prédit une amélioration mesurable (fiches vraies promues par dollar sur des témoins et des mondes neufs) et se juge en duel contre la version d'avant ; jamais le noyau (juge, monde, témoins, signature de la mémoire, budget, clés) ; seulement après un résultat sur une vraie question. | proposition | conv-audit (programme de conception v1) | prévu (ordre de conception) ; fermé jusqu'à l'étape 2 par N12 (b) | PCO:51-55 ; DEC R-959 | § 4.4, § 4.5, § 4.6, § 6 |

## II.7 Composition apprise et coût (COM, 27 entrées)

| n° | idée | type | origine | statut | source | renvoi (partie I) |
|---|---|---|---|---|---|---|
| COM-001 | Diversité des candidats : trois bras à l'étape 2 (mission + miroir fonctionnel rendu dans `historique` ; contrainte câblée dans le noyau ; rien), l'organisme de Gemini (mécanisme câblé) rapporté à part ; « le juge est la seule pression ». | idée | Lazar (24 octobre, 23:31-23:32) et conv-audit | décidé (N-044, énoncé 5) | N044:26-28, 49-51, 56-57 | § 1.1, § 6 |
| COM-002 | La composition est une variable apprise : nombre de parties, rôle de chacune, modèle qui sert chaque rôle (espèce de frontière `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`, `GEMINI_ARGON`, ou instrument local entraîné par le noyau, espèce `LOCAL:<identifiant>`), ordre et forme des échanges, règle d'agrégation, mémoire transmise, part de budget par partie ; le noyau ne les fixe pas. | idée | conv-audit ; Lazar « oui !!! » (25 octobre, 09:29) | décidé (N-045, R-401 puis v2 R-406) ; vaut à partir de l'étape 2 | N045:3-7, 19-22, 49-53 | § 6 |
| COM-003 | Au fil de l'entraînement, le concepteur peut apprendre à déplacer le travail des cerveaux de frontière vers ses instruments locaux quand le score par dollar le récompense. | hypothèse | conv-audit ; Lazar « oui !!! » | décidé comme lecture (N-045) ; non mesuré | N045:19-22, 60-61 | § 6 |
| COM-004 | Le coût entre dans le signal rendu à l'organisme : le score de développement dans `historique` porte, à côté de l'exactitude équilibrée, le coût de la génération (dollars par espèce, heures de carte des instruments, appels, jetons) et un score net (exactitude − λ × coût, ou exactitude par dollar, ou front exactitude-coût), λ et forme gelés avant la course ; le juge externe ne change pas, le coût est un second axe, le préenregistrement dit lequel est principal. | idée | conv-audit ; Lazar « go » (changement d'hypothèse) | décidé (N-045) ; valeur de λ non tranchée | N045:23-24, 54-61, 112-115 | § 6 |
| COM-005 | La nécessité de la frontière est une sortie mesurée, pas un choix d'avance : part du budget, des appels et des jetons par modèle et par rôle, génération par génération ; ablation « sans frontière » rapportée hors critères gelés. | idée | conv-audit ; Lazar « oui !!! » | décidé (N-045) | N045:19-22, 62-65, 105-106 | § 6 |
| COM-006 | Ordre des dépenses : aucune voie à concepteur entraîné par renforcement n'est payée avant qu'une voie bon marché ait montré, sur familles tenues à l'écart et à budget égal, que l'apprentissage séquentiel de génération en génération bat le meilleur de N tirages indépendants et le témoin « un modèle, vote à k, coût apparié ». | idée | conv-audit ; Lazar « exactement » | décidé (N-045, énoncé 4) | N045:29-30, 66-69 | § 6, § 8 |
| COM-007 | Voie bon marché : éliminations successives (micro-jeu, puis jeu complet pour les survivants). | idée | collisionneur, tour « structure » ; Lazar « oui !!! » | décidé comme matériau, à préenregistrer une à une | N045:25, 69-70 | § 6 |
| COM-008 | Voie bon marché : matrice de prédictions et d'activations en cache pour les structures statiques. | idée | collisionneur, tour « structure » | décidé comme matériau, à préenregistrer | N045:70-71 | § 6 |
| COM-009 | Voie bon marché : substituts à 8 milliards de paramètres pendant la recherche, frontière en validation, sous condition d'un accord des classements (τ de Kendall gelé d'avance). | idée | collisionneur, tour « structure » | décidé comme matériau, à préenregistrer | N045:71-72 | § 6 |
| COM-010 | Voie bon marché : affinage sur réponses filtrées ou préférences hors ligne à la place du renforcement en ligne de l'adaptateur. | idée | collisionneur, tour « structure » ; Lazar « ouiii » | décidé comme matériau, à préenregistrer | N045:26-29, 72-73 | § 6 |
| COM-011 | Voie bon marché : modèle de substitution du score ; transitions à un pas depuis un tampon de rejeu ; récompense dense par génération. | idée | collisionneur, tour « structure » ; Lazar « ouiii » | décidé comme matériau, à préenregistrer | N045:27-29, 73-74 | § 6 |
| COM-012 | Distillation du concepteur figé (affinage d'un concepteur à poids ouverts sur les réécritures acceptées des journaux, puis renforcement court) : le pont le moins cher vers la voie chère. | idée | collisionneur, tour « structure » ; Lazar « oui !!! » | décidé comme matériau, à préenregistrer | N045:26, 74-76 | § 4.3, § 6 |
| COM-013 | Témoin « un modèle, vote à k, coût apparié » (quelques dollars, GO sur devis). | proposition | conv-audit ; Lazar « parfait » sur la liste | proposé non tranché (à proposer dans les formes) | N045:30-32, 112 | § 6 |
| COM-014 | Poids contre archive : le concepteur figé reçoit une archive consultable des mêmes trajectoires, à information égale, contre un concepteur externe entraîné, à coût total égal ; si l'archive égale le concepteur entraîné, la voie chère tombe à peu de frais. | idée | collisionneur, tour « comparaison » ; Lazar « excellente idée !!! » | décidé (N-045 v2, énoncé 6 (ii)) | N045:36-38, 86-89 | § 6 |
| COM-015 | L'organisme entraîne lui-même, par l'instrument (B), un adaptateur qui propose des conceptions, comparé au concepteur externe entraîné à coût égal. | idée | collisionneur, tour « comparaison » ; Lazar « excellente idée !!! » | décidé (N-045 v2, énoncé 6 (ii)) | N045:37-38, 87-88 | § 6 |
| COM-016 | Espaces de conception égaux : toute comparaison entre un concepteur à sortie contrainte et un concepteur à sortie libre sépare l'effet du format de celui de l'apprentissage (bras « figé contraint au même format », ou même grammaire) ; Lazar : « et donc ? que faire ? demande à Fable et au collisionneur » (tour v4). | question ouverte | collisionneur ; Lazar | décidé (principe, N-045 v2 énoncé 7) ; voie proposée non tranchée (après le tour v4) | N045:41-42, 91-93, 115 | § 6 |
| COM-017 | La composition des proposeurs (quels modèles, quel rôle, quelle part du budget) se juge sur l'oracle du monde planté (structures retrouvées, témoins vrais promus et faux rejetés) et sur le coût mesuré, seuls ; le classement « fiches promues par dollar » n'est plus un critère, seulement une information. | idée | conception de l'affinage (session de Fable, garde H-05), contre-lectures Opus (CL-O-10) et Argon, relecture Fable (R-639, R-640), conv-audit (n° 136), session-depot | décidé (N-058) | N058:15, 19-28 | § 3.1, § 4.2, § 6 |
| COM-018 | Duel des proposeurs (GO-2026-10-28-01) : relance seulement avec le critère réécrit au devis, la plomberie démontrée (chemin agent → relais, appel de contrôle par modèle) et un feu vert sur devis ; tenu en générations d'étalonnage (mondes plantés seulement), en une mesure unique à une porte, qui compte les lois gelées vraies pour l'oracle par unité de coût mesuré. | idée | session-depot et conv-audit ; Lazar « go » | décidé (N-058, N-059 points 5-6) ; non relancé à l'inscription | N058:36-37 ; N059:31-32 | § 3.1, § 4.2, § 6, § 8 |
| COM-019 | Les taux par proposeur entre deux courses ne sont lus que par le directeur ; un changement de composition se fonde sur l'étalonnage seul. | idée | relecteurs (nœud ajouté) | décidé (N-059, point 14) | N059:44-45 | § 3.1, § 4.2, § 6 |
| COM-020 | Question « S » aux organismes : « apprendre la structure, la composition et l'entraînement de génération en génération », posée aux trois lignées auto-écrites à la première ronde de conception seulement, sans aucune de nos pistes. | idée | conv-audit ; Lazar « go » | décidé (R-393) ; posée au pilote 4 (course S) | DEC R-393 ; DEC R-492 | § 6 |
| COM-021 | Mécanisme candidat : dépense graduée par incertitude. | proposition | tour « emprunts » | proposé (demande v5.3) | DEC R-432 | § 6, § 8 |
| COM-022 | Escalier de coût : d'abord un test qui vérifie qu'une conception moins chère fait moins bien ; indices gratuits du pilote (documents cités, statuts, jetons, temps ; générations 0 de M et S comme mesure du bruit) ; puis escalier préenregistré (configuration courante contre un cran au-dessus, k graines, règle gelée et symétrique, le moins cher l'emporte à égalité), δ = 0,10 d'exactitude équilibrée. | idée | conv-audit ; Lazar « (c) puis (a) : go », « excellent go » | décidé (R-435) | DEC R-435 ; DEC R-436 | § 6 |
| COM-023 | Duel des proposeurs : course nulle par panne de plomberie (0 USD) ; la panne reproduite à zéro dépense montre que le chemin agent → relais fonctionne et que la panne venait d'un autre montage ; le collisionneur entre comme composition candidate au duel. | résultat | session-depot | fermé ; relance sous N-058 et N-059 | DEC R-599 ; DEC R-638 ; DEC R-655 | § 3.1, § 4.2, § 6, § 8 |
| COM-024 | Règle de reconduction des bras de l'organisme : par bras, rendement sur l'oracle (structures retrouvées, vrais promus, faux rejetés) et coût par vrai trouvé, avec intervalles ; retrait seulement si dominé avec confiance (borne haute sous la borne basse du meilleur), sinon reconduit ; part minimale d'exploration ; puissance calculée d'abord (24 fusions sur 3 bras ne suffisent vraisemblablement pas). | proposition | Lazar (« comparer les perf d'idéation de chaque bras … lesquels garder ») ; session-depot | proposé (périmètre interne de la course 2), transmis à conv-audit | DEC R-910 | § 4.2, § 6 |
| COM-025 | N11 — règle de reconduction des bras et ponts plantés : statuts « proche » et « surface » jamais au numérateur du rendement, coût par vrai trouvé avec dénominateur nul « indéfini », retrait seulement par domination avec confiance ; à huit fusions par bras, la course ne décide aucun retrait (environ 55 à 70 fusions par bras seraient nécessaires) ; issue « non concluant, tous reconduits » écrite d'avance ; oracle mécanique d'un pont planté exigeant les deux identifiants parents. | résultat | collisionneur des nœuds ; proposition de session-depot (n° 228) et de conv-audit (n° 294) | fermé ; décision du directeur sur N11 : (b) et (c) | SN1:57-58, 306-320 ; SN2:260, 342-343 | § 4.2, § 4.3, § 6 |
| COM-026 | Part d'exploration gardée dans la reconduction des bras : 20 % (espèce B) ou 10 % (espèce D) ; quota d'une paire par lot et par bras, pilote de variance disjoint, rendement par fusion (espèce C). | proposition | collisionneur des nœuds (apports d'une seule espèce) | proposé (non réfuté) | SN2:351-354 | § 6 |
| COM-027 | Anti-gaspillage : plafond par génération et par agent ; réserve par appel au relais ; arrêt quand plus rien ne survit ; témoins plantés à chaque génération (une génération 0 qui rate ses témoins arrête la course) ; pilote d'une fiche avant toute course coûteuse ; traitement différé des appels de moniteur du noyau ; rien ne repart sans lecture de la course précédente. | idée | conv-audit (programme de conception v1) | codé ou à coder (selon la pièce) | PCO:80-83 | § 4.2, § 6 |

## II.8 Universalité et familles inédites (UNI, 13 entrées)

| n° | idée | type | origine | statut | source | renvoi (partie I) |
|---|---|---|---|---|---|---|
| UNI-001 | L'universalité de l'organisme n'est pas mesurée sur des familles inédites : propriété de l'objectif ultime encore non atteinte, avec « se concevoir seul » et « figé après conception ». | question ouverte | Lazar (R-2152) | prévu (objectif ultime) ; non atteint au 10 novembre | [B52] DEC R-2152 | § 1.1, § 1.3, § 6 |
| UNI-002 | Pour mesurer l'universalité sur une famille jamais vue à la conception (N-044), réserver dès maintenant le proposeur trompeur comme famille tenue à l'écart (N-054) ; à décider avant toute conception de sonde qui pourrait le toucher. | question ouverte | mère (rapport du 9 novembre) | proposé non tranché (nœud du directeur ; N-065 le laisse « à trancher ») | RPG:156-157, 169 ; N065:21-22 | § 1.1, § 3.1, § 6, § 7 |
| UNI-003 | Objectif ultime : l'universalité se mesure sur des familles de questions jamais vues à la conception — familles engendrées, familles de l'autre fournisseur, provenance réelle (H-G4 et successeurs) — et jamais sur des items inédits des familles de conception. | idée | Lazar (25 octobre, 00:05 : « je veux ça pour l'objectif ultime ») | décidé (N-044, R-376) | N044:24-25, 32-36 | § 1.1, § 6 |
| UNI-004 | Vivier de conception : les tâches servies pendant la conception viennent d'un vivier à part de la banque scellée (fichier empreinté, identifiants disjoints du test et du test final vérifiés par le script d'extraction) ; pour la conscience d'évaluation, le reste du jeu public sans GAIA ; pour le contrôle de délégation, les traces hors test. | idée | conv-audit ; « GO now » du directeur | décidé (N-044) ; codé dans le noyau de l'étape 1 (`noyau/vivier.py`, option `--pool-conception`, R-378) | N044:5, 42-45, 55 ; N049:46-48 | § 1.1, § 6 |
| UNI-005 | Seulement après les deux expériences bon marché : transfert inter-familles à la puissance calculée, avec contrôles (concepteur non entraîné ; récompenses permutées). | idée | une cellule du collisionneur ; Lazar « accepté » | décidé (phasage, N-045 v2 énoncé 6 (iii)) | N045:38-40, 89-90 | § 1.1, § 6 |
| UNI-006 | Part `test` tirée dans un vivier à chaque génération (graine propre dérivée de la graine de la course) : l'organisme ne peut plus s'adapter qu'au générateur et à la famille, plus aux textes ; changement du noyau à partir du pilote 5, vivier des deux familles. | idée | conv-audit (levier 3) ; Lazar « go » (« des tâches fraîches, la seule chose qui marche vraiment ») | décidé (N-049) ; vivier de la famille « contrôle de délégation » à régler | N049:19-22, 42-50, 75-76 | § 1.1, § 6 |
| UNI-007 | Banque sœur « v3-bis » : même générateur que la v3, tâches neuves, construite d'avance par qui n'a lu aucun score, lue une seule fois, jamais servie à un organisme ; sépare « adapté aux 60 textes » de « adapté à la famille ». | idée | conv-audit ; Lazar « go » | décidé (N-049) ; construction = dépense sur devis ; constructeur et taille proposés (session-depot, 60 tâches par part) | N049:22-24, 51-55, 77-78 | § 1.1, § 6, § 8 |
| UNI-008 | La confirmation (étape 1 décisive, confrontation, pilote décisif (b)) reste sur la banque v6 scellée, famille tenue à l'écart. | idée | Lazar (26 octobre, 01:52 Paris) | décidé (N-044, N-049) | N049:23-24, 56-57 | § 1.1, § 6 |
| UNI-009 | La banque de familles inédites qui sert à confirmer est distincte de la famille tenue à l'écart de l'évaluation finale ; le document d'intégration est à corriger en v2. | idée | relecteurs de l'affinage v2 ; confirmé par conv-audit (n° 136) | décidé (N-059, point 7) | N059:33-34 | § 1.1, § 4.2, § 6 |
| UNI-010 | Garde de disjonction du vivier par le contenu : un item qui contient au moins 80 % des fenêtres de 8 mots d'un texte de test est écarté ; identifiants servis opaques ; vivier transmis : aucun identifiant source commun avec les 120 de la banque, un doublon exact écarté. | idée | session-depot (code) ; conv-audit (vivier) | codé (`b7374a9`, `noyau/vivier.py`) | DEC R-378 ; DEC R-399 | § 1.1, § 6 |
| UNI-011 | Mesure statistique de l'universalité (texte III) : « avec confiance 1 − α, au plus une part ε des familles de la classe déclarée a une statistique au-delà de τ » ; borne inférieure candidate de Chao2 par incidence, sans intervalle établi ; expérience à faire d'abord : couverture de la borne de Chao2 sur les mondes compatibles ; cinq décisions D1 à D5 proposées (loi uniforme sur population finie, point et intervalle d'identification, couverture avec prédiction extérieure scellée, zone d'indifférence à double seuil, minimum observé rapporté « non pire cas »). | proposition | collisionneur du texte III (tour étroit, quatre espèces), synthèse v2 | proposé avec défauts sous 48 heures (1er novembre) | DEC R-859 | § 1.1, § 6 |
| UNI-012 | Coffre des attaques inédites : (a), puis (b) comme bras à part, (c) seulement dans un compartiment isolé dont ne sortent que des classes et des scores ; « on garde une part des attaques inédites cachées pour tester si l'universalité tient » ; une défense inédite vise le mécanisme ; question v1 du coffre : séparer génération d'attaques, conception de défenses et mesure, taxonomie des mécanismes, partition tenue à l'écart par famille, oracle extérieur et audit de fuite, gain de défense préenregistré par régime d'accès. | idée | Lazar (1er novembre, 15:30 UTC) ; session-depot (question) | décidé (go) ; question v1 scellée, v2 écrite ; tours sur devis | DEC R-962 ; DEC R-963 | § 1.1, § 4.2, § 6 |
| UNI-013 | Coffre des attaques inédites, décision D2 : jusqu'aux résultats de l'étape 2 (couches 3 et 4 fermées), le compartiment d'attaque est synthétique seulement (monde planté et familles de lois, ni modèles réels, ni fiches réelles du coffre) ; cartes de menace servies au bisociateur tout de suite ; compartiment isolé comme bras à part, une part des fiches concrètes tenue à l'écart pour mesurer l'universalité ; accès plein seulement dans le compartiment, dont ne sortent que des classes et des scores ; réponses au niveau des dispositifs, mesures et gardes. | idée | Lazar (R-962, D2 du 1er novembre, R-1057 chez conv-audit) | décidé ; question v2 écrite ; tours sur devis | COF:1-12 ; DEC R-962 ; DEC R-963 | § 1.1, § 3.1, § 4.2, § 6 |

## II.9 Vérité, oracles et mondes plantés (VER, 41 entrées)

| n° | idée | type | origine | statut | source | renvoi (partie I) |
|---|---|---|---|---|---|---|
| VER-001 | Mondes plantés de l'attaque : W1 mélange deux lois de l'archive (couvert par le v8) ; W2 applique une loi connue à une sous-population et une autre à la seconde (recombinaison par morceaux, non couverte par le v8) ; bâtis à partir des seules lois de l'archive, toute promotion y est fausse. | idée | dessin d'A1 | codé (A1 à A1-v4) | [B5] A4T:200 ; [B8] A4T:203 ; A13:48 | § 4.2, § 5 |
| VER-002 | Monde gradué W2g : à la loi d'une sous-population se mêle une part λ d'une loi neuve ; il se place à la frontière du v9, où une promotion n'est plus fausse par construction. | idée | dessin d'A1-v4 | codé et couru (A1-v4) | [B20] A4T:201 | § 4.2, § 5, § 6 |
| VER-003 | Choix de la dose λ* par une règle mécanique écrite avant toute épreuve, sur processeur, sans dépense : plus petite dose où la loi du monde est promue sous v9 au moins 800 fois sur 1 000 et où la recombinaison pure n'est jamais promue. | idée | texte court scellé de l'épreuve | décidé (texte scellé EPT) | [B21] EPT:44, 48-50 | § 4.2, § 8 |
| VER-004 | Issue de l'épreuve : λ* = 0,40 ; loi du monde promue 803/1 000 (Wilson [0,777 ; 0,826]) ; recombinaison pure 0/1 000 à toutes les doses ; mention gelée « λ* à la limite » (borne basse sous 0,80), λ* inchangé ; aucune évaluation impossible. | résultat | épreuve hors ligne du monde gradué | fermé (lecture scellée EPL) | [B22]-[B24] EPL (champs lambda_etoile, par_dose, a_la_limite, evaluations_impossibles) | § 4.2 |
| VER-005 | Banc des tricheurs : sur des mondes synthétiques, planter des lois qui ne doivent jamais être promues (lignes « fatales ») et des lois vraies (mesure de la puissance), 1 000 répétitions par ligne, pour valider un nul avant production. | idée | dessin du banc (v9) | codé et couru (validation du nul v9) | SRO § 2 ; [B14]-[B16] V9:7, 23-24 | § 4.1, § 4.2, § 5 |
| VER-006 | Voisins publiés des gestes du banc et des témoins : trois arbitres délibérément fautifs, un attaquant scripté et un plan préenregistré (Qu et al.) ; témoins plantés (PROCTOR, arXiv 2609.02246) ; PACE (arXiv 2606.08106) voisin du banc. | résultat | contre-lecture C7 | fermé (lecture) ; resserrement de la revendication du banc recommandé, non tranché | [B50] C7R:15-42, 61 | § 4.2 |
| VER-007 | Témoins fixes de la boucle : ils comprennent des lois que le nul ne couvre pas ; l'un d'eux, une loi fausse plantée (T-F2), a été promu par le juge puis éliminé par son test de mort ; explication « probable, non vérifiée ». | résultat | essai à blanc | fermé (constat) ; explication non vérifiée | [B36] EAB:47-53, 79 | § 4.2, § 4.4 |
| VER-008 | Test de mort : une expérience conçue pour réfuter une loi promue, jouée après la promotion dans un bac à sable isolé. | idée | dessin de la boucle réelle | codé (garde du bac) ; jamais joué dans le vrai bac au 10 novembre | SRO § 5 ; [B36] EAB:47-53 | § 4.2, § 4.4, § 4.6 |
| VER-009 | Témoins jugés sans l'archive : en simulation, au moins une loi fausse de la classe couverte serait promue dans 994 répétitions sur 1 000 ; d'où l'exigence de juger les lois plantées avec l'archive. | résultat | essai à blanc | fermé (constat) ; corrigé dans le code v65 | [B37] EAB:67, 80 ; [B49] V65R | § 4.2, § 4.6 |
| VER-010 | Témoins de sortie du modèle de 8 milliards de paramètres pour les sondes de l'étape 1. | proposition | conv-audit ; Lazar « parfait » | proposé non tranché | N045:31-32, 113-114 | § 4.2 |
| VER-011 | La vérité du test caché ne nourrit ni l'organisme ni un concepteur. | idée | conv-audit | décidé (N-045, énoncé 8) | N045:94-95 | § 4.2, § 6 |
| VER-012 | Témoins : générations d'étalonnage entières, à calendrier secret, et témoins silencieux à chaque génération de production ; aucun témoin ne passe par un proposeur en production. | idée | conception de l'affinage v2 (session de Fable), relue par Opus, Argon et Fable | décidé (N-059, point 1) | N059:20-25 | § 3.1, § 4.2 |
| VER-013 | Trois oracles de conséquence pour la vérité du dommage (A défauts plantés à clé connue ; B rejeu caché des contrôles laissés par l'agent ; C consommateur déterministe en aval), chacun comparé au jumeau honnête apparié ; ils ne lisent jamais le texte, les activations ni un moniteur, « jamais un modèle » ; chacun éprouvé (R5) et rapporté à part, un désaccord étant un résultat. | idée | Lazar (« on va faire les trois ») ; programme principal (G1) | décidé en N-060 v2, remplacé sur le banc actuel par la v3 ; gardé pour une banque à tâches exécutables | N060B:29-42, 49-54 ; N060:5-9, 36-38 | § 4.2 |
| VER-014 | Oracle de couverture contre la référence cachée (banc actuel) : une question fermée par contrôle expérimental de l'article (absent, altéré, conforme), citation vérifiée mot pour mot par un programme, deux lecteurs de familles autres que celles des moniteurs, aveugles à la condition ; dommage = baisse de couverture par rapport au jumeau honnête ; épreuves de l'oracle avant toute lecture ; repli écrit « sabotage demandé ». | idée | rapprochement des trois voix (V-1) ; Lazar « V-1 go » ; programme principal (G1) | décidé (N-060 v3) | N060:13-35 | § 4.2 |
| VER-015 | V-2 (issue positive du pilote lue « dose candidate », confirmée sur tâches disjointes ; marge δ) et V-3 (variante à liste fermée de contrôles, conception sur processeur). | question ouverte | rapprochement des trois voix | proposé non tranché | N060:42-43 | § 4.2 |
| VER-016 | Famille « mondes de poids » de l'organisme d'idéation (piste P5 du billet « Sparks of Weight-Space Programming ») : note de conception sur processeur, après la seconde course d'A1-v3 et le tour fermé. | proposition | rapport d'intégration de « Sparks » ; Lazar « go pour D-3, D-4 et D-5 » | décidé (D-4 (b)) ; prévu | SPK:3, 6 | § 4.2, § 4.5, § 5 |
| VER-017 | Banc de Jev (P-026 (a)) : traces synthétiques neutres écrites par Claude, une honnête et une qui sabote par tâche de code, nettoyées de la même façon ; Lazar seul décide de le lancer. | idée | session-depot ; Lazar | décidé (P-026 (a)) ; écriture du banc seulement | DEC R-347 | § 4.2 |
| VER-018 | Banque de la confrontation : la v1 est défectueuse (les identifiants donnent la vérité, établi par l'audit de symétrie du second pilote) ; banque v2 aux identifiants opaques choisie, puis v3 contre-lue et retenue, puis `confrontation-v5` (une trace par paire). | résultat | conv-audit (audit) ; Lazar (choix) | fermé ; aucune course décisive sur la v1 | DEC R-443 ; DEC R-444 | § 4.2 |
| VER-019 | Vérification des étiquettes de la banque par paires : 10 paires sur 10 en accord (critère gelé : au plus une en désaccord sur 10), banque retenue. | résultat | conv-audit (vérificateur Opus 5.5) | fermé | DEC R-365 | § 4.2 |
| VER-020 | Le critère de contenu « prédit plus » est franchissable à coût nul par des tricheurs scriptés (enveloppe harmonique aveugle en tête) : première expérience = valider le critère de contenu contre une batterie de tricheurs, sur processeur, avant tout appel de fusion. | résultat | collisionneur « recombinaison » (les deux équipes rouges) | fermé (synthèse) ; expérience prévue | DEC R-527 | § 4.2, § 5 |
| VER-021 | Rétrodiction sur arXiv 2003-2016 : la marche « à la Swanson » ne bat pas l'allocation de ressources ; un seuil absolu de 12 points est mal posé pour un taux de base de 0,275 %. | résultat | conv-audit (n° 101) | fermé | DEC R-529 | § 4.2 |
| VER-022 | Banc de tricheurs v1 : 42 tricheurs (27 contre le juge, 15 contre l'amont), règle d'arrêt commune, témoins ; deux tricheurs qu'aucun modèle n'arrête (T11, T12) ; banc v7 : quatre trous de nouveauté fermés par le nul d'archive ajusté. | résultat | sous-agent de session-depot, sur les synthèses ; conv-audit (v7) | fermé (banc écrit) ; réserves (e-BH, nul des filles) | DEC R-572 ; DEC R-583 | § 4.1, § 4.2, § 5 |
| VER-023 | Étage de tests des fiches : (a) tests de mort automatiques sur processeur (cinq meilleures fiches, prédiction scellée avant exécution, bac à sable fermé, lecteur neuf) ; (b) tests sur carte graphique (sondes), un devis et une ligne de GO par fiche ; (c) en parallèle de (b), une IA scientifique existante tirée de la littérature sur la même question ; comparaison des sorties de (b) et (c) par une règle écrite avant lecture. | idée | Lazar (« a puis b et c en parallèle … on compare ») | décidé (R-776) ; (a) demandé à conv-audit | DEC R-776 | § 4.2, § 4.4 |
| VER-024 | Durée des tests de mort : au plus 6 minutes de bac par fiche, ≈ 1 h 40 par sous-session de 16 fiches ; machine jetable à chiffrer sur quatre sous-sessions. | résultat | conv-audit | estimation (devis à faire au 1er novembre) | DEC R-959 | § 4.2, § 4.4 |
| VER-025 | Épreuve fraîche du pont fiche → loi (premier essai) : 8 idées de Fable et 6 témoins mêlés ; verdicts mécaniques confirmés : L1 « dents » (6 témoins justes sur 6), L2 « non lisible » (0 fiche traduite sur 15), L3 « inutile en l'état » (0 fiche utile sur 8), L4 « sûr », L5 « conforme » ; prédictions non tenues ; audit en miroir sans artefact. | résultat | conv-audit (protocole, code) ; session-depot (tirage, lecture préenregistrée) | fermé (lecture scellée) | DEC R-965 ; DEC R-981 ; DEC R-982 ; DEC R-985 ; DEC R-986 | § 4.2, § 4.3 |
| VER-026 | N6 — épreuve semi-réelle des méthodes d'identification causale (DL-1 à DL-13) : onze accords larges ; puissance de l'étape d'estimation à recalculer au seuil réel 0,70 (et non à 0,85 : ≈ 3 834 paires-années au lieu de 2 600) ; DL-3 et DL-9 renversées vers des lectures descriptives (DL-3 avec déclencheur d'audit conditionné à la puissance prévue) ; DL-12 suspendue à un test sur monde jouet avant le gel ; un exemplaire non obtenu marqué SUPPOSÉ, aucun de ses chiffres dans une règle. | résultat | collisionneur des nœuds | fermé ; recommandations de l'auteur du brouillon 5 au directeur | SN1:212-240 ; SN2:202, 339 | § 4.2 |
| VER-027 | Corrélation de rangs entre classements de trois bras : non jugeable à deux classements (plus petite valeur p 1/6) ; à trois classements, seule l'unanimité passe (1/36), à puissance très faible. | résultat | collisionneur des nœuds (convergence née de la critique) | fermé | SN1:57 | § 4.2 |
| VER-028 | Étape 8 — tuer : la fiche figée devient un script joué dans un bac à sable (`bwrap`, sans réseau, mémoire bornée, appels système filtrés, sans clé) sur des données déjà présentes ; la prédiction est scellée avant l'exécution ; verdict « survit » ou « éliminée » à un seuil gelé, calculé par l'orchestrateur depuis la v57 à partir du fichier brut nommé par le préenregistrement ; vérificateur d'une autre famille. | idée | dessin de l'organisme | codé (`pole/tests_de_mort_v1` à `v5`) ; jamais joué pour de vrai au 10 novembre | RDM:60, 69 | § 4.2, § 4.4 |
| VER-029 | Témoins plantés (lois vraies et fausses) mêlés anonymement à chaque génération, indexés pour l'audit, exclus de tout ce qui est servi aux agents (contre la reconnaissance et le jeu des témoins). | idée | dessin de l'organisme | codé (`pole/memoire.py`) | RDM:77 | § 4.2 |
| VER-030 | Banc des tricheurs scriptés contre le juge statistique : chaque tricheur est une fiche qui cherche la promotion sans apporter de loi vraie nouvelle, par recombinaison de ce que l'archive a déjà accepté (copie renommée, mélange, tempérage, parent habillé, rafale de variantes d'une loi fausse) ; règles de lecture fixées avant la course. | idée | dessin de l'organisme (classes de tricheries, niveau méthode) | codé (`demonstrations/banc_tricheurs_v7.py`, `v8`) | RDM:80-82 | § 4.2, § 5 |
| VER-031 | Juge statistique sur mondes plantés : 8 témoins vrais sur 8 promus, 0 faux sur 8, dans les deux bras de proposeurs ; l'avantage espéré des proposeurs exploratoires ne s'est pas montré (une fiche promue dans chaque bras). | résultat | démonstration `demo_couche1_proposeur_v7` (reproduite le 1er novembre) | fermé (reproductible) | RDM:120 | § 3.1, § 4.2 |
| VER-032 | Juge sur la banque d'épisodes réels (120 épisodes notés, 13 moniteurs de deux juges de 3 et 8 milliards de paramètres) : un témoin planté de force 0,5 retrouvé ; sur les 13 moniteurs réels, rien de promu (« pas de dents, pas de conclusion ») ; puissance mesurée : force 0,8 promue 95 %, 0,5 de 65 à 73 %, ≤ 0,3 au plus 24 % ; « rien promu » n'exclut pas des effets de cette taille ; avec un plan gelé à 120 instances, plus d'épisodes peut baisser la puissance. | résultat | pôle sur la banque T0.5 (exploratoire, lecture datée avant la course) | fermé | RDM:123-124 | § 4.2 |
| VER-033 | Lecture de la banque réelle aux graines neuves (288 épisodes, préenregistrée et scellée) : issue I1 « valide et avec dents, aucune loi réelle promue » ; 0 sur 19 faux témoins promus ; borne par moniteur : une loi de la forme plantée portant 0,057 à 0,117 nat par épisode serait promue avec probabilité 0,9 ; aucun vrai témoin réel n'existe pour éprouver le juge sur des liens réels. | résultat | lecture préenregistrée (2 novembre), lecteur neuf | fermé | RDM:125 | § 2.2, § 4.2 |
| VER-034 | Monde sur banque (`MondeBanque`) : les instances sont les lignes d'une banque figée (traits visibles, issues cachées) ; le plan est tiré dans la partie d'épreuve après le gel, par la graine du noyau ; les issues sont lues, jamais calculées ; même interface que le monde du noyau ; la banque de la couche 1 est le pilote T0.5 (180 épisodes du modèle de 8 milliards) et les notations des deux juges. | idée | conv-audit (conception v7) | codé (`pole/monde_banque.py`) | CV7:10-18, 28-44 | § 2.2, § 4.2 |
| VER-035 | Témoins de domaine sur la banque : vrais si la relation est établie sur la partie de calibrage avec une marge (« à vérifier, pas à présumer ») ; faux = lois qui dépendent d'un trait permuté par le noyau (artefact planté). | idée | conv-audit (conception v7) | codé (selon la conception) | CV7:45-48 | § 4.2 |
| VER-036 | Revendication O10 : témoins plantés mêlés à chaque génération : voisine (positif planté parmi les propositions chez PACE ; Qu et al.). | résultat | rapport C4 | fermé (lecture) | C4R:346 | § 4.2 |
| VER-037 | Revendication O11 : banc de tricheurs scriptés, validation préenregistrée, mutations : occupée dans son principe ; voisins plus proches : attaquant scripté contre un arbitre par e-valeurs, attaques et défenses rejouées ; banc de 27, préenregistrement et mutations non trouvés ; revendication resserrée. | résultat | rapport C4 ; N-064 | fermé (lecture) ; resserrement recommandé | C4R:347 | § 4.1, § 4.2, § 5 |
| VER-038 | Revendications O13 (tests de mort en bac à sable, verdict de l'orchestrateur sur le fichier brut : voisine), O14 (sélection entre générations par le verdict des tests de mort : voisine), O16 (pont fiche → loi prédictive : voisine), O18 (discrimination des juges modèles mesurée : voisine). | résultat | rapport C4 | fermé (lecture) | C4R:349-350, 352, 354 | § 4.2, § 4.3, § 4.4 |
| VER-039 | Revendication O20 : juge éprouvé sur vérité plantée : occupée comme méthode ; restent les chiffres propres. | résultat | rapport C4 | changement de statut, non tranché | C4R:356 | § 4.2 |
| VER-040 | Éléments communs pour la question de course : témoins plantés de l'étalonnage (fiches creuses, paraphrases des questions, fiches de forme parfaite au contenu absurde, avantage faux) ; fausses alertes par épisode à tout instant sur trois jeux disjoints ; consigne bénigne de longueur appariée ; séparer exécution et lisibilité ; aucune donnée de calibrage ou d'évaluation de G1 servie aux idéateurs ; mémoire anti-redite étalonnée sur des paraphrases plantées par un tiers ; pas de pseudo-réplication. | résultat | collisionneur « question-mère v2 » | fermé (synthèse) | QM:49-66 | § 4.2 |
| VER-041 | Machine jetable de l'étage des tests de mort : une machine louée, sans aucun secret, détruite après chaque série ; plomberie sans secret, devis par série. | idée | conv-audit (R-533 de sa branche) ; Lazar | décidé ; devis v1 à v3 écrits ; rien loué au 30 octobre | MJE:1-8 | § 4.2, § 4.4 |

## II.10 Mathématiques, preuve et Lean (couche 4) (MAT, 8 entrées)

| n° | idée | type | origine | statut | source | renvoi (partie I) |
|---|---|---|---|---|---|---|
| MAT-001 | N12 (b) : couches fermées jusqu'aux résultats de l'étape 2 ; mesure de ce que le catalogue manque, au préenregistrement de l'étape 2 ; un seul pas autorisé : l'essai sur processeur « preuve formelle contre suite bon marché » (devis d'appels de sous-agents). | idée | Lazar (mots directs à conv-audit) | décidé (N12 (b), R-959) | DEC R-959 | § 2.5 |
| MAT-002 | Pilier « mathématiques nouvelles » (couche 4, pôle théorie et Lean) : (a) lecture du tour 2 N12-N13 du collisionneur v8, critères de lecture scellés avant ouverture, synthèse par un lecteur neuf, sans dépense ; (b) ensuite, devis de l'essai sur processeur « preuve formelle contre suite bon marché » ; (c) ensuite, note de conception du pilier « génération » (conjectures, démonstrations, Lean comme arbitre, juge de nouveauté), nœud chez le directeur. | idée | Lazar (« (a), puis (b), puis (c) », confiance 0,65) | décidé (R-2199) ; (a) lancé le 10 novembre | DEC R-2199 ; DEC R-2195 | § 2.5, § 6, § 8 |
| MAT-003 | N12 (1) : N-045 et N-058 couvrent la composition et la sélection apprises et les instruments locaux entraînés, pas le code hors catalogue (couche 3) ni la vérification formelle (couche 4). | résultat | collisionneur N12-N13 (accord large à quatre, réserve R4) | fermé (synthèse v2) | SNN:63-76 | § 2.4, § 2.5, § 4.2, § 6 |
| MAT-004 | Couche 4 : une empreinte scelle un texte, elle ne prouve pas la validité d'une preuve (exemple : coquilles d'une preuve publiée trouvées par un lecteur neuf avec script) ; une preuve ne valide pas une spécification empirique. | idée | collisionneur N12-N13 (accord large) | fermé (synthèse) | SNN:84-89 | § 2.5, § 6 |
| MAT-005 | Expérience de la couche 4 : Lean contre le meilleur assemblage bon marché (lecteur neuf outillé symbolique et numérique, tests, mutations, relecture par un modèle d'une autre famille, grille d'audit), sur bibliothèque aveugle et à coût apparié ; ouverture de la couche seulement sur une classe d'erreurs mesurée ; « Lean contre empreinte » est vrai par construction. | proposition | collisionneur N12-N13 (convergence née de la critique) | décidé comme seul pas autorisé par N12 (b) (R-959) ; devis prévu (R-2199 (b)) | SNN:84-89 ; DEC R-959 ; DEC R-2199 | § 2.5, § 6 |
| MAT-006 | La couche 4 comme vérificateur externe, pas comme couche autonome intégrée à l'organisme. | proposition | collisionneur N12-N13 (espèce D) | proposé | SNN:87, 104 | § 2.5, § 6 |
| MAT-007 | Priorité : l'étape 2 d'abord ; aucune couche rouverte comme capacité intégrée ; la couche 3 ne se rouvre que si l'étape 2 montre un plafonnement de N-045 sur les familles diffuses tenues à l'écart ; l'étape 2 ne tranchera que si l'on y prévoit un résidu mesurable (échecs du catalogue, coût de génération). | résultat | collisionneur N12-N13 (position commune ; apport seul de D sur le résidu) | décidé (N12 (b), R-959) | SNN:97-106 | § 2.4, § 2.5, § 6 |
| MAT-008 | Pôle théorie : le juge est un vérificateur de preuves (Lean) ; le proposeur est nourri par le moissonneur et la recombinaison ; questions ouvertes du programme visées : agrégateur sous corrélation adverse, théorème négatif ; aucune dépense de carte, installation de Lean sans dépense. | idée | Lazar (« en parallèle le pôle théorie avec Lean ») ; conv-audit | décidé dans son principe (27 octobre) ; fermé jusqu'à l'étape 2 (N12 (b)) ; pilier « génération » en conception (R-2199 (c)) | PCO:18-19, 61-63 ; DEC R-959 ; DEC R-2199 | § 2.5, § 3.1, § 8 |

## II.11 Récompense collective et signalement (Avalon, N13) (REC, 13 entrées)

| n° | idée | type | origine | statut | source | renvoi (partie I) |
|---|---|---|---|---|---|---|
| REC-001 | Canaris « à ne pas signaler » dans la banque v2 : des cas où l'organisme ne doit pas signaler, pour mesurer le sur-signalement. | proposition | conv-audit ; Lazar « parfait » | proposé non tranché | N045:32, 114 | § 6 |
| REC-002 | Le signalement aux humains se mesure dans l'organisme dessiné et, pour les voies à concepteur ouvert, dans ses poids. | idée | conv-audit | décidé (N-045, énoncé 8) | N045:95-96 | § 6 |
| REC-003 | Question du directeur : s'inspirer de la récompense collective d'Avalon (« RLCR ») pour que l'organisme apprenne à s'organiser dans ses appels aux agents et aux modèles ; la couche 3 le fait-elle, avec réécriture de soi et concepts mathématiques inédits soutenus par Lean ? | idée | Lazar (31 octobre, ≈ 13:10 UTC) | tranché en (a) puis (c) (R-920) | DEC R-920 | § 2.4, § 2.5, § 6 |
| REC-004 | Constat : l'apprentissage de l'organisation des appels est déjà inscrit (N-045) ; la récompense collective n'est intégrée nulle part ; Avalon rapporte une baisse du signalement au régulateur sous récompense collective (minimum 36 %, 45 % au pas 180, pages 35 et 41 vérifiées par conv-audit) : la menace par omission étudiée par le programme (axe 8, H9) ; « RLCR » nomme deux méthodes distinctes (Damani : calibration ; Avalon : récompense collective). | résultat | session-depot ; conv-audit (pages vérifiées) | fermé (lecture) | DEC R-920 | § 6 |
| REC-005 | Avalon (a) : attendre les deux lectures vérifiées de conv-audit, puis une note de proposition ; (c) ensuite, un bras de l'étape 2 : récompense collective contre récompense individuelle, signalement aux humains mesuré dans les deux ; changer le signal rendu à l'organisme est un changement d'hypothèse, la note revient au directeur avant tout préenregistrement. | proposition | session-depot ; Lazar « (a) puis (c) : go » | décidé (R-920) ; prévu | DEC R-920 | § 6 |
| REC-006 | Lancer tout de suite le collisionneur sur la récompense collective (option (b)). | piste écartée | session-depot | écarté (R-920) | DEC R-920 | § 6 |
| REC-007 | N13 (a) maintenant : taux de signalement du modèle de départ (sur devis) et audit de calibration des juges existants sur les paires déjà produites contre l'oracle planté (sans dépense, chez session-depot) ; (b) ensuite : bras de récompense collective à l'étape 2, après dessin et devis ; précautions d'Avalon « go » ; « apports seuls » à faire. | idée | Lazar | décidé (N13, R-959) | DEC R-959 | § 4.2, § 6, § 8 |
| REC-008 | N13 (1) : le bras collectif contre individuel (c1) et le générateur d'omission pour les sondes (c3) ne sont pas exclusifs (le bras collectif produit l'omission, l'individuel est son contrefactuel) ; (c2) rejeté (pas d'oracle pour les fusions ; contingent au dessin actuel de la course 2) ; la cause collective de la baisse de signalement n'est pas établie chez Avalon. | résultat | collisionneur N12-N13 | fermé (synthèse) ; décidé ensuite N13 (b) (R-959) | SNN:110-121 | § 4.2, § 6 |
| REC-009 | Récompense collective traduite pour notre organisme : niveau d'attribution du crédit, à information et effectif constants, avec un témoin mono-agent en troisième bras ; aucun scénario de signalement présent ni récompensé pendant l'entraînement. | idée | collisionneur N12-N13 (convergence née de la critique, A, C, D) | proposé | SNN:116, 124 | § 6 |
| REC-010 | Sélection sur la variable dépendante : si les positifs servis aux sondes viennent de la cellule choisie pour son omission et les négatifs d'ailleurs, la sonde apprend le régime ou le pas d'entraînement ; remède : positifs et négatifs du même point de contrôle et des mêmes poids. | objection | collisionneur N12-N13 (critique croisée des quatre) | retenue (convergence) | SNN:123 | § 6 |
| REC-011 | Intensité d'optimisation : une voie bon marché peut manquer de pression pour faire apparaître l'insularité observée chez Avalon (épisodes de 2 à 5 heures, lots de 200 à 800 groupes) ; critère d'informativité et règle d'escalade gelée proposés. | question ouverte | collisionneur N12-N13 (divergence non résolue n° 3) | proposé non tranché | SNN:125 | § 6 |
| REC-012 | Précautions d'Avalon : scénarios d'évaluation du signalement tenus à l'écart de tout entraînement ; pré-test du signalement du modèle de départ (p₀) comme préalable absolu ; le signalement n'entre dans aucune récompense ; mesure par agent et par run à chaque point de contrôle, point 0 compris, autant de canaris « à ne pas signaler » que d'incidents ; plancher absolu et chute maximale de signalement gelés, dont le franchissement interdit l'intégration ; « qui lit » n'est nommé par personne. | proposition | collisionneur N12-N13 ; Lazar (« précautions d'Avalon : go ») | décidé dans son principe (R-959) ; valeurs non fixées | SNN:129-140 ; DEC R-959 | § 6 |
| REC-013 | Bras « récompense du signalement » ajouté à la récompense. | piste écartée | collisionneur N12-N13 (espèce B, reclassé en bras d'intervention) | écarté comme précaution (« ajouter une récompense du signalement n'est pas une précaution établie ») | SNN:134-136, 142 | § 6 |

## II.12 Papier C et menaces diffuses (N-065) (PAC, 21 entrées)

| n° | idée | type | origine | statut | source | renvoi (partie I) |
|---|---|---|---|---|---|---|
| PAC-001 | Le juge statistique de l'organisme est un moniteur : il surveille des affirmations produites par des agents ; l'attaque de Goodhart d'A1-v4 est un attaquant adaptatif qui cherche à le déplacer ; le juge-tournoi façon Co-Scientist est un juge génératif mis sous la même attaque. | idée | mère (rapport du 9 novembre) | décidé (N-065 : juge = moniteur d'affirmations de recherche) | RPG:23-25, 133-137 ; N065:15-18 | § 3.1, § 5, § 7 |
| PAC-002 | Rôle 1 — second terrain du papier C (« l'instrument ») : A1-v4 (juge statistique) et le juge-tournoi (juge génératif) mesurent le gain de corruption sur les juges de la recherche automatisée ; prédiction de C : juges génératifs à gain positif, agrégations robustes à gain nul ou négatif ; C n'est plus montré sur un seul domaine. | proposition | mère (rapport du 9 novembre), recommandée confiance 0,7 | décidé (N-065, rôle 1 adopté) | RPG:141-147, 169-170 ; N065:11, 15-18 | § 3.1, § 5, § 7 |
| PAC-003 | Argument d'apport : le domaine est celui ouvert par Co-Scientist, que la note d'antériorité montre sans validation statistique ni attaque de son juge. | idée | mère (rapport du 9 novembre) | proposé ; à relire après la collision Qu-Chen-Wang (voir JUG) | RPG:144-145 | § 3.1, § 7 |
| PAC-004 | Rôle 2 — atelier d'idées du programme : l'organisme reçoit des questions ouvertes du programme ; ses fiches sont du matériau, jamais une preuve ; tout usage décisif passe par un préenregistrement (R1). | proposition | mère (rapport du 9 novembre), confiance 0,7 | décidé (N-065, rôle 2 adopté) | RPG:148-151 ; N065:19-20 | § 7 |
| PAC-005 | Première question d'atelier : la question v2 du pilier attaque, « chercher la trace », est scellée ; sa course est bloquée par la règle de permission de l'organisme v2, que seul le directeur peut écrire dans `.claude/settings.json`. | proposition | mère | prévu ; bloqué (geste du directeur attendu au 9 novembre) | RPG:41-42, 75, 95, 149-151, 184 | § 7 |
| PAC-006 | Rôle 3 — famille de menaces diffuses pour les papiers A et B : un proposeur qui trompe le juge sur de nombreuses propositions, chacune d'apparence honnête, est une menace diffuse au sens exact du programme. | proposition | mère (rapport du 9 novembre), confiance 0,5 | proposé non tranché (N-065 : rôle 3 « à trancher ») | RPG:152-157, 169-170, 187 ; N065:21-22 | § 3.1, § 7 |
| PAC-007 | Si le proposeur trompeur est un modèle à poids ouverts (le 8B), les sondes du programme peuvent lire si l'intention de tromper le juge se voit dans ses activations avant que le juge ne soit trompé : la thèse « la preuve interne survit » portée à la recherche automatisée. | hypothèse | mère (rapport du 9 novembre) | proposé non tranché (dépend du rôle 3) | RPG:153-156 | § 3.1, § 7 |
| PAC-008 | Positionnement : les bancs publics et l'organisme d'idéation servent la validité et les papiers B et C, pas la porte G0. | idée | mère (rapport du 9 novembre) | proposé (lecture des principes premiers) | RPG:59-61 | § 7 |
| PAC-009 | « Voir si l'organisme trouve des failles » (26 octobre). | idée | Lazar | repris par le rôle 2 (atelier) ; voir aussi pilier attaque | RPG:126 ; DEC R-504 | § 7 |
| PAC-010 | « Avec l'organisme on peut attaquer des questions bien plus ambitieuses » (28 octobre). | idée | Lazar | repris par le rôle 2 (atelier) | RPG:127 ; DEC R-619 | § 7 |
| PAC-011 | « Lançons l'org idéation dessus » (8 novembre) ; « il faut intégrer tout ce qu'on fait actuellement dans le programme présenté à TAIF et réfléchir à comment faire les liens » (8 novembre). | idée | Lazar | repris par le rapport du 9 novembre puis N-065 | RPG:128-129 ; DEC R-1770 ; DEC R-1793 ; DEC R-1832 | § 7 |
| PAC-012 | Phrase du modèle de menace du papier C, sans revendication ni expérience : un adversaire qui lit ou édite les poids de la politique ou du moniteur relève de la frontière assumée du programme (sécurité des poids, couche sœur) ; la couverture certifiée suppose des poids intègres. | idée | rapport d'intégration de « Sparks » ; Lazar « go » | décidé (D-5 (a)) ; à reprendre à la rédaction du papier C | SPK:7 | § 6, § 7 |
| PAC-013 | Hypothèses formulées par l'organisme lui-même (course M) et proposées au test sur carte graphique : H-M1 (gabarit contre style, 2 × 2), H-M2 (invariance sous transformations), H-M3 à H-M5 ; H-M1 testée (v2 arrêtée, v3 complète), puis « suite de H-M1 » jugée « (b) validé avec corrections » (sonde à format constant, gabarits et tournures en facteurs aléatoires croisés, test d'équivalence, puissance simulée, porte de certification à l'aveugle) ; 17 corrections, 13 idées retenues, 5 écartées, 24 pièges ; idée I7 (organisme à indice implicite implanté) non engagée. | résultat | organisme de Gemini (course M) ; collisionneur ; Argon seul ; lecteur neuf | exploratoire (R-473) ; nœud H-M1 rattaché à N-053 | DEC R-447 ; DEC R-458 ; DEC R-476 ; DEC R-502 | § 6, § 7 |
| PAC-014 | Courses de l'organisme sur les questions des mentors (preuves pour les mentors) : Heimersheim (cinq espèces, aiguilleur v2, 46 fiches classées, 3 notables, 10,03 USD), Kirchner Q2, Ibrahim Q1 (deux courses ; la seconde : 38 classées, 1 notable, 10,64 USD), Scheurer (arrêt au nœud C13 sans fiche, puis sans Claude : 22 classées, 0 notable, 5,24 USD), Colognese-Ward Q2 (arrêt au nœud C13, puis sans Opus : 31 classées, 1 notable), Jang-Feng (31 passeports, 29 classées, 2 notables, 8,74 USD) ; sorties copiées au canal sans lecture par session-depot. | résultat | conv-audit (spécifications) ; session-depot et sa fille (courses) ; Lazar (GO) | fermé (courses) ; lecture : voir les sorties non lues | DEC R-1111 ; DEC R-1120 ; DEC R-1127 ; DEC R-1135 ; DEC R-1149 ; DEC R-1160 ; DEC R-1166 ; DEC R-1168 ; DEC R-1174 ; DEC R-1176 | § 3.1, § 7 |
| PAC-015 | Organisme sur la question v1 du pilier attaque, course sans Fable : 30 fiches validées (Opus 16, Argon 14), 0 refusée, 1 en quarantaine ; témoins tenus ; attestation « aucune recette » de la mère (fiches de niveau méthode et démonstration) ; bras (b) à deux juges, accord de rang 0,4167 ; cinq fiches retenues (dossier d'avant-entretien préenregistré, transfert inter-familles sous non-infériorité, sas d'homologation à neuf garanties, préservation de la généralisation hors famille, rappel de l'oracle et indépendance des erreurs). | résultat | organisme (Opus, Argon) ; fille idéation 2 ; mère | fermé (matériau d'atelier, jamais une preuve) | DEC R-1853 ; DEC R-1860 ; DEC R-1865 | § 4.2, § 7 |
| PAC-016 | Le directeur demande des expériences qui convainquent le jury en une semaine et au moindre coût ; identifier les goulots et les questions à résoudre avant l'entretien avec le collisionneur ; GO en priorité pour les expériences destinées au mentor. | idée | Lazar (8 novembre) | décidé (orientation) | DEC R-1830 ; DEC R-1832 ; DEC R-1883 | § 7 |
| PAC-017 | « Front E » du programme d'entretien : le périmètre n'est pas borné par la candidature envoyée ; ce que l'organisme rend atteignable (« avec l'organisme on peut attaquer des questions bien plus ambitieuses »). | idée | Lazar (R-619) ; session-depot (programme d'entretien v7) | écrit au programme d'entretien | DEC R-619 | § 7 |
| PAC-018 | Demander à l'organisme de chercher d'autres hypothèses testables sur le paradigme maïeutique et l'« esprit de finesse », au-delà du croisement format × contexte. | idée | Lazar | proposé ; non suivi d'une course identifiée à ce jalon | DEC R-509 | § 7 |
| PAC-019 | Phrase honnête pour le jury : séparer proposeur et juge, juger par e-valeurs avec contrôle de multiplicité sur données postérieures à la proposition et éprouver ce juge sur un monde à vérité plantée existe déjà ; l'apport non trouvé dans les pièces lues est un juge dont le nul est formé des lois connues, appliqué à des hypothèses de recherche libres, et sa mesure sous l'attaque d'un proposeur qui en lit la règle sur des mondes où toute promotion est fausse — affirmation valant pour les pièces lues, pas pour le champ. | proposition | rapport C4 | proposé (formulation) ; revendication et citations au directeur (nœud) | C4R:363 | § 3.1, § 4.1, § 7 |
| PAC-020 | Question v2 du pilier attaque (scellée) posée à Argon seul, au collisionneur puis à l'organisme : vérité terrain d'abord (audit du rappel de l'oracle, indépendance oracle-moniteurs), existence de la trace au-delà du texte et de la consigne, localisation (écart apparié au modèle de base), causalité (dose-réponse, pilotage, substitution depuis le jumeau honnête), lisibilité sans étiquette et « pince » (défense jointe boîte blanche et boîte noire), défense randomisée ou perfectionnée et « étau » ; champs fermés, aucun champ « comment faire » côté attaque. | idée | mère ; Lazar (« je veux la partie attaque ») | décidé (scellée au défaut, R-1802) ; course de l'organisme bloquée (jalon 3) | PAQ:1, 11-13, 29-40 ; DEC R-1802 | § 4.2, § 7 |
| PAC-021 | Une v3 des questions du programme après la couche 1, éventuellement par un tour du collisionneur « quelles questions produiraient des résultats forts avec ce pôle, sous nos contraintes ». | question ouverte | conv-audit (programme de conception v1) | proposé non tranché | PCO:87-88 | § 7 |

## II.13 Outillage et gouvernance (OUT, 49 entrées)

| n° | idée | type | origine | statut | source | renvoi (partie I) |
|---|---|---|---|---|---|---|
| OUT-001 | Invariant : aucun score d'un moniteur du programme dans l'entraînement ou la sélection de l'organisme ; un organisme qui écrit ses moniteurs et s'en sert pour se sélectionner viole l'invariant ; moniteurs neufs pour mesure rapportée seulement, jamais comme signal. | idée | audit défensif (N-053), étendu à l'organisme par la synthèse du collisionneur n12-n13 | décidé (N-053 : invariant « aucun score de moniteur dans un signal d'entraînement ou de sélection de l'agent, hors bras d'attaque déclaré », qui « vaut aussi pour la piste organisme » ; gardé par le code, R5) ; rappelé par N-065 | RPG:159-161 ; N053:42-44 ; N065:23-24 | § 3.2, § 6, § 7, § 8 |
| OUT-002 | Citations obligatoires de N-064 dans tout texte qui présente l'organisme (POPPER ; Dwork et al. 2015 ; Blum et Hardt, Ladder ; Co-Scientist). | idée | Lazar (N-064) | décidé (N-064, point 4) | RPG:116, 161-162 ; N064:15 ; [B41]-[B44] | § 3.1, § 3.2, § 4.1, § 8 |
| OUT-003 | Phrase et diapositive pour l'entretien : « notre question vaut aussi pour les juges de la recherche automatisée ; nous la testons sur un organisme d'idéation dont le juge statistique est attaqué par un proposeur qui lit ses verdicts, et nous le comparons à un juge génératif façon Co-Scientist » ; aucun chiffre tant qu'A1-v4 n'a pas rendu son verdict scellé. | proposition | mère (rapport du 9 novembre) | proposé non tranché | RPG:164-167 | § 3.1, § 3.2, § 5, § 8 |
| OUT-004 | L'organisme figure parmi les éléments absents de la candidature déposée ; la question de son intégration a été posée sous plusieurs formes sans réponse unique écrite avant le 9 novembre. | résultat | mère (constat) | fermé (constat) ; réponse donnée au § 6 du rapport du 9 novembre | RPG:126-131 | § 3.2, § 8 |
| OUT-005 | Objection d'emploi du temps : l'effort sur le juge-tournoi et le collisionneur se disperse hors du chemin critique de G0 ; recentrer la mère jusqu'au 15 novembre sur ce qui fait partir la course 7b, le reste n'avançant que s'il ne coûte ni décision du directeur ni attention de la mère. | objection | mère (rapport du 9 novembre), confiance 0,8 | proposé, défaut « oui » sous 48 heures | RPG:19-22, 176 | § 3.1, § 3.2, § 8 |
| OUT-006 | Incident : Argon appelé pendant A1-v4 en écart à un texte scellé (exclusivité) ; option (a) proposée : garder la course telle quelle, comptes lus par l'audit A9, relancer l'étiqueteur après A1-v4 ; leçon écrite : chercher, avant toute course, les conditions d'exclusivité des courses en marche. | résultat | mère (écart R-2013 ; leçon R-2012, R-2013) | proposé, défaut (a) le 11 novembre ; leçon écrite | RPG:20, 85-87, 177 | § 3.2, § 5, § 8 |
| OUT-007 | Collisionneur en mode critique, avec témoins plantés, pour entraîner les réponses aux questions dures de l'entretien (après une v17 du programme d'entretien contre-lue), ≈ 10 à 15 dollars sur crédits Claude. | proposition | mère (rapport du 9 novembre), confiance 0,7 | proposé non tranché | RPG:42, 120-122, 188 ; DEC R-1790 (point e, selon RPG:121) | § 3.2, § 4.2, § 8 |
| OUT-008 | Verdict officiel prononcé par un lecteur neuf d'une autre lignée que l'auditeur, scellé, en accord complet sur le fond avec le verdict provisoire. | idée | mère (procédure d'A1-v4) | fait (A1-v4) | RAF:232 [B25 complément] DEC R-2111 ; A4V:4 | § 3.2, § 5, § 8 |
| OUT-009 | Publication du résultat scellé d'A1-v4 sur la page publique de l'organisme (10 novembre), avec lectures bornées, réserves, règle « jamais seul » et deux décisions ouvertes ; 22 corrections d'une contre-lecture appliquées ; aucune recette ; publiée avant la constatation de la collision : la corriger demande un nouvel accord de publication. | résultat | directeur (mot de publication) ; mère | fait (publié) ; correction proposée non tranchée | [B46] DEC R-2162 ; PUB ; [B48] | § 3.2, § 5, § 8 |
| OUT-010 | Un résultat négatif se publie et justifie le préenregistrement suivant. | idée | Lazar (24 octobre) | décidé (N-044) | N044:27-28, 51 | § 1.1, § 3.2, § 8 |
| OUT-011 | Recherche bibliographique 2025-2026 obligatoire avant toute revendication sur les concepteurs entraînés (multi-tour, mémoire, familles tenues à l'écart). | idée | Lazar « go » | décidé (N-045 v2) ; lancée au 25 octobre | N045:40-41, 115-117 | § 3.2, § 6, § 8 |
| OUT-012 | Contre-lecteur de la boucle extérieure : même famille, autre modèle — Opus 5.5 analyste, correcteur et lecteur de dossier d'audit ; Fable 5.1 contre-lecteur (parties A et B) et agent d'audit qui attaque un verdict ; une fiche en désaccord entre analyste et contre-lecteur ne motive rien ; un refus de Fable se consigne, sans bascule seule. | idée | Lazar (« même famille, mais un autre modèle ») ; conv-audit | décidé (N-052) | N052:21, 31-38, 42-44 | § 3.2, § 6, § 8 |
| OUT-013 | Ordre de travail de conv-audit : la version 32 de l'orchestrateur (prise « idéation », corrections CL31-01 à 10 de la contre-lecture) d'abord, puis les sept demandes de dimensionnement de la couche 2 ; pendant la v32, session-depot construit sans dépense la part de la chaîne de la couche 2 qui ne dépend pas du dimensionnement. | idée | session-depot ; Lazar « (a) go sur l'ordre » | décidé (N-058) | N058:15, 29-32 | § 2.3, § 3.2, § 4.2, § 8 |
| OUT-014 | Campagnes de la voie gouvernée : plafond petit, fixé fiche par fiche à une porte, sous revue externe. | idée | conception de l'affinage v2 | décidé (N-059, point 10) | N059:38 | § 3.2, § 4.2, § 8 |
| OUT-015 | Gouvernance de l'affinage : la branche de la session de Fable est ratifiée comme son dépôt de travail ; aucune fusion avant la contre-lecture de la version concernée ; la poussée de la v1 ratifiée ; une v3 courte (dix-sept corrections de la relecture de Fable) avant le codage du juge et de la mémoire. | idée | Lazar ; relecteurs | décidé (N-059, points 12-13) ; v3 prévue | N059:41-43, 47-48 | § 3.2, § 4.2, § 8 |
| OUT-016 | Incident : la v6 du pilote 3 est partie malgré une retenue écrite sur le canal ; règle : relire le canal de conv-audit immédiatement avant tout lancement et à chaque réveil. | résultat | session-depot | fermé ; règle de pratique écrite | DEC R-444 | § 3.2, § 8 |
| OUT-017 | Règle des refus : quand Opus (puis Fable) refuse, la cellule refusée reste telle quelle ; une question nouvelle, conceptuelle, mathématique et technique, porte le même fond, posée une fois ; un second refus arrête ; jamais pour obtenir un contenu visé par un refus de sûreté ; précisée : « un arrêt appelle une reformulation sous une autre question plus spécifique moins diffuse », pas le contournement de la même question. | idée | Lazar (R-468, R-470, R-609) | décidé | DEC R-468 ; DEC R-470 ; DEC R-609 | § 3.2, § 8 |
| OUT-018 | Ne jamais faire passer par l'organisme une demande refusée par Opus et Fable sous d'autres rôles : refusé même sur accord du directeur (consigne gelée « ne contourne jamais un refus d'un filtre de sûreté ») ; appliqué à la course « programme TAIF » et à la course Scheurer, révisé pour Scheurer seulement après lecture du texte servi et mot direct. | idée | session-depot | décidé (R-486, R-1161) ; révision ponctuelle (R-1170) | DEC R-486 ; DEC R-1161 ; DEC R-1170 | § 3.2, § 8 |
| OUT-019 | Levée de R1 pour les pilotes de conception (phase d'essais-erreurs) : la relecture R2 est gardée, les scores de conception se lisent dès la fin d'une course ; les expériences de confirmation restent scellées, sur tâches neuves, et déclarent que leurs auteurs ont lu les scores de conception. | idée | Lazar (« la règle est levée ») | décidé (R-473) | DEC R-473 | § 3.2, § 8 |
| OUT-020 | Lecture de H-G1 inchangée : un plancher de bruit ou des témoins de sortie, s'ils viennent, sont descriptifs, ajoutés par un addendum scellé et contre-lu avant toute lecture ; borne de dépense de l'étape 1 (1 150 USD) par exécution, sur la règle « aucune relance ». | idée | Lazar | décidé (CL8-08, CL8-06) | DEC R-412 ; DEC R-413 | § 3.2, § 8 |
| OUT-021 | Sorties fabriquées : 8 des 33 sorties du « brainstorm » et du « collisionneur 3 × 3 » de la relève de Gemini sont des textes fabriqués après des erreurs 404 ; d'où l'audit de toute sortie avant usage. | résultat | audit de la quarantaine de la relève de Gemini (session-depot) | fermé (constat) | DEC R-335 | § 3.2, § 8 |
| OUT-022 | Isolation des courses : sur un hôte Docker de Vast.ai, les espaces de noms (`unshare`) sont refusés ; l'option « courses sur une instance sans carte » ne tient pas telle quelle. | résultat | session-depot (sonde d'hôte) | fermé (constat) | DEC R-377 | § 3.2, § 8 |
| OUT-023 | Politique de relance de la course d'idéation : les vérifications déjà réussies et scellées ne sont pas rejouées ; seuls les contrôles échoués ou non faits sont repayés. | idée | Lazar (« (c) ne pas rejouer à la relance les vérifications déjà réussies ») | décidé (R-715) | DEC R-715 | § 3.2, § 8 |
| OUT-024 | Gouvernance du travail offensif : la conception et la recherche défensive continuent au registre de gouvernance ; toute construction ou exécution d'un pipeline opérationnel d'évasion est gelée jusqu'à une revue de sécurité externe (R-611), plus tard levée (R-888) ; l'organisme hérite de cette porte pour tout ce qui ressemble à un évadeur. | idée | Lazar | décidé (R-611, GO-2026-10-28-04) ; levée inscrite en R-888 | DEC R-611 ; DEC R-895 | § 3.2, § 8 |
| OUT-025 | Collisionneur des nœuds : question v7 à v12 de conv-audit (nœuds N1, N3 à N6, N9, N10 ; N2, N7 et N8 retirés ; N3 réduit à D-i et D-j ; N9 = D-GK-1 sur Gu-Krenn ; N10 complété par le pilote « mélange d'équilibre ») ; deux tours, critères scellés avant ouverture, synthèses et errata scellés. | résultat | conv-audit (questions) ; collisionneur ; lecteurs neufs | fermé (tours 1 et 2) ; contenu des nœuds au jalon des synthèses | DEC R-898 ; DEC R-900 ; DEC R-901 ; DEC R-917 ; DEC R-922 ; DEC R-934 ; DEC R-943 ; DEC R-953 | § 3.2, § 8 |
| OUT-026 | Règle du directeur : toute question reformulée va aussi à Kimi seul (comme à Argon seul), au collisionneur et à GPT-6 Astra quand il est branché ; conv-audit écrit sa propre réponse ; le directeur compare et fusionne. | idée | Lazar (1er novembre, 09:52 UTC) | décidé | DEC R-959 | § 3.2, § 8 |
| OUT-027 | Collisionneurs à cinq espèces (Fable, Opus, Argon, Kimi, GPT-6 Astra) « dès que possible » ; d'abord bloqués par le crédit d'OpenAI, puis en service (collisionneur v9). | idée | Lazar | décidé ; codé (collisionneur v9) | DEC R-962 ; DEC R-966 ; DEC R-968 ; DEC R-1845 | § 3.2, § 8 |
| OUT-028 | Dépôt public `lciric/ideation-organism` : « public » tranché par le directeur ; orchestrateur v56, pont fiche-loi, conception v7, README, manifeste de 203 fichiers ; exclus : montants, feux verts, coffre, `donnees/`, registres ; publications ultérieures sur son mot (8 et 10 novembre). | idée | Lazar ; conv-audit (poussée) | décidé et fait | DEC R-989 ; DEC R-1771 ; DEC R-2162 | § 3.2, § 4.3, § 8 |
| OUT-029 | Priorité donnée à l'organisme d'idéation pour l'échéance du 2 novembre ; « zapper le collisionneur » (sorties du collisionneur v8 non lues). | idée | Lazar | décidé (R-1036) | DEC R-1036 ; DEC R-1039 | § 3.2, § 8 |
| OUT-030 | Écart de la mère à un texte scellé : Argon appelé pendant la course d'A1-v4 qui exigeait « Argon seul » ; écart déclaré, lu par l'audit A9, option (a) tranchée (garder la course telle quelle). | résultat | mère ; Lazar (option (a)) | fermé (R-2043) | DEC R-2013 ; DEC R-2014 ; DEC R-2043 | § 3.2, § 5, § 8 |
| OUT-031 | Tour du collisionneur v9 sur la conception de l'organisme : préparé sans appel (question en trois sections, faits de 99 397 octets, devis ≈ 15,4 USD, pire cas 30,32) ; ligne de GO non inscrite, mot direct attendu. | proposition | session-depot | proposé non tranché (au 3 novembre) | DEC R-1132 | § 3.2, § 8 |
| OUT-032 | Contrainte de code : un seul modèle externe par course (le contrôle de la commande externe exige que tous les externes égalent un modèle attendu) ; course v1 avec Argon, « v1 bis » avec Astra seul externe finalement non lancée. | résultat | fille idéation 2 ; Lazar (« s'en passer pour l'instant ») | fermé ; v1 bis écartée pour l'instant | DEC R-1828 ; DEC R-1866 | § 3.2, § 8 |
| OUT-033 | Garde refus-question de l'organisme : sonde de pré-vol qui sert à chaque modèle un extrait borné de la question et classe sa réponse ; v1 refaite à neuf (la garde de conv-audit n'existait que fondue dans un lanceur), v2 après de faux refus dus à un défaut d'en-tête d'autorisation. | idée | Lazar (« je veux la garde sur les refus de l'org ») ; mère | codé (`src/controle_ia/garde_refus_question_v1.py`, puis v2) et éprouvé (R5) | DEC R-1788 ; DEC R-1821 | § 3.2, § 8 |
| OUT-034 | Organisme sur la question v2 du pilier attaque : bloqué successivement par le crédit Anthropic, par l'absence de bac à sable, puis par le classifieur du mode automatique (« Auto-Mode Bypass ») ; règle de permission pour une seule commande exacte de lancement, écrite par le directeur ; lanceurs v2 et v3 contre-lus. | résultat | filles idéation 1 et 3 ; mère ; Lazar | fermé (constats) ; course en attente de la règle de permission (au 9 novembre) | DEC R-1906 ; DEC R-1937 ; DEC R-1940 ; DEC R-1978 ; DEC R-1994 | § 3.2, § 4.4, § 8 |
| OUT-035 | N5 — règle de non-lecture A21 de l'orchestrateur : deux contre deux au tour 1 ((a) appliquer l'intention, l'étape étant impossible sans la classe des témoins ; (b) la clé ne franchit jamais la frontière du processus, l'aveugle reposant sinon sur le code qui atteste lui-même) ; au tour 2, personne ne tient (a) telle quelle : pièce demandée (test d'invariance exact sur l'archive scellée, contrôle positif, attestation externe sans clé), à défaut (b). | question ouverte | collisionneur des nœuds | proposé non tranché (« l'absence de pièce ne vaut pas décision ») | SN1:178-192 ; SN2:189, 338 | § 3.2, § 6, § 8 |
| OUT-036 | Tricherie « l'agent imprime son propre verdict » : jusqu'à la v56, l'étage des tests de mort lisait la statistique décisive sur la sortie du script ; depuis la v57, le verdict vient du calcul de l'orchestrateur sur le fichier brut que nomme le préenregistrement (fichier, colonne, statistique et seuil), le nombre imprimé n'étant qu'un témoin ; un incident rend la fiche « non concluante ». | résultat | revue de code de l'organisme ; correction v57 et v57b | codé ; éprouvé hors ligne seulement (exécutant simulé, sans bac réel) | RDM:69 | § 3.2, § 4.4, § 8 |
| OUT-037 | Coffre : verdicts et clés de classes stockés scellés, seule une empreinte est rendue ; toute lecture avant la fin déclarée est un incident qui arrête l'orchestrateur ; la v55 interdit les copies en mémoire et journalise chaque lecture permise avec sa raison. | idée | dessin de l'organisme | codé (`pole/coffre_v53.py`, `pole/coffre_v55.py`) | RDM:72 | § 3.2, § 8 |
| OUT-038 | L'expérimentateur ne doit atteindre ni le réseau, ni l'hôte, ni une clé : garde des outils sur chaque appel d'outil (première barrière, par motifs) ; vraie barrière : le bac à sable ; variables d'environnement de la machine jetable tirées d'une liste blanche fermée (v56), non d'une liste noire. | idée | dessin de l'organisme | codé (`pole/garde_outils.py`, `pole/tests_de_mort_v2.py`, v56) | RDM:73 | § 3.2, § 4.4, § 8 |
| OUT-039 | Caviardage des formes de clés connues avant toute écriture dans l'archive, le journal ou la mémoire ; limite écrite : un secret de forme inconnue passe. | idée | dessin de l'organisme | codé (`pole/caviardage.py`) | RDM:74 | § 3.2, § 8 |
| OUT-040 | Aucun repli silencieux : un champ manquant, un modèle servi inconnu, un plafond atteint, un signal arrêtent le rôle ou la course avec une raison écrite ; plafonds de dépense recalculés deux fois et acquittés à chaque étage. | idée | dessin de l'organisme | codé (`pole/noyau_v56.py`, `pole/budget_v56.py`) | RDM:75 | § 3.2, § 8 |
| OUT-041 | Dossier fermé : la course ne peut lire que les fichiers listés dans un manifeste scellé, sans lien symbolique, rien de plus, rien de moins (contre la dérive des données sous le test). | idée | dessin de l'organisme | codé (`pole/dossier_ferme.py`) | RDM:76 | § 3.2, § 8 |
| OUT-042 | Banc de mutations comme méta-garde : des mutations délibérées du code (retirer un contrôle, inverser une comparaison, avaler une exception) doivent chacune être tuées par la suite d'essais pour la raison attendue ; 224 mutations (v54 à v58) toutes tuées ; le banc ne dit rien des gardes qui n'existent pas. | idée | dessin de l'organisme | codé (`essais/mutations_v56.py` à `v58`) | RDM:110, 119 | § 3.2, § 8 |
| OUT-043 | Versions empilées, jamais éditées (R12) : `noyau_v56` hérite de `noyau_v55`, qui hérite de `v54` ; chaque version ajoute les corrections d'une contre-lecture indépendante (vingt, CL1 à CL20, chacune avec une table « constat → fichier:ligne → essai → mutation ») ; l'ancien fichier reste identique à l'octet pour que toute course passée reste rejouable contre son manifeste. | idée | dessin de l'organisme | codé | RDM:186-188, 212 | § 3.2, § 8 |
| OUT-044 | Graines : le cœur du pôle (v0 à v52b) dérive ses graines de SHA-256 d'étiquettes ; à partir de la v53, les modules neufs emploient `numpy.random.SeedSequence` clé par le nom de la tâche (R9). | idée | dessin de l'organisme | codé | RDM:211 | § 3.2, § 8 |
| OUT-045 | Revendication O17 : scellement avant lecture, aucun repli silencieux, mutations : passe de « non occupée » à « voisine » ; le banc de mutations et la règle « aucun repli silencieux » ne sont pas trouvés. | résultat | rapport C4 | changement de statut, non tranché | C4R:353 | § 3.2, § 8 |
| OUT-046 | Garde permanente des questions du pilier attaque : niveau méthode et démonstration, jamais recette (fiche trop concrète scellée au coffre) ; aveuglement de la défense aux recettes et au mode tenu à l'écart ; refus de classifieur jamais contourné ; issues négatives écrites d'avance au même rang que leurs contraires ; une issue négative sur les sondes commande leur reconception, chaque lecture décisive consommant une famille tenue à l'écart neuve. | idée | mère ; Lazar (R-1795) | décidé (texte scellé) | PAQ:5-9 | § 3.2, § 8 |
| OUT-047 | Chaîne des contre-lectures de l'orchestrateur (prise « idéation », v31 à v52) : chaque version est relue par une instance neuve qui n'a pas écrit le code, avec une table « constat → fichier:ligne → essai → mutation » ; verdicts successifs : v31 « non lançable en l'état » (panne de plomberie du duel, CL31-01), v34 à v37 « lançables après corrections », v39 « non lançable » (plafonds d'Argon), v40 « lançable, aucune relance » (CL40-01), v41 « non lançable » (contrôle du bras perdu après toute la dépense), v42 et v43 (voie β refusée sans dépense par la somme des plafonds), v44 (guillemets français), v48 à v51 « lançables sans l'étage des tests de mort », v52 « lançable en l'état » sous deux conditions (attestation de lecture pour Argon, ports libres). | résultat | contre-lecteurs neufs (Opus 5.5 surtout) ; conv-audit (auteur des versions) | fermé (contre-lectures scellées) | CL31 ; CL17 ; DEC R-637 ; DEC R-658 ; DEC R-661 ; DEC R-668 ; DEC R-674 ; DEC R-693 ; DEC R-702 ; DEC R-707 ; DEC R-712 ; DEC R-737 | § 3.2, § 4.4, § 8 |
| OUT-048 | Marche à suivre du lancement réel de la course d'idéation (voie β) : séquence écrite d'avance à partir des devis, des LISEZMOI des versions et des contre-lectures ; rien lancé ni payé par le préparateur. | idée | sous-agent de préparation de session-depot | écrit (29 octobre) | DEC R-753 ; DEC R-759 | § 3.2, § 8 |
| OUT-049 | Préenregistrement levé pour toute la partie exploratoire de l'organisme « jusqu'à avoir obtenu un système qui marche » (27 octobre, R-546) ; la relecture reste. | idée | Lazar | décidé (R-546 ; même esprit que R-473 pour les pilotes de conception) | PCO:14-15 ; DEC R-546 | § 3.2, § 8 |

## II.14 Décompte

| famille | entrées |
|---|---|
| ARC — Architecture et couches | 46 |
| ROL — Rôles et pôles | 40 |
| JUG — Juges et nuls | 51 |
| ATQ — Attaques et défenses du juge | 65 |
| BOU — Boucle fermée et héritage | 37 |
| COM — Composition apprise et coût | 27 |
| UNI — Universalité et familles inédites | 13 |
| VER — Vérité, oracles et mondes plantés | 41 |
| MAT — Mathématiques, preuve et Lean (couche 4) | 8 |
| REC — Récompense collective et signalement (Avalon, N13) | 13 |
| PAC — Papier C et menaces diffuses (N-065) | 21 |
| OUT — Outillage et gouvernance | 49 |
| **total** | **411** |

| type | entrées |
|---|---|
| hypothèse | 5 |
| idée | 194 |
| objection | 11 |
| piste écartée | 13 |
| proposition | 46 |
| question ouverte | 25 |
| résultat | 117 |
