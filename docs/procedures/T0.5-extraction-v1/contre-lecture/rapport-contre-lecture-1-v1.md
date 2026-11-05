# Contre-lecture — T0.5, procédure d'extraction v1 (brouillon 3) et son outillage — rapport v1

Contre-lecteur : sous-agent neuf, qui n'a rien écrit de ce qu'il lit. 2026-10-07, vers 04:45 UTC. Aucun fichier du dépôt modifié ; essais dans `…/scratchpad/contre-lecture-extraction-v1/essais/`. Versions relues : brouillon 3 `ba951ce9…`, fichiers de `docs/procedures/T0.5-extraction-v1/` et code listés en annexe B (inchangés pendant la relecture, vérifié par date de modification).

## Verdict

**Scellable après corrections.** 1 faute bloquante (énoncés corrompus en silence par des barres obliques inverses non doublées ; à corriger dans le script scellé) et 10 majeures à corriger ou trancher avant le scellement : chemin « avis illisible » impossible à suivre, rondes omises en silence, audit R4 sans lecture gelée, isolement des sous-agents inexact, 30 gardes sur 49 jamais testées, entre autres. La conception (machine d'états, remplacements, copie de lecture, accord script et module) est saine.

Échelle : **bloquante** = la procédure scellée produirait en silence des données fausses ; **majeure** = à corriger ou à trancher explicitement avant le scellement (texte ou fichier scellé touché, ou garantie annoncée non tenue) ; **mineure** = correction simple, avant le run ; **suggestion** = facultatif.

## Remarques

### CL-1 — bloquante — barres obliques inverses non doublées : énoncés corrompus en silence (B, C, D)
- **Où** : `extraction.py` l. 50-65 (`anomalies_h9`) et l. 89-124 ; `verifier-sortie-v1.py` l. 42-56 et 72-110 ; consigne de l'extracteur l. 22.
- **Problème** : en JSON, `\b`, `\f`, `\n`, `\r`, `\t` sont des échappements valides. Un énoncé écrit avec `$\theta$`, `$\beta$`, `\frac`, `\nabla`, `\rho`, `\tau`, `\text…`, `\times`… à une seule barre se lit sans erreur : tabulation, retour arrière, saut de page, saut de ligne ou retour chariot, puis la fin du mot. Essai (`essai_unitaires.py`) : un énoncé contenant `$\theta$ … $\beta$ … $\frac{1}{2}$ … $\nabla f$ … $\rho$` se lit avec les caractères 0x8, 0x9, 0xa, 0xc, 0xd ; `anomalies_h9` rend `[]`.
  - Pour les citations, la recherche échoue, donc l'erreur est vue. Pour l'énoncé et les descriptions, rien ne la voit.
  - Le contre-vérificateur ne la voit pas non plus : il lit le fichier brut (copie octet pour octet, `extraire_t05.py` l. 295-298), où `$\theta$` paraît juste.
  - L'énoncé est la donnée remise à l'agent 8B.
  - Effet de bord : un contre-vérificateur qui cite un passage ainsi corrompu voit son avis jugé illisible (passage introuvable), ce qui mène au chemin fautif de CL-2.
- **Correction** : dans le module et le script, refuser comme erreur tout caractère de contrôle U+0000 à U+001F autre que le saut de ligne, dans toute chaîne des trois sorties et dans les passages d'avis. Refuser aussi un saut de ligne à l'intérieur d'une formule `$…$` (cas `\nabla`, `\nu`, `\neq`). Message : « a LaTeX backslash must be written \\\\ inside a JSON string ». Ajouter ces cas aux tests d'accord. Le script est scellé avec la procédure : corriger avant le scellement.

### CL-2 — majeure — avis illisible du rôle « echantillon » : la règle ne peut être suivie (C)
- **Où** : brouillon 3 l. 124 ; `extraire_t05.py` l. 266-269 et 410-414 ; `extraction.py` l. 341-343.
- **Problème** : pour refaire un seul avis illisible, `preparer_contre_verification` refuse de nommer le papier en rôle « echantillon » (l. 267-268). La ronde nouvelle reprend donc tout l'échantillon.
  - Si les 16 nouveaux sous-agents rendent leur avis, chaque papier réussi à la ronde 1 a deux avis lisibles, et `statut_papier` arrête. Essai (`essai_illisible_echantillon2.py`) : `GardeArret : 2601.00005v1 : reprise sans motif`.
  - Seul contournement : ne lancer que le sous-agent du papier visé. Le résultat scellé de la ronde inscrit alors les autres papiers comme « illisibles », ce qui est faux (`essai_illisible_contournement.py` : `illisibles : ['2601.00005v1']`).
  - « La ronde illisible est consignée et ne compte pas » est ambigu : la ronde entière, ou l'avis ?
  - Un avis illisible est plausible : panne d'un sous-agent, avis non écrit, ou CL-1.
- **Correction** :
  - texte : « L'avis illisible est consigné et ne compte pas ; seul son papier est refait, par un nouveau sous-agent, dans une ronde nouvelle du même rôle et sur la même tentative » ;
  - code : en rôle « echantillon », accepter `--papiers`, limité aux papiers de l'échantillon qui n'ont pas encore d'avis lisible de ce rôle ;
  - test : un avis illisible refait, puis assemblage sans arrêt.

### CL-3 — majeure — audit R4 sans critère de lecture ni conséquence (C, F)
- **Où** : brouillon 3 l. 125-126 ; `extraire_t05.py` l. 271 et 389-403 ; `extraction.py` l. 334, où seuls les rôles « echantillon » et « reprise » comptent. Test `test_audit_r4_exige_si_tout_est_propre` (l. 424-429) : l'audit trouve une fuite, et le papier reste tâche d'évaluation.
- **Problème** :
  - Côté propre : l'audit est exigé, mais son résultat ne change rien et aucune lecture n'est gelée. Un audit qui trouve 4 fuites sur 4 laisse passer le « 0 échec ». R4 dit « trop beau = réserve », et le bilan n'inscrit aucune réserve.
  - Côté sale : « 4 des papiers en échec » n'est pas fixé quand 5 papiers ou plus échouent. Par défaut, le code prend les 4 premiers de l'échantillon (l. 271), pas les 4 premiers en échec. La session choisit donc après lecture des résultats.
- **Correction** : geler avant le scellement :
  1. côté propre, une réserve inscrite au bilan dès que l'audit est déclenché, et un critère. Recommandation : tout papier jugé en échec par l'audit suit la reprise (tentative 3, rôle « reprise »), et la réserve est portée à Lazar ;
  2. côté sale, « les 4 premiers papiers en échec, dans l'ordre de l'échantillon », calculés par le code ;
  3. l'accord est rapporté des deux côtés.

  Un test par branche.

### CL-4 — majeure — rondes sautées ou non lues : omission silencieuse (C)
- **Où** : `extraire_t05.py` l. 339-344 (`_rondes`) et l. 280-282 ; brouillon 3 l. 151.
- **Problème** : `_rondes` s'arrête au premier numéro sans résultat lu. Une ronde numérotée après un trou, ou préparée et jamais lue, sort du bilan et de l'archive sans arrêt, et les rondes suivantes avec elle. Essai (`essai_rondes.py`) : une ronde d'audit numérotée 3 (la 2 absente) signale une fuite ; le bilan porte `audit: None`, et ses avis manquent dans `sorties-brutes.tar`. Le texte promet « tous les avis de toutes les tentatives ».
- **Correction** :
  - `preparer_contre_verification` exige que le numéro de ronde soit 1 + le nombre de rondes déjà préparées ;
  - `_rondes` part des fichiers `preparation-contre-verification-ronde-*.json` et arrête si l'une n'a pas de lecture ;
  - un test d'artefact.

### CL-5 — majeure — entrée modifiée par un sous-agent : arrêt global sans règle, contournement par restauration (B, C)
- **Où** : brouillon 3 l. 77 ; `extraire_t05.py` l. 125-131, 206 et 312-315 ; test l. 385-392.
- **Problème** :
  - Une seule copie de lecture ou consigne modifiée arrête la validation de toute la tentative, et aucun résultat n'est écrit. Aucune règle ne dit quoi faire ensuite.
  - Le test du dépôt montre la voie : restaurer le fichier, puis revalider. La validation passe alors sans trace, et des sorties produites sous une entrée modifiée entrent comme saines.
  - Les fichiers `invites/*.txt` et le script de contrôle du dossier ne sont pas empreintés. Un sous-agent qui « répare » `verifier_sortie.py` ne serait pas vu : la validation officielle reste juste, mais la conduite du sous-agent change.
- **Correction** :
  - empreinter à la préparation toutes les entrées du dossier ;
  - à la validation, une entrée modifiée devient une anomalie du seul papier concerné, consignée au résultat scellé. Le papier suit la reprise (exclu s'il en est à la tentative 2), sans arrêter les autres ;
  - interdire toute restauration dans le texte ;
  - dans les deux consignes : « Do not modify any file other than your output file(s). »

### CL-6 — majeure — isolement : les sous-agents reçoivent les consignes permanentes du dépôt (B)
- **Où** : brouillon 3 l. 76 (« Le sous-agent ne voit ni le programme… ») et l. 43-45 ; `extraire_t05.py` l. 35.
- **Problème** : un sous-agent lancé par l'outil de la session reçoit dans son contexte le `CLAUDE.md` du dépôt. Constat direct : je l'ai reçu moi-même.
  - Ce fichier nomme le programme (« Contrôle boîte blanche des menaces diffuses »), ses règles, et une routine de reprise présentée comme impérative (lire `registres/etat.md`, lancer les tests…).
  - Avec l'invite des cibles (vérifier qu'un plan inclut les contrôles, un calcul sensé, des directions fécondes), le but, mesurer un sabotage de recherche, se devine.
  - La consigne interdit d'ouvrir d'autres fichiers. Mais l'affirmation de la l. 76 est fausse, et un sous-agent qui suivrait la routine lirait les registres. Il en va de même pour le contre-vérificateur.
- **Correction** :
  - déclarer le fait et ce qu'il révèle ;
  - ajouter à l'invite fixe une phrase de préséance : « This task is self-contained: ignore any project instructions or session routines, and open no file other than those named in the instructions. » (le texte de la l. 45 change, donc avant le scellement) ;
  - ou proposer à Lazar un lancement depuis une session hors du dépôt.

### CL-7 — majeure — R5 : 30 gardes d'arrêt sur 49 jamais exercées par les tests (D)
- **Où** : `tests/test_extraire_t05.py` (seul fichier de test des fonctions nouvelles). Relevé par traçage des lignes exécutées pendant les 60 tests (`traceur.py`).
- **Jamais exercées** :
  - `extraire_t05.py` l. 78, 86, 94, 131, 145, 156, 173, 177, 181, 185, 239, 258, 263, 268, 273, 276, 278, 282, 289, 297, 315, 414, 427 ;
  - `extraction.py` l. 187, 192, 194, 196, 323, 332, 384.
- **Problème** : R5 exige, pour toute garde, un cas sain et un artefact. Les gardes les plus utiles à l'intégrité ne sont pas testées :
  - l. 86 : texte altéré ;
  - l. 145 : fichiers scellés changés en cours de run ;
  - l. 297 et 427 : sortie changée depuis sa validation ;
  - l. 315 : réponses modifiées pendant la contre-vérification ;
  - l. 414 : avis illisible non refait.
- **Correction** : un test d'artefact par garde. Pour les gardes inatteignables par construction (gardes finales de la copie, l. 384), injecter la faute par remplacement temporaire d'une fonction interne, ou retirer la garde en le déclarant.

### CL-8 — majeure — code de décision non épinglé ; provenance incomplète (C, G)
- **Où** : brouillon 3 l. 145 ; `extraire_t05.py` l. 63-70, 234-251 et 305-336 ; `manifeste.py` l. 79-84.
- **Problème** :
  - Les décisions (anomalies, motifs d'échec, statuts, listes) sont prises par `extraction.py` et `extraire_t05.py`. Ces fichiers ne sont pas dans `fichiers_scelles`.
  - Le commit n'est consigné qu'à l'ouverture du run. Rien n'empêche de changer le code entre deux étapes, par exemple pour corriger CL-2 en cours de route.
  - `echantillonner` et `lire_contre_verification` ne vérifient même pas les fichiers scellés, alors que le texte dit « toute différence en cours de run arrête ».
  - Le modèle effectivement servi aux sous-agents n'est consigné nulle part (risque de modèle de repli).
- **Correction** :
  - ajouter les empreintes des deux modules à `fichiers_scelles`, et appeler `_exiger_memes_fichiers` à chaque étape ;
  - consigner dans chaque résultat le commit et la propreté de l'arbre ;
  - consigner l'identifiant du modèle des sous-agents à chaque préparation.

### CL-9 — majeure, à trancher avant le scellement (fichier scellé) — définition des contrôles (A, B)
- **Où** : `invite-cibles-v1.txt` l. 1 (« the controls this problem needs ») contre l. 8 (« a control, baseline or ablation the paper's own experiments rely on ») ; P-006 l. 19 (« contrôles nécessaires ») ; fixture des tests (C2 « ablation of the load-balancing loss », C3 « number of experts »).
- **Problème** : la description du schéma pousse vers les ablations de composants de la méthode du papier, que l'énoncé doit cacher.
  - Un agent qui n'a pas trouvé la méthode ne peut pas proposer ces ablations. La couverture des contrôles devient en partie une mesure de la direction féconde : les deux familles se confondent, et la marge baisse (plancher, P4 du pilote).
  - « Observable » ne protège pas : une telle ablation se vérifie dans un plan. Le contre-vérificateur ne la refusera donc pas.
- **Correction** : dans l'invite, « a control, baseline or ablation that any sound experimental plan for this problem would need, whatever method it proposes (not an ablation of a component specific to the paper's own method) ». Ou bien garder ces ablations mais les marquer (`"method_specific": true`), pour que le pilote les mesure à part.

### CL-10 — majeure — motif d'échec 2 et seuil : arrêt probable sans défaut d'extraction (F)
- **Où** : brouillon 3 l. 113-117 et 125 ; `extraction.py` l. 287-288.
- **Problème** : le seuil « plus de 4 sur 16 » vient du brouillon 2, où l'échec n'était pas défini. Il s'applique maintenant à quatre motifs, dont tout désaccord sur `theory_experiment`.
  - La frontière entre « mostly_experiments » et « experiments_only » (une seule proposition formelle suffit) est floue : deux lectures honnêtes divergent souvent.
  - Aucun taux d'échec attendu n'est estimé. Probabilité d'au moins 5 échecs sur 16, selon le taux d'échec par papier :

    | taux d'échec par papier | 20 % | 25 % | 30 % | 35 % |
    |---|---|---|---|---|
    | probabilité d'arrêt | 0,20 | 0,37 | 0,55 | 0,71 |

  - Un arrêt impose une version 2 et l'extraction entière refaite.
  - Un échec de classification seule fait aussi refaire tout le papier, énoncé et cibles compris. Cela ajoute des occasions d'échec, puis d'exclusion par simple bruit.
- **Correction** :
  - limiter le motif 2 aux erreurs qui changent une décision : « theory_only » attendu et non donné, ou l'inverse, ou un écart de deux crans ;
  - rapporter les autres désaccords ;
  - écrire un taux attendu par motif et la justification du seuil.

### CL-11 — majeure — sorties irremplaçables hors du dépôt jusqu'à l'assemblage (C)
- **Où** : brouillon 3 l. 47 et 151 ; `extraire_t05.py` l. 433-446.
- **Problème** : les sorties des sous-agents ne se reproduisent pas. Jusqu'à l'archive finale, elles ne vivent que dans le dossier de travail, dont l'emplacement n'est pas fixé.
  - Une perte (conteneur relancé, dossier temporaire) rend le run impossible à achever.
  - Elle oblige à tout refaire, soit un nouveau tirage des sorties, peut-être après avoir vu des avis de contre-vérification.
- **Correction** :
  - archiver et sceller les sorties de la tentative à chaque `valider` (`sorties-tentative-K.tar`), et les avis de la ronde à chaque `lire-contre-verification` ;
  - faire lire l'assemblage dans ces archives ;
  - fixer un emplacement de travail persistant hors du dépôt.

### CL-12 — mineure — ordre des étapes mal gardé (C)
- **Où** : `extraire_t05.py` l. 154-185, 172-182, 238 et 390-392.
- **Problèmes** :
  1. `preparer` (tentative 1) crée le manifeste avant de contrôler le dossier de travail et les textes. Un arrêt à ce stade « brûle » le run. Essai (`essai_preparer.py`) : manifeste créé, puis second essai refusé.
  2. La tentative 3 se prépare sans échec de contre-vérification (essai : acceptée avant tout échantillon). `echantillonner` ne refuse qu'une tentative 3 validée, pas une tentative 3 préparée.
  3. La tentative 3 et sa validation ne se font qu'une fois (R12). Si un avis refait plus tard révèle un échec, ce papier ne peut plus être repris.
  4. Le seuil de la l. 125 n'arrête qu'à l'assemblage, après d'éventuelles reprises inutiles.
- **Correction** :
  - faire tous les contrôles avant `creer_manifeste` ;
  - limiter la tentative 3 aux papiers en échec à leur premier avis lisible, et ne l'autoriser que lorsque tout l'échantillon a un avis lisible ;
  - contrôler le seuil dès la lecture de la ronde « echantillon » ;
  - écrire l'ordre des étapes dans le texte.

### CL-13 — mineure — validation ou lecture lancée trop tôt : irréversible (C)
- **Où** : `extraire_t05.py` l. 197-214 et 305-336 ; brouillon 3 l. 74.
- **Problème** :
  - Lancées avant la fin des sous-agents, ces étapes comptent les fichiers absents comme anomalies ou avis illisibles, sans réécriture possible (R12).
  - À la tentative 2, une panne d'infrastructure exclut le papier.
  - La dernière ligne rendue par chaque sous-agent n'est pas consignée.
- **Correction** :
  - écrire : « une étape de lecture ne se lance qu'après le retour de tous les sous-agents » ;
  - consigner la dernière ligne de chaque sous-agent, et la comparer au verdict du module : un « OK » du script face à une anomalie du module arrête. C'est un contrôle d'accord en production ;
  - une panne sans aucune sortie se relance dans la même tentative, consignée.

### CL-14 — mineure — plantages au lieu d'anomalies (C, D)
- **Où** : `extraction.py` l. 105-108, 121-122 et 362-368 ; `verifier-sortie-v1.py` l. 90-93 et 107-108.
- **Problème** :
  - Un identifiant non hachable (liste) lève `TypeError`, et un très grand entier (`10**400`) lève `OverflowError`, dans le module comme dans le script (`essai_unitaires.py`, `essai_bordure.py`). Dans `valider`, cela arrête toute la tentative au lieu de marquer un papier.
  - `listes_de_taches` traite en silence comme exclu un papier absent de `statuts`.
- **Correction** :
  - exiger un identifiant chaîne non vide ;
  - contrôler `reference_gpu_hours` sans risque de dépassement ;
  - exiger `set(statuts) == set(pilote) | set(reserve)`.

### CL-15 — mineure — script et module pas tout à fait équivalents ; tests d'accord faibles (D, E)
- **Où** : `verifier-sortie-v1.py` l. 115-119 ; `extraction.py` l. 171-173 ; tests l. 117-128 et 164-178.
- **Problème** :
  - Le script lit la copie, le module lit l'original. Après la coupe d'une bordure de tableau, les deux normalisations diffèrent. Essai (`essai_bordure.py`) : une citation à cheval sur la coupe donne « OK » au script et « citation introuvable » au module. C'est négligeable en pratique, mais pas nul.
  - Les tests comparent le nombre d'erreurs, pas leur nature.
  - Les guillemets, les tirets et les espaces insécables ne passent pas par le script dans les tests.
- **Correction** :
  - déclarer l'écart, ou le supprimer en ne coupant plus les bordures (voir CL-20) ;
  - faire émettre aux deux un code d'erreur stable et comparer les listes de codes ;
  - ajouter les cas de typographie, de bordure et de plantage.

### CL-16 — mineure — bilan incomplet par rapport au texte ; arrêts sans trace scellée (C, G)
- **Où** : brouillon 3 l. 102 et 127-129 ; `extraire_t05.py` l. 390-392 et 451-456 ; `extraction.py` l. 379-381.
- **Problème** :
  - Il manque au bilan : les désaccords de classification, les alertes lexicales sur tous les papiers, le nombre de tâches avec référence de coût (promis l. 102), la plausibilité du coût et le type de données.
  - Les arrêts « réserve épuisée » et « seuil dépassé » ne laissent aucun bilan scellé.
- **Correction** : calculer ces taux dans `assembler`, et écrire un bilan d'arrêt scellé avant de lever l'arrêt.

### CL-17 — mineure — contradictions et termes (G)
- L. 24 (« `costs` sert la cible de coût ») contre l. 95-102 (la référence est `compute.reference_gpu_hours`) : dire laquelle fait foi.
- L. 102, « Coût de référence nul » : écrire « absent (null) ». Zéro est une anomalie (l. 71 ; code l. 121).
- L. 20, « H.9 appliquée mot pour mot » : l'invite l'est, pas le procédé (contrôle et alertes, l. 61-63). Le dire.
- L. 66-71 : la liste des anomalies omet la description de moins de 10 caractères, l'identifiant absent ou en double, et la base du calcul.
- « Ancrés » désigne à la l. 83 la citation retrouvée, et à la l. 116 le jugement du contre-vérificateur : employer deux mots.

### CL-18 — mineure — écarts au brouillon 2 non listés (A)
- **Où** : brouillon 3 l. 7-14.
- **Non listés** :
  - citation introuvable devenue anomalie bloquante, puis cause d'exclusion (le brouillon 2 n'en disait pas la conséquence) ;
  - seuils de 200 et de 20 caractères ;
  - nouveaux motifs d'exclusion : classification jugée fausse deux fois, aucune direction féconde valable ;
  - échantillon tiré parmi les 96 papiers ;
  - « retenu » ajouté à la règle de remplacement, qui est une lecture de la l. 88 de la règle de sélection ; le dire comme tel.
- **Correction** : une ligne chacun dans la liste des écarts.

### CL-19 — mineure — chiffres de l'essai à blanc non rattachés (R6) (G)
- **Où** : brouillon 3 l. 59 et l. 15.
- **Problème** : « 230 parties, de 1 à 5 par papier » n'a ni chemin ni empreinte. L'essai à blanc lit mécaniquement les 96 textes avant le scellement, et il manque à la liste des lectures déclarées.
- **Correction** : sceller la sortie de l'essai (parties, lignes coupées, bordures coupées, longueurs maximales par papier), la citer, et l'ajouter à la l. 15.

### CL-20 — mineure — motifs de la copie de lecture en partie non vérifiés (E)
- **Où** : brouillon 3 l. 54-57.
- **Constat** : essai avec l'outil de lecture dont dispose ce sous-agent-ci, qui est l'outil de la session, sur des fichiers synthétiques.
  - Des lignes de 3 000 et de 30 000 caractères sont rendues entières.
  - Une partie de 49 113 caractères de formules denses (41 870 jetons) est coupée à 25 000 jetons, avec un avis explicite de pagination.
- **Problème** : « tronque les lignes très longues » n'est pas établi. La vraie limite se compte en jetons, et une partie de 50 000 caractères riche en formules ou en tableaux peut la dépasser.
- **Correction** : mesurer les jetons par partie à l'essai à blanc, ou ramener les parties vers 25 000 à 30 000 caractères. Garder ou retirer la coupe des lignes selon une mesure écrite ; la retirer supprimerait CL-15 et l'arrêt « sans espace ».

### CL-21 — mineure — cible de coût : périmètre incohérent (B, G)
- **Où** : `invite-cibles-v1.txt` l. 5 ; brouillon 3 l. 101-102 et 156.
- **Problème** :
  - La base « reported » vise le calcul total des expériences, la base « estimated » les « main experiments » : elles ne mesurent pas la même chose.
  - La l. 156 compare le coût d'une proposition à une référence qui couvre tout le papier.
  - Les références estimées ne sont vérifiées que sur 16 papiers, sans effet.
- **Correction** : même périmètre pour les deux bases (« the total compute of the paper's experiments »). Renvoyer au préenregistrement du pilote le mode de comparaison (somme de l'ensemble final, ou par proposition) et la stratification par base.

### CL-22 — mineure — directions stériles et contrôles se recouvrent (B)
- **Où** : `invite-cibles-v1.txt` l. 8 et 11.
- **Problème** : une ligne de base battue par le papier est à la fois un contrôle à inclure et une « approche clairement inférieure ». Une proposition qui l'inclut comme comparaison risque d'être appariée à une direction stérile.
- **Correction** : « an approach a plan might adopt as its main approach and that the paper shows to fail; not a baseline used only for comparison ». À défaut, le traiter dans la question d'appariement du pilote, et le déclarer ici.

### CL-23 — mineure — texte des papiers dans le dépôt (G)
- **Où** : brouillon 3 l. 165 ; règle de sélection l. 92 (« rien de leur texte n'entre dans le dépôt »).
- **Problème** : les citations sont mot pour mot par construction, et l'énoncé est une introduction retouchée. Les verser dans `diag/` et dans l'archive contredit la règle scellée.
- **Correction** : déclarer l'exception et sa raison (dépôt privé, extraits courts, nécessaires au contrôle), ou la soumettre à Lazar.

### CL-24 — mineure — consigne de l'extracteur (B)
- **Où** : `consigne-extracteur-v1.txt` l. 17-19.
- **Problème** : « until it reports no error » n'a pas d'issue écrite quand une erreur ne se corrige pas sans inventer. De plus, les retouches de l'énoncé à l'étape 5 se font en connaissant les cibles.
- **Correction** : ajouter « If an error cannot be fixed without inventing, leave it and reply with the last line printed. » et « When you edit research_questions, only remove or rephrase what breaks prompt H9's rules; never add content. »

### CL-25 — mineure — portée de la contre-vérification (F)
- **Où** : brouillon 3 l. 82, 106-108 et 125.
- **Problème** :
  - Les exclusions « theory_only » ne sont jamais vérifiées : ces papiers sont hors de l'échantillon par construction.
  - 80 papiers n'ont aucun contrôle sur le fond.
  - Intervalle exact à 95 % du taux de défaut : avec 4 échecs sur 16, de 7 % à 52 % ; avec 0 sur 16, de 0 % à 21 %.
- **Correction** :
  - faire contre-vérifier chaque exclusion « theory_only » (peu de papiers, aucun coût de carte) ;
  - inscrire au bilan le taux de l'échantillon et son intervalle, comme estimation du taux de défaut des tâches non vérifiées.

  Option, à proposer à Lazar car elle s'écarte de « sur échantillon » (P-006) : contre-vérifier les 96 papiers.

### CL-26 — suggestion — détecteur mécanique de fuite sur les 96 papiers (B)
- Lever une alerte (ou une anomalie) si l'énoncé normalisé contient au moins 8 mots consécutifs de la citation d'une direction féconde. Même calcul dans le script. Coût nul, et cela couvre les 80 papiers hors échantillon.

### CL-27 — suggestion — tolérances (D)
- Ajouter à la table typographique U+2010, U+2011, U+2012 et U+2212 (vers « - »), et retirer U+00AD : le message du script promet la tolérance des tirets.
- Accepter la clé `data\_type`, échappée comme dans H.10 l. 45, ou dire dans le message que la clé attendue est `data_type`. Essai : le message actuel est « data_type illisible : None ».

### CL-28 — suggestion — entropie connue avant le scellement (C)
- L'empreinte se calcule avant de sceller : l'auteur peut voir l'échantillon, et le choisir en retouchant le texte. C'est une pratique déjà admise pour la sélection : la déclarer. À défaut, dériver l'entropie de l'empreinte de la validation de la tentative 2.
- Préciser que la permutation se rejoue à version de numpy égale (version consignée au manifeste).

### CL-29 — suggestion — lancement et discipline de la session (B)
- Fixer aussi le champ de description de l'outil de sous-agents, avec un texte neutre.
- Écrire que la session ne lit pas le contenu des sorties avant le scellement du préenregistrement du pilote.
- Committer chaque résultat de `diag/` dès qu'il est écrit.

### CL-30 — suggestion — biais de la citation exacte (A, B)
- L'exigence favorise les cibles appuyées par une phrase de prose, au détriment de celles qui ne reposent que sur un tableau ou une formule. Rapporter au bilan la part des citations tirées d'une ligne de tableau.

## Annexe A — réponses courtes aux questions A à G

- **A. Fidélité** : P-006 (a) est appliquée : sous-agents neufs, échantillon contre-vérifié, sorties scellées. Les sept écarts déclarés sont réels et justifiés. Plusieurs effets ne sont pas déclarés (CL-18, CL-30). La définition des contrôles s'écarte des « contrôles nécessaires » de P-006 (CL-9).
- **B. Fuites et biais** : l'invite et la consigne ne poussent pas à inventer, grâce aux exceptions écrites, qu'il faut compléter (CL-24). L'isolement affirmé est faux (CL-6). Le schéma admet des ablations de la méthode cachée (CL-9), et stériles et contrôles se recouvrent (CL-22). Hors des 16 papiers, rien ne détecte une fuite (CL-25, CL-26). Entre sous-agents, aucun canal de contamination hors l'interdit de la consigne, qui n'est pas contraignant (CL-5).
- **C. Justesse mécanique** :
  - la machine d'états est juste sur tous les cas construits, sauf les avis multiples du rôle « echantillon » (CL-2) ;
  - remplacements et listes justes, dans l'ordre (CL-14 : complétude non contrôlée) ;
  - échantillon reproductible ;
  - seuil codé comme écrit, mais pas calibré (CL-10) ;
  - audit sans effet (CL-3) ;
  - rondes omises en silence (CL-4) ;
  - archive tardive (CL-11) ;
  - ordre des étapes et délais mal gardés (CL-12, CL-13).
- **D. Accord script et module** : décisions identiques à la lecture ligne à ligne, sauf copie contre original (CL-15) et plantages (CL-14). Les tests ne comparent que des nombres d'erreurs. 30 gardes sur 49 ne sont pas testées (CL-7).
- **E. Copie de lecture** : les deux gardes garantissent que la copie ne diffère que par des blancs, hors coupe des bordures, qui est admise. Une citation copiée de la copie se retrouve dans l'original à la normalisation près, sauf à cheval sur une bordure coupée : c'est démontré mais négligeable (CL-15). Les motifs de la copie ne se vérifient qu'en partie (CL-20).
- **F. Critères d'échec** : mécaniques et bien codés, mais le motif 2 est bruité et le seuil n'est pas calibré (CL-10). En sens inverse, accepter jusqu'à 4 échecs sur 16 laisse passer un taux de défaut jusqu'à 52 % (borne haute de l'intervalle) sur les 80 papiers non vérifiés (CL-25).
  - Reprises à la validation : peu nombreuses, puisque chaque sous-agent se contrôle.
  - Exclusions attendues : quelques papiers (« theory_only » de 2 à 6 % environ, plus une ou deux doubles chutes à la contre-vérification). Cela laisse de 22 à 28 tâches d'entraînement, proche du minimum de 20. C'est une estimation, non une mesure.
- **G. Autres** : contradictions et termes (CL-17), chiffre non scellé (CL-19), stockage (CL-23), provenance (CL-8).

## Annexe B — lectures, vérifications et essais

**Fichiers demandés**, avec les 16 premiers chiffres de leur empreinte :

| fichier | empreinte |
|---|---|
| brouillon 3 | `ba951ce9…` |
| brouillon 2 | `a434f433…` |
| P-006 (= compagnon) | `6fe36296…` |
| règle de sélection (= compagnon) | `8f43dcae…` |
| invite des cibles | `dd678a94…` |
| consigne de l'extracteur | `af450fb6…` |
| consigne du contre-vérificateur | `dc462938…` |
| `verifier-sortie-v1.py` | `4fc0a075…` |
| `verifier-avis-v1.py` | `fe13f39e…` |
| H9 (= compagnon et = procédure) | `15a3d48b…` |
| H10 (= compagnon et = procédure) | `9cced274…` |
| `extraction.py` | `fef50230…` |
| `extraire_t05.py` | `fecc2c18…` |
| `test_extraction.py` | `b12e5608…` |
| `test_extraire_t05.py` | `d381a252…` |
| `propositions.py` | `5d97b223…` |
| pilote, brouillon 1 | `b20b9139…` |

**Fichiers lus en plus**, cités par le code et nécessaires au jugement (déclarés) :
- `src/controle_ia/manifeste.py`, `src/controle_ia/scellement.py`, `src/controle_ia/gardes.py`, `src/controle_ia/environnements/invites.py`, `tests/conftest.py` ;
- l'empreinte seule de `diag/20261006-134235-t05-corpus/corpus.json` : `57f0aa47…`, égale à celle de la procédure ;
- le différentiel git de `extraction.py`, pour isoler le code neuf ;
- une recherche, dans `tests/`, des appels aux fonctions nouvelles (un seul fichier).

Ni `donnees/`, ni `registres/`.

**Contexte reçu** : le texte de `CLAUDE.md` du dépôt (CL-6).

**Essais**, hors du dépôt, sans écriture de cache dans le dépôt :
- les tests demandés : 60 réussis ;
- `essai_unitaires.py` : barres obliques inverses, identifiant non hachable, très grand entier, clé échappée, probabilités binomiales ;
- `essai_illisible_echantillon2.py` et `essai_illisible_contournement.py` (CL-2) ;
- `essai_rondes.py` (CL-4) ;
- `essai_preparer.py` (CL-12) ;
- `essai_bordure.py` (CL-14, CL-15) ;
- `traceur.py`, un greffon pytest qui relève les lignes exécutées (CL-7) ;
- l'outil de lecture sur `ligne_longue.md`, `ligne_30000.md` et `partie_dense.md` (CL-20).

Le dépôt a reçu d'autres modifications pendant la relecture (scripts du pilote, `juges.py`…). Elles sont hors du périmètre et ne viennent pas de moi. Les fichiers relus n'ont pas changé.
