# Lecture vérifiée des avis d'Argon seul et de Kimi seul — question de convergence v3 — v1

## En-tête

- Lecteur : sous-agent neuf, modèle Claude Fable 5.1 (`claude-fable-5-1`), lignée distincte d'Argon (`gemini-4-argon`), de Kimi (`kimi-k3.1-pro`), des rédacteurs du brouillon 4 (Opus) et de sa vérification (Sonnet 5.5). Je n'ai écrit ni la question, ni les pièces, ni les avis, ni la formalisation interne, ni la lecture vérifiée de la v2.
- Date (UTC) relevée par `date -u` : lecture commencée à **2026-11-01, 16:33:14** ; écriture à **16:39:06**.
- Cadre tenu : aucun fichier existant modifié, rien scellé, rien commis, aucun appel de modèle, aucun réseau. Lu sous `donnees/` : les deux seuls fichiers nommés. Lu en plus, hors `donnees/` : la première page du PDF `docs/sources/pdf/anteriorite-P-041-v1/2412.09565v2.pdf` (empreinte `9c23a613…`, celle que les faits nomment), pour contrôler les listes d'auteurs de Bailey et collègues données par les deux avis ; ce PDF n'a été servi à aucune espèce, son contenu reste RAPPORTÉ ici. Chargement local d'OpenSpiel 2.0.2 (installé pour le jouet du dépôt) pour contrôler trois noms de fonctions. Aucune recommandation dans ce document.
- Empreintes SHA-256 recalculées par `sha256sum` :

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

Les deux manifestes portent la même question (`73900b1e…`), les mêmes faits (`580444a6…`), le même collisionneur v7 (`c9725f02…`), et l'empreinte de leur réponse, conforme aux recalculs. Argon : 97 141 jetons d'entrée, 15 904 de sortie, 199,6 s, fin `STOP`, 1,7666 dollar (plafond 3). Kimi : 93 321 d'entrée, 30 384 de sortie, 1 099,3 s, fin `stop`, 0,4905 dollar (plafond 1).

Convention : « Pièce 1 » = brouillon 4, « Pièce 2 » = vérification, « Pièce 3 » = code, « Pièce 4 » = gel v4, « Pièce 5 » = calibrage. « faits l. » = ligne du fichier des faits ; « py l. » = ligne du fichier `.py` (le code commence à faits l. 722 : py l. n = faits l. 721 + n). « Argon l. », « Kimi l. » = ligne de l'avis.

---

## A. Avis d'Argon (`gemini-4-argon`)

### A.1 Chiffres et affirmations attribués aux pièces, recoupés

« Juste » = présent et identique ; « inexact » = présent mais différent ; « absent » = introuvable dans les pièces servies.

| Affirmation d'Argon (ligne) | Pièce | Verdict |
|---|---|---|
| d = 6, K = 3, loi propre N(0, I₆), ‖μ_k⁰‖ = 4, σ = 1 ; boîte \|μ\| ≤ 5, σ ∈ [0,5 ; 1,5] ; distance = racine de la moyenne sur k ; dimension 2Kd = 36 (l. 6–8) | configuration faits l. 59–61, 95–97 ; `distance` py l. 423, `deplier` py l. 413 | juste |
| δ ∈ {1,4 ; 1,6} après recalibrage sur 48 instances (l. 9) | Pièce 5 `deltas_choisis` ; Pièce 1 résumé 2–3 | juste |
| 7 paramètres (m = 1), 63 (m = 9) ; seuil au quantile 1 − α, α = 0,01, ±0,005, n_cal = 20 000 ; T = 8 (l. 10, 21) | § Métrique faits l. 259 ; S9, S12 ; `calibrer` py l. 514 | juste |
| oracle du défenseur : τ = 0,25, n_p = 2 000, n_a = 2 001, seuil gaussien exact pour m = 1, approché pour m > 1 ; ℓ₂ = 10⁻³ dans `_logistique` seul, aucune régularisation dans `objectif_detection` (l. 15, 17, 67) | `objectif_detection` py l. 655–673 et docstring ; `_logistique` py l. 639 | juste ; lignes « 594–608 » inexactes |
| attaquant : SLSQP, n_mc = 256 (512 en finale), tri sur le taux dur, n_eval = 19 998 (l. 16) | `meilleure_reponse` py l. 815–850 | juste |
| A déploie `[(moniteurs[-1], 1.0)]` ; entraîne sur `np.full(len(attaques), 1.0 / len(attaques))` (l. 21) | py l. 1075 et 1107 | juste (contenu) ; lignes « 634 », « 655 » inexactes |
| q̄_t = (1/(t+1)) Σ_{s=0}^{t} δ_{a_s} ; a_8 pèse 1/9 (l. 21, 89) | `attaques = [ctx.cible]` py l. 1063, puis `attaques.append` py l. 1096 | juste sur le compte ; **implicite** : a_0 est la loi cible, non dit |
| V(A) 0,0816 / 0,0359 ; V(B) 0,2099 / 0,1746 ; V(D) 0,4440 / 0,3541 ; B − A +0,1283 / +0,1387 ; D − A +0,362 / +0,318 ; C3 − B +0,1935 / +0,1443 ; B − C3 −0,1935 / −0,1443 ; B − D −0,2341 / −0,1795 (l. 27, 97, 100, 131–132) | § Prédiction A, B ; Pièce 2 § 4 | juste |
| v_restreint − V : B +0,019 / +0,024 ; B′ +0,004 / +0,004 (l. 37, 95) | faits l. 184 | juste |
| I1(A) +0,0020 [−0,0029 ; +0,0069] ; −0,0005 [−0,0046 ; +0,0034] (l. 38) | § Prédiction A | juste |
| valeur nulle 617/840 ≈ 0,73452 ; I3 0,9028 / 0,9444 ; excès +0,1683 / +0,2099 (l. 39) | `valeur_nulle_I3` py l. 1014 ; § Prédiction A. Recalculé : (1/2 + 2/3 + 3/4 + 4/5 + 5/6 + 6/7)/6 = 617/840 | juste |
| I2 = moyenne de H[t,t] − H[T,t] ; « oubli ou saturation, non distingués » (l. 40, 75) | `indicateurs_cycle` py l. 1034–1053 ; § Métrique (CM3-03) | juste |
| V₁(A) ≈ 0,072 ; rétention de A 0,37 (décalage 0), 0,24 et 0,23 (décalage 1) ; plateau de D ≈ 0,40 dès le tour 4 ; C1 − A ≈ +0,108 / +0,118, C1 sur la trajectoire de B (l. 55, 87, 131) | descriptives faits l. 251 ; `SOURCE_TEMOIN` py l. 143 | juste |
| D : I3 − 0,7345 = −0,2831 / −0,3804 ; B : +0,00 / +0,02 (l. 60, 131) | § Prédiction A ; résumé 6 | juste |
| « D ainsi que B′ présentent des valeurs fortement négatives (−0,2831 et −0,3804) » (l. 90) | ces deux nombres sont ceux de D ; pour B′ le résumé 6 ne donne que « −0,23 à −0,38 » | approximatif |
| Δ(B, A) sur (ii) −0,0538 [−0,0784 ; −0,0274] ; −0,0580 [−0,0893 ; −0,0233] (l. 98) | § Prédiction A | juste |
| 511 paramètres B′ et C3′, 63 pour D ; (T+1)² évaluations de G (l. 99, 134) | § Métrique l. 259 | juste |
| `resoudre_jeu` par HiGHS ; q* avant `entrainer` ; D à t + 1 unités ; C3/C3′ « ou » standardisé, λ = 8, recalibré (l. 94, 128, 143) | py l. 744–751, 1101–1106 ; `ou_deterministe` py l. 536, `MoniteurOu` 553 | juste ; lignes « 636–653 », « 650–651 », « 654 » inexactes |
| B′ − C3′ +0,0072 [+0,0015 ; +0,0127] ; +0,0114 [+0,0072 ; +0,0160] ; dilution déclarée (l. 135) | § Prédiction A ; § N'autorise pas | juste |
| 12 puis 48 départs en `phase_finale` ; 100 départs et (1 + 12) dans `attaquant_independant` ; déclencheur 5 (l. 119, 121) | `Config` ; py l. 1152–1158, 1642–1668 ; Critères de lecture | juste ; lignes « 674–681, 880–903 » inexactes |
| poids purs 70,8 % (17/24), 58,3 % (14/24) ; pureté forcée 17/17, 14/14 ; moniteur dominant aux tours 2–4 dans 14/17 et 12/14 ; S16 = 9 (l. 172–173) | § Prédiction A ; résumé 5 ; Pièce 2 § 4 | juste |
| `poids_max_min_equilibres` minimise max_i p_i parmi les stratégies optimales (l. 173, 186) | py l. 768–788 | juste ; lignes « 500–516 » inexactes |
| B′ − D +0,0024 / +0,0042 ; mélange réel +0,0031 (n = 7) / +0,0047 (n = 10) (l. 174) | § Prédiction A, descriptives | juste |
| Bailey cité comme `2412.09565v2` au § Antériorité (l. 200) | faits l. 208 | juste |
| angle de rotation ≈ arcsin(√K δ / r_cible) (l. 58) | dérivation d'Argon | absent des pièces (déduction) |
| « FP bilatéral converge au taux O(t^{−1/2}) ou O(t^{−1/(\|M\|+\|Θ\|−2)}) » (l. 24) | — | absent ; RAPPORTÉ ; O(t^{−1/2}) douteux (§ A.3) |
| contenu des articles de Bailey, Pinot, Zou, Perez, MART (§ 2.1, § 6) | les pièces : « aucun chiffre repris » (faits l. 208) | absents des pièces ; RAPPORTÉ |

**Décompte.** 37 chiffres et affirmations rattachés aux pièces : **35 justes, 1 approximatif** (−0,2831 / −0,3804 attribués à « D ainsi que B′ »), **1 implicite** (a_0 = loi cible), **0 chiffre du pilote absent ou déformé**. Les **neuf numéros de lignes** de la Pièce 3 cités (634, 655, 650–651, 594–608, 500–516, 636–653, 654, 674–681, 880–903) sont **tous inexacts** (objets réels : py l. 1075, 1107, 1101–1102, 655–673, 768–788, 1079–1104, 1106, 1152–1158, 1642–1668) ; aucun ne désigne un objet absent ; le contenu cité est exact. Même anomalie qu'à la v2 (lecture vérifiée v2 § 1.1). Trois énoncés sont des dérivations ou des résultats de littérature absents des pièces.

### A.2 Réponse à chaque point de la question

1. **Formalisation.** Jeu écrit en entier (Θ_δ, classe M_m, gain U = taux de détection à α, bilinéaire sur les mélanges ; somme nulle en population, « quasi-nulle » en implémentation par trois découplages : seuil gaussien, oracle lissé, invariance d'échelle brisée par la logistique ; l. 4–18). A = « suivre le meneur » (Follow-The-Leader) côté défenseur contre meilleure réponse myope ; le dernier itéré ne converge que si un point selle pur existe dans la classe (l. 22–27). Métrique : l'exploitabilité unilatérale v* − V(iii) « seule certifie » ; I1 = stationnarité, I3 = anti-persistance, H et I2 = rétention ; transposables aux sondes : H, I1, I2, le cosinus des vecteurs normaux pour I3, l'écart dual sur la sous-matrice H (l. 37–46).
2. **Pourquoi ça cycle.** Incompatibilité géométrique d'un demi-espace unique (m = 1 < K = 3) → pas d'équilibre pur ; instabilité du dernier itéré de « suivre le meneur » sans terme proximal ; saturation, pas oubli (tout l'historique est rejoué) (l. 54–79). Inévitable si m < K, δ intermédiaire, déploiement pur face à un adversaire myope ; disparaît avec une classe riche (D) ou un mélange stochastique (B) (l. 56–60).
3. **Mécanismes.** (a) A cycle car l'attaquant ne joue pas le jeu fictif, la classe linéaire n'est pas convexe en fonctions, l'uniforme dilue la dernière attaque ; pas un artefact de I3 ; test : mélange uniforme des moniteurs mêmes de A en une `phase_finale` (l. 86–91). (b) B, B′ = oracle double ; prix : capacité par requête, régression sur (ii), stockage (l. 93–103). (c) pénalité proximale ou moyenne mobile : stabilise sans progresser ; test sur 8 instances (l. 105–111). (d) gradients optimistes ou extragradient : hypothèses violées ; test par 8 pas puis `phase_finale` (l. 113–125). (e) D, C3, C3′ ; prix : coût par requête, dilution par borne de l'union ; test d = 20, K = 12, m = 3 (l. 127–138). (f) pire cas sur l'historique (softmin, robustesse par groupes) dans l'oracle ; test : `softmin` dans `objectif_detection` (l. 140–148). Pas de (g).
4. **Jeu jouet.** Pile ou face apparié, pierre–feuille–ciseaux, jeu bilinéaire sur le disque ; cinq lignes avec OpenSpiel et Gambit ; acceptation : I1 = 0, I3 − 0,7345 > 0 et NashConv > 0 pour la règle de A ; NashConv → 0 pour le jeu fictif et l'oracle double (l. 154–161).
5. **Classe égale.** Diagnostic : à 9 unités un moniteur domine faiblement toutes les lignes de G dès le tour 3–4 (l. 174). Conditions : régime sous-capacitaire contrôlé (1 < m < K, D bloqué à m), mélange sur un portefeuille de sous-familles, garde : médiane de `poids_max_min_equilibres` ≤ 1/2 (l. 179–188).
6. **Transfert.** (a) Bailey : ré-entraînement itératif ne converge pas (RAPPORTÉ) ; (e) Zou 2023, Zou 2024, MacDiarmid 2024 ; (a), (b), (f) : Perez 2022, Samvelyan 2024, MART ; aucun mélange d'équilibre explicite sur sondes publié (l. 199–216). Rien pour (c), (d).

### A.3 Sources citées — toutes RAPPORTÉ (aucun PDF servi aux espèces ; R7)

Classiques, identifiants plausibles, non vérifiés : Brown 1951 ; Robinson 1951 (JSTOR 1969530) ; Shalev-Shwartz 2012 ; Lanctot 2017 (arXiv 1711.00832) ; Mertikopoulos, Papadimitriou, Piliouras 2018 (arXiv 1709.02738) ; Daskalakis et collègues 2018 (arXiv 1711.00141) ; Madry 2018 (arXiv 1706.06083, PDF présent dans le dépôt, non relu) ; McMahan, Gordon, Blum 2003 ; Izmailov 2018 (arXiv 1803.05407) ; Mertikopoulos 2019 (arXiv 1807.02629) ; Goodfellow 2013 (arXiv 1302.4389) ; Sagawa 2020 (arXiv 1911.08731) ; Bohnenblust, Karlin, Shapley 1950 ; Zou 2023 (arXiv 2310.01405) ; Zou 2024 (arXiv 2406.04313) ; MacDiarmid 2024 (note Anthropic) ; Perez 2022 (arXiv 2202.03286) ; Samvelyan 2024 (arXiv 2402.16822, PDF présent, non relu) ; Savani et Turocy 2024 (Gambit, JOSS) ; Pinot et collègues 2020 (ICML, arXiv 2002.11560).

**Suspectes ou à vérifier en priorité** :
- **Bailey et collègues 2024** (l. 200) : « Bailey, L., Serrano, E., Abeliuk, A., wagstaff, B., & Steinhardt, J. » — **liste d'auteurs fausse** : la première page du PDF du dépôt (`9c23a613…`) donne Bailey, Serrano (Alex), Sheshadri, Seleznyov, Taylor, Jenner, Hilton, Casper, Guestrin, Emmons ; Abeliuk, Wagstaff, Steinhardt n'y figurent pas. Le contenu attribué (ré-entraînement itératif qui ne converge pas, Llama-3) est absent des pièces. Même anomalie qu'à la v2.
- **OpenSpiel** (l. 164) : identifiant juste ; **liste d'auteurs suspecte** (« Timmer, Karlsson, Eccles, Rowland, Letunic, Genes, Borsa, Mandhane » ne correspondent pas aux auteurs que je connais) ; nom de jeu `matching_pennies` **inexact** : dans OpenSpiel 2.0.2, `matrix_rps` et `matrix_mp` se chargent, `matching_pennies` non ; `exploitability.nash_conv` et `fictitious_play` existent (contrôle local).
- **MART** (l. 214) : « Ge, S., zhao, C., Rd, S. » — auteurs altérés ; identifiant arXiv 2311.07689 plausible (PDF présent, non relu).
- **Korpelevich 1976, Matekon 12, 747–756** : original (Ekonomika i Matematicheskie Metody 12) et traduction Matekon confondus ; même réserve qu'à la v2.
- **Shapley 1964** cité pour « les cycles limites des dynamiques de meilleure réponse » (l. 63) : l'exemple de Shapley porte sur le jeu fictif en somme non nulle (Kimi l. 132 ; formalisation interne § 4.4) : usage à vérifier.
- **Pinot 2020** : « théorème d'impossibilité d'une défense déterministe unique » (l. 64) : énoncé à vérifier sur PDF.
- **Taux O(t^{−1/2}) du jeu fictif** (l. 24, sans source) : la formalisation interne § 4.2 rappelle (RAPPORTÉ) le contre-exemple à la conjecture de Karlin (Daskalakis et Pan 2014).
- Énoncé négatif (l. 216, « n'a pas de résultat expérimental publié ») : affirmation d'absence, non vérifiable (R8).

### A.4 Ce que l'avis ne répond pas

- Point 1 : rien sur la convention de l'écart de Nash (somme ou moitié) ; le regret externe n'est pas discuté ; « ce qu'il faudrait ajouter » se réduit à compacifier les paramètres et à remplacer les échantillons par des espérances (l. 18).
- Point 2 : « bruit » (n_mc = 256 contre n_eval = 19 998) non traité ; la dépendance temporelle du départ chaud (`departs_suppl=[attaques[-1]]`, py l. 1084) n'est pas vue ; la valeur nulle 0,7345 est dite « exacte » (l. 39) sans dire que le code brise l'échangeabilité.
- Point 3 : aucun coût en secondes (60,7 s par tâche au brouillon, non repris) ; « distillation » et « entropie » nommées, non traitées ; (g) absent.
- Point 4 : ne dit pas, pour la règle de A, laquelle des deux moyennes (défenseur, attaquant) converge ; nom de jeu inexact.
- Point 5 : la garde « médiane ≤ 1/2 » est un seuil sans justification chiffrée.
- Point 6 : rien pour (c) ni (d) sur sondes ; aucune page ni chiffre localisé ; sources altérées.
- Transversal : ne signale pas que ses numéros de lignes ne correspondent pas au fichier ; ne commente ni la réserve de S17 (« contrôle faible de la forme » du cycle, faits l. 339) ni CM4-01 ; ne dit pas que les moniteurs ne sont pas sérialisés (tout V nouveau exige un rejeu).

---

## B. Avis de Kimi (`kimi-k3.1-pro`)

### B.1 Chiffres et affirmations attribués aux pièces, recoupés

| Affirmation de Kimi (ligne) | Pièce | Verdict |
|---|---|---|
| I1 +0,0020 / −0,0005 ; I3 0,9028 / 0,9444 contre 0,7345 ; écarts +0,1683 / +0,2099 (l. 3) | § Prédiction A ; Pièce 2 § 4 ; Pièce 4 § 3 point 5 | juste |
| matrice restreinte : lignes moniteurs, colonnes attaques, programme linéaire à somme nulle (l. 28) ; schéma en cinq étapes de `trajectoire` et `phase_finale` (l. 32–38) | py l. 734–757, 1056–1127, 1145–1182 | juste |
| règle idéalisée de A : argmax de la moyenne sur H_t ; attaquant argmin contre m_t (l. 44–48) | py l. 1075, 1084, 1107 | juste ; **omission** : H_t contient la loi cible (py l. 1063) |
| attaquant = optimiseur local multi-départs ; V = plus faible des deux recherches (l. 65) | `meilleure_reponse` ; py l. 1160 | juste |
| seuil gaussien « déclaré approché » pour les non linéaires (l. 65) | docstring py l. 656–658 | juste |
| agrégation déterministe recalibrée ≠ linéaire dans les poids (l. 90) | `ou_deterministe` py l. 536–550 | juste |
| l'attaque précédente sert de départ à la recherche suivante (l. 117) | py l. 1084 | juste |
| B′ purs 17/24 puis 14/24 ; forcés 17/17 et 14/14 (l. 160) | Pièce 2 § 4 ; résumé 5 | juste |
| V(A) = 0,0359 ≈ 3,6 α ; « ne progresse pas y discrimine peu » (l. 166) | résumé 6 ; Table 5 | juste |
| v_R − V : B +0,019 / +0,024 ; B′ +0,004 / +0,004 ; pas des certificats du jeu complet (l. 209) | § N'autorise pas | juste |
| `poids_max_min_equilibres` = min sur P* de max_i p_i, P* = {p ≥ 0, Σ p = 1, Gᵀp ≥ v*} (l. 277–286) | py l. 768–788 (tolérance 10⁻⁹) | juste |
| B′ − D mélange trois effets : tirage, sélection maximin, distribution d'entraînement (l. 308) | § N'autorise pas (sélection et distribution déclarées ; le tirage est le troisième) | juste |
| A n'est pas le protocole de Bailey, déclaré par les pièces (l. 318) ; PDF non servi (l. 358) | § N'autorise pas ; docstring py l. 41 ; en-tête des faits | juste |

**Décompte.** 15 chiffres et affirmations rattachés aux pièces : **15 justes, 0 inexact, 0 absent** ; une **omission** (la loi cible dans l'historique de A). Kimi ne cite aucun numéro de ligne (fonctions nommées, toutes existantes) et ne recopie aucun chiffre qu'il ne trouve dans les pièces.

### B.2 Réponse à chaque point de la question

1. **Formalisation.** Noyau statique (moniteur ou mélange p ; θ ∈ Θ_δ ; U = probabilité de détection au seuil calibré ; −U) ; le jeu complet est un jeu extensif à politiques dépendant de l'historique dont A est une politique fixée, pas une recherche d'équilibre (l. 13–38). Sept déclarations préalables à tout théorème (objet, exactitude des réponses, départage, objet de la convergence, gain dur ou lissé, calibrage, mélanges permis ; l. 55–63). Table des régimes : Robinson ne vaut que des deux côtés ; un seul côté : aucun théorème ; continu : hypothèses à ajouter (l. 69–78). L'oracle à fausses alertes fixées : seuil dans la stratégie, gain non bilinéaire en paramètres ; surrogate ≠ gain ; réponse à l'uniforme ≠ minimax (l. 86–88). Métrique : écart de Nash (NashConv) avec sa convention ; table de sept mesures (exploitabilité, valeur de sécurité, I1, I3, distance, H, regret) et leur lisibilité sur sondes ; NashConv répond à la question théorique mais seulement sur un jeu restreint déclaré (l. 94–115) ; 0,7345 est conditionnel, le départ chaud brisant l'échangeabilité (l. 117).
2. **Pourquoi ça cycle.** Quatre phénomènes distingués ; Shapley hors de la garantie de Robinson, ne réfute pas la somme nulle finie (l. 125–132). Quatre causes à statut inégal — asymétrie (structurelle, principale), uniforme (possible, non démontré), classe linéaire (plafond, pas universel), mesure — chacune avec ce qui la réfuterait (l. 136–168). Proposition : sans équilibre pur, pas de point fixe, mais pas nécessairement un cycle périodique (récurrent, irrégulier, chaotique) ; conditions où le cycle n'est pas inévitable (l. 172–187).
3. **Mécanismes.** (a) à (g) avec condition, prix, test ; tests génériques : discrétiser en jeu fini à réponses exactes et comparer A, jeu fictif complet, autres pondérations (l. 201) ; certificat de l'oracle double puis vérification indépendante (l. 211) ; H et NashConv séparés pour (c) (l. 221) ; surrogate contre gain dur pour (d) (l. 231) ; classes emboîtées sur deux familles à équilibre connu pour (e) (l. 239) ; robustesse intérieure contre robustesse à la réponse finale pour (f) (l. 251) ; (g) déployer la moyenne d'un algorithme sans regret (l. 253–261).
4. **Jeu jouet.** OpenSpiel tel quel ; jeu fictif complet puis dynamique asymétrique avec départages consignés ; oracle double jusqu'au certificat, recoupé avec Gambit ; séparation des mesures ; répétition sous départages et erreurs contrôlées (l. 267–271).
5. **Classe égale.** Deux certificats sur G : non-dégénérescence (équilibre intérieur connu, ou programmes linéaires bornant chaque p_i sur P*) et valeur stratégique v* − max_i min_j G_ij > 0 ; locaux au jeu restreint ; le portefeuille de tâches n'est pas une garantie ; comparateurs à moniteurs, distribution, classe et calibrage identiques (l. 277–308).
6. **Transfert.** Table (a) à (g) : une seule référence directement pertinente (Bailey, PDF non servi) ; (f) : entraînement adversarial latent (Sheshadri) adjacent ; le reste « non établi par les pièces, non "jamais publié" » (l. 314–326).

### B.3 Sources citées — toutes RAPPORTÉ (aucun PDF servi ; R7)

Classiques, identifiants plausibles, non vérifiés : [1] Robinson 1951 (DOI 10.2307/1969530) ; [2] Brown 1951 ; [3] Shapley 1964 (usage conforme) ; [4] Mertikopoulos 2018 (DOI SODA non vérifié) ; [5] Daskalakis 2018 ; [6] Mokhtari, Ozdaglar, Pattathil 2020 (arXiv 1901.08511) ; [7] McMahan 2003 ; [8] Lanctot 2017 ; [9] Freund et Schapire 1999 ; [10] McCloskey et Cohen 1989 ; [11] Kirkpatrick 2017 ; [12] Izmailov 2018 ; [14] Sinha, Namkoong, Duchi 2018 (arXiv 1710.10571 ; auteur Volpi omis) ; [17] OpenSpiel (daté 2020, arXiv 2019) ; [18] McKelvey, McLennan, Turocy 2016.

**Suspectes ou à vérifier** :
- **[15] Bailey et collègues** : « Bailey, Infanger, Sheshadri, Seleznyov, Taylor, Jenner, Steinhardt, Casper, Emmons » — **partiellement fausse** (première page du PDF du dépôt : Serrano, non Infanger ; Hilton, non Steinhardt ; Guestrin manque). Kimi écrit lui-même « PDF non servi, détails à contrôler ». Le contenu attribué (« amélioration de robustesse par ré-entraînement, sans clore la généralisation ») est absent des pièces et **diverge** de celui qu'Argon attribue au même papier.
- **[16] Sheshadri 2024, arXiv 2407.15567** : le dépôt tient `2407.15549v3` ; l'un des deux identifiants est à confronter au PDF.
- **[13] absent** : la numérotation saute de [12] à [14], aucun « [13] » dans le texte (anomalie de forme).

### B.4 Ce que l'avis ne répond pas

- Point 1 : ne dit pas que l'historique de A contient la loi cible ; n'écrit pas le jeu avec ses constantes (d, K, δ, m) ni les découplages d'implémentation un à un.
- Point 2 : aucun mécanisme géométrique (pourquoi m = 1 face à K = 3) ; « sous quelles conditions inévitable » reçoit une proposition abstraite sans lien aux chiffres ; « bruit » en une phrase (l. 187).
- Point 3 : aucun « test le moins cher **dans notre jeu** » rattaché à une fonction du code ou à un bras ; les tests supposent une version discrétisée qui n'existe pas ; aucun coût chiffré.
- Point 4 : pas de prédiction pour la règle asymétrique, seulement ce qu'il faut journaliser.
- Point 5 : « borner chaque p_i » sans formule ni seuil ; pas de condition de conception (m, K) rendant l'équilibre intérieur.
- Point 6 : presque tout « non établi » ; rien de localisé.
- Transversal : ne relève pas que C1 est bâti sur les moniteurs de B, non de A ; ne commente ni la Pièce 2 ni la Pièce 5 ; ne signale pas la non-sérialisation des moniteurs.

---

## 5. Accords entre Argon et Kimi, et pistes originales de chacun

### 5.1 Accords (pistes générales consensuelles)

1. **A n'est pas le jeu fictif de Brown–Robinson** : jeu fictif d'un seul côté, attaquant myope au dernier moniteur pur ; les théorèmes ne s'appliquent pas tels quels (Argon l. 22 ; Kimi l. 5, 51, 140). Conforme au code (py l. 1075, 1084, 1107) et à la formalisation interne § 0, § 2.1.
2. **Somme nulle en population, approximations en implémentation** : gain lissé ≠ gain dur, seuil approché, optimiseurs locaux (Argon l. 14–17 ; Kimi l. 61–65, 86–87).
3. **Sans point selle pur dans la classe déployée, le dernier itéré ne peut converger** ; moyennes ≠ dernier itéré (Argon l. 25–27 ; Kimi l. 74, 127–128, 176–178).
4. **L'écart de Nash (exploitabilité) est la métrique qui répond à la question, calculable exactement sur le méta-jeu restreint seulement** ; I1 et I3 ne mesurent pas la convergence (Argon l. 37–40 ; Kimi l. 107–115 ; formalisation interne § 3).
5. **v_R − V n'est pas un certificat du jeu complet** (Argon l. 95 ; Kimi l. 209).
6. **La pureté de B′ est un plafond de classe** lié à l'existence d'un équilibre pur (dominance d'une ligne de G, Argon l. 174 ; « plafond local de classe », Kimi l. 160).
7. **Jeu jouet** : OpenSpiel tel quel, pierre–feuille–ciseaux et pile ou face apparié, jeu fictif bilatéral, règle asymétrique de A, oracle double, écart de Nash par tour, recoupement Gambit, séparation des mesures (Argon l. 157–161 ; Kimi l. 267–271).
8. **Rendre Q2 posable par des certificats calculés sur G avant de lire B′ − D**, à partir de `poids_max_min_equilibres` et d'une marge (Argon l. 186–188 ; Kimi l. 283–306).
9. **Le portefeuille de tâches ne garantit rien seul** (Argon l. 183–184, avec condition de capacité ; Kimi l. 306).
10. **(c)** stabilise ou masque sans créer de valeur (Argon l. 108 ; Kimi l. 219) ; **(d)** hypothèses convexe-concave violées, surrogate ≠ détection dure (Argon l. 117–120 ; Kimi l. 225–227) ; **(f)** ne protège que dans le support (Argon l. 145 ; Kimi l. 243).
11. **Transfert** : aucun mélange d'équilibre ou oracle double sur sondes d'activations à citer ; Bailey = analogie d'objet (Argon l. 216 ; Kimi l. 318–319).

### 5.2 Pistes originales d'Argon

- A qualifié de « suivre le meneur » contre meilleure réponse, Shalev-Shwartz 2012 pour l'instabilité sans régularisation (l. 22, 33).
- Mécanisme géométrique m = 1 < K = 3, angle ≈ arcsin(√K δ / r_cible), conditions d'inévitabilité et de disparition (l. 55–60) ; impossibilité de Pinot (l. 64).
- Test de (a) : mélange uniforme Ā_T des moniteurs **mêmes de A** en une `phase_finale` (l. 91) — mesure que la formalisation interne § 3.3 point 2 nomme aussi, originale parmi les deux espèces.
- Tests localisés dans le code : pénalité proximale ou moyenne des poids normalisés recalibrée sur `Xcal`, 8 instances (l. 109) ; `softmin` par bloc dans `objectif_detection` (l. 146) ; 8 pas d'extragradient puis `phase_finale` contre le déclencheur 5 (l. 121) ; d = 20, K = 12, m = 3 pour faire recycler D (l. 136).
- Transposition de I3 aux sondes par le cosinus des vecteurs normaux ou des centroïdes ; écart dual sur la sous-matrice H (l. 45–46).
- B′ − C3′ > 0 expliqué par la borne de l'union sur le seuil (l. 135) ; pureté expliquée par dominance faible d'une ligne de G dès le tour 3–4 (l. 174).
- Conception sous-capacitaire (1 < m < K, D bloqué) et garde « médiane ≤ 1/2 » avant gel (l. 180, 186–188) ; jeu bilinéaire sur le disque (l. 154).

### 5.3 Pistes originales de Kimi

- Jeu extensif à politiques dépendant de l'historique ; A = politique fixée (l. 38) ; sept déclarations préalables (l. 55–63).
- Convention de l'écart de Nash à déclarer (l. 103) ; **valeur de sécurité** et **regret externe** comme mesures lisibles sans connaître l'équilibre (l. 108, 113).
- Valeur nulle 0,7345 conditionnelle : le départ chaud brise l'échangeabilité (l. 117).
- Statut inégal des quatre causes, chacune avec sa réfutation (l. 136–168) ; distinction « pas de point fixe » / « cycle périodique » (l. 178).
- (e) : limitation informationnelle (distributions recouvrantes à α fixé) contre fonctionnelle — aucune capacité ne lève la première (l. 235).
- (g) déployer la moyenne d'un algorithme sans regret ; l'entropie peut masquer la pureté (l. 219, 253–261).
- Point 5 : programmes linéaires bornant chaque p_i sur P* ; marge v* − max_i min_j G_ij (la formalisation interne § 6 propose la même marge, non les bornes par coordonnée) ; comparateurs à moniteurs, distribution, classe, calibrage identiques (l. 295–308).
- « Non établi par les pièces » ≠ « jamais publié » (l. 314) ; robustesse à l'intérieur de l'ensemble contre robustesse à la réponse finale (l. 251).

---

## 6. Cohérence avec le code de l'arène (`arene_melange_v4.py`, `70c77fd5…`)

**Ce qui existe déjà** (vérifié sur le code servi) :
- (a) « meilleure réponse à l'historique » = A (`trajectoire`, py l. 1075, 1107), loi cible comprise (py l. 1063).
- (b) oracle double = B et B′ (py l. 1079–1104 ; `resoudre_jeu` py l. 734–757, HiGHS, primal et dual contrôlés) ; valeur restreinte (`valeur_jeu_restreint`, py l. 1125) ; pureté et pureté forcée (`est_pur`, `poids_max_min_equilibres`, py l. 764–788, 1120) ; agrégats `poids_max_min_moyen`, `part_purete_forcee` dans `resume_bras` (py l. 1352–1354).
- (e) classe élargie = D (t + 1 unités, py l. 1106), C3 (`ou_deterministe`), C3′ (`MoniteurOu`) ; C1, C2 sur les moniteurs de B seulement (`SOURCE_TEMOIN`, py l. 143).
- (f) partiel : B′ entraîne contre q* (py l. 1102) ; l'uniforme de A et D est une ligne (py l. 1107).
- Mesures : H, I1, I2, rétention, I3, valeur nulle (`indicateurs_cycle`, py l. 1034–1053) ; V standard et renforcé (`phase_finale`, py l. 1160) ; attaquant indépendant (py l. 1642–1668) ; contrôle des tours de A (`auditer_tours_A`, py l. 1671–1703).
- `K`, `d`, `T`, `unites_Bp`, `alpha`, `tau` : champs de `Config` (py l. 165–218) ; toute valeur nouvelle change l'identité.
- Jouet : OpenSpiel 2.0.2 installé (`jouet-openspiel-v1/`, scellé, non relu) ; `matrix_rps`, `matrix_mp`, `exploitability.nash_conv`, `fictitious_play` existent.

**Ce qui n'existe pas** :
- Mélange uniforme des moniteurs de A (Ā_T, Argon l. 91 ; formalisation § 3.3) : aucun témoin sur A ; `defense_temoin` ne connaît que B et B′ ; les moniteurs ne sont pas sérialisés : rejeu nécessaire.
- Pénalité proximale, moyenne mobile ou de poids (Argon (c)) : `objectif_detection` sans terme de distance ; `entrainer` repart de `x0 = zeros` pour m = 1 (py l. 688).
- `softmin` ou pire cas par bloc (Argon (f)) : `J = sg.mean()` sur l'ensemble concaténé (py l. 667).
- Extragradient ou gradients optimistes (Argon, Kimi (d)) : incompatibles avec la réinitialisation et l'attaquant global SLSQP.
- Mélange sur un portefeuille de tâches (Argon 5.2 (2)) : `resoudre_jeu` appelé par instance.
- m fixe pour D (Argon 5.2 (1)) : m = t + 1 codé en dur (py l. 1106) ; seul `unites_Bp` est un champ.
- Déploiement sans regret (Kimi (g)) ; regret externe ; valeur de sécurité par tour hors (iii) ; bornes de chaque p_i sur P* ; marge v* − max_i min_j G_ij (Kimi 5 ; formalisation § 6) : dérivable de G (B, B′) ou de H (A, sans colonne cible), non codée.
- Version discrétisée du jeu à réponses exactes (Kimi 3) : rien de tel ; le jouet matriciel en est le plus proche.
- Témoin « mode » de B′, « ou » restreint au support : options déclarées pour Lazar (S16, CM3-02, CM3-07), non codées.
- Loi propre autre que N(0, I) : codée en dur (`propre_entr`, py l. 906).
- Garde « médiane de `poids_max_min_equilibres` ≤ 1/2 » (Argon 5.2 (3)) : la moyenne et la part forcée sont agrégées (py l. 1352–1354), pas la médiane, et aucune garde.

---

## 7. Ce que je n'ai pas pu faire

- Vérifier une source sur PDF au-delà des noms de la première page de `2412.09565v2.pdf` (dépôt, non servi) : tout contenu attribué aux articles reste RAPPORTÉ.
- Ouvrir le JSON du pilote (non servi) : chiffres recoupés sur le brouillon 4 et sur la vérification Sonnet (Pièce 2 § 4).
- Exécuter un test, un jouet ou le code (hors le chargement local d'OpenSpiel).
- Relire les 2 244 lignes du code en entier : lues docstring, `Config`, racines, oracle du défenseur, jeu, attaquant, `Contexte.entrainer`, indicateurs, `trajectoire`, `defense_temoin`, `phase_finale`, `construire_defenses`, `attaquant_independant`, `auditer_tours_A` (≈ 700 lignes) ; non lues : analyse, lecture des tables, audit complet, lancement, gardes de processus.
- Comparer les deux avis au collisionneur (non servi, non demandé).

Aucune recommandation.
