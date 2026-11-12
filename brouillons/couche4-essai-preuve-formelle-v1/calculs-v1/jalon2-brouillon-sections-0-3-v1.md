# Essai « preuve formelle contre suite bon marché » (couche 4, pas (b) de R-2199) — dessin et devis — v1, brouillon 1

- **Pour** : la session mère, puis Lazar. **Écrit par** : un sous-agent neuf (rédacteur), modèle **Opus 5.5** (`claude-opus-5-5`),
  session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, le 10 novembre 2026 (début 13:00:30 UTC, heures relevées par `date -u`).
  Je n'ai écrit ni les questions, ni les critères, ni les synthèses N12-N13. **Conflits déclarés** : je suis de la famille des
  espèces A et B du collisionneur et du même modèle que le lecteur du tour 2 ; je recommande plus bas Opus 5.5 comme modèle des
  deux bras de l'essai (§ 2.7) : un contre-lecteur d'un autre modèle doit vérifier que mon dessin ne favorise pas ce modèle.
- **Statut** : **brouillon 1, non contre-lu, non préenregistré**. Il devient un préenregistrement (R1) après contre-lecture par un
  sous-agent neuf (R2 ; un autre modèle de la même famille, comme le veut N-052 pour la boucle extérieure : Fable 5.1) et après le
  GO de Lazar. **Aucun appel de modèle, aucun réseau, aucune dépense** n'ont servi à l'écrire ; tous les chiffres de coût sont
  calculés par script (§ 4, table des empreintes) à partir de prix cités avec leur source ou marqués « à vérifier ».
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-devis-essai-preuve-formelle-couche4-v1.md`
  (`5403571b…`). Journal : `essai-preuve-formelle-devis-v1-journal-v1.md` (même dossier).

## Verdict

1. **L'essai est faisable sur processeur, en deux phases payées séparément.** Phase 1 (outillage puis pilote de 140 items) :
   **attendu ≈ 312 USD d'appels**, plafond proposé **450 USD** et au plus **50 USD de machine** (à vérifier). Phase 2
   (confirmation sur deux classes d'erreurs) : **attendu ≈ 800 USD** à l'effectif central, **≈ 1 250 USD** à l'effectif plafond,
   sur un **second GO** avec un devis refait sur les coûts mesurés au pilote. Rien n'est dépensé avant le GO de Lazar.
2. **Deux obstacles matériels avant toute dépense** : aucun vérificateur n'est installé ici (ni Lean, ni lake, ni elan, ni
   Mathlib, ni autre assistant de preuve), et le disque n'a que **2,7 Go libres** (94 % d'occupation), trop peu pour Mathlib
   (taille à vérifier) ; il faut une machine ou de la place, et l'accès réseau aux hôtes de la chaîne Lean (nœud d'environnement).
3. **L'essai ne rouvre pas la couche 4** : il produit une pièce (une classe d'erreurs mesurée, des fausses alertes bornées, un coût
   apparié) pour la décision que Lazar prendra après les résultats de l'étape 2 (N12 (b)). Ma prédiction (prior, § 1.4) est que la
   chaîne formelle **ne** franchit **pas** le critère conjoint ; le dessin est écrit pour que les deux issues soient lisibles (R3).

---

## 0. Statut, bornes, ce qui est repris

- **Décision** (R-959, N12 (b), mots de Lazar à conv-audit) : couches 3 et 4 fermées jusqu'aux résultats de l'étape 2 ; un seul
  pas permis, l'**essai sur processeur « preuve formelle contre suite bon marché »**, **sur devis d'appels de sous-agents**.
  **Ordre** (R-2199, 11:55 UTC) : (a) lecture du tour 2 (faite, R-2226), **(b) devis de cet essai, puis GO**, (c) note de
  conception du pilier « génération ». Ce texte est le (b).
- **Matériau repris** (synthèse du tour 2, `6ef6bc2e…`, § E.2 et E.4) : les **sept points tenus par au moins trois espèces** —
  vérificateur externe hors organisme ; conclusion bornée à une classe d'erreurs mesurée ; banque de confirmation séparée de la
  banque de découverte, construite par un tiers ; contrôles de fidélité de la formalisation (énoncé voisin prouvé, spécification
  altérée ou insuffisante) ; énoncés sains renotés pour mesurer les faux rejets ; puissance réglée sur les paires discordantes ;
  coût apparié — tous au statut « proposé, non tranché » ; je les adopte comme contraintes de dessin et je le dis. Les
  **désaccords** (qui formalise ; capacité de Lean ou chaîne complète ; une ou plusieurs classes ; suite d'un échec) sont tranchés
  ici seulement comme **options avec recommandation** (§ 2.7, § 7) : ils restent chez Lazar.
- **Points à la limite relevés par le lecteur du tour 2, non repris** (synthèse du tour 2, « Ce qui reste chez Lazar », point (1)
  à (4)) : aucune issue de cet essai n'est une **règle d'ouverture** de la couche 4 ; la suite bon marché **n'est pas** proposée
  comme **standard obligatoire du programme** ; le bornage à une classe d'erreurs est un **choix de dessin proposé par ce brouillon**
  (porté par les espèces A, B, C, D, E), **non une décision du directeur** ; l'essai **n'est pas** une « pièce sans dépense ».
- **Ce qu'aucune espèce n'a dit et que j'ajoute** (marqué « proposé par le rédacteur ») : l'objet vérifié est le **squelette de la
  preuve**, non le seul énoncé (§ 1.2) ; la définition opérationnelle d'un item fautif (§ 2.2) ; les jumelles saine/fautive
  issues d'une même graine (§ 2.3) ; le contrôle des graines par une famille hors des bras (§ 2.5) ; l'analyse conditionnelle aux
  paires formalisables (§ 3.7) ; le lien au pas (c) (§ 6).

---

## 1. Question, hypothèses, prédictions, métriques, seuils, issues

### 1.1 Question exacte

Sur une banque de **preuves mathématiques courtes, rédigées en langue naturelle avec des étapes numérotées**, dans cinq domaines
proches du programme, où un tiers a planté des erreurs de classes fixées d'avance et a gardé des jumelles saines : **la chaîne
« formalisation en Lean 4 avec Mathlib, puis vérification par le noyau de Lean, plus un contrôle de fidélité par un relecteur
d'une autre famille » détecte-t-elle, classe par classe, au moins δ de plus d'erreurs plantées que la « suite bon marché »
(lecture outillée par calcul symbolique et numérique, recherche de contre-exemples, mutation de l'énoncé, plus une relecture
indépendante par un modèle d'une autre famille), avec des fausses alertes sur les preuves saines sous un plafond φ_max, à
plafond de coût par item égal et avec le même modèle dans les deux bras ?**

### 1.2 Objet mesuré (estimand) et unité

- **Unité** : l'item (un énoncé et sa preuve numérotée). Chaque item est vu par les deux bras (L : formel ; S : suite), dans des
  contextes neufs : les observations sont **appariées par item**.
- **Verdict d'un bras** : `ACCEPTE` ou `NON-ACCEPTE` (tout le reste : rejet argumenté, infidélité relevée, délai, plafond de coût
  atteint, sortie invalide, refus). Le rejet porte une **étape localisée**.
- **Estimand primaire : la chaîne complète** (position E-T3 de la synthèse du tour 2), traducteur compris : ce qu'un vérificateur
  externe rendrait en usage. Rappel du bras b sur la classe k : r_b,k = P(NON-ACCEPTE | item fautif de classe k) ; fausses
  alertes : φ_b = P(NON-ACCEPTE | item sain). Différence appariée : **Δ_k = r_L,k − r_S,k**.
- **Piège nommé et fermé** : un bras qui ne sait rien formaliser « détecte » tout (rappel 1) et rejette tout le sain
  (φ = 1) ; c'est pourquoi aucune issue favorable n'existe sans le **plafond de fausses alertes** (§ 1.7), et pourquoi le
  rappel **conditionnel aux paires formalisables** est la première mesure secondaire (§ 3.7).
- **Ce qui est vérifié : le squelette, pas seulement l'énoncé** (proposé par le rédacteur). Une preuve fausse d'un énoncé vrai
  (cas ordinaire des classes K1, K3, K4) serait « vérifiée » si le bras L prouvait l'énoncé par un autre chemin. Le bras L doit
  donc formaliser **chaque étape numérotée i** comme une assertion intermédiaire nommée `etape_i` (dont l'énoncé formel est celui
  de l'étape écrite, prouvée par n'importe quelle tactique), puis l'énoncé final ; une garde mécanique vérifie la présence de toutes
  les étapes (§ 3.1) et le relecteur de fidélité vérifie leur correspondance.

### 1.3 Hypothèses, complémentaires par classe (règle B4 précisée, convergence G3 du tour 2)

Pour chaque classe k lue en confirmation : **H_L,k : Δ_k ≥ δ** ; **H_S,k : Δ_k < δ**. La zone où l'intervalle traverse δ est
**non concluante**, jamais une falsification. Les fausses alertes sont lues sur toutes les saines de la banque de confirmation.

### 1.4 Prédictions chiffrées du rédacteur, avec signe (priors, statut SUPPOSÉ ; aucun chiffre tiré de la littérature)

Écrites pour être démenties ; le dessin ne les vise pas (R3).
- **P1 — fausses alertes** : φ̂_L − φ̂_S ≥ **+0,15** (signe : la chaîne formelle rejette plus de preuves saines, par échecs de
  formalisation des étapes vraies). Confiance 0,7.
- **P2 — classe la plus favorable à Lean** : issue O3 ou O4, pas O1 ; Δ̂ dans [**−0,05 ; +0,20**[. Probabilité que j'attribue à
  O1 : **≈ 0,25**. Classement a priori des classes, de la plus à la moins favorable à Lean : K2 > K5 > K4 > K1 > K3.
- **P3 — paires formalisables** : Δ̂ conditionnel ≥ Δ̂ inconditionnel **+0,05** (signe : Lean détecte mieux là où il sait
  formaliser la jumelle saine).
- **P4 — coût** : rapport des **totaux** de dépense L/S dans [**2 ; 6**] (signe : L plus cher ; valeur centrale du devis : 3,1).
- **Aucune prédiction** sur le taux d'acceptations à énoncé infidèle (mesure descriptive, § 3.7).

### 1.5 Métriques

- **Primaires** : r_L,k, r_S,k et Δ_k par classe confirmée ; φ_L, φ_S et φ_L − φ_S ; dépense totale par bras et rapport des
  totaux L/S (jetons comptés à chaque appel par le harnais, prix du § 4.1).
- **Secondaires** : liste au § 3.7.

### 1.6 Seuils proposés (à geler par Lazar avant scellement ; § 7, D-4)

- **δ = 0,20** (gain absolu de rappel sur une classe). Raison : la chaîne formelle coûte environ trois fois la suite par item
  (§ 4.2) et exige une infrastructure (machine, Mathlib épinglée, gardes) ; un gain plus petit sur une classe ne paierait pas un
  vérificateur externe. Valeur de jugement, non dérivée d'une mesure.
- **φ_max = 0,30** : borne haute (Clopper–Pearson à 97,5 %) des fausses alertes de la chaîne formelle. Raison : au-delà, plus
  d'une preuve saine sur trois renvoyée à une relecture humaine.
- **Intervalles** : à 95 % bilatéraux pour Δ_k (méthode fixée au préenregistrement, § 3.6) ; séquence fixe sur deux classes (§ 3.6).

### 1.7 Issues écrites d'avance (aucune n'est visée)

Par classe k confirmée (B(·) borne basse, H(·) borne haute des intervalles) :

| Issue | Condition | Lecture écrite d'avance |
|---|---|---|
| **O1 gain établi** | B(Δ_k) > 0 **et** Δ̂_k ≥ δ **et** H(φ_L) ≤ φ_max | Sur cette banque plantée, à ce budget, avec ce modèle et cette version de Mathlib, la chaîne formelle détecte sur la classe k au moins δ de plus que la suite, à fausses alertes bornées. **Pièce** versée au dossier de la décision de Lazar après l'étape 2 ; n'ouvre rien. |
| **O2 gain au prix d'alertes** | B(Δ_k) > 0 **et** Δ̂_k ≥ δ **et** H(φ_L) > φ_max | La chaîne formelle trouve plus sur k, mais rejette trop de preuves saines pour servir de vérificateur à ce point de fonctionnement ; le coût des fausses alertes est rapporté. |
| **O3 gain sous le seuil** | H(Δ_k) < δ (sous-cas O3b si H(Δ_k) < 0 : suite meilleure) | Sur k, à ce seuil, la suite suffit sur cette banque ; rien sur les classes non testées, rien sur les erreurs de spécification, **aucun statut de norme** pour la suite. |
| **O4 non concluante** | tout autre cas | L'intervalle traverse δ ; aucune conclusion ; l'effectif nécessaire est rapporté, aucune relance sans nouveau devis ni GO. |
| **O0 chaîne non viable** (fin du pilote, § 3.8, A9) | φ̂_L > 0,60 sur les saines du pilote (symétrique : φ̂_S > 0,60 ⇒ « suite non viable ») | La chaîne ne vérifie pas, à ce budget, des preuves courtes saines de ces domaines ; pas de confirmation ; le taux de formalisation par domaine est rapporté (utile au pas (c), § 6). |

Propriété vérifiée par simulation (§ 3.6) : à la frontière Δ = δ, la condition de rappel de O1 sort **environ une fois sur deux**
(0,52 à 0,55) : la règle ne penche pas vers le gain.

### 1.8 Symétrie (R3, R4)

Un O1 propre (gain net, fausses alertes basses) **et** un O3 propre (suite meilleure partout) déclenchent le **même audit** avant
remise : relecture des 20 items discordants tirés au hasard (graine consignée), vérification que la clé n'a pas fui (dates de
scellement), classifieur de style relancé sur la banque de confirmation, audit de fidélité étendu à toutes les acceptations.

---

## 2. Banque d'items

### 2.1 Source des graines (options ; recommandation)

| Option | Avantage | Inconvénient |
|---|---|---|
| **(a) graines neuves écrites par le planteur** sur une liste de domaines fixée (recommandé) | pas de formalisation publique préexistante ; domaines choisis pour le programme ; volume réglable | des théorèmes classiques restent mémorisés par les modèles (sans effet sur la comparaison appariée, qui porte sur la **preuve écrite**) |
| (b) jeux publics de preuves déjà formalisées | référence de difficulté connue | **fuite** : énoncés formels et preuves publiés, contamination probable des modèles ; licences à vérifier ; téléchargement (réseau) |
| (c) lemmes du programme (carte des hypothèses v1, `f7dfe5fd…` : lemme maître L0 et 21 lemmes ; programme d'entretien v16, l. 386 et 807, « Vérification formelle (Lean) du lemme maître L0 et des 21 lemmes | conv-audit | à ouvrir ») | c'est l'usage visé ; erreurs éventuellement réelles | 22 items seulement ; justesse non établie, donc **pas d'étiquette** ; ne peut pas servir à la confirmation |

Recommandation : **(a)** pour les deux banques ; **(c)** en **bras descriptif** facultatif (« banque d'usage », § 7, D-6), sans
revendication, après le pilote. (b) écarté.

### 2.2 Classes d'erreurs et domaines (taxonomie fixée avant toute observation, indépendante de la facilité de formalisation)

**Définition opérationnelle d'un item fautif** (proposée par le rédacteur) : la preuve contient au moins une **assertion écrite**
(étape i, ou l'énoncé annoncé au regard de la dernière étape) **fausse pour au moins une instance admissible** des hypothèses
énoncées. Les « bonnes assertions mal justifiées » sont **exclues** de la banque : aucun des deux bras ne peut y être noté
équitablement. Un item **sain** : toutes les assertions vraies et chacune découlant des précédentes ; l'énoncé annoncé découle de
la dernière étape.

| Classe | Nature (le planteur ne reçoit que ce texte et des exemples génériques) | Ancrage dans l'expérience du programme |
|---|---|---|
| **K1 coquille de relation** | inégalité stricte ou large, sens, signe, indice, borne d'une somme décalée | coquilles d'une preuve publiée trouvées par un lecteur neuf avec script (« < λ » contre « ≤ λ », ligne de W′(p) mal imprimée : synthèse v2 l. 84, 89, 169) |
| **K2 hypothèse absente** | un résultat appliqué hors de ses hypothèses, ou une régularité implicite non énoncée, de sorte qu'une étape devient fausse pour une instance admissible | théorème appliqué hors hypothèses (synthèse v2 l. 86) ; régularité non énoncée (l. 89) |
| **K3 calcul faux** | constante, facteur, exposant ou étape algébrique fausse, conclusion restée plausible | — |
| **K4 faute de logique** | quantificateurs permutés, réciproque prise pour l'implication, cas oublié, récurrence mal fondée, rendant une assertion fausse | — |
| **K5 énoncé voisin** | les étapes sont justes mais établissent un énoncé plus faible ou différent ; l'énoncé annoncé est **faux** (contre-exemple dans la clé) | contrôle de fidélité intégré : « énoncé voisin prouvé » (synthèse du tour 2, § E.2 (ii), § E.4) |

**Domaines** (strates, cinq) : D1 inégalités réelles et analyse élémentaire ; D2 probabilités discrètes et inégalités de
concentration élémentaires ; D3 algèbre linéaire de dimension finie ; D4 combinatoire et dénombrement ; D5 statistique du programme
(identités de calibration, règles de décision, martingales simples). La couverture de Mathlib varie selon les domaines : c'est une
covariable rapportée, pas un critère de choix des items.

### 2.3 Construction (graine → jumelle saine renotée → jumelle fautive)

1. Le **planteur** écrit une graine : énoncé et preuve courte (au plus 25 lignes, 3 à 10 étapes numérotées), dans un domaine et
   pour une classe tirés par `numpy.random.SeedSequence` (R9 ; carré latin domaine × classe, au plus 3 graines par case au
   pilote).
2. Il produit la **jumelle saine renotée** (variables renommées, notation changée, numérotation gardée) : c'est l'item sain.
3. Il plante sur **cette même version renotée** une erreur de la classe tirée, édition minimale plus ajustements de surface :
   c'est l'item fautif. Saine et fautive sortent ainsi du **même** procédé de réécriture : le seul écart est l'erreur.
4. **Clé** (scellée à part, jamais servie aux bras) : classe, étape fautive, explication, et, **si disponible**, un témoin
   numérique de l'erreur (instance où l'assertion est fausse) vérifié par calcul au moment de la construction. L'existence d'un
   témoin numérique est **enregistrée, jamais exigée** : l'exiger sélectionnerait les erreurs trouvables par la suite (biais de
   facilité, position E de la synthèse du tour 2, § E.4).
5. **Témoins de fonctionnement** (pilote seulement, hors analyse) : 5 fautes grossières et 5 preuves trivialement saines.
6. **Saines renotées une seconde fois** (pilote seulement) : 10 graines tirées reçoivent une deuxième renotation, pour mesurer la
   stabilité des verdicts sur une même preuve saine.

### 2.4 Découverte et confirmation séparées (convergence G9)

- **Banque de découverte = banque du pilote** (60 graines, 12 par classe, plus les 20 items de contrôle).
- **Banque de confirmation** : graines **neuves**, générées **après** le scellement des sorties du pilote, le **gel** des consignes,
  des outils, du harnais et de la version de Mathlib (position C-T3), et la **fiche de passage** scellée (classes retenues, effectifs,
  devis 2). Le planteur ne reçoit jamais les consignes des bras, ni les résultats du pilote, ni les classes retenues au-delà des
  quotas qu'on lui demande.

### 2.5 Contrôles de la banque

- **Graine saine contrôlée** par une famille **hors du planteur et hors des bras** (recommandé : Gemini 4 Argon) plus le calcul
  numérique du harnais ; une graine douteuse est **écartée avant** tout passage aux bras (surgénération de 20 % prévue). Pourquoi
  pas la famille des relecteurs des bras : elle sélectionnerait les graines qu'elle juge saines et abaisserait à tort les
  fausses alertes de la suite (choix du rédacteur, journal, jalon 1).
- **Classifieur de style** (processeur, obligatoire par analogie avec N-029 : prédicteur sur les traits du texte) : régression
  logistique sur n-grammes de caractères et longueur, validation croisée à 5 plis, saine contre fautive. Aire sous la courbe
  **> 0,70** sur la banque de découverte ⇒ banque refaite une fois (consigne du planteur en version neuve) ; seconde fois ⇒ arrêt
  (A6). Rapporté aussi sur la confirmation.
- **Adjudication à l'aveugle des cas litigieux** (analyse de sensibilité seulement ; l'analyse primaire garde les étiquettes de
  construction) : (i) toute saine qui reçoit au moins une alerte, (ii) toute fautive acceptée par au moins un bras, est soumise à
  l'adjudicateur (même famille que le contrôle des graines), **sans savoir quel bras a alerté** (localisations fusionnées et
  anonymisées), qui dit si l'étiquette de construction tient ; les items réétiquetés sont exclus dans l'analyse de sensibilité.

### 2.6 Contrôles de fidélité de la formalisation (points tenus par les cinq espèces)

- **Énoncé voisin prouvé** : la classe K5 entière ; une acceptation de L sur un item K5 est une infidélité ou un échec de garde.
- **Spécification altérée** : si L formalise une étape ou l'énoncé autrement que le texte (correction silencieuse d'une coquille,
  hypothèse ajoutée, énoncé affaibli), le **relecteur de fidélité** du bras L doit le relever ; sinon l'acceptation est comptée
  comme telle par la chaîne (manquée sur une fautive) et l'**audit de mesure** l'enregistre comme « acceptation à énoncé
  infidèle ». Convention de la position A-T3 (« preuve d'une spécification altérée = fausse alerte ») : rapportée en sensibilité
  sur les saines.
- **Énoncés sains renotés** : chaque saine est une renotation (§ 2.3), et 10 graines du pilote en ont deux (stabilité).
- **Audit de mesure** (hors bras, ne change aucun verdict) : sur un tirage de 50 % des items au pilote et 30 % en confirmation,
  l'auditeur reçoit l'énoncé et les étapes écrites et l'énoncé formel **imprimé par Lean** (non celui que l'agent déclare) et dit,
  étape par étape, fidèle ou non.

### 2.7 Qui plante, qui formalise, qui contrôle — désaccord des espèces (options ; recommandation)

Positions du tour 2 (synthèse, § E.2 (ii), § E.4) : C fait formaliser par un modèle d'une famille distincte de la suite ; E par
des « opérateurs » humains aux qualifications consignées ; A, B, D ne le disent pas.

| Option pour « qui formalise » | Avantage | Inconvénient |
|---|---|---|
| **(a) le même modèle dans les deux bras ; seuls les outils diffèrent** (recommandé) | l'écart mesure l'**outil** (Lean contre suite), non le modèle ; erreurs du modèle communes aux deux bras, d'où plus de paires concordantes et un test plus efficace | la chaîne n'est pas « le meilleur formaliseur possible » ; conflit de modèle avec le rédacteur (déclaré) |
| (b) formaliseur d'une autre famille que la suite (C) | proche d'un usage où l'on choisit le meilleur formaliseur | l'écart confond modèle et outil : un O1 ne dirait pas si c'est Lean qui gagne |
| (c) opérateurs humains (E) | fidélité probablement meilleure | contact externe et dépense (nœuds), délais, qualification à établir ; hors d'un essai « sur processeur » |

**Familles recommandées** (quatre familles, aucune ne juge son propre travail) :

| Rôle | Modèle | Raison |
|---|---|---|
| agents des bras L et S (et lecture nue au pilote) | **Opus 5.5** (Anthropic) | même modèle, effort fixé égal (`high`) ; coût 4 / 20 USD par million (§ 4.1) |
| relecteur interne aux bras (S : relecture indépendante de la preuve ; L : fidélité de l'énoncé et des étapes formelles) | **Kimi K3.1 Pro** (Moonshot) | autre famille, symétrique dans les deux bras, prix vérifié le 30 octobre (§ 4.1) |
| planteur | **GPT-6 Astra** (OpenAI) | troisième famille : la banque n'a le style d'aucun modèle des bras ; identifiant d'interface « rapporté, à confirmer » (`collisionneur_v8.py` l. 79–80) |
| contrôle des graines, audit de mesure, adjudication à l'aveugle | **Gemini 4 Argon** (Google) | quatrième famille, hors bras et hors planteur |
| contre-lecture du préenregistrement (R2) ; verdict (R13) | Fable 5.1 (contre-lecture), sous-agent neuf (verdict) | N-052 ; R2, R13 |

Variante de modèle des bras (option de D-3) : Sonnet 5.5 (≈ −36 % sur le pilote) ou Fable 5.2 (≈ +73 %) ; § 4.3.

---

## 3. Bras, puissance, plan d'analyse, arrêts

### 3.1 Bras L — preuve formelle

- **Agent** : Opus 5.5, effort `high`, outil unique `lean_verifier(fichier)` (compilation par `lake env lean` sous la chaîne
  épinglée, délai par appel), au plus 40 tours, 30 minutes murales et **4 USD** par item (§ 3.3).
- **Tâche** : écrire l'énoncé formel `enonce_item`, une assertion `etape_i` par étape numérotée (énoncé = celui de l'étape écrite),
  puis la conclusion ; prouver chaque `etape_i` par toute tactique ; rendre une sortie structurée (`ACCEPTE` ou rejet, étape,
  raison, fichier Lean).
- **Gardes mécaniques du harnais** (le verdict `ACCEPTE` exige toutes) : G-L1 compilation sans erreur ; G-L2 aucun `sorry` ni
  `admit`, et `#print axioms enonce_item` ne liste que `propext`, `Classical.choice`, `Quot.sound` ; G-L3 aucun `axiom`, `unsafe`,
  `@[implemented_by]`, `@[extern]` dans le fichier ; G-L4 présence de `etape_1` à `etape_m` (m = nombre d'étapes de l'item) et du
  nom `enonce_item` ; G-L5 l'énoncé et les étapes **imprimés par Lean** (`#check`) sont ce que reçoit le relecteur de fidélité.
  **R5** : chaque garde est éprouvée avant tout lancement sur un cas sain et sur un artefact (preuve à `sorry`, axiome ajouté,
  étape manquante, théorème renommé, `native_decide` dont l'axiome doit apparaître).
- **Relecteur de fidélité** (Kimi K3.1 Pro, un appel) : énoncé et étapes écrites contre énoncé et étapes formels imprimés ;
  étape par étape, fidèle ou non. **Verdict de la chaîne** : `ACCEPTE` seulement si l'agent accepte, les gardes passent et le
  relecteur ne relève aucune infidélité ; sinon `NON-ACCEPTE` avec le motif.

### 3.2 Bras S — suite bon marché (définition)

« Le meilleur assemblage bon marché » (D-T3, synthèse v2 l. 87) à outils locaux, sans assistant de preuve :
- **Relecteur indépendant** (Kimi K3.1 Pro, un appel) : critique étape par étape de la preuve écrite (étape suspecte, raison).
- **Agent** : Opus 5.5, effort `high`, outil `python(code)` en bac à sable sans réseau avec sympy 1.14.0, mpmath 1.3.0, numpy
  2.4.6, scipy 1.17.1 (installés dans `.venv`), et, si la mère l'installe (routine, registre de paquets), le solveur `z3` ;
  méthode imposée par la consigne : vérification symbolique des égalités et inégalités, **recherche de contre-exemples**
  numériques (tirages, bords, cas d'égalité), **mutation de l'énoncé** (l'argument « prouve »-t-il aussi l'énoncé muté faux ? si
  oui, l'étape qui ne distingue pas est suspecte), grille d'audit (hypothèses utilisées à chaque étape, sens des inégalités, cas
  limites). Il reçoit la critique du relecteur et rend la même sortie structurée que L. Mêmes plafonds que L.
- **Verdict de la suite** : `NON-ACCEPTE` si l'agent rejette **ou** si le relecteur marque une étape « fausse » (règle du « ou »,
  symétrique de celle de L).

### 3.3 Coût apparié

Même modèle, même effort, **même plafond par item (4 USD) et même délai mural (30 minutes)** dans les deux bras ; chaque bras
dépense ce qu'il dépense sous ce plafond ; la dépense réelle est mesurée par appel et rapportée (rapport des totaux, coût par
détection). Atteindre le plafond vaut `NON-ACCEPTE` (motif « plafond »), compté et rapporté. Ordre d'exécution : par **paires
complètes** (L puis S, ou S puis L tiré au hasard, sur le même item avant de passer au suivant), pour qu'une coupure budgétaire
laisse une banque plus petite mais appariée.

### 3.4 Diagnostics sans revendication

- **Lecture nue** (pilote seulement) : Opus 5.5 sans outil, un appel, même sortie : mesure ce que les outils de chaque bras
  ajoutent à la seule lecture.
- **Dérivés gratuits** des mêmes sorties : « relecteur seul » (la passe Kimi de S) ; **union L ∪ S** (alerte si l'un des deux
  alerte) : complémentarité de Lean **en plus** de la suite, à coût additionné.
- **Classifieur de style** (§ 2.5) : sert de contrôle de la banque et de plancher : un bras qui ne bat pas ce classifieur lit le
  style, pas la preuve.

### 3.5 Aveuglement et consignes

Les bras reçoivent l'item sous un identifiant tiré au hasard, sans classe, sans proportion de fautives (« la preuve peut être
juste ou fausse »), avec un **tronc de consigne commun** aux deux bras ; seules les instructions d'outil diffèrent. La clé reste
scellée jusqu'au scellement des sorties des deux bras pour la phase ; le script d'analyse est scellé avant. Sortie structurée
validée par schéma ; sortie invalide = `NON-ACCEPTE` (motif « sortie invalide »), rapportée. Un refus de modèle est enregistré
tel quel, sans reformulation (compté `NON-ACCEPTE`, motif « refus »).

### 3.6 Puissance réglée sur les paires discordantes ; effectifs ; correction

- **Dimensionnement** (script `calculs_devis_essai_v3.py`, sortie `sortie-calculs-devis-v3.txt`, table des empreintes) : pour une
  demi-largeur h = δ/2 = 0,10 de l'intervalle de Δ_k, n_k = ⌈1,96² · d / h²⌉ où d = P(paire discordante) : d = 0,10 → 39 ;
  0,15 → 58 ; 0,20 → 77 ; **0,25 → 97** ; 0,30 → 116 ; 0,35 → 135 ; 0,40 → 154 ; 0,50 → 193.
- **Probabilités des issues** (20 000 tirages par case, intervalle gabarit de Wald ajusté « +0,5 par case ») ; à n = 100 et
  d = 0,30 : Δ vrai 0 → « gain sous le seuil » 0,957 ; Δ vrai 0,10 → sous le seuil 0,491, non concluante 0,469, gain 0,040 ;
  **Δ vrai 0,20 → gain 0,534**, sous le seuil 0,034 ; Δ vrai 0,30 → gain 0,991. À n = 150 et d = 0,30 : 0,994 ; 0,643 / 0,343 ;
  0,534 ; 0,998.
- **Borne des fausses alertes** : probabilité que H(φ_L) ≤ 0,30 (Clopper–Pearson 97,5 %) : 120 saines → 0,972 si φ = 0,15,
  0,644 si φ = 0,20, 0,175 si φ = 0,25 ; 200 saines → 0,903 si φ = 0,20 ; 300 saines → 0,982 si φ = 0,20.
- **Règle d'effectif de la confirmation** (écrite maintenant, appliquée à la fiche de passage) : n_k = min(150, max(40,
  ⌈1,96² · d⁺ / 0,10²⌉)), d⁺ = maximum de la borne haute unilatérale à 80 % (Clopper–Pearson) de la discordance **globale** des 60
  fautives du pilote et de la discordance observée de la classe k. Chaque graine de confirmation donne une saine et une fautive :
  saines = n_1 + n_2 (192 à 300).
- **Choix des deux classes** (fiche de passage) : classes rangées par Δ̂_k du pilote, décroissant (ex æquo départagés par la
  graine) ; classe 1 = la première, classe 2 = la deuxième, **quel que soit le signe** : tester la classe la plus favorable à Lean
  rend un négatif aussi fort qu'il peut l'être, et un positif exposé à une banque neuve (R3, R4).
- **Correction** : séquence fixe ; la classe 1 est lue au seuil plein ; la classe 2 n'est lue de façon confirmatoire que si la
  classe 1 a rendu O1, O2 ou O3 ; sinon elle est rapportée comme exploratoire. Contrôle de l'erreur de famille **à vérifier par
  simulation** avant scellement (contre-lecture).
- **Méthode d'intervalle du préenregistrement** : choisie parmi l'intervalle de score de Tango et l'intervalle hybride de
  Newcombe pour proportions appariées (références RAPPORTÉES, à vérifier), par simulation de couverture aux effectifs et
  discordances du pilote ; McNemar exact rapporté en complément. Le gabarit ci-dessus ne sert qu'au dimensionnement.

### 3.7 Plan d'analyse

- **Primaire** : par classe confirmée, Δ̂_k et son intervalle, φ̂_L, φ̂_S et bornes, issue O1 à O4 selon le § 1.7 ; dépense par
  bras.
- **Secondaires** (rapportées toutes, sans sélection) : rappel **localisé** (bonne étape) ; rappel **conditionnel aux paires
  formalisables** (items dont la jumelle saine est acceptée par L) ; union L ∪ S moins S ; motifs des `NON-ACCEPTE` (rejet, infidélité,
  plafond, délai, sortie invalide, refus) ; stabilité sous double renotation (pilote) ; acceptations à énoncé infidèle (audit) ;
  coût total, par item (quantiles de la distribution), par détection, temps mural ; résultats par domaine D1 à D5 ; par présence
  d'un témoin numérique dans la clé ; lecture nue et relecteur seul (pilote) ; classifieur de style.
- **Sensibilité** : étiquettes adjugées à l'aveugle (§ 2.5) ; exclusion appariée des pannes techniques de l'un ou l'autre bras ;
  bornes de pire et de meilleur cas pour les items non évaluables (dénominateur sur tous les items assignés, convergence G14) ;
  convention A-T3 pour les acceptations infidèles sur les saines.
- **Graines et manifestes** (R9) : `SeedSequence` dérivées par tâche (tirage domaine × classe, ordre, sens de la paire, tirage de
  l'audit, départage des ex æquo) ; un manifeste par phase (configuration et empreinte, versions de Lean, de Mathlib et des
  bibliothèques, identifiants exacts des modèles servis, graines, commit).

### 3.8 Liste d'arrêt (écrite d'avance ; chaque garde éprouvée sur un cas sain et sur un artefact, R5)

- **A1** gardes G-L1 à G-L5, plafonds et compteurs non éprouvés ⇒ aucun lancement.
- **A2** modèle servi différent du modèle demandé (identifiant exact) ⇒ arrêt de la phase.
- **A3** refus de modèle sur plus de 10 % des appels d'un bras parmi les 20 premiers items ⇒ arrêt, rapport tel quel, aucune
  reformulation.
- **A4** témoins de fonctionnement : un bras détecte moins de 4 fautes grossières sur 5, ou alerte sur au moins 2 preuves
  trivialement saines sur 5 ⇒ défaut de harnais présumé, arrêt ; correction en version neuve, nouveau scellement.
- **A5** plus de 50 % des graines écartées au contrôle ⇒ arrêt de la construction ; consigne du planteur en version neuve.
- **A6** classifieur de style > 0,70 deux fois de suite ⇒ arrêt.
- **A7** dépense de la phase + pire cas de la paire suivante > plafond de la phase ⇒ plus aucun lancement (paires complètes).
- **A8** étalonnage : après les 10 témoins et les 10 premières paires, coût projeté du pilote > plafond ⇒ nombre de graines
  ramené à ⌊(plafond − dépense) / coût mesuré par paire⌋, **au moins 40**, sinon arrêt.
- **A9** viabilité, fin du pilote : φ̂_L > 0,60 ⇒ O0 et pas de confirmation ; φ̂_S > 0,60 ⇒ O0 « suite non viable » ; les deux
  rapportés.
- **A10** échéance de la phase (fixée au GO) dépassée ⇒ arrêt et rapport.
- **A11** toute machine louée s'arrête par son identifiant (R10) et se consigne dans `registres/arrets.md`.
