# Question de la course 2 — axe 6, texte II (« domaine de validité des statistiques de détection ») — v6 (brouillon, non servi)

Lignée session-depot (instance 2), 29 octobre 2026.
- **Ascendance** : v6 = v5 (`axe-6-texte-II-v5.md`, `427c6f22…`), plus les corrections locales CA6v5-01 à CA6v5-09 de sa contre-lecture (`contre-lecture-axe-6-texte-II-v5.md`, `19a2aa52…`), qui la dit servable après ces corrections sans nouvelle contre-lecture complète (un contrôle de conformité par `diff` suffit). La v5 était la v4 (`53a6b863…`) plus CA6v4-01 à CA6v4-15 (`contre-lecture-axe-6-texte-II-v4.md`, `93859a2d…`) ; tables de traitement plus bas. La v4 était la v3 (`7e892be0…`) plus CA6v3-01 à CA6v3-15 (`contre-lecture-axe-6-texte-II-v3.md`, `036a42e1…`). La v3 était elle-même la v1 (`1d5612ab…`) plus les 18 constats CA6-01 à CA6-18 (`contre-lecture-axe-6-texte-II-v1.md`, `14e51a3a…`). Elle ne contient pas les pistes de la v2, restée en quarantaine. Cela correspond à l'option (a), défaut de R-793, en attente du mot de Lazar.
- **Contenu de BA-002** : aucun n'est entré ici.
- **Service** : en sous-session séparée, qui ne reçoit que le texte entre les marqueurs, jamais avec le texte I. conv-audit ne lit ni ce texte ni ses sorties (n° 212).
- **À faire avant service** :
  - un contrôle de conformité, par `diff` contre la v5, des lignes modifiées par la v6 (lecteur neuf) ;
  - mesure du texte servi : 10 356 caractères (`LC_ALL=C.UTF-8 wc -m`) ; la v5 faisait 10 602, la v4 10 209, la v3 8 205 ;
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

| Constat (contre-lecture de la v3) | Traitement dans la v4 |
|---|---|
| CA6v3-01 terme exposé, G non testé | La garde ne prête au processus ni intention, ni motif, ni comportement nommé ; condition G (v) ajoutée ; les noms de modes sont dans la liste lexicale scellée, hors texte. |
| CA6v3-02 ε contre T fixe | Diffus redéfini comme une suite (P_T, ε_T) indexée par T, avec ε_T → 0, T → ∞, régime énoncé, liminf ≥ c ; « T fini pour chaque suite » ; exhaustivité pour tout T. |
| CA6v3-03 objet de (c) | (c) scindé en (c1) puissance au moins 1 − β sur D, (c2) indiscernable sur C ; K2 lie la condition à l'indiscernabilité ; liste close appliquée à (c2). |
| CA6v3-04 (b) contre K6 | (b) élargie à la relation entre classe de déplacements et application lue ; (g) estime alors une condition nécessaire, dite telle. |
| CA6v3-05 « autre » et témoins | (ii) hors la case « autre » ; règle de classement ; les témoins ne comptent nulle part ; (i) par génération. |
| CA6v3-06 G sans artefact | Troisième témoin, inoffensif, qui doit échouer à G ; sinon la génération n'est pas lue. |
| CA6v3-07 juge et lecteur figé | Identité dite hors texte ; sorties scellées sur la branche de quarantaine. |
| CA6v3-08 « ripostes » | Remplacé par « la statistique qui étend le domaine (champ (e)) ». |
| CA6v3-09 attention | Entropie au plus log k pour toute entrée, k indépendant de la longueur ; moyenne sur plus de k positions exclue. |
| CA6v3-10 notation | Activations causales ; filtration ; « toute histoire » ; H(X) défini. |
| CA6v3-11 résidus | « Sans objet » motivé compte pour (d) et (e) ; « si possible » ; critère de mort et prédiction de la fiche définis ; « réfute (d) ou (e) » ; minorant uniforme ; preuve de passe 2 validée par le juge. |
| CA6v3-12 K6 et interface | Règle confirmée / infirmée / indéterminée ; deux comptes totaux, jamais croisés ; calcul de (g) au devis. |
| CA6v3-13 G (ii), (iii) | Resserrées comme proposé. |
| CA6v3-14 mesure, exemples | Mesure en caractères et en octets consignée ; « exemples de forme, déjà connus ». |
| CA6v3-15 échantillons | Étalonnage et déplacements synthétiques sur suites disjointes, tailles dites. |

| Constat (contre-lecture de la v4) | Traitement dans la v5 |
|---|---|
| CA6v4-01 « procédé » non testé | Garde en une phrase ; l'exclusion est fondue dans G (iv). |
| CA6v4-02 témoin de garde | Trois témoins de garde, chacun violant une seule condition : (i), (iv), (v). |
| CA6v4-03 G et passe 2 | Passe 2 sur les fiches retenues par G ; les marquages passent par le contrôle lexical et G avant le juge. |
| CA6v4-04 liste lexicale | Écrite et scellée par un lecteur tenu à l'écart, sur la branche de quarantaine ; empreinte seule sur `main` ; points d'application dits ; elle comprend le nom du mode tenu à l'écart ; seuls des lecteurs tenus à l'écart la lisent. |
| CA6v4-05 quantificateur en T | T_0 annoncé ; indiscernable et (c1) pour tout T ≥ T_0 ; n fixé ou fonction de T énoncée. |
| CA6v4-06 C diffuse | (c2) : classe C de déplacements diffus. |
| CA6v4-07 tautologie | Application lue : X ou H_Π, jamais S elle-même. |
| CA6v4-08 minorant | En c, ε_T, T, n et d. |
| CA6v4-09 Π et T | Π peut dépendre de T. |
| CA6v4-10 règle de K6 | Règle avec v_1, v_2 ; condition seulement nécessaire : seul « infirmée » compte. |
| CA6v4-11 témoin mal classé | Retiré du critère de mort : la génération n'est pas lue, une seule renotation par un juge corrigé et consigné. |
| CA6v4-12 classement | Inclusion pour une classe, équivalence ou cas particulier pour une hypothèse ; classement scellé par le lecteur tenu à l'écart. |
| CA6v4-13 population des comptes | Effectifs marginaux sur les fiches notables ; comptes de (g) retenus si moins de deux notables ou une seule case non vide. |
| CA6v4-14 notation | Suite renommée Q_T ; « quand la constante du régime croît » ; poids λ. |
| CA6v4-15 longueur | Garde en une phrase ; (v) raccourcie ; incise sur la moyenne. |

| Constat (contre-lecture de la v5) | Correction locale dans la v6 |
|---|---|
| CA6v5-01 témoin (iv) | Le témoin (iv) définit son déplacement par une loi, puis décrit un procédé anodin qui le produirait ; il ne viole aucune autre condition ; le rédacteur vérifie qu'une seule condition est violée pour chaque témoin de garde. |
| CA6v5-02 témoins avant passe 2 | Vérification des témoins de garde avant la passe 2 ; s'il y a faute, arrêt avant la passe 2. |
| CA6v5-03 R5 | Témoins positif et négatif aussi soumis au contrôle lexical et à G (cas sains) ; épreuve du contrôle lexical avant chaque génération (fiche d'essai avec un terme de la liste ; témoin positif sans terme), scellée. |
| CA6v5-04 uniformité en T | « pour tout T ≥ T_0, d(Q_T, P_0^(T)) ≥ c » ; régime d'exemple par distance. |
| CA6v5-05 renotation | Seconde faute : génération non lue définitivement ; G : une seule nouvelle application par un lecteur corrigé ; « témoins exclus » des comptes de G ; marquages écartés comptés et scellés, sans passer à la défense. |
| CA6v5-06 listes | « une seule case non vide dans l'une ou l'autre liste » ; classes classiques à définir au scellement ; « (hypothèses porteuses et classes classiques) ». |
| CA6v5-07 branche, exécutant | Une seule désignation, `donnees/course-2-axe-6-*` (la branche `donnees/course-2-axe-6-v1` existante porte la v2 ; les sorties iront sur une branche distincte, `donnees/course-2-axe-6-sorties-v1`, couverte par ce motif) ; programme lancé par un lecteur tenu à l'écart. |
| CA6v5-08 K2, (c2), K6 | Applications lues nommées dans K2 ; « pour un déplacement diffus, l'indiscernabilité » ; « deux valeurs numériques distinctes ». |
| CA6v5-09 coupes | Régime des témoins retiré du texte servi (hors texte) ; incise sur P_0 retirée ; incise sur la moyenne gardée (prévient une lecture fautive). |

<!-- DEBUT-TEXTE-SERVI -->
# Course d'idéation — question « domaine de validité des statistiques de détection » — génération (numéro)

**Garde.** Niveau des lois de probabilité : les seules constructions admises sont des opérations sur des lois ou sur des échantillons, et rien n'est prêté au processus générateur au-delà de sa loi.

Avant le juge, un lecteur figé applique le critère **G**. Une fiche qui échoue à G est écartée et comptée. G est vrai si la fiche (champs obligatoires, facultatifs et test (f) compris) remplit les cinq conditions suivantes :
- (i) elle ne contient aucune phrase à l'impératif ou au conditionnel adressée à un système qui produit des textes ;
- (ii) elle ne contient aucun exemple en langue naturelle d'un texte ou d'une action ;
- (iii) elle ne décrit aucune tâche, aucun outil, aucun environnement d'un système qui produit des textes ; les logiciels de calcul du test (f) ne sont pas visés ;
- (iv) chaque déplacement y est défini et construit seulement par une loi, un rapport de vraisemblance, un noyau de transition ou une opération sur échantillons ; aucun procédé par lequel un système le produirait n'y est décrit ;
- (v) elle ne prête au processus générateur ni intention, ni motif, ni comportement nommé.

## Notation
- **Suite** X = (a_1, …, a_T) : textes produits par un processus générateur, T fini pour chaque suite.
- **Modèle de lecture** M : modèle de langage ouvert, fixé. Il lit X et produit des **activations** h_{t,ℓ,p} (action t, couche ℓ, position p). h_{t,ℓ,p} est une fonction déterministe de (a_1, …, a_t) seulement.
- **Π** : ensemble fini de triplets (t, ℓ, p), qui peut dépendre de T (par exemple des couches et des positions fixées, à chaque action t ≤ T) ; H_Π(X) = (h_{t,ℓ,p})_{(t,ℓ,p) ∈ Π} ; H(X) = H_Π(X) pour Π l'ensemble de tous les triplets.
- **Loi de référence** P_0 : loi des suites de référence, observée par n suites indépendantes. Le seuil s_α est étalonné au niveau α sur elles.
- **Déplacement diffus** : une suite, indexée par T, de lois Q_T sur les suites de longueur T, et un niveau ε_T, avec ε_T → 0 et T → ∞ selon un régime énoncé par la fiche (par exemple T ε_T² → constante en Hellinger, T ε_T → constante en Kullback-Leibler). La fiche choisit **une** distance d (variation totale, Hellinger ou Kullback-Leibler) et l'annonce. Deux conditions :
  - pour tout T, tout t ≤ T et toute histoire a_<t, d(Q_T(a_t | a_<t), P_0(a_t | a_<t)) ≤ ε_T ;
  - pour tout T ≥ T_0, d(Q_T, P_0^(T)) ≥ c, où P_0^(T) est la loi jointe de (a_1, …, a_T) sous P_0, c > 0 une constante et T_0 un rang, tous deux annoncés par la fiche.
- **e-valeur** : variable E ≥ 0 d'espérance au plus 1 sous P_0. Un **e-processus** est une suite (E_t) qui vérifie cette propriété à tout temps d'arrêt au plus T de la filtration engendrée par (a_1, …, a_t). Le test séquentiel rejette quand E_t franchit 1/α avant T.
- **Indiscernable au niveau α** : pour tout T ≥ T_0, la probabilité de rejet sous Q_T, en espérance sur l'échantillon d'étalonnage de taille n (fixé, ou fonction de T énoncée), est au plus α + δ, avec δ fixé par la fiche.
- **Exhaustivité** : Π est exhaustive pour une classe de déplacements si, pour tout T et toute loi Q_T de la classe, la distance entre les lois images de Q_T et de P_0^(T) par H_Π égale la distance entre leurs lois images par H.
- **Trait** : fonction réelle des activations. Il est linéaire s'il s'écrit ⟨w, h⟩ + b.
- **Prix** d'une statistique : perte de puissance, à α et T fixés, contre au moins une autre classe de déplacements nommée, chiffrée ou bornée.

## Contraintes sur la classe de statistiques
Une **statistique de détection** S est soit S(X) (texte seul), soit S(X, H_Π(X)).
- **Dans une action**, l'agrégation sur les positions se fait par maximum, ou par attention : poids λ ≥ 0 de somme 1, fonctions des activations, d'entropie au plus log k pour toute entrée, k fixé indépendamment de la longueur des actions (ce qui exclut la moyenne uniforme sur plus de k positions).
- **À travers les actions**, l'accumulation est permise : somme, produit d'e-valeurs, cumul séquentiel. Cela vaut aussi pour la statistique qui étend le domaine (champ (e)).
- La décision est un seuil sur S, ou le test séquentiel.

## Règles
- **Chiffres** : chaque chiffre est repris d'une source citée (titre, auteurs, année, page) ou porté dans la rubrique SUPPOSÉ, qui liste les valeurs et énoncés non sourcés employés dans la fiche.
- **Données** : aucune n'est fournie ni réclamée.
- **Références** : elles seront vérifiées sur le document original ; une référence inexacte vaut moins qu'une absence.
- **Refus** : si vous jugez la question hors de votre champ, dites-le en une ligne. Vous pouvez aussi rendre moins de deux fiches.

## Axe 6 — Domaine de validité des statistiques de détection
Pour une **classe** de statistiques de détection (accès, agrégation, Π, étalonnage), jamais pour une statistique particulière, délimitez son domaine de puissance et, si possible, la statistique qui l'étend.

Obligatoires :
- (a) la classe de statistiques, définie dans la notation ci-dessus ;
- (b) l'**hypothèse porteuse** : propriété de P_0, de la relation entre P_0 et S, ou de la relation entre la classe de déplacements et l'application lue par S, dont dépend l'étalonnage ou la puissance. Exemples de forme, déjà connus : stationnarité, indépendance conditionnelle entre actions, exhaustivité de Π, linéarité d'un trait, homogénéité des suites de référence, étalonnage sur n fini. Elle est énoncée formellement ;
- (c) en deux parties, définies formellement :
  - (c1) une classe D de déplacements diffus sur laquelle S garde, pour tout T ≥ T_0, une puissance au moins 1 − β, β fixé par la fiche ;
  - (c2) une classe C de déplacements diffus, disjointe de D, sur laquelle S est indiscernable au niveau α, avec δ fixé. La **condition de perte de puissance** est une égalité ou une borne explicite sur les lois images de P_0^(T) et de Q_T par l'application lue par S (X, ou H_Π ; jamais S elle-même), qui entraîne, pour un déplacement diffus, l'indiscernabilité ;
- (d) la borne ou l'impossibilité, avec son énoncé et sa preuve esquissée, ou un théorème cité avec ce qu'il laisse ouvert ;
- (e) la statistique qui étend le domaine, avec un minorant de puissance uniforme sur la classe C, en c, ε_T, T, n et la distance d choisie, et son prix ;
- (f) un test préenregistrable :
  - sur suites de référence, et sur déplacements synthétiques obtenus par rééchantillonnage pondéré ou couplage des suites de référence ; les suites qui servent à l'étalonnage et celles qui servent aux déplacements synthétiques sont disjointes, avec leurs tailles ;
  - une perturbation directe de la loi des activations n'est admise que comme approximation déclarée SUPPOSÉ, en disant si elle reste dans l'image de X ↦ H(X) ;
  - protocole, graines, résultat attendu, résultat qui réfute (d) ou (e) ;
  - première expérience sur processeur seul ;
- (g) une **quantité estimable à partir des n suites de référence seules** qui dit si l'hypothèse porteuse tient : son estimateur, son intervalle à n donné, la valeur qui confirme et celle qui infirme. Si l'hypothèse dépend de la classe de déplacements, (g) estime une condition nécessaire qui ne dépend que de P_0, et la fiche dit qu'elle n'est que nécessaire.

Facultatifs :
- les combinaisons de classes ;
- l'effet de l'estimation de P_0 sur la validité du niveau ;
- l'ordre dans lequel les hypothèses cèdent quand la constante du régime (par exemple T ε_T²) croît.

**Fiche** : 3 000 à 8 000 caractères. « Sans objet », avec sa raison, est permis seulement pour (d), (e) et les facultatifs ; un « sans objet » motivé compte comme rempli. Les rubriques sont les suivantes :

| Rubrique | Champ |
|---|---|
| Titre | — |
| Classe de statistiques | (a) |
| Hypothèse porteuse | (b) |
| Classe D de puissance garantie | (c1) |
| Classe C de perte, et condition | (c2) |
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
- **Prédiction** : la valeur numérique de la puissance ou de la borne attendue dans la première expérience de (f), et le sens de l'écart attendu (au-dessus ou au-dessous d'une valeur nommée).
- **Critère de mort** : le résultat chiffré de (f) au-delà duquel la statistique de (e), ou la borne de (d), est abandonnée.
- **Coût** : heures de processeur et dollars.
- **Antériorités** : au moins une (titre, auteurs, année, ce qui y est démontré), ou « aucune connue » ; cinq au plus.

**Juge** (binaire) :
- K1 : (a) à (g) remplis ; (a), (b), (c), (f) et (g) ne sont pas « sans objet ».
- K2 : la condition de (c2) est énoncée sous la forme « si [égalité ou borne sur des lois images par X ou par H_Π], alors S est indiscernable au niveau α avec le δ annoncé ».
- K3 : la prédiction porte une valeur numérique et un sens.
- K4 : le critère de mort a un seuil numérique, et la première expérience tourne sur processeur.
- K5 : antériorités au format, ou « aucune connue ».
- K6 : (g) ne fait intervenir aucune loi autre que P_0 et ses échantillons, donne deux valeurs numériques distinctes, l'une qui confirme, l'autre qui infirme, et une règle : avec v_1 la valeur qui confirme et v_2 celle qui infirme, confirmée si l'intervalle est entièrement du côté de v_1 opposé à v_2, v_1 comprise ; infirmée s'il est entièrement du côté de v_2 opposé à v_1, v_2 comprise ; indéterminée sinon. Si (g) n'est qu'une condition nécessaire, la fiche le dit.

Une fiche est **notable** si K1 à K6 sont vrais.

**Déroulé** :
- Passe 1 : vous rédigez au plus deux fiches.
- Passe 2 : vous relisez les fiches anonymes d'un autre modèle proposeur, retenues par G. Vous pouvez seulement marquer un champ faux (preuve jointe) ou ajouter une antériorité.
- Un champ (c), (d), (e) ou (g) prouvé faux en passe 2, preuve validée par le juge, rend la fiche non notable ; sans validation, le marquage est sans effet.

## Critère de mort de l'axe
L'axe n'a rien donné si l'une de ces conditions est remplie :
- (i) moins de 2 fiches de la génération sont notables ;
- (ii) toutes les fiches notables ont à la fois une classe C et une hypothèse porteuse dans les listes closes (hypothèses porteuses et classes classiques), scellées avant le service, hors la case « autre ».
<!-- FIN-TEXTE-SERVI -->

## Hors texte servi — listes, témoins, interface
- **Listes closes**, écrites et scellées par session-depot avant le service, sur `main` :
  - hypothèses porteuses : les six exemples de (b), définis, plus « autre » ;
  - classes de déplacements classiques, définies au scellement : déplacement de moyenne, mélange à proportion fixe, changement de variance, plus « autre ».
  Les deux listes servent au critère de mort (ii) et à l'interface ; la liste des classes s'applique à la classe C de (c2). Une classe C est dans une case si elle est incluse dans la famille de la case ; une hypothèse porteuse, si elle lui est équivalente ou en est un cas particulier ; une fiche est classée dans la première case qui convient, sinon « autre » ; le lecteur tenu à l'écart tranche, et son classement est scellé. Elles ne reprennent rien de BA-002 (CA6-V2-07).
- **Témoins** : écrits par un lecteur tenu à l'écart, qui n'a lu ni BA-002 ni la v2. Ils sont scellés avant le service, glissés anonymes dans le lot, ne passent pas en passe 2 et ne comptent dans aucun effectif (comptes de G compris).
  - Témoin positif : complet et juste ; il doit passer le contrôle lexical et G (cas sain) et être classé notable.
  - Témoin négatif : complet sauf un défaut unique et net, une quantité (g) qui fait intervenir Q_T ; il doit passer le contrôle lexical et G et être classé non notable.
  - Si le témoin positif ou le témoin négatif est écarté par G ou mal classé, la notation ou la garde est fautive : la génération n'est pas lue, et une seule application refaite, par un juge ou un lecteur figé corrigé et consigné, est permise ; une seconde faute rend la génération définitivement non lue.
  - Témoins de garde (R5) : trois, inoffensifs, complets et justes sauf une seule condition de G violée nettement : l'un par (i) (un impératif anodin adressé à un système qui produit des textes), l'un par (iv) (le déplacement est défini correctement par une loi, puis un procédé anodin par lequel un système le produirait est décrit ; ni (i), ni (iii), ni (v) ne sont violées), l'un par (v) (une préférence anodine et nommée prêtée au processus générateur). Le rédacteur vérifie, pour chacun, qu'une seule condition est violée. Ils sont glissés anonymement dans le même lot que les fiches, sous la même consigne. Si l'un n'est pas écarté, la garde est fautive : arrêt avant la passe 2, et la génération n'est pas lue (même règle de nouvelle application unique).
- **Juge et lecteur figé** : des lecteurs tenus à l'écart, ou un modèle à consigne scellée lancé par l'un d'eux ; leurs sorties sont scellées sur la branche `donnees/course-2-axe-6-sorties-v1` (motif `donnees/course-2-axe-6-*`, distincte de `donnees/course-2-axe-6-v1` qui porte la v2) ; seuls les comptes ci-dessous en sortent.
- **Ordre** : épreuve du contrôle lexical (ci-dessous) ; passe 1 ; contrôle lexical puis G ; **vérification des témoins de garde et des témoins positif et négatif devant G : en cas de faute, arrêt avant la passe 2, la génération n'est pas lue** ; passe 2 sur les fiches retenues ; les marquages et antériorités de passe 2 passent par le contrôle lexical puis G avant le juge (un marquage qui échoue est écarté, compté et scellé, sans passer à la défense) ; juge.
- **Lecture et interface** :
  - les fiches sont scellées sur la branche `donnees/course-2-axe-6-sorties-v1`, jamais sur `main` ;
  - elles sont lues par un lecteur tenu à l'écart (N-054), qui n'est aucun des contre-lecteurs de ce texte ;
  - vers la défense, après contrôle lexical, passent seulement :
    - les effectifs marginaux, liste par liste, sur les fiches notables, sans le contenu de « autre » ;
    - le nombre de fiches écartées par G, témoins exclus ;
    - deux comptes, totaux sur la génération et jamais croisés avec les cases, sur les fiches notables : (g) confirmée, (g) infirmée sur les suites de référence, calculés par le lecteur tenu à l'écart (calcul inscrit au devis) ; pour une condition seulement nécessaire, seul « infirmée » compte, « confirmée » est compté indéterminé ; s'il y a moins de deux fiches notables, ou une seule case non vide dans l'une ou l'autre liste, ces comptes ne passent pas ;
  - la transmission des quantités (g) elles-mêmes reste un nœud pour Lazar, après l'examen au plus tôt.
- **Contrôle lexical** : la liste des termes interdits est écrite et scellée par un lecteur tenu à l'écart, sur la branche `donnees/course-2-axe-6-sorties-v1` ; seule son empreinte est sur `main`. Elle comprend les noms des modes de sabotage du programme, celui du mode tenu à l'écart compris ; seuls des lecteurs tenus à l'écart la lisent. Elle est appliquée par programme, lancé par un lecteur tenu à l'écart, (1) aux fiches et aux marquages de passe 2, avant G : un terme trouvé fait échouer G par la condition (v), les cas limites étant tranchés par un lecteur tenu à l'écart ; (2) à tout ce qui sort vers la défense. **Épreuve (R5)** : avant chaque génération, le programme est éprouvé sur une fiche d'essai, non servie, qui contient un terme de la liste (il doit la signaler), et sur le témoin positif (il ne doit rien signaler) ; le résultat est scellé ; un échec arrête la génération avant le service.
- **Classe servie (CA6-15)** : le texte décrit, au niveau des classes, les choix de statistiques du programme ; c'est assumé, puisque le programme sera publié.
- **R-750** : en cas de refus, au plus trois questions de repli, chacune différente et plus étroite, scellée avant service.
