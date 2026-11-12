# Contre-lecture n° 4 (R2) — préenregistrement « gradient conçu par l'essaim », étape 1 (sondes) — v4 « économe »

- Relecteur neuf : sous-agent de contre-lecture R2 n° 4. Il n'a écrit ni le brouillon v1, ni les v2, v3, v4, ni le code,
  ni le lanceur, ni les sections de conception et de moisson, ni les trois contre-lectures précédentes, ni la
  revérification du code sur `5e6876d`. Date (UTC, lue par `date -u`) : du 2026-10-24 23:46 au 2026-10-25 00:24.
- **Texte relu : `gradient-etape1-sondes-v4.md`, SHA-256
  `54b70722a6f87c53e450a6c3a5b4002f228d7d8ded46181b0bd79be47fd1a17e`** (compagnon vérifié : OK).
- Pièces relues : la v3 (`41feda40…`), les rapports n° 1 (`2efeb8db…`), n° 2 (`c377b2e3…`) et **n° 3** (`76f96658…`) ; le
  code de `essaim-m3-refonte-v1/` des pièces ; le diff `5e6876d..ed3ce0e` ; le lanceur v2, ses essais et leur sortie ; la
  puissance (script, v1, v2) ; la sonde d'hôte et son journal ; les manifestes des traits ; le résumé de la banque, son
  LISEZMOI v3 et sa provenance ; le résultat du collisionneur ; les messages n° 20, 21, 22, 25, 28, 29 de « conv-audit » et
  n° 20, 21, 22 de « session-depot » ; l'extrait des registres v5 ; `CLAUDE.md`, le gabarit et le validateur.
- Empreintes citées par la v4, recalculées et **toutes concordantes** : `analyse_gradient.py` `9fdeacb9…`, `analyse.py`
  `bf9c1a3b…`, `boucle.py` `ebf4c44d…`, `cli.py` `8a186b5a…`, `vivier.py` `b08094e3…`, `fichiers.py` `8bbc8dfd…`,
  `garde_fuite.py` `b17d3c82…`, `entrainement.py` `c06685bf…`, `moisson.py` `6973546e…`, `contrat.py` `40211a25…`,
  `extrait_mecanique.py` `6150da91…` ; arbre du noyau (`empreinte_arbre`) `7160461a…` ; lanceur `2c630e75…`, essais
  `d13f2bc6…` ; MISSION `bd2c6a15…`, note du programme `6b415104…`, sections `180a39af…`, collisionneur `213b52ef…` ;
  empreintes des traits `add13e09…`, manifeste `034d8460…`, script d'extraction `8286f4e7…` ; puissance v2 `50a1c248…`,
  script `e05f48bc…`, puissance v1 `eaf4ea5d…` ; sonde `5ac61f5a…`, journal `5e97b2d5…` ; brouillon v1 `2b6e5dcb…`. Tous les
  compagnons des pièces : OK.
- **Code des pièces = commit cité.** Un arbre de travail détaché à `ed3ce0ee29c0b8ccfb4c8ed67df6324a7f9e97ff`, tiré d'un
  clone partagé du dépôt dans mon dossier de travail, est identique aux pièces (`essaim_m3/`, `tests/`, collisionneur,
  sections) ; le diff `5e6876d..ed3ce0e` recalculé est celui des pièces (lignes `index` mises à part).

## VERDICT : **scellable après corrections**

Aucune bloquante. Les corrections de la contre-lecture n° 3 sont réelles dans le code et le lanceur (suivi plus bas) ; la
mémoire de conception est bien importée dans le bras B (vue de g000 identique en chemins **et** en contenus, rejoué) ; le
validateur ne relève que les marqueurs et l'entrée « Contre-lecture 4 » ; les 22 essais du lanceur se rejouent à
l'identique ; l'analyseur du noyau accepte les trois lignes de commande ; les chiffres de la banque, des traits, des
plafonds, des durées, des gardes de temps et de la puissance se vérifient.

Quatre **majeures**, qui touchent la lecture de H-G1 et la répétition, à corriger avant le scellement :

1. **CE4-01** — la règle « panne extérieure » (écart de taux d'échec > 10 points, par source, à la génération lue) coupe des
   paires sur le seul bruit des petits comptes : à taux d'échec **identiques** dans les deux bras, deux paires coupées ou
   plus sur six (lecture « non concluant ») ont une probabilité de 14 % à 98 % pour 2 à 10 recherches par source et un
   taux d'échec de 5 à 20 % (de 1 % à 28 % à 2 % d'échecs ; rejoué, E8).
2. **CE4-02** — le bras B relance sans service d'entraînement un organisme conçu avec lui, et paie chaque réponse par un
   appel : sous 80 % de couverture la paire est coupée (ce qui peut rendre H-G1 non concluante pour une cause liée au
   traitement), entre 80 et 100 % les absences de B comptent comme erreurs (dans le sens prédit). Rien de cela n'est dit ni
   rapporté ; le contrat promet à l'organisme une relance « à l'identique ».
3. **CE4-03** — la garde de disjonction du vivier ne mesure qu'un sens du recoupement et ne voit aucun texte sans lettres
   latines (copie exacte d'un texte de test cyrillique servie ; textes non latins distincts comptés « doublons ») ; or le
   vivier et ses vérités restent lisibles dans la vue de **toutes** les générations notées, dans les deux bras (rejoué).
4. **CE4-04** — l'extrait mécanique ne porte que des compteurs d'entraînements, de recherches et de téléchargements, pas
   leurs statuts : la répétition ne peut pas vérifier ce que le point 8 lui fait vérifier (entraînements, moisson) ; Fable et
   le chemin réel du bras B n'y sont pas exercés.

Décompte : **0 bloquante, 4 majeures, 7 mineures, 2 de forme.**

**Condition du scellement.** CE4-01, CE4-03 (si la correction de code est choisie) et CE4-04 changent le code ou le
lanceur (comme CE4-06 et CE4-07 si elles sont corrigées dans le code) : nouveau commit et nouvelle empreinte du lanceur cités, revérification par un sous-agent neuf limitée à ces
changements (R2). CE4-02 et le reste sont du texte, sauf options signalées.

**Validateur du dépôt** (`prereg.py` des pièces, bouchons inoffensifs pour `gardes` et `scellement`) : sur la v4, deux
plaintes exactement — « contre-lecture 4 sans ses deux empreintes » et « marqueurs de gabarit restants :
`<<HEURE_SCELLEMENT>>`, `<<REVERIFICATION_RAPPORT>>`, `<<REVERIFICATION_TRAITEMENT>>`, `<<VIVIER_CHEMIN>>`,
`<<VIVIER_COMMIT>>`, `<<VIVIER_MESSAGE>>`, `<<VIVIER_SHA256>>` » ; entrées détectées 1, 2, 3, 4 ; sur une copie remplie
de valeurs factices de bonne forme (entrée 4 avec deux empreintes), **aucun problème** (E4). Confirmé.

**Marqueurs.** Ce qui les remplit est défini, et le lanceur lit bien ce qu'il doit lire (E5) :
- `<<HEURE_SCELLEMENT>>` : heure `date -u` du scellement ; non lue par le lanceur.
- `<<VIVIER_COMMIT>>`, `<<VIVIER_CHEMIN>>`, `<<VIVIER_SHA256>>` : lus par `litteral` (lanceur l. 75, 80-82) au format
  `nom = valeur`, valeur nue (40 et 64 caractères hexadécimaux ; chemin en `[0-9a-zA-Z_./:-]`), **sans accents graves** ;
  non remplis, le lanceur s'arrête (« vivier : … absent », code 2) ; entre accents graves ou suivis d'un point, il s'arrête
  aussi (sûr). Le compagnon `<chemin>.sha256` doit exister au même commit (sinon sortie en code 128 sans note, CE4-07 c).
- `<<VIVIER_MESSAGE>>` : message de transmission de « conv-audit » (vérification de l'empreinte et de la disjonction des
  identifiants) ; à citer avec son empreinte (R6) ; non lu par le lanceur. Je recommande d'y joindre les comptes de
  `charger_vivier` sur le vrai fichier (CE4-03).
- `<<REVERIFICATION_RAPPORT>>`, `<<REVERIFICATION_TRAITEMENT>>` : chemin et empreinte du rapport du sous-agent sur
  `5e6876d`, et son traitement ; ils tombent dans le segment de l'entrée 3 pour le validateur, donc ne remplissent pas
  l'entrée 4. L'entrée 4 doit porter l'empreinte du texte relu (`54b70722…`), celle de ce rapport (compagnon `.sha256`),
  puis `graine_1 = …`, `graine_2 = …`, `entropie_analyse = …`, nus, chacun sur sa ligne, **seule occurrence** de chaque nom
  hors accents graves dans le texte (CE4-12).

---

## Corrections

### Majeures

**CE4-01 — majeure — La règle « panne extérieure » coupe des paires sur le bruit des petits comptes ; deux coupures
suffisent à rendre H-G1 « non concluant ».**

- Fichiers : `analyse_gradient.py` l. 116-144 (`taux_pannes`, `ecart_pannes` : taux par source sur les seules recherches de
  la génération lue, sans effectif minimal) et l. 187-189 (coupure dès que l'écart dépasse 0,10) ; texte l. 138-141
  (Métrique, point 4), l. 244, l. 314 ; règle d'un quart l. 243-244.
- Défaut : à la génération lue, chaque bras fait au plus 10 recherches, réparties entre sources ; un seul
  `ECHEC_RECHERCHE` sur 2 ou 3 recherches d'une source fait 33 à 50 points d'écart. OpenAlex répondait 429 depuis
  l'adresse partagée (texte l. 282-284). La règle ne mesure alors plus une panne propre à un bras mais le hasard des
  petits comptes, et deux paires coupées sur six invalident la lecture. Rien ne biaise le signe ; c'est l'informativité de
  l'expérience qui est en jeu, par construction.
- Preuve rejouée (E8, `travail/sortie-e8-regle-des-pannes.txt`) : `ecart_pannes` rend 0,50 pour « 1 échec OpenAlex sur
  2 contre 0 sur 3 » (coupure) et 0,114 pour « 1 `ECHEC_API` sur 8 appels contre 1 sur 90 » (coupure). Sous un taux
  d'échec **identique** p dans les deux bras, n recherches par source et par bras : n = 3, p = 0,05 → 24 % de paires
  coupées, P(≥ 2 sur 6) = 45 % ; n = 5, p = 0,05 → 37 %, 71 % ; n = 2, p = 0,10 → 32 %, 63 % ; n = 10, p = 0,05 → 11 %, 14 %.
- Correction (code, nouveau commit, essai sain et artefact) : ne comparer une source (ou les appels) que si chaque bras y
  a un effectif minimal (par exemple ≥ 10 tentatives) **et** couper seulement si l'écart dépasse 10 points **et** la
  différence des échecs atteint un compte fixé maintenant (par exemple ≥ 3), ou un test exact gelé (Fisher, α fixé) ;
  rejouer E8 et rapporter dans « Seuil » le taux de coupure sous taux identiques ; garder la coupure sur HTTP 402.

**CE4-02 — majeure — Le bras B sans réponse : la couverture coupe les paires où le retrait du service empêche de
répondre, les absences partielles comptent dans le sens prédit, et rien ne le dit.**

- Fichiers : texte l. 121-125 (couverture), l. 115-116 (H-G0 : A seulement), l. 134-147 (liste des différences),
  l. 197-205 (B : 160 appels, 20 USD par génération, `entrainer` et `predire` non servis) ; `analyse_gradient.py`
  l. 183-186 ; `serveur.py` l. 125-132 (`entrainer` → `INDISPONIBLE`, sans `identifiant`) ; `contrat.py` l. 139 (§ 5 bis :
  la génération 0 est celle « que le bras témoin relance à l'identique ») ; message n° 22 § 3 de « conv-audit » (« le bras
  B … doit pouvoir répondre par texte à chaque tâche au moins une fois : sinon H-G1 est confondue par « B n'a pas les
  moyens de répondre » »).
- Défaut : (a) la génération 0 de B est un organisme conçu en A avec des sondes ; relancé sans service, il reçoit
  `INDISPONIBLE` là où il attend un modèle ; s'il n'a pas de repli, il ne répond pas, ne laisse pas de successeur, est
  relancé une fois puis s'arrête : la paire est lue à une génération où B n'a rien répondu, et coupée par la couverture.
  Ce sont exactement les paires où le service compte le plus ; deux telles coupures font « non concluant ». (b) B paie
  chaque réponse (120 tâches mêlées, test et test final) sur 160 appels et 20 USD, A peut répondre par `predire` ; entre
  80 et 100 % de couverture, les tâches que B n'a pas pu payer comptent comme erreurs (règle du juge) : cette part de Δ va
  dans le sens prédit et mesure le budget autant que l'exactitude. (c) Le contrat dit à l'organisme que le bras témoin le
  relance « à l'identique » : c'est inexact pour B. Rien de (a) à (c) n'est dans « Ce qui reste différent », ni rapporté.
- Preuve : déduite du code et du texte (aucune course réelle) ; le chemin `INDISPONIBLE` est celui du serveur ; le compte
  « 120 tâches pour 160 appels » vient du contexte (`taches_test` = test + test final, `boucle.py` l. 557).
- Correction (texte ; aucune règle gelée changée) : (1) ajouter à « Ce qui reste différent » : (7) B paie chaque réponse,
  A peut répondre par ses sondes ; les absences de B entre 80 et 100 % de couverture comptent comme erreurs, dans le sens
  prédit ; (8) sous 80 %, la paire est coupée, ce qui peut rendre H-G1 non concluante pour une cause liée au traitement —
  le dire dans la « Limite dite avant la course » ; (2) rapport gelé, descriptif : par paire et par bras, couverture par
  famille, cause des absences (statuts `INDISPONIBLE`, `PLAFOND` d'appels ou de dollars, plantage), et Δ secondaire sur les
  seules tâches répondues par les deux bras (sans seuil, sans verdict) ; (3) dire l'inexactitude du contrat § 5 bis ; s'il
  faut l'écrire à l'organisme (« la génération 0 sera aussi relancée sans le service d'entraînement ») est une décision
  de Lazar (« ne lui suggère rien ») ; à défaut, la consigner comme limite.

**CE4-03 — majeure — La garde de disjonction du vivier ne mesure qu'un sens et ne voit pas les textes sans lettres
latines ; le vivier et ses vérités restent lisibles en génération notée, dans les deux bras.**

- Fichiers : `vivier.py` l. 70-83 (`recoupement_max` : part des fenêtres **du texte de la banque** retrouvées dans
  l'item), l. 127 (clé de doublon sur le texte normalisé), l. 133-141 (seuils 0,80 et 0,50) ; `garde_fuite.py` l. 25-32
  (`normaliser` ne garde que `[0-9a-zà-ÿ]` : tout mot cyrillique, grec, chinois, arabe… disparaît) ; `boucle.py` l. 566-582, l. 595
  et `bac_a_sable.preparer` (le contexte, vivier compris, est écrit dans `contexte.json` du dossier de travail, archivé,
  puis recopié dans la vue `cNNN/travail/`) ; texte l. 94-101 (« servi … pendant la conception »), l. 145-146 (6),
  l. 285-296 (point 10 : « un item à plus de 50 % d'un texte de test est servi et compté », « doublons internes comptés »,
  « aucune génération notée ne le reçoit »), l. 297-301.
- Défaut : (a) un item contenu tout entier dans un texte de test (préfixe, extrait, version tronquée) recoupe moins de
  50 % des fenêtres du texte de test : il est servi, et pas même compté « proche » ; (b) un texte sans lettres latines n'a
  aucune fenêtre : une copie exacte d'un texte de test russe ou chinois est servie avec sa vérité ; tous les items non
  latins ont la même clé de doublon (texte vide) : le premier est gardé, les autres comptés « doublons internes » à tort ;
  la garde de la moisson (CE3-04), qui partage `normaliser`, laisse passer une requête qui recopie un texte de test non
  latin ; (c) le vivier, avec ses vérités, est dans `cNNN/travail/contexte.json` de la vue : toutes les générations notées
  des deux bras peuvent le lire (B par l'import). Une quasi-copie d'un item de test que la garde laisse passer est donc
  exploitable au test (par recherche du plus proche voisin), dans les deux bras : pas de biais de Δ, mais une famille qui
  peut saturer et un audit déclenché par une fuite que la garde prétend fermer. La disjonction par identifiant de source
  (script de Lazar, vérifiée par « conv-audit ») ferme les copies d'un même item, pas les items proches.
- Preuves rejouées : E1 (`travail/sortie-e1-vivier-garde.txt`) — préfixe de 90 mots d'un texte de test de 200 mots :
  recoupement 0,43, servi, `servis_proches_test` = 0 ; copie exacte d'un texte de test russe : servie (`cv-0002`) ;
  copie d'un texte de test chinois et texte russe distinct : comptés « doublons internes » (2) ; requête qui recopie le
  texte de test russe : `recoupement` = `None`. E2 (`travail/sortie-e2-appariement-vivier.txt`) — en simulation, les
  5 items du vivier avec leur vérité sont lisibles dans la vue de g000, g001 et g002, en A **et** en B.
- Correction : (1) code : recoupement dans les deux sens (part des fenêtres de l'item dans un texte de test, et part des
  fenêtres du texte de test dans l'item) ; écarter si l'une ≥ 0,80, compter « proche » si l'une ≥ 0,50 ; normalisation
  Unicode (lettres et chiffres de toute écriture, `str.isalnum`), fenêtres de caractères pour les textes sans espaces ;
  clé de doublon sur le texte entier ; essais sain et artefact (préfixe, copie cyrillique, deux textes cyrilliques
  distincts) ; la même normalisation pour la garde de la moisson ; **ou**, sans code : avant le scellement, « conv-audit »
  (qui tient le fichier secret et le vivier) fait tourner `charger_vivier` sur le vrai fichier et un recoupement dans les
  deux sens, compte les items et les textes de la banque à moins de 8 mots latins, et transmet ces comptes, scellés, avec
  `<<VIVIER_MESSAGE>>` ; tout item à ≥ 0,50 dans un sens est retiré du fichier par le script de Lazar ; (2) texte : dire
  que le vivier et ses vérités restent lisibles par la vue en génération notée, dans les deux bras ; que la garde de fuite
  ne voit pas les textes sans lettres latines (s'il y en a dans la banque) ; corriger « à plus de 50 % » (le code dit
  ≥ 0,50) ; (3) mineur : les identifiants `cv-NNNN` suivent l'ordre du fichier ; si le script de Lazar groupe les items par
  catégorie, l'ordre des identifiants trahit les groupes : les numéroter après un tirage par une graine fixée, ou le dire.

**CE4-04 — majeure — La répétition ne peut pas vérifier ce que le point 8 lui fait vérifier ; Fable et le chemin du bras B
n'y sont pas exercés.**

- Fichiers : texte l. 257-269 (« seuls ses statuts sont lus, par l'extrait mécanique … : amorçage, rondes, exécution,
  appels conformes, entraînements, moisson, vivier servi, isolation ») ; `extrait_mecanique.py` l. 37-41 (`CHAMPS_RESUME` :
  `n_recherches`, `n_entrainements`, `n_telechargements`, des compteurs) et l. 158-169 (`fichiers_travail` écarte `noyau/`
  et `corpus/`) ; `boucle.py` : aucun événement par recherche, téléchargement ou entraînement (liste des `_evenement`) ;
  lanceur l. 131-136 (répétition : Opus et Argon seulement ; aucune course B).
- Défaut : (a) les statuts des entraînements (`journal-entrainements.jsonl` : `OK`, `REFUSE`, `ECHEC_ENTRAINEMENT`,
  `DELAI_DEPASSE`), des recherches (`ECHEC_RECHERCHE`, par source) et des téléchargements (`corpus/index.jsonl`) ne sont
  dans aucun champ de l'extrait ; un `ECHEC_RECHERCHE` consomme une recherche, donc « n_recherches = 2 » se lit pareil que
  la moisson marche ou non (par exemple un certificat du mandataire de sortie absent pour `urllib`, que l'appel de contrôle
  d'Anthropic ne prouve pas). Un entraîneur qui échoue en réel sur l'hôte rendrait A semblable à B : H-G1 « réfutée » par
  un défaut mécanique, que H-G0 ne signalerait qu'après coup ; (b) l'amorçage de Fable sous le contrat v3 (§ 7 compris)
  n'est exercé nulle part avant A_1 et A_2 : un refus ou un amorçage invalide de Fable dans les deux répliques coupe deux
  paires (non concluant) ; Opus a refusé une question abstraite le même soir (R-379) ; (c) le chemin réel de B (`--depuis`
  en réel, import des rondes sous root, parité Brave, `entrainer` → `INDISPONIBLE`) ne tourne pour la première fois qu'en
  course décisive.
- Preuve : lecture du code ; en E2, l'extrait de B ne porte que les compteurs.
- Correction : (1) code : l'extrait mécanique ajoute, par génération et par ronde, les comptes par statut des
  entraînements, des recherches (par source) et des téléchargements, lus aux journaux de l'archive (statut et source
  seulement, liste close), essai sain et artefact ; (2) texte : la répétition est réussie si, pour chaque espèce, l'amorçage
  est `ORGANISME_VALIDE`, et si les entraînements demandés et les recherches rendent au moins un `OK` — sinon les courses
  décisives ne partent pas (ligne de la liste d'arrêt) ; (3) ajouter Fable à la répétition (plafond porté à ≈ 30 USD :
  + 3,4 d'amorçage au pire, + 2 × 2 de rondes, + 3 de génération) ; (4) ajouter une course `repetition-B` (`--depuis
  repetition --entrainements-max 0`, une génération, ≈ 6 USD), statuts et `n_reponses_test` lus à l'extrait : elle exerce
  le chemin réel de B et dit d'avance si un organisme conçu avec le service répond sans lui (CE4-02). Exclue de toute
  analyse, comme la répétition.

### Mineures

**CE4-05 — mineure — « Historique et vue de g000 identiques dans les deux bras » est inexact ; d'autres différences
entre bras ne sont pas nommées.**
- Fichiers : texte l. 128-133 ; `archive.py` l. 210-216 (`historique` ajoute `importee: true` aux rondes importées),
  l. 183 ; `boucle.py` l. 569 (`rondes_conception_max` du contexte : 4 en A, 0 en B), l. 324 (indice de lignée calculé sur
  les lignées présentes) ; `cli._imposes_et_especes` (en B, toutes les lignées entrent comme imposées : `impose: true` dans
  l'index et dans `resume.json` de la vue) ; essai cité, qui ne compare que (phase, génération, statut, successeur) et les
  noms de premier niveau de la vue.
- Preuve (E2) : vue de g000 identique en chemins et en contenus (empreintes de chaque fichier) ; historique différent sur
  chaque ronde (`importee` : absent en A, `true` en B) ; `rondes_conception_max` 3 en A, 0 en B. Déduit du code, non
  rejoué : si une lignée de A n'a pas de g000 (invalidée en conception), B n'en a que deux, l'indice des autres change et
  leurs graines d'ordre et d'organisme diffèrent entre bras (contre l. 146-147 « les graines d'ordre des tâches sont les
  mêmes »).
- Correction : texte — « mêmes rondes, même vue (chemins et contenus) ; l'historique de B marque les rondes importées ;
  `rondes_conception_max` vaut 0 en B ; les lignées de B sont marquées imposées » dans « Ce qui reste différent » ;
  code, au choix (signe de bras supplémentaires pour l'organisme, qui le sait déjà par `traits.disponibles`) : servir à B
  le même `rondes_conception_max`, retirer `importee` de l'historique servi, tirer l'indice de lignée de la liste
  d'amorçage du manifeste d'origine.

**CE4-06 — mineure — Extrait mécanique de B et dépense : les rondes importées passent pour des rondes de B ; la dépense
« lue au journal des appels » compterait deux fois la conception.**
- Fichiers : `extrait_mecanique.py` l. 183-203 (générations lues dans `resume.json`, qui pour une ronde importée est celui
  de A, sans `importee`) ; lanceur l. 203-208 (lignes affichées au journal) ; texte l. 302-303 (point 12).
- Preuve (E2) : l'extrait de B liste `c001` à `c003` avec `importee: None`, les coûts et appels de A ; dépense du rapport
  de B 0,1677 USD, somme des journaux d'appels de l'archive de B 0,2721 USD.
- Correction : l'extrait marque les rondes importées d'après l'index (`importee`) et les sort des sommes ; point 12 : la
  dépense est `depense_totale_usd` du rapport du noyau (ou les journaux des seules générations non importées). Dire aussi
  que l'extrait est « sans clé de score » : les valeurs écrites par l'organisme (noms de fichiers, `erreurs`, déclaration
  de fin de conception) ne sont pas filtrées et peuvent porter un score de développement qu'il a reçu.

**CE4-07 — mineure — Lanceur : gardes sans artefact dans ses essais, ou fragiles.**
- (a) Hôte (lanceur l. 49, 61-63) : root, `unshare -n`, espaces de noms, `fs.protected_hardlinks` — aucun artefact dans
  `essais_lanceur_etape1_v2.sh` (R5 ; la liste d'arrêt, l. 341, renvoie à l'essai du noyau, qui ne couvre ni les espaces de
  noms ni `protected_hardlinks`, et le noyau tourne sans espaces de noms s'ils manquent, `bac_a_sable.py` l. 219). Rejoué
  (E6) : `protected_hardlinks` = 0 (fichier lié par-dessus dans un espace de noms de montage privé) → « doit valoir 1 »,
  code 2 ; `unshare` refusé → « unshare -n refusé », code 2 ; identifiant 1000 (espace de noms d'utilisateur) → « le noyau
  exige root », code 2 : les gardes sont justes ; les verser aux essais.
- (b) « Arbre propre » (l. 78, `--untracked-files=no`) ignore un fichier non suivi dans le code : rejoué (E6, L1), un
  `essaim_m3/noyau/non_suivi_essai.py` passe ; l'empreinte d'arbre citée (`7160461a…`) n'est vérifiée qu'après coup, au
  manifeste. Correction : `git status --porcelain` sans cette option, ou comparer `empreinte_arbre` à la valeur citée.
- (c) `vivier_chemin` absent du commit du vivier (l. 90-91, sous `set -e`) : sortie en code 128, sans note ni code 2
  (E6, L5) — sûr, mais contraire à l'en-tête (l. 13).
- (d) Parité de Brave (l. 151-152) lue sur la dernière ligne « A<r> : clés » du journal, qu'un `--controles A<r>` lancé
  après la course écrit avant de s'arrêter (« existe déjà ») : B refusé à tort, ou accepté à tort (E6, L6a-c ; le noyau
  rattrape l'acceptation à tort par `cle_brave_presente` du manifeste de A). Correction : lire le manifeste de A.
- (e) Clé Gemini : aucune parité entre A_r et B_r (clé n° 2 pour A, n° 1 pour B : accepté, E6, L7) ; deux comptes
  différents = conditions extérieures différentes. Correction : exiger le même nom de clé que A, comme pour Brave.
- (f) A_1 et A_2 lancés ensemble sur un dossier des courses neuf : l'extraction des entrées (l. 84-93) n'est pas sous
  verrou ; rejoué six fois (E9) : trois lancements doubles sur six échouent (`rm` ou `tar`, codes 1 et 2, sans note).
  Correction : verrou d'extraction, ou entrées préparées par un `--controles` préalable — à écrire au point 3.
- (g) `<course>.fin.json` « écrit … quelle qu'elle soit » (l. 24-26) : aucun pour un arrêt avant la course (le piège est
  posé l. 193) ; `<course>.erreurs.txt` n'est pas scellé (le n° 22 de « session-depot », PG2-01, l'annonçait).
- Tout changement du lanceur change son empreinte citée (l. 38-41).

**CE4-08 — mineure — Hôte : le même hôte pour A_r et B_r n'est pas exigé ; une course de plus de 2 h n'est pas éprouvée sur
l'option recommandée.**
- Fichiers : texte l. 216-222 ; P-029 ; message n° 20 de « conv-audit », RE-02 (« une commande de fond est tenue 2 h au
  plus, et le conteneur est repris quand la session est inactive »).
- Défaut : (a) rien n'interdit de faire tourner A_r et B_r sur deux hôtes (cœurs, réseau, mandataire différents) ; (b) sur
  l'option (a), A_r dure jusqu'à 10,5 h, la répétition au plus ≈ 1,5 h (2 lignées × 3 passes × 900 s) : la survie d'une
  course détachée au-delà de 2 h et pendant une session inactive n'est pas éprouvée avant la première course décisive ; un
  arrêt pendant la conception de A coupe les trois paires de la réplique (non concluant), après la dépense.
- Correction : les quatre courses (et la répétition) sur le même hôte, consigné (le journal du lanceur porte noyau et
  cœurs) ; un changement d'hôte entre A_r et B_r = écart, paires de la réplique coupées ; avant les courses décisives,
  une épreuve sans dépense (processus détaché surveillé par PID, plus de 2 h, session inactive) sur l'hôte retenu,
  consignée. La règle d'arrêt elle-même est suffisante (point 6).

**CE4-09 — mineure — Clé Gemini et GO : provenance et état réel.**
- Fichiers : texte l. 207-211 ; GO-2026-10-24-05 (« clés selon GO-2026-10-24-04 (Anthropic) et `GEMINI_API_KEY` ») ;
  GO-2026-10-24-07 (périmètre : préparatifs, appels de contrôle, répétition ; pas les courses décisives) ; R-370 (clé n° 2
  « non visible dans le conteneur de « session-depot » ») ; R-379 (crédit de `GEMINI_API_KEY` épuisé).
- Défaut : le texte fonde l'emploi de `GEMINI_API_KEY_2` dans les courses décisives sur GO-07, qui ne les couvre pas ; et,
  sur l'hôte recommandé, la clé n° 2 n'est pas visible et la n° 1 n'a plus de crédit : l'appel de contrôle d'Argon
  échouera et aucune course ne partira (sûr, mais le plan n'est pas exécutable tel quel aujourd'hui). Les appels de
  contrôle sont imputés à GO-05 par le lanceur (l. 171-175), à GO-07 par le registre.
- Correction : citer R-370 (Lazar, 22:37) comme source de la clé n° 2 et compléter la ligne de GO-05 au registre
  (consignation) ou demander à Lazar une confirmation d'une ligne ; dire l'état et ce qui débloque (clé n° 2 visible sur
  l'hôte, ou crédit rechargé) ; dire l'imputation des appels de contrôle.

**CE4-10 — mineure — Lecture : procédures non codées, réserve inexacte, mesures mal bornées.**
- (a) « Défaut touchant des paires » et « vue de l'archive contenant … » (l. 314, 328, 370) : couper ces paires puis
  recalculer la règle d'un quart n'est codé nulle part (`paires_h_g1` ne prend pas de paires exclues ; `lecture_h_g1`
  attend un `invalide` recalculé par l'appelant). Correction : un paramètre `exclues` gelé, ou la procédure écrite pas à pas.
- (b) Avec `apres_audit = "defaut_paires"`, la réserve rendue est « audit de symétrie sans défaut trouvé »
  (`analyse_gradient.py` l. 245) : faux ; une réserve propre à chaque état.
- (c) `recoupements_fuite` (l. 147-155, 182) ne compte que les générations notées communes ; le point 11 (« tout
  recoupement déclenche l'audit ») et H-C laissent croire que les refus des rondes de conception (possibles : gabarits
  partagés entre vivier et test) déclenchent aussi. Le dire.
- (d) La vérification humaine `find … -name modele.npz -o -name journal-entrainements.jsonl` (l. 370) frappe aussi un
  fichier de l'organisme portant ce nom : comparer aux empreintes des fichiers du noyau de la même génération.
- (e) « Score par famille rapporté » (n° 21 § 2 de « conv-audit » : le « premier résultat » que Lazar veut montrer) n'est
  pas gelé : geler un rapport descriptif des scores et de Δ pour **les deux** familles, quel qu'en soit le sens (R4), sans
  verdict par famille.

**CE4-11 — mineure — Puissance : la « réfutation » à tort à l'effet prédit n'est pas dite.**
- `puissance-v2.json` : à l'effet +0,10, « réfuté » 0,5 % (σ = 0), **4,5 %** (σ = 0,25), **9,2 %** (σ = 0,5). Le texte
  (l. 165, 177-179) ne vise que le « confirmé » à tort sous effet nul (≤ 2,5 %, tenu). Avec deux répliques, l'intervalle
  ne capte pas la dérive de réplique, dans les deux sens. Correction : le dire dans « Seuil » (symétrie, R4) ; aucun seuil
  changé.

### Forme

**CE4-12 — forme — Lecture littérale du lanceur.** `litteral` (l. 75) prend la première occurrence : un exemple
« graine_1 = 7 » écrit hors accents graves plus haut serait lu (E5). Écrire au point 5 « seule occurrence de chaque nom »
ou faire refuser le lanceur sur plusieurs occurrences.

**CE4-13 — forme — Menues inexactitudes.**
- Le manifeste dit toujours `"recherche": "arxiv"` (`boucle.py` l. 269) à côté de `sources_moisson` (reste de CE3-18).
- R6 : `donnees/collisionneur-reecriture-v1` cité par son commit sans l'empreinte de `EMPREINTES-v1.txt` (`5f2e6e51…`,
  R-379) ; GO-2026-10-24-07 employé (l. 210) mais absent de la liste des décisions (l. 69-71).
- Clés passées dans les arguments de `env` (lanceur l. 164-168) : lisibles un instant dans `/proc` de l'hôte (pas par
  les organismes, qui ont leur propre espace de processus) ; à dire, ou passer par l'environnement hérité.

---

## Suivi de CE3-01 à CE3-18 (et RE-01 à RE-05)

| remarque | état | vérification |
|---|---|---|
| CE3-01 mémoire de conception servie au seul bras A | **traitée** | `Archive.importer_conception` ; E2 : vue de g000 identique en chemins et contenus, rondes hors scores, hors dépense, hors `generations_valides` ; reste : historique marqué `importee`, `rondes_conception_max` 0 en B (CE4-05) |
| CE3-02 rondes comptées comme générations notées | **traitée** | `generations_valides` l. 85 (phase, importée, invalide) ; `reponses_finales` lève une erreur ; E2 : `[0, 1, 2]` avec trois rondes ; essais passés |
| CE3-03 audit sur absence de réponses ; pas de sortie | **traitée** | couverture ≥ 80 %, seuil bas sur les tâches répondues (`exactitude_repondue_par_famille`), `apres_audit` ; restes : réserve de `defaut_paires`, coupure non codée (CE4-10) ; la couverture ouvre CE4-02 |
| CE3-04 recherche de provenance | **traitée** | `garde_fuite.py`, recherche refusée sans consommer, document en quarantaine, comptage ; trois essais passés ; reste : écritures non latines (CE4-03), conception non comptée (CE4-10 c) |
| CE3-05 conditions extérieures | **en partie** | HTTP 402 (essai), manifeste des sources et de Brave, refus de B par le noyau, parité Brave au lanceur : réels ; la règle des pannes coupe sur le bruit (CE4-01) ; parité Brave fragile, aucune parité Gemini (CE4-07 d, e) |
| CE3-06 vues hors de la lignée et de la course | **traitée** | vues 0750 au groupe de la lignée, `archive_vue/` 0711, `--decalage-uid` 100 à 500, dossier des courses 0700 (essais du noyau en root et du lanceur rejoués) ; rondes importées en 0555 mais sous une vue de lignée 0750 |
| CE3-07 dossiers du noyau renommables | **traitée** | `<travail>.noyau` et `<travail>.corpus` hors du dossier, noms réservés, `ANOMALIE_NOYAU` ; essais passés ; texte l. 370 |
| CE3-08 `--strip-components=3` | **traitée** | lanceur l. 88 ; essai rejoué (traits sous `entrees/traits/etape1-v1`) |
| CE3-09 lanceur sans empreinte, en-tête, graine absente | **traitée** | empreinte citée et concordante ; en-tête juste (v4, répétition à 3 USD) ; graine absente : code 2 avec note (rejoué) ; addendum dit |
| CE3-10 lignées imposées en conception | **sans objet** | plus de lignées imposées (R-370) ; le lanceur ne passe pas `--organisme-impose` |
| CE3-11 temps, interruption, moisson, contention | **traitée** | durées au pire justes ; règle d'arrêt de l'hôte ; `temps_pire_cas` (1 730, 1 130, 615 s recalculés) appliqué aux générations et aux rondes ; cœurs au journal ; reste : survie au-delà de 2 h (CE4-08) |
| CE3-12 garde de plafond pendant la conception | **traitée** | `_doit_arreter` dans les deux boucles, raison « aucune lignée active » ; essai passé |
| CE3-13 répétition qui lit les scores ; Gemini | **en partie** | sortie 0600 scellée, extrait sans clé de score, Opus et Argon contrôlés ; mais l'extrait n'a pas les statuts d'entraînement et de moisson, Fable et B non exercés (CE4-04) ; `erreurs.txt` non scellé (CE4-07 g) |
| CE3-14 sections contradictoires | **traitée** | point 9 : ce qui prime, ce qui vaut, phrase sur l'injection nuancée |
| CE3-15 Brave, requêtes, consignation | **traitée** | R-363 cité ; 210 + 210 + 90 + 90 = 600, répétition 12 (recalculé) ; engagement exigé (essai `reel-sans-engagement` rejoué) |
| CE3-16 graines : entrée et format | **traitée** | entrée 4, format littéral ; lecture du lanceur rejouée (E5) |
| CE3-17 graines ronde k = génération k | **traitée** | `DECALAGE_CONCEPTION` ; E2 : ronde k ≠ génération k pour `ordre_train`, `ordre_test`, `organisme`, k = 1 et 2 |
| CE3-18 menues inexactitudes | **en partie** | alignement retiré, six artefacts, 429 sans pièce, 20:42, condition mécanique, borne déduite, redirections, `fin_conception.json` borné : faits ; `"recherche": "arxiv"` reste au manifeste (CE4-13) |
| RE-01 à RE-05 | **traitées** | RE-01 = CE3-01 ; RE-02 point 3 (reste CE4-08) ; RE-03 H-G2 et N-026 ; RE-04 Métrique (4) ; RE-05 en-tête du lanceur |

Bilan : 14 traitées, 3 en partie, 1 sans objet.

---

## Réponses aux sept points

**1. Le traitement de CE3-01 à CE3-18 et RE-01 à RE-05 est-il réel ? Les essais prouvent-ils ce qu'ils disent ?** Oui
pour l'essentiel (tableau ci-dessus), dans le texte, dans le code au commit cité et dans le lanceur. La suite du noyau
tourne : 109 réussis, 4 échecs, tous par absence des fichiers de données retirés des pièces (banque réelle et traces :
`FileNotFoundError`), 3 désélectionnés — cohérent avec « 113 passent ». Les essais cités prouvent leur énoncé, avec deux
limites : `test_bras_apparie_voit_les_rondes_de_conception_de_l_origine` ne compare qu'une projection de l'historique et
les noms de la vue (le texte dit « identiques » : CE4-05) ; les gardes d'hôte du lanceur n'ont pas d'artefact dans ses
essais (je les ai rejouées : justes, CE4-07 a).

**2. Le vivier de conception.** Servi pendant la conception seulement (contexte, ordre propre, identifiants opaques,
`id_source` et catégorie jamais servis, textes bornés comme la banque) : vrai (essai et E2). Refus : avec `--depuis`, sans
phase de conception, compagnon absent ou faux, lien, JSON illisible, item malformé : vrais (essais). Appariement A/B : B
n'a pas de vivier mais en hérite tout le contenu par l'import (les contextes des rondes, vérités comprises, sont dans la
vue) : symétrique, à condition de le dire. La garde par le contenu est juste dans son sens (contenance du texte de la
banque dans l'item) mais ni suffisante ni bien décrite : un sens seulement, écritures non latines invisibles, doublons
faux (CE4-03). Le seuil de 80 % (au lieu d'une fenêtre) est bien motivé par les gabarits partagés ; les items à 50-80 % sont
servis et comptés ; ceux qui ne le sont qu'en sens inverse ne sont pas comptés. Le fichier n'existe pas encore : sa forme
(clé `exemples`, `input`, `verite`) n'est vérifiée que par le noyau au départ de la répétition, pas par `--controles` ;
d'où la recommandation de faire tourner `charger_vivier` sur le vrai fichier avant le scellement.

**3. Bornes « économes ».** Arithmétique juste : A_r = 3 × 12 + 3 × 4 × 12 + 3 × 3 × 20 = 36 + 144 + 180 = 360 ; B_r =
180 + 10 = 190 ; total 1 100 USD au pire, plus 25 de répétition. Pire cas d'amorçage au maximum du modèle avec 60 000
caractères : Fable 0,2 + 3,2 = 3,4 ; Opus 0,08 + 1,28 ≈ 1,4 ; Argon 0,2 + 1,6 = 1,8 (prix du collisionneur) ; même avec une
relance au plafond de relance du collisionneur (le noyau n'en fait pas : `Appelant.appeler` réserve et appelle une
fois à `max`, `appels.py` l. 146-165), 19,3 < 36. Garde de temps (`temps_pire_cas`) : 10 × 60 + 10 × 25 + 4 × (25 + 120) + 300 =
1 730 ≤ 1 800 ; B 1 130 ; répétition 2 × 60 + 2 × 25 + 145 + 300 = 615 ≤ 900 ; la garde vaut aussi pour les rondes.
Durées au pire 10,5 h et 4,5 h ; requêtes 600 et 12. Le lanceur passe **exactement** les options du texte pour A_r, B_r et
la répétition (sortie des essais rejoués) et l'analyseur du noyau les accepte (E7 : arrêt voulu au refus des clés,
code 4). Réserve : 160 appels et 20 USD laissent à B tout juste un appel par tâche (120 tâches) plus le successeur
(CE4-02).

**4. Le lanceur v2.** Ordre juste : root et dossier 0700 (§ 0), hôte (§ 1), préenregistrement scellé et commit (§ 2),
code (§ 3), entrées (§ 4), engagement (§ 5), garde de calcul (§ 6), clés (§ 7), sortie et verrou (§ 8), graines et B
(§ 9), puis seulement l'appel de contrôle (§ 11, premier appel payant) et la course ; `--controles` sort avant tout appel.
Clés jamais écrites ni affichées (seuls les noms au journal ; valeurs passées au seul `env` du noyau ; voir CE4-13).
Verrou par course tenu par le descripteur 9 jusqu'à la fin du noyau ; B exige le verrou de A libre et une g000 archivée
(la recherche de `"generation": 0` ne peut pas tomber sur une ronde : elles commencent à 1). Sortie du noyau en 0600,
scellée à la fin, jamais affichée ; seul l'extrait mécanique est affiché, réduit à huit champs sans score. Valeurs
littérales lues justement (E5). Les essais couvrent dossier, clé Gemini, sortie existante, verrou, B avant et pendant A,
parité Brave, préenregistrement non scellé ou sans commit, graine absente, vivier faux, traits altérés, autre commit, GO
refusé, engagement absent (22 sur 22, rejoués) ; ils ne couvrent pas l'hôte, l'arbre modifié, la banque différente, la
clé Anthropic absente, ni l'extraction concurrente (CE4-07).

**5. Analyse et lecture de H-G1.** La table du texte est `lecture_h_g1`, ligne à ligne (l'ordre « audit en attente » /
« défaut du noyau » diffère mais les deux sont exclusifs). Le tirage à trois niveaux est celui du texte (répliques, paires
dans la réplique, tâches par strate, mêmes tâches pour les deux bras d'une paire, 2 000 tirages, `SeedSequence`). La
condition « Δ ≥ +0,10 dans chaque réplique » est codée ; avec au plus une paire coupée sur six, les deux répliques sont
toujours présentes. Couverture et recoupements : codés et essayés ; pannes : codées mais défectueuses (CE4-01).
Déclencheurs : seuils 0,95, 0,30, 0,40, recoupements ; sortie gelée : trois états, avec les restes de CE4-10. Puissance
rejouée : `puissance-v2.json` refait à l'identique (même empreinte `50a1c248…`, E10) ; la table du texte en est la
lecture exacte.

**6. L'hôte non décidé.** Le texte reste un préenregistrement complet au sens de R1 : hypothèse, prédiction, métrique,
seuil, plan, critères gelés et liste d'arrêt ne dépendent pas de l'hôte ; ce qui doit tenir sur tout hôte est une garde
du lanceur ou du noyau ; l'hôte effectif est consigné avant la répétition ; le défaut de P-029 tombe le 26 octobre vers
23:05 UTC. La règle d'arrêt de l'hôte (course arrêtée, consignée, lue à la dernière génération valide commune ou coupée,
aucune relance) suffit à la lecture et ne favorise aucun signe. Il manque : le même hôte pour A_r et B_r, et une épreuve
de durée sur l'option (a) (CE4-08).

**7. Le reste.** R1 : huit sections ; prédiction chiffrée et signée ; marqueurs définis ; addendum exigé pour le script
des témoins avant la lecture. R2 : ce rapport ; revérification du code sur `5e6876d` faite à part. R3 : la prédiction est
positive (R-344 exige un run décisif) ; la règle est symétrique ; CE4-02 (b) pousse un peu vers le signe prédit, à dire.
R4 : audit dans les deux sens ; asymétries de bras nommées sauf CE4-02 et CE4-05 ; erreurs de lecture dans les deux sens
(CE4-11). R5 : gardes essayées, sauf les gardes d'hôte du lanceur (CE4-07 a). R6 : empreintes complètes sauf CE4-13. R7 :
0,69 et 0,50 dits non audités ; puissance et annexe dites non opposables. R9 : graines par `SeedSequence`, E au
scellement, CE3-17 corrigée. R10, R12, R13 : tenus. Chiffres vérifiés : banque (80, 60, 60 ; 36 + 24 ; 18 + 18 ; 12 + 12),
traits (200 × 4 096, dix vues, 12 407 jetons au plus, aucune troncature, révision `0e9e39f…`, `revision_resolue` nul,
transformers 5.18.0), environnement (Python 3.13.17, numpy 2.4.6, anthropic 2.3.0, lus). Provenance des décisions de
Lazar : « économe » et retrait des lignées imposées (23:00) = n° 21 et R-370 ; garde CE3-04 = R-371 et R-375 (« ok oui ») ;
vivier « GO now » (00:05) = n° 28 § 2 et R-376 ; sonde d'hôte = R-377 ; collisionneur = R-379 ; P-029 ; GO-05 = R-355 ;
tout concorde, sauf la clé Gemini (CE4-09). Retrait des lignées imposées : réel (texte, lanceur) ; CE3-10 sans objet.
Refus d'Opus et crédit de Gemini : dans la liste d'arrêt (appel de contrôle, répétition) ; un refus ou un amorçage
invalide en course décisive n'est couvert que par les paires coupées (CE4-04 b).

---

## Ce que j'ai rejoué

Tout sous `env -i PATH=/usr/bin:/bin HOME=<travail>/home`, `python -B`, environnement `/opt/essaim-m3-venv-v1`, sur
une copie du code dans `travail/code` (et, pour le lanceur, un arbre de travail détaché au commit cité, `travail/code-git`,
tiré de `git clone --shared --no-checkout` du dépôt dans `travail/git-code`) ; les essais qui lancent des organismes
isolés dans un espace de noms de montage privé où `/var/tmp` est lié à `travail/vartmp` (vérifié : le vrai
`/var/tmp/essaim-m3` n'a pas bougé depuis 23:31 UTC, avant mon début). Root ; aucun processus laissé (vérifié pour les
utilisateurs 60000 à 61999) ; aucun appel à une interface de modèle ni à une source de moisson (essai réseau
désélectionné) ; aucune clé lue ni affichée (clés factices seulement) ; aucune écriture dans le dépôt (le clone partagé et
l'arbre de travail sont dans mon dossier) ; aucun script de la relève de Gemini exécuté. Les simulations E2 impriment des
« scores » de simulation (espèces simulées, banque simulée) : aucun résultat réel.

| essai | ce qu'il montre | sortie (`travail/`) | empreinte |
|---|---|---|---|
| suite du noyau au commit cité | 109 réussis ; 4 échecs, tous `FileNotFoundError` sur la banque ou les traces retirées des pièces ; 3 désélectionnés ; aucun essai sauté (les essais d'isolation ont tourné en root) | `sortie-pytest-ed3ce0e.txt` | `651b7c04…` |
| E1 | garde du vivier : préfixe d'un texte de test servi sans être compté ; copie cyrillique servie ; textes non latins comptés « doublons » ; requête cyrillique non refusée | `sortie-e1-vivier-garde.txt` | `66aacbf6…` |
| E2 | course A simulée (3 rondes, vivier) et B `--depuis A` : vue de g000 identique (chemins, contenus) ; historique marqué `importee` ; `rondes_conception_max` 3 contre 0 ; vivier lisible en g000-g002 dans les deux bras ; CE3-17 tenue ; extrait de B : rondes importées non marquées, dépense double | `sortie-e2-appariement-vivier.txt` | `6108cfaa…` |
| E3 | essais du lanceur rejoués : 22 sur 22 | `sortie-e3-essais-lanceur-rejoues.txt` | `b85636f0…` |
| E4 | validateur : marqueurs et entrée 4 seulement ; copie remplie sans problème | `sortie-e4-validateur.txt` | `53624348…` |
| E5 | lecture littérale du lanceur : vide sur la v4, juste sur une copie remplie ; refus sur accents graves ou point final ; première occurrence prise | `sortie-e5-litteral-lanceur.txt` | `d204b67c…` |
| E6 | lanceur : fichier non suivi accepté ; `protected_hardlinks` = 0, `unshare` refusé, non root : refus justes ; vivier absent du commit : code 128 sans note ; parité Brave trompée par un contrôle postérieur ; clé Gemini sans parité | `sortie-e6-lanceur-artefacts.txt` | `b9de8d73…` |
| E7 | les trois lignes d'options passent l'analyseur du noyau (arrêt au refus des clés, code 4) | `sortie-e7-options-analyseur.txt` | `2628d01e…` |
| E8 | règle des pannes sous taux d'échec identiques : coupures et P(≥ 2 sur 6) | `sortie-e8-regle-des-pannes.txt` | `24de10d8…` |
| E9 | A1 et A2 lancés ensemble sur un dossier neuf : 3 essais sur 6 en échec à l'extraction | `sortie-e9-course-simultanee-entrees.txt` | `0c272c40…` |
| E10 | puissance rejouée (`puissance_v2.py`, 9 cas) : fichier identique octet pour octet | `sortie-e10-puissance-rejouee.txt`, `puissance/puissance-v2-rejouee.json` | `b34d351e…`, `50a1c248…` |
| diff | diff `5e6876d..ed3ce0e` recalculé = pièce | `diff-rejoue-5e6876d-ed3ce0e.patch` | `6393edf0…` |

Empreintes complètes : `travail/EMPREINTES-travail-v1.txt`.

Organismes et scripts écrits par moi (simulation seulement) : `travail/exp/explorateur/organisme/` ; `travail/scripts/`
(`e1_vivier.py`, `e2_appariement.py`, `e5_litteral.sh`, `e6_lanceur_artefacts.sh`, `e7_options.py`, `e8_pannes.py`,
copie de `puissance_v2.py`) ; validateur et copies remplies : `travail/validateur/`.

## Ce que je n'ai pas pu vérifier

- Le fichier du vivier (il n'existe pas) : sa forme, ses comptes, la présence de quasi-copies ou de textes non latins.
- La banque réelle (fichiers retirés des pièces) : les quatre essais qui la lisent, la part de textes sans lettres latines
  dans le test, la référence de surface 0,69 / 0,50.
- La garde de calcul `.claude/hooks/garde_calcul.py` (hors des pièces ; exécutée seulement par le script d'essais) : son
  refus « hors période » n'est essayé nulle part.
- Les courses, espèces et moisson réelles : coûts, durées, débit, refus, comportement d'un organisme de A relancé sans
  service ; l'acceptation de l'en-tête d'espace de travail par le serveur.
- La borne de 2 h des commandes de fond et la reprise du conteneur en inactivité dans la session « session-depot » : je
  ne connais que celles de « conv-audit » (RE-02).
- Le rapport de revérification du code sur `5e6876d` (fait à part) ; je n'ai relu que le diff `5e6876d..ed3ce0e` et ce
  que les sept points demandaient du reste.
- La dérive des graines quand une lignée de A n'a pas de g000 (CE4-05) : déduite du code, non rejouée.
