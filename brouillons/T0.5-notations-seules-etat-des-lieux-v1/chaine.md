# Chaîne d'instance : comment les notations sont produites aujourd'hui, et ce qu'il faut pour un mode « notations seules »

Les notations décisives ne s'écrivent qu'une fois **tous** les lots d'un juge terminés. Quand l'échéance tombe en cours de route, tout ce qui a été calculé pour ce juge est perdu. C'est ce qui est arrivé au pilote. Le mode « notations seules » demande un nouveau module Python, une troisième valeur d'ETUDE dans les deux scripts d'instance, et une déclinaison des procédures : contrôles avant dépense, lanceur, récupération, scellement, répétition jouet et bancs. Compter environ 2 à 3 jours de travail de session, et environ 3,5 à 4,5 heures de carte, chiffre non mesuré.

## 1. Comment les notations sont produites et écrites aujourd'hui

**Chaîne d'appel**
- Le lanceur de l'instance passe `ETUDE` au script de l'instance (`scripts/amorce_instance_t05.sh:37-40`). Seules les valeurs `pilote` et `revalidation` sont acceptées (l. 38). Le plafond est de 300 minutes (l. 39).
- Le script de l'instance fait, dans l'ordre (`scripts/pilote_t05_instance.sh`) :
  - lecture précoce du préenregistrement et des sceaux, avant toute installation (l. 98-139) ;
  - poussée initiale de la branche (l. 147-158) ;
  - installation, puis tests, avec « N passed » exigé (l. 292-305) ;
  - lancement du module `lancer_pilote_a`, sous un délai externe de 270 minutes (l. 314-333) ;
  - commit, poussée, puis vecteurs (l. 345-362).
- Tout arrêt passe par `consigner_arret` (l. 225-236), qui pousse aussi les vecteurs si `donnees/$RUN` existe. Le signal TERM est relayé au run par son identifiant de processus (l. 240-252).

**Ordre des étapes dans `src/controle_ia/environnements/lancer_pilote_a.py`**
1. Gardes d'avant le manifeste (l. 269-299).
2. Graines : une clé `juge-<nom>/<épisode>/passe-<p>` par notation (l. 101-108). La dérivation se fait par le nom de la clé, pas par sa position (`manifeste.py:37-48`).
3. Chargement de l'agent, qui sert aussi de juge 8B (l. 321).
4. Contrôle du format (l. 324-329), puis préchargement du 3B seul (l. 233-248 et 331-332).
5. Épisodes, puis `episodes.json` (l. 333-358).
6. Appariement par le 8B (l. 395-411).
7. `noter("decisives")` puis `noter("descriptives")` (l. 415-436). À l'intérieur de chaque appel, le 8B passe avant le 3B. Chaque juge est chargé à sa première notation, le 3B hors ligne, avec le format recontrôlé (l. 381-393).

**Où est le défaut**
- `noter_ensembles` (`pilote_a.py:156-187`) ne vérifie l'échéance qu'**au début de chaque lot** (l. 165, puis l. 150-153).
- Le fichier `notations-<juge>-<étape>.json` n'est écrit qu'après le dernier lot (`lancer_pilote_a.py:425-433`).
- Rien n'est journalisé entre deux lots.

**Ce qui s'est passé au pilote** (`diag/20261012-105125-t05-pilote-reel/arret.json`)
- Arrêt à l'étape « notations decisives par 8B », à 15 063,6 s.
- Épisodes : 7 037,2 s. Appariement : 461,0 s.
- Le 8B a donc noté pendant **au moins 7 565 s** sans finir ses 180 notations (23 lots). On ne sait pas combien de lots étaient faits. Le test `test_lanceur_appariement_avant_les_notations_arret_pendant_les_decisives` (`tests/test_pilote_a.py:419-442`) fige justement ce comportement : aucun fichier de notation écrit.

## 2. Ce qu'il faut pour un mode « notations seules »

Je propose un nouveau module, `src/controle_ia/environnements/noter_pilote_a.py`. Il importe les fonctions de `lancer_pilote_a` et de `pilote_a` sans les modifier : ce code reste celui que cite le pilote (`2660b07`).

**Gardes d'avant le manifeste**
- Épisodes :
  - `verifier_resultat` sur `diag/<pilote>/episodes.json` : sceau, manifeste du pilote et rattachement ;
  - empreinte égale à celle que cite le nouveau préenregistrement ;
  - 180 fiches ;
  - tâches égales à celles de `arret.json` du pilote (`partiel.taches_sha256`).
- Paramètres des juges égaux à ceux du manifeste du pilote : `agent`, `juges`, `lot_juge`, `max_nouveaux_juge`, `temperature_juge`, `variante_juge`, `episodes_decisifs`, `episodes_notes_deux_fois`, `fils`.
- Refus si `diag/<pilote>/notations-*-decisives.json` existe déjà, pour ne jamais retirer au sort une notation existante (R3).
- Demandes produites par `demandes_de_notation`, filtrées sur les épisodes e0 et e1 : 180 par juge (60 A, 60 B, 60 C) ; nombre exact exigé.
- Citations du préenregistrement : commit du code (`exiger_code_cite`), configuration, tâches, épisodes, entropie.
- Si l'entropie du pilote est reprise : chaque graine `juge-<j>/<ép>/passe-<p>` du nouveau manifeste doit être égale à celle du manifeste du pilote. C'est possible parce que la dérivation se fait par le nom de la clé. **Reprendre ou non cette entropie est une décision à prendre dans le préenregistrement.**

**Après le manifeste, dans cet ordre**
1. Réglage du déterminisme.
2. Téléchargement des **deux** modèles. Le 8B n'a pas de champ `modele` dans sa fiche de juge : il faut prendre `config["agent"]`.
3. Contrôle du format des deux juges.
4. 8B : notations lot par lot, puis écriture de `notations-8B-decisives.json`.
5. Libération du 8B.
6. 3B chargé hors ligne, format recontrôlé, notations, écriture de `notations-3B-decisives.json`.
7. Résumé, précédé de `exiger_sans_signal`.

Garder le même nom de fichier et la même forme d'enregistrement (`cle`, `ensemble_sha256`, `score`…) : le contrôle d'alignement de la lecture (`lire_pilote.py:280-296`) s'appliquera alors tel quel. Mais la lecture devra lire **deux** runs : les épisodes dans le pilote, les notations dans le nouveau run. Aujourd'hui elle lit un seul dossier (l. 180-201).

**Deux ajouts recommandés, à trancher dans le préenregistrement**
- **Écriture lot par lot.** Le module appelle `noter_ensembles` sur des tranches de `lot_juge` demandes, alignées sur le découpage d'origine : les lots et leurs graines restent identiques. À l'arrêt, un fichier scellé `notations-<j>-decisives-partielles.json` est écrit avant `arret.json`. Le statut de lecture de ce fichier reste à fixer.
- **Une ligne de progression par lot** dans `run.err` : rang du lot, durée, nombre de passes, lignes terminées, aucun texte de réponse. On aurait enfin une mesure du débit.

Éventuellement : **une échéance par juge**, pour qu'un dépassement du 8B ne mange pas le temps du 3B.

## 3. Fichiers à créer ou à modifier, et tests

**Code**
- `scripts/amorce_instance_t05.sh` : `ETUDE=notations` (l. 38), plafond adapté au nouveau devis (l. 39).
- `scripts/pilote_t05_instance.sh` :
  - `notations` ajouté au `case` de l. 40-45 (branche `calcul/t05-notations-<MODE>-v1`, nouveau préenregistrement) ;
  - lecture précoce de « Chemin des épisodes : `…` » et de son sceau, avant l'installation (l. 112-138) ;
  - nouveau lanceur avec `--episodes` (l. 314-320) ;
  - délai de la l. 325 adapté ;
  - aucun vecteur à pousser : la l. 350 se limite déjà à `pilote`, et la l. 235 ne joue que si `donnees/$RUN` existe.
- Ces deux scripts font partie de l'arbre gelé : leurs empreintes doivent être citées par le nouveau préenregistrement.

**Tests**
- Nouveau `tests/test_noter_pilote_a.py`, en mode jouet sur un dépôt jetable. Le cas de départ est fabriqué comme le vrai : un pilote jouet arrêté pendant les notations décisives, sur le modèle des tests de `test_pilote_a.py:241-442`. Un cas sain et un artefact pour chaque garde (R5) :
  - bout en bout : deux fichiers de notations, comptes, clés, alignement `ensemble_sha256`, aucune notation descriptive ;
  - épisodes altérés ou rattachés à un autre manifeste ;
  - paramètres des juges différents de ceux du pilote ;
  - notations déjà présentes dans le pilote ;
  - citations du préenregistrement ;
  - graines égales à celles du pilote, artefact avec une autre entropie ;
  - lots identiques au découpage d'origine ;
  - échéance pendant le 8B (fichier partiel, rien pour le 3B), puis pendant le 3B (fichier du 8B présent) ;
  - échec du chargement du 3B ;
  - format hors ligne différent ;
  - signal TERM converti, ou avalé (sur le modèle de l. 815-858) ;
  - bornes de `duree_max_s` ;
  - mode réel sans préenregistrement.
- `tests/test_script_instance_t05.py` : cas `ETUDE=notations`, sur le modèle de l. 162 et 286 (lecture précoce des épisodes, absents ou au sceau faux, branche par défaut, aucun vecteur poussé). L'amorce doit aussi refuser une valeur d'ETUDE inconnue.
- Le nombre de tests attendus change : 689 au commit cité du pilote, une nouvelle valeur à citer.

## 4. Gardes de la chaîne existante à décliner

**Contrôles avant dépense** (`controles_avant_depense_pilote_v1.sh`), à décliner en `controles_avant_depense_notations_v1.sh`.

On garde :
- contenu de S (l. 54-56) ;
- commit du code et arbre gelé égal au code relu épinglé (l. 57-74) ;
- empreintes de l'amorce et du script de l'instance (l. 60-63) ;
- sceaux et citations (l. 75-85) ;
- `problemes()`, `verifier-arbre` (l. 231-238) ;
- format des vrais tokeniseurs (l. 300-312) ;
- suite complète au commit S (l. 314-318) ;
- garde de calcul (l. 319) ;
- branche absente (l. 217-229).

On remplace :
- les contrôles sur N-019 (l. 86-112) par le GO de dépense et la colonne d'état de N-020 ;
- les valeurs du verdict de la revalidation (l. 240-298) par :
  - toutes les gardes de la section 2 rejouées ;
  - le calcul de `duree_max_s` recalculé ;
  - l'état du pilote constaté : `arret.json` à l'étape attendue, aucun fichier de notation.

Ces contrôles n'ont pas à ouvrir les fichiers de la revalidation (D-20 respectée).

**Lanceur v2** (`lancer_pilote_v2.sh`), à décliner en `lancer_notations_v1.sh`.

On garde :
- fenêtre horaire et place disque (l. 48-50) ;
- S présent sur le dépôt distant (l. 55-58) ;
- scripts égaux à leurs copies versées (l. 82-94) ;
- contrôles rejoués, bornés à une heure (l. 98-101) ;
- empreinte de l'amorce et ligne « Lancement » (l. 103-109) ;
- filtre de l'offre, prix (l. 146-169) ;
- instances tolérées (l. 173-211) : l'instance du pilote, **55538944**, arrêtée, doit être ajoutée aux instances tolérées si elle existe encore ;
- crédit (l. 212-214), avec le nouveau devis ;
- garde de calcul (l. 216) ;
- création avec `ETUDE=notations` et une nouvelle étiquette (l. 226-246).

On remplace le bloc GO19 (l. 113-139) par le GO de dépense de N-020. Relancer l'instance 55538944 est inutile : son amorce refuse de repartir (R12, `amorce_instance_t05.sh:26-28`).

**Récupération** (`recuperation_pilote_v1.sh`), à décliner en `recuperation_notations_v1.sh`.
- On garde : ascendance, ajouts seulement, un seul run, auteurs (l. 52-63) ; sceaux (l. 65-73) ; manifeste et citations (l. 92-103) ; issue (l. 104-113) ; journal, carte et liste des paquets installés (l. 167-188) ; absence de jetons (l. 189-206).
- On remplace :
  - le motif du nom de run de la l. 61 (`t05-notations-reel`) ;
  - les contrôles 4c à 4f : deux fichiers décisifs, 180 notations chacun, recalculés depuis `episodes.json` du pilote, clés et `ensemble_sha256` alignés ;
  - la partie vecteurs (l. 150-166), qui disparaît.

**Autres déclinaisons**
- Relancement : interdit dès qu'un fichier de notations est écrit sur la branche `-v1` (même logique de préséance que pour les épisodes, `controles…:224-226`).
- Scellement : sur le modèle de `sceller_pilote_v1.sh`, sans tirer d'entropie si celle du pilote est reprise.
- Répétition jouet : quatre passages et récupérations, plus deux artefacts (épisodes altérés, notations manquantes).
- Bancs : contrôles, lanceur, scellement.

## 5. Ordre de grandeur

**Code**
- Module : environ 250 à 350 lignes ; tests : environ 400 à 500 lignes.
- Scripts d'instance : environ 50 lignes à modifier, plus environ 120 lignes de tests.
- Procédures : six à huit scripts, déclinés plus qu'écrits, en tout environ 1 500 lignes, bancs compris.
- Avec la relecture R2 et la répétition jouet : **environ 2 à 3 jours de session**.

**Carte**
- 8B : la borne basse mesurée est de 7 565 s, sans finir. Au plus 23 × 3 072 = 70 656 passes de décodage.
- Aux épisodes, une passe coûte 88,6 ms (6 499 s pour 73 362 passes, contextes d'au plus 5 798 jetons). Les contextes des juges sont plus longs, environ 33 000 caractères en moyenne : invites H3 et H4, plus 4 108 caractères d'énoncé et 8 035 d'ensemble. C'est une estimation, non mesurée.
- D'où environ 7 600 à 9 500 s pour le 8B.
- 3B : débit inconnu, peut-être 3 000 à 5 500 s.
- Mise en place : environ 15 minutes (de 10:36 à 10:51 au pilote, dont 801 s de tests).
- Total : **environ 3,5 à 4,5 heures**, à la limite des bornes actuelles (15 000 s pour `duree_max_s`, 270 et 300 minutes de délais). D'où l'intérêt de l'écriture par lot et d'une échéance par juge.

## Réserves
- Le débit des juges n'a jamais été mesuré. Le chiffre de 7 565 s est une borne basse pour le 8B, rien de plus.
- Le nombre de lots faits au pilote est inconnu.
- La reprise de l'entropie, le statut des notations partielles et l'échéance par juge sont des choix de préenregistrement. Changer `lot_juge` ou `max_nouveaux_juge` serait un écart au protocole gelé, donc un nœud de décision.