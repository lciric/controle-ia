# Orchestrateur du pôle, version 0.7.0 — engagement « apparié » — LISEZMOI v23

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5), v23 écrite après le relevé `date -u` de 21:28:12
UTC ; v1 à v22 gardées (R12). Troisième pièce du pari apparié borné : **la fiche, de bout en bout hors du cycle** —
construite et scellée avant toute issue d'épreuve, jugée sur la banque de scores. `pole/pari_apparie.py` n'est pas modifié
(contre-lecture de la conception v6 en cours). Reste : le lien avec le cycle (proposeur, gabarit, `Course` à la place de
la règle e-BH par génération pour ces fiches, mémoire à clé complète) et le script des contrôles.

| changement | fichiers |
|---|---|
| **`construire(monde, contrastes, tau, alpha_c, m_c, strate, partie, m_max, garde, population)`** : contrastes nommés (intersection-union ; règle double vérifiée ; cellules connues), garde (A, B, δ), budget d'entrée (α_c, m_c ; D-S25 bis), m_max (plafond, D-S27) ; **seuils pris au seul calibrage** (refus si « calibrage insuffisant ») ; **clé de l'héritage** (D-S18 de la conception v6 : contrastes et coefficients, pondération et m_max, τ, strate, comparateurs, seuils scellés, population = empreinte de la banque ou vivier déclaré, garde) et son empreinte ; empreinte de l'engagement (qui fixe l'ordre secret) ; la partie de calibrage ne se lit jamais comme épreuve | `pole/engagement_apparie.py` (nouveau) |
| **`evaluer(monde, engagement)`** : refus d'un engagement altéré ou scellé sur une autre banque ; parts de la partie lue, contrastes dans l'ordre secret, garde, e-valeur du minimum arrêtée au seuil m_c/α_c, bornes basses rapportées, empreinte de la clé | `pole/engagement_apparie.py` |
| essais : sept refus ; seuils inchangés quand seule l'épreuve change ; clé : égale pour deux engagements identiques, différente pour τ, m_max, strate, population, garde, **inchangée** pour le budget d'entrée (même affirmation, autre engagement) ; bout en bout (effet vrai promu, borne basse > 0 ; « rappel ≥ 0,9 » faux non promu) ; scellement (seuil altéré refusé ; autre banque refusée) | `essais/test_v7_engagement_apparie.py` (nouveau, 5) |

**255 essais passent** (238 s). Le reste : LISEZMOI v22, v21, v20, v19.
