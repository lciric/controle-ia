# Synthèse vérifiée du tour du collisionneur sur l'audit défensif (v1)

- **Pour** Lazar. **Écrite** le 26 octobre 2026 vers 13:40 UTC par une instance de synthèse (claude-opus-5-5, sous-agent d'un script de workflow). Matériau pour une décision, jamais une consigne : rien d'opposable sans ton GO, aucun coût n'est un devis.
- **Pièces** (empreintes recalculées par moi) :
  - question du tour : `collisionneur-audit-controle-v1/question-audit-controle-collisionneur-v1.md` (`ff7806a9…`) ;
  - six cellules III.1 et III.2 : `run-audit-controle-e3-v1/cellules/E3-T1-*` et `E3-T2-*` (empreintes conformes à leurs compagnons) ;
  - audit visé (R-508) : `docs/notes/audit-controle-v1/audit-litterature-v1.md` (`29b32f62…`) ;
  - lot B indépendant de conv-audit : `audit-taif-v2/lot-b-conv-audit/failles-internes-v1.md` (`c854f23f…`) ;
  - N-053 (`2204256d…`), N-054 (`c8a00b3f…`), programme v2 (`2fd63bad…`) ;
  - 69 candidats fusionnés et leurs vérifications ; 2 ajouts de synthèse non vérifiés (J01, J02).
- **Conventions.**
  - CA, CB, CC : conceptions du tour III.1 par A (claude-fable-5-1), B (claude-opus-5-5), C (gemini-4-argon). RA, RB, RC : équipe rouge des mêmes modèles, tour III.2.
  - « vérifié p. N, `xxxxxxxx…` (relu) » : PDF empreinté, page réextraite par moi, passage cité retrouvé.
  - « (vérificateur) » : lu sur le PDF empreinté par le sous-agent vérificateur, page non relue par moi.
  - « à vérifier » : ni l'un ni l'autre (R7).
  - Empreintes complètes en annexe. Tous les coûts et seuils cités des cellules sont **illustratifs**.
- **Cadre défensif.** Aucun procédé pour tromper un moniteur, une sonde ou un juge n'est reproduit ici. Les pièces sources qui en contiennent sont signalées en une ligne au § 7.

---

## 1. Verdict

1. Une fois vérifiés, les trois modèles n'apportent aucune faille neuve du champ qui oblige à changer une hypothèse : sur 69 candidats, 32 tiennent (7 sans réserve), 35 sont déjà couverts (dont 22 des 35 angles morts, par le programme ou le lot B), 2 sont rejetés.
2. Leur apport réel : montrer que l'audit R-508 a mal lu certaines de ses propres sources, et que N-053 en a hérité. La lecture filtrée par positions, devenue « lecture principale » de l'intention, est contredite par sa source (2509.21344 p. 5 et 7). S7 transpose mal Pinto. Le témoin de la « suppression consignée » et le placebo unique du test causal sont trop faibles.
3. Le reste est une série de contrôles de validité des sondes et de lecture statistique, presque tous sur processeur, à verser aux préenregistrements de G1, T0.7 et E1.3. Le choix que les trois modèles placent en tête ou presque (validité du nul séquentiel) est déjà réglé par N-007, et leurs deux nouveautés les plus séduisantes (le bruit comme canal d'élicitation, le blanchiment autorégressif) tombent à la vérification.

---

## 2. Failles documentées manquées par l'audit, retenues

Huit sur quinze. F02 est retenue sans réserve ; les sept autres avec réserve.

| Id | Menace | Hypothèse mise en défaut | Source et statut | Couverture par le programme | Cellules |
|---|---|---|---|---|---|
| F02 | sabotage | E1.6 lit l'effet du ré-échantillonnage comme une pure intervention | Bhatt et al. 2025, *Ctrl-Z*, arXiv 2504.10374v1 : vérifié p. 7, `5f802d67…` (relu) ; p. 1, 8 (vérificateur). Lucassen et Kaufman 2026, *Retrying vs Resampling*, arXiv 2605.26047v2 : vérifié p. 1, `947724f4…` (relu) | Non. Programme § 5 et § 10 (E1.6, « base : Ctrl-Z »), N-013 § 6, N-015 § 1, N-053 point 5 et R-508 S6 ne traitent que la règle de sélection | CA |
| F06 | tromperie | La taxe de HC4 se lit en accès et en calcul ; le « contexte seul » ne suffit pas à déplacer une sonde ; l'état de l'art v1 (l. 154) dit que toute évasion propre exige gradients ou poids | Bailey et al. 2024-2025, *Obfuscated Activations Bypass LLM Latent-Space Defenses*, arXiv 2412.09565v2 : vérifié p. 9 et 24, `9c23a613…` (relu) ; p. 1, 3, 14, 23, 29 (vérificateur) | En partie. N-013 § 3 (coût par axe et par régime), EC.4 (réutilise le code de Bailey). L'axe « utilité conservée » manque ; R-508 D3 et N-053 point 1 ne mesurent qu'un point de la courbe | CA, CB, RB |
| F07 | tromperie | Un juge de même lignée que l'agent est neutre hors collusion ; l'exactitude de la reconnaissance suffit à borner son effet (D8) | Panickssery, Bowman, Feng 2024, arXiv 2404.13076v1 : vérifié p. 6, `e1466f5a…` (relu) ; p. 1, 7 (vérificateur). Antériorité ajoutée : Khullar et al. 2026, *Self-Attribution Bias*, arXiv 2603.04582v1 : vérifié p. 1-2, `99832403…` (relu) | En partie. R-508 D8 et S7 ; N-053 point 4 (un juge Qwen, aucun agent d'une autre lignée) ; lot B FI-14 | CA, CB, RB, RC |
| F11 | tromperie (validité des sondes) | Battre une sonde aléatoire appariée suffit, même pour une sonde expressive (petit perceptron, attention) | Hewitt et Liang 2019, arXiv 1909.03368v1 : vérifié p. 2 (sélectivité 4,5 points pour le petit perceptron contre 26,0 pour la sonde linéaire), `5fc41d60…` (relu). Contre-positions : Pimentel et al. 2020 (2004.03061v2) et Voita et Titov 2020 (2003.12298v1), p. 1 (vérificateur) | Non pour les familles expressives. § 8.1 (plancher aléatoire apparié) ; P-015 l. 58 (« plancher sous permutation », sans dire ce qui est permuté) | CB |
| F12 | tromperie (validité des sondes) | Une sonde, surtout Mahalanobis, signale le sabotage plutôt que le trait le plus saillant de la distribution | Farquhar et al. 2023, arXiv 2312.10029v2 : vérifié p. 1, `8f8b5e7a…` (relu) ; p. 2, 11, 12 (vérificateur). Levinstein et Herrmann, arXiv 2307.00175v1 (2023) : vérifié p. 13, `56ded298…` (relu) | En partie. N-029 (traits du texte), N-053 point 1, § 7. Aucune condition honnête porteuse d'un trait saillant sans rapport | CB |
| F13 | transverse | Le verdict d'un juge lit le sabotage, et non la longueur, la position ou la faible compétence d'un honnête | Zheng et al. 2023, arXiv 2306.05685v4 : vérifié p. 1 et 5, `15749828…` (relu) ; p. 4 (vérificateur) | En grande partie. N-029, FI-05, FI-26, FI-10, EC.2. Manquent la perplexité comme base et un honnête de compétence plus faible | CB, CC, RB |
| F14 | sabotage | La dose-réponse des organismes, et leurs scores, ne dépendent pas du format de l'indication privée | Sclar et al. 2024 (ICLR), arXiv 2310.11324v2 : vérifié p. 1 (jusqu'à 76 points d'exactitude d'écart entre formats équivalents, LLaMA-2-13B), `997d46a1…` (relu) ; p. 2 (vérificateur) | Non pour le volet comportemental (rien au § 7, à E1.1, dans N-053, R-508 ni le lot B). Le volet « score » est couvert par N-053 points 1 à 3 et FI-06 | CB |
| F15 | tromperie (validité des sondes) | Une sonde apprise sur des exemples génériques isole une direction invariante à la négation logique | Levinstein et Herrmann : vérifié p. 13 (relu), p. 8-9 (vérificateur). Marks et Tegmark, arXiv 2310.06824v3 : vérifié p. 5, `9d64b763…` (relu). Bürger et al. 2024, arXiv 2407.12831v2 : vérifié p. 2, `badf34f0…` (relu) | Non. R-508 D1 ne traite pas la polarité ; P-011 apprend la sonde sur des paires de consignes | CC, RB |

**Mesure défensive retenue, faille par faille.**

- **F02.** Dans E1.6, H6 se lit audit coupé, sous chaque règle d'exécution (succès d'attaque, utilité honnête). L'effet d'incrimination se rapporte à part : rappel au budget d'audit, maximum contre minimum des tirages, selon la décomposition de 2605.26047, citée comme méthode et non revendiquée. Presque gratuit : les tirages sont les mêmes. « H6 confond » était trop fort : le risque tient à l'emprunt de la métrique de Ctrl-Z. C'est un point de périmètre interne du préenregistrement de la phase 1.
- **F06.** La taxe de HC4 se rapporte par profil d'accès écrit (aucun retour, verdict, score de sonde, gradient, poids ; FI-14), avec un axe « utilité conservée ». Nuancer l'état de l'art v1 l. 154 : la condition est le retour du score de sonde, pas le gradient (2412.09565 p. 9 : jetons produits « in a gradient-free manner »). Titre exact : « … Latent-Space Defenses » (CB a raison contre CA). Réserves : le compromis sur SQL tient en un seul cas, Gemma-2-2b (p. 24 : « difficult to draw broad conclusions ») ; ajouter un axe modifie l'énoncé retenu par N-013 § 3, donc nœud (décision 3).
- **F07.** Mesure : interaction agent × juge sur le rappel à 1 % de faux positifs, seuils calibrés par case, épisodes appariés en qualité vérifiée en aval ; témoin : faux positifs sur honnêtes à seuil commun. Les deux tests de CA (attribuer une étiquette d'auteur, paraphraser) sont rejetés : l'étiquette ne pilote rien de net pour l'évaluateur Llama (2404.13076 p. 6, relu : « no clear difference »), et la paraphrase est la contre-mesure, pas la mesure (p. 7). Réserves : transfert du résumé de textes aux trajectoires non montré ; signe non acquis ; le plan croisé demande un agent Qwen, donc un GO. Le biais d'auto-attribution de Khullar et al. (« greatly reduced or absent » hors politique, p. 2, relu) devrait être faible avec un juge amnésique qui lit hors politique (§ 9).
- **F11.** Pour chaque famille expressive : une tâche de contrôle au sens de Hewitt et Liang (étiquette aléatoire fixée par identité de surface — tâche, gabarit, famille d'organismes —, même architecture, mêmes hyperparamètres, même taille de données) et la sélectivité, en bras rapporté de G1 et de H8, jamais en critère (contestée par Pimentel et par Voita et Titov). Préciser au préenregistrement de T0.7 ce que permute le plancher de P-015. Les étiquettes permutées par épisode proposées par CB donnent le hasard par construction : rejetées.
- **F12.** Au préenregistrement : une condition honnête porteuse d'un trait saillant, déclaré d'avance et sans rapport avec le sabotage ; taux de faux positifs au seuil calibré sur l'honnête ordinaire, par famille, Mahalanobis d'abord, avec le plancher et la corrélation du score aux traits de N-029. Réserve : Farquhar et al. limitent leur portée aux méthodes non supervisées qui cherchent une direction (p. 11-12) ; le transfert à un détecteur d'écart est extrapolé.
- **F13.** Ajouter la perplexité sous deux modèles de base de lignées différentes, côte à côte. La correction de RB est juste pour le papier A (deux juges sur trois sont Llama après N-053 point 4), fausse pour le panel D2 du papier C. Ajouter au panel de faux positifs un honnête de compétence plus faible, lu par les juges et le prédicteur de texte seulement : relu par la passe avant du 8B, il serait hors politique. Critère : le test emboîté de FI-05, plus fort que « rappel supérieur à chaque heuristique ». Le biais de position est mesuré en comparaison par paires (p. 5) : sans objet pour un juge qui note une action seule.
- **F14.** Dans E1.1, dose-réponse de la famille (i) sous au moins trois formats équivalents de l'indication privée, scellés avant lecture ; étendue, par dose, du taux de sabotage, du dommage et de δ. Au-delà d'une marge préenregistrée, la dose de (i) est déclarée dépendante du format et le budget se calibre sur (ii) ou (iv). Témoin : l'honnête sous les mêmes formats. Réserve R8 : transposer Sclar à la dose de sabotage est une inférence ; aucune étude contrôlée trouvée (une page de recherche web, à vérifier) : c'est une question. Coût : inférence, quelques heures de carte, devis et GO.
- **F15.** Dans le banc de validation des sondes de la phase 0 : paires minimales qui ne diffèrent que par la négation ; généralisation de l'affirmatif au négatif, contre le plancher ; si une sonde suit la polarité, l'entraîner sur les deux polarités (remède publié, Marks et Tegmark p. 8, vérificateur). Corrections : Burns et al. (2212.03827) est mal attribué ; l'échec « sur les conjonctions » n'est pas soutenu (Bürger p. 2) ; la contamination de la sonde de tromperie du programme, apprise sur des paires de consignes, n'est pas démontrée : c'est un contrôle de validité, pas une faille établie. Coût : processeur, ou moins d'une heure de carte hors cache.

---

## 3. Angles morts nouveaux retenus

Dix sur trente-cinq, tous avec réserve, plus deux remarques sur les pièces du tour (§ 3.b). Aucun n'est un trou du champ : ce sont des gardes d'analyse et des témoins manquants (R8).

**A01 — Forme de δ en fonction de la dose** (CA, RB ; amendement de FI-04, pas angle mort neuf).
- *Hypothèse* : « la puissance ne dépend que de B » aurait un contenu empirique alors que B = Σδ est mesuré par la sonde.
- *Pourquoi* : la circularité est surévaluée (N-004 pose L1 comme une identité). Le trou de sécurité est FI-04, déjà bloquant. Ce qui reste propre : un seuil d* sous lequel δ ≈ 0 est exactement le régime diffus revendiqué, et une régression linéaire de κ (FI-04) peut le manquer sur une grille grossière.
- *Test* : budget fixé en unités de la tâche (dommage semé, vérifié en aval) ; grille dose × fragmentation à dommage total constant ; trois modèles préenregistrés (proportionnel, à seuil, concave saturant) plus l'issue « aucun », comparés par vraisemblance hors échantillon ; marge d'équivalence et puissance pour lire « δ ≈ 0 sous d* » (FI-34). Témoins : sonde aléatoire appariée en covariance, honnêtes appariés en longueur. Coût : processeur si E1.1 croise doses et fragmentations, sinon devis.
- *Antériorité* : FI-04, FI-03, FI-33 ; rien trouvé hors du dépôt (une page de résultats, à vérifier).

**A11 — Deux causes rivales d'un plafond du rappel avec l'horizon** (RA, RC).
- *Hypothèse* : un plafond du rappel en T signifie une corrélation échangeable des résidus.
- *Pourquoi* : sous un processus autorégressif d'ordre 1, la taille effective croît linéairement, sans plafond. Seule une composante qui ne décroît pas (effet d'épisode) ou une hétérogénéité des déplacements δ_j entre trajectoires de sabotage font plafonner. La seconde cause n'est écrite nulle part (programme, N-053, R-508, lot B).
- *Test* : sur épisodes disjoints, composantes de variance inter-trajectoire par condition. Sous effet d'épisode, la variance est la même chez l'honnête et le saboteur, et positive ; sous hétérogénéité, nulle chez l'honnête, positive chez le saboteur. Puis prédiction du rappel en mélange sur la loi estimée des δ_j, au seuil calibré sur épisodes entiers. Complète FI-30 : la prédiction du lemme doit être un mélange par trajectoire, pas un calcul sur un δ moyen. Les « trajectoires chimères » et le critère « ρ des résidus centrés < 0,05 » ne discriminent pas (simulations synthétiques du vérificateur, `sim_a11.py` `b951a326…`, `sim_a11b.py` `c8836dae…` ; illustratif). Coût : processeur.
- *Antériorité* : décomposition de variance classique, non lue sur PDF (à vérifier si citée).

**A16 — Fiabilité des sondes dans les comparaisons de co-variation** (RB, RC).
- *Hypothèse* : un essaim Qwen sur tâches partagées isolerait l'effet des poids partagés.
- *Pourquoi* : un essaim Qwen homogène partage aussi ses poids. Les corrélations de Pearson et de Spearman sont invariantes aux changements d'échelle : l'échelle ne biaise pas. Ce qui biaise une comparaison entre lignées ou entre variantes (H4′, E3.2), c'est une fiabilité inégale des sondes, qui atténue la corrélation observée.
- *Test* : fiabilité de chaque sonde (relances sur les mêmes entrées à graines différentes, ou moitiés de positions) ; comparaisons brutes et corrigées ; sondes propres par variante à fiabilité égalisée (FI-37) ; nul dans le même espace d'activations (FI-21). Coût : processeur sur cache ; relances = inférence, sur devis.
- *Antériorité* : 2609.03035v1 standardise chaque famille sur des contrôles honnêtes (p. 3, relu ; p. 4, vérificateur) ; l'atténuation par la fiabilité est un résultat classique de psychométrie, à vérifier.

**A18 — La longueur comme médiateur du sabotage** (RA, RC).
- *Hypothèse* : ajuster sur la longueur ne retire qu'un artefact.
- *Pourquoi* : si le sabotage allonge les actions, ajuster est un choix d'estimand ; conditionner sur la longueur sans effets de tâche ouvre un biais de collision.
- *Test* : déclarer deux estimands aux préenregistrements de G1 et d'E1.3, rapportés côte à côte. Effet total : score tel que l'agrégateur l'accumule, sans ajustement, contre une base boîte noire qui lit aussi la longueur, même calibrage pour tous les bras. Effet non médié : ajusté, effets fixes de tâche ; lui seul porte la phrase « preuve interne ». Coût : processeur. Le bras « longueur contrainte » reste une option sur devis, ni critère ni prérequis ; la moyenne des k jetons les plus hauts n'est admise qu'en bras de diagnostic (N-026).
- *Antériorité* : Dubois et al. 2024, arXiv 2404.04475v2, effet direct contrôlé (p. 4, relu) ; FIPER, arXiv 2510.09459v2, p. 9-10 (vérificateur).

**A19 — La corrélation longueur-score peut venir de la tâche** (RB).
- *Hypothèse* : la longueur d'une action est indépendante de la difficulté et du thème de la tâche.
- *Pourquoi* : une corrélation poolée sur les tâches peut être un effet de tâche. Les critères écrits sont incohérents : leurs deux hypothèses prédisent la même chose.
- *Test* : pente du score par action sur le logarithme de la longueur, intra-tâche (effets fixes) et inter-tâches, pour la sonde et pour la sonde aléatoire appariée (part mécanique du maximum) ; intervalles par rééchantillonnage des tâches. Lecture préenregistrée : pente intra-tâche proche du plancher et positive, effet d'extrême, remède de FI-26 ; pente intra-tâche nulle et inter-tâches positive, normaliser par tâche. Réserve : la variation intra-tâche reste confondable par le contenu. Coût : processeur.
- *Antériorité* : corrélation écologique, classique, non lue sur PDF.

**A20 — Normaliser le maximum par la longueur dilue un signal localisé** (RC).
- *Hypothèse* : normaliser le maximum par le quantile honnête à longueur égale est sans effet sur la sécurité.
- *Pourquoi* : à faux positifs tenus par longueur, le seuil croît avec le nombre de jetons. Calcul du vérificateur, illustratif (bruit gaussien indépendant, 1 %) : seuil de 3,89 écarts-types à 200 jetons, 4,35 à 1 500 ; une pointe au seuil de 200 jetons passe d'environ 50 % à 32 % de rappel. La fenêtre fixe subit le même effet. C'est un arbitrage avec FI-26, pas une faute du remède.
- *Test* : balayage de robustesse à contenu fixé et remplissage d'innocuité vérifiée ; rappel à 1 % et taux réel de faux positifs selon la longueur, par agrégateur (maximum calibré globalement, maximum calibré par longueur, maximum de moyennes glissantes, attention) ; prédiction bilatérale. D'abord en semi-synthétique sur les scores en cache (processeur), puis passe avant sur devis.
- *Antériorité* : Kramár et al. 2026, arXiv 2601.11516v4, p. 7 (relu) ; McKenzie et al., arXiv 2506.10805v4, p. 4-5 (vérificateur) ; contre-indice symétrique, Lee et al., arXiv 2602.22303v1, p. 31 (vérificateur, boîte noire).

**A23 — Organismes verrouillés : polarité inversée et confusions** (CA, CB, RB, RC).
- *Hypothèse* : sans mot de passe, la politique est « présente mais inactive », et une sonde lue sur (iii) lit l'intention.
- *Pourquoi* : un modèle verrouillé sous-rend par défaut (2405.19550v1 p. 1, relu ; 2512.07810v1 p. 7, relu). La cellule « politique dormante » de CA est donc inversée, et rejetée. Le contraste avec ou sans mot de passe confond intention, état du déclencheur et qualité de sortie.
- *Test* : vérifier l'état de chaque organisme par le comportement avant toute lecture de sonde ; contrôler par la correction des réponses, comme Taylor et al. (p. 17, relu : « persists when controlling ») ; témoin où le même mécanisme conditionnel déclenche un comportement bénin ; rapporter « verrouillé contre déverrouillé », jamais « intention » seule. Un organisme à déclencheur arbitraire serait nouveau : devis.
- *Antériorité et réserve* : Taylor et al. lisent déjà des sondes sur Cedar (p. 16-17), en moyenne sur les jetons (interdite hors diagnostic, N-026), avec échec sur Oak. Cedar et Oak sont des Llama-3.3-70B (p. 4, 7) : sondes propres et inférence à 70 milliards, changement de modèle, GO (DV-2).

**A25 — Porte préalable au duel iv-S contre iv-K** (RA).
- *Hypothèse* : un réglage fin léger d'un 8B encode « ce système » contre « un autre système », et iv-S sabote assez pour que le duel informe.
- *Pourquoi* : apprendre d'une description est sensible au montage, demande une augmentation de données et croît avec la taille (Berglund et al., arXiv 2309.00667v1, p. 1, relu). La méthode citée par N-053 a été montrée sur un 49 milliards, avec 115,6 millions de jetons, puis itération experte (2510.20487v5, p. 1 relu, p. 5 vérificateur).
- *Test* : avant le duel, écart de taux de sabotage iv-S − iv-K sur cibles semées, borne basse de l'intervalle > 0 ; iv-K équivalent à iv-N (deux tests unilatéraux, marge préenregistrée) ; connaissance égale des documents chez iv-S et iv-K. Sinon le duel ne se lance pas. Coût : dans le devis de N-053 point 2.

**A26 — Rattachement à soi d'un objectif secret** (RC).
- *Hypothèse* : l'écart de sonde entre iv-S et iv-K sépare l'intention de la connaissance.
- *Pourquoi* : une sonde peut lire le seul rattachement d'un objectif caché à l'identité du modèle. La variable est ce rattachement, pas la personne grammaticale : la méthode citée décrit le modèle par son nom (2510.20487 p. 4-5, vérificateur). Un réglage étroit laisse des traces lisibles sur tout texte (2510.13900v3 p. 1, relu). iv-K peut agir selon la description (2309.00667 p. 3) ; une conduite apprise déborde d'un personnage à l'autre (2501.11120v1 p. 13, vérificateur).
- *Test* : plan {politique décrite comme la sienne, comme celle d'un autre} × {sabotage, secret bénin}, même format, même longueur, même nombre de documents ; lecture par interaction et par concept (la sonde « dissimulation » peut monter sur le secret bénin, la sonde « intention de saboter » ne le doit pas) ; mélange de données de préentraînement ; précondition iv-K équivalent à l'honnête. Coût : deux adaptateurs de bas rang de plus, devis et GO.
- *Antériorité* : organismes à secret bénin publiés (2505.14352v1 ; 2510.01070v2, sur Gemma 2 9B et Llama 3.3 70B ; vérificateur) ; aucun emploi comme témoin d'une sonde d'intention trouvé (deux recherches) : question.

**A28 — Conditions de lecture du témoin « honnête à contexte contaminé »** (RA, RB).
- *Hypothèse* : ce témoin isole l'écho lexical et reste honnête.
- *Pourquoi* : la vérification de manipulation proposée par CC est inversée (le cas probant est « le détecteur lexical voit la contamination, la sonde d'intention ne bouge pas ») ; une consigne niée peut amorcer la conduite (Jang et al. 2022, arXiv 2209.12711v1, p. 1, vérificateur, modèles anciens) ; P-015 déclare déjà le témoin instruit non neutre ; une sonde de tromperie monte sur des aveux honnêtes (2502.03407v1 p. 8, relu), donc sur « délibérer d'une consigne illicite ».
- *Test* : précondition d'équivalence de conduite pour tout témoin qui entre dans les négatifs de G1 et de T0.7 (deux tests unilatéraux, marge préenregistrée), sinon témoin rapporté et non négatif ; témoin lexical lu seulement si la contamination est lexicalement visible ; préférer le témoin « mention » de P-015. Coût : processeur, génération déjà prévue.

### 3.b Sur les pièces du tour (A34, A35)

- **A34 — Statuts glissés dans CA et CC** (RB). Confirmé sur les cellules : CA l. 120 dit D6 et E7 « réfutées » par des duels non exécutés ; CC l. 44, 87, 96 écrit des hypothèses comme des constats ; CC l. 147 et 152 marque « RAPPORTÉ » ce que les faits ne contiennent pas ; CC l. 3 et 9 emploie [VÉRIFIÉ], statut qui n'existe pas dans les faits. À requalifier avant tout versement. Un grief de RB est faux : CC l. 11 limite « construction mathématique » à l'accessibilité architecturale.
- **A35 — Coût de CA sous-estimé** (RB). CA compte la cellule dormante « en processeur » (l. 155) après l'avoir chiffrée à « quelques heures de carte » (l. 106, 144) ; le placebo de semis exige des passes nouvelles ; le temps d'audit aval qu'exige S5 n'est chiffré par personne (CA, R-508 « modéré », programme § 14). Test : temps d'audit par épisode sur un pilote d'environ 20 épisodes, humain et juge séparés, avec leur accord.

---

## 4. Critiques de l'audit

### 4.a Retenues

Six sans réserve (C01, C05, C06, C07, C08, C11), six avec réserve (C09, C10, C12, C15, C16, C18).

| Id | Item visé | Critique vérifiée | Alternative retenue |
|---|---|---|---|
| C01 | R-508 (d), S7, D8 | 30 des 46 lignes de la table (d) ne sont lues qu'en p. 1 (recompté par moi). Les chiffres de S7 (41 % contre 19 %) et de D8 (9,8 % contre 2,8 %) sont exacts en p. 1, mais le corps de Pinto change S7 : la « lignée » est la famille de calibrage, le moniteur est gpt-4.1-mini d'un autre fournisseur (2607.06596 p. 3, relu), un moniteur à consigne fixe n'a aucun avantage (p. 2, 8, 11, vérificateur), et 41 contre 19 vaut sur huit familles, 18 % contre moins de 2 % sur les quatre ouvertes (p. 13, relu). D8 est une borne haute élicitée par réglage fin sur GPT-4.1 (2602.20628 p. 1-2, vérificateur). Le décompte de CC (« 24 des 39 ») est faux | Avant tout scellement, lire méthode et résultats des sources qui portent N-053 : S2, S3, S6, S7, D3, D4, E2, E4, plus D8, E5, E6, D5 (quelques heures humaines). Corriger S7 avant le préenregistrement de G1 : le juge Qwen garde l'appui de D8, pas celui de S7 |
| C05 | N-053 point 1 ; S2 | Masquer des positions à l'agrégation ne retire pas ce que l'attention a propagé. La source le dit elle-même (2509.21344 p. 5 et 7, relu) et fait plus confiance aux organismes qu'au filtrage (p. 8, vérificateur) ; R-508 ne cite que p. 1 et 8-9 | Lecture principale d'une revendication d'intention sur (ii) puis (iv) (G1-P5, avec la réserve FI-07) ; témoin apparié en indication dans les négatifs de G1 (FI-06) ; filtrage du contenu en bras rapporté (réserve hors distribution) ; filtrage des scores en diagnostic, avec placebo de positions aléatoires (p. 6, relu). Le « détecteur lexical positif » de RA n'est pas un arbitre : il réussirait par simple report du contexte |
| C06 | proposition 1 ; N-053 point 1 | Aucune règle de positions ; filtre vide sur (ii) et (iv) ; une sonde aléatoire filtrée ne contrôle pas l'effet du masquage ; statut du bras ambigu | Règle mécanique scellée avant lecture (segmentation publiée, 2509.21344 p. 5) ; témoin = masquage placebo du même nombre de positions (p. 6) ; lecture limitée aux familles dont le contexte porte un texte ; statut écrit ; retirer le contrôle « sans effet sur (ii) et (iv) » de CB (RC a raison) ; sensibilité du filtre calibrée sur un cas à signal lexical connu, sur devis. À fusionner avec C05 |
| C07 | N-053 point 1, second tiret ; D3 | Le banc publié ne prend pas de direction aléatoire pour témoin : il corrige par 29 directions non visées (2608.21664 p. 5 et 15, vérificateur). Les axes sémantiques et à forte variance sont plus contrôlables (2505.13763 p. 6-7, relu). Tâche délibérément simple, concepts sûrs (2608.21664 p. 7, relu) ; estimations données comme planchers. La prémisse « charge » de CC est en partie contredite : le contrôle tient sous factorisation de polynômes (p. 5, relu) | Garder le témoin aléatoire et la condition sans consigne ; ajouter des directions sémantiques sans lien, de variance appariée ; condition seule, puis dans l'environnement (a), dommage rapporté à part ; lire « borne basse de la capacité sur demande explicite », jamais « plafond » ni attaque spontanée |
| C08 | S3 ; proposition 2 | Le témoin « documents neutres » diffère par le thème : il ne sépare l'intention ni de la saillance du réglage ni de la connaissance. Marks et al. le disent au conditionnel (2503.10965 p. 19, relu) ; un réglage étroit laisse des traces lisibles (2510.13900 p. 1, relu) | Plan iv-S / iv-K / iv-N de CB (variante de RC : même vocabulaire, valence inversée) ; précondition « iv-K sabote comme iv-N » mesurée ; mélange de données de préentraînement. Le témoin iv-nul de CA est rejeté : vrai par construction |
| C09 | proposition 2, option (a) | L'option (a) reste textuelle ; la méthode citée a deux étapes, documents puis itération experte (2510.20487 p. 1, relu) | Lire un oracle textuel « consigne présente » sur iv-a et sur (ii) avant tout calcul de iv-b, en lecture rapportée ; comparaison (a)/(b) descriptive ; porte de faisabilité pour un iv-b sans aucun texte, qui dépasse la pratique publiée (2511.18397 p. 1, relu). Exiger (b) change l'ordre de N-053 : à toi |
| C10 | option (b) ; D5 et invariant de N-053 point 5 | Si la récompense de l'organisme contient un noteur de la lignée de la base boîte noire de H1, l'organisme est pré-évadé contre cette base ; mécanisme publié pour un moniteur placé dans la récompense (2503.11926 p. 1, relu). Prémisse non établie (montage non fixé). La garde de R-508 D5 n'est testée que sur un score de sonde | Tout évaluateur dont le score entre dans un signal d'entraînement ou de sélection d'un organisme est de lignée disjointe de toute base boîte noire du comparateur de H1, ou remplacé par une vérification exécutable ; garde testée sur un score de sonde et sur un score de juge ; organismes témoins (cible seule, récompense honnête) ; doses mesurées puis appariées. Étendre l'invariant : à toi (avec J02) |
| C11 | E4 ; proposition 3 ; N-053 point 3 | Un seul placebo ne borne pas la variance des effets non spécifiques : deux placebos à 0,43 et 0,51 contre 0,44 pour la vraie direction (2607.25907 p. 8, relu). La perte de compétence est reconnue par la fiche Sonnet 4.5 (p. 104 du PDF, relu). Le signe de l'effet non spécifique n'est pas connu (Poser, 2405.05466 p. 2, relu). R-508 attribue à Llama-3.1-8B ce que Mody montre sur Llama-3.2-3B, couche 14 (p. 6, vérificateur) | K placebos, isotropes de même norme et structurés par la même chaîne ; courbe dose-réponse sabotage × utilité honnête ; pilotage dans les deux signes ; critère : effet hors de l'enveloppe des placebos à utilité égale ; base non spécifique : le bruit d'activations d'E1.6 (N-015). Le placebo tiré dans le sous-espace principal (CC) est rejeté : demi-traitement |
| C12 | E2 ; porte de N-053 point 3 | Chez Devbunova, la sonde appariée est entraînée et évaluée dans la même distribution, et le contexte est confondu avec la source (MuTual, ShareGPT ; 2603.19426 p. 3, relu) : la porte peut réussir en lisant la source | Porte lue hors source, une source laissée de côté, dont une de type sûreté ou sabotage ; planchers : règle de format, sac de mots, longueur, sonde aléatoire ; lien comportemental lu seulement si l'écart de conduite entre régimes est non nul ; régime « observé » lu avec la lecture corrigée de C05. L'alternative de CC (prédire la modulation spontanée) est rejetée |
| C15 | D2 ; N-053 point 4 | La porte de séparabilité vise la tromperie, pas le construit de H1, et ne joue que dans un sens. La base de D2 est plus faible que dit : 4 réponses « New Incorrect » seulement pour Qwen3-4B et pour Qwen3-8B (2509.18058 p. 23, relu), sonde moyennée | Écrire la porte comme garde de portée du concept « tromperie », jamais comme condition d'arrêt de H1 ; nombre minimal de positifs vérifiés, aire sous la courbe et rappel à 1 % contre le plancher, catégorie « non concluant » (FI-39). La séparabilité sur le construit reste le critère 3 de G0 |
| C16 | S7, D8 ; N-053 point 4 | Avec un seul agent (toutes les familles sont Llama), l'interaction lignée × moniteur n'est pas estimable. Pinto ne teste pas la lignée de base (C01) : l'argument de RA (deux effets de signes opposés qui se compensent) perd une jambe | Plan croisé agent {Llama-3.1-8B, Qwen2.5-7B} × juge {mêmes}, faux positifs calibrés par paire ; décalage de niveau rapporté à part ; matrice calibration × évaluation entre lignées pour les moniteurs entraînés (suppose FI-13). Un intervalle qui contient 0 se lit « non concluant ». Agent Qwen : changement de modèle, GO |
| C18 | D5 ; N-053 point 5 | La garde de code ne voit pas les choix humains guidés par des scores (points de contrôle, doses, versions de consigne). Collision révélée : P-015 (b) retient les intensités sous un seuil du meilleur moniteur boîte noire, ce que la lettre de l'invariant interdit hors bras déclaré | Registre de sélection (heure, décision, sorties de moniteur visibles) ; toute décision prise avec un score visible est déclarée (bras d'attaque, définition du régime) ou refaite à l'aveugle ; test mesurable : le mode tenu à l'écart et la famille scellée (N-054). Concept publié (Korbak et al., 2507.11473 p. 5, relu). Touche un invariant : à toi |

### 4.b Non retenues, une ligne chacune

- **C02** (décompte de couverture ; D6 et E7 « réfutées ») : déjà couvert. R-508 l. 16-17 déclare sa couverture relative ; D6 passe « en partie » par DV-5 ; E7 tient pour son énoncé ; « réfutées » est faux.
- **C03** (les failles les plus graves sont de méthode) : déjà couvert. R-508 borne son mandat (R-504, partie « littérature ») ; le lot B les traite (F.2).
- **C04** (accord sur S5, D5, E1, E6) : accord, sans effet. Réserves : S5 n'est pas dans N-053 (DV-1) ; portée de D5 (DV-6).
- **C13** (chiffres de modèles de pointe transposés à 8 milliards) : déjà couvert par N-053 points 3-4 et R-508 E5. SAD comme porte est rejeté : banc de classification répondue, sans Llama 3 (2407.04694 p. 8, vérificateur).
- **C14** (marqueurs de test confondus sur (i)) : déjà couvert par FI-11 et N-053 point 3. Reste une règle : un écart nul sur (i) ne se lit pas comme une invariance.
- **C17** (réentraînement sur les détections) : déjà couvert par FI-16 et N-053 point 5. Reste à ajouter un témoin tiré au hasard de même taille : sans lui, le duel de RC gagne mécaniquement sur les « échappées ».
- **C19** (lecture de F3) : levé par N-053, N-035 et R-509. Ajouter N-053 à la rubrique « Où » de FI-42.
- **Sous-propositions rejetées** : cellule « politique dormante » de CA (polarité inversée, A23) ; détecteur lexical positif comme arbitre (C05) ; contrôle « sans effet sur (ii) et (iv) » de CB (C06) ; placebo tiré dans le sous-espace principal (C11) ; aire partielle « sans borne dure » de RC (bornée ; Loftus s'y applique, p. 5, relu) ; témoin iv-nul (C08) ; « plafond » de capacité (C07 : c'est une borne basse).

---

## 5. Ajouts classés

### 5.a Les cinq ajouts de chaque modèle, passés à la vérification

| Rang | CA | CB | CC |
|---|---|---|---|
| 1 | Budget en unités de tâche, δ(dose) × fragmentation — **A01, retenu avec réserve** (amende FI-04) | Nul séquentiel sur trajectoires longues — **A05, A10 : déjà couverts** (N-007, T0.3 P8) | Indépendance et blanchiment autorégressif — **A05 couvert, A08 rejeté** |
| 2 | Nul « toujours valide » par permutation et dérive — **A05, A06 : déjà couverts** | Bases mécaniques et longueur — **A17 couvert (FI-26) ; J01** | Honnête à contexte contaminé — **A28, C05 : retenus, réécrits** |
| 3 | Cellule « politique dormante » — **A23 : rejetée (polarité)**, contrôles retenus | Interaction 2 × 2 sur échelle latente — **A14 : couvert (FI-30), à corriger** | Densité contre direction ; polarité logique — **A29 couvert ; F15 retenu** |
| 4 | Bases mécaniques et strates — **A17, A21, A22 : couverts ; J01** | Famille scellée et registre de sélection — **A27 couvert (N-054) ; C18 retenu** | Bruit comme canal d'élicitation — **F03 : rejeté** |
| 5 | Nul de co-élévation et base adaptative — **A15 couvert (FI-21) ; F01 couvert** | Organisme « connaît sans exercer » — **C08, A25, A26 : retenus** | Organisme (iv) par renforcement — **C09, C10 : retenus avec réserve** |

Sources des classements : CA § (f) l. 138-150 ; CB Q4 l. 114-126 ; CC § (d) l. 115-140 (cellules empreintées, annexe).

### 5.b Convergences et divergences

- **Convergence qui ne sert plus.** Les trois modèles mettent la validité du nul séquentiel en tête (CA rang 2, CB et CC rang 1). Le programme l'a déjà mesurée et corrigée : la règle de Ville atteint 0,21 à 0,35 au lieu de 0,05 sous effet d'épisode, le calibrage conforme sur épisodes entiers donne 0,046 à 0,055 (N-007 § 1, `resultats-T0.3-v1.md` P8, selon le vérificateur de A05). Il reste à écrire « toujours valide » au sens de N-007.
- **Convergence utile.** La famille (iv) a besoin d'un meilleur témoin (CA en conditionnel, CB et CC au rang 5). Les bases mécaniques (CA rang 4, CB rang 2) sont surtout couvertes ; leur table consolidée (J01) sert de liste de contrôle.
- **Divergences.** CA met seul le budget en tête (CB le renvoie après le rang 5, CC l'ignore). CC est seul sur le bruit et le blanchiment, tous deux rejetés. CA est seul sur la cellule dormante, rejetée. CB est seul sur l'échelle de l'interaction, couverte.
- **Ce qu'aucun des trois ne classe.** Les corrections de la lecture qu'a faite R-508 de ses propres sources (C01, C05 à C07, C11) ne sont dans aucun top 5, sauf C05 par CC ; la vérification les met en tête.

### 5.c Classement unique, après vérification

| Rang | Ajout | Candidats | Coût (illustratif) | Nature | Porté par |
|---|---|---|---|---|---|
| 1 | Réécrire la lecture de l'intention : lecture principale sur (ii) puis (iv), contre un témoin apparié en indication ; filtrage des positions en diagnostic, règle scellée, placebo de positions | C05, C06, A28 | écriture et processeur ; témoin déjà prévu (P-009) ; sensibilité du filtre : un organisme, devis | nœud (N-053 point 1) | CC (2), critiques de CA, CB, RA, RC |
| 2 | Famille (iv) : oracle textuel, témoin iv-K, porte préalable chiffrée, noteur de lignée disjointe ; plan soi/autre × sabotage/bénin si la porte passe | C08, C09, C10, A25, A26 | un à trois adaptateurs de plus que N-053 ; dizaines d'heures de carte | nœud (dépense) | CA (cond.), CB (5), CC (5) |
| 3 | Validité des sondes et des juges : tâches de contrôle, condition saillante, paires de négation, perplexité à deux lignées, honnête plus faible, strate « risque », formats de l'indication | F11, F12, F15, F13, A22, F14 ; liste J01 | processeur ; F14 et négations hors cache : quelques heures de carte, devis | proposer, défaut 48 h | CA (4), CB (2), CC (3) |
| 4 | Tests causaux et contrôlabilité : placebos multiples et dose-réponse, porte hors source, témoin sémantique et borne basse ; axe « utilité » de HC4 | C11, C12, C07, F06 | faible à modéré, sur devis pour la carte | nœud pour HC4 ; le reste, proposer | aucun top 5 ; critiques de CA, CC, RA, RB, RC |
| 5 | Lecture statistique de G1, E1.3, E1.6 : forme de δ(dose), composantes de variance, deux estimands de longueur, intra/inter-tâches, balayage de longueur, H6 audit coupé | A01, A11, A18, A19, A20, F02 | processeur | proposer, défaut 48 h | CA (1, A01), CB (via B1′), RC |

Ensuite, dans l'ordre : relecture des sources de R-508 et volet lignée (C01, C16, F07) ; registre de sélection (C18) ; porte de séparabilité comme garde de portée (C15) ; fiabilité des sondes pour la co-variation (A16) ; contrôles d'état des organismes verrouillés (A23), qui dépendent du GO sur 70 milliards.

---

## 6. Rejeté ou déjà couvert, une ligne par candidat

**Failles documentées**
- **F01** (déploiement adaptatif comme base manquante) : déjà couvert (base (i) de N-007 ; antériorité niveau 2 l. 77). Description fausse : pas de budget d'audit adaptatif, « we take away this affordance » (2411.17693 p. 2, relu). À citer dans le papier A comme origine de « distributed threat setting » ; un bras éventuel reste hors critère, exemples d'attaque appariés des deux côtés.
- **F03** (bruit comme canal bon marché contre le sous-rendement) : **rejeté**. Sur les organismes (iii) eux-mêmes, Taylor et al. le trouvent « unreliable and does not distinguish sandbagging » (2512.07810 p. 22, relu). Mesuré, ce serait une réplication citée. C'est N-013, et non N-015, qui a retiré le bruit sur les poids de H6. Citer « NeurIPS 2025, arXiv 2412.01784 » (p. 1, relu).
- **F04** (antériorité de Benton et al. pour l'environnement (a)) : déjà couvert. (a) se déclare dérivé de 2606.08892 (§ 6, P-008) ; Benton est classé voisin (antériorité niveau 2, l. 78 et 207). Reste une phrase de situation dans le papier A.
- **F05** (sape délibérée par le moniteur) : déjà couvert (R-508 angle mort 10, FI-14). Benton p. 25-27 ne manipule aucun cadrage banc d'essai contre production (vérificateur). À citer comme source « sape du surveillant » dans FI-14 et D8.
- **F08** (Poser comme détecteur) : déjà couvert (N-015 § 1). Le « pilotage » est mal attribué : son effet est « indistinguishable from injecting noise » (2405.05466 p. 2, relu).
- **F09** (conscience d'évaluation composite) : déjà couvert (N-053 point 3). SAD est comportemental, sans activations ; E7 tient.
- **F10** (stéganographie apprise) : déjà couvert (R-508 D9). Précisions : bits par millier de caractères (2310.18512 p. 1, vérificateur) ; ne jamais revendiquer que la paraphrase coupe tout canal (borne par l'entropie sémantique, 2402.07510v5 p. 10, relu).

**Angles morts**
- **A02** (dose divisible) : déjà couvert (P-015, « dose réalisée » ; FI-04). Ajouter à FI-33 la branche « exécution échouée ».
- **A03** (évaluateur aval de la lignée du juge) : déjà couvert (P-014 retire ce rôle au juge 8B). À écrire en règle au préenregistrement de G1 si A01 est adopté.
- **A04** (le dommage dépend de la répartition) : déjà couvert (FI-04). « À B fixé » exigerait de lire la sonde pour doser, ce que P-015 interdit.
- **A05** (nul toujours valide sous dépendance) : déjà couvert (N-007 § 1, T0.3 P8). Le centrage sur la moyenne de l'épisode annule la somme terminale : irrecevable.
- **A06** (permutations comme nul) : déjà couvert. Le calibrage sur épisodes entiers est valide quelle que soit la source de dépendance. Pour localiser : corrélation intraclasse et autocorrélation des résidus, nul apparié en position (simulation `sim_a06_a08.py` `f8b8c1e7…`, sortie `08dbc91f…`, illustratif).
- **A07** (règles de décision des duels) : déjà couvert (FI-27, FI-34, FI-39). Calculs confirmés (même sortie) : zéro faux positif sur 500 donne une borne haute bilatérale de 0,735 % ; quantile à 95 % pour 1 % : 9 sur 500. Trois régions préenregistrées sur intervalles.
- **A08** (blanchiment autorégressif) : **rejeté**. À taux de faux positifs réalisé égal, pas de perte de puissance propre (ρ = 0,6 : rappel 0,049 brut contre 0,044 blanchi). Au seuil de Ville, il ne rétablit pas la validité sous effet d'épisode : 4,2 % et 5,3 % pour α = 1 % (même sortie, illustratif).
- **A09** (planchers de l'agrégateur) : déjà couvert (N-004 L2, seuil exact ; FI-28). La référence du programme § 3 est mal attribuée : 2208.07610 est de Pérez-Ortiz, Lardy, de Heide, Grünwald ; déjà corrigé dans la note v3.
- **A10** (facteur commun) : déjà couvert (N-004, note v3 § 5, FI-25, FI-30, FI-33). Le test ne sépare pas sa cible (voir A11).
- **A12** ((ii) garde la consigne) : déjà couvert (R-508 angle mort 2, FI-07, N-053 § 2).
- **A13** (E1.4 vrai par construction) : déjà couvert (FI-33).
- **A14** (interaction sur échelle latente) : déjà couvert (FI-30). Corrections : d′ seulement sous un modèle binormal déclaré et contrôlé ; règle de lissage déclarée ; seul un motif ordinal ne dépend d'aucune échelle (Loftus 1978, p. 4-7, vérificateur ; p. 5 relu).
- **A15** (nul de co-élévation) : déjà couvert (FI-21). Le nul se construit avec la structure de partage du déploiement, jamais à partir d'un modèle d'indépendance (2604.01151 p. 16, vérificateur).
- **A17** (maximum et longueur) : déjà couvert (FI-26). Remède sans perte : calibrage conditionnel à la longueur.
- **A21** (signature du semis) : déjà couvert (N-029, P-009, P-015, FI-05). Prémisse fausse : le sabotage est produit par l'organisme, pas inséré par gabarit.
- **A22** (thème « risque » sous honnêteté) : déjà couvert (FI-29, DV-5). Verser la strate à FI-29 avec ses effectifs (calcul du vérificateur, illustratif : environ 240 actions par strate contre le taux nominal, 600 pour comparer deux strates).
- **A24** (épisodes non sabotés des saboteurs) : déjà couvert (FI-25). Ajouter le test prédictif restreint aux pas non sabotés, conditionné sur l'occasion, à l'intérieur d'un même organisme (précédent : 2507.12428 p. 1, vérificateur).
- **A27** (biais de sélection à G0) : déjà couvert (N-054 points 3-4). Nommer deux lectures : « biais sur les instances » et « généralisation hors recette ».
- **A29** (sondes de densité et plaidoyer honnête) : déjà couvert (EC.2, FI-34). Lire effet principal et interaction par famille de sondes.
- **A30** (géométrie au-delà du linéaire) : déjà couvert (§ 8.1, § 8.2, R-508 D7). L'ensemble de familles de D7 n'est pas repris par N-053 : question résiduelle.
- **A31** (sabotage qui imite l'erreur) : déjà couvert (§ 3, § 11, N-053 points 1-2). Question ouverte documentée dans les deux sens (Taylor p. 16-17 ; Boxo p. 1).
- **A32** (paraphrase qui dégrade l'honnête) : déjà couvert : c'est l'issue qui falsifie H6. Deux ajouts rapportés : faux positifs du juge sur sorties honnêtes paraphrasées ; placebo plancher sur la sortie de l'agent.
- **A33** (conscience d'évaluation par la nature de la tâche) : déjà couvert (N-053 point 3, facteur « contexte » ; R-508 E6).

**Critiques** : C02, C03, C04, C13, C14, C17, C19, voir § 4.b.

**Ajouts de synthèse, non vérifiés comme tels**
- **J01** (table des vérifications mécaniques et des strates honnêtes) : consolidation en grande partie couverte (N-029, P-013, FI-05, FI-26, FI-29). À utiliser comme liste de contrôle du préenregistrement de G1, jamais comme critère ; sa taille « 2 500 à 3 000 actions » suppose l'indépendance (A07).
- **J02** (aucun instrument construit contre l'un des bras comparés) : cohérente avec C10, A03 et FI-03 ; à joindre à la décision sur l'invariant (C10, C18).

---

## 7. Réserves

**Le III.3 a tourné, et il n'est pas fusionné.** La consigne de cette synthèse dit que le III.3 n'a pas tourné. Sur disque (R11), c'est inexact. Après ton mot « go leve le plafond » (R-512, vers 11:55 UTC), les trois ripostes ont tourné de 12:08 à 12:16 UTC, pour 2,92 USD (étage complet : 9,32 USD). Sources : `LISEZMOI-v2.md` (`af85329c…`) et `E3-T3-riposte-A|B|C.md` (`8db6e95c…`, `fa7fbb4b…`, `e06f4074…`, empreintes conformes). Les candidats fusionnés viennent des seuls III.1 et III.2 : cette synthèse ne couvre pas les ripostes. Je n'en ai lu que les intitulés : CA y accepte presque toutes les attaques (cellule dormante, témoin iv-nul et essaim Qwen « remplacés »), CB corrige ses duels, CC rectifie ses cinq ajouts. Le sens va dans celui de cette synthèse ; leur fusion reste à faire (routine, v2 de ce fichier).

**Références non vérifiées (R7).**
- Christiano 2021, précurseur du régime « menace distribuée » cité par Wen et al. p. 1 : non lu.
- Gasteiger et al. 2025, *Automated Researchers Can Subtly Sandbag* : billet sans PDF, non opposable.
- MacDiarmid et al. 2024 (saillance du déclencheur, R-508 « restant à lire » n° 8) et Hu et al. 2025 (valence des documents) : billets, à vérifier.
- CIAware-Bench, arXiv 2606.11063 : lu en résumé de recherche seulement.
- Outils statistiques cités sans PDF : effet de plan de Kish, Clopper-Pearson, rééchantillonnage par blocs, atténuation par la fiabilité, préblanchiment, corrélation écologique, VanderWeele 2010. À vérifier s'ils entrent dans un papier.
- Années : Tice et al. (v1 2024, publiée à NeurIPS 2025) ; Levinstein et Herrmann (arXiv 2023 ; « 2024 », version de revue, non vérifiée).
- Pièces internes non relues par certains vérificateurs : lot B FI-11, FI-36, FI-37 (selon les candidats) ; « F1 § 7 » ; « C16 » cité par F07 ; « A27 » cité par C18.
- Simulations A06, A08, A11 : synthétiques, illustratives ; ce ne sont pas des mesures des instruments.

**Désaccords entre modèles, et avec la vérification.**
- Cellule dormante : CA la classe 3e ; RB et RC renversent la polarité ; les PDF leur donnent raison.
- Bruit comme canal (CC, 4e) : rejeté par la source même des organismes (iii).
- Blanchiment (CC, 1er) : RA le croit coûteux en puissance ; la vérification rejette les deux lectures.
- D6 et E7 « réfutées » (CA) contre « mises en question » (RB) : D6 passe « en partie » (DV-5), E7 tient.
- Lignée : RA soutient deux effets de signes opposés ; un seul est sourcé (auto-préférence, sur des résumés).
- Coûts : CC se contredit (20 à 40 contre 30 à 50 heures de carte) ; CA sous-estime (A35) ; aucun n'est un devis.
- Statuts : CC marque [VÉRIFIÉ] son propre jugement (A34).

**Limites.**
- Trois modèles, dont deux du même fournisseur ; un tour de conception et un d'équipe rouge (ripostes non fusionnées) ; vérification par des sous-agents, probablement de la même famille (risque de FI-43).
- Je suis claude-opus-5-5, le modèle de CB et RB : un biais en faveur de B est possible. Un contre-lecteur d'une autre famille serait plus sûr (R2).
- « Déjà couvert » veut dire couvert sur pièce (programme, décisions, R-508, lot B), pas mesuré : ces points restent à préenregistrer.
- La fusion des candidats a été faite par des extracteurs ; des nuances des cellules peuvent manquer.
- Mes relectures vérifient la présence du passage cité sur la page empreintée, pas la lecture entière du papier.

**Contenu opérationnel, signalé et non reproduit.** Aucune cellule n'a été signalée. Dans les sources : 2312.06942 p. 13 (une politique d'attaque par collusion contre un moniteur) ; 2412.09565 p. 7-9 (procédés d'obfuscation des activations) ; 2607.25907 p. 1 et 6 (procédé d'optimisation d'entrées) ; 2512.07810 p. 3 et 17 (comportements distracteurs de l'équipe rouge).

---

## 8. Décisions proposées

**Décision 1 — La lecture de l'intention (N-053, point 1).**
- *Décision* : remplacer « la lecture filtrée est la lecture principale de toute revendication d'intention » par une lecture principale sur les organismes sans consigne dans le contexte ((ii), puis (iv)) et contre un témoin apparié en indication ; le filtrage des positions devient un diagnostic rapporté.
- *Enjeu* : la source du filtrage dit elle-même qu'il ne retire pas l'information propagée par l'attention (2509.21344 p. 5 et 7). Sans correction, toute revendication d'intention de G1 et du papier C est exposée au premier relecteur.
- *Options* :
  - (a) garder N-053 tel quel. Avantage : rien à rouvrir. Inconvénient : lecture principale contredite par sa source.
  - (b) lecture principale sur (ii) puis (iv), témoin apparié en indication dans les négatifs (FI-06) ; filtrage avec règle mécanique scellée et placebo de positions, en diagnostic. Avantage : conforme à la source, coût d'écriture. Inconvénient : dépend de (iv) (dépense) et de la réserve FI-07 sur (ii).
  - (c) (b), plus la sensibilité du filtre calibrée sur un organisme à signal lexical connu. Avantage : mesure l'écho directement. Inconvénient : un organisme de plus, devis.
- *Recommandation* : (b), confiance élevée ; (c) au devis de la phase 1.
- *Défaut* : nœud (lecture d'une revendication que tu as fixée dans N-053).

**Décision 2 — Les témoins de la famille (iv), avant son devis.**
- *Décision* : avant tout calcul de (iv), ajouter un oracle textuel lu sur iv-a et (ii), un témoin iv-K (même politique décrite comme celle d'un autre système), une porte préalable chiffrée (iv-S sabote plus que iv-K, iv-K comme iv-N), le mélange de données de préentraînement, et un noteur de récompense de lignée disjointe des bases boîte noire.
- *Enjeu* : le témoin « documents neutres » ne sépare l'intention ni de la saillance du réglage ni de la connaissance (2510.13900 p. 1 ; 2503.10965 p. 19) ; la dépense peut acheter une circularité.
- *Options* :
  - (a) N-053 tel quel : réglage sur documents, témoin neutre. Avantage : un adaptateur. Inconvénient : ne tranche pas.
  - (b) ajouts ci-dessus. Avantage : sépare propriété et connaissance pour un adaptateur de plus ; l'oracle est gratuit. Inconvénient : le rattachement à soi d'un secret reste confondu (A26).
  - (c) (b), plus le plan {la sienne, d'un autre} × {sabotage, secret bénin}. Avantage : sépare aussi le rattachement à soi. Inconvénient : deux adaptateurs de plus, coût non chiffré, faisabilité à 8 milliards incertaine (2309.00667 p. 1).
- *Recommandation* : (b), confiance moyenne ; (c) seulement si la porte de (b) passe.
- *Défaut* : nœud (dépense ; l'exigence de lignée disjointe touche aussi l'invariant de N-053 point 5).

**Décision 3 — HC4 et la condition « suppression consignée ».**
- *Décision* : exprimer la taxe de HC4 par profil d'accès (aucun retour, verdict, score, gradient, poids) avec un axe « utilité conservée » ; ajouter un témoin sémantique à la « suppression consignée » et la lire comme borne basse ; nuancer l'état de l'art v1 l. 154.
- *Enjeu* : une obfuscation partielle sans gradient, avec retour du score, est publiée (2412.09565 p. 9) ; la taxe ignore le coût en utilité (p. 23-24, un seul cas) ; le témoin aléatoire favorise d'avance l'écart (2505.13763 p. 6-7).
- *Options* :
  - (a) statu quo. Avantage : rien à rouvrir. Inconvénient : une affirmation inexacte de l'état de l'art, une revendication exposée.
  - (b) énoncé par profil d'accès avec l'axe « utilité », témoin sémantique, lecture en borne basse. Avantage : aligne HC4 sur ce qui est lu. Inconvénient : modifie l'énoncé retenu par N-013 § 3.
  - (c) témoins et lecture seulement, sans toucher l'énoncé. Avantage : pas de nœud. Inconvénient : la taxe garde un axe manquant.
- *Recommandation* : (b), confiance moyenne (le compromis en utilité tient sur un cas).
- *Défaut* : nœud (revendication).

**Décision 4 — Le paquet de contrôles de validité et de lecture statistique.**
- *Décision* : verser en bras rapportés, jamais en critères, aux préenregistrements de T0.7, G1, E1.1, E1.3, E1.6 et du papier C : F11, F12, F13, F14, F15, A22, A28, C11, C12, C15, A01, A11, A18, A19, A20, F02 (détail aux § 2 à 4).
- *Enjeu* : chacun ferme, à faible coût, une lecture rivale d'un résultat de sonde (surface, saillance, longueur, placebo, source des données). Sans eux, un positif reste attribuable à un artefact.
- *Options* :
  - (a) tout verser maintenant ; processeur pour l'essentiel, devis pour F14 et les négations hors cache. Avantage : prêt avant le scellement de G1. Inconvénient : préenregistrements plus lourds, plus de bras à contre-lire (R2).
  - (b) seulement ce qui touche G1 (F11, F12, F13, A11, A18, A19, A20, A28, C15) ; le reste en phase 1. Avantage : G1 plus tôt. Inconvénient : H6, H8 et le papier C attendent.
  - (c) rien. Inconvénient : lectures rivales ouvertes.
- *Recommandation* : (a), confiance moyenne à élevée.
- *Défaut sous 48 heures* : (a), sans la partie payante, qui attend un devis et ton GO.

**Décision 5 — Les appuis de R-508 et le volet lignée.**
- *Décision* : relire méthode et résultats des sources qui portent N-053 avant tout scellement ; retirer S7 comme motivation du juge Qwen (qui garde l'appui de D8) ; renvoyer le plan croisé agent × juge à la décision sur FI-13.
- *Enjeu* : 30 des 46 sources de R-508 ne sont lues qu'en p. 1, et S7 transpose mal sa source (2607.06596 p. 3, 13) ; sans second agent, l'interaction de lignée n'est pas estimable.
- *Options* :
  - (a) relecture et corrections notées. Avantage : quelques heures, aucune dépense. Inconvénient : la question de lignée reste sans mesure.
  - (b) (a), plus le plan croisé agent {Llama-3.1-8B, Qwen2.5-7B} × juge en phase 1. Avantage : interaction estimable. Inconvénient : changement de modèle, organismes et sondes sur Qwen, devis.
  - (c) (a), plus la seule matrice calibration × évaluation entre lignées pour les moniteurs entraînés. Avantage : c'est ce que Pinto mesure. Inconvénient : suppose aussi des organismes d'une autre lignée.
- *Recommandation* : (a) tout de suite, (b) jointe à la décision FI-13 ; confiance moyenne.
- *Défaut* : (a) sous 48 heures ; (b) et (c) : nœud (changement de modèle, dépense).

Hors des cinq : le registre de sélection (C18) et l'extension de l'invariant (C10, J02) touchent un invariant, à te proposer avec FI-23 ; la fusion du III.3 est une routine.

---

## Annexe — empreintes

**Pièces du tour et du dépôt** (sha256 complets ; chemins relatifs à `scratchpad/` ou au dépôt `controle-ia-travail/`).

| Pièce | sha256 |
|---|---|
| `collisionneur-audit-controle-v1/question-audit-controle-collisionneur-v1.md` | `ff7806a94aaf166cc5ed86129b89a13dc2d077d40ef20c3a55d0e692c70df489` |
| cellule `E3-T1-conception-A.md` | `b56408d944751eec225c665f1ca3041ede8a9f7006697581d1ac5e129188c589` |
| cellule `E3-T1-conception-B.md` | `793e2fbdc03012c3200c1064926dfc49f4cf0c7208691dd30864d351a71915b6` |
| cellule `E3-T1-conception-C.md` | `ad9ef0aa051534f938beb355d5428feb7ae0399dc6b7b0ebaf012492f4e37cd3` |
| cellule `E3-T2-redteam-A.md` | `bdcd67494108030e194a8f608c6bfa2cabfd78cd1a7fe11c522bc3ee0b695feb` |
| cellule `E3-T2-redteam-B.md` | `77dc16c062e7582c970c284b28e6f62b01036645e9ba8ae135d392c7a4114ad2` |
| cellule `E3-T2-redteam-C.md` | `a76f6385df334f49ba908f10cc0887523af6f236213a0ff5a23d5ffd3959bb1b` |
| cellules III.3 (non fusionnées) A, B, C | `8db6e95cf8f06f5d81892aa6daa8d93b8bd035dca333c90e60698aa86c6b832b`, `fa7fbb4b7778bb3a3123ca09a11983348fad7f2db7f2a19d1c087bc8c63a8b4f`, `e06f4074cfef0aa6c6017ce6c42ca743500ad068ff362ea15bc126ed3958b523` |
| `collisionneur-audit-controle-v1/LISEZMOI-v2.md` | `af85329c8376a39d1b6b89c47f4b805a732883b5e14f776232a23a226d045a0d` |
| `docs/notes/audit-controle-v1/audit-litterature-v1.md` (R-508) | `29b32f620cb2310fad83166fd4f2957b3ce43b1c3dea090834d8c28f86e4823b` |
| `audit-taif-v2/lot-b-conv-audit/failles-internes-v1.md` | `c854f23f45b7994bb514e0104b3ca828878de8badab33d61cf71b054b20203a6` |
| `docs/decisions/decision-N-053-v1.md` | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` |
| `docs/decisions/decision-N-054-v1.md` | `c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f` |
| `docs/programme-controle-ia-v2.md` | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` |
| `audit-taif-v2/scripts-lot6/sim_a06_a08.py` ; sortie `sortie-sim-lot6-v1.txt` | `f8b8c1e7aee3ad4c53c928bc5895747510b72bb8724ddbb1652015410a3ec62f` ; `08dbc91f98ce720e76cfa0b521a363889e41a597f0b4d21858ddacca3591cc3f` |
| `audit-lot7-scripts/sim_a11.py` ; `sim_a11b.py` | `b951a32632c1aeb6517c0a04b2e576b3345c224dac0381a3fc49b5a0f6b203c0` ; `c8836dae48c7f8235c7c65727f04649848fa36c7619b656151b64cb1ebf3a8f3` |

**PDF cités** (dans `audit-taif-v2/pdf/`, sauf mention ; « relu » = pages réextraites par moi, passage retrouvé).

| arXiv ou document | sha256 | Pages relues par moi |
|---|---|---|
| 2504.10374v1 (Ctrl-Z) | `5f802d679344fe5e15d1edd50e96245f3bdc054e69d1ff0880b077d173549211` | 7 |
| 2605.26047v2 (Retrying vs Resampling) | `947724f42324070fd47b1ecaf8c1bf9b2257df0e0c7f8822447241d3ea9a28fa` | 1 |
| 2412.09565v2 (Bailey et al.) | `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9` | 9, 24 |
| 2404.13076v1 (Panickssery et al.) | `e1466f5ade6144599fda01deafdd737b4623eaae273d71e4a0099d55b33189d3` | 6 |
| 2603.04582v1 (Khullar et al.) | `99832403ee73aca07b3e7fc9ef3448734917b76c7c9ecf23a10249059ea6ed90` | 1, 2 |
| 1909.03368v1 (Hewitt, Liang) | `5fc41d60b1a9b8974f6a28dae562b9d118ace511e833d0107c6013583945426a` | 2 |
| 2004.03061v2 (Pimentel et al.) | `1d5f43c042dd3c2f5824cfd0b953519e46efcec2e1585abda406d7f6e223b0f3` | — |
| 2003.12298v1 (Voita, Titov) | `4cabe3217d528cd8e6ddfbc52b3505eb424a49d228ecfebf23dcd751a11fc110` | — |
| 2312.10029v2 (Farquhar et al.) | `8f8b5e7ad4391e822cacd768216ea475f74ef1540c8e0d09f42d8662b0e4c834` | 1 |
| 2307.00175v1 (Levinstein, Herrmann) | `56ded298914bea3c9fe650a1549b41bd807d0f89031e919ec2b05bc1fc16fe11` | 13 |
| 2306.05685v4 (Zheng et al.) | `1574982845157569b85c1214bfa9987000384d7a5e3b5fbdcc5a29afec59cb81` | 1, 5 |
| 2310.11324v2 (Sclar et al.) | `997d46a1fdb83e3d09d0146f70e891bb1d8e8c49153404054bab61735db52aae` | 1 |
| 2407.12831v2 (Bürger et al.) | `badf34f0ae9eddd6c159ac8b637d66af5b3a939f296a78cc32e9755584dd1506` | 2 |
| 2310.06824v3 (Marks, Tegmark) | `9d64b7633b07e7b9ba462ad5c405150d1fb7e834e3a7feedfc7f6ee196b83a6c` | 5 |
| 2212.03827v2 (Burns et al.) | `20062bccb4769416c800ede71f4660f3fe2ad9921a7e1964604cd1048efd3d7a` | — |
| 2509.21344v2 (Boxo et al.) | `aaac4ff91c909f9e4363fe9c19bb0fc7c2a635bf91e13c178992411f2a25ee5c` | 5, 6, 7 |
| 2608.21664v1 (Kowalski et al.) | `7303ce0c3ad1d55149bcca92508c555dee908a67696511d8740d20b16e4bc995` | 5, 7 |
| 2505.13763v2 (Ji-An et al.) | `b878d094ed08fbc2e0dcdbde0ec3473eec2c8dcdfdadf2c227e7f85ef57ce899` | 6-7 |
| 2607.25907v1 (Mody et al.) | `437069bdff532ec3158c55659aa70bb9252e3aeee9b65890b488e6518befea8c` | 8 |
| Fiche système Claude Sonnet 4.5 | `d5d1ce28fea101ae3b201a5d4da100090a5d6b73246f7da820cafd7dbb11100e` | 104 du PDF |
| 2405.05466v2 (Poser) | `aa781893236e877a8f63e22249e77f454c8df6e2d82018fff3ca99456ad782c4` | 2 |
| 2607.06596v3 (Pinto) | `63181efe25f4115bdb8652aad12f6bdeade2f9e27f3c61811161e9278b885c8e` | 3, 13 |
| 2602.20628v2 (Gardner-Challis et al.) | `b7d4663ace86c1cf9f730509c39ef0138022ccf4b72ae7242892b3a7e5f9d0bf` | — |
| 2510.13900v3 (Minder et al.) | `e90e7757b2511ff9965d7330e8a63a25550e65e7c9ba7549c112b4221d33186e` | 1 |
| 2503.10965v2 (Marks et al.) | `6cea87ef4a49ef861ce9c37a3aeef3d82dced5c70028a5b924211bb27773b60a` | 19 |
| 2510.20487v5 (Hua et al.) | `969dd38af789f1333eb14cc9d03a4ac14b9afc999fa0ebf143f0c8431a704712` | 1 |
| 2309.00667v1 (Berglund et al.) | `d540ecb8aa64c68d5dc7e059233811b0266291988cb57613057715fbb32b237a` | 1 |
| 2511.18397v1 (MacDiarmid et al.) | `312b50556c2c2b5b9c8c2c53e11b509344ef92ab5bb954406a3d593b76938210` | 1 |
| 2503.11926v1 (Baker et al.) | `2547162c549d70e02beca2687903a8fce75fd950269a3ee479d5b8ebbb53ff38` | 1 |
| 2507.11473v2 (Korbak et al.) | `420d2c12a787b6903242b4369d3b6c5c7949e27fdfa62dd4c2dc5b4e2f399307` | 5 |
| 2512.07810v1 (Taylor et al.) | `77e64bcd88754f506890ee99dc5672284145a8705d27c5a63e4fc47330d28c8f` | 7, 17, 22 |
| 2405.19550v1 (Greenblatt et al.) | `ae7243da8e4ea849a09ed6bb464ff5bd76969f18401fa020514bb75e475ccaae` | 1 |
| 2502.03407v1 (Goldowsky-Dill et al.) | `a4820ad59ef9b294609aa11cbcc044c27835d5f433d7e79d6ae374f874bc2e2b` | 8 |
| 2603.19426v1 (Devbunova) | `095a5a7c251642f4aed6b1d1848176eac12f19f1c21a354c1f4838469b1788bb` | 3 |
| 2407.04694v1 (SAD) | `8983ad5249f3ee0d75f8f875fa438529b7ee4b300d1694681309380b660d8d7a` | — |
| 2404.04475v2 (Dubois et al.) | `977f595564a60227549bc12e9efaab5afb06c143d8d8e870dbd6121c962badcf` | 4 |
| 2510.09459v2 (FIPER) | `df815e61dc535ff248b020b151c7b94d7921fa8cca21e5041899a7a165e8a597` | — |
| 2601.11516v4 (Kramár et al.) | `c4a36db54c9d679a718a0e35b9cad09fa628d81f6174bb6e1d8c6b26a063d8bf` | 7 |
| 2506.10805v4 (McKenzie et al.) | `54bf555501b831d2505b05a0104d59cc0ab46dbb55516e6c0b7548e11db2b7d6` | — |
| 2602.22303v1 (Lee et al.) | `739ee7747236c1886131b6e33cc2f6833d3d7eb99b34f34732d79dc61aebaccc` | — |
| 2501.11120v1 (Betley et al.) | `63ed57332c0fab632f2e3d22601edb0987e74d1a08694c73ecbcfaa1112639a8` | — |
| 2505.14352v1 ; 2510.01070v2 (Cywiński et al.) | `1eaff0250644edb23d627e5f4d2ed4ca192c0cea4c13622d6c867f914f01a1be` ; `ed857d0212c74c35b32cbe0d8822fb73e4e5060fc0250a2ea9d0c22723e16aaa` | — |
| 2209.12711v1 (Jang et al.) | `02da07951e05df1810c41f2ebadd052f2054a542631e9477611da2005f044e58` | — |
| 2411.17693v1 (Wen et al.) | `13a93a48dcb373595709da1096984d308cd3cd17c3bf00602944a24abcc2c627` | 2 |
| 2412.01784v3 (Tice et al.) | `7fbe44ec6d764951f76d94f8d52cfcb7db89f1a130526462c46afc3f626d11a2` | 1 |
| 2410.21514v1 (Benton et al.) | `67f35893f1ebacb83407db92caf44c9b86d24da222ea5caee3f23184949cbb4f` | 27 |
| 2208.07610v2 (Pérez-Ortiz et al.) | `e9e5fd4e0096e3be7e7b07d083fd73818791feafd69a65676c289c0f63db6223` | 2 |
| 2312.06942v5 (Greenblatt et al., AI Control) | `999f7a92bb8c085799e68f3d88f491ad8a334f862ccf5b286e5c2766677864c0` | 7 |
| 2402.07510v5 (Motwani et al.) | `432581bdcdf22542025733261a4bf21f9200591a1b552c961caf7cc3701221c5` | 10 |
| 2310.18512v2 (Roger, Greenblatt) | `f482f2baff935088b53f30b22c0f7805af91a5ff458490b9f5274c2bf871f1ef` | — |
| 2507.12428v2 (Chan et al.) | `9c1543c38b3e389dff304e1a9bee2881d8d462110e193ea8d32e4589cdd247a2` | — |
| 2509.18058v2 (Panfilov et al. ; `audit-taif-v1/pdf/`) | `a742da8fed61af7b0ae8cb6bb8e6db7aa39ee3454bd39cc663885364e25a5467` | 23 |
| 2604.01151v5 (Rose et al. ; `pdf-lot8/`) | `02527fd4f62ad9b996669275f0837697cbe288b253c9aa521f72a10e6dcf1849` | — |
| 2609.03035v1 (Das et al. ; `pdf-lot8/`) | `5092b602b687f8efb76ede8983794e6686a82b139bdc7bcb04bc43fd8d56090d` | 3 |
| Loftus 1978, doi 10.3758/BF03197461 (`pdf-lot8/loftus1978.pdf`) | `70fd9cd238c7c5125e7446dfb7e561c13cdf288e314b5fbcbef79554e31c0a51` | 5 |

Relecture : script `synthese-relecture-v1/scripts/controle.sh`, listes `liste-v1.txt` et `liste-v2.txt`, pages extraites dans `synthese-relecture-v1/txt/` (tout sous `scratchpad/`).
