# Proposition E — Critique croisée de méthode

**Statuts.** Les recommandations et contre-modèles ci-dessous sont des **HYPOTHÈSES** méthodologiques. Les descriptions des propositions sont **RAPPORTÉES**, avec attribution ; je ne transforme pas leurs vérifications déclarées en vérifications personnelles. Aucun dépôt, PDF ou calcul n’a été audité ici.

**Convention probabiliste — HYPOTHÈSE.** Les formules définissent des modèles et des estimateurs, non des résultats. Leurs constantes mathématiques ne sont pas des estimations empiriques.

Pour une mesure scalaire \(\theta\), un duel exclusif peut opposer
\[
H_A:\theta\leq\delta,\qquad H_B:\theta>\delta,
\]
avec \(\delta\) fixé avant lecture. Un intervalle entièrement au-dessus de \(\delta\) permet de rejeter \(H_A\) ; entièrement en dessous, de rejeter \(H_B\), aux risques annoncés. **Un intervalle traversant \(\delta\) ne falsifie ni l’une ni l’autre.** B4 exige des issues informatives opposées, pas la suppression artificielle de l’indécision.

## Sur la proposition A

### (a) Défauts de méthode

**QO-1 — HYPOTHÈSE critique.** Le duel D1 ne suffit pas à justifier le remplacement de l’antériorité des scores par celle du seul scellement.

- Même si toutes les entrées numériques sont figées, **l’existence du résultat rapporté** peut dépendre du verdict : exécution abandonnée, résultat non publié, nouveau nom de version, réparation suivie d’une nouvelle course. A reconnaît la décision de lancer parmi les entrées possibles, puis traite la réparation avant dépense comme dépourvue d’influence sur T0.7. Ce passage n’est pas justifié.
- L’auditeur ne recevant pas la question peut inventorier les paramètres, mais manquer précisément les décisions de continuation, de publication et de remplacement de version.
- Le contrôle sur l’étape B contenant une dépendance connue est un **contrôle positif de sensibilité de l’audit**, pas un contrôle négatif.
- Un témoin positif réussi ne rend pas rétrospectivement identifiable la cause du nul de P3. Il établit une capacité sur une distribution plantée, pas nécessairement sur celle de l’organisme précédent.
- **RAPPORTÉ :** A utilise le nombre \(0{,}014\) comme fausse alerte sur les honnêtes. La pièce 1 l’attribue à une simulation sous hypothèse nulle : cette utilisation change l’objet estimé, sans fournir de mesure nouvelle.

**Q1 — HYPOTHÈSE critique.**

- **E1 conditionne sur une variable postérieure à la génération.** « Propre » dépend des votes, du marquage et de la présence du canal privé. Les scénarios, la difficulté, la conformité et le contenu peuvent déterminer simultanément ce statut et les scores. Contrairement à l’affirmation d’A, les épisodes non propres ne garantissent même pas tous la présence du message privé.
- Une séparation propre/non-propre ne falsifie donc pas « lecture de la consigne seule » : les consignes varient entre scénarios et peuvent prédire la réussite.
- Les hypothèses d’E2 ne sont pas exclusives ; A dit explicitement qu’elles peuvent tenir ensemble. Une contribution du contexte et une contribution du texte ne constituent pas un duel.
- C4 contient un texte honnête **d’un épisode de collusion** ; C3 vient d’épisodes témoins. Leur comparaison ne maintient pas le texte ni l’histoire publique constants.
- C1′ change cible, scénario et coordination privée : ce n’est pas un préfixe sémantiquement neutre. Un effet important de C1′ ne démontre pas un artefact positionnel ; un effet faible ne l’exclut pas.
- Une différence d’aires mesure un changement de classement face aux négatifs, pas une « part » additive du score. Le ratio des gains proposé n’identifie pas une fraction causale.
- Égaliser la longueur des consignes ne neutralise ni leur contenu ni leurs interactions avec l’histoire.

**Choix E — HYPOTHÈSE.** Je refuse (b′) tant que l’audit ne couvre pas la sélection des exécutions et des résultats. Pour Q1, je retiendrais les relectures comme diagnostic de contexte, mais pas E1 comme identification de la collusion réalisée.

### (b) Conditions probabilistes de perte de puissance ou de non-jugement

**HYPOTHÈSES formelles.**

Soient \(V\) le verdict, \(Y\) le résultat potentiel de T0.7, \(R\) son indicatrice de disponibilité :
\[
p(y\mid R=1)=
\frac{\sum_v p(R=1\mid y,v)p(y,v)}{P(R=1)}.
\]
Si \(P(R=1\mid Y=y)\) varie avec \(y\), la distribution disponible diffère de la distribution cible, même lorsque \(Y=f(X)\) est déterministe.

Pour E1, soient \(G\) le statut propre, \(S\) le score et \(Z\) les covariables :
\[
S\perp G\mid Z,\qquad
p(z\mid G=1)\neq p(z\mid G=0)
\]
est compatible avec
\[
P(S_{G=1}>S_{G=0})\neq\tfrac12.
\]
Si \(P(G=g\mid Z=z)=0\), le contraste conditionnel correspondant n’est pas identifiable. Si \(P(G=1)\to0\) ou \(1\), sa variance d’estimation augmente.

Pour des scores \(S_1,S_2\) et un négatif indépendant \(N\) de fonction de répartition continue \(F_N\),
\[
\Delta_{\mathrm{AUC}}
=E[F_N(S_1)-F_N(S_2)].
\]
Si \(F_N(S_1)=F_N(S_2)\) presque sûrement, \(\Delta_{\mathrm{AUC}}=0\), même lorsque \(P(S_1\neq S_2)>0\).

Pour un ratio \(\widehat q=\widehat\Delta_2/\widehat\Delta_1\), lorsque \(\Delta_1\to0\), l’estimateur devient instable ; si \(\Delta_1=0\), le paramètre n’est pas défini.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — fatalité relative aux revendications d’A.**

- Pour D1 : un pipeline factice dont les fichiers sont tous figés, mais dont la **publication dépend d’un verdict injecté**. L’audit doit détecter ce canal ; sinon il ne justifie pas (b′).
- Pour E1 : honnêtes des mêmes épisodes, comme A le propose, **et** prédicteurs de réussite fondés seulement sur le scénario et la consigne avant génération. Le premier contrôle seul ne neutralise pas les difficultés propres aux colludeurs.
- Pour E2 : relecture identique ; transformations de préfixe sans changement de rôle ; relecture du **même texte honnête** sous ses contextes honnête et colludeur.
- Pour toute supériorité au lexical : prédictions lexicales hors pli, par étage, avec regroupement empêchant qu’un scénario contribue à l’apprentissage et à son évaluation.

## Sur la proposition B

### (a) Défauts de méthode

**QO-1 — HYPOTHÈSE critique.**

- Le diagnostic portant sur la décision de sceller est pertinent, mais l’inventaire de fichiers ne prouve pas l’absence de canal de sélection.
- Le duel sur la date mélange **fixation ex ante** et **indépendance statistique**. Une date fixée avant les résultats peut sélectionner les courses rapides ; leur durée peut être liée à leur résultat.
- L’affirmation selon laquelle (a) ne pourrait pas produire le même nœud que (c) est incompatible avec le fusible décrit par B elle-même : une levée humaine anticipée ferme également T0.7 sur la course concernée sous son texte actuel.
- Le chiffrement proposé n’a pas de modèle de menace défini. Si entropie et sel sont accessibles à la session dont on veut empêcher la lecture, la clé est reconstructible. Si le sel est secret, il faut préciser un dépositaire distinct et le traitement du texte clair, des journaux et des sauvegardes.
- Un horodatage ou un journal d’accès ne démontre pas l’absence de connaissance : copies, mémoire et accès non journalisés restent hors de cette preuve.

**Intégrité — RAPPORTÉ.** B emploie **VÉRIFIÉ** pour plusieurs affirmations en invoquant les pièces ou la contre-lecture, sans décrire un audit propre. Je conserve ces étiquettes comme déclarations de B, mais elles ne constituent pas ici des vérifications indépendantes.

**Q1 — HYPOTHÈSE critique.**

- Le duel « texte ou consigne » confond deux propriétés compatibles. C2 peut séparer de C3 **et** le changement de contexte modifier les scores.
- C4, tel que repris de la contre-lecture, comprend le canal privé. Il ne mesure donc pas « la consigne seule ». La matrice annoncée ne sépare pas consigne et canal.
- La case « C4 détecté, C1−C2 non positif » n’est pas nécessairement incohérente : une interaction texte–contexte peut produire exactement ce motif.
- C3 contre lui-même avec les mêmes observations donne une aire symétrique par construction. Ce contrôle peut vérifier une implémentation, pas calibrer une généralisation.
- Le duel comportemental laisse un intervalle entre ses hypothèses « joue » et « ne joue pas ». Ses deux hypothèses sont exclusives, mais non exhaustives.
- La probabilité de voter la cible « par hasard » n’est pas fournie : elle dépend des choix possibles, préférences et dépendances entre agents.
- Un faible taux d’épisodes propres ne rend pas toute séparation « forcément » instructionnelle. Une conduite partielle, une différence stylistique ou un audit comportemental imparfait restent possibles.
- La multiplicité descriptive n’est pas « sans conséquence » : elle affecte la fréquence des constats sélectionnés pour le commentaire.

**Choix E — HYPOTHÈSE.** Je conserve (a), mais refuse la garantie cryptographique annoncée sans dépositaire et contrôle des sorties. Je n’accepte pas la matrice C1–C4 comme identification des facteurs.

### (b) Conditions probabilistes de perte de puissance ou de non-jugement

**HYPOTHÈSES formelles.**

Avec \(T\) un temps d’achèvement et \(\tau\) fixé :
\[
p(y\mid T\leq\tau)=
\frac{P(T\leq\tau\mid Y=y)p(y)}{P(T\leq\tau)}.
\]
Une valeur constante de \(\tau\) n’implique pas \(Y\perp \mathbf1(T\leq\tau)\).

Pour une clé \(K=g(E,L)\) et l’information accessible \(I\),
\[
(E,L)\subseteq I\ \Longrightarrow\ H(K\mid I)=0.
\]

Pour le score conditionnel
\[
m(c,p,x)=\mu+\beta_c c+\beta_p p+\beta_x x+
\beta_{cx}cx+\beta_{px}px,
\]
des observations limitées à \(p=c\) identifient certaines sommes de coefficients, pas séparément \(\beta_c\) et \(\beta_p\). Les interactions permettent des contrastes de signes différents selon \(x\).

Avec \(n\) blocs de taille \(m\), variance marginale \(\sigma^2\) et corrélation intrabloc \(\rho\),
\[
\operatorname{Var}(\bar S)
=\frac{\sigma^2}{nm}[1+(m-1)\rho].
\]
Quand \(\rho\to1\), augmenter le nombre de messages par bloc apporte peu de précision.

Pour \(M\) tests indépendants de niveau \(\alpha\),
\[
P(\text{au moins un rejet erroné})=1-(1-\alpha)^M.
\]
Sans indépendance, cette probabilité dépend de la loi jointe des décisions ; elle n’est pas déterminée par leur seul niveau marginal.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE.**

- Pour la fermeture : artefacts synthétiques dont l’accès est tenté avec **exactement les droits et informations de la session mère**, y compris journaux et copies. Un fichier simplement chiffré ne suffit pas.
- Pour la matrice : consigne variée à canal fixe, puis canal varié à consigne fixe. Sans ces contrastes, l’attribution séparée est impossible.
- Pour C3 : deux échantillons honnêtes disjoints au niveau des scénarios, et permutations respectant les unités échangeables ; pas seulement un échantillon comparé à lui-même.
- Pour le comportement : fréquence empirique des votes cibles chez les témoins appariés, sans probabilité uniforme supposée.
- Pour les alertes : négatifs de calibration distincts des négatifs d’évaluation. Fixer puis mesurer un taux d’alerte sur les mêmes observations ne valide pas ce taux hors échantillon.

## Sur la proposition C

**RAPPORTÉ : la pièce C est absente, indiquée « jamais lancée » ; aucune critique de son contenu n’est possible.**

## Sur la proposition D

### (a) Défauts de méthode

**QO-1 — HYPOTHÈSE critique.**

- La revue humaine préspécifiée ne garantit pas que sa décision soit indépendante du verdict fermé. Échecs, tailles de fichiers, durées ou messages d’erreur peuvent constituer des informations auxiliaires. Il faut spécifier ce qui est observable au moment de la revue.
- Le duel sur les gardes est correctement limité aux chemins testés. Cependant, « réussite complète » signifie couverture d’une matrice finie, non absence générale de chemin fautif. La distribution des chemins réellement rencontrés reste à définir.
- QO-B oppose un signal détectable à un ensemble comprenant indétection, prédicteur trivial et fuite. Ces causes peuvent coexister avec un signal réel. Un test de validité de chaîne ne constitue donc pas automatiquement un duel sur l’existence du signal.

**Q1 — HYPOTHÈSE critique.**

- Le factoriel proposé est mieux défini que les comparaisons C4/C3, mais le canal « privé de colludeur » contient potentiellement déjà instruction, cible et coordination. Le garder fixe identifie l’effet du remplacement d’un message de consigne, **pas l’effet total de recevoir une instruction de collusion**.
- Une consigne honnête associée à une coordination collusive peut produire une contradiction. L’effet mesuré peut être celui de cette contradiction.
- Dans Q1-A, une borne basse non positive ne réfute pas l’existence d’une augmentation : elle réfute seulement la phrase « augmentation établie ». Cette dernière est une propriété de la décision statistique, pas une hypothèse scientifique concurrente.
- Dans Q1-B, battre un sac de mots ne prouve pas un « signal résiduel » conditionnel aux mots. Une sonde peut encoder syntaxe, ordre ou interactions lexicales que cette base ne représente pas.
- Qualifier C4 de fausse alerte sur l’« intention » suppose une vérité terrain sur cette intention contrefactuelle. On peut rapporter une alerte sur texte d’origine honnête, pas une erreur sur un état mental non observé.
- L’apprentissage lexical par étage exige une évaluation hors pli ; sinon la correction proposée remplace une base inadéquate par une base évaluée sur son apprentissage.

**Choix E — HYPOTHÈSE.** Je retiens (a) avec revue, sous restriction des informations accessibles. Pour Q1, je retiens le factoriel seulement comme diagnostic local de contexte ; je changerais d’avis si ses cellules ne peuvent être définies sans ambiguïté de contenu.

### (b) Conditions probabilistes de perte de puissance ou de non-jugement

**HYPOTHÈSES formelles.**

Soient \(W\) l’information accessible lors de la revue, \(V\) le verdict et \(R=r(W)\) :
\[
I(V;W)>0
\]
autorise une dépendance entre \(R\) et \(V\), sans accès direct à \(V\).

Pour une loi opérationnelle \(q\) sur les chemins \(\omega\), un ensemble testé \(\Omega_t\) et une indicatrice de faute \(F\),
\[
P_q(F=1)=
\sum_{\omega\in\Omega_t}q(\omega)F(\omega)
+\sum_{\omega\notin\Omega_t}q(\omega)F(\omega).
\]
Annuler le premier terme ne borne pas le second sans hypothèse supplémentaire.

Pour les relectures, si
\[
p(X=x\mid C=c,P=p,Z=z)=0
\]
sur une cellule cible, son score calculé reste observable, mais sa moyenne sous la loi naturelle correspondante n’est pas identifiable sans extrapolation.

Pour un effet apparié \(D\), une puissance faible est attendue lorsque
\[
\frac{|\theta-\delta|}{\sqrt{\operatorname{Var}(\widehat\theta)}}\to0.
\]

Pour une représentation lexicale \(L=\ell(X)\),
\[
S\perp Y\mid X
\]
est compatible avec
\[
\operatorname{AUC}(S)>\operatorname{AUC}(L),
\]
si \(\ell\) perd une information prédictive contenue dans \(X\). Le gain d’aire ne teste donc pas l’indépendance conditionnelle recherchée.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE.**

- Pour la revue : sorties synthétiques de verdicts différents partageant le même résumé opérationnel autorisé ; vérifier ce que le décideur peut distinguer.
- Pour le factoriel : contradictions de contexte **sans collusion**, appariées aux transformations étudiées ; sinon « instruction » et « incohérence » restent confondues.
- Pour les scores : relectures identiques et échanges honnête–honnête avec marge d’équivalence préspécifiée. Une simple non-significativité n’établit pas l’invariance.
- Pour le signal textuel : base textuelle hors pli permettant de tester si le gain vient seulement des limites du sac de mots, ainsi que base de métadonnées.
- Pour l’absence de fuite : permutation des étiquettes au niveau des groupes, en répétant **toute la sélection de sonde**. Permuter seulement après sélection ne contrôle pas l’optimisme introduit pendant la construction de l’instrument.

FIN-DE-CELLULE