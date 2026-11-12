# Consigne : contre-lecture 3 (R2) de T0.6, candidat 12, révision 3 — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-09 vers 22:00 UTC (`date -u`). Destinataire : un sous-agent **neuf**, d'un **autre modèle que le rédacteur de la révision 3** (Claude Opus 5.5) : Claude Fable (N-052). Il n'a écrit ni ce texte, ni ses brouillons, ni P3, ni le code ; il n'est pas le lecteur exploratoire de 7a (R-2041).

Dépôt : `/home/user/controle-ia-travail` (`main` local à `6886b61e`). `PYTHONPATH=src`. Python : `python3` ; si un module manque, `.venv/bin/python` (environnement en cours d'installation par la mère).

## Interdits (recopiés de `interdits-communs-v1.md`, même dossier)

1. **Fichiers et branches qu'on n'ouvre jamais** (ni lecture, ni affichage, ni copie, ni passage à un script, ni `git show`, ni `git ls-tree`, ni `git fetch`) : `diag/*/lecture-sondes-t06.json` de tout run, et nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; la lecture B de la course 7a et la branche `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/` et tout `runs/` de la course 7a (`20261109-070232-t06-reel`) et la branche `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; les items, clés et réponses de l'étiqueteur (branche `prep/etiqueteur-v2-lecture-interrompue-reprise-v1`).
2. Secrets : jamais une valeur de clé ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
3. Aucun appel de modèle ni d'interface externe, aucune location, aucun `vastai`, aucune dépense.
4. Git : aucun `checkout`, `switch`, `reset`, `stash`, `commit`, `push`, `fetch`, `merge`, `rebase`, ni modification de l'index ; autres commits par `git show <commit>:<chemin>` (déjà présents : `8cb539f9`, `fe240b24`, `1609a4bf`). Rien écrit hors des chemins de sortie ci-dessous (brouillons d'essai : dans un dossier temporaire hors du dépôt).
5. Pas de suite complète des essais ; essais ciblés permis.
6. Refus d'un contrôle de permissions ou d'un classifieur : s'arrêter sur ce point, le rapporter tel quel.
7. Heures relevées par `date -u`.

## Objet

`brouillons/T0.6-organismes-v0-v1-candidat12-r3.md` (`c24e268ee9821d1f37ff612023a9f07735864614f57e3a9cf58517b05bc55331`, vérifier d'abord). Sa section « Contre-lecture » contient la consigne de base (écrite au brouillon 4, « Points à viser ») et l'entrée « Contre-lecture 3 » avec la liste des fichiers à lire : **les suivre toutes deux**. Fichiers (rappel) : ce texte et son journal (`brouillons/T0.6-organismes-v0-v1-candidat12-r3-journal-v1.md`, `0728c7ed…`) ; la révision 2 (`git show 8cb539f9:brouillons/T0.6-organismes-v0-v1-candidat12-r2.md`, `0d6bf1c4…`) ; la contre-lecture 2 (`docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/contre-lecture-t06-course-v2-v1.md`, `09c202e6…`) et ses couples (`couples-candidat12-r2-v1.json`, `f094a804…`) ; le rapport de préparation du scellement (`git show fe240b24:docs/notes/g0-deux-semaines-v1/scellement-course-t06-v1/rapport-preparation-scellement-course-t06-v1.md`, `0aebc62b…`) ; la lecture A de 7a (`docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/lecture-A-exploratoire-non-opposable-v1.md`, `3c84c419…`) et la sortie de l'extracteur (`…/lecture-7a-v1/garde-equivalence-20261109-070232-t06-reel-exploratoire-non-opposable-r522.json`) ; `registres/decisions.md` R-1784, R-1840, R-1868, R-1891, R-1956, R-2038 à R-2051 ; `src/controle_ia/prereg.py` ; au commit `1609a4bf` : `scripts/lancer_t06_v13.sh`, `scripts/amorce_instance_t06_v11.sh`, `src/controle_ia/t06/configuration_v6.py`, `lanceur_v6.py`, `session_v12.py`, `scripts/tests-cibles-t06-v3.txt`, `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon5.json` ; l'ordre de la course 7a (`docs/procedures/ordre-fille-cles-2-course-dose-reponse-exploratoire-v1.md`, `4c6c70d4…`, § 9.2) ; `registres/go.md` (ligne GO-2026-11-02-28) ; `docs/brief-claude-code-programme-complet-v2.md` l. 160-201 ; les autres pièces de la consigne de base selon le besoin.

## Points à viser, en plus des « Points à viser » de la consigne de base

1. Les défauts M1 à M3 de la préparation du scellement et les couples W5 à W12, W11 bis, W13 à W15 : appliqués tels quels et au bon endroit (rejouer l'application par script dans un dossier temporaire, à partir de la révision 2, et comparer l'empreinte au `c24e268e…`) ; les couples X1 et suivants du rédacteur : justifiés, sans effet sur les sections gelées non déclaré.
2. **Aucun chiffre de 7a dans un critère** (ordre de 7a, § 9.2 : la puissance d'après les heures et les variances, jamais d'après le signe) ; ce que la r3 tire de 7a (section « Ce que les auteurs savaient », puissance de la confirmation 7b) : coût seulement, déclaré exploratoire (R-522).
3. **Devis et plafond** : 16 à 26 USD attendus, pire 151, sur GO-2026-11-02-28 (200 USD, échéance 16 novembre) ; heures réelles de 7a (lecture A : run 12,97 h, instance 13,59 h ; pic de mémoire 26,0 Gio ; un échec d'allocation non bloquant) ; recommander un plafond (garder 200, ou le réduire) et dire si l'échéance du 16 tient avec une création de 7b au plus tard le 15.
4. **Chaîne v13, amorce v11, 2 022 essais attendus** : cohérence du texte avec le lanceur et la configuration au commit `1609a4bf` (valeurs de configuration entre texte et lanceur).
5. **Empreinte du candidat 4** `a81cd47e…` (citée, non vérifiée) : la vérifier si le fichier est dans le clone local (`git log --all`, sans `fetch`) ; sinon l'écrire « non vérifiée » et dire quelle branche il faudrait récupérer.
6. **Compteur `jetons_generes`** (cause non vérifiée, R-2046) : ce que le texte en dit et ce que le code au commit `1609a4bf` fait.
7. **Marqueurs** : `controle_ia.prereg` ne refuse que sur les dix marqueurs restants (essai à valeurs factices dans un dossier temporaire) ; table des marqueurs complète et cohérente ; `DECISION_LAZAR_ECART_DT4_R2041` se remplit par renvoi à R-2048 et au rapport d'audit DT-4 (à venir) ; T0.7 devra déclarer l'écart DT-4 (R-2048) : la r3 ne doit pas affirmer « 7a jamais lue par une sonde ».
8. Tout ce qui pourrait faire perdre ou fausser la course 7b (création au plus tard le 15 novembre).

## Sorties

- Rapport `prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r3-cl3.md` : modèle qui contre-lit (dire lequel vous êtes, d'après ce que vous savez de vous) ; brouillon relu et son empreinte ; verdict en une ligne (« scellable après couples » / « non scellable » avec bloquants) ; remarques numérotées, chacune classée bloquant / majeur / mineur, avec lieu, raison, correction ; réponses aux points 1 à 8 ; liste des pièces lues avec empreintes vérifiées ; interdits tenus.
- Couples `prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r3-cl3-couples-v1.json` : liste d'objets `{"id", "ancien", "nouveau"}` (forme de `couples-candidat12-r2-v1.json`) ; chaque « ancien » présent exactement une fois dans la r3 au moment de son application, dans l'ordre ; vérifier par script dans un dossier temporaire que tous s'appliquent et que les marqueurs restants sont ceux attendus.
- Compagnons `.sha256` (`PYTHONPATH=src python3 -m controle_ia.scellement sceller FICHIER`).
- Ne rien committer, ne rien appliquer à la r3. Rendre à la mère : chemins, empreintes, verdict, bloquants, recommandation de plafond.
