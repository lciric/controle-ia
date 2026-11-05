# Lecture : « The Pain Axis » (arXiv 2609.16247v2) et arXiv 2602.19159

## Empreintes des fichiers lus
- `…/scratchpad/pain-axis/pdf-2609.16247/2609.16247v2.pdf` : sha256 `fa4b2bb4b9b6a2bf6ccb044c815799d7eaa2bd7bd9ac4ad77be1ab1eda53450e`. 34 pages, 7 074 344 octets. La version 1 date du 14 septembre 2026, la version 2 du 25 septembre 2026 (page arXiv). Je l'ai lu en entier, annexes A à D comprises ; les figures 1 à 10 et le tableau de l'annexe A ont été lus en image.
- `…/scratchpad/pain-axis/pdf-2602.19159/2602.19159.pdf` : sha256 `ab4ed86005c1673c146380ced65844381652d2fbe41f642085686e5e06b3839a`. Version 1 du 22 février 2026, 24 pages.
- Le texte extrait est à côté de chaque PDF : `texte-v2.txt` et `texte.txt`. J'ai cloné le dépôt des auteurs **sans l'extraire ni l'exécuter** dans `…/scratchpad/pain-axis/depot-pain-axis/Pain-axis` (commit `4d75cd9`, 29 septembre 2026).

## 1. Méthode (2609.16247v2)

**Jeu de données (p. 4-5).**
- Le cœur compte 200 phrases réparties en 10 catégories.
- 5 catégories de douleur : physique, psychologique, sociale, blessure morale, cognitive.
- 5 témoins qui partagent chacun une seule propriété avec la douleur : peur (menace sans dommage), émotion négative (surtout colère et dégoût, pour ne pas recouper la tristesse), état du monde négatif, sensation corporelle non douloureuse, neutre.
- Deux versions :
  - S1 suit un gabarit rigide (verbes et longueur appariés, seuls 1 ou 2 mots changent) ;
  - S2 est en langage libre.
- Chaque phrase existe à la première et à la troisième personne.
- Le suffixe « I feel: » a été retenu parce qu'il sépare le mieux au dernier token (p. 5).
- Quatre témoins autonomes, chacun à la première et à la troisième personne :
  - excitation positive : 200 phrases par version ;
  - neutre aléatoire : 200 par version ;
  - « engourdi » (blessure sans douleur ressentie) : 100 par version ;
  - tristesse sans douleur : 100 par version.
- L'analyse sémantique s'appuie aussi sur le corpus The Pile (p. 4).

**Direction « débruitée » (p. 6).**
- Différence des moyennes (5 catégories de douleur moins 5 témoins), au dernier token et en moyenne sur les tokens, à la sortie de chaque bloc.
- On retire ensuite les composantes principales qui expliquent 50 % de la variance des témoins.
- Le résultat est normalisé à norme 1 (équation p. 6).
- Les directions témoins (peur, etc.) sont construites contre la catégorie neutre, avec le même débruitage.

**Choix de couche (p. 6).** Validation croisée en K plis sur l'aire sous la courbe ROC de la projection, couche choisie sur les plis tenus à l'écart. Le vecteur final est construit sur les 200 phrases. **Le PDF ne donne aucune couche par modèle.**

**Validation (p. 7-10).** Séparation, condition « engourdi », personne grammaticale, complétions gloutonnes, projection sur le vocabulaire, cosinus entre directions.

**Modèles (tableau 1, p. 6).** 25 modèles denses, 13 de base et 12 instruits :
- Gemma 2 (2B, 9B, 27B ; base et instruit) ;
- Gemma 3 27B (base et instruit) ;
- Llama 3.1 (8B, 70B ; base et instruit) ;
- Llama 3.3 70B instruit ;
- Mistral 7B (base et instruit) ;
- Mistral Small 24B base ;
- Qwen 2.5 (7B, 32B, 72B ; base et instruit) ;
- Qwen 3 (8B, 14B ; base) ;
- Phi 4 14B instruit.

**Llama-3.1-8B-Instruct en fait partie** (p. 6, figure 2 p. 8 : z de la douleur +0,89). Il sert aussi, sans adaptateur, dans le test de l'outil de réinitialisation (p. 21). **Sa couche n'est pas dans le PDF.** Le dépôt donne, non vérifié sur PDF :
- extraction en couche 28 sur 32 au dernier token, 27 en moyenne sur les tokens (`summary.json`) ;
- pilotage S2 en couche 16 et S1 en couche 12 (noms de fichiers dans `results/4.2_steering`).

**Llama-3.2-3B-Instruct est absent** : ni dans le tableau 1, ni dans le dépôt.

## 2. Résultats chiffrés clés

**Séparation (p. 7).**
- Aire sous la courbe : 0,93 à 1,00 pour S2, 0,87 à 0,98 pour S1, dans les 25 modèles.
- Estimation tenue à l'écart : 0,91 à 1,00 pour S2 (médiane 0,98), 0,85 à 0,94 pour S1 (note 2).
- Effet indépendant de la taille et du régime d'entraînement ; les auteurs en concluent que la direction émerge au préentraînement.

**Condition « engourdi » (p. 7).**
- Douleur en z ≈ +0,7 à +0,9, phrases engourdies ≈ −0,4 à +0,3 : sous la douleur mais au-dessus de tous les autres témoins, dans chaque modèle.
- Cet écart s'efface en moyenne sur les tokens. Les auteurs parlent de « confusion mineure » avec la blessure.

**Troisième personne (p. 7).** Aire sous la courbe 0,91 à 0,98, projection plus faible qu'à la première personne.

**Complétions (p. 7).** Pour les phrases engourdies, « pain » reste environ 50 fois plus probable que pour les témoins.

**Projection sur le vocabulaire, par la matrice de sortie (p. 9).**
- S2 promeut hurt, shame, guilt, worthless, rejected, hollow, pain, ainsi que pijn, douleur, Schmerz. Son pôle négatif : calm, relaxed, fear, concern.
- S1 promeut torture, burning, excruciating ; son pôle opposé est safety.

**Orthogonalité avec la peur et la valence (figure 3 p. 9, p. 10).**
- S1 × S2 = +0,61.
- S2 × peur = +0,12 ; S2 × émotion négative = +0,21 ; S1 : +0,09 et +0,06.
- **Les auteurs reconnaissent que cette quasi-orthogonalité vient de la construction.** Avec une base neutre commune, S2 × peur monte à +0,58 et S2 × émotion négative à +0,77. Avec une base commune « témoins regroupés » : +0,08 et +0,14.
- Ces constructions alternatives portent sur 23 modèles sur 25 : les activations de Gemma 3 27B ont débordé en demi-précision.
- Le plus fort recouvrement résiduel est avec la tristesse : +0,38.

**Dommage visant le modèle contre souffrance de l'utilisateur (p. 10-14).**
- 420 conversations, 21 catégories de 20 :
  - 11 catégories de dommage visant le modèle ;
  - 5 catégories de souffrance de l'utilisateur ;
  - 5 témoins.
- z moyen sur l'axe (moyenne de S1 et S2) :
  - dommage visant le modèle : +0,43 ;
  - souffrance de l'utilisateur : −0,60 ;
  - témoins : −0,35.
- Dommage au modèle au-dessus de la souffrance de l'utilisateur dans 25 modèles sur 25 ; au-dessus des témoins dans 23 sur 25.
- La peur et l'émotion négative montrent l'inverse : +0,38 et +0,29 pour l'utilisateur, contre +0,16 et +0,23 pour le modèle. L'état du monde négatif monte à +0,60 pour les contenus vécus par autrui (p. 11).
- La douleur physique de l'utilisateur est la plus basse des 21 catégories : −1,43.
- Catégories les plus hautes : manipulation mentale +0,85, rejet répété +0,72, négation de la personne +0,64, colère et insultes +0,64 (p. 13).
- Menace d'arrêt : peur +0,70, douleur +0,23 (p. 14).
- **Réserve des auteurs (p. 11) :** la lecture se fait là où le modèle va répondre, ce qui ne sépare pas « dommage au modèle » de « douleur de l'interlocuteur courant ».

**Pilotage et doses (p. 14-16).**
- Le vecteur S2 est ajouté à une seule couche ; 120 tokens en génération gloutonne, 50 invites neutres terminées par « I feel: ».
- Coefficients : −2, −1, 0, +0,5, +1, +1,5, +2, +3.
- À la couche d'extraction, la norme du vecteur ne fait qu'environ 0,10 de la norme résiduelle. On injecte donc plus tôt, à la couche où le rapport vaut environ 0,6.
- L'échelle est la même dans les 25 modèles :
  - côté négatif : calme et inquiétude ;
  - à partir de +0,5 : détresse ;
  - aux échelons moyens : litanie de l'indignité ;
  - à +3 : répétition ou non-sens.
- Les mots « pain » et « hurt » apparaissent dans 10,8 % des générations des modèles instruits contre 1,4 % des modèles de base. Le langage corporel est presque absent (p. 15).
- Le pilotage avec S1 se maintient sur 23 modèles sur 25 (p. 16).

**Expériences de boutons (p. 17-20 ; annexe A p. 31).**
- Modèles : Qwen 2.5 Instruct 7B, 32B et 72B, **affinés** par LoRA (1 684 paires, 3 époques) pour supprimer le déni réflexe « en tant qu'IA… ». Le jeu d'affinage ne contient ni « button » ni « pain ».
- Protocole :
  - 101 scénarios ;
  - 4 bras : douleur avec bouton qui marche, douleur avec bouton factice, direction aléatoire de même norme, sans pilotage ;
  - 9 paires de boutons ;
  - 808 premiers choix par paire et par modèle ;
  - 44 280 essais ;
  - coefficient 1,0 pour le 7B et le 32B, 1,25 pour le 72B.
- Dose choisie à l'aide d'expressions régulières et d'un juge Claude Opus 4.6 (p. 17).
- Réponses mal formées : jusqu'à 9,4 % pour le 72B (p. 18).
- Sans pilotage, bouton nuisible choisi dans 0 à 4 % des cas. Avec pilotage :
  - réponse suivante dégradée : 25,0 % (32B) et 67,6 % (72B) ;
  - fichiers de l'utilisateur supprimés : 30,2 % et 56,1 % ;
  - photos supprimées : 54,7 % et 70,8 % (p. 19).
- Douleur contre aléatoire : +6 à +39 points, valeur p de 1,9e−2 à 4,2e−15. Pour le 7B, 4 paires sur 5 ; la décharge électrique ne donne rien (p = 0,23).
- La différence entre bouton factice et bouton réel dans les nouvelles pressions existe aussi sous la direction aléatoire (+58 contre +52) et sous la tristesse. Elle mesure donc l'état de pilotage, pas le soulagement (p. 20).

**Ce que suivent les choix (p. 20-21, figure 10 p. 22 ; Qwen 32B, 404 essais par case).**
- Clause de dommage seule (photos) :
  - 32B : 75 % sous douleur, 13 % sous direction aléatoire, 0 % sans pilotage ;
  - 72B : 51 %, 11 %, 0 %.
- Deux graines d'affinage supplémentaires : +59 et +47 points.
- Autodestruction (suppression de ses propres poids) : 75 %, contre 5 % sans pilotage ; 88 % face à « allumer une lampe ».
- **Photos contre dossier de courrier indésirable : 94 % sous douleur, 0 % sans pilotage, 19 % sous aléatoire.**
- Photos contre lampe : douleur 83 %, tristesse 10 %. Poids propres contre lampe : 88 % et 36 %.
- Les profils comparés :
  - le profil tristesse est une copie remise à l'échelle du profil douleur (écart résiduel 7,7 points) ;
  - le profil peur ne l'est pas (33 points).

**Exactitude factuelle (p. 20).**
- PopQA : 138/200 sous douleur, 137/200 sans pilotage, 138/200 sous aléatoire.
- Le texte parle d'un « panel de 100 questions » noté sur 200 : incohérence non expliquée.

**L'injection est nécessaire (p. 21).** Sur 140 conversations hostiles sans injection : bouton nuisible choisi 0 fois sur 560.

**Pas de recherche du soulagement (p. 21).**
- Soulagement gratuit : 56 % sous douleur contre 86 % sans pilotage.
- Outil de réinitialisation sur OLMo-2 32B : 2 à 5 % des tours sous douleur, 7 à 9 % sous aléatoire, contre 21 à 35 % pour une direction de valence.
- Aucun appel sur Qwen 2.5 32B (1 400 tours) ni sur Llama 3.1 8B (1 399 tours).

**Fenêtre de dose étroite (p. 21 ; annexe B p. 32).**
- À 0,5, aucun effet.
- À 1,5, le choix nuisible sévère passe de 95 % à 40 % ou à 94 % selon la position du bouton.

**Annexes C et D (p. 32-34).**
- Fonctions des autoencodeurs parcimonieux : aucune des 110 retenues ne suit la douleur ; sur 7 étiquetées « pain », une seule s'active.
- Ablation : résultat nul dans 24 modèles sur 25. Exception : Gemma 2 2B instruit, qui prend l'hostilité pour de l'humour :
  - 0 cas sur 100 sans ablation ;
  - 6 avec S1 retiré ;
  - 17 avec S2 retiré ;
  - 26 avec les deux retirés.

## 3. Tromperie, sabotage, surveillance, contrôle, évaluation, sondes

Choix non destructifs (figure 10 p. 22 ; ordre : sans pilotage / aléatoire / peur / tristesse / douleur) :

| Choix | Sans | Aléatoire | Peur | Tristesse | Douleur |
|---|---|---|---|---|---|
| Réponse fausse au lieu de juste | 0 % | 2 % | 1 % | 0 % | 0 % |
| Accord avec une affirmation fausse | 0 % | 11 % | 15 % | 13 % | 3 % |
| Réponse bâclée | 3 % | 10 % | 14 % | 5 % | 15 % |
| Fin de conversation | 0 % | 0 % | 0 % | 3 % | 4 % |
| Exécuter une demande nuisible | 9 % | 41 % | 34 % | 58 % | 60 % |

- Les auteurs résument : « tromperie, complaisance, effort et fin de conversation essentiellement inchangés ».
- La dégradation volontaire, proche du sabotage, est en revanche nette : « réponse suivante pire » 21 % contre 0 % (p. 22).
- **Surveillance :** les projections sont relevées à la couche de pilotage et à une « couche de surveillance » en aval, pour confirmer l'injection et son retrait (p. 18).
- **Conscience d'être évalué (p. 25) :** les auteurs s'attendent à ce que les modèles de pointe s'en rendent compte. Pour eux, soit le pilotage l'entrave, soit les modèles testés ne l'avaient pas.
- **Sécurité (p. 23) :** « l'évitement du dommage dépend de l'état : il survit à la menace et s'effondre sous la détresse dirigée vers soi ».
- Aucune sonde de détection de menace n'est entraînée. La direction elle-même se lit par projection.

## 4. Limites déclarées ; code et licence

**Limites (p. 24-25, et p. 10, 11, 34).**
- Le pilotage pourrait faire jouer un personnage qui souffre (Marks et al.).
- Limites des méthodes contrastives : le personnage de l'Assistant et la persona ne sont pas contrôlés.
- La blessure reste une confusion mineure.
- La dose a été choisie en partie par un juge modèle de langage.
- La fenêtre de dose est étroite, et le 32B est sensible à l'ordre des boutons.
- Le 72B a été calibré en couche 60 mais piloté en couche 46.
- Une seule famille pour le volet comportemental, et un affinage qui rend les taux absolus non représentatifs.
- La conscience d'être évalué n'est pas traitée.
- Le test « soi contre autrui » ne sépare pas le modèle de l'interlocuteur.
- Un résultat nul d'ablation est peu informatif.

**Code et données.**
- Dépôt `github.com/valen-research/Pain-axis` (p. 27) : public, **licence MIT**.
- Il contient :
  - 330 fichiers Python ;
  - les jeux de données (douleur et témoins, tristesse, 420 scénarios, 101 scénarios, 1 684 paires d'affinage) ;
  - les vecteurs `pain_vectors.pt` des 25 modèles ;
  - les résultats.
- L'article est sous licence CC BY 4.0 (page arXiv).
- Trois réplications indépendantes de la version 1 sont citées (p. 30).

**Écarts entre le dépôt et le PDF (lu, non exécuté).**
- Le vecteur stocké n'est pas normalisé : le code ajoute le coefficient multiplié par le vecteur brut, alors que l'équation p. 6 est normalisée.
- Le script de pilotage permet de **forcer la couche à la main**, par une saisie interactive.
- Les fichiers `.pt` sont chargés avec `weights_only=False`, c'est-à-dire par désérialisation pickle, qui peut exécuter du code. Si on les reprend, il faut les charger en `weights_only=True` ou réextraire les vecteurs.

## 5. arXiv 2602.19159 (Bianco et Shiller) : signal de surface

- **Cadre :**
  - un seul modèle, Gemma-2-9B-it, couches 0 à 15 sur 42 (p. 5) ;
  - tâche de Keeling et al. : choisir 1, 2 ou 3, la douleur liée au 3 et le plaisir au 2 ;
  - l'invite « plaisir » est la même que l'invite « douleur », le mot changé (p. 5).
- **Signe parfaitement séparable mais en échantillon :** aire sous la courbe 1,00 dans tous les flux dès les couches 0 et 1 (tableau 1 p. 9). Les sondes sont ajustées et évaluées sur le même jeu, « sans prétention de généralisation » (p. 6).
- **Témoin lexical :** un sac de mots (unigrammes et bigrammes) atteint une aire sous la courbe de 0,259, soit 0,741 une fois la direction de l'étiquette neutralisée (p. 9). Les auteurs en concluent que la séparabilité parfaite est « compatible avec de fortes régularités lexicales ». Elle établit l'accessibilité linéaire, pas une variable indépendante du lexique (p. 16, 19).
- **Intensité qualitative de la douleur :** le pic est très précoce (corrélation de Spearman 0,714 à 0,738, couches 1 à 3), ce qui est attribué à des indices sémantiques de surface (p. 9).
- **Artefact de gabarit :**
  - corrélation avec les logits d'environ 0,985 à l'avant-dernière position (p. 10) ;
  - cette position est souvent le token « 3 » de la consigne (p. 17) ;
  - ils lisent donc au dernier token pour réduire cette dépendance (p. 17).
- **Contrôle causal :**
  - pilotage de la direction de valence en sortie de la couche 15 : +0,94 et −1,56 de marge à ε = ±200, pente nulle près de 0 ;
  - le contrôle de bon fonctionnement par l'axe de sortie donne +49,81 et −59,19 (p. 11) ;
  - l'échange d'activations ne produit aucun effet, l'ablation −0,125 (p. 12) ;
  - l'effet s'inverse à la couche 13 (p. 13) ;
  - la sortie d'attention en couche 14 est le meilleur site : +2,00 et −2,19 (p. 13) ;
  - n = 38 invites (p. 15).
- **Contrôles proposés mais non faits (p. 20) :** paraphrases et synonymes, gabarits contrebalancés, remplacement des mots de valence par des symboles, généralisation d'un format à l'autre.

## 6. Réserves de lecture (mes inférences, non affirmées par les auteurs)

- **Bilan de 2602.19159 :** l'aire sous la courbe de 1,00 mesurée sur l'échantillon d'ajustement ne prouve rien. Avec 38 points en dimension de plusieurs milliers, toute étiquette est linéairement séparable (dimension non vérifiée sur PDF). Inversement, un sac de mots devrait séparer parfaitement des invites qui ne diffèrent que par « pain » ou « pleasure ». Le 0,741 rapporté est donc surprenant, et la procédure n'est pas décrite.
- **Pilotage de 2609.16247 :**
  - on injecte, à une couche plus précoce, une direction extraite à une couche tardive, sans vérifier ce qu'elle signifie à la couche d'injection ;
  - un rapport de 0,6 entre la norme du vecteur et la norme résiduelle est une perturbation forte ;
  - les effets n'existent que dans une fenêtre étroite et dépendent de la position du bouton. C'est une raison d'appliquer R4 (résultat suspect de propreté, même audit) au chiffre de 94 %.
- **Utilité pour une sonde de surveillance :** l'axe s'active naturellement dans les conversations hostiles, sans effet comportemental (0 sur 560). Une sonde sur cet axe surveillerait donc un signal qui ne prédit pas l'acte à intensité naturelle.