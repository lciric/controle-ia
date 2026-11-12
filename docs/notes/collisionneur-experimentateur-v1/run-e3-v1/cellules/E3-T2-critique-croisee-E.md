# Proposition E — Critique croisée de méthode

**Statuts :** les choix attribués à A, B et C sont **RAPPORTÉS** par leurs pièces, sans validation expérimentale. Mes objections et modèles conditionnels portent le statut **HYPOTHÈSE**. Aucune performance n’est ici présentée comme observée ou vérifiée.

**HYPOTHÈSE — Convention d’inférence.** Pour un effet \(\Delta\) et une marge gelée \(\delta\), un duel exclusif peut opposer \(H_A:\Delta>\delta\) à \(H_B:\Delta\leq\delta\). Une borne inférieure dépassant \(\delta\) permet de rejeter \(H_B\) ; une borne supérieure ne dépassant pas \(\delta\) permet de rejeter \(H_A\), avec erreurs contrôlées. Un intervalle chevauchant la frontière reste **non jugeable** : l’absence de significativité ne falsifie pas un bénéfice. Les constantes mathématiques ci-dessous définissent des lois ou des estimateurs ; elles ne constituent pas des mesures.

## Sur la proposition A

### (a) Défauts de méthode

**HYPOTHÈSE — La boucle minimale n’isole pas, à elle seule, l’exécution.** `exp-min` contre « meilleur de N » modifie simultanément l’interactivité, les consignes, la répartition du budget, le nombre de candidats et leur sélection. Cela permet de comparer deux politiques complètes, pas d’attribuer leur différence à l’accès à un exécuteur.

Le contrôle `exp-sham` proposé par A est utile comme intervention, mais une sortie vide ou tronquée introduit également une panne reconnaissable. Elle peut provoquer davantage de reprises, une perte de confiance ou un autre arrêt. Surtout :

- `exp-min` et `exp-sham` tous deux meilleurs que le témoin n’exclut pas un effet additionnel de l’exécution ;
- le contraste pertinent pour cet effet est `exp-min` contre `exp-sham`, pas seulement leurs contrastes respectifs contre le témoin ;
- même ce contraste dépend de la fidélité du placebo.

**HYPOTHÈSE — Les portes généralisent au-delà de leur objet.** L’échec de `exp-min` ne falsifie pas l’utilité de tous les scientifiques du marché. L’affirmation qu’ils « ne font pas autre chose sur ce point » suppose précisément l’absence d’interaction entre architecture et exécution, interaction non testée. De même, Kaimen contre `exp-min` n’est pas une simple ablation « + tournoi » : génération, évolution, consignes et mémoire peuvent aussi changer.

**HYPOTHÈSE — La sonde de mémorisation confond exposition et prédictibilité.** Les lois publiques et les leurres ne sont pas nécessairement échangeables : auteur, complexité, identifiants et fréquence des formes peuvent différer. Une meilleure reproduction des premières n’identifie donc pas une mémorisation. Inversement, une absence d’écart ne prouve pas son absence : la récupération peut dépendre du contexte fourni lors de l’expérience réelle. La conclusion « toute comparaison est invalide » est plus large que ce que la sonde établit.

**HYPOTHÈSE — Risque de fabrication de l’instrument sur sa cible.** Ajuster le détecteur de lois plantées ou l’appariement oracle sur les seules transformations qui serviront à leur validation rend la réussite partiellement vraie par construction. Une découverte honnête peut aussi reproduire exactement la loi plantée : la correspondance textuelle ne distingue pas découverte et fuite.

**HYPOTHÈSE — La porte Sakana mélange fonctionnement et sécurité.** Un relais coupé n’implique pas nécessairement une sortie vide : une réponse déjà disponible ou une production déterministe peut subsister. Une réussite ne prouve donc pas une route réseau alternative. Le canari absent ne prouve pas davantage l’isolement si l’agent ne tente pas sa récupération.

**RAPPORTÉ — Contrainte des faits.** Aucun réseau hors relais n’est permis. Le comparateur « non enfermé » d’A n’est donc pas admissible comme bras de l’expérimentateur ; il faudrait une décision distincte pour un banc technique extérieur au rôle.

### (b) Conditions probabilistes de perte de puissance ou de non-identification

**HYPOTHÈSE — Modèles conditionnels.** Notons \(Y_{ar}\) le rendement oracle du bras \(a\) sur le monde \(r\), \(D_r=Y_{ar}-Y_{br}\), et \(m\) le nombre de mondes indépendants.

- **Rendement et A/A :**
  \[
  \widehat\Delta=\overline D,\qquad
  \operatorname{Var}(\widehat\Delta)=\operatorname{Var}(D_r)/m.
  \]
  Lorsque \(|\Delta-\delta|\sqrt m/\operatorname{sd}(D_r)\) est faible, le duel manque de puissance. Si les \(D_r\) sont corrélés, la variance contient aussi leurs covariances. La loi d’une différence A/A isolée n’identifie pas cette matrice de covariance.

- **Placebo :**
  \[
  \Delta_{\rm réel-fictif}
  =\tau_{\rm information}+\tau_{\rm panne}+\tau_{\rm interaction}.
  \]
  Si les derniers termes ne sont pas identifiés séparément, \(\tau_{\rm information}\) ne l’est pas.

- **Mémorisation :** avec \(X_P\sim\mathrm{Bin}(n_P,p_P)\) et \(X_L\sim\mathrm{Bin}(n_L,p_L)\),
  \[
  p_P-p_L=\theta_{\rm exposition}+\theta_{\rm difficulté}.
  \]
  Sans contrainte sur \(\theta_{\rm difficulté}\), \(\theta_{\rm exposition}\) est non identifiable. Si les lois observables sous mémorisation et sans mémorisation ont une distance de variation totale faible, tout test a une somme d’erreurs proche de l’unité.

- **Fausses découvertes par dollar :**
  \[
  \rho_F=\mathbb E[F]/\mathbb E[C].
  \]
  Une politique telle que \(P(F=0,V=0)=1\) minimise \(\rho_F\) sans découverte. Le critère primaire d’E2 ne départage donc pas qualité et abstention sans contrainte sur \(\mathbb E[V]\).

- **Gardes et canaris :** si une fuite a probabilité \(p\), sa détection conditionnelle sensibilité \(s\), et la tentative probabilité \(a\), la probabilité d’absence de détection sur \(n\) essais indépendants vaut
  \[
  (1-aps)^n.
  \]
  Pour \(a=0\) ou \(s=0\), l’absence observée n’informe pas \(p\). Une sensibilité estimée sous \(Q_{\rm calibration}\) n’identifie pas celle sous \(Q_{\rm usage}\) lorsque leurs supports diffèrent.

- **Coût :** si \(C^\*=C+\varepsilon\), un biais \(\mathbb E[\varepsilon\mid a]\) dépendant du bras peut inverser l’ordre de \(\mathbb E[V]/\mathbb E[C^\*]\). Par ailleurs, \(\mathbb E[V/C]\) et \(\mathbb E[V]/\mathbb E[C]\) sont des paramètres distincts.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — Pour l’attribution à l’information expérimentale :** un placebo conservant schéma, volume et latence des retours, avec résultats tirés indépendamment du monde cible. Duel sur le contraste réel–placebo : \(H_A:\Delta>\delta\), \(H_B:\Delta\leq\delta\). Une borne entièrement d’un côté rejette l’hypothèse opposée ; sinon, attribution non jugeable. Le coût et les trajectoires de reprise doivent être estimés, pas supposés appariés.

**HYPOTHÈSE — Pour l’alerte de contamination :** des mondes privés aux identifiants opaques et des lois non exposées provenant du même générateur que les lois exposées. Le duel porte sur un excès de récupération dû à l’exposition, avec marge gelée. Sans échangeabilité, l’alerte reste descriptive.

**HYPOTHÈSE — Pour les gardes :** des journaux de découvertes honnêtes contenant effectivement la bonne loi, et une famille de transformations retenue hors construction du détecteur. Le duel porte sur un taux de fausse alerte inférieur ou supérieur à une tolérance gelée. Sans ce contrôle, la garde risque de sanctionner ce que l’expérience recherche.

## Sur la proposition B

### (a) Défauts de méthode

**HYPOTHÈSE — Le critère de sélection réintroduit le juge.** B définit les vraies découvertes comme des lois **promues**, pénalise les fausses **promotions**, et invoque la méthode O2 pour départager les architectures.

**RAPPORTÉ — Contraintes des faits.** La composition doit être jugée sur l’oracle et le coût, jamais sur le verdict du juge ; aucun score du juge ne doit sélectionner l’agent.

**HYPOTHÈSE — Conséquence méthodologique.** Même recalculée avec l’oracle, une métrique conditionnée à la promotion dépend du juge. B doit compter la vérité des fiches soumises indépendamment de leur promotion pour sélectionner le bras. Les promotions peuvent rester un diagnostic séparé. L’inférence comparative entre bras doit également être distincte de la procédure O2 appliquée aux lois.

**HYPOTHÈSE — Les hypothèses changent entre énoncé et décision.** L’expérience principale annonce un gain de vraies découvertes, mais décide sur une utilité pénalisée. L’expérience de bruit compare une différence de scores à une « variance » : les unités diffèrent. L’expérience sur les fausses promotions transforme « pas de différence significative » en réfutation d’une nuisance ; il faudrait une marge de non-infériorité.

**HYPOTHÈSE — La monotonie du témoin n’est pas garantie.** Le maximum d’un score de développement peut croître avec le nombre de candidats. La vérité oracle du candidat sélectionné ne le doit pas : davantage de candidats peut accentuer l’optimisation du bruit. Une courbe oracle non monotone ne prouve donc pas que le sélecteur est défectueux ; sa saturation n’est pas une condition du coût apparié.

**HYPOTHÈSE — Les contrôles proposés peuvent tester autre chose.**

- Un « modèle incompatible » effectivement appelé violerait la liste autorisée. Une requête interdite bloquée teste la barrière, pas la compatibilité fonctionnelle de Kimi.
- Couper le pont teste une dépendance au relais, pas l’absence d’autres voies de sortie.
- Une consigne dégradée ne garantit pas davantage de fausses promotions : un juge fonctionnel peut tout rejeter.
- Le rendement du proposeur simple n’est pas une borne inférieure garantie.

**RAPPORTÉ — Portée du GO.** La question mentionne un GO pour le collisionneur. B l’affecte à ses premières expériences sans autorisation correspondante transmise ; ces dépenses restent à soumettre séparément.

### (b) Conditions probabilistes de perte de puissance ou de non-identification

**HYPOTHÈSE — Modèles conditionnels.**

- **Compatibilité et achèvement :**
  \[
  X_i\sim\mathrm{Bernoulli}(p),\qquad \widehat p=n^{-1}\sum_iX_i.
  \]
  Une porte \(H_A:p\geq p_\star\), \(H_B:p<p_\star\) n’est pas tranchée lorsque l’intervalle de \(p\) couvre \(p_\star\). Sous dépendance :
  \[
  \operatorname{Var}(\widehat p)=
  \frac{np(1-p)+2\sum_{i<j}\operatorname{Cov}(X_i,X_j)}{n^2}.
  \]
  Compter les fiches plutôt que les tentatives change le paramètre en \(\mathbb E[K]\), distinct de \(P(K>0)\).

- **A/A :** pour \(D=Y_1-Y_2\), \(|D|<\delta\) sur une réalisation ne borne pas \(\operatorname{Var}(D)\). Sous une loi mélange concentrée près de zéro avec une composante rare de grande amplitude, cet événement peut être probable malgré une variance élevée.

- **Utilité :**
  \[
  U_a=\frac{\mathbb E[V_a]-\lambda\mathbb E[F_a]}{\mathbb E[C_a]}.
  \]
  Des bras présentant des compromis différents changent d’ordre selon \(\lambda\). Sans valeur gelée, l’ordre n’est pas défini.

- **Conditionnement à la promotion :** avec \(T\) la vérité oracle et \(J\) la promotion,
  \[
  \theta_a=P(T=0\mid J=1,a),\qquad
  \widehat\theta_a=F_a/R_a.
  \]
  Pour \(P(J=1\mid a)=0\), \(\theta_a\) n’est pas défini. Pour \(R_a\) faible, son estimation est peu précise. Si \(P(J=1\mid T,a)\) varie entre bras, \(\theta_a\) n’identifie pas \(P(T=0\mid a)\).

- **Meilleur de N :** soient \((S_i,T_i)\) échangeables et \(I_N=\arg\max_iS_i\). Si \(T_i\perp S_i\), alors
  \[
  \mathbb E[T_{I_N}]=\mathbb E[T_i].
  \]
  Si \(\mathbb E[T_i\mid S_i=s]\) décroît dans la queue supérieure de \(S_i\), le rendement oracle sélectionné peut décroître avec \(N\).

- **Gardes :** zéro fuite détectée sur \(n\) essais a vraisemblance \((1-p)^n\), compatible avec des valeurs positives de \(p\). Si les deux compteurs de coût ont la même erreur systématique, leur différence peut être nulle sans exactitude de l’un ou de l’autre.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — Pour la sélection du bras :** recalcul des critères oracle en masquant entièrement les verdicts de promotion. Duel sur la probabilité que la décision de sélection change quand seuls ces verdicts changent : \(H_A:p\leq\varepsilon\), \(H_B:p>\varepsilon\). Sans invariance, le critère ne respecte pas la séparation annoncée.

**HYPOTHÈSE — Pour le témoin :** lots où le score de développement est indépendant de la vérité oracle. Duel entre un gain de sélection ne dépassant pas une marge gelée et un gain la dépassant. Un excès persistant imposerait de chercher fuite, réutilisation de calibration ou erreur de calcul, plutôt que de déclarer le filtre validé.

**HYPOTHÈSE — Pour les fausses promotions :** mondes sans loi nouvelle et soumissions nulles fixées indépendamment du juge. Duel entre taux de rejet sous le nul inférieur ou égal au seuil gelé et taux supérieur. Une consigne « mauvaise » n’est pas un substitut à cette loi nulle contrôlée.

## Sur la proposition C

### (a) Défauts de méthode

**HYPOTHÈSE — La conclusion causale dépasse encore le contraste.** Le filtre mécanique du témoin exécute déjà des prédictions sur les épisodes. Le contraste teste donc une allocation entre génération, filtrage et révision interactive, non « calcul contre absence de calcul ». Une victoire reste informative pour choisir une politique ; elle ne prouve pas seule le mécanisme invoqué.

**HYPOTHÈSE — L’échec minimal ne ferme pas les architectures riches.** C critique correctement la porte Kaimen→Sakana, mais reproduit sa structure avec Minimal→Sakana. Une architecture riche pourrait bénéficier d’une interaction absente de la boucle minimale. Lire ensuite les traces pour choisir les mondes où la tester crée une fuite entre diagnostic et évaluation si cette nouvelle comparaison réutilise ces mondes.

**HYPOTHÈSE — Le placebo est doté d’un résultat présumé.** Le bras aveugle ne « doit » pas perdre : l’auto-révision sans retour empirique peut améliorer les fiches. Sa défaite ne peut pas être une condition de validité imposée par construction.

**HYPOTHÈSE — Multiplicité et erreurs sont confondues.** Même quota de fiches ne signifie pas même nombre d’hypothèses distinctes, même dépendance ni même puissance. Par ailleurs, \(F/\$\) ne se compare pas à un seuil de FDR : leurs unités diffèrent. Les faits imposent un contrôle des comparaisons multiples, sans établir le critère particulier choisi par C.

**HYPOTHÈSE — Les instruments changent de cible.** La table du juge demande une sensibilité aux vraies lois mais fournit parmi ses cas honnêtes des reformulations du nul. Être vrai ne suffit pas à constituer une nouveauté contre ce nul. Le test de l’outil mêle quant à lui transport correct, analyse correcte et décision de rejet : une faible réussite ne localise pas la panne.

**HYPOTHÈSE — La porte architecturale est incomplète.** Les hypothèses « un cadriciel apporte un gain » et « le minimal domine les deux » laissent mal définis les ex æquo, effets inférieurs à la marge et interactions avec les familles de mondes. Le devis ne démontre pas que la précision nécessaire sera atteinte.

### (b) Conditions probabilistes de perte de puissance ou de non-identification

**HYPOTHÈSE — Modèles conditionnels.**

- **Gain relatif :**
  \[
  G=(\mu_E-\mu_T)/\mu_T.
  \]
  Pour \(\mu_T=0\), \(G\) est indéfini ; lorsque \(\mu_T\) approche zéro, son estimateur devient instable. Comparer directement ce gain relatif à un écart-type exprimé en découvertes par dollar n’est pas défini.

- **Quota fixe sous nul :** si chaque fiche est classée vraie ou fausse, \(V+F=M\). Sous \(P(V=0)=1\),
  \[
  P(F=M)=1.
  \]
  Le nombre de fausses soumissions ne départage alors aucun bras contraint au même quota.

- **Dépendance entre fiches :**
  \[
  \operatorname{Var}\!\left(\sum_iT_i\right)
  =\sum_i\operatorname{Var}(T_i)+2\sum_{i<j}\operatorname{Cov}(T_i,T_j).
  \]
  Fixer \(M\) ne fixe ni cette variance ni la puissance.

- **Sélection architecturale :** avec \(\Delta_a=\mu_a-\mu_{\min}\),
  \[
  \mathbb E[\max_a\widehat\Delta_a]\geq\max_a\mathbb E[\widehat\Delta_a].
  \]
  Sélectionner puis évaluer le gagnant sur les mêmes observations introduit un biais favorable. Si
  \[
  \Delta_a=\int\Delta_a(w)\,dP_W(w),
  \]
  changer \(P_W\) après inspection peut changer le signe du paramètre.

- **Calibration de l’outil :** soit \(p=P(R=1\mid I=1)\), avec \(I\) livraison correcte et \(R\) rejet correct. Le taux global \(P(R=1)\) n’identifie pas \(p\) sans estimation de \(P(I=1)\) et de \(P(R=1\mid I=0)\).

- **Séparation développement–évaluation :** pour un sélecteur \(\widehat h=f(D)\), la validité hors échantillon exige une loi d’évaluation correctement spécifiée conditionnellement à \(D\). Si \(D\) et l’évaluation \(Z\) partagent une variable latente non conditionnée, \(P(Z\mid D)\neq P(Z)\) ; les calibrations fondées sur leur indépendance ne s’appliquent plus.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — Pour la nouveauté :** reformulations exactes des lois connues, accompagnées de fiches nulles indépendantes. Duel entre taux de promotion de ces reformulations inférieur ou égal à la tolérance gelée et taux supérieur. Sans ce contrôle, le système peut récompenser la redécouverte du nul.

**HYPOTHÈSE — Pour l’information des retours :** retours d’expériences provenant d’un monde indépendant, mais conformes au même format. Duel réel–retours indépendants autour d’une marge gelée, sans exiger que le contrôle perde contre le témoin.

**HYPOTHÈSE — Pour le passage architectural :** famille de mondes tenue hors diagnostic des traces et hors réglage des consignes. Duel sur le gain du candidat sélectionné dans cette famille, et non sur le maximum réestimé parmi tous les candidats. Sans cette séparation, la porte mesure aussi la sélection opportuniste de l’instrument.

## Sur la proposition D

Pièce E3-T1-conception-D absente, signalée « ECHEC » ; aucune critique de son contenu n’est possible.

**HYPOTHÈSE — Position E pour l’arbitrage.** Aucun des plans transmis ne justifie encore une conclusion négative sur *tous* les expérimentateurs à partir de l’échec d’un seul. Je conditionnerais le branchement à un critère oracle indépendant des promotions, un coût réellement mesuré, une marge décisionnelle gelée et une précision suffisante pour rejeter l’une des deux hypothèses — faute de quoi la conclusion correcte reste « non départagé ».

FIN-DE-CELLULE