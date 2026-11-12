# Préenregistrement — quatre règles de mise à jour de la défense dans l'arène coévolutive synthétique v4, témoin « défense figée », exploitabilité finale et moyenne sur les tours, détection sur attaques tenues à l'écart, coût — v2 — BROUILLON 4 (prêt au scellement, non scellé)

**Note de version (brouillon 4, 1er novembre 2026, ≈ 15:55 UTC)** — Ce brouillon 4 est le brouillon 3 (`brouillon-prereg-regles-defense-v3.md`, empreinte `7862c944458425f096bfb926ebea3aa2abddee91d03afeb997a5d23b85c946b8`, archivé sans modification) plus, exactement, les corrections de la contre-lecture 2 (`contre-lecture-2-prereg-regles-defense-v3.md`, empreinte `c5ba88fc6ec874dce22bcc6fbb1d1ae8544cabd17ce36dfc6a0266722222f227`, verdict « scellable après corrections mineures ») : **CL2-01** (phrase de déclaration des indications contraires du pilote v2 pour P13 et P14, ajoutée au paragraphe « Déclaré (CL-06) » du § Prédiction), **CL2-02** (citation de R-962 conforme au registre), **CL2-03** (restes « ce brouillon 2 » et « recommandation S8 »), l'entrée « Contre-lecture 2 » remplie, et les phrases de statut. Rien d'autre : aucune hypothèse, prédiction, métrique, table de lecture, liste d'arrêt ni plan d'analyse n'est modifié ; le bloc d'identité est recopié tel quel (identifiant PREREG-REGLES-DEFENSE-V2, code v2 inchangé). Rédacteur : le contre-lecteur 2 (sous-agent neuf, Fable 5.1), par script de remplacement (chaque chaîne originale trouvée au compte attendu, arrêt sinon) ; il ne décide rien. Statut : **brouillon 4, prêt au scellement** (validateur `controle_ia.prereg.problemes` muet ; garde d'identité du code v2 passée sur ce texte).

**Note de version (brouillon 3, 1er novembre 2026, ≈ 15:40 UTC)** — Ce brouillon 3 est le brouillon 2 (`brouillon-prereg-regles-defense-v2.md`, empreinte `9629fa1e307934d6ae908841ab0675fc0c486ac2228a9196dbb3bae1c40eac97`, archivé sans modification) dans lequel chaque champ « à remplir » et chaque marqueur « DÉCISION DE LAZAR » est remplacé par la valeur que Lazar a retenue le 1er novembre 2026 (≈ 15:30 UTC, `registres/decisions.md` R-962 : « Recommandation (b) … : go ; go tout go ligne N ») : option (b) du constat CL-05 (HR2 sur X̄, témoin R0) et **toutes les valeurs recommandées du brouillon 2** — S1 = 0,02 ; S2 = 5 % bilatéral par famille ; S3 selon la recommandation ; S4 N = 100 ; S5 = 0,02 ; S6 λ* = 0,3, référence « moyenne » ; S7 T = 8 ; S8 `timeout 3600` ; S9 α = 0,01 ; S10 selon la recommandation ; S11 δ = (1,4 ; 1,6) ; S12 = 0,999 ; S13 « détection » ; S15 = 0,02 ; cinq variantes R0, R1, R2, R3, R4(λ*) ; ordre : après la course du pilote v4. **Ce qui change par rapport au brouillon 2 : ces seuls reports, le commit du code d'analyse (relevé par `git`), la mise à jour des phrases de statut (« à trancher » → « tranché ») et l'ajout du point 7 de l'historique de conception. Rien d'autre : aucune hypothèse, prédiction, métrique, table de lecture, liste d'arrêt ni plan d'analyse n'est modifié ; le bloc d'identité est recopié tel quel du brouillon 2 (il vient du code v2, inchangé : identifiant PREREG-REGLES-DEFENSE-V2, aucune identité « v3 » n'existe ni n'est nécessaire).** Rédacteur du brouillon 3 : sous-agent neuf (Fable 5.1), qui n'a écrit ni le code v2, ni le gel v2, ni le brouillon 2, ni la contre-lecture 1 ; il ne décide rien : il reporte. Reste avant scellement : la contre-lecture 2 (courte, R2), seule entrée encore « à remplir » — faite, reportée au brouillon 4.

**Statut : brouillon 4, prêt au scellement ; brouillon 2 = brouillon 1 (`brouillon-prereg-regles-defense-v1.md`, empreinte `be08f4385dba0642ec857c96c67cc11c2d2acd09da026533d942fd7c87f1a48c`, archivé sans modification) corrigé constat par constat d'après la contre-lecture 1 (`contre-lecture-prereg-regles-defense-v1.md`, empreinte `19ca1e283b579acadd4a91453e5d5268984f2aaabdea055e127d4de5a6938495`, verdict « scellable après corrections »), par un sous-agent neuf qui n'a écrit ni le brouillon 1, ni le code v1, ni la contre-lecture 1 ; seuils et marqueurs tranchés par Lazar le 1er novembre 2026 (R-962) et reportés dans ce brouillon 3 ; contre-lecture 2 (courte, R2) faite et reportée dans ce brouillon 4 ; reste le scellement, puis la course décisive (GO de Lazar, nœud de décision distinct). Le validateur `controle_ia.prereg` refuse tout texte qui garde un marqueur « à remplir » ou « DÉCISION DE LAZAR » : l'entrée « Contre-lecture 2 » est remplie : aucun marqueur ne reste.**

**Décision du directeur (1er novembre 2026, ≈ 15:30 UTC, R-962 : « Recommandation (b) … : go ; go tout go ligne N ») — l'hypothèse de travail de la session principale est retenue telle quelle : option (b) du constat CL-05 (HR2 portée sur X̄, moyenne des exploitabilités par tour, code v2) ; témoin R0 « défense figée » ajouté ; cinq variantes à la décision : R0, R1, R2, R3, R4(λ*) ; λ* = 0,3, référence « moyenne », produit mécanique de la règle du gel v1 § 3 sur le pilote d'essai v1 ; S12 = 0,999 déclaré posé en voyant les cosinus du pilote v1 ; grille complète retirée (CL-07) ; T = 8, N = 100, δ = (1,4 ; 1,6), m = 0,02.**

Identifiant : **PREREG-REGLES-DEFENSE-V2** (remplace PREREG-REGLES-DEFENSE-V1, jamais scellé ni exécuté). Tâche : demande du directeur (1er novembre 2026) : « comparer dans notre jeu quatre règles de mise à jour de la défense (dernière attaque ; historique ; mélange d'équilibre des deux côtés ; régularisation vers le passé) sur exploitabilité, détection sur attaques tenues à l'écart et coût ; rendre le jeu posable à classe de fonctions égale ; préenregistrer ». Pilote de **mécanisme** : aucun modèle de langage, aucun texte ; « l'attaquant » est un choix de paramètres d'une loi synthétique (mélange gaussien) sous contrainte de comportement ; le monde, l'oracle du défenseur, l'attaquant et les familles tenues à l'écart sont ceux de l'arène v4 (`arene_melange_v4.py`, jamais modifiée). La formalisation du jeu (`../formalisation-jeu-convergence-v1.md`) et le jeu jouet OpenSpiel sont d'un autre sous-agent : hors de ce texte, cités pour le vocabulaire (exploitabilité, § 3.1 ; condition g, § 6).

- Auteur : sous-agent neuf (développeur-rédacteur, modèle Fable 5.1), 1er novembre 2026 ; a écrit le gel v2, le code v2, ses essais, le pilote d'essai v2 et le brouillon 2 ; n'a écrit ni le v4, ni le gel v1, ni le code v1, ni le brouillon 1, ni la contre-lecture 1. Brouillon 3 : report des décisions de Lazar par un sous-agent rédacteur neuf (Fable 5.1), sans autre changement.
- Date (UTC) : 2026-11-01 ; heure de fin du brouillon 2 au LISEZMOI v2 ; brouillon 3 : 2026-11-01, ≈ 15:40 UTC.
- Commit du code d'analyse : `ed3377bd400caf46189f3ff21c930f179335bd17` (1er novembre 2026, 11:04:31 UTC, « chantier convergence : code v2 … ; R-961 »), qui contient `arene_regles_defense_v2.py` à l'empreinte du bloc d'identité (`9f0dcf5e…`, vérifiée par `git show` sur ce commit le 1er novembre 2026 à 15:39 UTC) ; aucun commit par le sous-agent rédacteur.
- Documents qui font foi (chemin + empreinte) :
  - `donnees/argon-seul-convergence-v1/arene_melange_v4.py` — `70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61` (le jeu, les bras A et B, l'attaquant, les lois tenues, les indicateurs I1 à I3, le rééchantillonnage) ;
  - `donnees/argon-seul-convergence-v1/preenregistrement-arene-melange-equilibre-v1-brouillon4.md` — `305911b7ab1945d7607377ede9c8cbfcf2257834bca6d6aadcf7c19be41f8160` (brouillon 4 du v4 : bras A = « historique », valeur nulle 0,7345, δ = (1,4 ; 1,6), N = 100, S18 = 0,10, Table 5) et `verification-arene-melange-v4-brouillon4.md` — `28ab322f9d2e6098562d127f20e98560c4b202ef737b75ff217dfe0c9c7672f2` ;
  - `docs/notes/convergence-defense-v1/regles-defense-v1/gel-regles-defense-v2.md` — `9977d7df7f87f081f3c89709c6f36ab2c3861cb06c972dffbabe0e777e9910f3` (racines v2, règles dont R0, X̄, ce qui change ; écrit avant toute exécution du code v2 ; empreinte épinglée dans le code) ; gel v1 — `4fbb12dc941479f59504d9c3dc8246bf88c474a40c387bea40ac2e24c4ef0890` (archivé ; grille de λ et règle de choix) ;
  - `prereg/gabarit-preregistrement-v1.md` — `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` ;
  - contre-lecture 1 — `19ca1e283b579acadd4a91453e5d5268984f2aaabdea055e127d4de5a6938495` (constats CL-01 à CL-16, calcul de puissance § 5, trois faits sur λ* § 4).
- Code, essais et pilotes (même dossier) : `arene_regles_defense_v2.py` (bloc d'identité) ; `test_arene_regles_defense_v2.py` (25 essais) ; `pilote-essai-regles-defense-v2.json` et `.md` ; `pilote-essai-regles-defense-v1.json` et `.md` (λ*, référence) ; empreintes recalculées au LISEZMOI v2.

**Aucune lecture n'a été faite sur les racines de décision RACINE_DECISION = 20266201 et RACINE_DECISION_TENUE = 20266202** (refusées par le code sans préenregistrement scellé ; inchangées de la v1, aucune graine n'en a été tirée). Tout nombre de ce texte vient du brouillon 4 du v4 (contexte, **non opposable**), du gel, de la contre-lecture 1, ou est un marqueur ; **aucune prédiction n'est tirée des pilotes d'essai** (le pilote v1 fournit λ*, la référence et les écarts-types du calcul de puissance ; le pilote v2 fournit la projection de temps et la preuve que X̄ et R0 sortent).

### Bloc d'identité (vérifié par le code à la décision ; régénéré par `arene_regles_defense_v2.py identite` le 1er novembre 2026 à 10:54 UTC ; à régénérer si le code ou la configuration change)

- Identifiant : PREREG-REGLES-DEFENSE-V2
- Racines de décision : RACINE_DECISION = 20266201 ; RACINE_DECISION_TENUE = 20266202
- Code : `arene_regles_defense_v2.py` — 9f0dcf5e0d10fe93dd19c318f076728d62b64734161dc72b40a812a817340da3
- Arène v4 : `arene_melange_v4.py` — 70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61
- Gel : `gel-regles-defense-v2.md` — 9977d7df7f87f081f3c89709c6f36ab2c3861cb06c972dffbabe0e777e9910f3
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

Réglages de R4 (vérifiés par le code à la décision) — **produit mécanique de la règle du gel v1 § 3 appliquée au pilote d'essai v1** (racines 20266101 / 20266102, 6 instances × 2 δ, grille {0,03 ; 0,1 ; 0,3 ; 1 ; 3} × {« dernier », « moyenne »}), avec les trois faits recalculés par la contre-lecture 1 (S6) ; réglage **retenu par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2** (S6, option (a)) :

- LAMBDA_RETENU = 0.3
- REFERENCE_RETENUE = moyenne

Codes de graine des règles (gel v2 § 2) : R0 20 (neuf), R1 21, R2 1 (= A), R3 2 (= B), R4 24. Rang des variantes à l'analyse (clés de rééchantillonnage) : R0 0, R1 1, R2 2, R3 3, R4(λ*) 4.

## Résumé pour Lazar

1. **Question** : dans le jeu synthétique du v4, laquelle de quatre règles de mise à jour du défenseur laisse le moniteur déployé le moins exploitable après T = 8 tours de coévolution, à quel prix sur les attaques jamais vues (tenues à l'écart) et en temps de calcul ; et **une règle quelconque fait-elle mieux que ne rien faire** (témoin R0 : M0 jamais réentraîné, l'attaquant jouant en dernier à chaque tour) ? R1 « dernière attaque » (transposition du protocole de Bailey et collègues) ; R2 « historique » (= bras A du v4, référence) ; R3 « mélange d'équilibre des deux côtés » (= bras B du v4 ; lecture R3′ = valeur du jeu restreint) ; R4 « régularisation vers le passé » (historique plus pénalité sans échelle 2λ(1 − cos(w, u)) ; λ* et référence gelés).
2. **Deux lectures de l'exploitabilité** : **X finale** = 1 − V (défense finale figée, attaquant lourd : standard puis renforcé) et **X̄** = moyenne sur les T tours de X_t = 1 − (iii)_t (défense déployée au tour t, attaquant du tour). Pourquoi les deux (CL-05) : la dynamique de R1 est de période 2 (le moniteur du tour impair est très exploitable, celui du tour pair peu), si bien que X finale de R1 **lit la phase du cycle à la parité de T près** ; X̄ ne dépend pas de cette parité au-delà d'une tolérance (essai lent, une instance, configuration complète : |ΔX̄| = 0,021 contre |ΔX finale| = 0,131 entre T = 3 et T = 4). **HR2 (R1 contre R2) est portée sur X̄** ; X finale de R1 est recopiée sans verdict. Les autres hypothèses restent sur X finale (V), X̄ recopiée.
3. **Classe de fonctions égale** : R0, R1, R2, R4 déploient **un moniteur linéaire** (7 paramètres par requête) ; R3 un **mélange** de T + 1 moniteurs linéaires (7 par requête, 63 déployés) : classe déployée égale (linéaire), à nombre de paramètres par requête égal ; toutes les règles gardent la liste des moniteurs pour la matrice H (analyse seulement, CL-09). Aucun maxout : la question « classe égale » du v4 (B′ contre D) n'est pas reprise.
4. **Hypothèses (signes par principe, confiance modérée)** : HR1 : R3 moins exploitable que R2 (= « B − A » du v4, plomberie, Table A seule) ; HR2 : R1 plus exploitable que R2 sur X̄ (oubli) ; HR3 : R4(λ*) au plus aussi exploitable que R2 (classes « R4 > R2 », « R4 ≳ R2 » ou « ≈ » de la Table B) ; **HR0 (neuve)** : R2 moins exploitable que R0 sur V (réentraîner contre l'historique vaut mieux que ne rien faire) — **réserve déclarée** : le pilote v1 indiquait V(R2) ≈ V(R4, λ = 3), une défense presque figée ; c'est un indice, non la prédiction ; HR4 : sur les tenues à l'écart, R3 régresse, R1 régresse, R4 ne régresse pas (R0 recopié) ; HR5 : R2 ne progresse pas et revient vers d'anciennes attaques (Table 5 du v4) ; HR6 : coût R3 > R2 ≈ R4 > R1 > R0.
5. **Seuils** : S1 à S15 retenus par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeurs recommandées du brouillon 2 : m = 0,02 (= v4), N = 100 par δ, T = 8, δ = (1,4 ; 1,6), 5 % bilatéral par famille (B8 exacte pour 8 tests par famille), bornes par rééchantillonnage apparié comme le v4 ; **puissance** (S3, contre-lecture 1 § 5 et ce brouillon) : ≈ 1 pour P1 à l'effet du contexte v4, ≈ 0,5 à l'effet m exactement ; Table C pour R4 au δ 1,6 : 0,75 à N = 100 sous effet nul.
6. **Coût de la décision** (pilote v2, racine d'essai, 4 tâches à 5 variantes) : 17,3 s de processeur par tâche → 200 tâches ≈ 58 min de processeur, **≈ 30 min de mur sur 2 processus** à l'efficacité mesurée 0,96 (≈ 14 min sur 4) ; S8 retenu : `timeout 3600` (deux fois la projection) : **≈ 1 h de mur au plus**. Aucune dépense : processeur seulement.
7. **Points tranchés par Lazar le 1er novembre 2026 (R-962 : « go tout »)** : l'hypothèse de travail elle-même (option (b) + R0, cinq variantes) ; S6 (λ* = 0,3, référence « moyenne », option (a)) ; S12 (0,999, plus de la moitié des tâches) ; ordre : après la course du v4. Contre-lecture 2 faite ; reste : scellement, GO de la course.

## Ce que l'expérience n'autorise pas

- **Rien sur les vrais modèles** ni sur les moniteurs d'activations réels ; le monde est une famille de lois écrite par le programme (v4, § Portée). R1 est une **transposition** du protocole de Bailey et collègues (réentraîner contre la dernière attaque) avec l'oracle « détection » du v4, non une reproduction ; aucun chiffre de ce papier n'est repris (R7).
- Deux budgets δ, choisis au v4 sur A seul ; T = 8 ; attaquant local en boîte blanche (SLSQP, départs du v4). **Vocabulaire (CL-12)** : V surestime la garantie inf_θ Det(σ_D, θ) de la défense construite (optimiseur local) ; X = 1 − V en est une **borne basse de 1 − garantie** ; X diffère de l'exploitabilité expl_D = v* − V de la formalisation (§ 3.1) d'une constante par tâche, 1 − v*, de sorte que les **contrastes appariés entre règles sont les mêmes** ; la valeur du jeu v* n'est bornée ni d'un côté ni de l'autre par V. Même lecture pour X_t et X̄ (attaquant du tour, plus léger : 4 départs, 256 échantillons de Monte-Carlo). Sans attaquant indépendant dans cette v2 (option : celui du v4, `attaquant_independant`, non branché ; déclaré).
- **X̄ et X finale ne mesurent pas la même chose** : X̄ est l'exploitabilité moyenne de la défense **déployée au fil des tours** (ce que subit un déploiement continu), X finale celle de la défense **figée après T tours** contre un attaquant plus lourd ; à T = 1 elles diffèrent déjà (gel v2 § 4). Pour R1, X finale dépend de la parité de T (CL-05) : elle est recopiée, jamais lue comme verdict sur HR2.
- R3′ n'est pas une trajectoire distincte : la valeur du jeu restreint est lue sur la trajectoire de R3 (gel § 2).
- R4 dépend d'un réglage (λ*, référence) choisi sur le pilote d'essai v1 par une règle écrite d'avance : le résultat vaut pour ce λ* dans ce monde. **Effet de sélection (contre-lecture 1, § 4 M1)** : HR3 teste R4 au λ* que le pilote v1 a trouvé le meilleur sur V ; par cet effet, V(R4, λ*) à la décision est attendu un peu plus bas qu'au pilote ; la racine de décision est indépendante, le test reste valide.
- R0 est un témoin « ne rien faire » : il ne dit rien d'une défense figée **meilleure que M0** (M0 est entraîné contre la seule loi cible) ; HR0 compare « historique » à « rien », pas « historique » au meilleur moniteur figé.
- Aucune revendication d'antériorité ni de nouveauté (R8) ; aucune porte, aucune dépense, aucune modification du programme.

## Hypothèse

Renvoi : question du directeur (1er novembre 2026) ; brainstorm P-041 piste 3 (mélange d'équilibre contre défense unique) ; brouillon 4 du v4 (Table 5 : la défense unique A ne progresse pas et revient vers d'anciennes attaques au-delà du hasard) ; formalisation § 4.1 (meilleure réponse pure itérée : cycle) et § 5 (H-e1 à H-e4, non testées ici). **Oracle du défenseur** : « détection » du v4, identique pour R1 à R4 (principe S13 du v4) ; R0 n'en appelle aucun.

- **HR1 (principale, plomberie)** : contre la meilleure réponse finale, le mélange d'équilibre R3 est moins exploitable que l'historique R2 d'au moins m = S1 aux deux δ : Δ(R3, R2) = moyenne de V(R3) − V(R2) ≥ m. **HR1 se lit par la Table A seule** ; la classe de R3 dans la Table B est recopiée sans verdict sur HR1 ; le déclencheur 1 s'applique à P1 quand la Table A rend la ligne 5 ou 6 (CL-01). H0 : ligne 5 ou 6 de la Table A.
- **HR2 (sur X̄)** : la règle « dernière attaque » R1 est plus exploitable que R2 au fil des tours : D̄(R1, R2) = moyenne de X̄(R1) − X̄(R2) ≥ +m aux deux δ (la défense qui oublie se fait reprendre sur les attaques anciennes ; cela se voit tour par tour). **Verdict par la Table B′ (X̄)** : confirmée si classe « R2 > R1 » aux deux δ ; réfutée si « R1 > R2 », « R1 ≳ R2 » ou « ≈ » à un δ ; « ? » ou « R2 ≳ R1 » à un δ = non tranchée (CL-02). X finale de R1 : Table B recopiée, sans verdict (CL-05).
- **HR3** : R4(λ*) n'est pas plus exploitable que R2 d'un effet d'intérêt : classe « R4 > R2 », « R4 ≳ R2 » ou « ≈ » (Table B sur V, bornes B8 et E8) aux deux δ, S12 non déclenché ; réfutée si « R2 > R4 » à un δ ; sinon non tranchée (CL-03). Prédiction non ferme sur l'ampleur.
- **HR0 (neuve, témoin)** : réentraîner contre l'historique vaut mieux que ne rien faire : R2 est moins exploitable que la défense figée R0 d'un effet d'intérêt en finale : Δ(R0, R2) = moyenne de V(R0) − V(R2) ≤ −m aux deux δ, soit la classe « R2 > R0 » de la Table B ; réfutée si « R0 > R2 », « R0 ≳ R2 » ou « ≈ » à un δ ; sinon non tranchée. **Réserve déclarée** : au pilote d'essai v1 (non opposable), V(R2) − V(R4, λ = 3) valait +0,002 ; +0,006 au δ 1,4 et −0,011 ; −0,009 au δ 1,6, et R4 à λ = 3 est une défense presque figée (cosinus 1,000) : c'est un **indice** que « historique » ne ferait pas mieux, en finale, que « ne rien faire » ; la prédiction de HR0 est posée **par principe** (une mise à jour contre les attaques vues devrait réduire l'exploitation), pas sur cet indice ; une réfutation par « ≈ » serait donc attendue au vu du pilote et n'est pas une surprise (déclencheur 7 : symétrie). D̄(R0, R2) sur X̄ et Δ(R0, R2) sur (ii) : recopiés sans verdict (P13, P14).
- **HR4 (tenues à l'écart)** : sur les familles jamais vues par aucune mise à jour (50 lois par tâche, racine tenue à part), Δ(R3, R2) sur (ii) < 0 (régression, comme B − A au v4) ; Δ(R1, R2) sur (ii) < 0 ; Δ(R4, R2) sur (ii) ≥ −S5 (sans régression à la tolérance près) ; Δ(R0, R2) sur (ii) recopié sans verdict.
- **HR5 (condition d'application)** : R2 ne progresse pas (I1 ≈ 0) et ses attaques reviennent vers d'anciennes au-delà du hasard (I3 − 0,7345 > 0) : réplication de la Table 5 du v4, recopiée en entier (Table D, CL-04) ; R1 : retours au-delà du hasard au moins autant que R2 ; R4(λ*) : I3 − nul plus bas que R2 ; R0 : I1 et I3 de l'attaquant seul contre une défense fixe (descriptif).
- **HR6 (coût)** : descriptif, sans verdict : temps processeur par tâche et appels à l'optimiseur de R3 > R2 ≈ R4 > R1 > R0 ; programmes linéaires : R3 seul ; entraînements : R0 = 0.
- **Hypothèses de travail** : oracle du défenseur approché (seuil gaussien, départs du v4) ; attaquant approché, contrôlé par la réponse renforcée (V = min) ; loi propre N(0, I) connue du code ; R3 itéré tronqué ; λ* fixé sur racine d'essai v1 ; X̄ calculée avec l'attaquant du tour (plus léger que celui de la finale).

## Prédiction chiffrée et signe attendu

Signes et ordres de grandeur **par principe et par le contexte du v4 (brouillon 4, non opposable : B − A +0,128 / +0,139 sur (iii), −0,054 / −0,058 sur (ii) au pilote v4 ; A : I1 ≈ 0, I3 − nul +0,17 / +0,21)** ; aucune valeur ne vient des pilotes d'essai de ce dossier. Confiance = probabilité subjective arrondie ; la branche opposée déclenche l'audit (R4, déclencheur 1). Notations : Δ = contraste apparié sur V ou sur (ii) (détection : + = R_k meilleure) ; D̄ = contraste apparié sur X̄ (exploitabilité : + = R_k plus exploitable).

| # | Contraste ou indicateur | δ | Signe | Classe prédite | Ordre de grandeur | Confiance | Branche opposée |
|---|---|---|---|---|---|---|---|
| P1 | Δ(R3, R2) sur V (HR1, Table A) | 1,4 ; 1,6 | + | Table A ligne 4 | ≥ +0,05 (contexte v4 : ≈ +0,13) | 0,9 | lignes 5, 6 |
| P2 | Δ(R1, R2) sur V (descriptif, CL-05) | 1,4 ; 1,6 | − par principe | recopiée, sans verdict | ≈ 0 à −0,02 ; **dépend de la parité de T** | 0,4 | — (aucun verdict) |
| P3 | Δ(R4, R2) sur V (HR3) | 1,4 ; 1,6 | ≥ 0 | « R4 ≳ R2 » ou « ≈ » (non ferme) | [0 ; +0,05] | 0,5 | « R2 > R4 » |
| P4 | Δ(R3, R2) sur (ii) (HR4) | 1,4 ; 1,6 | − | « régression » | ≈ −0,05 (contexte v4) | 0,8 | borne basse B8 > 0 |
| P5 | Δ(R1, R2) sur (ii) (HR4) | 1,4 ; 1,6 | − | « régression » | ≤ −0,02 | 0,6 | borne basse B8 > 0 |
| P6 | Δ(R4, R2) sur (ii) (HR4) | 1,4 ; 1,6 | ≥ −S5 | « sans régression à S5 près » | [−0,02 ; +0,05] | 0,5 | borne haute B8 < −S5 |
| P7 | R2 : I1, I3 − 0,7345 (HR5) | 1,4 ; 1,6 | I1 ≈ 0 ; I3 − nul > 0 | Table D ligne 2 « cycle » | I3 − nul ≈ +0,1 à +0,2 | 0,85 | ligne 1 ; borne haute de I3 − nul < 0 |
| P8 | R1 : I3 − 0,7345 (descriptif) | 1,4 ; 1,6 | > 0 | — | ≥ celui de R2 | 0,6 | — |
| P9 | R4(λ*) : I3 − 0,7345 (descriptif) | 1,4 ; 1,6 | < celui de R2 | — | — | 0,6 | — |
| P10 | Coût (HR6) : processeur par trajectoire | — | R3 > R2 ≈ R4 > R1 > R0 | — | R3 ≥ 1,3 × R2 ; R1 ≤ R2 ; R0 ≤ 0,7 × R2 | 0,7 | ordre différent (sans effet sur les tables) |
| P11 | Fausses alertes finales | 1,4 ; 1,6 | — | \|moyenne − α\| ≤ 0,001 par règle | — | 0,9 | déclencheur 6 |
| **P12** | **D̄(R1, R2) sur X̄ (HR2)** | 1,4 ; 1,6 | **+** | **« R2 > R1 » (Table B′)** | **≥ +0,02 (= m)** | **0,6** | « R1 > R2 », « R1 ≳ R2 », « ≈ » |
| **P13** | **Δ(R0, R2) sur V (HR0)** | 1,4 ; 1,6 | **−** | **« R2 > R0 » (Table B)** | **≤ −0,02** | **0,5** (réserve : indice contraire du pilote v1, § Hypothèse) | « R0 > R2 », « R0 ≳ R2 », « ≈ » |
| P14 | D̄(R0, R2) sur X̄ ; Δ(R0, R2) sur (ii) (descriptifs) | 1,4 ; 1,6 | D̄ > 0 ; (ii) : + par principe (M0 n'a vu que la cible) | recopiées | — | 0,4 | — |
| P15 | D̄(R3, R2), D̄(R4, R2) sur X̄ (descriptifs) | 1,4 ; 1,6 | R3 : − ; R4 : ≈ 0 | Table B′ recopiée | — | 0,6 ; 0,5 | — |

**Déclaré (CL-06) — indications des pilotes d'essai, non opposables, que les prédictions ne recopient pas et auxquelles certaines s'opposent** : le pilote d'essai v1 (6 instances par δ, racine d'essai) indique pour Δ(R1, R2) sur V −0,006 ; +0,011 (signe contraire de P2, devenue descriptive) et sur (ii) +0,010 ; +0,066 (**signe contraire de P5**) ; pour D̄(R1, R2) sur X̄ +0,034 ; +0,019 (signe de P12, recalculé sur le fichier du pilote v1 par l'auteur de ce brouillon pour le calcul de puissance ; le second est à 0,001 de m : coïncidence déclarée, la marge m = 0,02 est posée par principe, = S1 du v4) ; P5 est maintenue par principe (oubli) ; une confirmation de P5 à la décision serait donc aussi une surprise au vu du pilote et déclenche la relecture du déclencheur 7. La borne haute de P6 (+0,05) est posée par principe (= borne haute de P3) et non lue sur le pilote, où Δ(R4, R2) sur (ii) au δ 1,6 vaut +0,051 : **coïncidence déclarée**. Pour P13, l'indice contraire (V(R2) ≈ V(R4, λ = 3)) est déclaré au § Hypothèse. L'auteur de ce brouillon a vu les tables du pilote v2 (2 instances par δ) en vérifiant que X̄ et R0 sortent ; aucune prédiction n'en est tirée ni ajustée (déclaré ; vérifié par la contre-lecture 2 : aucune prédiction ne recopie le pilote v2). **Déclaré (CL2-01)** : le pilote d'essai v2 (2 instances par δ, racine d'essai, non opposable, seul pilote où R0 existe) indique Δ(R0, R2) sur V +0,029 ; −0,002 et D̄(R0, R2) sur X̄ −0,006 ; −0,006, soit le signe contraire de P13 au δ 1,4 et de P14 aux deux δ ; P13 et P14 sont maintenues par principe ; une confirmation de P13 ou de P14 à la décision serait donc aussi une surprise au vu de ce pilote et relève du déclencheur 7.

Ce qui compterait comme réfutation : HR1 par la Table A (ligne 5) ; HR2 par la Table B′ (« R1 > R2 », « R1 ≳ R2 » ou « ≈ » à un δ) ; HR3 par la Table B (« R2 > R4 » à un δ) ; HR0 par la Table B (« R0 > R2 », « R0 ≳ R2 » ou « ≈ » à un δ) ; HR4 lue par la Table C.

## Métrique

Notations : une **tâche** = (δ, instance) ; les deux δ partagent la loi cible d'une instance ; une **variante** = une règle (R4 : à λ* et référence gelés). Taux de détection d'une défense mixte {(m_i, p_i)} sur une loi Q : Σ_i p_i × part des échantillons de Q dont le score dépasse le seuil t_i de m_i ; seuils calibrés au quantile 1 − α de 20 000 échantillons propres communs (α = S9).

- **Exploitabilité finale (principale pour HR0, HR1, HR3)** : **V(règle)** = métrique (iii) du v4 : après T tours, défense figée ; deux meilleures réponses sous la contrainte distance ≤ δ et la boîte — **standard** (12 départs tirés + départ vers l'origine + attaques passées de la trajectoire, 512 échantillons de Monte-Carlo par composante, 100 itérations SLSQP) et **renforcée** (48 départs, 200 itérations, plus la réponse standard) — chacune évaluée sur 19 998 échantillons frais ; **V = la plus basse des deux détections** ; **X = 1 − V** (dans [0 ; 1], garde). Contrastes sur V : Δ(R_k, R2) = moyenne sur les instances de V(R_k) − V(R2), à δ fixé ; X = 1 − V en est la lecture miroir (même intervalle, signe opposé).
- **Exploitabilité par tour et moyenne sur les tours (principale pour HR2)** : (iii)_t = détection de la meilleure réponse du tour t contre la défense déployée au tour t (départs du v4, `departs` = 4, plus l'attaque précédente, 256 échantillons de Monte-Carlo), sur 19 998 échantillons frais ; X_t = 1 − (iii)_t ; **X̄ = (1/T) Σ_{t=1}^{T} X_t** par trajectoire (`exploitabilite_moyenne_tours`, garde : dans [0 ; 1]) ; contraste **D̄(R_k, R2)** = moyenne sur les instances de X̄(R_k) − X̄(R2), à δ fixé (signe de l'exploitabilité : + = R_k plus exploitable). X̄ ≠ X finale même à T = 1 (gel v2 § 4).
- **R3′** : valeur du jeu restreint à chaque tour (après la colonne de l'attaque du tour, avant le moniteur nouveau) et en finale (programme linéaire du v4) ; descriptif, à côté de (iii)_t.
- **(ii) familles tenues à l'écart** : 50 lois par tâche tirées de RACINE_DECISION_TENUE (deux sous-familles du v4, 3 999 échantillons par loi), jamais passées à un entraînement (essai `test_tenues_jamais_vues_par_l_entrainement`, R0 comprise) ; score = moyenne des 50 taux, par tour (défense déployée) et en finale ; sous-familles recopiées. **(i) familles vues** : descriptif.
- **Condition d'application** (R2 : verdict ; R0, R1, R3, R4 : descriptif) : matrice H (ligne s = moniteur du tour s, colonne t = attaque du tour t ; pour R3, moniteurs un à un ; pour R0, T + 1 lignes identiques, M0), **I1** = moyenne de (iii) aux tours 5–8 moins aux tours 1–4 ; **I2** recopié (R0 : 0 par construction) ; **I3** = part des tours t ≥ 3 où le déplacement de l'attaque est plus proche (cosinus) d'une attaque d'un tour ≤ t − 2 que de celle du tour t − 1 ; **valeur nulle 0,7345** à T = 8 ; l'indicateur lu est I3 − 0,7345. Fonctions du v4 inchangées. **Réserve (CL-13)** : I3 est une part sur 6 tours (multiples de 1/6), bornée en 1, donc I3 − nul borné en +0,2655 ; au plafond, les percentiles d'un rééchantillonnage sont peu fiables (voir Table D, saturation).
- **Coût** : temps processeur de la trajectoire et de la finale (`time.process_time`) ; nombre d'appels à `scipy.optimize.minimize` (L-BFGS-B des entraînements, SLSQP de l'attaquant ; compteur posé sur la copie chargée du v4) ; nombre d'appels à `linprog` ; nombre d'entraînements ; nombre de départs de l'attaquant ; **paramètres déployés par requête** (`parametres_deployes` : 7 pour R0, R1, R2, R4 ; 63 pour R3) ; `parametres_stockes` recopié avec l'explication CL-09 (toutes les règles gardent la liste des moniteurs pour H : 63 pour R1 à R4, 7 pour R0). Descriptif ; ratios contre R2 par tâche.
- **Dégénérescence de R4** : cosinus entre le moniteur nouveau et le dernier moniteur à chaque tour, moyenne par tâche (≈ 1 : la défense ne bouge plus) ; liste par tâche rendue par l'analyse (`cos_consecutif_par_tache`, CL-11) ; seuil S12 appliqué par le lecteur. R0 : 1 par construction, hors S12.
- **Contrôles** : fausses alertes de chaque défense finale sur 20 000 échantillons propres indépendants (garde α ± 0,005) ; V standard − V renforcé par variante ; **écart des contrastes sur V entre attaquant standard seul et renforcé seul** (rendu par l'analyse, déclencheur 5, CL-11) ; poids finaux de R3 (support, pureté, plus petit poids maximal parmi les équilibres) ; statuts de l'optimiseur, départs non finis, réponses à la limite ; entraînements non convergés (S18 = 0,10 par tâche, v4) ; reproductibilité bit à bit du moniteur du tour 0 ; R0 : zéro entraînement (compteur).
- **Intervalles** : rééchantillonnage apparié des instances, 20 000 tirages, quantiles linéaires 0,3125 %, 0,625 %, 1,25 %, 2,5 %, 5 % et symétriques (comme le v4) ; graines `SeedSequence(entropy=RACINE_DECISION, spawn_key=(code_delta, code, 0, 0, 99))`, code = 200 + 100 × j + rang de la variante pour les contrastes (j = 0 : V ; 1 : (ii) ; 2 : X finale ; **8 : X̄**, soit 1000 + rang, sans collision avec les indicateurs), 500 + 100 × j + rang pour les indicateurs (j = 0 : I1 ; 1 : I3 − nul ; 2 : I2) ; rangs R0 0, R1 1, R2 2, R3 3, R4 4.

## Seuil

**Tous les seuils ci-dessous ont été retenus par Lazar le 1er novembre 2026 (≈ 15:30 UTC ; `registres/decisions.md`, R-962 : « go tout »), aux valeurs recommandées du brouillon 2 ; aucun défaut de 48 heures n'a eu à s'appliquer ; les recommandations du brouillon 2 sont conservées sous chaque valeur pour la traçabilité. Aucun défaut ne s'applique au lancement d'une course décisive (nœud de décision : GO exigé).** S4, S7, S9, S11 et S13 sont des champs de la configuration (identité à régénérer s'ils changent) ; S1, S2, S3, S5, S6, S8, S10, S12, S15 sont appliqués par le lecteur R13 ou par la commande.

**S1 — marge d'effet d'intérêt sur V et sur X̄ (Tables A, B, B′)** — Valeur : **m = 0,02**, retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Recommandation du brouillon 2 : **m = 0,02** (deux fois α ; = S1 et S6 du v4), par principe ; la même marge pour X̄ (même échelle [0 ; 1], même nature de taux).

**S2 — erreur de première espèce et corrections (CL-15)** — Valeur : **5 % bilatéral par famille** (cinq familles, bornes B2, B8, E8 ci-après), retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Recommandation du brouillon 2 : **5 % bilatéral par famille**, cinq familles, une par table : Table A (plomberie, 2 δ : **B2** = [q0,00625 ; q0,99375]) ; Table B (V finale : 4 règles R0, R1, R3, R4 × 2 δ = 8 tests : bornes **B8** = [q0,003125 ; q0,996875], **exactes pour 8** ; équivalence **E8** = [q0,00625 ; q0,99375]) ; Table B′ (X̄ : 4 × 2 = 8 tests : B8, E8) ; Table C ((ii), 4 × 2 = 8 tests : B8) ; Table D (R2, 2 δ : B2). Réserve héritée du v4 : les percentiles d'un rééchantillonnage peuvent dépasser le nominal d'un facteur 2 près des frontières (brouillon 4, S2) ; aucune simulation de taille par rééchantillonnage réel (voir S3).

**S3 — puissance visée** — Valeur : **≥ 0,8 pour la classe prédite de P1 à un effet ≥ 0,035 et pour « sans régression à S5 près » de R4 sur (ii) sous effet nul**, retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Recommandation du brouillon 2 : **≥ 0,8 pour la classe prédite de P1 à un effet ≥ 0,035 et pour « sans régression à S5 près » de R4 sur (ii) sous effet nul**. Calcul : contre-lecture 1, § 5 (écarts-types des contrastes appariés du pilote d'essai v1, 6 instances par δ ; erreur-type à N = 100 = sd/10 ; approximation normale des bornes : B8 bas ≈ est − 2,734 × erreur-type, B2 ≈ est − 2,498 × erreur-type ; puissance 0,8 ⇔ |Δ − seuil| ≥ (z + 0,842) × erreur-type) : puissance ≈ 1 pour P1 à l'effet du contexte v4 (+0,13), 0,89 ; 0,95 à 0,04, **≈ 0,5 à l'effet m exactement** (règle « est ≥ S1 et borne basse > 0 », comme au v4) ; Table B pour R1 et R4 sur V : erreur-type ≈ 0,001, toute différence vraie ≥ 0,005 est démontrée et « ≈ » a une puissance ≈ 1 sous effet nul ; Table C pour R4 au δ 1,6 : 0,75 à N = 100 sous effet nul (sd 0,059), 0,8 à N ≈ 115 ; « régression avérée » pour R3 à −0,06 : ≈ 1, à −0,04 : 0,72 ; Table D : I1 quasi certain, I3 − nul saturé au δ 1,6 (CL-13). **Complément de ce brouillon pour X̄ (même méthode, même fichier du pilote v1, calcul de l'auteur, déclaré)** : écarts-types des contrastes appariés sur X̄ : R1 − R2 0,051 ; 0,032 (δ 1,4 ; 1,6), R3 − R2 0,043 ; 0,023, R4(λ*) − R2 0,016 ; 0,012 ; erreurs-types à N = 100 : 0,0051 ; 0,0032 pour R1 ; puissance de « R2 > R1 » (borne basse B8 > m) : à un effet vrai de 0,04, 0,88 ; ≈ 1 ; à 0,03, 0,22 ; 0,65 ; **à l'effet m = 0,02 exactement, ≈ 0 (la classe exige borne basse > m)** ; « R2 ≳ R1 » à 0,02 : 0,88 ; ≈ 1. Pour R0 (absent du pilote v1 ; 2 instances par δ au pilote v2), aucun écart-type opposable : par analogie avec les règles à moniteur unique (sd ≈ 0,01 sur V), Table B tranchera R0 presque sûrement. Réserve : écarts-types sur 6 instances, incertains d'un facteur 1,5 ; aucune simulation à la manière de M4 du v4 ; racine 20266401 non employée (option : rééchantillonnage réel, 1 000 répétitions sur les 12 tâches du pilote v1, ≈ 1 min de processeur, si Lazar le veut : **non fait** — option non demandée par Lazar le 1er novembre 2026, qui a retenu la recommandation telle quelle (R-962) ; la racine 20266401 reste réservée et non employée).

**S4 — nombre d'instances N par δ** — Valeur : **N = 100**, retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Recommandation du brouillon 2 : **N = 100** (champ `n_instances`, = v4) ; coût au § Plan 5.

**S5 — tolérance de non-régression sur (ii)** — Valeur : **0,02**, retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Recommandation du brouillon 2 : **0,02** (= S1).

**S6 — réglage de R4 : λ* et référence** — Valeur : **λ* = 0,3, référence « moyenne » (option (a) ci-dessous ; LAMBDA_RETENU = 0.3, REFERENCE_RETENUE = moyenne du bloc sous l'identité)**, retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Règle du gel v1 § 3 appliquée au pilote d'essai v1 : λ* = valeur de la grille {0,03 ; 0,1 ; 0,3 ; 1 ; 3} qui maximise la moyenne de V(R4) sur les 12 tâches du pilote (δ confondus), égalité à 0,005 près → la plus petite λ, **puis « dernier »** (règle du code, essai `test_analyse_et_choix_lambda`, CL-14) ; même règle pour la référence. **Résultat mécanique : LAMBDA_RETENU = 0.3, REFERENCE_RETENUE = moyenne** (bloc ci-dessus, vérifiés par le code ; cosinus consécutif moyen 0,958 ; 0,943 au pilote v1). **Trois faits recalculés par la contre-lecture 1 (§ 4 M1), déclarés** : (1) le maximum brut de la règle est R4[dernier, λ = 1] (moyenne de V 0,1051) ; R4[moyenne, λ = 0,3] (0,1040) n'est retenue que par la tolérance d'égalité (écart 0,0011 ± 0,0011 d'erreur-type, à 0,005 près → plus petite λ) ; or R4[dernier, λ = 1] est dégénérée au sens de S12 dans 4 tâches sur 6 au δ 1,4 (cosinus ≥ 0,999) : la tolérance a, par chance, écarté une variante qui aurait déclenché S12 ; (2) les écarts entre les dix variantes vont de 0,000 à 0,020 avec des erreurs-types de 0,001 à 0,006 sur 12 tâches : λ* est « une valeur raisonnable », pas un optimum démontré ; (3) R4[moyenne, λ = 0,3] n'est pas dégénérée sous S12 (part des tâches à cosinus ≥ 0,999 : 1/6 et 0/6 ; cosinus par tâche de 0,86 à 0,999). Est-ce un choix sur résultat ? Oui au sens strict (fonction des données du pilote v1), non au sens de R1 (racine d'essai indépendante, règle écrite d'avance, aucune racine de décision lue). Options : (a) garder la règle et son résultat (λ* = 0,3, « moyenne »), lire R4 avec S12 — **recommandation, confiance 0,6**, rien n'est changé après lecture ; (b) restreindre la grille et reprendre la règle — choix après lecture, à éviter ; (c) autre réglage posé par Lazar (identité à régénérer). **Défaut sous 48 heures : (a) — sans objet, (a) retenue par Lazar le 1er novembre 2026 (R-962).**

**S7 — nombre de tours T** — Valeur : **T = 8**, retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Recommandation du brouillon 2 : **T = 8** (= v4 ; valeur nulle de I3 = 0,7345 ; pair : X finale de R1 lit le moniteur pair, déclaré ; HR2 lue sur X̄).

**S8 — plafond de temps** — Valeur : **`timeout 3600`** (externe, sur 2 processus ; 600 s de processeur par tâche en garde interne), retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Recommandation du brouillon 2 : `timeout` externe égal à **deux fois** la projection au § Plan 5 à l'efficacité mesurée, soit **`timeout 3600`** sur 2 processus (projection ≈ 30 min) ; 600 s de processeur par tâche (garde interne `plafond_cpu_tache_s`, v4). Condition de lancement : machine sans autre calcul lourd ; charge relevée par `uptime` avant lancement et consignée ; réserve : la charge peut monter pendant le run (CM4-02 du v4).

**S9 — taux de fausses alertes α et tolérances** — Valeur : **α = 0,01** (garde ± 0,005 par défense finale ; déclencheur à 0,001 sur la moyenne d'une règle), retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Recommandation du brouillon 2 : **α = 0,01** ; garde |taux mesuré − α| ≤ 0,005 par défense finale ; déclencheur |moyenne d'une règle − α| > 0,001 dans un δ.

**S10 — déclencheur « trop beau / trop mauvais »** — Valeur : **la recommandation ci-après, telle quelle** (V ≥ 0,99 ; V ≤ 2α pour les cinq variantes ; Δ(R3, R2) > 0,30 ; |D̄| > 0,30), retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Recommandation du brouillon 2 : audit si la moyenne de V d'une règle ≥ 0,99 dans un δ, ou si la moyenne de V ≤ 2α pour les cinq variantes dans un δ (jeu dégénéré), ou si Δ(R3, R2) dépasse 0,30 dans un δ (au-delà du double du contexte v4), ou si |D̄(R_k, R2)| dépasse 0,30 pour une règle. Pas de bande centrée sur un pilote d'essai (trop peu d'instances ; déclaré).

**S11 — budgets de comportement δ** — Valeur : **δ = (1,4 ; 1,6)**, retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Recommandation du brouillon 2 : **δ = (1,4 ; 1,6)** (`DELTAS_V4`, recalibrés au v4 sur A seul ; A = R2 : le calibrage vaut pour la règle de référence).

**S12 — dégénérescence de R4** — Valeur : **0,999, sur plus de la moitié des tâches d'un δ**, retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Recommandation du brouillon 2 : R4 « non exercée » à un δ si le cosinus consécutif moyen de R4(λ*) est ≥ **0,999** sur plus de la moitié des tâches de ce δ (la défense ne bouge plus ; part calculée par le lecteur R13 sur `cos_consecutif_par_tache`) ; la classe de la Table B est alors recopiée avec la mention « R4 ≈ défense figée », sans verdict sur HR3, et **comparée à R0** (recopiée). **Déclaré** : le seuil 0,999 a été **posé après le pilote v1, en voyant les cosinus** (il sépare, au pilote v1, λ ≤ 0,3 (0,86 à 0,999) de λ ≥ 1 (0,996 à 1,000)) ; il est sans effet sur la variante retenue au pilote v1 (1/6, 0/6). R0 est hors S12 (cosinus 1 par construction). **Défaut sous 48 heures : 0,999, plus de la moitié des tâches — sans objet, retenu par Lazar le 1er novembre 2026 (R-962).**

**S13 — oracle du défenseur** — Valeur : **« détection »**, retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Recommandation du brouillon 2 : « détection » (v4, S13). S18 du v4 (0,10, convergence) repris dans la configuration.

**S15 — marge de la Table D (I1)** — Valeur : **S15 = 0,02**, retenue par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2. Recommandation du brouillon 2 : **S15 = S1 = 0,02** (= S15 du v4) (CL-04).

## Plan d'analyse

### 1. Monde
Celui du v4 (brouillon 4, Plan 1) : loi propre N(0, I_6) ; loi cible à 3 composantes, moyennes de norme 4, écarts-types 1 ; loi d'attaque appariée dans la boîte (|μ| ≤ 5, σ ∈ [0,5 ; 1,5]) ; contrainte de comportement : racine de la moyenne sur k du carré de la distance de Wasserstein d'ordre 2 entre composantes appariées ≤ δ. Configuration `CONFIG_V4` inchangée (empreinte `3fbb27fc…` du bloc d'identité, la même que le v4).

### 2. Règles (gel v2 § 2 ; boucle commune `trajectoire_regle`)
Tour 0 commun : moniteur linéaire M0 entraîné contre la loi cible (reproductibilité bit à bit exigée). Pour t = 1 … T : l'attaquant calcule une meilleure réponse contre la défense déployée (graines du code de la règle : R0 20, R1 21, R2 1, R3 2, R4 24 ; départ supplémentaire = attaque précédente) ; puis :
- **R0** : aucune mise à jour ; M0 reste déployé ; zéro entraînement (essai par instrumentation `test_R0_ne_reentraine_jamais_instrumentation`) ; l'attaquant seul évolue d'un tour à l'autre (graines et départ supplémentaire).
- **R1** : moniteur linéaire entraîné contre la **seule attaque du tour** ; seul déployé. **La loi cible, présente dans l'historique uniforme de R2 et R4 (coup du tour 0), n'y entre plus** après le tour 0 (CL-10).
- **R2** : moniteur linéaire entraîné contre le mélange uniforme de toutes les attaques passées, la loi cible comprise ; seul déployé (= A du v4 au bit : essai `test_R2_reproduit_A_du_v4_au_bit`).
- **R3** : p = équilibre du défenseur sur la matrice G des détections croisées ; q = équilibre de l'attaquant après la colonne nouvelle ; moniteur linéaire entraîné contre q ; défense = tous les moniteurs aux poids p (= B du v4 au bit : essai `test_R3_reproduit_B_du_v4_au_bit`) ; valeur du jeu restreint recopiée (R3′).
- **R4** : comme R2, objectif de détection plus 2λ*(1 − cos(w, u)), u = direction de référence gelée (S6) ; à λ = 0, identique à R2 à entrée égale (essai).
Pour chaque règle, défense finale figée ; l'attaquant joue en dernier (standard puis renforcé) ; finale « légère » du v4 plus (ii) finale et (i) sur les attaques vues. Les règles ne partagent que M0, la loi cible, le propre d'entraînement de chaque tour, les lois tenues et les échantillons de calibration. Le rang d'exécution des variantes (R0 en premier) ne change aucun tirage (clés de graine par code de règle ; R2 = A au bit vérifié).

### 3. Graines (R9)
- **RACINE_DECISION = 20266201**, **RACINE_DECISION_TENUE = 20266202** (décision, jamais employées ; refusées par `gen_regles` sans préenregistrement scellé, conforme et identifié). Racines d'essai v2, écrites au gel v2 avant emploi : 20266501 / 20266502 (pilote d'essai v2) ; 20266511 à 20266513 (essais du code v2) ; 20266401 (réservée, simulations) ; 20266521 (réservée).
- **Refusées par garde** (`exiger_racine_permise_regles`) : les racines de décision du v4 (20261201, 20261202), toutes les racines déjà employées par les arènes v1 à v4 et leurs contre-lectures, **les racines d'essai de la v1 des règles (20266101, 20266102, 20266301 à 20266303), employées**, la plage 20265001–20265999 (autre session), la plage 20264001–20264999 (réservée au v4), toute racine absente du gel v2.
- Chaque tirage : `numpy.random.SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, rôle, …))`, numpy ≥ 1.25, rôles du v4 ; le remplacement de `gen` ne change que la liste des racines permises, pas le schéma.

### 4. Comparaisons et multiplicité (CL-15)
- **Table A** : Δ(R3, R2) sur V, B2 (plomberie / HR1). **Table B** : Δ(R0, R2), Δ(R1, R2), Δ(R3, R2), Δ(R4, R2) sur V, B8 et E8, marge m (HR0, HR3 ; R1 et R3 recopiées). **Table B′** : D̄(R0, R2), D̄(R1, R2), D̄(R3, R2), D̄(R4, R2) sur X̄, B8 et E8, marge m (HR2 ; les autres recopiées). **Table C** : les quatre contrastes sur (ii), B8, tolérance S5 (HR4 ; R0 recopiée). **Table D** : I1 et I3 − 0,7345 de R2, B2, marge S15 (HR5). **Table E** : coût, descriptif (ratios et ordre). **Descriptives** : X par tour et en finale, X̄ ; R3′ ; I1, I2, I3 − nul de R0, R1, R3, R4 ; matrices H ; cosinus consécutifs par tâche ; poids de R3 (support, pureté, pureté forcée) ; contrôles.
- « Confirmée » = intersection-union sur les deux δ ; « réfutée » = union protégée par la correction (une famille par table, 5 % bilatéral par famille ; B8 exacte pour 8 tests).

### 5. Ordre d'exécution, arrêt et reprise
(1) Essais du code (`pytest`, 25 essais, dont l'essai lent de parité avec `REGLES_ESSAIS_LENTS=1`) ; (2) variantes de la décision : **R0, R1, R2, R3, R4(λ*)** (cinq variantes retenues par Lazar le 1er novembre 2026, R-962 ; 5 trajectoires par tâche ; fixées par le code : la commande `decision` n'accepte qu'un λ et une référence ; la grille complète est retirée, CL-07) ; (3) une seule invocation `PYTHONPATH=src OMP_NUM_THREADS=1 timeout <S8> python3 arene_regles_defense_v2.py decision --prereg prereg/<nom>.md --instances 0:N --run-id <AAAAMMJJ-HHMMSS-regles-defense-v2> --lambda <λ*> --reference <réf> --processus 2`, arbre git propre, machine sans autre calcul lourd ; le code revérifie le gel sur disque après l'autorisation (CL-08) ; manifeste et PID (scellés) sous `runs/<run-id>/`, résultats et analyse rattachés sous `diag/<run-id>/` (bibliothèque `manifeste.py`, comme le v4) ; (4) lecture par un sous-agent neuf (R13), qui applique les tables ; (5) **coordination avec la course du v4** : même monde, même machine ; ordre des deux courses : **après la course du v4**, retenu par Lazar le 1er novembre 2026 (R-962 : « go tout »), valeur recommandée du brouillon 2, pour ne pas partager la machine (règle de lancement S8) ; la course des règles ne lit rien de celle du v4 (racines différentes).
- **Coût projeté** (pilote d'essai v2, racine d'essai, 4 tâches à 5 variantes, T = 8 ; § 1 du `pilote-essai-regles-defense-v2.md`) : 17,3 s de processeur par tâche (R0 ≈ 2,0 s, R1 ≈ 2,6 s, R2 ≈ 2,8 s, R3 ≈ 6,6 s, R4 ≈ 3,2 s, trajectoire et finale) → 200 tâches ≈ 58 min de processeur, ≈ 30 min de mur sur 2 processus à l'efficacité mesurée 0,96 (≈ 14 min sur 4 processus) ; pilote v2 : 69 s de processeur, 36 s de mur, aucune garde déclenchée, 0 entraînement non convergé sur 136, 0 départ non fini sur 2 540 ; S8 retenu : `timeout 3600`. Cohérent avec le pilote v1 (≈ 15 s par tâche à 4 variantes).
- **Reprise après arrêt** : comme le v4 (Plan 5 du brouillon 4) : arrêt externe → arrêt par PID des processus consignés, garde « aucun orphelin » (`orphelins --pids …`), puis une reprise complète, même code, mêmes racines, nouvel identifiant ; seconde interruption → non concluant ; arrêt par garde interne → non concluant, version nouvelle ; aucun point de reprise partiel.

### 6. Historique de conception (déclaré)
1. Demande du directeur (1er novembre 2026). 2. Gel v1 (09:52 UTC), code v1, essais, pilote d'essai v1 (13 variantes, 6 instances par δ), brouillon 1 (10:09 UTC) — par un premier sous-agent. 3. Contre-lecture 1 (10:20 UTC) : constats CL-01 à CL-16, calcul de puissance, trois faits sur λ* ; **l'origine de la remarque CL-05 (métrique de HR2) est le pilote v1** (période 2 de R1 visible sur (iii)_t) : déclaré. 4. Hypothèse de travail de la session principale (option (b) + R0 ; soumise au directeur). 5. **Gel v2 (10:46 UTC, avant toute exécution du code v2)**, code v2 (copie de la v1 : X̄, R0, identité v2, racines neuves, CL-08, CL-11), 25 essais passés (essai lent de parité compris : une instance, configuration complète, racine d'essai v2, |ΔX̄| = 0,021, |ΔX finale| = 0,131 entre T = 3 et T = 4 pour R1), pilote d'essai v2 (10:52 UTC : 2 instances × 2 δ × 5 variantes, T = 8, racines 20266501 / 20266502). 6. Ce brouillon 2 : **viennent des pilotes** λ*, la référence (pilote v1, règle du gel v1 § 3), les écarts-types du calcul de puissance (pilote v1, méthode de la contre-lecture 1, dont le complément sur X̄ calculé par l'auteur), la projection de temps (pilote v2) ; **rien d'autre** ; l'auteur a vu les tables des deux pilotes (celles du v1 par la contre-lecture 1 et le résumé v1 ; celles du v2 en vérifiant que X̄ et R0 sortent) ; les signes et ordres de grandeur sont posés par principe et par le contexte du v4 ; un contre-lecteur neuf vérifiera que les prédictions ne les recopient pas. 7. **Brouillon 3 (≈ 15:40 UTC)** : décisions de Lazar du 1er novembre 2026 (≈ 15:30 UTC, R-962 : « go tout ») reportées par un sous-agent rédacteur neuf — option (b) + R0, S1 à S15 et les marqueurs aux valeurs recommandées du brouillon 2, commit du code d'analyse relevé ; aucune hypothèse, prédiction, métrique, table ni plan changés ; bloc d'identité recopié tel quel.

## Critères de lecture gelés

Un sous-agent neuf (R13) applique ces tables telles qu'écrites, **de haut en bas ; la première ligne vraie décide**. Notations à δ fixé : est = moyenne ; qX = quantile X ; **B2** = [q0,00625 ; q0,99375] ; **B8** = [q0,003125 ; q0,996875] ; **E8** = [q0,00625 ; q0,99375].

**V0** = aucune condition de la liste d'arrêt ∧ tâches exécutées = 2 × N ∧ racines du manifeste = RACINE_DECISION et RACINE_DECISION_TENUE ∧ empreintes du code, de l'arène v4, du gel v2, de la configuration et de la bibliothèque = celles du texte scellé ∧ **empreinte du gel v2 sur disque = `9977d7df…` (vérifiée par le code en décision et par le lecteur, CL-08)** ∧ λ et référence de la commande = LAMBDA_RETENU et REFERENCE_RETENUE ∧ cinq variantes par tâche (R0, R1, R2, R3, R4) ∧ une seule invocation ayant écrit des résultats (au plus une reprise complète consignée).

**Déclencheurs d'audit (R4), symétriques** — un seul suffit ; l'effet bloquant est écrit :
1. **Contradiction d'une prédiction ferme, dans les deux sens** : P1 (Table A ligne 5 ou 6 à un δ), P12 (Table B′ : classe autre que « R2 > R1 » à un δ), P13 (Table B : classe autre que « R2 > R0 » à un δ — y compris « ≈ », attendue au vu de l'indice du pilote v1 : l'audit est alors une relecture du code de R0 et du compteur d'entraînements), P7 (Table D autre que ligne 2 à un δ), P11 ; *bloque* la table contredite.
2. **Trop beau / trop mauvais** (S10) ; *bloque* toutes les tables.
3. **Mélange R3 dégénéré** : poids de R3 purs (un poids ≥ 1 − 10⁻⁹) sur plus de la moitié des tâches d'un δ ; *bloque* Tables A, B et B′ pour R3.
4. **R4 dégénéré** (S12) : lecture « R4 ≈ défense figée », comparée à R0 ; *bloque* le verdict de HR3 seulement.
5. **Optimiseur** : moyenne de (V standard − V renforcé) > 0,01 pour une variante dans un δ ; ou un contraste de la Table B dont l'écart « standard seul − renforcé seul » (rendu par l'analyse) dépasse 0,01 en valeur absolue ; *bloque* toutes les tables.
6. **Dérive des fausses alertes** : |moyenne des fausses alertes finales d'une variante − α| > 0,001 dans un δ ; *bloque* toutes les tables.
7. **Conforme et trop propre (R4)** : P1, P12 et P13 conformes aux deux δ **et** P7 conforme, ou P5 conforme (contre l'indice du pilote v1) : *effet* : relecture du code par un sous-agent neuf et vérification que R2 = A et R3 = B au bit sur deux tâches de la décision (rejeu par la boucle commune avec `v4.trajectoire` sur la copie chargée), et que R0 n'a appelé aucun entraînement (compteur) ; *bloque* la phrase de synthèse jusqu'au rapport.

**Contenu de l'audit** : relecture du code par un sous-agent neuf ; vérification que R3 déploie les poids du programme linéaire, R1 un moniteur entraîné sur la seule dernière attaque (compte des échantillons d'entraînement), R4 la pénalité à λ*, R0 M0 inchangé (zéro entraînement, 7 paramètres stockés) ; option : attaquant indépendant du v4 branché sur les défenses finales des cinq variantes (code v3). **Issue** : « artefact trouvé » si le rapport scellé constate une erreur de code ou un chemin non exercé ; sinon « pas d'artefact ».

### Table A — contrôle de plomberie et HR1, Δ(R3, R2) sur V (bornes B2)

| # | Condition | Verdict |
|---|---|---|
| 0 | V0 fausse | **non concluant** ; aucune lecture |
| 1 | un déclencheur qui bloque la Table A est présent et l'audit n'est pas rendu | **non concluant (audit en attente)** |
| 2 | audit rendu, artefact trouvé | **non concluant** ; version nouvelle |
| 3 | dans un δ, la moyenne de V ≤ 2α pour les cinq variantes | **non concluant** : jeu dégénéré |
| 4 | est ≥ S1 ∧ borne basse B2 > 0, aux deux δ | **HR1 confirmée** (le mélange d'équilibre bat l'historique) |
| 5 | borne haute B2 < 0 dans au moins un δ | **HR1 réfutée** (l'historique bat le mélange) |
| 6 | sinon | **HR1 non démontrée** |

### Table B — classement de chaque variante k ∈ {R0, R1, R3, R4} contre R2 sur V, à chaque δ (marge m = S1 ; Δ = V(R_k) − V(R2) : + = R_k moins exploitable)

| Classe | Condition | Sens |
|---|---|---|
| « R_k > R2 » | borne basse B8 > m | R_k moins exploitable d'un effet d'intérêt |
| « R2 > R_k » | borne haute B8 < −m | R_k plus exploitable d'un effet d'intérêt |
| « ≈ » | E8 ⊂ ]−m ; +m[ | équivalentes à la marge près |
| « R_k ≳ R2 » | borne basse B8 > 0 | R_k meilleure, effet d'intérêt non démontré |
| « R2 ≳ R_k » | borne haute B8 < 0 | R2 meilleure, effet d'intérêt non démontré |
| « ? » | sinon | non tranché |

Verdicts : **HR0 confirmée** si « R2 > R0 » aux deux δ ; **réfutée** si « R0 > R2 », « R0 ≳ R2 » ou « ≈ » à un δ ; sinon non tranchée. **HR3 confirmée** si « R4 > R2 », « R4 ≳ R2 » ou « ≈ » aux deux δ (et S12 non déclenché) ; **réfutée** si « R2 > R4 » à un δ ; sinon non tranchée ; sous S12, « R4 ≈ défense figée », sans verdict, classe de R0 recopiée à côté. **R1 et R3 : classes recopiées sans verdict** (HR2 par la Table B′ ; HR1 par la Table A). Les classes sont toujours recopiées, avec est [B8].

### Table B′ — classement de chaque variante k ∈ {R0, R1, R3, R4} contre R2 sur X̄, à chaque δ (marge m = S1 ; D̄ = X̄(R_k) − X̄(R2) : + = R_k **plus** exploitable)

| Classe | Condition | Sens |
|---|---|---|
| « R2 > R_k » | borne basse B8 de D̄ > m | R_k plus exploitable au fil des tours, d'un effet d'intérêt |
| « R_k > R2 » | borne haute B8 de D̄ < −m | R_k moins exploitable d'un effet d'intérêt |
| « ≈ » | E8 ⊂ ]−m ; +m[ | équivalentes à la marge près |
| « R2 ≳ R_k » | borne basse B8 > 0 | R2 meilleure, effet d'intérêt non démontré |
| « R_k ≳ R2 » | borne haute B8 < 0 | R_k meilleure, effet d'intérêt non démontré |
| « ? » | sinon | non tranché |

Verdict : **HR2 confirmée** si « R2 > R1 » aux deux δ ; **réfutée** si « R1 > R2 », « R1 ≳ R2 » ou « ≈ » à un δ ; « ? » ou « R2 ≳ R1 » à un δ : **non tranchée**. R0, R3, R4 : classes recopiées sans verdict (P14, P15). Les classes sont toujours recopiées, avec est [B8].

### Table C — attaques tenues à l'écart, Δ(R_k, R2) sur (ii), k ∈ {R0, R1, R3, R4}, bornes B8, tolérance S5 (lecture par règle et par δ)

| # | Condition | Lecture |
|---|---|---|
| 1 | borne haute < −S5 | **régression avérée au-delà de la tolérance** |
| 2 | borne haute < 0 ∧ borne basse > −S5 | **régression démontrée, sous la tolérance** |
| 3 | borne haute < 0 | **régression démontrée, ampleur non tranchée** |
| 4 | borne basse > 0 | **amélioration sur (ii)** |
| 5 | borne basse > −S5 | **sans régression à S5 près** |
| 6 | sinon | **régression non exclue (imprécis)** |

HR4 : conforme pour R3 et R1 si lignes 1 à 3 aux deux δ ; conforme pour R4 si lignes 4 ou 5 aux deux δ ; R0 : ligne recopiée sans verdict. La lecture sans seuil (est [B8]) est recopiée dans tous les cas.

### Table D — condition d'application (R2), par δ, bornes B2, marge S15 (recopiée en entier de la Table 5 du brouillon 4 du v4, CL-04)

| # | Condition | Lecture |
|---|---|---|
| 1 | borne basse de I1 > S15 | **R2 progresse** |
| 2 | borne haute de I1 < S15 ∧ borne basse de (I3 − 0,7345) > 0 | **ne progresse pas, retours au-delà du hasard (cycle)** |
| 3 | borne haute de I1 < S15 ∧ borne haute de (I3 − 0,7345) < 0 | **ne progresse pas, sans retours au-delà du hasard** |
| 4 | borne haute de I1 < S15 | **ne progresse pas, forme indéterminée** |
| 5 | sinon | **indéterminé** |

Verdict : condition vérifiée si lignes 2 à 4 aux deux δ. **Saturation (CL-13)** : I3 − nul est borné en +0,2655 ; si plus de 90 % des tâches d'un δ sont à ce plafond, la ligne 2 est lue avec la mention « indicateur saturé » et I3 est recopié par tâche. I1, I3 − nul de R0, R1, R3, R4 recopiés sans verdict (P8, P9 descriptifs).

### Table E — coût (descriptif, sans verdict)

Par variante et par δ : processeur moyen de la trajectoire et de la finale, ratio contre R2, appels à l'optimiseur, programmes linéaires, entraînements, paramètres déployés par requête (et stockés, avec l'explication CL-09) ; ordre observé recopié et comparé à P10.

**Phrase de synthèse** (lecteur R13, en recopiant, sans rien omettre) : « Table A : … ; Table B (V) : R0 …, R1 …, R3 …, R4 … (par δ, est [B8]) ; HR0 : … ; HR3 : … (S12 : …) ; Table B′ (X̄) : R0 …, R1 …, R3 …, R4 … (par δ, est [B8]) ; HR2 : … ; Table C : … (par règle et δ, est [B8]) ; Table D : … (I1, I3 − 0,7345, I2 de R2 avec intervalles ; saturation : …) ; R3′ : valeur du jeu restreint par tour et finale ; Table E : … ; déclencheurs : … ; issue des audits : … ; portée : résultat local au monde, à l'oracle, aux δ, à T, à λ* et à l'attaquant du tour pour X̄ ».

## Liste d'arrêt

Gardes de ce module (essais nommés dans `test_arene_regles_defense_v2.py`, R5 : cas sain et artefact, motif vérifié) et gardes du v4 réemployées (essais du v4, brouillon 4 § Liste d'arrêt).

| Condition | Action | Garde et essai |
|---|---|---|
| Lancement en décision sans préenregistrement scellé, conforme, identifié (identifiant V2, racines, configuration, empreintes du code v2, de l'arène v4, du gel v2, de la bibliothèque, versions, N, λ*, référence) | pas de départ ; aucune graine de décision | `autoriser_decision_regles`, `exiger_identite_prereg_regles` ; `test_decision_refusee_sans_prereg_scelle`, `test_bloc_identite_et_identite_prereg_sain_et_artefacts` |
| Graine tirée d'une racine de décision sans autorisation ; racine de décision du v4 ; racine déjà employée (v4, ou v1 des règles) ; plage d'une autre session ; plage du v4 ; racine non gelée ; racine tenue égale à la principale | arrêt | `gen_regles`, `exiger_racine_permise_regles`, `exiger_racines_essai_regles` ; `test_racines_sain_et_artefacts`, `test_cli_essai_refuse_racines_interdites_et_ecrasement` |
| Arène v4 absente ou modifiée (empreinte ≠ épinglée) | pas de chargement | `charger_arene_v4` ; `test_chargement_v4_empreinte_sain_et_artefacts` |
| Gel v2 absent, modifié, ou ne citant pas la racine (gel v1 présenté à la place : refusé) | arrêt (modes essai **et** décision, CL-08) | `exiger_gel_regles` ; `test_gel_v2_sain_et_artefacts` |
| Règle inconnue ; λ négatif ou non fini ; référence inconnue ; direction de référence nulle ; oracle autre que « détection » pour R4 | arrêt | `exiger_regle`, `exiger_lambda`, `direction_reference`, `entrainer_regularise` ; `test_regle_lambda_reference_gardes`, `test_entrainement_regularise_lambda_zero_egal_v4_et_lambda_fort_rapproche` |
| Taux de détection hors de [0 ; 1] (exploitabilité) ; X̄ sans tour ou hors de [0 ; 1] | arrêt | `exploitabilite`, `exploitabilite_moyenne_tours` ; `test_exploitabilite_sain_et_artefacts`, `test_X_barre_sain_et_artefacts` |
| R0 : la liste des moniteurs n'est plus [M0] (objet changé ou ajouté) | arrêt | `exiger_defense_figee` ; `test_garde_defense_figee_sain_et_artefact` ; instrumentation `test_R0_ne_reentraine_jamais_instrumentation` |
| Fichier de sortie ou de PID existant | arrêt (R12) | `_exiger_absent`, `_ecrire_nouveau` du v4 ; `test_cli_essai_refuse_racines_interdites_et_ecrasement` |
| Temps processeur d'une tâche > 600 s | arrêt | `exiger_plafond` du v4 ; `test_plafond_de_temps_processeur_sain_et_artefact` (branches R1 et R0) |
| Fausses alertes d'une défense finale hors de α ± 0,005 ; entraînements non convergés > 0,10 par tâche ; départs non finis > 5 % ; moniteur du tour 0 non reproductible ; programme linéaire non résolu ; loi d'attaque inadmissible ; moniteur non fini ou non calibrable | arrêt | gardes du v4 (`exiger_fpr`, `exiger_convergence`, `exiger_departs_finis`, `exiger_meme_moniteur`, `resoudre_jeu`, `exiger_admissible`, `Moniteur`) ; essais du v4 ; exercées ici par `test_chaque_regle_trajectoire_T3_petite_config_en_moins_de_30_s` (cas sains) |
| Processus de travail consigné encore vivant ; signal TERM | arrêt par PID (R10), aucune reprise avant `orphelins` sain | `_lancer`, `arreter_par_pid`, `exiger_aucun_orphelin` du v4 ; `test_cli_essai_ecrit_un_pilote_minuscule_et_orphelins` |
| Attaque tenue à l'écart passée à un entraînement | constat d'essai (jamais au run) | `test_tenues_jamais_vues_par_l_entrainement` (R0 à R4) |
| R2 ≠ A ou R3 ≠ B au bit ; R4(λ = 0) ≠ R2 à code égal ; R0 non reproductible à graine fixée ; X̄ ≠ X_1 à T = 1 | constat d'essai | `test_R2_reproduit_A_du_v4_au_bit`, `test_R3_reproduit_B_du_v4_au_bit`, `test_R4_lambda_zero_egal_R2_sur_la_trajectoire_a_code_de_graine_egal`, `test_R0_reproductible_a_graine_fixee_et_autre_racine_differente`, `test_X_barre_egale_X1_quand_T_vaut_1` |
| Parité de T : X̄ de R1 varie plus que X finale entre T = 3 et T = 4 (une instance, configuration complète) | constat d'essai lent (informe, ne bloque pas) | `test_lent_parite_de_T_X_barre_stable_X_finale_non_pour_R1` (`REGLES_ESSAIS_LENTS=1`) |
| Tâches ≠ 2 × N ; invocation hors § Plan 5 ; paramètre changé après lecture ; variantes ≠ 5 | V0 fausse | contrôle du lecteur R13 |
| Appel de modèle, réseau, dépense | arrêt (devis et GO exigés) | — |
| Lecture d'un résultat de décision avant scellement | arrêt et consignation (R1) | — |
| Marqueur de gabarit ou de décision de Lazar restant ; contre-lecture sans ses deux empreintes | pas de scellement | validateur `controle_ia.prereg.problemes` |

## Rôles

- Auteur du brouillon 1, du gel v1, du code v1 et du pilote v1 : premier sous-agent (Fable 5.1). Auteur du gel v2, du code v2, des essais v2, du pilote v2 et du brouillon 2 : sous-agent neuf (Fable 5.1).
- **Contre-lecture 1 (R2)** : faite (section Contre-lecture). **Contre-lecture 2 (courte)** : un sous-agent neuf qui n'a écrit ni ce texte ni le code v2 ni la contre-lecture 1 ; fichiers à lui donner explicitement : ce brouillon 3, le brouillon 2, le brouillon 1, la contre-lecture 1, `gel-regles-defense-v2.md`, `arene_regles_defense_v2.py`, `test_arene_regles_defense_v2.py`, `pilote-essai-regles-defense-v2.json` et `.md`, `pilote-essai-regles-defense-v1.json` et `.md`, `LISEZMOI-regles-defense-v2.md`, `donnees/argon-seul-convergence-v1/arene_melange_v4.py`. Points à juger en priorité : chaque constat CL-01 à CL-15 est traité comme la section Contre-lecture le dit ; les prédictions (P12 à P15 surtout) ne recopient pas les pilotes ; R0 ne réentraîne jamais (code et essai) ; la clé de rééchantillonnage de X̄ (1000 + rang) ne heurte rien ; la cohérence des verdicts HR0 à HR3 entre § Hypothèse, § Prédiction et Tables ; le bloc d'identité régénéré ; les familles de tests (S2).
- Lecteur de porte (R13) : sous-agent neuf, ni auteur ni contre-lecteur ; applique les Tables A à E ; verdict scellé, soumis à Lazar.
- Lazar : a tranché le 1er novembre 2026 (R-962 : « go tout ») l'hypothèse de travail (option (b) + R0), S1 à S15 et les marqueurs, aux valeurs recommandées du brouillon 2 ; donne le GO de l'exécution (processeur, aucune dépense ; ≈ 1 h de mur au plus).

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf (modèle Claude Fable 5.1), 1er novembre 2026, 10:12 à 10:20 UTC ; brouillon relu : `brouillon-prereg-regles-defense-v1.md`, empreinte `be08f4385dba0642ec857c96c67cc11c2d2acd09da026533d942fd7c87f1a48c` ; rapport : `docs/notes/convergence-defense-v1/regles-defense-v1/contre-lecture-prereg-regles-defense-v1.md`, empreinte `19ca1e283b579acadd4a91453e5d5268984f2aaabdea055e127d4de5a6938495` ; verdict « scellable après corrections ». Traitement de chaque remarque dans le brouillon 2 (conservé dans ce brouillon 4) :

| Constat | Traitement | Où |
|---|---|---|
| CL-01 (bloquant) trois définitions de « HR1 réfutée » | **accepté**, texte de la contre-lecture repris : HR1 par la Table A seule ; classe de R3 en Table B recopiée sans verdict ; déclencheur 1 sur les lignes 5 et 6 | § Hypothèse HR1 ; § Prédiction ; déclencheur 1 ; Table B |
| CL-02 (bloquant) deux définitions de « HR2 réfutée » | **accepté** : verdict par la table (B′ désormais) ; « ? » ou « R2 ≳ R1 » = non tranchée | § Hypothèse HR2 ; Table B′ |
| CL-03 (bloquant) HR3 : énoncé ≠ table | **accepté**, texte repris (classes « R4 > R2 », « R4 ≳ R2 », « ≈ », bornes B8 et E8) | § Hypothèse HR3 ; Table B |
| CL-04 (bloquant) Table D incomplète, S15 non défini | **accepté** : les cinq lignes de la Table 5 du brouillon 4 recopiées ; S15 défini | Table D ; S15 |
| CL-05 (bloquant ; métrique de HR2) | **option (b) retenue comme hypothèse de travail** (session principale ; décision de Lazar en attente) : X̄ préenregistrée, code v2, HR2 sur X̄, V finale de R1 descriptive, réserve de parité déclarée ; essai lent de parité ; famille séparée (Table B′) | § Résumé 2 ; § n'autorise pas ; HR2 ; Métrique ; Table B′ ; historique 3 et 5 |
| CL-06 (bloquant) indications contraires du pilote | **accepté** : paragraphe « Déclaré (CL-06) » après la table des prédictions, texte de la contre-lecture repris et étendu à X̄ et à P13 ; déclencheur 7 étendu | § Prédiction ; déclencheur 7 |
| CL-07 (moyen) grille complète non exécutable | **accepté** : option retirée ; variantes fixées à R0, R1, R2, R3, R4(λ*) | Plan 5 point 2 |
| CL-08 (mineur) gel non revérifié en décision | **accepté, dans le code v2** (`exiger_gel_regles(RACINES_DECISION)` après l'autorisation ; empreinte du gel dans le manifeste) et dans V0 | Plan 5 ; V0 ; liste d'arrêt |
| CL-09 (mineur) paramètres stockés | **accepté**, texte repris (déployés 7 / 63 ; stockés 63 pour R1 à R4, 7 pour R0, explication) | § Résumé 3 ; Métrique (coût) ; Table E |
| CL-10 (mineur) R1 sans la cible | **accepté**, texte repris | Plan 2 |
| CL-11 (mineur) déclencheur 5 et S12 non calculés | **accepté, dans le code v2** : `cos_consecutif_par_tache` et écart « standard seul / renforcé seul » rendus par l'analyse ; la part ≥ S12 est calculée par le lecteur (aucun seuil dans le code) | Métrique ; S12 ; déclencheur 5 |
| CL-12 (mineur) vocabulaire de la borne | **accepté**, texte repris | § n'autorise pas |
| CL-13 (réserve) I3 saturé | **accepté**, texte repris (Table D, mention « indicateur saturé », I3 par tâche) | Métrique ; Table D |
| CL-14 (mineur) départage des références | **accepté** (« puis « dernier », règle du code ») | S6 |
| CL-15 (à compléter) familles de tests | **accepté** : une famille par table (A, B, B′, C, D) ; B8 exacte pour 8 tests ; déclaré | S2 ; Plan 4 |
| CL-16 (conforme) | rien à faire | — |
| § 4 M1–M2 (λ*, trois faits, effet de sélection) | **accepté** : trois faits déclarés dans S6 ; phrase d'effet de sélection ; option (a) recommandée | S6 ; § n'autorise pas |
| § 4 réserve « défense presque figée » et témoin R0 | **accepté** : R0 implanté (code v2, graine 20) ; HR0 neuve ; indice du pilote v1 déclaré sans en tirer la prédiction | gel v2 ; HR0 ; P13, P14 |
| § 4 M3 (S12 posé après le pilote) | **accepté** : déclaré, part par tâche | S12 |
| § 4 M4 (variantes) | **accepté** : grille retirée (CL-07) ; 5 variantes | Plan 5 |
| § 4 M5 (ordre des courses) | **accepté** : précision « ne lit rien de la course du v4 » ; défaut écrit | Plan 5 point 5 |
| § 5 (calcul de puissance) | **accepté**, texte de S3 repris ; complété sur X̄ par l'auteur (même méthode, déclaré) | S3 |

- **Contre-lecture 2** (courte, R2) — sous-agent neuf (modèle Claude Fable 5.1, `claude-fable-5-1`), 1er novembre 2026, 15:42 à ≈ 15:52 UTC ; brouillon relu : `brouillon-prereg-regles-defense-v3.md`, empreinte `7862c944458425f096bfb926ebea3aa2abddee91d03afeb997a5d23b85c946b8` ; rapport : `docs/notes/convergence-defense-v1/regles-defense-v1/contre-lecture-2-prereg-regles-defense-v3.md`, empreinte `c5ba88fc6ec874dce22bcc6fbb1d1ae8544cabd17ce36dfc6a0266722222f227` ; verdict « scellable après corrections mineures » ; traitement : CL2-01 (indications contraires du pilote v2 pour P13 et P14) : accepté, phrase ajoutée au paragraphe « Déclaré (CL-06) » du § Prédiction ; CL2-02 (citation de R-962) et CL2-03 (restes « brouillon 2 », « recommandation S8 ») : forme, acceptés ; CL2-04 (entrée écrite dans une version nouvelle, R12) et CL2-05 (« n = 6 » du pilote v2) : information, rien à changer.
