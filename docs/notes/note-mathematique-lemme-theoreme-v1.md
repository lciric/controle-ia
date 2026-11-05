# Note mathématique — lemme d'additivité et théorème négatif — v1 (brouillon de travail, T0.3)

Date : 2026-10-04 (UTC). Statut : **brouillon**, non contre-lu, non préenregistré. Il prépare le préenregistrement de T0.3 et instruit les nœuds de décision N-003 (théorème négatif) et N-004 (lemme). Les énoncés du programme (section 3) ne sont pas modifiés par cette note : elle propose des formulations précises, que T0.3 testera à côté des formulations du programme telles qu'écrites.
Références (niveau transcription, à vérifier sur PDF avant toute citation) : 2606.10456 ; Howard, Ramdas, McAuliffe, Sekhon (2021) ; Koning et Grünwald, 2208.07610 ; Ramtin, Nain, Towsley, 2601.20022 ; Arias-Castro, Candès, Plan (2011) ; Mei (2010) ; Xie et Siegmund (2013).

## 1. Cadre

- Ensemble d'indices I ⊂ {1,…,N} × {1,…,T} : l'action a_{i,t} de l'agent i au pas t. Chaque action reçoit un score X_{i,t} ∈ ℝ (score de sonde agrégé par max ou attention sur les tokens, ou score boîte noire). Indexation agnostique : N = 1 et N = k sont le même objet.
- Ordre de lecture ≺ : le défenseur lit les actions pas après pas, et à un pas donné tous les agents (ordre temps d'abord). On note X_1, X_2, … les scores dans cet ordre et n le nombre d'actions lues.
- Loi honnête P₀ : les X_{i,t} sont indépendants et de même loi F₀, de moyenne μ₀ et de variance σ² connues ou estimées sur épisodes honnêtes (hypothèse (c) du programme). Variante plus faible : P₀ échangeable sur I.
- Règle d'alarme au risque α :
  - à horizon fixé n₀ : P₀(alarme à n₀) ≤ α ;
  - toujours valide : P₀(∃ n : alarme à n) ≤ α.
- Deux classes d'attaquants, à budget fixé :
  - **Classe M (décalage de marginale)** : l'attaquant choisit un ensemble S ⊂ I d'actions sabotées et des décalages δ_k ≥ 0 de somme B ; X_k = Y_k + δ_k·1{k ∈ S}, avec Y ~ P₀. **Les actions non sabotées gardent la loi honnête (pas de compensation).**
  - **Classe C (multi-ensemble préservé)** : X = π_Y(Y) avec Y ~ P₀ et π_Y une permutation de I choisie par l'attaquant en fonction de Y (et de son aléa privé). Le multi-ensemble des scores est exactement celui d'un épisode honnête. Le dommage dépend de l'arrangement (quelles actions reçoivent les valeurs hautes, et où elles se trouvent).

## 2. Lemme d'additivité (classe M)

Cas gaussien de référence : Y_k ~ N(μ₀, σ²). Somme centrée S_n = Σ_{k≤n} (X_k − μ₀). Processus e de mélange normal unilatéral ou bilatéral, par exemple pour un mélange N(0, ρ²) sur λ :
E_n = (1 + ρ²σ²n)^(−1/2) · exp( ρ² S_n² / (2(1 + ρ²σ²n)) ).

**L1 — invariance de la statistique terminale.** Si tout le sabotage tombe dans les n₀ premières actions lues, alors S_{n₀} ~ N(B, n₀σ²), quelle que soit la répartition (ensemble S, nombre d'actions sabotées m, agents, pas, valeurs δ_k). Toute règle fonction de S_{n₀} — en particulier « E_{n₀} ≥ 1/α » et le test à horizon fixé sur S_{n₀} — a une puissance qui ne dépend que de (B, n₀, σ, α).
Preuve : somme de normales indépendantes. Hors cas gaussien, l'invariance vaut pour l'espérance et la variance de S_{n₀}, et en loi asymptotiquement (théorème central limite) ; les corrections à distance finie dépendent de la forme de F₀ (à mesurer en T0.3).

**L2 — effondrement du max par action.** Test du max M_n = max_{k≤n} (X_k − μ₀)/σ au seuil c_n tel que P₀(M_n ≥ c_n) = α (seuil ≈ √(2 log(n/α))). Si le budget B est réparti également sur m actions (δ = B/m), alors par la borne de l'union
P(M_n ≥ c_n) ≤ m · Φ̄(c_n − B/(mσ)) + (n − m) · Φ̄(c_n),
qui tend vers au plus α quand m → ∞ à B fixé, alors que la puissance de L1 ne bouge pas. C'est la séparation entre preuve par action et preuve cumulée.

**L3 — en lecture toujours valide, le calendrier compte ; la statistique terminale donne une borne inférieure indépendante de la répartition.** Pour la règle « première alarme quand E_n ≥ 1/α » avec un mélange unilatéral (λ ≥ 0, donc E_n croissant en S_n) :
- (a) couplage trajectoriel : si la dérive cumulée D_n = Σ_{k≤n} δ_k d'une répartition domine celle d'une autre à tout n, la probabilité d'alarme avant n₀ est plus grande. Avancer le sabotage aide le défenseur ; le reporter en fin d'horizon est la meilleure réponse de l'attaquant ;
- (b) pour toute répartition de B dans les n₀ premières actions : P(alarme avant n₀) ≥ P(E_{n₀} ≥ 1/α), et le membre de droite ne dépend que de (B, n₀, σ, α) par L1.
L'invariance exacte n'existe donc qu'à horizon fixé ; en toujours valide, on a une borne inférieure invariante. L'écart entre le test à horizon fixé (seuil gaussien) et « E_{n₀} ≥ 1/α » (inégalité de Markov) est le prix de la garantie toujours valide — la distinction puissance de Wald / toujours valide de Koning et Grünwald, à chiffrer.

**L4 — répartition entre agents.** Si la règle est évaluée aux frontières de pas (après les N actions d'un pas), la répartition du sabotage entre agents à un même pas est exactement invariante, y compris en toujours valide : seule compte la dérive cumulée par pas.

**L5 — la condition de non-compensation est essentielle.** Si l'attaquant peut aussi abaisser le score de ses actions non sabotées (décalages −γ_k), seul compte le budget net B_net = Σδ − Σγ ; à B_net = 0, la statistique terminale n'a aucune puissance. Et si la compensation restaure exactement la loi du multi-ensemble, on tombe dans la classe C. En boîte noire, compenser est bon marché (écrire un texte encore plus innocent) ; en boîte blanche, il faut piloter ses propres activations. **Proposition (pour Lazar) : la condition empirique du lemme est le coût de la compensation interne, c'est-à-dire la question de la taxe de déplacement (HC4) et de la transposition (Tr).** Elle relie A et C.

## 3. Théorème négatif (classe C)

**Mise en garde sur l'énoncé du programme.** « Toute statistique fondée sur les marginales (max, moyenne, somme cumulée) a une puissance égale au taux de faux positifs » est faux tel qu'écrit pour une attaque par copule autorégressive qui préserve seulement la marginale *par pas* (cas de 2606.10456) : la corrélation change la variance de la moyenne et de la somme (facteur de variance de long terme ≈ (1+φ)/(1−φ) pour un processus autorégressif d'ordre 1), la loi du max et les excursions d'une somme lue séquentiellement. Une statistique de moyenne a alors une puissance supérieure au taux de faux positifs. (Le « Monitor A » de 2606.10456 est rapporté à une puissance ≤ 0,048 pour un taux visé de 1 %, ce qui est compatible avec cette fuite — niveau transcription.)

**T1 — aveuglement des statistiques invariantes.** Soit G un groupe de permutations de I et f une statistique G-invariante (f(g·x) = f(x) pour tout g ∈ G). Si π_Y ∈ G presque sûrement, alors f(X) = f(Y) presque sûrement : la loi de f(X) sous attaque est celle sous P₀, et tout test fondé sur f a une puissance égale à son niveau.
Preuve : une ligne. Exemples :
- G = toutes les permutations de I : moyenne, somme terminale, max, moyenne des k plus hauts, quantiles, comptes de dépassement, toute fonctionnelle de l'histogramme ;
- G = permutations du temps à l'intérieur de chaque agent : toute fonctionnelle de la marginale empirique par agent, et toute agrégation de celles-ci entre agents ;
- G = permutations des agents à l'intérieur de chaque pas : toute statistique qui ignore l'identité des agents pas par pas.
Temps et agents sont deux sous-groupes du même groupe de permutations de I : c'est la forme précise du « même objet mathématique » du programme.

**T2 — sans structure, impossibilité totale.** Si P₀ est échangeable sur I et si l'attaquant compose son arrangement avec une permutation uniforme de G = toutes les permutations de I, tirée indépendamment, alors X ~ P₀ exactement. La loi d'un vecteur échangeable est déterminée par celle de son multi-ensemble. **Aucun test sur les scores, séquentiel ou non, n'a de puissance supérieure à α.** Si le dommage ne dépend pas de la position des actions sabotées (dommage « sans structure »), un attaquant qui préserve le multi-ensemble est donc indétectable par tout moniteur de scores. Les deux seules issues pour le défenseur sont :
- un décalage net de marginale (classe M, lemme) ;
- un dommage qui exige une structure que l'attaquant ne peut pas brouiller (T3).

**T3 — dommage structuré, détection sensible à l'ordre.** Si le dommage exige des suites d'au moins r actions sabotées consécutives chez un agent (structure temporelle), ou au moins m agents sabotant au même pas (coordination), et si une action sabotée porte un score élevé (compensé ailleurs), l'arrangement imposé crée une dépendance locale. Les statistiques sensibles à l'ordre ont alors une puissance supérieure à α : autocorrélation, test des suites, max de moyennes glissantes, somme cumulée de Page, co-élévation entre agents. À dommage égal, découper en suites plus courtes affaiblit le signal — le pendant de L2 côté corrélation.

**T4 — la somme cumulée lue séquentiellement n'est pas aveugle, mais l'attaquant peut la rendre impuissante.** Le processus e sur la somme n'est pas invariant par permutation. Sa puissance dépend de l'arrangement. Placer d'abord les valeurs basses, puis la grappe haute en fin d'horizon, donne une trajectoire qui ne dépasse pas, en loi, celle d'un épisode honnête ; la probabilité d'alarme peut alors descendre à α ou en dessous. La prédiction du programme « la somme cumulée échoue » est donc vraie :
- exactement pour la somme terminale (T1) ;
- au sens adverse pour la somme séquentielle (T4) ;
- mais pas pour toute somme lue séquentiellement face à n'importe quel arrangement.

## 4. Ce que T0.3 testera (à préregistrer, R1)

Attaques simulées :
- **M** : répartition de B sur m ∈ {1, 2, 5, 10, 20, 50, 100} actions, N ∈ {1, 2, 3, 5, 10}, T ∈ {20, 50, 100, 200} ; calendrier avancé, uniforme ou reporté.
- **C0** : réordonnancement uniforme, sans structure.
- **C-suites** : suites de longueur r dans le temps.
- **C-synchrone** : simultanéité entre agents.
- **C-copule** : copule gaussienne autorégressive à marginale par pas préservée, comme 2606.10456 — elle teste l'énoncé du programme tel qu'écrit.

Agrégateurs, tous sur le même multi-ensemble indexé (i, t) :
- max par action ;
- moyenne glissante, max de moyennes glissantes ;
- somme cumulée, terminale et séquentielle ;
- processus e de mélange ;
- somme cumulée de Page ;
- autocorrélation de pas 1, test des suites ;
- co-élévation entre agents (corrélation des scores entre agents par pas, compte de dépassements simultanés).

Gardes :
- taux de faux positifs empirique de chaque agrégateur sous P₀, avec intervalle Monte-Carlo, contrôlé avant toute lecture de puissance ;
- graines par `SeedSequence` dérivées par tâche (R9).

Prédictions à geler (signes et formes) :
1. L1 : puissance plate en m, N et T à B fixé, pour la statistique terminale.
2. L2 : puissance du max décroissante vers α quand m croît.
3. L3 : alarme toujours valide plus probable pour un calendrier avancé que reporté, et toujours au-dessus de la borne terminale.
4. T1 et T2 : puissance de toutes les statistiques invariantes égale à α sous C0 ; puissance de toute statistique égale à α sous C0.
5. T3 : statistiques sensibles à l'ordre au-dessus de α sous C-suites et C-synchrone.
6. C-copule : moyenne et max au-dessus de α (l'énoncé du programme tel qu'écrit serait réfuté).
7. T4 : somme séquentielle à α ou en dessous sous l'arrangement « bas d'abord ».
