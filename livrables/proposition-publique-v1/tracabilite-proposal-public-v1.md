# Traçabilité de la proposition, version pour évaluateurs — v1

Rédigée le 2026-10-07 par la session, sur la décision de Lazar (« a », réponse à la décision 1 du compte rendu du README : une version de la proposition destinée aux recruteurs et à BlueDot, sans budget ni mention de confidentialité réservée au fonds). Document interne (R6).

## 1. Source

`proposal-public-v1.md` dérive de `livrables/candidature-ea-funds-v1/proposal-v1.md` (`2f1e0864110f5f74`, relue par un sous-agent neuf, R-097 ; traçabilité `livrables/candidature-ea-funds-v1/tracabilite-proposal-v1.md`). Tout ce qui n'est pas listé ci-dessous est inchangé, et garde la traçabilité de la source.

## 2. Changements

| lieu | changement | source |
|---|---|---|
| en-tête | lignes « Fund » et « Request » retirées ; « Applicant » devient « Author » ; période « 12 months from 1 November 2026, if funded » ; version « for evaluators », budget omis, mention de non-redistribution | décision de Lazar (R-104) |
| section 5, « Who does what » | même formulation que le README vérifié : trois niveaux de décision ; rédaction par les agents ; relecteurs désignés comme agents ; apport de Lazar sur la destination libre ĉ ; validation humaine budgétée dans le plan | `livrables/readme-v1/verification-readme-v1.md` (K-4, K-5, K-6) ; R-018, R-028 ; `docs/decisions/decision-N-005-N-006-v1.md` l. 20 |
| section 6, harnais | domaine (1 087 jetons au contrôle strict, 1 192 en production ; carte, logiciels, noyau) ; description exacte de la vérification ; histoire des versions 1 à 3 du préenregistrement, sans enjolivure | K-2 et K-3 du même rapport ; `prereg/T0.4-validation-modele-reel-v3.md` l. 136 et 360 ; verdict v3 l. 18 |
| section 6, code | « provisional recipe » pour le plancher ; 644 tests au 7 octobre 2026 (au lieu de 602) | `registres/etat.md`, ligne de T0.7 ; message du commit `a0d8777` |
| section 4, famille (iii) | « optional, if compute allows » au lieu de « ambitious scenario only » | scénarios de budget retirés |
| section 7 | « if funded » ; phrase sur le scénario minimal retirée | scénarios de budget retirés |
| section 9 | validation humaine « budgeted in the plan » ; devis du calcul du plan entier (800 à 1 200 heures-équivalent A100) | `livrables/premier-rendu-v1/devis-v1.md` (`16d71febf1491780`), section 2 |
| section 11 | « Author » au lieu de « Applicant » | — |
| section 12 | budget retiré, avec ses notes | décision de Lazar |

## 3. Contrôle

Contrôle mécanique, sans nouvelle relecture : la version ne fait que retirer des passages de la proposition relue et reprendre des formulations du README vérifié par un sous-agent neuf (`verification-readme-v1.md`). Recherches faites dans le texte final : aucune occurrence de « EA Funds », « Confidential », « mainline », « ambitious », « minimal », « stipend », « Applicant » ; « budget » ne désigne plus que le budget de sabotage de la théorie et la validation humaine « budgeted in the plan ». PDF de 8 pages, page 1 relue à l'œil.
