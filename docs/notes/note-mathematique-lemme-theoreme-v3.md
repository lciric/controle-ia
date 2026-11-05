# Note mathématique — lemme d'additivité et théorème négatif — v3 (T0.3)

Date : 2026-10-06 (UTC), session 10. Remplace la v2 (`note-mathematique-lemme-theoreme-v2.md`, empreinte 85703afd…, archivée sans modification), qui remplaçait la v1 (277ffc9b…).
La v2 intégrait la contre-vérification adverse d'un sous-agent neuf : `contre-verification-note-v1.md` (empreinte 4ce2dfd6…), scripts dans `contre-verification-note-v1-scripts/`. Les preuves des sections 2 à 5 sont celles de la v2, inchangées ; la v3 ajoute les résultats de T0.3, les énoncés retenus par Lazar et les lectures sur PDF (section 0).
Statut : note de travail, non préenregistrée. Elle fixe la base mathématique du papier A ; les énoncés retenus sont ceux des décisions N-003 et N-004 (section 6) et la lecture du programme corrigée par P-008 (section 8).
Références :
- lues sur PDF empreinté (R7) : Pérez-Ortiz, Lardy, de Heide et Grünwald, arXiv 2208.07610v2 ; Ramtin, Nain et Towsley, arXiv 2601.20022v2 (rapport `docs/sources/lecture-pdf-niveau2/rapport-lemme-v1.md`, a3c837de…) ; 2606.10456 (niveau 1, `docs/sources/lecture-pdf-niveau1/rapport-2606.10456-v1.md`) ; voisins de L et T lus au niveau 2 (section 8) ;
- de fond, encore sur transcription, à lire sur PDF avant citation dans un papier : Howard, Ramdas, McAuliffe et Sekhon (2021) ; Shin, Ramdas et Rinaldo (détecteurs e).

## 0. Ce qui change depuis la v2

1. **Résultats de T0.3** (section 7, qui remplace les prédictions de la v2) : le run décisif `20261004-080257-t03` confirme les 31 prédictions préenregistrées (`docs/notes/resultats-T0.3-v1.md`, 9ab618ed…). Les nombres exploratoires de la v2 restent tels quels ; les nombres opposables sont ceux du run.
2. **Énoncés retenus** (section 6, qui remplace les recommandations) : N-003 et N-004, option (a), GO-2026-10-04-02 et GO-2026-10-04-03.
3. **Références corrigées** (P-008, GO-2026-10-06-03 ; `docs/decisions/decision-P-008-v1.md`, ac9551b0…) :
   - 2208.07610 est de Pérez-Ortiz, Lardy, de Heide et Grünwald, et non « Koning et Grünwald » ; sous garantie toujours valide, le critère qui remplace la puissance est la croissance au pire cas (GROW) ;
   - 2601.20022 donne un délai d'ordre Θ(γ) contre un adversaire couvert stationnaire qui connaît γ ; l'hypothèse (b) du lemme (budget total borné) est un choix de modélisation, pas une conséquence de cet article.
4. **Antériorité sur source primaire** (section 8) : aucun énoncé de L ni de T n'est occupé en entier ; 2608.02698 occupe L en partie, en boîte noire et par des outils classiques ; 2607.11751 occupe la seule moitié négative de T, qui n'est pas revendiquée.

## 0 bis. Ce qui avait changé de la v1 à la v2

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
  Confirmé par T0.3 (P3.4) : sabotage en bloc en fin d'horizon (m = 5 à 20), alarme avant la dernière action sabotée, au même taux de fausses alarmes, processus e cumulé calibré 0,09 à 0,25, Page 0,57 à 1,00, détecteur e 0,52 à 1,00 (`resultats-T0.3-v1.md`, magnitude 2).

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
  - Confirmé par T0.3 (P6) sur la construction même de 2606.10456 (φ₀ = 0,5, T = 300) : pour φ₁ = 0,9, somme 0,253, max 0,027, autocorrélation 1,000, Page 0,72. La « puissance = taux de faux positifs » de sa proposition 1 est fausse pour la somme ; elle est vraie, et même pessimiste, pour le max (`resultats-T0.3-v1.md`, magnitude 4).

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

Confirmé par T0.3 (P8) : la règle de Ville monte à 0,21 (effet épisode τ = 0,2, n₀ = 200) et 0,35 (n₀ = 1000) ; le calibrage conforme sur 1 000 épisodes honnêtes entiers donne 0,046 à 0,055 dans les 17 réglages, pour 0,04995 prédit (`resultats-T0.3-v1.md`, magnitude 6). C'est la piste 1, retenue pour G1 (brouillon 3 du préenregistrement, `bases.sequentiel`).

## 6. Énoncés retenus (décisions de Lazar)

- **N-003, théorème négatif** (GO-2026-10-04-02, option (a)) : énoncé par invariance.
  - T1 à T4 de cette note ; classes C et K distinguées ;
  - temps et agents comme sous-groupes de permutations de I ;
  - 2606.10456 cité comme antécédent défectueux : sa proposition 1 est fausse pour la somme en classe K (section 4).
- **N-004, lemme d'additivité** (GO-2026-10-04-03, option (a)) : énoncé adverse.
  - invariance terminale et spatiale (L1, L4) ;
  - borne inférieure toujours valide (L3 b) ;
  - coût du report chiffré (L3 c, d ; T0.3, P3.2) ;
  - non-compensation comme condition empirique (L5).
- Rien n'a changé dans ces énoncés depuis leur décision : P-008 et le niveau 2 de l'état de l'art ne touchent que leurs références et leur antériorité (sections 0 et 8).

## 7. Résultats de T0.3 (run décisif)

- **Pièces** : préenregistrement scellé `prereg/T0.3-simulation-lemme-theoreme-v1.md` (7474743a…), grille `prereg/T0.3-grille-v2.json` (5609f920…), trois contre-lectures, run `20261004-080257-t03` (manifeste c9bba5e1…), lecture gelée `diag/20261004-080257-t03/lecture.json` (c5aa62b4…), figures F1 à F6. Résumé : `docs/notes/resultats-T0.3-v1.md` (9ab618ed…).
- **Prononcé** : 31 prédictions sur 31 confirmées ; 342 cellules statistiques et 544 trajectorielles ; 0 contraire ; audit de symétrie non déclenché (variance des écarts réduits 0,955 et 0,853, bornes gelées [0,3 ; 3]).
- **Réserve (R4)** : la plupart de ces prédictions vérifient l'instrument. Le run établit que les agrégateurs et les calibrages sont corrects, que l'arithmétique des preuves est juste et que les magnitudes informatives sont celles annoncées. Il ne prouve ni le lemme ni le théorème sur des activations réelles.
- **Magnitudes informatives** (α = 0,05, R = 20 000) :
  1. calendrier (L3) : à n₀ = 200, B = 25, m = 10, alarme d'ici n₀ de 1,000 (sabotage au début) à 0,160 (à la fin), borne terminale 0,158 (théorie 0,159) ;
  2. détecteurs de rupture (L3 d) : voir section 3 ;
  3. max contre somme (L1, L2) : à n₀ = 200, B = 20, somme terminale 0,41 quelle que soit la répartition ; max de 1,00 (m ≤ 5) à 0,071 (m = 200), plancher prédit 0,0714 ;
  4. classe K et 2606.10456 : voir section 4 ;
  5. classe C (T1 à T3) : statistiques symétriques identiques au bit près sous réarrangement ; après appariement adaptatif, autocorrélation de 0,46 à 0,0515 (P₀ : 0,0507), moyenne glissante (w = 5) 1,000 et Page 0,997 ; le groupe compte (rebrassage total 0,967, intra-agent 0,0505) ;
  6. validité hors hypothèses : voir section 5.
- **Lecture des énoncés du programme** (table E du run) : lemme exact pour la statistique terminale à n₀ fixé ; faux à variance par action fixée quand n₀ varie, et pour la lecture séquentielle quant au calendrier ; L4 non testé. Théorème vrai en classe C, faux en classe K.

## 8. Références sur source primaire et antériorité (P-008 ; niveau 2)

**Lecture retenue des deux précautions du lemme** (P-008, mot pour mot ; rapport `rapport-lemme-v1.md`, section 3 ; 106 citations contrôlées par script, 0 échec) :
- « Sous garantie toujours valide (arrêt et continuation optionnels), la puissance n'est pas un critère d'optimalité utilisable : sa définition exige une règle d'arrêt connue. Elle reste le critère des tests à taille fixe et des tests séquentiels classiques de Wald, dont la règle d'arrêt est fixée. Le critère qui la remplace est la croissance logarithmique espérée au pire cas sous l'alternative (GROW) (Pérez-Ortiz, Lardy, de Heide et Grünwald, arXiv 2208.07610v2, p. 2, 6-7 et 26). Cet article ne chiffre pas l'écart entre les deux régimes. »
- « Contre un adversaire couvert qui connaît le paramètre γ de la contrainte de fausses alarmes (temps moyen avant fausse alarme au moins γ) et choisit une loi après rupture stationnaire dépendant de γ, le délai moyen de détection optimal au pire cas (critère de Lorden, atteint par la somme cumulée de Page réglée sur cette loi) est d'ordre Θ(γ), au lieu de log γ dans le cadre classique ; dans ce régime furtif, le dommage cumulé avant détection est au plus d'ordre γ^(1−ρ), soit √γ pour un décalage de moyenne (Ramtin, Nain et Towsley, arXiv 2601.20022v2, p. 3-4, 8-11). L'article ne traite ni de budget total, ni d'adversaire non stationnaire, ni de garantie toujours valide. »

**Ce que ces deux lectures changent dans la note.**
- L3 (c), le prix chiffré de la garantie toujours valide (horizon fixé contre lecture toujours valide, et calendrier), est un écart que 2208.07610 ne chiffre pas ; le lecteur le note : « ce chiffrage serait une contribution du programme » (annexe 2 de la synthèse du niveau 2).
- L3 (d) rejoint 2601.20022 sur la nécessité d'un détecteur de rupture avant un seuil de dommage, mais sous une autre hypothèse : budget total borné, choix de modélisation déclaré du programme, au lieu d'un adversaire stationnaire qui connaît γ.

**Antériorité de L et T sur PDF** (synthèse `docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md`, bbe0c1f5… ; annexe 2, `niveau2-v1/anteriorite-v1.md`, c5465a9b…) :
- **L** :
  - occupé en partie par 2608.02698 (p. 5, `lot2-B1`) : la puissance de tout test y est bornée par une fonction de la divergence totale, sous décomposition additive. C'est une borne supérieure seulement, en boîte noire, par des outils classiques, sans résultat mesuré ;
  - voisins (outils à citer comme classiques) : 2208.07610 et 2601.20022 (ci-dessus) ; 2607.11751 (agrégation « alarme si l'une », p. 10, 16) ; 2610.04575 et 2411.17693 ;
  - reste revendicable : l'énoncé adverse complet appliqué aux scores de sondes — invariances exactes, borne toujours valide, coût du report, détection à temps, validité sous dépendance.
- **T** :
  - 2607.11751 (p. 2, 3, 10, `lot3-Ab`) occupe la seule moitié négative : un moniteur qui ne voit que des fragments localement bénins et indiscernables est aveugle (borne en variation totale). Cette moitié n'est pas revendiquée ;
  - voisins : 2005.07821 (chaque statistique cumulée est aveugle à une attaque qui préserve ce qu'elle accumule, remarque, p. 5) ; 2605.26047 (le bon agrégateur dépend des corrélations que l'attaquant choisit, p. 7) ;
  - reste revendicable : les quatre pièces de N-003 — unification temps × agents par sous-groupes de permutations, distinction C/K, garanties locales face à un attaquant adaptatif, transposition aux activations réelles.
- Libre veut dire « non trouvé dans les sources lues » (R8). La veille hebdomadaire porte sur ces deux zones.
