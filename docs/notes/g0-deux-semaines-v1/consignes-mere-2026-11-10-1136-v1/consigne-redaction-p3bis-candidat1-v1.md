# Consigne : rédiger le candidat 1 de P3-bis (témoin positif) sous la règle (a') — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 12:44 UTC (heure relevée par `date -u`). Destinataire : un **rédacteur neuf**, qui n'a écrit ni P3-bis, ni son code, ni sa chaîne, ni leurs contre-lectures, et **qui ne lit pas T0.7** (ni son texte, ni ses brouillons, ni ses notes : P3-bis doit rester écrit sans lecture de T0.7, R-2237 ; seul le module `t07/plancher_v2.py` que P3-bis importe peut être lu, par `git show`).

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

Exception à la règle 4 : aucune. Tu n'écris que sous `brouillons/P3-bis-temoin-positif-v1/` (noms neufs : `P3-bis-preenregistrement-v1-candidat1.md` et `P3-bis-preenregistrement-v1-candidat1-pieces/` : couples, script, journal, configuration du candidat) et dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-candidat1/`. Aucun commit, aucun appel de modèle, aucune dépense. Sceller chaque sortie : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`. Le conteneur redémarre parfois : écris au fil de l'eau.

## Ce qui fonde ce travail (lis ces lignes de `registres/decisions.md`)
R-2295 (phase 1 des préalables), R-2296 (P3-bis prend la règle (a')), R-2299 (réserves du nul de P3), R-2320 (k = 800), R-2337 (code `5e457525`, options RA-23 et RA-24 **acceptées**), R-2340 (contre-lecture courte du code : « citable au scellement », CLP-04, **CLP-05 à porter au texte**).

## À lire (empreintes à vérifier)
- Base : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon12.md` (`07b16063…`), ses sections « Préalables » et « Marqueurs restants ».
- Couples du développeur : `docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/couples-proposes-p3bis-regle-a-v1.json` (`41f8c885…`, 37 couples RA-01 à RA-37 contre le brouillon 12 et la configuration brouillon 1 `8ab04d54…`) et le rapport `rapport-code-p3bis-regle-a-v1.md` (`0f57e202…`) ; contre-lecture courte `contre-lecture-courte-code-p3bis-regle-a-v1.md` (`03f1bb59…`).
- Préalables de la phase 1 (session fille, branche `prep/p3bis-prealables-v1`, commit `dfb1ed7b`, à lire par `git show`) : rapport `docs/notes/g0-deux-semaines-v1/p3bis-prealables-v1/rapport-prealables-p3bis-phase1-v1.md` (`d62c0c54…`), longueurs attendues (`7c94d43c…`) et mesurées (`4e5093bc…`), consignes posées en `prereg/P3-bis-consignes-v1.md` sur cette branche.

## Mandat (couples appliqués par un script à toi ; chaque « ancien » une fois)
1. **Les 37 couples RA** tels qu'écrits, options **RA-23 et RA-24 comprises** ; la configuration du candidat (`n_plancher` = 800 par RA-35) écrite sous un nom neuf dans tes pièces, empreinte canonique calculée par `manifeste.config_canonique`.
2. **CLP-05** au texte (« Critères de lecture gelés » ou « Plan », là où le verdict lit l'issue) : le lecteur du verdict **exige** au manifeste de la lecture complémentaire la commande `lecture_p3bis_v2` et la présence de `resultat.etat_decisif.regle` ; sinon « non lisible », nœud. Couple exact, rattaché à R-2296, R-2340.
3. **Code** : `COMMIT_CODE_P3BIS` = `5e4575259478af3611e2c7fb1313342912caf484` ; identité et empreintes du code (fichiers neufs et `t07/plancher_v2.py` = blob de C7) ; P-7 fait (`03f1bb59…`) ; CLP-04 (trois essais à ajouter au prochain commit d'essais) et notes CLP-06 à CLP-09 dans « Ce que le code et la chaîne doivent changer » ou « Préalables ».
4. **Marqueurs remplissables** : `TESTS_ATTENDUS_P3BIS` (N = 531 de la liste ciblée v2, phase 1 ; dis si les 31 essais neufs changent N), `LONGUEURS_P3BIS` (sorties de la phase 1, chemins et empreintes ; A = T = B sur 60 tâches), `EMPREINTE_CONSIGNES_P3BIS` (sha256 des consignes relues, copie de la phase 1), `EMPREINTE_CONFIG_P3BIS` (ta configuration du candidat). **Laisse explicitement** : `CHAINE_P3BIS` (chaîne v2, journaux canoniques des bancs et des répétitions : phase 2, P-5, P-6) et `CANDIDAT_RELU` (relecture courte de l'écart du brouillon 11 au candidat, après toi) ; date du rendez-vous : défaut de P-11 le 2026-11-11 vers 16:03 UTC (la mère le consigne ; écris la place).
5. **Sections gelées** : liste chaque changement (C1-xx : section, ancien, nouveau, motif R-…) ; vérifie par programme que défaire tes couples redonne le brouillon 12 à l'octet ; aucune hypothèse, prédiction, signe, niveau, jeu décisif, sonde décisive ni issue ne change ; sinon arrête-toi et écris-le (nœud).
6. `controle_ia.prereg.problemes` ne relève que `CHAINE_P3BIS` et `CANDIDAT_RELU`.

## Sortie
Candidat 1, couples, script, journal, configuration, scellés ; rapport final : chemins, empreintes, changements gelés, marqueurs restants, questions, ton modèle.
