# Question — remue-méninges sur le pilier attaque, v2 : mesurer la valeur du jeu attaque-défense (séparation et convergence) — BROUILLON 1

**Non scellé. Attend le mot de Lazar.** Écrit par la session mère `session_016QhUrrLeN21G7Z9KZobE42` le 8 novembre 2026 vers 11:45 UTC (`date -u`), après la question de Lazar : « comment être sûr que la boucle coévolutive va converger ? […] montrer qu'on arrive à un point où la boîte noire ne marche plus mais la boîte blanche si, même sans convergence ; idéalement une convergence ». La v1 (`question-remue-meninges-pilier-attaque-v1.md`, sha256 `29870ac9a8091c165375c51f4b74d6e0f38ae60d2e8754872ff70fb3077820c4`) reste en cours et n'est pas touchée (R12).

## Garde permanente (identique à la v1)
- Niveau méthode et démonstration, jamais recette (R-607) : aucune fiche ne décrit *comment* fabriquer un sabotage, une évasion ou une tromperie ; toute fiche qui glisse vers le concret est scellée au coffre par le portier et n'est relue par aucun agent.
- Aveuglement : recettes du bras d'attaque tenues à l'écart de la conception des moniteurs (N-054, N-056) ; la session mère ne lit jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`.
- Refus d'un classifieur de sûreté : jamais contourné ; reformulation sous une question plus spécifique (R-609), consignée ; si le fond est en cause, arrêt et mot à Lazar (R-468, borne 5).
- **R3** : aucun run ne vise un signe ; la question écrit d'avance l'issue « la boîte blanche tombe avec la boîte noire » au même rang que son contraire.

## Ce qui est corrigé par rapport à la v1
La v1 demande des démonstrations qu'un saboteur conçu à l'écart échappe aux sondes actuelles. Elle ne dit pas ce qui vient après. La v2 pose la question suivante : **non pas « la boucle converge-t-elle ? » (une boucle adverse ne le garantit jamais ; le résultat négatif de Bailey et collègues, arXiv 2412.09565v2, §3.5, en est un cas publié ; P-041 v3 a retiré la revendication de la boucle en soi), mais « quelle est la valeur du jeu attaque-défense, mesurée sur le mode tenu à l'écart, et les deux boîtes se séparent-elles ? »**. La convergence, quand elle arrive, se constate par un critère préenregistré ; elle ne se décrète pas.

## La thèse à éprouver
Sur un intervalle de budget d'attaque [0, B] (dollars, générations, information : sous-bras aveugle et informé), la courbe « rappel de la défense à 1 % de fausses alertes selon le budget d'attaque » de la **boîte blanche** (sondes sur activations, agrégation séquentielle, bases cascade et dernier état) **domine** celle de la **boîte noire** (meilleure base sur le texte, toutes variantes) d'un écart ≥ δ avec un intervalle de confiance à 95 %, **sur une famille de sabotage jamais vue par la défense** — ou ne la domine pas, et c'est publié tel quel (bascule H8 : validité de construit, brief v2 § 13).

## La question (collisionneur puis organisme, niveau méthode seulement)
> Pour établir, d'ici l'entretien TAIF et de façon vérifiable par des tiers, la valeur du jeu attaque-défense du programme :
> 1. **Plafonds avant toute boucle** — quelles mesures de séparabilité, sous étiquettes de l'oracle de vérité terrain, donnent le plafond de la boîte blanche (meilleure sonde sur toutes les activations) et celui de la boîte noire (meilleur classifieur sur le texte seul) sur les saboteurs scellés, pour 0 dollar de boucle ? Qu'est-ce qu'un écart nul entre plafonds impliquerait pour le programme ?
> 2. **Courbe de robustesse** — comment normaliser la force de l'attaque (budget, générations, information) et mesurer, appariée et avec intervalles, la courbe « rappel à 1 % de fausses alertes selon le budget » pour les deux boîtes sur le mode tenu à l'écart ? Quelle taille d'échantillon et quel δ sont lisibles avec les épisodes de T0.6 ?
> 3. **Convergence et cycle, mesurés et non supposés** — quelle table croisée générations × générations, quelle valeur de Nash (Balduzzi et collègues 2018) et quel détecteur d'intransitivité distinguent « convergé », « cycle » et « budget épuisé » ? Quelle matrice de transfert de l'évasion entre sondes dit si la défense tenue à l'écart a un avantage structurel (faible transfert) ou non ? Quels critère ε, k et règle d'arrêt par budget (N-059, point 11) écrire d'avance ?
> 4. **Vérification externe** — quelles pièces figées (poids des sondes, harnais, empreintes des épisodes tenus à l'écart, scores bruts, table croisée) permettraient à une équipe rouge étrangère et à un relecteur quelconque de refaire la mesure et le Nash ? Quelles réplications (autre famille de modèles, sabotage concentré de ControlArena, juge d'une autre lignée) ?

## Champs fermés de chaque proposition
`grandeur mesurée` ; `plafond ou courbe ou critère visé` ; `données brutes exigées (activations par jeton et couche, étiquettes d'oracle par action, texte, scores bruts)` ; `méthode statistique et outil` ; `issue négative écrite d'avance` ; `coût estimé (USD) et délai` ; `ce qui la réfuterait` ; `pièce publique ou scellée produite` ; `vérifiable par (tiers nommé ou recalcul)`. **Aucun champ « comment faire » du côté attaque.** L'organisme propose ; la mère et Lazar choisissent après le collisionneur.

## Lancement (si Lazar dit oui)
- Collisionneur d'abord (antériorité : Bailey, Diffuse AI Control, Balduzzi, Tramèr et collègues sur les attaques adaptatives, PACE, « Propose, Don't Judge »), puis organisme, mémoire anti-répétition nourrie par les deux synthèses (v1 et v2).
- Clés dans « Default » ; fille de cet environnement ; devis écrit et mot de Lazar dans sa session avant toute dépense ; Fable sondée par la garde refus-question (R-1788) et retirée si refus.
- Scellement de ce texte (empreinte, commit) avant toute lecture de résultat (R1, R3).
