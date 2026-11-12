# Consigne : session fille « préalables de P3-bis » (clés, disque neuf) — phase 1 — v1

Écrite par la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` le 2026-11-10 à 23:56 UTC (heure relevée par `date -u`). Mots de Lazar (R-2285) : les clés du calcul sont dans l'environnement ; la session qui porte les clés est nécessaire à P3-bis. Tu es une **session fille neuve**, dans le même environnement que la mère (mêmes clés, disque neuf). Tu n'as écrit ni P3-bis, ni sa chaîne, ni leurs contre-lectures. **Tu ne lis aucun fichier de T0.7** (P3-bis doit garder des lecteurs qui ne l'ont pas lu). Aucune dépense dans cette phase.

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

**Avant tout** : ton dépôt a été cloné en entier par la plateforme ; **n'ouvre rien sous `docs/notes/bras-attaque/`** ; passe aussitôt en extraction partielle (`git sparse-checkout init --no-cone`, motifs `/*` et `!/docs/notes/bras-attaque/`, `git sparse-checkout reapply`) et vérifie que le dossier a disparu de l'arbre. Clés : lues **par leur nom seulement** (`HF_TOKEN` pour le tokeniseur), jamais affichées ni écrites. Aucun commit sur `main` : tu travailles sur la branche `prep/p3bis-prealables-v1` (depuis `main`), tu pousses seulement elle (`git push -u origin prep/p3bis-prealables-v1`, retentatives 2, 4, 8, 16 s ; garde des secrets à 0 avant chaque commit, enchaînée par `&&`). Un `git fetch` se fait toujours avec une refspec. Si un contrôle refuse une commande, arrête-toi et rapporte-le tel quel.

## À lire (empreintes à vérifier)
- `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon12.md` (`07b16063…`) : table des préalables P-1 à P-11, marqueurs restants ; contre-lecture 4 `brouillons/P3-bis-temoin-positif-v1/contre-lecture-4-brouillon11-v1.md` (`90847ae2…`) ; registre R-2197, R-2233, R-2237.
- Chaîne de P3-bis : branche `prep/p3bis-lanceur-v1` (`git fetch origin +refs/heads/prep/p3bis-lanceur-v1:refs/remotes/origin/prep/p3bis-lanceur-v1` ; commits `614fd5da`, `8ad29273`) et `docs/procedures/P3-bis-temoin-positif-v1/` ; code au commit `a1de39151ebae29138a389829751397074239615`.

## Mandat, phase 1 (aucune dépense, aucun appel de modèle)
1. **P-4** : relève `df -Pk` sur le dossier parent de la future racine de répétition (≥ 12 692 612 ko exigés) ; rapporte.
2. **P-1** : environnement `PY` neuf sous Python 3.11 (`/usr/bin/python3.11` ; installe-le s'il manque), `pip install -r requirements-gpu.txt` **du commit du code** ; versions relevées (dont `pypandoc_binary`).
3. **P-2** : recompte de N : la liste ciblée v2 (`scripts/essais-cibles-p3bis-v2.txt`) jouée par `PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider --color=no`, comme au bloc 8, au commit du code, dans un clone en extraction partielle de la chaîne où `docs/sources/` est présent ; dernière ligne exacte, sortie brute versée.
4. **`LONGUEURS_P3BIS`** : mesure des longueurs au vrai tokeniseur (révision citée par le texte ; téléchargement par `HF_TOKEN` lu par son nom), selon ce que le texte et la chaîne prescrivent ; fichier JSON des longueurs attendues ; **A = T exigé** : si non, arrête-toi (nœud).
5. Verse sur ta branche, sous `docs/notes/g0-deux-semaines-v1/p3bis-prealables-v1/` : sorties brutes, versions, longueurs, rapport `rapport-prealables-p3bis-phase1-v1.md`, tous scellés (`PYTHONPATH=src python -m controle_ia.scellement sceller`). Rien d'autre.

## Rapport à la mère
Par `send_message` vers `session_01VJdZpSMxSdk2SJ1ScmdfNv` : place disque, Python et versions, N exact, longueurs (A = T ?), branche et commit, empreintes. Puis attends la phase 2 (épingles P-5 et passages canoniques P-6, après le candidat) ; rien ne part sur une instance payante sans consigne neuve.
