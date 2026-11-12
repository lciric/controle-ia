# Faits pour le collisionneur — la « Boucle d'or » : fenêtre de distance entre parents et allocation des expériences (v1)

Statut : **RAPPORTÉ** (pièces du programme, transcrites telles quelles, empreinte de chacune vérifiée contre son compagnon ou contre l'empreinte que cite la question). Aucun sigle de financeur. Aucun score de pilote. Rien ici n'est une consigne. Pièces nommées par la question v1 de conv-audit (`2e9db80b…`) : A (branche `canal/conv-audit-relais-memoire-v1`, commit `0ba98ae` ; ses chiffres de l'étude d'Uzzi et collègues sont lus par transcription, non vérifiés sur un PDF empreinté : à lire comme tels) ; P, le plan seul, sans ses résultats (commit `de4dbf6`) ; R en deux parties, R1 sur `main` et R2 ; T ; C (branche `canal/conv-audit-n04`, commit `03851f5`, mêmes octets qu'à `de4dbf6` pour R2, T et C).

<<<DÉBUT A — avis de l'instance sortante de conv-audit sur la « Boucle d'or » (branche `canal/conv-audit-relais-memoire-v1`, commit `0ba98ae`) (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/avis-boucle-d-or-gemini-v1.md`, sha256 `0414f1ab4dc7a76346e885d4b2c2f69293af094fc52db966e1915cb1363000aa` ; ses chiffres de l'étude d'Uzzi et collègues sont lus par transcription, non vérifiés sur un PDF empreinté)>>>

# Avis de l'instance sortante de conv-audit sur la « Boucle d'or » de Gemini (v6.3.0) — v1

Écrit le 27 octobre 2026 à partir de 08:18 UTC (heure lue sur `date -u`). Pièce lue : la réponse de Gemini relayée par
Lazar (09:16 heure de Paris), fichier joint d'empreinte `2784138902c62532602fa9e3f738d58c7ab7ed7e52c4f7cd422f7fc19f3acb1e`
(non versée ; son script PowerShell n'est pas exécuté ici). Exploratoire, non opposable.

## Verdict

Les deux idées valent d'être éprouvées : une fenêtre non monotone sur la distance entre parents, et une allocation du
budget d'expériences selon le gain d'information. Mais la simulation de Gemini ne prouve rien : elle est construite
pour passer. Ne pas l'adopter sur ce chiffre. Gemini a vérifié le commit `52d4b2f7` (huit empreintes, **avant
l'addendum**), pas `ce22a89` : il n'a pas vu la rétrodiction (la marche « à la Swanson » ne bat pas l'allocation de
ressources), et sa brique 1 se branche encore sur cette marche. Envoyer le texte PowerShell v2 (neuf « OK »).

## Pourquoi la simulation ne prouve rien

1. **Circulaire** : les mondes rangent les hypothèses en trois strates par bandes de similarité de domaine
   (0,50-0,80 / 0,12-0,26 / 0-0,015) ; la fenêtre de l'allocateur est centrée dans la bande du milieu ; la mémoire de
   calibration lui est **donnée** avec les taux de survie mêmes du monde (18/20, 10/20, 1/20) ; les triviales ne
   comptent jamais comme découvertes, les chimères presque jamais (3 %). Le facteur « × 2,5 » découle de l'arithmétique de la construction
   (environ 0,5 découverte par dollar pour la strate du milieu, environ 0,17 au hasard) ; l'essai qui exige « > 1,8 fois »
   vérifie que le monde a été construit comme prévu.
2. **Bandit de paille** : le bonus « UCB » ne dépend que de l'indice du monde, le même pour toutes les hypothèses ; c'est
   un tri glouton sur la probabilité de survie, récompensé par la survie et non par la découverte. Un vrai bandit récompensé
   par les découvertes (par exemple un échantillonnage de Thompson par strate) apprendrait les mêmes strates.
3. **Prémisse fausse pour notre juge** : Gemini assimile « triviale » à « survit à 90 % ». Chez nous, une fille sans contenu
   nouveau est dans son propre nul : elle survit au plus à α. Ce n'est pas l'allocateur qui écarte les triviales, c'est le
   juge. L'objectif juste est l'espérance de découvertes vraies par dollar, plus la valeur d'apprendre la calibration ;
   l'entropie du verdict (maximale à p = 0,5) n'en est qu'un substitut, utile surtout au début. Le score
   H₂(p) × 4p(1−p) × pénalité compte deux fois la même chose et n'a pas de fondement.

## Uzzi et collègues (2013)

Référence juste : *Science* 342, 468-472 ; 17,9 millions d'articles du Web of Science ; conventionnalité = z médian des
paires de revues citées ensemble, nouveauté = z au 10ᵉ centile. Taux de « hits » (5 % les plus cités) :
**9,11 pour 100** pour les articles à forte conventionnalité et forte nouveauté, contre 5 pour 100 en moyenne ; **5,33 pour
100** pour faible conventionnalité et forte nouveauté (lu par transcription du PDF de Kellogg, page 469 ; à revérifier sur
PDF empreinté avant tout usage, R7). Deux inexactitudes chez Gemini : les proportions « 85-90 % d'ancrage, 10-15 % de
nouveauté » ne sont pas dans l'article ; les articles très atypiques ne « s'effondrent » pas, ils restent au niveau de la
moyenne. Surtout, la transposition est inventée : Uzzi mesure les paires de revues dans les références d'**un** article,
pas la similarité entre **deux** articles parents ; le centre de la fenêtre (0,18 dans le code, 0,22 dans le texte) et sa
largeur ne sont étalonnés sur rien.

## Le test qui pourrait échouer (proposé, dans l'orchestrateur, sur processeur)

- L'allocateur apprend la calibration **en ligne** (rien n'est donné) ; ses concurrents : hasard, échantillonnage de
  Thompson récompensé par les découvertes, tri par espérance de découverte par dollar.
- Mondes où la valeur **ne suit pas** la fenêtre (monotone, ou maximale aux bords) : la fenêtre doit y perdre (contrôle
  « monde inversé », comme pour les ponts plantés).
- Mesure : découvertes vraies par dollar sur les témoins, promues par le juge v1 ; seuil préenregistré.
- Pour la fenêtre d'Uzzi sur données réelles : il faut les citations (OpenAlex avec une clé : décision de Lazar).

<<<FIN A>>>

<<<DÉBUT P — plan d'essai de conv-audit, fixé avant tout lancement, sans ses résultats (commit `de4dbf6`) (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/essais-boucle-d-or-v1/plan-essai-boucle-d-or-v1.md`, sha256 `f2653da3496bced948c2e2d0a48c46a4736a91b1086dd061f72158ffb856f861`)>>>

# Essai « Boucle d'or » — l'allocateur à fenêtre de Gemini contre des allocateurs qui apprennent — plan v1 (fixé avant tout lancement)

Lignée conv-audit (instance nouvelle), écrit le 27 octobre 2026 à partir de 08:22 UTC (heure lue sur `date -u`), sur le
mot de Lazar de 09:20 heure de Paris, d'après l'avis de l'instance sortante `avis-boucle-d-or-gemini-v1.md`
(`0414f1ab4dc7a76346e885d4b2c2f69293af094fc52db966e1915cb1363000aa`, branche `canal/conv-audit-relais-memoire-v1`, commit
`0ba98ae`). **Exploratoire (R-522), non opposable, lu dans les deux sens.** Ce plan est poussé avant le premier lancement ;
aucun essai, même de fumée, n'a tourné avant lui. Le script PowerShell de Gemini n'est ni lu ni exécuté.

## Question

L'allocateur de Gemini — ne tester que les filles dont les parents ont une similarité de domaine dans une **fenêtre**
(0,12 à 0,26, la bande du milieu de sa simulation) et, dans la fenêtre, viser l'**entropie** maximale du verdict — fait-il
plus de découvertes vraies par dollar que des allocateurs qui **apprennent en ligne**, quand la valeur suit la fenêtre, et
perd-il quand elle ne la suit pas ?

## Monde, candidats, juge

- Par répétition, un réservoir de 300 filles candidates. Chacune : similarité de domaine s tirée uniformément sur
  [0 ; 0,8] (seule information visible des allocateurs) ; elle est **vraie** (contenu neuf sur les traits) avec la
  probabilité v(s) du monde, sinon fausse.
- Vraie : monde = parent A sur la sous-population 0, loi neuve sur la 1 (force tirée uniformément sur [0,3 ; 1,5], pour
  des effets de taille variée) ; la fille prédit exactement cela (forme « fille neuve » de l'expérience 1).
- Fausse : monde tiré parmi « parent A vrai », « parents vrais par sous-population », « mélange des parents » ; la fille
  est une copie du parent A ou une enveloppe aveugle des parents (formes contenues dans le nul augmenté). Le trou connu du
  critère des filles (« parent + loi aveugle ») est **exclu** de cet essai, et dit.
- Tester une fille = le **juge v1** (ordre secret, urne, nul augmenté des parents, marge 2δ₀ = 0,02), 50 tirages de
  calibrage et 200 tirages frais, coût d'un dollar simulé par test. Une découverte vraie = une fille vraie promue.
- Mêmes nombres aléatoires pour tous les allocateurs dans une répétition : le réservoir, les vérités et l'issue du juge
  pour une fille donnée sont les mêmes quel que soit l'allocateur qui la teste.

## Mondes v(s)

| monde | v(s) | la fenêtre devrait |
|---|---|---|
| cloche | 0,5 si 0,12 ≤ s ≤ 0,26, sinon 0,05 | gagner |
| bords | 0,5 si s < 0,06 ou s > 0,6, sinon 0,05 | perdre |
| croissant (proches meilleurs) | 0,05 + 0,55·s/0,8 | perdre |
| décroissant (lointains meilleurs) | 0,60 − 0,55·s/0,8 | perdre |
| plat | 0,2 | ne rien changer |

## Allocateurs (budget : 40 tests par répétition ; une fille au plus une fois ; rien ne leur est donné)

- **hasard** : uniforme parmi les filles non testées.
- **Thompson** : huit cases de s (largeur 0,1), loi bêta(1, 1) par case sur la probabilité de promotion ; à chaque test,
  un tirage par case ; une fille non testée au hasard dans la case du plus grand tirage ; récompense = promotion par le juge.
- **tri par espérance de découvertes par dollar** : mêmes cases, moyenne a posteriori (coût constant) ; égalités tirées au
  hasard.
- **fenêtre (Boucle d'or)** : seulement s dans [0,12 ; 0,26] ; sept cases de largeur 0,02 ; probabilité de promotion
  apprise en ligne par case (moyenne a posteriori bêta(1, 1)) ; choisit la case d'entropie maximale du verdict (la plus
  proche de 0,5) ; fenêtre épuisée → hasard sur le reste (dit au rapport).

## Mesure, seuil, lecture (fixés ici)

- Mesure : découvertes vraies par dollar = filles vraies promues / 40, par répétition ; rapportées aussi : promotions
  fausses par dollar.
- 30 répétitions par monde ; graine maîtresse **20261027** (exploration), dérivation `graine_derivee` (SHA-256).
- Différences appariées, sur les 30 répétitions : D₁ = fenêtre − meilleur des deux allocateurs appris (Thompson ou tri,
  le meilleur des deux choisi par sa moyenne dans ce monde) ; D₂ = fenêtre − hasard. Intervalle à 95 % par rééchantillonnage
  des répétitions (10 000 tirages, graine dérivée de la graine maîtresse).
- **Lecture par monde** : la fenêtre **gagne** si l'intervalle de D₁ est entièrement au-dessus de 0 ; **perd** s'il est
  entièrement au-dessous ; **indistincte** sinon. Même lecture pour D₂ contre le hasard.
- **Verdict d'ensemble** : la fenêtre est **à garder** seulement si elle gagne contre les allocateurs appris dans le monde
  « cloche » **et** ne perd contre eux dans aucun des quatre autres ; **à écarter** si elle perd dans au moins un monde
  où la valeur ne suit pas la fenêtre et ne gagne pas dans « cloche » ; **à garder sous condition** (seulement si l'on sait
  d'avance que la valeur suit la fenêtre) si elle gagne dans « cloche » et perd ailleurs.
- **Mes prédictions** (signées, confiance) : cloche — gagne contre le hasard (0,9), indistincte ou gagne contre les
  appris (0,6) ; bords, croissant, décroissant — perd contre les appris (0,8) ; plat — indistincte (0,8). Verdict
  d'ensemble prédit : « à garder sous condition » (0,6).
- **Ce qui mettrait l'essai en défaut** : Thompson pas meilleur que le hasard dans les mondes non plats (apprentissage
  trop lent pour ce budget : l'essai ne départagerait rien) ; promotions fausses au-dessus de α en moyenne (le juge
  serait en cause, pas l'allocation).

<<<FIN P>>>

<<<DÉBUT R1 — synthèse du tour « recombinaison bisociative » (R-527, sur `main`) (`docs/notes/pole-scientifique-automatique/synthese-recombinaison-v1.md`, sha256 `47490973ce85c18bb1c2a15511a830e61e9b2cf43b9ccc083271e8dde12bc65a`)>>>

# Recombinaison bisociative — synthèse du tour du collisionneur (v1)

- **Pour** Lazar. Écrite le 26 octobre 2026 par « session-depot », à partir des neuf cellules du tour (GO-2026-10-26-07, R-526 ; `donnees/collisionneur-recombinaison-v1`, `19aa452`). Matériau de décision, jamais une consigne. Étiquettes RAPPORTÉ / HYPOTHÈSE conservées des modèles.
- **Modèles** : A = Fable 5.1, B = Opus 5.5, C = Gemini. Neuf cellules valides, aucun refus, 8,86 USD. **Toutes les pièces servies** (méta-conception, relecture, génération 0 de conv-audit, synthèse R-525). Pièce C4 (test « ponts plantés ») non rendue au départ.

## Verdict en cinq lignes

1. **Le tirage déterminantal d'origine est mort** : son noyau n'est pas semi-défini positif (1 000 violations sur 1 000, génération 0 de conv-audit) et il récompense la *similarité* de domaine, l'inverse de ce qu'on veut. La méta-conception de Gemini citait en outre des fonctions **absentes** du vrai code v6.2.1.
2. **La forme corrigée est juste algébriquement, mais incomplète.** Elle cède sur quatre points : quand la représentation de domaine porte le gabarit ou le style ; sur les opérateurs « moyeux » et les jargons rares fabriqués (il faut rareté **et** structure) ; sur les homonymes ; et dans les petits corpus sans pont, faute d'abstention.
3. **Les deux équipes rouges trouvent le même trou, plus grave que le tirage** : le critère « la fille prédit plus que ses parents » est **franchissable à coût nul** par des tricheurs scriptés (enveloppe harmonique aveugle, copie renommée, pari couvert, adimensionnement, jargon rare). L'attaque la plus forte : une simple enveloppe bat la conjonction même sur un anti-oracle.
4. **La première expérience n'est donc pas « quel tirage », c'est « le critère de contenu résiste-t-il aux tricheurs ? »** — processeur seul, ~0 USD, cette semaine, aucun appel de fusion. C'est le **même principe que la première expérience du pôle** (valider le juge avant de choisir le moteur), appliqué à la recombinaison.
5. **Pour la version 0** : recombiner des **hypothèses** du pôle (observable, prédiction), pas des articles ; tirage **stratifié** sur domaine estimé (le témoin que personne n'attaque) + appariement par opérateur **forcé après le tirage** + filtre de compatibilité ; le noyau déterminantal corrigé n'est adopté que s'il bat la stratification à budget égal sur étiquettes **estimées et bruitées** (indécis, c'est l'expérience 1).

## Ce qui survit aux essais sur processeur (génération 0, RAPPORTÉ, non réaudité)

1. Normalisation des hachages SimHash 3-grammes avant relèvement (+0,135 de rappel ; accord topologique 0,014 → 0,48).
2. Noyau corrigé L = diag(q)·(S + εI)·diag(q), S_ij = ⟨d_i, d_j⟩² (diversité de domaine dans la répulsion, pertinence dans la qualité), Sinkhorn sur S seul : 0,90 à 0,95 de paires de domaines distincts sans perte de qualité.
3. **Attraction d'opérateur hors du noyau déterminantal** : appariement forcé après le tirage (0,995 à 1,00 sur étiquettes propres).
4. Filtre de pivots par fréquence de fond externe (rejette les « hubs » génériques).
5. Filtre lexical de compatibilité : ramène les fusions contradictoires de 55,9 % à 34,4 %.

## La première expérience (convergente, chiffrée par les trois)

**Valider le critère de contenu contre des tricheurs, avant tout appel de fusion.** Processeur seul, ~0 USD, moins de dix minutes, réutilise l'infrastructure NumPy de la génération 0.
- Faire passer au critère et au monde planté une **batterie de tricheurs scriptés** : tricheur de forme, copie-renommée, **enveloppe aveugle**, fille constante, pari couvert, adimensionnement. Aucun appel de modèle.
- Issue 1 : un tricheur promu au-delà de α **invalide le critère avant toute dépense** — on s'arrête là.
- Issue 2 : aucun tricheur promu → le banc devient opposable, et on passe au plan factoriel {noyau continu, grille discrète} × {lexique, arbre d'opérateurs} à budget égal, sur étiquettes **estimées et bruitées**, pour trancher entre la grille (A et C) et le noyau corrigé (B).
- Règle de contenu durcie : une fille doit **battre l'enveloppe harmonique de 2 δ₀** (pas seulement la conjonction), avec une règle de score propre sur données fraîches, trois familles de modèles distinctes (générateur, extracteur, fusionneur), et des lois tenues hors calibrage.

## Ce qu'aucun modèle n'a établi (tout HYPOTHÈSE)

- Qu'une fusion par modèle de langue accroisse vraiment le contenu empirique (plutôt qu'une juxtaposition ou une copie).
- Qu'un critère mécanique sépare un vrai pont d'un homonyme.
- Que le tirage déterminantal batte la stratification à budget égal, sur étiquettes estimées.
- Qu'un signal d'opérateur batte une prédiction de liens classique sur la littérature réelle.
- C4 absente : aucun monde planté réel n'a encore été couru (le test de conv-audit est en cours).

## Pour toi, maintenant

- **Forme v0** : stratification + opérateur après tirage + filtre, avec abstention ; le noyau corrigé en réserve, à départager par l'expérience 1.
- **La première expérience est sur processeur, quasi gratuite, et elle va droit vers un résultat net** : soit elle casse notre critère (et nous épargne une dépense), soit elle le rend opposable. conv-audit en écrit déjà le code ; je l'exécuterai sous préenregistrement scellé.
- **Convergence des deux tours** : avant de dépenser sur un moteur (pôle) ou un tirage (recombinaison), valider le juge contre des tricheurs à coût nul. C'est le chemin solide.

<<<FIN R1>>>

<<<DÉBUT R2 — essai des ponts plantés « trancher la recombinaison » (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/trancher-recombinaison/trancher-recombinaison-v1.md`, sha256 `72cff8a067641cab173f3b6fbba32976a64989ded279d078ec4da432a582e4bf`)>>>

# Trancher la recombinaison bisociative — un test qui pouvait échouer — v1

Rédigé le 2026-10-26T19:21:35Z (heure lue sur `date -u` dans la commande qui l'écrit). Lignée conv-audit, sous-agent neuf ;
processeur seul, bibliothèque standard de Python 3.13.17 (`python3 -I -B`). Préenregistrement scellé avant toute
exécution d'une méthode : `preenregistrement-trancher-recombinaison-v1.md` (`5335614b…`, scellé à 19:10:31 UTC ; run
lancé à 19:13:44 UTC). Régime exploratoire : rien d'opposable. Chiffres : `resultats-trancher-recombinaison-v1.json`
(`daaef112…`) sauf mention ; « points » = points de pourcentage ; crochets = intervalle à 95 % (2 000
rééchantillonnages appariés des mondes).

## Décision : **réfutée**

- La forme corrigée **perd** contre le tirage stratifié qui reçoit le même étage commun (même choix d'opérateur après
  tirage, même filtre) : **−4,8 points [−6,3 ; −3,3]** dans les mondes bien observés et **−2,2 [−3,4 ; −1,0]** dans les
  mondes moyennement observés (400 mondes chacun). Le seuil d'adoption était **+12** dans les deux.
- Elle ne fait pas mieux qu'un tirage uniforme parmi les mêmes paires valides : +0,4 [−1,0 ; +2,0] et −0,1
  [−1,3 ; +1,0]. Son noyau ne cible pas l'éloignement des paires : part de paires éloignées 0,532 contre 0,525 pour
  l'uniforme.
- Contrôles. Monde sans pont : aucun artefact, aucune perte (placebo −0,5 [−1,6 ; +0,5]). Monde inversé : elle
  perd (−3,5 [−4,5 ; −2,6]). Le contrôle passe à la lettre, mais **pas pour la raison attendue** (section 2.2).
- Aucune autre forme n'atteint le seuil. La meilleure mesurée est la **marche de Swanson par étiquette rare (d1)** :
  +3,5 [+2,0 ; +5,0] et +3,8 [+2,7 ; +4,9] sur le stratifié, +8,3 et +6,0 sur la forme corrigée. **Forme gardée par
  défaut : le tirage stratifié (b)**, plus simple et meilleur que (a). (d1) est la candidate à essayer ensuite ; la
  règle ne la retient pas.

## 1. Chiffres principaux

Précision = part de vrais ponts parmi les 12 paires tirées par monde (k = 4 paires × 3 générations), moyenne sur 400
mondes ; écart apparié au stratifié.

| Bras | bien : précision | écart à (b) | moyen : précision | écart à (b) |
|---|---|---|---|---|
| (a) forme corrigée | 0,155 [0,144 ; 0,168] | **−4,8 [−6,3 ; −3,3]** | 0,105 [0,096 ; 0,115] | **−2,2 [−3,4 ; −1,0]** |
| (b) tirage stratifié | 0,203 [0,192 ; 0,215] | — | 0,127 [0,118 ; 0,137] | — |
| (c) tirage uniforme | 0,151 [0,141 ; 0,162] | −5,2 [−6,5 ; −4,0] | 0,107 [0,098 ; 0,115] | −2,1 [−3,1 ; −0,9] |
| (d1) marche de Swanson | 0,239 [0,227 ; 0,249] | +3,5 [+2,0 ; +5,0] | 0,165 [0,155 ; 0,175] | +3,8 [+2,7 ; +4,9] |
| (d2) contraste d'import | 0,137 [0,121 ; 0,151] | −6,7 [−8,3 ; −5,0] | 0,093 [0,082 ; 0,105] | −3,4 [−4,8 ; −2,1] |
| (e) forme du rapport, γ minimal | 0,147 [0,136 ; 0,157] | −5,7 [−6,9 ; −4,4] | 0,094 [0,085 ; 0,102] | −3,4 [−4,3 ; −2,3] |
| diagnostic a_2dpp (déterminantal exact à 2) | 0,152 | −5,1 [−6,4 ; −3,8] | 0,108 | −1,9 [−3,0 ; −0,8] |
| diagnostic a_q1 (a avec q ≡ 1) | 0,163 | −4,0 [−5,4 ; −2,7] | 0,106 | −2,1 [−3,2 ; −1,0] |
| diagnostic b_eloigne (strates dissemblables d'abord) | 0,322 | +11,9 [+10,4 ; +13,4] | 0,193 | +6,6 [+5,5 ; +7,8] |
| diagnostic d1_inv (poids 1 / fréquence) | 0,257 | +5,3 [+3,8 ; +6,8] | 0,175 | +4,8 [+3,6 ; +6,0] |
| plafond (oracle) | 0,750 | — | 0,487 | — |

Rappel des ponts à budget fixé (bien / moyen) : (a) 0,161 / 0,108 ; (b) 0,214 / 0,131 ; (c) 0,157 / 0,109 ; (d1) 0,253 /
0,175 ; (d2) 0,131 / 0,089 ; (e) 0,148 / 0,094. Écart de rappel (a) − (b) : −5,3 [−6,8 ; −3,7] et −2,3 [−3,5 ; −1,1].

Pièges tirés, mondes bien observés (part des 12 paires) : opérateur-pont moyeu (a) 0,347, (b) 0,385, (c) 0,345, (d1)
0,122 ; homonyme 0,033 / 0,038 / 0,036 / 0,040 ; parasite 0,059 / 0,076 / 0,060 / 0,070 ; contraintes vraiment
incompatibles (le filtre en laisse passer) 0,271 / 0,262 / 0,274 / 0,251. Diversité : part de paires éloignées 0,532 /
0,654 / 0,525 / 0,446 ; strates distinctes par paire 0,707 / 0,998 / 0,765 / 0,736.

Par nombre de champs (bien), écart (a) − (b) : −3,5 [−6,0 ; −1,1] (2 champs), −5,8 [−8,2 ; −3,3] (3), −5,2 [−8,0 ; −2,4]
(4). La forme corrigée perd dans toutes les géométries.

## 2. Contrôles

### 2.1 Monde sans pont planté

La vérité y est vide : précision 0 pour tous. Mesure préenregistrée : la précision contre un placebo (6 paires valides
tirées au hasard, graine propre au monde, indépendante des bras). (a) 0,133, (b) 0,139, (c) 0,138, (d1) 0,140, (d2)
0,139. Écarts au stratifié : (a) −0,5 [−1,6 ; +0,5], (d1) +0,2 [−0,9 ; +1,2], (d2) +0,0 [−1,1 ; +1,1]. **Ni artefact, ni
perte.** Sur les 124 écarts placebo de toutes les conditions, 4 ont un intervalle qui exclut 0 (3,2 %), dont (a) − (b)
en domaines mal séparés (+1,2 [+0,2 ; +2,2]). L'espérance est nulle par construction et ce taux est celui du hasard.
Ce que les méthodes tirent quand il n'y a rien à trouver : paires éloignées (a) 0,458, (b) 0,586, (d1) 0,269 ; moyeux
0,446 / 0,532 / 0,187 ; contraintes incompatibles 0,346 / 0,333 / 0,338.

### 2.2 Monde à vérité inversée (les ponts relient des domaines proches)

(a) perd contre (b) : −3,5 [−4,5 ; −2,6]. Le contrôle préenregistré passe. Mais il passe pour une autre raison que
celle visée par le brief :
- (a) − (c) vaut +0,4 [−1,0 ; +2,0] dans le monde normal et −0,8 [−1,8 ; +0,2] dans le monde inversé. Aucun
  changement significatif : la forme corrigée ne préfère pas les domaines éloignés.
- L'écart (a) − (b) passe de −4,8 à −3,5 : il **remonte** quand on inverse la vérité. C'est le contraire de ce que
  ferait une méthode qui cible l'éloignement.
- Le diagnostic qui cible vraiment l'éloignement (b_eloigne) passe de +11,9 à **−11,6 [−12,5 ; −10,8]** (précision
  0,001) : c'est ce que le contrôle devait détecter.
- La perte de (a) dans le monde inversé vient de l'avantage du stratifié, présent dans les deux mondes (section 3), et
  non d'une préférence pour l'éloignement.

### 2.3 Hypothèses de la forme corrigée violées

- **Domaines mal séparés** (cosinus 0,44 / 0,41 / 0,33 au lieu de 0,54 / 0,28 / 0,03) : (a) − (b) = −4,5 [−6,0 ; −3,0],
  comme dans le monde normal. Le critère d'échec préenregistré ne s'applique pas (seuils non atteints). La forme
  corrigée ne dépend pas du vecteur de domaine, parce qu'elle ne s'en servait déjà pas pour les paires.
- **Étiquettes d'opérateur absentes** (étage commun réduit à « domaines différents + filtre ») : tous au taux de base
  (≈ 0,025) : (a) 0,028, (b) 0,024, (c) 0,029 ; (a) − (b) +0,4 [−0,3 ; +1,1]. (d1), (d2) et (e) ne s'appliquent pas
  (elles reposent sur les étiquettes).
- **Moyeux dominants** (deux moyeux à 0,6) : (a) 0,044, (b) 0,040, (c) 0,034 ; (a) − (b) +0,4 [−0,4 ; +1,1]. La marche
  de Swanson tient : 0,210, soit **+17,0 [+15,9 ; +18,1]** sur le stratifié. Éviter les moyeux est le seul mécanisme qui
  survit à cette violation.
- **Mal observé** : (a) 0,060, (b) 0,066, (c) 0,067 ; (a) − (b) −0,6 [−1,5 ; +0,3] ; (d1) +3,7 [+2,7 ; +4,6].

## 3. Pourquoi la forme corrigée vaut un tirage uniforme

Audit fait après lecture des résultats, descriptif ; aucune règle n'en dépend (`audit-mecanisme-v1.json`,
`f28a2238…`, 400 mondes bien observés, graines du run).
- L'ordre glouton suit la qualité : corrélation de rang 0,977 entre l'ordre et q. Ici q (la pertinence) est
  indépendante de la vérité, comme dans l'essai. q² varie d'un facteur 9 ; la répulsion entre domaines proches est
  S = cos² = 0,093 (éloignés 0,001 ; même domaine 0,309).
- Avec q ≡ 1, le noyau diversifie bien les **articles** : 7,8 domaines distincts parmi les 8 premiers, contre 6,1
  avec q. Il ne diversifie pas les **paires** : part de paires proches parmi ses 12 paires, 0,452 (q ≡ 1) et 0,449 (q),
  pour 0,449 dans l'ensemble des paires valides. Un ensemble d'articles divers contient toutes les paires de domaines,
  proches comprises. Or les paires proches sont les plus denses en paires valides (opérateurs partagés dans un champ).
  La forme corrigée les tire donc dans leur proportion, comme l'uniforme.
- Le stratifié gagne parce qu'il équilibre les **paires de domaines** : il donne le même poids à chaque strate, ce qui
  allège les strates denses en partages de fond. Part de paires proches : 0,329 contre 0,451 pour l'uniforme.
- C'est structurel, pas un artefact du monde. Pour une paire, le déterminant vaut q_i² q_j² ((1 + γ)² − cos⁴). À
  cos = 0,28 (domaines proches), la pénalité est de 0,6 %. Pour préférer les paires éloignées, il faudrait des domaines
  proches à cos ≳ 0,8, c'est-à-dire presque confondus. Le processus déterminantal exact à 2 éléments (a_2dpp) le
  confirme : −5,1 et −1,9, comme (a).

## 4. Les autres formes

- **(d1) Marche de Swanson.** Provenance : caste 3 (Opus) du rapport de l'essaim, « marche aléatoire sur graphe biparti
  Concepts × Articles pondérée par IDF des concepts-ponts ». C'est le schéma A–B–C de la découverte fondée sur la
  littérature (Swanson, 1986 ; de mémoire, non vérifié). Adaptation : les concepts sont les étiquettes d'opérateur
  observées, pas les mots. Dans ces mondes, les mots de domaine sont les plus rares mais ne franchissent jamais un
  domaine. C'est la meilleure forme mesurée, et ses gains ont deux sources :
  - elle évite les moyeux : pièges moyeux 0,122 contre 0,385 ;
  - elle trouve les jumeaux : rappel 0,434 contre 0,269 pour (b) et 0,180 pour (a). Sur les greffes, elle fait jeu égal
    (0,188 contre 0,193).
  Elle ne cible pas l'éloignement (paires éloignées 0,446). Elle tient dans le monde inversé (+4,6 [+3,4 ; +5,8]) et
  domine quand les moyeux dominent (+17,0). Son avantage disparaît quand les moyeux sont rares (sensibilité moyeux à
  0,10 : −0,2 [−1,3 ; +0,9]) et grandit à 0,50 (+10,1 [+8,9 ; +11,2]). Elle reste sous le seuil dans les mondes de
  décision.
- **(d2) Appariement par structure de cooccurrences étiquette × domaine.** Je l'ai construite à partir de l'exemple du
  brief. Une étiquette courante dans un domaine et rare dans l'autre signale un import ; le principe est voisin des
  « combinaisons atypiques » de la scientométrie (Uzzi et al., 2013 ; de mémoire, non vérifié). C'est un échec :
  −6,7 et −3,4. Elle ne trouve pas mieux les greffes (0,172 contre 0,193), manque les jumeaux par construction
  (0,013) et se concentre sur peu de strates (0,454). Avec 5 articles par domaine, la fréquence par domaine est trop
  bruitée.
- **(e) Forme du rapport de Gemini, pour mémoire.** Noyau q_i q_j ⟨o_i,o_j⟩² (1 − cos²), Sinkhorn-Knopp 5
  itérations, puis γ minimal pour la rendre semi-définie positive (médiane 0,94 ; 0,76 avec moyeux dominants).
  Elle tourne dans tous les mondes étiquetés. Elle est un peu sous l'uniforme (0,147 contre 0,151) et perd contre le
  stratifié (−5,7). C'est l'effet décrit par l'essai : une fois réparée, elle repousse les paires qu'elle visait.
- **Ce que vaudrait l'idée bisociative elle-même**, avec un a priori d'éloignement grossier (diagnostic b_eloigne,
  qui sert d'abord les strates dissemblables) : +11,9 [+10,4 ; +13,4] (bien), +6,6 [+5,5 ; +7,8] (moyen), +10,2
  (domaines mal séparés), −11,6 (inversé). Par nombre de champs (bien), le gain est de +19,4 (2 champs), +11,0 (3) et
  +3,9 (4). La valeur de l'éloignement dépend de la part de paires de domaines proches et du bruit des étiquettes. Même
  cet a priori idéalisé n'atteint pas +12 dans les deux mondes de décision. Il n'est pas éligible (diagnostic).

## 5. Méthode (détail : préenregistrement)

- **Mondes** (`monde_v1.py`, `conditions_v1.py`) :
  - 8 domaines × 5 articles, répartis en 2, 3 ou 4 champs tirés par monde ;
  - 3 opérateurs latents par groupe, avec un mot de surface différent dans chaque domaine ; opérateurs propres à un
    article ; un moyeu présent dans 25 % des articles ;
  - 3 greffes et 3 jumeaux plantés par monde. Vérité : champs différents, opérateur latent non moyeu commun,
    contraintes vraies compatibles. Soit 12,3 vraies paires par monde, dont 9,5 valides en « bien ».
  - Observations : vecteur de domaine (fréquences brutes des mots hors lexique, cosinus exacts ; validés à 0,54 /
    0,28 / 0,03 avant toute méthode) ; étiquette de domaine juste à 0,95 ; lexique d'opérateurs à trois niveaux
    (couverture 0,90 / 0,70 / 0,45, parasites 0,05 / 0,15 / 0,30, homonymes 0,05 / 0,10 / 0,20) ; contraintes par le
    canal de l'essai b4 (rappel du filtre mesuré 0,57 à 0,60, rejets à tort 4 à 5 %).
- **Budget et étage commun** : k = 4 paires par génération, 3 générations, mêmes 40 candidats, aucune paire retirée
  deux fois. Toutes les sorties sont des paires valides : domaines observés différents, étiquette partagée (opérateur
  retenu après tirage = la plus rare), filtre passé.
- **Bras** :
  - (a) correctif c5 de l'essai étendu à k paires : ordre glouton du déterminant maximal par Cholesky incrémentale,
    vérifié contre un glouton par déterminants explicites (50 cas sur 50) ; paires rangées par (rang maximal, somme
    des rangs) ;
  - (b) tour aléatoire des strates (paires de domaines observés), puis une paire valide au hasard dans la strate ;
  - (c) tirage uniforme ;
  - (d1), (d2) et (e) : section 4 ; γ minimal vérifié contre des valeurs propres de Jacobi (écart 4·10⁻⁹).
- **Graines** :
  - monde : `random.Random(20261026000000 + 100000 × identifiant + indice)` ;
  - bras : `random.Random(f"{graine}-{bras}")` ;
  - placebo : `random.Random(f"placebo-{graine}")` ;
  - rééchantillonnage : `random.Random(20261026)`.
  Run complet en 93 s ; relance : `python3 -I -B trancher_v1.py --heure "$(date -u +%Y-%m-%dT%H:%M:%SZ)"`.

## 6. Ce que ce test ne dit pas

- **Il porte sur le tirage**, c'est-à-dire sur les paires envoyées à la fusion. Il ne dit rien de la qualité des
  hypothèses fusionnées par un modèle. Une fusion pourrait tirer parti de paires que la vérité synthétique ne compte
  pas, ou gâcher de vrais ponts.
- **Un monde synthétique encode mes hypothèses**, notamment trois :
  - les ponts sont des partages d'opérateur entre champs ;
  - le partage de fond est concentré dans les champs, ce qui favorise le stratifié, comme je l'avais écrit avant les
    résultats (préenregistrement, section 6) ;
  - les moyeux sont présents à 25 %.
  Si, dans la littérature réelle, le partage d'opérateurs n'est pas plus dense entre domaines proches, l'avantage du
  stratifié sur l'uniforme fond. La forme corrigée resterait pourtant au niveau de l'uniforme, puisque son noyau
  n'agit pas sur les paires (section 3).
- **Il ne dit pas que l'idée bisociative est fausse.** Un a priori d'éloignement grossier gagne +11,9 et +6,6 ici. Il
  dit que le noyau corrigé ne la met pas en œuvre.
- **Ce qui n'a pas été testé** :
  - des noyaux plus tranchants (exponentielle du cosinus), ou un noyau sur les paires de domaines (c'est, à peu près,
    le stratifié pondéré) ;
  - une pertinence q corrélée aux ponts ;
  - des viviers plus grands (ici n = 40, soit 5 articles par domaine) ;
  - la dynamique réelle des survivants d'une génération à l'autre.
- **Comment j'ai essayé d'éviter de favoriser une forme par construction** :
  - préenregistrement scellé avant toute méthode, avec la liste de ce qui pouvait favoriser chaque bras ;
  - mondes ordinaires calibrés pour **satisfaire** l'hypothèse de la forme corrigée (vecteur de domaine qui code la
    proximité), vérifiés sur des graines de validation distinctes ;
  - géométrie des champs tirée par monde ;
  - deux mécanismes de pont, pour ne servir ni les formes « rareté » ni les formes « import » ;
  - articles mélangés (aucun avantage d'indice) ; étage commun identique pour tous ;
  - cosinus exacts, c'est-à-dire la meilleure version possible du vecteur de domaine ;
  - deux mises en œuvre de (a) et une ablation de q, qui concordent.
  L'instrument sait enregistrer de grands gains : plafond 0,750, +11,9 pour le diagnostic d'éloignement, +17,0 pour
  (d1) avec moyeux dominants. La réfutation ne vient donc pas d'un monde où rien ne peut gagner.

## 7. Contrôles que je crois mal posés (dit à part ; la décision ne change pas)

1. **Monde sans pont.** Avec la vérité définie par les ponts, la précision y vaut 0 pour toutes les méthodes : le
   contrôle est vide. Je l'ai mis en œuvre par un placebo. Celui-ci ne peut échouer que par un artefact de mesure
   (fuite, effet d'ordre, agrégation). Pour savoir si un avantage vient des ponts, il vaut mieux décomposer l'écart du
   monde normal en une part « éloignement » et une part « opérateur » que de demander l'égalité.
2. **Monde inversé.** « La forme corrigée doit y perdre » est satisfait dès que le comparateur gagne dans les deux
   mondes, ce qui est le cas ici. Il faudrait exiger que l'écart **baisse** quand on inverse la vérité (Δ_inversé −
   Δ_normal < 0, intervalle sous 0) ou comparer au tirage uniforme muni du même étage. Ici, l'écart remonte de 1,3
   point ; pour le diagnostic d'éloignement, il chute de 23,5.
3. **Seuil absolu de 12 points.** À des précisions de 10 à 20 %, +12 points signifie ×1,6 à ×2,2 : même l'a priori
   d'éloignement idéalisé ne l'atteint pas dans les deux mondes. Un seuil relatif, ou un rapport gain / coût de la
   machinerie, comparerait mieux les formes. La forme corrigée perd ici en absolu comme en relatif.

## 8. Étape suivante proposée (non exécutée) : rétrodiction sur littérature réelle

- **Principe.** On fige une date T. Avec la seule information antérieure à T, on construit des viviers d'articles de
  champs différents. Chaque bras tire ses paires avec le même budget et le même étage commun. Une paire est un « pont
  réalisé » si les deux littératures étaient disjointes avant T et deviennent reliées après T, dans une fenêtre fixée
  d'avance. Disjointes : ni références communes, ni cocitation, ni comention de leurs termes clés. Reliées : un
  article postérieur les cite ensemble ou combine leurs termes clés, à la manière des cas de Swanson. On garde les
  mêmes mesures, la même règle et les mêmes contrôles : dates tirées au hasard ou liens mélangés pour le monde sans
  pont, liens entre champs proches pour le monde inversé.
- **Données nécessaires** :
  - un corpus bibliographique daté, avec résumés, rattachement disciplinaire et références (par exemple l'instantané
    ouvert d'OpenAlex : dates, thèmes, résumés, références ; ou les métadonnées d'arXiv : catégories, dates, résumés,
    plus une source de citations) ;
  - une taxonomie à deux niveaux (champ, domaine) figée à T, pour dire « proche » et « éloigné » ;
  - un lexique d'opérateurs (méthodes, structures mathématiques) figé avant T, et sa couverture mesurée sur un
    échantillon annoté à la main. C'est elle qui situe le réel parmi les trois niveaux d'observation ;
  - un lexique de marqueurs de contraintes, avec son rappel mesuré ;
  - la définition du lien après T et son taux de base, sans doute très faible : il faudra des viviers assez grands ou un
    échantillonnage stratifié des paires candidates ;
  - les cas historiques de Swanson, comme vérification qualitative seulement : leur sélection est biaisée.
- **Garde contre les fuites** : vecteurs, lexiques et fréquences calculés sur le texte antérieur à T ; aucune
  information de citation postérieure à T dans les entrées.
- **Coût** : processeur, sans appel de modèle pour le tirage. Le téléchargement du corpus est un accès réseau : il
  attend le GO de Lazar. La qualité des fusions par un modèle reste une expérience distincte.

## 9. Réserves et écarts

- Aucune contre-lecture par un sous-agent neuf (R2) : le brief interdit les sous-agents. À faire avant tout usage.
- J'ai changé la pondération du vecteur de domaine (TF-IDF → fréquences brutes) **avant toute méthode**. Avec le
  TF-IDF, domaines proches et éloignés étaient presque indiscernables (0,11 contre 0,009), donc l'hypothèse de la
  forme corrigée n'était pas satisfaite. Ce choix la **favorise**.
- R12 : la première sortie de validation (TF-IDF) a été écrasée par la seconde, sous le même nom. Ses chiffres
  (cosinus 0,48 / 0,11 / 0,009) viennent de la console. La première ligne de `calibrer_vocabulaire_v1.py` la reproduit.
- (d1), (d2) et (e) ne s'appliquent pas au monde sans étiquettes. Le préenregistrement ne le disait pas ; cela découle
  de leur définition.
- L'audit du mécanisme (section 3) est postérieur aux résultats et descriptif.
- Les provenances bibliographiques (Swanson ; Uzzi et al.) sont citées de mémoire, sans chiffre (R7).

## 10. Fichiers (sous `sortie/`) et empreintes

| Fichier | Rôle | SHA-256 |
|---|---|---|
| `preenregistrement-trancher-recombinaison-v1.md` | règles gelées avant toute méthode | `5335614b2b8b38deb50408c4755401242e5a8436f82b1f9e8be48e57f9dd2985` |
| `resultats-trancher-recombinaison-v1.json` | agrégats, intervalles, décision, manifeste | `daaef112ce5a402bda785c1206db222c8f94793afaf7c0ced910467b4bf4a624` |
| `mondes-trancher-recombinaison-v1.jsonl` | mesures brutes par monde et par bras (4 000 mondes) | `9677cc3ca31d762234de79e07a083d907f30839e6a9dd169246894542e8ad1d3` |
| `validation-generateur-v1.json` | propriétés des mondes, graines de validation | `41e475982974be3ae631dcfa6092eb239887e053a844ec9a95b7f45ffa86d3b3` |
| `audit-mecanisme-v1.json` | audit de la section 3 | `f28a2238223a28e2877e9de4559e7cd120fbb8987dedf21f70c6efea3b8e92e0` |
| `monde_v1.py` | générateur | `af907b1d5d779dfc1c4353503d31059f20d031a4b4324fea3ca775ad6a6bc98c` |
| `conditions_v1.py` | conditions, graines | `9246ecc6a4a71f8a701600a0c55c549d622423496a436f2f708b0d9ffe53af35` |
| `methodes_v1.py` | bras | `2f7a8b1192a79d5bed64fb48f9a5db6f1df6bf86e3a2296eafca75493f2790dd` |
| `mesures_v1.py` | mesures, rééchantillonnage | `0a1e3c3806ae892a526fa6a21bcf07217e6f41118244a7cdd01a2f8ad9f8a82e` |
| `trancher_v1.py` | lanceur et règle de décision | `781335dda51954f5d4ac1ab25ce0ce850a421d8c0c2346ae8284fddc8a6609e0` |
| `tests_v1.py` | tests des instruments | `bf12486a5936ad50cdfe7d6407477cdb99442f2c9ebf2d9f64da6a288b70c037` |
| `valider_generateur_v1.py` | validation du générateur | `c2aef23e4d48aa6b12231db6d4f1cdcf3fbc548bfe178d4d61f53c128fa5978f` |
| `calibrer_vocabulaire_v1.py` | calibrage du vecteur de domaine | `a0aec03e885857ce202795dd18bada3cb3a748afc268d95917796f1205be6c8d` |
| `audit_mecanisme_v1.py` | audit | `5762c7a4b0f9404171329139fc95480efb00db19ef311b5c087a996adc6497a8` |
| `horodater_v1.py` | horodatage par `date -u` | `79ea1845209a8dc0633b55d334ffbf4d50058333c342e0725d6163252731e2b6` |

Chaque fichier a son compagnon `.sha256` ; celui de ce rapport est `trancher-recombinaison-v1.md.sha256`.

<<<FIN R2>>>

<<<DÉBUT T — rétrodiction sur les métadonnées d'arXiv 2003-2016 (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/retrodiction-swanson/retrodiction-swanson-v1.md`, sha256 `057ef8a5314fba92b305a2e71fc4008a228aecd1e2a22598c2b85b64e362783b`)>>>

# Rétrodiction sur arXiv : la marche « à la Swanson » relie-t-elle mieux les champs éloignés ? — v1

Exécution du brief `BRIEF-retrodiction-swanson-v1.md` (empreinte `3b83d113…c7c0e4`) selon le préenregistrement
`preenregistrement-retrodiction-v1.md` (empreinte `7a4868aa48cfff5eb48937b0a1a99647fc9968c44c1fe8a7bb8047629b3c91eb`,
scellé à 20:13:35 UTC, avant tout calcul). Sous-agent neuf de la lignée conv-audit, 26 octobre 2026.

## Décisions (figées par le brief, découpage principal : avant 2003-2010, après 2011-2016)

- **D1 — réfutée.** Précision à 10 000 : marche à la Swanson (S) **9,83 %** [9,22 ; 10,44] contre tirage stratifié (ST)
  **0,22 %** [0,14 ; 0,32] ; écart **+9,61 points** [+8,98 ; +10,23], sous le seuil de 12 points. La marche n'est pas
  retenue comme règle de tirage de la version 0.
- **D2 — pas de contribution.** Meilleure méthode classique = **allocation de ressources (RA) : 10,65 %**
  [10,08 ; 11,23]. Écart S − RA = **−0,82 point** [−1,43 ; −0,25] : S est *en dessous*, pas 2 points au-dessus ; les
  intervalles se recouvrent. Selon la règle, on adopte l'allocation de ressources **sous son nom**, sans revendication.
- Contrôles : permutations des issues réussies (toutes les méthodes au taux de base) ; placebo 2003-2006 / 2007-2010
  **stable** (même ordre des cinq méthodes à score, tau de Kendall = 1 sur les sept) ; essais d'absence de fuite
  temporelle réussis (cas sain, artefact pris, référence lente à 4e−15 près).

Les nombres (intervalles à 95 % par rééchantillonnage des paires, 1 000 tirages) viennent de
`resultats/issues-v1.json` et `resultats/synthese-v1.json` (empreintes dans la table des sources, fin du document).

## Résultats du découpage principal

1 000 000 de paires candidates, 2 752 positives : **taux de base 0,2752 %** [0,2651 ; 0,2857] (Wilson).

| méthode | précision à 1 000 (%) | précision à 10 000 (%) | précision moyenne (%) | aire sous la courbe de fonctionnement du récepteur |
|---|---|---|---|---|
| S, marche à la Swanson (moyenne des deux sens) | 19,20 [16,90 ; 21,80] | **9,83** [9,22 ; 10,44] | 9,05 [8,38 ; 10,01] | **0,9595** [0,9572 ; 0,9618] |
| AA, Adamic-Adar | 24,20 [21,50 ; 26,80] | 9,05 [8,52 ; 9,65] | 9,47 [8,59 ; 10,52] | 0,9419 [0,9384 ; 0,9455] |
| RA, allocation de ressources | **28,40** [25,70 ; 31,30] | **10,65** [10,08 ; 11,23] | **12,16** [11,14 ; 13,36] | 0,9574 [0,9547 ; 0,9602] |
| CN, voisins communs | 23,70 [21,10 ; 26,30] | 8,87 [8,33 ; 9,45] | 9,16 [8,29 ; 10,18] | 0,9396 [0,9361 ; 0,9432] |
| PA, attachement préférentiel | 11,40 [9,60 ; 13,40] | 5,62 [5,19 ; 6,07] | 3,79 [3,45 ; 4,25] | 0,8897 [0,8840 ; 0,8951] |
| ST, tirage stratifié | 0,30 [0,00 ; 0,60] | 0,22 [0,14 ; 0,32] | 0,27 [0,26 ; 0,29] | 0,4975 [0,4868 ; 0,5082] |
| U, tirage uniforme | 0,30 [0,00 ; 0,70] | 0,25 [0,16 ; 0,36] | 0,27 [0,26 ; 0,29] | 0,4964 [0,4861 ; 0,5073] |
| S(A→C), sens unique (secondaire) | 18,20 [15,90 ; 20,60] | 7,98 [7,46 ; 8,56] | 6,52 [5,94 ; 7,34] | 0,9176 [0,9133 ; 0,9220] |
| S(C→A), sens unique (secondaire) | 9,80 [7,90 ; 11,60] | 4,11 [3,69 ; 4,49] | 2,67 [2,37 ; 3,07] | 0,8768 [0,8720 ; 0,8816] |

Écarts de précision à 10 000, appariés (points ; dans les deux sens) : S − ST **+9,61** [+8,98 ; +10,23] ;
S − RA **−0,82** [−1,43 ; −0,25] ; S − AA +0,78 [+0,12 ; +1,42] ; S − CN +0,96 [+0,30 ; +1,59] ; S − PA +4,21
[+3,69 ; +4,76].

Lecture, sans changer les décisions :
- S bat Adamic-Adar, voisins communs et attachement préférentiel à 10 000, de moins d'un point face aux deux premiers ;
  elle perd contre l'allocation de ressources à 10 000, et plus nettement en tête de liste (précision à 1 000 :
  19,2 % contre 28,4 %, la plus faible des quatre méthodes de cooccurrence) et en précision moyenne (9,05 % contre 12,16 %).
- Seule mesure où S devance RA : l'aire sous la courbe (0,9595 contre 0,9574), intervalles qui se recouvrent. S
  ordonne un peu mieux le gros de la liste, moins bien la tête — or c'est la tête que mesure la décision.
- Le choix préenregistré de la moyenne des deux sens n'a pas desservi S : chacun des deux sens seuls fait pire
  (7,98 % et 4,11 %).
- L'avantage de toutes les méthodes sur ST ne tient pas au choix des strates : la précision qu'aurait la tête de liste
  de chaque méthode avec sa seule composition par strates est de 0,23 à 0,30 % (audit n° 2, non préenregistré).

Taux de base par paire de champs (Wilson ; aucune strate ne touche « stat », qui n'a aucun terme candidat) :

| strate | paires candidates N_s | paires tirées | taux de base (%) |
|---|---|---|---|
| math – cs | 2 469 001 | 17 489 | 0,36 [0,28 ; 0,46] |
| math – physique | 112 832 560 | 799 241 | 0,17 [0,16 ; 0,18] |
| math – q-bio | 258 547 | 1 831 | 0,11 [0,03 ; 0,40] |
| math – q-fin | 6 834 | 49 | 0,00 [0,00 ; 7,27] |
| cs – physique | 23 113 888 | 163 726 | 0,76 [0,72 ; 0,80] |
| cs – q-bio | 52 064 | 369 | 0,00 [0,00 ; 1,03] |
| cs – q-fin | 1 436 | 10 | 0,00 [0,00 ; 27,75] |
| physique – q-bio | 2 374 883 | 16 822 | 0,47 [0,38 ; 0,58] |
| physique – q-fin | 65 247 | 462 | 0,00 [0,00 ; 0,82] |
| q-bio – q-fin | 150 | 1 | 0,00 [0,00 ; 79,35] |
| les cinq strates avec stat | 0 | 0 | — |

Strate « dominée par les termes passe-partout » (plus de la moitié de la masse de S par les 432 termes du 1 % le plus
fréquent) : **494 paires, une seule positive**. Précision à 1 000 et à 10 000 non définies (strate plus petite que k,
règle préenregistrée) ; la précision moyenne et l'aire y reposent sur une seule positive : aucune lecture possible.

## Contrôles

**(a) Issues permutées.** 20 permutations par découpage ; toutes les méthodes restent au taux de base (critère :
moins de 4 erreurs-types). Principal : précision à 10 000 moyenne de 0,27 à 0,29 % pour un taux de base de 0,2752 %,
écarts de −0,61 à +1,43 erreur-type ; aire de 0,4965 à 0,5014, écart le plus grand −2,81 erreurs-types (S). Placebo :
écarts tous sous 1,9 erreur-type. Comme les écarts d'aire au découpage principal penchaient tous du même côté (−1,85 à
−2,81 pour les méthodes à score), je les ai audités (non préenregistré) : 200 permutations de plus, autre graine →
aire à −0,18 à −1,21 erreur-type, écart-type observé 0,0050 à 0,0051 contre 0,0055 en théorie ; précision à 10 000 à
−1,4 à −2,3 erreurs-types, même signe pour toutes. Sous permutation, l'espérance est exactement le taux de base et 0,5 ;
ces écarts de même signe viennent de permutations communes et de têtes de liste qui se recouvrent (fluctuation
corrélée, moins de 0,01 point en valeur absolue), pas d'une fuite.

**(b) Placebo 2003-2006 / 2007-2010** (chaîne entière refaite : 180 284 documents d'avant, 248 918 d'après, 19 975 termes,
1 000 000 de paires, taux de base 0,528 % [0,514 ; 0,542]). Précision à 10 000 : RA 16,17 % [15,38 ; 16,83] > S 13,67 %
[13,03 ; 14,43] > AA 12,65 % > CN 12,29 % > PA 8,75 % > U 0,55 % ≈ ST 0,54 %. **Même ordre qu'au découpage principal :
« stable »**, tau de Kendall = 1,0. Écarts : S − RA −2,50 [−3,24 ; −1,57] ; S − ST **+13,13** [+12,47 ; +13,83].
Au placebo, la règle D1 aurait **retenu** S ; elle la réfute au découpage principal. Le préenregistrement fait décider
le seul découpage principal ; ce basculement est une réserve sur le seuil, traitée plus bas.

**(c) Absence de fuite temporelle.**
- Essai synthétique avec la chaîne même du calcul réel (`code/essais_v1.py`, `resultats/essais-v1.json`) : documents
  d'après mélangés, retirés, ou bourrés des paires candidates → vocabulaire, champs, candidats, paires tirées et scores
  identiques au bit près, issues changées ; un document d'avant modifié → tout change ; un calculateur volontairement
  fuyant est pris par la garde ; calcul à deux processus identique au calcul à un processus.
- Données réelles (`resultats/scores-bilan-v1.json`) : matrices d'avant limitées à 2003-2010 (2003-2006 au placebo) ;
  les fréquences d'avant de la matrice sont égales à celles de la passe d'extraction ; 1 000 paires recalculées par une
  implémentation lente sur les seuls documents d'avant (écart relatif maximal 4,0e−15, 3,3e−15 au placebo) ; degrés et
  normalisations r exacts sur 300 termes ; aucune des 2 000 000 de paires tirées ne cooccurre avant.
- Chronologie : scores écrits et empreintés à 20:30:32 et 20:32:31 UTC ; issues calculées à partir de 20:33:11 UTC.

## Description du corpus et du tirage

- 999 260 lignes, 999 213 articles (37 identifiants en double réduits). Avant : 429 202 ; après : 570 011.
- Vocabulaire : 43 162 termes (dont 27 583 bigrammes) de fréquence documentaire 50 à 21 460 ; 48,8 termes de vocabulaire
  par document d'avant ; 2 688 668 termes distincts avant (risque de conflit d'empreinte borné par 2e−7 ; aucun conflit
  touchant le vocabulaire).
- Part des documents d'avant : physique 73,9 %, math 19,4 %, cs 4,9 %, q-bio 1,1 %, stat 0,44 %, q-fin 0,30 %.
- Termes candidats (spécifiques, fréquence 50 à 3 000) : physique 33 078, math 3 497, cs 722, q-bio 75, q-fin 2, stat 0.
  141 174 610 paires candidates ; tirage proportionnel → 80 % de paires math – physique, 16 % cs – physique.
- Toutes les paires tirées ont au moins un voisin commun (K > 0).

## Ce que le test ne dit pas

- **Des termes ne sont pas des concepts.** Les unigrammes et bigrammes de titres et de résumés mêlent synonymes,
  polysémies et mots de discours. Les têtes de liste le montrent : celle de S ressemble à des ponts de physique
  mathématique (« toric variety — witten », « hopf — supergroups », « projective curves — calabi yau ») ; celle de RA
  est faite de mots courants (« ball — consistently », « users — shifts », « resp — thought », « proofs — vice »), qui
  cooccurrent pourtant plus souvent ensuite. L'issue mesurée est la **cooccurrence lexicale future**, pas une découverte
  féconde. Cette impression vient de 15 exemples et ne sert pas à racheter S.
- **arXiv n'est pas toute la littérature** : physique surreprésentée (74 % des documents d'avant), statistique et finance
  quantitative presque absentes avant 2011, pas de biomédecine (le terrain d'origine de Swanson).
- **« Champs éloignés » se réduit ici, pour l'essentiel, à math – physique et cs – physique**, deux champs reliés par la
  physique mathématique. Le test ne dit rien des champs vraiment lointains.
- **Le régime « termes passe-partout » n'est pas testé** : la strate est vide en pratique (494 paires sur 1 000 000, une
  positive). Le +17 points des mondes synthétiques n'est donc ni confirmé ni réfuté.
- Précision à 10 000 sur un échantillon d'un million = précision du premier centile de la population (≈ 1,4 million de
  paires sur 141 millions). Ce n'est pas la précision des 10 000 meilleures paires de la population entière.
- Une seule fenêtre (2011-2016), un seul seuil d'issue (3 documents), une seule graine par tâche, un seul corpus.
- La précision à 10 000 seule décide. S a la meilleure aire mais une tête plus faible.
- S et RA choisissent des têtes presque disjointes (2 378 paires communes sur 10 000), avec des taux de réussite voisins
  (983 et 1 065 positives). Leur combinaison est une **question ouverte**, à préenregistrer ; elle n'est pas testée ici
  et rien ne s'en revendique.

## Points du brief que je crois mal posés (dits à part ; décisions inchangées)

1. **Spécificité non normalisée par la taille des champs.** Avec 74 % des documents d'avant en physique, un mot réparti
   au hasard a 74 % de ses documents en physique : il devient « spécifique » de la physique (« consistently »,
   « thought », « apparently »…). La statistique n'a aucun terme spécifique. Une spécificité relative à la part du champ
   serait plus fidèle à l'idée de « champs éloignés ».
2. **La strate « passe-partout » est vide par construction.** Le vocabulaire exclut les termes de plus de 5 % des
   documents (les vrais termes passe-partout). De plus, P(C|B) = n(B,C)/r(B) donne peu de masse aux intermédiaires
   fréquents : par le 1 % le plus fréquent passent 22 % de la masse de S en médiane, 38 % au 99e centile. Le motif
   principal du test (le +17 points) ne peut donc pas être éprouvé avec ces définitions.
3. **Le seuil de D1 est absolu alors que ST vaut le taux de base.** Le verdict dépend du taux de base : 9,61 points à
   0,28 % (réfutée) et 13,13 points à 0,53 % (placebo, retenue), pour un même ordre des méthodes. En relatif, S
   multiplie le taux de base par 36 (principal) et 26 (placebo). Un seuil relatif, ou calé sur le taux de base, voyagerait
   mieux. L'allocation de ressources, adoptée par D2, ne passerait pas non plus la barre de D1 (+10,43 points).
4. **Le sens de la marche n'était pas fixé.** Le préenregistrement a tranché pour la moyenne des deux sens, qui
   l'emporte sur chaque sens seul ; aucune décision n'en dépend.
5. **« Paires possibles de chaque strate » était ambigu.** Lu comme le nombre exact de paires candidates. Les paires
   cooccurrentes écartées font de 0 à 4,3 % des paires |T_f|·|T_g| selon la strate (2,5 % pour math – physique) :
   l'autre lecture aurait à peine changé l'allocation.

## Écarts au préenregistrement

Aucun sur les définitions, les seuils, les périodes, le vocabulaire ou les décisions. Ajouts **non préenregistrés**,
signalés comme tels, sans effet sur les décisions :
- `resultats/audit-v1.json` : 200 permutations de plus ; parts des groupes ; masse de S par le 1 % le plus fréquent ;
  recouvrement des têtes de liste ; fréquences des termes en tête.
- `resultats/audit-strates-v1.json` : composition par strates des 10 000 premiers de chaque méthode.

## Sources (chemins sous `sortie/`, empreintes SHA-256)

| fichier | empreinte |
|---|---|
| `preenregistrement-retrodiction-v1.md` | `7a4868aa48cfff5eb48937b0a1a99647fc9968c44c1fe8a7bb8047629b3c91eb` |
| `resultats/synthese-v1.json` (D1, D2, stabilité) | `345e9a4e955f4f41baa24e4983379b0e46d12893f0bd62ab9cf4ed14c50d1ce8` |
| `resultats/issues-v1.json` (mesures, intervalles, permutations, strates) | `dd16d06e6feb59d85f38503cf4eba47fd9b134a0c13059664dd8e69fdc76373e` |
| `resultats/scores-bilan-v1.json` (corpus, vocabulaire, strates, contrôle de référence) | `54463b67fd7c13368b80b34d7926eab1feceeca95f11e4833c912217f4c0c371` |
| `resultats/essais-v1.json` (essais automatiques) | `b9c5b7cafb6e9dca0c2237877df58d358621ef6cb08097af83d714f3a94deb28` |
| `resultats/audit-v1.json` (non préenregistré) | `7f19db8caf136581f16f7b74cbedf14d69140dda2867ad8baf531ca8a387ac26` |
| `resultats/audit-strates-v1.json` (non préenregistré) | `e0700fbaf621e753b5f3a4ed0c6e2470bfffa681b47bb6c5e80535f3c1b4aa8b` |
| `resultats/scores-principal-v1.npz` (scores par paire) | `0850c7e33011fc89e94dd3f4cfd83a8ed8ee47e0ef8871035b5a6814bab92b0d` |
| `resultats/issues-principal-v1.npz` (issues par paire) | `31fbb60da3739cdbd7e7076f22c96c7af486baa9989afb202e5f6e481b1077ab` |
| `resultats/vocabulaire-principal-v1.npz` | `06c065948f0235711492cf58694d9687e50e326f9df20abf7ce781e2f237bff4` |
| `resultats/scores-placebo-v1.npz` | `173684c34fd58162a45f35f65b58393d345b9ab6f2313d1fbb3ff187412c2b49` |
| `resultats/issues-placebo-v1.npz` | `700db17558fc94406f68acf097f17308e32a1ea7a98ac0550dcddd04ff52525e` |
| `resultats/vocabulaire-placebo-v1.npz` | `c73f0c98e588ceb60907b4bd213be08d644b7ff4378bfe6672b33c9663be824d` |

Code (`code/`, chaque fichier a son compagnon `.sha256`) : `termes_v1.py`, `corpus_v1.py`, `chaine_v1.py`,
`mesures_v1.py`, `essais_v1.py`, `lancer_v1.py` (étapes `essais`, `scores`, `issues`, `synthese`), `tables_rapport_v1.py`,
`audit_v1.py`, `audit_strates_v1.py`. Empreintes, versions (Python 3.13.17, numpy 2.3.4, scipy 1.16.3, duckdb 1.4.1),
graines (`SeedSequence(20261026)`, clés d'engendrement par tâche) et heures sont consignées dans chaque fichier JSON et
dans `manifeste-v1.json`. Journaux : `travail/journal-*-v1.txt`. Matrices d'après intermédiaires : `travail/apres-*-v1.npz`.

Horodatage : écrit le 2026-10-26 20:52:23 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).

<<<FIN T>>>

<<<DÉBUT C — conception du pôle (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/conception-pole-scientifique-v1.md`, sha256 `a4f94148c9c55b76f208edecd7220b51a8e21ca69f52e50c7f2abb6484b81b52`)>>>

# Conception du pôle « scientifique automatique » : des agents qui expérimentent, éliminent et recombinent — v1

De : conv-audit, le 26 octobre 2026 (heure au pied). Mots de Lazar (heure de Paris) : 18:30 « des agents qui font leurs
propres expériences sur les hypothèses formulées et les éliminent au fur et à mesure, genre darwinisme, et après
recombinent celles qui ont survécu sur le mode bisociatif proposé par Gemini » ; 18:43 « avance en priorité la conception
de l'organisme avec agents lançables qui font des expériences et testent les hypothèses, si on le construit nous-mêmes à
partir de la dernière version ou si on en utilise un déjà disponible ». Le choix du moteur est au collisionneur
(GO-2026-10-26-06, R-524) puis à Lazar ; cette pièce fixe ce qui **ne dépend pas** du moteur, décrit les deux moteurs, et
démarre une version 0 tout de suite. Régime exploratoire (R-522) ; rien d'opposable.

## 1. Le cœur, indépendant du moteur

**La fiche d'hypothèse** (un fichier JSON par hypothèse, empreinté) : identifiant ; énoncé en une phrase ; **prédiction
signée et chiffrée** ; métrique ; **nul** (comment l'absence d'effet est simulée ou mesurée) ; **seuil qui peut échouer** ;
sévérité attendue (probabilité, sous le nul, de passer le seuil) ; coût borné ; protocole (plan ou code) ; parents (pour la
recombinaison) ; domaines ; opérateurs ; contraintes de validité (pour le filtre de compatibilité) ; statut.

**Le cycle d'une génération** :
1. **Gel du test** : la fiche est empreintée **avant** l'expérience. C'est la seule « formalité » gardée, automatique, et
   c'est elle qui rend l'élimination signifiante : un test choisi après coup ne réfute rien.
2. **Expérimentateur** (un agent par fiche, en parallèle) : dans un bac à sable, il écrit et exécute son code, et rend le
   verdict, les nombres, les artefacts.
3. **Vérificateur** (un agent neuf, d'une autre famille de modèles que l'expérimentateur) : il rejoue le code, vérifie que
   le test exécuté est le test gelé, que le verdict suit le seuil, et cherche les raccourcis (code qui contourne la mesure,
   nul trop faible, données touchées). Un verdict non vérifié ne compte pas.
4. **Sélection** : réfutée → éliminée (et archivée) ; survivante → aptitude = **sévérité du test survécu**
   (−log de la probabilité de survie sous le nul), jamais le signe ni l'ampleur du résultat ; indécise → un test plus
   puissant, ou retirée après deux essais.
5. **Recombinaison bisociative** des survivantes : tirage diversifié par domaine (noyau de similarité de domaine dans la
   répulsion, pertinence dans la qualité — forme corrigée, relecture `9a791017…`, brique 2), pont par un opérateur commun,
   **filtre de compatibilité des contraintes** (la bonne idée du rapport de Gemini) ; la fiche fille doit **prédire plus
   que ses parents** (contenu empirique accru), sinon elle n'entre pas dans la population.
6. **Archive complète**, éliminées comprises (contre le biais du survivant, et pour mesurer le pôle lui-même).

**Les garde-fous (ce qui fait que le pôle produit des résultats solides et non des résultats flatteurs)** :
- **Témoins plantés** à chaque génération : des fiches dont la vérité est connue (vraies et fausses) ; le taux auquel le
  pôle élimine les fausses et garde les vraies **est sa mesure de qualité**. Sans eux, un pôle qui garde tout et un pôle
  qui élimine tout sont indiscernables.
- L'aptitude ne récompense jamais un résultat positif (R3) ; une hypothèse qui ne prédit rien a une sévérité nulle et ne
  survit à rien d'utile.
- **Évaluation scellée** avant toute revendication : une part des simulations ou des données que les expérimentateurs
  n'ont jamais vue ; un résultat « mémorable » n'en sort qu'après cette évaluation.
- **Bac à sable** : aucune clé, aucun réseau (hors moissonnage borné du noyau), écriture dans le seul dossier de
  l'expérience, temps et mémoire bornés. Le budget est fixé par génération.
- **Réécriture de soi** : le pôle peut proposer des modifications de son propre code, qui sont elles-mêmes des fiches
  (« la modification X augmente le taux de bonne élimination des témoins »), testées de la même façon et appliquées après
  survie et essais ; **le noyau, ses gardes et ses bornes ne sont jamais réécrits par le pôle**.

## 2. Les deux moteurs (le collisionneur compare ; Lazar décide)

| | (A) notre organisme, à partir de la dernière version | (B) un moteur de la littérature |
|---|---|---|
| ce qui existe | castes contradictoires (formuler, croiser, sonder, critiquer, arbitrer), moissonnage borné, mémoire spectrale, archive, noyau à bornes et clés protégées, questions servies | ShinkaEvolve, OpenEvolve : population, évaluation parallèle, îles, archive, juge de nouveauté (évolution de programmes) ; Agentic Scientist v3 : d'une tâche à des expériences, des ablations et une **évaluation finale scellée** |
| ce qui manque | un **exécuteur d'expériences** en bac à sable dans le noyau ; les rôles expérimentateur et vérificateur ; la réécriture de soi (restreinte par C-17 à trois paramètres : à lever dans le bac à sable) | la fiche d'hypothèse (le « programme » devient un script d'expérience et sa prédiction gelée ; l'évaluateur, l'exécution plus le vérificateur), les témoins, la recombinaison bisociative ; agents à pleins droits dans Docker, clés montées (avertissement de leur propre README) |
| coût du premier résultat | plusieurs jours de conception et d'essais du noyau | une instance avec Docker et des clés (chez session-depot), un jour d'adaptation |
| maîtrise | totale (notre code, nos gardes) | partielle (code tiers, mises à jour) |

Une voie **hybride (C)** est probable : le cœur du § 1 (fiches, sévérité, témoins, recombinaison) au-dessus d'un moteur
d'exécution emprunté, ou au-dessus du noyau étendu.

## 3. Version 0, tout de suite, dans la session de conv-audit

- **Orchestrateur** : conv-audit. **Expérimentateurs** : des sous-agents sur processeur, chacun dans un dossier isolé
  (aucune clé, aucun réseau, aucun `git`). **Vérificateur** : un sous-agent neuf d'une autre famille. **Recombinaison** :
  un sous-agent sur les survivantes.
- **Génération 0** (en cours) : les affirmations du rapport de méta-conception de Gemini, testées par deux expérimentateurs
  (brique 1 ; briques 2 à 4), verdict « survit / éliminée / indécise » par affirmation.
- **Génération 1** : vérification des verdicts, puis recombinaison des survivantes en fiches filles, plus deux témoins
  plantés ; un expérimentateur par fiche fille.
- Ce que la version 0 mesure pour le choix du moteur : le coût par fiche, le délai par génération, et le taux de bonne
  élimination des témoins — un point de comparaison empirique pour (A), (B) ou (C).

Horodatage : écrit le 2026-10-26 17:45:16 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).

<<<FIN C>>>
