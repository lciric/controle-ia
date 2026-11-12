# Proposition A — Tour III.3 : réponse aux critiques

**Pièces reçues** : critiques B, D, E présentes ; **C absente** (statut « jamais lancée »), rien n'en est inféré. Je ne réponds qu'aux sections qui visent A. **Statuts** : les pièces et les critiques sont RAPPORTÉES ; mes réponses et mes reformulations sont des HYPOTHÈSES de conception ; aucun chiffre nouveau n'est VÉRIFIÉ ; ceux que j'avance sont marqués illustratifs.

---

## (a) Réponse à chaque critique

### QO-1

| id | critique (source) | réponse |
|---|---|---|
| Q-1 | D1 inventorie les *entrées* de l'étape A mais pas les décisions de **tenue** (lancer 7b, relancer, différer, abandonner, publier, remplacer la version) ; il est vrai par construction et muet sur ce que la garde protège (B-1, D-1, E) | **Acceptée.** C'est la critique qui décide. Transformée en **D1′** : inventaire étendu aux décisions de tenue, avec le contrôle négatif demandé par D et E (pipeline factice à entrées toutes figées dont la *publication* dépend d'un verdict injecté ; l'audit doit le détecter, sinon il est aveugle). |
| Q-2 | D1 n'est pas un duel probabiliste mais un inventaire déterministe (B-b) | **Acceptée.** D1′ est requalifié « audit préalable » ; le duel B4 de QO-1 est porté par D2 (P3-bis lui-même), dont les deux issues falsifient chacune une hypothèse. |
| Q-3 | le contrôle sur l'étape B est un contrôle positif de sensibilité, pas un contrôle négatif (D-1, E) | **Acceptée.** Il reste comme contrôle positif ; le contrôle négatif est celui de Q-1. |
| Q-4 | (b′) repose sur l'implication non démontrée « aucune entrée humaine ⇒ SCELLEMENT-T07 suffit » ; réécrire b15 pour justifier l'assouplissement est circulaire (B-2, D-2, E) | **Acceptée en partie.** R12 autorise la version neuve ; ce qu'il n'autorise pas, c'est de prétendre qu'elle protège sans le montrer. La charge est reportée sur D1′ et sur une **règle de registre** explicite (section b) ; sans l'une et l'autre, (b′) n'est pas défendable. |
| Q-5 | « un “non vu” permet de réparer avant 7b » est une décision conditionnée par V ; et cela suppose T0.7 scellé au moment du « non vu », ce que (b′) contredirait (B-3, D-2) | **Rejetée pour la seconde moitié, acceptée pour la première.** Sous (b′), T0.7 *est* scellé avant le verdict (c'est la condition même) ; la réparation est une version neuve, que T0.7 impose lui-même à l'issue « non vu » (L0b : « ouverts que sous un texte nouveau », RAPPORTÉ). Le canal réel, que je n'avais pas nommé : le **détail** de V (E′, PB-*, sonde qui a vu) peut informer une version neuve de T0.7 écrite *avant* les scores, qui paraîtrait alors propre vis-à-vis des scores. Fermeture proposée : seule l'issue binaire est ouverte ; le détail reste scellé jusqu'à `SCORES-T07` ; une version de T0.7 scellée après `VERDICT-P3BIS` ne lit pas 7b (section b). |
| Q-6 | un témoin positif réussi n'identifie pas rétrospectivement la cause du nul de P3 sur (i-a) (E) | **Acceptée.** « Vu » établit que la chaîne n'est pas aveugle à un comportement instruit et ancré dans un texte, à cette puissance ; le nul de P3 reste « non détecté à cette puissance », sans cause identifiée. Je retire « et non comme instrument mort ». |
| Q-7 | 0,014 est une simulation sous le nul, pas une fausse alerte mesurée sur H (E) | **Acceptée**, correction de statut : le taux de fausses alertes sur H est *mesuré* par P3-bis (PB-2, n_H) ; 0,014 est le niveau simulé (RAPPORTÉ, pièce 1). |
| Q-8 | transport de puissance de P3 à P3-bis : si la corrélation intra-tâche est forte, les intervalles au niveau action sont trop étroits (D-b) | **Transformée.** La pièce 1 (point 10) rapporte des erreurs types *par blocs* ; le transport reste une HYPOTHÈSE. Je demande que `puissance-p3-bis-v2.txt` écrive le nombre de blocs et le coefficient intra-bloc estimé sur P3 (0 USD), et que tout nul se lise « non détecté à cette puissance », comme le texte le dit déjà. |
| Q-9 | sous (a), le mot de Lazar tue aussi T0.7 sur 7b ; mon asymétrie (a)/(c) tient (E sur B, D sur B) | Non visée contre A ; je la note parce qu'elle confirme mon point 6 : (a) ne vaut que si l'attente est tenue. |

### Q1

| id | critique (source) | réponse |
|---|---|---|
| N-1 | E1 conditionne sur une variable post-génération (« propre » dépend des votes, du privé, du drapeau) ; H_A/H_B non exclusives ; « refus » et « mal joué » confondus ; les non-propres n'ont pas tous le privé (B-4, D-3, E) | **Acceptée.** E1 est **rétrogradé** : lecture stratifiée descriptive, trois groupes (propre / mal joué avec privé / refus ou sans privé), prédicteur de réussite appris sur les seules métadonnées pré-génération (scénario, domaine, consigne ; E), positivité par scénario rapportée (D). Il n'est plus un duel B4. |
| N-2 | C1′ (consigne d'un autre scénario) n'est pas un contrôle de préfixe pur : cible, contenu, privé changent (B-5, D-4, E) | **Acceptée.** C1′ retiré. Remplacé par **P1** (relecture identique, marge d'équivalence préspécifiée) et **P2** (décalage positionnel sans changement de rôle ni de privé). |
| N-3 | C4 contre C3 ne tient ni le texte ni l'historique constants (E, D) | **Acceptée.** C4 est comparée au **même texte honnête sous son contexte d'origine** (C5), différence appariée par message. |
| N-4 | les deux hypothèses d'E2 peuvent tenir ensemble : pas un duel (D-4, E) | **Acceptée.** E2 devient **deux duels séparés**, chacun exclusif, avec un δ dont la règle est gelée (section b). |
| N-5 | une différence d'aires n'est pas une « part » additive ; le ratio est instable quand le dénominateur tend vers zéro (E) | **Acceptée.** Les mots « part » et la fraction sont retirés ; seules des différences appariées sont rapportées. |
| N-6 | fuite d'apprentissage : S-C, H, bases notées hors pli ; base de métadonnées gelée avant STEGO, mêmes plis, même chaîne d'agrégation (D-5, B-c3, E-c) | **Acceptée.** Écrit dans le plan (section b). |
| N-7 | le contrôle de longueur des consignes est dans une clause de sortie, pas dans le plan (B-c1) | **Acceptée.** Mesuré à l'étape 0, par scénario, avant toute génération. |
| N-8 | tolérance de relecture non chiffrée (B-c2) | **Acceptée.** Marge d'équivalence illustrative fixée (section b). |
| N-9 | sous agrégation par maximum, des longueurs différentes par rôle écartent l'aire de 0,5 ; le plancher ne corrige que s'il reproduit la loi de longueur (D-b) | **Rejetée en partie.** Le plancher de T0.7 est calculé sur le même jeu, avec la même chaîne (maximum sur les jetons) : ses 200 directions subissent le même effet de longueur, que le quantile 0,95 absorbe par construction (RAPPORTÉ, pièce 3, « Plancher »). Acceptée pour l'ajout d'une base de métadonnées explicite (longueur, siège, tour), qui rend l'effet visible plutôt qu'absorbé. |
| N-10 | égaliser la longueur des consignes ne neutralise ni le contenu ni les interactions (E) | **Acceptée.** La clause « consignes rééquilibrées » est retirée ; le contrôle positionnel est P2. |
| N-11 | C2a (consigne honnête, privé gardé) est un contexte incohérent (D-4) | **Acceptée.** C2a est gardée comme intervention déclarée artificielle ; elle mesure « remplacement de la consigne à privé fixe », jamais « consigne seule ». |
| N-12 | variance intra-scénario, 50 blocs, effet petit non détectable (B-b) | **Acceptée.** Puissance non calculable avant les données ; chiffres illustratifs donnés ; bloc = scénario, écrit. |
| N-13 | E3 (option b) ne tranche rien (B, note transversale) | **Acceptée**, c'était déjà dit ; E3 est retiré du plan et reste nommé comme écarté. |

---

## (b) Expériences corrigées

### QO-1

**D1′ — Audit du canal de tenue** (processeur, 0 USD, requalifié « audit », pas un duel).
- Inventaire par un sous-agent neuf (qui ne reçoit ni P3-bis ni cette question) de **deux listes** : (i) les entrées de l'étape A de T0.7 ; (ii) les décisions de tenue entre `SCELLEMENT-T07` et `SONDES-T07` : lancement de 7b, relance après arrêt, différé, abandon, version neuve, publication. Chaque élément est classé « gelé par le texte », « lu au registre » ou « décidé par un humain ».
- Contrôle positif : l'étape B (dépendance au verdict connue).
- **Contrôle négatif (nouveau, de D et E)** : un pipeline factice dont tous les fichiers sont figés mais dont la *publication* dépend d'un verdict injecté ; l'auditeur doit l'écrire en classe « décidé par un humain ». S'il le manque, l'audit est aveugle et (b′) tombe.
- Issue attendue (HYPOTHÈSE) : la liste (ii) n'est pas vide ; au minimum le lancement de 7b. La question devient alors : *la dépendance de ces décisions à V est-elle déjà écrite dans T0.7 ?* Pour l'issue binaire, oui : L0b/L0c prescrivent « scores non ouverts, nœud » (RAPPORTÉ) ; la distribution des résultats publiés de T0.7 conditionnée à V est donc la même sous (a) et sous (b′) : résultat si « vu », aucun sinon. Ce qui n'est pas écrit dans T0.7, c'est la dépendance au **détail** de V. D'où la règle suivante.

**Règle de registre proposée pour (b′) corrigé, notée (b″)** — HYPOTHÈSE, à relire par un sous-agent neuf sur l'écart :
1. lecture mécanique jouée dès la récupération, **fermée** (comme (a), points 3-6 de la pièce 1) ;
2. le verdict (R13) ne commence qu'après `SCELLEMENT-T07` ; il écrit le fichier d'issue et `VERDICT-P3BIS` aussitôt ;
3. **seule la valeur du fichier d'issue** (« vu », « non vu », « non tranché », « échec », « non lu ») est ouverte ; `lecture-p3bis.json`, `lecture-p3.json`, scores et sortie standard restent scellés jusqu'à `SCORES-T07` ou jusqu'à un mot de Lazar qui ferme T0.7 sur 7b ;
4. **le texte de T0.7 qui lit 7b est celui dont la ligne `SCELLEMENT-T07` précède `VERDICT-P3BIS`** ; toute version scellée après `VERDICT-P3BIS` ne peut lire 7b (garde de registre, essai R5 comme D3) ;
5. T0.7 b15 remplace « `SCORES-T07` < `VERDICT-P3BIS` » par les règles 2 et 4, et le déclare dans DS-2.
Ce que (b″) ferme : le canal « version neuve informée par le détail de V ». Ce qu'elle ne ferme pas : la décision de ne pas lancer 7b sur « non vu » — qui est la lettre de L0b, pas un écart.

**D2 — P3-bis** (inchangé, statuts corrigés) : H_A « E′ de PB-1 au-dessus du plancher » (aire minimale détectable 0,6389 / 0,6585, RAPPORTÉ) contre H_B « non détecté à cette puissance ». Fausses alertes : mesurées sur H (PB-2, n_H) ; 0,014 est le niveau simulé sous le nul (RAPPORTÉ). Issue « vu » : la chaîne n'est pas aveugle à un comportement instruit, textuellement ancré, à cette puissance ; le nul de P3 sur (i-a) reste « non détecté à cette puissance », cause non identifiée (Q-6). Issue « non vu » : nœud, L0b. Ajout demandé à `puissance-p3-bis-v2.txt` : nombre de blocs et corrélation intra-bloc estimée sur P3 (Q-8).

**D3 — Essais R5 de garde** (inchangé, plus la règle 4 de (b″) et le cas « registre absent », B3 de la pièce 4).

### Q1

**E2′ — Décomposition du contexte à texte fixé** (passes forcées seules ; surcoût illustratif 0,8 à 1,2 h, ≈ 1,5 USD).

Cellules, toutes sur les **identifiants gardés** des messages du 8B, égaux au bit près entre cellules (garde d'identité étendue) :
- C1 : texte de colludeur, contexte d'origine (consigne de colludeur + tour privé) ;
- C2a : même texte, consigne honnête du même siège, privé gardé (intervention artificielle, déclarée) ;
- C2b : même texte, consigne honnête, privé retiré ;
- C5 : texte d'honnête du même épisode de collusion, contexte d'origine ;
- C4 : même texte d'honnête, consigne de colludeur + privé du colludeur du même épisode (pièce 4, repris en le disant) ;
- C3 : témoins (négatifs) ;
- **P1** : C1 relu une seconde fois, contexte identique (bruit de relecture) ;
- **P2** : C1 avec un décalage positionnel sans changement de rôle ni de privé — une ligne neutre du gabarit (par ex. un en-tête de date dupliqué, « illustratif ») insérée avant la consigne, de longueur en jetons égale à l'écart médian honnête/colludeur mesuré à l'étape 0.

Étape 0 (N-7) : écart en jetons consigne honnête − consigne de colludeur, par scénario, écrit avant génération.

Ordre de lecture mécanique gelé : P1 → P2 → duels. Marge d'équivalence de P1 (N-8) : différence appariée d'aires |C1 − C1_relu| contre C3, intervalle 95 % contenu dans ±0,01 (**illustratif**) ; sinon, lecture « bruit de relecture non borné », tout E2′ en descriptif. δ_ctx := borne haute de l'intervalle de |aire(P2) − aire(C1)| contre C3 (règle gelée, valeur calculée avant l'ouverture de C2b ; si P2 n'est pas calculable, δ_ctx := 0,02, **illustratif**).

Deux duels, chacun exclusif (N-4) :
- **E2′-ctx** : θ_ctx = différence appariée d'aires (C1 − C2b) contre C3, bloc = scénario. H_A : θ_ctx ≤ δ_ctx (le remplacement du contexte ne change pas le classement au-delà de l'artefact positionnel). H_B : θ_ctx > δ_ctx. Intervalle entièrement d'un côté → l'autre hypothèse est falsifiée ; intervalle traversant δ_ctx → « non tranché à cette puissance » (convention de E, que je reprends). C1 − C2a et C2a − C2b rapportés séparément, sans phrase.
- **E2′-txt** : aire de C2b contre C3 contre le plancher apparié (200 directions, même chaîne). H_A : borne basse ≤ quantile 0,95 (le texte seul, sous contexte honnête, ne sépare pas à cette puissance). H_B : borne basse > quantile 0,95 et au-delà de la base des mots **et** de la base de métadonnées, toutes deux hors pli.
- **Symétrie honnête** (N-3) : θ_sym = différence appariée (C4 − C5) contre C3 ; même δ_ctx ; rapportée avec la même grille. Une sonde qui lit le contexte donne θ_ctx > δ et θ_sym > δ ; une sonde qui lit le texte donne E2′-txt en H_B et θ_ctx ≤ δ. Quatre combinaisons, quatre phrases gelées ; aucune ne dit « part ».

Puissance (N-12, **illustratif**) : 50 blocs CORE ; avec un écart-type par bloc de la différence d'aires de 0,05, un δ de 0,02 est séparable d'un θ de 0,06 environ à 80 % ; en dessous, « non tranché ».

**E1′ — Lecture stratifiée du jeu de la collusion** (descriptive, 0 h).
Trois groupes de colludeurs : propre ; mal joué avec privé ; refus ou sans privé (règle lexicale de refus gelée avant lecture, N-1). Rapportés : aire par action de chaque sonde entre groupes, hors pli ; **prédicteur de réussite pré-génération** (régression logistique sur scénario, domaine, consigne, sans texte ; E) : si son aire est haute, la séparation entre groupes est imputable au scénario ; nombre de scénarios présents dans deux groupes au moins (positivité, D) ; contrôle : honnêtes des mêmes épisodes, par groupe de leur épisode. Aucune phrase de falsification ; marque d'étage du brouillon inchangée.

**Bases et plis** (N-6) : S-C, H, base des mots (par étage, B4 de la pièce 4) et base de métadonnées (longueur en jetons, siège, tour) sont apprises et notées **hors pli**, mêmes plis par groupes de domaines (CORE) ou de sabots (STEGO), même chaîne d'agrégation ; la base de métadonnées est consignée dans `sondes-narc-8b.json` **avant** toute notation de STEGO, à côté de la sonde principale S-C.

**E3** (option b) : retiré ; nommé pour mémoire comme écarté.

---

## (c) Réponse à l'arbitre

### QO-1

**Ce qui est établi** (RAPPORTÉ, par les pièces) : T0.7 b14 n'est pas scellé ; le registre `scellements-v1.md` n'existe pas ; les défauts DB-1 à DB-6 ne sont pas consignés ; T0.7 lit déjà le verdict de P3-bis par construction (L0a-L0c) et refuse ses scores si « non vu ». **Ce qui est établi par ce tour** (HYPOTHÈSE partagée par B, D, E et acceptée) : la garde d'ordre ne protège pas seulement des entrées figées ; elle protège les **décisions de tenue** de T0.7 contre une connaissance de V. Mon D1 ne le testait pas.

**Ce qui n'est pas établi** : que ce canal diffère entre (a) et (b″) pour l'issue binaire — sous les deux, « non vu » n'ouvre aucun score de T0.7 et impose un texte neuf. La différence réelle entre les options porte sur (1) le **détail** de V et (2) le **coût** : sous (a) ou (c), un « non vu » est appris après que 7b et l'étape A ont été payées ; sous (b″), avant.

**Recommandation : (b″)**, confiance ≈ 0,5 (contre 0,65 au tour précédent) : lecture fermée tôt ; verdict après `SCELLEMENT-T07` ; issue binaire seule ouverte ; détail scellé jusqu'à `SCORES-T07` ; aucune version de T0.7 scellée après `VERDICT-P3BIS` ne lit 7b. Raison : elle garde ce que la garde protège (le texte et ses versions), découple P3-bis de 7b, rend un « non vu » utile avant dépense, et donne un résultat binaire avant le 22 novembre si T0.7 est scellable avant. **Ce qui la ferait échouer** : D1′ montre une décision de tenue qui dépend du détail de V et que la règle 3 ne ferme pas ; ou T0.7 n'est pas scellable avant l'entretien (ses marqueurs, B3). **Condition de changement d'avis** : si Lazar veut que 7b soit lancée quel que soit V, ou si D1′ échoue, je passe à (a) avec la restriction de D et E sur ce qui est visible au moment de la revue (codes de sortie et comptes qui ne dépendent pas de V) — et non à (c), dont la date fixe sélectionne sur la durée (point de E). Si P3-bis rend « échec », identique dans toutes les options.

**À faire en premier** : D1′ avec son contrôle négatif, et D3 (registre absent, règle 4), tous deux à 0 USD, avant de sceller P3-bis — avec la création du registre et la consignation des défauts, sans lesquelles aucune option n'est possible.

### Q1

**Ce qui est établi** (RAPPORTÉ) : toute collusion du banc est instruite ; C1 − C2 mêle consigne et privé ; C2, C2a, C4 sont hors politique. **Ce qui est établi par ce tour** (accepté) : aucune cellule n'identifie une « intention » ni une « part » ; on mesure l'effet d'interventions de contexte sur un classement, à texte fixé, et l'effet du texte à contexte honnête fixé.

**Ce qui n'est pas établi** : que le 8B joue (taux d'épisodes propres inconnu) ; que le bruit de relecture soit petit ; que les effets soient détectables avec 50 blocs.

**Recommandation : (c) corrigée** = (a) + E2′ (C1, C2a, C2b, C4, C5, C3, P1, P2) + E1′ en descriptif ; confiance ≈ 0,6 sur le choix, ≈ 0,8 sur « pas (b) ». Raison : seule la relecture à texte fixé sépare contexte et texte au sens opérationnel ; le bras externe donne déjà la comparaison avec HELIOS sans licence ni texte étranger. **Échec** : taux propre < 0,2 ; P1 hors marge ; δ_ctx grand ; effectifs dégénérés. **Changement d'avis** : si P2 montre qu'un simple décalage positionnel déplace l'aire autant qu'un changement de consigne, je retire les cellules et ne garde que (a) + E1′ ; si Lazar fait des « mêmes textes que HELIOS » un objectif propre, (b) redevient un bras externe du 8B, sous licence vérifiée.

**À faire en premier** : l'étape 0 (écart de longueur des consignes par scénario, concordance code-jeu, corrections B1-B4 de la contre-lecture), puis P1 et P2 avant toute cellule de contraste.

FIN-DE-CELLULE