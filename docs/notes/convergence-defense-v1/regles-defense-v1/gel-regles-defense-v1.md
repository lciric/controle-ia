# Gel — quatre règles de mise à jour de la défense dans l'arène v4 — v1 (écrit AVANT toute exécution)

- Auteur : sous-agent neuf (développeur-chercheur, modèle Fable 5.1), 1er novembre 2026, 09:52 UTC (relevé `date -u`).
- Objet : comparer, dans le jeu synthétique de l'arène `arene_melange_v4.py` (empreinte `70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61`, dossier `donnees/argon-seul-convergence-v1/`), quatre règles de mise à jour du défenseur, chacune à trajectoire propre, l'attaquant jouant en dernier par meilleure réponse au moniteur déployé. Aucun modèle de langage, aucun texte : « l'attaquant » est un choix de paramètres d'une loi (mélange gaussien).
- Chaîne : ce gel → module `arene_regles_defense_v1.py` (qui épingle l'empreinte de ce gel et refuse de partir sans lui) → essais → pilote d'essai → brouillon de préenregistrement. Le fichier `arene_melange_v4.py` n'est jamais modifié (R12) : il est chargé par chemin, son empreinte vérifiée, et deux de ses noms sont remplacés **dans la copie chargée en mémoire seulement** : `gen` (dérivation des graines, voir § 1) et le dictionnaire `BRAS` (étendu des codes des règles nouvelles, § 2).

## 1. Racines (R9) — toutes neuves, plage 20266001 à 20266999, aucune encore employée

Le `gen` du v4 refuse toute racine hors de ses listes gelées (plage 20264001 à 20264999) ; une racine neuve exige donc une dérivation propre, écrite dans le module (même schéma : `SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, role, …))`, numpy ≥ 1.25), qui refuse tout ce que le v4 refuse (racines déjà employées, plage 20265001 à 20265999, racines de décision du v4 20261201 et 20261202, racines gelées du v4 elles-mêmes, pour ne pas les consommer) et toute racine absente de ce gel.

| Racine | Rôle | Emploi |
|---|---|---|
| 20266101 / 20266102 | pilote d'essai (principale / familles tenues à l'écart) | pilote d'essai de ce dossier |
| 20266201 / 20266202 | **décision** (principale / tenues) | **réservées, jamais employées** : refusées par le module sans autorisation par préenregistrement scellé, conforme et identifié (`PREREG-REGLES-DEFENSE-V1`) |
| 20266301 / 20266302 | essais du code (pytest) | essais |
| 20266303 | essais : « une autre racine change le résultat » | essais |
| 20266401 | simulations (calcul de puissance éventuel) | réservée |

Racine des familles tenues à l'écart toujours distincte de la racine principale (garde).

## 2. Règles (chacune à trajectoire propre sur T tours, moniteur commun M0 au tour 0 entraîné contre la loi cible)

À chaque tour t = 1 … T : l'attaquant calcule une meilleure réponse (SLSQP, départs du v4, départ supplémentaire = attaque précédente) contre la défense déployée ; la défense se met à jour selon la règle.

| Code | Règle | Mise à jour du défenseur | Code de graine (`code_bras`) |
|---|---|---|---|
| R1 | « dernière attaque » (protocole de Bailey transposé : réentraîner contre la seule dernière attaque) | moniteur linéaire réentraîné (oracle « détection » du v4) contre la **seule attaque du tour t** ; seul déployé | 21 |
| R2 | « historique » | = bras A du v4 : moniteur linéaire réentraîné contre le mélange **uniforme de toutes les attaques passées** ; seul déployé. Même code de graine que A : la trajectoire doit être **identique au bit** à celle de A (essai clé) | 1 |
| R3 | « mélange d'équilibre des deux côtés » | = bras B du v4 (double oracle tronqué) : moniteurs passés tirés selon les poids d'équilibre p du jeu restreint ; oracle du défenseur entraîné contre la stratégie d'équilibre q de l'attaquant. Même code de graine que B : identique au bit à B (essai). **Lecture « attaquant à l'équilibre » (R3′)** : sur la même trajectoire, la valeur du jeu restreint à chaque tour (les deux joueurs à l'équilibre du jeu restreint) est rapportée à côté de l'exploitabilité (meilleure réponse pure). Une trajectoire distincte où l'attaquant déploierait son mélange n'ajouterait rien au double oracle (aucune stratégie nouvelle n'entrerait) : non construite, déclaré | 2 |
| R4 | « régularisation vers le passé » | moniteur linéaire réentraîné contre le mélange uniforme de l'historique (comme R2), objectif de détection du v4 **plus** une pénalité quadratique **sans échelle** λ‖w/‖w‖ − u‖² = 2λ(1 − cos(w, u)), u = direction de référence : « dernier » = poids du moniteur déployé au tour t ; « moyenne » = moyenne des directions unitaires des moniteurs passés (poids de moniteurs, pas de jetons). Le biais n'est pas pénalisé (il disparaît de l'objectif de détection linéaire). À λ = 0, R4 = R2 au bit (essai) | 24 |

Justification de la pénalité sans échelle : l'objectif de détection du v4 est invariant par changement d'échelle de (w, b) pour un moniteur linéaire ; une pénalité ‖w − w_{t−1}‖² brute dépendrait de la norme arbitraire rendue par l'optimiseur. Les départs de l'entraînement, le nombre d'itérations et la calibration du seuil sont ceux du v4.

## 3. Réglages de R4 à geler : grille et règle de choix (écrites avant le pilote)

- Grille de λ : **{0,03 ; 0,1 ; 0,3 ; 1 ; 3}** (l'objectif de détection est dans [0 ; 1], la pénalité dans [0 ; 4λ] : la grille va de « presque R2 » à « presque figé sur M0 »). Référence par défaut : « dernier » ; « moyenne » rapportée sur la même grille si le temps le permet (pilote : les deux références).
- Règle de choix sur racine d'essai (à recopier dans le préenregistrement) : λ* = valeur de la grille qui **maximise la moyenne, sur les tâches du pilote d'essai (les deux δ confondus), de la détection finale V(R4, λ) contre la meilleure réponse** (la plus basse des réponses standard et renforcée, comme (iii) du v4) ; en cas d'égalité à 0,005 près, la plus petite λ. La référence (« dernier » ou « moyenne ») est choisie par la même règle. λ* et la référence sont gelés avant la course décisive, qui ne lit que λ*.
- Le pilote d'essai ne fixe aucune prédiction chiffrée pour la décision : il calibre la durée, vérifie que les mesures bougent et choisit λ*.

## 4. Mesures (par règle, par tâche = (δ, instance), par tour puis en finale)

- **Exploitabilité** : X_t = 1 − (iii)_t, (iii)_t = taux de détection de la meilleure réponse de l'attaquant au tour t contre la défense déployée, sur un échantillon frais (19 998 points) ; X_fin = 1 − V, V = la plus basse des détections des réponses standard et renforcée contre la défense finale figée (métrique (iii) du v4). Valeur absolue (dans [0 ; 1], garde) ; les contrastes appariés R_k − R2 sont calculés à l'analyse.
- **Détection sur attaques tenues à l'écart** : (ii)_t = moyenne, sur les 50 lois tenues de la tâche (racine tenue à part, jamais vues par aucune mise à jour), du taux de détection de la défense déployée au tour t ; (ii)_fin sur la défense finale ; deux sous-familles rapportées.
- **I1** (progrès : moyenne de (iii) sur la seconde moitié des tours moins la première) et **I3** (retours, lu contre sa valeur nulle 0,7345 à T = 8), I2 et la matrice H recopiés : fonctions du v4 inchangées.
- **Coût** : temps processeur de la trajectoire et de la finale ; nombre d'entraînements ; nombre d'appels à l'optimiseur (`scipy.optimize.minimize`, compté par un compteur posé sur la copie chargée du v4), nombre de programmes linéaires (`linprog`), nombre de départs de l'attaquant.
- Contrôles du v4 : fausses alertes de la défense finale (α ± 0,005), convergence des entraînements (S18 = 0,10), départs non finis, plafond de temps processeur par tâche.

## 5. Pilote d'essai (racines 20266101 / 20266102)

- Instances 0 à 5 (6) × 2 δ (1,4 ; 1,6, `DELTAS_V4`) × règles R1, R2, R3, R4 (grille de 5 λ × 2 références) ; T = 8 ; configuration `CONFIG_V4` du v4 inchangée (empreinte dans le manifeste) ; finale « légère » du v4 (réponses standard et renforcée, fausses alertes) plus (ii) finale et (i) sur les attaques vues ; pas de courbe de contournement (hors objet).
- Deux processus de travail, PID consignés, arrêt par PID (R10), `OMP_NUM_THREADS=1`.
- Attentes de fonctionnement (pas des prédictions de résultat) : R2 = A au bit ; R3 = B au bit ; R4(λ = 0) = R2 au bit ; fausses alertes dans α ± 0,005 ; aucune garde déclenchée ; temps par tâche sous 600 s.

## 6. Ce que ce gel ne fait pas

Aucune décision pour le programme, aucun scellement, aucun commit, aucun appel réseau ; aucune lecture de `donnees/` hors `argon-seul-convergence-v1/` ; aucune modification de `arene_melange_v4.py` ; aucune racine de décision employée.
