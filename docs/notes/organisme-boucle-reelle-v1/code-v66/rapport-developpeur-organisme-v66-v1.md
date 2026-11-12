# Rapport du développeur — code v66 de l'organisme d'idéation (corrections de la contre-lecture du code v65) — v1

- **Développeur** : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent neuf de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`.
  Je n'ai écrit ni la v65, ni sa contre-lecture, ni aucune version précédente de l'organisme.
- **Heures** (temps universel, relevées par `date -u`, 10 novembre 2026) : début 12:20:18 ; code de 12:27 à 12:45 ; essais de
  12:45 à 12:58 ; banc de mutations de 13:03:45 à 13:19:15 (premier passage), puis passage final de 13:25:56 à 13:40:28 ; essai à blanc de 13:05:08 à 13:06:03 ; suite rejouée de
  13:20:13 à 13:25:30 ; rapport écrit à partir de 13:41.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-developpeur-organisme-v66-v1.md`,
  sha256 `264e8a080e90dc278b2fb33e2d25af1340bd8c1d87e230b4b56b88e5c9dceb0b`, égale à son compagnon. Sources lues : contre-lecture
  `contre-lecture-code-v65-v2.md` (`c4ddfc7f…`, égale), consigne v65 (`2dc207e7…`, égale), rapport et blocs du développeur v65,
  brouillon 1 du texte (`736e3fd6…`), garde de calcul `.claude/hooks/garde_calcul.py` (fonction `lire_go`), `registres/go.md`
  (lecture seule, `2c396b01…`).
- **Interdits communs v2 suivis** : aucun fichier interdit ouvert, aucune recherche récursive sur un dossier qui en contient,
  aucune variable d'environnement lue ni affichée, aucun appel de modèle, aucun réseau, aucune dépense, aucune instance. Git :
  seulement l'exception de la consigne (branche locale `prep/organisme-v66-boucle-reelle-v1` créée depuis `cef5ea60` dans
  `/home/user/organisme-v65-cl`, commits locaux, **aucune poussée**) ; rien committé dans le dépôt de travail.
- **Un refus de classifieur, rapporté tel quel (règle 6)** : entre 12:27 et 12:45 (heure exacte non relevée par `date -u` ; je n'en écris pas d'autre), la commande d'analyse suivie de
  `rm -rf /tmp/c1-* /tmp/tmp*` a été refusée (« Shared Scratch Sweep »). Je ne l'ai ni relancée ni reformulée. Effet : les
  dossiers provisoires de ma première course d'essai (`/tmp/c1-…` et des `/tmp/tmp…` créés par `tempfile` avant que je fixe
  `TMPDIR`) restent dans `/tmp` ; tous les essais suivants ont écrit dans mon bac à sable.
- **Aucune dépense.**

## 0. Verdict

**Les dix corrections demandées sont faites sous des noms neufs (v66, R12 ; rien de la v65 n'est modifié), chacune avec un
essai sur un cas sain et sur un artefact.** Suite touchée : `323 passed, 4 skipped, 326 subtests passed in 316.56s (0:05:16)` (les quatre sautés sont les essais du vrai bac). Banc v66 : **`133 tuées pour la raison attendue sur 133 mutations`**, dont les vingt
mutations du contre-lecteur (X06 découpée en six, X19 en deux : 26) et les 38 du banc v65 portées. Essai à blanc : 14 étapes,
codes attendus. Ce qui reste non éprouvé tient au seul `bwrap` (section 8).

## 1. Base et arbre

- Arbre `/home/user/organisme-v65-cl` (clone de travail du dépôt public de l'organisme), branche locale
  **`prep/organisme-v66-boucle-reelle-v1`** créée depuis `cef5ea60ea22a9bb46a2b0be761972672a4c2ede` ; commits : `838fa68` (jalon 1 : code), `3ba4727` (jalon 2 : essais), `7e415cb` (jalon 3 : banc, deux angles morts fermés).
  Tête : **`7e415cbaaa3ff602db43a44dad6b4307c08352c7`**. Jamais poussé.
- Fichiers neufs seulement (onze) ; aucun fichier existant modifié (`git diff cef5ea60 --stat` : onze ajouts).
- Interpréteur : `/home/user/controle-ia-travail/.venv/bin/python -I -B` (Python 3.13.16, numpy 2.4.6, scipy 1.17.1, pytest 9.1.1).
  Dossiers provisoires dans mon bac à sable (`TMPDIR`), sauf l'exception ci-dessus.

## 2. Corrections, une par une

La v66 réutilise **sans les modifier** le cœur v65 (jeu planté, héritage de départ, gardes 17, 19, 20, 21, copies,
`exiger_go`, `exiger_part_avant_appel`), le tour fermé v64 et la boucle fermée v59. Le bloc du jeu reste `jeu-plante-v65`
(même jeu, même empreinte `21b4b005…`) et l'héritage de départ reste `heritage-depart-v65.json` (`93dcf517…`).

| correction | ce que fait la v66 | où | essais (sain / artefact) |
|---|---|---|---|
| **CLV65-01** | **Complétude exigée avant toute issue autre que C5** (`completude`) : générations [1, 2], un étage par génération, membres attendus > 0, V1 à V4, T-ELIM, T-MAL une fois en génération 1, F1 à F4 une fois dans chaque génération, rien d'autre en génération 2, copies = min(4, retenues de la génération 1) et chacune d'une retenue, chaque fausse et chaque copie **passée au gardien et jugée** (membres d'archive consignés, log W maximal présent), toute plantée passée jugée, membres de chaque plantée de la génération 1 = ceux qu'impose {K1} (garde 18), vue servie consignée pour les deux générations, sélection finale relue ; sinon **C5 « relevé incomplet »**, manques écrits (`cause_c5`). En génération 2, un écart de membres reste un écart de P6, donc C4, comme le dit la ligne C4 du texte (« archive de la génération 2 ≠ … ») : c'est le seul point où je lis la consigne du contre-lecteur plus étroitement, et je le dis. L'audit A1 ne lit plus un log W absent comme « ≤ 0 », ni un contre-calcul absent comme « égal », et « bac réel partout » exige deux étages. | `pole/lecture_boucle_reelle_v66.py` | `test_C1_sain` / `test_C5_releve_incomplet_artefacts_de_la_contre_lecture` (19 relevés altérés, dont les six de la contre-lecture : fausses refusées au gardien, absentes de la génération 2, des deux, aucune copie, une seule, génération 2 absente ou aucun étage) ; `test_A1_artefacts`, `test_A1_bac_reel_partout` |
| **CLV65-02 (a)** | **Jugements écrits au relevé dès la sortie du juge**, avant les étages (promotion, log e, log W maximal, membres d'archive, membre dominant, empreinte d'engagement, graines ; `etage` « en attente ») ; verdicts, contre-calcul et retenue ajoutés après. | `pole/boucle_reelle_v66.py`, `jouer_generation` | `test_sain_jugements_puis_verdicts` / `test_artefact_arret_pendant_l_etage_jugements_presents` (contre-calcul en désaccord pendant l'étage : 12 cartes et 10 lois plantées au relevé partiel, C5) ; `test_artefact_arret_ne_masque_pas_une_fausse_promue` (juge artefact qui promeut F2, puis arrêt pendant l'étage : **C5 et « C2 (partielle) »**) ; essai à blanc, étape 9 |
| **CLV65-02 (b)** | **Héritage refusé consigné** : `lecture_selection` porte l'empreinte attendue, l'**empreinte sur disque du bilan, relue à part en octets** (et non l'écho de l'empreinte attendue que rend `lire_heritage`), le type et le motif ; idem pour la relecture finale (`selection_finale.refus`). La lecture en fait un écart de P6 : sous C5, **« C4 (partielle) »**. La branche « empreinte lue ≠ écrite » est donc atteignable. | cœur `jouer_boucle` ; lecture `p6_ecarts` | `test_artefact_heritage_altere_C4_partielle` (sélection modifiée après le sceau) ; `test_artefact_empreinte_lue_differente_de_l_ecrite` (bilan réécrit et rescellé : lu ≠ écrit, lu = empreinte sur disque) ; `test_artefact_relecture_finale_refusee` ; `test_C4_heritage_refuse_sous_C5` |
| **CLV65-03** | **Garde 23 (neuve) : vue réellement servie, vérifiée au moment du service.** Avant le premier appel : les lois du contexte servi = {K1} ∪ retenues **écrites** par la génération 1 (fichier de sélection relu à part, pas l'héritage lu), chacune égale à sa loi d'archive, aucune loi plantée. Après chaque appel : l'empreinte du texte que le proposeur a reçu (`ProposeurAdaptateur.appels[-1].consigne_sha256`) = celle du texte bâti sur ce contexte vérifié. Sinon `VueServieRefusee` (arrêt, incident écrit). Le relevé porte `vues_servies` (identifiants, empreintes des lois, du contexte, du texte, de chaque texte reçu) ; P6 compare la vue servie de la génération 2 à {K1} ∪ retenues **recalculé depuis le relevé**, la génération 1 à {K1}, l'archive de jugement de la génération 2 à {K1} ∪ retenues. | cœur ; lecture | `test_sain_vues_servies_au_releve` / `test_artefact_la_generation_2_ne_sert_que_K1` (**mutation « ne sert que K1 » devenue artefact : arrêt, C5 et C4 (partielle)**), `test_artefact_heritage_d_un_autre_contenu`, `test_artefacts_garde_23_avant_l_appel`, `test_artefacts_garde_23_apres_l_appel`, `test_C4_lecture_de_selection_et_vue_servie` |
| **CLV65-04** | Un essai sur artefact pour chaque garde sans essai citée (tableau de la section 5 : X01 à X20) : garde 7 réécrite (sélection), appel de la garde 21, refus du bac factice en mode réel, branche réelle du lanceur **jusqu'à la garde 22** (refus : `bwrap` absent), et, avec des doublures à la place des gardes 22 et 15 et des rôles réels, jusqu'à `--verifier-seulement`, coût d'un appel qui s'arrête, plafond restant avant l'appel, version et génération de l'héritage, grammaire du jeu, empreinte du relevé et du monde au lecteur, relecture finale, plafonds > 0, champs de A1, A3, fausse découverte réelle, seuil de T-ELIM. | essais v66 | voir section 5 |
| **CLV65-05** | **Garde 7, moitié « ni servies », reprise** : `tour_ferme_v64.exiger_sans_temoin` (identifiants réels et servis des lois plantées) sur l'héritage lu avant la génération 2 et sur la relecture finale ; la garde 23 refuse aussi une loi plantée servie ; la lecture voit une loi plantée retenue (écart de P6). | cœur ; lecture | `test_artefact_loi_plantee_dans_l_heritage_lu`, `test_artefact_loi_plantee_a_la_relecture_finale`, `test_artefact_loi_plantee_dans_la_selection`, cas « loi plantée retenue » de `test_C4_lecture_…` |
| **CLV65-06** | `WHICH` (module du lanceur) cherche `bwrap` ; l'essai `test_artefact_bwrap_absent_refus_code_2_sans_repli_partout` la remplace (`None`) et vérifie qu'elle est appelée : il **tourne aussi là où `bwrap` existe**, et tue `N-bac-factice` partout. Le banc ne compte plus jamais « survit » une sélection entièrement sautée (défaut du banc). | lanceur ; banc | idem |
| **CLV65-07** | **Lecteur du registre des GO v66** (`pole/registre_go_v66.py`) : la règle de `garde_calcul.lire_go`, recopiée ligne pour ligne (extension admise seulement si périmètre « extension… », même type, accordée par Lazar, pas antérieure, échéance non plus lointaine ; validité de la première ligne). Deux règles neuves, dites : un GO cité **qui porte une extension est refusé** (montant ambigu : le registre montre des extensions qui relèvent le plafond) ; une **enveloppe** `TOTAL USD (nom N, nom N ; texte)` est lue part par part (somme = total au centime, aucun nombre étranger) et la part **« organisme »** doit valoir exactement le montant requis. Sur le **vrai registre** (lecture seule, 255 identifiants, 34 lignes d'extension) : **GO-2026-11-08-02 → 45 USD** (montant seul), **GO-2026-11-10-10 → 45 USD** (part « organisme » de 120) ; 40 et 50 refusés pour les deux ; mêmes identifiants que la garde ; la lecture v53 refuse toujours (« en double »). | `pole/registre_go_v66.py` ; lanceur | `test_registre_go_v66.py` : 12 registres artefacts, **équivalence « admis / refusé » avec la garde elle-même** sur chacun, vrai registre ; lanceur : `test_vrai_registre_lu`, `test_go_enveloppe_lu_par_le_lanceur`, cas GO de `test_refus_nommes` |
| **CLV65-08** | Mesures promises par le brouillon **toutes au relevé** : recherche de L* chez **l'expérimentateur et le vérificateur** (enveloppe `EtageMesure` de l'adaptateur de l'étage : touches hors de la loi gelée du test, attendu zéro, et dans la loi gelée, comptées à part ; l'écho canonique de la loi dans les scripts de l'expérimentateur est rangé « dans ») ; **membre dominant du nul** et **empreinte d'engagement** par loi (`juger_v66`, même calcul que v64 + v65, équivalence essayée) ; graines par loi ; **intervalles de Wilson à 95 %** des parts par fournisseur (lecture, P7) ; **jetons** d'entrée et de sortie par appel en mode réel (champ `usage` de la dernière ligne JSON des commandes, `ReleveDeJetons`, sommes par relais) ; **lignes de tranche dans les contextes servis** (mesure de la v64, reprise, à six décimales). À blanc : 0 touche hors de la loi gelée (192 dedans), 0 ligne de tranche servie. **Rien n'est à retirer du texte** ; deux précisions à y écrire (section 9). | cœur ; lecture ; lanceur | `test_sain_mesures_au_releve`, `test_consigne_sans_loi_gelee`, `test_etage_mesure_artefact_fuite_vers_l_experimentateur`, `test_jetons`, `test_lignes_de_tranche_artefact`, `test_wilson`, `test_oracle_mesures_wilson_…`, `test_sain_meme_calcul_que_v64_et_v65_…` |
| **CLV65-09** | **Garde 22 qui vérifie l'utilisateur réel du bac** : (1) le lanceur réel doit tourner **en superutilisateur** (sinon `setpriv` ne peut pas passer à l'utilisateur dédié : le bac tournerait sous le compte du lanceur, défaut relevé par le contre-lecteur) ; (2) après la sonde, l'identité du script sur l'hôte lue dans la description de l'exécuteur sondé (non factice, sonde réussie) doit être l'utilisateur dédié demandé — la sonde elle-même vérifie sur l'hôte le propriétaire de son fichier témoin (`controler_hote_apres_sonde`). **Ordre du mode réel** : texte, monde, configuration, GO, **garde 17**, **garde 22**, garde 15, et **en dernier** les rôles réels (portes de plafond). | lanceur | `test_garde_22_avant_la_sonde`, `test_garde_22_apres_la_sonde`, `test_garde_22_cablee_identite_du_bac_puis_garde_15_avant_les_portes` (rôles réels jamais appelés), `test_ordre_configuration_puis_garde_17_puis_garde_22`, `test_verifier_seulement_roles_en_dernier_jetons_branches` |
| **CLV65-10** | **Configuration v6** (`exemples/configuration-boucle-reelle-v6.json`, `4743ddbe…`) : commandes v6 et pièces nommées par des **chemins relatifs** au dossier de la configuration (aucun absolu, aucun « .. », fichier régulier sous ce dossier après résolution des liens, empreinte nommée) ; la commande lancée reçoit le chemin absolu résolu (copie ; l'empreinte reste celle du fichier) ; plus de GO dans la configuration (il n'est que dans le plan gelé). **Dossier de course complet** versé (`configuration-v6/` : configuration, six pièces de la v4, trois commandes v6 du commit `12f9e0e3`, octet pour octet) : le lanceur le déclare conforme. | lanceur ; exemples | `test_fichier_v6_…`, `test_sain_dossier_complet`, `test_artefacts` (11 cas, dont chemin absolu ou « .. » restant dans le dossier, lien qui en sort) ; essai à blanc, étape 14 |
| dossier du texte | **Gardé** : `orchestrator/prereg/preenregistrement-boucle-reelle-organisme-v1-v<N>.md`, seul chemin accepté (copie locale à l'octet de l'exemplaire du dépôt de travail) ; pousser au dépôt public reste une décision de Lazar. | lanceur | `test_texte_artefacts` (mauvais dossier refusé) |

Mineurs de la contre-lecture traités au passage : CLV65-11 (la phrase de résultat dit le mode, l'exécuteur factice, l'absence
d'oracle et met en tête une fausse découverte d'une carte réelle ; `--releve-sha256` **exigé**) ; CLV65-13 (une erreur à
l'écriture du manifeste est un refus nommé, code 2 ; le lanceur n'écrit plus d'issue ; le dossier des sessions des proposeurs
est gardé, chemin au rapport). Non traité, dit : une fausse ou une copie promue en génération 2 est encore testée (dépense
minime, cas de brèche seulement) ; les messages de `exiger_bras` (v65 réutilisée) disent encore « code v65 ».

## 3. Fichiers neufs et empreintes (commit `7e415cb`)

| sha256 | fichier (`orchestrator/`) | gelé |
|---|---|---|
| `ea17a4b8645ab4fc81df4702479fbdcd7ced912d9575190779b23fc334fb45b6` | `pole/boucle_reelle_v66.py` | oui |
| `0152103a9f2b33271eddfb6493368e387d5a6c5ade010e217c7abdfda43d52c6` | `pole/lecture_boucle_reelle_v66.py` | oui |
| `4541ef7f53e2210bff7f74e1872ac46a10b29fda30f9cf4db568a99b03c04b4c` | `pole/registre_go_v66.py` | oui |
| `e2dd83ab6e4542de7c40ac4b5d59d8d817950d8327f4f9c4c595bb9b0f129d6b` | `demonstrations/boucle_reelle_v66.py` | oui |
| `e2183565c5867255addf0c74d6de9f1498e3129ded1161e1cf0c6f5f96844db8` | `demonstrations/lire_boucle_reelle_v66.py` | oui |
| `c6a7e110bbbb9858f2159c37b35adaefc0464a81a17ef850dfdc9b06f493c103` | `demonstrations/preparer_boucle_reelle_v66.py` | non (outil) |
| `4743ddbe4d294643ac8e1924476dec056b1a08dac9f8010cd647dd1861160b0d` | `exemples/configuration-boucle-reelle-v6.json` | par le plan |
| `194d342f82cff01ac6dbf5a7ab56f73034b6d4b125b990e5979daccf91fae68f` | `essais/test_boucle_reelle_v66.py` | non |
| `bceb6181eb67899da5859b4b78523163ba0e0576ca4a9f0e7344a7539ba648ab` | `essais/test_lecture_boucle_reelle_v66.py` | non |
| `895cabf510c5755f5a0d0e36e4f6291f364b6617c4350b1194863857c515d5bb` | `essais/test_registre_go_v66.py` | non |
| `959bf41ad644a52284b98327b497d823111d02381bd4f0fc083ff061e95e1437` | `essais/mutations_boucle_reelle_v66.py` | non |

Code gelé (fermeture statique, essai `Fermeture`) : **98 fichiers** = les 92 du bloc v64, `pole/boucle_reelle_v65.py`
(réutilisé), et les cinq fichiers v66 du chemin de course.

## 4. Essais

Suite touchée, finale, sur la tête `7e415cb` (13:20:13 → 13:25:30, `POLE_ESSAI_BAC_REEL_NON_JOUE=1`, neuf fichiers :
`test_registre_go_v66.py`, `test_boucle_reelle_v66.py`, `test_lecture_boucle_reelle_v66.py`, `test_boucle_reelle_v65.py`,
`test_lecture_boucle_reelle_v65.py`, `test_tour_ferme_v64.py`, `test_gardes_tour_ferme_v64.py`, `test_v59_boucle_fermee.py`,
`test_v57b_cablage_verdict.py`) :

**`323 passed, 4 skipped, 326 subtests passed in 316.56s (0:05:16)`**, code 0 (sortie `suite-v66-final.txt`).

Les quatre sautés sont les essais du vrai bac à sable, vérifiés par `-rs` : `test_boucle_reelle_v66.py` (l. 740),
`test_boucle_reelle_v65.py` (l. 553), `test_tour_ferme_v64.py` (l. 1485), `test_v59_boucle_fermee.py` (l. 332). Les essais de
la v65 passent toujours (la v65 est intacte). L'artefact « bwrap absent » de la v66 ne saute jamais (CLV65-06). Les essais du
vrai registre et de l'équivalence avec la garde de calcul tournent ici (le dépôt de travail est présent). Sur une machine sans
le dépôt de travail, ils sont déclarés non joués.

## 5. Banc de mutations

**Construction** (`essais/mutations_boucle_reelle_v66.py`) : 133 mutations. 26 viennent du contre-lecteur : X01 à X20, avec
X06 découpée en six et X19 en deux. 38 viennent du banc v65, portées sur le code que joue la v66. 69 sont neuves, une ou
plusieurs par condition des corrections CLV65-01 à CLV65-10. Une mutation compte comme **tuée** seulement si l'essai de la
**raison attendue** est parmi les essais en échec, sous-essais compris. Une mutation tuée par un autre essai est comptée à part.
Avant toute mutation, chaque sélection est jouée sur la copie saine : elle doit passer avec au moins un essai passé (une
sélection toute sautée est un défaut du banc, CLV65-06), et chaque raison attendue doit figurer parmi les essais collectés.
Les dossiers provisoires sont isolés dans la copie mutée.

**Premier passage** (13:03:45 → 13:19:15, essais de la tête `3ba4727`, banc non encore committé) : **131 tuées sur 133**. Deux
survivantes, deux angles morts des essais, aucun du code :
- `G17-cles` : le contrôle « clés » de `lire_heritage_depart` (v65) double l'égalité exacte de l'archive. Seul le **motif
  nommé** du refus le distingue, et l'essai v65 le vérifiait par expression régulière. L'essai v66 vérifie maintenant le motif
  nommé de chaque refus de la garde 17.
- `N07l-part-demandee` : ma cellule « part absente » (« 120 USD (bailey 120) ») était lue par la lecture v55 comme un montant
  seul de 120, et n'atteignait donc jamais l'enveloppe. Le cas est remplacé par « 120 USD (bailey 75, autre 45) ». L'ancien
  cas est gardé sous le nom « total seul déguisé ».

**Passage final** (13:25:56 → 13:40:28, tête `7e415cbaaa3ff602db43a44dad6b4307c08352c7`, `--processus 4`) :
**`133 tuées pour la raison attendue sur 133 mutations`**, code 0, soit 38 sur 38 pour le banc v65 porté, 26 sur 26 pour le
contre-lecteur et 69 sur 69 pour les neuves (`mutations-v66-final.txt` et `.json`). Aucune mutation n'est déclarée équivalente.
Les deux contrôles redondants trouvés en écrivant le banc ont été **retirés** (section 10). La mutation équivalente déjà dite
par le développeur v65 (boucle « aucune vraie ni instrument dans l'héritage ») reste hors du banc, inchangée.

Les vingt mutations du contre-lecteur, rejouées :

| contre-lecteur | ce qui est retiré | mutation(s) v66 | essai qui la tue (raison attendue) |
|---|---|---|---|
| X01 | garde 7, sélection | `X01-garde-7-selection` | `test_artefact_loi_plantee_dans_la_selection` |
| X02 | familles séparées (cœur) | `X02-familles-coeur` | `test_familles_dans_le_coeur` |
| X03 | familles séparées (lanceur) | `X03-familles-lanceur` | `test_familles_dans_le_lanceur` (code 2, aucune sortie) |
| X04 | appel de la garde 21 | `X04-appel-garde-21` | `test_artefact_copie_d_une_carte_non_retenue` |
| X05 | refus du bac factice en mode réel | `X05-bac-factice-reel` | `test_refus_nommes` |
| X06 | branche réelle du lanceur | `X06a` GO vérifié, `X06b` GO du texte, `X06c` empreinte de la configuration, `X06d` options, `X06e` confirmation, `X06f` garde 17 | `test_refus_nommes` (11 refus nommés) |
| X07 | coût d'un appel qui s'arrête | `X07-…` | `test_artefact_cout_d_un_appel_qui_s_arrete_compte` |
| X08 | plafond restant avant l'appel | `X08-…` | `test_artefact_plafond_restant_avant_l_appel` |
| X09 | version et génération de l'héritage | `X09-…` | `test_garde_17` |
| X10 | grammaire des lois du jeu | `X10-…` | `test_garde_19` |
| X11, X12 | empreintes du relevé et du monde au lecteur | `X11-…`, `X12-…` | `test_bout_en_bout_et_lecture` |
| X13 | relecture finale | `X13-…` | `test_artefact_relecture_finale_refusee` |
| X14 | plafonds, montant, durée > 0 | `X14-…` | `test_plan_artefacts` |
| X15, X16 | champs « contre-calcul égal » et « bac réel partout » de A1 | `X15-…`, `X16-…` | `test_A1_artefacts`, `test_A1_d_office_sous_C1` |
| X17 | audit A3 | `X17-A3` | `test_A3_sans_dents` |
| X18 | fausse découverte réelle | `X18-…` | `test_oracle_mesures_wilson_et_fausse_decouverte_en_tete` |
| X19 | génération 2 qui ne sert que K1 | `X19a` (vue), `X19b` (texte servi) | `test_sain_vues_servies_au_releve` (garde 23) |
| X20 | seuil de T-ELIM | `X20-…` | `test_C1_sain` |

## 6. Essai à blanc v66 (script `lancer_essai_a_blanc_v66.sh`, 13:05:08 → 13:06:03)

Commande : `bash lancer_essai_a_blanc_v66.sh /home/user/organisme-v65-cl SORTIES PYTHON /home/user/controle-ia-travail/registres/go.md CONFIGURATION_V6` ;
fournisseurs simulés, deux générations, exécuteur factice déclaré. Sorties dans `essai-a-blanc-v66/`. Le code joué est celui de la tête `7e415cb` : le jalon 3 ne change que des essais et le banc. Le manifeste dit `3ba4727`, arbre modifié, parce que le banc n'était pas encore committé.

| étape | quoi | code | issue |
|---|---|---|---|
| 1 | `--bac reel` (pas de `bwrap` ici) | **2** | « BacASableIndisponible : … bwrap absent … aucun repli sur l'exécuteur factice » ; aucune sortie |
| 2 | course `--bac factice` | **0** | relevé `81b7fb54…` ; 24 cartes, 18 lois plantées, 2 générations |
| 3 | lecture (empreinte donnée) | **0** | **C1** ; A1 d'office (bac réel partout : faux, dit) ; V1, V2 promues puis survivantes ; V3, V4 non promues (P3, mesure) ; fausses : plus grand log W max −0,145 ; T-ELIM promue puis éliminée ; T-MAL refusée au gardien ; P6 tenue ; recherche : 0 touche hors de la loi gelée, 192 dedans ; phrase « course à blanc, exécuteur factice » |
| 4, 5 | refus de modèle au 2ᵉ appel des proposeurs ; lecture | **3**, **0** | **C5**, rien de partiel en plus |
| 6 | part de Kimi à 0,5 USD | **3** | « part restante du relais kimi (0.2000 USD) sous le pire cas de l'étage (9.6000 USD) : arrêt avant l'étage » |
| 7, 8 | `--bras aleatoire` ; `--generations 3` | **2**, **2** | garde 20 ; D2 |
| 9, 10 | expérimentateur qui fabrique ses gains (contre-calcul en désaccord **pendant** l'étage) ; lecture | **3**, **0** | relevé partiel avec **12 cartes et 10 lois plantées jugées** (dont 3 promues), étage « en attente » ; **C5** (CLV65-02 a) |
| 11 | lecture sans `--releve-sha256` | **2** | refus (empreinte exigée) |
| 12 | blocs du texte | **0** | jeu `21b4b005…`, héritage `93dcf517…`, configuration `4743ddbe…`, 98 fichiers gelés |
| 13 | **vrai registre des GO** (lecture seule) | **0** | 255 identifiants, 34 lignes d'extension ; GO-2026-11-08-02 → 45 (montant seul) ; GO-2026-11-10-10 → 45 (part « organisme ») ; 40 et 50 refusés |
| 14 | dossier de course `configuration-v6/` | **0** | « configuration v6 conforme `4743ddbe…` » ; commandes résolues `commandes-v6/…` |

Constats : (a) comme en v65, le relevé n'est pas reproductible à l'octet (durées, chemins provisoires), les décisions le sont ;
(b) les doublures recopient L* : l'issue C1 à blanc est « trop belle » par construction, A1 le dit.

## 7. Bloc pour le texte, commandes exactes

`blocs-v66/blocs-pour-le-texte-v66.md` (`9933ee114687079bbf95af94b5e39cd898b69d1d197b4c48587d12692fee1b29`) remplace le bloc v65 du texte : bloc `empreintes-du-code-v66` (98 fichiers),
bloc `plan-gele-v66` (mêmes clés et valeurs que le plan v65, sauf `configuration_sha256` = `4743ddbe…` ; `go` =
GO-2026-11-08-02 par défaut, `--go GO-2026-11-10-10` dans l'outil pour l'autre), bloc `jeu-plante-v65` inchangé ;
`blocs-v66/heritage-depart-v65.json` (`93dcf517…`, inchangé).

Commandes (depuis `orchestrator/`, sur la machine à `bwrap`, **lanceur en superutilisateur**, après le scellement et la
contre-lecture ; `DOSSIER_COURSE` = le dossier `configuration-v6/` versé, avec `heritage-depart-v65.json`) :

```
POLE_ESSAI_BAC_REEL_NON_JOUE= python3 -I -B -m pytest -q -p no:cacheprovider essais/test_registre_go_v66.py essais/test_boucle_reelle_v66.py essais/test_lecture_boucle_reelle_v66.py essais/test_boucle_reelle_v65.py essais/test_lecture_boucle_reelle_v65.py essais/test_tour_ferme_v64.py essais/test_gardes_tour_ferme_v64.py essais/test_v59_boucle_fermee.py essais/test_v57b_cablage_verdict.py
python3 -I -B essais/mutations_boucle_reelle_v66.py --processus 4
python3 -I -B demonstrations/boucle_reelle_v66.py SORTIE_ESSAI --a-blanc --graine 20261110 --bac reel --utilisateur-bac 64097
python3 -I -B demonstrations/boucle_reelle_v66.py SORTIE --preenregistrement prereg/preenregistrement-boucle-reelle-organisme-v1-v<N>.md \
    --heritage-depart DOSSIER_COURSE/heritage-depart-v65.json --configuration DOSSIER_COURSE/configuration-boucle-reelle-v6.json \
    --moteur reel --confirmer-moteur-reel --registre-go CHEMIN/registres/go.md --go GO-2026-11-08-02 --bac reel --utilisateur-bac 64097 --verifier-seulement
(puis la même sans --verifier-seulement)
python3 -I -B demonstrations/lire_boucle_reelle_v66.py SORTIE LECTURE.json --releve-sha256 <empreinte du relevé>
```

## 8. Ce qui reste non éprouvé sans `bwrap`

1. Garde 3, cas sain, et garde 22 en situation : `bwrap --version` réel, sonde réussie, identité du témoin sur l'hôte = 64097,
   dossier racine en 0700 ; `test_sain_bac_reel_essai_a_blanc` (v66, v65, v64, v59) et l'essai à blanc `--bac reel`.
2. La branche réelle **après** la garde 22 n'est jouée ici qu'avec des doublures (gardes 22 et 15 remplacées, rôles à blanc à
   la place des rôles réels) jusqu'à `--verifier-seulement` : la construction des adaptateurs et commandes réels, la garde 15
   réelle, les portes de plafond des relais et **la mesure des jetons sur les vraies commandes** (le champ `usage` de leur
   dernière ligne JSON, lu dans leur code, jamais vu en sortie réelle) restent à voir sur la machine.
3. L'étage des tests de mort au moteur réel ; le banc et la suite sous numpy 2.5.3 (machine) ; tout appel aux relais.

## 9. Points ouverts pour la mère

1. **Empreinte de configuration de GO-2026-11-10-10** : la ligne exige « configuration v5 (`995eb918…`) » ; aucune configuration de
   l'organisme n'a cette empreinte (v5 = `bff138d8…`, v6 = `4743ddbe…`). À rapprocher avant la course (nœud si la ligne doit
   changer de lecture).
2. **Texte à reprendre** (brouillon → v<N>) : bloc v66 à la place du bloc v65 ; noms des programmes v66 ; dossier de course v6 ;
   lancement **en superutilisateur** avec `--utilisateur-bac 64097` ; `--releve-sha256` exigé ; GO cité (11-08-02 ou 11-10-10 :
   les deux sont lus) ; section 5 : préciser que les intervalles de Wilson portent sur les six parts par fournisseur de P7 et
   que les jetons sont lus dans le champ `usage` des commandes (sommes par relais) ; section 7, point 6 : les échos de la loi
   gelée dans les scripts de l'expérimentateur sont comptés « dans la loi gelée » s'ils sont écrits en JSON canonique, « hors »
   sinon (à relire à la main) ; section 8 : un relevé incomplet se lit C5, la liste des manques est celle de `completude` ;
   garde 23 (vue servie) et garde 7 complète à ajouter à la liste d'arrêt.
3. **Registre cité par la course** : le vrai `registres/go.md` est maintenant lu ; un extrait scellé n'est plus nécessaire.
   Un GO cité qui porterait plus tard une ligne d'extension serait refusé (règle 1 de `registre_go_v66`).
4. Contre-lecture courte du différentiel v65 → v66 par un autre modèle, puis rejeu sur la machine à `bwrap` (section 8).

## 10. Écarts à la consigne (dits)

- CLV65-01 : en génération 2, l'égalité des membres d'archive reste un écart de P6 (C4), pas un manque de complétude (C5) ;
  en génération 1, elle est un manque (garde 18). Raison : la ligne C4 du texte nomme ce cas.
- CLV65-07 : deux règles ajoutées à celle de la garde (GO à extension refusé ; enveloppe lue part par part) ; la règle des
  doublons est celle de la garde, à l'identique (équivalence essayée sur douze registres).
- Banc : le banc v66 juge « tuée » seulement **pour la raison attendue** (un essai nommé en échec) ; une mutation tuée par un
  autre essai est comptée à part. Une mutation équivalente trouvée en écrivant le banc (le contrôle « part nommée deux fois »
  du lecteur de GO, redondant avec « nombre étranger ») a conduit à **retirer le contrôle redondant** plutôt qu'à déclarer la
  mutation ; de même le contrôle « loi plantée servie » de la lecture, remplacé par « loi plantée retenue » (les vues servies
  étant comparées exactement).

## 11. Livraison (`docs/notes/organisme-boucle-reelle-v1/code-v66/`, chaque fichier scellé par son compagnon)

58 fichiers, dont ce rapport, chacun avec son compagnon `.sha256` écrit par `controle_ia.scellement sceller` (les compagnons écrits par l'organisme ont été retirés et refaits). Le paquet git `organisme-v66-boucle-reelle-v1.bundle` va de `cef5ea60..prep/organisme-v66-boucle-reelle-v1` : il exige `cef5ea60` et porte la tête `7e415cb`, vérifié par `git bundle verify`. Le patch `organisme-v66-contre-cef5ea6.patch` (`git format-patch`) contient les trois commits. Dans `essai-a-blanc-v66/`, il y a en plus les 28 fichiers `etape-N.stdout` et `etape-N.stderr`, scellés un par un.

| sha256 | fichier |
|---|---|
| `9933ee114687079bbf95af94b5e39cd898b69d1d197b4c48587d12692fee1b29` | `blocs-v66/blocs-pour-le-texte-v66.md` |
| `93dcf51715f7a1aa4f313e9e1761c5a375a275d572ffcdb6969fbfaf2fb623c1` | `blocs-v66/heritage-depart-v65.json` |
| `5eae1a0468430e243c3c4e099b3969f949f62add688531aafdd7f0f44e036e55` | `configuration-v6/commandes-v6/commande_argon_v56_nuit_v6.py` |
| `889309305aeb37de9801c2f40c31769fd268abded1ac61ea94196fd0d51195ae` | `configuration-v6/commandes-v6/commande_kimi_v6.py` |
| `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | `configuration-v6/commandes-v6/registre_depense_cumulee_v1.py` |
| `4743ddbe4d294643ac8e1924476dec056b1a08dac9f8010cd647dd1861160b0d` | `configuration-v6/configuration-boucle-reelle-v6.json` |
| `036de84a297f5c3e402caeb9069e4d8eb9d0d3ec4ef86a5fc6a039022c8b3874` | `configuration-v6/pieces/concepts-mini-course-v1.json` |
| `4b15b31add9fe8e3ae5a18a309fdc9a7165da3be0533c5240dd9854ba08e14e9` | `configuration-v6/pieces/consigne-aiguilleur-mini-course-v1.md` |
| `df57bc9117e85b6a032355159a84451c4fe60a5c44793c5986ac6b1a89c45bd9` | `configuration-v6/pieces/consigne-juge-mini-course-v1.md` |
| `016789aeb9fc4177d865634882e1e5bc18053d0a16b72ccc83c7abbc6fbcb636` | `configuration-v6/pieces/consigne-lecteur-mini-course-v1.md` |
| `95b92e325ca95ded574073db8d13dcc8886c475d30dd01317c31fc40b96609e4` | `configuration-v6/pieces/consigne-metteur-mini-course-v1.md` |
| `98185e70f5d4bd3f0574b7517858efbec982d6decea0e5493da6abe12e9607b1` | `configuration-v6/pieces/consigne-proposeur-mini-course-v1.md` |
| `e2217482b0c1467f03d392a85d0af805a33a16fa99091b7b1f75e86fc5083eb0` | `essai-a-blanc-v66/journal-essai-a-blanc-v66.txt` |
| `200194a2ef837558bfeead039d9661200c4a1bc09853a4fbc3f5a72284bd9040` | `essai-a-blanc-v66/lecture-course-arret.json` |
| `44148413cd59944e142f99a98c0e4a07c2021247a44805a619fc4dda0084c432` | `essai-a-blanc-v66/lecture-course-etage.json` |
| `11ac361ff8a7a054f7edfba1ef0e7b2ba79155a4dca83616dba99c3517b94816` | `essai-a-blanc-v66/lecture-course.json` |
| `383aba8d9dc34fa967e614d12088be5644c89317b222a8d61d16a33be43d7e94` | `essai-a-blanc-v66/manifeste-course.json` |
| `bceda8bb762a92bf5edc544f360f782b458d25e7fafd5a012f0bdf88a9fa65f6` | `essai-a-blanc-v66/releve-course-arret.json` |
| `127a742de5b2bafff8741da77e0c37a58541f33317e8591803d91bc6bf6de787` | `essai-a-blanc-v66/releve-course-etage.json` |
| `81b7fb544c70d4debe014af8c1c61fbd5e860ace1b86e7764382d04dd5ac160d` | `essai-a-blanc-v66/releve-course.json` |
| `2fc70c74bf381a03606a6e56ea35e129d5cd964ccac185a31e6ab8132cee5dd3` | `heures-suite-et-banc-v66.txt` |
| `6e864ed6f42fcb5d0539c652b9166d863d7ddc91df8090bf2fbabc1bbbd21519` | `lancer_essai_a_blanc_v66.sh` |
| `96bd635c98dc7c86e9aaa698010ac6c0153257f6d952d6e46b49879c1cbcb9fa` | `mutations-v66-final.json` |
| `3518c92365ee7891a1672e038afc80561dbb2bd16c0b566c8cbbfad4bf9aeb16` | `mutations-v66-final.txt` |
| `45630acfd5aa8763b08aa8fd1da410132924f47bd96b3c556da8d80647374501` | `mutations-v66-premier-passage.json` |
| `1cbeada19a0276267ba3f2766d6a0fd65f29abb7416817836861307a905dd245` | `mutations-v66-premier-passage.txt` |
| `84ab119f0b3eefdd689b4be03f03bb776ebd2c7c1247b9d76e903181a419b1bc` | `organisme-v66-boucle-reelle-v1.bundle` |
| `d489f013b0bacbef82d5987a3a3a5777b069b9d643da37361ccf843c40c2618a` | `organisme-v66-contre-cef5ea6.patch` |
| `0fc19e8962971baceff7b58457c3a390ec3e3df82b7649840e0dd3b26b4f7ddb` | `suite-v66-final.txt` |

