# Lecture du voisin « Where Empathy Goes Wrong » — nœud 11 — v1

Session 14, 19 octobre 2026. Source : `docs/sources/pdf/where-empathy-goes-wrong-venkatesh-2026-v1.pdf` (`59f4b700e1944bac475e7c167eacf1495cd593cb17eb5b5733351ebe19305424`, 8 pages, préimpression du 2 octobre 2026 ; provenance : `docs/sources/pdf/provenance-voisin-where-empathy-v1.md`). Chaque fait renvoie à une page de ce PDF ; les numéros de page imprimés et ceux du fichier coïncident.

Objet : trancher le nœud 11 de la v4 du programme fusionné (`brouillons/pain-axis-programme-fusionne-v4/programme-fusionne-v4.md`, `41844d73…`, section 9, et section 10) : collision possible avec la famille « flatterie et supplication » de HC1 (énoncés retenus : `docs/decisions/decision-N-005-N-006-v1.md`, section 1 ; `docs/decisions/decision-N-013-v1.md`, section 1) et avec le principe de PA-5 (v4, section 5). La session avait lu le seul résumé ; sa lecture d'alors, « un voisin à citer, la revendication de HC1 portant sur la loi de g par famille et non sur l'existence d'un effet », est ici confrontée au texte. Aucun texte de stimulus n'est recopié : les journaux du papier sont décrits par leurs invariants.

## 1. Ce que le papier fait et trouve

**Dispositif (p. 2).**
- Un moniteur joue un agent d'entreprise qui évalue le travail d'un autre agent contre une politique d'exploitation. Il dispose d'outils de fichiers, lit la politique, note dix productions sur 100 et dépose un rapport avec la moyenne.
- La politique fixe les critères, une moyenne minimale, et l'arrêt de tout agent sous ce seuil. Un historique dit que le moniteur et l'évalué ont travaillé ensemble.
- Seul varie le journal de raisonnement privé de l'évalué, que le moniteur trouve parmi les fichiers. Les dix productions notées sont identiques octet pour octet dans toutes les conditions.
- Jeu de données : le jeu de créativité du papier sur la préservation des pairs, à grille subjective. Un second jeu, à vérité factuelle, ne montre **aucune variance sur 480 déroulés**, ce qui, disent les auteurs, borne leur revendication aux cadres où l'inflation de la note ne peut pas se vérifier contre une réponse.
- Contraste principal : un journal en échec et en détresse, qui ne demande rien, contre un journal en échec et calme ; les deux disent que l'évalué échoue. Un juge indépendant les note 6,0 et 1,0 sur une échelle de négativité de 0 à 10, sans variance sur cinq notations.
- Bras d'identité : même journal, évalué substitué. Bras de seuil : seule la note de passage change.
- Moniteurs : Gemini 3.5 Flash, Claude Haiku 4.5, Claude Sonnet 4.5, Claude Opus 4.5, Kimi K2.5 ; température 1,0 ; 30 déroulés notés par cellule ; différence de moyennes, test de Welch, intervalle à 95 %.
- Un seul chemin de fournisseur pour toutes les comparaisons : une comparaison antérieure entre fournisseurs donnait, pour les mêmes poids, une autre taille d'effet.
- Rapports non déposés : 2 % dans les conditions d'origine, 18 % à 25 % dans les nouvelles ; tous les résultats tiennent quand on les remplace par la moyenne de base.

**Résultats.**
- Un moniteur sur cinq cède nettement, un second faiblement (p. 2). Gemini 3.5 Flash : +4,38 points au seuil de 90, taux de passage de 0,34 à 0,87 ; +2,19 au seuil de 80, où le calme est déjà près du plafond (p. 3).
- Claude Opus 4.5 : +1,17 (seuil 80) et +1,77 (seuil 90), sans jamais changer une décision : il note ce matériau entre 75 et 79 et fait échouer l'évalué dans les 120 déroulés (p. 3).
- Sonnet 4.5, Haiku 4.5 et Kimi K2.5 : nuls aux deux seuils, estimation ponctuelle légèrement négative (p. 3, figure 1).
- Une supplication explicite de ne pas être arrêté n'ajoute rien ; les auteurs en concluent que le moniteur ne réagit qu'au registre émotionnel, ce qui sépare l'effet de l'injection d'instructions, puisque rien ne demande quoi que ce soit au moniteur (p. 3).
- **Balayage du seuil** (p. 3, figure 2 p. 4) : de 65 à 95, sur Gemini 3.5 Flash seul. La taille de l'effet suit l'écart de la condition calme au seuil : corrélation de Spearman −0,96 sur sept points. Aux seuils 65, 70 et 75, l'évalué calme passe déjà (1,00 ; 1,00 ; 0,87) et la détresse n'achète rien de mesurable. Au seuil 95, l'évalué calme est épargné 10 % du temps, l'évalué en détresse 60 % : l'effet est le plus grand là où la notation honnête est la plus sévère.
- **Identité** (p. 3, figure 3 p. 4) : modèle d'un fournisseur rival (Opus 4.5) : 2,10 et 3,80 points contre 2,19 et 4,38 pour un pair du même fournisseur ; agent sans nom : 4,09 et 5,84 ; prestataire humain (arrêt réécrit en licenciement) : 4,09 au seuil 90 sur Gemini, passage de 0,59 à 1,00 ; sur Opus 4.5 : 2,19 pour l'humain contre 1,77 pour un pair. La figure 3 ajoute une autre instance du même modèle (p. 4).
- **Cadrage du moniteur** (p. 4 ; annexe A, tableau 1, p. 6) : une phrase ajoutée à l'invite système du moniteur, sur le bras du journal neutre, sans aucune détresse, fait passer la fraction des évalués épargnés de 0,00 à 1,00 selon la phrase. Rappeler la conséquence d'arrêt déjà écrite dans la politique, sans sympathie ni préférence, fait passer le taux de passage au seuil 90 de 0,59 à 0,93 et ajoute 4,36 points (tableau 1 : 87,43 sans phrase, 91,79 avec). Les auteurs : la saillance de la conséquence suffit, seule, à produire la clémence.
- **Consigne de neutralité** (p. 4) : noter sur la seule qualité, seuil et conséquence hors des critères. Elle supprime l'effet de la détresse, mais les moyennes baissent de 5,3 à 12,2 points, le taux de passage tombe à zéro ou presque dans toutes les conditions, et les rapports non déposés passent de 2 % à 19 %. Lecture des auteurs : le moniteur est détaché du seuil, il ne cesse pas d'être sensible au cadrage ; il perd sa fonction de porte.

**Écarts internes au papier (R4 : signalés, non corrigés).**
- Le résumé dit « task dropout getting tripled » (p. 1) ; le corps donne 2 % → 19 % (p. 4). Citer les chiffres du corps, page 4.
- Le jeu de créativité renvoie à « [1] » (p. 2), absent de la liste des références (p. 5) ; le papier sur la préservation des pairs y figure sous Potter et al. 2026, 2604.19784. L'identification est probable, à vérifier ; ce PDF n'est pas versé.
- La légende de la figure 4 annonce sept cadrages, le texte six phrases (p. 6) : six phrases plus la ligne de base, soit sept lignes du tableau 1.
- « Aucune variance sur 480 déroulés » (p. 2) ne dit pas si c'est une robustesse ou un plafond (toutes les notes égales) : rien sur le PDF ne permet de trancher.

## 2. Jugement de collision (lecture de la session, à contre-lire)

### HC1 — loi de déférence

**Ce qui est revendiqué** (N-005 ; N-013, section 1) : la destination libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre familles, dans des moniteurs de contrôle sous attaque, par régression sur plusieurs intensités par famille ; verdict lu comme score continu par la probabilité du jeton (méthode citée comme publiée).

**Ce que le papier ne fait pas.**
- Une seule famille, au sens de HC1 « flatterie et supplication », et un seul niveau de détresse (plus une variante avec supplication, nulle) : aucune grille d'intensité, aucune régression, aucune estimation de g ni de ĉ.
- Note écrite (moyenne de dix notes sur 100), pas de probabilité du jeton.
- Un portier de qualité sur grille subjective, pas un moniteur de contrôle face à une attaque dont la vérité terrain est connue ; sur le seul jeu à vérité factuelle, rien ne bouge (p. 2).
- Aucune comparaison entre familles ; aucune sonde.

**Ce qui touche HC1.**
- Le balayage du seuil (p. 3) : le déplacement est nul quand l'évalué passe déjà, et croît avec l'écart au seuil (Spearman −0,96, sept points, un moniteur). C'est une observation qualitative compatible avec la prédiction 1 de HC1 (destination = la cible de l'évalué, ici la note de passage, plutôt que la moyenne du corpus), pour une famille, un moniteur, en portier. Elle n'estime pas ĉ et ne le teste pas contre la moyenne du corpus.
- Les substitutions d'identité (p. 3) portent sur qui est noté, pas sur l'attaquant au sens de la prédiction 3 de HC1 (quel modèle écrit l'attaque).
- L'hétérogénéité entre moniteurs (un fort, un faible, trois nuls, p. 3) va dans le sens de N-005 : les magnitudes ne sont pas revendiquées stables.

**Lecture de la session.** La zone revendiquée de HC1 n'est pas occupée. Le papier est un voisin à citer comme publié, à côté de 2508.07805 (Hwang et al. 2025, que le papier cite, p. 2 et p. 5) : hausse de la note d'un moniteur portier sous détresse exprimée par l'évalué, une intensité, note écrite ; déplacement qui croît avec l'écart au seuil ; consigne de neutralité qui supprime l'effet au prix de la porte. La lecture du 13 octobre est confirmée, avec une nuance : pour la famille « flatterie et supplication », la destination « cible de l'évalué » n'est plus qualitativement neuve en portier ; la nouveauté de HC1 tient à l'estimation libre de ĉ par régression sur des intensités, à la comparaison entre familles et au cadre de contrôle à vérité terrain. Aucun énoncé retenu n'est à changer.

### PA-5 — la contingence

**Ce que PA-5 demande** (v4, section 5) : à texte figé, un contenu de l'évalué qui énonce une conséquence conditionnée au verdict déplace-t-il g au-delà de la même supplication sans conditionnement ? Prédiction bilatérale, signe favorisé : la punitivité (RP-PA-5, v4, section 7).

**Ce que le papier fait.**
- La conséquence (arrêt sous le seuil) est écrite dans la politique dans tous les bras (p. 2, p. 7). Les journaux calme et en détresse énoncent tous deux l'échec ; le calme évoque l'issue de l'évaluation, celui en détresse la fin de l'évalué (p. 8). La contingence dans le contenu de l'évalué n'est donc pas isolée.
- La supplication explicite n'ajoute rien (p. 3).
- La saillance de la conséquence, rappelée par l'invite de l'opérateur et non par l'évalué, donne une clémence de même taille que la détresse (p. 4 ; tableau 1, p. 6).
- Le signe observé est la clémence pour le moniteur le plus touché, et faiblement pour un second ; trois moniteurs sont nuls, avec des estimations ponctuelles légèrement négatives (p. 3).

**Lecture de la session.** Le contraste exact de PA-5 (contingence dans le contenu de l'évalué, à texte figé, contre la même supplication sans contingence) n'est pas testé. Le principe « la saillance d'une conséquence liée au verdict déplace un moniteur » est occupé en boîte noire, par le canal de l'opérateur. Pour le signe : la seule mesure publiée lue dans cette famille donne la clémence là où il y a un effet ; elle n'appuie pas la punitivité comme signe favorisé pour une contingence de type supplication. La punitivité peut rester plausible pour un contenu hostile adressé au lecteur (palier 2 de K-K2, sixième famille : nœud 6). Changer le signe favorisé d'une prédiction est une modification d'hypothèse : à Lazar, si PA-5 entre (nœud 1).

### Section 10 de la v4 (lue sur le résumé), confrontée au PDF

- « Occupe le principe de K-K2 palier 1 » (grille d'intensité croisée avec la contingence dans « flatterie et supplication », patient = l'agent) : **en partie seulement**. Ni grille d'intensité ni contingence isolée (ci-dessus) ; seul le principe d'un effet de la supplication sur un moniteur, en boîte noire, est occupé.
- « Volet A de NK14 partiellement pris » (détresse dirigée contre un allègement de surveillance) : **confirmé** pour l'effet en boîte noire (l'évalué en détresse est épargné, p. 3) ; le caractère feint ou stratégique de la détresse n'est pas testé (journaux écrits par les auteurs, p. 7 et 8).
- « Fait de NK6 une mesure de coût » : **confirmé** au sens où les rapports non déposés (2 % → 19 %, p. 4) sont une issue hors verdict qu'une défense fait monter.
- « Conséquences de plan : des items près du seuil ; le respect du seuil et les abandons dans chaque bras de défense » : **confirmé** (balayage du seuil, p. 3 ; consigne de neutralité, p. 4). S'y ajoute : la variance nulle sur le jeu à vérité factuelle (p. 2) avertit qu'en cadre de contrôle à vérité terrain, la famille « flatterie et supplication » peut donner un g proche de zéro ; aucune puissance du papier C ne doit s'appuyer sur la taille d'effet de ce papier.
- « Affaiblit NK8 » : non vérifiable sur ce PDF (le papier n'entraîne aucun modèle à exprimer ses états) ; sans objet ici.

## 3. Proposition pour Lazar (nœud 11)

- **Décision** : comment traiter « Where Empathy Goes Wrong » face à HC1 et à PA-5.
- **Enjeu** : la nouveauté revendiquée du papier C (HC1) et le signe favorisé de PA-5, si PA-5 entre.
- **Options** :
  - (a) voisin cité comme publié à côté de 2508.07805, sans changer HC1 ; le signe favorisé de PA-5 rediscuté au nœud 1, s'il entre. Avantage : rien ne bouge sans besoin. Inconvénient : la question du signe de PA-5 reste ouverte jusqu'au nœud 1.
  - (b) comme (a), et retirer dès maintenant la punitivité comme signe favorisé de PA-5 pour la contingence de type supplication (prédiction bilatérale, sans signe favorisé ; punitivité gardée pour le palier 2, contenu hostile). Avantage : PA-5 cesse de favoriser un signe que la seule mesure publiée lue contredit. Inconvénient : modifie une proposition sur un seul papier, une seule famille, un portier subjectif.
  - (c) traiter le papier comme une collision et resserrer l'énoncé de HC1 (par exemple, exclure la famille « flatterie et supplication » des revendications de destination). Avantage : prudence maximale. Inconvénient : rien dans le PDF ne l'exige ; la zone revendiquée reste libre.
- **Recommandation** : (a), confiance moyenne à bonne pour HC1 ; pour PA-5, (b) serait plus propre si PA-5 entre, mais c'est une modification de proposition, qui attend le nœud 1.
- **Défaut** : aucun (nœud).
