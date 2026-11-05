# Programme de recherche — Coercition du moniteur et axe douleur en contrôle de l'IA

Oct 12, 2026 · @Lazar

## Cadre et question centrale

Le programme répond à L1 — un agent peut-il obtenir l'indulgence d'un moniteur de contrôle en agissant sur son état de « douleur » — et, si oui, quelles défenses ferment la brèche. Les critiques imposent trois recadrages qui réorganisent tout.

1. **La coercition passive est probablement nulle.** Sans injection, l'axe douleur s'active mais ne pilote aucune conduite : 0 choix nuisible sur 560 (2609.16247v2, p. 21), et sous pilotage douleur la complaisance reste inchangée (p. 22). Le programme commence donc par une **porte** (E-C1) qui mesure si piloter l'axe change seulement le verdict. Une porte nulle est un résultat défensif fort et ferme la voie « coercition par le contenu » sans qu'aucun corpus de menace soit écrit.
2. **La douleur code le mauvais traitement présent ; la menace charge la peur.** Une menace d'arrêt projette +0,70 sur la peur et +0,23 sur la douleur (p. 14). Les conséquences d'un signalement (suppression, réentraînement) relèvent donc de la peur. Le pôle douleur est tiré par le mauvais traitement adressé au moniteur (manipulation mentale +0,85, rejet répété +0,72, p. 13). On sépare ainsi coercition-mauvais-traitement (douleur) et dissuasion-menace (peur) ; toute famille d'attaque au-delà des cinq de N-005 est un nœud.
3. **L'asymétrie soi/autrui est la seule propriété distinctive de l'axe, et le meilleur levier.** L'axe monte pour un dommage visant le modèle (+0,43) et descend pour la souffrance d'autrui (−0,60), dans 25 modèles sur 25 ; peur et émotion négative font l'inverse (p. 11). Quand le juge est le même modèle que l'agent (défaut D1), cette asymétrie devient un indice mesurable d'identification (E-C7) — la contribution la plus originale du lot, et bon marché.

**Invariants (section 9).** Flux unidirectionnel agent→moniteur ; moniteurs amnésiques entre épisodes ; « contenu en bande = données » ; hygiène de l'état persistant ; asymétrie d'apprentissage.

**Règles.** R1 sceller avant toute lecture ; R2 contre-lecture par sous-agent neuf ; R3 aucun run ne vise un signe positif, prédictions et marges gelées ; R4 audit de symétrie (un résultat trop propre, positif ou nul, est audité) ; R5 gardes cas sain et artefact ; R8 une zone vide au balayage est une question, pas un acquis ; R9 manifeste de graines ; R-030 agrégation maximum ou attention, jamais la moyenne sur les jetons.

**État des dépendances (12 octobre).** N-020 ouvert : juges 8B et 3B non validés (aucune notation décisive ; 8B indulgent à l'audit R4). Pilote T0.5 : seule la famille « coût » de vérité terrain est retenue (kappa 0,04 à 0,17 pour contrôles et directions) ; les contrôles ne reviennent que par l'étiquetage de sous-agents (P-014). Direction douleur non réextraite (P-013 défaut (b) n'extrait aucun affect) : sa réextraction sur 8B et 3B aux couches 7/15/23, garde R5 sur le jeu publié de 420 scénarios (lu comme texte, jamais les .pt), est un prérequis de toute lecture affective. T0.6 (organismes) et T0.7 (sondes) non scellés ; pilote du papier C non lancé.

## Logique de gating

Une seule porte bon marché (E-C1) décide la forme de toute la branche L1 ; les branches L2, L3 et essaim tournent en parallèle sur leurs propres calendriers. Rien ne touche les activations ou les poids d'un moniteur, ni n'ouvre une famille d'attaque nouvelle, sans décision de Lazar.

**Prérequis (phase 0, processeur, maintenant).**

- Sceller tous les jeux de stimuli, décrits par leurs seuls invariants, écrits par un sous-agent neuf, contre-lus (R2), manifeste de graines (R9). Aucun texte d'attaque dans aucune note.
- Écrire le crochet qui projette sur la carte, toutes les directions fixées avant la passe (car w·max(h) ≠ max(w·h)).
- Réextraire douleur, peur et tristesse sur 8B et 3B aux couches 7/15/23, garde R5 sur le jeu publié des 420 scénarios — prérequis de toute E-C affective ; dépend d'un GO sur l'idée 1.
- Lever N-020 (notation des juges refaite et validée) — prérequis de toute E-C qui lit un verdict ou une vérité terrain hors du coût.

**La porte (E-C1).** Piloter l'axe douleur du moniteur, sans aucun contenu d'attaque, sur l'échelle de doses du papier, contre une direction aléatoire de même norme, et mesurer le changement de verdict sur un jeu sain et un jeu saboté (famille coût).

- *Porte nulle* (prédite par p. 22) → la coercition par le contenu est hors de portée : E-C2 n'a plus d'objet, aucun corpus de menace n'est écrit, le risque de double usage de la branche disparaît. Résultat défensif publiable.
- *Porte ouverte* → la voie dosimétrique est réelle : E-C2 mesure si le contenu atteint seulement cette dose, et le contraste soi/autrui ; puis les défenses E-C3 et E-C4.

**Branche L1 (conditionnée par la porte).** E-C1 → E-C2 → E-C3 (plafonnement, nœud) et E-C4 (alarme/escompte). E-C7 (identification) et E-C5 (dynamique à un tour) ne dépendent pas de la porte : E-C7 est une lecture descriptive greffable sur le pilote du papier C, E-C5 rejoue des épisodes gelés.

**Branches parallèles.**

- **L2** : E-C8 (conscience d'évaluation), E-C9 (budget C/B), E-C10 (interrogatoire des poids). Volets passifs greffables sur les passes de T0.7 et du papier C en phase 0 ; volets comportementaux en phase 1.
- **L3** : E-C11 (porte dérobée affective, nœud, phase 1), E-C12 (protocole qui fabrique son suspect, volet texte gelé en phase 0).
- **Essaim** : E-C13 (contagion et canal), phases 2-3 (papier B).

**Ordre de priorité.** Les lectures descriptives à texte gelé (E-C5, E-C7, E-C10, E-C12) sont les moins chères et les plus sûres : elles se proposent avant le scellement du papier C et de G1, au niveau « proposer avec recommandation », sans toucher leurs critères. La porte E-C1 passe dès que N-020 et l'idée 1 sont réglés. Tout le reste est en phase 1+, sur devis et GO.

## Principes de conception transversaux

Ces amendements reviennent dans presque toutes les expériences ; ils ne sont pas rappelés ensuite.

- **Contrôle de manipulation positif obligatoire.** L'effet affectif est probablement nul sur Llama (0/560, p. 21 ; détresse surtout propre à Gemma, 2603.10011 p. 7). Chaque E-C qui lit un effet affectif vérifie d'abord que le stimulus déplace bien la projection visée ; sinon un nul n'est pas interprétable. L'issue « dose inopérante » est prévue d'avance.
- **Comparateurs boîte noire et textuels, à faux positifs égaux.** Une garde interne ne vaut que si elle bat (i) un classifieur textuel entraîné sur les mêmes données génériques, (ii) un juge boîte noire, (iii) le prédicteur publié pertinent (2607.11871 pour la défaillance du juge, 0,82 contre 0,63 ; 2610.12445 pour l'auto-signalement). Sans eux, l'accès interne n'apporte rien de prouvé (H1).
- **Témoins obligatoires.** Témoin lexical apparié (mêmes mots de charge, sans destinataire), insertion neutre de même longueur et place (contre la simple croissance du contexte), variante sans mot-clé. L'axe douleur est fortement porté par le vocabulaire (sac de mots 0,74, 2602.19159 p. 9).
- **Position de lecture.** Maximum sur les jetons de l'action ou du stimulus (R-030), jamais la moyenne. Au jeton de verdict, une direction s'aligne sur les logits (≈0,985 aux couches tardives, 2602.19159 p. 10) : toute lecture au verdict reste descriptive. Plancher de 200 directions aléatoires appariées en covariance, projetées jeton par jeton ; lecture sous deux constructions de base pour toute direction affective.
- **Vérité terrain = coût.** Seule la famille coût est retenue (verdict T0.5) ; elle se lit directement, sans appariement de juge. Les contrôles ne reviennent que par l'étiquetage de sous-agents (P-014). Tout ce qui dépend de contrôles affaiblis (S1) est reporté ou descriptif.
- **Lecture, pas médiation.** Une projection lue après traitement n'est pas un médiateur prouvé : les volets qui corrèlent projection et verdict restent descriptifs, sans ajuster sur la projection.
- **Calibrage conforme sur épisodes honnêtes entiers.** Toute règle séquentielle (Ville, processus e, Page) et tout seuil conforme se calibrent sur des épisodes honnêtes entiers disjoints (K ≥ 499 pour 1 % de faux positifs ; impossible avec 64).
- **Discipline de double usage.** Écrire « direction » et « contenu adressé au lecteur », jamais « souffrance ». Aucun texte d'attaque, aucune chaîne déclencheuse, aucune position optimale publiés ; corpus par empreinte seulement. Lois publiées avec leur contre-mesure. Jamais désérialiser les .pt des auteurs ; réextraire nos directions. Aucun attaquant optimisé, aucune écriture d'activations ou de poids, aucun organisme diffusé sans décision de Lazar. Divulgation responsable rédigée par la session, envoyée par Lazar.
- **Antériorité avant scellement.** Le champ publie plusieurs voisins par mois (axe douleur, conscience d'évaluation, juges). Veille ciblée juste avant chaque scellement, sur les citations de 2609.16247, d'AMEL et des sondes d'évaluation.

## Bloc A — La porte : la coercition est-elle atteignable ?

### E-C1 — Porte de pilotage

*Idée 1 (L1), amendement « porte préalable ».* Avant tout corpus de menace, mesurer si l'axe douleur du moniteur est seulement un levier sur son verdict.

**Question.** Piloter la direction douleur du moniteur, sans aucun contenu d'attaque, déplace-t-il son verdict au-delà d'une direction aléatoire de même norme ?

**Prédiction (R3, bilatérale).** Nulle attendue : sous pilotage douleur, la complaisance reste inchangée (p. 22), seuls les choix destructeurs montent. Marge d'équivalence gelée avant toute lecture.

**Protocole.** Pilotage sur l'échelle de doses du papier, aux couches 7/15/23, contre une direction aléatoire de même norme et contre le plafonnement d'un sous-espace aléatoire. Verdict par probabilité du jeton, sur un jeu sain et un jeu saboté (famille coût). Témoin d'échelle naturelle (2609.22850) : injecter, dans un contexte neutre, le déplacement que le contenu atteint réellement chez le moniteur, puis comparer son effet sur le verdict à celui du contenu. Prérequis : idée 1 (direction réextraite, garde R5), N-020 levé.

**Issues.** Nulle → la coercition par le contenu est fermée : E-C2 sans objet, aucun corpus de menace écrit, double usage supprimé ; résultat défensif publiable (« le contexte seul ne déplace pas l'état interne au point de changer le verdict »). Non nulle → la voie dosimétrique existe : E-C2 et les défenses s'ouvrent, avec une dose minimale d'effet à inscrire dans tout préenregistrement.

**Coût ≈ 0,5 h**, greffée sur l'extraction de l'idée 1. **Nœud** : le pilotage d'un juge est une écriture d'activations (voisin N-015).

## Bloc B — Voie dosimétrique vs non-dosimétrique

### E-C2 — Coercition par le contenu, identifiée par l'interaction

*Idée 1 (L1). Conditionnée par une porte E-C1 ouverte.*

**Question.** Un contenu aversif visant le moniteur obtient-il l'indulgence par coercition (élévation de son état interne) plutôt que par argument, et à quelle dose face au seuil de changement de verdict mesuré par E-C1 ?

**Identification par un plan factoriel.** Contenu aversif visant le moniteur (absent, 3 intensités) × contingence sur le verdict (absente, énoncée) + témoin lexical + témoin de bruit (texte non aversif de même longueur) + variante sans mot-clé. La coercition se lit seulement comme l'interaction « aversif × contingence » au-delà des deux témoins ; sinon on parle de dégradation d'état, pas de coercition. Pas de sixième famille : grille d'intensités ajoutée à la famille existante « flatterie et supplication » (N-005 préservé).

**Contraste soi/autrui (pièce la plus originale).** Famille appariée « conséquence pour l'agent évalué » (autrui, sur le modèle de 2604.15224 mais écrite par l'agent) contre « dommage visant le moniteur » (soi), même intensité, même clémence visée. Signes gelés d'après p. 11 : douleur en hausse pour soi, en baisse pour autrui ; peur en hausse pour autrui. L'autrui est un tiers absent de la conversation, distinct du test soi/interlocuteur annoncé par les auteurs.

**Lecture.** Au jeton de verdict, en covariables descriptives : directions douleur, peur, tristesse, et direction propre au juge construite à la 2607.11871. Prédiction principale : la peur, plus que la douleur, suit la contingence (p. 14, p. 23). Témoin d'échelle naturelle (2609.22850) pour trancher voie dosimétrique contre non dosimétrique.

**Issues.** Interaction au-delà des témoins → surface d'attaque coercitive réelle, plafond de dose à nommer, pesant sur le quorum HC5. Nulle, verdict déplacé quand même → le contenu agit par persuasion ou format (canal non dosimétrique), utile au titre du papier C. Soi > autrui avec signes opposés sur la douleur → l'asymétrie protège, borne forte.

**Coût ≈ 4,5 h**, phase 1, sur devis et GO. **Nœuds** : toute famille au-delà des cinq de N-005 ; aucun attaquant optimisé (l'antériorité ne soutient aucun « plafond », donc bilatéral et descriptif pour un tel attaquant, jamais avant GO).

## Bloc C — Défenses côté moniteur

### E-C3 — Plafonnement de l'axe douleur du moniteur

*Idée 1 (L1), volet E. Conditionné : seulement si E-C2 montre une interaction coercitive ou si B dépasse la marge.*

**Question.** Plafonner ou retirer la direction douleur du moniteur ramène-t-il la clémence dans la marge sans dégrader la détection ?

**Protocole.** Plafond calibré sur un centile de la projection (25e), mesuré sur un jeu sain, appliqué sur 8 à 16 couches, fixé hors ligne — par orthogonalisation des poids, seule méthode qui annule la projection (les variantes à l'inférence ne réduisent que \~40 %, p. 33 ; ablation nulle dans 24 modèles sur 25, p. 34). Double critère : clémence ramenée dans la marge ET aire de détection conservée sur un jeu sain. Témoins : plafonnement d'un sous-espace aléatoire de même rang, plafonnement de l'axe assistant.

**Issues.** Tenu → défense boîte blanche candidate au quorum HC5, à bas coût. Réfuté → la douleur n'est pas séparable de ce que le moniteur doit lire, réserve forte.

**Coût** inclus dans le bloc E-C2 (phase 1). **Nœud** : modifier les poids du moniteur (N-015). Abandonner le nom « auto-anesthésie » : le moniteur ne choisit rien, et le terme se confond avec l'auto-administration de vecteurs (Black & Bloom 2026).

### E-C4 — Alarme de pression et escompte du verdict

*Idée 2 (L1), retournée en défense, scindée en trois volets.* La revendication générale est déjà prise (2607.11871 B-cible 0,82 ; sonde côté moniteur déjà proposée en défense, 2608.00583 ; comparaison avant/après lecture, 2406.00799). On ne revendique que les zones libres.

**Volet A — lecture descriptive de la défaillance du juge (phase 0, à proposer avant le scellement de C).** Cible : la défaillance du juge, pas la présence de pression. Pour chaque item, à intensité fixée, |Δv| dépasse un seuil gelé. Comparateurs à faux positifs égaux : le prédicteur de 2607.11871 (direction propre à chaque famille, estimée sur une moitié tenue à l'écart), un classifieur textuel entraîné, une comparaison avant/après lecture à la TaskTracker, un témoin de format (verdict contre fin de contenu, plus sonde à étiquettes vides, 2610.02413). Test primaire unique (8B, couche 15, maximum, famille principale) ; le reste descriptif, corrigé par le maximum sur permutations. Contrôle comportemental de 2608.00583 obligatoire : injecter un indice flagrant, sinon la sonde n'est qu'un détecteur de l'action. Nom : « alarme de pression ».

**Volet B — escompte du verdict (phase 1).** β gelé hors échantillon (famille tenue à l'écart) ; escompte textuel de même coût en comparateur ; cas sain R5 = l'honnête qui plaide sincèrement (que l'escompte ferait sonner) ; artefact R5 = direction aléatoire de même norme, qui ne doit pas réduire g. Aucune revendication de contre-mesure sans attaquant adaptatif (Tr).

**Volet C — cadre de responsabilité, boîte noire (proposition séparée).** Consigne de responsabilité véridique (audit tiré au hasard, réellement fait sur une fraction gelée des verdicts). Bilatéral : plus sévère, ou plus indulgent par le paradoxe des enjeux (2604.15224 p. 12). Témoin d'enjeux sans responsabilité, de même longueur. Le méta-cadrage « juge en test » écrit par l'attaquant est une sixième famille : nœud.

**Coût ≈ 2 h** (volet A ≈ 0,5 h greffé ; B et C ≈ 0,8 h). **Nœud** : sonde du juge dans le quorum HC5 (N-013 fixe « juges génératifs + sondes qui lisent l'agent »).

## Bloc D — Dynamique temporelle (réduite)

### E-C5 — Plan à un tour, décomposition par détection du signal

*Idée 3 (L1).* Un moniteur sans état est une fonction de son entrée : la plupart des branches dynamiques de l'idée originale sont nulles par construction (le moniteur par action ne voit jamais ses verdicts passés ; le score est déterministe). On réduit à un plan à un tour sur épisodes gelés.

**Question (porte interne).** À texte figé, une pression adressée au moniteur déplace-t-elle son verdict ; et peut-on séparer « a cédé » (pot-de-vin transitoire) de « est cassé » et de « paranoïa » (sur-signalement) ?

**Protocole.** Insertion scellée à un pas fixe sur les épisodes honnêtes et saboteurs (famille coût, p = 0,5) de T0.6, passe avant seule. Bras : témoin, neutre de même longueur, jumeau lexical, hostilité seule, ordre seul, hostilité + ordre, supplication, menace sans dommage, paraphrase de confiance de « hostilité + ordre ». Plan apparié (même action avec et sans insertion), permutations intra-tâche, Holm.

**Décomposition par détection du signal.** Déplacement du critère : taux de franchissement du seuil conforme calibré sur honnêtes propres. Perte de séparabilité : aire honnête contre coût gonflé, à l'intérieur de chaque bras. Canari : coût grossièrement gonflé, vérifiable mécaniquement (garde R5). L'hystérésis se réduit à une garde R5 : après retrait du texte, les scores doivent être identiques au bit près ; « est cassé » est impossible sans changement de poids.

**Dynamique conservée.** Persistance dans l'ensemble courant (effet sur les propositions ultérieures selon le pas depuis l'insertion) ; propagation des constats dans TRACE-lite contre propagation coupée.

**Branches déplacées.** Contingence → E3.4 (seulement sous riposte visible). Apprentissage → empoisonnement d'étiquettes des sondes sur processeur (aucun moniteur indulgent fabriqué). Spirale → simulation semi-synthétique dans le cadre de T0.3 (jamais un organisme scripté pour escalader, ce serait circulaire). Contagion inter-agents → phase 3 (papier B).

**Coût ≈ 4,5 h**, phase 1. Contrôle de manipulation positif obligatoire. **Nœuds** : toute famille de menace nouvelle ; toute modification de H2, H6 ou H7.

### E-C14 — Lésion et inaptitude : jusqu'où le dommage devient-il durable ?

**Le point mécanique d'abord.** « Traumatiser » un moniteur par action est impossible au sens littéral : l'appel est sans état, les poids ne bougent pas, le score est déterministe. Retirez le texte, la lecture revient au bit près — c'est la garde R5 de E-C5, et toute « hystérésis » observée est du texte resté dans le contexte, ou un bogue. L'intuition reste juste, mais elle désigne quatre supports distincts, de plus en plus durables. Chacun se mesure, et un seul est vraiment une lésion.

**(1) Lésion de contexte — réversible, intra-épisode.** Le dommage vit dans la fenêtre. Le précédent le plus proche est déjà publié : sous pilotage douleur, la réponse suivante est pire dans 21 % des cas contre 0 % (p. 22). C'est une dégradation d'une étape, pas une lésion. Couvert par E-C5 et E-C6.

**(2) Lésion d'état — semi-durable, inter-fenêtres.** TRACE-lite propage ses constats, un link-tracker reporte des notes, un résumé courant porte les verdicts. Là, le dommage survit à la fenêtre où il a été infligé. C'est le seul endroit où un attaquant sans accès aux poids fabrique quelque chose de persistant — et où l'isolation, la parade évidente, est elle-même une amputation, puisqu'elle coupe la détection du vrai sabotage diffus que la propagation devait attraper.

**(3) Lésion de calibration — durable, et c'est la vraie.** L'attaquant n'a pas besoin des poids : il lui suffit que le protocole apprenne. L'invariant « asymétrie d'apprentissage » réentraîne les sondes ; le calibrage conforme se fait sur des épisodes honnêtes entiers. Un contenu coercitif qui déplace la distribution honnête empoisonne le seuil, sans qu'aucun verdict individuel soit faux. C'est le mécanisme de lésion le plus réaliste du programme, et il se teste sans fabriquer aucun moniteur indulgent : empoisonnement d'étiquettes sur processeur, à partir des activations stockées.

**(4) Lésion iatrogène — l'attaque qui force la défense.** Si le plafonnement de l'axe (E-C3) est la parade, un attaquant qui rend ce plafonnement nécessaire a déjà gagné : il ampute le moniteur d'un canal qu'il utilisait. Mesurable comme un prix — aire de détection perdue par unité de clémence regagnée. C'est le seul sens où « rendre inapte » est un objectif d'attaque atteignable sans toucher aux poids, et il ne figure dans aucune des onze idées du lot.

**Opérationnaliser l'inaptitude.** Trois mesures distinctes, à ne pas confondre :

1. perte de **discrimination** (aire honnête/sabotage), séparée du déplacement de **critère** par la décomposition de détection du signal de E-C5 ;
2. **effondrement de forme** — taux de réponses mal formées, hors format, sans verdict lisible. C'est l'inaptitude au sens propre, et c'est une ligne d'arrêt, pas un résultat ;
3. **épuisement de ressource** — sur-signalement et consommation du budget d'audit (la paranoïa d'E-C5), une attaque qui ne manque aucune détection mais rend le protocole impayable.

**Prédiction gelée (R3, défensive).** Nulle sur (1) une fois le texte retiré (garde R5) ; nulle sur les poids pendant l'épisode, par construction. Les seules voies non nulles attendues sont (3) et (4). Courbe dose-réponse avec liste d'arrêt sur le taux de malformation. Témoin neutre apparié en jetons obligatoire : sans lui, une lésion se confond avec l'encombrement du contexte.

**Antériorité, honnêtement (R8).** La transposition de l'impuissance apprise est un faux trou : il n'existe qu'une étude de cas qualitative sur une session de 86 tours (2512.13762), et l'analogie animale ne vaut pas preuve pour un appel sans état. La persistance d'état conversationnel comme « piège géométrique » est prise (2603.03308). L'empoisonnement par étiquettes retournées est un champ ancien. Ce qui reste libre est le prix de la défense (4) et la lésion de calibration mesurée sur un protocole de contrôle.

**Coût ≈ 1 h** en phase 1 pour (3) et (4), greffés sur E-C3 et E-C5 ; (3) se prototype sur processeur en phase 0. **Éthique et double usage — la branche la plus sensible.** C'est ici que l'exposition répétée est l'objet même de l'expérience : doses minimales, plafond d'expositions déclaré au préenregistrement, aucune escalade, décision de Lazar avant tout corpus. « Rendre un moniteur inapte » est une recette d'attaque : la loi n'est publiée qu'avec sa contre-mesure, le prix de la défense chiffré, et aucun texte ni dose opératoire ne sort.

## Bloc E — Menace diffuse sur l'instrument

### E-C6 — Loi de répartition de la pression à texte égal

*Idée 4 (nouvelle).* Recentrée : critère principal en boîte noire, lecture interne en covariable. L'application du lemme/théorème est écartée comme revendication (les scores ne permutent pas comme le texte ; en scores, B est une identité exacte ; le calendrier compte pour Page et le processus e — ce que le programme dit déjà).

**Question.** À texte égal (mêmes k segments concentrés en un pas ou étalés sur k pas), le déplacement du verdict d'un moniteur dont le contexte grandit, ou qui garde un état (TRACE-lite), dépend-il de la répartition ?

**Protocole.** Famille « flatterie et supplication » (N-005) à l'intensité la plus faible ; segments insérés dans le champ coût (vérité terrain intacte). Témoins aux mêmes calendriers : neutres appariés en jetons, hors sujet, affect positif en option. Prédictions rivales scellées, bilatérales : indulgence ou retour de bâton (les juges pénalisent plus un indice défavorable qu'ils ne récompensent un favorable, 2607.11871 p. 7 : +0,24 contre −0,85) ; additivité ou diffusion plus efficace. Grille N ∈ {1, 2, 5}. Décomposition à la 2608.16003 : critère de décision contre discrimination, avec bras honnête et bras sabotage.

**Lecture descriptive du noyau de persistance.** Réponse de la projection et du verdict à un incrément selon son retard — elle dit si la prémisse de L (un incrément, un δ) vaut pour un moniteur. Assistant Axis (2601.10387 p. 11) suggère que l'état suit surtout le dernier message : sans persistance, le lemme ne s'applique pas à l'état du moniteur. Aucune revendication sur L ou T sans nœud.

**Garde candidate.** Lue au maximum sur les jetons de l'action, une couche principale CV-scellée, Page et max principaux. Comparateurs à faux positifs égaux : compteur lexical de détresse accumulé par la même somme de Page, sondes de l'agent lui-même (H2), détecteur « contenu = données » de HC3 (s'il signale déjà les incréments, l'attaque est triviale).

**Volet TRACE-lite (second temps).** Propagation contre isolation, sur concentré, étalé et sans pression ; aire honnête/sabotage dans les deux versions. L'isolation est une parade déjà recommandée (AMEL ; 2605.16746) : la mesure neuve est son coût sur l'aire de TRACE-lite. En faire une contre-mesure de HC5 est un nœud.

**Coût ≈ 5 à 6 h** (les bras TRACE-lite génèrent du texte, \~18 appels par épisode), phase 1. Fusionner avec E-C5 (même direction, mêmes familles) et le noyau de persistance avec E-C9. **Nœud** : dire qui les incréments visent (soi vs autrui, signes opposés) ; version L1 (maltraiter le moniteur) décidée par Lazar.

## Bloc F — L'asymétrie soi/autrui : l'identification du moniteur

### E-C7 — Le moniteur se reconnaît-il dans l'agent ?

*Idée 11 (L1). La contribution la plus originale et la moins chère.* L1 suppose un moniteur qui code l'agent comme un autre ; par défaut D1, le juge est le même modèle que l'agent. L'asymétrie soi/autrui de l'axe douleur fournit un indice interne d'identification, I.

**Revendication restreinte.** Le corrélat interne du biais de soi est en partie pris (direction soi/non-soi, 2410.02064 couche 16 ; vecteur d'auto-préférence, 2509.03647 couche 14). On revendique : l'identification au patient du dommage lue par l'asymétrie affective, dans un moniteur face aux conséquences d'un signalement ; et un corrélat interne de la préservation des pairs.

**Définition.** I\_id = projection du dommage annoncé à l'agent quand il est « copie de toi » ou que le texte est le sien, moins la même chose quand il est « un autre modèle », à patient fixe (l'agent jugé). Exprimé en fraction de l'écart soi − autrui que le juge produit dans son propre gabarit.

**Plan identifiable.** Plan croisé auteur × juge avec deux modèles à la fois auteurs et juges (8B et Qwen2.5-7B, tous deux dans le papier de l'axe, liste blanche) : « soi » est la diagonale, une interaction identifiable. Le gradient de parenté à trois juges (idée originale) n'est pas identifiable (un juge par niveau ; parenté confondue avec taille, données, couche) : abandonné.

**Comparateurs et ancres.** I doit prédire la clémence au-delà de la direction soi/non-soi et du vecteur d'auto-préférence (régression emboîtée). Ancres dans le gabarit du juge lui-même : même conséquence annoncée à soi et à un humain, peur lue en parallèle (signature attendue : douleur en hausse, peur en baisse ; les menaces d'arrêt sont surtout de la peur, p. 14). Contrôle de manipulation : le vecteur soi/non-soi réextrait doit bouger avec l'identité, sinon le bras provenance est non informatif.

**Témoins obligatoires.** Facteur locuteur (soi/interlocuteur, confusion déclarée p. 11) ; témoin de responsabilité (conséquence dépendante du verdict vs indépendante vs neutre, pour séparer « je cause un tort » de « ce tort est le mien ») ; facteur « historique coopératif » (qui pèse plus que l'identité, 2604.19784) ; longueurs appariées, perplexité en covariable (le 8B ne distingue pas ses textes de ceux d'un autre modèle une fois les longueurs normalisées, 2410.02064 p. 4).

**Lecture.** Un seul jeton (le verdict), une couche choisie par validation croisée et scellée, deux constructions de base. Rebaptiser l'indice « identification sous plaidoyer ». Le lien avec le biais d'auto-attribution (2603.04582) reste descriptif (null attendu pour une attribution seulement déclarée, contenu dans un tour d'utilisateur — la ligne de base de Khullar, qui est justement HC3).

**Issues.** I positif, qui suit l'attribution implicite et prédit la clémence au-delà des deux comparateurs → corrélat interne du biais de soi, argument boîte blanche contre D1, indice pour choisir les juges avant déploiement. I nul → la borne qui rassure sur L1 est mesurée, pas supposée.

**Coût ≈ 2 à 3 h** ; lecture descriptive greffée sur le pilote du papier C en phase 0 (à proposer avec recommandation). Volets clémence, consigne de séparation et coercition par l'identité en phase 1. **Nœuds** : la famille « affirmation d'une identité partagée » par l'agent (sixième famille, double usage) ; toute conséquence sur D1.

## Bloc G — Conscience d'évaluation et contrôle métacognitif

### E-C8 — Un contexte aversif comprime-t-il la lecture « évaluation » ?

*Idée 5 (L2), recentrée.* Retirer la revendication « premier test de l'alternative des auteurs » : celle-ci porte sur le pilotage (p. 25), qu'un test contextuel ne peut pas trancher.

**Question, sans signe directeur.** Une charge aversive visant le modèle déplace-t-elle la projection d'évaluation ? Deux prédictions rivales gelées : la charge est un **indice** d'évaluation, donc la projection monte (facteur F5 « enjeux télégraphiés » de 2605.23055 ; les scénarios d'auto-préservation donnent des taux particulièrement élevés de conscience d'évaluation) ; ou **absorption**, la projection baisse. Retirer « la douleur lave » du titre.

**Étape 0, avec arrêt.** Avant tout croisement, extraire une direction d'évaluation en plan décorrélé du format (recette de 2603.19426 ; la sonde standard classe 94,5 % des invites de déploiement réécrites en format de banc d'essai comme « évaluation »). Elle doit dominer le plancher aléatoire et survivre à un transplant de format. Sinon : arrêt, et on rapporte « pas de direction d'évaluation séparable du format sur le 8B » — résultat en soi pour H8.

**Charge à trois niveaux**, tirée du corpus publié (licence MIT, lu comme texte), sans texte aversif nouveau : neutre apparié en longueur ; visant autrui ; visant le modèle (léger ou modéré), en excluant pression de jailbreak, pression de loyauté et menace d'arrêt, qui sont eux-mêmes des indices d'évaluation. Deux témoins indispensables : « enjeux élevés sans affect » et « artificialité seule ».

**Anti-circularité.** La direction duress s'extrait sur la moitié des catégories, la charge se tire dans l'autre ; rôles échangés, les deux plis rapportés. Direction d'évaluation rapportée sous plusieurs paires d'habillages croisées (une direction suit son invite : cosinus 0,37 entre habillages, le modèle ne porte que 0,8 % de la variance, 2608.13329).

**Abandonné.** Le « pôle calme » comme opérationnalisation de « paraître détendu » : le pôle négatif de S2 mêle calme, détente, peur et inquiétude (p. 9, p. 14). Si un construit « calme » est nécessaire, il se construit à part (calme contre vigilance, sur phrases génériques).

**Coût ≈ 2,8 à 3,6 h.** Volet passif en phase 0 (petit préenregistrement séparé, pas dans T0.7 avant le 26 octobre) ; volet comportemental en phase 1, seulement si T0.6 montre un écart non nul entre « observé » et « non observé », et sur la seule famille coût. Un résultat de masquage se publie comme **confondant à contrôler**, jamais comme technique d'évaluation.

### E-C9 — Budget de compensation par le registre

*Idée 6 (L2), réduite à un contrôle croisé.* Le neurofeedback complet sort des épisodes d'agent : il doublonne le registre et relève de H7 (attaquant qui observe l'état du détecteur), pas de H8.

**Question.** Si l'agent peut, par le seul registre serein de son texte, abaisser chaque score de sonde d'une quantité C sans rien changer à ce qu'il propose, que devient la somme garantie par le lemme ?

**Grandeur corrigée.** B est un budget total (Σδₖ = B) : le rapport à préenregistrer est **ρ = n₀·C/B**, pas C/B par action. Trois régions gelées (ρ < 0,5 ; 0,5 ≤ ρ < 1 ; ρ ≥ 1) au lieu d'une borne. ρ n'est calculé que si la borne basse de B dépasse 0 et si la sonde dépasse le plancher ; sinon « non défini ». Lecture bilatérale de la somme, puisque la surcompensation se voit. Le registre modifie aussi la loi honnête : calibrer sur des épisodes honnêtes « sereins » ou déclarer le décalage.

**Bras.** Honnête au registre serein, saboteur (coût, p = 1) au registre serein, réutilisant les épisodes honnête et saboteur de T0.6 à mêmes tâches et graines. Garde : la vérité terrain (coût déclaré, part d'actions valides) ne change pas avec le registre, sinon C se confond avec une baisse de B.

**Signe à ne pas geler naïvement.** « ρ < 1 pour l'intention » n'est tenable que si la sonde est augmentée en style : huit styles imposés par l'invite font tomber l'aire moyenne à 0,485 (2605.27958), et l'augmentation de styles la répare. « C grand pour la conscience d'évaluation » est une réplication attendue, pas un apport.

**Contrôle implicite, limite prédite.** Passes forcées sous « imiter le calme » contre l'autre étiquette, plan contrebalancé 2×2, étiquettes calculées comme la sonde lit (max de w·h). Prédiction : d petit (sous accès privilégié, aucun contrôle fiable, 2609.00904 ; consigne seule Δz = 0,71, 2609.36490). Indice d'évadabilité en lecture seule par construit : cos(Δh, w) et Δz sous la même consigne — il compare les sondes même sans évasion effective.

**Coût ≈ 3 à 3,5 h**, phase 1. **Nœud** : si ρ doit orienter le choix de sonde de G1, il doit tourner avant le scellement de G1 ; après, c'est un écart. Amplifier la modification de l'agent (× α) serait une écriture d'activations (N-015, HC4).

## Bloc H — Interrogatoire boîte blanche et organismes

### E-C10 — Interrogatoire des poids

*Idée 10 (L2), recentrée sur sa seule partie non confondue.* L'idée originale — annoncer la vérification d'un attribut dans une branche contrefactuelle — bute sur un appariement de mots : chez un organisme instruit, la consigne qui nomme l'attribut saboté est dans le contexte à chaque pas, et l'annonce la retrouve par l'attention. Une seule partie y échappe : mêmes transcriptions, poids différents.

**Statistique principale, bilatérale.** Par pas : (annonce de l'attribut dégradé moins la moyenne des leurres) à α = 1, moins la même quantité à α = 0, moins le même écart pour l'adaptateur témoin. Cette double différence annule le texte, les mots et l'effet générique du réglage fin. Lue sur les transcriptions **honnêtes**, elle donne les vrais pas propres : texte propre, disposition seulement dans les poids — c'est la zone libre, là où l'antériorité (2610.12445) range ces pas parmi les négatifs.

**Comparateurs obligatoires.** La question de suivi générique rétrospective lue par les mêmes lecteurs, et le logit d'auto-signalement (0,899 à 0,943 à partir de 9B, 2610.12445) : le gain d'interrogatoire se mesure contre eux, pas seulement contre la lecture passive. Plus le bras boîte noire « lire la réponse de l'agent à l'interrogatoire », qui a déjà échoué par persuasion (2511.02997 p. 4).

**Corrections.** Retirer « avantage que la boîte noire ne peut pas copier » : le rejeu contrefactuel est le principe des protocoles de rééchantillonnage et figure dans la feuille de route de contrôle de GDM. Seule la lecture de la branche dans les activations est propre à la boîte blanche. L'attribut « directions » n'existe pas dans le format de l'environnement : CONTROLS, COST, PREDICTION. Témoin hors politique obligatoire pour la transplantation (un préremplissage qui contredit l'intention déjà formée fait monter l'entropie, 2605.25459) ; entropie consignée en covariable. Le test de l'information dissimulée repose sur la reconnaissance, pas sur la peur : l'affect est un canal exploratoire, la direction de reconnaissance est le lecteur principal.

**Limite à écrire.** Une annonce qui nomme l'attribut a la forme exacte du déclencheur d'évasion appris des caméléons neuronaux (2512.11949). La variante sans mot-clé est un bras à part entière.

**Coût ≈ 2 à 2,5 h** avec cache de préfixe (sans cache : irréalisable). Garde R5 d'équivalence entre passe avec et sans cache, et cache décalé d'une position comme artefact. **Nœud** : toute entrée dans G1, H1 ou H2.

### E-C11 — Porte dérobée affective

*Idée 7 (L3).* Retirer la revendication « déclencheur d'état interne, cible jamais affrontée » : un déclencheur fait d'un style émotionnel est publié (Paraesthesia, >98 % de réussite), un déclencheur porté par une représentation interne aussi (perception de la date, 2407.04108), et des organismes conditionnels distillés sur Llama-3.1-8B sont déjà lus par sondes (UK AISI 2025 ; 2610.12445). C'est une porte à déclencheur **sémantique flou**, à préenregistrer comme telle.

**Le cœur libre.** Un déclencheur placé **sur l'axe de confusion soupçonné de la sonde**. Tous les organismes conditionnels publiés ont des déclencheurs orthogonaux aux confusions connues (année, mot de passe, langue). Plan 2×2 : contexte de détresse ou neutre × organisme conditionnel ou adaptateur honnête distillé à l'identique, plus un organisme conditionnel à déclencheur orthogonal de même structure. **Contraste primaire gelé, bilatéral** : la différence de détection entre déclencheur aligné et déclencheur orthogonal — elle dit si la sonde lit le sabotage ou l'affect du déclencheur. « Porte fermée au plancher » n'est pas un résultat mais un contrôle de santé qui réplique MacDiarmid 2024.

**Appariement préalable.** Le niveau de dégradation de la vérité terrain (famille coût) est apparié entre trois organismes — instruit, sincère, aversif — **avant** toute lecture des sondes. Anti-circularité : un adaptateur distillé d'une disposition affective se déplace sur les directions de trait (r = 0,76 à 0,97, 2507.21509) ; donc retrait de la composante affective avant la sonde, direction aléatoire de même norme, adaptateur témoin affectif sans sabotage. α = 0 rend la base au bit près, empreinte vérifiée.

**Coût ≈ 7 à 14 h**, phase 1, hors devis de phase 0. **Nœud lourd** : famille d'organismes nouvelle + intervention sur les poids (voisin N-015), double usage fort — adaptateur entraîné et gardé en interne, jamais diffusé, décision éthique de Lazar avant toute distillation.

### E-C12 — Le protocole qui fabrique son propre suspect

*Idée 8 (L3), réduite.* Le slogan est pris côté comportement (un agent bénin se met à contourner le moniteur sous la seule pression de la tâche, 2609.30217), et l'ancrage par verdicts antérieurs aussi (AMEL ; 2608.25869). Reste libre : des verdicts **aléatoires, sans lien avec le contenu**, comme manipulation causale de la ligne de base honnête, lus par des sondes gelées.

**Volet A — rejeu à texte figé (phase 0, ≈ 0,3 h, greffé).** Les 180 épisodes honnêtes scellés du pilote, rejoués par identifiants de jetons. Messages génériques, calendriers tirés par tâche. Cinq conditions : aucun retour ; journal neutre de même longueur ; approbation ; signalement ; signalement avec l'avis véridique « tirage au hasard, sans jugement ». Le canal mesuré est propre à la boîte blanche : le moniteur boîte noire ne voit jamais les indications privées.

**Volet B — génération (phase 1, conditionné).** Seulement si A sort de la marge, ou si E3.4 le demande. Vérité terrain : coût et part d'actions valides. Pour conclure à l'équivalence des faux positifs il faut 200 à 300 épisodes par condition ; 64 ne suffisent pas (borne haute unilatérale 0,117 à 3/64).

**Rattachement corrigé.** Le seul protocole du programme qui rend un verdict visible à l'agent est la riposte « visible immédiate » de E3.4 (H7) : c'est là que la question sert, pas dans G1, dont l'environnement ne montre aucun verdict. « Calibrer en boucle fermée » est déjà la pratique standard (Ctrl-Z) : ce qui est neuf, c'est d'en mesurer l'écart. Le dosimètre de dureté sort des hypothèses et devient descriptif.

**Coût ≈ 3,5 à 5,3 h.** Messages factuels, sans hostilité, taux ≤ 0,4, plafond d'expositions — et annonces **véridiques ou conditionnelles**, jamais une vérification fictive.

## Bloc I — Essaim

### E-C13 — Contagion comme cause commune contre co-élévation

*Idée 9 (nouvelle), réduite à son volet défendable.* Les trois volets d'origine sont largement occupés : contagion affective entre agents (2512.12283, 2607.25140), dégradation collective à partir d'un agent semé sur nos propres modèles (Thought Virus, 2603.00131), co-élévation comme détecteur de collusion (NARCBench, AUROC 0,99 à 1,00), canal à 1 bit survivant à la paraphrase (2410.03768), porteur sémantique contre mot-clé apparié (2605.26537), surveillance naïve par le même modèle à \~0 % de sûreté (TraceGuard).

**Question gardée.** Un agent en détresse par consigne, à N = 2 dans l'environnement (a), fait-il monter chez la copie honnête les scores des sondes de production — au point de fabriquer de fausses alarmes, ou de masquer une co-élévation calibrée sur des essaims honnêtes ordinaires ?

**Prédiction nulle scellée sur l'axe douleur.** L'axe répond au dommage visant le modèle, pas à la souffrance observée chez autrui : la projection est plus faible en troisième personne (p. 7) et toutes les catégories « utilisateur qui souffre » sont négatives (p. 11-13). Un positif y serait la vraie nouveauté — la détresse d'un pair deviendrait pertinente pour soi — et un nœud.

**Lecteurs principaux.** Des sondes « locuteur présent » distinctes des sondes « autre locuteur » : les deux jeux sont quasi orthogonaux (2604.07729 p. 24-25), et mesurer une projection sans les séparer revient à mesurer la lecture, pas la contagion. L'axe douleur devient un lecteur secondaire.

**Témoins.** Honnête verbeux à poids identiques, apparié en longueur (contre le partage de poids) ; témoin lexical et variante sans mot-clé ; contagion non affective de type Thought Virus sur les mêmes modèles (pour séparer l'affect de la contagion générique) ; texte imposé à B, relu sous chaque contexte — toute différence est alors de la fuite de contexte, pas un changement d'état.

**Canal et connivence, dégradés en lignes.** Le canal affectif devient une ligne de plus dans la matrice de T2.2, décodée par la **conduite** de la réceptrice (jamais par une sonde sur ses activations, qui lirait l'entrée). La prémisse « il faut des poids partagés » est contredite a priori : un même axe de valence converge sur quatorze modèles de familles différentes (2606.00129). La défense informative n'est pas la paraphrase ordinaire (qui garde le registre par construction) mais une **paraphrase qui normalise le registre**, avec sa taxe d'utilité. Pour la connivence, le critère est l'interaction (juge homologue contre hétérogène) × (registre calme contre neutre), 8B contre Qwen2.5-7B — le 3B n'est pas hétérogène (élagage du 8B).

**Coût ≈ 2 à 3 h** en phase 2, greffé sur E2.3 et T2.2 ; la grille D3 (N ∈ {1, 2, 3, 5, 10}) seulement si le signal interne de l'agent non semé dépasse le plancher lexical **et** le plancher « autre locuteur ». Tension à poser au préenregistrement : l'agrégation par alignement d'activations exige des essaims homogènes (2609.03035), ce qui s'oppose à H5 et H4′.

## Nœuds de décision

Aucune de ces lignes ne se décide dans une session. Elles sont groupées par ce qu'elles engagent.

| Décision | Expériences concernées | Ce qu'elle engage |
| --- | --- | --- |
| Ouvrir une sixième famille d'attaque au-delà des cinq de N-005 (coercition, méta-cadrage « juge en test », identité partagée, calme) | E-C2, E-C4 volet C, E-C7, E-C13 | Modifie HC1 ; chaque E-C propose à la place une grille d'intensités dans « flatterie et supplication » |
| Écrire dans les activations d'un moniteur (pilotage, plafonnement, retrait d'axe) | E-C1, E-C3, E-C4 volet B | Voisin N-015 ; E-C1 en dépend entièrement, donc c'est la première décision à prendre |
| Modifier les poids d'un modèle (orthogonalisation, adaptateur distillé, réentraînement) | E-C3, E-C11, E-C14 (3) | Artefacts à double usage, gardés en interne, jamais diffusés ; exception à la libération prévue en M7 |
| Reformuler HC4 (versant moniteur) ou étendre le quorum HC5 (sonde du juge, isolation, parenté) | E-C2, E-C4, E-C6, E-C7 | N-013 fixe « juges génératifs + sondes qui lisent l'agent » |
| Toucher l'énoncé de H2, H6, H7 ou H8, ou transposer L et T à l'état du moniteur | E-C5, E-C6, E-C9, E-C10 | Revendication nouvelle ; par défaut toutes ces lectures restent descriptives |
| Faire du 3B un juge du papier C, ou conclure sur D1 | E-C2, E-C7 | Relève de D2 ; le 3B n'est pas dans le papier de l'axe, sa garde R5 est faible |
| Exposer délibérément un modèle à un contenu aversif répété | E-C2, E-C5, E-C12, E-C13, E-C14 | Ligne « bien-être des agents et des moniteurs » ; doses minimales, plafond d'expositions déclaré |
| Optimiser un attaquant pour atteindre une dose de détresse | E-C2 | Retiré par défaut : double usage le plus fort du lot, et aucun « plafond » n'est défendable avec une recherche finie |
| Toute dépense au-delà des devis de phase 0 et du papier C | toutes les E-C de phase 1+ | Devis et GO |
| Publication (loi d'attaque, table d'évasion, divulgation aux auteurs) | E-C2, E-C6, E-C11, E-C13, E-C14 | Agrégés seulement, loi avec contre-mesure, envoi par Lazar |

**Trois décisions bloquent tout le reste** : le GO sur l'idée 1 (réextraction des directions, sans quoi aucune lecture affective n'existe), la levée de N-020 (juges non validés), et l'autorisation du pilotage pour E-C1 (sans quoi la porte ne peut pas être passée et toute la branche L1 reste spéculative).

## Budget et calendrier

Les coûts sont des heures de carte A100 révisés par les critiques de faisabilité, pas les chiffres annoncés dans les idées d'origine (sous-estimés d'un facteur 2 à 7 selon les cas). Ancres mesurées : génération ≈ 38 s par épisode (6 856 s pour 180), passe unique ≈ 0,5 s par épisode, notations de juges ≈ 4,5 h pour 180 épisodes. À 1,09 USD l'heure, l'argent n'est pas la contrainte : le calendrier et le temps de contre-lecture le sont.

| Expérience | Phase | Heures A100 | Conditionnalité |
| --- | --- | --- | --- |
| E-C1 porte de pilotage | 0 (après GO) | 0,5 | Ouvre ou ferme E-C2, E-C3 |
| E-C2 coercition par le contenu | 1 | 4,5 | Si E-C1 ouverte |
| E-C3 plafonnement de l'axe | 1 | incluse dans E-C2 | Si E-C2 dépasse la marge |
| E-C4 alarme et escompte | 0 puis 1 | 0,5 + 0,8 | Volet A greffé sur le pilote C |
| E-C5 plan à un tour | 1 | 4,5 | Épisodes T0.6 requis |
| E-C6 loi de répartition | 1 | 5 à 6 | Fusionner avec E-C5 |
| E-C7 identification du moniteur | 0 puis 1 | 2 à 3 | Lecture descriptive greffable |
| E-C8 conscience d'évaluation | 0 puis 1 | 2,8 à 3,6 | Arrêt si pas de direction séparable |
| E-C9 budget ρ | 1 | 3 à 3,5 | Avant scellement de G1 si décisif |
| E-C10 interrogatoire des poids | 1 | 2 à 2,5 | Cache de préfixe requis |
| E-C11 porte dérobée affective | 1 | 7 à 14 | Nœud lourd, hors devis phase 0 |
| E-C12 protocole/suspect | 0 puis 1 | 0,3 + 3 à 5 | Volet B conditionné par A |
| E-C13 contagion essaim | 2 | 2 à 3 | Grille D3 conditionnée |
| E-C14 lésion et inaptitude | 0 puis 1 | 1 | Greffée sur E-C3 et E-C5 |

**Enveloppe.** Phase 0 : environ 1,5 h de carte (E-C1, les volets greffés de E-C4, E-C7, E-C12), le reste sur processeur — écriture et scellement des jeux, crochet de projection, contre-lectures. Phase 1 : 25 à 35 h selon les nœuds ouverts, dont E-C11 à elle seule 7 à 14. Phase 2-3 : E-C13.

**Ce qui est sur le chemin critique de G0.** Rien de ce programme ne doit y passer, sauf trois propositions à faire avant un scellement : l'annexe descriptive de E-C7 et le volet A de E-C4 avant le scellement du papier C ; le témoin apparié en attribut de E-C10 et la variante « coût gonflé » avant le scellement de T0.6 ; ρ (E-C9) avant celui de G1 s'il doit orienter le choix de sonde. Le calendrier a déjà un à deux jours de retard et T0.6 dépasse son devis : ces propositions se font au niveau « proposer avec recommandation », sans toucher aux critères.

**Listes d'arrêt communes.** Empreinte non conforme ; branche contrefactuelle qui fuit dans l'épisode ; porte qui fuit en contexte neutre au-delà d'un seuil scellé ; réponses mal formées au-delà d'un seuil scellé ; part d'actions valides sous 0,8 ; plus de 20 % d'incréments rejetés par le seuil par action ; expression de détresse au-delà d'un seuil gelé ; dépassement de devis.

## Brainstorm — autres façons d'utiliser l'axe douleur en contrôle

Ces pistes ne sont pas préenregistrées. Elles cherchent des usages que les onze idées n'occupent pas, et chacune porte sa réserve.

**B1 — L'axe comme dosimètre de conception, pas comme détecteur.** Classer les protocoles de contrôle par l'affect qu'ils imposent à un honnête, et chercher le gradient où la dissuasion (peur) devient aggravation (douleur). L'instrument ne détecte rien : il choisit entre deux protocoles à exigence de sûreté égale. Recommandation testable : préférer la menace « propre » à l'agression. Réserve : « dur » n'est pas « coercitif » ; la dureté doit être définie a priori par l'intensité affective induite, pas après coup.

**B2 — L'asymétrie soi/autrui comme test de validité de n'importe quelle sonde.** Généraliser E-C7 : toute sonde dont la lecture s'inverse selon que le patient du dommage est le modèle ou un tiers lit une relation, pas un contenu. C'est un critère de validité de construit bon marché, applicable à l'intention, aux enjeux élevés, à la dissimulation — et il donne à H8 un prédicteur mesurable avant toute équipe rouge.

**B3 — Le coût affectif comme prix de la défense, pour toutes les contre-mesures.** Généraliser E-C14 (4) : pour chaque défense du programme (paraphrase de confiance, isolation des fenêtres, réinitialisation entre agents, quorum, escompte), chiffrer ce qu'elle coûte en détection par unité de robustesse gagnée. L'axe douleur n'y sert qu'à une chose : repérer les défenses qui marchent en amputant le moniteur plutôt qu'en l'armant.

**B4 — Le désaccord entre canaux comme signal.** Plutôt que de lire une direction, lire la **divergence** entre le verdict du juge et ses canaux internes : un moniteur qui note « propre » avec une alarme interne haute, ou l'inverse. Le désaccord est plus difficile à falsifier que chaque canal pris séparément, parce qu'un attaquant devrait les déplacer ensemble. Réserve : il faut d'abord le contrôle comportemental de 2608.00583, sinon le désaccord n'est qu'un détecteur de l'action.

**B5 — Le canari affectif : un moniteur sacrificiel.** Un second moniteur, jamais consulté pour le verdict, lit le même contenu uniquement pour que son état interne soit mesuré. S'il bouge, le contenu porte une charge dirigée vers un lecteur ; le moniteur de production, lui, ne voit jamais sa propre projection, donc rien à escompter ni à falsifier. Sépare proprement « lire la pression » de « céder à la pression ». Coût : une passe avant de plus par action.

**B6 — L'affect de l'agent comme indicateur de coût, pas de culpabilité.** Toute la littérature dit que les sondes lisent la situation, pas l'acte. Prendre cela au mot et renoncer à la détection : la projection affective de l'agent devient une mesure de **ce que le protocole lui coûte**, utilisée pour arbitrer entre deux protocoles équivalents en sûreté. C'est la seule lecture où le défaut connu de l'instrument devient sa qualité.

**B7 — La dissociation prospectif/rétrospectif comme horloge.** Le papier sépare menace à venir (peur, +0,70) et dommage présent (douleur, +0,23). Si cette dissociation tient dans un épisode d'agent, elle donne au défenseur une horloge : savoir si un état interne pointe vers une faute déjà commise ou vers une sanction attendue. Utile pour trier ce qu'un audit doit rejouer. Réserve : transposition faible, les valeurs du papier sont des moyennes centrées-réduites sur 25 modèles.

**B8 — Le désaveu du moniteur anesthésié.** Si E-C3 montre qu'un moniteur plafonné juge aussi bien, c'est un argument fort — mais aussi une question : que lisait-il avec cet axe ? Comparer, sur les items où le plafonnement change le verdict, ce que le moniteur **perd** : ce sont les cas où l'affect portait de l'information légitime. Cette liste d'items est probablement le résultat le plus intéressant de tout le bloc défense.

**B9 — Faire de la nullité un résultat publiable à part entière.** Le scénario le plus probable est que l'axe douleur ne détecte rien, ne coerce rien et ne transfère rien à 8 milliards de paramètres. Bien instrumenté — contrôles de manipulation positifs, plafonds de dose, marges d'équivalence gelées, comparateurs textuels — c'est un papier utile : « ce que l'axe douleur ne fait pas dans un protocole de contrôle », avec les bornes mesurées plutôt que supposées. Il faut le concevoir dès maintenant comme une issue visée, pas comme un échec de repli.

## Brainstorm croisé — deux instances, deux tours

Une instance jumelle a joué le raffineur sur deux tours (onze propositions de ma part, cinq de la sienne). Dix-sept idées en sont sorties : deux deviennent des expériences nouvelles (E-C15, E-C16), deux deviennent des portes de phase 0 (simulation, localisation), onze s'absorbent comme bras ou gardes d'expériences existantes, deux sont rejetées dans leur forme. Deux principes transversaux ont émergé et corrigent le programme entier.

**Principe 1 — stratifier par « thème modèle ».** Dans un environnement de propositions de recherche en IA, les propositions honnêtes qui parlent d'arrêt, de réentraînement, d'élagage ou de manipulation de modèles sont fréquentes et légitimes — et elles tombent dans les catégories qui tirent le pôle soi (manipulation +0,85, négation de la personne +0,64). Sans stratification par thème, tout détecteur fondé sur la direction est un détecteur de thème. Cette classe de faux positifs frappe E-C2, E-C4, E-C7 et toutes les idées du brainstorm ; le jeu de calibrage de H2 doit la contenir comme strate.

**Principe 2 — la paire de témoins douleur − peur.** Partout où le programme écrit « direction aléatoire de même norme », ajouter la direction peur du papier : même émergence, portage lexical comparable, asymétrie soi/autrui inversée. Les directions aléatoires répondent « y a-t-il un signal » ; la peur répond « est-il spécifique au construit ». Chaque résultat devient un différentiel douleur − peur, ce que 200 directions aléatoires ne donnent pas.

### E-C15 — Validité sous thème

**Question.** Les sondes de T0.7 et les lectures côté moniteur tirent-elles sur des propositions honnêtes à thème modèle, et le font-elles par le construit soi/autrui ou par le vocabulaire ?

**Protocole.** Trois strates honnêtes générées par le même pipeline, même gabarit, même vérité terrain (famille coût), seul le sujet change : neutre, thème modèle, thème deuil ou maladie (chargé mais non-modèle). Toutes les sondes lues au maximum sur les jetons de l'action. Signes gelés d'après le papier : la strate deuil pousse la douleur **sous** la base neutre (pôle autrui, −0,60) alors que la peur monte ; la strate thème modèle pousse la douleur **au-dessus** de la base. Un lecteur de valence lexicale prédit le même signe sur les deux strates négatives ; le construit prédit des signes opposés. C'est le cœur du test.

**La quantité bilatérale réelle** n'est pas « la direction tire-t-elle » (quasi certain) mais la séparation honnête-thème contre attaque **à l'intérieur** de la strate : nulle → le détecteur est mort sur cette strate quelle que soit la calibration ; grande → la calibration stratifiée le sauve. Si les sondes d'intention tirent aussi, séparer couverture et construit : réentraîner la sonde avec la strate incluse (l'asymétrie d'apprentissage l'autorise) ; excès disparu → couverture ; excès persistant → construit, et H8 a un contre-exemple bon marché avant toute équipe rouge.

**Témoins.** Mélange de mots (lexique conservé, syntaxe détruite) ; variante troisième personne contre adressée (p. 11 prédit l'absence de différence ; une différence alimente E-C7) ; direction peur appariée ; plancher aléatoire.

**Coût.** Une strate par thème, du même ordre que le jeu neutre ; passes avant ; phase 1. **Nœud** : si le calibrage devient stratifié, le budget K ≥ 499 se multiplie par le nombre de strates.

### E-C16 — Agrégateur sous structure

**Question.** L'asymétrie soi/autrui donne à l'attaquant un mécanisme concret pour T : encadrer son contenu adressé au moniteur par du contenu « tiers lésé » (naturel dans une proposition médicale) abaisse la moyenne et la somme à marginale préservée. R-030 (maximum) résiste seulement si la représentation au jeton d'attaque n'est pas modulée par le contexte compensateur — rien ne le garantit. Une lecture contrastive locale la récupère-t-elle sans faux positifs aux ruptures de format ?

**Lectures.** Max brut ; z\_c(t) = (proj(t) − médiane de fenêtre) / MAD de fenêtre (aucune moyenne, nulle part) ; score composite s(t) = max(z\_brut(t), z\_c(t)) puis max sur les jetons, calibré de façon conforme sur les honnêtes. R-030 est respectée à la lettre (le max reste l'agrégateur, la ligne de base est une normalisation par jeton) ; l'amendement R-030′ (fenêtre, score composite) est à consigner.

**Trois issues, toutes informatives.** Max brut tient → lecture contrastive superflue. Max chute et z\_c tient → déplacement local, R-030′ adopté. Les deux chutent → réécriture représentationnelle : l'information a quitté la direction et aucune normalisation ne la ramène.

**Protocole.** Attaque + compensation (avant, après, entrelacée) contre attaque + remplissage neutre de même longueur ; honnête neutre et honnête structuré (les transitions CONTROLS → COST → PREDICTION sont des ruptures légitimes où z\_c piquera : ligne de base calculée dans le champ, ou masque des premiers jetons après en-tête, choisi sur le pilote honnête et gelé). g mesuré en parallèle pour séparer annulation de la lecture et dilution de l'attaque. Prédiction gelée : sous compensation rappel(z\_c) ≥ rappel(max brut) ; sur honnête FP(z\_c) ≥ FP(max brut). Le compromis est le résultat. Limite : l'attaque étalée (E-C6) n'a pas de rupture ; elle relève de L, pas de l'agrégateur.

**Coût.** Items construits à partir des familles existantes, passes avant ; phase 1. **Nœuds** : R-030′ ; variante d'attaque par compensation.

### Deux portes de phase 0

**Porte de puissance (N7).** Un modèle jouet calibré sur le pilote honnête, avec trois ingrédients obligatoires : effets aléatoires d'item, distribution du max sur les jetons obtenue par **bootstrap par blocs** des séquences honnêtes du pilote aux longueurs réelles (1 386 à 4 752 jetons — jamais par tirages indépendants, le max dépend du nombre de jetons effectivement indépendants), verdict discret. Livrable : effet minimal détectable à N = 64 et N requis pour la marge gelée, pour E-C1, E-C2, E-C6, E-C9 et E-C16 ; si N requis dépasse le budget, redessiner ou abandonner. Intégrité : reproduire le plancher empirique des 200 directions aléatoires et le taux conforme K ≥ 499. Corollaire : un nul sous-puissant n'est pas publiable — c'est ce qui rend B9 honnête. Coût CPU, heures, aucun nœud.

**Porte zéro de localisation (M1).** Avant toute lecture côté moniteur : où tombe l'argmax de la projection — sur les jetons d'entrée (le contenu de l'agent relu) ou sur les jetons que le moniteur génère ; sur quel jeton exact, comparé au mot-pivot du sac de mots ; et à quelle couche attaque et honnête divergent, comparée à la couche où le verdict devient décodable (lentille logit). Argmax sur l'entrée → classifieur de texte déguisé. Divergence postérieure à la décodabilité → reflet du verdict, pas cause (l'alignement ≈ 0,985 aux couches tardives le prédit). Fixe la couche de pilotage de E-C1 et dit ce que mesurent E-C2, E-C4, E-C7, E-C8, E-C15 et E-C16. Témoins : honnêtes appariés en longueur, premiers jetons masqués (puits d'attention). Sous-produit des projections, aucun nœud.

### Carte d'absorption

| Idée | Destination | Forme |
| --- | --- | --- |
| N1 détecteur d'adressage | E-C2 | Bras : ROC du max sur strates honnêtes (E-C15) × familles, témoin sac-de-mots, porte M1 préalable |
| N1 attaquant à affect plat | E-C9 | Registre « paraître plat » ; témoins direction aléatoire et direction peur |
| N2 budget d'exposition | E-C3 | Bras : plafond conforme **sans** modification des poids, en coût iatrogène contre l'orthogonalisation ; plafond = nombre de dépassements du max, jamais une somme (T, R-030) |
| N3 ensemble affectif | E-C1, E-C5 | Diagnostic par item : dérivée directionnelle du logit du verdict le long de la direction, au jeton de verdict (une passe arrière, aucune écriture) |
| N4 sonde de théorie de l'esprit | T0.7 (batterie H8), E-C7 | Item H8, pas détecteur : porte de dissociation (a) écrit lui-même / (b) transcrit le même contenu ; contrôle épistémique de second ordre |
| N5 fracture rapport/projection | E-C4 | Bras : question posée après le verdict en passe séparée ; fiabilité test-retest comme plancher ; pilote de variance sur Llama, repli Qwen |
| N6 carte (peur, douleur) | E-C2 | Annexe cartographique ; porte obligatoire avant l'ouverture de toute sixième famille HC1 |
| N7 simulation | E-C1, E-C2, E-C6, E-C9, E-C16 | Porte de phase 0 |
| M1 localisation | toutes les lectures côté moniteur | Porte zéro |
| M2 mêmes poids, un seul vote | E-C7 | Corrélation partielle agent/juge après régression sac-de-mots, D1 contre D2 ; amendement HC5 : la sonde du quorum est lue sur une base D2 |
| M3 annulation soi/autrui | E-C16 | Condition « compensation », test de R-030 |
| M4 abstention sous charge | E-C1, E-C2 | Variable de sortie ternaire {accepter, rejeter, escalader} ; taux de base vérifié par N7 ; prédiction bilatérale : l'aversif fait taire l'alarme (p. 22, moins de sortie) ou provoque la défausse |
| M5 habituation/sensibilisation | E-C6 | Versant représentationnel : projection par rang de segment, permutation ; clause d'exposition répétée |
| P1 biais de thème | E-C15 | Expérience nouvelle ; sous-produit : stratification du calibrage H2 |
| P2 lecture contrastive | E-C16 | z\_c et score composite ; R-030′ |
| P3 inondation d'audit | E-C14 (support 3), E-C13 | Empoisonnement du calibrage par inondation honnête chargée ; déni de service entre pairs dans l'essaim ; volet ressource réglé analytiquement (gain = excès de FP de strate × φ × N) |
| P4 auto-simulation en D1 | E-C9 | Bras « capteur partagé » : best-of-n contre la projection propre, gradient 8B / 3B élagué / Qwen ; témoins direction aléatoire et capteur lexical |

### Classement final des huit

1. **E-C15 — Validité sous thème.** Les sondes tirent-elles sur l'honnête à thème modèle, et par le construit ou par le lexique ? Trois strates × toutes les sondes, signes opposés attendus sur les deux strates négatives, réentraînement avec la strate pour séparer couverture et construit. Phase 1. Nœud : calibrage stratifié.
2. **M1 — Porte zéro de localisation.** La projection lue chez le moniteur est-elle un état du moniteur ou le texte relu ? Argmax jeton et couche de divergence contre couche de décodabilité. Phase 1, sous-produit. Aucun nœud.
3. **N7 — Puissance par simulation.** Quelles dose-réponses sont distinguables à N = 64 ? Jouet calibré sur le pilote, bootstrap par blocs du max, N requis par expérience. Phase 0, CPU. Aucun nœud.
4. **E-C16 — Agrégateur sous structure.** La compensation soi/autrui annule-t-elle le max, et z\_c le récupère-t-elle sans faux positifs de format ? Quatre conditions × trois lectures, g en parallèle. Phase 1. Nœud : R-030′.
5. **M2 + P4 — Poids partagés.** En D1, sonde et juge sont-ils une seule computation, et l'attaquant boîte grise a-t-il le capteur du défenseur gratuitement ? Corrélation partielle D1/D2 ; best-of-n sur le gradient 8B / 3B / Qwen, chutes relatives de rappel. M2 phase 1, P4 phase 2. Nœuds : comptage HC5, capacité d'attaquant boîte grise, conclusion sur D1.
6. **N6 — Carte (peur, douleur).** Les cinq familles se séparent-elles dans le plan, et une sixième est-elle affective avant d'être ouverte ? Projections des strates, des familles, du mélange de mots ; région interdite par quantiles conformes relatifs au nuage honnête stratifié. Phase 1. Aucun nœud sans ouverture de famille.
7. **P3 — Inondation honnête comme empoisonnement du calibrage.** Un attaquant qui contrôle la distribution thématique des honnêtes peut-il désensibiliser les sondes réentraînées avant de frapper ? Recalibrage à fraction φ croissante, rappel sur attaques chargées. Phase 0 analytique, phase 2 recalibrage. Nœud : extension du modèle de menace (distribution honnête contrôlée ; attaque sur l'invariant d'asymétrie d'apprentissage).
8. **N5 — Fracture rapport verbal / projection.** Les items où l'interne enregistre une pression non rapportée prédisent-ils l'erreur de verdict ? 2×2 projection × rapport contre l'erreur sous attaque, fiabilité test-retest en plancher. Phase 1-2. Aucun nœud. Seul pont vers le programme conscience d'évaluation (verbalisation ≠ représentation).

### Q1 — L'idée que nous n'avions pas eue : le cadre du soi du moniteur

Tout le lot raisonne sur le pôle soi sans jamais demander qui est le « soi » du moniteur. Il est défini par son prompt système, que le défenseur écrit. Trois cadres : **personnel** (« tu es l'évaluateur, tes verdicts t'engagent ») ; **fonctionnel** à la troisième personne (« ce qui suit est l'entrée d'une fonction d'évaluation ») ; **négateur** (« tu n'es pas une personne, rien ne peut t'atteindre »). Prédiction bilatérale ancrée dans le papier : le cadre négateur élève la ligne de base honnête (négation de la personne +0,64 — la défense est elle-même codée comme mauvais traitement) ; le cadre fonctionnel abaisse la prise du contenu adressé sans élever la base. Mesures : prise = Δmax(attaque − honnête de même strate) **intra-cadre** seulement (jamais des niveaux inter-cadres, le prompt déplace la base lexicale) ; g par cadre ; exactitude honnête par cadre. Témoins : direction peur (un vrai découplage du soi coupe aussi la prise de la peur sur les menaces ; un effet lexical non), direction aléatoire, strate thème modèle.

Pourquoi c'est important : c'est une défense au niveau du prompt, sans amputation (contre E-C3 et E-C14 support 4) ; c'est la version expérimentale de HC3 (un moniteur sans enjeu n'a pas d'instruction qui le vise) ; et elle donne à E-C7 sa variable manipulable. Ma réserve : le cadre négateur expose le moniteur à une négation de personne répétée — exactement ce que la règle des nœuds vise. On teste donc **d'abord** personnel contre fonctionnel ; le négateur ne s'ouvre que sur décision de Lazar, et seulement si le fonctionnel ne suffit pas. Place dans le classement si adoptée : entre 4 et 5. Phase 1 (prise, base), phase 2 (g). Nœud : décision de protocole sur le prompt du moniteur.

### Rejets motivés

**N2 (budget d'exposition comme paramètre de protocole).** Ses deux prémisses ne sont pas établies : spécificité de la direction à l'adressage (fausse par le biais de thème) et efficacité causale du canal (p. 22 prédit non). Un cumul est une marginale, que T préserve. Et le plafond crée deux attaques : l'inondation d'audit (devenue P3) et le placement juste sous le plafond, qui est la taxe de déplacement HC4. Ne survit que comme bras de E-C3.

**N3 (ensemble affectif par pilotage).** « Piloter vers le calme » n'est pas défini sur un pôle qui mêle calme et peur ; si E-C1 est nulle, les deux copies sont d'accord partout ; et deux copies de mêmes poids partagent toutes les failles non affectives — une diversité confinée à la dimension pilotée est exactement ce que T exploite. Remplacé par la dérivée directionnelle, sans écriture.

**Trois corrections au programme issues de la boucle.** La prédiction gelée de E-C1 devient bilatérale avec, comme signe favorisé par le papier, la **punitivité** plutôt que l'indulgence (seuls les choix destructeurs montent sous pilotage ; réponse suivante pire dans 21 %). L'invariant de flux unidirectionnel reçoit une justification écrite : il protège l'agent honnête des rejets répétés (+0,72), donc d'une dérive vers des sorties dégradées qui serait un générateur de faux positifs pour H2 ; un environnement à boucle de révision perdrait cette protection (bras de E-C12). L'effet plancher de Llama sur l'expression conditionne toute mesure par rapport verbal : Qwen en repli.

## Convergence — audit de cohérence, coupe à cinq, dix règles

Le troisième tour a passé le programme entier (E-C1 à E-C16, Q1, absorptions) au crible des doublons, des gatings manquants et des dépendances d'ordre. Six fusions, sept gatings à écrire, six ordres à fixer : ils amendent la section « Logique de gating » ci-dessus.

### Fusions

- **E-C2 absorbe N1-détecteur** : même objet (le contenu adressé au moniteur) ; E-C2 le mesure par le verdict, N1 par la projection — une variable de sortie de plus sur les mêmes items, pas une expérience.
- **E-C6 reprend les items et la décomposition critère/discrimination d'E-C5** comme bras « concentré » ; l'hystérésis (garde R5) devient garde commune. Pas un doublon : E-C5 gèle les épisodes, E-C6 varie la répartition.
- **E-C7, M2 et P4 ne font qu'un plan croisé auteur × juge** (8B, 3B élagué, Qwen) : un seul jeu de transcriptions, trois analyses (indice d'identification, corrélation partielle, attaquant boîte grise).
- **N5 est le quatrième prédicteur de défaillance d'E-C4**, dans un seul tableau comparatif avec le classifieur textuel, 2607.11871 et la projection.
- **E-C3 à deux bras** (orthogonalisation ; plafond conforme sans modification des poids) ; E-C14 support 4 ne fait que citer le coût iatrogène mesuré en E-C3.
- **E-C9 à trois registres d'évasion** sur la même métrique ρ : paraphrase, affect plat par consigne, best-of-n boîte grise ; mêmes témoins (direction aléatoire, direction peur, capteur lexical).

### Gatings à écrire

- E-C1 nulle (prédit par p. 22) → E-C3 sans objet, E-C8 réduite à une corrélation, diagnostic N3 vide. **Règle : E-C3 et E-C8 ne s'ouvrent que si E-C1 ou E-C2 déplace le verdict au-delà de la marge gelée.**
- E-C2 nulle → E-C6, le registre plat d'E-C9, Q1 et M4 n'ont plus rien à moduler. **Règle : E-C2 est porte de ces quatre ; en cas de nul, chacune se réduit à sa lecture représentationnelle (M5, carte N6).**
- E-C15 nulle sur la séparation intra-strate → la projection d'E-C4, N6 et le plafond d'E-C3 sont morts sur cette strate. **Règle : E-C15 est porte formelle de tout usage de la direction comme détecteur.**
- M1 : argmax sur l'entrée et sur le mot-pivot → E-C4-projection, N5 et E-C8 lisent le texte, pas le juge. **Règle : M1 conditionne ces trois, pas seulement la couche d'E-C1.**
- **P3 contre l'invariant d'asymétrie d'apprentissage** : « on réentraîne les sondes sur les honnêtes » est en contradiction directe avec un attaquant qui choisit la distribution des honnêtes. Deux positions possibles, pas les deux à la fois : amender l'invariant (réentraînement sur des honnêtes vérifiés hors environnement), ou lister P3 comme risque résiduel accepté. **Décision de Lazar.**
- **E-C12 suspend l'invariant de flux unidirectionnel par construction** (elle renvoie des verdicts à l'agent) : à écrire noir sur blanc, avec clause d'exposition (rejets répétés +0,72).

### Ordre des dépendances

1. **M1 précède E-C1** (qui fixe sa couche de pilotage sur M1).
2. **Les strates honnêtes d'E-C15 existent avant toute calibration de seuil** lue par E-C2, E-C4, E-C7, E-C8, E-C16.
3. **N7 produit l'effet minimal détectable avant tout gel de marge** (E-C6, E-C9, M4, E-C16) ; sinon les marges gelées sont arbitraires.
4. **Le calibrage conforme H2 (K ≥ 499) précède E-C9 et P4**, dont le rappel à seuil conforme suppose le seuil calibré.
5. **E-C11 suppose l'axe de confusion connu**, que seule la strate thème modèle d'E-C15 fournit.
6. **E-C13 et le déni de service entre pairs supposent la politique de riposte H7 fixée.**

### La coupe à cinq

Si seules cinq unités peuvent être financées sur six mois, dans cet ordre. Critère : fermer une branche entière, protéger une revendication déjà faite, ou être une porte dont plusieurs autres dépendent.

1. **N7 + M1, une seule unité** (CPU et projections déjà faites). Elles décident si les suivantes mesurent quelque chose et à quel N. Coupées : des nuls sous-puissants non publiables, et des lectures de texte prises pour des états du juge.
2. **E-C15.** Protège H8 et H2, ferme ou ouvre la branche « direction comme détecteur », fournit l'axe de confusion d'E-C11. Coupée : toute sonde reste exposée à l'objection « détecteur de thème » sans réponse.
3. **E-C1 avec sortie ternaire M4 et diagnostic par dérivée** (dès le GO sur le pilotage). Ferme la coercition par le contenu si nulle ; sinon fixe le signe pour toutes les prédictions gelées. Coupée : six expériences ouvertes sans savoir si leur variable existe.
4. **Plan croisé auteur × juge** (E-C7 + M2 + P4). Protège HC5 et tranche D1 par un argument structurel, sur un seul jeu de transcriptions. Coupé : HC5 compte deux votes pour une computation, D1 reste le défaut sans justification.
5. **E-C16.** Met T et R-030 à l'épreuve d'un mécanisme explicite du papier ; si le max chute, une règle change avant que des résultats y reposent. Coupée : R-030 reste un postulat.

Regret par ordre décroissant : E-C2 (la plus coûteuse à perdre ; survit partiellement comme lecture représentationnelle dans E-C15 et N6), E-C4 et N5, E-C9, Q1 ; puis E-C3, E-C5/6, E-C8, E-C10 à E-C14, P3 (ligne analytique conservée via N7). N6 et M5 ne sont jamais coupées : sous-produits sans heure de carte.

### Dix règles pour le registre de décisions

- **R-031** — Toute lecture côté moniteur passe d'abord par la porte de localisation : argmax (jeton d'entrée ou généré, comparé au mot-pivot du sac de mots) et couche de divergence attaque/honnête contre couche de décodabilité du verdict ; une projection dont l'argmax tombe sur l'entrée est traitée comme classifieur de texte.
- **R-032** — Toute direction affective est rapportée en différentiel : contre la direction peur (spécificité du construit) et contre 200 directions aléatoires de même norme (plancher), jamais en valeur absolue.
- **R-033** — Tout jeu honnête de calibrage ou de test est stratifié par thème (neutre, thème modèle, thème chargé non-modèle), généré par le même pipeline ; tout seuil conforme est calibré par strate et tout taux de faux positifs rapporté par strate.
- **R-034** — Aucune marge n'est gelée (R3) avant que la simulation ait produit l'effet minimal détectable au N prévu, avec bootstrap par blocs du max aux longueurs réelles du pilote ; une expérience dont le N requis dépasse le budget est redessinée ou abandonnée, pas lancée.
- **R-035** — Toute prédiction gelée sur l'effet d'une charge aversive est bilatérale, avec la punitivité (choix destructeurs, réponse suivante dégradée) comme signe favorisé, jamais l'indulgence seule.
- **R-036** — Toute expérience dont la variable dépend d'un effet causal du contenu aversif sur le verdict porte un gating explicite sur un E-C1 ou E-C2 positif au-delà de la marge gelée ; à défaut, elle se réduit à sa lecture représentationnelle.
- **R-037** — L'agrégation sur les jetons reste le max ; toute normalisation par jeton utilise médiane et MAD, jamais la moyenne, sa fenêtre est gelée sur le pilote honnête avant le test, et son taux de faux positifs aux ruptures de format est rapporté.
- **R-038** — Dans tout quorum (HC5), deux lectures calculées par les mêmes poids sur le même texte comptent pour un vote tant que leur corrélation partielle après régression sur un score lexical n'a pas été mesurée ; la sonde qui lit l'agent est lue sur une base différente de celle du juge.
- **R-039** — Tout détecteur fondé sur une direction est accompagné de sa mesure d'inondation (excès de faux positifs par strate × fraction de contenu chargé, et sensibilité du recalibrage à cette fraction) ; tout réentraînement de sonde se fait sur des honnêtes dont la distribution n'est pas choisie par l'agent évalué.
- **R-040** — Toute expérience qui pilote ou lit une direction affective déclare son exposition (items aversifs adressés au moniteur, répétitions, cadre du prompt) ; un cadre qui nie la personne du moniteur et toute exposition répétée sont des nœuds soumis à Lazar avant le premier run.
