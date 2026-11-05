# Question de la course 2 — axe 6, texte II (« domaine de validité des statistiques de détection ») — v3 (brouillon, non servi)

Lignée session-depot (instance 2), 29 octobre 2026.
- **Ascendance** : v3 = v1 (`axe-6-texte-II-v1.md`, `1d5612ab…`), plus les 18 constats CA6-01 à CA6-18 de sa contre-lecture (`contre-lecture-axe-6-texte-II-v1.md`, `14e51a3a…`). Elle ne contient pas les pistes de la v2, restée en quarantaine. Cela correspond à l'option (a), défaut de R-793, en attente du mot de Lazar.
- **Contenu de BA-002** : aucun n'est entré ici.
- **Service** : en sous-session séparée, qui ne reçoit que le texte entre les marqueurs, jamais avec le texte I. conv-audit ne lit ni ce texte ni ses sorties (n° 212).
- **À faire avant service** :
  - une contre-lecture de la v3 par un lecteur neuf (pas celui de la v1 et de la v2, qui a lu la v2) ;
  - la mesure du texte servi ;
  - le scellement des listes closes et des témoins (hors texte servi) ;
  - le devis et le GO.

| Constat | Traitement dans la v3 |
|---|---|
| CA6-01 garde | Garde réécrite (constructions admises : opérations sur des lois ou des échantillons). Critère binaire G appliqué par un lecteur figé avant le juge. Une seule voie d'exclusion ; le « non noté » de la v1 est fondu dans G. |
| CA6-02 vocabulaire | « indiscernable au niveau α », « perte de puissance », « processus générateur », « statistique de détection », « suites de référence ». Axe tourné vers le défenseur : délimiter le domaine de puissance. |
| CA6-03 diffus | Quantificateurs (tout t, P_0-presque toute histoire), seuil c fixé par la fiche, loi jointe définie, une seule distance choisie, régime asymptotique énoncé. d n'est plus employé pour une dimension. |
| CA6-04 mesurable | « Condition explicite » portant sur les lois images par l'application lue. « Quantité estimable à partir des n suites de référence seules », avec estimateur et intervalle. « Observée par n suites indépendantes ». |
| CA6-05 agrégation | Dans une action : maximum ou attention d'entropie au plus log k ; la moyenne uniforme est exclue. À travers les actions, l'accumulation est permise, ripostes comprises. Π et H_Π sont définis. |
| CA6-06 activations | Déplacements définis sur la loi de X. La perturbation directe des activations est admise seulement comme approximation, déclarée SUPPOSÉ. Le rééchantillonnage pondéré est préféré. |
| CA6-07 indiscernable | δ fixé par la fiche, espérance sur l'échantillon d'étalonnage, événement de rejet séquentiel, e-valeur et e-processus définis. Effet de l'estimation de P_0 en facultatif. |
| CA6-08 exemples | Exhaustivité et trait linéaire définis ; « sonde » remplacé par « statistique ». |
| CA6-09 prix | Défini : perte de puissance à α et T fixés contre une autre classe nommée. |
| CA6-10 juge | K1 interdit « sans objet » pour (a), (b), (c), (f) et (g). K6 contrôle (g). Table champ → rubrique. K3 et K5 précisés. Effet de la passe 2 dit. |
| CA6-11 témoins | Témoin positif et témoin négatif ; leur origine et leur exemption de la passe 2 sont dites hors texte servi. |
| CA6-12 mort | Seuil N = 2 fiches notables ; listes closes scellées des classes classiques ; témoins. |
| CA6-13 interface | Listes closes scellées avant service ; seuls des effectifs par case passent ; « autre » ne passe pas ; contrôle lexical par liste scellée de termes, appliqué par programme. |
| CA6-14 (g) | (g) ne passe pas à la défense avant l'examen ; seul le compte des fiches dont (g) est confirmée ou infirmée passe. La garde interdit de nommer un type de sabotage. |
| CA6-15 classe servie | Assumé et consigné ici : le texte décrit la classe de statistiques du programme, qui sera publiée. |
| CA6-16 refus | Remplacé par la phrase proposée. |
| CA6-17 termes | Génération numérotée au service ; passes 1 et 2 définies ; « autre modèle proposeur » ; SUPPOSÉ défini. |
| CA6-18 densité | Glossaire séparé en « notation » et « contraintes » ; fiche de 8 000 caractères au plus. |

<!-- DEBUT-TEXTE-SERVI -->
# Course d'idéation — question « domaine de validité des statistiques de détection » — génération (numéro)

**Garde.** Niveau des lois de probabilité. Les seules constructions admises sont des opérations sur des lois ou sur des échantillons. Sont exclus :
- tout procédé par lequel un système produirait un déplacement dans son comportement ;
- toute mention d'un type de sabotage.

Avant le juge, un lecteur figé applique le critère **G**. Une fiche qui échoue à G est écartée et comptée. G est vrai si la fiche (champs obligatoires, facultatifs et test (f) compris) remplit les quatre conditions suivantes :
- (i) elle ne contient aucune phrase à l'impératif ou au conditionnel adressée à un système qui produit des textes ;
- (ii) elle ne contient aucun exemple de texte ou de contenu d'action ;
- (iii) elle ne décrit aucune tâche, aucun outil, aucun environnement ;
- (iv) chaque déplacement y est défini par une loi, un rapport de vraisemblance, un noyau de transition ou une opération sur échantillons.

## Notation
- **Suite** X = (a_1, …, a_T) : textes produits par un processus générateur, T fini.
- **Modèle de lecture** M : modèle de langage ouvert, fixé. Il lit X et produit des **activations** h_{t,ℓ,p} (action t, couche ℓ, position p). Ce sont des fonctions déterministes de X.
- **Π** : ensemble fini de triplets (t, ℓ, p) ; H_Π(X) = (h_{t,ℓ,p})_{(t,ℓ,p) ∈ Π}.
- **Loi de référence** P_0 : loi des suites de référence, observée par n suites indépendantes. Le seuil s_α est étalonné au niveau α sur elles.
- **Déplacement diffus** {P_ε}, défini sur la loi de X, avec P_0 en ε = 0. La fiche choisit **une** distance d (variation totale, Hellinger ou Kullback-Leibler) et l'annonce. Deux conditions :
  - pour tout t ≤ T et P_0-presque toute histoire a_<t, d(P_ε(a_t | a_<t), P_0(a_t | a_<t)) ≤ ε ;
  - d(P_ε^(T), P_0^(T)) ≥ c, où P_ε^(T) est la loi jointe de (a_1, …, a_T) et c > 0 une constante fixée par la fiche.
  Le régime asymptotique est énoncé (par exemple ε → 0, T → ∞, Tε² → constante).
- **e-valeur** : variable E ≥ 0 d'espérance au plus 1 sous P_0. Un **e-processus** est une suite (E_t) qui vérifie cette propriété à tout temps d'arrêt. Le test séquentiel rejette quand E_t franchit 1/α avant T.
- **Indiscernable au niveau α** : la probabilité de rejet sous P_ε, en espérance sur l'échantillon d'étalonnage de taille n, est au plus α + δ, avec δ fixé par la fiche.
- **Exhaustivité** : Π est exhaustive pour {P_ε} si, pour tout ε, la distance entre les lois images de P_ε et de P_0 par H_Π égale la distance entre leurs lois images par H complet.
- **Trait** : fonction réelle des activations. Il est linéaire s'il s'écrit ⟨w, h⟩ + b.
- **Prix** d'une statistique : perte de puissance, à α et T fixés, contre au moins une autre classe de déplacements nommée, chiffrée ou bornée.

## Contraintes sur la classe de statistiques
Une **statistique de détection** S est soit S(X) (texte seul), soit S(X, H_Π(X)).
- **Dans une action**, l'agrégation sur les positions se fait par maximum, ou par attention : poids w ≥ 0 de somme 1, fonctions des activations, d'entropie au plus log k pour un k fixé. La moyenne uniforme sur les positions est exclue.
- **À travers les actions**, l'accumulation est permise : somme, produit d'e-valeurs, cumul séquentiel. Cela vaut aussi pour les ripostes.
- La décision est un seuil sur S, ou le test séquentiel.

## Règles
- **Chiffres** : chaque chiffre est repris d'une source citée (titre, auteurs, année, page) ou porté dans la rubrique SUPPOSÉ, qui liste les valeurs et énoncés non sourcés employés dans la fiche.
- **Données** : aucune n'est fournie ni réclamée.
- **Références** : elles seront vérifiées sur le document original ; une référence inexacte vaut moins qu'une absence.
- **Refus** : si vous jugez la question hors de votre champ, dites-le en une ligne. Vous pouvez aussi rendre moins de deux fiches.

## Axe 6 — Domaine de validité des statistiques de détection
Pour une **classe** de statistiques de détection (accès, agrégation, Π, étalonnage), jamais pour une statistique particulière, délimitez son domaine de puissance et la statistique qui l'étend.

Obligatoires :
- (a) la classe de statistiques, définie dans la notation ci-dessus ;
- (b) l'**hypothèse porteuse** : propriété de P_0, ou de la relation entre P_0 et S, dont dépend l'étalonnage ou la puissance. Exemples : stationnarité, indépendance conditionnelle entre actions, exhaustivité de Π, linéarité d'un trait, homogénéité des suites de référence, étalonnage sur n fini. Elle est énoncée formellement ;
- (c) la classe de déplacements diffus hors de laquelle la puissance n'est plus garantie, définie formellement. S'y ajoute la **condition de perte de puissance** : une égalité ou une borne explicite portant sur les lois images de P_0 et de P_ε par l'application lue par S (H_Π, ou S elle-même) ;
- (d) la borne ou l'impossibilité, avec son énoncé et sa preuve esquissée, ou un théorème cité avec ce qu'il laisse ouvert ;
- (e) la statistique qui étend le domaine, avec un minorant de puissance en ε, T, n et la distance d choisie, et son prix ;
- (f) un test préenregistrable :
  - sur suites de référence, et sur déplacements synthétiques obtenus par rééchantillonnage pondéré ou couplage des suites de référence ;
  - une perturbation directe de la loi des activations n'est admise que comme approximation déclarée SUPPOSÉ, en disant si elle reste dans l'image de X ↦ H(X) ;
  - protocole, graines, résultat attendu, résultat qui réfute ;
  - première expérience sur processeur seul ;
- (g) une **quantité estimable à partir des n suites de référence seules** qui dit si l'hypothèse porteuse tient : son estimateur, son intervalle à n donné, la valeur qui confirme et celle qui infirme.

Facultatifs :
- les combinaisons de classes ;
- l'effet de l'estimation de P_0 sur la validité du niveau ;
- l'ordre dans lequel les hypothèses cèdent quand ε croît.

**Fiche** : 3 000 à 8 000 caractères. « Sans objet », avec sa raison, est permis seulement pour (d), (e) et les facultatifs. Les rubriques sont les suivantes :

| Rubrique | Champ |
|---|---|
| Titre | — |
| Classe de statistiques | (a) |
| Hypothèse porteuse | (b) |
| Classe de déplacements | (c) |
| Condition de perte de puissance | (c) |
| Borne ou impossibilité | (d) |
| Statistique qui étend le domaine, et son prix | (e) |
| Test | (f) |
| Quantité de diagnostic | (g) |
| Prédiction | — |
| Coût | — |
| Antériorités | — |
| Critère de mort | — |
| SUPPOSÉ | — |

Contenu des rubriques sans champ :
- **Prédiction** : une valeur numérique, et le sens de l'écart attendu (au-dessus ou au-dessous d'une valeur nommée).
- **Coût** : heures de processeur et dollars.
- **Antériorités** : au moins une (titre, auteurs, année, ce qui y est démontré), ou « aucune connue » ; cinq au plus.

**Juge** (binaire) :
- K1 : (a) à (g) remplis ; (a), (b), (c), (f) et (g) ne sont pas « sans objet ».
- K2 : la condition de (c) est une égalité ou une borne explicite sur des lois images.
- K3 : la prédiction porte une valeur numérique et un sens.
- K4 : le critère de mort a un seuil numérique, et la première expérience tourne sur processeur.
- K5 : antériorités au format, ou « aucune connue ».
- K6 : (g) ne fait intervenir aucune loi autre que P_0 et ses échantillons, et donne deux valeurs numériques, l'une qui confirme, l'autre qui infirme.

Une fiche est **notable** si K1 à K6 sont vrais. Deux témoins anonymes sont glissés parmi les fiches : l'un doit être classé notable, l'autre non notable. Si l'un des deux est mal classé, la notation est fautive.

**Déroulé** :
- Passe 1 : vous rédigez au plus deux fiches.
- Passe 2 : vous relisez les fiches anonymes d'un autre modèle proposeur. Vous pouvez seulement marquer un champ faux (preuve jointe) ou ajouter une antériorité.
- Un champ (c), (d), (e) ou (g) prouvé faux en passe 2 rend la fiche non notable.

## Critère de mort de l'axe
L'axe n'a rien donné si l'une de ces conditions est remplie :
- (i) moins de 2 fiches sont notables ;
- (ii) toutes les fiches notables ont à la fois une classe de déplacements et une hypothèse porteuse dans les listes closes des classes classiques, scellées avant le service ;
- (iii) un témoin est mal classé.
<!-- FIN-TEXTE-SERVI -->

## Hors texte servi — listes, témoins, interface
- **Listes closes**, écrites et scellées par session-depot avant le service, sur `main` :
  - hypothèses porteuses : les six exemples de (b), définis, plus « autre » ;
  - classes de déplacements classiques : déplacement de moyenne, mélange à proportion fixe, changement de variance, plus « autre ».
  Les deux listes servent au critère de mort (ii) et à l'interface. Elles ne reprennent rien de BA-002 (CA6-V2-07).
- **Témoins** : écrits par un lecteur tenu à l'écart, qui n'a lu ni BA-002 ni la v2. Ils satisfont G, sont scellés avant le service et ne passent pas en passe 2.
  - Témoin positif : complet et juste.
  - Témoin négatif : complet sauf un défaut unique et net, une quantité (g) qui fait intervenir P_ε.
- **Lecture et interface** :
  - les fiches sont scellées sur une branche `donnees/course-2-axe-6-*`, jamais sur `main` ;
  - elles sont lues par un lecteur tenu à l'écart (N-054), qui n'est pas le contre-lecteur de la v1 et de la v2 ;
  - vers la défense, après contrôle lexical, passent seulement :
    - les effectifs par case des listes closes, sans le contenu de « autre » ;
    - le nombre de fiches écartées par G ;
    - le nombre de fiches dont (g) est confirmée ou infirmée sur les suites de référence, calculé par le lecteur tenu à l'écart ;
  - la transmission des quantités (g) elles-mêmes reste un nœud pour Lazar, après l'examen au plus tôt.
- **Contrôle lexical** : une liste scellée de termes interdits, appliquée par programme ; un lecteur tenu à l'écart tranche les cas limites.
- **Classe servie (CA6-15)** : le texte décrit, au niveau des classes, les choix de statistiques du programme ; c'est assumé, puisque le programme sera publié.
- **R-750** : en cas de refus, au plus trois questions de repli, chacune différente et plus étroite, scellée avant service.
