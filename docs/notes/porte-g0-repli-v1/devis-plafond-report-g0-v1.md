# Devis — plafond de dépense du report de G0, séquencé (point G0-6 du mémo de conv-audit) — v1

Lignée session-depot, 29 octobre 2026. Objet : chiffrer d'avance le plafond de calcul du report (30 novembre → 31 janvier, R-750), en deux étapes : critère 2 d'abord, puis critères 3 et 4. Ce n'est ni une lecture de G0 ni un GO. Les sources sont citées par chemin et ligne. Ce qui n'est pas observé est marqué SUPPOSÉ.

## Sources
- Heures de carte : devis v1 de la phase 0, dans `docs/decisions/proposition-P-007-plan-G0-v1.md`.
  - l. 31 : T0.6, famille (i) 8 heures, famille (ii) 10 heures ;
  - l. 32 : T0.7, 6 heures ; T0.8, 6 heures ;
  - l. 23 : débit de 119 jetons par seconde sur H200 ; la génération de T0.6, environ 4,5 millions de jetons, prend environ 10 heures.
- Prix observés, dans `registres/depenses.md` :
  - A100 80 Go, 1,08 USD/h : l. 52 (revalidation de T0.5, 1,06 h, 1,14 USD) ;
  - A100, 1,0889 USD/h : l. 65 (pilote de T0.5, 4,49 h, 4,89 USD) et l. 88 (P3, 3,64 h, 3,96 USD) ;
  - H200, environ 4,67 USD/h : l. 42 (T0.4 v3, 0,572 h, 2,67 USD) ;
  - téléchargement d'un run court, environ 0,6 USD : l. 38 ;
  - rejeu des juges : 1,92 USD (l. 227) et environ 2,79 USD (l. 234).
- Reprises observées :
  - T0.4 : six instances, dont trois échecs avant le moindre calcul (l. 7 à 9, 34, 38, 42) ;
  - notations de T0.5 : huit appels du lanceur avant exécution, presque tous sans dépense (l. 66 à 85).
- État des critères : `docs/notes/porte-g0-grille-v1/constat-etat-preuves-G0-2026-10-29-v1.md` (critères 2, 3 et 4 « manquants ») ; grille G0 v6 ; table de dépendance v4 de conv-audit (R-508), qui ne débloque 3 et 4 que sur le statut « 2 tenu » prononcé.

## Conventions de calcul
- Prix de base : A100 à 1,2 USD/h, soit le haut des prix observés (1,08 à 1,21). Pire cas : H200 à 4,67 USD/h.
- SUPPOSÉ : sur A100, une génération 1,5 fois plus lente que sur H200. Les heures du devis v1, comptées sur H200, sont donc multipliées par 1,5 au prix de base, et laissées telles quelles au pire cas.
- Reprises prudentes : × 2 sur les heures de calcul. C'est l'ordre de grandeur des relances de T0.4 et de T0.5 ; la plupart de ces relances avaient échoué avant le calcul et coûté peu, le × 2 est donc prudent.
- Frais fixes : 1 USD par run (téléchargement, disque).
- SUPPOSÉ : les prix de décembre et janvier restent ceux d'octobre.

## Étape 1 — critère 2 (T0.6 : organismes (i) et (ii), dose-réponse)

| Run | Heures (devis v1) | Base (A100, × 1,5, × 2) | Pire cas (H200, × 2) |
|---|---|---|---|
| Essai court du lanceur et sonde de mémoire | 1 | 3,6 | 9,3 |
| Famille (i) : épisodes à 4 doses × 2 intensités et témoins | 8 | 28,8 | 74,7 |
| Famille (ii) : données de distillation, adaptateurs, épisodes | 10 | 36,0 | 93,4 |
| Frais fixes (4 runs) | — | 4,0 | 4,0 |
| **Sous-total** | 19 | **72,4** | **181,5** |

- La vérité terrain de l'appariement (P-014) est un étiquetage par sous-agents. SUPPOSÉ : il passe par l'abonnement, à 0 USD de facture. S'il passe par l'interface payante, il faut une réserve de 10 USD, comptée à part ci-dessous.
- **Plafond proposé pour l'étape 1 : 80 USD.** Il couvre le cas de base avec deux reprises complètes ; il ne couvre pas le pire cas sur H200.

## Étape 2 — critères 3 (T0.7, sondes) et 4 (T0.8, bases boîte noire), sur les mêmes épisodes

| Run | Heures (devis v1) | Base | Pire cas |
|---|---|---|---|
| T0.7 : activations des épisodes de (i) et (ii), une passe | 6 | 21,6 | 56,0 |
| T0.8 : juges par action 8B et 3B, et séquentiel | 6 | 21,6 | 56,0 |
| Rejeux des juges, si la cellule est redéfinie (R-788 : H_B) | 2 × environ 2,8 | 5,6 | 11,2 |
| Frais fixes (3 runs) | — | 3,0 | 3,0 |
| **Sous-total** | 12 | **51,8** | **126,2** |

- Les sondes s'entraînent et se lisent sur processeur, sans dépense (P-011, l. 52).
- **Plafond proposé pour l'étape 2 : 60 USD.**

## Plafond total et séquencement
- Étape 1 : 80 USD. Étape 2 : 60 USD. Réserve pour l'étiquetage par l'interface payante (SUPPOSÉ) : 10 USD.
- **Total : 150 USD.** Cas de base : environ 124 USD. Pire cas des deux étapes : environ 308 USD.
- **Ouverture de l'étape 1** : préenregistrement de T0.6 scellé et contre-lu (R1, R2), et GO sur devis.
- **Passage de l'étape 1 à l'étape 2** : seulement sur le statut « 2 tenu », prononcé par un verdict scellé (table v4, R-508 ; grille v6). Les préenregistrements de T0.7 et de T0.8 doivent aussi être scellés et contre-lus. Un « non concluant » ou un « négatif » au critère 2 n'ouvre pas l'étape 2.
- **Report des crédits non dépensés** : le reliquat de l'étape 1 ne passe pas à l'étape 2 sans un mot de Lazar.
- **Plafond atteint sans verdict** : le run s'arrête (R10, par identifiant). La session ouvre un nœud ; aucun dépassement n'est engagé sans GO.
- **Exclusions** : le plafond ne couvre ni G1, ni le papier C, ni la course d'idéation, ni le pilote de la couche 2. Celui-ci hérite d'un droit de devis séparé (G0-4, option (1)).

## Décision pour Lazar
**Fixer d'avance le plafond de calcul du report de G0.**
- **Enjeu** : un plafond écrit avant le 30 novembre empêche que le report devienne une dépense ouverte. Il doit aussi laisser les critères 2, 3 et 4 atteignables.
- **(a) 150 USD, séquencé : 80 pour le critère 2, puis 60 pour les critères 3 et 4, plus 10 de réserve.**
  - Avantage : chaque étape est bornée, et l'étape 2 n'est payée que si le critère 2 tient.
  - Inconvénient : le pire cas (environ 308 USD) n'est pas couvert ; un dépassement demande un nœud.
- **(b) 250 USD en une enveloppe** (le chiffre illustratif de la synthèse).
  - Avantage : marge large, moins de nœuds.
  - Inconvénient : pas de séquencement ; l'argent des critères 3 et 4 est engageable avant que le critère 2 tienne.
- **(c) 315 USD, séquencé (pire cas couvert : 185 puis 130).**
  - Avantage : aucun nœud de dépassement prévisible.
  - Inconvénient : deux fois le cas de base, immobilisés.
- **Recommandation** : (a), confiance 0,6. Les écarts aux devis observés jusqu'ici tiennent surtout à des relances sans calcul, et le séquencement protège plus que la marge.
- **Défaut sous 48 heures** : (a).
