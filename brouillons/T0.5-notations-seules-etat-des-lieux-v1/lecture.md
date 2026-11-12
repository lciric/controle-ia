# Les notations refaites et la lecture gelée

**En bref.** Oui. Des notations produites par un run séparé peuvent être lues par le code de lecture gelé **sans modifier aucun module de lecture**. Aucune voie n'est neutre pour autant. Chacune demande trois choses que le préenregistrement ne prévoit pas :
- un **nouveau run d'analyse** ;
- un **choix sur l'étiquetage** ;
- **poser les notations là où le code les cherche**, c'est-à-dire `diag/20261012-105125-t05-pilote-reel/`. Cela repose sur un comportement de `verifier_resultat` qui n'est écrit nulle part.

Le code ne change pas, mais la procédure de lecture s'écarte du texte scellé. À mon sens c'est un nœud : Lazar tranche avant que ce soit fait, et le choix s'écrit dans le préenregistrement du lanceur limité aux notations.

## 1. Ce que lit le code gelé, et où

- **État du gel.**
  - `git diff 2660b07 HEAD -- src/` est vide et l'arbre est propre au commit `7be281f`.
  - `MODULES_LECTURE` (`lire_pilote.py` l.82-85) contient aussi `lancer_pilote_a.py`, `juges.py`, `propositions.py`, `rubrique.py`, `manifeste.py`, `scellement.py` et `gardes.py`.
  - `exiger_modules_cites` (l.472-489) les compare au commit cité, modifications non commitées comprises.
  - Le préenregistrement (l.167) gèle ces modules « du scellement à la fin de la lecture, … même pour une autre tâche ». La lecture des juges n'est pas finie.
  - Conséquence : le lanceur limité doit être un **module neuf**. Il importe sans les toucher `demandes_de_notation` (`lancer_pilote_a.py` l.122-137) et `noter_ensembles` (`pilote_a.py` l.156-188, fichier hors de la liste mais faisant partie du code cité).
- **Un seul emplacement lu.** `charger_pilote` (l.177-213) prend un seul argument, `run_pilote`. Il lit `runs/<run_pilote>/manifeste.json`, puis chaque résultat **seulement** dans `diag/<run_pilote>/<nom>.json` (l.182-186).
- **Noms attendus.** Les fichiers s'appellent `notations-8B-decisives.json` et `notations-3B-decisives.json`. Les noms de juges viennent du manifeste du pilote (l.192, 198-201). Le code lit `resultat["notations"]`.
- **Format exigé par `notes_alignees`** (l.273-316), qui est exactement celui que produit `noter_ensembles` (`pilote_a.py` l.182-187). Une liste où chaque notation porte :
  - `cle` = `juge-<juge>/<tâche>/e<k>/passe-<p>`, pour e0 passe 0 (A), e0 passe 1 (B) et e1 passe 0 (C) ;
  - `ensemble_sha256`, l'empreinte de l'ensemble noté ;
  - `notes` (un dictionnaire, sommé l.264) ;
  - `score`, qui vaut `None` si et seulement si la réponse est incomplète ;
  - `reponse`, qui sert à comparer A et B (l.308-312) ;
  - `tronquee` (l.316).
- **Tout ou rien.** Les clés doivent correspondre exactement aux ensembles décisifs non vides : une notation manquante, en trop (l.284-290) ou en double (l.281) arrête la lecture. Le lanceur n'écrit donc le fichier d'un juge qu'à la fin de son étape, comme `lancer_pilote_a.py` l.428.
- **Contrôle de l'empreinte des ensembles notés.** Chaque `ensemble_sha256` est comparé au hachage SHA-256 du texte `bilan.ensemble` de l'épisode, tiré du `episodes.json` scellé du pilote (l.267-270 et 293-296). Ce contrôle vaut quelle que soit l'origine des notations : c'est le vrai garde-fou de l'alignement.
- **Empreinte des tâches.** Elle est lue dans `arret.json`, champ `partiel.taches_sha256` (l.203-208). Ce champ existe.
- **Rattachement des résultats.** `verifier_resultat` (`manifeste.py` l.142-150) fait deux choses : il vérifie le sceau posé à côté du fichier, puis il suit `corps["run_id"]` jusqu'au manifeste de ce run et compare `manifeste_sha256`. **Il ne vérifie pas que le fichier se trouve dans le dossier de son run.**
  - Je l'ai éprouvé dans le dossier de travail : la copie octet pour octet d'un résultat d'un run B, avec son sceau, placée dans `diag/<run A>/`, est acceptée, et le `run_id` lu est B.
  - Script : `/tmp/claude-0/-home-user-controle-ia/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/notations-seules/lecteur-lecture-gelee/essai_rattachement.py`.

## 2. Un nouveau run d'analyse est inévitable

- **Pourquoi.** `diag/20261012-150724-t05-pilote-analyse/lecture.json` existe déjà. `analyser` écrit par `ecrire_resultat` (l.1029), qui refuse d'écraser un fichier (`manifeste.py` l.134-135, conformément à R12).
- **Comment il se crée.** Seul `preparer_etiquetage` (l.591-624) crée un run d'analyse. Il exige :
  - un arbre propre (`manifeste.py` l.81-83) ;
  - un préenregistrement d'analyse identique à celui que cite le manifeste du pilote (l.603).
  
  Le nouveau run d'analyse se fait donc **sous `prereg/T0.5-pilote-8B-v1.md`** (empreinte `9ce91ba1…`), et non sous le préenregistrement du lanceur limité.
- **Graines.** Elles ne dépendent que de l'entropie citée et du nom des clés (`manifeste.py` l.37-48). Un nouveau run d'analyse a donc les mêmes graines, donc le même sous-échantillon et les mêmes lots, à condition d'utiliser numpy 2.4.6 (l.523-526). On peut le vérifier : `engagement_sha256` et `empreintes_lots` doivent être égaux à ceux de `diag/20261012-150724-t05-pilote-analyse/echantillon-etiquetage.json`.
- **Étiquetage.** `analyser` exige `diag/<run_analyse>/etiquettes.json` (l.991-994). Trois façons de le fournir :
  - (a) **réétiqueter par des sous-agents neufs**, selon la procédure gelée (préenregistrement l.161-163). Les kappas sont alors recalculés et peuvent s'écarter de ceux du verdict (0,17 pour les contrôles, 0,04 pour les directions fécondes, 0,07 pour les stériles) : on aurait deux lectures des familles ;
  - (b) **recopier les étiquettes de la première analyse** dans les lots du dossier de travail. `lire_lot` (l.640-667) ne contrôle que les paires, la consigne, le script de contrôle et la forme ;
  - (c) **copier `etiquettes.json` scellé**, avec son sceau, dans `diag/<nouvelle analyse>/`. `analyser` l'accepte, grâce au même trou dans le rattachement.
  
  Les voies (b) et (c) redonnent les familles à l'identique, ce qui se vérifie contre la première `lecture.json`. Mais elles sortent de la lecture en trois étapes : c'est un écart.
- **Effets mécaniques à régler d'avance.**
  - `lecture_suspendue` redeviendra vraie, car la couverture des directions fécondes vaut 0,930, au-dessus de 0,9 (l.1014, 1021, 1028). Or Lazar n'a levé la suspension que pour la première lecture (R-155, point 2).
  - `tirer_relectures` (l.891-897) tirera d'abord 10 réponses de juge, puis 10 actions avec le même générateur. Ce ne seront donc pas les 10 actions de l'audit de symétrie (R4) déjà scellé.
  - `run_partiel` restera vrai, puisque `arret.json` est présent (l.1028).

## 3. Les voies pour poser les notations

| voie | code gelé | sceaux, R12, « seulement des ajouts » | ascendance | avis |
|---|---|---|---|---|
| **B1** : `ecrire_resultat` appelé avec le manifeste du pilote, ce qui écrit `diag/<pilote>/notations-*-decisives.json` rattaché à ce manifeste (empreinte `8c3d7985…`) | lu | tout passe : noms neufs, sceaux neufs, seulement des ajouts | **faussée**. Le manifeste du pilote (commit `1c6c900`, commande `lancer_pilote_a`, versions, date) se porterait garant d'un autre code, d'une autre machine et d'une autre date. C'est contraire à R9 (un manifeste par run) et à `arret.json` (arrêt pendant les notations du 8B). La ligne « run partiel » (préenregistrement l.190) lirait le fichier comme écrit par le pilote, et le contrôle « un seul run » de `recuperation_pilote_v1.sh` (l.57-60) ne verrait rien. | **à écarter** |
| **B2** : nouveau run R′ avec son propre manifeste ; notations écrites et scellées dans `diag/R′/` par `ecrire_resultat` ; puis copie octet pour octet du fichier **et de son sceau** dans `diag/<pilote>/` | lu sans modification (essai ci-dessus) | passe : rien n'est écrasé, seulement des ajouts ; `verifier-arbre` passe, car le sceau porte le nom de base (`scellement.py` l.91-112) | honnête dans le fichier (`run_id` et empreinte de R′). Mais `diag/<pilote>/` mélange deux runs, et la voie repose sur un comportement non écrit de `verifier_resultat`. Le script de récupération de R′ doit admettre deux dossiers. | **voie la moins intrusive**, à déclarer |
| **C** : R′ héberge dans `diag/R′/` des copies octet pour octet de `episodes.json` et `appariements.json` (toujours rattachées au pilote), plus ses notations et son résumé ; analyse avec `run_pilote` = R′ | lu, à trois conditions : la configuration de R′ porte `CONFIG_ATTENDUE`, les deux juges (l.188-194) et `max_nouveaux` (l.947) ; R′ est lancé sous le préenregistrement passé à l'analyse (l.603) ; ce texte cite le commit `2660b07` et l'entropie (l.86 et 599) | passe ; le dossier du pilote reste intact | honnête, mais l'analyse ne se rattache plus au manifeste du pilote : le « pilote » lu devient R′, sous un autre préenregistrement que celui qui gèle les critères | plus lourd, déconseillé |

Il existe une variante de B2 : écrire directement dans `diag/<pilote>/` un fichier rattaché à R′. `ecrire_resultat` ne le permet pas, puisqu'il écrit dans `diag/<run du manifeste>/` (l.131). Il faudrait du code d'écriture neuf. La copie est préférable.

## 4. Recommandation

- **Voie.** Je recommande B2, avec un nouveau run d'analyse sous `T0.5-pilote-8B-v1.md`, et l'étiquetage repris par (b) ou (c). La reprise est contrôlée par l'égalité de l'engagement et des empreintes des lots avec la première analyse, puis par l'égalité des familles et des kappas avec la première `lecture.json` ; tout écart arrête.
- **Ce que le préenregistrement du lanceur limité doit écrire** :
  - des graines de R′ égales à celles du pilote : même entropie et mêmes clés `juge-<juge>/<épisode>/passe-<p>`, avec `etat_controle` comparé ;
  - qui fait la copie dans `diag/<pilote>/` : la session, dans un commit à part, jamais la machine de calcul ;
  - le traitement de `lecture_suspendue` et des relectures tirées de nouveau ;
  - la règle selon laquelle seuls les juges, P2 et P3 sont pris de la nouvelle `lecture.json`.
- **Nature de l'écart.** Aucun module de lecture n'est à modifier. Mais trois choses sortent du texte scellé, qui prévoit un seul run d'analyse et trois étapes (préenregistrement l.160-166) :
  - lire des notations refaites par un second run d'analyse ;
  - copier des fichiers dans le dossier du pilote ;
  - reprendre l'étiquetage.
  
  C'est un écart de procédure, donc un nœud : Lazar décide avant.
- **Si Lazar refuse B2 et C**, la seule voie restante est de modifier `charger_pilote`, par exemple pour lui donner un second dossier de notations. Ce serait **une modification d'un module de lecture, donc un écart au préenregistrement scellé**, un nœud à faire décider avant de l'écrire.