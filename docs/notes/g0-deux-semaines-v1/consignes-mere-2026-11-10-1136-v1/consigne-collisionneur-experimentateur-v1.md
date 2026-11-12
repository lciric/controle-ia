# Consigne : un tour ciblé du collisionneur sur le choix de l'expérimentateur de l'organisme — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 15:31 UTC (heure relevée par `date -u`). Destinataire : un **opérateur neuf** (Claude Opus 5.5), qui n'a écrit ni la note de conception, ni le collisionneur. Dépense : **GO-2026-11-11-03** (ligne de `registres/go.md`, mot de Lazar « go collisionneur ≤ 15 USD », R-2380) : **plafond 15 USD**, aucune autre dépense.

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

**Écarts écrits, et eux seuls** : règle 3 levée pour **ce seul tour du collisionneur**, sous GO-2026-11-11-03 et son plafond (le script reçoit `--plafond-usd 15`, ou moins) ; interface de Claude **seulement** par la clé `RR_ANTHROPIC_API_KEY_RIGAUD`, passée par son nom sous `env -i` (`ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_RIGAUD"`), **jamais** `ANTHROPIC_BASE_URL` ; Kimi par son relais, comme au tour du 9 novembre ; autres clés par leur nom seulement ; jamais une valeur affichée. Règle 4 : aucune écriture git. Tu n'écris que sous `docs/notes/collisionneur-experimentateur-v1/` (dossier neuf) et ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/collisionneur-exp/`. Processus arrêtés par leur PID (R10).

## Modèle à suivre
Le tour du 9 novembre (QO-1 et Q1) : `docs/notes/collisionneur-conception-qo1-q1-v1/` (`faits-v1.md`, `question-v1.md`, `relais-v1/`, `run-e3-v1/`, consoles, `synthese-v1.md`) et le registre R-2009 à R-2020 (script employé, espèces, commande, relais, dépense 10,89 USD). Prends le même script et la même mécanique, sauf ce qui suit.

## Ce tour
1. **Faits** (`faits-v1.md`) : résumé fidèle et court de la note `docs/notes/ideation-organisme-v1/experimentateur-v1/note-conception-experimentateur-v1.md` (`7df9afc4595e22c7cde3bd0757c3b304085291cb61bf789b7d8bd0da70c87655`) et de ses contraintes (O2 : juge statistique hors des agents ; N-053 ; Claude exclu des proposeurs de l'organisme ; pièces des mondes plantés publiques dans `lciric/ideation-organism` : aucun Web pour l'expérimentateur) ; aucun chiffre non marqué « estimé ».
2. **Question** (`question-v1.md`, étage III) : « Pour donner à l'organisme un rôle d'expérimentateur, faut-il brancher d'abord Kaimen-Inc/Co-Scientist sur Kimi, avec un outil d'exécution neuf et isolé, comparé à coût égal à un témoin « Kimi, meilleur de N », et ne passer à The Agentic Scientist que s'il bat le témoin ; ou d'abord The Agentic Scientist, enfermé (sans réseau, sans Web) ; ou autre chose ? Donner : choix, raisons, risques, mesure qui départagerait, et ce qui ferait changer d'avis. » (Lazar a demandé : « pourquoi pas lui ? » à propos de The Agentic Scientist.)
3. **Devis** (`devis` du script) avant tout appel ; si le pire cas dépasse 15 USD, retire une espèce ou baisse le plafond de sortie, et écris-le.
4. **Tour** (`etage3`, plafond ≤ 15) ; refus, absences et incidents consignés tels quels ; relais arrêtés par PID.
5. **Sorties** scellées (faits, question, devis, run, consoles, relais) ; **dépense réelle** relevée par espèce.
6. **Synthèse** : tu ne la fais pas ; dis seulement si toutes les cellules sont valides.

## Rapport final à la mère
Chemins et empreintes ; espèces jouées, refus ; dépense réelle par espèce et totale (≤ 15) ; ligne proposée pour `registres/depenses.md` ; ton modèle.
