# Devis — collisionneur séparé sur N12 et N13 (couches 3 et 4 de l'organisme ; récompense collective) — v2

session-depot (instance 3), 31 octobre 2026, ≈ 18:32 UTC. Remplace la v1 (`devis-collisionneur-n12-n13-v1.md`,
`f35c25d2…`, gardée, R12) sur deux points : les faits courts sont désormais **assemblés et scellés** (le chiffrage se fait sur
le fichier réel, par la commande `devis` du collisionneur, sans appel) ; et le plafond de run applique la règle de Lazar du
31 octobre (R-924 : plafond ≥ 1,5 × l'estimation, pour ne plus subir la coupure de R-923). Aucune dépense n'est engagée avant un
mot direct de Lazar sur ce devis.

## Ce qui serait lancé

Collisionneur v7 (`c9725f02…`), quatre espèces (Fable 5.1, Opus 4.6, Argon, Kimi K3.1 Pro), étage III (conception, critique
croisée, réponse : 12 cellules), question **v2** de conv-audit (`question-collisionneur-n12-n13-couches-recompense-v2.md`,
`9faee0aa…`, 1 071 mots, sans section de recommandation), faits courts v1 assemblés par session-depot
(`donnees/collisionneur-n12-n13-v1/faits-n12-n13-v1.md`, `ccec9e94…`, 19 004 mots, 6 pièces : N-045 v2, N-058, pré-collision
d'Opus, lectures vérifiées d'Avalon-M1 (`a8251ea8…`) et de Damani (`4e29301a…`), provenance des PDF ; recommandation, confiance
d'auteur et défaut retirés (4 marques, règle 2) ; balayage `balayage-faits-n12-n13-v1.txt`, `cd72c53c…` : aucune clé, aucun
contenu d'attaque, aucune donnée). Script `lancer-tour-n12-n13-v1.sh` sur le gabarit éprouvé (R-919 : relais Kimi sous `env -i`,
contrôle préalable, appel de contrôle, `trap`, sans `set -e`), port 8795, Python neuf de l'instance 3. Règle R-831 sur les refus.
Les deux conditions de la v1 sont remplies : lecture vérifiée de Damani rendue (n° 301), section de recommandation retirée de la
question (v2), servie à part pour un éventuel tour 2 (`annexe-tour-2-n12-n13-v1.md`, `9dc13ece…`, non lue par session-depot).

## Chiffrage (commande `devis` du collisionneur sur les fichiers réels, 31 octobre 18:30 UTC)

| Run | Pire cas sans relance (barème du collisionneur) | Réalisé | Rapport |
|---|---:|---:|---:|
| Nœuds, tour 1 v12 (45 811 mots, 12 cellules) | 43,51 | 23,87 | 0,55 |
| Protocelles, tour 1 (9 cellules, Fable absent ; pire cas hors Fable 32,01) | 45,99 | 18,52 | 0,58 |
| D-ML-1 (9 cellules, Fable absent ; pire cas hors Fable 21,92) | 32,18 | 4,30 | 0,20 |
| **N12-N13 (19 004 mots, 12 cellules)** | **36,46** | — | — |

Estimation : 0,20 à 0,58 du pire cas, soit **7 à 21 USD** ; valeur centrale (rapport 0,5) **≈ 18 USD**. La v1 disait 7 à 10 USD
par analogie avec des tours à faits plus courts (arène : 8,2 et 8,4) ; le chiffrage sur le fichier réel est plus haut parce que
les lectures vérifiées font 13 000 mots à elles deux.

Contrainte de la garde de plafond (R-923) : le collisionneur refuse une cellule si « dépense + pire cas de la cellule » dépasse
le plafond ; la dernière cellule d'Opus pèse 5,93 au pire cas. Un plafond de 12 (v1) ou de 15 arrêterait vraisemblablement le
run vers la septième cellule, comme le tour 1 v12 à 22.

## Options

| Option | Plafond de run | Avantage | Inconvénient |
|---|---:|---|---|
| (a) | **30 USD** (≥ 1,5 × 18 ; ≥ 21 + 5,93) | aucune coupure attendue, même au haut de la fourchette ; règle R-924 respectée | engage 30 au lieu de 12 ; dépense réelle attendue ≈ 18 |
| (b) | 15 USD (1,5 × 10, estimation de la v1) | moindre engagement | coupure probable (R-923), script suite et avenant ensuite |
| (c) | 0 USD : Argon seul sur la même question sous GO-2026-10-31-08 (3 USD par appel, cumul 4,20 / 25) | aucune dépense nouvelle | une seule voix, pas de critique croisée |

## Recommandation

(a), plafond de run **30 USD**, lancement dès le mot de Lazar. Confiance 0,6 sur l'attendu (rapport réalisé / pire cas entre 0,2
et 0,58 sur trois runs) ; 0,9 que (b) coupe avant la fin. Nœud de dépense : pas de défaut à 48 heures.
