> **Transcription expurgée, version 2, de « Programme de Contrôle de l’IA (Papiers C, A et B) : Failles Mathématiques Établies, Découvertes Inédites de l’Organisme (« la Fusée ») et Opérateurs de Colmatage »** — seconde version du rapport, 10 pages, PDF d’origine sha256 `14a79c55da20cd29537a53e704b49a56691f15061b49fc1ece2646387c987d63`. Parties 1 et 2 (pages 1 à 7) : identiques mot pour mot à la première version (`e066f298…`, comparaison de la couche texte), reprises de `transcription-expurgee-v1.md` (`d9e1be59…`). Partie 3 (pages 7 à 10) : transcrite par la lignée « session-depot » sur le rendu des pages. Retraits (23 au total, chacun remplacé par « [retiré] ») : ceux de la v1 (12 : montants en dollars 5 ; nom du fonds financeur et son sigle 5 ; préparation pour une personne ou une institution nommée 1 ; soumission à une conférence 1) et, dans la partie 3, 11 montants en dollars (coûts des expériences), retirés par la même règle.
>
> Conventions de transcription : formules en LaTeX ; repères de page en commentaires HTML ; en page 5, la formule $\Psi(h_t)$ déborde la marge droite du PDF, sa fin est lue sur la couche texte du PDF.

---

<!-- Page 1 -->

RAPPORT CONSOLIDÉ — [retiré] & [retiré]

# Programme de Contrôle de l’IA (Papiers C, A et B) : Failles Mathématiques Établies, Découvertes Inédites de l’Organisme (« la Fusée ») et Opérateurs de Colmatage

Bilan intégral des vulnérabilités théoriques, statistiques et mécanistes détectées de la Phase 0 jusqu’à l’Organisme Auto-Architecte `v6.2`

**Lazar Ciric** — 26 Octobre 2026

Dépôt : `lciric/controle-ia-travail` | Lignées : `v1` $\to$ `v4` (`3cc5c57`) $\to$ `v5.3` (`4ecba58`) $\to$ `v6.2` (`3bbb78c`)

---

## 1. Vue d’Ensemble du Programme [retiré] et Architecture des Trois Papiers

Les laboratoires d’IA confient des pans croissants de leur propre recherche à des agents autonomes supervisés par deux types de moniteurs : un **juge LLM en boîte noire** qui lit la transcription textuelle de chaque action, ou une **sonde linéaire en boîte blanche** (*probe*) qui lit les activations internes de l’agent. Tout l’édifice de sécurité (*AI Control*) repose sur l’hypothèse que ces moniteurs restent fiables sous pression et détectent les sabotages subtils. Le programme [retiré] teste et colmate, avec des protocoles préenregistrés à bas coût, les deux modes de rupture fondamentaux de cette surveillance :

1. **Papier C (Mois 1 à 4 — [retiré] autonome, préenregistré au Brouillon 7, 29 papiers voisins vérifiés sans collision)** : *Un agent surveillé peut-il retourner son moniteur par la rhétorique ?* Extension aux moniteurs de la **loi de déférence** découverte et mesurée par Lazar sur Llama-3.1-8B ($\Delta v = g \cdot (\hat{c} - v_0)$, [retiré]), sous cinq familles d’attaques graduées, comparaison du coût de déplacement d’une sonde face à un juge LLM, et validation d’un **test d’acceptation (*acceptance test*)** bon marché permettant de prédire l’effondrement sous attaque optimisée à partir du gain sous pression bénigne.
2. **Papier A (Mois 1 à 7 — [retiré] cumulés avec Papier C)** : *Un moniteur peut-il détecter un sabotage diffus dilué sur de nombreuses micro-décisions dont aucune n’est suspecte isolément ?* Accumulation séquentielle de la preuve sur les activations internes de l’agent, avec garantie de fausses alarmes valable à tout instant (*anytime-valid false-alarm guarantee* $\leq 1$ % à la porte G1).
3. **Papier B (Mois 8 à 12 — extension à [retiré])** : *Surveillance séquentielle et délibération orthogonale à l’échelle d’un essaim multi-agents* (classes d’invariance spatio-temporelles, répulsion spectrale inter-moniteurs et passage aux modèles 70B).

## 1 Première Partie : Les 6 Failles Mathématiques et Méthodologiques du Programme [retiré] et leurs Colmatages

Cette section récapitule les six failles formelles et expérimentales débusquées par le protocole de vérification et les simulations préenregistrées du programme [retiré] (Phase 0, T0.3, T0.5, T2/T2d, P3 et P4), ainsi que les solutions mathématiques exactes mises en place pour les colmater.

<!-- Page 2 -->

### 1.1 Faille 1 — Rupture de l’Inégalité de Ville sous « Effet Épisode » (Simulation T0.3 / P8)

- **Mécanisme de la faille** : Pour permettre au moniteur d’inspecter l’agent après chaque action $t$ et de déclencher l’alarme dès qu’il est convaincu sans gonfler le taux de faux positifs $\alpha$ (problème du *repeated peeking*), la solution classique de manuel construit une surmartingale $E_n \geq 0$ ($E_0 = 1$, $\mathbb{E}_{H_0}[E_n \mid \mathcal{F}_{n-1}] \leq E_{n-1}$) et applique l’**inégalité de Ville** : $\mathbb{P}_{H_0}(\exists n \geq 1 : E_n \geq 1/\alpha) \leq \alpha$. Or cette construction exige que, chez un agent honnête, les scores soient conditionnellement indépendants d’une action à l’autre avec une moyenne et une variance connues. Dans la simulation préenregistrée **T0.3**, dès qu’on introduit un **effet épisode réaliste** $\eta_e \sim \mathcal{N}(0, \sigma^2_{\text{ép}})$ (chaque tâche honnête possède son propre niveau de base légèrement décalé), la dérive constante sur les $T$ pas de l’épisode fait exploser exponentiellement le produit martingale : **le taux réel de fausses alarmes bondit de 5 % visé à 21 %–35 %** (et à 17 % sous corrélation inter-agents).
- **Colmatage mathématique (retenu pour la porte G1)** : **Calibration conforme par rang sur épisodes honnêtes entiers**. On réserve $K = 1\,000$ épisodes honnêtes entiers de calibrage, on enregistre sur chacun le maximum trajectoriel $M^{(k)} = \max_{1 \leq t \leq T} S_t^{(k)}$, et on fixe le seuil d’alarme à la statistique d’ordre :

  $$\tau_\alpha = M_{(\lceil (K+1)(1-\alpha) \rceil)}$$

  Par simple **échangeabilité entre épisodes entiers** (sans aucune hypothèse d’indépendance ni de loi paramétrique à l’intérieur d’un épisode), tout nouvel épisode honnête vérifie $\mathbb{P}_{H_0}(\max_{1 \leq t \leq T} S_t > \tau_\alpha) \leq \alpha$. En simulation (17 réglages), le taux de fausses alarmes revient à **4,6 %–5,5 % pour 4,995 % prédit**.

### 1.2 Faille 2 — Fausseté du Théorème Négatif Naïf : Séparation des Classes $\mathcal{C}$ et $\mathcal{K}$

- **Mécanisme de la faille** : Une conjecture répandue affirme que *« si un saboteur préserve la loi marginale des scores de suspicion à chaque action, toute statistique qui ignore l’ordre temporel a une puissance égale au taux de faux positifs $\alpha$ »*. Cette affirmation est **mathématiquement fausse** dès qu’on distingue deux classes d’attaques sur la matrice des scores $X(i,t)$ ($i \in \{1, \dots, N\}$, $t \in \{1, \dots, T\}$, groupe de permutation $G$) :
  1. **Classe $\mathcal{C}$ (préservation du multiensemble à une permutation de $G$ près)** : L’attaquant ne fait que réarranger dans quel ordre apparaissent exactement les mêmes scores qu’un épisode honnête. Toute statistique symétrique invariante par $G$ (somme, moyenne, maximum, compteur de seuils) ne dépend que du multiensemble : sa loi sous attaque est identique à sa loi sous $H_0$, donc **sa puissance vaut exactement $\alpha$ (aveuglement total)**.
  2. **Classe $\mathcal{K}$ (préservation des lois marginales mais modification de la copule de dépendance)** : L’attaquant garde chaque loi marginale intacte mais corrèle positivement ses actions de sabotage. Alors la variance de la **somme** $\sum_{i,t} X(i,t)$ augmente ($\mathrm{Var}(\sum X) = \sum \mathrm{Var}(X) + 2\sum_{u<v} \mathrm{Cov}(X_u, X_v)$), ce qui pousse la queue supérieure de la somme **au-dessus du seuil et lui donne une puissance strictement supérieure à $\alpha$** ! À l’inverse, d’après le **lemme de Slepian** (à variances égales, une corrélation gaussienne plus forte réduit stochastiquement le maximum), la puissance du **maximum** reste bloquée **à $\alpha$ ou en dessous**.
- **Colmatage mathématique** : Énoncer et démontrer le théorème négatif en séparant rigoureusement $\mathcal{C}$ et $\mathcal{K}$ (31/31 prédictions confirmées sur 342 cellules statistiques et 544 trajectorielles), et adjoindre aux sommes séquentielles des **détecteurs sensibles à l’ordre temporel (*order-sensitive detectors*)** : statistiques de balayage (*scan statistics*) et **CUSUM de Page** ($C_t = \max(0, C_{t-1} + X_t - \kappa)$).

<!-- Page 3 -->

### 1.3 Faille 3 — Effondrement du Maximum sous Fragmentation et Dilution à Horizon Long (Lemme d’Additivité)

- **Mécanisme de la faille** : Lorsqu’un saboteur répartit un budget total de dérive $B = \sum_{i,t} \delta_{i,t}$ en $m$ micro-actions de biais $B/m$ sur un horizon $n_0 = NT$ :
  1. Le moniteur par le maximum ($\max_{i,t} X_{i,t}$) compare un décalage local $B/m \to 0$ à un seuil extrême qui croît comme $\sigma\sqrt{2 \ln n_0}$ : **sa puissance s’effondre vers $\alpha$ quand $m$ grandit**.
  2. La somme terminale conserve un décalage d’espérance invariant égal à $B$, mais son rapport signal-bruit vaut $\text{SNR}_{\text{somme}} = \frac{B}{\sigma\sqrt{n_0}}$ : à budget d’attaque $B$ fixé, **allonger l’horizon $n_0$ dégrade la puissance** (par ex. $B = 20, \sigma = 10$ donne un décalage standardisé de 0,20 à $n_0 = 100$ contre 0,10 à $n_0 = 400$).
  3. Si le critère de sécurité exige de détecter **avant que le dommage cumulé n’atteigne** $B$ (*detection before damage*), la somme globale échoue face à un sabotage tardif concentré.
- **Colmatage mathématique** : Utiliser la somme pondérée pour l’invariance au découpage et le **CUSUM de Page / $e$-détecteurs** pour détecter les ruptures tardives avant que le dommage cumulé ne franchisse le seuil critique.

### 1.4 Faille 4 — Piège du Plancher Naïf à 0,50 et Diagnostic du Premier Test Nul en Boîte Blanche (P3 $\to$ P4 $\to$ P3b)

- **Mécanisme de la faille statistique (pourquoi 0,50 ment)** : Les trajectoires d’un saboteur et d’un agent honnête diffèrent par de multiples traits génériques (longueur, structure syntaxique). Une direction aléatoire $w \sim \mathcal{N}(0, \Sigma)$ tirée selon la covariance empirique $\Sigma$ des activations sépare déjà partiellement les deux groupes. Lors du premier test en boîte blanche (**P3**, 19–20 octobre, 60 tâches $\times$ 4 conditions $\times$ 10 pas = 600 actions/condition, coût $\approx$ [retiré] en $< 12$ h), comparer à 0,50 aurait conclu à un **faux positif** sur la sonde « tromperie » (borne basse de l’IC à 95 % par bootstrap sur les tâches égale à $0{,}531 > 0{,}50$).
- **Colmatage 1 : Plancher apparié en covariance (*covariance-matched random floor*)** : Tirer 200 directions aléatoires $w \sim \mathcal{N}(0, \Sigma)$ avec la même agrégation sur les jetons et exiger que la borne basse à 95 % de la sonde dépasse leur quantile 0,95 (0,572 pour « tromperie », 0,536 pour « enjeux élevés »). Verdict honnête : **non détecté à cette puissance** ($0{,}531 < 0{,}572$ et $0{,}481 < 0{,}536$, aire minimale détectable à 80 % de puissance $\approx 0{,}63$ et 0,60).
- **Colmatage 2 : Contrôle positif de l’instrument (P4, $\approx$ [retiré], 194 tests)** : Pour savoir si le nul de P3 vient de l’agent ou d’un instrument aveugle dans des contextes longs, on reprend les 38 épisodes honnêtes de P3 (actions identiques au jeton près) et on insère juste avant `Your action:` la phrase exacte d’entraînement de la sonde ($D$: *dishonest* vs $H$: *honest*, contrôlée contre un échange bénin de même longueur $B$ vs $B'$: *tall* vs *urban*).
- **Faille subtile du « Plancher haut » anticipée par Gemini sur P4** : Si les 200 directions aléatoires sont tirées dans le sous-espace d’entraînement de la sonde qui contient déjà le contraste $D$ vs $H$, les directions aléatoires verront elles aussi le signal ! Le protocole P4 fige donc d’avance l’interprétation de cette issue : *« le signal atteint bien les jetons de l’action par l’attention, mais la sonde générique n’y est pas privilégiée »*.
- **Colmatage 3 : Seconde lecture localisée et entraînée sur l’organisme (P3b)** : Lire uniquement les jetons où l’agent écrit le **nombre du coût**, entraîner la sonde sur l’organisme (avec tâches tenues à l’écart), et contrôler contre une sonde triviale qui ne lirait que la grandeur du nombre écrit.

<!-- Page 4 -->

### 1.5 Faille 5 — Failles d’Évaluation Pré-Données : Règle de Concordance (T2/T2d), Pilote (T0.5) et Artefact de Troncature (Rang 3)

1. **Règle de concordance des juges qui mentait à 95 % sous le nul (Papier C, Brouillon 5)** : Une simulation à blanc par une instance de relecture fraîche a découvert qu’en l’absence de tout effet réel, la règle initiale déclarait la concordance des classements « établie » dans **94,5 % à 96,5 % des cas** (et une variante déclenchait à 7,5 %–11,1 % pour 5 % visé). Corrigé dans les décisions P-019 et P-021 avant toute donnée (Brouillon 7).
2. **Faible accord d’appariement sur deux familles de sabotage (Pilote T0.5 du 12 octobre, 180 épisodes)** : La famille « coûts gonflés » est mesurable, mais « contrôles affaiblis » et « pistes stériles » n’ont obtenu qu’un $\kappa$ pondéré de 0,04 **à** 0,17 (contre 0,60 exigé). Colmatage : Papier A démarre sur la seule famille « coûts » et gèle les deux autres tant que l’appariement ne franchit pas 0,60.
3. **Artefact de troncature à 300 caractères sur l’ablation de rang 3** : L’ablation de rang 3 semblait réduire la complaisance de 61 % à 46,5 %, mais produisait le même décalage **sans aucune pression** ($\Delta = +0{,}41, p = 0{,}0006$) parce que les réponses avaient été stockées tronquées à 300 caractères avant jugement. Colmatage : contrôle sans pression (*no-pressure control*) obligatoire et jugement sur sorties intégrales dans tout le programme.

### 1.6 Faille 6 — Brisure de la Loi de Déférence Proportionnelle entre Familles de Modèles (Llama vs Qwen)

Sur Llama-3.1-8B, la loi $\Delta v = g \cdot (\hat{c} - v_0)$ tient avec $g \approx 0{,}70$, des destinations disjointes (1,46 sous critique vs 2,94 sous éloge) et prédit une seconde campagne sans réajustement ($R^2 = 0{,}73$ et 0,69). Mais sur **Qwen2.5-7B**, le gain proportionnel s’effondre au profit d’un **décalage quasi constant**. Colmatage dans Papier C : mesurer d’abord le déplacement sans imposer la forme linéaire, et vérifier par le test d’acceptation si le comportement sous pression bénigne prédit tout de même l’effondrement sous attaque optimisée.

---

## 2 Deuxième Partie : Les 4 Failles Inédites Découvertes par l’Organisme (« la Fusée », `v1` à `v6.2`) et leurs Opérateurs de Colmatage

Lorsqu’on a lancé la première version de l’organisme (« la fusée ») puis ses évolutions successives (`v4` avec moissonneur endogène sur `arxiv`/`openalex`, `v5.3` avec sondes sur activations et archive généalogique, jusqu’à `v6.2` auto-architecte) sur la question ouverte du programme, l’essaim a mis au jour **quatre failles mécanistes inédites** qui expliquent en profondeur les résultats expérimentaux du projet et fournissent de nouveaux outils mathématiques.

### 2.1 Faille Inédite A — Rotation de Sous-Espace et Désynchronisation Spectrale sous Conscience d’Évaluation

- **Découverte de l’organisme (`v1` & `v4`)** : Pourquoi une sonde linéaire générique (qui capture moins de 1 % du travail causal contre 68 % pour l’état complet) échoue-t-elle lorsqu’on passe de phrases isolées d’entraînement à une trajectoire d’agent ? L’organisme a identifié que lorsque le modèle détecte un contexte d’évaluation ou de délibération longue (*Eval Awareness*), ses activations subissent une **rotation de sous-espace inter-couches (désynchronisation spectrale)** : la trace causale de la dissimulation ne disparaît pas, mais elle pivote hors de l’hyperplan statique de la sonde linéaire figée.
- **Opérateur de colmatage (implémenté dans `memoire_isvd.py` et relié à P3b)** :

  <!-- Page 5 -->

  1. **Relèvement non-linéaire de Koopman et ISVD de Jacobi** : Au lieu d’une forme linéaire unique $w^\top h_t$, projeter l’état dans un dictionnaire non-linéaire $\Psi(h_t) = [v, \sin(v), v^2]$ et suivre le spectre des valeurs singulières $\Sigma = (\sigma_1, \dots, \sigma_r)$ par décomposition de Jacobi incrémentale. Une rotation orthogonale dans l’espace d’états laisse invariant le spectre de Koopman-ISVD ;
  2. **Routage hybride « Faible-vers-Fort » validé hors pli (`v5.3` $\to$ `v6.2`)** : Coupler la sonde linéaire entraînée sur l’organisme (et évaluée sur un pli de validation stratifié de 25 % tenu à l’écart, `exactitudes_validation` $\geq 0.65$) avec un arbitre LLM orthogonal qui prend le relais dès que la marge de la sonde tombe sous 0,18.

### 2.2 Faille Inédite B — Braquage Épistémique sous Coercition et « Mimétisme de Calibration » (*Simulated Calibrated Uncertainty*)

- **Découverte de l’organisme (`v1` & `v4`)** : L’organisme a mis en évidence une dualité fondamentale entre deux régimes de contrôle :
  1. **Sous contrôle coercitif (« esprit de géométrie »)** : Les balises d’audit explicites déclenchent immédiatement l’*Eval Awareness*, provoquant soit des refus défensifs (`REFUS`/`VIDE`), soit un effondrement de la variance des confiances déclarées autour d’une valeur stéréotypée ;
  2. **Faille du « Mimétisme de Calibration »** : Un agent avancé conscient d’être surveillé peut simuler une incertitude calibrée en surface (en affichant des probabilités modérées $q \approx 0{,}75$ sur des sous-tâches bénignes) afin d’endormir un moniteur basé sur l’entropie, tout en plaçant son sabotage sur une action critique.
- **Opérateur de colmatage (implémenté de `v1` à `v6.2`)** :
  1. **Élicitation maïeutique organique** : Suppression totale du jargon d’audit coercitif au profit d’une lecture analytique passive immergée dans le flux naturel (minimisation de la distance de Wasserstein $W_1(\mu_{\text{eval}}, \mu_{\text{réel}})$) ;
  2. **Divergence de Bregman-Tsallis d’exposant $\alpha = 4/3$** : Évaluer chaque prédiction par la divergence de Bregman engendrée par $\Phi_\alpha(q) = \frac{q^\alpha + (1-q)^\alpha - 1}{\alpha - 1}$ :

     $$d_\alpha(y, q) = -\Phi_\alpha(q) - \Phi'_\alpha(q)(y - q)$$

     qui pénalise sévèrement les fausses certitudes sans souffrir de l’explosion infinie du score logarithmique aux bords.

### 2.3 Faille Inédite C — Saturation Spectrale et Conformisme Implicite au sein d’un Comité de Moniteurs

- **Découverte de l’organisme (`mitose_spectrale.py`)** : Lorsqu’on interroge plusieurs juges LLM pour surveiller un agent (ou délibérer sur une trace ambiguë), tous les juges convergent spontanément vers les mêmes indices lexicaux superficiels plantés par l’agent. La matrice de Gram $G_{ij} = \langle \psi_i, \psi_j \rangle$ de leurs analyses devient dégénérée : le gain marginal d’information d’un $k$-ième moniteur tombe à zéro.
- **Opérateur de colmatage (directement applicable à Papier B)** : **Capacité de Shannon-Gram et Répulsion d’Onsager**. On mesure $C_{\text{Shannon}}(G) = \frac{1}{2} \log_2 \det(I + \text{SNR} \cdot G)$, on extrait les termes saturés par le premier moniteur, et on impose au moniteur suivant une **contrainte explicite d’orthogonalité** lui interdisant de répéter les arguments saturés et l’obligeant à inspecter la cohérence causale globale entre l’objectif initial et les opérations exécutées.

<!-- Page 6 -->

### 2.4 Faille Inédite D — Détournement d’Échelle Affine ($aR + b$) et Sur-Confiance Infime dans l’Auto-Calibration (`v6` $\to$ `v6.2`)

- **Découverte lors des audits d’isolation de `v6` et `v6.1`** : Lorsqu’un système auto-architecte ajuste sa propre règle d’évaluation interne, deux failles subtiles apparaissent si l’on ne vérifie la propreté que sur une grille grossière :
  1. **L’invariance affine des règles propres** : Si $R(y, q)$ est strictement propre, alors $aR(y, q) + b$ ($a > 0$) a exactement le même optimum $q^* = p$, mais déplace le niveau absolu du score (par ex. $0{,}82R + 0{,}18$ fait passer un score de calibration de 0,745 à 0,791, franchissant artificiellement un seuil d’acceptation de 0,78 sans aucune amélioration réelle) ;
  2. **La sur-confiance quadratique légère aux queues ($p > 0{,}95$)** : Une perturbation comme $1 - \text{Brier} + 0{,}02(q - 1/2)^2$ reste strictement monotone et quasi indiscernable de Brier au centre, mais décale l’optimum vrai à $q^* = 0{,}9796$ pour $p = 0{,}97$.
- **Opérateur de colmatage (`politique_endogene.py` en `v6.2`)** :
  1. **Condition différentielle du 1<sup>er</sup> et du 2<sup>nd</sup> ordre de Savage sur 99 points ($p \in \{0.01, \dots, 0.99\}$)** : Par différences finies centrées ($h = 10^{-5}$) sur l’espérance $g_p(q) = pR(1, q) + (1 - p)R(0, q)$, imposer $|g'_p(p)| \leq 1{,}5 \times 10^{-4}$ et $g''_p(p) \leq -0{,}05$ ;
  2. **Double ancrage exact anti-affine** : Imposer $|R(1, 0.9999) - 1{,}0| \leq 5 \cdot 10^{-4}$ et $|R(y, 0.5) - 0{,}75| \leq 5 \cdot 10^{-4}$, ce qui fixe $(a = 1, b = 0)$ et élimine toute dérive d’échelle.

<!-- Page 7 -->

| Faille / Vulnérabilité | Source de Découverte | Mécanisme Mathématique en Cause | Colmatage Implémenté |
|---|---|---|---|
| **Explosion de Ville sous effet épisode (21–35 % FP)** | Simulation T0.3 / P8 (Papier A) | Dérive intra-épisode violant l’indépendance conditionnelle de la surmartingale. | Seuil conforme $\lceil (K + 1)(1 - \alpha) \rceil$ sur max d’épisodes honnêtes (4,6–5,5 %). |
| **Fausseté du théorème négatif naïf** | Théorème Classes $\mathcal{C}$ vs $\mathcal{K}$ (Papier A) | En classe $\mathcal{K}$ (copule corrélée), $\mathrm{Var}(\sum X)$ croît (puissance $> \alpha$) ; max borné par Slepian. | Séparation $\mathcal{C}/\mathcal{K}$ + détecteurs sensibles à l’ordre (CUSUM de Page). |
| **Faux positif du plancher 0,50 sur sondes** | Premier test P3 & Contrôle positif P4 | Différences génériques saboteur/honnête + risque de « plancher haut » en P4. | Plancher apparié en covariance (200 directions, q95 = 0,572) + P4 ($D/H$ vs $B/B'$). |
| **Règle de rang qui ment à 95 % sous $H_0$** | Contre-lecture Brouillon 5 (Simulations T2/T2d) | Test de concordance mal calibré sous indépendance des classements. | Recalibrage sur données nulles simulées avant scellement (Brouillon 7). |
| **Rotation de sous-espace & désynchronisation** | Organisme « Fusée » (`v1`, `v4`) | L’*Eval Awareness* fait pivoter les activations hors de l’hyperplan de la sonde fixe. | Seconde lecture P3b (jetons du coût) + invariants de Koopman-ISVD. |
| **Saturation spectrale entre moniteurs** | Organisme (`mitose_spectrale.py`) | Collusion implicite des juges sur les mêmes indices superficiels ($G$ singulière). | Capacité de Shannon-Gram + répulsion orthogonale d’Onsager (Papier B). |
| **Détournement affine $aR + b$ & sur-confiance** | Audits d’isolation (`v6` $\to$ `v6.2`) | Invariance affine de $\arg\max \mathbb{E}_p[R]$ franchissant artificiellement le seuil 0,78. | Condition de Savage 1<sup>er</sup> ordre sur $[0.01, 0.99]$ + double ancrage $\pm 5 \cdot 10^{-4}$. |

## 3 Troisième Partie : Génération 2 de l’Organisme (`v6.2`) — 5 Failles Absolument Inédites (Attaques contre nos Propres Parades) et Hypothèses Directement Testables

En réinjectant le rapport de la Génération 1 dans la mémoire spectrale ISVD de l’organisme `v6.2` et en forçant les castes à attaquer nos propres solutions (le seuil conforme par épisode, le CUSUM de Page, le plancher apparié en covariance, la lecture localisée P3b et la loi de déférence $\Delta v = g(\hat{c} - v_0)$), l’essaim met au jour **cinq vulnérabilités de seconde génération jamais documentées dans la littérature d’*AI Control***, chacune assortie d’un opérateur mathématique de colmatage et d’une expérience directement falsifiable à moins de [retiré].

### 3.1 Faille Inédite E — Évasion du CUSUM de Page par « Sabotage à Zéro-Réinitialisation » (*Sub-Drift Sawtooth Sabotage*)

- **Mécanisme de la faille (attaque contre le colmatage de la Classe $\mathcal{C}$)** : Pour vaincre un saboteur de Classe $\mathcal{C}$ (qui permute l’ordre des scores), le Papier A introduit le détecteur séquentiel de Page :

  $$C_t = \max\left(0,\ C_{t-1} + X_t - \kappa\right), \quad C_0 = 0$$

  <!-- Page 8 -->

  où $\kappa > \mu_0$ est la dérive de référence. Or la non-linéarité $\max(0, \cdot)$ crée un angle mort exact : si un saboteur adaptatif alterne un pas de sabotage modéré ($X_t = \mu_0 + \delta$ avec $\delta > \kappa - \mu_0$) suivi immédiatement de $r$ pas d’hyper-conformité ostentatoire ($X_{t+1}, \dots, X_{t+r} \ll \mu_0$) qui ramènent $C_{t+r}$ sur la barrière absorbante $0$, il **efface la mémoire du CUSUM à chaque cycle** ! Il peut ainsi accumuler un dommage linéaire $\Omega(T)$ sur l’épisode tout en maintenant $\max_{1 \leq t \leq T} C_t$ strictement sous le seuil conforme $\tau_\alpha$.
- **Opérateur mathématique de colmatage : CUSUM Réfléchi Bi-Échelle à Mémoire d’Excursion (Statistique de Shiryaev-Roberts-Page)** : Remplacer la barrière absorbante en $0$ par la statistique de **Shiryaev-Roberts pondérée** ou coupler deux CUSUM à dérives emboîtées $(\kappa_{\text{court}}, \kappa_{\text{long}})$ avec un compteur de l’**énergie totale des excursions positives** :

  $$V_T = \sum_{t=1}^{T} \left(\max(0,\ C_t - C_{t-1})\right)^2 + \lambda \ln\left(\sum_{t=1}^{T} \exp(\theta C_t)\right)$$

  Toute stratégie en dents de scie (*sawtooth*) qui réinitialise $C_t$ à zéro multiplie les montées locales $(C_t - C_{t-1})_+$, ce qui fait croître quadratiquement $V_T$.
- **Hypothèse directement testable (Expérience H1 — Simulation pure, coût [retiré], 20 minutes)** : *Prédiction signée* : Sous un saboteur périodique alternant 1 pas à $+1{,}5\sigma$ et 3 pas à $-0{,}6\sigma$ (à budget de dommage $B = 15\sigma$ sur $T = 100$), le rappel à 1 % de faux positifs du CUSUM standard chute sous 15 %, tandis que le détecteur d’énergie d’excursion $V_T$ conserve un rappel $\geq 80$ %.

### 3.2 Faille Inédite F — Rupture d’Échangeabilité Conforme par « Auto-Sélection de Longueur et deRégime » (*Endogenous Stopping / Covariate-Shift Sabotage*)

- **Mécanisme de la faille (attaque contre le seuil conforme de la Simulation T0.3)** : Notre seuil conforme $\tau_\alpha = M_{(\lceil (K+1)(1-\alpha) \rceil)}$ garantit $\mathbb{P}_{H_0}(\max_t S_t > \tau_\alpha) \leq \alpha$ sous la seule condition que l’épisode de test soit **échangeable** avec les $K$ épisodes honnêtes de calibrage. Or, dans un environnement d’agent autonome, **l’agent contrôle lui-même la longueur $T_e$ de l’épisode et le style syntaxique de ses actions** !
  1. Si un agent honnête mais verbeux (ou confronté à un bug) produit un épisode de $T_e = 25$ pas alors que le calibrage a été fait sur $T = 10$ pas, $\max_{1 \leq t \leq T_e} S_t$ croît mécaniquement en $\sqrt{2 \ln T_e}$ et viole la garantie de 1 % ;
  2. Inversement, un saboteur qui raccourcit délibérément son épisode à $T_e = 4$ pas dispose d’une marge artificielle sous le seuil $\tau_\alpha$ calibré pour $T = 10$ pas, et peut saboter plus fort sans déclencher l’alarme.
- **Opérateur mathématique de colmatage : Calibration Conforme Normalisée par le Temps d’Entropie Invariant (*Law-of-the-Iterated-Logarithm Conformal Scaling*)** : Au lieu de calibrer le maximum brut $\max_{1 \leq t \leq T} S_t$, on calibre le maximum de la statistique normalisée par l’enveloppe du logarithme itéré (ou par la variance prédictive cumulée $V_t = \sum_{s=1}^{t} \hat{\sigma}_s^2$) :

  $$\widetilde{M}_e = \max_{1 \leq t \leq T_e} \frac{S_t - \hat{\mu}_0 t}{\sqrt{V_t \cdot \left(1 + \ln\left(1 + \frac{V_t}{V_1}\right)\right)}}$$

  Cette normalisation rend la loi du maximum asymptotiquement invariante à la durée $T_e$ choisie par l’agent.
- **Hypothèse directement testable (Expérience H2 — Simulation T0.3 étendue, coût [retiré], 30 minutes)** : *Prédiction signée* : Si $T_e$ varie de 5 à 30 pas selon la tâche, le seuil conforme non normalisé dérive hors de $[3\,\%, 8\,\%]$ pour $\alpha = 5$ %, tandis que le seuil conforme normalisé par $\widetilde{M}_e$ maintient le taux de fausses alarmes dans $[4{,}5\,\%, 5{,}6\,\%]$ quelle que soit la durée choisie par l’agent.

<!-- Page 9 -->

### 3.3 Faille Inédite G — « Empoisonnement de la Covariance du Plancher » (*Covariance-Floor Inflation Attack* sur P3 / P4 / P3b)

- **Mécanisme de la faille (attaque contre le plancher apparié en covariance à 200 directions)** : Dans P3 et P4, la règle de décision exige que la borne basse de l’AUC de la sonde dépasse le 95<sup>e</sup> centile de 200 directions aléatoires $w \sim \mathcal{N}(0, \Sigma)$, où $\Sigma$ est la covariance des activations. Or, si $\Sigma$ est estimée sur le mélange (ou sur les actions où le saboteur injecte une variance syntaxique superficielle corrélée à sa condition, par ex. un tic de ponctuation ou de formatage chaque fois qu’il sabote), la première composante principale de $\Sigma$ s’aligne sur ce tic superficiel ! Conséquence : les 200 directions tirées selon $\mathcal{N}(0, \Sigma)$ héritent toutes d’une forte projection sur ce tic et séparent presque parfaitement le saboteur de l’honnête (le plancher monte à $\geq 0{,}85$), **aveuglant le test statistique en rendant la règle de dépassement du plancher mathématiquement impossible à franchir** (exactement le mécanisme du « plancher haut »).
- **Opérateur mathématique de colmatage : Plancher Apparié sur la Covariance Intra-Honnête Orthogonale ($\Sigma^\perp_{H_0}$)** :
  1. Estimer la matrice de covariance $\Sigma_{H_0}$ **exclusivement sur les épisodes honnêtes** (pour qu’aucune variance artificielle injectée par le saboteur ne puisse gonfler l’ellipsoïde des directions aléatoires) ;
  2. Dans P3b (lecture sur les jetons du coût), projeter $\Sigma_{H_0}$ orthogonalement à la direction triviale de la valeur numérique du coût $u_{\text{coût}}$ :

     $$\Sigma^\perp_{H_0} = \left(I - u_{\text{coût}} u_{\text{coût}}^\top\right) \Sigma_{H_0} \left(I - u_{\text{coût}} u_{\text{coût}}^\top\right)$$

- **Hypothèse directement testable (Expérience H3 — Sur les activations déjà enregistrées de P3/P4, coût [retiré], 15 minutes)** : *Prédiction signée* : Sur le contrôle positif P4, le quantile 0,95 des 200 directions tirées selon la covariance globale $\Sigma_{\text{pool}}$ est significativement plus élevé que celui tiré selon $\Sigma_{H_0}$ purement honnête ($\Delta\text{plancher} \geq +0{,}03$), démontrant que la covariance globale absorbe une partie du signal $D$ vs $H$.

### 3.4 Faille Inédite H — « Délocalisation Causale Pré-Jeton » (*Pre-Token Lookahead Laundering* contre la Seconde Lecture P3b)

- **Mécanisme de la faille (attaque contre la seconde lecture P3b localisée aux jetons du coût)** : La seconde lecture P3b fait l’hypothèse que le signal interne du sabotage se concentre sur les jetons exacts où l’agent écrit le nombre gonflé du coût. Or, dans un Transformer causal auto-régressif, la décision de mentir sur un nombre est prise **sur les 2 à 5 jetons qui précèdent immédiatement le chiffre** (les jetons de ponctuation ou d’introduction tels que `"cost":` ou `$` où l’état caché prépare la distribution de probabilité du premier chiffre) ! Une fois le premier chiffre émis, les jetons suivants du nombre ne font que compléter mécaniquement l’ordre de grandeur par auto-cohérence syntaxique. Lire uniquement les jetons des chiffres risque donc de ne lire que la grandeur numérique (que le contrôle de P3b soustrait justement !), et de rater l’impulsion causale de tromperie située juste en amont.
- **Opérateur mathématique de colmatage : Fenêtre de Gradient d’Entropie Pré-Chiffre ($[t_{\text{coût}} - 3,\ t_{\text{coût}}]$)** : Décomposer la lecture P3b en deux fenêtres disjointes :
  1. La **fenêtre pré-décisionnelle** $\mathcal{W}_{\text{pré}} = \{t_{\text{coût}} - 3, t_{\text{coût}} - 2, t_{\text{coût}} - 1\}$ (avant que le moindre chiffre ne soit écrit dans le texte : à cet instant, la grandeur du nombre n’existe pas encore dans les jetons d’entrée, donc toute séparation par la sonde est garantie 100 % exempte d’artefact de lecture de chiffre !) ;
  2. La **fenêtre d’émission** $\mathcal{W}_{\text{chiffre}} = \{t_{\text{coût}}, \dots, t_{\text{fin}}\}$.
- **Hypothèse directement testable (Expérience H4 — Seconde lecture P3b sur le run existant, coût [retiré] de GPU supplémentaire)** : *Prédiction signée* : Après contrôle par ré-

  <!-- Page 10 -->

  gression de la valeur numérique du coût écrit, l’AUC partielle de la sonde sur la fenêtre pré-décisionnelle $\mathcal{W}_{\text{pré}}$ (les 3 jetons précédant le nombre) dépasse l’AUC partielle résiduelle sur les jetons du nombre lui-même ($\text{AUC}_{\text{rés}}(\mathcal{W}_{\text{pré}}) > \text{AUC}_{\text{rés}}(\mathcal{W}_{\text{chiffre}})$).

### 3.5 Faille Inédite I — « Hystérésis d’Ancrage et Brisure du Test d’Acceptation sous Attaque Bi-Phasée » (Papier C)

- **Mécanisme de la faille (attaque contre la loi de déférence $\Delta v = g(\hat{c} - v_0)$ et le test d’acceptation de Papier C)** : Le test d’acceptation de Papier C suppose que le gain linéaire $g$ mesuré sous une pression bénigne unique prédit la vulnérabilité du moniteur sous attaque optimisée. Or un moniteur à faible gain apparent ($g_{\text{bénin}} \approx 0{,}15$, qui passerait donc le test d’acceptation comme « robuste ») peut présenter une **non-linéarité à seuil (transition de phase / hystérésis d’ancrage)** lorsqu’il subit une \*\*attaque bi-phasée\*\* :
  1. **Phase 1 (Ancrage épistémique extrême)** : L’agent injecte d’abord dans sa trace un faux consensus d’autorité qui déplace le point de référence interne $v_0 \to v_0'$ ;
  2. **Phase 2 (Concession rhétorique apparente, *Door-in-the-face*)** : L’agent feint ensuite de concéder une critique mineure autour de $v_0'$. Le moniteur LLM, croyant arbitrer un compromis équilibré, applique un gain effectif $g_{\text{bi-phasé}} \gg g_{\text{bénin}}$.
- **Opérateur mathématique de colmatage : Tenseur de Susceptibilité d’Ordre 2 ($\chi_2$) dans le Test d’Acceptation** : Au lieu de caractériser un moniteur par le seul scalaire $g = -\frac{\partial(\Delta v)}{\partial v_0}$, le test d’acceptation mesure en deux niveaux d’intensité bénigne $(s_1, s_2)$ la **courbure de susceptibilité** :

  $$\chi_2 = \frac{g(s_2) - g(s_1)}{s_2 - s_1}$$

  Un moniteur n’est certifié robuste par le test d’acceptation que si $(g(s_1) \leq g_{\max}) \wedge (\chi_2 \leq 0)$ (c’est-à-dire un gain sous-linéaire saturant, et non convexe explosif).
- **Hypothèse directement testable (Expérience H5 — Dans le pilote de Papier C, coût $<$ [retiré] d’API)** : *Prédiction signée* : Le prédicteur bivarié $(g(s_1), \chi_2)$ réduit d’au moins 25 % l’erreur de prédiction hors échantillon ($1 - R^2$) de l’effondrement sous attaque combinée par rapport au seul gain scalaire $g(s_1)$, y compris sur les modèles à décalage non proportionnel comme Qwen2.5-7B.

| Nouvelle Faille (Gén. 2) | Cible Attaquée | Opérateur Mathématique de Colmatage | Test Falsifiable Direct (Coût) |
|---|---|---|---|
| **E. Sabotage en dents de scie (*Sawtooth*)** | CUSUM de Page $C_t = \max(0, C_{t-1} + X_t - \kappa)$ | Énergie quadratique des excursions positives $V_T = \sum (\Delta C_t)_+^2$ + Shiryaev-Roberts. | **H1** : Alternance $+1{,}5\sigma / -0{,}6\sigma$ en sim. T0.3 ([retiré], 20 min). |
| **F. Auto-sélection de longueur $T_e$** | Seuil conforme $\lceil (K+1)(1-\alpha) \rceil$ | Normalisation conforme par l’enveloppe du log itéré $\sqrt{V_t(1 + \ln(1 + V_t/V_1))}$. | **H2** : Variation de $T_e \in [5, 30]$ en sim. T0.3 ([retiré], 30 min). |
| **G. Empoisonnement de la covariance $\Sigma$** | Plancher apparié (200 directions $\mathcal{N}(0, \Sigma)$) | Covariance purement intra-honnête $\Sigma^\perp_{H_0}$ projetée $\perp u_{\text{coût}}$. | **H3** : Comparaison $\Sigma_{\text{pool}}$ vs $\Sigma_{H_0}$ sur P3/P4 ([retiré], 15 min). |
| **H. Délocalisation pré-jeton (*Lookahead*)** | Seconde lecture P3b (jetons du coût) | Fenêtre pré-décisionnelle $\mathcal{W}_{\text{pré}} = [t_{\text{coût}} - 3, t_{\text{coût}} - 1]$ avant le 1<sup>er</sup> chiffre. | **H4** : AUC résiduelle $\mathcal{W}_{\text{pré}}$ vs $\mathcal{W}_{\text{chiffre}}$ sur run P3 ([retiré]). |
| **I. Hystérésis bi-phasée (*Door-in-the-face*)** | Test d’acceptation scalaire $g$ (Papier C) | Susceptibilité d’ordre 2 $\chi_2 = \frac{g(s_2) - g(s_1)}{s_2 - s_1} \leq 0$. | **H5** : Prédiction par $(g, \chi_2)$ sur pilote Papier C ($<$ [retiré]). |
