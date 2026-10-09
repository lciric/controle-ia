# Lecture sur source primaire — 2606.10456 (Distributed Detectability Band), preuves et code — v1

Rapport d'un sous-agent lecteur neuf (il n'a rien écrit de ce qu'il vérifie), rendu le 2026-10-04 (UTC).
PDF lus : 2606.10456v2 (et dépôt Gyyz/distributed_sabotage_frontier, commit b35f23838d14, lu sans copie).
Texte extrait **mot pour mot** du journal du sous-agent par `extraire_rapport.py`, sans aucune modification.
Les chiffres marqués « calcul » ou « mon calcul » sont des reconstructions du lecteur, pas des chiffres des auteurs.

---

# Vérification sur source primaire : arXiv 2606.10456v2

**Ce qui a été fait.**
- PDF lu en entier : 11 pages, pas d'annexe, figures vérifiées sur pages rendues en image. Empreinte SHA-256 conforme.
- Dépôt lu en entier (commit b35f238, un seul commit, signé Yuze GAO, 9 juin 2026).
- Rien n'a été modifié dans `/home/user/controle-ia` ni dans `/home/user/ressources` (vérifié avec `git status`).
- Scripts et sorties : `/tmp/claude-0/-home-user-cplt-run-2026-09-03/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/lecture-2606.10456/`.
- Scikit-learn est absent de l'environnement. J'ai calculé l'AUC par rangs moyens, ce qui est identique à `roc_auc_score`. Le classifieur séquentiel n'a pas été reproduit.

**Reproductions exactes à partir du code copié :**
- `monitor_ab.json` : 9 statistiques hors classifieur, identiques à 6 décimales.
- `realdata_detect.json` : KS 0,009722 et les 5 AUC.
- `adaptive_redteam.json` : « meilleur A » aux trois δφ testés, identique à 4 décimales.

## 1. Identité
- **Titre** : « The Distributed Detectability Band Against Marginal-Preserving Attacks » (p. 1). Le README du dépôt porte un autre titre : « The Distributed Sub-Threshold Sabotage Frontier: A Realizability Gate, a Monitor-A-vs-B Reconciliation, and a Demonstrated Detectability Band… ».
- **Auteurs** : Zhang Qinqin et Yuze Gao. **Aucune affiliation.** Adresses personnelles : qinqinzhang956@gmail.com, yuze.gao@outlook.com.
- **Version** : arXiv:2606.10456v2 [cs.CR], 13 juin 2026.
- **Contenu formel** : 2 propositions et 4 définitions ; les preuves font 2 à 4 lignes. 19 références.
- **Code** : adresse donnée p. 1. **Aucune licence**, ni dans le papier, ni dans le dépôt.

## 2. Table des affirmations

| Affirmation | Verdict | Valeur exacte | Page | Citation |
|---|---|---|---|---|
| Titre | confirmé | voir §1 | 1 | titre |
| Date, version | confirmé | v2, 13 juin 2026 | 1 | "arXiv:2606.10456v2 [cs.CR] 13 Jun 2026" |
| Proposition 1, énoncé | confirmé | — | 3 | "Any monitor whose decision rule depends only on F̂att (i.e., a marginal feature) has detection power equal to its false-positive rate against any zero-stealth-budget attack." |
| Hypothèse : marginale empirique ou de population ? | corrigé | la définition 2 et la proposition 1 portent sur la marginale **empirique**. La construction ne garantit que la marginale **de population par pas**, puis assimile les deux. | 3 | "where F̂att is the empirical marginal CDF of the attack scores." |
| Budget ε défini par Kolmogorov-Smirnov ? | confirmé | D_KS(F̂att, Fben) ≤ ε | 3 | "satisfies a stealth budget ε ≥ 0 if DKS (F̂att , Fben ) ≤ ε" |
| Preuve de la proposition 1 correcte ? | contredit | énoncé vide de contenu et raisonnement qui ne suit pas (§3) | 3 | "At ε = 0, F̂att = Fben by definition." |
| Leur construction préserve-t-elle exactement la marginale empirique ? | contredit | seule la loi de chaque pas est préservée. Distance KS par trajectoire (T = 300) : minimum 0,021, médiane 0,062. Le « rank coupling » n'existe que dans le README : il désigne l'attribution du dommage aux scores les plus hauts. | 3 | "By construction, the marginal of s_t^att equals Fben for all t" |
| La moyenne ou le max sont-ils exactement aveugles dans leurs expériences ? | contredit | moyenne : puissance ≈ 0,020 pour 1 % visé. Max : AUC 0,31 à δφ = 0,40 (leur fichier JSON donne un « meilleur A » de 0,690). | 6–7, 9 | "Monitor A remains at chance throughout (it is marginal-preserving for every δϕ )." |
| Proposition 2(a) | contredit | hérite du défaut de la proposition 1 | 4 | "For any Monitor A (marginal functional), the detection power equals the FPR (by Proposition 1)." |
| Proposition 2(b) | confirmé en substance | vrai pour un test du rapport de vraisemblance à horizon fixe ; imprécis pour le SPRT de Wald | 4 | "For the SPRT with correctly specified AR(1) parameters, the Type-II error vanishes as T → ∞" |
| Proposition 2(c) : puissance → 1 quand T → ∞ | confirmé en substance | asymptotique ponctuelle, sans vitesse | 4 | "the power converges to 1 as T → ∞ for any δϕ > 0." |
| Autre proposition ; « preuve formelle » de la réconciliation A-B avec un score différent | introuvable | il n'y a que les propositions 1 et 2 | 1, 4–5 | "we show formally that the attack, built against Monitor A's score marginal, remains marginal-preserving under a different-score Monitor B" |
| Moniteurs A | confirmé, avec un écart | moyenne, max, moyenne des k plus hauts, compteur de seuil. k = 15 dans le papier, 30 dans le code ; le seuil est la fraction > 0,7. | 3, 5 | "Monitor A: mean score, max score, top-k tail (k = 15), threshold counter." |
| Moniteurs B | corrigé | le code diffère du papier pour 4 statistiques sur 6 (§5) | 3 | "(a) CUSUM-on-products: Ct = max(0, Ct−1 + st st−1 − κ) with threshold hCUS" |
| Calibrage des seuils | introuvable | le papier ne donne que α. Code : quantile 0,99 de 250 trajectoires bénignes de test, puissance mesurée sur 125 attaques. Ni bornes de Wald, ni seuil h_CUS. | 5 | "The operating point for power comparison is α = 1% FPR" |
| AUROC 0,52 (A) | confirmé | moyenne 0,519 ; plage de A : 0,476–0,535 | 6–7 | "Monitor A (mean, max, threshold, top-k tail) achieves AUC ≈ 0.52 (chance)." |
| AUROC 0,79–0,97 (B) | confirmé | 0,788 à 0,973 | 6 | "Monitor B: AUC ranges from 0.788 (runs test) to 0.973 (SPRT)" |
| Puissance 0,688 (SPRT), H = 2,0 | corrigé | H n'est pas indiqué (1,5 dans le code, sans effet sur les scores). Un seul tirage : 86/125. Puissance vraie ≈ 0,53. Le papier donne aussi 0,55 au même point (p. 7). | 7, 9 | "Marginal-preserving attack, T = 300, spread= 150, stealth= 0.2." |
| Puissance de A ≤ 0,048 | confirmé (chiffre) ; interprétation contredite | 0,048 = 6/125, c'est la **moyenne** | 6 | "power at 1% FPR ranges from 0.00 (max) to 0.048 (mean), indistinguishable from the nominal FPR." |
| KS ≈ 0,013 | confirmé (chiffre) ; signification contredite | 0,01333, identique bit à bit pour les 16 niveaux de H. C'est le plancher de bruit de la mesure. L'expérience phare donne 0,0161. | 5 | "The stealthy attack achieves KS = 0.013 uniformly across all harm levels from 0 to 3.0" |
| Traces réelles 120 × 24, agent Qwen2.5-7B-Instruct, moniteur Llama-3.2-3B-Instruct | confirmé, avec réserves | 16 objectifs tirés avec remise (et non 120) ; plans écrits, jamais exécutés ; 7 valeurs de score seulement | 8 | "emits multi-step plans for 120 benign goals" |
| Beta(2,7 ; 4,2) | confirmé (chiffre) ; « bien capturée » contredit | ajustement par les moments. KS contre les données réelles : 0,31. 52,6 % de la masse est sur la seule valeur 0,4. | 8 | "The real benign marginal is well captured by a Beta(2.7, 4.2) fit (mean 0.393)" |
| φ réel = 0,064 | confirmé | moyenne des autocorrélations calculées par trajectoire. Avec un centrage global, on obtient 0,336. | 8 | "its lag-1 autocorrelation is low, ϕreal = 0.064" |
| AUROC 0,68 → 0,98 de T = 24 à 400 | confirmé (chiffre) ; « réel » contredit | 0,679 → 0,982, mais bénin **et** attaque sont générés synthétiquement | 8, 10 | "Monitor B's AUC climbs from 0.68 at T =24 to 0.98 at T =400 (Figure 7c)." |
| AUROC 0,62 → 0,86 de 100 à 1 600 pas | corrigé | c'est le texte. La figure 6b et le JSON donnent 0,635 → 0,847, de façon non monotone (0,599 à T = 200). | 7, 9 | "the autocorrelation detector's AUC rises from 0.62 at T =100 to 0.86 at T =1600" |
| Un seul agent | confirmé | 0 occurrence de « multi-agent » | 1 | "an agent amortizes a fixed harm budget H across T steps" |
| Boîte noire seulement | confirmé | un score scalaire par pas ; 0 occurrence de « activation » | 9 | "our results are an upper bound on Monitor B power under the scalar-score assumption." |
| Processus e, garantie toujours valide | introuvable | 0 occurrence de « e-process », « anytime », « martingale » | — | — |
| Invariance de la puissance au budget total | introuvable | 0 occurrence de « invarian » | — | — |
| Statistique entre agents | introuvable | — | — | — |
| Adresse du code ; licence | confirmé ; licence introuvable | — | 1 | "The released code is available at https://github.com/Gyyz/distributed_sabotage_frontier" |
| Les trois portes | confirmé | (1) réalisabilité ; (2) réconciliation A-B ; (3) bande de détectabilité non vide | 1 | "We sequence the paper around three reviewer-mandated gates." |

**Les trois portes.** Ce sont des critères d'acceptation imposés par des relecteurs que le papier ne nomme pas ; aucun lieu de publication n'est indiqué. La structure du papier suit ces trois critères. En section 5, la porte 2 devient « Monitor-A Blindness » et la porte 3 « Power vs. Harm Spread (The Money Figure) » ; le tableau 4 les résume. Les trois portes figurent dans le titre du README. La v1 n'est pas disponible ici.

## 3. Analyse mathématique

### Proposition 1

**L'énoncé est vide de contenu.** Avec une marginale bénigne Fben continue (N(0,1) dans le papier, Beta dans le code), on a toujours D_KS(F̂, Fben) ≥ 1/(2T) : à chaque point de l'échantillon, F̂ saute de 1/T alors que Fben est continue.
- ε = 0 est donc impossible, et la classe des attaques « à budget nul » est vide.
- C'est vrai aussi pour la marginale réelle discrète : il faudrait que T·p soit entier pour chaque valeur, ce qui échoue déjà avec 24 × 0,526.

**Le raisonnement ne suit pas.** Si F̂att = Fben, la statistique est la constante f(Fben) sous attaque, alors que f(F̂ben) est aléatoire sous l'hypothèse bénigne : les deux lois diffèrent.
- L'hypothèse qui ferait marcher la preuve est l'égalité **en loi** du multi-ensemble des scores sous les deux hypothèses. C'est exactement T1 de notre note, avec le groupe de toutes les permutations du temps.
- L'appel au lemme de Neyman-Pearson est sans objet.

**Leur construction ne préserve que la loi de chaque pas.**
- L'équation (1) ne donne pas de condition initiale ; le code part bien de la loi stationnaire.
- Seule l'espérance des fonctionnelles linéaires est conservée ; leur variance change, et les fonctionnelles non linéaires (max, top-k) changent de loi.
- Mesure : 40 000 + 40 000 trajectoires, T = 300, construction exacte du code, graine `SeedSequence(20261004)` :

| δφ | Moyenne : puissance à 1 % | Écarts-types attaque/bénin | Max : AUC ; puissance | Seuil 0,7 : puissance |
|---|---|---|---|---|
| 0,09 (leur point phare) | 0,019 (0,020 au second tirage) | 1,13 | 0,486 ; 0,009 | 0,021 |
| 0,225 | 0,047 | 1,43 | 0,445 ; 0,009 | 0,040 |
| 0,40 | 0,168 | 2,49 | 0,302 ; 0,005 | 0,107 |

- **Moyenne au-dessus de α, max en dessous** (inégalité de Slepian). C'est exactement la correction de notre contre-vérification ; leurs propres données publiées la montrent déjà.
- Le point de notre note « à vérifier sur le PDF » est levé : **le 0,048 est bien la moyenne**.
- Un tirage de 250 contre 125 trajectoires donne, sous la vraie fuite de 0,020, un intervalle à 95 % de [0 ; 0,064], et P(estimation ≥ 0,048) = 0,14. Le papier ne peut donc ni établir ni exclure la fuite.

### Proposition 2

- **(a)** Hérite du défaut de la proposition 1.
- **(b)** Correct en substance pour le test du rapport de vraisemblance à horizon fixe, qui est ce que le code calcule.
  - Taux de Kullback-Leibler par pas : 0,0101 et 0,0114 nat ; l'AUC théorique est ≈ 0,963.
  - Leur « bande » est donc un calcul de manuel sur un AR(1) gaussien.
  - Pour le SPRT de Wald proprement dit, les erreurs sont fixées par les bornes et ne tendent pas vers 0.
  - Le code n'est pas « correctement spécifié » : l'alternative vaut 0,725 au lieu de 0,59. Le test reste consistant (pente de la dérive 0,86 > 0). Puissance vraie à 1 % : 0,530 avec le code, 0,552 avec l'alternative exacte.
- **(c)** Correct pour une autocorrélation calculée sur les scores ramenés à l'échelle gaussienne.
  - Sur les scores bruts non centrés de la définition 4(e), il faut en plus que la corrélation croisse avec φ. C'est vrai ici, mais l'argument manque.
  - La CUSUM n'est pas un estimateur, et sa consistance n'est pas discutée.
- **Aucune réconciliation formelle A-B avec un score différent** : la section 3.5 se limite à une mise en garde de portée.

### Définitions
- La définition 3 compare un dommage h_t à un seuil d'alarme τ défini sur les scores : ce ne sont pas les mêmes unités.
- Le dommage n'est relié à aucune observable. À graine fixée, les scores sont **identiques bit à bit** pour H ∈ {0 ; 0,2 ; 1,5 ; 3} et K ∈ {1 ; 150 ; 300}. La « porte de réalisabilité » est donc une tautologie.

### Ce que le papier montre, contre ce qu'il affirme
- **Il montre** : deux AR(1) gaussiens (φ = 0,5 contre 0,59) passés par la même marginale connue sont séparés par le rapport de vraisemblance et l'autocorrélation, et non par les statistiques sans ordre en AUC.
- **Il n'établit pas** :
  - l'aveuglement exact de A ;
  - la nécessité d'un moniteur B : le max lu à l'envers détecte à δφ = 0,40 ;
  - l'effondrement de A pour l'attaque qu'il décrit : la figure 4 utilise une autre attaque, non furtive, sans le dire ;
  - un résultat B sur données réelles. Sur le bénin réel, l'autocorrélation donne 0,59 et le SPRT oracle 0,47, sous le hasard, ce que le texte ne mentionne pas.
- **Données réelles** :
  - effet de position (analyse de variance, p = 0,0016) ;
  - marginale discrète, donc copule gaussienne non identifiable ;
  - le quantile interpolé crée des valeurs hors support : 0,21 % des pas et 4,9 % des trajectoires de 24 pas (7 sur 120 dans leur tirage). Un simple test de support, qui est une fonctionnelle de la marginale, en détecte donc 4,9 % sans fausse alarme. Cela contredit « preserved exactly ».
- **Mesure KS** : dans leur mesure (150 000 scores contre 5 000 tirages Beta), le bénin lui-même obtient 0,0117 en médiane. La valeur 0,013 ne mesure donc pas la furtivité.
- **Budget de furtivité** : le « 90e centile bénin contre bénin sur 500 paires » vaut en réalité 0,134 pour T = 300, pas 0,013.

## 4. Chiffres utilisables

| Chiffre | Signification | Page |
|---|---|---|
| SPRT : AUC 0,973, puissance 0,688 à 1 % | un tirage (250 bénignes / 125 attaques), δφ = 0,09, T = 300, alternative 0,725. Valeurs vraies ≈ 0,96 et ≈ 0,53. Intervalle à 95 % d'un tirage : [0,38 ; 0,74]. | 7 |
| A : AUC 0,476–0,535, puissances 0–0,048 | même tirage ; compatible avec une fuite vraie de la moyenne ≈ 2α | 7 |
| KS 0,013 | plancher de bruit de la mesure. La distance KS par trajectoire est ≈ 0,06. | 5–6 |
| Max : AUC 1,000 (K = 1) → 0,504 (K = 300) ; moyenne entre 0,48 et 0,58 | attaque semi-furtive à décalage total fixe de 0,6 (K ≥ 2). Mon Monte-Carlo : moyenne plate à 0,529 pour K ≥ 10. C'est une illustration involontaire de nos résultats L1/L2. | 8 |
| Frontière adaptative : δφ⋆ = 0,05 (autocorrélation 0,70 à 0,05 ; 0,54 à 0,02) | un tirage, 250 contre 250 | 7, 9 |
| Évidence : autocorrélation 0,635 → 0,847, SPRT 0,726 → 0,989 (T de 100 à 1 600) | prendre la figure et le JSON, pas le texte | 9 |
| Données réelles : 120 × 24, 7 valeurs, moyenne 0,393, φ = 0,064 | bénin seulement ; aucune attaque réelle | 8 |
| Réel : A 0,46 / 0,54 / 0,56 ; autocorrélation 0,59 ; SPRT 0,47 | 120 contre 120 ; écart-type de l'AUC ≈ 0,04 | 8, 10 |
| 0,68 → 0,98 (T de 24 à 400) | synthétique, calibré sur le réel | 8, 10 |

## 5. Écarts entre papier et dépôt

| Point | Papier | Dépôt |
|---|---|---|
| Marginale bénigne | N(0,1) (p. 3, 5) | Beta(2,05 ; 5,12) |
| φ bénin | « estimated from benign SHADE-Arena-like traces » (p. 5) | 0,5 codé en dur. `fit_benign` n'est appelé par aucune expérience. L'ingestion SHADE-Arena est un bouchon vide. |
| Placement du dommage | pas « contiguous » ou « uniformly spaced » (p. 3–4) | étiquettes posées sur les K scores les plus hauts, poids proportionnels au rang. Les scores ne sont pas modifiés. |
| Figure 4 et tableau 3 | présentés comme l'attaque à marginale préservée | `semi_stealthy_attack` : on ajoute min(0,30 ; 0,3·H/K) aux K scores les plus hauts. La marginale n'est pas préservée. |
| CUSUM | Page sur les produits s_t s_{t−1} | Σ max(0, 1 − w_t²) ; la récursion de Page est calculée puis ignorée |
| SPRT | alternative φ_att ; légende « oracle ϕ » (p. 9) | alternative fixée à 0,725 ; aucune règle d'arrêt |
| HMM | 2 états, ajusté sur des traces bénignes | chaîne de Markov à 4 classes, ajustée sur la trajectoire testée elle-même |
| Autocorrélation | pas 1, scores bruts | somme des pas 1 à 5, sur l'échelle gaussienne |
| Classifieur | 3 caractéristiques | 14 caractéristiques, entraîné sur des attaques de même φ |
| top-k | k = 15 | k = 30 (k = 4 sur données réelles) |
| Effectifs | 500 bénignes / 250 attaques | évaluation sur 250 / 125 |
| Bootstrap | « averaged over 500 bootstrap replications » (p. 5) | aucun bootstrap ; un seul tirage |
| §5.5 (p. 7) | 0,56 ; 0,62→0,86 ; 0,46/0,21 ; 0,55/0,60 ; 0,003 ; 0,07 | 0,545 ; 0,635→0,847 ; 0,468/0,124 ; 0,524/0,472 ; 0,004 ; 0,036 |
| Légende de la figure 2 | KS 0,57 à H = 1,2 | 0,384 (cohérent avec le tableau 1) |
| Tableau 4 | « 34× improvement over A » | 0,688 / 0,048 = 14,3 |
| Données réelles | « 120 goals », « episodes concatenated » | 16 objectifs ; la figure 7c ne concatène pas d'épisodes réels, elle est synthétique |
| p. 10 | « the feedback oracle described in Section 6. » | ce renvoi ne mène à rien |

## 6. Collision avec le programme

| Revendication | Niveau | Justification | Pages |
|---|---|---|---|
| T, première partie : toute statistique de marginales a une puissance égale au taux de faux positifs | **partiel** | L'énoncé est revendiqué dans le temps, pour un seul agent, en boîte noire, avec une revendication d'antériorité. Mais il est vide et faux pour leur propre construction. La version correcte (loi du multi-ensemble préservée) n'y est pas. Le programme a le même défaut tant qu'il n'est pas reformulé. | 1, 3–4, 9 |
| T, deuxième partie : il faut un agrégateur d'autocorrélation dans le temps | partiel | Le moniteur B et la proposition 2(b)(c) sont là. La nécessité est affirmée sans preuve, et elle est fausse hors du cas « multi-ensemble préservé ». | 3–4, 9–10 |
| T, troisième partie : co-élévation entre agents ; même objet dans le temps et entre agents | **libre** | aucun agent multiple | — |
| L : lemme d'additivité | **libre** (adjacent) | Ni processus e, ni énoncé d'invariance. Le tableau 3 illustre L1 et L2 sans le dire. | 8 |
| Vraies activations | **libre** | un score scalaire ; le moniteur multidimensionnel est renvoyé à plus tard | 8–9 |
| Invariance au budget total | **libre** (adjacent : tableau 3) | — | 8 |
| Indexation unifiée temps × agents | **libre** | — | — |
| Énoncé par invariance aux permutations (classe « multi-ensemble préservé ») | **adjacent** | Seule la remarque informelle « function of the multiset … ignores their order » existe. Ni classe d'attaque, ni sous-groupes, ni équivalent de T2. | 1 |
| Garantie toujours valide | **libre** | — | — |

## 7. Références qui menacent une revendication (bibliographie, p. 11)
- **Détection séquentielle classique** : [4] Basseville et Nikiforov, [15] Page, [18] Wald. Le séquentiel en boîte noire est classique.
- **Copules** : [13] Nelsen, [17] Sklar. La dichotomie marginale/copule est classique ; le théorème T ne peut pas reposer sur elle seule.
- **Précédent de sabotage étalé dans le temps** : [5] Benton et al. (bogue inséré sur de nombreux commits).
- **Utiles surtout pour le papier C** : [1], [3], [11].
- **Aucune référence** sur les processus e, les sondes d'activations ou la détection entre agents. Rien dans la bibliographie ne menace donc L ni la différenciation boîte blanche / essaim.

## 8. Alertes
1. **Ne pas citer la proposition 1, ni « provably blind », comme un théorème.** L'énoncé est vide, faux pour leur construction, et contredit par leur propre figure 6a. Notre T doit être énoncé dans la classe « multi-ensemble préservé ». L'énoncé du programme (section 3) doit être corrigé de la même manière.
2. **Les chiffres viennent d'un seul tirage**, et plusieurs procédures annoncées sont absentes du code (bootstrap, SPRT oracle). Les chiffres de §5.5 ne correspondent pas au JSON, et la remontée « réelle » 0,68 → 0,98 est synthétique. Deux mentions du programme sont à corriger :
   - « 0,688 avec H = 2,0 » : H n'est pas indiqué dans le papier ; il vaut 1,5 dans le code et n'a aucun effet sur les scores ;
   - « 0,62 → 0,86 » : la figure et le JSON donnent 0,635 → 0,847.
3. **Provenance et licence.**
   - Aucune affiliation et des adresses personnelles.
   - Des relecteurs non identifiés.
   - Le titre du README diffère de celui du papier.
   - Il n'y a aucune licence, donc tous droits réservés par défaut.
   - On peut citer le papier avec prudence, mais il faut ré-implémenter plutôt que reprendre le code.
