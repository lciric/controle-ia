# Protocole du jeu jouet — meilleure réponse itérée, jeu fictif, jeu fictif unilatéral — v1

Rédacteur-chercheur neuf (sous-agent), 1er novembre 2026, 09:51 UTC (relevé `date -u`), écrit **avant** toute exécution du script `jouet_meilleure_reponse_v1.py` à 2 000 itérations. Seuls des essais de l'interface d'OpenSpiel (3 itérations de `XFPSolver`, exploitabilité d'une politique uniforme et d'une politique pure sur `matrix_rps`) ont été faits avant ce texte ; aucune trajectoire n'a été lue. Ce protocole n'est pas un préenregistrement du programme (rien n'est scellé, aucune porte) ; c'est le témoin demandé par le point 4 de la question v2 de conv-audit : vérifier qu'une bibliothèque publique prise telle quelle voit le cycle de la meilleure réponse et la convergence du jeu fictif.

## Outils, tels quels

- OpenSpiel 2.0.2 (`pyspiel`, `open_spiel.python.algorithms.exploitability`, `open_spiel.python.algorithms.fictitious_play`), numpy 2.4.6, scipy 1.17.1, Python 3.13.18, environnement `/home/user/controle-ia-travail/.venv`.
- Les jeux matriciels sont convertis en jeux tour par tour (`pyspiel.convert_to_turn_based`) parce que `exploitability.exploitability` n'accepte que des jeux séquentiels à somme nulle ; la conversion ne change ni les stratégies ni les gains (l'information du premier coup est cachée au second joueur).
- `exploitability.exploitability(jeu, politique)` d'OpenSpiel rend NashConv / 2, c'est-à-dire la moyenne, sur les deux joueurs, du gain que chacun obtiendrait en passant à sa meilleure réponse contre l'autre. Le script calcule aussi, sur la matrice, l'exploitabilité **de chaque joueur séparément** : pour le défenseur (lignes, qui maximise), expl_D(p) = v* − min_j (pᵀG)_j ; pour l'attaquant (colonnes, qui minimise), expl_A(q) = max_i (Gq)_i − v*, avec v* la valeur du jeu obtenue par programme linéaire. L'identité « OpenSpiel = (expl_D + expl_A)/2 » est vérifiée par un essai.

## Jeux

1. **Pierre-feuille-ciseaux** `matrix_rps` d'OpenSpiel : valeur v* = 0, unique équilibre (1/3, 1/3, 1/3) des deux côtés, aucun équilibre pur.
2. **Pile ou face biaisé** (jeu à somme nulle 2 × 2 créé par `pyspiel.create_matrix_game`, gains du joueur ligne [[2, −1], [−1, 1]]) : aucun point-selle pur (maximin pur −1 < minimax pur 1) ; équilibre unique p* = (2/5, 3/5), q* = (2/5, 3/5), valeur v* = 1/5. Choisi parce que sa valeur n'est pas nulle et que l'équilibre n'est pas uniforme : une convergence « par symétrie » n'y suffit pas.

Convention : le joueur ligne est le **défenseur** (il maximise le gain), le joueur colonne l'**attaquant** (il minimise), comme dans `resoudre_jeu` de l'arène (lignes = moniteurs, colonnes = attaques).

## Dynamiques

Chaque dynamique part d'une paire d'actions pures tirée au hasard et s'exécute 2 000 itérations ; les égalités de meilleure réponse sont départagées au hasard (graine dérivée). Trois répétitions (graines dérivées) par jeu et par dynamique.

- **D1, meilleure réponse pure alternée** : à chaque itération, l'attaquant répond au dernier coup pur du défenseur, puis le défenseur répond au dernier coup pur de l'attaquant. Relevé : exploitabilité du dernier itéré du défenseur à chaque itération ; exploitabilité OpenSpiel du profil pur ; période de la suite des paires (plus petit P tel que la suite soit P-périodique sur sa seconde moitié).
- **D2, jeu fictif** (Brown 1951) : chaque joueur répond à la **moyenne empirique** des coups passés de l'autre (mise à jour simultanée). Relevé : exploitabilité OpenSpiel du profil des stratégies moyennes, et expl_D de la moyenne du défenseur, aux itérations 1 à 2 000 ; exploitabilité du dernier itéré (pur). Référence prise telle quelle : `fictitious_play.XFPSolver` d'OpenSpiel sur le même jeu, exploitabilité de `average_policy()` aux mêmes points de relevé.
- **D3, jeu fictif unilatéral** (lecture du bras A du pilote, brouillon 4 § Plan 2 : « déploie le dernier moniteur, entraîné contre le mélange uniforme de toutes les attaques passées ») : le défenseur répond à la moyenne empirique des coups passés de l'attaquant ; l'attaquant répond au **dernier** coup pur du défenseur. Relevé : expl_D du dernier itéré du défenseur ; expl_D de la **moyenne** des coups du défenseur ; distance L1 de la moyenne empirique de l'attaquant à q* ; période de la suite des paires.

Graines (R9) : `numpy.random.SeedSequence(entropy=31415926, spawn_key=(code_jeu, code_dynamique, repetition))` ; la racine 31415926 est hors de toute plage employée ou refusée par l'arène (20261xxx à 20269xxx) ; manifeste (versions, graines, commit) dans le JSON de sortie.

## Prédictions (signes et seuils), avant exécution

| # | Dynamique, jeu | Prédiction | Seuil | Confiance |
|---|---|---|---|---|
| P1 | D1, les deux jeux | l'exploitabilité du dernier itéré du défenseur **ne décroît pas** : constante et égale à son maximum sur les stratégies pures | étendue (max − min) sur les 2 000 itérations ≤ 10⁻⁹ ; valeur = 1 (pierre-feuille-ciseaux) ; valeur = 1,2 (pile ou face biaisé : v* − (−1)) | 0,95 |
| P2 | D1, période | la suite des paires est périodique | période 3 (pierre-feuille-ciseaux), période 2 (pile ou face biaisé), détectée dans les trois répétitions | 0,9 |
| P3 | D2, moyennes | l'exploitabilité OpenSpiel du profil moyen **décroît vers 0** | < 0,05 à 2 000 itérations dans les deux jeux et les trois répétitions ; valeur à 2 000 < valeur à 200 < valeur à 20 | 0,9 |
| P3′ | D2, référence OpenSpiel | `XFPSolver.average_policy()` donne la même conclusion | exploitabilité < 0,05 à 2 000 itérations | 0,9 |
| P4 | D2, dernier itéré | l'exploitabilité du dernier itéré (pur) du jeu fictif ne décroît pas | étendue ≤ 10⁻⁹ ; valeur = 1 et 1,2 comme en P1 | 0,9 |
| P5 | D3, dernier itéré | comme P1 : le dernier moniteur « déployé » reste à exploitabilité maximale | étendue ≤ 10⁻⁹ ; valeur 1 et 1,2 | 0,9 |
| P6 | D3, moyenne de l'attaquant | la moyenne empirique des coups de l'attaquant converge vers q* (c'est l'adversaire du joueur fictif qui est tiré vers l'indifférence) | ‖q̄ − q*‖₁ < 0,05 à 2 000 itérations, les deux jeux | 0,8 |
| P7a | D3, moyenne du défenseur, pierre-feuille-ciseaux | la moyenne des coups du défenseur converge vers l'uniforme | expl_D(moyenne) < 0,05 à 2 000 | 0,7 |
| P7b | D3, moyenne du défenseur, pile ou face biaisé | la moyenne des coups du défenseur **ne converge pas** vers p* : elle tend vers (3/5, 2/5) (le défenseur joue H exactement quand l'attaquant joue T, et la fréquence de T tend vers 3/5) | expl_D(moyenne) à 2 000 dans [0,35 ; 0,45] (valeur limite calculée : v* − min(2·0,6 − 0,4 ; −0,6 + 0,4) = 0,2 + 0,2 = 0,4) | 0,7 |

Dérivation de P6 et P7b (pile ou face biaisé) : l'attaquant répond à la dernière ligne pure ; contre H il joue T, contre T il joue H. Le défenseur répond à la fréquence q_t de H chez l'attaquant : H si 3q_t − 1 > 1 − 2q_t, c'est-à-dire q_t > 2/5, T sinon. Si q_t > 2/5 le défenseur joue H, l'attaquant T, et q_t baisse ; sinon q_t monte : q_t oscille autour de 2/5 et converge (pas en 1/t). La fréquence de H chez le défenseur égale la fréquence de T chez l'attaquant, qui tend vers 3/5 ≠ p*(H) = 2/5. Pour pierre-feuille-ciseaux, le même argument donne un cycle d'ordre 3 des deux côtés et des moyennes uniformes.

## Ce qui réfuterait

- P1, P4, P5 réfutées si l'exploitabilité du dernier itéré décroît d'au moins 0,01 sur les 2 000 itérations dans une répétition.
- P2 réfutée si aucune période n'est détectée, ou si elle diffère de 3 et 2.
- P3 réfutée si l'exploitabilité du profil moyen à 2 000 dépasse 0,05 dans une répétition, ou si elle n'est pas plus petite à 2 000 qu'à 20.
- P6, P7 réfutées hors des bandes écrites. Une réfutation de P7b (moyenne du défenseur à exploitabilité < 0,05) contredirait la dérivation ci-dessus et serait rapportée telle quelle.

## Sorties

`sortie-jouet-v1.json` (par jeu, dynamique, répétition : exploitabilités par itération, période détectée, distances aux équilibres, manifeste) ; `resultat-jouet-v1.md` écrit après ; essais `test_jouet_v1.py` (cycle détecté, décroissance vérifiée, graine reproductible, identité des deux exploitabilités).
