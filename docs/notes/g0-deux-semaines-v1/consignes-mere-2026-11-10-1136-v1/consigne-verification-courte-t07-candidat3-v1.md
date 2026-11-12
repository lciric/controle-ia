# Consigne : vérification courte du candidat 3 de T0.7 et de l'ordre brouillon 7 (différentiel du candidat 1 et du brouillon 5) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 04:18 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, vérificateur, d'un autre modèle que le rédacteur (Opus 5.5) : N-052 ; tu n'as écrit ni T0.7, ni son module, ni ses ordres, ni leurs contre-lectures, ni les notes de l'erreur de première espèce. Ayant lu T0.7, tu seras exclu ensuite de tout rôle de lecteur de P3-bis.

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

Exception à la règle 4 : aucune. Bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/verif-t07-candidat3/` (scripts depuis des copies, `python -I` ; essais ciblés permis avec `--basetemp` au bac à sable). Aucun appel de modèle, aucune dépense. Sceller ta sortie par `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`. Le conteneur a redémarré trois fois cette nuit : écris ta sortie tôt et complète-la au fil de l'eau.

## Ce qui fonde les changements
- **Mot de Lazar R-2285** : « (a') le remède, plus davantage de directions dans le plancher : un seuil du texte à changer : go ». Autorise, dans les sections gelées, la **définition de « au-dessus du plancher »** et le **nombre de directions** ; rien d'autre de gelé.
- Décisions R-2296, R-2298, R-2299, R-2304, R-2305, R-2306, R-2309, R-2310 (lis ces lignes de `registres/decisions.md`).

## À lire (empreintes à vérifier)
- Base : `brouillons/T0.7-sondes-v0-v1-candidat1.md` (`1718f2a0…`) et sa vérification courte `prereg/contre-lectures/T0.7-sondes-v0-v1-candidat1-verification-courte-v1.md` (`ef3431a1…`) ; ordre `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md` (`d0b75d16…`).
- Candidat 2 : `brouillons/T0.7-sondes-v0-v1-candidat2.md` (`9de13f6a…`) et ses pièces (60 couples `beb5ecfb…`, script, journal, puissance) ; ordre brouillon 6 (`92d9aebe…`) et son script.
- Candidat 3 : `brouillons/T0.7-sondes-v0-v1-candidat3.md` (`1b9b75f0…`) et ses pièces (23 couples `4e5fc8b0…`, script, journal) ; ordre brouillon 7 `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon7.md` (`d799a01b…`) et son script (`478dde84…`).
- Sources des nombres : notes `docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v3.md` (`760a562c…`) ; audit de P3 `docs/notes/g0-deux-semaines-v1/audit-p3-regle-plancher-v1/audit-verdict-p3-regle-plancher-v1.md` (`57f16378…`, section 7) ; rapports du code `…/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v1.md` (`cb31edc8…`) et `-v2.md` (`71cc3b89…`), configuration v8 (`e31c7a79…`, canonique `0f32c6de…`), répétition jouet v3.
- Code : branche `prep/t07-plancher-v3-v1`, commit `7e23a554aca040016a08fe510504adec172c6998`, par `git show` seulement ; `CODE-T07-v1.json` sous `registres/code-t07/`.

## Mandat
1. **Rejeu** : les scripts du candidat 2 (sur une copie du candidat 1) et du candidat 3 (sur une copie du candidat 2) redonnent les textes à l'octet ; de même pour les ordres 6 et 7.
2. **Changements gelés** (G2-01 à G2-17, G3-01, G3-02) : chacun est-il **dans le périmètre de R-2285** (définition de « au-dessus », nombre de directions, et ce qui en découle nécessairement : plancher neuf des sondes figées, repli, réserves) ? Un changement qui n'en découle pas = **nœud** (dis lequel, et le couple qui le retirerait). Vérifie par programme qu'aucune hypothèse, prédiction, signe, niveau, ligne L ni entrée de grille ne change, et que le reste des sections gelées est égal à l'octet au candidat 1.
3. **Exactitude** : la règle écrite au Seuil est-elle exactement celle de `plancher_v2.comparer_difference_au_plancher` au commit `7e23a554` ? Les seuils des paliers, la configuration v8 (recalcule l'empreinte canonique par la fonction de `lecture_v4`, chargée par `git show` dans ton bac), les 26 empreintes du module au commit `7e23a554`, les nombres de puissance (aire minimale 0,6408 / 0,6058 / 0,5815 à 0,6658 ; refais le calcul par `puissance_regle_a_t07_v1.py` des pièces du candidat 2), le devis, les réserves de P3 (mot pour mot de R-2299) : chaque nombre renvoie-t-il à un chemin et une empreinte (R6) ?
4. **Ordre brouillon 7** : commandes `lecture_v4`, script v3 (`a19c594d…`), contrôle P12 changé (arbres comparés à ceux de C7) — sain ou faille ? marqueurs (douze), `SRC7`, `ATT_C7_T07`.
5. **Marqueurs** : candidat 3 → un seul, `C7_ET_CODE_T07_26_MODULES` ; `MOT_LAZAR_P064`/`P065` remplis selon R-2269 ; VC1-A et VC1-B appliqués.
6. **Verdict** : « scellable » (une fois C7 fixé par la mère et CODE-T07 écrit) ou « après corrections » (couples exacts) ou « nœud » (lequel).

## Sortie
`prereg/contre-lectures/T0.7-sondes-v0-v1-candidat3-verification-courte-v1.md`, scellé ; constats VC3-n. Rapport final : chemin, empreinte, verdict en une ligne, constats bloquants, ton modèle.
