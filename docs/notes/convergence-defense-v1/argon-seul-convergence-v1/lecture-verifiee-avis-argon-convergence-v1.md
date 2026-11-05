# Lecture vérifiée de l'avis d'Argon seul — question de convergence v2 — v1

## En-tête

- Lecteur : sous-agent neuf, modèle Claude Fable 5.1 (`claude-fable-5-1`), lignée distincte d'Argon (`gemini-4-argon`) et des rédacteurs du brouillon 4 (Opus) et de sa vérification (Sonnet 5.5). Je n'ai écrit ni la question, ni les pièces, ni l'avis.
- Date (UTC) relevée par `date -u` après lecture de tous les fichiers : **2026-11-01, 09:54:26**.
- Cadre tenu : aucun fichier existant modifié, rien scellé, rien commité, aucun appel de modèle, aucun réseau. Lu sous `donnees/` : le seul dossier `donnees/argon-seul-convergence-v1/` (fichier des faits et code de l'arène ; le JSON du pilote n'a pas été ouvert, il n'a pas été servi à Argon non plus). Aucune recommandation dans ce document.
- Empreintes SHA-256 recalculées par `sha256sum` (jamais retapées à la main) :

| Fichier | Empreinte |
|---|---|
| `docs/notes/convergence-defense-v1/argon-seul-convergence-v1/reponse-argon-convergence-v2-v1.md` (l'avis, 8 626 mots, 258 lignes) | `fa49440fb82f4eec528a712ee619fe5359cb94b47bbdd91b8e2ab262004ace49` |
| `…/manifeste-argon-convergence-v2-v1.json` | `75cb2d7e2a559f978883a7b27486cd4b5faa6b4af7400ce6618cfbd933269fef` |
| `…/question-convergence-defense-unique-v2.md` (787 mots) | `08f2b01724ea08005f647e5a6b666aa064b8ba539829f3464f9999113a3feda0` |
| `donnees/argon-seul-convergence-v1/faits-convergence-v2-argon-v1.md` (31 750 mots, 2 942 lignes) | `15d19443e94832f2e94787251574d50be2b8adabcedffb3622380f0fbce21953` |
| `donnees/argon-seul-convergence-v1/arene_melange_v4.py` (2 241 lignes) | `70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61` |

Le manifeste confirme que la question servie et les faits servis sont ceux de ces empreintes (`question_sha256`, `faits_sha256`), que la réponse est celle de l'empreinte ci-dessus (`reponse_sha256`), modèle servi `gemini-4-argon`, fin de réponse `STOP`, 86 420 jetons d'entrée et 19 039 de sortie, coût 1,8161 dollar sous un plafond de 3 dollars. Le code `arene_melange_v4.py` est recopié entier dans les faits à partir de la ligne 700 (décalage de 699 lignes entre le fichier `.py` et les faits) ; son empreinte est celle du bloc d'identité du brouillon 4.

Dans la suite, « Pièce 1 » = brouillon 4, « Pièce 2 » = vérification du brouillon 4, « Pièce 3 » = code, comme dans l'avis. « l. » renvoie aux lignes du fichier des faits sauf mention « py l. » (fichier `.py`).

## 1. Chiffres et affirmations qu'Argon attribue aux pièces

Méthode : chaque chiffre ou énoncé que l'avis rattache à une pièce est recherché dans les faits (texte du brouillon 4, vérification, code). « Juste » = présent et identique ; « inexact » = présent mais différent ; « absent » = introuvable dans les pièces servies.

### 1.1 Chiffres du monde et de la configuration (bloc d'identité, l. 44–121 ; code)

| Affirmation d'Argon | Pièce (ligne) | Verdict |
|---|---|---|
| T = 8 tours, K = 3 composantes, d = 6 | `"T": 8`, `"K": 3`, `"d": 6` (l. 47, 46, 59) | juste |
| 36 paramètres d'attaque θ = (μ, σ) ∈ ℝ^{2Kd} | `deplier` (py l. 413–415) : K·d moyennes puis K·d écarts-types | juste |
| ‖μ_k‖₂ = 4, σ_{k,j} = 1 pour la cible | `r_cible: 4.0`, `sigma_cible: 1.0` ; `loi_cible` (py l. 461–465) | juste |
| boîte μ ∈ [−5 ; 5], σ ∈ [0,5 ; 1,5] | `boite_mu 5.0`, `sigma_min 0.5`, `sigma_max 1.5` ; `bornes` (py l. 418–420) | juste |
| distance W₂ = √(1/K · ‖θ − θ_cible‖²) ≤ δ | `distance` (py l. 423–425) ; contrainte dans `meilleure_reponse` (py l. 826–828) | juste |
| δ ∈ {1,4 ; 1,6} (`DELTAS_V4`) | py l. 137 ; l. 139 | juste |
| moniteur : score logsumexp(Wx + b), m = 1 linéaire 7 paramètres, m = 9 maxout 63 paramètres | `Moniteur.score` (py l. 498–500) ; § Métrique l. 259 | juste |
| seuil au quantile 1 − α, α = 0,01, sur n_cal = 20 000 échantillons propres N(0, I₆) | `Moniteur.calibrer` (py l. 514–522), `Xcal` tiré en `standard_normal((n_cal, d))` (py l. 889) ; `"n_cal": 20000`, `"alpha": 0.01` | juste |
| n_eval = 19 998 | `"n_eval": 19998` (l. 86) | juste |
| attaquant : sigmoïde centrée sur t_i, échelle τ·e_i, τ = 0,25, n_mc = 256 par composante, SLSQP, choix du départ sur `taux_dur` | `objectif_lisse` (py l. 790–806), `meilleure_reponse` (py l. 842), `"tau": 0.25`, `"n_mc": 256` | juste |
| défenseur : L-BFGS-B, seuil approché μ_propre + z_{1−α}·σ_propre, départ logistique pénalisé ℓ₂ = 10⁻³ ; « exact en population pour m = 1, approché pour m > 1 » | `objectif_detection` (py l. 655–672, docstring), `_logistique` (py l. 639–652), `"l2": 0.001` | juste |
| 12 départs (standard) et 48 (renforcé) en phase finale ; 4 à 48 départs dans `meilleure_reponse` | `departs_final 12`, `departs_renforce 48`, `departs 4` ; `phase_finale` (py l. 1152–1158) | juste |
| l'attaquant réinjecte `attaques[-1]` comme départ supplémentaire | `trajectoire` py l. 1084 (`departs_suppl=[attaques[-1]]`) | juste |
| λ = 8 pour C3 et C3′ (`ou_deterministe`, `MoniteurOu`) | `lambda_ou: 8.0` ; py l. 536, 553 | juste |
| support d'un mélange : poids > 10⁻⁶ ; pur : poids ≥ 1 − 10⁻⁹ ; pureté forcée : ≥ 1 − 10⁻⁶ | py l. 1344, 760–761 | juste |
| garde `np.any(G < 0) or np.any(G > 1)` de `resoudre_jeu`, solveur HiGHS | py l. 739, 746 | juste |
| `poids_max_min_equilibres(G, valeur)` : programme linéaire du plus petit poids maximal | py l. 768–788 | juste |
| A : poids d'entraînement `np.full(len(attaques), 1.0 / len(attaques))` | py l. 1107 | juste |
| réinitialisation `x0 = np.zeros(d + 1)` à chaque tour (m = 1) ; maxout initialisé par permutation aléatoire | `entrainer` py l. 686–694 | juste |
| D : m = t + 1 unités au tour t | py l. 1106 | juste |
| B′ entraîne contre la stratégie d'équilibre q de l'attaquant ; D sur le mélange uniforme | py l. 1102–1107 | juste |
| `indicateurs_cycle(H, iii, deplacements)`, clés `I1_progres`, `I3_retours`, `I3_moins_nul` ; `ligne_table5` ; `est_pur(p)` | py l. 1034–1053, 1482, 764 | juste |
| I3 : cosinus du déplacement θ_t − θ_cible avec une attaque s ≤ t − 2 contre celle du tour t − 1 | `taux_retours` py l. 1021–1031 ; `v = a - ctx.cible` py l. 1093 | juste |
| valeur nulle (1/(T−2)) Σ_{t=3}^{T} (t−2)/(t−1) = 0,7345 à T = 8 | `valeur_nulle_I3` py l. 1014–1018 ; vérifié à la main : (0,5 + 0,6667 + 0,75 + 0,8 + 0,8333 + 0,8571)/6 = 0,7345 | juste |
| C3′ « empile 81 unités soit 511 paramètres » | B′ garde M₀ linéaire (1 unité, 7 paramètres) plus 8 maxouts à 9 unités (py l. 1061–1062, 1102) : **73 unités**, 7 + 8 × 63 = 511 paramètres. Le brouillon lui-même parle du « maxout unique de 73 unités (même total que B′) » (l. 155, 180, 336) | **inexact** (81 unités ; 511 paramètres juste) |
| « deux programmes linéaires par tour » pour B/B′ | `trajectoire` appelle `resoudre_jeu` deux fois par tour (p avant l'attaque, q après la colonne nouvelle), chaque appel résolvant un primal et un dual (py l. 1079, 1101, 744–751) | approximatif (quatre résolutions par tour, de deux jeux) ; sans effet sur son argument de coût |
| **numéros de lignes de la Pièce 3** (l. 534, 549, 594, 617, 619, 635, 639, 660, 676, 694, 719–745, 743, 752, 765) | aucun ne tombe sur l'objet désigné, ni dans le `.py` ni dans les faits ; le décalage croît de 2 (`ou_deterministe` : 536 contre 534) à 364 (`np.full` : 1107 contre 743 ; `defense_temoin` : 1129 contre 765) | **tous inexacts** ; les identifiants cités existent tous et leur contenu est rapporté exactement |

### 1.2 Chiffres du pilote v4 (Pièce 1 § Prédiction A et B, § Résumé, § N'autorise pas ; Pièce 2 § 4)

| Affirmation d'Argon | Pièce (ligne) | Verdict |
|---|---|---|
| V(A) = 0,0816 / 0,0359 ; V(B) = 0,2099 / 0,1746 ; V(D) = 0,4440 / 0,3541 | Pièce 2 § 4 l. 659 ; Pièce 1 l. 210 (V(A)) | juste |
| valeur du jeu restreint − V : B +0,019 / +0,024 ; B′ +0,004 / +0,004 | l. 162 | juste |
| I1 de A : +0,0020 [−0,0029 ; +0,0069] ; −0,0005 [−0,0046 ; +0,0034] | l. 219 | juste |
| I3 de A : 0,9028 / 0,9444 ; écart +0,1683 [+0,0988 ; +0,2308] / +0,2099 [+0,1613 ; +0,2516] | l. 220 ; Pièce 2 l. 659 | juste |
| D : I3 − 0,7345 = −0,2831 / −0,3804 | l. 221 | juste |
| nouveauté résiduelle de D au tour 8 : 0,199 | l. 251 (« 0,151 (B′) à 0,199 (D) ») | juste |
| rétention de A : 0,37 au décalage 0, 0,24 et 0,23 au décalage 1 | l. 251 | juste |
| D et B′ plafonnent ≈ 0,40 dès le tour 4 ; A autour de 0,07 | l. 251 (« ≈ 0,40 dès le tour 4 » ; A « 0,072 → 0,066 ») | juste |
| C1 − A ≈ +0,108 / +0,118 (dérivé) | l. 251 | juste |
| B − C1 = +0,0202 / +0,0205 | l. 213, 240 | juste |
| B − A (iii) = +0,1283 / +0,1387 | l. 211, 239 | juste |
| B − C3 = −0,1935 / −0,1443 ; B − D = −0,2341 / −0,1795 | l. 214, 242–243 | juste |
| B − A (ii) = −0,0538 [−0,0784 ; −0,0274] / −0,0580 [−0,0893 ; −0,0233] | l. 215 | juste |
| B′ − D = +0,0024 / +0,0042 ; sur tâches pures +0,0021 / +0,0038 ; tâches à mélange réel n = 7 et n = 10 | l. 216, 251 | juste |
| B′ − C3′ = +0,0072 [+0,0015 ; +0,0127] / +0,0114 [+0,0072 ; +0,0160] | l. 217 | juste |
| part pure de B′ : 70,8 % (17/24) et 58,3 % (14/24) ; pureté forcée 100 % (17/17, 14/14) | l. 218–219 ; Pièce 2 l. 659 | juste |
| moniteur de poids pur aux tours 2 à 4 dans 14/17 et 12/14 tâches pures | l. 133 ; Pièce 2 l. 660 | juste |
| support moyen de B : 3,7 et 3,8 moniteurs ; facteur ≈ 2,4 | l. 251 ; 9/3,75 = 2,4 | juste |
| seuil de 50 % de tâches pures (Table 7) ; m = S6 = 0,02 ; 24 instances ; Tables 2 et 3 pour les tests déjà faits | l. 467, 301–303, 128, 415, 427 | juste |
| paramètres stockés / déployés : B 63 et 7 ; C3, D 63 et 63 ; B′ 511 et ≤ 63 ; C3′ 511 et 511 | l. 259 | juste |
| I2 renommé (CM3-03) ; options CM3-02, CM3-07, S16 (témoin mode, « ou » restreint) ; S9 = α ; S17 | l. 146, 155, 336, 541, 311, 339 | juste |

**Décompte.** Chiffres et affirmations rattachés aux pièces : 60 recoupés ; **58 justes, 1 inexact** (81 unités pour C3′ ; les 511 paramètres sont justes), **1 approximatif** (« deux programmes linéaires par tour »), **0 absent**. Les **quinze numéros de lignes** cités sont **tous inexacts** mais ne désignent jamais un objet absent. Aucun chiffre du pilote n'est déformé.

## 2. A-t-il vu que A s'entraîne sur tout l'historique ?

**Oui, explicitement.** Fait établi par session-depot, vérifié : la question (l. 7 et point 1) écrit « ré-entraînée à chaque tour contre la dernière attaque » ; le brouillon 4 dit « entraîné contre le mélange uniforme de toutes les attaques passées » (faits l. 354, soit l. 348 du brouillon seul), la docstring du code dit « réentraîné à chaque tour sur toutes les attaques passées (mélange uniforme) » (faits l. 739–740 ; py l. 40–41), et le code le fait (py l. 1107).

Section 1.B de l'avis, citée : « Bien que la question décrive le bras A comme ré-entraîné « contre la dernière attaque », le code et le Plan d'analyse montrent que dans l'implémentation actuelle, le bras A déploie le seul dernier moniteur linéaire M_t, mais l'entraîne contre le **mélange uniforme de toutes les attaques passées** […] tandis que l'attaquant joue une meilleure réponse locale contre le seul dernier moniteur M_t ». Il en tire : « Ce n'est donc ni une dynamique de meilleure réponse pure […] ni un jeu fictif bilatéral […]. C'est une dynamique hybride asymétrique : le défenseur joue une meilleure réponse approchée dans une classe paramétrique restreinte à la distribution empirique historique de l'attaquant, mais sans mémoire d'affichage (il jette M₀, …, M_{t−1}), et l'attaquant joue une meilleure réponse pure à l'unique moniteur affiché M_t. » Cette description est conforme au code (`defense_courante` rend `[(moniteurs[-1], 1.0)]` pour A ; `historique` garde les anciens pour la matrice H seulement).

Il reprend cette lecture correcte en 2.1 (« Même si A est entraîné sur le mélange uniforme de toutes les attaques passées »), en 2.4 (« l'entraîne sur l'union de toutes les attaques passées »), en 3(a) (« A entraîne sur q̄_t mais ne déploie pas M̄_t »), en 3(f) (« le mélange uniforme des attaques passées, Pièce 3 ») et en 6.1.

**Où la lecture fautive « dernière attaque » subsiste malgré tout :**
- Section 3(c), test de réfutation : « Sur le bras A (m = 1, entraîné uniquement sur la dernière attaque), ajouter une pénalité … » : contradictoire avec sa section 1.B ; tel quel, ce test porte sur une variante de A qui n'existe pas dans le code.
- Section 2.2 (cycles de Shapley, meilleure réponse itérée) : écrite au conditionnel (« Si la défense était ré-entraînée uniquement contre la dernière attaque »), elle n'explique pas A tel qu'il est ; Argon le sait et propose une seconde voie pour A réel, la condition (ii) « mémoire complète mais asymétrie des objectifs » (somme non nulle induite par les deux lissages différents). Son test de réfutation 2.2 exige de réécrire A (« entraînement sur la seule dernière attaque ») : c'est un test d'une autre dynamique, pas de celle des pièces.
- Section 4, protocole, étape 2 : la dynamique « meilleure réponse » du jeu jouet répond à « la seule dernière action adverse » ; ce jouet n'est donc pas l'analogue de A réel (qui est un jeu fictif unilatéral côté défenseur), mais Argon ne le présente pas comme tel : il vérifie la mesure, pas la dynamique de A.

**Ce qui tient quand même, indépendamment de « dernière attaque »** : le diagnostic principal 2.1 (sous-capacité d'un moniteur linéaire unique face à une enveloppe multimodale : pas d'équilibre pur, l'hyperplan sur la moyenne des attaques bascule) ; 2.3 (dernier itéré contre moyenne des itérés) ; 2.4 (saturation, pas oubli catastrophique, puisque A réapprend sur l'union) ; les métriques de 1.C ; les mécanismes (a), (b), (e), (f), (g) ; la section 5 ; la section 6. Le cœur de l'avis ne dépend pas de l'erreur de la question.

Réserve de ma part sur 2.3 : Argon cite « C1 bat le dernier itéré de A de +0,108 / +0,118 » comme preuve de l'écart dernier itéré / moyenne des itérés. Mais C1 est construit sur les moniteurs de **B** (entraînés contre q*, trajectoire de B), pas sur ceux de A : C1 − A mêle « moyenne contre dernier » et « trajectoire de B contre trajectoire de A ». Son propre test de réfutation (« le dernier moniteur de B déployé seul fait-il aussi bien que C1 ou B ? ») est le bon découplage ; il n'est pas calculable depuis les JSON sans les objets moniteurs (non sérialisés), mais il est bon marché sur processeur.

## 3. Mécanismes (a) à (g) de la section 3, en une ligne chacun, et cohérence avec le code

| Mécanisme | Condition de convergence (selon Argon) | Coût | Ce que ça casse | Test de réfutation le moins cher | Cohérence avec le code de l'arène |
|---|---|---|---|---|---|
| (a) jeu fictif (Brown, Robinson) | somme nulle, deux joueurs, espaces finis ou compacts, oracles exacts ; convergence lente (exposant d'après Daskalakis et Pan 2014, à vérifier) | stocker T + 1 moniteurs (63), déployer 1 par requête (7) | dilution par les premiers moniteurs faibles (B − C1 = +0,020) ; échec si M₁ ne contient pas la meilleure réponse au mélange | trajectoire où le défenseur déploie le mélange uniforme des moniteurs passés et entraîne sur celui des attaques ; réfuté si V reste sous B de 0,02 ou sous C3/D | **A fait déjà** la moitié défenseur du jeu fictif (entraînement sur l'historique) ; manque le déploiement du mélange uniforme pendant la trajectoire (C1 n'existe qu'en finale, sur les moniteurs de B) : variante non codée, petite (`defense_courante`) |
| (b) oracle double / PSRO | somme nulle sur la méta-matrice, compacité, oracles exacts contre p* et q* | deux appels de programme linéaire par tour, évaluation croisée O(T²), stockage 63 (B) ou 511 (B′) | plafond de l'espérance linéaire face au « ou » et au maxout (Q1 réfutée : B − C3, B − D) ; régression sur (ii) ; effondrement pur à classe riche (Q2 non exercée) | déjà exécuté au pilote v4 (Tables 2 et 3) | **existe déjà : bras B et B′**, exactement comme décrit (`resoudre_jeu`, `linprog` HiGHS) |
| (c) régularisation vers les moniteurs passés (pénalité ℓ₂, moyenne mobile, distillation, entropie côté méta-jeu) | paysage localement convexe ou même bassin de permutation (faux pour un maxout réinitialisé) ; capacité suffisante pour la distillation | zéro à l'inférence, modéré à l'entraînement | à m = 1, moyenner des vecteurs d'attaques opposées annule le vecteur | sur A, pénalité λ/2 ‖W_t − W_{t−1}‖² ou moniteur de poids moyen W̄ recalibré ; réfuté si V(W̄) < V(C1) et I1 < 0,02 | **n'existe pas** dans le code (`objectif_detection` n'a aucun terme de distance aux moniteurs passés ; `entrainer` repart de zéro) ; le test « poids moyen » est calculable à partir des moniteurs de A (objets non sérialisés : rejeu nécessaire) ; le test est formulé sur un A « entraîné uniquement sur la dernière attaque », qui n'est pas celui du code (voir § 2) |
| (d) gradients optimistes / extragradient | jeu convexe-concave (ou condition de Minty), équilibre pur intérieur, petits pas couplés | deux gradients par pas, pas couplés | gain ni concave en W ni convexe en θ (quantile, logsumexp, mélange gaussien) ; irréaliste face à un attaquant global | extragradient sur une instance à m = 1, puis V(W_T) contre `meilleure_reponse` à 12 départs ; réfuté si V ≈ 0,08 | **n'existe pas** ; incompatible avec la réinitialisation complète à chaque tour et l'attaquant global SLSQP ; Argon le dit |
| (e) élargir la classe du défenseur (« ou » C3/C3′, maxout D) | queues légères de la loi propre, m modéré (seuil du maximum de m variables ≈ α/m) | ×m paramètres par requête (63 contre 7 ; 511 pour C3′) | dilution du seuil par les moniteurs faibles (B′ − C3′ > 0) ; queues lourdes sur de vraies activations | déjà visible (B′ − C3′) ; pour la limite : T = 32 ou loi propre de Student ν = 3 | **existe déjà : C3, C3′, D** ; le test « Student » demande de changer la loi propre, codée en dur `standard_normal` (py l. 889–890, `propre_entr`) |
| (f) changer l'objectif (pire cas sur l'historique, robustesse distributionnelle de Wasserstein) | capacité suffisante pour relever l'attaque la moins détectée sans perdre ailleurs ; à m = 1, maximin sur attaques opposées ramène à un score constant | quasi identique à A/D (repondération) ; boucle interne pour la version Wasserstein | B′ (entraîné contre q*, déjà un pire cas pondéré) ne bat D (uniforme) que de 0,002–0,004 à m = 9 | remplacer les poids uniformes de D (ou A) par q_s ∝ exp(−η H[t−1, s]) ; réfuté si V ne monte pas de 0,02 | **partiellement présent** : B′ entraîne contre q* (py l. 1102) ; la repondération exponentielle de D/A n'existe pas (une ligne, py l. 1107) ; la version Wasserstein n'existe pas |
| (g) sélection du mode (g1) ; « ou » restreint au support de p* (g2) | g1 : un bon moniteur pur existe dans l'historique (vrai à m = 9) ; g2 : 1 < support < T + 1 | g1 : coût d'une défense unique ; g2 : coût de C3 divisé par ≈ 2,4 | g1 échoue si tout moniteur pur est exploitable (m = 1) ; g2 viole « classe égale » si support > 1 | deux témoins ajoutés à `defense_temoin` : le moniteur arg max p* de B′ seul ; le « ou » sur le support de B ; g1 réfuté si V(B′) − V(mode) > 0,02 sur les tâches à mélange réel | **pas un bras, mais des options déclarées** du brouillon 4 (l. 155, 336, 541) ; `indice_poids_max` déjà consigné (py l. 1118) ; V du mode seul exige un rejeu (moniteurs non sérialisés) |

Note sur la section 2 (pourquoi ça cycle), même grille : 2.1 (sous-capacité) est cohérent avec le code et avec D ; 2.2 (Shapley) ne décrit pas A réel sauf par l'asymétrie des lissages, qui est bien dans le code (`objectif_detection` seuil gaussien contre `objectif_lisse` seuil empirique) ; 2.3 (dernier itéré) cohérent, avec la réserve C1/B du § 2 ; 2.4 (saturation) cohérent avec la réinitialisation `x0 = zeros` et l'union des attaques.

## 4. Sources citées — toutes RAPPORTÉ (aucun PDF servi ; R7)

Aucune source n'a été vérifiée sur PDF ; aucun chiffre ni énoncé ci-dessous n'est opposable. « Classique » = résultat bien connu dont l'attribution est très vraisemblable, sans garantie ; « à vérifier en priorité » = attribution, identifiant ou détail qui me paraît douteux.

| # | Référence (telle qu'Argon l'écrit) | Énoncé attribué | Statut |
|---|---|---|---|
| 1 | Johanson, Zinkevich, Bowling 2011, IJCAI, « Accelerating Best Response Calculation in Large Extensive Games », pp. 258–265 | définition de l'exploitabilité et du NashConv | RAPPORTÉ ; papier réel (calcul de meilleure réponse au poker) ; **à vérifier** : le terme « NashConv » me semble plutôt introduit par Lanctot et collègues 2017 ; pages non vérifiées |
| 2 | Lanctot et collègues 2017, NeurIPS 30, arXiv 1711.00832 | PSRO, réponse à une population ; NashConv | classique ; cité aussi par le brouillon (SUPPOSÉ) |
| 3 | von Neumann 1928, Math. Annalen 100, 295–320 | écart maximin / minimax pur | classique |
| 4 | Pinot, Meunier, Yger, Gouy-Pailler, Chevaleyre, Atif 2020, Machine Learning 109(8), arXiv 1902.08748, « On the robustness of randomized classifiers to adversarial examples » | classificateurs randomisés sous attaquant qui observe la distribution | **à vérifier en priorité : amalgame probable**. De mémoire, arXiv 1902.08748 est un papier NeurIPS 2019 au titre différent ; le titre cité serait un article de revue postérieur (vers 2022) ; et le « Pinot et collègues 2020 » du brouillon (SUPPOSÉ) est sans doute l'article ICML 2020 sur les stratégies mixtes. Trois papiers fusionnés en une référence |
| 5 | Shapley 1964, Annals of Math. Studies 52, « Some topics in two-person games » | cycle du jeu fictif en somme non nulle | classique |
| 6 | Mertikopoulos, Papadimitriou, Piliouras 2018, SODA, arXiv 1709.02738 | cycles de l'apprentissage régularisé en somme nulle, moyenne converge, dernier itéré non | classique (bien connu) ; pages non vérifiées |
| 7 | Bailey, J., Piliouras 2018, EC '18, arXiv 1801.08652 | poids multiplicatifs en somme nulle divergent au dernier itéré | classique ; **homonymie** avec Bailey L. (arXiv 2412.09565) correctement distinguée par Argon ; identifiant arXiv à vérifier |
| 8 | French 1999, Trends in Cognitive Sciences 3(4), 128–135 | oubli catastrophique | classique |
| 9 | Brown 1951, Cowles Commission Monograph 13, 374–376 | jeu fictif | classique |
| 10 | Robinson 1951, Annals of Mathematics 54(2), 296–301, JSTOR 1969530 | convergence du jeu fictif en somme nulle | classique ; identifiant JSTOR non vérifié |
| 11 | Daskalakis, Pan 2014, FOCS, arXiv 1405.5949 | taux de convergence en pire cas « O(t^{−1/(|S|−2)}) » | papier réel (contre-exemple à la conjecture de Karlin) ; **l'exposant exact cité est à vérifier** (je ne le garantis pas) |
| 12 | McMahan, Gordon, Blum 2003, ICML, 536–543 | oracle double | classique ; cité par le brouillon (SUPPOSÉ) |
| 13 | Kirkpatrick et collègues 2017, PNAS 114(13), arXiv 1612.00796 | consolidation élastique des poids | classique ; **liste d'auteurs altérée** (« Tiago, R. » n'est pas un nom d'auteur : garble probable de Ramalho, T.) |
| 14 | Izmailov et collègues 2018, UAI, arXiv 1803.05407 | moyenne de poids | classique |
| 15 | Korpelevich 1976, Matekon 12, 747–756 | extragradient | classique ; détails de revue/volume à vérifier (l'original est en russe, traduction postérieure) |
| 16 | Daskalakis, Ilyas, Syrgkanis, Zeng 2018, ICLR, arXiv 1711.00141 | gradients optimistes, convergence du dernier itéré | classique |
| 17 | Mertikopoulos et collègues 2019, ICLR, arXiv 1807.02629 | descente miroir optimiste, extragradient | classique |
| 18 | Goodfellow et collègues 2013, ICML, PMLR 28(3), arXiv 1302.4389 | réseaux maxout | classique |
| 19 | Biggio, Fumera, Roli 2010, Int. J. Machine Learning and Cybernetics 1(1–4), 27–41 | systèmes à classificateurs multiples en milieu adverse | RAPPORTÉ ; papier vraisemblable ; non garanti |
| 20 | Sagawa, Koh, Hashimoto, Liang 2020, ICLR, arXiv 1911.08731 | robustesse distributionnelle par groupes | classique |
| 21 | Sinha, Namkoong, Volpi, Duchi 2018, ICLR, arXiv 1710.10571 | robustesse distributionnelle de Wasserstein certifiée | classique |
| 22 | Madry et collègues 2018, ICLR, arXiv 1706.06083 | entraînement adversarial minimax | classique |
| 23 | Lanctot et collègues 2019, arXiv 1908.09453, OpenSpiel | bibliothèque | classique ; **noms de fonctions à vérifier** : `pyspiel.load_matrix_game` et `exploitability.nash_conv` me semblent exacts ; `fictitious_play.XFPMain` ne me dit rien (la classe que je connais est `XFPSolver`) ; `psro_v2` est un module |
| 24 | McKelvey, McLennan, Turocy 2014, Gambit 16.0.1 | logiciel | classique ; version non vérifiée |
| 25 | Bailey, L. et collègues 2024, arXiv 2412.09565, « Obfuscated Activations Bypass LLM Latent-Space Defenses » | non-convergence du ré-entraînement itératif de sondes ; Llama-3-8B, Mistral-7B, Gemma-2-9B ; sondes linéaires, MLP, autoencodeurs épars ; chute à α = 1 % | **à vérifier en priorité** : **liste d'auteurs manifestement altérée** (« Somani, A.,acy, J. » tronqué ; Rajamanoharan, Nanda, Tegmark que je ne reconnais pas comme auteurs de ce papier) ; modèles et résultat sont des énoncés précis dont rien ne figure dans les pièces (le brouillon : « aucun chiffre repris », R7). PDF lu par session-depot (R-874) : vérifiable en interne |
| 26 | Zou et collègues 2024, NeurIPS 37, arXiv 2406.04313, Circuit Breakers | entraînement des représentations, pas d'une sonde externe | vraisemblable ; l'énoncé « sonde externe vulnérable au noyau de l'ensemble de sondes » est une **inférence d'Argon**, pas un résultat de ce papier |
| 27 | Zou et collègues 2023, arXiv 2310.01405, Representation Engineering | lecture multi-couches | vraisemblable |
| 28 | Marks, Tegmark 2023, arXiv 2310.06824, COLM 2024 | sondage par moyenne de masse | vraisemblable |
| 29 | Casper, Schulze, Patel, Hadfield-Menell 2024, arXiv 2403.05030 | entraînement adversarial latent | vraisemblable |
| 30 | Sheshadri et collègues 2024, arXiv 2407.15549 | entraînement adversarial latent ciblé | vraisemblable ; l'énoncé « lorsque seule une sonde externe de faible capacité est entraînée, elle perd en précision sur le propre » est **à vérifier** (ces papiers entraînent le modèle, pas une sonde) |
| 31 | Perez et collègues 2022, EMNLP, arXiv 2202.03286 | équipe rouge automatique, historique cumulatif | vraisemblable |
| 32 | Ge et collègues 2023, NAACL 2024, arXiv 2311.07689, MART | 4 rondes ; plafond dès la ronde 3–4 ; dégradation sur les bénins proches de la frontière | vraisemblable comme papier ; **les détails (4 rondes, plafond, dégradation) sont à vérifier** |
| 33 | Ma et collègues 2023, arXiv 2310.00322, Red Teaming Game | jeu attaquant–défenseur résolu par théorie des jeux | vraisemblable ; non garanti |
| 34 | « Dhillon et collègues 2024 pour les mélanges stochastiques de défenses » | — | **source suspecte** : citée dans le corps du § 6.4 sans entrée dans la liste des sources, sans titre ni identifiant ; je ne reconnais pas un tel papier de 2024 (le Dhillon que je connais sur les défenses stochastiques est de 2018, élagage stochastique d'activations) |
| 35 | « RepBend » (§ 6.2) | nommé sans référence | sans source ; à vérifier |

Énoncé négatif d'Argon (§ 6.4) : « aucune étude publiée à ce jour n'a démontré qu'un mélange d'équilibre de Nash par tirage aléatoire de sondes linéaires passées bat un agrégateur non linéaire déterministe de même capacité ». C'est une affirmation d'absence, invérifiable par construction et contraire à la règle R8 (zone vierge = question, pas constat) ; à lire comme une question ouverte, pas comme un fait.

Sources que je soupçonne inventées ou fusionnées : n° 4 (fusion de trois papiers de Pinot et collègues), n° 34 (Dhillon 2024, sans référence), et la liste d'auteurs du n° 25. Les noms de fonctions OpenSpiel (n° 23) et l'exposant du n° 11 sont des détails à contrôler avant tout usage.

## 5. Section 5 : les deux conditions pour poser Q2 à classe égale, et le test d'acceptation

**Condition 5.1 — sous-capacité stricte par tâche.** Énoncé : aucun moniteur unique de la classe ne couvre toutes les attaques admissibles, soit max_i min_j G_ij < v* − ε ; Argon la dit « nécessaire et suffisante » pour l'absence d'équilibre pur forcé. Lecture : dans un jeu matriciel, une ligne i est optimale pure si et seulement si min_j G_ij = v* ; la condition caractérise « aucune stratégie pure optimale », plus fort que « pureté non forcée ». Les deux mesures sont distinctes dans le code : `poids_max_min_equilibres` (pureté forcée) et max_i min_j G_ij, calculable depuis `cycle["H"]` (G privée de la colonne de la loi cible). La réalisation proposée (m = 2 unités face à K = 3, ou K = 6, d = 12) est un **changement de configuration** (`unites_Bp` ; pour D, m = t + 1 est codé en dur, py l. 1106) : nouvelle identité, nouveau gel, racine neuve, ce que le brouillon 4 prévoit déjà (S16 : « nouvelle conception à moins d'unités »).

**Condition 5.2 — mélange calculé sur un portefeuille de tâches.** Énoncé : concaténer les attaques de L sous-tâches en colonnes de G. Cohérence : **non codé** ; `resoudre_jeu` est appelé par instance dans `trajectoire`, une loi cible par instance (`loi_cible`). Changement de conception, pas de paramètre ; c'est une piste que la question proposait, reprise sans test ni seuil.

**Test d'acceptation (garde pour le brouillon 5)** : (1) sur ≥ 80 % des tâches du pilote de calibrage, `poids_max_min_equilibres` ≤ 0,60 et part de tâches pures (`est_pur`) < 0,20 ; (2) moyenne de v* − max_i min_j G_ij ≥ S6 = 0,02. Réfutation : si, sous ces conditions, B′ − D ≈ 0 et B′ − mode(B′) ≈ 0, Q2 est « réfutée » et non plus « non exercée ». Cohérence avec le code : les trois quantités existent ou se dérivent (`poids_max_min_equilibres`, `est_pur`, H + `valeur_jeu_restreint`) ; les seuils 0,60, 0,80, 0,20 sont des choix d'Argon sans justification chiffrée dans l'avis ; le seuil de 50 % de la Table 7 et S6 = 0,02 sont bien ceux du brouillon. Le témoin « mode(B′) » n'existe pas comme bras (option du brouillon, voir (g)). Ce test est cohérent avec la logique R5 du brouillon (chemin non exercé) mais il se ferait **sur un pilote de calibrage, avant lecture de la racine de décision**, ce qu'Argon précise.

## 6. Section 6 : transfert aux vrais modèles — résultats publiés cités, tous RAPPORTÉ

1. Bailey, L. et collègues 2024 (arXiv 2412.09565) — ré-entraînement itératif de sondes (linéaires, MLP, autoencodeurs épars) sur Llama-3-8B, Mistral-7B, Gemma-2-9B ; échec de convergence, dégradation des attaques précédentes. RAPPORTÉ ; auteurs altérés ; détails à vérifier sur le PDF lu par session-depot (R-874).
2. Zou et collègues 2024 (Circuit Breakers), Zou et collègues 2023 (Representation Engineering), Marks et Tegmark 2023 — agrégation multi-couches et entraînement des représentations ; vulnérabilité d'une sonde externe au noyau d'un ensemble fini de sondes (ce dernier point est une inférence d'Argon). RAPPORTÉ.
3. Casper et collègues 2024, Sheshadri et collègues 2024 — entraînement adversarial dans l'espace latent (mécanisme f) ; robustesse accrue sur distributions tenues à l'écart ; perte de précision d'une sonde externe de faible capacité (énoncé à vérifier : ces travaux entraînent le modèle). RAPPORTÉ.
4. Perez et collègues 2022, Ge et collègues 2023 (MART), Ma et collègues 2023 (Red Teaming Game), « Dhillon et collègues 2024 » — historique cumulatif (mécanisme a) et formulation en jeu (mécanisme b) sur modèles de langage ; plafond dès la ronde 3–4 dans MART. RAPPORTÉ ; Dhillon sans référence.
5. Pinot et collègues 2020 — invoqué pour la concordance avec le constat B < C3 ; référence amalgamée (§ 4, n° 4).

Pour les mécanismes (c) régularisation et (d) gradients optimistes, Argon ne cite aucun résultat sur sondes ou moniteurs de modèles de langage : il n'écrit ni qu'il en existe, ni qu'il n'en existe pas (silence). La question demandait « lesquels ont été essayés […] avec quel résultat publié » : la réponse est donc partielle pour (c) et absente pour (d).

## 7. Ce qu'il ne répond pas de la question

- Point 1 : « ce qu'il faudrait ajouter » se réduit à une ligne de code (q = (0, …, 0, 1)) et à la distinction erreur de classe / erreur d'oubli ; rien sur l'attaquant local (SLSQP à départs multiples), la boîte et la projection comme parties du jeu.
- Point 2 : les conditions « mémoire de l'attaquant » et « bruit » (n_mc = 256 contre n_eval = 19 998) ne sont pas traitées ; la somme nulle l'est (asymétrie des lissages).
- Point 3 : (c) le volet entropique côté méta-jeu est nommé sans condition, coût ni test ; (d) le test exige d'implanter l'extragradient (pas « le moins cher ») ; aucun coût chiffré en temps de processeur (60,7 s par tâche au brouillon, non repris).
- Point 4 : la dynamique « meilleure réponse » du jouet ne reproduit pas A (§ 2) ; rien de précis pour Gambit au-delà de `gambit-lp` ; nom de fonction OpenSpiel douteux.
- Point 5 : la condition 5.2 n'a ni test ni seuil ; « tâches à équilibre intérieur connu » n'apparaît que par le jouet du § 4.
- Point 6 : rien pour (d) ; (c) couvert par des papiers qui entraînent le modèle, pas une sonde ; une affirmation d'absence (R8) ; aucune page ni chiffre localisé dans les papiers.
- Transversal : il ne signale pas que ses numéros de lignes ne correspondent pas au fichier ; il écrit « sur les JSON déjà calculés du pilote v4 » pour g1 et g2, alors que les moniteurs ne sont pas sérialisés : poids, H et indices sont dans les JSON, tout V d'un moniteur nouveau exige un rejeu.
- Il ne commente pas la Pièce 2 : ni CM4-01 (temps), ni la réserve de S17 (« contrôle faible de la forme » du cycle), qui touche la fiabilité de I3.

## 8. Ce que je n'ai pas pu faire

- Vérifier une seule source sur PDF (aucun servi ; aucun réseau) : tout le § 4 reste RAPPORTÉ.
- Ouvrir le JSON du pilote (non servi à Argon, hors de ma consigne de lecture utile) : les chiffres sont recoupés sur le texte du brouillon 4 et sur la vérification Sonnet, qui les a elle-même recalculés depuis les JSON (Pièce 2 § 4).
- Exécuter le code ou les tests d'Argon (section 4 et tests de réfutation) : aucune exécution.
- Relire les 2 241 lignes du code en entier : lues les fonctions citées par Argon et celles des bras, des indicateurs, du jeu et de l'attaquant (environ 600 lignes) ; non lues : analyse, audit, lancement, gardes de processus.

Aucune recommandation.
