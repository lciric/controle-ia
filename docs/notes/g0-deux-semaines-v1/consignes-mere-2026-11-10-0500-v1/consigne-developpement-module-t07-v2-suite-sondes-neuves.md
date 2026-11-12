# Consigne : suite du module de lecture de T0.7 — sondes neuves de l'étape A, lectures manquantes, répétition jouet — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10, écrite vers 04:58 UTC (`date -u`). Destinataire : **le développeur du module de T0.7 v2** (même sous-agent, qui a rendu `rapport-developpeur-t07-module-v2.md`, `b4d5784b…`, commits `9e844915`, `984796f2`). Il continue sur le même arbre et la même branche.

## Lieu

Arbre `/home/user/wt-t07`, branche locale `prep/t07-module-v2` (poussée par la mère à `984796f2` sur le dépôt de travail : n'y pousse rien toi-même). Commits locaux permis sur cette branche seulement ; jamais `fetch`, `push`, ni action sur `main`, sur `/home/user/controle-ia-travail` (sauf son interpréteur `.venv/bin/python`) ni sur `/home/user/integ-t06`. **Committe à chaque jalon** (au moins après les sondes neuves, après la répétition jouet, après les lectures manquantes) : le conteneur a redémarré deux fois cette nuit, seul un commit survit.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/interdits-communs-v1.md` (`851028fc…`), en entier, avec les deux exceptions de ta consigne précédente (commits locaux sur ta branche ; essais de T0.7 et suite complète permis sur ton arbre). Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni la branche `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. Aucun appel externe ni téléchargement (si la répétition jouet en demande un, arrête ce point et rapporte), aucune dépense. Pas de nettoyage hors de tes propres dossiers temporaires (motif du refus « Shared Scratch Sweep » : ne le contourne pas). Garde des secrets à 0 avant chaque commit.

## Décisions de la mère sur les écarts de ton rapport

1. **Écart 1 (sondes neuves non calculées) : écrire le code, ne pas changer le texte.** Le brouillon 19 garde l'apprentissage à l'étape A, sur l'instance (plan, point 8, étape A (1) à (4) ; « Métrique » ; section « Module » l. 2094 à 2467). À écrire, en **fichiers neufs** de `src/controle_ia/t07/` (par exemple `sondes_neuves_v1.py`, `lectures_t07_v1.py`), appelés par la commande `lecture_v2` (tu peux modifier `lecture_v2.py` sur ta branche : aucun texte scellé ni `main` ne le cite ; tes empreintes de `9e844915` restent vraies pour ce commit) :
   - les **30 couples neufs** (familles × concepts × couches du texte), appris par les fonctions du **paquet gelé** (`familles.entrainer`, et `entrainer_v2(…, calcul="produit_matriciel_v2")` pour Mahalanobis avec l'essai d'égalité au paquet gelé avant chaque usage, l. 1194 à 1200 ; réutiliser, ne rien réécrire de ce que le paquet fait) ; aires de validation générique (avant le champ et, pour le domaine, sur l'action entière) ;
   - la **sonde principale par concept**, règle d'ex aequo écrite (l. 1201 à 1207), consignée avec son empreinte **avant toute notation d'une action d'organisme** (garde : notation refusée si l'empreinte n'est pas écrite) ;
   - la notation de toutes les actions des neuf conditions (point 8, étape A (3)) : 4 principales, 30 couples neufs, 24 figées (déjà fait), T7-P6 et son témoin, directions des concepts, **témoins lexicaux** (sur `texte`), **base « coût seul »** (l. 1060), les 200 directions de plancher par principale ;
   - les lectures **T7-P3 à T7-P19** selon leurs lignes de la table des prédictions et du plan d'analyse, dont le **placebo** (T7-P19 : 200 permutations, unité l'épisode, échange par tâche, graine dérivée `placebo/<sonde>/<jeu>`, déclencheur R9 unique, l. 1044 à 1052) ;
   - aucune moyenne ni médiane sur les jetons dans une sonde de production ; graines par `SeedSequence` dérivées par clé (R9) ; chaque garde neuve éprouvée sur un cas sain et un artefact (R5).
2. **Écart 2 (ouverture réduite inscrite pendant l'étape A → `notation-t07.json`)** : accepté ; la mère l'écrira au brouillon 20.
3. **Écart 3 (interprétations de la garde adaptée)** : gardées telles quelles ; elles iront au contre-lecteur du code. Les lister au rapport complémentaire, une ligne chacune, avec la lettre du texte.
4. **Écarts 4 et 5, Q10** : côté texte ; la mère les écrira au brouillon 20 (clés de configuration, nom `lecture_v2`, liste des modules et fichiers d'essais, noms `niveau_base_t06` et `scores_base_t06`). Ne rien écrire dans le brouillon.
5. **Écart 6** : à faire, après le point 1 : contrôle de disjonction des tâches d'évaluation et de réserve ; T4 (`aire_stratifiee`, `difference_aires_appariee`) ; réserves R1 à R13 par identifiant dans `lecture-t07.json` ; durées dans le résultat ; repli du recalcul ; **répétition jouet de bout en bout** sur la chaîne de T0.6 en mode `jouet` (commit `1609a4bf`, lisible par `git show` ou par un arbre détaché que tu crées sous `/home/user/wt-t07-jouet` ; aucun essai existant modifié).
6. **Q11** (arrêt de T0.6 sans `lecture-cout-t06.json`) : établir le fait dans le code gelé de la chaîne au commit `1609a4bf` (`src/controle_ia/t06/`, lanceur `scripts/lancer_t06_v13.sh`) : le fichier est-il écrit quand la chaîne s'arrête ? Chemin et lignes au rapport. Le module garde la lettre (refus, attente) tant que la mère n'a pas écrit autre chose.

Ordre : 1, puis 5 (répétition jouet d'abord), puis le reste de 5, 6 à tout moment. Si le temps manque, rendre après le point 1 et la répétition jouet, en le disant.

## Essais

Essais de T0.7 (v1, v2 et neufs) à chaque jalon ; la suite complète si le temps le permet, avec `-o tmp_path_retention_policy=failed` et un `--basetemp` neuf sous ton arbre (effacé ensuite par son chemin exact). Aucun essai existant modifié pour passer.

## Sorties

Commits locaux sur `prep/t07-module-v2` ; rapport complémentaire `docs/notes/g0-deux-semaines-v1/t07-module-v2/rapport-developpeur-t07-module-v2-complement-v1.md` dans ton arbre, scellé, avec compagnon (le premier rapport n'est pas réécrit) : fait, essais (comptes, durées, heures `date -u`), table complète des empreintes du code au dernier commit, valeur proposée de `COMMIT_CODE_T07`, empreinte canonique de la configuration brouillon, écarts texte / code restants, fait de Q11. Réponse courte à la mère : commits, comptes d'essais, ce qui reste avant la contre-lecture du code.
