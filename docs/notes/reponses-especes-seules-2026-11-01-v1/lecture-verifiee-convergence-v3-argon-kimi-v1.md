# Lecture vérifiée des avis d'Argon seul et de Kimi seul — question de convergence v3 — v1

## En-tête

- Lecteur : sous-agent neuf, modèle Claude Fable 5.1 (`claude-fable-5-1`), lignée distincte d'Argon (`gemini-4-argon`), de Kimi (`kimi-k3.1-pro`), des rédacteurs du brouillon 4 (Opus) et de sa vérification (Sonnet 5.5). Je n'ai écrit ni la question, ni les pièces, ni les avis, ni la formalisation interne, ni la lecture vérifiée de la v2.
- Date (UTC) relevée par `date -u` : lecture commencée à **2026-11-01, 16:33:14**, écriture commencée à **16:39:06**.
- Cadre tenu : aucun fichier existant modifié, rien scellé, rien commis, aucun appel de modèle, aucun réseau. Lu sous `donnees/` : les deux seuls fichiers nommés (question v3, faits v3). Lu en plus, hors `donnees/` : la première page du PDF `docs/sources/pdf/anteriorite-P-041-v1/2412.09565v2.pdf` (empreinte `9c23a613…`, celle que les faits nomment), pour contrôler les listes d'auteurs de Bailey et collègues que les deux avis donnent ; ce PDF n'a été servi à aucune espèce et son contenu reste RAPPORTÉ ici (seuls les noms de la première page sont employés). Aucune recommandation dans ce document.
- Empreintes SHA-256 recalculées par `sha256sum` (jamais retapées à la main) :

| Fichier | Empreinte | Taille |
|---|---|---|
| `docs/notes/reponses-especes-seules-2026-11-01-v1/reponse-convergence-v3-argon-v1.md` | `4d98830106864eaed29ea203c55d3efdd958d514bef566d6cb65e8edaf42ef2f` | 6 918 mots, 216 lignes |
| `…/manifeste-convergence-v3-argon-v1.json` | `3b7acff926e973bb53e312b0c03bfe2fc5a94d39824296a6de352a7230a80861` | |
| `…/reponse-convergence-v3-kimi-v1.md` | `20ec0cb1b968f0213df377b058b67b65c4188b3f57cbf395dee143b2d13b073f` | 4 867 mots, 364 lignes |
| `…/manifeste-convergence-v3-kimi-v1.json` | `74b57eacfd0730c079245d51a94786820c08ef0b2b5a9a29c318d35a26c8cffd` | |
| `donnees/questions-3-novembre-v1/question-convergence-defense-unique-v3.md` | `73900b1e968380a961c9aca15cdbfd535da00813e90ac148e21c65af0dc30f3c` | 990 mots |
| `donnees/questions-3-novembre-v1/faits-convergence-v3-v1.md` | `580444a6d0f1de3b3624ea8f9703486391ffd8896ffa4aafb9e6d22a55576dff` | 35 056 mots, 3 273 lignes |
| `docs/notes/convergence-defense-v1/argon-seul-convergence-v1/lecture-verifiee-avis-argon-convergence-v1.md` | `a403e5aa9b87eb3b583e6a8a5d9dfe11d9ffb780e3d54c6087802d7a489658d2` | 5 813 mots |
| `docs/notes/convergence-defense-v1/formalisation-jeu-convergence-v1.md` | `a277a5ba28e36c4a4042ef0905510ec9e1772954a5fe29dbd1a4eb7f49d92a77` | 5 507 mots |

Les deux manifestes portent la même question (`question_sha256` = `73900b1e…`) et les mêmes faits (`faits_sha256` = `580444a6…`), le même collisionneur v7 (`c9725f02…`), et chacun l'empreinte de sa réponse (`reponse_sha256` conforme aux recalculs ci-dessus). Argon : 97 141 jetons d'entrée, 15 904 de sortie, 199,6 s, fin `STOP`, 1,7666 dollar sous un plafond de 3. Kimi : 93 321 jetons d'entrée, 30 384 de sortie, 1 099,3 s, fin `stop`, 0,4905 dollar sous un plafond de 1. Observation : 30 384 jetons de sortie pour un texte de 4 867 mots suggère que le compteur de Kimi inclut des jetons de raisonnement non rendus ; rien dans le manifeste ne le dit.

Convention : « Pièce 1 » = brouillon 4, « Pièce 2 » = vérification, « Pièce 3 » = code `arene_melange_v4.py`, « Pièce 4 » = gel v4, « Pièce 5 » = calibrage, comme dans les faits et les avis. « faits l. » = ligne du fichier des faits ; « py l. » = ligne du fichier `.py` (le code commence à faits l. 722 : py l. n = faits l. 721 + n). « Argon l. » et « Kimi l. » = ligne de l'avis.

---

## A. Avis d'Argon (`gemini-4-argon`)

### A.1 Chiffres et affirmations attribués aux pièces, recoupés

Méthode : chaque chiffre ou énoncé rattaché à une pièce est cherché dans les faits. « Juste » = présent et identique ; « inexact » = présent mais différent ; « absent » = introuvable dans les pièces servies.

| Affirmation d'Argon (ligne de l'avis) | Pièce (ligne des faits ou du code) | Verdict |
|---|---|---|
| d = 6, K = 3, loi propre N(0, I₆), ‖μ_k⁰‖ = 4, σ = 1 (l. 6) | configuration faits l. 59–61, 95–97 ; `Config` py l. 166–170 | juste |
| boîte \|μ\| ≤ 5, σ ∈ [0,5 ; 1,5], distance = racine de la moyenne sur k, dimension 2Kd = 36 (l. 7–8) | `Config`, `distance` py l. 423–425, `deplier` py l. 413 | juste |
| δ ∈ {1,4 ; 1,6} après recalibrage sur 48 instances (l. 9) | Pièce 5 `deltas_choisis` ; Pièce 1 résumé 2–3 | juste |
| 7 paramètres (m = 1), 63 (m = 9) ; seuil au quantile 1 − α, α = 0,01, tolérance ±0,005, n_cal = 20 000 (l. 10) | § Métrique faits l. 259 ; S9 ; `calibrer` py l. 514–522 | juste |
| oracle du défenseur : τ = 0,25, n_p = 2 000, n_a = 2 001, seuil gaussien exact pour m = 1, approché pour m > 1 (l. 15) | `objectif_detection` py l. 655–673 et sa docstring ; `Config` | juste |
| attaquant : SLSQP, n_mc = 256 (512 en finale), tri sur le taux dur, n_eval = 19 998 (l. 16) | `meilleure_reponse` py l. 815–850 ; `Config` | juste |
| ℓ₂ = 10⁻³ dans `_logistique` seulement ; `objectif_detection` sans régularisation (l. 17, 67) | py l. 639–652, 655–673 | juste |
| T = 8 (S12) (l. 21) | faits l. 322 | juste |
| A déploie `[(moniteurs[-1], 1.0)]` ; entraîne sur `np.full(len(attaques), 1.0 / len(attaques))` (l. 21) | py l. 1075 et 1107 | juste (contenu) ; **numéros de lignes inexacts** (« l. 634 », « l. 655 ») |
| q̄_t = (1/(t+1)) Σ_{s=0}^{t} δ_{a_s} ; a_8 pèse 1/9 à t = 8 (l. 21, 89) | `attaques = [ctx.cible]` puis une attaque par tour, py l. 1064, 1095 | juste sur le compte ; **implicite** : a_0 est la loi cible, ce que l'avis ne dit pas |
| V(A) 0,0816 / 0,0359 ; V(B) 0,2099 / 0,1746 ; B − A +0,1283 / +0,1387 (l. 27, 100) | Pièce 1 § Prédiction A ; Pièce 2 § 4 | juste |
| v_restreint − V : B +0,019 / +0,024 ; B′ +0,004 / +0,004 (l. 37, 95) | § N'autorise pas, faits l. 184 | juste |
| I1(A) +0,0020 [−0,0029 ; +0,0069] ; −0,0005 [−0,0046 ; +0,0034] (l. 38) | § Prédiction A | juste |
| valeur nulle 617/840 ≈ 0,73452 ; I3 0,9028 / 0,9444 ; excès +0,1683 / +0,2099 (l. 39) | `valeur_nulle_I3` py l. 1014–1018 ; § Prédiction A ; Pièce 2 § 4. Recalculé : (1/2 + 2/3 + 3/4 + 4/5 + 5/6 + 6/7)/6 = 617/840 | juste |
| I2 = moyenne de H[t,t] − H[T,t] ; « oubli ou saturation, non distingués » (CM3-03) (l. 40, 75) | `indicateurs_cycle` py l. 1034–1053 ; § Métrique | juste |
| V₁(A) ≈ 0,072 ; rétention de A 0,37 (décalage 0), 0,24 et 0,23 (décalage 1) (l. 55) | descriptives, faits l. 251 | juste |
| D : I3 − 0,7345 = −0,2831 / −0,3804 (l. 60, 131) | § Prédiction A | juste |
| B : I3 − 0,7345 = +0,00 / +0,02 (l. 60) | résumé 6 | juste |
| « D ainsi que B′ présentent des valeurs fortement négatives (−0,2831 et −0,3804) » (l. 90) | les deux nombres sont ceux de D ; pour B′ le résumé 6 ne donne que « −0,23 à −0,38 » (D et B′ ensemble) | approximatif |
| C1 − A ≈ +0,108 / +0,118 ; C1 construit sur la trajectoire de B (l. 87) | descriptives l. 251 ; `SOURCE_TEMOIN` py l. 143 | juste |
| B − C3 −0,1935 / −0,1443 ; B − D −0,2341 / −0,1795 (l. 97) | § Prédiction A, B | juste |
| Δ(B, A) sur (ii) −0,0538 [−0,0784 ; −0,0274] ; −0,0580 [−0,0893 ; −0,0233] (l. 98) | § Prédiction A | juste |
| 511 paramètres B′ et C3′, 63 pour D ; (T+1)² évaluations de G (l. 99, 134) | § Métrique l. 259 | juste |
| `resoudre_jeu` par HiGHS ; q* avant `entrainer` (l. 94, 143) | py l. 744–751, 1101–1102 | juste (contenu) ; lignes « 636–653 », « 650–651 » inexactes |
| D : maxout à t + 1 unités ; C3/C3′ : « ou » standardisé, λ = 8, recalibré à α (l. 128) | py l. 1106 ; `ou_deterministe` py l. 536, `MoniteurOu` 553 | juste ; ligne « 654 » inexacte |
| D 0,4440 / 0,3541 ; D − A +0,362 / +0,318 ; plateau ≈ 0,40 dès le tour 4 (l. 131) | Pièce 2 § 4 ; descriptives | juste |
| C3 − B +0,1935 / +0,1443 (l. 132) | descriptives (C3 − A +0,322 / +0,283 ; B − C3) | juste |
| B′ − C3′ +0,0072 [+0,0015 ; +0,0127] ; +0,0114 [+0,0072 ; +0,0160] ; dilution déclarée (l. 135) | § Prédiction A ; § N'autorise pas | juste |
| 12 puis 48 départs en `phase_finale` ; 100 départs et (1 + 12) dans `attaquant_independant` (l. 119) | `Config` : `departs_final 12`, `departs_renforce 48`, `audit_departs 100`, `audit_es_lambda 12` ; py l. 1152–1158, 1642–1668 | juste ; lignes « 674–681, 880–903 » inexactes |
| déclencheur 5 (optimiseur) (l. 121) | Critères de lecture, déclencheur 5 | juste |
| poids purs 70,8 % (17/24) et 58,3 % (14/24) ; pureté forcée 17/17 et 14/14 ; moniteur dominant aux tours 2–4 dans 14/17 et 12/14 (l. 172–173) | § Prédiction A ; résumé 5 ; Pièce 2 § 4 | juste |
| `poids_max_min_equilibres` minimise max_i p_i parmi les stratégies optimales (l. 173, 186) | py l. 768–788 | juste ; lignes « 500–516 », « 500 » inexactes |
| B′ − D +0,0024 / +0,0042 ; tâches à mélange réel +0,0031 (n = 7) / +0,0047 (n = 10) (l. 174) | § Prédiction A, descriptives | juste |
| S16 = 9 unités = classe du moniteur final de D (l. 172) | S16 | juste |
| Bailey cité comme `2412.09565v2` au § Antériorité (l. 200) | faits l. 208 | juste |
| « l'angle de rotation maximal ≈ arcsin(√K δ / r_cible) » (l. 58) | dérivation d'Argon | absent des pièces (déduction, non attribuée) |
| « FP bilatéral converge au taux O(t^{−1/2}) ou O(t^{−1/(\|M\|+\|Θ\|−2)}) » (l. 24) | — | absent des pièces ; RAPPORTÉ ; le taux O(t^{−1/2}) pour le jeu fictif n'est pas un résultat établi en général (voir § A.3) |
| contenu des articles de Bailey, Pinot, Zou, Perez, MART (§ 2.1, § 6) | les pièces disent « aucun chiffre repris » de Bailey (faits l. 208) | absents des pièces ; tous RAPPORTÉ (§ A.3) |

**Décompte.** 40 chiffres et affirmations rattachés aux pièces : **38 justes, 1 approximatif** (les −0,2831 / −0,3804 attribués à « D ainsi que B′ »), **1 implicite** (a_0 = loi cible non dite), **0 chiffre du pilote absent ou déformé**. Les **neuf numéros de lignes de la Pièce 3** cités (634, 655, 650–651, 594–608, 500–516, 636–653, 654, 674–681, 880–903) sont **tous inexacts** (objets réels : py l. 1075, 1107, 1101–1102, 655–673, 768–788, 1079–1104, 1106, 1152–1158, 1642–1668) ; aucun ne désigne un objet absent, et le contenu cité (noms, extraits) est exact. C'est la même anomalie que sur la v2 (lecture vérifiée v2, § 1.1 : quinze numéros tous inexacts). Trois énoncés sont des dérivations ou des résultats de littérature absents des pièces.

### A.2 Réponse à chaque point de la question

1. **Formalisation.** Jeu écrit en entier (joueurs, Θ_δ, classe M_m, gain U = taux de détection à α, bilinéaire sur les mélanges ; somme nulle en population, « quasi-nulle » en implémentation par trois découplages : seuil gaussien, oracle lissé de l'attaquant, invariance d'échelle brisée par la logistique ; l. 4–18). A n'est pas le jeu fictif : « suivre le meneur » (Follow-The-Leader) côté défenseur contre meilleure réponse myope côté attaquant ; le dernier itéré ne peut converger que si un point selle pur existe dans la classe (l. 22–27). Métrique : l'exploitabilité unilatérale v* − V(iii) est « la seule qui certifie » ; I1 est une stationnarité, I3 un test non paramétrique d'anti-persistance, H et I2 une rétention ; sur des sondes réelles, transposables : la matrice H et I1, I2, le cosinus des vecteurs normaux des sondes pour I3, et l'écart dual sur la sous-matrice H (l. 37–46).
2. **Pourquoi ça cycle.** Trois mécanismes : incompatibilité géométrique d'un demi-espace unique (m = 1 < K = 3) face à des composantes mobiles, donc pas d'équilibre pur ; instabilité du dernier itéré de « suivre le meneur » sans terme proximal ; saturation de capacité (pas oubli : tout l'historique est rejoué) (l. 54–79). Inévitable si m < K, δ intermédiaire, déploiement pur face à un adversaire myope ; disparaît avec une classe assez riche (D) ou un mélange stochastique (B) (l. 56–60).
3. **Mécanismes.** (a) A cycle car l'attaquant ne joue pas le jeu fictif, la classe linéaire n'est pas convexe en fonctions, l'uniforme dilue la dernière attaque, et ce n'est pas un artefact de I3 ; test : évaluer le mélange uniforme des moniteurs mêmes de A en une `phase_finale` (l. 86–91). (b) B et B′ sont déjà l'oracle double ; prix : plafond de capacité par requête, régression sur (ii), stockage (l. 93–103). (c) pénalité proximale ou moyenne mobile des poids : stabilise sans progresser ; test sur 8 instances (l. 105–111). (d) gradients optimistes ou extragradient : conditions violées (ni concave en W ni convexe en θ) ; test par 8 pas puis `phase_finale` (l. 113–125). (e) classe élargie : D, C3, C3′ ; prix : coût par requête, dilution du seuil par borne de l'union ; test : d = 20, K = 12, m = 3 (l. 127–138). (f) pire cas sur l'historique (softmin, robustesse par groupes) dans la boucle de l'oracle ; test : `softmin` dans `objectif_detection` (l. 140–148). Pas de (g).
4. **Jeu jouet.** Pile ou face apparié, pierre–feuille–ciseaux, jeu bilinéaire sur le disque ; protocole en cinq lignes avec OpenSpiel (`matrix_rps`, `matching_pennies`, `fictitious_play`, `exploitability.nash_conv`) et Gambit ; critère d'acceptation : I1 = 0, I3 − 0,7345 > 0 et NashConv > 0 pour la règle de A ; NashConv → 0 pour le jeu fictif et l'oracle double (l. 154–161).
5. **Classe égale.** Diagnostic : à 9 unités un moniteur domine faiblement toutes les lignes de G dès le tour 3–4, d'où la pureté forcée (l. 172–174). Conditions : régime sous-capacitaire contrôlé (1 < m < K, D bloqué à m), mélange sur un portefeuille de sous-familles, et garde de préqualification : médiane sur les instances de `poids_max_min_equilibres` ≤ 1/2 (l. 179–188).
6. **Transfert.** (a) Bailey et collègues : ré-entraînement itératif ne converge pas (RAPPORTÉ) ; (e) Zou 2023, Zou 2024, MacDiarmid 2024 : agrégation déterministe multi-couches (RAPPORTÉ) ; (a), (b), (f) : Perez 2022, Samvelyan 2024, MART : boucles co-évolutives ; aucun mélange d'équilibre explicite sur sondes publié (l. 199–216). Rien pour (c), (d).

### A.3 Sources citées — toutes RAPPORTÉ (aucun PDF servi aux espèces ; R7)

| # | Référence telle qu'écrite | Statut |
|---|---|---|
| 1 | Brown 1951, Cowles 13, 374–376 | classique |
| 2 | Robinson 1951, Ann. Math. 54(2), 296–301, JSTOR 1969530 | classique ; identifiant plausible |
| 3 | Shalev-Shwartz 2012, Found. Trends ML 4(2), 107–194 | classique ; usage (instabilité de « suivre le meneur ») plausible |
| 4 | Lanctot et collègues 2017, arXiv 1711.00832 | classique |
| 5 | Shapley 1964, Ann. Math. Studies 52, 1–28 | classique ; attribué aux « cycles limites des dynamiques de meilleure réponse », alors que l'exemple de Shapley porte sur le jeu fictif en somme non nulle (voir Kimi l. 132 et formalisation interne § 4.4) : **usage à vérifier** |
| 6 | Pinot, Ettedgui, Rizk, Chevaleyre, Atif 2020, ICML, PMLR 119, 7717–7727, arXiv 2002.11560 | plausible (article ICML 2020 sur les stratégies mixtes) ; « théorème d'impossibilité d'une défense déterministe unique » : énoncé à vérifier sur PDF |
| 7 | Mertikopoulos, Papadimitriou, Piliouras 2018, SODA, 2703–2717, arXiv 1709.02738 | classique |
| 8 | Daskalakis, Ilyas, Syrgkanis, Zeng 2018, ICLR, arXiv 1711.00141 | classique |
| 9 | Madry et collègues 2018, arXiv 1706.06083 | classique ; PDF `1706.06083v4` présent dans le dépôt, non relu |
| 10 | McMahan, Gordon, Blum 2003, ICML 536–543 | classique |
| 11 | Izmailov et collègues 2018, UAI, arXiv 1803.05407 | classique |
| 12 | Korpelevich 1976, Matekon 12, 747–756 | **à vérifier** : l'original (Ekonomika i Matematicheskie Metody 12, 747–756) et la traduction Matekon sont deux publications ; même réserve qu'à la v2 |
| 13 | Mertikopoulos et collègues 2019, ICLR, arXiv 1807.02629 | classique |
| 14 | Goodfellow et collègues 2013, ICML, arXiv 1302.4389 | classique |
| 15 | Sagawa et collègues 2020, ICLR, arXiv 1911.08731 | classique |
| 16 | Lanctot et collègues 2019, OpenSpiel, arXiv 1908.09453 | identifiant juste ; **liste d'auteurs suspecte** (« Timmer, S., Karlsson, K., Eccles, T., Rowland, M., Letunic, R., Genes, H., Borsa, D., Mandhane, A. » ne correspondent pas aux auteurs que je connais de ce rapport) ; nom de jeu `matching_pennies` **inexact** : dans OpenSpiel 2.0.2 installé dans le dépôt (jouet v1), `matrix_rps` et `matrix_mp` se chargent, `matching_pennies` non ; `exploitability.nash_conv` et le module `fictitious_play` existent (vérifié localement, sans réseau) |
| 17 | Savani et Turocy 2024, « Gambit: The package for computation in game theory », JOSS | plausible ; non vérifié |
| 18 | Bohnenblust, Karlin, Shapley 1950, Ann. Math. Studies 24, 51–72 | classique ; usage (dimension du polytope des stratégies optimales) plausible |
| 19 | Bailey, L., Serrano, E., Abeliuk, A., wagstaff, B., & Steinhardt, J. 2024, arXiv 2412.09565 | identifiant juste ; **liste d'auteurs fausse** : la première page du PDF du dépôt (`9c23a613…`) donne Bailey, Serrano (Alex), Sheshadri, Seleznyov, Taylor, Jenner, Hilton, Casper, Guestrin, Emmons ; Abeliuk, Wagstaff et Steinhardt n'y figurent pas. Le contenu attribué (ré-entraînement itératif qui ne converge pas, Llama-3) est absent des pièces : **à vérifier en priorité** (même anomalie qu'à la v2) |
| 20 | Zou et collègues 2023, arXiv 2310.01405 | plausible |
| 21 | Zou et collègues 2024, arXiv 2406.04313 | plausible ; l'énoncé « augmentation de la dimension du sous-espace surveillé améliore la détection » est une lecture d'Argon |
| 22 | MacDiarmid et collègues 2024, « Simple probes can catch sleeper agents », note Anthropic | plausible ; non vérifié |
| 23 | Perez et collègues 2022, EMNLP 3419–3448, arXiv 2202.03286 | plausible |
| 24 | Samvelyan et collègues 2024, arXiv 2402.16822 | plausible ; PDF `2402.16822v3` présent dans le dépôt, non relu |
| 25 | « Ge, S., zhao, C., Rd, S., et al. / Meta (2024). MART », NAACL 2024, arXiv 2311.07689 | identifiant plausible (PDF `2311.07689v1` présent, non relu) ; **liste d'auteurs altérée** (« Rd, S. ») |
| 26 | taux O(t^{−1/2}) du jeu fictif (l. 24, sans source) | **douteux** : la formalisation interne § 4.2 rappelle (RAPPORTÉ) que la conjecture de Karlin O(1/√t) a un contre-exemple (Daskalakis et Pan 2014) ; seule la borne lente de Robinson est établie |

Sources suspectes : n° 19 (auteurs faux, contrôlé sur la première page du PDF), n° 16 (auteurs, nom de jeu), n° 25 (auteurs), n° 26 (taux sans source), n° 5 (usage). Énoncé négatif (l. 216 : « n'a pas de résultat expérimental publié ») : affirmation d'absence, non vérifiable, à lire comme une question (R8).

### A.4 Ce que l'avis ne répond pas

- Point 1 : rien sur la convention de l'écart de Nash (somme ou moitié) ; le regret externe n'est pas discuté ; « ce qu'il faudrait ajouter » se limite à compacifier les paramètres et à remplacer les échantillons par des espérances (l. 18).
- Point 2 : « bruit » (n_mc = 256 contre n_eval = 19 998, Monte-Carlo) n'est pas traité comme condition du cycle ; la dépendance temporelle introduite par le départ chaud de l'attaquant (`departs_suppl=[attaques[-1]]`, py l. 1084) n'est pas vue ; il affirme la valeur nulle 0,7345 « exacte » sous échangeabilité (l. 39) sans dire que le code brise l'échangeabilité.
- Point 3 : aucun coût en secondes de processeur (60,7 s par tâche au brouillon, non repris) ; (c) « distillation » et « entropie » nommées dans le titre, non traitées ; (g) absent.
- Point 4 : le protocole ne dit pas, pour la règle de A, laquelle des deux moyennes (défenseur, attaquant) converge ou non ; nom de jeu OpenSpiel inexact.
- Point 5 : la garde « médiane ≤ 1/2 » (l. 187) est un seuil posé sans justification chiffrée ; « tâches à équilibre intérieur connu » n'est traité que par la conception sous-capacitaire.
- Point 6 : rien pour (c) ni (d) sur sondes ; aucune page ni chiffre localisé ; sources altérées.
- Transversal : ne signale pas que ses numéros de lignes ne correspondent pas au fichier ; ne commente ni la réserve de S17 (« contrôle faible de la forme » du cycle, faits l. 339) ni CM4-01 ; ne dit pas que les moniteurs ne sont pas sérialisés (tout V d'un moniteur nouveau exige un rejeu).

---

## B. Avis de Kimi (`kimi-k3.1-pro`)

### B.1 Chiffres et affirmations attribués aux pièces, recoupés

| Affirmation de Kimi (ligne de l'avis) | Pièce | Verdict |
|---|---|---|
| I1 +0,0020 / −0,0005 ; I3 0,9028 / 0,9444 contre 0,7345 ; écarts +0,1683 / +0,2099 (l. 3) | § Prédiction A ; Pièce 2 § 4 ; Pièce 4 § 3 point 5 (« § 3.5 ») | juste |
| matrice restreinte : lignes = moniteurs, colonnes = attaques, programme linéaire à somme nulle (l. 28) | `resoudre_jeu` py l. 734–757 | juste |
| schéma en cinq étapes de `trajectoire` et `phase_finale` (l. 32–38) | py l. 1056–1127, 1145–1182 | juste |
| règle idéalisée de A : argmax de la moyenne sur H_t, attaquant argmin contre m_t (l. 44–48) | py l. 1075, 1084, 1107 | juste ; **omission** : l'historique H_t contient la loi cible (a_0) |
| attaquant = optimiseur local multi-départs ; V = plus faible des deux recherches (l. 65) | `meilleure_reponse`, `phase_finale` py l. 1159 | juste |
| seuil gaussien « déclaré approché » pour les non linéaires (l. 65) | docstring `objectif_detection` py l. 656–658 | juste |
| agrégation déterministe recalibrée ≠ linéaire dans les poids (l. 90) | `ou_deterministe` py l. 536–550 (recalibrage à α) | juste |
| le code emploie l'attaque précédente comme départ de la recherche suivante (l. 117) | py l. 1084 `departs_suppl=[attaques[-1]]` | juste |
| B′ purs 17/24 puis 14/24 ; forcés 17/17 et 14/14 (l. 160) | Pièce 2 § 4 ; résumé 5 | juste |
| V(A) = 0,0359 au δ haut ≈ 3,6 α ; « ne progresse pas y discrimine peu » (l. 166) | résumé 6 ; Table 5 | juste |
| v_R − V : B +0,019 / +0,024 ; B′ +0,004 / +0,004 ; « pas des certificats du jeu complet » (l. 209) | § N'autorise pas | juste |
| `poids_max_min_equilibres` = min sur P* de max_i p_i, P* = {p ≥ 0, Σ p = 1, Gᵀp ≥ v*} (l. 277–286) | py l. 768–788 (avec tolérance 10⁻⁹) | juste |
| B′ − D mélange trois effets : tirage, sélection maximin, distribution d'entraînement (l. 308) | § N'autorise pas (« B′ ajoute à D une sélection … et une distribution d'entraînement différente ») | juste (le tirage est le troisième, implicite dans la pièce) |
| A n'est pas le protocole de Bailey : oracle et règle différents, déclaré par les pièces (l. 318) | § N'autorise pas ; docstring py l. 40–43 | juste |
| Bailey cité en v2, PDF non servi (l. 358) | faits en-tête | juste |

**Décompte.** 15 chiffres et affirmations rattachés aux pièces : **15 justes, 0 inexact, 0 absent** ; une **omission** (la loi cible dans l'historique de A). Kimi ne cite aucun numéro de ligne (fonctions nommées seulement : toutes existent). Il recopie peu de chiffres du pilote et aucun qu'il ne trouve dans les pièces.

### B.2 Réponse à chaque point de la question

1. **Formalisation.** Noyau statique (moniteur ou mélange p ; θ ∈ Θ_δ ; U = probabilité de détection au seuil calibré ; −U) ; le jeu dynamique complet est un jeu extensif à politiques dépendant de l'historique dont A est une politique fixée, pas une recherche d'équilibre (l. 13–38). Liste de sept choses à déclarer avant tout théorème (objet, exactitude des réponses, départage, objet de la convergence, gain dur ou lissé, calibrage, mélanges permis ; l. 55–63). Table des régimes : Robinson ne vaut que des deux côtés ; un seul côté : aucun théorème ; continu : hypothèses à ajouter (l. 69–78). L'oracle à fausses alertes fixées : seuil dans la stratégie, gain non bilinéaire en paramètres ; surrogate ≠ gain ; réponse à l'uniforme ≠ minimax (l. 86–88). Métrique : écart de Nash (NashConv) défini avec sa convention, table de sept mesures (exploitabilité, valeur de sécurité, I1, I3, distance, H, regret) avec ce que chacune établit et sa lisibilité sur sondes ; NashConv répond à la question théorique mais seulement sur un jeu restreint déclaré (l. 94–115) ; 0,7345 est une référence conditionnelle, le départ chaud brisant l'échangeabilité (l. 117).
2. **Pourquoi ça cycle.** Quatre phénomènes distingués (meilleure réponse pure, jeu fictif complet, descente-montée, oubli) ; Shapley est hors de la garantie de Robinson et ne réfute pas la somme nulle finie ; l'apprentissage régularisé est une analogie (l. 125–132). Quatre causes avec statut inégal : asymétrie (structurelle, principale), uniforme (possible, non démontré), classe linéaire (plafond, pas universel), mesure (I3 ≠ non-convergence), chacune avec ce qui la réfuterait (l. 136–168). Proposition : avec réponses exactes, un point fixe serait une meilleure réponse mutuelle pure ; sans équilibre pur, pas de point fixe, mais pas nécessairement un cycle périodique (récurrent, irrégulier, chaotique) ; conditions où le cycle n'est pas inévitable (l. 172–187).
3. **Mécanismes.** (a) à (g), chacun avec condition, prix, test ; les tests sont génériques : discrétiser en jeu fini avec réponses exactes et comparer A, jeu fictif complet, autres pondérations (l. 201) ; certificat de l'oracle double puis vérification indépendante (l. 211) ; mesurer H et NashConv séparément pour (c) (l. 221) ; surrogate contre gain dur pour (d) (l. 231) ; classes emboîtées sur deux familles (équilibre pur connu, intérieur connu) pour (e) (l. 239) ; robustesse intérieure contre robustesse à la réponse finale pour (f) (l. 251) ; (g) déployer la moyenne d'un algorithme sans regret, regret et NashConv mesurés ensemble (l. 253–261).
4. **Jeu jouet.** Cinq lignes : OpenSpiel tel quel sur pile ou face apparié et pierre–feuille–ciseaux ; jeu fictif complet puis dynamique asymétrique avec départages consignés ; oracle double jusqu'au certificat, recoupé avec Gambit ; séparation des mesures (I3 élevé ne vaut plus non-convergence si NashConv moyen → 0) ; répétition sous départages et erreurs contrôlées avant transposition (l. 267–271).
5. **Classe égale.** Deux certificats sur G : non-dégénérescence (tâche à équilibre intérieur connu, ou programmes linéaires bornant chaque p_i sur P*) et valeur stratégique du mélange v* − max_i min_j G_ij > 0 ; locaux au jeu restreint ; le portefeuille de tâches n'est pas une garantie ; comparateurs à moniteurs, distribution d'entraînement, classe et calibrage identiques (l. 277–308).
6. **Transfert.** Table (a) à (g) : une seule référence directement pertinente (Bailey, PDF non servi) ; (f) : entraînement adversarial latent (Sheshadri) adjacent ; tout le reste « non établi par les pièces, non "jamais publié" » (l. 314–326).

### B.3 Sources citées — toutes RAPPORTÉ (aucun PDF servi ; R7)

| # | Référence telle qu'écrite | Statut |
|---|---|---|
| [1] | Robinson 1951, DOI 10.2307/1969530 | classique |
| [2] | Brown 1951, Cowles 13 | classique |
| [3] | Shapley 1964, Ann. Math. Studies 52 | classique ; usage conforme (non-convergence du jeu fictif hors somme nulle) |
| [4] | Mertikopoulos, Papadimitriou, Piliouras 2018, arXiv 1709.02738, DOI 10.1137/1.9781611975031.172 | classique ; DOI non vérifié |
| [5] | Daskalakis et collègues 2018, arXiv 1711.00141 | classique |
| [6] | Mokhtari, Ozdaglar, Pattathil 2020, AISTATS, PMLR 108, 1497–1507, arXiv 1901.08511 | plausible |
| [7] | McMahan, Gordon, Blum 2003, DBLP conf/icml/McMahanGB03 | classique |
| [8] | Lanctot et collègues 2017, arXiv 1711.00832 | classique |
| [9] | Freund et Schapire 1999, GEB 29, 79–103, DOI 10.1006/game.1999.0738 | classique |
| [10] | McCloskey et Cohen 1989, PLM 24, 109–165 | classique |
| [11] | Kirkpatrick et collègues 2017, PNAS 114(13), arXiv 1612.00796 | classique |
| [12] | Izmailov et collègues 2018, arXiv 1803.05407 | classique |
| [13] | **absent** : la numérotation saute de [12] à [14] ; aucun « [13] » dans le texte | anomalie de forme |
| [14] | Sinha, Namkoong, Duchi 2018, ICLR, arXiv 1710.10571 | classique (auteur Volpi omis selon la v2) |
| [15] | Bailey, Infanger, Sheshadri, Seleznyov, Taylor, Jenner, Steinhardt, Casper, Emmons 2024, arXiv 2412.09565 v2 | identifiant juste ; **liste d'auteurs partiellement fausse** (première page du PDF du dépôt : Serrano, non Infanger ; Hilton, non Steinhardt ; Guestrin manque) ; Kimi déclare lui-même « PDF non servi, détails à contrôler » ; le contenu attribué (« amélioration de robustesse par ré-entraînement, sans clore la généralisation ») est absent des pièces et **diverge** de celui qu'Argon attribue au même papier |
| [16] | Sheshadri et collègues 2024, arXiv 2407.15567 | plausible (le dépôt tient `2407.15549v3`, autre identifiant : à vérifier lequel est le bon) |
| [17] | Lanctot et collègues 2020, OpenSpiel, arXiv 1908.09453 | identifiant juste ; daté 2020 (arXiv 2019) |
| [18] | McKelvey, McLennan, Turocy 2016, Gambit | plausible |

Sources suspectes : [15] (auteurs, contenu divergent d'Argon), [16] (identifiant arXiv à confronter à celui du dépôt), [13] manquant.

### B.4 Ce que l'avis ne répond pas

- Point 1 : il ne dit pas que l'historique de A contient la loi cible ; il n'écrit pas le jeu avec ses constantes (d, K, δ, m) ni les trois découplages d'implémentation un à un (l'avis reste au niveau des principes).
- Point 2 : aucun mécanisme géométrique (pourquoi m = 1 face à K = 3) ; « sous quelles conditions inévitable » reçoit une proposition abstraite (pas d'équilibre pur → pas de point fixe) sans lien aux chiffres du pilote ; « bruit » traité en une phrase (l. 187).
- Point 3 : aucun « test le moins cher **dans notre jeu** » rattaché à une fonction du code ou à un bras existant ; les tests supposent une version discrétisée à réponses exactes qui n'existe pas ; aucun coût chiffré.
- Point 4 : le protocole ne dit pas ce que la règle asymétrique doit donner (prédiction), seulement ce qu'il faut journaliser.
- Point 5 : la méthode « borner chaque p_i » est nommée sans formule ni seuil ; pas de condition sur la conception (m, K) qui rendrait l'équilibre intérieur.
- Point 6 : presque tout est « non établi » ; une seule référence à sondes ; rien de localisé.
- Transversal : ne relève pas que C1 est construit sur les moniteurs de B et non de A ; ne commente ni la Pièce 2 ni la Pièce 5 (calibrage) ; ne signale pas la non-sérialisation des moniteurs.

---

## 5. Accords entre Argon et Kimi, et pistes originales de chacun

### 5.1 Accords (pistes générales consensuelles), avec renvois

1. **A n'est pas le jeu fictif de Brown–Robinson** : jeu fictif d'un seul côté, attaquant myope au dernier moniteur pur ; les théorèmes de convergence ne s'appliquent pas tels quels (Argon l. 22 ; Kimi l. 5, 51, 140). Conforme au code (py l. 1075, 1084, 1107) et à la formalisation interne § 0 et § 2.1.
2. **Somme nulle en population, approximations en implémentation** : gain lissé ≠ gain dur, seuil approché, optimiseurs locaux des deux côtés (Argon l. 14–17 ; Kimi l. 61–65, 86–87).
3. **Sans point selle pur dans la classe déployée, le dernier itéré ne peut converger** ; convergence des moyennes ≠ convergence du dernier itéré (Argon l. 25–27 ; Kimi l. 74, 127–128, 176–178).
4. **L'écart de Nash (exploitabilité) est la métrique qui répond à la question théorique, calculable exactement seulement sur le méta-jeu restreint** ; I1 est une stationnarité et I3 une récurrence géométrique, ni l'un ni l'autre ne mesure la convergence (Argon l. 37–40 ; Kimi l. 107–115). La formalisation interne § 3 dit la même chose.
5. **v_R − V n'est pas un certificat du jeu complet** (Argon l. 95 ; Kimi l. 209).
6. **La pureté de B′ est un plafond de classe** lié à l'existence d'un équilibre pur (dominance d'une ligne de G chez Argon l. 174 ; « plafond local de classe » chez Kimi l. 160).
7. **Jeu jouet** : OpenSpiel pris tel quel, pierre–feuille–ciseaux et pile ou face apparié, jeu fictif bilatéral, règle asymétrique de A, oracle double, écart de Nash par tour, recoupement Gambit, et séparation des mesures (I1, I3 contre NashConv) (Argon l. 157–161 ; Kimi l. 267–271).
8. **Rendre Q2 posable par des certificats calculés sur G avant de lire B′ − D**, à partir de `poids_max_min_equilibres` et d'une marge (Argon l. 186–188 ; Kimi l. 283–306).
9. **Le portefeuille de tâches ne garantit rien seul** : Argon l'assortit d'une condition de capacité (l. 183–184), Kimi le dit explicitement (l. 306).
10. **Régularisation (c)** : stabilise ou masque sans créer de valeur stratégique (Argon l. 108 ; Kimi l. 219). **Extragradient (d)** : hypothèses convexe-concave ou monotone violées ; convergence du surrogate ≠ convergence de la détection dure (Argon l. 117–120 ; Kimi l. 225–227). **Pire cas sur l'historique (f)** : ne protège que dans le support (Argon l. 145 ; Kimi l. 243).
11. **Transfert** : aucun mélange d'équilibre ou oracle double sur sondes d'activations publié que l'un ou l'autre puisse citer ; Bailey et collègues est une analogie d'objet seulement (Argon l. 216 ; Kimi l. 318–319).

### 5.2 Pistes originales d'Argon (une seule espèce)

- Qualification de A comme « suivre le meneur » (Follow-The-Leader) contre meilleure réponse, avec Shalev-Shwartz 2012 pour l'instabilité sans régularisation (l. 22, 33).
- Mécanisme géométrique : m = 1 < K = 3, angle de rotation ≈ arcsin(√K δ / r_cible), conditions d'inévitabilité (δ intermédiaire, déploiement pur) et de disparition (classe riche, mélange stochastique) (l. 55–60) ; théorème d'impossibilité de Pinot et collègues (l. 64).
- Test de (a) : évaluer le mélange uniforme Ā_T des moniteurs **mêmes de A** en une `phase_finale` (l. 91). (Cette mesure est aussi celle que la formalisation interne § 3.3 point 2 nomme « exploitabilité de la moyenne de A » ; originale parmi les deux espèces, pas dans le dépôt.)
- Tests chiffrés et localisés dans le code : pénalité proximale ou moyenne des poids normalisés recalibrée sur `Xcal`, 8 instances (l. 109) ; `softmin` sur les blocs d'attaques dans `objectif_detection` (l. 146) ; 8 pas d'extragradient puis `phase_finale` contre le déclencheur 5 (l. 121) ; d = 20, K = 12, m bloqué à 3 pour faire recycler D (l. 136).
- Transposition de I3 aux sondes réelles par le cosinus des vecteurs normaux w_s/‖w_s‖ ou des centroïdes d'activations ; écart dual sur la sous-matrice H (l. 45–46).
- Explication de B′ − C3′ > 0 par la borne de l'union sur le seuil (dilution par les moniteurs faibles) (l. 135) ; explication de la pureté par dominance faible d'une ligne de G dès le tour 3–4 (l. 174).
- Conception sous-capacitaire contrôlée (1 < m < K, D bloqué à m) et garde « médiane de `poids_max_min_equilibres` ≤ 1/2 » avant gel (l. 180, 186–188).
- Jeu bilinéaire sur le disque unité comme témoin continu (l. 154).

### 5.3 Pistes originales de Kimi (une seule espèce)

- Le jeu complet comme jeu extensif à politiques dépendant de l'historique ; A est une politique fixée, non une recherche d'équilibre (l. 38).
- Liste des sept déclarations préalables à tout théorème (objet, exactitude et erreur des réponses, départage, objet de la convergence, gain dur ou lissé, calibrage exact ou non, mélanges permis) (l. 55–63).
- Convention de l'écart de Nash à déclarer (somme ou moitié) (l. 103) ; « valeur de sécurité » min_q U(p, q) et **regret externe** comme mesures lisibles sur la séquence observée sans connaître l'équilibre (l. 108, 113).
- La valeur nulle 0,7345 est conditionnelle : le départ chaud `departs_suppl=[attaques[-1]]` brise l'échangeabilité (l. 117).
- Statut inégal des quatre causes (asymétrie structurelle principale ; uniforme possible non démontré ; classe = plafond, pas universel ; mesure) avec, pour chacune, ce qui réfuterait l'attribution (l. 136–168) ; et, en 2.3, la distinction entre « pas de point fixe » et « cycle périodique » (récurrent, irrégulier, chaotique) (l. 178).
- (e) : « si la limitation est informationnelle (distributions trop recouvrantes au taux de fausses alertes imposé) plutôt que fonctionnelle, aucune capacité ne supprime le plafond » (l. 235).
- (g) : déployer la moyenne d'un algorithme sans regret, regret externe et NashConv mesurés ensemble dans un méta-jeu fini (l. 253–261) ; l'entropie peut masquer la pureté (l. 219).
- Point 5 : programmes linéaires bornant chaque p_i sur P* (équilibre intérieur certifié si toutes les bornes inférieures sont strictement positives) ; marge v* − max_i min_j G_ij (la formalisation interne § 6 propose la même marge, non les bornes par coordonnée) ; comparateurs à moniteurs, distribution d'entraînement, classe et calibrage identiques, seuls les poids variant (l. 295–308).
- Discipline de lecture : « non établi par les pièces » ≠ « jamais publié » (l. 314) ; séparation « robustesse à l'intérieur de l'ensemble d'incertitude » et « robustesse à la réponse finale » (l. 251).

### 5.4 Divergences de fond (sans jugement)

- Inévitabilité : Argon la tient pour acquise sous m < K (l. 57–59) ; Kimi refuse de la généraliser (l. 158, 178).
- I3 sur sondes réelles : transposable par cosinus des poids (Argon l. 45) contre « difficile à transposer sans métrique canonique » (Kimi l. 110).
- Valeur nulle 0,7345 : exacte (Argon l. 39) contre conditionnelle (Kimi l. 117).
- Bailey et collègues : « ne converge pas, nouvelles directions à chaque itération » (Argon l. 201) contre « amélioration de robustesse par ré-entraînement sans clore la généralisation » (Kimi l. 318) ; les deux RAPPORTÉ, le PDF non servi.
- Shapley 1964 : cité pour les cycles de meilleure réponse (Argon l. 63) contre « hors de la garantie de Robinson, ne s'applique pas » (Kimi l. 132).

---

## 6. Cohérence avec le code de l'arène (`arene_melange_v4.py`, `70c77fd5…`)

**Ce qui existe déjà comme bras ou mesure** (vérifié sur le code servi) :
- (a) « meilleure réponse à l'historique » : c'est A (`trajectoire`, py l. 1075, 1107), la loi cible comprise dans l'historique (py l. 1064).
- (b) oracle double : B et B′ (py l. 1079–1104 ; `resoudre_jeu` py l. 734–757, solveur HiGHS, primal et dual contrôlés) ; valeur restreinte consignée (`valeur_jeu_restreint`, py l. 1116) ; pureté et pureté forcée (`est_pur`, `poids_max_min_equilibres`, py l. 764–788, 1118–1119).
- (e) classe élargie : D (maxout à t + 1 unités, py l. 1106), C3 (`ou_deterministe`), C3′ (`MoniteurOu`) ; C1, C2 sur les moniteurs de B seulement (`SOURCE_TEMOIN`, py l. 143).
- (f) partiel : B′ entraîne contre q* (pondération d'équilibre, py l. 1102) ; l'uniforme de A et D est une ligne (py l. 1107).
- Mesures : H, I1, I2, rétention, I3, valeur nulle et I3 − nul (`indicateurs_cycle`, py l. 1034–1053) ; V standard et renforcé (`phase_finale`) ; attaquant indépendant (`attaquant_independant`, py l. 1642–1668) ; contrôle des tours de A (`auditer_tours_A`, py l. 1671–1703).
- Configuration : `K`, `d`, `T`, `unites_Bp`, `alpha`, `tau` sont des champs de `Config` (py l. 165–218) ; toute valeur nouvelle change l'identité (Pièce 1, § Seuil).
- Jouet : OpenSpiel 2.0.2 installé dans le dépôt (`docs/notes/convergence-defense-v1/jouet-openspiel-v1/`, protocole et résultat scellés, non relus ici) ; `matrix_rps`, `matrix_mp`, `exploitability.nash_conv`, `fictitious_play` existent.

**Ce qui n'existe pas** :
- Le mélange uniforme des moniteurs de A (Ā_T, Argon l. 91 ; formalisation § 3.3) : aucun témoin sur A ; `defense_temoin` ne connaît que B et B′ comme sources ; les moniteurs de A sont gardés en mémoire (`moniteurs`, `historique`) mais non sérialisés dans les JSON : rejeu nécessaire.
- Pénalité proximale, moyenne mobile ou moyenne de poids (Argon (c)) : `objectif_detection` n'a aucun terme de distance ; `entrainer` repart de `x0 = zeros` pour m = 1 (py l. 686).
- `softmin` ou pire cas par bloc d'attaques dans l'oracle (Argon (f)) : `J = sg.mean()` sur l'ensemble concaténé (py l. 666).
- Extragradient ou gradients optimistes (Argon (d), Kimi (d)) : incompatibles avec la réinitialisation et l'attaquant global SLSQP.
- Mélange sur un portefeuille de tâches (Argon 5.2 (2)) : `resoudre_jeu` est appelé par instance dans `trajectoire`.
- m fixe pour D (Argon 5.2 (1)) : m = t + 1 codé en dur (py l. 1106) ; seul `unites_Bp` est un champ.
- Déploiement d'une moyenne sans regret (Kimi (g)) ; regret externe ; valeur de sécurité par tour hors (iii) ; bornes de chaque p_i sur P* (Kimi 5) ; marge v* − max_i min_j G_ij (Kimi 5 ; formalisation § 6) : dérivable de G (B, B′) ou de H (A, sans la colonne cible), non codée.
- Version discrétisée du jeu à réponses exactes (Kimi 3 (a), (b)) : rien de tel ; le jouet matriciel du dépôt en est le plus proche.
- Témoin « mode » de B′ et « ou » restreint au support : options déclarées pour Lazar (Pièce 1 S16, CM3-02, CM3-07), non codées.
- Loi propre autre que N(0, I) : codée en dur (`standard_normal`, `propre_entr` py l. 907).
- Garde « médiane de `poids_max_min_equilibres` ≤ 1/2 » (Argon 5.2 (3)) : la quantité est calculée par tâche ; aucune garde ni agrégat.

---

## 7. Ce que je n'ai pas pu faire

- Vérifier une source sur PDF au-delà des noms de la première page de `2412.09565v2.pdf` (dépôt, non servi) : tout contenu attribué aux articles reste RAPPORTÉ.
- Ouvrir le JSON du pilote (non servi) : les chiffres sont recoupés sur le brouillon 4 et sur la vérification Sonnet, qui les a recalculés depuis les JSON (Pièce 2 § 4).
- Exécuter un test, un jouet ou le code (hors le chargement local d'OpenSpiel pour contrôler trois noms).
- Relire les 2 244 lignes du code en entier : lues la docstring, `Config`, les racines, l'oracle du défenseur, le jeu, l'attaquant, `Contexte.entrainer`, les indicateurs, `trajectoire`, `defense_temoin`, `phase_finale`, `construire_defenses`, `attaquant_independant`, `auditer_tours_A` (environ 700 lignes) ; non lues : analyse, lecture des tables, audit complet, lancement, gardes de processus.
- Comparer les deux avis au collisionneur (non servi, non demandé).

Aucune recommandation.
