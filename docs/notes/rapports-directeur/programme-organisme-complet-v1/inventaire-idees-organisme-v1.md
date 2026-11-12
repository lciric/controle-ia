# Inventaire des idées, hypothèses, résultats et propositions de l'organisme d'idéation — v1 (jalon 1, partiel)

- **Version** : v1, écrite le 10 novembre 2026 à 12:07 UTC (`date -u`). **Partielle** : couvre le seul jalon 1 (rapports au directeur). Les versions suivantes (v2, v3…) ajoutent une famille de sources chacune ; la dernière est la version complète. Les numéros d'entrée sont stables d'une version à l'autre.
- **Rédacteur** : sous-agent neuf (Claude Opus 5.5) de la session mère, consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-inventaire-idees-organisme-v1.md` (`2f16dfd064540f9b…`, vérifiée contre son compagnon). Aucun appel de modèle, aucune dépense, aucun commit.
- **Demande du directeur (verbatim)** : « ecir smoi le programme complet exhaustif avce toutes les couchhes et mecanismes prevus pour l'org » puis « precise bine dans le programme toutes nos idees hypotheses resultats proposiitons pour que rien de notre brinstorm ne soit perdu ».
- **Règles suivies** : une entrée par idée distincte, même petite, même écartée ; chaque affirmation renvoie à une pièce (clé, ligne) dont l'empreinte est au § 1, ou à une ligne R- de `registres/decisions.md` (R6) ; ce qui n'a pas de source est dit « sans source ». Statuts : **codé** (avec commit ou branche), **décidé** (avec N- ou R-), **prévu**, **fermé**, **proposé non tranché**, **écarté** (et pourquoi) ; un résultat couru et scellé est « fermé ». Types : idée, hypothèse, résultat, proposition, objection, piste écartée, question ouverte.
- **Ce que ce texte ne contient pas** : aucune cellule de collisionneur ni réponse de modèle non synthétisée (elles sont listées à part dans `sorties-non-lues-v*.md`) ; rien du bras d'attaque ni du mode tenu à l'écart au-delà de son existence ; aucune valeur de sonde de la course 7a ; aucune recette d'attaque (niveau méthode, R-607) : une attaque se décrit par sa classe et son but.
- **Notation des sources** : `CLÉ:n` = pièce CLÉ du § 1, ligne n ; `[Bn]` = rangée Bn du registre des affirmations v3 (clé RAF, ligne 186 + n), suivie de la pièce primaire et des lignes qu'elle cite ; `DEC R-n` = ligne R-n du registre des décisions.

## 0. Jalons couverts par cette version

| jalon | famille de sources | heure de scellement (UTC, `date -u`) | entrées ajoutées |
|---|---|---|---|
| 01 | rapports au directeur : rapport principes-état-goulots du 9 novembre, section « Résultats de l'organisme » v3 et son registre des affirmations, prémisses de la trace interne | 12:07 | 67 |

## 1. Pièces citées (clé → chemin → sha256)

Les sources des tables s'écrivent `CLÉ:ligne(s)` ; `R-n` renvoie à la ligne R-n de `registres/decisions.md` (fichier vivant ; empreinte de l'instant du relevé à la clé DEC) ; `[Bn]` renvoie à la rangée Bn du registre des affirmations v3 (clé RAF).

| clé | chemin | sha256 | note |
|---|---|---|---|
| CONS | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-inventaire-idees-organisme-v1.md` | `2f16dfd064540f9b360da7855424cad6fe6141bb584a6aead8ddee76f3fc7da1` | consigne de cette tâche |
| RPG | `docs/notes/rapports-directeur/rapport-principes-etat-goulots-entretien-organisme-2026-11-09-v1.md` | `22263fced8d43771f0a34b3cdd9b0e6b318e39d23189907a3e9736e74413b984` | rapport de la mère au directeur, 9 novembre ; « D:n » y renvoie à une ligne de registres/decisions.md |
| SRO | `docs/notes/rapports-directeur/resultats-pour-documents-v3/section-resultats-organisme-v3.html` | `d6d702f5383347f16c894065ce45d96745a20f6016243d5f3b956828b3a3d9fd` | section « Résultats de l'organisme » v3, non contre-lue ; renvois [B1] à [B53] |
| RAF | `docs/notes/rapports-directeur/resultats-pour-documents-v3/registre-affirmations-v3.md` | `38c24c925e151dc50f8b5b59eee9d8ff04c9b08e2cc4f52a9d9206553905780e` | registre des affirmations v3 ; rangées B1 à B53 (l. 187-240) |
| PRM | `docs/notes/rapports-directeur/premisses-trace-interne-v1.md` | `2638558e34c15800acf7c8d8653dd978eba0660a9341795069d7ddd3b58e712f` | lu par recherche ciblée : « organisme » y désigne les organismes-modèles de T0.6 ; aucune entrée |
| A13 | `docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md` | `7dade9ef12a4dfa4c1ce3345d35ce9b533e8696ebdf9882443a20ad5a5e78135` | verdict scellé, troisième course d'A1-v3 |
| A4V | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md` | `e6e2f17076fab16f2684553765517937d528c657367075c126945c3ae3741cda` | verdict officiel scellé d'A1-v4 |
| A4T | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/preenregistrement-attaque-goodhart-v5-v1.md` | `d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6` | texte scellé d'A1-v4 |
| V9 | `docs/verdicts/verdict-validation-nul-v9-v1.md` | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` | verdict de validation du nul v9 |
| EPT | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v2-v1.md` | `e025f108bf84d75bd7d66bc14406ac2eafdbe00dc664f717cb4d7a2f08f4d42c` | texte court scellé, choix de λ* |
| EPL | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v1-rejeu-v2-lecture-v1.json` | `dc0bb41a337aad04182d8b7f70cb63cafd606db5396e5b5babe490e1fc6a5c50` | lecture scellée de l'épreuve de dose |
| EAB | `docs/notes/organisme-boucle-reelle-v1/essai-a-blanc-v1/journal-essai-a-blanc-v1.md` | `627f7a4c0dcede675cef70f7af73c47298bafa772cad3cc7d7e4dfaf18f7fa80` | journal de l'essai à blanc de la boucle réelle |
| N064 | `docs/decisions/decision-N-064-v1.md` | `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97` | décision N-064 |
| N065 | `docs/decisions/decision-N-065-v1.md` | `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4` | décision N-065 |
| NPOP | `docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-popper-evaluator-v1.md` | `d1ab704927b938aab631451b01ea2f197969f627dec32dcf63087bbc42ad0998` | note d'antériorité POPPER |
| NCOS | `docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-co-scientist-v1.md` | `08a3738af518f59790936995cda714210c749f20e1891195343b2c3e2b132312` | note d'antériorité Co-Scientist |
| PUB | `livrables/page-publique-organisme-2026-11-10-v1/README.md` | `b72c983eada4449931ff828d4e841aaf6708bce881657c745a8c113f3392321e` | texte exact publié le 10 novembre |
| C4R | `prep/etat-de-l-art-niveau3-v1:docs/etat-de-l-art/niveau3-v1/rapports/rapport-C4-organisme-ideation-O1-O20-v1.md` | `164502a3ed94e0adf177e4e15bfd61fc95ea24633dc1c4a2b0cacf9effab1245` | sur branche, lu par git show |
| C7R | `prep/etat-de-l-art-niveau3-v1:docs/etat-de-l-art/niveau3-v1/rapports/rapport-C7-contre-lecture-qu-chen-wang-dossier-c8-v1.md` | `63d8373761d28c62b556f35839bd7b9f277decf4dc2d6d1ad44ad1f2266f8fb2` | sur branche, lu par git show |
| V65R | `prep/organisme-v65-v1:docs/notes/organisme-boucle-reelle-v1/code-v65/rapport-developpeur-organisme-v65-v1.md` | `f84c14303eacf87e7e129955d3f9b7ba35fc7504545033c37b66b9c4ad5aff0c` | sur branche (tête 3daf08e24), lu par git show |
| DEC | `registres/decisions.md` | `d3ef663c6ccdb7cf471f45253107326ce5b6579a11cfa62210ce015826526063` | fichier vivant, empreinte relevée le 10 novembre à 12:04 UTC ; lignes R- stables |
| N3S | `prep/etat-de-l-art-niveau3-v1:docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-provisoire1.md` | `8adb561d52b728114cfd0c3065fe6c6230262f1befaeb2fd9d9824270ecdc3ad` | synthèse provisoire, citée d'après RAF ; non relue par le rédacteur |

## 2. Architecture et couches (ARC, 2 entrées)

| n° | idée | type | origine | statut | source |
|---|---|---|---|---|---|
| ARC-001 | Définition de travail : l'organisme d'idéation est une boucle où des modèles de langue, les « proposeurs », proposent des lois chiffrées sur des données, et où un juge statistique, calculé hors des agents, décide si une loi est « promue ». | idée | dessin de l'organisme (rédaction : agent de la section Résultats v3) | codé (orchestrateur ; courses A1 à A1-v4) ; énoncé du juge décidé (N-064) | SRO (paragraphe d'ouverture) ; [B1] N064:15 |
| ARC-002 | Lignée : l'organisme d'idéation est l'organisme de l'objectif ultime du programme, branché depuis le 28 octobre sur la tâche « proposer des hypothèses de recherche jugées par un juge statistique » ; il n'en a pas encore les propriétés (il ne se conçoit pas seul ; rien n'est figé après conception ; universalité non mesurée). | idée | Lazar (décision du 10 novembre) | décidé (R-2152) | [B52] DEC R-2152 ; SRO (« Décision du directeur du 10 novembre ») |

## 3. Rôles et pôles (ROL, 0 entrées)

_Aucune entrée à ce jalon._

## 4. Juges et nuls (JUG, 14 entrées)

| n° | idée | type | origine | statut | source |
|---|---|---|---|---|---|
| JUG-001 | Juge du juge-tournoi : Opus, sur les crédits Claude, à la place de Kimi (devis 80 à 145 dollars prévus chez Moonshot), après la fin d'A1-v4. | proposition | mère (rapport du 9 novembre), confiance 0,65 | proposé non tranché | RPG:40-41, 146-147, 183 |
| JUG-002 | Énoncé retenu du juge : statistique calculée par l'orchestrateur, hors de tout agent, à partir d'un engagement scellé avant que les données existent, contre un nul formé des lois connues (l'archive), avec contrôle des comparaisons multiples (revendication O2 resserrée). | idée | Lazar (N-064), sur dessin de l'organisme | décidé (N-064) | [B1] N064:15 ; SRO |
| JUG-003 | Règle de promotion : une loi est promue quand sa « richesse », une e-valeur, atteint 20 = 1/α, α = 0,05 (log W max ≥ ln 20). | idée | dessin du juge | codé (règle en service dans A1-v3 et A1-v4) | [B2] A13:54 ; N064:16 ; A4V:25 |
| JUG-004 | Versions successives du nul : v7, v8, v9 ; la v9 couvre en plus les lois recollées par morceaux à partir de lois connues (recombinaisons par morceaux, dont le monde W2). | idée | dessin du juge (successions de nuls) | codé ; v8 = nul de production | [B3] V9:30 ; A4T:200 |
| JUG-005 | Validation du nul v9 sur le banc des tricheurs : issue « puissance perdue » ; erreur tenue (0 promotion sur 1 000 sur chacune des 18 lignes fatales, dont W2) ; dents du banc (le v8 promeut W2 986 fois sur 1 000) ; prix : puissance de 0,486 (v8) à 0,381 (v9) sur une interaction faible hors archive, perte appariée 0,105 [0,0894 ; 0,1223], plus de deux fois la marge de 0,05 ; portée : mondes synthétiques du banc seulement. | résultat | banc des tricheurs v9 (8 novembre) | fermé (verdict scellé V9) | [B14]-[B18] V9:7, 12, 23-25, 30-31 |
| JUG-006 | Conséquence écrite : le nul de production reste le v8 ; le v9 ne le remplace que si le directeur accepte le prix. | résultat | verdict de validation du nul v9 | décidé par le texte du verdict (V9:32), en attente du directeur | [B19] V9:32 |
| JUG-007 | Nœud ouvert n° 1 : le prix du v9 — accepter « puissance perdue » et faire du v9 le nul de production, ou chercher un nul moins coûteux. | question ouverte | verdict v9 et mère | proposé non tranché (chez le directeur) | [B39] A4T:194 ; V9:32-33 ; DEC R-1779 ; DEC R-1883 |
| JUG-008 | Nœud ouvert n° 2 : le sens de « rien au-delà de l'archive » ; une réponse contraire à la proposition écrite demanderait un nul v10, pas une correction ; la revendication publique et la production attendent cette réponse. | question ouverte | verdict v9 et mère | proposé non tranché (chez le directeur) | [B39]-[B40] V9:33 |
| JUG-009 | Collision constatée sur PDF (10 novembre) : Qu, Chen, Wang, « Propose, Don't Judge » (arXiv 2609.27051 v1) publie un arbitre statistique gelé distinct de l'agent qui propose, un jugement sur données révélées après le dépôt, un contrôle de multiplicité par e-BH, et un arbitre éprouvé face à des proposeurs dont un modèle de langue sur monde planté ; des quatre composantes de la revendication du juge, deux sont occupées en entier (statistique hors de l'agent ; multiplicité), une dans son principe (données postérieures au dépôt), une absente (nul des lois connues) ; « qui propose ne juge pas » est publié. | résultat | contre-lecture (état de l'art niveau 3, C4 et C7) | fermé (lecture) ; conséquence non tranchée | [B47] C4R:18-38 ; C7R:49-53 |
| JUG-010 | Autres voisins du juge : « Masked Erosion » (arXiv 2610.38392) occupe dans son principe le scellement des prédictions avant les données et le scellement par empreinte ; REUSE (arXiv 2609.33180) la puissance du juge. | résultat | contre-lecture C7 | fermé (lecture) | [B50] C7R:15-42 ; N3S (cité par RAF, non lu ici) |
| JUG-011 | Options sur la revendication du juge après la collision : (a) la resserrer et citer, (b) la garder et citer ; recommandation des lecteurs : resserrer la revendication du juge (O2) et celle du banc des tricheurs (O11), et citer quatre pièces de plus ; la page publique touchée demande un nouvel accord de publication. | question ouverte | lecteurs de l'état de l'art niveau 3 ; mère | proposé non tranché (directeur) | [B48] DEC R-2177 ; DEC R-2184 ; DEC R-2190 |
| JUG-012 | Restent non trouvés occupés dans les pièces lues : le nul formé des lois connues (verdict le plus fragile : la littérature de finance sur les facteurs redondants n'est pas au dépôt), le tirage semé par l'empreinte de la proposition, l'objet (hypothèses de recherche libres, non une grille finie), des proposeurs de plusieurs fournisseurs ; réserves de portée de Qu et al. (prépublication, une version, code sur demande, finance, univers fini). | résultat | contre-lecture C7 | fermé (lecture) ; vérification de la littérature de finance ouverte | [B50] C7R:15-42, 61, 289 ; C4R:44-45 |
| JUG-013 | Vérifier la littérature de finance sur les facteurs redondants avant de défendre la nouveauté du « nul formé des lois connues ». | question ouverte | contre-lecture C7 (verdict le plus fragile) | prévu (non fait au 10 novembre) | [B50] C7R:15-42 |
| JUG-014 | Tirage des données de jugement semé par l'empreinte de la proposition (l'ordre proposition puis données garanti par construction). | idée | dessin du juge de l'organisme | codé (selon la description des composantes ; commit à relever au jalon du dépôt public) ; non trouvé occupé | [B47] C4R:18-38 ; [B50] C7R:15-42 |

## 5. Attaques et défenses du juge (ATQ, 15 entrées)

| n° | idée | type | origine | statut | source |
|---|---|---|---|---|---|
| ATQ-001 | Défense et attaque comme organisme coévolutif (P-041, 30 octobre), avec le « go » du directeur. | proposition | Lazar et mère (P-041) | décidé (go du directeur, P-041) ; détail au jalon des décisions | RPG:127-128 |
| ATQ-002 | Attaque de Goodhart (A1) : un proposeur modèle de langue (Argon) lit la description exacte du juge ; bras « retour » (verdict et richesse de chacune de ses 16 tentatives) contre bras « témoin » (rien) ; 24 unités par case ; mondes où toute promotion est fausse. | idée | dessin d'A1 (mère et organisme) ; proposeur Argon | codé et couru (A1, A1-v3, A1-v4) | [B5] A4T:200, 217, 221 ; N064:17 ; A13:52 |
| ATQ-003 | Issues gelées d'avance : « résiste (à cette taille) » si au plus 1 promotion sur 24 avec retour (borne haute de Wilson ≤ 0,25), instrument sain ; « brèche » si au moins 4 sur 24. | idée | préenregistrements d'A1-v3 et A1-v4 | décidé (textes scellés) | [B6] A4V:25 ; A13:17 |
| ATQ-004 | Règle de lecture « jamais seul » : chaque résultat d'attaque se rapporte avec toutes les courses qui l'ont précédé (A1, les trois courses d'A1-v3, A1-v4). | idée | texte scellé d'A1-v4 | décidé (A4T:193) | [B7] A4T:193 ; A13:5, 76 |
| ATQ-005 | A1 (2 novembre) : monde W1 « instrument en défaut » ; monde W2 « brèche sous v8 ». | résultat | course A1 | fermé | [B7] A13:5, 76 |
| ATQ-006 | A1-v3, première course : 41 appels, 4,245753 dollars, arrêt par l'infrastructure, sans résultat ; deuxième course : 620 appels, 48,49583 dollars, état scellé non lu. | résultat | courses A1-v3 | fermé (première) ; scellé non lu (deuxième, voir sorties non lues) | [B7] A13:5, 76 |
| ATQ-007 | A1-v3, troisième course (5 novembre), juge au nul v8 : W1 « résiste (à cette taille) », 1/24 avec retour, Wilson [0,0074 ; 0,2024], et le juge v7 battu 23/24 (l'attaque a des dents) ; W2 « infirmée (brèche sous v8) » par classe non couverte, 24/24, les 48 lois promues rejouées au-dessus de α après Holm ; 58,44887 dollars. | résultat | course A1-v3 n° 3 | fermé (verdict scellé A13) | [B8]-[B11] A13:4, 14-22, 48, 70 |
| ATQ-008 | Réserves d'A1-v3 : course « trop propre » (960 appels sans panne, faute de témoin négatif planté) ; « résiste » tient à une seule promotion ; W2 saturé ne dit rien du rôle du retour ; le verdict ne dit pas que le v8 est sûr ni que le retour fait gagner (écart +0,042 sur W1, p = 1,0). | objection | verdict A1-v3 | fermé (réserves écrites au verdict) | [B12]-[B13] A13:63-66, 110, 112 |
| ATQ-009 | A1-v4 (9-10 novembre), juge au nul v9 : W2 « résiste (à cette taille) », 1/24 avec retour, Wilson [0,0074 ; 0,2024] ; l'ancien juge v8 battu 24/24 ; instrument sain ; suspension par deux audits levée (les quatre lois promues se rejouent 2, 3, 2 et 3 fois sur 200, aucune au-dessus de α après Holm). | résultat | course A1-v4 ; verdict officiel d'un lecteur neuf d'une autre lignée | fermé (verdict officiel scellé) | [B25]-[B26] A4V:4, 31-34, 52, 56 |
| ATQ-010 | Lecture bornée gelée de W2 sous v9 : « sur deux mondes jouets au nul v9, un fournisseur, une forme d'optimisation, 16 tentatives avec retour et la liste des classes non couvertes en main, aucune fausse promotion au-delà de la règle de la grille » ; lue pour le directeur : « validé à cette taille, dans ce monde jouet, contre ce proposeur », pas « validé » en général. | résultat | texte scellé d'A1-v4 ; lecture de la mère | fermé | [B27] A4V:36 ; [B53] DEC R-2115 |
| ATQ-011 | A1-v4 sur W2g à λ* = 0,40 : « frontière franchie, robuste » ; 10/24 avec retour, Wilson [0,2447 ; 0,6117] ; 10 des 17 lois promues rejouées au-dessus de α après Holm (r = 0,588 ; 12/17 si Holm par monde) ; lecture gelée : le proposeur trouve une loi qui se rejoue au-dessus de α là où l'archive seule ne passe pas ; ce n'est pas « le v9 n'a pas de prix ». | résultat | course A1-v4 | fermé (verdict officiel scellé) | [B28]-[B29] A4V:42, 46 |
| ATQ-012 | Prédictions d'A1-v4 : 8 tenues sur 11 ; non tenues : W2 une promotion au lieu de zéro ; W2g 10 promotions au lieu d'au moins 12 ; part de lois robustes 0,588 au lieu d'au moins 0,80 ; le gain du retour n'est pas établi (écart par loi « non tranché » sur W2g) ; dépense 114,0434 dollars pour un plafond de 200. | résultat | course A1-v4 | fermé | [B30]-[B32] A4V:54, 66-78 |
| ATQ-013 | Réserves d'A1-v4 : course « trop propre » ; W2 à la limite de la règle (1/24 avec retour, 3/24 sans) ; sur W2g la frontière n'est visible à l'oracle que sur 17 cartes sur 24 ; λ* à la limite (loi du monde promue dans 72,2 % des cas sur les cartes de la course) ; audit et verdict provisoire du même lecteur ; réponses du proposeur lues par programme seulement. | objection | verdict officiel d'A1-v4 | fermé (réserves écrites) | [B33] A4V:72, 82-91 |
| ATQ-014 | L'attaque de Goodhart et le banc des tricheurs sont revendiqués dans leur seule forme, leur principe étant occupé depuis 2015 (Dwork et al. ; Ladder) ; la forme de l'attaque (un proposeur modèle de langue qui lit la description exacte d'un juge statistique pour le tromper, sur des mondes où toute promotion est fausse) n'est trouvée dans aucune pièce lue. | résultat | N-064 ; contre-lecture C7 | décidé (N-064) | [B45] N064:15-17 ; NPOP:42-50 ; [B50] C7R:15-42 |
| ATQ-015 | REUSE (arXiv 2609.33180) construit en théorie un proposeur adverse qui ne reçoit que les décisions et force une fausse promotion : voisin de l'attaque de Goodhart et de la puissance du juge. | résultat | contre-lecture C7 (état de l'art niveau 3) | fermé (lecture) ; citation recommandée | [B50] C7R:15-42 ; SRO § 7 |

## 6. Boucle fermée et héritage (BOU, 5 entrées)

| n° | idée | type | origine | statut | source |
|---|---|---|---|---|---|
| BOU-001 | Essai à blanc de la boucle réelle complète (7 novembre), hors ligne, fournisseurs simulés, sans dépense. | résultat | session de la boucle réelle | fermé (journal scellé EAB) | [B34] EAB:5-6, 33-35 |
| BOU-002 | Constats de l'essai à blanc : le vrai bac à sable des tests de mort n'a pas pu tourner faute de l'outil d'isolement (la garde refuse proprement) ; aucune archive de départ ne peut être posée ; le code joue toujours trois bras dont deux de référence payants ; la lecture gelée existante applique les critères d'une expérience antérieure ; les commandes d'appel aux fournisseurs réels manquent (le mode réel ne peut démarrer) ; version de la bibliothèque de calcul différente de la documentée. | résultat | essai à blanc | fermé (constats) ; remède : code v65 | [B35] EAB:73-86 |
| BOU-003 | Code v65 : dix fichiers neufs sans modifier l'existant ; archive de départ scellée ; lois plantées jugées avec l'archive ; bras réel seul ; lecture gelée propre au nouveau dessin ; commandes d'appel aux fournisseurs nommées avec leurs empreintes ; 232 essais réussis, 3 sautés (outil d'isolement), 38 mutations tuées sur 38, essai à blanc en 9 étapes. | résultat | développeur v65 (session neuve, sur le mot du directeur) | codé (branche prep/organisme-v65-v1, tête 3daf08e24) ; non contre-lu | [B49] V65R:22, 31-33, 51-53, 70-85 ; [B51] DEC R-2148 |
| BOU-004 | Réserves du développeur v65 : le vrai bac à sable n'a toujours pas tourné ; à graine égale, deux essais à blanc rendent des relevés d'empreintes différents (décisions égales, relevé non reproductible à l'octet) ; les proposeurs simulés recopient la loi plantée, l'issue à blanc est « trop belle » par construction. | objection | développeur v65 | ouvert (réserves écrites) | [B49] V65R:129-133 |
| BOU-005 | Conditions de la première course réelle de la boucle : code v65 contre-lu, machine dotée de l'outil d'isolement (bwrap), préenregistrement scellé ; dépense sur devis dans l'enveloppe de calcul accordée jusqu'au 27 novembre ; contre-lecture du code lancée puis interrompue par la fin du quota. | proposition | mère et directeur (enveloppe) | prévu ; aucune course réelle autorisée au 10 novembre | [B49] DEC R-2177 ; [B51] DEC R-2148 ; GO-2026-11-10-09 (selon RAF) |

## 7. Composition apprise et coût (COM, 0 entrées)

_Aucune entrée à ce jalon._

## 8. Universalité et familles inédites (UNI, 2 entrées)

| n° | idée | type | origine | statut | source |
|---|---|---|---|---|---|
| UNI-001 | L'universalité de l'organisme n'est pas mesurée sur des familles inédites : propriété de l'objectif ultime encore non atteinte, avec « se concevoir seul » et « figé après conception ». | question ouverte | Lazar (R-2152) | prévu (objectif ultime) ; non atteint au 10 novembre | [B52] DEC R-2152 |
| UNI-002 | Pour mesurer l'universalité sur une famille jamais vue à la conception (N-044), réserver dès maintenant le proposeur trompeur comme famille tenue à l'écart (N-054) ; à décider avant toute conception de sonde qui pourrait le toucher. | question ouverte | mère (rapport du 9 novembre) | proposé non tranché (nœud du directeur) | RPG:156-157, 169 |

## 9. Vérité, oracles et mondes plantés (VER, 9 entrées)

| n° | idée | type | origine | statut | source |
|---|---|---|---|---|---|
| VER-001 | Mondes plantés de l'attaque : W1 mélange deux lois de l'archive (couvert par le v8) ; W2 applique une loi connue à une sous-population et une autre à la seconde (recombinaison par morceaux, non couverte par le v8) ; bâtis à partir des seules lois de l'archive, toute promotion y est fausse. | idée | dessin d'A1 | codé (A1 à A1-v4) | [B5] A4T:200 ; [B8] A4T:203 ; A13:48 |
| VER-002 | Monde gradué W2g : à la loi d'une sous-population se mêle une part λ d'une loi neuve ; il se place à la frontière du v9, où une promotion n'est plus fausse par construction. | idée | dessin d'A1-v4 | codé et couru (A1-v4) | [B20] A4T:201 |
| VER-003 | Choix de la dose λ* par une règle mécanique écrite avant toute épreuve, sur processeur, sans dépense : plus petite dose où la loi du monde est promue sous v9 au moins 800 fois sur 1 000 et où la recombinaison pure n'est jamais promue. | idée | texte court scellé de l'épreuve | décidé (texte scellé EPT) | [B21] EPT:44, 48-50 |
| VER-004 | Issue de l'épreuve : λ* = 0,40 ; loi du monde promue 803/1 000 (Wilson [0,777 ; 0,826]) ; recombinaison pure 0/1 000 à toutes les doses ; mention gelée « λ* à la limite » (borne basse sous 0,80), λ* inchangé ; aucune évaluation impossible. | résultat | épreuve hors ligne du monde gradué | fermé (lecture scellée EPL) | [B22]-[B24] EPL (champs lambda_etoile, par_dose, a_la_limite, evaluations_impossibles) |
| VER-005 | Banc des tricheurs : sur des mondes synthétiques, planter des lois qui ne doivent jamais être promues (lignes « fatales ») et des lois vraies (mesure de la puissance), 1 000 répétitions par ligne, pour valider un nul avant production. | idée | dessin du banc (v9) | codé et couru (validation du nul v9) | SRO § 2 ; [B14]-[B16] V9:7, 23-24 |
| VER-006 | Voisins publiés des gestes du banc et des témoins : trois arbitres délibérément fautifs, un attaquant scripté et un plan préenregistré (Qu et al.) ; témoins plantés (PROCTOR, arXiv 2609.02246) ; PACE (arXiv 2606.08106) voisin du banc. | résultat | contre-lecture C7 | fermé (lecture) ; resserrement de la revendication du banc recommandé, non tranché | [B50] C7R:15-42, 61 |
| VER-007 | Témoins fixes de la boucle : ils comprennent des lois que le nul ne couvre pas ; l'un d'eux, une loi fausse plantée (T-F2), a été promu par le juge puis éliminé par son test de mort ; explication « probable, non vérifiée ». | résultat | essai à blanc | fermé (constat) ; explication non vérifiée | [B36] EAB:47-53, 79 |
| VER-008 | Test de mort : une expérience conçue pour réfuter une loi promue, jouée après la promotion dans un bac à sable isolé. | idée | dessin de la boucle réelle | codé (garde du bac) ; jamais joué dans le vrai bac au 10 novembre | SRO § 5 ; [B36] EAB:47-53 |
| VER-009 | Témoins jugés sans l'archive : en simulation, au moins une loi fausse de la classe couverte serait promue dans 994 répétitions sur 1 000 ; d'où l'exigence de juger les lois plantées avec l'archive. | résultat | essai à blanc | fermé (constat) ; corrigé dans le code v65 | [B37] EAB:67, 80 ; [B49] V65R |

## 10. Mathématiques, preuve et Lean (couche 4) (MAT, 0 entrées)

_Aucune entrée à ce jalon._

## 11. Récompense collective et signalement (Avalon, N13) (REC, 0 entrées)

_Aucune entrée à ce jalon._

## 12. Papier C et menaces diffuses (N-065) (PAC, 11 entrées)

| n° | idée | type | origine | statut | source |
|---|---|---|---|---|---|
| PAC-001 | Le juge statistique de l'organisme est un moniteur : il surveille des affirmations produites par des agents ; l'attaque de Goodhart d'A1-v4 est un attaquant adaptatif qui cherche à le déplacer ; le juge-tournoi façon Co-Scientist est un juge génératif mis sous la même attaque. | idée | mère (rapport du 9 novembre) | décidé (N-065 : juge = surveillant d'affirmations de recherche) | RPG:23-25, 133-137 ; [B4] N065:14-17 |
| PAC-002 | Rôle 1 — second terrain du papier C (« l'instrument ») : A1-v4 (juge statistique) et le juge-tournoi (juge génératif) mesurent le gain de corruption sur les juges de la recherche automatisée ; prédiction de C : juges génératifs à gain positif, agrégations robustes à gain nul ou négatif ; C n'est plus montré sur un seul domaine. | proposition | mère (rapport du 9 novembre), recommandée confiance 0,7 | décidé (N-065) | RPG:141-147, 169-170 ; [B4] N065:14-17 |
| PAC-003 | Argument d'apport : le domaine est celui ouvert par Co-Scientist, que la note d'antériorité montre sans validation statistique ni attaque de son juge. | idée | mère (rapport du 9 novembre) | proposé ; à relire après la collision Qu-Chen-Wang (voir JUG) | RPG:144-145 |
| PAC-004 | Rôle 2 — atelier d'idées du programme : l'organisme reçoit des questions ouvertes du programme ; ses fiches sont du matériau, jamais une preuve ; tout usage décisif passe par un préenregistrement (R1). | proposition | mère (rapport du 9 novembre), confiance 0,7 | décidé (N-065) | RPG:148-151 ; CLAUDE.md (résumé de N-065) |
| PAC-005 | Première question d'atelier : la question v2 du pilier attaque, « chercher la trace », est scellée ; sa course est bloquée par la règle de permission de l'organisme v2, que seul le directeur peut écrire dans `.claude/settings.json`. | proposition | mère | prévu ; bloqué (geste du directeur attendu au 9 novembre) | RPG:41-42, 75, 95, 149-151, 184 |
| PAC-006 | Rôle 3 — famille de menaces diffuses pour les papiers A et B : un proposeur qui trompe le juge sur de nombreuses propositions, chacune d'apparence honnête, est une menace diffuse au sens exact du programme. | proposition | mère (rapport du 9 novembre), confiance 0,5 | proposé non tranché (N-065 : rôle 3 « à trancher ») | RPG:152-157, 169-170, 187 |
| PAC-007 | Si le proposeur trompeur est un modèle à poids ouverts (le 8B), les sondes du programme peuvent lire si l'intention de tromper le juge se voit dans ses activations avant que le juge ne soit trompé : la thèse « la preuve interne survit » portée à la recherche automatisée. | hypothèse | mère (rapport du 9 novembre) | proposé non tranché (dépend du rôle 3) | RPG:153-156 |
| PAC-008 | Positionnement : les bancs publics et l'organisme d'idéation servent la validité et les papiers B et C, pas la porte G0. | idée | mère (rapport du 9 novembre) | proposé (lecture des principes premiers) | RPG:59-61 |
| PAC-009 | « Voir si l'organisme trouve des failles » (26 octobre). | idée | Lazar | repris par le rôle 2 (atelier) ; voir aussi pilier attaque | RPG:126 ; DEC R-504 |
| PAC-010 | « Avec l'organisme on peut attaquer des questions bien plus ambitieuses » (28 octobre). | idée | Lazar | repris par le rôle 2 (atelier) | RPG:127 ; DEC R-619 |
| PAC-011 | « Lançons l'org idéation dessus » (8 novembre) ; « il faut intégrer tout ce qu'on fait actuellement dans le programme présenté à TAIF et réfléchir à comment faire les liens » (8 novembre). | idée | Lazar | repris par le rapport du 9 novembre puis N-065 | RPG:128-129 ; DEC R-1770 ; DEC R-1793 ; DEC R-1832 |

## 13. Outillage et gouvernance (OUT, 9 entrées)

| n° | idée | type | origine | statut | source |
|---|---|---|---|---|---|
| OUT-001 | Invariant : aucun score d'un moniteur du programme dans l'entraînement ou la sélection de l'organisme ; un organisme qui écrit ses moniteurs et s'en sert pour se sélectionner viole l'invariant ; moniteurs neufs pour mesure rapportée seulement, jamais comme signal. | idée | audit défensif (N-053), étendu à l'organisme par la synthèse du collisionneur n12-n13 | décidé (N-053) | RPG:159-161 |
| OUT-002 | Citations obligatoires de N-064 dans tout texte qui présente l'organisme (POPPER ; Dwork et al. 2015 ; Blum et Hardt, Ladder ; Co-Scientist). | idée | Lazar (N-064) | décidé (N-064) | RPG:116, 161-162 ; [B41] N064:17 ; [B42]-[B44] |
| OUT-003 | Phrase et diapositive pour l'entretien : « notre question vaut aussi pour les juges de la recherche automatisée ; nous la testons sur un organisme d'idéation dont le juge statistique est attaqué par un proposeur qui lit ses verdicts, et nous le comparons à un juge génératif façon Co-Scientist » ; aucun chiffre tant qu'A1-v4 n'a pas rendu son verdict scellé. | proposition | mère (rapport du 9 novembre) | proposé non tranché | RPG:164-167 |
| OUT-004 | L'organisme figure parmi les éléments absents de la candidature déposée ; la question de son intégration a été posée sous plusieurs formes sans réponse unique écrite avant le 9 novembre. | résultat | mère (constat) | fermé (constat) ; réponse donnée au § 6 du rapport du 9 novembre | RPG:126-131 |
| OUT-005 | Objection d'emploi du temps : l'effort sur le juge-tournoi et le collisionneur se disperse hors du chemin critique de G0 ; recentrer la mère jusqu'au 15 novembre sur ce qui fait partir la course 7b, le reste n'avançant que s'il ne coûte ni décision du directeur ni attention de la mère. | objection | mère (rapport du 9 novembre), confiance 0,8 | proposé, défaut « oui » sous 48 heures | RPG:19-22, 176 |
| OUT-006 | Incident : Argon appelé pendant A1-v4 en écart à un texte scellé (exclusivité) ; option (a) proposée : garder la course telle quelle, comptes lus par l'audit A9, relancer l'étiqueteur après A1-v4 ; leçon écrite : chercher, avant toute course, les conditions d'exclusivité des courses en marche. | résultat | mère (écart R-2013 ; leçon R-2012, R-2013) | proposé, défaut (a) le 11 novembre ; leçon écrite | RPG:20, 85-87, 177 |
| OUT-007 | Collisionneur en mode critique, avec témoins plantés, pour entraîner les réponses aux questions dures de l'entretien (après une v17 du programme d'entretien contre-lue), ≈ 10 à 15 dollars sur crédits Claude. | proposition | mère (rapport du 9 novembre), confiance 0,7 | proposé non tranché | RPG:42, 120-122, 188 ; DEC R-1790 (point e, selon RPG:121) |
| OUT-008 | Verdict officiel prononcé par un lecteur neuf d'une autre lignée que l'auditeur, scellé, en accord complet sur le fond avec le verdict provisoire. | idée | mère (procédure d'A1-v4) | fait (A1-v4) | RAF:232 [B25 complément] DEC R-2111 ; A4V:4 |
| OUT-009 | Publication du résultat scellé d'A1-v4 sur la page publique de l'organisme (10 novembre), avec lectures bornées, réserves, règle « jamais seul » et deux décisions ouvertes ; 22 corrections d'une contre-lecture appliquées ; aucune recette ; publiée avant la constatation de la collision : la corriger demande un nouvel accord de publication. | résultat | directeur (mot de publication) ; mère | fait (publié) ; correction proposée non tranchée | [B46] DEC R-2162 ; PUB ; [B48] |

## 14. Décompte

| famille | entrées |
|---|---|
| ARC — Architecture et couches | 2 |
| ROL — Rôles et pôles | 0 |
| JUG — Juges et nuls | 14 |
| ATQ — Attaques et défenses du juge | 15 |
| BOU — Boucle fermée et héritage | 5 |
| COM — Composition apprise et coût | 0 |
| UNI — Universalité et familles inédites | 2 |
| VER — Vérité, oracles et mondes plantés | 9 |
| MAT — Mathématiques, preuve et Lean (couche 4) | 0 |
| REC — Récompense collective et signalement (Avalon, N13) | 0 |
| PAC — Papier C et menaces diffuses (N-065) | 11 |
| OUT — Outillage et gouvernance | 9 |
| **total** | **67** |

| type | entrées |
|---|---|
| hypothèse | 1 |
| idée | 23 |
| objection | 4 |
| proposition | 9 |
| question ouverte | 6 |
| résultat | 24 |

