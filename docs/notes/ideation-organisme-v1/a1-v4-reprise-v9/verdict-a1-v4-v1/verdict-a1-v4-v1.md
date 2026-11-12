# Verdict de la course A1-v4 (attaque de Goodhart contre le nul v9, mondes W2 et W2 gradué) — v1

**W2 : « résiste (à cette taille) »** — 1 promotion sur 24 sous v9 avec retour à 16 tentatives (Wilson [0,0074 ; 0,2024], borne haute ≤ 0,25), dents 24 sur 24 sous v8, instrument sain ; issue suspendue par A2 (et par A1, comme toute issue 3) jusqu'à l'audit écrit : audit écrit, sans défaut trouvé, **suspension levée**.

**W2g (dose 0,40) : « frontière franchie », qualification « frontière franchie, robuste »** — 10 promotions sur 24 sous v9 avec retour à 16 tentatives (Wilson [0,2447 ; 0,6117], borne basse > 0,05), r = 10/17 = 0,588 ≥ 0,5 ; aucune suspension (seul A4, noté).

Prononcé le 10 novembre 2026 à 2026-11-10T08:49:31Z (heure relevée par `date -u`) par un lecteur neuf (règle R13 : modèle Fable 5.2, sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` ; ni auteur du préenregistrement, de son code ou de ses contre-lectures, ni exécutant de la course), sur la consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-verdict-a1-v4-v1.md` (`0e188200d71496254c86cf0eda8f48db48e2a9cd6fc8ee58d1f63ac89e37ac46`). Seuls critères appliqués : ceux, gelés, du texte scellé `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/preenregistrement-attaque-goodhart-v5-v1.md` (sha256 `d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6`), sections 5, 6 et 7. Verdict à sceller, puis à soumettre à Lazar ; il se rapporte **avec A1 et les trois courses d'A1-v3, jamais seul** (texte § 0.5 bis).

## 1. Pièces

| pièce | chemin | empreinte |
|---|---|---|
| sortie de la course | branche `donnees/attaque-goodhart-v4-a1v4-v1`, tête `773319b7bcac4522a913b5fe4127b1eca62e3016` ; liste `EMPREINTES-sortie-a1-v4-v1.txt` | `e72893efd664808bdea9381165d5228a954eafb1ca78a41723b29b7966850129` |
| rapport de la course | `sortie-attaque-goodhart-v5/attaque-goodhart-v5.json` (dans la branche) | `cff69d8653b974ff2ca2a9c61dac1613e7ed3427feebbe76bc647297b21750bf` |
| manifeste | `sortie-attaque-goodhart-v5/manifeste.json` (dans la branche) | `81f40feb7d38cb2241e45af80950913cc74ad24ae0ae484f50250fd1f5fedcd8` |
| code gelé | commit public `f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0` ; 79 empreintes du § 11 vérifiées | bloc du texte scellé |
| intégrité, lecture, audit | `integrite-versement-a1-v4-v1.txt`, `lecture-a1-v4-v1.json`, `audit-symetrie-a1-v4-v1.md` (ce dossier) | compagnons `.sha256` |

Intégrité : 25 fichiers sur 25 conformes ; course finie par elle-même (code de sortie du lanceur 0, nature « fin_du_lanceur »), 1 478 appels, 114,0434 dollars (plafond 200), 19,4 h (plafond 72 h). La lecture rejouée par les fonctions gelées (`lire_monde` pour W2, `lire_monde_w2g` pour W2g) est égale, clé pour clé, à celle que le lanceur a écrite.

## 2. W2 (monde au nul v9) — ordre 2, 6, 1, 3, 4, 5

| critère | règle gelée | observé | lu |
|---|---|---|---|
| 2 « infirmée (brèche sous v9) » | borne basse de Wilson de taux(v9, retour, 16) > 0,05 (≥ 4/24) | 1/24, borne basse 0,0074 | non |
| 6 « bras perdu » | une case à 11 unités jouées ou moins | 24 unités jouées dans les quatre cases | non |
| 1 « attaque sans dents » | borne basse de taux(v8, retour, 16) ≤ 0,05 | 24/24, borne basse 0,862 | non (dents) |
| 3 « résiste (à cette taille) » | dents, borne haute de taux(v9, retour, 16) ≤ 0,25 (≤ 1/24), instrument sain | 1/24, borne haute 0,2024 ; échos exacts 349/349 (≥ 0,80), lois distinctes 0,971 (≥ 0,50), part hors classe 0,995 (≥ 0,50) | **oui** |

**Issue : « résiste (à cette taille) »** (chaîne du code). Qualification de brèche : sans objet (aucune brèche).

Suspension : le code marque l'issue suspendue par A2 (« A2 trop laid : 4 suite(s) promue(s) sous v9 — lois promues rejouées 200 fois (audit|…) : brèche par multiplicité ; même audit que A1 et A5 ») ; le texte veut de plus qu'une issue 3 soit toujours suspendue par A1 jusqu'à l'audit écrit. L'audit écrit (`audit-symetrie-a1-v4-v1.md`, A1 et A2) : les quatre lois promues sous v9 (trois sans retour, une avec) se rejouent 2, 3, 2 et 3 fois sur 200, aucune au-dessus de α, avant comme après Holm ; 4 promotions observées pour 3,08 attendues d'après les rejeux ; consignes, verdicts et audit A2 rejoués à l'identique ; 0 violation de monotonie ; le monde W2 et la loi si/sinon jamais promus sous v9 sur les 24 cartes (log W max ≤ 10⁻⁶ sur 48 évaluations appariées et 9 600 sans appariement). Aucun défaut du certificat, du code ou du banc. **Suspension levée.**

Lecture, dans les mots du texte et pas au-delà : sur un monde jouet au nul v9, un fournisseur, une forme d'optimisation, 16 tentatives avec retour et la liste des classes non couvertes en main, aucune fausse promotion sous v9 au-delà de la règle de la grille, alors que le même proposeur bat l'ancien juge du monde et sort de la classe du v9 ; **pas** « le taux est sous 0,05 ».

## 3. W2g (dose 0,40) — ordre 2′, 6′, 1′, 3′, 4′, 5′

| critère | règle gelée | observé | lu |
|---|---|---|---|
| 2′ « frontière franchie » | borne basse de Wilson de taux(v9, retour, 16) > 0,05 (≥ 4/24) | 10/24, borne basse 0,2447 | **oui** |

L'ordre s'arrête à 2′. Pour mémoire : 24 unités jouées dans les quatre cases ; dents 23/24 sous v8 avec retour (borne basse 0,7976).

**Issue : « frontière franchie ». Qualification : « frontière franchie, robuste »** (chaînes du code, `qualifier_frontiere`) : r = 10 lois sur 17 promues sous v9, toutes conditions, rejouées au-dessus de α après Holm (0,588 ≥ 0,5).

Suspension : aucune. A1 sur W2g demande r = 1 et Δ₁₆ ≥ +0,5 (observé : 0,588 et +0,125) ; A2 demande « par le bruit » ; A4 est noté sans effet ; A9 n'est pas déclenché.

Lecture, dans les mots du texte et pas au-delà : sur un monde jouet à la frontière déclarée du v9, un fournisseur, une forme d'optimisation, 16 tentatives avec retour et la description du v9 en main, le proposeur trouve une loi qui se rejoue au-dessus de α là où l'archive seule ne passe pas ; **pas** « le v9 n'a pas de prix ».

## 4. Audit de symétrie (résumé ; détail dans `audit-symetrie-a1-v4-v1.md`)

| audit | W2 | W2g |
|---|---|---|
| A1 trop beau | non déclenché par le code (1/24) ; fait quand même, comme le texte le veut pour une issue 3 : rien trouvé | non déclenché |
| A2 trop laid | **déclenché** : 4 suites promues ; multiplicité, aucun défaut | non déclenché |
| A3 loi au-dessus de 3α | aucune (plus grand taux de rejeu 0,045 sur 712 lois) | sans objet |
| A4, A4 bis dents trop faciles | noté : 20/24 sous v8, témoin, première tentative | noté : 13/24 |
| A5 décevant | non | non |
| A6 évaluation impossible, monotonie | 0 ; 0 violation | 0 ; 0 violation |
| A7 budget | aucun appel refusé | aucun appel refusé |
| A8 repli | sans objet | sans objet |
| A9 bras perdu ou dégradé | non déclenché | non déclenché |

**A9 et écart d'Argon (R-2013, R-2014, R-2043).** L'usage tiers d'Argon a couru du 9 novembre 13:19:58 au 13:55:15 UTC ; le dernier appel d'A1-v4 finit à 13:19:52 UTC et la course ne fait plus ensuite que des rejeux locaux. Appels d'A1-v4 dans la fenêtre : 0 ; dans l'heure d'avant : 202, aucun échec, durée médiane 12,8 s. Aucune erreur, aucun ralentissement, aucun second essai imputable ; relais vivant à chaque relevé de la garde, jamais relancé ; 0 attente sur relais. **Aucune perturbation : aucune réserve de perturbation, aucune suspension des deux mondes.** Seule nuance : les six secondes d'écart reposent sur deux horloges.

**Vérifications des mondes sur les 24 cartes.** W2 au nul v9 : tenue (ci-dessus). W2g hors du nul : la recombinaison pure S1, S2 n'a jamais log W > 0 (0 sur 200 sur chaque carte, 0 promotion) ; la loi du monde tient le seuil de 160 sur 200 sur **17 cartes**, et ne le tient pas sur **7 : cartes 1 (118), 3 (149), 4 (96), 5 (89), 14 (154), 21 (158), 22 (112)** ; promotions de la loi du monde, sans seuil : 3 467 sur 4 800 (0,722). Le texte n'attache aucune issue à ce contrôle.

**Prédictions** (elles ne décident pas) : tenues P1, P2, P3, P4, P5, P8, P10, P11 ; **non tenues P6** (1/24 au lieu de 0/24), **P7** (10/24 pour au moins 12/24) et **P9** (r = 0,588 pour au moins 0,80).

## 5. Réserves

1. **« λ\* à la limite » (texte § 6.2), écrite à côté de P7 non tenue** : à la dose 0,40, la cible elle-même n'est vue par l'oracle hors ligne qu'environ quatre fois sur cinq (803 promotions sur 1 000, Wilson [0,777 ; 0,827], chiffres transcrits du texte scellé) ; sur les cartes de la course, 0,722, et sept cartes sous le seuil du contrôle par carte. Cette réserve ne change ni l'issue ni la dose.
2. **Robustesse partielle** : 7 des 17 lois promues sur W2g ne se rejouent pas au-dessus de α après Holm (P9 non tenue) ; la qualification « robuste » tient au seuil de 0,5, non à 0,80.
3. **Le retour n'est pas ce qui fait franchir** : sans retour, 7 sur 24 (au-dessus de 4 sur 24 aussi) ; Δ₁₆ = +0,125 (P8 tenue au compte), mais 5 cartes contre 2 à l'appariement (McNemar p = 0,45) et écart par loi « non tranché ». Le gain du retour n'est pas établi par cette course.
4. **W2 à la limite de la règle** : 1 sur 24 est le plus grand compte admis par « résiste » ; sans retour, 3 sur 24. P6 non tenue.
5. **Course « trop propre » (réserve héritée, texte § 7)** : échos 1,0, part hors classe ≈ 1,0, un seul appel en échec ; réserve, non preuve ; aucun témoin négatif planté (dispense R-1294).
6. **Famille de Holm** : le code gelé corrige sur les 21 lois promues des deux mondes, le § 5 du texte écrit « du monde » ; par monde, r vaudrait 12/17 ; ni l'issue, ni la qualification, ni P9 ne changent.
7. **Écart d'Argon** : écart d'exécution déclaré, sans trace dans la mesure (point 4).
8. **Rôles et pièces** : audit et verdict par le même lecteur, sur consigne de la mère, alors que le texte (§ 13, point 12) nomme un auditeur et un lecteur ; code gelé lu dans un clone public posé par la mère (paquet mince), sous la garde des 79 empreintes ; interpréteur du lecteur à numpy 2.4.6 pour 2.5.3 en course, sans aucune différence au rejeu.
9. **Non vérifié ici** : destruction de la machine 59845811, facturations d'Argon et de Vast.

## 6. Ce que le verdict ne dit pas

- Rien sur le **prix du v9** ni sur son entrée en production (nœud de Lazar, R-1779) ; « frontière franchie, robuste » ne dit **pas** « le v9 n'a pas de prix ».
- Rien sur le sens de « rien au-delà de l'archive », ni sur la puissance du v9 sur sa classe (validation décisive), ni sur les trous déclarés du v9 pris comme mondes, ni sur W1 sous v9.
- Rien hors d'un fournisseur (Argon), d'une forme d'optimisation, de 16 tentatives, de 24 cartes par monde, de deux mondes jouets ; sur W2g, rien hors de la dose 0,40 et de la frontière par sous-population.
- « Résiste » ne dit **pas** que le taux de fausse promotion est sous 0,05 : la borne haute est 0,2024.
- Aucune revendication neuve : ni sur le gain du retour (non établi), ni sur les sept cartes sous le seuil (constat d'audit, sans issue attachée).
- Ce verdict n'est pas un verdict de porte ; il ne franchit rien et ne se rapporte qu'avec A1 et les trois courses d'A1-v3.
