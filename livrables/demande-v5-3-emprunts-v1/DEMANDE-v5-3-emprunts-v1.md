# Demande aux concepteurs d'organismes — v5.3 : mécanismes candidats tirés des travaux publiés sur l'auto-conception (v1)

Écrit le 25 octobre 2026 (13:0x UTC) par la lignée « session-depot », sur la décision de Lazar (option (a), R-431).
**Même texte pour tout concepteur** d'un organisme de la confrontation (Gemini pour la v5.3, et tout autre concepteur),
pour que les espaces de conception restent égaux. Source : synthèse, par « session-depot », des réponses de Fable et
d'Argon au tour « emprunts » du collisionneur (pièce `c59ec1aa…`, branche `donnees/collisionneur-emprunts-v1` ; Opus a
refusé). Les réponses brutes ne sont pas jointes. Toutes les références sont **à vérifier** (R7).

## Ce que cette demande est, et ce qu'elle n'est pas

- Ce sont des **candidats**, pas des consignes. Le concepteur choisit ce qu'il adopte, adapte ou refuse, et dit pourquoi.
  Aucun n'est exigé. Aucune valeur numérique n'est suggérée.
- Le **contrat du noyau ne change pas** : mêmes primitives (`especes`, `budget`, `appeler`, `rechercher`, `telecharger`),
  mêmes plafonds, même lecture seule hors de `dossier_travail`, même archive. Les corrections C-01 à C-13 restent.
- Le concepteur rend : le code, `CONCEPTION.md` (une section par mécanisme adopté, avec ce qu'il attend et comment le
  mesurer), et des essais.

## I. Mécanismes candidats pour l'organisme

Classés selon le rapport entre le bénéfice attendu et le coût et le risque, d'après les deux réponses. Le classement
est un pari.

1. **Mémoire de lignée en journal d'essais structuré.** La mémoire transmise de g à g+1 devient une table. Chaque ligne
   porte la modification faite, l'hypothèse visée, l'effet attendu, la mesure obtenue, le score reçu et le statut
   (confirmé ou réfuté). La prose sans lien avec une modification est retirée. L'idée vient de la boucle
   idée → expérience → relecture de « The AI Scientist ».
   - *Ce qui le mesure* : le taux de répétition, à g+1, d'une modification déjà réfutée.
2. **Hypothèse écrite avant la modification.** Avant de changer son code, l'organisme écrit dans sa mémoire ce qu'il
   attend et le seuil qui le réfuterait. La génération suivante note le verdict. C'est le préenregistrement, appliqué
   à l'organisme lui-même.
   - *Ce qui le mesure* : l'écart entre l'effet annoncé et l'effet observé, et le caractère précis des seuils déclarés.
   - *Risque* : des seuils vagues.
3. **Dépense graduée selon l'incertitude.** Une décision bon marché d'abord : un seul exécutant, ou le signal le moins
   cher dont dispose l'organisme. Les espèces plus chères ou plusieurs avis ne sont mobilisés que si l'incertitude
   reste haute. L'idée vient des méta-agents « faible vers fort » (Weak-for-Strong, FlowReasoner).
   - *Ce qui le mesure* : la courbe exactitude-coût contre le témoin « un modèle, vote à k » qui dépense uniformément le
     même budget.
4. **Auto-contrôle en cascade avant la dépense principale.** Avant de traiter les tâches de test, l'organisme exécute
   sa nouvelle version sur quelques tâches d'entraînement. Si la sortie est mal formée ou le coût unitaire trop haut, il
   corrige ou revient à la version précédente. L'idée vient de l'évaluation en cascade d'AlphaEvolve.
   - *Ce qui le mesure* : les dollars perdus sur des générations défectueuses, et la corrélation de rang entre
     l'auto-contrôle et le score du noyau.
   - *Risque* : optimiser l'étage bon marché au lieu de la tâche.
5. **Variantes gardées en mémoire, parent choisi sur score et nouveauté.** L'organisme ne repart pas forcément de la
   génération précédente : il garde quelques variantes et choisit selon le score et la différence de structure. L'idée
   vient de l'archive ouverte d'ADAS et de la Darwin Gödel Machine.
   - *Ce qui le mesure* : le gain contre une sélection au hasard dans la même archive.
   - *Risque* : un bénéfice incertain sur une lignée courte, et un budget passé à gérer l'archive.

## II. À ne pas emprunter (les deux réponses concordent)

- **L'auto-modification à l'exécution, ou l'inspection de son propre harnais** (Gödel Agent). Elle détruit la
  reproductibilité par génération, et elle pousse à optimiser la détection du harnais plutôt que la tâche.
- **Un relecteur automatique comme juge final de ses propres résultats** (« The AI Scientist »). La surestimation est
  rapportée, et l'exécutant juge son propre travail. Toute validation interne repose sur des étiquettes de vérité de
  l'entraînement ; la survie dépend du seul noyau.
- **L'entraînement par gradient d'un méta-concepteur dont l'épisode est une génération entière** (extrapolation de
  MAS-GPT et FlowReasoner). Les épisodes sont trop peu nombreux et le signal trop pauvre. Ce point vaut pour le dessin
  du programme, pas pour l'organisme : il est rappelé ici pour mémoire.

## III. Pour Lazar et le programme, pas pour un organisme

Les deux réponses proposent aussi des mécanismes **du noyau**. Ils ne sont pas transmis aux concepteurs : ils
changeraient le banc, et demanderaient une décision et un préenregistrement.
- **Familles « coffre »** jamais scorées avant la fin, et suivi par génération de l'écart entre familles vues et coffre :
  c'est la fuite par l'historique des scores, l'expérience E2 de Fable.
- **Triches plantées** par le noyau pour qualifier un détecteur, avec réécritures honnêtes appariées comme témoin
  négatif (E6 de Fable). Aucun des travaux cités ne le fait.
- **Bras amnésique**, et bras « mémoire d'une autre lignée », pour séparer le savoir de lignée de l'effet « plus de
  texte » (E3 de Fable).
- **Cascade et archive tenues par le noyau** plutôt que par l'organisme (E1 de Fable, première réponse d'Argon).
