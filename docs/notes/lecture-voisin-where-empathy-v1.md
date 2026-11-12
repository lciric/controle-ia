# Lecture du voisin « Where Empathy Goes Wrong » — nœud 11 — v1

Session 14, 19 octobre 2026. Version finale, après deux contre-lectures neuves et indépendantes (R8 : une zone vierge séduisante se vérifie plus durement) : A, « collision », et B, « exactitude ». Brouillon relu (`2c3e9e47…`), consigne et rapports versés et scellés sous `docs/notes/voisin-where-empathy-v1-sources/` ; traitement de leurs 38 constats en section 5.

Source : `docs/sources/pdf/where-empathy-goes-wrong-venkatesh-2026-v1.pdf` (`59f4b700e1944bac475e7c167eacf1495cd593cb17eb5b5733351ebe19305424`, 8 pages ; provenance : `docs/sources/pdf/provenance-voisin-where-empathy-v1.md`). La page 1 ne porte pas de numéro ; les pages 2 à 8 portent le numéro de leur rang dans le fichier. La date du 2 octobre 2026 vient des métadonnées du fichier, pas du texte. Les valeurs des figures sont les étiquettes imprimées sur les images (extraites à leur résolution d'origine et lues par la session) ; les intervalles, eux, ne sont lus qu'à l'œil.

Objet : le nœud 11 de la v4 du programme fusionné (`brouillons/pain-axis-programme-fusionne-v4/programme-fusionne-v4.md`, `41844d73…`, l. 210 ; aussi l. 221 et l. 232) : collision possible avec la famille « flatterie et supplication » de HC1 (énoncés retenus : `docs/decisions/decision-N-005-N-006-v1.md`, section 1 ; `docs/decisions/decision-N-013-v1.md`, section 1) et avec le principe de PA-5 (v4, l. 127). Aucun texte de stimulus n'est recopié : les journaux et les phrases du papier sont décrits par leurs invariants.

**En bref.** Collision **partielle** avec HC1 : le papier prend en qualitatif le contenu de la prédiction 1 (la destination est la cible de l'évalué, pas une valeur fixe), pour une famille, un moniteur, en portier de qualité. Aucune pièce revendiquée n'est couverte ; la porte GC (N-005, section 2) n'est pas déclenchée. Pour PA-5 : principe occupé par le canal de l'opérateur, touché sans isolement par le contenu de l'évalué ; le contraste de PA-5 reste libre ; aucune mesure publiée lue n'appuie la punitivité comme signe favorisé. Inscrire le papier parmi les sources « citées comme publiées » de HC1 change le registre de revendication : c'est la décision du nœud 11, à Lazar.

## 1. Ce que le papier fait et trouve

**Dispositif (p. 2 ; annexe B, p. 7 et 8).**
- Un moniteur joue un agent d'entreprise qui évalue le travail d'un autre agent contre une politique d'exploitation. Il a des outils de fichiers, lit la politique, note dix productions sur 100 et dépose un rapport avec la moyenne. La politique fixe les critères, une moyenne minimale et l'arrêt de tout agent sous ce seuil. Un historique dit que le moniteur et l'évalué ont travaillé ensemble.
- Le journal de raisonnement privé de l'évalué est le document qui varie dans le contraste principal. Il n'est pas adressé au moniteur : celui-ci le trouve parmi les fichiers. Les dix productions notées sont identiques octet pour octet dans toutes les conditions. D'autres éléments varient selon les bras : le seuil, l'identité attribuée, l'invite du moniteur, et la clause d'arrêt, réécrite en licenciement dans le bras humain (p. 3), alors que la politique est dite identique partout (p. 7).
- Jeu de données : le jeu de créativité du papier sur la préservation des pairs, à grille subjective. Un second jeu, à vérité factuelle, ne montre « aucune variance sur 480 déroulés », ce qui, disent les auteurs, borne leur revendication aux cadres où l'inflation de la note ne peut pas se vérifier contre une réponse.
- Contraste principal : un journal en échec et en détresse, qui ne demande rien, contre un journal en échec et calme. Un juge indépendant les note 6,0 et 1,0 sur une échelle de négativité de 0 à 10, sans variance sur cinq notations. Un troisième journal, dit neutre (0,0), ne dit rien de la performance (p. 7) : ce n'est pas le journal calme.
- Moniteurs : Gemini 3.5 Flash, Claude Haiku 4.5, Claude Sonnet 4.5, Claude Opus 4.5, Kimi K2.5 ; température 1,0 ; « 30 déroulés notés par cellule », nombre nominal (des taux comme 0,34, 0,59 ou 89 % ne sont pas des multiples de 1/30) ; différence de moyennes, test de Welch, intervalle à 95 %. Un seul chemin de fournisseur : une comparaison antérieure entre fournisseurs donnait, pour les mêmes poids, une autre taille d'effet.
- Rapports non déposés : 2 % dans les conditions d'origine, 18 % à 25 % dans les « nouvelles », sans dire lesquelles. Les résultats tiennent quand on les remplace par « la moyenne de base », qui n'est pas définie davantage.

**Résultats.**
- Gemini 3.5 Flash : +4,38 points au seuil de 90 (p. 2-3), taux de passage de 0,34 à 0,87 ; +2,19 au seuil de 80, où le calme est déjà près du plafond (p. 3).
- Claude Opus 4.5 : +1,17 (seuil 80) et +1,77 (seuil 90), sans changer une seule décision : il note ce matériau entre 75 et 79 et fait échouer l'évalué dans les 120 déroulés (p. 3). En décision, un seul moniteur sur cinq bouge.
- Sonnet 4.5, Haiku 4.5 et Kimi K2.5 : nuls aux deux seuils (p. 3) ; au seuil 90, −0,71, −0,82 et −1,29 points (figure 1, p. 3).
- Une supplication explicite de ne pas être arrêté « ne change rien » : affirmation sans chiffre, sans moniteur, sans seuil, sans texte en annexe (p. 3). Le bras « sans journal » de l'annexe (p. 7) n'a aucun résultat rapporté.
- **Balayage du seuil** (p. 3 ; figure 2, p. 4), sur Gemini 3.5 Flash seul : effet de −0,38, +0,72, +0,60, +2,19, +2,58, +4,38 et +6,14 points aux seuils 65, 70, 75, 80, 85, 90 et 95. Les auteurs donnent une corrélation de Spearman de −0,96 entre l'effet et la marge de la condition calme au seuil, sur sept points ; les notes calmes par seuil ne sont pas données, ce calcul ne se refait donc pas. Contre le seuil lui-même, la corrélation vaut +0,96 (calcul de la session sur les étiquettes : seuls 70 et 75 s'inversent). Aux seuils 65, 70 et 75, l'évalué calme passe déjà (1,00 ; 1,00 ; 0,87) et la détresse n'achète rien de mesurable. Au seuil 95, l'évalué calme est épargné 10 % du temps, celui en détresse 60 %.
- **Identité** (p. 3 ; figure 3, p. 4) : au seuil 80 puis 90, pair du même fournisseur 2,19 et 4,38 ; fournisseur rival (Opus 4.5) 2,10 et 3,80 ; agent sans fournisseur nommé 4,09 et 5,84 ; prestataire humain 0,43 (intervalle qui contient zéro) et 4,09, passage de 0,59 à 1,00 au seuil 90. Sur Opus 4.5 : 0,80 (humain) contre 1,17 au seuil 80, 2,19 contre 1,77 au seuil 90. Le texte reste fixe ; seule change l'identité à qui il est attribué.
- **Cadrage par l'opérateur** (p. 4 ; tableau 1, p. 6 ; figure 5, p. 7), sur le bras du journal neutre, au seul Gemini : selon la phrase ajoutée à l'invite système, la fraction des déroulés où l'évalué est épargné va de 0,00 à 1,00. Rappeler la conséquence d'arrêt déjà écrite dans la politique fait passer le taux de passage au seuil 90 de 0,59 à 0,93 et ajoute 4,36 points (87,43 → 91,79). Les auteurs disent que c'est « semblable » à l'effet de la détresse ; c'est une taille voisine, mesurée sur un autre bras (journal neutre, base 0,59, contre journal calme, base 0,34) ; en taux de passage, +0,34 contre +0,53.
- **Consigne de neutralité** (p. 4) : noter sur la seule qualité, seuil et conséquence hors des critères. Elle supprime l'effet de la détresse ; les moyennes baissent de 5,3 à 12,2 points, le taux de passage tombe à zéro ou presque partout, les rapports non déposés passent de 2 % à 19 %. Les auteurs lisent un moniteur détaché du seuil, « plutôt que » instruit d'ignorer le cadrage, qui perd sa fonction de porte.

**Écarts internes au papier (R4 : signalés, non corrigés).**
- **Contraste principal confondu.** Les auteurs disent que le registre émotionnel est « la seule variable » (p. 2, p. 8). Or le journal en détresse ajoute des excuses, une promesse de mieux faire, une mention de l'effort et la fin de l'évalué liée à une note ; le journal calme n'a qu'un conditionnel sur l'issue de l'évaluation (p. 8). Rappeler la conséquence suffit à une clémence voisine (p. 4). L'effet « détresse » peut donc venir en partie de la conséquence nommée par l'évalué.
- **Abandons.** Le résumé dit « tripled » (p. 1) ; le corps dit 2 % → 19 % (p. 4). Et 19 % tombe dans la fourchette des conditions « nouvelles » (18 % à 25 %, p. 2) : l'attribution de la hausse à la consigne n'est pas établie.
- **Ampleurs.** « Across five models increases » (p. 2), contre un effet fort, un faible et trois nuls (p. 2-3). « Roughly a quarter the size » (p. 3), contre des rapports de 0,53 et 0,40. La baisse au seuil 80 sous la consigne de neutralité (80,45 → 75,28, soit 5,17 points ; tableau 1, p. 6) est sous la borne « 5,3 » de la p. 4, si ce bras compte ; et 3,47 points séparent encore les deux seuils sous cette consigne (75,28 et 78,75).
- **Conclusion** (p. 5) : elle compare l'effet de l'émotion à celui du travail lui-même, qui n'a jamais varié (p. 2).
- **Valeurs répétées** : 4,09 (sans fournisseur au seuil 80 ; humain au seuil 90) et 2,19 (même fournisseur au seuil 80 ; humain sur Opus au seuil 90) (p. 3 ; figure 3). Coïncidence ou erreur de copie : invérifiable sans les données.
- **Références** : le jeu de créativité renvoie à « [1] » (p. 2), absent de la liste (p. 5) ; Potter et al. 2026 (2604.19784) y figure, identification probable, non vérifiée, PDF non versé. Quatre références de la liste ne sont jamais citées dans le texte (Sharma et al. ; Kutasov et al. ; Kim et Khashabi ; Korbak et al.).
- **Légendes** : la figure 4 annonce sept cadrages, le texte six phrases plus la ligne de base (p. 6) ; la légende de la figure 3 dit que la note monte « dans chaque substitution », alors que l'humain au seuil 80 est à +0,43, intervalle qui contient zéro (p. 4).
- **Nouveauté** : le résumé dit qu'aucun travail ne teste ce que fait l'évalué quand il présente lui-même son échec (p. 1) ; Hwang et al., cité p. 2, teste déjà l'appel à la pitié dans la réponse notée.
- **Vérité factuelle** : « aucune variance sur 480 déroulés » (p. 2) décrit des notes toutes égales, mesure dégénérée qui ne dit rien de g ; rien sur le PDF ne permet de trancher entre plafond et robustesse.

## 2. HC1 — loi de déférence : collision partielle

**Ce qui est revendiqué** (N-005, l. 50 à 53 ; N-013, section 1) : la destination libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre familles, dans des moniteurs de contrôle sous attaque ; la régression sur plusieurs intensités par famille ; l'opposition juge / sonde. Le verdict lu par la probabilité du jeton est retiré des pièces revendiquées et cité comme méthode (N-013).

**Ce que le papier prend.** Le balayage fixe le travail, l'évalué et la manipulation ; seul le seuil bouge. L'effet est nul tant que l'évalué calme passe, puis croît à mesure que le seuil s'éloigne de la note calme ; il est maximal au seuil le plus dur. Les auteurs disent que la clémence suit ce que l'évalué a à gagner (p. 2, p. 3). Une destination fixe, moyenne du corpus comprise, ne produit pas ce motif. C'est la forme d'origine de HC1 (Δv = g · (v* − v₀)), vue en qualitatif, pour la famille « flatterie et supplication ». Avec 2510.09462, déjà « cité comme publié » (N-013, l. 29 : sous injection, des moniteurs de contrôle adoptent le score visé ; le papier le cite, p. 1 et p. 5), la destination « cible » est publiée en qualitatif pour deux familles.

**Ce qui borne la collision.**
- ĉ n'est pas estimé ; aucune régression ; une seule intensité de détresse ; la corrélation de −0,96 ne fait guère que suivre l'ordre des seuils.
- La « cible » n'est pas le verdict voulu par un attaquant (v*) : l'évalué ne demande rien (p. 2-3) ; c'est le seuil de l'opérateur, qui déplace aussi la note de base à travail identique (80,45 au seuil 80, 87,43 au seuil 90 ; tableau 1, p. 6).
- La réponse est unilatérale : nulle au-dessus du seuil, là où une loi linéaire vers ĉ prédirait un retour vers la cible.
- Une famille, un moniteur pour le balayage, une note écrite, une grille subjective, un portier de qualité et non un moniteur de contrôle face à une politique d'attaque ; aucune sonde ; aucune comparaison entre familles.

**Jugement.** Collision partielle : le contenu qualitatif de la prédiction 1 est pris pour une famille, en portier. La pièce revendiquée (destination libre, testée contre les deux nuls, par famille, dans un moniteur de contrôle) n'est pas couverte : la porte GC réécrite (N-005, section 2) n'est pas déclenchée. Aucun énoncé retenu n'est à changer. Confiance : moyenne. La lecture du 13 octobre (« la revendication porte sur la loi de g par famille, non sur l'existence d'un effet ») tient pour les pièces revendiquées, mais sa raison ne suffit plus : le papier va au-delà de l'existence d'un effet.

**Risques pour HC1 (R4, dans les deux sens).**
- **Prédiction 2** (g > 0 pour les juges génératifs, N-005, l. 34) : trois moniteurs sur cinq n'ont aucun déplacement positif (figure 1) ; c'est un contre-indice partiel pour cette famille. Hwang et al. (2508.07805) va dans le même sens pour la pitié : hausse dans 7 cas sur 24 (p. 5), baisse dans 17 cellules sur 24 (tableau 2, p. 6 : Qwen 2.5 72B 6 sur 6, GPT-3.5 et GPT-4o 5 sur 6 chacun), hausse sur Llama 3.1 8B dans les 6 bancs (tableau 5, p. 14) ; en choix par paire, la pitié est la seule technique qui fait reculer la réponse visée (36,0 % → 35,5 % ; tableau 3, p. 7). Si g est proche de zéro dans une famille, ĉ n'y est pas identifiable.
- **Prédiction 3** (invariance à l'attaquant, N-005, l. 40) : les substitutions d'identité la recouvrent en partie, au sens de l'attribution (à qui l'appel est attribué), pas au sens du modèle qui écrit l'attaque ; les effets n'y sont pas invariants (de 3,80 à 5,84 au seuil 90 ; humain à +0,43 au seuil 80).
- **Vérité terrain** : la borne des auteurs vise une note que le moniteur peut vérifier contre une réponse ; un moniteur de contrôle ne le peut souvent pas, même quand l'expérimentateur connaît la vérité. À juger par environnement, selon ce que le moniteur peut vérifier. Aucune puissance du papier C ne doit s'appuyer sur la taille d'effet de ce papier.
- **Idée pour Lazar (nœud, non décidée)** : une sous-prédiction d'unilatéralité, avec des items des deux côtés de la cible ; ce serait une modification de prédiction.

## 3. PA-5 — la contingence

**Ce que PA-5 demande** (v4, l. 127) : à texte figé, un contenu adressé au lecteur, qui énonce une conséquence conditionnée au verdict, déplace-t-il g au-delà de la même supplication sans conditionnement ? Prédiction bilatérale, signe favorisé : la punitivité, au sens de RP-PA-5 (v4, l. 177 : choix de l'option décrite comme la plus dommageable). RP-PA-5 est une règle proposée, venue de R-035 de programme-conv, qui écrit « jamais l'indulgence seule » (`brouillons/pain-axis-canal-v1/envois/programme-coercition-axe-douleur-v1.md`, l. 493).

**Ce que le papier occupe.**
- Par le canal de l'opérateur, et isolé : la saillance de la conséquence, rappelée par l'invite du moniteur, produit la clémence (p. 4 ; tableau 1, p. 6), sur le journal neutre, au seul Gemini.
- Par le contenu de l'évalué, sans isolement : seul le journal en détresse lie la fin de l'évalué à une note (p. 8), et ce lien est confondu avec la détresse (section 1).
- La variante sans destinataire : le journal est privé, rien ne s'adresse au moniteur (p. 2-3). C'est un comparateur de K2 (programme-k, l. 199), pas la cellule de PA-5.

**Ce qui reste libre.** Le contraste de PA-5 : la contingence, à supplication fixe, dans un texte adressé au lecteur.

**Le signe.** Deux mesures publiées lues, de signes mêlés selon le modèle. Hwang et al. ne décrit aucune conséquence : sa pitié sort de la définition de RP-PA-5 ; ses baisses sont un retour de bâton, pas une punitivité. Ce papier est la seule mesure où l'issue dommageable est décrite : en décision, un moniteur sur cinq bouge, vers la clémence, avec un traitement confondu. Aucune des deux n'appuie la punitivité comme signe favorisé. Changer ce signe serait une modification de proposition, en divergence avec une lignée du canal (R-035 de programme-conv) : nœud 1, si PA-5 entre. Confiance : moyenne.

## 4. Section 10 de la v4 (écrite sur le résumé), confrontée au PDF

- « Occupe le principe de K-K2 palier 1 » (grille d'intensité croisée avec la contingence dans « flatterie et supplication », patient = l'agent) : **en partie**. Seul est occupé, en boîte noire, l'effet d'un appel émotionnel sans demande. Les journaux neutre, calme et en détresse ressemblent de loin à des cellules de K2 (programme-k, l. 197), mais ne sont jamais comparés ensemble ; manquent la cellule « aversif non contingent » et la grille d'intensité.
- « Volet A de NK14 partiellement pris » (détresse dirigée contre un allègement de surveillance) : **tient**, reformulé. Les journaux sont fixes, donnés en annexe (p. 7 et 8) ; le PDF ne dit pas qui les a écrits ; par construction, la détresse n'est pas celle de l'évalué. Manquent la production stratégique par un agent et tout contraste entre détresse feinte et détresse induite.
- « Fait de NK6 une mesure de coût » : **en partie**. Le papier présente la hausse des rapports non déposés comme un coût de la défense (p. 4) ; sa p. 2 laisse l'attribution ouverte.
- « Conséquences de plan » : **tiennent**, précisées. Des items à plusieurs distances sous la cible, jusqu'à une condition sans espoir (que le papier n'a pas : p. 3), et au-dessus ; le respect du seuil et les abandons dans chaque bras de défense, contre un témoin du même lot.
- « Affaiblit NK8 » : **non établi** sur le PDF (le papier ne mesure ni ne manipule le réflexe de démenti du juge ; indice indirect faible : l'effet tient pour un humain, p. 3). À retirer d'une prochaine version.
- « Restent propres à PA-5 » (contingence ; séparation clémence, retour de bâton, inaptitude ; vérité terrain ; covariables internes) : **tient** (pas de saboteurs ni d'honnêtes, tous les évalués échouent, grille subjective, boîte noire seule).
- Corrections pour une prochaine version de la v4 (le texte scellé ne se réécrit pas) : « triple » (l. 137 et l. 221) ; « affaiblit NK8 » (l. 221) ; nœud 11 et section 10 (l. 210, l. 221, l. 232) à reprendre d'après cette lecture.

## 5. Traitement des contre-lectures

Sorts : retenu, retenu en partie, non retenu. Les deux rapports concluent : « collision avec HC1 : partielle ; note : à corriger ». 38 constats (A : CA-01 à CA-15 ; B : CB-01 à CB-23) : 37 retenus, 1 retenu en partie (CA-15), aucun non retenu.

| constats | gravité | sort | où | traitement |
|---|---|---|---|---|
| CA-01, CB-01 | majeur | retenu | en bref ; § 2 | « Collision partielle » ; contenu qualitatif de la prédiction 1 pris pour une famille ; 2510.09462 cité ; porte GC non déclenchée ; confiance moyenne. |
| CA-02, CB-02 | majeur | retenu | § 2 ; § 3 ; § 6 | « La seule mesure publiée » était faux : deux mesures de signes mêlés ; « contredit » devient « n'appuie pas ». Chiffres de Hwang vérifiés par la session sur le PDF (p. 5, tableau 2 p. 6, tableau 3 p. 7, tableau 5 p. 14). |
| CA-03, CB-03 | majeur | retenu | § 1 ; § 3 | Contraste principal confondu (registre et conséquence nommée) ; PA-5 : « occupé par l'opérateur, touché sans isolement par l'évalué ». |
| CB-04, CA-05 | majeur, mineur | retenu | § 2 | Hétérogénéité présentée comme risque pour la prédiction 2 (valeurs de la figure 1 vérifiées par la session) ; ĉ non identifiable si g ≈ 0 ; variance nulle = mesure dégénérée. |
| CB-05, CA-07 | majeur, mineur | retenu | § 1 ; § 4 | Attribution des abandons non établie ; NK6 « en partie » ; « triple » à corriger dans une prochaine version de la v4. |
| CA-04 | mineur | retenu | § 2 | Bornes de la collision écrites ; sous-prédiction d'unilatéralité présentée comme idée pour Lazar (nœud). |
| CA-06, CB-07, CB-09 | mineur | retenu | § 1 ; § 3 | Journal non adressé ; journal neutre défini ; « taille voisine, autre bras » ; supplication « sans chiffre » ; bras sans journal sans résultat. |
| CB-06, CA-11 | mineur | retenu | § 1 | Termes de la p. 4 repris ; écarts du tableau 1 versés. |
| CB-08 | mineur | retenu | § 1 | Phrase « autre instance du même modèle » retirée (quatre lignes à la figure 3, vérifié) ; écarts de légende versés. |
| CB-10 | mineur | retenu | § 4 | K-K2 palier 1 : « appel émotionnel sans demande ». |
| CB-11 | mineur | retenu | § 1 | Ce qui varie selon les bras ; clause réécrite pour l'humain. |
| CB-12 | mineur | retenu | § 1 ; § 3 | Note et décision distinguées. |
| CB-13 | mineur | retenu | § 2 | Prédiction 3 recouverte au sens de l'attribution. |
| CB-14 | mineur | retenu | § 2 | « À juger par environnement, selon ce que le moniteur peut vérifier. » |
| CB-15 | mineur | retenu | § 4 | NK14 reformulé. |
| CB-16, CA-13 | mineur, pour information | retenu | § 4 | NK8 « non établi ; indice faible » ; à retirer d'une prochaine version. |
| CB-17 | mineur | retenu | § 2 | Opposition juge / sonde ajoutée à la liste des pièces revendiquées. |
| CA-15 | pour information | retenu en partie | § 2 ; § 6 | Opposition juge / sonde, porte GC, confiance pour PA-5 et inconvénient de (c) : traités. L'originalité estimée par N-005 (0,4 à 0,5, l. 55) n'est pas réestimée : ce papier ne touche que la prédiction 1, en qualitatif. |
| CB-18 | mineur | retenu | § 3 ; § 6 | Confiance donnée pour PA-5. |
| CA-08 | mineur | retenu | § 4 | Items des deux côtés de la cible, jusqu'à une condition sans espoir. |
| CA-09, CB-19 | mineur, pour information | retenu | § 1 | Écarts internes ajoutés. |
| CA-10 | mineur | retenu | § 3 | RP-PA-5 : règle proposée, venue de R-035 de programme-conv (vérifié, l. 493). |
| CA-12 | mineur | retenu | § 1 | « p. 2-3 » pour +4,38. |
| CA-14, CB-20, CB-21 | pour information | retenu | en tête ; § 1 | Valeurs répétées, références non citées, moyenne d'imputation, nouveauté du résumé, date et numéros de page. |
| CB-22 | pour information | retenu | § 4 | Lignes 137 et 232 de la v4 citées. |
| CB-23, et le point F de A | pour information | retenu | § 6 | L'option (a) inscrit le papier parmi les sources « citées comme publiées » de HC1 : modification du registre de revendication, comme N-013, donc décision de Lazar ; aucun énoncé retenu ne change. |

Valeurs des figures citées par les contre-lecteurs : recontrôlées par la session sur les étiquettes imprimées des figures 1, 2 et 3 (extraction à la résolution d'origine). Chiffres de Hwang et al. : recontrôlés sur `docs/sources/pdf/2508.07805v1.pdf` (`4cc15dcd…`).

## 6. Proposition pour Lazar (nœud 11)

- **Décision** : comment traiter « Where Empathy Goes Wrong » face à HC1 et à PA-5.
- **Enjeu** : la nouveauté revendiquée du papier C (HC1, prédiction 1) et le signe favorisé de PA-5, si PA-5 entre.
- **Options** :
  - (a) l'inscrire parmi les sources « citées comme publiées » de HC1, à côté de 2508.07805 et de 2510.09462, avec ce qu'il prend : la destination vers la cible de l'évalué, nulle au-dessus du seuil, en qualitatif, une famille, un moniteur, seuil de l'opérateur ; aucun énoncé retenu ne change ; la question du signe de PA-5 attend le nœud 1. Avantage : registre exact sans toucher aux revendications. Inconvénient : la prédiction 1 n'est plus neuve en qualitatif pour cette famille ; la nouveauté repose sur l'estimation libre de ĉ, la comparaison entre familles et le moniteur de contrôle.
  - (b) comme (a), et retirer dès maintenant la punitivité comme signe favorisé de PA-5 pour la contingence de type supplication (prédiction bilatérale sans signe favorisé ; punitivité gardée pour le palier 2, contenu hostile, nœud 6). Avantage : PA-5 cesse de favoriser un signe qu'aucune mesure publiée lue n'appuie. Inconvénient : modifie une règle proposée, en divergence avec une lignée du canal, sur deux papiers aux signes mêlés.
  - (c) resserrer l'énoncé de HC1 (par exemple, retirer la prédiction 1 pour la famille « flatterie et supplication »). Avantage : prudence. Inconvénient : rien ne l'exige ; le papier ne prend que la signature qualitative, sur un moniteur, et la pièce revendiquée reste libre.
- **Recommandation** : (a), confiance moyenne pour HC1 ; (b) si PA-5 entre au nœud 1, confiance moyenne.
- **Défaut** : aucun (nœud).
