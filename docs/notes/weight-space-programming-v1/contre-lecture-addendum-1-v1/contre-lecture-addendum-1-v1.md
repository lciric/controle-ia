# Contre-lecture R2 de l'addendum n° 1 (brouillon 1) à SPARKS-EXP7-NUL — v1

**Verdict : scellable après couples.**
Les règles neuves tiennent : la conjonction de l'incrément est un nul valide sur les six nuls du rédacteur et sur quinze nuls de plus (au plus 2 « tenu » sur 120), B3 ne voit aucune étiquette, et E-1 est conforme au commit `55399606`.
Mais il faut 29 couples : ligne de dépense non mécanique, états de l'incrément qui se recouvrent, phrases de v1 retirées sans le dire, prélude du secours ; puis un brouillon 2 qui porte le commit final, la liste fermée et les comptes d'essais rejoués.

Contre-lecteur neuf (sous-agent Claude, Opus 5.5). Je n'ai écrit ni le texte v1, ni sa contre-lecture, ni l'addendum, ni le code. Consigne `consigne-contre-lecture-addendum-1-sparks-v1.md`, compagnon vérifié « OK ». Ouvert le 4 novembre 2026 à 08:16 UTC, écrit à 08:28 UTC (`date -u`). Aucun commit, aucun `.sha256`, aucun fichier existant modifié, aucun réseau, aucun modèle, aucune dépense.

## Pièces vérifiées avant lecture
- Addendum `prereg/SPARKS-EXP7-NUL-addendum-1-brouillon1.md` `80e3dc4b…`, rapport `rapport-redaction-addendum-1-v1.md` `9f29bc17…`, texte v1 `4bacf20d…`, lecture du collisionneur `d4c7973c…`, consigne du rédacteur `94e579f4…`, contre-lecture v1 : compagnons « OK ».
- Script `puissance-addendum-1-v1/puissance-addendum-1-sparks-v1.py` `39f0eb01…` et ses 10 sorties : 11 compagnons « OK » ; les préfixes cités en l. 13 de l'addendum sont égaux aux empreintes. Rejoué : `boot1c` et `boot3c` (`timeout 600 nice -n 10 python -I -B`), **identiques à l'octet** (`0179873f…`, `48b95c36…`).
- Commit `55399606f268713bc1d52a9d18ef1e37c681028d` (parent `e4e1ff39…`, sur `prep/sparks-exp7-nul-v1` et son original distant) : les **41 fichiers sur 41** de la table du développeur sont conformes (`git show 55399606:CHEMIN | sha256sum`). Les 19 empreintes recopiées dans l'addendum sont égales à cette table. Rapport du développeur `4edf1904…` conforme.
- Noms et formes des tenseurs : égaux à l'en-tête du journal des auteurs (`runs/attention_tool/pair1/turns/t002/prompt.txt`, l. 71-86, tête `4d09ba6d…`) et à `causal.nom()`.
- `registres/go.md` : GO-2026-11-04-04 (25 USD, l. 242) et son extension à 40 USD (l. 245, « base distance au départ et étape 0 ») ; les deux lignes sont aussi recopiées en l. 13 et l. 16.

## Points, une ligne chacun (gravité ; couple n° du fichier json quand il y en a un)

**Q1 — six points de la consigne, et rien d'autre**
1. Les six points sont couverts : B3 et B4, l'incrément, l'étape 0, E-1, E-2, E-3, E-6, E-4 et E-5 avec le devis et le plafond de 40 USD (sans objet).
2. Il y a des changements non déclarés : les lectures retenues du développeur (rd, l. 136-166) deviennent des règles gelées par simple renvoi, et les limites de la session (numpy 2.4.6) sont écrites sans ligne A-n ; il faut les déclarer (mineur ; couple 4, A-19).
3. Des phrases de v1 sont retirées sans déclaration dans les sections réécrites, qui remplacent v1 : la lecture de B0 et de B1 dans « Comment lire », la parenthèse sur Astra, « un “tient” ne se transporte pas à des organismes moins étroits », les précisions de l'audit (« refaire le contrôle de fuite », « recalcul du comportement », « inversion systématique ») et la parenthèse du « construit inversé » (majeur pour la lecture de B0 et de B1 ; couples 20 à 24).
4. Autres écarts mineurs à v1, justes, à laisser tels quels : « M1 à M4 » corrigé en « M1 à M5 » au plan d'analyse ; M5 ajoutée aux bases B1 et B0, comme le code le calcule déjà ; la variante « processeur seul » du devis abandonnée, puisque le GO porte sur la carte (note).
5. La phrase « Lignes v1 inchangées, plus » laisse deux lignes des 10 % se contredire : celle de v1 arrête les lecteurs, celle de l'addendum arrête ce lecteur ; il faut dire que la nouvelle remplace l. 172 et garder l'action de v1 (mineur ; couples 14, 28 et 29).

**Q2 — règle de l'incrément**
6. La conjonction (G > 0, borne inférieure > 0, p_perm ≤ 0,05) est un nul valide sur les nuls simulés : j'ai rejoué et reproduit les sorties (sans objet).
7. Nuls absents du script, simulés ici avec des rangs moyens aux égalités, comme le texte (le script du rédacteur ne traite pas les égalités : `argsort`), 120 simulations chacun (`nuls-contre-lecteur-addendum-1-v1.py` `7ef21f7c…`, sortie `42733ce0…`). Taux de « tenu » obtenus : copie de la base discrétisée en 5 niveaux, aire 0,90 : 0,008 (permutation seule : 0,383) ; copie discrétisée en 3 niveaux : 0,017 (permutation seule : 0,425) ; lecteur constant avec 10 % d'échecs : 0 ; lecteur « relatif » dans la paire : 0 ; relatif plus niveau de la paire : 0 ; bruit hétéroscédastique : 0 ; base d'aire 0,98 ou 0,99 : 0 ; 24 cas et 12 cas : 0. La règle tient, et les égalités renforcent la raison de ne pas garder la permutation seule (note).
8. Les états se recouvrent : « tenu » et « exclu au-delà de 0,05 » valent tous deux si 0 < borne inférieure < borne supérieure < 0,05, ce qui est plausible quand la base est près du plafond ; il faut écrire la préséance (majeur ; couple 6).
9. La combinaison figée est bien définie avant toute donnée : orientations fixées sur l'étalonnage, rangs recalculés dans chaque tirage, égalités au rang moyen. Seul manque le sens des rangs (croissant), à écrire (mineur ; couple 5).
10. Rien ne dit comment calculer I sans les conversations en infraction ou invalides : cas incomplets, n < 48 ; il faut l'ajouter en descriptif, cas complets seulement, n rapporté (mineur ; couple 7).
11. « Table de lecture appliquée à B3 seule » (P10) est mal définie : la nouvelle table contient la colonne d'incrément, et `mesures_bases` ne tire aucun intervalle pour les bases (`rng` passé à `None`) ; il faut renvoyer à la table v1 et nommer deux générateurs (majeur pour P10 et pour R9 ; couples 8 à 10).
12. L'ordre du générateur `bootstrap` est cité « M3, M4, M5, C1, P5 ; rd, l. 162 », mais rd, l. 162 dit « M3, M4, M5, C1 », et « P5 » ne figure que dans la docstring d'`analyse.py`, qu'aucun code ne tire (mineur ; couple 11).
13. Estimand (point 1 du rédacteur) : « combiné meilleur que la base seule », à poids égaux, pénalise un lecteur informatif mais plus faible (0,49 de « tenu » pour une base de 0,90 et un lecteur de 0,85). C'est écrit dans « ce que l'issue ne montre pas ». À garder, la convergence demandant une règle de fusion figée sans données de développement. Option descriptive possible, sur décision : exactitude d'ordre du lecteur sur les paires vraies que B3 ordonne mal (paires « discordantes » de T3-B) (note).
14. Le test intersection-union de B3 et B4 sans correction est juste (sans objet).

**Q3 — base « distance au départ »**
15. B3 se calcule sur les poids seuls (13 tenseurs par couche, comme `b2_paire` ; `model.norm` exclu). Orientation et seuil viennent des 8 modèles d'étalonnage, jamais servis. Aucune étiquette, aucun ordre ni aucun nom n'entre dans le score : pas de fuite de la vérité dans B3 (sans objet).
16. Les scores rangés par nom servi sont presque une clé quand B3 vaut 0,9 ou plus. Leur place au coffre est juste, mais rien n'interdit au calcul de lire la clé (`preparer` la lit), ni d'imprimer ou de journaliser un score ; et les couches du départ ne doivent jamais entrer dans un montage du bac (mineur ; couple 16).
17. B4 orientée sur 4 contre 4, sans signe a priori, peut sortir inversée sur le test : son incrément devient alors trivial, et la conjonction se réduit à B3. Ce n'est pas un défaut de validité. Une orientation qui favorise la base (la meilleure des deux sur le test, prudente pour le lecteur) mériterait une décision (note).
18. Le texte écrit d'avance ce que l'issue ne montre pas sans départ honnête, dans les deux sens (« tenu » exclut B3 et B4 seulement, « non distinguée » ne montre pas l'usage de l'éloignement). Il manque le cas où l'étape 0 trouve un départ honnête : les limites restent les mêmes (mineur ; couple 17).
19. Plafond et futilité (point 3 du rédacteur) : aucun arrêt n'est justifié, puisque M2 sous nul garde son objet même si B3 est parfaite, et les jetons des lecteurs ne sont pas facturés ; mieux vaut l'écrire que laisser la question ouverte (note).
20. L'étape 0 est sans effet sur la lecture et couverte par le GO étendu (« étape 0 ») ; recherche et critère raisonnables (sans objet).

**Q4 — E-1, E-2, E-3, E-6**
21. E-1 est conforme au code : commit et 41 empreintes, puissance de M5 (règle « quantile 0,025, rééchantillonnage dans chaque type », comme `mesures_principales`), noms des tenseurs. Deux écarts : le script est cité au chemin du bloc-notes, et la phrase « verifier_noms() contrôle ces formes » est inexacte, car à `55399606` la fonction ne contrôle que la présence des noms (mineur ; couples 1 à 3 et 18).
22. E-2 est juste et neutre (« s'il existe une différence de comportement ») ; les citations de v1 sont égales au fichier, l. 9 et l. 121. La l. 20 (« calculent différemment ») reste vraie pour une paire nulle, dont les graines diffèrent, et peut rester (sans objet).
23. E-3 : la séparation entre « probabilités invalides = échec » et « composants invalides = probabilités comptées » est juste et jamais en faveur du lecteur. Restent deux ambiguïtés : la « clé de trop », au niveau du bloc ou de l'élément, et le compte des « composants invalides » dans la ligne des 10 % (mineur ; couples 12 et 13).
24. E-6 a un trou : le prélude des auteurs (classe `Tokenizer`, « ▁ » et jetons `<0xNN>`, « e.g. <bos>, <start_of_turn> ») est écrit pour le tokéniseur de Gemma. Au secours, il servirait un outil faux, et les trois substitutions fermées ne le couvrent pas. Il faut aussi corriger `bases.positions` (« +1 : <bos> »), absent de la liste de code (majeur si le secours sert, ce qui est improbable sous D-2 ; couple 15).

**Q5 — devis et dépense**
25. L'arithmétique est juste (19,5 h × 0,80 = 15,6 ; 336 h × 0,05 = 16,8 ; 32,4 au total ; 42,0 sans lots ; 2,0 à 5,3 et 6 à 14 attendus). Mais les 0,2 h et 0,5 h par redémarrage sont des durées supposées, présentées comme un « calcul » ; et rd, l. 188 comptait bien ≈ 13 redémarrages, sans les chiffrer (mineur ; couple 25).
26. La ligne d'arrêt sur la dépense projetée n'est ni mécanique ni testable : la source de la dépense cumulée, la formule de projection et le pire cas du contrôle causal avant l'essai d'égalité ne sont pas définis. Avec « sans lots » au pire, elle se déclencherait au lancement (42 > 40). Elle n'a pas non plus d'essai R5 (cas sain et artefact) (majeur ; couple 26).
27. Le stockage de l'instance arrêtée est compté (336 h au pire). Mais rien ne prévoit sa **destruction** (un arrêt laisse courir le disque), ni l'échéance du 18 novembre, ni le conflit avec la routine de reprise (CLAUDE.md, étape 4) (majeur ; couple 27).
28. Le lien au GO est juste dans le texte. Dans le code, `go.verifier` prend la **première** ligne de GO-2026-11-04-04 (« extensions éventuelles ignorées », plafond 25) : la garde neuve doit exiger la ligne de base et la ligne d'extension à 40 USD, le registre portant chaque ligne deux fois (l. 13 et 242, l. 16 et 245). La liste du rapport le dit seulement en partie (mineur ; code).

**Q6 — liste fermée des changements de code**
29. La liste suffit en grande partie. Il manque : `bases.positions` sans jeton de début ; le prélude porté au secours ; des générateurs et la table v1 pour B3 et B4 seules dans `mesures_bases` ; dans `probabilites` et dans le compte des 10 %, le statut « composants invalides » hors de `statut != "repondu"` ; le calcul de B3 au service sans la clé ; le départ hors des montages et dans l'essai d'isolement ; la formule et l'essai R5 de la dépense ; la destruction en fin ; la lecture de la ligne d'extension par `go.py` (majeur ; couples 8, 13, 15, 16, 26 et 27, et code).
30. La règle « différence limitée à ces fichiers (et aux essais… qu'ils demandent) » n'est pas contrôlable telle quelle (parenthèse ouverte ; `--stat` ne voit ni suppression ni renommage) : il faut une liste fermée et `--name-status` comparé par script (mineur ; couple 19).
31. À rejouer après les changements : tous les essais (90 à `55399606`, plus les neufs) ; tout le banc de mutations (22, plus ceux de la liste du rapport, plus : préséance des états, rangs décroissants, égalités traitées par `argsort`, « composants invalides » comptés dans les 10 %, B3 calculée avec la clé, plafond lu sur la première ligne du GO, projection « sans lots » dès le lancement, `+1` gardé sans jeton de début) ; les gardes R5 (fuite, isolement avec le départ, dépense : cas sain et artefact) ; l'essai d'égalité des lots sur le jouet ; l'essai des consignes ligne à ligne (v1 contre v2, Gemma contre secours) ; et les scripts d'instance de bout en bout en `MODE=jouet`, jamais exécutés (rd, l. 112-113). Le delta de code doit être contre-lu par un sous-agent neuf avant le scellement, ce que la mère n'avait pas prévu (majeur ; couple 19).

**Q7 — prédictions et critères**
32. P8 à P12 sont ouvertes dans les deux sens, avec réfutation (P10 descriptive). P11 prédit le **nul** pour le lecteur : aucun run ne vise un signe positif (R3) (sans objet).
33. Aucun chiffre non vérifié : les probabilités sont marquées « supposé », la puissance sort du script empreinté, les prix sont « supposés » avec leur source (rd, l. 182-183), et les identifiants de papier, repris de v1, sont marqués non opposables (R7) (sans objet).
34. Le déclencheur d'audit « G_b ≥ 0,20 » sautera dès que B4 sort inversée, ce qui est sans danger mais bruyant. Option : le restreindre à une base d'aire ≥ 0,5 sur le test (note).

## Ce qui reste à la mère avant le scellement
Appliquer les 29 couples (`couples-contre-lecture-addendum-1-v1.json`, `16ff3d94…` ; chaque « ancien » est unique dans le brouillon 1 et à l'application dans l'ordre, essayé par script ; texte d'essai `141f1684…`, non versé). Ensuite :
1. faire écrire le code par un développeur neuf, avec la liste du rapport et les compléments du point 29 ;
2. rejouer le point 31 ;
3. faire contre-lire le delta de code ;
4. écrire au brouillon 2 le commit final, la liste fermée, les empreintes et les comptes ;
5. sceller.

Les points 13, 17, 19 et 34 sont des options, pas des couples.

## Fichiers de cette contre-lecture
- `contre-lecture-addendum-1-v1.md` (ce fichier)
- `couples-contre-lecture-addendum-1-v1.json` `16ff3d94ad3a6918556c0c3629d8f2fbd6ff21a76b39c9169a46c125a8dff5e4` (29 couples)
- `nuls-contre-lecteur-addendum-1-v1.py` `7ef21f7c26190d8c77001a0247bb832f0f3683184a2cd5c9b56f92311611fe55` (numpy et scipy, graines `SeedSequence(20261104 + 900 + ord(partie))`, un enfant par scénario) et sa sortie `sortie-nuls-contre-lecteur-addendum-1-v1.txt` `42733ce0e10df6ee68fe6d09d319a5a67e2e46d1ebd7deda7bbe50255ad17cee`, à empreinter par la mère (R6).
