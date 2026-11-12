# Erratum — note « Paramètres d'infrastructure du dépôt public de Bailey » v1 — v1

31 octobre 2026, ≈ 12:25 UTC. Session-depot. Note visée : `docs/notes/anteriorite-P-041-v1/bailey-depot-public-parametres-v1.md` (`cb24587d…`, R-897), scellée, non modifiée (R12).

**Erreur** : la section « Matériel et longueur de boucle » attribue « une carte graphique A100 80 Go » à la note de bas de page de la p. 26 du papier de Bailey et collègues (`bailey-2025-obfuscated-activations-2412.09565.pdf`, `9c23a613…`). Le papier ne nomme **aucune** carte : la note de bas de page donne seulement les durées (« about 10 hours on a single GPU », ~16 384 pas ; « about 10 minutes », ~256 pas).

**Source correcte** de la carte A100 80 Go : le dépôt public `LukeBailey181/obfuscated-activations`, commit `9c1f4b1a721fa3c43d00b8605ee7db4c84a55942` (README, l. 96 ; `evaluate_defenses.sh`, l. 7) — provenance par lecture de dépôt, non opposable seule (R7).

**Effet** : aucun sur le choix du matériel (A100 80 Go reste la cible) ni sur les devis ; la référence est corrigée dans `prereg/P-041-malleabilite-v3.md` (`49f94354…`). Erreur relevée par le rédacteur de la v3.
