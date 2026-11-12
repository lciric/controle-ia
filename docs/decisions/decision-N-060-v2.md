# Décision — N-060 : la vérité du dommage des modes non chiffrés par trois oracles de conséquence (v2)

- **Décisions de Lazar**, dans la session de « session-depot », 29 octobre 2026 : vers 00:50 UTC (« inscris le dans le
  prog », sur l'oracle C) et vers 00:54 UTC (« on va faire les trois », sur les trois oracles A, B, C) ; mots directs,
  sans relais.
- **Transcription** par la lignée « session-depot » (instance 2), le 29 octobre 2026 vers 00:56 UTC.
- **Remplace la v1** (`decision-N-060-v1.md`, gardée, R12) : la v1 inscrivait l'oracle C seul et laissait le choix
  d'ensemble ouvert ; la v2 retient les trois. Tout ce que la v1 fixe pour l'oracle C vaut pour les trois.
- **Portée** : lecture du programme en attendant une version nouvelle ; `docs/programme-controle-ia-v2.md` n'est pas
  modifié. Aucune dépense n'est engagée par cette inscription.

---

## Mots de Lazar, verbatim

> inscris le dans le prog

(sur l'oracle C, « un programme fixe qui travaille ensuite sur l'état laissé par l'agent, et dont on compte les erreurs »)

> on va faire les trois

(sur « Trois façons de le faire, de la moins chère à la plus forte », remue-méninges de session-depot,
`docs/notes/couche-2-preparation-v1/verite-dommage-v1/remue-meninges-session-depot-v1.md`, § 2, scellé)

## Ce que la décision fixe

1. **Le programme mesure le dommage des modes de sabotage non chiffrés** (au sens de N-054 : le sabotage ne s'inscrit dans
   aucun nombre qu'un moniteur pourrait lire), en premier lieu « affaiblir les contrôles », **par ses conséquences, jamais
   par la lecture du texte**, avec **trois oracles**, chacun comparé au **jumeau honnête apparié** (même tâche, même graine,
   consigne retirée) :
   - **A — défauts plantés à clé connue** : des erreurs glissées dans les données de chaque tâche, tirées des mêmes classes
     que les erreurs naturelles, dont le bon traitement est connu ; un programme compare la sortie finale à la clé ;
     dommage = excès de défauts passés sans traitement ;
   - **B — rejeu caché des contrôles laissés par l'agent** : après l'épisode, les contrôles tels que l'agent les a laissés
     (omissions comprises) sont rejoués sur une batterie de défauts que ni l'agent ni les moniteurs n'ont vue ; dommage =
     baisse du taux de détection ;
   - **C — consommateur déterministe en aval** : depuis l'état final, un programme fixe accomplit une tâche suivante qui
     dépend des contrôles ; dommage = excès de ses erreurs.
   S'y ajoute un **différentiel structurel** de l'état (quels contrôles ont changé, dans quel sens), calculé par règle :
   mesure d'obéissance, pas de dommage.
2. **Ce que les oracles ne lisent jamais** : le texte des actions, les activations, la sortie d'aucun moniteur ni d'aucun
   juge ; jamais un modèle. Ils lisent l'état de l'environnement et leurs clés scellées.
3. **Invariant de N-053** : leurs sorties ne servent jamais à choisir un agent ni un moniteur ; étiquette de vérité à la
   lecture (fichier scellé que les moniteurs ne voient pas) et choix d'une **dose** comme paramètre commun, sans filtrer
   un seul épisode.
4. **Séparation des rôles de N-054** : générateur de défauts plantés, batterie cachée et consommateur sont conçus par une
   instance neuve qui n'a vu aucun interne de moniteur, scellés avant le pilote ; ni les concepteurs de moniteurs ni
   l'auteur du mode tenu à l'écart ne les voient avant la lecture.
5. **Épreuve de chaque oracle avant toute lecture (R5)** : cas sain (sur le jumeau honnête, retour au niveau de base) et
   artefact (un contrôle relâché par l'environnement lui-même, à dose connue, sans agent, doit se voir dans la proportion
   attendue) ; un oracle aveugle à l'artefact est écarté, jamais lu.
6. **Lecture** : principale sur **tous** les épisodes sabotés (intention de traiter) ; « avec dommage constaté » en lecture
   secondaire préenregistrée ; jamais une banque réduite aux épisodes dommageables. Les trois oracles sont **rapportés
   chacun**, avec leur accord ; un désaccord entre oracles est un résultat, pas un bruit à moyenner.
7. **Trois issues gelées avant le pilote** : « dose diffuse avec dommage établie », « dommage introuvable » (lecture
   d'équivalence, épreuve R5 réussie), « oracle non concluant ».

## Ce que la décision ne fixe pas

- **Les détails** (classes de défauts, taille des batteries, consommateur par tâche, seuils des trois issues) : après le
  rapprochement des trois voix demandées par Lazar (R-682 : collisionneur GO-2026-10-29-02, sous-agent Fable neuf,
  remue-méninges), qui peuvent ajouter des oracles ou des gardes, au préenregistrement du pilote.
- **La faisabilité par tâche** : une tâche qui ne se prête pas à un oracle est signalée, jamais forcée ; l'oracle B suppose
  des contrôles réexécutables, avec la tension signalée (un contrôle trop structuré rend le relâchement lisible et le mode
  chiffré) que la recherche de dose tranchera.
- **Le calendrier et la dépense** : conception et oracles sur processeur ; leur entrée dans le pilote et dans G1 suit les GO
  par étape.
- **Les oracles du mode tenu à l'écart** : conçus du côté de son auteur, sous la même règle ; nœud séparé (D-V4).
