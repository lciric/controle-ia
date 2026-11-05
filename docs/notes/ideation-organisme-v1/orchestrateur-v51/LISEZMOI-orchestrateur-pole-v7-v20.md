# Orchestrateur du pôle, version 0.7.0 — cœur du pari apparié borné — LISEZMOI v20

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5), v20 écrite après le relevé `date -u` de 20:57:19
UTC ; v1 à v19 gardées (R12). Premier code du second type d'engagement du pôle, selon la conception v5 du pari apparié
borné (`../pari-de-signe/conception-pari-de-signe-v5.md`, `95af46e4…` ; sa contre-lecture par Fable est en cours : ce
module suivra ses constats). **Seul le cœur statistique** est codé ; le lien avec le cycle (monde sur banque de scores,
engagement, clé complète de l'héritage, règle en ligne entre générations) reste à faire.

| changement | fichiers |
|---|---|
| **`pole/pari_apparie.py`** : règle double des coefficients ; contraste borné ; richesse en forme « parts » seule (moyenne sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9} de Π (1 + λ·v)) ; garde appariée (1 + λ·(δ − g)) ; e-valeur de la fiche = minimum des processus (intersection-union sur les comparateurs, garde comprise), arrêtée au seuil log(m/α) ; variante sans remise ; borne basse de confiance à tout instant par inversion des paris (monotone en θ) ; Python pur | `pole/pari_apparie.py` (nouveau) |
| le duel des proposeurs lit L2 à L4 par ce cœur (un seul code) | `demonstrations/duel_proposeurs_v7.py` |
| essais : règle double (interaction admise, sommes refusées) ; validité sous S1 et S2 (≤ 0,08 sur 300 répétitions) ; puissance à 20 points et 60 unités (≥ 0,90) ; intersection-union avec un comparateur au nul (≤ 0,08) ; garde qui bloque un tricheur (0 sur 200) ; arrêt au septième instant à m = 1, plus tard à m = 10 ; sans remise sur banque figée 90/10 (≤ 0,08) ; couverture de la borne basse (≥ 92 sur 100) | `essais/test_v7_pari_apparie.py` (nouveau, 9) |

**235 essais passent.** Le reste : LISEZMOI v19.
