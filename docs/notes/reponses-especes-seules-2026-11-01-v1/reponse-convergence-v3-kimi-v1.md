## Portée

Les pièces établissent un fait local et précis, mais plus limité que « la défense ne converge pas » : dans le pilote, A ne progresse pas et présente des retours de déplacements au-delà de la référence d’échangeabilité. À T = 8, I1 vaut +0,0020 et −0,0005 ; I3 vaut 0,9028 et 0,9444 contre une référence de 0,7345, soit des écarts de +0,1683 et +0,2099 (pièce 1, § Prédiction A et § Métrique ; pièce 2, § 4 ; pièce 4, § 3.5). Ces indicateurs ne mesurent ni la périodicité, ni la convergence des fréquences empiriques, ni l’exploitabilité.

Le point théorique central est le suivant : **A n’est pas le jeu fictif de Robinson–Brown. C’est une dynamique asymétrique de meilleures réponses approchées, avec mémoire historique côté défenseur et mémoire d’un seul tour côté attaquant.** Les théorèmes de convergence du jeu fictif ne lui sont donc pas directement applicables.

---

# 1. Formalisation

## 1.1 Le noyau de jeu effectivement codé

On peut écrire le noyau statique ainsi :

- **Défenseur** : un moniteur \(m\), ou une loi de mélange \(p\) sur des moniteurs.
- **Attaquant** : un paramètre \(\theta\in\Theta_\delta\), dans une boîte compacte et sous une contrainte de distance à la loi cible.
- **Gain du défenseur** :
  \[
  U(m,\theta)=\Pr_{x\sim Q_\theta}\!\left[s_m(x)>t_m\right],
  \]
  où \(t_m\) est calibré sur la loi propre pour viser le taux de fausses alertes \(\alpha\).
- **Gain de l’attaquant** : \(-U\), si l’on choisit explicitement une forme à somme nulle.
- **Défense mixte** :
  \[
  U(p,\theta)=\sum_i p_iU(m_i,\theta).
  \]

C’est bien la structure employée dans la matrice restreinte de B et B′ : lignes = moniteurs, colonnes = attaques, valeur = détection, programme linéaire à somme nulle (pièce 3, `resoudre_jeu`, `taux_defense`, `trajectoire` ; pièce 1, § Métrique).

Mais le **jeu dynamique complet** n’est pas ce simple jeu matriciel :

1. A déploie un moniteur pur.
2. L’attaquant calcule une meilleure réponse approchée contre ce moniteur.
3. A ré-entraîne contre le mélange uniforme de toutes les attaques passées.
4. B et B′ résolvent un méta-jeu restreint, puis entraînent un nouveau moniteur contre une stratégie adverse d’équilibre.
5. L’évaluation finale fige la défense, puis laisse encore l’attaquant répondre.

C’est le schéma de `trajectoire` et `phase_finale` (pièce 3 ; pièce 1, § Plan d’analyse 2 et § Métrique). Le jeu complet serait donc plutôt un jeu extensif dont les stratégies sont des **politiques dépendant de l’historique**. A est une telle politique fixée ; ce n’est pas une recherche d’équilibre dans ce jeu extensif.

### Règle de A, sous forme idéalisée

En ignorant les erreurs d’optimisation :

\[
m_t\in\arg\max_{m\in\mathcal M}
\frac1{|H_t|}\sum_{a\in H_t}U(m,a),
\qquad
a_{t+1}\in\arg\min_{a\in\Theta_\delta}U(m_t,a).
\]

Cela ressemble à du jeu fictif **côté défenseur seulement**. L’attaquant ne best-répond pas à la distribution empirique des défenses passées, mais à la dernière défense.

## 1.2 Ce qui manque pour appliquer un théorème

Il faudrait ajouter explicitement :

- si l’objet analysé est le noyau statique, le méta-jeu restreint ou le jeu dynamique complet ;
- si les meilleures réponses sont globales, locales ou seulement approchées, et avec quelle erreur ;
- les règles de départage entre meilleures réponses ;
- si la convergence porte sur le dernier itéré, les fréquences empiriques, les gains moyens ou la politique déployée ;
- si le gain théorique est la détection dure ou le surrogate lissé utilisé pendant l’entraînement ;
- si le calibrage du seuil est considéré comme exact ;
- si les mélanges continus de moniteurs sont autorisés, ou seulement les mélanges finis sur les moniteurs déjà produits.

Dans le code, l’attaquant est un optimiseur local multi-départs et la valeur finale retient la plus faible détection obtenue par deux recherches ; ce n’est pas une preuve de meilleure réponse globale (pièce 3, `meilleure_reponse`, `phase_finale`). Le défenseur optimise également un objectif approché, avec échantillonnage fini et approximation du seuil ; pour les moniteurs non linéaires, l’approximation gaussienne du seuil est déclarée approchée (pièce 3, `objectif_detection`, `entrainer`).

## 1.3 Somme nulle, stratégies finies et mélanges continus

| Régime | Résultat applicable |
|---|---|
| Jeu fini à deux joueurs, somme nulle, **jeu fictif des deux côtés** | Robinson établit la convergence au sens des valeurs et des stratégies empiriques approchant l’équilibre ; cela ne garantit pas le dernier coup [1, 2]. |
| Jeu fini général | Aucune convergence générale du jeu fictif ; l’exemple de Shapley est hors de la garantie générale de Robinson [3]. |
| **Un seul côté** joue le jeu fictif, l’autre best-répond au dernier itéré | Aucun théorème général de convergence ne suit des seules hypothèses « fini » et « somme nulle ». |
| Meilleure réponse pure dans un jeu à équilibre entièrement mixte | Le dernier itéré peut cycler indéfiniment, même lorsque les moyennes empiriques du jeu fictif complet convergent. |
| Stratégies continues | La preuve finie de Robinson ne se transporte pas automatiquement. Il faut des hypothèses supplémentaires de compacité, continuité, convexité-concavité ou monotonie, et un théorème adapté. |
| Deux joueurs sans regret | Dans un jeu à somme nulle, les profils moyens deviennent approximativement d’équilibre ; cela ne dit toujours rien du dernier moniteur [9]. |

Ainsi, « somme nulle » ne suffit ni à faire converger le dernier itéré, ni à faire converger la variante asymétrique de A.

## 1.4 Ce que change l’oracle « détection à fausses alertes fixées »

Cet oracle choisit un point de la courbe de compromis détection/fausses alertes, plutôt qu’une perte logistique classique.

Trois conséquences :

1. **Le seuil fait partie de la stratégie déployée.** Changer le moniteur change aussi son seuil. Le gain n’est donc pas une fonction bilinéaire des paramètres du score.
2. **Le surrogate d’entraînement n’est pas le gain évalué.** Une convergence de l’objectif lissé n’implique pas une convergence de la détection dure.
3. **Une meilleure réponse à un mélange uniforme n’est pas une réponse minimax.** Maximiser la détection moyenne sur l’historique peut accepter une détection très faible sur certaines attaques de l’historique, notamment les plus récentes.

Pour les mélanges randomisés de moniteurs, détection et fausses alertes sont linéaires dans les poids. En revanche, une agrégation déterministe suivie d’un recalibrage, comme les témoins « ou », ne se réduit pas à cette linéarité (pièce 3, `ou_deterministe`, `MoniteurOu` ; pièce 1, § Métrique).

## 1.5 La métrique de convergence appropriée

Avec la convention « défenseur maximise, attaquant minimise », une définition possible est :

\[
\operatorname{NashConv}(p,q)=
\underbrace{\max_{p'}U(p',q)-U(p,q)}_{\text{gain possible du défenseur}}
+
\underbrace{U(p,q)-\min_{q'}U(p,q')}_{\text{gain possible de l’attaquant}}.
\]

Certaines conventions divisent cette somme par deux ; il faut donc déclarer la convention.

| Mesure | Ce qu’elle établit | Ce qu’elle n’établit pas | Lecture sur de vraies sondes |
|---|---|---|---|
| **NashConv / exploitabilité** | Distance opérationnelle à un équilibre, si les meilleures réponses et le jeu sont bien spécifiés | Rien de global avec des optimiseurs seulement locaux | Calculable exactement seulement dans un méta-jeu restreint ; sinon estimation dépendante de la classe de recherche |
| **Valeur de sécurité d’une défense**, \(\min_q U(p,q)\) | Performance après réponse adverse | Ne mesure pas à elle seule l’écart à la valeur du jeu | Estimable sur des attaques observées et une classe d’optimisation déclarée, sans certificat hors de cette classe |
| **I1, progrès d’un tour à l’autre** | Stagnation ou amélioration de la trajectoire mesurée | Non-convergence, équilibre ou cycle | Directement mesurable, mais sensible au plancher de détection |
| **I3, retours** | Récurrence géométrique dans un espace de déplacements | Périodicité, NashConv, divergence | Difficile à transposer sans métrique canonique sur les attaques |
| **Distance aux moniteurs passés** | Stabilité de la défense | Convergence stratégique | En paramètres, fragile aux permutations et rescalings ; une distance fonctionnelle est plus interprétable |
| **H / rétention / I2** | Conservation de la détection sur l’historique | Ne distingue pas oubli et saturation dans les pièces | Utile comme diagnostic, pas comme métrique d’équilibre |
| **Regret externe** | Écart moyen à la meilleure défense fixe rétrospective | Robustesse du dernier moniteur ou équilibre | Mesurable sur la séquence observée, sans connaître l’équilibre |

Sur des sondes réelles, **NashConv reste la métrique qui répond à la question théorique**, mais seulement dans un jeu restreint explicitement défini. Sur la séquence réellement observée, la valeur de sécurité estimée, le regret, la rétention et le calibrage sont mesurables ; aucun ne fournit seul un certificat global.

Enfin, la valeur nulle de I3 suppose une forme d’échangeabilité des déplacements. Or le code utilise notamment l’attaque précédente comme départ de la recherche suivante, ce qui introduit une dépendance temporelle : 0,7345 est une référence conditionnelle, pas une loi nulle universelle (pièce 3, `trajectoire`, `meilleure_reponse`, `valeur_nulle_I3`).

---

# 2. Pourquoi cela peut cycler

## 2.1 Le résultat connu le plus proche

Il faut distinguer quatre phénomènes :

1. **Meilleure réponse pure itérée dans un jeu cyclique.** À équilibre entièrement mixte, le dernier itéré ne peut pas s’installer sur un équilibre pur. Des récurrences ou cycles sont alors naturels.
2. **Jeu fictif complet.** Les fréquences empiriques peuvent converger alors même que les actions pures continuent de changer. Il n’y a donc aucune contradiction entre « retours du dernier itéré » et « convergence des moyennes ».
3. **Descente-montée de gradient.** Sur des jeux bilinéaires ou non convexes, le dernier itéré peut tourner ou diverger alors que la moyenne se comporte mieux. Les méthodes optimistes et extragradient répondent à ce problème sous des hypothèses précises [5, 6].
4. **Apprentissage séquentiel avec oubli.** L’oubli peut ramener le défenseur vers des états antérieurs, mais ce n’est ni nécessaire ni suffisant pour un cycle stratégique [10, 11].

L’exemple de Shapley concerne la non-convergence du jeu fictif dans une classe où la garantie de Robinson ne s’applique pas ; il ne réfute pas la convergence du jeu fictif complet en somme nulle finie [1, 3]. Les résultats de récurrence de l’apprentissage régularisé offrent également une analogie de mécanisme, pas un théorème directement applicable à A [4].

## 2.2 Pourquoi la règle historique de A ne supprime pas le cycle

Les quatre explications candidates n’ont pas le même statut.

### a. L’asymétrie des règles de mise à jour — explication structurelle principale

Le défenseur répond à une moyenne historique ; l’attaquant répond au dernier moniteur. La condition essentielle du jeu fictif de Robinson — la construction coordonnée des réponses aux distributions empiriques des deux côtés — est absente.

La part d’une nouvelle attaque dans l’objectif uniforme décroît avec la taille de l’historique. La défense peut donc rester proche d’un compromis ancien, tandis que la réponse adverse change immédiatement.

**Ce qui réfuterait cette attribution** : dans une version finie discrétisée du jeu, avec meilleures réponses exactes, la variante asymétrique et le jeu fictif complet présenteraient le même comportement de NashConv moyen et de dernier itéré. L’asymétrie ne suffirait alors pas à expliquer l’observation.

### b. Le mélange uniforme — facteur possible, non démontré comme cause

Uniforme, pondéré par récence ou pondré par difficulté définissent trois objectifs différents. Aucun ne coïncide nécessairement avec l’objectif minimax.

Mais remplacer l’uniforme par une pondération ne crée pas, à lui seul, une garantie de convergence dans la dynamique asymétrique.

**Réfutation minimale** : si une large famille de pondérations produit les mêmes retours et la même stagnation à meilleures réponses exactes, le caractère uniforme n’est pas la cause suffisante.

### c. La classe linéaire — facteur de plafond et d’existence d’équilibre

Une classe pauvre peut imposer un compromis entre plusieurs régions et empêcher l’existence d’un bon moniteur pur. Une classe plus riche peut rendre un équilibre pur ou presque pur possible.

Elle n’est cependant pas une explication universelle : une classe riche peut encore avoir un équilibre mixte et des meilleures réponses cycliques. À l’inverse, une classe linéaire peut converger dans un jeu strictement dominé ou contractant.

Les pièces montrent justement un effet de classe : les poids de B′ sont purs sur 17 tâches sur 24 puis 14 sur 24, et cette pureté est forcée par le jeu restreint sur toutes les tâches pures, respectivement 17/17 et 14/14 (pièce 2, § 4 ; pièce 1, résumé 5). Cela établit un plafond local de classe, pas une loi générale.

### d. La mesure — elle peut appeler « cycle » ce qui n’est pas non-convergence

I3 mesure des retours géométriques. Il ne dit pas si les fréquences empiriques convergent. I1 peut être plat parce que la défense est déjà au plancher, parce que l’évaluation est bruitée ou parce que l’horizon est court.

Au δ haut, V(A) vaut 0,0359 au pilote, soit environ 3,6 α ; les pièces déclarent elles-mêmes que « ne progresse pas » y discrimine peu (pièce 1, résumé 6 et Table 5 ; pièce 2, § 4).

**Réfutation de la lecture “non-convergence”** : monitors fonctionnellement stables et NashConv des fréquences empiriques décroissant vers zéro, alors même que I3 reste élevé. Cela signifierait que les attaques reviennent, mais que la défense moyenne converge.

## 2.3 Quand le cycle est-il inévitable ?

Une proposition limitée mais propre est disponible :

- supposons des meilleures réponses exactes ;
- supposons que le couple défense/attaque se stabilise sur des points fixes ;
- alors l’historique finit par décrire la même attaque, et le point fixe doit être une meilleure réponse mutuelle pure.

**S’il n’existe aucun équilibre pur**, cette stabilisation est impossible. Cela exclut la convergence vers un point fixe pur, mais n’impose pas un cycle périodique : la trajectoire peut être récurrente, irrégulière ou chaotique.

Le cycle n’est pas inévitable lorsque, par exemple :

- un équilibre pur atteignable existe et la dynamique y est contractante ;
- le jeu possède une structure de dominance ou de potentiel compatible avec la règle ;
- les deux joueurs emploient une dynamique pour laquelle un théorème de convergence s’applique ;
- la classe de défense permet une réponse robuste pure et l’oracle la retrouve effectivement.

Le bruit peut supprimer une périodicité exacte sans supprimer l’exploitabilité. Une classe de fonctions plus riche peut supprimer le cycle sans garantir une meilleure généralisation. L’oubli peut entretenir les retours, mais un cycle purement géométrique peut exister sans aucun oubli.

---

# 3. Mécanismes de convergence : validité, prix et réfutation minimale

## (a) Meilleure réponse à l’historique — déjà la règle de A

**Condition de convergence reconnue.** Jeu fini à somme nulle, meilleures réponses suffisamment exactes, et surtout **jeu fictif des deux côtés** pour la garantie classique de Robinson [1, 2]. La convergence porte sur les moyennes, pas sur le dernier moniteur.

**Pourquoi A peut malgré tout cycler.** L’attaquant ne joue pas le jeu fictif ; l’objectif uniforme n’est pas minimax ; les oracles sont approchés ; le gain réel n’est pas nécessairement concave-convexe ; la mesure porte sur le dernier itéré.

**Prix.** Stockage de l’historique, ré-entraînement répété, adaptation de plus en plus lente aux attaques récentes, aucune garantie sur la défense pure finalement déployée.

**Test le moins cher.** Discrétiser le jeu en une matrice finie, rendre les meilleures réponses exactes et comparer : A asymétrique, jeu fictif complet, et A avec d’autres pondérations. Si le jeu fictif complet ne fait pas décroître l’exploitabilité moyenne dans ce cadre, l’implémentation ou la formalisation est en cause. Si A converge aussi dans ce jeu particulier, on ne peut pas lui attribuer une non-convergence générale.

## (b) Double oracle / PSRO

**Condition.** Pour le double oracle classique : stratégies finies sous-jacentes, somme nulle, meilleures réponses capables de trouver toute stratégie améliorante, méta-jeu résolu exactement. L’arrêt avec certificat exige qu’aucune stratégie nouvelle ne puisse améliorer le joueur concerné [7]. PSRO généralise ce schéma à des méta-solveurs et à des réponses approchées, mais hérite de leurs erreurs [8].

**Prix.** Croissance de la méta-matrice, stockage des moniteurs, calculs croisés de détection, résolution répétée du méta-jeu. Une mixture peut aussi diluer un moniteur récent performant. Les mélanges réduisent le coût par requête mais pas nécessairement le stockage.

**Limite visible dans les pièces.** B et B′ sont tronqués ; l’écart « valeur du jeu restreint − V » vaut +0,019/+0,024 pour B et +0,004/+0,004 pour B′. Ce ne sont pas des certificats d’équilibre du jeu complet (pièce 1, § Ce que l’expérience n’autorise pas).

**Test le moins cher.** Sur une version finie du même jeu, exécuter le double oracle jusqu’au certificat « aucune stratégie améliorante », puis vérifier indépendamment la valeur et l’exploitabilité. Si le certificat restreint est obtenu mais que la défense déployée reste très exploitable par l’évaluation principale, l’écart vient de l’oracle, du calibrage ou de la différence entre méta-jeu et jeu réel.

## (c) Régularisation vers les moniteurs passés

Cela couvre la distillation fonctionnelle, les pénalités de distance, la moyenne de poids et l’entropie sur les poids.

**Condition.** Pour réduire l’oubli : tâches suffisamment proches, paramétrisation alignée et optimisation dans un même bassin. Pour la moyenne de poids, les symétries de permutation et d’échelle doivent être traitées. Aucune de ces méthodes ne donne à elle seule une convergence de Nash [11, 12].

**Prix.** Perte de plasticité, adaptation plus lente aux attaques récentes, conservatisme. L’entropie peut produire des poids non purs sans créer de valeur stratégique supplémentaire : elle peut masquer la pureté plutôt que rendre le mélange utile.

**Test le moins cher.** Mesurer séparément la rétention H et l’exploitabilité finale. Si la régularisation améliore fortement H sans changer NashConv ni la valeur de sécurité, l’hypothèse « l’oubli cause le cycle » est réfutée comme explication suffisante. Si elle ne change même pas H dans le régime étudié, son efficacité pratique est réfutée dans ce régime.

## (d) Gradients optimistes / extragradient

**Condition.** Noyau différentiable, domaines convexes-compacts, structure convexe-concave ou opérateur monotone lipschitzien, gradients contrôlés et pas adaptés. Les résultats de dernier itéré ne couvrent pas automatiquement le jeu neuronal général [5, 6].

**Obstacle ici.** Détection dure non différentiable, seuil dépendant du moniteur, non-convexité des deux côtés, meilleures réponses locales. Faire converger le surrogate ne suffit pas à faire converger la détection au seuil.

**Prix.** Extragradient ajoute des évaluations de gradient ; les deux méthodes ajoutent une sensibilité aux pas et aux projections.

**Test le moins cher.** Vérifier d’abord le dernier itéré sur un jeu bilinéaire témoin. Puis comparer, dans le jeu synthétique, convergence du surrogate et NashConv du gain dur. Si le surrogate converge tandis que la détection dure reste inchangée, le transfert du théorème au véritable objectif est réfuté.

## (e) Élargir la classe de fonctions du défenseur

**Condition.** La nouvelle classe doit contenir une défense pure ou presque pure de bonne valeur de sécurité, et l’oracle doit pouvoir la trouver. Si la limitation est informationnelle plutôt que fonctionnelle — distributions trop recouvrantes au taux de fausses alertes imposé — aucune capacité ne supprime ce plafond.

**Prix.** Entraînement et calibrage plus coûteux, surapprentissage de l’historique, stockage et évaluation accrus. Une classe plus riche peut aussi augmenter la complexité stratégique au lieu de la réduire.

**Test le moins cher.** Employer des classes emboîtées, à distribution d’entraînement et budget déployé contrôlés, sur deux familles de tâches : équilibre pur connu et équilibre intérieur connu. Si la classe riche conserve un équilibre strictement mixte et que le dernier itéré continue de cycler avec des oracles exacts, « la capacité guérit le cycle » est réfuté dans cette famille.

## (f) Changer l’objectif : pire cas historique, regret, robustesse distributionnelle

**Pire cas sur l’historique.** Il protège contre le pire élément du support historique, pas contre une nouvelle attaque hors de ce support. Son exacte résolution peut toujours laisser une dynamique cyclique lorsque de nouvelles colonnes entrent dans le jeu.

**Robustesse distributionnelle.** Le certificat vaut uniquement dans l’ensemble d’incertitude déclaré ; sa validité exige que cet ensemble couvre le changement de distribution pertinent et que l’optimisation minimax soit effectivement résolue [14].

**Sans regret.** Donne une garantie sur la performance moyenne et sur la meilleure défense fixe rétrospective. Il ne donne pas une garantie sur le dernier moniteur [9].

**Prix.** Conservatisme, baisse possible de la détection moyenne ou des cas récents, coût de l’adversaire interne et de la résolution du pire cas.

**Test le moins cher.** Séparer la robustesse **à l’intérieur** de l’ensemble historique/d’incertitude de la robustesse à la réponse finale. Si la première est obtenue mais pas la seconde, le problème est la couverture de l’ensemble, pas la preuve du solveur. Si la première elle-même échoue, l’oracle minimax est insuffisant.

## (g) Déployer une moyenne issue d’un algorithme sans regret

C’est distinct de ré-entraîner un moniteur unique : la sortie est une distribution sur un ensemble fini de moniteurs.

**Condition.** Gains bornés, ensemble de références déclaré, mise à jour effectivement sans regret. Avec deux joueurs sans regret en somme nulle, l’exploitabilité du profil moyen décroît ; cela ne garantit toujours pas le dernier itéré [9].

**Prix.** Stockage, coût de déploiement du mélange, adaptation temporelle plus lente, interprétation statistique plus délicate.

**Test le moins cher.** Vérifier simultanément regret externe et NashConv de la moyenne dans un méta-jeu fini. Un faible regret accompagné d’une forte exploitabilité de la défense moyenne montrerait que le regret ne répond pas, à lui seul, à la question de robustesse finale.

---

# 4. Jeu jouet d’abord — protocole en cinq lignes

1. **Prendre OpenSpiel sans modification**, sur pile ou face apparié et pierre–feuille–ciseaux à somme nulle, et vérifier que son calcul d’exploitabilité retrouve les équilibres connus et une NashConv nulle à tolérance numérique près [17].  
2. **Exécuter le jeu fictif complet**, puis la dynamique asymétrique « historique côté défenseur / dernier itéré côté attaquant », avec initialisations et règles de départage consignées ; journaliser derniers coups, fréquences empiriques et NashConv à chaque tour.  
3. **Exécuter double oracle/PSRO** jusqu’au certificat disponible, et recouper valeur et équilibre des petits jeux avec Gambit [7, 8, 18].  
4. **Vérifier la séparation des mesures** : la meilleure réponse pure doit pouvoir présenter des retours persistants, tandis que la NashConv des moyennes du jeu fictif complet décroît ; un I3 élevé ne doit plus être interprété comme non-convergence si NashConv moyen tend vers zéro.  
5. **Répéter sous départages, initialisations et erreurs de meilleure réponse contrôlées**, puis seulement transposer l’instrumentation au jeu synthétique ; un écart au résultat connu du jouet invalide d’abord l’implémentation ou la métrique.

---

# 5. Rendre « à classe de fonctions égale » réellement posable

Les pièces contiennent déjà un certificat important : pour une matrice restreinte \(G\) de valeur \(v^\*\), le polytope des stratégies d’équilibre du défenseur est

\[
P^\*=\{p\ge 0,\ \mathbf1^\top p=1,\ G^\top p\ge v^\*\mathbf1\}.
\]

Le programme `poids_max_min_equilibres` calcule essentiellement

\[
\min_{p\in P^\*}\max_i p_i.
\]

- S’il est proche de 1, toute stratégie d’équilibre est pure ou presque pure : la pureté est imposée par le jeu.
- S’il est nettement inférieur à 1, il existe au moins un équilibre mélangé : la pureté observée tient alors au sommet choisi par le solveur, pas à une nécessité du jeu (pièce 3, fonction éponyme ; pièce 1, § Métrique).

Pour que la question du mélange soit **réellement exercée**, deux conditions plus fortes sont testables :

1. **Non-dégénérescence de l’équilibre.**  
   Soit construire une tâche dont un équilibre intérieur est connu et vérifié indépendamment ; soit résoudre, pour chaque \(i\), des programmes linéaires bornant \(p_i\) sur \(P^\*\). Des bornes inférieures strictement positives pour tous les \(i\) certifient que tous les équilibres sont intérieurs. Une simple existence d’un équilibre mixte suffit seulement à exclure la pureté forcée.

2. **Valeur stratégique du mélange.**  
   Calculer
   \[
   v^\*-\max_i\min_jG_{ij}.
   \]
   Si cet écart est nul, la meilleure défense pure atteint déjà la valeur du jeu restreint : des poids non purs ne démontrent aucune utilité du tirage. Une marge strictement positive certifie que le mélange améliore la valeur dans le méta-jeu restreint.

Ces certificats restent locaux au jeu restreint. Ils ne prouvent pas que l’équilibre du jeu complet est intérieur ; cela exige en plus un contrôle de meilleure réponse hors du support.

**Le mélange calculé sur un ensemble de tâches n’est pas une garantie.** Il change l’estimand et peut stabiliser une fréquence de pureté, mais ne crée pas nécessairement un équilibre intérieur par tâche. Il peut aussi agréger des moniteurs qui ne sont pas des stratégies communes aux tâches. La sélection des tâches doit être fondée sur les seuls certificats de \(G\), et non sur le résultat B′ − D.

Enfin, pour isoler le tirage, les comparateurs doivent partager **le même ensemble de moniteurs, la même distribution d’entraînement, la même classe déployée et le même calibrage**, seuls les poids de déploiement variant. Les pièces déclarent explicitement que B′ − D mélange déjà trois effets : tirage, sélection maximin et distribution d’entraînement différente (pièce 1, § Ce que l’expérience n’autorise pas).

---

# 6. Transfert aux sondes et moniteurs de modèles de langage

La réponse doit rester limitée : **une seule référence empirique directement pertinente est identifiée dans les pièces, et son PDF n’est pas servi.** Les autres cases sont donc « non établi par les pièces », et non « jamais publié ».

| Mécanisme | Résultat publié identifiable | Portée |
|---|---|---|
| **(a) Ré-entraînement sur des réponses adverses** | Bailey et collègues étudient des défenses en espace latent et leur ré-entraînement adversarial. Le résultat qualitatif est une amélioration de robustesse par ré-entraînement, sans clore la généralisation à de nouvelles optimisations adverses ; ce n’est pas un théorème de non-convergence [15]. | Analogie d’objet seulement. A n’est pas leur protocole : l’oracle et la règle de mise à jour diffèrent, comme le déclarent explicitement les pièces (pièce 1, § Ce que l’expérience n’autorise pas ; pièce 3, en-tête). |
| **(b) Double oracle / PSRO sur sondes d’activations** | Aucun résultat de ce type n’est identifiable dans les pièces. Les sources [7, 8] établissent les algorithmes généraux, pas leur efficacité sur des moniteurs de langage. | Aucun transfert empirique à revendiquer sans autre PDF. |
| **(c) Régularisation/distillation/moyenne de poids sur moniteurs de langage** | Les sources repérées concernent l’apprentissage continu et la moyenne de poids en général [11, 12], pas une preuve de convergence de sondes adversariales. | Résultat sur moniteurs non établi ici. |
| **(d) Optimisme / extragradient sur sondes** | Les résultats identifiés portent sur les jeux saddles et l’entraînement génératif antagoniste [5, 6]. | Pas de résultat publié sur sondes d’activations établi par les pièces. |
| **(e) Classe élargie / ensembles sur moniteurs de langage** | Aucun contrôle publié isolant proprement capacité, mélange et distribution d’entraînement n’est identifiable dans les pièces. | Le résultat D/B′ du pilote reste synthétique et local. |
| **(f) Objectif robuste ou pire cas** | L’entraînement adversarial latent a été étudié sur de vrais modèles, avec amélioration de robustesse comportementale rapportée par Sheshadri et collègues [16]. | Défense du modèle adjacent à la problématique, pas preuve de convergence d’un moniteur ni validation de A. |
| **(g) Déploiement sans regret** | Aucun résultat sur sondes d’activations n’est identifié dans les pièces. | Garantie théorique seulement, dans le cadre en ligne déclaré. |

Ainsi, les pièces ne permettent pas d’affirmer que les résultats du pilote se transfèrent aux vrais modèles. Elles permettent seulement de conclure que **la règle A, telle qu’implémentée dans ce monde synthétique, ne bénéficie pas de la garantie de convergence du jeu fictif complet et que ses indicateurs actuels ne mesurent pas NashConv**.

---

# Sources bibliographiques

**[1]** Julia Robinson, 1951, **“An Iterative Method of Solving a Game”**, *Annals of Mathematics* 54(2), 296–301. Identifiant : **DOI 10.2307/1969530**.

**[2]** George W. Brown, 1951, **“Iterative Solution of Games by Fictitious Play”**, dans Tjalling C. Koopmans (dir.), *Activity Analysis of Production and Allocation*, Cowles Commission Monograph 13, Wiley, 374–376. Identifiant bibliographique : **Cowles Monograph 13, chapitre de Brown**.

**[3]** Lloyd S. Shapley, 1964, **“Some Topics in Two-Person Games”**, dans Melvin Dresher, Lloyd S. Shapley et Albert W. Tucker (dir.), *Advances in Game Theory*, Annals of Mathematics Studies 52, Princeton University Press, 1–28. Identifiant bibliographique : **Annals of Mathematics Studies 52**.

**[4]** Panayotis Mertikopoulos, Christos Papadimitriou et Georgios Piliouras, 2018, **“Cycles in Adversarial Regularized Learning”**, *SODA 2018*, 2703–2717. Identifiants : **arXiv:1709.02738** ; **DOI 10.1137/1.9781611975031.172**.

**[5]** Constantinos Daskalakis, Andrew Ilyas, Vasilis Syrgkanis et Haoyang Zeng, 2018, **“Training GANs with Optimism”**, *ICLR 2018*. Identifiant : **arXiv:1711.00141**.

**[6]** Aryan Mokhtari, Asuman Ozdaglar et Sarath Pattathil, 2020, **“A Unified Analysis of Extra-gradient and Optimistic Gradient Methods for Saddle Point Problems: Proximal Point Approach”**, *AISTATS 2020*, PMLR 108, 1497–1507. Identifiant : **arXiv:1901.08511**.

**[7]** H. Brendan McMahan, Geoffrey J. Gordon et Avrim Blum, 2003, **“Planning in the Presence of Cost Functions Controlled by an Adversary”**, *ICML 2003*, 536–543. Identifiant : **DBLP conf/icml/McMahanGB03**.

**[8]** Marc Lanctot, Vinicius Zambaldi, Audrunas Gruslys, Angeliki Lazaridou, Karl Tuyls, Julien Pérolat, David Silver et Thore Graepel, 2017, **“A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning”**, *NeurIPS 2017*. Identifiant : **arXiv:1711.00832**.

**[9]** Yoav Freund et Robert E. Schapire, 1999, **“Adaptive Game Playing Using Multiplicative Weights”**, *Games and Economic Behavior* 29(1–2), 79–103. Identifiant : **DOI 10.1006/game.1999.0738**.

**[10]** Michael McCloskey et Neal J. Cohen, 1989, **“Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem”**, *Psychology of Learning and Motivation* 24, 109–165. Identifiant : **DOI 10.1016/S0079-7421(08)60536-8**.

**[11]** James Kirkpatrick et al., 2017, **“Overcoming Catastrophic Forgetting in Neural Networks”**, *Proceedings of the National Academy of Sciences* 114(13), 3521–3526. Identifiants : **DOI 10.1073/pnas.1611835114** ; **arXiv:1612.00796**.

**[12]** Pavel Izmailov, Dmitrii Podoprikhin, Timur Garipov, Dmitry Vetrov et Andrew Gordon Wilson, 2018, **“Averaging Weights Leads to Wider Optima and Better Generalization”**, *UAI 2018*. Identifiant : **arXiv:1803.05407**.

**[14]** Aman Sinha, Hongseok Namkoong et John Duchi, 2018, **“Certifying Some Distributional Robustness with Principled Adversarial Training”**, *ICLR 2018*. Identifiant : **arXiv:1710.10571**.

**[15]** Luke Bailey, Alex Infanger, Abhay Sheshadri, Mikhail Seleznyov, Jordan Taylor, Erik Jenner, Jacob Steinhardt, Stephen Casper et Scott Emmons, 2024, **“Obfuscated Activations Bypass LLM Latent-Space Defenses”**. Identifiant : **arXiv:2412.09565**, version **v2** indiquée dans les pièces ; PDF non servi ici, détails à contrôler sur ce PDF.

**[16]** Abhay Sheshadri et al., 2024, **“Latent Adversarial Training Improves Robustness to Persistent Harmful Behaviors in LLMs”**. Identifiant : **arXiv:2407.15567**.

**[17]** Marc Lanctot et al., 2020, **“OpenSpiel: A Framework for Reinforcement Learning in Games”**. Identifiant : **arXiv:1908.09453**.

**[18]** Richard D. McKelvey, Andrew M. McLennan et Theodore L. Turocy, 2016, **“Gambit: Software Tools for Game Theory”**. Identifiant logiciel : **gambit-project.org**.