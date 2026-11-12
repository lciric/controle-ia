# Corrections de code proposées au lanceur T0.6 (versions neuves, R12 : `lanceur_v3`, amorce v3, `lancer_t06_v3.sh`) — v1

Contre-lecture 2 du lanceur T0.6 v2 (`0d48103b`), fille 9, 5 novembre 2026. Chaque correction : un cas sain et un artefact (R5), et une mutation au banc.

- **C-V3-1 (à corriger ; peut perdre la course)** — `lanceur_v2.sous_ensemble_en_morceaux` remplit chaque morceau jusqu'à 90 000 000 octets de tableaux, puis lève `GardeArret` si le fichier écrit dépasse cette borne. L'enveloppe `.npz` pèse ≈ 17 ko pour 49 actions, et 340 octets par tableau.
  - Correction : remplir jusqu'à une borne de tableaux plus petite (par exemple 85 000 000 octets, ou borne − 1 000 × actions − 1 Mo), et garder la vérification du fichier écrit à 90 Mo (GitHub refuse au-delà de 100 Mo).
  - Si un morceau écrit dépasse quand même la borne : le réécrire en deux, jamais un arrêt de la course.
  - Artefact : actions de taille choisie pour que la somme tombe à moins de 17 ko de la borne ; le run doit finir.
- **C-V3-2 (à corriger)** — amorce : le second démarrage se teste *avant* les contrôles « démarrage après l'échéance » et « après l'heure de dépense épuisée ».
  - Après une dépense épuisée, ou une échéance passée, avec `amorce-depot` présent : `t06-consigner.sh` (poussée des commits en attente), puis destruction (l'argent est épuisé : pas de sommeil) ou sommeil (fin normale), selon la règle que la session fixe.
  - Essai avec `DEPENSE_EPUISEE_UTC_S` **dans le passé** au second démarrage (l'essai actuel la pose à + 10⁶ s).
- **C-V3-3 (à corriger)** — `lancer_t06_v2.sh creation` : `vastai search offers "id=<OFFRE>" --storage <disque_min_go> --raw`, pour que `dph_total` et `storage_total_cost` soient lus au disque demandé (150 Go). Comparer à E2 avec le prix de l'instance créée.
- **C-V3-4 (note ; selon le nœud de Lazar sur Mahalanobis)** — si l'option (d) est retenue : un module neuf `t06/mahalanobis_rapide_v1.py`, même formule par `((z @ P) * z).sum(1)`.
  - Avant chaque usage, l'égalité au paquet gelé est vérifiée sur 256 jetons tirés (écart relatif ≤ 10⁻¹² ; sinon arrêt du couple, état « échec »).
  - Le paquet gelé `sondes/familles.py` reste inchangé.
  - Mesure : 80 à 120 fois plus rapide, écart 6·10⁻¹⁵ (`outils/mesure_mahalanobis_v1.py`).
