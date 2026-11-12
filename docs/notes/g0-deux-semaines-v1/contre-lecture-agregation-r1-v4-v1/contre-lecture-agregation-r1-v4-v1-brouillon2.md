# Contre-lecture neuve (R2) du préenregistrement « agrégateurs sur les scores réels de R1 v4 » — additif : brouillon 2 et code `c88cfd47` — v1

**Verdict : scellable après couples** (12 couples sur le brouillon 2, `couples-contre-lecture-agregation-r1-v4-v1-brouillon2.json`) et corrections de code Q1 à Q4 (Q5 faite par `analyse_v2`).
Les 17 couples d'auteur sont justes : le brouillon 2 est exactement le brouillon 1 plus ces 17 couples, à une ligne près (le titre, « brouillon 2 », hors couples : à déclarer).
31 essais sur 31 passent. Opposabilité tenue.

- Lecteurs : fille 9 (lignée Claude Opus 5.5, même modèle que l'autrice) ; la seconde lecture Sonnet du brouillon 1 (points 2, 3, 7) reste valable sur les passages que les 17 couples ne touchent pas, et ses couples sont repris ci-dessous. 6 novembre 2026, de 12:41 à 12:31 UTC (`date -u`).
- Ce rapport complète `contre-lecture-agregation-r1-v4-v1.md` (brouillon 1, `39cf2b3e…`), qui reste tel quel pour tout ce qui n'est pas repris ici.
- Pièces, empreintes recalculées et égales : branche `prep/fille-11-agregation-v1` à `6d0f84bc` ; brouillon 2 `fb2c93ef…`, couples d'auteur `260fefc7…`, rapport `4307d847…` ; `analyse_v2.py` `f02b7580…` et `tests/test_agregation_r1_v4_v2.py` `ef0fb00c…`, au commit `c88cfd47` (égaux à la table du brouillon 2). Aucune sortie de R1 ou R2 lue.

## Les 17 couples d'auteur

1. Lecture déclarée sur `main` à `a113adb6` (couples 2, 3, 4, 5, 10, 11, 12) — **juste** :
   - `a113adb6` est un ancêtre de `main` ; les trois textes ont les empreintes citées ;
   - les extraits sont conformes (vérifié de mon côté, rapport du brouillon 1, point 1) ;
   - « la principale corrige par Bonferroni » est exact (principale, l. 80 : Bonferroni sur W − G et W − J3s à 97,5 %).
2. Paragraphe sur l'hybride (couple 6) — **juste**, et il couvre le constat A3 (recombinaison de données réelles, pas un épisode joué ; non-échangeabilité ; effet de contexte ; audit R4 d'abord sur les effets de pas). Mon couple 8 ci-dessous y ajoute l'appariement (9 actions sur 10 partagées) et ce qu'un « confirmé » ne sépare pas (constat A4).
3. Holm dans la famille, plus borne d'union (couples 12 et 13) — **juste sur le fond**. La phrase « que la session mère tient pour acceptable » ne suffit pas : la borne n'est vérifiable que si chaque texte contrôle son taux à son niveau nominal, et aucune décision n'en dépend. Couple 9 : « à titre d'information seulement ».
4. Commande passée à `analyse_v2` (couples 1, 14, 15, 16) — **juste** :
   - `analyse_v2` ne diffère de `analyse_v1` que par la recette de W (5 plis de 12 par `np.array_split` ; L-BFGS-B, `gtol` 10⁻⁵, 10 000 itérations ; écart type sans correction, sous 10⁻⁸ remplacé par 1 ; garde de 60 tâches) et par le nom de la commande ;
   - c'est la recette de la principale (Métrique 2 et 3, l. 58 à 60) ; seule la permutation des plis diffère, et c'est déclaré ;
   - `analyse_v1` reste au dépôt, jamais lancée.
5. Couples 7 à 9, 17 — **justes** : réduction, plis, liste d'arrêt. Mon couple 11 sur le brouillon 1, qui portait sur la recette de W, est donc levé.

## Mes couples sur le brouillon 2 (12 ; chaque « ancien » unique dans le brouillon 2, vérifié par script, appliqués dans l'ordre)

- Couples 1, 2 : théorie (A1, A2 ; δ_k ≥ 0 est une hypothèse ; transposition « budget, puissance » → « décalage, aire »).
- Couples 3, 4 : plages cohérentes avec les gardes de puissance (B2).
- Couple 5 : conduite au plafond (C1) : « appuyée à m = 1 seulement » à a_W ≥ 0,95 ; « non interprétable (plafond ou fuite) » à a_W ≥ 0,999 tant que l'audit R4 n'a pas conclu.
- Couple 6 : trou de la table des issues (B1, conforme au code `lire`).
- Couple 7 : « appui partiel » mis en accord avec la règle et `lire_hag` (B3).
- Couple 8 : appariement des hybrides et dépendance intra-épisode (A3, A4), ajoutés au paragraphe d'auteur.
- Couple 9 : borne d'union à titre d'information.
- Couple 10 : non-convergence → nœud avant tout relancement.
- Couple 11 : rapport aux verrous des textes scellés (par épisode l. 133, principale l. 167 : « une autre agrégation »). Ce texte n'est pas leur relecture, et ses issues ne les qualifient jamais. Ce point n'est pas traité par les couples d'auteur.
- Couple 12 : GO-2026-11-06-03 relu dans `registres/go.md` de `main`, l. 259. L'en-tête du brouillon 2 dit encore « non relu ».

Après application : `controle_ia.prereg.problemes` ne rend que les deux lignes attendues d'un brouillon (entrée de contre-lecture, marqueur `<<CONTRE_LECTURE_1>>`).

## Code (`c88cfd47`)

- **31 passed** en 48,69 s (25 de la v1, 6 de la v2 ; `--basetemp` propre, supprimé). Les essais v2 éprouvent les cinq plis de douze, les réglages de la principale, la régression saine et son artefact, l'écart type nul remplacé par 1, l'analyse de bout en bout et la commande décisive.
- **Q5 faite** (recette de W). Restent **Q1 à Q4**, inchangées : `analyse_v2.main` est celui de la v1.
  - Q1 : liste fermée du code non vérifiée contre le texte ;
  - Q2 : chemin du préenregistrement non imposé ;
  - Q3 : empreintes d'entrée non exigées (`scores-p3.npz` `968414fc…`, activations selon la fiche v4) ;
  - Q4 : aucune garde de second passage ;
  - plus les artefacts R5 « non scellé » et « arbre sale » de la commande décisive, toujours absents.
- Détail : `corrections-code-agregation-r1-v4-v1.md`.
