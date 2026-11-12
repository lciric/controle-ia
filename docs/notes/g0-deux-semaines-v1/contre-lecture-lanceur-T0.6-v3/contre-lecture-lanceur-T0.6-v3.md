# Contre-lecture du lanceur T0.6 v3 (delta v2 → v3) et du candidat 1 de T0.6 (R2, lignée Opus 5.5) — v1

**Verdict : lançable après corrections.**
C-V3-1 à C-V3-4 sont faites comme écrites, avec cas sain et artefact ; 185 essais (76 + 67 + 42), banc 55/55 et E1 v3 rejoués conformes.
Avant le scellement :
- 12 couples vers le candidat 2 : six valeurs « à remplir » invisibles au contrôle des marqueurs, clé `mahalanobis_calcul` dans la configuration scellée, branche, devis ;
- une correction de code recommandée (C-V4-1 : la fin de run de l'amorce sous le même verrou que la minuterie) ;
- E2 et E3 avant le 11 novembre.

- Contre-lecteur : fille 9 (lignée Claude Opus 5.5), qui a fait la contre-lecture du lanceur v2 et n'a écrit ni le code ni le candidat. 5 novembre 2026, de 22:13 à 22:27 UTC (`date -u`).
- Consigne : `docs/notes/g0-deux-semaines-v1/consigne-contre-lecture-lanceur-T0.6-v3-v1.md` (`260730cf7e59c664…`, compagnon vérifié, `main` `7e09c6e7`).
- Pièces, empreintes recalculées et égales :
  - branche `prep/t06-lanceur-v2` à `4f1b402d` : 19 fichiers ajoutés, 0 modifié depuis `0d48103b`, `sondes/familles.py` intact ;
  - rapport v3 `c8c318bb…` ; `familles_v2.py` `4fea2c52…` ;
  - candidat 1 `4c27a254…`.
- Ce que je n'ai pas fait : aucune location, aucune clé, rien sous `donnees/` ni `diag/`, aucun `.sha256`, rien d'existant modifié. Le `--basetemp` et le `TMPDIR` du banc et d'E1 sont supprimés.

## Points (une ligne chacun ; gravité)

1. **C-V3-1 — conforme (note).**
   - Remplissage à `min(85 Mo, 90 Mo − 1 Mo − 1 000 × actions)` ; fichier vérifié à 90 Mo ; un fichier trop gros est retiré et réécrit en deux, récursivement, sans arrêt.
   - La garde d'avant les épisodes exige qu'une action au pire cas tienne dans un morceau.
   - Artefacts éprouvés :
     - le scénario de la contre-lecture v2, 50 actions à 2 688 octets de la borne : réécrit 25 + 25, le run finit ;
     - le jouet à 100 octets de la borne : 5 réécritures ; la v2 s'arrête aux mêmes bornes.
   - Manifeste cohérent après découpe : la liste `morceaux` ne contient que les fichiers finaux, `reecrits` les fichiers retirés. Le nom d'un fichier retiré est réutilisé par sa première moitié, et son sceau n'est écrit qu'au succès.
2. **C-V3-2 — conforme ; le risque 3 du développeur est réel mais étroit (à corriger, C-V4-1).**
   - Ce qui est en place : la branche du second démarrage passe avant les contrôles d'heure ; `t06-consigner.sh` est sous `flock -w 1500` ; les commits en attente sont poussés avant la destruction ; essais avec la dépense épuisée dans le passé.
   - Le risque : la fin de run de l'amorce (`commit_verifie`, `pousser`) ne prend pas le verrou. Si la minuterie consigne au même instant (heure de dépense épuisée ou échéance pendant la fin de run), un `index.lock` fait échouer l'un des deux commits.
   - Le cas grave : `commit_verifie` lit cet échec comme « aucun résultat léger à committer ». La suite pose alors `t06-fin-normale` et pousse une branche sans les résultats.
   - Le rattrapage est partiel. `consigner_partiel` fait `git add -A runs diag` et rattrape donc aussi un commit jamais fait, mais seulement si l'instance redémarre. À l'échéance, la minuterie détruit après sa propre consignation, et ce qui n'était pas encore écrit par le run est perdu.
   - Probabilité faible : il faut que l'échéance, au 17 novembre à 00:00, ou les 200 USD tombent pendant les quelques minutes de la fin de run.
   - Correction (C-V4-1) : prendre le même verrou dans la fin de run ; distinguer « rien à committer » (`git diff --cached --quiet`) d'un commit en échec ; avant de poser `t06-fin-normale`, vérifier que `git status --porcelain runs diag donnees` est vide.
3. **C-V3-3 — conforme (note).** `search offers "id=…" --storage <disque_min_go> --raw` ; le disque est écrit dans `lancement.txt` ; le faux `vastai` refuse un appel sans `--storage`. La syntaxe réelle de l'outil et le prix de l'instance créée restent pour E2.
4. **C-V3-4 — conforme ; l'essai d'égalité suffit pour l'implémentation, pas pour le domaine (note, C-V4-2 facultative).**
   - En place : même interface, mêmes μ et P, même empreinte ; essai joué avant chaque usage, une fois par sonde (4 par couple) ; un échec met le couple en « échec », jamais l'ensemble ; défaut `paquet_gele`.
   - Ma mesure (`outils/egalite_mahalanobis_v1.py`) : P appris par `familles.mahalanobis`, rétrécissement 0,1, conditionnement 5,6·10³. Jetons « réalistes » : échelles hétérogènes, 8 dimensions de grande amplitude (× 300), moyenne décalée, passage par la demi-précision.
   - Résultats : écart relatif de 6,5 à 6,9·10⁻¹⁵ sur les jetons réalistes, 4,5·10⁻¹⁵ sur les 256 jetons synthétiques. La notation est 84 à 90 fois plus rapide (machine chargée) ; le gain d'environ 30 fois du rapport porte sur le couple entier, apprentissage et essai d'égalité compris, et il est cohérent.
   - Les maxima par action ne sont pas égaux au bit près (écart de l'ordre de 10⁻¹⁴) : sans effet sur les aires, sauf égalités exactes.
   - Recommandation (C-V4-2, facultative) : jouer l'essai aussi sur 256 jetons réels des actions notées, pas seulement sur des jetons tirés autour de μ.
5. **Essais, banc, E1 — conformes (note).**
   - **185 passed** en 163,88 s. Une mesure de durée a tourné en même temps que la suite (déclaré ; aucun effet sur les comptes).
   - Banc v3 : **55 mutations, 55 tuées**, 6 témoins verts (22:17 → 22:25 UTC).
   - E1 v3 rejouée sous `produit_matriciel_v2` : code 0 ; 34 lignes `PROGRES`, contre 36 au rapport (écart de jouet, à expliquer en note) ; 0 mot interdit dans le journal, `run.err`, `run.json` et les 8 traces ; 12 essais d'égalité, tous égaux (écarts de 3 à 4·10⁻¹⁵), écrits dans le seul résultat scellé des sondes ; trois commits poussés.
6. **Candidat 1 contre v3 (à corriger ; 12 couples vers le candidat 2).**
   - Conformes : les noms `lancer_t06_v3.sh` et `amorce_instance_t06_v3.sh`, les signatures (inchangées), « Tests attendus » et l'amorce citée par empreinte, onze marqueurs distincts, la ligne Mahalanobis sous `<<MOT_LAZAR_DT>>`.
   - **Défaut 1** : les six valeurs de l'en-tête sont écrites « `à remplir au candidat 2` », qui n'est pas un marqueur. Le contrôle des marqueurs (`<<[A-Z0-9_]+>>`) et `problemes` ne les verraient pas si on les oubliait ; seul `controles` les refuserait, le jour même.
     - Couples 1 à 9 : un marqueur `<<VALEURS_CITEES_T06>>` (six occurrences, une par valeur), sa ligne dans la table des marqueurs, et « onze » → « douze ».
   - **Défaut 2** : la clé `mahalanobis_calcul` (et `familles_descriptives`) n'est pas dite comme entrant dans la configuration scellée. Couple 10, sur la ligne Mahalanobis.
   - **Défaut 3** : le devis ignore la durée sous `produit_matriciel_v2` (≈ 18 min par couche). Couple 11.
   - **Défaut 4** : la branche n'est pas nommée (« `calcul/…` »). Couple 12 : `calcul/t06-reel-v3`, défaut du lanceur v3.
   - Le module `controle_ia.t06.lanceur_v3` n'a pas à être cité : l'amorce le lance, et l'empreinte du code le couvre.
7. **E2 et E3 : ma liste v2 tient, avec ces ajouts.**
   - **E2 (Vast)** :
     - syntaxe réelle de `search offers … --storage 150 --raw` ; prix de l'instance créée comparé à `dph_total` et `storage_total_cost` lus ;
     - `flock` présent sur l'image `python:3.11-bookworm` ;
     - redémarrage réel après une dépense épuisée simulée (heure basse) : poussée, puis destruction ;
     - échéance posée pendant la poussée finale, après C-V4-1 (risque 3) ;
     - le reste de la liste v2 (clés et unités de l'offre, clone partiel avec le jeton, PUT « stopped », DELETE, `MemTotal`).
   - **E3 (carte)** : la liste v2 ; plus la durée d'un couple Mahalanobis sous le calcul retenu par Lazar, sur 16 cœurs, et la dernière ligne exacte de la suite complète (pour `<<TESTS_ATTENDUS_T06>>`).
   - **Aucun bloquant qui ne puisse attendre E2 et E3.** C-V4-1 est à faire avant E2, pour qu'E2 l'éprouve.

## Fichiers

- `couples-candidat1-vers-candidat2-T0.6-v1.json` : 12 couples. Chaque « ancien » est unique dans le candidat 1 (`4c27a254…`) ; ils sont appliqués dans l'ordre et vérifiés par script : plus aucun « à remplir » en accents graves, 12 marqueurs distincts, chaque clé lue par la chaîne citée une fois.
- `corrections-code-lanceur-T0.6-v4.md` : C-V4-1 (à corriger) et C-V4-2 (facultative).
- `outils/egalite_mahalanobis_v1.py` et sa sortie.
