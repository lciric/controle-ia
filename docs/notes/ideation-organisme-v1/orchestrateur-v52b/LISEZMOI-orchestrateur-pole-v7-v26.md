# Orchestrateur du pôle, version 0.7.0 — fraîcheur des unités par identifiants (conception v9 du pari) — LISEZMOI v26

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), v26 écrite après le relevé `date -u` de 23:32:28
UTC ; v1 à v25 gardées (R12). Suit la **conception v9 du pari apparié borné** (`../pari-de-signe/conception-pari-de-signe-v9.md`)
après la contre-lecture de la v8 (`../pari-de-signe/contre-lecture-v8/`, rapport `b2edabeb…` : K8-1 fraîcheur vérifiée pour une
répétition exacte seulement, K8-3 traces). v9 et v26 pas encore contre-lues.

| changement | fichiers |
|---|---|
| `Course.ajouter_trajectoire(fiche, trajectoire_log, unites=None, sans_identite=False)` : **identifiants d'unités obligatoires** ; toute **intersection** avec les unités déjà lues par la fiche est refusée (K8-1 : fraîcheur, pas seulement répétition exacte) ; une partie sans identité n'est acceptée qu'avec `sans_identite=True`, tracée dans `parties_sans_identite` ; `abandonner(..., unites=…, sans_identite=…)` ; un second abandon d'une fiche gelée est tracé (`abandons[("redite", fiche)]`, K8-3) ; en-tête « versions 20 à 26 » | `pole/pari_apparie.py` |
| `evaluer` rend `identifiants_unites` = [(empreinte de la banque, partie, unité)…], à passer à la course ; l'empreinte reste pour le manifeste | `pole/engagement_apparie.py` |
| essais : intersection partielle refusée ; sans identité refusée, puis déclarée et tracée ; redite d'abandon tracée ; identifiants de l'engagement refusés à la seconde lecture ; les essais synthétiques de l'héritage passent des identifiants frais (génération, fiche, indice) | `essais/test_v7_pari_apparie.py`, `essais/test_v7_engagement_apparie.py` |

**262 essais passent** (224 s). Le reste : LISEZMOI v25 à v19.
