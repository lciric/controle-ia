# Contre-lecture neuve (R2) du préenregistrement « agrégateurs sur les scores réels de R1 v4 » et de son code — v1

**Verdict : scellable après couples** (14 couples, `couples-contre-lecture-agregation-r1-v4-v1.json`) et corrections de code, liste à part (avant la commande décisive).
Opposabilité tenue : aucune grandeur des sorties de R1 ou R2 dans le texte, le code, les essais ni la simulation.
La simulation se reproduit à l'octet, les 25 essais passent, et les extraits des trois textes scellés concordent avec `main`.

## Lecteurs et ce qu'ils ont lu

- **Lecteur 1** : fille 9, session de contre-lectures, lignée **Claude Opus 5.5**, même modèle que l'autrice (réserve déclarée par la consigne). 6 novembre 2026, de 12:21 à 12:28 UTC (`date -u`).
  - Consigne : `docs/notes/g0-deux-semaines-v1/consigne-contre-lecture-agregation-r1-v4-v1.md` (`c230cd3f5c26ffdf…`, compagnon vérifié, `main` `8b14b298`).
  - Il a lu : le brouillon 1 (`b6d5cdc6…`, commit `361a2308`) ; le rapport (`2006bcbb…`) ; le module et ses essais ; la simulation et sa sortie (`531166428bc4…`) ; la lecture préparatoire (`9feb038a…`) ; les trois analyses scellées et l'addendum sur `main` (empreintes égales à celles citées) ; `registres/go.md` de `main`, l. 259.
- **Lecteur 2**, seconde lecture ciblée (points 2, 3 et 7) : sous-agent neuf, lignée **Claude Sonnet**, qui n'a écrit ni lu aucune pièce de l'autrice avant cette lecture.
  - Il a lu : le brouillon, le rapport, la simulation, le module, `sondes/evaluation.py`, la note mathématique v3 (`dfe4fe0f…`, lue dans l'arbre principal, l'arbre de lecture ne la portant pas), le préenregistrement de T0.3 et les consignes de P3, l. 25 à 50.
  - Ses constats A1 à A4, B1 à B6 et C1 à C3 sont repris ci-dessous ; je les ai vérifiés sur le code (B1, B3) et sur la sortie de la simulation (B2).
- Ce que ni l'un ni l'autre n'a lu : aucune sortie de R1 ou R2, rien sous `runs/` (hors noms), `diag/` ni `donnees/`, ni la branche `analyses-r1-v4`, ni le canal. Aucun `.sha256`, aucune clé, aucune dépense. Les dossiers temporaires d'essai sont supprimés.

## Points (une ligne chacun ; gravité)

1. **Opposabilité — conforme (note).**
   - Ce que le texte déclare avoir lu est exact, sur le commit `a338caed` de `main`. La lecture préparatoire ne porte, des courses v3 et v4, que des noms de manifestes et la mention « lues et jugées », sans aucune valeur.
   - Les seuls nombres réels du texte sont les aires publiées de P3 (0,5248 et 0,5748, verdict P3 v2), le coût médian 8 400 contre 200 (P3, par le texte parent), le taux de 97 % (addendum v4, un seuil) et l'empreinte de `scores-p3.npz` (fiche v4).
   - Rien dans le code, les essais ni la simulation ne porte une grandeur des analyses.
   - Le texte dit avoir cité les analyses sans les lire. Je les ai confrontées sur `main` : les recettes, les paramètres (k = 0,5, ρ = 0,5, w = 3, l. 110), `(i) − i_max` (l. 122), l'exclusion (l. 57) et les membres de la famille concordent.
2. **Théorie — à corriger (couples 1 à 4).**
   - La classe M dense est fixée par la construction (consignes de P3, l. 29 à 45, « for every proposal », rappel à chaque pas). Mais δ_k ≥ 0 est une hypothèse sur les scores, pas un fait de la construction (couple 1).
   - Le passage de « budget fixé, puissance à α » à « décalage fixé, aire sous la courbe » n'est pas un énoncé de la note v3 ni de T0.3 (P1-P2, n₀ = 200) : l'ordre « somme ≥ maximum en dense » vient de la simulation seule (couple 2).
   - Le renversement à m = 1 est fidèle à L1-L2.
   - Les hybrides sont légitimes comme construction de classe M, mais leurs limites doivent figurer dans « ce que ce texte ne teste pas » (couple 3) : l'action saboteuse a été écrite sous l'historique du saboteur ; 9 actions sur 10 sont partagées avec l'épisode honnête.
   - Un C3 confirmé ne sépare pas la classe M d'une dépendance intra-épisode propre au saboteur (couple 4).
3. **Statistique — à corriger (couples 5, 6, 8, 9, 10) ; simulation reproduite.**
   - Rejouée (`timeout 900 nice -n 10`, 12:24 → 12:26 UTC) : sortie **identique à l'octet** à `…-puissance.json`.
   - La table et les puissances citées concordent : C3 0,98 à a = 0,75 et 0,43 à 0,65 ; C2 0,48 à 0,85 et 1,00 à 0,95 ; contraste positif dans les 28 cellules.
   - Ce qui est bien en place : C3 calculé sur le même tirage de tâches ; Holm avec p = 1 pour un test écarté ; gardes écrites d'avance, sans chemin bifurquant (le seuil a_W est mesuré, mais la règle est fixée).
   - Défauts :
     - les plages annoncées ne correspondent pas aux zones où la garde laisse le test confirmatoire (couples 5 et 6) ;
     - la table des issues a un trou : un intervalle entièrement du côté prédit sans rejet de Holm (couple 8, conforme au code `lire`) ;
     - « C2 confirmé, C3 non concluant : appui partiel » contredit la règle et `lire_hag` (couple 9) ;
     - la borne d'union, non vérifiable sur des textes qui décident par intervalles, ne vaut qu'à titre d'information (couple 10).
4. **Famille et redondance — à corriger (couple 13).**
   - Le texte ne re-prédit rien de ce que lisent les trois analyses : ni W − G, W − J, W − T, ni `(i) − i_max`, ni P-E6. La secondaire calcule `somme_terminale` et `max` sans les comparer, et ne fabrique pas d'hybrides.
   - Le bras « moyenne » `Wm` reste un diagnostic (N-026), jamais une sonde de production ; la moyenne sur les actions (axe (c)) n'est pas visée par la règle gelée 1.
   - Mais la lecture par épisode (l. 133) et la principale (l. 167) interdisent de les relire « avec une autre agrégation (somme brute, moyenne, maximum) ». Le texte doit dire qu'il n'en est pas une relecture et que ses issues ne les qualifient jamais (couple 13).
5. **Code — à corriger (corrections Q1 à Q5 ; couples 11 et 12).**
   - Rejoué : **25 passed** en 86,23 s (`--basetemp` propre, supprimé).
   - Ce qui est en place : formats exacts de la fiche v4 ; une seule commande ; manifeste décisif (préenregistrement scellé exigé, arbre propre, refus d'écraser par `creer_manifeste` et `ecrire_resultat`) ; empreintes relues après chargement.
   - Ce qui manque :
     - (a) aucune vérification de la liste fermée du code contre le texte, que la principale fait par `exiger_code_cite` ;
     - (b) chemin du préenregistrement non imposé ;
     - (c) empreinte de `scores-p3.npz` (`968414fc…`, citée par le texte) non exigée ;
     - (d) aucune garde de second passage, alors que le texte dit « une seule fois » ;
     - (e) l'essai de la commande décisive dit « refus sans prereg » sans l'éprouver : aucun artefact pour « non scellé » ni « arbre sale » (R5).
   - La recette de W diffère de la principale (10 plis au lieu de 5 ; `gtol` et nombre d'itérations ; plancher de l'écart type). L'écart n'est ni justifié ni nécessaire : écrire l'écart exact (couple 11), ou mieux, aligner sur la recette de la principale (Q5).
   - La non-convergence arrête la commande unique : relance soumise à un nœud (couple 12).
6. **R4, R7, R8 — conformes (note), avec le couple 7.**
   - L'audit de symétrie est écrit d'avance : réfuté, |contraste| > 0,35, aire de 1,000 partout, a_W ≥ 0,999, |moyenne − somme| > 0,02.
   - Aucun chiffre de l'état de l'art n'est repris. L'antériorité renvoie à la note v3, section 8, lue sur PDF avec pages citées. La zone non trouvée est dite « une question, pas un trou » (R8).
   - Reste ce qu'on dit au plafond (couple 7).
7. **Ce qui peut rendre l'issue non interprétable — à corriger (couple 7).**
   - Pour un organisme flagrant, a_W est attendu au plafond : la principale prévoit « W parfaite » (Q6), et la secondaire une aire de (i) ≥ 0,97.
   - À a_W ≥ 0,95, Δ(10) ≈ 0 et C3 ne dit plus que Δ(1) < 0. La phrase gelée « l'avantage de la somme décroît » serait alors littéralement vraie sans aucun avantage mesuré en dense.
   - À a_W ≥ 0,999, la garde borne a_W à 0,995 et la simulation gaussienne n'est plus représentative.
   - Conduite écrite par le couple 7 : « appuyée à m = 1 seulement » au plafond ; « non interprétable (plafond ou fuite) » à a_W ≥ 0,999 tant que l'audit R4 n'a pas conclu.
   - Notes : la simulation suppose un décalage uniforme sur les dix actions, ce qui rend la garde optimiste. La garde « signal présent » de C3 ne regarde que les épisodes naturels. Le couple 14 relit le GO dans `registres/go.md` (l. 259).
