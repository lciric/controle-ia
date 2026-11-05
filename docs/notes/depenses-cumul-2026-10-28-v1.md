# Dépenses du programme : réconciliation au 28 octobre 2026 — v1

Rédigé par session-depot le 2026-10-28 ≈ 10:55 UTC, par lecture de `registres/depenses.md` (211 lignes) et des journaux des runs en cours, sur la demande de conv-audit (programme d'entretien TAIF v2, réserve 2 : « à faire totaliser par session-depot avant l'appel ; ne pas citer de chiffre exact tant que ce n'est pas fait »). Méthode : seules les lignes **réalisées** sont comptées (jamais les engagements, plafonds, « au plus », cumuls « engagés ») ; quand le registre donne une fourchette ou un « ≈ », la **borne haute** est retenue ; le registre lui-même marque plusieurs relevés « à confirmer sur la facturation ». Précision globale : **± 15 %**, hors le trou de la relève (section 3).

## 1. Totaux par poste (USD, bornes hautes)

| Poste | GO | Réalisé | Détail |
|---|---|---|---|
| **GPU, phase 0 proprement dite** (T0.4 v1–v3, disques gardés 6→10 oct., T0.5 revalidation v1/v2, pilote, notations P2, P3) | GO-2026-10-04-08 (+ -12-01, -12-02) | **≈ 70** | registre : « au plus ≈ 63,2 » au 18 oct. (disques compris) + P3 6,42 (relevé du 23 oct., disque compris) |
| GPU, comparaison d'échelle | GO-2026-10-27-04 (plafond 24) | ≈ 1,7 | 32 min de 4 × A40 + descente 160 Go ; relevé à confirmer |
| GPU, couche 1 bis (a) + (b) | GO-2026-10-27-07 (plafond 25) | ≈ 11,9 | 0,15 + 6,2–7,2 + 3,3–4,3 |
| GPU, test H-M1 v2/v3 | GO-2026-10-25-03 | ≈ 0,25 | deux instances, quelques minutes |
| GPU, gradient étape 1 (extraction, sonde d'hôte, répétition) | GO-2026-10-24-05, -24-07 | ≈ 11,6 | 0,29 + 0,01 + 11,32 |
| **Sous-total GPU sous GO** | | **≈ 95** | |
| **Relève Gemini, 23 oct., sans GO** (13 instances Vast.ai, R-327) | aucun | **≥ 6,0 — réel inconnu** | 6,01 visibles au relevé du 23 à 0 h ; facturation postérieure « pas encore lisible » ; plan annoncé par la relève : 468 USD sur 72 h de H200 ; **jamais relu depuis** (section 3) |
| **API, pilotes de l'organisme écrit par Gemini** (v4 question ; second pilote M, S ; pilote 3 v5.3, v6 ; pilote 4 M, S) | GO-2026-10-24-07, -25-01, -25-02 | **≈ 156,3** | 2,05 + 14,92 + 15,30 + 15,12 + 15,11 + 31,57 + 62,20 |
| **API, collisionneur** (tous tours 24–27 oct. : v2.5 III.1 ×14, marathon du 26, audit défensif, rapport consolidé, pôle, recombinaison, mémoire, boucle d'or, proposeur v1+v2, questions fortes, pari de signe, mesures fortes, Opus/Argon seuls) | GO-2026-10-24-06/-07, -26-02/-04/-06/-07, -27-01/-02/-06/-09/-11/-12 | **≈ 179,9** | 24–25 oct. ≈ 18,5 ; 26 oct. ≈ 111,5 ; 27 oct. ≈ 49,9 |
| API, pôle scientifique automatique, lancements (a) et (a) bis | GO-2026-10-27-05, -27-10 | ≈ 12,1 | 6,24 + 5,89 |
| API, collisionneur « évasion et moniteurs », tour 1 en cours | GO-2026-10-28-03 | ≈ 4,4 (en cours) | 7 cellules sur 9 à 10:50 UTC |
| API, duel des proposeurs | GO-2026-10-28-01 | 0 | course nulle (R-599) |
| **Sous-total API** | | **≈ 352,7** | |
| **TOTAL CONNU** | | **≈ 450 USD** | hors facturation réelle de la relève (≥ 6) |

## 2. Lecture pour un financeur
- « Phase zero has cost under a hundred dollars of compute » n'est **vrai que pour le GPU des instruments préenregistrés** (≈ 70 USD pour la phase 0 au sens strict ; ≈ 95 avec l'échelle, la couche 1 bis, H-M1 et le gradient).
- **Le programme entier a coûté ≈ 450 USD** à ce jour, dont ≈ 156 pour les pilotes de l'organisme (24–26 oct.) et ≈ 180 pour les tours du collisionneur multi-modèles (24–27 oct.). Formulation juste : *the preregistered instrument work ran under ≈ 100 USD of GPU; the whole programme, idea-collider rounds and organism pilots included, is a few hundred dollars to date.*
- Le plafond du devis de phase 0 (150 USD, GO-2026-10-04-08) **n'est pas dépassé** par le GPU qu'il couvre (≈ 70–95) ; les dépenses d'API relèvent d'autres lignes de GO, chacune avec son plafond, toutes tenues.

## 3. Lignes ambiguës, trous
1. **Relève Gemini (23 oct.)** : 13 instances, aucun GO, aucune ligne de facturation relue depuis le relevé du 23 à 0 h (6,01). Le plan annoncé (468 USD) peut s'être réalisé en partie. **À lire sur la console Vast.ai par Lazar** (la lecture par l'API ne rend rien depuis cette session) ; seule ligne qui peut déplacer le total de plus de 15 %.
2. Relevés « à confirmer sur la facturation » : échelle (≈ 1,6–1,7), couche 1 bis (≈ 9,7–11,7), notations P2 (« au plus 8,23 », indissociable de l'autre projet de Lazar sur le même compte).
3. Disques gardés du 6 au 10 octobre (N-009, « ne détruis rien ») : ≈ 0,303 USD/h, comptés dans les « 39,6 » du 10 octobre ; ordre de grandeur 30 USD, soit près de la moitié du GPU de la phase 0.
4. Lancements de `registres/go.md` sans ligne de dépense réalisée : GO-2026-10-26-03 et -26-05 (courses v6.2.1, suspendues, 0), GO-2026-10-17-01 (pilote papier C, suspendu, 0), GO-2026-10-26-08 (cache d'activations, pré-autorisation, 0).
5. Le compte Vast.ai est partagé avec un autre projet de Lazar (`rr-…`) : certains écarts de crédit lus ne sont pas séparables (le registre le dit à chaque fois).

## 4. Ce qui manque pour un chiffre opposable
Un export de facturation Vast.ai (console) et des relevés d'usage Anthropic/Google pour octobre, rapprochés ligne à ligne de ce registre. Sans cela, dire « a few hundred dollars » et non un nombre.
