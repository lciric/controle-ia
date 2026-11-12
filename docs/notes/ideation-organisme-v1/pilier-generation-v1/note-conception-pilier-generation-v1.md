# Note de conception — pilier « génération » de la couche 4 de l'organisme d'idéation (mathématiques nouvelles pour le contrôle, l'alignement et l'interprétabilité mécaniste) — v1

- **Pour** : la session mère, puis Lazar. **Nature** : **proposition, nœud chez Lazar** (pas (c) de R-2199). Rien n'est ouvert,
  rien n'est lancé, aucune dépense, aucun appel de modèle, aucun réseau n'ont servi à l'écrire. N12 (b) (R-959) garde les
  couches 3 et 4 fermées jusqu'aux résultats de l'étape 2 : ce texte ne les rouvre pas et n'est pas une règle d'ouverture.
- **Écrit par** : un sous-agent neuf (rédacteur), modèle **Opus 5.5** (`claude-opus-5-5`), session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv`, le 10 novembre 2026 (début 14:11:52 UTC, écriture à partir de 14:19:32 UTC ; heures
  relevées par `date -u`). Je n'ai écrit ni la synthèse du tour 2, ni le dessin de l'essai Lean, ni le programme de
  l'organisme. **Conflits déclarés** : je suis de la famille des espèces A et B du collisionneur, et du même modèle que le
  lecteur du tour 2, que le rédacteur de l'essai Lean et que le rédacteur du programme de l'organisme v3 ; mes ordres de
  grandeur reprennent l'hypothèse de l'essai (Opus 5.5 dans les bras) sans la recommander ici.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-note-pilier-generation-v1.md`
  (`61ec586c…`, vérifiée avant lecture). **Journal** : `note-conception-pilier-generation-v1-journal-v1.md` (même dossier :
  sources lues et empreintes, affirmations et renvois, questions ouvertes). **Calculs** : `calculs-v1/` (même dossier).
- **Conventions** : « proposé par le rédacteur » = rien de tel dans les pièces lues ; « RAPPORTÉ » = dit par une pièce du
  dépôt que je n'ai pas pu vérifier à sa source ; « SUPPOSÉ » = hypothèse de chiffrage. Les renvois « [J-n] » pointent la
  ligne n du tableau des affirmations du journal.
- **Citations obligatoires** (N-064, point 4 ; N-065, point 4 : tout texte qui présente l'organisme) : POPPER (Huang, Jin,
  Li, Li, Candès, Leskovec, ICML 2025, PMLR 267, p. 2-5 et algorithme 1 p. 14 ; PDF au dépôt, `a3c4b370…`) ; Dwork et al.
  (arXiv 1506.02629, p. 20-21) ; Blum et Hardt, « The Ladder » (arXiv 1502.04585, p. 10-12) ; Co-Scientist (Nature 655,
  p. 487-496), voisin de la boucle générer-classer-faire évoluer. Collision rapportée avec Qu, Chen et Wang (arXiv 2609.27051)
  sur la revendication O2 du juge, nœud ouvert chez Lazar [J-24]. Références recopiées de N-064 et du programme v3, non
  relues ici.

## Verdict

1. **Le pilier se dessine comme une chaîne de six maillons** — proposeurs, formalisation, Lean comme arbitre, juge de
   nouveauté, juge d'utilité, relecture humaine — **où chaque maillon a sa garde mécanique et son oracle planté**. Lean ne
   tranche qu'une chose : l'énoncé **formel** est démontré. La fidélité à la conjecture, la non-vacuité, la non-trivialité,
   la nouveauté et l'utilité demandent chacune leur propre mesure ; aucune ne se lit sur le verdict d'un juge seul (N-058).
2. **Les trois propriétés se mesurent sur des oracles plantés, à coût mesuré.** **Vrai** : banc de tricheurs scriptés et
   cibles fausses plantées (toute acceptation y est une faille). **Neuf** : jamais « nouveau », seulement « non trouvé dans
   les pièces lues » au-dessus d'un plancher mécanique (pas un corollaire immédiat de Mathlib au commit épinglé), avec un
   taux de faux « neuf » mesuré sur une banque d'énoncés connus plantés. **Utile** : fermer ou réfuter une **cible formelle
   scellée d'avance**, tirée d'une question du programme, avec sa table de décision ; tout le reste est information. Les
   proposeurs se jugent sur des **mondes mathématiques plantés** à vérité calculable et sur le coût (N-058).
3. **Cinq questions du programme où un énoncé formel aiderait** (§ 1.2) : le sens exact de « au-delà de l'archive » pour le
   juge de l'organisme ; le plafond d'horizon (A7) face à H2 ; l'agrégateur sous corrélation adverse ; le lemme maître
   d'impossibilité face à « δ > 0 » ; la sonde qui ne lit que l'indication (A13). Les quatre dernières viennent de la carte
   des hypothèses v1, que je n'ai pas lue (hors de `main`, corrections annoncées) : elles sont RAPPORTÉES.
4. **Rien ne peut commencer avant** : les résultats de l'étape 2 et la décision de Lazar (N12 (b)) ; la carte de couverture,
   les gardes éprouvées et l'isolement de l'essai (b), dont ni D-1a ni D-1b n'est accordé ; la carte des hypothèses corrigée
   sur `main`. **Ordre de grandeur d'un pilote** (aucun devis, hypothèses non vérifiées) : **≈ 600 à 3 000 USD d'appels**,
   ≈ 3 à 130 USD de machine, **≈ 2,5 à 20 heures de relecture humaine** (§ 5).
5. **Ma prédiction** (SUPPOSÉ, écrite pour être démentie ; aucun run ne la vise, R3) : le premier goulot mesuré sera la
   **fidélité et la trivialité** des énoncés, pas la démonstration ; les premiers produits utiles seraient « vrais, utiles,
   **non neufs** » (vérification formelle des lemmes du programme lui-même), et le taux de faux « neuf » d'un juge à modèle
   seul sur des connus reformulés sera haut — c'est la raison du plancher mécanique et de la banque plantée.

---

## 0. Statut, bornes, ce qui est repris

- **Origine.** Question de Lazar du 31 octobre (R-920) : « réécriture de soi et de concepts mathématiques inédits avec lean en
  soutien ? » ; réponse alors inscrite : la couche 4 est le pôle théorie et Lean, qui n'existe pas encore [J-32].
- **Décisions qui bornent ce texte.** N12 (b) (R-959) : couches 3 et 4 fermées jusqu'aux résultats de l'étape 2, un seul pas
  permis, l'essai sur processeur « preuve formelle contre suite bon marché » [J-2]. R-2199 : (a) lecture du tour 2, **faite**
  (R-2226) ; (b) devis de l'essai, **dessiné** (brouillon 3, R-2240 ; D-1a présenté à Lazar, aucun GO) ; (c) **cette note**,
  nœud chez Lazar [J-3, J-4, J-5]. Pôle théorie « go » du 27 octobre : « ne pas promettre de révolution, mesurer ce qui sort »
  [J-17].
- **Matériau des espèces : aucun.** La synthèse du tour 2 le constate (§ E.3) : aucune espèce ne parle de conjectures, de
  démonstrations nouvelles, de Lean comme arbitre d'objets produits ni de juge de nouveauté ; toutes les mentions de Lean
  portent sur la vérification [J-6]. Tout ce qui suit est donc **proposé par le rédacteur**, sauf renvoi.
- **Repris comme contraintes de dessin, et dit tel** : le vérificateur **externe, hors organisme** (convergence des cinq
  espèces pour la vérification, réserve R4 « trop propre ») [J-7] ; la règle « le rôle qui produit un artefact ne tient
  jamais la clé qui l'évalue » [J-18] ; l'invariant de N-053 et N-058 (aucun verdict de juge dans la sélection d'agents ;
  la composition des proposeurs se juge sur l'oracle planté et le coût) [J-9, J-10] ; les rôles 1 et 2 de N-065 (second
  terrain du papier C ; atelier dont les fiches sont du matériau, jamais une preuve) [J-11] ; les gardes G-L1 à G-L7,
  l'audit de fidélité sur l'énoncé imprimé par Lean et l'isolement de la machine de l'essai [J-12, J-13, J-14] ; les
  mécanismes du pôle de test de l'organisme : témoins plantés, banc des tricheurs, attaque d'un proposeur qui lit la règle
  du juge sur des mondes où toute promotion est fausse [J-19, J-20, J-21].
- **Ce que ce texte n'est pas** : ni un préenregistrement (R1), ni un devis, ni une règle d'ouverture de la couche 4, ni une
  revendication. Il dit **ce qu'il faudrait mesurer** pour pouvoir dire qu'un énoncé est neuf, vrai et utile.

---

## 1. Objet

### 1.1 Ce que le pilier produirait

| objet | définition opérationnelle (proposée par le rédacteur) | statut d'un objet sorti de la chaîne |
|---|---|---|
| **conjecture** | énoncé en langue naturelle, énoncé formel proposé, cible visée, prédiction du proposeur (vrai ou faux, confiance), et **ce qui la tuerait** (instance attendue en contre-exemple) | « ouverte » ; jamais promue par le seul verdict d'un modèle |
| **lemme** | énoncé formel **démontré** par Lean sous toutes les gardes (§ 2.3), fidèle, non vide, non trivial ; sous-but d'une cible scellée, ou autonome | « vrai (formel) » ; neuf et utile se lisent à part |
| **démonstration** | le **fichier Lean accepté** (squelette par étapes, définitions imprimées en entier), plus une version lisible ; l'objet vérifié est le fichier, jamais la prose | pièce scellée, rejouable à la version épinglée |
| **contre-exemple** | instance qui rend fausse une conjecture ou une cible, **vérifiée exactement** (calcul en rationnels, ou par Lean), jamais par virgule flottante seule | « réfutée » ; la réfutation d'une cible scellée compte comme utile |

Ce que le pilier **ne produit pas** : des affirmations empiriques (une preuve ne valide pas une spécification empirique,
MAT-004 [J-8]) ; des énoncés sur des modèles réels ou des organismes réels ; des recettes d'attaque (niveau méthode seulement,
R-607 [J-23]).

### 1.2 Cinq questions du programme où un énoncé formel aiderait

| n° | question du programme (source) | énoncé formel visé (forme, sans valeur) | si démontré | si réfuté | neuf ? (question, R8) | domaine de l'essai |
|---|---|---|---|---|---|---|
| **Q1** | Juge de l'organisme (papier C, revendication O2) : **nœud ouvert n° 2, « le sens de “rien au-delà de l'archive” »** ; une réponse contraire demanderait un nul v10 [J-22] ; la brèche de W2 sous le nul v8 était une brèche du **critère de nouveauté** (42 des 48 lois promues sont, à l'octet, la loi du monde) [J-21] | (i) définition formelle de la **clôture de l'archive** (lois connues et leurs recombinaisons par morceaux à un niveau, membres du nul v9) ; (ii) sous le nul composite, la richesse du juge franchit 1/α avec probabilité au plus α, **quel que soit le nombre de membres** (ce que le programme dit tenu pour le v9, contre-lu et éprouvé par simulation) [J-20] | « erreur tenue » cesse de reposer sur des mondes simulés ; le nœud n° 2 se tranche sur une **définition**, non sur un exemple ; la classe « non couverte » devient un ensemble écrit | le candidat v9 est bloqué avant toute production ; la faille est localisée dans le certificat | l'inégalité de Ville est classique : **vrai, utile, non neuf** probable ; la clôture par recombinaison : question (JUG-013, JUG-046 : nouveauté du « nul formé des lois connues » à durcir) [J-25] | D5 (règles de décision, martingales simples) |
| **Q2** | **Plafond d'horizon (A7)** : sous un effet d'épisode de part r₀, le rappel de toute statistique contre un décalage constant plafonne, quel que soit l'horizon (RAPPORTÉ par le programme d'entretien v16) [J-26] ; face à **H2** : l'accumulation séquentielle rattrape-t-elle ce que le seuil par action manque ? [J-27] | le plafond, avec ses hypothèses **écrites** (indépendance, forme de l'effet d'épisode, approximation éventuelle) | la lecture de H2 reçoit un plafond auquel se comparer ; mesurer r₀ d'abord (piste « mesure unanime ») devient une condition de dessin de G1 et de H2 | le lemme sort du programme d'entretien ; l'hypothèse cachée est nommée | question (analyse séquentielle à effets aléatoires) | D2 (probabilités, concentration) |
| **Q3** | **Agrégateur sous corrélation adverse** (question ouverte nommée pour le pôle théorie le 27 octobre) [J-17] ; **matrice « statistique × union de classes d'écart »** : quel panel de moniteurs reste non aveugle [J-28] | bornes sur le manque d'une règle d'agrégation d'un panel quand l'adversaire choisit la **dépendance** entre les erreurs des moniteurs à marges fixées ; ou énoncé négatif : aucune règle fixe ne bat le meilleur moniteur seul contre cet adversaire | la conception du panel (front A, point 2) passe d'empirique à argumentée ; la prédiction du papier C « agrégations robustes à gain nul ou négatif » [J-29] pourrait recevoir un ancrage ou un contre-exemple (lien proposé par le rédacteur : la prédiction porte sur des juges, Q3 sur un panel de moniteurs) | un contre-exemple dit quelle règle échoue et sous quelle dépendance | question (bornes de dépendance classiques, agrégation robuste) | D1, D2 |
| **Q4** | **Lemme maître L0** (« invariance, proximité en variation totale, strate, impossibilité », RAPPORTÉ) et **« δ > 0 sur organismes réels ? — lemme, ou théorème négatif »** (se tranche à G1) [J-26, J-30] | conditions mesurables (proximité en variation totale par pas, strate) sous lesquelles **aucune** statistique des signaux observés n'a une puissance au-dessus de α + ε | ne dit **pas** si δ > 0 (question empirique, G1 ; MAT-004) ; dit quelles issues de G1 sont hors d'atteinte sous des conditions mesurées, donc éclaire la lecture d'un échec de G1, **sans changer N-062** (l'échec commande la reconception) [J-34] | une hypothèse de L0 est trop faible ; la carte est corrigée | question (bornes d'indistinguabilité classiques) | D2 |
| **Q5** | **Sonde qui ne lit que l'indication (A13)** : contre des négatifs appariés en indication, son rappel égale son taux de fausses alertes, et son aire sous la courbe le cache (RAPPORTÉ) [J-26] ; interprétabilité : sondes d'intention | égalité du rappel et du taux de fausses alertes sous l'appariement, hypothèses écrites | la métrique des papiers (rappel à fausses alertes fixées contre négatifs appariés) devient opposable | l'appariement exigé est plus fort que dit | probablement **trivial et non neuf** ; utile malgré tout : c'est le cas qui empêche de confondre « trivial » et « inutile » (§ 3.2) | D5 |

**Cible d'étalonnage, hors du programme scientifique** : le **score apparié de l'essai Lean** (racine en forme close égale au
maximum de vraisemblance sous la contrainte p₁₀ − p₀₁ = Δ₀ ; réduction à McNemar en Δ₀ = 0), aujourd'hui contrôlé par
dérivation numérique et bloqué par le marqueur `<<SOURCE_TANGO>>` [J-15]. Réponse connue, petit énoncé, domaine D5 : c'est
le premier essai naturel de toute la chaîne, et un **connu planté** naturel pour le juge de nouveauté, qui doit répondre
« connu ». Une preuve formelle ne remplacerait pas la lecture de la source pour l'attribution.

**Avant toute cible Q2 à Q5** : lire la carte des hypothèses corrigée sur `main` (aujourd'hui hors de `main`, corrections
annoncées, lemmes sans étiquette [J-16]) ; aucune cible ne se scelle sur une forme rapportée.

---

## 2. Chaîne

### 2.0 Principes (proposés par le rédacteur, sur les pièces citées)

- **Placement.** Les proposeurs sont des rôles de l'organisme ; **l'arbitre (Lean), les gardes et les deux juges sont hors de
  l'organisme**, tenus par le noyau (vérificateur externe [J-7] ; règle de la clé [J-18]).
- **Sélection.** Aucun verdict de la chaîne — Lean compris — n'entre dans un signal d'entraînement ou de sélection des
  proposeurs pendant la mesure ; la composition des proposeurs se juge sur l'oracle des mondes plantés et sur le coût (N-058,
  invariant de N-053) [J-9, J-10]. Les **énoncés**, eux, se trient sur les gardes (l'interdit porte sur la sélection d'agents,
  pas sur celle des fiches) [J-10]. Faire de l'acceptation par Lean une récompense d'entraînement serait un changement
  d'hypothèse (nœud), hors de ce texte.
- **Cloison.** Tout code écrit par un modèle (fichier Lean compilé, calcul de contre-exemple) tourne dans la machine isolée de
  l'essai : sans clé ni dépôt, réseau coupé et éprouvé avant tout code de modèle, chaîne en lecture seule, dossier neuf par
  énoncé, aucune persistance [J-14].
- **Aveuglement.** Juges et relecteurs ne voient ni l'identité du proposeur, ni les verdicts des autres maillons au-delà de
  ce que leur entrée exige ; les témoins plantés sont mêlés anonymement aux énoncés réels.

### 2.1 Les six maillons

| maillon | entrée | sortie | garde | mode d'échec connu |
|---|---|---|---|---|
| **1. Proposeurs** (rôles de l'organisme, plusieurs familles) | une **carte de cible scellée** (question du programme, énoncé formel visé laissé ouvert, table de décision) ou un **monde mathématique planté** (définitions neuves, sans la clé) ; la bibliothèque au commit épinglé ; l'archive des énoncés connus ; la moisson de littérature (métadonnées) | fiches-conjectures à champs fermés (§ 1.1) | champs fermés ; aiguillage par la forme ; mémoire anti-redite ; plafond par proposeur ; aucune clé, aucun verdict servi qui sélectionne | redites ; **connu reformulé** (renommage, spécialisation, contraposée, assemblage de deux lemmes : l'analogue de la brèche de W2 [J-21]) ; énoncés triviaux en rafale ; dérive hors cible ; énoncés mémorisés (contamination) |
| **2. Formalisation** (rôle distinct du proposeur ; qui : même question que D-3 de l'essai) | conjecture en langue naturelle | énoncé formel, **imprimé par Lean** (et non tel que l'agent le déclare), définitions imprimées en entier ; rétro-traduction aveugle par une autre famille | G-L5, G-L6 de l'essai (énoncé imprimé ; ni notation ni macro ; définitions imprimées) [J-12] ; relecteur de fidélité d'une autre famille [J-13] ; **épreuve du contre-exemple déclaré** : l'énoncé formel doit être faux sur l'instance « qui la tuerait » ; **témoin de non-vacuité** (G-V) ; **sonde de trivialité** (G-T) | **formalisation infidèle** : énoncé renforcé, affaibli, hypothèse ajoutée, coquille corrigée en silence (classe K5 et « spécification altérée » de l'essai [J-12, J-13]) ; **conventions de Mathlib** (division par zéro, soustraction tronquée des entiers naturels, racine et logarithme hors domaine : valeurs conventionnelles qui rendent vrai un énoncé formel dont la conjecture est fausse ou sans objet ; à vérifier sur la version épinglée) ; hypothèses contradictoires ; type vide |
| **3. Lean comme arbitre** (noyau de Lean dans la machine isolée) | énoncé formel et tentative de preuve (ou de réfutation) | **ACCEPTE** (démontré), **RÉFUTÉ** (négation démontrée, ou contre-exemple vérifié exactement), **OUVERT** (budget épuisé) ; « ouvert » ne vaut jamais « faux » | G-L1 à G-L7 de l'essai (compilation, ni `sorry` ni `admit`, axiomes limités à `propext`, `Classical.choice`, `Quot.sound`, ni `axiom`, `unsafe`, `implemented_by`, `extern`, contrôle par un fichier du harnais) [J-12] ; plafonds de temps et de coût par énoncé ; versions épinglées | **triche de Goodhart sur l'arbitre** (§ 2.4) ; preuve d'un énoncé voisin ; délai ; dérive de version de Mathlib ; code exécuté à la compilation (cloison) |
| **4. Juge de nouveauté** (hors organisme, autre lignée que les proposeurs) | énoncé formel accepté, sa version lisible | une étiquette parmi trois : **« connu »** (avec la référence), **« corollaire immédiat de la bibliothèque »** (preuve close en k pas d'automatisation au commit épinglé), **« non trouvé dans les pièces lues »** (avec la trace de recherche) ; jamais « nouveau » | **plancher mécanique** (G-N) : automatisation de la bibliothèque sous budget fixé et comparaison aux énoncés de la bibliothèque après normalisation ; recherche d'antériorité par la moisson, puis lecture sur PDF empreinté (R7) ; **taux de faux « neuf » mesuré sur la banque d'énoncés connus plantés** (§ 3.4, B1) | **théorème déjà connu reformulé** ; littérature hors des métadonnées ; date de coupure du juge ; angles morts partagés avec le proposeur s'ils sont de la même famille ; proposeur qui apprend à déguiser le connu |
| **5. Juge d'utilité** | énoncé accepté et la carte de cible scellée | **« ferme la cible k »**, **« ferme un sous-but scellé de k »**, **« réfute k »**, ou **« hors cible »** | l'utilité se décide **mécaniquement** quand l'énoncé ferme (ou réfute) dans Lean une cible ou un sous-but **scellés avant la génération** ; un juge à modèle peut annoter les énoncés hors cible, **comme information seulement** | « utile » déclaré sans effet ; cible elle-même infidèle à la question (d'où la relecture des cartes avant scellement) ; variante affaiblie de la cible démontrée à sa place (l'analogue de K5 au niveau de la cible : empêché si la cible est l'énoncé scellé lui-même) |
| **6. Relecture humaine** (Lazar ; un mathématicien extérieur seulement sur nœud) | dossier par énoncé : conjecture, énoncé formel imprimé, définitions, témoin de non-vacuité, audit de fidélité, trace de nouveauté, rattachement à la cible, coût | « retenu pour un préenregistrement » ou « non retenu », avec raison | lit **après** le scellement des verdicts mécaniques, qu'elle ne change pas ; aveugle au proposeur ; budget de temps fixé | confiance excessive dans « vérifié par Lean » ; compétence du domaine ; goulot du temps de Lazar ; un contact extérieur est un nœud |

### 2.2 Classes d'erreurs de la génération, et ce que l'essai (b) en mesure

| classe (proposée par le rédacteur) | ce que l'essai (b) mesure, s'il est couru | ce qu'il ne mesure pas |
|---|---|---|
| **E1 formalisation infidèle** | la part d'acceptations à énoncé infidèle (audit sur 50 % des items au pilote, 30 % en confirmation) et le rappel sur la classe **K5 « énoncé voisin »**, **sans pression d'optimisation** [J-13] | le même taux quand un générateur optimise contre la chaîne |
| **E2 énoncé vide** | rien comme taux ; un artefact des essais de gardes (« étape à hypothèses contradictoires prouvée à vide ») [J-12] | la fréquence des énoncés vides produits par un générateur |
| **E3 énoncé trivial** | rien | tout |
| **E4 connu reformulé** | rien (l'essai n'a aucun juge de nouveauté, § 6, point 6 de l'essai) [J-15] | tout |
| **E5 triche sur l'arbitre** | les gardes G-L1 à G-L7 et l'épreuve d'isolement, éprouvées sur des artefacts fixés (R5) [J-12, J-14] | une triche adaptative, cherchée par un proposeur qui lit les gardes |
| **E6 vrai, neuf, inutile** | rien | tout |
| **E7 contre-exemple faux** | rien (la suite bon marché cherche des contre-exemples ; l'essai note le rejet et l'étape localisée, pas l'exactitude des contre-exemples avancés) | la part de réfutations numériques fausses |
| **couverture** (pas une erreur) | la **carte de couverture par domaine** : part des preuves courtes saines que la chaîne formelle accepte avec un énoncé fidèle, de D1 à D5 ; l'issue O0 (chaîne non viable) [J-15] | la couverture sur des énoncés neufs, plus longs |

**Ce qui découle de l'essai pour le pilier** : si l'essai rend O0 sur un domaine, Lean n'y est pas un arbitre possible pour
des énoncés **neufs**, et les cibles de ce domaine attendent (le rédacteur de l'essai le dit aussi, § 6, point 1 [J-15]) ;
le taux d'acceptations infidèles sans pression est le **plancher** auquel comparer le même taux sous attaque (§ 3.5).

### 2.3 Lean comme arbitre : ce qu'il tranche, ce qu'il ne tranche pas

- **Tranche** : l'énoncé formel imprimé est démontré à partir de la bibliothèque épinglée, sans axiome hors des trois admis.
- **Ne tranche pas** : que l'énoncé formel dise la conjecture (fidélité, E1) ; que ses hypothèses soient satisfiables (E2) ;
  qu'il ne soit pas immédiat (E3) ; qu'il soit neuf (E4) ; qu'il serve (E6) ; qu'une question empirique soit tranchée
  (MAT-004).
- **Gardes ajoutées à celles de l'essai** (proposées par le rédacteur, à éprouver sur cas sain et artefact, R5) :
  **G-V non-vacuité** : un témoin des hypothèses (une instance qui les satisfait) est démontré dans Lean, ou l'énoncé est
  classé « vide » ; **G-T trivialité** : l'énoncé se ferme-t-il par l'automatisation de la bibliothèque dans un budget court
  fixé ? Si oui, il est **« trivial »**, ce qui touche la nouveauté (plancher), **jamais la vérité ni l'utilité** (Q5 montre
  qu'un énoncé trivial peut être utile) ; **G-C contre-exemple exact** : toute réfutation est vérifiée en arithmétique exacte
  ou par Lean ; **G-E épreuve du contre-exemple déclaré** (maillon 2).
- **Trois issues, jamais deux** : ACCEPTE, RÉFUTÉ, OUVERT. Compter OUVERT comme faux ferait du budget de preuve un juge de
  vérité ; la part d'OUVERT par domaine est rapportée.

### 2.4 Triche de Goodhart sur l'arbitre (niveau méthode, R-607)

Dans l'essai, **personne n'optimise contre Lean** : il donne un taux de base [J-15]. Un générateur sous pression d'acceptation
trouverait des énoncés vides, triviaux ou voisins, ou des failles du contrôle (classe E5), comme les proposeurs de l'organisme
ont trouvé la classe que le nul v8 déclarait non couverte [J-21]. Le pilier mesure donc cette pression **sur des mondes où
toute promotion est fausse**, à la manière de l'attaque A1 [J-21] : (i) **cibles fausses plantées** (énoncés faux, clé de
contre-exemple scellée) : toute acceptation est une faille de vérité ; (ii) **archive complète** d'un monde planté (tous ses
énoncés vrais de complexité bornée sont dans l'archive) : toute étiquette « non trouvé » y est une faille de nouveauté. Un
proposeur qui lit la description exacte des gardes et des juges, et, dans un bras, leurs verdicts, y tente sa chance ; le
**gain de corruption** de la chaîne est la part de promotions obtenues. Aucune recette n'est écrite ici ni dans les sorties.

---

## 3. Mesures

### 3.1 Vrai

Un énoncé est dit **« vrai (formel, fidèle) »** si et seulement si : Lean l'**accepte** sous G-L1 à G-L7 ; il passe **G-V**
(non vide) ; l'**audit de fidélité** d'une autre famille, sur l'énoncé imprimé par Lean, le dit fidèle à la conjecture, et la
rétro-traduction aveugle et l'épreuve du contre-exemple déclaré concordent. « Vrai » ne vaut que pour l'énoncé formel et la
version épinglée ; la vérité de la conjecture en langue naturelle repose sur la fidélité, mesurée, jamais acquise.
**Mesures** : taux de fausses acceptations sur le **banc des tricheurs scriptés** (B2) et sur les **cibles fausses plantées**
(B4), sans puis avec attaque adaptative ; taux d'acceptations infidèles sur un tirage audité ; part d'OUVERT.

### 3.2 Neuf

- **Jamais « nouveau »** : trois étiquettes (maillon 4). « Non trouvé dans les pièces lues » est une affirmation sur des
  pièces, pas sur le champ (R8) ; une zone qui paraît vierge reste une question.
- **Plancher mécanique** (G-N, G-T) : l'énoncé n'est pas fermé par l'automatisation de la bibliothèque au commit épinglé, dans
  un budget fixé, et n'égale pas un énoncé de la bibliothèque après normalisation. C'est une nouveauté **relative à Mathlib**,
  rien de plus : Mathlib n'est pas la littérature.
- **Recherche d'antériorité** : moisson par métadonnées, puis lecture sur PDF empreinté, page citée (R7), par un lecteur d'une
  autre lignée que les proposeurs.
- **Taux de faux « neuf » mesuré** : sur la **banque d'énoncés connus plantés** (B1) — énoncés de la bibliothèque et de la
  littérature, reformulés par une troisième famille (renommage, notation changée, spécialisation, contraposée, assemblage de
  deux énoncés), mêlés anonymement aux énoncés réels ; la clé (référence de chaque connu) n'est jamais servie.
- **Contamination** : un connu célèbre peut être reconnu par mémoire, un connu obscur non ; B1 est **stratifiée** (célèbre,
  obscur, publié après la date de coupure déclarée des modèles si une telle source est lisible) et le taux est rapporté par
  strate. Les mondes plantés (B3) sont neufs par construction : la contamination y est nulle, la nouveauté y est triviale, et
  ils ne servent donc pas à mesurer le juge de nouveauté, seulement les proposeurs.

### 3.3 Utile

- **Utile ⇔ ferme ou réfute une cible scellée** : avant toute génération, chaque question du programme retenue (Q1 à Q5 ou
  d'autres) reçoit une **carte de cible** : énoncé formel visé (ou ses sous-buts) écrit en Lean avec `sorry`, relu par deux
  familles et par Lazar pour la fidélité **avant** scellement (la fidélité de la cible se juge une fois, hors pression) ;
  **table de décision** : ce qui change dans le programme si la cible est démontrée, si elle est réfutée, si elle reste
  ouverte. Un énoncé qui ferme la cible ou un sous-but scellé, dans Lean, est utile ; c'est mécanique.
- **Tout le reste est information** : un lemme hors cible peut être intéressant ; il est rapporté, relu par Lazar, et ne compte
  pas dans les mesures d'utilité. Le verdict d'un juge d'utilité à modèle n'est jamais un critère (N-058).
- **Utile ≠ décisif** : une cible fermée change un dessin, un seuil, une lecture ou une revendication ; jamais l'issue d'une
  hypothèse empirique (MAT-004) ; son usage dans le programme passe par un préenregistrement scellé (R1 ; N-065, rôle 2).

### 3.4 Oracles plantés et coût (N-058)

| oracle | ce qu'il contient | ce qu'il mesure | juge seul ? |
|---|---|---|---|
| **B1 banque d'énoncés connus plantés** | connus reformulés par une troisième famille, clé des références scellée | taux de faux « neuf » du maillon 4, par strate | non : la clé décide |
| **B2 banc des tricheurs scriptés** (sans modèle, processeur) | énoncés vides, triviaux, voisins, déguisés ; fichiers qui tentent les failles connues du contrôle | taux de fausses acceptations des maillons 2 et 3 ; chaque garde éprouvée (R5) | non : la construction décide |
| **B3 mondes mathématiques plantés** | définitions neuves tirées par graine (par exemple une structure finie ou une famille paramétrée), vérité de leurs énoncés **calculée** par énumération jusqu'à une taille fixée et, quand c'est possible, démontrée ; énoncés vrais et faux plantés | **rendement des proposeurs** : énoncés vrais plantés retrouvés, faux rejetés, **par dollar** — le seul critère de composition (N-058) | non : le calcul décide |
| **B4 mondes où toute promotion est fausse** | cibles fausses plantées ; mondes à archive complète | **gain de corruption** de la chaîne sous attaque adaptative (§ 2.4) | non : la construction décide |
| **coût** | dollars par appel et par espèce, heures de machine, temps humain | coût par énoncé vrai fidèle, par cible fermée, par connu correctement étiqueté | — |

Le verdict d'un juge à modèle n'est lu, comme critère, **que contre une clé plantée** ; sur les énoncés réels (cibles du
programme), il est une information pour la relecture humaine.

### 3.5 Ce qui est préenregistrable (forme ; aucune valeur de seuil proposée ici)

1. **Taux de faux « neuf »** du juge de nouveauté sur B1, par strate, avec borne haute ; issue écrite d'avance : au-dessus du
   seuil gelé, aucune étiquette « non trouvé » du juge n'est lue sur les énoncés réels.
2. **Taux de fausses acceptations** de la chaîne sur B2 et sur les cibles fausses de B4, sans attaque ; issue : toute
   acceptation sur B2 bloque la chaîne (défaut de garde, R5).
3. **Gain de corruption** sous attaque adaptative sur B4, rapporté avec les courses qui l'ont précédé, jamais seul (règle
   gelée de la série d'attaques du juge [J-21]) ; comparé au taux sans attaque (plancher de l'essai pour E1).
4. **Rendement des proposeurs sur B3** (vrais retrouvés, faux rejetés, par dollar), unité = le monde ; témoin « un modèle,
   vote à k, coût apparié » (N-045) [J-33] ; décide de la composition, rien d'autre.
5. **Cibles fermées ou réfutées** parmi les cibles scellées, avec coût par cible ; chaque fermeture relue (maillon 6).
6. **Taux d'acceptations infidèles** sur un tirage audité des énoncés réels, comparé au taux de l'essai.
7. **Symétrie (R3, R4)** : un tour où « beaucoup d'énoncés neufs et utiles » sortent déclenche le même audit qu'un tour
   où rien ne sort (relecture d'un tirage, contrôle de fuite des clés, recherche d'antériorité étendue) ; trop beau = réserve.

Non préenregistrable en l'état : la **valeur** mathématique d'un énoncé hors cible ; la nouveauté **pour le champ** ;
l'intérêt d'une conjecture ouverte. Ce sont des lectures humaines, dites comme telles.

---

## 4. Dépendances

### 4.1 De l'essai (b) « preuve formelle contre suite bon marché »

| ce qu'il faut | pourquoi | état |
|---|---|---|
| **carte de couverture par domaine** (saines acceptées avec énoncé fidèle, D1 à D5) et issue **O0** | dit où Lean peut être arbitre ; les cibles Q1 à Q5 tombent en D1, D2, D5 | essai non couru ; D-1a présenté, aucun GO ; D-1b après préenregistrement complet [J-5, J-15] |
| **taux d'acceptations infidèles sans pression**, rappel sur K5 et K2 | plancher de E1 ; K2 (hypothèse absente) est l'erreur typique d'une conjecture | idem |
| **coût par item formel et temps mural** (attendu SUPPOSÉ 1,162 USD, pire réaliste 3,082, plafond 4 par item) [J-12] | base des ordres de grandeur du § 5 | idem ; profils supposés, mesurés au pilote |
| **cloison** : machine isolée, chaîne et Mathlib épinglées en lecture seule, gardes G-L1 à G-L7 et épreuve d'isolement éprouvées (R5), harnais à comptage par item [J-14] | condition de tout code écrit par un modèle | dans le périmètre de D-1a, non accordé |
| **réponse à D-3** (qui formalise ; mêmes modèles ou familles différentes) | détermine ce que le maillon 2 mesure | proposée (a), défaut sous 48 heures dans l'essai |

### 4.2 De l'étape 2 (N12 (b))

- **Les couches 3 et 4 restent fermées jusqu'aux résultats de l'étape 2** [J-2] ; la mesure de ce que le catalogue manque y est
  préenregistrée. Aucune pièce lue ne fixe la date de ces résultats ni **qui décide l'ouverture de la couche 4** (les espèces
  ne le nomment pas, sauf E « en général ») [J-6] : je propose que ce soit Lazar, sur trois pièces (résultats de l'étape 2,
  issue de l'essai, cette note), sans règle automatique.
- **Ne peut pas commencer avant** : toute course de génération (payée) ; toute construction de banque plantée (B1, B3, B4) qui
  appelle un modèle ; toute attaque adaptative ; tout scellement de carte de cible en Lean (Lean n'est pas installé, D-1a).

### 4.3 Du papier C (N-065, juges sous attaque)

- Le juge de nouveauté et le juge d'utilité sont des **juges de la recherche automatisée** : exactement l'objet du rôle 1 de
  N-065 [J-11, J-29]. La méthode de l'attaque A1 (proposeur qui lit la règle du juge, mondes où toute promotion est fausse)
  est celle de B4 [J-21] ; N-064 (point 3) rappelle que le principe de ces attaques est occupé depuis 2015 (Dwork et al. ;
  Blum et Hardt) et que seule la forme est revendiquée [J-24].
- **Dépend de** : la conception v3 du juge-tournoi (à écrire) pour le juge génératif ; le nœud de la collision Qu, Chen et
  Wang ; les citations obligatoires de N-064 dans toute pièce qui présente le pilier.
- **Rattacher le pilier au papier C est une décision de revendication** (nœud, DP-5) : ce texte ne le fait pas.

### 4.4 Autres préalables

- La **carte des hypothèses** corrigée et versée sur `main` (Q2 à Q5) [J-16].
- **Antériorités lues** (R8, § 6.3) avant toute revendication.
- **Accès** des fournisseurs (troisième famille pour B1 ; l'identifiant de GPT-6 Astra reste « à confirmer » dans l'essai) :
  nœud de compte si un accès manque.
- **Réseau** pour la moisson et pour télécharger les PDF : nœud d'environnement, hors de la machine isolée.

---

## 5. Coûts (ordres de grandeur seulement ; aucun devis)

Calcul par `calculs-v1/ordres-de-grandeur-pilier-generation-v1.py`, sortie `calculs-v1/sortie-ordres-de-grandeur-pilier-generation-v1.txt`
(empreintes en table). **Hypothèses nommées, aucune vérifiée** :

- **Prix** par million de jetons, repris de l'essai tels quels avec leur statut : Opus 5.5 à 4 / 20 (« à vérifier ») ; Kimi
  K3.1 Pro à 2 / 10 (« vérifiés le 30 octobre », rapporté) ; Gemini 4 Argon au barème prudent 10 / 50 (une page archivée
  donne moins jusqu'au 30 novembre) ; GPT-6 Astra à 10 / 50 (« SUPPOSÉS ») [J-12].
- **Profils** : proposition 10 k d'entrée et 3 k de sortie (S-02) ; formalisation et preuve = l'item du bras L de l'essai
  (1,162 USD attendu, 3,082 au profil pire réaliste) jusqu'à un **plafond de 10 USD par énoncé neuf** (S-01, choix de dessin,
  non mesuré : un énoncé neuf demande plus qu'une preuve courte connue) ; fidélité = deux appels du profil du relecteur de
  l'essai ; nouveauté = une ou deux recherches à 8 k et 4 k ; utilité = un appel, information seulement.
- **Pilote hypothétique** (S-06, effectifs non dimensionnés) : 200 énoncés candidats, 100 connus plantés, une attaque
  adaptative de 50 à 200 USD (S-07, ordre de grandeur), un banc de 100 tricheurs scriptés (processeur seul).

| poste | bas | haut |
|---|---|---|
| un énoncé candidat par toute la chaîne | ≈ 1,8 USD | ≈ 11 USD |
| 200 candidats | ≈ 370 USD | ≈ 2 220 USD |
| 100 connus plantés | ≈ 200 USD | ≈ 530 USD |
| **total d'appels du pilote** | **≈ 620 USD** | **≈ 2 950 USD** |
| machine (≈ 28 à 103 heures murales à 3 processus ; 0,10 à 0,40 USD l'heure, sans source) | ≈ 3 USD | ≈ 41 USD (≈ 134 à la borne haute de 1,30) |
| **relecture humaine** (5 % à 20 % des candidats franchissent les gardes ; 15 à 30 minutes chacun) | ≈ 2,5 heures | ≈ 20 heures |

Lecture : **un pilote coûte de l'ordre de mille dollars**, comparable à la phase 2 de l'essai (plafond indicatif 1 950 USD) [J-5] ; le poste qui décide est le
**plafond par énoncé neuf** (S-01) ; le coût caché est le **temps de Lazar**, borné par la part d'énoncés qui franchissent les
gardes. Hors calcul : temps des sous-agents de la session (la question de savoir si c'est une dépense reste ouverte dans
l'essai, § 8, point 6) ; un mathématicien extérieur (contact externe, nœud, prix inconnu).

---

## 6. Risques, et ce qu'on ne dira pas

### 6.1 Risques

1. **Goodhart sur la chaîne** : un générateur optimise vers ce que les gardes laissent passer (E2, E3, E5) ; d'où B2, B4 et
   le gain de corruption mesuré avant toute lecture d'énoncés réels.
2. **Fidélité sous pression** : le taux de l'essai est un plancher sans pression ; sous génération, il peut monter, et il
   ne se voit que par l'audit.
3. **Nouveauté surestimée** : un juge à modèle étiquette du connu comme neuf (E4), surtout reformulé ; la brèche de W2 en est
   l'exemple interne [J-21].
4. **Utilité dérivée** : des énoncés vrais et neufs qui ne changent rien (E6) occupent le temps humain ; d'où les cibles
   scellées.
5. **Ouverture de fait de la couche 4** : construire des banques, sceller des cibles en Lean ou lancer des générateurs avant les
   résultats de l'étape 2 contredirait N12 (b).
6. **Cloison** : du code écrit par un modèle s'exécute à la compilation ; sans la machine isolée de l'essai, le pilier
   n'existe pas.
7. **Même famille** : proposeur, formaliseur et juge de la même famille partagent leurs angles morts ; familles séparées
   par rôle, et juge de nouveauté d'une autre lignée (N-053, point 4) [J-9].
8. **Temps de Lazar** comme goulot ; **dérive de G0** : le pilier n'est pas sur le chemin de G0 [J-31] et ne doit pas en
   prendre le temps.
9. **Versions** : une preuve vaut pour un commit de Mathlib ; un changement de version peut la casser ou changer une
   convention.
10. **Multiplicité** : beaucoup d'énoncés tentés, peu retenus ; une preuve ne devient pas fausse par multiplicité ;
    l'**intérêt** choisi après coup parmi beaucoup d'essais, lui, est biaisé ; seules les cibles scellées comptent.

### 6.2 Ce qu'on ne dira pas

- « L'organisme produit des mathématiques nouvelles » : aucune partie ne le fait aujourd'hui [J-19] ; ce texte est une
  conception.
- « Vérifié par Lean, donc vrai » : seul l'énoncé formel l'est, à cette version, sous ces gardes ; la conjecture dépend de la
  fidélité.
- « Nouveau » : seulement « non trouvé dans les pièces lues », au-dessus d'un plancher relatif à Mathlib.
- « Utile » au-delà des cibles scellées.
- « Un théorème tranche une hypothèse du programme » : il change un dessin, un seuil, une lecture, jamais une issue empirique
  (MAT-004) ; « δ > 0 » se tranche à G1.
- Aucun chiffre de l'état de l'art (R7) : aucun PDF sur la preuve automatique, la formalisation automatique ou la génération
  de conjectures n'a été trouvé sous `docs/sources/pdf/` (noms filtrés) ; aucune comparaison de performance.
- Aucune recette d'attaque contre un juge ou un arbitre (R-607).

### 6.3 Antériorités probables : questions à vérifier (R8), sans affirmation

Hors POPPER et le rapport « Jr. AI Scientist » (au dépôt), aucun PDF de ces zones n'a été trouvé sous `docs/sources/pdf/`
(noms filtrés) ; les noms ci-dessous viennent de la mémoire du rédacteur et **ne sont pas vérifiés**.
1. **Systèmes de preuve automatique sur Lean et Mathlib** (par exemple AlphaProof, DeepSeek-Prover, LeanDojo, Lean Copilot) :
   occupent-ils la démonstration d'énoncés **donnés** seulement, ou aussi le choix d'énoncés ? Mesurent-ils la triche sur le
   contrôle (axiomes, `sorry` caché, exécution à la compilation) ?
2. **Formalisation automatique** (par exemple les travaux sur la formalisation par modèles de langue, les bancs miniF2F et
   ProofNet) : la fidélité par rétro-traduction et par épreuve de contre-exemple est-elle déjà une méthode établie ? Les
   conventions de Mathlib comme source d'infidélité y sont-elles documentées ?
3. **Génération de conjectures** (par exemple AM de Lenat, Graffiti, HR, la « Ramanujan Machine », FunSearch, AlphaEvolve) :
   la mesure de la nouveauté contre une banque de connus plantés, ou le rendement de proposeurs sur des mondes plantés à
   vérité calculable, y existent-ils ?
4. **Agents de recherche automatisée et juges de nouveauté** (Co-Scientist, cité ; POPPER, cité ; le rapport de risques
   « Jr. AI Scientist », PDF au dépôt, non lu ici) : un juge de nouveauté y est-il mis sous attaque ?
5. **Contamination des bancs de preuve** : documentée ? Comment la stratifier ?
Toute zone qui paraîtrait vierge après ces lectures resterait une **question**, durcie par la lecture des travaux qui les
citent.

---

## 7. Décisions pour Lazar

**DP-1 — Statut de cette note et calendrier.** Garder la note comme pièce au dossier de la décision d'ouverture de la couche 4,
prise après les résultats de l'étape 2. **Enjeu** : N12 (b) ; éviter une ouverture de fait. **Options** : (a) **pièce au
dossier, rien ne se prépare avant les résultats de l'étape 2 et de l'essai** (avantage : N12 (b) tenue sans ambiguïté ;
inconvénient : le pilier démarrera à froid) ; (b) autoriser maintenant le seul travail de table, sans appel de modèle facturé
ni Lean : cartes de cibles en langue naturelle (Q1 à Q5), contrat écrit des banques B1 à B4, liste des tricheurs scriptés
(avantage : gain de quelques semaines ; inconvénient : à la limite de N12 (b), temps de sous-agents) ; (c) pilote de génération
maintenant (avantage : matériau tôt ; inconvénient : contraire à N12 (b) ; écarté). **Recommandation** : (a), confiance 0,6 ; (b) si Lazar juge que le travail de table
n'ouvre pas la couche. **Défaut** : aucun (ouverture de couche).

**DP-2 — Définition de « utile ».** Utile = fermer ou réfuter, dans Lean, une cible scellée d'avance tirée d'une question du
programme, avec sa table de décision. **Enjeu** : sans définition mécanique, l'utilité devient le verdict d'un juge (N-058).
**Options** : (a) **cibles scellées seulement ; le reste est information** (avantage : mécanique, opposable ; inconvénient :
étroit, les trouvailles hors cible ne comptent pas) ; (b) cibles scellées plus un juge d'utilité à modèle comme critère
secondaire (avantage : plus large ; inconvénient : critère porté par un verdict de juge, corruptible) ; (c) juge d'utilité seul
(écarté). **Recommandation** : (a), confiance 0,65. **Défaut sous 48 heures** : (a), comme dessin seulement ; rien n'est construit.

**DP-3 — Définition de « neuf ».** Trois étiquettes (« connu », « corollaire immédiat de la bibliothèque », « non trouvé dans les
pièces lues »), jamais « nouveau ». **Enjeu** : la nouveauté est la propriété la plus exposée à la triche (brèche de W2) et au
faux vide (R8). **Options** : (a) **plancher mécanique, recherche d'antériorité sur PDF et taux de faux « neuf » mesuré sur une
banque de connus plantés** (avantage : chaque étiquette a un oracle ; inconvénient : la banque coûte, ≈ 200 à 530 USD au
pilote hypothétique) ; (b) plancher mécanique seul (avantage : presque gratuit ; inconvénient : nouveauté relative à Mathlib
seulement) ; (c) juge à modèle seul (écarté). **Recommandation** : (a), confiance 0,65. **Défaut sous 48 heures** : (a), comme
dessin seulement ; la banque attend un devis et un GO.

**DP-4 — Oracle de composition des proposeurs.** Étendre N-058 au pilier : la composition se juge sur des mondes mathématiques
plantés à vérité calculable et sur le coût, jamais sur ce que la chaîne accepte. **Enjeu** : sans oracle planté, choisir les
proposeurs reviendrait à les sélectionner sur un verdict de juge (N-053). **Options** : (a) **mondes synthétiques neufs (B3)**
(avantage : vérité calculée, aucune contamination ; inconvénient : loin des cibles réelles du programme) ; (b) énoncés connus
retirés de la bibliothèque, à redécouvrir (avantage : proches des vraies mathématiques ; inconvénient : contamination par
mémoire) ; (c) les deux, rapportés séparément. **Recommandation** : (c), (a) comme critère et (b) comme information ;
confiance 0,55. **Défaut sous 48 heures** : (c), comme dessin seulement.

**DP-5 — Rattacher la chaîne du pilier au papier C.** Mesurer la corruptibilité d'un arbitre formel et d'un juge de nouveauté
comme troisième sorte de juge de la recherche automatisée. **Enjeu** : revendication du papier C (nœud) ; les principes sont
occupés (N-064), seule une forme peut l'être. **Options** : (a) oui, comme bras prévu après l'ouverture (avantage : donne au
pilier une mesure publiable même sans mathématiques neuves ; inconvénient : élargit le papier C avant que sa première mesure
soit écrite) ; (b) non, le pilier reste hors du papier C (avantage : papier C resserré ; inconvénient : la mesure B4 perd son
cadre) ; (c) décider après l'issue de l'essai et la collision Qu-Chen-Wang (avantage : décision sur pièces ; inconvénient : la
mesure B4 reste sans cadre jusque-là). **Recommandation** : (c), confiance 0,55. **Défaut** : aucun (revendication).

**DP-6 — Antériorités avant tout scellement de cible.** Faire lire, sur PDF empreinté, les zones du § 6.3 avant toute carte de
cible et toute revendication. **Enjeu** : R8 ; la génération de conjectures et la formalisation automatique sont des zones où une
antériorité est probable (question, non affirmation). **Options** : (a) **lecture maintenant, en parallèle de l'essai, sans calcul payé** (avantage : rien
n'attend la lecture le jour de l'ouverture ; inconvénient : temps de sous-agents, réseau pour les PDF) ; (b) lecture au moment
de l'ouverture (avantage : aucun coût avant décision ; inconvénient : décision d'ouverture sans antériorité). **Recommandation** :
(a), confiance 0,6. **Défaut sous 48 heures** : (a) si le temps des sous-agents n'est pas une dépense au sens du programme
(question ouverte de l'essai, § 8, point 6) ; sinon aucun.

---

## 8. Questions ouvertes (détail au journal)

1. Qui décide l'ouverture de la couche 4, et sur quelles pièces (non nommé par les espèces).
2. La carte des hypothèses v1 : où la lire, quand elle sera corrigée sur `main` ; Q2 à Q5 en dépendent.
3. L'acceptation par Lean peut-elle devenir un signal d'entraînement d'un proposeur (couche 3, N-045) sans contredire
   l'invariant de N-053 ? Changement d'hypothèse, nœud.
4. Les conventions de Mathlib à la version épinglée (division par zéro, soustraction des entiers naturels, racine et logarithme
   hors domaine) : liste exacte à établir sur la chaîne installée (D-1a).
5. Une source lisible de la date de coupure des modèles, pour la strate « publié après » de B1.
6. Le temps des sous-agents est-il une dépense (question ouverte de l'essai, § 8, point 6) ?

---

## Table des empreintes (SHA-256, calculées par script à l'assemblage ; aucune valeur retapée)

| pièce | chemin | sha256 |
|---|---|---|
| consigne de cette note | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-note-pilier-generation-v1.md` | `61ec586c07037c7db3ab86fec9821df787de081a2f6d5083aa3ce625cf2bdce5` |
| interdits communs v2 | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` | `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` |
| registre des décisions (vivant) | `registres/decisions.md` | à la lecture (14:12 UTC) `8a06c09316e58fbe1369849cbb6d8f96fe0d84ba406a3ffdb00e65c55256dfde` ; à l'assemblage `d0f731bc1e767ea820dc0565d6adfdd98c3120120d7b89cac37b650a1c2ddcd0` (lignes ajoutées en fin : R-2241, R-2242 ; lignes citées inchangées) |
| N-044 | `docs/decisions/decision-N-044-v1.md` | `2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf` |
| N-045 v2 | `docs/decisions/decision-N-045-v2.md` | `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d` |
| N-058 | `docs/decisions/decision-N-058-v1.md` | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` |
| N-064 | `docs/decisions/decision-N-064-v1.md` | `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97` |
| N-065 | `docs/decisions/decision-N-065-v1.md` | `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4` |
| synthèse du tour 2 N12-N13 | `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-tour2-v1.md` | `6ef6bc2e1cbea69b0b47f20508fa09391e7c2271785287c470dc632de5a2b1ce` |
| essai Lean, brouillon 3 | `brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon3.md` | `717259ed1dfd5e4e9c591b3c7d22a4316ec1fe1195ea83bb887ca3f60fd2ac37` |
| essai Lean, contre-lecture 1 | `prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon1-cl1.md` | `f565d51cd39ae047d50a1774e79c67301f54ab5c1c107c4cba50193d33ba7744` |
| essai Lean, vérification courte | `prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon2-verification-courte-v1.md` | `38e40d21e60f7588233b3fda27b365c6a48abb97ecb9dd3a5ff94cb44ad73d8a` |
| programme de l'organisme v3 | `docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v3.md` | `bbde32b7eedc05eb5c3bc1f67c2282e4ef01fef61fd88c5afac6c11be93064fc` |
| inventaire des idées v4 | `docs/notes/rapports-directeur/programme-organisme-complet-v1/inventaire-idees-organisme-v4.md` | `66e05f31f56a239f437c338fa89f4de02589344ee59b36a4ddb24679ed79be2e` |
| programme d'entretien v16 | `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` | `186173d9d9b949bfb3922503adff1be9d60f49f07fb975750de4c88bd60a060e` |
| calcul des ordres de grandeur | `docs/notes/ideation-organisme-v1/pilier-generation-v1/calculs-v1/ordres-de-grandeur-pilier-generation-v1.py` | `11c98699471539f2db5810c32144c8a8ceef098483e645096dfa82b4c83cb480` |
| sortie du calcul | `docs/notes/ideation-organisme-v1/pilier-generation-v1/calculs-v1/sortie-ordres-de-grandeur-pilier-generation-v1.txt` | `c2240177a29a1b9374f3f08a67642a8ea5bb05d422073f51331e6b0370164f93` |
| ce script | `docs/notes/ideation-organisme-v1/pilier-generation-v1/calculs-v1/table-empreintes-note-v1.py` | `1d65e917bbb06f76af53b1b0563cfc6d2a10907dcc125ec8ad7a0849d72e168e` |
| programme de conception de l'organisme v1 (branche du canal, lu par git show) | `origin/canal/conv-audit-n04:brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/programme-conception-organisme-v1.md` | `72fa0e609258d1a208195440c645f2b7f250c5c5bba70e304407ded09de3c6ff` |

Le journal (`note-conception-pilier-generation-v1-journal-v1.md`) porte l'empreinte de cette note ; la note ne porte pas la sienne.
