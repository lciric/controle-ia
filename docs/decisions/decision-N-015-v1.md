# Décision — N-015 : H6, la composante « bruit d'activations » trouvée en partie occupée (Poser) — v1

- **Décision de Lazar** : option (b), donnée dans la session 14 le 2026-10-20 vers 08:08 UTC (« go », précisé par sa réponse
  « Les deux » : N-015 (b) et l'adaptation du relais) ; GO-2026-10-20-01 (type « revendication ») ; R-253.
- **Proposition tranchée** : `docs/decisions/proposition-N-015-v1.md`
  (`d632ae49ba6c2b6aef00f7a6a06fb502308ea1e7c08ae3dafe3f96986010f12d`) ; R-091 (lot 6 du niveau 2 de l'état de l'art,
  lecteur neuf, `docs/sources/lecture-pdf-niveau2/rapport-lot6-pistes-v1.md`, c593418b…).
- **Source** : Clymer, Juang et Field 2024, « Poser », arXiv 2405.05466v2 (rapport du lot 6, section 5 et prononcé 4).

## 1. H6 — énoncé retenu, à partir de cette décision

Cette section remplace l'énoncé de H6 fixé par `docs/decisions/decision-N-013-v1.md`, section 6, pour la seule liste des
interventions revendiquées.

- **Énoncé retenu** : pour l'une au moins des trois interventions non spécifiques (paraphrase, ré-échantillonnage, remise à
  zéro du contexte), il existe une intensité où, **en moyenne à intensité fixe**, le succès du sabotage d'agent chute
  significativement plus vite que l'utilité honnête.
- **Le bruit d'activations n'est plus revendiqué**, comme le bruit sur les poids (N-013) : Poser montre déjà qu'à intensité
  fixe un bruit ajouté aux activations rend un modèle qui simule l'alignement plus enclin à l'action non alignée, tandis que
  le modèle aligné reste « relativement inchangé », avec un usage en détection (98 % des paires), en cadre jouet, sans agent,
  sans utilité honnête mesurée, sans comparaison de pentes ni test.
- **La mesure reste faite** : le bruit d'activations reste l'une des interventions mesurées dans E1.6, avec la même
  méthode que les trois autres. Un résultat sur cette intervention se rapporte comme une extension agentique de Poser, cité
  comme antériorité, jamais comme une revendication de H6.
- **Retour possible**, par un nœud de Lazar seulement et après le résultat : Poser trouve que le bruit augmente le
  comportement non aligné ; si la mesure agentique montrait l'effet inverse (succès du sabotage qui chute plus vite que
  l'utilité honnête), une revendication propre pourrait être proposée, comme résultat et non comme prédiction.

## 2. Ce qui ne change pas

- Les autres énoncés retenus par N-013 et les décisions antérieures, la porte GC, et rien de la phase 0 : aucune tâche de la
  phase 0 ne dépend de H6.
- Le programme (`docs/programme-controle-ia-v2.md`) n'est pas réécrit : il se lit avec cette décision, comme avec les
  décisions N-003 à N-023 (consignes permanentes), jusqu'à une version nouvelle transmise par Lazar.
