# Orchestrateur du pôle, version 0.7.0 — monde sur banque de scores — LISEZMOI v22

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5), v22 écrite après le relevé `date -u` de 21:22:14
UTC ; v1 à v21 gardées (R12). Deuxième pièce du pari apparié borné (conception v2 § 7 point 2 ; v3 à v6) : les **données**
du pari. `pole/pari_apparie.py` n'est pas modifié (sa contre-lecture, celle de la conception v6, est en cours). Toujours
hors du cycle (engagement « apparié », mémoire à clé complète, contrôles : à faire).

| changement | fichiers |
|---|---|
| **`MondeBanqueScores`** : banque d'épisodes (`id`, `unite`, `etiquette` honnete / sabote, `partie` calibrage / developpement / epreuve **par unité**, `strates` déclarées, `scores` réels finis pour chaque cellule) ; refus d'une unité sur deux parties, d'un identifiant en double, d'un score absent ou non fini, d'une strate non déclarée ; **seuil conforme strict** au point de fonctionnement τ sur les honnêtes du calibrage (alerte si score > s_(j), j = ⌊τ·(n + 1)⌋ ; « calibrage insuffisant » si τ·(n + 1) < 1 ; masse d'ex æquo et taux sur le calibrage rapportés ; filtrable par strate et par unités) ; **parts** par unité (r sur les sabotés, f sur les honnêtes) ; **ordre secret** (graine du noyau, par fiche) ; **contrastes** (règle double ; plafond D-S27 si m_max) ; **écarts de faux positifs** pour la garde ; **jumeau calibré** (contrôle 12 : deux moitiés disjointes du calibrage, par unité) ; description publique sans score | `pole/monde_banque_scores.py` (nouveau) |
| essais : six refus de validation ; seuil conforme (j = 10 sur 199, taux 9/199 ; calibrage insuffisant à n = 50 et τ = 1 %) ; ex æquo rapportés ; faux positifs neufs ≤ τ en moyenne (30 calibrages de 399, 4 000 honnêtes neufs) ; parts, contrastes, plafond et garde à la main ; strate ; ordre secret ; **bout en bout** : effet vrai de 32 points promu par le pari apparié avec garde (δ = 0,10, 100 unités) — à δ = 0,05 et 60 unités, la garde ne certifie pas, comme la v2 le chiffre (≈ 150 unités honnêtes) ; B = A jamais promu ; jumeau calibré à moitiés disjointes | `essais/test_v7_monde_banque_scores.py` (nouveau, 9) |

**250 essais passent** (226 s). Le reste : LISEZMOI v21, v20, v19.
