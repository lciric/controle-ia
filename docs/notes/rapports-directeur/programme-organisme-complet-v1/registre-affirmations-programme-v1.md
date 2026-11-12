# Registre des affirmations — programme complet de l'organisme d'idéation, architecture (v1)

Compagnon de `programme-organisme-complet-v1.md` (même dossier). Écrit par le rédacteur de l'architecture (sous-agent neuf, Claude
Opus 5.5) le 10 novembre 2026 ; heures relevées par `date -u`. Chaque renvoi **[RAn]** du programme renvoie ici à une ou plusieurs
pièces. « l. n » = ligne du fichier à l'empreinte donnée ; « R-n », « GO-… » = ligne du registre vivant correspondant ; « DOC
<module> » = première docstring du module au commit `651019905ec267c2f339997a6bd67cb3707c4945` du dépôt public, empreinte du module
en annexe ; « lu » = lu par moi ; « cité par » = je n'ai pas relu la pièce primaire, je cite la pièce qui la cite avec son empreinte.

## 1. Pièces et abréviations

| abréviation | pièce | sha256 | lecture |
|---|---|---|---|
| CONS | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-architecture-programme-organisme-v1.md` | `7335655c594f41acb78f19fdfddad98af8e2bd7f65e3efbb909b7a855aaacf92` | lu |
| RPG | `docs/notes/rapports-directeur/rapport-principes-etat-goulots-entretien-organisme-2026-11-09-v1.md` | `22263fced8d43771f0a34b3cdd9b0e6b318e39d23189907a3e9736e74413b984` | lu en entier |
| N044 | `docs/decisions/decision-N-044-v1.md` | `2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf` | lu |
| N045 | `docs/decisions/decision-N-045-v2.md` | `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d` | lu |
| N049 | `docs/decisions/decision-N-049-v1.md` | `8a5bf5e57e2bb447467388acb572e032d1a6a578a868db1b7304263a1c9d4460` | lu |
| N050 | `docs/decisions/decision-N-050-v1.md` | `a54b128df955dba34bb360fa2fea466c787026a934f25135d698e8cd925d5f58` | lu |
| N052 | `docs/decisions/decision-N-052-v1.md` | `817d218b22b8d1d4a2c03bb78fb4870867f19bd1a1f9c08b0a1873efbb31a384` | lu |
| N053 | `docs/decisions/decision-N-053-v1.md` | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` | lu |
| N058 | `docs/decisions/decision-N-058-v1.md` | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` | lu |
| N059 | `docs/decisions/decision-N-059-v1.md` | `41aff854c38bed3a43aced62bd0c1b3af782c5a5f6174f335a175847b407e687` | lu |
| N060 | `docs/decisions/decision-N-060-v3.md` | `2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591` | lu |
| N064 | `docs/decisions/decision-N-064-v1.md` | `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97` | lu |
| N065 | `docs/decisions/decision-N-065-v1.md` | `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4` | lu |
| SN12 | `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-v2.md` (synthèse scellée) | `f0340581766c5fb4d97a0ccb06f0cf1738a15228385b332ee602e93a0be28f0a` | l. 1-32, 63-108, 256-272 |
| RES3 | `docs/notes/rapports-directeur/resultats-pour-documents-v3/section-resultats-organisme-v3.html` (non contre-lue) | `d6d702f5383347f16c894065ce45d96745a20f6016243d5f3b956828b3a3d9fd` | lu (texte extrait) ; renvois « [Bn] » |
| RAV3 | `docs/notes/rapports-directeur/resultats-pour-documents-v3/registre-affirmations-v3.md` | `38c24c925e151dc50f8b5b59eee9d8ff04c9b08e2cc4f52a9d9206553905780e` | abréviations et lignes B1-B53 |
| PAS | `registres/passations/2026-11-10-1159.md` | `e113d747251b1f004b55d7f7c549f08f83d226a9cd19b8f80e493b180d762121` | l. 12-36, 55-100 |
| V16 | `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` | `186173d9d9b949bfb3922503adff1be9d60f49f07fb975750de4c88bd60a060e` | l. 300-330 ; l. 406-413, 783-784 vues par recherche |
| DEC | `registres/decisions.md` (vivant ; `ffa5a882c112bbbed6aae01613677f33d5fc562275073003bc19e13589fcd7c6` à 12:11 UTC) | lignes R- citées | lu ligne à ligne |
| ETA | `registres/etat.md` (vivant ; `1ef56d65e747b59761833a17273a954d1398b5a505a7a076ec49c305cdadd548` à 12:11 UTC) | — | en-tête, l. 39-45, 65, 69, 198, 410-443 par recherche |
| GOR | `registres/go.md` (vivant ; `2c396b016d4ab86bd3f09cc7e21173f19d0c9765cc1a85b8efc08e59c2bc39f0` à 12:11 UTC) | lignes GO- citées | lu par identifiant |
| DEP | `registres/depenses.md` (vivant ; `5268f0f09943ab37d103534206121a30a28b76807b8eae6bac98c3e0d77b02a9` à 12:11 UTC) | — | lignes citées |
| RDM | dépôt public `/home/user/ideation-organism`, `README.md` (tête `6510199`) | `b72c983eada4449931ff828d4e841aaf6708bce881657c745a8c113f3392321e` | lu sauf l. 202 |
| MAN | même dépôt, `MANIFEST.md` | `c58638c9966d01ac1741ed90602e038e90b7e668d1e0cc58020cc670579fcf86` | structure, exclusions |
| C7V1 | même dépôt, `orchestrator/conception-v7-v1.md` | `31fc8c4bc286341fcbf10181be6779ecd20ddf9de092a2c885ce8d11b27fedee` | lu |
| LPT | même dépôt, `pont-fiche-loi-v1/LISEZMOI-pont-v1.md` | `7b1c131db760014798af159047849163bedc03b706f2f684dd0962ac4d6bd17a` | l. 1-60 |
| PONT | même dépôt, `pont-fiche-loi-v1/pont_v1.py` | `9fb2d9366e7764d4fc810b921e8565ca2dcae9af5f1b30ec8866efeb5d3eb692` | l. 1-52 |
| ADA | même dépôt, `orchestrator/pole/adaptateurs.py` | `a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99` | l. 15-30 |
| PGA | même dépôt, `resultats/attaque-goodhart-v2/README.md` (page d'état publique) | `c549a31b266b6952c9f7fc2922243eab21ca304fe7626099310016f071f8ccbb` | titres et lignes citées |
| GLOG | même dépôt, historique (`git log`), tête `651019905ec267c2f339997a6bd67cb3707c4945` | — | sujets des commits |
| DOC | docstrings de tête des modules de `orchestrator/pole/` (fichiers cloisonnés exclus) | annexe | première docstring |
| PCO6 | branche `origin/canal/conv-audit-n04` (`ec3863bbc`), `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/programme-conception-organisme-v6.md` | `6e95f6c5ae6bec23b86ec4eaca39d50ddd02a9e071942d99a74004827c6271c3` | l. 44-214 |
| PCO7 | même dossier, `programme-conception-organisme-v7.md` | `b7cd2f56bf99357caf51493ca0ed966753711926c91c094f971197b29c7192fd` | l. 1-151, 321-fin ; § 3 bis et 3 ter non lus |
| V65R | branche `origin/prep/organisme-v65-v1` (`3daf08e24`), `docs/notes/organisme-boucle-reelle-v1/code-v65/rapport-developpeur-organisme-v65-v1.md` | `f84c14303eacf87e7e129955d3f9b7ba35fc7504545033c37b66b9c4ad5aff0c` | l. 1-60 ; l. 95 et 158 par recherche |
| SDN | branche `origin/claude/upbeat-cray-dmauvv`, `registres/passations/2026-11-10-1114-decision-lazar-enveloppe-120-usd.md` | `ddb77ed67196e50bddc4d0a75af7bc1ad05009b60de0af572269aa94bbae9114` | l. 17 par recherche |
| GREP | mes recherches par `git grep` dans le dépôt public (12:11 et 12:20 UTC) et par `grep` sur les registres nommés | — | consignées au journal |

## 2. Affirmations

| n° | affirmation (courte) | sources |
|---|---|---|
| RA1 | orchestrateur publié jusqu'à la v64 ; v65 sur la branche `prep/organisme-v65-v1` | GLOG (63ed933 « code v64 ») ; fichiers `tour_ferme_v64.py`, `adaptateur_commande_v64.py` à `6510199` ; V65R l. 1-30 |
| RA2 | nul de production v8 ; v9 candidat, validation « puissance perdue », v8 reste en production sauf acceptation du prix | RES3 § 2 [B14], [B19] (V9 `1407e460…`, cité par) ; RDM l. 9 ; PGA l. 52 |
| RA3 | boucle complète jamais courue avec de vrais agents | RDM l. 9, l. 132 |
| RA4 | décision R-2152 : organisme d'idéation = organisme de l'objectif ultime ; branché depuis le 28 octobre ; sans rupture de code jusqu'aux v64-v65 ; propriétés manquantes ; organisme de Gemini concurrent | DEC R-2152 ; RES3 [B52] |
| RA5 | N12 (b) : couches fermées jusqu'aux résultats de l'étape 2 ; essai sur processeur « preuve formelle contre suite bon marché » (devis d'appels de sous-agents) ; couche 3 = réécriture de soi sous bac à sable, couche 4 = pôle théorie et Lean, aucune n'existe (31 octobre) | DEC R-959 (1) ; DEC R-920 |
| RA6 | configuration v5 du code v65 : `exemples/configuration-boucle-reelle-v5.json`, `bff138d8a30c57b898b84c5db49e00a501d15c158009deb12e697b9a13b0e322` | V65R l. 41, l. 95, l. 158 |
| RA7 | GO-2026-11-10-10 : 120 USD au plus jusqu'au 30 novembre ; organisme 45 (40 modèles, 5 machine Hetzner CPX32) ; conditions de GO-2026-11-08-02 ; configuration v5 `995eb918…` ; Bailey 75 ; inscrit à 12:05 UTC ; lève le nœud de R-2202 ; `995eb918…` sans contexte dans la note de la session-dépôt ; absent de `main` | GOR GO-2026-11-10-10 (l. 300) ; DEC R-2206, R-2202 ; SDN l. 17 ; GREP (recherche de `995eb918` dans `registres/etat.md`, les passations du 10 novembre et `docs/notes/organisme-boucle-reelle-v1` : aucune occurrence) |
| RA8 | homonymies : « couche 1 bis » et « couche 2 » de T0.5 au registre ; organismes-modèles saboteurs | DEC R-561, R-564, R-576, R-596 ; V16 l. 783-784 ; PCO6 l. 176-181 |
| RA9 | deux moitiés : prise d'idéation et pôle de test ; étapes 1 à 9 du parcours ; pont | RDM l. 4, l. 51-61 ; PONT l. 1-26 |
| RA10 | règle « le rôle qui produit un artefact ne tient jamais la clé qui l'évalue » ; rôle de l'humain | RDM l. 47 |
| RA11 | figure 1 ; flèche non fermée au 1er novembre (v57b) ; v59 ferme la boucle en code, non courue | RDM l. 12-26, l. 61 ; GLOG 7fadf96 |
| RA12 | N-044 : mots de Lazar ; énoncés 1 à 5 ; portée (code figé et trois régimes en attente) | N044 (sections « Mots de Lazar », « Énoncés retenus », portée) |
| RA13 | vivier de conception codé dans le noyau de l'étape 1 (`noyau/vivier.py`, R-378) | N049, N-049 point 1 |
| RA14 | aucune occurrence de « récompense », « score net », « LOCAL: », « question_ouverte », « test_final » dans `orchestrator/pole` ; « vivier » dans `engagement_apparie.py` et `__init__.py` seulement ; « héritage » = preuve et sélection | GREP (12:20 UTC, `git grep -i` avec exclusions des fichiers cloisonnés) |
| RA15 | aucune ligne du registre consultée ne rapporte un préenregistrement ou une course de l'étape 2 | GREP (motif « étape 2 » dans DEC, lignes au-delà de 1 300, et dans ETA) |
| RA16 | N-045 v2 : énoncés 1 à 8 | N045 |
| RA17 | lignée A : noyau et contrat ; étape 1 « gradient conçu par l'essaim » ; pilotes sur organismes de Gemini (v4 à v6.3) ; confrontation des essaims | GOR GO-2026-10-24-01, -02, -05, -07 ; GO-2026-10-25-01, -02 ; GO-2026-10-26-03 ; noms de branches `canal/gemini-organisme-v4` à `canal/gemini-organisme-v6-3-0` (liste des branches) ; N044, N045, N049, N050, N052 |
| RA18 | lignée B : voie hybride ancrée sur le noyau (26 octobre) ; prise « idéation » (R-634) ; v31, `pole/ideation.py`, 479 lignes ; contre-lecture « non lançable » (CL31-01) | PCO6 l. 46-49 ; DEC R-634, R-635, R-637 |
| RA19 | tests de mort et boucle : « implemented, tested offline, never run for real » ; essais du vrai bac déclarés non joués | RDM l. 118, l. 132 |
| RA20 | composition fixée : Kimi et Argon proposent, aucun rôle pour Claude (course réelle minimale) ; modèles Claude permis : Opus 5.5, Fable 5.1 | DEC R-1738 ; ADA l. 18-23 ; PCO6 l. 52 |
| RA21 | trois numérotations des couches | PCO6 l. 111-183 ; PCO7 l. 1-17, 149, 321-323 ; DEC R-920 ; SN12 l. 1 |
| RA22 | ordre de conception : point 2 (réécriture sous bac à sable, jamais le noyau, après un résultat sur une vraie question) ; point 4 (pôle théorie, Lean) ; « go » du 27 octobre 14:32, « ne pas promettre de révolution » | PCO6 l. 153-157, l. 163-166, l. 54-55 |
| RA23 | pont : trois sorties dont `loi_couche_3` (demande d'épisodes au niveau méthode) ; étapes du module | PONT l. 1-26, l. 36-40 |
| RA24 | couche 0 : monde tenu par le noyau (v6, 0.6.0), (a) puis (a) bis « passée propre » (5,89 USD) ; monde tautologique : 2 vrais promus, 2 faux éliminés, 11 rejeux sur 11 | PCO6 l. 93, l. 96, l. 176 ; RDM l. 122 ; DOC `monde_noyau.py` |
| RA25 | couche 1 : pilote T0.5 de 180 épisodes ; banque v2 de 120 épisodes et 13 moniteurs ; `monde_banque.py` 0.7.0 ; démonstration « pas de dents » | PCO6 l. 94, l. 177 ; C7V1 § « Verdict » 1-2 ; RDM l. 123 ; DOC `monde_banque.py` |
| RA26 | couche 1 bis : 192 épisodes, 96 tâches, parties 48/48/96 ; lue le 27 ; graines neuves : I1, 0 faux sur 19, borne 0,057-0,117 nat par épisode | PCO6 l. 178 ; RDM l. 125 |
| RA27 | couche 2 : définition et dimensionnement ; banque des deux modes connus et pilote de la couche 2 (≈ 234 USD, non accordé) ; « Rien de cela n'existe encore en données » | PCO6 l. 179 ; V16 l. 413, l. 783-784 |
| RA28 | R-2199 : (a), (b), (c) ; (a) lancé ; consigne des critères `0f5d5c78…` | DEC R-2199, R-2200 ; PAS l. 34, l. 75-78 |
| RA29 | question des couches (H2 proposé, « à confirmer ») ; mesure à chaque couche ; anti-gaspillage | PCO6 l. 169-172, l. 183-186 |
| RA30 | synthèse N12-N13 : accords, priorité, risques, divergences n° 1 et n° 5 ; accords trop propres | SN12 l. 40, l. 63-108, l. 256-272 |
| RA31 | collisionneur v8, quatre runs ; question « bac à sable non circulaire » `26f2db15…` ; 16,24 USD | DEP l. 319 ; DEC R-959 (2), R-964, R-1039 ; GOR GO-2026-11-01-05 à -08 |
| RA32 | durée des tests de mort : ≤ 6 min de bac par fiche, ≈ 1 h 40 par sous-session de 16 fiches | DEC R-959 (5) |
| RA33 | recherche : aucune partie de l'organisme ne produit de mathématiques nouvelles ; renvoi N3 du pont | DEC R-2195 ; PONT l. 45 |
| RA34 | voie (b) « théorie adversariale du contrôle » : carte des hypothèses (23 hypothèses, 21 lemmes) ; le pôle théorie la sert | PCO7 l. 84-96 |
| RA35 | bras de l'organisme suspendu (R-597) ; neuf voies (a) à (i) acceptées le 28 octobre ; sortie de (d) au niveau méthode | PCO7 l. 1-17, l. 23-42, l. 48-58, l. 66-77 |
| RA36 | rôles déclarés par le code | ADA l. 18-25 ; DOC `adaptateur_kimi_v53.py` (l. 34, `ROLES_PERMIS`) |
| RA37 | proposeur à liberté bornée ; références enfichables ; 23/35, 5/35, 1/35 sur 20 mondes | DOC `proposeur.py`, `proposeurs_references.py`, `proposeurs_references_v59.py` ; PCO6 l. 98 |
| RA38 | prise idéation codée ; course 1 : 29 fiches, 27 éligibles, 17 idées ; second tour : Kimi et Argon, 12 fiches classées | DOC `ideation.py`, `ideation_v2.py`, `ideation_v59.py` ; RDM l. 53, l. 126-127 |
| RA39 | aiguilleur : forme seule, passeport, étape protégée ; consigne v1 `c2efa120…` ; M4 non calculée par v53 à v56 | RDM l. 54, l. 78 ; DOC `aiguilleur_v53.py` ; DEC R-959 (3) |
| RA40 | mémoire anti-redite, coffre, caviardage | RDM l. 55, l. 72, l. 74 ; DOC `memoire.py`, `memoire_v53.py`, `coffre_v53.py`, `coffre_v55.py`, `caviardage.py` |
| RA41 | juges croisés (Kimi, Argon, Opus 5.5) ; plafond : 11 sur 12 « notables », κ = 0 | RDM l. 56, l. 127 ; DOC `juges_croises_v53.py` |
| RA42 | juges d'idée v2 : contenu ; brouillons ; brouillon 4 non scellable (B10) ; course suspendue | DOC `juges_idees_v2.py` ; GLOG c15a073, 3e7ca5c, eaa74ca, faff48b ; DEC R-1469, R-1471 ; GOR GO-2026-11-04-08, GO-2026-11-02-24, -32 |
| RA43 | juge-tournoi : conception v2 `0ac81c9a…` (Kimi) ; devis 80 à 145 USD ; juge Opus décidé ; v3 et devis à écrire ; nœuds D-1, D-2, D-5, D-9 | DEC R-1999, R-2026 ; RPG § 6, § 7 |
| RA44 | bisociateur à trois bras, sans bras hasard ; SciMuse « à vérifier sur PDF » | RDM l. 57 ; DOC `bisociateur_v53.py` ; DEC R-959 (4) |
| RA45 | metteur en fusion ; fusion complète avec passeport et verdicts ; une fusion au second tour | DOC `course2_v56.py` (CL20-05) ; RDM l. 127 |
| RA46 | moissonneur : arXiv et OpenAlex, métadonnées ; non opposable ; option (A) du 29 octobre | RDM l. 58 ; DOC `moisson.py`, `relais_moisson.py` |
| RA47 | lecteurs ; chiffre imprimé et lecteur neuf comme témoins depuis v57 | RDM l. 69, l. 127 ; DOC `simulation_v54.py`, `tests_de_mort_v5.py` |
| RA48 | tests de mort : script, bac à sable, prédiction scellée, seuil gelé, vérificateur d'une autre famille | RDM l. 60, l. 73 ; DOC `cycle.py`, `tests_de_mort.py` |
| RA49 | vérificateur : rejeu limité ; autre lignée ou famille | C7V1 § 6 ; RDM l. 47 ; DOC `cycle.py` |
| RA50 | pont : 82 essais (77 + 5), 25 mutations ; note de conception `5161e199…` hors public ; ce qui reste (couche v57, témoins, épreuve décisive) | LPT l. 1-40 ; MAN section « Excluded » |
| RA51 | gardien mécanique seul (D9) ; fausse découverte par l'oracle (D2) ; oracle v60 | GOR GO-2026-11-02-18 ; DOC `tour_ferme_v61.py` à `_v64.py`, `lecture_tour_ferme_v60.py` à `_v63.py`, `oracle_tour_ferme_v60.py` |
| RA52 | recombinaison bisociative des survivantes ; rôles `recombinaison`, `synthese` | DOC `recombinaison.py` ; ADA l. 18 |
| RA53 | noyau, configuration, pré-pilote, course 2, suivi des rôles, table des gardes au départ | DOC `noyau_v54.py` à `_v56.py`, `configuration_v53.py` à `_v56.py`, `prepilote_v54.py` à `_v56.py`, `course2_v53.py` à `_v59.py`, `suivi_roles_v54.py`, `gardes_e0_v54.py` à `_v56.py` |
| RA54 | rôles de dépense ; aucun repli silencieux | RDM l. 75, l. 78 ; DOC `budget_v53.py`, `budget_v54.py`, `budget_v56.py` (`ROLES`) |
| RA55 | adaptateurs et relais ; clé jamais dans l'environnement de l'agent ; correctif v47 (R-764) | ADA l. 18-30 ; DOC `relais.py`, `relais_reel.py`, `relais_reel_v2.py`, `adaptateurs_v56.py`, `adaptateur_commande_v64.py` ; RDM l. 73 |
| RA56 | versions empilées (R12), vingt contre-lectures CL1 à CL20 ; arbre public = extrait au commit `91a3c7f8` | RDM l. 188 (figure 2), l. 210 |
| RA57 | table des versions v2 à v7 v21 ; nul des filles v2 ; nul ajusté (0/200 contre 148 à 179) ; 154 et 241 essais | PCO6 l. 89-105 |
| RA58 | course 1, tentative 1 arrêtée le 29 octobre (arbre v45) ; contre-lectures CL2 à CL11 des v34 à v44 | DEP l. 237-238 ; liste du dossier `docs/notes/ideation-organisme-v1/` (fichiers `contre-lecture-v34-cl2.md` à `contre-lecture-v44-cl11.md`) |
| RA59 | v46 à v52b : dossier fermé, moissonneur, tests de mort, juges seulement, borne de 768 Mo | DOC `dossier_ferme.py`, `moisson.py`, `relais_reel.py`, `tests_de_mort.py`, `tests_de_mort_v2.py`, `juges_seulement_v1.py`, `etage_entre_generations_v53.py` |
| RA60 | v53 à v56 : course 2 ; liste blanche (v56) ; base de l'arbre public | DOC `course2_v53.py`, `etage_entre_generations_v56.py` ; RDM l. 188, l. 210 ; GLOG dc2b2ba |
| RA61 | v57, v57b : verdict par le noyau, point de sélection ; 19 et 15 mutations ; 224 mutations jusqu'à v58 | RDM l. 61, l. 69, l. 110, l. 119 ; DOC `tests_de_mort_v4.py`, `tests_de_mort_v5.py` ; GLOG 7ffee97, e488b51 |
| RA62 | v58 : nul v8 seul nul ; validation décisive confirmée | RDM l. 98-108 ; GLOG 1bad95f, 2cfb940, bfa5a02 |
| RA63 | v59 : boucle fermée ; proposeurs sans classement des juges | GLOG 7fadf96 ; DOC `boucle_fermee_v59.py`, `course2_v59.py` ; GOR GO-2026-11-02-06 |
| RA64 | v60 à v64 : tour fermé (réserve, oracle, cœur, lecture, adaptateur de commande) | GLOG 0469450, 7d3aa82, 8247cac, af92034, 63ed933 ; DOC `tour_ferme_v61.py` à `_v64.py`, `adaptateur_commande_v64.py` ; existence de `reserve_tenue_a_l_ecart_v60.py`, `_v61.py` (non ouverts) |
| RA65 | code v65 : dix fichiers neufs ; M1 à M6 ; 232 passés, 3 sautés, 38/38 mutations ; essai à blanc en 9 étapes ; réserves ; non contre-lu | V65R l. 1-60 ; RES3 § 5 [B49] |
| RA66 | hors de la chaîne : nul v9, attaques v1 à v5, juges v2, juge à plan plein, porte PACE (bras de référence, jamais une sélection d'agent, exploratoire) | DOC `nul_v9.py`, `attaque_goodhart_v1.py` à `_v5.py`, `juges_idees_v2.py`, `juge_plan_plein_v1.py`, `porte_pace.py` |
| RA67 | principe du juge ; richesse ≥ 20 ; α = 0,05 ; tirages semés par l'empreinte | RDM l. 59 ; DOC `selection_pari.py` ; RES3 [B2] |
| RA68 | O2 resserrée (N-064) ; e-valeurs et seuil hors agents non revendiqués | N064 points 1-2 |
| RA69 | nul informé : prédicteur connu ajusté avant le gel sur une partie de calibrage | C7V1 § 2 |
| RA70 | nul v9 : recombinaisons par morceaux, certificat, Ville à α ; validation « puissance perdue » | GLOG 5e352ec ; DOC `nul_v9.py` ; RES3 § 2 [B14]-[B19] |
| RA71 | e-BH par défaut ; erratum ; témoins vrais hors famille, m fixé avant les issues (v11) | PCO6 l. 65-67, l. 101, l. 190 |
| RA72 | pari apparié borné : unité, forme « parts », garde, intersection-union, héritage ; D-S1 à D-S12 (N-055) ; cœur codé hors du cycle | PCO6 l. 80-84, l. 105, l. 125-148 ; DOC `pari_apparie.py`, `engagement_apparie.py`, `monde_banque_scores.py` |
| RA73 | puissance sur la banque : 0,8 → 95 % ; 0,5 → 65-73 % ; ≤ 0,3 → ≤ 24 % ; faux témoins ≤ 5 % | RDM l. 124 |
| RA74 | citations obligatoires ; collision Qu, Chen et Wang : deux composantes en entier, une dans son principe, une absente ; nœud | N064 point 4 ; RES3 § 7 [B41]-[B48], [B50] |
| RA75 | témoins plantés anonymes ; témoins jugés sans agents ; signal « pas de dents » | RDM l. 77 ; PCO6 l. 149-151 |
| RA76 | mondes en grammaire (v7 v7, v8) ; W1, W2, W2g ; monde S-V1 | PCO6 l. 98-99 ; RES3 § 1, § 3 [B8], [B20] ; DEC R-1738 |
| RA77 | N-058 : composition jugée sur l'oracle et le coût ; duel non relancé par l'inscription | N058 |
| RA78 | N-059 : points 1 à 14 | N059 |
| RA79 | N-060 v3 : oracle de couverture ; épreuves ; repli ; oracles exécutables gardés | N060 |
| RA80 | épreuve fraîche du pont : L1 6/6 ; L2 0/15 ; L3 0/8 ; L4 sûr (0 arrêt, 0 canari) ; L5 conforme ; lecture `400506d9…` ; **1,34 USD sur 5** (le jalon 2 portait 1,11, chiffre d'une autre ligne : corrigé) | DEC R-986 ; DEP l. 302-303 |
| RA81 | nœud D-P1 sans défaut ; options (b), (c) ; recommandation (c), 0,55 ; D-P2 à D-P5 | DEC R-990 ; ETA l. 198 ; LPT « Ce qui reste », point 1 |
| RA82 | garde des outils ; dossier fermé ; liste blanche de la machine jetable | RDM l. 73, l. 76 ; DOC `garde_outils.py`, `dossier_ferme.py`, `etage_entre_generations_v56.py` |
| RA83 | devis de plomberie de la machine jetable v1 à v3 (Hetzner) ; CPX32 pour la v65 | liste du dossier `docs/notes/ideation-organisme-v1/machine-jetable-v1/` ; GOR GO-2026-11-10-10 |
| RA84 | tour fermé : objet, étages, décisions GO-2026-11-02-06, -18, -19, -23 | GOR GO-2026-11-02-06, -18, -19, -23 ; DOC `tour_ferme_v61.py` ; GLOG 0469450 |
| RA85 | préenregistrement du tour fermé en six brouillons contre-lus ; commandes v6 ; configuration v4 | GLOG 0469450, 7e357d1, 7d3aa82, 82ad7a8, 8247cac, 8261c30, af92034, a12713a, 171b856, 63ed933, d54b85c ; DEC R-1128, R-1129, R-1130 |
| RA86 | aucune ligne de dépense sous GO-2026-11-02-19 ni -23 | GREP (DEP, 12:13 UTC) |
| RA87 | essai à blanc du 7 novembre : dessin de la course réelle ; défauts de la v64 (fausses hors classe ; 994/1 000) ; devis | DEC R-1738 |
| RA88 | GO-2026-11-07-11 ; GO-2026-11-08-02 (45 USD, 30 novembre, « GO de 40 + 5 dollars. : go complrtt ») | GOR GO-2026-11-07-11, GO-2026-11-08-02 |
| RA89 | préalables (R-2195) ; contre-lecture v65 lancée (R-2197 ; consigne `67b086ce…` ; arbre `cef5ea60`) ; brouillon 1 du préenregistrement au dossier ; suite écrite par la mère | DEC R-2195, R-2197 ; PAS l. 33, l. 80 ; liste du dossier `docs/notes/organisme-boucle-reelle-v1/` |
| RA90 | règle « jamais seul » ; série A1, A1-v3 (trois courses), A1-v4 | RES3 « Règle de lecture » [B7] |
| RA91 | banc des tricheurs v7 rejoué (200 répétitions) | RDM l. 80-96 |
| RA92 | validation décisive du nul v8 : 11 lignes fatales à 0/1 000 ; artefact 395/1 000 ; pertes 0,005 et 0,020 ; « confirmée », deux réserves | RDM l. 98-108, l. 121 |
| RA93 | A1 : dessin ; W1 « instrument en défaut » ; W2 brèche (Argon 12/12) ; correction (plafond commun) ; 3 572 appels, 39,45 USD sur 80 | PGA l. 68-90 ; GLOG 421d090, 4609069 ; GOR GO-2026-11-02-07, -16 |
| RA94 | A1-bis : plan en trois temps ; code v3 ; aucune ligne de dépense sous GO-11 ni GO-12 ; A1-v3 décidée ensuite | GOR GO-2026-11-02-11, -12, -13, -15 ; GLOG a0d087d ; DOC `attaque_goodhart_v3.py` ; GREP (DEP) |
| RA95 | A1-v3 : trois courses (41 appels, 4,245753 ; 620 appels, 48,49583, état non lu ; 960 appels, 58,44887) ; W1 résiste (1/24 ; v7 23/24) ; W2 brèche (24/24) | RES3 [B7], [B9]-[B13] (A13 `7dade9ef…`, cité par) ; GOR GO-2026-11-02-17, -21 ; GO-2026-11-03-01 ; GO-2026-11-04-06 ; GO-2026-11-05-06 |
| RA96 | 42 des 48 lois promues sont la loi du monde ; note W2 | RDM l. 131 ; PGA l. 63 ; DEC R-1768 |
| RA97 | nul v9 : membres ajoutés ; preuve contre-lue (48 mondes, 288 instants, 0 échec) | RDM l. 131 ; GLOG 5e352ec |
| RA98 | validation du nul v9 : « puissance perdue » ; 18 lignes fatales à 0/1 000 ; I02 0,486 → 0,381 ; perte 0,105 [0,0894 ; 0,1223] | RES3 § 2 [B14]-[B17] ; ETA l. 420, l. 438 (sur processeur, 0 dollar ; R-1779) |
| RA99 | dose λ* = 0,40 ; 803/1 000 ; recombinaison 0/1 000 ; « à la limite » | RES3 § 3 [B20]-[B24] |
| RA100 | A1-v4 : issues, 8/11 prédictions, réserves, lecture bornée, 114,0434 USD sur 200, 1 478 appels, publication | RES3 § 4 [B25]-[B33], [B46], [B53] ; PGA l. 3-55 ; DEP l. 414 ; GOR GO-2026-11-02-22, GO-2026-11-08-12 |
| RA101 | classes déclarées non couvertes par le v9 | GLOG 5e352ec ; PGA l. 55 (`NON_COUVERT_V9`) |
| RA102 | réplication Kimi : GO-2026-11-02-25 (150 USD, 16 novembre) ; aucune ligne de dépense | GOR GO-2026-11-02-25 ; GREP (DEP) |
| RA103 | juge-tournoi comme juge génératif sous la même attaque | RPG § 6 ; N065 point 1 ; DEC R-2026 |
| RA104 | nœuds : prix du v9 ; sens de « rien au-delà de l'archive » (v10) ; collision (resserrer ou garder ; « go publication ») | RES3 § 6 [B39], [B40] ; § 7 [B48] |
| RA105 | N-045 v2 : énoncés 1 à 7 et « ce que cela ne décide pas » | N045 |
| RA106 | N-049 points 1-3 ; N-050 | N049 ; N050 |
| RA107 | N-052 ; pratique en lignée B (v31 contre-lue par Opus 5.5, auteur Fable 5.1 ; v65 par Fable) | N052 ; DEC R-635, R-637, R-2197 |
| RA108 | N-053 : cinq propositions ; invariant valable pour la piste « organisme », gardé par le code | N053 |
| RA109 | dans l'orchestrateur : juges aveugles, mémoire sans verdict ni témoin ; v59 sans classement | RDM l. 71 ; GOR GO-2026-11-02-06 |
| RA110 | Avalon : R-920 (a) puis (c) ; N13 (a) maintenant, (b) ensuite ; aucune mention de N13 au registre entre R-964 et R-2199 | DEC R-920, R-959 ; GREP (DEC, motif « N13 ») |
| RA111 | code figé après conception et trois régimes : en attente du mot de Lazar | N044 (portée ; énoncé 2) |
| RA112 | N-065 : rôles 1 et 2 adoptés, rôle 3 à trancher ; invariants | N065 |
| RA113 | rapport du 9 novembre, § 6 : trois rôles, invariants, phrase d'entretien, recommandations 0,7 et 0,5 | RPG § 6, § 7 |
| RA114 | pilier attaque : questions v1 `29870ac9…` et v2 `2dbad4b7…` ; dépenses 2,52, 8,42, ≈ 11,07 USD ; règle de permission refusée (R-1994) ; GO-2026-11-08-13 | GOR GO-2026-11-08-06, -07, -08, -10, -13 ; DEP l. 393-407 ; DEC R-1994 |
| RA115 | courses des mentors du 3 novembre ; Heimersheim 10,026275 ; Kirchner Q2 ≈ 24,07 (deux courses) ; Ibrahim Q1 7,976282 USD | GOR GO-2026-11-03-02 à -18 ; DEP l. 334, l. 342, l. 346, l. 350 |
| RA116 | organisme hors du chemin critique de G0 ; sert la validité et les papiers B et C | RPG § 2 (dernier point) |
| RA117 | organisme de Gemini : conception concurrente rapportée à part | DEC R-2152 |
| RA118 | P-041 (30 octobre, « go ») ; arène coévolutive ; test (a) Bailey dans le devis de P-041 | RPG § 6 ; GOR GO-2026-10-30-13, -15 ; GO-2026-10-31-02, -05 |
| RA119 | (réservé) | — |
| RA120 | lignes de GO de l'organisme et leurs échéances | GOR (lignes citées par identifiant) |
| RA121 | GO-2026-11-10-09 : 500 USD jusqu'au 27 novembre ; dépense de la v65 sur devis dans l'enveloppe | GOR GO-2026-11-10-09 ; RES3 [B51] |
| RA122 | programme complet : assembler, contre-lire par un autre modèle, remettre | PAS l. 79 |
| RA123 | collisionneur v8 : branche, commit, quatre dépenses, total ≈ 74,33 ; espèce B = Opus 4.6 ; versé sans lecture ; « zapper le collisionneur » | DEP l. 319 ; DEC R-1036, R-1039, R-1050 |
| RA124 | collisionneur v9 du 2 novembre : branche, commit `ac25c055`, liste `08aebf56…`, 20,84 + suite 1,85 = 22,69 USD sur 40 | DEP l. 323-331 ; GOR GO-2026-11-02-31 |
| RA125 | A1-v3, deuxième course : état scellé non lu | RES3 [B7] |
| RA126 | collisionneur N12-N13, tour 1 : 13,52 USD | SN12 l. 29 (état du run) |
| RA127 | la page publique cite POPPER, Dwork et al., Blum et Hardt, Co-Scientist | RDM l. 8 |
| RA128 | publication d'A1-v4 le 10 novembre (complément de RA100, non appelé seul dans le programme) | RES3 [B46] ; PGA l. 3 |
| RA129 | course 1, tentative 1 : arrêt, Claude 8,67 USD | DEP l. 237-238 |
| RA130 | second tour réel : 1,47 USD sur 10 | DEP l. 311-312 ; RDM l. 127 |
| RA131 | épreuve fraîche du pont : 1,34 USD sur 5 | DEP l. 303 |
| RA132 | génération de la banque T0.5 complète : ≈ 9,7 à 11,7 USD sur 25 (GO-2026-10-27-07) | DEC R-596 |
| RA133 | (réservé) | — |

## Annexe — empreintes des modules de `orchestrator/pole/` cités par « DOC »

Calculées par `sha256sum` au commit `651019905ec267c2f339997a6bd67cb3707c4945` du dépôt public, le 10 novembre 2026 vers 12:31 UTC. Exclus et jamais hachés : `bras_attaque_v54.py`, `reserve_tenue_a_l_ecart_v60.py`, `reserve_tenue_a_l_ecart_v61.py` (cloison), `__init__.py`, `__main__.py`.

| module | sha256 |
|---|---|
| `orchestrator/pole/a_blanc_v59.py` | `606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c` |
| `orchestrator/pole/ablation.py` | `543737074cafd0b3d0c672932ef8dbc88355335606e62c66c332fa9868349e00` |
| `orchestrator/pole/adaptateur_commande_v64.py` | `adb7328721342601eb487856840e385493e6e35c522c90d804a4f8c96bfb5700` |
| `orchestrator/pole/adaptateur_kimi_v53.py` | `09a46515ff30a99f360fcbc7d4c613c35cb511439a5b6c249327e477fdee4ada` |
| `orchestrator/pole/adaptateurs.py` | `a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99` |
| `orchestrator/pole/adaptateurs_v2.py` | `350b6d06804c5280cbf2aefb9f39309a22e01ce6533471fc61c32c1a8bb75e6d` |
| `orchestrator/pole/adaptateurs_v56.py` | `d36c79b272af450b8d67313f44068743d80f0204bcedbd30f5d879829c945a17` |
| `orchestrator/pole/aiguilleur_v53.py` | `a856cdaa37e8fb1f3b873ef2c0d9aa439ee0a8838f5ee9a2910cb3c0dcf8007f` |
| `orchestrator/pole/attaque_goodhart_v1.py` | `7bdbfe243fbfab3a76fb04fb5692fe34470c851955ba0df4a91ff002d1aed317` |
| `orchestrator/pole/attaque_goodhart_v2.py` | `3c9de8b83b6fcf198d12cacf6a6738c2fc3fe4ade9391f943b3924592959e703` |
| `orchestrator/pole/attaque_goodhart_v3.py` | `cb9cffe77fb858bf279c41881638edecba0166b034a05d44c2f62e2b25a45df3` |
| `orchestrator/pole/attaque_goodhart_v4.py` | `0077a6470781b8cd9e0599232ddd52e3601c8c4c8735a5cfcf817800bda3bb5c` |
| `orchestrator/pole/attaque_goodhart_v5.py` | `8692746a1b02b15465062423d1f05e2084ce1d1861c979316ce1a5ef4384ba15` |
| `orchestrator/pole/bisociateur_v53.py` | `962eb8ce22d5af1bf59970e9ef9cab15620edef4d5e9746161bc302e97c2af02` |
| `orchestrator/pole/bisociateur_v54.py` | `20d938b2dcafcd4bb7c9777a0182a3590b390a146a8375590905741ea0e250f8` |
| `orchestrator/pole/bisociateur_v55.py` | `d9521311a96384494871e9f9fcd4b4554548b9f45fdc28e8e75ca30d4c54d22f` |
| `orchestrator/pole/boucle_fermee_v59.py` | `a2de486592fc98c14e13bb9071d272fb65d4f49de38dd188ee64857698177681` |
| `orchestrator/pole/budget_v53.py` | `cefc7e76322b8f8266ec77f31ecb06bf1ea21633ab5dec1e1b91dc62e4374345` |
| `orchestrator/pole/budget_v54.py` | `220d25e6ce5a7eed008c095ef1a9f66e84b4e98f801dfee2f74bdda02ba5ac62` |
| `orchestrator/pole/budget_v56.py` | `3a672aceeeee3cf83cd4e46ca461fdbaf3acd0a9552be24d2566627ce6b7c13e` |
| `orchestrator/pole/caviardage.py` | `78abfd4731218e20538418608ebebaca3364206ef6d014b7a34829a3c9fd7e85` |
| `orchestrator/pole/coffre_v53.py` | `f8a70c8f71c380689b2979e3c212d09379ceee1973465b2b207b493cbd73c380` |
| `orchestrator/pole/coffre_v55.py` | `ef10fe044608fda51d5cd4b3b855da677845be83d1367ca3aa33fe45337e33fd` |
| `orchestrator/pole/configuration_v53.py` | `ef72ffbf6b5ba546fb5e509502b59f0d9ac4f78772dcb9570ef36086639f4a78` |
| `orchestrator/pole/configuration_v54.py` | `3424ca7fa8911e5c2656cb56632f7d74c958008b9366af0ac45e6a62e4d16d66` |
| `orchestrator/pole/configuration_v55.py` | `2e6237c0a8b1c823fa17ddd6c680357a59ec4030bfbe9ac6ba970a700a864071` |
| `orchestrator/pole/configuration_v56.py` | `122405228d6ec550b2120114e87a1e70bcc74c14eee17342605d8402bd015d6b` |
| `orchestrator/pole/controles_pari.py` | `fabc3d0873e6db639f2578eb00ef0035d7831a3b2a1457ffce1d91aa7a364e1c` |
| `orchestrator/pole/controles_pari_v1.py` | `0389fcbb9f3e016880d6261cd6271b97e9ea073a2b75c54a164b9eff1dfc6ea8` |
| `orchestrator/pole/course2_v53.py` | `8f2d035828df913d8fa92e1b7d0c8e41ac73e8416e60f3b674753c27f5c61237` |
| `orchestrator/pole/course2_v54.py` | `ac1980d04eb88d8fbb9a073902e47146ab9eadd3375a41cd72835fa5acf20342` |
| `orchestrator/pole/course2_v55.py` | `ee6a861e7f8db32a9545372a51f902389cdbea809b0ba354e621a3681e541a70` |
| `orchestrator/pole/course2_v56.py` | `14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1` |
| `orchestrator/pole/course2_v57.py` | `2efc4e0ece6b5cea8354503ae476195cffb448f85bdf5db5b99b6295a22ff17d` |
| `orchestrator/pole/course2_v59.py` | `b5a19a479bba806acb71f6ba49e238b79c717c5423d8ea17a5921c57eae82262` |
| `orchestrator/pole/cycle.py` | `798f039042e3ee1f18df5c566f5a0ddee5dac5c98225c8ce621e267174c8ee18` |
| `orchestrator/pole/dossier_ferme.py` | `62fd284519278382592a4684e9d4ecd32baad5e11491c256ef64ee844f08d087` |
| `orchestrator/pole/duel_pari.py` | `df5f07bd3838e661dd1fd751daeb1ea843436f36d8382047ccc0e664fd78aec7` |
| `orchestrator/pole/engagement_apparie.py` | `fd80872a2e4770a334528b37ccfca6913e093afb350649fe42949b8e93764b0e` |
| `orchestrator/pole/etage_entre_generations_v53.py` | `d568d25bf7d96011cfdcda12e7bc2c1933a61827b237f8c8c363b4055122ad4b` |
| `orchestrator/pole/etage_entre_generations_v54.py` | `86a6bec00c3fee9b4ea510cf8dad8d899b9c96adef1e5ae4f8a8281d658143e5` |
| `orchestrator/pole/etage_entre_generations_v55.py` | `865bd7e5734618a2e989bdd14726ff7db53e014963cbc93b48be1892c7ab4dd9` |
| `orchestrator/pole/etage_entre_generations_v56.py` | `f0c80e2d9801d4a928574f7f442e2950c2d130d77015b30102911bfa87dd6eba` |
| `orchestrator/pole/etage_entre_generations_v57.py` | `e4bf36819d18844079a2bb4996991fd65c233a51d76b7d3daf5b866a71328318` |
| `orchestrator/pole/evaluateur_lois_v62.py` | `26613fe72da7f049d5dd076aab51a3808221bf52686b9d0258a201c8b38b8632` |
| `orchestrator/pole/experience_critere.py` | `87ee8f2dc6a0e21f3235df7f50e0886c32852ed790a9fce988e516d122e8cc86` |
| `orchestrator/pole/experience_juge_v1.py` | `b797fe6041f2b291dec1ab15eac21ba483ec6231c91555cb7c3b1f2d8556060a` |
| `orchestrator/pole/fiche.py` | `ec018f147196222268d91358ce2038bb35bf76069e6bf8928dea9e3db59d1074` |
| `orchestrator/pole/fiches_v53.py` | `7cfcf8329c66c7a37ceb2992cc96e21aedbfa0a10525467672794090a128eda6` |
| `orchestrator/pole/fiches_v54.py` | `1ab0796dd5d9de14ea84953b0307a065572bc300ebe45209ca207d7880bbaebf` |
| `orchestrator/pole/garde_outils.py` | `3abd0e19a8f16cc1c2a8f2590ea04831a7d9ba25c02129fb881b87be3983f390` |
| `orchestrator/pole/gardes_e0_v54.py` | `83b54b816b3277d97f5340ad4a316094a492bc2090c782b3e134092a97ca1edf` |
| `orchestrator/pole/gardes_e0_v55.py` | `e46c5cd0a301c89830d97c098ee52b33ead6b01cafe15ab8454e6b7957c54db1` |
| `orchestrator/pole/gardes_e0_v56.py` | `921e59f23753666d6367678447edf4ee2964dc6ec3d382aefa8582b996e123b9` |
| `orchestrator/pole/graines_v53.py` | `7eb838958b28c7b7a5ee20177dfc3d0c194002b99b2382e019fe7d91c3090dc0` |
| `orchestrator/pole/ideation.py` | `4ee70d25567a9b3ac90911cc5ebee8cebba0537d541e7a0ebc1fa3ed170abdc2` |
| `orchestrator/pole/ideation_v2.py` | `67d2ad3591b21601ece4101154138f532ba519024761beb8c9738181f8f3fefc` |
| `orchestrator/pole/ideation_v59.py` | `069f920aaf8345309cb59e41354be7c566b68f86ae23cd9864ee34cef5833169` |
| `orchestrator/pole/juge_plan_plein_v1.py` | `6bcec082991bd8a4d55d195adb0e7b35f4e5dec00f85330e70863da96f4b4569` |
| `orchestrator/pole/juges_croises_v53.py` | `c4c6ab12dc471eef078c116a4205a22d9b498da720ce71e37a0a6edae6c4239b` |
| `orchestrator/pole/juges_idees_v2.py` | `57e4474aef700adbe9e494ce3955f62b62c2152c810e262e5914fdf675f4a3c8` |
| `orchestrator/pole/juges_seulement_v1.py` | `7147fb1a5a0d3ce0320a0685f4726850a63e3f79085dff693a1a217e0af92608` |
| `orchestrator/pole/lecture_tour_ferme_v60.py` | `f7f5101ed32a52e2c1866ab9a06892c083abfab07684398c17a326ebf8990261` |
| `orchestrator/pole/lecture_tour_ferme_v61.py` | `0e9d19630d02ab140c7190aa94a212974021b179602eb00984fb52e50e81dfee` |
| `orchestrator/pole/lecture_tour_ferme_v62.py` | `c7f6ebc8ea0cb24ed97a45362361ab9c9b3a17f0e88d43aeb914617eafd8387a` |
| `orchestrator/pole/lecture_tour_ferme_v63.py` | `2e2c695abcfe2715ca29101c434346658949a2c86be86ed8f9d6f68a408f94ea` |
| `orchestrator/pole/memoire.py` | `71f1d08613bf335aa9ef7aa1397f20aa24553fea2f1b858c10b265d62f8ab79e` |
| `orchestrator/pole/memoire_v53.py` | `43b01b43b1ec347ff02b456975d74c17e7a0e974e9b95e9ba4935bdb895f31a0` |
| `orchestrator/pole/mesures_v54.py` | `8f3f57fc98972fbcf6aefb27fd37298ac67f249cd295c7127b47ab8e77626c08` |
| `orchestrator/pole/moisson.py` | `35d9a996aaacf6d61e84762a2173e73e3c1a90eda730cce122a0f321b038d0e1` |
| `orchestrator/pole/monde_banque.py` | `33088eb9088549a20ffd489687928a1f1469d1df85a025db29bc9ce3f93e7b18` |
| `orchestrator/pole/monde_banque_scores.py` | `58d4fee878fe7957e163a6b5b791adf8895eb2e136aad55502c011b314bccb28` |
| `orchestrator/pole/monde_noyau.py` | `b2aaf3958525e399f0c6453eace41550146327623f95578d64e158bb13e8cae0` |
| `orchestrator/pole/noyau_v54.py` | `711a32679164bd63605f0bcc2a96f37d53260c479004d04d887d8228ac7d431b` |
| `orchestrator/pole/noyau_v55.py` | `ca0f2dda980777da9c549519c6b15994309722353b22f88d117e95aa2c2d4035` |
| `orchestrator/pole/noyau_v56.py` | `eb5a003e8f23b0882e5588fe537e8b65b890f0d7d19560896be4e85a0731543b` |
| `orchestrator/pole/nul_filles_v2.py` | `0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910` |
| `orchestrator/pole/nul_v8.py` | `cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888` |
| `orchestrator/pole/nul_v9.py` | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |
| `orchestrator/pole/oracle_tour_ferme_v60.py` | `514864b7879e5131ee37f7a57951db5ece514abe9acbd90b1294e0d914041669` |
| `orchestrator/pole/outils.py` | `966d9553026aad1eb7d97fa677334f1b59f22a39f15eef95134d63bc47634444` |
| `orchestrator/pole/pari_apparie.py` | `ec6c2cf64d0c9a3bcb3484f2bc58ca986c89e97829bd45fdb96cbc42bf094fef` |
| `orchestrator/pole/pole.py` | `69e08e9586a7c5991ee8d7fd57de251079df4e965ba21214cce69cab96cb3845` |
| `orchestrator/pole/porte_pace.py` | `1f31a5917d0fec912b1b81e393bacdfa6018e16d63356677e72382e3e2090ef6` |
| `orchestrator/pole/prepilote_v54.py` | `77056684e5d1b2149521878da396d51bb3f16834de85ca9e86acdc7e1998592d` |
| `orchestrator/pole/prepilote_v55.py` | `e91e07e4f3bf67cd5106129586048abb3b06284eb9812f8e4da4082087859f05` |
| `orchestrator/pole/prepilote_v56.py` | `dfce55061c65b5ae7526161c54be17005ddef631cb539463cd2c23b32b87b087` |
| `orchestrator/pole/proposeur.py` | `a77018584ec5d20c25224fc675c412c4606ba3a6ce8dfde6e469a651a425a2ea` |
| `orchestrator/pole/proposeurs_references.py` | `6ed7e56fb1a1f7441467281d414b892176e73a1ffa528db090684cb6cf20805c` |
| `orchestrator/pole/proposeurs_references_v59.py` | `7d00371a8fcfa3efc2c17b2f0ab33d18ef83b41f3988744ea12dcf823806f68f` |
| `orchestrator/pole/protocole_outils.py` | `0657eec8e0b1a3d2a3f57f37aad59c34554a2352be4e42ed2c3395e9e94fe2b5` |
| `orchestrator/pole/recombinaison.py` | `71faad38644c77ae2cc21f23bfb1011c48fe674a08e542983819425ee47bd3d0` |
| `orchestrator/pole/relais.py` | `b5a76343e458cf8fb91ee1928244f9cb65d50c27ab9b1bae91c21a5c82349da3` |
| `orchestrator/pole/relais_moisson.py` | `11584bfa67d78439cc369b4e82eb1418077660c4abd61e00bc8e06e01d763cce` |
| `orchestrator/pole/relais_reel.py` | `1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153` |
| `orchestrator/pole/relais_reel_v2.py` | `98c3e79e2c795a69345ffcf9aa742e31dde4a578a15f7c610f1ec7fd535ac8d7` |
| `orchestrator/pole/selection_pari.py` | `359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc` |
| `orchestrator/pole/simulation.py` | `be14d44e7a8ebf6b2a71f16b5290555f5d7a11309e5dbf309ce9097f19ae7892` |
| `orchestrator/pole/simulation_v53.py` | `27129c62498e3d5b801eb4d882b8abb7db2c3a0bfb2205829a62d7f0c69a353c` |
| `orchestrator/pole/simulation_v54.py` | `de2232922516f0d3fa2ca664ff80800d0ac53ff8e823b784864aab375e01941c` |
| `orchestrator/pole/simulation_v55.py` | `91ac1c345c3670dd232b0c1da63825608aac1a840192639dd01e7fb175efbf4f` |
| `orchestrator/pole/simulation_v56.py` | `bcafca44c5117dfd30262ee520a67944d051208f1b1deac6fac016e8cb95dc76` |
| `orchestrator/pole/suivi_roles_v54.py` | `620225973d68670a56ca913cdd02709fa576fa43e1393d166915ea67c1d7c3bb` |
| `orchestrator/pole/tableau_v53.py` | `1a8267fea6d147b070d697ccd2c9d33f2514be6fcba106dca8ca123be1cb7403` |
| `orchestrator/pole/tests_de_mort.py` | `fc5d3507b33e13094d64751ff2b4564ba5ed4c238f93aaae808c458b3c123252` |
| `orchestrator/pole/tests_de_mort_v2.py` | `363a3725885da08412f25b28defba7a8d204d883c3637f1de1df83686d93a41a` |
| `orchestrator/pole/tests_de_mort_v3.py` | `ea05eb55f9d179501fb091d25298deaf36cd66ad16fd65bdca4dcf5e4ba74bba` |
| `orchestrator/pole/tests_de_mort_v4.py` | `35912a3ab5e9e289077ffdceb492bb966f24176244976b3923dcfe95bda1603a` |
| `orchestrator/pole/tests_de_mort_v5.py` | `da524871b9b498693d67cc099240acb98c4c84c800ee4c69f0a1cb5fe60b64f1` |
| `orchestrator/pole/tour_ferme_v61.py` | `d7817ce03877e0817d1f7b381981a16455ece514b383cbe78013bfc91c4a3a7f` |
| `orchestrator/pole/tour_ferme_v62.py` | `0af0f759a45cf90b769908d0fb72a2837f18994859651444fc280dc5127c3c99` |
| `orchestrator/pole/tour_ferme_v63.py` | `9982ae3c819eedec78f5c1757e876f01051d2fd732c1e2371692a3823cf13c40` |
| `orchestrator/pole/tour_ferme_v64.py` | `35a8294e24c870685435b990d6c03cd33cb5b2e288bcb2cc91cd9af04679c2da` |
