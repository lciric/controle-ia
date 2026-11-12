# Comparaison du verdict officiel et du verdict provisoire de la course A1-v4 — v1

**Accord complet sur le fond.** Les deux verdicts concordent sur les deux issues, les deux qualifications, les suspensions et leur levée, et les onze prédictions. Il n'y a de différences que dans la forme : une citation adaptée, une formule de réserve qui va plus loin que les critères, et des notes présentes dans un verdict seulement. Aucune ne change une issue.

Écrit le 10 novembre 2026 à partir de 08:58:57 UTC (heure relevée par `date -u`) par le lecteur neuf Opus 5.5 auteur du verdict officiel (session mère `session_01QPDgKgACWyCkCN8HjqwNXy` ; consigne `consigne-verdict-officiel-a1-v4-v1.md`, `25d25eb8…`). Ce fichier est écrit **après** le scellement du verdict officiel. Le verdict provisoire et la fin de R-2110 n'ont été lus qu'après ce scellement.

## Pièces comparées (dossier `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/`)

| verdict | fichier | sha256 | auteur | scellé |
|---|---|---|---|---|
| officiel | `verdict-officiel-a1-v4-v1.md` | `e6e2f17076fab16f2684553765517937d528c657367075c126945c3ae3741cda` | lecteur neuf, Opus 5.5 | 2026-11-10, avant 08:58:25 UTC (`date -u`) |
| provisoire | `verdict-a1-v4-v1.md` | `c1af538fe05032ba788bec735c32a74dd356fca290159c9177a20e131eac82e4` (vérifiée contre son compagnon avant lecture) | lecteur neuf Fable 5.2, auteur aussi de l'audit | prononcé à 08:49:31 UTC |

Lu aussi après le scellement : `registres/decisions.md`, R-2110 en entier. Cette entrée résume le rendu du lecteur Fable. Elle consigne l'écart de rôles (audit et verdict confiés au même lecteur) et la décision de routine de faire prononcer le verdict officiel par un lecteur Opus. Rien dans cette entrée ne change le verdict officiel.

## Point par point

| # | point | verdict officiel | verdict provisoire | accord |
|---|---|---|---|---|
| 1 | Issue de W2, ordre 2, 6, 1, 3, 4, 5 | 3, « résiste (à cette taille) » (1/24 ; Wilson [0,0074 ; 0,2024] ; dents 24/24 ; instrument sain : 349/349, 0,971, 0,995) | même issue, mêmes nombres | **accord** |
| 2 | Qualification de W2 | sans objet (aucune brèche) | sans objet | **accord** |
| 3 | Suspension de W2 | suspendue par A1 (texte) et A2 (code) ; levée par l'audit écrit, raison donnée (A1 « rien d'anormal », A2 multiplicité, aucun défaut). Point d'interprétation déclaré : l'audit n'écrit pas le mot « levée », je lis sa conclusion (§ 9) comme la levée | mêmes déclencheurs ; « Suspension levée », au vu des mêmes constats | **accord** (le verdict provisoire, écrit par l'auteur de l'audit, dit la levée en toutes lettres : mon point d'interprétation est confirmé) |
| 4 | Lecture bornée de W2 | recopiée **mot pour mot** de B2v4 l. 290–292 (« sur deux mondes jouets au nul v9 … »), avec une note : dans cette course, W2 seul est au nul | donnée « dans les mots du texte », mais **adaptée** (« sur un monde jouet au nul v9 … ») | **accord sur le sens, différence de forme** : la phrase du provisoire n'est pas exactement celle du texte gelé |
| 5 | Issue de W2g, ordre 2′, 6′, 1′, 3′, 4′, 5′ | 2′, « frontière franchie » (10/24 ; Wilson [0,2447 ; 0,6117]) ; 6′ et 1′ contrôlés pour mémoire | même issue, mêmes nombres ; 6′ et 1′ pour mémoire | **accord** |
| 6 | Qualification de W2g | « frontière franchie, robuste », r = 10/17 = 0,588 ; 12/17 avec une famille de Holm par monde, même qualification ; recalculé par moi à partir des comptes de l'audit | même qualification, même r ; mentionne 12/17 | **accord** |
| 7 | Suspension de W2g | aucune : A4 seul ; A1 et A2 non déclenchés ; pas d'A3 sur W2g | aucune, mêmes raisons | **accord** |
| 8 | Lecture de « robuste » sur W2g | phrase gelée du § 6.2, recopiée ; **pas** « le v9 n'a pas de prix » | même phrase | **accord** |
| 9 | A9 et écart d'Argon (R-2043) | non déclenché ; aucune perturbation ; réserve 6 de l'audit recopiée | non déclenché ; aucune perturbation ; détail des fenêtres | **accord** |
| 10 | A7 | non déclenché (0 appel `budget_depasse`). Un appel a coûté plus que sa réserve (1,6259 USD pour 1,6178). Ce dépassement est discuté : ce n'est pas un déclencheur du code gelé, et il serait sans effet même lu comme un A7 | « aucun appel refusé », sans discuter ce dépassement | **accord** ; note en plus dans le verdict officiel |
| 11 | P1 à P11 | tenues : P1, P2, P3, P4, P5, P8, P10, P11 ; non tenues : P6, P7, P9. P1, P3 et P8 sont tenues à la limite du compte | mêmes tenues et non tenues ; P8 « tenue au compte » | **accord** |
| 12 | Réserve « λ\* à la limite » à côté de P7 (§ 6.2, obligatoire) | écrite à côté de P7 | écrite (réserve 1, « écrite à côté de P7 non tenue ») | **accord** |
| 13 | Gain du retour sur W2g | garde contre la sur-lecture de P8 : H3 est descriptive, et la lecture donne « non tranché » (5 contre 2, McNemar p = 0,453 ; écart par loi −0,020) | réserve 3 : « Le retour n'est pas ce qui fait franchir : sans retour, 7 sur 24 (au-dessus de 4 sur 24 aussi) » ; « Le gain du retour n'est pas établi par cette course » | **accord sur le fond** (gain non établi). **Réserve de forme** : le titre « le retour n'est pas ce qui fait franchir » applique au bras témoin la règle de 2′, que le § 6.2 ne lit que sur le bras « retour ». C'est une lecture au-delà des critères (R8). La phrase qui suit, « le gain du retour n'est pas établi », suffit et reste dans la lecture descriptive de H3 |
| 14 | Autres réserves de l'audit (trop propre, W2 à la limite, sept cartes sous le seuil, famille de Holm, rôles, source du code, non vérifié) | les neuf réserves du § 8 de l'audit, recopiées mot pour mot et contrôlées par programme | reprises en substance, reformulées ; plus une réserve « robustesse partielle » (7 lois sur 17 non robustes, P9) | **accord** (même contenu ; la réserve « robustesse partielle » redit P9 non tenue) |
| 15 | Rôles (§ 13, point 12) | réserve 7 de l'audit recopiée ; le verdict officiel, prononcé par un lecteur Opus d'une autre lignée que l'auditeur, répond à la lettre pour le verdict | déclare l'écart (réserve 8) | **accord** ; l'écart est levé pour le verdict par le présent verdict officiel. L'audit reste celui du lecteur Fable |
| 16 | Règle de rapport | non écrite | « se rapporte avec A1 et les trois courses d'A1-v3, jamais seul » (texte § 0.5 bis ; aussi § 13, point 12) | **accord sur la règle** ; omission dans le verdict officiel, signalée ici : la règle vaut pour lui aussi |
| 17 | Ce que le verdict ne dit pas | pas de section dédiée ; les lectures bornées gelées sont recopiées | section 6 : limites (prix du v9, « rien au-delà de l'archive », un fournisseur, etc.) | **accord** : ces limites ne revendiquent rien et ne contredisent aucun critère |

## Bilan

- **Désaccord sur une issue, une qualification, une suspension ou une prédiction : aucun.**
- Différences de forme, sans effet sur l'issue :
  - la lecture bornée de W2 est adaptée dans le provisoire au lieu d'être recopiée (point 4) ;
  - le titre de la réserve 3 du provisoire va au-delà des critères (point 13) ;
  - le verdict officiel n'écrit pas la règle de rapport avec A1 et A1-v3 (point 16).
- Le verdict que la consigne nomme officiel est `verdict-officiel-a1-v4-v1.md`. Le provisoire reste tel quel (R12). La soumission à Lazar revient à la mère.
