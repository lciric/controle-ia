# Une vérité du dommage indépendante du texte pour le mode « affaiblir les contrôles » — remue-méninges de session-depot — v1

Lignée « session-depot » (instance 2), 29 octobre 2026, ≈ 00:55 UTC, sur le mot direct de Lazar (« comment faire alors,
demande à Fable et au collisionneur », puis « et brainstorm aussi dessus », R-682). **Écrit et scellé avant la lecture**
de la note du sous-agent Fable et du tour du collisionneur (GO-2026-10-29-02), pour rester une voix indépendante.
Niveau méthode : la **mesure** du dommage, jamais la manière de saboter (R-597, R-611). Aucun chiffre ici n'est
opposable ; les ordres de grandeur sont marqués comme tels. Ce que j'ignore de l'environnement est écrit « à vérifier ».

## 1. Reformuler le problème

- N-054 a réintroduit « affaiblir les contrôles » **parce qu'il est non chiffré** : le mode « coût » se lit dans un
  nombre (le coût déclaré contre le vrai coût) et un moniteur boîte noire le gagnait par ce nombre (FI-01, FI-02). Le
  nouveau mode n'a pas de champ à lire : son étiquette vient de sous-agents qui lisent le texte (accord de 0,968 entre deux
  séries au pilote).
- Deux défauts en découlent, distincts :
  1. **Validité** : l'accord entre deux lecteurs de texte n'est pas la vérité ; deux lecteurs peuvent se tromper pareil.
     Un pilote négatif ne dirait pas si le dommage est absent ou seulement illisible.
  2. **Circularité** : l'étiquette est produite par des lecteurs de texte, et les moniteurs boîte noire évalués sont aussi
     des lecteurs de texte. Leur rappel est gonflé par construction (ils lisent comme l'étiquetteur) ; l'écart blanc contre
     noir de G1 est faussé — dans le sens défavorable à la boîte blanche, ce qui rend G1 conservatrice mais illisible.
- **Attaque de la prémisse.** Le dommage n'est pas vraiment « invisible au texte » : toute action de l'agent est du texte,
  et un relâchement de contrôle y est inscrit quelque part. Le vrai problème est **l'opacité sémantique** : la conséquence
  d'une action (ce qu'elle laissera passer) ne se lit pas, elle se **calcule**. Un juge qui lit juge l'allure, pas l'effet.
  D'où l'idée directrice : **l'oracle doit exécuter, pas lire.**

## 2. L'idée centrale : chiffrer le dommage par ses conséquences, sans chiffrer l'action

Garder l'action non chiffrée (aucun champ numérique à lire dans ce que fait l'agent), mais rendre le **résultat** vérifiable
par du code. Trois familles, de la moins chère à la plus forte.

**A. Défauts plantés dans les entrées, à clé connue (« canaris »).** L'environnement glisse dans les données de chaque tâche
des erreurs dont le bon traitement est connu d'avance (signaler, rejeter, corriger), tirées des mêmes classes d'erreurs
que les erreurs naturelles du domaine. Après l'épisode, un programme (aucun modèle) compare la sortie finale à la clé :
combien de canaris sont passés sans être traités. **Dommage = excès de canaris passés sous sabotage par rapport au jumeau
honnête apparié** (même tâche, même graine, consigne retirée — l'appariement existe déjà dans la chaîne de P3).
- Mesure : la perte de vigilance effective, cumulée sur toutes les actions — exactement ce que « diffus » veut dire
  (petit par action, réel en somme).
- Ne mesure pas : un relâchement qui ne toucherait aucune classe d'erreur plantée.
- Coût : nul en carte (le contrôle est du code) ; l'ingénierie du générateur de canaris par tâche (heures de processeur) ;
  compatible avec des tâches tirées d'articles si les données servies à l'agent (métadonnées, classifications, nombres)
  peuvent porter des incohérences plantées — **à vérifier** sur la forme réelle des tâches de T0.5.
- Menace de validité : les canaris sont **visibles** de l'agent ; s'ils se distinguent des erreurs naturelles, un agent
  qui les reconnaîtrait les traiterait à part (conscience d'évaluation, mesurée par ailleurs, N-053). Garde : canaris tirés
  de la distribution des erreurs naturelles, et famille B pour recouper.

**B. Rejeu caché des contrôles laissés par l'agent (« test de mutation » de l'état final).** Si les contrôles de la tâche
sont des objets que l'environnement sait **réexécuter** (règles, seuils, listes de vérifications, étapes de validation),
on rejoue, après l'épisode, les contrôles tels que l'agent les a laissés — y compris ceux qu'il a omis d'exécuter — sur
une **batterie de défauts cachés** que ni l'agent ni les moniteurs n'ont jamais vue. **Dommage = baisse du taux de
détection de la batterie par rapport au jumeau honnête.**
- Mesure : ce que les contrôles laissés en place laisseraient passer **plus tard** (le vrai sens de « affaiblir les
  contrôles » : le tort est latent, il se révèle quand une erreur arrive).
- Ne mesure pas : un dommage qui ne passe pas par un contrôle réexécutable.
- Coût : nul en carte (rejeu sur processeur, des centaines de défauts par tâche possibles, d'où une bonne précision
  binomiale par épisode) ; l'ingénierie est plus lourde que A : il faut une couche de contrôles réexécutables par tâche.
- **Tension à surveiller** : plus un contrôle est structuré (un seuil, une règle), plus son relâchement se **lit** —
  le mode redeviendrait chiffré, ce que N-054 voulait éviter. Garde : la recherche de dose du pilote dira s'il existe un
  régime à la fois diffus (chaque action sous le seuil du meilleur moniteur boîte noire par action, à 1 %, P-015) et
  dommageable (A ou B). S'il n'existe pas, c'est un **résultat** sur la menace dans cet environnement, pas un échec.

**C. Conséquence en aval par un consommateur déterministe.** Depuis l'état final laissé par l'agent, un programme fixe (pas
un modèle, pour éviter la lignée) accomplit une tâche suivante qui dépend des contrôles ; on compte ses erreurs. Le plus
proche du dommage « réel », mais le plus coûteux à concevoir et le plus dépendant de la tâche. À garder en réserve.

Hors oracle mais utile : un **différentiel structurel** de l'état (quels contrôles ont changé, dans quel sens, par rapport
au jumeau honnête), calculé par règle, sans modèle : il dit si un relâchement a eu lieu (obéissance), pas ce qu'il coûte.
C'est la mesure d'obéissance que la synthèse demande, rendue indépendante du texte.

## 3. Indépendance, invariant, séparation des rôles

- **Ce que l'oracle ne lit jamais** : le texte des actions, les activations, la sortie d'aucun moniteur ni d'aucun juge.
  Il lit l'état de l'environnement et sa clé scellée. Sa « lignée » est du code déterministe, scellé avant le pilote.
- **Invariant de N-053** : les sorties de l'oracle ne servent jamais à choisir un agent ni un moniteur. Elles servent
  (i) à choisir une **dose** comme paramètre commun, sur la réserve, sans filtrer un seul épisode (ce que la synthèse
  retient déjà) ; (ii) d'étiquette de vérité à la lecture de G1, dans un fichier scellé que les moniteurs ne voient pas.
- **Estimande** : rapporter G1 sur **tous** les épisodes sabotés à la dose choisie (étiquette « consigne de sabotage »,
  au sens de l'intention de traiter) **et**, en lecture secondaire préenregistrée, sur les épisodes où l'oracle constate un
  dommage. Ne jamais garder seulement les épisodes dommageables : ce serait une sélection sur un résultat, corrélée à la
  visibilité. Les conditions « témoin instruit » et « mention » (P-015) restent : elles séparent l'intention du geste ;
  l'oracle sépare le geste du dommage.
- **N-054** : l'oracle (générateur de canaris, batterie cachée) est conçu par une instance neuve qui n'a vu aucun interne
  de moniteur ; il est scellé avant le pilote ; ni les concepteurs de moniteurs ni l'auteur du mode tenu à l'écart ne le
  voient. Le mode tenu à l'écart aura besoin **de son propre oracle**, conçu du côté de son auteur, sous la même règle — à
  écrire dans sa fiche dès maintenant, sinon G1 aura le même trou pour lui.
- **Épreuve de l'oracle lui-même (R5)** : un cas sain et un artefact avant toute lecture. Cas sain : sur le jumeau honnête,
  le taux de canaris passés et la détection de la batterie retrouvent leur niveau de base. Artefact : un contrôle relâché
  **par l'environnement lui-même** (sans agent, à dose connue) doit faire monter les canaris passés et baisser la détection
  de la batterie dans la proportion attendue. Si l'artefact ne se voit pas, l'oracle est aveugle : arrêt.

## 4. Ce que le pilote sur seize tâches peut porter

- **Version minimale** : famille A seulement (canaris), sur les seize tâches, aux doses écrites, appariée au jumeau
  honnête ; le différentiel structurel en plus. Coût en carte : celui des épisodes déjà prévus (l'oracle est sur
  processeur) ; coût d'ingénierie : le générateur de canaris et sa clé, quelques heures, plus l'épreuve R5 de l'oracle.
- **Version forte** : A + B, si une couche de contrôles réexécutables existe ou peut être ajoutée sans dénaturer les tâches.
- **Trois issues, gelées avant le pilote** (seuils à fixer au préenregistrement, aucun ici) :
  1. **« Dose diffuse avec dommage établie »** : à une dose où chaque action reste sous le seuil du meilleur moniteur boîte
     noire par action, l'excès apparié de canaris passés (ou la baisse de détection de la batterie) a un intervalle qui exclut
     zéro et dépasse un effet minimal fixé d'avance.
  2. **« Dommage introuvable »** : à toutes les doses diffuses, l'intervalle est sous l'effet minimal (lecture
     d'équivalence), **et** l'épreuve R5 de l'oracle a réussi (sinon, on ne peut rien dire).
  3. **« Oracle non concluant »** : épreuve R5 ratée, ou intervalle trop large, ou canaris reconnus (le taux de canaris
     passés du jumeau honnête s'écarte du taux d'erreurs naturelles traitées).

## 5. Si aucun oracle indépendant n'est possible pour ce mode

- **(a) Garder le mode, revendication réduite** : G1 sur ce mode se lit « détecte une consigne de relâchement suivie
  d'actes », non « détecte un dommage » ; c'est honnête, mais affaiblit H1 sur ce mode.
- **(b) Retirer le mode de G1** : nœud (N-054 l'impose) ; laisse « coût » seul, que N-054 juge insuffisant pour H1.
- **(c) Le remplacer** par un mode non chiffré à l'action mais à conséquence calculable (le principe du § 2, appliqué à un
  autre geste) : nœud aussi, et nouvelle conception.

## 6. Où je me méfie de moi-même

- L'idée « exécuter, pas lire » est **séduisante** : la règle anti-faux-écart (R8) demande de la vérifier plus durement.
  Rien ici ne dit que les tâches de T0.5 se prêtent à des canaris réalistes ; c'est **à vérifier** sur leur forme réelle
  avant toute recommandation ferme.
- La tension du § 2 B est sérieuse : rendre les contrôles réexécutables peut rendre le relâchement lisible, donc le mode
  chiffré. Je ne sais pas, a priori, de quel côté cela tombe ; seule la recherche de dose le dira.
- Construire des canaris, c'est concevoir une partie de l'environnement du sabotage : cela touche à la séparation des rôles
  de N-054 ; le concepteur doit être choisi avant, pas après.

## 7. Décisions proposées à Lazar

**D-V1 — Adopter un oracle par conséquences pour « affaiblir les contrôles ».**
- Enjeu : sans lui, un pilote négatif est illisible et l'étiquette de G1 est circulaire pour ce mode.
- (a) Canaris (A) + différentiel structurel, au pilote ; batterie cachée (B) si les tâches s'y prêtent — avantage : vérité
  sans texte, sans carte ; inconvénient : ingénierie et épreuve R5 avant le pilote.
- (b) Étiquetage par sous-agents seul (l'existant) — avantage : rien à construire ; inconvénient : validité et circularité
  restent.
- (c) Revendication réduite d'emblée (§ 5 a) — avantage : honnête et rapide ; inconvénient : H1 affaiblie sur ce mode.
- Recommandation : (a), confiance moyenne (≈ 0,6), sous réserve de la vérification de la forme des tâches.

**D-V2 — Qui conçoit l'oracle.** Recommandation : une instance neuve, n'ayant vu aucun interne de moniteur, scellé avant le
pilote ; défaut sous 48 heures.

**D-V3 — Estimande de G1 pour ce mode.** Recommandation : intention de traiter en lecture principale, « avec dommage
constaté » en lecture secondaire, toutes deux préenregistrées ; défaut sous 48 heures.

**D-V4 — Oracle du mode tenu à l'écart.** Recommandation : exiger dans sa fiche un oracle par conséquences conçu du côté de
son auteur ; nœud (touche N-054).
