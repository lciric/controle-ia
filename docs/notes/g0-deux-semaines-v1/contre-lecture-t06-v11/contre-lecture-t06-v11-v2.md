# Contre-lecture de la v11 de T0.6 — v2 (conclusion à la tête du rendu 4)

Fille 9, contre-lectrice neutre (R2). Écrit le 2026-11-08, de 01:33 à 02:35 UTC (heures relevées par `date -u`). Non scellé ; aucun `.sha256`. Complète la v1 de la même branche, qui reste (R12).

## Message de la mère (recopié mot pour mot)

> **rendu 4 de la fille 10**, la v11 complète : branche `prep/t06-v11`, **tête `2848642e18ab44bf91a6eab9597cb73548631217`**. Elle remplace les têtes des rendus 1 à 3. Conclus ta contre-lecture à cette tête : verdict par pièce, et couples pour l'ordre d'E3 bis.
> **Ce qui a changé depuis ton rendu partiel** :
> - `session_v11` (`c3989859…`) : un identifiant différent de celui demandé est non concluant. Le 404 exact reste une absence établie. 32 essais.
> - Bras B v3 (`3fa8c4c1…`) : 18 mutations tuées sur 18, dont X3 et X8, avec un témoin non muté. La mesure de la tolérance est refaite avec `SeedSequence`. L'addendum brouillon v2 (`08d0bcff…`) applique tes deux couples ; la valeur de 0,15 est inchangée et soumise à Lazar, avec ta recommandation de 0,3.
> - **Liste figée** : refus de `T06_EPUISEMENT_SIMULE_S` éprouvé, doublon d'exclusion détecté, motifs corrigés. Le rapport v2 (`a6303ee1…`) porte « 47 + 3 ».
> - **Amorce et lanceur** :
>   - `TESTS_ARGS` refusé hors du mode jouet ;
>   - plus de variable de total : les épreuves sous GO-2026-11-06-01 (5) et GO-2026-11-07-08 (8), avec les deux lignes vérifiées au registre ;
>   - une dépense antérieure d'au moins 2,092 exigée ;
>   - configuration d'E3 bis v2 (`a20aba78…`, GO-2026-11-07-08, création jusqu'au 11) ;
>   - brouillon d'ordre d'E3 bis v2 (`3c5df576…`).
> - **Empreintes** : amorce v9 `6a6897ce…`, lanceur v11 `e134419b…`, `configuration_v5` `0f75e16f…`, `lanceur_v5` `17efa881…` (inchangé).
> - **Suite ciblée** : 81 fichiers, 1 878 essais, tous verts.
> Vise 60 minutes. E3 bis part dès le scellement de son ordre.

## Qui a lu quoi
- **Code**, delta de `888f4d6e` à `2848642e` : un sous-agent neuf de lignée Opus, qui n'avait lu aucune des pièces. Il a joué 25 mutations à lui, dont 22 sont tuées, et rejoué le banc du bras B v3 (18 sur 18, témoin réussi). Les 12 fichiers d'essais neufs ou modifiés donnent **294 réussis, 0 échec**. **La suite ciblée complète (1 878 essais annoncés) n'a pas été jouée.**
- **Moi** :
  - le brouillon d'ordre d'E3 bis v2 (`3c5df5769d15581becf59bd30a82abf0ad8f00c7155c185e1b8e14be563f3afc`), comparé à la v1 ;
  - la configuration d'E3 bis v2 (`a20aba78…`), comparée à celle d'E3 v5 : seuls `go_id`, `plafond_usd`, `dernier_jour_creation` et `fin_go_utc` changent ;
  - le rapport v2 (`a6303ee1…`, « 47 + 3 » conforme) ;
  - l'addendum v2 (`08d0bcff…`) : il décrit `bras_b_v3.py`, applique les deux couples, et les empreintes de la mesure v2 sont justes (`0bc1f89c…`, `4326bca2…`) ;
  - GO-2026-11-07-08 : présent au registre de `main` (`a20fcd0c`), ce que le sous-agent n'avait pu voir.

## Verdict
**E3 bis peut partir à cette tête, une fois les 6 couples appliqués à l'ordre.** Aucune pièce de code n'est à corriger avant E3 bis. Deux points sont à corriger avant la course : `T06_TESTS_ATTENDUS` non validé, et la vérification de GO-2026-11-06-01 à la création sans essai.

| pièce | verdict | motif |
|---|---|---|
| `session_v11` (`c3989859…`) | **prête** | Un autre identifiant (`{"id":456}`, `{"instances":{"id":456}}`, `[{"id":456}]`, `"456"`, un 404 qui porte 456) est non concluant (`:61-71`). Le 404 exact établit l'absence ; `{"instances":null}`, `[]` et `{}` restent non concluants. C'est bien ce module qui sert en surveillance (lanceur `:89`, `:279`, `:286`). Mutation tuée. |
| Bras B v3 (`3fa8c4c1…`) | **prêt, avec réserve** | La v3 ne diffère de la v2 que par les noms. Les 13 mutations jouées par le sous-agent sont toutes tuées : X3, X8, G7, rangement de la mention, `<`/`≤`, `>`/`≥`, seuil à 0,66. Pas d'issue ni d'aire sur les sorties. **Réserve** : deux mutations survivent, `TOLERANCE_SCORE = 0.2` et `<` au lieu de `≤` sur la tolérance, parce qu'aucun essai ne fixe la valeur ni la borne incluse. Il faut un essai qui fixe la valeur scellée par Lazar et la borne, une fois cette valeur choisie. Faiblesse latente du banc : un filtre `-k` vide (code 5) compterait la mutation comme tuée, mais aucun ne l'est aujourd'hui. |
| Addendum v2 (`08d0bcff…`) | **prêt pour le scellement** | La valeur (0,15 ou 0,3) et la lecture du « sinon » sont soumises à Lazar. |
| Liste figée (81 fichiers) | **prête** | L'empreinte en dur égale la liste. Chaque fichier est listé ou exclu, et les doublons d'exclusion sont détectés (artefact tué). Les exclusions neuves ont un remplaçant listé, qui reprend tous leurs essais. Le refus de `T06_EPUISEMENT_SIMULE_S` est éprouvé (cas sain, et une mutation tuée). |
| Amorce v9 (`6a6897ce…`) | **prête, avec réserve** | `TESTS_ARGS` est refusé hors du mode jouet (`:239`), et elle appelle `bras_b_v3` et `lanceur_v5`. **Réserve, à corriger avant la course** : `T06_TESTS_ATTENDUS` n'est validé nulle part (lanceur `:226`, amorce `:371`). Une valeur comme `7 -e PYTEST_ADDOPTS=…` injecterait des options de pytest. Il faut exiger `^[0-9]*$` au lanceur. Pour E3 bis, l'ordre la fixe vide (couple 6). **28 motifs** de clonage, et non 27 (couple 5). |
| Lanceur v11 (`e134419b…`) | **prêt pour E3 bis si l'ordre porte les couples 3, 4 et 6** | Les deux lignes de GO sont vérifiées au registre passé, et une dépense antérieure ≥ 2,092 est exigée sous 07-08. Contournements refusés : total 8 sans la ligne, dépense de 0 ou 2,091, plafond de 5,81, 07-08 pour la course. Il reste trois défauts : la création est refusée après le 10 novembre, la dépense antérieure peut valoir 0 sous 06-01, et un essai manque. **(a)** La création vérifie que 06-01 est dans son échéance (10 novembre) : le 11 serait refusé, contre la configuration (couples 3 et 4). **Réserve** : sous 06-01 seul, une dépense antérieure de 0 reste acceptée ; c'est sans objet pour E3 bis, qui passe sous 07-08. **Mutation L2 survivante** : la vérification de 06-01 à la création (`:197`) n'a aucun essai, à ajouter avant la course. **(b)** Le « 0 » positionnel est la dépense des tentatives d'E3 bis elle-même ; `T06_DEPENSE_EPREUVES_ANTERIEURES_USD` est sans effet à la création (couple 6). |
| `configuration_v5` (`0f75e16f…`), `lanceur_v5` (`17efa881…`) | **prêts** | Le plafond d'épreuve doit être fini, 0 exclu, au plus 8, et un booléen est refusé. La garde du mode réel est inchangée. Le diff de `lanceur_v5` se limite à la note, l'import et `COMMANDE`. Les vraies configurations (E3 v5, E3 bis v1 et v2, course brouillon 5) sont chargées : la course est acceptée, puis refusée sans préenregistrement pour le bon motif. |
| Configuration d'E3 bis v2 (`a20aba78…`) | **prête** | `dernier_jour_creation` vaut le 11, mais le lanceur interdit le 11 ; l'ordre, plus strict, fait foi (couple 3). La configuration n'a pas besoin d'une v3, puisqu'E3 bis part le 8. |
| Brouillon d'ordre d'E3 bis v2 (`3c5df576…`) | **corriger avant le scellement : 6 couples** | Voir plus bas. Les 3 marqueurs `<<COMMIT_E3BIS>>` sont présents. |
| Rapport v2 (`a6303ee1…`) | **prêt** | « 47 + 3 » appliqué. |

**Forme, R12.** L'amorce v9, le lanceur v11, les deux listes et plusieurs fichiers d'essais ont été modifiés sous le même nom depuis `888f4d6e`, et le rapport v1 a reçu un § 7. Aucune de ces pièces n'était scellée ni n'avait servi sur une carte. Les empreintes citées à la tête du rendu 4 font donc foi. Toute citation antérieure, comme l'amorce v9 `3390ff1e…` dans ma v1, est caduque.

## Couples pour l'ordre d'E3 bis (`couples-ordre-e3bis-v2.json`, 6)
Chaque « ancien » est unique dans le brouillon `3c5df576…`, et les couples sont appliqués dans l'ordre par script :
1. § 0 : « 47 d'environnement… 3 défauts », au lieu de « 46… 4 » ;
2. § 0 : le rapport cité devient la v2, avec son empreinte ;
3. § 1 : création permise jusqu'au **10** novembre, avec le motif (le lanceur refuse le 11) ;
4. § 5 : « aucune création après le 10 novembre » ;
5. étape 4 : `motifs=28` ;
6. étape 3 : sens du « 0 » positionnel (jamais 0 pour une relance) ; `T06_DEPENSE_EPREUVES_ANTERIEURES_USD` sans effet à la création ; `T06_TESTS_ATTENDUS` vide, exactement.

## Réserves reportées à la course
1. Valider `T06_TESTS_ATTENDUS` (`^[0-9]*$`) au lanceur.
2. Ajouter un essai à la vérification de 06-01 à la création (mutation L2).
3. Ajouter un essai qui fixe la valeur scellée de `TOLERANCE_SCORE` et la borne incluse.
4. Rendre le banc du bras B strict sur le code 5 de pytest.
5. Relever la suite ciblée complète sur l'instance à E3 bis : c'est la seule ligne opposable.
