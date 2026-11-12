# Consigne : vérification courte du brouillon 2 du dessin et devis de l'essai « preuve formelle contre suite bon marché » — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 13:48 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, vérificateur, d'un autre modèle que le rédacteur (Opus 5.5) ; tu n'as écrit ni ce dessin, ni sa contre-lecture 1.

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

Exception à la règle 4 : aucune. Tu peux exécuter les scripts de `brouillons/couche4-essai-preuve-formelle-v1/calculs-v2/` **depuis des copies** dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/verif-devis-lean-b2/` (`python -I`, chemins passés en arguments), jamais dans le dépôt. Aucun appel de modèle, aucun réseau, aucune dépense. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN` (depuis `/home/user/controle-ia-travail`).

## À lire (empreintes à vérifier)
- Brouillon 2 : `brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon2.md` (`05bcf094…`), journal v2 (`a56bc3e9…`), `calculs-v2/` (huit scripts et sorties, compagnons) ; brouillon 1 (`9ccc9ac0…`) et `calculs-v1/`.
- Contre-lecture 1 : `prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon1-cl1.md` (`f565d51c…`) : couples C01 à C14, ajouts, CLP-01 à CLP-09.
- Décisions de la mère : `registres/decisions.md` R-2230 et le message de relance qu'il résume (D-1a et D-1b, C04 à deux classes lues à 97,5 % sans porte, CLP-04 à CLP-07, CLP-09).

## Mandat
1. Rejoue l'application des couples (`appliquer_couples_cl1_v1.py`, `retouches_brouillon2_v1.py`, `deplacer_*`, `table_et_controle_brouillon2_v1.py`) sur une copie du brouillon 1 et compare au brouillon 2 ; chaque couple retrouvé, écarts C08 et C10 jugés (conformes au sens du couple ou non).
2. Rejoue `calculs_devis_essai_v4.py` ; compare la sortie à la sortie versée et aux tables du brouillon 2 (D-1a, D-1b, phase 2, engagement maximal 2 641 USD) ; vérifie les lignes de CLP-06 et le profil de CLP-09.
3. **Fait nouveau de C04** : l'affirmation « sous le seuil » (O3) atteindrait une erreur de famille de 0,027 à 0,060 au gabarit de Wald. Est-ce un défaut du dessin ou une limite écrite et bornée ? Que faut-il (méthode d'intervalle, lecture d'O3, simulation de C09) pour que chaque affirmation lue soit contrôlée au niveau annoncé ? Recommandation.
4. **Fait nouveau d'A8** : 35 graines payables sous 450 USD au profil pire réaliste, 48 sous 550 : vérifie le calcul et la règle d'arrêt.
5. Cloison et dépense (CLP-04, CLP-05) : le texte exige-t-il bien une machine sans clé ni dépôt du programme, une garde éprouvée sur un cas sain et un artefact, la nature de la dépense et un repli pour GPT-6 Astra ?
6. **Verdict** : « présentable à Lazar pour D-1a » (oui ou non, avec ce qui manque) ; « préenregistrement scellable » n'est pas demandé (pièces « À REMPLIR »).

## Sortie
`prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon2-verification-courte-v1.md`, scellé ; constats numérotés VL-n (gravité, constat, ce qu'il faut). Rapport final : chemin, empreinte, verdict en une ligne, constats bloquants.
