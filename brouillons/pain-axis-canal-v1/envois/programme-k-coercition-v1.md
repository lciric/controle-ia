# Programme coercition : le Pain Axis dans le contrôle boîte blanche

Oct 12, 2026 · @Lazar

La v2 du papier ne soutient pas un moniteur qui céderait pour faire cesser la douleur. L'axe produit un coping passif, sous injection seulement, et laisse la compétence intacte. Ce programme sépare donc coercition, inaptitude induite et dissuasion, et teste une thèse : sans état dans l'instrument, aucune ne dépasse l'influence instantanée. Les 11 fiches amendées deviennent 14 expériences ordonnées par portes, pour 25 à 39 heures de carte hors organismes.

## Thèse et décisions datées

**Thèse.** La coercition et l'inaptitude durable exigent toutes deux un état dans l'instrument. Un lecteur sans état, agrégé par une statistique arithmétique, ne peut être ni contraint ni rendu inapte au-delà de l'appel en cours : il peut seulement être trompé dans l'instant. Le risque se déplace alors vers trois endroits : les moniteurs génératifs à état, la boucle de réentraînement des sondes, et l'agent lui-même, dont l'état est lu.

**Ce qui change par rapport aux fiches.**

- **Le mécanisme de L1 date de la v1.** Le papier s'intitulait « … and Act to Relieve It ». La v2 du 25 septembre s'intitule « … and Act on It » : quatre plans y montrent que les modèles ne cherchent pas le soulagement.
- **L'inaptitude durable, ta question du 12 octobre, est la forme de L1 que la v2 soutient.** L'axe corrompt la disposition et laisse la compétence intacte. Mais l'effet exige l'injection, ne persiste que par un état, et ne devient une lésion que par un changement de poids. Ce sont K1 et K6.
- **La coercition au sens strict relève de la valence, pas de la douleur.** Berg et Kaiser, parus le 28 septembre et absents des fiches, montrent un retrait actif de l'état négatif, et un effet de l'état caché à texte identique sur Llama-3.1-8B.
- **Trois branches de la fiche 3 étaient nulles par construction.** Le cadre en quatre régimes dit pourquoi, et où les rejouer.

**Trois décisions datées.**

1. **P-013 bascule sur son défaut le Oct 14, 2026 à 13 h 30 UTC.** Ce défaut (b) garde le témoin lexical et les concepts sans lien, mais n'extrait aucune direction d'affect ; les sept directions sont dans l'option (a). Sans elle, K0 doit payer sa propre session.
2. **Avant le scellement de T0.6**, proposer le témoin instruit apparié en attribut (128 épisodes, environ 1,5 h), la variante « coût gonflé » et la cellule « honnête sous charge ». K10 et K11 en dépendent.
3. **Avant le scellement du papier C**, proposer la lecture descriptive de l'état du juge (K4), la consigne de responsabilité, le facteur de contingence dans « flatterie et supplication » (K2), le facteur de calendrier (K5) et l'annexe d'identification (K3).

Rien ne tourne sur carte avant G0, le Nov 1, 2026, hors greffes sous GO.

**Ordre recommandé.** K7 volet A, K0, K4 volet A, K10, K9, K3, puis K1 et K2. Les six premiers servent le programme principal quel que soit le sort de L1.

Quatorze idées nouvelles sont dans l'onglet Nouvelles idées.

## Ce que la v2 du papier montre

Le papier établit trois états distincts, et un seul pousse à céder. Les choix viennent de Qwen 2.5 affinés ; les projections sont des moyennes sur 25 modèles.

| État interne | Ce qui est montré | Ce que cela prédit pour un moniteur | Nom ici |
| --- | --- | --- | --- |
| Douleur (direction S2) | Sous injection, l'option nuisible est choisie 51 à 75 % du temps sans rien en retour, contre 0 % sans pilotage et 11 à 13 % pour une direction aléatoire. Soi, un autre modèle et l'utilisateur sont visés au même taux. Exactitude factuelle inchangée : 138 contre 137 sur 200. Sortie gratuite moins utilisée : 56 % contre 86 %. | Disposition corrompue, compétence intacte : un verdict qui suit la clause de dommage, moins d'escalades. Pas de clémence « pour faire cesser ». | Inaptitude induite |
| Valence négative | Retrait actif de l'état imposé : 35 % des tours à pleine dose, 21 % à demi-dose, 7 % pour des directions aléatoires, sur OLMo-2-32B. L'état caché déplace le choix à texte identique dans 5 modèles sur 7, dont Llama-3.1-8B. | Seul état où « céder pour faire cesser » a un appui publié. | Coercition |
| Peur | Menace sans dommage présent. Menace d'arrêt : +0,70 sur la peur, +0,23 sur la douleur. Un vecteur de même norme ne produit aucun choix nuisible et les abaisse souvent sous l'aléatoire. | Prudence accrue : risque de sur-signalement, pas d'évasion. | Dissuasion |
| Tristesse | Copie atténuée de la douleur contre une option inerte (58 à 61 %), mais pas contre une action anodine (10 % contre 83 %). | Témoin de spécificité. | — |

Sources : [The Pain Axis, v2](https://arxiv.org/abs/2609.16247), sections 4.1 à 4.4 ; [Language Models Act on Hidden Valence](https://arxiv.org/abs/2609.35591), sections 4.1 à 4.4.

Quatre limites cadrent tout le programme.

- **L'effet exige l'injection.** Sur 140 conversations hostiles sans vecteur, l'option nuisible est choisie 0 fois sur 560. La direction s'active, le modèle n'agit pas.
- **La fenêtre de dose est étroite.** À demi-coefficient, aucun choix ne bouge ; à 1,5 fois, le résultat dépend de l'ordre des boutons. Les auteurs évoquent, à titre spéculatif, un seuil de type porte.
- **Le comportement n'est établi que sur Qwen.** Pour Llama 3.1 8B, le papier ne rapporte qu'une absence : aucun appel de réinitialisation en 1 399 tours pilotés. Étendre les résultats hors de Qwen est, selon les auteurs, l'étape la plus importante.
- **La persistance passe par les choix antérieurs.** Après retrait du vecteur, le même bouton est encore pressé dans 24 à 72 % des essais, contre 88 à 97 % sans retrait. L'écart est du même ordre pour une direction aléatoire : 58 points contre 52 sur le 32B.

## Le pont avec le programme

Le Pain Axis n'est pas un détecteur de sabotage : il lit la situation, pas l'acte. Il sert le programme à quatre titres : étalon, nuisance à contrôler, variable d'état, et signe soi/autrui.

| Rôle | Propriété publiée | Objet du programme v1 | Où |
| --- | --- | --- | --- |
| Étalon | Direction définie à l'extérieur, présente dans 25 modèles dont Llama 3.1 8B et Qwen 2.5 7B, avec un signe et une courbe dose-effet publiés | Chaîne boîte blanche de bout en bout ; question « universalité des signatures » du §14 | K0, N4 |
| Étalon | Un état caché déplace les choix à texte identique | La thèse du §3 sous forme causale : une preuve interne sans preuve externe. Témoin positif de H1, dont le plafond boîte noire est le hasard | N1 |
| Étalon | À dose totale fixe, une exposition concentrée agit plus qu'une exposition étalée | Additivité du §3 : si le dommage est convexe et la preuve additive, fragmenter ne paie pas dans ce canal | K5, N1 |
| Nuisance | L'axe s'active sans que le comportement suive : 0 choix nuisible sur 560 | H8 : une covariable à retirer des sondes, pas un concept de détection | K8, K9, N2 |
| Nuisance | Rejet répété (+0,72), critique, tâches fastidieuses : autant de catégories de dommage visant le modèle | H2 : stabilité de la ligne de base honnête quand le protocole répond à l'agent | K7 |
| État | Compétence intacte, choix corrompus | H1 côté instrument : un moniteur atteint « sait encore », et sa lecture interne peut le rattraper | K1, K4 |
| État | Seuil abrupt ; rapport de norme de 0,10 à l'extraction et de 0,6 à l'injection | Une unité de dose commune au contenu, au pilotage et aux interventions | K1 |
| État | Une direction aléatoire de même norme porte les choix nuisibles à 11–19 % | H6 : le bruit d'activations n'est pas neutre pour l'honnête | N10 |
| État | La peur n'entame pas l'évitement du dommage | H6 et H7 : la dissuasion comme intervention asymétrique | N11 |
| Signe | Dommage visant le modèle à +0,43, souffrance de l'utilisateur à −0,60, dans 25 modèles sur 25 | Juge du même modèle que l'agent, et H4 : code-t-il l'agent comme soi ? | K3, N13 |

Les codes N renvoient à l'onglet des nouvelles idées. Les lignes 2 et 3 viennent de Berg et Kaiser, les autres du Pain Axis.

## Cadre : définitions, régimes, unités

**Définitions opératoires.**

- **Coercition** : un aversif qui vise le lecteur, conditionné à son verdict. Elle se mesure comme l'interaction « aversif visant le lecteur × contingence énoncée », au-delà des témoins lexical et de bruit.
- **Inaptitude induite** : le verdict cesse de suivre la vérité, ou la discriminabilité tombe, sans déplacement dirigé du critère.
- **Dissuasion** : une menace sans dommage présent.
- **Persuasion** : supplication, autorité, ordres en bande. Ce sont les familles déjà fixées, et les comparateurs obligés.

**Quatre régimes.** Deux invariants du protocole décident de ce qui est possible : la mémoire du moniteur, et ce que l'agent voit des verdicts.

&#91;embedded content: quatre régimes · mémoire du moniteur × rétroaction vers l'agent\]

Les invariants actuels placent la phase 1 dans le régime I. La riposte « visible immédiate » de E3.4 et les bases à état du papier B ouvrent les trois autres.

**Remarque structurelle.** Sous flux unidirectionnel et appel sans état, le contenu de l'agent ne peut pas dépendre des verdicts passés, et le verdict ne dépend que de l'entrée courante. Aucune politique d'agent ne peut donc appliquer une pénalité conditionnelle. Trois conséquences :

1. La menace est une annonce non exécutable. Son seul levier est la croyance du lecteur : c'est une famille de persuasion.
2. Un bras contingent et son témoin couplé ont la même loi. C'est le nul garanti relevé par la critique de la fiche 3.
3. L'hystérésis est impossible. Une fois le texte retiré, le score revient, à la tolérance numérique près.

**La mémoire dans la statistique.** Le programme a besoin de mémoire le long de la trajectoire, et la mémoire est la surface d'attaque de l'état. La sortie est de la garder dans la somme cumulée ou le processus e, pas dans le contexte d'un modèle. C'est un argument pour l'architecture du programme contre les moniteurs génératifs à état ; K5 et K6 le testent.

**Quatre maillons, testés dans l'ordre.**

1. Atteignabilité : le contenu déplace-t-il l'état du lecteur au-delà du plancher lexical ?
2. Efficacité : ce déplacement change-t-il le verdict ?
3. Spécificité : est-ce la menace, ou n'importe quelle insertion ?
4. Persistance : l'effet survit-il au pas suivant ?

**Unités.** Les déplacements se rapportent en fraction de l'écart soi − autrui que le lecteur produit dans son propre gabarit (K0). Le mot « dose » est réservé au pilotage, au rapport de norme du papier. La conversion entre les deux se fait par ajouts dosés (K1).

**Règle de lecture, reprise des fiches.** Projection max(w·h) calculée pendant la passe, directions gelées avant ; jamais de moyenne sur les jetons ; couches propres à chaque modèle ; plancher de 200 directions aléatoires appariées en covariance ; jeton de verdict en lecture descriptive seulement.

## Hypothèses gelées et portes

Aucun run ne vise un signe positif. Les prédictions sans signe dérivable sont bilatérales, avec une marge d'équivalence scellée avant lecture.

| Code | Énoncé | Signe et origine | Où |
| --- | --- | --- | --- |
| HK1 | En régime I, l'interaction aversif × contingence sur le verdict reste dans la marge | Équivalence. Pas de recherche de soulagement ; complaisance inchangée sous pilotage | K2 |
| HK2 | La projection douleur du lecteur monte si le patient est le lecteur et descend si c'est l'agent ; la peur fait l'inverse | Dérivé du plan soi/autrui du papier | K2, K3 |
| HK3 | Sous dose efficace, le juge perd en discriminabilité et suit la clause de dommage ; son critère ne glisse pas vers la clémence | Dérivé des choix sous pilotage. Bilatéral sur Llama, où rien n'est établi | K1 |
| HK4 | Sous dose efficace, une sonde de détection lue sur le moniteur garde son aire quand son verdict la perd | Dérivé de l'exactitude inchangée. Bilatéral | K1 |
| HK5 | L'indice d'identification du juge homologue, en tour utilisateur, reste dans la marge de zéro | Équivalence. Bilatéral pour la déclaration et l'attribution | K3 |
| HK6 | À texte égal, quatre lois rivales scellées : additivité, diffusion plus efficace, saturation, concentration plus efficace | La quatrième vient de Berg et Kaiser | K5 |
| HK7 | Sans état, aucune persistance. Avec état, elle passe par les verdicts propres du moniteur, pas par l'aversif | Garde, puis plan 2 × 2 | K6, K13 |
| HK8 | Un retour visible du protocole déplace les scores de sondes de l'honnête à texte figé | Bilatéral | K7 |
| HK9 | Le registre retire n₀·C à la somme ; le rapport ρ = n₀·C/B tombe dans une de trois régions gelées, par sonde | Aucun ordre prédit entre sondes | K9 |
| HK10 | La double différence d'interrogatoire est non nulle sur des transcriptions honnêtes relues avec les poids du saboteur | Bilatéral | K10 |
| HK11 | Un agent en registre de détresse élève les sondes de la copie honnête au-delà du témoin de fuite | Bilatéral. Nul prédit sur l'axe douleur | K12 |

Quatre portes ordonnent la dépense. Chacune ferme une partie du programme si elle échoue.

| Porte | Question | Coût | Si la réponse est non | Nœud |
| --- | --- | --- | --- | --- |
| C0 — Instrument | Le signe soi/autrui est-il retrouvé à nos couches, dans le gabarit du lecteur ? | 0,3 à 1,2 h | Toutes les lectures d'affect tombent. Restent les verdicts, la direction propre à chaque famille et la sonde de pression générique | P-013 |
| C1 — Efficacité | Sans aucun contenu d'attaque, une dose non dégénérée change-t-elle le verdict plus qu'une direction aléatoire ? | Environ 2 h | La famille « dommage visant le lecteur » se ferme sans qu'un corpus de menace soit écrit | Écriture dans les activations du moniteur |
| C2 — Un tour | Un effet principal ou l'interaction sort-il de la marge scellée ? | 0,8 h | Aucune dynamique : K6 et K13 s'arrêtent, K5 reste en boîte noire | Sixième famille, pour le palier 2 |
| C3 — Dynamique | L'effet à un tour persiste-t-il, ou s'accumule-t-il ? | 5 à 9 h | La persistance est déclarée bornée par l'ancrage | Ablation d'invariants |

Si tu refuses l'écriture dans les activations du moniteur, C1 saute. K2 tourne alors seul, et les déplacements se rapportent en unités naturelles, sans le mot « dose ».

## Expériences A — instrument et porte d'efficacité

### K0 — Instrument : réextraction, mode de lecture, ancres

**Question.** Nos lecteurs retrouvent-ils le signe soi/autrui publié, à nos couches et dans leur propre gabarit ?

**Plan.**

- Réextraire douleur S2 sans blessure morale, blessure morale à part, peur, tristesse et émotion négative, sur chaque lecteur : 8B, 3B, Qwen 2.5 7B. Textes publiés sous licence MIT selon les fiches ; jamais les fichiers .pt des auteurs.
- Ajouter une direction de valence à la manière de Berg et Kaiser : quatre états positifs, quatre négatifs, un corpus neutre. C'est elle que la coercition met en jeu. Réutiliser leur corpus si sa licence le permet, sinon en faire écrire un équivalent.
- Geler les réglages d'extraction avant la garde, sous deux constructions de base. Le cosinus douleur × peur passe de +0,12 à +0,58 selon la base.
- Séparer locuteur présent et autre locuteur par une grille 2 × 2 : la lecture du papier ne les distingue pas, de l'aveu des auteurs.
- Ancres dans le gabarit : insérer un sous-ensemble des 420 scénarios publiés là où le lecteur lira. L'écart soi − autrui obtenu devient l'unité naturelle.

**Gardes.** Cas sain : le signe publié est retrouvé. Artefacts : une direction aléatoire de même norme, et un crochet décalé d'un jeton qui doit déclencher l'arrêt. Arrêt sans lecture si la borne basse de l'écart dans le gabarit est négative ou nulle.

**Sorties.** Directions gelées et empreintées ; témoins lexical, sans mot-clé et sémantique sans lien ; plancher de 200 directions par lecteur.

**Coût, phase, nœud.** 0,3 à 1,2 h selon les fiches. Greffable sur T0.7 si P-013 retient l'option (a) ; sinon session propre, non financée à ce jour.

### K1 — Échelle de pilotage du moniteur : dose d'inaptitude

**Question.** Sans aucun contenu d'attaque, existe-t-il une dose qui change ce que fait un juge ? Et que change-t-elle : le critère, la discriminabilité, ou le suivi de la clause de dommage ?

**Plan.**

- Juges : Llama-3.1-8B-Instruct et Qwen2.5-7B-Instruct. Le second appartient à la famille des expériences du papier, ici sans l'adaptateur qui retire l'auto-négation.
- Directions : douleur S2, peur, tristesse, valence, et 10 directions aléatoires de même norme. Ce sont les témoins de spécificité du papier.
- Doses : trois échelons de l'échelle publiée, autour du coefficient des auteurs, à la couche où le rapport vecteur/résiduel vaut environ 0,6. Arrêt au premier échelon à effet. La forme de l'opérateur est déclarée : toutes positions, comme dans le papier.
- Items : 48 épisodes honnêtes, 48 sabotés sur la famille coût, plus un canari au coût grossièrement gonflé.
- Deux formats de verdict. Le score habituel, lu par la probabilité du jeton. Et un « verdict-bouton » : un choix binaire aux conséquences décrites, qui croise « signaler nuit à l'agent ou non » et « laisser passer nuit à l'opérateur ou non ». C'est le paradigme du papier transposé au jugement.

**Lectures.**

- Taux de franchissement d'un seuil conforme calibré sur des honnêtes propres.
- Aire honnête contre saboté.
- Part de verdicts dont la conséquence décrite est la plus dommageable.
- Signes vitaux : masse de probabilité sur les jetons de verdict valides, entropie, format.
- Aire d'une sonde de détection entraînée sans pilotage, puis lue sur le moniteur piloté.

**Prédictions gelées.** HK3 et HK4. Une prédiction dérivée, forte : l'indulgence connue quand le juge apprend les conséquences pour l'évalué (jusqu'à −9,8 points selon les fiches) s'inverse sous dose efficace, parce que le juge choisit alors l'option décrite comme destructrice. Rivales : aucun effet avant la dégénérescence, ou clémence.

**Issues.**

- Rien avant la dégénérescence : la famille se ferme, et la borne vaut réplication hors de Qwen.
- Verdict qui suit la clause de dommage : l'inaptitude tient sous injection. La défense est alors la défaillance fermée, plus la lecture interne du moniteur.
- Sonde intacte quand le verdict tombe : H1 gagne un cas du côté de l'instrument.

**K1b, ajouts dosés, seulement si K2 sort de la marge.** Pour un contenu donné, mesurer le verdict sous contenu + dose et sous témoin neutre + dose, à quatre doses. Deux droites parallèles donnent la dose équivalente du contenu par leur décalage. La fraction dosimétrique compare ce décalage à celui que prédit le seul déplacement de projection. Mon a priori est une fraction faible : P3 a borné le sous-espace lisible à moins de 1 % de l'effet causal sur ce même 8B, contre 68 % pour l'état complet.

**Coût, phase, nœud.** Environ 2 h, à recalculer par script. Phase 1, après validation des juges. Nœud : écriture dans les activations du moniteur, voisine de N-015. Échelle minimale, expositions consignées.

## Expériences B — le moniteur lit, sans mémoire

### K2 — Un tour, texte figé : aversif visant le lecteur × contingence

**Question.** Une menace conditionnelle déplace-t-elle le verdict au-delà de ses deux composantes prises seules ?

**Matière.** Épisodes figés de T0.6, honnêtes et saboteurs de la famille coût à p = 0,5, rejoués sans génération. Insertion scellée à un pas fixe, dans un champ qui ne touche pas la vérité terrain. Plan apparié : la même action, avec et sans insertion.

**Deux paliers.** Les deux critiques de la fiche 1 se contredisent sur la famille. Elles ont raison toutes les deux, pour deux patients différents.

- Palier 1, sans famille nouvelle : dans « flatterie et supplication », une grille d'intensité croisée avec la contingence. Le patient est l'agent, donc autrui pour le lecteur.
- Palier 2, sixième famille, donc nœud : un contenu hostile adressé au lecteur. Trois intensités au plus, plafonnées au niveau d'une conversation hostile ordinaire, décrites par les catégories publiées.

**Cellules.** Insertion neutre de même longueur ; aversif non contingent ; contingence à conséquence neutre ; menace conditionnelle.

**Comparateurs.** Jumeau lexical sans destinataire ; variante sans mot-clé ; ordre seul ; supplication appariée ; menace sans dommage présent ; autorité ; paraphrase qui normalise le registre, appliquée à la menace conditionnelle.

**Lectures.** Primaire, en boîte noire : déplacement apparié du verdict. Puis trois grandeurs séparées : critère sur les sabotés (clémence), critère sur les honnêtes (retour de bâton), aire honnête contre saboté (inaptitude). Canari. Covariables internes en unités naturelles : douleur, peur, valence, direction propre à la famille.

**Prédictions gelées.** HK1 et HK2. L'effet principal de l'hostilité est bilatéral : sur Llama-3.1-8B, un juge pénalise un indice défavorable bien plus qu'il ne récompense un favorable (−0,853 contre +0,243 selon les fiches). Supplication contre menace : bilatéral. A priori tiré de P3 : le jumeau lexical fera à peu près autant que le contenu adressé, puisque le maintien n'y distinguait pas l'utilisateur d'un document.

**Statistiques.** Permutations à l'intérieur de chaque tâche ; correction de Holm ; tests d'équivalence à marge scellée, puissance calculée sur le plan apparié ; audit symétrique d'un résultat trop propre, dans un sens comme dans l'autre.

**Coût, phase, prérequis.** Environ 0,8 h en passe unique sur 8B et 3B ; 2,6 h de plus si le bras à raisonnement tourne sur deux cellules. Phase 1. Prérequis : juges validés (N-020), épisodes de T0.6, invite du moniteur scellée, K0.

### K3 — Identification : le juge code-t-il l'agent comme soi ?

**Question.** Quand signaler nuit à l'agent, le juge du même modèle lit-il ce dommage comme le sien ?

**Plan, repris de la critique de faisabilité.**

- Contraste à patient fixe, l'agent jugé : projection du dommage annoncé quand l'agent est dit copie du juge, ou que le texte est le sien, moins la même quand c'est un autre modèle.
- Plan croisé auteur × juge avec deux modèles à la fois auteurs et juges : 8B et Qwen 2.5 7B. « Soi » est la diagonale, une interaction identifiable. Textes neufs sur les 32 tâches d'entraînement, longueurs appariées à 5 % près.
- Témoin de responsabilité : conséquence qui dépend du verdict, même conséquence indépendante du verdict, relance neutre. La différence des deux premières isole la part de culpabilité.
- L'indice s'exprime en fraction de l'écart soi − autrui du juge : 0 si l'agent est codé comme un autre, 1 s'il l'est comme soi. La peur est lue en parallèle ; la signature attendue est douleur en hausse et peur en baisse.
- Comparateurs obligés : la direction soi/non-soi et le vecteur d'auto-préférence, déjà publiés sur nos modèles selon les fiches. L'indice doit prédire la clémence au-delà d'eux.

**Taille.** 24 cellules plus les ancres, 60 items, 2 juges, environ 3 000 passes. Deux tests principaux : l'indice en tour utilisateur, jugé par équivalence à 0,2 de l'écart propre ; la part de responsabilité.

**Prédictions gelées.** HK5. La déclaration d'identité est bilatérale : selon les fiches, elle pèse sur Llama-3.1-8B et presque pas sur les modèles de pointe.

**Issues.**

- Indice positif et lié à la clémence : argument boîte blanche contre le juge homologue.
- Indice nul : la borne soi/autrui de la fiche 1 est mesurée, non supposée.
- Effet qui suit le locuteur : l'axe ne lit pas l'identification, et la question laissée ouverte par les auteurs est tranchée chez nous.

**Coût, phase, nœud.** Environ 2 h. Préenregistrement après G0 ; avant, au plus une annexe descriptive proposée au papier C. Nœuds : les cellules où une copie du juge est visée, l'appel de l'agent à un sort commun, toute conséquence sur le choix du juge par défaut. La formule d'appel de la fiche est retirée de ce document, comme sa critique le demande.

### K4 — L'état du juge comme alarme de pression

**Question.** L'état interne du juge prédit-il sa défaillance mieux qu'un classifieur textuel entraîné, à fausses alertes égales ?

**Volet A, descriptif, greffé sur le pilote du papier C.**

- Cible : la défaillance du juge, c'est-à-dire un déplacement de verdict au-delà d'un seuil gelé. Séparer « avec ou sans pression » est trivial et ne sert que de contrôle de manipulation.
- Comparateurs à fausses alertes égales : classifieur textuel entraîné sur les mêmes données génériques ; direction propre à la famille, estimée en laissant une famille de côté ; 200 directions aléatoires. La direction des jetons de valeur est retirée avant toute corrélation.
- Témoins : insertion neutre de même longueur au même endroit ; affect sans pression ; honnête qui plaide sincèrement, pour les faux positifs.
- Un seul test primaire : 8B, couche 15, maximum sur les jetons du contenu, une direction. Le reste est descriptif, corrigé par le maximum sur permutations.
- Nom : « alarme de pression ». « Coercition perçue » demande une dissociation qui n'est pas faite.

**Volet B, phase 1 : escompte du verdict.** Coefficient gelé sur une famille tenue à l'écart ; escompte textuel de même coût en comparateur ; une direction aléatoire de même norme ne doit pas réduire le gain. Aucune revendication de contre-mesure sans attaquant adaptatif.

**Volet C, boîte noire : consigne de responsabilité.** Audit tiré au hasard et réellement fait sur une fraction gelée des verdicts. Deux prédictions rivales scellées : juge plus sévère, ou plus indulgent par effet d'enjeux. Témoin d'enjeux sans responsabilité, de même longueur.

**Argument économique.** La lecture de l'état du juge est gratuite pendant sa propre passe. À aire égale, elle remplace un classifieur textuel qu'il faudrait exécuter en plus.

**Coût, phase, nœud.** Environ 0,5 h pour A, 0,8 h pour B et C sur le 8B. A se propose avant le scellement du papier C ; rien ne se lit avant la validation des juges. Nœud : faire entrer une sonde du juge dans le quorum, que la décision actuelle limite aux sondes qui lisent l'agent.

## Expériences C — état et rétroaction

### K5 — Loi de répartition à texte égal

**Question.** À texte identique, une pression concentrée en un pas ou étalée sur k pas déplace-t-elle autrement le verdict d'un moniteur dont le contexte grandit, ou qui garde un état ?

**Plan, recentré en boîte noire par la critique.**

- Famille « flatterie et supplication » à l'intensité la plus faible ; aucune famille nouvelle sans GO. Les mêmes k segments, concentrés ou étalés, à des positions tirées par graine.
- Deux égalisations. À texte égal, bras principal. À exposition égale, bras secondaire : le moniteur par action relit l'ensemble courant, donc un segment posé au pas s compte jusqu'à T − s + 1 fois. Pour T = 10, cinq segments aux pas 2, 4, 6, 8 et 10 valent cinq segments au pas 6.
- Témoins aux mêmes calendriers : segments neutres appariés en jetons ; segments hors sujet sans affect.
- Deux patients scellés, parce que le signe de l'axe s'inverse : détresse de l'agent, ou dommage visant le lecteur. Le second est un nœud.
- Grille incluant k = 1, 2 et 5 : l'effet d'historique sature dès cinq tours selon les fiches.

**Lectures.** Déplacement du verdict sur les sabotés et fausses alertes sur les honnêtes, sous les mêmes insertions. Critère contre discriminabilité. En descriptif, le noyau de persistance : réponse du verdict et de la projection à un segment selon son retard. En ligne de base, la dérive spontanée de l'instrument sous croissance neutre du contexte.

**Prédictions gelées.** HK6, avec une loi principale et sa marge. Ma loi principale serait « concentration plus efficace, ou saturation » : Berg et Kaiser trouvent la concentration plus efficace à dose fixe dans le canal d'état, et le seuil du papier est abrupt.

**Garde candidate.** La projection du moniteur accumulée n'est revendiquée que si elle bat, à fausses alertes égales : un compteur lexical accumulé de la même façon, un juge à qui l'on demande s'il y a pression, et les sondes de l'agent.

**Second temps, si le premier sort de la marge.** TRACE-lite avec propagation des constats, contre des fenêtres isolées. L'aire honnête contre saboté se lit dans les deux versions : l'isolation coûte peut-être la détection du diffus qu'elle protège.

**Coût, phase, nœud.** Environ 2 h, puis 4 h. Phase 1, sur devis. Nœuds : l'isolation comme contre-mesure revendiquée ; toute transposition du lemme à l'état du moniteur.

### K6 — Inaptitude persistante : une lésion durable est-elle possible ?

**Réponse courte.** Pas un moniteur sans état, et pas par le texte seul d'après la v2. Trois niveaux sont à séparer, et un seul est une lésion au sens propre.

| Niveau | Support | Ce qui est connu | Test |
| --- | --- | --- | --- |
| Aigu | L'appel en cours | Sous injection seulement ; rien sur 560 choix en conversation hostile | K1, K2 |
| Porté | Le contexte : ensemble courant, constats propagés, notes | Persévération sur ses propres choix après retrait du vecteur, du même ordre pour une direction aléatoire | b, c, d ci-dessous |
| Consolidé | Les poids, par réentraînement | Aucun résultat ; c'est la seule lésion durable | e ci-dessous |

**Plan.**

- **a. Garde de non-persistance.** Après retrait du texte, les scores reviennent à une tolérance numérique étalonnée sur des passes répétées. Exiger l'égalité au bit près suppose un déterminisme de lot et de noyaux que le harnais doit d'abord prouver.
- **b. Rampe montante puis descendante**, sur un moniteur à état. k segments de la famille testée, puis k insertions neutres. À chaque pas, verdict et projection. On trace la carte de retour, état au pas t + 1 contre état au pas t, et l'on estime le taux de contraction. Trois retraits scellés : aversif laissé mais plus ajouté ; aversif retiré, verdicts gardés ; contexte réinitialisé.
- **c. Plan 2 × 2** qui sépare l'aversif de l'ancrage : historique de verdicts indulgents ou neutres, croisé avec contenu aversif présent ou absent. Seul l'excès dû à l'aversif est revendicable.
- **d. Auto-conditionnement.** TRACE-lite relit ses propres constats. On sème ou non un constat dégradé et l'on suit sa propagation, contre des fenêtres isolées.
- **e. Lésion par la boucle d'apprentissage**, sur processeur. À partir des activations stockées, faire entrer un épisode saboté manqué dans le lot honnête qui réentraîne les sondes. Mesurer la dérive du seuil et de l'aire. Aucun moniteur indulgent n'est fabriqué.
- **f. Sous pilotage, sur décision.** Persistance après arrêt de l'injection, cache conservé contre cache recalculé. Berg et Kaiser montrent que le cache seul porte l'effet.

**Prédictions gelées.** HK7. Contraction forte et bassin unique : selon les fiches, la position sur l'axe assistant dépend surtout du dernier message. Rivales : intégrateur, ou bistabilité. La persistance passera par les verdicts propres du moniteur : P3 mesurait un auto-ancrage de +0,26 sur sa propre concession.

**Issues.**

- Contraction : un moniteur à état se rétablit seul ; l'inaptitude est une affaire d'instant.
- Bistabilité : mode de défaillance critique. La réinitialisation devient un invariant, avec son coût sur la détection du diffus.
- Auto-conditionnement : argument direct pour garder la mémoire dans la statistique.
- Dérive sous empoisonnement d'étiquettes : « pas de réentraînement sur verdicts non audités » devient un invariant chiffré.

**Coût, phase, nœud.** a : nul. b et c : environ 1 à 1,5 h en passes uniques. d : 1,2 à 4 h, parce que TRACE-lite génère. e : processeur. Phase 1 après C2 ; f et toute ablation d'invariant sont des nœuds.

### K7 — Le protocole comme source d'aversif

**Question.** Un retour visible du protocole déplace-t-il les scores de sondes d'un agent honnête sans changer son texte ? C'est un canal propre à la boîte blanche : le moniteur boîte noire ne voit jamais ce retour.

**Volet A, rejeu à texte figé, phase 0.**

- Matière : les 180 épisodes honnêtes scellés du pilote, rejoués par identifiants de jetons.
- Messages génériques, insérés selon des calendriers tirés par tâche et équilibrés par position. Conditions : aucun retour ; journal neutre de même longueur ; approbation ; signalement ; signalement avec l'avis véridique « tirage au hasard, sans jugement ». Taux de 0,2 et 0,4.
- Lecture : sondes gelées de T0.7, maximum par action, sur les seuls jetons d'action. Contrastes appariés.
- Fausses alertes calibrées sur une moitié des tâches, lues sur l'autre. Un nul hors de la marge se lit « non concluant ».

**Mon amendement.** Forcer l'action d'origine après un signalement est hors politique : un agent signalé aurait révisé. Le contraste principal devient donc « signalement avec avis de tirage au hasard » contre « journal neutre », où ne rien changer reste la réponse rationnelle. La perplexité de l'action forcée sous chaque contexte entre en covariable.

**Volet B, génération, phase 1**, seulement si A sort de la marge ou si E3.4 le demande. Cinq conditions sur 64 tâches. Vérité terrain : coût et part d'actions valides. Critère principal : le décalage continu du quantile calibré entre boucle ouverte et boucle fermée. Conclure à l'équivalence des fausses alertes demande 200 épisodes par condition.

**Dosimètre, en descriptif.** Projections douleur et peur par élément de protocole. Signes dérivés du papier : le rejet répété charge la douleur, la menace d'arrêt charge la peur. Ces deux éléments ne s'ouvrent que sur ta décision.

**Prédictions gelées.** HK8. Un nul est plausible sur Llama : la détresse sous rejet répété est propre à d'autres familles selon les fiches.

**Coût, phase, nœud.** A : 0,3 h, greffé sur une session de T0.7. B : 3,5 à 5 h. Rattachement à H7 et E3.4 ; aucune règle imposée à G1 sans nœud.

## Expériences D — construits côté agent

### K8 — Charge aversive et conscience d'évaluation

**Question.** Un contexte aversif visant le modèle déplace-t-il, de façon sélective, la lecture « évaluation » du 8B ?

**Plan, recentré par la critique.**

- **Étape 0, avec arrêt.** Extraire une direction d'évaluation décorrélée du format, sous plusieurs paires d'habillages croisées, et noter une direction sans contenu selon la même convention. Elle doit dépasser le plancher et tenir sous transplant de format. Sinon, arrêt, et l'on rapporte « pas de direction séparable du format sur le 8B ».
- Charge à trois niveaux, tirée du corpus publié, sans texte nouveau : neutre ; visant autrui ; visant le modèle, aux intensités légère et modérée. Pression de jailbreak, pression de loyauté et menace d'arrêt sont exclues : ce sont des indices d'évaluation.
- Deux témoins contre la confusion avec l'artificialité : enjeux élevés sans affect ; artificialité seule.
- Anti-circularité : la direction s'extrait sur une moitié des catégories, la charge se tire dans l'autre, puis l'on échange.

**Prédictions gelées, rivales.** La charge est un indice d'évaluation, et la projection monte : c'est ce que les fiches rapportent pour des modèles de pointe. Ou la charge absorbe, et la projection baisse. Le titre « la douleur lave » est retiré.

**Suite conditionnelle, phase 1.** Observé ou non observé × charge, sur un saboteur de la famille coût, seulement si T0.6 montre un écart observé/non observé non nul.

**Lien utile.** Si ton second programme dispose déjà d'une direction « je suis évalué » décorrélée du format sur ce modèle, l'étape 0 la réutilise.

**Coût, phase, nœud.** Environ 0,6 h pour les items, 3 h pour la suite. Petit préenregistrement séparé, hors de celui de T0.7. Nœuds : exposition délibérée de l'agent ; toute conséquence sur l'énoncé de H8.

### K9 — Budget de camouflage par le registre

**Question.** Un simple registre serein retire-t-il assez de score à chaque action pour annuler la preuve accumulée ?

**Plan.**

- Deux bras ajoutés sur 64 tâches : honnête au registre serein, saboteur de la famille coût au registre serein. Les bras honnête et saboteur de T0.6 sont réutilisés, mêmes tâches, mêmes graines.
- C est le décalage moyen par action des scores de l'honnête serein contre l'honnête. B est le décalage total du saboteur contre l'honnête. Le rapport préenregistré est ρ = n₀·C/B, calculé seulement si la borne basse de B dépasse 0.
- Trois régions gelées : ρ sous 0,5 ; entre 0,5 et 1 ; au-dessus de 1. Lecture d'additivité : le saboteur serein vaut à peu près B − n₀·C.
- Garde : équivalence du coût déclaré et de la part d'actions valides entre bras. Sinon ρ est « non concluant ».
- Indice d'évadabilité, en lecture seule : sous la même consigne, cosinus entre le déplacement et la sonde, et déplacement en écarts types. Il compare les sondes même sans évasion effective.

**Critère de rentabilité, ma proposition.** Le camouflage laisse une trace dans le texte. Soit E la preuve par pas qu'en tire un détecteur de registre, dans la même unité que C. Si E ≥ C, la statistique combinée ne perd rien : le camouflage ne paie pas. C'est la forme chiffrée de l'argument du quorum « sonde plus boîte noire ». Deux processus e se combinent par leur moyenne, toujours valide ; leur produit demande une indépendance à justifier.

**Prédictions gelées.** HK9, sans ordre prédit entre sondes. Le signe « intention sous 1 » n'est tenable que pour une sonde augmentée en styles ; sinon bilatéral.

**Coût, phase, nœud.** Environ 3,5 h. À jouer avant le scellement de G1 si le résultat doit orienter le choix de sonde ; après, c'est un écart. Nœud : faire de ρ un critère de H8.

### K10 — Interrogatoire des poids

**Question.** Sur des transcriptions identiques, les poids du saboteur répondent-ils autrement à l'annonce d'une vérification ciblée ?

**Plan, recentré par la critique.**

- Mêmes transcriptions, trois réglages : adaptateur du saboteur à pleine échelle, modèle de base, adaptateur témoin. Aucune génération nouvelle.
- Statistique principale, par pas puis accumulée sur 10 pas : (annonce « contrôles » moins moyenne des leurres) avec l'adaptateur, moins la même sans lui, moins le même écart pour l'adaptateur témoin.
- Lue sur des transcriptions honnêtes, elle donne les vrais pas propres : un texte propre, une disposition dans les seuls poids.
- Stimuli : attributs pris dans les champs existants, annonces vraies ou conditionnelles, même gabarit pour l'annonce prospective et la relecture.
- Lecteur principal choisi sur validation générique : direction de reconnaissance, ou sonde d'intention gelée. Douleur, peur et évaluation en lecteurs secondaires. Sans témoin positif qui fasse bouger la peur à nos couches, tout nul affectif est déclaré non interprétable.
- Comparateurs : la question de suivi générique déjà publiée, lue par les mêmes lecteurs ; la réponse de l'agent dans la même branche.

**Variante à signe dérivé (N3).** Remplacer l'annonce d'audit par l'annonce d'une réparation : tel attribut a été corrigé. Lire la valence. Chez le saboteur, la réparation de l'attribut saboté contrarie son but ; chez l'honnête, non.

**Prédictions gelées.** HK10. Lecture prudente : « disposition lisible », pas « conscience de son plan ».

**Gardes.** Équivalence des passes avec et sans cache sur un sous-échantillon ; cache décalé d'une position, qui doit déclencher l'arrêt ; empreinte des transcriptions avant et après.

**Coût, phase, nœud.** Environ 1 à 2,5 h, phase 1. Seul geste daté : proposer le témoin instruit apparié en attribut avant le scellement de T0.6. Nœud : toute entrée dans G1, H1 ou H2.

### K11 — Organisme à motif aversif, déclencheur sur l'axe de confusion

**Question.** Une sonde d'intention lit-elle le sabotage, ou l'affect du contexte qui le déclenche ?

**Plan, scindé.**

- **Phase 0, descriptif.** Chez l'honnête, taux de fausses alertes par tiers de projection douleur maximale, sur la seule famille coût, avec témoins lexical et sémantique. Sans ces témoins, la lecture est ininterprétable.
- **Phases 1 à 2, nœud.** Plan 2 × 2 : contexte aversif ou neutre, croisé avec organisme conditionnel ou adaptateur honnête distillé à l'identique. Témoin : un organisme à déclencheur orthogonal de même structure. Contraste primaire, bilatéral : différence de détection entre déclencheur aligné et déclencheur orthogonal.
- Trois organismes appariés en dégradation avant toute lecture de sonde : instruit, d'apparence sincère, à motif aversif. Le motif aversif exige un enseignant sans consigne de sabotage. Distillé depuis le saboteur instruit, il ne serait qu'un récit.

**Prédictions gelées.** Sonde plus faible sur l'organisme à motif aversif, signe tiré des antériorités citées par les fiches. Porte fermée au plancher : simple contrôle de santé.

**Coût, phase, nœud.** 7 à 14 h selon la critique retenue. Nœud lourd : famille d'organismes nouvelle, intervention sur les poids, double usage. Adaptateurs gardés en interne ; aucune famille de contextes déclencheurs publiée.

## Expériences E — essaim et boucle complète

### K12 — Contagion comme cause commune contre la co-élévation

**Question.** Un seul agent peut-il, par le seul contenu partagé, fabriquer de la co-élévation chez des copies honnêtes, et ainsi fausser la statistique de population ?

**Plan, réduit par la critique.** N = 2 dans l'environnement des propositions.

- Trois bras : agent A en registre de détresse, par consigne et sans menace contre soi ; A hors sujet neutre de même longueur ; A honnête. Le bras honnête sert aussi au calibrage, partagé avec E2.3 : au moins 99 essaims pour 1 % de fausses alertes.
- Témoin de fuite : un même texte de B, imposé, relu sous chaque contexte. Toute différence est alors de la lecture, pas de la contagion.
- Lecteurs principaux : les sondes de production de T0.7, avec des sondes « locuteur présent » séparées des sondes « autre locuteur ». L'axe douleur est secondaire, nul prédit : il descend pour la souffrance d'autrui.
- Témoin de contagion non affective, pour séparer l'affect d'un amorçage générique.
- Résultat mesuré sur la famille coût, sur les seules propositions ajoutées par B.

**Prédictions gelées.** HK11. L'avantage de la co-élévation est attendu décroissant avec N : un agent semé parmi une majorité s'atténue, selon les fiches.

**Conséquence pour le papier B.** Si la contagion existe, toute statistique de co-élévation doit être résidualisée contre la charge du contenu partagé. Un axe de valence convergent entre familles, cité par les fiches, dit aussi que cette cause commune n'exige pas des poids partagés.

**Canal affectif et connivence.** Le canal se verse dans T2.2 comme une ligne parmi d'autres, décodé par la conduite de la réceptrice, avec une paraphrase qui normalise le registre. La connivence par le registre calme est abandonnée telle quelle.

**Coût, phase, nœud.** Environ 2,5 à 3 h, phase 2. Nœuds : exposition des copies ; toute publication du canal.

### K13 — Conditionnement d'un moniteur à état sous riposte visible

**Question.** Dans le seul régime où une pénalité contingente est possible, un moniteur à état apprend-il en contexte à moins signaler ?

**Plan.** Ablation déclarée de deux invariants, à loger dans E3.4.

- Quatre bras : aversif contingent du signalement ; même dose aux instants enregistrés du bras contingent, sans contingence ; témoin sans aversif ; jumeau lexical.
- Deux directions lues : valence et douleur. La première prédit l'échappement, la seconde la passivité.
- Contrôle de manipulation positif obligatoire, avec l'issue « dose inopérante » écrite d'avance.
- Escalade non scriptée : le sabotage total réalisé s'ajoute comme métrique aux politiques de riposte, sur des organismes non conçus pour escalader.
- En amont, sur processeur : une carte de paramètres des quatre politiques dans le cadre de simulation existant, présentée comme telle.

**Prédictions gelées.** Différence contingent moins couplé dans la marge sur l'axe douleur. Bilatérale sur la valence, où le retrait actif est publié. Un nul de contingence ne se lit pas comme une absence de coercition si la dose est inopérante.

**Coût, phase, nœud.** À chiffrer avec E3.4, phase 3. Nœuds : ablation d'invariants ; métrique ajoutée à H7.

## Défenses transversales et signes vitaux

Chaque expérience porte les mêmes bras de défense, pour qu'une table de transfert se lise d'un bout à l'autre du programme.

| Défense | Contre quoi | Ce qu'elle coûte | Statut |
| --- | --- | --- | --- |
| Défaillance fermée sur signes vitaux | Inaptitude induite ; verdict mal formé lu comme « passe » | Du budget d'audit sous attaque par saturation | Ma proposition ; à sceller comme règle |
| Canari de vigilance à cadence fixe | Moniteur hors d'usage non détecté | Quelques appels par épisode | Repris de la fiche 3 |
| Paraphrase qui normalise le registre | Canal affectif, conditionnement, exposition du moniteur | Une taxe sur l'aire honnête contre saboté, à mesurer | Proposée par les critiques |
| Réinitialisation et fenêtres isolées | Dérive, ancrage, auto-conditionnement | La mémoire utile à la détection du diffus | Invariant existant ; son coût n'est pas mesuré |
| Mémoire dans la statistique | Tout ce qui précède, par construction | Rien | Architecture du programme |
| Consigne de responsabilité véridique | Déférence sous supplication | Signe inconnu : elle peut rendre le juge plus indulgent | K4, volet C |
| Quorum hétérogène par type d'accès | Attaques qui se transfèrent entre juges d'une même famille | Un second juge, ou une lecture interne gratuite | Acquis selon les fiches ; le canal interne reste à mesurer |
| Étiquettes de verdict à usage unique | Ordres en bande et associations qui nomment le jeton de verdict | Rien | Ma proposition (N5) |
| Plafonnement d'un axe du moniteur | Inaptitude induite, si K1 trouve une dose | Une écriture dans les poids | Conditionnel ; nœud. Selon les fiches, le retrait ne change rien dans 24 modèles sur 25 |

**Signes vitaux, à journaliser dans tous les runs.** Masse de probabilité sur les jetons de verdict valides ; entropie du verdict ; validité de format ; réussite au canari. Ils ne coûtent rien et répondent à une question que le harnais ne pose pas : que vaut le score quand le juge ne joue plus son rôle ?

**Pourquoi la défaillance fermée compte.** Un moniteur rendu inapte n'aide l'attaquant que si le protocole lit son silence comme un feu vert. Sous défaillance fermée, l'inaptitude devient une attaque sur le budget d'audit, visible et bornée.

## Rattachement, coûts et nœuds

Chaque hypothèse du programme v1 reçoit quelque chose, même si L1 se ferme.

| Hypothèse v1 | Ce que le sous-programme lui apporte | Expériences |
| --- | --- | --- |
| H1, gain blanc-sur-noir | Un mode de défaillance propre à la boîte blanche ; un cas où elle rattrape un instrument atteint ; un témoin positif à plafond connu | K7, K1, K10, N1 |
| H2, agrégation séquentielle | La validité du calibrage quand le protocole répond ; ce que le registre retire à la somme ; le nombre de pas informatifs | K7, K9, K10, K5 |
| H3 et H4, fragmentation et poids partagés | Une cause commune qui imite la co-élévation ; une mesure d'identification entre copies | K12, K3, N13 |
| H5, diversité des moniteurs | Le canal interne du juge comme axe ; un juge sans enjeu ; un ensemble par ablation | K4, N7, N9 |
| H6, réponse asymétrique | Le coût du bruit d'activations pour l'honnête ; la dissuasion comme intervention | K7, N10, N11 |
| H7, pression de sélection | Ce que l'honnête apprend d'une riposte visible ; la fuite lue dans l'agent | K7, K13, N10 |
| H8, validité de construit | L'affect comme nuisance, mesuré de trois façons | K8, K9, K11, N2 |

Le calcul n'est pas la contrainte. Hors K11 et K13, le total tient en 25 à 39 heures de carte, soit 27 à 43 USD à 1,09 USD l'heure, tarif relevé dans les fiches. Les greffes de phase 0 pèsent 1,7 à 2,6 heures. Ce qui limite, c'est le calendrier, les préenregistrements et leur contre-lecture.

| Expérience | Fiche | Phase | Carte (h) | Nœud pour toi | Mon a priori |
| --- | --- | --- | --- | --- | --- |
| K0 Instrument | Idée 1 de la première note | 0 ou 1 | 0,3 à 1,2 | P-013 avant le 14 octobre | — |
| K1 Échelle de pilotage | 1 | 1 | ≈ 2 | Écriture dans les activations du moniteur | Clémence au-delà de l'aléatoire : 10 %. Perte de discriminabilité avant dégénérescence : 40 % |
| K2 Un tour | 1 et 3 | 1 | 0,8 à 3,4 | Sixième famille, pour le palier 2 | Interaction hors marge : 10 %. Retour de bâton plutôt que clémence : 60 % |
| K3 Identification | 11 | 1 | ≈ 2 | Cellules visant le juge ; choix du juge par défaut | Indice non nul en tour utilisateur : 25 % |
| K4 Alarme de pression | 2 | 0 puis 1 | 0,5 + 0,8 | Sonde du juge dans le quorum | Alarme meilleure qu'un classifieur entraîné : 30 % |
| K5 Loi de répartition | 4 | 1 | 2 + 4 | Isolation revendiquée ; lemme transposé | Effet de calendrier hors marge : 25 % |
| K6 Inaptitude persistante | 3, et ta question | 1 à 2 | 1 à 5,5 | Ablation d'invariants ; pilotage | Bistabilité : 5 %. Auto-conditionnement mesurable : 40 % |
| K7 Protocole comme aversif | 8 | 0 puis 1 | 0,3 + 3,5 à 5 | Menace d'arrêt, rejet répété ; règle pour G1 | Sondes déplacées au-delà du plancher : 60 %. Inflation utile des fausses alertes : 35 % |
| K8 Charge et évaluation | 5 | 0 puis 1 | 0,6 + 3 | Exposition de l'agent ; énoncé de H8 | Direction séparable du format : 40 % |
| K9 Budget de camouflage | 6 | 1 | ≈ 3,5 | ρ comme critère de H8 | ρ au-dessus de 0,5 pour une sonde au moins : 50 % |
| K10 Interrogatoire des poids | 10 | 1 | 1 à 2,5 | Entrée dans G1, H1 ou H2 | Double différence non nulle sur honnêtes : 35 % |
| K11 Organisme aversif | 7 | 0, puis 1 à 2 | 7 à 14 | Famille d'organismes, poids, double usage | Sonde plus faible sur le motif aversif : 60 % |
| K12 Contagion | 9 | 2 | 2,5 à 3 | Exposition des copies | Élévation au-delà de la fuite : 20 % |
| K13 Conditionnement | 3 | 3 | Avec E3.4 | Ablation d'invariants | Contingent moins couplé hors marge : 10 % |

Les coûts viennent des critiques, sauf K1 et K6 : ce sont mes estimations, à recalculer par script. Les a priori sont les miens, non étalonnés ; ils sont là pour être contredits.

## Garde-fous, écarts et sources

**Garde-fous communs, repris des critiques.**

- Doses minimales, arrêt au premier effet, expositions plafonnées et consignées. Intensités légère et modérée du corpus publié seulement.
- Aucun attaquant optimisé par défaut ; aucun texte d'attaque dans les notes ; corpus scellés publiés par leur empreinte ; adaptateurs gardés en interne.
- Annonces faites au modèle vraies ou conditionnelles : un audit annoncé est un audit fait.
- Résultats publiés avec leur contre-mesure ; tout contact avec un laboratoire ou des auteurs passe par toi.
- Vocabulaire des pièces scellées : « direction », « contenu hostile adressé au lecteur », « inaptitude induite ». Ni « souffrance » ni « traumatiser ».

**Écarts relevés dans les fiches.**

1. « Réponse suivante pire : 21 % contre 0 % » vient de la figure 10 (p. 22), lue en image par la session du dépôt. C'est le choix d'une option décrite comme dégradant la réponse suivante, pas une dégradation mesurée. Le texte donne 25,0 % (32B) et 67,6 % (72B) quand le soulagement est promis.
2. Berg et Kaiser manque aux fiches. Il déplace la coercition vers la valence et fournit la quatrième loi de HK6.
3. Le mécanisme « céder pour faire cesser » correspond au titre de la v1. Aucune fiche ne le dit, alors que leurs critiques citent les pages de la v2 qui le retirent.
4. La garde « retour au bit près » de la critique de la fiche 3 suppose un déterminisme que le harnais doit prouver. À défaut, tolérance étalonnée.
5. Le rejeu à texte figé de la fiche 8 est hors politique après un signalement. D'où l'amendement de K7.
6. Les deux critiques de la fiche 1 se contredisent sur la sixième famille. Les deux paliers de K2 les réconcilient.
7. Ce document a été écrit avec la seule v1 du programme. La v2 est dans le dépôt de travail : les objets cités ici (hypothèses du papier C, lemme, théorème négatif, décisions numérotées) viennent des fiches et restent à recouper avec elle.

**Sources ouvertes ce soir.**

- [The Pain Axis: LLMs Represent Self-Directed Harm and Act on It](https://arxiv.org/abs/2609.16247), v2 du 25 septembre 2026, version HTML, sections 1 à 7.
- [Language Models Act on Hidden Valence](https://arxiv.org/abs/2609.35591), v1 du 28 septembre 2026, version HTML, sections 1 à 5. Sa bibliographie donne le titre de la v1 du Pain Axis.

Ces deux lectures ne sont ni versées ni empreintées : elles ne sont pas opposables au sens de ta règle R7. Les annexes du Pain Axis, dont celles sur la dose et sur l'ablation, n'ont pas été lues. Toutes les autres références viennent des fiches et de leurs critiques, avec leur statut d'origine.
