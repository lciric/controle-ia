# Lecture vérifiée — avis d'espèces seules sur la boucle de sélection génération à génération de l'organisme — v1

## En-tête

- **Lecteur** : sous-agent neuf, Fable 5.1 (`claude-fable-5-1`), lignée conv-audit. Je n'ai écrit ni la question, ni les faits servis, ni aucun des avis, ni la réponse propre de conv-audit.
- **Heure** (`date -u`) : lecture commencée `Sun Nov  1 16:33:34 UTC 2026` ; écriture commencée `Sun Nov  1 16:37:19 UTC 2026`.
- **Régime** : lecture seule sur processeur ; aucun appel de modèle, aucun réseau, aucun fichier existant modifié, aucun scellement, aucun commit. Rien lu sous `donnees/` hors les deux fichiers nommés ci-dessous. Ce fichier est neuf ; son scellement revient à l'appelant.
- **Statut des avis** : avis d'espèces consultées seules, sous GO ; ils ne tranchent rien. Cette lecture ne juge pas, ne recommande pas.
- **Empreintes SHA-256 recalculées (`sha256sum`) des fichiers lus** :

| fichier | sha256 | mots |
|---|---|---|
| `docs/notes/reponses-especes-seules-2026-11-01-v1/reponse-selection-generations-v1-argon-v1.md` (ci-après « A ») | `ae9938c106c527dcf2cb2f09347cc42d19fe0b425ab8d30ff9d1e972e88252dd` | 5 305 |
| `docs/notes/reponses-especes-seules-2026-11-01-v1/reponse-selection-generations-v1-kimi-v1.md` (« K ») | `12e1bee1743ebb6f298b21c09bd8c3e8356071404c17770d97343bf3079d4a8d` | 4 123 |
| `donnees/questions-3-novembre-v1/question-selection-generations-v1.md` (« Q ») | `c899221888d14e2df0640ac1b405cef286ca3bd84b45bec998519ac53fccbfcd` | 780 |
| `donnees/questions-3-novembre-v1/faits-selection-generations-v1.md` (« F », lu entier, en quatre morceaux) | `7c3404f477c79b3490d18677238be15456d6732648088a13a835d1213de7da17` | 17 253 |
| `…/scratchpad/relecture/reponse-conv-audit-selection-generations-v1.md` (« C », réponse propre de conv-audit, lue pour comparaison, non jugée) | `99544f60838318bd171e413b744136e8bd80b2e31268a3086da20226d626cec4` | 9 075 |

Les renvois « A l. n », « K l. n », « F l. n », « C l. n » désignent la ligne du fichier. « Pièce n » renvoie aux pièces de F (pièce 1 dossier factuel ; 2 intégration des proposeurs ; 3 programme v7 § 0 ; 4 lancement « (a) bis » ; 5 couche 1 v7 ; 6 cycle v5 ; 7 conception du pont ; 8 LISEZMOI du pont ; 9 programme v2 § 5 ; 10 N-013 ; 11 N-035). « RAPPORTÉ » : source bibliographique citée par l'avis, qu'aucune pièce ne sert en PDF ; je n'ai vérifié que la cohérence de l'identifiant avec les pièces ou, à défaut, sa forme ; rien n'est opposable (règle R7).

---

## 1. Avis d'Argon (A)

### 1.1 Chiffres et affirmations attribués aux pièces, recoupés

**Justes** (le chiffre ou l'énoncé figure dans la pièce citée, au sens cité ; « A l. → F l. ») : 3 exécutions de 120 s (8 → 131) ; parts des sorties du pont 5-15 / 45-60 / 30-45 %, axes 2 et 5 en sortie 3 (9-10 → 614-617) ; codes N1 à N11, N3 au pôle théorie, sortie 2 à spécification gelée (8, 11 → 585-606) ; m = 88 en couche 1 v7, 17 idées distinctes en course 1 (17 → 341, 170) ; seuil m/(α·k) (17 → 340-341) ; ≈ 150 épisodes seul, ≈ 300 à 17 fiches pour un effet 0,6 (18 → 539-540) ; couche 1 bis, richesse 2,28 pour un seuil 3,0 à 288 épisodes (19 → 534) ; `pari_apparie.ebh_pondere`, `cycle.membres_de_l_archive` (20, 100 → 524, 522) ; classe C sous K1-K5 (22 → 118) ; signal `qualite_generation.sans_dents` (23 → 343) ; témoins de force 0,5 sur 144 épisodes (24 → 531) ; 288 épisodes de T0.5 tous lus (35, 41 → 473) ; N-049 et N-053 (38, 35 → 208-209, 220-222) ; code N6 (47 → 651) ; vue `contenu` seule, 3 000 à 8 000 caractères (58, 64 → 485, 490) ; aptitude = sévérité, jamais signe ni ampleur (58 → 201-202) ; mémoire 0/31 et 11/40, `p_redite` 0,5, six générations (62 → 416-423) ; fusions inachevées archivées à part en v56 (62 → 136, 174) ; filles refusées à tort 31 → 4, 0 triviale sur 36 et 48 (65 → 400-403) ; catalogue des hypothèses par papier, H9 compris (79 → 926-948, 1065) ; G0 critères 1 et 5 (80 → 176) ; R-575 et N4 (89 → 45, 643-645) ; génération 0 : 5 / 10 / 3 (90 → 143) ; marchepieds 282/212 et 236/245, vivier de 60 (98-99 → 386-388, 413-414) ; 29 fiches, 17 idées, 12 doublons (101 → 170) ; course 1 ≈ 37 USD, plafond 160 USD (108 → 170, 679) ; pont 0,05-0,15 USD par fiche, 0,026 et 0,067 par appel, 1 à 3 min (109 → 673-676) ; « (a) bis » 136 appels, 5,89 USD, 11 rejeux, 15:37:35-15:42:20, réservation 1,5 USD, G0-F08 hors budget sous 7,5 USD (111-112 → 282, 296, 312-315) ; essai D-P5, 10 fiches, plafond 5 USD (113 → 734, 770) ; accord de rang 0,12, porte des juges 0,38, auto-préférence ≈ 1,8 (125, 137 → 118-119, 170) ; 1 fiche sur 10 en sortie 1 différée, 0 témoin vrai sur 20 (127 → 723, 352-355) ; 20 graines (138 → 376) ; identifiants arXiv des sept systèmes (148-151 → 782-788) ; duel à 100 USD (155 → 160).

**Inexacts ou imprécis** (l'attribution ou le chiffre s'écarte de la pièce) :

| affirmation d'Argon | où | ce que dit la pièce |
|---|---|---|
| « en couche 1 v7 sur 120 épisodes, une richesse de 21 passe le seuil par fiche » (l. 19) | A l. 19 | la richesse 21 est atteinte « sur 53 épisodes » (F l. 340) ; les 120 épisodes sont la taille de la banque (F l. 253, 533). Mélange de deux grandeurs, sens préservé |
| « vivier de 60 tâches en simulation cycle v5 » (l. 40) | A l. 40 | vivier de 60 **fiches** (F l. 386, 409) ; les tâches ne sont pas comptées dans la pièce 6 |
| « axes 1 à 7 » (l. 97) | A l. 97 | la pièce 1 cite les axes 1 à 5 et 7, l'axe 6 à part (F l. 42) ; la pièce 7 cite des axes 1, 4, 7, **8** (F l. 615). Le compte des axes n'est pas « 1 à 7 » |
| « écart de rendement de +30 % (282 contre 212) » (l. 138) | A l. 138 | la pièce 6 écrit +33 % (F l. 386) ; l'écriture « environ 25 % » de la l. 99 est le même rapport lu à l'envers (212/282), juste |
| « témoins faux (S-F1, S-F4, T3 à T6) » (l. 136) | A l. 136 | T3 à T6 sont des témoins de **renvoi** du pont (vide, sans mesure, théorème, sans chiffre : F l. 717-719), pas des hypothèses fausses au sens du juge ; S-F1 et S-F4 le sont (F l. 295) |
| « statut » des témoins S-V1, S-V4 « Pièce 4, Lectures » (l. 136) | A l. 136 | juste pour S-V1, S-V4, S-F1, S-F4 (F l. 294-295) ; la mention est groupée avec T1 à T6 qui viennent de la pièce 7 § g |
| « tests de mort s'exécutent en bac à sable même pour les fiches en sortie 2 (Pièce 7, § e) » (l. 137) | A l. 137 | la pièce 7 § e dit « en parallèle des tests de mort, cloisonnés » (F l. 683-686) ; elle ne dit pas explicitement que les fiches en sortie 2 passent aux tests de mort, c'est une déduction plausible du cloisonnement |

**Absents des pièces** (énoncés d'Argon sans appui dans F ; aucun n'est présenté par lui comme tiré d'une pièce, sauf mention) :

- la formule e-BH ordonnée $k^* = \max\{k : E_{(k)} \ge m/(\alpha k)\}$ (l. 17) : forme standard, cohérente avec F l. 340-341, mais la pièce ne l'écrit pas sous cette forme ;
- « Alpha-investing / LOND sur e-valeurs », « richesse d'alpha » (l. 20) : notions extérieures, RAPPORTÉ ;
- « Échelle de Blum-Hardt (Thresholdout / Ladder) » et « bruit laplacien » (l. 46) : extérieures, RAPPORTÉ ;
- « compilateur Lean en bac à sable » (l. 14) : la pièce 7 nomme Lean pour le code N3 (F l. 597), pas un compilateur en bac à sable ;
- la formule $\text{CPS}_g$ (l. 106) : construction d'Argon à partir de coûts unitaires qui, eux, sont dans F ;
- « bandit (UCB) » attribué à HypoGeniC (l. 149) : la pièce 7 dit « mises à jour » (F l. 788), rien sur un bandit ; RAPPORTÉ ;
- « modèle en îlots, sélection par score × longueur du programme » attribué à FunSearch (l. 152) : hors des pièces, RAPPORTÉ ;
- « $k \ge 3$ fiches en sortie 1 » pour la jugeabilité (l. 127) et « $\log_2(4)$ » : seuils d'Argon.

### 1.2 Réponse à chaque question posée

- **Q1** — Deux mécanismes exposés : la conjonction stricte à deux états (A l. 8-10), réfutée selon lui par l'extinction mécanique des 45 à 60 % de fiches en sortie 2 ; et un automate à trois états avec **file de dormance** (morte / promue / vivante en dormance réinjectée en génération g + k quand la banque existe, A l. 11-13). Pour les fausses découvertes : e-BH par génération (A l. 17-19), ou e-BH pondéré a priori par la sévérité du test de mort ou la puissance calculée par le pont, poids fixés avant l'épreuve (A l. 20-22). Garde : le signal « sans dents » suspend toute lecture négative (A l. 23).
- **Q2** — La génération g + 1 apprend le bruit d'échantillonnage de l'épreuve fixe par le canal étiquette-classement-preuve ; la garantie de Ville tombe (A l. 35). Règles : partition fraîche par génération, coût linéaire G × [144 ; 300] épisodes (A l. 38-41) ; ou banque fixe avec division du budget d'erreur entre générations, coût logarithmique mais seuil vite infranchissable (A l. 42-45) ; option manquante : seuil révélé seulement au-dessus de la meilleure richesse précédente plus un bruit (A l. 46).
- **Q3** — Transmission complète (survivantes et éliminées avec raison, A l. 58-60) contre **dissociation fonctionnelle** : les proposeurs ne reçoivent que les survivantes et un tableau agrégé des renvois par code ; l'archive des éliminées reste au noyau et à la mémoire prédictive (A l. 61-63). Option manquante : servir l'arbre syntaxique canonisé plutôt que le texte (A l. 64). Antériorités : MAP-Elites, recherche de nouveauté, FunSearch (A l. 68-70).
- **Q4** — Filtre conjonctif en quatre portes : survie empirique double ; nouveauté externe (R7, R8) et interne contre le catalogue gelé des hypothèses, avec la classe « affine Hx » pour une simple paramétrisation ; décisivité pour une porte nommée ; coût borné (A l. 77-81). Chaîne R1 → R2 → R13 (A l. 82-85). Condition : une table formelle des signatures prédictives des hypothèses (A l. 86). Option manquante : prendre les lois de H1 à H9 et HC1 à HC6 comme « nul informé » (A l. 88).
- **Q5** — Quotas par niche (axe × opérateur canonisé) et plafond de descendance par parent (A l. 97-99) ; ou pénalisation du nul d'archive par lignée (A l. 100-102, avec l'effet de masquage comme réfutation). Coût complet amorti par survivante neuve, coûts unitaires tirés des pièces (A l. 105-111) ; pire cas : famine budgétaire par réservation trop large (A l. 112).
- **Q6** — Dessin à deux bras (filtre complet contre juges-modèles seuls), évaluation finale commune sur épreuve fraîche (A l. 123-126) ; jugeable seulement si au moins 3 fiches passent en sortie 1 en génération 1, effet plancher sinon (A l. 127-128). Métrique : « par euro » biaisée contre le bras filtré ; préférer taux de survie en g = 2, richesse nette d'archive, capture des témoins (A l. 131-137). Pièce qui trancherait : calcul de puissance par simulation, 20 graines (A l. 138).
- **Q7** — Tableau de cinq familles (POPPER, HypoGeniC, AI Scientist et Agent Laboratory, co-scientist et Robin, FunSearch et MAP-Elites) avec l'élément transposable : agrégation en e-valeurs pour les tests de mort, indiçage par contre-exemples sur le développement, recherche arborescente confinée au développement, modèle en îlots (A l. 146-152). Condition : invariant N-053 sur tout emprunt (A l. 154). POPPER à lire d'abord sur PDF (A l. 156).

### 1.3 Sources citées (toutes RAPPORTÉ, aucun PDF servi)

| source | état | remarque |
|---|---|---|
| Wang et Ramdas 2022, JRSS-B 84(3) 822-852, arXiv 2009.02824 | RAPPORTÉ | identifiant arXiv identique à C l. 230 ; cohérent |
| Wasserman et Roeder 2009, Annals of Statistics 37(5A), arXiv 0704.1139 | RAPPORTÉ | hors des pièces |
| Ramdas, Grünwald, Vovk, Shafer 2023, Statistical Science 38(4), arXiv 2210.01948 | RAPPORTÉ | identique à K S4 |
| Dwork et al. 2015, « The reusable holdout », Science 349(6248) 636-638, **arXiv 1411.2664** | RAPPORTÉ, **suspecte** | C l. 228 associe l'article de Science à arXiv 1506.02629 ; l'identifiant 1411.2664 désigne, de mémoire, un article compagnon (« Preserving statistical validity in adaptive data analysis »). Le couple titre-identifiant est à vérifier |
| Blum et Hardt 2015, ICML, PMLR 37:1006-1014, arXiv 1502.04585 | RAPPORTÉ | identique à C l. 229 |
| Mouret et Clune 2015, arXiv 1504.04909 | RAPPORTÉ | identique à K S5 et C l. 139 |
| Lehman et Stanley 2011, Evolutionary Computation 19(2), PMID 20868264 | RAPPORTÉ | K donne un DOI, A un PMID ; non recoupés |
| Romera-Paredes et al. 2024, Nature 625(7995) 468-475, DOI 10.1038/s41586-023-06924-6 | RAPPORTÉ | identique à K S8 |
| Pugh, Soros, Stanley 2016, Frontiers in Robotics and AI 3:40 | RAPPORTÉ | identique à K S7 |
| Fontaine et al. 2020, GECCO, arXiv 1912.02400 | RAPPORTÉ | hors des pièces, seule chez Argon |
| POPPER 2502.09858 ; HypoGeniC 2404.04326 ; AI Scientist 2408.06292 ; v2 2504.08066 ; Agent Laboratory 2501.04227 ; co-scientist 2502.18864 ; Robin 2505.13400 | RAPPORTÉ | identifiants égaux à ceux de la pièce 7 § i (F l. 782-788), eux-mêmes « à vérifier sur PDF » |

Aucun chiffre d'un de ces papiers n'est repris par Argon (il le dit, A l. 144).

### 1.4 Ce que l'avis ne répond pas

- Q1 : le sort chiffré d'une fiche « non concluante » au test de mort (ni morte ni survivante) n'est pas distingué de la dormance ; la pièce 1 § 9.2 (F l. 131) prévoit pourtant ce troisième verdict.
- Q1 : le contrôle **cumulé** des fausses découvertes sur plusieurs générations n'est traité qu'en Q2 (budget divisé), pas comme question de garantie globale.
- Q2 : le coût en **dollars** d'une tranche n'est pas estimé (seulement en épisodes).
- Q3 : la question « transmettre le rang ? » reçoit une réponse implicite (le classement est transmis en mécanisme A, A l. 58), sans discussion de son statut de preuve.
- Q5 : « compter le temps » (minutes d'horloge, heures de carte) apparaît dans la formule comme postes nommés, sans unité séparée des dollars.
- Q6 : aucune prédiction signée ni critère de lecture gelé pour l'ablation ; aucun bras de comparaison « sélectivité égale ».
- Q7 : « que faut-il reprendre **tel quel** » reçoit des composants, pas de système ; la programmation génétique avec test (nommée dans Q) n'est pas traitée.
- Aucune confiance chiffrée n'est donnée par question (le format du tour 1 la demande) ; aucune « option retenue » (cohérent avec « sans recommandation »).

---

## 2. Avis de Kimi (K)

### 2.1 Chiffres et affirmations attribués aux pièces, recoupés

**Justes** (« K l. → F l. ») : tests de mort codés, jamais activés, trois verdicts (7 → 131-132) ; pont non intégré, épreuve entièrement lue (8 → 473, 858-862) ; « (a) bis » tautologique, « pas de dents » (10 → 285-287, 342) ; la garantie de 5 % porte sur le juge (12 → 249-250, 121) ; indécise : test plus puissant ou retrait après deux essais (25 → 202-203) ; sorties du pont, N1-N11, comptes agrégés (33-35 → 581-612) ; « une fiche, une loi » (45 → 574-575) ; ≈ 150, 300, 560 et réserve 4 (49 → 539-540, 814) ; 88 fiches, 0 promotion, 0 témoin vrai sur 5 (49 → 350-355) ; lecture fausse partagée par deux traducteurs (55 → 636-637) ; D-P4 (b) (68 → 764-766) ; 288 épisodes lus, aucune épreuve disjointe (77 → 534-535) ; tâches fraîches (77 → 208-209) ; juges : cohérence entre champs seulement (105 → 120) ; archive contre le biais du survivant (107 → 211) ; N2 sur la forme (109 → 596) ; « non trouvée » ≠ vierge (133 → 682-683) ; référentiel avec HC6, L, T, Tr, H4′, N-013 sans retrait, H9 sous réserve (137 → 929-946, 962, 1065) ; R1, R2, R13 (139 → 128) ; aucune fiche sortie, aucune porte franchie (145 → 53, 171, 176) ; tirage domaine × opérateur (159 → 205-206) ; marchepieds en monde construit, lignées réelles non mesurées (161 → 386-388, 441-446) ; coûts du pont supposés (184 → 674, 813) ; « échec qui ne coûte presque rien » (188 → 254-255) ; K ≥ 3 générations (210 → 209-210) ; deux témoins vrais en monde tautologique, pas de dents (218 → 280-287, 342) ; lois vraies construites par le script (223 → 441-446).

**Inexacts** : aucun chiffre attribué à une pièce ne s'en écarte. Deux imprécisions de portée :

- « la seule banque réelle disponible » (K l. 8) : la pièce 7 parle « des seules banques d'épisodes du pôle », au pluriel (celles de T0.5, 13 moniteurs ; F l. 472-473) ; le sens (une seule famille de banque, toute lue) tient.
- « le rang de course n'est pas une preuve expérimentale » (K l. 105) : juste, mais la pièce 1 § 1.2 point 11 prévoit bien de transmettre le classement (F l. 52) ; Kimi ne le dit pas.

**Absents des pièces** : Kimi n'avance aucun chiffre extérieur aux pièces. Ses seuls apports non sourcés sont des catégories (deux axes empirique × testabilité, K l. 20-35 ; trois ratios de coût, K l. 165-180) et ses confiances (0,88 ; 0,93 ; 0,76 ; 0,82 ; 0,72 ; 0,86 ; 0,61), qui sont les siennes.

### 2.2 Réponse à chaque question posée

- **Q1** — Trois états restent insuffisants ; représentation à **deux axes** : empirique (réfutée / non concluante / non promue / promue) et testabilité (jugeable / en attente d'épisodes / renvoi N1-N11) (K l. 20-35). Survivante héréditaire = test de mort survécu **et** promue **et** correspondance fiche-loi démontrée ; la non testable est archivée gelée, hors du dénominateur (K l. 35). e-BH valide sous dépendance, à conditions : famille et m fixés avant lecture, toutes les lois comptées, aucune conversion des verdicts des juges ou des tests de mort en e-valeurs ; la puissance vient de l'effectif, pas du contrôle (K l. 41-49) ; un contrôle par génération ne donne pas un contrôle cumulé (K l. 51). Confiance 0,88.
- **Q2** — Même épreuve : la génération 2 apprend l'épreuve, qui devient un développement indirect (K l. 66) ; la réutilisation déclarée n'est plausible que pour une fiche indépendante des verdicts, pas pour un héritage adaptatif (K l. 68). Partie jamais vue par génération ; banque croissante valide si seul le segment neuf sert d'épreuve ; rotation insuffisante ; réutilisation exploratoire seulement (K l. 72-75). Coût : produire des unités neuves pour chaque génération, témoins compris (K l. 77). Confiance 0,93.
- **Q3** — Séparer ce qui est conservé (archive probatoire complète, K l. 94-103) de ce qui est servi ; l'aptitude est la sévérité, le rang reste métadonnée d'audit (K l. 105) ; pour les éliminées, une vue minimale (signature, cible, portée du refus, code) plutôt que le texte intégral (K l. 107) ; « même engagement réfuté » ne doit pas devenir « domaine interdit » (K l. 109). Antériorité : archive pour la diversité, preuve pour la survie ; la nouveauté seule ne valide pas (K l. 113-117). Confiance 0,76.
- **Q4** — Quatre conditions : identité probatoire ; nouveauté revendicable ; décisivité avec une porte nommée **avant** l'expérience et une règle pour chaque issue ; coût total borné (K l. 132-135). Le référentiel ne se limite pas à H1-H9 et HC1-HC5 (K l. 137). Le lecteur R13 ne peut pas établir la nouveauté bibliographique : deux contrôles distincts (K l. 139). Option manquante : la sortie comme **restriction ou réfutation** d'une hypothèse existante (K l. 143). Confiance 0,82.
- **Q5** — Deux niveaux de garde : généalogique (concentration des descendants, part de la lignée maximale) et fonctionnel (niches par cible, domaine, opérateur, type de preuve) ; descripteurs fixés avant les résultats (K l. 156-159). Trois ratios distincts (par promue, par survivante neuve, par sortie) ; numérateur complet, unités non convertibles séparées, dénominateur en idées distinctes (K l. 165-182). Option manquante : coût par élimination correcte (K l. 188). Confiance 0,72.
- **Q6** — Non jugeable si chaque bras a sa propre définition de survie ; conditions : même population, budget et arrêt déclarés, répétitions indépendantes de la boucle entière (les graines ne font pas la puissance), adjudication finale commune sur épreuve indépendante, témoins dans les deux bras, zéro survivante dans les deux bras = non concluant (K l. 198-208). Métrique : idées distinctes, nouvelles et confirmées sur l'épreuve commune, par coût total, avec fausses promotions, rappel des témoins, taux de non-conclusion et diversité (K l. 216). Option manquante : bras **filtre aléatoire de même sélectivité** (K l. 222). Confiance 0,86.
- **Q7** — Aucun système repris comme boucle complète ; tableau de neuf familles avec l'élément transférable et ce qui n'est pas acquis (K l. 232-242) ; l'élément « tel quel » est mathématique (e-valeurs, e-BH) (K l. 244). Option manquante : une base de comparaison **non agentique** (recherche évolutionnaire simple, même évaluateur, même budget) (K l. 248). Confiance 0,61 tant que les PDF ne sont pas lus.

### 2.3 Sources citées (toutes RAPPORTÉ, aucun PDF servi)

| source | état | remarque |
|---|---|---|
| S1 Wang et Ramdas 2022, DOI 10.1111/rssb.12489, arXiv 2009.02824 | RAPPORTÉ | identique à A et C |
| S2 Vovk et Wang 2021, Annals of Statistics 49(3), arXiv 1912.06116 | RAPPORTÉ | seule chez Kimi |
| S3 Wasserman, Ramdas, Balakrishnan 2020, PNAS 117(29) | RAPPORTÉ | l'inférence universelle est nommée par la pièce 1 § 6 (F l. 121) sans référence ; seule chez Kimi |
| S4 Ramdas et al. 2023 | RAPPORTÉ | identique à A |
| S5 Mouret et Clune 2015 ; S6 Lehman et Stanley 2011 (DOI 10.1162/EVCO_a_00025) ; S7 Pugh et al. 2016 ; S8 Romera-Paredes et al. 2024 | RAPPORTÉ | identiques à A (sauf le DOI de S6, non recoupé) |
| S9 Koza 1992, MIT Press, ISBN 978-0-262-11170-6 | RAPPORTÉ | seule chez Kimi ; programmation génétique, nommée dans Q |
| S10 à S14 (AI Scientist v1, v2 ; Agent Laboratory ; co-scientist ; Robin) | RAPPORTÉ | identifiants égaux à la pièce 7 § i |
| S15 POPPER, titre « POPPER: A Framework for Rigorous Hypothesis Validation with LLM Agents » | RAPPORTÉ, **suspecte** (signalée par Kimi lui-même : « titre et liste complète des auteurs à contrôler ») | la pièce 7 ne donne pas de titre ; le titre proposé ne correspond pas, de mémoire, à celui de l'article 2502.09858. À vérifier sur PDF |
| S16 HypoGeniC 2404.04326 | RAPPORTÉ | égal à la pièce 7 |

Aucun chiffre de ces papiers n'est repris.

### 2.4 Ce que l'avis ne répond pas

- Q1 : aucun mécanisme chiffré pour « sans tuer la puissance quand les fiches sont peu nombreuses » au-delà du constat que la puissance vient de l'effectif ; ni pondération, ni pari à fraction, ni niveau.
- Q2 : aucun ordre de grandeur du coût en données (épisodes par génération) ; seulement sa nature.
- Q3 : « quelle antériorité » reçoit trois familles sans FunSearch ni programmation génétique à cet endroit (ils apparaissent en Q7).
- Q4 : « qui la lit » : le lecteur R13 est nommé, sans dire d'où vient sa famille de modèle ni ce qu'il reçoit.
- Q5 : aucune règle numérique de garde (quota, part, indicateur) ; les descripteurs sont nommés, pas les seuils.
- Q6 : aucune estimation de l'effectif nécessaire ; l'analyse de puissance est renvoyée au préenregistrement.
- Q7 : « que faut-il reprendre tel quel » : réponse « rien d'agentique », sans mécanisme concret à copier hors e-BH.

---

## 3. Réponse propre de conv-audit (C), notée à part, non jugée

Pour la comparaison seulement : cinq états (morte, non concluante, en attente d'épisodes, hors pôle, promue), seule la promue se reproduit (C l. 22-25, 52-60) ; e-BH ne tue pas la puissance à 20-40 fiches mais coûte +45 à +57 % d'épisodes ; le pari à fraction est le levier (C l. 26-29, 269-285) ; banque croissante à tranches rétrogradées, ≈ 330 épisodes par génération à effet 0,6 (C l. 30-33, 94-108) ; états servis, pas de rangs ; la mémoire refuse (C l. 121-127) ; règle de sortie à quatre conditions dont la malédiction du vainqueur, lecteur R13 d'une autre famille, référentiel élargi à HC6, L, T, Tr (C l. 146-162, 355-368) ; lignées tracées, quota d'un tiers, 30 % d'immigrants, nombre effectif de lignées (C l. 174-182) ; ablation à 20-40 fiches non jugeable, témoin interne d'immigrants, bras de comparaison « parents choisis par les juges » (C l. 194-213) ; témoin de sévérité par permutation pour les tests de mort, e-processus de mort (C l. 82-87) ; POPPER et LLM-SR les plus proches (C l. 218-235). Tous les chiffres de C viennent de sa propre simulation, annoncée exploratoire (C l. 525-559, réserve 1).

---

## 4. Pistes générales consensuelles

Accords entre A et K ; la position de C est notée à part entre crochets.

1. **Plus de deux états.** A rejette la conjonction stricte à deux états (extinction mécanique, A l. 9-10) et propose la dormance ; K rejette même trois états et sépare l'axe empirique de l'axe testabilité (K l. 20-35). Les deux archivent la fiche non traduisible avec sa spécification gelée, sans qu'elle se reproduise ni compte au dénominateur (A l. 11 ; K l. 35). [C : cinq états, même règle « seule la promue se reproduit », C l. 52-60.]
2. **e-BH par génération, valide sous dépendance, m fixé avant toute issue ; aucun contrôle cumulé sur la suite des générations sans règle supplémentaire.** A l. 17-18 et l. 42 ; K l. 41-51. [C : même constat, contrôle en ligne jugé inutile tant que la promotion est un criblage, C l. 286-288.]
3. **Sur la même épreuve, la génération 2 apprend l'épreuve ; la garantie tombe ; il faut une partie jamais vue par génération.** A l. 35-41 (coût linéaire en épisodes) ; K l. 66-77. Les deux citent la règle N-049 des tâches fraîches (A l. 38 ; K l. 77) et le fait que T0.5 est entièrement lue. [C : banque croissante à tranches rétrogradées, C l. 94-108.]
4. **Rotation ou réutilisation : exploratoires au mieux.** A : banque fixe avec pénalité vite infranchissable (A l. 42-45) ; K : rotation insuffisante, réutilisation déclarée non confirmatoire (K l. 74-75). [C : réutilisation corrigée par transcription comme repli chiffré seulement, C l. 113-115.]
5. **Héritage : servir aux proposeurs une vue réduite, garder l'archive complète au noyau.** A, mécanisme B (survivantes et agrégats, éliminées au noyau, A l. 61-63) ; K (vue minimale des éliminées, archive probatoire conservée, K l. 94-107). Les deux nomment le risque d'ancrage et la fuite par le texte intégral. [C : titre et code de raison seuls, la mémoire refuse, C l. 121-130.]
6. **L'aptitude héritée est la sévérité, jamais le signe ni l'ampleur** (A l. 58 ; K l. 105). [C : idem, « états, pas des rangs », C l. 121.]
7. **Antériorité évolutionnaire commune : MAP-Elites, recherche de nouveauté, FunSearch ; la nouveauté ne vaut pas preuve** (A l. 68-70, 152 ; K l. 113-117, 241-242). [C : même liste plus AlphaEvolve, ShinkaEvolve, machine de Gödel darwinienne, C l. 336-349.]
8. **Sortie vers le programme : quatre conditions écrites, dont nouveauté interne contre un référentiel élargi (HC6, L, T, Tr, H4′, H9) et décisivité pour une porte nommée ; lecture par un lecteur neuf R13 séparé.** A l. 77-85 (catalogue par papier) ; K l. 132-139. Les deux séparent nouveauté bibliographique et verdict R13. [C : quatre conditions aussi, signatures par le pont, C l. 146-162.]
9. **Une table des signatures des hypothèses du programme** pour que la nouveauté interne ne dépende pas d'un jugement libre : A l. 86 (« table formelle des signatures prédictives ») ; K l. 142 (« table de correspondance avec toutes les revendications »). [C : passer H1 à H9 et HC1 à HC6 par le pont, C l. 167-170.]
10. **Diversité : niches fonctionnelles (axe, opérateur, cible) et contrôle de la descendance par lignée ; MAP-Elites comme mécanisme ; l'avantage des marchepieds n'est montré qu'en monde simulé.** A l. 97-99 ; K l. 156-161. [C : quota d'un tiers, immigrants, nombre effectif de lignées, C l. 174-182.]
11. **Coût : numérateur complet (données comprises), dénominateur en survivantes uniques ou idées distinctes ; les coûts du lancement « (a) bis » et du pont sont des ordres de grandeur supposés.** A l. 105-111 ; K l. 182-184. [C : grand livre par rôle, intervalle de Poisson, C l. 178-182.]
12. **Ablation : effet plancher si la génération 1 promeut moins de 2 ou 3 fiches ; adjudication finale commune sur épreuve fraîche ; « survivantes neuves par euro » insuffisante comme critère principal.** A l. 126-128, 131-132 ; K l. 206-208, 214-216. [C : « non jugeable » déclaré d'avance sous 3 promues, test exact de Fisher sur la part promue, C l. 194-213.]
13. **Les témoins plantés valident le mécanisme, ils ne sont pas la valeur d'une découverte** : K l. 218 explicitement ; A les range dans les métriques de validation (capture, A l. 136) tout en les comptant comme métrique, ce qui est une divergence de degré. [C : « ils ne sont pas la métrique », C l. 206-207.]
14. **Q7 : POPPER est le voisin le plus proche, à lire en premier sur PDF ; aucun système publié n'est repris comme boucle complète ; l'invariant N-053 borne tout emprunt.** A l. 148, 154, 156 ; K l. 238, 244, 250. [C : POPPER et LLM-SR, C l. 234-239.]

Divergences notées (sans jugement) : A transmet le classement aux proposeurs dans son mécanisme A (A l. 58) là où K en fait une métadonnée d'audit (K l. 105) ; A chiffre un coût en épisodes par génération (A l. 39), K non ; A pondère l'e-BH par la sévérité du test de mort (A l. 20), K refuse toute conversion des verdicts des tests de mort en e-valeurs (K l. 47) ; A tient le dessin à deux bras pour jugeable sous condition d'effectif, K exige des répétitions de la boucle entière (K l. 204).

---

## 5. Pistes originales (une seule source)

**Argon seul :**

- File de **dormance** avec réinjection en génération g + k dès que la banque ou le moniteur requis existe, intégrité du gel maintenue entre g et g + k (A l. 11-13).
- Évaluation **stratifiée par canal** : les fiches en N3 (preuve) jugées par un vérificateur formel plus un test de mort par simulation, hors du juge statistique (A l. 14).
- **e-BH pondéré a priori** par la sévérité du test de mort ou la puissance calculée par le pont, poids mesurables avant l'épreuve ; ou budget d'erreur séquentiel entre générations (A l. 20, 42).
- Garde mécanique : le signal « sans dents » **suspend l'interprétation négative** des éliminations de la génération (A l. 23).
- **Échelle à révélation bruitée** pour le juge figé sur épreuve fixe : la survie n'est révélée que si la richesse dépasse la meilleure richesse précédente d'une marge bruitée (A l. 46).
- Garde contre la fuite par recombinaison : exiger le nul des filles v2 conditionné sur les prédictions des parents, codes N6 (A l. 47).
- **Élagage contrefactuel** : servir l'arbre syntaxique canonisé des survivantes plutôt que leur texte, contre l'ancrage stylistique (A l. 64).
- Expérience contrôlée en passe « tableau » : survivantes seules contre survivantes plus éliminées, taux de redites et diversité d'opérateurs (A l. 66).
- Classe « **affine Hx** » pour une fiche qui ne fait que paramétrer une loi déjà au programme (A l. 79).
- Les lois de H1 à H9 et HC1 à HC6 **comme nul informé** du pôle pour tester une candidate (A l. 88).
- **Pénalisation du nul d'archive par lignée** : chaque survivante entre dans le nul de ses sœurs, avec l'effet de masquage nommé comme réfutation (A l. 100-102).
- **Famine budgétaire** par réservation (1,5 USD par fiche contre ≈ 0,5 réel) ; ordonnancement par rang ou libération dynamique du reliquat (A l. 112).
- Métriques d'ablation : **richesse nette d'archive** (somme des log W au-dessus des parents), taux de survie aux tests de mort seuls comme signal intermédiaire à plus haute puissance (A l. 133-137).
- Emprunts précis : e-valeurs séquentielles pour les tests de mort (POPPER) ; **indiçage par contre-exemples** sur la partie de développement (HypoGeniC) ; **modèle en îlots** K sous-populations isolées 2 à 3 générations avant croisement (FunSearch) (A l. 148-152).
- Réfutation des emprunts par le duel des proposeurs à 100 USD (A l. 155).

**Kimi seul :**

- Représentation à **deux axes** (empirique × testabilité), au lieu d'un nombre d'états (K l. 20-35).
- État « **loi promue, mais identité avec l'idée de course non établie** » (K l. 55).
- Interdiction d'assimiler « non testée » à « réfutée » ; les deux essais d'une indécise appartiennent à la même génération (K l. 25, 54).
- Aucune conversion des verdicts de juges-modèles ou de tests de mort en e-valeurs (K l. 47) ; plusieurs contrôles par famille ne donnent pas un contrôle global (K l. 46).
- Pièce qui trancherait : **tableau des erreurs par étage** (test de mort, traduction, juge, antériorité) sur témoins à vérité connue, dénominateurs complets (K l. 57).
- Deux voies séparées, exploration sur données déclarées et confirmation sur épreuve fraîche, sans que la première compte comme survie (K l. 81).
- **Portée du refus** : « même engagement réfuté » ≠ « domaine interdit » ; transmettre les **frontières de validité et contre-exemples** comme information positive (K l. 109, 121).
- Sortie vers le programme comme **restriction ou réfutation décisive** d'une hypothèse existante, pas seulement « neuve » (K l. 143) ; règle associant chaque issue (positive, nulle, négative, non concluante) à une décision avant l'expérience (K l. 134).
- **Coût par élimination correcte** (K l. 188) ; trois ratios distincts (par promue, par survivante neuve, par sortie) ; coût rapporté par strate de difficulté, jamais utilisé comme aptitude (K l. 165-187).
- Bras **filtre aléatoire de même sélectivité** pour séparer l'information expérimentale de la réduction de population (K l. 222).
- Répétitions indépendantes de la boucle entière ; une seule génération 2 ne mesure pas l'héritage de long terme (K l. 204, 210).
- Base de comparaison **non agentique** (recherche évolutionnaire simple) pour mesurer ce que les modèles de langage ajoutent (K l. 248).
- Tableau mécanisme par mécanisme (gel, développement, épreuve, juge, nul, multiplicité, témoins, archive, coût) plutôt que comparaison par nom de système (K l. 247).

**conv-audit seul (noté à part) :** témoin de sévérité par permutation, e-processus de mort, immigrants comme témoin interne, pari à fraction, malédiction du vainqueur, tous les n80 chiffrés, tranche rétrogradée en développement (C l. 82-87, 94-108, 157-158, 194-201, 269-285).

---

## 6. Ce que je n'ai pas pu faire

- Aucune source bibliographique vérifiée sur PDF (aucun PDF servi, aucun réseau) : toutes sont RAPPORTÉ ; deux sont signalées suspectes (couple titre-identifiant de Dwork et al. chez A ; titre de POPPER chez K, signalé par K).
- Les lignes de la pièce 7 § h retirées par la règle 2 (recommandations D-P1 à D-P5) n'étaient pas lisibles ; je n'ai donc pas pu vérifier si A ou K recoupe une recommandation retirée.
- Je n'ai pas rejoué la simulation de C (hors mandat) ; ses chiffres ne servent qu'à situer les accords.
- Les sources des pièces (brouillons B10, TI, registres, lectures de génération 0 et de la couche 1 bis) ne sont pas servies ; les renvois d'A et de K à ces sources par l'intermédiaire de F n'ont été vérifiés que contre F.
- Le fichier `pont_v1.py` et ses essais ne sont pas servis : les affirmations sur le code (`ebh_pondere`, `membres_de_l_archive`) sont vérifiées contre le texte de la pièce 7, pas contre le code.

Horodatage de fin d'écriture : voir le `date -u` relevé par l'appelant au scellement ; dernier relevé propre `16:37:19 UTC`, 1er novembre 2026.
