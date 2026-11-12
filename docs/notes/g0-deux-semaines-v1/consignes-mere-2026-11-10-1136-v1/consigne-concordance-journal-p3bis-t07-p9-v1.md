# Consigne : préalable P-9 de P3-bis — concordance du journal des ouvertures rejouée sur les commits finaux — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 13:26 UTC (heure relevée par `date -u`). Destinataire : un **agent neuf**, qui n'a écrit ni P3-bis, ni T0.7, ni leur code, ni leurs contre-lectures. Tu lis des fichiers de T0.7 : tu seras **exclu ensuite de tout rôle de lecteur de P3-bis** (dis-le dans ton rapport).

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

Exception à la règle 4 : aucune. Tu n'écris que sous `docs/notes/g0-deux-semaines-v1/concordance-journal-p3bis-t07-v2/` (dossier neuf) et dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-p9/`. Aucun commit. Sceller chaque sortie (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`).

## Le préalable (texte du candidat 1 de P3-bis, `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat1.md`, `9a56a657…`, ligne P-9 de la section « Préalables »)
« Concordance du journal rejouée sur les commits finaux des deux côtés (écrivain : commit du code cité ; lecteur : commit de la ligne `CODE-T07`), le lecteur de T0.7 appliquant en entier le prédicat du plan, point 8 (R-2103), les cas « retour chariot seul » et « fins de ligne mêlées » ajoutés au rejeu (C-1 de la contre-lecture `845c4de5…`) ; sortie versée : aucune discordance ; une discordance est un nœud. »

## Commits finaux
- Écrivain : commit du code de P3-bis `5e4575259478af3611e2c7fb1313342912caf484` (le module qui écrit le journal des ouvertures : à identifier au plan, point 8, de P3-bis, et dans `src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py` et ses dépendances).
- Lecteur : C7 = `b4cd9953d199dd8f220f5162e5868c5b00fd392d` (ligne `CODE-T07` de `registres/scellements-v1.md`, fichier `registres/code-t07/CODE-T07-v2.json`) : `src/controle_ia/t07/journal_p3bis_v1.py` et ce qu'il importe ; prédicat du plan, point 8, du texte scellé de T0.7 (`prereg/T0.7-sondes-v0-v1.md`, `d7d180ec…`), appliqué en entier (R-2103).

## À lire
Le rapport v1 (`docs/notes/g0-deux-semaines-v1/concordance-journal-p3bis-t07-v1/rapport-concordance-journal-v1.md`) et son script (`essai_concordance_journal_v1.py`, `b30c9db7…`) ; la contre-lecture `845c4de5…` (constat C-1 ; chemin : à l'en-tête du candidat 1) ; R-2103 et les décisions qui ont traité D-1 à D-4 (à retrouver par `git grep -n 'D-1' registres/decisions.md` et lectures ciblées).

## Mandat
1. Écris `essai_concordance_journal_v2.py` (nom neuf ; reprends la v1) : code de l'écrivain importé d'une extraction de `5e457525` (src seulement), code du lecteur d'une extraction de C7 (src seulement), chacun dans son bac à sable ; empreintes des modules relevées et comparées aux compagnons à leur commit.
2. Rejoue les scénarios de la v1 (modes, codes de refus, `deja-ouverte`, E-3, E-8, E-9), plus « retour chariot seul » et « fins de ligne mêlées » ; le lecteur applique le prédicat entier du plan, point 8 de T0.7.
3. Pour chaque discordance de la v1 (D-1 à D-4) : dis si elle tient aux commits finaux et comment elle a été traitée.
4. Rapport `rapport-concordance-journal-v2.md` : verdict en une ligne (« aucune discordance » ou la liste) ; une discordance est un nœud : ne corrige rien.

## Sortie
Script, sortie brute, rapport, scellés ; rapport final : chemins, empreintes, verdict, ton modèle.
