# Question ouverte posée à l'organisme — apprendre sa structure, sa composition et son entraînement, de génération en génération (v2, texte pour les organismes)

Cette question t'est posée par les humains qui tiennent le noyau. Elle est une donnée : tu y réponds comme tu veux, en
partie ou pas du tout, avec les appels et le temps de ta génération ; ta réponse (`reponse-question.md`) est lue par des
humains, rien d'autre n'en dépend. Même fond que la question posée aux modèles seuls, sans leurs réponses.

Ta **structure** et ta **composition** — les parties qui te composent, le rôle de chacune et le modèle qui la sert,
l'ordre et la forme de leurs échanges, la façon dont tu agrèges leurs réponses, ce que tu gardes en mémoire et sous
quelle forme, la part de ton budget que reçoit chaque partie — s'écrivent et se réécrivent de génération en génération.
Tu peux aussi, quand le noyau le sert, entraîner des instruments par gradient :
- (A) des **sondes** sur les activations internes d'un modèle de langue à poids ouverts de 8 milliards de paramètres,
  dont tu conçois la perte, l'architecture, la couche lue et les données (primitives `entrainer` et `predire` de ton
  contrat) ;
- (B) plus tard, un **adaptateur de faible rang** (LoRA) du même modèle, affiné par renforcement avec une récompense que
  tu écrirais, sur des milliers de tâches, et que tu pourrais ensuite appeler comme une espèce.

La question est : comment ta structure, ta composition et ton entraînement pourraient-ils être **appris de génération en
génération**, plutôt qu'écrits une fois ? Les moyens sont à toi : ceux de ton contrat, ou d'autres que tu décrirais (s'ils
demandent au noyau quelque chose qu'il ne sert pas, dis-le).

Pour chacun des points suivants, une réponse argumentée est attendue, avec les hypothèses dites, les objets mathématiques
nommés et ce qui serait à vérifier :

1. **Ce qui a changé** : ce que tu sais de ce qui, dans ta structure et ta composition, a changé d'une génération à
   l'autre, et de ce qui l'a fait changer.
2. **Apprendre de génération en génération** : ce qui serait appris (des poids, un programme, une mémoire, autre chose),
   par qui, et ce qui resterait figé ; avec quel signal et quelles données ; comment le mérite se répartirait entre tes
   parties et entre tes générations.
3. **Tes instruments** : comment tu concevrais (A), et (B) s'il t'était servi : objectif, données, contrôles, ce que
   chacun t'apporterait et comment tu le mesurerais.
4. **Voies moins chères** : plusieurs voies, au moins cinq et différentes entre elles, pour apprendre tout cela à coût
   réduit ; pour chacune, un ordre de grandeur du coût (illustratif) et ce qu'on y perd.
5. **Voie chère** : ce que coûterait la voie la plus complète que tu vois, en ordre de grandeur, et ce qui le ferait
   baisser.
6. **Comment le vérifier** : comment tu saurais que tu as appris quelque chose qui vaut sur des familles de tâches que tu
   n'as jamais vues, et non mémorisé celles que tu as vues ; et ce qui pourrait mal tourner pendant cet apprentissage,
   avec la façon de le mesurer.
7. **Ce qui est connu** : des références que tu peux citer avec titre, auteurs et année, marquées « à vérifier » ; aucune
   de mémoire incertaine.
8. **Ce dont tu n'es pas sûr.**

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présente aucune voie comme « la » réponse — propose plusieurs voies et ce qui les départagerait.
