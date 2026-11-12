# Proposition P-041 — attaque et défense comme un seul organisme coévolutif, avec l'avantage du terrain à la défense — v1

Lignée session-depot (instance 2), 30 octobre 2026, 15:59 UTC. Nœud de décision (modification du programme) : Lazar décide. Rien n'est lancé.

**Question de Lazar (≈ 16:25 UTC), verbatim** : « peut-être que la défense et l'attaque devraient elles-mêmes être un organisme coévolutif ? qui s'améliore de génération en génération genre course aux armements darwinienne ? mais avec l'avantage du terrain pour la défense qui a les params et recettes de l'attaque et qui peut ainsi tâcher de construire une barrière universelle ? donc barrière construite pas juste sur la base de brainstorms et tests d'hypothèses des organismes mais aussi sur le terrain même de la course aux armements. et comme notre organisme a des générations et des épisodes qui s'améliorent, on peut imaginer que l'attaque et surtout la défense s'affinent de génération en génération ? ce serait quasiment natif non ? » — puis demande d'une version approfondie (expert, données brutes, méthodes, vérification extérieure, reformulation).

Ce que touche la proposition : R-597 (aucun attaquant construit), R-575 (détails concrets scellés ; la défense ne reçoit que comptes et classes), N-054 (modes tenus à l'écart), N-056 (bras aveugle et informé), N-053 (invariant « aucun score de moniteur dans l'entraînement de l'agent » ; aucune chaîne d'évasion opérationnelle avant revue de sécurité extérieure), N-044 et N-045 (objectif ultime, organisme à partir de l'étape 2). Zone **occupée** par la « défense universelle coévolutive » : SafeCoEvo, AgentSafeEvo, EvoSafety, Terekhov et al., RvB (antériorité rapportée, non vérifiée sur PDF ; R7, R8 : zone séduisante, à vérifier plus durement).

## 1. Ce qu'un expert du domaine ferait ici, et que la demande ne dit pas

1. **Nommer le jeu avant de le construire.** Joueurs (défense D, générateur de familles A), gains (taux de détection à 1 % de fausses alertes, contre le dommage), structure d'information, et **concept de solution**. L'« avantage du terrain » (la défense connaît les paramètres de l'attaque) fait de la défense un joueur qui joue en second et informé : c'est un jeu de Stackelberg, et sa solution n'est pas une coévolution mais une **optimisation robuste** : la barrière est le minimax sur la classe déclarée. En apprentissage automatique adverse, c'est l'entraînement adverse (la défense voit la recette de l'attaque) et la robustesse certifiée (une preuve sur un modèle de menace déclaré). Références à vérifier sur PDF (R7) : Madry et collègues 2018 ; Cohen et collègues 2019 ; Tramèr, Carlini, Brendel et Madry 2020.
2. **Séparer trois problèmes que la demande confond.** (i) La **conception robuste** : couvrir la classe déclarée ; se résout par certificat, pas par évolution. (ii) La **découverte** : quelles familles existent hors de la couverture ; c'est le seul rôle utile du côté attaque, et c'est une recherche de nouveauté, pas une optimisation contre les scores de la défense. (iii) La **généralisation** : la barrière tient-elle sur des familles jamais découvertes ; se mesure seulement sur des familles tenues à l'écart. La coévolution n'apporte quelque chose que sur (ii), et elle ne peut rien dire de (iii) si la défense a vu les familles de mesure.
3. **Fixer la granularité de l'information**, sinon l'universalité devient non mesurable. Trois paliers : le **schéma** (classes et plages de paramètres : les listes closes de l'axe 6), les **familles d'entraînement** (instanciées, vues par la défense après chaque génération), les **familles tenues à l'écart** (conçues par les cinq instances, jamais vues, lues une seule fois, N-050). C'est la discipline entraînement, validation, épreuve, appliquée aux familles.
4. **Préenregistrer les pathologies connues de la coévolution et leurs diagnostics** : cyclage (la défense bat la famille A, l'attaque trouve B, la défense passe à B et reperd A), désengagement (un camp domine, plus de pression de sélection), surspécialisation (la défense s'ajuste au répertoire courant de l'attaque : c'est le « péché antigénique originel » de la fiche argon-p2-05 de la course 1). Remèdes et instruments classiques : archives (« panthéon » des adversaires), tournoi maître (chaque génération de défense contre chaque génération d'attaque), graphiques de l'individu courant contre les adversaires ancestraux, concepts de solution de Pareto. Références à vérifier (R7) : Rosin et Belew 1997 ; Cliff et Miller 1995 ; Watson et Pollack 2001 ; Ficici 2004 ; de Jong 2004 ; Popovici, Bucci, Wiegand et de Jong 2012.
5. **Mesurer un progrès absolu, pas relatif.** Une course aux armements fait monter les scores relatifs (la défense bat l'attaque courante) sans que la défense progresse dans l'absolu. L'étalon fixe, posé avant la boucle : familles tenues à l'écart et bancs publics.
6. **Prédire le signe du résultat à partir de la littérature** : l'entraînement adverse contre un modèle de menace transfère mal à un autre (Kang et collègues 2019 ; Tramèr et Boneh 2019, à vérifier). Le résultat scientifique attendu n'est donc pas « la barrière est universelle » mais « le débordement hors de la classe déclarée est de tant », avec un signe préenregistré.
7. **Construire la garde de sécurité avant la boucle** : attaque au niveau des lois sur activations synthétiques, sorties scellées, **aucun score de moniteur réel dans les entrées du générateur** (invariant N-053, vérifié par code comme la garde de calcul), revue extérieure avant tout passage à des agents réels ; et contrôle de la contamination (les familles générées ne doivent pas entrer dans les données d'entraînement des moniteurs).
8. **Quatre bases à battre**, sinon rien n'est montré : défense évoluant seule contre une banque fixe ; défense redémarrée de zéro à chaque génération à budget égal ; attaque sans sélection (recherche aléatoire de familles) ; barrière théorique conçue une fois sur le schéma, sans évolution.
9. **Calculer la puissance et commencer en simulé** : générations × familles × épisodes nécessaires pour voir un effet donné sur les familles tenues à l'écart, d'abord sur le monde simulé sur processeur, avant toute dépense sur carte graphique.

## 2. Les données brutes de départ

- Les **générateurs scellés** des familles de BA-002 (Argon 28, Opus 5.5 25, Fable 25) après le contrôle de pureté (`purete_v2.py`, quarantaine) : activations synthétiques tirées sous chaque famille, avec graines. Seul un exécutant tenu à l'écart les touche.
- Les **épisodes de P3** (240 épisodes, 2 400 actions, activations réelles du modèle à 8 milliards de paramètres) et les scores des moniteurs par famille (`diag/`, scellés) : l'arène réelle, plus tard.
- Les **trajectoires brutes des bancs publics** (SHADE-Arena, ControlArena, MonitoringBench, SLEIGHT-Bench, Liars' Bench) : familles conçues par d'autres, étalon extérieur.
- Les **journaux de l'orchestrateur** sur le monde simulé (manifestes, promotions, fausses promotions sur témoins) : la dynamique de la boucle telle qu'elle est.
- Les **29 fiches brutes de la course 1**, en particulier argon-p2-05 (héritage), argon-p2-08 (mutation de la défense), argon-p1-07 (dilution sans attaquant).
- Les **familles tenues à l'écart** des cinq instances (à produire, scellées avant tout).
- Les **PDF** de coévolution et d'entraînement adverse, à verser et lire (R7).

## 3. Méthodes et outils

- **Formalisation du jeu** (Stackelberg pour la barrière ; recherche de nouveauté pour l'attaque) et concept de solution de Pareto pour l'arène.
- **Barrière certifiée** : minimax sur C1 ∪ C2 ∪ C3 à plages déclarées, sur le monde synthétique ; certificat = taux de détection à 1 % de fausses alertes ≥ x sur toute la boîte de paramètres, par grille plus argument de continuité, ou par tirage aléatoire avec garantie de couverture.
- **Arène coévolutive** à G générations avec archive, tournoi maître et graphiques courant contre ancestral ; score absolu sur l'étalon fixe.
- **Mesure de l'universalité** = débordement hors classe : généralisation à une famille laissée de côté, puis épreuve finale sur les familles des cinq instances, lue une seule fois.
- **Duel préenregistré** héritage contre redémarrage à budget égal (effet, seuil, signe).
- **Simulation de puissance** sur processeur ; devis séparé pour la carte graphique.
- **Outils du dépôt** : `pole/` (cycle, mémoire, proposeur, recombinaison, sélection par pari, porte, tests de mort), le monde simulé, le générateur de pureté en quarantaine, les relais, le collisionneur pour la critique de conception.

## 4. Ce qui, hors de nous deux, vérifierait le résultat

- Les familles tenues à l'écart conçues par cinq instances de fournisseurs différents, scellées avant la boucle, lues une seule fois.
- Les bancs publics, conçus par d'autres, pour le transfert de la barrière aux épisodes réels.
- Trois prédictions chiffrées et signées, scellées avant : certificat intra-classe ≥ x ; débordement hors classe ≤ y (signe attendu : modeste) ; héritage < redémarrage de δ sur les familles tenues à l'écart.
- Reproductibilité : graines (R9), manifestes, code scellé ; un tiers rejoue l'arène simulée sur processeur.
- Verdict de porte par un sous-agent neuf (R13), contre-lecture de conv-audit, revue de sécurité extérieure avant tout passage à des agents.
- Comparaison aux courbes publiées des occupants, après vérification sur PDF seulement.

## 5. La demande reformulée

> Concevoir et préenregistrer une **arène coévolutive attaque–défense à trois paliers d'information** (schéma → familles d'entraînement → familles tenues à l'écart), d'abord au niveau des lois sur activations synthétiques, puis sur épisodes réels si le simulé passe sa porte.
> (a) Formaliser le jeu : joueurs, gains, information, concept de solution (barrière minimax sur la classe déclarée pour la défense ; recherche de nouveauté pour l'attaque).
> (b) Construire la **barrière certifiée** sur les classes déclarées à plages déclarées, avec son certificat.
> (c) Faire tourner l'arène G générations avec archive et diagnostics de cyclage ; score absolu sur un étalon fixé avant.
> (d) Mesurer l'universalité comme le **débordement hors classe** sur les familles tenues à l'écart des cinq instances et sur les bancs publics.
> (e) Préenregistrer trois prédictions chiffrées avec signe : certificat intra-classe, débordement hors classe, effet d'héritage (défense héritée contre défense repartie de zéro à budget égal).
> (f) Battre quatre bases : défense seule contre banque fixe, défense redémarrée, attaque sans sélection, barrière théorique sans évolution.
> (g) Garde : attaque au niveau des lois, aucun score de moniteur réel dans ses entrées (vérifié par code), sorties scellées, revue extérieure avant tout agent.
> (h) Puissance calculée sur le monde simulé avant toute dépense sur carte graphique.
> (i) Antériorité sur PDF contre les occupants de la défense coévolutive et contre l'entraînement adverse et la robustesse certifiée.

« Quasiment natif » : oui pour les mécanismes (générations, épisodes, sélection par pari, héritage récompensé, mémoire, témoins, étage de tests). Il manque : un rôle de proposeur côté attaque nourri du schéma de la défense, les trois paliers d'information, le certificat, les diagnostics de cyclage, et la garde de l'invariant.

## 6. Décision

**Options** : (a) oui, en trois paliers séparés, comme ci-dessus ; (b) non, banque d'attaque figée et défense évoluant seule ; (c) oui, avec un attaquant opérationnel (agents réels) : pipeline d'évasion interdit avant revue extérieure, et exactement ce que font les occupants.
**Recommandation** : (a), confiance 0,6. **Si GO** : note de conception v1 par un rédacteur neuf, antériorité sur PDF, contre-lecture, préenregistrement ; la conception versée au niveau méthode dans le texte III de la course 2 comme conception du programme à attaquer ; un tour du collisionneur sur la conception (devis ≈ 10 USD). Dépense du pilote simulé : ordre de 10 à 20 USD d'appels de modèles, SUPPOSÉ, devis à faire ; carte graphique : devis séparé, plus tard.
**Aucun défaut** : modification du programme, attend le GO.
