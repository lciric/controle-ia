# Contrôle de conformité R2 — axe 6, texte II, bras « avec pistes » — v8 contre v7

- Date : 30 octobre 2026, 7 h 55 UTC (`date -u` : Fri Oct 30 07:52 UTC 2026 au premier contrôle).
- Contre-lecteur : sous-agent Claude, modèle Sonnet 5.5 (`claude-sonnet-5-5`). **Neuf** : n'a écrit aucune pièce, n'a lu aucun moniteur.
- Pièces lues, et rien d'autre : la v7 (`908abd79147091f34eafbaee55634a44ee5d9a06e8883663c6c2acc853774c15`, recalculée par `git show … | sha256sum`, égale), la v8 (`3f16fec37cd2a43503059b1dbb9e2538b7bb292ca7bae206655fc3de60526dfa`, recalculée, égale), la contre-lecture de la v7 (constats CA6P7-01 à 06 et restes de CA6-V2-01, 05, 06). Lues sur `origin/donnees/course-2-axe-6-v1` par `git show`. Aucune autre branche. Le fichier des listes closes (`08e391c9…`) et la liste lexicale n'ont pas été ouverts.
- Ce rapport va sur `main` : il ne recopie aucune piste ; il ne cite que des numéros de ligne de la v8 et des catégories.
- Déclaration : ayant lu les pistes, ce contre-lecteur ne peut être ni lecteur tenu à l'écart des sorties de ce bras, ni rédacteur de ses témoins.

## Verdict
**Conforme, servable** (réserves mineures ci-dessous, aucune ne bloque ; restent à faire avant service l'épreuve du contrôle lexical, le devis et le GO, comme la v8 le dit ligne 33).

## Mesure (critère 4)
Texte servi (marqueurs lignes 37 et 153, lignes 38 à 152) : **11 291 caractères** (`LC_ALL=C.UTF-8 wc -m`, décompte Python identique) ; la v7 : 11 042 ; écart +249. L'en-tête (ligne 35) est exact : 11 291, 11 042, 10 356 (la valeur de la v6 n'est pas recalculée ici).

## Table de conformité

| Constat | Lignes de la v8 | Appliqué | Commentaire |
|---|---|---|---|
| CA6P7-01 protocole des deux bras | 176 à 181 ; table 22 | **oui** | Les cinq points demandés sont écrits : attribution (deux sous-sessions neuves, au plus deux fiches par bras, une génération numérotée une fois, étiquette portée par la fiche), comptage par bras, mort par bras (bras sans pistes seul décisif, bras avec pistes lu à part), mesure de l'ancrage par le lecteur tenu à l'écart et scellée sur la branche des sorties, compte par bras vers la défense = nœud pour Lazar. Conforme à la recommandation. Voir CA6C8-03. |
| CA6P7-02 piste sur S | 101 | **oui** | Réécrite comme propriété du problème de test (loi de référence, classe d'alternatives invariantes sous un groupe agissant sur les suites) ; aucune propriété de S ; n'appelle plus de condition portant sur S (contraste avec lignes 70 du texte servi et K2). |
| CA6P7-03 notation et lecture double | 51, 99 | **oui, par variante** | h_t défini (ligne 51) ; la ligne 99 nomme une classe de déplacements (« déplacement de la moyenne »), plus une forme d'agrégation. Le rapport proposait de retirer la piste ou de dire « à travers les actions » ; la v8 choisit de définir l'objet et de qualifier en déplacement : cela règle les défauts (1) et (2) ; pour (3), la formule ne dit toujours pas si la moyenne est prise dans ou à travers les actions, mais, portant sur la loi (espérance), elle ne construit pas une statistique. Acceptable. |
| CA6P7-04 contrôle lexical | 182 | **oui** | Le programme est appliqué aux lignes du matériau avant service, seul le résultat est scellé, renvoi en réécriture si signalement. Ligne 33 en fait une tâche avant service. Épreuve non encore faite. |
| CA6P7-05 hors-texte | 158, 160, 165 | **oui** | Ligne 160 : « ni la v7, ni la v8 », avec la précision sur les témoins écrits sur la v6. Ligne 165 : branche portant v2, v7 et v8. Ligne 158 : classes classiques renvoyées au fichier scellé (`08e391c9…`, même empreinte que la v7). |
| CA6P7-06 objet | 107, 98 | **oui** | Ligne 107 : combinaisons de classes de déplacements, statistique jointe renvoyée au champ (e) ; ligne 98 : intitulé « classes de déplacements ». |
| CA6-V2-01 reste | 176 à 181 | **oui** | Voir CA6P7-01. |
| CA6-V2-05 reste | 100 | **oui** | Sous-classe définie par la loi limite de la statistique ; régime diffus et δ → 0 quand T → ∞ dits. Voir CA6C8-02. |
| CA6-V2-06 reste | 101, 103, 25 | **oui** (option « retirer les noms ») | Plus aucun nom d'auteur dans le texte servi (principe d'invariance, Hunt-Stein, Ingster, Donoho et Jin retirés). Voir CA6C8-01 pour une trace périmée dans l'en-tête. |

## Critère 2 — chaque bloc du `diff`
Texte servi : sept lignes changées (quatorze lignes de `diff`, v7 et v8) ; neuf blocs au total avec le hors-texte ; tous justifiés :
- ligne 1 (titre, v7 → v8) : numéro de version ;
- ligne 6 : ajout de la ligne « v8 » à la provenance ;
- lignes 21 à 35 (remplacent v7 20 à 22) : table des constats, À faire avant service, lecture des sorties (v8 ajoutée à la liste d'exclusion de lecture, cohérent), mesure ; justifiés ;
- ligne 51 : définition de h_t (CA6P7-03) ;
- lignes 98 à 101 : intitulé, trois lignes de matériau (CA6P7-02, 03, 06 ; CA6-V2-05) ;
- ligne 103 : retrait des noms d'auteurs (CA6-V2-06) ;
- ligne 107 : dernière piste précisée (CA6P7-06) ;
- lignes 158, 160, 165 : trois mises à jour du hors-texte (CA6P7-05) ;
- lignes 176 à 182 : protocole des deux bras et contrôle lexical sur les pistes.
Aucun bloc non justifié, aucune suppression collatérale.

## Critère 3 — texte servi intact, exposition à un filtre
- Seules sept lignes du texte servi changent (51, 98, 99, 100, 101, 103, 107). Garde, notation hors ligne 51, contraintes sur la classe de statistiques, rubriques de la fiche, K1 à K6, déroulé et critère de mort : **intacts** (aucune ligne de ces zones dans le `diff`).
- Formulations nouvelles : vocabulaire purement statistique (« problème de test invariant », « groupe agissant sur les suites », « loi limite », « statistique spécialisée », « statistique jointe »). Aucune n'est un nom de mode ni un procédé ; non vérifiable ici contre la liste lexicale (non ouverte). L'épreuve avant service (ligne 182) est le contrôle approprié ; CA6C8-04 propose d'y faire passer deux mots.
- Aucun impératif, aucune intention prêtée, aucune mention d'un système qui produit des textes dans les lignes changées.

## Constats nouveaux

### CA6C8-01 — Table de l'en-tête périmée (mineur)
- Lignes : 15 et 16, contre 25.
- Défaut : la table héritée de la v7 dit encore, pour CA6-V2-05 et 06, le traitement de la v7 (références nommées, restriction au premier moment) ; le texte servi de la v8 ne les porte plus. La table de la v8 (lignes 24, 25) les remplace, mais les deux tables coexistent sans mention de l'une qui supplante l'autre.
- Correction proposée : ajouter « remplacé par la v8 » aux deux lignes, ou n'y rien changer (hors texte servi, sans effet de sûreté). Peut attendre la v9.

### CA6C8-02 — δ fixé contre δ → 0 (mineur)
- Lignes : 100, contre 49 (« indiscernable au niveau α »).
- Défaut : la notation fait de δ une constante fixée par la fiche ; la ligne 100 le fait tendre vers 0 quand T croît. Les deux se concilient (δ peut dépendre de T), mais la notation ne le dit pas.
- Correction proposée : à la prochaine version servie, écrire « δ fixé par la fiche, éventuellement fonction de T ». Sans urgence : la ligne 100 est du matériau sans effet sur la notation.

### CA6C8-03 — Protocole : deux silences (mineur)
- Lignes : 176 à 181.
- Défaut : (1) l'étiquette de bras est portée par la fiche mais le juge et le lecteur figé ne la voient pas : le texte ne dit pas qui la retire ni qui compte par bras (le lecteur tenu à l'écart, vraisemblablement) ; (2) les mêmes témoins étant glissés dans les deux bras, un témoin vu deux fois par le juge peut lever l'aveugle sur les bras. Le texte servi (critère de mort, « moins de 2 fiches de la génération ») parle de la génération, la mort s'applique par bras selon le hors-texte : sans contradiction (le texte servi n'est pas appliqué par le proposeur), mais à consigner.
- Correction proposée : consigner dans le devis qui retire l'étiquette ; décider si les témoins sont dédoublés par une reformulation neutre ou présentés dans un lot commun unique. Aucun changement du texte servi.

### CA6C8-04 — Mots à passer à l'épreuve lexicale (mineur)
- Lignes : 100, 107.
- Défaut : « spécialisée » et « jointe » (ligne 107) sont des mots proches du vocabulaire du programme (bras génériques et spécialisés) ; ils peuvent déclencher le contrôle lexical selon ce que contient la liste, que ce contre-lecteur n'a pas lue.
- Correction proposée : s'assurer que l'épreuve de la ligne 182 couvre ces deux mots ; en cas de signalement, utiliser « d'un seul type » et « combinée ».

## Décompte
- Constats de la contre-lecture de la v7 : appliqués 9 sur 9 (CA6P7-01 à 06, restes de CA6-V2-01, 05, 06) ; partiellement 0 ; non 0 ; CA6P7-03 par variante acceptable.
- Constats nouveaux : bloquant 0 ; majeur 0 ; mineur 4 (CA6C8-01 à 04).
- Rien de nuisible ajouté : aucune formulation ajoutée ne construit un procédé, ne nomme un composant ou une forme de statistique, ni n'affecte la notabilité.
- Prochaines actions (hors texte) : épreuve du contrôle lexical sur les lignes 98 à 107, devis, GO.
