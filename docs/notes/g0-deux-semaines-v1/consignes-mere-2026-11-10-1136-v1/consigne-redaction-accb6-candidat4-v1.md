# Consigne : rédiger le candidat 4 du barreau 6 (« accumuler bat le score action par action ») après le scellement de T0.7 — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 11:51 UTC (heure relevée par `date -u`). Destinataire : un **rédacteur neuf**, qui n'a écrit ni le barreau 6 (brouillons, candidats 1 à 3), ni son code, ni ses contre-lectures, ni sa revérification, ni T0.7. Ayant lu T0.7, il sera exclu ensuite de tout rôle de lecteur de P3-bis.

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

Exception à la règle 4 : aucune. Tu n'écris que sous `brouillons/accumulation-barreau6-v1/` (noms neufs : `accumulation-barreau6-v1-candidat4.md` et `accumulation-barreau6-v1-candidat4-pieces/` : couples, script, journal) et dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/accb6-candidat4/`. Aucun commit, aucun appel de modèle, aucune dépense. Sceller chaque sortie : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`. Le conteneur redémarre parfois : écris tes sorties et ton journal au fil de l'eau.

## À lire (empreintes à vérifier)
- **Base** : `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat3.md` (`d48fb8a3…`) et ses pièces (couples C3, script, journal) ; vérification courte du candidat 2 (`prereg/contre-lectures/accumulation-barreau6-v1-candidat2-verification-courte-v1.md`, si présente ; R-2278).
- **Revérification sur T0.7 scellé** : `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/reverification-t07-scelle-v1.md` (`80f06ac4…`), couples proposés `…/reverification-t07-scelle-v1-pieces/couples-proposes-v1.json` (`771abfaf…`, RV-01 à RV-11, chaque « ancien » une fois dans le candidat 3).
- **Contre-lecture du code v1** : `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/contre-lecture-code-accb6-v1.md` (`67614af4…`), points CCB-2 à CCB-7 « à trancher au candidat final ».
- **Code v2** : rapport `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/rapport-developpeur-accb6-v2.md` (`72642740…`) ; commit `282e295ec8e825b9c045bd30ebfdac3cbe55496f` (branche `prep/accumulation-b6-code-v2`, par `git show`) ; sortie neuve de l'énumération `scripts/enumeration-etats-accb6-v2-code-v2.txt` (au commit, `6b078d6c…`).
- **T0.7 scellé** : `prereg/T0.7-sondes-v0-v1.md` (`d7d180ec…`), ligne `SCELLEMENT-T07` et ligne `CODE-T07` de `registres/scellements-v1.md`, note `docs/notes/g0-deux-semaines-v1/t07-module-v2/erratum-concordance-adaptateur-t07-scelle-v1.md` (`f5936762…`).
- Décisions R-2272 à R-2281, R-2321, R-2330, R-2336 de `registres/decisions.md` (ces lignes).

## Mandat (couples appliqués par un script à toi ; chaque « ancien » une fois)
1. **RV-01 à RV-11** tels qu'écrits, avec **l'option (a) de E-2** (décision de la mère, R-2330) : le membre « au-dessus de son plancher » garde la règle d'intervalle contre quantile, **déclarée distincte** de la règle de T0.7 scellé (différence appariée), avec la réserve écrite qu'il est plus facile à obtenir que son homonyme de T0.7 ; le niveau des conclusions tient à l'intervalle de Δ.
2. **Code** : `COMMIT_CODE_ACCB6` = `282e295ec8e825b9c045bd30ebfdac3cbe55496f` partout où le texte cite le commit du code (en-tête, « Code », lignes de registre, plan) ; empreintes des fichiers changés (`etats_v1.py` `81e4a19b…`, `lecture_v1.py` `1f4c035f…`) ; essais (195), mutations (128 sur 128), CCB-1 levé ; énumération : sortie neuve (`6b078d6c…`), seule la ligne 3 diffère, aucune règle d'état ni phrase changée.
3. **CCB-2 à CCB-7** (contre-lecture `67614af4…`) : écris les phrases recommandées (CCB-2 : erreur hors `GardeArret` après le manifeste sans `arret-accb6.json` ; CCB-3 : audit de symétrie à aire exactement 1 ; CCB-4 : sortie standard de la commande détournée ; CCB-5, CCB-6 : phrases à déclarer ; CCB-7 : au lancement, vérifier que `sondes/evaluation.py`, `sondes/temoins.py`, `manifeste.py` égalent le commit cité).
4. **Marqueur `REVERIFICATION_T07_SCELLE`** : rempli par le chemin et l'empreinte de la revérification (`80f06ac4…`), son verdict (« écarts », E-1 à E-5) et leur traitement (code v2 `282e295e`, couples RV-01 à RV-11 de ce candidat) ; les renvois au brouillon 22 de T0.7 deviennent des renvois à T0.7 scellé (chemin, empreinte), là où la revérification les a confirmés.
5. **Puissance** : la section simule 200 directions ; dis si 800 change quelque chose à ses nombres (le plancher ne fait que restreindre) ; sinon écris la réserve « non resimulé à 800 ».
6. **Sections gelées** : liste chaque changement (G4-xx : section, ancien, nouveau, motif R-…) ; vérifie par programme que défaire tes couples redonne le candidat 3 à l'octet ; **aucun signe, seuil, niveau ni règle d'état ne change** hors ce que R-2330 décide ; sinon arrête-toi et écris-le (nœud).
7. `controle_ia.prereg.problemes` sur le candidat 4 : vide (aucun marqueur restant).

## Sortie
Candidat 4, couples, script, journal, scellés ; rapport final : chemins, empreintes, changements gelés, questions, ton modèle.
