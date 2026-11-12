# Consigne : contre-lecture 2 (des écarts) de la consigne de l'audit des fuites de T0.7, brouillon 5 — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 13:51 UTC (heure relevée par `date -u`). Destinataire : un **contre-lecteur neuf, Claude Fable 5.2** (autre modèle que l'auteur des brouillons 2 à 5, Claude Opus 5.5 ; N-052), qui n'a écrit ni T0.7, ni ses contre-lectures, ni son module, ni aucun brouillon de cette consigne, ni la contre-lecture 1. Tu lis T0.7 : tu seras exclu ensuite de tout rôle de lecteur de P3-bis et de tout rôle d'auditeur de l'audit des fuites.

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

Exception à la règle 4 : aucune (`git show` d'un commit déjà présent permis, dont `c7484c43` de la branche de données du découpeur). Tu n'écris que `prereg/contre-lectures/T0.7-consigne-audit-fuites-v1-brouillon5-cl2.md` (nom neuf) et, au besoin, un dossier de pièces `prereg/contre-lectures/T0.7-consigne-audit-fuites-v1-brouillon5-cl2-pieces/`, et ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/audit-fuites-cl2/`. Aucun commit, aucune dépense. Sceller chaque sortie (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`).

## Objet (§ 14.2 du brouillon 5, tel qu'écrit)
Lis le § 14.2 de `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon5.md` (`7228ce724d4f2a7c146124ceb70156cf99118b2acebcdc4b3b7d9e5d977d2b67`) : son objet et la liste des fichiers à lire font ta consigne. En bref : (1) différentiel du brouillon 2 (`ecd80ce4…`) au brouillon 5, série par série (2 → 3 : corrections de la contre-lecture 1 `02b9d8b5…` et décisions R-2212 ; 3 → 4 et 4 → 5 : couples rejoués, défaire chaque série redonne le précédent à l'octet ; R-2346, R-2348) ; (2) remplissage de `LIGNE_AUDIT_FUITES_T07_B22` sur le texte scellé (`prereg/T0.7-sondes-v0-v1.md`, `d7d180ec…`) ; (3) remplissage de `CHEMIN_DECOUPEUR` (commit `c7484c43657a2ce22d76af33efd06aaa11a6aafa`, écriture par `git show`, trois empreintes contre R-2238 et les compagnons du commit) ; (4) **conformité de la ligne `AUDIT-FUITES-T07` du texte scellé à la décision R-2203** (lecture (a)).

## Points que la mère te demande aussi de trancher
- **Q-B5-1** (rédacteur) : en `transformers` 5.18.0 le chargement du découpeur avertit que le nettoyage des espaces de `tokenizer_config.json` est ignoré. Les dépendances épinglées de la chaîne (`requirements-gpu.txt` tire `requirements-cpu.txt` : `transformers==5.18.0`, `tokenizers==0.23.2`) sont celles de l'auditeur ; vérifie que la chaîne de T0.6 décode les textes des actions par le même chemin (`harnais/modeles.py`, l. 146 cité au § 6.1) et dis si le contrôle `decode(ids[:jetons_notes], skip_special_tokens=True) == texte` peut échouer pour une raison de version (si oui, c'est un arrêt prévu : dis-le, ne change rien).
- **Q-B5-3** (rédacteur) : le § 9 dit « Aucun autre chemin n'est écrit » alors que l'auditeur écrit les fichiers du découpeur dans son bac à sable, hors du dépôt : faut-il un mot au § 9 ?

## Sortie
Rapport scellé : verdict en une ligne (« scellable », « scellable après corrections » avec couples exacts « ancien → nouveau » prêts à appliquer, ou « non scellable » avec motif) ; constats numérotés (CL2-01…), chacun avec preuve (commande, sortie, ligne) ; ce que tu n'as pas pu vérifier. Rapport final à la mère : chemin, empreinte, verdict, ton modèle.
