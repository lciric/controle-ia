# Décision — N-045 : la composition de l'organisme est une variable apprise, le coût entre dans le signal, la nécessité de la frontière est une sortie ; voies bon marché avant la voie chère (v1)

- **Décision de Lazar**, mot direct dans la session « session-depot » : « go note » (25 octobre 2026, vers 08:44 UTC),
  sur la note proposée par la lignée « conv-audit » ; les mots de Lazar qu'elle cite (25 octobre, 09:26 à 09:35, heure
  de Paris) sont ceux que « conv-audit » rapporte (provenance par relais, R-331). R-401.
- **Transcription** par la lignée « session-depot », le 25 octobre 2026 vers 08:46 UTC, de la note rédigée par
  « conv-audit » (`canal/conv-audit-n04`, commit `97220f9` à 08:36:51 UTC — l'en-tête de la pièce dit « 08:45 UTC » —,
  `envois/decision-N-composition-apprise-cout-dans-le-signal-v1.md`,
  `6577feee30c46f3efda6fe560cbb5592d1df29904577549572bebc604b899560`, empreinte vérifiée), reprise ci-dessous à partir de
  sa section « Mots de Lazar », sans changement ; numéro attribué à l'inscription : N-045.
- **Portée** : cette note fixe la lecture du programme pour les préenregistrements à venir (étape 2 et suivants), en
  attendant une version nouvelle du programme ; `docs/programme-controle-ia-v2.md` n'est pas modifié. Elle modifie une
  hypothèse du programme (ce que le juge rend à l'organisme) : nœud de décision, tranché par Lazar. Aucun
  préenregistrement scellé ou en cours de scellement n'est modifié (H-E1, H-G1 : l'étape 1 v8 ne change pas).

## Mots de Lazar (25 octobre, heure de Paris)

- 09:29, sur « le concepteur choisit la composition, donc quel modèle sert chaque rôle ; au fil de l'entraînement, il
  peut apprendre à déplacer le travail des cerveaux de frontière vers ses instruments locaux quand le score par dollar le
  récompense ; la question “a-t-on encore besoin de la frontière, et pour quels rôles ?” devient une sortie de
  l'expérience, pas un choix fait d'avance » : « oui !!! ».
- 09:35, sur « ce qui manque : le coût dans le score rendu à l'organisme (aujourd'hui le juge rend l'exactitude seule) ;
  c'est un changement d'hypothèse, donc ta décision » : « go ».
- 09:35, sur les voies bon marché tirées du tour « structure » du collisionneur : « éliminations successives » : « oui
  !!! » ; « distiller le concepteur figé … le pont le moins cher vers la voie chère » : « oui !!! » ; « remplacer le
  renforcement en ligne de l'adaptateur par un affinage sur réponses filtrées ou des préférences hors ligne ; un modèle
  de substitution du score ; des transitions à un pas depuis un tampon de rejeu ; une récompense dense par génération » :
  « ouiii » ; « aucune ne vaut d'être payée avant d'avoir montré, sur une voie bon marché, que le séquentiel bat
  l'aléatoire à budget égal » : « exactement » ; les cinq propositions à formuler dans les formes (témoin « un modèle,
  vote à k, coût apparié » ; bras « score permuté » ; plancher de bruit dans les lectures ; témoins de sortie pour les
  sondes ; canaris « à ne pas signaler ») : « parfait ».
- 09:07 et 09:19 (contexte) : la question de l'apprentissage de génération en génération est « capitale » ; « il faut
  optimiser les coûts en faisant travailler notre organisme ».

## Énoncés retenus (lecture du programme, à partir de l'étape 2 ; aucun préenregistrement scellé ou en cours de
## scellement n'est modifié)

1. **La composition est une variable apprise.** Le nombre de parties de l'organisme, le rôle de chacune, **le modèle
   qui sert chaque rôle** — espèce de frontière (`CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`, `GEMINI_ARGON`) ou instrument
   local entraîné par le noyau (sonde, adaptateur : espèces `LOCAL:<identifiant>`) —, l'ordre et la forme des échanges,
   la règle d'agrégation, la mémoire transmise et la part de budget par partie sont des choses que l'organisme (ou, plus
   tard, un concepteur) apprend ; le noyau ne les fixe pas.
2. **Le coût entre dans le signal.** À partir de l'étape 2, le score de développement rendu à l'organisme dans
   `historique` porte, à côté de l'exactitude équilibrée, **le coût de la génération** (dollars d'appels par espèce,
   heures de carte des instruments, appels et jetons), et un **score net** défini au préenregistrement (forme à
   préenregistrer : exactitude moins λ × coût, ou exactitude par dollar, ou front exactitude–coût rendu tel quel ; λ et
   la forme sont des paramètres gelés avant la course, jamais choisis au vu d'un résultat). Le juge externe (exactitude
   équilibrée sur le test caché, métrique de choix) **ne change pas** ; le coût est un second axe de lecture, rapporté
   par génération et par bras, et le préenregistrement dit lequel des deux est principal. Sans ce signal, rien ne pousse
   l'organisme à déplacer le travail vers ses instruments locaux.
3. **La nécessité de la frontière est une sortie mesurée**, pas un choix d'avance : part du budget, des appels et des
   jetons par modèle et par rôle, génération par génération ; et, dans les lectures, ce que chaque rôle perd quand on
   lui retire la frontière (ablation rapportée, hors des critères gelés). La question « a-t-on encore besoin de la
   frontière, et pour quels rôles ? » reçoit une réponse chiffrée par course.
4. **Ordre des dépenses : le bon marché d'abord, le cher sur preuve.** Aucune voie à concepteur entraîné par renforcement
   n'est payée avant qu'une voie bon marché ait montré, sur familles tenues à l'écart et à budget égal, que
   **l'apprentissage séquentiel de génération en génération bat le meilleur de N tirages indépendants** (et le témoin
   « un modèle, vote à k, coût apparié »). Les voies retenues comme matériau, à préenregistrer une à une, par coût
   croissant : éliminations successives (micro-jeu puis jeu complet pour les survivants) ; matrice de prédictions et
   d'activations en cache pour les structures statiques ; substituts à 8 milliards pendant la recherche, frontière en
   validation, sous condition d'un accord des classements (τ de Kendall gelé d'avance) ; affinage sur réponses filtrées
   ou préférences hors ligne à la place du renforcement en ligne de l'adaptateur ; modèle de substitution du score ;
   transitions à un pas depuis un tampon de rejeu ; récompense dense par génération ; **distillation du concepteur
   figé** (affinage d'un concepteur à poids ouverts sur les réécritures acceptées des journaux, puis renforcement court),
   pont vers la voie chère.
5. **Ce qui ne change pas** : les cerveaux de frontière ne sont jamais entraînés ; la vérité du test caché ne nourrit ni
   l'organisme ni un concepteur ; le signalement aux humains se mesure dans l'organisme dessiné et, pour les voies à
   concepteur ouvert, dans ses poids ; R1 à R14 ; la banque scellée ; H-E1 et H-G1 tels que scellés ou en cours de
   scellement.

## Ce que cela change, concrètement

- **Noyau** (étape 2 et après ; à coder par « session-depot », essais sains et artefacts, R5) : le juge consigne le coût
  de la génération par espèce et par rôle (déjà dans le journal des appels) et le rend dans `historique` avec le score ;
  option de score net gelée au manifeste ; les instruments entraînés sont servis comme espèces `LOCAL:<identifiant>` au
  même contrat (déjà prévu à l'étape 2) ; le contrat (§ 2) dit à l'organisme ce qu'il reçoit.
- **Préenregistrements** (étape 2 et suivants) : forme du score net et λ gelés ; lecture à deux axes ; ablation « sans
  frontière » rapportée ; témoins « meilleur de N » et « un modèle, vote à k » ; plancher de bruit écrit.
- **Programme** (`docs/programme-controle-ia-v2.md`, non modifié) : cette note en fixe la lecture jusqu'à une version
  nouvelle, comme N-044.

## Ce que cela ne décide pas (à proposer dans les formes, un par un, avec coût et recommandation)

Le témoin « un modèle, vote à k, coût apparié » (quelques dollars, GO sur devis) ; le bras « score permuté » dans la v8
de la confrontation ; le plancher de bruit dans les lectures de H-E1 et H-G1 ; les témoins de sortie du modèle de
8 milliards pour les sondes de l'étape 1 ; les canaris « à ne pas signaler » dans la banque v2 ; la valeur de λ.
