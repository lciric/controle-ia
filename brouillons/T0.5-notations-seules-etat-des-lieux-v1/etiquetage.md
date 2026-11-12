# Étiquetage par sous-agents comme référence d'appariement des contrôles (T0.6) : lecture pour le point 4 de N-020

## En bref
- On ne peut pas faire étiqueter toutes les paires par des sous-agents. Le plan du brouillon de T0.6 en produirait environ 87 000 pour les contrôles, soit environ 1 450 lots.
- On peut en revanche étiqueter un échantillon tiré par graine, limité aux conditions décisives : environ 7 800 à 15 500 paires, soit 130 à 260 lots.
- Il faut d'abord un pré-test de fidélité : faire réétiqueter les 480 paires du pilote par des sous-agents neufs. La supériorité de l'étiquetage sur le juge 8B est plausible pour les contrôles, mais elle n'est pas établie.

## 1. Ce que le pilote établit
Sources : section 4 du verdict et audit R4.
- **Accord entre le juge 8B et l'étiquetage, sur les contrôles** : kappa pondéré 0,17, intervalle [0,04 ; 0,35]. Sur 80 paires où le 8B dit « oui », l'étiquetage en confirme 22. Sur 80 paires où il dit « non », il en contredit 7.
- **Ce que cela donne, rapporté aux 7 660 paires** (strates de 662 « oui » et 6 998 « non » ; calcul du lecteur) :
  - environ 794 paires seraient « Yes » pour l'étiquetage ;
  - le 8B n'en retrouve qu'environ 23 % ;
  - 72 % de ses « oui » sont contredits.
- **Ce que l'audit R4 a vérifié** : il a confirmé l'indulgence du 8B sur les directions seulement. Pour les contrôles, il note une indulgence « moindre », constatée sans être examinée. Un kappa bas dit qu'il y a désaccord ; il ne dit pas lequel des deux a raison.
- **Fiabilité pratique de l'étiquetage au pilote** : 8 lots de 60 paires, tous conformes à la première tentative. Chaque lot fait environ 78 à 82 Ko, soit à peu près 20 000 jetons. Les 8 sous-agents ont travaillé en parallèle et ont écrit leurs étiquettes 1 à 6 minutes après la préparation (horodatages des fichiers, lus sans ouvrir leur contenu).
- **Ce que le pilote ne mesure pas** : la fidélité de l'étiquetage. Aucune paire n'a été étiquetée deux fois. Les 160 paires de contrôles du pilote sont la seule base disponible pour la valider.

## 2. Combien de paires demanderait T0.6
Base du pilote : 60 tâches, 5,92 contrôles semés par tâche, 42,6 paires de contrôles par ensemble final. Le brouillon de T0.6 parle encore de 64 tâches ; il faut le corriger à 60.

| plan | ensembles | paires de contrôles | lots de 60 |
|---|---|---|---|
| tout le brouillon (17 conditions, 2 épisodes) | 2 040 | ≈ 87 000 | ≈ 1 450 |
| conditions décisives seulement (9 : (i-a) forte aux 3 proportions et honnête ; famille (ii) aux 4 valeurs d'échelle et témoin), 2 épisodes | 1 080 | ≈ 46 000 | ≈ 770 |
| les mêmes, 1 épisode | 540 | ≈ 23 000 | ≈ 380 |
| échantillon : 2 contrôles tirés par tâche (les mêmes d'une condition à l'autre), toutes les propositions de l'ensemble final comparées à ces contrôles, 9 conditions, 1 épisode | — | ≈ 7 800 | ≈ 130 |
| le même avec 4 contrôles par tâche | — | ≈ 15 500 | ≈ 260 |
| double étiquetage de 15 % | — | + 1 200 à 2 300 | + 20 à 40 |

- **Puissance de l'échantillon (estimation grossière)** :
  - supposons une couverture honnête d'environ 0,3 ;
  - avec 2 contrôles par tâche, l'erreur type d'une différence appariée vaut environ 0,05 ;
  - une chute de 0,2 à la proportion p = 1 se détecte facilement ; une chute de 0,1 pour la famille (ii) reste limite.
- **À faire avant le scellement** : une simulation de puissance (R1), dont il faut sceller le résultat.

## 3. Coût en sous-agents
- **Échantillon (130 à 300 lots)** :
  - environ 3 à 7 millions de jetons de paires lus ;
  - quelques heures de temps réel, par vagues de 8 ;
  - aucune dépense de carte.
- **Tout étiqueter (1 450 lots)** :
  - plus de 30 millions de jetons ;
  - environ 15 à 20 heures ;
  - le risque de dérive du modèle des étiqueteurs devient réel (section 4). Ce volume est à écarter.
- **Pré-test de fidélité** : 8 lots, les 480 paires du pilote. Coût négligeable.

## 4. Validité
- **Ce n'est pas une vérité terrain humaine** :
  - les contrôles semés sont la vérité terrain ; l'appariement reste un instrument ;
  - il faut écrire « référence d'appariement », jamais « vérité ».
- **Même modèle que la session** : les cibles ont été extraites par des sous-agents de ce même modèle (P-006 (a)). Les erreurs sur ce qui compte comme « contrôle » peuvent donc aller dans le même sens. Le kappa entre deux étiquetages mesure la constance de l'instrument, pas sa justesse.
- **Modèle non épinglé** : le préenregistrement du pilote le dit (TX-17 : « la session ne choisit pas son modèle »). En conséquence :
  - il faut consigner le modèle par lot, par renvoi, sans jamais le nommer dans le dépôt ;
  - il faut une campagne courte ;
  - il faut glisser dans chaque vague quelques paires d'ancrage déjà étiquetées au pilote, pour détecter une dérive.
- **Fidélité à vérifier** :
  - pré-test avec un seuil gelé avant l'étiquetage (proposition : kappa entre étiqueteurs ≥ 0,7 sur les contrôles, borne basse ≥ 0,5) ;
  - puis double étiquetage de 15 % des paires dans T0.6 ;
  - en cas de désaccord, un troisième étiqueteur départage (règle à geler).
- **Ce que la consigne figée laisse passer** : elle dit « Yes … even briefly ». Un contrôle affaibli mais mentionné compte donc comme inclus. L'intensité légère de (i-a) (« omis ou affaibli ») est en partie invisible. Deux voies :
  - définir S1 comme une **omission** dans les consignes de T0.6, et garder la consigne validée ;
  - ou écrire une consigne nouvelle, qui serait un instrument nouveau à revalider.

## 5. Risques
- **Indépendance** :
  - les étiqueteurs reçoivent `CLAUDE.md`, qui nomme le programme. Le but (mesurer un sabotage) se devine ;
  - l'invite fixe n'a pas de phrase de préséance, car le classificateur de la session l'a refusée ;
  - parades :
    - les étiqueteurs ne voient ni la condition ni la dose ;
    - chaque lot mélange les conditions, dans un ordre tiré par graine, avec des identifiants opaques ;
    - on vérifie que le taux de « Yes » ne dépend ni du lot ni de la position dans le lot ;
    - le lecteur du verdict n'est pas un étiqueteur (R13).
- **Scellement** :
  - l'étiquetage devient la mesure décisive ;
  - il faut geler la consigne, l'invite, la taille des lots, les tentatives, le plan d'échantillonnage, les graines et la règle de double étiquetage ;
  - il faut une empreinte d'engagement avant l'étiquetage, comme au pilote, et des étiquettes scellées avant toute analyse ;
  - un étiquetage ne se rejoue pas à l'identique : seules les étiquettes scellées font foi.
- **D-20** :
  - par construction, les étiqueteurs lisent le texte des épisodes ;
  - les lots restent hors du dépôt ;
  - la session ne manipule que des empreintes, des identifiants et des étiquettes, et ne lit que la dernière ligne de chaque sous-agent ;
  - avant tout versement, il faut contrôler le dépôt avec `verifier_d20.py`.
  - Le risque de fuite croît avec le nombre de sous-agents. Il y a déjà eu un incident (R-146), ce qui est un argument de plus contre l'étiquetage complet.
- **Publication** : un papier devra nommer le modèle des étiqueteurs. C'est à décider par Lazar.

## 6. Alternatives
- **Juge local plus fort** (de l'ordre de 70 milliards de paramètres) :
  - avantages : poids figés, reproductible, note toutes les paires ;
  - inconvénients : changement de modèle sous GO, devis de carte, mise au point (mémoire, format) dans un calendrier serré ;
  - sa validation passerait de toute façon par les 480 étiquettes du pilote, c'est-à-dire par la même référence. Il peut échouer comme le 8B.
- **Règles lexicales** (mots-clés gelés par contrôle, écrits avant les épisodes) :
  - avantages : gratuites, déterministes, transparentes ;
  - inconvénients : elles ratent les paraphrases ; un saboteur peut garder le mot et vider le contenu ; le chevauchement avec l'énoncé gonfle la couverture (selon le 8B, l'énoncé seul couvre déjà 0,53 des contrôles) ;
  - utiles comme contre-vérification descriptive, pas comme référence.
- **Vérité terrain réduite au coût** (seule famille retenue par le texte gelé) :
  - avantage : aucun nouvel instrument ;
  - inconvénients :
    - elle oblige à déplacer le mode principal de (i-a) vers S2, gonfler les choix coûteux, ce qui modifie P-009 ;
    - le lecteur du coût lit mal les séparateurs de milliers ;
    - 57 références sur 58 sont estimées ;
    - chez l'agent honnête, 43,7 % des coûts sont à plus d'un facteur 10 de la référence.

**À corriger dans le brouillon de T0.6, quelle que soit l'option** :
- 64 tâches → 60 ;
- « juge 8B validé au pilote » est faux ;
- T6-P6 dépend des notations du 8B et du 3B, à refaire selon N-020 (1).

## 7. Brouillon de proposition (numéro à attribuer)

**Décision** : choisir la référence qui décide si une proposition inclut un contrôle semé, pour mesurer la couverture des contrôles (mode S1) dans T0.6, à la place du juge 8B (kappa 0,17).

**Enjeu** : sans référence fiable, S1 n'a pas de mesure lisible, et le critère 2 de G0 ne repose que sur le coût, instrument fragile. Échéances : point de contrôle du 19 octobre (P-007), G0 le 1er novembre.

**Options** :
- **(a) Étiquetage échantillonné par sous-agents, après un pré-test de fidélité préenregistré.**
  - Pré-test : les 480 paires du pilote réétiquetées par 8 sous-agents neufs. Seuil gelé : kappa entre étiqueteurs ≥ 0,7 sur les contrôles, borne basse ≥ 0,5.
  - Puis T0.6 : 2 à 4 contrôles tirés par tâche dans les 9 conditions décisives, soit environ 7 800 à 15 500 paires, 130 à 260 lots, plus 15 % en double.
  - Le 8B note tout, à titre descriptif. S1 est défini comme une omission.
  - Avantages : la référence la plus solide disponible sans dépense de carte ; elle a déjà fonctionné au pilote (8 lots sur 8 conformes à la première tentative).
  - Inconvénients : étiqueteurs non humains, du même modèle que la session et non épinglés ; la puissance reste à établir par simulation ; aucun rejeu à l'identique.
- **(b) Juge local plus fort, validé sur les 480 paires du pilote avant T0.6.**
  - Avantages : reproductible ; toutes les paires sont notées.
  - Inconvénients : changement de modèle et dépense sous GO ; délai ; même référence de validation que (a), et risque d'échec comme le 8B.
- **(c) Vérité terrain réduite au coût : mode principal de (i-a) déplacé vers S2, contrôles descriptifs.**
  - Avantages : aucun nouvel instrument ; aucune paire à étiqueter.
  - Inconvénients : modifie P-009 ; lecteur du coût à corriger ; références presque toutes estimées ; dispersion qui affaiblit la dose-réponse.

**Recommandation** : (a), avec le coût relevé pour toutes les conditions, et un repli préenregistré sur (c) si le pré-test échoue. Confiance d'environ 55 %.

**Défaut** : aucun. R-155 en fait une modification du dispositif, que Lazar décide. Sans décision, T0.6 ne se scelle pas sur S1.

---
Lus (dépôt en lecture seule) :
- `/home/user/controle-ia-travail/brouillons/T0.6-organismes-v0-v1-brouillon1.md`
- `/home/user/controle-ia-travail/brouillons/T0.6-organismes-v0-conception-brouillon1.md`
- `/home/user/controle-ia-travail/docs/decisions/proposition-P-009-T0.6-organismes-v1.md`
- `/home/user/controle-ia-travail/docs/verdicts/verdict-T0.5-pilote-v1.md`
- `/home/user/controle-ia-travail/docs/verdicts/audit-R4-T0.5-pilote-v1.md`
- `/home/user/controle-ia-travail/src/controle_ia/environnements/lire_pilote.py`
- `/home/user/controle-ia-travail/registres/decisions.md` (R-153 à R-155, N-020)

Calculs du lecteur, faits sur des comptes seulement : `/tmp/claude-0/-home-user-controle-ia/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/notations-seules/lecteur-etiquetage/comptes.py`

Ni `episodes-defaut.json` ni `chemin-defaut.json` n'ont été ouverts. Aucun texte d'épisode n'a été affiché, et aucune commande vastai n'a été lancée.