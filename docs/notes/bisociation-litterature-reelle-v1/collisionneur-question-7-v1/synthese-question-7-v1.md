# Synthèse — question 7 : l'allumage comme ensemble autocatalytique de fiches — v1

Lecteur neuf, 31 octobre 2026. Pièces lues : la question servie, `faits-question-7-v1.md`, `etat.md`, `question-etage3.md`, les neuf cellules (A Fable 5.1, B Opus 4.6, C Argon ; D Kimi absent aux trois tours, absences acceptées par l'arbitre). Les cellules sont RAPPORTÉ ; rien ici n'est empirique. Les faits servis ne contiennent aucune réponse de conv-audit à la question 7 elle-même (seulement la question 3, sa réponse, la réponse d'Argon et sa lecture) ; l'hypothèse attaquée est celle du fichier de question.

## Verdict

Les trois espèces réfutent, au niveau logique et de façon convergente, la transposition telle que conv-audit l'énonce : sur le journal d'une course (graphe orienté sans cycle), la « fermeture autocatalytique » calculée sur les fiches citées est vraie par construction et se réduit à la composante atteignable depuis le corpus ; le taux de reproduction brut (R0 ou R_endo) est fixé par la dose que l'expérimentateur choisit. Les conceptions A et B ont commis ces erreurs et les reconnaissent au tour III.3. Ce qui reste testable : une **catalyse nécessaire** (ablation avec remplacement iso-longueur, seconde famille de modèles) et **endogène** (catalyseur produit par le lot, pas par le corpus). Les trois convergent sur la même première expérience, une porte instrumentale en génération 1 (15 à 35 USD illustratifs), avant toute grille de dose. La fertilité comme « contribution à la fermeture » est jugée fuyante ou dégénérée par tous. Le critère de mort de l'arbitre (« aucun lot ne s'entretient quelle que soit la dose ») est jugé insuffisant par les trois : critères étagés, et mort de l'hypothèse distincte de la mort du bisociateur.

## (a) L'analogie tient-elle, où casse-t-elle ?

- **A** (E3-T1-A §1–2) : huit présupposés ; cassure principale « pas de catalyse définie (P1) : sans catalyse, le RAF dégénère en atteignabilité, c'est-à-dire en la composante géante de Bettencourt » ; puis pas de disparition, pas de stœchiométrie, substrat ouvert. Antériorité contre P5 : auto-entretien ≠ évolutivité (Vasas et al. 2010, SUPPOSÉ).
- **B** (E3-T1-B) : trois ruptures : non-consommation, stœchiométrie absente, **goulot du jugement** (« le taux de catalyse dépend du budget de vérification, pas de la structure du lot ») ; « bon générateur d'hypothèses, mauvais modèle littéral ».
- **C** (E3-T1-C I.1) : réparation la plus forte : séparer formellement réactifs (fiches problèmes) et catalyseur (fiche opérateur, lemme, protocole) ; la littérature rapportée (Uzzi, Guimerà, Derex-Boyd) parle de cloche, pas de seuil.

Accord des trois, renforcé par les critiques : la clôture sur un graphe de génération est triviale (E3-T2-A, B-a1 : « dégénéré à 1 » ; E3-T2-C sur B : « soit identiquement 1, soit identiquement 0 par construction topologique » ; E3-T2-C sur A, 1 : « tautologiquement équivalent à avoir un degré entrant de catalyse ≥ 1 à chaque pas »). A l'accepte (E3-T3-A, C-a1 : « ma conception initiale confondait fermeture et autocatalyse »), B aussi (E3-T3-B, B-a1, C-1). Réserve de A : un RAF n'exige pas de cycle temporel ; ce qui compte est la **nécessité** et l'**origine** du catalyseur.

Apports d'une seule espèce : B, la distinction mort de l'hypothèse / mort du bisociateur, reprise par A et C ; C, la contrainte de catalyse endogène (α), reprise par A et B.

## (b) Définition opérationnelle mesurable sur le journal

Versions initiales, toutes refondues : A1 de A (RAF après gel, ≥ 1 fiche non-doublon par génération pendant k = 3) ; B (clôture + survie + R0 filtré > 1, sans catalyse) ; e-RAF de C (catalyse déclarée par le prompt, α ≥ 0,5, R_endo ≥ 1). Versions corrigées (tour III.3), convergentes :
- **A** (E3-T3-A §2, A1') : après gel, ≥ 1 fiche survivante non-doublon par génération pendant k générations, **et** fraction de fusions à catalyseur nécessaire endogène supérieure à celle du bras « corpus × corpus », **et** échec des bras perroquet et aléatoire. Le RAF de Hordijk-Steel n'est calculé que sur les arêtes de catalyse nécessaire, comme description.
- **B** (E3-T3-B) : ≥ s_min fiches survivantes après sevrage, ≥ α_min = 0,3 (illustratif) des fusions survivantes avec un catalyseur ablatif produit par le lot, et R0 excédentaire > 0 par rapport à l'espérance sous appariement uniforme à même dose. « La condition 2 est la seule qui teste l'hypothèse autocatalytique au sens strict. »
- **C** (E3-T3-C) : arêtes admises seulement si le catalyseur passe l'ablation différentielle ; multiplicateur R̃_endo = survie à g = 2 avec catalyseur de X_1 / survie avec catalyseur du corpus ou nul ; excès de clôture ΔP_e-RAF contre 1 000 permutations à degrés et verdicts conservés.

Accord : tout seuil sur R0 ou R_endo s'exprime en écart à son espérance sous appariement aléatoire à dose égale (E3-T2-A, B-a3 et C-a2 ; E3-T2-C sur B, 4 : « R0 ≈ 2·δ·p_survie » ; accepté en III.3 par B et C) ; la permutation à degrés conservés appliquée à R0 a une puissance nulle (E3-T2-C sur B, b3).

**Fertilité d'une paire.** Toutes les versions par knock-out de fermeture tombent : fuite temporelle (E3-T2-C sur A, point 3 : « le prédicteur contient algébriquement la variable cible ») ou masse de Dirac en 0 au-delà de 90 % hors du seuil de percolation (E3-T2-C sur B, b1). A accepte et rétrograde en description a posteriori ; sa version prospective (E3-T3-A, duel 4') : rôle catalytique nécessaire à g+1 comme prédicteur des descendants à g+2 et g+3, métriques de décile supérieur et log-vraisemblance (sur critique de B). B conclut : « il n'existe pas de définition opérationnelle satisfaisante de la fertilité comme contribution à un RAF » (E3-T3-B, non établi 3). C remplace par une intervention randomisée intra-course (duel 2 corrigé).

Désaccord résiduel A/B sur un signe : B (E3-T3-B, étapes 4–6) lit « chute seulement face à une fiche hors lot, pas face à une fiche aléatoire du lot » comme favorable à l'autocatalyse, et la chute dans les deux cas comme « structure locale, pas de fermeture globale » ; A (E3-T3-A, C-a2) lit la chute face à une fiche **appariée en pertinence** comme la catalyse même, et l'absence de spécificité comme « contexte pertinent générique », donc non-catalyse. Un RAF exige des catalyseurs spécifiques ; la lecture de B paraît inversée. À trancher au préenregistrement.

## (c) Prédiction chiffrée et critère de mort pour la génération 2

Chiffres illustratifs selon leurs auteurs.
- **A** : bascule attendue « à une ou deux catalyses nécessaires endogènes par fiche survivante et par génération, pas à des dizaines » (Mossel-Steel 2005, SUPPOSÉ) ; réfutée si la fraction endogène nécessaire reste < 0,1 par fiche dans des lots qui s'entretiennent. Critères étagés : Mort 0 (porte : κ < κ_min sur une famille), Mort 1 (celle de l'arbitre), Mort 2 (entretien sans chute à l'ablation → branchement), Mort 3 (artefact de paraphrase ou de seuil de doublon) ; non-jugeabilité si σ̂ hors [0,3 ; 3].
- **B** : H_A si Δ_k (survie bras réel − bras à catalyseur remplacé iso-longueur) > 0 significatif pour 2 des 3 générations après gel **et** R0 excédentaire > 0. Mort de l'hypothèse : condition 2 jamais remplie sur 3 générations. Mort du bisociateur : survie inter-niches ≤ survie d'une réflexion profonde intra-niche, mêmes juges, même budget.
- **C** : au-dessus d'une dose M_c, R̃_endo(g = 2) ≥ 1,25 maintenu à g = 3, p < 0,01, signal disparaissant sous permutation des verdicts ; mort si R̃_endo ≤ 1,05 à toute dose ou ΔP_e-RAF ≤ 0,15 sur toute la grille.

Accord : le critère de l'arbitre est trop grossier (B : « trop sévère » ; A : « deux critères plus probables que celui de l'arbitre »). Accord de puissance : n = 10 lots par dose ne sépare rien (E3-T2-C sur A, b2 : puissance < 0,35 au seuil Δ = 0,2 ; E3-T2-A sur C : « le plan est biaisé vers la mort ») ; le critère de mort initial de C se déclenchait par construction (R_endo ≈ 0,5 < 0,8), accepté par C.

Désaccord : garder ou non un duel de dose en génération 2. C le garde corrigé (6 niveaux, 15 courses par niveau) ; A le rétrograde en exploratoire vers la question 3 ; B le supprime au profit d'un unique duel de sevrage.

## (d) Antériorités

Toutes SUPPOSÉ (attribution de mémoire), sauf mention ; R7 avant tout usage.
- Déjà dans les pièces : Bettencourt et al. 2006, 2008, 2009, 2015 (existence vérifiée, contenu SUPPOSÉ) ; Tria et al. 2014 (notice vérifiée) ; Kauffman, Hordijk-Steel, Arthur 2009, Weitzman 1998 (SUPPOSÉ) ; Uzzi 2013, Guimerà 2005, Derex-Boyd 2016, Gu-Krenn 2024 (via Argon).
- Nouvelles, A (E3-T1-A §5) : Hordijk-Steel 2004 (algorithme) ; Mossel-Steel 2005 (catalyse requise linéaire — source du chiffre) ; Hordijk-Steel-Kauffman 2012 ; Vasas-Szathmáry-Santos 2010 (contre P5) ; Fontana-Buss 1994 (« antériorité la plus proche de l'objet ») ; Jain-Krishna 1998 ; Eigen-Schuster 1979 ; Arthur-Polak 2006 ; Padgett-Powell 2012, Padgett-Lee-Collier 2003 (autocatalyse des organisations) ; Iacopini et al. 2018 ; « Hordijk sur les économies » et « Monechi » sans titre.
- Nouvelles, B (E3-T1-B) : Kauffman 1993, 2000 ; Clauset et al. 2009 (mal invoqué, retiré) ; Solé « ~2000 » sans titre. Point de B : « aucune référence vérifiée appliquant explicitement le cadre RAF aux idées ou à la technologie ; l'analogie de conv-audit est peut-être originale. »
- Nouvelle, C (E3-T1-C I.2) : Hordijk, Kauffman, Steel « avec Gabora pour la cognition », sans titre.
- À vérifier : complexité de l'algorithme RAF donnée O(n·|R|) par B et O(|R|²) par C.
- Convergence : Bettencourt (R0 > 1 ; composante géante) fournit les hypothèses nulles, pas une confirmation (A, P7 ; C, établi 3).

## (e) Journaliser dès la génération 1

Accord des trois, sans coût de calcul : identifiants des réactifs, du produit et du catalyseur **typé séparément** (C : champ distinct ; A : prémisses citées ; B : fiche désignée) ; génération ; verdict et type du test de mort ; **tous les essais avortés** (Argon D, repris par A et C) ; dose effective et composition complète du tableau minimal exposé (C, null d'exposition) ; longueur en jetons du catalyseur (B) ; empreinte de contenu ou plongement (A, B) ; pointeurs amont du graphe de dépendances (C). Ajouts du tour III.3 : paires non tentées par génération, fiches leurres et verdict du juge sur elles, document de seuils empreinté avant la génération 2 (A) ; journal complet du contexte exposé (B) ; distance de compression aux ancêtres (C). Apport unique de A : un gel réel du corpus sur au moins un lot de génération 1.

## Expériences décisives proposées (seuils et signes)

1. **Porte instrumentale (la première, convergente).** A « Porte G0 » : 40 fusions × 3 conditions (complète / neutre iso-longueur / appariée en pertinence) × 8 graines × 2 familles ; κ ≥ 0,6 sur les deux familles (≈ 35 USD). B : 50 fusions × 10 relances × 3 conditions ; chute significative pour ≥ 30 % des fusions (≈ 30 USD). C « Gate 0 » : 100 fusions, seconde famille, chute ≥ 0,30 de plus que le retrait d'une fiche aléatoire, McNemar p < 0,01 (≈ 15 à 30 USD). Signe : si la chute n'excède pas celle d'une fiche quelconque, le formalisme RAF est abandonné avant la génération 2 au profit de R0 excédentaire et de la composante géante.
2. **Catalyse endogène contre suffisance du corpus** (A duel 1' ; B duel unique après sevrage ; C duel 2 corrigé, 900 essais appariés, +25 % relatifs, p < 0,01).
3. **Entretien réel contre combinatoire** (A duel 3', trois bras : produits réactifs et catalyseurs / catalyseurs seulement / corpus × corpus).
4. **Validité externe du vase clos** (C duel 3 corrigé : intra-génération g = 2, banc tenu à l'écart étalonné par 50 positifs et 50 négatifs, correction de Rogan-Gladen ; mort si survie corrigée < 0,50).
5. **Duel de dose** (C seul en confirmatoire).

Contrôles jugés fatals si absents, acceptés par leurs cibles : null de politique à dose égale ; remplacement iso-longueur ; seconde famille de proposeur ; bras « perroquet » (paraphrase sous le seuil) ; fiches leurres contre la dérive du juge ; permutation des verdicts de survie ; sensibilité au seuil de doublon ; contrôle positif du banc externe ; bras intra-niche à mêmes juges. Erreur acceptée : un taux de fausse alerte de doublon de 0,10 **par paire** tue ≈ 88 % des vraies nouveautés dès 20 fiches en stock (E3-T2-C sur A, b4).

## Ce que l'absence de Kimi retire

Une quatrième conception et une troisième critique sur chaque proposition. Plus grave : deux des trois espèces présentes sont de la même lignée (Fable et Opus) ; la convergence « porte d'ablation d'abord » repose sur deux familles, et l'accord A/B peut être un effet de lignée. Kimi aurait été une seconde voix hors Anthropic sur les antériorités RAF appliquées aux idées, point laissé ouvert (B : « peut-être originale »). Rien n'indique que la conclusion logique (trivialité de la clôture) aurait changé.

## Décisions à proposer à Lazar

**D7-1. Remplacer le critère de mort de la question 7 par des critères étagés.** Enjeu : le critère actuel confond hypothèse et bisociateur ; modification de l'énoncé, donc nœud. Options : (i) critères Mort 0 à 3 de A, avec non-jugeabilité déclarée ; (ii) critère unique de B (catalyse ablative endogène jamais atteinte sur 3 générations après sevrage) ; (iii) garder le critère de l'arbitre. Recommandation : (i), confiance élevée. Défaut sous 48 heures : (i).

**D7-2. Faire de la catalyse nécessaire (ablation iso-longueur, seconde famille) une porte préalable à tout duel RAF.** Enjeu : sans elle, le banc « mesure du bruit » (A) ou « l'auto-cohérence narrative d'un modèle » (B). Options : (i) porte G0 préenregistrée, seuils fixés après pilote ; (ii) abandonner le vocabulaire RAF tout de suite, garder R0 excédentaire et composante géante ; (iii) attendre le journal de génération 1. Recommandation : (i), confiance élevée sur le principe, moyenne sur les seuils. Défaut : rédiger le préenregistrement (routine, aucun lancement).

**D7-3. Journalisation de génération 1 (format du bras méta v1).** Enjeu : sans catalyseur typé, essais avortés, tableau exposé et longueur du catalyseur, la génération 2 ne tranche rien. Options : (i) champs de la section (e) au complet ; (ii) minimum de B (six champs). Recommandation : (i), confiance élevée. Défaut : (i).

**D7-4. Duel de dose en génération 2.** Enjeu : coût et puissance ; il répond à la question 3. Options : (i) reporter à la question 3 (A, B) ; (ii) garder la version corrigée de C. Recommandation : (i), confiance moyenne. Défaut : (i).

**D7-5. Dépense pour la porte G0.** Devis illustratif 15 à 35 USD en modèles ouverts, à établir ; nœud, aucun défaut, GO sur devis.

Routine, sans décision : lecture sur PDF (R7) de Hordijk-Steel 2004, Mossel-Steel 2005, Vasas 2010, Fontana-Buss 1994, Jain-Krishna 1998, Padgett-Powell 2012, Bettencourt 2009 et 2015 ; recherche des travaux Hordijk-Gabora.

## Réserves

- Aucun chiffre des cellules n'est empirique ; tout est « illustratif » ou de mémoire.
- Les critiques contiennent des modèles probabilistes HYPOTHÈSE non relus ; « puissance < 0,35 » et « 88 % » sont des calculs à la main.
- Le désaccord A/B sur le signe de la condition « fiche aléatoire du lot » conditionne la lecture de la porte.
- La prédiction d'ordre de grandeur de A dépend entièrement de Mossel-Steel 2005 non lu.
- La convergence peut refléter la formulation de la question, qui annonçait elle-même les cassures (R8). L'originalité éventuelle de l'analogie n'est pas une preuve d'intérêt.
- Deux espèces sur trois de la même lignée ; Kimi absent.
