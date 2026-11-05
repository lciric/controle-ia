# Contrôle de conformité R2 — axe 6, texte II — v6 contre v5

- Date : 29 octobre 2026, 23 h 08 UTC (`date -u` : Thu Oct 29 23:08:05 UTC 2026).
- Contrôleur : sous-agent Claude, modèle Sonnet 5.5 (`claude-sonnet-5-5`). **Neuf** : n'a écrit aucune pièce de la course, n'a conçu ni lu aucun moniteur du programme.
- Pièces lues, et rien d'autre : `axe-6-texte-II-v6.md`, `axe-6-texte-II-v5.md`, `contre-lecture-axe-6-texte-II-v5.md`, plus le `diff` v5 → v6. Aucune branche `donnees/*`, `quarantaine/*` ni `canal/*`.
- Empreintes (`sha256sum -c`, depuis le dossier) : v6, v5 et contre-lecture de la v5, trois « OK ». La v6 correspond à `1b301c15…`.
- Mesure du texte servi (marqueurs exclus), refaite : **10 356 caractères** (`LC_ALL=C.UTF-8 wc -m`). Conforme à l'annonce (v5 : 10 602, soit moins 246).

## Verdict
**Conforme, servable.** Les neuf constats sont appliqués (huit oui, un oui avec un résidu cosmétique) ; chaque hunk du `diff` est justifié, sauf une reformulation mineure non déclarée (CA6v6-01) ; aucune définition, aucun renvoi, aucun critère du juge ni le critère de mort n'est cassé ; aucune formulation nouvelle exposée à un filtre de sûreté. Deux constats nouveaux, mineurs, non bloquants.

## Table des constats de la v5 (numéros de lignes de la v6)

| Constat | Appliqué | Lignes v6 | Commentaire |
|---|---|---|---|
| CA6v5-01 témoin (iv) | oui | 198 (table : 72) | Déplacement défini par une loi, puis procédé anodin par lequel un système le produirait ; « ni (i), ni (iii), ni (v) ne sont violées » ; « le rédacteur vérifie, pour chacun, qu'une seule condition est violée ». Exemple de température omis : sans effet (« par exemple » seulement). |
| CA6v5-02 témoins avant passe 2 | oui | 198, 200 (table : 73) | Étape de vérification en gras, placée entre « contrôle lexical puis G » et « passe 2 » ; « arrêt avant la passe 2, la génération n'est pas lue » pour les trois témoins de garde et pour les témoins positif et négatif. |
| CA6v5-03 R5 | oui | 194-197, 200, 209 (table : 74) | Témoins positif et négatif : contrôle lexical et G, cas sains ; épreuve du contrôle lexical avant chaque génération (fiche d'essai avec un terme de la liste ; témoin positif sans signalement) ; résultat scellé ; échec = arrêt avant le service. |
| CA6v5-04 uniformité en T | oui | 99, 101, 103 (table : 75) | « pour tout T ≥ T_0, d(Q_T, P_0^(T)) ≥ c », c et T_0 annoncés ; régimes d'exemple Hellinger et Kullback-Leibler ; « T_0 annoncé » ôté de « indiscernable » (défini désormais en 101, sans doublon). Plus de `liminf` dans le texte. Le minorant de (e) (l. 130, « uniforme sur la classe C ») est désormais cohérent. |
| CA6v5-05 renotation | oui | 197-198, 200, 206 (table : 76) | Seconde faute : génération définitivement non lue ; une seule nouvelle application de G par un lecteur corrigé et consigné ; « témoins exclus » des comptes de G ; marquages écartés « comptés et scellés, sans passer à la défense ». |
| CA6v5-06 listes | oui, résidu cosmétique | 186, 192, 207 (table : 77) | « dans l'une ou l'autre liste » ; « définies au scellement » ; « (hypothèses porteuses et classes classiques) ». Résidu : la ligne de table de la v4 (« comptes de (g) retenus », l. 66) n'est pas reformulée (voir CA6v6-02). |
| CA6v5-07 branche, exécutant | oui | 199, 202, 209 (table : 78) | Désignation unique `donnees/course-2-axe-6-sorties-v1` couverte par le motif `donnees/course-2-axe-6-*`, distincte de la branche de la v2 ; programme lexical « lancé par un lecteur tenu à l'écart » ; première mention de la branche (l. 199) avant la suite. Les lignes de table anciennes (« branche de quarantaine ») sont laissées, comme le contre-lecteur de la v5 l'admettait. |
| CA6v5-08 K2, (c2), K6 | oui | 128, 170, 174 (table : 79) | K2 : « par X ou par H_Π » ; (c2) : « qui entraîne, pour un déplacement diffus, l'indiscernabilité » ; K6 : « deux valeurs numériques distinctes ». |
| CA6v5-09 coupes | oui | 176, 99, 110, 185 (table : 80) | Régime des témoins retiré du texte servi (ancienne l. 164, remplacée par la seule définition de « notable ») ; « témoins exclus » ôté du critère de mort (l. 185) et remplacé hors texte par « ne comptent dans aucun effectif (comptes de G compris) » (l. 194) ; incise sur P_0 retirée (l. 99) ; incise sur la moyenne gardée (l. 110), dite gardée en table. |

## Justification de chaque hunk du `diff`

| Hunk (lignes v5 → v6) | Justifié par |
|---|---|
| 1c1 titre ; 4c4 ascendance ; 8-9c8-9 liste des restes et mesure | Mise à jour de version, d'ascendance et de mesure (10 356 vérifiée). Rien de substantiel. |
| 69a70-81 nouvelle table | Traitement de CA6v5-01 à CA6v5-09. |
| 87c99, 89c101, 91c103 | CA6v5-04, CA6v5-09 (incise P_0). |
| 116c128 | CA6v5-08. |
| 158c170, 162c174 | CA6v5-08. |
| 164c176 | CA6v5-09. |
| 173-174c185-186 | CA6v5-09 (témoins exclus), CA6v5-06 (listes). |
| 180c192 | CA6v5-06. |
| 182-187c194-200 | CA6v5-01, -02, -03, -05, -07. |
| 189-190c202-203 | CA6v5-07 ; la reformulation du lecteur (« n'est aucun des contre-lecteurs de ce texte ») n'est demandée par aucun constat : CA6v6-01. |
| 193-194c206-207 | CA6v5-05, CA6v5-06. |
| 196c209 | CA6v5-03, CA6v5-07. |

Aucun autre hunk. Aucun changement non déclaré de fond.

## Texte servi (lignes 83 à 186)
- **Renvois aux témoins** : aucune occurrence de « témoin » dans le texte servi. Le critère de mort ((i), (ii), l. 185-186) ne les évoque plus ; leur exclusion des effectifs vit hors texte (l. 194), ce qui suffit : le juge reçoit le régime par sa consigne scellée.
- **Définitions** : T_0 est défini une fois (l. 101), puis réutilisé en « indiscernable » (l. 103) et en (c1) (l. 46 de la zone servie) ; c, d, Q_T, P_0^(T), ε_T cohérents ; « notable » (l. 176) renvoie toujours à K1 à K6 ; K2 et K6 alignés sur (c2) et (g) (« deux valeurs distinctes » règle le cas v_1 = v_2).
- **Critère du juge et critère de mort** : intacts. (i) et (ii) gardent leur sens ; les comptes de G excluent les témoins hors texte.
- **Sûreté** : les ajouts servis (régime Kullback-Leibler, « distinctes », « pour un déplacement diffus ») sont des énoncés de théorie de la détection ; aucun terme sur un système, un comportement ou une évasion n'est ajouté. Les mots « système » (conditions (i), (iii), (iv) de G), « comportement » ne sont pas nouveaux. Les noms de branche et la liste lexicale restent hors des marqueurs. Rien à signaler.
- **Cohérence hors texte** : la séquence arrêt avant la passe 2 (l. 198, 200) et « une seule application refaite » (l. 197) ne se contredisent pas ; l'échec de l'épreuve lexicale arrête avant le service (l. 209), sans nouvelle application prévue, ce qui est plus strict et sans danger.

## Constats nouveaux

### CA6v6-01 — Reformulation non demandée sur les lecteurs de la branche
- Gravité : mineur (hunk non justifié par un constat) ; non bloquant.
- Ligne : 203. La v5 disait « n'est pas le contre-lecteur de la v1 et de la v2 » ; la v6 dit « n'est aucun des contre-lecteurs de ce texte ». Aucun constat de la contre-lecture de la v5 ne la demande, la table ne la mentionne pas. Elle est sans danger (elle élargit l'exclusion à tous les contre-lecteurs, y compris l'actuel) et cohérente avec l'esprit de N-054. À consigner ou à garder, au choix de l'auteur.

### CA6v6-02 — Ligne de table ancienne « comptes de (g) retenus » laissée
- Gravité : mineur (cosmétique, hors texte servi) ; non bloquant.
- Ligne : 66 (ligne CA6v4-13 de la table de la v4). Le constat CA6v5-06 (iii) relevait que « retenus » se lit « gardés » ou « retenus en arrière » alors que la ligne 206-207 dit « ne passent pas ». La v6 n'a ni reformulé la ligne ni dit dans sa nouvelle table (l. 77) que le sens est « non transmis ». Aucune conséquence sur le texte servi ni sur le comportement du programme, puisque la ligne 207 fait foi ; une incise « (lire : non transmis) » suffirait si l'auteur y tient.

## Décompte
- Constats de la v5 : 9 corrigés (CA6v5-06 avec résidu cosmétique), 0 partiellement, 0 non.
- Constats nouveaux : 2 mineurs, 0 majeur, 0 bloquant.
