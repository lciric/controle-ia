# Gel — quatre règles de mise à jour de la défense dans l'arène v4, plus le témoin « défense figée » et la mesure X̄ — v2 (écrit AVANT toute exécution du code v2)

- Auteur : sous-agent neuf (développeur-rédacteur, modèle Fable 5.1), 1er novembre 2026, 10:46 UTC (relevé `date -u`) ; n'a écrit ni le gel v1, ni le code v1, ni le brouillon 1, ni la contre-lecture 1.
- Ce gel **remplace** `gel-regles-defense-v1.md` (empreinte `4fbb12dc941479f59504d9c3dc8246bf88c474a40c387bea40ac2e24c4ef0890`, archivé sans modification, R12) pour le code `arene_regles_defense_v2.py`, qui épingle l'empreinte de ce gel v2 et refuse de partir sans lui. Tout ce qui n'est pas repris ici du gel v1 reste tel quel (§ 2 à 4 recopiés, complétés).
- Hypothèse de travail posée par la session principale (le directeur n'a pas encore tranché ; écrite comme telle, modifiable par lui) : option (b) du constat CL-05 de la contre-lecture 1 (mesure X̄ préenregistrée pour HR2) ; témoin R0 « défense figée » ajouté (option (c) du brouillon 1, S6) ; quatre variantes de décision plus le témoin : R0, R1, R2, R3, R4(λ*) ; λ* = 0,3, référence « moyenne » (produit mécanique de la règle du gel v1 § 3 sur le pilote d'essai v1) ; grille complète retirée (CL-07) ; T = 8, N = 100, δ = (1,4 ; 1,6), m = 0,02.

## 0. Ce qui change entre la v1 et la v2 (et pourquoi)

| Changement | Pourquoi | Où |
|---|---|---|
| Mesure **X̄** = moyenne des X_t sur les T tours (X_t = 1 − (iii)_t, déjà calculé par tour) rendue par trajectoire, à côté de X finale = 1 − V ; contraste apparié R_k − R2 sur X̄ à l'analyse | CL-05 : V finale lit la phase du cycle de R1 à la parité de T près ; X̄ ne dépend pas de cette parité au-delà d'une tolérance (essai) ; HR2 est portée sur X̄ (option (b)) | code v2 `trajectoire_regle`, `executer_tache_regles`, `MESURES_CONTRASTE` |
| Témoin **R0 « défense figée »** : M0 déployé à tous les tours, jamais réentraîné ; l'attaquant joue en dernier à chaque tour (meilleure réponse à M0, départ supplémentaire = attaque précédente) ; finale du v4 sur M0 ; code de graine **20** (neuf : libre dans le v4 et la v1) | S6 option (c) du brouillon 1 et avis de la contre-lecture 1 (§ 4) : isole l'effet « ne rien faire » ; rend R4 lisible comme interpolation entre R0 et R2 ; hypothèse HR0 neuve (R2 contre R0) | code v2 `trajectoire_regle` (branche R0), `CODES`, `REGLES` = (R0, R1, R2, R3, R4) |
| Identité de préenregistrement **PREREG-REGLES-DEFENSE-V2**, `VERSION = arene_regles_defense_v2`, empreinte de ce gel épinglée | nouvelle version = nouveau nom (R12) ; le bloc d'identité change (code, gel, identifiant) | code v2 |
| Racines d'essai **neuves** (§ 1) ; les racines d'essai de la v1 sont déclarées employées et refusées par le code v2 | R9 : une racine d'essai lue (pilote v1, essais v1) n'est pas réemployée ; même pratique que le v4 pour ses prédécesseurs | code v2 `exiger_racine_permise_regles` |
| En mode `decision`, le gel sur disque est revérifié (`exiger_gel_regles(RACINES_DECISION)`) après l'autorisation | CL-08 (mineur) : en v1 le gel n'était revérifié qu'en mode `essai` | code v2 `main` |
| Analyse : par variante, liste du cosinus consécutif moyen **par tâche** (pour S12, lu par le lecteur R13 sans seuil dans le code) ; par contraste, écart « attaquant standard seul » contre « renforcé seul » (déclencheur 5) | CL-11 (mineur) : ces deux lectures n'étaient pas calculées par l'analyse v1 | code v2 `resume_variante`, `analyser_regles` |

**Rien d'autre ne change** : règles R1 à R4, oracle, attaquant, lois tenues, finale, graines de R1 à R4 (codes 21, 1, 2, 24), compteurs de coût, gardes. R2 = A et R3 = B au bit restent exigés (essais clés repris). La grille de λ du gel v1 § 3 et sa règle de choix ne sont pas rejouées : λ* = 0,3 et la référence « moyenne » viennent du pilote d'essai v1 (racines 20266101 / 20266102, règle écrite avant lui) ; le pilote d'essai v2 ne sert qu'à vérifier que X̄ et R0 sortent et à mesurer le temps.

## 1. Racines (R9) — plage 20266001 à 20266999 ; état en v2

Dérivation inchangée : `SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, role, …))`, numpy ≥ 1.25, dans la copie chargée du v4 (`gen` remplacé par `gen_regles`). Le code v2 refuse tout ce que le v1 refusait (racines de décision du v4, racines déjà employées par les arènes v1 à v4 et leurs contre-lectures, plage 20265001 à 20265999, plage 20264001 à 20264999) **et** les racines d'essai de la v1, employées.

| Racine | Rôle | État en v2 |
|---|---|---|
| 20266101 / 20266102 | pilote d'essai **v1** | **employées** (pilote v1 lu pour λ*) : refusées par le code v2 |
| 20266301 / 20266302 / 20266303 | essais du code **v1** | **employées** : refusées par le code v2 |
| 20266401 | simulations (calcul de puissance par rééchantillonnage réel, si le directeur le demande) | réservée, non employée ; permise hors décision |
| **20266201 / 20266202** | **décision** (principale / tenues) | **réservées, jamais employées** (ni par la v1 ni par la v2) : refusées par le module sans autorisation par préenregistrement scellé, conforme et identifié (`PREREG-REGLES-DEFENSE-V2`) ; inchangées de la v1 : aucune graine n'en a été tirée |
| **20266501 / 20266502** | pilote d'essai **v2** (principale / familles tenues à l'écart) | pilote d'essai v2 de ce dossier |
| **20266511 / 20266512** | essais du code **v2** (pytest) | essais |
| **20266513** | essais v2 : « une autre racine change le résultat » | essais |
| 20266521 | réservée (reprise éventuelle du pilote v2 en cas d'erreur de code) | non employée |

La plage 20266201 à 20266299 proposée pour les racines d'essai v2 n'est pas retenue : elle contient les racines de décision. Racine des familles tenues à l'écart toujours distincte de la racine principale (garde).

## 2. Règles (chacune à trajectoire propre sur T tours, moniteur commun M0 au tour 0 entraîné contre la loi cible)

À chaque tour t = 1 … T : l'attaquant calcule une meilleure réponse (SLSQP, départs du v4, départ supplémentaire = attaque précédente) contre la défense déployée ; la défense se met à jour selon la règle.

| Code | Règle | Mise à jour du défenseur | Code de graine (`code_bras`) |
|---|---|---|---|
| **R0** | **« défense figée » (témoin)** | **aucune** : M0 reste déployé à tous les tours ; zéro entraînement après le tour 0 (essai par instrumentation) ; l'attaquant répond à M0 à chaque tour (sa réponse peut varier d'un tour à l'autre par les graines et le départ supplémentaire) ; finale du v4 sur M0 figé. Matrice H : T + 1 lignes identiques (le moniteur « du tour s » est M0 pour tout s), donc I2 = 0 par construction ; cosinus consécutif = 1 par construction (recopié, hors S12) | **20** |
| R1 | « dernière attaque » (protocole de Bailey transposé) | moniteur linéaire réentraîné (oracle « détection » du v4) contre la **seule attaque du tour t** ; seul déployé ; la loi cible n'entre plus dans son entraînement après le tour 0 (CL-10) | 21 |
| R2 | « historique » | = bras A du v4 : moniteur linéaire réentraîné contre le mélange **uniforme de toutes les attaques passées, la loi cible comprise** (coup du tour 0) ; seul déployé. Même code de graine que A : trajectoire **identique au bit** à celle de A (essai clé) | 1 |
| R3 | « mélange d'équilibre des deux côtés » | = bras B du v4 (double oracle tronqué) : moniteurs passés tirés selon les poids d'équilibre p du jeu restreint ; oracle du défenseur entraîné contre la stratégie d'équilibre q de l'attaquant. Même code de graine que B : identique au bit à B (essai). **R3′** : valeur du jeu restreint à chaque tour, rapportée à côté de l'exploitabilité ; une trajectoire distincte où l'attaquant déploierait son mélange n'ajouterait rien au double oracle : non construite, déclaré | 2 |
| R4 | « régularisation vers le passé » | moniteur linéaire réentraîné contre le mélange uniforme de l'historique (comme R2), objectif de détection du v4 **plus** la pénalité sans échelle λ‖w/‖w‖ − u‖² = 2λ(1 − cos(w, u)), u = « dernier » (direction du moniteur déployé) ou « moyenne » (moyenne des directions unitaires des moniteurs passés, M0 compris ; poids de moniteurs, pas de jetons) ; biais non pénalisé ; à λ = 0, R4 = R2 au bit (essai) | 24 |

Justification de la pénalité sans échelle : inchangée (gel v1 § 2). Les départs de l'entraînement, le nombre d'itérations et la calibration du seuil sont ceux du v4.

## 3. Réglages de R4 (gel v1 § 3, non rejoués)

Grille {0,03 ; 0,1 ; 0,3 ; 1 ; 3} × références {« dernier », « moyenne »} ; règle de choix : λ* maximise la moyenne de V(R4, λ) sur les tâches du pilote d'essai (les deux δ confondus), égalité à 0,005 près → la plus petite λ, puis « dernier » (règle du code, CL-14). Résultat sur le pilote v1 : **λ* = 0,3, référence « moyenne »** (voir `pilote-essai-regles-defense-v1.md` § 3 et les trois faits recalculés par la contre-lecture 1, § 4 M1). La v2 ne relance pas la grille ; le pilote v2 ne lance R4 qu'à (0,3 ; « moyenne »). Si le directeur choisit un autre réglage, le bloc d'identité du préenregistrement (LAMBDA_RETENU, REFERENCE_RETENUE) change, pas ce gel.

## 4. Mesures (par règle, par tâche = (δ, instance), par tour puis en finale)

- **Exploitabilité par tour** : X_t = 1 − (iii)_t, (iii)_t = taux de détection de la meilleure réponse de l'attaquant au tour t contre la défense déployée, sur un échantillon frais (19 998 points). **X̄** = (1/T) Σ_{t=1}^{T} X_t (moyenne sur les tours, par trajectoire ; rendue `exploitabilite_moyenne_tours`). **X finale** = 1 − V, V = la plus basse des détections des réponses standard et renforcée contre la défense finale figée (métrique (iii) du v4). Valeurs absolues dans [0 ; 1] (garde) ; contrastes appariés R_k − R2 sur V, sur (ii) finale, sur X finale et sur X̄ calculés à l'analyse (rééchantillonnage apparié des instances, codes de graine de rééchantillonnage : contrastes 200 + 100 × j + rang de la variante avec j = 0 (V), 1 ((ii)), 2 (X finale), **8 (X̄ : 1000 + rang, pour ne pas heurter les codes 500 à 799 des indicateurs)** ; indicateurs 500 + 100 × j + rang). Rang de la variante = ordre R0, R1, R2, R3, R4.
- Note : à T = 1, X̄ = X_1 (un seul tour) ; X̄ n'est **pas** égale à X finale, même à T = 1, parce que la finale emploie l'attaquant lourd du v4 (12 puis 48 départs, 512 échantillons de Monte-Carlo, plus les attaques passées) contre la défense finale, alors que X_t emploie l'attaquant léger du tour (4 départs, 256 échantillons) contre la défense déployée au tour t.
- **Détection sur attaques tenues à l'écart** (ii), **I1**, **I2**, **I3** et H, **coût**, contrôles : inchangés (gel v1 § 4). Pour R0 : I1 lu sur (iii)_t (l'attaquant varie, la défense non), I2 = 0, H à lignes identiques.
- **Dégénérescence** : cosinus consécutif par tour et sa moyenne par tâche, rendus par variante (liste par tâche à l'analyse) ; R0 : 1 par construction.

## 5. Pilote d'essai v2 (racines 20266501 / 20266502)

- Instances 0 à 1 (2) × 2 δ (1,4 ; 1,6, `DELTAS_V4`) × variantes R0, R1, R2, R3, R4[moyenne, λ = 0,3] ; T = 8 ; configuration `CONFIG_V4` inchangée (empreinte dans le manifeste) ; finale « légère » du v4 plus (ii) finale et (i) sur les attaques vues.
- But : vérifier que X̄ et R0 sortent, qu'aucune garde ne se déclenche, mesurer le temps par tâche à 5 variantes (projection du coût de la décision) ; **rien n'en est lu comme résultat** ; aucune prédiction n'en est tirée.
- Deux processus de travail, PID consignés, arrêt par PID (R10), vérification « aucun orphelin », `OMP_NUM_THREADS=1`.
- Attentes de fonctionnement (pas des prédictions) : R2 = A au bit ; R3 = B au bit ; R0 : 0 entraînement, 7 paramètres stockés et déployés ; fausses alertes dans α ± 0,005 ; temps par tâche sous 600 s.

## 6. Ce que ce gel ne fait pas

Aucune décision pour le programme (l'hypothèse de travail ci-dessus est celle de la session principale, soumise au directeur), aucun scellement, aucun commit, aucun appel réseau ; aucune lecture de `donnees/` hors `argon-seul-convergence-v1/` ; aucune modification de `arene_melange_v4.py` ni d'aucun fichier v1 ; aucune racine de décision employée.
