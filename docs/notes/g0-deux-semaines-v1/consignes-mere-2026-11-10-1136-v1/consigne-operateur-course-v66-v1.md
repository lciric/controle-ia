# Consigne : opérateur de la course réelle de l'organisme (code v66, GO-2026-11-10-11) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 23:51 UTC (heure relevée par `date -u`). **Dépense autorisée** : GO-2026-11-10-11 (45 USD au plus : 40 de modèles, Kimi 33, Argon 7 ; 5 de machine jetable Hetzner CPX32) ; mot de Lazar, R-2285 : « lance la location de la machne, les cles sont dans l'env ». Tu es un sous-agent **neuf**, opérateur ; tu n'as écrit ni le code de l'organisme, ni le texte de la course, ni leurs contre-lectures.

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

**Exceptions de cette consigne, et elles seules** : (1) appels à l'API de Hetzner (`api.hetzner.cloud`) avec `HCLOUD_TOKEN` lu de l'environnement **par son nom** (`-H "Authorization: Bearer $HCLOUD_TOKEN"`), jamais affiché, jamais écrit dans un fichier ; **chaque commande qui crée un serveur cite `GO_ID=GO-2026-11-10-11`** ; (2) connexion SSH à la seule machine que tu crées (clé SSH jetable générée dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/operateur-course-v66/`, jamais versée) ; (3) les relais Kimi et Argon reçoivent `KIMI_API_KEY` et `GEMINI_API_KEY` (valeur prise de `GEMINI_API_KEY_2`) **par l'entrée standard** de la commande distante (par exemple `printf '%s' "$KIMI_API_KEY" | ssh … 'IFS= read -r K; KIMI_API_KEY="$K" exec …'`), jamais en argument, jamais dans un fichier, jamais dans l'environnement du lanceur ; (4) appels payants aux modèles **seulement par les deux relais**, sous leurs plafonds. Aucune autre dépense ; aucune autre machine ; aucun autre fournisseur ; ne touche à **aucun** serveur ou instance que tu n'as pas créé (inventaire d'abord, par nom et identifiant seulement).

## À lire (empreintes à vérifier)
- **Texte scellé** `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-v1.md` (`46d7545b…`) : sections 3, 10 (liste d'arrêt), **12.3 (préalables, dans l'ordre)**, **12.4 (commandes exactes)**, 13 (devis), 16 (blocs gelés). Il fait foi sur tout.
- Code : paquet git `docs/notes/organisme-boucle-reelle-v1/code-v66/organisme-v66-boucle-reelle-v1.bundle` (tête `7e415cbaaa3ff602db43a44dad6b4307c08352c7`, `git bundle verify`) ; rapport du développeur v66 et contre-lecture courte `docs/notes/organisme-boucle-reelle-v1/code-v66/contre-lecture-code-v66-courte-v1.md` (`a2880368…`, section 6 : ce qui ne se joue que sous `bwrap`) ; dossier de course `docs/notes/organisme-boucle-reelle-v1/code-v66/configuration-v6/` et `docs/notes/organisme-boucle-reelle-v1/code-v66/blocs-v66/heritage-depart-v65.json` **avec son compagnon**.
- Relais Kimi `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py` (`d54ed2bc…`) ; collisionneur v7 `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/kits-v8/ref/v7/collisionneur_v7.py` (`c9725f02…`, vérifie l'empreinte entière avant copie).
- `registres/go.md` de `main` (ligne GO-2026-11-10-11) : copie sur la machine, empreinte notée (§ 12.3, point 4).

## Mandat
1. Inventaire des serveurs Hetzner existants (identifiants et noms seulement) ; crée **un** serveur CPX32 (Ubuntu 24.04 ou image où `bwrap` ≥ 0.9), nom `organisme-v66-course`, commande citant `GO_ID=GO-2026-11-10-11` ; note son identifiant, l'heure (`date -u`) et le prix horaire ; écris tout de suite l'identifiant dans ton journal.
2. Prépare la machine : paquets nécessaires, `bubblewrap`, interpréteur et numpy notés ; arbre de l'organisme depuis le paquet git à `7e415cba` ; le texte scellé copié sous `orchestrator/prereg/preenregistrement-boucle-reelle-organisme-v1-v1.md` (octets égaux, compagnon) ; dossier de course ; héritage et compagnon ; relais Kimi ; collisionneur v7.
3. Joue les **préalables 1 à 7 de la section 12.3, dans l'ordre** ; consigne chaque sortie (code, dernière ligne). **Tout préalable manqué arrête avant tout appel payant** : rapporte, détruis la machine si la correction n'est pas immédiate et sans effet sur le texte, et rends la main.
4. Lance les deux relais (commandes de 12.3, point 6, valeurs exactes), puis la commande de 12.4 avec `--verifier-seulement` (« vérification : conforme »), puis sans ; suis la course (journaux, dépense des relais) ; à la fin, lecture par `lire_boucle_reelle_v66.py` ; arrête les relais **par leur PID** (R10).
5. Rapatrie dans `docs/notes/organisme-boucle-reelle-v1/course-v66/` (dépôt de travail, seul chemin d'écriture hors du bac à sable) : relevé, lecture, journaux des relais et du lanceur, dossier des sessions des proposeurs (audit A1), rapport de course `rapport-course-v66-v1.md` (empreinte du `go.md` copié, plafonds des relais, interpréteur, numpy, empreinte du relevé, phrase rendue, dépense par relais, durée, coût de la machine), tous scellés ; **aucune clé, aucun fichier qui en contienne**.
6. **Détruis le serveur par son identifiant** (API `DELETE /v1/servers/<id>`), vérifie qu'il n'existe plus, note l'heure et le coût ; dans tous les cas (succès, arrêt, refus), la machine ne survit pas à ta session de travail.
7. **Tu ne lis pas l'issue pour la juger** : tu rapportes la phrase rendue par le programme de lecture, sans commentaire ; le verdict (R13) sera rendu par un agent neuf.

## Arrêts
Refus d'un contrôle → arrête-toi sur ce point et rapporte-le tel quel (règle 6). Dépense d'un relais au plafond → c'est le relais qui arrête ; rapporte. Toute surprise sur le coût de la machine (> 5 USD prévisible) → détruis et rapporte.

## Rapport final à la mère
Identifiant et vie du serveur (création, destruction, heures, coût), sorties des préalables, codes du lanceur, dépense par relais, chemins et empreintes rapatriés, phrase rendue, incidents.
