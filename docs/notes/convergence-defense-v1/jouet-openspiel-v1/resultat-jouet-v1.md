# Résultat du jeu jouet — v1 (écrit après l'exécution)

Rédacteur-chercheur neuf (sous-agent), 1er novembre 2026. Exécution : 09:53 UTC, `jouet_meilleure_reponse_v1.py --iterations 2000 --repetitions 3`, 11 s de processeur ; sortie `sortie-jouet-v1.json` (manifeste : racine 31415926, commit `e125e4f4`, Python 3.13.18, numpy 2.4.6, scipy 1.17.1, OpenSpiel 2.0.2). Essais : `test_jouet_v1.py`, **8 réussis, 0 échoué** (2,0 s). Protocole et prédictions : `protocole-jouet-v1.md`, écrit avant.

Lecture : « expl_os » = exploitabilité d'OpenSpiel (NashConv / 2, moyenne des deux joueurs) ; « expl_D » = exploitabilité du seul défenseur calculée sur la matrice (v* − min_j (pᵀG)_j). Chiffres recopiés du JSON (arrondis à 4 décimales) ; trois répétitions sauf la référence `XFPSolver`, déterministe.

## 1. Sort des prédictions

| # | Prédiction | Observé (répétitions 0 ; 1 ; 2) | Sort |
|---|---|---|---|
| P1 | D1 : dernier itéré du défenseur constant à son maximum | pierre-feuille-ciseaux : expl_D = 1,000 à chaque itération (étendue 0) ; pile ou face biaisé : 1,200 (étendue 0) | **tenue** |
| P2 | D1 : période 3 et 2 | période **3** (paires `3,2,7` répétées) ; période **2** (paires `3,0`) ; les trois répétitions | **tenue** |
| P3 | D2 : expl_os du profil moyen < 0,05 à 2 000, décroissante | pierre-feuille-ciseaux : 0,2143 ; 0,1667 ; 0,2381 (à 20) → 0,0622 ; 0,0622 ; 0,0647 (à 200) → **0,0200 ; 0,0202 ; 0,0205** (à 2 000). Pile ou face biaisé : 0,1429 ; 0,1429 ; 0,1667 → 0,0547 ; 0,0647 ; 0,0597 → **0,0165 ; 0,0177 ; 0,0185** | **tenue** |
| P3′ | `XFPSolver` d'OpenSpiel tel quel < 0,05 à 2 000 | pierre-feuille-ciseaux : 0,1905 (20) → 0,0448 (200) → **0,0140** (2 000) ; pile ou face biaisé : 0,1548 → 0,0597 → **0,0185** | **tenue** |
| P4 | D2 : dernier itéré (pur) constant au maximum | expl_D = 1,000 et 1,200, étendue 0, toutes répétitions | **tenue** |
| P5 | D3 : dernier moniteur déployé constant au maximum | expl_D = 1,000 et 1,200, étendue 0 | **tenue** |
| P6 | D3 : moyenne de l'attaquant → q*, ‖·‖₁ < 0,05 | pierre-feuille-ciseaux : 0,0000 ; 0,0000 ; 0,0000 ; pile ou face biaisé : **0,0004 ; 0,0006 ; 0,0006** (moyenne finale de l'attaquant (0,400 ; 0,600) = q*) | **tenue** |
| P7a | D3, pierre-feuille-ciseaux : expl_D de la moyenne du défenseur < 0,05 | 0,0000 ; 0,0010 ; 0,0005 | **tenue** |
| P7b | D3, pile ou face biaisé : expl_D de la moyenne du défenseur dans [0,35 ; 0,45] (limite dérivée 0,40) | **0,4014 ; 0,4004 ; 0,3984** ; moyenne finale du défenseur (0,600 ; 0,400) contre p* = (0,400 ; 0,600) | **tenue** |

Bilan : 9 prédictions, 9 tenues, 0 réfutée.

## 2. Les deux résultats demandés, en chiffres

1. **La meilleure réponse pure itérée cycle.** Sur pierre-feuille-ciseaux, la suite des paires (défenseur, attaquant) est exactement périodique de période 3 dès la deuxième itération ; sur pile ou face biaisé, de période 2. L'exploitabilité du dernier itéré du défenseur vaut 1,000 (respectivement 1,200) à **chacune** des 2 000 itérations : elle ne décroît jamais, par construction (un coup pur contre sa meilleure réponse perd le maximum). L'exploitabilité d'OpenSpiel du profil pur vaut 1,0 à chaque itération sur pierre-feuille-ciseaux, et alterne entre 1,0 et 1,5 sur pile ou face biaisé.
2. **Le jeu fictif fait décroître l'exploitabilité de la stratégie moyenne vers 0.** Exploitabilité d'OpenSpiel du profil des moyennes empiriques : 0,21 → 0,06 → 0,02 (pierre-feuille-ciseaux) et 0,14 → 0,06 → 0,017 (pile ou face biaisé) aux itérations 20, 200, 2 000 ; `XFPSolver` d'OpenSpiel pris tel quel : 0,014 et 0,0185 à 2 000. Pendant ce temps, le **dernier itéré** du jeu fictif reste à exploitabilité maximale (1,0 et 1,2) : c'est la moyenne qui converge, pas le dernier coup — exactement la distinction entre « ce que le bras A déploie » (le dernier moniteur) et « ce que la théorie dit converger » (la moyenne).

## 3. Le troisième résultat (lecture du bras A : jeu fictif unilatéral)

- Le dernier itéré du défenseur reste à exploitabilité maximale (P5), comme en D1 et D2.
- C'est **la moyenne de l'attaquant** qui converge vers son équilibre q* (P6, ‖·‖₁ ≤ 0,0006 à 2 000) : le joueur qui répond à la moyenne tire l'autre vers son point d'indifférence.
- La **moyenne du défenseur** converge vers l'uniforme sur pierre-feuille-ciseaux (P7a, par symétrie) mais **pas** vers p* sur pile ou face biaisé : elle tend vers (0,60 ; 0,40), de valeur −0,2 contre sa meilleure réponse, soit une exploitabilité 0,40 (P7b), deux fois la valeur du jeu. Conséquence pour l'arène : même la moyenne uniforme des moniteurs de A (un « C1 sur les moniteurs de A ») n'a aucune garantie d'équilibre sous cette dynamique ; la garantie de Robinson vaut pour le jeu fictif des deux côtés, pas pour le jeu fictif unilatéral.
- Aucune période exacte n'est détectée en D3 (paires quasi-périodiques `5,1,6` sur pierre-feuille-ciseaux, `1,2` sur pile ou face biaisé, avec des bégaiements dus aux égalités de la moyenne) : un cycle « au-delà du hasard » sans période stricte, ce qui est la forme que le taux de retours I3 de l'arène mesure (retours vers d'anciennes attaques), et non une période.

## 4. Réserves

- Pierre-feuille-ciseaux est un **témoin faible** à lui seul : par symétrie, même les moyennes de la meilleure réponse pure alternée y convergent vers l'uniforme (expl_os 0,0005 à 2 000 en D1). Sur pile ou face biaisé, les moyennes de D1 convergent vers (1/2, 1/2) ≠ (2/5, 3/5), exploitabilité d'OpenSpiel 0,249 à 2 000, non décroissante (0,19 à 20, 0,24 à 200, 0,25 à 2 000). C'est le second jeu qui sépare « moyenne qui converge parce que le jeu est symétrique » de « moyenne qui converge parce que la dynamique est un jeu fictif ».
- L'exploitabilité d'un seul joueur (expl_D) sous le jeu fictif des deux côtés n'est pas monotone aux points de relevé (pile ou face biaisé, répétition 1 : 0,0012 à 1 000 puis 0,0321 à 2 000) ; la mesure jointe d'OpenSpiel l'est aux points de relevé des six répétitions. Le seuil du protocole portait sur la mesure jointe ; les deux sont rapportées.
- Jeux à deux actions et trois actions, 2 000 itérations, trois graines : aucune vitesse de convergence n'est revendiquée ; aucun résultat ici ne porte sur l'arène ni sur de vrais moniteurs.
- Tous les résultats de théorie cités dans la note de formalisation restent RAPPORTÉ (aucun PDF dans le dépôt) ; le jouet ne les remplace pas, il montre que la mesure retenue les voit.
