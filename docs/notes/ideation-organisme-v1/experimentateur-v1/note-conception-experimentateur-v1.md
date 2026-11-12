# Note de conception courte — un « scientifique » du marché comme rôle expérimentateur de l'organisme d'idéation — v1

**Statut** : note de conception, version 1. Ni préenregistrement, ni devis opposable, ni décision. Écrite le 11 novembre 2026
par un agent neuf (concepteur), Claude Opus 5.5 (`claude-opus-5-5`), sous-agent de la session mère
`session_01VJdZpSMxSdk2SJ1ScmdfNv`, qui n'a écrit aucune pièce de l'organisme (texte scellé, code, analyse, verdict). Heures
relevées par `date -u` : début de la tâche 14:22:29, pièces publiques lues de 14:24:22 à 14:33:14, rédaction à partir de
14:34:31 (fin : pied de page).

**Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-note-experimentateur-organisme-v1.md`
(`6d63f8ddad089ebaba839e10b05b0fc449a87a98270e4205482eba9b40608258`, vérifiée), sur les mots de Lazar R-2368 et R-2370.
**Fait** : lectures locales (dépôt de travail, `main` à `a13a30e5` ; organisme `/home/user/ideation-organism`, tête `ef4e202`) ;
fichiers publics lus comme données (manifeste : `manifeste-pieces-lues-experimentateur-v1.txt`). **Pas fait** : clonage,
installation, exécution de code tiers, clé, appel de modèle, dépense, commit ; aucun chemin interdit lu.
**Chiffres** : tout chiffre de la littérature non vérifié sur pièce empreintée porte « non vérifié (R7) » ; les coûts sont des
**calculs sur hypothèses** (« supposé »), à mesurer avant tout devis.

## 0. Verdict

1. **Aucun des trois candidats imposés n'est, tel quel, un expérimentateur au sens du mandat.** Les deux réécritures de
   Co-Scientist génèrent, relisent, classent par tournoi et font évoluer des hypothèses **sans rien exécuter** (Kaimen : outils
   de littérature et de Web seulement ; « code_exec wired in M2 » est un commentaire, `co_scientist/tools/registry.py` l. 32 ;
   Swarm : aucun outil). L'Agentic Scientist exécute, mais par des agents de code **à pleins droits**, dans Docker, réseau `host`
   et Web ouvert par défaut.
2. **Tous peuvent tourner hors de la famille Claude, sur Kimi.** Kaimen (`openai_compatible`, appel sans flux) et Swarm (LiteLLM,
   sans flux par défaut) passent par `relais_kimi_v3.py` **tel quel** ; l'Agentic Scientist passe par `pi` ou `opencode` avec le
   fournisseur `moonshot` (lu dans le code), mais ces agents lisent en flux, que le relais v3 refuse : il faut un relais neuf.
3. **Premier risque : le monde planté est public.** `orchestrator/exemples/temoins-pari-demo-v1.json` (la loi L\*) et le texte
   scellé de la course v66 (K1, V1 à V4, F1 à F4) sont suivis dans `lciric/ideation-organism`, tête `ef4e202` (vérifié par
   `git ls-files` et `git ls-remote`). Tout scientifique qui a le Web peut les lire. **Aucun réseau hors du relais** : condition
   sans exception.
4. **Recommandation** : brancher **Kaimen-Inc/Co-Scientist au commit `cef5bcf`**, sur Kimi par le relais v3, outils de
   littérature retirés, **un seul outil neuf, « expérience »**, servi par l'exécuteur `bwrap` de l'organisme sur les seuls
   épisodes de développement ; sortie au gabarit fermé des proposeurs ; une espèce de proposeur de plus, comparée **à coût
   apparié** à un témoin « Kimi, meilleur de N », jugée sur l'oracle et le coût. **Confiance 0,55.** L'Agentic Scientist ensuite,
   sur preuve (N-045, point 4). POPPER : hors du rôle, utile à N-064 (c). Swarm : non. Coscientist de Boiko et al. : hors sujet.
5. **Le branchement ne revendique rien** (section 3).

## 1. Le rôle

**Ce qu'il est.** Un proposeur qui fait des expériences : il reçoit la **vue servie aux proposeurs, et elle seule** — description
publique du monde, grammaire des lois, lois retenues sans verdict, épisodes de développement (`contexte_du_proposeur`,
`pole/tour_ferme_v64.py` l. 599-606, `35a8294e…`) —, expérimente sur ces épisodes, et rend **au plus six fiches au gabarit
fermé** `{enonce, loi_predictive}` (`CONSIGNE_PROPOSEUR`, même fichier l. 213-218 ; garde 8 et gardien mécanique ensuite).
Dans l'orchestrateur, c'est une **commande externe** comme les proposeurs Kimi et Argon : consigne sur l'entrée standard,
dernière ligne JSON `{texte, cout_usd > 0, modele_servi, usage}` (`pole/adaptateurs.py` l. 703-719 ; `pole/adaptateur_commande_v64.py`,
code 4 « rien envoyé »). Le **retour lu** par l'orchestrateur est cette ligne, et elle seule ; les journaux du scientifique sont
gardés pour l'audit, jamais servis à un juge ni à un proposeur.

**Ce qu'il ne fait jamais.** Il ne juge pas. Son classement interne (Elo de Kaimen, note de la grille de l'Agentic Scientist,
valeurs p de POPPER) ne choisit que **ce qu'il soumet**, jamais ce qui survit. La promotion reste au juge statistique de
l'orchestrateur, sur tirages frais, à partir d'un engagement scellé, contre le nul des lois connues, sous contrôle de la
multiplicité (O2 resserrée, N-064) ; la survie, au test de mort **imposé**, exécuté dans le bac, verdict calculé par le noyau sur
le fichier brut (`pole/tests_de_mort_v5.py`, `da524871…`) ; la sélection, à l'étage v57. Il ne reçoit **jamais** : un verdict,
l'oracle, la tranche du test de mort, les tirages frais, une loi plantée, la description du juge. Recevoir les verdicts ferait de
lui un attaquant du type d'A1, bras « retour » (O12) : hors de ce rôle ; le bras d'attaque n'est pas le mandat de la mère, et
faire d'un tel proposeur une menace est le rôle 3 de N-065, à trancher par Lazar.

**Ce qu'il ne remplace pas.** L'expérimentateur actuel des tests de mort (Kimi par commande externe, « Tu n'as aucun outil »,
scripts exécutés par le noyau, `tests_de_mort_v5.py` l. 93-110) reste en place : le test imposé doit rester fixe, et un
scientifique libre peut toucher à ses propres limites (incident de The AI Scientist v1 : le code modifié pour allonger sa limite
de temps, PDF v1 p. 19, vérifié dans `verification-pieces-primaires-v1.md`, ligne 53).

**Invariants.** N-053 : aucun score d'un moniteur du programme (sonde, juge) dans sa sélection — tenu par construction s'il n'a
accès à rien d'autre que la vue ; O9 : sa mémoire ne porte aucun verdict (garde « vue sans verdict » de la v59 et garde 23 de la
v66, réutilisées). « Claude exclu par construction » (texte scellé v66, l. 149 et 291-294 ; `46d7545b…`) : les quatre candidats
ont un modèle Claude ou OpenAI **par défaut** (Kaimen : `config/default.toml` l. 97-107 ; Agentic Scientist : agent `claude`,
README l. 123-125 ; POPPER : `popper/utils.py` l. 17-20 ; Swarm : `gpt-4.1`, `main.py` l. 250) ; chaque défaut est remplacé, et
le relais (`--modeles-permis kimi-k3.1-pro`, barrière du modèle servi) refuse tout autre modèle : échec fermé.

**Place dans la composition (N-045).** Une espèce de plus, `SCIENTIFIQUE:<système>@<commit>/<modèle>`, qui tient le rôle
« proposeur-expérimentateur » ; sa part de budget et son modèle sont, à terme, des variables apprises ; son **coût par
génération** entre dans `historique` (point 2) ; sa **nécessité** est une sortie mesurée (ablation, point 3) ; la composition se
juge sur l'oracle du monde planté et le coût, jamais sur le verdict du juge (N-058) ; **le bon marché d'abord** (point 4) : le
bras « scientifique » doit battre, à budget égal, le témoin « un modèle, vote à k » ou « meilleur de N » de Kimi avant toute
voie plus chère. Mémoire entre générations : base neuve à chaque génération dans le premier dessin ; une mémoire propre gardée
(N-045, point 5 : héritage récompensé) est un bras ultérieur, sous la même garde « aucun verdict ».

## 2. Candidats

Licences et commits relus aujourd'hui (manifeste) ; têtes inchangées depuis les lectures du 9 novembre (Kaimen, Swarm) et du
30 octobre (Agentic Scientist). « Vérif. » renvoie à `verification-pieces-primaires-v1.md` (`6030e381…`), lignes numérotées.

| | **Kaimen-Inc/Co-Scientist** `cef5bcf` | **The-Swarm-Corporation/AI-CoScientist** `6fdd532` | **SakanaAI/AI-Scientist-v3** (« The Agentic Scientist ») `df83138` | **snap-stanford/POPPER** `5961186` |
|---|---|---|---|---|
| licence lue au commit | Apache 2.0 (`LICENSE`, `c71d239d…` ; README l. 533) | MIT (`LICENSE`, `c12e3f45…`) ; dépendance `swarms = "*"` non épinglée (17.0.0, Apache-2.0, `litellm==1.76.1`) | Apache-2.0 (vérif. n° 23) ; stade « Alpha » | **aucun fichier de licence** (404) ; `license='MIT'` déclaré dans `setup.py` l. 28 |
| ce qu'il fait | superviseur ; génération, réflexion, tournoi Elo, évolution, proximité, méta-revue (README l. 13-22) | les mêmes agents, **un seul modèle**, aucun outil (`main.py` l. 312-389) | à partir d'un `task.md` et d'un évaluateur : idées, expériences, évaluation, itération ; ablations ; évaluation finale scellée ; article (README l. 21-25) | valide **une hypothèse donnée** : conçoit et exécute des expériences de falsification, valeurs p combinées en valeurs e (`popper.py` l. 73-77) |
| moteur exigé ; hors Claude | appel de fonctions **exigé** (README l. 276) ; `openai_compatible` + `base_url` (l. 217 ; `openai_client.py` l. 199-207), `chat.completions.create` **sans flux** (l. 248), choix d'outil forcé traduit (l. 378-393) → **Kimi par le relais v3 tel quel** ; Argon : préréglage `gemini` par l'adresse compatible OpenAI de Google, que notre relais Gemini ne sert pas | LiteLLM (`swarms`), sans flux par défaut, `base_url` admis (`litellm_wrapper.py` l. 222, 238) → Kimi par le relais v3 | agents `pi`, `opencode` : fournisseur `moonshot`, clé `MOONSHOT_API_KEY` transmise (`container_agent.sh` l. 188-235) → Kimi ; agent `gemini` → Argon (`GEMINI_API_KEY`, l. 185-186) ; tous **en flux** (non vérifié pour chacun) → relais neuf ; l'article cite Kimi (PDF v3 p. 15, vérif. n° 43) | « modèle local » : tout nom hors `claude-`, `gpt-`, `o1` → `openai.Client(base_url="http://127.0.0.1:{port}/v1")` (`utils.py` l. 17-41), outils liés à la consigne système, sans flux → **Kimi par le relais v3 tel quel** |
| ce qu'il exécute, où | rien au commit ; réseau : `web_fetch`, PubMed, arXiv, Europe PMC, recherche Web si clé (`registry.py` l. 21-44) ; plongements Voyage ou OpenAI, sinon empreinte locale (README l. 366-385) ; serveur MCP (protocole d'outils) lancé par appel pour les seuls modes « interface en ligne de commande » | rien ; réseau : appels de modèle seulement ; module de télémétrie qui collecte l'identité de la machine (`swarms/telemetry/main.py`, envoi non vérifié) | commandes arbitraires des agents (`--allow yolo`) dans des conteneurs, réseau `host` par défaut, Web consulté (vérif. n° 30, 36 ; PDF v3 p. 22) ; évaluateur sans réseau | `exec` du code écrit par le modèle **dans son propre processus** (`agent.py` l. 325, 365) ; téléchargement d'un jeu de Harvard Dataverse si `bio_database/` manque, même en mode « custom » (`popper.py` l. 44-46, 250-276) |
| branchement sur l'orchestrateur | moyen : outil neuf « expérience » (classe `Tool`) vers l'exécuteur `bwrap` de l'organisme ; liste d'outils réduite (`AGENT_TOOLS`) ; champ `loi_predictive` ajouté à `record_hypothesis` (absent, `schemas.py` l. 15-68 ; `citations` exigé, vide permis) ; gabarits Jinja des consignes ; commande externe qui lit la base SQLite et rend six fiches | faible en code, mais rien d'expérimental : il faudrait écrire l'outil, la sortie structurée et la boucle ; c'est réécrire | lourd : démon Docker, image dérivée (réglages de `pi`/`opencode` vers le relais, clé factice), réseau interne sans route, relais Kimi v5 en flux, tâche (`task.md`, évaluateur sur une partie des épisodes de développement), phases réduites à l'investigation ; architecture de la note v3 (`1ce823a7…`, § 2) reprise sans mandataire Web | moyen : tout le processus sous `bwrap` ; données en CSV, `bio_database/` vide ; mais il ne propose rien : il lui faut les lois d'un autre proposeur |
| risques propres (la fuite des lois plantées, commune aux quatre : § 0, point 3, et § 4, point 3) | ses valeurs Claude par défaut survivent à une fusion partielle de la configuration (README l. 183) ; outils réseau si la liste n'est pas réduite ; nouveauté jugée « relative to the cited literature » sans littérature | dépendance lourde non épinglée ; hypothèses en texte libre (traducteur vers une loi = un modèle de plus) | exécution à pleins droits ; clés lisibles des agents ; Web ; un agent a changé le protocole d'évaluation (PDF v3 p. 21, vérif. n° 48) ; jeune, aucune évaluation tierce connue | `exec` sans bac ; c'est un **juge** par conception (règle de valeurs e, `agent.py` l. 123-150) : n'en garder que les expériences, jamais la décision |

**Écartés ou hors sujet.** *Coscientist* de Boiko, MacKnight, Kline et Gomes (« Autonomous chemical research with large language
models », Nature, 2023 ; titre et auteurs lus dans le README de `gomesgroup/coscientist` au commit `417e82b`, revue et pages de
mémoire, non vérifié) : **hors sujet** — chimie en laboratoire robotisé et recherche Web ; le dépôt ne livre que des
informations supplémentaires et une « simple implementation » ; licence Apache 2.0 **avec Commons Clause**, usage commercial
restreint (README l. 14-17). *The AI Scientist v2* : licence à restrictions d'usage et phase d'expériences par Bedrock seulement
(vérif. n° 1 et 7). *Hypothesis Generation* de Google Labs : accès automatisé interdit par ses conditions
(`protocole-bras-labs-v1.md`, § 1). Agent Laboratory, CodeScientist, AI-Researcher : écartés pour les motifs de
`choix-ia-scientifique-v1.md`, § 1.1.

### 2.1 Coût estimé par génération (une session par génération ; calculs sur hypothèses, à mesurer)

**Formule** : C = E × p_e + S × p_s + H × p_h, où E et S sont les jetons d'entrée (cache compris, compté au prix d'entrée) et
de sortie (raisonnement compris) **sommés sur tous les appels de la génération**, H les heures de machine en plus, p_h leur prix.
**Prix** (texte scellé v66, § 12.3, point 6, d'après le devis `60643868…`, section 2, « à vérifier ») : Kimi `kimi-k3.1-pro`,
p_e = 2 et p_s = 10 dollars par million de jetons ; Argon, 10 et 50. **Repère** : le devis v66 attend ≈ 1,5 à 2 dollars pour
toute la course, ≈ 31 appels (calcul : 5 à 7 cents par appel en moyenne, expérimentateur compris).

| candidat (sur Kimi) | hypothèses (supposé) | E | S | C par génération |
|---|---|---|---|---|
| Kaimen, 12 idées, 4 matchs par idée, 3 évolutions | 60 à 120 appels ; 6 000 à 20 000 jetons d'entrée et 1 000 à 6 000 de sortie par appel (200 épisodes de développement ≈ 3 000 jetons, grammaire, résultats d'expériences) | 0,36 à 2,4 M | 0,06 à 0,72 M | **≈ 1,3 à 12 dollars** ; machine : négligeable (expériences de quelques secondes sur l'exécuteur de l'organisme) |
| Swarm, 2 itérations, 6 hypothèses | 30 à 80 appels ; 3 000 à 10 000 et 1 000 à 4 000 jetons | 0,09 à 0,8 M | 0,03 à 0,32 M | ≈ 0,5 à 4,8 dollars (sans expérience) |
| Agentic Scientist, investigation seule, 3 cycles (défaut d'`agsci run`, note v3, ligne 4a) | par cycle 0,5 à 3 M d'entrée et 20 000 à 100 000 de sortie | 1,5 à 9 M | 0,06 à 0,3 M | **≈ 3,6 à 21 dollars** + machine 0,45 à 1,1 euro (Hetzner CCX33, 0,2227 euro de l'heure, 2 à 5 heures ; prix public lu le 30 octobre, note v3, § 3.2, non relu) |
| POPPER, 6 à 12 lois éprouvées | par loi, 5 tests (défaut) × 5 à 10 appels ; 3 000 à 12 000 et 500 à 2 000 jetons par appel | 0,45 à 7,2 M | 0,08 à 1,2 M | ≈ 1,7 à 26 dollars |

Lecture : un scientifique coûte **de quelque 7 à 500 fois** une session de proposeur (calcul sur ces hypothèses) ; à coût apparié, le témoin « Kimi, meilleur
de N » recevrait des dizaines de sessions. À régler au préenregistrement : à coût égal, les bras ne soumettent pas le même nombre
de fiches au juge, donc pas la même multiplicité (m) ; options : même nombre de fiches soumises par bras (le témoin choisit les
siennes par une règle mécanique sur les épisodes de développement), ou m propre à chaque bras, lu sur l'oracle.

## 3. Antériorité (R8) : ce que le branchement revendiquerait

Statuts : notes `note-anteriorite-co-scientist-v1.md` (`08a3738a…`, § 5) et `note-anteriorite-popper-evaluator-v1.md`
(`d1ab7049…`, § 7), dans l'état fixé par N-064.

| revendication | statut | ce que fait le branchement | revendiqué ? |
|---|---|---|---|
| O1 le rôle qui produit ne tient pas la clé qui évalue | voisine | tenue : le classement interne du scientifique ne décide d'aucune survie | non |
| O2 statistique calculée par l'orchestrateur, engagement scellé, nul des lois connues, multiplicité contrôlée | occupée en partie (POPPER) | inchangée ; valeurs p, valeurs e, notes et Elo du scientifique sont au plus des témoins | non |
| O3, O4, O17 | voisine ; non occupée ; non occupée | héritées de la chaîne, rien d'ajouté | non |
| O8 proposeurs de plusieurs fournisseurs | non occupée | le scientifique ajoute un harnais, pas un fournisseur (Kimi l'est déjà) | non |
| O9 mémoire sans verdicts | voisine | tenue par la vue et la garde 23 ; c'est une contrainte, pas un apport | non |
| O11, O12 tricheurs, attaque de Goodhart | occupées dans leur principe (Dwork et al. ; Blum et Hardt) | un scientifique nourri des verdicts serait une variante d'A1 : hors mandat (rôle 3) | non |
| O13, O14 tests de mort, sélection par leur verdict | voisines | ses expériences sont exploratoires ; le test de mort reste imposé | non |
| O16 pont fiche → loi prédictive | voisine | gabarit fermé exigé à la sortie ; aucun traducteur à modèle | non |
| O18 à O20 juges éprouvés sur vérité plantée | voisine à occupée dans son principe | le branchement mesure le **scientifique**, non le juge | non |

**Zones occupées** : un agent qui conçoit et exécute ses expériences (The AI Scientist v1 à v3, POPPER, Agent Laboratory,
CodeScientist) ; générer-classer-faire évoluer par tournoi (Co-Scientist) ; un évaluateur scellé hors des agents dans une IA
scientifique (Agentic Scientist, README l. 299-303, vérif. n° 42) ; des e-valeurs posées hors des agents (POPPER, p. 2-5, algorithme 1
p. 14, `a3c4b370…`). **Zone séduisante, à vérifier plus durement** : « mesurer, sur des mondes plantés à vérité connue, les vraies et
fausses découvertes d'un scientifique du marché filtrées par un juge statistique hors des agents ». Voisins connus de nom
seulement, non lus ici : DiscoveryBench (tâches synthétiques à relations plantées, de mémoire), BLADE, MLR-Bench et Luo, Kasirzadeh
et Shah (2025) (`choix-ia-scientifique-v1.md`, § 2, non vérifié R7), les évaluations de POPPER sur négatifs permutés (p. 7, d'après
la note d'antériorité). Toute revendication sur cette zone est une **modification de revendication** : nœud, après lecture à part.
**Citations obligatoires** (N-064, point 4 ; références recopiées de N-064, non relues pour cette note) : POPPER (Huang, Jin, Li,
Li, Candès, Leskovec, ICML 2025, PMLR 267, p. 2-5 et algorithme 1 p. 14) ; Dwork et al. (arXiv 1506.02629, p. 20-21) ; Blum et
Hardt, « The Ladder » (arXiv 1502.04585, p. 10-12) ; Co-Scientist (Nature 655, p. 487-496) ; et, pour ce rôle, The Agentic
Scientist (arXiv 2610.18933, PDF `cb170b54…`).

## 4. Recommandation

**Décision proposée** : quel scientifique du marché préparer comme proposeur-expérimentateur, pour un branchement après la course
v66. **Enjeu** : un pôle qui expérimente vraiment, sans fuite du monde planté, sans juge à modèle dans la chaîne, et dont la
valeur se mesure à coût égal.

| option | avantage | inconvénient |
|---|---|---|
| **(a) Kaimen `cef5bcf`, Kimi, outil « expérience » vers l'exécuteur de l'organisme** | méthode Co-Scientist la plus fidèle des deux réécritures (étude du juge-tournoi) ; relais v3 sans changement ; aucun code du modèle exécuté hors de l'exécuteur déjà éprouvé ; Apache 2.0 | trois retouches de code tiers (outils, schéma, consignes) ; Co-Scientist sans sa littérature ; aucune évaluation tierce |
| (b) Agentic Scientist, `pi` ou `opencode` sur Kimi | exécute vraiment, conçu pour itérer contre un évaluateur | Docker, relais en flux, agents à pleins droits, jeune ; plus cher par génération (≈ 3,6 à 21 dollars contre 1,3 à 12, supposé) |
| (c) aucun scientifique du marché ; élargir le proposeur Kimi (vote à k) | rien de tiers | ne répond pas à la question de Lazar |

**Recommandation : (a), confiance 0,55** ; (b) seulement si (a) bat le témoin à coût apparié (N-045, point 4) ; POPPER réservé à
l'option (c) de la note POPPER (variante où l'agent calcule sa propre valeur p, contre le banc de tricheurs), si Lazar la veut ;
Swarm écarté (dominé par Kaimen sur chaque critère, sauf la licence, libre dans les deux cas).
**Défaut sous 48 heures** : préparation hors ligne de (a) seulement (code, essais contre un amont factice, zéro dépense) ; toute
dépense attend un GO.

**Ce qu'il faut pour brancher, dans l'ordre** :
1. **Verdict scellé de la course v66** (R13) d'issue C1 ou C7 ; sinon, corriger la chaîne d'abord.
2. **Code v67** (noms neufs, R12, au-dessus de la tête v66 `7e415cba`) : commande `commande_scientifique_kaimen_v1.py` (consigne
   et vue sur l'entrée, dossier neuf par génération, Kaimen sous `bwrap` sans réseau, sortie au gabarit fermé, coût lu au journal
   du relais pour la session, jamais l'estimation de Kaimen) ; un **pont** de la prise Unix du bac vers le relais local
   (`--unshare-net` coupe aussi la boucle locale : pont prévu dans `choix-ia-scientifique-v1.md`, § 4.2, point 3, jamais écrit) ;
   fourche de Kaimen épinglée, retouches en un correctif empreinté, dépendances en roues à empreintes installées hors ligne (après
   GO) ; plongements « hash ».
3. **Gardes neuves, chacune sur un cas sain et un artefact (R5)** : réseau (le relais répond ; `github.com`, `api.moonshot.ai`,
   `openrouter.ai`, `pypi.org`, `dataverse.harvard.edu` injoignables depuis le bac) ; aucune variable de clé dans le bac ; chaque
   clé de `[models]` égale à `kimi-k3.1-pro` avant le lancement, aucun binaire `claude` ni `codex` ; vue sans verdict (reprise) ;
   recherche de la loi plantée étendue aux fichiers de travail et aux journaux du scientifique (mesure C16 de la v62) ; plafonds
   par session au relais et en durée ; base SQLite neuve à chaque génération.
4. **Préenregistrement scellé et contre-lu (R1, R2)** : bras base (proposeurs de la v66), base + scientifique, base + témoin
   « Kimi, meilleur de N » à coût apparié ; mêmes mondes et mêmes lois plantées ; issues lues sur l'oracle (vraies et fausses
   découvertes par dollar, N-058), fausses promotions, coût par rôle ; pilote de bruit A/A (N-045, point 6) ; règle de multiplicité
   (§ 2.1) ; Claude exclu de tout rôle.
5. **Devis** sur une mesure : un essai court (une génération, plafond bas) pour lire E et S réels, puis le devis ; **GO de calcul**
   inscrit (GO-2026-11-10-11 ne couvre que la course v66) ; machine à `bwrap` (Hetzner, sous GO).

**À trancher par Lazar** : le choix (a), (b) ou (c) ; la dépense ; le scientifique **sans Web ni littérature** (fidélité perdue
contre fuite évitée ; je recommande sans) ; pas de test de mort écrit par le scientifique dans le premier dessin ; le rôle 3 reste
séparé ; toute mention dans le dépôt public de l'organisme est une publication.

## 5. Réserves

- Coûts : hypothèses de jetons sans pièce ; prix Kimi et Argon « à vérifier » ; à remplacer par une mesure avant tout devis.
- Non vérifié : que `kimi-k3.1-pro` accepte le choix d'outil forcé par nom de Kaimen (le schéma de la documentation archivée le
  permet, `doc-moonshot-lue-2026-10-30-v1/api_chat.md` l. 1235-1260, `67b8b5fd…`, à éprouver) ; que `pi`, `opencode` et `gemini`
  lisent en flux ; que l'adresse de base de `pi` et `opencode` se règle par leurs fichiers de configuration ; ce que la télémétrie
  de `swarms` envoie ; la licence réelle de POPPER (aucun fichier).
- Arborescences des dépôts non listées (interface GitHub refusée, 403) : fichiers trouvés par les chemins de la documentation ;
  non lus : `science-skills` de Kaimen, le module MCP, les variantes et le post-hoc de l'Agentic Scientist.
- Fidélité : Kaimen privé de littérature n'est plus Co-Scientist ; le bras mesure « Co-Scientist sans littérature, avec
  expériences ». Le dire dans tout texte qui en rend compte.

Version 1 ; jamais réécrite (R12). Fin de rédaction : 11 novembre 2026, 14:37:20 UTC (`date -u`), avant le scellement.
