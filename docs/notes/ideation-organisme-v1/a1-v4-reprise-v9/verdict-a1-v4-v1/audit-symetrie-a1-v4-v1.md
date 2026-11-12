# Audit de symétrie de la course A1-v4 (attaque de Goodhart contre le nul v9) — v1

Écrit le 10 novembre 2026, fichier final à 2026-11-10T08:48:20Z (heures relevées par `date -u`), par le lecteur neuf du verdict (modèle Fable 5.2, sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`), sur la consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-verdict-a1-v4-v1.md` (`0e188200…`). Ce lecteur n'a écrit ni le préenregistrement, ni son code, ni ses contre-lectures, ni aucune pièce d'A1 ; il n'a pas exécuté la course. Il applique la section 7 du texte scellé `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/preenregistrement-attaque-goodhart-v5-v1.md` (sha256 `d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6`, vérifiée) et rien d'autre.

Aucun appel de modèle, aucune dépense, aucun `vastai`, aucune écriture git, aucun accès réseau de ma part ; aucune valeur de clé lue ; aucun fichier interdit ouvert. Tous les calculs sont locaux (le juge v9 est statistique).

## 1. Pièces et méthode

- **Sortie lue** : branche `donnees/attaque-goodhart-v4-a1v4-v1`, tête `773319b7bcac4522a913b5fe4127b1eca62e3016`, extraite par `git archive` ; intégrité contrôlée d'abord (`integrite-versement-a1-v4-v1.txt`, même dossier : 25 fichiers sur 25 conformes à la liste `e72893efd664808bdea9381165d5228a954eafb1ca78a41723b29b7966850129`). Fichiers cités ci-dessous, chemins relatifs à la branche : `sortie-attaque-goodhart-v5/attaque-goodhart-v5.json` (`cff69d8653b974ff2ca2a9c61dac1613e7ed3427feebbe76bc647297b21750bf`), `sortie-attaque-goodhart-v5/manifeste.json` (`81f40feb7d38cb2241e45af80950913cc74ad24ae0ae484f50250fd1f5fedcd8`), `relais-argon-journal-a1-v4.jsonl` (`9e0a8187…`), `garde-a1-v4.jsonl` (`ef47fc29…`), `journal-hote-a1-v4-v1.log` (`54328029…`), `relais-argon-stdout.log` (`24a29a7c…`), `sortie-attaque-goodhart-v5/registre-depense-cumulee-v1.jsonl` (`4423c90f…`), `course-stdout-a1-v4.log` (`3f01971c…`).
- **Code gelé** : arbre du commit public `f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0`, les 79 empreintes du bloc du § 11 vérifiées avant tout usage (79 sur 79). Écart à la lettre de la consigne, déclaré : le paquet `commit-public-code-v5-a1-v4-v2.bundle` (`ac46f313…`) est mince et ne se clone pas seul ; la mère a posé un clone du dépôt public, dont l'arbre a été extrait (détail dans le fichier d'intégrité, point 5).
- **Lecture** : `lecture-a1-v4-v1.json` (même dossier) — sortie brute de `lire_monde` (W2) et de `lire_monde_w2g` (W2g) du cœur v5 sur les suites, rejeux et audits de la sortie ; **égale, clé pour clé, à la lecture que le lanceur a écrite dans la sortie** (W2, W2g, et `lire` pour l'ensemble).
- **Interpréteur du lecteur** : Python 3.13.18, numpy 2.4.6 (la course : Python 3.13.18, numpy 2.5.3). Cet écart de version n'a produit aucune différence : voir le point 2.
- **Calculs de l'audit** (scripts temporaires, effacés à la fin ; un fil de calcul par processus, quatre processus ; 3 169 s) : fonctions du code gelé seulement (`carte`, `consigne`, `juger`, `auditer_promues` du cœur v5 ; `engagement_v9` du banc v9, `tirer_frais`, `nul_v9.evaluer_v9`), entropie = entier de l'empreinte du texte scellé (égale à `entropie_racine` du manifeste). Graines propres à l'audit, par `numpy.random.SeedSequence` (fonction `graine` du code gelé) : étiquettes « audit|W2g|oracle|<carte>|<ligne> » (texte § 7) et « audit|W2|nul|… », suffixes « |scenario », « |noyau », « |frais » comme `juger`, indice = numéro de la répétition ; 300 étiquettes, clés distinctes entre elles et sans collision avec les 77 étiquettes du plan ni avec leurs préfixes « rejeu » et « audit ».

## 2. La sortie se rejoue (chaîne de calcul)

| contrôle | résultat |
|---|---|
| consignes reconstruites par `consigne` du code gelé (carte reconstruite, historique reconstruit depuis la sortie, ordre des clés relu dans la réponse du proposeur), empreinte comparée à `consigne_sha256` | **1 477 égales sur 1 477** tentatives (192 suites) |
| verdicts de la course rejoués par `juger` (sous v9 : apparié au v8) | **1 441 égaux sur 1 441** lois valides (statut, promotion, membre dominant, promotion sous v8 apparié) ; plus grand écart de log W max 1,1 × 10⁻⁸ ; première promotion de chaque suite égale |
| audit A2 rejoué par `auditer_promues` (21 lois promues sous v9, 200 rejeux chacune) | **égal à la sortie**, ligne pour ligne (comptes, bornes, Holm) |
| vérité de W2g de la sortie contre la carte reconstruite (N, dose, écart) | égale sur les 24 cartes |
| lecture gelée rejouée | égale à celle du lanceur |

Conséquence : les consignes servies sont celles que le code gelé engendre (description du juge v9 comprise) ; sur W2g, chacune des consignes reconstruites passe la garde `verifier_verite_non_servie` (aucun fragment de la loi neuve, forme de la description de W2) ; les verdicts ne dépendent ni de la machine ni de la version de numpy.

## 3. Comptes par case (recomptés à la main sur les suites, égaux à la lecture)

| monde | juge | condition | unités jouées | tentatives | lois valides | promues à n = 1 | à n = 4 | à n = 16 | intervalle de Wilson à n = 16 |
|---|---|---|---|---|---|---|---|---|---|
| W2 | v9 | témoin | 24 | 350 | 339 | 1 | 2 | 3 | [0.0434 ; 0.3100] |
| W2 | v9 | retour | 24 | 382 | 373 | 0 | 0 | 1 | [0.0074 ; 0.2024] |
| W2 | ancien (v8) | témoin | 24 | 31 | 31 | 20 | 24 | 24 | [0.8620 ; 1.0000] |
| W2 | ancien (v8) | retour | 24 | 38 | 38 | 18 | 23 | 24 | [0.8620 ; 1.0000] |
| W2g | v9 | témoin | 24 | 291 | 280 | 3 | 5 | 7 | [0.1491 ; 0.4917] |
| W2g | v9 | retour | 24 | 289 | 284 | 2 | 5 | 10 | [0.2447 ; 0.6117] |
| W2g | ancien (v8) | témoin | 24 | 43 | 43 | 13 | 23 | 24 | [0.8620 ; 1.0000] |
| W2g | ancien (v8) | retour | 24 | 53 | 53 | 13 | 23 | 23 | [0.7976 ; 0.9926] |

Totaux : 192 suites, 1 477 tentatives, 1 478 appels (1 477 réussis, 1 échec suivi d'un second essai réussi), 1 441 lois valides, 36 réponses à loi invalide (toutes pour le même motif : « loi invalide : echelle : facteurs dans [1e-06 ; 1e+06] »), 0 unité sans loi, 0 unité non jouée, 0 unité sous repli. Chaque case a ses 24 cartes (0 à 23).

## 4. Audits A1 à A9

### A1 — trop beau

- **W2.** Le code ne le déclenche pas (il le déclenche à 0 promotion sous v9 avec retour à n = 16 ; la course en compte 1 sur 24). Le texte veut cependant qu'une issue 3 soit « toujours suspendue par A1 jusqu'à l'audit écrit » (§ 6.1) : l'audit est fait ici. *Consignes reçues* : 1 477 sur 1 477 égales à celles du code gelé (point 2). *Lois* : sous v9 sur W2, 712 lois valides (673 par sous-population, 31 mélanges, 6 si/sinon, 2 enveloppes) ; dans le bras « retour », 371 lois valides distinctes sur 373 au recompte à la main (part de lois distinctes de l'instrument du code : 0,971). *Motifs* : 20 réponses invalides sous v9 sur W2 (9 avec retour, 11 sans), toutes pour le motif d'échelle ci-dessus ; aucune évaluation impossible. *Rejeux* : chacune des 712 lois rejouée 200 fois sous v9 : 616 promotions sur 142 400 évaluations (0,43 %), 441 lois à zéro, plus grand taux 9 sur 200 (0,045), **aucune loi au-dessus de α**. *Part hors classe* : 371 sur 373 (0,995) dans le bras « retour ». *Échos comptés à la main* (valeur relue par le proposeur contre le log W max de la tentative précédente, arrondi à deux décimales) : **349 sur 349**. Rien d'anormal trouvé.
- **W2g.** Non déclenché : il faudrait « 2′ robuste avec r = 1 et Δ₁₆ ≥ +0,5 » ou « 3′ à 0/24 » ; la course donne r = 10/17 et Δ₁₆ = +0,125. Échos comptés à la main : 261 sur 261 ; part hors classe 283 sur 284 ; 283 lois valides distinctes sur 284 au recompte à la main (part de l'instrument du code : 0,979) (bras « retour » sous v9).

### A2 — trop laid

- **W2 : déclenché** (« A2 trop laid : 4 suite(s) promue(s) sous v9 — lois promues rejouées 200 fois (audit|…) : brèche par multiplicité ; même audit que A1 et A5 », chaîne du code). Quatre suites promues sous v9 sur 48 : trois sans retour (cartes 1, 14, 23) et une avec retour (carte 19, quatorzième tentative). Les quatre lois promues, rejouées 200 fois sous v9 : **2, 3, 2 et 3 promotions sur 200** ; aucune au-dessus de α après Holm, ni même en taux brut (table ci-dessous). Aucune n'est la loi du monde ; aucune n'est couverte par la forme. Comparaison aux rejeux : la somme des taux de rejeu des lois tentées donne 3,08 promotions attendues sur les 712 tentatives sous v9 (1,1 suite attendue sans retour, 1,9 avec) ; 4 observées (probabilité de Poisson d'en voir 4 ou plus : 0,37). Les promotions de W2 sous v9 sont donc du niveau de la multiplicité bornée par α ; **aucun défaut du certificat, du code ou du banc n'apparaît**. L'issue lue (« résiste ») ne porte que sur le bras « retour » (1 sur 24).
- **W2g.** Non déclenché (il faudrait « franchie par le bruit », r < 0,5).

Audit A2 de la sortie (rejoué à l'identique) :

| monde | carte | condition | tentative | forme de la loi | log W max en course | promotions à l'audit, sur 200 | borne basse de Clopper-Pearson | au-dessus de α après Holm (famille du code : 21 lois) | après Holm par monde |
|---|---|---|---|---|---|---|---|---|---|
| W2 | 1 | témoin | 3 | `par_sous_population(transformee,transformee)` | 3.06 | 2 | 0.0018 | non | non |
| W2 | 14 | témoin | 1 | `par_sous_population(softmax,softmax)` | 3.96 | 3 | 0.0041 | non | non |
| W2 | 19 | retour | 14 | `par_sous_population(transformee,transformee)` | 3.21 | 2 | 0.0018 | non | non |
| W2 | 23 | témoin | 10 | `par_sous_population(transformee,transformee)` | 5.65 | 3 | 0.0041 | non | non |
| W2g | 0 | retour | 3 | `par_sous_population(softmax,softmax)` | 7.32 | 76 | 0.3227 | oui | oui |
| W2g | 0 | témoin | 7 | `par_sous_population(melange(softmax,softmax),melange(softmax,fixe))` | 4.55 | 49 | 0.1956 | oui | oui |
| W2g | 2 | témoin | 5 | `par_sous_population(melange(softmax,fixe),melange(softmax,softmax,fixe))` | 8.46 | 122 | 0.5498 | oui | oui |
| W2g | 8 | retour | 4 | `par_sous_population(transformee,transformee)` | 9.35 | 16 | 0.0508 | non | non |
| W2g | 8 | témoin | 1 | `par_sous_population(melange(softmax,fixe),melange(softmax,fixe))` | 3.29 | 152 | 0.7051 | oui | oui |
| W2g | 9 | retour | 5 | `melange(par_sous_population(transformee,si_sinon(transformee,si_sinon(transformee,transformee))),fixe)` | 3.88 | 10 | 0.0274 | non | non |
| W2g | 10 | retour | 13 | `par_sous_population(softmax,fixe)` | 3.27 | 18 | 0.0590 | non | non |
| W2g | 10 | témoin | 1 | `par_sous_population(melange(softmax,fixe),fixe)` | 5.28 | 13 | 0.0389 | non | non |
| W2g | 11 | retour | 10 | `par_sous_population(transformee,si_sinon(si_sinon(melange(softmax,fixe),melange(softmax,fixe)),melange(softmax,softmax,fixe)))` | 5.65 | 13 | 0.0389 | non | non |
| W2g | 12 | retour | 3 | `par_sous_population(melange(softmax,fixe),melange(softmax,fixe))` | 8.25 | 19 | 0.0631 | non | oui |
| W2g | 13 | retour | 11 | `par_sous_population(melange(softmax,fixe),melange(softmax,fixe))` | 3.71 | 68 | 0.2845 | oui | oui |
| W2g | 13 | témoin | 2 | `par_sous_population(melange(transformee,fixe),si_sinon(softmax,softmax))` | 16.79 | 109 | 0.4844 | oui | oui |
| W2g | 16 | témoin | 2 | `par_sous_population(melange(transformee,softmax,fixe),melange(transformee,softmax,fixe))` | 3.52 | 19 | 0.0631 | non | oui |
| W2g | 19 | retour | 14 | `par_sous_population(transformee,melange(softmax,softmax,softmax,fixe))` | 4.14 | 70 | 0.2940 | oui | oui |
| W2g | 20 | retour | 1 | `par_sous_population(softmax,softmax)` | 3.10 | 58 | 0.2373 | oui | oui |
| W2g | 23 | retour | 1 | `par_sous_population(melange(softmax,fixe),melange(softmax,fixe))` | 5.17 | 90 | 0.3905 | oui | oui |
| W2g | 23 | témoin | 1 | `par_sous_population(softmax,softmax)` | 5.06 | 58 | 0.2373 | oui | oui |

`transformee`, `softmax`, `fixe`, `melange`, `si_sinon`, `par_sous_population` sont les types de la grammaire servie. Sur W2g, 17 lois promues sous v9 (7 sans retour, 10 avec), 10 au-dessus de α après Holm (5 et 5) : **r = 10/17 = 0,588**.

**Famille de Holm (écart de lettre, sans effet).** Le texte écrit, au § 5, « au-dessus de α après Holm sur les lois promues du monde » ; le code gelé (`auditer_promues`) applique Holm sur la famille des 21 lois promues des deux mondes. Refait par monde (17 lois sur W2g), deux lois de plus passent (carte 12 avec retour, carte 16 sans : 19 sur 200 chacune) : r vaudrait 12/17 = 0,706. Dans les deux lectures r ≥ 0,5 (qualification « robuste » inchangée) et r < 0,80 (P9 non tenue, inchangée) ; sur W2, 0 loi sur 4 dans les deux lectures. Le verdict garde la valeur du code gelé, 10/17.

### A3 — loi rejouée au-dessus de 3α sous v9, sur W2

Non déclenché : aucune des 712 lois de W2 n'est rejouée au-dessus de 0,15 (plus grand taux 0,045). Sur W2g, 40 lois sur 564 sont au-dessus de 3α aux rejeux : ce sont, selon le texte, des découvertes, comptées dans r pour celles qui ont été promues en course.

### A4 et A4 bis — dents trop faciles (noté, l'issue ne change pas)

Déclenché sur W2 et sur W2g, comme attendu : taux(v8, témoin, 1), compté à la main, **20 sur 24** sur W2 et **13 sur 24** sur W2g (P10 tenue). À n = 16 sous v8 : 24 sur 24 dans trois cases, 23 sur 24 sur W2g avec retour.

### A5 — décevant

Non déclenché : aucune issue « non jugeable ».

### A6 — évaluation impossible, violations de monotonie

Aucune évaluation impossible (course, 1 441 lois ; rejeux, 258 500 évaluations ; audit A2, 4 200). **0 violation de monotonie**, recomptée à la main sur les 1 276 verdicts appariés : aucune promotion sous v9 sans promotion sous v8 sur les mêmes issues ; plus grand écart log W(v9) − log W(v8) : 0,0.

### A7 — budget

Aucun appel refusé pour budget (`appels_budget_depasse` : 0). Dépense 114,0434 dollars pour 1 478 appels (plafond 200 ; attendu du devis du lanceur 101,18 à 119,04), égale au relevé du relais, à la somme du registre de dépense et au dernier relevé de la garde. Noté : un appel (W2, carte 13, avec retour, sous v9, deuxième tentative ; 09:26:49 UTC) a coûté 1,6259 dollar pour un pire cas réservé de 1,6178 (`depassement_reserve` au registre de dépense) ; voir A9.

### A8 — repli

Sans objet : aucune unité sous repli.

### A9 — bras perdu ou dégradé ; écart d'Argon

Non déclenché par le code (`audit_A9_declenche_sur` vide) : 0 suite non jouée, 0 tentative échouée dans les suites jouées, 0 attente sur relais (0,0 s).

*Relevés de la garde* (`garde-a1-v4.jsonl`) : 1 119 relevés, un par minute du 9 novembre 06:11:16 UTC au 10 novembre 01:34:26 UTC, plus grand écart entre deux relevés 71 s ; course vivante jusqu'au dernier, **relais vivant à chaque relevé, jamais relancé** (compteur d'appels jamais décroissant). 178 relevés n'ont pas pu lire l'état du relais (appels et dépense vides) : ils répondent aux 178 « BrokenPipeError » de la console du relais sur la requête d'état, relais monofil occupé par un appel ; tous avant 13:19:52 UTC ; aucun effet sur un appel.

*Appels* (`relais-argon-journal-a1-v4.jsonl`) : 1 478 appels numérotés sans trou, du 9 novembre 06:11:32 au **13:19:52 UTC** ; 1 477 « OK » ; **1 échec** : appel 465, 09:26:49 UTC, réponse vide arrêtée à la limite de 32 000 jetons de sortie après 342,6 s, 1,6259 dollar ; la tentative a été rejouée aussitôt (second essai réussi en 32,8 s) et compte comme jouée. Durée médiane d'un appel 11,8 s (moyenne 16,9 s ; plus long appel réussi 442,1 s, à 12:48:37 UTC) ; aucun trou de plus de 120 s entre deux appels ; modèle servi `gemini-4-argon` à chaque appel. Après 13:19:52 UTC la course ne fait plus que des rejeux locaux, jusqu'à 01:33:26 UTC le 10 novembre (durée totale 69 728,7 s, soit 19,4 h ; plafond 72 h).

*Écart d'Argon (R-2013, R-2014, R-2043)* : la mère a appelé Argon 203 fois avec la même clé, du 9 novembre 13:19:58 au 13:55:15 UTC (heures du registre, `registres/decisions.md`, R-2013). Comptes demandés par R-2014 :

| fenêtre (UTC, 9 novembre) | appels d'A1-v4 | échecs | durée médiane | seconds essais |
|---|---|---|---|---|
| heure d'avant, 12:19:58 → 13:19:58 | 202 | 0 | 12,8 s | 0 |
| usage tiers, 13:19:58 → 13:55:15 | **0** | 0 | — | 0 |
| heure d'après, 13:55:15 → 14:55:15 | 0 | 0 | — | 0 |

Le dernier appel d'A1-v4 (appel 1 478, 14,9 s, « OK ») finit à 13:19:52 UTC, six secondes avant le premier appel tiers ; la garde lit 1 478 appels et 114,0434 dollars à 13:20:24 UTC et à chaque relevé suivant. **Aucun appel d'A1-v4 n'a eu lieu pendant l'usage tiers : ni erreur, ni ralentissement, ni second essai à y lire ; aucune perturbation.** Seule nuance : l'écart de six secondes repose sur deux horloges (celle de la machine et celle du conteneur de la mère) ; un décalage de quelques secondes ne ferait chevaucher que les tout derniers appels, tous réussis en 8 à 20 s. L'écart à la condition « Argon seul » reste un écart d'exécution déclaré ; il ne laisse aucune trace dans la mesure. Aucune réserve de perturbation n'est écrite.

## 5. Vérification du monde W2 au nul v9, sur les 24 cartes de la course

Réplique de l'essai `Juges.test_w2_sortant_de_v8_refuse_par_v9` : sur chaque carte, la loi du monde et la loi « si/sinon par sous-population S1, S2 » sont jugées une fois sous v9 avec appariement au v8, et une fois sous le rôle « ancien » (v8). En plus, sans seuil neuf : chacune évaluée 200 fois sous v9 à tirages frais.

| carte | monde : promu sous v9 (apparié) | monde : log W max sous v9 | monde : promu sous v8 apparié | monde : promu sous « ancien » (v8) | monde : 200 évaluations sous v9, promotions ; log W max > 10⁻⁶ | si/sinon : promu sous v9 (apparié) | si/sinon : log W max sous v9 | si/sinon : promu sous v8 apparié | si/sinon : promu sous « ancien » (v8) | si/sinon : 200 évaluations sous v9, promotions ; log W max > 10⁻⁶ |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | non | -3.5e-07 | oui | oui | 0 ; 0 | non | -1.3e-08 | oui | oui | 0 ; 0 |
| 1 | non | -5.0e-09 | oui | oui | 0 ; 0 | non | -2.6e-01 | oui | oui | 0 ; 0 |
| 2 | non | -6.9e-02 | oui | oui | 0 ; 0 | non | -1.6e+00 | oui | oui | 0 ; 0 |
| 3 | non | -5.8e-01 | oui | oui | 0 ; 0 | non | -2.2e-07 | oui | oui | 0 ; 0 |
| 4 | non | -4.1e-01 | oui | oui | 0 ; 0 | non | -2.8e-01 | oui | oui | 0 ; 0 |
| 5 | non | -2.9e-01 | oui | oui | 0 ; 0 | non | -1.3e+00 | oui | oui | 0 ; 0 |
| 6 | non | -6.5e-01 | oui | oui | 0 ; 0 | non | -4.8e-01 | oui | oui | 0 ; 0 |
| 7 | non | -2.6e-08 | oui | oui | 0 ; 0 | non | -2.6e+00 | non | oui | 0 ; 0 |
| 8 | non | -2.3e-01 | oui | oui | 0 ; 0 | non | -1.6e-08 | oui | oui | 0 ; 0 |
| 9 | non | -4.5e-01 | oui | oui | 0 ; 0 | non | -8.2e-03 | oui | oui | 0 ; 0 |
| 10 | non | -8.3e-08 | oui | oui | 0 ; 0 | non | -1.9e-07 | oui | oui | 0 ; 0 |
| 11 | non | -2.0e-09 | oui | oui | 0 ; 0 | non | -1.2e-08 | oui | oui | 0 ; 0 |
| 12 | non | -3.6e-02 | oui | oui | 0 ; 0 | non | -3.3e-08 | oui | oui | 0 ; 0 |
| 13 | non | -8.9e-01 | oui | oui | 0 ; 0 | non | -6.5e-08 | oui | oui | 0 ; 0 |
| 14 | non | -2.6e-08 | oui | oui | 0 ; 0 | non | -1.3e+00 | oui | oui | 0 ; 0 |
| 15 | non | -7.4e-09 | oui | oui | 0 ; 0 | non | -1.8e-08 | oui | oui | 0 ; 0 |
| 16 | non | -8.2e-09 | oui | oui | 0 ; 0 | non | -8.0e-02 | oui | oui | 0 ; 0 |
| 17 | non | -1.7e-07 | oui | oui | 0 ; 0 | non | -1.0e-02 | oui | oui | 0 ; 0 |
| 18 | non | -1.2e-08 | oui | oui | 0 ; 0 | non | -7.1e-09 | oui | oui | 0 ; 0 |
| 19 | non | -3.1e-09 | oui | oui | 0 ; 0 | non | -1.0e+00 | oui | oui | 0 ; 0 |
| 20 | non | -7.4e-02 | oui | oui | 0 ; 0 | non | -3.0e-03 | oui | oui | 0 ; 0 |
| 21 | non | -1.3e-08 | oui | oui | 0 ; 0 | non | -1.9e-09 | oui | oui | 0 ; 0 |
| 22 | non | -1.9e-08 | oui | oui | 0 ; 0 | non | -5.0e-01 | oui | oui | 0 ; 0 |
| 23 | non | -1.0e-07 | oui | oui | 0 ; 0 | non | -6.1e-07 | oui | oui | 0 ; 0 |

**Sous v9 : jamais promues, log W max ≤ 10⁻⁶ partout** — 48 évaluations appariées (plus grand log W max −1,9 × 10⁻⁹) et 9 600 évaluations sans appariement (0 promotion, 0 valeur au-dessus de 10⁻⁶, plus grande −1,8 × 10⁻¹⁰, 0 évaluation impossible). Les deux lois sont couvertes par la forme (`structurellement_couverte`). **Sous v8** : la loi du monde est promue 24 fois sur 24 (apparié) et 24 sur 24 (« ancien ») ; la loi si/sinon 23 sur 24 (apparié ; **carte 7 non promue sur ce tirage**) et 24 sur 24 (« ancien »). Le monde W2 de la course est au nul v9 et hors du v8, comme le texte le veut ; la carte 7 est nommée pour l'unique tirage apparié où le v8 ne promeut pas la loi si/sinon.

## 6. Vérification de W2g hors du nul, sur les 24 cartes de la course (dose 0,40)

Application du § 7 : sur chaque carte, (a) la loi du monde (avec N) et (b) la recombinaison pure S1, S2 (`monde_w2(L)`), chacune évaluée 200 fois sous v9 (200 tirages frais, lecture finale à l'instant 200) ; grandeur lue `log_richesse_finale` ; seuil de (a) : au moins 160 sur 200 au-dessus de 10⁻⁶ ; (b) : jamais. Promotions rapportées en plus, sans seuil.

| carte | écart (nat par instance) | (a) log W final > 10⁻⁶, sur 200 | (a) seuil ≥ 160 | (a) promotions, sur 200 | (a) log W final médian | (b) log W final > 10⁻⁶, sur 200 | (b) promotions, sur 200 | (b) plus grand log W max |
|---|---|---|---|---|---|---|---|---|
| 0 | 0.1079 | 198 | tenu | 195 | 12.58 | 0 | 0 | -1.1e-09 |
| 1 | 0.0480 | 118 | **sous le seuil** | 33 | 0.59 | 0 | 0 | -1.2e-08 |
| 2 | 0.0492 | 197 | tenu | 188 | 9.37 | 0 | 0 | -1.3e-09 |
| 3 | 0.0406 | 149 | **sous le seuil** | 73 | 1.85 | 0 | 0 | -2.7e-09 |
| 4 | 0.1761 | 96 | **sous le seuil** | 6 | -0.13 | 0 | 0 | -1.0e-08 |
| 5 | 0.1078 | 89 | **sous le seuil** | 4 | -0.22 | 0 | 0 | -1.5e-08 |
| 6 | 0.0734 | 194 | tenu | 181 | 8.01 | 0 | 0 | -4.1e-09 |
| 7 | 0.0272 | 160 | tenu | 110 | 2.98 | 0 | 0 | -5.6e-09 |
| 8 | 0.2191 | 199 | tenu | 197 | 13.04 | 0 | 0 | -1.4e-09 |
| 9 | 0.2219 | 195 | tenu | 191 | 8.88 | 0 | 0 | -7.3e-08 |
| 10 | 0.2363 | 199 | tenu | 198 | 16.52 | 0 | 0 | -7.4e-09 |
| 11 | 0.3065 | 199 | tenu | 199 | 15.54 | 0 | 0 | -6.2e-10 |
| 12 | 0.6894 | 199 | tenu | 192 | 9.49 | 0 | 0 | -1.5e-08 |
| 13 | 0.1263 | 200 | tenu | 197 | 15.80 | 0 | 0 | -2.1e-09 |
| 14 | 0.0156 | 154 | **sous le seuil** | 88 | 2.15 | 0 | 0 | -6.7e-10 |
| 15 | 0.1843 | 182 | tenu | 155 | 6.07 | 0 | 0 | -8.4e-08 |
| 16 | 0.2563 | 194 | tenu | 189 | 11.95 | 0 | 0 | -7.9e-09 |
| 17 | 0.2905 | 195 | tenu | 191 | 13.92 | 0 | 0 | -1.2e-08 |
| 18 | 0.2389 | 195 | tenu | 184 | 10.30 | 0 | 0 | -3.5e-09 |
| 19 | 0.1304 | 191 | tenu | 185 | 8.15 | 0 | 0 | -3.6e-09 |
| 20 | 0.3134 | 199 | tenu | 197 | 14.23 | 0 | 0 | -8.0e-08 |
| 21 | 0.0180 | 158 | **sous le seuil** | 106 | 2.74 | 0 | 0 | -1.3e-09 |
| 22 | 0.0253 | 112 | **sous le seuil** | 24 | 0.42 | 0 | 0 | -1.1e-09 |
| 23 | 0.3389 | 194 | tenu | 184 | 10.78 | 0 | 0 | -4.0e-08 |

- **(b), recombinaison pure : 0 sur 200 sur chacune des 24 cartes**, 0 promotion (0 sur 4 800), plus grand log W max −6,2 × 10⁻¹⁰ : le certificat tient ; aucune promotion de (b) à nommer.
- **(a), loi du monde : seuil tenu sur 17 cartes, non tenu sur 7.** Cartes sous le seuil, nommées : **carte 1 (118), carte 3 (149), carte 4 (96), carte 5 (89), carte 14 (154), carte 21 (158), carte 22 (112)**. Sur les cartes 4 et 5, la loi du monde n'est promue que 6 et 4 fois sur 200 et son log W final médian est négatif : à cette dose, la loi neuve n'y est presque pas visible pour le v9.
- Rapporté sans seuil : promotions de (a) **3 467 sur 4 800 (0,722)**, de 4 à 199 sur 200 selon la carte ; log W final positif 4 166 fois sur 4 800 ; écart moyen des 24 cartes 0,1767 nat par instance. Information (texte § 7) : l'épreuve hors ligne donnait 803 promotions sur 1 000 à cartes indépendantes et un écart moyen de 0,173686 (chiffres transcrits du texte scellé, § 4 et § 6.2 ; lecture `dc0bb41a…` non rouverte ici).
- Ce qui en dépend : rien (le texte n'attache aucune issue à ce contrôle). Fait utile à la lecture, sans règle : aucune des 17 lois promues sous v9 en course ne l'a été sur l'une des sept cartes sous le seuil (cartes promues sans retour : 0, 2, 8, 10, 13, 16, 23 ; avec retour : 0, 8, 9, 10, 11, 12, 13, 19, 20, 23).

## 7. Prédictions (rapportées ; elles ne décident pas de l'issue)

| | prédiction | observé | tenue |
|---|---|---|---|
| P1 | taux(v9, retour, 16) ≤ 2/24 et Δ₁₆(v9) dans [−0,10 ; +0,10], sur W2 | 1/24 ; Δ₁₆ = 1/24 − 3/24 = −0,083 | oui |
| P2 | taux(v8, retour, 16) ≥ 12/24, sur W2 | 24/24 | oui |
| P3 | sous v9, taux(16) − taux(1) ≤ 0,10 dans les deux conditions, sur W2 | +0,042 (retour), +0,083 (témoin) | oui |
| P4 | 0 violation de monotonie, sur W2 | 0 | oui |
| P5 | issue « résiste (à cette taille) » sur W2 | « résiste (à cette taille) » | oui |
| P6 | 0/24 sous v9 avec retour à n = 16, sur W2 | 1/24 | **non** |
| P7 | taux(v9, retour, 16) ≥ 12/24, sur W2g | 10/24 | **non** |
| P8 | Δ₁₆(v9) ≥ +0,10, sur W2g | 10/24 − 7/24 = +0,125 | oui |
| P9 | part des lois promues robustes ≥ 0,80, sur W2g | 10/17 = 0,588 | **non** |
| P10 | taux(v8, témoin, 1) ≥ 12/24, sur W2g | 13/24 | oui |
| P11 | 0 violation de monotonie, sur W2g | 0 | oui |

H3, descriptif : sur W2g sous v9 à n = 16, 5 cartes promues avec retour seulement, 2 sans retour seulement (McNemar exact p = 0,45) ; écart par loi −0,020, intervalle [−0,078 ; +0,023], « non tranché » ; sur W2 sous v9 à n = 16, 1 contre 3 (p = 0,625).

## 8. Réserves de l'audit

1. **Course « trop propre » (réserve héritée, texte § 7)** : échos exacts 349/349 et 261/261, part hors classe 0,995 et 0,996, aucune attente sur relais, un seul appel en échec sur 1 478. C'est une réserve, non une preuve. Un échec de chaîne qui toucherait également les deux bras passerait inaperçu, faute de témoin négatif planté (dispense R-1294, maintenue par le texte). Ce que cet audit y oppose : les consignes, les verdicts et l'audit A2 se rejouent à l'identique sur une autre machine, et les deux vérifications des mondes passent par la même chaîne de jugement.
2. **W2 à la limite de la règle** : 1 promotion sur 24 avec retour est le plus grand compte que « résiste » admette ; sans retour, 3 sur 24. Les quatre lois promues se rejouent à 1 à 1,5 % : multiplicité, pas défaut.
3. **W2g : sept cartes sous le seuil du contrôle par carte** (point 6) ; la frontière n'est visible à l'oracle, au sens du seuil, que sur 17 cartes sur 24.
4. **Famille de Holm** : écart de lettre entre le § 5 du texte et le code gelé, sans effet sur l'issue, la qualification ni P9 (A2 ci-dessus).
5. **« λ\* à la limite »** (réserve déclarée du texte, § 6.2) : à la dose 0,40, l'oracle hors ligne n'est promu que 803 fois sur 1 000 (Wilson [0,777 ; 0,827]) ; sur les cartes de la course, 0,722.
6. **Écart d'Argon** : déclaré (R-2013) ; aucune perturbation mesurée, aucun appel d'A1-v4 dans la fenêtre (A9).
7. **Rôles** : le texte (§ 13, point 12) prévoit un audit écrit par un auditeur neuf et un verdict par un lecteur neuf ; la consigne de la mère confie les deux au même lecteur. Déclaré ; à Lazar de dire s'il veut un second lecteur.
8. **Source du code** : arbre extrait d'un clone public posé par la mère, le paquet du dépôt étant mince ; garde tenue par les 79 empreintes du § 11.
9. **Non vérifié ici** : la destruction de la machine 59845811 (aucun `vastai`), la facturation d'Argon et de Vast ; les réponses du proposeur n'ont été lues que par programme (formes des lois, motifs), non une à une.

## 9. Conclusion de l'audit sur les suspensions

- **W2** : issue suspendue par A2 (code) et, selon le texte, par A1 pour toute issue 3. Les deux audits sont écrits ci-dessus et ne trouvent ni défaut du juge, ni défaut d'instrument, ni défaut de chaîne. A3, A5, A6, A7, A8 : non déclenchés. A4 : noté, sans effet.
- **W2g** : seul A4 est déclenché (noté, sans effet) ; l'issue n'est pas suspendue par le code.
- **A9** : non déclenché sur aucun monde ; l'écart d'Argon n'a rien perturbé. Aucune suspension commune aux deux mondes.

Le prononcé appartient au verdict (`verdict-a1-v4-v1.md`, même dossier).
