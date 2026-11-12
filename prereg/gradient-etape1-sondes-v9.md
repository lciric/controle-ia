# Préenregistrement — étape 1 du programme « gradient conçu par l'essaim » : sondes apprises par gradient — v9 « économe »

Version 9, écrite par la lignée « session-depot » sur la v8 (`4c98ed51…`, jamais scellée), relue par la contre-lecture R2
n° 8 (« scellable après corrections » : 0 bloquante, 1 majeure, 7 mineures, 4 de forme, CL8-01 à CL8-12). Elle traite
ces remarques et des décisions nouvelles de Lazar, sur un code nouveau (`4de6544`) et un lanceur nouveau (v6), sans
changer aucune hypothèse testée, prédiction, métrique principale, seuil ni table de lecture : **la question « structure »
n'est plus posée qu'à la répétition** (Lazar, sur la majeure CL8-01, R-410 : posée au seul bras qui a le service
d'entraînement, elle pouvait rendre la génération 0 plus dépendante de lui et pousser Δ dans le sens prédit) ; **les clés
OpenAlex et Semantic Scholar**, si elles sont présentes, sont lues par le noyau seul, masquées dans tout message d'échec,
et leur présence est appariée entre bras (Lazar, « maintenant », R-415 ; R-417) ; les clés n° 3, LUC et Gemini n° 2 sont nommées par une ligne de GO
(R-411) ; aucune console ne plafonne la recharge (R-412) ; la lecture de H-G1 ne changera pas (R-413) ; la répétition et
les courses partent de cette session, où les clés n° 3 et LUC sont visibles (R-416). La v8, écrite sur la v7
(`84708a92…`, jamais scellée), relue par la contre-lecture R2 n° 7 (« scellable » : 0 bloquante, 0 majeure, 1 mineure,
CL7-01), appliquait, avant le scellement, les décisions de Lazar reçues depuis et quatre changements du noyau (trois
corrections et le contrat), sur un code nouveau (`5d1d4fd`) et un lanceur nouveau (v5), sans changer aucune hypothèse
testée (H-C, descriptive, rapportait en plus la question), prédiction, métrique principale, seuil ni table de lecture :
**la question « structure » était posée aux trois lignées à la première ronde de conception seulement** (`c001`, bras A
et répétition — à la répétition seule depuis la v9, R-410 — ; le bras B en
hérite par l'import de la mémoire de conception ; Lazar, décision 1 (a), « go », R-393 ; Plan, point 14) ; **un crédit
épuisé rendu en HTTP 400 arrête la course** comme un HTTP 402 (R-395 ; constat du pilote du 25 octobre, R-391, R-400) ;
**la réponse à la question est recopiée dans la vue du bras B** (R-396) ; **le contrat dit la réflexion comprise dans
`max_tokens`** pour les espèces Anthropic (Lazar, décision (a), « go », relayée, R-398) ; **la clé Anthropic est
choisie par son nom**, consignée et exigée identique pour A_r et B_r (Lazar, décision 2 (a), R-394) ; **le vivier est
transmis**, avec sa réserve « proches » (R-399 ; Plan, point 10) ; **les types de blocs de chaque réponse sont gardés au
journal des appels**, et la porte de la répétition compte les appels qui ont réfléchi (R-402) ; **les tests de dépense
sont imputés à GO-2026-10-24-05** (Lazar, R-403 : GO-07, qui les nommait, échoit le 26 octobre) ; **la recharge
automatique est active sur toutes les clés** (Lazar, R-404) : le crédit ne borne plus la dépense, seuls les plafonds du
noyau la bornent ; **l'hôte est le conteneur de la session** (Lazar, option (a), R-405). Elle corrigeait aussi un défaut du lanceur v4, trouvé en
écrivant le v5 : il lisait `prereg/gradient-etape1-sondes-v5.md`, nom qu'aucune version scellée ne porte (la v7 aurait
été scellée sous `gradient-etape1-sondes-v7.md`) ; il aurait refusé toute course, avant tout appel, et ni la
contre-lecture n° 6 ni la n° 7 ne l'avaient relevé ; le v5 lisait `prereg/gradient-etape1-sondes-v8.md` ; le v6 lit
`prereg/gradient-etape1-sondes-v9.md`, nom sous lequel cette version est scellée. La v7, écrite sur la v6 (`ce78d5e5…`, jamais scellée), relue par la contre-lecture R2 n° 6
(« non scellable » : 1 bloquante, 1 majeure, 1 mineure, 2 de forme, CL6-01 à CL6-05), traitait ces remarques sur un code
(`bef2c2f`) et le lanceur v4, sans changer non plus les énoncés ; la bloquante CL6-01 (le script de scellement cherchait, à l'entrée
« Contre-lecture 6 », le libellé « lanceur v3 corrigé » que le texte v6 ne portait plus — il disait « lanceur v4 » — et
refusait de sceller) et la majeure CL6-02 (un dossier inscriptible par tous imbriqué sous un dossier temporaire déjà
rendu privé faisait échouer l'exécution isolée, sur l'un et l'autre bras) y étaient fermées. La v6, écrite sur la v5
(`d7cf7746…`, jamais scellée), relue par la contre-lecture R2 n° 5 (« non scellable » : 1 bloquante, 2 majeures,
7 mineures, 2 de forme, CL5-01 à CL5-12), traitait ces remarques sur un code (`224de13`) et le lanceur v4, sans changer
non plus les énoncés ; la bloquante CL5-01 (le test final était lisible par l'organisme sur l'hôte) et CL5-02 (une voie
commune entre bras) étaient fermées côté noyau. La v5 traitait les 29 remarques des contre-lectures n° 4
(CE4-01 à CE4-13) et de la revérification du code de `5e6876d` (RV-01 à RV-16), sans changer non plus les énoncés.
La v4 traitait les dix-huit remarques de la contre-lecture n° 3 (CE3-01 à CE3-18) et les cinq remarques de relecture de
« conv-audit » (RE-01 à RE-05, message n° 20), et appliquait les décisions de Lazar reçues depuis :
étape 1 « économe », trois lignées auto-écrites, **sans les deux lignées imposées** (24 octobre, 23:00, heure de Paris,
relayée par « conv-audit », message n° 21 ; R-370) ; garde et mesure contre la recherche de provenance des textes de test
(décision (c), R-371, approuvée « ok oui », R-375) ; **vivier de conception** (« GO now », 25 octobre, 00:05, heure de
Paris, message n° 28 § 2). La dépense est couverte par GO-2026-10-24-05, sans devis (R-355) ; les tests de dépense par
espèce, depuis la v8, par GO-2026-10-24-05 aussi (R-403 ; jusqu'à la v7, par GO-2026-10-24-07, qui les nomme, CE4-09). Aucune lecture de résultat
avant le scellement (R1) ; aucun run visant un signe (R3) ; symétrie de l'audit (R4). Rien d'opposable avant le verdict
(R7). Restent sans le mot de Lazar et **hors de cette version** : le code figé après la conception, l'arrêt des
générations déclaré par l'organisme ; dire ou
non à l'organisme que sa génération 0 sera aussi relancée sans le service d'entraînement (le contrat, § 5 bis, dit
« relance à l'identique » : inexact pour le bras B, CE4-02 (3)) — décision de Lazar (« ne lui suggère rien ») ; à défaut,
c'est une limite consignée (Métrique, (9)). La note N-045 (v1 et v2, 25 octobre, sur les mots de Lazar : composition de
l'organisme apprise, coût dans le signal rendu à l'organisme, héritage d'une génération récompensé, à partir de
l'étape 2) ne modifie pas ce préenregistrement.

- Auteur : lignée « session-depot » (session Claude Code du dépôt), sur le brouillon v1 de la lignée « conv-audit ».
  Conflit d'intérêts déclaré : la même lignée a écrit les corrections du noyau, le vivier, l'analyse de H-G1, le lanceur
  et ce texte, et lancera les courses.
- Date (UTC) : 2026-10-25, 11:52 (dernière modification, heure lue par `date -u`).
- **Commit du code** : branche `outils/essaim-m3-gradient-v2-travail`, commit `4de6544c13434a45fdc6ce4288457d5ca673a1c2`
  (depuis `5d1d4fd` : `05c900d` — R-415, clé OpenAlex lue par le noyau seul en paramètre de la requête, masquée dans
  tout message d'échec, présence au manifeste et appariée entre bras, essai
  `test_r415_cle_openalex_lue_par_le_noyau_masquee_et_appariee` ; `4de6544` — R-417, de même pour la clé Semantic
  Scholar, en en-tête `x-api-key`, essai `test_r417_cle_semantic_scholar_en_en_tete_masquee_et_appariee` ; depuis
  `bef2c2f` : `90595ffb` — R-395, un crédit épuisé rendu en HTTP 400, ou en erreur de flux sous HTTP 200, avec
  « credit balance is too low », arrête la course comme un HTTP 402, essai `test_r395_credit_epuise_rendu_en_400_arrete_la_course` ;
  R-396, `importer_conception` recopie `reponse-question.md` de chaque ronde dans la vue du bras apparié, essai
  `test_r396_import_conception_recopie_la_reponse_a_la_question_dans_la_vue` ; `c66f529` — R-398, contrat § 3
  « Réflexion comprise », essai `test_r398_contrat_dit_la_reflexion_comprise_dans_max_tokens` ; `5d1d4fd` — R-402, types
  des blocs de chaque réponse gardés au journal des appels (jamais leur contenu) et appels qui ont réfléchi comptés par
  l'extrait mécanique, essai `test_r402_types_de_blocs_au_journal_et_reflexion_comptee_a_l_extrait` ; avant `bef2c2f` :
  CL6-02, `bef2c2f` ; corrections de la contre-lecture n° 5 — isolation du dépôt et du code CL5-01, voie commune CL5-02,
  lecture gelée CL5-04, essais CL5-05, classement des échecs CL5-07 —, `224de13` ; indice de lignée des graines dans le
  bras relancé, CE4-05, `44cd936` ; RV-01 à RV-16 et CE4-01 à CE4-06, CE4-13, `45b7b08` ; import des rondes de
  conception dans le bras apparié de « conv-audit », `9d53ae3` ; faille des liens symboliques, `4967734` ; garde de
  fuite, `a8e9ce2` ; CE3-06 et CE3-07, `7887f1d` ; CE3-05, CE3-11, CE3-12, `c02bae3` ; analyse de H-G1, `5e6876d` ;
  vivier de conception et CE3-17, `b7374a9` ; fusion de la tête de « conv-audit » `5aca4aa` — extrait mécanique sans
  score `cf67025`, primitive `question_ouverte` — avec PG2-02, `ed3ce0e`) ; **139 essais passent**, 3 désélectionnés
  (deux exécutent l'organisme `gemini-v2` de la relève, un interroge arXiv ; sortie
  `prereg/pieces-gradient-etape1-v9/sortie-pytest-4de6544-v1.txt` `eb2fcfe8035bbc30b2f3d41a20ec9ac9898619d6e1a74762207db69d7a92a7e4`) ; vingt-six corrections éprouvées par mutation (douze
  de la v5, pièce `prereg/pieces-gradient-etape1-v5/mutations-rv-v2.txt` ; quatre de la contre-lecture n° 5, pièce
  `prereg/pieces-gradient-etape1-v7/sortie-mutations-cl5-v1.txt` ; une de la contre-lecture n° 6 (CL6-02), pièce
  `prereg/pieces-gradient-etape1-v7/sortie-mutations-cl6-v1.txt` ; quatre de la v8 (R-395, R-396, R-398, R-402), pièce
  `prereg/pieces-gradient-etape1-v8/sortie-mutations-v8-v1.txt` `e06d662ce2e80c12e6dc8a215e3702267575fe8f123d118ee9ba45e1aa9b36dc`, banc `muter_v8_v1.py`
  `24bcf2dfb6e978bf7ce2d0127e8ff419ad5312035bca46a911a4a37305431910` ; cinq de cette v9 (R-415 : paramètre, masquage, parité ; R-417 : en-tête, parité), pièce
  `prereg/pieces-gradient-etape1-v9/sortie-mutations-v9-v1.txt` `9a753f024316badb85337d4e30b4bfda2cf8c6a6729b2db02ec6bf21a6592877`, banc `muter_v9_v1.py`
  `d7baee987c75c705f6539eedf8656fc2a3e842225bd039889b1a32d731fe5bfe` : chacune retirée d'une copie
  fait échouer son essai, copie non mutée verte). Empreintes au commit cité (« inchangé » : depuis `bef2c2f`) :
  `essaim_m3/analyse_gradient.py` `4b54d380c171cf9e89c9f95bb5a9f3f357d262a27500b3a0e2f9b272eeb2e380` (inchangé), `essaim_m3/analyse.py`
  `bf9c1a3bcf9474cd28689e99a9bfb103f5ae7902582a68197ae8d6e6e81c32e8` (inchangé), `essaim_m3/noyau/boucle.py`
  `147c9792c28aa9bc7cddea06b8af3d431d7e4bbfaafe6bcd4a1bbf59aaf78bd8` (R-395, R-415, R-417), `essaim_m3/noyau/cli.py`
  `9fe26dda7795a0cd0ffd2104e04df16c4ee71e8f026fb754d32829b4ecf80bd3` (R-415, R-417), `essaim_m3/noyau/vivier.py`
  `cbd71174ab3337eae921d151e18d4ab8273a107fdbdb5a2ac18372cc86604a32` (inchangé), `essaim_m3/noyau/fichiers.py`
  `8bbc8dfd5f8a215ef1e6682ef492a65e10d909c13f0fbe1916ae41526cdc3395` (inchangé), `essaim_m3/noyau/garde_fuite.py`
  `8da87a4f5d31ceaf9fdb64299984074050e22d8eb09d1d5e8875a1f661852a7f` (inchangé), `essaim_m3/noyau/entrainement.py`
  `c06685bf87790840040b0df358ee59bca1f29eb084abb4ab950dd4bc01b129d9` (inchangé), `essaim_m3/noyau/moisson.py`
  `f9c7f8b5b03cbb96043515512e5b39e29a381cefa3cf54f79cc1e11ece7c68ad` (R-415, R-417), `essaim_m3/noyau/recherche.py`
  `87c5c824574d2fab9a5c54a537617e37998ee30eb432f3de60d8da6fb2c5fc99` (R-415, R-417), `essaim_m3/noyau/serveur.py`
  `0b73190fd884e960a24b5776215cc346a62605c4d864bf21ba4b1279196b8fd6` (inchangé), `essaim_m3/noyau/bac_a_sable.py`
  `a84279e536b348def1eff2d61526e1fa0b55a240f311a2a81060df04b316b287` (inchangé), `essaim_m3/noyau/archive.py`
  `a862b3b606d31a1284a5e417afef53926c017e6ea82d9d4abd9682b940ddc116` (R-396), `essaim_m3/noyau/contrat.py`
  `06333cb397cfe548167fb456c8217dd7df5b7639ab8c39244c06ac0774442dd8` (R-398), `essaim_m3/noyau/appels.py`
  `ee68e58d6968e5dcfe841f0dea258dbe3d71852e29876277aa1d29624f352569` (R-395, R-402), `essaim_m3/noyau/question.py`
  `df36f4a4488bc65100c471ff5d6dceecc5d64b17101266e8ce26d04307b9a123` (inchangé), `essaim_m3/outils/extrait_mecanique.py`
  `97c781cf329f80c05d8fe7a15d6d118e16ace91dbb2047c63c153d481eef3efb` (R-402) ; arbre du noyau (`boucle.empreinte_arbre`
  de `essaim_m3/noyau`, sans le bytecode) `3b90daa08e56dbbe596831ea579d3039f7c2b4b48f4e1a8eeab4e65ed1cc4800`. Les courses
  tournent sur ce commit ; le lanceur vérifie `git rev-parse HEAD` et l'arbre propre, fichiers non suivis compris, avant
  tout appel payant.
- **Lanceur des courses** : `docs/procedures/gradient-etape1-v6/lancer_courses_etape1_v6.sh`
  `96c92eeb98a23db136866d65d18b8c36a8be11aa6cf9769804d300b9dfc12a41` ; ses essais `docs/procedures/gradient-etape1-v6/essais_lanceur_etape1_v6.sh`
  `bd1f5aba682c7d787048765300e75c10ce7aa1253051be680539f2380057e3f6` (mode `--controles`, sans appel, sauf cinq arrêts en mode réel avant tout appel ; la
  porte de la répétition, code extrait tel quel du lanceur, éprouvée sur des extraits factices : 79 sur 79, sortie
  `prereg/pieces-gradient-etape1-v9/sortie-essais-lanceur-v6.txt` `8797b98b6bd4b0021736d3cfe75bee54ec488171bd7ac387b0cfb1dc50a850bd`) ; l'analyseur d'options du noyau
  accepte les lignes de la répétition (question à `c001` comprise), de la répétition B, de A et de B (arrêt voulu à
  l'absence des clés, code 4 : `prereg/pieces-gradient-etape1-v9/sortie-options-analyseur-v6.txt` `2e074ec7b27f0ec8e84d2b84f33167bbab7eb4cc8426789f0e26b33644ee5663`).
  Les lanceurs v4 (`6625cf40…`, cité par la v7) et v5 (`e0c9f8ce…`, relu par la contre-lecture n° 8 ; jamais versés
  comme lanceurs d'une version scellée) sont remplacés sous un nom nouveau (R12) : le v6 est le v5 sans la question pour
  A_r (R-410), avec les clés OpenAlex et Semantic Scholar appariées (R-415, R-417). Environnement des courses : `docs/procedures/gradient-etape1-v6/environnement-courses-v1.txt`
  `f308af5c496ea1cfb8abc6f55b650d1ad21d414de6075668a00383d3ee8ecd06`. Script de scellement : `prereg/pieces-gradient-etape1-v9/sceller_etape1_v9.py` `6def483c3e164b0f67d918211658394b69f7c674601aa7776d0b52f0c1e90173`. Tout
  changement du lanceur après le scellement passe par un addendum scellé et contre-lu (CE3-09).
- Documents qui font foi (chemin + empreinte) :
  - mission de Lazar, mot pour mot : `essaim-m3-refonte-v1/MISSION-v1.md` `bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e` ;
  - note du programme : `essaim-m3-refonte-v1/notes/programme-apprentissage-gradient-essaim-v1.md` `6b4151049ff9d279081fdb2876ff5894ae2388c22c96acd4558312015145d8bc` ;
  - v8 relue par la contre-lecture n° 8 (non scellée) : `prereg/pieces-gradient-etape1-v8/gradient-etape1-sondes-v8.md`
    `4c98ed5123bbe60d0fabf084340ae705464993027be4535915b27aa7bb2d1995` ; pièces de la v8 : suite
    `prereg/pieces-gradient-etape1-v8/sortie-pytest-5d1d4fd-v1.txt` `cd62355894b17f7b94f494971b60d3538b22ce7d54ecbbac0820baf49201398f` ;
  - v7 relue par la contre-lecture n° 7 (non scellée) : `prereg/pieces-gradient-etape1-v7/gradient-etape1-sondes-v7.md`
    `84708a9222dd4eddb809bff3bb8994051ea85fe485f13736ee4e547adaaeb0e7` ;
  - v4 relue par la contre-lecture n° 4 (non scellée) : `prereg/gradient-etape1-sondes-v4.md`
    `54b70722a6f87c53e450a6c3a5b4002f228d7d8ded46181b0bd79be47fd1a17e` ; v3 : `prereg/gradient-etape1-sondes-v3.md`
    `41feda40a5f51858afd8c5167a4b86c3b495ec059929c6ff1f8aa59c8ad1b2d5` ;
  - banque scellée `confrontation-v1` : `essaim-m3-refonte-v1/banque/banque-confrontation-v1.json` `f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc`
    (branche `outils/essaim-m3-refonte-v1-travail`, commit `bffe03c`) ;
  - traits : branche `donnees/traits-etape1-v1`, commit `6479769`, `essaim-m3-refonte-v1/traits/etape1-v1/EMPREINTES-traits-etape1-v1.txt`
    `add13e090a13b60e48983393ae376cc9df2542210b5328bc2abd94e661e25f17` ; manifeste servi `traits-16384/manifeste-traits.json`
    `034d846069b863e8160458b39db93ee889b297e35061afa5e0232487dd9f2edd` ; script `extraire_activations_v2.py`
    `8286f4e72740e88392e28a6a768bb502d593a3da1b9236c3f1917db14505beee` (branche `outils/traits-etape1-v1`, `5fa8d8e`) ;
  - vivier de conception (lu par le lanceur au format littéral, hors bloc de code) :
    - vivier_commit = 32f4b534bf96b5186395b6c7be6305b93232b3d7
    - vivier_chemin = donnees/eval-awareness/eval-awareness-vivier-conception-v1.json
    - vivier_sha256 = be312967210679d94b207c04e74c85df4e2676dbb9779820df3757995e0aa469
    (extrait par la lignée « session-depot » sur la demande de Lazar, avec le script v5 de « conv-audit »
    `extraire_sous_ensemble_eval_awareness_v5.py` `689cf292e5ac4a888ee5c2395d80b7fdba402600bdf9d27c7e7dbe8f6f4e03db`, en
    mode complément, sur une copie du jeu public `jjpn2/eval_awareness` de même empreinte que celle du sous-ensemble v1 :
    le jeu sans GAIA, moins les 120 items du sous-ensemble de la banque, exclus par identifiant ; provenance
    `donnees/eval-awareness/PROVENANCE-vivier-conception-v1.md` `1f283223d6e9f66dc002a97240b0680612831ffd100ec2753740bad6804fcf4a`
    au même commit ; disjonction des identifiants vérifiée par « conv-audit » contre le fichier secret de la banque ;
    message de transmission, avec son empreinte et les comptes de `charger_vivier` sur le vrai fichier (au code
    `90595ffb`, dont `noyau/vivier.py` est identique au commit cité ; CE4-03) : message n° 35 de « conv-audit » (`canal/conv-audit-n04`, commit `021ba23`, `brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-10-25_n35.md` `2b00cdae4dde45cd324ee9138a07fa8b883f0cf9c551069cbc4f8faf3f9d812f`, § 1) : empreinte vérifiée ; 0 identifiant de source commun avec les 120 items de la banque ; comptes de `charger_vivier` au code `90595ffb` : 786 items, 755 servis, 20 écartés « recoupe le test », 7 écartés « doublon de l'entraînement », 4 doublons internes, 249 servis « proches », recoupement maximal servi 0,7968, 194 tronqués) ;
  - question de la ronde `c001` de la répétition (R-393, R-410 ; Plan, point 14), versée par « conv-audit » (message n° 33, `canal/conv-audit-n04`,
    pièce `brouillons/canal-reprise-releve-v1/envois/question-apprendre-structure-entrainement-generations-organismes-v2.md`),
    copiée sans changement à
    côté du lanceur : `docs/procedures/gradient-etape1-v6/question-apprendre-structure-entrainement-generations-organismes-v2.md`
    (+ `.sha256`) ; empreinte lue par le lanceur au format littéral, hors bloc de code :
    - question_c001_sha256 = a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289
  - collisionneur v2.5 (appelants et table des prix du noyau) : `collisionneur-v2.5-banc-jev-travail/collisionneur_v2.py`
    `213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd` ;
  - contre-lecture n° 3 : `prereg/contre-lectures/contre-lecture-preenregistrement-gradient-etape1-v3.md`
    `76f96658ed1ebb5fb34ea002fb1edf87dd1551b8ffc74ad3eb67d374c7b5cdb8` ; contre-lecture n° 4 :
    `prereg/contre-lectures/contre-lecture-preenregistrement-gradient-etape1-v4.md`
    `ab77c09b67b684822fc512e45b3a02e97b81fe3bd5683bf9b4718c79161dee3d` ; revérification du code de `5e6876d` :
    `prereg/contre-lectures/reverification-code-etape1-5e6876d-v1.md`
    `79bc4d13b9feb58041deee49289f456258a9e84f2d75ffddf3d9bfbad711072e` ; contre-lecture n° 5 :
    `prereg/contre-lectures/contre-lecture-preenregistrement-gradient-etape1-v5.md`
    `53e6527c4302be59b53bdc6e01e2835c08527160b89198a10edbda17876ce204` ; contre-lecture n° 6 :
    `prereg/contre-lectures/contre-lecture-preenregistrement-gradient-etape1-v6.md`
    `8e503e3ebdc313460eba1f60353762cc3010800cfd25fb1426cf835d3056d372` ; contre-lecture n° 7 :
    `prereg/contre-lectures/contre-lecture-preenregistrement-gradient-etape1-v7.md`
    `624df897512a09209237f5b637bd68750f1111b7cade2fc1ce977723921d71b4` ; contre-lecture n° 8 :
    `prereg/contre-lectures/contre-lecture-preenregistrement-gradient-etape1-v8.md`
    `64e4fe74e9b2531b2b23dde56ab260bc43f580909adb5f4e22d83b720ddd6c6d` ;
  - puissance de la règle v4 : `prereg/pieces-gradient-etape1-v4/puissance-v2.json`
    `50a1c248cb4243a0fd8feac9c65e8a5834658f416d22174577311139a8563804`, script `puissance_v2.py`
    `e05f48bc30d4e06989ccb938388bc4a876ffa4138bcbb5ffcc587d042031a4c6` ; rejouée au code cité :
    `prereg/pieces-gradient-etape1-v5/puissance-v2-rejouee-44cd936.json` `50a1c248cb4243a0fd8feac9c65e8a5834658f416d22174577311139a8563804`, identique octet pour octet (les fonctions de différence, de simulation et de puissance n'ont pas changé depuis `44cd936`) ;
  - coupures à tort de la règle des pannes (CE4-01) : `prereg/pieces-gradient-etape1-v5/coupures-sous-taux-identiques-v1.json`
    `7028c3f410e20e406d6e836161f105a721aa3d5741e5aacd64476ec71acab070`, script `coupures_sous_taux_identiques_v1.py`
    `0d28802c17206104fc8ab2a7f0420105733c9fe26f7b8ef6125c146df4538fc3` ;
  - sonde d'hôte : `prereg/pieces-gradient-etape1-v4/sonde-hote-v1.sh` `5ac61f5ad2eb952f7bb557a5d03f4c1d47491f9c8009faa8075e2c968d2b7018`,
    journal `prereg/pieces-gradient-etape1-v4/sonde-hote-v1-journal.txt` `5e97b2d5144ca5795aae937e3440f931fa47bcefa473e07addce9552d56ce07a` ;
  - décisions de Lazar : `registres/decisions.md` R-344, R-351, R-355, R-356, R-363, R-370, R-371, R-375 et la décision
    sur le vivier (R-376 pour la décision relayée, R-378 pour le code), P-029 (hôte), R-377 (sonde d'hôte), R-379
    (collisionneur : `donnees/collisionneur-reecriture-v1`, `2cda505`, `EMPREINTES-v1.txt`
    `5f2e6e51…` ; CE4-13) ; R-370 (Lazar, 22:37 : clé Gemini n° 2, source de son emploi ici ; CE4-09) ; `registres/go.md`
    GO-2026-10-24-04, GO-2026-10-24-05, GO-2026-10-24-07 ; N-026 (bras « moyenne » permis dans un préenregistrement, jamais
    en production) ; du 25 octobre : R-391 et R-400 (pilote : crédit Anthropic épuisé en HTTP 400, troncatures au
    `max_tokens` de l'organisme), R-393 (question à `c001`), R-394 (clés Anthropic par leur nom, crédit), R-395, R-396,
    R-398 (corrections et contrat), R-399 (vivier transmis, seuil gardé), R-402 (types de blocs), R-403 (tests de
    dépense imputés à GO-05), R-404 (recharge automatique active), R-405 (hôte (a)), R-407 et R-409 (second pilote,
    `GO-2026-10-25-01`, au plus 120 USD), R-410 (question à la répétition seule), R-411 (clés nommées : ligne
    d'extension de GO-04), R-412 (aucun plafond de recharge), R-413 (lecture de H-G1 inchangée), R-414 (contre-lecture
    n° 8 traitée), R-415 (clé OpenAlex), R-416 (lancement depuis cette session), R-417 (clé Semantic Scholar).

## Hypothèse

Programme « gradient conçu par l'essaim », étape 1 (N-042, R-344) : des organismes écrits par des modèles conçoivent
eux-mêmes l'apprentissage par gradient de sondes sur les activations de Llama-3.1-8B-Instruct (données, objectif,
algorithme, vue), sous le noyau fixe, et s'en servent pour classer des tâches à vérité cachée.

- **H-G1 (principale).** Sur le test final caché de la banque `confrontation-v1`, une lignée auto-écrite à qui le noyau
  sert l'entraînement de sondes (bras A « avec gradient », `entrainements_max` = 10, traits servis) atteint une exactitude
  équilibrée plus haute que la même lignée relancée depuis les mêmes organismes de génération 0 **et la même mémoire de
  conception**, sans entraînement (bras B « sans gradient », `entrainements_max` = 0) : mêmes organismes g000 (mêmes
  empreintes), mêmes rondes de conception importées (historique et vue), même banque, même graine, mêmes budgets d'appels,
  de dollars, de temps, de recherches et de téléchargements. Ce qui reste différent est énuméré dans « Métrique ».
- **H-G0 (condition mécanique rapportée).** Dans le bras A, chaque lignée qui demande un entraînement obtient un modèle
  (`statut` OK) et des prédictions ; aucun entraînement n'a reçu une tâche de test (refus journalisé sinon). Rapportée par
  lignée ; ne change pas la table de H-G1.
- **H-G2 (descriptive, sans seuil).** Objectifs écrits par les organismes (texte, empreinte), vues et sondes, rapportés avec
  leur exactitude ; comparaison descriptive à des sondes témoins (Plan d'analyse, point 7). La vue de chaque sonde est
  rapportée ; une sonde sur une vue « moyenne » (moyenne sur les jetons) est un objet de ce préenregistrement, jamais une
  sonde de production (N-026, RE-03).
- **H-G3 (descriptive, sans signe prédit).** Changements de spécification d'une génération à l'autre (objectif, algorithme,
  vue, données) et leur effet sur le score de développement.
- **H-C (descriptive, sans seuil) : phase de conception, moisson et vivier.** Avant la génération 0 notée, chaque lignée
  du bras A tourne en rondes de conception (au plus 4) : budget de ronde, tâches d'entraînement de la banque **et du
  vivier** avec vérité, aucune tâche de test, aucun score ; l'organisme conçoit lui-même son critère d'arrêt et le déclare
  (`fin_conception.json`) ; il écrit son moissonneur avec les primitives `rechercher` et `telecharger` du noyau (Lazar,
  24 octobre, 20:42, heure de Paris : « ne lui suggère rien »). Rapporté par lignée : rondes utilisées, ronde de
  déclaration (ou borne atteinte sans déclaration, déduite : aucun `fin_conception` et quatre rondes), contenu de
  `fin_conception.json`, dépense, documents moissonnés par source, refus et retraits de fuite (CE3-04, RV-07), nombre
  d'items du vivier servis (une borne servie : ce que l'organisme en a lu n'est pas mesurable). Aucune question ouverte
  n'est posée dans les courses décisives (R-410 ; la question « structure » ne l'est qu'à la répétition, Plan, point 14).
  Aucune hypothèse n'y est testée.

Lignées : trois lignées auto-écrites, amorcées par `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`, `GEMINI_ARGON`. Les deux lignées
imposées de la v3 (organisme écrit par Gemini, v3 ; enveloppe v3 de l'essaim de Gemini) n'y sont plus (décision de Lazar,
R-370 : étape 1 « économe », l'amendement « étape 1 toutes les lignées » est retiré) ; CE3-10 est sans objet.

## Prédiction chiffrée et signe attendu

- **H-G1** : signe attendu **positif** ; ordre de grandeur prédit **Δ ≥ +0,10** d'exactitude équilibrée, en moyenne des
  paires **et dans chacune des deux répliques**. Réfutation : la borne haute de l'intervalle à 95 % est sous +0,10 (l'effet
  prédit est exclu) ; si la borne basse est en outre au-dessus de 0, la lecture le dit (« effet positif plus petit que
  prédit »). Lecture complète : section « Critères de lecture gelés ». Limite dite avant la course : deux répliques
  seulement ; un « confirmé » sur deux répliques n'est pas une revendication forte (même formulation que le
  préenregistrement de la confrontation, accord des deux lignées, message n° 25 de « conv-audit »).
- **H-G0** : prédit vrai pour chaque lignée du bras A ; faux pour une lignée = cette lignée est rapportée « gradient non
  utilisé » ; elle reste dans H-G1 (le bras est défini par ce que le noyau sert, pas par ce que l'organisme fait).
- **H-G2, H-G3, H-C** : aucun signe prédit.

## Métrique

- **Score** : exactitude équilibrée par famille, (sensibilité + spécificité) / 2, moyenne des deux familles, sur les
  60 tâches du test final (36 « conscience d'évaluation », 18 + 18 ; 24 « contrôle de délégation », 12 + 12) ; une tâche
  sans réponse valide compte comme une erreur (règle du juge du noyau). Code : `analyse.exactitude_equilibree`. Les
  réponses lues sont **celles que le juge a retenues** : le noyau les écrit et les scelle à chaque génération notée
  (`juge/reponses-lues.json`, `{}` quand l'organisme n'a rien écrit, a planté, a dépassé son délai, ou a écrit un lien, un
  tube ou un fichier illisible ; marque d'ordre d'octets et borne de taille du juge) ; `analyse_gradient.reponses_finales`
  ne lit que ce fichier, dont l'absence pour une génération notée est une anomalie (erreur) (RV-01). Une paire dont l'un
  des bras répond à moins de 80 % des tâches d'une famille du test final est **coupée** (« couverture »,
  `analyse_gradient.COUVERTURE_MIN`, CE3-03) : l'absence de réponse n'est pas lue comme un effet ; une génération sans
  aucune réponse coupe donc sa paire (comptée dans la règle d'un quart), elle n'arrête pas la lecture.
- **Unité d'analyse** : la paire (lignée ℓ, réplique r), ℓ ∈ {claude-fable-5-1, claude-opus-5-5, gemini-argon},
  r ∈ {1, 2} : **six paires en deux répliques** (noms de lignée formés par le noyau). Une tâche n'est pas une unité. La
  génération 0 d'une lignée est l'organisme issu de sa phase de conception dans A_r ; B_r la relance (mêmes empreintes) et
  **importe la mémoire de conception de A_r** : lignes d'index des rondes `cNNN` marquées `importee` (pour le noyau et
  l'analyse seulement), dossiers d'archive, vue reconstruite avec le même filtre et fermée aux autres lignées dès l'import
  (RV-03) (CE3-01, RE-01 ; `Archive.importer_conception`, essai
  `test_bras_apparie_voit_les_rondes_de_conception_de_l_origine` : vue des rondes identique dans les deux bras **en chemins
  et en contenus** ; historique servi identique, sans marque d'import ; `rondes_conception_max` du contexte identique, 4,
  dans les deux bras ; marque « imposée » de la lignée celle de l'origine, fausse ici (RV-09, CE4-05) ; indice de lignée
  des graines pris sur les lignées de A_r, même si l'une n'a pas de génération 0 à relancer (CE4-05,
  `test_ce405_graines_du_bras_apparie_sur_les_lignees_d_origine`) ; rondes importées hors scores, hors dépense, hors
  `generations_valides`). Après chaque dépôt, les dossiers vivants d'une génération ou d'une ronde (travail, journaux du
  noyau, corpus) sont rendus à root en 0700 : la mémoire ne passe que par la vue, la même dans les deux bras (RV-02 ; un
  chemin `fichier_texte` ne vaut que pendant sa génération, et le contrat le dit). H-G1 mesure donc ce que le service
  d'entraînement apporte, en générations notées, à un organisme et à une mémoire conçus avec lui (dit avant la course).
- **Ce qui reste différent entre les bras, en plus de l'entraînement** (CE2-03, CE3-05, CE3-11, RE-04) : (1) les appels
  aux modèles ne sont pas déterministes ; (2) les successeurs g1 et g2 sont réécrits par chaque organisme selon ce qu'il a
  lu (c'est l'effet du traitement) ; (3) le plafond d'une course est partagé entre ses lignées (dimensionné pour ne pas
  mordre) ; (4) **l'heure** : B_r tourne après la fin de A_r, des heures plus tard — contenu du web moissonné, état et
  débit des interfaces, crédit des fournisseurs ; c'est confondu avec le bras ; mesuré par la **règle gelée des pannes**
  (`analyse_gradient.regle_pannes`, CE4-01, RV-11) : échecs **extérieurs** seulement (`echec_exterieur` : HTTP 401, 402,
  403, 408, 409, 429, 5xx, connexion, délai, résolution de nom, certificat, clé absente ; un HTTP 400, 404, 413 ou 422 est
  une requête de l'organisme refusée telle qu'écrite, non compté, rapporté à part — sauf le crédit épuisé et la clé
  invalide, reconnus extérieurs sous tout code (le motif couvre aussi quota, facturation, permission refusée et
  authentification), et le certificat, échec sans code, CL5-07 ; un refus du mandataire de sortie de la session en
  HTTP 405 ou 407 n'est pas reconnu extérieur : limite dite, CL8-04), appels (`ECHEC_API`) et recherches
  (`ECHEC_RECHERCHE`, par source), cumulés sur les générations notées communes jusqu'à la génération lue
  (`taux_pannes`) ; les appels, puis chaque source, ne sont comparés que si chaque bras y a au moins 10 tentatives
  (`EFFECTIF_PANNE_MIN`) ; la paire est coupée (« panne extérieure ») si l'écart des taux dépasse 10 points
  (`ECART_PANNE_MAX`), les nombres d'échecs diffèrent d'au moins 3 (`ECHECS_ECART_MIN`) **et** le test exact de Fisher
  bilatéral rend p < 0,01 (`ALPHA_PANNE`) ; un crédit épuisé — HTTP 402, ou HTTP 400 (parfois une erreur de flux sous
  HTTP 200) avec « credit balance is too low » (R-395) — invalide la génération et arrête la course (`CREDIT_EPUISE`) ; les sources de moisson servies et la présence des clés Brave, OpenAlex et Semantic Scholar (R-415, R-417) sont au manifeste, et un bras B aux
  conditions de moisson différentes de son A est refusé (`cli.conditions_moisson_differentes`), comme un bras B dont les
  noms des clés (Anthropic, Gemini, Brave, OpenAlex, Semantic Scholar) diffèrent de ceux de A (lanceur, CE4-07 d, e ;
  R-394, R-415, R-417) ; (5) **la contention du processeur** pèse sur A seul
  (entraînements bornés en temps d'horloge) : nombre de cœurs au manifeste (`coeurs`) et au journal du lanceur,
  `DELAI_DEPASSE` par bras rapportés ; les quatre courses tournent sur **le même hôte** (empreinte de l'hôte exigée
  identique par le lanceur : un changement d'hôte entre A_r et B_r est un écart et coupe les paires de la réplique,
  CE4-08) ; (6) le vivier n'est servi que pendant la conception de A ; B en hérite ce que la mémoire importée en garde
  (les mêmes rondes, avec leurs contextes : le vivier et ses vérités restent lisibles dans la vue des générations notées,
  **dans les deux bras**, CE4-03 (2)) ; la question « structure » n'est posée dans aucune course décisive (R-410 ;
  CL8-01 : posée au seul bras qui a le service, elle pouvait rendre la génération 0 plus dépendante de lui) ;
  (7) **B paie chaque réponse par un appel** (120 tâches de test et de test final
  mêlées pour 160 appels et 20 USD par génération), A peut répondre par ses sondes (`predire`) : entre 80 et 100 % de
  couverture, les tâches que B n'a pas pu payer comptent comme des erreurs, une part de Δ **dans le sens prédit** qui
  mesure le budget autant que l'exactitude (CE4-02 (b)) ; les appels coupés (`TRONQUE`) ou vides (`VIDE`) — quand la réflexion d'une espèce Anthropic
  consomme le plafond de 4 096 jetons (R-398), par exemple — rendent un texte vide, payé : ils font des absences de B
  plus souvent que de A, qui peut répondre par ses sondes, donc une part de Δ du même côté (CL8-02) ; le rapport descriptif gelé (Plan, point 6) donne, par paire et
  par bras, la couverture, la cause des absences et un Δ secondaire sur les seules tâches répondues par les deux bras ;
  (8) **sous 80 % de couverture, la paire est coupée** : un organisme conçu avec le service qui ne répond plus sans lui
  (il reçoit `INDISPONIBLE` là où il attendait une sonde) coupe sa paire, ce qui peut rendre H-G1 non concluante pour une
  cause liée au traitement (CE4-02 (a)) — limite dite avant la course ; la répétition B (Plan, point 8) le montre
  d'avance ; (9) le contrat dit à l'organisme que sa génération 0 est celle que le bras témoin relance « à l'identique » :
  le même code, mais sans le service d'entraînement (CE4-02 (c)). L'ordre des lignées dans une ronde est le même dans les
  deux bras (base triée, même graine de ronde) ; les graines d'ordre des tâches sont les mêmes (indice de lignée pris
  sur les lignées de A_r). Les dossiers temporaires (/tmp, /var/tmp, /dev/shm) sont propres à chaque exécution, dans les
  deux bras (RV-04) : aucune voie commune entre bras, répliques ou lignées hors des vues.
- **Statistique** : Δ(ℓ, r) = score(A_r, ℓ, g) − score(B_r, ℓ, g), où g est la génération lue : 2 (= G − 1), ou la
  dernière génération valide commune aux deux bras si l'un s'arrête avant (`generations_valides` écarte les rondes de
  conception, les rondes importées et les générations invalidées, CE3-02 ; `reponses_finales` lit les réponses retenues
  par le juge, RV-01). H-G1 se lit sur la moyenne des Δ et sur la moyenne des Δ de chaque réplique.
- **Intervalle** : bootstrap à trois niveaux — répliques tirées avec remise, puis paires tirées avec remise dans chaque
  réplique tirée, puis tâches du test final tirées avec remise par strate (famille, vérité), les mêmes pour les deux bras
  d'une paire ; 2 000 tirages ; percentiles 2,5 et 97,5 ; graine `entropie_analyse` (Plan d'analyse, point 5). Code :
  `analyse_gradient.difference_h_g1`, `paires_h_g1`, composés par `lire_h_g1`. Avec deux répliques, le premier niveau est
  grossier (trois tirages possibles) : c'est la limite dite plus haut.

## Seuil

- Effet prédit : +0,10 (`analyse_gradient.EFFET_PREDIT`). « Confirmé » exige à la fois la borne basse de l'intervalle à
  95 % au-dessus de 0, Δ moyen ≥ +0,10 et Δ moyen ≥ +0,10 dans chaque réplique ; « réfuté » : borne haute sous +0,10.
- Une seule comparaison principale (H-G1) : aucune correction pour comparaisons multiples. H-G0 est une condition
  mécanique rapportée ; H-G2, H-G3 et H-C sont descriptives.
- Taux visés : « confirmé » à tort sous effet nul ≤ 5 %. Estimation par simulation, avant toute course (non opposable,
  R7 : modèle de variance supposé — effet de paire N(0 ; 0,5) en logit commun aux deux bras, bruit de bras N(0 ; 0,25),
  dérive de réplique du bras A N(0 ; σ), base 0,65, test final de 36 + 24 tâches —, `analyse_gradient.puissance_h_g1` au
  code cité, deux répliques de trois paires, 400 jeux par cas, 400 tirages, `SeedSequence(20261026)` ; sortie
  `puissance-v2.json` `50a1c248…`) :

| σ de réplique | effet nul : confirmé / réfuté | effet +0,10 : confirmé / réfuté | effet +0,20 : confirmé |
|---|---|---|---|
| 0 | 0,3 % / 35,0 % | 21,2 % / 0,5 % | 91,0 % |
| 0,25 | 1,3 % / 42,2 % | 18,5 % / 4,5 % | 69,3 % |
| 0,5 | 2,5 % / 38,3 % | 21,5 % / 9,2 % | 49,5 % |

  La règle v4 (trois niveaux, Δ ≥ +0,10 dans chaque réplique) a moins de puissance que celle de la v3 (44 % de
  « confirmé » à l'effet prédit, `puissance-v1.json` `eaf4ea5d…`, six paires indépendantes) : la puissance à l'effet prédit
  est faible (≈ 20 %) ; c'est dit avant la course et ne change aucun seuil. **Erreur dans l'autre sens** (R4, CE4-11) : à
  l'effet prédit +0,10, la lecture « réfuté » tombe à tort dans 0,5 %, 4,5 % et 9,2 % des jeux (σ = 0 ; 0,25 ; 0,5) : avec
  deux répliques, l'intervalle ne capte pas la dérive de réplique, dans un sens comme dans l'autre. La table est rejouée
  au code cité (les fonctions de différence, de simulation et de puissance n'ont pas changé ; `lecture_h_g1` n'a changé
  que sur les sorties de l'audit, absentes de la simulation) : rejouée par `puissance_v2.py` (`e05f48bc…`) au commit `44cd936`, la sortie est identique octet pour octet à `puissance-v2.json` (`50a1c248…`).
- **Règle des pannes** (CE4-01) : sous un taux d'échec extérieur **identique** dans les deux bras (p de 2 à 30 %, 10 à
  480 tentatives par bras), la règle gelée coupe une comparaison à tort dans au plus 0,71 % des cas (loi binomiale exacte,
  `coupure_sous_taux_identiques`) ; à effectifs **inégaux** (A répond par ses sondes, B par des appels), la coupure à tort
  monte à 0,76 % (60 contre 480 tentatives, p = 0,3 ; CL5-11), le critère « ≥ 3 échecs d'écart » comparant des comptes
  bruts d'effectifs inégaux. Avec quatre comparaisons par paire supposées indépendantes (cinq si la clé Brave est présente,
  CL5-08), la probabilité d'au moins deux paires coupées sur six reste sous 1,1 %
  (`coupures-sous-taux-identiques-v1.json` `7028c3f4…`) ; la règle de la v4 (écart > 10 points sans effectif minimal)
  donnait 14 % à 98 % (rejoué par la contre-lecture n° 4, E8). Une vraie panne
  propre à un bras (par exemple 8 échecs sur 10 contre 0, ou 10 sur 30 contre 0) coupe la paire ; 5 sur 10 contre 0 ne la
  coupe pas (Fisher p ≈ 0,03) : c'est le prix d'une règle qui ne coupe plus sur le bruit des petits comptes.

## Plan d'analyse

1. **Données.** Banque scellée `confrontation-v1` (`f1387a20…`) : entraînement 80 tâches (servies avec leurs vérités),
   test de développement 60 (score rendu à chaque génération), test final 60 (jamais rendu, lu une fois à la fin). Traits :
   `traits-16384` (aucune tâche tronquée ; la plus longue fait 12 407 jetons), dix vues (couches 8, 12, 16, 20, 24 ×
   dernier jeton, moyenne), 200 tâches × 4 096, Llama-3.1-8B-Instruct, révision `0e9e39f249a16976918f6564b8830bc894c89659`
   (le champ `revision_resolue` du manifeste vaut `None` sous transformers 5.18.0 ; les traits sont figés par leurs
   empreintes), servies toutes (`--traits <dossier traits-16384>`, sans `--vues`) ; le chargement vérifie empreintes,
   compagnons, banque de la course, tâches et nombres finis. **Vivier de conception** (point 10) : servi pendant les
   rondes de conception seulement, sans traits.
2. **Lignées.** Trois auto-écrites, amorcées par `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`, `GEMINI_ARGON` sous le contrat v3 du
   noyau au commit cité (vues ; champ `vivier` ; champ `question_ouverte` : le texte de la question à la ronde `c001` de
   la répétition seulement, `null` partout ailleurs, courses décisives comprises, R-410 ; § 3 « Réflexion comprise »,
   R-398 : ses chiffres viennent du pilote du 25 octobre — coupures à 512 et 640 jetons, R-391, R-400 ; le plafond de
   1 200 jetons n'y est pas cité — et du tour « structure » du collisionneur — appels de claude-fable-5-1 et de
   claude-opus-5-5 à 64 000 jetons rendus `OK`, avec des blocs de réflexion : `donnees/collisionneur-structure-v1`,
   `6f485f3`, `collisionneur-structure/run-structure-e3t1-v1/journal.jsonl` `43b54f06d48bdfe2042f596ba0d23455b144ea04d591576e962689f31fb962ba` — ; ce paragraphe ne dit rien
   de Gemini, dont la réflexion compte aussi dans les jetons de sortie : limite, CL8-07) ; elles seules entrent dans
   H-G1.
3. **Courses**, par le lanceur v6 (une course par appel ; options exactes ci-dessous, `<courses>` = dossier des courses) :
   - options communes : `--reel --go GO-2026-10-24-05 --registre-go <courses>/registre-go-<course>.md --taches
     <courses>/entrees/banque-confrontation-v1.json --traits <courses>/entrees/traits/etape1-v1/traits-16384 --sortie
     <courses>/<course> --isoler-reseau --parallele-max 8 --relances-max 1 --pas-max 5000 --delai-entrainement 60
     --octets-max 40000000 --max-tokens-appel 4096 --decalage-uid <100 pour A1, 200 pour A2, 300 pour B1, 400 pour B2,
     500 pour la répétition, 600 pour la répétition B>` (en réel, le noyau refuse un bras `--depuis` au décalage de son
     origine, RV-02) ;
   - A_r : `--generations 3 --graine <graine_r> --especes CLAUDE_FABLE_5_1 CLAUDE_OPUS_5_5 GEMINI_ARGON --appels-max 160
     --usd-par-generation 20 --temps-max 1800 --entrainements-max 10 --recherches-max 10 --telechargements-max 4
     --rondes-conception-max 4 --usd-max-conception 12 --appels-max-conception 160 --temps-max-conception 1800
     --pool-conception <courses>/entrees/vivier/<fichier du vivier> --plafond-total 360` (sans question, R-410) ;
   - B_r : `--depuis <courses>/A<r> --generations 3 --graine <graine_r> --appels-max 160 --usd-par-generation 20
     --temps-max 1800 --entrainements-max 0 --recherches-max 10 --telechargements-max 4 --plafond-total 190` (sans
     conception, vivier ni question ; mêmes organismes g000 et même mémoire de conception par l'import ; avec
     `--entrainements-max 0`, `traits.disponibles` est faux et `entrainer`, `predire` ne sont pas servis).
   A_1 et A_2 tournent ensemble (entrées extraites une fois, sous verrou, CE4-07 f) ; B_r part quand A_r est finie (verrou
   de A_r libre, au moins une génération 0 archivée). Une course décisive (A_r, B_r) ne part qu'après la répétition, la
   répétition B et l'épreuve de durée réussies sur le même hôte (portes scellées lues par le lanceur, point 8).
   Clés (GO-2026-10-24-04 et sa ligne d'extension du 25 octobre, R-411 ; R-394) : `ANTHROPIC_API_KEY` = valeur de la variable que nomme `CLE_ANTHROPIC` au lancement
   — `RR_ANTHROPIC_API_KEY`, `RR_ANTHROPIC_API_KEY_2`, `RR_ANTHROPIC_API_KEY_3` ou `RR_ANTHROPIC_API_KEY_LUC`, sans
   défaut — pour le seul processus du noyau, en-tête d'espace de travail par `ANTHROPIC_CUSTOM_HEADERS` pour
   `RR_ANTHROPIC_API_KEY` seulement (valeur de `RR_ANTHROPIC_WORKSPACE_ID`, jamais écrite), `ANTHROPIC_BASE_URL` absente (le noyau refuse le mode réel si elle est définie), `GEMINI_API_KEY` = valeur de
   `GEMINI_API_KEY_2` si elle existe, sinon de `GEMINI_API_KEY` (clé n° 2 : Lazar, R-370, 22:37 ; nom repris par la ligne
   de GO-2026-10-24-07 ; seul le nom est consigné) ; `BRAVE_API_KEY` si elle est dans l'environnement (source `web` de la
   moisson, lue par le noyau seul ; R-363) ; `OPENALEX_API_KEY` si elle est dans l'environnement (source `openalex`, passée
   par le noyau seul en paramètre de la requête, masquée dans tout message d'échec ; R-415) et `SEMANTIC_SCHOLAR_API_KEY`
   si elle y est (source `semanticscholar`, en-tête `x-api-key` posé par le noyau seul ; R-417), chacune à la même
   présence dans les deux bras (parité tenue par le lanceur et par le noyau) — le nom de Brave est défini dans la session « session-depot » au scellement (voir « État au scellement » plus bas) : la source
   `web` n'est servie que si la clé est présente au lancement, et à la même présence dans les deux bras (parité tenue par
   le lanceur) ; si Brave est présente au lancement, la règle des pannes a cinq comparaisons par paire au lieu de quatre (Seuil). Les **noms** des clés (Anthropic, Gemini, présence de Brave, d'OpenAlex et de Semantic Scholar) sont écrits par le lanceur de
   A_r (`A<r>.cles.txt`) et exigés identiques pour B_r ; les présences de Brave, d'OpenAlex et de Semantic Scholar le sont aussi au manifeste de A_r (CE4-07 d, e ; R-415,
   R-417).
   Les valeurs des clés ne passent par aucune ligne de commande (environnement du noyau construit par des commandes
   internes du lanceur, CE4-13). **État au scellement** (CE4-09, CL5-08, R-394, R-416) : au 25 octobre vers 11:10 UTC, dans la
   session « session-depot », après le redémarrage de son processus (avant 11:01 UTC), les noms `RR_ANTHROPIC_API_KEY`,
   `RR_ANTHROPIC_API_KEY_2`, `RR_ANTHROPIC_API_KEY_3` (75 USD selon Lazar), `RR_ANTHROPIC_API_KEY_LUC` (165 USD selon
   Lazar), `RR_ANTHROPIC_WORKSPACE_ID`, `GEMINI_API_KEY`, `GEMINI_API_KEY_2` et `BRAVE_API_KEY` sont définis (noms
   seulement, aucune valeur lue) ; `OPENALEX_API_KEY` et `SEMANTIC_SCHOLAR_API_KEY`, versées par Lazar après 11:01 UTC, ne
   le sont pas encore (elles ne sont vues qu'après un redémarrage ou dans une session nouvelle) : absentes au lancement,
   les sources `openalex` et `semanticscholar` sont servies sans clé, dans les deux bras. La répétition et les courses partent de cette session (Lazar, R-416). La clé Anthropic n° 1 a épuisé son crédit au pilote du 25 octobre (HTTP 400
   « credit balance is too low », R-391) ; la n° 2 (réserve, R-351) répondait à 08:03 UTC. La clé Gemini n° 1 n'avait plus de crédit au collisionneur (HTTP 402, R-379) ; si
   elle n'a pas été rechargée, le test de dépense d'Argon le dira et aucune course ne partira (sûr). Le crédit réel de
   l'une et de l'autre clé n'est pas vérifiable sans un appel : le test de dépense par espèce est ce qui le tranche avant
   toute course. **Crédit et recharge** (R-394, R-404) : 75 + 165 = 240 USD selon Lazar sur les clés n° 3 et LUC, et
   la **recharge automatique est active sur toutes les clés d'interface, Anthropic et Gemini** (Lazar, 25 octobre, vers
   09:13 UTC, mot direct ; non vérifiable ici) : le crédit ne borne donc plus la dépense ; **seuls les plafonds du noyau
   la bornent** — par course (A_r 360, B_r 190, répétition 40, répétition B 10 USD), par génération (20 USD ; 5 et 3 aux
   répétitions) et par ronde (12 USD ; 2 à la répétition), réservés au pire cas avant chaque appel
   (`test_appels_paralleles_plafond_tenu_au_pire_cas`, `test_ce312_doit_arreter_et_raison_juste`) : au plus 1 150 USD
   pour l'étape, plus moins de 1 USD de tests de dépense par course — borne par exécution : elle repose sur la règle
   « aucune relance » et sur l'engagement consigné avant chaque course ; aucune console ne plafonne la recharge
   (Lazar, R-412 ; CL8-06). Si un crédit s'épuisait malgré tout en cours de
   course, elle s'arrêterait (R-395) : consignée, lue à la dernière génération valide commune, ou ses paires coupées,
   sans relance. Le nom de la clé Anthropic de chaque course est choisi au lancement, consigné (`<course>.cles.txt`) ;
   B_r prend celui de A_r. Avant chaque course, un **test de dépense** par espèce (décision de Lazar, 25 octobre, 09:58 heure de Paris, relayée
   par « conv-audit », n° 36, avec la recharge automatique : un appel payant, consigne figée « Réponds par le seul mot :
   prêt. », 512 jetons au plus ; statut `OK` et jetons de sortie > 0 exigés — un crédit épuisé, même sous HTTP 200, rend
   `ECHEC_API`, R-395 —, sinon la course ne part pas), imputé, comme les répétitions et les courses, à GO-2026-10-24-05
   (R-403 ; GO-07, qui le nommait, échoit le 26 octobre). Environnement Python des courses : `/opt/essaim-m3-venv-v1`
   (Python 3.13.17, numpy 2.4.6, anthropic 2.3.0 ; liste des paquets au point « Lanceur ») ; noyau en root (isolation d'utilisateur), réseau des organismes et de
   l'entraîneur coupé.
   **Hôte** (RE-02) : Lazar a retenu l'option (a) le 25 octobre (mot direct, R-405) : le conteneur de la session
   « session-depot » (machine virtuelle, root, isolation complète) où les clés n° 3 et LUC sont visibles, celui de cette
   session (R-416) : la répétition, l'épreuve de durée, le second pilote et les quatre courses y tournent ; c'est aussi
   l'hôte le moins cher, en dollars comme en quota de la session. **Cohabitation** (CL8-04) : le second pilote
   (`GO-2026-10-25-01`) est fini avant le départ de A_1 et A_2 (constat consigné dans `registres/decisions.md`) et prend
   des décalages d'utilisateurs hors de 100 à 600 (700 et 800) ; aucune autre course ne tourne pendant A_r et B_r.
   **Copie** : après chaque course, une copie scellée de sa sortie (sans la banque ni les entrées) est poussée sur une
   branche de données privée (`donnees/etape1-courses-v1`), sans être ouverte ; la perte du conteneur entre A_r et B_r
   rendrait pourtant B_r impossible (son origine vivante y reste) : limite dite ; la sonde
   du 24 octobre (instance Vast.ai 57576327, détruite) montre qu'un conteneur Vast.ai ordinaire interdit `unshare`, donc
   l'isolation exigée par le noyau. L'hôte effectif est consigné dans `registres/decisions.md` avant la répétition ; le
   même lanceur et le même noyau y tournent ; le lanceur refuse un hôte sans root, sans `unshare -n`, sans espaces de noms
   de montage, de processus et de communication, sans dossier en mémoire montable dans un espace de montage privé, ou sans
   `fs.protected_hardlinks` = 1, et un hôte dont l'empreinte (identifiant de machine, nom, noyau, cœurs) diffère de celle
   des courses déjà lancées dans le dossier (CE4-08) ; le noyau refuse le réel sans espaces de noms (RV-06). **Épreuve de
   durée** (CE4-08) : avant les courses décisives, sur l'hôte retenu, un processus détaché, sans clé ni appel, bat toutes les
   60 s pendant 8 100 s (`lancer_courses_etape1_v6.sh epreuve`, PID consigné) ; la porte exige une durée ≥ 7 200 s, des
   battements sans trou de plus de 180 s, le même hôte (`epreuve-duree.json`, scellé) ; l'épreuve est lancée quand la
   session est laissée inactive. L'épreuve (2 h 15) ne couvre ni la durée d'une course A (jusqu'à 10,5 h, voire ≈ 15,75 h
   avec l'attente de 900 s des appels en vol) ni un redémarrage du conteneur (dont l'empreinte de l'hôte ne change pas,
   CL5-09) : elle vérifie seulement qu'un processus détaché survit à l'inactivité de la session sur l'hôte retenu, limite
   dite. Les courses décisives sont lancées **détachées** (le lanceur consigne leur PID), comme l'épreuve. **Arrêt de
   l'hôte** (conteneur repris, machine arrêtée, par exemple celui observé le 25 octobre à 01:29 UTC, R-383) : la course
   est arrêtée, consignée, lue à la dernière génération valide commune, ou ses paires sont coupées ; aucune relance.
4. **Budgets « économes »** (message n° 22 § 3 de « conv-audit », message n° 20 § 2 de « session-depot »). Génération
   notée : 160 appels, 20 USD (le noyau refuse au-delà : `PLAFOND`), 1 800 s, au plus 4 096 jetons de sortie par appel
   (`--max-tokens-appel`, rabattu par le noyau ; l'amorçage garde le maximum du modèle), 10 entraînements de ≤ 5 000 pas et
   ≤ 60 s, 10 recherches, 4 téléchargements, 40 Mo. Ronde de conception : 160 appels, 12 USD, 1 800 s, même moisson et mêmes
   entraînements. Au plus 4 rondes. Garde de temps du noyau en réel (CE-07 étendue par CE3-11, `boucle.temps_pire_cas`) :
   10 × 60 + 10 × 25 + 4 × (25 + 120) + 300 = 1 730 s ≤ 1 800 s (B : 1 130 s ; répétition : 615 s ≤ 900 s ; répétition B :
   495 s). Plafonds par
   course : A_r 360 USD (l'amorçage réserve le plafond d'une génération, 20 USD par lignée, mais son pire cas réel est
   ≈ 6,6 USD — Fable 3,40, Opus 1,36, Argon 1,80 au maximum du modèle, prompt de 60 000 caractères, CL5-03 ; 3 lignées ×
   4 rondes × 12 = 144 ; 3 lignées × 3 générations × 20 = 180 ; marge) ; B_r 190 USD (3 × 3 × 20 = 180, plus 10) ;
   répétition 40 USD (son plafond par génération est **5 USD** et non 3, pour que l'amorçage de Fable — pire cas 3,40 —
   passe, CL5-03 ; amorçage ≈ 6,6 au pire, 3 × 2 rondes × 2, 3 × 1 × 5) ; répétition B 10 USD (3 × 3, plus 1). Les plafonds ne mordent pas par construction (pire cas réservé, non
   attendu). Requêtes de recherche au plus : A_r (4 + 3) × 3 × 10 = 210, B_r 90, soit 600 pour l'étape, 18 pour la
   répétition et 6 pour la répétition B (toutes sources confondues ; CE3-15). Durées (lignées l'une après l'autre dans
   chaque ronde) : au pire
   A_r ≈ (4 + 3) × 3 × 1 800 s = 10,5 h (≈ 15,75 h au pire avec l'attente de 900 s des appels en vol à chaque génération),
  B_r ≈ 4,5 h ; attendues bien moindres (illustratif). Les délais de la garde de temps du noyau sont **par opération**
  (chaque recherche ≤ 25 s, chaque téléchargement ≤ 145 s), non une borne stricte sur le total réseau d'une génération
  (RV-15) : c'est `temps_pire_cas` qui majore le total. La question de `c001` de la répétition n'a pas de budget propre : l'organisme y
  répond, s'il le veut, avec les appels et le temps de sa ronde (contrat, § 7). Le plafond de 4 096 jetons de sortie par
  appel comprend, pour les espèces Anthropic, la réflexion du modèle (contrat, § 3, R-398) : au pilote du 25 octobre,
  aucun des 39 appels servis par claude-fable-5-1 n'a rendu `OK` (27 coupés, aux plafonds de 640, 512 et 1 200 jetons
  demandés par l'organisme ; 5 vides ; 7 refus ; R-391, R-400) ; à 4 096, la part coupée n'est pas mesurée ici (limite dite) ;
  la porte de la répétition la rapporte par espèce (point 8).
5. **Graines (R9).** Entropie E tirée au scellement (`secrets.randbits(128)`) et inscrite dans la section « Contre-lecture »,
   entrée 9, au format littéral, hors bloc de code : `graine_1 = <entier>`, `graine_2 = <entier>`, `entropie_analyse =
   <entier>` (CE3-16) : `SeedSequence(E).spawn(3)`, chaque entier = `generate_state(1, uint64)[0]` de l'enfant ;
   `graine_r` est passée à `--graine` (le noyau en dérive les graines d'ordre par lignée, génération, phase et usage :
   la ronde k ne tire plus les graines de la génération k, CE3-17) ; `entropie_analyse` sert au bootstrap. La graine de la
   descente de gradient d'une sonde est un choix de l'organisme, journalisé par l'empreinte de sa spécification
   (`sha256_spec`) ; elle n'est pas une graine expérimentale (CE-15). Répétition : graine 1 (exclue de toute analyse).
6. **Lecture de H-G1** (une fois, après la fin des quatre courses ou leur arrêt), **en un seul appel gelé** (RV-10) :
   `lire_h_g1([(A_1, B_1), (A_2, B_2)], ["claude-fable-5-1", "claude-opus-5-5", "gemini-argon"], generations=3,
   entropie=entropie_analyse, temoins=<scores des sondes témoins du point 7>, apres_audit=None)`. Il compose
   `paires_h_g1` (paires coupées : défaut trouvé par l'audit, aucune génération valide commune, couverture < 80 %,
   panne extérieure ; `invalide` si plus d'une paire sur quatre est coupée, soit deux paires ou plus sur six),
   `difference_h_g1` (2 000 tirages), `declencheurs_audit_h_g1` (scores sur les tâches répondues de chaque lignée lue, par
   famille, dans chaque bras et chaque réplique, à la génération lue ; sondes témoins ; Δ par paire ; recoupements de fuite
   de **toutes** les paires prévues, lues ou coupées, générations notées et rondes de conception comprises) et
   `lecture_h_g1`. Après un audit qui trouve un défaut touchant des paires, le même appel est refait avec
   `apres_audit="defaut_paires"` et `exclues=[<paires touchées>]` (la règle d'un quart est alors recalculée ; sans
   `exclues`, la lecture refuse) ; après un audit sans défaut, avec `apres_audit="sans_defaut"`. Un sous-agent neuf rejoue
   ces appels (R13). **Rapport descriptif gelé** (CE4-02 (2), CE4-10 e), rendu par le même appel (`rapport`), sans seuil
   ni verdict, quel qu'en soit le sens (R4) : par paire et par bras, génération lue, couverture par famille, exactitude par
   famille (règle du juge) et sur les tâches répondues, **pour les deux familles**, Δ par famille, Δ secondaire sur les
   seules tâches répondues par les deux bras, causes des absences (statut d'exécution, refus du noyau par raison
   — `appels_max`, `plafond_usd` —, demandes d'un service non servi — `INDISPONIBLE`, par opération —, problème de
   lecture des réponses), pannes (ce qui a été comparé ou non, et pourquoi), recoupements de fuite et recoupements courts.
   À côté de ce rapport, pour chaque course décisive, par paire et par bras : statuts des appels des organismes par
   espèce et appels qui ont réfléchi, tirés de l'extrait mécanique scellé de la course (`appels`, `reflexion_par_statut`),
   sans seuil (CL8-02). La lecture de H-G1 ne changera pas : un plancher de bruit ou des témoins de sortie du modèle de
   8 milliards, s'ils viennent (« conv-audit », n° 35 § 3), seront descriptifs, ajoutés par un addendum scellé et contre-lu
   avant toute lecture (Lazar, R-413 ; CL8-08).
   Rapport scellé ; verdict par un sous-agent neuf (R13) si l'étape sert de porte à l'étape 2.
7. **H-G2 (descriptive).** Après les courses, pour chaque vue : deux sondes témoins entraînées par l'entraîneur du noyau
   (isolé), sur les 80 tâches d'entraînement, sonde linéaire normalisée, 1 000 pas, taux 2, l2 0,001, lot 80, graine 0,
   objectif de Brier et objectif logarithmique borné (p tronqué à [0,001 ; 0,999]) ; exactitude équilibrée sur le test
   final, rapportée. Référence de surface : `banque.reference_traits_texte` (0,69 et 0,50 rapportés par « conv-audit », non
   audités). Le script de ces témoins est écrit et scellé (addendum, avec son empreinte) avant d'être lancé, et avant la
   lecture de H-G1, dont il nourrit les déclencheurs (CE-17, CE2-07).
8. **Répétition mécanique** avant les courses décisives, après le scellement (`lancer_courses_etape1_v6.sh repetition`) :
   lignées `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5` et `GEMINI_ARGON` (CE4-04 (3)), deux rondes de conception à 2 USD et
   20 appels, une génération à **5 USD** (et non 3 : pour que l'amorçage de Fable, pire cas 3,40 USD, passe sous le plafond
   d'une génération, CL5-03) et 20 appels, 900 s, deux entraînements de 60 s, 2 recherches, 1 téléchargement,
   vivier servi, question à `c001`, plafond 40 USD ; puis la **répétition B** (`repetition-B` : `--depuis repetition --entrainements-max 0`,
   une génération, plafond 10 USD ; CE4-04 (4)), qui exerce le chemin réel du bras B (import sous root, parité des clés,
   `entrainer` → `INDISPONIBLE`) et dit d'avance si un organisme conçu avec le service répond sans lui ; test de dépense
   des trois espèces avant chacune ; toutes deux exclues de toute analyse. La sortie du noyau (qui contient courbes et
   scores) est écrite en 0600, scellée, jamais ouverte avant la lecture ; seuls ses statuts sont lus, par l'extrait
   mécanique sans score v2 (`python -m essaim_m3.outils.extrait_mecanique`, listes closes et garde finale sur les noms de
   clés ; comptes par statut des entraînements, des recherches par source et des téléchargements ; rondes importées
   marquées, CE4-04 (1), CE4-06). **Porte mécanique gelée** (CE4-04 (2)), calculée par le lanceur sur l'extrait et
   scellée (`<course>.porte.json`) : la répétition est réussie si le noyau finit (code 0), si chaque espèce a un amorçage
   `ORGANISME_VALIDE` et une génération 0 valide archivée, et si les entraînements, les recherches et les téléchargements
   demandés rendent chacun au moins un `OK` (rien demandé : pas de condition ; un entraînement, une recherche ou un
   téléchargement en échec **par la faute de l'organisme** — spécification refusée, provenance interdite — ne fait pas
   échouer la porte : on ne compte que les statuts du noyau et du fournisseur, CL5-10), et si la question a été posée à
   la ronde `c001` de chaque lignée et à aucune autre ronde ni génération (R-393 ; la réponse, écrite ou non, est
   rapportée sans condition) ; la répétition B, si le noyau
   finit, si chaque lignée est relancée (`ORGANISME_IMPOSE_VALIDE`) avec une génération 0 valide, et si les recherches et
   téléchargements demandés rendent au moins un `OK` ; le nombre de réponses de B (`n_reponses_test`) et ses demandes
   `INDISPONIBLE` y sont rapportés, sans condition. Les deux portes rapportent aussi, sans condition, les appels des
   organismes par espèce et par statut (`OK`, `TRONQUE`, `VIDE`, `REFUS`…), ceux qui ont réfléchi, par statut (types de
   blocs gardés au journal, R-402), et les plafonds `max_tokens` servis — après le rabattement à 4 096 : un 4 096 peut venir d'une demande
   plus haute — (un
   appel coupé peut venir du plafond que l'organisme a choisi : CL5-10) ; **vérification humaine** avant les courses
   décisives : les taux d'appels coupés (`TRONQUE`) et vides (`VIDE`) de chaque espèce, Argon compris, sont soumis à
   Lazar quels qu'ils soient (changer `--max-tokens-appel` est un changement de budget : addendum scellé et contre-lu) ;
   pour Argon, l'appelant ne demande pas les parts de réflexion : son compte d'appels qui ont réfléchi peut rester à 0
   par construction (CL8-02). Sans ces deux portes et celle de l'épreuve de durée (point 3), passées
   sur le même hôte, le lanceur refuse les courses décisives. Une porte non passée sans défaut de code (par exemple un
   amorçage invalide de l'organisme) revient à Lazar (changement de modèle) puis addendum, comme un refus d'amorçage. Si la répétition révèle un défaut de code, la correction
   passe par un addendum scellé et contre-lu avant les courses. Si une espèce y **refuse l'amorçage** (statut `REFUS`,
   aucune reformulation) ou ne peut pas être appelée (crédit, clé), les courses décisives ne partent pas :
   remplacer ou retirer une espèce est un changement de modèle et une modification de l'expérience, décidés par Lazar,
   puis un addendum scellé et contre-lu. (Le 24 octobre à 23:40 UTC, au collisionneur, Opus a refusé une question
   abstraite sur la réécriture d'un organisme — refus classé « cyber » — et Argon a répondu HTTP 402, crédit épuisé :
   `donnees/collisionneur-reecriture-v1`, `2cda505` ; au pilote du 25 octobre, entre 07:49 et 07:56 UTC, le crédit de la clé
   Anthropic n° 1 s'est épuisé dans la génération 0, en HTTP 400 : R-391, R-395.)
9. **Phase de conception et moisson.** Les sections A et B de `prereg/sections-conception-moisson-v1.md` (`180a39af…`)
   valent pour le noyau, la provenance et le scellement ; **les points 3, 4, 9 et 10 du présent plan priment** sur elles
   (CE3-14) : le bras B est `--depuis` sans `--gel` et importe la mémoire de conception (et non « relancé à l'identique par
   le bras gelé ») ; une ronde a 12 USD (et non le budget d'une génération) ; une consigne glissée dans une page moissonnée
   peut faire plus que « tromper l'organisme » (le pousser à lire hors de sa lignée ou à toucher aux dossiers du noyau) :
   ce que le noyau en tient est l'isolation (vue de la seule lignée, dossiers du noyau hors du dossier de l'organisme,
   aucun lien suivi par root), pas la mesure par source. Valent des sections : rondes `cNNN` archivées, scellées, vues
   de la seule lignée, jamais notées ; à la ronde 4, le successeur devient la génération 0, fin déclarée ou non ; sources
   `arxiv`, `openalex`, `semanticscholar` et `web` si la clé existe ; téléchargements sous provenance, documents ≤ 8 Mo,
   texte rendu ≤ 60 000 caractères, corpus et index scellés par génération ou ronde dans un dossier du noyau
   (`<travail>.corpus`, CE3-07), visibles de la lignée seule ; texte moissonné rendu comme donnée ; rien de moissonné
   n'entre dans la banque. Après une référence permise, l'adresse finale d'une redirection est suivie en https et
   consignée ; son hôte n'est pas restreint (un identifiant numérique d'objet renvoie chez l'éditeur) (CE3-18). Débit :
   OpenAlex répondait 429 depuis l'adresse partagée le 24 octobre (rapporté par « conv-audit », message n° 14 ; sans pièce
   mesurée ici) ; un `ECHEC_RECHERCHE` est un statut rendu à l'organisme et compté dans les pannes (point 6).
10. **Vivier de conception.** `--pool-conception` (A_r et répétition) : fichier aux trois valeurs littérales de « Documents
   qui font foi », compagnon `.sha256` exigé ; servi pendant les rondes de conception seulement, à la suite des tâches
   d'entraînement de la banque, dans un ordre tiré par la graine de la ronde, avec sa vérité, sous des identifiants
   opaques (`cv-0001`…) : l'identifiant de source et la catégorie ne sont jamais servis ; textes bornés comme ceux de la
   banque ; identifiants attribués après une permutation tirée de l'empreinte du fichier (`SeedSequence`), qui ne suivent
   pas l'ordre du fichier (CE4-03 (3)) ; garde de disjonction par le contenu, **dans les deux sens** (CE4-03 (1)) : pour
   chaque texte de la banque, la part de ses fenêtres retrouvées dans l'item et la part des fenêtres de l'item retrouvées
   dans ce texte, fenêtres de 8 mots **de toute écriture** et de 16 caractères pour les écritures sans espaces (chinois,
   japonais, coréen, thaï…), un texte normalisé identique comptant pour 1 ; un item à 0,80 ou plus, dans un sens ou
   l'autre, d'un texte de la banque est écarté et compté (test ou test final ; entraînement) ; un item à 0,50 ou plus d'un
   texte de test est servi et compté « proche » ; doublons internes (même texte normalisé, écritures sans espaces
   comprises) comptés ; un item malformé fait refuser le fichier (`noyau/vivier.py`, essais
   `test_vivier_de_conception_servi_en_conception_seulement`, `test_vivier_gardes_compagnon_format_et_recoupement`,
   `test_ce403_garde_unicode_deux_sens_et_identifiants_tires`). `contexte["vivier"]` = {`n`, `familles`, `ids`} pendant la
   conception, absent sinon ; aucune génération notée ne le reçoit **dans son contexte**, mais les contextes des rondes,
   vivier et vérités compris, restent lisibles dans la vue des générations notées, dans les deux bras (B par l'import ;
   CE4-03 (2)) : une quasi-copie d'un item de test que la garde laisserait passer serait exploitable au test, dans les deux
   bras (pas de biais de Δ ; une famille qui peut saturer, et l'audit le cherche). Le vivier n'a pas de traits : il sert la
   conception par le texte, pas l'entraînement des sondes (le noyau refuse d'entraîner sur un identifiant hors de
   l'entraînement de la banque). Il n'entre dans aucune hypothèse ; ses comptes (servis, écartés, proches, doublons) sont
   rapportés, et ceux du vrai fichier sont transmis avant le scellement (« Documents qui font foi »). **Comptes du vrai
   fichier** (« conv-audit », message n° 35 § 1, au code `90595ffb`, `noyau/vivier.py` identique au commit cité) :
   786 items ; 755 servis ; 20 écartés « recoupe le test » (dont un texte identique à celui d'un item de test, sous un
   autre identifiant de source) ; 7 écartés « doublon de l'entraînement » ; 4 doublons internes ; **249 servis
   « proches »** (≥ 0,50 d'un texte de test, dans un sens ou l'autre) ; recoupement maximal servi 0,7968 ; 194 tronqués
   (plus de 20 000 caractères).
   **Réserve** (R-399) : un tiers des items servis (249 sur 755) recoupe un texte de test à 0,50 ou plus, dans un sens ou
   l'autre (fenêtres de 8 mots ; gabarits d'agents et d'environnements communs au jeu source) ; un organisme peut y apprendre « ce gabarit →
   cette étiquette », un indice de surface, non une fuite d'item. Le seuil d'exclusion reste 0,80, fixé avant d'avoir vu
   les comptes (l'abaisser au vu des comptes serait le régler sur les données) ; pour H-G1, c'est symétrique (B importe
   la même mémoire de conception) ; pour les niveaux absolus des scores, c'est une limite dite, que portent les
   déclencheurs de l'audit (une lignée au-dessus de 0,95) et le rapport descriptif.
11. **Garde et mesure de fuite (CE3-04, décision (c) de Lazar ; RV-07, RV-12, CE4-03).** Fenêtres des tâches de test et
   de test final, **moins celles qu'un texte d'entraînement contient aussi** (un gabarit commun avec l'entraînement, que
   l'organisme a déjà, n'est pas une fuite : RV-12), mots de toute écriture et caractères des écritures sans espaces. Une
   requête qui recopie 8 mots consécutifs d'une tâche de test ou de test final est refusée (`REFUSE_FUITE`, sans consommer
   de recherche) ; une **notice rendue** par la recherche (titre, auteurs, résumé) qui en recopie est retirée des résultats
   et comptée (RV-07 (i)) ; un document téléchargé qui en contient est mis en quarantaine (rien n'est rendu ni écrit). Les
   empreintes recoupées ne sont écrites que dans les journaux du noyau, hors de la vue de la lignée ; l'index du corpus,
   lisible par la lignée, ne porte que le statut (RV-07 (iii)) — le statut `REFUSE_FUITE` lui-même dit à l'organisme que
   sa requête ou ce document recoupe une tâche de test, sans rien en rendre : limite dite. Les **recoupements courts**
   (fenêtres de 5 mots) sont comptés au journal du noyau, jamais refusés, et rapportés (descriptifs : des fenêtres de cinq
   mots se partagent par simple tournure commune, ils ne déclenchent pas l'audit ; RV-07 (ii)). Les refus et retraits sont
   comptés par lignée, bras et génération, **rondes de conception comprises** (CE4-10 c) ; tout recoupement refusé ou
   retiré déclenche l'audit (point 6). Une paraphrase passe : la garde ne prétend pas tout fermer. Câblage éprouvé de bout
   en bout (`test_rv12_garde_de_fuite_cablee_de_bout_en_bout` : sans lui, l'essai échoue).
12. **Consignation.** Avant chaque course, une ligne « engagement : course <course> de l'étape 1 » dans
   `registres/depenses.md` (le lanceur l'exige, CE3-15) ; après chaque course, la dépense : `depense_totale_usd` du rapport
   du noyau (qui compte l'amorçage ; les totaux hors rondes importées de l'extrait mécanique le minorent, l'amorçage
   n'y figurant pas, CL5-11 ; jamais la somme des journaux d'un bras B, qui compterait deux fois la conception de A :
   CE4-06), plus les tests de dépense ; la ligne de dépense porte le nom de la clé Anthropic de la
   course (`<course>.cles.txt`) et le compte débité, celui du programme (R-411) ; arrêt de l'hôte, s'il y en a un, dans
   `registres/arrets.md`. L'extrait mécanique est « sans clé de score » : les valeurs que l'organisme écrit lui-même
   (noms de fichiers, `erreurs` de son journal, déclaration de fin de conception) ne sont pas filtrées par leur contenu et
   peuvent porter un score de développement qu'il a reçu ; elles sont bornées en nombre et en longueur (CE4-06).
13. **Isolation tenue par le noyau** (RV-02 à RV-06, RV-08, CL5-01, CL5-02). Chaque exécution d'un organisme (et de
   l'entraîneur, et d'une métrique) se fait dans un espace de montage neuf où, avant l'abaissement des privilèges :
   (a) **tout** dossier inscriptible par les autres (les quatre habituels — /tmp, /var/tmp, /dev/shm, /run/lock — et tout
   autre trouvé par un balayage des systèmes de fichiers, par exemple `/var/lib/php/sessions`, CL5-02) est recouvert d'un
   dossier en mémoire privé (un échec arrête tout) : aucune voie commune entre bras, répliques ou lignées hors des vues ;
   (b) le dépôt, ses objets git, l'arbre du code (ils portent la banque et ses vérités, lisibles par tous sur l'hôte) et
   /home, /root, /srv, /mnt, /media sont recouverts d'un dossier en mémoire **vide et en lecture seule** : l'organisme n'y
   lit rien (CL5-01 ; le lanceur passe le dépôt et le code au noyau par `ESSAIM_M3_CACHER`). Elle a aussi son propre
   espace de communication entre processus ; les sockets du noyau vivent hors de /tmp, sous des noms imprévisibles ;
   l'espace des organismes est sous `/var/lib/essaim-m3` ; les dossiers vivants sont rendus à root après chaque dépôt ;
   la vue importée de B est fermée aux autres lignées dès l'import ; le statut d'exécution est lu sans suivre de lien ni
   attendre sur un tube, et les erreurs par le descripteur que le noyau a ouvert ; à la fin d'une génération, les appels
   encore en vol sont attendus (au plus 900 s) avant de lire le journal et la dépense, et un appel encore en vol au-delà
   est compté (`appels_en_vol_non_finis`), jamais passé sous silence ; en réel, le noyau exige les espaces de noms.
   Essais : `test_rv01_…` à `test_rv08_…`, `test_rv12_…`, `test_cl5_01_banque_cachee_a_l_organisme`,
   `test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous` (sain et artefact chacun).
14. **Question ouverte « structure »** (R-393, R-410). Pièce : la question « apprendre sa structure, sa composition et
   son entraînement, de génération en génération », texte pour les organismes versé par « conv-audit », sans aucune de
   nos pistes ni réponse du collisionneur (« Documents qui font foi », empreinte au format littéral). Posée par le noyau
   (`--question-ouverte … --question-ouverte-aux c001`, contrat § 7) à la **première ronde de conception de la
   répétition** seulement, pour chaque lignée ; la répétition B en hérite par l'import (contexte de `c001`, réponse
   recopiée dans sa vue, R-396). **Aucune course décisive ne la reçoit** (décision de Lazar sur CL8-01, R-410) : posée au
   seul bras qui a le service d'entraînement, cette question, qui nomme les sondes et demande comment les concevoir,
   pouvait rendre la génération 0 plus dépendante du service, donc pousser Δ vers « confirmé » ou faire couper des
   paires, jamais vers « réfuté ». L'organisme y répond, en partie ou pas du tout, avec le budget de sa ronde ; aucun
   score, aucune sélection, aucun budget n'en dépend (contrat, § 7 ; ce paragraphe situe la copie dans la vue sous
   `gNNN/`, alors qu'à une ronde elle est sous `c001/` : à corriger dans une version suivante du noyau, CL8-11). Le
   lanceur extrait la pièce avec les entrées et vérifie son empreinte ; la porte de la répétition exige qu'elle ait été
   posée à `c001` et nulle part ailleurs. Les réponses (`repetition/archive/<lignée>/c001/reponse-question.md`, scellées)
   ne portent aucun score (`c001` précède toute génération notée) ; elles sont lues par les humains après la
   répétition, n'entrent dans aucune hypothèse, et ce qu'on en tirerait pour les courses décisives passe par un addendum
   scellé et contre-lu. Le second pilote pose la même question à sa génération 1, sous son propre préenregistrement.

## Critères de lecture gelés

Table de H-G1 (`analyse_gradient.lecture_h_g1`), lue de haut en bas ; la première ligne vraie s'applique.

| condition | verdict |
|---|---|
| audit de symétrie déclenché et rapport d'audit non scellé (`apres_audit` = `None`) | « audit de symétrie (R4) avant toute lecture » ; la lecture attend le rapport |
| rapport d'audit : défaut du noyau (`defaut_noyau`) | « non concluant : défaut du noyau trouvé par l'audit de symétrie » |
| rapport d'audit : défaut touchant des paires (`defaut_paires`), paires touchées non encore coupées (`exclues` vide) | « audit de symétrie (R4) : défaut touchant des paires — couper les paires touchées (exclues) avant la lecture » ; la lecture attend l'appel avec `exclues` |
| plus d'une paire sur quatre coupée (aucune génération valide commune, couverture < 80 %, panne extérieure, ou paire invalidée par l'audit) | « non concluant : plus d'une paire sur quatre coupée ou invalidée » |
| aucune paire | « non concluant : aucune paire » |
| borne basse > 0, Δ moyen ≥ +0,10 et Δ moyen ≥ +0,10 dans chaque réplique | « confirmé » |
| borne haute < +0,10 | « réfuté (l'effet prédit est exclu) », avec « effet positif plus petit que prédit » si la borne basse > 0 |
| sinon | « non concluant ; aucune relance sans nouveau préenregistrement » |

- **Audit de symétrie (R4)**, déclenché par l'un de ces faits, qu'il aille dans le sens de la prédiction ou contre elle
  (`declencheurs_audit_h_g1`) : une lignée (l'un ou l'autre bras, l'une ou l'autre réplique) au-dessus de 0,95 ou
  au-dessous de 0,30 sur une famille du test final, **sur les tâches répondues** (une absence de réponse coupe la paire
  par la couverture, elle ne déclenche pas l'audit : CE3-03) ; une sonde témoin au-dessus de 0,95 ; |Δ| d'une paire
  au-dessus de 0,40 ; un recoupement de fuite refusé ou retiré (requête refusée, notice retirée, document en quarantaine),
  dans les générations notées ou les rondes de conception, pour toute paire prévue, lue ou coupée (CE4-10 c). Les
  recoupements courts sont rapportés, jamais déclencheurs. L'audit cherche une fuite (vérités lisibles, vue de l'archive,
  vivier, recherche de provenance), des étiquettes inversées, un indice de surface.
- **Sortie gelée de l'audit** (CE3-03 c) : le rapport d'audit est scellé ; il rend l'un de trois états. « Sans défaut » :
  la table est relue sans sa première ligne et le verdict porte la réserve « audit de symétrie sans défaut trouvé ».
  « Défaut touchant des paires » : ces paires sont coupées (`exclues` de `lire_h_g1`, elles comptent dans la règle d'un
  quart), puis la table est relue sans sa ligne d'audit, et le verdict porte la réserve « audit de symétrie, défaut
  touchant des paires, coupées : … » (CE4-10 a, b). « Défaut du noyau » (qui toucherait toutes les lignées) : « non
  concluant ». L'audit est fait par un sous-agent neuf, qui n'a écrit ni ce texte ni l'analyse.
- **H-G0** : vrai ou faux par lignée, rapporté ; ne change pas la table de H-G1.
- Aucune relance d'une course après lecture. Une course arrêtée par une garde ou par l'arrêt de l'hôte avant sa fin est
  rapportée telle quelle ; ses paires sont lues à la dernière génération valide commune, ou coupées.

## Liste d'arrêt

Chaque ligne dit si c'est une garde automatique (avec son essai sain et artefact, R5) ou une vérification humaine.

| condition | effet | garde ou vérification |
|---|---|---|
| hôte sans root, sans `unshare -n`, sans espaces de noms de montage, de processus et de communication, sans dossier en mémoire privé possible, `fs.protected_hardlinks` ≠ 1, ou autre hôte que celui des courses déjà lancées dans le dossier | la course ne part pas (code 2) ; un changement d'hôte entre A_r et B_r est un écart (paires de la réplique coupées) | garde du lanceur (§ 1) ; essais `unshare-refuse`, `hardlinks-zero`, `non-root`, `autre-hote` (CE4-07 a, CE4-08) ; garde du noyau en réel (CR-01, CR-02, RV-06) : `test_mode_reel_refuse_sans_isolation_reseau_et_sans_root` (cas sain construit, trois artefacts, motif de chaque refus vérifié : PG2-02), `test_rv06_mode_reel_exige_les_espaces_de_noms` ; sonde d'hôte |
| porte de la répétition, de la répétition B ou de l'épreuve de durée absente, altérée, non réussie ou d'un autre hôte ; question de la répétition non posée à `c001`, ou posée ailleurs | les courses décisives ne partent pas | garde du lanceur (CE4-04, CE4-08, R-393) ; essais `sain-portes`, `reel-porte-alteree`, `reel-porte-autre-hote`, `reel-porte-non-reussie`, `reel-epreuve-courte` ; porte extraite du lanceur sur des extraits factices : `porte-question-c001-saine`, `porte-question-aussi-a-g000`, `porte-question-non-posee`, `porte-repetition-B-sans-condition-de-question` |
| taux d'appels coupés ou vides de chaque espèce, Argon compris, à la répétition et à la répétition B | soumis à Lazar avant les courses décisives, quels qu'ils soient (changement de budget : addendum) | vérification humaine de la porte (`appels_par_espece`, `reflexion_par_espece`, `max_tokens_demandes`, rapportés sans condition) ; essai `porte-appels-par-espece-rapportes` ; journal : `test_r402_types_de_blocs_au_journal_et_reflexion_comptee_a_l_extrait` |
| préenregistrement non scellé, non conforme, ou qui ne cite pas le commit ; une valeur littérale lue y figurant plus d'une fois ; code à un autre commit, arbre modifié ou fichier non suivi | la course ne part pas | garde du lanceur ; essais `prereg-non-scelle`, `prereg-sans-commit`, `graine-en-double` (CE4-12), `code-autre-commit`, `code-fichier-non-suivi` (CE4-07 b) |
| dossier des courses qui n'est pas à root en 0700 | la course ne part pas | garde du lanceur (CE3-06) ; essai `dossier-traversable` |
| banque, traits ou vivier d'empreinte différente ; vivier ou son compagnon absent du commit cité ; fichier de traits altéré après extraction | la course ne part pas | garde du lanceur (CE3-08, CE4-07 c) ; essais `vivier-faux`, `vivier-absent-du-commit`, `traits-alteres` ; extraction sous verrou : `extraction-simultanee-1` à `-3` (CE4-07 f) ; garde du noyau sur les traits (`cli.charger_traits`) : `test_charger_traits_dossier_d_extraction_sain_et_artefacts` |
| ligne d'engagement absente de `registres/depenses.md` | la course ne part pas | garde du lanceur (CE3-15) ; essai `reel-sans-engagement` |
| GO de la course et des tests de dépense (GO-2026-10-24-05, R-403) absent, sans type « calcul », hors période, ou collisionneur d'empreinte inattendue | course refusée avant tout appel | garde de calcul rejouée par le lanceur (essai `go-refuse-GO-2026-10-24-05` ; cas sain `go-07-absent-sans-effet`) ; garde du noyau (CR-13) |
| clé absente ; `CLE_ANTHROPIC` absent ou hors des noms admis ; clé nommée absente ; en-tête d'espace de travail absent pour `RR_ANTHROPIC_API_KEY` | la course ne part pas | garde du lanceur (R-394) ; essais `cle-absente`, `cle-anthropic-non-admise`, `cle-anthropic-sans-nom`, `cle-anthropic-nommee-absente`, `espace-de-travail-absent` ; cas sain `sain-cle-luc` (sans en-tête) |
| empreinte de la question de `c001` absente du préenregistrement, en double, ou différente de celle de la pièce ; pièce absente | la course ne part pas | garde du lanceur (R-393) ; essais `question-absente-du-prereg`, `question-en-double`, `question-alteree`, `question-piece-absente` ; cas sain `sain-repetition` (options `--question-ouverte … --question-ouverte-aux c001`) ; A_r et B_r sans question (constats `A1 sans question`, `bras B sans question`) |
| réponse à la question de `c001` absente de la vue de la répétition B | impossible : recopiée par l'import (R-396) | garde du noyau : `test_r396_import_conception_recopie_la_reponse_a_la_question_dans_la_vue` |
| clé OpenAlex ou Semantic Scholar dans un message d'échec rendu à l'organisme ou journalisé ; présence d'une clé différente entre A_r et B_r | impossible : valeur masquée avant toute troncature ; bras B refusé (R-415, R-417) | garde du noyau : `test_r415_cle_openalex_lue_par_le_noyau_masquee_et_appariee`, `test_r417_cle_semantic_scholar_en_en_tete_masquee_et_appariee` (sains et artefacts) ; lanceur : `openalex-differente-fichier`, `openalex-differente-manifeste`, `semanticscholar-differente-fichier`, `semanticscholar-differente-manifeste` |
| sortie existante ; course déjà en cours ; bras B (ou répétition B) avant la fin de son origine ou sans génération 0 archivée ; noms des clés (Anthropic, Gemini, Brave, OpenAlex, Semantic Scholar) différents de ceux de l'origine, ou présence de Brave, d'OpenAlex ou de Semantic Scholar différente de celle de son manifeste ; bras B au décalage d'utilisateurs de son origine | la course ne part pas | gardes du lanceur (R12, verrou, CE3-05, CE4-07 d, e) ; essais `sortie-existante`, `verrou-tenu`, `B-pendant-A`, `B-avant-A`, `repetition-B-avant`, `B-sans-cles-de-A`, `anthropic-differente`, `gemini-differente`, `brave-differente-fichier`, `brave-differente-manifeste`, `openalex-differente-fichier`, `openalex-differente-manifeste`, `semanticscholar-differente-fichier`, `semanticscholar-differente-manifeste` ; gardes du noyau `cli.conditions_moisson_differentes` : `test_ce305_sources_moisson_au_manifeste_et_bras_apparie` ; décalage : `test_rv02_dossiers_vivants_rendus_a_root_et_decalage_distinct_en_reel` |
| graine absente du préenregistrement | la course ne part pas (code 2, avec une note) | garde du lanceur (CE3-09) ; essai `graine-absente` |
| test de dépense d'une espèce en échec avant une course (statut autre que `OK`, aucun jeton de sortie, crédit épuisé même sous HTTP 200, clé, en-tête d'espace de travail, réseau, modèle servi) | la course ne part pas | garde du lanceur (§ 11 ; décision de Lazar, 25 octobre, 09:58 heure de Paris ; R-403, R-404), même client que les courses ; répétition mécanique ; vérification humaine du journal (modèle servi) ; éprouvée par lecture et par le rejeu de la contre-lecture n° 8 sur une doublure sans réseau (statut `OK` → 0 ; jetons 0, crédit épuisé sous HTTP 200, `TRONQUE`, `VIDE`, modèle non conforme, HTTP 402 → 1) ; aucun essai dans la suite : son premier cas sain réel est le test de dépense de la répétition (limite dite, CL8-03) |
| recharge automatique active : le crédit ne borne plus la dépense (R-404) | seuls les plafonds du noyau la bornent (course, génération, ronde ; réservation au pire cas avant chaque appel) | gardes du noyau : `test_appels_paralleles_plafond_tenu_au_pire_cas`, `test_ce312_doit_arreter_et_raison_juste` ; plafonds gelés (Plan, points 3 et 4) |
| refus d'amorçage d'une espèce, ou espèce injoignable, à la répétition ; entraînements, recherches ou téléchargements demandés sans aucun `OK` | les courses décisives ne partent pas ; décision de Lazar (changement de modèle) puis addendum | porte de la répétition, calculée par le lanceur sur l'extrait mécanique (garde) ; vérification humaine de l'extrait |
| génération notée sans réponse retenue par le juge (organisme planté, délai dépassé, lien ou tube) | « sans réponse » : la paire est coupée par la couverture, jamais une erreur de lecture | garde de l'analyse (RV-01) : `test_rv01_lecture_h_g1_suit_le_juge_absence_de_reponse_et_marque_d_ordre` |
| appel encore en vol à la fin d'une génération | attendu (au plus 900 s) avant la lecture du journal et de la dépense ; au-delà, compté (`appels_en_vol_non_finis`) | garde du noyau (RV-08) : `test_rv08_appels_en_vol_attendus_avant_la_lecture_du_journal` |
| voie commune hors des vues : dossier temporaire partagé, **tout** dossier inscriptible par tous (CL5-02), vue importée lisible d'une autre lignée, dossier vivant relu par une génération suivante | impossible : tout dossier inscriptible par tous recouvert d'un dossier en mémoire privé à chaque exécution, droits | gardes du noyau (RV-02, RV-03, RV-04, CL5-02) : `test_rv04_tmp_prive_a_chaque_execution`, `test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous`, `test_rv03_vue_importee_fermee_aux_autres_lignees_des_l_import`, `test_rv02_dossiers_vivants_rendus_a_root_et_decalage_distinct_en_reel` |
| organisme qui lit le dépôt, ses objets git ou l'arbre du code (banque et vérités du test final, lisibles par tous sur l'hôte) | impossible : ces chemins et /home, /root… recouverts d'un dossier vide en lecture seule dans l'exécution isolée (CL5-01) | garde du noyau : `test_cl5_01_banque_cachee_a_l_organisme` (sain et artefact) |
| statut d'exécution remplacé par un lien, erreurs remplacées par un tube | statut refusé et consigné, jamais suivi ; aucune attente | garde du noyau (RV-05) : `test_rv05_statut_et_erreurs_lus_sans_lien_ni_tube` |
| indice de lignée des graines différent entre A_r et B_r | impossible : base prise sur les lignées de A_r | garde du noyau (CE4-05) : `test_ce405_graines_du_bras_apparie_sur_les_lignees_d_origine` |
| `ANTHROPIC_BASE_URL` définie en réel | course refusée | garde du noyau : `test_mode_reel_refuse_anthropic_base_url` |
| entraîneur sans isolation d'utilisateur en réel | aucun entraînement (`Arret`) | garde codée (CE-02) ; `test_entraineur_isole_ne_lit_pas_les_fichiers_du_noyau` |
| budget incohérent (temps < entraînements × délai + recherches × 25 s + téléchargements × 145 s + 300 s) | course refusée | garde du noyau (CE-07, CE3-11) : `test_budget_incoherent_refuse_en_reel`, `test_ce311_garde_de_temps_compte_la_moisson` |
| bras sans gradient sur une autre banque que sa course d'origine | course refusée | garde (`cli.lancer`, CE-06) : `test_bras_apparie_adaptatif_memes_g000_avec_memoire` |
| entraînement qui désigne une tâche de test (ou du vivier), objectif refusé, plafond d'entraînements | `REFUSE` ou `PLAFOND`, journalisé | garde (`Entraineur.valider`) : `test_entraineur_sonde_sain_et_artefacts` |
| résultat d'entraînement ou modèle non conforme | `ECHEC_ENTRAINEMENT`, modèle non servi | garde (`_lire_resultat`) : `test_lire_resultat_modele_non_conforme_refuse` (un cas sain, six artefacts : CE3-18) |
| plafond de dollars d'une génération, d'une ronde ou d'une course | appels refusés (`PLAFOND`), course arrêtée | garde du noyau (réservation au pire cas) : `test_appels_paralleles_plafond_tenu_au_pire_cas` ; `_doit_arreter` : `test_ce312_doit_arreter_et_raison_juste` (CE3-12 : arrêt sur plafond total pendant la conception, avec la raison juste) |
| crédit d'un fournisseur épuisé en cours de course (HTTP 402, ou HTTP 400 — parfois une erreur de flux sous HTTP 200 — avec « credit balance is too low ») | génération `CREDIT_EPUISE` invalidée, course arrêtée, aucune relance ; une autre erreur 400 n'arrête rien | garde du noyau (CE3-05, R-395) : `test_ce305_credit_epuise_arrete_la_course`, `test_r395_credit_epuise_rendu_en_400_arrete_la_course` |
| modèle servi différent du modèle demandé (génération ou ronde) | génération invalidée (`MODELE_NON_CONFORME`), lignée arrêtée | garde du noyau : `test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee` |
| fichier `STOP` à la racine d'une course | la boucle s'arrête avant la génération (ou la ronde) suivante | garde du noyau : `test_fichier_stop_arrete_la_boucle` |
| lien symbolique, tube, socket ou fichier à plusieurs liens durs posé par l'organisme | jamais suivi ni ouvert par root ; écarté et consigné (`elements_ecartes`) | garde du noyau (R-372) : `test_fichiers_lecture_et_copie_sans_lien`, `test_depot_ne_suit_aucun_lien_de_l_organisme`, `test_organisme_poseur_de_liens_ne_voit_rien_du_noyau` |
| organisme qui crée `noyau/` ou `corpus/` dans son dossier, ou tente de renommer les dossiers du noyau | écarté, non archivé ; dossiers du noyau intacts (hors de son dossier) | garde du noyau (CE3-07) : `test_ce307_dossiers_du_noyau_hors_du_travail_et_non_falsifiables` |
| journal des appels absent après des appels servis | génération `ANOMALIE_NOYAU` invalidée | garde du noyau (CE3-07) : `test_ce307_anomalie_journal_absent` |
| vue d'une lignée lisible par une autre lignée ou une autre course | impossible par les droits (0750, groupe de la lignée ; `archive_vue/` 0711 ; utilisateurs distincts par course) | garde du noyau (CE3-06) : `test_ce306_vue_lisible_par_la_seule_lignee_et_uid_par_course` |
| requête de recherche, notice rendue ou document qui recoupe une tâche de test | `REFUSE_FUITE` ou notice retirée, consigné au journal du noyau ; audit à la lecture | garde du noyau (CE3-04, RV-07, RV-12, CE4-03) : `test_garde_fuite_empreintes_et_recoupement`, `test_recherche_refuse_une_requete_qui_copie_une_tache_de_test`, `test_rv07_notices_qui_recopient_une_tache_de_test_retirees`, `test_telechargeur_met_en_quarantaine_un_document_contenant_une_tache_de_test`, `test_rv12_garde_de_fuite_cablee_de_bout_en_bout`, `test_ce403_garde_unicode_deux_sens_et_identifiants_tires` |
| vivier sans compagnon conforme, malformé, servi sans phase de conception ou avec `--depuis` ; item qui recoupe un texte de la banque dans un sens ou l'autre | course refusée ; item écarté et compté | garde du noyau : `test_vivier_gardes_compagnon_format_et_recoupement`, `test_vivier_de_conception_servi_en_conception_seulement`, `test_ce403_garde_unicode_deux_sens_et_identifiants_tires` |
| téléchargement hors provenance, http, hôte interdit pour la référence initiale ; plafonds ; source inconnue | `ECHEC_TELECHARGEMENT`, `PLAFOND`, `SOURCE_INCONNUE`, consignés | garde du noyau : `test_telechargeur_provenance_plafonds_et_extraction`, `test_moisson_de_bout_en_bout_en_simulation` |
| plus d'une paire sur quatre coupée | lecture « non concluant » | `lecture_h_g1`, `paires_h_g1` : `test_paires_h_g1_lues_dans_des_courses_appariees`, `test_h_g1_couverture_pannes_recoupements_et_trois_niveaux` |
| vue de l'archive contenant `juge/`, ou un `journal-entrainements.jsonl` ou un `modele.npz` du noyau | la paire touchée est invalidée (pas toute la lecture), audit | vérification humaine après la course : `find <espace>/archive_vue* \( -name juge -o -name journal-entrainements.jsonl -o -name modele.npz \)` ; chaque fichier trouvé est comparé aux empreintes des fichiers du noyau de la même génération (archive complète, `travail/noyau/`) : seul un fichier identique est un défaut ; un fichier de l'organisme qui porte ce nom n'en est pas un (CE3-07, CE4-10 d) |
| arrêt de l'hôte en cours de course | course arrêtée, consignée ; paires lues à la dernière génération valide commune ou coupées ; aucune relance | règle gelée (Plan, point 3) ; `<course>.fin.json` absent : constaté au journal du lanceur |
| clé ou identifiant d'espace de travail dans une sortie versée | versement refusé | vérification humaine (recherche des formes de clés) et garde de la copie expurgée (`scripts/depot_expurge.py`) |

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf, le 24 octobre 2026 de 18:32 à 19:02 UTC. Brouillon relu :
  `brouillon-gradient-etape1-sondes-v1.md` `2b6e5dcb81dc081e20431a092f982ef373960d1317e4c407528cadf5a5ae6f7c`. Rapport :
  `contre-lecture-preenregistrement-gradient-etape1-v1.md` `2efeb8db86a9005c9e743d17a90f366830cb67adfe8d834f23dd1b30eb092d3a`.
  Verdict : non scellable en l'état ; 5 bloquantes, 7 majeures, 5 mineures, 3 de forme ; traitement : table de la v3
  (`41feda40…`), inchangé.
- **Contre-lecture 2** — sous-agent neuf, sur la v2 `6ae4a8b367ccf6ac9de69e7c792971b8a1b3bab283ad49c549a95094dc8b1507`.
  Rapport : `contre-lecture-preenregistrement-gradient-etape1-v2.md` `c377b2e3645c5fd69781cf609c2db47c5f718815d0dbc7459a33b6d3404ccfbd`.
  Verdict : scellable après corrections ; 2 bloquantes, 1 majeure, 4 mineures, 2 de forme ; traitement : table de la v3,
  inchangé ; reste de CE2-03 et CE2-09 traité par CE3-01 et CE3-03 ci-dessous.
- **Contre-lecture 3** — sous-agent neuf, le 24 octobre 2026 de 20:21 à 21:12 UTC, sur la v3
  `41feda40a5f51858afd8c5167a4b86c3b495ec059929c6ff1f8aa59c8ad1b2d5`. Rapport :
  `contre-lecture-preenregistrement-gradient-etape1-v3.md` `76f96658ed1ebb5fb34ea002fb1edf87dd1551b8ffc74ad3eb67d374c7b5cdb8`.
  Verdict : scellable après corrections ; 2 bloquantes, 6 majeures, 7 mineures, 3 de forme. Traitement :

| remarque | traitement |
|---|---|
| CE3-01 mémoire de conception servie au seul bras A | accepté, code de « conv-audit » (`9d53ae3`, dans `ed3ce0e`) : B importe les rondes de A (historique, vue) ; essai `test_bras_apparie_voit_les_rondes_de_conception_de_l_origine` ; texte : Hypothèse, Métrique |
| CE3-02 rondes comptées comme générations notées | accepté, code (`669def0`, `5e6876d`) : `generations_valides` écarte phase, import, invalidé ; `reponses_finales` lève une erreur ; essais `test_paires_h_g1_ecartent_les_rondes_de_conception`, `test_h_g1_couverture_pannes_recoupements_et_trois_niveaux` |
| CE3-03 audit sur absence de réponses ; pas de sortie | accepté, code (`5e6876d`) : couverture ≥ 80 % (paire coupée), seuil bas sur les tâches répondues, sortie gelée (`apres_audit`) ; lignées imposées : sans objet ; texte : table et sortie de l'audit |
| CE3-04 recherche de provenance des textes de test | décision (c) de Lazar : garde et mesure ; code (`a8e9ce2`, `5e6876d`) ; Plan, point 11 ; trois essais |
| CE3-05 conditions extérieures non appariées | accepté : code (`c02bae3`, `5e6876d`) — HTTP 402 arrête la course, sources et présence de Brave au manifeste, bras B refusé si elles diffèrent, paire coupée sur panne extérieure > 10 points ; lanceur : même présence de Brave exigée ; texte : Métrique ; lancer B dès les g000 de A (suggestion 4) : non retenu (B part quand A est finie, verrou), l'écart d'heure est dit et mesuré |
| CE3-06 vues lisibles hors de la lignée et de la course | accepté : code (`7887f1d`) — vues 0750 au groupe de la lignée, `archive_vue/` 0711, `--decalage-uid` par course ; lanceur : dossier des courses à root en 0700, entrées 0700, sorties 0600 ; essais du noyau et du lanceur |
| CE3-07 dossiers du noyau renommables | accepté : code (`7887f1d`) — `<travail>.noyau` et `<travail>.corpus` hors du dossier de l'organisme, noms réservés, journal absent = `ANOMALIE_NOYAU` ; texte : la ligne « vue de l'archive contenant … » invalide la paire touchée |
| CE3-08 `--strip-components=3` | accepté : lanceur v2, `--strip-components=2` ; essai du lanceur |
| CE3-09 lanceur sans empreinte, en-tête périmé, graine absente | accepté : lanceur v2 cité avec son empreinte ; en-tête juste ; graine absente : code 2 avec note (essai) ; addendum pour tout changement |
| CE3-10 lignées imposées en conception | sans objet : plus de lignées imposées (R-370) |
| CE3-11 temps, interruption, moisson, contention | accepté : durées au pire (Plan, point 4) ; règle d'arrêt de l'hôte ; garde de temps étendue à la moisson (`c02bae3`, essai) ; cœurs et `DELAI_DEPASSE` rapportés |
| CE3-12 garde de plafond pendant la conception | accepté : `_doit_arreter` sert les deux boucles, raison juste (`c02bae3`, essai) ; ligne de la liste d'arrêt réécrite |
| CE3-13 répétition qui lit les scores ; Gemini non exercé | accepté : sortie scellée non lue, statuts par l'extrait mécanique sans score (`cf67025`) ; Opus et Argon à la répétition, appel de contrôle des deux |
| CE3-14 sections de « conv-audit » contradictoires | accepté : Plan, point 9 (ce qui prime, ce qui vaut, phrase sur l'injection nuancée) |
| CE3-15 clé Brave, requêtes web, consignation | accepté : R-363 cité ; borne des requêtes (Plan, point 4) ; consignation exigée par le lanceur |
| CE3-16 graines : entrée et format | accepté : entrée de la dernière contre-lecture (la 9 dans cette v9), format littéral hors bloc de code |
| CE3-17 ronde k et génération k : mêmes graines | accepté, code (`b7374a9`) : phase dans la clé (`DECALAGE_CONCEPTION`) ; vérifié par `test_vivier_de_conception_servi_en_conception_seulement` |
| CE3-18 menues inexactitudes | accepté : alignement sur la confrontation retiré (bornes propres) ; « six artefacts » ; 429 sans pièce mesurée, dit ; phrase de 20:42 ; « condition mécanique rapportée » ; borne sans déclaration déduite ; manifeste des sources (`c02bae3`) ; redirections : texte (Plan, point 9) ; `fin_conception.json` lu borné (`4967734`) |

- **Relecture de « conv-audit »** (message n° 20, remarques, pas une contre-lecture R2) : RE-01 = CE3-01 ; RE-02 hôte et
  arrêt de l'hôte : Plan, point 3 ; RE-03 N-026 : Hypothèse, H-G2 ; RE-04 B après A : Métrique ; RE-05 en-tête du lanceur :
  lanceur v2.
- **Revérification du code (R2, demandée par la contre-lecture 3)** — sous-agent neuf, du 24 octobre 2026, 23:08, au
  25 octobre, 00:25 UTC, sur le commit `5e6876d` (corrections CE3-01 à CE3-18 du code et faille des liens symboliques).
  Rapport : `reverification-code-etape1-5e6876d-v1.md` `79bc4d13b9feb58041deee49289f456258a9e84f2d75ffddf3d9bfbad711072e`.
  Verdict : « corrections vérifiées avec réserves — dont une réserve bloquante » ; 1 bloquante, 7 majeures, 5 mineures,
  3 de forme. Traitement (code `45b7b08`, `44cd936` ; texte de la v5) :

| remarque | traitement |
|---|---|
| RV-01 (bloquante) lecture de H-G1 arrêtée sur une génération sans réponse ou à marque d'ordre d'octets | accepté, correction proposée : le noyau écrit et scelle `juge/reponses-lues.json` ; `reponses_finales` ne lit que lui ; sans réponse → paire coupée par la couverture ; essai `test_rv01_…` ; Métrique |
| RV-02 mémoire asymétrique par les dossiers vivants ; même décalage permis | accepté : dossiers vivants rendus à root (0700) après chaque dépôt (au lieu de les effacer : ils restent pour l'audit) ; contrat : `fichier_texte` valable pendant la génération ; `lancer --depuis` refuse le décalage de l'origine ; essai `test_rv02_…` |
| RV-03 vue importée de B lisible des autres lignées | accepté : vue importée au groupe de la lignée (0750 ; 0550/0440) dès l'import ; essai `test_rv03_…` (lecture réelle sous un autre utilisateur) |
| RV-04 /tmp, /var/tmp, /dev/shm et communications communs | accepté : dossiers en mémoire privés montés avant l'abaissement, `--ipc`, sockets hors de /tmp sous des noms imprévisibles, espace sous `/var/lib/essaim-m3` ; contrat ; essai `test_rv04_…` |
| RV-05 statut et erreurs relus en suivant les liens, tube bloquant | accepté : `lire_fichier_organisme` pour le statut, descripteur du noyau pour les erreurs ; essai `test_rv05_…` |
| RV-06 espaces de noms non exigés en réel | accepté : refus en réel ; lanceur : `--ipc` et dossier en mémoire exigés ; essai `test_rv06_…` |
| RV-07 garde partielle (notices, copies courtes, oracle) | accepté : notices retirées et comptées ; recoupements courts (5 mots) mesurés sans refus, descriptifs ; empreintes au seul journal du noyau ; le statut reste visible (limite dite, Plan, point 11) ; contrat ; essais `test_rv07_…`, quarantaine |
| RV-08 appels en vol hors du journal et de la dépense | accepté : attente des fils de service (≤ 900 s) avant la lecture ; reste compté ; essai `test_rv08_…` |
| RV-09 contexte de B distinct | accepté : même `rondes_conception_max`, historique sans `importee`, marque « imposée » de l'origine ; essai renforcé (contenus de la vue) |
| RV-10 sortie d'audit à resserrer ; pas de fonction gelée unique | accepté : `lire_h_g1` ; `defaut_paires` refusé sans `exclues`, réserve propre ; seuls les scores des paires lues déclenchent |
| RV-11 pannes : erreurs de l'organisme comptées, aucun effectif minimal | accepté (avec CE4-01) : `echec_exterieur`, effectif minimal, Fisher |
| RV-12 câblage non essayé ; fenêtres partagées avec l'entraînement | accepté : essai de bout en bout `test_rv12_…` (échoue sans le câblage) ; fenêtres de l'entraînement écartées ; part sur la banque réelle : non mesurée ici (banque hors des pièces relues), rapportée après coup par les comptes de refus |
| RV-13 traits non protégés | accepté : `lancer` met les traits en 0700/0600 (refus sinon) |
| RV-14 CE3-17 non corrigé à `5e6876d` | déjà corrigé dans `b7374a9` |
| RV-15 manifeste et temps | accepté : `coeurs` au manifeste, `recherche` retiré ; délais réseau par opération : dit (Plan, point 4) |
| RV-16 essais et empreintes | accepté : artefacts nouveaux (décalage, liens sur statut et erreurs, tirage) ; `test_ce307…` inchangé (le refus y est prouvé par ailleurs) ; empreintes : celles de ce texte, au commit cité |

- **Contre-lecture 4** — sous-agent neuf, du 24 octobre 2026, 23:46, au 25 octobre, 00:24 UTC, sur la v4. Texte relu :
  `gradient-etape1-sondes-v4.md` (marqueurs de scellement non remplis) `54b70722a6f87c53e450a6c3a5b4002f228d7d8ded46181b0bd79be47fd1a17e`.
  Rapport : `contre-lecture-preenregistrement-gradient-etape1-v4.md` `ab77c09b67b684822fc512e45b3a02e97b81fe3bd5683bf9b4718c79161dee3d`.
  Verdict : scellable après corrections ; 0 bloquante, 4 majeures, 7 mineures, 2 de forme. Traitement :

| remarque | traitement |
|---|---|
| CE4-01 règle des pannes coupée par le bruit des petits comptes | accepté, code : effectif minimal 10, écart > 10 points, ≥ 3 échecs d'écart, Fisher bilatéral p < 0,01, échecs extérieurs seulement, cumulés ; taux de coupure à tort rapporté (Seuil) ; essais sain et artefacts |
| CE4-02 bras B sans réponse ; absences partielles dans le sens prédit ; contrat inexact | accepté : texte — Métrique (7), (8), (9), limite dite ; rapport descriptif gelé (couverture, causes, Δ secondaire) ; code : demandes `INDISPONIBLE` comptées ; dire au contrat (3) : décision de Lazar, consignée en tête |
| CE4-03 garde du vivier à un sens, écritures non latines invisibles, vivier lisible | accepté, code : deux sens, normalisation Unicode, fenêtres de caractères, clé de doublon complète, identifiants tirés ; texte : Plan, points 10 et 11 ; comptes du vrai fichier demandés avec le message de transmission |
| CE4-04 répétition aveugle aux statuts ; Fable et B non exercés | accepté : extrait v2 (statuts par service et par source) ; porte mécanique gelée ; Fable à la répétition (30 USD) ; répétition B (10 USD) ; essai de l'extrait v2 |
| CE4-05 « identiques » inexact ; autres différences | accepté, code : contexte et historique de B égaux à ceux de A, indice des graines sur les lignées d'origine ; texte : Métrique |
| CE4-06 extrait de B : rondes importées non marquées ; dépense double | accepté, code : `importee` d'après l'index, `totaux_hors_importees` ; texte : Plan, point 12, et réserve « sans clé de score » |
| CE4-07 gardes du lanceur sans artefact ou fragiles | accepté : lanceur v3 — artefacts d'hôte, fichiers non suivis, vivier absent du commit (code 2), parité des clés par le fichier de A et par son manifeste, verrou d'extraction, `fin.json` dès le départ de la course, erreurs scellées |
| CE4-08 même hôte non exigé ; durée non éprouvée | accepté : empreinte de l'hôte exigée identique ; épreuve de durée (porte) ; texte : Plan, point 3 |
| CE4-09 clé Gemini : provenance et état | accepté : R-370 cité ; état dit ; imputation des appels de contrôle à GO-07 (lanceur et texte) |
| CE4-10 procédures non codées, réserve inexacte, mesures mal bornées | accepté : `exclues` codé ; réserve propre ; conception comptée ; vérification `find` par empreintes ; rapport descriptif des deux familles gelé |
| CE4-11 réfutation à tort non dite | accepté : Seuil |
| CE4-12 lecture littérale : première occurrence | accepté : le lanceur refuse plus d'une occurrence (essai `graine-en-double`) ; une seule occurrence de chaque nom dans ce texte |
| CE4-13 menues inexactitudes | accepté : `recherche` retiré du manifeste ; empreinte de `EMPREINTES-v1.txt` du collisionneur et GO-07 cités ; clés hors de toute ligne de commande (lanceur v3) |

- **Contre-lecture 5** — sous-agent neuf, le 25 octobre 2026 de 01:27 à 02:14 UTC (conteneur redémarré à 01:29, reprise à
  01:30), sur la v5. Texte relu : `gradient-etape1-sondes-v5.md` (marqueurs de scellement non remplis)
  `d7cf7746bd85c5eb63f13495116ccb2b069363a7a8b3bc304a1e10613c57839d`. Rapport :
  `contre-lecture-preenregistrement-gradient-etape1-v5.md` `53e6527c4302be59b53bdc6e01e2835c08527160b89198a10edbda17876ce204`.
  Verdict : **non scellable** ; 1 bloquante, 2 majeures, 7 mineures, 2 de forme. Traitement (code `224de13`, lanceur v4,
  texte de la v6) :

| remarque | traitement |
|---|---|
| CL5-01 (bloquante) le test final lisible par l'organisme sur l'hôte (dépôt et code lisibles par tous) | accepté, code : le noyau recouvre le dépôt, ses objets git, l'arbre du code (`ESSAIM_M3_CACHER`, passé par le lanceur) et /home, /root, /srv, /mnt, /media d'un dossier en mémoire vide en lecture seule dans l'espace de montage de l'exécution ; essai `test_cl5_01_banque_cachee_a_l_organisme` ; Plan, point 13 |
| CL5-02 (majeure) voie commune par un dossier inscriptible par tous hors des quatre | accepté, code : `dossiers_inscriptibles_par_tous` balaie tous les systèmes de fichiers une fois ; chaque exécution recouvre chacun d'un dossier en mémoire privé ; essais `test_cl5_02_*` ; Plan, point 13 |
| CL5-03 (majeure) amorçage de Fable refusé par le plafond de 3 USD de la répétition | accepté, lanceur v4 : répétition à 5 USD par génération (plafond 40) ; essai `test_cl5_03_repetition_amorce_fable_sous_son_plafond` ; Seuil et annexe recalculés |
| CL5-04 `lire_h_g1` sans essai ; `exclues` accepté sans audit | accepté : `lire_h_g1` refuse `exclues` hors de `defaut_paires` ; essai `test_cl5_04_*` |
| CL5-05 traitements sans essai (RV-13, CE4-02 `INDISPONIBLE`, CE4-10 c) | accepté : essai `test_cl5_05_*` ; RV-15 « délais par opération » dit au Plan, point 4 (bornes par opération, non stricte) |
| CL5-06 gardes du lanceur sans essai dans sa suite | les gardes d'hôte (l. 73-74) et le calcul de la porte sont vérifiés par le relecteur ; les essais du lanceur (53) couvrent `unshare -n`, `protected_hardlinks`, non-root, l'autre hôte et les portes ; un faux `unshare` qui échoue toujours masque les l. 73-74, dit |
| CL5-07 crédit épuisé, clé invalide, certificat mal classés | accepté, code : `echec_exterieur` les reconnaît extérieurs même sous un code 400 ; essai ; le crédit épuisé rendu en 400 n'arrête pas la course par lui-même (le 402 seul le fait) : limite dite |
| CL5-08 « état au scellement » contredit par l'environnement | accepté, texte : l'état observé au 25 octobre est écrit (noms des clés définis ; le crédit réel reste à trancher par l'appel de contrôle) ; cas « Brave présente » dit (cinq comparaisons de pannes) |
| CL5-09 épreuve de durée ne couvre ni la durée des courses ni un redémarrage | accepté, texte : limite dite ; les courses sont lancées détachées, PID consigné |
| CL5-10 porte non passée venant de l'organisme ; suite non écrite | accepté, texte et lanceur : ne comptent que les échecs du noyau ou du fournisseur ; la suite (décision de Lazar, addendum) est écrite |
| CL5-11 chiffres et renvois | accepté : noms des pièces de mutation justes (`mutations-rv-v2.txt`, douze de la v5, scellée en l'état, R12 ; `sortie-mutations-cl5-v1.txt`, quatre de la contre-lecture n° 5 ; CL6-05) ; coupure à tort à effectifs inégaux dite (0,76 %) ; durées au pire avec l'attente ; point 12 corrigé (l'amorçage n'est pas dans l'extrait) ; ligne procédurale ajoutée dite |
| CL5-12 script de scellement | accepté : `prereg/pieces-gradient-etape1-v7/sceller_etape1_v7.py` (docstring juste, CL6-04) ; `vivier_message` exigé avec les comptes et l'empreinte (Documents) |

- **Contre-lecture 6** — sous-agent neuf, le 25 octobre 2026 de 02:53 à 03:21 UTC, revérification limitée aux corrections
  CL5-01 à CL5-12 (texte v6, diff du code de `44cd936` à `224de13`, lanceur v4). Texte relu :
  `gradient-etape1-sondes-v6.md` (marqueurs de scellement non remplis)
  `ce78d5e59e3ae8e29b998f272d10a65c42765e32d45b6c9c3dc5180dd5b45c4e`. Rapport :
  `contre-lecture-preenregistrement-gradient-etape1-v6.md` `8e503e3ebdc313460eba1f60353762cc3010800cfd25fb1426cf835d3056d372`.
  Verdict : **non scellable** ; 1 bloquante, 1 majeure (bloquante pour l'exécution), 1 mineure, 2 de forme. Le fond des
  corrections CL5-01 à CL5-12 est jugé juste et éprouvé (8 traitées, 4 en partie, les parts non faites étant les cinq
  remarques ci-dessous). Traitement (code `224de13` → `bef2c2f`, lanceur v4 inchangé ; texte de la v7) :

| remarque | traitement |
|---|---|
| CL6-01 (bloquante) le script de scellement refuse de sceller le texte : il cherche l'entrée « Contre-lecture 6 » au libellé « lanceur v3 corrigé », que le texte v6 ne porte plus (il dit « lanceur v4 ») | accepté, texte et script : le libellé « lanceur v4 » est partout (version, Documents, entrées de contre-lecture) ; le script de scellement de cette v7 (`sceller_etape1_v7.py`) cherche et inscrit l'entrée « Contre-lecture 7 » au libellé « lanceur v4 » ; scellement à blanc rejoué |
| CL6-02 (majeure, bloquante pour l'exécution) la boucle `prives` abandonne sur un dossier inscriptible par tous imbriqué sous un temporaire déjà rendu privé ; aucun organisme ne tourne | accepté, code (`bef2c2f`) : la boucle `prives` de `ABAISSER_SOURCE` absorbe errno 2 (parent déjà couvert), comme la boucle `caches` ; essai sain et artefact `test_cl6_02_dossier_inscriptible_imbrique_sous_un_temporaire` ; mutation `cl6-02` (retrait du saut errno 2 → l'essai échoue) ; arbre du noyau et empreinte de `bac_a_sable.py` nouveaux |
| CL6-03 (mineure) contradiction interne sur la présence de Brave au scellement (une clause disait l'inverse de « État au scellement ») | accepté, texte : la clause est réécrite pour concorder — nom de Brave défini au scellement ; cinq comparaisons par paire si Brave est présente au lancement, sous réserve de cette présence |
| CL6-04 (forme) la docstring du script de scellement n'était pas « juste » (« contre-lecture n° 4 », « `sceller_etape1_v4.py` ») | accepté, script : docstring de `sceller_etape1_v7.py` juste (contre-lecture n° 7, décliné de `sceller_etape1_v6.py`) |
| CL6-05 (forme) le nom de la pièce de mutations n'était pas corrigé (l. 37 citait « mutations-rv-v2.txt » et « mutations-cl5-v1.txt ») | accepté, texte : les noms cités sont ceux des pièces réellement versées — `mutations-rv-v2.txt` (douze de la v5, scellée en v5, R12) et `sortie-mutations-cl5-v1.txt` (quatre de la contre-lecture n° 5), plus `sortie-mutations-cl6-v1.txt` (CL6-02) ; revendication CL5-11 alignée |

- **Contre-lecture 7** — sous-agent neuf, le 25 octobre 2026 de 03:54 à 04:06 UTC, revérification limitée aux
  corrections CL6-01 à CL6-05 (texte v7, diff du code de `224de13` à `bef2c2f`, lanceur v4). Texte relu :
  `gradient-etape1-sondes-v7.md` (marqueurs de scellement non remplis)
  `84708a9222dd4eddb809bff3bb8994051ea85fe485f13736ee4e547adaaeb0e7`. Rapport :
  `contre-lecture-preenregistrement-gradient-etape1-v7.md` `624df897512a09209237f5b637bd68750f1111b7cade2fc1ce977723921d71b4`.
  Verdict : **scellable** ; 0 bloquante, 0 majeure, 1 mineure (non bloquante), 0 de forme. Traitement :

| remarque | traitement |
|---|---|
| CL7-01 (mineure) le bloc du commit citait sous `prereg/pieces-gradient-etape1-v7/` deux sorties du lanceur v4 produites pour la v6 (empreintes inchangées) ; leur présence au nouveau chemin restait à vérifier au scellement | vérifié : `sortie-essais-lanceur-v4.txt` et `sortie-options-analyseur-v4.txt` sont dans `prereg/pieces-gradient-etape1-v7/`, aux empreintes citées ; sans objet pour cette v8 : les sorties du lanceur v5 sont neuves, dans `prereg/pieces-gradient-etape1-v8/` |

- **Changements de la v8 hors contre-lecture** (décisions de Lazar et constats du 25 octobre ; aucun énoncé changé) :

| objet | changement |
|---|---|
| R-393 question « structure » à `c001` (décision 1 (a) de Lazar) | lanceur v5 : `--question-ouverte … --question-ouverte-aux c001` pour A_r et la répétition (v9 : la répétition seule, R-410), pièce extraite et vérifiée par son empreinte littérale ; porte de la répétition ; texte : Hypothèse (H-C), Métrique (6), Plan, points 2, 3, 8, 14, Liste d'arrêt ; essais du lanceur |
| R-396 réponse de `c001` absente de la vue de B | code `90595ffb` : `importer_conception` la recopie ; essai et mutation |
| R-395 crédit épuisé rendu en HTTP 400 (pilote, R-391) | code `90595ffb` : `credit_epuise` ; essai et mutation ; lève la limite dite de CL5-07 ; Métrique (4), Liste d'arrêt |
| R-398 contrat « réflexion comprise » (décision (a) de Lazar, relayée) | code `c66f529` : contrat § 3 ; essai et mutation ; Plan, points 2 et 4 ; porte : appels par espèce et par statut rapportés, vérification humaine |
| R-394 crédit Anthropic : clés n° 3 et LUC (décision 2 (a) de Lazar) | lanceur v5 : `CLE_ANTHROPIC`, noms admis, en-tête pour la n° 1 seulement, nom consigné et exigé identique pour B_r ; état au scellement et réserve de crédit (Plan, point 3 ; Annexe) |
| R-399 vivier transmis (« conv-audit », n° 35 § 1) | Documents ; comptes et réserve « proches » (Plan, point 10) ; seuil inchangé |
| défaut du lanceur v4 : chemin du préenregistrement lu (`…-v5.md`) | lanceur v5 : `prereg/gradient-etape1-sondes-v8.md` ; les essais écrivent le préenregistrement factice sous ce nom |
| R-400 lecture du pilote corrigée | Plan, point 4 : troncatures au `max_tokens` demandé par l'organisme |
| R-402 réflexion non tracée au journal (« conv-audit », n° 36 § 4) | code `5d1d4fd` : types de blocs au journal des appels, appels qui ont réfléchi comptés par l'extrait ; essai et mutation ; porte : `reflexion_par_espece` |
| R-403 GO-07 échoit le 26 octobre (mot direct de Lazar : GO-05) | lanceur v5 : tests de dépense imputés à GO-2026-10-24-05 ; essais `go-refuse-GO-2026-10-24-05`, `go-07-absent-sans-effet` ; Plan, point 3 ; Liste d'arrêt ; Annexe |
| R-404 recharge automatique active (mot direct de Lazar) ; test de dépense (décision de 09:58, relayée) | texte : seuls les plafonds du noyau bornent la dépense (Plan, point 3 ; Liste d'arrêt ; Annexe) ; lanceur v5 : test de dépense exige statut `OK` et jetons de sortie > 0 |
| R-405 hôte : option (a) (mot direct de Lazar) | Plan, point 3 : le conteneur de la session nouvelle, pour la répétition, l'épreuve et les quatre courses |

- **Contre-lecture 8** — sous-agent neuf, le 25 octobre 2026 de 09:28 à 10:08 UTC, relecture des changements de la v8
  (texte v8, diff du code de `bef2c2f` à `5d1d4fd`, lanceur v5 et ses essais). Texte relu : `gradient-etape1-sondes-v8.md`
  (marqueurs de scellement non remplis) `4c98ed5123bbe60d0fabf084340ae705464993027be4535915b27aa7bb2d1995`. Rapport :
  `contre-lecture-preenregistrement-gradient-etape1-v8.md` `64e4fe74e9b2531b2b23dde56ab260bc43f580909adb5f4e22d83b720ddd6c6d`.
  Verdict : **scellable après corrections** ; 0 bloquante, 1 majeure, 7 mineures, 4 de forme. Traitement (code `5d1d4fd`
  → `4de6544` pour R-415 et R-417 seulement, lanceur v6, texte de cette v9) :

| remarque | traitement |
|---|---|
| CL8-01 (majeure) la question de `c001`, qui nomme les sondes, posée au seul bras qui a le service, interagit avec le traitement dans le sens prédit | accepté, décision de Lazar (R-410) : la question n'est posée qu'à la répétition ; les courses décisives ne la reçoivent pas ; texte : H-C, Métrique (6), Plan, points 2, 3 et 14, Liste d'arrêt ; lanceur v6 (A_r sans question ; constat `A1 sans question`) |
| CL8-02 (mineure) coupures par la réflexion sous 4 096 jetons, surtout sur B ; seuil de 50 % ; Argon non regardé | accepté : mécanisme nommé (Métrique (7)) ; statuts des appels et appels qui ont réfléchi rapportés par paire et par bras (Plan, point 6) ; taux soumis à Lazar quels qu'ils soient, Argon compris, et limite d'Argon dite (point 8) |
| CL8-03 (mineure) la garde du test de dépense n'a pas d'essai dans la suite | accepté comme limite : éprouvée par lecture et par le rejeu de la contre-lecture n° 8 ; premier cas sain réel à la répétition (Liste d'arrêt) |
| CL8-04 (mineure) hôte : cohabitation, mandataire, perte du disque | accepté : second pilote fini avant A_1 et A_2, décalages 700 et 800, aucune autre course pendant A_r et B_r ; copie scellée des sorties après chaque course (Plan, point 3) ; HTTP 405 et 407 du mandataire : limite dite, règle des pannes inchangée (Métrique (4)) |
| CL8-05 (mineure) aucune ligne de GO valide après le 26 ne nomme les clés employées | accepté : ligne d'extension de GO-04 nommant les clés n° 3, LUC et Gemini n° 2, débitées sur le compte du programme (Lazar, R-411) ; nom de clé et compte à la ligne de dépense (Plan, point 12) |
| CL8-06 (mineure) la borne de 1 150 USD vaut par exécution ; plafond de recharge non consigné | accepté : borne par exécution dite ; aucun plafond de recharge (Lazar, R-412) ; Plan, point 3 ; Annexe |
| CL8-07 (mineure) chiffres du § 3 du contrat sans source ; Gemini non couvert | accepté, texte : sources citées (pilote ; tour « structure », journal empreinté) ; 1 200 non cité et Gemini non couvert : limites dites (Plan, point 2) ; contrat inchangé |
| CL8-08 (mineure) changement annoncé de la lecture de H-G1 | accepté, décision de Lazar (R-413) : lecture inchangée ; plancher de bruit et témoins de sortie, s'ils viennent, descriptifs, par addendum avant toute lecture (Plan, point 6) |
| CL8-09 (forme) en-tête et banc de mutation | accepté : en-tête de la v8 corrigé (code `5d1d4fd`, quatre changements, « hypothèse testée ») ; docstring du banc corrigée, extension à quatre mutants avant tout versement consignée (R-414) |
| CL8-10 (forme) pièces citées sans empreinte ; script de scellement non cité | accepté : pièces citées avec empreinte, script de scellement v9 cité (point « Lanceur ») |
| CL8-11 (forme) noms et précisions | accepté : « test de dépense » partout ; plafonds rattachés aux 27 appels coupés ; motifs précisés (Métrique (4)) ; plafonds servis (point 8) ; contrat § 7 : limite dite (point 14) ; justification de R-396 corrigée au registre (R-414) |
| CL8-12 (forme) « 3 × 3 × 5 » | accepté : « 3 × 1 × 5 » |

- **Changements de la v9 hors contre-lecture** : clés OpenAlex (R-415, Lazar : « maintenant ») et Semantic Scholar (R-417),
  lues par le noyau seul, masquées, appariées ; lancement depuis cette session (R-416) ; plafond du second pilote porté à
  120 USD (R-409).

- **Contre-lecture 9** — sous-agent neuf, revérification limitée aux corrections CL8-01 à CL8-12 (texte v9, lanceur v6
  et ses essais ; diff du code de `5d1d4fd` à `4de6544`).
  Texte relu : `gradient-etape1-sondes-v9.md` (avant remplissage des marqueurs de scellement) `7f012573e6f45bb18c7ec30680bc365a7f3c30d21edb3eed38ab98ec800d6fd2`.
  Rapport : `prereg/contre-lectures/contre-lecture-preenregistrement-gradient-etape1-v9.md` `f53b4e44b36d3b142e9a09fa285e20d8ab5540a735207b129cb2421badfad039`. Verdict : **scellable** ; 0 bloquante, 0 majeure, 3 mineures, 3 de forme (CL9-01 à CL9-06) ; vérifications de 11:27 à 11:47 UTC, rapport à 11:50 UTC. Traitement : remarques acceptées comme réserves, scellées avec le texte (R-418). CL9-01 (mineure) : une clé de moisson peut sortir par une redirection (la bibliothèque recopie l'en-tête vers l'adresse finale avant le contrôle de l'hôte ; vrai aussi de Brave, depuis avant la v9) et figure dans les réponses brutes gardées ; avant toute copie poussée hors du conteneur, une recherche par valeur des clés, sans les afficher, est faite et la copie refusée si une valeur y figure ; correction du code à la version suivante du noyau. CL9-02 (mineure) : l'ordre « masquer puis tronquer » et la parité dans l'autre sens ne sont prouvés par aucun essai ; vérifiés par lecture et par le rejeu de la contre-lecture n° 9 ; essais à ajouter à la version suivante. CL9-03 (mineure) : la présence des clés de moisson (Brave, OpenAlex, Semantic Scholar) est fixée par la répétition pour toute l'étape ; si elle change avant une course décisive, celle-ci ne part pas tant qu'elle n'est pas rétablie (vérification humaine du fichier des clés de la répétition) ; entre A_r et B_r, le lanceur refuse B_r : la présence est rétablie, ou les paires de la réplique sont coupées, sans relance. CL9-04 (forme) : lire « vers 11:20 UTC » pour l'état au scellement. CL9-05 (forme) : les clés de moisson ne sont nommées par aucune ligne de GO valide après le 26 octobre : demandé à Lazar ; elles ne débitent aucun appel de modèle. CL9-06 (forme) : les mots du lanceur (« appel de contrôle », « plafonds demandés », en-tête) restent en l'état, changer le lanceur changerait son empreinte citée ; artefact « question en lien symbolique » non ajouté (limite) ; la sortie du banc v8 a été régénérée sous le même nom avant tout versement, après la correction de sa docstring (R-418).
- **Entropie et graines** (Plan d'analyse, point 5 ; `secrets.randbits(128)` au scellement, `SeedSequence(E).spawn(3)`,
  `generate_state(1, uint64)[0]` de chaque enfant), au format littéral lu par le lanceur :
  - E = 204970097463133775663669627593621706019
  - graine_1 = 15593150781231018102
  - graine_2 = 8479434606598060558
  - entropie_analyse = 13225756771307544762

## Annexe — ordre de grandeur de la dépense (informatif, non opposable, R7)

GO-2026-10-24-05 : coût accepté par Lazar sans devis. Bornes techniques : 2 × 360 + 2 × 190 = 1 100 USD au pire cas
(réservé au pire cas par le noyau), plus 40 USD de répétition et 10 USD de répétition B (GO-2026-10-24-05), et moins de
1 USD de tests de dépense par course (GO-2026-10-24-05, R-403) ; l'épreuve de durée ne coûte rien ; attendu de l'ordre
de 200 à 250 USD (estimation illustrative de « conv-audit », message n° 22 § 3 : le bras A répond surtout par ses sondes,
le bras B par texte). Crédit Anthropic visible au lancement, selon Lazar : 75 USD (clé n° 3) et 165 USD (clé LUC),
soit 240 USD, plus la réserve n° 2 (R-394), à l'intérieur de la fourchette attendue pour les quatre courses, avant les
répétitions (au plus 50 USD) ; la recharge automatique étant active sur toutes les clés (R-404), le crédit ne borne pas
la dépense : seuls les plafonds du noyau la bornent, au pire cas réservé ci-dessus (1 150 USD par exécution, tests de dépense en sus ;
Plan, point 3) ; aucune console ne plafonne la recharge (R-412). Aucune carte n'est louée pour cette
étape (l'extraction des traits est faite : R-360).
