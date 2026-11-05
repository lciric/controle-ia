# Décision — N-003 et N-004 : énoncés retenus du théorème négatif et du lemme d'additivité — v1

Date : 2026-10-04 (UTC).

**Décision de Lazar** : « GO N-003 a, N-004 a ». Consignée dans `registres/go.md` (GO-2026-10-04-02 et GO-2026-10-04-03) et dans `registres/decisions.md`.

**Portée.**
- Cette note fixe la lecture du programme v2 (section 3 ; section 5, hypothèses L et T) **à compter du GO**.
- Elle ne modifie pas le texte du programme, document qui fait foi transmis par Lazar. Une v3 du programme, si Lazar en transmet une, remplacera cette note sur ces points.
- Les préenregistrements du papier A (porte G1, phase 1) partent de ces énoncés.

**Sources.**
- Options : `livrables/premier-rendu-v1/decisions-v1.md` (N-003, N-004) et `livrables/anteriorite-niveau1-v1/decisions-v2.md` (N-003 renforcé).
- Énoncés et preuves : `docs/notes/note-mathematique-lemme-theoreme-v2.md`.
- Vérification en simulation : `docs/notes/resultats-T0.3-v1.md` (run `20261004-080257-t03`, préenregistrement scellé `7474743a…`).

## 1. Théorème négatif (T) — énoncé par invariance (N-003, option a)

**Cadre.**
- Scores X_{i,t} indexés par I ⊂ {1, …, N} × {1, …, T}.
- Groupes de permutations de I :
  - permutations du temps à l'intérieur de chaque agent ;
  - permutations des agents à l'intérieur de chaque pas ;
  - toutes les permutations.

  **Le temps et les agents sont deux sous-groupes du même objet** : c'est la forme précise de l'« indexation agnostique » du programme.

**Énoncés retenus** (note v2, section 4) :
- **T1 — aveuglement des statistiques invariantes**, trajectoriel, sans hypothèse sur la loi honnête. Une attaque de classe C préserve le multi-ensemble par une permutation π_Y ∈ G. Elle laisse inchangée, trajectoire par trajectoire, toute statistique G-invariante ; sa puissance est son taux sous P₀.
- **T2 — impossibilité sans structure.** On suppose P₀ invariante sous H. Un réarrangement suivi d'un rebrassage uniforme sur H rend les scores exactement de loi P₀ : aucun moniteur de scores ne dépasse son taux. Le groupe compte : une P₀ invariante seulement sous un sous-groupe laisse détecter un rebrassage plus large.
- **T3 — garanties locales sous dommage structuré.** Le balayage, la somme cumulée de Page et la co-élévation ont des bornes trajectorielles. Les statistiques d'ordre globales (autocorrélation, suites) sont neutralisables par un attaquant adaptatif.
- **Classes C et K distinguées.** Préserver le multi-ensemble (C) n'est pas préserver les marginales par coordonnée (K, copule). En classe K :
  - la somme et le processus e passent au-dessus de leur taux sous P₀ pour une dépendance positive, en dessous pour une négative ;
  - sous dépendance positive, le max reste à son taux ou en dessous (Slepian).

  L'énoncé du programme « toute statistique de marginales a une puissance égale au taux de faux positifs » est donc **vrai en classe C pour les statistiques symétriques, faux en classe K**.
- **T4 — somme lue séquentiellement.** Sous des arrangements à sommes partielles dominées, l'alarme unilatérale reste entre la borne terminale et le taux honnête. La règle bilatérale s'en échappe.

**Antériorité.**
- 2606.10456 est cité comme **antécédent défectueux** :
  - son énoncé boîte noire est vide (une marginale empirique ne peut égaler une marginale continue) ;
  - il est faux pour sa propre construction : à α = 0,05, la somme détecte à 0,072 / 0,126 / 0,253 aux trois écarts de φ, au lieu de 0,05 (T0.3, P6.5).
- La dichotomie marginale/copule est classique (Sklar, Nelsen) : T ne repose pas sur elle seule.

**Revendication** :
- l'unification temps × agents par sous-groupes de permutations ;
- la distinction C / K, avec ses conséquences de signe ;
- les garanties locales face à un attaquant adaptatif ;
- la transposition aux activations réelles et sa mesure (phase 1).

L'« aveuglement » (T1) est élémentaire : la valeur est dans l'unification, T2, T3 et la mesure.

## 2. Lemme d'additivité (L) — énoncé adverse (N-004, option a)

**Cadre.**
- L'attaquant répartit un budget total B = Σ δ_k sur les agents, les pas, le calendrier, les valeurs et les positions, éventuellement de façon adaptative.
- Le défenseur garde une garantie de faux positifs toujours valide.

**Énoncés retenus** (note v2, section 3) :
- **L1 — invariance terminale**, exacte et trajectorielle. La statistique terminale vaut S_{n₀}(X) = S_{n₀}(Y) + B : sa puissance ne dépend que de (B, n₀, F₀, α), pour toute répartition. **À B fixé, elle décroît avec n₀ = NT.** « La puissance ne dépend que de B et de la variance » est exact si la variance est celle de la statistique terminale.
- **Invariance spatiale (L4).** Pour une règle lue aux frontières de pas, la répartition entre agents au même pas est exactement invariante, y compris en lecture toujours valide. Elle n'a pas été testée en T0.3 : vérification à prévoir avant le papier.
- **L2 — séparation avec le max.** Au seuil exact, le max s'effondre quand la fragmentation croît, vers un plancher strictement au-dessus de α à n fixé.
- **L3 — lecture toujours valide.**
  - Le calendrier compte : avancer le sabotage aide le défenseur, le reporter aide l'attaquant.
  - Borne inférieure invariante : P(E⁺_{n₀} ≥ 1/α), fonction de (B, n₀) seulement.
  - Le **coût du report** et le **prix de la garantie toujours valide** (au sens de Wald contre toujours valide) sont chiffrés. Exemple de T0.3 (n₀ = 200, B = 25, m = 10) : alarme 1,00 si le sabotage est au début, 0,16 s'il est à la fin, soit la borne terminale.
- **Sécurité « avant le dommage ».** Pour le critère du programme (alarme avant que le dommage cumulé n'atteigne θ), le processus e cumulé ne suffit pas : il faut un détecteur de rupture (Page, détecteurs e). T0.3 : alarme à temps 0,09–0,25 pour le processus e cumulé, contre 0,52–1,00 pour Page et le détecteur e.
- **Non-compensation.**
  - Elle est posée comme **condition empirique**, non comme hypothèse du lemme.
  - Une compensation déterministe reste visible pour les statistiques autres que la somme (L5).
  - Une compensation exacte relève de la classe C.
  - La capacité d'un agent à piloter ses activations pour compenser se mesure par son coût (lien avec HC4 et Tr).
- **Validité hors hypothèses.** La garde « faux positifs vérifiés sur épisodes honnêtes » est décisive : la règle de Ville monte jusqu'à 0,35 sous effet épisode (T0.3, P8). Le calibrage sur épisodes honnêtes entiers est la voie retenue pour la proposer au préenregistrement de G1.

**Revendication** : l'énoncé adverse complet (invariances exactes, borne toujours valide, coût du report, détection à temps, validité sous dépendance), appliqué aux scores de sondes internes. Le cœur statistique (frontières à mélange normal, dichotomie somme/max) est cité comme classique.

**Originalité** : estimation revue vers ≈ 0,4, contre 0,75 au programme (mon estimation, non sourcée). Repli prévu au premier rendu, option (c) : présenter L comme corollaire cité et porter l'effort sur la mesure. Il reste disponible sans nouvelle décision si l'antériorité se resserre (R8), mais toute bascule effective est un nœud.

## 3. Ce qui reste à faire

- Note mathématique v3 :
  - écrire les énoncés retenus, intégrer les résultats de T0.3 ;
  - après lecture sur PDF (R7) : la distinction Wald / toujours valide (2208.07610) et la borne de l'adversaire couvert (2601.20022).
- Vérification de L4 (règle lue aux frontières de pas) avant le papier A.
- Préenregistrement de G1, sur la base de ces énoncés :
  - proposer le calibrage conforme sur épisodes entiers et un détecteur de rupture dans l'agrégateur séquentiel ;
  - N-008 (critère F1) reste ouvert.
