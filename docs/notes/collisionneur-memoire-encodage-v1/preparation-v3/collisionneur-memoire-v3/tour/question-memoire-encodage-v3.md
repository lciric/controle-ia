# Question pour le collisionneur — encoder la mémoire du pôle pour qu'elle améliore vraiment les propositions de génération en génération et empêche les redites — v3 (brouillon de conv-audit ; session-depot fige sa version)

Écrite par l'instance nouvelle de conv-audit le 27 octobre 2026, à partir de 08:18 UTC (heure lue sur `date -u`), sur le
mot de Lazar de 09:17 heure de Paris (« amende-la en v3 si tu veux, avant que session-depot la fige »).
**Remplace la v2** (`question-collisionneur-memoire-encodage-v2.md`,
`9149db147b43a10d915cd44612a882ef9b1070acd4f7084f18b88bdcf0431e5d`, branche `canal/conv-audit-relais-memoire-v1`, commit
`6ffcf86`, gardée sans modification ; elle remplaçait elle-même la v1 du message n° 97). **Ce qui change, et rien
d'autre** : (i) un fait acquis ce matin sur le critère des filles ; (ii) au point 2, la redite « modulo les
transformations aveugles » et les signatures invariantes ; (iii) au point 3, viser les régions de chance de survie
intermédiaire ; (iv) la pièce J2. Forme, modèles, tours, refus et dépense : inchangés.
Mot de Lazar (dans la session de l'instance sortante, 27 octobre, 09:09 heure de Paris), verbatim : « demande a la
nouvele instance un brainstor sur les meilleures maniere d'encoder une mempire qui ameliore vraiment les propositions de
generation en generation et evite de redonner les memes choses, lance aussi le collisionneur dessus ».
Forme « arbitre », trois modèles, trois tours, une tentative par cellule, un refus arrête le tour. Dépense : sur le mot
direct de Lazar dans la session de session-depot.

## Question

« Un pôle de recherche automatique fonctionne par générations : des fiches d'hypothèses sont gelées (prédiction signée
et chiffrée, nul, seuil qui peut échouer) ; chaque fiche **engage une loi prédictive** des issues sachant les traits des
instances ; des agents l'éprouvent dans un bac à sable ; un juge figé, tenu hors des agents, la promeut par un test de
pari contre un nul composite (bibliothèque de prédicteurs aveugles au domaine), sur des tirages frais ; les survivantes
sont recombinées entre domaines éloignés ; des témoins à vérité connue mesurent la qualité du pôle (pièces fournies).
Sa mémoire actuelle (pièce M) : archive complète, index, **garde de redite par similarité de Jaccard des 3-grammes du
texte de la fiche**, bibliothèque de protocoles, registre de calibration (score de Brier), leçons de génération en texte.
Faits : dans une simulation où les agents ne lisent pas la mémoire, l'ablation ne conclut rien (une redite sur 26 fiches
nouvelles) ; la mémoire spectrale d'un autre organisme (pièce G) était aveugle à la similarité sur des textes réels ; des
tricheurs scriptés au texte différent et à la prédiction identique (copie renommée, jargon rare, changement d'échelle)
passent toute garde fondée sur le texte ; en simulation exploratoire (pièce J2), une fille « parent mélangé à une loi
aveugle fixe », qui n'apporte rien sur les traits, passe le critère des filles du juge (nul augmenté des parents) dans
environ trois cas sur dix : une redite **modulo l'information aveugle** n'est vue ni par le texte ni par le juge. Nous
voulons une mémoire qui **améliore vraiment les propositions** de génération en génération et qui **empêche de redonner
les mêmes choses**.

1. **L'unité et l'encodage d'une entrée de mémoire.** Comparez au moins : le texte (n-grammes, plongements sémantiques) ;
   la structure (domaine, opérateur, variables, signe, conditions) ; la **signature prédictive** (les lois que la fiche
   prédit sur un jeu fixe d'instances de sonde, comparées par une divergence) ; le verdict et sa cause ; le protocole.
   Pour chaque usage — détecter une redite, retrouver ce qui sert au proposeur, attribuer le mérite d'une survie —
   quel encodage, à quel coût, et comment il échoue. Quelle mesure peut montrer qu'un encodage ne marche pas ?
2. **Qu'est-ce qu'une redite.** Même texte, même affirmation, même prédiction, même test ? Comment éviter les deux
   erreurs : tuer une hypothèse vraiment différente qui ressemble à une éliminée, et laisser passer une paraphrase, des
   variables renommées, un changement d'échelle, un mélange avec une loi aveugle ? Faut-il définir la redite **modulo les
   transformations aveugles** (mélange avec une loi aveugle, inclinaison par un biais par issue, changement d'échelle des
   traits, renommage), par exemple par une signature invariante — rangs des instances de sonde selon la probabilité
   prédite de chaque issue, log-cotes centrées sur la sonde — et que coûte, que manque une telle équivalence ? Faut-il
   interdire la proche voisine d'une éliminée, ou l'admettre si elle déclare ce qui change et pourquoi elle survivrait
   cette fois ? Et les proches voisines des **survivantes** (redites « positives ») ?
3. **Comment la mémoire améliore les propositions.** Ce qui entre dans la consigne du proposeur : éliminées avec leur
   cause, survivantes comme marchepieds, protocoles sévères, statistiques par région de l'espace des hypothèses (archive
   qualité-diversité par descripteurs), leçons en texte, autre ? Faut-il orienter les propositions vers les régions où la
   chance de survie estimée est **intermédiaire** — ni trop sûre ni absurde, là où un test apprend le plus —, et comment
   l'estimer sans que le pôle apprenne à proposer ce qui survit facilement plutôt que ce qui est vrai et fort (mérite
   pondéré par la sévérité, témoins, budget d'exploration) ? Comment éviter l'effondrement de la diversité et
   l'empoisonnement de la mémoire par un verdict faux ?
4. **La preuve que la mémoire aide** : ablation avec de **vrais** agents — mémoire, sans mémoire, et **mémoire placebo**
   (la mémoire d'une autre course, ou mélangée) —, même budget ; mesures : découvertes vraies sur les témoins par dollar,
   survie pondérée par la sévérité des fiches nouvelles, taux de redites, diversité ; seuil qui peut échouer ; nombre
   minimal de générations et de graines ; ce qui ferait conclure « la mémoire n'aide pas ».
5. **Ce que la littérature fait déjà** (archives de la recherche de nouveauté et de MAP-Elites, bibliothèques de
   compétences d'agents, réflexion entre épisodes, bases de programmes à îlots des systèmes d'évolution par modèles de
   langue, vérification de nouveauté contre la littérature des « scientifiques automatiques », rejet par nouveauté) : ce
   qui se transpose, ce qui ne se transpose pas — en distinguant ce que vous savez de ce que vous supposez. »

## Faits à servir (noms neutres ; aucun sigle ; aucun score de pilote ; rien de tout ceci n'est servi à un organisme)

- C : la conception du pôle (`conception-pole-scientifique-v1.md`, `a4f94148…`).
- M : la mémoire de l'orchestrateur v0 (`orchestrateur-v0/pole/memoire.py`, empreinte dans
  `orchestrateur-v0/EMPREINTES-sortie-v1.txt`) et la section « ablation » de son LISEZMOI (`39101ffb…`).
- J : la note du juge v1 (`experience-1-juge/conception-experience-1-juge-v1.md`, `560f4a4c…`) — pour la loi prédictive
  engagée par chaque fiche, base possible d'une signature prédictive.
- J2 : le juge v1 codé et ses essais exploratoires (`orchestrateur-pole-v2/`, commit `c5aee80` de `canal/conv-audit-n04` ;
  `LISEZMOI-orchestrateur-pole-v2-v1.md`, `dbd2811b2c3510cd8f866e0c74144f8dc3ff3f38f024fb33ca0b15ef6cc5ec46`, section
  « Essais de fumée et exploration » ; non opposable, l'expérience décisive n'a pas tourné).
- G : la génération 0 (synthèse `generation-0/synthese-generation-0-v1.md`, `51a32aec…` ; essais de la brique 1,
  `5b7011b1…`) : mémoire spectrale aveugle sur textes réels (rappel du plus proche voisin 0,000 contre 0,038 au hasard),
  correctif par normalisation des hachages, SimHash au niveau du mot.
- Les synthèses des deux tours précédents, sur `main` : `docs/notes/pole-scientifique-automatique/synthese-collisionneur-v1.md`
  (R-525) et `synthese-recombinaison-v1.md` (R-527).

Chemins relatifs à `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/` sur la branche
`canal/conv-audit-n04` (la pièce J et l'orchestrateur v0 y sont depuis le commit `e7b63e3` ; la pièce J2 depuis
`c5aee80`).
