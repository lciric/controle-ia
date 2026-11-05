# SPARKS-EXP7-NUL — contre-lecture du delta : brouillon 2 de l'addendum n° 1 et code v2 (`50fb15cd`)

Contre-lecteur neuf (R2, sous-agent Claude, Opus 5.5) : n'a écrit ni le texte v1, ni l'addendum, ni le code, ni aucune
contre-lecture précédente. Consigne `consigne-contre-lecture-delta-sparks-v2-v1.md`, compagnon « OK » avant lecture.
Ouvert le 4 novembre 2026 à 13:21 UTC ; coupé par un redémarrage du conteneur (≈ 13:40 → 22:03) ; écrit à 22:14 UTC
(`date -u`). Lecture seule du dépôt ; aucun commit, aucun `.sha256`, aucun réseau (aucun fetch : le commit était présent
localement), aucun modèle, aucune dépense. Travail au bloc-notes (dépôt nu local de répétition, copies extraites).

## Verdict

**À reprendre (le code ; le texte est scellable après les 11 couples ci-joints).**
Le brouillon 2 est exactement brouillon 1 + 29 couples + D-1 à D-8 ; la liste fermée est conforme ; l'incrément, B3, B4 et l'aveuglement suivent le texte ; essais 159/159 rejoués.
Mais le chemin de redémarrage (copies par lots, phase causale) n'existe pas dans le code, et la dépense n'est pas bornée sans session vivante : il faut du code neuf, puis rejouer et contre-lire ce nouveau delta avant le scellement.

## Points (gravité ; une ligne chacun)

### Q1. Brouillon 2 = brouillon 1 + 29 couples + D-1 à D-8, rien d'autre
1. **Conforme.** J'ai rejoué le script (`a84c8576…`) sur une racine copiée au bloc-notes : sortie identique à l'octet (`7775cbca…`), empreinte intermédiaire `141f1684e9ad0b8c95b5339bde7921245265067a88f2fb6aeeee18d35b4e6636`, brouillon 2 identique à l'octet (`7e98397e…`) ; 3 marqueurs. Les D-5 à D-8 suivent les quatre décisions de conv-audit (R-1476) et la consigne du développeur. Copie de la sortie : `sortie-rejeu-appliquer-couples-v1.txt`.

### Q2. Le code applique-t-il le texte ?
2. **Conforme — `analyse.increment` :** rangs croissants et rangs moyens (`rangs`) ; c_b = (r_L + r_b)/2 ; G = aire(c) − aire(s) ; rééchantillonnage des 48 cas avec A et B ensemble, rangs recalculés à chaque tirage ; permutation des couples (p_A, p_B) entre cas, A sur A ; p_perm = (1 + #≥G)/(n + 1) ; « tenu » = G > 0 et borne inférieure > 0 et p ≤ 0,05, et « tenu » a la préséance ; plafond ≥ 0,95.
3. **Conforme — conjonction :** `lecture_principale` exige « tenu » sur B3 **et** sur B4 ; avec plusieurs lignes, le verdict est « non concluant ».
4. **Conforme — `scores_b3_b4` et B4 :** o₄ maximise l'aire sur les 96 modèles, +1 en cas d'égalité ; il est fixé une seule fois avant l'incrément, et les tirages ne le recalculent pas ; le seuil de B4 vient de l'étalonnage avec o₄ ; B3 garde o₃ et le seuil de l'étalonnage.
5. **Conforme — générateurs :** les six générateurs neufs viennent de `SeedSequence(entropie du texte v1, spawn_key = clé de tâche)` (`plan.generateur_tache` en v1) ; `bootstrap` est consommé dans l'ordre M3, M4, M5, C1, inchangé par rapport à la v1.
6. **Conforme — B3 aveugle et aucun score journalisé :** `bases_poids_cas` ne reçoit que le dossier servi et les couches du départ ; `ajouter_bases_coffre` n'écrit qu'au coffre (droits 700/600), et le journal ne contient que le nom du cas ; les messages d'erreur ne contiennent aucun score.
7. **Moyen — secondaire « sur M5 » absent du code :** le texte (« Métrique », l. 243) dit « même calcul sur M1 … et sur M5 » ; `secondaires_increment` ne calcule que M1 et l'aire du lecteur moins celle de la base. Correction de code demandée (liste en fin de document).
8. **Mineur — construit inversé au secours :** le texte (« Modèles », l. 159) dit qu'au construit inversé l'orientation *a priori* de B3 s'inverse ; `bases.orientation_b3` garde toujours +1 a priori. L'écart ne se voit qu'à une aire de 0,5 exactement sur l'étalonnage. Correction de code demandée (paramètre a priori).
9. **Mineur — étape 0 :** conforme (révision fixée, quatre fichiers, `trust_remote_code` faux, « non mesuré » sans arrêt) ; `charger_candidat_hf` n'a jamais tourné (aucun réseau), et l'essai ne passe que par l'injection d'un chargeur factice.

### Q3. Lectures retenues du développeur (risque 2)
10. **L1 (`-y`, aucune sortie brute) :** juste ; **à écrire** dans la ligne de destruction (couple 1).
11. **L2 (un rappel aussi pour une faute des seuls composants) :** juste et conforme à « un rappel » ; **à écrire** (couple 4).
12. **L3 (clé de trop dans un élément = « composants invalides ») :** juste ; **déjà écrite** au brouillon 2 (l. 177, couple 12) ; aucun couple.
13. **L4 (o₄ fixé une fois, seuil recalculé avec o₄) :** juste ; **déjà écrite** (D-1, l. 186) ; aucun couple.
14. **L5 (secondaires tirés sur les générateurs `increment-<b>-…` après le principal) :** juste et sans effet sur le principal ; **à écrire**, R9 (couple 3).
15. **L6 (jeton de début retiré en tête du format au secours) :** juste, car l'outil remet ce jeton devant et le modèle voit la même séquence ; mais le texte dit « la sortie de `apply_chat_template` » telle quelle. **À écrire**, avec un essai d'égalité des jetons (couple 5 ; essai demandé).
16. **L7 (égalité des lots : seules les fractions décident sur l'instance) :** juste mais plus étroite que le texte (« parts rouvertes … et décisions porteur »). Les décisions « porteur » sont vérifiées par un essai unitaire dont l'échec arrête la course au lieu de passer sans lots. C'est plus strict, non silencieux, mais c'est un écart ; **à écrire** (couple 6).
17. **L8 (`CHEMIN_ADDENDUM`) :** juste, et la garde l'exige ; **à écrire** (couple 7).
18. **L9 (clone partiel et clairsemé) :** juste, mais jamais joué (Q6) ; l'amorce v2 n'installe ni `git` ni `curl` et suppose leur présence dans l'image `pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime` (non vérifié ; la sonde A1-v3 installe `git`).
19. **L10 (la liste fermée compte les compagnons et elle-même ; égalité exacte) :** juste ; la garde compare au fichier de la liste **au commit du code**, pas au texte de l'addendum, donc l'égalité entre les deux se contrôle au scellement (couple 9).

### Q4. Dépense
20. **Moyen — la garde `depense.projeter` est mécanique et éprouvée (R5)** : cas sain à 30 USD, artefact à 41 USD, sans lots, facture, entrées illisibles, état d'égalité inconnu, tous tués par le banc. Ses entrées (heures démarrées, `DEJA_USD`, phases faites) sont cependant écrites à la main par la session, donc passent par un modèle (R-1481).
21. **Majeur — chemin de redémarrage absent.** `vastai start` relance les arguments du conteneur, c'est-à-dire l'amorce, qui refuse dès que `amorce-depot` existe sur le disque gardé (amorce v2, l. 26-27 ; v1 : « une seconde exécution refuse de repartir »). L'environnement reste celui de la création (`PHASE`, `CLE`, `REPONSES`, `MODELES`, `DEJA_USD` ne changent pas). Le mode « arguments » n'offre aucune voie de copie écrite. Les 14 à 18 redémarrages de copie (E-4, A-11) et la phase causale (E-5, A-12) n'ont donc **aucune voie exécutable**. Les modèles (≈ 53 cas × 2 × ≈ 0,54 Go en bf16, calcul) ne passent pas par git.
22. **Majeur — borne sans session vivante (R-1481).** La carte est bornée sur la machine (le `timeout` de l'amorce arrête le conteneur et l'instance passe « exited »), mais seulement au premier démarrage, faute de chemin de redémarrage. Le stockage d'une instance arrêtée n'est **borné par rien sur la machine** : la destruction (`decision_instance`, puis `vastai destroy … -y`) exige une session. Une minuterie comme celle de la sonde A1-v3 (`amorce_sonde_hote_durable_a1_v3_v3.sh`, destruction par l'interface de Vast avec la clé du conteneur) ne tourne que pendant qu'un démarrage est en cours. Il faut donc : (a) que la machine se détruise elle-même à la fin du contrôle causal, après la poussée vérifiée des sorties ; (b) qu'elle se détruise elle-même à tout démarrage après l'échéance ; (c) écrire la borne résiduelle : stockage × durée d'absence, 0,53 à 1,20 USD par jour, hors GO après le 18 ; (d) un tir réel avant la création (R-1477) (couples 1 et 2 ; code). Une minuterie extérieure sans modèle (par exemple une tâche planifiée hors du compte Claude, avec une clé de Vast dédiée) relève d'un **nœud de Lazar** (compte, secret).
23. **Mineur — échéance et stockage :** traités (`FIN_STOCKAGE` = fin du 18 ; nœud le 16 ; destruction à l'échéance ; l'instance arrêtée est « en tâche » pour la routine de reprise). `duree_max_minutes` soustrait le stockage projeté, mais l'amorce n'en reçoit le `DEJA_USD` qu'à la création (couple 11).
24. **Mineur — état d'égalité au lancement :** avant la création, l'essai sur l'instance n'existe pas, et la garde refuse un état inconnu. Le texte doit dire que c'est l'essai jouet de la session qui sert alors (couple 6).

### Q5. Banc
25. **Rejoué : 22/22 v1 et 48/50 neuves, puis 50/50.** Les deux « survivantes » (liste fermée : fichier hors liste ; suppression) avaient une sortie vide, ce qui indique des processus tués pendant l'incident qui a précédé le redémarrage du conteneur. Rejouées seules, elles sont **tuées**, chacune avec « 1 failed » (`rejeu-mutation-suppression-v1.txt` pour la seconde ; la première l'a été dans le terminal en 94 s). Le banc du développeur (`22c10add…`) a « failed » pour ses 72 mutations tuées.
26. **Moyen — gardes neuves sans mutation :** `duree_max_minutes` (stockage non soustrait, plafond de 24 h retiré) ; l'échéance du 18 dans `projeter` et dans `decision_instance` (seul le nœud du 16 est muté) ; les droits 700 de `exiger_coffre` ; le compte d'`engager_bases` ; « cas servi sans bases » dans `scores_b3_b4` ; « 4 contre 4 » dans `etalonnage_b3_b4` ; les conditions de type, d'auteur et de dates de l'extension dans `go.verifier` (seul « extension » est muté) ; « commit du code cité en entier » et la descendance dans `garde_code` ; `trust_remote_code` ; **aucune mutation des scripts shell** (refus du GO, refus du code, `MINUTES < 60`).
27. **Mineur — le banc compte « tuée » tout code de retour > 0 :** une mutation dont le filtre `-k` ne sélectionne aucun essai (code 5) serait comptée tuée à tort. Exiger le code 1 et « failed » dans la sortie (sans effet sur les 72 du développeur).

### Q6. Risque 1 : scripts d'instance jamais joués
28. **Majeur — à jouer avant le scellement :** création **et** redémarrage **et** phase causale, en `MODE=jouet`, avec la minuterie de destruction (couple 8). Sans réseau, j'ai construit un dépôt nu local (alternats vers le dépôt, frontière superficielle copiée, `uploadpack.allowFilter` et `allowAnySHA1InWant` vrais) et un commit de lancement factice `b96d2d89…`, qui porte un addendum d'essai et descend de `50fb15cd`. Le clone `--filter=blob:none` en `file://` n'a pas fini en 300 s (arrêté par `timeout`), comme chez le développeur. Voie recommandée : jouer la répétition dans la session mère, qui atteint le dépôt distant, avec `RACINE_AMORCE` et `VENV_EXISTANT` locaux et une branche `essai/` (≈ 75 Mo extraits au commit : `diag/` 68 Mo, `src/` 1,5 Mo, calcul sur `git ls-tree -l`) ; ou bien un dépôt nu complet non superficiel. Ajouter les essais d'un second démarrage sur disque existant et de la présence de `git` et de `curl`.

### Q7. Liste fermée
29. **Conforme.** `git diff --name-status --no-renames 55399606 50fb15cd` donne 48 « A » et aucun autre statut ; l'ensemble est égal à `liste-fermee-v1.txt` ; `55399606` est un ancêtre ; les 24 compagnons « OK » ; les 24 empreintes du rapport sont justes.

## Changements de code requis (nouvelle version des fichiers, R12 ; puis rejeu des essais et du banc et contre-lecture neuve du delta)
1. **Chemin de redémarrage** dans l'amorce et le script d'instance : un second démarrage sur le même disque reconnaît son état (phase faite, lot suivant) au lieu de refuser. Il faut une voie de copie écrite et bornée sur la machine (conteneur gardé vivant au plus N minutes pour la copie, puis sortie), une phase causale sans variables d'environnement neuves (clé ouverte et réponses apportées par une voie écrite), et `DEJA_USD` lu à chaque démarrage.
2. **Minuterie de destruction sur la machine** (comme `amorce_sonde_hote_durable_a1_v3_v3.sh`) : autodestruction à la fin du contrôle causal après une poussée vérifiée, et à tout démarrage après l'échéance. `curl` et `git` sont exigés ou installés. Tir réel avant la création (R-1477).
3. `analyse.secondaires_increment` : secondaire « sur M5 » (c_b contre s_b).
4. `bases.orientation_b3` : a priori −1 au construit inversé, et l'appel au secours qui le transmet.
5. Essai : jetons de l'outil pour le format de conversation = `apply_chat_template(…, tokenize=True)` (secours).
6. Banc : mutations des gardes du point 26, mutations des scripts shell, et « tuée » seulement pour le code 1.

## Fichiers (ce dossier, neufs, sans compagnon)
- `couples-brouillon3-v1.json` : 11 couples ; chaque « ancien » est unique dans le brouillon 2 et à son application dans l'ordre ; 3 marqueurs gardés ; texte d'essai `e5535c96…` (non versé).
- `couples-brouillon3-contre-lecteur-v1.py` (le script qui les vérifie et les a écrits), `banc-rejeu-contre-lecteur-v1.txt`, `rejeu-mutation-suppression-v1.txt`, `sortie-rejeu-appliquer-couples-v1.txt`.
