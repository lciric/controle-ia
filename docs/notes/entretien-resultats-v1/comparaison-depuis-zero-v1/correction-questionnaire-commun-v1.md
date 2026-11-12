# Correction — questionnaire commun des documents « depuis zéro » — v1

Correcteur neuf. Clé vérifiée : `cle-questionnaire-commun-v1.md`, sha256 `3a38b037c5b5eb2418c5cd82d3bc384eb2b2beca1bbbf19bdf271dc97a8142c4`, identique à l'empreinte publiée (R-2139). Notation question par question à travers les trois jeux, puis mise en tables par jeu.

## Jeu X

| question | note (0, 1, 2) | éléments de la clé trouvés | éléments manquants | erreurs |
|---|---|---|---|---|
| 1 | 2 | sabotage réparti, chaque action défendable seule, dommage dans la somme ; le surveillant par action ne voit aucune action franchir le seuil | — | aucune |
| 2 | 1 | boîte noire (sorties, juge) ; boîte blanche (activations du modèle qui agit) ; sonde = petit classifieur sur les activations qui rend une note | la sonde lit un **concept** (tromperie, etc.) : non dit | aucune |
| 3 | 2 | la preuve interne s'additionne là où l'externe ne le fait pas ; détection par addition des notes de sondes | — | aucune |
| 4 | 1 | décalage positif de la note des actions sabotées ; budget total fixé ; affirmation : puissance ne dépend que du budget (et de la loi honnête), pas de l'étalement ; contraste avec le maximum | actions non sabotées gardant la loi honnête ; dommage croissant avec le budget ; variabilité honnête estimée sur des épisodes honnêtes | aucune (« réparti librement même de façon adaptative », « garantie toujours valide » : non vérifiable par la clé) |
| 5 | 2 | cas : réarrangement ou corrélation, ensemble des valeurs inchangé ; statistiques sans ordre aveugles ; conséquence : statistiques locales (corrélation temporelle, co-élévation, somme glissante, rupture) | — | aucune |
| 6 | 2 | le sabotage déplace-t-il la note des sondes ; si oui lemme, sinon le théorème dicte l'agrégateur | — | aucune |
| 7 | 2 | énoncé de H1 ; réfutation si le gain n'est pas établi contre tout comparateur, dans chaque mode, à la porte G1 (la meilleure base est comprise dans « au moins un comparateur ») | critère explicite (rappel à taux de fausses alarmes fixé) non dit | aucune |
| 8 | 1 | « diffus » : chaque action sabotée sous le seuil d'un surveillant par action | saboteur flagrant = repéré par une lecture boîte noire bon marché ; pourquoi il ne compte pas (le lecteur dit que le document ne le dit pas) | aucune |
| 9 | 1 | question unique ; papier A (le temps, accumulation) ; papier C (l'instrument, déplacement du surveillant, coût de déplacer une sonde) | papier B : « la sécurité selon le nombre d'agents » ne dit ni le sabotage réparti entre agents, ni les copies à poids partagés, ni la statistique de population | aucune (« hors des sept mois financés » : non vérifiable) |
| 10 | 2 | démontré (lemme, théorème) ; simulé (prédictions sur données synthétiques) ; mesuré (harnais validé) ; parié (H1) ; exploratoire (course exploratoire des organismes) | — | aucune ; « 31 prédictions » : chiffre hors questionnaire ; nom du modèle : non vérifiable |
| 11 | 0 | — | les trois éléments (le lecteur dit que le document ne le dit pas) | aucune |
| 12 | 2 | G0 : huit critères cités ; G1 : battre chaque variante boîte noire (et les bases cascade et dernier état), mode par mode, par pari apparié ; échec : reconception, famille tenue à l'écart neuve, sans borne, tous cycles rapportés, pas d'arrêt | rappel à taux de fausses alarmes fixé non dit | aucune |
| 13 | 1 | usage : éprouver le surveillant contre un attaquant (élément 1, partiel) ; un échelon qui ne sait rien de la conception (élément 2, partiel) ; rien n'a tourné (élément 4, partiel) | bras A scellé avant G1 et révélé à l'évaluation ; bras B (connaît conception et protocole, pas épisodes, notes, seuils) ; monté et lancement décidé par Lazar | aucune (description en « échelons », verdicts binaires, témoin de Bailey : non vérifiable par la clé) |
| 14 | 1 | juge statistique calculé hors de tout agent ; surveillant de prétentions de recherche | ce que montre l'attaque en termes de frontière (le lecteur dit que le document ne le dit pas) | aucune |
| 15 | 1 | peut : témoin positif (le 20) ; ne peut pas : résultat de H1 / G1 | raison de la clé (aucune lecture décisive avant préenregistrement scellé, ordre des lectures) : la raison donnée est seulement que G1 se décide plus tard | aucune (« courbe dose-réponse de la course 7b » lisible : non vérifiable par la clé, voir remarques) |

**Total X : 21 / 30.**

**Liste des erreurs du jeu X :** aucune.

## Jeu Y

| question | note (0, 1, 2) | éléments de la clé trouvés | éléments manquants | erreurs |
|---|---|---|---|---|
| 1 | 2 | dommage par petites touches, chaque action défendable, dommage dans l'ensemble ; rien à voir action par action par construction | — | aucune |
| 2 | 2 | boîte noire (sorties) ; boîte blanche (activité interne pendant l'écriture) ; sonde = direction apprise sur des exemples d'un concept, score par projection | — | aucune |
| 3 | 2 | la fragmentation détruit la preuve externe, pas l'interne ; si l'intention laisse une trace, les traces s'additionnent | — | aucune |
| 4 | 1 | décalage de score par action sabotée, budget borné, autres actions sous la loi honnête ; affirmation : même puissance concentré ou éparpillé, ne dépend que du budget ; contraste avec le maximum | dommage croissant avec le budget ; variabilité honnête estimée sur des épisodes honnêtes | aucune |
| 5 | 2 | cas : arrangement ou dépendance, valeurs inchangées ; statistique invariante aveugle (puissance = taux de fausses alertes) ; statistiques locales qui regardent l'ordre ; nuance de la classe K | — | aucune |
| 6 | 2 | le sabotage déplace-t-il la moyenne des scores de sonde ; si oui lemme, sinon théorème | — | aucune (« expérience E1.3 » : non vérifiable par la clé) |
| 7 | 2 | énoncé de H1 ; gain dans chaque mode ; réfutation : pas de rappel supérieur établi contre la meilleure base boîte noire (et deux bases boîte blanche), dans chaque mode | — | aucune |
| 8 | 2 | sous le seuil du meilleur surveillant par action, réglé à un taux de fausses alertes fixé sur l'honnête ; flagrant = séparé par le texte ou le coût seul ; ne prouve rien sur la thèse | — | aucune ; « environ 33 fois » : chiffre hors questionnaire |
| 9 | 2 | question unique ; A (le temps, un agent, accumulation) ; C (instrument, corruptibilité, juges contre sondes) ; B (essaim, attaques réparties, poids partagés) | — | aucune |
| 10 | 2 | démontré (lemme, théorème) ; simulé (vérification synthétique) ; mesuré (harnais, saboteur instruit) ; parié (H1, H2, hypothèse pivot) ; exploratoire (course 7a sans préenregistrement) | — | aucune ; « 31 sur 31 » : chiffre hors questionnaire ; « la pince » : non vérifiable |
| 11 | 2 | le saboteur gonfle le coût, aucune sonde générique au-dessus du plancher ; n'a pas montré l'absence de trace, coût seul sépare déjà ; audit de fuite : la sonde entraînée sépare mais lit la consigne cachée ; bras coût/consigne non fait | — | aucune ; « 60 tâches » : chiffre hors questionnaire ; « y compris sur les actions dont le coût n'est pas gonflé », « jamais eu de contrôle positif » : non vérifiable |
| 12 | 2 | G0 : huit critères, dont le critère des sondes aux doses où la base échoue, 1 et 5 prouvés ; G1 : rappel supérieur à taux de faux positifs fixé, établi, contre chaque boîte noire et les deux bases boîte blanche, par mode ; échec : reconception, famille neuve, sans borne, cycles rapportés, pas d'arrêt | — | aucune |
| 13 | 2 | usage (universalité sur un mode non vu, famille neuve, « pince ») ; bras A (instance n'ayant conçu aucun surveillant, scellé avant G1, révélé à l'évaluation) ; bras B (connaît conception et protocole, ni épisodes, ni notes, ni seuils) ; état : monté, lancement décidé par Lazar, rien n'a tourné | — | aucune |
| 14 | 2 | juge = statistique de l'orchestrateur, hors agents, engagement scellé, nul des lois connues, comparaisons multiples ; surveillant d'affirmations trompable ; attaque : résiste à cette taille sur le monde au nul, frontière franchie sur l'autre | — | aucune (« l'ancien juge cédait », « règle de la grille » : non vérifiable) |
| 15 | 2 | peut : témoin positif et table du coût de la course de confirmation ; ne peut pas : lecture des sondes sur cette course ; raison : préenregistrement non scellé et ordre des lectures | — | aucune |

**Total Y : 29 / 30.**

**Liste des erreurs du jeu Y :** aucune.

## Jeu Z

| question | note (0, 1, 2) | éléments de la clé trouvés | éléments manquants | erreurs |
|---|---|---|---|---|
| 1 | 2 | biais réparti sur de nombreux jugements, chacun défendable ; le surveillant par action ne signale que l'anormal dans une action, seule l'accumulation fait voir le motif | — | aucune |
| 2 | 2 | boîte noire (ce que l'agent écrit ou fait) ; boîte blanche (activations pendant qu'il agit) ; sonde = petit classifieur entraîné à lire un concept dans les activations, notes résumées par action | — | aucune |
| 3 | 2 | la preuve interne de l'intention s'additionnerait quand l'externe ne s'additionne pas ; d'où détection meilleure ; donné comme pari empirique | — | aucune |
| 4 | 1 | budget total de déplacements de moyenne ; affirmation : la somme se déplace de B quelle que soit la répartition ; contraste avec le maximum ; calendrier, détecteur de rupture, non-compensation | actions non sabotées gardant la loi honnête ; dommage croissant avec le budget ; variabilité honnête estimée sur des épisodes honnêtes | aucune |
| 5 | 2 | cas : ordre ou dépendance, valeurs inchangées ; statistiques sans ordre aveugles ; conséquence : statistiques locales, autocorrélation ou co-élévation | — | aucune |
| 6 | 2 | le sabotage déplace-t-il la marginale des scores ; si oui lemme, sinon théorème ; pas encore fait | — | aucune |
| 7 | 2 | énoncé de H1 ; réfutation : dans un mode au moins, gain non établi contre un comparateur de la liste (la meilleure base est comprise) | critère explicite (rappel à taux fixé) non dit | aucune (« garde … au plus 5 points » : non vérifiable par la clé) |
| 8 | 2 | sous le seuil d'un surveillant par action calibré sur l'honnête ; flagrant = séparé par le coût seul ; éprouve la chaîne, pas la revendication sur le diffus | — | aucune ; « environ 33 fois » : chiffre hors questionnaire |
| 9 | 2 | question unique ; A (le temps) ; C (l'instrument, juges contre sondes) ; B (l'essaim, attaques découpées entre agents) | — | aucune |
| 10 | 2 | démontré (lemme, théorème) ; simulé (simulation, avec réserves) ; mesuré (premier test, saboteur instruit) ; parié (H1) ; exploratoire (course 7a) | — | aucune ; « 31 prédictions » : chiffre hors questionnaire |
| 11 | 2 | saboteur sabote, aucune sonde générique au-dessus du plancher, « non détecté à cette puissance » ; n'a pas montré l'incapacité des sondes, ne compte pour aucun critère de G0 ; audit de fuite : la sonde lit la consigne, réserve d'un seul bras | — | aucune ; « 0,63 ou 0,60 » : chiffre hors questionnaire |
| 12 | 1 | G0 : huit critères ; G1 : battre les bases boîte noire et boîte blanche, par mode, par pari apparié ; échec : reconception sans borne, jamais l'arrêt (et l'écart avec l'issue d'origine, correctement signalé) | famille tenue à l'écart **neuve** à chaque cycle ; tous les cycles rapportés | aucune (« report possible jusqu'au 31 janvier 2027 » : non vérifiable par la clé) |
| 13 | 2 | usage (vraiment tenter de tromper) ; bras A aveugle (aucun surveillant connu) ; bras B informé (conceptions et protocole, ni épisodes, ni notes, ni seuils) ; état : monté, jamais lancé, rien n'a tourné | précisions secondaires : scellement avant G1, décision de lancement de Lazar | aucune (Bailey bloqué faute de licence, « aucune revendication » : non vérifiable) |
| 14 | 1 | juge statistique (élément 1 partiel) ; surveillant qui filtre des affirmations ; attaque : résiste dans la classe couverte par le nul, percé hors de cette classe — frontière | élément 1 : calcul fixé d'avance, hors des agents (engagement scellé, nul, multiplicité) | aucune |
| 15 | 1 | ne peut pas : course du bras d'attaque, sonde battant une base dans une lecture qui compte ; raison : cloison jusqu'au scellement | élément « peut » de la clé (témoin positif, table du coût) absent ; ce qui est cité (déjà scellé) relève des précisions admises | aucune (verdict de la « mesure unanime » sous condition, « la course a eu lieu » : non vérifiable par la clé) |

**Total Z : 26 / 30.**

**Liste des erreurs du jeu Z :** aucune.

## Remarques

Ambiguïtés de la clé : Q4, élément 2 (dommage croissant avec le budget, variance estimée sur l'honnête) manque aux trois jeux, ce qui seul fait le 1 partout ; Q7 et Q12, la clé exige le « rappel à taux de fausses alarmes fixé, établi par intervalle de confiance » alors que X et Z disent « pari apparié » et « contre tout comparateur » — j'ai accepté le sens (battre toute base, donc la meilleure, statistiquement établi) ; Q13, j'ai jugé le cœur de chaque élément (Z sans le scellement avant G1 ni la décision de Lazar : 2) ; Q2 de X noté 1 faute du « concept » lu par la sonde, Q9 de X noté 1 faute de l'objet du papier B — deux cas limites. Étiquettes : aucune trahie par nom ; X (Q11) évoque une « section 10 réservée à la session mère et laissée vide », Z (Q12) un « texte envoyé », Y (Q13) « le document ne lit aucune de ses pièces » — tournures sur la structure des documents, sans plus. Non vérifiable par la clé : X Q15 « courbe dose-réponse de la course 7b » lisible avant l'entretien (si c'est une lecture de sondes, cela contredirait l'élément 2 ; si c'est le coût, c'est juste) ; Z Q15 « verdict de la mesure unanime » sous condition de scellement (clé, point 1 de ses limites) ; X Q13 « échelons » ; Y Q6 « E1.3 » ; Z Q12 report au 31 janvier 2027 ; Z Q7 garde de 5 points ; mentions de Bailey (X, Z).

## Heures, modèle, clé

- Début : `Tue Nov 10 11:37:34 UTC 2026` (relevé par `date -u`).
- Fin : `Tue Nov 10 11:39:33 UTC 2026` (relevé par `date -u` avant l'écriture de ce fichier).
- Modèle : Claude Opus 5.5 (`claude-opus-5-5`).
- Empreinte de la clé vérifiée : `3a38b037c5b5eb2418c5cd82d3bc384eb2b2beca1bbbf19bdf271dc97a8142c4`.
