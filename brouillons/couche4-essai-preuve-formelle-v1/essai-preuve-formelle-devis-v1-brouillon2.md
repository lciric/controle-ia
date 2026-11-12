# Essai « preuve formelle contre suite bon marché » (couche 4, pas (b) de R-2199) — dessin et devis — v1, brouillon 2

- **Pour** : la session mère, puis Lazar. **Écrit par** : un sous-agent neuf (rédacteur), modèle **Opus 5.5** (`claude-opus-5-5`),
  session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, le 10 novembre 2026 (brouillon 1 commencé à 13:00:30 UTC, brouillon 2 à 13:30:55 UTC ; heures relevées par `date -u`).
  Je n'ai écrit ni les questions, ni les critères, ni les synthèses N12-N13. **Conflits déclarés** : je suis de la famille des
  espèces A et B du collisionneur et du même modèle que le lecteur du tour 2 ; je recommande plus bas Opus 5.5 comme modèle des
  deux bras de l'essai (§ 2.7) : la contre-lecture 1 n'a trouvé aucun élément qui favorise ce modèle ; le biais qu'elle relève penchait vers le **bras formel** (CLP-01, CLP-02), corrigé ici.
- **Statut** : **brouillon 2, contre-lu une fois, non préenregistré**. La contre-lecture 1 (`prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon1-cl1.md`, `f565d51c…`, Claude Fable 5.2, « scellable après corrections », sept bloquants) est appliquée : 14 couples par programme (`calculs-v2/appliquer_couples_cl1_v1.py`), trois ajouts sans couple (CLP-07, CLP-10, CLP-12), devis refait par script (`calculs-v2/calculs_devis_essai_v4.py`), décisions de la mère (§ 0). Le contre-lecteur est **Fable 5.2**, non le Fable 5.1 que nommaient N-052 et le brouillon 1 : écart signalé à la mère. Le texte devient un préenregistrement (R1) quand les pièces marquées « À REMPLIR » (§ 9) existent, après vérification par un sous-agent neuf, et le GO de D-1b ne se prend qu'ensuite. **Aucun appel de modèle, aucun réseau, aucune dépense** n'ont servi à l'écrire ; tous les chiffres de coût sont
  calculés par script (§ 4, table des empreintes) à partir de prix cités avec leur source ou marqués « à vérifier ».
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-devis-essai-preuve-formelle-couche4-v1.md`
  (`5403571b…`). Journal : `essai-preuve-formelle-devis-v1-journal-v2.md` (même dossier). Le brouillon 1 (`9ccc9ac0…`) et son journal (`f8c2b8c6…`) restent intacts.

## Verdict

1. **L'essai est faisable sur processeur, en trois pas payés séparément** (scission demandée par la contre-lecture 1, CLP-07).
   **D-1a — outillage** : machine dédiée et isolée, Lean et Mathlib à un commit fixé, gardes éprouvées, simulations ; **aucun appel
   de modèle** ; machine seule, ≈ 48 heures allumées, 4,80 à 19,20 USD à 0,10–0,40 USD l'heure (prix à vérifier), borne haute
   62,40 ; plafond proposé **65 USD**. **D-1b — pilote** (140 items), **seulement après le préenregistrement complet, contre-lu et
   scellé** : attendu **≈ 337 à 347 USD** au profil supposé, **≈ 448 à 457** avec toutes les lignes conditionnelles, **≈ 606 à 726**
   au profil « pire réaliste » de l'agent formel (CLP-09) ; plafond proposé **550 USD** (au profil pire réaliste, la coupure A8 garde
   48 graines sur 60 ; sous 450 elle arrêterait le pilote) et **35 USD** de machine. **Phase 2 — confirmation** (deux classes lues
   à 97,5 %, sans porte) : la règle d'effectif atteint le plafond de 2 × 150 graines dès 15 discordantes sur 60 au pilote ; attendu
   **≈ 1 299 USD** au profil supposé (1 346 avec 60 % d'items litigieux, **1 865** avec les lignes conditionnelles), **≈ 2 451 à
   3 017** au profil pire réaliste ; plafond **indicatif 1 900 USD**, fixé par le devis 2 sur les coûts mesurés au pilote, second GO.
2. **Trois obstacles avant toute dépense** : aucun vérificateur installé (ni Lean, ni Mathlib) ; 2,7 Go libres ; et d'abord la
   **cloison** : les deux outils exécutent du code écrit par un modèle, d'où une machine dédiée **sans clé ni dépôt du programme**
   (§ 4.5, CLP-04). La dépense est faite d'**appels d'interface chez quatre fournisseurs et d'une machine louée**, non de
   sous-agents : Lazar l'accorde en le sachant (CLP-05, D-1b).
3. **L'essai ne rouvre pas la couche 4** : il produit une pièce pour la décision que Lazar prendra après les résultats de l'étape 2
   (N12 (b)). O1 n'établit qu'un gain positif (O1b), sauf si la borne basse dépasse δ (O1a). Ma prédiction (prior, § 1.4) reste que
   la chaîne formelle ne franchit pas le critère conjoint ; avec un écart de fausses alertes de +0,15 ou plus, O1 est presque hors
   d'atteinte : φ_max décide autant que δ.

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
  issues d'une même graine (§ 2.3) ; le contrôle des graines par une famille hors des bras (§ 2.5) ; l'analyse conditionnelle aux paires formalisables (§ 3.7) ; le lien au pas (c) (§ 6).
- **Brouillon 2 — ce qui change** (contre-lecture 1 et décisions de la mère, aucune n'engageant de dépense) : O1 scindé en O1a et O1b, lu avec le rappel conditionnel et l'écart « rappel moins fausses alertes » (C01, C02) ; classes choisies sur cet écart (C03) ; deux classes lues à 97,5 % sans porte, effectifs et devis refaits par script (C04, `calculs-v2/`) ; environnement isolé des outils (C05, § 4.5) ; nature de la dépense, scission D-1a / D-1b, repli si GPT-6 Astra manque (C06, § 2.7, § 7) ; coupure A7 étendue et chiffrée (C07) ; lignes absentes du devis chiffrées (C08, § 4.3) ; méthode d'intervalle fixée avant toute donnée (C09) ; effectif des saines et lecture de A9 (C10, C11) ; profil « pire réaliste » de l'agent formel et effet sur A8 (C12) ; contrôle de l'adjudicateur (C13) ; lacunes de justification hors de portée (C14) ; prix précisés (CLP-10) ; gardes du bras formel complétées (CLP-12) ; motifs de `NON-ACCEPTE` en tête du rapport (CLP-13) ; pièces à remplir nommées (§ 9) ; D-6 non pour l'instant.

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
  (φ = 1) ; c'est pourquoi l'issue favorable O1 n'existe pas sans le **plafond de fausses alertes** (§ 1.7), pourquoi O1 et O2 se lisent avec le rappel conditionnel et la différence des écarts « rappel moins fausses alertes » (C01), pourquoi les classes se choisissent sur cette différence (C03), et pourquoi le
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

- **Primaires** : r_L,k, r_S,k et Δ_k par classe confirmée ; φ_L, φ_S et φ_L − φ_S ; dépense totale par bras et rapport des totaux L/S (jetons comptés à chaque appel par le harnais, prix du § 4.1) ; **en tête du rapport**, avant les issues : décomposition des `NON-ACCEPTE` par motif et part des items au plafond, par bras (CLP-13, C12), et différence appariée des écarts « rappel moins fausses alertes » par classe (C01, C03).
- **Secondaires** : liste au § 3.7.

### 1.6 Seuils proposés (à geler par Lazar avant scellement ; § 7, D-4)

- **δ = 0,20** (gain absolu de rappel sur une classe). Raison : la chaîne formelle coûte trois à huit fois la suite par item selon le profil (§ 4.2) et exige une infrastructure (machine, Mathlib épinglée, gardes) ; un gain plus petit sur une classe ne paierait pas un
  vérificateur externe. Valeur de jugement, non dérivée d'une mesure.
- **φ_max = 0,30** : borne haute (Clopper–Pearson à 97,5 %) des fausses alertes de la chaîne formelle. Raison : au-delà, plus
  d'une preuve saine sur trois renvoyée à une relecture humaine.
- **Intervalles** : à **97,5 %** bilatéraux pour Δ_k de chacune des deux classes (Bonferroni sur deux classes, sans porte, C04) ; méthode fixée **avant le pilote** par simulation de couverture (C09, § 3.6) ; borne des fausses alertes de Clopper–Pearson à 97,5 %.

### 1.7 Issues écrites d'avance (aucune n'est visée)

Par classe k confirmée (B(·) borne basse, H(·) borne haute des intervalles) :

| Issue | Condition | Lecture écrite d'avance |
|---|---|---|
| **O1 gain établi** | B(Δ_k) > 0 **et** Δ̂_k ≥ δ **et** H(φ_L) ≤ φ_max | Sur cette banque plantée, à ce budget, avec ce modèle et cette version de Mathlib, la chaîne formelle détecte sur la classe k strictement plus que la suite (borne basse au-dessus de zéro), avec une estimation ponctuelle d'au moins δ, à fausses alertes bornées. « Au moins δ » n'est dit établi que si B(Δ_k) ≥ δ (sous-cas O1a) ; sinon l'issue se lit « gain positif établi, ampleur non établie » (sous-cas O1b). **Lecture obligatoire, comme pour O2, avec le rappel conditionnel aux paires formalisables et avec la différence appariée des écarts « rappel moins fausses alertes »** : si l'une des deux est nulle ou négative, le rapport le dit en tête. **Pièce** versée au dossier de la décision de Lazar après l'étape 2 ; n'ouvre rien. |
| **O2 gain au prix d'alertes** | B(Δ_k) > 0 **et** Δ̂_k ≥ δ **et** H(φ_L) > φ_max | La chaîne formelle trouve plus sur k, mais rejette trop de preuves saines pour servir de vérificateur à ce point de fonctionnement ; le coût des fausses alertes est rapporté. **Lecture obligatoire avec le rappel conditionnel aux paires formalisables** : si l'écart conditionnel est nul ou négatif, l'écart vient des échecs de formalisation, non d'une détection, et le rapport le dit en tête. |
| **O3 gain sous le seuil** | H(Δ_k) < δ (sous-cas O3b si H(Δ_k) < 0 : suite meilleure) | Sur k, à ce seuil, la suite suffit sur cette banque ; rien sur les classes non testées, rien sur les erreurs de spécification, **aucun statut de norme** pour la suite. |
| **O4 non concluante** | tout autre cas | L'intervalle traverse δ ; aucune conclusion ; l'effectif nécessaire est rapporté, aucune relance sans nouveau devis ni GO. |
| **O0 chaîne non viable** (fin du pilote, § 3.8, A9) | φ̂_L > 0,60 sur les saines du pilote (symétrique : φ̂_S > 0,60 ⇒ « suite non viable ») | La chaîne ne vérifie pas, à ce budget, des preuves courtes saines de ces domaines ; pas de confirmation ; le taux de formalisation par domaine est rapporté (utile au pas (c), § 6). |

Propriété vérifiée par simulation (§ 3.6) : à la frontière Δ = δ, la condition de rappel de O1 sort **environ une fois sur deux**
(0,52 à 0,55), alors que « sous le seuil » n'y sort qu'environ trois fois sur cent : la condition de rappel de O1 n'établit donc pas Δ ≥ δ, elle établit Δ > 0 avec une estimation d'au moins δ ; pour un Δ vrai de 0,15 elle sort encore de 0,14 à 0,31 selon l'effectif et la discordance (contre-lecture 1, annexe, bloc A). C'est pourquoi O1 distingue O1a et O1b. **Au niveau retenu de 97,5 %** (C04 ; `calculs-v2/sortie-calculs-devis-v4.txt`, bloc 2) : à la frontière, la condition de rappel de O1 sort 0,48 à 0,53 et O1a 0,004 à 0,011 ; pour un Δ vrai de 0,15, la condition de rappel sort 0,09 à 0,25 ; pour un Δ vrai de 0,30, O1a sort 0,21 à 0,60, selon l'effectif (74 à 150) et la discordance (0,20 à 0,40).

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
  (A6). **Même règle sur la banque de confirmation**, avant tout passage aux bras (ajout du brouillon 2 ; ligne de coût comptée, CLP-06).
- **Adjudication à l'aveugle des cas litigieux** (analyse de sensibilité seulement ; l'analyse primaire garde les étiquettes de
  construction) : (i) toute saine qui reçoit au moins une alerte, (ii) toute fautive acceptée par au moins un bras, est soumise à l'adjudicateur (même famille que le contrôle des graines : il peut tendre à confirmer des étiquettes de sa propre famille ; pour le mesurer, un tirage de 20 items non litigieux lui est soumis dans le même lot, sans marque, et son taux de confirmation y est rapporté à côté de celui des litigieux ; une saine acceptée par L avec un énoncé jugé fidèle à l'audit garde son étiquette sans adjudication), **sans savoir quel bras a alerté** (localisations fusionnées et
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
| planteur | **GPT-6 Astra** (OpenAI) | troisième famille : la banque n'a le style d'aucun modèle des bras ; identifiant d'interface « rapporté, à confirmer » (`collisionneur_v8.py` l. 79–80) ; repli écrit ci-dessous |
| contrôle des graines, audit de mesure, adjudication à l'aveugle | **Gemini 4 Argon** (Google) | quatrième famille, hors bras et hors planteur |
| contre-lecture du préenregistrement (R2) ; verdict (R13) | contre-lecture 1 faite par Fable 5.2 (N-052 nommait Fable 5.1 : écart signalé à la mère) ; sous-agent neuf (verdict) | N-052 ; R2, R13 |

Variante de modèle des bras (option de D-3), recalculée par fonction (v4) : pilote ordinaire 223,88 avec Sonnet 5.5 et 564,50 avec Fable 5.2, contre 337,42 avec Opus 5.5 ; § 4.3.

**Repli si GPT-6 Astra n'a ni identifiant ni accès confirmés au moment de D-1b** (CLP-05) : (R1) planteur = Gemini 4 Argon ; contrôle des graines par Argon **en contexte neuf** plus le calcul du harnais, audit et adjudication par Argon ; **réserve écrite** : contrôle, audit et adjudication sont alors de la famille du planteur (risque de confirmer ses propres étiquettes, mesuré par le tirage de 20 items non litigieux de C13) ; aucune famille des bras n'entre dans la construction ni le contrôle de la banque ; devis inchangé (mêmes prix supposés, 10 / 50). (R2) reporter D-1b jusqu'à l'accès. Recommandation : (R2) tant que l'échéance de D-1b n'est pas atteinte, (R1) au-delà ; c'est un nœud de compte, chez Lazar.

---

## 3. Bras, puissance, plan d'analyse, arrêts

### 3.1 Bras L — preuve formelle

- **Agent** : Opus 5.5, effort `high`, outil unique `lean_verifier(fichier)` (compilation par `lake env lean` sous la chaîne
  épinglée, délai par appel), au plus 40 tours, **30 minutes de temps de processus** et **4 USD** par item, parallélisme fixé au manifeste (3 processus Lean) (§ 3.3 ; CLP-12 c).
- **Tâche** : écrire l'énoncé formel `enonce_item`, un lemme de premier niveau `etape_i` par étape numérotée (énoncé = celui de
  l'étape écrite), puis la preuve de `enonce_item` ; prouver chaque `etape_i` par toute tactique ; rendre une sortie structurée
  (`ACCEPTE` ou rejet, étape, raison, fichier Lean).
- **Gardes mécaniques du harnais** (le verdict `ACCEPTE` exige toutes) : G-L1 compilation sans erreur ; G-L2 aucun `sorry` ni
  `admit`, et `#print axioms` de `enonce_item` **et de chaque** `etape_i` ne liste que `propext`, `Classical.choice`,
  `Quot.sound` ; G-L3 aucun `axiom`, `unsafe`, `@[implemented_by]`, `@[extern]` dans le fichier ; G-L4 présence des lemmes
  `etape_1` à `etape_m` (m = nombre d'étapes de l'item) et de `enonce_item` ; G-L5 les énoncés **imprimés par Lean** (`#check`
  de `enonce_item` et de chaque `etape_i`) sont ce que reçoit le relecteur de fidélité ; G-L6 (CLP-12 a) aucune `notation`, `macro`, `macro_rules`, `syntax`, `elab`, `infix`, `prefix`, `postfix` dans le fichier de l'agent, et toute définition, abréviation, structure ou instance qu'il introduit est imprimée en entier (`#print`) et envoyée au relecteur avec les énoncés ; G-L7 (CLP-12 b) `#print axioms` et `#check` sont lancés par le harnais dans un **fichier à lui** qui importe celui de l'agent, jamais lus dans une sortie que l'agent contrôle. G-L6 et G-L7 sont à vérifier sur la chaîne installée (D-1a).
  **R5** : chaque garde est éprouvée avant tout lancement sur un cas sain et sur un artefact (preuve à `sorry`, axiome ajouté,
  étape manquante, théorème renommé, `native_decide` dont l'axiome doit apparaître, notation locale qui redéfinit un symbole, **étape à hypothèses contradictoires prouvée à vide** (CLP-12 d), lecture d'un fichier hors du bac et appel réseau pendant la compilation (garde d'isolement, § 4.5)).
- **Relecteur de fidélité** (Kimi K3.1 Pro, un appel) : énoncé et étapes écrites contre énoncé et étapes formels imprimés ;
  étape par étape, fidèle ou non. **Verdict de la chaîne** : `ACCEPTE` seulement si l'agent accepte, les gardes passent et le
  relecteur ne relève aucune infidélité ; sinon `NON-ACCEPTE` avec le motif.

### 3.2 Bras S — suite bon marché (définition)

« Le meilleur assemblage bon marché » (D-T3, synthèse v2 l. 87) à outils locaux, sans assistant de preuve :
- **Relecteur indépendant** (Kimi K3.1 Pro, un appel) : critique étape par étape de la preuve écrite (étape suspecte, raison).
- **Agent** : Opus 5.5, effort `high`, outil `python(code)` exécuté **dans l'environnement isolé** (§ 4.5 : sans clé, sans dépôt, sans réseau) avec les versions de `.venv` : sympy 1.14.0, mpmath 1.3.0, numpy 2.4.6, scipy 1.17.1, et, si la mère l'installe (routine, registre de paquets), le solveur `z3` ;
  méthode imposée par la consigne : vérification symbolique des égalités et inégalités, **recherche de contre-exemples**
  numériques (tirages, bords, cas d'égalité), **mutation de l'énoncé** (l'argument « prouve »-t-il aussi l'énoncé muté faux ? si
  oui, l'étape qui ne distingue pas est suspecte), grille d'audit (hypothèses utilisées à chaque étape, sens des inégalités, cas
  limites). Il reçoit la critique du relecteur et rend la même sortie structurée que L. Mêmes plafonds que L.
- **Verdict de la suite** : `NON-ACCEPTE` si l'agent rejette **ou** si le relecteur marque une étape « fausse » (règle du « ou »,
  symétrique de celle de L).

### 3.3 Coût apparié

Même modèle, même effort, **même plafond par item (4 USD) et même délai de processus (30 minutes)**, parallélisme fixé au manifeste (3 processus Lean, 4 de la suite), dans les deux bras ; chaque bras
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

- **Dimensionnement** (script `calculs-v2/calculs_devis_essai_v4.py`, sortie `calculs-v2/sortie-calculs-devis-v4.txt` ; la v3 reste sous `calculs-v1/`) : pour une demi-largeur h = δ/2 = 0,10 de l'intervalle à 97,5 % de Δ_k, n_k = ⌈2,2414² · d / h²⌉ où d = P(paire discordante) : d = 0,10 → 51 ; 0,15 → 76 ; 0,20 → 101 ; **0,25 → 126** ; 0,30 → 151 ; 0,35 → 176 ; 0,40 → 201 ; 0,50 → 252 (à 95 % : 39 à 193).
- **Probabilités des issues à 97,5 %** (v4, bloc 2 ; 40 000 tirages par case, intervalle gabarit de Wald ajusté « +0,5 par case » ; « gain » = condition de rappel commune à O1 et O2, sans la condition des fausses alertes ; « sous le seuil » = O3 ; « non concluante » = O4) ; à n = 102 et d = 0,30 : Δ vrai 0 → sous le seuil 0,934 ; Δ vrai 0,10 → sous le seuil 0,385, non concluante 0,587, gain 0,028 ; **Δ vrai 0,20 → gain 0,490** (O1a 0,009), sous le seuil 0,016 ; Δ vrai 0,30 → gain 0,988 (O1a 0,420). À n = 150 et d = 0,30 : 0,988 ; 0,526 / 0,460 ; 0,529 (O1a 0,009) ; 0,997 (O1a 0,602).
- **Erreur de famille** (v4, blocs 2b et 2c ; deux classes indépendantes, sans porte) : pour l'affirmation que O1 établit, « Δ > 0 », la probabilité d'au moins une borne basse au-dessus de zéro quand Δ vrai = 0 dans les deux classes est de 0,020 à 0,026 ; au moins un O1a quand Δ vrai = δ : 0,008 à 0,024 ; au moins un « sous le seuil » quand Δ vrai = δ : 0,027 à 0,060, **au-dessus** du niveau visé (0,025) avec ce gabarit, surtout à faible discordance : la simulation de couverture doit vérifier les **deux** bornes (ci-dessous). La condition « estimation ≥ δ » n'est pas une affirmation : à Δ vrai = 0,15 dans les deux classes, elle sort au moins une fois avec une probabilité de 0,26 à 0,36, ce que O1b dit en clair (« ampleur non établie »).
- **Borne des fausses alertes** (v4, bloc 3) : probabilité que H(φ_L) ≤ 0,30 (Clopper–Pearson 97,5 %) : 80 saines → 0,859 si φ = 0,15, 0,463 si φ = 0,20 ; 148 saines → 0,789 si φ = 0,20 ; 200 → 0,905 ; 258 → 0,955 ; 300 → 0,983 si φ = 0,20 ; à φ = 0,25 : 0,110 à 0,464 selon l'effectif.
- **Règle d'effectif de la confirmation** (écrite maintenant, appliquée à la fiche de passage) : n_k = min(150, max(40,
  ⌈2,2414² · d⁺ / 0,10²⌉)) (C04), d⁺ = maximum de la borne haute unilatérale à 80 % (Clopper–Pearson) de la discordance **globale** des 60
  fautives du pilote et de la discordance observée de la classe k. Chaque graine de confirmation donne une saine et une fautive :
  saines = n_1 + n_2 (80 à 300 selon la règle ; 150 à 300 aux scénarios du devis v4). Si n_1 + n_2 < 200, la condition H(φ_L) ≤ φ_max est sous-dimensionnée (borne des fausses alertes, ci-dessus) : la fiche de passage le dit, avec la probabilité calculée. Scénarios (v4, bloc 1b) : 6 discordantes sur 60 au pilote → n_k = 75 ; 9 → 102 ; 12 → 129 ; 15 et plus → 150 (plafond). Le « central 2 × 96 » du brouillon 1 n'était rendu par aucune ligne de la règle (CLP-15 a) : il est retiré ; le devis de la phase 2 se lit par scénario (§ 4.3).
- **Choix des deux classes** (fiche de passage) : classes rangées, par ordre décroissant, selon la différence appariée des écarts « rappel moins fausses alertes » du pilote, (r̂_L,k − φ̂_L,k) − (r̂_S,k − φ̂_S,k), les fausses alertes d'une classe étant lues sur les jumelles saines des graines de cette classe (ex æquo départagés par la graine) ; le rang par Δ̂_k seul est rapporté à côté, sans servir au choix : il désignerait la classe où la chaîne formelle échoue le plus à formaliser (piège du § 1.2) ; classe 1 = la première, classe 2 = la deuxième, **quel que soit le signe** : tester la classe la plus favorable à Lean
  rend un négatif aussi fort qu'il peut l'être, et un positif exposé à une banque neuve (R3, R4). **Variante soumise à Lazar** (D-5 (i bis)) : classe 1 fixée d'avance à K1 « coquille de relation » (ancrée dans les coquilles déjà trouvées par le programme, position de l'espèce A), classe 2 = la première des quatre autres au rang ci-dessus ; même lecture à 97,5 % sans porte, même effectif.
- **Correction** : les deux classes sont lues chacune avec des intervalles à 97,5 % bilatéraux (Bonferroni sur deux classes), sans porte entre elles ; la règle d'effectif s'écrit alors avec 2,24 au lieu de 1,96 (environ 1,31 fois plus de graines à discordance égale, plafond de 150 inchangé ; devis central à refaire). La porte « classe 1 conclusive » de la version précédente ne contrôlait pas l'erreur de famille : elle ouvrait la classe 2 dès que la classe 1 rendait « sous le seuil » (contre-lecture 1, annexe, bloc A).
- **Méthode d'intervalle du préenregistrement** : choisie parmi l'intervalle de score de Tango et l'intervalle hybride de
  Newcombe pour proportions appariées (références RAPPORTÉES, à vérifier), par simulation de couverture sur une grille fixée d'avance (effectifs de 40 à 150, discordances de 0,10 à 0,50), **avant le scellement et avant le pilote**, selon une règle écrite (la méthode dont la couverture minimale sur la grille est la plus proche de la couverture nominale par le haut) ; McNemar exact rapporté en complément. Le gabarit ci-dessus ne sert qu'au dimensionnement. La simulation vérifie la couverture des **deux** bornes au niveau 97,5 % (côté O1 et côté O3, bloc 2c) ; la méthode retenue est inscrite au marqueur « À REMPLIR : MÉTHODE-INTERVALLE » (§ 9) pendant D-1a, avant tout appel de modèle.

### 3.7 Plan d'analyse

- **Primaire** : par classe confirmée, Δ̂_k et son intervalle, φ̂_L, φ̂_S et bornes, issue O1 (O1a ou O1b) à O4 selon le § 1.7 ; dépense par bras ; en tête, décomposition des `NON-ACCEPTE` par motif et part des items au plafond, par bras (CLP-13).
- **Secondaires** (rapportées toutes, sans sélection) : rappel **localisé** (bonne étape) ; rappel **conditionnel aux paires
  formalisables** (items dont la jumelle saine est acceptée par L) ; union L ∪ S moins S ; motifs des `NON-ACCEPTE` (rejet, infidélité,
  plafond, délai, sortie invalide, refus) ; stabilité sous double renotation (pilote) ; acceptations à énoncé infidèle (audit) ;
  coût total, par item (quantiles de la distribution), par détection, temps mural ; résultats par domaine D1 à D5 ; par présence
  d'un témoin numérique dans la clé ; lecture nue et relecteur seul (pilote) ; classifieur de style.
- **Sensibilité** : étiquettes adjugées à l'aveugle (§ 2.5) ; exclusion appariée des pannes techniques de l'un ou l'autre bras ;
  bornes de pire et de meilleur cas pour les items non évaluables (dénominateur sur tous les items assignés, convergence G14) ;
  convention A-T3 pour les acceptations infidèles sur les saines ; taux de confirmation de l'adjudicateur sur le tirage de 20 items non litigieux, rapporté à côté de celui des litigieux (C13).
- **Graines et manifestes** (R9) : `SeedSequence` dérivées par tâche (tirage domaine × classe, ordre, sens de la paire, tirage de
  l'audit, départage des ex æquo) ; un manifeste par phase (configuration et empreinte, versions de Lean, de Mathlib et des
  bibliothèques, identifiants exacts des modèles servis, graines, commit).

### 3.8 Liste d'arrêt (écrite d'avance ; chaque garde éprouvée sur un cas sain et sur un artefact, R5)

- **A1** gardes G-L1 à G-L7, garde d'isolement (§ 4.5), plafonds, compteurs, réserve de A7 et refus de A12 non éprouvés sur un cas sain et sur un artefact ⇒ aucun lancement.
- **A2** modèle servi différent du modèle demandé (identifiant exact) ⇒ arrêt de la phase.
- **A3** refus de modèle sur plus de 10 % des appels d'un bras parmi les 20 premiers items ⇒ arrêt, rapport tel quel, aucune
  reformulation.
- **A4** témoins de fonctionnement : un bras détecte moins de 4 fautes grossières sur 5, ou alerte sur au moins 2 preuves
  trivialement saines sur 5 ⇒ défaut de harnais présumé, arrêt ; correction en version neuve, nouveau scellement.
- **A5** plus de 50 % des graines écartées au contrôle ⇒ arrêt de la construction ; consigne du planteur en version neuve.
- **A6** classifieur de style > 0,70 deux fois de suite, sur la banque de découverte ou sur celle de confirmation ⇒ arrêt.
- **A7** dépense de la phase + pire cas de tous les appels en cours (paires lancées en parallèle comprises) + pire cas du prochain appel, quel qu'il soit (paire, planteur, contrôle des graines, lecture nue, audit, adjudication) > plafond de la phase ⇒ plus aucun lancement (paires complètes). Réserve chiffrée (v4) : 3 items L et 4 items S en vol à 4 USD, plus le plus cher des appels suivants (4 USD) = **32 USD** ; la coupure se déclenche dès que la dépense dépasse le plafond moins 32.
- **A8** étalonnage : la banque du pilote est construite d'abord ; après les 10 témoins et les 10 premières graines (20 items,
  chacun vu par les deux bras), coût projeté du pilote > plafond ⇒ nombre de graines restantes ramené à ⌊(plafond − dépense) /
  coût mesuré par graine⌋ (une graine = deux items vus par les deux bras), **au moins 40 graines au total**, sinon arrêt.
  L'ordre d'exécution suit des **blocs équilibrés** (chaque bloc de 5 graines couvre les 5 classes) pour qu'une coupure (A7, A8)
  garde l'équilibre des classes. Effet chiffré (v4, réserve A7 et adjudication comprises) : au profil supposé, le pilote complet tient sous 450 comme sous 550 (81 et 107 graines payables) ; au profil « pire réaliste » de l'agent L (CLP-09), 35 graines sous 450 (arrêt, sous le minimum de 40), 41 sous 500, **48 sous 550**, 54 sous 600 : d'où le plafond proposé de 550 (§ 4.3).
- **A9** viabilité, fin du pilote : φ̂_L > 0,60 ⇒ O0 et pas de confirmation ; si la borne basse à 95 % (Clopper–Pearson) de φ_L au pilote dépasse φ_max, la fiche de passage écrit que O1 est hors d'atteinte en confirmation (restent O2, O3, O4) et le second GO se prend en le sachant ; φ̂_S > 0,60 ⇒ O0 « suite non viable » ; les deux
  rapportés.
- **A10** échéance de la phase (fixée au GO) dépassée ⇒ arrêt et rapport.
- **A11** toute machine louée s'arrête par son identifiant (R10) et se consigne dans `registres/arrets.md`.
- **A12** (D-1a) aucun appel d'interface facturé tant que le GO de D-1b n'est pas inscrit dans `registres/go.md` : le harnais refuse tout appel sans identifiant de GO valide (garde éprouvée sur un cas sain et sur un artefact).

---

## 4. Devis (aucune dépense avant le GO de Lazar)

Tous les montants sont en USD, calculés par `calculs-v2/calculs_devis_essai_v4.py` (sortie `calculs-v2/sortie-calculs-devis-v4.txt`), qui dérive tous les coûts unitaires en un seul lieu (CLP-15 b) ; les scripts du brouillon 1 restent sous `calculs-v1/` (table des empreintes). Les profils de consommation par appel sont **SUPPOSÉS** ; le pilote les mesure et le devis 2 les remplace.

### 4.1 Prix par million de jetons (entrée / sortie)

| Modèle (rôle) | Entrée | Sortie | Source | Statut |
|---|---|---|---|---|
| Opus 5.5 (agents des bras, lecture nue) | 4 | 20 | référence locale `claude-api` : table « Current Models (cached: 2026-11-03) » et `shared/models.md` l. 83 (`74245a8d…`) | **à vérifier** sur la page publique des tarifs avant GO |
| Sonnet 5.5 (variante) | 2 | 10 | même référence, `shared/models.md` l. 89 | à vérifier |
| Fable 5.2 (variante) | 8 | 40 | même référence, `shared/models.md` l. 78 | à vérifier |
| Kimi K3.1 Pro (relecteurs internes aux bras) | 2 | 10 | `collisionneur_v8.py` l. 76–77 : « Prix vérifiés le 30 octobre » | vérifiés le 30 octobre (RAPPORTÉ) |
| GPT-6 Astra (planteur) | 10 | 50 | `collisionneur_v8.py` l. 79–82 : « Prix SUPPOSÉS … barème volontairement haut » | **à vérifier** (identifiant aussi) |
| Gemini 4 Argon (contrôle, audit, adjudication) | 10 | 50 | `collisionneur_v8.py` l. 73–74 : « valeur volontairement haute » | **à vérifier** |

Cache : le calcul prend une lecture à 0,1 fois le prix d'entrée et une écriture à 1,25 fois ; **le multiplicateur d'écriture n'est pas sur la ligne d'Opus 5.5** (il se lit sur celle de Fable 5.2 : écriture à 10 pour 8) : **à vérifier** (CLP-10 a) ; pour Opus 5.5, `shared/models.md` l. 83 donne 0,20 USD par million en lecture, soit 0,05 fois : l'attendu est donc
prudent sur ce point (à vérifier) ; **les pires cas ne comptent aucun cache**. Le raisonnement des modèles est facturé comme sortie et compté comme tel. Durée de vie du cache (cinq minutes pour l'écriture citée) contre le délai d'une compilation Lean : à vérifier ; si le cache expire entre deux tours, le profil se rapproche du cas « sans cache » (item L ≈ 2,64, contre-lecture 1, bloc D).

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
| adjudication à l'aveugle, par item soumis | Gemini 4 Argon | 6 k ; 4 k | 0,26 | 0,88 (8 k ; 16 k) |
| agent du bras L, profil **pire réaliste** (CLP-09) | Opus 5.5 | 1 000 k ; 100 k ; mêmes parts en cache | 3,04 (item L 3,082 ; rapport L/S 8,24) | 4,00 (plafond par item) |

Rapport attendu des coûts par item L/S : **3,11** (prédiction P4 : entre 2 et 6). **Sensibilité** (contre-lecture 1, annexe, bloc D) : le profil de l'agent L est la supposition qui pèse le plus ; à 60 k de sortie l'item L vaut 1,76 (rapport 4,7) ; à 1 000 k d'entrée et 100 k de sortie, 3,08 (rapport 8,2 ; pilote ramené à 42 graines par A8) ; sans cache, 2,64. Au-delà, l'item touche le plafond de 4 USD, et le plafond devient un motif fréquent de `NON-ACCEPTE` du seul bras L, ce qui gonfle à la fois son rappel et ses fausses alertes : la part des items au plafond, par bras, est une mesure de tête. Avec la réserve de A7 et l'adjudication (v4), l'effet du profil pire réaliste sur A8 est plus fort que dans la contre-lecture : 35 graines payables sous 450 (sous le minimum de 40), 48 sous 550 (§ 3.8).

### 4.3 Devis par pas et par élément

**D-1a — outillage** (aucun appel de modèle ; machine seule) : machine dédiée et isolée (§ 4.5), Lean 4 et Mathlib à un commit
fixé, harnais des deux bras (boucle d'outils, compteurs de jetons par appel, plafonds par item et par phase, réserve de A7, sortie
structurée, gardes G-L1 à G-L7 et garde d'isolement, clé scellée, ordre par paires et par blocs, refus d'appel sans GO de D-1b :
A12), essais R5 des gardes sur cas sains et sur artefacts écrits à la main, simulation de couverture des méthodes d'intervalle
(C09) et de l'erreur de famille, classifieur de style, script d'analyse ; écrit et contre-lu par des sous-agents de la session (coût
d'abonnement, **hors devis d'interface, à confirmer par la mère**). Machine : ≈ 48 heures allumées (SUPPOSÉ) ; **4,80 / 9,60 /
19,20 USD** à 0,10 / 0,20 / 0,40 USD l'heure (prix d'une machine à processeur : **aucune source ici, à vérifier** avant D-2) ;
**borne haute 62,40** au prix horaire des machines à carte graphique du devis de la phase 0 (1,30 USD l'heure,
`brouillons/P3-chaine-v1-brouillon4/lancer_p3_v1.sh` l. 44). **Plafond proposé : 65 USD** (machine seule). Durée : 2 à 3 jours.

**D-1b — pilote** (60 graines, 12 par classe ; 60 saines, 60 fautives, 10 témoins, 10 saines renotées bis : 140 items ; audit sur
50 % ; **seulement après le préenregistrement complet, contre-lu et scellé**) :

| Élément | Attendu, profil supposé | Attendu, profil pire réaliste (CLP-09) |
|---|---|---|
| planteur des graines (72, surgénération de 20 %) | 39,60 | 39,60 |
| planteur des 10 témoins et des 10 renotations bis | 11,00 | 11,00 |
| contrôle des graines | 18,72 | 18,72 |
| bras L | 162,68 | 431,48 |
| bras S | 52,36 | 52,36 |
| lecture nue | 25,20 | 25,20 |
| audit de fidélité (50 %) | 13,30 | 13,30 |
| adjudication à l'aveugle (30 % d'items litigieux, plus 20 non litigieux, C13) | 14,56 | 14,56 |
| **total ordinaire** (entre parenthèses : 60 % d'items litigieux) | **337,42** (346,78) | **606,22** (615,58) |
| conditionnel : audit étendu à tous les items (§ 1.8) | 13,30 | 13,30 |
| conditionnel : banque refaite une fois (A6) | 58,32 | 58,32 |
| conditionnel : graines rejetées jusqu'à 50 % (A5) | 38,88 | 38,88 |
| **total avec toutes les lignes conditionnelles** (60 % d'items litigieux) | **447,92** (457,28) | **716,72** (726,08) |
| pire cas sans plafond (chaque item à son plafond, rejet de 50 % et banque refaite, tous les items audités et adjugés) | 2 048,00 | 2 048,00 |

**Lignes absentes du tableau du brouillon 1, comprises dans le plafond** (estimation de la contre-lecture, reprise telle quelle ; le tableau ci-dessus les chiffre par le script v4) (contre-lecture 1, annexe, bloc E ; mêmes prix et profils) : planteur des 10 témoins et des 10 renotations bis (≈ 11) ; adjudication à l'aveugle (≈ 9 à 19 selon la part d'items litigieux) ; audit étendu à tous les items si l'audit de symétrie du § 1.8 se déclenche (≈ 11) ; banque refaite une fois si le classifieur de style dépasse 0,70 (≈ 58) ; graines rejetées jusqu'à 50 % avant A5 (≈ 39). Avec elles l'attendu du pilote va d'environ 332 à 450, c'est-à-dire jusqu'au plafond ; les mêmes lignes sont à ajouter au devis 2.

**Plafond proposé de D-1b : 550 USD** d'appels (coupures A7 et A8 : la dépense ne peut pas le dépasser ; le pire cas théorique sert
seulement à dire que la coupure est nécessaire). Raison : au profil supposé, 550 couvre l'attendu avec toutes les lignes
conditionnelles (448 à 457) et la réserve de A7 (32) ; au profil pire réaliste, A8 garde 48 graines sur 60 (35 seulement sous 450,
ce qui arrêterait le pilote). Plus la machine : ≈ 26 heures allumées, 2,60 / 5,20 / 10,40 USD à 0,10 / 0,20 / 0,40 USD l'heure,
borne haute 33,80 ; **plafond machine proposé : 35 USD**.

**Phase 2 — confirmation** (deux classes lues chacune à 97,5 %, sans porte ; une saine et une fautive par graine ; audit sur 30 % ;
effectifs par la règle du § 3.6 ; banque de confirmation soumise à A6 ; **sur second GO** avec devis 2 refait sur les coûts mesurés
au pilote) ; v4, par scénario de discordance au pilote :

| Discordantes au pilote | n_k | Items | Attendu ordinaire, profil supposé (60 % litigieux) | Avec lignes conditionnelles | Attendu ordinaire, profil pire réaliste | Pire cas sans plafond |
|---|---|---|---|---|---|---|
| 6 sur 60 | 75 | 300 | 652,30 (675,70) | 935,20 | 1 228,30 | 4 355,60 |
| 9 sur 60 | 102 | 408 | 885,53 (917,36) | 1 270,16 | 1 668,89 | 5 917,28 |
| 12 sur 60 | 129 | 516 | 1 118,57 (1 158,82) | 1 605,12 | 2 109,29 | 7 478,96 |
| 15 sur 60 et plus | 150 | 600 | **1 299,40** (1 346,20) | **1 865,20** | **2 451,40** (3 017,20 avec les conditionnelles) | 8 693,60 |

Détail au plafond d'effectif, profil supposé (v4) : planteur 198,00 ; contrôle des graines 93,60 ; bras L 697,20 ; bras S 224,40 ;
audit 34,20 ; adjudication 52,00 ; conditionnelles : audit étendu 79,80, banque refaite (A6) 291,60, graines rejetées jusqu'à 50 %
194,40.

**Plafond indicatif de la phase 2 : 1 900 USD** (profil supposé, plafond d'effectif : attendu avec toutes les lignes
conditionnelles 1 865,20, plus la réserve de A7). Au profil pire réaliste, l'attendu ordinaire (2 451,40) le dépasse : le devis 2
dira quel profil le pilote a mesuré, et le second GO se prendra sur ce chiffre, en sachant aussi si O1 reste atteignable (C11).
Machine : ≈ 62 à 70 heures allumées, 6,20 à 28,00 USD à 0,10–0,40 USD l'heure, borne haute 91,00 ; plafond machine indicatif
91 USD.

**Engagement maximal** (plafonds proposés ou indicatifs) : D-1a 65 + D-1b 550 + 35 (machine) + phase 2 1 900 + 91 (machine) =
**2 641 USD**. Attendu au profil supposé : D-1b 337 à 457 et phase 2 1 299 à 1 865, soit ≈ 1 636 à 2 322 USD, plus la machine
(≈ 14 à 58 USD à 0,10–0,40 USD l'heure ; borne haute 187,20). Brouillon 1 : 1 900 USD ; l'écart vient de C04 (97,5 %), des lignes
de C08, de la réserve de A7 et du plafond de D-1b relevé pour le profil pire réaliste.

**Options chiffrées** (pour les décisions du § 7) : D-5 (i bis), classe 1 fixée à K1 : même coût que (i). D-5 (ii), une seule
classe lue à 95 %, au plus 150 graines, 300 items : attendu ordinaire 652,30 au profil supposé (même nombre d'items que la ligne
« 6 sur 60 »). D-5 (iii), cinq classes avec Holm : non recalculé en v4 (v3, à 95 % : 3 118,50 ; plus cher à 97,5 % et avec Holm).
D-6 : non pour l'instant (décision de la mère), non compté. Modèle des bras (D-3 ; recalculé par fonction en v4, lecture en cache à
0,1 fois pour tous, approximation, CLP-10 c) : pilote ordinaire Opus 5.5 337,42 / Sonnet 5.5 223,88 / Fable 5.2 564,50 ; phase 2
au plafond d'effectif 1 299,40 / 866,80 / 2 164,60.

### 4.4 Durées (SUPPOSÉES : 15 minutes de processus par item pour L, 3 pour S, 1 pour la lecture nue)

- Pilote : bras L 35 heures de processus, **≈ 12 heures murales** à 3 processus Lean en parallèle (mémoire) ; bras S et lecture
  nue ≈ 9 heures de processus, ≈ 2,3 heures murales à 4.
- Confirmation : bras L 129 (12 discordantes sur 60) à 150 heures de processus (plafond d'effectif, 600 items), **≈ 43 à 50 heures murales** à 3 processus ; bras S ≈ 5 à 8 heures murales ; machine allumée ≈ 62 à 70 heures (v4).
- Calendrier : D-1a, 2 à 3 jours ; pièces « À REMPLIR », vérification, scellement et GO de D-1b, 1 à 2 jours ; pilote, 2 jours (construction, exécution) ; fiche
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
  programme (Anthropic ; Kimi par le relais local ; OpenAI ; Gemini), aucun compte neuf prévu ; si l'accès à GPT-6 Astra ou à Argon manque, c'est un nœud de compte (repli : § 2.7). **Nature de la dépense** (CLP-05) : appels d'interface facturés au jeton chez **quatre fournisseurs** (Anthropic pour les bras, Moonshot pour les relecteurs, OpenAI pour le planteur, Google pour le contrôle, l'audit et l'adjudication) et une **machine louée** ; ce n'est pas un « devis d'appels de sous-agents » au sens littéral de R-959 : Lazar l'accorde en le sachant (D-1b).
- **Isolement des outils (cloison et secrets)** : `lean_verifier` et `python(code)` exécutent du code écrit par un modèle (un fichier Lean peut lire des fichiers et lancer des processus pendant sa compilation) ; ils ne tournent que sur une machine ou dans un conteneur qui ne contient ni le dépôt de travail, ni aucune clé, et sans réseau sortant ; le harnais, qui porte les clés, reste hors de cet environnement et n'y envoie que le fichier à vérifier ou le code à exécuter. Garde éprouvée sur un cas sain et sur un artefact (lecture d'un fichier hors du bac, appel réseau) avant tout lancement (R5 ; ajoutée à A1).
- **Garde de calcul** : toute machine louée cite un GO valide de `registres/go.md` (`.claude/hooks/garde_calcul.py`) et s'arrête
  par identifiant (R10).
- **Exigence de la mère (CLP-04)** : la machine dédiée ne porte **ni clé ni dépôt du programme** ; le code écrit par un modèle n'y voit ni `/home/user/controle-ia-travail` ni aucune variable de clé ; le harnais, qui porte les clés, tourne hors de la machine et ne lui envoie que le fichier Lean ou le code Python à exécuter ; la liaison entre les deux (accès distant à la machine) est un point d'environnement à vérifier (D-2). Artefacts de la garde : un fichier Lean et un code Python qui tentent de lire un chemin du dépôt, d'énumérer les variables d'environnement et d'ouvrir une connexion sortante ; chaque tentative doit échouer et être journalisée (R5), un cas sain (compilation ordinaire) doit passer.
- **Machine (CLP-10 b)** : aucun prix horaire de machine à processeur n'a de source ici (aucun réseau) ; chiffrage par durée allumée × prix (v4) : D-1a ≈ 48 h, D-1b ≈ 26 h, phase 2 ≈ 62 à 70 h ; 14,40 à 57,60 USD au total à 0,10–0,40 USD l'heure ; borne haute 187,20 au prix des machines à carte graphique du devis de la phase 0. Machine éteinte entre les pas (arrêt par identifiant, R10), sauf décision contraire au GO.

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
- **les lacunes de justification** : les assertions vraies mal justifiées sont exclues de la banque (§ 2.2) et le squelette laisse prouver chaque étape par n'importe quel chemin ; l'essai ne dit donc rien d'une étape vraie que l'argument écrit n'établit pas, cas où une vérification de l'argument lui-même pourrait avoir un avantage ;
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

Les recommandations suivent l'accord de la mère sur la contre-lecture 1 (D-3 (a), D-4 (i) sous C01 et C02, D-5 (i) amendée par C03
et C04, D-6 non pour l'instant) ; elles restent des propositions : Lazar décide.

**D-1 — enjeu commun à D-1a et D-1b.** Enjeu : seul pas autorisé par N12 (b) ; sans lui, (b) s'arrête au devis. **Nature de la dépense, à accorder explicitement** : R-959 parle d'un « devis d'appels de sous-agents » ; ce devis demande autre chose, des appels d'interface au jeton chez quatre fournisseurs (dont GPT-6 Astra, identifiant et accès non confirmés : nœud de compte, avec un repli à écrire) et, selon D-2, une machine louée. **Ordre** : le pilote est une expérience décisive (viabilité A9, choix des classes) ; son GO ne se prend qu'après le scellement du préenregistrement complet (méthode d'intervalle, consignes du planteur et des bras, commit de Mathlib, script d'analyse, gardes éprouvées), qui exige l'outillage. D-1 se scinde donc en **D-1a** (outillage : aucun appel de modèle facturé, machine selon D-2) et **D-1b** (pilote, après scellement et contre-lecture).

**D-1a — GO de l'outillage (machine seule, aucun appel de modèle).** Enjeu : sans outillage, ni le préenregistrement (méthode
d'intervalle, gardes éprouvées, commit de Mathlib) ni le pilote ne peuvent exister ; c'est une dépense de calcul (machine louée),
donc un nœud. Options : (i) GO, machine dédiée et isolée, plafond **65 USD**, échéance à fixer (avantage : lève les trois obstacles
sans aucun appel de modèle ; inconvénient : prix horaire non vérifié, devis de la machine à produire avant location) ; (ii) attendre
(aucune dépense ; le préenregistrement reste incomplet, D-1b impossible). Recommandation : **(i)**, confiance 0,65. Défaut : aucune
dépense (nœud).

**D-1b — GO du pilote (seulement après le préenregistrement complet, contre-lu et scellé).** Enjeu : la première mesure ; la nature
de la dépense est à accorder (interface chez quatre fournisseurs). Options : (i) GO, plafond **550 USD** d'appels plus **35 USD** de
machine (avantage : pilote complet au profil supposé, et d'au moins 48 graines sur 60 au profil pire réaliste ; inconvénient : attendu 337 à 457
au profil supposé, la coupure joue au profil pire réaliste) ; (ii) GO à 450 USD (moins cher ; au profil pire réaliste, A8 arrête le
pilote à 35 graines, sous le minimum de 40) ; (iii) pilote réduit à 40 graines (non recalculé en v4 ; écarté par la contre-lecture :
huit items par classe ne portent pas un choix de classes). Recommandation : **(i)**, confiance 0,55, à prendre seulement après le
scellement. Défaut : aucune dépense.

**D-2 — Machine et réseau pour Lean.** Enjeu : d'abord la **cloison** (CLP-04 : les outils exécutent du code écrit par un modèle),
ensuite le disque (2,7 Go libres). Options : (i) machine processeur dédiée, louée sur devis, sans clé ni dépôt du programme, harnais
hors de la machine (avantage : cloison et place ; inconvénient : location, prix à vérifier, accès distant à ouvrir) ; (ii) conteneur
sans accès au dépôt ni aux clés sur une autre infrastructure (acceptable seulement à ces conditions) ; (iii) attendre.
Recommandation : **(i)**, confiance 0,65. Défaut : aucun (nœud d'environnement et de dépense).

**D-3 — Qui formalise ; modèles et familles.** Enjeu : divergence des espèces (C : autre famille ; E : opérateurs) ; détermine ce que
l'écart mesure. Options : (a) **même modèle (Opus 5.5) dans les deux bras, seuls les outils diffèrent** ; relecteurs Kimi K3.1 Pro
dans les deux bras ; planteur GPT-6 Astra (repli R1 ou R2 du § 2.7 s'il manque) ; contrôle, audit et adjudication Gemini 4 Argon
(avantage : l'écart mesure l'outil ; la contre-lecture n'y trouve aucun avantage indu à Opus 5.5 ; inconvénient : pas « le meilleur
formaliseur ») ; (b) formaliseur d'une autre famille que la suite (avantage : proche d'un usage ; inconvénient : modèle et outil
confondus) ; (c) opérateurs humains (avantage : fidélité ; inconvénient : contact externe, dépense, délais). Variantes du modèle des
bras (v4) : Sonnet 5.5, pilote 223,88 (O0 plus probable pour une raison de modèle, non d'outil) ; Fable 5.2, 564,50 (ne se justifie
pas au prix). Recommandation : **(a) avec Opus 5.5**, confiance 0,6. Défaut sous 48 heures : (a).

**D-4 — Seuils.** Enjeu : fixent l'issue ; à geler avant scellement. Options : (i) **δ = 0,20, φ_max = 0,30, sous C01 et C02** (O1
lu O1a ou O1b, lecture conditionnelle obligatoire) ; à savoir : avec la prédiction P1 (écart de fausses alertes d'au moins +0,15), O1
est presque hors d'atteinte, φ_max décide autant que δ ; (ii) δ = 0,15 (plus fin ; effectif multiplié par (0,10 / 0,075)² ≈ 1,8 à
discordance égale, phase 2 plus chère) ; (iii) δ = 0,25 (moins cher ; ne voit que de gros gains). Recommandation : **(i)**, confiance
0,5. Défaut sous 48 heures : (i).

**D-5 — Une ou plusieurs classes.** Enjeu : divergence des espèces (A : une classe préenregistrée ; B, C, E : plusieurs avec
correction) ; détermine l'effectif et le coût de la phase 2. Options : (i) **amendée** : pilote sur les cinq classes ; deux classes
choisies sur la différence des écarts « rappel moins fausses alertes » (C03), quel que soit le signe, lues chacune à 97,5 % sans porte
(C04) ; phase 2 attendue 652,30 à 1 299,40 au profil supposé selon la discordance du pilote (avantage : contrôle de l'erreur de
famille pour les affirmations établies ; inconvénient : coût, sélection sur les données du pilote) ; (i bis) **variante** : classe 1
fixée d'avance à K1 « coquille de relation », classe 2 choisie par le pilote, même coût (avantage : une classe ancrée dans l'usage et
non sélectionnée ; inconvénient : K1 peut être peu favorable à Lean et rendre un négatif moins fort) ; (ii) une seule classe fixée (K1)
lue à 95 % (attendu 652,30 ; aucune sélection ; une seule classe mesurée) ; (iii) cinq classes avec Holm (non recalculé ; v3 à 95 % :
3 118,50). Recommandation : **(i) amendée**, (i bis) exposée comme alternative proche ; confiance 0,55. Défaut sous 48 heures : (i)
amendée.

**D-6 — Banque d'usage (L0 et 21 lemmes de la carte des hypothèses v1).** Décision de la mère : **non pour l'instant** (c'est le
défaut) ; la carte v1 n'est pas sur `main`, attend des corrections et ses lemmes n'ont pas d'étiquette ; à reposer après le pilote,
sur la carte corrigée, si Lazar le souhaite. Non compté dans l'engagement.

---

## 8. Points ouverts et à vérifier avant scellement

1. Prix d'Opus 5.5, de Sonnet 5.5 et de Fable 5.2 sur la page publique ; prix et identifiants d'interface de GPT-6 Astra et de
   Gemini 4 Argon ; accès effectifs (comptes) ; repli R1 ou R2 si GPT-6 Astra manque (§ 2.7).
2. Taille de Mathlib et de son cache, mémoire par processus Lean, hôtes de téléchargement ; commit à épingler (§ 9).
3. Profils de consommation (§ 4.2) et durées (§ 4.4) : suppositions, l'écart entre profil supposé et pire réaliste pèse un facteur
   près de deux sur le pilote ; durée de vie du cache contre le délai d'une compilation ; le pilote mesure, le devis 2 remplace.
4. Méthode d'intervalle (Tango ou Newcombe) fixée en D-1a par simulation sur une grille d'avance (C09), en vérifiant les **deux**
   bornes : le gabarit de Wald dépasse le niveau visé côté O3 à faible discordance (v4, bloc 2c). Références des méthodes nommées :
   RAPPORTÉES, à vérifier ; aucun chiffre de l'état de l'art n'est utilisé (R7).
5. Le coût des sous-agents de la session est-il une dépense au sens du programme ? (à confirmer par la mère).
6. Carte des hypothèses v1 : hors de `main`, corrections annoncées, D-6 non pour l'instant.
7. Modèle du contre-lecteur : Fable 5.2 au lieu du Fable 5.1 de N-052 ; la contre-lecture 1 juge suffisante une **vérification
   courte** du brouillon 2 par un sous-agent neuf si les 14 couples sont appliqués tels quels et si les voies de CLP-02 et CLP-03 ne
   changent pas (c'est le cas : couples appliqués par programme, C03 et C04 retenus ; seules retouches de texte inséré, documentées
   au journal : le titre du paragraphe de C08 et le complément de C10) ; à la mère de dire si une seconde contre-lecture entière est
   requise.
8. Adjudicateur : contrôlé par le tirage de 20 items non litigieux et le certificat mécanique des saines (C13) ; une adjudication
   humaine reste la meilleure voie, mais c'est du temps de Lazar ou un contact externe : à lui de dire.
9. Prix horaire et devis de la machine dédiée ; liaison entre le harnais et la machine (accès distant) ; aucune clé ni dépôt sur la
   machine (§ 4.5).
10. Gardes G-L6 et G-L7 : à vérifier sur la chaîne installée ; limite du délai si le parallélisme n'est pas tenu.

## 9. Pièces à remplir avant le scellement (marqueurs « À REMPLIR », refusés par le validateur des préenregistrements)

Chaque marqueur est remplacé par un chemin et une empreinte (R6) avant le scellement du préenregistrement ; aucune de ces pièces
n'exige d'appel de modèle, toutes se produisent en D-1a ou à la table.

- « À REMPLIR : MÉTHODE-INTERVALLE » — Tango ou Newcombe, choisie par la simulation de C09 sur la grille fixée (effectifs de 40 à 150,
  discordances de 0,10 à 0,50, niveau 97,5 %, deux bornes) ; script et sortie.
- « À REMPLIR : VERSION-LEAN » et « À REMPLIR : COMMIT-MATHLIB » — chaîne et commit épinglés à l'installation (D-1a).
- « À REMPLIR : SEUILS-GELÉS » — δ et φ_max gelés par Lazar (D-4).
- « À REMPLIR : CONSIGNE-PLANTEUR » — consigne du planteur, version neuve scellée, avec des exemples génériques de chaque classe qui
  ne viennent d'aucune banque ; consigne de repli (R1) si GPT-6 Astra manque.
- « À REMPLIR : CONSIGNES-BRAS » — tronc commun, instructions d'outil de L et de S, consigne de la lecture nue.
- « À REMPLIR : CONSIGNES-RELECTEURS-CONTRÔLE-AUDIT-ADJUDICATION » — relecteurs Kimi des deux bras, contrôle des graines, audit de
  fidélité, adjudication avec son tirage de 20 items non litigieux.
- « À REMPLIR : HARNAIS-ET-ISOLEMENT » — code du harnais et de l'environnement isolé (commit, empreinte).
- « À REMPLIR : ESSAIS-R5 » — rapport des essais des gardes G-L1 à G-L7, de la garde d'isolement, de A7, A8 et A12, sur cas sains et
  sur artefacts.
- « À REMPLIR : SCRIPT-ANALYSE » — script d'analyse scellé, fiche de passage comprise (choix des classes par C03, règle d'effectif).
- « À REMPLIR : IDENTIFIANTS-MODÈLES » et « À REMPLIR : PRIX-VÉRIFIÉS » — identifiants exacts servis et prix relevés sur les pages
  publiques, avec leur date.
- « À REMPLIR : MACHINE » — fournisseur, caractéristiques, prix horaire, identifiant.
- « À REMPLIR : ÉCHÉANCES » — échéances de D-1b et de la phase 2 (A10).

---

## Table des empreintes (SHA-256, calculées par script à l'assemblage ; aucune valeur retapée)

| Fichier | Rôle | SHA-256 | Compagnon |
|---|---|---|---|
| `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-devis-essai-preuve-formelle-couche4-v1.md` | consigne ; lue en entier | `5403571b05f6733a69ec8e26cbd6ecc53d2d8243fe1c77288ee058c77d45cfba` | égale au compagnon |
| `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` | interdits communs v2, recopiés dans la consigne | `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` | égale au compagnon |
| `prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon1-cl1.md` | contre-lecture 1 (Fable 5.2) ; lue en entier ; source des 14 couples | `f565d51cd39ae047d50a1774e79c67301f54ab5c1c107c4cba50193d33ba7744` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon1.md` | brouillon 1, intact ; texte de départ des couples | `9ccc9ac01cb95db8184f87629e3b77eaa24820717ffa29a822f471ccf91bdade` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-journal-v1.md` | journal du brouillon 1, intact | `f8c2b8c64e3e9c7125c1496321765be0b3891c809e36a290cbc1b484c1cd003d` | égale au compagnon |
| `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-tour2-v1.md` | synthèse du tour 2 ; lue en entier (brouillon 1) | `6ef6bc2e1cbea69b0b47f20508fa09391e7c2271785287c470dc632de5a2b1ce` | égale au compagnon |
| `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-v2.md` | synthèse v2 ; lue en entier (brouillon 1) | `f0340581766c5fb4d97a0ccb06f0cf1738a15228385b332ee602e93a0be28f0a` | égale au compagnon |
| `docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v2.md` | programme complet v2 ; parties lues (brouillon 1) | `dffe0b632bfa24ffa5af3e460110515e05dfc74283d856a15eba01afab168556` | égale au compagnon |
| `docs/notes/ideation-organisme-v1/course-2/collisionneur-v8/collisionneur_v8.py` | table des prix, l. 60–95 | `22e5ed8a64075f2f985755d9bff2c2336d8edc5f73cbc3b0511405fd8f43d264` | égale au compagnon |
| `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` | l. 384–388, 436–440, 800–810 (carte des hypothèses v1) | `186173d9d9b949bfb3922503adff1be9d60f49f07fb975750de4c88bd60a060e` | égale au compagnon |
| `brouillons/P3-chaine-v1-brouillon4/lancer_p3_v1.sh` | l. 44 : prix horaire de borne haute (1,30 USD l'heure) | `8cd40e08ee4cab05356cd73f433c541f5ae22abe279b6b261621ea52038e4e12` | égale au compagnon |
| `registres/decisions.md` | registre vivant : R-920, R-946, R-957, R-959, R-2199 à R-2226 (lus pour le brouillon 1) | `187c36d7cd87b2bd7f6d3c8f9a7f58e96f74d40fa7072726eec189b42efcde99` | pas de compagnon (registre vivant) |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v1/calculs_devis_essai_v1.py` | copie versée par la mère des calculs et jalons du brouillon 1 (égale au bac à sable d'origine) | `6f374d0c651e1ce127ab99841ce4f51efcb13433407a0af19f82fcede953f9f3` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v1/calculs_devis_essai_v2.py` | copie versée par la mère des calculs et jalons du brouillon 1 (égale au bac à sable d'origine) | `d57e176b24258d2c1f650f111e7a136b5b9bf08b8a761b01fe9b86cf6dfb278c` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v1/calculs_devis_essai_v3.py` | copie versée par la mère des calculs et jalons du brouillon 1 (égale au bac à sable d'origine) | `236371fdcdc754b997286ca3add3cf1c05c67ff29f65161df03350af694472c7` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v1/jalon1-journal-v1.md` | copie versée par la mère des calculs et jalons du brouillon 1 (égale au bac à sable d'origine) | `966949d52d51de7164c4bc78848130c3744e0530cf5cda4e402328958fb92c90` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v1/jalon2-brouillon-sections-0-3-v1.md` | copie versée par la mère des calculs et jalons du brouillon 1 (égale au bac à sable d'origine) | `4b98b352028c0a78592e1c63d1452807185dd610590c178fa2b8ff78201c4e8a` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v1/option_pilote_reduit_v1.py` | copie versée par la mère des calculs et jalons du brouillon 1 (égale au bac à sable d'origine) | `cb8a5dc230d04229ff1ad797e8094db505886060086ed5718ad455503b603e63` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v1/sortie-calculs-devis-v1.txt` | copie versée par la mère des calculs et jalons du brouillon 1 (égale au bac à sable d'origine) | `7fb79ee398095b08000032433dc66f9e89564b0d69734469f547098054bc364f` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v1/sortie-calculs-devis-v2.txt` | copie versée par la mère des calculs et jalons du brouillon 1 (égale au bac à sable d'origine) | `d6492d79c636996105c4bfa89376651b92a7afbb653a72cee885a5a78cab6f7d` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v1/sortie-calculs-devis-v3.txt` | copie versée par la mère des calculs et jalons du brouillon 1 (égale au bac à sable d'origine) | `18221e7b6b676cdaa88bf8e095202da3a2ac475876aeb61ecf78c4fe7ad1d7f3` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v1/sortie-option-pilote-reduit-v1.txt` | copie versée par la mère des calculs et jalons du brouillon 1 (égale au bac à sable d'origine) | `6a4d0ae69b72f610d93d1d94e493978884bfef99cd8de2afdd250c9481a3452d` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v1/sortie-variantes-modele-bras-v1.txt` | copie versée par la mère des calculs et jalons du brouillon 1 (égale au bac à sable d'origine) | `3651c56cc976cd119b280afbdfb7e42d58650bddf16afe47510af3e81367cbf0` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v1/variantes_modele_bras_v1.py` | copie versée par la mère des calculs et jalons du brouillon 1 (égale au bac à sable d'origine) | `25ff8f46ca92afadb23127984c77d923a9eac86fd2247efdfff841da034e980d` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v2/appliquer_couples_cl1_v1.py` | brouillon 2 : application programmatique des 14 couples | `c09eeefc1b29d62a1cbfbcd5883f7b6d27a4cb63e5ea6c1e515ea9377d6e99f9` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v2/calculs_devis_essai_v4.py` | brouillon 2 : calculs v4 (C04, CLP-06, CLP-09, CLP-10) | `9dc88b634eacb970c1a92a1a04d654946b20310396354dd364c6981561e37a4d` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v2/sortie-appliquer-couples-cl1-v1.txt` | brouillon 2 : sortie de l'application des couples | `c992bbf6b7fb627ff52ecfa1d2a09635ef9ef9e4eadb3df2eff00afb0ac2cdd1` | égale au compagnon |
| `brouillons/couche4-essai-preuve-formelle-v1/calculs-v2/sortie-calculs-devis-v4.txt` | brouillon 2 : sortie des calculs v4 | `d44c4573437d436d35e2a37b331f02008081428c3161f3f90055f346d755e57e` | égale au compagnon |
| `/tmp/claude-0/bundled-skills/2.1.322/3f5d19faa48e8729fa23bef895bf9c5b/claude-api/shared/models.md` | référence locale de prix de l'outil `claude-api` (hors dépôt, non un fichier du rédacteur), l. 78, 80, 83, 89 | `74245a8d11939d988321c47ab4b4775ac1fa287f97ed94f7b65eb6145bcbe7b9` | pas de compagnon |

Table assemblée par script le Tue Nov 10 13:44:57 UTC 2026 (horloge du système, UTC). L'empreinte du présent brouillon est celle de son compagnon `.sha256`. Aucun fichier du bac à sable du rédacteur n'est cité : les calculs et jalons du brouillon 1 le sont par leurs copies sous `calculs-v1/` (mêmes empreintes) ; les instantanés de jalon du brouillon 2 sont décrits au journal v2.
