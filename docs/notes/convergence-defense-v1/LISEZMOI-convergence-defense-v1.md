# LISEZMOI — convergence de la défense unique lue comme dynamique de meilleure réponse — v1

Rédacteur-chercheur neuf (sous-agent), 1er novembre 2026, 10:01 UTC. Tâche : la formalisation du jeu du pilote « mélange d'équilibre » (brouillon 4) et le jeu jouet OpenSpiel demandés par Lazar (via la question v2 de conv-audit) ; les quatre règles de mise à jour sur l'arène sont confiées à un autre sous-agent. Rien n'est décidé, scellé ni commis ; aucun appel payant, aucun réseau ; rien lu sous `donnees/` hors `donnees/argon-seul-convergence-v1/` (quatre pièces nommées).

## Contenu du dossier (mes fichiers seulement)

| Fichier | Rôle |
|---|---|
| `formalisation-jeu-convergence-v1.md` | la note : (a) le jeu du pilote comme jeu à deux joueurs à somme nulle, ce que `resoudre_jeu` résout ; (b) dynamique de chaque bras (A = jeu fictif unilatéral, B/B′ = oracle double, D) ; (c) exploitabilité, définition et calcul dans l'arène, comparaison avec I1 et I3 ; (d) résultats connus sur les cycles (tous RAPPORTÉ) ; (e) quatre hypothèses testables H-e1 à H-e4 ; (f) condition testable g = v_R − max_i min_j G_ij ≥ m pour rendre Q2 « posable à classe égale ». Longueur : 5 056 mots alphabétiques (5 507 par `wc -w`, qui compte les symboles et les nombres) ; la cible était 3 000 à 5 000 |
| `jouet-openspiel-v1/protocole-jouet-v1.md` | protocole et neuf prédictions chiffrées, écrit **avant** l'exécution (09:51 UTC) |
| `jouet-openspiel-v1/jouet_meilleure_reponse_v1.py` | le script : OpenSpiel 2.0.2 tel quel (`matrix_rps`, `create_matrix_game`, `convert_to_turn_based`, `exploitability`, `XFPSolver`) ; trois dynamiques (meilleure réponse pure alternée ; jeu fictif ; jeu fictif unilatéral = lecture du bras A) ; deux jeux à somme nulle sans équilibre pur ; graines `SeedSequence(entropy=31415926, spawn_key=(jeu, dynamique, répétition))` (R9) ; manifeste dans la sortie |
| `jouet-openspiel-v1/sortie-jouet-v1.json` | sortie (exploitabilités par itération, périodes, distances aux équilibres, manifeste : versions, graines, commit `e125e4f4`) ; 09:53 UTC |
| `jouet-openspiel-v1/resultat-jouet-v1.md` | sort des neuf prédictions (9 tenues), chiffres, réserves ; écrit **après** |
| `jouet-openspiel-v1/test_jouet_v1.py` | 8 essais pytest : cycle détecté (périodes 3 et 2, exploitabilité du dernier itéré constante), décroissance du jeu fictif (< 0,05 à 2 000, décroissante), `XFPSolver` tel quel, graine reproductible, identité « exploitabilité OpenSpiel = (expl_D + expl_A)/2 », détecteur de période sain et sur un cas sans période. Lancés : `/home/user/controle-ia-travail/.venv/bin/python -m pytest -q -p no:cacheprovider` sur le dossier : **8 réussis, 0 échoué** (2,0 s) |

Les sous-dossiers `argon-seul-convergence-v1/` et `regles-defense-v1/` présents dans ce même dossier **ne sont pas de moi** (autre sous-agent ou session, apparus pendant mon travail) ; je ne les ai ni lus ni touchés, et leurs empreintes ne figurent pas ici.

## Ce qui est fait

- Lecture entière des quatre pièces ; vérification sur le code que le bras A déploie le dernier moniteur linéaire **entraîné contre le mélange uniforme de toutes les attaques passées, cible comprise** (`trajectoire`, l. 1073–1075 et 1106–1107 ; brouillon 4 l. 348 ; docstring l. 40–41) : la phrase de la question v2 (« contre la dernière attaque ») est fausse, le fait établi par session-depot est confirmé. Lecture retenue : **jeu fictif unilatéral** côté défenseur, meilleure réponse pure côté attaquant.
- Jeu écrit (joueurs, espaces purs et mixtes, gain = taux de détection à α, somme nulle parce que fausses alertes et distance sont des contraintes et non des termes du gain) ; `resoudre_jeu` = équilibre du jeu matriciel restreint aux moniteurs et attaques passés (valeur v_R, borne haute de la garantie réelle du p rendu, jamais une borne de v*).
- Exploitabilité définie : expl_D(σ_D) = v* − inf_θ Det(σ_D, θ) ; dans l'arène, (iii) = V en est l'estimation à v* près et par en dessous (optimiseur local) ; I1 = −(variation de l'exploitabilité du dernier itéré) ; I3 mesure la récurrence de l'attaquant, pas l'exploitabilité ; seul le côté défenseur est estimable (pas d'oracle exact pour la borne haute) ; mesure manquante : V de la moyenne uniforme des moniteurs de A (une `meilleure_reponse` par tâche).
- Jouet exécuté : meilleure réponse pure alternée à exploitabilité 1,000 (pierre-feuille-ciseaux) et 1,200 (pile ou face biaisé) à chaque itération, périodes 3 et 2 ; jeu fictif : exploitabilité OpenSpiel des moyennes 0,020 et 0,017 à 2 000 (`XFPSolver` : 0,014 et 0,0185), dernier itéré constant au maximum ; jeu fictif unilatéral : dernier itéré constant au maximum, moyenne de l'attaquant à ≤ 0,0006 de q*, moyenne du défenseur à exploitabilité 0,40 sur le second jeu (dérivé avant, observé après) et 0 sur pierre-feuille-ciseaux (symétrie).

## Ce qui reste

1. **Les quatre règles de mise à jour** sur l'arène (autre sous-agent) ; cette note leur fournit la mesure (expl_D relative = V_réf − V, et V de la moyenne) et la lecture de A.
2. **Les tests de H-e1 à H-e4** sur le JSON du pilote v4 (H-e1 et H-e2 (1)–(2) sans aucune exécution, sur la matrice H et le jeu restreint des moniteurs de A ; H-e2 (3), H-e3, H-e4 (2) : une meilleure réponse par tâche, racine d'essai, jamais de racine de décision) ; à écrire dans un préenregistrement court (R1, R2) si Lazar veut en faire une lecture opposable.
3. **La condition g ≥ m** (§ 6) calculée sur les matrices G finales de B et B′ du pilote v4 : dit, avant toute comparaison, à quelle classe Q2 est posable ; candidate pour le brouillon 5.
4. **Le préenregistrement** de toute mesure décisive (aucune ici) ; ce dossier n'est pas un préenregistrement.
5. **La revue sur PDF** (R7) : aucun des résultats de théorie des jeux cités (Brown 1951, Robinson 1951, Shapley 1964, Miyasawa 1961, Monderer et Shapley 1996, Freund et Schapire 1999, McMahan et collègues 2003, Lanctot et collègues 2017 et 2019, Daskalakis et Pan 2014, Mertikopoulos et collègues 2018, Bailey et Piliouras 2018, Daskalakis et collègues 2018, Daskalakis et Panageas 2019, Fudenberg et Levine 1998) n'est dans `docs/sources/pdf/` (163 PDF, vérifiés par le titre) ; tous restent RAPPORTÉ. Cinq PDF voisins présents, non relus : `2412.09565v2`, `2601.19726v1`, `2602.01539v2`, `2511.00554v1`, `2605.15377v2`.
6. Empreintes compagnons `.sha256` (R6) : non écrites par moi (aucun scellement) ; le bloc ci-dessous permet `sha256sum -c`.
7. Correction de la question v2 (§ constat : « contre la dernière attaque ») par conv-audit.

## Empreintes sha256 (recalculées par `sha256sum`, 10:01 UTC, dans ce dossier)

```
a277a5ba28e36c4a4042ef0905510ec9e1772954a5fe29dbd1a4eb7f49d92a77  formalisation-jeu-convergence-v1.md
964c60ae5fecb8adcfe1459a425fe47f5ff9cb3d013afb0584ebebd0b9126e70  jouet-openspiel-v1/jouet_meilleure_reponse_v1.py
ad775f75d89d15097d9f6baf34b599f78414ada0a1af0aa0207016def5580f96  jouet-openspiel-v1/protocole-jouet-v1.md
1c76fc69fcda567f8e27c5503beb6556377d083c1c3627de7c4ff9ca3a3ee013  jouet-openspiel-v1/resultat-jouet-v1.md
75f13d2ec0ea46dabf4dd5e66cf0a89f3159892b79960d8e0f1dfecdfaadb5fb  jouet-openspiel-v1/sortie-jouet-v1.json
80267030662caa6382b5f745d06d7424bc25b18631f60fbb1b1863562ae6ccd5  jouet-openspiel-v1/test_jouet_v1.py
```

Pièces lues (empreintes de la vérification du brouillon 4, non recalculées par moi sauf la question v2) : brouillon 4 `305911b7ab19…` ; `arene_melange_v4.py` `70c77fd5c0ec…` ; question v2 `08f2b01724ea08005f647e5a6b666aa064b8ba539829f3464f9999113a3feda0` (recalculée) ; vérification du brouillon 4 `28ab322f9d2e…` (recalculée, sans compagnon dans le dossier lu). Les empreintes du brouillon 4 et du code ont été recalculées et concordent avec celles citées.
