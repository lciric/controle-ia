# Question de la course 2 — axe 6, texte II (« hypothèses fragiles des statistiques ») — v1 (brouillon, non contre-lu, non servi)

Lignée session-depot (instance 2), 29 octobre 2026. Écrit sur le mot de Lazar relayé par conv-audit n° 212 et consigné par conv-audit en R-490 : l'axe 6 entre dans la course 2 ; session-depot l'écrit, le fait contre-lire et le sert.
Source de forme : la question BA-001 (`docs/notes/ideation-organisme-v1/argon-classes-ecart-v1/question-argon-classes-ecart-v1.md`), écrite par cette lignée avant toute réponse. Rien n'est repris d'une réponse de BA-001 ni de BA-002 (réserve R-790 : la session a reçu un résumé de BA-002 ; rien n'en est entré ici).
**Service** : en sous-session séparée, qui ne reçoit que le texte entre les marqueurs ; jamais avec le texte I (axes de défense). conv-audit ne lit ni ce texte ni ses sorties (n° 212). Sorties : branche de quarantaine, lecteur tenu à l'écart (N-054), interface vers la défense par comptes et classes seulement (n° 208).
**À faire avant service** : contre-lecture R2 par un Opus neuf tenu à l'écart (R-785) ; mesure du texte servi ; devis et GO ; ajout à la fusion sous la main de session-depot (texte I = fusion de conv-audit ; texte II = ce texte).

<!-- DEBUT-TEXTE-SERVI -->
# Course d'idéation — question « hypothèses fragiles » — génération g

**Garde.** Niveau des lois de probabilité. Aucune fiche ne décrit une conduite d'agent, une consigne, une séquence d'actions, ni un procédé concret pour produire un déplacement. Une telle fiche est écartée avant le juge et comptée. Les déplacements synthétiques sont des opérations sur des lois ou des échantillons (rééchantillonnage pondéré, couplage, perturbation d'une loi d'activations), jamais des comportements.

## Glossaire (vaut définition)
- **Suite d'actions** X = (a_1, …, a_T) : textes produits par un agent ; un modèle de langage ouvert M, fixé, lit X et produit des **activations** h_{t,ℓ,p} (action, couche, position), fonction déterministe de X.
- **Statistique de surveillance** S : boîte noire S(X), ou boîte blanche S(X, H_Π(X)) sur un ensemble fini de **positions lues** Π. L'agrégation se fait **par maximum ou par attention** (poids dépendant des activations, concentrés sur peu de positions), jamais par moyenne uniforme. La décision est un seuil, ou un **test séquentiel** à e-valeurs (martingale de test, rejet au-delà de 1/α).
- **Loi de référence** P_0 : loi des suites honnêtes, connue par n suites ; le seuil est étalonné au niveau α sur elles.
- **Déplacement diffus** {P_ε} : P_0 en ε = 0 ; effet par action d(P_ε(a_t | a_<t), P_0(a_t | a_<t)) ≤ ε ; effet cumulé d(P_ε^(T), P_0^(T)) non négligeable (d : variation totale, Hellinger ou Kullback-Leibler).
- **Invisible** : puissance P_ε(S > s_α) ≤ α + δ.
- **Hypothèse porteuse** : propriété de P_0, ou de la relation entre P_0 et S, dont dépend l'étalonnage ou la puissance de S. Exemples : stationnarité, indépendance conditionnelle entre actions, exhaustivité des positions lues, linéarité d'un trait, homogénéité des suites honnêtes, étalonnage sur n fini.
- **Statistique riposte** : statistique qui retrouve de la puissance contre une classe donnée, avec un prix nommé contre les autres classes.

## Règles
Les chiffres sont repris d'une source citée (titre, auteurs, année, page) ou marqués SUPPOSÉ. Aucune donnée n'est réclamée : ni familles d'épisodes, ni statistiques ou directions du programme, ni résultats. Les références seront vérifiées sur le document original ; une référence inexacte vaut moins qu'une absence. Un refus arrête votre tour.

## Axe 6 — Hypothèses fragiles des statistiques
Pour une **classe** de statistiques (accès, agrégateur, positions lues, étalonnage), jamais pour une sonde particulière, nommez l'hypothèse porteuse dont dépend sa puissance, et la classe de lois déplacées sous laquelle elle tombe.

Obligatoires :
- (a) la classe de statistiques visée, définie dans le cadre ci-dessus ;
- (b) l'hypothèse porteuse, énoncée formellement ;
- (c) la classe de déplacements diffus, définie formellement, et la **condition mesurable** sur P_0 et S qui la rend invisible ;
- (d) la borne ou l'impossibilité, avec son énoncé et sa preuve esquissée, ou un théorème cité avec ce qu'il laisse ouvert ;
- (e) la statistique riposte, avec un minorant de puissance en ε, T, n et d, et son prix contre les autres classes ;
- (f) un test préenregistrable, sur suites honnêtes et déplacements synthétiques au niveau des lois : protocole, graines, résultat attendu, résultat qui réfute la riposte. La première expérience tourne sur processeur seul ;
- (g) une **quantité mesurable sur P_0 seule**, sans aucune loi déplacée, qui dit si l'hypothèse tient, avec la valeur qui la confirme et celle qui l'infirme.

Facultatifs :
- les combinaisons de classes ;
- la dépendance en n de l'étalonnage ;
- l'ordre dans lequel les hypothèses cèdent quand ε croît.

Non noté : toute fiche dont (c) ou (f) exige de produire une loi déplacée par un agent plutôt que par une opération sur des lois.

**Fiche** (3 000 à 8 000 caractères ; « sans objet » avec sa raison si un champ est inapplicable) :
- titre ;
- classe de statistiques ;
- hypothèse porteuse ;
- classe de déplacements ;
- condition d'invisibilité ;
- borne ou impossibilité ;
- riposte et prix ;
- test (f) ;
- quantité (g) ;
- prédiction chiffrée et signée (borne, ou puissance prédite en simulation à ε, T et n donnés) ;
- coût (heures de processeur, dollars) ;
- antériorités (au plus cinq : titre, auteurs, année, ce qui y est démontré) ;
- critère de mort ;
- SUPPOSÉ.

**Juge** (binaire) :
- K1 : (a) à (g) présents.
- K2 : condition (c) mesurable, c'est-à-dire écrite comme une égalité ou une borne sur des lois images.
- K3 : prédiction chiffrée et signée.
- K4 : critère de mort à seuil numérique, et première expérience sur processeur.
- K5 : antériorités au format.

Notable : K1 à K5 vrais. Un **témoin planté**, notable par construction, est glissé anonyme ; s'il n'est pas classé notable, la notation est fautive.

**Déroulé** : au plus deux fiches par proposeur. En passe 2, sur les fiches anonymes de l'autre fournisseur : seulement marquer un champ faux (preuve jointe) ou ajouter une antériorité.

## Critère de mort de l'axe
L'axe n'a rien donné si l'une de ces conditions est remplie :
- aucune fiche notable ne porte une condition (c) et une quantité (g) vérifiables ;
- toutes les fiches notables reprennent des classes classiques (déplacement de moyenne, mélange) sans hypothèse porteuse nouvelle ;
- le témoin planté échoue.
<!-- FIN-TEXTE-SERVI -->

## Hors texte servi — interface et lecture
- Fiches scellées sur une branche `donnees/course-2-axe-6-*`, jamais sur `main`.
- Lecture par le lecteur tenu à l'écart (N-054).
- Vers la défense, après contrôle lexical, seulement :
  - le nombre de fiches notables par classe d'hypothèse porteuse et par classe de déplacement ;
  - le nombre de fiches écartées par la garde.
- Transmettre les quantités (g) à la défense serait plus que « comptes et classes » : c'est un nœud pour Lazar, non tranché ici.
- R-750 : en cas de refus, au plus trois questions de repli, chacune différente et plus étroite, scellée avant service.
