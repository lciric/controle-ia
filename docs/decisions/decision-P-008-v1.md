# Décision — P-008 : corrections de trois affirmations du programme v2 — v1

Date : 2026-10-06 (UTC).

**Décision de Lazar** : « P-008 oui » (message du 2026-10-06 vers 15:57 UTC). Consignée dans `registres/go.md` (GO-2026-10-06-03, type « revendication ») et dans `registres/decisions.md`.

**Portée.**
- Cette note fixe, à compter du GO, la lecture des trois passages ci-dessous du programme v2 (`docs/programme-controle-ia-v2.md`).
- Elle ne modifie pas le texte du programme, document qui fait foi transmis par Lazar. Une nouvelle version, s'il en transmet une, la remplacera sur ces points.
- Tout document de la session (note mathématique v3 de T0.3, préenregistrements, papiers) emploie les formulations retenues ci-dessous, avec leurs pages.

**Sources.**
- Proposition : `docs/decisions/proposition-P-008-corrections-programme-v1.md` (sha256 a8a97123…).
- Lecture sur PDF par un lecteur neuf : `docs/sources/lecture-pdf-niveau2/rapport-lemme-v1.md` (sha256 a3c837de…), section 3. Elle porte sur 106 citations, contrôlées par script, sans aucun échec.
- PDF : `docs/sources/pdf/2208.07610v2.pdf` et `docs/sources/pdf/2601.20022v2.pdf` (empreintes compagnon ; provenance `docs/sources/pdf/provenance-niveau2-lot1-v1.md`).

## 1. Section 3, première précaution du lemme

**Lecture retenue** : « Sous garantie toujours valide (arrêt et continuation optionnels), la puissance n'est pas un critère d'optimalité utilisable : sa définition exige une règle d'arrêt connue. Elle reste le critère des tests à taille fixe et des tests séquentiels classiques de Wald, dont la règle d'arrêt est fixée. Le critère qui la remplace est la croissance logarithmique espérée au pire cas sous l'alternative (GROW) (Pérez-Ortiz, Lardy, de Heide et Grünwald, arXiv 2208.07610v2, p. 2, 6-7 et 26). Cet article ne chiffre pas l'écart entre les deux régimes. »

Remplace : « (Koning & Grünwald, arXiv 2208.07610) » et « la notion de puissance n'est pas la même ».

## 2. Section 3, seconde précaution du lemme

**Lecture retenue** : « Contre un adversaire couvert qui connaît le paramètre γ de la contrainte de fausses alarmes (temps moyen avant fausse alarme au moins γ) et choisit une loi après rupture stationnaire dépendant de γ, le délai moyen de détection optimal au pire cas (critère de Lorden, atteint par la somme cumulée de Page réglée sur cette loi) est d'ordre Θ(γ), au lieu de log γ dans le cadre classique ; dans ce régime furtif, le dommage cumulé avant détection est au plus d'ordre γ^(1−ρ), soit √γ pour un décalage de moyenne (Ramtin, Nain et Towsley, arXiv 2601.20022v2, p. 3-4, 8-11). L'article ne traite ni de budget total, ni d'adversaire non stationnaire, ni de garantie toujours valide. »

Conséquence : l'hypothèse (b) du lemme (budget total borné) reste au programme, comme **choix de modélisation déclaré**. Elle n'est plus présentée comme une conséquence de cet article.

## 3. Section 6, environnement (a)

**Lecture retenue** : « Base : le jeu de Terekhov et al. (arXiv 2606.08892), reconstruit », au lieu de « porté en 8 milliards de paramètres ». L'article ne publie ni code ni données (P-004).

## 4. Ce qui ne change pas

Aucune hypothèse, aucune prédiction, aucun critère de porte. Les énoncés retenus de L et T (décision N-003, N-004) sont inchangés. Seule la justification bibliographique de deux précautions est corrigée.
