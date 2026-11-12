# Consigne : code de P3-bis sous la règle (a') — différence appariée et 800 directions — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 10:33 UTC (heure relevée par `date -u`). Destinataire : un **développeur neuf**, qui n'a écrit ni P3-bis (brouillons 1 à 12), ni son code, ni sa chaîne, ni T0.7, ni leurs contre-lectures. Ce rôle n'est pas celui d'un lecteur de P3-bis ; tu n'ouvres de toute façon aucune sortie de P3-bis (il n'y en a pas) ni de T0.6.

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

Exceptions à la règle 4 : (1) une branche **neuve** `prep/p3bis-regle-a-v1` partie de `614fd5dab…` (tête de `prep/p3bis-lanceur-v1`, qui porte le code `a1de3915` et la chaîne ; récupère-la par `git fetch origin prep/p3bis-lanceur-v1` à refspec), dans un arbre clairsemé à toi (`/src/`, `/tests/`, `/scripts/`, `/docs/procedures/` si la chaîne s'y trouve, plus ce dont les essais ont besoin, déclaré), commits et poussée de **ta seule branche** (`git push origin HEAD:prep/p3bis-regle-a-v1`, retentatives 2, 4, 8, 16 s, garde des secrets à 0 chaînée par `&&`) ; jamais de fusion dans `main` ; (2) essais et répétitions jouets permis (règle 5 levée pour tes fichiers, `--basetemp` dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/code-p3bis-regle-a/`, temps et tailles bornés). Aucun appel de modèle, aucune dépense, aucune instance. Le conteneur redémarre parfois (quatre fois aujourd'hui, une fois avec un disque neuf) : **pousse tôt et souvent**.

## Ce qui fonde ce travail (lis ces lignes de `registres/decisions.md`)
- **R-2296** : P3-bis prend exactement la règle de lecture de T0.7 sous (a') ; l'ancienne règle (200 directions, borne basse de l'intervalle de la sonde > quantile 0,95 du plancher) est calculée et **rapportée comme information**, jamais décisive ; un désaccord des deux issues est écrit en réserve.
- **R-2320** : **k = 800** directions aux effectifs de PB-1 (note `docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/note-n-plancher-p3bis-v1.md`, `1613d5bd…`, à lire en entier : taux, puissance, aire minimale 0,680, coût de notation **non mesuré** sur la chaîne de P3-bis, remarque sur les 200 premières directions sous la graine de P3).
- **R-2299** : réserves jointes à toute citation du nul de P3.
- La règle (a) elle-même : `plancher_v2.comparer_difference_au_plancher`, `src/controle_ia/t07/plancher_v2.py` au commit C7 `b4cd9953d199dd8f220f5162e5868c5b00fd392d` (sur `main`), et sa notation par lots `plancher_v3.py` (même commit) ; lis-les par `git show`.

## À lire (empreintes à vérifier)
- `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon12.md` (`07b16063…`) : « Métrique », « Seuil », « Plan d'analyse » (PB-1, PB-9, PB-13, point 10), « Critères de lecture gelés », « Liste d'arrêt », « Ce que le code et la chaîne doivent changer », « Préalables », « Devis ».
- Code de P3 (inchangé, R12) et de P3-bis au commit `a1de3915` : `src/controle_ia/premier_test_ia/` (`run.py`, `run_v2.py`, `lecture.py`, `lecture_p3bis_v1.py`, `statistiques.py`, `figees.py`, `notation.py`) et `src/controle_ia/sondes/evaluation.py` (`plancher_apparie`) ; la chaîne et ses scripts d'instance.

## Mandat
1. **Où naît le plancher dans la chaîne de P3-bis** (tirage, nombre, graine, notation, stockage) et comment obtenir **800 directions dont les 200 premières sont celles de P3** sous la graine de P3 (si `plancher_apparie` tire en séquence) — de sorte que l'identité avec P3 (PB-9) reste éprouvable sur les 200 premières ; dis-le avec les lignes de code.
2. **Lecture décisive de PB-1 sous la règle (a)** (et PB-13 aligné, ou déclaré) : module **neuf** (aucun fichier de P3 ni de P3-bis existant modifié, R12), qui reçoit les scores par action de la sonde et des 800 directions et applique **exactement** la règle de `plancher_v2.comparer_difference_au_plancher` de C7 (soit en l'important d'un arbre qui le porte, soit en la recopiant avec un essai d'égalité au bit près contre celle de C7 — choisis et justifie) ; l'ancienne règle à 200 directions calculée et rapportée à côté ; réserve écrite si les deux issues diffèrent ; notation des 800 directions **par lots** (comme `plancher_v3`), éprouvée égale à la boucle.
3. **Chaîne** : ce qui change dans la configuration et les scripts de l'instance (nombre de directions, appel du module neuf) ; **répétition jouet** de bout en bout de la chaîne modifiée ; **mesure du temps ajouté** (notation des 800 directions) et devis mis à jour.
4. **Essais R5** (cas sain et artefact pour chaque garde neuve), suite des essais de P3-bis de l'arbre, **mutations** sur copies (`-o pythonpath=`, import tracé).
5. **Couples proposés** pour le candidat suivant de P3-bis (sections « Métrique », « Seuil », PB-1, PB-13, point 10 (puissance : aire minimale ≈ 0,680 sous (a), R-2320), « Devis », commit du code), écrits mais **non appliqués** (un rédacteur neuf les appliquera) ; chaque changement d'une section gelée nommé et rattaché à R-2296 (un seuil du texte change sur décision ; c'est ce que Lazar a accordé pour T0.7, R-2285, et la mère l'a porté à P3-bis par R-2296 sous son accord général).

## Livrables
- Commit(s) poussés sur `prep/p3bis-regle-a-v1`.
- Rapport scellé (non committé) `docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/rapport-code-p3bis-regle-a-v1.md`, avec les couples proposés en JSON à côté (`couples-proposes-p3bis-regle-a-v1.json`), journaux d'essais et de la répétition, scellés.
- Réponse finale : commit, fichiers neufs et empreintes, essais, mutations, répétition, temps ajouté et devis, couples, réserves, ton modèle.
