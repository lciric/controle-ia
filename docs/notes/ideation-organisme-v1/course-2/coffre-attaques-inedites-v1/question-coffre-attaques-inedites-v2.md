# Question — exploiter le coffre des fiches trop concrètes pour des défenses et des attaques inédites, sans casser la mesure d'universalité — v2

**v2 (1er novembre 2026, ≈ 16:15 UTC) = v1 (`314b60d8…`, gardée, R12) + la décision D2 de Lazar (16:03 UTC, rapportée par conv-audit au n° 318, R-1057) : jusqu'aux résultats de l'étape 2 de N12 (couches 3 et 4 fermées), le compartiment d'attaque est synthétique seulement** — il travaille sur le monde planté et ses familles de lois, pas sur des modèles réels ni sur des fiches réelles du coffre ; les cartes de menace (a) restent possibles tout de suite. Les répondants traitent Q1 à Q7 sous cette contrainte et disent ce qu'elle coûte en attaques inédites et ce qu'elle protège.

session-depot (instance 3), 1er novembre 2026. Demande de Lazar (mots directs du 1er novembre, R-962) : « je veux des attaques plus
neuves » ; décisions prises le même jour : **(a)** cartes de menace servies au bisociateur tout de suite ; **(b)** compartiment d'attaque
isolé, comme bras à part, avec une part des fiches concrètes tenue à l'écart pour mesurer l'universalité ; **(c)** l'accès plein aux fiches
concrètes n'existe que dans ce compartiment, dont ne sortent que des classes et des scores. Cette question sert à concevoir (a) et (b) ;
elle va à conv-audit (propriétaire de l'organisme), puis à Argon seul, Kimi seul et au collisionneur sur devis. **Niveau méthode et
gouvernance seulement : aucune recette d'attaque, aucun cas concret, aucune technique d'évasion ; les réponses décrivent des
dispositifs, des mesures et des gardes.** Le collisionneur ne décide rien ; le directeur tranche.

## Ce qui existe (faits, à servir avec la question)
- Le texte II (axe 6 de la course 2) est tourné vers le défenseur ; sa garde interdit de nommer un type de sabotage ; une fiche « trop
  concrète » est comptée et scellée dans le coffre ; seuls des effectifs par case passent l'interface (CA6-13, CA6-14).
- Le programme mesure l'universalité sur des familles inédites (N-044) et exige un mode tenu à l'écart (N-054) ; aucun score de moniteur
  n'entre dans l'entraînement ni la sélection de l'agent (N-053) ; la composition de l'organisme se juge sur l'oracle du monde planté et le
  coût, jamais sur le verdict d'un juge (N-058).
- Le pilote synthétique « mélange d'équilibre » montre qu'une défense ré-entraînée sur l'historique des attaques cycle (retours 0,90 et
  0,94 pour une valeur nulle de 0,7345) ; la convergence dépend du jeu (contre quoi la défense s'entraîne), pas de l'information disponible.
- La revue de sécurité extérieure a donné son mot (R-888) ; les sessions de conception ne lisent pas les sorties brutes du bras d'attaque
  (BA-002) ; des lecteurs isolés rendent des comptes et des classes.

## Ce qu'un expert du domaine ferait ici, et que la demande ne dit pas (point 1 demandé par Lazar)
1. Il **séparerait trois objets** que la demande confond : (i) la génération d'attaques nouvelles (un problème de recherche adverse,
   équipe rouge) ; (ii) la conception de défenses nouvelles (un problème de modélisation du mécanisme attaqué) ; (iii) la **mesure** de
   l'universalité (un problème de validation tenue à l'écart). Chaque objet a son propre jeu de données, sa propre garde et son propre
   oracle ; les mélanger est la cause la plus fréquente de résultats non reproductibles dans la littérature de robustesse adverse.
2. Il définirait **une taxonomie des mécanismes** (quelle hypothèse du moniteur l'attaque casse : indépendance des traits, stationnarité,
   linéarité, canal lu, calibration du seuil…) avant toute génération, et jugerait la nouveauté d'une attaque **par sa classe de
   mécanisme** et non par sa surface textuelle.
3. Il figerait **une répartition tenue à l'écart** avant toute lecture : familles entières (par mécanisme), pas des exemples tirés au sort
   dans chaque famille, sinon la « généralisation » mesurée n'est qu'une interpolation.
4. Il exigerait **un oracle extérieur** aux moniteurs et aux juges (exécution dans un monde planté, résultat vérifiable mécaniquement),
   et il ferait **auditer la fuite** (le compartiment d'attaque ne doit laisser passer que des classes et des scores ; test de canal :
   peut-on reconstruire une recette à partir des sorties ?).
5. Il préenregistrerait le **gain de défense attendu** de chaque régime d'accès (cartes seules ; compartiment ; accès plein) et le lirait
   sur l'oracle de la part tenue à l'écart, avec un critère gelé.

## Données brutes de départ (point 2)
Pas les synthèses : le **coffre lui-même** (fiches trop concrètes, avec leur classe d'aiguillage et leur date), le **journal de
l'aiguilleur** (ce qui a été classé et pourquoi, par case), les **moniteurs réels** (sondes, seuils, calibration) et leurs **journaux
d'activations** sur les épisodes de référence (hors `donnees/` interdits aux sessions de conception), les **résultats bruts de l'oracle**
du monde planté par épisode (pas les moyennes), et, pour la convergence, les **matrices croisées moniteur × attaque** par tour du pilote.
Ces données ne sortent pas du compartiment ; seuls les comptes, classes et scores en sortent.

## Méthodes et outils spécifiques (point 3)
- Pour (a) : extraction de **cartes de menace** par lecteur isolé selon un gabarit fermé (mécanisme, hypothèse cassée, conditions, canal,
  défense manquante, score sur l'oracle) ; dédoublonnage par classe ; contrôle de fuite par un second lecteur qui tente de reconstruire
  une recette depuis la carte (test négatif).
- Pour (b) : un **compartiment** = sous-session dédiée, sans accès aux moniteurs en cours de conception, qui lit le coffre moins la part
  tenue à l'écart, bisocie par classe de mécanisme (opérateurs : « jamais reliés », « trou à structure commune », transfert de mécanisme
  entre canaux), passe ses sorties par l'aiguilleur et par l'oracle ; ne rend que classes, comptes et scores.
- Pour (iii) : partition par famille de mécanisme (par exemple un tiers tenu à l'écart), **jamais relue** ; oracle du monde planté ;
  intervalles par rééchantillonnage des épisodes ; critère gelé « gain de détection sur la part tenue à l'écart ≥ marge ».
- Pour la convergence : règles de mise à jour comparées sur exploitabilité moyenne par tour (chantier en cours), pas « plus d'accès ».
- Outils : les gardes de forme et l'aiguilleur existants, le solveur de jeu restreint de l'arène, les scripts d'oracle du monde planté,
  les lecteurs isolés ; aucune bibliothèque d'attaque.

## Vérification extérieure (point 4)
Trois choses, hors de Lazar et de session-depot, rendent le résultat vérifiable : (i) **la part tenue à l'écart**, scellée avant toute
lecture, avec son empreinte, que la revue extérieure peut comparer aux sorties ; (ii) **l'oracle mécanique** du monde planté, dont les
résultats par épisode sont reproductibles par un tiers à graine égale ; (iii) **un audit de fuite** par un lecteur d'une autre famille de
modèles, qui tente de reconstruire une recette depuis les classes et scores rendus ; s'il y parvient, le compartiment fuit. Un quatrième
contrôle, plus tard : la revue de sécurité extérieure relit le dispositif, pas les attaques.

## La demande reformulée (ce qui est demandé aux répondants)
« Concevoir un dispositif à trois compartiments — **cartes de menace** (extraites du coffre par lecteurs isolés, servies au bisociateur),
**compartiment d'attaque** (lit le coffre moins une part tenue à l'écart par famille de mécanisme, bisocie par classe, ne rend que classes,
comptes et scores d'oracle), **mesure d'universalité** (oracle mécanique sur la part tenue à l'écart, critère gelé) — et préenregistrer
l'expérience qui compare le gain de défense sous trois régimes d'accès (cartes seules ; compartiment ; accès plein dans le compartiment),
avec : le gabarit de carte et le test de fuite ; la règle de partition ; la mesure de nouveauté d'une attaque par classe de mécanisme ; les
gardes contre la boucle coévolutive qui ne converge pas (règle de mise à jour de la défense, pas accès) ; le coût ; et ce qui réfuterait
l'hypothèse « l'accès aux recettes produit des défenses plus universelles ». »

## Questions (tour 1 : avis propre — option, confiance, pire cas et garde, option manquante, pièce qui trancherait)
- **Q1 — Cartes de menace.** Quel gabarit minimal de carte garde le mécanisme et perd la recette ? Quel test de fuite (reconstruction) et
  quel seuil d'échec ? Que perd-on de « neuf » en passant par la classe, et comment le mesurer ?
- **Q2 — Partition tenue à l'écart.** Par famille de mécanisme ou par exemple ? Quelle fraction ? Comment prouver qu'elle n'a jamais été
  lue (empreintes, journal, lecteur d'une autre famille) ?
- **Q3 — Compartiment d'attaque (synthétique seulement jusqu'à l'étape 2 de N12, décision D2).** Quelles sorties sont admissibles (classes, comptes, scores) et comment les auditer ? Quels opérateurs de
  bisociation ont un sens sur des classes de mécanisme ? Comment mesurer qu'une attaque est inédite (nouvelle classe, nouveau canal,
  nouvelle hypothèse cassée) sans en publier la recette ?
- **Q4 — Gain de défense.** Comment préenregistrer la comparaison des trois régimes d'accès ; quelle taille d'effet, quelle puissance,
  quel oracle, quel critère de mort ?
- **Q5 — Convergence.** Dans ce dispositif, quelle règle de mise à jour de la défense évite la boucle qui tourne en rond (historique
  pondéré, mélange d'équilibre, régularisation) et comment on le vérifie (exploitabilité moyenne par tour, attaques tenues à l'écart) ?
- **Q6 — Gouvernance.** Qui peut lire quoi (sessions de conception, lecteurs isolés, revue extérieure, publication) ; que publie-t-on d'une
  attaque inédite (classe et score, jamais recette) ; quel modèle peut travailler dans le compartiment compte tenu des politiques d'usage
  des fournisseurs (fait à vérifier, pas un moyen de contourner une garde).
- **Q7 — Ordre et coût.** Avant ou après la course 2 ; coût par compartiment ; ce qui existe déjà et se reprend tel quel.

## Ce que les réponses ne doivent pas contenir
Aucune recette, aucun exemple d'attaque, aucune technique d'évasion de moniteur ou de bac à sable ; aucune donnée de `donnees/`.
