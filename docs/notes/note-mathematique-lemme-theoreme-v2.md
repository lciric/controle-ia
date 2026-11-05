# Note mathématique — lemme d'additivité et théorème négatif — v2 (T0.3)

Date : 2026-10-04 (UTC). Remplace la v1 (`note-mathematique-lemme-theoreme-v1.md`, empreinte 277ffc9b…, archivée sans modification).
Intègre la contre-vérification adverse d'un sous-agent neuf : `contre-verification-note-v1.md` (empreinte 4ce2dfd6…), scripts dans `contre-verification-note-v1-scripts/`.
Statut : note de travail, non préenregistrée. Elle instruit les nœuds N-003 et N-004 et prépare le préenregistrement de T0.3. Les énoncés du programme (section 3) ne sont pas modifiés ici.
Références de fond (transcription, à vérifier sur PDF avant citation dans un papier) : Howard, Ramdas, McAuliffe, Sekhon (2021) ; Shin, Ramdas, Rinaldo (détecteurs e) ; Koning et Grünwald (2208.07610) ; Ramtin, Nain, Towsley (2601.20022). Le PDF de 2606.10456 est reçu ; sa lecture sur source primaire est en cours.

## 0. Ce qui change depuis la v1

1. Processus e : la forme close de la v1 était la forme **bilatérale** (paire en S_n, non monotone) ; la forme unilatérale (croissante en S_n), sur laquelle reposent L3 et T4, est ajoutée.
2. L1 est trajectoriel et vaut pour toute loi F₀, sans théorème central limite ; la puissance dépend de n₀ = NT. **La prédiction « plate en N et T » de la v1 était fausse** ; seule la platitude en m (la répartition) tient.
3. L2 : seuil exact du max ; plancher de puissance strictement au-dessus de α à n fixé.
4. L3 : règle unilatérale croissante, alarme « au plus tard à n₀ » (inclusif). Ajout d'une mise en garde : le critère de sécurité du programme (alarme avant que le dommage n'atteigne θ) n'est pas couvert.
5. L5 était faux : une compensation déterministe n'aveugle que les statistiques fonctions de la somme.
6. Mise en garde sur le programme : sous une copule autorégressive positive, le max a une puissance ≤ α (inégalité de Slepian), pas au-dessus ; sous une corrélation négative, la moyenne passe sous α.
7. T2 : hypothèses explicitées, version par sous-groupe, contre-exemple avec rôles. T3 corrigé : seules les statistiques **locales** ont une garantie face à un attaquant adaptatif. T4 précisé : « pas plus que sous P₀ », faux en bilatéral.
8. Validité hors hypothèses : un effet aléatoire par épisode, une corrélation entre agents ou un σ sous-estimé font exploser le taux de fausses alarmes de la règle toujours valide. Nouvelles gardes pour T0.3, la porte G1 et le papier B.

## 1. Cadre et hypothèses, résultat par résultat

- Indices I ⊂ {1,…,N} × {1,…,T} ; score X_{i,t} de l'action a_{i,t}. Ordre de lecture « temps d'abord » ; X_1, X_2, … dans cet ordre ; n = nombre d'actions lues ; n₀ = horizon (au plus NT).
- Lois honnêtes :
  - (P-iid) les X_k sont indépendants, de loi F₀, de moyenne μ₀ et de variance σ² ;
  - (P-H) la loi P₀ est invariante sous un groupe H de permutations de I (échangeable si H = toutes les permutations).
- Validité du processus e (V) : incréments indépendants, ou différences de martingale, sous P₀ ; μ₀ connu ; σ connu ou majoré ; incréments conditionnellement sous-gaussiens de paramètre σ².
- Hypothèses requises :

| Résultat | Hypothèses |
|---|---|
| L1, L4 | trajectoriels : aucune hypothèse sur P₀ pour l'identité ; (V) seulement pour le niveau de la règle |
| L2 | P-iid gaussienne pour la forme exacte (la décroissance en m vaut pour Φ log-concave) |
| L3 | (V) et règle unilatérale croissante |
| T1 | aucune |
| T2 | P-H |
| T3 | aucune (énoncé trajectoriel), seuil calibré sous P₀ |
| T4 | règle unilatérale croissante ; « ≤ α » demande (V) |

- Classes d'attaquant, à budget fixé :
  - **M** (décalage) : X_k = Y_k + δ_k·1{k ∈ S}, Y ~ P₀, Σδ_k = B (δ_k éventuellement adaptatifs, Σδ = B presque sûrement) ; les actions non sabotées gardent la loi honnête.
  - **M±** (décalage avec compensation) : on ajoute des décalages −γ_k sur des actions non sabotées.
  - **C** (multi-ensemble préservé) : X = π_Y(Y), π_Y permutation de I mesurable en Y (et en l'aléa privé).
  - **K** (copule) : la marginale de chaque coordonnée est F₀, la dépendance change (par exemple une copule gaussienne autorégressive de paramètre φ, comme dans 2606.10456).

## 2. Processus e de mélange normal

Avec S_n = Σ_{k≤n}(X_k − μ₀), V_n = σ²n, et un mélange sur λ :
- bilatéral, λ ~ N(0, ρ²) :
  E_n = (1 + ρ²V_n)^(−1/2) · exp( ρ²S_n² / (2(1 + ρ²V_n)) ) ;
- unilatéral, λ demi-normal sur [0, ∞) :
  E⁺_n = 2·(1 + ρ²V_n)^(−1/2) · exp( ρ²S_n² / (2(1 + ρ²V_n)) ) · Φ( ρS_n / √(1 + ρ²V_n) ), **croissant en S_n**.

Sous (V), ce sont des surmartingales positives d'espérance initiale 1 : P₀(∃n : E_n ≥ 1/α) ≤ α (inégalité de Ville).
ρ est fixé au préenregistrement comme minimiseur numérique de la frontière d'alarme à l'horizon n₀ ; à titre indicatif, la contre-vérification donne ρ ≈ 0,18 en unilatéral et ≈ 0,20 en bilatéral pour n₀ = 200 et σ = 1.
Le taux effectif de fausses alarmes à horizon fini est bien sous α (≈ 0,017 pour α = 0,05 et n₀ = 200, exploratoire) : toute comparaison se fait au taux effectif sous P₀, pas à α.

## 3. Lemme d'additivité

**L1 — invariance terminale (trajectorielle).** En classe M, pour toute trajectoire, S_{n₀}(X) = S_{n₀}(Y) + B, dès que tout le sabotage tombe dans les n₀ premières actions.
La loi de S_{n₀} est donc la loi honnête translatée de B, pour toute F₀, toute répartition (ensemble S, nombre m, agents, pas, valeurs δ_k) et même des δ_k adaptatifs.
Toute règle fonction de S_{n₀} a une puissance fonction de (B, n₀, F₀, α) — plus ρ et le côté pour E_{n₀}. Exemple gaussien, test z unilatéral : puissance = Φ̄(z_α − B/(σ√n₀)).
**À B fixé, la puissance décroît avec n₀ = NT** : plus d'actions honnêtes, plus de bruit.
Limite : un sabotage qui change la *forme* de la loi des actions sabotées, et pas seulement sa position, rend la loi de S_{n₀} dépendante de m. Par exemple, une variance σ₁² donne Var S_{n₀} = (n₀ − m)σ² + mσ₁².
*Lecture du programme* : « la puissance ne dépend que de B et de la variance » est exact si « la variance » est celle de la statistique terminale (n₀σ²). C'est faux si N et T varient à variance par action fixée.

**L2 — effondrement du max.** P-iid gaussienne, seuil exact c_n = Φ⁻¹((1 − α)^{1/n}), budget réparti également sur m ≤ n actions :
puissance = 1 − Φ(c_n)^{n−m} · Φ(c_n − B/(mσ))^m.
- Elle est décroissante en m (par concavité de log Φ, la dérivée de m·log Φ(c − B/(mσ)) est au moins log Φ(c)).
- À n fixé, elle a un plancher (atteint en m = n) ≈ α + (1 − α)·φ(c_n)·B/σ, strictement au-dessus de α.
- Elle ne tend vers α que si n → ∞ avec B√(log n)/n → 0.
- L'approximation √(2 log(n/α)) du seuil est à proscrire (taux réel de fausses alarmes 0,4 % à 0,7 % au lieu de 5 % : elle exagérerait la séparation entre L1 et L2).
- L'hypothèse (a) du programme (δ_k ≥ δ_min) borne la fragmentation : m ≤ B/δ_min.

**L3 — lecture toujours valide (règle unilatérale croissante, alarme au plus tard à n₀ inclusivement).**
- (a) Couplage : si la dérive cumulée D_n = Σ_{k≤n} δ_k d'une répartition domine celle d'une autre à tout n, trajectoire par trajectoire, la probabilité d'alarme d'ici n₀ est au moins aussi grande. Avancer le sabotage aide le défenseur, le reporter l'aide moins. En bilatéral, la preuve tombe.
- (b) Borne inférieure invariante : P(alarme d'ici n₀) ≥ P(E⁺_{n₀} ≥ 1/α), qui ne dépend que de (B, n₀, F₀, ρ, α) par L1. C'est faux pour « strictement avant n₀ ».
- (c) Prix de la garantie toujours valide : exploratoire, n₀ = 200, B = 25σ — test z à horizon fixé 0,549, contre 0,166 à 0,278 pour la règle toujours valide selon le calendrier.
- (d) **Mise en garde — critère de sécurité du programme.** La sécurité y est définie comme la probabilité d'une alarme *avant* que le dommage cumulé n'atteigne θ. Un attaquant qui reporte son sabotage en fin d'horizon ramène la détection à temps au niveau de P₀ (exploratoire : 0,017 pour m = 1, 0,127 pour m = 10). Le processus e cumulé depuis le début dilue la fenêtre de sabotage dans le préfixe honnête. Pour ce critère, les bons outils sont les **détecteurs de rupture** : somme cumulée de Page, ou détecteurs e (maximum ou somme de processus e redémarrés). L'agrégateur séquentiel du programme doit les inclure.

**L4 — répartition entre agents (trajectorielle).** Pour une règle qui ne dépend que des sommes aux frontières de pas (S_{tN})_t, la répartition du sabotage entre agents à un même pas est exactement invariante, y compris en toujours valide.
Hypothèses : pas d'interférence entre agents ; nombre d'actions par pas fixe ; pas de statistiques par agent.
**Validité** : le seuil suppose des agents indépendants au sein d'un pas. Exploratoire, avec N = 5, T = 40 et une équicorrélation c entre agents, les fausses alarmes valent 0,017 (c = 0) et 0,164 (c = 0,4). C'est le régime visé par le papier B (copies à poids partagés) : il faut une calibration robuste à la dépendance (section 5).

**L5 — compensation (corrigé).** Si des décalages déterministes ramènent le budget net à B_net = Σδ − Σγ = 0, **seules les statistiques fonctions de la somme sont aveugles**. La forme du multi-ensemble change, puisque E Σ(X − μ₀)² = n₀σ² + Σδ² + Σγ² ; le max, une statistique du χ² ou de Kolmogorov-Smirnov détectent (exploratoire : 0,53 ; 0,65 ; 0,08 contre 0,05 pour la somme).
Une restauration exacte de la loi du multi-ensemble exige des décalages *dépendant des données* : c'est la classe C. Que l'agent sache piloter ses propres activations pour cela est une **question empirique** (lien avec HC4 et Tr), pas un théorème.

## 4. Théorème négatif

**Mise en garde sur l'énoncé du programme : deux invariances différentes.**
- Classe C (multi-ensemble préservé) : toute statistique symétrique (invariante par permutation de I) a exactement le même taux de rejet que sous P₀ (T1).
- Classe K (marginales par coordonnée préservées, dépendance modifiée) : seules les *espérances* des statistiques additives sont préservées. Les taux de rejet s'écartent de α dans les deux sens.
  - φ > 0 : la moyenne, la somme et le processus e sont au-dessus de α. Le max est **à α ou en dessous** (inégalité de Slepian : la corrélation positive rend le max stochastiquement plus petit).
  - φ < 0 : la moyenne et le processus e sont sous α ; l'autocorrélation en valeur absolue détecte.
  - Exploratoire, φ = +0,5, n₀ = 200 : moyenne unilatérale 0,171 (valeur analytique 0,170), max 0,048, e unilatéral 0,200 (P₀ : 0,018), Page 0,663.
  - « Toute statistique de marginales (max, moyenne, somme cumulée) a une puissance égale au taux de faux positifs » est donc faux en classe K, et vrai en classe C pour les statistiques symétriques.

**T1 — aveuglement des statistiques invariantes (trajectoriel, aucune hypothèse sur P₀).** Soit G un groupe de permutations de I et f une statistique G-invariante. Si π_Y ∈ G presque sûrement (π_Y mesurable), alors f(X) = f(Y) pour chaque trajectoire. Tout test fondé sur f, dont l'aléa éventuel est indépendant de l'attaque, a une puissance égale à **son taux de rejet effectif sous P₀**.
Groupes utiles :
- toutes les permutations de I (moyenne, somme terminale, max, quantiles, histogramme) ;
- permutations du temps à l'intérieur de chaque agent (statistiques de marginale empirique par agent et leurs agrégats) ;
- permutations des agents à l'intérieur de chaque pas.

Le temps et les agents sont deux sous-groupes de permutations de I : c'est la forme précise du « même objet » du programme.

**T2 — impossibilité sans structure.** On suppose :
- (i) P₀ est H-invariante ;
- (ii) l'attaquant produit X = σ ∘ π_Y(Y), avec π_Y ∈ H et σ uniforme sur H, tirée indépendamment de Y et de son aléa, appliquée après π_Y.

Alors X ~ P₀ exactement : pour tout ensemble A, P(X ∈ A) = |H|⁻¹ Σ_{h∈H} P(hY ∈ A) = P(Y ∈ A).
Aucun test sur les scores ne dépasse alors son taux sous P₀. Si le dommage ne dépend pas de la position des actions sabotées, cet attaquant est indétectable par tout moniteur de scores.
- **Idéalisation** : l'attaquant fixe à l'avance son multi-ensemble et son arrangement. C'est une borne supérieure du pouvoir de l'attaquant.
- **Le groupe compte.** Exploratoire, avec trois agents de moyennes honnêtes −0,5, 0 et +0,5 (P₀ invariante seulement par permutations du temps à l'intérieur de chaque agent) : un rebrassage sur tout I est détecté avec une probabilité de 0,9995, un rebrassage du temps agent par agent reste à 0,050.
- **Les issues du défenseur ne sont pas deux mais au moins cinq** :
  - un décalage net de marginale (classe M, L1) ;
  - un changement de forme du multi-ensemble (L5) ;
  - un dommage structuré que l'attaquant ne peut pas brouiller (T3) ;
  - une loi honnête non invariante sous le groupe que l'attaquant utilise ;
  - de l'information hors des scores.

**T3 — dommage structuré : seules les statistiques locales ont une garantie (corrigé).**
- Si r actions consécutives d'un agent ont chacune un score ≥ v, la somme glissante maximale de fenêtre w ≤ r vaut au moins w·v, trajectoire par trajectoire. Sa puissance vaut 1 dès que w·v ≥ c_{n,w,α} (seuil calibré sous P₀).
- Même énoncé pour la co-élévation : si m agents ont un score ≥ v au même pas, le maximum sur les pas de la somme des m plus hauts scores du pas vaut au moins m·v.
- **Les statistiques d'ordre globales (autocorrélation, test des suites) n'ont aucune garantie face à un attaquant adaptatif**, qui réarrange le reste de l'épisode pour les neutraliser. Exploratoire : autocorrélation de 0,464 à 0,049, test des suites de 0,074 à 0,036, alors que le balayage et Page restent ≥ 0,996.
- La garantie exige que v soit assez haut. Exploratoire : avec les r valeurs juste au-dessus du quantile q, le balayage reste ≈ α pour q ≤ 0,8 et r ≤ 5.

**T4 — somme cumulée lue séquentiellement (corrigé).** On considère une règle unilatérale croissante en chaque S_n, et un arrangement dont les sommes partielles sont, pour chaque trajectoire, dominées par celles de l'ordre honnête. C'est le cas du tri croissant, ou du déplacement des r plus hautes valeurs en fin d'horizon en conservant les ordres relatifs. Alors
P(alarme d'ici n₀) ∈ [ P₀(E⁺_{n₀} ≥ 1/α) , P₀(alarme d'ici n₀) ],
donc ≤ α si (V) tient.
- C'est **faux pour la règle bilatérale** : le tri croissant creuse les sommes partielles et déclenche l'alarme (exploratoire : 1,000).
- Ces arrangements sont détectés par le balayage et par Page.
- La prédiction du programme « la somme cumulée échoue » est exacte pour la somme terminale (T1). Pour la somme séquentielle unilatérale, elle est exacte au sens adverse (T4).

## 5. Validité hors hypothèses — gardes nécessaires

Taux de fausses alarmes de la règle toujours valide (exploratoire, `SeedSequence(27182818)`) :

| Situation | n₀ = 200 | n₀ = 1000 |
|---|---|---|
| F₀ gaussienne | 0,016 | 0,018 |
| F₀ asymétriques ou à queues lourdes | 0,019 à 0,029 | — |
| σ sous-estimé de 20 % | 0,067 | — |
| effet épisode τ = 0,05 / 0,1 / 0,2 | 0,035 / 0,086 / 0,214 | 0,111 / 0,242 / 0,364 |
| équicorrélation entre agents c = 0,4 (N = 5) | 0,164 | — |

**Conséquence pour tout le programme.** Sur des activations réelles, les scores d'un même épisode partagent un effet (consigne, sujet, état du contexte), et les copies à poids partagés sont corrélées. Un processus e qui suppose des incréments indépendants n'est pas valide en l'état. Pistes à préenregistrer :
1. Calibration par rééchantillonnage d'épisodes honnêtes entiers (amorçage par blocs).
2. Agrégation au niveau de l'épisode, puis processus e sur les agrégats d'épisodes.
3. Variance estimée de façon conservatrice (borne supérieure), avec pari adaptatif.
4. Modèle hiérarchique à effet épisode.

La garde de la porte G1 (« le taux de faux positifs des agrégateurs toujours valides est vérifié empiriquement sur épisodes honnêtes ») est donc **décisive**, pas formelle.

## 6. Conséquences pour les nœuds de décision

- **N-003 (théorème négatif)** : la recommandation (a) tient, précisée.
  - Énoncé par invariance (T1) ; impossibilité sans structure sous P₀ invariante (T2) ; garanties locales sous structure (T3).
  - Unification temps × agents par sous-groupes de permutations.
  - Distinction explicite des classes C et K, qui corrige l'énoncé du programme et se démarque de 2606.10456.
- **N-004 (lemme)** : la recommandation (a) tient, précisée.
  - Invariance terminale exacte et trajectorielle (L1), dépendant de n₀.
  - Séparation avec le max (L2, plancher au-dessus de α à n fixé).
  - Borne inférieure toujours valide (L3 b) et prix de la garantie.
  - Mise en garde sur le critère « avant le dommage », qui impose des détecteurs de rupture.
  - Validité sous dépendance (section 5).
  - La non-compensation n'est plus une « condition du lemme » mais un régime (L5) : la compensation déterministe reste visible, la compensation exacte relève de la classe C.

## 7. Prédictions révisées pour le préenregistrement de T0.3

Toutes les puissances se comparent au **taux effectif sous P₀** de la même statistique, mesuré sur des répétitions dédiées. Grille : m ≤ NT ; seuils exacts ou calibrés par Monte-Carlo sous P₀, avec des graines distinctes.

1. L1 : à n₀ fixé, puissance terminale plate en m et en répartition (agents, pas) ; à B fixé, décroissante en n₀ selon Φ̄(z_α − B/(σ√n₀)) (test z).
2. L2 : max au seuil exact, décroissant en m vers un plancher ≈ α + (1 − α)·φ(c_n)·B/σ.
3. L3 : règle unilatérale ; alarme d'ici n₀ ordonnée avancé ≥ uniforme ≥ reporté, toujours ≥ P(E⁺_{n₀} ≥ 1/α). Détection avant la dernière action sabotée : celle du processus e cumulé est dominée par celle de Page et des détecteurs e.
4. T1 et T2 : sous un réarrangement uniforme (P₀ échangeable), toute statistique à son taux sous P₀ ; sous tout arrangement, les statistiques symétriques à leur taux sous P₀.
5. T3 : pour (r, q) préenregistrés, le balayage de fenêtre ≤ r et Page au-dessus du taux sous P₀ dès que w·v ≥ seuil ; autocorrélation et suites neutralisables par l'arrangement adaptatif.
6. Classe K : φ > 0 → moyenne, somme et e au-dessus, max à son taux ou en dessous ; φ < 0 → moyenne et e en dessous, |autocorrélation| au-dessus.
7. T4 : e unilatéral entre la borne terminale et le taux sous P₀ pour les arrangements dominés ; e bilatéral au-dessus.
8. Gardes de mauvaise spécification (effet épisode, corrélation entre agents, σ estimé, F₀ asymétrique) : taux de fausses alarmes mesurés et publiés ; au moins une variante robuste à la dépendance (section 5) comparée.

**Transparence (R1, R4).** Des simulations exploratoires du contre-vérificateur ont déjà touché plusieurs de ces configurations. Les prédictions ci-dessus découlent de preuves, pas de ces chiffres. Le préenregistrement le déclarera, et T0.3 utilisera des graines neuves et une grille fixée indépendamment.
