# Contre-lecture ciblée — « Registre des prédictions, en une page », brouillon 3

**Verdict : bon pour impression avec retouches de forme.** Aucun taux nulle part ; tous les comptes et les deux lectures de sensibilité sont ceux attendus et toutes les sommes tombent juste ; les citations neuves sont exactes à la ligne citée ; la ligne « mesure unanime » ne porte aucun résultat ; le PDF fait 2 pages, registre entier en page 1, liste « ce qui manque » en page 2, rien de coupé. Aucun écart majeur. Onze écarts : 0 majeur, 4 mineurs, 7 de forme. Sur les 12 écarts du brouillon 2 : 9 traités, 3 traités en partie, 0 mal traité, 0 non traité.

**Une réserve à porter au directeur avant impression (écart 1)** : la page liste maintenant six prédictions chiffrées manquées au rejeu (dont P-E5) et n'en compte que quatre dans la lecture de sensibilité 33 / 11 / 6. C'est fidèle à la source retenue, mais la page ne dit pas pourquoi P-E5 n'y est pas. Je n'ai pas pu trancher (le recompte n'est pas dans ma liste).

**Avertissement de mise en page** : la page 1 est pleine jusqu'à la marge basse (dernier mot à 569,5 points, limite 569,4 points pour une marge de 9 mm). Toute retouche qui ajoute une ligne fait passer le PDF à 3 pages ; à refaire et recompter après chaque retouche.

Contre-lecteur : sous-agent neuf (règle R2), je n'ai écrit aucune des pièces lues. Aucune pièce modifiée. Aucun refus de contrôle ni de classifieur rencontré.

## 0. Empreintes (vérifiées d'abord)

| pièce | attendu | trouvé |
|---|---|---|
| `docs/notes/entretien-resultats-v1/registre-predictions-une-page-v1-brouillon3.html` | c23294cd… | `c23294cd07ac0983795e1df5eb239075d502eb4acbeffa74bd0cc96d0df407a3` égale |
| `livrables/registre-predictions-une-page-v1-brouillon3.pdf` | 17a4e976… | `17a4e97635e7e15d5585debc0e92668c9ec4a8302e04ab8e852f46521840c7e6` égale ; compagnon `.sha256` égal |
| `…/registre-predictions-une-page-v1-brouillon2.html` | 90b8feb8… | `90b8feb8c2b264ced0633aea85fc5252639ac1ad32e07ff21b0ceef1f18f1812` égale |
| `…/contre-lecture-registre-predictions-brouillon2-v1.md` | 7ff41bcf… | `7ff41bcf6fb9b5568266df1e64572ae9345ef2cd897457a214dd49baa1965434` égale |
| `…/taux-retenu-recompte-predictions-v2.md` | a745adc5… | `a745adc561176a0548372976b28a69388c73819f94561ad4474f28efe8c67d3b` égale |

Empreintes courtes des quinze verdicts cités par la pièce (`bc53b746`, `fb9919f9`, `98d53c70`, `63444faa`, `f98b5684`, `b9a07230`, `d861605c`, `05e896da`, `070a6dd4`, `320463e6`, `dece9980`, `9f7830b9`, `aaf43f95`, `7dade9ef`, `1407e460`) : recalculées, toutes égales.

## 1. Table des écarts

Lignes « html » = `cat -n` du brouillon 3. Verdicts sous `docs/verdicts/`. « taux v2 » = `taux-retenu-recompte-predictions-v2.md`.

| n° | cellule | constat | gravité |
|---|---|---|---|
| 1 | Bloc de droite (html l. 54 et l. 55) | L. 55 liste six prédictions manquées au rejeu « du côté favorable à la sonde » : P-R2 J3s, P-R2 T, P-E1, P-E2, P-E4, P-E5 (exact contre `verdict-analyses-r1-r2-relance-v4-v1.md`, l. 46-47). L. 54 n'en compte que quatre réfutées dans 33 / 11 / 6 (P-R2 J3s, P-R2 T, P-E2, P-E4), comme taux v2 l. 25-26. P-E1 s'explique (confirmée pour le signe, comptée). P-E5 (« C ≥ 0,9, observé 0,133 », l. 47) est, comme les quatre, une prédiction chiffrée manquée « sans verdict propre » ; rien dans la page ni dans taux v2 ne dit pourquoi elle n'entre pas dans la lecture de sensibilité (qui serait alors 33 / 12 / 6), ni comment elle est comptée dans 7 / 0 / 2. La page est fidèle à sa source ; la question porte sur la source. À faire : une incise qui dit le sort de P-E5, ou une décision de la session sur le compte. | **mineur** (à trancher avant impression) |
| 2 | Bloc de droite (html l. 55) | « les prédictions comptées sont écrites avant leurs courses, sauf… » : les deux exceptions sont maintenant citées et exactes (`verdict-validation-nul-v9-v1.md`, l. 13 ; `verdict-P3-premier-test-i-a-v2.md`, l. 477-478). La partie affirmative (toutes les autres séries) reste sans pièce. Nuance omise, dans le sens prudent : le même alinéa du verdict de P3 ajoute que B1 « a été calculé après S2, sans qu'aucune de ses grandeurs soit connue avant […] : son issue était prédite, non connue » (l. 478-479). | mineur |
| 3 | Mots (html l. 40) et cellules | Définis depuis le brouillon 2 : « tranchée », « non concluante », « hors compte », collision « juge » / « juge statistique » levée. Restent employés sans définition : « organisme », « témoin positif » (page 2 seulement), « G1 », « m = 1 », « J3s » (maintenant aussi dans le bloc du haut), « T » de « P-R2 T » (neuf), « v8 », « nul v9 », « puissance perdue », « kappa pondéré », « épisode », « dose », « harnais », « noyaux », « agrégateurs », « lemme d'additivité », « théorème négatif », « quarantaine », « cloison », « M1 », « M4 », « B1 », « A1 », « P-R1 », « P-E1 », « C1 à C3 ». | mineur |
| 4 | Note des sommes (html l. 114) | Liste des préenregistrements : les dix chemins existent sous `prereg/` et chacun est bien nommé par son verdict (vérifié par `ls` du chemin exact et recherche du nom dans le verdict). Incomplète : la série du harnais compte les versions 1 à 3 mais seul `T0.4-validation-modele-reel-v3` est listé (les verdicts v1 et v2 nomment `…-v1` et `…-v2`) ; rejeu « trois textes, non nommés ici » ; nul v9 hors du dépôt (dit) ; « mesure unanime » : « préenr. v15 » sans chemin. | mineur |
| 5 | Mots (html l. 40) | « Tranchée » est défini mais n'est plus employé dans la pièce (la phrase « Taux = confirmées / tranchées » a disparu ; restent « non tranché » et « ne tranche pas » dans des citations). Définition orpheline ; à garder ou à retirer pour gagner une demi-ligne. | forme |
| 6 | Bloc de droite (html l. 54) | « les quatre fourchettes […] (P-R2 J3s, P-R2 T, P-E2, P-E4, rejeu de P3) » : la parenthèse se lit comme cinq éléments ; écrire « au rejeu de P3 : … ». Le passage de 46 à 50 prédictions (les quatre s'ajoutent, elles ne sont pas retirées des confirmées : 33 + 11 + 6 = 50, taux v2 l. 25) n'est pas dit. | forme |
| 7 | Note du haut (html l. 51) | « Une première table, produite par script, est remplacée » : sans pièce. Les empreintes du recompte (`a30f24a6`) et de sa contre-lecture (`1f90eeed`), présentes au brouillon 2, ont disparu ; seule la source v2 porte chemin et empreinte. Le nom du fichier source contient « taux » : inévitable, sans conséquence. | forme |
| 8 | Colonne 1 (html l. 73) ; série étiqueteur (html l. 94-96) | Notations du pilote toujours sans date. « P-1 à P-11 » pour 5 / 3 / 1 : le verdict classe P-1 changer, P-5, P-10, P-11 « non lisibles » et P-7 « retirée » (`verdict-etiqueteur-phase1-v1.md`, l. 55, 61, 63, 66) ; ces cas ne sont couverts ni par « non concluante » ni par la définition de « hors compte ». Compte juste. | forme |
| 9 | Corps (PDF) | Corps toujours à 7,5 points (hauteur de ligne mesurée 8,7 points) ; notes et code remontés à 7,5 points ; page 1 sans aucune marge de réserve (voir avertissement en tête). | forme |
| 10 | Citations de verdict avec dénombrement (html l. 63, 95) | « 31 sur 31 était l'issue attendue par construction. 19 prédictions sur 31… » et « 11 fausses alarmes sur 120 placebos » : comptes cités mot pour mot d'un verdict, non présentés comme taux. Conforme à la décision ; signalé pour que le directeur le sache. | forme (observation) |
| 11 | Page 2, ligne de source (html l. 136) | « dernier commit du fichier `983dd664` » : conforme à ce que la contre-lecture du brouillon 2 avait relevé ; non revérifié par moi (la branche `main` m'est interdite ; branche courante `claude/upbeat-cray-dmauvv`). | forme (non revérifié) |

## 2. Consigne 1 — aucun taux, comptes bruts

- **Taux** : aucun. La colonne « taux » de la table du haut est supprimée ; « 0,717 », « 0,673 », « 0,660 », « 0,667 », « 0,857 », « 0,914 », « 1,000 » sont absents ; aucun « % » hors de la feuille de style ; aucune fraction de prédictions présentée comme taux. Le mot « taux » n'apparaît que dans « Comptes bruts, sans taux » et dans le nom du fichier source.
- **Décimaux restants en page 1**, tous des grandeurs mesurées ou prédites, aucun un taux de prédictions : 0,5 (aire au hasard), 0,1 et 0,5219 (écart de demi-précision), 0,04 à 0,17 et 0,6 (kappa), 0,48, 1,5227, 1,2464, 1,8012 (écart de coût), 0,6315 et 0,523 (aires), 0,3 et 0,932 (avance de W), 0,05 à 0,12 (prédiction M1, écrite d'avance), 8 089,62 s.
- **Groupes** (html l. 46-49) : simulation 31 / 0 / 0 ; instruments 32 / 2 / 1 ; empiriques 33 / 7 / 6 ; toutes 96 / 9 / 7 : égaux à taux v2 l. 16-19 et à l'attendu.
- **Sommes refaites sur les lignes du tableau** : instruments = harnais 24 / 1 / 1 + noyaux 8 / 1 / 0 = 32 / 2 / 1. Empiriques = pilote 3 / 2 / 2 + P3 4 / 1 / 0 + agrégateurs 2 / 0 / 1 + rejeu 7 / 0 / 2 + étiqueteur 5 / 3 / 1 + Goodhart 5 / 1 / 0 + nul v9 7 / 0 / 0 : confirmées 3 + 4 + 2 + 7 + 5 + 5 + 7 = 33 ; réfutées 2 + 1 + 0 + 0 + 3 + 1 + 0 = 7 ; non concluantes 2 + 0 + 1 + 2 + 1 + 0 + 0 = 6. Total 31 + 32 + 33 = 96 ; 0 + 2 + 7 = 9 ; 0 + 1 + 6 = 7 ; 96 + 9 + 7 = 112. La note « Sommes » (html l. 114) dit les mêmes termes. Séries « hors compte » (audit de fuite, conscience) et « fermé » (mesure unanime) : absentes des sommes, comme il se doit.
- **Lectures de sensibilité** : 33 / 11 / 6 (7 + 4 = 11 ; 33 + 11 + 6 = 50, égal au « 33 / 50 » de taux v2 l. 25) ; 26 / 7 / 6 (33 − 7 = 26 ; 26 + 7 + 6 = 39, égal au « 26 / 39 » de taux v2 l. 27). Exactes.
- **Comptes de série recomptés par moi sur le verdict** : simulation (31, l. 25) ; pilote 3 / 2 / 2 (l. 56) ; agrégateurs 2 / 0 / 1 (l. 4-5) ; étiqueteur 5 / 3 / 1 (l. 54-65 : confirmées P-1 retirer, P-2, P-4 réunies, P-6, P-8 ; réfutées P-3, P-4 relecture, P-9 ; non concluante P-1 affaiblir) ; nul v9 7 / 0 / 0 (P1 à P7, l. 13). **Non recomptés par moi** (inchangés depuis le brouillon 2, où la contre-lecture `7ff41bcf` les a trouvés égaux aux comptes retenus) : harnais 24 / 1 / 1, noyaux 8 / 1 / 0, P3 4 / 1 / 0, rejeu 7 / 0 / 2, Goodhart 5 / 1 / 0.

## 3. Consigne 2 — suivi des 12 écarts du brouillon 2

| n° | sujet | état | constat |
|---|---|---|---|
| 1 | 0,673 imprimé ; source = version 1 | **traité** | 0,673 et « (35 / 52) » supprimés ; source citée : version 2, `a745adc5`, chemin complet. |
| 2 | « Taux = confirmées / tranchées » | **traité** | Phrase supprimée avec les taux ; « tranchée » et « non concluante » définis, sans contradiction (reste : écart 5). |
| 3 | « prédictions scellées avant les courses » | **traité** | « écrites avant leurs courses, sauf » nul v9 et B1, citations et lignes exactes (reste : écart 2). |
| 4 | Liste des ampleurs manquées incomplète | **traité** | P-E2 et P-E4 ajoutés, lignes 46-47 citées ; l'ajout de P-E5 ouvre l'écart 1. |
| 5 | Goodhart : « jamais seul » | **traité** | Phrase citée mot pour mot (l. 5). |
| 6 | Préenregistrements sans chemin | **traité en partie** | Dix noms sous `prereg/`, vérifiés ; manquent harnais v1 et v2, les trois textes du rejeu, le chemin du v15 (écart 4). Pas de ligne par énoncé. |
| 7 | Rejeu : audit « trop beau » | **traité** | « déclenché », « trop beau », « audit de fuite […] avant tout énoncé », « non clos », renvoi à la série suivante : exact (l. 16). |
| 8 | Mots non définis | **traité en partie** | « hors compte » et la collision « juge » traités ; le reste de la liste demeure (écart 3). |
| 9 | Taille du corps | **traité en partie** | Notes 7 → 7,5 points, code 6,9 → 7,5 points ; corps inchangé ; interligne et marges resserrés pour tenir (écart 9). |
| 10 | Dates de course ou de verdict | **traité** | Titre de colonne refait ; « verdict 8 nov. », « verdict 5 nov. », « verdict 8 nov. » vérifiés (`verdict-etiqueteur-phase1-v1.md` l. 4 ; Goodhart l. 7 ; nul v9 l. 3). Reste : notations du pilote sans date (écart 8). |
| 11 | « non concluant par construction » coupé | **traité** | Parenthèse rétablie, exacte (l. 4). |
| 12 | Commit de la page 2 | **traité** | « dernier commit du fichier `983dd664` » ; non revérifié par moi (écart 11). |

## 4. Consigne 3 — phrases neuves (`diff` brouillon 2 → brouillon 3)

Le `diff` touche : la feuille de style (interligne, marges, tailles), le titre et l'heure d'état (11:59 UTC), l'alinéa « Mots », la table du haut et sa note, les deux alinéas du bloc de droite, l'en-tête de la table des séries, les cellules pilote (mot « notations »), agrégateurs, rejeu, étiqueteur, Goodhart et nul v9 (mot « verdict »), la note des sommes, la ligne de source de la page 2. Rien d'autre ; la liste de la page 2 est identique au brouillon 2.

Citations neuves, relues à la ligne citée :

| phrase | pièce et ligne | résultat |
|---|---|---|
| « issue attendue par construction » (les 31 de la simulation) | `verdict-T0.3-simulation-lemme-theoreme-v1.md`, l. 25 | exact (la ligne n'est pas redonnée dans le bloc, elle l'est dans la série) |
| P-R2 J3s, P-R2 T, P-E1, P-E2, P-E4, P-E5, « l. 46-47 » | `verdict-analyses-r1-r2-relance-v4-v1.md`, l. 46 (P-R2 J3s, P-E2), l. 47 (P-R2 T, P-E4, P-E5, P-E1) | exact ; « favorable à W » est écrit à la l. 47, déduit des nombres à la l. 46 |
| « écrites après les lectures préalables », `1407e460` l. 13 | `verdict-validation-nul-v9-v1.md`, l. 13 | exact |
| « écrites en connaissant l'effet décisif », `05e896da` l. 477-478 | `verdict-P3-premier-test-i-a-v2.md`, l. 477-478 | exact (à cheval sur deux lignes) |
| « non concluant par construction (puissance simulée insuffisante ou signe simulé contraire) » | `verdict-agregation-r1-v4-v1.md`, l. 4 | exact |
| audit « trop beau » déclenché, « audit de fuite […] avant tout énoncé » : non clos | `verdict-analyses-r1-r2-relance-v4-v1.md`, l. 16 | exact |
| « Le résultat se rapporte avec les deux courses interrompues et avec A1, jamais seul » | `verdict-attaque-goodhart-v3-troisieme-course-v1.md`, l. 5 | exact (« (section 0.5 bis) » omis, sans effet) |
| « préenregistrement hors du dépôt » (nul v9) | taux v2, l. 27 | conforme à la source ; non vérifié au-delà |

Affirmations neuves ou restantes sans pièce : « les prédictions comptées sont écrites avant leurs courses » pour les séries autres que les deux exceptions (écart 2) ; « Une première table, produite par script, est remplacée » (écart 7) ; « Pas encore couru : saboteurs sans consigne (T0.6) ; T0.7 et P3-bis en écriture » (cohérent avec la page 2, lignes 1, 2 et 4 ; aucune pièce citée) ; « qui recevait une consigne » (appuyé par « Fuite (lecture de la consigne) », verdict de l'audit de fuite l. 3, cité dans la série). « dix prédictions scellées » (T0.6) et « consigne privée », sans pièce au brouillon 2, sont retirés.

## 5. Consigne 4 — ligne « mesure unanime »

Inchangée depuis le brouillon 2 (aucune ligne du `diff`). **Aucun résultat, aucune lecture du résultat.** Elle porte : deux prédictions écrites d'avance (M1, M4), l'empreinte du préenregistrement `3a1651f4`, les heures de course, l'empreinte du verdict `7d19704d`, « verdict scellé en quarantaine, non lu », la cloison, « fermé ». Je n'ai ouvert ni le préenregistrement ni le verdict (interdits).

## 6. Consigne 5 — PDF

- 2 pages, A4 paysage (841,92 × 594,96 points), produit le 10 novembre 2026 à 12:00:25 UTC, polices incorporées.
- Page 1 : titre, mots, table des groupes, bloc de droite, treize séries, note des sommes jusqu'à « Page 2 : ce qui manque. » ; pied « Registre des prédictions — brouillon 3 1/2 ». Page 2 : titre « Ce qui manque… », trois alinéas, table de 11 lignes, sources, ligne de provenance ; pied « 2/2 » ; corps terminé à 481 points sur 595.
- Rien de coupé : comparaison par programme des caractères du HTML (balises retirées) et du texte du PDF, page par page : page 1, aucun caractère manquant hors de deux traits d'union de fin de ligne (effet de l'extraction du texte) ; page 2, aucun. Les seuls caractères en plus sont ceux des pieds de page. Aucun mot hors des marges (abscisses de 17,2 à 824,6 points).
- Page 1 pleine à ras de la marge basse (voir avertissement).

## 7. Fichiers ouverts, heures, modèle

Fichiers ouverts par chemin exact :
- `docs/notes/entretien-resultats-v1/` : `registre-predictions-une-page-v1-brouillon3.html`, `registre-predictions-une-page-v1-brouillon2.html` (par `diff`), `contre-lecture-registre-predictions-brouillon2-v1.md`, `taux-retenu-recompte-predictions-v2.md`.
- `livrables/registre-predictions-une-page-v1-brouillon3.pdf` et son compagnon `.sha256`.
- `docs/verdicts/` : empreinte des quinze verdicts cités ; lignes lues dans `verdict-analyses-r1-r2-relance-v4-v1.md` (13-18, 44-48, 58), `verdict-validation-nul-v9-v1.md` (1-13), `verdict-P3-premier-test-i-a-v2.md` (474-479), `verdict-agregation-r1-v4-v1.md` (3-5), `verdict-attaque-goodhart-v3-troisieme-course-v1.md` (3-7), `verdict-etiqueteur-phase1-v1.md` (1-5, 52-68), `verdict-T0.3-simulation-lemme-theoreme-v1.md` (25) ; recherche du nom du préenregistrement (compte d'occurrences) dans les verdicts T0.3, T0.4 v1 à v3, T0.5 revalidation, T0.5 pilote, P3, agrégation, audit de fuite, étiqueteur, conscience, Goodhart.
- `prereg/` : existence seule (`ls` du chemin exact) des dix préenregistrements nommés par la note des sommes ; aucun ouvert.
- `git branch --show-current` (lecture seule). Aucune autre commande git.

Non ouverts : tout fichier « mesure-unanime » ou « lectures-possibles », le préenregistrement v15, le verdict `7d19704d`, `registres/decisions.md`, `donnees/`, `diag/`, `docs/notes/bras-attaque/`, toute autre branche, le recompte et sa contre-lecture, la source de la page 2. Aucune recherche récursive, aucune variable d'environnement, aucun réseau, aucune commande git qui écrit. Fichiers temporaires (extractions du texte du PDF) écrits dans le dossier de travail temporaire de la session, hors du dépôt. Aucun compagnon `.sha256` créé pour cette note (consigne : un seul fichier de sortie) ; à sceller par la session.

Heure de début (`date -u`) : Tue Nov 10 12:01:27 UTC 2026.
Heure de fin (`date -u`) : Tue Nov 10 12:05:05 UTC 2026.

Mon modèle : Fable 5.2 (`claude-fable-5-2`).
