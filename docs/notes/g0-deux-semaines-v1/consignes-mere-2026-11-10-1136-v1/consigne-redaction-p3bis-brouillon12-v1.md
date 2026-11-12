# Consigne : rédiger le brouillon 12 de P3-bis (couples de la contre-lecture 4, bloquants de procédure levés) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 13:42 UTC (heure relevée par `date -u`), autonomie de 12 heures (R-2201) sous accord général (GO-2026-11-10-05, GO-2026-11-10-09). Destinataire : un **rédacteur neuf**, qui n'a écrit ni P3-bis (brouillons 1 à 11), ni son code, ni sa chaîne, ni leurs contre-lectures. **Tu ne lis aucun fichier de T0.7** (ni `brouillons/T0.7-*`, ni `prereg/T0.7*`, ni `src/controle_ia/t07/`, ni `docs/notes/g0-deux-semaines-v1/t07-*`, ni `brouillons/T0.7-audit-fuites-v1/`) : P3-bis doit garder des lecteurs qui ne l'ont pas lu.

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

Exception à la règle 4 : aucune. Tu n'écris que sous `brouillons/P3-bis-temoin-positif-v1/` (noms neufs ci-dessous) et dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-b12/`. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN` (depuis `/home/user/controle-ia-travail`). Aucun commit.

## À lire (empreintes à vérifier)
- `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon11.md` (`409c37ed…`), ses couples, son script et son journal (méthode).
- Contre-lecture 4 : `brouillons/P3-bis-temoin-positif-v1/contre-lecture-4-brouillon11-v1.md` (`90847ae2…`) : constats CL4-01 à CL4-16, **couples CL4-C01 à CL4-C17** écrits en entier.
- Registre `registres/decisions.md` : R-2158, R-2167, R-2191, R-2197, R-2198, R-2233 (et toute ligne qui nomme P3-bis depuis R-2158, par `git grep -n "P3-bis" -- registres/decisions.md`).

## Mandat
1. Appliquer **les dix-sept couples CL4-C01 à CL4-C17 tels qu'écrits**, par **un script à toi** (nom neuf), chaque « ancien » trouvé une fois ; sections gelées touchées (« Plan d'analyse » : C05, C08, C10 ; « Liste d'arrêt » : C07, C09) déclarées une par une, avec leur raison ; **aucune hypothèse, prédiction, signe ni seuil ne change** ; si un couple l'exigeait, arrête-toi et signale-le (nœud).
2. Porter l'état des bloquants de procédure, par couples neufs déclarés (hors sections gelées) :
   - **CL4-07 levé** (R-2198) : `registres/go.md` à huit colonnes ; cite-le **par commit** (`cbc9c5ce589f6b07aac26bd313ca581cadc5db42`, dernier commit qui le change) et non par empreinte vivante (CL4-16) ;
   - **CL4-08 levé** (R-2233) : voie retenue par la mère pour P-10 (empreinte orpheline renommée en note scellée, contenu gardé, commit `62a91e64` de `main`) ; la branche de scellement doit porter ce commit avant S ;
   - **CL4-11 levé** : `prep/p3bis-lanceur-v1` récupérée, commits `614fd5da` et `8ad29273` présents dans le clone ;
   - **CL4-01** : contre-lecture différentielle courte de `a1de3915` rendue (`845c4de5…`, R-2158) ;
   - **CL4-06 ouvert** : place disque (≈ 13,0 Go exigés, ≈ 5 Go libres ici) : P-2, P-4 et P-6 se joueront sur une machine qui a la place ; ne change pas `PLACE_MIN_KO` ;
   - **CL4-13** : date du rendez-vous « proposée » jusqu'au défaut du 11 novembre vers 16:03 UTC (R-2167) : scellement après le défaut ou le mot de Lazar ; écris-le.
3. Marqueurs : garde ceux de la table de la contre-lecture 4 (`TESTS_ATTENDUS_P3BIS`, `LONGUEURS_P3BIS`, `EMPREINTE_CONSIGNES_P3BIS`, `EMPREINTE_CONFIG_P3BIS`, `CHAINE_P3BIS`, `CONTRE_LECTURE_4_P3BIS` à remplir par l'empreinte du rapport de la contre-lecture 4 si la consigne de ce marqueur le permet) et `CANDIDAT_RELU` ; une occurrence chacun ; liste-les à l'en-tête ; vérifie par `controle_ia.prereg.problemes`.
4. En-tête : statut « brouillon 12 ».

## Sorties (noms neufs, scellés ; brouillon 11 intact)
`brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon12.md`, `…-brouillon12-couples-v1.json`, `…-brouillon12-faire-v1.py`, `…-brouillon12-journal-v1.md` (couples, comparaison programmée des sections gelées au brouillon 11, écarts, questions Q-n avec recommandation). Rapport final : chemins, empreintes, nombre de couples, marqueurs restants, questions pour la mère.
