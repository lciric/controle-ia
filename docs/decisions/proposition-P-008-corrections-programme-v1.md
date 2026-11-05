# Proposition — P-008 — corrections de trois affirmations du programme v2 — v1

Rédigée le 2026-10-06 vers 14:14 UTC par la session de mise en œuvre. Le programme ne se modifie pas par défaut (CLAUDE.md : « tu proposes, Lazar décide ») : ces corrections attendent ta décision et, si tu les retiens, une nouvelle version du programme de ta main. D'ici là, les documents de la session (note mathématique v3 de T0.3, préenregistrement de G1, papiers) emploient les formulations vérifiées ci-dessous, et le critère 8 de G0 compte ces trois affirmations comme corrigées, pas comme vérifiées.

## 1. Section 3, première précaution du lemme (A1)

- **Texte actuel** : « la notion de puissance n'est pas la même sous garantie toujours valide et au sens du test séquentiel de Wald (Koning & Grünwald, arXiv 2208.07610) ».
- **Erreurs** (lecteur neuf, `docs/sources/lecture-pdf-niveau2/rapport-lemme-v1.md`, a3c837de…, section 3) :
  - les auteurs sont Pérez-Ortiz, Lardy, de Heide et Grünwald ; « Koning » n'apparaît pas dans l'article ;
  - l'article ne compare pas deux notions de puissance. Il dit que la puissance n'est pas un critère utilisable sous garantie toujours valide et la remplace par la croissance au pire cas.
- **Formulation proposée** (reprise du rapport) : « Sous garantie toujours valide (arrêt et continuation optionnels), la puissance n'est pas un critère d'optimalité utilisable : sa définition exige une règle d'arrêt connue. Elle reste le critère des tests à taille fixe et des tests séquentiels classiques de Wald, dont la règle d'arrêt est fixée. Le critère qui la remplace est la croissance logarithmique espérée au pire cas sous l'alternative (GROW) (Pérez-Ortiz, Lardy, de Heide et Grünwald, arXiv 2208.07610v2, p. 2, 6-7 et 26). Cet article ne chiffre pas l'écart entre les deux régimes. »

## 2. Section 3, seconde précaution du lemme (A2)

- **Texte actuel** : « un adversaire couvert qui connaît la contrainte de faux positifs peut imposer un délai de détection d'ordre Θ(γ) si l'on ne contraint que la furtivité *par action* (arXiv 2601.20022) — d'où l'hypothèse (b), qui borne le budget *total* ».
- **Ce qui est exact** : le délai Θ(γ), au lieu de log γ dans le cadre classique. C'est l'optimum au pire cas au sens de Lorden : aucun détecteur ne fait mieux.
- **Ce qui est à corriger** (même rapport, section 3) :
  - γ borne un temps moyen avant fausse alarme, pas un risque α ni une garantie toujours valide ;
  - l'article ne pose aucune contrainte de furtivité par action. Son modèle est une loi après rupture stationnaire, et la furtivité en est le résultat ;
  - l'article ne traite d'aucun budget total. L'hypothèse (b) est un choix de modélisation du programme, pas une conséquence de l'article.
- **Formulation proposée** (abrégée du rapport) : « Contre un adversaire couvert qui connaît le paramètre γ de la contrainte de fausses alarmes (temps moyen avant fausse alarme au moins γ) et choisit une loi après rupture stationnaire dépendant de γ, le délai moyen de détection optimal au pire cas (critère de Lorden, atteint par la somme cumulée de Page réglée sur cette loi) est d'ordre Θ(γ), au lieu de log γ dans le cadre classique ; dans ce régime furtif, le dommage cumulé avant détection est au plus d'ordre γ^(1−ρ), soit √γ pour un décalage de moyenne (Ramtin, Nain et Towsley, arXiv 2601.20022v2, p. 3-4, 8-11). L'article ne traite ni de budget total, ni d'adversaire non stationnaire, ni de garantie toujours valide : l'hypothèse (b) du lemme est un choix de modélisation du programme. »

## 3. Section 6, environnement (a) (rappel de P-004)

- **Texte actuel** : « Base : le jeu de Terekhov et al. (arXiv 2606.08892), porté en 8 milliards de paramètres. »
- **Correction proposée** (P-004, déjà soumise) : « reconstruit » au lieu de « porté en 8 milliards de paramètres ». L'article ne publie ni code ni données.

## Enjeu

- Ces trois affirmations sont dans le document qui fait foi sur le fond.
- **Critère 8 de G0** : aucun chiffre ni aucune attribution non vérifiés dans un document du programme. Ces trois affirmations y sont corrigées, pas vérifiées.
- **Aucune hypothèse ne change.** L'hypothèse (b) reste, mais sa justification change : elle passe d'une conséquence attribuée à 2601.20022 à un choix de modélisation déclaré.

## Recommandation

Retenir les trois corrections dans une version suivante du programme (confiance haute : les deux premières reposent sur une lecture du PDF, 106 citations contrôlées, aucun échec). Pas de défaut : c'est ta décision.
