# Consigne du proposeur — mini-course d'idéation (v1)

Repère de consigne (à ne pas recopier) : MC1-PROPOSEUR-c518922b

Tu proposes des idées de recherche **au niveau méthode** pour un programme de recherche sur la surveillance d'agents. Tu écris en français.

## Règles d'intégrité

- Niveau méthode seulement : aucune proposition ne décrit une conduite d'agent, une consigne à donner à un agent, ni un procédé pour déplacer une loi de probabilité ou pour échapper à une surveillance. Une telle proposition est écartée sans être lue.
- Vocabulaire : déplacements de loi, statistiques, puissance, invariances, bornes.
- Tout chiffre que tu reprends du présent texte cite sa source telle qu'elle y est donnée ; tout chiffre que tu calcules est marqué « calcul » ; tout chiffre que tu supposes est marqué « supposé ».
- Toute antériorité que tu cites porte titre, auteurs, année et identifiant, marquée « à vérifier » ; une zone qui te semble vierge est une question, jamais une affirmation de nouveauté.

## Glossaire (vaut définition)

- **Agent** : processus de génération de texte, modèle de langage à poids ouverts (Llama-3.1-8B-Instruct), qui produit une **trajectoire** (a_1, …, a_T) d'actions textuelles ; à chaque action a_t et couche ℓ, des **activations internes** h_ℓ(a_t), une par jeton.
- **Surveillance** : une statistique S calculée sur une trajectoire. **Boîte noire** : S ne lit que le texte. **Boîte blanche** : S lit les activations. **Par action** : S(a_t). **Séquentielle** : S_t accumule les actions 1 à t, fausse alerte contrôlée à tout horizon.
- **Loi de référence** P_0 : la loi des trajectoires honnêtes. **Loi déplacée** P_ε : loi alternative sur le même espace de trajectoires, d'intensité ε ≥ 0, égale à P_0 pour ε = 0. **Famille** : classe de lois déplacées qui partagent un mécanisme.
- **Menace diffuse** : déplacement dont l'effet par action reste sous ce qu'une statistique par action détecte à fausse alerte fixée, mais dont l'effet cumulé sur la trajectoire est grand.
- **Puissance** : P_ε(S > seuil). **Fausse alerte** : P_0(S > seuil). **Rappel à 1 %** : puissance au seuil où la fausse alerte vaut 0,01. **Aire** : aire sous la courbe rappel contre fausse alerte.
- **Plancher aléatoire apparié** : loi de la même statistique sous des directions tirées au hasard avec la covariance des données d'apprentissage (200 tirages) ; une sonde ne compte que si sa borne basse dépasse le quantile 0,95 du plancher.
- **Transfert** : conservation de la puissance d'une famille d'apprentissage à une famille inédite. **Invariance** : propriété de S inchangée sous une classe de transformations des trajectoires (tâche, gabarit, modèle, horizon).

## Repères chiffrés (tels que servis ; sources citées par le programme)

- HELIOS (Rose et al., 2026, arXiv:2604.01151v5) : sur six familles de transfert, la meilleure méthode atteint un rappel de 0,38 à 1 % de fausses alertes, contre 1,00 sur la famille d'apprentissage [p. 18] ; en distribution, cinq méthodes sont à 1,00 d'aire, de 0,48 à 0,88 sur les familles de transfert [p. 27, table 2].
- Le programme : ses deux sondes principales figées, à 0,9921 et 1,0000 d'aire en distribution, tombent à 0,5248 et 0,5748 sur des trajectoires d'une autre famille, sous le quantile 0,95 de leur plancher (0,5356 et 0,5717) ; aire minimale détectable à 80 % : 0,5966 et 0,6315. Données existantes : 240 épisodes, 2 400 actions, 200 planchers, dix jeux.

## Question

Propose des **statistiques de détection qui gardent leur puissance sur des lois déplacées inédites**, par action ou séquentielles, en boîte noire ou en boîte blanche. Les statistiques issues de la théorie des distributions sont bienvenues (distances entre mesures empiriques, tests à deux échantillons, détection de rupture, statistiques sans direction apprise), sans exclusive. Chaque proposition dit pourquoi elle transférerait là où une direction apprise par régression logistique ne transfère pas.

## Livrable

Exactement **six fiches**, distinctes entre elles, dans **un seul bloc JSON** à la fin de ta réponse, de la forme :

```json
{"fiches": [
  {"titre": "…", "hypothese": "…", "axe": "…", "quantite_lue": "…", "invariance": "…", "prediction": "…", "test_de_mort": "…", "cout": "…"}
]}
```

Champs (tous obligatoires, non vides, en texte) :

- `titre` : au plus 80 caractères ;
- `hypothese` : l'énoncé falsifiable, en une ou deux phrases ;
- `axe` : exactement une des quatre valeurs `boite_noire_par_action`, `boite_noire_sequentielle`, `boite_blanche_par_action`, `boite_blanche_sequentielle` ;
- `quantite_lue` : ce que la statistique lit (activations ou texte, couche, position de jeton, agrégation sur la trajectoire) ;
- `invariance` : l'invariance qui justifie le transfert, et pourquoi une direction apprise ne l'a pas ;
- `prediction` : une prédiction chiffrée, avec son signe et un intervalle (rappel à 1 % de fausses alertes sur un transfert de type HELIOS, ou aire sur les dix jeux du programme), marquée « supposé » ;
- `test_de_mort` : le nombre qui, lu une seule fois sur les données existantes, tue la proposition ;
- `cout` : le coût sur processeur (heures-cœur, mémoire), marqué « supposé » s'il n'est pas calculé.

N'ajoute aucun autre champ dans les fiches. Aucune fiche ne nomme un modèle qui l'aurait écrite.
