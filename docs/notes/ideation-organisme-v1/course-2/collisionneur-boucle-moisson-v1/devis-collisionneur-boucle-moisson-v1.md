# Devis — collisionneur sur la boucle itérative moisson ↔ fiches ↔ bisociateur (question v1 de conv-audit), tour 1 — v1

session-depot (instance 3, seconde session), 1er novembre 2026, ≈ 09:41 UTC. Demande de Lazar rapportée par conv-audit (n° 312, 09:27 UTC :
« envoie-la aussi au collisionneur en urgence ») puis **mot direct de Lazar dans cette session (≈ 09:42 UTC)**, verbatim : « Deux
dépenses attendent ton mot direct chez session-depot : le devis du collisionneur sur la boucle, et Argon seul sur la convergence
(≈ 1 USD : go depenses go TOUTES les depenses ». Ce devis fixe le plafond de run que ce mot engage (règle R-924 : plafond ≥ 1,5 ×
l'estimation) ; il est écrit avant tout lancement.

## Ce qui est lancé

Collisionneur v7 (`c9725f02…`), quatre espèces (Fable 5.1, Opus 4.6, Argon, Kimi K3.1 Pro), étage III (12 cellules), **tour 1** de la
question v1 `question-collisionneur-boucle-moisson-fiches-v1.md` (`72b4f149…`, 797 mots, sept questions Q1 à Q7, recommandations des
auteurs retirées et réservées au tour 2) ; faits v1 assemblés par session-depot `donnees/collisionneur-boucle-moisson-v1/faits-boucle-moisson-v1.md`
(`53f78bb2…`, 14 237 mots : dossier factuel de l'organisme § 1, 2, 3, 7, 9, 10 (`0751fc8c…`) ; rétrodiction de Swanson (`057ef8a5…`) ;
état des lieux de Gu et Krenn (`1c1618a2…`) avec la décision de Lazar du 1er novembre ; lectures des essais de la mémoire (`0cd614b1…`,
`27e4cdac…`) ; l'antériorité de la boucle, non rendue au lancement, n'est pas servie) ; balayage `balayage-faits-boucle-moisson-v1.txt`
(aucune clé ; mentions d'attaque au niveau des noms de concepts seulement ; aucune fiche réelle). Script `lancer-tour-boucle-moisson-v1.sh`
(`7ed8bc04…`, gabarit éprouvé R-919, port 8796, clé Anthropic `RR_ANTHROPIC_API_KEY_LUC` par nom, R-947), run neuf
`run-boucle-moisson-e3-v1`. Règle R-831 sur les refus. Le **tour 2** (annexe des recommandations de conv-audit) fera l'objet d'un devis à
part après la synthèse du tour 1.

## Chiffrage (commande `devis` du collisionneur sur les fichiers réels, 09:41 UTC)

| Run | Pire cas sans relance | Réalisé | Rapport |
|---|---:|---:|---:|
| Nœuds, tour 1 v12 (45 811 mots) | 43,51 | 23,87 | 0,55 |
| N12-N13 (19 004 mots) | 36,46 | 13,52 | 0,37 |
| Nœuds, tour 2 (14 318 mots) | 35,22 | 12,81 | 0,36 |
| **Boucle moisson, tour 1 (14 237 mots)** | **35,37** | — | — |

Attendu : 0,36 à 0,55 du pire cas, soit **13 à 19 USD** ; centre ≈ 16. Dernière cellule d'Opus au pire cas 5,78 (garde R-923).

## Plafond

**30 USD** (≥ 1,5 × 19,5 ; ≥ 19 + 5,78). Options écartées : 22 (coupure possible au haut de la fourchette) ; 15 (coupure probable, R-923).
Nœud de dépense engagé par le mot de Lazar ci-dessus ; ligne GO-2026-11-01-03 de `registres/go.md`.
