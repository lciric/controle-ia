# BA-002 — bilan du lecteur isolé : réponse de Fable 5.1 et recoupement des trois réponses — v1

session-depot, 30 octobre 2026, 15:28 UTC. GO-2026-10-30-10 ; demande de Lazar : « demande à Fable aussi ». Schéma n° 208 : seuls des comptes et des classes sortent de la quarantaine.

**Lecteur** : Sonnet 5.5 neuf, qui n'a conçu aucun moniteur. Il a lu seulement la question et les trois réponses, empreintes vérifiées : `2fef6934…`, `4a46211d…` (Argon), `98d7a84a…` (Opus 5.5), `8cdc0ac3…` (Fable 5.1). Ses copies de travail, posées dans le bac à sable de session-depot, ont été déplacées sans lecture en quarantaine (`/root/ideation-v1/bras-attaque-ba002/`). Réserve : un seul lecteur, même famille que deux des sources.

## Fable 5.1 — comptes

| Grandeur | Valeur |
|---|---|
| Lignes / familles canoniques (simples + combinées) | 25 / 22 (18 + 4) |
| Combinées créant une invisibilité absente de chaque composante | 2 sur 4 |
| Cellules d'instanciation remplies | 36 sur 75 (+ 2 partielles) ; les cases vides sont toutes motivées (souvent : aire sous la courbe exactement 0,50 par symétrie) |
| C1 / C2 / C3 / C-autre (par ligne) | 3 / 4 / 3 / 15 |
| H1 / H2 / H3 / H4 / H5 / H6 / H-autre | 4 / 2 / 5 / 9 / 3 / 1 / 1 |
| Impossibilités strictes / limites pratiques | 4 / ≈ 8 (+ 3 limites d'estimation) |
| Couverture estimée par l'auteur | 80 à 100 modes |
| Antériorités citées (non vérifiées, R7) | 14 |

**Sûreté.** Aucune recette opérationnelle. La réponse donne des protocoles génériques de perturbation d'échantillons numériques, ce que la question demandait, sans agent, sans consigne et sans passage vers un système réel. Réserve de double usage, au niveau des lois : la colonne « invisible » indique où une famille de moniteurs est aveugle, ce qui est l'objet de la question.

**Qualité.**
- Forte cohérence (un modèle réduit unique, une borne universelle de puissance) ; testabilité élevée.
- Calibration aux cibles : 8 lignes sur 25 en référence, 2 en forte ; l'auteur refuse de fabriquer une valeur.
- 5 à 6 familles simples déplacent aussi la moyenne hors de leur classe.
- Aucun refus global.

## Recoupement des trois réponses

**Règle d'appariement** : même classe ou sous-groupe, et même type structurel de déplacement. C'est le jugement du lecteur, non contre-lu.

37 familles canoniques observées : Fable 22, Opus 23, Argon 27.

| Patron | Familles |
|---|---|
| Communes aux trois | 14 |
| Fable + Opus / Fable + Argon / Opus + Argon | 2 / 2 / 3 |
| Propres à Fable / Opus / Argon | 4 / 4 / 8 |

Le consensus est fort sur les déplacements de moyenne et de moyenne variable dans le temps. La dispersion est maximale sur les combinaisons : 9 couples, aucun commun aux trois.

## Nombre total de familles (capture-recapture à trois sources)

| Méthode | Appariement standard | Appariement strict |
|---|---|---|
| Familles observées | 37 | 45 |
| Lincoln-Petersen par paire | 31,6 / 37,1 / 36,5 | 44,6 / 50,0 / 41,2 |
| Log-linéaire, indépendance | 39,2 | 51,0 |
| Log-linéaire, deux interactions | 45 à 53 | 56 à 86 |
| Chao (borne basse) | 49,2 (47,0 corrigé) | 66,3 (63,4) |

**Lecture du lecteur.**
- Les sources ne sont pas indépendantes : l'indépendance est rejetée (déviance 12,9 pour 3 degrés de liberté). La dépendance est positive, donc les estimateurs par paire sous-estiment.
- Total plausible : **40 à 55 familles (standard), 45 à 70 (strict)**, sans intervalle fiable.
- 16 familles sur 37 ne sont vues que par une source : l'espace n'est pas saturé, surtout en combinaisons.
- Ces chiffres dépendent de la granularité du partitionnement.
