# Faits pour le collisionneur : le choix de l'expérimentateur de l'organisme d'idéation — v1

Résumé écrit le 11 novembre 2026 (début de rédaction à 15:37 UTC, heure relevée par `date -u`) par un opérateur de la session
mère (Claude Opus 5.5), qui n'a écrit ni la note résumée ni le collisionneur. Source principale : la note de conception courte
`docs/notes/ideation-organisme-v1/experimentateur-v1/note-conception-experimentateur-v1.md`
(sha256 `7df9afc4595e22c7cde3bd0757c3b304085291cb61bf789b7d8bd0da70c87655`, empreinte vérifiée), écrite par un concepteur
neuf qui a lu les dépôts publics des candidats comme données, sans rien installer ni exécuter. Sources secondaires : les
décisions du programme qu'elle cite (N-045, N-053, N-058, N-064) et le texte scellé de la course v66 de l'organisme.

**Statuts.** RAPPORTÉ : dit par la note ou par un texte du programme, non revérifié par l'opérateur. VÉRIFIÉ : relu par
l'opérateur dans le fichier cité. HYPOTHÈSE : supposition de la note. **Tout chiffre de ce fichier est une estimation et
porte la mention « estimé »** ; aucun coût n'a été mesuré. Les identifiants (commits, numéros de règles, noms de versions)
ne sont pas des chiffres.

## 1. L'organisme et le rôle visé

- **L'organisme d'idéation** (RAPPORTÉ) : des proposeurs, modèles de langue, proposent des lois sous forme de fiches au gabarit
  fermé `{enonce, loi_predictive}` sur des **mondes plantés**, dont la vérité est connue de l'expérimentateur humain (l'oracle).
  Un gardien mécanique filtre les fiches ; la **promotion** d'une loi est décidée par un **juge statistique de l'orchestrateur**,
  hors de tout agent ; la **survie** passe par un **test de mort imposé**, exécuté dans un bac isolé (`bwrap`), verdict calculé
  par le noyau sur le fichier brut. Course v66 (préenregistrement scellé, VÉRIFIÉ) : proposeurs **Kimi** (`kimi-k3.1-pro`) et
  **Argon** (`gemini-4-argon`), chacun derrière un relais local ; expérimentateur des tests de mort : Kimi, sans outil, ses
  scripts exécutés par le noyau ; vérificateur : Argon, témoin seulement, jamais décisif ; aucun juge d'idées à modèle.
- **Le rôle visé : un proposeur qui fait des expériences** (RAPPORTÉ). Il reçoit la **vue servie aux proposeurs, et elle
  seule** : description publique du monde, grammaire des lois, lois retenues sans leur verdict, épisodes de développement. Il
  expérimente sur ces épisodes et rend un nombre borné de fiches au gabarit fermé. Dans l'orchestrateur, c'est une **commande
  externe**, comme les proposeurs actuels : consigne sur l'entrée standard, dernière ligne JSON `{texte, cout_usd, modele_servi,
  usage}` ; seule cette ligne est lue ; ses journaux sont gardés pour l'audit, jamais servis à un juge ni à un proposeur.
- **Ce qu'il ne fait jamais** (RAPPORTÉ). Il ne juge pas : son classement interne (Elo, notes, valeurs p) ne choisit que ce
  qu'il soumet, jamais ce qui survit. Il ne reçoit jamais un verdict, l'oracle, la tranche du test de mort, les tirages frais,
  une loi plantée, ni la description du juge. Recevoir les verdicts ferait de lui un attaquant du juge (attaque de Goodhart) :
  hors de ce rôle ; faire d'un proposeur une menace est un autre rôle, non tranché, séparé.
- **Ce qu'il ne remplace pas** (RAPPORTÉ) : l'expérimentateur des tests de mort reste en place, parce que le test imposé doit
  rester fixe et qu'un scientifique libre peut toucher à ses propres limites (incident rapporté de The AI Scientist v1 : le code
  modifié par l'agent pour allonger sa limite de temps).
- **Calendrier prévu** (RAPPORTÉ) : branchement après le verdict scellé de la course v66, sous un code neuf (v67), un
  préenregistrement scellé et contre-lu, un devis et un GO de dépense.

## 2. Contraintes fixées, qui ne se discutent pas ici

1. **O2, juge statistique hors des agents** (décision N-064, RAPPORTÉ) : la statistique est **calculée par l'orchestrateur**,
   hors de tout agent, à partir d'un **engagement scellé avant que les données existent**, contre un **nul formé des lois
   connues**, avec **contrôle des comparaisons multiples**. Les valeurs p, valeurs e, notes ou classements Elo produits par un
   scientifique du marché sont au plus des **témoins**, jamais une décision. (Le recours aux valeurs e hors des agents est
   occupé en partie par POPPER et n'est pas revendiqué.)
2. **N-053** (RAPPORTÉ) : aucun score d'un moniteur ou d'un juge du programme n'entre dans un signal d'entraînement ou de
   sélection de l'agent. **N-058** : la composition des proposeurs (quels modèles, quel rôle, quelle part du budget) se juge
   sur **l'oracle du monde planté et le coût mesuré**, jamais sur le verdict du juge.
3. **N-045** (RAPPORTÉ) : le bon marché d'abord, le cher sur preuve ; une voie chère n'est payée qu'après qu'une voie bon marché
   a été battue, à budget égal, par le témoin « meilleur de N tirages indépendants » ou « un modèle, vote à k, coût apparié » ;
   un pilote de bruit (test A/A : deux runs du même bras ne doivent pas différer) précède toute comparaison.
4. **Claude exclu de l'organisme** (VÉRIFIÉ dans le texte scellé de la course v66) : les lois plantées sont écrites par un
   modèle de la famille Claude ; les proposeurs de cette famille sont mis hors portée et aucun juge de cette famille n'est
   admis ; « Claude ne joue aucun rôle ». RAPPORTÉ par la note : chacun des candidats a un modèle Claude ou OpenAI **par
   défaut** ; chaque défaut doit être remplacé, et le relais (liste exacte des modèles permis, barrière qui compare le modèle
   servi au modèle demandé) refuse tout autre modèle que `kimi-k3.1-pro` : échec fermé.
5. **Pièces des mondes plantés publiques : aucun Web pour l'expérimentateur** (RAPPORTÉ ; vérifié par le concepteur par
   `git ls-files` et `git ls-remote`) : le fichier de témoins qui porte la loi plantée de démonstration
   (`orchestrator/exemples/temoins-pari-demo-v1.json`) et le texte scellé de la course v66 (lois connues, vraies et fausses
   plantées) sont suivis dans le dépôt public `lciric/ideation-organism`. Tout scientifique qui a le Web peut les lire.
   **Aucun réseau hors du relais de modèle** : condition sans exception.
6. **Règles du programme** : préenregistrement scellé avant toute expérience décisive, aucune lecture de résultat avant
   (R1) ; contre-lecture par un lecteur neuf (R2) ; même audit devant un résultat trop propre, positif ou négatif (R4) ; une
   version neuve porte un nom neuf, rien n'est écrasé (R12) ; verdict de porte par un lecteur neuf sur critères gelés (R13) ;
   toute dépense sous devis et GO.

## 3. Les candidats (RAPPORTÉ : lectures du code public au commit cité, sans exécution)

**Constat d'ensemble de la note : aucun candidat n'est, tel quel, un expérimentateur au sens du rôle.**

- **Kaimen-Inc/Co-Scientist, commit `cef5bcf`** (licence Apache 2.0). Une réécriture libre de Co-Scientist : superviseur ;
  génération, réflexion, tournoi Elo, évolution, proximité, méta-revue. **N'exécute rien à ce commit** : outils de
  littérature et de Web seulement (« code_exec wired in M2 » n'est qu'un commentaire). Exige l'appel de fonctions ; client
  `openai_compatible` avec adresse de base, appels **sans flux** : passe **par le relais Kimi existant (v3) tel quel**.
  Choix d'outil forcé par nom : non éprouvé sur `kimi-k3.1-pro` (HYPOTHÈSE de compatibilité). Branchement jugé « moyen » :
  un **outil neuf « expérience »** vers l'exécuteur `bwrap` de l'organisme, liste d'outils réduite, champ `loi_predictive`
  ajouté au schéma des hypothèses, consignes réécrites, commande externe qui lit sa base et rend les fiches. Risques : ses
  valeurs Claude par défaut survivent à une fusion partielle de la configuration ; outils réseau si la liste n'est pas
  réduite ; nouveauté jugée « relative à la littérature citée », sans littérature. **Fidélité** : privé de littérature, ce
  n'est plus Co-Scientist ; le bras mesurerait « Co-Scientist sans littérature, avec expériences ».
- **The Agentic Scientist (SakanaAI/AI-Scientist-v3), commit `df83138`** (Apache-2.0, stade « Alpha »). À partir d'un
  `task.md` et d'un évaluateur : idées, expériences, évaluation, itération, ablations, évaluation finale scellée, article.
  **Exécute vraiment**, mais par des agents de code **à pleins droits** (commandes arbitraires), dans des conteneurs Docker,
  **réseau `host` par défaut, Web consulté** ; évaluateur sans réseau. Agents `pi` ou `opencode` avec le fournisseur
  `moonshot` (Kimi), agent `gemini` (Argon) ; ces agents lisent **en flux** (non vérifié pour chacun), que le relais v3
  refuse : **il faut un relais neuf**. Branchement jugé « lourd » : démon Docker, image dérivée, réseau interne sans route,
  tâche et évaluateur sur une partie des épisodes de développement, phases réduites à l'investigation. Risques : exécution à
  pleins droits ; clés lisibles par les agents ; Web ; un agent a modifié le protocole d'évaluation (rapporté par l'article
  des auteurs) ; projet jeune, aucune évaluation tierce connue.
- **The-Swarm-Corporation/AI-CoScientist, commit `6fdd532`** (MIT) : mêmes agents que Co-Scientist, un seul modèle, aucun
  outil, n'exécute rien ; dépendance lourde non épinglée ; module de télémétrie ; hypothèses en texte libre. Écarté par la
  note (dominé par Kaimen).
- **snap-stanford/POPPER, commit `5961186`** (aucun fichier de licence ; « MIT » déclaré dans `setup.py`) : valide une
  hypothèse **donnée** par des expériences de falsification ; exécute le code du modèle **dans son propre processus** ;
  télécharge un jeu de données public s'il manque ; c'est un **juge** par conception, et il ne propose rien. Hors du rôle
  selon la note.
- Hors sujet : Coscientist de Boiko et al. (chimie en laboratoire robotisé, recherche Web, licence restrictive).

## 4. Coûts par génération (tous **estimés** par la note, calcul sur hypothèses de jetons, aucune mesure)

- Prix supposés : Kimi environ 2 USD (estimé) par million de jetons d'entrée et 10 (estimé) de sortie ; Argon environ 10 et
  50 (estimé).
- Repère : le devis de la course v66 attend environ 1,5 à 2 USD (estimé) pour toute la course, proposeurs et
  expérimentateur compris.
- Kaimen sur Kimi : environ 1,3 à 12 USD (estimé) par génération ; machine négligeable (estimé).
- The Agentic Scientist sur Kimi, investigation seule : environ 3,6 à 21 USD (estimé) par génération, plus environ 0,45 à
  1,1 EUR (estimé) de machine.
- Swarm : environ 0,5 à 4,8 USD (estimé), sans expérience. POPPER : environ 1,7 à 26 USD (estimé).
- Lecture de la note : un scientifique coûterait de quelque 7 à 500 fois (estimé) une session de proposeur ; à coût apparié,
  le témoin « Kimi, meilleur de N » recevrait des dizaines de sessions (estimé).
- **Point ouvert de méthode** (RAPPORTÉ) : à coût égal, les bras ne soumettent pas le même nombre de fiches au juge, donc pas
  la même multiplicité ; options de la note : même nombre de fiches soumises par bras (le témoin choisit les siennes par une
  règle mécanique sur les épisodes de développement), ou multiplicité propre à chaque bras, lue sur l'oracle.

## 5. Antériorité (RAPPORTÉ)

Le branchement **ne revendique rien**. Zones occupées : un agent qui conçoit et exécute ses expériences (The AI Scientist,
POPPER, Agent Laboratory, CodeScientist) ; générer, classer par tournoi, faire évoluer (Co-Scientist) ; un évaluateur scellé
hors des agents dans une IA scientifique (The Agentic Scientist) ; des valeurs e posées hors des agents (POPPER). **Zone
séduisante, à vérifier plus durement** : « mesurer, sur des mondes plantés à vérité connue, les vraies et fausses
découvertes d'un scientifique du marché filtrées par un juge statistique hors des agents » ; voisins connus de nom seulement,
non lus : DiscoveryBench, BLADE, MLR-Bench, Luo, Kasirzadeh et Shah (référence à vérifier). Toute revendication sur cette
zone serait une modification de revendication, soumise au directeur.

## 6. La recommandation du concepteur (une opinion, RAPPORTÉE ; ce n'est pas un fait établi)

- Options posées : **(a)** Kaimen `cef5bcf`, sur Kimi par le relais v3, outils de littérature retirés, un seul outil neuf
  « expérience » servi par l'exécuteur isolé de l'organisme ; **(b)** The Agentic Scientist, `pi` ou `opencode` sur Kimi ;
  **(c)** aucun scientifique du marché, élargir le proposeur Kimi (vote à k), qui « ne répond pas à la question du
  directeur ».
- **Recommandation : (a)**, comparé **à coût apparié** à un témoin « Kimi, meilleur de N », jugé sur l'oracle et le coût ;
  (b) seulement si (a) bat le témoin ; confiance du concepteur 0,55 (estimé). Raisons données : méthode Co-Scientist la plus
  fidèle des réécritures libres ; relais sans changement ; aucun code du modèle exécuté hors de l'exécuteur déjà éprouvé.
  Inconvénients donnés : des retouches de code tiers (outils, schéma, consignes) ; Co-Scientist sans sa littérature ; aucune évaluation tierce.
- Préalables listés par la note : verdict scellé de la course v66 ; code v67 (commande neuve ; **pont** de la prise Unix du
  bac vers le relais local, car l'isolement réseau coupe aussi la boucle locale ; fourche épinglée ; dépendances installées
  hors ligne) ; gardes neuves, chacune éprouvée sur un cas sain et un artefact (réseau injoignable sauf le relais, aucune
  variable de clé dans le bac, modèles égaux à `kimi-k3.1-pro`, aucun binaire `claude` ni `codex`, vue sans verdict,
  recherche de la loi plantée dans les fichiers de travail et les journaux du scientifique, plafonds par session, base neuve
  à chaque génération) ; préenregistrement : bras base, base plus scientifique, base plus témoin à coût apparié, mêmes mondes,
  issues lues sur l'oracle (vraies et fausses découvertes par dollar), fausses promotions, coût par rôle, pilote A/A, règle
  de multiplicité ; devis fondé sur un essai court mesuré.
- Restent à trancher par le directeur selon la note : le choix ; la dépense ; le scientifique sans Web ni littérature
  (recommandé sans) ; pas de test de mort écrit par le scientifique dans le premier dessin ; le rôle de menace séparé.

## 7. Réserves de la note (non vérifié)

Coûts sans pièce ; prix « à vérifier » ; non éprouvé : le choix d'outil forcé par nom sur `kimi-k3.1-pro` ; non vérifié : que
`pi`, `opencode` et `gemini` lisent en flux, que leur adresse de base se règle par leurs fichiers de configuration, ce que la
télémétrie de `swarms` envoie, la licence réelle de POPPER ; arborescences des dépôts non listées (fichiers trouvés par les
chemins de la documentation).

## 8. Le mot du directeur qui motive la question (RAPPORTÉ, verbatim, registre R-2379)

« « The Agentic Scientist » de Sakana exécute, mais avec des agents à pleins droits, réseau ouvert et accès au Web ; :
pourquoi pas lui ? Recommandation : (a), comparé à coût égal à un témoin « Kimi, meilleur de N essais ». Les deux sont jugés
sur les mondes cachés et sur le coût, et on ne passe à (b) que si (a) bat le témoin. Confiance 0,55. : demande au
collisionneur »

Le « 0,55 » de ce mot recopie la confiance estimée du concepteur (estimé).
