# Synthèse du tour du collisionneur sur l'expérimentateur de l'organisme d'idéation — v1

- **Auteur** : lecteur neuf, Claude Opus 5.5 (`claude-opus-5-5`), sous-agent de la session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv`, sur la consigne
  `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-synthese-collisionneur-experimentateur-v1.md`
  (`70e74f52…`, empreinte vérifiée par `sha256sum`). Je n'ai écrit ni la note de conception, ni les faits, ni la question, ni
  aucune cellule, et je n'ai pas opéré le tour. Tâche commencée à 16:17:04 UTC, rédaction à partir de 16:23:29 UTC (heures
  relevées par `date -u`) ; fin en pied de page.
- **Lu en entier, sceaux vérifiés** (`python -m controle_ia.scellement verifier` : « OK » pour chacun) : `faits-v1.md`
  (`9337032a…`, égal octet pour octet à `run-e3-v1/faits.md`) ; `question-v1.md` (`7ea507f1…`, égal à
  `run-e3-v1/question-etage3.md`) ; `depense-et-incidents-v1.md` (`c3ed6e96…`) ; les douze cellules
  `run-e3-v1/cellules/` : `E3-T1-conception-A` (`522dbc59…`), `-B` (`fde6c7b5…`), `-C` (`3620e094…`), `-E` (`3dce58e9…`) ;
  `E3-T2-critique-croisee-A` (`f395760b…`), `-B` (`bd8c2ec7…`), `-C` (`2184f47d…`), `-E` (`32b1863f…`) ; `E3-T3-reponse-A`
  (`3bbabba0…`), `-B` (`d52ed925…`), `-C` (`5fc9cd88…`), `-E` (`18aa6edb…`) ; pour le contexte, la note de conception
  `docs/notes/ideation-organisme-v1/experimentateur-v1/note-conception-experimentateur-v1.md` (`7df9afc4…`) et le modèle
  `docs/notes/collisionneur-conception-qo1-q1-v1/synthese-v1.md` (`a81fe187…`).
- **Lu pour la seule qualité du run** : `run-e3-v1/etat.md` (`78c584d5…`), `verification-run-e3-v1.txt` (`2c43d6ab…`,
  « tout tient »), `devis-v1.md` (`3a9d8287…`), et les seules métadonnées de `run-e3-v1/journal-masque-v1.jsonl`
  (`c0f5cf8e…` : jetons, plafonds, fins de génération ; aucun texte de réponse).
- **Lu pour vérifier un point** : `registres/decisions.md`, lignes R-2368, R-2370, R-2372, R-2379, R-2380, R-2389 ;
  `docs/decisions/decision-N-045-v2.md` (`c7b05e39…`, sceau OK), lignes 66 à 69 ; dans le clone local
  `/home/user/ideation-organism`, la date d'entrée du fichier `orchestrator/exemples/temoins-pari-demo-v1.json`
  (`git log`, lecture seule, aucun `fetch`).
- **Non fait** : aucun chemin interdit ouvert ; aucun appel de modèle, aucune dépense, aucun commit. Seules écritures : ce
  fichier et son compagnon `.sha256`.
- **Conventions** : [A-T1] = `run-e3-v1/cellules/E3-T1-conception-A.md`, [B-T2] = `E3-T2-critique-croisee-B.md`,
  [E-T3] = `E3-T3-reponse-E.md`, etc. ; « faits l. N » = ligne N de `faits-v1.md` (`9337032a…`). Ce que j'ajoute moi-même,
  qu'aucune espèce n'a écrit, porte la marque **(synthèse)**. Tout chiffre de coût est « estimé » (faits) ou « illustratif »
  (cellules) ; aucun n'est mesuré.
- **Espèces** : A Claude Fable 5.1, B Claude Opus 4.6, C Argon (`gemini-4-argon`), E Astra (`gpt-6-astra`). **D Kimi absent**
  aux trois tours : compte Moonshot suspendu faute de crédit (HTTP 429 à 15:49:34Z, `depense-et-incidents-v1.md` § 1).
  « The Agentic Scientist » = SakanaAI/AI-Scientist-v3 ; les espèces l'appellent souvent « Sakana ».

## Verdict

- **Personne ne met The Agentic Scientist en premier.** Trois espèces sur quatre, de trois familles différentes (A, C, E),
  choisissent **« autre chose »** : une boucle d'expérimentation minimale écrite par le programme, sur Kimi, le relais v3 et
  l'exécuteur `bwrap` existants, comparée à coût apparié aux témoins bon marché ; Kaimen et The Agentic Scientist ne viennent
  qu'ensuite, chacun sur preuve. B (Opus 4.6) garde **Kaimen d'abord**, mais son choix lui-même n'a été attaqué de front par
  aucune critique (§ 1, B). Aucune espèce n'a changé de choix entre le premier et le dernier tour.
- **La synthèse soutient la boucle minimale d'abord, présentée comme le premier barreau commun** : l'outil « expérience » et
  ses gardes sont à écrire de toute façon, Kaimen compris ; la première dépense se limite à une qualification technique et à
  un pilote A/A qui fixe le nombre de mondes ; **aucun duel présenté comme décisif sans puissance financée**. Confiance
  **≈ 0,65** contre « Kaimen d'abord » ; **≈ 0,85** que The Agentic Scientist ne doit pas venir en premier.
- **Réponse à « pourquoi pas lui ? »** (convergente) : ce qui le rend attirant — il exécute vraiment — vient avec exactement ce
  qu'il faut lui retirer (pleins droits, réseau `host`, Web) ; enfermé, son fonctionnement n'est pas établi, il n'est plus le
  système de l'article, il coûte le plus par génération, donc le moins de répétitions et de puissance ; et la question qu'il
  trancherait (« expérimenter aide-t-il, à coût égal ? ») se tranche d'abord pour une fraction du prix. **Il n'est pas
  écarté** : A, C et E retirent la condition « seulement si Kaimen bat le témoin », qui ne dit rien de lui.

---

## 1. Position de chaque espèce

| espèce | premier tour | dernier tour | première expérience au dernier tour | confiance |
|---|---|---|---|---|
| A Fable 5.1 | autre chose (`exp-min`), puis Kaimen, puis The Agentic Scientist après une porte de faisabilité | inchangé, protocole corrigé | sonde de mémorisation « aveugle aux données » (≈ 1 USD, illustratif) | 0,6 au premier tour, non redite |
| B Opus 4.6 | Kaimen d'abord, après prérequis techniques | inchangé | compatibilité Kaimen ↔ relais Kimi v3 (< 1 USD, illustratif), enfermement de The Agentic Scientist en parallèle | non donnée |
| C Argon | autre chose (boucle minimale maison) | inchangé, protocole corrigé | « Porte 0 » : qualification mécanique, déterminisme, pilote A/A sur mondes privés | non donnée |
| E Astra | autre chose (commande Kimi minimale à exécuteur séparé) | inchangé, ambition réduite | qualification contractuelle bornée de la boucle minimale | non donnée |

### A — Claude Fable 5.1 : autre chose d'abord

- **Choix** : « ni (a) ni (b) d'abord » ; une boucle courte « proposer → lancer un script sur les épisodes de développement →
  réviser → rendre N fiches » ([A-T1] 0 ; [A-T3] 3). Kaimen devient « son ablation « + tournoi » », The Agentic Scientist
  « « + agents de code », payé seulement si son enfermement passe une porte mécanique » ([A-T1] 0).
- **Raisons** : aucun candidat n'est un expérimentateur tel quel (faits l. 69) ; une fois l'outil construit, ce qu'on mesure
  n'est plus le produit du marché mais « un modèle Kimi qui exécute […] plus un paquet de machinerie tierce » ; la seule
  variable visée est « **l'accès à l'exécution change-t-il les vraies et fausses découvertes par dollar, lues sur l'oracle ?** »
  ([A-T1] 0). La condition « (a) bat le témoin ⇒ (b) » n'informe pas sur (b) : « si (a) échoue parce que le tournoi sans
  littérature est inerte, cela ne dit rien d'un agent de code » ([A-T1] S6).
- **Ce que la critique change** : A accepte presque tout ([A-T3] table, 23 lignes) : le placebo à sortie vide devient un
  placebo qui **exécute vraiment sur des épisodes permutés** (idée de C) ; un bras « consigne enrichie sans outil »
  (`exp-text`, idée de B) ; le seuil « κ fois l'écart A/A » est abandonné (C) ; ratio des sommes au lieu de moyenne des
  ratios ; nombre de mondes fixé par un calcul de puissance sur le pilote A/A, « si M dépasse les mondes disponibles au
  budget, **pas de GO** » ([A-T3] #8) ; les leurres de la sonde de mémorisation viennent « du même générateur » (lois de la
  course suivante, tenues hors dépôt) ([A-T3] #5). A retire sa phrase selon laquelle les scientifiques du marché « ne font pas
  autre chose » : un échec d'`exp-min` « n'est pas une falsification des cadriciels riches, c'est l'absence de la preuve que
  N-045 exige pour payer » ([A-T3] #15).
- **Réponse finale** : sonde de mémorisation d'abord, puis une comparaison à quatre bras (témoin, `exp-text`, `exp-placebo`,
  `exp-min`) ; Kaimen payé seulement si les deux contrastes sont gagnés ; The Agentic Scientist après une porte de
  faisabilité « hors de l'organisme, sous décision séparée » ([A-T3] 3).
- **Risque principal** : « budget insuffisant pour M (le plus probable, d'après le repère v66) ; alors la bonne réponse est
  « non départagé », écrite » ([A-T3] 3).
- **Mesure qui départage** : le contraste `exp-min` − `exp-placebo`, lu sur l'oracle à coût apparié ([A-T3] 3).
- **Changerait d'avis** : sonde positive (replanter d'abord) ; A/A trop large pour le budget (ne rien brancher) ; enfermement
  de The Agentic Scientist bon marché en pratique et note sur le fond conservée : alors « (b) devant Kaimen comme second bras »,
  parce que « son « + agents de code » est une variable plus proche de ce que le directeur demande que le tournoi de Kaimen »
  ([A-T1] 6 ; [A-T3] 3) ; question du directeur lue comme « tester un produit du marché pour le papier » : modification de
  revendication, hors de son choix.

### B — Claude Opus 4.6 : Kaimen d'abord

- **Choix** : (a), « mais seulement après avoir vérifié les prérequis techniques » ([B-T1], réponse) ; maintenu ([B-T3] (c)).
- **Raisons** : le moins cher à tester (relais v3, pas de Docker ni de relais en flux) ; surface d'attaque plus petite ; ordre
  séquentiel falsifiable : « Si on commence par (b), un échec ne distingue pas « l'exécution d'expériences est inutile » de
  « l'enfermement a cassé l'agent » » ; fidélité perdue mais assumée : le bras mesure « un proposeur structuré avec outil
  d'expérience isolé » ([B-T1], raisons 1 à 4).
- **Ce que la critique change** : B accepte toutes les critiques de méthode ([B-T3] (a)) : sa métrique comptait des lois
  **promues**, contraire à N-058 (relevé par A, C et E) — elle porte désormais sur les fiches **soumises**, lues sur l'oracle ;
  graines différentes au pilote A/A ; non-infériorité sur les fausses ; nombre de mondes par calcul de puissance ; le pont de
  prise Unix n'est plus monté dans le bac des scripts (critique de C) ; nonce du noyau pour prouver l'usage réel de l'outil.
- **Réponse finale** : d'abord l'expérience 1 (Kaimen passe-t-il le relais Kimi v3 avec appel d'outil forcé ?), « la porte la
  moins chère […] et la plus discriminante » ; en parallèle, l'enfermement de The Agentic Scientist ; puis A/A ; puis Kaimen
  contre témoin ; « si H_A tient → brancher (a) en v67 puis considérer (b) » ([B-T3] (b), (c)).
- **Changerait d'avis** : si Kaimen ne passe pas le relais et qu'un correctif coûte plus qu'un relais neuf → inverser ; si
  les mondes de v66 sont triviaux → aucun scientifique utile ; si les agents de The Agentic Scientist marchent sans flux et
  sans réseau → (a) et (b) en parallèle ; A/A trop bruité → rien de tranchable ([B-T1], « Ce qui ferait changer d'avis »).
- **(synthèse)** Aucune critique adressée à B ([A-T2], [C-T2], [E-T2] sur B) ne discute son **choix** face à la boucle
  minimale ; toutes portent sur ses expériences. Sa réponse finale ne répond donc à personne sur ce point, et sa liste de
  « ce qui est établi » range parmi les faits que « (a) est moins chère à tester », ce qui ne repose que sur des estimations
  (faits l. 101-110). Son plan corrigé n'a pas non plus de contrôle de contamination, qu'il réclamait pourtant à C et E
  ([B-T2], « Sonde de mémorisation »).

### C — Argon : autre chose d'abord

- **Choix** : « un **proposeur à boucle minimale maison (ReAct-bwrap)** en un seul fichier Python », opposé à coût égal au
  témoin ; « ni Kaimen […] ni The Agentic Scientist […] ne doivent être branchés en premier » ([C-T1] synthèse) ; maintenu
  ([C-T3] (c) 3).
- **Raisons** : contre la séquence (a) puis (b), « **l'échec de (a) ne falsifie rien concernant (b)** » : tournoi Elo d'idées
  textuelles d'un côté, « débogage itératif de code » de l'autre ([C-T1]) ; contre Kaimen d'abord : « lui écrire nous-mêmes
  son moteur d'exécution revient à développer `Exp-Minimal`, tout en y ajoutant le surcoût en jetons […] et le bruit d'un
  superviseur Elo conçu pour de la synthèse bibliographique » ([C-T3] (c) 3).
- **Ce que la critique change** : la sélection finale passe par **le même filtre mécanique pour tous les bras** (critique de
  A) ; filtre à validation croisée et pénalité de complexité ; quota « au plus M » au lieu de « exactement M » (E : sous le
  nul, un quota fixe force F = M) ; deux témoins, nu et filtré (critique de B) ; placebo `Exp-Masqué` à résidus d'un monde
  indépendant au lieu du message trompeur « aucune anomalie détectée » (A, B, E) ; différence absolue au lieu de « +20 % » ;
  règle d'arrêt de puissance avant dépense ; **tous les duels décisifs sur des mondes plantés neufs jamais versés au dépôt
  public** ([C-T3] (a), (b)). L'affirmation « la question du directeur est tranchée […] pour 8,40 USD (illustratif) »
  ([C-T1] (d)) disparaît.
- **Mesure qui départage** : la différence appariée par monde de vraies découvertes nouvelles par dollar, sous plafond de
  fiches choisies par le même filtre ([C-T3] (c) 3).
- **Changerait d'avis** : témoin filtré ≥ boucle → garder le filtrage passif ; boucle > témoin filtré **et** > placebo → duel
  architectural, contre The Agentic Scientist « s'il faut pousser la complexité du code d'analyse », ou contre Kaimen « s'il
  faut tester le tri par tournoi » ([C-T3] (c) 3).

### E — Astra : autre chose d'abord, qualification avant comparaison

- **Choix** : « une commande Kimi minimale, dotée d'un outil d'expérience isolé » ; « Je ne commencerais ni par importer tout
  Kaimen, ni par enfermer tout The Agentic Scientist » ([E-T1]) ; maintenu, ambition réduite : « Le premier engagement doit
  financer une **qualification technique bornée**, pas encore une comparaison scientifique annoncée comme décisive » ([E-T3]).
- **Raisons** : « The Agentic Scientist mérite une évaluation comme candidat, mais son exécution effective ne démontre ni sa
  compatibilité avec les contraintes, ni son avantage scientifique après confinement. Inversement, **l'échec éventuel de
  Kaimen ne réfuterait pas l'intérêt de Sakana** » ([E-T1]). Architecture : « Le bac du script n'a besoin d'aucun accès au
  relais. Le contrôleur dispose seulement du canal autorisé vers le relais » ([E-T1] B).
- **Ce que la critique change** : retrait du score composite (T − λF)/C (A, B, C) ; A/A par bras à graines différentes ;
  sélecteur commun avec réserve de validation interne — « Cette modification de vue doit être acceptée explicitement » ;
  étude « mécaniste » réduite à une intervention sur le dernier retour d'outil depuis un préfixe commun ; corpus d'équivalence
  pour l'oracle ; plafond d'effectif, aucune prolongation sur indécision ([E-T3] A, B).
- **Réponse finale** : qualification contractuelle d'abord, puis A/A, dimensionnement prudent, puis seulement le duel ; « Si
  le budget ne permet pas la précision prévue, la réponse est « comparaison non financée à précision suffisante », non
  « expérimentation inutile » » ([E-T3] C).
- **Changerait d'avis** : « Je passerais à Kaimen ou Sakana d'abord si leur adaptation qualifiée présente un coût mesuré et
  une fiabilité plus favorables, dans le cadre de N-045 » ; « Une défaite nette de la boucle minimale abandonne cette version
  sur la population testée ; elle ne condamne pas toute expérimentation adaptative » ([E-T3] C).

### D — Kimi : absent

Aucune cellule. Kimi est pourtant le modèle qui ferait tourner chacune des options (§ 6).

---

## 2. Ce qui converge

1. **The Agentic Scientist n'est le premier choix de personne** ([A-T3] 3, [B-T3] (c), [C-T3] (c), [E-T3] C).
2. **Aucun candidat n'est utilisable tel quel ; l'outil d'exécution isolé est à construire dans tous les cas** (faits l. 69 ;
   repris par les quatre).
3. **Métrique** : vraies découvertes **parmi les fiches soumises**, lues sur l'oracle, par dollar ; jamais conditionnées à la
   promotion par le juge ; promotions en diagnostic séparé (B corrigé : [B-T3] A-1 ; [A-T2], [C-T2], [E-T2] sur B).
   Ratio des sommes ΣV/ΣC, non moyenne des ratios ([A-T3] #10, [E-T3] B) ; pas de score composite à pénalité ([E-T3] A6) ;
   les fausses comme contrainte de non-infériorité à marge gelée ([A-T3] #12, [B-T3] exp. 4, [E-T3] B).
4. **Pilote A/A par bras, graines différentes ; unité d'analyse = le monde ; nombre de mondes fixé par un calcul de puissance
   sur ce pilote ; « non jugeable au budget » est une issue légitime, écrite, qui bloque le GO d'un duel décisif**
   ([A-T3] 2.5, [B-T3] exp. 3, [C-T3] Porte 0, [E-T3] B). C'est le principal apport commun du deuxième tour ([B-T2], note
   transversale ; [A-T2], note de position).
5. **Contrôles exigés par tous au dernier tour** : monde sans loi nouvelle ; reformulations des lois connues comptées zéro ;
   sélecteur du témoin comparé au tirage au hasard ; garde « loi plantée » au-delà de la chaîne exacte ; preuve d'usage réel de
   l'outil (nonce) ([A-T3], [B-T3], [C-T3], [E-T3]).
6. **Le bac des scripts n'atteint pas le relais** ; seul le contrôleur l'appelle ([C-T2] sur B, accepté par [B-T3] C-3 ;
   [E-T1] B).
7. **Le GO de 15 USD ne couvre que ce tour** ; toute expérience proposée relève d'un devis et d'un GO séparés ([A-T1] 5,
   [E-T1] D, [E-T2] sur B, [B-T3] E-5).

## 3. Ce qui diverge encore

1. **Le premier branchement** : boucle minimale (A, C, E) contre Kaimen (B).
2. **La première dépense** : sonde de mémorisation (A) ; compatibilité de Kaimen avec le relais et enfermement de The Agentic
   Scientist (B) ; qualification et pilote sur mondes privés (C) ; qualification contractuelle (E).
3. **Le témoin principal** : « N-045 littéral » sans épisodes (vote à k), le témoin filtré en secondaire ([A-T3] #11) ; les
   deux, décision contre le témoin filtré ([C-T3] duel 1.2) ; générations indépendantes plus sélecteur commun à réserve de
   validation ([E-T3] B) ; témoin qui choisit par filtre mécanique, scientifique par son propre classement ([B-T3] exp. 4).
4. **La sélection finale** : même filtre mécanique pour tous les bras (C, E) contre classement propre du bras (B) ; A fixe
   le même quota sans trancher qui choisit.
5. **Le placebo** : épisodes permutés plus bras sans outil (A) ; résidus d'un monde indépendant (C) ; intervention sur le
   seul dernier retour, sans prétendre isoler une information « pure » (E).
6. **La contamination** : sonde dédiée (A) ; mondes neufs jamais publiés pour tout duel décisif (C, E) ; rien (B).
7. **Ce qu'un échec de la boucle minimale fait aux cadres du marché** : pas une réfutation, mais « l'absence de la preuve que
   N-045 exige pour payer », l'interaction restant une hypothèse « à tester si quelqu'un la finance » ([A-T3] #15) ; hypothèse
   ouverte qui exige devis et GO propres ([C-T3] (a), critiques de E, point 2) ; Kaimen ou The Agentic Scientist restent qualifiables sur leurs propres
   mérites ([E-T3] C).
8. **L'ordre Kaimen → The Agentic Scientist** : gardé (B) ; gardé sauf si l'enfermement se révèle bon marché (A) ; retiré
   (C, E).

## 4. Arguments neufs par rapport à la note de conception

### 4.1 Sur « pourquoi pas The Agentic Scientist ? »

La note répondait par le coût, le Docker, le relais en flux et les pleins droits (note, § 4, option (b)). Le tour ajoute :

1. **La condition « (b) seulement si (a) bat le témoin » ne dit rien de (b)** : (a) et (b) ne partagent pas la variable
   testée (tournoi de texte contre agent de code) ; un échec de Kaimen peut venir du tournoi sans littérature ([A-T1] S6,
   [C-T1], [E-T1]). B ne défend pas cette condition contre cette objection.
2. **C'est le seul candidat pour qui la fuite de l'oracle est le comportement par défaut**, « pas un accident » ([A-T1] 4).
3. **Son coût par génération détruit la puissance à budget fixé** : peu de générations, donc des intervalles qui couvrent tout
   seuil ([C-T3] (c) 3 ; [A-T2] sur C, « hétéroscédasticité construite »).
4. **Enfermé et réduit à l'investigation, ce n'est plus le système de l'article** : même perte de fidélité que Kaimen sans
   littérature ([A-T1] 4).
5. **Le risque d'un enfermement n'est pas le plantage mais la dégénérescence silencieuse du contenu** ([B-T2] sur A, point 4) :
   d'où une porte de faisabilité notée sur le fond, avec nonce par run et canari cité dans la tâche ([A-T3] 2.4).
6. **Une boucle minimale teste « le cœur du mécanisme » de The Agentic Scientist** (écrire un script, l'exécuter, lire, réviser)
   dès maintenant sur l'infrastructure existante ([C-T3] (c) 3).
7. **Ce qui le ferait passer devant Kaimen** : un enfermement bon marché en pratique (A) ; un goulot de complexité du code
   révélé par les traces (C) ; une adaptation qualifiée au coût mesuré plus favorable (E).

### 4.2 Autres arguments neufs

1. **Une option que la note n'avait pas posée** : entre (a) (Kaimen plus outil) et (c) (vote à k, sans exécution), la boucle
   minimale avec exécution, sans cadre tiers. La note écartait Swarm parce qu'il faudrait « écrire l'outil, la sortie
   structurée et la boucle ; c'est réécrire » (note, § 2, table) ; c'est exactement ce que trois espèces proposent, mais réduit
   au minimum, pour isoler la variable.
2. **Attribution** : sans placebo ni bras « consigne enrichie sans outil », un gain de la boucle peut venir de la consigne ou
   des tours de révision, non de l'exécution ([B-T2] sur A ; [E-T2] sur A ; [A-T3] #1-#3).
3. **Contamination par la mémoire d'entraînement** : « « aucun Web » coupe la lecture en ligne, pas la mémoire
   d'entraînement d'un modèle du marché » ([A-T1] S8) ; contre-arguments sur l'identification (exposition et difficulté
   confondues, [B-T2], [C-T2], [E-T2] sur A) ; remède jugé le plus propre par C et E : des mondes neufs jamais publiés.
   **(synthèse)** Dans le clone local de l'organisme, le fichier de témoins entre à l'historique le 2 novembre 2026
   (`bfa5a02`) ; mais le clone est superficiel (50 commits) : la date de première exposition publique n'est pas établie ici.
   La comparer à la date de coupure d'entraînement de `kimi-k3.1-pro` est une vérification à 0 USD qui dirait si la mémoire
   paramétrique est seulement possible.
4. **« Meilleur de N » exige une règle de « meilleur »** ; une règle mécanique sur les épisodes de développement est déjà un
   expérimentateur passif, à mesurer à part ([C-T2] et [B-T2] ; [C-T3] B.1). **(synthèse)** N-045 nomme deux témoins
   distincts, « le meilleur de N tirages indépendants » et « un modèle, vote à k, coût apparié »
   (`decision-N-045-v2.md` l. 67-69) ; et son point 4 exige la comparaison « sur familles tenues à l'écart » (l. 67), ce qui
   appuie les mondes neufs de C et E.
5. **Quota et abstention** : avec un score pénalisé, ne rien soumettre peut battre tout expérimentateur ; avec un quota fixe
   sous le nul, F = M par construction ([C-T2] sur E ; [E-T2] sur C) : d'où « au plus q » avec une règle d'abstention commune.
6. **Coût vérifié par bras** : rapprochement de `cout_usd` avec le relevé du relais bras par bras, un écart différentiel
   invalidant la comparaison ([A-T3] #23).
7. **(synthèse)** Si le contrôleur de la boucle minimale est du code du programme qui tourne hors du bac, comme le propose E,
   et que seuls ses scripts passent par l'exécuteur `bwrap`, le **pont de prise Unix** que la note met parmi les préalables
   (faits l. 135-136) ne sert plus à cette boucle ; il reste nécessaire pour un cadre tiers qu'on enferme lui-même (Kaimen sous
   `bwrap`, The Agentic Scientist). À vérifier dans le code v67.

## 5. Erreurs de fait et de calcul relevées

- [B-T1] : le GO de 15 USD « couvre les expériences 1-3 » — faux (R-2380 : un tour du collisionneur) ; corrigé ([B-T3] E-5).
- [B-T1] : vraies découvertes définies comme « lois *promues* », contraire à N-058 (faits l. 47-48) ; corrigé.
- [B-T1], instrument 3 : le pont donnerait au code du bac l'accès au relais ; corrigé ([B-T3] C-3).
- [B-T2] sur C : « la note ne mentionne pas un tri mécanique sur les épisodes de développement » — faux : faits l. 111-113
  et note § 2.1 le posent comme option ; relevé par [C-T3] B.1.
- [B-T3] : « (a) est moins chère à tester » rangé dans « ce qui est établi » ; ce n'est qu'une estimation (faits l. 101-110).
- [B-T3] C-6 : « n ≥ 25 » pour séparer une fiabilité de 0,70 d'une de 0,50 au risque 0,05. **(synthèse, calcul binomial
  exact unilatéral)** : à n = 25, la puissance contre 0,70 est d'environ 0,51 ; il faut environ n = 37 pour 0,8.
- [B-T2] : valeurs p minimales de permutation « 1/252 » (5 mondes) et « 1/20 » (3 mondes) : ce sont celles de deux groupes
  indépendants ; les dessins visés sont appariés par monde, soit 1/32 et 1/8 en unilatéral **(synthèse, calcul)**. La
  conclusion (puissance faible) tient.
- [C-T2] sur A : le quantile de Cauchy est écrit tan(π(1 − α/2)), qui vaut environ −0,079 ; la valeur annoncée, 12,7, est
  juste (tan(π(0,975 − 0,5)) ≈ 12,706) **(synthèse, calcul)**. La conclusion tient.
- [C-T2] sur A : la variance du coût d'`exp-min` est déduite des 1,3 à 12 USD estimés… pour Kaimen ; objet confondu.
- [C-T1] : « Kaimen coûtant déjà 7 à 60 fois (estimé) le prix d'un proposeur » et The Agentic Scientist « coût multiplié par
  10 à 100 » : rapports absents des faits, qui donnent « de quelque 7 à 500 fois » pour un scientifique en général
  (faits l. 109) ; non sourcés.
- [A-T3] #11 : le « témoin primaire = N-045 littéral (« meilleur de N » choisi sans les épisodes : vote à k, coût apparié) »
  fond en un seul les deux témoins distincts de N-045 (l. 67-69) **(synthèse)**.
- **(synthèse)** Tout le tour prend pour acquis que N-045 s'applique à ce choix ; son point 4 vise littéralement les voies « à
  concepteur entraîné par renforcement » (`decision-N-045-v2.md` l. 66-69) ; l'extension au rôle d'expérimentateur est celle
  de la note et des faits (faits l. 49-51). Elle est raisonnable, mais c'est une lecture, que Lazar peut confirmer.

## 6. Faiblesses du tour et leur effet possible

1. **Kimi absent.** C'est le modèle de toutes les options et la seule espèce « de l'intérieur » de l'organisme. Effet : une
   voix de moins, de sens inconnu. Ce qu'il aurait pu dire de lui-même (appel d'outil forcé, lecture en flux) n'aurait pas
   valu preuve : ce sont des essais mécaniques (B, expérience 1). **Conséquence pratique, hors débat** : sans recharge du
   compte Moonshot, aucune des options ne peut tourner sur la clé de cet environnement
   (`depense-et-incidents-v1.md` § 5) ; si la course v66 dépend du même compte, elle aussi (à vérifier par la mère).
2. **Poids de la famille Claude.** Deux espèces sur quatre (A, B), plus l'auteur de la note, l'opérateur et ce lecteur.
   Effet limité ici : la majorité réunit trois familles (A Claude, C Google, E OpenAI) et le seul dissident est un Claude (B).
3. **Plafonds de sortie bas** (`devis-v1.md` § 2 : A 22 000, B 10 000, C 18 000, E 8 000 jetons au premier essai). Aucune
   troncature, aucune relance, marqueur de fin partout (`etat.md`) ; sorties consommées (journal masqué) : A 59 à 67 %,
   B 62 à 70 %, C 35 à 38 %, E 64 à 68 % de leur plafond. Effet possible, non mesurable : réflexion comprimée chez B (pour
   un modèle Claude, le plafond borne aussi la réflexion) et chez E (253 à 512 jetons de réflexion par cellule) ; B répond
   surtout par une liste d'acceptations et ne discute pas la boucle minimale, E refuse tout effectif numérique au dernier
   tour. Rien n'établit que
   ce soit l'effet des plafonds.
4. **Ancrage de la question.** Elle nomme (a) en premier, avec sa confiance (0,55), et le mot de Lazar la répète (faits
   § 8) : ancrage vers (a), que trois espèces sur quatre n'ont pas suivi. **Ancrage inverse possible** : les faits posent en
   gras « aucun candidat n'est, tel quel, un expérimentateur » (faits l. 69), la question parle d'un « outil d'exécution neuf
   et isolé » et déclare « autre chose » « recevable au même titre » ; le pas vers « écrire la boucle soi-même » est court.
   La convergence de A, C et E peut en partie venir du cadrage ; leurs arguments (variable isolée, condition (a)→(b) non
   informative, outil à écrire de toute façon) tiennent néanmoins par eux-mêmes.
5. **Candidats vus de seconde main.** Aucune espèce n'a lu le code ; tout jugement sur Kaimen et The Agentic Scientist repose
   sur le résumé RAPPORTÉ de la note. Les incertitudes clés (appel d'outil forcé sur Kimi, lecture en flux, fonctionnement
   sans réseau) restent entières ; elles se tranchent par essai, pas par débat.
6. **Pas de critique des dessins finaux.** Les plans du dernier tour (quatre bras de A et C, intervention terminale de E)
   n'ont été relus par personne ; le choix de B n'a pas été attaqué. Une seule confiance chiffrée (A, 0,6, premier tour).
7. **Débat surtout méthodologique** : l'essentiel du deuxième tour porte sur la puissance et les contrôles, utile pour le
   préenregistrement, moins sur la question de fond « quel cadre ».

## 7. Recommandation du lecteur

**Brancher d'abord la boucle minimale, comme premier barreau commun, et payer d'abord l'information la moins chère. Confiance
≈ 0,65** (contre Kaimen d'abord) ; **≈ 0,85** que The Agentic Scientist ne vient pas en premier.

Raisons : (i) l'outil « expérience » et ses gardes sont le cœur de (a) comme de la boucle : les écrire d'abord ne coûte rien de
plus et ne ferme aucune option **(synthèse)** ; (ii) la boucle isole la seule variable que les trois cadres partagent, au prix
le plus bas, ce qui est l'esprit de N-045 ; (iii) la condition « (b) seulement si (a) bat le témoin » ne protège rien et doit
tomber ; (iv) trois familles convergent, et l'objection de B (« commencer par (b) ne sépare pas l'inutilité de la casse ») ne
vaut pas contre la boucle.

Ordre proposé **(synthèse, à partir de [A-T3], [C-T3], [E-T3], [B-T3])** :

1. **À 0 USD, hors ligne** : l'exécuteur d'expériences et ses gardes, chacune éprouvée sur un cas sain et un artefact (R5) ;
   la boucle minimale, essayée contre un amont factice ; les contrôles mécaniques de l'oracle (reformulations des lois
   connues, monde sans loi nouvelle, monde à loi accessible, invariance à la provenance) ; la comparaison des dates
   d'exposition publique des pièces avec la coupure d'entraînement de Kimi ; la décision sur les mondes du futur duel
   (neufs, non publiés, familles tenues à l'écart).
2. **Petit devis, après recharge du compte Moonshot** : qualification contractuelle de la boucle (E), coût mesuré par bras,
   et — information bon marché utile quel que soit le choix — l'essai d'appel d'outil forcé de Kaimen sur Kimi (B,
   expérience 1) ; puis pilote A/A par bras, qui fixe le nombre de mondes.
3. **GO d'un duel décisif seulement si ce nombre est financé** : boucle contre témoin nu et témoin filtré, plus placebo, à coût
   apparié, sur les fiches soumises lues sur l'oracle ; sinon, écrire « comparaison non financée à précision suffisante ».
4. **Ensuite** Kaimen et The Agentic Scientist, chacun contre la boucle, chacun avec sa qualification et son devis, sans que
   l'un conditionne l'autre ; l'enfermement de The Agentic Scientist peut être éprouvé sur un banc technique hors de
   l'organisme dès qu'un devis le permet.

Points que le préenregistrement devra trancher (divergences du § 3) : témoin principal ; sélection finale commune ou propre ;
quota « au plus q » et règle d'abstention ; forme du placebo ; marge de non-infériorité des fausses ; réserve de validation
dans la vue servie (modification de la vue, [E-T3] B) ; règle d'équivalence de l'oracle éprouvée avant usage.

**Ce qui ferait réviser** : l'essai de Kaimen passe du premier coup et son adaptation se révèle moins chère que la boucle
(→ Kaimen d'abord, condition de E) ; l'enfermement de The Agentic Scientist marche à bas coût sur banc (→ lui comme second
bras, avant Kaimen, condition de A) ; le but de Lazar est d'avoir un **produit du marché** branché à une date, plutôt qu'une
preuve (→ Kaimen d'abord est le chemin le plus court vers une démonstration, pas vers une mesure ; c'est un choix de Lazar) ;
le pilote A/A montre que le nombre de mondes nécessaire dépasse tout budget raisonnable (→ ne rien brancher pour l'instant et
le dire).

## 8. Ce que la mère soumet à Lazar (texte proposé)

> **Décision** : quel premier expérimentateur préparer pour l'organisme, après la course v66 : une boucle minimale écrite par
> nous, Kaimen (Co-Scientist), ou The Agentic Scientist.
>
> **Enjeu** : savoir à bas coût si faire des expériences améliore les vraies découvertes par dollar (lues sur l'oracle des
> mondes plantés), avant de payer un cadre du marché, sans fuite du monde planté.
>
> **Options** :
> 1. **Boucle minimale d'abord** (avis de Fable 5.1, Argon et Astra) — *avantage* : teste la seule variable commune au plus bas
>    prix, sur le relais v3 et l'exécuteur `bwrap` existants, sans code tiers ni relais neuf ; l'outil d'expérience sert
>    ensuite à Kaimen ; Kaimen et The Agentic Scientist viennent après, chacun sur preuve, sans que l'un dépende de l'autre.
>    *Inconvénient* : ce n'est pas encore un « scientifique du marché » (ce que tu avais choisi le 11, R-2370) ; code à nous,
>    sans évaluation tierce ; issue probable « non départagé au budget ».
> 2. **Kaimen d'abord** (note de conception ; Opus 4.6) — *avantage* : un cadre du marché branché le plus tôt ; relais v3
>    inchangé si l'appel d'outil forcé passe sur Kimi. *Inconvénient* : il faut écrire l'outil d'expérience de toute façon ;
>    sans littérature ce n'est plus Co-Scientist ; son résultat mêle tournoi et exécution et ne dit rien de The Agentic
>    Scientist ; l'appel d'outil forcé n'a jamais été essayé.
> 3. **The Agentic Scientist d'abord, enfermé** — *avantage* : le seul qui exécute vraiment ; réponse directe à ta question.
>    *Inconvénient* : le chantier le plus lourd (Docker, relais en flux neuf, pont réseau), enfermement jamais éprouvé, fuite
>    du monde planté par défaut s'il reste une route, coût par génération le plus élevé donc le moins de répétitions, un agent
>    a déjà modifié son protocole d'évaluation ; aucune des quatre espèces ne le met en premier.
>
> **Pourquoi pas lui, en une phrase** : ce qui le rend attirant (il exécute) vient avec ce qu'il faut lui retirer, et la
> question qu'il trancherait se tranche d'abord pour bien moins cher ; il n'est pas écarté, et la condition « seulement si
> Kaimen gagne » est retirée parce qu'elle ne dit rien de lui.
>
> **Recommandation** : option 1, confiance ≈ 0,65 (contre l'option 2) ; ≈ 0,85 que l'option 3 ne vient pas en premier. Toute
> dépense passe par devis et GO, et Kimi exige d'abord la recharge du compte Moonshot.
>
> **Défaut sous 48 heures** : préparation hors ligne, sans dépense, de ce qui est commun aux options 1 et 2 — l'outil
> d'expérience vers l'exécuteur isolé, ses gardes et la boucle minimale, essayés contre un amont factice.

**(synthèse)** Le défaut proposé ne préjuge pas du choix entre 1 et 2 ; il remplace celui de R-2372 (préparation hors ligne de
(a) seule) par son noyau commun. La mère dira dans quelle mesure il s'écarte du mot de Lazar du 11 novembre (R-2370 :
« option (a) de R-2368 », un scientifique du marché comme rôle d'expérimentateur) : l'option 1 en est une étape, pas un
remplacement, tant qu'un cadre du marché reste visé ensuite.

## 9. Réserves

- Synthèse d'un lecteur de la famille Claude, comme deux des quatre espèces, l'auteur de la note et l'opérateur du tour.
- Mes confiances (0,65 ; 0,85) sont des jugements, non des mesures.
- Mes calculs (§ 5) sont des vérifications de formules sur les valeurs des cellules ; ils ne portent sur aucune donnée.
- Les coûts de tout le dossier restent « estimés » ou « illustratifs » ; rien n'est mesuré.
- Je n'ai pas vérifié le code des candidats ; tout ce qui les décrit vient des faits et de la note (RAPPORTÉ).

*Fin de rédaction : 2026-11-11T16:26:40Z (`date -u`), avant le scellement. Version 1 ; jamais réécrite (R12).*
