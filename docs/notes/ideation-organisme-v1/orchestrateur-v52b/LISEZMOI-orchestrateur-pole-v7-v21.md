# Orchestrateur du pôle, version 0.7.0 — règle de l'héritage et plafond (conception v6 du pari) — LISEZMOI v21

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5), v21 écrite après le relevé `date -u` de 21:11:46
UTC ; v1 à v20 gardées (R12). Suit la **conception v6 du pari apparié borné** (`../pari-de-signe/conception-pari-de-signe-v6.md`),
écrite après la contre-lecture de la v5 par Fable 5.1 (`../pari-de-signe/contre-lecture-v5/`, rapport `4e8e3270…`).
Toujours hors du cycle des générations (lien à faire).

| changement | fichiers |
|---|---|
| **règle de l'héritage D-S25 bis** : `ebh_pondere` (tri par b_i·E_i, k* le plus grand k dont la k-ième valeur atteint 1/k) ; `Course` (budget d'entrée α_c/m_c gardé à vie, somme des niveaux de familles ≤ α sinon refus, une fiche n'entre qu'une fois, valeur héritée multipliée et arrêtée au seuil d'entrée m_c/α_c, gel à l'abandon et à la promotion, une lecture e-BH pondérée sur toutes les fiches entrées, promotion une seule fois, union des promotions, relecture e-Bonferroni) | `pole/pari_apparie.py` |
| **plafond D-S27** : `ponderation_plafonnee(m_t, m_max)` = min(m_t, m_max)/m_max ; `contraste_plafonne` (v calculé sur tous les épisodes) | `pole/pari_apparie.py` |
| `evaluer` : seuil d'arrêt dit pour les fiches nouvelles (m_g/α_g) ; relancées par `Course` (K5-3) | `pole/pari_apparie.py` |
| essais : plafond (bornes, coïncidence) ; e-BH pondérée égale à l'ordinaire pour une famille (300 tirages contre une référence écrite à part) ; budgets refusés ; budget gardé quand les sœurs sont abandonnées (30 < 100 : pas de promotion, là où la lecture « seule » l'aurait faite) ; promotion une seule fois et gel ; **nul complet, monde A′** (contre-lecture v5, section 7 H ; 400 répétitions, graine 29) : lecture valide **0,0275** ≤ α, lecture « seule » de la cohorte **0,085** (mécanisme de K5-1) | `essais/test_v7_pari_apparie.py` (6 essais de plus) |

**241 essais passent** (233 s). Le reste : LISEZMOI v20, v19.
