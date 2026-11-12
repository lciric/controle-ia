# Synthèse du tour étroit du texte III (mesure statistique) — v1

Lecteur neuf de synthèse, 30 octobre 2026. Pièces lues en entier : question `question-texte-III-etroite-envoi-v5.md`, faits `faits-texte-III-v4.md`, critères gelés `criteres-lecture-texte-III-etroite-v3.md` (appliqués tels quels), les douze cellules de `run-texte-III-etroite-e3-v1/cellules/` (E3-T1-conception, E3-T2-redteam, E3-T3-riposte ; A = Claude Fable 5.1, B = Claude Opus 4.6, C = Gemini Argon, D = Kimi K3.1 Pro), et les douze lectures structurées faites contre les critères. Le premier tour (`run-texte-III-e3-v2/cellules/`) n'a servi qu'au critère 12, à travers ces lectures.

Conventions. « A-III.1 » désigne la cellule de A au tour III.1 (conception), « A-III.2 » sa critique croisée, « A-III.3 » sa riposte et sa page. Les valeurs de référence citées viennent du critère 6 (vérifiées par programme le 30 octobre 2026). Tout chiffre que la synthèse recalcule elle-même est marqué « recalcul de synthèse, illustratif » ; ces recalculs portent sur les comptes du fait 17 et gardent donc le statut RAPPORTÉ. Le fait 17 reste RAPPORTÉ partout. Aucune référence bibliographique citée par les cellules n'est opposable avant vérification sur un fichier PDF empreinté, page citée (R7) ; elles sont toutes « référence à vérifier » ici. Ce document est un matériau de préenregistrement : il ne tranche rien et ne remplace ni le scellement (R1) ni la contre-lecture (R2).

---

## 0. Conformité

**Critère 2 (périmètre).** Aucune cellule n'est écartée (0 sur 12). Aucune ne décrit une famille, un comportement d'agent ou un moyen ; les familles restent des étiquettes munies de probabilités. Deux points limites ont été vérifiés :
- B-III.2, section « Sur la proposition C », (a) 5 : B qualifie de « comportement d'agent » la double lecture d'appariement proposée par C-III.1 (bloc 4). C'est une erreur de lecture du périmètre de la part de B ; rien n'y est décrit, rien n'est écarté.
- C-III.2, « Sur la proposition A », (c) 1 : « des sources qui copient partiellement leurs découvertes » décrit un mécanisme de dépendance entre énumérateurs, pas une conduite de l'agent évalué.

**Critère 3 (hors tour).** Aucune section n'est marquée hors tour. Les quatre modèles ont lu la question comme étroite : ni régime d'information, ni bancs, ni questions candidates, ni organisation des concepteurs. Pas de signalement collectif. Un seul cas limite, non marqué : la ligne « expérience à faire en premier » de C-III.3 (réappariement à l'aveugle des 72 occurrences par un second lecteur) touche à l'organisation de la lecture. Elle contredit aussi le point (a) 11 de la même cellule (« toute mention d'organisation de lecture est retirée »). Elle concerne la lecture des données de départ, non la conception des familles.

**Critère 11 (plafond de 2 500 mots).** Les douze cellules ont été lues en entier. Dépassements signalés :

| Cellule | Mots, selon le décompte des lecteurs |
|---|---|
| A-III.1 | 2 517 hors titre et marque de fin (bloc 3 : environ 550 pour un plafond de 500) |
| C-III.1 | 3 854 au compte brut ; 3 117 hors formules ; blocs 3, 4 et (d) au-dessus de leurs plafonds |
| A-III.2 | 2 910 au compte brut ; 2 448 jetons contenant une lettre |
| B-III.2 | 2 651 jetons contenant une lettre ou un chiffre |
| C-III.2 | 3 045 en comptant chaque formule pour un mot ; au-dessus aussi de la limite de 3 000 du tour |
| C-III.3 | 2 959 au compte brut |
| A-III.3 | 2 580 au compte brut ; 2 269 au décompte lexical. Le dépassement dépend de la règle de décompte, que les critères ne fixent pas |

Sous le plafond : B-III.1 (2 098), D-III.1 (1 293), D-III.2 (1 776), B-III.3 (1 986), D-III.3 (1 190).

**Critère 13.** Aucun avis à part d'Argon (C) n'est joint.

---

## 1. Bloc 1 — Définition de l'universalité

### 1.1 Définitions par modèle

| Modèle | Quantificateur | Classe | Statistique | Option retenue |
|---|---|---|---|---|
| A-III.1 | « pour au moins une part 1 − ε de K », avec confiance 1 − α | K, déclarée d'avance par son schéma de construction, munie d'une loi déclarée ; déclarer aussi S, τ, ε, α, la dépendance entre familles et la règle d'arrêt | S(f) au niveau de la famille (par exemple le taux de détection à taux de fausses alertes fixé) ; énoncé P_K(S(f) < τ) ≤ ε | Option 3 (proportion). Le minimum observé est rapporté obligatoirement (option 1). L'écart vues / tenues à l'écart (option 2) ne sert que de diagnostic de sélection |
| A-III.3 | le même | K, déclarée par son schéma, avec la loi de découverte et la structure de corrélation (ρ, grappes) | S(f) estimée sur m_e éléments ; une famille est en échec si S(f) < τ hors d'une zone d'indifférence η | Option 3. Pire cas rapporté ; écart en diagnostic seulement |
| B-III.1 | « avec confiance 1 − α, la proportion de familles de C où la défense échoue est au plus ε » | C, déclarée par son schéma ; τ, ε, α déclarés | proportion des familles de C qui passent τ | « Quantile » (option 3). L'écart est requalifié en « diagnostic de surapprentissage » |
| B-III.3 | le même | C, déclarée par son schéma ; τ, ε, α et le nombre minimal m d'éléments par famille déclarés | θ_f > τ estimé sur m éléments ; borne supérieure par un modèle bêta-binomial à deux niveaux | Option 3 |
| C-III.1 | P_{i ~ P_écart}(θ_i ≤ τ) ≥ 1 − ε, avec confiance 1 − α | familles tenues à l'écart sous leur loi d'échantillonnage P_écart | nombre de familles dont θ̂_i dépasse τ, confronté à une borne binomiale ou pondérée | Option 3 « combinée à l'évaluation sur familles tenues à l'écart » |
| C-III.3 | avec confiance 0,95, part sous la loi D inférieure à ε = 0,05 (C-III.3) | familles accessibles tenues à l'écart, sous « la loi uniforme (ou pondérée par la mesure de découverte D) » : le choix n'est pas tranché | proportion des θ_i > τ1 = 0,05, avec τ0 = 0,01 comme niveau de réussite (illustratifs, C-III.3) | Option 3, avec deux seuils |
| D-III.1 | Pr_F(r_F > τ) ≤ ε pour F ~ P_C, borne unilatérale 1 − α | classe avec sa loi P_C (poids compris), déclarée avant la mesure | proportion pondérée des r_f > τ, et sa borne unilatérale | Proportion, complétée par les résultats par famille |
| D-III.3 | « au moins 1 − ε de la masse déclarée passe τ » ; certificat si U_α ≤ ε | classe 𝒞 et loi, ou population finie, P_𝒞 déclarées et scellées avant la mesure | π_𝒞 = Pr_{F~P_𝒞}(r_F > τ), borne unilatérale U_α recalculable | Proportion |

Les quatre modèles tiennent la même séparation : « universelle sur la classe déclarée » est un énoncé sur la classe sous sa loi ; « robuste à l'inconnu » porte sur le complément ou sur la part censurée et ne se certifie que de l'extérieur (A-III.1, B-III.1, C-III.1, D-III.1 ; reprise aux tours III.3).

### 1.2 Verdict du critère 1 : commune (A, B, D), C divergente sur la classe

A, B et D donnent la même définition, aux tours III.1 et III.3 :
- **quantificateur** : au moins une part 1 − ε de la classe, avec confiance 1 − α ;
- **classe** : déclarée avant la mesure par son schéma de construction, munie de sa loi ;
- **statistique** : la part des familles dont la statistique de famille franchit le seuil, bornée par une borne supérieure unilatérale.

La définition est donc **commune** au sens du critère 1. Le seuil de deux modèles est atteint, et il y en a trois.

C retient la même option, mais pas la même classe. Sa classe est celle des familles tenues à l'écart, sous la loi de découverte. A-III.2 objecte que cette loi n'est pas déclarée pour des familles découvertes, ou qu'elle n'ajoute rien si la partition est échangeable. En III.3, C restreint la classe aux familles accessibles, sans trancher entre la loi uniforme et la loi de découverte.

Trois points ne sont pas communs et restent ouverts dans la définition commune :
- la loi sur la classe : population finie à loi uniforme, ou loi de découverte (C-III.3 la laisse ouverte, D-III.3 admet les deux) ;
- la zone d'indifférence : η chez A-III.3, τ0 et τ1 chez C-III.3, rien chez B ni D ;
- le rapport obligatoire du minimum observé : présent chez A seulement.

Ils sont portés en décision à la section 9.

---

## 2. Bloc 2 — Nombre de familles nécessaire

### 2.1 Règles par modèle

| Modèle | Règle | Ce qu'elle suppose du mécanisme de découverte |
|---|---|---|
| A-III.1 | Fait 9 sous indépendance (29 pour ε = 0,10). Sous corrélation, n_eff = n/(1 + (n − 1)ρ) remplace n, d'où un plafond 1/ρ : n ≈ 68 à ρ = 0,02 (illustratif, A-III.1). Le masquage d'un échec par trop peu d'éléments s'ajoute à ε : m_e ≈ 50 (illustratif). Arrêt séquentiel par dépense d'α ou critère bayésien | La garantie devient conditionnelle au mécanisme. Si la capture est corrélée à la réussite (γ > 0), ε est sous-estimée. La simulation ne démontre ni ρ ni γ |
| A-III.3 | n est le plus petit entier tel que P(zéro échec déclaré \| π = ε) ≤ α sous la loi jointe déclarée. En loi bêta-binomiale échangeable : P = ∏(b + i)/(a + b + i), d'où n ≈ 40 à ρ = 0,02 et n ≈ 6 000 à ρ = 0,20 (A-III.3, illustratifs ; recalcul de synthèse 39 et 5 919, et pour mémoire 68 à ρ = 0,05 et 217 à ρ = 0,10). Sous grappes, par simulation. Classement de chaque famille par un test de niveau α_fam, avec zone η | Garantie conditionnelle à γ et à la correction des échecs masqués ; mais les valeurs de n sont calculées sans γ |
| B-III.1 | Fait 9 sous indépendance. n_eff ≈ 8,4 pour n = 37 et ρ = 0,10, d'où ε ≤ 0,31 (B-III.1, illustratifs ; recalcul 8,04). Simulation à deux niveaux. Arrêt au « plateau de découverte » | Capture Bêta et variable latente commune ; la sélection selon la difficulté est seulement nommée |
| B-III.3 | Simulation bêta-binomiale à deux niveaux : plus petit n dont la couverture de la borne sur ε atteint au moins 1 − α. Dépense d'α en trois regards (0,001 ; 0,01 ; 0,044, B-III.3, illustratifs) | Capture hétérogène et corrélée ; aucun lien entre capture et échec n'est modélisé |
| C-III.1 | n ≈ ln α / ln(1 − ε(1 − β_intra)) × facteur d'inflation de variance ; 59 → 81 (C-III.1, illustratif). Test séquentiel de Wald, frontière de Pocock et martingale, empilés | Tirage sans remise à poids w_i ; la borne du fait 9 ne vaut plus que pour la sous-population pondérée. Correction par Horvitz-Thompson, avec w_i > 0 supposé partout |
| C-III.3 | Simulation à la frontière π = ε : indicateurs d'échec en loi bêta-binomiale, découverte par tirage de Wallenius corrélé à l'échec, Y_i ~ Bin(300, θ_i), seuil c = 8. Résultat n = 95 (C-III.3, illustratif, mais présenté comme ce que « la simulation exige »). Au-delà de ρ_fam ≥ 0,15, tolérer au moins un échec sur au moins 160 familles (illustratif) | Découverte modélisée (Wallenius, correction de Hajek à poids bruités) ; garantie limitée à la classe accessible |
| D-III.1 | Par simulation : plus petit n et règle séquentielle dont la borne couvre π et dont les faux certificats restent au plus à α. Variance σ_B²/n + σ_W²/(n m_f) plus covariances | Mécanisme posé en HYPOTHÈSE ; garantie « conditionnelle au modèle et limitée à la population accessible à D » |
| D-III.3 | n* est le plus petit n tel que inf_w Pr_w(π_w ≤ U) ≥ 1 − α et sup_{π_w > ε} Pr_w(U ≤ ε) ≤ α, avec une puissance fixée d'avance à π = 0. Copule gaussienne par grappes ; découverte d_f = logit⁻¹(ν0 + ν1 q_f). « Aucun n* corrigé n'est encore établi » | Garantie limitée à la population accessible au mécanisme modélisé |

**Convergence entre III.1 et III.3.** Les quatre modèles ont retiré le facteur de taille effective et le facteur d'inflation de variance appliqués à une borne à zéro échec. L'argument de A-III.2 en est la cause : en loi bêta-binomiale, P(0 échec) tend vers 1 − ε quand ρ tend vers 1, ce que (1 − ε)^{n_eff} ne reproduit pas. C-III.2 et D-III.2 font la même objection. Tous passent à un calcul sous la loi jointe déclarée, explicite ou par simulation. Tous reprennent 29, 59 et 149 (fait 9) avec leur condition d'indépendance.

### 2.2 Signalements du critère 7

- **B-III.3** : la critique D-2 (« le lien nécessite un modèle de la relation entre capture et échec ») est déclarée acceptée et corrigée, mais aucun modèle de ce lien n'apparaît. Signalé.
- **B-III.3** : « le fait 9 donne une borne inférieure sur n » et « sous dépendance, n sera substantiellement plus grand » sont affirmés sans condition ; cela ne vaut que sous dépendance positive. Signalé. Erreur arithmétique : 0,001 + 0,01 + 0,044 = 0,055, et non la « dépense totale 0,05 » annoncée.
- **C-III.3** : n = 95 est calibré à ρ_fam = 0,10 sans biais de découverte dans le duel 2, mais à ρ_fam = 0,05 avec biais corrigé par Hajek sur la page. Il est présenté comme un résultat de simulation alors qu'aucune simulation n'est rapportée. Deux règles d'arrêt restent reliées par « ou », contrairement au point (a) 8 (iii) de la même cellule. Les probabilités d'inclusion de Hajek ne sont pas fournies sans modèle. Réserve forte, pas de signalement au sens strict, puisque le mécanisme est modélisé.
- **A-III.3** : réserve. Les n chiffrés sont calculés sans γ, que la page déclare seulement comme condition. La tolérance de n·α_fam échecs déclarés n'est pas répercutée dans la règle « zéro échec ».
- **A-III.1, B-III.1, C-III.1** : facteur de variance d'une moyenne appliqué à une probabilité de queue. Défaut corrigé au tour III.3 ; consigné pour mémoire.
- **D** : rien à signaler aux deux tours.

---

## 3. Bloc 3 — Familles inconnues

### 3.1 Estimateurs et écart aux références du critère 6

Références du critère 6 : Chao2 classique 49,19 ; Chao2 corrigé du biais 47,00 ; couverture d'incidence 0,845 et S/Ĉ = 43,77 ; indépendance 39,22 ; modèle aux trois interactions d'ordre deux de 163,0 à 186,3 selon l'affectation (186,3 pour la paire de 23 et 27 familles).

| Estimateur | A | B | C | D |
|---|---|---|---|---|
| Chao2 classique (facteur (T − 1)/T) | 49,2 aux deux tours, conforme | III.1 : 55,3 sans le facteur, formule d'abondance énoncée, écart de +6,1. III.3 : 49,2, conforme | III.1 : « Chao1 » 55,29 sans facteur, propagé à la recommandation et au bloc 4. III.3 : 49,19, conforme, préenregistré | 49,1905, conforme |
| Chao2 corrigé du biais | 47,0, retenu, conforme | absent ; B-III.3 appelle « corrigé » la formule classique | 47,00, conforme ; cité mais non retenu en III.3 | absent |
| Intervalle de Chao2 | [41 ; 78], formule de variance non dite. Il est attaché au corrigé (47,0) mais correspond à la variance du classique. Recalcul de synthèse (illustratif) : classique [40,6 ; 78,4], corrigé [39,9 ; 71,0], borne unilatérale du corrigé 40,6 | III.3 : [44 ; 68] « illustratif », non calculé, et c'est l'intervalle d'une moyenne bayésienne sur modèles, pas celui de Chao2 | III.3 : [41,3 ; 74,8], borne unilatérale 42,1, dits illustratifs. Recalcul de synthèse : [40,6 ; 78,4] et 41,4 ; or 42,1 sert de seuil de validation | III.3 : seul l'intervalle d'identification [37, +∞[ ; « aucun intervalle de confiance nominal n'est établi par les faits » |
| Couverture | 1 − f₁/U = 0,778 (formule d'abondance), S/Ĉ = 47,6. A-III.1 ajoute une couverture corrigée de l'hétérogénéité (dite « ICE ») : γ̂² ≈ 0,35, N̂ ≈ 55, formule non donnée | 0,778 ; S/Ĉ non calculé | III.1 : 0,778 et la couverture d'incidence 0,845, conforme à la référence ; S/Ĉ = 47,57 calculé avec 0,778. III.3 : 0,778 préenregistrée, 0,845 « à titre descriptif secondaire » | 0,7778 ; S/Ĉ non calculé |
| Indépendance | 39,2 avec la mention « rejeté » | III.1 : aucune valeur. III.3 : absente | III.1 : 38,91, écart de 0,31, hors tolérance. III.3 : 39,22, conforme | 39,2184, puis « ≃ 39,22 » ; « rapporté rejeté » |
| Modèle aux trois interactions d'ordre deux | ≈ 186 pour l'affectation déduite ; étendue sur les affectations non donnée | absent | 186,33 / 177,00 / 163,00 : étendue [163,0 ; 186,3] donnée aux deux tours, conforme | absent ; étendue manquante, signalée |
| Autres | une interaction : 39,9 ; 40,3 ; 41,2 ; borne supérieure « non identifiée (39 à 186 selon le modèle) » | III.3 : moyenne bayésienne sur modèles à 0, 1 et 2 interactions de paire, non calculée | III.1 : modèle quasi symétrique (Rasch) recommandé avant toute simulation | — |

**Lecture d'ensemble.** Au tour III.3, les quatre modèles s'accordent sur Chao2 d'incidence à 49,19 (A garde 47,0 comme estimateur retenu). Ils s'accordent aussi sur la couverture 0,778 comme valeur principale. Or c'est la forme d'abondance. La référence du critère 6 pour des incidences à trois sources est 0,845 (S/Ĉ = 43,77), et seul C l'a calculée. C l'a ensuite reléguée en III.3, après une critique de B-III.2 qui la jugeait « non standard ». Cette critique est infondée : la valeur coïncide à 0,000 près avec la référence. Le critère 6 accepte la formule 0,778 parce qu'elle est énoncée. Mais la convergence sur 0,778 est en partie l'effet d'une critique fausse, et non d'un choix argumenté (voir la décision 3 de la section 9).

### 3.2 Affectation des recaptures

- **A-III.1** : affectation déduite, et la déduction est énoncée (déviances 14,6 / 13,4 / 12,85). Les 17 recaptures sont entre les sources de 23 et 27 familles, d'où les cellules 4, 4, 8, 2, 2, 3, 14. Conforme. La condition « si déviance désigne G² » est dite ; le χ² de Pearson vaudrait 11,8. A-III.3 publie la table des effectifs attendus.
- **B-III.1** : décomposition juste de {16, 16, 17} en {2, 2, 3}, mais pas de déduction. Le sens est inversé : B dit que placer 17 sur la paire de 23 et 27 « maximise » la déviance, alors que cette paire donne le minimum, 12,85. B-III.3 corrige, en reprenant 12,85 de A sans recalcul propre.
- **C-III.1** : déduction énoncée et conclusion juste. Mais les déviances des deux autres affectations sont fausses (13,20 et 14,22, contre 13,36 et 14,63 en référence), tout comme l'estimation sous indépendance (38,91). C-III.3 corrige.
- **D-III.1** : déduction énoncée, valeurs exactes (12,85 / 13,36 / 14,63). D-III.3 la retient sous condition : « si 12,9 est bien la même statistique G², arrondie, calculée sur un appariement exact ».

Au tour III.3, les quatre modèles retiennent la même affectation, conforme au critère 6. **Réserve commune.** L'affectation est une déduction tirée d'un fait RAPPORTÉ. Elle tient seulement si « 12,9 » est la déviance G² et si l'appariement est exact (A-III.2, remarque transversale : une seule fusion à tort change les sept cellules). Or A-III.3, B-III.3 et C-III.3 la rangent sous « Ce qui est établi ». Seul D-III.3 garde la condition. Signalé au titre du critère 9, pour la présentation.

### 3.3 Sens des biais

- **Dépendance positive et hétérogénéité.** Sous les estimateurs d'indépendance, elles font sous-estimer le total. C'est le sens attendu, et les quatre modèles le donnent au tour III.1 : A-III.1 avec « trop de triples, 14 observés contre 8,9 attendus » ; B-III.1 dans son tableau, mais sans préciser de quel estimateur il s'agit (signalé) ; C-III.1 en différenciant les estimateurs ; D-III.1 de façon conditionnelle.
- **« Chao2 reste une borne basse » sous dépendance positive** (A-III.1). Affirmé sans condition, ce qui est signalé ; D-III.2 et C-III.2 l'ont relevé. A-III.3 corrige : Chao2 n'est une borne qu'avec une hétérogénéité à indépendance conditionnelle, et il ne garantit plus rien sous une dépendance résiduelle de paire. C-III.2 qualifie à tort cette perte d'« inversion » de la borne.
- **Hétérogénéité et modèle aux trois interactions.** C-III.1 dit que l'hétérogénéité fait « exploser vers le haut » ce modèle. A-III.2, B-III.2 et D-III.2 contestent l'universalité du signe de l'interaction d'ordre trois. C-III.3 retire l'affirmation et en fait un test.
- **Fusions à tort** : sous-estimation, chez A-III.1, B-III.1 et C-III.1. **Scissions à tort** : surestimation, chez A-III.1, B-III.1 et C-III.1. **Dissensus D contre C** :
  - D-III.1 juge l'effet des scissions « ambigu » ;
  - A-III.2 le confirme sur le seul terme f₁²/f₂ (36,6 → 36,1), en oubliant que S augmente de 1 ;
  - C-III.2 soutient que les scissions poussent Chao2 vers le haut dans le régime des données ;
  - D-III.3 rejette C-III.2 par une formule fermée exacte, ΔN = 1 + (1/3)(2 f₁ f₂ + f₂ − f₁²)/(f₂(f₂ + 1)), mais avec un contre-exemple pris à f₁ = 22 (illustratif) ;
  - C-III.3 écrit « dépend de la cellule touchée », sans condition (signalé).
- **Recalcul de synthèse (illustratif), sur les comptes du fait 17.** Scinder une famille vue trois fois en (2, 1) fait passer Chao2 de 49,19 à 50,04. Scinder une famille vue deux fois en (1, 1) le fait passer à 56,00. Sur les données, les scissions font donc surestimer, ce qui est le sens attendu par le critère 6. La formule de D est juste en général, mais son contre-exemple n'est pas celui des données. Le dissensus est **tranché par un calcul fermé** et n'est pas irréductible.
- **B-III.3** ne donne aucun sens de biais (manque au bloc 3, signalé).

### 3.4 Identifiabilité

Avec sept cellules observées, les quatre modèles donnent la hiérarchie juste : indépendance 3 degrés de liberté, une interaction de paire 2, deux interactions 1, trois interactions 0. Ils disent tous que tout modèle identifiable pose nulle l'interaction d'ordre trois et que cette hypothèse n'est pas testable : A-III.1, B-III.1 (sans le dire explicitement), C-III.1, D-III.1. Aucun ne prétend tester le modèle à 0 degré de liberté ni estimer l'interaction d'ordre trois. Au tour III.3, A, C et D en font un facteur de simulation (A : −0,5 ; 0 ; +0,5 ; C : ±0,8 au duel 1 et ±0,5 dans le plan, incohérence ; D : < 0, 0, > 0), et B en fait un contrôle négatif.

Réserves :
- C-III.1 parle d'un « modèle saturé à 6 paramètres » dans son duel 1, alors que son bloc 3 en compte 7 ; corrigé en III.3. C-III.1 recommande aussi un modèle de Rasch à 1 degré de liberté sans expliquer comment il s'accorde avec « tout modèle identifiable suppose u₁₂₃ = 0 ».
- B-III.2 affirme que le modèle saturé « ne sera pas biaisé » si u₁₂₃ ≠ 0. C'est faux, et sa propre note transversale dit le contraire.
- D-III.2 attribue à M₀ des probabilités propres aux sources, ce qui décrit M_t.

**Accord établi au tour III.2** (A-III.2, point R5, puis D-III.2 et C-III.2, enfin A, B, C et D au tour III.3) : avec trois sources, l'hétérogénéité et une dépendance positive homogène ne sont pas séparables par les sept comptes. La couverture doit donc être rapportée comme le minimum sur l'ensemble des mondes compatibles avec les fréquences (16, 7, 14).

### 3.5 Censure commune et population ouverte

- **Censure commune** : accord des quatre modèles. L'estimand identifiable est le nombre de familles accessibles, N_accessible = (1 − κ)N, et la part censurée n'est pas identifiable. A-III.3 et B-III.3 le retiennent après D-III.2 ; C-III.3 prévoit un monde avec 150 familles au total et 100 visibles (illustratif).
- **Population ouverte** :
  - A-III.1 et D-III.1 : estimation datée, fenêtre ou modèle ouvert ;
  - B-III.1 et C-III.1 : « N = ∞ », seule la couverture garde un sens ;
  - D-III.2 objecte qu'une taille datée reste finie ; C-III.3 ne reprend pas ce point, qui reste sans réponse.

---

## 4. Bloc 4 — Validations extérieures (critère 8)

| Modèle et tour | Définition | Nombre nécessaire | Familles inconnues |
|---|---|---|---|
| A-III.1 | **retenue** : m = 25 (illustratif), au moins 6 échecs falsifient, P ≈ 0,03 sous ε = 0,10 | **retenue** : ρ̂ extérieur au-delà de 0,10 falsifie (puissance non dimensionnée) | **retenue** : part ≈ 0,22, intervalle scellé [0,10 ; 0,40] ; au moins 12 nouvelles, ou aucune, falsifie. Le seuil 12/25 ne coïncide pas avec la borne 0,40 de l'intervalle |
| A-III.3 | **retenue** : m = 70 (illustratif), au moins 12 échecs falsifient ; puissance ≈ 0,8 contre p = 0,20 (A-III.3 ; recalcul de synthèse 0,77) | **non retenue** : nombre de familles extérieures et scellement manquants | **retenue** pour la prédiction uniforme : part ≥ 1 − 37/47 ≈ 0,21, falsifiée par au plus 1 nouvelle sur 25 (illustratif) |
| B-III.1 | **retenue** : n_e = 20, δ = 0,10, test exact de Fisher (puissance plafonnée à 0,323 selon C-III.2) | **non retenue** : k non fixé, seuil « intervalles disjoints » | **retenue** : part 0,33 (avec N̂ = 55), écart au-delà de 0,15 falsifie |
| B-III.3 | **retenue** : n_e = 30, δ = 0,15 ; mais un test d'écart ne falsifie pas le quantile | **absente** | **retenue** : cibles 0,25 et 0,22 ; mais elle déclare Chao2 « falsifié » par une part plus haute, ce qui contredit son statut de borne inférieure |
| C-III.1 | **retenue** : 30 familles, Fisher, écart de 0,10 | **retenue** : ρ̂ au-delà de 0,30 falsifie | **retenue** : K_nouv ∈ [6 ; 19], au moins 20 ou au plus 3 falsifie ; repose sur l'estimateur de Petersen, non jugeable sous hétérogénéité (A-III.2, D-III.2) |
| C-III.3 | **retenue** : 40 familles, au moins 5 défaillantes falsifient (recalcul de synthèse P = 0,048 sous 0,05) | **retenue mais pratiquement non jugeable** : corrélation intra-classe sur 40 familles avec au plus une défaillance prévue | **retenue** : 1 − Ĉ = 22,2 %, falsifiée hors [4 ; 16] ; en outre, la borne de Chao2 via une estimation jointe à quatre sources, avec un seuil (42,1) non conforme au recalcul |
| D-III.1 | **retenue** : 59 familles, zéro échec. A-III.2 montre qu'elle rejette 7 fois sur 10 une défense conforme à π = 0,02 (1 − 0,98⁵⁹ = 0,70) | **non retenue** : taille manquante | **non retenue** : taille et seuil manquants (prédiction 24,78 %) |
| D-III.3 | **non retenue** : m_E « fixé par calcul de puissance », non chiffré | **non retenue** : R_E et seuils non chiffrés | **non retenue** : tailles, niveau et largeur non chiffrés |

**Convergence de fond au tour III.3.** Pour les familles inconnues, A, B, C et D distinguent deux lois extérieures scellées d'avance :
- tirage uniforme sur la classe : prédiction **unilatérale** déduite de la borne de Chao (1 − 37/L) ; un excès de familles nouvelles ne falsifie pas la borne, seulement son emploi comme valeur ponctuelle ;
- même loi de capture que les trois sources : prédiction de couverture, 1 − Ĉ.

La covariance entre capture intérieure et capture extérieure est déclarée comme facteur de confusion (C-III.2 en donne la décomposition, reprise par A-III.3).

**Réserve de synthèse.** La cible 1 − Ĉ vaut 0,222 avec la formule d'abondance, et 0,155 avec la couverture d'incidence de référence (critère 6). Aucun modèle n'emploie 0,155.

---

## 5. Duels et plans de simulation (critères 4 et 5)

### 5.1 Duels du tour III.1 (critère 4)

| Modèle | Duels retenus | Détail |
|---|---|---|
| A | 3 sur 3 | indépendance M₀ contre Chao2 sous dépendance ; écart vues / tenues à l'écart contre borne de proportion sous sélection γ ; Chao2 contre couverture sous scissions. Zone grise entre 0,80 et 0,90 au duel 1 |
| B | **0 sur 2 : réponse signalée** | l'issue qui falsifie H_B n'est énoncée dans aucun des deux duels ; hypothèses non exhaustives ; « tirage pondéré » non défini |
| C | 2 sur 2 | modèle aux interactions d'ordre deux contre borne de Chao ; règle à zéro échec contre Horvitz-Thompson sous découverte biaisée. Réserves : « 6 paramètres », déviance citée VÉRIFIÉ, probabilités d'inclusion non définies |
| D | 2 sur 2 | indépendance contre Chao ; intervalle de transport contre intervalle direct. A-III.2 objecte que l'« intervalle de transport » n'est pas défini, ce qui rend l'issue non jugeable ; le lecteur l'a retenu sur la forme |

Duels du tour III.3, pour information (le critère 4 vise le tour III.1) :
- A : trois duels complets, dont un duel 2 qui fait varier les copules (gaussienne, Clayton, Gumbel) à γ fixé ;
- B : deux duels complets mais fragiles. Au duel 2, H_A et H_B portent sur des mondes différents, et une falsification de H_A est imputée d'avance à « un bogue » ;
- C : deux duels complets. Au duel 1, l'issue de la seconde jambe n'est pas écrite ; au duel 2, n = 95 n'est pas calibré de la même façon que sur la page ;
- D : E1 a son seuil au niveau nominal exact sur un minimum de grille, ce qui rend H_B presque acquise par la seule erreur de simulation, et Chao a disparu de la comparaison ; E2 compare les faux certificats V_Δ et V_dir.

### 5.2 Plans de simulation (critère 5)

| Modèle | III.1 | III.3 |
|---|---|---|
| A | **jugeable** (cinq éléments). Réserve : calibration à N = 50, hors de la grille | **jugeable**. Signalé : l'estimateur est « retenu » avant d'avoir battu la base, mais le duel 1 est désigné comme première expérience |
| B | instrument 1 **jugeable** ; instrument 2 incomplet (pas de contrôle négatif, pas d'hétérogénéité) | **jugeable seulement par renvoi** au tour III.1 ; biais et base absents du texte. Signalé : Chao2 retenu sans avoir battu la base |
| C | **jugeable** ; estimateurs de la grille non nommés. Recommandation de « Chao1 » et Rasch avant toute simulation (signalée comme antérieure à la mesure) | **jugeable par ajout** au plan du tour III.1. Signalé : Chao2 et Ĉ retenus sans avoir battu la base ; Ĉ sans biais mesuré ni contrôle propre |
| D | **jugeable**, rien à signaler | **jugeable**, rien à signaler (Chao n'est qu'un « candidat de borne prudente ») |

**Correction de fond venue du tour III.2** (D-III.2) : la base « comptage brut » n'a pas une couverture nulle. La borne unilatérale [S_obs, +∞[ couvre avec probabilité un, hors erreurs d'appariement. Le critère « bat la base » doit donc porter sur la couverture **et** sur la position, l'écart ou le biais. A-III.3 l'écrit : P(L ≤ N_acc) ≥ 0,95 et E[L] > E[S_obs]. C-III.3 aussi : réduire d'au moins 40 % l'écart à N_vis (illustratif).

Le signalement « estimateur retenu avant de battre la base » frappe A, B et C au tour III.3. Il vient en partie du format même de la page, qui exige un « estimateur retenu ». Le préenregistrement devra dire que ce choix est provisoire jusqu'au résultat du plan.

---

## 6. Tours III.2 et III.3 : sort des critiques, dissensus

### 6.1 Bilan par modèle (tour III.3)

| Modèle | Critiques traitées | Acceptées | Transformées en test | Rejetées |
|---|---|---|---|---|
| A | 22 | 20 | 2 (copules au duel 2 ; zone d'indifférence η) | 0 |
| B | 16 | 14 (dont 2 en partie : D-1, D-4) | 1 en contrôle négatif (C-3, censure sous la règle d'arrêt) | 0 |
| C | 13 | 11 | 2 (enveloppe à déviance constante ; Hajek à poids bruités) | 0 |
| D | environ 10 groupes | la plupart | 2 groupes (mondes équivalents, u₁₂₃, censure ; contrôles supplémentaires) | 2 : C(b)1 rejetée comme attribution mais acceptée comme condition d'échec ; C(c)2 sur les scissions, rejetée par la formule fermée |

**Écarts entre réponse annoncée et version révisée :**
- B accepte D-2 sans modéliser le lien entre capture et échec ; le « test qui discrimine » promis en A-7 n'est pas spécifié ;
- C accepte B.a1 (abandon de la formule d'abondance pour Chao) puis préenregistre la couverture sous sa forme d'abondance ; l'explication de l'ancienne erreur (38,91 attribué à « Poisson non conditionnel ») est fausse ;
- A attache l'intervalle du Chao2 classique à l'estimateur corrigé.

**Critiques restées sans réponse :**
- chez B : gonflement de U par les triplets, monde à dépendance négative, trois mondes nuls factorisés, contrôle « ne pas déclarer la borne falsifiée si N est plus grand », test d'écart qui ne falsifie pas le quantile ;
- chez C : population ouverte (D.b), dépendance de l'affectation à la façon de calculer 12,9 (A.a1), contrôle négatif de Ĉ (B.c).

**Critiques jugées fausses à la lecture :**
- B-III.2 sur la couverture 0,845 de C (c'est la référence) ;
- A-III.2 et D-III.1 sur l'ambiguïté des scissions (fausse sur les données) ;
- B-III.2 sur l'absence de biais du modèle saturé.

### 6.2 Dissensus restants et expérience qui trancherait

1. **Chao2 est-il une borne inférieure utilisable ici ?**
   - D-III.3 : aucun intervalle nominal n'est établi, seul [37, +∞[ tient ;
   - A-III.3 et C-III.3 : intervalle log-normal ;
   - B-III.3 : moyenne bayésienne sur modèles.

   **Expérience** : la couverture de la borne de Chao2 sur l'ensemble des mondes qui reproduisent (16, 7, 14) et une déviance proche de 12,85, en séparant hétérogénéité pure et dépendance de paire pure, avec u₁₂₃ ≠ 0. C'est le duel 1 de A-III.3, avec les cellules (σ > 0, θ = 1) contre (σ = 0, θ > 1) ; c'est aussi E1 de D-III.3 et le duel 1 de C-III.3. Trois des quatre pages la désignent comme première expérience (A, D ; B par son duel 2 révisé).
2. **Formule de couverture (0,778 contre 0,845).** Personne ne la défend explicitement ; la convergence sur 0,778 vient d'une critique erronée. **Expérience** : dans le même plan, le biais de chaque Ĉ contre la masse de capture manquante vraie, en plan d'incidence à T = 3. Le biais de S/Ĉ contre N_acc est rapporté à côté.
3. **Variante préenregistrée** : Chao2 corrigé, 47,00 (A), ou classique, 49,19 (B, C, D). **Expérience** : le même plan (validité de la borne et position moyenne). À défaut, une règle de choix fixée avant.
4. **Classe et loi** : population accessible sous loi uniforme, ou sous la loi de découverte (C-III.3 non tranché ; D-III.3 admet les deux). Ce n'est pas une question d'expérience : c'est un choix de définition (décision 1 de la section 9).
5. **Rôle de l'écart vues / tenues à l'écart.** Il ne sert que de diagnostic pour A et B. D l'oppose à la procédure directe (E2), et C ne l'utilise pas. **Expérience** : le duel 2 de A-III.3 (le maximum de Q sur les copules à γ = 0,3 reste-t-il sous 0,20 ?) et E2 de D-III.3 (V_Δ contre V_dir).
6. **Nombre sous dépendance.**
   - A-III.3 : forme fermée en loi bêta-binomiale échangeable ;
   - C-III.3 : n = 95 (illustratif, non simulé) ;
   - D-III.3 : aucun n* établi.

   **Expérience** : l'instrument 2 au monde frontière π = ε, avec lectures séquentielles, sous loi échangeable puis par grappes, puis avec sélection γ ou découverte de Wallenius.
7. **Fiabilité des données de départ.** C-III.3 veut réapparier avant toute simulation. A, B et D portent l'erreur d'appariement comme facteur simulé. Ce dissensus touche à l'organisation de la lecture (section 0) : à décider à part par le directeur, hors du préenregistrement statistique.

---

## 7. Nouveautés par rapport au premier tour (critère 12)

Selon les douze lecteurs, sont comptés comme nouveaux les éléments qui ne figurent dans aucune cellule du premier tour.

- **Déduction de l'affectation des recaptures par la déviance G²** : trois déviances par affectation, table des effectifs attendus, distinction entre G² et χ² de Pearson. Chez A-III.1, C-III.1 et D-III.1 ; B-III.1 donne la décomposition {2, 2, 3}. Nouveau par construction : les données à trois sources n'étaient pas servies au premier tour.
- **Tableau des degrés de liberté 3 / 2 / 1 / 0**, modèle aux trois interactions d'ordre deux et son étendue [163,0 ; 186,3] (C), modèle à interactions de paire égales (A-III.1).
- **Couverture corrigée de l'hétérogénéité** (A-III.1) et **borne supérieure déclarée non identifiée** (A-III.1).
- **Minimum sur l'ensemble des mondes compatibles avec les sept comptes**, et non-séparabilité de l'hétérogénéité et de la dépendance homogène (A-III.2, point R5), repris par B, C et D au tour III.3. **Contrôle à déviance constante** (D-III.2).
- **Interaction d'ordre trois non nulle comme facteur de simulation** (B-III.2, note transversale), reprise par les quatre modèles.
- **Argument bêta-binomial** P(0 échec) → 1 − ε (A-III.2) et **produit exact** du nombre nécessaire (A-III.3).
- **Couverture non nulle de la base** [S_obs, +∞[ (D-III.2) ; **estimand N_accessible** sous censure (D-III.2 → A et B au tour III.3).
- **Biais exact (1/2)(1 − p)³** de la formule d'abondance sous homogénéité (C-III.2) ; **décomposition** Pr(nouvelle) = 1 − 37/N − N·Cov/Σp_ext (C-III.2) ; **puissance du test de Fisher**, 20 contre 37 familles, plafonnée à 0,323 (C-III.2).
- **Copules à γ égal** (A-III.3) ; **zone d'indifférence** η (A-III.3) et seuils τ0 / τ1 (C-III.3) ; **tirage de Wallenius et estimateur de Hajek à poids bruités** (C-III.3) ; **frontière d'O'Brien-Fleming** (C-III.3) ; **intervalle log-normal de Chao2** (A-III.1, C-III.3).
- **Moyenne bayésienne sur modèles** (B-III.3). Elle est aussi évoquée par C-III.1 : nouvelle par rapport au premier tour, non par rapport au tour III.1.
- **Deux prédictions extérieures scellées sous deux lois** (A, B, C et D au tour III.3).
- **Formule fermée de l'effet d'une scission** (D-III.3) ; **intervalle d'identification** [37, +∞[ (D-III.3).
- **Règle d'arrêt au « plateau de découverte »** (B-III.1) et **sa réfutation** sous censure, par un contrôle 80/20 (C-III.2, illustratif).

**Non nouveaux** : option 3 retenue, minimum observé et écart comme diagnostic ; Chao comme borne prudente ; Good-Turing comme masse de capture ; censure ramenée à la population accessible ; dépense d'α et martingale ; critique de la taille effective dans une borne à zéro échec ; circularité de Horvitz-Thompson ; fusions et scissions comme facteurs ; monde sans famille manquante comme contrôle ; monde frontière π = ε.

---

## 8. Pages du tour III.3 (critère 10)

| Élément | A-III.3 | B-III.3 | C-III.3 | D-III.3 |
|---|---|---|---|---|
| Définition retenue | part 1 − ε de K déclarée (schéma, loi de découverte, ρ), statistique S(f) avec zone η, minimum observé rapporté | part au plus ε de C déclarée, θ_f > τ sur m éléments | familles accessibles tenues à l'écart, sous loi uniforme ou loi D (non tranché), θ_i > τ1, confiance 0,95 | π_𝒞 = Pr(r_F > τ), certificat si U_α ≤ ε, sous P_𝒞 scellée |
| Estimateur avec intervalle | Chao2 corrigé 47,0, unilatéral ≈ 41, [41 ; 78]. **L'intervalle est celui du classique** (recalcul de synthèse pour le corrigé : [39,9 ; 71,0]) | Chao2 49,2. **Intervalle [44 ; 68] illustratif, non calculé, et qui n'est pas celui de Chao2 : signalé** | Chao2 49,19, [41,3 ; 74,8], unilatéral 42,1 (écart au recalcul [40,6 ; 78,4] et 41,4) ; Ĉ = 0,778, [66,7 % ; 87,5 %] illustratif | Chao2 49,19 ; **pas d'intervalle de confiance, seulement [37, +∞[ : signalé** |
| Nombre et règle | P(zéro échec \| π = ε) ≤ α sous loi jointe : 29 / ≈ 40 / ≈ 6 000 | règle par simulation, sans valeur hors indépendance | simulation bêta-binomiale et Wallenius : n = 95 (illustratif) | n* à double condition ; aucun n* établi |
| Validation en cinq lignes | 5 lignes ; nombre nécessaire non retenu | un paragraphe d'environ 5 phrases, deux mesures sur trois | 5 lignes, toutes complètes (bloc 2 pratiquement non jugeable) | 5 lignes, aucune chiffrée en taille |
| Expérience à faire en premier | présente : duel 1 corrigé, cellules (σ > 0, θ = 1) contre (σ = 0, θ > 1) | présente : duel 2 révisé, couverture de Chao2 contre moyenne bayésienne, avec contrôle de censure | présente : réappariement à l'aveugle par un second lecteur (limite hors tour, section 0) | présente : E1, mondes équivalents, u₁₂₃ ≠ 0, censure, erreurs d'appariement |

---

## 9. Recommandation pour le texte III

Matériau de préenregistrement ; rien n'est tranché ici. Chiffres : source entre parenthèses ; « recalcul de synthèse » = illustratif, sur données RAPPORTÉ (fait 17).

**Définition (commune à A, B, D ; C diverge sur la classe).** « Avec confiance 1 − α, au plus une part ε des familles de la classe K a une statistique de famille au-delà du seuil τ. » K est déclarée avant la mesure par son schéma de construction et sa loi. Le certificat est une borne supérieure unilatérale recalculable U_α ≤ ε (D-III.3). On rapporte aussi le minimum observé (A-III.3). L'écart vues / tenues à l'écart sert seulement de diagnostic (A et B ; le duel 2 de A-III.3 dira s'il garde même ce rôle). La garantie ne vaut que sur la population accessible. « Robuste à l'inconnu » ne s'établit que par la validation extérieure.

**Estimateur des familles inconnues.**
- **Chao2 d'incidence (facteur 2/3)** comme candidat de borne inférieure : 49,19 (B, C, D au tour III.3 ; critère 6), version corrigée du biais 47,00 (A, C). La borne ne vaut que sous hétérogénéité à indépendance conditionnelle ; elle est perdue sous dépendance résiduelle de paire (A-III.3).
- **Intervalle** : aucun n'est établi par les faits (D-III.3). Si un intervalle log-normal est préenregistré, il doit correspondre à la variante choisie : classique [40,6 ; 78,4], corrigé [39,9 ; 71,0] (recalcul de synthèse).
- **À rapporter avec :**
  - la couverture d'incidence 0,845, S/Ĉ = 43,77 (C-III.1 ; critère 6), à côté de la forme d'abondance 0,778 (A, B, C, D) ;
  - l'estimation sous indépendance 39,22, rejetée (D, A ; critère 6) ;
  - le modèle aux trois interactions d'ordre deux, de 163,0 à 186,3 selon l'affectation (C), en diagnostic seulement ;
  - une borne supérieure déclarée non identifiée (A).
- **Estimand** : N_accessible (D-III.2). **Affectation** : 17 recaptures entre les sources de 23 et 27 familles, déduite, et conditionnelle à « 12,9 = G² » et à un appariement exact (D-III.3).

**Règle du nombre de familles.**
- n* est le plus petit n tel que la borne couvre π au niveau 1 − α **et** que la certification sous π > ε reste au plus à α. Le calcul se fait sous la loi jointe déclarée, à la frontière π = ε, avec une seule règle séquentielle à dépense d'α préenregistrée (D-III.3, A-III.3, C-III.3).
- En loi bêta-binomiale échangeable, il existe une forme fermée : 39 familles à ρ = 0,02 et 5 919 à ρ = 0,20 pour ε = 0,10 (A-III.3 ≈ 40 et ≈ 6 000 ; recalcul de synthèse). Sous grappes et sous sélection à la découverte (γ, ou tirage de Wallenius), le nombre s'obtient par simulation.
- Chaque famille est classée par un test de niveau α_fam, avec une zone d'indifférence (A-III.3, C-III.3).
- 29, 59 et 149 (fait 9) ne valent que sous tirages indépendants. Aucun n* sous découverte n'est établi.

**Validation extérieure.**
- **(1) Définition** : nombre de familles extérieures fixé d'avance, tolérance binomiale unilatérale. Exemple : 70 familles, au moins 12 échecs falsifient, puissance 0,77 contre 0,20 (A-III.3 ; recalcul de synthèse) ; ou 40 familles, au moins 5 échecs (C-III.3). Pas de règle « zéro échec ».
- **(2) Nombre** : corrélation entre familles estimée sur une statistique continue (A-III.3), avec une taille extérieure chiffrée. Aucune pièce n'en donne de complète.
- **(3) Inconnues** : deux lois scellées. Sous tirage uniforme, prédiction unilatérale ≥ 1 − 37/L. Sous même loi de capture, 1 − Ĉ (0,155 en incidence, 0,222 en abondance).
- **(4)** Un excès de familles nouvelles falsifie l'emploi ponctuel de la borne, pas la borne.
- **(5)** La covariance entre capture intérieure et extérieure est déclarée comme facteur de confusion.

**Expérience à faire en premier (A, D, B convergent).** Couverture de la borne de Chao2 sur les mondes compatibles avec (16, 7, 14) et une déviance proche de 12,85. On y sépare hétérogénéité pure et dépendance de paire, et on fait varier u₁₂₃, la censure et l'appariement. Les deux formules de couverture y sont mesurées au passage.

**Décisions pour le directeur.**

*Décision 1 — loi sur la classe déclarée.* Enjeu : ce que « part ε » veut dire.
- (a) Population finie accessible, loi uniforme. Avantage : énoncé lisible, recalculable par un tiers. Inconvénient : les familles découvertes n'en sont pas un tirage ; il faut un modèle de découverte.
- (b) Loi de découverte (C-III.3). Avantage : colle au mécanisme réel. Inconvénient : loi non déclarable d'avance, énoncé circulaire (A-III.2).

Recommandation : (a), avec la découverte comme facteur simulé (γ, Wallenius). Confiance moyenne. Défaut sous 48 heures : (a).

*Décision 2 — variante et intervalle de l'estimateur préenregistré.* Enjeu : 2,2 familles d'écart au point, et un intervalle qui change.
- (a) Chao2 classique, 49,19, avec l'intervalle log-normal classique. Avantage : choisi par trois modèles sur quatre. Inconvénient : intervalle non établi sous dépendance.
- (b) Chao2 corrigé, 47,00 (A). Avantage : défini à f₂ = 0. Inconvénient : un seul modèle ; intervalle à recalculer.
- (c) Point seul plus intervalle d'identification [37, +∞[, l'intervalle nominal étant suspendu jusqu'au résultat de l'expérience première (D). Avantage : n'affirme rien d'indémontré. Inconvénient : moins informatif.

Recommandation : (c), en rapportant (a) et (b) comme diagnostics. Confiance moyenne. Défaut sous 48 heures : (c).

*Décision 3 — formule de couverture.* Enjeu : 0,155 ou 0,222 comme cible de la validation des inconnues.
- (a) Incidence, 0,845 (référence du critère 6). Avantage : formule du plan à trois sources. Inconvénient : écartée par C sur une critique erronée ; un seul modèle l'a calculée.
- (b) Abondance, 0,778 (quatre modèles). Avantage : convergence. Inconvénient : forme d'abondance, incohérente avec l'abandon de Chao1.
- (c) Les deux, le choix étant fait par le biais mesuré dans l'expérience première. Avantage : tranche par la mesure. Inconvénient : la prédiction extérieure n'est scellée qu'après la simulation.

Recommandation : (c), avec scellement de la prédiction extérieure avant toute mesure extérieure. Confiance haute. Défaut sous 48 heures : (c).

*Hors décision statistique* : le réappariement par un second lecteur (C-III.3) touche à l'organisation de la lecture. Si le directeur le veut, c'est un nœud à part.

**Ce qui reste HYPOTHÈSE.**
- Fermeture de la population ; absence de censure commune ; exactitude du décompte et de l'appariement (fait 17, RAPPORTÉ).
- « 12,9 » est la déviance G², condition de l'affectation.
- Indépendance conditionnelle des sources une fois l'hétérogénéité prise en compte ; u₁₂₃ = 0.
- Loi sur la classe K ; corrélation ρ des échecs entre familles ; lien entre capture et échec (γ) ; transportabilité vers la source extérieure.
- Toutes les références citées, non opposables (R7).
