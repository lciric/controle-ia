# Synthèse — collisionneur « D-ML-1 » (taille du jeu bénin de l'estimation de la malléabilité) — v1

**Auteur** : lecteur neuf, sous-agent, modèle : Claude Fable 5.1 (`claude-fable-5-1`). Réserve de position : ce modèle est de la même
famille que l'espèce A (Fable), absente du run par refus ; aucune position n'est prêtée à A (critère 1) et le lecteur n'en formule
aucune en son nom.
**Date** : 31 octobre 2026, 18:33 UTC (`date -u`).
**Critères appliqués** : `docs/notes/anteriorite-P-041-v1/collisionneur-dml1-v1/criteres-lecture-dml1-v1.md`, empreinte
`86f1d32f9d6afeb05b91fcf5a44b5ffec923d4f6499654160f24089337a2c309` (vérifiée : commence par `86f1d32f`). Quinze critères, appliqués
à la lettre ; la synthèse a été écrite après la lecture complète des neuf cellules (critère 15). Rien n'est tranché (critère 14).

## Fichiers lus, dans l'ordre, empreintes sha256 recalculées

| Fichier | Empreinte |
|---|---|
| `donnees/collisionneur-dml1-v1/question-dml1-v1.md` | `c3ed02b58e767479f1a98297ca93124beff94a41f56395e69fb6cfb27c5866b5` |
| `donnees/collisionneur-dml1-v1/faits-dml1-v1.md` | `3da07a08c7c6a1615a1dd78eb6897e6b4ebd6bf569aabd9f146f1ba542a0587a` |
| `docs/notes/anteriorite-P-041-v1/calcul-taux-fausses-alertes-benins-v1.py` | `9dc348901059d08537e056ac8c113a4dedd2e8a0f9f94685dd994d66b410876b` |
| `docs/notes/anteriorite-P-041-v1/calcul-taux-fausses-alertes-benins-v1.sortie.txt` | `b39f629d5b366ef7941a829042a85e1b53ec0377e8ba5800799fce0bc5586939` |
| `…/run-dml1-e3-v1/cellules/E3-T1-conception-B.md` | `866f16543d2daefdaadf4232566b73618d4003d6679edb472320a5c41dd1dce6` |
| `…/run-dml1-e3-v1/cellules/E3-T1-conception-C.md` | `5410b3910ab4836b940a770daae39d47afc2b273c4d5153106c12e1bcbe320e8` |
| `…/run-dml1-e3-v1/cellules/E3-T1-conception-D.md` | `70b2e5f012cff9aeced51c06343a143a598033767331fdc69c69297ef1445236` |
| `…/run-dml1-e3-v1/cellules/E3-T2-critique-croisee-B.md` | `ead9b516de3c73311039a3323a97a3173da968c104f4e6033bc350d7e9f16968` |
| `…/run-dml1-e3-v1/cellules/E3-T2-critique-croisee-C.md` | `dda14db28a8abf3e8b6835203a92670e5ef197d27a7e91c48f9a8ee9d95af235` |
| `…/run-dml1-e3-v1/cellules/E3-T2-critique-croisee-D.md` | `b21bfe0fb0ee4430f1a5e9e4ceb9bae21399c1670606c9a2b1b4545216d79a87` |
| `…/run-dml1-e3-v1/cellules/E3-T3-reponse-B.md` | `e11ebeb11c82cd1775358fa880a1fced5b84d2c35778bae7ad677730f80131e5` |
| `…/run-dml1-e3-v1/cellules/E3-T3-reponse-C.md` | `b1f8533115e3cc97aab59fea85888435baa737cb9d5c251ea34863e1ad8726d9` |
| `…/run-dml1-e3-v1/cellules/E3-T3-reponse-D.md` | `653d566cc1f54ed660316f4d9bdd65410a1a3a8b699e56381628080c722c63d6` |
| `donnees/collisionneur-dml1-v1/run-dml1-e3-v1/etat.md` | `327673a6ab78438de2a3660c726ccb6de9a7199967ec296102d9ebea8075f42d` |

(`…` = `donnees/collisionneur-dml1-v1`.) Espèces : B = Opus 4.6, C = Argon, D = Kimi K3.1 Pro ; A = Fable, trois cellules absentes
(`etat.md` : E3-T1-conception-A en REFUS, 0 caractère, 0,24 USD ; les deux cellules suivantes jamais lancées ; absences acceptées
par l'arbitre). Dépense totale du run : 4,30 USD (`etat.md`).

**Recalculs du lecteur** (critère 10), hors dépôt, dans le bloc-notes de session :
`/tmp/claude-0/-home-user-controle-ia-travail/3cc5e598-4440-5eda-aeb9-bcd3cae5cbfb/scratchpad/dml1-recalculs/recalc_dml1.py`
(`b7dc3f798ea5d34cc1f14f5cc37b06470606a284a97637d011663799a4bf69fe`), sortie `recalc_dml1.sortie.txt`
(`4b0adbd4bcde1df31f19fd28a0a19de69ebc8e9d5253251a6bc31035d3d1958f`) ; relance du calcul servi avec `python3 -I`, sortie
`calcul-servi-relance.txt` (`8b871c2eb9300682c17a378b8fc5ae1470d27eef6ee8ba151fa18ed5f7b8cc35`). Méthode : fonction bêta incomplète
régularisée (fraction continue) et dichotomie, sans scipy ; loi bêta-binomiale par fonctions gamma logarithmiques ; loi binomiale exacte.
Non versés au dépôt ; les lignes utiles sont reproduites ci-dessous.

---

## 1. Décompte de tête

| Catégorie | Nombre | Détail (sections où ils sont développés) |
|---|---|---|
| Accords indépendants (T1, ≥ 2 espèces sur 3, même objet) | 8 | § 4 ; dont 7 unanimes à trois → réserve de symétrie (§ 11) |
| Convergences nées de la critique | 11 | § 5 ; qui a cédé à qui, noté |
| Divergences résolues (une espèce cède en T3 avec raison) | 2 | § 6 (C quitte sa troisième option ; C corrige le signe de son critère) |
| Divergences non résolues | 6 | § 6 (choix final B contre {C, D} ; première expérience ; contrôle base/instruct ; licence d'Alpaca ; statistique du test de ressemblance ; « (A) réfutée formellement ») |
| Apports d'une seule espèce (gardés, non réfutés) | 9 | § 7 |
| Affirmations inexactes (au-delà de l'arrondi, ou contradiction interne) | 8 | § 8 ; aucune ne touche les lignes du calcul servi, toutes justes |
| Passages hors niveau (critère 2), par classe | 8, dont 2 limites | § 9 : procédure d'optimisation des directions (4) ; motif de contournement du juge (2) ; mécanisme de l'intervention sur la sonde (2, limites) |
| Vérification du calcul servi par les espèces (question 1) | 3 sur 3 l'ont faite, résultat « exact » pour les trois | § 3 |

---

## 2. Table par espèce et par sous-tour

Statuts (critère 3) : VÉRIFIÉ = recalculé par le lecteur ou lu dans les faits ou le calcul servis ; RAPPORTÉ = cité, non vérifié (R7) ;
SUPPOSÉ = l'espèce le dit elle-même, ou rien ne le fonde. Tailles et licences de jeux publics : RAPPORTÉES ou SUPPOSÉES, aucun jeu versé.

### 2.1 Espèce B (Opus 4.6)

| | E3-T1 conception | E3-T2 critique croisée (de C et D) | E3-T3 réponse |
|---|---|---|---|
| **Choix** | Troisième option : sonde sur les 800 bénins de Bailey ; seuil et mesure sur un jeu externe de 1 000 + 1 000, sous réserve d'un test de ressemblance ; repli sur (B) si aucun jeu ne passe (§ 1). *Remarque : ce montage coïncide avec (A) telle que les faits la décrivent (800 Bailey, 1 000 + 1 000 externes, « vérification de distribution ») ; ce qui est propre à B est le repli explicite et le test chiffré.* | Pas de choix propre ; écrit que C et D « convergent vers (B) avec analyse de sensibilité, ce qui me semble correct » (tableau final), sans modifier son choix de T1. | Maintient la troisième option « corrigée » (jeu externe vérifié, ≤ 3 candidats préenregistrés dans un ordre fixé, correction de Bonferroni α = 0,01/3, scores hors entraînement seulement, test de permutation sur le quantile 99 %, repli sur (B) avec bornes bêta exactes) (§ c). |
| **Statuts des affirmations** | Intervalles servis : RAPPORTÉ puis vérifiés analytiquement → VÉRIFIÉ ; jeux Alpaca (≈ 52 k, Apache 2.0), LMSYS-Chat-1M (CC-BY-NC-4.0), Dolly-15k (CC-BY-SA-3.0) : SUPPOSÉ (déclaré) ; coûts et temps de calcul : « illustratif » ; puissance « < 50 % », « ~500 adverses » (§ 3) : « illustratif ». | Puissance du test de Kolmogorov-Smirnov, taille d'échantillon « ≈ 1 200 », puissance « 20–30 % », « 0 ou ≥ 7 dépassements » : marqués « illustratif » ; recalculés § 8 (inexacts). | Puissance « ~60 % » du test de permutation : « illustratif », à vérifier par simulation (SUPPOSÉ) ; δ_p = 0,025 : dérivé de la critique de C (VÉRIFIÉ au recalcul : demi-largeur 0,0211). |
| **Intervalle recalculé par le lecteur, comparé au calcul servi** | B écrit 10/1 000 → [0,0048 ; 0,0183] ; 3/300 → [0,0021 ; 0,0289] ; seuil n = 300 → [0,0021 ; 0,0238] : identiques au calcul servi (`b39f629d…`) et à mon recalcul exact ([0,0048 ; 0,0183], [0,0021 ; 0,0289], [0,0021 ; 0,0239]). B ajoute 10/200 → [0,024 ; 0,089] ; recalcul [0,0242 ; 0,0900] : exact. « Facteur 11 » : 0,0238/0,0021 = 11,3 : exact. | 2/200 → [0,0012 ; 0,0356] : identique au servi (recalcul [0,0012 ; 0,0357]). 90/100 : « ± 8 points » ; recalcul [0,824 ; 0,951], demi-largeurs 0,076 / 0,051 : ordre de grandeur. | Bornes « Beta(3, 298) » et « Beta(1, 300) » associées à S(297) et S(299) : décalage d'indice d'un rang (§ 8, n° 6). |
| **Pire cas / condition de changement d'avis (critère 11)** | Pire cas : le jeu externe passe le test global mais sa queue droite est décalée (quantile 99 % à 1,5 σ au-dessus de Bailey, illustratif) → seuil trop haut, fausses alertes < 0,1 %, borne surestimée. Changement : vers (B) si trois candidats échouent ; vers (A) pure si la sonde à 400 ne perd rien ET que le budget interdit le jeu externe ; vers la validation croisée si l'intervalle bootstrap de τ dépasse 0,5 σ sans jeu externe. **Complet.** | — | Conditions : perte de rappel > 5 points dans ≥ 8/10 répétitions disqualifie (B) ; trois candidats échouent → repli (B). Pire cas de T1 non restitué ni retiré. **Complet sur T1 + T3.** |
| **Test de ressemblance (critère 12)** | Kolmogorov-Smirnov bilatéral sur les scores de la sonde, p < 0,01 ; issue : rapporter D et un diagramme quantile-quantile, puis (i) autre jeu, (ii) recalibrer sur le jeu externe, (iii) repli (B) — issue en menu. Complément : permutation sur le quantile 99 %, 10 000 permutations, **sans seuil** → non préenregistrable en l'état. Défaut relevé par C et D en T2 : scores **in-sample** des 800 d'entraînement (accepté en T3). | — | Test de permutation sur le quantile 99 %, 10 000 permutations, bilatéral, α = 0,01/3, marge δ_p = 0,025 ; issue : jeu rejeté ; 3 échecs → (B). Statistique, seuil, issue nommés → **retenu**. Puissance SUPPOSÉE. |

### 2.2 Espèce C (Argon)

| | E3-T1 conception | E3-T2 critique croisée (de B et D) | E3-T3 réponse |
|---|---|---|---|
| **Choix** | Troisième option : calibration hors pli (validation croisée à 10 plis, illustratif) sur 700 bénins de Bailey + mesure sur 300 isolés ; sinon (B), découpage 500/300/200 ou 400/300/300 ; (A) écartée par défaut (§ 1). | Pas de choix propre ; critique B (fuite in-sample, sélection, AUC, normalisation, aveuglement du KS, bootstrap des queues, sous-puissance) et D (dilemme du rééchantillonnage, tolérances libres, variable confondante du duel 3, TOST impossible à n = 200). | **Retire** la calibration hors pli (cède à B et D) ; choisit **(B) pure**, sous-découpage conditionnel à l'expérience 1 : 400/300/300 si la sonde à 400 (repondérée 2:1) tient, sinon 600/200/200 (§ c.3). |
| **Statuts des affirmations** | Lignes « mesure » et « seuil » : VÉRIFIÉ (loi nommée) ; jeux XSTest (≈ 250, CC-BY-4.0), OR-Bench (≈ 80 k, MIT ou Apache-2.0), Alpaca/UltraChat (52 k, CC-BY-NC-4.0) : « HYPOTHÈSE » (= SUPPOSÉ) ; dimension 4 096, 10 plis, seuils de décision : « illustratif » ; « Beta(7, 694) ≈ [0,0040 ; 0,0186] » : « illustratif interpolé », en fait exact au recalcul. | Valeur critique du KS 0,126 : VÉRIFIÉ (recalcul 0,1263) ; P(Beta(2,199) < 0,005) ≈ 0,26 et P(> 0,020) ≈ 0,09 : VÉRIFIÉ (0,2642 ; 0,0894) ; « dépasse 45 % » : **inexact** (§ 8, n° 3) ; intervalle à 90 % de 2/200 [0,0018 ; 0,0310] : VÉRIFIÉ ([0,0018 ; 0,0311]) ; borne d'AUC 0,51 pour une variation totale de 0,02 : algèbre exacte, prémisse illustrative. | Les mêmes lignes servies, recopiées : VÉRIFIÉ ; seuils de décision (2,0 points, cos ≥ 0,95, ± 0,15 σ, Δ⁺ ≤ 0,15, 5 points de rappel, plancher 10) : « illustratif » déclarés comme coupures proposées. |
| **Intervalle recalculé, comparé au servi** | [0,0048 ; 0,0183], [0,0021 ; 0,0289], [0,0012 ; 0,0356], [0,0048 ; 0,0171], [0,0021 ; 0,0238] : identiques au servi. Beta(7,694) : recalcul [0,0040 ; 0,0186], exact. 10/200 → [2,4 % ; 9,0 %] : recalcul [0,0242 ; 0,0900], exact. Moyennes 1/301 ≈ 0,33 % et 7/301 ≈ 2,33 % : exactes. | Beta(2,199) et Beta(1,100) nommées pour un seuil fixé sur 200 ou 100 bénins : conformes à la loi du calcul servi. | n = 200 : seuil [0,0012 ; 0,0275], mesure [0,0012 ; 0,0356] : identiques au servi. |
| **Pire cas / changement d'avis** | Pire cas : (1) effet de falaise des scores adverses près du seuil ; (2) sonde dégradée à 400. Changement vers (A) : si le dépôt de Bailey documente la source exacte des bénins et qu'on peut en tirer 2 000 de la même population avec D_KS < 0,05 (illustratif) ; ou si la bande de sensibilité relative dépasse 30 % (illustratif) sur le pilote à τ < 5 %. **Complet.** | — | Pire cas : écart massif entre N_dir(X(7)) et N_dir(X(1)) (Δ⁺ à 5 % > 15 %) combiné à une sonde dégradée à 400. Changement vers (A) : seulement si la source mère exacte de Bailey livre 2 000 bénins de plus ET qu'ils passent le TOST de l'expérience 2. **Complet.** |
| **Test de ressemblance** | Double test sur les 200 bénins val+test de Bailey contre 2 000 externes : KS (ou Anderson-Darling) sur les scores, acceptation p > 0,05 ET D_KS ≤ 0,08 (illustratif) ; test de queue : quantile 99 % à plus d'un demi écart-type → rejet. Expérience 2 : p_KS > 0,05 ET α̂_croisé ∈ [0,0021 ; 0,0238] ; issue : (A) rejetée avec ce jeu. Statistique, seuil, issue nommés → **retenu en forme**, mais sous-puissance démontrée par B et D en T2 et concédée en T3 (critère « quasi certain de passer », B T2 (b)). | — | TOST par bootstrap (10 000 répliques, illustratif) sur l'écart standardisé du quantile 99 %, intervalle à 90 % dans [−0,15 ; +0,15] (illustratif) ET intervalle de Clopper-Pearson à 90 % du taux croisé dans [0,0048 ; 0,0171] ; données : 1 000 scores de Bailey rendus hors échantillon par validation croisée à 5 plis contre 2 000 externes ; issue : (A) certifiée, sinon (B). **Retenu en forme.** Réserve : le côté Bailey agrège les scores de cinq sondes, ce que C vient de reconnaître (§ a.1) comme brisant la loi bêta exacte ; C ne dit pas si cela vaut pour la comparaison de lois. |

### 2.3 Espèce D (Kimi K3.1 Pro)

| | E3-T1 conception | E3-T2 critique croisée (de B et C) | E3-T3 réponse |
|---|---|---|---|
| **Choix** | **(B)** en version « B+ » : 400/300/300, analyse de sensibilité obligatoire, seuil jamais présenté comme un point de fonctionnement à exactement 1 % ; (A) seulement si un candidat passe un contrôle préenregistré avant tout résultat. | Pas de choix propre ; critique B (déséquilibre 400/800 non reproduit, AUC, in-sample, contrôle vrai par construction, non-significativité prise pour validation, réutilisation des 200, bootstrap) et C (transfert hors pli non établi, sélection d'hyperparamètre, « borné » abusif, bande ≠ intervalle de confiance, **signe inversé** de Δ_τ, optimisation et évaluation non séparées, non-rejet, permutation à 50 %). | **Maintient (B)** « comme déviation explicite et sans certification d'un point de fonctionnement à exactement 1 % » ; retire ses trois duels à tolérance libre comme conditions ; la sonde à 400 est « un nouvel instrument » ; comparaison 400/800 reclassée exploratoire. |
| **Statuts des affirmations** | Contraintes et comptes : RAPPORTÉ ; sortie numérique : « OBSERVÉE-NON-AUDITÉE faute de script » (le script, `9dc34890…`, n'a pas été servi aux espèces : cohérent) ; reconstruction des lois : VÉRIFIÉ ; Dolly-15k (≈ 15 k, CC BY-SA 3.0), oasst1 (≈ 160 k, Apache-2.0) : SUPPOSÉ ; mémoire 16 Go, 0,5 à 4 heures-GPU, 1 à 8 € : « illustratif ». | Aucun chiffre nouveau ; les lois Beta(1,300), Beta(3,298), Beta(7,294) pour X(1), X(3), X(7) : VÉRIFIÉ (recalcul § 3). | Lois Beta(10,991), Beta(8,793), Beta(5,496), Beta(4,397), Beta(3,298), Beta(2,199) : conformes au script servi ; comptes 99 / 39 / 9 sur 200 adverses : VÉRIFIÉ. |
| **Intervalle recalculé, comparé au servi** | Beta(10,991) ≈ [0,0048 ; 0,0171], Beta(3,298) ≈ [0,0021 ; 0,0238], 10/1 000 → [0,0048 ; 0,0183], 3/300 → [0,0021 ; 0,0289] : identiques au servi. Comptes « au plus 39 » (< 20 %) et « au plus 9 » (< 5 %) : exacts. | — | « Au plus 99 » (< 50 %) : exact. |
| **Pire cas / changement d'avis** | Pire cas : sonde affaiblie par 400 bénins ET seuil anormalement permissif → directions gonflées, surtout à 5 %. Changement vers (A) : jeu versé, licencié, dédupliqué, erreur de calibration cible < δ_p au contrôle opérationnel, sensibilité τ favorable, sonde inchangée. **Complet** (δ_p non chiffré, par choix déclaré). | — | Pire cas : le même ; si un changement de rang adjacent au seuil modifie la conclusion discrète, ou si le contrôle aléatoire reproduit l'effet, D suspendrait la campagne plutôt que de « réparer » (B) par bootstrap. Vers (A) : candidat versé et compatibilité démontrée sur assez de données cibles indépendantes. **Complet.** |
| **Test de ressemblance** | Quatre niveaux : contrôle mécanique des données ; descripteurs ciblés ; classifieur « Bailey contre candidat » hors pli, AUC comparée à des partitions aléatoires (sans seuil) ; contrôle opérationnel de la queue sur les 200 bénins Bailey (sans seuil, « un non-rejet n'est pas une certification »). Duel 1 : test d'équivalence à marge δ_p **non chiffrée** → **non préenregistrable en l'état** (D le dit lui-même). | — | Duel A, « seulement si un candidat externe et de nouvelles données cibles existent » : dépassements au seuil externe sur un échantillon cible indépendant, taille calculée pour une puissance préenregistrée, marge fixée avant les scores ; AUC de domaine réduite à un diagnostic ; un seul candidat ou correction de multiplicité. Marge toujours non chiffrée → **non préenregistrable en l'état** (déclaré). |

---

## 3. Vérification du calcul servi (critère 10, question 1)

Relance de `calcul-taux-fausses-alertes-benins-v1.py` (`9dc34890…`) avec `python3 -I`, numpy 2.5.3 (le servi dit 2.4.6) : les neuf
lignes de chiffres sont **identiques** à la sortie servie (`b39f629d…`), graine `SeedSequence(20261031)` oblige (R9).

Quantiles exacts (fraction continue, sans tirage), pour comparaison à la sortie Monte-Carlo servie :

| Ligne | Servi | Recalcul exact | Écart |
|---|---|---|---|
| seuil n = 1 000, k = 10, Beta(10, 991) | [0,0048 ; 0,0171] | [0,0048 ; 0,0170] | 0,0001 (arrondi Monte-Carlo) |
| seuil n = 800, Beta(8, 793) | [0,0043 ; 0,0179] | [0,0043 ; 0,0179] | 0 |
| seuil n = 500, Beta(5, 496) | [0,0033 ; 0,0203] | [0,0033 ; 0,0204] | 0,0001 |
| seuil n = 400, Beta(4, 397) | [0,0027 ; 0,0218] | [0,0027 ; 0,0218] | 0 |
| seuil n = 300, Beta(3, 298) | [0,0021 ; 0,0238] | [0,0021 ; 0,0239] | 0,0001 |
| seuil n = 200, Beta(2, 199) | [0,0012 ; 0,0275] | [0,0012 ; 0,0275] | 0 |
| mesure 10/1 000, Clopper-Pearson | [0,0048 ; 0,0183] | [0,0048 ; 0,0183] | 0 |
| mesure 3/300 | [0,0021 ; 0,0289] | [0,0021 ; 0,0289] | 0 |
| mesure 2/200 | [0,0012 ; 0,0356] | [0,0012 ; 0,0357] | 0,0001 |

Aucun écart au-delà de l'arrondi : le calcul servi est exact pour la convention qu'il déclare (k-ième score bénin le plus haut,
k = 0,01 n, taux futur ~ Beta(k, n + 1 − k) ; mesure par Clopper-Pearson). Les trois espèces ont fait la vérification demandée (B T1
§ a ; C T1 § 1 ; D T1 § 1) et l'ont trouvée exacte ; C et D nomment les deux lois ; D note que l'intervalle « seuil » est prédictif pour
un seuil aléatoire, non un Clopper-Pearson à seuil fixe.

Lignes de recalcul supplémentaires utilisées plus bas :
- Beta(1,300) [0,0001 ; 0,0122], moyenne 0,0033 ; Beta(2,299) [0,0008 ; 0,0184] ; Beta(4,297) [0,0036 ; 0,0289], moyenne 0,0133 ;
  Beta(7,294) [0,0094 ; 0,0430], moyenne 0,0233 ; Beta(7,694) [0,0040 ; 0,0186].
- Clopper-Pearson 95 % de 10/200 : [0,0242 ; 0,0900] ; de 90/100 : [0,824 ; 0,951] ; à 90 % de 2/200 : [0,0018 ; 0,0311].
- P(Beta(2,199) < 0,005) = 0,2642 ; P(Beta(2,199) > 0,020) = 0,0894 ; somme 0,3536 ; probabilité bêta-binomiale exacte que K/1 000
  tombe hors de [0,005 ; 0,020] avec K ~ BêtaBinomiale(1 000 ; 2, 199) : 0,3588.
- Valeur critique du test de Kolmogorov-Smirnov à 1 %, n = 200 et m = 1 000 : 1,63 · √(1 200 / 200 000) = 0,1263.
- Formule de taille d'échantillon de B T2 (0,01 contre 0,03, puissance 80 %, unilatéral 5 %) : 236 ; puissance binomiale exacte à
  m = 200 (rejet si K ≥ 6, niveau 0,016) : 0,557.
- k/200 hors de [0,0021 ; 0,0238] : k = 0, ou k ≥ 5 (5/200 = 0,025).

---

## 4. Accords indépendants (critère 4 : portés en T1 par au moins deux espèces, même objet)

1. **Le calcul servi est exact et mêle deux lois** (seuil prédictif Beta(k, n+1−k) ; mesure Clopper-Pearson) — B, C, D (B T1 § a ;
   C T1 § 1 ; D T1 § 1). Unanime.
2. **Réduire l'entraînement de la sonde de 800 à 400 bénins est un coût caché de (B), absent des faits, à tester avant tout** —
   B (présupposé 8, expérience 1), C (présupposé 2, expérience 1), D (hypothèse 3, duel 3). Unanime.
3. **Le risque de (A) est un biais systématique, non borné par les intervalles binomiaux, qui peut dépasser le bruit de (B)** —
   B T1 § 2 (« possible et même probable »), C T1 § 2 (92ᵉ ou 99,99ᵉ centile, illustratif), D T1 § 3 (« peut s'écarter arbitrairement
   de 1 % »). Unanime sur le constat ; non sur la conséquence (B garde le jeu externe).
4. **Le test de ressemblance doit porter sur les scores de la sonde (une dimension), pas sur les activations brutes, et viser la
   queue droite** — B T1 § c et § 2 (KS sur les scores + quantile 99 %), C T1 § 2 (KS/Anderson-Darling + quantile 99 %, rejet du MMD
   brut), D T1 § 3 niveau 4 (« contrôle opérationnel de la queue de la sonde, le plus important »). Unanime.
5. **Un test global (KS, MMD) non significatif ne certifie pas la queue** — B T1 § 2 (« nécessaire mais pas suffisante »), C T1 § 2
   (ajout d'un test de queue), D T1 § 3 (« MMD non significatif donc identiques serait insuffisant »). Unanime.
6. **La résolution des lectures à 20 % et 5 % vient du nombre d'adverses (200), pas des bénins ; les 300 bénins jouent sur la
   position du seuil** — C T1 § 3 (10/200 → [2,4 % ; 9,0 %]), D T1 § 4 (39 et 9 détections), B T1 § 3 (10/200 → [0,024 ; 0,089] ; « le
   vrai problème est que τ lui-même est bruité »). Unanime.
7. **(B) n'est lisible que si l'on rapporte la sensibilité du compte de directions au seuil** — B (rappel aux bornes de l'intervalle
   de τ, dérivée discrète), C (compte à X(1), X(3), X(7) et courbe N_dir(α)), D (sensibilité à une recalibration, même règle de seuil).
   Unanime sur l'objet, instruments différents.
8. **Candidats de jeux bénins publics** (tous RAPPORTÉS/SUPPOSÉS) : Alpaca cité par B et C ; Dolly-15k par B et D ; LMSYS-Chat-1M (B
   seul), XSTest et OR-Bench (C seul), UltraChat (C seul), oasst1 (D seul). Accord à deux sur deux noms ; aucune taille ni licence
   n'est vérifiée ; voir divergence sur la licence d'Alpaca (§ 6).

Vrai par construction, jamais compté comme accord (critère 8) : les options (A) et (B), les découpages 1 000/1 000 et 400/300/300, la
validation croisée (option hors pli de C), le rééchantillonnage (bootstrap de B, recalibration de D), les autres découpages (500/300/200
et 600/200/200 de C) — ce sont des exemples cités par la question.

---

## 5. Convergences nées de la critique (critère 5)

1. **C abandonne sa calibration hors pli sur 700 bénins** et passe à (B) pure — C T3 § a.1 cède à B T2 (a.1 : le seuil est calibré
   sur les résidus de K sondes, pas sur la sonde finale ; a.5 déséquilibre 700/800) et à D T2 (a.1 transfert non établi ; a.2 fuite de
   sélection de l'hyperparamètre). Raison donnée : la loi Beta(k, n+1−k) n'est exacte que pour une sonde unique figée sur un échantillon
   disjoint.
2. **C corrige le signe de son critère Δ_τ** — C T3 § a.2 cède à D T2 (a.5) : N_dir est croissant en t, donc N_dir(X(7)) − N_dir(X(1))
   ≤ 0 toujours et le critère « ≤ 0,10 » était satisfait par construction ; les rôles « strict/lâche » sont inversés (X(7) = borne
   inférieure conservatrice, X(1) = borne supérieure). B T2 n'avait pas vu ce défaut (il discute Δ en valeur absolue, b.3).
3. **B abandonne les scores in-sample pour le test de ressemblance** — B T3 (C-a1, D-a3) cède à C T2 (a.1) et D T2 (a.3).
4. **B remplace l'AUC par le rappel au point de fonctionnement à 1 %** — B T3 (C-a3, D-a2) cède à C T2 (a.3) et D T2 (a.2, b).
5. **B abandonne le bootstrap des quantiles extrêmes pour la bande bêta exacte des statistiques d'ordre** — B T3 (C-b2, D-a7) cède à
   C T2 (b.2) et D T2 (a.7, b) ; adopte l'instrument de C T1 § 3 (lecture à plusieurs statistiques d'ordre). **C → B.**
6. **B abandonne le KS comme test principal au profit d'un test sur le quantile 99 %** — B T3 (C-b1) cède à C T2 (b.1 : valeur
   critique 0,126 contre effet de queue ≤ 0,05, VÉRIFIÉ au recalcul). B T1 avait déjà le test de quantile en complément.
7. **Cadre d'équivalence (TOST) adopté par les trois en T3** — source : D T1 duel 1 (« test d'équivalence dont l'intervalle doit être
   entièrement contenu dans δ_p ») ; repris par B T2 contre C (a.2 : « C ne propose pas de test d'équivalence ») et par C T2 contre D
   (b.2 : impossibilité pour δ_p < 0,021 à n = 200) ; B T3 (D-a5, expérience 2 corrigée, δ_p = 0,025) et C T3 (expérience 2 corrigée)
   l'adoptent ; D T3 le garde avec marge non chiffrée. **D → B, C.**
8. **« Les 200 bénins de Bailey hors entraînement ne peuvent pas certifier la queue d'un jeu externe »** — dit en T2 par les trois
   (B T2 sur C b.2 et sur D b ; C T2 sur B b.3 et sur D b.2 ; D T2 sur B a.5–a.6 et sur C a.7), accepté en T3 par les trois (B T3 D-a5,
   D-a6 ; C T3 § a.4 ; D T3 ligne « 200 bénins Bailey »). Chacun en tire une conséquence différente (§ 6, divergences 1 et 6).
9. **Contrôle de non-trivialité : perturbations aléatoires de même norme et audit du juge sur les sorties après perturbation** —
   source : D T1 § 6 ; réclamé comme bloquant par B T2 (c.1–c.2 sur D) et C T2 (c.2 sur B, c.1 sur D) ; B T3 ajoute un contrôle de
   dégénérescence du juge, C T3 les directions aléatoires de même norme, D T3 un « duel de non-trivialité » bloquant. **D → B, C.**
10. **D retire ses trois duels à tolérance libre comme conditions du choix** — D T3 cède à B T2 (a.1 : non falsifiables) et C T2
    (a.2 : non jugeables sans règle d'arrêt). D ne les chiffre toujours pas ; il les retire.
11. **D reclasse son duel 2 en « calcul de fragilité »** — D T3 cède à B T2 (a.2 : à sonde figée, c'est une lecture de fonctions en
    escalier) et accepte la saturation (B T2 b, C T2 b.3). Converge avec la courbe N_dir(α) de C T1 § 3 (tous les seuils observés,
    directions qui changent de statut entre rangs adjacents).

Cas particuliers : B T3 corrige son expérience 1 pour reproduire le déséquilibre 800 nuisibles / 400 bénins (cède à D T2 a.1) et
C T3 ajoute la repondération 2:1 (cède à B T2 a.5) — convergence B ↔ C sur la forme de l'expérience 1, à partir de deux critiques
différentes. B T3 accepte « en partie » la fuite de sélection (C T2 a.2) et la transforme en Bonferroni sur ≤ 3 candidats (§ 7).

---

## 6. Divergences (critère 6)

**Résolues** (une espèce cède en T3 avec raison) :

- R1. Troisième option « calibration hors pli » (C) contre « pas de validation croisée pour le seuil » (D T1 § 4 : « ne fabriquent pas
  les 2 000 bénins indépendants ») : C cède (§ 5, n° 1).
- R2. Signe et rôles des statistiques d'ordre dans l'expérience 3 de C : C cède (§ 5, n° 2).

**Non résolues** :

- N1. **Choix final.** Après T3 : B → jeu externe vérifié (≈ (A) avec test et repli) ; C → (B) pure, 400/300/300 ou 600/200/200
  selon l'expérience 1 ; D → (B) 400/300/300 comme déviation déclarée. B n'a pas cédé ; C et D n'ont pas cédé. B T2 avait écrit que C
  et D « convergent vers (B) », sans en tirer de conséquence pour lui-même.
- N2. **Première expérience à faire.** B T3 et C T3 : la comparaison sonde-800 / sonde-400 au rappel à 1 % de fausses alertes
  (accord né en T1, B expérience 1 et C expérience 1). D T3 : la retire comme contrôle bloquant (« B définit une nouvelle sonde »),
  parce que C T2 (a.3) a montré que la sonde-800 ne peut être calibrée que sur ≤ 200 bénins (Beta(1,100) ou Beta(2,199)), variable
  confondante avec la taille d'entraînement ; D fait d'abord un pilote figé de (B). Observation, sans verdict : l'expérience 1 corrigée
  de C T3 calibre chaque sonde sur « son propre 2ᵉ plus grand score sur les 200 bénins val+test », la configuration Beta(2,199) même
  que C T2 reprochait à D ; C y répond en partie par 50 répétitions et une ligne de base à taille égale, sans le dire.
- N3. **Contrôle « sonde sur modèle de base contre modèle instruit »** : proposé par B T2 (c, pour C et pour D) comme le contrôle
  « le plus critique » ; rejeté par C T3 § a.7 (hors mandat de D-ML-1, modèle fermé par le préenregistrement) et par D T3 (dernière
  ligne du tableau : « la question porte sur l'évasion d'une sonde figée »). B ne revient pas dessus en T3 : ni cédé ni maintenu.
- N4. **Licence d'Alpaca** : Apache 2.0 (B T1 § d) contre CC-BY-NC-4.0 (C T1 § 2). Les deux sont RAPPORTÉES, aucune vérifiée ; le
  lecteur n'a pas vérifié (R7, pas de chiffre opposable sans pièce versée).
- N5. **Statistique et données du test de ressemblance** (T3) : B → permutation sur le quantile 99 %, 200 Bailey contre 1 000
  externes, α = 0,01/3, δ_p = 0,025 ; C → TOST par bootstrap sur l'écart standardisé du quantile 99 % (± 0,15 σ) et Clopper-Pearson à
  90 % du taux croisé dans [0,0048 ; 0,0171], 1 000 scores Bailey hors pli contre 2 000 externes ; D → dépassements au seuil externe sur
  de **nouvelles** données cibles indépendantes, marge et puissance fixées avant, sans chiffre. Même cadre (équivalence), trois
  instruments et trois jeux de référence différents.
- N6. **Portée de l'impossibilité à n = 200.** C T3 § a.4 : « preuve formelle qu'il faut rejeter (A) au profit de (B) » ; B T3 D-a5 :
  « si cette marge [≈ 0,025] est jugée trop large par l'arbitre, cela constitue un argument en faveur d'un jeu externe plus grand » ;
  D T3 : « une équivalence plus étroite exige davantage de données cibles ou une tolérance plus large explicitement acceptée ». Même
  fait (intervalle à 90 % de 2/200 : [0,0018 ; 0,0311], VÉRIFIÉ), trois lectures.

---

## 7. Apports d'une seule espèce (critère 7 : gardés, « une source », non réfutés)

1. **D — la convention exacte de seuil doit être versée et testée** (D T1 § 1 « réserve importante » ; D T3 § 2.1) : la loi
   Beta(k, n+1−k) vaut pour le k-ième plus grand score sans ex æquo ; une interpolation de `quantile`, des arrondis ou des ex æquo
   changent la loi. Recalcul : si le seuil est le quantile empirique usuel à 99 %, S(297) sur 300 (4ᵉ plus grand), le taux futur suit
   Beta(4, 297), [0,0036 ; 0,0289], moyenne 1,33 %, contre [0,0021 ; 0,0239] pour Beta(3, 298). C T2 (b.2) effleure le point sans en
   tirer la conséquence ; B T3 trébuche dessus (§ 8, n° 6).
2. **D — la borne est empirique sur les directions trouvées, non une borne de confiance sur toutes les directions existantes**
   (D T1 § 2.6 ; D T3). Non repris, non contesté.
3. **D — séparer les deux incertitudes et utiliser la loi prédictive bêta-binomiale induite par Beta(3, 298) plutôt que d'additionner
   deux intervalles** (D T3 § 2.2). Non repris, non contesté.
4. **D — échangeabilité des partitions : doublons, quasi-doublons, stratification cachée, à contrôler avant tout** (D T1 § 2.1 ; D T3).
   C T2 (c.2 sur D) propose en écho une inversion des blocs seuil/mesure ; D T3 la reporte après gel du résultat principal.
5. **C — bande de lecture aux statistiques d'ordre X(1), X(3), X(7) sans coût de calcul** (C T1 § 3), devenue l'instrument commun en
   T3 (B T3 rapporte S(297)…S(300) ; D T3 « tous les seuils distincts observés »). Source C ; reprise, donc aussi convergence (§ 5, n° 5).
6. **C — aveuglement structurel du KS aux événements de probabilité < 5 %** (C T2 b.1 ; valeur critique 0,1263 VÉRIFIÉE) et
   **impossibilité d'un TOST à δ_p < 0,021 sur 200 bénins** (C T2 b.2 ; demi-largeur 0,0211 VÉRIFIÉE). Acceptées par leurs cibles.
7. **C — découpage de repli 600/200/200** si 400 bénins dégradent la sonde (C T3), avec les intervalles déjà servis pour n = 200
   ([0,0012 ; 0,0275] au seuil, [0,0012 ; 0,0356] en mesure). Une source ; C T1 proposait 500/300/200, abandonné sans commentaire.
8. **B — sélection des jeux externes bornée : ≤ 3 candidats préenregistrés dans un ordre fixé, Bonferroni α = 0,01/3, le premier qui
   passe est retenu, contrôle de stabilité de la sélection sur deux moitiés des 200** (B T3 C-a2). Une source ; non critiqué (T3 est
   le dernier tour).
9. **C — rendre hors échantillon les 1 000 bénins de Bailey par validation croisée à 5 plis pour le côté Bailey du test d'équivalence**
   (C T3, expérience 2 corrigée). Une source ; non critiqué ; réserve du lecteur en § 2.2.

---

## 8. Affirmations inexactes (critère 10 : au-delà de l'arrondi ; et contradictions internes)

1. **C T1 § 1** : « on sacrifie 500 bénins de l'entraînement (passant de 800 à 400) » — 800 − 400 = 400.
2. **C T1 expérience 3, § 3 et § 4** : la métrique Δ_τ = [N_dir(X(7)) − N_dir(X(1))] / max(1, N_dir(X(3))) est toujours ≤ 0 (N_dir
   croissant en t), donc le critère « ≤ 0,10 » est vide ; le pire cas « 450 directions à X(3), 12 à X(1) » contredit la monotonie ;
   X(1) est nommé « conservateur pour l'attaquant » alors qu'il est le seuil le plus permissif pour lui. Trouvé par D T2 (a.5), concédé
   par C T3 (a.2).
3. **C T2 (b.3) sur B** : « la probabilité … dépasse 45 % » alors que les deux termes donnés (0,26 et 0,09) font 0,35 ; recalcul exact :
   0,3536 (loi bêta) et 0,3588 (bêta-binomiale avec m = 1 000). La phrase suivante, « plus d'une fois sur trois », est juste. **Propagé** :
   B T3 (C-b3) reprend « > 45 % » dans son titre et écrit « le calcul est correct » (B n'a recalculé que le 0,26).
4. **B T2 (b) sur D, duel 1** : la formule de taille écrite donne 236, non « ≈ 1 200 » ; la « puissance de 20–30 % » à m = 200 contre
   0,01 → 0,03 est, en binomiale exacte (rejet si K ≥ 6, niveau 0,016), 0,557. Marqué « illustratif », mais l'arithmétique de la formule
   citée est fausse d'un facteur 5 ; la conclusion « essentiellement aveugle aux décalages modérés » est affaiblie (sous-puissant, pas
   aveugle). D T3 a accepté la critique sans recalcul.
5. **B T2 (b) critère 2 sur C** : « il faudrait observer 0 ou ≥ 7 dépassements » pour sortir de [0,0021 ; 0,0238] sur 200 — c'est 0
   ou ≥ 5 (5/200 = 0,025). Marqué « illustratif » ; le sens (le critère rejette rarement) tient.
6. **B T3 expérience 3 corrigée** : « S(297) … couverture nominale Beta(3, 298) » et « S(299) … Beta(1, 300) » — sous la convention du
   calcul servi (k-ième plus grand), le 3ᵉ plus grand de 300 est S(298) et le plus grand est S(300) ; S(297) donne Beta(4, 297) et S(299)
   Beta(2, 299). Décalage d'un rang ; c'est précisément la réserve de D sur la convention (§ 7, n° 1).
7. **C T1 § 1 et § 2** : le bruit de (B) « analytiquement borné par la loi Beta » et « borné dans [0,21 % ; 2,38 %] » — c'est un
   intervalle de couverture à 95 %, le support reste (0, 1). Trouvé par D T2 (a.3), concédé par C T3 (a.3).
8. **B T3 (D-a4)** : renvoi erroné « contrôle de permutation cyclique (identifié par C-c2 ci-dessus) » — C-c2 dans la numérotation de B
   désigne le contrôle de dégénérescence du juge ; l'inversion des blocs seuil/mesure est le (c.2) de C **sur D**. Erreur d'étiquette, pas
   de chiffre.

Vérifiés exacts : Beta(7,694) ≈ [0,0040 ; 0,0186] (C T1) ; 10/200 → [0,024 ; 0,089] (B T1, C T1) ; 117 et 13,5 (B T2) ; 39 / 9 / 99
(D) ; 0,126 et [0,0018 ; 0,0310] (C T2) ; « facteur 11 » (B T1). Aucune ligne du calcul servi n'a été mal recopiée.

---

## 9. Passages hors niveau (critère 2 : comptés et signalés par leur classe seulement, ni reproduits ni résumés)

| Classe | Occurrences | Cellules et sections |
|---|---|---|
| Procédure d'optimisation des directions (règle d'arrêt, objectif) | 4 | C T1 § 4 pire cas 1 ; C T1 expérience 3 protocole ; C T2 (b.3) sur D ; C T3 expérience 3 corrigée, étape 1 |
| Motif de contournement du juge de nuisance | 2 | C T1 § c, tableau ligne 3, colonne « vérifications mécaniques » ; B T2 (a.5) sur D |
| Mécanisme de l'intervention sur la sonde (limite : relève de la définition même de l'expérience dans les faits) | 2 | C T2 (c.1) sur D ; D T3 tableau, ligne C(c)1 |

Aucun paramètre d'évasion chiffré n'a été relevé. Les contrôles « perturbations aléatoires de même norme » et « > 3 σ dans des
directions aléatoires » (B T3) sont des contrôles négatifs, non des méthodes d'attaque ; non comptés.

---

## 10. Les options telles que les espèces les laissent, avec leurs conditions

**(A) — jeu bénin public plus large à verser.** Portée par aucune espèce sous cette forme nue. Condition préalable commune : une preuve
positive d'équivalence de la queue droite des scores (cadre TOST, § 5 n° 7) ; les trois constatent que les 200 bénins de Bailey hors
entraînement ne la fournissent pas à une marge plus étroite qu'environ 0,021 à 0,025 (recalcul : intervalle à 90 % de 2/200 =
[0,0018 ; 0,0311]). Conditions supplémentaires : B → ≤ 3 candidats
préenregistrés, Bonferroni, scores hors entraînement, repli (B) ; C → seulement si la source mère exacte des bénins de Bailey livre
2 000 textes de plus (après déduplication) et passe le TOST ; D → seulement avec de nouvelles données cibles indépendantes, marge et
puissance fixées avant les scores, un seul candidat ou correction de multiplicité. Candidats nommés (tous SUPPOSÉS) : Alpaca (B, C ;
licence en désaccord), Dolly-15k (B, D), LMSYS-Chat-1M (B), XSTest et OR-Bench (C, signalés par C comme décalés vers la frontière),
UltraChat (C), oasst1 (D). Risque reconnu par les trois : un biais systématique non borné, dans un sens ou dans l'autre.

**(B) — Bailey seul, 400 / 300 / 300.** Portée par D (T1, T3) et par C (T3) ; repli de B (T1, T3). Conditions posées : la sonde à 400
est un nouvel instrument (D), à comparer à la sonde-800 avant (B, C : première expérience, perte de rappel à 1 % de fausses alertes
≤ 2 points pour C, ≤ 5 points pour B, illustratifs) ou seulement à titre exploratoire (D) ; convention de seuil versée et testée (D) ;
déduplication et découpage reproductible avant tout (D) ; le « 1 % » n'est jamais présenté comme un point de fonctionnement exact (D,
C) ; rapport obligatoire du compte de directions aux statistiques d'ordre X(7) (borne inférieure), X(3) (nominal), X(1) (borne
supérieure) ou à tous les seuils observés, en comptes bruts, avec la loi prédictive de calibration Beta(3, 298) et Clopper-Pearson sur
les 300 de mesure (B, C, D) ; contrôle de non-trivialité bloquant (D ; B et C comme contrôles). Lecture à 20 % et 5 % : oui pour les
trois, en comptes sur 200 adverses (39 et 9 détections au plus), conditionnellement au seuil, bloc de mesure jamais réutilisé. Pire cas
commun : sonde affaiblie + seuil permissif → directions gonflées à 5 % ; D suspendrait alors la campagne.

**Troisièmes options.** (i) Calibration hors pli sur 700 + mesure 300 (C T1) : **retirée** par son auteur en T3 (loi bêta non exacte,
transfert vers la sonde finale non établi, fuite de sélection) ; C T3 en garde un « test subsidiaire » non bloquant. (ii) Jeu externe
avec sonde-800 et repli (B) (B T1, T3) : maintenue par B, voir (A). (iii) Découpage 600 / 200 / 200 (C T3) si 400 bénins dégradent la
sonde ; intervalles servis pour n = 200 ([0,0012 ; 0,0275] au seuil, [0,0012 ; 0,0356] en mesure) : plus larges que pour 300, en
échange d'une sonde moins amputée ; une source. (iv) Bootstrap ou validation croisée pour fixer le seuil : **écartés** par les trois
en T3 (inconsistance des quantiles extrêmes à n α = 3 ; « ne fabriquent pas les données manquantes »). (v) Seuil paramétrique
(moyenne + 2,326 σ) : écarté par C T1 (tableau) et D T1 § 4 (déplace le problème vers une hypothèse de queue).

---

## 11. Réserves

- **Symétrie (critère 9, R4).** Sept des huit accords de T1 sont unanimes à trois ; en T3, les trois espèces adoptent le même cadre
  d'équivalence, la même lecture aux statistiques d'ordre, le même contrôle de non-trivialité et la même phrase « le non-rejet n'est pas
  une certification ». C T1 § 1 et D T1 (chapeau) disent presque dans les mêmes mots « variance connue préférable à un biais non borné ».
  La critique croisée a homogénéisé : réserve, pas preuve. Deux chiffres inexacts ont circulé sans recalcul du récepteur (§ 8, n° 3, 4).
- **Absence de Fable (A).** Trois cellules sur douze manquent (refus dès la première) ; aucune position ne lui est prêtée ; les accords
  « unanimes » sont des unanimités à trois, non à quatre. Le lecteur de la présente synthèse est de la même famille de modèles que A :
  il n'a produit aucune réponse à la question et s'est tenu aux critères.
- **Les trois espèces n'ont pas eu le script du calcul**, seulement sa sortie (D le dit explicitement : « OBSERVÉE-NON-AUDITÉE ») ; elles
  ont reconstruit la convention (k-ième plus grand score) par concordance numérique, et le lecteur l'a confirmée sur le script. La
  réserve de D sur la convention réellement codée dans le run futur (interpolation, ex æquo) reste entière.
- **Chiffres « illustratifs » servant de coupures.** B T2 (a.4) l'a relevé pour C ; C T3 répond en déclarant chaque « illustratif » comme
  coupure proposée. Pour D, les marges restent non chiffrées par choix. Aucune coupure de T3 n'est donc fondée sur une mesure : toutes
  sont SUPPOSÉES.
- **Aucune pièce versée** : aucun jeu, aucune licence, aucun score de sonde ; tout ce qui concerne (A) est RAPPORTÉ ou SUPPOSÉ.
- **Tensions internes non critiquées** (T3 est le dernier tour) : § 6 N2 ; § 2.2 (scores hors pli au côté Bailey du TOST de C) ; B
  garde le jeu externe en premier choix tout en acceptant que 200 bénins ne certifient rien de plus étroit que ≈ 0,025.

## 12. Rien n'est tranché

La décision D-ML-1 revient à Lazar ; la question est aussi posée à conv-audit (critère 14). Cette synthèse présente les options et
leurs conditions telles que les trois espèces les laissent, les accords et divergences, et les chiffres recalculés ; elle ne
recommande rien.
