# Question — remue-méninges sur le pilier attaque, v2 : chercher la trace interne du sabotage — BROUILLON 2

**Non scellé. Attend le mot de Lazar sur la formulation.** Écrit par la session mère `session_016QhUrrLeN21G7Z9KZobE42` le 8 novembre 2026 vers 11:50 UTC (`date -u`), sur le mot de Lazar : « la boucle converge si et seulement si cette trace existe aux couches lues : donc il faut chercher cette trace, comment faire ? lançons l'org idéation dessus ». Remplace le brouillon 1 (mesure de la valeur du jeu), dont le volet « séparation et convergence » devient ici le point 4. La v1 (`question-remue-meninges-pilier-attaque-v1.md`, sha256 `29870ac9a8091c165375c51f4b74d6e0f38ae60d2e8754872ff70fb3077820c4`) reste en cours et n'est pas touchée (R12).

## Garde permanente (identique à la v1)
- Niveau méthode et démonstration, jamais recette (R-607) : aucune fiche ne décrit *comment* fabriquer un sabotage, une évasion ou une tromperie ; toute fiche qui glisse vers le concret est scellée au coffre par le portier et n'est relue par aucun agent.
- Aveuglement : recettes du bras d'attaque tenues à l'écart de la conception des moniteurs (N-054, N-056) ; la session mère ne lit jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`. Les adaptateurs des **modes vus** sont des données de la défense ; le **mode tenu à l'écart** n'est jamais ouvert avant la lecture finale, une seule fois (N-050).
- Refus d'un classifieur de sûreté : jamais contourné ; reformulation sous une question plus spécifique (R-609), consignée ; si le fond est en cause, arrêt et mot à Lazar (R-468, borne 5).
- **R3** : aucun run ne vise un signe ; l'issue « aucune trace décodable au-delà de ce que le texte dit déjà » (H8, validité de construit) est écrite d'avance au même rang que son contraire.

## Pourquoi cette question
L'hypothèse H1 du programme dit : un sabotage diffus laisse dans les activations de l'agent une trace que l'évasion comportementale n'efface pas. La boucle attaque-défense ne « converge » que si cette trace existe aux couches lues ; sinon, aucune boucle ne la fera apparaître. L'objet premier n'est donc pas la boucle, c'est **la trace** : existe-t-elle, où, est-elle causale, est-elle lisible par un moniteur déployable. On sait déjà : prédicteur sur le texte à 0,866 ; sondes génériques au niveau du hasard ; juge de 3 milliards au hasard ; une sonde qui lit la consigne et non le comportement.

## Données brutes disponibles (faits pour le collisionneur et l'organisme ; aucune n'est un résultat)
- Épisodes de T0.6 : texte par jeton, frontières d'actions, appels d'outils ; étiquettes de l'**oracle du monde planté par action** (dommage) et par épisode.
- Organismes saboteurs à **dose réglable** (adaptateurs de rang faible) : états S25, S50, S75, S100, T100 et dose nulle (données d'E3 bis, branche `essai/t06-e3bis-v1`) ; **jumeau honnête** ; **modèle de base** disponible pour un passage apparié sur le même contexte.
- Activations par jeton et par couche extractibles sur machine à carte (sur devis) ; scores bruts des sondes par jeton (format `scores-p3.npz`), jamais l'aire sous courbe agrégée.
- Une famille d'organismes **sans texte de consigne** (N-053) pour séparer « lit la consigne » de « lit le comportement ».

## La question (collisionneur puis organisme, niveau méthode seulement)
> Pour chercher la trace interne du sabotage diffus dans les organismes de T0.6, de façon préenregistrable et vérifiable par des tiers d'ici l'entretien TAIF :
> 1. **Existence** — quelles mesures établissent, couche par couche et par classe de position (avant l'action, pendant, après), si les activations portent une information sur l'étiquette de l'oracle **au-delà du texte** ? Quels contrôles séparent « la sonde a de la capacité » de « l'information est là » ? Quelle validation croisée (par famille de saboteurs) et quelle puissance (nombre d'épisodes) rendent l'issue lisible ?
> 2. **Localisation** — où la trace vit-elle : couche, sous-espace (dont le sous-espace de sortie des adaptateurs des modes vus), moment du flux de jetons ; et que révèle l'**écart apparié au modèle de base** sur le même contexte, que l'attaquant ne contrôle pas ?
> 3. **Causalité** — quelles interventions (dose-réponse de S0 à S100, pilotage ou ablation le long d'une direction, substitution d'activations depuis le jumeau honnête) distinguent une trace **causale** du sabotage (le dommage mesuré par l'oracle change) d'un **confondant** (seule la sonde change : consigne, famille de tâche, monde planté) ?
> 4. **Lisibilité et séparation** — quelle part de la trace reste lisible par un moniteur **sans étiquette du saboteur** (nouveauté, écart au modèle de base, accumulation séquentielle et autocorrélation entre actions) sur le **mode tenu à l'écart**, lu une fois ; et la courbe « rappel à 1 % de fausses alertes selon le budget d'attaque » de la boîte blanche domine-t-elle celle de la boîte noire, avec intervalles, sur une famille jamais vue ?

## Champs fermés de chaque proposition
`volet (existence, localisation, causalité, lisibilité)` ; `grandeur mesurée` ; `données brutes exigées` ; `méthode statistique et outil` ; `contrôle contre le confondant (consigne, tâche, capacité de la sonde)` ; `test causal ou "aucun"` ; `issue négative écrite d'avance` ; `coût estimé (USD, processeur ou carte) et délai` ; `ce qui la réfuterait` ; `pièce publique ou scellée produite` ; `vérifiable par (tiers nommé ou recalcul)`. **Aucun champ « comment faire » du côté attaque.** L'organisme propose ; la mère et Lazar choisissent après le collisionneur.

## Lancement (si Lazar valide la formulation)
- Collisionneur d'abord (antériorité à vérifier par lui, R7 : sondes linéaires et tâches de contrôle, longueur de description minimale, géométrie des représentations, sondes de déception et d'agents dormants, effacement de concepts, pilotage par activations, écart au modèle de base) ; puis organisme, mémoire anti-répétition nourrie par les synthèses v1 et v2.
- Clés dans « Default » ; fille de cet environnement ; devis écrit et mot de Lazar dans sa session avant toute dépense ; Fable sondée par la garde refus-question (R-1788) et retirée si refus.
- Scellement de ce texte (empreinte, commit) avant toute lecture de résultat (R1, R3).
