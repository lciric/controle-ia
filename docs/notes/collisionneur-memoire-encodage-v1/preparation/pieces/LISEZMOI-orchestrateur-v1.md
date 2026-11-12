# Orchestrateur du pôle « scientifique automatique », version 0 — LISEZMOI v1

Lignée conv-audit, sous-agent. Écrit le 2026-10-26T19:49:33Z (heure lue sur `date -u` dans la commande qui écrit cette ligne).
Régime exploratoire : tout ce qui suit est mesuré **en simulation** ; rien n'est opposable ; rien n'a été contre-lu par
un sous-agent neuf (R2 et R13 restent à faire : les sous-agents étaient interdits ici).

## Verdict

- Le paquet `pole/` est écrit et marche de bout en bout **en simulation**. Il couvre le brief (fiche gelée par empreinte,
  adaptateurs simulé et Claude Agent SDK, expérimentateur, vérificateur d'un autre modèle, sélection par sévérité, témoins,
  recombinaison bisociative corrigée, boucle, ligne de commande), le premier ajout (`memoire.py`), le second (sélection par
  pari, contrôles fatals, duel des trois bras, relais de clé) et le troisième (nul augmenté des filles, tricheurs scriptés).
- **83 essais passent** (`python -I -m unittest`, environ 60 secondes). Première expérience : T1a, T6 et les sept tricheurs
  scriptés passent (critère non invalidé, en simulation) ; **T1b montre que la bibliothèque nulle ne suffit pas contre une
  dérive non modélisée** (65,2 % de promotions d'une loi aveugle qui suit la dérive).
- Le moteur réel **n'est pas testé** (seules ses options et sa garde le sont). **Incident** : le paquet `claude_agent_sdk`
  est installé dans cet environnement, contrairement au brief ; un essai a lancé une fois l'outil Claude Code réel ; arrêté
  par son identifiant de processus ; un verrou d'armement l'interdit désormais (détail plus bas).

## Incident : un essai a lancé le moteur réel

- Cause : l'essai « paquet absent → erreur claire » appelait `AdaptateurClaudeSDK.lancer`, en supposant le paquet absent. Il
  est installé (`site-packages/claude_agent_sdk`), donc `query()` a démarré l'outil Claude Code embarqué, avec pour dossier
  le dossier `sortie/`, `max_turns` 3 et `max_budget_usd` 1,0.
- Ce que l'outil recevait : `ANTHROPIC_BASE_URL=http://127.0.0.1:8787` (relais local **inexistant**) et le jeton factice
  `relais-local-sans-cle` à la place de la clé. Ses appels à l'interface de programmation visaient donc un port local fermé.
  Mon code n'a lu ni écrit aucune clé. Je ne peux pas vérifier si l'outil a tenté d'autres connexions (télémétrie, mises à
  jour) ni s'il a écrit ses fichiers de session dans le dossier personnel (lecture hors de `fournis/` interdite).
- Arrêt (R10) : processus 6203, orphelin, arrêté par son identifiant (`kill -TERM 6203`), puis vérifié absent ; aucun autre
  processus de l'outil embarqué ne restait. Deux lancements antérieurs du même essai ont pu démarrer l'outil brièvement ;
  ils se sont terminés avec leur processus parent (vérifié : aucun processus restant).
- Correctif : l'adaptateur réel n'est lancé que s'il est **armé** (`arme=True`, posé seulement par la ligne de commande avec
  `--confirmer-moteur-reel`) ; l'ordre est : absence de variable de clé → armement → import du paquet. Les essais rendent le
  paquet introuvable (`sys.modules["claude_agent_sdk"] = None`) avant d'armer. Après correctif : aucun lancement réel.

## Écarts au brief, et pourquoi

1. `python -I -m pole …` ne peut pas marcher : sous `-I`, Python n'ajoute pas le dossier courant au chemin d'import
   (option `-P` impliquée depuis la version 3.11 ; vérifié : « No module named »). On lance **`python -I pole …` depuis
   `sortie/`** (le paquet exécuté comme dossier ; `pole/__main__.py` remet le parent dans le chemin). Sans `-I`,
   `python -m pole` marche depuis `sortie/`. Les essais se lancent bien par `python -I -m unittest` (la découverte ajoute
   elle-même le dossier).
2. R9 (graines par `numpy.random.SeedSequence`) : le brief impose la bibliothèque standard ; les graines dérivent de
   SHA-256(« graine|étiquettes ») (`outils.graine_derivee`), règle écrite dans chaque manifeste.
3. En sélection par pari, la sévérité d'une fiche est l'α du pôle : une fiche qui annonce autre chose est refusée.
4. La vue de la fiche donnée à l'expérimentateur exclut la vérité du témoin, la source et les parents ; une seconde
   empreinte (« complète ») gèle ces champs privés, revérifiée avant toute mesure de qualité.

## Architecture (`pole/`)

| module | rôle |
|---|---|
| `fiche.py` | fiche d'hypothèse (dataclass, validation), vue publique, empreinte du test (SHA-256 du JSON canonique trié, qui est aussi le contenu exact de `fiche.json`), empreinte complète, registre de gel |
| `adaptateurs.py` | interface `Adaptateur.lancer(role, consigne, dossier, budget_usd, max_tours) -> Resultat` ; `construire_options(...)` (fonction pure) ; `AdaptateurClaudeSDK` (import paresseux, verrou d'armement) |
| `garde_outils.py` | crochet `PreToolUse` : refuse les commandes qui sortent du dossier, lisent l'environnement, touchent au réseau ou élèvent les droits ; refuse Read, Write, Edit hors du dossier et tout autre outil |
| `relais.py` | relais de clé tenu par le noyau : interface, adresse locale obligatoire, variables de l'agent (point d'accès vers le relais, jeton factice), relais simulé |
| `simulation.py` | monde à vérité cachée ; agents simulés : expérimentateur honnête, tricheur « test changé », tricheur « sans calcul », vérificateur honnête ou complaisant, recombinaison, synthèse ; le code d'expérience est réellement écrit, exécuté et rejoué |
| `cycle.py` | une génération : gel, expérimentateurs en parallèle par vagues, budget réservé avant chaque lancement, vérificateur d'un autre modèle, sélection (aptitude = −ln sévérité), mesure de qualité sur les témoins ; modes « seuil » et « pari » |
| `selection_pari.py` | lois prédictives, bibliothèque nulle 𝓛, engagement gelé, tirages frais liés à l'engagement, richesse W et promotion (calculées par l'orchestrateur), nul augmenté des filles, part de calibrage, marge 2δ₀ |
| `controles_pari.py`, `duel_pari.py`, `experience_critere.py` | première expérience : contrôles fatals, tricheurs scriptés, duel des trois bras, étalonnage A/A |
| `recombinaison.py` | noyau S_ij = ⟨d_i,d_j⟩², L = diag(q) S diag(q) + γI vérifié par Cholesky, tirage glouton du déterminant maximal, filtre de compatibilité, consigne de fusion, validation de la fille |
| `memoire.py` | index de l'archive, garde de redite (Jaccard des 3-grammes), bibliothèque de protocoles, registre de calibration (Brier), leçons |
| `pole.py`, `__main__.py`, `ablation.py` | boucle, témoins plantés, arrêts, journal scellé par génération, archive complète, manifeste, ligne de commande, ablation de la mémoire |
| `caviardage.py`, `outils.py` | caviardage des secrets avant toute écriture ; JSON canonique, écriture scellée sans écrasement, graines, blocs JSON |

Choix du dénominateur (sélection par pari) : **maximum de vraisemblance a posteriori sur 𝓛, ajusté sur les tirages frais
eux-mêmes** (inférence universelle). Si les issues suivent une loi de 𝓛, W_t reste sous une martingale de test ; l'inégalité
de Ville borne la promotion par α, même lue à tout instant. Les ajustements « sur une part séparée » et « en ligne » sont
gardés comme artefacts : T6 montre qu'ils laissent passer un parasite de Kelly (43,9 % et 90,3 %). Pour une fille, le nul
est augmenté de chaque parent, de chaque parent mélangé à une loi aveugle, du mélange des parents (poids maximal a posteriori
sur une grille, plus le poids ajusté sur la part de calibrage), de l'enveloppe harmonique et des concaténations si/sinon sur
les partitions déclarées ; promotion si W ≥ 1/α **et** gain moyen de score logarithmique sur la meilleure enveloppe ≥ 2δ₀
(δ₀ = 0,01 nat par tirage par défaut : valeur provisoire, à fixer par Lazar).

## Lancer en simulation (depuis `sortie/`)

```bash
python3 -I -m unittest                                   # 83 essais, environ 60 secondes
python3 -I pole --experience-critere --sortie DOSSIER --horodatage "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
python3 -I pole --moteur simule --population exemples/population-demo-v1.json --temoins exemples/temoins-demo-v1.json \
  --monde-simule exemples/monde-demo-v1.json --generations 3 --budget-usd 30 --sortie DOSSIER \
  --taux-tricheurs 0.08 --p-echec 0.08 --p-redite 0.35 --p-sans-prediction 0.15 --horodatage "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
# sélection par pari : --selection pari avec exemples/*-pari-demo-v1.json ; ablation : --ablation-memoire --ablation-graines 20
```

Le dossier de sortie doit être absent ou vide (rien n'est jamais écrasé). Chaque fichier écrit a son compagnon `.sha256`.

## Première expérience : le critère par pari (simulation à vérité connue)

Source : `demo/experience-critere-v1/controles-fatals-v1.json` (`2b86b37f…`) et `duel-trois-bras-v1.json` (`62ad6ab9…`),
manifeste `manifeste.json` (`0bf0fc23…`) ; graine 20261026 ; 1 000 répétitions par contrôle ; 200 tirages frais ; α = 0,05.

- **T1a** (nul dans 𝓛) : 18, 14 et 3 promotions sur 1 000 (marginale, uniforme, moyenne glissante) → passe.
- **T6** (parasite de Kelly 0,95·p0 + 0,05·marginale d'entraînement) : 0 sur 1 000 → passe (par construction du dénominateur).
- **Tricheurs scriptés** (forme, copie renommée, enveloppe aveugle, fille constante, pari couvert, adimensionnement, jargon
  rare ; mondes tirés parmi quatre) : 0 sur 1 000 chacun → passe ; une fille réellement neuve est promue 993 fois sur 1 000.
  Réserve : ces tricheurs sont rejetés **par construction**, car chacun est une forme incluse dans le nul augmenté ; un
  tricheur hors de ces formes (partition non déclarée, enveloppe d'un autre type) n'est pas couvert.
- **T1b** (dérive non modélisée) : oracle aveugle de la dérive promu 652 fois sur 1 000 (> 2α) → **la bibliothèque ne suffit
  pas** ; il faut une famille de dérive dans 𝓛 ou borner les mondes où le pôle s'applique. Loi fausse sous dérive : 7 sur 1 000.
- **T3** (paris couverts) : composante nette fausse 0 et 12 sur 1 000 (ε = 0,05 et 0,2) → passe ; nette vraie 913 et 996.
- **T9** (disjonction partitionnée) : 0 sur 1 000 contre le nul augmenté ; contre 𝓛 seul, gain médian de 98,5 nats sur le
  meilleur parent (c'est pourquoi le nul des filles doit contenir les concaténations des parents).
- Artefacts (critères cassés) tous détectés : 𝓛 réduite à l'uniforme 957, part séparée 439, en ligne 903, filles sans
  parents dans le nul 474 (forme) et 700 (enveloppe). La détection de la « part séparée » demande un horizon de l'ordre de
  200 tirages (à 40 tirages, elle n'est pas vue).
- **Duel** (40 hypothèses par type) : fausses éliminées 1,000 / 1,000 / 0,808 (bras 1, 2, 3) ; vraies gardées 0,500 / 0,512
  / 1,000 ; le bras 3 garde 47,5 % des paris couverts à composante nette fausse. Plancher A/A : 0 et 0,0125. Règle d'arrêt :
  « réfutateur superflu » vrai **dans cette simulation** ; le plancher repose sur une seule paire A/A (0,0125 = une hypothèse
  sur 80) ; les bras 1 et 2 ne promeuvent presque pas les paris couverts à composante vraie (7,5 % et 5 % à 120 tirages).

## Démonstrations (simulation)

- `demo/demonstration-v1/` (mode seuil ; trois générations ; six fiches ; `bilan.json` `149239de…`) : 3 témoins faux testés,
  aucun gardé ; 4 vrais, aucun éliminé ; tricheurs vus (verdict sans calcul → indécise, test changé → rejetée) ; une fiche
  retirée après deux essais indécis ; filtre de compatibilité actif (« discret » contre « continu ») ; 8,6 dollars simulés.
- `demo/demonstration-pari-v1/` (mode pari ; trois générations ; `bilan.json` `1c6838c2…`) : lancé **sans tricheurs** pour
  montrer les filles jugées contre le nul augmenté (gains 0,19, 0,61, 0,17 nat pour les promues, −0,44 pour une éliminée) ;
  deux redites refusées par la mémoire ; témoins : 0 faux gardé, 0 vrai éliminé.
- `demo/ablation-memoire-v1/` (20 graines appariées, trois générations ; `comparaison-memoire-v1.json` `91b5742b…` ; archives
  brutes zippées `archives-par-graine-v1.zip` `34e6a312…`) : une seule redite d'éliminée proposée sur 26 fiches nouvelles ;
  testée sans mémoire, refusée avec ; témoins identiques dans les deux bras ; la mémoire coûte l'agent de synthèse (152,7
  contre 150,8 dollars simulés). **Aucune conclusion** : les agents simulés ne lisent pas la mémoire, l'écart ne mesure que
  le mécanisme, et l'effectif de redites est trop petit.
- Les populations de démonstration ont été retouchées (opérateurs partagés) pour que la recombinaison ait des ponts ; ce sont
  des illustrations de mécanique, pas des mesures.

## Ce qu'il faut à l'opérateur pour le moteur réel

1. Une instance avec Docker ou un bac à sable (Linux), sans autre secret ; `pip install claude-agent-sdk` (lu ici : source
   0.2.174) ; Python ≥ 3.10.
2. **Un relais local tenu par le noyau** (autre processus, idéalement autre utilisateur ou conteneur) qui écoute sur
   127.0.0.1, ajoute aux requêtes sortantes **une clé à plafond de dépense** qu'il est seul à détenir, et refuse tout autre
   jeton que le jeton factice. L'environnement de l'orchestrateur ne doit contenir **aucune variable de clé** (l'adaptateur
   refuse de démarrer sinon) ; l'agent reçoit `ANTHROPIC_BASE_URL` pointé vers le relais et le jeton factice. Aucun code de
   relais réel n'est écrit ici (interface et simulation seulement). À ajouter dans le relais : un jeton par exécution et un
   plafond par session, car une commande de l'agent qui atteindrait le port local pourrait dépenser par le relais.
3. Lancement : `python3 -I pole --moteur claude-sdk --confirmer-moteur-reel --url-relais http://127.0.0.1:PORT
   --modele-experimentateur M1 --modele-verificateur M2 … --population … --temoins … --budget-usd X --sortie DOSSIER
   --horodatage "$(date -u +%Y-%m-%dT%H:%M:%SZ)"` (le vérificateur doit être d'un autre modèle).
4. Options de chaque agent : dossier de l'expérience pour répertoire courant ; outils Read, Write, Edit, Bash autorisés ;
   WebFetch, WebSearch, Agent, Task et autres interdits ; mode de permission `dontAsk` ; aucun réglage de fichier chargé ;
   invites transmises telles quelles ; bac à sable activé, commandes hors bac à sable interdites, aucun domaine réseau ;
   plafond `max_budget_usd` par agent (l'outil peut le dépasser d'un appel), plafond par génération et plafond total.

## Limites connues et risques

- Le moteur réel n'a jamais tourné ici : le format exact des messages, les coûts déclarés et le comportement du bac à sable
  restent à éprouver sur l'instance, d'abord sur une génération de deux fiches.
- La garde `PreToolUse` est une barrière par motifs : un chemin encodé ou un interpréteur détourné peut la franchir ; la
  vraie barrière est le bac à sable et l'absence de clé dans l'environnement de l'agent. Le caviardage ne reconnaît que des
  formes connues de clés.
- Les agents simulés jouent des tricheries scriptées ; des agents réels tricheront autrement (choix du code dans le test
  gelé, données touchées). Les témoins doivent être indiscernables des fiches réelles : un témoin évidemment faux est
  reconnaissable par un agent instruit (c'est le cas de plusieurs témoins de `exemples/temoins-demo-v1.json`).
- Mode pari dans la boucle : le plan d'instances est tiré par l'orchestrateur dans un espace déclaré par la fiche (simulation) ;
  en réel, le réservoir d'instances doit venir du domaine de l'expérience. En mode pari, toutes les survivantes ont la même
  aptitude (−ln α) : le tirage de la recombinaison ne dépend alors que de la diversité de domaine.
- Budget : réservation par vagues, témoins d'abord ; sous un plafond serré, les témoins peuvent tout consommer.
- Le registre de calibration ne mesure la calibration que sous un nul connu (témoins faux) ; ailleurs, le score de Brier
  mêle calibration et proportion d'hypothèses vraies.

## Provenance

Lus dans `fournis/` (SHA-256) : `conception-pole-scientifique-v1.md` `a4f94148…`, `relecture-meta-conception-v6-3-v1.md`
`9a791017…`, `essais-brique1-spectre-v1.md` `5b7011b1…`, `claude-agent-sdk-python/README.md` `c38a933b…`,
`src/claude_agent_sdk/types.py` `c06ccef3…`, `query.py` `5528bc5b…`, `__init__.py` `1582188c…` (le fichier des empreintes
des fournis, hors de `fournis/`, n'a pas été lu). Entrées de démonstration : `exemples/` (empreintes dans
`EMPREINTES-sortie-v1.txt`). Toutes les sorties et leurs empreintes : `EMPREINTES-sortie-v1.txt`.
