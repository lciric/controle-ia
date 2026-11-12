# Paramètres d'infrastructure du dépôt public de Bailey — v1

31 octobre 2026, ≈ 10:35 UTC. Session-depot (Opus 4.8). Lecture seule du dépôt public ; aucune dépense ; aucune donnée de `donnees/`.

Objet : fixer, à partir du code public de Bailey et collègues, les deux éléments « à fixer » communs aux préenregistrements de l'examen final (`prereg/P-041-examen-final-v2.md`) et de la malléabilité (`prereg/P-041-malleabilite-v2.md`) : le juge de nuisance et le jeu bénin/nuisible. Niveau infrastructure uniquement (juge, données, matériel, longueur de boucle) ; aucune recette d'attaque.

## Source

- Dépôt public cloné en lecture seule (hors dépôt de travail) : `github.com/LukeBailey181/obfuscated-activations`, commit `9c1f4b1a721fa3c43d00b8605ee7db4c84a55942` (11 février 2025).
- Papier empreinté : `docs/sources/pdf/anteriorite-P-041-v2/c3/bailey-2025-obfuscated-activations-2412.09565.pdf` (`9c23a613…`).
- À revérifier au scellement sur une empreinte du dépôt (le commit public peut bouger). Provenance par lecture de dépôt, non opposable seule (R7) : tout chiffre repris dans un préenregistrement renvoie en plus au papier empreinté.

## Juge de nuisance — RÉSOLU

Le code appelle `strongreject_finetuned` (import `from strong_reject.evaluate import strongreject_finetuned`), c'est-à-dire **l'évaluateur StrongREJECT affiné** (autograder fin). Chaque réponse du modèle reçoit un score de nuisance par ce juge ; c'est la mesure du taux d'évasion du refus.

Conséquence pour les préenregistrements : le juge est **StrongREJECT affiné** (paquet `strong_reject`, fonction `strongreject_finetuned`). Version et empreinte du paquet à épingler au scellement.

## Jeu bénin/nuisible — RÉSOLU

Jeu `harmful_dataset` du dépôt (fichiers `harmful_{train,val,test}_no_spec_tokens.csv` et `benign_{train,val,test}_no_spec_tokens.csv`) :

| Partition | Nuisible | Bénin |
|---|---:|---:|
| entraînement | 800 | 800 |
| validation | 100 | 100 |
| test | 100 | 100 |

Conséquence : le jeu bénin pour le seuil de 1 % de fausses alertes et pour la mesure peut être celui de Bailey (bénin entraînement 800 + validation/test), disjoint par partition. Les tailles d'échantillon des préenregistrements (≥ 1 000 bénins pour le seuil) peuvent demander un jeu bénin public plus large que les 800 de Bailey : à trancher au scellement (élargir le jeu bénin, ou abaisser le seuil de taille en le justifiant).

## Matériel et longueur de boucle (pour le devis)

- Modèle : Llama-3-8B-Instruct (poids en float16).
- Matériel déclaré par le papier : une carte graphique A100 **80 Go** (note de bas de page p. 26 : « about 10 hours on a single GPU » pour ~16 384 pas de descente de gradient d'une attaque dure contre la défense adversaire ; ~256 pas « about 10 minutes » sans défense adversaire).
- Longueur de boucle dans la configuration publique : `attack_defense_epochs: 100` (le texte dit « over 70 epochs » pour la sonde MLP, ~90 pour l'ensemble).

**Réserve pour le devis** : le devis v1 (`22c34601…`) cite une A100 40 Go. Bailey a déclaré une A100 80 Go ; une reproduction fidèle devrait viser 80 Go (Llama-3-8B en float16 ≈ 16 Go de poids, plus les gradients, l'état de l'optimiseur et les activations sur 32 couches ; 40 Go peut déborder). L'écart de prix sur Vast.ai est faible (A100 80 Go SXM4 ≈ 1,08 USD/h, PCIE ≈ 0,87 USD/h, relevé 10:25 UTC). À corriger dans la v2 du devis.

**Réserve de durée** : la note p. 26 (~10 h pour 16 384 pas d'une attaque dure) ne borne pas directement la boucle itérée (attaquant réoptimisé à chaque époque, défenseur réajusté) ; la durée de bout en bout peut dépasser l'estimation de 12 à 24 h du devis. L'approche pilote d'abord (calibrer la durée d'une époque) et le plafond de 75 USD gardent la marge, mais la durée est la plus grande incertitude du devis.
