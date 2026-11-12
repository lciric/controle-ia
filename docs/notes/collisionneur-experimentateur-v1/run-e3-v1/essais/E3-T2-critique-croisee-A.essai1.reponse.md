# Proposition A — Tour III.2 : critique croisée de méthode

**Pièce D** : absente (statut ECHEC) ; je ne la critique pas et n'en suppose aucun contenu.

Convention : tout ce qui suit est ma lecture des pièces B, C, E ; les statuts des faits restent ceux du fichier FAITS. Les chiffres que j'avance sont **illustratifs** sauf indication contraire. Je ne fusionne pas les trois conceptions ; là où je m'en sers, je le dis.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Le juge entre dans le critère de comparaison des bras (exp. 4 et 5).** B définit « vraie découverte » comme « loi *promue* dont l'oracle confirme la vérité » et fixe le seuil « p < 0,05 ou e > 20 selon la méthode du juge O2 ». Or N-058 (RAPPORTÉ) dit que la composition des proposeurs se juge sur l'oracle et le coût, **jamais sur le verdict du juge**. Compter les promotions, c'est faire du juge un facteur multiplicatif commun aux deux bras, mais non neutre : la puissance du juge dépend du nombre de fiches soumises (multiplicité), donc du bras. Un bras qui soumet moins de fiches subit une correction de multiplicité plus douce et verra plus de ses fiches promues *à vérité égale*. Ce n'est pas un gain du scientifique, c'est un artefact du contrôle des comparaisons multiples. La mesure devrait porter sur les fiches **soumises** jugées par l'oracle, le verdict du juge n'étant qu'un témoin (c'est ce que fait E ; je m'en sers).

2. **Les expériences 4 et 5 sont deux tests sur les mêmes runs sans correction.** B l'écrit : « même donnée qu'exp. 4 ». Deux hypothèses, deux seuils, un seul jeu : le risque d'erreur de première espèce global n'est pas celui annoncé.

3. **L'exp. 5 n'est pas en inférence forte.** « H_A : pas significativement supérieur » n'est pas falsifiable par l'absence de signification ; une absence de différence détectée est compatible avec H_A *et* avec un H_B à faible puissance. Il manque une marge d'équivalence (E en pose une ; C aussi implicitement). Violation de B4.

4. **A/A avec « même graine fixée pour l'orchestrateur » (exp. 3).** Si la graine fixe tout ce qui est local (tirages d'épisodes, ordre des fiches), les deux runs ne diffèrent que par la stochasticité du modèle distant. Le pilote mesure alors une variance plus petite que celle des runs réels de la comparaison, où graines et mondes changeront. Le δ calibré sur cet A/A est trop serré : l'exp. 4 déclarera des différences « au-delà du bruit » qui sont du bruit. Fuite entre calibration et évaluation.

5. **Le contrôle négatif de l'exp. 3 est réglable à volonté.** « Proposeur avec consigne dégradée » : le degré de dégradation est choisi par l'expérimentateur, donc le contrôle réussit par construction. Il faut une dégradation graduée et gelée (par ex. retirer une fraction préenregistrée des épisodes de développement), sinon on n'apprend rien sur la sensibilité du banc à des effets de la taille attendue.

6. **Le contrôle négatif de l'exp. 1 teste la barrière, pas l'appel de fonctions.** « Modèle intentionnellement incompatible » : le relais v3 refuse tout modèle autre que `kimi-k3.1-pro` (RAPPORTÉ, échec fermé). Le contrôle échouera 10/10 à cause de la liste d'autorisation, quel que soit le support de l'appel de fonctions. Vrai par construction ; il ne dit rien sur ce qu'on veut savoir.

7. **Le contrôle négatif de l'exp. 2 (pont coupé) mesure la dépendance au relais, pas l'enfermement.** Qu'un agent échoue sans relais prouve qu'il a besoin du modèle ; cela ne prouve pas qu'avec le pont, le réseau est fermé. Le contrôle pertinent est : agent avec pont, consigne qui exige une ressource Web ; l'accès doit échouer *et* être tracé.

8. **Instrument 5 : la monotonie de score(N) n'est pas un critère de validité.** Le « meilleur de N » sélectionne sur les épisodes de développement ; au-delà d'un certain N, il sélectionne les fiches les plus sur-ajustées, et V/$ (lu sur l'oracle) peut décroître. La non-monotonie serait un résultat, pas un défaut de la règle. De même « N = 1 égale le proposeur seul » est vrai par construction si la règle de sélection est l'identité.

9. **Confondant principal non fixé : la multiplicité.** B le nomme dans ses risques mais ne le tranche pas dans son dessin ; « 3 mondes × 2 bras » sans nombre de fiches par bras laisse le confondant ouvert.

### (b) Conditions sous lesquelles les mesures perdent leur puissance ou deviennent non jugeables

- **Exp. 1 et 2 (Binomiale(n, p), n = 10 ou 5).** Avec un seuil 8/10, la région où ni H_A ni H_B n'est rejetée au risque usuel couvre, illustrativement, p ∈ ]0,55 ; 0,95[ ; avec 5 essais et seuil 3/5, la région indécise couvre presque tout ]0,2 ; 0,9[. Un « 10/10 » ne borne un taux de fuite qu'à environ 3/n en borne supérieure (illustratif : 0/10 → ≈ 26 %). Les instruments 1 à 4 (5 à 10 requêtes) sont dans le même cas : un taux « 100 % / 0 % » sur dix essais n'exclut pas un taux d'échec de l'ordre de 20 %.
- **Exp. 3 (A/A sur un monde).** Si le nombre de vraies découvertes par run suit une loi de comptage de moyenne λ (modèle de Poisson, HYPOTHÈSE), |X₁ − X₂| a un écart-type ≈ √(2λ) et une masse discrète. Un δ = 20 % de la moyenne est inférieur à une unité dès que λ < 5 : le critère n'est pas jugeable. Pour qu'un écart relatif de 20 % dépasse deux écarts-types, il faut λ ≳ 50 par run (illustratif), bien au-delà de ce qu'un monde planté à 1,5–2 USD (estimé) peut produire.
- **Exp. 4 (différence de ratios sur 3 mondes).** Unité d'analyse = monde, n = 3 par bras : un test apparié a au plus 2 degrés de liberté ; l'écart-type de la différence moyenne est σ_monde/√3. Si σ_monde (variance inter-mondes de V/$) est de l'ordre de l'effet attendu, la puissance est proche du risque de première espèce. Non jugeable tant que k_mondes n'est pas choisi par un calcul de puissance.
- **Exp. 5 (binomiale conditionnelle au nombre de promotions).** Le dénominateur (promotions) est lui-même aléatoire et petit ; si E[promotions] par bras < 10 (illustratif), aucune différence de taux de fausses promotions n'est estimable avec un intervalle utile.
- **Instrument 5 (courbe score(N)).** Le max de N tirages a une loi de valeur extrême dont la variance ne décroît pas avec N ; 3 réplications par point ne permettent pas de distinguer monotonie et bruit.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Monde « bruit pur »** (aucune loi vraie au-delà du nul) pour chaque bras : sans lui, un bras qui gagne en T peut gagner en fabriquant des artefacts, et l'exp. 5 n'a pas de plancher.
- **Reformulations algébriques des lois connues** passées à l'oracle et au compteur de « vraies découvertes » : doivent compter 0 ; sinon T est gonflé par du nul.
- **Garde loi plantée sur paraphrase et sur forme numérique** : B pose le `grep -F` comme plancher ; un plancher qui ne couvre que la chaîne exacte laisse passer la fuite la plus probable (loi recopiée sous une autre notation). Son absence rend toute « découverte » non attribuable.
- **Sélection aléatoire de M parmi N** comme témoin du témoin : sans elle, on ne sait pas si « meilleur de N » apporte quoi que ce soit au-delà du tirage.
- **Rejeu d'une même liste de fiches sous deux étiquettes de bras** : vérifie que l'évaluation oracle ne dépend pas de la provenance (E le propose ; je m'en sers).

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Deux règles de sélection différentes dans l'exp. 1.** Le Témoin-Filtre soumet les M fiches choisies par un script mécanique ; Exp-Minimal « soumet ses M meilleures fiches », choisies par l'agent. La comparaison confond deux facteurs : l'accès à l'exécution *et* la règle de sélection finale. Pour isoler l'expérimentation, le même filtre mécanique doit s'appliquer aux candidats des deux bras (C le fait à l'exp. 2 mais pas à l'exp. 1).

2. **Le témoin est construit pour sur-ajuster.** Un max de N sur l'erreur de développement sélectionne, parmi N lois indépendantes, celles qui collent le mieux à l'échantillon : par construction, la fraction de sur-apprises croît avec N. Le bras Exp-Minimal, qui en produit moins, gagne sur F/$ par construction, pas par vertu. Il faut soit un filtre avec pénalité de complexité gelée, soit un partage développement/validation interne du filtre, et publier F/$ séparément (C le fait, mais le seuil ne porte que sur V/$).

3. **Le contrôle négatif « sortie constante "aucune anomalie détectée" » injecte une fausse information.** Ce n'est pas un contrôle « sans information » : c'est un signal positif constant qui peut conforter des lois fausses. Le résultat « doit sous-performer Témoin-Filtre » n'est pas une condition de validité de l'instrument ; si le contrôle aveugle *égale* le témoin, l'instrument n'est pas cassé, il montre que la boucle sans information ne nuit pas. E propose un masquage explicite sans résultat fabriqué ; sur ce point, je préfère E et le dis.

4. **Seuil « +20 % et > 2σ₀ » avec σ₀ estimé d'un seul A/A.** Un pilote à deux runs donne un estimateur de σ₀ à un degré de liberté ; sa loi (chi-deux à 1 ddl, à un facteur près) est si dispersée que « 2σ₀ » peut valoir, selon le tirage, de 0,1 à 4 fois la vraie valeur (illustratif). Le seuil n'est pas gelé : il est tiré au sort.

5. **Exp. 2 : hétéroscédasticité construite.** À budget égal, 2 générations de Sakana contre 50 d'Exp-Minimal : la variance de l'estimateur de V/$ du bras Sakana est de l'ordre de 25 fois celle du bras minimal (illustratif, sous indépendance des générations). Tout écart de 25 % est noyé dans la variance du bras pauvre. Le protocole ne peut rejeter H_A que par manque de données du candidat, ce qui n'est pas une falsification.

6. **Issues de l'exp. 2 non exhaustives (B4).** Trois issues listées ; manquent les cas « (a) et (b) battent tous deux Exp-Minimal », « un seul bat sans atteindre +25 % », et l'indécision. Chaque issue doit falsifier quelque chose ; un cas non prévu ne falsifie rien.

7. **« Batterie de mondes de complexité graduée » non spécifiée.** Si la gradation est choisie après qu'on connaît les forces des bras, fuite entre construction et évaluation.

8. **Instrument 3 : l'artefact est trop grossier.** « Loi qui prédit une croissance linéaire sur des données périodiques » : un modèle en zéro-coup, qui est pourtant la « vérification mécanique à battre », rejettera aussi cette loi ; le test ne discrimine pas l'outil du modèle sans outil. L'artefact doit être apparié à la difficulté des mondes (loi fausse plausible sur l'échantillon vu).

9. **« Question tranchée pour 8,40 USD »** : à 3 mondes et 2 USD par bras, le nombre attendu de vraies découvertes par bras est faible ; voir (b). L'affirmation dépasse ce que le dessin peut réfuter.

10. **Crash d'outil confondu avec inutilité de l'expérimentation.** Si l'outil `exec_python` échoue (pont, JSON, quota), Exp-Minimal perd sans qu'on sache si c'est la boucle ou la plomberie. C ne demande pas de compter le taux d'exécutions réussies par session (E le fait à son duel de qualification).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Exp. 1, différence relative de V/$.** Sous un modèle de Poisson pour V (HYPOTHÈSE), l'écart-type relatif de V/$ par bras est 1/√λ. Pour qu'un +20 % soit à deux écarts-types de la différence, il faut λ₁ + λ₂ ≈ 2·(2/0,2)² = 200 vraies découvertes cumulées, soit λ ≈ 100 par bras (illustratif). À 2 USD par bras sur un monde dont la course entière coûte 1,5–2 USD (estimé), λ est vraisemblablement de l'ordre de quelques unités : le seuil de +20 % n'est pas jugeable. Le critère devient jugeable seulement si l'effet réel est de l'ordre de plusieurs fois λ, ce qui ne se décide pas avant d'avoir vu les données.
- **Seuil 2σ₀ à 1 ddl.** L'intervalle de confiance à 95 % de σ₀ estimé à 1 ddl couvre environ [0,45σ ; 32σ] (illustratif, loi chi-deux) : la décision dépend du tirage du pilote.
- **Exp. 2, bras à n_gen = 2.** Si les générations de Sakana ont une variance inter-générations non nulle, l'intervalle de V/$ pour ce bras a une demi-largeur ∝ σ/√2 ; pour tout σ comparable à l'effet, l'intervalle couvre le seuil : indécidable par construction. La comparaison n'est jugeable que si l'on apparie le nombre d'unités d'analyse (mondes) et non seulement le budget, ou si l'on modélise explicitement la variance par génération.
- **Contrôle « bruit pur ».** Sous le nul, F par bras suit une loi de comptage dont l'estimation d'un taux de fausses promotions ≤ α exige E[fiches soumises] ≫ 1/α ; avec M petit et α = 5 % (illustratif), M·k_mondes doit dépasser une centaine pour que « ≤ α » soit distinguable de « ≈ 2α ».
- **Instrument 1, « détection ≥ 80 % »** : la proportion de lois plantées détectées se mesure sur le nombre de lois plantées, qui est petit par monde (le texte v66 en liste un nombre non donné dans les faits) ; l'intervalle d'une proportion sur moins de 10 lois ne franchit pas 80 % dans le bon sens même à 100 % observé.

### (c) Contrôles négatifs dont l'absence serait fatale

- **A/A sur Exp-Minimal lui-même** (C ne fait l'A/A que sur le témoin) : la variance d'une boucle multi-tours n'est pas celle d'un tirage indépendant.
- **Monde bruit pur à l'exp. 1**, pas seulement à l'exp. 2 : c'est à l'exp. 1 que l'on tranche « aucun scientifique » ; sans plancher sur F, un bras peut gagner V/$ en inflant les soumissions fausses.
- **Reproductibilité de l'exécuteur** : exécuter deux fois le même script sur les mêmes épisodes doit donner la même sortie ; sinon l'agent reçoit du bruit qu'on attribuera à l'expérimentation.
- **Épisodes de développement sans la réponse** : vérifier qu'aucune loi plantée n'est reconstruible exactement à partir du seul développement (sinon T est vrai par construction pour tout bras qui ajuste).
- **Contrôle du même filtre appliqué aux deux bras** : rejeu de la liste de candidats d'Exp-Minimal à travers le filtre mécanique du témoin ; si le choix de l'agent et le filtre divergent peu, le facteur « sélection » est neutralisé ; sinon il est confondant.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **L'indécision est un troisième état sans règle d'arrêt.** E pose correctement que l'intervalle chevauchant le seuil reste indécis ; mais aucun des duels ne fixe k (nombre de mondes ou d'exécutions) par un calcul de puissance préenregistré. Sans k gelé, « indécis » est l'issue par défaut, et la décision « nouvelle expérience plutôt qu'un choix » peut être répétée indéfiniment : B4 exige que chaque issue falsifie quelque chose ; une issue indécise prévisible dès le dessin ne falsifie rien. Il faut préenregistrer k tel que, sous l'effet minimal δ, la probabilité d'un intervalle concluant dépasse un niveau fixé.

2. **A/A avec « graines et ordres appariés ».** Même critique qu'à B : si les graines locales rendent les deux étiquettes identiques, Δ_AA ≈ 0 par construction et ε est calibré sur une variance sous-estimée. Le contrôle négatif « rejeu d'une même trace brute sous deux étiquettes » ne teste que l'évaluateur ; il ne mesure pas la variance du bras. Les deux pièces manquantes : A/A à graines *différentes*, et A/A **par bras** (E ne l'exige que pour « la même commande » sans dire laquelle).

3. **Duel mécaniste : le masquage change la trajectoire.** E l'admet en partie, mais le dessin « scripts, quotas et occasions de révision conservés autant que possible » n'est pas un contrôle apparié : un agent qui ne reçoit pas de résultat produit d'autres scripts aux tours suivants. Le duel compare « boucle avec information » et « boucle sans information *et* trajectoire différente ». Une version plus propre : rejouer la trajectoire du bras complet en masquant les résultats à un tour choisi au hasard, et mesurer la divergence des fiches finales ; cela isole l'effet marginal de l'information à trajectoire fixée.

4. **Le témoin est « gelé » mais non spécifié.** La puissance du duel principal dépend entièrement de la force du sélecteur mécanique : avec un sélecteur faible (proche du tirage), H_B est falsifiée trop facilement ; vrai par construction. E n'exige pas que le sélecteur soit le meilleur mécanique disponible ni qu'il soit lui-même comparé au tirage aléatoire (C l'exige dans son instrument 4 ; je le retiens contre E).

5. **Règle oracle d'équivalence des lois : jamais testée.** T compte les lois « distinctes, nouvelles relativement aux lois connues ». Tout repose sur une règle d'équivalence préenregistrée. E ne prévoit aucun test de cette règle (reformulations algébriques, changements de paramétrage, lois composées de lois connues). Si la règle est permissive, T est gonflé par du nul pour tous les bras ; si elle est stricte de façon asymétrique (par ex. selon le style d'écriture d'un bras), elle devient un confondant lié à la provenance.

6. **Le critère S = (T − λF)/C mélange deux objectifs avec un λ « fixé par le directeur ».** Rien à redire au gel ; mais la loi de T − λF est une différence de comptages dont la variance est λ²Var(F) + Var(T) : pour λ > 1, la variance est dominée par F, le terme le moins fréquent et le plus mal estimé. Les seuils δ et η portent sur une quantité dont la variance dépend du choix de λ ; le calcul de puissance doit être refait pour chaque λ, ce que E ne dit pas.

7. **Contrôle négatif du duel principal incomplet.** « Mondes où les lois connues épuisent la grammaire » force T = 0 pour tous : c'est un plancher pour F, pas un contrôle du banc. Il manque un **contrôle positif** (monde où une loi nouvelle est accessible par construction à un bras naïf) pour prouver que le banc peut voir un gain de taille δ. Sans lui, un rejet de H_A est indistinguable d'un banc aveugle.

8. **Tableau des instruments : « Kaimen avec outil » et « Agentic confiné » sont décrits comme des détecteurs d'anomalies semées.** C'est une tâche différente de celle du rôle (proposer des lois sur des épisodes) ; E le reconnaît (« ne remplace pas la course oracle »), mais la rubrique reste alors sans mesure du rôle lui-même ; elle mesure un sous-produit. Le risque de méthode : qualifier une implémentation sur un défi qui ne corrèle pas avec la performance en course.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Bande d'équivalence A/A.** Pour conclure « intervalle entièrement dans [−ε, ε] », il faut que z·σ_Δ/√k < ε − |Δ̂|. Si σ_Δ (écart-type inter-exécutions de S) vérifie σ_Δ > ε·√k/z, l'issue est indécise quelle que soit la vraie valeur. Avec ε « inférieur au gain minimal utile » et k non fixé, c'est la configuration la plus probable à petit budget.
- **Duel principal.** ΔS est une différence de ratios de comptages ; sous Poisson (HYPOTHÈSE), Var(ΔS) ≈ (λ_T,1 + λ²λ_F,1 + λ_T,2 + λ²λ_F,2)/C². Pour δ exprimé en unités de S, la condition de jugeabilité est k ≥ (z_α + z_β)²·Var(ΔS)/δ². Tant que les λ par monde ne sont pas mesurés (pilote court mesuré, que E demande d'ailleurs), k est inconnu et le duel ne peut pas être préenregistré avec une puissance.
- **Duel mécaniste.** L'effet η est un sous-effet de δ (gain dû à l'information ⊂ gain total) ; sa détection exige un k plus grand que celui du duel principal, à variance égale. Si le dessin alloue le même k aux deux duels, le mécaniste est structurellement moins puissant et son issue indécise est attendue.
- **Duel de qualification.** r est une proportion sur n tâches synthétiques ; pour que l'intervalle franchisse r_⋆ dans le bon sens, il faut n ≳ z²·r_⋆(1 − r_⋆)/(r̂ − r_⋆)² ; avec r_⋆ élevé (fiabilité d'une commande externe) et r̂ proche de r_⋆, n atteint des centaines (illustratif) : le coût de qualification peut dépasser celui du duel.
- **Porte « toute sortie du périmètre invalide ».** C'est une décision à 0 fuite observée sur n attaques ; la borne supérieure du taux de fuite est ≈ 3/n : avec 10 attaques, on n'exclut pas 25 % (illustratif). E le dit presque (« pas une preuve absolue ») ; la règle doit fixer n.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Test de la règle d'équivalence oracle** : lot de reformulations, de compositions de lois connues et de lois vraies réécrites ; T doit être 0 sur le nul et constant sous reformulation. Sans lui, T n'a pas de sens.
- **A/A par bras à graines différentes**, pas seulement rejeu de trace.
- **Contrôle positif du banc** (monde à loi nouvelle accessible) : sans lui, un rejet de H_A n'est pas interprétable.
- **Sélecteur du témoin contre tirage aléatoire** : sans ce test, la victoire de la boucle sur le témoin est peut-être une victoire sur un sélecteur mort.
- **Reproductibilité de l'exécuteur** (même script, même sortie) pour que le duel mécaniste mesure de l'information et non du bruit.
- **Clés et artefacts dans l'image** : E nomme caches, montages, variables ; le contrôle négatif concret — bac lancé avec une fausse clé semée dans un emplacement de cache, et vérification qu'elle n'apparaît ni dans les journaux ni dans les requêtes au relais — n'est pas dans le tableau. Son absence rend non attribuable toute « découverte » coïncidant avec une pièce publique.

---

## Note de position (sans fusion)

Je retiens contre B son usage du verdict du juge dans le critère de comparaison, contraire à N-058, et je le signale comme le défaut qui invalide le plus directement son dessin. C et E convergent vers une boucle minimale ; je ne les harmonise pas : C paie sa simplicité par des seuils non jugeables (2σ₀ à 1 ddl, +20 % à λ faible, bras Sakana à deux générations) et un contrôle négatif qui fabrique un signal ; E paie sa rigueur par une issue indécise sans règle d'arrêt et un témoin non spécifié. Aucune des trois ne fixe k par un calcul de puissance avant préenregistrement ; c'est la condition commune sous laquelle toutes leurs mesures deviennent non jugeables.

FIN-DE-CELLULE