# Reproduction de R-599 à zéro dépense — chemin de la clé avec la v31 — v1

Écrit par session-depot (instance 2, Opus 5.5) le 28 octobre 2026 vers 15:35 UTC. Aucune vraie clé, aucun appel payant :
clé factice (`cle-factice-repro-r599`) dans l'environnement du seul relais, amont mort (`http://127.0.0.1:9`).

**Montage** : relais réel de la v31 (`pole/relais_reel.py`, empreinte inchangée depuis v30) lancé sous `env -i`, port
38611, plafond 1 USD ; une session du kit d'agent (`claude-agent-sdk` 0.2.174, outil en ligne de commande 2.1.312) par
`AdaptateurClaudeSDK` de la v31, **options exactes** (`construire_options` : bac à sable actif, `failIfUnavailable`,
lectures bornées), environnement de l'orchestrateur vide (`environnement={}`) et processus sous `env -i` (PATH, HOME, LANG,
TMPDIR seulement) ; rôle `juge_ideation`, un tour, consigne « Réponds exactement : OK ». `bubblewrap` et `socat` installés ;
bac à sable vérifié (réseau isolé, `/proc` neuf).

**Résultat** (`relais-journal.jsonl`, `relais.log`) : le relais reçoit **20 requêtes conformes** `POST /v1/messages?beta=true`,
toutes transmises à l'amont, toutes en 502 (amont mort, `ConnectionRefusedError`) ; **aucune « Bad request version »** ;
aucun refus du jeton factice. L'agent réessaie jusqu'à la borne de temps (180 s) : la session ne rend rien.

**Lecture** :
1. Dans ce montage, le chemin agent → relais fonctionne : adresse sans `/v1` (l'outil ajoute `/v1/messages` lui-même), en
   clair, jeton factice accepté. La panne du duel (requêtes non conformes, `ValueError` dans `parse_request` : un client qui
   parle autre chose que du HTTP en clair, très probablement une poignée de main chiffrée) venait donc d'un autre montage
   (adresse ou environnement du duel), pas du relais lui-même. Cause exacte non établie : les mondes et le lanceur du duel
   sont perdus avec l'ancien conteneur.
2. Constat neuf : **quand l'amont échoue, l'agent réessaie longtemps et ne rend rien** ; il faut une borne de temps par
   session et un appel de contrôle qui échoue vite (CL31-01).
3. Reste à démontrer avant la course : le dernier maillon, relais → amont réel avec la vraie clé (un appel de contrôle par
   modèle, quelques centimes, sous GO), et que le coût déclaré par l'agent concorde avec la dépense comptée par le relais.

Relais arrêté par son identifiant de processus (4050) à la fin (R10).
