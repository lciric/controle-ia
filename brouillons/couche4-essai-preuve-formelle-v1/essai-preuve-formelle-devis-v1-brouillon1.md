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
  (φ = 1) ; c'est pourquoi l'issue favorable O1 n'existe pas sans le **plafond de fausses alertes** (§ 1.7), pourquoi O2 se lit
  avec le rappel conditionnel, et pourquoi le
  rappel **conditionnel aux paires formalisables** est la première mesure secondaire (§ 3.7).
- **Ce qui est vérifié : le squelette, pas seulement l'énoncé** (proposé par le rédacteur). Une preuve fausse d'un énoncé vrai
  (cas ordinaire des classes K1, K3, K4) serait « vérifiée » si le bras L prouvait l'énoncé par un autre chemin. Le bras L doit
  donc formaliser **chaque étape numérotée i** comme un lemme de premier niveau nommé `etape_i` (hypothèses de l'item et, au
  besoin, conclusions des étapes précédentes ; énoncé formel = celui de l'étape écrite ; prouvé par n'importe quelle tactique),
  puis l'énoncé final ; une étape fausse ne peut pas être prouvée, quel que soit le chemin pris pour l'énoncé final. Une garde
  mécanique vérifie la présence de toutes les étapes (§ 3.1) et le relecteur de fidélité vérifie leur correspondance.

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
| **O2 gain au prix d'alertes** | B(Δ_k) > 0 **et** Δ̂_k ≥ δ **et** H(φ_L) > φ_max | La chaîne formelle trouve plus sur k, mais rejette trop de preuves saines pour servir de vérificateur à ce point de fonctionnement ; le coût des fausses alertes est rapporté. **Lecture obligatoire avec le rappel conditionnel aux paires formalisables** : si l'écart conditionnel est nul ou négatif, l'écart vient des échecs de formalisation, non d'une détection, et le rapport le dit en tête. |
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
| (c) lemmes du programme (carte des hypothèses v1, `f7dfe5fd…` : lemme maître L0 et 21 lemmes ; programme d'entretien v16, l. 386 et 807 : « Vérification formelle (Lean) du lemme maître L0 et des 21 lemmes », ouverte par conv-audit, état « à ouvrir » au 28 octobre) | c'est l'usage visé ; erreurs éventuellement réelles | 22 items seulement ; justesse non établie, donc **pas d'étiquette** ; ne peut pas servir à la confirmation |

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
- **Tâche** : écrire l'énoncé formel `enonce_item`, un lemme de premier niveau `etape_i` par étape numérotée (énoncé = celui de
  l'étape écrite), puis la preuve de `enonce_item` ; prouver chaque `etape_i` par toute tactique ; rendre une sortie structurée
  (`ACCEPTE` ou rejet, étape, raison, fichier Lean).
- **Gardes mécaniques du harnais** (le verdict `ACCEPTE` exige toutes) : G-L1 compilation sans erreur ; G-L2 aucun `sorry` ni
  `admit`, et `#print axioms` de `enonce_item` **et de chaque** `etape_i` ne liste que `propext`, `Classical.choice`,
  `Quot.sound` ; G-L3 aucun `axiom`, `unsafe`, `@[implemented_by]`, `@[extern]` dans le fichier ; G-L4 présence des lemmes
  `etape_1` à `etape_m` (m = nombre d'étapes de l'item) et de `enonce_item` ; G-L5 les énoncés **imprimés par Lean** (`#check`
  de `enonce_item` et de chaque `etape_i`) sont ce que reçoit le relecteur de fidélité.
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
- **Probabilités des issues** (20 000 tirages par case, intervalle gabarit de Wald ajusté « +0,5 par case » ; « gain » = condition
  de rappel commune à O1 et O2, sans la condition des fausses alertes ; « sous le seuil » = O3 ; « non concluante » = O4) ; à n = 100 et
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
- **A8** étalonnage : la banque du pilote est construite d'abord ; après les 10 témoins et les 10 premières graines (20 items,
  chacun vu par les deux bras), coût projeté du pilote > plafond ⇒ nombre de graines restantes ramené à ⌊(plafond − dépense) /
  coût mesuré par graine⌋ (une graine = deux items vus par les deux bras), **au moins 40 graines au total**, sinon arrêt.
  L'ordre d'exécution suit des **blocs équilibrés** (chaque bloc de 5 graines couvre les 5 classes) pour qu'une coupure (A7, A8)
  garde l'équilibre des classes.
- **A9** viabilité, fin du pilote : φ̂_L > 0,60 ⇒ O0 et pas de confirmation ; φ̂_S > 0,60 ⇒ O0 « suite non viable » ; les deux
  rapportés.
- **A10** échéance de la phase (fixée au GO) dépassée ⇒ arrêt et rapport.
- **A11** toute machine louée s'arrête par son identifiant (R10) et se consigne dans `registres/arrets.md`.

---

## 4. Devis (aucune dépense avant le GO de Lazar)

Tous les montants sont en USD, calculés par `calculs_devis_essai_v3.py` (sortie `sortie-calculs-devis-v3.txt`) et
`variantes_modele_bras_v1.py` (sortie `sortie-variantes-modele-bras-v1.txt`), scellés dans le bac à sable du rédacteur (table
des empreintes). Les profils de consommation par appel sont **SUPPOSÉS** ; le pilote les mesure et le devis 2 les remplace.

### 4.1 Prix par million de jetons (entrée / sortie)

| Modèle (rôle) | Entrée | Sortie | Source | Statut |
|---|---|---|---|---|
| Opus 5.5 (agents des bras, lecture nue) | 4 | 20 | référence locale `claude-api` : table « Current Models (cached: 2026-11-03) » et `shared/models.md` l. 83 (`74245a8d…`) | **à vérifier** sur la page publique des tarifs avant GO |
| Sonnet 5.5 (variante) | 2 | 10 | même référence, `shared/models.md` l. 89 | à vérifier |
| Fable 5.2 (variante) | 8 | 40 | même référence, `shared/models.md` l. 78 | à vérifier |
| Kimi K3.1 Pro (relecteurs internes aux bras) | 2 | 10 | `collisionneur_v8.py` l. 76–77 : « Prix vérifiés le 30 octobre » | vérifiés le 30 octobre (RAPPORTÉ) |
| GPT-6 Astra (planteur) | 10 | 50 | `collisionneur_v8.py` l. 79–82 : « Prix SUPPOSÉS … barème volontairement haut » | **à vérifier** (identifiant aussi) |
| Gemini 4 Argon (contrôle, audit, adjudication) | 10 | 50 | `collisionneur_v8.py` l. 73–74 : « valeur volontairement haute » | **à vérifier** |

Cache : le calcul prend une lecture à 0,1 fois le prix d'entrée et une écriture à 1,25 fois (référence locale, ordre de grandeur
général) ; pour Opus 5.5, `shared/models.md` l. 83 donne 0,20 USD par million en lecture, soit 0,05 fois : l'attendu est donc
prudent sur ce point (à vérifier) ; **les pires cas ne comptent aucun cache**. Le raisonnement des modèles est facturé comme sortie et compté comme tel.

### 4.2 Coûts unitaires (attendu SUPPOSÉ ; pire cas)

| Élément | Modèle | Profil supposé (entrée cumulée, sortie cumulée, part en cache) | Attendu | Pire cas |
|---|---|---|---|---|
| agent du bras L, par item | Opus 5.5 | ≈ 20 tours ; 500 k ; 30 k ; 85 % lus et 10 % écrits en cache | 1,12 | — |
| relecteur de fidélité (L), par item | Kimi K3.1 Pro | un appel ; 6 k ; 3 k | 0,042 | — |
| **item du bras L** | | | **1,162** | **4,00** (plafond par item) |
| agent du bras S, par item | Opus 5.5 | ≈ 6 tours ; 100 k ; 10 k ; 80 % et 10 % | 0,322 | — |
| relecteur indépendant (S), par item | Kimi K3.1 Pro | un appel ; 6 k ; 4 k | 0,052 | — |
| **item du bras S** | | | **0,374** | **4,00** (même plafond) |
| lecture nue, par item (pilote) | Opus 5.5 | un appel ; 5 k ; 8 k | 0,18 | 0,66 (32 k de sortie) |
| planteur, par graine (graine, saine renotée, fautive, clé) | GPT-6 Astra | 5 k ; 10 k | 0,55 | 1,68 (8 k ; 32 k) |
| contrôle de la graine saine, par graine | Gemini 4 Argon | 6 k ; 4 k | 0,26 | 0,88 (8 k ; 16 k) |
| audit de fidélité, par item tiré | Gemini 4 Argon | 4 k ; 3 k | 0,19 | 0,46 (6 k ; 8 k) |

Rapport attendu des coûts par item L/S : **3,11** (prédiction P4 : entre 2 et 6).

### 4.3 Devis par phase et par élément

**Phase 0 — outillage** (aucun appel facturé au jeton) : harnais des deux bras (boucle d'outils, compteurs de jetons par appel,
plafonds par item et par phase, sortie structurée, gardes G-L1 à G-L5, clé scellée, ordre par paires), installation de Lean 4 et
de Mathlib épinglés, essais R5 des gardes sur cas sains et artefacts, simulations de couverture et d'erreur de famille (§ 3.6),
classifieur de style, scripts d'analyse scellés. Écrit et contre-lu par des sous-agents de la session (coût d'abonnement, **hors
devis d'interface, à confirmer par la mère**). Machine : **0 à 50 USD** selon D-2 (à vérifier). Durée : 2 à 3 jours.

**Phase 1 — pilote** (60 graines, 12 par classe ; 60 saines, 60 fautives, 10 témoins, 10 saines renotées bis : 140 items ; audit
sur 50 %) :

| Élément | Attendu | Pire cas (chaque item à son plafond) |
|---|---|---|
| planteur (72 graines, surgénération 20 %) | 39,60 | 120,96 |
| contrôle des graines | 18,72 | 63,36 |
| bras L | 162,68 | 560,00 |
| bras S | 52,36 | 560,00 |
| lecture nue | 25,20 | 92,40 |
| audit de fidélité | 13,30 | 32,20 |
| **total** | **311,86** | 1 428,92 |

**Plafond proposé de la phase 1 : 450 USD** d'appels (coupures A7 et A8 : la dépense ne peut pas le dépasser ; le pire cas
théorique sert seulement à dire que la coupure est nécessaire) ; plus la machine (≤ 50 USD).

**Phase 2 — confirmation** (deux classes ; une saine et une fautive par graine ; audit sur 30 % ; effectifs par la règle du
§ 3.6, **sur second GO** avec devis 2 refait sur les coûts mesurés) :

| Élément | Central : 2 × 96 graines, 384 items | Plafond d'effectif : 2 × 150 graines, 600 items |
|---|---|---|
| planteur | 127,05 (pire 388,08) | 198,00 (pire 604,80) |
| contrôle des graines | 60,06 (pire 203,28) | 93,60 (pire 316,80) |
| bras L | 446,21 (pire 1 536,00) | 697,20 (pire 2 400,00) |
| bras S | 143,62 (pire 1 536,00) | 224,40 (pire 2 400,00) |
| audit de fidélité | 22,04 (pire 53,36) | 34,20 (pire 82,80) |
| **total** | **798,97** (pire 3 716,72) | **1 247,40** (pire 5 804,40) |

**Plafond proposé de la phase 2 : 1 400 USD**, révisé par le devis 2. La règle d'effectif (borne haute à 80 % de la discordance)
pousse vers le plafond d'effectif si les discordances du pilote sont de l'ordre de 0,3 : le chiffre central est un repère, non une
promesse.

**Engagement maximal des deux phases** (plafonds) : 450 + 1 400 + 50 (machine) = **1 900 USD** ; attendu ≈ 1 110 à 1 560 USD
plus la machine.

**Options chiffrées** (pour les décisions du § 7) : une seule classe fixée maintenant, 150 graines (D-5 (ii)) : attendu 623,70 au
lieu de la phase 2 ; cinq classes confirmées à 150 (D-5 (iii)) : attendu 3 118,50 ; banque d'usage, 22 lemmes du programme
(D-6) : attendu 35,88, pire cas 181,06, plafond proposé 60. Modèle des bras (D-3) : pilote Sonnet 5.5 198,32 / Fable 5.2 538,94 ;
confirmation centrale Sonnet 5.5 522,11 / Fable 5.2 1 352,70 ; plafond d'effectif Sonnet 5.5 814,80 / Fable 5.2 2 112,60.

### 4.4 Durées (SUPPOSÉES : 15 minutes de processus par item pour L, 3 pour S, 1 pour la lecture nue)

- Pilote : bras L 35 heures de processus, **≈ 12 heures murales** à 3 processus Lean en parallèle (mémoire) ; bras S et lecture
  nue ≈ 9 heures de processus, ≈ 2,3 heures murales à 4.
- Confirmation : bras L 96 (central) à 150 (plafond) heures de processus, **≈ 32 à 50 heures murales** ; bras S ≈ 5 à 8 heures
  murales.
- Calendrier : phase 0, 2 à 3 jours ; contre-lecture et scellement, 1 jour ; pilote, 2 jours (construction, exécution) ; fiche
  de passage, devis 2 et GO, 1 à 2 jours ; confirmation, 3 à 4 jours ; analyse et verdict (R13), 1 à 2 jours. **≈ 2 à 3
  semaines**, hors du chemin de G0.

### 4.5 Outillage, machine, réseau, mode d'appel

- **Constat sans réseau** (13:01:14 UTC) : `lean`, `lake`, `elan` absents ; aucun autre assistant de preuve ni solveur (`coqc`,
  `isabelle`, `agda`, `z3`, `cvc5`, `vampire`, `eprover`, `sage`, `maxima`, `gp`) ; pas de `~/.elan`, pas de cache de Mathlib.
  Présents dans `.venv` : Python 3.13.16, sympy 1.14.0, mpmath 1.3.0, numpy 2.4.6, scipy 1.17.1, networkx 3.6.1. Machine : 4
  cœurs, 15 Go de mémoire, **2,7 Go de disque libre** (94 %).
- **Lean et Mathlib** : chaîne installée par `elan`, Mathlib épinglée sur un commit fixé au préenregistrement, avec son cache
  précompilé ; **taille sur disque, mémoire par processus, hôtes de téléchargement : à vérifier** au moment de l'installation
  (aucune valeur avancée ici). L'installation ne coûte rien en argent (décision de principe du 27 octobre, programme complet v2,
  § 2.5) mais exige du disque et l'ouverture des hôtes (nœud d'environnement, D-2).
- **Mode d'appel** : (M1) appels d'interface au jeton par un harnais (recommandé : seul mode où le **coût apparié** se mesure par
  item, où l'identifiant exact du modèle servi est vérifié et où un manifeste par phase est possible, R9) ; (M2) sous-agents de la
  session : pas de comptage par item, modèle non épinglé — incompatible avec la métrique de coût. Comptes : clés existantes du
  programme (Anthropic ; Kimi par le relais local ; OpenAI ; Gemini), aucun compte neuf prévu ; si l'accès à GPT-6 Astra ou à
  Argon manque, c'est un nœud de compte.
- **Garde de calcul** : toute machine louée cite un GO valide de `registres/go.md` (`.claude/hooks/garde_calcul.py`) et s'arrête
  par identifiant (R10).

### 4.6 Hors devis

Temps des sous-agents de la session (développeur du harnais, contre-lecteur R2, lecteur du pilote, verdict R13) ; temps de Lazar ;
aucune carte graphique.

---

## 5. Ce que l'essai décide et ce qu'il ne décide pas

**Il mesure** (mesure, non décision de programme), pour au plus deux classes, sur cette banque plantée, avec ce modèle, cette
version de Lean et de Mathlib et ce plafond par item : l'issue O0 à O4 ; les fausses alertes des deux chaînes ; le rapport de
coût et le coût par détection ; la part des preuves saines que la chaîne formelle sait vérifier, par domaine ; la part des
acceptations formelles à énoncé infidèle.

**Il ne décide pas** :
- **l'ouverture de la couche 4**, fermée jusqu'aux résultats de l'étape 2 (N12 (b), R-959) : un O1 est une **pièce** au dossier de
  cette décision, qui appartient à Lazar (nœud ; les espèces ne nomment pas qui décide, sauf E en général, synthèse du tour 2,
  § E.1) ; aucune issue n'est une règle d'ouverture ;
- **la suite d'un échec** : ni « couche 4 fermée, vérificateur externe suffisant » (A), ni « suite bon marché comme standard
  obligatoire du programme » (C, modification du programme) ne découlent d'un O3 ;
- **l'intégration dans l'organisme** : l'essai est hors organisme (vérificateur externe, synthèse du tour 2, § E.4) ; aucun
  score de l'essai n'entre dans un entraînement ni dans une sélection d'agents (N-053 non concerné : pas d'entraînement) ;
- **la distribution réelle des erreurs** du programme (banque plantée, aucune prétention de représentativité, position E) ;
- **les erreurs de spécification empirique** : une preuve ne valide pas une spécification empirique (D ; MAT-004) ;
- **les classes non testées, d'autres modèles, d'autres versions de Mathlib**, ni la capacité intrinsèque de Lean (seulement
  approchée par l'analyse conditionnelle aux paires formalisables) ;
- **la génération** de mathématiques nouvelles (§ 6).

---

## 6. Lien vers le pas (c) : ce que l'essai apprendra pour un pilier de génération

Les espèces n'en ont rien dit (synthèse du tour 2, § E.3) ; ce qui suit est **proposé par le rédacteur, non tranché**, et ne
préjuge pas de la note (c).
1. **Fidélité de formalisation par domaine.** Le taux de saines que la chaîne formelle accepte avec un énoncé fidèle, de D1 à D5,
   est la **carte de couverture** de Mathlib sur les domaines du programme. Si la chaîne ne sait pas vérifier des preuves courtes
   **connues** de ces domaines, « Lean comme arbitre » de conjectures **nouvelles** y est prématuré ; l'issue O0 répondrait déjà à
   cette question.
2. **Acceptation vide, sans pression d'optimisation.** L'audit mesure la part d'acceptations dont l'énoncé formel n'est pas celui
   du texte. Dans l'essai, personne n'optimise contre Lean ; un **générateur** qui le ferait subirait une pression de type Goodhart
   (énoncés triviaux, hypothèses contradictoires, énoncé voisin), celle que le programme étudie pour les juges (N-064, N-065).
   L'essai donne le **taux de base** ; la classe K5 et l'audit de fidélité sont les premiers instruments d'une garde
   « anti-vacuité » du pilier.
3. **Coût par preuve vérifiée et temps mural** : base du budget d'une boucle « génération puis vérification ».
4. **Partage du travail** : les classes que la suite manque disent où un générateur devrait passer par Lean, et celles où des
   contrôles bon marché suffisent.
5. **Artefacts réutilisables** : environnement Lean épinglé, gardes mécaniques éprouvées (R5), harnais à comptage par item,
   protocole d'audit de fidélité, et une petite bibliothèque d'énoncés **sains formalisés** dans les domaines du programme (graines
   possibles d'un générateur) ; la banque d'usage (D-6) toucherait en outre la piste « Vérification formelle (Lean) du lemme maître
   L0 et des 21 lemmes » du front théorie.
6. **Ce qu'il n'apprendra pas** : si un modèle produit des énoncés vrais et nouveaux ; comment juger la **nouveauté** ou la
   valeur d'une conjecture (aucun matériau ici pour un juge de nouveauté) ; l'effet d'une pression d'optimisation (absente de
   l'essai).

---

## 7. Décisions à poser à Lazar

**D-1 — GO de dépense de la phase 1 (outillage et pilote).** Enjeu : seul pas autorisé par N12 (b) ; sans lui, (b) s'arrête au
devis. Options : (i) GO, plafond **450 USD** d'appels plus **≤ 50 USD** de machine, échéance à fixer (avantage : pilote complet,
viabilité et discordances mesurées ; inconvénient : ≈ 312 USD attendus) ; (ii) GO réduit à 40 graines, 100 items, attendu ≈ 220 USD
(`option_pilote_reduit_v1.py`), plafond 320 USD (moins cher ; discordances par classe sur 8 items, choix des classes plus
fragile) ; (iii) pas de GO maintenant (aucune dépense ; le pas
(c) part sans mesure). Recommandation : **(i)**, confiance 0,6. Défaut : **aucune dépense** (nœud : pas de défaut de dépense).

**D-2 — Machine et réseau pour Lean.** Enjeu : 2,7 Go libres ici ; Mathlib n'y tient pas. Options : (i) machine processeur
dédiée, louée sur devis (isolée du dépôt de travail, arrêt par identifiant ; coût à vérifier, ≤ 50 USD) ; (ii) libérer de la
place sur le conteneur courant et y ouvrir les hôtes de la chaîne Lean (pas de location ; risque d'interférence avec les autres
chantiers, nettoyage à décider par la mère) ; (iii) attendre. Recommandation : **(i)**, confiance 0,55. Défaut : aucune
(nœud d'environnement et de dépense).

**D-3 — Qui formalise ; modèles et familles.** Enjeu : divergence des espèces (C : autre famille ; E : opérateurs) ; détermine ce
que l'écart mesure. Options : (a) **même modèle (Opus 5.5) dans les deux bras, seuls les outils diffèrent** ; relecteurs Kimi
K3.1 Pro dans les deux bras ; planteur GPT-6 Astra ; contrôle et audit Gemini 4 Argon (avantage : l'écart mesure l'outil ;
inconvénient : pas « le meilleur formaliseur ») ; (b) formaliseur d'une autre famille que la suite (avantage : proche d'un usage ;
inconvénient : modèle et outil confondus) ; (c) opérateurs humains (avantage : fidélité ; inconvénient : contact externe,
dépense, délais). Variante de modèle des bras : Sonnet 5.5 (≈ −36 % au pilote, chaîne formelle sans doute moins viable) ou
Fable 5.2 (≈ +73 %). Recommandation : **(a) avec Opus 5.5**, confiance 0,6. Défaut sous 48 heures : (a).

**D-4 — Seuils.** Enjeu : fixent l'issue ; à geler avant scellement (D-T1 demandait que le directeur les gèle). Options :
(i) **δ = 0,20, φ_max = 0,30** (effectifs du § 3.6) ; (ii) δ = 0,15 (plus fin ; effectif multiplié par (0,10 / 0,075)² ≈ 1,8 à
discordance égale, donc phase 2 plus chère) ; (iii) δ = 0,25 (moins cher ; ne voit que de gros gains). Recommandation : **(i)**, confiance 0,5. Défaut sous 48
heures : (i).

**D-5 — Une ou plusieurs classes.** Enjeu : divergence des espèces (A : une classe préenregistrée ; B, C, E : plusieurs avec
correction). Options : (i) **pilote sur les cinq classes, deux classes retenues par la règle écrite (la plus favorable à Lean,
quel que soit le signe), séquence fixe** (phase 2 attendue 800 à 1 250) ; (ii) une classe fixée maintenant, K1 « coquille de
relation » (type des coquilles déjà trouvées) (attendu 624 ; aucune sélection ; peut tester la classe la moins favorable) ;
(iii) cinq classes confirmées avec correction de Holm (attendu ≈ 3 120). Recommandation : **(i)**, confiance 0,6. Défaut sous
48 heures : (i).

**D-6 — Banque d'usage (L0 et 21 lemmes de la carte des hypothèses v1).** Enjeu : seul contact de l'essai avec les preuves
réelles du programme. Options : (i) bras descriptif après le pilote, sans revendication, plafond 60 USD (attendu ≈ 36) ;
(ii) non. Recommandation : **(i)**, confiance 0,55. Défaut : **non** (dépense).

---

## 8. Points ouverts et à vérifier avant scellement

1. Prix d'Opus 5.5, de Sonnet 5.5 et de Fable 5.2 sur la page publique ; prix et identifiants d'interface de GPT-6 Astra et de
   Gemini 4 Argon ; accès effectifs (comptes).
2. Taille de Mathlib et de son cache, mémoire par processus Lean, hôtes de téléchargement ; commit de Mathlib à épingler.
3. Les profils de consommation (§ 4.2) et la durée par item (§ 4.4) sont des suppositions ; le pilote les mesure, le devis 2 les
   remplace.
4. Méthode d'intervalle apparié (Tango ou Newcombe) et contrôle de l'erreur de famille de la séquence fixe : à fixer par
   simulation avant scellement ; références des méthodes nommées (McNemar, Clopper–Pearson, Wald ajusté, Tango, Newcombe, Holm) :
   RAPPORTÉES, à vérifier ; aucun chiffre de l'état de l'art n'est utilisé (R7).
5. Le coût des sous-agents de la session est-il une dépense au sens du programme ? (à confirmer par la mère).
6. La carte des hypothèses v1 (`f7dfe5fd…`) n'est pas dans les fichiers suivis de `main` ; son dossier est touché par les commits
   `444bfff13` et `9778cd6f3` (branche du canal) ; non ouverte ; sa contre-lecture (même branche, commit `9778cd6f3`) annonce
   des corrections à porter en v2 : la banque d'usage devrait partir de la version corrigée.
7. Consigne du planteur et tronc de consigne des bras : à écrire au préenregistrement (versions neuves, scellées), avec des
   exemples génériques de chaque classe qui ne viennent pas des banques.
8. Contre-lecture (R2) : vérifier en particulier que le dessin ne favorise pas Opus 5.5 (conflit déclaré), que la règle du « ou »
   des deux bras est symétrique, et que la définition d'un item fautif (§ 2.2) n'exclut pas des classes où Lean serait favorisé.
9. L'adjudicateur des cas litigieux (§ 2.5) est de la famille qui a contrôlé les graines saines (Gemini 4 Argon) : il pourrait
   tendre à confirmer les étiquettes qu'il a déjà validées. L'effet ne touche que l'analyse de sensibilité et reste aveugle au
   bras qui a alerté ; une autre voie (adjudication humaine sur un tirage, ou un autre modèle) est à trancher à la contre-lecture.

---

## Table des empreintes (SHA-256, calculées par script à l'assemblage ; aucune valeur retapée)

| Fichier | Rôle, ce qui en a été lu | SHA-256 | Compagnon |
|---|---|---|---|
| `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-devis-essai-preuve-formelle-couche4-v1.md` | consigne ; lue en entier | `5403571b05f6733a69ec8e26cbd6ecc53d2d8243fe1c77288ee058c77d45cfba` | égale au compagnon |
| `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` | interdits communs v2 ; empreinte vérifiée, texte lu tel que recopié dans la consigne | `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` | égale au compagnon |
| `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-tour2-v1.md` | synthèse du tour 2 ; lue en entier | `6ef6bc2e1cbea69b0b47f20508fa09391e7c2271785287c470dc632de5a2b1ce` | égale au compagnon |
| `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-v2.md` | synthèse v2 ; lue en entier | `f0340581766c5fb4d97a0ccb06f0cf1738a15228385b332ee602e93a0be28f0a` | égale au compagnon |
| `docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v2.md` | programme complet v2 ; l. 1–61, 142–264, 1319–1331 et lignes trouvées par « lean » | `dffe0b632bfa24ffa5af3e460110515e05dfc74283d856a15eba01afab168556` | égale au compagnon |
| `docs/notes/ideation-organisme-v1/course-2/collisionneur-v8/collisionneur_v8.py` | table des prix, l. 60–95 | `22e5ed8a64075f2f985755d9bff2c2336d8edc5f73cbc3b0511405fd8f43d264` | égale au compagnon |
| `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` | l. 384–388, 436–440, 800–810 (carte des hypothèses v1, piste Lean) | `186173d9d9b949bfb3922503adff1be9d60f49f07fb975750de4c88bd60a060e` | égale au compagnon |
| `registres/decisions.md` | registre vivant : R-920, R-946, R-957, R-959, R-2199 ; R-2200 à R-2226 filtrées par mots | `cbd3f950ce7dac81f5576ca9cfdacefdcf346843730bf3e0f7b98e3118032580` | pas de compagnon (registre vivant) |
| `/tmp/claude-0/bundled-skills/2.1.322/3f5d19faa48e8729fa23bef895bf9c5b/claude-api/shared/models.md` | référence locale `claude-api` (prix des modèles Claude), l. 78, 80, 83, 89 | `74245a8d11939d988321c47ab4b4775ac1fa287f97ed94f7b65eb6145bcbe7b9` | pas de compagnon |
| `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/calculs_devis_essai_v1.py` | calculs v1 (bac à sable) | `6f374d0c651e1ce127ab99841ce4f51efcb13433407a0af19f82fcede953f9f3` | égale au compagnon |
| `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/sortie-calculs-devis-v1.txt` | sortie v1 | `7fb79ee398095b08000032433dc66f9e89564b0d69734469f547098054bc364f` | égale au compagnon |
| `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/calculs_devis_essai_v2.py` | calculs v2 : contrôle des graines par Gemini 4 Argon | `d57e176b24258d2c1f650f111e7a136b5b9bf08b8a761b01fe9b86cf6dfb278c` | égale au compagnon |
| `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/sortie-calculs-devis-v2.txt` | sortie v2 | `d6492d79c636996105c4bfa89376651b92a7afbb653a72cee885a5a78cab6f7d` | égale au compagnon |
| `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/calculs_devis_essai_v3.py` | calculs v3 : pilote à 140 items, options, durées (chiffres du § 3.6 et du § 4) | `236371fdcdc754b997286ca3add3cf1c05c67ff29f65161df03350af694472c7` | égale au compagnon |
| `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/sortie-calculs-devis-v3.txt` | sortie v3 | `18221e7b6b676cdaa88bf8e095202da3a2ac475876aeb61ecf78c4fe7ad1d7f3` | égale au compagnon |
| `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/variantes_modele_bras_v1.py` | variantes du modèle des bras (D-3) | `25ff8f46ca92afadb23127984c77d923a9eac86fd2247efdfff841da034e980d` | égale au compagnon |
| `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/sortie-variantes-modele-bras-v1.txt` | sortie des variantes | `3651c56cc976cd119b280afbdfb7e42d58650bddf16afe47510af3e81367cbf0` | égale au compagnon |
| `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/option_pilote_reduit_v1.py` | option D-1 (ii) | `cb8a5dc230d04229ff1ad797e8094db505886060086ed5718ad455503b603e63` | égale au compagnon |
| `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/sortie-option-pilote-reduit-v1.txt` | sortie de l'option D-1 (ii) | `6a4d0ae69b72f610d93d1d94e493978884bfef99cd8de2afdd250c9481a3452d` | égale au compagnon |
| `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/jalon1-journal-v1.md` | jalon 1 du journal | `966949d52d51de7164c4bc78848130c3744e0530cf5cda4e402328958fb92c90` | égale au compagnon |
| `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/jalon2-brouillon-sections-0-3-v1.md` | jalon 2 : sections 0 à 3 du brouillon | `4b98b352028c0a78592e1c63d1452807185dd610590c178fa2b8ff78201c4e8a` | égale au compagnon |

Table assemblée par script le Tue Nov 10 13:20:12 UTC 2026 (horloge du système, UTC). L'empreinte du présent brouillon est celle de son compagnon `.sha256`. Le chemin du bac à sable est `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/` ; ses fichiers ne sont pas versés au dépôt (consigne : rien hors des chemins de sortie nommés).
