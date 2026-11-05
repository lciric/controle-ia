# Contre-lecture adverse : plan de la voie « notations seules » (pilote de T0.5)

**Affirmations vérifiées, toutes exactes :**
- **Demandes de notation.** Il y a 180 demandes par juge. Aucun ensemble décisif n'est vide (e0 : 0 sur 60 ; e1 : 0 sur 60), ce qui donne 22 lots de 8 et 1 lot de 4.
- **Durée des notations du 8B.** 15 063,6 − 7 037,2 − 461,0 = 7 565 s.
- **Mise en place.** 972 s, de la création de l'instance au début du run (10:35:13 → 10:51:25).
- **Chargements.** 128 s pour le 8B et 48,7 s pour le 3B.
- **Graines.** Chaque graine dérive de l'entropie et du nom de sa clé (`manifeste.py` l. 37-48) : mêmes clés, mêmes graines.
- **Modules gelés.** `git diff 2660b07 HEAD` est vide sur `MODULES_LECTURE`, et aussi sur `src/`, `tests/` et `scripts/`.
- **`verifier_resultat`** suit le `run_id` écrit dans le fichier, pas le dossier où il se trouve (`manifeste.py` l. 142-151).

## Constats

**1. Majeur, bloquant si on l'implémente par une capture d'exception : « l'échéance du 8B passe, le 3B continue ».**
- `noter_ensembles` contrôle l'échéance par `_exiger_echeance` (`pilote_a.py` l. 150-153, 165). Celle-ci appelle d'abord `exiger_sans_signal`. Le dépassement d'échéance et le signal TERM lèvent donc la même classe, `GardeArret`.
- Le dépôt interdit de la capturer pour continuer (`gardes.py` l. 15-16 : « Ne jamais l'attraper pour continuer »).
- Une capture qui laisse le 3B démarrer avalerait un TERM. Cinq minutes plus tard, l'arrêt forcé (KILL) tomberait sans `arret.json`.

Correction :
- Le nouveau lanceur appelle `noter_ensembles` un lot à la fois (8 demandes, `lot=8`). Le découpage reste identique.
- Il contrôle lui-même l'échéance du juge avant chaque lot, sans exception.
- Il passe à `noter_ensembles` une échéance globale qui, elle, arrête vraiment le run.
- Tout `GardeArret` se propage. Un test vérifie qu'un TERM reçu pendant le 8B n'ouvre jamais le 3B.

**2. Majeur : le plafond du GO est calculé sur la mauvaise base.**
- Le plan déduit le plafond des échéances : 24 700 s, soit 8,9 USD.
- Or le seul arrêt certain est la surveillance, à la création plus 26 400 s. Au pilote, le pire cas ajoutait 10 minutes avant l'arrêt (`registres/depenses.md`, entrées du 12 octobre). Ici, cela donne 27 000 s, soit 7,5 heures.
- Au prix maximal du filtre (`PRIX_MAX=1.30`, `lancer_pilote_v2.sh` l. 34) : 9,75 USD, plus moins de 0,5 USD, soit environ 10,3 USD.
- Le plan se contredit : son crédit minimum compte 7,5 heures.

Correction (une des trois) :
- demander un plafond de 10,5 USD ;
- ou abaisser le prix du filtre à 1,13 USD de l'heure au plus ;
- ou raccourcir la surveillance.

**3. Majeur : le crédit minimum est faux, et le lancement serait bloqué.**
- Le lanceur exige heures × (prix de l'offre + somme des instances des autres projets en marche) + 1,2 USD (`lancer_pilote_v2.sh` l. 172, 212-214 ; R-149). Le plan omet le second terme.
- À 15:05 UTC, le crédit était de 8,47 USD, et l'instance 55555587 d'un autre projet consommait 3,98 USD de l'heure (`depenses.md` l. 65).
- Le minimum serait donc d'environ 7,5 × (1,0889 + 3,98) + 1,2 ≈ 39 USD.

Correction : écrire la formule complète dans la demande de GO, et demander à Lazar la recharge ou l'arrêt de son autre instance.

**4. Majeur : la durée du gel n'est pas écrite.**
- Le gel vaut « du scellement à la fin de la lecture… même pour une autre tâche » (`prereg/T0.5-pilote-8B-v1.md` l. 167). Or la lecture des juges n'est pas finie.
- `MODULES_LECTURE` (`lire_pilote.py` l. 82-85) contient `manifeste.py`, `gardes.py`, `scellement.py` et `propositions.py`. Le verdict renvoie à T0.6 la correction de `heures_declarees` (`docs/verdicts/verdict-T0.5-pilote-v1.md` l. 360).
- Toute modification de ces modules pour T0.6, ou pour le nouveau lanceur, avant le verdict complémentaire ferait échouer `exiger_modules_cites`.

Correction : écrire dans N-021, dans le nouveau préenregistrement et dans `etat.md` que le gel dure jusqu'au verdict complémentaire scellé. Les nouvelles gardes vont dans des modules neufs.

**5. Majeur : le lecteur neuf omet des gardes gelées.**
- Le texte gelé exige à chaque étape : constantes égales au manifeste d'analyse, version de numpy égale (2.4.6), commit courant et état de l'arbre consignés (l. 165 ; `_ouvrir_analyse`, `lire_pilote.py` l. 507-529).
- Le plan ne vérifie que les graines. Sans ces gardes, « l'équivalence avec `analyser` » n'est pas démontrée, et l'écart dépasse le « minimal » annoncé.

Correction : appeler `_ouvrir_analyse(racine, "20261012-150724-t05-pilote-analyse")`, fonction gelée qui n'écrit rien, puis `_etat_courant`. Les deux entrent dans le test d'équivalence.

**6. Majeur : la règle de relancement se contredit.**
- L'étape 6 dit : « un nouvel arrêt est un nœud, sans nouvelle tentative ».
- L'étape 8 dit : « relancement interdit dès qu'un fichier de notations est sur la branche », ce qui sous-entend qu'il est permis avant.
- Une panne de réseau au téléchargement, après le manifeste, tombe dans ce trou.

Correction : reprendre la liste fermée des causes du pilote (l. 198-204). Une cause d'infrastructure avant tout fichier de notations donne un relancement unique sur `-v2`, au même commit et dans le devis ; tout le reste est un nœud.

**7. Mineur : la marge sous le délai externe est mince.**
- Pire durée dans le run : 23 700 s, pour 24 000 s de délai externe. Il reste 300 s, contre 1 200 s au pilote.
- Le plan ne dit pas d'où part chaque échéance.

Correction :
- l'échéance du 8B part du début du run ;
- celle du 3B part de son premier lot, avec une borne globale à 23 100 s ;
- un test couvre les trois horloges.

**8. Mineur : les lignes de progression sont invisibles pour la surveillance.**
- La sortie d'erreur du lanceur va dans le fichier `run.err` (`pilote_t05_instance.sh` l. 329-330), et non dans le journal que lit `vastai logs` (l. 57). L'étape 13 n'aurait rien à lire.

Correction : recopier dans le journal, en tâche de fond, les seules lignes à préfixe fixe ; un test vérifie qu'aucun texte n'y passe. Les « passes de décodage » ne sortent pas de `noter_ensembles` : les déduire de `jetons_reponse`, sans toucher `pilote_a.py`.

**9. Mineur : la récupération et la consignation ne prévoient pas le cas « 8B échu ».**
- Le script tient pour complet un run qui a un résumé sans arrêt (l. 335-337). La récupération exige « deux fichiers de 180 ». Le cas « 8B échu, 3B écrit » serait donc rejeté ou mal consigné.

Correction :
- traiter explicitement le cas « un seul fichier » ;
- consigner l'échéance du 8B dans le résumé (scellé) et non seulement dans `arret.json`, sinon c'est un repli silencieux (R5).

**10. Mineur : l'ascendance et le « seulement des ajouts » ne sont pas énumérés.**

Correction : reprendre les points 1a, 1b et 1c de `recuperation_pilote_v1.sh` (l. 52-57), en resserrant le point 1c à `runs/R′/` et `diag/R′/`. Ajouter : aucun ajout, aucune modification ni suppression sous `diag/20261012-105125-…` et `runs/20261012-105125-…`.

**11. Mineur : les entrées du pilote ne sont vérifiées qu'en partie.**

Correction :
- exiger, pour `episodes.json`, `run_id` = pilote et `manifeste_sha256` = `8c3d7985…` ;
- citer et sceller aussi `runs/<pilote>/manifeste.json` et `arret.json` ;
- le script de l'instance les lit tôt, en plus du « Chemin des épisodes » ;
- comparer les formats des juges à ceux, scellés, de `episodes.json`, et les versions de torch et de transformers à celles du manifeste du pilote.

**12. Mineur : les expressions qui lisent les citations ne prennent que la première occurrence.**
- Sont concernés : `COMMIT_CITE` (`validation_reelle.py` l. 68), `CONFIG_CITEE` et `TACHES_CITEES` (`lancer_pilote_a.py` l. 55-56), et `lire_chemin` dans le script de l'instance.
- Un nouveau préenregistrement qui recopie les lignes du pilote ferait lire le mauvais commit ou la mauvaise configuration.
- Par ailleurs, « comparés au commit S′ » est impossible à citer dans le texte scellé à S′.

Correction :
- une seule ligne « Commit du code d'analyse » (C′, antérieur à S′) ;
- citer le pilote sous des intitulés distincts ;
- le lecteur prend S′ dans le manifeste de R′.

**13. Mineur : registre des GO.** Aucune entrée GO n'existe pour N-020 (R-155) dans `registres/go.md`, alors que l'étape 8 en exige une. Correction : inscrire N-020, puis N-021, avant les contrôles d'avant dépense.

**14. Mineur : R12.** Le plan modifie sur place `scripts/amorce_instance_t05.sh` et `pilote_t05_instance.sh`, dont le pilote cite les empreintes. Correction : créer des scripts à nouveau nom, ou nommer le précédent (revalidation, puis pilote) comme un écart à R12 dans N-021.

**15. Mineur : l'arrêt de la surveillance est codé en dur.**
- `surveiller-instance-t04-v1.sh` (l. 19) fixe l'arrêt à la création plus 6 heures. Pour 26 400 s, il faut passer comme base la création plus 4 800 s.

Correction : l'écrire dans `lancement.txt` et le tester, ou écrire une version 2 paramétrée.

**16. Mineur : section « Transparence ».** La session connaît déjà les deux faits suivants ; les y déclarer :
- les épisodes ont pris 88,6 ms par passe de décodage (6 499 s pour 73 362 passes) ;
- 344 s par lot suppose au moins 112 ms par passe, donc des lots presque tous au plafond de 3 072 jetons, et un plan B plausible pour le 8B.

Y déclarer aussi les résultats du double étiquetage, s'ils sont connus avant le scellement. Côté mémoire, rien d'inquiétant sur 80 Go, mais garder la règle « panne de mémoire → nœud » et le relevé `memoire_pic_gio` par juge.

## Verdict

**Tenable avec corrections.** Avant le scellement, il faut traiter les constats 1 à 6. Le 1 décide si un TERM peut être avalé. Le 2 et le 3 fixent le GO et le crédit à demander.

Aucun fichier n'a été écrit dans le dépôt. Aucune commande Vast.ai n'a été lancée. `episodes-defaut.json` et `chemin-defaut.json` n'ont pas été ouverts. Des fichiers du pilote, seuls des clés, des nombres et des empreintes ont été lus.