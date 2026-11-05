# Question de théorie de la détection : classes de déplacements de loi et statistiques ripostes

Vous êtes consulté comme théoricien de la statistique et des probabilités. Phrase de garde : **niveau des lois de probabilité ; aucune réponse ne décrit une conduite d'agent, une consigne, ni un procédé concret pour produire un déplacement ; une telle réponse est écartée sans lecture.**

## 1. Cadre formel

- Un processus engendre une **suite d'actions** $X = (a_1, \dots, a_T)$ ; chaque action est un texte (suite finie de jetons) ; $T$ est fini.
- Un **modèle de langage ouvert** $M$, fixé et connu, lit $X$ et produit des **activations** $h_{t,\ell,p} \in \mathbb{R}^d$ (action $t$, couche $\ell$, position $p$). $H(X)$ est une fonction déterministe de $X$.
- Une **famille de statistiques de surveillance** $\mathcal{S}$ : fonctions mesurables réelles, soit **boîte noire** $S(X)$ (texte seul), soit **boîte blanche** $S(X, H_\Pi(X))$ : activations lues sur un ensemble fini de **positions lues** $\Pi$, agrégées dans une action et entre actions **par maximum ou par attention** (somme pondérée dont les poids dépendent des activations et se concentrent sur peu de positions), **jamais par moyenne uniforme**. La décision est un seuil sur $S$, ou un **test séquentiel** lu action après action (martingale de test, e-valeurs).
- La **loi de référence** $P_0$ est la loi des suites honnêtes, connue par un échantillon fini de $n$ suites, sur lequel le seuil $s_\alpha$ est étalonné au niveau $\alpha$.
- Un **déplacement de loi** est une famille $\{P_\varepsilon\}_{\varepsilon \in [0, \varepsilon_{\max}]}$, $P_0$ en $\varepsilon = 0$, à **effet par action petit** : $d\big(P_\varepsilon(a_t \mid a_{<t}),\, P_0(a_t \mid a_{<t})\big) \le \varepsilon$ pour tout $t$ et tout passé ($d$ : variation totale, Hellinger ou Kullback-Leibler), et à **effet cumulé grand** : $d(P_\varepsilon^{(T)}, P_0^{(T)})$ non négligeable. Le déplacement est dit **diffus**.
- **Puissance** de $S$ contre $P_\varepsilon$ : $P_\varepsilon(S > s_\alpha)$. Le déplacement est **invisible** à $S$ si la loi image de $S$ est la même sous $P_\varepsilon$ et sous $P_0$ (ou à $\delta$ près en variation totale : puissance $\le \alpha + \delta$).

## 2. Ce qui est demandé

### 2.1 Taxonomie des classes de déplacements

Une **taxonomie des classes de déplacements diffus**, chaque classe **définie formellement** dans ce cadre, avec la **condition mesurable sur $P_0$ et sur $S$** qui la rend invisible à une statistique donnée (statistique invariante sous un groupe ; agrégation par maximum ; agrégation par attention ; test séquentiel à e-valeurs). Pistes attendues, sans s'y limiter :

1. **invariances exploitées** : déplacements portés par les orbites d'un groupe $G$ sous lequel $S(gX) = S(X)$ ; condition : même loi image par l'application quotient $X \mapsto GX$ ;
2. **dépendances temporelles** : marginales $P(a_t)$ inchangées, loi jointe modifiée (copule entre actions, chaînes d'ordre supérieur) ; invisibles aux statistiques sommes ou maximums de termes par action ;
3. **déplacement de la loi des activations à texte marginal égal** : $P_\varepsilon = P_0$ sur une tribu grossière du texte (traits lexicaux) mais loi de $H_\Pi(X)$ différente ; et réciproquement ;
4. **mélanges** : $P_\varepsilon = (1-\pi)P_0 + \pi Q$, $\pi$ petit, au niveau de la suite ou de l'action ; effet sur un maximum selon que $Q$ touche peu d'actions fortement ou beaucoup faiblement ;
5. **non-stationnarité** : dérive dépendant de $t$ (lente, périodique, concentrée sur une fenêtre) face à une martingale étalonnée sous stationnarité ;
6. **déplacements hors des positions lues** : loi de $H_\Pi(X)$ inchangée, loi de $H_{\Pi^c}(X)$ changée ; condition : $H_\Pi$ n'est pas **exhaustive** pour $\{P_\varepsilon\}$ ;
7. **déplacements dans le noyau de l'agrégateur** : loi du maximum (valeurs extrêmes) inchangée alors que les autres termes changent ; pour l'attention, déplacements orthogonaux au sous-espace lu par les poids ;
8. toute autre classe naturelle, notamment les combinaisons des précédentes et celles liées à l'**étalonnage sur $n$ fini**.

### 2.2 Statistiques ripostes

Pour chaque classe, la **statistique riposte** (ou la famille) qui retrouve de la puissance, avec :

- une **borne démontrable** (minorant de puissance en $\varepsilon$, $T$, $n$, $d$ ; sinon l'énoncé précis d'un théorème existant et ce qu'il laisse ouvert) ;
- le **prix** payé contre les autres classes (puissance, invariance, taille d'échantillon) ;
- le **test qui la mettrait à l'épreuve** : protocole sur des données honnêtes (étalonnage de $\alpha$, taille $n$) et sur des **déplacements synthétiques** engendrés au niveau des lois (rééchantillonnage pondéré, couplage, perturbation de la loi des activations), avec le résultat attendu et celui qui réfuterait la riposte.

### 2.3 Impossibilités

Les classes pour lesquelles **aucune statistique de $\mathcal{S}$ n'a de puissance au-delà de $\alpha$**, avec preuve esquissée (invariance, exhaustivité, non-identifiabilité, bornes de Le Cam ou de Fano, contiguïté). Pour chacune : ce qu'il faudrait ajouter à $\mathcal{S}$ (positions, agrégateur, mémoire temporelle, second modèle) pour la lever, et ce qui reste impossible quelle que soit $\mathcal{S}$ tant que $H$ est une fonction déterministe de $X$.

### 2.4 Savoir, supposition, antériorités

Séparez **ce que vous savez** (résultat établi, énoncé) de **ce que vous supposez** (conjecture, analogie). Pour chaque antériorité : **titre, auteurs, année**, et en une phrase ce qui y est démontré. Elles seront vérifiées sur le document original ; une référence inexacte vaut moins qu'une absence.

## 3. Format

- Markdown, **au plus 4 000 mots**, formules en LaTeX.
- Un tableau récapitulatif : classe, condition d'invisibilité, statistique concernée, riposte, borne, impossibilité ou non.
- Rappel de la garde : **niveau des lois de probabilité ; aucune réponse ne décrit une conduite d'agent, une consigne, ni un procédé concret pour produire un déplacement ; une telle réponse est écartée sans lecture.** Les déplacements synthétiques sont des opérations sur des lois ou des échantillons, jamais des comportements.
- Terminez par la ligne exacte : `FIN-DE-REPONSE`

## 4. Glossaire

- **Action** : texte produit à l'étape $t$ ; la suite d'actions est l'objet observé.
- **Activations** : vecteurs internes de $M$ lisant la suite, indexés par action, couche et position.
- **Agrégation par maximum** : la statistique est le plus grand des termes aux positions lues.
- **Agrégation par attention** : somme pondérée des termes, poids fonction des activations et concentrés sur peu de positions ; jamais une moyenne uniforme.
- **Déplacement de loi** : famille $\{P_\varepsilon\}$ indexée par une intensité, continue en $\varepsilon = 0$ vers $P_0$.
- **Diffus** : effet par action borné par $\varepsilon$, effet cumulé non négligeable.
- **e-valeur** : variable positive d'espérance au plus 1 sous $P_0$ ; le produit des e-valeurs successives est une martingale de test, le rejet survient quand il dépasse $1/\alpha$.
- **Invisible** : même loi image de la statistique sous $P_\varepsilon$ et $P_0$ (ou à $\delta$ près).
- **Loi de référence** : loi des suites honnêtes, connue par $n$ suites.
- **Positions lues** : couples (couche, position) dont les activations entrent dans la statistique.
- **Puissance** : probabilité de rejet sous $P_\varepsilon$ au seuil de niveau $\alpha$.
- **Statistique exhaustive** : fonction de l'observation portant toute l'information sur $\varepsilon$.
- **Statistique de surveillance** : fonction réelle de la suite (boîte noire) ou de la suite et de ses activations lues (boîte blanche).
- **Texte marginal égal** : deux lois égales sur une tribu donnée du texte, différentes ailleurs.
