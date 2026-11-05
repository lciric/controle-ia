# Lecture de niveau 2 — lemme d'additivité : vérification sur source primaire de arXiv 2208.07610v2 et arXiv 2601.20022v2

**Date** : 2026-10-06, 14:03 temps universel coordonné.
**Lecteur** : sous-agent neuf, qui n'a rien écrit de ce qu'il vérifie. Lecture seule de `/home/user/controle-ia` : ce lecteur n'y a écrit aucun fichier et n'y a rien commité. Après lecture, les deux PDF gardent leurs empreintes et leur date (2026-10-06 13:46 temps universel coordonné).
**Dossier de travail** : `/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/lecture-niveau2-lemme/`

## En-tête : fichiers lus et empreintes

| fichier (lu en entier, annexes et références comprises) | pages | empreinte sha256 attendue | empreinte calculée le 2026-10-06 | statut |
|---|---|---|---|---|
| `docs/sources/pdf/2208.07610v2.pdf` | 31 | `e9e5fd4e0096e3be7e7b07d083fd73818791feafd69a65676c289c0f63db6223` | `e9e5fd4e0096e3be7e7b07d083fd73818791feafd69a65676c289c0f63db6223` | identique |
| `docs/sources/pdf/2601.20022v2.pdf` | 34 | `8d090f3171ef76cad597ab263a2de9df49de1d1accf78a8afff55ceb82881b42` | `8d090f3171ef76cad597ab263a2de9df49de1d1accf78a8afff55ceb82881b42` | identique |

**Méthode.** Extraction `pdftotext -layout`, une page par fichier (`extraits/<article>/page-NN.txt`) ; la page citée est le rang de la page dans le fichier PDF. Les formules clés ont en plus été lues sur le rendu image des pages (2208.07610v2 : p. 5, 6, 7, 10, 11, 12, 14, 26, 27 ; 2601.20022v2 : p. 3 à 6 et 8 à 11), car l'extraction déplace les radicaux, les fractions et les exposants. Chaque citation anglaise porte une étiquette `[Pnn, p. x]` (2208.07610v2) ou `[Rnn, p. x]` (2601.20022v2) et a été contrôlée par script contre le texte extrait (section 6). Dans une citation : ⟦…⟧ signale une formule transcrite (non comparée lettre à lettre), […] une coupure, `\|` une barre verticale échappée pour les tableaux.

**Sigles anglais présents dans les citations (laissés tels quels, puisque cités mot pour mot).** GROW : *growth-rate optimal in the worst case*, croissance optimale au pire cas ; GHK : Grünwald, de Heide et Koolen, [P59, p. 22] «Safe testing», référence interne de l'article 2208.07610 ; KL : divergence de Kullback-Leibler ; SPRT : test séquentiel du rapport des probabilités de Wald ; ADD : délai moyen de détection ; AT2FA : temps moyen avant fausse alarme ; QCD : détection de rupture la plus rapide ; CuSum : somme cumulée (procédure de Page) ; pdf : densité de probabilité ; rvs : variables aléatoires ; i.i.d. : indépendantes et de même loi.

## Verdicts

- **A1 : corrigé.** L'attribution est fausse : l'article a quatre auteurs, Pérez-Ortiz, Lardy, de Heide et Grünwald ; le nom « Koning » n'apparaît nulle part dans les 31 pages. Sur le fond, l'article ne dit pas que « la notion de puissance n'est pas la même ». Il dit que la puissance est le critère des tests à taille fixe et des tests séquentiels classiques de Wald, à règle d'arrêt fixée, mais qu'elle **n'est pas un critère d'optimalité utilisable** sous garantie toujours valide, faute de règle d'arrêt connue. Il la remplace par la croissance logarithmique espérée au pire cas (critère GROW). Il ne chiffre aucun « prix » de la garantie toujours valide.
- **A2 : corrigé.** Le résultat d'ordre Θ(γ) existe, pour le délai moyen de détection optimal au pire cas au sens de Lorden. Mais quatre points sont à corriger :
  - γ est une borne sur le **temps moyen avant fausse alarme**, et non une probabilité de faux positif ni une garantie toujours valide ;
  - l'article n'impose **aucune contrainte de furtivité par action** : l'adversaire choisit une loi après rupture stationnaire, et la furtivité est un *résultat*, n(γ) = Θ(γ), obtenu quand l'écart par observation est d'ordre 1/γ en divergence, c'est-à-dire quand γ·D(q‖qγ) reste borné, les deux divergences étant du même ordre comme dans les cas gaussien et exponentiel ;
  - l'article ne traite **aucun budget total** et ne dit pas qu'une borne de budget change le résultat ;
  - il montre en revanche que, dans ce régime, le dommage total cumulé avant détection est au plus d'ordre γ^(1−ρ) pour un dommage par observation D^ρ avec ρ ∈ (0, 1), soit √γ pour le décalage de moyenne cumulé.

  « D'où l'hypothèse (b) » est une inférence du programme, pas une conclusion de l'article.

---

## 1. arXiv 2208.07610v2 — « E-statistics, group invariance and anytime-valid testing »

### 1.1 Identité

- **Titre** : *E-statistics, group invariance and anytime-valid testing* (en capitales p. 1, [P01] ; même titre dans les métadonnées du PDF).
- **Auteurs (quatre)** : Muriel Felipe Pérez-Ortiz (Eindhoven University of Technology), Tyron Lardy (Leiden University), Rianne de Heide (Vrije Universiteit, Amsterdam), Peter D. Grünwald (Centrum Wiskunde & Informatica, Amsterdam ; aussi Mathematical Institute, Leiden University).
- **Version et date** : v2, 17 octobre 2023, catégorie arXiv math.ST, théorie statistique (tampon arXiv p. 1).
- **Revue** : en-tête [P08, p. 1] «Submitted to the Annals of Statistics». L'article est donc *soumis* à la date de la v2 ; ce fichier n'établit pas sa publication définitive, qui n'est pas vérifiée ici.
- **« Koning & Grünwald » : inexact.** Aucune occurrence de « Koning » dans le texte, les annexes ni les références (recherche sur les 31 pages extraites). Piste **non vérifiée, non opposable** (mémoire du lecteur) : N. W. Koning a publié sur les tests toujours valides par permutation et invariance de groupe (arXiv 2310.01153 ?). Si le programme visait cette source, il faut la retrouver et l'empreinter avant toute citation.

### 1.2 Table des questions 1 à 4

| # | question | verdict ou réponse | page | citation exacte |
|---|---|---|---|---|
| 1 | Titre | *E-statistics, group invariance and anytime-valid testing* | 1 | [P01, p. 1] «E-STATISTICS, GROUP INVARIANCE AND ANYTIME-VALID TESTING» |
| 1 | Auteurs | Quatre auteurs ; « Koning & Grünwald » est inexact (0 occurrence de « Koning ») | 1 | [P02, p. 1] «BY MURIEL FELIPE PÉREZ-ORTIZ⟦1,a⟧, TYRON LARDY⟦2,b⟧ RIANNE DE HEIDE⟦3,c⟧ AND PETER D. GRÜNWALD⟦4,d⟧» |
| 1 | Affiliations | Eindhoven, Leiden, Amsterdam (Vrije Universiteit), Amsterdam (Centrum Wiskunde & Informatica) | 1, 21 | [P03, p. 1] «Eindhoven University of Technology, Eindhoven, The Netherlands, ⟦a⟧ m.f.perez.ortiz@tue.nl» ; [P04, p. 1] «Leiden University, Leiden, The Netherlands, ⟦b⟧ t.d.lardy@math.leidenuniv.nl» ; [P05, p. 1] «Vrije Universiteit, Amsterdam, The Netherlands, ⟦c⟧ r.de.heide@vu.nl» ; [P06, p. 1] «Centrum Wiskunde & Informatica, Amsterdam, The Netherlands, ⟦d⟧ pdg@cwi.nl» ; [P09, p. 21] «Peter D. Grünwald is also affiliated with the Mathematical Institute of Leiden University.» |
| 1 | Version, date | v2 du 17 octobre 2023 | 1 | [P07, p. 1] «arXiv:2208.07610v2 [math.ST] 17 Oct 2023» |
| 1 | Revue | Soumis aux *Annals of Statistics* ; publication définitive non établie par ce fichier | 1 | [P08, p. 1] «Submitted to the Annals of Statistics» |
| 2 | Le test toujours valide et le test de Wald sont-ils comparés ? | Oui, qualitativement : le test toujours valide est un autre objet que le test séquentiel classique de Wald, « dans lequel la puissance a un sens » | 2 | [P10, p. 2] «we stress that, as elaborated in Appendix C, anytime-valid testing, while taking place in a sequential setting, is different from classical, Wald-style sequential testing, in which power is meaningful.» |
| 2 | La puissance sous garantie toujours valide | N'est pas une mesure d'optimalité pertinente | 2 | [P11, p. 2] «In this context, power is not a meaningful measure of optimality (see Section 2.4).» |
| 2 | Pourquoi | La puissance suppose une règle d'arrêt connue : c'est le critère à taille fixe ou, en séquentiel classique, à règle d'arrêt fixée | 6 | [P16, p. 6] «The standard optimality criterion for hypothesis tests satisfying a certain type-I error guarantee is worst-case power maximization for a fixed-sample-size or, with classic sequential tests, for a fixed stopping rule.» ; [P17, p. 6] «This criterion cannot be used when the stopping rule is unknown because knowledge of the stopping rule is required by the definition of power.» |
| 2 | Effet d'une e-statistique optimisée pour la puissance | Elle vaut zéro avec probabilité positive, donc elle est inutilisable pour la continuation optionnelle par produit | 6 | [P18, p. 6] «Additionally, an e-statistic that optimizes power at fixed stopping time will take the value zero with positive probability, making it useless for optional continuation by multiplication.» |
| 2 | Ce qui remplace la puissance | La croissance au pire cas : maximiser le pire cas, sur l'alternative, de l'espérance du logarithme de l'e-statistique | 2, 6, 7 | [P12, p. 2] «We replace power by GROW (see again below), the natural optimality criterion in this context» ; [P13, p. 2] «A natural replacement of power is the GROW criterion, which stands for growth rate optimal in the worst case.» ; [P19, p. 6] «A more sensible criterion for e-statistics under optional continuation is growth rate optimality in the worst case (GHK).» ; [P20, p. 7] «if it maximizes the worst-case expected logarithmic value under the alternative hypothesis» |
| 2 | Synonymes du critère | « puissance e maximale », critère de Kelly | 2 | [P15, p. 2] «Some other authors refer to GROW as ‘maximal e-power’ (Zhang, Ramdas and Wang, 2023) or as ‘optimizing the Kelly criterion’ (Ramdas et al., 2023).» |
| 2 | Lecture informelle de la croissance | Accumuler la preuve contre l'hypothèse nulle le plus vite possible, en taille d'échantillon | 2 | [P14, p. 2] «Informally, among all e-statistics, those that are GROW accumulate evidence against the null as fast as possible (in terms of sample size).» |
| 2 | Cas de la taille fixe | Théorème de Hunt et Stein : le max-min de puissance est atteint parmi les tests invariants | 2 | [P21, p. 2] «For fixed-sample size tests, with power as a criterion, the answer is positive: a celebrated theorem of Hunt and Stein (Lehmann and Romano, 2005, Section 8.5) shows that, when looking for a test that has max-min power, no loss is incurred by looking only among group-invariant tests.» |
| 2 | Cas du séquentiel classique | Invariance utilisée, mais aucun résultat d'optimalité connu | 2 | [P22, p. 2] «In classical sequential testing, the principle of invariance has been used (Cox, 1952; Hall, Wijsman and Ghosh, 1965), but no optimality results are known.» |
| 2 | Contribution de l'article | Un analogue du théorème de Hunt et Stein pour les tests toujours valides | 2 | [P23, p. 2] «In this article we address this question and provide an analogue of the Hunt-Stein theorem within the setting of anytime-valid tests.» |
| 2 | Différence de nature entre les deux critères | La puissance est linéaire en le test ; l'objectif de croissance ne l'est pas | 8 | [P24, p. 8] «At the core of the proof of the Hunt-Stein theorem lies the fact that the power is a linear function of the test under consideration.» ; [P25, p. 8] «This line of reasoning cannot be directly translated to our setting because of the nonlinearity of the objective function that characterizes the optimal e-statistics that we consider (see Section 2.4).» |
| 2 | Travaux séquentiels antérieurs | Comme le SPRT de Wald, ils fixent la règle d'arrêt a priori ; ils ne sont pas directement comparables au cadre toujours valide | 8 | [P26, p. 8] «most previous work (including the pioneering Rushton (1950); Cox (1952) and in fact, as far as we could ascertain, all work pre-dating Robbins (1970)) dealt, like Wald’s original SPRT, with a priori fixed stopping rules and is not directly comparable to our anytime-valid work (see Appendix C for elaboration of this point).» |
| 2 | Annexe C : ce que « décide » chaque test | Le SPRT répond « pas de décision » jusqu'à un certain n, puis 1 ou 0 pour toujours. Le test toujours valide répond à chaque instant : « si tu t'arrêtes maintenant, pour quelque raison que ce soit, rejeter est sûr » | 26 | [P27, p. 26] «We note that Wald-style—Sequential Probability Ratio Tests—tests are different because they would output "no decision" until a particular sample size n. Afterwards, they would output 1 ("reject the null") or 0 ("there is no evidence to reject the null") forever.» ; [P28, p. 26] «In contrast, in the present setting ξn = 1 means "if you stop now, for whatever reason, it is safe to reject the null".» |
| 2 | Objet de la garantie toujours valide | Contrôle de l'erreur de première espèce à distance finie, sous arrêt optionnel et sous agrégation d'expériences dépendantes | 2 | [P29, p. 2] «The main objective that is achieved by testing with e-statistics is finite-sample type-I error control in two common situations: when experiments are optionally stopped—sampling is stopped at a data-dependent sample size—, and when aggregating the evidence of interdependent experiments.» |
| 2 | Comparaison chiffrée (puissance, taille d'échantillon espérée, délai) entre test toujours valide, test de Wald et test à taille fixe | **Non trouvé.** Recherché : « power » (13 occurrences dans le corps, p. 2, 5, 6 et 8, toutes qualitatives ; 2 autres dans des titres de références ; 0 en annexe), « Wald », « SPRT », « sample size », « expected », « price », « cost ». Aucun chiffre ni aucune borne ne compare les deux régimes | — | — |
| 2 | Limite propre du critère de croissance au pire cas | Parfois trop conservateur, d'où la variante relative | 7 | [P58, p. 7] «Given its worst-case nature, the GROW e-statistic, while appropriate in some scenarios (e.g. testing exponential families with given minimum effect sizes and no nuisance parameters), is too conservative in others (GHK).» |
| 3 | A1 confirmée, à corriger, introuvable ? | **Corrigée** : formulation exacte proposée en section 3 | 2, 6–8, 26 | voir [P10], [P11], [P16]–[P20], [P26]–[P28] |
| 4 | Résultat principal | Le rapport de vraisemblance de la statistique maximalement invariante est optimal pour la croissance au pire cas, au sens absolu comme au sens relatif, et un test toujours valide peut s'y adosser | 1 | [P30, p. 1] «We show that among all e-statistics, invariant or not, the likelihood ratio of the maximally invariant statistic is GROW, both in the absolute and in the relative sense, and that an anytime-valid test can be based on it.» |
| 4 | Forme bayésienne | Facteur de Bayes avec loi a priori de Haar à droite sur le groupe | 1, 5 | [P31, p. 1] «The GROW e-statistic is equal to a Bayes factor with a right Haar prior on G.» ; [P53, p. 5] «This is known as Wijsman’s representation theorem» |
| 4 | Hypothèse clé | Groupe moyennable (vrai pour les familles position-échelle) | 1 | [P32, p. 1] «A crucial assumption on the group G is its amenability, a well-known group-theoretical condition, which holds, for instance, in scale-location families.» |
| 4 | Lien avec la divergence de Kullback-Leibler | L'e-statistique optimale est le rapport de vraisemblance des lois qui minimisent la divergence entre enveloppes convexes de l'hypothèse nulle et de l'alternative | 2 | [P33, p. 2] «Under regularity conditions, a GROW e-statistic can be found by minimizing the Kullback-Leibler (KL) divergence between the convex hull of the null and alternative models (GHK). Indeed, the likelihood ratio of the distributions that achieve this minimum KL is a GROW e-statistic.» |
| 4 | Rapport de vraisemblance simple contre simple | C'est une e-statistique | 6 | [P34, p. 6] «An example of an e-statistic is the likelihood ratio statistic in any simple-vs-simple testing problem» |
| 4 | Erreur de première espèce | Markov à instant fixé ; inégalité de Ville pour une martingale positive, uniformément dans le temps | 6 | [P35, p. 6] «The type-I error of the test that rejects the null hypothesis anytime that Tn ≥ 1/α is smaller than α, a consequence of (7) and Markov’s inequality.» ; [P36, p. 6] «The first part follows from Ville’s inequality for nonnegative martingales: the probability that there will ever be a sample size n at which Tn ≥ 1/α is bounded by α.» |
| 4 | Corollaire 3 | Le rapport de vraisemblance de toute statistique maximalement invariante est optimal pour la croissance au pire cas | 10 | [P37, p. 10] «Under the assumptions of Theorem 2, a GROW e-statistic for testing H1 against H0 as in (4) is given by the likelihood ratio of any maximally invariant statistic» |
| 4 | Théorème 4 | En cadre invariant, croissance optimale au pire cas et croissance relativement optimale coïncident ; ce n'est pas vrai en général | 10, 7 | [P38, p. 10] «Consequently, any maximizer of (8) also maximizes (10), that is, an e-statistic is GROW if and only if it is relatively GROW for the hypothesis testing problem (4).» ; [P39, p. 7] «As we will see and contrary to the general case, in the group-invariant setting, any GROW e-statistic is also relatively GROW.» ; [P40, p. 10] «This is not true in general; the result relies crucially on the invariance of the models.» |
| 4 | Proposition 6 (processus) | La suite des rapports de vraisemblance invariants est une martingale positive sous toute loi de l'hypothèse nulle | 11, 3 | [P41, p. 11] «then the process ⟦(T^{Mn})n∈N⟧ is a nonnegative martingale with respect to the filtration ⟦(σ(M1, …, Mn))n∈N⟧ under any of the elements of the null hypothesis.» ; [P54, p. 3] «As a further contribution, we show that every time that Mn is a maximal invariant the sequence ⟦T = (T^{Mn})n∈N⟧ is a nonnegative martingale. This extends its use and optimality to optional stopping.» |
| 4 | Proposition 13 | Le test « rejeter dès que T ≥ 1/α » est toujours valide au niveau α | 27 | [P46, p. 27] «The sequential test ξ is anytime valid at level α» |
| 4 | Règle d'arrêt agressive | Couverte : s'arrêter au premier n où T ≥ 1/α | 11 | [P42, p. 11] «This includes the aggressive stopping time ‘stop at the smallest n at which ⟦T^{Mn}⟧ ≥ 1/α’.» |
| 4 | Subtilité de filtration | Un temps d'arrêt fondé sur plus d'information que la filtration du processus peut détruire la propriété d'e-statistique de la valeur arrêtée (contre-exemple : espérance ≈ 1,19), sans affecter la garantie d'arrêt optionnel | 11, 27, 28 | [P43, p. 11] «if τ′ is a stopping time relative to the filtration induced by (Xn)n∈N but not relative to the coarser filtration induced by (Mn)n∈N, then ⟦T^{Mτ′}⟧ is not necessarily an e-statistic anymore.» ; [P44, p. 27] «However, using such a stopping time has no repercussions for optional stopping, since the time N in part 1 of the proposition above is not even required to be a stopping time» ; [P45, p. 28] «The above expectation is then approximately equal to 1.19, which shows that, even though ⟦T̃n⟧ is an e-statistic at each n by Corollary 9 (it is even a GROW one), ⟦T̃τ*⟧ is not an e-statistic (its expectation is 0.19 too large), providing the claimed counterexample.» |
| 4 | Cas gaussien (test de Student) | Le rapport de vraisemblance de la statistique t est optimal pour la croissance au pire cas ; même chose en unilatéral composite | 10, 12 | [P47, p. 10] «Hence, Corollary 3 implies that the likelihood ratio for the t-statistic, given in (6), is a GROW e-statistic.» ; [P48, p. 12] «Corollary 8 shows that no loss is incurred if we only look among e-statistics that are a function of the maximally invariant function Mn, the t-statistic.» |
| 4 | Mélanges | Méthode des mélanges, issue de Wald (1945) | 11 | [P49, p. 11] «This implements the method of mixtures, a standard method to combine test martingales (Wald, 1945; Darling and Robbins, 1968), which was already used in the context of the anytime-valid t-test (Lai, 1976).» |
| 4 | Loi a priori de Cauchy (test t bayésien) | Donne une e-statistique, mais la condition de moments (14) échoue | 12 | [P50, p. 12] «It is itself an e-statistic (GHK), but condition (14) of Theorem 2 does not hold because the Cauchy distribution does not have any moments.» |
| 4 | Gaussien multivarié, régression linéaire | Applications traitées en section 4 | 13 | [P51, p. 13] «We show how the theory developed in the previous sections can be applied to hypothesis testing under normality assumptions.» |
| 4 | Limite de portée | Le groupe linéaire général (test de Hotelling) n'est pas moyennable ; résultat seulement pour d = 2 | 15 | [P52, p. 15] «the general linear group GL(d), which is the relevant group in Hotelling’s test, is nonamenable.» |

### 1.3 Énoncés principaux transcrits (notation lisible ; formules vérifiées sur le rendu des pages)

- **e-statistique** (éq. (7), p. 6) : T_n = t_n(X^n) ≥ 0 et sup_{g∈G} E^P_g[T_n] ≤ 1.
- **Propriétés** (p. 6) :
  - si l'on rejette quand T_n ≥ 1/α, l'erreur de première espèce est au plus α (Markov) ;
  - le produit d'e-statistiques successives, la seconde choisie au vu de la première expérience, est une e-statistique : c'est la continuation optionnelle ;
  - si (T_n) est une martingale positive pour une filtration F, alors P(∃n : T_n ≥ 1/α) ≤ α (Ville) et T_τ est une e-statistique pour tout temps d'arrêt τ adapté à F.
- **Critère de croissance au pire cas** (éq. (8), p. 7) : T*_n maximise T_n ↦ inf_{g∈G} E^Q_g[ln T_n] sur les e-statistiques.
- **Variante relative** (éq. (10), p. 7) : maximiser inf_g { E^Q_g[ln T_n] − sup_{T'_n e-stat.} E^Q_g[ln T'_n] }.
- **Théorème 1** (repris de GHK, p. 7) :
  - Hypothèse : il existe V_n = v_n(X^n) telle que inf_{Π0,Π1} KL(Π1^g Q_g, Π0^g P_g) = min_{Π0,Π1} KL(Π1^g Q_g^{V_n}, Π0^g P_g^{V_n}) < ∞ (éq. (9)).
  - Conclusion : max_{T_n e-stat.} inf_g E^Q_g[ln T_n] = KL(Π1*^g Q_g^{V_n}, Π0*^g P_g^{V_n}).
  - Ce maximum est atteint par T*_n = ∫ q_g^{V_n}(v_n(X^n)) dΠ1*(g) / ∫ p_g^{V_n}(v_n(X^n)) dΠ0*(g).
- **Représentation de Wijsman** (éq. (5), p. 5) :
  - Formule : T^{M_n} = q^{M_n}(m_n(X^n)) / p^{M_n}(m_n(X^n)) = ∫_G q_g(X^n) dρ(g) / ∫_G p_g(X^n) dρ(g), où ρ est la mesure de Haar à droite.
  - Conditions (p. 4) : action continue et propre ; groupe σ-compact et localement compact ; densités par rapport à une mesure relativement invariante à gauche.
- **Théorème 2** (p. 10) :
  - Hypothèses : M_n maximalement invariante ; G moyennable ; Hypothèse 1 (p. 9 : espaces polonais localement compacts ; action libre, continue et propre ; modèles invariants à densités de support commun) ; il existe ε > 0 tel que E^Q_1[|ln(q_1(X^n)/p_1(X^n))|^{1+ε}] et E^{Q^{M_n}}[|ln(q^{M_n}(M_n)/p^{M_n}(M_n))|^{1+ε}] soient finis (éq. (14)).
  - Conclusion : inf_{Π0,Π1} KL(Π1^g Q_g, Π0^g P_g) = KL(Q^{M_n}, P^{M_n}).
- **Corollaire 3** (p. 10) : sous ces hypothèses, T^{M_n} est une e-statistique optimale pour la croissance au pire cas, pour tester H1 contre H0.
- **Théorème 4 et corollaire 5** (p. 10) :
  - Hypothèses : partie 3 de l'hypothèse 1, et, pour tout g, un h tel que KL(Q_g, P_h) soit fini.
  - Conclusion : g ↦ sup_{T_n} E^Q_g[ln T_n] est constante ; les deux critères (au pire cas et relatif) coïncident ; T^{M_n} est optimal pour les deux.
- **Proposition 6** (p. 11) : (T^{M_n})_n est une martingale positive pour la filtration (σ(M_1, …, M_n))_n sous toute loi de l'hypothèse nulle.
- **Proposition 13** (annexe C, p. 27) : avec ξ_n = 1{T^{M_n} ≥ 1/α} :
  - (1) pour tout temps aléatoire N, sup_{θ0} P_{θ0}(ξ_N = 1) ≤ α ;
  - (2) pour tout temps d'arrêt τ ≤ ∞ relatif à la filtration de M, sup_{θ0} E_{θ0}[T^{M_τ}] ≤ 1 (éq. (34)).
- **Annexe C.1** (p. 27–28) : test t, temps d'arrêt τ* adapté à X mais pas à M ; avec κ = 200, a ≈ 0,44 et b ≈ 1,70, l'espérance du facteur de Bayes arrêté vaut environ 1,19. La valeur arrêtée n'est donc pas une e-statistique.
- **Proposition 7, corollaires 8 et 9** (p. 11–12) :
  - pour des hypothèses composites en δ, il suffit de résoudre le problème réduit par invariance (éq. (17)) ;
  - T* = ∫ q_δ^{M_n} dΠ1*(δ) / ∫ p_δ^{M_n} dΠ0*(δ) est optimal au sens absolu et au sens relatif ;
  - avec des lois a priori fixées sur δ, le rapport (19) est optimal pour les modèles mélangés ;
  - test t unilatéral H0 : δ ≤ δ0 contre H1 : δ ≥ δ1 : l'e-statistique optimale est p^{M_n}_{δ1} / p^{M_n}_{δ0}, optimale parmi toutes les e-statistiques des données d'origine (p. 12).
- **Exemple 1, cas gaussien** (éq. (6), p. 5) :
  - Cadre : X_i indépendantes et de même loi N(μ, σ) ; on teste δ = μ/σ ; groupe des échelles (R+, ·), de mesure de Haar à droite dσ/σ.
  - Formule : T^{M_n} = ∫_{σ>0} σ^{−n} exp(−(n/2)[(X̄_n/σ − δ1)² + (1/n)Σ_i((X_i − X̄)/σ)²]) dσ/σ, divisé par la même intégrale avec δ0.
  - C'est le rapport de vraisemblance de la statistique t, optimal au sens absolu et au sens relatif (p. 10).
- **Lemme 1, gaussien multivarié** (éq. (21), p. 14) :
  - Cadre : groupe des matrices triangulaires inférieures à diagonale positive ; δ0 = 0.
  - Formule : q^{M_{S,n}}/p^{M_{S,n}} = e^{−(n/2)‖δ1‖²} ∫ e^{n⟨δ1, T A_n^{−1} M_{S,n}⟩} dP_{n,I}(T), où A_n A_n' = I + M_{S,n} M_{S,n}' et où n T T' suit une loi de Wishart W(n, I).

### 1.4 Conséquences pour le programme (2208.07610v2)

1. **Citation à corriger** : Pérez-Ortiz, Lardy, de Heide et Grünwald (arXiv 2208.07610v2, 2023, soumis aux *Annals of Statistics*), et non « Koning & Grünwald ».
2. **Ce que l'article permet d'écrire** : à horizon ou règle d'arrêt fixés, la puissance est définie ; c'est le cas du test à taille fixe et du test de Wald. Sous garantie toujours valide, la puissance n'est pas un critère utilisable, et le critère retenu est la croissance logarithmique espérée au pire cas [P11, P16–P20]. Cela s'accorde avec une distinction entre statistique terminale à n₀ fixé (puissance) et lecture toujours valide (croissance). L'article n'énonce pas cette distinction pour une somme de scores.
3. **Ce que l'article ne permet pas d'écrire** :
   - le « prix » chiffré de la garantie toujours valide : aucune comparaison quantitative ;
   - une puissance qui ne dépendrait que de B, n₀ et α ;
   - un effet du calendrier du sabotage.
4. **Outils réutilisables, avec leurs hypothèses** :
   - rapport de vraisemblance simple contre simple : c'est une e-statistique [P34] ;
   - martingale positive et inégalité de Ville donnent une garantie uniforme dans le temps [P36, P46] ;
   - réduction par invariance (application envisageable, à vérifier dans le cadre du programme) : si la loi nulle des scores comporte des paramètres de nuisance de position ou d'échelle, le rapport de vraisemblance invariant (test t et ses variantes) est optimal pour la croissance au pire cas et forme une martingale positive [P30, P37, P41, P47]. Cela vaut sous groupe moyennable, l'Hypothèse 1 et la condition de moments (14).
5. **Point d'attention tiré du texte** : si la règle d'arrêt d'un moniteur utilise plus d'information que la filtration du processus e (par exemple les données brutes alors que le processus est construit sur une réduction), la garantie « rejeter dès que T ≥ 1/α » tient toujours [P44]. En revanche, la valeur arrêtée peut cesser d'être une e-statistique [P43, P45]. Cela compte si le programme multiplie des valeurs e arrêtées d'un épisode à l'autre (continuation optionnelle).

---

## 2. arXiv 2601.20022v2 — « Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary »

### 2.1 Identité

- **Titre** : *Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary* [R01].
- **Auteurs (trois)** : Amir Reza Ramtin (University of Massachusetts Amherst), Philippe Nain (Inria, centre d'Université Côte d'Azur, Sophia Antipolis), Don Towsley (University of Massachusetts Amherst).
- **Version et date** : v2, 16 février 2026, catégorie arXiv cs.IT, théorie de l'information (tampon arXiv p. 1).
- **Lieu de publication** : **aucun indiqué dans le PDF** : ni revue, ni conférence, ni mention « submitted to ». C'est une prépublication arXiv. Le PDF cite deux travaux voisins des mêmes auteurs, non vérifiés ici : la référence [12] (conférence MILCOM 2024, *Military Communications Conference* ; adversaire non stationnaire, notion de dommage total) et la référence [14] (*IEEE Signal Processing Letters* 2025, temps continu).

### 2.2 Table des questions 5 à 8

| # | question | verdict ou réponse | page | citation exacte |
|---|---|---|---|---|
| 5 | Titre | Titre exact | 1 | [R01, p. 1] «Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary» |
| 5 | Auteurs | Ramtin, Nain, Towsley | 1 | [R02, p. 1] «Amir Reza Ramtin» ; [R03, p. 1] «Philippe Nain» ; [R04, p. 1] «Inria centre at Université Côte d’Azur» ; [R05, p. 1] «Don Towsley» ; [R06, p. 1] «University Massachusetts at Amherst» |
| 5 | Version, date, lieu | v2 du 16 février 2026, cs.IT ; aucun lieu de publication indiqué | 1 | [R07, p. 1] «arXiv:2601.20022v2 [cs.IT] 16 Feb 2026» |
| 6 | Adversaire couvert | Il connaît le paramètre γ de la contrainte de fausses alarmes et choisit une loi après rupture **stationnaire** qui dépend de γ, pour rester indétecté le plus longtemps possible | 1, 2 | [R10, p. 1] «Unlike classical formulations, we consider a covert adversary who has knowledge of the detector’s false alarm constraint parameter γ and selects a stationary post-change distribution that depends on it, seeking to remain undetected for as long as possible.» ; [R16, p. 2] «a covert adversary can deliberately choose a post-change distribution that depends on γ, causing the post-change and pre-change distributions to become increasingly similar as γ grows.» |
| 6 | γ et la contrainte de fausses alarmes | γ est une borne inférieure sur le **temps moyen avant fausse alarme** : E∞[T] ≥ γ, soit un taux de fausses alarmes au plus 1/γ. Ce n'est ni une probabilité ni une garantie uniforme dans le temps | 1, 3 | [R13, p. 1] «More precisely, the goal of the decision-maker is to make the average detection delay (ADD) as small as possible, while constraining the average time to false alarm (AT2FA) to be above some threshold.» ; [R21, p. 3] «over all stopping times T ∈ T such that E∞ [T] ≥ γ. In words, the goal is to minimize the worst-case average detection delay under a constraint on the false alarm rate (i.e., 1/E∞ [T] ≤ 1/γ).» |
| 6 | Mesure du délai | Délai moyen au **pire cas de Lorden** : supremum sur l'instant de rupture t et supremum essentiel sur le passé. n(γ) est l'**optimum sur toutes les règles d'arrêt** qui respectent la contrainte | 3 | [R22, p. 3] «Define ⟦n(γ) = inf_{T∈T: E∞[T]≥γ} d(T)⟧, the optimal worst-case average detection delay.» |
| 6 | Détecteur | Somme cumulée de Page construite avec la loi après rupture : optimale pour le critère de Lorden (Moustakides). Le détecteur est donc supposé connaître qγ | 2, 4 | [R15, p. 2] «The CuSum test is well known for its optimality under Lorden’s minimax criterion [8], which minimizes the worst-case expected detection delay subject to a false-alarm constraint.» ; [R26, p. 4] «Moustakides [9] (see also [11, Section 6.2]) showed that Page’s Cumulative Sum (CuSum) stopping rule [10]» ; [R25, p. 4] «solves Lorden’s optimization problem if h is selected so that ⟦E_{q0}[τh]⟧ = γ.» ; [R56, p. 4] «It is known that d(τh) = E_{q1} [τh] for h > 0 [11, p. 143], [15, p. 25], thereby implying that» |
| 6 | Modèle | Observations indépendantes ; loi q avant la rupture, loi qγ après ; instant de rupture inconnu mais déterministe ; après la rupture, observations indépendantes et de même loi | 3, 4 | [R23, p. 3] «Let X1, X2, . . . be mutually independent random variables (rvs) taking values in a measurable space» ; [R24, p. 3] «Random variables X1, . . . , Xt−1 have common (pre-change) probability distribution Q0 while rvs Xt, Xt+1, . . . have common (post-change) probability distribution Q1» ; [R20, p. 3] «The change time t is unknown but constant (non-Bayesian setting).» ; [R29, p. 4] «In other words, under Pqγ (resp. Pq), X1, X2, . . . are i.i.d. real-valued rvs with common pdf qγ (resp. q).» |
| 6 | Contrainte de furtivité : par pas, cumulée ? | **Ni l'une ni l'autre comme contrainte.** La furtivité est *définie comme un résultat* : n(γ) = Θ(γ). Le seul levier de l'adversaire est la loi après rupture qγ, la même à chaque pas ; son écart par observation se mesure par D(q‖qγ) et D(qγ‖q). La seule grandeur cumulée, le « dommage total », est une grandeur de sortie, pas une contrainte | 3, 4 | [R18, p. 3] «which we define as the scenario in which the best achievable ADD, under the constraint that AT2FA is at least γ, grows asymptotically as Θ(γ).» ; [R30, p. 4] «We say that an attacker is covert if n(γ) = Θ(γ), namely, for large γ, the optimal worst-case average detection delay is of the same order of magnitude as the largest admissible lower bound on the expected time between false alarms.» |
| 6 | Grandeur cumulée | Dommage total espéré jusqu'à la détection : d(γ) = n(γ)·g(D(q‖qγ)), g croissante, g(0) = 0 | 3, 4 | [R19, p. 3] «We also quantify the extent of this influence by building upon the notion of total damage introduced in [12], which measures the cumulative impact incurred prior to detection, and study its asymptotic scaling.» ; [R31, p. 4] «We model this impact through a damage measure defined as a function of the KL divergence between the pre-change and post-change models [12].» ; [R32, p. 4] «the corresponding total expected damage accrued up to the detection time is defined as» |
| 6 | Hypothèse technique | Dépassements du seuil qui s'annulent asymptotiquement, conditions (6)–(7). Prouvées seulement pour les modèles gaussien et exponentiel ; le cas général reste ouvert | 5, 8, 10, 11, 12 | [R34, p. 5] «Propositions 3.1-3.2 and Lemma 3.1 will be proved under the conditions that the expected overshoots converge to zero as γ → ∞» ; [R35, p. 8] «Condition (C) is of course very restrictive; in particular, it does not hold for the Gaussian and exponential models discussed in Section IV.» ; [R42, p. 10] «Proposition 4.1 (Gaussian pdfs): Conditions (28)-(29) are satisfied for Gaussian pdfs q and qγ defined in (44).» ; [R47, p. 11] «Proposition 4.3 (Exponential pdfs): Conditions (28)-(29) are satisfied for exponential pdfs q and qγ defined in (46).» ; [R52, p. 12] «A natural direction for future research is to identify structural properties of the pdfs qγ and q that would guarantee that sufficient conditions (28) and (29), for the vanishing of the overshoots, are automatically satisfied.» |
| 6 | Énoncé central (proposition 3.3) | Trois régimes selon la limite de γ·D(q‖qγ) (transcription en 2.3) | 8–9 | [R36, p. 8] «Proposition 3.3 (Limiting behavior of n(γ)): When conditions (6)-(7) hold,» |
| 7 | Ordre du délai | **Θ(γ), c'est-à-dire linéaire en γ**, du même ordre que le temps moyen avant fausse alarme, quand γ·D(q‖qγ) reste borné et que les deux divergences sont du même ordre. Dans les cas gaussien et exponentiel, où elles sont asymptotiquement égales : n(γ) ∼ γ·G(y)/y avec G(y)/y ∈ (0, 1) si la limite y est dans (0, ∞) ; n(γ) ∼ γ si la limite est 0. **Logarithmique**, log(γ·D(q‖qγ))/D(qγ‖q), quand γ·D(q‖qγ) → ∞. Cadre classique, loi après rupture fixe : log γ / D, c'est-à-dire O(log γ) | 1, 4, 8, 9, 11 | [R12, p. 1] «We identify the critical scaling laws governing covert behavior and derive explicit conditions under which an adversary can maintain covertness, defined by ADD = Θ(γ), whereas in the classical setting, ADD grows only as O(log γ).» ; [R37, p. 9] «The largest asymptotic order of n(γ) is reached when γD(q\|\|q0) = y + o(1) (γ → ∞), and it corresponds to covertness, i.e., n(γ) = Θ(γ).» ; [R27, p. 4] «There is in general no closed-form expression for n(γ). The behavior of n(γ) as γ → ∞ was obtained by Lorden [8], [11, Thm 6.17, p. 160].» |
| 7 | Cas gaussien | Furtif si (i) ½γ(μ² + ½σ⁴) tend vers une constante positive, ou si (ii) \|μ\|√γ → 0 et σ²√γ → 0 ; par exemple μ = γ^(−δ1), σ² = γ^(−δ2) avec δ1, δ2 ≥ ½ | 11 | [R43, p. 11] «Proposition 4.2 shows that an attacker is covert if either (i) ⟦½γ(μ² + ½σ⁴)⟧ converges to a positive constant as γ → ∞, or if (ii) \|μ\|√γ ∼γ 0 and σ²√γ ∼γ 0. Hence, covertness will occur, in particular, when (μ, σ²) = (γ^{−δ1}, γ^{−δ2}) with ⟦δ1 ≥ ½ and δ2 ≥ ½⟧.» ; [R50, p. 11] «yielding D(qγ\|\|q) ∼γ ⟦½μ² + ¼σ⁴⟧ and D(q\|\|qγ) ∼γ ⟦½μ² + ¼σ⁴⟧.» |
| 7 | Cas exponentiel | Furtif si √γ·\|1 − λγ/λ\| tend vers y ∈ [0, ∞) ; les deux divergences sont asymptotiquement égales | 11 | [R48, p. 11] «We conclude from Proposition 4.4 that an attacker is covert if √γ \|1 − λγ/λ\| ∼γ y ∈ [0, ∞).» ; [R49, p. 11] «In particular, the result that D(q\|\|qγ) ∼γ D(qγ\|\|q) gives the third asymptotic in (47).» |
| 7 | Ne pas en déduire le cas classique | La formule ne redonne pas le résultat classique, car les conditions (6)–(7) échouent quand qγ ne tend pas vers q | 2, 10 | [R53, p. 2] «In this regime, we demonstrate that the classical asymptotic result for ADD due to Lorden no longer applies.» ; [R39, p. 10] «This conclusion is however incorrect since (43) only holds if conditions (6)-(7) are met, which will clearly be not true if qγ does not depend on γ or, more specifically, if qγ does not converge to q as γ → ∞.» |
| 7 | Dommage total (proposition 3.4) | Avec g(x) = x^ρ, ρ ∈ (0, 1), et un rapport des deux divergences tendant vers c > 0 : le dommage total est maximal en ordre quand γ·D(q‖qγ) = Θ(1), et vaut alors Θ(γ^(1−ρ)). Ce régime est la frontière entre détectabilité et furtivité | 10 | [R40, p. 10] «Assume g(x) = x^ρ with ρ ∈ (0, 1) and that lim_γ D(q\|\|qγ)/D(qγ\|\|q) = c for some c > 0. Then, if conditions (6)–(7) hold, the total damage d(γ) = n(γ)g(D(q\|\|qγ)) has its largest asymptotic order when γD(q\|\|qγ) = Θ(1), with d(γ) = Θ(γ^{1−ρ}).» ; [R41, p. 10] «Note that, in the setting of the above proposition and following Proposition 3.3, the regime γD(q\|\|qγ) = Θ(1) coincides with the transition between detectability and covertness.» |
| 7 | Dommage total, cas gaussien | Avec g = √ et σ = 0, le dommage est proportionnel au **décalage de moyenne cumulé avant détection**, n(γ)·\|μ\|. Il est maximal pour μ = Θ(1/√γ) et vaut alors Θ(√γ). Même loi d'échelle que la référence [6] | 11 | [R44, p. 11] «Consequently, the total damage d(γ) = n(γ)g(D(q\|\|qγ)) is proportional to n(γ)\|μ\|, which corresponds to the total mean shift introduced by the adversary prior to detection.» ; [R45, p. 11] «Then, following Proposition 3.4, when γD(q\|\|qγ) = Θ(1), which here implies μ = Θ(1/√γ), the total damage is maximized and satisfies d(γ) = Θ(√γ).» ; [R46, p. 11] «The same scaling law was also reported in [6] for this communication setting.» |
| 8 | « Si l'on ne contraint que la furtivité par action » est-il le cadre de l'article ? | **Non.** L'article ne contraint pas l'adversaire. Il fixe un modèle — loi après rupture stationnaire, la même à chaque observation, choisie en fonction de γ — et caractérise le délai selon l'écart par observation D(q‖qγ). La non-stationnarité est explicitement laissée à la référence [12] | 1, 2, 12 | [R10, p. 1] (ci-dessus) ; [R17, p. 2] «In contrast, [12] investigates an adversarial setting against the CuSum procedure under non-stationarity, without assuming that the adversary knows the false-alarm constraint parameter, whereas in our work the post-change distribution explicitly depends on this parameter.» ; [R51, p. 12] «In this work, we developed an asymptotic framework for covert quickest change detection in discrete time, analyzing the CuSum procedure in a stationary setting where the post-change distribution qγ depends on the false-alarm constraint γ and approaches the pre-change distribution as γ → ∞.» |
| 8 | Une borne sur un budget total change-t-elle le résultat, d'après l'article ? | **Non traité (non trouvé).** Aucune contrainte de budget, aucune occurrence de « budget ». Recherché : « budget », « total » (seulement « total damage »), « per-step », « per action », « per sample », « adaptive », « non-stationary » (seulement pour décrire [12]). Seule notion proche : le dommage total d(γ), qui est une sortie et non une contrainte ; il est au plus d'ordre γ^(1−ρ), soit √γ pour le décalage de moyenne cumulé, dans le régime furtif | 4, 10, 11 | [R32, p. 4], [R40, p. 10], [R45, p. 11] (ci-dessus) |
| 8 | Garantie toujours valide, processus e, martingales | **Non trouvé** : aucune occurrence de « e-value », « e-process », « anytime », « martingale » | — | — |
| 8 | A2 confirmée, à corriger, introuvable ? | **Corrigée** : formulation exacte proposée en section 3 | 1, 3, 4, 8–11 | — |

### 2.3 Énoncés principaux transcrits (notation lisible ; formules vérifiées sur le rendu des pages)

- **Cadre** (section II, p. 3) :
  - X_1, X_2, … sont indépendantes ; X_1 … X_{t−1} suivent q ; X_t, X_{t+1}, … suivent qγ ; t est inconnu et déterministe.
  - Critère de Lorden : d(T) = sup_{t≥1} ess sup E_t[(T − t + 1)^+ | F_{t−1}].
  - Optimum : n(γ) = inf { d(T) : T temps d'arrêt, E∞[T] ≥ γ }.
- **Procédure de Page** (éq. (1), p. 4) :
  - τ_h = inf{ k ≥ 0 : max_{1≤j≤k+1} Σ_{i=j}^{k} log(q1(X_i)/q0(X_i)) ≥ h }.
  - Elle résout le problème de Lorden si E_{q0}[τ_h] = γ (Moustakides). Alors n(γ) = E_{q1}[τ_{h*}] (éq. (2)).
- **Lorden, cadre classique** (éq. (3), p. 4) : n(γ) ∼ log γ / D(q1‖q0) quand γ → ∞, pour une loi après rupture fixe.
- **Notation** (p. 4) : « f ∼x g » est défini comme f = g + o(1) (voir réserve 4) [R57, p. 4] «The shorthands f(x) ∼x g(x) and limx f(x) will stand for f(x) = g(x) + o(1) (x → ∞) and limx→∞ f(x), respectively.»
- **Furtivité** (p. 4) : l'attaquant est dit furtif si n(γ) = Θ(γ).
- **Dommage total** (éq. (4), p. 4) : d(γ) = n(γ)·g(D(q‖qγ)), g strictement croissante, g(0) = 0.
- **Hypothèse** (p. 5) : dépassements espérés du seuil qui tendent vers 0, conditions (6)–(7). Conditions suffisantes : lemme 3.2 (p. 7), conditions (28)–(29).
- **Proposition 3.2** (p. 6) :
  - E_{qγ}[τ_h] ∼ (e^{−h} + h − 1)/D(qγ‖q) ;
  - E_q[τ_h] ∼ (e^{h} − h − 1)/D(q‖qγ) ;
  - ce sont les approximations de Khan, rendues exactes asymptotiquement dans ce régime.
- **Proposition 3.3** (p. 8–9) : sous (6)–(7), selon la limite de γ·D(q‖qγ) :

  | régime | n(γ) ∼ |
  |---|---|
  | lim γ·D(q‖qγ) = ∞ | log(γ·D(q‖qγ)) / D(qγ‖q) |
  | lim γ·D(q‖qγ) = y ∈ (0, ∞) | [γ·D(q‖qγ) / D(qγ‖q)] · G(y)/y |
  | lim γ·D(q‖qγ) = 0 | γ·D(q‖qγ) / D(qγ‖q) |

  avec G(y) = e^{1+y+W_{−1}(−e^{−1−y})} − W_{−1}(−e^{−1−y}) − y − 2 (éq. (37)), où W_{−1} est la branche inférieure de la fonction de Lambert. G(y)/y ∈ (0, 1), G(y)/y → 1 quand y → 0 et G(y)/y → 0 quand y → ∞.
- **Corollaire 3.1** (p. 9) : l'ordre maximal de n(γ) est atteint quand γ·D(q‖q0) = y + o(1), et il correspond à la furtivité, n(γ) = Θ(γ). « q0 » est probablement une coquille pour qγ : voir réserve 3.
- **Remarque 3.2** (p. 9) : le seuil optimal h*(γ) vaut, selon les trois régimes ci-dessus, log(γ·D) ; −1 − y − W_{−1}(−e^{−1−y}) ; √(2γ·D).
- **Proposition 3.4** (p. 10) :
  - Hypothèses : g(x) = x^ρ, ρ ∈ (0, 1) ; D(q‖qγ)/D(qγ‖q) → c > 0 ; conditions (6)–(7).
  - Conclusion : d(γ) atteint son ordre maximal quand γ·D(q‖qγ) = Θ(1), et vaut alors Θ(γ^{1−ρ}).
  - Dans les deux autres régimes, d(γ) = o(γ^{1−ρ}).
- **Proposition 4.2, cas gaussien** (p. 11) :
  - Lois : q = N(0, 1) ; qγ = N(μ, 1 + σ²), μ et σ tendant vers 0. Asymptotiquement, D(qγ‖q) ∼ D(q‖qγ) ∼ ½μ² + ¼σ⁴.

  | régime | n(γ) ∼ |
  |---|---|
  | \|μ\|√γ → ∞ ou σ²√γ → ∞ | log(γ(μ²/2 + σ⁴/4)) / (½μ² + ¼σ⁴) |
  | ½γ(μ² + ½σ⁴) → y ∈ (0, ∞) | γ·G(y)/y |
  | \|μ\|√γ → 0 et σ²√γ → 0 | γ |

- **Proposition 4.4, cas exponentiel** (p. 11) : q de paramètre λ, qγ de paramètre λγ → λ. Mêmes trois régimes selon √γ·|1 − λγ/λ| ; furtif si cette quantité tend vers y ∈ [0, ∞), par exemple λγ = λ(1 ± γ^{−δ}) avec δ ≥ ½.

### 2.4 Conséquences pour le programme (2601.20022v2)

1. **Ce qui est établi, dans ce cadre** : contre un adversaire qui connaît γ et dilue son effet par observation à l'ordre 1/γ en divergence, soit 1/√γ en décalage de moyenne gaussien (les deux divergences restant du même ordre), le *meilleur* détecteur ne fait pas mieux qu'un délai d'ordre γ. Ce détecteur respecte un temps moyen avant fausse alarme ≥ γ, connaît la loi d'attaque et minimise le délai au pire cas de Lorden. Il est donc de l'ordre du temps entre deux fausses alarmes [R30, R37, R43].
2. **Ce que l'adversaire paie** : dans ce même régime, l'effet cumulé avant détection est borné. Le dommage total est au plus Θ(γ^(1−ρ)) pour g(D) = D^ρ, soit Θ(√γ) pour le décalage de moyenne cumulé [R40, R44, R45]. L'article situe ce maximum du dommage à la frontière entre détectabilité et furtivité [R41]. C'est un résultat, non une contrainte posée sur l'adversaire.
3. **Ce que l'article ne couvre pas** :
   - garantie de fausses alarmes en probabilité ou toujours valide, au sens de Ville ;
   - adversaire non stationnaire ou adaptatif, qui dose son effet dans le temps ;
   - contrainte de budget total ;
   - détecteur qui ne connaît pas la loi d'attaque ;
   - plusieurs flux ;
   - détecteurs fondés sur des processus e.

   Toute transposition de « Θ(γ) » au cadre du programme (risque α toujours valide, budget B, n₀) est une **inférence du programme** à justifier, pas un résultat de cette source.

---

## 3. Verdicts sur A1 et A2, avec formulations proposées

### A1 — « la notion de puissance n'est pas la même sous garantie toujours valide et au sens du test séquentiel de Wald (Koning & Grünwald, arXiv 2208.07610) »

**Verdict : corrigé.** Deux erreurs :

- les auteurs sont faux ;
- la nuance de fond est déformée : l'article ne compare pas deux « notions de puissance » ; il dit que la puissance n'est pas un critère utilisable sous garantie toujours valide et la remplace par la croissance au pire cas.

**Formulation exacte proposée** :

> Sous garantie toujours valide (arrêt et continuation optionnels), la puissance n'est pas un critère d'optimalité utilisable : sa définition exige une règle d'arrêt connue. Elle reste le critère des tests à taille fixe et des tests séquentiels classiques de Wald, dont la règle d'arrêt est fixée. Le critère qui la remplace est la croissance logarithmique espérée au pire cas sous l'alternative, appelée GROW (Pérez-Ortiz, Lardy, de Heide et Grünwald, arXiv 2208.07610v2, p. 2 et p. 6–7 ; annexe C, p. 26). Cet article ne chiffre pas l'écart entre les deux régimes.

Appuis : [P10, p. 2], [P11, p. 2], [P16, p. 6], [P17, p. 6], [P18, p. 6], [P19, p. 6], [P20, p. 7], [P26, p. 8], [P27, p. 26], [P28, p. 26].

### A2 — « un adversaire couvert qui connaît la contrainte de faux positifs peut imposer un délai de détection d'ordre Θ(γ) si l'on ne contraint que la furtivité par action (arXiv 2601.20022) — d'où l'hypothèse (b), qui borne le budget total »

**Verdict : corrigé.** Le noyau est exact : un adversaire couvert qui connaît γ obtient un délai Θ(γ). Quatre points sont à corriger :

1. γ borne un temps moyen avant fausse alarme, pas un risque de faux positif α ;
2. le délai est l'optimum au pire cas de Lorden : aucun détecteur qui respecte la contrainte ne fait mieux, pas même la somme cumulée de Page réglée sur la loi d'attaque, qui l'atteint ;
3. il n'y a pas de « contrainte de furtivité par action » dans l'article, mais un modèle stationnaire dont la furtivité est le résultat ;
4. l'article ne dit rien d'un budget total ; « d'où l'hypothèse (b) » n'en découle pas.

**Formulation exacte proposée** :

> On considère un adversaire couvert qui connaît le paramètre γ de la contrainte de fausses alarmes — un temps moyen avant fausse alarme au moins égal à γ — et qui choisit une loi après rupture stationnaire qγ dépendant de γ. Contre lui, le délai moyen de détection optimal au pire cas (critère de Lorden, atteint par la somme cumulée de Page réglée sur qγ) est d'ordre Θ(γ) dès que γ·D(q‖qγ) reste borné et que les deux divergences D(q‖qγ) et D(qγ‖q) sont du même ordre. Dans le cadre classique, il serait d'ordre log γ / D. Dans les cas gaussien et exponentiel traités, les deux divergences sont asymptotiquement égales, et la condition revient à un écart de paramètre d'ordre γ^(−1/2) au plus (moyenne μ, σ² pour la variance, écart relatif du taux exponentiel). Dans ce régime, le dommage total cumulé avant détection est au plus d'ordre γ^(1−ρ) pour un dommage par observation g(D) = D^ρ avec ρ ∈ (0, 1), soit √γ pour le décalage de moyenne cumulé (Ramtin, Nain et Towsley, arXiv 2601.20022v2 : définitions p. 3–4, proposition 3.3 et corollaire 3.1 p. 8–9, proposition 3.4 p. 10, propositions 4.2 et 4.4 p. 11). L'article ne traite ni de contrainte de budget total, ni d'adversaire non stationnaire, ni de garantie de fausses alarmes en probabilité ou toujours valide. L'hypothèse (b) du programme est un choix de modélisation du programme, non une conséquence de cet article.

Appuis : [R10, p. 1], [R12, p. 1], [R21, p. 3], [R22, p. 3], [R30, p. 4], [R37, p. 9], [R40, p. 10], [R43, p. 11], [R45, p. 11], [R48, p. 11], [R51, p. 12].

---

## 4. Question 9 — ce que ces deux sources impliquent pour le lemme

### Déjà publié dans ces deux sources

- **Garantie toujours valide par martingale positive.**
  - Le rapport de vraisemblance simple contre simple est une e-statistique [P34].
  - Une martingale positive d'espérance 1 donne, par l'inégalité de Ville, P(∃n : T_n ≥ 1/α) ≤ α [P36], ce qui fonde un test toujours valide [P46].
  - La valeur arrêtée reste une e-statistique pour tout temps d'arrêt de la bonne filtration, mais pas forcément pour un temps d'arrêt d'une filtration plus fine [P43–P45].
- **Critère d'optimalité en lecture toujours valide.**
  - La puissance n'y est pas utilisable [P11, P17] ; la croissance logarithmique espérée au pire cas la remplace [P13, P19, P20].
  - Elle s'obtient par minimisation de la divergence de Kullback-Leibler entre enveloppes convexes [P33].
  - En cadre invariant, le rapport de vraisemblance invariant est optimal, au sens absolu comme au sens relatif [P30, P37, P38]. Cas gaussien : test t [P47, P48].
- **Détection de rupture contre un adversaire couvert** (temps moyen avant fausse alarme ≥ γ, critère de Lorden, loi après rupture stationnaire) :
  - délai optimal d'ordre Θ(γ) quand γ·D(q‖qγ) reste borné, les deux divergences étant du même ordre ; logarithmique sinon [R12, R37, R43] ;
  - dommage total avant détection au plus d'ordre γ^(1−ρ) pour g(D) = D^ρ, soit √γ pour le décalage de moyenne cumulé [R40, R45] ;
  - optimalité de la somme cumulée de Page pour ce critère [R15, R26].

### Non publié dans ces deux sources (recherché, non trouvé)

- Une puissance de la statistique terminale d'une somme de scores qui ne dépendrait que de B, n₀ et α. Aucune somme de scores, aucun budget, dans l'une ou l'autre source.
- Un effet du calendrier du sabotage sur un processus e (« avancer aide le défenseur, reporter aide l'attaquant ») :
  - 2208.07610 ne traite pas d'alternatives non identiquement distribuées dans le temps : ses observations sont des copies indépendantes d'une même variable, [P60, p. 3] «and X^n := (X1, . . . , Xn) for n independent copies of X under the distributions that are to be considered.» ;
  - 2601.20022 suppose une loi après rupture stationnaire et prend le pire cas sur l'instant de rupture.
- Un chiffrage du « prix » de la garantie toujours valide face à Wald ou à la taille fixe. 2208.07610 n'en donne qu'une distinction qualitative.
- Une analyse sous contrainte de budget total, ou contre un adversaire non stationnaire ou adaptatif. 2601.20022 renvoie la non-stationnarité à sa référence [12], non vérifiée ici.
- Des détecteurs de rupture fondés sur des processus e, un seuil de dommage, ou la *nécessité* d'un détecteur de rupture pour alarmer avant un seuil de dommage. 2601.20022 n'utilise que la somme cumulée de Page et ne fixe aucun seuil de dommage.
- Le passage d'une contrainte en temps moyen avant fausse alarme (γ) à une contrainte en probabilité toujours valide (α).

### Énoncés du programme qui s'appuient sur A1 et A2

| énoncé du programme | appui dans ces sources |
|---|---|
| puissance de la statistique terminale fonction de B, n₀ et α seulement | aucun |
| en lecture toujours valide, le calendrier compte | aucun |
| « prix » de la garantie toujours valide chiffré | aucun : 2208.07610 donne seulement la distinction qualitative, ce chiffrage serait une contribution du programme |
| un détecteur de rupture (Page, détecteurs e) est nécessaire avant un seuil de dommage | partiel : optimalité de Page pour le critère de Lorden [R15, R26] et notion de dommage total avant détection [R19, R32] ; rien sur les détecteurs e ni sur la nécessité |

---

## 5. Réserves

1. **Formules.** L'extraction texte déplace radicaux, fractions et exposants : par exemple « ½ » est extrait « 12 » ou « 21 », et « √γ » est extrait « γ » avec un « √ » sur la ligne voisine. Toutes les formules transcrites aux sections 1.3 et 2.3 ont été relues sur le rendu image des pages citées. Le script ne peut pas contrôler les signes radicaux (section 6) ; les ordres en √γ (2601.20022v2 p. 11) ont été vérifiés visuellement.
2. **Statut de publication.** 2208.07610v2 est « soumis » d'après son en-tête. 2601.20022v2 n'indique aucun lieu de publication. Ni l'une ni l'autre publication définitive n'est vérifiée ici.
3. **Corollaire 3.1 de 2601.20022v2 (p. 9).**
   - Il écrit γD(q‖q0) ; je le lis comme γD(q‖qγ), puisque q0 = q dans les notations de la section III, [R58, p. 4] «For simplicity, q0 is denoted by q.», et que D(q‖q) = 0. La lecture est cohérente avec la proposition 3.3, la remarque 3.2 et la proposition 3.4.
   - Pris à la lettre, il situe l'ordre maximal au régime où γ·D tend vers une constante positive. Or la proposition 3.3 donne aussi Θ(γ) quand γ·D → 0 si le rapport des deux divergences reste borné ; l'article compte d'ailleurs les deux régimes comme furtifs dans les cas gaussien et exponentiel (p. 11).
   - Ma formule « Θ(γ) dès que γ·D(q‖qγ) reste borné » combine donc la proposition 3.3 et les cas traités ; ce n'est pas un énoncé unique de l'article en toute généralité.
4. **Notation ∼γ de 2601.20022v2.** Elle est définie p. 4 comme f = g + o(1), un écart additif [R57]. Les preuves procèdent par limite de rapport égale à 1 (par exemple éq. (27), p. 7). J'ai lu ∼γ comme une équivalence en rapport.
5. **Hypothèses des résultats de 2601.20022v2.** Ils sont asymptotiques (γ → ∞) et conditionnels aux dépassements évanescents (6)–(7). Ces conditions ne sont prouvées que pour les modèles gaussien et exponentiel ; le cas général est laissé ouvert (p. 12).
6. **Piste « Koning ».** Signalée en 1.1 de mémoire, non vérifiée et non opposable.

---

## 6. Contrôle des citations

- **Script** : `verifier_citations.py`, dans le dossier de travail (sha256 `6e7ec3e706e31a1cbb9d2aba12f35bbbfafe03daf2d023cd535b8361ce3afb32`). Il lit les citations étiquetées directement dans ce rapport, puis les compare au texte extrait de la page citée.
  - Tolérances : normalisation Unicode NFKC ; tirets et guillemets unifiés ; césures de fin de ligne ; espaces ; caractères ^ { } _ des exposants et indices transcrits ; signe radical.
  - Une formule ⟦…⟧ n'est pas comparée lettre à lettre. L'écart qu'elle couvre est borné (2 × longueur + 25 caractères) et affiché. Le contrôle échoue si cet écart contient un mot de trois lettres ou plus absent de la transcription.
  - Une citation non retrouvée sur sa page est cherchée sur les autres pages.
- **Garde testée sur des cas sains et sur des artefacts** (`tests-garde/`) :
  - 5 cas sains passent ;
  - 6 artefacts échouent : mot altéré, mauvaise page (retrouvée p. 2), chiffre altéré, négation masquée par une formule, mot masqué, phrase masquée hors borne ;
  - le conflit d'identifiant est détecté ; code de sortie 1.
- **Résultat sur ce rapport** : 106 citations distinctes contrôlées (57 de 2208.07610v2, 49 de 2601.20022v2), 106 retrouvées sur la page citée, **0 échec** ; aucun conflit d'identifiant ; code de sortie 0. Le détail figure dans `controle-citations.txt`, qui liste aussi le texte extrait que remplace chaque formule transcrite.
- **Limite** : le signe radical est ignoré par le script, donc une confusion entre Θ(γ) et Θ(√γ) ne serait pas détectée par lui. Ces ordres ont été vérifiés sur le rendu des pages (réserve 1).
- **Empreintes** : celles du script, de la sortie du contrôle et des fichiers de test sont dans `empreintes.txt` ; celle de ce rapport est dans `rapport.md.sha256`.
