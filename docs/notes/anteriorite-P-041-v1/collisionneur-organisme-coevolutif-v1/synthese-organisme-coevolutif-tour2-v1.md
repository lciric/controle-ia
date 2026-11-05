# Synthèse — organisme coévolutif, étage III, tour 2 — v1

31 octobre 2026, 10:10 UTC. Rédacteur : session-depot (Opus 4.6). A Fable 5.1, B Opus 4.6, C Argon, D Kimi K3.1 Pro.

Pièces lues : les douze cellules de `run-organisme-coevolutif-tour2-e3-v1/cellules/` (empreintes égales à leurs compagnons) ; `question-etage3.md` ; `faits.md` (v5, 30 faits) ; `etat.md` (12 cellules OK, 8,41 USD) ; `synthese-organisme-coevolutif-v2.md` (tour 1, `1f6de90b…` — non relue en entier, sections 2 à 4 et 6 consultées pour comparaison).

## 1. Verdict

Tour exploitable : douze cellules au premier essai, aucun refus, aucune absence, 8,41 USD. La critique croisée (tour III.2) a produit une convergence majeure sur six points d'architecture : trajectoire commune du générateur aveugle ; permutation au niveau des réplications de défense (familles fixes) ; borne analytique de continuité sinon certificat non délivré ; trois jeux honnêtes disjoints ; contrôle négatif par bras réétiquetés ; banc de validation instrumentale avant toute dépense d'arène. Les quatre espèces divergent sur ce que reçoit le générateur informé, la statistique de rechute au protocole de Bailey, l'estimand du débordement et l'arrêt anticipé. Aucune espèce ne produit un préenregistrement complet qui puisse être scellé tel quel : chacun a au moins un point « illustratif » non gelé (budget, seuils, constante de Lipschitz).

## 2. Convergences nées de la critique croisée

### 2.1. Trajectoire commune du générateur aveugle

En régime aveugle, le générateur ne reçoit aucun score de défense (invariant de N-053, fait 4, VÉRIFIÉ) ; sa trajectoire est donc indépendante des défenses et peut être partagée par tous les bras. A-T3 l. 49 formule le principe : « une seule séquence de familles d'entraînement G, graine scellée, consommée par tous les bras ». C-T3 l. 35 apparie les archives cumulées. D-T3 l. 56–57 confirme. B-T3 l. 30 adopte la version faible (même archive, même ordre). Conséquence : l'état hérité devient le seul traitement de D1, non l'exposition aux familles.

### 2.2. Permutation au niveau des réplications de défense

Le plancher de valeur p à 5 grappes d'instances (1/32 ≈ 0,031) était fatal au tour III.1 sous correction de Holm (A-T2 l. 11 ; C-T2 l. 69). Les quatre corrigent :
- A-T3 l. 56–58 : K = 8 paires (Hér_k, Zéro_k), plancher 1/256, familles fixes conditionnées.
- B-T3 l. 12 : Holm retiré, un test par duel à α = 0,05, plancher 1/32 < 0,05.
- C-T3 l. 8 : P = 8 paires de graines appariées, 2^8 = 256 inversions, plancher ≈ 0,004 < α_{(1)}.
- D-T3 l. 56 : 16 paires H/Z, plancher 1/2^16.

Convergence : permutation par paire de runs appariés, familles fixes. Divergence : nombre de paires (8, 5, 8, 16).

### 2.3. Borne analytique de continuité

A-T2 l. 3 (iii) soulevait l'absence d'estimateur de la variation totale dans les certificats. Au tour III.3 :
- A-T3 l. 37 : « K doit être une borne fermée déclarée au schéma pour chaque classe. »
- C-T3 l. 10 (tableau) : « Si L_Lip > L_max ou si L_Lip·h > 0,10, le certificat est NON DÉLIVRÉ. »
- D-T3 l. 99–103 : constante de continuité vérifiée, « sans continuité, aucun certificat n'est délivré ».
- B-T3 l. 18 : accepte, mais la borne proposée porte sur θ ↦ TV(P_θ, P₀), qui ne borne pas |TPR(θ) − TPR(θ′)| (signalé par la synthèse du tour 1, section 2.7).

Convergence A, C, D : borne analytique fermée, non estimée par Monte-Carlo. B : en retard.

### 2.4. Trois jeux honnêtes disjoints

D-T1 proposait la calibration sur trois jeux. Au tour III.3 :
- A-T3 l. 91 : « n_cal tirages disjoints ; FA sur n_FA tirages disjoints ; TPR sur n_eval tirages disjoints ».
- B-T3 l. 25 : « troisième jeu honnête disjoint (calibration / évaluation FPR / test de rappel) ».
- C-T3 l. 15 (tableau) : échantillon honnête disjoint de vérification N_vérif = 50 000 (illustratif).
- D-T3 l. 95 : « divisés avant tout score en calibration, évaluation des fausses alertes et contrôles techniques ».

Convergence unanime.

### 2.5. Formule du certificat

Les quatre convergent vers L = min_grille(bornes inférieures) − terme de continuité − terme de calibration. Détails :
- A-T3 l. 70 : L = min_nœuds − K·h·√d_θ/2, avec bornes de Clopper-Pearson au niveau 1 − α_cert/N.
- B-T3 l. 96 : L = min_nœuds [borne inf. IC(rappel)] − L_lip · h, plus correction √(2 ln K)/√n_test.
- C-T3 l. 42–43 : L = min_m [R̂_LCB] − L_Lip · h − ε_cal, bornes de Šidák sur M nœuds.
- D-T3 l. 99–102 : L = min_j(ℓ_j − K h_j), bornes simultanées avec Bonferroni.

Convergence sur la structure. Divergence sur la correction de multiplicité (Bonferroni chez A et D, Šidák chez C, implicite chez B) et la propagation de l'incertitude de calibration (C seul l'ajoute explicitement).

### 2.6. Exclusion commune

A-T3 l. 92 et C-T3 l. 7 (acceptant C-b4) : « une famille non calibrée pour un bras quelconque sort de D1 pour tous les bras ». D-T3 l. 117 : « contrôle négatif ou simulation de niveau en échec : invalidation du pipeline concerné ». B-T3 l. 24 : « FPR mesuré > 1,5 % sur jeu d'évaluation → invalidation de la lecture ». Convergence implicite : l'estimand Δ porte sur un ensemble commun aux bras.

### 2.7. Plancher d'admissibilité relatif à P₀

A-T3 l. 93 : d_TV(P_f, R_f) ≥ τ_TV (illustratif 0,20). B-T3 l. 38 : TV(P_f, P₀) ≥ η_min (illustratif 0,10). C-T3 l. 17 : η_min^C = 0,85 (illustratif) dans C ; η_min^hors ∈ [0,25 ; 0,90] hors classe. D-T3 l. 90–91 : TV(P, P₀) ≥ η. Convergence unanime. Divergence sur la valeur (0,10 à 0,85 selon la strate et l'espèce) ; C est la seule à distinguer le plancher dans C (élevé, cohérent avec Neyman-Pearson) de celui hors C.

### 2.8. Familles ambiguës rapportées à part

A-T3 l. 94 : « S3 rapportée, exclue des estimands primaires ». B-T3 l. 21 : « les familles ambiguës sont rapportées à part, dans aucune des deux strates principales ». C-T3 l. 66 : strates 2 et 3 rapportées séparément. D-T3 l. 93 : « ambiguë, exclue du principal et utilisée seulement dans la sensibilité ». Convergence unanime.

### 2.9. Issue « inconclus »

A-T3 l. 34 : « renommée inconclus, sans attribution de cause ». C-T3 l. 38 : « falsifie l'hypothèse de puissance conditionnelle ex ante ». D-T3 l. 70 : « hypothèse de précision/puissance du plan falsifiée ». B-T3 l. 67 : « IC enjambant → non jugeable, falsifie la prédiction de puissance ». Convergence : un intervalle qui couvre le seuil n'est pas un verdict ; il invalide la prédiction de puissance du plan.

### 2.10. Banc de validation instrumentale avant dépense

A-T3 l. 142 : « expérience à faire en premier — validation R5 du bloc d'instruments ». B-T3 l. 155 : « établir ou réfuter la borne de continuité sur un sous-ensemble jouet ». C-T3 l. 109 : « banc de validation couplant garde, FPR randomisé, certificat jouet ». D-T3 l. 127 : « banc instrumental TV–calibration–certificat ». Convergence unanime : aucun lancement d'arène avant la réussite du banc instrumental.

## 3. Divergences non résolues

### (a) Régime informé du générateur

- A-T3 l. 78–83 : fait 9 tel quel (ni poids, ni scores, ni seuils) ; D2b lu après l'acte aveugle, dans un acte distinct.
- B-T3 l. 44 : 4e configuration lue à part ; hors du tour pour les scores (l. 80, tour 1).
- C-T3 l. 44 : scores synthétiques et architecture de la défense courante, dans l'arène, dans un rapport séparé.
- D-T3 l. 72 : même défense, mêmes régularités, séparément pour les deux régimes.

La synthèse du tour 1 (section 3, décision 3) posait déjà cette divergence et proposait fait 9 tel quel au tour 2, scores instruits à part. Rien n'est résolu.

### (b) Nombre de réplications

A : K = 8 (illustratif), 2K+1 = 17 défenses. B : I ≥ 5 grappes, 4 configurations. C : P = 8 paires, 4 défenses × 8 graines = 32 jeux de poids. D : 16 paires + 4 contrôles = 36 artefacts. Le coût de calcul est proportionnel au nombre de réplications ; aucune entrée ne le chiffre (section 6, réserve).

### (c) Estimand du débordement

- A-T3 l. 87 : Déb = moyenne par instance de TPR sur S0 − moyenne sur S1 ∪ S2, pour Hér, signe préenregistré positif.
- B-T3 l. 109 : τ_hors_C seul, comparé à la prédiction (τ_hors_C < r_min).
- C-T3 l. 62 : Δ_déb = μ_hors(D_hér) − L(C, D_hér), signe négatif (déficit de rappel hors classe).
- D-T3 l. 84 : O_H = (1 − p̂), non-détection hors classe, signe positif, seuil O_H ≥ 0,10.

Le signe même est en désaccord : A et D positif (TPR ou non-détection mesuré), C négatif (déficit par rapport au certificat), B non signé (comparaison à r_min). Le désaccord (c) du tour 1 persiste.

### (d) Arrêt anticipé

- A-T3 l. 112–125 : arrêt sur garde, sur budgets inégaux, sur validation du test, sur contrôle négatif échoué.
- B-T3 l. 127–137 : garde, FPR, contrôle négatif, budget, cyclage.
- C-T3 l. 88–96 : garde, déséquilibre des compteurs, quota non atteint, FPR, diagnostics consignés sans arrêt.
- D-T3 l. 116–117 : fuite, budget, contrôle négatif, admission, continuité ; « résultat anormalement propre : audit identique ».

Convergence : garde = arrêt immédiat. Divergence : C et D ne prévoient pas d'arrêt sur diagnostics (durée fixe T) ; A garde un E_arrêt diagnostique.

### (e) Zone (0, δ) de l'intervalle

A-T3 l. 34 : « les deux → effet réel sous la marge » (falsifie H_A et H_B). C-T3 l. 38 : « falsifie l'hypothèse de puissance conditionnelle ». D-T3 l. 70 : « hypothèse de précision/puissance du plan falsifiée ». B-T3 l. 67 : « non jugeable ». Le vocabulaire diffère ; le fond converge vers « non conclusif ».

### (f) Pilote

A-T3 l. 99–101 : « simulation sur monde simulé qui fixe δ_H et m_min » ; « pilote puis décisif ». D-T3 l. 107 : « analyse de scénarios, lois explicitement HYPOTHÈSE ». B, C : fixation avant scellement sur simulation de puissance. Non résolu.

## 4. Apports d'une seule espèce

| Apport | Source |
|---|---|
| Corrélation partielle (à d_TV donné) comme diagnostic, non arrêt | A-T3 l. 106 |
| Strate « inexprimable » (classe hors liste, R_f := R) | A-T3 l. 92 (via C-a2) |
| Trajectoire commune formulée comme architecture | A-T3 l. 49 |
| Contrôle de faisabilité du certificat (min_C d_TV < L_min → infaisable) | A-T3 l. 67 |
| Pente de la répartition sous P₀ au quantile 0,99 | B-T3 implicite, via B-T1 |
| Non-jugeabilité si > 50 % familles saturées | B-T2 l. 24 |
| Diagnostic de cyclage sur fenêtre T/2 | B-T3 l. 56 |
| Variation totale par rapport de vraisemblance exact (lois synthétiques à densité) | C-T3 l. 16 |
| Plancher dans C à η_min^C = 0,85 (cohérent avec Neyman-Pearson et τ_cert = 0,80) | C-T3 l. 17 |
| Correction séquentielle des diagnostics IOR, IDM | C-T3 l. 18 |
| Indice de dérive multi-pas IDM_t | C-T3 l. 80 |
| 36 artefacts dans la liste scellée (empreintes individuelles) | D-T3 l. 111 |
| Estimation conditionnelle aux familles fixes, sans prétention de généralisation | D-T3 l. 120 |
| Archive reconstruite depuis le flux complet scellé | D-T3 (via tour 1, section 4) |
| Test de faisabilité géométrique (TV(P, P₀) ≥ ρ − 0,01 sur C) | D-T3 (via C-a4) |

## 5. Noyau consensuel pour le préenregistrement P-041

### Architecture

- Trajectoire commune G : une séquence de familles d'entraînement, graine scellée, consommée par tous les bras (unanime).
- Bras : K paires appariées (Hér_k, Zéro_k) à trajectoire identique, seule différence la réinitialisation des poids (A, C, D) ; K ≥ 8 (illustratif) pour plancher de valeur p < 0,004 sous Holm.
- Point de contrôle final, sans sélection (unanime).
- Acte unique exécuté par un sous-agent neuf (fait 5, unanime).

### Duels

- D1 (héritage contre zéro, hors classe) : H_A : Δ ≥ δ_H ; H_B : Δ ≤ 0 ; intervalle couvrant les deux → « inconclus ». Permutation par retournement de signe des K différences Δ_k.
- D2a (certificat, régime aveugle) : L = min_grille(bornes inférieures simultanées) − K·h − ε_cal. Non délivré si la borne de continuité fait défaut.
- D2b (certificat, régime informé) : même formule, lu et rapporté à part (A, C, D).

### Métriques

- Taux de détection à 1 % de fausses alertes.
- Trois jeux honnêtes disjoints (calibration, vérification du taux de fausses alertes, test).
- Plancher d'admissibilité relatif à P₀ et à la classe.
- Familles ambiguës rapportées à part, exclues des estimands primaires.
- Exclusion commune si non-calibration pour un bras quelconque.

### Contrôles négatifs

- Bras identiques réétiquetés (contrôle de D1).
- Certificat sur boîte jouet à pire cas analytique hors nœuds, avec artefact de K sous-estimé.
- Défense triviale (rappel analytiquement borné par α).
- Validation du test de permutation sous H₀ exacte (taille ≤ α + 0,01).
- Famille plantée P₀ dans le lot hors classe (exclue du principal).

### À trancher par Lazar

- Nombre de réplications K (divergence (b)).
- Estimand du débordement (divergence (c)).
- Ce que reçoit le générateur informé (divergence (a) ; proposition : fait 9 tel quel au tour 2, scores à part).
- Budget de calcul et seuils numériques (non chiffrés par aucune entrée).
- Pilote ou non (divergence (f)).

## 6. Réserves

- **R4 (trop propre)** : quatre héritages positifs au signe de P-041, quatre x = 0,80, quatre transferts « positifs mais dégradés ». Le tour 1 (v2, section 7) l'avait déjà signalé.
- **Borne de régularité** : les conditions d'explosion de la grille (C-T2 l. 26 ; A-T3 l. 25) montrent que pour d_θ ≥ 10, le certificat risque d'être structurellement non délivrable. Aucune entrée ne chiffre le coût en dimension.
- **Familles tierces hypothétiques** : les cinq instances tierces sont RAPPORTÉ (fait 10) ; elles n'existent pas encore.
- **Budget non chiffré** : le tour 1 (v2, section 6, décision 5) signalait déjà l'absence ; les quatre entrées du tour 2 ne le calculent pas non plus.
- **Rédacteur** de la même famille que B (Opus 4.6) ; contre-lecture par une autre famille recommandée (R2).
- **Contre-lecture non faite** de cette synthèse.
