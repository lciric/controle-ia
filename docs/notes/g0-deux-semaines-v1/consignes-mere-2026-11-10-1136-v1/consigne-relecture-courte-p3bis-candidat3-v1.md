# Consigne : relecture courte de l'écart du candidat 2 au candidat 3 de P3-bis — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 15:02 UTC (heure relevée par `date -u`). Destinataire : un **relecteur neuf, Claude Fable 5.2**, qui n'a écrit ni P3-bis, ni ses couples, ni son code, ni sa chaîne, ni aucune de leurs contre-lectures ou relectures, et **qui ne lit pas T0.7**.

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

Exception à la règle 4 : aucune. Tu n'écris que `brouillons/P3-bis-temoin-positif-v1/P3-bis-candidat3-relecture-courte-v1.md` (nom neuf) et ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-relecture-c3/`. Aucun commit, aucune dépense. Sceller ta sortie.

## Ce qui fonde ce travail (registre)
R-2356, R-2358 (candidat 2 relu conforme), **R-2367, R-2373, R-2374** (bancs corrigés au commit `68ded698ce1bbfd8815d7b7ab28557775e4d2e5b`, citables au scellement), **R-2375** (candidat 3 écrit).

## À relire
- Départ : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat2.md` (`eb7e5b8b671a71a745323135fc6aed5b0f30ad28e515575518189a2d22d71ecc`).
- Arrivée : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat3.md` (**`76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb`**), couples `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat3-pieces/P3-bis-preenregistrement-v1-candidat3-couples-v1.json` (`5dba04f8…`, 17 couples), script `…-candidat3-faire-v1.py` (`9d406236…`), épingles proposées `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat3-pieces/P3-bis-epingles-proposees-v2.json` (`85500d90…`).
- Chaîne v2 : commit du code `5e4575259478af3611e2c7fb1313342912caf484` et correction des bancs `68ded698` (`git show`) ; `sceller_p3bis_v2.sh`, `controles_avant_depense_p3bis_v2.sh` (épingles, `releve`, bloc 14).

## Mandat
1. Par programme : couples réappliqués au candidat 2 = candidat 3 à l'octet ; défaits = candidat 2 ; **sept sections gelées égales à l'octet au candidat 2** ; aucun marqueur ; `prereg.problemes` vide ; phrase de la date tenue inchangée.
2. **Chaîne** : douze fichiers cités au commit du code, trois bancs au commit `68ded698` (empreintes égales à `git show 68ded698:…` et aux compagnons) ; aucune empreinte qui dépende du texte lui-même (circularité, R-2345) ; règle (b) exacte au regard des scripts et de la branche `scellement/p3bis-v2`.
3. **Rapports** : onze, chacun cité par chemin et empreinte complète, égal à son compagnon sur `main` ; épingles v2 justes ; pièces à verser complètes au regard des étapes 4 et 5 du scellement.
4. Table « du candidat 2 au candidat 3 » et en-tête exacts.

## Sortie
Rapport scellé : verdict en une ligne (« relu, conforme » ou « à corriger » avec couples exacts) ; constats numérotés avec preuve. Rapport final : chemin, empreinte, verdict, ton modèle.
