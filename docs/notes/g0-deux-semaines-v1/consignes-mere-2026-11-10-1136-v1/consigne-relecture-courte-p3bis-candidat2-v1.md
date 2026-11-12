# Consigne : relecture courte de l'écart du candidat 1 au candidat 2 de P3-bis — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 13:59 UTC (heure relevée par `date -u`). Destinataire : un **relecteur neuf, Claude Fable 5.2**, qui n'a écrit ni P3-bis, ni ses couples, ni son code, ni sa chaîne, ni aucune de leurs contre-lectures ou relectures, et **qui ne lit pas T0.7** (ni texte, ni brouillons, ni notes, ni module hors `t07/plancher_v2.py` par `git show`).

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

Exception à la règle 4 : aucune. Tu n'écris que `brouillons/P3-bis-temoin-positif-v1/P3-bis-candidat2-relecture-courte-v1.md` (nom neuf) et ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-relecture-c2/`. Aucun commit, aucune dépense. Sceller ta sortie (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`).

## Ce qui fonde ce travail (registre)
R-2342, R-2344 (relecture du candidat 1), **R-2345** (défaut de définition de `CHAINE_P3BIS` : circularité, décision), R-2349 (P-9), **R-2352** (mot de Lazar ; décisions Q-1 à Q-5).

## À relire
- Départ : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat1.md` (`9a56a657b1fad1e23b0cc11e41831f066eed48674159dbc55c2a869aa56c4271`).
- Arrivée : la **sortie à blanc v2** `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat2-pieces/P3-bis-preenregistrement-v1-candidat2-a-blanc-v2.md` (`bfd9d889fc8b2014bd54bed2076212d064bdfd53c3c88204de79e1d67b3251fd`) ; le texte final ne diffère d'elle que par la phrase de la « date tenue » (« mot de Lazar, R-2352 » au lieu de « défaut échu, R-0000 ») : la mère le vérifiera par programme.
- Couples `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat2-pieces/P3-bis-preenregistrement-v1-candidat2-couples-v2.json` (`bffe8e38…`, 22 couples C2-01 à C2-22), script `…-faire-v2.py`, journal à blanc v2, épingles proposées `P3-bis-epingles-proposees-v1.json` (`0fb1443a…`).
- Chaîne v2 au commit du code `5e4575259478af3611e2c7fb1313342912caf484` (`git show`) : `controles_avant_depense_p3bis_v2.sh`, `sceller_p3bis_v2.sh`, `recuperation_p3bis_v2.sh`.

## Mandat
1. Par programme : couples réappliqués au candidat 1 = sortie à blanc, à l'octet ; défaits = candidat 1 ; sept sections gelées : six égales à l'octet au candidat 1, « Plan d'analyse » = candidat 1 + N-1 seul ; aucun marqueur ; `prereg.problemes` vide.
2. **Circularité levée ?** Le texte ne cite plus aucune empreinte qui dépende de lui-même (contrôles épinglés, journaux canoniques, ce texte) ; la règle d'épinglage écrite est exacte au regard des scripts (`releve` du bloc 4, étapes 4, 5, 7 du scellement, épingle `PY` de la récupération) ; les phrases corrigées (C2-03, C2-08, C2-13 à C2-15, C2-19 à C2-21) disent juste ; rien d'autre du texte ne promet ces citations.
3. **Épingles proposées** : chaque valeur juste (chemins sous `brouillons/` là où l'exigent les scripts ; neuf rapports cités par chemin et empreinte complète dans le texte, chacun égal à son compagnon sur `main`) ; liste des pièces à verser complète au regard des étapes 4 et 5 du scellement.
4. Lignes P-9 et `CANDIDAT_RELU`, en-tête et table « du candidat 1 au candidat 2 » : exactes.

## Sortie
Rapport scellé : verdict en une ligne (« relu, conforme » ; ou « à corriger » avec couples exacts « ancien → nouveau ») ; constats numérotés avec preuve (commande, sortie, ligne). Rapport final : chemin, empreinte, verdict, ton modèle.
