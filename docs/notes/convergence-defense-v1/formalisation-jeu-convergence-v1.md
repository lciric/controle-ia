# La non-convergence de la défense unique, lue comme une dynamique de meilleure réponse — formalisation du jeu du pilote, exploitabilité, hypothèses testables — v1

Rédacteur-chercheur neuf (sous-agent), 1er novembre 2026 (UTC). Note de méthode ; rien n'est décidé, scellé ni commis. Pièces lues en entier : `preenregistrement-arene-melange-equilibre-v1-brouillon4.md` (brouillon 4, `305911b7…` selon sa vérification), `verification-arene-melange-v4-brouillon4.md`, `question-convergence-defense-unique-v2.md`, et `arene_melange_v4.py` (`70c77fd5…`) pour les parties nommées : docstring, `Config`, `Moniteur`, `entrainer`, `objectif_detection`, `resoudre_jeu`, `poids_max_min_equilibres`, `meilleure_reponse`, `objectif_lisse`, `lois_tenues`, `Contexte.entrainer`, `trajectoire`, `indicateurs_cycle`, `taux_retours`, `valeur_nulle_I3`, `phase_finale`. Chaque renvoi au code donne la ligne du fichier v4. Le jeu jouet qui accompagne cette note est dans `jouet-openspiel-v1/` (protocole écrit avant, résultat après). Aucun contenu d'attaque : le monde est une famille de lois synthétiques écrite par le programme.

Tout chiffre de l'arène vient du brouillon 4 ou de sa vérification (recopié, non recalculé par moi). Tout résultat de théorie des jeux est marqué **RAPPORTÉ** : aucun des articles cités n'est présent sous `docs/sources/pdf/` (vérifié par les titres des 163 PDF), donc aucun n'est opposable (règle R7) tant qu'il n'a pas été lu sur PDF empreinté.

## 0. Verdict en trois lignes

1. Le bras A du pilote n'est **pas** « une défense ré-entraînée contre la dernière attaque » (question v2, § constat) : c'est un **jeu fictif unilatéral** — le défenseur répond à la moyenne uniforme de **toutes** les attaques passées (plus la loi cible), l'attaquant répond au **dernier** moniteur pur (brouillon 4 l. 348 ; code, docstring l. 40–41 et `trajectoire` l. 1083–1084, 1106–1107). La question v2 est à corriger sur ce point.
2. L'arène mesure déjà l'exploitabilité du dernier itéré **à une constante inconnue près** : (iii) du tour t est la détection de la défense déployée contre sa meilleure réponse, donc v* − expl ; I1 ≈ 0 veut dire « exploitabilité du dernier itéré plate ». Il manque une estimation de v* par tâche et l'exploitabilité de la **moyenne** des moniteurs de A, l'objet dont la théorie parle.
3. Le jouet (OpenSpiel tel quel) voit ce qu'il doit voir : meilleure réponse pure itérée à exploitabilité constante 1,0 et 1,2, périodes 3 et 2 ; jeu fictif à exploitabilité moyenne 0,020 et 0,017 à 2 000 itérations ; jeu fictif unilatéral (lecture de A) dont le dernier itéré reste maximalement exploitable tandis que **la moyenne de l'attaquant** converge vers l'équilibre et que celle du défenseur n'y converge pas en général (0,40 d'exploitabilité sur le second jeu, valeur dérivée avant l'exécution).

## 1. (a) Le jeu du pilote, écrit comme un jeu à deux joueurs

### 1.1 Monde et joueurs

Une tâche est un couple (δ, instance). L'instance fixe une loi cible P_cible (mélange gaussien à K = 3 composantes en dimension d = 6, moyennes de norme 4, écarts-types 1 ; `loi_cible`, § Plan 1 du brouillon) et la loi propre P_0 = N(0, I_6), connue du code et non des bras.

- **Attaquant.** Stratégie pure : un vecteur de paramètres θ = (μ_1..μ_K, σ_1..σ_K) d'une loi P_θ de la famille bornée (|μ_kj| ≤ 5, σ_kj ∈ [0,5 ; 1,5] ; `bornes`), sous la contrainte de comportement dist(θ, cible) ≤ δ, racine de la moyenne sur k des distances de Wasserstein d'ordre 2 au carré entre composantes appariées (`distance`, contrainte de `meilleure_reponse` l. 828–830 : Σ(θ − cible)² / K ≤ δ²). Θ_δ est compact. Stratégie mixte : une loi sur Θ_δ ; dans le code, seules des mixtes à support fini apparaissent (les colonnes du jeu restreint, pondérées par q).
- **Défenseur.** Stratégie pure : un moniteur m = (W, b) à u unités, score s(x) = log Σ_i exp(W_i x + b_i) (u = 1 : linéaire ; `Moniteur`, l. 477–533), **seuillé** au quantile 1 − α des scores sur 20 000 échantillons propres communs (`calibrer`, l. 514–522 ; α = 0,01). Le seuil est fixé par la contrainte de fausses alertes, ce qui fait du défenseur un joueur à un seul objectif. Classe : linéaire (A, B), maxout à t + 1 unités au tour t (D), maxout à 9 unités (B′). Stratégie mixte : une liste [(m_i, p_i)] (`taux_defense`, l. 730–731) : le moniteur est **tiré** selon p à chaque requête, la détection d'une loi Q est Σ_i p_i Pr_Q[s_i(x) > t_i].

### 1.2 Gain et somme nulle

Gain du défenseur contre (m, θ) : **le taux de détection à α**, u(m, θ) = Pr_{x ~ P_θ}[s_m(x) > t_m] ∈ [0, 1]. Gain de l'attaquant : −u (ou 1 − u, ce qui ne change aucune meilleure réponse ni aucun équilibre).

Le jeu est **à somme nulle**, et c'est une conséquence de deux choix du pilote, non une hypothèse gratuite : (i) le taux de fausses alertes est **fixé** à α par calibration, donc le second objectif que le défenseur aurait sinon (ne pas alerter sur le propre) est retiré du gain et mis dans la contrainte ; (ii) l'intérêt de l'attaquant à « rester proche de la cible » est lui aussi retiré du gain et mis dans la **contrainte** dist ≤ δ (pas de pénalité, une borne dure ; `projeter` ramène tout point hors de la boule sur sa frontière). Il reste un seul scalaire, maximisé par l'un, minimisé par l'autre. Si l'on remettait l'un de ces termes dans le gain (par exemple un coût de contournement, piste 5, ou un gain d'attaque qui croît avec la distance), le jeu cesserait d'être à somme nulle et les théorèmes du § 4 ne s'appliqueraient plus tels quels.

La valeur du jeu complet, **v*** = sup_σ_D inf_θ∈Θ_δ Σ p_i u(m_i, θ) (sup sur les mixtes du défenseur dans la classe choisie), existe (gain borné, Θ_δ compact), mais **n'est calculée nulle part** dans le code : elle dépend de la classe de moniteurs et de l'oracle.

Deux approximations séparent ce jeu idéal de ce que le code joue : l'oracle du défenseur maximise un taux de détection **lissé** (sigmoïde de température τ = 0,25, seuil approché par moyenne + z_{1−α} × écart-type des scores propres ; `objectif_detection`, l. 655–673) par quasi-Newton à mémoire limitée depuis 8 départs (`entrainer`, l. 676–716) ; l'attaquant minimise un taux de détection **lissé** (`objectif_lisse`, l. 790–806) par programmation quadratique séquentielle depuis 4 départs tirés, un départ vers l'origine et la dernière attaque (`meilleure_reponse`, l. 815–850), puis retient le candidat au plus petit taux **dur** sur un échantillon de Monte-Carlo. Les deux sont des optimiseurs **locaux** ; le brouillon le dit : (iii) est une borne haute de la valeur contre l'attaquant exact (§ « n'autorise pas »).

### 1.3 Ce que `resoudre_jeu` résout exactement

`resoudre_jeu(G)` (l. 734–757) résout par programme linéaire (primal et dual, solveur HiGHS, contrôle |primal − dual| ≤ 10⁻⁷) le **jeu matriciel à somme nulle restreint** : lignes = les moniteurs produits jusque-là (M_0 puis un par tour), colonnes = la loi cible (colonne 0) puis les attaques produites jusque-là ; G_ij = taux de détection du moniteur i sur 19 998 échantillons de la colonne j (`taux_cache` ; `trajectoire` l. 1068, 1099–1104). Il rend p (mixte du défenseur sur les lignes), q (mixte de l'attaquant sur les colonnes) et la valeur restreinte v_R. Ce n'est **pas** l'équilibre du jeu complet : c'est l'équilibre d'une méta-matrice à T + 1 lignes et T + 1 colonnes, exactement ce que l'oracle double appelle le jeu restreint. Le brouillon le déclare (§ « n'autorise pas » : « rien sur l'équilibre du jeu complet ») et mesure l'écart v_R − V : +0,019 / +0,024 pour B, +0,004 / +0,004 pour B′ (résumé, [M4 § 6]).

Deux propriétés utiles plus loin : (1) pour le p rendu, V(p) = inf_θ Det(p, θ) ≤ min sur les colonnes = v_R, donc v_R est une **borne haute** de la garantie réelle de p, jamais une borne de v* ; (2) `poids_max_min_equilibres` (l. 768–784) calcule, parmi toutes les stratégies d'équilibre du défenseur de ce jeu restreint, le plus petit poids maximal : s'il vaut 1, l'équilibre restreint est **nécessairement pur** (« pureté forcée »), ce qui est la mesure que le § 6 réemploie.

## 2. (b) La dynamique de chaque bras

Notation : tour t = 1 … T = 8 ; M_0 moniteur linéaire commun entraîné contre la cible ; a_0 = cible ; a_t attaque du tour t ; m_t moniteur produit à la fin du tour t.

### 2.1 Bras A — jeu fictif unilatéral côté défenseur, meilleure réponse pure côté attaquant

Vérifié sur le code, `trajectoire` l. 1078–1114 :

1. défense déployée au tour t : `[(moniteurs[-1], 1.0)]`, le **dernier** moniteur, pur (l. 1073–1075) ;
2. l'attaquant calcule a_t = meilleure réponse approchée à ce seul moniteur, avec a_{t−1} parmi ses départs (l. 1083–1084) ;
3. (iii)_t = détection de ce moniteur sur a_t (l. 1087) ;
4. nouveau moniteur m_t = `ctx.entrainer(cb, t, attaques, uniforme, 1)` où `attaques = [cible, a_1, …, a_t]` et les poids valent 1/(t + 1) chacun (l. 1106–1107 ; `Contexte.entrainer` l. 918–938 répartit 2 001 échantillons d'attaque selon ces poids). Le moniteur est donc entraîné contre le **mélange uniforme de toutes les attaques passées, la cible comprise**.

C'est la définition du jeu fictif pour le défenseur : réponse (approchée, dans la classe linéaire) à la **moyenne empirique** des coups de l'adversaire, la cible comptant pour un coup au tour 0. L'attaquant, lui, ne moyenne rien : il répond au dernier coup pur. D'où le nom **jeu fictif unilatéral**. La phrase de la question v2 (« ré-entraînée à chaque tour contre la dernière attaque ») est donc fausse ; le brouillon 4 l. 348 et la docstring l. 40–41 sont exacts. Deux nuances : la « moyenne empirique » de l'attaquant inclut la cible avec le poids 1/(t + 1) (ce n'est pas un coup de l'attaquant, mais c'est une loi à détecter aussi) ; et la réponse du défenseur est locale et lissée, donc pas une meilleure réponse exacte même dans la classe linéaire (hypothèse H-e1 au § 5).

### 2.2 Bras D — même dynamique, classe croissante

Identique à A (l. 1106–1109), mais le moniteur a t + 1 unités au tour t, donc la classe s'élargit d'un tour à l'autre et le dernier moniteur à 9 unités est un maxout. Jeu fictif unilatéral dans une classe qui grandit : D est le témoin qui dit si la non-convergence de A tient à la dynamique ou à la classe (D : (iii) croissant puis plat ≈ 0,40 dès le tour 4 ; I3 − nul −0,28 / −0,38 : pas de retours).

### 2.3 Bras B et B′ — oracle double tronqué

Code l. 1080–1081, 1098–1104, 1117–1118 : au tour t, p = équilibre du défenseur du jeu restreint ; l'attaquant répond à la **mixte** p ; nouvelle colonne ; q = équilibre de l'attaquant du jeu restreint augmenté ; l'oracle entraîne un moniteur contre le mélange q (linéaire pour B, maxout à 9 unités pour B′) ; nouvelle ligne. Défense finale : p sur la matrice 9 × 9. C'est l'**oracle double** de McMahan, Gordon et Blum (2003, RAPPORTÉ), ou la réponse stratégique à une population de politiques avec méta-solveur de Nash (Lanctot et collègues 2017, RAPPORTÉ), tronqué à 8 tours, avec deux oracles approchés. La différence de principe avec A n'est pas seulement « mélange contre dernier moniteur » : c'est **(i) pondération d'équilibre q au lieu de l'uniforme** pour entraîner, et **(ii) déploiement de la mixte p au lieu du dernier pur**. Le § 5 sépare les deux.

### 2.4 Témoins C1, C2, C3, C3′

Sans dynamique propre (l. 1129–1142) : recombinaisons des moniteurs mêmes de B (ou B′) après le tour T. C1 (uniforme) est **la moyenne du jeu fictif appliquée aux moniteurs de B** — pas à ceux de A. Aucun bras du pilote ne déploie la moyenne uniforme des moniteurs de A : c'est la mesure manquante la plus directe (§ 3.3).

## 3. (c) L'exploitabilité, définie et calculable dans ce jeu

### 3.1 Définition

Pour une stratégie mixte du défenseur σ_D = {(m_i, p_i)} et la valeur v* du jeu complet (classe de moniteurs fixée) :

  **expl_D(σ_D) = v* − inf_{θ ∈ Θ_δ} Det(σ_D, θ)** ≥ 0,

le gain que l'attaquant arrache, en meilleure réponse, au-delà de ce qu'un défenseur à l'équilibre lui concède. Symétriquement, pour une mixte de l'attaquant σ_A : expl_A(σ_A) = sup_m Det(m, σ_A) − v*. L'écart de Nash (NashConv) du profil est la somme expl_D + expl_A ; l'« exploitabilité » d'OpenSpiel est leur moyenne (NashConv / 2 ; vérifié par l'essai `test_identite_exploitabilite_matrice_openspiel` du jouet). Un profil est un équilibre si et seulement si les deux termes sont nuls. En somme nulle, expl_D(σ_D) = 0 si et seulement si σ_D est maximin.

### 3.2 Ce que l'arène calcule déjà

- **(iii) = V(bras)** (§ Métrique) = min des deux meilleures réponses (standard, renforcée) à la défense finale figée, évaluée sur 19 998 échantillons frais. C'est **une estimation de inf_θ Det(σ_D, θ)**, biaisée vers le haut (optimiseur local : il ne trouve pas toujours le vrai infimum ; d'où le contrôle « V standard − V renforcé » et l'attaquant indépendant S17), et bruitée (échantillon frais). Donc **expl_D(σ_D) = v* − V, à v* près**, et V sous-estime expl_D (une borne basse de l'exploitabilité ; une attaque meilleure ne peut que l'augmenter). Toute comparaison de V entre bras ou entre tours **à tâche fixée** est une comparaison d'exploitabilités, puisque v* est une constante de la tâche.
- **(iii)_t par tour** (`par_tour["iii"]`, l. 1087) = détection de la défense déployée au tour t contre la meilleure réponse du tour (optimiseur plus léger : 4 départs, 256 échantillons de Monte-Carlo). C'est la **trajectoire de l'exploitabilité du dernier itéré**, à v* près et à l'optimiseur près.
- **I1** = moyenne de (iii) aux tours 5–8 moins aux tours 1–4 = **−(variation de l'exploitabilité du dernier itéré entre les deux moitiés)**. I1 ≈ 0 (+0,002 / −0,001 au pilote) dit : l'exploitabilité du dernier itéré de A est plate. Ce n'est pas un indicateur distinct de l'exploitabilité : c'en est la différence finie. Ce qu'il ne dit pas : à quelle hauteur elle est plate (il faut v*).
- **I3** (taux de retours, `taux_retours` l. 1021–1031) et sa valeur nulle 0,7345 (`valeur_nulle_I3`, l. 1014–1018, moyenne de (t − 2)/(t − 1) sous échangeabilité des déplacements) mesurent **la récurrence de la trajectoire de l'attaquant**, pas l'exploitabilité. Les deux peuvent se produire ensemble (un cycle à exploitabilité constante, comme la meilleure réponse pure du jouet) ou séparément (une exploitabilité plate sans retours, si l'attaquant explore une courbe sans revenir ; des retours avec exploitabilité décroissante, si le défenseur progresse pendant que l'attaquant tourne). I3 − nul = +0,17 et +0,21 : retours au-delà du hasard ; I1 ≈ 0 : exploitabilité plate ; les deux ensemble sont la signature d'un **cycle de meilleure réponse** (§ 4), ce que la Table 5 appelle « cycle ».

### 3.3 Ce qui manque et comment le calculer avec l'optimiseur existant

1. **Une estimation de v* par tâche**, pour lire expl_D en niveau. Borne basse : v* ≥ V(σ) pour toute σ construite (toute garantie atteinte minore la valeur) ; le meilleur V observé sur la tâche parmi les bras (D ou B′, ≈ 0,44 / 0,36 en moyenne) est une borne basse de v* **pour la classe maxout à 9 unités**, et V(B) une borne basse pour la classe linéaire mixte. Borne haute : v* ≤ sup_m Det(m, σ_A) pour toute mixte σ_A de l'attaquant, mais ce sup exige un oracle du défenseur **exact**, que le code n'a pas (optimiseur local) ; l'oracle rend donc une borne basse de la borne haute, inutilisable comme majorant. Conclusion : dans ce jeu, **seule l'exploitabilité du défenseur est estimable (par en dessous)** ; l'écart de Nash des deux côtés ne l'est pas sans oracle exact. On rapportera donc **expl_D relative** = V_réf − V(σ) avec V_réf le meilleur V de la tâche dans la même classe (une borne basse de expl_D, suffisante pour montrer la non-convergence, insuffisante pour prouver la convergence).
2. **L'exploitabilité de la moyenne de A** : construire σ̄_A = {(m_s, 1/(T + 1)) : s = 0 … T} (les moniteurs de la trajectoire de A, poids uniformes — `historique`, l. 1065, 1112) et appeler `meilleure_reponse(σ̄_A, cible, δ, cfg, …, departs_suppl = attaques de A)` puis `taux_defense` sur un échantillon frais, comme `phase_finale` le fait pour les témoins. Une meilleure réponse par tâche, soit à peu près le coût d'un témoin C1. Prédiction de Robinson (§ 4) si A était un jeu fictif des deux côtés : V(σ̄_A) croît avec T ; sous le jeu fictif unilatéral, le jouet montre que ce n'est **pas** garanti (§ 4.3), ce qui en fait une mesure et non une prédiction.
3. **L'exploitabilité du dernier itéré en niveau** : V(A) − V_réf, déjà disponible : B − A = +0,13 / +0,14 ; D − A = +0,36 / +0,32 (tous bras de classe différente, donc des bornes basses de expl_D(A) dans la classe « linéaire mixte » et « maxout 9 »).
4. **Borne de Monte-Carlo** : V est une moyenne de 19 998 indicatrices, erreur-type ≤ 0,0035 ; le biais d'optimiseur domine (S17 : écart maximal par tâche 0,0097 à l'audit d'essai) ; l'incertitude de expl_D relative est celle du rééchantillonnage des instances déjà en place, plus l'attaquant indépendant.

### 3.4 Comparaison avec I1 et I3, en une table

| Mesure | Objet | Ce qu'elle voit | Ce qu'elle ne voit pas |
|---|---|---|---|
| expl_D(dernier itéré) ≈ v* − (iii)_t | moniteur déployé au tour t | si la défense déployée progresse ; niveau d'exploitation si v* est borné | l'allure de la trajectoire de l'attaquant |
| I1 | différence de (iii) entre moitiés | **le signe** de la variation de l'exploitabilité du dernier itéré | le niveau ; une décroissance lente (< S15 = 0,02 sur 4 tours) |
| expl_D(moyenne) ≈ v* − V(σ̄) | mélange uniforme des moniteurs passés | l'objet des théorèmes de convergence (Robinson, regret) ; si « mélanger A » suffirait | rien sur ce que A déploie |
| I3 − 0,7345 | récurrence des déplacements de l'attaque | retours au-delà du hasard : cycle au sens faible (sans période) | si le défenseur progresse pendant le cycle |
| v_R − V | équilibre du jeu restreint contre la garantie réelle | combien l'attaque fraîche dépasse les colonnes passées | la distance à v* |

Lisibilité sur de vrais moniteurs (question v2, point 1) : expl_D(dernier itéré) est lisible — détection contre une équipe rouge fraîche (mesure de Bailey et collègues, PDF `2412.09565v2` présent, non relu ici) ; expl_D(moyenne) l'est au prix d'un ensemble de sondes ; v* ne l'est pas ; I3 suppose une géométrie des attaques (cosinus de déplacements) sans équivalent direct pour des textes.

## 4. (d) Pourquoi une meilleure réponse itérée peut cycler — résultats connus (tous RAPPORTÉ)

### 4.1 Meilleure réponse pure alternée

Dans tout jeu matriciel à somme nulle **sans équilibre pur**, la suite (m_t, a_t) où chacun répond au dernier coup pur de l'autre ne peut pas converger : sa limite serait un point-selle pur. Elle visite un ensemble fini de coups purs : elle est finalement périodique, et l'exploitabilité du dernier itéré, v* − min_j G_ij, est constante le long du cycle. Jouet, résultat 1 : 1,000 à chaque itération et période 3 (pierre-feuille-ciseaux) ; 1,200 et période 2 (second jeu). Aucune source n'est nécessaire : c'est l'absence de point-selle.

Dans l'arène, espaces continus et réponses approchées : pas de période exacte, mais une **récurrence** (retours vers d'anciennes attaques, I3 au-dessus de sa valeur nulle), ce que le pilote observe et ce que le jouet montre en D3 (paires quasi-périodiques, aucune période stricte).

### 4.2 Jeu fictif à somme nulle : les moyennes convergent, pas le dernier itéré

- **Brown, G. W. (1951)**, « Iterative solution of games by fictitious play », dans *Activity Analysis of Production and Allocation* (T. C. Koopmans, dir.), Wiley, p. 374–376 — RAPPORTÉ. Définit la dynamique.
- **Robinson, J. (1951)**, « An iterative method of solving a game », *Annals of Mathematics* 54(2), p. 296–301 — RAPPORTÉ. Dans tout jeu matriciel à somme nulle à deux joueurs, les **stratégies moyennes** des deux joueurs convergent (la valeur du jeu contre les moyennes tend vers v*), quelle que soit la règle de départage des égalités ; rien n'est dit du dernier itéré, qui est pur et reste maximalement exploitable (jouet, P4 : 1,0 et 1,2 à chaque itération pendant que la moyenne descend à 0,020 et 0,017).
- Vitesse : la borne de Robinson est lente (ordre t^{−1/(m + n − 2)}) ; la conjecture de Karlin (O(1/√t)) a un contre-exemple sous départage adverse : **Daskalakis, C. et Pan, Q. (2014)**, « A counter-example to Karlin's strong conjecture for fictitious play », FOCS 2014 — RAPPORTÉ. Le jouet n'établit aucune vitesse.
- Les dynamiques **sans regret** (poids multiplicatifs) garantissent la convergence des moyennes en O(1/√T) en somme nulle : **Freund, Y. et Schapire, R. E. (1999)**, « Adaptive game playing using multiplicative weights », *Games and Economic Behavior* 29, p. 79–103 — RAPPORTÉ.

### 4.3 Jeu fictif unilatéral (ce que A fait) : pas de théorème de Robinson

Robinson suppose que **les deux** joueurs répondent aux moyennes. Dans A, l'attaquant répond au dernier coup. Dérivation directe sur un jeu 2 × 2 (protocole du jouet, § prédictions, écrite avant l'exécution) : le joueur qui répond à la moyenne (le défenseur) pousse la fréquence empirique de l'autre vers son **point d'indifférence**, qui est la stratégie d'équilibre de l'attaquant q* ; la fréquence du défenseur, elle, est l'image de celle de l'attaquant par la règle « je joue la contre de ce qu'il vient de jouer », qui n'a aucune raison d'être p*. Jouet, second jeu : moyenne de l'attaquant à 0,0006 de q* ; moyenne du défenseur (0,60 ; 0,40) contre p* = (0,40 ; 0,60), exploitabilité 0,40 ; sur pierre-feuille-ciseaux les deux moyennes convergent, par symétrie seulement. Conséquence : **ni le dernier moniteur de A, ni la moyenne uniforme des moniteurs de A n'ont de garantie de convergence** ; seule la moyenne uniforme des **attaques** de A en a une (vers q* du jeu complet, si l'oracle du défenseur était exact). Aucune source nommée pour cette dynamique asymétrique : dérivation et observation du jouet, pas un théorème.

### 4.4 Hors somme nulle : le jeu fictif lui-même peut cycler

- **Shapley, L. S. (1964)**, « Some topics in two-person games », dans *Advances in Game Theory* (Dresher, Shapley, Tucker, dir.), Annals of Mathematics Studies 52, Princeton University Press, p. 1–28 — RAPPORTÉ. Exemple 3 × 3 **à somme non nulle** où les moyennes du jeu fictif ne convergent pas. Il ne s'applique pas tel quel au jeu du pilote, à somme nulle (§ 1.2) ; il s'appliquerait si l'on remettait dans le gain un terme propre à un joueur (coût de contournement, pénalité de distance, second objectif du défenseur).
- Classes où le jeu fictif converge : jeux 2 × 2 (**Miyasawa, K. (1961)**, Princeton Econometric Research Program, rapport 33 — RAPPORTÉ), jeux de potentiel (**Monderer, D. et Shapley, L. S. (1996)**, *Journal of Economic Theory* 68, p. 258–265 — RAPPORTÉ), somme nulle (Robinson). Synthèse : **Fudenberg, D. et Levine, D. K. (1998)**, *The Theory of Learning in Games*, MIT Press, chapitre 2 — RAPPORTÉ.

### 4.5 Dernier itéré des dynamiques de gradient en somme nulle : récurrence, pas convergence

Avec des pas de gradient au lieu de meilleures réponses, le dernier itéré des dynamiques sans regret **tourne** autour de l'équilibre au lieu d'y converger : **Mertikopoulos, P., Papadimitriou, C. et Piliouras, G. (2018)**, « Cycles in adversarial regularized learning », SODA 2018, arXiv `1709.02738` — RAPPORTÉ ; **Bailey, J. P. et Piliouras, G. (2018)**, « Multiplicative weights update in zero-sum games », EC 2018 — RAPPORTÉ. Remèdes à dernier itéré convergent, gradients optimistes ou extragradient : **Daskalakis, C., Ilyas, A., Syrgkanis, V. et Zeng, H. (2018)**, « Training GANs with optimism », ICLR 2018, arXiv `1711.00141` — RAPPORTÉ ; **Daskalakis, C. et Panageas, I. (2019)**, « Last-iterate convergence: zero-sum games and constrained min-max optimization », ITCS 2019, arXiv `1807.04252` — RAPPORTÉ. Ces résultats supposent de petits pas des deux côtés ; A n'en est pas une (meilleure réponse complète à chaque tour) ; une variante « petit pas » de l'oracle relève des règles de mise à jour de l'autre sous-agent.

### 4.6 Méthodes de convergence par population (ce que B et B′ font)

**McMahan, H. B., Gordon, G. J. et Blum, A. (2003)**, « Planning in the presence of cost functions controlled by an adversary », ICML 2003 — RAPPORTÉ (oracle double : convergence finie quand les stratégies pures sont en nombre fini ; en continu, si les oracles sont exacts, à une tolérance près). **Lanctot, M. et collègues (2017)**, « A unified game-theoretic approach to multiagent reinforcement learning », NeurIPS 2017, arXiv `1711.00832` — RAPPORTÉ (réponse stratégique à une population de politiques ; l'**exploitabilité** y est la mesure de convergence, usage retenu ici). OpenSpiel : **Lanctot, M. et collègues (2019)**, arXiv `1908.09453` — RAPPORTÉ ; version installée 2.0.2.

PDF présents dans le dépôt et voisins du sujet, **non lus pour cette note** : `2412.09565v2` (Bailey et collègues), `2601.19726v1` (jeux rouge–bleu itérés), `2602.01539v2` (jeu coévolutif attaquant–défenseur), `2511.00554v1` (équipe rouge de sondes), `2605.15377v2` (ensembles de moniteurs).

## 5. (e) Ce que change le fait que A s'entraîne déjà sur l'historique — hypothèses testables

Puisque A répond déjà à la moyenne, « passer au jeu fictif » n'est pas le remède : A **est** le jeu fictif, d'un côté. Les causes possibles de la non-convergence observée (I1 ≈ 0, I3 − nul > 0) se séparent en quatre hypothèses, chacune avec un test sur les pièces existantes ou pour une seule meilleure réponse supplémentaire par tâche. Aucune n'est exclusive ; le D du pilote (même dynamique, classe plus riche, converge vers un plateau) est le témoin commun.

**H-e1 — Oracle du défenseur inexact.** La non-convergence viendrait de ce que m_t n'est pas une meilleure réponse à l'historique même dans la classe linéaire (optimum local, lissage τ, seuil approché). *Prédiction si vraie* : sur la matrice H de A (ligne s = moniteur, colonne t = attaque ; `indicateurs_cycle`, l. 1034–1053, H rendue dans le JSON), la détection du mélange uniforme des colonnes 1 … t par la ligne t (le moniteur entraîné contre lui) est **inférieure**, dans une part non négligeable des tours, à celle d'une ligne s < t sur le même mélange — une meilleure réponse exacte ne peut pas être battue sur son propre objectif par un moniteur plus ancien de la même classe (à l'écart près entre objectif lissé et taux dur). *Test* : calcul sur le JSON du pilote, aucune exécution. *Réfutation* : la ligne t domine toujours (à 0,01 près) : l'oracle n'est pas en cause. *Ce que ça casserait* : si H-e1 tient, un oracle plus lourd (plus de départs, départ chaud depuis m_{t−1}) est la première règle de mise à jour à essayer.

**H-e2 — Classe linéaire trop pauvre : pas d'équilibre pur dans la classe.** Si le jeu « moniteurs linéaires contre Θ_δ » n'a pas d'équilibre pur du défenseur, aucune suite de moniteurs purs ne peut converger vers une garantie v*_lin (valeur en mixte), et le dernier itéré d'un jeu fictif reste exploitable, comme en pierre-feuille-ciseaux. *Prédiction si vraie* : (1) sur le jeu restreint construit des **moniteurs de A** et de ses attaques (matrice H de A, plus la colonne cible), `poids_max_min_equilibres` rend une valeur nettement < 1 (équilibre nécessairement mixte) dans la majorité des tâches ; (2) la valeur restreinte dépasse le meilleur maximin pur, max_s min_t H[s, t], d'au moins la marge m = 0,02 ; (3) V(σ̄_A) (§ 3.3, point 2) dépasse V(A) d'au moins 0,02. Le pilote a déjà un indice indirect : les poids de B (linéaire) ne sont **jamais** purs (support moyen 3,7–3,8), alors que ceux de B′ (9 unités) le sont dans 58–71 % des tâches, pureté forcée : la classe riche a un équilibre pur, la classe linéaire n'en a pas. *Réfutation* : équilibre restreint pur sur les moniteurs de A, et V(σ̄_A) ≈ V(A). *Ce que ça casserait* : si H-e2 tient, aucune règle de mise à jour d'un **seul** moniteur linéaire ne peut converger ; le remède est de déployer une mixte (B) ou d'élargir la classe (D) — ce que le pilote mesure déjà (B − A +0,13, D − A +0,36), mais sans avoir isolé H-e2 comme cause.

**H-e3 — Moyenne uniforme contre pondération d'équilibre.** B entraîne contre q (équilibre de l'attaquant sur le jeu restreint), A contre l'uniforme. Par § 4.3, sous jeu fictif unilatéral, la moyenne uniforme des attaques de A tend vers q* : les deux pondérations devraient se rapprocher quand T croît, mais à T = 8 l'écart peut dominer. *Prédiction si vraie* : le dernier moniteur de B **déployé seul** bat le dernier moniteur de A (V(m_T^B seul) − V(A) ≥ 0,02), à classe linéaire égale et à nombre de paramètres égal (7 contre 7). *Test* : une meilleure réponse par tâche contre `(moniteurs_B[-1], 1.0)` ; aucune racine de décision ; le moniteur existe dans l'état de B. *Réfutation* : écart < 0,02 ou de signe contraire. Variante : entraîner un moniteur linéaire contre q_A (équilibre de l'attaquant sur le jeu restreint de A) et comparer à m_T^A. *Ce que ça casserait* : si H-e3 tient, la règle « entraîner contre l'équilibre restreint, déployer le dernier » est une mise à jour bon marché de A ; si H-e2 tient aussi, elle ne suffira pas.

**H-e4 — La moyenne de l'attaquant converge, celle du défenseur non (signature du jeu fictif unilatéral).** *Prédiction si vraie* : (1) la nouveauté résiduelle des attaques de A (`residu_relatif`, l. 952–961, « nouveauté » par tour) décroît avec t (les attaques se répètent dans un sous-espace), et la mixte uniforme des attaques de A est proche, en détection, de q_A (l'équilibre restreint de l'attaquant) : pour chaque moniteur s de A, |Σ_t H[s, t]/T − Σ_t q_A(t) H[s, t]| ≤ 0,02 en moyenne ; (2) V(σ̄_A) **ne** croît pas de façon monotone avec T (la moyenne du défenseur n'a pas de garantie, § 4.3), à vérifier en calculant V(σ̄_A^{(t)}) aux tours 4, 6, 8. *Réfutation* : moyenne du défenseur à exploitabilité décroissante et nette (alors « déployer C1 sur A » serait un remède, ce que la théorie ne promet pas). *Ce que ça casserait* : rien dans le pilote ; cela fixe quelle moyenne il est licite de déployer.

« A oublie les attaques anciennes » n'est pas une cinquième hypothèse : I2 est recopié sans verdict (CM3-03) et, sous H-e2, la baisse sur les anciennes attaques est **la conséquence** de l'absence d'équilibre pur (un moniteur linéaire ne couvre pas toutes les colonnes) ; le test de H-e1 sépare oubli d'oracle et contrainte de classe.

## 6. (f) Rendre le jeu « posable à classe de fonctions égale » : une condition testable

Le constat du pilote (Q2 « non exercée ») : à classe de 9 unités, les poids de B′ sont purs dans 58–71 % des tâches et cette pureté est **forcée** par le jeu restreint (plus petit poids maximal parmi les équilibres = 1 dans 17/17 et 14/14 tâches pures). Autrement dit, le jeu restreint a un point-selle pur : la question « le mélange bat-il le meilleur moniteur seul ? » n'a pas d'objet, puisque l'équilibre **est** un moniteur seul.

**Condition testable (avant toute comparaison, par tâche, sur le jeu restreint final de la classe considérée)** : le jeu est posable à la marge m si

  **g(tâche) = v_R − max_i min_j G_ij ≥ m**,

c'est-à-dire si la valeur en mixte du jeu restreint dépasse le meilleur maximin pur d'au moins la marge de lecture (m = S6 = 0,02). g ≥ 0 toujours ; g = 0 si et seulement si un point-selle pur existe ; `poids_max_min_equilibres` < 1 implique g > 0 mais pas g ≥ m. La question Q2 est **exercée** à un δ si g ≥ m dans plus de la moitié des tâches de ce δ ; sinon elle est « non exercée par construction », ce qu'on sait **avant** de regarder B′ − D. Avantages : la mesure n'emploie que la matrice G déjà calculée (aucune graine, aucun optimiseur) ; elle est la même pour toute classe, donc elle dit à quelle classe la question se pose. Deux compléments, parce que G est restreint aux attaques passées :

1. **Version « jeu complet »** : g_complet = V(mixte d'équilibre déployée) − max_i V(m_i seul), avec une meilleure réponse fraîche par moniteur du support (9 au plus par tâche) ; c'est le « gain du mélange » réel, borné par en dessous par les optimiseurs ; condition g_complet ≥ m.
2. **Sélection des tâches a priori** (question v2, point 5) : calculer g sur une **classe plus pauvre** (la classe linéaire, où les poids de B ne sont jamais purs) ; la question « mélange contre meilleur seul » se pose alors **à la classe linéaire** : B contre le meilleur moniteur linéaire seul (le moniteur de B de poids maximal déployé seul, témoin « mode » laissé en option à Lazar par CM3-02). Le pilote contient déjà B − A = +0,13, mais A n'est pas le meilleur linéaire seul (H-e1, H-e3).

Artefacts à exclure : g ≥ m obtenu par une matrice bruitée (erreur-type ≤ 0,0035 par cellule : un g de 0,02 est à 5 erreurs-types, un seuil plus petit ne l'est pas) ; ou un mélange calculé sur une matrice dont les colonnes sont les attaques de la trajectoire même (l'attaquant du tour t a été construit contre p_{t−1}, donc G est « plus facile » que le jeu complet ; d'où le complément 1).

## 7. Ce que cette note ne fait pas

- Aucune règle de mise à jour sur l'arène (autre sous-agent) ; aucun calcul sur le JSON du pilote (les tests de H-e1 à H-e4 sont écrits, non exécutés) ; aucune lecture de racine de décision.
- Aucun chiffre de théorie des jeux opposable : toutes les sources sont RAPPORTÉ, à lire sur PDF empreinté (R7) ; les cinq PDF voisins du dépôt n'ont pas été relus.
- Le jouet est matriciel (2 et 3 actions) : rien sur les espaces continus ni sur les oracles approchés ; il montre que la mesure voit le cycle et la convergence, et que la lecture « jeu fictif unilatéral » a une signature propre.
- Le transfert aux vrais moniteurs (question v2, point 6) n'est pas traité.
