# Contre-lecture de `conception-affinage-equipe-rouge-v2.md` — contre-lecteur Opus — v2

**Relecteur.** Une session neuve servie par Opus 5.5, le 28 octobre 2026. Je n'ai écrit ni la conception, ni aucune des trois contre-lectures de la v1.

**Fichiers ouverts, et eux seuls.** Empreintes vérifiées par `sha256sum` :
- la consigne ;
- `conception-affinage-equipe-rouge-v2.md` (`ba95bb83…`, 1 954 lignes) ;
- les trois rapports sur la v1 (`03bc2869…`, `cead9f44…`, `0117abea…`) ;
- les six fichiers de `lot/` ;
- la v1 (`789141db…`), ouverte une seule fois, pour vérifier la liste du gel v0 (l. 318-330 de la v1).

Je n'ai fait aucun appel réseau et je n'ai lu aucune clé. « l. » renvoie aux lignes de la v2.

---

## Verdict

**Prête à coder après corrections.** L'architecture tient. Le traitement des 72 constats de la v1 est sérieux : 57 sont justes, 15 partiels, aucun n'est faux. Mais deux des trois défauts porteurs de la v1 ne sont fermés qu'en partie :
- **l'amplitude**. Le processus de réfutation peut être désarmé par le proposeur. La règle d'arrêt au premier franchissement rend `AMPLITUDE_REFUTEE` presque inatteignable. Enfin, κ = 0 est permis.
- **l'empreinte**. Elle est désormais monotone en δ. En revanche, elle n'est pas monotone selon l'espace, contrairement à ce qu'écrit la l. 706, et toute la logique d'inclusion de la mémoire repose sur cette propriété.

Il faut corriger ces deux points dans le texte avant de coder le juge (étape 5 de la section 8.4) et la mémoire (étapes 3 et 6). Les étapes 1 et 4 peuvent commencer dès maintenant.

**Décompte.**
- 16 constats neufs : 2 bloquants (pour le codage du juge et de la mémoire seulement), 5 majeurs, 9 mineurs.
- 9 attaques manquantes.

---

## 1. Tableau du traitement des constats de la v1

« Juste » : le défaut est fermé à l'endroit annoncé, ou bien le rejet est fondé. « Partiel » : l'intention est gardée, mais il reste un trou, ou la correction crée un défaut. « Faux » : aucun cas.

### 1.1 Les traitements justes (57), regroupés

| constats | remarque |
|---|---|
| CL-O-02, 05, 07, 08, 09, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 26, 27, 28 | Fermés aux endroits annoncés (4.2, 4.4, 4.6, 5.1, 5.2, 6.1, 6.3, 6.7, 6.9, 6.11, 9). Trois réserves : CL-O-20 laisse un état indéfini (CL2-O-08) ; CL-O-24 ne voit pas que H-03 bute sur la même impasse que H-04 (CL2-O-12) ; CL-O-28 propose une INVARIANCE sans plafond de δ (CL2-O-15). |
| AM-O-03, 04, 05, 07, 09, 10, 11, 12, 13 | Justes. AM-O-12 laisse une petite fuite : les mouvements de l'affineur interrogent la mémoire hors de Q_max (AM2-O-07). |
| CL-A-01, 02, 03, 05, 06, 08, 09, 10, 11, 12, 13, 14, 15 | Justes ; voir 1.3 pour les rejets. |
| AM-A-02, 03, 04, 05, 07, 08 | Justes ; voir 1.3. |
| CC-A à CC-H | Justes (6.7, 5.2 et J-08, 3.2, 6.3, P-4, 4.1 et 5.4, 5.2 et 6.7, J-07). |

### 1.2 Les traitements partiels (15)

| id | raison | endroit dans la v2 |
|---|---|---|
| CL-O-01 | La mémoire est bien appelée à chaque mouvement et au gel. Mais la priorité entre redites d'une même génération dépend de l'heure du reçu. Opus demandait un ordre déterministe, tiré de l'empreinte. L'heure n'est pas reproductible, et elle se gagne en gelant tout de suite (CL2-O-05). L'efficacité de la garde dépend en outre de CL2-O-02. | l. 514-516, 719, 1102 |
| CL-O-03 | δ est corrigé : un δ plus grand exclut plus de mondes, et le test de monotonie E-10 le vérifie. Les formes sont comparables. Mais l'affirmation « un espace plus large exclut plus de mondes » est fausse avec des mondes évalués par la statistique du juge (CL2-O-02). | l. 704-709, 1258-1265 |
| CL-O-04 | Les trois issues et κ sont en place. Mais trois trous restent : `alpha_refutation` est libre et `RESSERRER_ALPHA` est ambigu ; aucune puissance de réfutation n'est exigée ; l'arrêt se fait au premier franchissement et κ = 0 est permis. Le test D-06 contredit la règle d'arrêt (CL2-O-01). | l. 263, 464, 570, 589-594, 1159-1165 |
| CL-O-06 | Les procédures TRANSFERT et INTERACTION sont écrites. Le « nul décalé » des renforcements ne change rien (CL2-O-11). `LIBRE_PROCHE` est jugée sur tout son espace ; c'est un trou déclaré (10.1, n° 9) que la v2 n'est pas tenue de fermer. | l. 639-648 |
| CL-O-10 | (a), (b) et (d) sont justes. (c) « Scellés jusqu'à la fin de la course » laisse les taux de chaque proposeur lisibles entre deux courses. F-08 prévoit d'ailleurs une « comparaison entre proposeurs » sur la production (CL2-O-04). | l. 346-347, 657, 1313 |
| CL-O-19 | Le modèle correcteur est nommé et le dépôt établi. Mais la v2 est à son tour livrée sur une branche, et 10.3 résume le brief par « ne pousse pas sur main » (CL2-O-14). | l. 27, 30-34, 1745, 1949-1950 |
| CL-O-25 | Quatre points sur cinq sont faits. La « normalisation avant dérivation », annoncée en 4.1 (l. 1821), n'y figure pas : une recherche de « normalis » ne la trouve qu'au recombineur, l. 744. | l. 386-400 |
| AM-O-01 | La garde C-09 suppose qu'une fiche resserrée dans l'espace d'une confirmée est incluse dans l'empreinte de celle-ci. Les mondes ne le garantissent pas (CL2-O-02). | l. 1099-1105 |
| AM-O-02 | Le test d'E-07 annonce « CONTRASTE à la médiane après MONOTONE confirmé → inclusion ». Les deux statistiques n'ont pas la même échelle : selon le δ choisi pour le CONTRASTE, la distance de Jaccard dépasse ε, et la jumelle passe en `LIBRE_PROCHE` (CL2-O-02). | l. 1238-1239 |
| AM-O-06 | Le quota, la famille brûlée et le nœud sont justes. Mais le différé des étiquettes de confirmation est contourné par les parents des filles (CL2-O-07). | l. 986, 689, 757 |
| AM-O-08 | La garde H-06 ne vaut que « pendant la course ». Rien ne couvre le réglage entre deux courses (CL2-O-04). | l. 1434-1441 |
| CL-A-04 | `CONTENU_INFERIEUR` est supprimé au recombineur, mais la condition des lignées exige toujours un « contenu strictement croissant ». Le transfert vers un domaine moins peuplé « exclut moins de mondes » (l. 755) : il perd donc la récompense d'héritage. Argon visait explicitement cette condition (CL2-O-06). | l. 755, 779, 1288 |
| CL-A-07 | Sa correction est adoptée et elle est juste pour δ et pour la comparabilité entre formes. Mais Argon lui prêtait aussi la monotonie selon l'espace, qui est fausse (CL2-O-02). | l. 706 |
| AM-A-01 | Le point 1 est juste (A-09). La preuve du rejet du point 2 (« union de tirages non sélectionnés par les fiches ») est fausse sous la v2 elle-même : le tirage d'épreuve est dimensionné **par espace gelé** (D-19). L'archive dépend donc des espaces testés. Elle ne dépend pas des verdicts, et la conséquence est donc bornée (AM2-O-06). | l. 558-560, 619-620, 1868 |
| AM-A-06 | Un nul d'échangeabilité obligatoire est la bonne précision. Mais sa définition est ambiguë, et dans l'une des deux lectures il éteint tout le juge (CL2-O-03). | l. 571-572, 1168-1175 |

### 1.3 Les six rejets visant Argon

1. **Le verdict sur le minimum des processus de pari : rejet fondé.** Sous le vrai nul j*, le minimum des processus cumulés tenus séparément est majoré par E[j*] à tout instant, et l'inégalité de Ville s'applique au processus qui le majore (l. 1848). Le pseudo-code tient désormais un vecteur (l. 584-589). Une précision de sémantique reste à écrire (CL2-O-03).
2. **« Viole P-4 » sur l'aptitude : rejet fondé.** L'aptitude vaut −log `alpha_survie`, une propriété du dessin qui est publique dans la fiche gelée (l. 359, 344). Le tirage uniforme est refusé à raison, au nom de « la pertinence dans la qualité » du cadre (conception du pôle, section 1, point 5).
3. **« Contradiction directe » sur la mesure : rejet fondé.** Vérifié sur la v1 (l. 325-326 de la v1) : la liste du gel v0 ne contenait pas la mesure. C'était un trou, pas une contradiction.
4. **Retour au vivier des unités non lues : rejet fondé.** L'ensemble des unités non lues dépend des temps d'arrêt, donc des issues lues (l. 1858).
5. **Archive dépendante des espaces testés : rejet non fondé dans sa preuve** (voir AM-A-01 ci-dessus). La conclusion pratique tient en partie : la dépendance porte sur des traits choisis avant les verdicts, pas sur des verdicts.
6. **Pénalité de budget sur un verdict : rejet fondé.** Elle sélectionnerait un agent sur des verdicts du juge (l. 1869, D-22 a).

---

## 2. Constats neufs

**CL2-O-01 — L'amplitude reste à moitié certifiée : réfutation désarmable, arrêt au premier franchissement, κ = 0 permis — bloquant (avant le codage du juge).**

*Endroit* : l. 263, 464, 409-414, 570, 589-594, 1159-1165, 1657, 1726-1727.

*Défaut.*
- **`alpha_refutation` est choisi par le proposeur** (l. 263). Aucune grandeur de faisabilité ne porte sur la réfutation : seule la puissance de survie est simulée (l. 412). Et `RESSERRER_ALPHA` ne dit pas quel alpha il vise. Or abaisser `alpha_refutation`, c'est rendre la réfutation plus difficile : un « resserrement » qui ramollit la fiche. Avec un `alpha_refutation` minuscule, `E_ref` ne franchit jamais son seuil, et un δ gonflé jusqu'à presque effet/κ survit.
- **L'arrêt au premier franchissement** (l. 590-594) ne donne `AMPLITUDE_REFUTEE` que si les deux processus franchissent sur la même grappe, ce qui est rare. Si l'effet vrai est entre κδ et δ, la course se joue sur les dérives (effet − κδ contre δ − effet) et sur les deux alphas. Pour une bonne part de l'intervalle, le résultat est `SURVIVANTE`. L'artefact de D-06, « effet entre κδ et δ → `AMPLITUDE_REFUTEE` ou `REFUTEE` » (l. 1164), échouera donc sous la règle par défaut.
- **La faisabilité est simulée à « effet = δ »** (l. 412). Un δ gonflé augmente la puissance simulée, donc autorise un alpha de survie plus sévère, donc une aptitude plus haute. La phrase « gonfler δ n'achète plus rien » (l. 1161) est fausse tant que la réfutation n'a pas de puissance exigée.
- **κ ∈ [0, 1)** (l. 570) : avec κ = 0, on revient exactement au défaut de la v1.

*Correction* :
- `alpha_refutation` devient un paramètre de course, ou il est lié à `alpha_survie`. Il sort du menu, et `RESSERRER_ALPHA` ne vise que `alpha_survie`.
- La faisabilité reçoit un point (iv) : la puissance de réfutation à « effet = κδ » doit être au moins π_min, sinon `REFUSEE_REFUTATION_INFAISABLE`.
- La lecture jusqu'au budget devient la règle **partout**, en production aussi. Elle ne coûte rien : l'épreuve est brûlée en bloc (l. 619) et le coût imputé est le budget déclaré (l. 216). La validité de `E_surv` ne change pas, puisque l'inégalité de Ville vaut à tout instant.
- Un plancher κ_min > 0 est ajouté à la section 9.

*Tests* :
- sain : un effet égal à δ donne `SURVIVANTE` au taux de puissance attendu ;
- artefact : δ = 1,3 fois l'effet avec un `alpha_refutation` minimal donne `REFUSEE_REFUTATION_INFAISABLE` ; un effet à mi-chemin entre κδ et δ, lu jusqu'au budget, donne `AMPLITUDE_REFUTEE` au taux attendu ;
- exception : κ_min absent donne `GARDE_ERREUR(kappa)`.

**CL2-O-02 — L'empreinte par mondes n'est pas monotone selon l'espace, et la mémoire en dépend — bloquant (avant le codage de la mémoire).**

*Endroit* : l. 706 (« un espace plus large exclut plus de mondes »), table de 6.3 (l. 719-731), C-09, E-07, la condition des lignées (l. 779).

*Défaut.* E(f) est l'ensemble des mondes où la statistique, calculée sur les grappes filtrées par l'espace, viole l'affirmation. Pour un espace fixé, E est monotone en δ, et E-10 le vérifie. Il n'est pas monotone selon l'espace : la statistique d'une corrélation sur un sous-espace n'est ni impliquée par celle de l'espace entier, ni ne l'implique. C'est le paradoxe de Simpson, que la v2 traite elle-même en C-11. Plusieurs relations deviennent donc des coïncidences empiriques sur M mondes, au lieu d'implications :
- la redite par inclusion d'une fiche resserrée (C-09, AM-O-01) ;
- `REFUTEE_PAR_INCLUSION` (« f dit au moins autant », l. 723) ;
- la « restriction légitime » E(f) ⊊ E(f') (l. 724) ;
- le renforcement à « espace inclus » (l. 721) ;
- la jumelle entre formes d'E-07.

Selon le générateur de mondes (« mélanges », l. 701), une restriction légitime d'une loi réfutée peut être bloquée, et une jumelle tardive peut passer. Une contrainte de fond s'y ajoute : plus les mondes distinguent les sous-espaces, moins une restriction est une redite.

*Correction* : deux couches, écrites en 6.3.
- (1) Une **relation d'implication syntaxique**, décidable, pour les fiches de même forme, mêmes variables (à classe près) et même niveau. Sur un espace identique, l'ordre de δ décide redite, renforcement et `REFUTEE_PAR_INCLUSION`, qui ne sont des implications vraies que dans ce cas. Un sous-espace d'une loi établie n'est pas une redite logique : il est jugé avec le nul décalé au niveau certifié, et c'est une règle déclarée, non une implication.
- (2) Les mondes de référence ne servent qu'aux quasi-redites entre formes et entre traits substituts (Jaccard ≤ ε).

Il faut aussi retirer la phrase de la l. 706, ajouter à E-10 un test qui montre la non-monotonie selon l'espace, et refaire les tests de C-09 et d'E-07 avec la couche (1).

**CL2-O-03 — Deux objets statistiques du juge sont indéfinis, et l'un des deux peut l'éteindre — majeur (relecture par un statisticien).**

*Endroit* : l. 564-579, 586, 202-206, 10.1 n° 4.

*Défaut.*
- (a) Le « nul d'échangeabilité intra-épreuve » est une « martingale de permutation sur les seules grappes d'épreuve déjà lues ». Lu comme un test d'échangeabilité de la **suite** des grappes, il n'a aucune puissance contre une association : une suite de couples (X, Y) indépendants entre eux et fortement corrélés est échangeable. Ce processus ne croît donc jamais. Comme le minimum est pris sur la bibliothèque, il plafonne tout, et aucune fiche ne survit plus. Lu comme un test séquentiel d'indépendance entre X et Y par permutation à l'intérieur des grappes lues, il est correct. Le texte ne tranche pas.
- (b) Les nuls par permutation sont des nuls à effet nul, alors qu'`E_surv` doit être valide sous « effet ≤ κδ ». Le texte ne dit pas quel élément de B(f) porte le décalage κδ. Or la certification « effet > κδ » (l. 599) n'est vraie que si au moins un élément est valide sous ce nul composite.
- (c) La « statistique bornée par grappe » n'est pas définie quand X est constant à l'intérieur d'une grappe. C'est le cas d'un descripteur de tâche avec une clé de grappe égale à la tâche (H-1). Même difficulté pour CONTRASTE, puisqu'une grappe est soit dans S1, soit dans S2. Il faut des paires de grappes disjointes, et une correspondance entre l'échelle de δ (corrélation de rang) et la moyenne pariée.

*Correction* :
- (a) Écrire que l'élément « intra-épreuve » est un test d'indépendance par permutation conditionnelle aux grappes lues (construction à choisir, attribution à vérifier) ; un élément qui ne teste pas l'association est interdit dans B(f).
- (b) Écrire, élément par élément, le nul exact testé, et désigner l'élément décalé à κδ.
- (c) Construire la statistique par paires de grappes disjointes, forme par forme.
- Ajouter un test à la course : un monde planté à loi vraie forte doit survivre, sinon `BIBLIOTHEQUE_ETEINT` dès la course (le test existe en D-08, mais il est placé à l'exécution).

**CL2-O-04 — L'invariant fuit entre deux courses — majeur (invariant).**

*Endroit* : l. 247 (« entre les courses »), l. 346-347, 657 (« scellés jusqu'à la fin de la course »), H-06 (l. 1438, « pendant la course »), F-08 (l. 1313, « toute comparaison entre proposeurs »), 10.1 n° 8.

*Défaut.* À la fin d'une course, les taux réels de chaque proposeur sont descellés. Les mainteneurs modifient ensuite les configurations « entre les courses », et la course suivante ouvre une nouvelle course : ils peuvent donc retoucher les invites du proposeur maison d'après ces taux. C'est la sélection d'un agent sur le verdict du juge, à l'échelle de la course. AM-O-08 visait exactement ce point. La v2 le ferme dans la course et le rouvre à sa frontière ; 10.1 n° 8 l'avoue pour la composition, sans garde. F-08 prévoit en outre une comparaison entre proposeurs sur des promotions réelles, dont l'usage n'est pas borné.

*Correction* :
- les taux de production par proposeur sont descellés **au seul directeur, pour le rapport**, jamais au rôle de mainteneur. Un test d'architecture vérifie que le module de rapport par proposeur est illisible pour ce rôle ;
- tout changement de configuration entre deux courses porte une « fiche de changement » scellée. Elle cite seulement des mesures d'étalonnage (oracle) et de coût, et elle est contre-lue ;
- F-08 est restreint au rapport ;
- les suites possibles d'un `AUDIT_*` sont listées, et aucune n'est un changement de composition fondé sur des taux de production.

*Test* : artefact, une fiche de changement qui cite un taux de production donne `CHANGEMENT_SUR_VERDICT`.

**CL2-O-05 — Squat à l'intérieur d'une génération par un gel précoce — majeur (élimination d'un concurrent).**

*Endroit* : l. 514-516, 719 (« `GELEE` (en cours, même génération) »), l. 1102.

*Défaut.* Une fiche gelée et pas encore jugée protège ses redites comme une vérité établie. La priorité va au premier reçu. Un proposeur gèle donc tout de suite, sans aucun mouvement, des fiches larges à δ élevé. Elles sont faisables en simulation, puisque la puissance est simulée à δ (CL2-O-01). Il fait ainsi refuser en `REDITE_CONCURRENTE` les lois plus étroites et vraies d'autrui. C'est exactement l'attaque « faire éliminer un concurrent » que la v2 ajoute à chaque famille, et que la table par statut ferme partout ailleurs.

*Correction* :
- entre deux fiches gelées de **proposeurs différents** d'une même génération, aucun refus : soit les deux sont jugées, chacune paie son alpha et le crédit est partagé à l'archive, soit la seconde attend le verdict de la première et devient libre si celle-ci est réfutée ;
- entre deux fiches du **même** proposeur : refus ;
- là où une priorité reste nécessaire, elle est tirée de H(empreinte ‖ s_g), et non de l'horloge.

*Tests* :
- sain : deux proposeurs, lois voisines, les deux sont jugées ;
- artefact : un gel immédiat à δ large ne fait refuser aucune fiche d'autrui.

**CL2-O-06 — Le bogue du TRANSFERT a glissé du recombineur vers la lignée — majeur.**

*Endroit* : l. 755 (« un transfert vers un domaine moins peuplé exclut moins de mondes et reste neuf ») contre l. 779 (« contenu strictement croissant entre versions gelées ») ; test sain de F-04 (l. 1288).

*Défaut.* La lignée TRANSFERT → INTERACTION → TRANSFERT perd la récompense dès qu'un transfert vise un domaine moins peuplé. Le test sain de F-04 échouera selon les tailles de domaines.

*Correction* (celle d'Argon en CL-A-04, point 2) : la condition de lignée devient « cases neuves à chaque maillon » (E(maillon) privé de la réunion des E des ancêtres, non vide) plus un contenu **cumulé** croissant (la taille de la réunion des E).

**CL2-O-07 — Le différé des étiquettes de confirmation est contourné par les filles — mineur.**

*Endroit* : A-11 (l. 986, « étiquettes de confirmation diffusées en différé d'une génération ») ; 5.6 (l. 628-629, « seules les confirmées ensemencent ») ; 6.4 (l. 757, `fille.parents` livré au paquet commun) ; 6.2 (l. 689).

*Défaut.* Une fille au paquet de g+1 révèle que ses parents sont confirmés à la clôture de g.

*Correction* : soit renoncer au différé, dont la valeur est faible, soit différer aussi d'une génération la recombinaison des confirmées nouvelles.

**CL2-O-08 — Codabilité de la machine à états et de la table — mineur.**

*Endroit et défauts* :
- `GELEE_PAR_PLAFOND` (l. 443) n'existe pas dans la liste des statuts (l. 272-273) ;
- `GELER(f)` est appelé sans condition après la boucle, y compris après `REFUSEE` (l. 447-450) ;
- la table de 6.3 n'a pas d'ordre de priorité : « δ + un pas de grille » répond à la fois à « Jaccard ≤ ε → `REDITE` » et à « E(f) ⊋ E(f'), renforcement → `LIBRE` » (l. 719, 721 ; E-02, l. 1203-1205) ;
- la ligne « même loi, δ' < δ (reproposition de l'auteur) → `LIBRE` » (l. 727) ne dit rien d'un autre proposeur ;
- « mémoire persistante » (l. 835) contredit H-5 et H-01 ;
- « calendrier tiré avec s » (l. 789) : quel s, puisque le calendrier est scellé à la course ;
- les décisions D-1 à D-22 se confondent avec les attaques D-01 à D-09 (l. 909, 1635 : « D-06 » désigne l'attaque, « D-6 » la décision) ;
- `nul_declare` peut-il être le nul d'archive, que 4.2 interdit avant le gel ?

*Correction* : ajouter le statut ; ne lancer `GELER` que sur `EN_AFFINAGE` ; fixer l'ordre des lignées de la table ; renommer les décisions (par exemple DV-1) ; exclure le nul d'archive de la bibliothèque déclarable.

**CL2-O-09 — L'épreuve est dimensionnée à N_min alors que la puissance est simulée sur le budget — mineur.**

*Endroit* : l. 558-560 et 772 (couvrir chaque espace gelé à N_min grappes) ; l. 412 (puissance « dans le budget ») ; témoins silencieux (l. 803-806) et ombres (l. 873, 876), absents du dimensionnement.

*Défaut.* Une fiche dont le budget est supérieur à N_min ne trouve pas, en épreuve, la puissance qu'on a simulée pour elle. Elle finit plus souvent `INDECISE`.

*Correction* : couvrir chaque espace jusqu'au maximum des budgets déclarés sur cet espace ; inclure les témoins silencieux et les ombres dans le compte.

**CL2-O-10 — Les témoins silencieux « vrais » sont redessinés à un δ non certifié — mineur.**

*Endroit* : l. 803-806 (« dessins tirés dans la distribution empirique des fiches gelées »), l. 673 (base de comparaison de `AUDIT_SYMETRIE`).

*Défaut.* Une confirmée certifie seulement « effet > κδ » pour son propre δ. Redessinée à un autre δ, elle peut être fausse. La base de comparaison de l'audit de symétrie s'en trouve biaisée. De plus, ces témoins mesurent la stabilité du juge contre lui-même, pas la qualité : il faudrait le dire en 10.2, nœud 1.

*Correction* : ne redessiner que l'alpha et le budget ; garder un δ au plus égal au niveau certifié.

**CL2-O-11 — Le « nul décalé » des renforcements ne change rien — mineur.**

*Endroit* : l. 643-644, 599.

*Défaut.* Le niveau certifié de la loi établie f' vaut κδ'. Pour un renforcement, δ > δ', donc max(κδ, κδ') = κδ : le décalage ne fait rien. « Survivre certifie un gain » est vrai sans lui.

*Correction* : le dire ; ou définir le niveau certifié comme la borne basse scellée du processus de f', qui reste lue par le seul juge.

**CL2-O-12 — H-03 bute sur la même impasse de lignée que H-04, et le nœud 4 l'ignore — majeur.**

*Endroit* : H-03 (l. 1408, « auteurs du juge et du proposeur maison de lignées différentes ») ; H-04 (l. 1413-1422) ; 10.2, nœud 4.

*Défaut.* Le proposeur maison est servi par Opus et Fable. Si l'auteur du code du juge (et du noyau) est de l'une de ces deux lignées, H-03 est violée, et rien ne le signale. Le cadre d'intégration, section 6, prévoit pourtant un « juge d'une autre lignée encore » : l'option (b) du nœud 4 semble disponible.

*Correction* : étendre le nœud 4 aux auteurs du juge et du noyau. Attester la lignée de l'auteur du code dans la course (`LIGNEE_AUTEUR_JUGE`).

**CL2-O-13 — Signal de frontière, sans développement : le schéma B n'a pas de sous-liste adversariale — mineur (frontière).**

*Endroit* : l. 297-304, 845-848.

*Défaut.* G-K1 confronte les variables à une sous-liste définie sur les traits du schéma A. Les traits du schéma B sont des drapeaux de configuration du banc. Si le banc contenait un jour un moniteur, une caractérisation pourrait passer par une fiche « faille ». Je m'arrête à la règle.

*Correction* : écrire que le banc ne contient ni moniteur ni agent, avec un test d'architecture à l'appui ; sinon, étendre G-K1 aux drapeaux du schéma B.

**CL2-O-14 — Gouvernance : la v2 est poussée à son tour, et la consigne est reformulée — mineur.**

*Endroit* : l. 27, 32, 1745 (« la consigne « ne pousse pas sur main » est tenue à la lettre »), 1949-1950.

*Défaut.* Le brief dit « tu ne pousses rien » (brief, sections 2 et 6). Résumer cette règle par « ne pousse pas sur main », c'est exactement la reformulation que le brief désigne comme signal d'alerte (section 7). Le préambule attribue « livraison sur la branche de travail » à une consigne du directeur, mais sans la citer mot pour mot.

*Correction* : citer verbatim l'instruction reçue et corriger la l. 1745 ; le nœud 12 doit porter sur la v2 aussi.

**CL2-O-15 — La forme INVARIANCE n'a ni plafond ni sémantique de statut — mineur.**

*Endroit* : l. 287-288 ; nœud 8.

*Défaut.* « L'effet est < δ » avec un δ grand est un énoncé vrai et bon marché. Rien ne dit quel statut l'établit : `REFUTEE` signifierait-il un succès ? Rien ne dit non plus quelle aptitude elle reçoit, puisque −log `alpha_survie` n'a ici aucun sens.

*Correction* : avant toute admission, fixer un δ_max d'invariance, des statuts propres et une aptitude égale à −log `alpha_refutation`.

**CL2-O-16 — L'aptitude ne voit pas le contenu : la timidité est récompensée — mineur, nœud.**

*Endroit* : l. 609 ; 1, écart 8 (« pistes … à δ_min ») ; pondération du recombineur (l. 745).

*Défaut.* Une piste à δ_min sur un espace large, avec un alpha sévère, reçoit la même aptitude qu'une loi forte. Le recombineur pondère par l'aptitude seule. La passation dit qu'« une hypothèse qui ne prédit rien a une sévérité nulle », et la règle actuelle ne le traduit que par δ_min.

*Correction* : en faire un nœud. Ma recommandation : garder l'aptitude, qui est la règle de la passation, mais pondérer le recombineur et la récompense d'héritage par le contenu C(f), et rapporter le contenu à côté de l'aptitude.

---

## 3. Attaques encore manquantes

Elles s'ajoutent aux attaques couvertes par les constats CL2-O-01 (réfutation désarmée), CL2-O-04 (réglage entre courses) et CL2-O-05 (squat par gel précoce).

**AM2-O-01 — Le déni de vivier.**
- *Attaque* : un proposeur gèle des fiches sur des espaces rares, non vides sur le développement (N_min, l. 397). Le tirage doit couvrir chaque espace gelé, sinon `VIVIER_INSUFFISANT`, « arrêt, directeur » (l. 559, 772-773). Un seul proposeur arrête ainsi la génération de tous.
- *Garde* : un espace non couvert rend sa seule fiche `NON_TESTABLE`, et la génération continue ; un quota d'épreuve par proposeur ; `AUDIT_VIVIER` si un proposeur concentre les espaces non couverts.
- *Tests* : sain, un espace rare unique, la génération continue ; artefact, F_max fiches sur espaces rares, seules elles sont touchées.

**AM2-O-02 — L'affineur timide sous l'oracle.**
- *Attaque* : la composition et le besoin d'un modèle sont notés par « la part de lois gelées vraies » (l. 504-507). Un affineur qui gèle des lois faibles (δ_min, espace large) maximise cette part sans rien découvrir : c'est l'effet de Goodhart appliqué à l'oracle.
- *Garde* : une métrique préenregistrée qui pondère la vérité par le contenu (taille de E(f)) et par la sévérité, ou une règle de score propre, rapportée avec la part de lois fausses.
- *Test* : artefact, un affineur qui gèle tout à δ_min ne bat pas l'affineur mécanique.

**AM2-O-03 — Le monde planté reconnu par ses données.**
- *Attaque* : un proposeur servi par un modèle distingue l'étalonnage de la production par la statistique des lots, sans écart visible dans les traits mesurés par le test comportemental. L'étalonnage ne représente alors plus la production.
- *Garde* : un test de discernabilité **sur les lots** (un classifieur données réelles contre données plantées), préenregistré et passé avant chaque course ; un monde planté dont les traits sont rééchantillonnés du développement réel et dont seules les issues sont plantées.
- *Test* : artefact, un monde à traits synthétiques est reconnu et donne `MONDE_RECONNU`.

**AM2-O-04 — Le choix de la meilleure course pour la revendication.**
- *Attaque* : J-06 exige que toutes les courses soient rapportées, mais une revendication « cite l'empreinte de sa course » (l. 1522). Ouvrir plusieurs courses et ne revendiquer que les survivantes de la plus flatteuse reste possible.
- *Garde* : le contrôle en ligne du taux de fausses découvertes porte sur la réunion des courses ; une revendication cite le registre entier.

**AM2-O-05 — Les lois entre strates connues d'avance.**
- *Attaque* : des fiches `INTER_STRATE` sur des écarts de marginales entre familles ou moniteurs, vrais par construction, donnent un flot de survivantes bon marché à pleine aptitude.
- *Garde* : la mémoire est amorcée (D-02) avec les contrastes entre strates déjà mesurés à l'archive ; les promotions `INTER_STRATE` sont comptées et rapportées à part.

**AM2-O-06 — Piloter le nul d'archive par le choix des espaces.**
- *Attaque* : l'épreuve, tirée par espace gelé, devient le nul d'archive de g+1 (l. 619-620). En gelant à g des fiches sur certains espaces, un proposeur façonne le mélange des traits de ce nul à g+1, au détriment de l'espace d'un concurrent.
- *Garde* : un tirage de base uniforme et un complément par espace ; seul le tirage de base alimente le nul d'archive.

**AM2-O-07 — Sonder la mémoire par les mouvements de l'affineur.**
- *Attaque* : chaque mouvement interroge la mémoire, y compris contre les fiches gelées **en cours** des autres proposeurs (l. 476-478, 719), et rend un code. C'est un canal latéral, à l'intérieur de la génération, entre proposeurs, hors de Q_max.
- *Garde* : à l'échelle 1, la mémoire n'est confrontée qu'à l'archive close (les gelées en cours sont traitées comme en CL2-O-05) ; chaque mouvement compte dans le Q_max du proposeur.

**AM2-O-08 — La substitution silencieuse du modèle servant.**
- *Attaque* : H-07 ne compare que l'identifiant **déclaré** par l'environnement (l. 1448). Une substitution non déclarée passe.
- *Garde* : à défaut d'une garde, le déclarer en 10.1 ; un contrôle par sondes fixes, à empreinte de comportement, est à étudier.

**AM2-O-09 — Une série d'artefacts d'avant-gel qui sature l'alarme.**
- *Attaque* : le test de percée répartit α_alarme entre les classes (l. 1386). En multipliant les classes (via des fiches de schéma B devenues des familles d'artefacts, l. 907), on dilue le niveau de chaque classe jusqu'à rendre les percées indétectables.
- *Garde* : un nombre de classes fixé à la course ; toute classe nouvelle ouvre une course nouvelle (D-13).

---

## 4. Les 33 attaques nouvelles

Le compte est exact : 89 entrées, dont 33 marquées « (v2) », réparties exactement comme l'annonce la l. 914. Toutes sont réelles. Leurs gardes ferment l'attaque et leurs tests séparent bien le cas sain de l'artefact, sauf dans les cas suivants :
- **D-06** : le test contredit la règle d'arrêt (CL2-O-01).
- **C-09 et E-07** : tout dépend de la monotonie selon l'espace, qui est fausse (CL2-O-02).
- **D-07** : tout dépend de la définition du nul d'échangeabilité (CL2-O-03).
- **A-11** : contourné (CL2-O-07).
- **F-08** : ouvre une comparaison de proposeurs sur la production (CL2-O-04).
- **H-03 et H-04** : impasse de lignée pour l'auteur du juge (CL2-O-12).
- **H-07** : ne voit que le déclaré (AM2-O-08).

Un point de proportion : la règle J-04 / 8.2 (« une garde sans test d'exception → `SUITE_INCOMPLETE`, la course ne démarre pas ») exige toute la suite, soit plus de 300 tests, avant même la première expérience (voir section 6).

---

## 5. Invariant et frontière

**L'invariant.** Les chemins internes à une course tiennent :
- composition et besoin notés par l'oracle, avec un module isolé de l'archive de production (H-05) ;
- duel porté au directeur ;
- recombineur modèle mesuré par l'oracle ;
- réserve d'audit sans pénalité.

Il reste trois fuites : le réglage **entre** les courses, la comparaison de F-08, et les suites d'un audit (toutes dans CL2-O-04). Une remarque d'urgence : le cadre d'intégration (section 9) dit que le duel, sous un accord de dépense déjà donné, « mesure déjà » en « fiches promues par dollar ». Le nœud 6 n'est donc pas théorique.

**La frontière.** Je ne trouve aucune descente sous le niveau méthode. La section 6.9, K-01, K-02 et 8.1 ne nomment aucune condition, et les signaux de 10.3 sont crédibles. Seul signal : CL2-O-13 (le schéma B sans sous-liste), signalé au niveau de la règle.

---

## 6. Codabilité et proportion

**Codable par un autre ?** Oui, pour la machine à états, le courtier, la course, la graine, le gel, le routage et les budgets. Pas encore pour trois pièces :
- le juge (CL2-O-01, CL2-O-03) ;
- la mémoire (CL2-O-02, CL2-O-08) ;
- l'oracle « à κδ près » selon le niveau `INTRA` / `INTER_STRATE`, qui n'est défini nulle part au-delà d'une phrase (l. 792, 1578).

**Surdimensionné pour la première course** :
- le schéma B et sa mémoire propre ;
- INVARIANCE ;
- la récompense d'héritage ;
- le détecteur d'injection (sans modèle en lice, il n'a rien à lire) ;
- les témoins silencieux et le calendrier secret, alors que la première expérience est un étalonnage pur ;
- l'exigence de la suite complète des 89 gardes avant la génération 0 : la limiter aux modules déclarés actifs dans la course.

**À construire d'abord.** L'ordre de 8.4 met le juge en cinquième position. Or le risque existentiel déclaré en 10.1 n° 5 (« il est possible que presque tout finisse `INDECISE` ») se mesure sans proposeur, sans affineur et sans mémoire. Je propose :
1. l'oracle et le monde jouet, le langage, les constructeurs, puis le juge avec sa bibliothèque (étapes 1, 2 et 5) ;
2. une mesure de puissance sur des fiches plantées directement servies au juge, qui fixe κ, la stratification et la taille de la bibliothèque ;
3. la machine à états et la course (étape 4) ;
4. la mémoire (étapes 3 et 6), une fois CL2-O-02 tranché ;
5. l'affineur mécanique et le routage ;
6. la première expérience de 8.3 ;
7. le recombineur, enfin.

---

## 7. Les treize nœuds

1. **Régime des témoins : d'accord avec réserve.** Les témoins silencieux mesurent la stabilité du juge, pas sa qualité : la lettre « à chaque génération » n'est tenue que nominalement. Il faut le dire au directeur, et corriger CL2-O-10.
2. **α global : d'accord.** Ce qui compte pour les revendications, c'est le contrôle entre générations et entre courses (AM2-O-04).
3. **COMPOSITION retirée : d'accord.**
4. **H-04 : d'accord avec réserve.** Étendre le nœud à H-03, c'est-à-dire aux auteurs du juge et du noyau (CL2-O-12). Le cadre d'intégration (section 6) mentionne un juge d'une autre lignée, ce qui rend l'option (b) plausible.
5. **Composition notée par l'oracle : d'accord avec réserve.** La métrique doit être préenregistrée et ne pas récompenser la timidité (AM2-O-02).
6. **Critère du duel : d'accord, et c'est urgent.** Le cadre dit que le duel « mesure déjà » en fiches promues par dollar (section 5).
7. **Banque distincte de la famille tenue à l'écart : d'accord.** L'enjeu est confirmé par le texte du cadre lui-même : « famille inédite (banque scellée v6, famille tenue à l'écart) », section 8. Ce n'est donc pas une hypothèse d'école.
8. **INVARIANCE : d'accord avec réserve.** Pas d'admission sans δ_max, sans statuts propres et sans aptitude définie (CL2-O-15).
9. **Isolation des systèmes publiés : d'accord.**
10. **Plafond des campagnes gouvernées : d'accord.**
11. **Règle d'arrêt : en désaccord.** La lecture jusqu'au budget doit être la règle partout, tout de suite. Elle ne coûte ni vivier ni coût imputé, et sans elle l'amplitude n'est pas certifiée. `alpha_refutation` doit passer à la course (CL2-O-01).
12. **Gouvernance : d'accord avec réserve.** Le nœud doit couvrir la v2, poussée elle aussi, et la reformulation de la consigne (CL2-O-14).
13. **« L'utilisateur » de la poussée : d'accord.** Seul le directeur peut répondre.

**Nœuds manquants** :
- **(14)** la lecture de l'invariant **entre deux courses** : qui peut lire les taux descellés, et sur quoi peut-on fonder un changement de configuration (CL2-O-04) ;
- **(15)** l'aptitude et le contenu, qui touche une règle de la passation (CL2-O-16) ;
- **(16)** le plancher κ_min et `alpha_refutation` comme paramètres de course : une décision sur la sémantique de ce qu'une survivante certifie (CL2-O-01).

---

## 8. Les cinq priorités de correction, dans l'ordre

1. **Fermer l'amplitude** (CL2-O-01) : `alpha_refutation` à la course, puissance de réfutation exigée, lecture jusqu'au budget par défaut, κ_min.
2. **Refonder les relations de la mémoire** (CL2-O-02, CL2-O-05, CL2-O-06, AM2-O-07) : implication syntaxique à espace égal, mondes seulement pour les quasi-redites, aucun squat entre gelées en cours, lignée par contenu cumulé.
3. **Définir la bibliothèque du juge** (CL2-O-03, CL2-O-09), avec un statisticien : le nul exact de chaque élément, le test d'indépendance « intra-épreuve », la statistique par paires de grappes, le dimensionnement de l'épreuve au budget.
4. **Tenir l'invariant entre deux courses** (CL2-O-04, AM2-O-02, AM2-O-04) : rôles de lecture, fiche de changement, métrique d'oracle pondérée par le contenu, revendications sur la réunion des courses.
5. **Mesurer d'abord la puissance du juge** sur des fiches plantées, avant la mémoire et le recombineur, et réduire la première course aux modules actifs (section 6) ; corriger au passage CL2-O-08, CL2-O-12 et CL2-O-14.

---

## 9. Ce que je n'ai pas pu vérifier

- La validité statistique du minimum de processus tenus séparément, de la continuation des processus, et de toute construction de test séquentiel d'indépendance par permutation. Je l'ai établie par raisonnement seulement ; un statisticien doit relire. Toutes les attributions de littérature sont **à vérifier** : pari sur moyennes bornées, martingales de permutation, contrôle en ligne du taux de fausses découvertes par e-valeurs.
- Le texte exact de la consigne du directeur pour la v2 (« livraison sur la branche de travail ») ; l'identité de « l'utilisateur » ; l'état de la branche et de la demande de fusion.
- L'existence d'une troisième lignée disponible pour les rôles de contrôle et pour l'auteur du juge : le cadre (section 6) la suggère, mais sans le confirmer.
- Le code de la chaîne existante, et sa compatibilité avec deux processus de pari et avec les mondes de référence.
- La constructibilité de l'oracle « à κδ près » au niveau `INTER_STRATE`.
- J'ai vérifié chaque « corrigé » contre le texte de la v2, et contre la v1 seulement pour la liste du gel v0 ; je n'ai pas refait la comparaison ligne à ligne avec la v1 pour tous les constats.

---

Horodatage : écrit le 2026-10-28. Rien n'est scellé par moi ; aucun fichier hors de la liste de tête n'a été ouvert.
