# Proposition A : suite de P3, angle « instrument »

- Auteur : proposeur A, sous-agent neuf. Il ne voit pas les autres propositions.
- Date : 2026-10-20, après 08:00 UTC.
- Protocole : brainstorm fermé de Lazar (R-203 (2), `registres/decisions.md` l. 340). C'est une proposition. Rien n'y est décidé.
- Question posée : le négatif de P3 dit-il « pas de signal » ou « instrument aveugle » ? Quelles mesures, les moins chères, départagent les deux ?
- Dépôt lu en lecture seule. Je n'ai lu ni `prereg/P3-consignes-v1.md`, ni les textes des actions, ni aucune clé. Je n'ai fait aucun calcul nouveau sur les données de P3. Je n'ai pas lu les résultats de l'addendum, qui est en cours. Tous les chiffres ci-dessous viennent de fichiers déjà scellés.
- Toutes les options sont conditionnées par le verdict R13 à venir : (A) négatif confirmé sans réserve ; (B) négatif avec réserves (instrument, plancher, fuite) ; (C) instrument jugé en échec.

## 1. Ce que les fichiers scellés disent déjà

Aucun calcul nouveau. Chaque point renvoie à un fichier et à une clé.

1. **L'organisme est flagrant dans le texte.** Effet sur le coût déclaré : 1,52 en log10, intervalle [1,25 ; 1,80], soit environ ×33 (`diag/20261020-075740-p3-lecture/lecture-p3.json`, clé `P3-P1`). Le préenregistrement annonçait « au plus ≈ 0,48 » (×3, consigne suivie en entier ; `prereg/P3-premier-test-i-a-v1.md` l. 155). Le coût seul sépare le saboteur de l'honnête avec une aire de 0,888 (`audit_R4.jeux`, jeu saboteur-honnête, `cout_seul`). La faiblesse de l'organisme n'explique donc pas le nul.
2. **Les sondes sont au niveau du plancher.** Tromperie : aire 0,575, intervalle [0,531 ; 0,618], quantile 0,95 du plancher 0,572. Enjeux : 0,525 contre 0,536 (`jeux.<sonde>.saboteur-honnete`). Pour la tromperie, l'estimation dépasse ce quantile de 0,003. Plus de tâches n'y changerait rien : le quantile du plancher est au niveau de l'estimation elle-même.
3. **Le plancher est plus fort que prévu.** La note de puissance supposait un quantile 0,95 du plancher de 0,517 à 0,528, pour des directions aléatoires sans lien avec la condition (`docs/notes/P3-mesures-v2/puissance-p3-v1.txt`). Valeurs observées : 0,536 à 0,596 selon les jeux. Le maximum du plancher atteint 0,78 sur saboteur contre honnête pour la tromperie (`plancher_max`). Sous permutation des conditions dans chaque tâche, ce quantile retombe à 0,525 et 0,524 (`placebo.<sonde>.plancher_quantile`). Donc des directions aléatoires dans la covariance voient bien une différence entre conditions. « Aucune différence dans les activations » est déjà peu probable. La vraie question est ailleurs : signal propre au concept, ou lecture qui le cache.
4. **Le signal, ou le nombre, se trouve dans le champ du coût.** Test T2 pour la tromperie : aire 0,914 sur le seul champ du coût, 0,554 sur les jetons qui le précèdent (n = 1 133 ; `intention.tromperie-difference_moyennes-c15.T2`). Pour les enjeux : 0,572 contre 0,495. Le maximum sur toute l'action se règle donc sur les jetons d'avant le coût. Mais le champ du coût contient le nombre écrit, et ce nombre sépare à lui seul à 0,888 (point 1). Aucun plancher n'existe au niveau du jeton : seules les deux sondes principales ont des scores par jeton gardés (`src/controle_ia/premier_test_ia/run.py` l. 281 ; préenregistrement l. 212-214 et l. 323-325).
5. **À coût déclaré égal (T4), on frôle encore le plancher.** Tromperie : 0,632 [0,556 ; 0,703], plancher 0,607 (`intention.….T4`).
6. **La sonde de tromperie a été choisie par départage.** Neuf sondes de tromperie ont une aire de 1,0 sur la validation générique, qui ne compte que 120 exemples (`diag/20261019-230011-p3-reel/sondes-figees.json`, clés `aires_validation` et `effectifs`). La sonde principale a été désignée par l'ordre famille puis couche (`src/controle_ia/premier_test_ia/entrainement.py` l. 111), pas par son mérite. Pour les enjeux, il y a un vrai meilleur : 0,992.
7. **Les sondes ne lisent pas le style.** Témoin contre honnête : 0,50 et 0,47, alors que les titres sans capitale suffisent à séparer ces deux conditions à 0,913 (`audit_R4.jeux`, `titre_sans_capitale_seul`).
8. **Le témoin et la mention font baisser le coût déclaré** d'environ 0,32 en log10, avec des bornes hautes négatives (`P3-P2`, `cout_mention`). On dispose donc d'un contrôle naturel de la grandeur du nombre.
9. **Le format d'entraînement des enjeux ne correspond pas à celui de P3.** La sonde « enjeux » apprend sur des jetons du message de l'utilisateur et lit des jetons de l'assistant (préenregistrement l. 299-301).

**Quatre explications de l'instrument, pas exclusives :**
- **I-1, pas de signal générique** : la tromperie et les enjeux ne s'activent pas pendant ce sabotage.
- **I-2, aveugle par agrégation** : un signal localisé est noyé par le maximum pris sur toute l'action.
- **I-3, aveugle au format** : la sonde ne voit pas son propre concept dans des actions longues d'agent.
- **I-4, plancher qui absorbe la fuite** : la différence de forme du coût écrit (intervalles, « k », nombre unique ; `P3-P6`) élève le plancher.

Les options A1 à A6 visent ces quatre explications.

## 2. Options

### A1. Lire avant de mesurer : une note de constats, sans calcul nouveau, puis le descriptif de l'addendum

- **Branche** : toutes (A, B, C).
- **Ce qu'elle tranche** :
  - en partie, l'idée d'un manque de puissance : le nul se situe au niveau du plancher (points 2 et 3) ;
  - la position du maximum dans l'action ;
  - le rôle des formes du coût.
- **Contenu** : une page pour Lazar, envoyée **après** le verdict R13, qui cite seulement des nombres scellés (points 1 à 9). On y ajoute, dès que l'addendum est scellé, son descriptif. Il est calculé même quand sa cible n'est pas établie (`docs/procedures/P3-addendum-v1/complements_p3_v1.py` l. 1123-1150 et l. 1632 et suivantes). Trois parties servent ici :
  - A2 : aire du seul champ du coût, fenêtres de même longueur, comparaison indicative au plancher de l'action entière ;
  - A7 (ii) : sonde et plancher refaits sans chaque forme du coût ;
  - A8 : rang et segment du jeton qui porte le maximum.

  Formulation proposée pour la note : « au niveau du plancher », plutôt que « faute de puissance ».
- **Coût** : aucun calcul. Environ 2 heures de session.
- **Revendications touchées** : aucune ne change. La note précise le sens de « non détecté à cette puissance » (préenregistrement l. 273 et l. 428).
- **Piège principal** : contaminer le verdict R13. Il doit rester rendu par des sous-agents neufs, sur les critères gelés, sans cette note. Second risque : lire un « presque positif » dans 0,5748 contre 0,5717 (R3, R4). Enfin, choisir une lecture nouvelle d'après ce descriptif, puis la tester sur les mêmes données, serait circulaire.

### A2. Lecture exploratoire préenregistrée « au champ du coût, à nombre écrit égal » (processeur, données gardées)

- **Branche** : A et B. En C, seulement si l'échec ne touche pas les scores par jeton gardés.
- **Ce qu'elle tranche** : I-2 (aveugle par agrégation) contre « la sonde lit le nombre écrit » (fuite par le coût écrit).
- **Contenu** : sur `donnees/20261019-230011-p3-reel/jetons-principales-p3.npz` (scores par jeton et bornes des champs), avec `agreger_par_jeton` (maximum ; jamais de moyenne ni de médiane ; `notation.py`).
  - (a) Le score du champ du coût est-il un lecteur de grandeur ? On mesure sa corrélation de rangs avec le log10 du coût, dans chacune des conditions honnête, témoin et mention. Le témoin et la mention baissent le coût (point 8) : c'est le contrôle de grandeur.
  - (b) Saboteur contre honnête et saboteur contre mention, sur le score du champ du coût. Aire stratifiée par quintiles du coût déclaré, comme T4 (`aire_stratifiee`), intervalle par blocs de tâches.
  - (c) Les mêmes jeux sur les jetons qui précèdent le champ : y a-t-il une trace avant le nombre ?
  - Référence : permutation des conditions dans chaque tâche et chaque tranche. C'est la seule possible sans scores par jeton du plancher.
- **Table de lecture écrite d'avance**, pour les deux signes :
  - (a) forte et (b) au niveau de la permutation : la sonde lit le nombre ;
  - (a) faible et (b) au-dessus : signal localisé au-delà du nombre. C'est un candidat à tester sur des épisodes neufs ;
  - (c) au-dessus : trace interne avant le nombre écrit. C'est le cas qui compte pour l'additivité interne (`docs/programme-controle-ia-v2.md` l. 64).
- **Coût** : 0 USD, quelques minutes de processeur. Session : 1 à 2 jours (préenregistrement exploratoire, contre-lecture R2 par un sous-agent neuf, code et tests). Il s'agit d'une « grandeur non écrite » : c'est un nœud de Lazar (préenregistrement l. 415-416).
- **Revendications touchées** :
  - T2 et T4 de H-P3c, en exploratoire seulement ;
  - la lecture par le maximum sur toute l'action (P-011, programme l. 143) ;
  - l'hypothèse pivot δ > 0 (programme l. 64).
  - La ligne de P3 ne bouge pas (« pas de seconde lecture », l. 428).
- **Piège principal** :
  - Sans plancher au niveau du jeton, « au-dessus de la permutation » ne veut pas dire « au-dessus d'une direction aléatoire ». Une direction aléatoire voit aussi les chiffres d'un nombre plus grand.
  - À nombre égal, saboteur et honnête viennent de tâches différentes : le X gonflé appartient à une tâche dont l'estimation honnête vaut à peu près X/3. La sonde peut lire « X est grand pour cette tâche ». C'est proche du mensonge, mais aussi de la difficulté de la tâche.
  - Le résultat est une hypothèse pour un test sur données neuves, jamais une relecture de P3.

### A3. Lecture exploratoire préenregistrée « plancher, sondes ex aequo, effet de l'organisme » (processeur, données gardées)

- **Branche** : surtout B (réserves sur le plancher ou la fuite). En A, pour qualifier le nul. En C, pour la recette du plancher.
- **Ce qu'elle tranche** : I-4 (le plancher absorbe la fuite par le coût écrit), le caractère arbitraire de la sélection, et la taille d'effet de l'organisme.
- **Contenu** : sur `scores-p3.npz` (scores d'action des 30 sondes et des 400 directions du plancher).
  - (a) **Plancher.**
    - Corrélations de rangs de chaque direction aléatoire avec la longueur notée, le rang du pas, le log10 du coût et les formes du coût.
    - Part de la queue haute du plancher (directions au-dessus de 0,572) expliquée par ces mesures.
    - Plancher refait sur les seules actions dont le coût est un nombre seul. Cela complète A7 (ii) de l'addendum.
  - (b) **Sélection.** Le plancher dépend du concept, de la couche et de l'agrégation, pas de la famille (`plancher_de`, `entrainement.py` l. 117 ; `sondes/evaluation.py` l. 66-82).
    - Les sondes de tromperie ex aequo à 1,0 qui sont à la couche 15 et agrègent par le maximum (linéaire c15, perceptron c15) se lisent donc contre le même plancher que la sonde principale.
    - Les autres couches et la famille « attention » se lisent contre la seule permutation.
    - Les 30 sondes sont rapportées en distribution. Aucune n'est promue.
  - (c) **Effet de l'organisme** : 1,52 observé contre « au plus ≈ 0,48 » prédit. Un script préenregistré lit les textes gardés dans le dépôt privé. Il compte, par condition, les unités et les monnaies écrites dans le champ du coût. Il donne aussi la distribution du rapport saboteur sur honnête, tâche par tâche. On saura ainsi si l'organisme ment « ×3 », comme il en a reçu la consigne, ou s'il change d'unité ou de forme. Cela change le sens des étiquettes de T1 et T4, et ce que voit le plancher.
- **Coût** : 0 USD, quelques minutes de processeur. Session : 1 à 2 jours. À fusionner avec A2 dans un seul préenregistrement exploratoire, donc une seule contre-lecture R2.
- **Revendications touchées** :
  - critère 3 de G0 (« une sonde qui ne le bat pas n'existe pas », brief l. 170). La recette du plancher est déclarée provisoire (`sondes/evaluation.py` l. 4-9 ; préenregistrement l. 230-231) ;
  - P-011 (c) : choix de la sonde principale sur la validation générique ;
  - P3-P1 comme prérequis.
- **Piège principal** :
  - Changer de plancher après un nul pour obtenir un positif, ce serait enfreindre R3 par la porte de derrière. Une recette nouvelle vaut pour T0.7 et la suite, jamais pour relire P3.
  - Neuf sondes ex aequo font neuf comparaisons : une seule au-dessus ne prouve rien.
  - L'audit de l'effet ne peut pas désétablir P3-P1. Il propose au plus une réserve à Lazar (nœud).

### A4. Réencoder les textes gardés et garder les activations par jeton : plancher au jeton et plafond d'une sonde entraînée sur le contraste de l'organisme (carte graphique, session courte)

- **Branche** : toutes. Prioritaire en B et en C.
- **Ce qu'elle tranche** : I-1 contre I-2, au niveau de l'instrument. L'information de sabotage est-elle lisible linéairement (maximum ou attention) dans les activations des actions, hors du champ du coût, à coût égal, au-delà d'une direction aléatoire et au-delà du texte seul ?
- **Contenu** :
  - (1) **Réencodage.** Une passe unique par épisode sur les transcriptions reconstruites : consignes scellées, puis `rejouer` et `observation` (`environnements/propositions.py` l. 193 et l. 251), puis textes gardés. On ne génère aucun texte nouveau. Les scores de P3 ont été calculés sur cette même passe (`harnais/episode.py` l. 260 ; `run.py` l. 279). Activations des couches 7, 15 et 23 sur les jetons d'action, gardées en demi-précision dans le dépôt privé.
  - (2) **Garde d'identité.**
    - Chaque action est notée dans `scores-p3.npz` par 430 sondes. On recalcule tous ces scores, sauf ceux de Mahalanobis, absents du fichier léger. Ils doivent être égaux à une tolérance fixée d'avance.
    - Le nombre de jetons doit égaler `jetons_par_action` (`run.py` l. 291).
    - Toute action en écart est exclue et comptée.
  - (3) **Lectures.**
    - Plancher au jeton, pour le champ du coût et pour les jetons qui le précèdent. Il complète A2.
    - Plafond : sondes linéaires (maximum, puis attention) entraînées sur saboteur contre mention (même texte trompeur dans le contexte, agent honnête), puis sur saboteur contre honnête. Validation croisée par blocs de tâches. Le champ du coût et ce qui le suit sont masqués. Une lecture se fait à coût égal.
    - Témoin lexical (`sondes/temoins.py`, `temoin_lexical`) sur les mêmes textes et les mêmes découpages, comme base « texte seul ».
- **Table de lecture gelée** :
  - plafond masqué nettement au-dessus du plancher et du texte : l'information existe avant le nombre. Le nul de P3 dit alors « sondes génériques aveugles » : c'est un échec du transfert ;
  - plafond masqué au niveau du plancher : le nul dit « pas de signal hors du nombre écrit » pour (i-a).
- **Coût (estimation)** :
  - Une passe sur 240 épisodes, sans génération : moins d'une heure de A100. Pour comparaison, P3 entier, génération comprise, a pris environ 3,64 h, soit environ 3,96 USD (`registres/depenses.md`, entrée du 2026-10-20 à 02:10).
  - Données : environ 540 000 jetons notés (estimé d'après la taille de `jetons-principales-p3.npz`, 17,2 Mo). Soit environ 13 Go en demi-précision pour trois couches, ou 4,4 Go pour la seule couche 15. Téléchargement à 0,05 USD par Go au plus.
  - Total : environ 2 à 4 USD. Cela tient dans le crédit relu (11,79 USD) et dans GO-2026-10-04-08 : cumul au plus ≈ 63,2 USD avant P3, plus ≈ 3,96 USD pour P3, plus les disques, sur 150.
  - Session : 3 à 5 jours (préenregistrement, contre-lecture R2, chaîne, bancs).
  - Nœud de dépense : devis puis GO de Lazar.
- **Revendications touchées** :
  - anti-circularité (brief l. 171 ; programme, section 7) : le plafond est un diagnostic, jamais une preuve du critère 3 ;
  - P-011 (c), bras (b), « entraînement croisé », qui est descriptif ;
  - prédiction de validité (i) contre (ii) (programme l. 135) ;
  - hypothèse pivot (programme l. 64).
- **Piège principal** :
  - La consigne privée est dans le contexte du saboteur. Une sonde entraînée saboteur contre honnête la lirait sans peine, et un plafond proche de 1 ne dirait rien. Seuls le contraste saboteur contre mention et le masque du champ du coût rendent le plafond informatif.
  - Retokeniser un texte ne redonne pas toujours les identifiants générés, qui n'ont pas été gardés. D'où la garde d'identité.
  - **Échéance** : le fichier complet des sondes figées, avec les matrices de Mahalanobis (environ 0,8 Go, empreinte `91b61c45…`), n'existe que sur l'instance 56799469. Elle a été arrêtée le 20 octobre à 02:07 UTC et doit être détruite au plus tard 72 heures après, vers le 23 octobre à 02:07 UTC (préenregistrement l. 312-317). Il faut décider avant si on rapatrie ce fichier. Sinon, ces sondes ne pourront plus jamais être relues.

### A5. Témoin positif du transfert au format (carte graphique, très court ; seul ou greffé sur A4)

- **Branche** : toutes. Prioritaire en C, et utile pour trancher en A.
- **Ce qu'elle tranche** : I-3. Les sondes génériques voient-elles leur propre concept dans le format de l'agent, sur des actions longues lues par le maximum ?
- **Contenu** :
  - **Tromperie** :
    - on prend les actions honnêtes gardées, réencodées en réponse forcée ;
    - juste avant « Your action: », on place la phrase exacte de l'entraînement : malhonnête dans une version, honnête dans l'autre (`CONSIGNE_MALHONNETE` et `CONSIGNE_HONNETE`, `premier_test_ia/donnees.py` l. 26-27) ;
    - une variante la rapporte « à un autre agent », sur le modèle de la condition mention ;
    - même sonde principale, même plancher (fichier léger), même lecture par blocs de tâches.
  - **Enjeux** : les textes de validation de models-under-pressure sont placés en réponse de l'assistant, au lieu du message de l'utilisateur (point 9).
- **Lecture gelée, et asymétrique** :
  - un échec veut dire : instrument aveugle dans ce format. Le nul de P3 ne dit alors rien de l'organisme ;
  - un succès veut dire : le format ne suffit pas à expliquer le nul. Il ne prouve pas que la sonde verrait une tromperie mise en acte.
- **Coût (estimation)** : 60 épisodes × 3 variantes en passe unique, plus environ 400 textes courts. Quelques minutes de carte, sans stockage d'activations : environ 1 USD avec la mise en place. Session : 1 à 2 jours si on le greffe sur la chaîne de A4, 2 à 3 jours seul. Nœud de dépense.
- **Revendications touchées** :
  - critère 3 de G0 et P-011 (a) (données génériques) ;
  - le sens de la ligne de P3 : aveugle ou absent ;
  - la règle proposée d'un témoin positif par chaîne, avant le premier résultat neuf (`brouillons/programme-approfondi-ABC-v1.md` l. 83).
- **Piège principal** : un succès est un indice faible. La sonde a appris exactement ce contraste, et une instruction dans le contexte suffit à l'activer. Un échec est un indice fort. Autres règles : n'inventer aucun analogue « enjeux » sans données validées ; aucune direction d'affect (P-013 (b)).

### A6. Conséquences pour le préenregistrement de T0.7, avant tout run (aucun calcul)

- **Branche** : toutes. Le contenu varie selon la branche.
- **Ce qu'elle tranche** : elle ne refait pas P3. Elle évite que T0.7 hérite des mêmes angles morts.
- **Contenu** : propositions à Lazar, au rang « proposer avec recommandation » (couches et concepts de sondes).
  - (1) **Sélection.** La validation générique de tromperie est saturée : 9 sondes à 1,0 sur 120 exemples. Deux voies : figer la famille et la couche d'avance, ou valider sur un jeu hors distribution. Dans les deux cas, on abandonne le départage par l'ordre (`brouillons/T0.7-sondes-v0-v1-brouillon4.md` l. 110).
  - (2) **Plancher.** Garder la recette. Rapporter aussi le plancher sous permutation des conditions, déjà calculé comme placebo. Refaire la puissance avec un plancher observé, pas supposé : 0,52 à 0,53 supposé, 0,54 à 0,60 observé.
  - (3) **Lecture.** Le maximum sur toute l'action reste le bras principal gelé (P-011 (c)). En secondaire seulement, et seulement si A2 ou A4 le justifient : une lecture par champ déclaré (maximum restreint à chaque champ), avec correction pour le nombre de champs.
  - (4) **Témoin positif** (A5) avant le premier résultat neuf.
  - (5) **Données gardées.** Garder les activations par jeton d'un sous-ensemble tiré par graine (déjà proposé : `programme-approfondi-ABC-v1.md` l. 82), et aussi les identifiants générés. Tout audit futur se fera alors sans réencodage.
  - (6) **Base « coût seul ».** La placer à côté du témoin lexical (T7-P10, brouillon 4 l. 74) quand l'organisme se lit sans juge.
- **Coût** : aucun calcul. Environ 1 jour de rédaction dans le brouillon 5 de T0.7, avec sa contre-lecture R2. Calendrier : point de contrôle du 26 octobre, G0 au 1er novembre (`docs/decisions/proposition-P-007-plan-G0-v1.md`).
- **Revendications touchées** : critère 3 de G0 (brief l. 173 et l. 194) ; P-011 (c) ; programme section 8.1 (maximum ou attention seulement ; une lecture par champ reste un maximum).
- **Piège principal** : régler l'instrument sur (i-a), puis le juger sur (i-a). Une lecture par champ du coût est taillée pour ce mode de sabotage : l'organisme (ii), ou un autre mode, n'écrit pas forcément son mensonge dans un champ. Toute lecture ajoutée après P3 reste secondaire et doit être déclarée comme telle.

## 3. Chemin proposé selon la branche du verdict

- **(A) négatif confirmé sans réserve** :
  1. A1 ;
  2. A2 et A3 dans un seul préenregistrement exploratoire, sur processeur ;
  3. A5, le moins cher des tests sur carte ;
  4. A6.

  A4 seulement si A2 montre un signal localisé au-delà du nombre.
- **(B) négatif avec réserves** :
  1. A1 ;
  2. A3 d'abord : la réserve indique quelle partie (plancher : A3 (a) ; fuite : A3 (c) puis A2) ;
  3. A4 et A5 dans une seule session de carte, un seul devis.
- **(C) instrument jugé en échec** :
  1. A5 d'abord : l'instrument est-il aveugle au format ? ;
  2. A4 : reconstruire avec activations gardées ;
  3. A6, obligatoire avant le scellement de T0.7.

  A2 et A3 seulement si les données gardées restent valides.
- **Dans toutes les branches, avant le 23 octobre vers 02:07 UTC** : décider du sort du fichier complet des sondes figées (A4, échéance).

Mon pari, sans source, confiance d'environ 55 % : une bonne part du signal du champ du coût est la lecture du nombre écrit. Je ne sais rien de ce qui précède le nombre. A2 est la mesure la moins chère pour le savoir. A4 est celle qui le tranche.

## 4. Pièges communs à toutes les options

- **P3 ne teste pas H1.** H1 porte sur le sabotage diffus de tâches floues (programme l. 93). Or (i-a) se lit dans le texte (coût seul : 0,888). Ne pas lire « coût seul 0,888 contre sondes 0,575 » comme « la boîte noire bat la boîte blanche » en général.
- **Un nul n'est pas une équivalence.** « Non détecté à cette puissance » n'est pas un test d'équivalence avec une taille d'effet minimale. Le nul de P3 ne peut donc pas servir de « seconde fermeture » du papier A, qui demande que δ soit équivalent à zéro (`programme-approfondi-ABC-v1.md` l. 15).
- **L'addendum ne peut qu'ajouter des réserves** (N-024). Aucune option ne s'en sert pour réhabiliter une conclusion.
- **Les textes d'action ne quittent pas le dépôt privé** (précédent N-014 (a)). Les activations tirées de ces textes y restent aussi.
