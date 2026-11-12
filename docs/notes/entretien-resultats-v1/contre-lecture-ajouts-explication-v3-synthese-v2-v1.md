# Contre-lecture des ajouts : explication v3 et synthèse v2

**Verdict : fidèle avec corrections.** La liste « ce qui manque » est identique mot pour mot à la source dans les deux documents. Aucun résultat de la mesure unanime n'apparaît. Restent quelques écarts d'état, de cohérence et de formulation, listés ci-dessous.

## Empreintes vérifiées (sha256)
Les sept empreintes fournies concordent : source edb0bf03, explication v2 a382d02d, v3 01a39935, synthèse v1 b46f02b1, v2 e460995b, PDF explication 84cf5e77, PDF synthèse a73987c5.

## Changements exhaustifs (diff, lignes coupées)
- Explication v2 vers v3 : en-tête et statut (version 3) ; encadré « Changements depuis la version 2 » ; insertion de la liste (titre, ouverture, priorités, tableau de 11 lignes, sources, ligne de renvoi) ; passages de la mesure unanime en section 3.6, tableau 4.2, section 4.6 (4 pastilles), 7.1 et limites finales ; réserve sur 0,783 en 6.1 (cellule et renvois de sources) ; ajout du dépôt à 167 fichiers en 6.1 ; six lignes ajoutées au tableau des pièces (trois passations, la liste, la contre-lecture du registre des prédictions, le verdict T0.4 v2).
- Synthèse v1 vers v2 : en-tête ; encadré « État au 10 novembre, 11 h UTC » (5 points) ; insertion de la liste ; sept lignes ajoutées au tableau des pièces. Rien d'autre.

## Table des écarts
| Document | Passage | Écrit | Attendu | Gravité |
|---|---|---|---|---|
| Synthèse v2 | encadré, point 4 « Bras d'attaque » (session attaquant informé, règle du bras 88418df0, courriel Bailey prêt, « ton geste ») | présent | Ajout non annoncé dans l'objet (ni liste, ni mesure unanime, ni dépôt, ni calibration) ; absent de l'explication v3. Il faut le déclarer comme ajout ou le retirer ; faits non vérifiables ici | moyenne |
| Synthèse v2 | encadré, point 1 (verdict T0.3 « confirmé avec réserves ») | présent | Même remarque : mise à jour d'état hors du périmètre annoncé, absente de l'explication v3 (incohérence entre documents) | moyenne |
| Synthèse v2 | cellules anciennes inchangées : « verdict formel … en cours » (l. 88, 417, 701, 764-766 du HTML) ; « Version 15 en cours » (l. 95, 743) ; « Version 14 non scellé ; v15 en cours » (l. 982) | texte périmé | Mises à jour ou renvoi explicite ; l'encadré dit seulement « prime » et ne cite pas les cellules de la mesure unanime (il cite les sections 0, 2 et 5 pour T0.3 seulement) | moyenne |
| Synthèse v2 | cellule du tableau de calibration (l. 725) : « 60 tranchées sur 235 : 47 confirmées, 5 réfutées, 8 non concluantes » | chiffres bruts sans réserve dans la cellule | Ces comptes viennent de la même table jugée trop favorable ; la réserve n'est que dans l'encadré. Ajouter la réserve dans la cellule | moyenne |
| Explication v3 et synthèse v2 | encadrés : « la table automatique (0,783) » | taux cité comme chiffre, avec avertissement | Le taux n'est pas présenté comme acquis (« Ne pas citer tel quel »), donc toléré ; préférable de ne pas répéter le chiffre. 0,857 absent | mineure |
| Explication v3 | 6.1, cellule calibration : « issues mal attribuées qui gonflent les confirmations » ; « L'audit de fuite est compté confirmé alors qu'il ne pariait aucun signe ; trois prédictions de B1 occupent cinq lignes ; … verdict v2 dit non prouvé » | affirmations détaillées | Non vérifiables ici (voir liste ci-dessous). « gonflent » affirme un sens avant la fin du recompte | mineure |
| Explication v3 | en-tête : « liste … et quatre mises à jour d'état » | quatre | L'encadré compte une liste et trois mises à jour (mesure unanime, calibration, dépôt) ; à corriger en « trois » ou à compter autrement | mineure |
| Explication v3 | statut : v2 « puis contrôlée « fidèle en l'état » » | affirmation | Aucune pièce fournie ne la porte | mineure |
| Explication v3 | encadré, point 2 : « Sections 3.6, 4.2, 4.6 et 7.1 mises à jour » | liste de sections | Les sections 6.1 et la liste des limites ont aussi changé (6.1 est citée aux points 3 et 4) ; liste incomplète | mineure |
| Explication v3 (PDF) | tableau des pièces | chemins et empreintes tronqués dans les cellules | Défaut d'affichage du PDF qui touche aussi les anciennes lignes ; pas un écart de contenu | mineure |

## À vérifier par la session-dépôt (phrases exactes)
- « la course est finie (10:01:43 → 10:33:16 UTC, code de sortie 0) » ; « Elle a couru une seule fois, de 10:01:43 à 10:33:16 UTC, avec le code de sortie 0 » (passation 10:36, l. 6).
- « Son verdict est prononcé par un lecteur neuf et scellé (7d19704d…) » (passation 10:46, l. 11-12).
- « datée à son tour, avec 167 fichiers, le 10 novembre à 10:32:17 UTC » ; « 164 fichiers à 09:44:58, puis 167 à 10:32:17 UTC » ; « Le projet reste privé et non figé ».
- « version 15 … scellée (3a1651f4…) et datée chez le tiers à 09:44:58 UTC ».
- « mot relayé par la mère à 10:46 UTC » ; « main 983dd664 » ; « vers 11:10 UTC ».
- « le verdict formel du lecteur neuf est prononcé, « T0.3 : confirmé avec réserves » » (verdict T0.3 v1, l. 10), et « sections 0, 2 et 5 ».
- « la session « attaquant informé » existe et a scellé la règle du bras (88418df0…) » ; « le courriel aux auteurs est prêt » ; note 1050, branche claude/compassionate-meitner-d4ryyk, commit a1bd02c9.
- Calibration : « L'audit de fuite est compté « confirmé » alors qu'il ne pariait aucun signe ; trois prédictions de B1 occupent cinq lignes ; les prédictions du harnais v2 sont rattachées au verdict v3, alors que le verdict v2 dit « non prouvé » » ; « gonflent les confirmations » ; lignes citées (contre-lecture l. 13-17 ; préenr. audit de fuite l. 92 ; verdict P3 v2 l. 476 ; verdict T0.4 v2 l. 4, 10) ; « Fable 5.2 » ; « un recompte … est en cours ».
- Les six empreintes complètes ajoutées à l'explication (54ab71dc…, efa31c80…, 07ed03b9…, edb0bf03…, aeb45c39…, 98d53c70…) et leur mention « compagnon conforme », ainsi que les huit caractères de la synthèse (2e46fe8d, bc53b746, fbf0a440, etc.).
- « la version 1 (95f6dcc8… en PDF) » (synthèse, en-tête) ; « 8c190a57… » et « b8b5df18 » (explication, déjà présents).

## Points vérifiés sans écart
- Liste : les 60 cellules du tableau, l'ordre, les trois paragraphes (ouverture « Ce qui est dit d'abord… », priorités, sources) et la phrase d'état identique à la source dans l'explication v3 et dans la synthèse v2 ; contrôle automatique (texte normalisé, balisage et gras ignorés).
- Les PDF contiennent tout le texte ajouté (comparaison mot à mot, seuls les en-têtes de pages, formules et empreintes tronquées diffèrent) ; versions 3 et 2 annoncées dans les pieds de page.
- Aucun résultat de la mesure unanime : seuls « courue, verdict scellé, tenu à l'écart » et des heures. Aucun taux 0,857.
- Cohérence des deux documents sur les points communs : heures 10:01:43, 10:33:16, 10:32:17, 09:44:58, 164 puis 167 fichiers, hachage 7d19704d, 0,783 avec réserve, liste identique.
- Les modifications de la mesure unanime dans l'explication ne laissent aucune mention « lancé » ou « non attestée » périmée.

## Fichiers ouverts
Les sept fichiers du dossier (source, deux HTML v2 et v3 de l'explication, deux HTML de la synthèse, deux PDF) ; fichiers intermédiaires créés dans ce dossier puis supprimés.

## Heures et modèle
Début 11:38:51 UTC ; fin 11:41 UTC environ (`date -u` à la dernière commande : 11:39:56, puis écriture). Modèle : Sonnet 5.5.
