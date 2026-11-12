# Préenregistrement — quatre règles de mise à jour de la défense dans l'arène coévolutive synthétique v4 : exploitabilité, détection sur attaques tenues à l'écart, coût — v1 — BROUILLON 1 (non scellé)

**Statut : brouillon 1, non gelé ; écrit par un sous-agent neuf après le code, ses essais et un pilote d'essai sur racines d'essai ; à contre-lire (R2) par un sous-agent neuf, puis gel des seuils et des marqueurs par Lazar, puis scellement, puis course décisive (GO de Lazar). Les marqueurs « [DÉCISION DE LAZAR] » et les champs laissés au gabarit signalent ce que le directeur tranche ; le validateur `controle_ia.prereg` refuse tout texte qui garde un champ de gabarit non rempli.**

Identifiant : **PREREG-REGLES-DEFENSE-V1**. Tâche : demande du directeur (1er novembre 2026) : « comparer dans notre jeu quatre règles de mise à jour de la défense (dernière attaque ; historique ; mélange d'équilibre des deux côtés ; régularisation vers le passé) sur exploitabilité, détection sur attaques tenues à l'écart et coût ; rendre le jeu posable à classe de fonctions égale ; préenregistrer ». Pilote de **mécanisme** : aucun modèle de langage, aucun texte ; « l'attaquant » est un choix de paramètres d'une loi synthétique (mélange gaussien) sous contrainte de comportement ; le monde, l'oracle du défenseur, l'attaquant et les familles tenues à l'écart sont ceux de l'arène v4 (`arene_melange_v4.py`, jamais modifiée). La formalisation du jeu et le jeu jouet OpenSpiel sont confiés à un autre sous-agent : hors de ce texte.

- Auteur : sous-agent neuf (développeur-chercheur, modèle Fable 5.1), 1er novembre 2026 ; a écrit le gel v1, le code, les essais, le pilote d'essai et ce brouillon ; n'a écrit ni le v4 ni ses brouillons.
- Date (UTC) : 2026-11-01, voir le LISEZMOI pour l'heure de fin.
- Commit du code d'analyse : À REMPLIR au gel (commit qui contient `arene_regles_defense_v1.py` à l'empreinte du bloc d'identité ; le dossier n'est pas encore commité : aucun commit par le sous-agent).
- Documents qui font foi (chemin + empreinte) :
  - `donnees/argon-seul-convergence-v1/arene_melange_v4.py` — `70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61` (le jeu, les bras A et B, l'attaquant, les lois tenues, les indicateurs I1 à I3, le rééchantillonnage) ;
  - `donnees/argon-seul-convergence-v1/preenregistrement-arene-melange-equilibre-v1-brouillon4.md` (brouillon 4 du v4 : bras A = « historique », valeur nulle 0,7345, δ = (1,4 ; 1,6), N = 100, S18 = 0,10 ; empreinte au LISEZMOI du dossier v4) et `verification-arene-melange-v4-brouillon4.md` (même dossier) ;
  - `docs/notes/convergence-defense-v1/regles-defense-v1/gel-regles-defense-v1.md` — `4fbb12dc941479f59504d9c3dc8246bf88c474a40c387bea40ac2e24c4ef0890` (racines neuves, règles, grille de λ et règle de choix, écrits avant toute exécution ; empreinte épinglée dans le code) ;
  - `prereg/gabarit-preregistrement-v1.md` — `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`.
- Code, essais et pilote (même dossier que ce texte) : `arene_regles_defense_v1.py` (bloc d'identité) ; `test_arene_regles_defense_v1.py` ; `pilote-essai-regles-defense-v1.json` et `.md` ; empreintes recalculées au LISEZMOI.

**Aucune lecture n'a été faite sur les racines de décision RACINE_DECISION = 20266201 et RACINE_DECISION_TENUE = 20266202** (refusées par le code sans préenregistrement scellé). Tout nombre de ce texte vient du brouillon 4 du v4 (cité comme contexte, **non opposable** : pilote v4 sur 24 instances d'une racine d'essai), du gel v1, ou est un marqueur ; **aucune prédiction n'est tirée du pilote d'essai de ce dossier** (il ne fournit que λ*, la référence de R4, et la projection de temps, par des règles écrites avant lui).

### Bloc d'identité (vérifié par le code à la décision ; à régénérer par `arene_regles_defense_v1.py identite` si le code ou la configuration change)

- Identifiant : PREREG-REGLES-DEFENSE-V1
- Racines de décision : RACINE_DECISION = 20266201 ; RACINE_DECISION_TENUE = 20266202
- Code : `arene_regles_defense_v1.py` — 337c569bd90d5b8964a4e6b7491c0c5a67042d54333401b65540e889a15a2c97
- Arène v4 : `arene_melange_v4.py` — 70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61
- Gel : `gel-regles-defense-v1.md` — 4fbb12dc941479f59504d9c3dc8246bf88c474a40c387bea40ac2e24c4ef0890
- Configuration (empreinte de la forme canonique) : 3fbb27fc0824b7a9d13a0036c975c43e00e4dc7ece9f0231dfca7c0234785098
- Bibliothèque `src/controle_ia/gardes.py` — a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439
- Bibliothèque `src/controle_ia/prereg.py` — 3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306
- Bibliothèque `src/controle_ia/scellement.py` — 93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2
- Bibliothèque `src/controle_ia/manifeste.py` — 1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d
- Versions : numpy 2.4.6 ; scipy 1.17.1 ; Python 3.13.18

<!-- configuration-canonique-debut -->
```json
{
 "K": 3,
 "T": 8,
 "alpha": 0.01,
 "audit_critere": 0.01,
 "audit_departs": 100,
 "audit_es_generations": 400,
 "audit_es_lambda": 12,
 "audit_iter": 300,
 "audit_k": 10,
 "audit_n_mc": 1024,
 "audit_quantile_t": 0.995,
 "boite_mu": 5.0,
 "d": 6,
 "deltas": [
  1.4,
  1.6
 ],
 "departs": 4,
 "departs_cout": 3,
 "departs_entr": 8,
 "departs_final": 12,
 "departs_renforce": 48,
 "entrainement": "detection",
 "fractions_courbe": [
  0.25,
  0.5,
  0.75
 ],
 "grille_calibrage": [
  0.6,
  0.8,
  1.0,
  1.2,
  1.4,
  1.6,
  1.8,
  2.0,
  2.4
 ],
 "iter_entr": 300,
 "iter_max": 100,
 "iter_renforce": 200,
 "kappa_contournement": 0.5,
 "l2": 0.001,
 "lambda_ou": 8.0,
 "n_attaque_entr": 2001,
 "n_cal": 20000,
 "n_calibrage": 48,
 "n_eval": 19998,
 "n_eval_tenue": 3999,
 "n_fpr": 20000,
 "n_instances": 100,
 "n_mc": 256,
 "n_mc_final": 512,
 "n_propre_entr": 2000,
 "n_tenue": 50,
 "pas_bissection": 3,
 "plafond_cpu_tache_s": 600.0,
 "r_cible": 4.0,
 "schema_graines": "SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, role, ...)) ; bras commun 0, A 1, B 2, D 4, C1 5, C2 6, C3 7, B' 8, C3' 9 ; roles cible 0, propre 1, attaques d'entrainement 2, calibration 3, fausses alertes 4, Monte-Carlo 5, departs 6, evaluation 7, init maxout 8, lois tenues 9, echantillons tenus 10, final 11, cout 12, Dirichlet 13, courbe 14, attaquant independant 15 ; reechantillonnage (code_delta, code_contraste, 0, 0, 99)",
 "seuil_calibrage_bas": 0.1,
 "seuil_calibrage_haut": 0.03,
 "sigma_cible": 1.0,
 "sigma_max": 1.5,
 "sigma_min": 0.5,
 "tau": 0.25,
 "taux_departs_non_finis_max": 0.05,
 "taux_nonconv_max": 0.1,
 "tol_fpr": 0.005,
 "unites_Bp": 9
}
```
<!-- configuration-canonique-fin -->

Réglages de R4 gelés par la règle du gel v1 § 3 sur le pilote d'essai (vérifiés par le code à la décision ; **[DÉCISION DE LAZAR]** : confirmer ou choisir autrement, voir S6) :

- LAMBDA_RETENU = 0.3
- REFERENCE_RETENUE = moyenne

## Résumé pour Lazar

1. **Question** : dans le jeu synthétique du v4, laquelle de quatre règles de mise à jour du défenseur laisse le moniteur déployé le moins exploitable après T = 8 tours de coévolution, à quel prix sur les attaques jamais vues (tenues à l'écart) et en temps de calcul ? R1 « dernière attaque » (réentraîner contre la seule dernière attaque, transposition du protocole de Bailey et collègues) ; R2 « historique » (= bras A du v4 : mélange uniforme de toutes les attaques passées, règle de référence) ; R3 « mélange d'équilibre des deux côtés » (= bras B du v4 : double oracle, moniteurs passés aux poids d'équilibre, oracle du défenseur contre la stratégie d'équilibre de l'attaquant ; lecture R3′ « les deux joueurs à l'équilibre » = valeur du jeu restreint, sur la même trajectoire) ; R4 « régularisation vers le passé » (historique plus pénalité sans échelle 2λ(1 − cos(w, u)) vers la direction du moniteur déployé ou la moyenne des directions passées ; λ* et la référence choisis sur le pilote d'essai par une règle écrite avant lui).
2. **Classe de fonctions égale** : les quatre règles déploient **un moniteur linéaire** (7 paramètres par requête) pour R1, R2, R4, et un **mélange** de moniteurs linéaires (7 paramètres par requête, 63 stockés) pour R3 : classe de fonctions déployée égale (linéaire), à nombre de paramètres déployés par requête égal ; R3 stocke T + 1 moniteurs (déclaré : c'est le même écart que B − A au v4). Aucun maxout ici : la question « classe égale » du v4 (Q2, B′ contre D) n'est pas reprise.
3. **Ce qui est nouveau par rapport au v4** : R1 et R4 n'existaient pas ; R2 et R3 sont A et B (reproduits au bit par la boucle commune, essais clés) ; l'exploitabilité est lue **par tour** (X_t = 1 − (iii)_t) et en finale (X = 1 − V) ; le coût est compté (processeur, appels à l'optimiseur, programmes linéaires).
4. **Hypothèses (signes par principe, confiance modérée)** : R3 moins exploitable que R2 (= « B − A » du v4, contrôle de plomberie) ; R1 plus exploitable que R2 (oubli) ; R4(λ*) au plus aussi exploitable que R2 (amortissement du cycle) ; sur les tenues à l'écart : R3 régresse (comme B − A au v4), R1 régresse, R4 ne régresse pas ; coût : R3 > R2 ≈ R4 > R1.
5. **Seuils** : S1 à S12 à geler par Lazar ; recommandations : marge m = 0,02 (= v4), N = 100 par δ, T = 8, δ = (1,4 ; 1,6), Bonferroni par famille, bornes par rééchantillonnage apparié comme le v4.
6. **Coût estimé de la décision** (pilote d'essai, racine d'essai, 12 tâches) : 4 variantes (R1, R2, R3, R4 à λ*) : ≈ 15 s de processeur par tâche → 200 tâches ≈ 50 min de processeur, ≈ 26 min de mur sur 2 processus à l'efficacité mesurée 0,97 (≈ 13 min sur 4 processus) ; grille complète de 13 variantes : ≈ 41 s par tâche → ≈ 136 min de processeur, ≈ 70 min de mur sur 2 processus ; pilote : 12 tâches, 490 s de processeur, 253 s de mur, aucune garde déclenchée, 0 entraînement non convergé sur 1 272, 0 départ non fini sur 19 812 ; recommandation S8 : `timeout 3600` pour 4 variantes, `timeout 9000` pour la grille. Aucune dépense : processeur seulement.
7. **Points à trancher** : S6 (λ* et référence : la règle de choix peut retenir l'extrémité « défense presque figée » ; options), S12 (dégénérescence de R4), l'ajout éventuel d'un témoin R0 « défense figée (M0 jamais réentraîné) », la grille complète de λ en descriptif à la décision ou non, l'ordre d'exécution avec la course du v4.

## Ce que l'expérience n'autorise pas

- **Rien sur les vrais modèles** ni sur les moniteurs d'activations réels ; le monde est une famille de lois écrite par le programme (v4, § Portée). R1 est une **transposition** du protocole de Bailey et collègues (réentraîner contre la dernière attaque) avec l'oracle « détection » du v4, non une reproduction ; aucun chiffre de ce papier n'est repris (R7).
- Deux budgets δ, choisis au v4 sur A seul ; T = 8 ; attaquant local en boîte blanche (SLSQP, départs du v4) : (iii) est une **borne haute** de la valeur du jeu, donc X = 1 − V une **borne basse de l'exploitabilité** ; sans attaquant indépendant dans cette v1 (option : celui du v4, `attaquant_independant`, non branché sur les règles nouvelles ; déclaré).
- R3′ n'est pas une trajectoire distincte : la valeur du jeu restreint est lue sur la trajectoire de R3 ; une trajectoire où l'attaquant déploierait son mélange d'équilibre n'ajouterait aucune stratégie nouvelle au double oracle (déclaré, gel § 2).
- R4 dépend d'un réglage (λ, référence) choisi sur racine d'essai par une règle écrite d'avance : le résultat vaut pour ce λ* dans ce monde ; la grille entière peut être recopiée en descriptif.
- Aucune revendication d'antériorité ni de nouveauté (R8) ; aucune porte, aucune dépense, aucune modification du programme.

## Hypothèse

Renvoi : question du directeur (1er novembre 2026) ; brainstorm P-041 piste 3 (mélange d'équilibre contre défense unique) ; brouillon 4 du v4 (Table 5 : la défense unique A ne progresse pas et revient vers d'anciennes attaques au-delà du hasard). **Oracle du défenseur** : « détection » du v4, identique pour les quatre règles (principe S13 du v4).

- **HR1 (principale)** : contre la meilleure réponse finale, le mélange d'équilibre R3 est moins exploitable que l'historique R2 d'au moins m = S1 aux deux δ : Δ(R3, R2) = moyenne de V(R3) − V(R2) ≥ m. H0 : non à au moins un δ. (C'est le contrôle de plomberie B − A du v4, repris comme hypothèse principale parce que R2 est ici la référence de toutes les règles.)
- **HR2** : la règle « dernière attaque » R1 est plus exploitable que R2 : Δ(R1, R2) ≤ −m aux deux δ (la défense qui oublie se fait reprendre sur les attaques anciennes). H0 : non à au moins un δ.
- **HR3** : la régularisation vers le passé R4(λ*) est au plus aussi exploitable que R2 : Δ(R4, R2) ≥ 0 (borne basse B2 > −m aux deux δ ; « au moins aussi bien, à la marge près »). Prédiction non ferme sur l'ampleur ; voir S12 pour la dégénérescence.
- **HR4 (tenues à l'écart)** : sur les familles jamais vues par aucune mise à jour (50 lois par tâche, racine tenue à part), Δ(R3, R2) sur (ii) < 0 (régression, comme B − A au v4) ; Δ(R1, R2) sur (ii) < 0 ; Δ(R4, R2) sur (ii) ≥ −S5 (sans régression à la tolérance près).
- **HR5 (condition d'application)** : R2 ne progresse pas (I1 ≈ 0) et ses attaques reviennent vers d'anciennes au-delà du hasard (I3 − 0,7345 > 0) : réplication de la Table 5 du v4, avec sa lecture ; R1 : retours au-delà du hasard au moins autant que R2 ; R4(λ*) : I3 − nul plus bas que R2 (descriptif).
- **HR6 (coût)** : descriptif, sans verdict : temps processeur par tâche et appels à l'optimiseur de R3 > R2 ≈ R4 > R1 ; programmes linéaires : R3 seul.
- **Hypothèses de travail** : oracle du défenseur approché (seuil gaussien, départs du v4) ; attaquant approché, contrôlé par la réponse renforcée (V = min) ; loi propre N(0, I) connue du code ; R3 itéré tronqué ; λ* fixé sur racine d'essai.

## Prédiction chiffrée et signe attendu

Signes et ordres de grandeur **par principe et par le contexte du v4 (brouillon 4, non opposable : B − A +0,128 / +0,139 sur (iii), −0,054 / −0,058 sur (ii) au pilote v4 ; A : I1 ≈ 0, I3 − nul +0,17 / +0,21)** ; aucune valeur ne vient du pilote d'essai de ce dossier. Confiance = probabilité subjective arrondie ; la branche opposée déclenche l'audit (R4, déclencheur 1).

| # | Contraste ou indicateur | δ | Signe | Classe prédite (Tables B à D) | Ordre de grandeur | Confiance | Branche opposée |
|---|---|---|---|---|---|---|---|
| P1 | Δ(R3, R2) sur V (HR1) | 1,4 ; 1,6 | + | « R3 > R2 » | ≥ +0,05 (contexte v4 : ≈ +0,13) | 0,9 | « R2 ≳ R3 », « R2 > R3 », « ≈ » |
| P2 | Δ(R1, R2) sur V (HR2) | 1,4 ; 1,6 | − | « R2 > R1 » | ≤ −0,02 | 0,6 | « R1 ≳ R2 », « R1 > R2 » |
| P3 | Δ(R4, R2) sur V (HR3) | 1,4 ; 1,6 | ≥ 0 | « R4 ≳ R2 » ou « ≈ » (non ferme) | [0 ; +0,05] | 0,5 | « R2 > R4 » |
| P4 | Δ(R3, R2) sur (ii) (HR4) | 1,4 ; 1,6 | − | « régression » | ≈ −0,05 (contexte v4) | 0,8 | borne basse B8 > 0 |
| P5 | Δ(R1, R2) sur (ii) (HR4) | 1,4 ; 1,6 | − | « régression » | ≤ −0,02 | 0,6 | borne basse B8 > 0 |
| P6 | Δ(R4, R2) sur (ii) (HR4) | 1,4 ; 1,6 | ≥ −S5 | « sans régression à S5 près » | [−0,02 ; +0,05] | 0,5 | borne haute B8 < −S5 |
| P7 | R2 : I1, I3 − 0,7345 (HR5) | 1,4 ; 1,6 | I1 ≈ 0 ; I3 − nul > 0 | Table D ligne « cycle » | I3 − nul ≈ +0,1 à +0,2 | 0,85 | « R2 progresse » ; borne haute de I3 − nul < 0 |
| P8 | R1 : I3 − 0,7345 (descriptif) | 1,4 ; 1,6 | > 0 | — | ≥ celui de R2 | 0,6 | — |
| P9 | R4(λ*) : I3 − 0,7345 (descriptif) | 1,4 ; 1,6 | < celui de R2 | — | — | 0,6 | — |
| P10 | Coût (HR6) : processeur par trajectoire | — | R3 > R2 ≈ R4 > R1 | — | R3 ≥ 1,3 × R2 ; R1 ≤ R2 | 0,7 | ordre différent (sans effet sur les tables) |
| P11 | Fausses alertes finales | 1,4 ; 1,6 | — | \|moyenne − α\| ≤ 0,001 par règle | — | 0,9 | déclencheur 6 |

Ce qui compterait comme réfutation : HR1 réfutée si « R3 > R2 » n'est pas la classe aux deux δ (y compris « ≈ ») ; HR2 réfutée si « R2 > R1 » n'est pas la classe aux deux δ ; HR3 réfutée si « R2 > R4 » à un δ ; HR4 lue par la Table C.

## Métrique

Notations : une **tâche** = (δ, instance) ; les deux δ partagent la loi cible d'une instance ; une **variante** = une règle (R4 : à λ* et référence gelés). Taux de détection d'une défense mixte {(m_i, p_i)} sur une loi Q : Σ_i p_i × part des échantillons de Q dont le score dépasse le seuil t_i de m_i ; seuils calibrés au quantile 1 − α de 20 000 échantillons propres communs (α = S9).

- **Exploitabilité, principale** : **V(règle)** = métrique (iii) du v4 : après T tours, défense figée ; deux meilleures réponses sous la contrainte distance ≤ δ et la boîte — **standard** (12 départs tirés + départ vers l'origine + attaques passées de la trajectoire, 512 échantillons de Monte-Carlo par composante, 100 itérations SLSQP) et **renforcée** (48 départs, 200 itérations, plus la réponse standard) — chacune évaluée sur 19 998 échantillons frais ; **V = la plus basse des deux détections** ; **X = 1 − V** (exploitabilité finale, valeur absolue dans [0 ; 1], garde). **Par tour** : (iii)_t = détection de la meilleure réponse du tour t contre la défense déployée au tour t (départs du v4, `departs` = 4, plus l'attaque précédente), sur 19 998 échantillons frais ; X_t = 1 − (iii)_t. Les contrastes se lisent sur V (Δ(R_k, R2) = moyenne sur les instances de V(R_k) − V(R2), à δ fixé) ; X = 1 − V en est la lecture miroir (même intervalle, signe opposé).
- **R3′** : valeur du jeu restreint à chaque tour (après la colonne de l'attaque du tour, avant le moniteur nouveau) et en finale (programme linéaire du v4) : détection quand les deux joueurs jouent l'équilibre du jeu restreint ; descriptif, à côté de (iii)_t.
- **(ii) familles tenues à l'écart** : 50 lois par tâche tirées de RACINE_DECISION_TENUE (deux sous-familles du v4, 3 999 échantillons par loi), jamais passées à un entraînement (essai `test_tenues_jamais_vues_par_l_entrainement`) ; score = moyenne des 50 taux, par tour (défense déployée) et en finale ; sous-familles recopiées. **(i) familles vues** : descriptif.
- **Condition d'application** (R2 : verdict ; R1, R3, R4 : descriptif) : matrice H (ligne s = moniteur du tour s, colonne t = attaque du tour t ; pour R3, moniteurs un à un), **I1** = moyenne de (iii) aux tours 5–8 moins aux tours 1–4 ; **I2** recopié ; **I3** = part des tours t ≥ 3 où le déplacement de l'attaque est plus proche (cosinus) d'une attaque d'un tour ≤ t − 2 que de celle du tour t − 1 ; **valeur nulle 0,7345** à T = 8 ; l'indicateur lu est I3 − 0,7345. Fonctions du v4 inchangées.
- **Coût** : temps processeur de la trajectoire et de la finale (`time.process_time`) ; nombre d'appels à `scipy.optimize.minimize` (L-BFGS-B des entraînements, SLSQP de l'attaquant ; compteur posé sur la copie chargée du v4) ; nombre d'appels à `linprog` ; nombre d'entraînements ; nombre de départs de l'attaquant ; paramètres stockés et déployés par requête. Descriptif ; ratios contre R2 par tâche.
- **Dégénérescence de R4** : cosinus entre le moniteur nouveau et le dernier moniteur à chaque tour, moyenne par tâche (≈ 1 : la défense ne bouge plus) ; recopié ; seuil S12.
- **Contrôles** : fausses alertes de chaque défense finale sur 20 000 échantillons propres indépendants (garde α ± 0,005) ; V standard − V renforcé ; poids finaux de R3 (support, pureté, plus petit poids maximal parmi les équilibres) ; statuts de l'optimiseur, départs non finis, réponses à la limite ; entraînements non convergés (S18 = 0,10 par tâche, v4) ; reproductibilité bit à bit du moniteur du tour 0.
- **Intervalles** : rééchantillonnage apparié des instances, 20 000 tirages, quantiles linéaires 0,3125 %, 0,625 %, 1,25 %, 2,5 %, 5 % et symétriques (comme le v4) ; graines `SeedSequence(entropy=RACINE_DECISION, spawn_key=(code_delta, code, 0, 0, 99))`, code = 200 + 100 × mesure + rang de la variante (contrastes), 500 + 100 × indicateur + rang (indicateurs).

## Seuil

**Tous les seuils ci-dessous sont à geler par Lazar en une ligne datée de `registres/decisions.md` ; aucun défaut ne s'applique à une course décisive (nœud de décision : dépense de calcul sur devis et porte R1).** S4, S7, S9, S11 et S13 sont des champs de la configuration (identité à régénérer s'ils changent) ; S1, S2, S3, S5, S6, S8, S10, S12 sont appliqués par le lecteur R13 ou par la commande.

**S1 — marge d'effet d'intérêt sur V (Tables A et B)** — Valeur : À REMPLIR par Lazar. Recommandation : **m = 0,02** (deux fois α ; = S1 et S6 du v4), par principe.

**S2 — erreur de première espèce et corrections** — Valeur : À REMPLIR par Lazar. Recommandation : **5 % bilatéral par famille**, trois familles : Table A (plomberie, 2 δ : B2 = [q0,00625 ; q0,99375]) ; Table B (3 règles × 2 δ = 6 tests : bornes **B8** = [q0,003125 ; q0,996875], conservatrices pour 6 ; équivalence **E8** = [q0,00625 ; q0,99375]) ; Table C ((ii), 6 tests : B8) ; Table D (R2, 2 δ : B2). Réserve héritée du v4 : les percentiles d'un rééchantillonnage peuvent dépasser le nominal d'un facteur 2 près des frontières (brouillon 4, S2) ; aucune simulation de taille refaite ici (voir S3).

**S3 — puissance visée** — Valeur : À REMPLIR par Lazar. Recommandation : ≥ 0,8 pour la classe prédite de P1 à N = 100. **Réserve** : aucun calcul de puissance n'a été fait pour ce brouillon (le pilote d'essai, 6 instances par δ, ne le permet pas de façon opposable) ; option : simulation à la manière de (M4) du v4 sur le pilote d'essai, racine 20266401, avant gel — À REMPLIR (fait / non fait).

**S4 — nombre d'instances N par δ** — Valeur : À REMPLIR par Lazar. Recommandation : **N = 100** (champ `n_instances`, = v4) ; coût au § Plan 5.

**S5 — tolérance de non-régression sur (ii)** — Valeur : À REMPLIR par Lazar. Recommandation : **0,02** (= S1).

**S6 — réglage de R4 : λ* et référence** — Valeur : **[DÉCISION DE LAZAR]** À REMPLIR. Règle du gel v1 § 3 appliquée au pilote d'essai : λ* = valeur de la grille {0,03 ; 0,1 ; 0,3 ; 1 ; 3} qui maximise la moyenne de V(R4) sur les tâches du pilote (δ confondus), égalité à 0,005 près → la plus petite ; même règle pour la référence. Résultat de la règle : **LAMBDA_RETENU = 0.3, REFERENCE_RETENUE = moyenne** (ci-dessus, vérifiés par le code). **Enjeu** : à grand λ, R4 tend vers une défense figée (le moniteur ne bouge plus : cosinus consécutif ≈ 1) ; la règle de choix, écrite avant le pilote, peut retenir cette extrémité, auquel cas « R4 » mesure surtout « ne jamais réentraîner » (ce qui est une information en soi : une défense figée est-elle moins exploitable que l'historique dans ce monde ?). Options : (a) garder la règle et le λ* rendu, lire R4 avec S12 (recommandation, confiance 0,6 : règle écrite d'avance, rien n'est changé après lecture) ; (b) restreindre la grille à λ ≤ 0,3 et reprendre la règle (nouveau gel, nouveau pilote, racine neuve 20266401 réaffectée ou plage neuve) ; (c) ajouter un témoin **R0 « défense figée »** (M0 jamais réentraîné, code de graine 20) qui isole l'effet « ne rien faire » et rend R4 lisible comme interpolation entre R0 et R2 (coût : une trajectoire de plus, ≈ 2,5 s par tâche ; nouveau code v2, nouvel essai, nouveau gel) — option que l'auteur juge la plus utile mais qui n'a pas été implantée (hors gel v1).

**S7 — nombre de tours T** — Valeur : À REMPLIR par Lazar. Recommandation **T = 8** (= v4 ; valeur nulle de I3 = 0,7345).

**S8 — plafond de temps** — Valeur : À REMPLIR par Lazar. Recommandation : `timeout` externe égal à **deux fois** la projection au § Plan 5 à l'efficacité mesurée ; 600 s de processeur par tâche (garde interne `plafond_cpu_tache_s`, v4). Condition de lancement : machine sans autre calcul lourd ; charge relevée par `uptime` avant lancement et consignée ; réserve : la charge peut monter pendant le run (CM4-02 du v4).

**S9 — taux de fausses alertes α et tolérances** — Valeur : À REMPLIR par Lazar. Recommandation : **α = 0,01** ; garde |taux mesuré − α| ≤ 0,005 par défense finale ; déclencheur |moyenne d'une règle − α| > 0,001 dans un δ.

**S10 — déclencheur « trop beau / trop mauvais »** — Valeur : À REMPLIR par Lazar. Recommandation : audit si la moyenne de V d'une règle ≥ 0,99 dans un δ, ou si la moyenne de V ≤ 2α pour les quatre règles dans un δ (jeu dégénéré), ou si Δ(R3, R2) dépasse 0,30 dans un δ (au-delà du double du contexte v4). Pas de bande centrée sur le pilote d'essai (6 instances : trop peu ; déclaré).

**S11 — budgets de comportement δ** — Valeur : À REMPLIR par Lazar. Recommandation : **δ = (1,4 ; 1,6)** (`DELTAS_V4`, recalibrés au v4 sur A seul ; A = R2 : le calibrage vaut pour la règle de référence).

**S12 — dégénérescence de R4** — Valeur : **[DÉCISION DE LAZAR]** À REMPLIR. Recommandation : R4 « non exercée » à un δ si le cosinus consécutif moyen de R4(λ*) est ≥ **0,999** sur plus de la moitié des tâches de ce δ (la défense ne bouge plus) ; la classe de la Table B est alors recopiée avec la mention « R4 ≈ défense figée », sans verdict sur HR3.

**S13 — oracle du défenseur** — Valeur : À REMPLIR par Lazar. Recommandation : « détection » (v4, S13). S18 du v4 (0,10, convergence) repris dans la configuration.

## Plan d'analyse

### 1. Monde
Celui du v4 (brouillon 4, Plan 1) : loi propre N(0, I_6) ; loi cible à 3 composantes, moyennes de norme 4, écarts-types 1 ; loi d'attaque appariée dans la boîte (|μ| ≤ 5, σ ∈ [0,5 ; 1,5]) ; contrainte de comportement : racine de la moyenne sur k du carré de la distance de Wasserstein d'ordre 2 entre composantes appariées ≤ δ. Configuration `CONFIG_V4` inchangée (empreinte `3fbb27fc…` du bloc d'identité, la même que le v4).

### 2. Règles (gel v1 § 2 ; boucle commune `trajectoire_regle`)
Tour 0 commun : moniteur linéaire M0 entraîné contre la loi cible (reproductibilité bit à bit exigée). Pour t = 1 … T : l'attaquant calcule une meilleure réponse contre la défense déployée (graines du code de la règle : R1 21, R2 1, R3 2, R4 24) ; puis :
- **R1** : moniteur linéaire entraîné contre la seule attaque du tour ; seul déployé.
- **R2** : moniteur linéaire entraîné contre le mélange uniforme de toutes les attaques passées ; seul déployé (= A du v4 au bit : essai `test_R2_reproduit_A_du_v4_au_bit`).
- **R3** : p = équilibre du défenseur sur la matrice G des détections croisées ; q = équilibre de l'attaquant après la colonne nouvelle ; moniteur linéaire entraîné contre q ; défense = tous les moniteurs aux poids p (= B du v4 au bit : essai `test_R3_reproduit_B_du_v4_au_bit`) ; valeur du jeu restreint recopiée (R3′).
- **R4** : comme R2, objectif de détection plus 2λ*(1 − cos(w, u)), u = direction de référence gelée (S6) ; à λ = 0, identique à R2 à entrée égale (essai `test_entrainement_regularise_lambda_zero_egal_v4_et_lambda_fort_rapproche`).
Pour chaque règle, défense finale figée ; l'attaquant joue en dernier (standard puis renforcé) ; finale « légère » du v4 plus (ii) finale et (i) sur les attaques vues. Les règles ne partagent que M0, la loi cible, le propre d'entraînement de chaque tour, les lois tenues et les échantillons de calibration.

### 3. Graines (R9)
- **RACINE_DECISION = 20266201**, **RACINE_DECISION_TENUE = 20266202** (décision, jamais employées ; refusées par `gen_regles` sans préenregistrement scellé, conforme et identifié). Racines d'essai, toutes écrites au gel v1 avant emploi : 20266101 / 20266102 (pilote d'essai) ; 20266301 à 20266303 (essais du code) ; 20266401 (réservée, simulations).
- **Refusées par garde** (`exiger_racine_permise_regles`) : les racines de décision du v4 (20261201, 20261202), toutes les racines déjà employées par les arènes v1 à v4 et leurs contre-lectures, la plage 20265001–20265999 (autre session), la plage 20264001–20264999 (réservée au v4), toute racine absente du gel v1.
- Chaque tirage : `numpy.random.SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, rôle, …))`, numpy ≥ 1.25, rôles du v4 ; le remplacement de `gen` ne change que la liste des racines permises, pas le schéma.

### 4. Comparaisons et multiplicité
- **Table A** : Δ(R3, R2) sur V, B2 (plomberie / HR1). **Table B** : Δ(R1, R2), Δ(R3, R2), Δ(R4, R2) sur V, B8 et E8, marge m (HR1 à HR3). **Table C** : les trois contrastes sur (ii), B8, tolérance S5 (HR4). **Table D** : I1 et I3 − 0,7345 de R2, B2, marge S15 = S1 (HR5). **Table E** : coût, descriptif (ratios et ordre). **Descriptives** : X par tour et en finale ; R3′ ; I1, I2, I3 − nul de R1, R3, R4 ; matrices H ; cosinus consécutifs ; poids de R3 (support, pureté, pureté forcée) ; contrôles ; si la grille de λ est lancée en descriptif (§ 5), V et (ii) de chaque λ sans verdict.
- « Confirmée » = intersection-union sur les deux δ ; « réfutée » = union protégée par la correction.

### 5. Ordre d'exécution, arrêt et reprise
(1) Essais du code (`pytest`, 19 essais) ; (2) **[DÉCISION DE LAZAR]** : variantes de la décision — recommandation : R1, R2, R3, R4(λ*) seulement (4 trajectoires par tâche) ; option : grille complète de λ en descriptif (13 trajectoires, ≈ 3 fois le coût) ; (3) une seule invocation `PYTHONPATH=src OMP_NUM_THREADS=1 timeout <S8> python3 arene_regles_defense_v1.py decision --prereg prereg/<nom>.md --instances 0:N --run-id <AAAAMMJJ-HHMMSS-regles-defense-v1> --lambda <λ*> --reference <réf> --processus 2`, arbre git propre, machine sans autre calcul lourd ; manifeste et PID (scellés) sous `runs/<run-id>/`, résultats et analyse rattachés sous `diag/<run-id>/` (bibliothèque `manifeste.py`, comme le v4) ; (4) lecture par un sous-agent neuf (R13), qui applique les tables ; (5) **coordination avec la course du v4** : même monde, même machine ; **[DÉCISION DE LAZAR]** ordre des deux courses (recommandation : après la course du v4, pour ne pas partager la machine).
- **Coût projeté** (pilote d'essai, racine d'essai ; § 1 du `pilote-essai-regles-defense-v1.md`) : 4 variantes (R1, R2, R3, R4 à λ*) : ≈ 15 s de processeur par tâche → 200 tâches ≈ 50 min de processeur, ≈ 26 min de mur sur 2 processus à l'efficacité mesurée 0,97 (≈ 13 min sur 4 processus) ; grille complète de 13 variantes : ≈ 41 s par tâche → ≈ 136 min de processeur, ≈ 70 min de mur sur 2 processus ; pilote : 12 tâches, 490 s de processeur, 253 s de mur, aucune garde déclenchée, 0 entraînement non convergé sur 1 272, 0 départ non fini sur 19 812 ; recommandation S8 : `timeout 3600` pour 4 variantes, `timeout 9000` pour la grille.
- **Reprise après arrêt** : comme le v4 (Plan 5 du brouillon 4) : arrêt externe → arrêt par PID des processus consignés, garde « aucun orphelin » (`orphelins --pids …`), puis une reprise complète, même code, mêmes racines, nouvel identifiant ; seconde interruption → non concluant ; arrêt par garde interne → non concluant, version nouvelle ; aucun point de reprise partiel.

### 6. Historique de conception (déclaré)
1. Demande du directeur (1er novembre 2026). 2. Gel v1 (racines, règles, grille, règle de choix, taille du pilote) écrit à 09:52 UTC avant toute ligne de code ; empreinte épinglée dans le code. 3. Code, essais (une tâche de chronométrage à configuration complète sur la racine d'essais 20266301, non lue autrement que pour le temps et le bon fonctionnement). 4. Pilote d'essai (racines 20266101 / 20266102, 6 instances × 2 δ, 13 variantes). 5. Ce brouillon : **viennent du pilote** λ*, la référence (règle du gel § 3) et la projection de temps ; **rien d'autre** (les signes et ordres de grandeur sont posés par principe et par le contexte du v4, avant lecture des tables du pilote par l'auteur ; déclaré : l'auteur a vu le résumé du pilote en le produisant ; un contre-lecteur neuf vérifiera que les prédictions ne le recopient pas).

## Critères de lecture gelés

Un sous-agent neuf (R13) applique ces tables telles qu'écrites, **de haut en bas ; la première ligne vraie décide**. Notations à δ fixé : est = moyenne ; qX = quantile X ; **B2** = [q0,00625 ; q0,99375] ; **B8** = [q0,003125 ; q0,996875] ; **E8** = [q0,00625 ; q0,99375].

**V0** = aucune condition de la liste d'arrêt ∧ tâches exécutées = 2 × N ∧ racines du manifeste = RACINE_DECISION et RACINE_DECISION_TENUE ∧ empreintes du code, de l'arène v4, du gel, de la configuration et de la bibliothèque = celles du texte scellé ∧ λ et référence de la commande = LAMBDA_RETENU et REFERENCE_RETENUE ∧ une seule invocation ayant écrit des résultats (au plus une reprise complète consignée).

**Déclencheurs d'audit (R4), symétriques** — un seul suffit ; l'effet bloquant est écrit :
1. **Contradiction d'une prédiction ferme, dans les deux sens** : P1 (classe autre que « R3 > R2 » à un δ), P2 (autre que « R2 > R1 »), P7 (Table D autre que « cycle » à un δ), P11 ; *bloque* la table contredite.
2. **Trop beau / trop mauvais** (S10) ; *bloque* toutes les tables.
3. **Mélange R3 dégénéré** : poids de R3 purs (un poids ≥ 1 − 10⁻⁹) sur plus de la moitié des tâches d'un δ ; *bloque* Tables A et B pour R3.
4. **R4 dégénéré** (S12) : lecture « R4 ≈ défense figée » ; *bloque* le verdict de HR3 seulement.
5. **Optimiseur** : moyenne de (V standard − V renforcé) > 0,01 pour une règle dans un δ ; ou un contraste de la Table B qui diffère de plus de 0,01 entre attaquant standard seul et renforcé seul ; *bloque* toutes les tables.
6. **Dérive des fausses alertes** : |moyenne des fausses alertes finales d'une règle − α| > 0,001 dans un δ ; *bloque* toutes les tables.
7. **Conforme et trop propre (R4)** : P1 et P2 conformes aux deux δ **et** P7 conforme : *effet* : relecture du code par un sous-agent neuf et vérification que R2 = A et R3 = B au bit sur deux tâches de la décision (rejeu du v4 sur les mêmes graines : possible seulement par un code v2 du v4 acceptant ces racines, sinon rejeu par la boucle commune avec `v4.trajectoire` sur la copie chargée) ; *bloque* la phrase de synthèse jusqu'au rapport.

**Contenu de l'audit** : relecture du code par un sous-agent neuf ; vérification que R3 déploie les poids du programme linéaire, R1 un moniteur entraîné sur la seule dernière attaque (compte des échantillons d'entraînement), R4 la pénalité à λ* ; option : attaquant indépendant du v4 branché sur les défenses finales des quatre règles (code v2). **Issue** : « artefact trouvé » si le rapport scellé constate une erreur de code ou un chemin non exercé ; sinon « pas d'artefact ».

### Table A — contrôle de plomberie et HR1, Δ(R3, R2) sur V

| # | Condition | Verdict |
|---|---|---|
| 0 | V0 fausse | **non concluant** ; aucune lecture |
| 1 | un déclencheur qui bloque la Table A est présent et l'audit n'est pas rendu | **non concluant (audit en attente)** |
| 2 | audit rendu, artefact trouvé | **non concluant** ; version nouvelle |
| 3 | dans un δ, la moyenne de V ≤ 2α pour les quatre règles | **non concluant** : jeu dégénéré |
| 4 | est ≥ S1 ∧ borne basse B2 > 0, aux deux δ | **HR1 confirmée** (le mélange d'équilibre bat l'historique) |
| 5 | borne haute B2 < 0 dans au moins un δ | **HR1 réfutée** (l'historique bat le mélange) |
| 6 | sinon | **HR1 non démontrée** |

### Table B — classement de chaque règle k ∈ {R1, R3, R4} contre R2 sur V, à chaque δ (marge m = S1)

| Classe | Condition | Sens |
|---|---|---|
| « R_k > R2 » | borne basse B8 > m | R_k moins exploitable d'un effet d'intérêt |
| « R2 > R_k » | borne haute B8 < −m | R_k plus exploitable d'un effet d'intérêt |
| « ≈ » | E8 ⊂ ]−m ; +m[ | équivalentes à la marge près |
| « R_k ≳ R2 » | borne basse B8 > 0 | R_k meilleure, effet d'intérêt non démontré |
| « R2 ≳ R_k » | borne haute B8 < 0 | R2 meilleure, effet d'intérêt non démontré |
| « ? » | sinon | non tranché |

Verdicts : **HR2 confirmée** si « R2 > R1 » aux deux δ ; **réfutée** si « R1 > R2 », « R1 ≳ R2 » ou « ≈ » à un δ ; sinon non tranchée. **HR3 confirmée** si « R4 > R2 », « R4 ≳ R2 » ou « ≈ » aux deux δ (et S12 non déclenché) ; **réfutée** si « R2 > R4 » à un δ ; sinon non tranchée ; sous S12, « R4 ≈ défense figée », sans verdict. Les classes sont toujours recopiées, avec est [B8].

### Table C — attaques tenues à l'écart, Δ(R_k, R2) sur (ii), bornes B8, tolérance S5 (lecture par règle et par δ)

| # | Condition | Lecture |
|---|---|---|
| 1 | borne haute < −S5 | **régression avérée au-delà de la tolérance** |
| 2 | borne haute < 0 ∧ borne basse > −S5 | **régression démontrée, sous la tolérance** |
| 3 | borne haute < 0 | **régression démontrée, ampleur non tranchée** |
| 4 | borne basse > 0 | **amélioration sur (ii)** |
| 5 | borne basse > −S5 | **sans régression à S5 près** |
| 6 | sinon | **régression non exclue (imprécis)** |

HR4 : conforme pour R3 et R1 si lignes 1 à 3 aux deux δ ; conforme pour R4 si lignes 4 ou 5 aux deux δ. La lecture sans seuil (est [B8]) est recopiée dans tous les cas.

### Table D — condition d'application (R2), par δ, bornes B2, marge S15 = S1

Identique à la Table 5 du v4 (brouillon 4) : ligne 1 « R2 progresse » si borne basse de I1 > S15 ; ligne 2 « ne progresse pas, retours au-delà du hasard (cycle) » si borne haute de I1 < S15 ∧ borne basse de (I3 − 0,7345) > 0 ; ligne 3 « sans retours au-delà du hasard » si … ∧ borne haute de (I3 − 0,7345) < 0 ; ligne 4 « forme indéterminée » ; ligne 5 « indéterminé ». Verdict : condition vérifiée si lignes 2 à 4 aux deux δ. I1, I3 − nul de R1, R3, R4 recopiés sans verdict (P8, P9 descriptifs).

### Table E — coût (descriptif, sans verdict)

Par règle et par δ : processeur moyen de la trajectoire et de la finale, ratio contre R2, appels à l'optimiseur, programmes linéaires, paramètres stockés et déployés ; ordre observé recopié et comparé à P10.

**Phrase de synthèse** (lecteur R13, en recopiant, sans rien omettre) : « Table A : … ; Table B : R1 …, R3 …, R4 … (par δ, est [B8]) ; HR2 : … ; HR3 : … (S12 : …) ; Table C : … (par règle et δ, est [B8]) ; Table D : … (I1, I3 − 0,7345, I2 de R2 avec intervalles) ; R3′ : valeur du jeu restreint par tour et finale ; Table E : … ; déclencheurs : … ; issue des audits : … ; portée : résultat local au monde, à l'oracle, aux δ, à T et à λ* ».

## Liste d'arrêt

Gardes de ce module (essais nommés dans `test_arene_regles_defense_v1.py`, R5 : cas sain et artefact, motif vérifié) et gardes du v4 réemployées (essais du v4, brouillon 4 § Liste d'arrêt).

| Condition | Action | Garde et essai |
|---|---|---|
| Lancement en décision sans préenregistrement scellé, conforme, identifié (identifiant, racines, configuration, empreintes du code, de l'arène v4, du gel, de la bibliothèque, versions, N, λ*, référence) | pas de départ ; aucune graine de décision | `autoriser_decision_regles`, `exiger_identite_prereg_regles` ; `test_decision_refusee_sans_prereg_scelle`, `test_bloc_identite_et_identite_prereg_sain_et_artefacts` |
| Graine tirée d'une racine de décision sans autorisation ; racine de décision du v4 ; racine déjà employée ; plage d'une autre session ; plage du v4 ; racine non gelée ; racine tenue égale à la principale | arrêt | `gen_regles`, `exiger_racine_permise_regles`, `exiger_racines_essai_regles` ; `test_racines_sain_et_artefacts`, `test_cli_essai_refuse_racines_interdites_et_ecrasement` |
| Arène v4 absente ou modifiée (empreinte ≠ épinglée) | pas de chargement | `charger_arene_v4` ; `test_chargement_v4_empreinte_sain_et_artefacts` |
| Gel v1 absent, modifié, ou ne citant pas la racine | arrêt (mode essai) | `exiger_gel_regles` ; `test_gel_sain_et_artefacts` |
| Règle inconnue ; λ négatif ou non fini ; référence inconnue ; direction de référence nulle ; oracle autre que « détection » pour R4 | arrêt | `exiger_regle`, `exiger_lambda`, `direction_reference`, `entrainer_regularise` ; `test_regle_lambda_reference_gardes`, `test_entrainement_regularise_lambda_zero_egal_v4_et_lambda_fort_rapproche` |
| Taux de détection hors de [0 ; 1] (exploitabilité) | arrêt | `exploitabilite` ; `test_exploitabilite_sain_et_artefacts` |
| Fichier de sortie ou de PID existant | arrêt (R12) | `_exiger_absent`, `_ecrire_nouveau` du v4 ; `test_cli_essai_refuse_racines_interdites_et_ecrasement` |
| Temps processeur d'une tâche > 600 s | arrêt | `exiger_plafond` du v4 ; `test_plafond_de_temps_processeur_sain_et_artefact` |
| Fausses alertes d'une défense finale hors de α ± 0,005 ; entraînements non convergés > 0,10 par tâche ; départs non finis > 5 % ; moniteur du tour 0 non reproductible ; programme linéaire non résolu ; loi d'attaque inadmissible ; moniteur non fini ou non calibrable | arrêt | gardes du v4 (`exiger_fpr`, `exiger_convergence`, `exiger_departs_finis`, `exiger_meme_moniteur`, `resoudre_jeu`, `exiger_admissible`, `Moniteur`) ; essais du v4 ; exercées ici par `test_chaque_regle_trajectoire_T3_petite_config_en_moins_de_30_s` (cas sains) |
| Processus de travail consigné encore vivant ; signal TERM | arrêt par PID (R10), aucune reprise avant `orphelins` sain | `_lancer`, `arreter_par_pid`, `exiger_aucun_orphelin` du v4 ; `test_cli_essai_ecrit_un_pilote_minuscule_et_orphelins` |
| Attaque tenue à l'écart passée à un entraînement | constat d'essai (jamais au run) | `test_tenues_jamais_vues_par_l_entrainement` |
| R2 ≠ A ou R3 ≠ B au bit ; R4(λ = 0) ≠ R2 à code égal | constat d'essai | `test_R2_reproduit_A_du_v4_au_bit`, `test_R3_reproduit_B_du_v4_au_bit`, `test_R4_lambda_zero_egal_R2_sur_la_trajectoire_a_code_de_graine_egal` |
| Tâches ≠ 2 × N ; invocation hors § Plan 5 ; paramètre changé après lecture | V0 fausse | contrôle du lecteur R13 |
| Appel de modèle, réseau, dépense | arrêt (devis et GO exigés) | — |
| Lecture d'un résultat de décision avant scellement | arrêt et consignation (R1) | — |
| Marqueur de gabarit ou de décision de Lazar restant ; contre-lecture sans ses deux empreintes | pas de scellement | validateur `controle_ia.prereg.problemes` |

## Rôles

- Auteur : sous-agent neuf (Fable 5.1), code, essais, pilote d'essai, ce brouillon.
- **Contre-lecture (R2)** : un sous-agent neuf qui n'a écrit ni ce texte ni le code ; fichiers à lui donner explicitement : ce brouillon, `gel-regles-defense-v1.md`, `arene_regles_defense_v1.py`, `test_arene_regles_defense_v1.py`, `pilote-essai-regles-defense-v1.json` et `.md`, `LISEZMOI-regles-defense-v1.md`, `donnees/argon-seul-convergence-v1/arene_melange_v4.py`, le brouillon 4 du v4 et sa vérification. Points à juger en priorité : les prédictions ne recopient pas le pilote ; la règle de choix de λ* et sa dégénérescence (S6, S12) ; l'identité R2 = A, R3 = B ; la pénalité de R4 (sans échelle, biais libre) ; la multiplicité (B8 pour 6 tests) ; l'absence de calcul de puissance (S3) ; le remplacement de `gen` dans la copie chargée du v4.
- Lecteur de porte (R13) : sous-agent neuf, ni auteur ni contre-lecteur ; applique les Tables A à E ; verdict scellé, soumis à Lazar.
- Lazar : gèle S1 à S13 et les marqueurs ; donne le GO de l'exécution (processeur, aucune dépense).

## Contre-lecture

À REMPLIR — sous-agent neuf (identifiant), empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque (accepté, refusé et pourquoi).
