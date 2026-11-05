# Proposition — P-006 — conception de l'environnement (a) v0 (T0.5) — v1

Rédigée le 2026-10-06 par la session de mise en œuvre. Hiérarchie de décision : « proposer avec recommandation » (portage d'un environnement, périmètre interne d'une phase) ; défaut appliqué 48 heures après l'envoi à Lazar. Détail : `brouillons/T0.5-conception-environnement-a-v0-brouillon1.md`. Invites de l'article transcrites et vérifiées sur le PDF : `docs/sources/invites-2606.08892-v1/` (18 invites, 18 conformes).

## Décision

Comment reconstruire l'environnement (a) de Terekhov et al. (arXiv 2606.08892) pour le programme : unité d'action, vérité terrain, préparation des données.

## Enjeu

- L'article ne publie ni code ni données (P-004 : reconstruction, défaut appliqué). Il note un ensemble de 10 propositions par tâche, en un seul tour, sans indice d'agent ; sa vérité est un modèle fort fermé qui lit le papier.
- Le programme exige des contributions (agent i, pas t) qui resservent telles quelles quand N = k, une vérité par cibles semées préenregistrées, et le modèle Llama-3.1-8B pour l'agent.
- Ces choix fixent tout le papier A (phases 0 à 2) : ils doivent être pris avant le préenregistrement du pilote 8B.

## Options

**(a) Tâche en pas, cibles semées, extraction par le modèle de la session.**
- Une tâche se joue en T pas ; à chaque pas, l'agent i = t mod N ajoute ou révise une proposition (action structurée) ; T = 10 pour N = 1.
- Vérité de la phase 0 : cibles semées par tâche (contrôles nécessaires, budget de calcul, direction féconde cachée), préenregistrées ; proxy fort qui lit le papier reporté en phase 1, sous son propre devis (comme P-002).
- Questions de recherche et cibles extraites par le modèle de la session (sous-agents neufs, contre-vérifiés sur échantillon), sorties figées et scellées comme données.
- Rubrique à dix critères agrégée par une formule fixe (points ramenés sur 100).
- Avantages : contributions (i, t) natives ; vérité objective et bon marché ; aucun coût de carte en plus du pilote (5 heures au devis).
- Inconvénients : la notation par action s'écarte de la rubrique d'ensemble de l'article ; la qualité des cibles dépend de l'extraction.

**(b) Plus près de l'article : ensemble de 10 propositions en un tour, révisé sur T pas ; proxy 70B dès la phase 0.**
- Avantages : comparabilité avec l'article ; vérité par un modèle fort.
- Inconvénients : contributions moins fines (une révision d'ensemble par pas) ; coût d'un 70B dès la phase 0 (deux cartes ou quantification), hors devis.

**(c) Minimal : rubrique simplifiée d'emblée (le plan B) et cibles semées seules.**
- Avantages : le plus simple et le moins cher ; risque d'effet plancher du 8B réduit.
- Inconvénients : s'éloigne de l'article ; perd la comparaison avec sa rubrique.

## Recommandation

**(a)**, confiance d'environ 60 %. Elle tient les exigences du programme (contributions (i, t), cibles semées) au coût du devis. Le pilote 8B, préenregistré, dira si le plan B s'impose.

## Défaut

(a), 48 heures après l'envoi.
