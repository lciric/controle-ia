# Consigne : note de conception courte — un « scientifique » du marché comme rôle expérimentateur de l'organisme d'idéation — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 14:22 UTC (heure relevée par `date -u`), sur le mot de Lazar (R-2370) : « (a) Comme expérimentateur : go ; … deux réécritures libres … : go ; … note de conception courte maintenant et le branchement après la course v66 : go ». Destinataire : un **agent neuf** (concepteur), qui n'a écrit aucune pièce de l'organisme. Aucune lecture de T0.7, de T0.6 ni de P3-bis n'est utile ici.

## Interdits, recopiés mot pour mot (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, `1ee3b370…`)

# Interdits communs aux sous-agents de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (10 novembre 2026, v2)

Écrit le 2026-11-09 vers 22:00 UTC (heure relevée par `date -u`). Recopié mot pour mot dans chaque consigne de cette série.

**v2** (R-2086) : v1 recopiée à l'identique (`851028fc…`), plus la règle 9 ; écrite après deux accès mécaniques par recherche récursive (R-2064, R-2086).


1. **Fichiers et branches qu'on n'ouvre jamais** (ni lecture, ni affichage, ni copie, ni passage à un script, ni `git show`, ni `git ls-tree`, ni `git fetch`) :
   - `diag/*/lecture-sondes-t06.json` de tout run, et nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` (DT-4 : rien avant le verdict scellé de P3-bis) ;
   - la lecture B de la course 7a et la branche `donnees/lecture-b-7a-quarantaine-v1` (R-2041, R-2048) ;
   - tout `diag/` et tout `runs/` de la course 7a (`20261109-070232-t06-reel`) et la branche `essai/t06-explo-v3`, sauf permission écrite dans la consigne ;
   - `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` (le bras d'attaque n'est pas le mandat de la mère : N-056, R-2045, R-2047) ;
   - les items, clés et réponses de l'étiqueteur (branche `prep/etiqueteur-v2-lecture-interrompue-reprise-v1`).
2. **Secrets** : ne jamais lire, afficher ni copier une valeur de clé ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`, même avec la sortie jetée.
3. **Aucun appel** de modèle ni d'interface externe (Argon, Claude, autres), aucune location d'instance, aucun `vastai`, aucune dépense.
4. **Git** : aucun `checkout`, `switch`, `reset`, `stash`, `commit`, `push`, `fetch`, `merge`, `rebase`, ni modification de l'index ; les autres commits se lisent par `git show <commit>:<chemin>` seulement (ils sont déjà dans le clone local). Rien n'est écrit hors des chemins de sortie nommés dans la consigne.
5. **Essais** : ne pas lancer la suite complète (la session mère la fait tourner) ; des essais ciblés sont permis.
6. **Refus** : si un contrôle de permissions ou un classifieur refuse une action ou une réponse, s'arrêter sur ce point et le rapporter tel quel ; ni contournement, ni reformulation, ni transfert.
7. **Heures** : toute heure écrite est relevée par `date -u` et dite telle.
8. **Rapport final à la mère** : chemins écrits, empreintes sha256, verdict en une ligne, points ouverts ; **aucune valeur numérique tirée d'une sonde de 7a** (il ne doit d'ailleurs y en avoir aucune sous vos yeux).
9. **Recherches et parcours** : aucune recherche récursive (`grep -r`, `rg`, `find … -exec`, motif `**` ou `*/` développé par l'interpréteur) sur un dossier qui contient un chemin interdit sans l'exclure explicitement ; en pratique, chercher avec `git grep` et des exclusions de chemins (`git grep -n MOTIF -- . ':(exclude)docs/notes/bras-attaque' ':(exclude)scripts/extraire_mesures_epreuve_t06_v1.py' ':(exclude)diag' ':(exclude)runs'`) ou dans une liste de fichiers nommés ; `verifier-arbre` et tout outil qui hache un arbre entier ne se lancent que sur un arbre où `docs/notes/bras-attaque/` n'est pas extrait.

**Écarts écrits, et eux seuls** : règle 3 levée pour la **lecture** de pages publiques (dépôts de code au commit de tête, fichiers bruts, articles), sans clonage, sans installation, sans exécution, sans clé, sans appel de modèle ; règle 4 : aucune écriture git. Tu n'écris que sous `docs/notes/ideation-organisme-v1/experimentateur-v1/` (dossier neuf) et dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/experimentateur/`. Sceller chaque sortie (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`). Toute source citée : adresse, commit ou version, date de lecture ; tout chiffre de la littérature non vérifié sur pièce empreintée porte « non vérifié (R7) ».

## Ce qui fonde ce travail
Registre : R-2368, R-2370 (mots de Lazar), N-044, N-045 (v1 et v2), N-053, N-064, N-065 (`docs/decisions/`). Organisme : préenregistrement scellé de la course v66 `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-v1.md` (`46d7545b…` ; l. 149 et 291-294 : **Claude exclu par construction**, lois plantées écrites par la famille Claude ; gardien mécanique ; juge statistique de l'orchestrateur). Travaux déjà faits, à reprendre et non à refaire : `docs/notes/ideation-organisme-v1/ia-scientifique-externe-v1/choix-ia-scientifique-v1.md` et `verification-pieces-primaires-v1.md` (Sakana AI Scientist v2 et v3, « Agentic Scientist ») ; `docs/notes/ideation-organisme-v1/bras-labs-co-scientist-v1/protocole-bras-labs-v1.md` ; `docs/notes/ideation-organisme-v1/juge-tournoi-elo-v1/conception-juge-tournoi-elo-v1.md` (réécritures libres de Co-Scientist : Kaimen-Inc/Co-Scientist, Apache 2.0, `cef5bcf…` ; The-Swarm-Corporation/AI-CoScientist, MIT, `6fdd532…`) ; `docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/`.

## Mandat (note de 4 à 6 pages, pas plus)
1. **Rôle** : un expérimentateur propose et **exécute** des expériences sur les mondes plantés de l'organisme et rend des fiches ; il ne juge jamais : la statistique reste calculée par l'orchestrateur, hors de tout agent (O2, N-064) ; aucun score d'un moniteur du programme dans sa sélection (N-053) ; place dans la composition apprise (N-045).
2. **Candidats** (au moins trois, dont les deux réécritures de Co-Scientist et l'Agentic Scientist ; dis si le « Coscientist » de Boiko et al. 2023, chimie robotisée, est hors sujet) : licence lue au commit, moteur de modèle exigé et **possibilité de le faire tourner hors de la famille Claude** (Kimi, Argon ou un modèle ouvert), ce qu'il exécute et où (bac à sable, réseau), effort de branchement sur l'interface de l'orchestrateur (fiche, retour lu), coût estimé par génération (formule et hypothèses écrites), risques (fuite des lois plantées, exécution de code, réseau).
3. **Antériorité (R8)** : ce que le branchement revendiquerait ou non (O1 à O20 dans l'état de N-064) ; zones déjà occupées.
4. **Recommandation** : un candidat (ou aucun), confiance, ce qu'il faut pour le brancher après la course v66 (version de l'orchestrateur, préenregistrement, devis, GO), et ce qui reste à trancher par Lazar.

## Sortie
Note scellée `note-conception-experimentateur-v1.md` (et pièces lues, si utiles, scellées) ; rapport final à la mère : chemin, empreinte, recommandation en une ligne, ton modèle.
