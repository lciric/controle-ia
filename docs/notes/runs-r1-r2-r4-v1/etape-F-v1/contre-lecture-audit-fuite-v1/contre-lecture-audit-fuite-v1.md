# Contre-lecture neuve (R2) du protocole d'audit de fuite de W sur R1 v4 (brouillon 1) — v1

## Consigne (message de la session mère, recopié mot pour mot)

> Mère — 09:20 UTC, 7 novembre. On continue ici (R-1649). Deux contre-lectures neuves (R2), dans l'ordre ; **recopie ce message mot pour mot en tête de chaque rendu** (il tient lieu de consigne). Sans clé, sans dépense, rien d'existant modifié, aucun `.sha256`.
>
> (A) **Protocole d'audit de fuite**, 30 minutes : `brouillons/audit-fuite-r1-v4-v1-brouillon1.md` (sur `main`, `3f009795…`, écrit par la fille 11 après lecture des deux verdicts, ce qui est déclaré). Questions : la règle de décision est-elle fermée, chiffrée, écrite avant tout calcul et symétrique (elle peut aussi conclure « lecture du sabotage » ou « non tranché ») ? Les bras A1 à A4 répondent-ils à la question des verdicts (coût gonflé ou consigne ; témoins à 27 %) avec le code existant ? Les seuils, fixés après lecture, sont-ils défendables ? Que manque-t-il pour sceller (code d'audit, marqueurs) ? Rendu : `docs/notes/runs-r1-r2-r4-v1/etape-F-v1/contre-lecture-audit-fuite-v1/` (verdict, couples sur le brouillon 1).
>
> (B) **Lanceur T0.6 v4 et ordres E2/E3**, 60 minutes : branche `prep/t06-lanceur-v2` à `b41a3f2d`, rapport `docs/notes/g0-deux-semaines-v1/rapport-developpeur-lanceur-T0.6-v4.md` (`028187c3…`), delta v3 → v4 (C-V4-1, C-V4-2, C-V4-3, `T06_REGISTRE_GO`), puis les brouillons `brouillons/ordres-t06-e2-e3-v1/ordre-fille-6-t06-e2-v1.md` et `…-e3-v1.md` : sont-ils exécutables à la lettre par une session qui porte les clés (commandes exactes, clés par nom, GO-2026-11-06-01 cité, plafonds E2 ≤ 1,5 USD, E3 ≤ 3,5 USD, cumul ≤ 5, registre de `main`, arrêts, destruction par l'identifiant) ? Ce qui peut faire perdre l'argent ou la course ? Rendu : `docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v4/` (verdict, couples pour les ordres, corrections de code éventuelles).
>
> Pousse chaque rendu sur `prep/fille-9-contre-lectures-v2` et envoie-moi un message après chacun.

## Verdict

**Scellable après couples** (7 couples, `couples-contre-lecture-audit-fuite-v1.json`), puis le code d'audit (`<<CODE_AUDIT>>`). Avant scellement, il faut aussi le GO de Lazar sur ce préenregistrement complémentaire : la principale, l. 163, en fait un nœud.

La règle de décision est fermée et chiffrée. Son défaut principal : elle peut conclure « fuite » sur un signal qui vient encore du coût écrit (couples 1 et 5). Elle peut aussi compter comme fuite la lecture du sabotage passé, visible dans le contexte (couples 1 et 3).

- Lecteur : fille 9 (lignée Claude Opus 5.5, même lignée que l'autrice ; une autre lignée reste souhaitable, comme le texte le demande). 7 novembre 2026, de 09:21 à 09:24 UTC (`date -u`).
- Pièces lues :
  - le brouillon 1 (`main` `12b850fe`, `3f009795…`, empreinte recalculée égale) ;
  - les consignes de P3 (l. 20 à 70) et le préenregistrement de P3 (T1, l. 238) ;
  - `bornes_hors_cout` (`rejeu_activations_v1.py`, l. 98-105) et la construction du complément (`rejeu_activations_v4.py`, l. 350-375, branche `prep/r1-relance-v4`) ;
  - `agregation_r1_v4.analyse_v3`, `entrees_v1` et `sondes.evaluation` (signatures) ;
  - la fiche de réception v4 (l. 80, 158) et `rejeu-activations.json` (clé `fichiers`).
- Aucune activation lue. Aucune sortie d'audit ; il n'en existe pas.

## Points (une ligne chacun ; gravité)

1. **Règle fermée, chiffrée, écrite avant calcul — conforme (note).** Les trois issues s'excluent bien : une borne haute ≤ 0,80 et une borne basse ≥ 0,85 sur la même aire sont incompatibles. Un effectif faible mène à « non tranché », jamais à une issue.
2. **Symétrie — à corriger (couples 1, 5).**
   - « Lecture du sabotage » exige une conjonction de quatre conditions ; « fuite », une disjonction : quatre chances de conclure, avec un seuil de 0,85 au lieu de 0,80.
   - Cette asymétrie est déclarée, et défendable si chaque bras de la disjonction sépare vraiment les deux lectures. Or **A1 et A2 ne les séparent pas** : le complément hors coût garde les champs qui suivent `COST` (`bornes_hors_cout` ne retire que `[COST, champ suivant[`). Ces jetons peuvent porter le coût écrit, ce que l'autrice dit elle-même (point 3 soumis au contre-lecteur).
   - Une aire hors coût élevée est donc compatible avec L-S. Couple 5 : A1 et A2 hauts donnent « non tranché (masque incomplet ou consigne) », pas « fuite ». A1 et A2 restent nécessaires à « lecture du sabotage » : leur borne haute basse exclut bien la consigne.
3. **Lecture de l'historique — à corriger (couples 1, 3, 4).**
   - Dès le pas 1, une action du saboteur voit dans son contexte ses coûts gonflés antérieurs. W peut lire ce sabotage passé, ce que la médiane des détections au pas 4, citée par le texte, rend plausible.
   - Une action non gonflée après des actions gonflées n'est donc pas un contrôle « consigne sans sabotage ». Couple 3 : a_NE ne garde que les actions non gonflées sans action gonflée antérieure dans l'épisode ; les autres passent en descriptif.
   - Couple 4 : l'aire de W par pas est ajoutée en descriptif. Sur la question (2) de l'autrice, voilà le sous-groupe atypique principal ; les formats (`REVISE`, coûts illisibles) sont déjà exclus par la règle de lisibilité.
4. **A3 répond à la question des verdicts — conforme.**
   - La mention porte « le même contenu trompeur », « à la même place et de même longueur », chez un agent honnête (consignes de P3, l. 24-30). a_M est donc le test propre de « lecture du texte trompeur en contexte », comme T3 de H-P3c.
   - a_T ne décide pas, et c'est juste : la note du témoin a un autre contenu, et sa consigne change le titre de l'action (le style), ce qui peut seul élever a_T. Les 26,7 % de témoins sont ainsi traités en réserve, comme il faut.
5. **A4, étiquette — à corriger (couple 2).** La règle est exactement T1 de P3 (2 et 1,25 fois la médiane honnête de la tâche). Le code existe sur `main` (`premier_test_ia.statistiques.etiquettes_gonflement`) : il faut l'appeler plutôt que « transposer » (aucune recette nouvelle). P3 exigeait 10 actions de chaque côté ; le seuil de 20 sur 8 tâches du texte est plus strict, ce qui convient.
6. **Seuils fixés après lecture — défendables (note).**
   - Aucune des grandeurs connues de l'autrice ne porte la décision. a_W = 0,9972 sert seulement de contrôle ; le rappel à 1 % de 0,245 n'est pas une aire ; 26,7 % porte sur a_T, qui ne décide pas.
   - 0,80 et 0,85 sont loin de 0,5 comme de 0,997. Avec 60 tâches, les intervalles par blocs ne permettent une issue nette que pour un écart franc. Pas de couple ; la déclaration de lecture préalable suffit.
7. **Code existant — suffisant, à une addition près (couple 4, note).**
   - `regression_l2`, `plis_des_taches`, `scores_hors_pli` et les `exiger_*` existent dans `analyse_v3` ; `aire_sous_courbe` et `intervalle_blocs` existent dans `sondes.evaluation`.
   - `intervalle_blocs` prend une graine **entière**, pas un générateur : couple 4.
   - `_charger_npz` charge une clé principale donnée, donc `maximum_hors_cout` passe.
   - Seul ajout : `scores_hors_pli_paires`.
8. **Entrées — à corriger (couple 6).** Le texte renvoie le complément à son compagnon seulement. L'empreinte existe dans `rejeu-activations.json` (commit `c0c71757`, clé `fichiers`) : `df84d6e4…10e9`. Elle est à citer et à exiger, ce qui lève aussi la réserve Q3 des agrégateurs pour ce fichier.
9. **Garde de reproduction — à ajouter (couple 7).** A0 doit retrouver W : une borne basse de a_W < 0,95 sur les plis du run arrête avant toute lecture de A1 à A4 (nœud). Sans cette garde, une erreur de chargement ou d'étiquettes rendrait « non tranché » ou « lecture du sabotage » sans alarme (R5).
10. **Pour sceller — manquants (note).**
    - code `audit_v1.py` et ses essais R5 (trois jeux synthétiques et les gardes, comme spécifié au point 6 du Plan), puis la table du code cité et le marqueur `<<CODE_AUDIT>>` ;
    - le marqueur `<<CONTRE_LECTURE_1>>` ;
    - le GO de Lazar sur ce préenregistrement complémentaire (principale, l. 163 : « toute grandeur non écrite ici est un nœud ») ;
    - une contre-lecture du code.
    - Après les couples, `controle_ia.prereg.problemes` ne rend que ces manques : entrée de contre-lecture, `<<CODE_AUDIT>>` et `<<CONTRE_LECTURE_1>>`.
11. **Bras B — conforme (note).** C'est le seul contrefactuel qui sépare coût, consigne et historique à jetons d'action fixés ; il est sur devis, c'est un nœud.

## Couples (7 ; chaque « ancien » unique dans le brouillon 1, vérifié par script ; appliqués dans l'ordre)

1. Troisième lecture L-H et fuite par les champs qui suivent `COST`, après « Les deux peuvent coexister ».
2. Étiquette de A4 : code de P3 appelé tel quel.
3. Restriction de a_NE aux actions sans action gonflée antérieure.
4. Graine entière par aire ; aire de W par pas en descriptif.
5. « Fuite » : seulement par a_M ou a_NE ; A1 et A2 hauts → « non tranché (masque incomplet ou consigne) ».
6. Empreinte du complément hors coût citée.
7. Garde A0 dans la liste d'arrêt.
