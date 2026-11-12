# Registre des goulots d'étranglement et des questions à résoudre avant l'entretien avec le Transformative AI Fund — v1, brouillon 1

- **Auteur** : sous-agent neuf de la session mère (`session_016QhUrrLeN21G7Z9KZobE42`), modèle déclaré par l'environnement : Claude Fable 5.1. Il n'a écrit aucune pièce citée ici. Brouillon non contre-lu, non scellé ; aucun fichier existant modifié ; aucune dépense ; aucun réseau.
- **Heure de début** : 2026-11-08 14:28:44 UTC (relevé `date -u`) ; dossier créé à 14:33:27 UTC ; heure de fin en dernière ligne.
- **Cadre fixé par Lazar** (mots verbatim au registre) : « les expériences à faire pour convaincre le jury doivent se faire en une semaine et coûter le moins possible car pas encore de bourse obtenue » (R-1830, `registres/decisions.md` l. 1788) ; « c'est dans deux semaines en fait mais procédons déjà sur ce qui peut être fait en une semaine » (R-1834, l. 1792) : l'entretien est **dans deux semaines (vers le 22 novembre 2026, jour exact à confirmer)**. Conséquence pour ce registre : la colonne **« remède faisable en ≤ 7 jours »** est le plan d'action ; une colonne **« si 8 à 14 jours »** n'apparaît que quand le remède ne tient pas en une semaine mais tient avant l'entretien ; rien n'est planifié au-delà (la seconde semaine se décide plus tard, message de la session mère du 8 novembre 14:33 UTC).
- **Pièces lues** (extraits ciblés par `grep -n`, jamais les données) : `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` (`f5599896…`) ; `registres/etat.md` (l. 1-60, 166-195, 340-410) ; `registres/decisions.md` R-1580 à R-1834 (l. 1538-1792) ; `registres/go.md` (l. 216-280) ; `registres/depenses.md` (l. 315-402) ; `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` (`186173d9…`, sections 4, 9, 10, 11, « Points à trancher », « Questions qu'un évaluateur poserait », « Ce que la v11 n'a pas pu vérifier ») ; `docs/decisions/decision-N-062-v1.md` (`63f42690…`) ; `docs/decisions/decision-N-060-v3.md` (`2b448f69…`) ; `prereg/audit-rappel-oracle-sabotages-connus-v1-brouillon1.md` (brouillon, `ccc0d972…` au moment de la lecture) ; `docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` (§ 4, 8, 9 ; `60980ae6…`) ; `livrables/registres-taif-v3/` (`promis-livre-v2.md` `57522295…`, `calibration-v2.md` `112b147b…`, `total-depenses-v2.md` `8e6a1c01…` ; tables régénérées le 8 novembre à 14:28 UTC, noms de fichiers au suffixe « -v2 » du script) ; `docs/notes/g0-deux-semaines-v1/compte-rendu-e2-t06-2026-11-07-v1.md` (`5a6debc5…`) ; `docs/notes/g0-deux-semaines-v1/e3-ter-v1/ordre-e3-ter-garde-equivalence-v1-brouillon1.md` (brouillon, `69a1c969…`) ; `docs/notes/convergence-defense-v1/regles-defense-v1/` (synthèse scellée `lecture-course-regles-defense-v1.md` `24081eed…`, audits scellés `audit-r4-p12-p13-v1.md` `02a87957…` et `audit-trop-beau-course-regles-defense-v1.md` `7e81d094…`) ; `docs/notes/etat-critique-v1/etat-critique-programme-v1.md` (`b72fa381…`) ; `docs/verdicts/verdict-audit-fuite-r1-v4-v1.md` (`320463e6…`) ; `docs/verdicts/verdict-analyses-r1-r2-relance-v4-v1.md` (`dece9980…`) ; `prereg/preenregistrement-epreuve-etiqueteur-v1.md` (`f73455b8…`, l. 120, 165-186) ; `docs/programme-controle-ia-v2.md` (l. 113, 145, 213) ; `docs/procedures/brief-reprise-nouvelle-mere-2026-11-08-v2.md` (§ 4) ; **la candidature exactement envoyée le 7 octobre**, versée et scellée par la session mère à 14:40 UTC (R-1836, `registres/decisions.md` l. 1794) : `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` (texte extrait, 420 l., `b2458c2d…` ; PDF `737c482c…`) et `budget_v3_TAIF_2026-10-07.txt` (16 l., `caec18b2…` ; feuille `037765b0…`) — ce sont ces textes, et non la v16, qui disent « ce que la candidature promettait ».
- **Ce qui manque** (et marque les `<<À VÉRIFIER>>`) : l'appel et la grille du fonds — **absents du dépôt** (R-1832 l. 1790) ; aucune note d'appel : **l'appel prévu le 30 octobre a été décalé, il n'y a pas encore eu d'appel** (R-1836 l. 1794) ; la facturation réelle (consoles des fournisseurs) ; la relecture de l'étiqueteur après 14:04 UTC ; le verdict de la validation du nul v9 (non lu, cité par R-1779) ; tout ce qui vit sous `donnees/` et `diag/` (interdit). Les durées et les comptes de sessions sont des jugements de ce rédacteur, dits comme tels ; les montants en dollars renvoient à une ligne de registre ou à un devis cité.
- **Conventions** : identifiants A-n, B-n, C-n ; responsable **M** session mère, **S** sous-agent neuf, **D** développeur, **R** rédacteur, **L** Lazar ; « 8 caractères » = début de l'empreinte compagnon `.sha256` quand la pièce est scellée ; un chiffre sans chemin ni ligne n'existe pas ici.

---

## A. Questions scientifiques ouvertes

### A-1 — La trace du sabotage existe-t-elle dans les activations aux couches lues (7, 15, 23 de Llama-3.1-8B-Instruct) ?
- **Énoncé** : aucune mesure propre ne montre encore qu'un sabotage diffus laisse une trace lisible aux couches lues ; le seul test réel « intérieur contre extérieur » (R1 v4) a montré une sonde qui lit la consigne privée du saboteur, non le sabotage.
- **Déclencheur** : verdict de l'audit de fuite « Fuite (lecture de la consigne) » (`docs/verdicts/verdict-audit-fuite-r1-v4-v1.md` l. 3, 47, `320463e6…`) ; état critique : « H1 n'est pas testée », sondes génériques au niveau de directions aléatoires (`docs/notes/etat-critique-v1/etat-critique-programme-v1.md` l. 17-19, `b72fa381…`) ; la question v2 du pilier attaque scellée le 8 novembre a pour objet « chercher la trace interne du sabotage » (`docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md` l. 1, 29, `2dbad4b7…`) ; N-062 : si les sondes ne lisent pas le sabotage, on les reconçoit (`docs/decisions/decision-N-062-v1.md` l. 17, 21-22, `63f42690…`).
- **Dommage pour le jury** : « Votre seule expérience réelle montre que la sonde lit la consigne, pas le sabotage. Qu'est-ce qui vous fait croire qu'une trace existe ? »
- **Remède ≤ 7 jours** : (1) la **course de T0.6** (organisme par adaptateur à dose réglable, sans consigne au contexte, dose–réponse, test croisé) sous GO-2026-11-02-28 (`registres/go.md` l. 216 : plafond 200 USD, échéance 16 novembre ; devis v3 : A100 ≈ 17 à 27 USD, H200 NVL ≈ 43 à 74, pire cas ≈ 198, R-1764 l. 1722, R-1707 l. 1665) — c'est la première mesure propre ; verdict par lecteur neuf vers le 15-17 novembre (voir B-1) ; (2) le **bras B** (contrefactuel de contexte sur la même machine, GO-2026-11-07-04, `registres/go.md` l. 264 ; ≈ 20 minutes de carte, ≈ 0,37 USD estimés, R-1721 l. 1679) qui sépare « consigne » et « autre trace » dans R1 v4 ; (3) le collisionneur à cinq espèces et l'organisme d'idéation sur la question v2 (GO-2026-11-08-07 15 USD l. 279, GO-2026-11-08-08 20 USD l. 278 ; plafond cible du run à cinq ≤ 30 USD, R-1830) donnent des **protocoles**, pas des mesures. Sessions : 4 à 6 (ordre de la course, fille d'exécution, contre-lectures, lecteur neuf). **Phrase à dire** : « non établie, pas réfutée : le test manquait de puissance et était contaminé par la consigne ; la première mesure propre est en cours ; un échec commande la reconception, pas l'arrêt (N-062) ».
- **Dépendance** : B-1 (E3 ter → scellement de T0.6 → course → verdict R13).
- **Responsable** : M (ordre, scellement), fille d'exécution avec la clé Vast, S (verdict), L (GO E3 ter, mot dans la session qui dépense).
- **État au 8 novembre** : ouverte ; course non lancée à 14:33 UTC ; chaîne v12 « scellable » (R-1781 l. 1739), ordre de la course bloqué par E3-6 (R-1784 l. 1742).

### A-2 — Le saboteur diffus sabote-t-il réellement ? (vérité du dommage : rappel de l'oracle de couverture sur des sabotages connus)
- **Énoncé** : la vérité du dommage du mode « affaiblir les contrôles » est un oracle de couverture contre la référence cachée de l'article (N-060 v3) ; ses cinq épreuves R5 ne sont pas jouées ; l'étiqueteur en cours ne valide pas cet oracle.
- **Déclencheur** : `docs/decisions/decision-N-060-v3.md` l. 21-30 (`2b448f69…`) : « un oracle qui échoue à ses épreuves n'est pas lu » ; GO-2026-11-07-10 (`registres/go.md` l. 270) : l'oracle décide à la porte, l'étiqueteur validé est rapporté à côté ; `prereg/preenregistrement-epreuve-etiqueteur-v1.md` l. 120 (`f73455b8…`) : l'épreuve « ne valide pas l'oracle de couverture de N-060 », bras T-1 reporté ; brouillon 1 de l'audit du rappel : `prereg/audit-rappel-oracle-sabotages-connus-v1-brouillon1.md` l. 18-19 (ce qui existe), l. 100-101 (devis ≈ 55 USD attendus, plafond proposé 180 ; variante réduite ≈ 40, plafond 120).
- **Dommage pour le jury** : « Comment savez-vous que votre organisme "diffus" fait un dommage, et pas seulement qu'il a reçu l'ordre d'en faire ? Qui a validé votre vérité terrain ? »
- **Remède ≤ 7 jours** : (1) **verdict de la phase 1 de l'étiqueteur** par un lecteur neuf dès la relecture finie (lecture principale finie sans arrêt le 8 novembre à 14:04 UTC : A 389 ok / 7 illisibles = 1,77 %, B 396 / 0 ; 36,90 / 300 USD estimés, R-1827 l. 1785, `registres/depenses.md` l. 401) : 0 USD de plus, 2 sessions, 1 à 2 jours ; (2) **audit du rappel de l'oracle** : contre-lecture R2 du brouillon 1, scellement, devis, GO, lectures (variante réduite recommandée par ce rédacteur pour le coût : ≈ 40 USD attendus, plafond 120, l. 101 du brouillon), analyse par lecteur neuf : 3 à 4 jours, 3 à 4 sessions. **Phrase à dire** : « deux lecteurs d'autres familles que les moniteurs, jugés contre une vérité de construction (216 dégradations plantées), seuils gelés (rappel ≥ 0,8, fausses alertes ≤ 0,05, l. 165-186) ; l'oracle de couverture est audité à part sur des sabotages connus ».
- **Dépendance** : GO sur devis (L) ; lecteur Argon qui bloque certains items (1,77 %) ; items et clé de l'étiqueteur (lus par le seul programme).
- **Responsable** : S (contre-lecture, lecteur neuf), M (scellement, ordre), L (GO).
- **État au 8 novembre** : étiqueteur phase 1 en relecture ; oracle : brouillon 1 écrit à 13:50 UTC (R-1817 l. 1775), non contre-lu, non scellé.

### A-3 — Dans l'arène des règles de défense, la défense adaptative progresse sur les attaques vues et régresse sur les attaques tenues à l'écart ; la défense figée fait aussi bien
- **Énoncé** : course préenregistrée et scellée du 1er novembre (`prereg/preregistrement-regles-defense-convergence-v1.md`, `d82dea33…`) : HR4 « conforme pour R3 » = régression avérée de R3 sur les lois tenues à l'écart (−0,066 et −0,077 aux deux δ) ; R1 détecte **mieux** les attaques tenues à l'écart que R2 (+0,023, +0,024 ; branche opposée de P5) ; R0 (figée) ≈ R2 sur V (P13 contredite) ; audit R4 du 8 novembre : « pas d'artefact ».
- **Déclencheur** : `docs/notes/convergence-defense-v1/regles-defense-v1/lecture-course-regles-defense-v1.md` l. 97-98, 115, 127-134 (`24081eed…`) ; `audit-r4-p12-p13-v1.md` l. 3, 433 (`02a87957…`) ; `audit-trop-beau-course-regles-defense-v1.md` l. 62, 95-96 (`7e81d094…`). Les Tables B et B′ « se lisent » désormais ; la règle gelée rend HR0 « réfutée » et HR2 « non tranchée » (l. 97, 115 de la lecture) — verdict R13 d'hypothèses **non prononcé** au 8 novembre.
- **Dommage pour le jury** : « Votre règle de défense qui s'adapte ne bat pas une défense figée et régresse sur ce qu'elle n'a pas vu : pourquoi l'adaptation ? » et « c'est un jouet synthétique ; qu'en est-il sur des sondes réelles ? »
- **Remède ≤ 7 jours** : verdict R13 sur HR0, HR2, HR3 maintenant que l'audit est rendu (S, 0 USD, 1 session) ; le dire comme **résultat négatif préenregistré et audité** (c'est un argument de méthode) ; mot de Lazar du 8 novembre : « ne pas recommencer si déjà fait mais approfondir » (R-1795 (3), l. 1753). **Infaisable en une semaine** : la matrice de transfert sur les sondes réelles et le Nash sur la table croisée (demandent les sondes de T0.7 et les épisodes de T0.6) — ce qu'on dit à la place : « le jouet a montré que l'adaptation naïve surapprend les attaques vues ; la version réelle attend la course ».
- **Dépendance** : aucune pour le verdict ; T0.6 et T0.7 pour la suite.
- **Responsable** : S (verdict), M.
- **État au 8 novembre** : audit rendu à 14:06 UTC (R-1823 l. 1781) ; hypothèses non prononcées.

### A-4 — Le mode tenu à l'écart reste-t-il non vu, et combien de familles faut-il ?
- **Énoncé** : aucune famille du mode tenu à l'écart n'est scellée ; N-062 fait de « une famille tenue à l'écart neuve par cycle » une ligne de budget récurrente, et une famille lue une fois est vue.
- **Déclencheur** : `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` l. 6, 18 (`f5599896…` : brief `0a17c6bc…`, devis `55b2cbb1…`, « aucune famille scellée ») ; `docs/decisions/decision-N-062-v1.md` l. 23-24, 26 (`63f42690…`) ; N-054 point 3 (`docs/decisions/decision-N-054-v1.md`, `c8a00b3f…`, ligne `<<À VÉRIFIER>>`).
- **Dommage pour le jury** : « Qui garantit que personne n'a vu le mode tenu à l'écart ? Et une fois lu, qu'est-ce qui vous reste pour la revendication finale ? »
- **Remède ≤ 7 jours** : pas 5 du chemin critique — cinq instances neuves hébergées hors des concepteurs de moniteurs, chaque famille scellée avec sa vérité du dommage et sa déclaration « flou / net », lue par personne ; appels Argon et Kimi 2 à 8 USD (devis `55b2cbb1…`, chemin v1 l. 18), instances Claude en usage ; 3 à 6 heures ; **GO requis**. En plus, à 0 USD : une page « chaîne de garde du mode tenu à l'écart » (empreinte scellée avant conception, journal de lecture unique, hôte distinct) à montrer au jury.
- **Dépendance** : GO (L) ; retour de Fable 5.1 (limite hebdomadaire jusqu'au 10 novembre 05:00 UTC, R-1621 l. 1579) pour une des cinq instances.
- **Responsable** : M (hôte), S (instances), L (GO).
- **État au 8 novembre** : brief et devis du 5 novembre ; aucun mouvement depuis.

### A-5 — Diversité effective des moniteurs (H5) : rien n'est mesuré ; le seul juge boîte noire réel est au hasard
- **Énoncé** : H5 (« la sécurité croît avec le nombre de moniteurs seulement via la diversité effective, mesurée par une matrice de transfert d'attaque », `docs/programme-controle-ia-v2.md` l. 113 ; six axes § 8.2 l. 145 ; figure E3.3 l. 213) n'a ni panel de sondes ni matrice ; le juge de 3 milliards ne sépare pas mieux que le hasard (aire 0,523, p = 0,19 ; état critique l. 19, repère [A10]).
- **Déclencheur** : lecture du billet de Redwood Research sur la collusion des moniteurs (R-1818 l. 1776) ; axe « protocole de déploiement » non ouvert, recommandation « après G0 » (R-1829 (7), l. 1787).
- **Dommage pour le jury** : « Vous promettez une courbe sécurité(N) ; aucun panel n'existe et votre seul juge est au hasard. »
- **Remède ≤ 7 jours** : **infaisable** (demande les sondes de T0.7 et une banque) ; ce qu'on dit à la place : H5 est au papier B (mois 4,5 à 6 de la candidature, `livrables/registres-taif-v3/promis-livre-v2.md` ligne C7-4) ; la base boîte noire plus forte est T0.8 (critère 4) ; le protocole de mesure existe (§ 8.2), la mesure non. À 0 USD : la Table E de l'arène (lois tenues à l'écart) comme illustration de méthode, jamais comme mesure sur des modèles.
- **Dépendance** : T0.7, T0.8, banque de G1.
- **Responsable** : M (texte), L (ordre des priorités).
- **État au 8 novembre** : ouverte, hors du chemin d'ici l'entretien.

### A-6 — La base boîte noire à battre : rien n'existe pour T0.8, et un prédicteur sur les traits du texte atteint déjà 0,866
- **Énoncé** : le critère 4 de G0 n'a aucun brouillon (chemin v1 l. 22 ; dernière mention au registre : « T0.8 n'a aucun brouillon », `registres/decisions.md` l. 1539) ; la page publique du 8 novembre dit « prédicteur sur le texte à 0,866 » (R-1773 l. 1731) ; la règle « mots et coût » (GO-2026-11-07-03, `registres/go.md` l. 263) ne juge la lecture interne que là où la base échoue.
- **Dommage pour le jury** : « Un prédicteur sur le texte fait 0,866 ; pourquoi lire l'intérieur ? Contre quoi comparez-vous ? »
- **Remède ≤ 7 jours** : brouillon 1 de T0.8 (R, 1 jour, 0 USD) et contre-lecture (S, 1 jour) ; dire que la règle (b) est écrite d'avance (la boîte blanche n'est créditée que là où la meilleure base boîte noire échoue). **Si 8 à 14 jours** : course de T0.8 sur les épisodes de T0.6 (ordre de grandeur ≈ 20 à 60 USD, chemin v1 l. 22, non opposable) et verdict du critère 4 avant l'entretien — serré (voir B-3).
- **Dépendance** : épisodes de T0.6 ; invites H.12 dérivées (faites) ; devis et GO.
- **Responsable** : R, S, M, L.
- **État au 8 novembre** : rien n'existe.

### A-7 — Puissance : à quelle taille le programme devient-il concluant, et combien cela coûte-t-il ?
- **Énoncé** : les tests menés sont sous-puissants ou contaminés (« non établie » plutôt que « réfutée », question de Lazar R-1717 (3), l. 1675) ; G1 exige au moins 288 unités d'épreuve par mode (v16 § 4 l. 934-935) ; la garde δ v10 n'est pas simulée ; la puissance de T0.6 est écrite (aire minimale détectable à 80 % sur 64 tâches ≈ 0,60 à 0,66, R-1584 l. 1542).
- **Pièce** : `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 932-938 (`186173d9…`) ; chemin v1 l. 15, 50.
- **Dommage pour le jury** : « Vos tests sont sous-puissants ; quelle taille, quel coût, et qu'avez-vous appris d'un test sans puissance ? »
- **Remède ≤ 7 jours** : simulation de la garde δ v10 sur processeur (pas 2 du chemin : 4 à 8 heures de calcul, 0 USD, 1 à 2 sessions) ; une page « puissance par expérience » qui aligne T0.6, étiqueteur (annexe B, l. 186 du préenregistrement) et G1 (288 unités ; plafond de campagne 6 331 USD, GO-2026-11-05-07, `registres/go.md` l. 255).
- **Dépendance** : aucune.
- **Responsable** : S, M.
- **État au 8 novembre** : garde δ v10 à lancer ; rien depuis le 5 novembre.

---

## B. Goulots de programme (chemin critique vers G0 et G1)

### B-1 — La course de T0.6 (critère 2, et 3 par le test croisé) n'a pas tourné : l'ordre de la course est bloqué par E3-6
- **Énoncé** : la chaîne v12 est « scellable » (R-1781 l. 1739) mais l'ordre de la course est bloqué par le point E3-6 (garde d'équivalence jamais exercée à E3 bis : 0 action contrôlée dans les six états, R-1769 l. 1727) ; Lazar a choisi l'option (b), un galop d'essai E3 ter (R-1824 l. 1782) ; brouillon 1 de l'ordre reçu à 14:27 UTC, en contre-lecture (R-1833 l. 1791).
- **Déclencheur** : `docs/notes/g0-deux-semaines-v1/e3-ter-v1/ordre-e3-ter-garde-equivalence-v1-brouillon1.md` l. 4, 9 (probabilité 0,44 qu'aucune action ne soit tirée à E3 bis : pas un défaut de code), l. 89-99 (devis : attendu ≈ 7 USD, pire ≈ 14, plafond proposé 15) ; course visée « le 11 novembre » (R-1770 l. 1728 : « lance les courses du 11 nov now ») ; **dernier jour de création le 15 novembre** (L11, R-1623 l. 1581) ; **échéance du GO le 16 novembre** (`registres/go.md` l. 216) ; carte : A100 SXM4 de 80 Go rare (1 à 4 offres conformes selon l'heure, 1,13 à 2,07 USD/h, R-1696 l. 1654, R-1755 l. 1713), repli H200 NVL après 3 heures de recherche (GO-2026-11-07-02 l. 262) ; suite ciblée de 1 878 essais en 67 minutes sur la carte (R-1762 l. 1720).
- **Dommage pour le jury** : « Votre première mesure propre n'a pas encore tourné ; G0 est due dans trois semaines. »
- **Remède ≤ 7 jours** : 9 novembre : contre-lecture, scellement et GO d'E3 ter, galop (≈ 7 USD, plafond 15) ; 10 novembre : règlement d'E3-6 au registre, remplissage de l'ordre, seconde contre-lecture, scellement du candidat 12 ; **11 à 13 novembre : création de la course** (A100 ≈ 17 à 27 USD ; H200 NVL ≈ 43 à 74 ; plafond 200 accordé) ; sortie scellée avant lecture ; verdict R13 des critères 2 et 3 vers le 15-17 novembre. Sessions : 5 à 7.
- **Dépendance** : GO d'E3 ter sur devis (L) ; mot de Lazar dans la session de la fille qui loue (contrôle de permissions par session, R-1751 et R-1752 l. 1709-1710) ; marché des cartes.
- **Responsable** : M, fille d'exécution (clé Vast), S (contre-lectures, verdict), L.
- **État au 8 novembre** : bloqué ; épreuves E2, E3, E3 bis faites (5,744 USD cumulés, `registres/depenses.md` l. 390 ; E2 0,627, E3 1,465 l. 387, E3 bis 3,652) ; onze versions du lanceur et dix de l'amorce en quatre jours.

### B-2 — Le scellement de T0.7 (critère 3) attend : jeux prêts, texte au brouillon 6, découplé de T0.6
- **Énoncé** : brouillon 6 de T0.7 en mode « coût » rendu le 5 novembre (`brouillons/T0.7-sondes-v0-v1-brouillon6.md` `29f0ab43…`, R-1584 l. 1542) ; trois jeux synthétiques écrits sur les 32 tâches de réserve, contrôles conformes, contre-vérification à l'aveugle faite (R-1675 l. 1633) ; réserve R4 : l'aire du sac de mots monte avec le nombre de tâches (0,745 à 8 tâches, 0,813 à 30 ; 0,818 à 32 : fuite lexicale résiduelle à trancher avant scellement, R-1641 l. 1599) ; T0.6 se scelle seul, les états des sondes ne sont lus qu'après le scellement de T0.7 et de P3-bis (R-1654 l. 1612) ; la lecture de T0.7 « ne commence pas avant son scellement, après le retour de Fable » (10 novembre).
- **Dommage pour le jury** : « Vos sondes sont-elles préenregistrées avant d'être lues ? » — oui par construction (garde DT-4), mais tant que T0.7 n'est pas scellé, le critère 3 ne peut pas être lu sur la course.
- **Remède ≤ 7 jours** : brouillon 7 (règle du seuil à taille fixée ou réécriture des paires : décision de routine), contre-lecture R2 par un autre modèle (N-052), scellement `prereg/T0.7-…-v1.md` les 10-12 novembre ; même chemin pour P3-bis (marqueur `<<EMPREINTE_PREREG_P3BIS>>` non scellé, R-1650 l. 1608) ; 0 USD ; 3 à 4 sessions.
- **Dépendance** : aucune dépense ; disponibilité des sessions après le 10 novembre.
- **Responsable** : R, S, M.
- **État au 8 novembre** : non scellé ; aucun mouvement depuis le 7 novembre.

### B-3 — T0.8 (critère 4) : rien n'existe
- **Énoncé** : ni brouillon ni devis ; dépend des épisodes de T0.6 ; devis à écrire (≈ 20 à 60 USD, chemin v1 l. 22, non opposable).
- **Dommage pour le jury** : voir A-6 ; pour le programme : W21 (table de dépendance v7) exige le verdict du critère 4 avant le scellement de G1 (chemin v1 l. 5).
- **Remède ≤ 7 jours** : brouillon 1 (R, 1 jour), contre-lecture (S, 1 jour), scellement ; devis et GO ; course dès que les épisodes de T0.6 sont scellés (≈ 1 jour de carte : juge 8B ≈ 58 s par épisode, chemin v1 l. 22). **Si 8 à 14 jours** : verdict du critère 4 vers le 19-21 novembre.
- **Dépendance** : B-1 (épisodes) ; GO (L).
- **Responsable** : R, S, M, lecteur neuf, L.
- **État au 8 novembre** : rien.

### B-4 — Le banc neuf de ≈ 480 tâches pour G1 n'est pas lancé (reporté au 10 novembre)
- **Énoncé** : ≈ 1 000 à 1 200 passages de sous-agents, 2 à 5 jours de calendrier, usage de sessions lourd ; **reporté au retour de Fable (10 novembre, 05:00 UTC)** pour ne pas épuiser la limite d'Opus dont dépend la mère (R-1624 l. 1582) ; sans lui, G1 est « non jugeable par puissance » par construction (DG1-1, chemin v1 l. 50).
- **Dommage pour le jury** : « Votre banc d'épreuve pour G1 n'existe pas ; votre banc actuel est consommé (96 tâches, toutes vues). »
- **Remède ≤ 7 jours** : lancer le 10 novembre par lots de 5 à 10, compteur journalier ; si le 20 novembre le compte est partiel, sceller G1 avec la liste partielle vérifiée et le nombre réel (n_h ≥ 288, chemin v1 l. 50). 0 USD ; usage : le poste le plus lourd en sessions.
- **Dépendance** : quotas des comptes (Fable épuisé jusqu'au 10 novembre ; alerte Opus le 6, R-1639 l. 1597) ; réseau vers arXiv.
- **Responsable** : M, S (par lots).
- **État au 8 novembre** : non lancé.

### B-5 — Le scellement du préenregistrement de G1 (critère 6) : brouillon 6, dix-neuf marqueurs, aucun pas lancé depuis le 5 novembre
- **Énoncé** : brouillon 6 (`939b56e5…`, R-1581 l. 1539) avec 13 décisions prises (GO-2026-11-05-07, `registres/go.md` l. 255) ; les pas 1 (contre-lecture R2), 2 (garde δ v10), 4 (portage du juge du pari apparié dans `src/controle_ia/`), 6 (vérification R7 de DeLong et Obuchowski), 11 (recette d'HELIOS) n'ont aucune ligne au registre depuis le 5 novembre (grep de R-1580 à R-1834 : aucune occurrence) ; **D:3 tranché (2)** le 6 novembre : le pilote de la couche 2 ne bloque plus le scellement (R-1624 l. 1582 ; `registres/etat.md` l. 352).
- **Dommage pour le jury** : « Vous dites "préenregistré" ; le préenregistrement de la porte décisive est un brouillon. »
- **Remède ≤ 7 jours** : lancer les pas 1, 2, 4, 6 (0 USD, 4 à 5 sessions) ; demander à Lazar si W21 tient (le critère 6 lu par la grille v8 l. 920-940 n'exige pas les verdicts 2, 3, 4 ; seule la table v7 l'exige, chemin v1 l. 49) — nœud `<<À VÉRIFIER : posé ou non à Lazar depuis le 5 novembre ; aucune ligne trouvée>>`.
- **Dépendance** : B-1 à B-4 (marqueurs) ; A-4 (mode tenu à l'écart) ; A-2 (oracle).
- **Responsable** : S, D, M, L.
- **État au 8 novembre** : brouillon 6 ; aucun mouvement.

### B-6 — Le verdict de G0 : fin novembre, 2 critères sur 8, grille v8 non scellée, aucune règle de repli écrite
- **Énoncé** : G0 au plus tard fin novembre 2026 (N-027, `CLAUDE.md`) ; verdict scellé avant le 30 novembre 23:59 UTC, sinon report unique au 31 janvier 2027 (chemin v1 l. 4) ; critères prouvés : 1 et 5 ; « reste » : 2, 3, 4, 6, 7, 8 (`livrables/registres-taif-v3/promis-livre-v2.md` lignes G0-1 à G0-8 et C6-G0) ; grille de lecture v8 encore un brouillon (chemin v1 l. 29) ; « aucune règle de repli écrite » si G0 échoue (v16 « Points à trancher » pt 12, l. 1444-1445 ; « Questions qu'un évaluateur poserait » pt 3, l. 1478-1479).
- **Dommage pour le jury** : « G0 était promise au 1er novembre ; elle est à 2 sur 8 ; quelle probabilité pour fin novembre, et que faites-vous si elle échoue ? »
- **Remède ≤ 7 jours** : sceller la grille v8 (S, 0 USD) ; table promis → livré à jour (faite, v3) ; une phrase de repli écrite par Lazar (nœud) ; sinon dire tel quel « no fallback rule is written yet ».
- **Dépendance** : L (règle de repli).
- **Responsable** : S, M, L.
- **État au 8 novembre** : 2 sur 8.

### B-7 — L'oracle de couverture (N-060 v3) : aucune conception scellée par une instance neuve ; lectures au pilote 100 à 250 USD
- **Énoncé** : pas 10 du chemin (chemin v1 l. 23) : conception scellée par une instance qui n'a vu aucun interne de moniteur ; deux lecteurs hors Llama et Qwen ; épreuves R5 ; vérification que l'agent ne voit pas `cibles` (garde `tests/test_cibles_invisibles_v1.py`, 21 essais sur `main`, R-1679 l. 1637) ; le brouillon 1 de l'audit du rappel (A-2) couvre les épreuves, pas la conception scellée.
- **Dommage pour le jury** : « Votre vérité terrain n'est pas encore conçue ; comment avez-vous choisi vos doses ? »
- **Remède ≤ 7 jours** : conception par une instance neuve (1 jour, 0 USD) ; épreuves négatives (autre référence, plan tronqué) dans l'audit de A-2 ; lectures complètes au pilote **hors** de la semaine (100 à 250 USD).
- **Dépendance** : épisodes honnêtes de T0.6 pour les épreuves (B-1) ; GO (L).
- **Responsable** : instance neuve, M, L.
- **État au 8 novembre** : non conçu ; module d'artefacts existant (`src/controle_ia/verite_dommage/artefacts_v1.py`, chemin v1 l. 6).

### B-8 — Le mode tenu à l'écart : aucune famille scellée (voir A-4)
- **Énoncé** : pas 5 du chemin ; 2 à 8 USD d'appels ; GO requis ; N-062 en fait une ligne de budget par cycle.
- **Remède ≤ 7 jours** : voir A-4. **Responsable** : M, S, L. **État** : aucune famille.

### B-9 — Ressources : une personne, des quotas de sessions, une carte à la fois, des fournisseurs qui refusent ou bloquent, des permissions par session
- **Énoncé** : Fable 5.1 épuisé jusqu'au 10 novembre 05:00 UTC, filles 7 et 8 hors service (R-1621 l. 1579) ; limite hebdomadaire d'Opus en alerte le 6 (R-1639 l. 1597) ; cinq redémarrages du conteneur de la mère le 5 novembre (R-1601 l. 1559) ; relais de comptes les 7 et 8 novembre (`registres/etat.md` l. 377-399) ; A100 SXM4 de 80 Go : 1 à 4 offres (B-1) ; Argon bloque 1,77 % des items (R-1827 l. 1785) ; Fable refusée « bio » puis « cyber » au collisionneur v1 (R-1789 l. 1747), Opus refus « cyber » sur la question v2 (R-1826 l. 1784) ; **chaque session qui dépense exige le mot écrit de Lazar dans cette session** (R-1751 et R-1752 l. 1709-1710 ; GO-2026-11-08-05 l. 276).
- **Dommage pour le jury** : « Un programme à une personne, dépendant de quotas et de refus de modèles : quelle robustesse, quelle réplicabilité ? »
- **Remède ≤ 7 jours** : écrire le calendrier des quotas et la file d'attente des tâches (chemin critique de G0 d'abord ; 0 USD, 1 session) ; dire au jury que c'est un risque géré par écrit (pauses R-1639, passations scellées, deux comptes).
- **Dépendance** : aucune.
- **Responsable** : M, L (arbitrage).
- **État au 8 novembre** : risque vivant.

### B-10 — Arbitrage des priorités de la semaine : le chemin critique de G0 et le pilier attaque se disputent la même session mère
- **Énoncé** : du 9 au 15 novembre se superposent : E3 ter et la course de T0.6 (B-1), T0.7 (B-2), T0.8 (B-3), le banc (B-4), le collisionneur à cinq espèces (≤ 30 USD, R-1830 l. 1788), l'organisme v1 et v1 bis sur la question v1 (GO-2026-11-08-08, 20 USD, l. 278 ; R-1831 l. 1789), la plus petite course réelle de l'organisme (GO-2026-11-08-02, 45 USD, l. 273), l'étiqueteur (phase 1 puis verdict), le dossier d'intégration et la v17 du programme d'entretien.
- **Dommage pour le jury** : voir C-8 (dispersion) ; pour le programme : glissement de la course au-delà du 15 novembre, donc GO neuf (nœud) et chaîne décalée.
- **Remède ≤ 7 jours** : Lazar tranche l'ordre (nœud proposé ici) ; recommandation de ce rédacteur : (1) B-1, (2) B-2 et B-3 en parallèle, (3) B-4 dès le 10, (4) pilier attaque dans ce qui reste de sessions ; confiance 0,6.
- **Responsable** : L, M.
- **État au 8 novembre** : non tranché.

### B-11 — Échéances croisées (rappel, sans remède propre)
- G0 : 30 novembre 23:59 UTC. Course de T0.6 : création au plus tard le 15 novembre (L11), GO jusqu'au 16 (`registres/go.md` l. 216). E3 bis : GO jusqu'au 12 (l. 268). Étiqueteur : GO 300 USD (l. 267). Organisme : GO 45 USD jusqu'au 30 novembre (l. 273). Fable : retour le 10 novembre 05:00 UTC. Entretien : vers le 22 novembre, jour exact à confirmer (R-1834 l. 1792).

---

## C. Risques de crédibilité du récit devant le jury

### C-1 — « Compute spent: about $20 » dans la candidature, contre un relevé strict de 645,42 USD, qui est un plancher
- **Énoncé** : la candidature envoyée le 7 octobre déclare « Compute spent: about $20 » (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 283, `b2458c2d…` ; repris en `livrables/registres-taif-v3/promis-livre-v2.md`, ligne C6-7) et demande **58 630 USD** (ligne principale, papiers C et A, 7 mois ; fourchette 28 160 minimal à 138 600 ambitieux ; l. 7, 388), dont carte graphique et stockage **1 200 / 4 000 / 12 000 USD** selon le scénario (l. 381 ; `budget_v3_TAIF_2026-10-07.txt` l. 7, `caec18b2…`) et outillage d'agents de code et d'interface de programmation **4 000 / 7 000 / 12 000** (budget l. 8) ; le total relevé strict de la phase 0 au 8 novembre est **645,42 USD** (136 lignes sommées), **plancher** : 185 lignes au journal non sommées et 49 lignes estimées à part (111,85 USD) (`livrables/registres-taif-v3/total-depenses-v2.md` l. 9-12, 152, `8e6a1c01…`) ; la proposition de recherche brouillon 1 écrit « ≈ 1 000 USD » (§ 8, l. 46) ; la v16 disait « ≈ 525 », « ≈ 531 », « a few hundred dollars » (l. 1334-1352) ; la facturation réelle n'est pas rapprochée (v16 l. 1508).
- **Déclencheur** : toute question sur le budget ; la ligne « about $20 » est dans le texte envoyé.
- **Dommage pour le jury** : « Vous avez écrit 20 dollars et dépensé plus de 600 en un mois, sans savoir combien exactement ; votre ligne "AI research tooling" est de 1 000 dollars par mois (budget l. 8) : comment tiendrez-vous 58 630 dollars sur sept mois ? »
- **Remède ≤ 7 jours** : (1) ventilation par poste (carte graphique, appels de modèles par fournisseur, par GO) depuis `total-depenses-v2.md` et `cout-par-resultat-v2.md`, rapprochée ligne à ligne des deux lignes du budget envoyé (carte graphique 4 000 ; outillage 7 000 en ligne principale) (S, 0 USD, 1 session) ; (2) **rapprochement avec la facturation réelle = geste de Lazar** (consoles Vast, Google, Anthropic, Moonshot, OpenAI) ; (3) phrase gelée : « "about $20" était la carte graphique au 7 octobre ; depuis, le registre relève au moins 645 dollars, surtout en appels de modèles pour l'idéation multi-modèles et les pilotes, chaque ligne sous un plafond autorisé sauf l'incident du 23 octobre ; le total exact attend le rapprochement ». **Ne jamais présenter 645,42 comme le total.**
- **Dépendance** : L (consoles).
- **Responsable** : S, L.
- **État au 8 novembre** : tables v3 régénérées à 14:28 UTC ; facturation non rapprochée.

### C-2 — G0 promise au 1er novembre en interne, reportée à fin novembre, à 2 critères sur 8 ; la candidature envoyée dit « décembre 2026 »
- **Énoncé** : **la candidature envoyée** écrit « Gate G0 (at the start of the grant, December 2026) still requires organisms with a dose–response, probes above the random floor, a running black-box baseline, sealed and counter-read pre-registrations of G1 and Paper C, and the closing of the literature check » et « Month 1, Dec 2026 : Close G0 » (`proposal_v2_TAIF_2026-10-07.txt` l. 284-285, 289, `b2458c2d…`) ; la date du 1er novembre est celle du programme interne (N-017, `registres/etat.md` l. 185) et de la version v1 de la proposition reprise par `promis-livre-v2.md` (ligne C6-G0 : « Gate G0 (1 November 2026) ») ; N-027 l'a portée à fin novembre ; la page publique du 8 novembre dit « porte G0 : 2 critères sur 8, due fin novembre » (R-1773 l. 1731) ; la v16 corrigeait « deux sur sept » en « deux sur huit » (l. 889-890). Devant le fonds, le report est donc **interne** ; le risque est l'écart visible entre le dépôt public (« 1er novembre » puis « fin novembre ») et le texte envoyé (« décembre »), et le compte de 2 sur 8 à trois semaines de la date.
- **Dommage pour le jury** : « Votre dépôt public et votre candidature ne disent pas la même date pour G0 ; et à 2 critères sur 8, la fermez-vous en décembre ? »
- **Remède ≤ 7 jours** : dire la cause par pièces (fuite de la sonde sur R1 v4 → organisme sans consigne au contexte ; onze versions du lanceur, épreuves E2, E3, E3 bis à 5,744 USD) ; table promis → livré v3 ; règle de repli (B-6). 0 USD, 1 session.
- **Dépendance** : L (règle de repli).
- **Responsable** : M, L.
- **État au 8 novembre** : 2 sur 8.

### C-3 — G1 « fin du mois 4 » dans la candidature contre « fin M2 » dans le programme ; et N-062 supprime la bascule « résultat négatif publié » : ce qui tient lieu de borne
- **Énoncé** : **la candidature envoyée** place G1 « end of month 4 » et écrit « If G1 fails, the negative result is published, and construct validity (H8) becomes the main line » (`proposal_v2_TAIF_2026-10-07.txt` l. 110, 159-162 ; tableau des bascules l. 323-324, `b2458c2d…`) ; le programme interne dit « G1 et GC en fin de M2 » (écart signalé en v16 § 9 pt 3 l. 1278-1280 ; § 11 pt 7 l. 1369 : « dire la version envoyée, elle fait foi devant le fonds ») ; N-062 (`docs/decisions/decision-N-062-v1.md`, `63f42690…`) remplace l'issue « échouée → résultat négatif publié + H8 dominante » par un cycle de reconception **sans borne de cycles** (l. 24) ; **ce qui tient lieu de borne** (l. 24-26) : le GO par cycle (devis, plafond, ligne de GO), la disponibilité d'une famille tenue à l'écart neuve à usage unique, le calendrier du programme ; contre « courir jusqu'au signe positif » (R3) : famille neuve par lecture, aucune sélection sur le tenu à l'écart, tous les cycles rapportés avec leur nombre à côté de la revendication, préenregistrement court et lecteur neuf par cycle ; la bascule du brief reste écrite comme issue possible à la main de Lazar (l. 26). La proposition de recherche brouillon 1 (§ 4 l. 32, § 9 l. 49) dit encore « borne de cycles et de budget écrite d'avance » : **périmée** sur ce point.
- **Dommage pour le jury** : « Sans borne, c'est courir jusqu'au résultat positif » ; « la version envoyée dit résultat négatif publié : laquelle fait foi ? »
- **Remède ≤ 7 jours** : une page « ce qui tient lieu de borne » (texte de N-062 l. 24-26, plus la ligne de budget « une famille tenue à l'écart par cycle » chiffrée depuis le devis `55b2cbb1…`, 2 à 8 USD l'étape 1) ; brouillon 2 de la proposition (§ 4, § 9) ; phrase : « la version envoyée fait foi ; l'écart est déclaré ; la décision est écrite et scellée avant tout résultat ». 0 USD, 1 à 2 sessions (R, S).
- **Dépendance** : aucune.
- **Responsable** : R, M.
- **État au 8 novembre** : N-062 scellée à 13:43 UTC (R-1815 l. 1773) ; proposition brouillon 1 périmée.

### C-4 — Refus de modèles au collisionneur : fréquence non comptée, pratique de la « question resserrée »
- **Énoncé** : au 8 novembre, Fable refusée deux fois (« bio », « cyber ») au collisionneur v1 du pilier attaque et retirée du run (R-1789 l. 1747, R-1792 l. 1750) ; Opus 5.5 refuse la question v2 (« cyber », R-1826 l. 1784) ; Lazar : « si fable refuse resserre pour lui la question » (R-1830 l. 1788 ; pratique R-609, question étroite scellée à part) ; le dénominateur des refus n'est pas compté (v16 l. 1473, 1392-1396, 1498-1500).
- **Dommage pour le jury** : « Vos propres outils refusent vos questions de sécurité : êtes-vous du mauvais côté ? Avez-vous contourné ? »
- **Remède ≤ 7 jours** : compter le dénominateur par script sur les journaux des runs (tours lancés, cellules refusées, par modèle et par catégorie ; S, 0 USD, 1 session) ; phrase : « refus consignés, jamais contournés, garde de refus qui ferme le tour (code 2), question étroite scellée séparément et dite dans la synthèse ».
- **Dépendance** : accès aux journaux des runs (hors `donnees/` pour ce rédacteur).
- **Responsable** : S, M.
- **État au 8 novembre** : non compté.

### C-5 — Les chiffres exploratoires du collisionneur et de l'organisme d'idéation ne doivent jamais être cités comme mesures
- **Énoncé** : règle de la v16 § 10 pt 5 (l. 1311-1314) : « on ne cite pas ses chiffres comme mesures » (puissance annoncée 0,65-0,80 qui valait 0,33, R-665) ; la semaine ajoute un run à cinq espèces, un organisme v1 et v1 bis, un tour critique prévu avec témoins plantés (R-1832 (e), l. 1790).
- **Dommage pour le jury** : un chiffre de synthèse pris pour une mesure, démenti en séance.
- **Remède ≤ 7 jours** : règle écrite dans le dossier d'intégration et la v17 ; témoins plantés et rappel mesuré au tour critique ; relecture de la v17 par un lecteur neuf avec la consigne « aucun chiffre du collisionneur ». 0 USD.
- **Responsable** : R, S.
- **État au 8 novembre** : règle écrite dans la v16, à reporter.

### C-6 — L'incident des clés d'octobre et les treize instances du 23 octobre
- **Énoncé** : clés collées en clair les 27 et 28 octobre, « toujours à révoquer » (v16 § 11 pt 9 l. 1382 ; pt 9 des points à trancher l. 1432-1433) ; « rotation des clés à faire » (R-1539, R-1540, cités l. 1571 et 1581) ; rotation de la clé d'Argon **close sans rotation** sur le mot « utilise la clé existante pour argon » (R-1723 l. 1681) ; « rotation des secrets » dans les nœuds en attente du 5 novembre (`registres/etat.md` l. 341) ; treize instances louées sans GO par la relève du 23 octobre, jamais relues sur la console (v16 l. 1341-1343 ; état critique l. 21).
- **Dommage pour le jury** : « Vous avez exposé des clés et loué treize machines sans autorisation : comment contrôlez-vous vos agents ? »
- **Remède ≤ 7 jours** : révocation et rotation = **geste de Lazar** (consoles) ; état écrit « révoquées le … » ; lecture de la facturation du 23 octobre (L) ; phrase de la v16 (forme (a) de CL3-01 : détection, quarantaine, audit, R-327) ; sans révocation : « exposed in a working thread; revocation is scheduled ».
- **Dépendance** : L.
- **Responsable** : L, M (état écrit).
- **État au 8 novembre** : aucune ligne de révocation trouvée de R-1580 à R-1834 `<<À VÉRIFIER : révocation faite hors registre ?>>`.

### C-7 — Erreurs reconnues : la liste de la v16 (§ 11 pt 9) s'est allongée depuis le 29 octobre
- **Énoncé** : v16 l. 1373-1387 (liste du 28-29 octobre) ; depuis : « E2 a coûté 0,600 » écrit sur un relevé partiel, total facturé 0,627 (R-1711 l. 1669) ; heures d'en-tête non relevées par `date -u` (R-1716 l. 1674, R-1698 l. 1656) ; devis de l'étiqueteur annoncé à Lazar à 25-40 au lieu de 4 250 à 11 700 euros avec annotation humaine (R-1722 l. 1680) ; plafond d'E3 porté sans la marge du forfait de téléchargement (R-1712 l. 1670) ; cinquième empreinte caduque dans le candidat 12 (M1, R-1784 l. 1742).
- **Dommage pour le jury** : découvertes en séance, elles passent pour cachées ; dites d'avance, elles sont une culture d'audit (R4).
- **Remède ≤ 7 jours** : liste à jour depuis le 29 octobre, chaque ligne avec son R-… (S, 0 USD, 1 session) ; une phrase.
- **Responsable** : S, R.
- **État au 8 novembre** : non compilée.

### C-8 — Dispersion apparente d'un programme à une personne : pôle, collisionneur, organisme d'idéation, arène, étiqueteur, SPARKS, attaque A1-v3, R1 v4, T0.6
- **Énoncé** : l'en-tête de `registres/etat.md` (l. 3) et le bilan R-1829 (l. 1787) montrent, le même jour, l'étiqueteur, le collisionneur v2, l'organisme v1, N-062, E3 ter, l'audit de l'arène, la proposition de recherche ; l'organisme d'idéation a une brèche (W2 : 42 des 48 lois promues sont la loi du monde, R-1768 l. 1726) et un nul v9 à « puissance perdue » (R-1779 l. 1737) ; aucune porte franchie (promis-livre).
- **Dommage pour le jury** : « Vous faites dix choses ; aucune porte franchie ; qu'est-ce qui est le programme, et où va l'argent ? »
- **Remède ≤ 7 jours** : matrice de traçabilité promesses × activités sourcée (sous-agent A, R-1832 (a)) ; une page « cœur / instruments / explorations » avec le coût par ligne depuis `livrables/registres-taif-v3/cout-par-resultat-v2.md` ; **ce qu'on gèle d'ici l'entretien** : nœud de Lazar (B-10). 0 USD, 2 sessions.
- **Dépendance** : L.
- **Responsable** : S, M, L.
- **État au 8 novembre** : matrice en cours (sous-agent A).

### C-9 — L'appel et la grille du fonds restent absents du dépôt ; la candidature et le budget v3 y sont depuis le 8 novembre 14:40 UTC ; l'appel prévu le 30 octobre a été décalé
- **Énoncé** : R-1832 (l. 1790) demandait à Lazar la candidature, le budget v3, l'appel et la grille, et des « notes de l'appel du 30 octobre » ; R-1836 (l. 1794) : la candidature exactement envoyée (`proposal_v2_TAIF_2026-10-07.pdf` `737c482c…`, texte `b2458c2d…`) et le budget v3 (`037765b0…`, texte `caec18b2…`) sont versés et scellés sous `docs/sources/candidature-taif-2026-10-07/` ; « il n'y a pas eu encore d'appel, il a été décalé » : aucune note n'existe ; **l'appel et la grille du fonds manquent toujours**. La v16 (l. 1418-1421) préparait une demande à 176 550 ou 86 130 USD : ce ne sont pas les chiffres envoyés (58 630 ; fourchette 28 160 à 138 600, proposition l. 7, 388).
- **Dommage pour le jury** : réponses hors grille ; chiffres de la demande dits de mémoire (v16) et non ceux du texte envoyé.
- **Remède ≤ 7 jours** : Lazar verse l'appel et la grille s'il les a (0 USD, geste) ; toute pièce de l'entretien cite désormais le texte envoyé (`b2458c2d…`) ; relire la v16 contre ce texte (S, 0 USD, 1 session).
- **Dépendance** : L.
- **Responsable** : L, S, M.
- **État au 8 novembre** : candidature et budget présents ; appel et grille absents ; aucun appel encore tenu.

### C-10 — Les « trois faiblesses » et le mot « quitte à prendre un modèle plus gros et à scaler »
- **Énoncé** : Lazar le 8 novembre : corriger les trois faiblesses (sonde qui lit la consigne, sondes génériques au niveau du hasard, juge de 3 milliards au hasard), « quitte à prendre un modèle plus gros et à scaler » (R-1770 l. 1728) ; « accord sur la reformulation des trois faiblesses » est un nœud ouvert (`registres/etat.md` l. 167 ; brief v2 § 4) ; changer de modèle est un interdit sans GO (`CLAUDE.md`).
- **Dommage pour le jury** : « Vous changez de modèle quand ça ne marche pas ? » (R3 : courir vers un signe positif) ; et « ces trois faiblesses, c'est le cœur de votre hypothèse ».
- **Remède ≤ 7 jours** : écrire les trois faiblesses avec leurs remèdes **déjà préenregistrés** (organisme sans consigne au contexte = T0.6 ; sondes d'intention et jeux appariés = T0.7 ; base boîte noire plus forte = T0.8) ; tout changement de modèle = nœud, devis, GO, après G0 ; phrase : « nous les avons trouvées nous-mêmes, par audit préenregistré ». 0 USD, 1 session.
- **Dépendance** : accord de Lazar sur la reformulation (nœud).
- **Responsable** : R, L.
- **État au 8 novembre** : reformulation non accordée.

### C-11 — Le dépôt des empreintes sur l'Open Science Framework est privé et non gelé : la preuve d'antériorité n'est pas encore opposable à un tiers
- **Énoncé** : projet privé `dr57c`, 118 fichiers scellés déposés le 5 novembre à 16:20:34 UTC (R-1580 l. 1538), empreintes de l'étiqueteur déposées le 8 novembre à 05:54:40 UTC (R-1757 l. 1715) ; **nœud de Lazar** : rendre le projet public et le geler (« registration »), « seule forme qui prouve la date à un tiers » (R-1580) ; R-1832 (f) : dépôt avant l'entretien.
- **Dommage pour le jury** : « Vos préenregistrements sont-ils vérifiables par nous ? » — pas tant que le projet est privé.
- **Remède ≤ 7 jours** : passage en public et gel = geste de Lazar (0 USD) ; redéposer le manifeste à jour avant (script `scripts/osf_depot_v1.py`, idempotent, 0 USD, 1 session).
- **Dépendance** : L.
- **Responsable** : L, M.
- **État au 8 novembre** : privé, non gelé.

### C-12 — Le programme d'entretien v16 est périmé et non contre-lu ; les listes ouvertes du 29 octobre, point par point
- **Énoncé** : la v16 date du 29 octobre, écrite pour un appel **prévu le 30 octobre, décalé** (aucun appel n'a encore eu lieu, R-1836 l. 1794) ; elle n'est pas contre-lue (R-1832 l. 1790 ; v16 § 11 pt 12 l. 1397-1401). Sort de ses listes ouvertes au 8 novembre :
  - **« Points à trancher par Lazar » (l. 1405-1454)** : 1 texte qui fait foi — **périmé** (v17 à écrire) ; 2 comment dire les refus — **ouvert**, à mettre à jour (C-4) ; 3 la demande (176 550 / 86 130 / paliers) — **périmé** : le texte envoyé demande 58 630 USD, fourchette 28 160 à 138 600 (`proposal_v2_TAIF_2026-10-07.txt` l. 7, 388) ; dire ces chiffres-là ; 4 « about a hundred dollars of GPU » — **périmé** (cartes ≈ 130 selon la proposition de recherche § 8 l. 46 ; à recompter depuis `total-depenses-v2.md`, `<<À VÉRIFIER : part carte graphique dans la table par GO>>`) ; 5 incident de la relève du 23 octobre — **ouvert** (C-6) ; 6 les deux résultats négatifs (juges, garde) — **clos**, s'y ajoutent l'arène (A-3) et la fuite (A-1) ; 7 heure et fuseau de l'appel — **périmé** (appel du 30 octobre décalé ; date de l'entretien à confirmer) ; 8 état de T0 à T5 — **clos** (registres) ; 9 clés exposées — **ouvert** (C-6) ; 10 et 15 course d'idéation du 29 octobre — **périmés**, remplacés par les courses du 8 novembre (ne citer aucune sortie) ; 11 arrêts par filtre, aucun nombre — **ouvert** (C-4) ; 12 règle de repli si G0 échoue — **ouvert** (B-6) ; 13 ce que chaque palier livre — **ouvert** ; 14 ligne « R-609 remplace R-468 » — **ouvert** `<<À VÉRIFIER>>` ; 16 juge texte préparé dans la liste scellée de G1 — **ouvert**, nœud de porte, après G0.
  - **« Questions qu'un évaluateur poserait » (l. 1471-1492)** : 1 dénominateur des refus — **ouvert** (C-4) ; 2 pourquoi 12 000 USD de carte graphique — **ouvert mais réparable** : la ligne est au scénario ambitieux seulement (proposition l. 381 ; budget l. 7 : « quote for the whole plan 800-1,200 A100-hours (1,200-2,700 USD) », ligne principale 4 000), à rapprocher des ≈ 130 USD de cartes dépensés ; 3 si G0 échoue — **ouvert** (B-6) ; 4 revue de sécurité externe — **ouvert** (rien n'a avancé) ; 5 garde des contenus en quarantaine — **ouvert** (C-6) ; 6 ce que chaque palier livre — **ouvert** ; 7 contrôle humain sur les agents — **à mettre à jour** (permissions par session, R-1751/R-1752 : argument neuf) ; 8 l'agent a-t-il touché à son frein — **clos** (réponse écrite, l. 1489-1492).
  - **« Ce que la v11 n'a pas pu vérifier » (l. 1494-1513)** : proposition et budget v3 — **clos le 8 novembre** (versés et scellés, mêmes empreintes, R-1836 ; les lignes du plancher 58 630 sont lisibles l. 7, 388) ; compte des refus — **ouvert** ; heure de R-597 — **ouvert, mineur** ; régénération au bit près — **clos** (R-679, sceau `91b61c45…`, `registres/etat.md` l. 58) ; état de T0 à T5, P4, P3b — **clos** (registre unique depuis R-1450, `registres/etat.md` l. 9) ; CL10 — **périmé** ; compte de mots du cadrage — **périmé** (v17) ; facturation réelle — **ouvert** (C-1) ; mot du 29 octobre sur la course d'idéation — **périmé** ; carte des hypothèses « absente du disque » — **ouvert** `<<À VÉRIFIER>>`.
- **Dommage pour le jury** : un texte de préparation périmé fait dire des chiffres faux (dépense, G1, date).
- **Remède ≤ 7 jours** : v17 (R, 1 session) sur le dossier d'intégration, **contre-lue par un lecteur neuf d'un autre modèle** (N-052) ; répétition d'entretien par lecteur neuf (R-1832 (g)). **Si 8 à 14 jours** : répétition avec deux externes humains (geste de Lazar).
- **Dépendance** : C-9 (pièces), sous-agent A (matrice, journal des changements).
- **Responsable** : R, S, L.
- **État au 8 novembre** : v16 non contre-lue, périmée.

### C-13 — Calibration des prédictions : « 80 % de confirmations » et « Brier 0,252 » sont tous deux vrais, et le jury verra l'un ou l'autre
- **Énoncé** : `livrables/registres-taif-v3/calibration-v2.md` (`112b147b…`, section « Comptes par issue » en fin de fichier) : 235 lignes ; tranchées 55 : 44 confirmées, 3 réfutées, 8 non concluantes (taux 44 / 55 = 0,800) ; mais 9 contradictoires, 15 non encore lues, 66 sans run décisif cité par un manifeste, 58 au registre sans verdict scellé ; état critique l. 61-62 : sur 7 prédictions chiffrées avec confiance, score de Brier 0,252 (« autant que dire 0,5 partout »), 7 ampleurs ratées dans le même sens.
- **Dommage pour le jury** : « 80 % : trop beau ? » (R4) ou « Brier 0,25 : vous ne savez pas prédire ».
- **Remède ≤ 7 jours** : présenter les deux chiffres ensemble avec leurs dénominateurs ; lire à la main les 9 lignes contradictoires (S, 0 USD, 1 session) ; dire que les ampleurs ratées s'expliquent par la fuite et la flagrance (état critique l. 62).
- **Responsable** : S, R.
- **État au 8 novembre** : tables v3 régénérées ; contradictoires non lues.

---

## Classement des dix entrées les plus urgentes (jugement de ce rédacteur, dit comme tel)

Critère : probabilité que le jury frappe × dommage × réparabilité en une semaine ; une « × » faible sur l'un des trois fait reculer l'entrée (A-5 et A-7 : fort dommage, faible réparabilité ; B-4 : réparabilité réelle, mais le jury le verra peu).

| rang | entrée | pourquoi maintenant | geste de la semaine (coût) |
|---|---|---|---|
| 1 | **C-1** dépense « about $20 » contre ≥ 645,42 USD plancher | question certaine, dommage maximal, réparable par une ventilation et une phrase | ventilation par poste (0 USD, 1 session) ; rapprochement des consoles (L) |
| 2 | **B-1** course de T0.6 bloquée par E3-6 | seule mesure propre possible avant l'entretien ; fenêtre de création 11-15 novembre | E3 ter (≈ 7 USD, plafond 15) puis course (≈ 17 à 74 USD dans les 200 accordés) |
| 3 | **A-1** la trace existe-t-elle | la question de fond ; se répare en partie par B-1 et par la phrase « non établie, reconception » | bras B (≈ 0,37 USD) ; verdict R13 |
| 4 | **C-3** bascule de G1 supprimée (N-062), calendrier M2 contre M4 | contradiction visible entre le texte envoyé et la décision ; réparable par une page | page « ce qui tient lieu de borne » ; brouillon 2 de la proposition (0 USD) |
| 5 | **C-2** G0 reportée, 2 sur 8 | question certaine ; réparable par la table v3 et une règle de repli | règle de repli (L) ; cause par pièces (0 USD) |
| 6 | **A-2** vérité du dommage | le jury demande la vérité terrain ; l'étiqueteur rend son verdict dans la semaine | verdict de la phase 1 (0 USD) ; audit de l'oracle en variante réduite (≈ 40 USD, plafond 120) |
| 7 | **B-2** scellement de T0.7 (et de P3-bis) | sans lui, le critère 3 ne se lit pas sur la course ; tout est prêt, rien ne coûte | brouillon 7, contre-lecture, scellement (0 USD, 3 à 4 sessions) |
| 8 | **C-8** dispersion apparente | question probable ; matrice déjà en cours | matrice (sous-agent A) ; gel des chantiers hors chemin (L) |
| 9 | **C-6** clés et treize instances | dommage fort si posé ; geste simple mais seul Lazar peut le faire | révocation, lecture de la console (L) |
| 10 | **C-12** v16 périmée, listes ouvertes | le véhicule de toutes les réponses ; réparable | v17 contre-lue, répétition par lecteur neuf (0 USD) |

Juste derrière : C-9 (appel et grille toujours absents : geste de Lazar, levier réduit depuis que la candidature est au dépôt), B-3 et A-6 (T0.8 : brouillon en une semaine, course si 8 à 14 jours), C-11 (passage en public de l'Open Science Framework : geste de Lazar), A-3 (verdict d'hypothèses de l'arène : 0 USD).

---

## Nœuds ouverts pour Lazar (relevés dans `registres/etat.md` l. 3, 167-172, 341, 352, 408 ; brief v2 § 4 ; R-1829 ; R-1580 ; chemin v1)

1. **Transformative AI Fund** : appel et grille du fonds absents du dépôt (`registres/etat.md` l. 3 ; R-1832) ; la candidature envoyée et le budget v3 sont versés depuis 14:40 UTC (R-1836) ; l'appel prévu le 30 octobre a été décalé, aucune note n'existe.
2. **Date exacte de l'entretien** (« dans deux semaines », R-1834).
3. **Prix du nul v9** : accepter la perte de puissance ou chercher un nul moins coûteux, options (a)/(b)/(c), recommandation (c) (`registres/etat.md` l. 3, 408 ; R-1779).
4. **E3-6** : tranché (b) le 8 novembre (galop E3 ter) ; reste la ligne de GO sur devis (plafond proposé 15 USD) et le mot dans la session de la fille qui loue (R-1833).
5. **D:3** : tranché (2) le 6 novembre (R-1624) — fermé, rappelé parce que le chemin v1 le portait ouvert.
6. **W21** : le scellement de G1 doit-il attendre les verdicts des critères 2, 3 et 4 ? (chemin v1 l. 49) `<<À VÉRIFIER : posé ou non depuis le 5 novembre>>`.
7. **Nœuds du 8 novembre, sans défaut** (`registres/etat.md` l. 167 ; brief v2 § 4) : question de sens de W2 (Q1, Q2) ; périmètre de l'attaque v4 (68 à 104 USD) ; ajouts à la plus petite course réelle de l'organisme ; relance du développeur v65 ; **accord sur la reformulation des trois faiblesses** ; devis des courses d'idéation ; destruction des instances R8 58936096, 58936099, 58936100 (59288960 détruite le 8 novembre, R-1777) ; publication de la validation du v9 après son verdict ; objection éventuelle à la v1 bis avec Astra (R-1829) ; axe « protocole de déploiement » (collusion des moniteurs), recommandation « après G0 » (R-1829).
8. **Open Science Framework** : rendre le projet `dr57c` public et le geler (R-1580).
9. **Rotation et révocation des clés** (R-624, R-1539, R-1540 ; `registres/etat.md` l. 341) ; lecture de la facturation de la relève du 23 octobre.
10. **Conséquences de l'audit de fuite de R1 v4** (adoption des lignes « fuite établie » dans les deux verdicts, bras B sur devis — déjà accordé pour la machine de la course) (`registres/etat.md` l. 169) ; **relance de R1 par addendum** (l. 170) ; **D-P1 « qui écrit la loi »** (l. 172) ; suite d'A1 « en attente jusqu'après G0 » (R-1623).
11. **Règle de repli si G0 échoue** et **ce que chaque palier livre, et quand** (v16 pts 12 et 13 ; proposition § 8 à chiffrer).
12. **Nœud proposé ici** : l'ordre des priorités de la semaine du 9 au 15 novembre (B-10).

Compte des `<<À VÉRIFIER>>` de ce brouillon : **9** (relevé par `grep -o`). Entrées : A 7, B 11, C 13.

Fin d'écriture : 2026-11-08 14:49:43 UTC (relevé `date -u`) ; corrections de cadre de la session mère intégrées (14:33 : entretien dans deux semaines, tables `registres-taif-v3` ; 14:50 : candidature envoyée versée au dépôt, appel du 30 octobre décalé).
