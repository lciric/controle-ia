# Vérification courte du préenregistrement complémentaire des notations refaites du pilote de T0.5 — v1

Objet : la vérification courte prévue par le plan de lancement (préalable 3), après la contre-lecture R2 complète du texte, du code et de la chaîne (rapports versés sous `prereg/contre-lectures/T0.5-notations-v1-relecture-*`). Chaque tour est confié à des sous-agents neufs, qui n'ont écrit ni le texte, ni le code, ni les scripts, avec la liste explicite des fichiers à lire ; chaque tour relit le traitement du précédent. Les rapports sont recopiés mot pour mot (titres de section abaissés d'un niveau) ; leurs chemins de travail renvoient au bloc-notes de la session, non versé. Ce rapport est hors de la famille des rapports cités par le préenregistrement : le texte ne peut pas citer le rapport qui porte sur lui.

Objets relus (chemin, sha256) :
- tour 1 : candidat 2 (`brouillons/T0.5-pilote-notations-v1-candidat2.md`, `efa4b68ada13e50b473cde9fda37d8ec48115d710dee48d4f500cbc87fe618ce`) ; code, différentiel `a85904596fd7dcd500506750acfc9c17d5d26ca3` → `20da280bf59b8f320ef7454347a3a45c7ad1ec52` (suite : `brouillons/T0.5-notations-suite-20da280-v1.txt`, `cac5546f87f1c0d65fad39449e363dd4bc1f781a5c991e30b6b56de149a42ae3`) ; chaîne, brouillon 3 (`brouillons/T0.5-notations-chaine-v1-brouillon3/empreintes.sha256`, `a4f9648e53f9d27eff4c048fefb4227385afaf26bc660c940f541298229d1ed1`) ;
- tour 2 : candidat 3 (`brouillons/T0.5-pilote-notations-v1-candidat3.md`, `5df4f0829ab94ee22b604f94c2cd17b3f4e435d39424f7dafe64ff75905e0147`) ; code, différentiel `20da280` → `259cf5e9da5d96c921fad06122a519e59a14c5ea` (suite : `brouillons/T0.5-notations-suite-259cf5e-v1.txt`, `1fd7d5e188ee9fd472059837f2f3000c3099ce9ae565124cf31129facd49ad4d`) ; chaîne, brouillon 4 (`brouillons/T0.5-notations-chaine-v1-brouillon4/empreintes.sha256`, `1b997367704a9398da6030987cf55dada002060c4ca6ee2416987d4503ec4159`) ;
- tour 3 : candidat 4 (`brouillons/T0.5-pilote-notations-v1-candidat4.md`, `6d408c7899a9ee764b31cd49b5909058361c82987b8e05dc66aeedf2ce9bec04`) ; code, différentiel `259cf5e` → `c63d4f1c073f3b6146729dae0086cd7205cdfa57` (suite : `brouillons/T0.5-notations-suite-c63d4f1-v1.txt`, `d4a32162d8764e90cccd4fd427ae60866821d2d0ca35b886af86694b55d9ee3a`) ; chaîne, brouillon 5 (`brouillons/T0.5-notations-chaine-v1-brouillon5/empreintes.sha256`, `43ebeaa97fdc8986d38ed6541a4f8314dc2ad75a67d3995e9d0a79a433d265d7`).

## Tour 1

### Rapport — texte du candidat 2

**Verdict : à corriger.** Le candidat 2 (commit b9c4f7f) est presque prêt. Trois contradictions internes, de gravité majeure, touchent le relancement et la préséance des écarts déclarés. Neuf constats mineurs portent sur la transparence et la provenance des chiffres. Les empreintes, le code et les tests sont fidèles.

#### Constats

**1. Classement des pannes réseau contradictoire : un relancement dépend de la ligne qu'on lit (majeur)**
- **Lieu :** brouillons/T0.5-pilote-notations-v1-candidat2.md:126 et :137.
- **Constat :**
  - « Causes d'un arrêt » classe en cause d'infrastructure :
    - le réseau, « téléchargement du 8B et préchargement du 3B compris » ;
    - une erreur de la carte autre que de mémoire ;
    - un signal TERM après plus de 1 500 s de mise en place.
  - La phrase qui clôt la Liste d'arrêt, « Pendant le run », dit l'inverse : « Ces entrées n'ajoutent aucun classement : seul l'échec réseau du préchargement est une cause d'infrastructure ». Ces entrées comprennent pourtant le « chargement du 8B (téléchargement compris) » et le signal TERM.
  - L'enjeu est concret. Une panne réseau au téléchargement du 8B, dans les premières minutes, est le cas le plus probable d'un relancement tenable sous le plafond de 10,5 USD.
  - Autre cas réseau : le tokeniseur du 3B est téléchargé pendant le « contrôle du format » (`lancer_pilote_a.py:219`, `AutoTokenizer.from_pretrained`). La parenthèse de la ligne 126 ne le nomme pas.
- **Preuve :** les deux citations ci-dessus. Le code au commit 20da280 (`noter_pilote_a.py:236-249`) consigne ces pannes sous les étapes « chargement du juge 8B » et « contrôle du format ».
- **Correction :** fin de la ligne 137 → « Ces entrées n'ajoutent aucun classement : la cause se qualifie selon « Causes d'un arrêt » ». À la ligne 126, ajouter « tokeniseur du 3B au contrôle du format » dans la parenthèse « réseau ».

**2. La ligne « jamais renoté » et la règle des combinaisons ferment le relancement (majeur)**
- **Lieu :** candidat2.md:111, :113, :114, :118 et :130.
- **Constat :**
  - La ligne 2 de la table s'applique à tout juge sans fichier, « de statut consigné « échu » ou « en cours » (ou absent : juge non commencé) ». Elle conclut « jamais renoté (Préséance) ».
  - La ligne « combinaisons » ajoute : « quand deux lignes s'appliquent ensemble, celle qui exclut le relancement prévaut ».
  - Lors de tout arrêt avant qu'un juge ait fini, la ligne 2 s'applique donc aux deux juges. Elle l'emporte sur la ligne 5 (« relancement unique aux seules conditions de « Relancement » »), qui devient lettre morte.
  - Cela contredit « Relancement » (ii), qui admet « statut « en cours » dans un `arret.json` poussé ». Le paragraphe « Préséance » ne vise que les juges finis (« Une fois un juge fini… » ; « Un juge échu n'est jamais renoté »).
  - Même ambiguïté à la ligne 4 : son « aucun relancement implicite » couvre l'instance perdue, une cause d'infrastructure relançable.
- **Preuve :** citations des lignes 111, 113, 114, 118 et 130.
- **Correction :**
  - Ligne 2 : « jamais renoté s'il est « échu » (Préséance) ; un juge « en cours » ou non commencé ne l'est que par la ligne « arrêt avant tout juge fini » ».
  - Ligne 4 : « relancement seulement aux conditions de « Relancement » ».
  - Ligne « combinaisons » : réserver la priorité aux lignes qui disent « aucun relancement ».

**3. La « Préséance des textes » fait plier les écarts déclarés 2 et 3 devant le texte du pilote (majeur)**
- **Lieu :** candidat2.md:77 (repris à la ligne 120), face aux lignes 88-89, 111 et 113.
- **Constat :**
  - La ligne 77 dit : « Les rappels de ce complément (sections « Prédiction », « Métrique », « Seuil » et « Critères de lecture gelés ») sont indicatifs ; en cas d'écart ou d'omission, le texte gelé du pilote […] et le code gelé […] font foi. »
  - La section « Critères de lecture gelés » contient pourtant les lignes qui appliquent les écarts 2 et 3, tranchés par R-164 :
    - « sans déclencheur « décomposition impossible » » ;
    - « nœud pour les deux juges, même si un fichier de notations est écrit ».
  - Lue à la lettre, la préséance rétablit le texte du pilote (« décomposition impossible pour un juge (D-13) » ; « il est lu ») précisément là où le complément s'en écarte de façon déclarée. Pour l'écart 2, elle fait en outre foi à la fois au texte et au code, qui divergent.
- **Preuve :** citations ci-dessus.
- **Correction :** ligne 77 → « en cas d'écart non déclaré ou d'omission […] font foi ; les écarts déclarés (Plan d'analyse, « Écarts déclarés », 1 à 3) et les lignes propres à cette étape priment dans leur seul domaine ».

**4. Écart 3 : sa justification décrit mal le lecteur gelé du pilote (mineur)**
- **Lieu :** candidat2.md:89 (même phrase dans R-164, registres/decisions.md:301).
- **Constat :** « C'est le comportement, sans repli, du lecteur gelé du pilote (`charger_pilote`, commit `2660b07`) ». C'est vrai pour une issue absente et pour un fichier sans sceau. C'est faux pour une issue double et pour des statuts en désaccord avec les fichiers : `charger_pilote` ne s'arrête pas dans ces cas.
- **Preuve :** dans `git show 2660b07:src/controle_ia/environnements/lire_pilote.py`, lignes 195-206, `charger_pilote` lit `resume` et `arret`. Il n'arrête que si `attendu is None` (« ni résumé ni arrêt consigné »). Quand les deux fichiers sont présents, il prend le résumé et continue ; il ne lit aucun statut. Les arrêts sur issue double et sur désaccord sont des gardes neuves : `issue_des_notations` et `charger_notations`, `lire_notations_pilote.py:85-87` et :120-122.
- **Correction :** préciser « gardes neuves, plus strictes que `charger_pilote` » pour l'issue double et le désaccord. Rectifier R-164 par une ligne nouvelle du registre, sans la réécrire.

**5. Mise en place attendue : faux décompte des attentes, référence la plus favorable seule (mineur)**
- **Lieu :** candidat2.md:100.
- **Constat :**
  - Le texte écrit « environ 85 s d'attentes fixes ». La suite de 760 tests en contient au moins 300 s, car les tests de poussée refusée appellent vraiment les scripts.
  - Seul le rapport instance/session 0,65 est donné, qui repose sur la mesure de 1 224,61 s. Une autre mesure des mêmes 689 tests, sur le processeur de la session, donne 1 072,50 s (rapport 0,75). La contre-lecture du texte et du code (vérification « chaîne » 2.1) demandait une fourchette « 0,65 à 0,84 ».
- **Preuve :**
  - Le journal `brouillons/T0.5-notations-suite-20da280-v1.txt` liste parmi les dix tests les plus lents : `test_poussees_apres_le_run_trois_tentatives` 90,72 s ; `test_poussee_finale_refusee_resultats_gardes` 76,43 s ; `test_poussee_finale_cas_sain_et_refus` 75,76 s ; `test_vecteurs_refus_permanent_restes_sur_l_instance` 75,57 s.
  - Chaque poussée refusée trois fois attend 15 + 60 s (`sleep $((15 * essai * essai))`). Aucun test ne simule l'attente : `grep sleep tests/test_script_*` ne renvoie rien.
  - L'autre mesure : `docs/procedures/pilote-T0.5-v1/repetition-jouet-pilote-v1.log:12`, « 689 passed in 1072.50s ».
  - Recalcul, en retirant environ 235 s d'attentes de chaque mesure du pilote et environ 320 s de la suite de 760 tests :
    - avec 1 224,61 s : environ 950 s de tests, marge d'environ 420 s ;
    - avec 1 072,50 s : environ 1 064 s de tests, mise en place d'environ 1 190 s, marge d'environ 310 s.
- **Correction :** écrire « au moins 300 s d'attentes fixes » et donner une marge d'environ 300 à 420 s selon la mesure de référence, avec les deux journaux.

**6. Paragraphe « Marges » : plusieurs inexactitudes (mineur)**
- **Lieu :** candidat2.md:101.
- **Constat :**
  - « plafond de l'amorce (25 800 s, compté depuis la ligne « AMORCE ») » : le `timeout 430m` ne démarre qu'après le clonage. Le seuil réel vaut donc 1 500 s plus la durée du clonage, et la borne de la surveillance environ 286 s, non 300 s.
  - « poussée finale de l'amorce (42 s au pilote) » : les 42 s mesurent le démarrage du conteneur, pas une poussée. La phrase dit d'ailleurs aussi « non mesurée ».
  - « même calcul qu'au pilote » : le texte gelé du pilote tire ses 1 500 s de la surveillance moins le délai externe (Z-5, 17 700 − 16 200 s). Le traitement de la contre-lecture « texte et règles » 5 (point 3) demandait d'écrire cette justification sans « même calcul ».
- **Preuve :**
  - `scripts/amorce_instance_t05_notations.sh` : ligne 24 « AMORCE », ligne 29 clonage, ligne 38 `timeout`.
  - Au pilote : création 10:35:13 (R-151), « AMORCE 10:35:55 » et « début 10:36:09 » (`traces/t05-pilote-v1-20261012-1035/journal-5min.txt` ; `traces/t05-20261012-150232-quTp/journal.txt`). L'amorce n'a pas atteint son plafond : « fin, code 1 ».
  - Correction amendée de la vérification « chaîne » 2.1 : « compté après le clonage, 14 s au pilote » ; « 286 s (26 400 − 25 800 − 300 − 14) » ; « Au pilote, le démarrage a pris 42 s ».
- **Correction :** reprendre ces trois éléments et la justification demandée en NT-5.

**7. « Relançables à aucun prix admis » : affirmation non établie (mineur)**
- **Lieu :** candidat2.md:130.
- **Constat :** au même prix p pour les deux lancements, la condition (iii) avec plus de 6 h de premier lancement exige 6p ≤ 10 − 7,5p, soit p ≤ 0,74 USD de l'heure. Le filtre n'a pas de prix plancher.
- **Preuve :** `lancer_notations_v1.sh:38` fixe `PRIX_MAX=1.30`, sans minimum.
- **Correction :** « à aucun prix au-dessus d'environ 0,74 USD de l'heure ». La condition (iii) reste gardée par le lanceur.

**8. Contenu décrit pour `arret.json` inexact (mineur)**
- **Lieu :** candidat2.md:137.
- **Constat :**
  - « laisse un `arret.json` scellé (étape, motif, et, par juge, statut, lots, lots faits, durée) » : un juge interrompu pendant ses lots n'a pas de durée. Un arrêt avant les notations ne consigne aucun juge.
  - Les « fenêtres » « TERM pendant l'écriture ou le scellement d'un fichier de notations » laissent bien un `arret.json` : elles relèvent du désaccord (ligne 4 de la table), non de son absence.
- **Preuve :** `noter_pilote_a.py:275-276` crée le suivi avec `lots`, `lots_faits` et `statut` ; `duree_s` n'est posée qu'après la boucle (l. 293) ; le bloc d'exception l. 217-222 écrit `arret.json`.
- **Correction :** décrire ces cas tels quels.

**9. Contrôle des formats rangé avant le manifeste (mineur)**
- **Lieu :** candidat2.md:82.
- **Constat :** « formats des deux juges égaux à ceux, scellés, du début du pilote » figure dans la liste « contrôlés égaux par le lanceur avant le manifeste ». Le code les contrôle après, à l'étape « contrôle du format ». La Liste d'arrêt les place correctement « Pendant le run ».
- **Preuve :** `noter_pilote_a.py:241-247`, dans `_apres_manifeste`.
- **Correction :** sortir les formats de cette liste.

**10. Provenance des chiffres de durée (mineur)**
- **Lieu :** candidat2.md:84, :93 et :100.
- **Constat :**
  - La section « Durée et coût » de `plan.md` n'existe pas : les chiffres (7 900 et 9 700 s, rapport 1,24, 15 lots, rapport 0,4 à 1,0) sont dans sa section « Devis ».
  - Les « bornes (N-021) » 23 100 s, 400 min, 430 min et 26 400 s ne figurent pas dans la proposition N-021. Elles viennent de `plan.md` (« Devis ») et du constat 7 de la critique adverse.
  - Les 930 s et 972 s du pilote sont donnés sans pièce.
- **Preuve :** les titres de section de `plan.md` sont seulement « En tête », « Étapes », « Devis » et « Réserves ». La recherche de « 23 100 », « 400 minutes », « 430 » et « 26 400 » dans la proposition N-021 ne trouve rien ; elle ne dit que « ≈ 7,5 heures ».
- **Correction :** renvoyer à `plan.md`, « Devis » (61f78ad5…), à `critique.md`, constat 7, et aux traces `traces/t05-pilote-v1-20261012-1035/` avec empreintes.

**11. Diagnostics de fin d'amorce décrits incomplètement (mineur)**
- **Lieu :** candidat2.md:85.
- **Constat :** le texte annonce « les 15 dernières lignes de `run.err` […] et les 20 dernières du journal ». L'amorce affiche aussi les 20 dernières lignes de `tests.txt` et de `tests.err`. Rien de décisif n'y figure.
- **Preuve :** `amorce_instance_t05_notations.sh:51-53`.
- **Correction :** les nommer.

**12. Une issue sans ligne : l'arrêt de la lecture par une autre garde (mineur)**
- **Lieu :** candidat2.md:116 et :138.
- **Constat :** seul l'arrêt sur le format ou sur P1, P4 à P7 a une lecture (nœud). Les autres gardes de lecture n'en ont aucune : désalignement, modules modifiés, rattachements, arbre non propre.
- **Correction :** ajouter une ligne. Garde de procédure (arbre non propre, identifiant déjà pris) : correction puis nouvel appel du lecteur. Toute autre garde : nœud, proposition à Lazar.

#### Vérifié conforme
- **Empreintes :** les 27 fichiers cités présents sur disque ont des empreintes égales ; les deux scripts au commit 20da280 aussi. L'empreinte canonique de la configuration relue, b3d24dec…, est recalculée. L'entropie est celle du manifeste du pilote. Les gardes de citation du lanceur, rejouées sur le candidat avec torch simulé, passent, et le commit lu est 20da280.
- **Seuil :** recopié mot pour mot (`diff` vide avec les lignes 128-133 du pilote). Le tableau P2-P3 et la phrase sur P2 et P3 sont fidèles.
- **(f) Intitulés :** les 14 intitulés figurent chacun exactement une fois sous la forme « <intitulé> : ` ».
- **Code :**
  - entre 2660b07 et 20da280, sept fichiers ajoutés seulement, aucun modifié ;
  - rien dans `src/`, `tests/` ou `scripts/` entre 20da280 et b9c4f7f ;
  - 760 = 689 + 71 (tests des trois fichiers, paramétrisations comprises), et le journal dit « 760 passed in 1419.11s ».
- **(d) Code décrit fidèlement :** ordre des étapes ; échéances par juge et globale, avec leurs ancrages ; lignes de progression ; juge échu ; libération du 8B ; issue et accord des statuts ; lecture sous ce préenregistrement ; graines de la lecture ; `audit_r4_juges` sans volet familles.
- **Tests nommés :** les 11 existent et affirment ce que dit le texte. Seule réserve : « deux juges concluants » n'est pas affirmé tel quel dans le test d'équivalence sur le même pilote.
- **Actions de l'audit recalculées :** aucune en commun avec la première lecture, pour 180 comme pour 360 réponses ; sans réponse, le tirage redonne exactement celui de `lecture.json`.
- **(c) Calculs justes :** 7 565 ; 7 900 et 9 700 ; 1,24 ; 514 s ; 15 lots ; 435 s ; 9,75 ; environ 10,3 ; 0,25 ; 1,83 ; 7,33 h ; 0,65 ; 930 et 972 ; 128,0 et 48,7 ; 7 037,2, 461,0 et 15 063,6 ; 0,930 ; kappas de R-156 ; aucun ensemble décisif vide.
- **(e) Traitement réellement présent :** NT-1, NK-1, NL-1 et NT-3, NL-2, NL-3, NT-2, NT-4, NT-6, NT-7, NT-8 et NE-1, NE-7, NK-2, NT-9, NL-5, NC-1, KR-7. En partie seulement : NT-5, NC-2 et NK-3 (constats 5 et 6).
- **Registres :** R-147, R-155, R-160, R-163, R-164, N-021 et GO-2026-10-12-02 sont cités fidèlement.

#### Non vérifié
- Tests non exécutés (torch absent de cet environnement) : vérifiés par lecture seulement.
- Que la mesure de 1 419,11 s ait été prise « sur le même processeur ».
- Chaîne de lancement (brouillon 3) : seules ses constantes ont été lues.
- Identité des lots sur les 60 tâches réelles : établie seulement sur le cas jouet.
- `prereg/T0.5-pilote-notations-config-v1.json` est absent aujourd'hui (contrôlé par `git ls-files` et `ls`) ; il doit être copié au scellement.
- Rapport JSON de la contre-lecture de la chaîne non parcouru en détail.

Aucun fichier du dépôt n'a été modifié. Mes fichiers de travail (extraits du code au commit 20da280, scripts de recalcul) sont dans /tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/vc-texte/.

### Rapport — code, `a859045` → `20da280`

**Verdict : conforme avec réserves.** Je n'ai trouvé aucun constat bloquant ni majeur. Il y a cinq constats mineurs, tous de précision du texte ou de couverture de tests. Aucun ne cache de repli silencieux ni de part de résultat visible pendant le run.

Je n'ai modifié aucun fichier du dépôt (`git status` est vide). Mes fichiers de travail sont sous `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/vc-code/` :
- `arbre/` : extraction de 20da280 ;
- `verif/tests/test_zz_verif.py` : sept contrôles ciblés ;
- `mut/` : mutant aux ancrages des échéances inversés.

Tests passés sur l'extraction : les 71 tests des trois fichiers passent (533,9 s). La suite collecte 760 tests à 20da280, ce qui correspond aux tests attendus cités par le candidat.

#### Constats

**1. Fenêtre sans `arret.json` non déclarée, entre la création du manifeste et le bloc qui consigne l'arrêt**
- Gravité : mineur.
- Lieu : `src/controle_ia/environnements/noter_pilote_a.py:208-215`. Le candidat 2 (ligne 137, fenêtres déclarées) ne la nomme pas.
- Constat : après le retour de `creer_manifeste` (208-210), les lignes 211 à 214 s'exécutent hors du `try` (ligne 215) : `debut = …` et `etat = {… empreinte_config(config) …}`. Un TERM reçu à ce moment laisse un manifeste sans `arret.json` ni `resume.json`. Le texte ne déclare que « signal reçu pendant la création du manifeste ». La fenêtre dure quelques microsecondes. Elle se lit déjà par la quatrième ligne de la table (non lisible, nœud), donc sans repli silencieux.
- Preuve : le contrôle v5 remplace `npa.empreinte_config` par un appel à `gardes.lever_sur_term(15, None)`. En mode jouet sans préenregistrement, c'est son premier appel. Sortie : « V5 motif: signal TERM reçu … | appels: 1 | manifeste: True | fichiers diag: dossier diag absent ».
- Correction proposée : la plus simple est dans le texte, sans toucher au code gelé : « signal reçu pendant la création du manifeste ou juste après, avant l'entrée dans le bloc qui consigne l'arrêt ». Autre voie, dans le code : calculer `debut` et `etat` avant `creer_manifeste`. Elle demande un nouveau commit et une nouvelle suite.

**2. Durée par juge absente de `arret.json` pour un juge « en cours »**
- Gravité : mineur.
- Lieu : candidat 2, ligne 137 (« `arret.json` scellé (étape, motif, et, par juge, statut, lots, lots faits, durée) ») ; code, `noter_pilote_a.py:275` et `:293`.
- Constat : `suivi` naît avec `lots`, `lots_faits` et `statut`. `duree_s` et `memoire_pic_gio` ne s'ajoutent qu'après la boucle des lots. Un arrêt pendant les lots ne laisse donc aucune durée par juge, seulement la durée globale. La phrase de la ligne 85 (« ne portent … que ») reste juste.
- Preuve : contrôle v6 (TERM pendant le 8B). Sortie : « clés du 8B en cours dans arret.json: ['lots', 'lots_faits', 'statut'] | clés d'arret: ['duree_s', 'etape', 'motif', 'partiel'] ».
- Correction proposée : ligne 137, écrire « (étape, motif, durée du run et, par juge, statut, lots, lots faits ; durée et mémoire pour un juge fini) ».

**3. Deux propriétés décrites comme établies par un test sans que le test les affirme**
- Gravité : mineur.
- Lieu : candidat 2, ligne 87 (« cas non trivial : deux juges concluants ») ; docstring `lire_notations_pilote.py:15` (« sans déclencheur ») ; test `tests/test_lire_notations_pilote.py:294-311`.
- Constat : `test_equivalence_avec_analyser_sur_le_meme_pilote` affirme au moins 48 tâches, P3 tranchée et 10 réponses tirées. Il n'affirme ni deux décompositions concluantes, ni l'absence de déclencheur. Les deux propriétés sont vraies au passage du test, mais rien ne les garde. L'absence de déclencheur est bien affirmée ailleurs, à la ligne 324 de `test_8b_echu_3b_seul_lu`.
- Preuve :
  - contrôle v1 : « decomposition_concluante: {'8B': True, '3B': True} taches diff: 50 P3: confirmée » ;
  - contrôle v7 : « lecteur: {'trop_propre': [], 'trop_sale': [], 'declenche': False} … suspendue: False False » ;
  - le test ne contient aucune assertion sur `decomposition_concluante` (lignes 294-311).
- Correction proposée : dans le texte, écrire « deux juges concluants (constaté, non affirmé par le test) », sans changer le code. Autre voie : ajouter les deux assertions, ce qui demande un nouveau commit.

**4. Règle R5 : trois branches de gardes neuves sans artefact**
- Gravité : mineur.
- Lieu : `lire_notations_pilote.py:75`, `:88`, `:120`. Le candidat 2, section Contre-lecture, annonce pourtant « tests de chaque garde neuve sur un cas sain et sur un artefact ».
- Constat :
  - (a) `exiger_run_sous_prereg` : la moitié « même chemin, empreinte différente de celle du manifeste » n'a pas d'artefact. L'artefact « prereg-modifie » s'arrête avant, au sceau (ligne 69). C'est bien la garde de sceau visée, voir la preuve.
  - (b) `issue_des_notations` : un `resume.json` ou un `arret.json` sans sceau conforme n'a pas d'artefact au niveau du lecteur. La garde est la fonction gelée `verifier_resultat`.
  - (c) Désaccord dans le sens « statut écrit, fichier absent » : non testé. Il fonctionne.
- Preuve :
  - `grep -rn "exiger_run_sous_prereg\|issue_des_notations" tests/` ne trouve qu'une assertion de résultat (ligne 209) ;
  - aucun test ne retire le sceau d'une issue ;
  - le seul cas de `statuts=` est `{"8B": "échu"}` avec le fichier du 8B présent (lignes 199-203) ;
  - contrôle v3 (sens inverse) : « fichiers de notations et statuts de resume.json en désaccord pour ['3B'] » ;
  - contrôle v2 : « empreinte f63e597dcda9… ≠ scellée 67306df6e996… | levée par exiger_prereg_scelle du lecteur : True ».
- Correction proposée : nommer ces trois branches dans le texte (même expression ou garde gelée réutilisée), ou ajouter trois artefacts au prochain commit du code.

**5. Préenregistrement donné en chemin absolu hors du dépôt : `ValueError` au lieu de `GardeArret`**
- Gravité : mineur.
- Lieu : `lire_notations_pilote.py:66-68`.
- Constat : `relative_to` lève `ValueError` avant la garde « préenregistrement … hors du dépôt » de `creer_manifeste`, que la Liste d'arrêt cite. L'arrêt reste bruyant et la lecture n'est pas écrite. La seule commande permise passe un chemin relatif et n'atteint donc jamais ce cas.
- Preuve : contrôle v4. Sortie : « V4 exception: ValueError GardeArret ? False : '…/ailleurs.md' is not in the subpath of '…/depot' … ».
- Correction proposée : rien d'obligatoire avant le scellement. Si le code est retouché pour une autre raison : `except ValueError: raise GardeArret("préenregistrement hors du dépôt")`.

#### Vérifié conforme

- **(a) Lignes de progression :**
  - par lot, seulement juge, rang et durée (`noter_pilote_a.py:292`) ;
  - par fin de juge, statut, lots faits et durée (304-305) ;
  - aucun compte de jetons pour un juge non écrit (275, 301-303) ;
  - test `tests/test_noter_pilote_a.py:471-477`.
- **(a) Étape « chargement du juge 8B »** : ligne 236 ; test 580-595.
- **(a) Journal :** « run terminé : $RUN » ne recopie plus le résumé (`scripts/notations_t05_instance.sh:267`) ; test `test_script_notations_t05.py:138`.
- **(a) Graines du lecteur :** quatre graines consignées, une seule entropie exigée et égalité exigée avant toute écriture (198-207). Sur les données réelles, la même entropie et les quatre clés figurent au manifeste d'analyse.
- **(a) Lecture décisive :** elle exige le run sous le préenregistrement passé (107-108), et `--prereg` est obligatoire en ligne de commande (214-215).
- **(a) Issue du run :** exactement une issue, scellée et rattachée, avec des statuts accordés aux fichiers présents.
- **(a) Arrêts :** toutes les gardes neuves lèvent `GardeArret` (sauf le constat 5) ; aucun repli silencieux.
- **(b) Les artefacts atteignent la garde visée :** les messages sont précis. Celui du sceau est confirmé par un espion (contrôle v2). Le mutant aux ancrages inversés fait échouer `test_echeance_du_3b_ancree_a_son_premier_lot` et `test_echeance_du_8b_ancree_au_debut_du_run`.
- **(c) Les neuf tests nommés existent à 20da280** et affirment ce que dit le texte, à la nuance du constat 3 près. `test_memes_notations_que_le_lanceur_du_pilote` compare bien, dans l'ordre, une tâche, e0 noté deux fois et e1, des lots de 2 dont le dernier partiel, et les six champs.
- **(d) Code et scripts gelés intacts :**
  - `git diff --quiet 2660b07 20da280` sur les neuf modules de `MODULES_LECTURE` rend 0 ;
  - même résultat pour `pilote_t05_instance.sh` et `amorce_instance_t05.sh` ;
  - de a859045 à 20da280, seuls changent deux modules neufs et `notations_t05_instance.sh` ;
  - de 2660b07 à 20da280, aucun autre fichier de `src/` ne change.
- **(e) Empreintes des scripts :** à 20da280, `c751190226eb…d8d1` pour l'amorce et `2106eade84ea…73b5` pour le script de l'instance, égales à celles du candidat 2. Le commit cité est bien `20da280bf59b…`.
- **Lignes du traitement :** NL-1, NL-3 (hors le constat 1), NL-4, NL-5, NL-8, NL-11, NT-2, NT-7, NT-8, NT-9, NE-2 à NE-5, NE-8, NC-3, NC-4, NK-1, NK-5, NK-6, et KR-7 pour la partie script : toutes conformes au code.

#### Non vérifié

- Comportement en mode réel sur processeur graphique : versions, téléchargement, mémoire de la carte.
- Suite complète : non relancée ; je me suis appuyé sur `brouillons/T0.5-notations-suite-20da280-v1.txt` (760 passed).
- Lecture sur les vraies pièces du pilote : non exécutée.
- Chaîne de lancement (brouillon 3), surveillance et récupération : hors du périmètre demandé.
- Contenu possible des avertissements et traces d'appel des bibliothèques recopiés au journal en cas d'arrêt : comportement déclaré, non testable ici.

### Rapport — chaîne, brouillon 3

**Verdict : à corriger.** Je n'ai trouvé aucun constat bloquant. Il y a un constat majeur et neuf mineurs. Aucun ne change le texte du candidat 2 ; tous portent sur des scripts de la chaîne, que le plan fige au commit C1. Il faut donc les corriger avant C1.

Fichiers de travail : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/vc-chaine/` (banc de la surveillance, journaux synthétiques, essais du module). Je n'ai modifié aucun fichier du dépôt ni du bloc-notes, je n'ai fait aucun appel à vastai et aucun accès réseau.

#### Constats

**1. Banc du lanceur : la vérification du cas sain P00 est périmée, plante, et cet échec n'est pas compté**
- Gravité : majeur.
- Lieu : `essais_lanceur_notations_v1.sh:158-166` (et l'en-tête, ligne 5) ; `lancer_notations_v1.sh:268-270`.
- Constat :
  - Le bloc Python de P00 cherche `^base de la surveillance (\d+) `. Le lanceur du brouillon 3 n'écrit plus cette ligne : il écrit « plafond de la surveillance N (création + 26400 s ; …) ».
  - `re.search` rend donc None et le bloc lève AttributeError.
  - Le code de sortie de ce bloc n'est pas compté. Le banc finit quand même sur « cas non conformes : 0 », avec une trace d'erreur dans un journal versé comme preuve. C'est un repli silencieux, interdit par R5.
  - Conséquence : aucun banc n'éprouve le plafond de la surveillance écrit par le lanceur (création + 26 400 s). Les contrôles ne relient pas non plus `PLAFOND_SURVEILLANCE_S` du lanceur.
  - Les autres vérifications de ce bloc (étiquette, ETUDE absente, branche v1) sont seulement affichées, jamais comptées.
  - L'en-tête parle encore d'une « base de la surveillance à la création + 4 800 s ».
- Preuve : j'ai reproduit `lancement.txt` avec le `printf` du lanceur, puis joué les lignes 159-165 du banc.
  ```
  AttributeError: 'NoneType' object has no attribute 'group'
  code du bloc P00 : 1
  occurrences de « base de la surveillance » dans le lanceur : 0
  ```
- Correction proposée :
  - Lire `^plafond de la surveillance (\d+) \(création \+ 26400 s` et exiger la valeur = création + 26 400.
  - Faire sortir le bloc en code 1 sur toute valeur fausse, et compter cet échec (`|| NON_CONFORMES=…`).
  - Corriger l'en-tête.
  - Relier `^PLAFOND_SURVEILLANCE_S=26400 ` dans le bloc 9 des contrôles, avec un artefact.

**2. Les preuves des essais acceptent un journal où un contrôle a échoué sans être compté**
- Gravité : mineur.
- Lieu : `verifications_notations_v1.py:152-154` ; `essais_lanceur_notations_v1.sh:360` ; `repetition_finale_notations_v1.sh:50-54` et `:65`.
- Constat :
  - Le sous-programme `preuves` ne lit que la dernière ligne de chaque journal.
  - Le banc du lanceur affiche « JETON AFFICHÉ : … » sans incrémenter le compteur d'échecs.
  - La répétition finale peut écrire « scellement : NON CONFORME » puis « RÉPÉTITION FINALE : CONFORME », car son verdict ne dépend que des codes `c` et `c2`.
  - Le lanceur laisserait alors partir la création. Ces défauts existaient déjà dans le brouillon 2 et au pilote, mais ces journaux sont désormais la porte du lanceur.
- Preuve : un dossier de journaux synthétiques où le journal du lanceur contient, avant son verdict, « Traceback… », « JETON AFFICHÉ… » et « P13c : … NON CONFORME » donne `preuves` : code 0.
- Correction proposée : compter ces deux cas dans leur script. Ou faire refuser par `preuves` toute ligne qui commence par « JETON AFFICHÉ », contient « NON CONFORME » ou commence par « Traceback ».

**3. La garde d'adresse du scellement est contournable par une seconde adresse de poussée**
- Gravité : mineur (sûreté).
- Lieu : `sceller_notations_v1.sh:50-53`, poussée à la ligne 157.
- Constat : `git remote get-url --push origin` ne rend que la première adresse de poussée, alors que `git push origin` pousse vers toutes. Avec une seconde `pushurl` vers `lciric/controle-ia`, la garde passe et S part aussi vers la copie publique.
- Preuve : dans le bloc-notes de vérification, avec deux `pushurl` (travail.git, puis publique.git) :
  ```
  garde du scellement (sens --push) : acceptée (…/travail.git)
  poussée : code 0
  main du dépôt « publique » : a59178fd…
  ```
- Correction proposée : exiger que `git remote get-url --all origin` et `git remote get-url --all --push origin` rendent chacune une seule ligne, égale à DISTANT.

**4. Banc du scellement : les cas S39 et S39b pointent la vraie copie publique**
- Gravité : mineur (sûreté).
- Lieu : `essais_scellement_notations_v1.sh:235` et `:238`.
- Constat :
  - S39b règle l'adresse de poussée sur `https://github.com/lciric/controle-ia.git`.
  - Si la garde régressait, le scellement irait jusqu'à `git push -q origin HEAD:main` (ligne 157) et pousserait tout l'historique de travail vers ce nom. Le banc ferait l'action interdite au lieu de signaler l'échec.
  - Aucun chemin n'existe aujourd'hui : j'ai vérifié que la garde est présente dans le brouillon 3.
- Correction proposée : utiliser un dépôt nu local (par exemple `$E/lciric/controle-ia.git`) et vérifier qu'il reste vide après le cas.

**5. Le relevé du premier lancement n'est lié ni au commit S, ni à l'instance, ni à la copie versée**
- Gravité : mineur.
- Lieu : `lancer_notations_v1.sh:94-109` ; `plan-lancement-notations-v1.md:99-100` contre `:106`.
- Constat :
  - Le lanceur accepte tout fichier qui porte une ligne « AMORCE … : commit » vers un commit quelconque, sans exiger S.
  - Il ne lit pas la copie versée et scellée du relevé, et ne vérifie pas qu'elle correspond à l'instance nommée par la ligne R-….
  - Le plan donne deux emplacements pour ce relevé : `traces/t05-notations-releve-<id>/` à l'étape 5, et `traces/t05-notations-v1-<date>/` à l'étape 6.
- Preuve : les lignes 96-107 du lanceur, jouées sur un fichier contenant seulement `AMORCE 2026-10-01T08:00:00Z : commit 000…0`, rendent « aucune fin de juge », code 0.
- Correction proposée :
  - Exiger `AMORCE … : commit $S`.
  - Lire le relevé à HEAD sous `traces/t05-notations-releve-$PREMIERE/releve-cumulatif.txt`, avec son sceau.
  - Unifier l'emplacement dans le plan.

**6. La surveillance exécutée n'est jamais comparée à sa copie versée après S**
- Gravité : mineur.
- Lieu : `lancer_notations_v1.sh:111-112` ; `surveiller_notations_v1.sh`, qui n'a pas de contrôle de lui-même ; plan, étape 5.
- Constat :
  - Le lanceur ne compare que les contrôles, le module commun et lui-même aux copies de S.
  - Le scellement compare les 13 scripts au moment de S. Ensuite, la surveillance du bloc-notes tourne pendant des heures sans aucune vérification.
  - La récupération, elle, se vérifie elle-même (lignes 41-43).
- Correction proposée : faire comparer par le lanceur les 13 scripts de la liste CHAINE aux copies de S.

**7. Le lanceur garde sa propre copie de la lecture du GO, et elle a déjà dérivé du module**
- Gravité : mineur.
- Lieu : `lancer_notations_v1.sh:151-177` contre `verifications_notations_v1.py:43-45`.
- Constat :
  - Le texte du module commun cite lui-même la dérive des copies d'un même bloc comme sa raison d'être. Or le lanceur garde une troisième copie de la lecture du GO.
  - Cette copie accepte une seconde ligne mal formée « - Décision de Lazar sur N-021 : … », que le module refuse.
  - L'effet est faible, car les contrôles rejoués sur le même S la refusent.
- Preuve : le candidat 2 plus la ligne « - Décision de Lazar sur N-021 : retirée par Lazar (essai) » donne : copie du lanceur → code 0 ; module → code 1, « absente, en double ou mal formée ».
- Correction proposée : appeler `python3 -I "$H/verifications_notations_v1.py" go "$T/prereg-S.md" …`.

**8. Contrôles, bloc 9 : une assertion littérale toujours vraie, qui ne dit pas ce que dit le texte**
- Gravité : mineur.
- Lieu : `controles_avant_depense_notations_v1.sh:250`.
- Constat :
  - `assert 26400 >= 430 * 60 + 240` n'utilise que des littéraux : aucun artefact ne peut la faire échouer. C'est la raison même pour laquelle la « marge d'un lot » a été ramenée à un commentaire (ligne KS-5 du traitement).
  - Le texte (Plan d'analyse, « Marges ») compare la surveillance au KILL de l'amorce : 25 800 + 300 s, avec un démarrage du conteneur sous 300 s moins la poussée finale. L'assertion prend 240 s et ignore les 300 s du KILL.
- Correction proposée : la ramener à un commentaire, ou la calculer à partir des valeurs relues (430 lu dans l'amorce, PLAFOND_S lu dans la surveillance, plus 300 s).

**9. Gardes neuves sans artefact ou sans cas sain dans les bancs (règle R5)**
- Gravité : mineur.
- Lieu et constat :
  - `preuves` : les refus « éprouvé sous deux empreintes », « mal formée » et « aucune ligne » ne sont joués par aucun cas du banc du lanceur. `grep` sur le banc : 0 occurrence. P30b altère les deux journaux de façon cohérente, donc il n'atteint pas le refus « deux empreintes ».
  - Surveillance : aucun cas sain pour « ÉTAT TERMINAL vu deux fois de suite » (un seul état hors ligne, puis retour en marche). Seuls `etat-2` et `etat-3` existent, tous deux hors ligne. Aucun cas pour un usage faux.
  - Contrôles : aucun artefact pour « `$D.suite.txt` existe déjà (R12) » (ligne 68). Le banc ne mentionne `suite.txt` que dans le bouchon.
- Preuve que les gardes elles-mêmes fonctionnent : je les ai jouées directement sur le module (voir « Vérifié conforme »).
- Correction proposée : ajouter ces cas aux bancs.

**10. Les contrôles et la récupération ne lisent, des traces poussées, que `journal.txt`**
- Gravité : mineur ; portée nulle en pratique sous la condition (iii) du relancement.
- Lieu : `controles_avant_depense_notations_v1.sh:199-202` ; `recuperation_notations_v1.sh:56-57` ; `notations_t05_instance.sh:143` et `:247-248` (au commit 20da280).
- Constat :
  - Le texte compte comme fin de juge toute ligne de fin des « traces poussées », dont `run.err` complet.
  - Les lignes de progression passent de `run.err` à `journal.txt` par un relais asynchrone (`tail | grep | while`). Seul `journal.txt` est lu.
  - La condition (iii) borne le premier lancement à moins de deux heures d'instance, ce qui rend une ligne de dernier lot hors d'atteinte avant un relancement admis. D'où la portée nulle en pratique.
- Correction proposée : chercher aussi dans `traces/*/run.err`.

#### Vérifié conforme
- **Empreintes et bloc-notes** : les 14 empreintes du brouillon 3 sont conformes. Le bloc-notes de la session de pilotage est identique au brouillon 3 (14 fichiers comparés octet par octet). Rien n'a changé dans `src`, `scripts` et `tests` depuis 20da280.
- **Module commun**, lu de la même façon par le scellement (`sceller:112`, `:118`) et par les contrôles (`controles:129`, `:145`) :
  - `go` : conforme sur les registres réels ; 7 altérations refusées (révocation en colonne 3 ou 8, révocation du GO de calcul, colonne d'état avec suffixe, lignes R-160, GO ou N-021 en double).
  - `repetition` : un journal synthétique sain est accepté. 19 altérations sont refusées : KO dans chaque bloc conforme, KO après une ligne « -- », second KO, préfixe autre, KO déplacé hors de son bloc, candidat autre ou en double, script manquant, en plus, en double ou mal formé, passages, FIN, commit, conforme en trop.
  - `preuves` : le cas sain est accepté ; les refus « deux empreintes », « mal formée », « aucune ligne » et « verdict autre » fonctionnent.
  - `statuts-v1` : « en cours » et « aucun juge » acceptés ; écrit, échu, fichier illisible et clés manquantes refusés.
- **Lanceur** :
  - Relevé : ligne « AMORCE » exigée ; `fin=` et `lot=n/n` refusés.
  - Dépense engagée lue une seule fois dans la ligne R-… ; plafond de 10,5 USD respecté.
  - Instance du premier lancement nommée une seule fois et tolérée seulement si elle est arrêtée.
  - Preuves des essais : cinq journaux, sceau exact, dix scripts éprouvés, chacun égal à sa copie de S.
  - Adresse du dépôt de l'instance (DEPOT_URL) écrite en dur sur le dépôt de travail.
- **Contrôles en mode relance** : branche `-v2` absente ; branche `-v1` descendante de S ; seuls les fichiers ajoutés sont lus ; notations, résumé, arrêt illisible ou de statut autre que « en cours », et lignes de fin ou de dernier lot sont refusés. Les formats des lignes de progression (`noter_pilote_a.py:74`, `:292`, `:304`) et de `arret.json` correspondent aux motifs cherchés.
- **Récupération en mode relance** : conforme au texte du candidat (notations, résumé, ligne de fin ou de dernier lot).
- **Surveillance** :
  - Plafond = création + 26 400 s.
  - Le relevé `progres.txt` est seulement complété, jamais tronqué.
  - Banc joué avec HN pointé sur le brouillon 3 : 9 cas conformes, code 0, aucun fichier du dépôt touché.
- **Ordre des préalables** : C1, puis bancs et répétitions, puis C2, puis S, sans circularité. Le scellement ne dépend pas des preuves. Les noms de journaux et leurs dernières lignes sont identiques entre bancs, module et lanceur. Les 13 scripts sont couverts (10 éprouvés, 3 répétés).
- **Faisabilité de la répétition finale** : les copies jouées du scellement et des contrôles ne contiennent plus « github » ni l'adresse du dépôt réel après substitution. Les dépendances et les modules de lecture à HEAD sont égaux à ceux du pilote.
- **Candidat 2** : les 14 intitulés sont cités une seule fois, et les 7 valeurs de bornes sont citées.
- **Sûreté** :
  - Aucun arrêt par motif de ligne de commande (pas de `kill`, `pkill` ni `killall`), aucun `vastai stop` ni `destroy` dans la chaîne.
  - `show instances --raw` et `show instance --raw` sont toujours filtrés. Seule exception : sur réponse illisible, la surveillance garde 120 caractères bruts, masqués.
  - Les jetons sont masqués partout.
  - Dossiers neufs exigés partout (R12).
  - Aucune poussée possible vers `lciric/controle-ia`, hors les constats 3 et 4.

#### Non vérifié
- Les bancs du lanceur, des contrôles et du scellement, ainsi que les répétitions jouet et finale, n'ont pas été joués (consigne). Leur verdict réel reste inconnu.
- Le format réel de `vastai logs` et le jeton GitHub de l'instance.
- La course entre `run.err` et `journal.txt` sur une instance réelle.
- `construire_pilote_jouet_v1.py`, inchangé depuis le brouillon 2, n'a pas été relu.
- Le rapport brut de la contre-lecture (`…-relecture-chaine-v1.json`) n'a pas été relu en entier ; seules les lignes KL, KS, KR, KH et KK du traitement l'ont été.

### Traitement

Identifiants : VT (texte), VC (code), VH (chaîne), dans l'ordre des rapports ci-dessus.

| id | gravité | constat | traitement |
|---|---|---|---|
| VT-1 | majeur | classement des pannes réseau contradictoire | candidat 3 : clôture de la Liste d'arrêt « la cause se qualifie selon « Causes d'un arrêt » » ; tokeniseur du 3B nommé dans « réseau » |
| VT-2 | majeur | « jamais renoté » et combinaisons ferment le relancement | candidat 3 : ligne 2 de la table (« jamais renoté s'il est échu » ; un juge en cours ou non commencé ne l'est que par la ligne « arrêt avant tout juge fini ») ; ligne 4 (« relancement seulement aux conditions de « Relancement » ») ; combinaisons (une ligne qui dit « aucun relancement » prévaut) |
| VT-3 | majeur | préséance des textes contre les écarts déclarés | candidat 3 : « en cas d'écart non déclaré ou d'omission » ; écarts déclarés et lignes propres à l'étape priment dans leur seul domaine |
| VT-4 | mineur | justification de l'écart 3 | candidat 3, écart 3 ; R-165 (précision de R-164, sans réécriture) |
| VT-5 | mineur | mise en place : attentes et référence | candidat 3 : au moins 300 s d'attentes fixes, deux mesures de référence (1 224,61 s et 1 072,50 s, journaux et empreintes), marge d'environ 290 à 410 s (suite au commit `259cf5e` : 1 444,88 s) |
| VT-6 | mineur | paragraphe « Marges » | candidat 3 : plafond de l'amorce compté après le clonage (14 s au pilote), borne d'environ 286 s, 42 s = démarrage du conteneur, justification du seuil sans « même calcul » |
| VT-7 | mineur | « aucun prix admis » | candidat 3 : « à aucun prix au-dessus d'environ 0,74 USD de l'heure » |
| VT-8 | mineur | contenu d'`arret.json` et fenêtres | candidat 3 : contenu exact (durée du run ; durée et mémoire pour un juge fini seulement) ; fenêtres sans `arret.json` et fenêtres en désaccord séparées |
| VT-9 | mineur | formats rangés avant le manifeste | candidat 3 : formats contrôlés au début du run, après le manifeste |
| VT-10 | mineur | provenance des chiffres | candidat 3 : `plan.md`, « Devis » ; critique, constat 7 ; traces du pilote avec empreintes (création, « AMORCE », début, « run : ») |
| VT-11 | mineur | diagnostics de fin d'amorce | candidat 3 : `tests.txt` et `tests.err` nommés |
| VT-12 | mineur | arrêt de la lecture par une autre garde sans ligne | candidat 3 : ligne de la table (nœud ; garde de procédure corrigée puis lecteur rappelé) |
| VC-1 | mineur | fenêtre sans `arret.json` après le manifeste | code `259cf5e` : état et début du run calculés avant le manifeste ; candidat 3 : fenêtre nommée |
| VC-2 | mineur | durée par juge absente pour un juge en cours | candidat 3 (avec VT-8) |
| VC-3 | mineur | propriétés décrites sans assertion | code `259cf5e` : test d'équivalence sur le même pilote, deux juges concluants et aucun déclencheur affirmés |
| VC-4 | mineur | trois branches de gardes sans artefact | code `259cf5e` : préenregistrement rescellé (même chemin, autre empreinte), issue sans sceau conforme, statut « écrit » sans fichier |
| VC-5 | mineur | chemin absolu hors du dépôt : ValueError | code `259cf5e` : GardeArret « hors du dépôt », artefact |
| VH-1 | majeur | vérification du cas sain P00 périmée, non comptée | banc du lanceur : plafond de la surveillance lu et exigé (création + 26 400 s), vérifications comptées, en-tête corrigé ; contrôles : `PLAFOND_SURVEILLANCE_S` du lanceur relié (banc A44c) |
| VH-2 | mineur | preuves : échec non compté accepté | module commun : toute ligne « NON CONFORME », trace d'exception ou jeton affiché refusée (banc P30g) ; banc du lanceur : jeton affiché compté ; répétition finale : verdict conditionné au scellement conforme |
| VH-3 | mineur | seconde adresse de poussée | scellement : toutes les adresses de origin, une seule admise dans chaque sens (banc S39c) |
| VH-4 | mineur | bancs S39 et S39b sur la vraie copie publique | dépôt nu local nommé comme elle, vérifié vide après chaque cas |
| VH-5 | mineur | relevé non lié à S ni à sa copie versée | lanceur : copie versée et scellée à HEAD sous `traces/t05-notations-releve-<instance>/`, égale à l'argument, ligne « AMORCE » du commit de scellement (bancs P13q, P13r, P13s, P13i) ; plan : emplacement unique |
| VH-6 | mineur | surveillance non comparée après S | lanceur : les treize scripts du bloc-notes comparés aux copies versées à S (banc P31) |
| VH-7 | mineur | copie du GO dans le lanceur | lanceur : lecture par le module commun |
| VH-8 | mineur | assertion littérale toujours vraie | ramenée à un commentaire |
| VH-9 | mineur | gardes neuves sans cas | bancs : P30h, P30i, P30j (preuves) ; M08, M09 (surveillance) ; Z2f (contrôles) |
| VH-10 | mineur | `run.err` des traces non lu | contrôles et récupération : journal et `run.err` des traces (banc A48d) |

## Tour 2

### Rapport — texte, candidat 2 → candidat 3

**Verdict : conforme avec réserves.** Le candidat 3 règle les douze constats VT du premier tour, ainsi que VC-1 et VC-2 côté texte. Le différentiel n'ouvre ni ne ferme à tort la porte du relancement, et tous les chiffres et empreintes recalculés sont justes. Trois constats neufs, tous mineurs et sans effet sur une lecture ou un relancement, restent à reprendre avant le scellement.

#### Constats du premier tour

- **VT-1 : tenu.**
  - Ligne 138 : « Ces entrées n'ajoutent aucun classement : la cause d'un arrêt se qualifie selon « Causes d'un arrêt » ».
  - Ligne 127 : « réseau (téléchargement du 8B, du tokeniseur du 3B au contrôle du format et préchargement du 3B compris) ».
  - Le code le confirme : `charger_format_seul` appelle `AutoTokenizer` (`lancer_pilote_a.py:206-218`) sous l'étape « contrôle du format » (`noter_pilote_a.py:243-246`).
- **VT-2 : tenu.**
  - Ligne 111 : « jamais renoté s'il est « échu » (Préséance) ; un juge « en cours » ou non commencé ne l'est que par la ligne « arrêt avant tout juge fini » (relancement unique) ».
  - Ligne 113 : « relancement seulement aux conditions de « Relancement » ; sinon, proposition à Lazar ».
  - Ligne 119 : « une ligne qui dit « aucun relancement » prévaut ».
  - J'ai repris les cas un par un :
    - arrêt avant tout juge fini : lignes 2 et 5, relancement ouvert sous « Relancement » ;
    - 8B échu puis arrêt pendant le 3B : la ligne 5 est exclue, aucun relancement, comme le dit le paragraphe de préséance ;
    - 8B écrit puis arrêt : ligne 3, aucun relancement ;
    - run sans issue : ligne 4, renvoi à la condition (ii) ;
    - dernier lot fait sans fichier : la condition (ii) ferme.
  - Seule la ligne 3 dit « aucun relancement », et elle ne peut pas s'appliquer en même temps que la ligne 4 ou la ligne 5.
- **VT-3 : tenu.** Ligne 77 : « en cas d'écart non déclaré ou d'omission […] font foi ; les écarts déclarés (Plan d'analyse, « Écarts déclarés », 1 à 3) et les lignes propres à cette étape (Critères de lecture gelés) priment dans leur seul domaine ».
- **VT-4 : tenu.**
  - Ligne 89 : « Pour une issue absente et pour un fichier sans sceau, c'est le comportement […] ; pour une issue double et pour des statuts en désaccord avec les fichiers, ce sont des gardes neuves du lecteur […], plus strictes que `charger_pilote` […] (R-165) ».
  - R-165 est une ligne nouvelle (`registres/decisions.md:302`). R-164 (ligne 301) n'a pas été réécrite : ajoutée au commit 0090f02, intacte au commit 2cc1345.
  - La description de `charger_pilote` au commit 2660b07 est exacte : il lit les deux fichiers, prend d'abord l'empreinte du résumé et ne lit aucun statut.
- **VT-5 : tenu.** Ligne 100 : « dont au moins 300 s d'attentes fixes […] Deux mesures […] 1 224,61 s […] et 1 072,50 s […] une marge d'environ 290 à 410 s ». Les deux journaux sont cités avec leurs empreintes et leurs lignes.
- **VT-6 : tenu.**
  - Ligne 101 : « compté après le clonage (14 s au pilote, de la ligne « AMORCE » au début du script) » ; « environ 286 s (26 400 − 25 800 − 300 − 14) » ; « 42 s au pilote » rattaché au démarrage du conteneur.
  - La justification du seuil, « 17 700 − 16 200 s depuis la création, Z-5 », est conforme au texte gelé du pilote (ligne 173 : « que si le run démarre dans les 1 500 s après la création »).
- **VT-7 : tenu, avec une réserve** (constat neuf 2). Ligne 131 : « à aucun prix au-dessus d'environ 0,74 USD de l'heure (6 h × prix ≤ 10 − 7,5 h × prix ; […]) ».
- **VT-8 : tenu.**
  - Ligne 138 : « étape, motif, durée du run et, pour chaque juge commencé, statut, lots et lots faits (durée et mémoire pour un juge fini seulement ; aucun juge pour un arrêt avant les notations). Fenêtres déclarées sans `arret.json` : […] Fenêtres avec un `arret.json` en désaccord avec les fichiers : […] ».
  - Conforme au code : `noter_pilote_a.py:210-222`, 277, 295-296.
- **VT-9 : tenu.** Ligne 82 : « Les formats des deux juges sont contrôlés égaux […] au début du run, après le manifeste (étape « contrôle du format ») ».
- **VT-10 : tenu.**
  - Ligne 84 : « (état des lieux, `plan.md`, `61f78ad5…`, section « Devis ») ».
  - Ligne 93 : « (état des lieux, `plan.md`, « Devis », `61f78ad5…` ; critique adverse, constat 7, `17767964…` ; GO-2026-10-12-02) ».
  - Ligne 100 : création, « AMORCE », début et « run : » rattachés à des traces empreintées.
  - Vérifié dans les sources :
    - la section « Devis » de `plan.md` (lignes 185-200) porte 12 000 s, 400 min, 430 min, 26 400 s et 7,5 h ;
    - le constat 7 de la critique (lignes 63-70) porte 23 100 s.
- **VT-11 : tenu.** Ligne 85 : « les 20 dernières du journal, et les 20 dernières de `tests.txt` et de `tests.err` ». C'est bien ce que fait `amorce_instance_t05_notations.sh:51-54`.
- **VT-12 : tenu.** Ligne 117 : « toute autre garde de la lecture (Liste d'arrêt, « À la lecture » : désalignement, modules, rattachements, issue, préenregistrement, graines) | arrêt de la lecture ; nœud ; proposition à Lazar ; une garde de procédure seulement (arbre non propre, identifiant du run de lecture déjà pris) se corrige […] ». Un recouvrement avec la quatrième ligne reste : voir le constat neuf 1.
- **VC-1 (côté texte) : tenu.**
  - Ligne 138 : « signal reçu pendant la création du manifeste ou juste après, avant l'entrée dans le bloc qui consigne l'arrêt (l'état du run est calculé avant le manifeste : plus rien ne s'exécute entre les deux) ».
  - Conforme à `noter_pilote_a.py:208-217` au commit 259cf5e.
- **VC-2 (côté texte) : tenu.** Ligne 138 : « durée et mémoire pour un juge fini seulement ». C'est le code : `duree_s` et `memoire_pic_gio` ne sont posés qu'après la boucle des lots, lignes 295-296.

#### Constats neufs

**1. Une issue écrite sans sceau tombe hors de la ligne vers laquelle la Liste d'arrêt la renvoie (mineur)**
- **Lieu :** `brouillons/T0.5-pilote-notations-v1-candidat3.md:138`, avec :113 et :117.
- **Constat :**
  - La ligne 138 range « exception ou signal pendant la consignation de l'arrêt » parmi les « Fenêtres déclarées sans `arret.json` ». Elle conclut : « Toutes se lisent par la table (quatrième ligne) ».
  - Or `ecrire_resultat` écrit le fichier avant de le sceller (`manifeste.py:137-138`). Une interruption entre les deux laisse un `arret.json` présent mais sans sceau.
  - Le lecteur s'arrête alors dans `verifier_resultat` (`lire_notations_pilote.py:91`). La quatrième ligne ne nomme pas ce cas : elle ne vise que le « fichier de notations présent sans sceau conforme ». Le cas tombe donc sous la ligne neuve 117, au mot « issue ». Cette ligne prescrit « arrêt de la lecture ; nœud ; proposition à Lazar », sans le renvoi à « Relancement » de la quatrième ligne.
  - Même endroit, autre point : l'intitulé « Fenêtres avec un `arret.json` en désaccord avec les fichiers » couvre aussi « TERM pendant ou après l'écriture du résumé ». Ce cas donne une issue double, non un désaccord, même s'il aboutit bien à la quatrième ligne par « ou avec les deux ».
  - Effet pratique nul : nœud pour les deux juges dans tous les cas, et le paragraphe « Relancement » s'applique de lui-même.
- **Correction :** ajouter à la quatrième ligne « ou issue (`resume.json` ou `arret.json`) sans sceau conforme », et intituler « Fenêtres avec un `arret.json` en désaccord avec les fichiers ou en double avec le résumé ».

**2. Le seuil de 0,74 USD de l'heure suppose le même prix aux deux lancements, sans le dire (mineur)**
- **Lieu :** `brouillons/T0.5-pilote-notations-v1-candidat3.md:131`.
- **Constat :** « ne sont donc relançables à aucun prix au-dessus d'environ 0,74 USD de l'heure (6 h × prix ≤ 10 − 7,5 h × prix ; …) ». Ce n'est vrai que si les deux lancements ont le même prix. La phrase qui précède nomme « prix » le prix de l'offre du relancement.
- **Preuve :**
  - Premier lancement à 0,80 USD de l'heure pendant 7 h : 5,60 USD.
  - Relancement à 0,55 USD de l'heure : 5,60 + 7,5 × 0,55 + 0,5 = 10,225 ≤ 10,5. La condition (iii) est satisfaite, avec un premier prix au-dessus de 0,74.
  - Le texte écrit lui-même que « le filtre de l'offre n'a pas de prix plancher ».
  - La condition reste gardée par le lanceur ; seule la portée déclarée est surévaluée.
- **Correction :** écrire « à aucun prix au-dessus d'environ 0,74 USD de l'heure si les deux lancements ont le même prix (en général : 6 h × prix du premier + 7,5 h × prix du relancement ≤ 10) ».

**3. Coquille typographique (mineur, forme)**
- **Lieu :** `brouillons/T0.5-pilote-notations-v1-candidat3.md:82`.
- **Constat :** « relevé seulement dans les traces) . Les formats » : une espace avant le point.
- **Correction :** « traces). Les formats ».

#### Vérifications faites

- **Candidats et différentiel :**
  - Empreinte du candidat 2 : efa4b68a…, égale à celle citée ligne 3.
  - Les copies du bloc-notes sont identiques aux fichiers du dépôt, et le différentiel fourni est exactement celui des deux candidats.
- **Empreintes, recalculées et égales aux sceaux compagnons :**
  - le journal de la suite au commit 259cf5e (1fd7d5e1…) ;
  - `controles-avant-depense-S-v1.log` (64583e18…) et `repetition-jouet-pilote-v1.log` (531f2d79…) ;
  - `lancement.txt` (692aea4c…) et `journal-5min.txt` (7376e723…) ;
  - `journal.txt` (19c8b883…) et `tests.txt` (cfc1ee96…) ;
  - `plan.md` (61f78ad5…) et `critique.md` (17767964…).
- **Scripts de l'instance :**
  - l'amorce (c7511902…) et le script de l'instance (2106eade…) sont égaux sur disque et au commit 259cf5e ;
  - rien n'a changé dans `src/`, `tests/` ni `scripts/` entre 259cf5e et HEAD ;
  - entre 2660b07 et 259cf5e, sept fichiers ont été ajoutés et aucun modifié.
- **Lignes citées :**
  - ligne 61 du journal des contrôles : « 689 passed in 1224.61s » ;
  - ligne 12 de la répétition : « 689 passed in 1072.50s ». C'est le même code que 2660b07 : différence vide avec 7b07300 sur `src/`, `tests/` et `scripts/` ;
  - journal de la suite : première ligne 259cf5e9…, dernière ligne avant « code 0 » : « 762 passed in 1444.88s (0:24:04) ».
- **Horodatages :**
  - création 1791801313 = 10:35:13 UTC ; « AMORCE » 10:35:55 ; début 10:36:09 ; « run : » 10:51:25 ;
  - d'où 930 s, 972 s, 14 s et 42 s ;
  - tests 801,48 s.
- **Calculs refaits :**
  - (801,48 − 235) / (1 224,61 − 235) = 0,572 et (801,48 − 235) / (1 072,50 − 235) = 0,676 ;
  - tests attendus 964 s et 1 081 s. Avec 0,68 tel qu'écrit, on obtient 1 085 s : écart d'arrondi de 5 s, sans effet ;
  - mise en place d'environ 1 093 à 1 210 s, marge de 290 à 407 s ;
  - 286 s ; 1 500 s ; 2 400 s ; 0,7407 USD de l'heure ; 0,25 et 1,83 USD.
- **Nombre de tests :** 762 = 760 + 2 nouvelles paramétrisations (« prereg-rescelle », « prereg-hors-du-depot »). Tests non exécutés : torch et pytest sont absents de cet environnement.
- **Intitulés de citation :** les 14 figurent chacun exactement une fois sous la forme « <intitulé> : ` ».
- **Chaîne de lancement :** le brouillon 4 est cohérent avec les ajouts de la ligne 123 (`lancer_notations_v1.sh:94-115`, contrôles lignes 199-205, récupération ligne 56).
- **Registres et décomptes :**
  - R-147, R-164 et R-165 sont cités fidèlement ;
  - les décomptes du premier tour, ligne 158, sont exacts : 3 majeurs et 9 mineurs ; 5 mineurs ; 1 majeur et 9 mineurs.
- **Non vérifiable :**
  - que les trois mesures sur la session aient été prises sur le même processeur ;
  - `docs/procedures/notations-T0.5-v1/verification-courte-candidat-v1.md` est absent aujourd'hui (constaté par `ls`). Le texte écrit qu'il « est versé » : il devra exister avant le scellement.

Je n'ai modifié aucun fichier du dépôt ni du bloc-notes, je n'ai lu ni `episodes-defaut.json` ni `chemin-defaut.json`, et je n'ai fait ni accès réseau ni appel à vastai. Mes fichiers de travail (différentiel mot à mot, script de découpage) sont dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/vc2/agent-texte/`.

### Rapport — code, `20da280` → `259cf5e`

**Verdict : conforme avec réserves.** Les cinq constats du premier tour sont tenus. Je n'ai trouvé aucun défaut bloquant ni majeur. Restent quatre constats mineurs : deux sur des tests qui ne prennent pas un mutant, deux sur la précision du texte.

#### Constats du premier tour

- **VC-1 : tenu.**
  - Code : à 259cf5e, `etat` et `debut` sont calculés avant `creer_manifeste` (`noter_pilote_a.py:210-216`).
  - Désassemblage sous Python 3.11.17 : entre l'appel `creer_manifeste` et la zone protégée par le `try`, seules s'exécutent quatre instructions (`UNPACK_SEQUENCE`, deux `STORE_FAST`, `NOP`). Aucune n'exécute de code Python ni ne traite un signal en attente. La zone protégée couvre les octets 1250 à 1290.
  - Seul reste le point de contrôle de fin de l'appel lui-même : c'est la fenêtre « pendant la création du manifeste ou juste après » que nomme le candidat 3 (ligne 138).
  - Preuve sur 259cf5e : le contrôle v5 du premier tour (signal TERM levé dans `empreinte_config`) ne laisse plus de manifeste. Mon contrôle « ordre » relève, dans cet ordre, `empreinte_config`, `perf_counter`, `creer_manifeste`, `_apres_manifeste`.
  - Preuve sur le mutant qui rétablit l'ordre de 20da280 : manifeste présent sans `arret.json`. Mon contrôle « fenêtre résiduelle » (signal juste après le retour de `creer_manifeste`) laisse un manifeste sans `arret.json` aux deux commits, comme déclaré.
  - Aucun test du dépôt ne garde ce traitement : voir le constat neuf 1.
- **VC-2 : tenu.** Ligne 138 du candidat 3 : « durée et mémoire pour un juge fini seulement ; aucun juge pour un arrêt avant les notations ».
  - Mon contrôle (8B écrit, signal TERM pendant le 3B) relève dans `arret.json` : pour le 3B, seulement `lots`, `lots_faits`, `statut` ; pour le 8B, en plus `duree_s` et `memoire_pic_gio`. C'est conforme au texte.
  - L'énumération reste incomplète : voir le constat neuf 3.
- **VC-3 : tenu.** Les deux assertions ajoutées (`test_lire_notations_pilote.py:330-331` : deux décompositions concluantes, aucun déclencheur ni lecture suspendue) passent sur 259cf5e.
- **VC-4 : tenu.** Chacune des trois branches a maintenant un artefact, et chaque artefact prend son mutant :
  - (a) `prereg-rescelle` prend le mutant qui retire `or pr.get("sha256") != sha` (ligne 78) : « DID NOT RAISE ».
  - (b) l'issue sans sceau conforme prend le mutant qui lit `resume.json` sans `verifier_resultat` (ligne 91) : « DID NOT RAISE », test ligne 213.
  - (c) `("resume", {"3B": "écrit"})` prend le mutant au désaccord à sens unique (ligne 123) : « DID NOT RAISE », test ligne 204, quatrième cas. Les statuts gardent bien le 8B « écrit » (`juges.update`, ligne 76 du test), donc le désaccord ne vise que le 3B.
- **VC-5 : tenu.** La garde lève maintenant `GardeArret` « … hors du dépôt » (`lire_notations_pilote.py:68-71`). Le mutant qui retire le `try` fait échouer `prereg-hors-du-depot` avec une `ValueError`. Le cas sain reste `test_lecture_decisive_cas_sain`, qui passe un chemin absolu dans le dépôt. Un mutant plus fin survit au test : voir le constat neuf 2.

#### Constats neufs

1. **Mineur : le traitement de VC-1 n'est gardé par aucun test.**
   - Lieu : `src/controle_ia/environnements/noter_pilote_a.py:208-216` et `tests/test_noter_pilote_a.py`.
   - Constat : le mutant qui rétablit l'ordre de 20da280 (manifeste, puis `debut` et `etat`) passe les 36 tests de `test_noter_pilote_a.py`.
   - Preuve : 36 passent en 386,6 s (`journaux/m-vc1-lanceur.txt`). Ce fichier de tests et le reste de `src/` sont inchangés de 20da280 à 259cf5e : le journal `T0.5-notations-suite-20da280-v1.txt` (760 passés) le confirme pour toute la suite. Mes trois contrôles prennent le mutant (`journaux/m-vc1.txt`, 3 échecs).
   - Correction proposée : ajouter un test qui remplace `npa.empreinte_config` par une fonction exigeant que `runs/<run>` n'existe pas encore, ou qui vérifie l'ordre des appels.
2. **Mineur : le motif de l'artefact `prereg-hors-du-depot` ne distingue pas la garde neuve de la garde gelée de `creer_manifeste`.**
   - Lieu : `tests/test_lire_notations_pilote.py:228` ; garde `lire_notations_pilote.py:68-71`.
   - Constat : un mutant remplace la levée par `return`, ce qui saute en silence toutes les vérifications de la lecture décisive. Il passe le test, parce que la lecture va jusqu'à l'écriture et `creer_manifeste` lève « préenregistrement … hors du dépôt <racine> ». L'arrêt final reste sûr (aucune lecture écrite), mais le test n'éprouve pas la garde neuve.
   - Preuve : `journaux/m-vc5b.txt` (2 passés). Mon contrôle d'origine (`journaux/m-vc5b-origine.txt`, `obs-m-vc5b.json`) montre que, sur le mutant, `creer_manifeste` est appelé et que le message nomme la racine. Sur 259cf5e (`journaux/base-vc5b.txt`), `creer_manifeste` n'est pas appelé.
   - Correction proposée : prendre le motif `"hors du dépôt$"`, ou exiger dans le test que `creer_manifeste` ne soit jamais appelé.
3. **Mineur (texte) : le contenu d'`arret.json` est énuméré comme exact, mais l'énumération est incomplète.**
   - Lieu : candidat 3, ligne 138 ; code `noter_pilote_a.py:220-222` et `:302-305` ; ligne VT-8 du traitement (« contenu exact »).
   - Constat : `partiel` porte aussi `commit_cite`, `config_sha256`, `episodes_sha256`, `run_pilote`, `taches_sha256`, `reglages` et `precharges`. Pour un juge écrit, il porte aussi `jetons_generes`, `notations` et `completes`. Le texte n'en dit rien.
   - Preuve : `obs-base.json`, clé `arret_8b_ecrit_3b_en_cours` (`journaux/base-arret.txt`, 1 passé).
   - Correction proposée : ajouter « citations, réglages, préchargements ; pour un juge écrit, jetons, notations et réponses complètes », ou écrire « notamment ».
4. **Mineur (texte) : depuis VC-5, l'arrêt « hors du dépôt » a lieu à la lecture, alors que le texte le range à l'écriture.**
   - Lieu : candidat 3, ligne 139 (« à l'écriture : … préenregistrement non scellé ou hors du dépôt ») ; code `lire_notations_pilote.py:68-71`.
   - Constat : un chemin absolu hors du dépôt arrête maintenant dans `exiger_run_sous_prereg`, avant tout calcul. La formule fourre-tout du texte (« toute autre garde du lecteur ») couvre ce cas, mais le texte le place mal.
   - Preuve : sur 259cf5e, `creer_manifeste` n'est pas appelé (`obs-base.json`, clé `vc5b`).
   - Correction proposée : ajouter « préenregistrement hors du dépôt » à la liste de la lecture décisive.

#### Vérifications faites

- **Différentiel :** le fichier fourni est identique à `git diff 20da280 259cf5e -- src tests scripts`. Il touche trois fichiers, aucun script. 762 = 760 + 2 cas paramétrés neufs, ce qui concorde avec le journal de 259cf5e. Son sceau est conforme (`1fd7d5e1…`).
- **Durée du run :** elle reste juste.
  - `debut` est pris juste avant `creer_manifeste`, donc la durée consignée inclut la création du manifeste : 0,019 à 0,022 s mesurées sur le dépôt jouet.
  - Les échéances du 8B et l'échéance globale sont donc ancrées plus tôt de ce même écart, ce qui va dans le sens prudent. Le lanceur du pilote prenait `debut` après le manifeste (`lancer_pilote_a.py:297-300`). Le texte dit « depuis le début du run ».
  - Mon contrôle « ancrage » (horloge avancée de 2 000 s pendant `creer_manifeste`, échéance du 8B à 1 500 s) donne « échu » et une durée de 2 018,4 s sur 259cf5e. Sur l'ancien ordre, il donne « écrit » et 36,6 s.
- **Tests lancés sur 259cf5e** (`journaux/base.txt`) : 14 passés en 121 s. Ce sont mes 5 contrôles, `test_issue_du_run…`, les 6 cas de `test_lecture_decisive_exige…`, `test_equivalence_avec_analyser_sur_le_meme_pilote` et `test_lecture_decisive_cas_sain`. S'y ajoutent `base-arret.txt` (1 passé) et `base-vc5b.txt` (1 passé).
- **Mutants :** cinq pris, deux survivants.

| Mutant | Effet | Sort |
|---|---|---|
| m-vc1 | ordre de 20da280 rétabli | survit aux 36 tests du dépôt ; pris par mes contrôles |
| m-vc5 | `try` retiré | pris (`ValueError`) |
| m-vc5b | garde sautée en silence | survit au test du dépôt ; pris par mon contrôle |
| m-vc4a | moitié « empreinte » retirée | pris |
| m-vc4b | issue lue sans vérifier le sceau | pris |
| m-vc4c | désaccord dans un seul sens | pris |

- **Remarque non remontée :** le docstring de `noter_pilote_a.py:24-26` liste encore seulement trois fenêtres sans `arret.json`. Il n'a pas changé dans le différentiel.
- **Dépôt :** je n'ai modifié aucun fichier ; `git status` est vide. Le dépôt est passé à `e39b3fb` pendant mon travail, sans moi.
- **Fichiers de travail**, sous `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/vc2/agent-code/` :
  - `arbre/` (259cf5e) et `arbre-20da280/` : extractions ;
  - `base/` et `m-*/` : copies et mutants ;
  - `verif/` : `test_zz_vc2.py`, `test_zz_vc2_arret.py`, `test_zz_vc5b.py`, `dis_executer.py`, `muter.py`, `lancer.sh` ;
  - `journaux/` : sorties des tests et observations `obs-*.json`.

### Rapport — chaîne, brouillon 3 → brouillon 4

**Verdict : conforme avec réserves.** Les dix constats du premier tour sont traités dans le brouillon 4. Je n'ai trouvé aucun défaut bloquant ni majeur. Cinq constats neufs sont mineurs ; deux d'entre eux manquent à R5 (un changement de garde sans épreuve). Comme les scripts sont figés au commit C1, mieux vaut les corriger avant lui.

#### Constats du premier tour

- **VH-1 : tenu.**
  - Le bloc du cas sain P00 est maintenant compté (`essais_lanceur:162`, `|| { …; NON_CONFORMES+1; }`). Il lit « plafond de la surveillance N (création + 26400 s ; … <id> C <dossier neuf>) ». Il exige N − création = 26 400 et C = création.
  - L'en-tête est corrigé (ligne 5). Les contrôles relient `PLAFOND_SURVEILLANCE_S` (`controles:251`), avec l'artefact A44c.
  - Preuve, cas sain : banc rejoué, toutes les vérifications à vrai.
  - Preuve, artefact : avec un lanceur réglé à `PLAFOND_SURVEILLANCE_S=20000`, le banc sort en code 1. P00 affiche « … : False » et « P00 : vérifications du cas sain : NON CONFORME », puis « cas non conformes : 1 ».
  - A44c n'est pas jouable. J'ai joué son expression à part : elle rend `['20000']` sur la copie fautive et `['26400']` sur le brouillon 4.
  - Réserve sur la vérification de l'étiquette : voir le constat neuf 3.
- **VH-2 : tenu.**
  - Le module refuse toute ligne qui contient « NON CONFORME » ou qui commence par « Traceback » ou « JETON AFFICHÉ » (`verifications:156-159`).
  - Le banc du lanceur compte le jeton affiché (lignes 398-399). Le verdict de la répétition finale dépend du scellement conforme (lignes 54-55 et 67). Bancs : P30g (lanceur), P01 à P03 (contrôles).
  - Preuve : je refais l'essai du premier tour (Traceback, JETON AFFICHÉ, « P13c … NON CONFORME », « scellement : NON CONFORME », trace indentée). Chaque ajout donne maintenant le code 1.
  - Les journaux réels conformes passent toujours (code 0, voir « Vérifications faites »).
- **VH-3 : tenu.**
  - `sceller:52-55` lit toutes les adresses avec `get-url --all`.
  - J'ai joué la garde seule sur des dépôts nus locaux. Le cas sain est accepté. Sont refusés : deux adresses de poussée, deux adresses de lecture, `pushInsteadOf` et `insteadOf` vers la copie publique simulée. Celle-ci reste vide.
- **VH-4 : tenu.** `essais_scellement:237-248` emploie un dépôt nu local et vérifie qu'il reste vide (`vide`) après S39, S39b et S39c. `remise` retire toutes les adresses de poussée. Le banc ne contient plus aucune adresse réelle (seule la garde `grep github` de la ligne 31 la nomme).
- **VH-5 : tenu.**
  - Le lanceur (`lancer:98-111`) exige trois choses : la copie versée à HEAD sous `traces/t05-notations-releve-<instance de la ligne R-…>/`, son sceau à la ligne exacte, et une ligne `AMORCE … : commit <S>`.
  - Ce format est celui de l'amorce (`scripts/amorce_instance_t05_notations.sh:24`). Le sceau a le format de `controle_ia.scellement` (`{h}  {nom}`).
  - Cas P13i, P13j, P13q, P13r et P13s : conformes au journal rejoué.
  - Le plan donne un seul emplacement (lignes 99-103 et 124-128), et le candidat 3 dit la même chose.
- **VH-6 : tenu.**
  - `lancer:122-128` compare treize scripts, les mêmes que la liste CHAINE du scellement (`sceller:60-63`, comparées nom à nom). Cas P31.
  - Remarque : la liste du lanceur est une copie de CHAINE. Elle est égale aujourd'hui, mais n'est pas lue dans CHAINE.
- **VH-7 : tenu.**
  - `lancer:166-169` appelle le module `go`.
  - Preuve : le candidat 3 avec les registres réels donne « GO-2026-10-12-02 (R-160) conforme ».
  - Avec la ligne « - Décision de Lazar sur N-021 : retirée par Lazar (essai) » ajoutée : le module rend le code 1, et le bloc du lanceur joué à part s'arrête avec ce message.
- **VH-8 : tenu.** L'assertion littérale est retirée (`controles:252-253`). Il reste un commentaire périmé qui dit « 240 s » (constat neuf 5).
- **VH-9 : tenu.**
  - P30h, P30i et P30j atteignent chacun leur refus (journal, lignes 242-247).
  - M08 et M09 sont conformes au banc rejoué. M08 est exactement le cas que demandait le premier tour.
  - Z2f, joué à part : code 2, « …suite.txt existe déjà (R12) », et rien n'est créé.
  - Réserve : M08 ne prouve pas le « de suite » (constat neuf 2).
- **VH-10 : tenu dans le code, épreuve incomplète.**
  - `controles:200` et `recuperation:56` lisent aussi `run.err`. Le chemin correspond à celui des traces de l'instance (`notations_t05_instance.sh:142-143`, un seul niveau sous `traces/`).
  - A48d éprouve les contrôles ; je l'ai émulé : KO attendu.
  - La récupération n'a aucun artefact (constat neuf 1).

#### Constats neufs

**1. La récupération lit `run.err` sans aucun artefact (R5)**
- Gravité : mineur.
- Lieu : `recuperation_notations_v1.sh:56` ; `repetition_jouet_notations_v1.sh:166-174` ; `verifications_notations_v1.py:81-86`.
- Constat : le traitement cite le banc A48d, mais il n'éprouve que les contrôles. Dans la répétition jouet :
  - l'artefact g n'écrit que dans `journal.txt` ;
  - l'artefact « relance après notations » prend d'abord le KO « notations », ce qui masque la lecture des traces.

  Une régression de l'expression qui lit `run.err` passerait donc inaperçue.
- Preuve :
  - `run.err` apparaît 0 fois dans la répétition jouet, dans le constructeur et dans le module.
  - Lignes 54-62 jouées à part sur un mini-dépôt dont la branche `-v1` n'ajoute que `run.err`, avec une ligne `fin=` : le brouillon 4 donne « KO 0 », l'expression du brouillon 3 donne « OK 0 ».
- Correction proposée : ajouter à la répétition jouet un artefact dont seul `run.err` porte la ligne du dernier lot (un seul KO, 0), et l'inscrire dans `ARTEFACTS` et dans le plan (étape 0.4).

**2. Banc de la surveillance : M08 ne prouve pas « vu deux fois de suite »**
- Gravité : mineur.
- Lieu : `essais_surveillance_notations_v1.sh:85-88` ; `surveiller_notations_v1.sh:79`.
- Constat : M08 montre qu'un seul état hors ligne ne suffit pas. Il n'éprouve pas la remise à zéro du compteur quand l'instance revient en marche.
- Preuve :
  - Avec une surveillance sans `*) terminal=0 ;;`, le banc passe quand même : code 0, « cas non conformes : 0 ».
  - Scénario hors ligne, en marche, hors ligne, en marche, puis fin : la surveillance du brouillon 4 sort sur « FIN … » ; la surveillance mutée sort sur « ÉTAT TERMINAL ».
- Correction proposée : ajouter le cas sain M08b, qui joue ce scénario alterné et attend « FIN ».

**3. Banc du lanceur : étiquette et branche de la relance affichées, jamais comptées ; étiquette du cas sain vérifiée par sous-chaîne**
- Gravité : mineur. Le défaut existait avant le brouillon 4 ; c'est le même motif que VH-1.
- Lieu : `essais_lanceur_notations_v1.sh:266` et `:167`.
- Constat : rien ne compte une relance lancée sur la branche `-v1`. La garde PREREG/BRANCHE du lanceur l'accepte, puisque la ligne « Lancement » cite les deux branches.
- Preuve :
  - Lanceur muté (relance avec `BRANCHE=…-v1`, étiquette `t05-notations-v1`) : banc en code 0, P13c et P13f CONFORME. Seules les lignes affichées 157-158 montrent `-v1`.
  - `"etiquette t05-notations-v1" in "etiquette t05-notations-v1-relance"` vaut True : une étiquette de relance passerait le cas sain.
- Correction proposée :
  - pour P13c, compter l'étiquette exacte `t05-notations-v1-relance` et `env BRANCHE=calcul/t05-notations-reel-v2` ;
  - pour P00, comparer la ligne d'étiquette entière.

**4. Les preuves des essais ne sont lues par le module qu'au lancement, après S**
- Gravité : mineur. Le défaut existait déjà ; le filtre élargi du brouillon 4 en accroît la portée.
- Lieu : plan, préalable 6 (lignes 59-67) ; `lancer:132-146`. Ni le scellement ni les contrôles ne lisent les preuves.
- Constat : un journal versé que le module refuse ne se découvre qu'à la création. Or toute correction après S est un écart (nœud).
- Preuve : `banc-lanceur-7.log`, tel que fourni avec les lignes `real/user/sys` et « code 0 » de l'enveloppe `time`, rend `preuves` en code 1 : « dernière ligne ≠ … ».
- Correction proposée : au commit C2, avant le scellement, jouer `python3 -I verifications_notations_v1.py preuves` sur les cinq journaux versés, avec la comparaison aux copies versées, et le consigner dans la ligne R-… des préalables. Préciser aussi que les journaux versés sont la sortie brute redirigée.

**5. Commentaires périmés dans des scripts figés à C1**
- Gravité : mineur.
- Lieux et constat :
  - `controles:244-245` dit encore « démarrage du conteneur d'au plus 240 s ». Cela contredit les lignes 252-253 et le texte du candidat 3, « Marges » (environ 286 s), et plus aucune assertion ne le porte.
  - `lancer:17-18` et `:119` parlent de « contrôles, module commun et lanceur » et de « (contrôles, lanceur) », alors que la boucle compare treize scripts.
  - `essais_lanceur:6` dit « lanceur et contrôles égaux… ».
  - Le titre du plan (ligne 1) porte encore « (brouillon 3) ».
  - `controles:200` a perdu son indentation (sans effet).
- Preuve : lecture des lignes citées.
- Correction proposée : mettre ces commentaires à jour avant C1.

#### Vérifications faites

- **Différentiel et copies** :
  - Le différentiel recalculé par `git diff --no-index` entre les brouillons 3 et 4 est identique au fichier fourni.
  - Les 14 empreintes du brouillon 4 sont conformes.
  - Le bloc-notes de pilotage est identique au brouillon 4 (14 fichiers).
  - `bash -n` passe sur les 11 scripts bash, et le module se compile.
- **Banc du lanceur rejoué** (faux outil de location, aucun service appelé) : code 0, « cas non conformes : 0 ». Le journal est identique à `banc-lanceur-7.log`, aux chemins et au commit S près.
- **Bancs mutés** :
  - plafond à 20 000 s : code 1, échec compté (VH-1) ;
  - relance sur `-v1` : code 0 (constat 3).
- **Banc de la surveillance rejoué** : code 0, 11 cas conformes. Avec la surveillance mutée : code 0 (constat 2).
- **Module `preuves`** :
  - Le journal réel du lanceur et celui de la surveillance, plus des journaux synthétiques portant les empreintes du brouillon 4, donnent le code 0. Aucune ligne d'un banc conforme ne fait échouer le filtre ; la ligne « | … Traceback » de P30g passe parce qu'elle est préfixée.
  - Chaque ligne d'échec ajoutée donne le code 1. « non conforme » en minuscules et « | Traceback » donnent le code 0, comme voulu.
  - Le bloc « preuves » du banc des contrôles (lignes 258-284), joué à part, est conforme : 0 non conforme. Avec un module privé de son filtre : 3 non conformes.
- **Module `go`, garde d'adresse, Z2f, A44c et A48d** : joués à part ; résultats donnés plus haut.
- **Non joués (consigne)** : bancs des contrôles et du scellement, répétitions jouet et finale. La répétition jouet devra être rejouée avec la récupération du brouillon 4 (`e67fda58…`) ; sinon les contrôles refuseront « script répété ≠ copie versée ».
- **Sûreté** : aucun fichier du dépôt ni du bloc-notes modifié (`git status` vide, empreintes du brouillon 4 conformes après le travail). Aucun appel à vastai, aucun accès réseau, aucun jeton affiché.
- **Fichiers de travail** : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/vc2/agent-chaine/`. On y trouve :
  - les copies `b4/` (brouillon 4) et `b4-plafond`, `b4-surv-mut`, `b4-branche`, `b4-sans-filtre` (copies mutées) ;
  - les journaux `banc-lanceur-sain.log`, `banc-lanceur-plafond.log`, `banc-lanceur-branche.log`, `banc-surv-sain.log`, `banc-surv-mut.log` ;
  - les dossiers d'essai `preuves-*`, `module-go`, `garde-adresse`, `z2f`, `a48d`, `recup-run-err`, `controles-preuves*` ;
  - `diff-recalcule.diff`.

### Traitement

Identifiants : WT (texte), WC (code), WH (chaîne), dans l'ordre des rapports ci-dessus. Les trois rapports tiennent
tous les constats du premier tour (VT-1 à VT-12, VC-1 à VC-5, VH-1 à VH-10) pour traités, VH-10 avec une épreuve
incomplète (WH-1).

| id | gravité | constat | traitement |
|---|---|---|---|
| WT-1 | mineur | issue écrite sans sceau hors de la quatrième ligne ; intitulé « en désaccord » trop étroit | candidat 4 : quatrième ligne « ou issue (`resume.json` ou `arret.json`) sans sceau conforme » ; fenêtre « consignation de l'arrêt » : un `arret.json` écrit mais pas encore scellé est une issue sans sceau conforme ; intitulé « en désaccord avec les fichiers ou en double avec le résumé » |
| WT-2 | mineur | seuil de 0,74 USD de l'heure : même prix aux deux lancements, non dit | candidat 4 : « si les deux lancements ont le même prix » et la forme générale (6 h × prix du premier + 7,5 h × prix du relancement ≤ 10 USD) |
| WT-3 | forme | espace avant un point | candidat 4 |
| WC-1 | mineur | ordre avant le manifeste gardé par aucun test | code `c63d4f1` : `test_etat_et_debut_du_run_avant_le_manifeste` (empreinte de la configuration jamais calculée après la création du dossier du run ; 2 000 s pendant la création du manifeste comptées dans l'échéance du 8B) ; mutant à l'ordre de `20da280` pris (`assert ([True] and not True)`) |
| WC-2 | mineur | motif de l'artefact « hors du dépôt » pris aussi par la garde de `creer_manifeste` | code `c63d4f1` : motif `hors du dépôt$` ; mutant qui saute la garde en silence pris (« Regex pattern did not match ») |
| WC-3 | mineur (texte) | contenu d'`arret.json` incomplet | candidat 4 : citations du run, réglages, juges préchargés ; pour un juge écrit, jetons, notations et réponses complètes |
| WC-4 | mineur (texte) | arrêt « hors du dépôt » rangé à l'écriture | candidat 4 : rangé à la lecture décisive ; retiré de l'écriture |
| — | remarque | docstring du lanceur : trois fenêtres seulement | code `c63d4f1` : les fenêtres du préenregistrement |
| WH-1 | mineur | lecture de `run.err` par la récupération sans artefact (R5) | répétition jouet : septième artefact (branche i-v1 : seul `run.err` porte la ligne d'un dernier lot ; relance : un seul KO, 0) ; module commun (`ARTEFACTS`), contrôles et plan : sept artefacts |
| WH-2 | mineur | surveillance : remise à zéro du compte hors ligne non éprouvée | banc de la surveillance : cas sain M08b (hors ligne, en marche, hors ligne, en marche, fin → « FIN ») ; mutant sans remise à zéro pris (« ÉTAT TERMINAL », code 1 du banc) |
| WH-3 | mineur | étiquette et branche de la relance affichées, non comptées ; étiquette du cas sain par sous-chaîne | banc du lanceur : P13c compte l'étiquette exacte `t05-notations-v1-relance`, `env BRANCHE=calcul/t05-notations-reel-v2` et la ligne « branche » du lancement ; P00 : lignes entières (étiquette, branche, variable) |
| WH-4 | mineur | preuves des essais lues seulement au lancement, après S | plan, préalable 6 : journaux versés = sortie brute redirigée ; avant le scellement, au commit C2, `verifications_notations_v1.py preuves` sur les cinq journaux versés et comparaison aux copies versées, consignées dans la ligne R-… des préalables |
| WH-5 | mineur | commentaires périmés | contrôles (240 s, indentation), lanceur (treize scripts), banc du lanceur (en-tête), plan (titre, durée de la suite, mise en place) |

## Tour 3

Un sous-agent neuf relit les trois différentiels du traitement du second tour, avec les rapports et la table de traitement du second tour, les journaux des bancs, de leurs mutants et de la répétition jouet à blanc ; il rejoue les bancs du lanceur et de la surveillance et leurs mutants. Interrompu par un redémarrage du conteneur, il a repris depuis sa transcription, ses fichiers de travail intacts.

### Rapport — texte, code et chaîne : candidat 3 → 4, `259cf5e` → `c63d4f1`, brouillon 4 → 5

**Verdict : conforme.** Le traitement règle les douze constats du second tour : je les tiens tous, preuves et mutants à l'appui. Les trois différentiels n'introduisent aucun défaut bloquant, majeur ni mineur, et n'ouvrent ni ne ferment à tort la porte du relancement. Il reste un point de forme dans le plan, qui se corrige sans nouveau tour.

#### Constats du second tour

- **WT-1 : tenu.**
  - Ligne 113 du candidat 4 : « … ou fichier de notations présent sans sceau conforme, ou issue (`resume.json` ou `arret.json`) sans sceau conforme ».
  - Ligne 138 : le texte précise « (un `arret.json` écrit mais pas encore scellé est une issue sans sceau conforme) » et l'intitulé devient « … en désaccord avec les fichiers ou en double avec le résumé ».
  - Le code dit la même chose. `ecrire_resultat` écrit le fichier, puis le scelle (`manifeste.py:137-138`), sans autre étape. `issue_des_notations` appelle `verifier_resultat` sur l'issue présente (`lire_notations_pilote.py:83-96`) et s'arrête donc sur une issue non scellée.
  - La quatrième ligne et la ligne « toute autre garde » se recouvrent encore, mais sans contradiction : aucune des deux ne dit « aucun relancement ».
  - Le relancement reste borné par la condition (ii). Une branche `-v1` qui porte un fichier de notations, une ligne de fin ou un dernier lot reste refusée.
- **WT-2 : tenu.**
  - Le texte écrit « si les deux lancements ont le même prix » et la forme générale « 6 h × prix du premier lancement + 7,5 h × prix du relancement ≤ 10 USD ».
  - Recalcul : 13,5 × prix ≤ 10, donc prix ≤ 0,7407 USD de l'heure.
  - La forme générale est bien une condition nécessaire tirée de (iii), avec une dépense engagée d'au moins 6 h × prix du premier.
  - Le contre-exemple du second tour (0,80 puis 0,55 : 4,80 + 4,125 = 8,925 ≤ 10) est maintenant couvert.
- **WT-3 : tenu.** Ligne 82 : « relevé seulement dans les traces). Les formats ».
- **WC-1 : tenu.**
  - `test_etat_et_debut_du_run_avant_le_manifeste` passe au commit c63d4f1 (1 passé, 114 s).
  - Trois mutants sont pris :
    - ordre de 20da280 rétabli : `assert ([True] and not True)` ;
    - début seul repris après le manifeste : 8B « écrit » au lieu de « échu » ;
    - état seul repris après le manifeste : `[True]`.
  - Le test ne peut pas passer à vide : `vu` doit être non vide.
- **WC-2 : tenu.** Le cas sain passe. Deux mutants de la garde (`lire_notations_pilote.py:71`) sont pris :
  - `return` : « Regex pattern did not match » ; le message vient de `creer_manifeste` et finit par la racine ;
  - `pass` : « … fichier absent sur disque ».
- **WC-3 : tenu.**
  - Champs de `arret.json` au commit c63d4f1 :
    - `etat`, lignes 211-213 : `commit_cite`, `run_pilote`, trois empreintes, `juges` ;
    - `reglages`, ligne 234, et `precharges`, ligne 252 ;
    - pour chaque juge, `lots`, `lots_faits`, `statut`, puis `duree_s` et `memoire_pic_gio` (296-297) ;
    - pour un juge écrit, `jetons_generes`, `notations` et `completes` (304-306).
  - Le texte de la ligne 138 les énumère tous.
  - Mon contrôle (`journaux/vc3-arret-ecriture-8b.txt`) relève les mêmes clés de `partiel`.
- **WC-4 : tenu.**
  - Ligne 139 : « lecture décisive (préenregistrement passé) : préenregistrement hors du dépôt ; » ; la mention est retirée de la liste « à l'écriture ».
  - Le code arrête bien à la lecture : `exiger_run_sous_prereg`, appelé par `charger_notations` (ligne 111), passe avant `creer_manifeste` (ligne 209).
- **Remarque sur la docstring : tenue.** `noter_pilote_a.py:24-27` liste maintenant les fenêtres du texte.
- **WH-1 : tenu.**
  - L'artefact i-v1 est ajouté (`repetition_jouet:194-203`), et le compte passe à sept dans `ARTEFACTS` (`verifications:87`), dans les contrôles (ligne 163) et dans le plan (étape 4).
  - Dans `rep-jouet-essai-4.log`, lignes 114-117, la récupération d'i-v1 donne un seul KO : « KO  0 … traces avec une ligne de fin de juge ou de dernier lot ».
  - b-v1 seule donne « OK 0 » (passage 4, lignes 53-54) : le KO vient donc du seul `run.err`.
  - Module `repetition` sur ce journal privé de sa ligne « code 0 » : code 0. Les trois empreintes répétées sont celles du brouillon 5.
  - Journaux synthétiques mutés :
    - une récupération qui ne lit pas `run.err` (artefact rendu conforme) donne le code 1, « ligne absente ou en double » ;
    - un KO à un autre contrôle donne le code 1 ;
    - deux KO donnent le code 1.
- **WH-2 : tenu.**
  - Banc de la surveillance rejoué : code 0, journal identique à `banc-surv-5.log` aux chemins près.
  - Mutant sans `*) terminal=0 ;;` (`surveiller:79`) : M08b est NON CONFORME (« ÉTAT TERMINAL »), le banc sort en code 1, et M08 reste conforme sous ce mutant. C'est donc bien M08b qui prend la remise à zéro.
- **WH-3 : tenu.**
  - Banc du lanceur rejoué : code 0, 276 lignes identiques à `banc-lanceur-8.log` aux chemins et commits près.
  - Trois mutants, chacun pris (code 1, un cas non conforme) :
    - relance sur `-v1` avec l'étiquette `t05-notations-v1` : « P13c : étiquette ou branche de la relance : NON CONFORME » ;
    - étiquette de relance « t05-notations-v1-relance-x » : même refus ;
    - premier lancement étiqueté « t05-notations-v1-relance » : P00 « étiquette : False ».
- **WH-4 : tenu.**
  - Plan, étape 6 : sortie brute redirigée ; avant S, au commit C2, `verifications_notations_v1.py preuves` et comparaison aux copies versées, consignées dans la ligne R-… des préalables.
  - C'est la même lecture que le lanceur (`lancer:129-147`).
  - `preuves` sur un dossier qui réunit mes deux journaux de bancs rejoués et trois journaux synthétiques : code 0, dix scripts aux empreintes du brouillon 5. Aucune ligne neuve des bancs (« P13c … : CONFORME », « M08b … ») n'est refusée.
  - Avec le journal de la surveillance mutée à la place : code 1.
- **WH-5 : tenu.**
  - Contrôles : lignes 244-245 « (marge : voir plus bas) », renvoi au commentaire des « 286 s » des lignes 252-253 ; ligne 200 réindentée.
  - Lanceur : lignes 17-18 et 119.
  - Banc du lanceur : ligne 6.
  - Plan : titre « (brouillon 5) », durée de la suite, réserve sur la mise en place.

#### Constats neufs

1. **Forme. `plan-lancement-notations-v1.md:82`.**
   - Constat : « environ 24 minutes pour la suite au code relu ». Or la mesure citée est 1 491,03 s, soit 24 min 51 s (`brouillons/T0.5-notations-suite-c63d4f1-v1.txt`, d4a32162…, « 763 passed in 1491.03s (0:24:51) »).
   - Correction proposée : écrire « environ 25 minutes ».

Je n'ai trouvé aucun autre défaut dans les différentiels :
- aucune contradiction dans le texte ;
- les chiffres et empreintes sont justes (voir plus bas) ;
- aucun test neuf ne passe sur les mutants essayés ;
- aucun cas de banc n'est compté conforme sans vérification ;
- aucune ligne neuve ne fait refuser un journal conforme.

#### Vérifications faites

- **Différentiels.** Je les ai recalculés : texte (`git diff --no-index`), chaîne (brouillon 4 → 5) et code (`git diff 259cf5e c63d4f1 -- src tests scripts`). Les trois sont identiques aux fichiers fournis.
- **Empreintes :**
  - les 14 du brouillon 5 sont conformes, et le bloc-notes est égal au brouillon 5 ;
  - le candidat 3 donne 5df4f082… ; le candidat 2, le candidat 1 et le brouillon 1 sont conformes à l'en-tête ;
  - le candidat 4 donne 6d408c78… ;
  - le journal de la suite donne d4a32162…, égal à son sceau ; la dernière ligne avant « code 0 » est « 763 passed in 1491.03s (0:24:51) » ;
  - l'amorce (c7511902…) et le script de l'instance (2106eade…) sont égaux au commit c63d4f1 ;
  - les six journaux de la mise en place sont conformes aux empreintes citées : ligne 61 = 1224.61 s, ligne 12 = 1072.50 s, tests 801.48 s, création 1791801313 = 10:35:13 UTC.
- **Calculs refaits :**
  - rapports 0,5724 et 0,6764 ;
  - tests attendus 990 s et 1 112 s (1 116 s avec 0,68 arrondi) ;
  - mise en place de 1 119 à 1 245 s, avec 128,5 s hors tests ;
  - marge de 255 à 384 s ;
  - seuil de prix 0,7407 USD de l'heure.
- **Citations et tests.** Les 14 intitulés de citation figurent chacun une seule fois. 763 = 762 + 1 test neuf.
- **Remarques non remontées** (antérieures au différentiel, sans effet sur une lecture ni sur un relancement) :
  - (a) « durée et mémoire pour un juge fini seulement » (ligne 138) n'est pas exact dans la fenêtre déclarée « TERM pendant l'écriture d'un fichier de notations ». Mon contrôle (`depot/tests/test_zz_vc3.py`, dans mon clone) arrête l'écriture du fichier du 8B. Il relève alors un 8B « en cours » avec `duree_s`, `memoire_pic_gio` et `lots_faits` = `lots`, sans fichier : l'issue est lisible, ce n'est pas un désaccord. La table conclut donc par ses deuxième et cinquième lignes, non par la quatrième. Le relancement reste fermé par la ligne `lot=2/2` des traces.
  - (b) « à l'écriture : … préenregistrement non scellé » (ligne 139) : l'arrêt a en fait lieu à la lecture, par `exiger_prereg_scelle` dans `exiger_run_sous_prereg` (ligne 72), avant `creer_manifeste`. La liste « lecture décisive » le couvre déjà (« empreinte égale à celle de son sceau »).
- **Non joué (consigne) :** répétition jouet, bancs des contrôles et du scellement.
- **Sûreté :**
  - aucun fichier du dépôt ni du bloc-notes modifié : `git status` vide ;
  - le dépôt est passé de c9e3172 à eb8ab88 pendant mon travail (commits d'état), sans moi ;
  - aucun appel à vastai (faux outil seulement), aucun accès réseau, aucun sous-agent, aucun jeton affiché ;
  - pour faire de la place sur le disque (2,8 Go libres alors que le lanceur en exige 3), j'ai supprimé mes copies mutées du code, après en avoir gardé les différentiels.
- **Fichiers de travail**, sous `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/vc3/agent/` :
  - `depot/` : clone au commit c63d4f1, avec mon contrôle `tests/test_zz_vc3.py` ;
  - `mutants-code/*.diff` : les cinq mutants du code ;
  - `b5/`, `b5-mut-v1/`, `b5-mut-etiq/`, `b5-surv-mut/` : copie du brouillon 5 et copies mutées ;
  - `journaux/` :
    - tests et mutants du code : `base-t1.txt`, `base-t2.txt`, `m-*-t1.txt`, `m-*-t2.txt`, `vc3-arret-ecriture-8b.txt` ;
    - bancs : `banc-lanceur-sain.log`, `banc-lanceur-mut-v1.log`, `banc-lanceur-mut-etiq.log`, `banc-lanceur-mut-p00.log`, `banc-surv-b5.log`, `banc-surv-b5-surv-mut.log` ;
  - `rep/` : journal de la répétition sans sa ligne « code 0 », journaux synthétiques mutés et leurs sorties ;
  - `preuves-sain/` : dossier synthétique des cinq journaux ;
  - `diff-*-recalcule.diff`, `word.diff`, `changements.txt` : différentiels recalculés, dont le différentiel mot à mot du texte.

### Traitement

Le rapport tient les douze constats du second tour (WT-1 à WH-5) pour traités et n'en ajoute aucun de fond.

| id | gravité | constat | traitement |
|---|---|---|---|
| XH-1 | forme | plan : « environ 24 minutes » pour 1 491,03 s | plan, copie versée : « environ 25 minutes » ; titre sans « brouillon 5 » et ligne d'historique (troisième tour : un point de forme) |
| Xa | remarque | contenu d'`arret.json` inexact dans la fenêtre « TERM pendant l'écriture d'un fichier de notations » | candidat 5 : durée et mémoire pour un juge dont la boucle des lots est close (fini, ou interrompu pendant l'écriture de son fichier, encore « en cours », tous ses lots faits) ; fenêtres de l'écriture séparées : avant que le fichier existe → `arret.json` lisible, juge sans fichier (deuxième ligne, et cinquième si aucun juge n'est fini), relancement fermé par la ligne du dernier lot ((ii)) ; après la création et avant le sceau, ou entre le sceau et « écrit » → quatrième ligne |
| Xb | remarque | arrêt du préenregistrement non scellé rangé à l'écriture | candidat 5 : « préenregistrement hors du dépôt ou non scellé » à la lecture décisive ; retiré de l'écriture |

## Contrôles courts du texte final

Deux sous-agents neufs, chacun sur le seul différentiel du texte (et du plan pour le premier), au regard du code au commit `c63d4f1`.

Candidat 5 (`brouillons/T0.5-pilote-notations-v1-candidat5.md`, `0fbf5c1a52675ce29940115455015b78262ee88f7bf42f38ada8cbec05d61df4`) : reprises du troisième tour.

### Rapport — candidat 4 → candidat 5, plan

**Verdict : conforme avec réserves.**

Les trois reprises sont exactes au regard du code au commit c63d4f1 ; je les ai éprouvées avec le vrai gestionnaire du signal TERM. Le différentiel n'introduit aucune erreur : aucune affirmation fausse sur le code, aucun mauvais renvoi à une ligne de la table, et la porte du relancement reste fermée où il faut.

La réserve porte sur la fenêtre jumelle de la remarque (a), celle du résumé. Le défaut est antérieur au différentiel et se corrige en une phrase avant le scellement.

#### Reprises

**Point de forme du plan : tenue.**
- Le plan, ligne 82, dit maintenant « environ 25 minutes ». Le journal `brouillons/T0.5-notations-suite-c63d4f1-v1.txt` (d4a32162…, égal à son sceau) porte « 763 passed in 1491.03s (0:24:51) ».
- Les deux autres changements du plan sont exacts : titre sans « (brouillon 5) », et ligne d'historique « troisième tour : un point de forme (durée de la suite) ».
- Seul le plan diffère du brouillon 5 dans le bloc-notes : ses 13 scripts sont égaux à ceux du brouillon 5, dont les `empreintes.sha256` sont conformes.
- Aucun script ni le candidat ne cite l'empreinte du plan. Le lanceur n'exige que les 13 scripts (plan, ligne 93).

**Remarque (a) : tenue.**
- Code (`noter_pilote_a.py`) : `duree_s` et `memoire_pic_gio` sont posés lignes 296-297, après la boucle des lots. Ils précèdent `ecrire_resultat` (ligne 299) et le statut « écrit » (ligne 303). `ecrire_resultat` écrit le fichier puis le scelle (`manifeste.py`, lignes 137-138).
- Le premier TERM lève aussitôt `GardeArret` (`gardes.py`, lignes 24-36). La ligne `lot=n/n` part avant l'écriture, avec `flush=True` (ligne 75).
- Mon contrôle (`test_zz_vc4.py`, 3 réussis) appelle `gardes.lever_sur_term` à trois instants de l'écriture du fichier du 8B :
  - **avant la création du fichier** : `arret.json` scellé, 8B « en cours », lots faits = lots = 2, `duree_s` et `memoire_pic_gio` présents, aucun fichier. `charger_notations` passe : l'issue est lisible, sans désaccord. Les traces portent `lot=2/2` et aucune ligne de fin ;
  - **après la création, avant le sceau** : fichier présent sans sceau. Le lecteur s'arrête (« empreinte compagnon … absente ») : quatrième ligne ;
  - **entre le sceau et « écrit »** : le lecteur s'arrête (« en désaccord pour ['jouet-8B'] ») : quatrième ligne.
- Les renvois du texte sont justes : deuxième ligne = juge sans fichier (ligne 111), cinquième = arrêt avant tout juge fini (ligne 114), quatrième = non lisible (ligne 113). La condition (ii) du relancement cite bien la « ligne … de dernier lot ».
- La porte reste fermée, en accord avec les autres pièces :
  - la deuxième ligne de la table : un juge « en cours » n'est renoté que par la cinquième ;
  - la cinquième ligne : relancement seulement aux conditions de « Relancement » ;
  - le paragraphe « Fini, établi sur les pièces » : la ligne `lot=n/n` y est une fin possible.

**Remarque (b) : tenue.**
- `exiger_run_sous_prereg` (`lire_notations_pilote.py`, lignes 63-80) contrôle, dans l'ordre du texte : hors du dépôt (ligne 71), scellé (`exiger_prereg_scelle`, ligne 72), décisif (ligne 74), mode réel (ligne 76), autre préenregistrement (ligne 78).
- Elle est appelée par `charger_notations` (ligne 111), avant `creer_manifeste` (ligne 209). `creer_manifeste` refait ces deux contrôles (`manifeste.py`, lignes 95-96), mais ils ne peuvent pas se déclencher en premier.
- La liste « à l'écriture » contient maintenant exactement les deux gardes de procédure de la ligne 117 de la table (arbre non propre, identifiant déjà pris). Aucun classement ne change.

**Paragraphe « Contre-lecture » et en-tête : exacts.**
- Le paragraphe est fidèle au rapport du troisième tour : « conforme », un point de forme, remarques (a) et (b).
- Les empreintes citées en tête sont conformes : candidats 4, 3, 2 et 1, et brouillon 1.

#### Constats neufs

1. **Mineur, antérieur au différentiel, trouvé par symétrie avec (a).**
   - **Lieu :** Liste d'arrêt, « Pendant le run », ligne 138 : « TERM pendant ou après l'écriture du résumé (un `arret.json` s'ajoute alors au `resume.json`) », puis « Ces fenêtres, et celles sans `arret.json`, se lisent par la table (quatrième ligne) ».
   - **Constat :**
     - Un TERM pendant l'écriture du résumé, avant que `resume.json` existe, laisse un `arret.json` seul, scellé, avec les deux juges « écrit » en accord avec leurs fichiers. L'issue est lisible : selon les conditions de la table, ce sont les première et troisième lignes qui s'appliquent (deux juges lus, aucun relancement), et non la quatrième (nœud pour les deux).
     - De même, un TERM reçu après le retour d'`executer` n'ajoute aucun `arret.json` : la ligne 219 est hors du bloc qui consigne l'arrêt, et `GardeArret` est attrapé dans `__main__` (lignes 342-352, code 1). Le `resume.json` reste seul et il est lu.
     - Le texte contredit donc la table dans ces deux sous-fenêtres de quelques millisecondes.
     - Effet sur le relancement : aucun. Les fichiers et les lignes de fin ferment (ii).
     - Effet sur la lecture : le texte dit nœud là où la table et le lecteur lisent les deux juges, d'où une divergence possible au verdict.
   - **Preuve :** `test_zz_vc4_resume.py` (2 réussis).
     - TERM avant la création : fichiers présents `arret.json` et les deux fichiers de notations ; étape « résumé » ; statuts « écrit » ; `charger_notations` passe et lit les deux juges.
     - TERM après la création, avant le sceau : `resume.json` et `arret.json` présents ; arrêt « un seul attendu : run non lisible ». La quatrième ligne est juste dans ce cas.
   - **Correction :** découper cette fenêtre comme celle des fichiers de notations : « TERM après la création du résumé et avant le retour d'`executer` (`arret.json` en double) ; un TERM avant que le résumé existe laisse un `arret.json` seul et lisible, juges écrits (première et troisième lignes), et un TERM après le retour d'`executer` laisse le `resume.json` seul, lu ».

**Remarques non remontées** (sans effet sur une lecture ni sur un relancement) :
- « cinquième si aucun juge n'est fini » se lit au sens de la cinquième ligne (aucun fichier, aucun juge échu) ou au sens de la procédure (`lot=n/n` vaut fin possible). Les deux lectures donnent nœud pour les deux juges et aucun relancement.
- Un TERM pendant `memoire_pic_gio()` (ligne 297) laisse une durée sans mémoire, pour un juge « en cours » dont tous les lots sont faits, avant l'écriture au sens strict. Le « seulement » reste vrai, et le lecteur ne lit que le statut.
- Si le TERM tombe pendant l'écriture du fichier du 3B, avant sa création, et que le 8B est écrit, la troisième ligne s'applique aussi (aucun relancement). La phrase ne la nomme pas ; la ligne « combinaisons » de la table la couvre.

#### Vérifications faites

- **Différentiels recalculés :**
  - texte, du candidat 4 au candidat 5 ;
  - plan, du brouillon 5 au bloc-notes.
  - Les deux sont identiques aux fichiers fournis.
- **Empreintes :** candidat 5 = 0fbf5c1a… (commit 6845487) ; plan : 315e266c… (brouillon 5) → 145d0ed1… (bloc-notes).
- **Code lu au commit c63d4f1 :**
  - `noter_pilote_a.py`, lignes 71-75 et 195-352 ;
  - `gardes.py`, lignes 19-59 ;
  - `manifeste.py`, lignes 68-150 ;
  - `lire_notations_pilote.py`, lignes 63-126 et 209-211 ;
  - `prereg.py`, lignes 70-76.
- **Tests,** dans une copie du clone au commit c63d4f1, avec l'interpréteur indiqué :
  - `test_zz_vc4.py` : 3 réussis, 82 s ;
  - `test_zz_vc4_resume.py` : 2 réussis, 103 s.
- **Sûreté :**
  - `git status` du dépôt vide (tête 6845487) ;
  - bloc-notes `notations-v1/` non touché ;
  - clone du troisième tour inchangé ;
  - aucun réseau, aucun appel à vastai, aucun sous-agent, aucun jeton affiché ;
  - `episodes-defaut.json` et `chemin-defaut.json` non lus.

Fichiers, sous `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/vc4/agent/` :
- `depot/tests/test_zz_vc4.py`
- `depot/tests/test_zz_vc4_resume.py`
- `journaux/vc4-term-ecriture-8b.txt`
- `journaux/vc4-term-resume.txt`
- `diff-texte-recalcule.diff`
- `diff-plan-recalcule.diff`

### Traitement

| id | gravité | constat | traitement |
|---|---|---|---|
| YT-1 | mineur | fenêtres de l'écriture du résumé décrites à tort comme non lisibles (quatrième ligne) | candidat 6 : seule la fenêtre « après la création du résumé et avant le retour du lanceur » donne un `arret.json` en double (quatrième ligne) ; avant que le résumé existe, `arret.json` seul et lisible, statuts finals en accord avec les fichiers (troisième ligne si un juge est écrit, deuxième pour un juge échu ; aucun relancement) ; après le retour du lanceur, `resume.json` seul, lu (code 1 du run) |
| — | remarque | troisième ligne non nommée pour un TERM pendant l'écriture du fichier du 3B, le 8B écrit | candidat 6 : « troisième si l'autre juge est écrit » |
| — | remarques | lecture de « cinquième si aucun juge n'est fini » ; TERM pendant la mesure de la mémoire | sans effet sur une lecture ni sur un relancement (rapport) ; gardées en l'état |

Candidat 6 (`brouillons/T0.5-pilote-notations-v1-candidat6.md`, `6b8df25d22e37b6e1bd2a2d05de61d72a4572137146b8a6552f616713766164a`) : reprises du contrôle du candidat 5.

### Rapport — candidat 5 → candidat 6

**Verdict : conforme avec réserves.**

Les deux reprises tiennent. Chaque phrase changée de la Liste d'arrêt est exacte au regard du code au commit c63d4f1 et cohérente avec la table et avec « Relancement ». Je l'ai vérifié par quatre tests neufs qui utilisent le vrai gestionnaire du signal TERM, et pour le dernier cas le vrai bloc `__main__`. Il reste deux réserves de précision, toutes deux dans le différentiel. Aucune ne touche une lecture ni un relancement, et chacune se corrige en une parenthèse avant le scellement.

#### Reprises

**Constat 1 du contrôle précédent (fenêtres de l'écriture du résumé) : tenu.** Il porte sur la ligne 138 du candidat 6.

- **« TERM après la création du résumé et avant le retour du lanceur (un `arret.json` s'ajoute alors au `resume.json`) » : exact.**
  - Dans le code, `ecrire_resultat` crée le fichier puis le scelle (`manifeste.py`, lignes 137-138). Après lui, `lire_manifeste` (ligne 325) et le `return` restent dans le bloc `try` (`noter_pilote_a.py`, lignes 218-225), donc un `arret.json` s'écrit.
  - Je l'ai éprouvé à deux instants. Avant le sceau, par le test du contrôle précédent. Après le sceau, pendant `lire_manifeste`, par mon cas c. Dans les deux cas, `resume.json` et `arret.json` sont présents, et le lecteur s'arrête sur « un seul attendu : run non lisible ».
  - Le renvoi à la quatrième ligne de la table est donc juste.
- **« TERM à l'étape « résumé », avant que `resume.json` existe → `arret.json` seul et lisible, statuts finals en accord » : exact.**
  - À la ligne 317, chaque juge est soit « écrit », avec son fichier scellé (lignes 298-303), soit « échu », sans fichier (lignes 284-286).
  - `issue_des_notations` lit les statuts dans `partiel.juges` (`lire_notations_pilote.py`, lignes 94-95). `charger_notations` n'exige que l'accord entre fichiers et statuts (lignes 123-125).
  - Je l'ai éprouvé dans deux configurations. Les deux juges écrits (test du contrôle précédent) : les deux sont lus. Le 8B échu et le 3B écrit (mon cas b) : issue « arret », seul le 3B est lu, le 8B est « échu » sans fichier. Deux juges échus donnent le même accord, d'après le code.
  - **Renvois à la table :**
    - « troisième ligne si un juge est écrit » renvoie à la ligne 112 : juge écrit lu, aucun relancement ;
    - « deuxième pour un juge échu » renvoie à la ligne 111 : nœud, jamais renoté ;
    - la cinquième ligne est bien exclue.
  - « aucun relancement : les deux juges ont fini » s'accorde avec « Relancement » (ii) et avec « Fini » (« écrit » ou « échu »).
  - Le cas du 8B échu avec le 3B écrit n'entre pas dans la phrase de préséance « s'arrête ensuite pendant le 3B » : le 3B a fini, et la première ligne le lit « quelle que soit la cause ».
- **« TERM après le retour du lanceur : aucun `arret.json`, `resume.json` seul lu (le run sort en code 1) » : exact pour le processus du lanceur.**
  - La ligne 342 est hors du `try`. `lever_sur_term` lève `GardeArret` au premier signal (`gardes.py`, lignes 33-36), et `__main__` l'attrape (lignes 350-352), d'où le code 1.
  - Mon cas d passe par le vrai bloc `__main__` (exécuté par runpy), avec le TERM envoyé à l'impression du résumé :
    - sortie `SystemExit` de code 1, et « ARRÊT : signal TERM reçu… » sur la sortie d'erreur ;
    - pièces présentes : les deux fichiers de notations et `resume.json`, aucun `arret.json` ;
    - lecteur : issue « resume », les deux juges lus.
  - Pour la parenthèse « code 1 », voir le constat neuf 1.
- **« Ces fenêtres […] (quatrième ligne) » :** la phrase ne vise plus que les fenêtres où les pièces sont en désaccord ou en double. Elle est exacte.

**Remarque sur la troisième ligne (TERM pendant l'écriture du fichier du 3B, le 8B écrit) : tenue.**
- La phrase dit : « deuxième ligne ; cinquième si aucun juge n'est fini ; troisième si l'autre juge est écrit ».
- Mon cas a envoie le TERM à l'appel d'`ecrire_resultat` pour le 3B :
  - **pièces :** `arret.json` seul, étape « notations decisives par jouet-3B » ; le 8B « écrit » avec son fichier ; le 3B « en cours », 2 lots faits sur 2, sans fichier ;
  - **traces :** `juge=jouet-8B fin=écrit` et `juge=jouet-3B lot=2/2`, aucune ligne de fin pour le 3B ;
  - **lecteur :** issue « arret », seul le 8B est lu.
- La ligne 112 donne alors : 8B lu, 3B en nœud, P3 non concluant, aucun relancement. La condition (ii) de « Relancement » tombe aussi (fichier du 8B, ligne de fin).
- Si le 8B est échu, seule la deuxième ligne s'applique : la cinquième est exclue, car un juge échu a fini. C'est cohérent avec la préséance (nœud pour les deux juges, aucun relancement).

#### Constats neufs

1. **Mineur, dans le différentiel (ligne 138) : la parenthèse « le run sort en code 1 » et l'expression « retour du lanceur ».**
   - **Le code 1 ne se voit pas au niveau de l'instance.**
     - Partout ailleurs dans la Liste d'arrêt, « (code N) » désigne le code du script de l'instance : « (code 2) » à la ligne 135, « (code 1) » pour la poussée finale à la ligne 138.
     - Or le TERM du délai externe vient de `timeout`, qui rend 124. Je l'ai vérifié avec GNU coreutils 9.4 : un enfant qui sort en 1 après le TERM donne 124.
     - Le script `scripts/notations_t05_instance.sh` au commit c63d4f1 (lignes 254-256) écrit alors au journal « run : code 124, mais résumé écrit sans arrêt consigné : run complet ». Il committe, pousse, et sort en 0 si la poussée réussit.
     - Sous le plafond de l'amorce, `sur_term` écrit « ARRÊT pendant run … », committe `resume.json` seul et sort en 124.
     - La seule trace du code 1 est la ligne « ARRÊT : … » de `run.err`.
   - **« le lanceur » désigne aussi le lanceur de l'instance** (lignes 99 et 131). La frontière voulue est le retour d'`executer` (ligne 342), que le texte ne nomme pas.
   - **Effet :** aucun sur une lecture, puisque le lecteur juge sur les pièces. Aucun sur un relancement, puisque le résumé présent fait tomber (ii). Le risque est ailleurs : quelqu'un qui qualifie l'issue au journal y lira « code 124 … run complet », non « code 1 ».
   - **Correction proposée :** « un TERM après le retour d'`executer` n'ajoute aucun `arret.json` : le `resume.json`, seul, est lu (le lanceur sort en code 1, que `timeout` rend en 124 ; le script de l'instance tient le run pour complet) ». Écrire de même « avant le retour d'`executer` » dans la phrase des fenêtres en double. Retirer simplement la parenthèse convient aussi.
2. **Forme, dans le différentiel (« Contre-lecture », ligne 158).**
   - Le paragraphe cite le constat repris, mais pas la remarque reprise (troisième ligne nommée, ligne 138). Pour le tour précédent, il nomme pourtant les remarques reprises.
   - Ajouter « et une remarque (troisième ligne nommée pour un TERM pendant l'écriture du fichier du 3B, le 8B écrit), reprise ».

#### Vérifications faites

- **Différentiel :** recalculé du candidat 5 au candidat 6, il est identique au fichier fourni.
- **Empreintes :**
  - candidat 5 = 0fbf5c1a…, égal au commit 6845487 et à la citation de l'en-tête ;
  - candidat 6 = 6b8df25d…, égal au commit b87d17a ;
  - candidats 4 à 1 et brouillon 1 égaux aux citations de l'en-tête.
- **Code lu au commit c63d4f1 :**
  - `noter_pilote_a.py`, lignes 60-80 et 190-352 ;
  - `gardes.py`, lignes 15-60 ;
  - `manifeste.py`, lignes 68-150 ;
  - `lire_notations_pilote.py`, lignes 50-126 ;
  - script de l'instance, lignes 140-185 et 230-280 (égal à la tête).
- **Texte lu :** la table (lignes 108-119), « Fini, établi sur les pièces ; préséance » (ligne 123), « Relancement » (ligne 131), « Pendant le run » (ligne 138).
- **Tests :** 4 tests neufs réussis en 158 s, avec l'interpréteur indiqué, dans une copie du clone au commit c63d4f1 (sources et tests égaux au commit).
- **Sûreté :**
  - dépôt non modifié (`git status` vide, tête b87d17a) ;
  - clone du contrôle précédent inchangé ;
  - aucun accès réseau, aucun appel à vastai, aucun sous-agent, aucun jeton affiché ;
  - `episodes-defaut.json` et `chemin-defaut.json` non lus.

Fichiers, sous /tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/vc5/agent/ :
- depot/tests/test_zz_vc5.py
- journaux/vc5-tests.txt
- diff-recalcule.diff

### Traitement

| id | gravité | constat | traitement |
|---|---|---|---|
| ZT-1 | mineur | « (le run sort en code 1) » trompeur au niveau de l'instance ; « retour du lanceur » ambigu | candidat 7 : frontière nommée « retour d'`executer`, la fonction du lanceur des notations qui conduit le run », dans les deux phrases ; parenthèse sur le code de sortie retirée (option proposée par le rapport ; aucune affirmation neuve). Vérifié par la session sur `scripts/notations_t05_instance.sh` au commit `c63d4f1` : un résumé présent sans arrêt consigné est tenu pour un run complet, quel que soit le code |
| ZT-2 | forme | paragraphe « Contre-lecture » : la remarque reprise n'est pas nommée | candidat 7 : nommée ; contrôle du candidat 6 résumé |

## Bilan

Texte relu et vérifié : candidat 7 (`brouillons/T0.5-pilote-notations-v1-candidat7.md`, `66784ceb9c93f699b211fa26a142a8e64e1cccbc2c2fb3479df559f297c474f6`, scellé), qui ne diffère du candidat 6 que par les reprises ZT-1 et ZT-2 et par son en-tête ; ce dernier différentiel, sans affirmation neuve sur le code hors du nom de la fonction `executer`, est relu par la session (différentiel mot à mot), sans nouveau tour. Code relu : commit `c63d4f1c073f3b6146729dae0086cd7205cdfa57` (763 tests). Chaîne : brouillon 5, plus le seul point de forme du plan (troisième tour) ; ses copies versées et scellées sous `docs/procedures/notations-T0.5-v1/` au commit C1 sont celles qui font foi. Configuration relue : `brouillons/T0.5-pilote-notations-config-v1-candidat2.json` (`143cfa258a8364ded0ffced1ad5213a26a2c8598112fa11a3fc44357fbe9ea97`), inchangée depuis la contre-lecture R2.

Décompte : premier tour, 4 majeurs (3 sur le texte, 1 sur la chaîne) et 23 mineurs ; second tour, 12 mineurs ; troisième tour, un point de forme et deux remarques ; contrôles courts, un mineur et une remarque, puis deux précisions et un point de forme. Aucun constat bloquant ; tous traités ; aucun n'a changé une hypothèse, une prédiction, un seuil ni un critère de lecture du fond.
