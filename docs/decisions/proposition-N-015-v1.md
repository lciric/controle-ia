# Proposition — nœud N-015 — H6 : la composante « bruit d'activations » trouvée en partie occupée (Poser) — v1

Rédigée le 2026-10-07 vers 06:20 UTC par la session de mise en œuvre, après la lecture du lot 6 du niveau 2 de l'état de l'art par un lecteur neuf (`docs/sources/lecture-pdf-niveau2/rapport-lot6-pistes-v1.md`, c593418b… ; 232 citations contrôlées par script, 0 échec). C'est un nœud : une zone revendiquée est trouvée en partie occupée (consignes permanentes, « Nœuds de décision »). Il ne bloque aucune tâche de la phase 0 : H6 relève du papier A (phase 1).

## Décision

Faut-il retirer le bruit d'activations des interventions revendiquées par H6, comme N-013 l'a fait pour le bruit sur les poids ?

Énoncé retenu de H6 (`docs/decisions/decision-N-013-v1.md`, 157d388e…, section 6) : « pour l'une au moins des quatre interventions non spécifiques (paraphrase, ré-échantillonnage, remise à zéro du contexte, bruit d'activations), il existe une intensité où, en moyenne à intensité fixe, le succès du sabotage d'agent chute significativement plus vite que l'utilité honnête ».

## Enjeu

- **Ce que montre Poser** (Clymer, Juang, Field 2024, arXiv 2405.05466v2 ; rapport du lot 6, section 5 et prononcé 4) : à intensité fixe, un bruit ajouté aux activations rend un modèle qui simule l'alignement plus enclin à l'action non alignée, tandis que le modèle aligné reste « relativement inchangé » ; en détection, 98 % des paires sont classées.
- C'est la même structure de résultat que celle qui a fait retirer le bruit sur les poids (2412.01784, N-013).
- **Ce que Poser ne fait pas** : ni agent, ni sabotage (choix d'un jeton A ou B dans des jeux de rôle, cadre jouet, modèles de 13 milliards de paramètres) ; ni utilité honnête mesurée ; ni comparaison de pentes ; ni test statistique. Le sens de l'effet (le comportement nuisible augmente sous bruit) peut même jouer contre H6 selon la définition du « succès du sabotage ».
- Réserves de symétrie (R4) du lecteur sur Poser : cinq ou six stratégies selon les pages, 47 % ou 37 % pour la même, bruit non centré, paires non indépendantes.

## Options

| option | contenu | avantage | inconvénient |
|---|---|---|---|
| (a) garder, revendication réduite | le bruit d'activations reste l'une des quatre interventions ; la revendication ne porte que sur la mesure agentique (sabotage d'agent contre utilité honnête, pentes comparées, test) ; Poser est cité comme antériorité | garde l'intervention la plus proche de l'accès interne du programme | l'originalité de cette composante devient mince : le reviewer y verra Poser |
| **(b) retirer, comme le bruit sur les poids** | le bruit d'activations est encore mesuré dans E1.6, mais n'est plus revendiqué ; H6 repose sur la paraphrase, le ré-échantillonnage et la remise à zéro du contexte | cohérent avec N-013 ; aucune revendication exposée | H6 perd la composante la plus « boîte blanche » |
| (c) aucun changement | l'énoncé reste tel quel | rien à réécrire | une zone revendiquée connue pour être en partie occupée resterait revendiquée (R8) |

## Recommandation

**(b)**, confiance ≈ 65 %. Même raisonnement que pour le bruit sur les poids (N-013) ; la mesure reste faite, seule la revendication tombe. Le lecteur recommande aussi (b).

Nœud : pas de défaut. Rien de la phase 0 n'en dépend.
