# LISEZMOI — quatre règles de mise à jour de la défense dans l'arène v4 — v1

Sous-agent neuf (développeur-chercheur, Fable 5.1), 1er novembre 2026, 09:52 → 10:10 UTC. Demande du directeur : comparer dans le jeu synthétique quatre règles de mise à jour de la défense (dernière attaque ; historique ; mélange d'équilibre des deux côtés ; régularisation vers le passé) sur exploitabilité, détection sur attaques tenues à l'écart et coût, à classe de fonctions égale, et préenregistrer. Ma part : **code et essais, pilote d'essai sur racines d'essai, brouillon de préenregistrement** — pas la course décisive (préenregistrement scellé et contre-lu, R1 et R2, et mot du directeur exigés). Rien décidé, rien scellé, rien commité, aucun appel payant ni réseau ; rien lu sous `donnees/` hors `argon-seul-convergence-v1/` ; `arene_melange_v4.py` jamais modifié (empreinte vérifiée au chargement : `70c77fd5…`).

## Contenu du dossier (empreintes sha256 recalculées à 10:09 UTC)

| Fichier | Rôle | sha256 |
|---|---|---|
| `gel-regles-defense-v1.md` | gel écrit **avant** toute exécution : racines neuves (plage 20266001–20266999), définitions des règles, grille de λ et règle de choix, taille du pilote ; empreinte épinglée dans le code | `4fbb12dc941479f59504d9c3dc8246bf88c474a40c387bea40ac2e24c4ef0890` |
| `arene_regles_defense_v1.py` | module : charge le v4 par chemin (empreinte vérifiée, aucun `.pyc` écrit sous `donnees/`), remplace `gen` dans la copie chargée (dérivation propre, même schéma `SeedSequence`), étend `BRAS` des codes des règles, compte `minimize` et `linprog` ; boucle commune des quatre règles ; finale du v4 ; analyse (contrastes appariés contre R2, rééchantillonnage, choix de λ*) ; commandes `essai`, `identite`, `decision` (préenregistrement scellé exigé), `orphelins` | `337c569bd90d5b8964a4e6b7491c0c5a67042d54333401b65540e889a15a2c97` |
| `test_arene_regles_defense_v1.py` | 19 essais pytest (11,7 s), tous passés : gardes sur cas sain et artefact (R5), **R2 = A du v4 au bit** (essai clé), R3 = B au bit, R4(λ = 0) = R2 à entrée égale et à code de graine égal, exploitabilité dans [0 ; 1], tenues jamais vues par l'entraînement (instrumentation), graine reproductible et autre racine différente, plafond de temps, analyse et règle de choix de λ, commande, identité du préenregistrement | `8a03f1f813ed31011d79ad48b0153a98d9a76c7837caad4b6c976850a857d941` |
| `pilote-essai-regles-defense-v1.json` | pilote d'essai, racines 20266101 / 20266102, 6 instances × 2 δ, T = 8, 13 variantes (R1, R2, R3, R4 × 5 λ × 2 références), configuration `CONFIG_V4` inchangée ; manifeste, temps, analyse, résultats | `dcd24d31155bf04a45c672a4eef5ef102deaec581f0733be76b23247d6eaddec` |
| `pilote-essai-regles-defense-v1.md` | résumé mécanique du pilote (temps, extrapolation, mesures par variante et par tour, contrastes, choix de λ*) — **à ne pas lire comme un résultat** | `b9f2bb078698f42a3e0bab98201f3b69666ee249cce484e8a2de2b107a640356` |
| `resumer-pilote-essai-regles-defense-v1.py` | script qui produit le `.md` à partir du `.json` | `9974647250307d36443eb0b8a08a80c674bacb5a0b32d1db2ee135314c12bce6` |
| `brouillon-prereg-regles-defense-v1.md` | brouillon 1 de préenregistrement au gabarit du dépôt (bloc d'identité vérifié par le code ; hypothèses HR1 à HR6 ; prédictions P1 à P11 avec signes ; métriques ; seuils S1 à S13 avec recommandations ; plan d'analyse ; Tables A à E gelées ; liste d'arrêt ; rôles) ; marqueurs « [DÉCISION DE LAZAR] » (5) et champs à remplir | `be08f4385dba0642ec857c96c67cc11c2d2acd09da026533d942fd7c87f1a48c` |
| `journal-pilote-essai-regles-defense-v1.log` | sortie de la commande du pilote | `433b630a577801ca6880b055f731abf56f4c719f2747cb5017860969f84b15cb` |
| `pids-pilote-essai-regles-defense-v1.txt` | PID et instants de départ des deux processus de travail (R10) ; `orphelins` rend « aucun processus de travail consigné ne tourne » | `1b1ca5ab99e0cd7ae71063aafa81b5990e9e2a8601f2692651f416637dd93475` |

Lancement : `cd docs/notes/convergence-defense-v1/regles-defense-v1 && PYTHONPATH=/home/user/controle-ia-travail/src OMP_NUM_THREADS=1 python -B -m pytest -q test_arene_regles_defense_v1.py` ; pilote : `… python -B arene_regles_defense_v1.py essai --instances 0:6 --sortie … --processus 2 --pids …`.

## Ce que fait chaque règle (gel § 2)

- **R1 « dernière attaque »** : moniteur linéaire réentraîné (oracle « détection » du v4) contre la seule attaque du tour ; seul déployé ; code de graine 21.
- **R2 « historique »** : bras A du v4 réemployé par la boucle commune (mélange uniforme de toutes les attaques passées) ; code 1 ; identique au bit à A (attaques, moniteurs, (iii), (ii), H, finale).
- **R3 « mélange d'équilibre des deux côtés »** : bras B du v4 (double oracle : moniteurs passés aux poids d'équilibre p, oracle du défenseur contre la stratégie d'équilibre q de l'attaquant) ; code 2 ; identique au bit à B. **R3′** : la valeur du jeu restreint (les deux joueurs à l'équilibre) est rapportée à chaque tour et en finale sur la même trajectoire ; une trajectoire distincte où l'attaquant déploierait son mélange n'ajouterait aucune stratégie au double oracle (ce qui manque pour une vraie variante : un autre oracle, par exemple le défenseur répondant à la meilleure réponse pure plutôt qu'à q — non demandé, non construit).
- **R4 « régularisation vers le passé »** : historique plus pénalité **sans échelle** 2λ(1 − cos(w, u)) = λ‖w/‖w‖ − u‖² (l'objectif de détection du v4 est invariant par changement d'échelle du moniteur linéaire : une pénalité ‖w − w_{t−1}‖² brute dépendrait d'une norme arbitraire) ; u = direction du moniteur déployé (« dernier ») ou moyenne des directions passées (« moyenne » : poids de moniteurs, pas de jetons) ; biais non pénalisé ; code 24 ; à λ = 0, mise à jour identique au bit à celle de R2.

Mesures par règle et par tour : (iii)_t, exploitabilité X_t = 1 − (iii)_t (valeur absolue), (ii)_t sur les 50 lois tenues (racine à part, jamais vues par aucune mise à jour), cosinus entre moniteurs consécutifs (dégénérescence), valeur du jeu restreint (R3) ; en finale : V (min des réponses standard et renforcée), X = 1 − V, (ii), (i), fausses alertes ; I1, I2, I3 − 0,7345 et H par les fonctions du v4 ; coût : processeur, appels à l'optimiseur, programmes linéaires, entraînements, départs de l'attaquant, paramètres.

## Pilote d'essai (racine d'essai ; aucune lecture de résultat)

- 12 tâches, 13 variantes : 490 s de processeur, 253 s de mur sur 2 processus (efficacité 0,97), 40,9 s par tâche (max 47,4 s ; plafond 600 s) ; 0 entraînement non convergé sur 1 272, 0 départ non fini sur 19 812, fausses alertes dans α ± 0,0005 en moyenne ; les mesures bougent entre règles et entre tours.
- Extrapolation à N = 100 par δ (200 tâches) : décision à 4 variantes (R1, R2, R3, R4 à λ*) ≈ 15 s par tâche → ≈ 50 min de processeur, ≈ 26 min de mur sur 2 processus (≈ 13 min sur 4) ; grille complète (13 variantes) ≈ 41 s par tâche → ≈ 136 min de processeur, ≈ 70 min de mur sur 2 processus.
- Règle de choix du gel § 3 : **λ* = 0,3, référence « moyenne »** (cosinus consécutif moyen 0,958 et 0,943 : non dégénéré) ; recopié dans le brouillon (LAMBDA_RETENU, REFERENCE_RETENUE, vérifiés par le code).

## Réglages à geler (brouillon, S1 à S13)

m = 0,02 ; N = 100 par δ ; T = 8 ; δ = (1,4 ; 1,6) ; α = 0,01 ; λ* = 0,3 et référence « moyenne » (S6, décision de Lazar : la règle peut retenir l'extrémité « défense figée » ; options a, b, c dont un témoin R0 « défense figée ») ; seuil de dégénérescence de R4 (S12, cosinus ≥ 0,999) ; Bonferroni par famille (B2, B8, E8) ; `timeout` (S8) ; variantes de la décision (4 ou grille complète) ; ordre avec la course du v4.

## Ce qui reste (hors de ma part)

1. **Contre-lecture (R2)** du brouillon par un sous-agent neuf (fichiers listés dans le brouillon § Rôles), puis gel des seuils et des marqueurs par Lazar, puis scellement (`controle_ia.prereg.sceller_prereg`), puis GO ; la commande `decision` du module refuse de partir sans cela (essai `test_decision_refusee_sans_prereg_scelle`).
2. **Calcul de puissance** (S3) : non fait ; option : simulation à la manière de (M4) du v4 sur le pilote d'essai, racine réservée 20266401.
3. **Attaquant indépendant** du v4 non branché sur les règles nouvelles (audit S17 du v4 : code v2 si Lazar le veut).
4. **Témoin R0 « défense figée »** : non implanté (hors gel v1) ; proposé dans le brouillon (S6, option c).
5. Commit, empreintes compagnons `.sha256`, passation : par la session principale (je ne commets ni ne scelle).
6. Note sur la petite configuration des essais : la garde de fausses alertes du v4 (α ± 0,005) exige les 20 000 points de calibration ; les autres effectifs sont réduits (T = 3, 999 échantillons, 4 lois tenues).
7. Le `__pycache__` créé par pytest dans ce dossier a été retiré ; aucun fichier écrit sous `donnees/`.
