# Consigne : rédiger le candidat 2 de T0.7 (remède (a'), 800 directions, plancher neuf des sondes figées de P3) et l'ordre d'exécution brouillon 6 — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 02:40 UTC (heure relevée par `date -u`). Destinataire : un **rédacteur neuf**, qui n'a écrit ni T0.7 (brouillons, candidat 1), ni son module, ni ses ordres, ni leurs contre-lectures, ni les notes de l'erreur de première espèce. Ayant lu T0.7, il est exclu ensuite de tout rôle de lecteur de P3-bis.

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

Exception à la règle 4 : aucune. Tu n'écris que sous `brouillons/` (noms neufs : `brouillons/T0.7-sondes-v0-v1-candidat2.md`, ses pièces sous `brouillons/T0.7-sondes-v0-v1-candidat2-pieces/`), sous `docs/procedures/` (nom neuf : `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6.md` et ses pièces `…-brouillon6-appliquer-v1.py`) et dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/t07-candidat2/`. Aucun commit, aucun appel de modèle, aucune dépense. Sceller chaque sortie : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`. Le conteneur a redémarré deux fois cette nuit : écris tes sorties tôt et souvent (journal tenu au fil), pour qu'une reprise soit possible.

## Ce qui fonde ce travail (lis les lignes du registre seulement)
- **Mot de Lazar** R-2285 : « (a') le remède, plus davantage de directions dans le plancher : un seuil du texte à changer : go ». C'est l'**autorisation** de changer, dans les sections gelées, la **définition de « au-dessus du plancher »** et le **nombre de directions** — et rien d'autre de gelé.
- R-2270 (défaut trouvé), R-2271, R-2273 (remède (a) codé), R-2296 (P3-bis prendra la même règle), **R-2298** (n_plancher = 800, notation par lots, réextraction des sondes figées de P3), **R-2299** (audit de P3 : deux réserves jointes à toute citation du nul de P3), **R-2304** (code rendu, configuration v7, « garde_principale » = « rapportee », repli), R-2269 (défauts de P-064 et P-065, qui remplissent `MOT_LAZAR_P064` et `MOT_LAZAR_P065`), R-2264 (vérification courte du candidat 1, couples VC1-A et VC1-B).

## À lire (empreintes à vérifier avant lecture)
- Texte de base : `brouillons/T0.7-sondes-v0-v1-candidat1.md` (`1718f2a0…`), ses pièces (`…-candidat1-pieces/` : script, couples, journal, configuration v5) ; vérification courte `prereg/contre-lectures/T0.7-sondes-v0-v1-candidat1-verification-courte-v1.md` (`ef3431a1…`).
- Notes de l'erreur de première espèce, sous `docs/notes/g0-deux-semaines-v1/t07-module-v2/` : v1 `erreur-premiere-espece-lectures-decisives-t07-v1.md` (`8e996ab0…`), v2 `…-v2.md` (`5ccf0940…`, section 5 : remède (a)), **v3 `…-v3.md` (`760a562c…`)** : taux, puissance, coût, réserve à 36 tâches au plafond, sondes figées de P3.
- Audit de P3 : `docs/notes/g0-deux-semaines-v1/audit-p3-regle-plancher-v1/audit-verdict-p3-regle-plancher-v1.md` (`57f16378…`), section 7 (réserves).
- Code : rapport `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v1.md` (`cb31edc8…`), configuration v7 au même dossier (`3701407c…`, canonique `4ff92c8e…`) ; modules par `git show 0d0c5da4061c28d808c3aa3b53c9a9a5e56a3a07:src/controle_ia/t07/<fichier>` (`plancher_v3.py`, `reextraction_p3_v1.py`, `lecture_v4.py`) ; règle (a) dans `plancher_v2.py` au même commit.
- Ordre : `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md` (`d0b75d16…`) et son script d'application.
- Registre GO : GO-2026-11-10-04 et GO-2026-11-10-06 (20 USD, non cumulés).

## Mandat — texte (couples appliqués par un script à toi, nom neuf ; chaque « ancien » présent une fois)
1. **Seuil** (section gelée, changement autorisé) : « au-dessus du plancher » devient la règle (a) : borne basse de l'intervalle percentile, par blocs de tâches, de la différence D = aire de la sonde − quantile 0,95 des aires des directions du plancher, recalculées sur les mêmes tirages, **strictement positive** ; niveau des lectures décisives inchangé (`niveau_decisif`) ; `quantile_plancher` inchangé ; **`n_plancher` = 800**. Écris la règle exactement comme la code `plancher_v2.comparer_difference_au_plancher` (cite-la).
2. **Plan d'analyse et Métrique** : recette du plancher (l. 1078-1100 du candidat 1 environ) à 800 directions, notation par lots (`plancher_v3`, égale à la boucle à 10⁻¹² de l'échelle, contrôle en ligne partiel déclaré) ; fonction de lecture de l'étape B = celle de la v4.
3. **Planchers des sondes figées de P3** (ligne 381 du candidat 1 et tout passage qui dit « les 200 directions de P3 réutilisées ») : réextraction à l'étape A (avant toute autre extraction), témoin déterministe et seconde garde décisifs, paliers « identique / processeur / carte / échec » et leurs seuils tels que codés, sonde linéaire refaite **rapportée** (`garde_principale` = « rapportee », R-2304) ; 800 directions neuves sous la graine dérivée (clé `plancher/<sonde>`) ; les 200 de P3 notées en **lecture descriptive** ; **repli** (R-2304) : bras arrêté → lectures décisives de cette sonde figée en « échec », motif « plancher neuf de la sonde figée non établi », aucune lecture décisive contre les 200 de P3, organisme selon la règle gelée (U, E, Z) ; T7-P1 n'est plus une réplication de P3 pour cette sonde (dis-le là où le texte parle de réplication).
4. **Puissance** : remplace les grandeurs de puissance et d'aire minimale détectable par celles de la note v3 et du rejeu du code (cite chemins et empreintes) ; écris la perte de puissance du remède ; **réserve** de la note v3 : à 36 tâches au plafond, estimation ponctuelle 1,4 à 1,8 fois le nominal, défaut résiduel non établi.
5. **P3 cité** : partout où le texte cite le nul de P3, joins les deux réserves de R-2299 telles quelles.
6. **Calcul et dépense** : devis de l'étape A du rapport du code (+ 0,23 h attendu, + 0,66 h au pire ; variante B ≈ 5,5 à 7,4 USD attendu, 12,5 à 16,4 USD au pire, sous 20 USD) ; réserve CLE-12 aggravée (marge ≈ 0,45 h au pire).
7. **Marqueurs** : `MOT_LAZAR_P064` et `MOT_LAZAR_P065` remplis par R-2269 avec les couples VC1-A et VC1-B ; `EMPREINTE_CONFIG_T07` → configuration v7 à son chemin **final** nommé par l'ordre brouillon 6 (comme au candidat 1 : copie sous `prereg/` faite par la mère au scellement ; donne le chemin) ; `EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07` → l'ordre brouillon 6 (ton fichier, son empreinte) ; `ENTROPIE_T07` inchangée ; **C7 et la ligne CODE-T07 laissés à la mère** (le code neuf sera fusionné dans `main` avant le scellement ; le module compte 26 fichiers) : un marqueur explicite, nommé, que `controle_ia.prereg.problemes` relève.
8. **Sections gelées** : vérifie par programme que tout le reste des sections gelées est égal à l'octet au candidat 1 ; liste chaque changement gelé (section, ancien, nouveau, motif R-…) ; **aucune hypothèse, prédiction, signe ni autre seuil ne change** ; si un changement non autorisé te semble nécessaire, arrête-toi et écris-le (nœud).
9. En-tête et section « Contre-lecture » : statut « candidat 2 », ce qui change depuis le candidat 1 et pourquoi ; à contre-lire par une vérification courte neuve avant scellement.

## Mandat — ordre d'exécution brouillon 6
Depuis le brouillon 5, par script : commandes `lecture_v4` (`repli-seul`, `passe-blanc`, `etape-a-apres-repli` ; `repli-recalcul` refusé), `CUBLAS_WORKSPACE_CONFIG=:4096:8` exporté pour le processus de l'étape A, préférence d'hôte EPYC (ou `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2`, non éprouvé, déclaré), révision de P3 (`0e9e39f2…`) dans le cache local, condition P8 `ANT0` ≤ 3,6 USD, devis et marge de la minuterie, configuration v7, CODE-T07 à 26 modules ; tout le reste égal à l'octet (vérifié par programme).

## Sorties (scellées ; candidat 1 et brouillon 5 intacts)
Candidat 2, couples, script, journal, ordre brouillon 6 et son script. `controle_ia.prereg.problemes` sur le candidat 2 ne doit relever que le marqueur de C7 et CODE-T07. Rapport final : chemins, empreintes, liste des changements gelés, marqueurs restants, questions, ton modèle.
