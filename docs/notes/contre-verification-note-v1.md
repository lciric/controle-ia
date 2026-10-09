# Contre-vérification adverse de la note mathématique v1

Date : 2026-10-04 (UTC). Relecteur : sous-agent neuf, qui n'a pas écrit la note (R2 appliquée par analogie à une note de travail).
Document relu : `docs/notes/note-mathematique-lemme-theoreme-v1.md` (empreinte 277ffc9b…).
Scripts du relecteur, scellés : `docs/notes/contre-verification-note-v1-scripts/` (graines `SeedSequence` indiquées dans chaque script).
Reproductibilité : `v1_formes_closes.py` et `v7_copule.py` ont été rejoués par l'auteur de la note ; sorties identiques.
**Statut des chiffres : simulations exploratoires de vérification, non préenregistrées.** Elles ne sont pas les résultats de T0.3.
Le rapport est reproduit tel que rendu (mise en forme seule).

---

Conventions communes : α = 0,05 et F₀ = N(0,1) sauf mention contraire ; ρ choisi pour minimiser la frontière d'alarme à n₀ (à n₀ = 200 : ρ = 0,183 unilatéral, 0,203 bilatéral) ; seuils calibrés par Monte-Carlo sous P₀, avec une graine distincte de celle de l'attaque.

## Préambule — forme close du processus e
**Correcte en bilatéral, absente pour l'unilatéral.**
- La formule affichée est exactement le mélange bilatéral λ ~ N(0, ρ²). Écart en log avec l'intégration numérique ≤ 2,3·10⁻¹¹ (S ∈ [−30 ; 25], n ∈ {1, 10, 100, 1000}, σ ∈ {0,5 ; 1 ; 2}, ρ ∈ {0,05 ; 0,3 ; 1}).
- Elle dépend de S_n² : paire en S_n, donc non monotone. Or L3 et T4 reposent sur la monotonie.
- Forme unilatérale (λ ≥ 0, mélange demi-normal), vérifiée à 1,4·10⁻⁶ près en log : E⁺_n = 2·(1+ρ²σ²n)^(−1/2)·exp(ρ²S_n²/(2(1+ρ²σ²n)))·Φ(ρS_n/√(1+ρ²σ²n)). La formule affichée prise pour l'unilatérale donne une erreur en log jusqu'à 363.
- Hypothèses à ajouter : E_n n'est un processus e que si μ₀ est connu, σ connu ou surestimé, et les incréments conditionnellement sous-gaussiens de proxy σ².

## L1 — invariance de la statistique terminale
**Correct, et plus fort qu'énoncé ; dépendance en n₀ oubliée ailleurs.**
- En classe M, S_{n₀}(X) = S_{n₀}(Y) + B trajectoire par trajectoire, pour toute F₀, même avec des δ_k adaptatifs dès que Σδ = B presque sûrement. L'invariance en loi est exacte sans théorème central limite ; la phrase « hors cas gaussien… asymptotiquement » est trop faible.
- Vraie limite : un sabotage qui change la forme de la loi (par exemple une variance σ₁² sur les actions sabotées : Var S_{n₀} = (n₀−m)σ² + mσ₁² dépend de m).
- La puissance vaut Φ̄(z_α − B/(σ√n₀)) : elle dépend de n₀ = NT. Le programme (« ne dépend que de B et de la variance ») et la prédiction 1 (« plate en m, N et T ») sont faux pour N et T. À B = 20σ : 0,998 (NT = 20), 0,409 (NT = 200), 0,116 (NT = 2000).
- Correction : la loi de S_{n₀} est la loi honnête translatée de B, pour toute F₀ et toute répartition dans les n₀ premières actions ; la puissance dépend de (B, n₀, F₀, α), plus ρ et le côté pour E_{n₀}.

## L2 — effondrement du max
**Correct dans le fond (décroissance en m par log-concavité de Φ), faux sur deux calculs.**
- Seuil : √(2 log(n/α)) surestime le seuil exact c_n = Φ̄⁻¹(1−(1−α)^{1/n}) de 0,55 à 0,80 ; le taux de faux positifs réel tombe entre 0,41 % et 0,72 % (n de 1 à 2000) au lieu de 5 %. Utiliser c_n exact ou calibré, sinon T0.3 exagère la séparation entre L1 et L2.
- Borne de l'union : à B = 0 elle vaut n(1−(1−α)^{1/n}), croissante vers −ln(1−α) = 0,0513 > α ; elle ne « tend pas vers au plus α ». Et m → ∞ à n fixé est impossible (m ≤ n).
- Puissance exacte : 1 − Φ(c_n)^{n−m}·Φ(c_n − B/(mσ))^m ; à n fixé, plancher strictement au-dessus de α, ≈ α + (1−α)·φ(c_n)·B/σ. Avec B tel que le test terminal ait une puissance de 0,5 : plancher 0,140 (n = 20), 0,076 (n = 200), 0,058 (n = 2000) ; n = 200 et m = 100 : 0,082. Tend vers α seulement si n → ∞ avec B√(log n)/n → 0.
- Incohérence avec l'hypothèse (a) du programme (δ_k ≥ δ_min) : elle impose m ≤ B/δ_min.

## L3 (a) — couplage trajectoriel
**Correct avec des hypothèses à ajouter** : E_n = h_n(S_n) avec h_n croissante (règle unilatérale, pas la formule affichée) ; dérives comparées trajectoire par trajectoire ; « plus grande ou égale » ; « au plus tard à n₀ ». En bilatéral, la preuve tombe (l'ordre a tenu sur la grille, sans démonstration).
Simulation : n₀ = 200, B = 25σ, 40 000 répétitions, `SeedSequence(20261004)`. Probabilité d'alarme d'ici n₀ :

| Règle | m | avancé | uniforme | reporté |
|---|---|---|---|---|
| unilatérale | 10 | 1,000 | 0,276 | 0,166 |
| unilatérale | 50 | 0,830 | 0,276 | 0,175 |
| unilatérale | 200 | 0,278 | 0,278 | 0,278 |
| bilatérale | 10 | 1,000 | 0,190 | 0,114 |

Sous P₀ : 0,017 (unilatéral), 0,015 (bilatéral).
Mise en garde : « meilleure réponse » vaut pour l'alarme d'ici n₀. Pour le critère de sécurité du programme (alarme avant que le dommage n'atteigne θ), un calendrier reporté rend la détection à temps quasi nulle : alarme strictement avant la dernière action sabotée = 0,017 pour m = 1 (niveau de P₀), 0,127 pour m = 10.

## L3 (b) — borne inférieure terminale
**Correct si « avant n₀ » est inclusif, faux s'il est strict** (reporté, m = 1 : 0,017 contre une borne de 0,159). Le membre de droite dépend aussi de ρ et du côté (0,159 unilatéral, 0,103 bilatéral). Prix de la garantie toujours valide : un test z à horizon fixé a une puissance de 0,549, contre 0,166 à 0,278 pour la règle toujours valide.

## L4 — répartition entre agents
**Correct (identité trajectorielle, pour toute F₀).** Hypothèses à écrire : la règle ne dépend que de (S_{tN})_t (pas de statistiques par agent) ; pas d'interférence entre agents ; nombre d'actions par pas fixe.
Validité : le seuil suppose des agents indépendants au sein d'un pas. N = 5, T = 40, équicorrélation c, `SeedSequence(27182818)` : fausses alarmes 0,017 (c = 0), 0,049 (c = 0,1), 0,083 (c = 0,2), 0,164 (c = 0,4) — précisément le régime du papier B.

## L5 — non-compensation
**Faux pour « la statistique terminale »** : seule la somme (et ses fonctions) devient aveugle. Des décalages déterministes ne restaurent jamais la loi du multi-ensemble (E Σ(X−μ₀)² = n₀σ² + Σδ² + Σγ²).
n₀ = 200, 10 actions à +2σ et 100 à −0,2σ (B_net = 0), 20 000 répétitions, `SeedSequence(57721566)` : somme bilatérale 0,051 (= P₀), max 0,532, χ² 0,653, Kolmogorov-Smirnov 0,081.
Correction : à B_net = 0, seules les statistiques fonctions de la somme sont aveugles ; une restauration exacte suppose des décalages dépendant des données (classe C). La « proposition pour Lazar » est une conjecture empirique, pas un énoncé mathématique.

## Mise en garde sur l'énoncé du programme
**Conclusion correcte, mais signe faux pour le max et oubli du cas φ < 0.** Pour φ > 0, la puissance du max est ≤ α (inégalité de Slepian) ; pour φ < 0, la moyenne et le processus e passent sous α.
Copule AR(1), n₀ = 200, seuils calibrés sous P₀ indépendante, `SeedSequence(16180339)` : φ = +0,5 → moyenne unilatérale 0,171 (analytique 0,170), max 0,048, e unilatéral 0,200 (P₀ : 0,018), Page 0,663 ; φ = +0,8 → max 0,037 ; φ = −0,5 → moyenne 0,002, e 0,000, |autocorrélation| 1,000. Même profil avec une marginale Exp(1)−1.
Correction : distinguer (i) multi-ensemble préservé (classe C) — toute statistique symétrique a le même taux de rejet que sous P₀ ; (ii) marginale par coordonnée préservée (copule) — seule l'espérance des statistiques additives est préservée, l'écart à α peut aller dans les deux sens. La compatibilité invoquée avec le « Monitor A » suppose qu'il est de type moyenne : à vérifier sur le PDF.

## T1 — aveuglement des statistiques invariantes
**Correct (trajectoriel, aucune hypothèse sur P₀).** Écrire « puissance égale à son taux de rejet effectif sous P₀ », pas « à son niveau » (la règle toujours valide est à 0,017, pas 0,05). Ajouter : π_Y mesurable ; aléa éventuel du test indépendant de l'attaque. Vérifié : somme terminale et max ont des taux identiques sous tous les arrangements testés (0,0505 et 0,0486).

## T2 — impossibilité sans structure
**Correct avec hypothèses à ajouter** : X = σ∘π_Y(Y), σ uniforme, tirée indépendamment de Y et de l'aléa de l'attaquant, appliquée après π_Y ; P₀ échangeable sur tout I — version par sous-groupe : si P₀ est H-invariante, π_Y ∈ H et σ uniforme sur H, alors X ~ P₀ ; attaquant anticipatif (connaît Y à l'avance).
Contre-exemple avec rôles : N = 3 agents de moyennes −0,5 / 0 / +0,5, T = 50 ; un rebrassage uniforme sur tout I est détecté avec probabilité 0,9995 ; un rebrassage restreint au temps, agent par agent, reste à 0,050.
La dichotomie « deux seules issues » est incomplète : P₀ non échangeable ; tout changement de forme du multi-ensemble, pas seulement de sa moyenne (cf. L5) ; information hors des scores.

## T3 — dommage structuré
**Faux en généralité.**
- Contre-exemple 1 (attaquant adaptatif) : n = 200, les 5 plus hautes valeurs en suite, le reste réarrangé par échanges gloutons, 8 000 répétitions, `SeedSequence(31415)` : autocorrélation 0,464 → 0,049 ; test des suites 0,074 → 0,036 (P₀ : 0,039) ; balayage de fenêtre 5 reste à 1,000 et Page à 0,996.
- Contre-exemple 2 (« score élevé » à quantifier) : la suite porte les r valeurs juste au-dessus du quantile q, `SeedSequence(57721566)` : balayage ≈ α pour q ≤ 0,8 et r ≤ 5 ; 0,162 (r = 5, q = 0,9), 0,962 (r = 5, q = 0,95), 0,259 (r = 10, q = 0,8).
- Correction : si r actions consécutives ont chacune un score ≥ v, la somme glissante maximale de fenêtre w ≤ r vaut au moins w·v pour chaque trajectoire, et sa puissance vaut 1 dès que w·v ≥ c_{n,w,α} ; énoncé analogue pour la co-élévation. Les statistiques d'ordre globales n'ont aucune garantie face à un attaquant adaptatif.

## T4 — réponse précise
**Correct pour la règle unilatérale, faux pour la formule bilatérale affichée ; « peut descendre à α ou en dessous » est imprécis.**
- Le tri croissant, ou le déplacement des r plus hautes valeurs en fin d'horizon en conservant les ordres relatifs, donne pour chaque réalisation des sommes partielles ≤ celles de l'ordre honnête, à somme terminale égale. Pour toute règle croissante en chaque S_n : P(alarme) ≤ P₀(alarme sur le même horizon), sans hypothèse de loi. L'énoncé sûr est « pas plus que sous P₀ » ; « ≤ α » n'en découle que si E est un vrai processus e sous la vraie P₀. Borne basse : P(alarme) ≥ P₀(E_{n₀} ≥ 1/α). Avec une grappe finale dans un ordre arbitraire, la domination tombe (valeurs {0, 0, 5, 10} : l'ordre 0, 0, 10, 5 donne S₃ = 10 > 5).
- n₀ = 200, r = 10, 20 000 répétitions, `SeedSequence(4102026)` (couplage vérifié, écart ≤ 2·10⁻¹³) : e unilatéral 0,0162 (honnête), 0,0025 (tri croissant), 0,0027 (10 plus hautes à la fin ; borne basse 0,0028) ; e bilatéral 1,000 (tri) et 0,105 (10 plus hautes à la fin) ; balayage et Page 1,000 ; autocorrélation 1,00 et 0,91.
- Sous une P₀ mal spécifiée (effet épisode τ = 0,1, `SeedSequence(14142135)`) : honnête 0,089, tri 0,056 > α ; « ≤ P₀ » tient, « ≤ α » tombe.
- Énoncé corrigé : pour toute règle unilatérale croissante en S_n, tout arrangement à sommes partielles dominées par celles de l'ordre honnête vérifie P(alarme d'ici n₀) ∈ [P₀(E_{n₀} ≥ 1/α), P₀(alarme d'ici n₀)], donc ≤ α si E est valide ; faux en bilatéral ; l'arrangement est détecté par le balayage et par Page.

## Validité hors hypothèses
`SeedSequence(27182818)`. Taux de fausses alarmes de la règle toujours valide : F₀ gaussienne 0,016 (n₀ = 200), 0,018 (n₀ = 1000) ; F₀ asymétriques ou lourdes (max de 50 gaussiennes, Gumbel, Exp, Beta, t5) 0,019 à 0,029 ; σ sous-estimé de 20 % : 0,067 ; effet épisode τ = 0,05 / 0,1 / 0,2 : 0,035 / 0,086 / 0,214 (n₀ = 200) et 0,111 / 0,242 / 0,364 (n₀ = 1000).
La « variante échangeable » suffit pour T1 et T2, pas pour la règle du lemme. Grille de T0.3 : imposer m ≤ NT.

## Trois corrections prioritaires avant le préenregistrement de T0.3
1. Fixer la règle séquentielle : forme unilatérale exacte (facteur 2Φ), ρ fixé en fonction de n₀, « au plus tard à n₀ » inclusif ; réécrire T4 ; préciser que la borne de L3 porte sur la détection d'ici n₀, pas avant le dommage.
2. Corriger les prédictions fausses par construction : (1) plate en m mais décroissante en NT ; (2) seuil exact du max, plancher au-dessus de α ; (6) copule avec φ > 0 : max ≤ α ; (4) et (7) comparer au taux empirique sous P₀ de chaque statistique ; (5) paramétrer r et q, limiter la prédiction au balayage de fenêtre ≤ r et à Page.
3. Séparer les hypothèses par résultat (T1 aucune ; T2 échangeabilité sur I ou un sous-groupe ; L1 et L4 trajectoriels ; validité de E : incréments indépendants ou différences de martingale, μ₀ connu, σ majoré, loi sous-gaussienne) et ajouter des gardes de mauvaise spécification (effet épisode, corrélation entre agents, σ estimé, F₀ asymétrique).
