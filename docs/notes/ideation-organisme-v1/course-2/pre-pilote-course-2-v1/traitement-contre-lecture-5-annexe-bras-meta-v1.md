# Traitement de la contre-lecture 5 de l'annexe du bras méta (brouillon 5 → brouillon 6)

**Auteur** : sous-agent neuf Fable 5.1, reprise du chantier de la session conv-audit (suspendue) par une autre session, 1er novembre 2026, à partir de 19:20 UTC (`date -u`). Je n'ai écrit ni les brouillons 1 à 5 de l'annexe, ni leurs contre-lectures (dont la contre-lecture 5 que je traite), ni le script de calcul v5, ni l'erratum v2, ni le préenregistrement.
**Statut** : pièce de travail, non scellée, sans compagnon d'empreinte ; aucun commit ; rien ne tranche ni ne gèle ici. Aucun fichier existant modifié (le brouillon 5, le script v5, sa sortie, l'erratum v2 sont gardés tels quels, R12) ; aucune dépense, aucun réseau, aucun appel de modèle ; rien lu sous `donnees/` (les copies de la question du tour 2 trouvées dans une sauvegarde `donnees/` n'ont pas été ouvertes : la pièce vient de `git show` sur un chemin `brouillons/`). Les rejeux du script v5 ont tourné par `python3 -I` depuis des dossiers temporaires vides neufs de la zone de travail de session (restés vides, `PYTHONDONTWRITEBYTECODE=1`).

**Pièces créées** (toutes dans `docs/notes/ideation-organisme-v1/course-2/pre-pilote-course-2-v1/`) :
- `annexe-bras-meta-v1-brouillon6.md` — brouillon 6 de l'annexe, `e1680c41a180fea506bc5e80f9e686cf9efb42d6acdd3eef353dd5e7d2f21fcf` ;
- `appliquer-cl5-brouillon6-v1.py` — script de substitutions exactes (brouillon 5 → brouillon 6 ; 40 substitutions, chacune contrôlée « une occurrence exactement » ; il calcule aussi les empreintes du texte hors bloc N4 et du bloc de paramètres, comme le script v5) ;
- ce traitement.

## 1. Pièces lues (empreintes recalculées par `sha256sum`)

Le dossier transmis par conv-audit (`chantiers-conv-audit/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/`) contenait le brouillon 5, les contre-lectures 1, 3, 4 et 5 et les erratums v1 et v2, **mais ni le script v5, ni sa sortie, ni le brouillon 4** : je les ai retrouvés par `git show` sur le commit `e1b603bf` du dépôt de travail (chemin `brouillons/…/pre-pilote-course-2-v1/`), empreintes égales à celles que l'annexe et la contre-lecture 5 citent.

| Pièce | Empreinte | Lecture |
|---|---|---|
| `annexe-bras-meta-v1-brouillon5.md` | `c04ddf15c92c68c33a6770d42ffb6513c66414ee41a7ae76b7bf5bf6d91faf07` | en entier |
| `contre-lecture-annexe-bras-meta-v1-brouillon5.md` (Sonnet 5.5) | `156b9c557f9c5a692374db1f991a7e38846fa2e38214735178f5d5eae0911e2e` | en entier |
| `erratum-N4-annexe-bras-meta-v2.md` | `b3196687534269819d4abe7f645f67a578be87b64768ef40ac7961404e346382` | en entier |
| `calcul-profil-bras-meta-v1-brouillon5.py` (git `e1b603bf`) | `612e543d16f7b70d10a09a4f07fba28777fcf9815fdc14f176b5ef28da315607` | en-tête, lecture de l'annexe, sections 8, 9, 16, 18, 19 (gardes et dépendances) |
| `calcul-profil-bras-meta-v1-brouillon5.sortie.txt` (git `e1b603bf`) | `16e5ff7edd4236ae804365a2f1b6258d037d0ce3853e8a40210bfecc91d84ccb` | en entier (313 lignes) |
| `annexe-bras-meta-v1-brouillon4.md` (git) | `397e1cbc7483e7c5106bd859a77514605166e1fb699eb4b4ab5ed2730d15fb7c` | non relu ; exigé par le § 19 du script |
| `calcul-profil-bras-meta-v1-brouillon4.py` ; `….sortie.txt` (git) | `48e3c57d…` ; `9279d4ad…` | empreintes seulement |
| `contre-lecture-annexe-bras-meta-v1-brouillon4.md` | `7b467e84351503e69d789c98978213ac251665bd917a9cd1dbdf574f696342cd` | en-tête |
| `preenregistrement-pre-pilote-course-2-brouillon10.md` (git `e1b603bf`) | `ea940d56e5ee949e7b71a57488f7c2c8a2b7ac4835f30cb5f98933e4c00c824f` | l. 360 (S18) |
| texte I `question-course-2-defense-fusion-v5.md` (copie de session) | `a750144963913ba1c3dcf3eed5d4f8322d7d0246135e17c95ac8e7253c2dd680` | l. 36, 52, 57 |
| `consigne-aiguilleur-v1.md` (copie de session) | `c2efa12003bb8ce1a9a636e4610fa9caa9464ae685b0bd628c9c351b64e3271e` | l. 253, 321, 437, 462 (garde A4) |
| code v55 (git `9fb76cd9`) : `fiches_v53.py`, `fiches_v54.py`, `outils.py` | `7cfcf832…`, `1ab0796d…`, `966d9553…` | `garde_etiquettes`, `trouver`, `normaliser_texte` |
| PDF Bettencourt et Kaiser 2015 | `2fb9aab049631cdffe59631ce5196b800220dbeb584afd179ce8e6623485a523` (compagnon conforme) | texte extrait par `pdftotext` |
| PDF Uzzi et coll. 2013 | `532970985650d07fe69c66d912dfae96d6f45522fcb72e92c88857f4fd101173` (compagnon conforme) | texte extrait par `pdftotext` |
| synthèse du tour 1 v12, critères, question du tour 2, question des nœuds v12, relecture Opus | `e4d5a5c9…`, `22edbf47…`, `19ff79d9…`, `a7fac44b…`, `d1209130…` | empreintes (exigées par le script v5) |

**Non lus** : synthèse du tour 2, synthèses des questions 4 à 7, `registres/decisions.md`, brouillons 1 à 3 et leurs contre-lectures, archive du code v56, erratum v1. Ce que l'annexe rapporte des tours 1 et 2 n'est pas re-vérifié ici (la contre-lecture 5 a vérifié le tour 1 sur la synthèse).

## 2. Verdict de la contre-lecture 5 et classement de ses douze constats

Verdict de la contre-lecture 5 : **« présentable après corrections »**, 0 bloquant, 1 majeur, 4 moyens, 7 mineurs ; rejeu identique octet pour octet ; recalculs indépendants concordants à moins de 0,01 ; citations d'Uzzi exactes ; les neuf constats de la contre-lecture 4 traités. Je retiens ce verdict : mes propres vérifications (section 4) ne le contredisent sur aucun point.

**Comptes** : **10 acceptés** (dont 4 en partie : CA5-04, CA5-08, CA5-10, CA5-12), **0 refusé**, **2 hors mandat** (CA5-09 en entier ; et les parts de CA5-08, CA5-10, CA5-12 qui touchent le script v5, qui n'est pas modifié). Mandat : brouillon 6 de l'annexe seulement ; ni le script v5, ni l'erratum v2, ni aucune pièce existante ne sont réécrits.

| Constat | Gravité | Décision | Motif et ce qui est fait |
|---|---|---|---|
| CA5-01 collision `n1_…`–`n6_…` / étiquettes `N1` à `N4` de la liste A4 de la consigne de l'aiguilleur | majeur | **accepté, voie (ii)** | Reproduit (section 4.1) : `fiches_v53.garde_etiquettes` avec la liste de la consigne (l. 462) trouve N1 à N4 sur ce qui est servi au lecteur et N1, N2 sur les quatre règles ; D1 à D3 seraient trouvés aussi. Voie (ii) écrite dans l'annexe (sections 1, 8, 9 étape 4, table 11) : la liste gelée ne contient ni `N1` à `N4`, ni `D1` à `D3`, ni un identifiant de la grille, confirmation du détenteur de la configuration avant É0. Voie (i), renommage : non faite, elle touche le script v5 (hors mandat) et rouvre une relecture entière ; posée à Lazar comme alternative. |
| CA5-02 repli 0,53 et non produit 0,028 comptés deux fois | moyen | **accepté** | Arithmétique confirmée (0,47 + 0,53 + 0,028 = 1,028). Trois issues qui font 1, par option, ajoutées sous la table 0.2 ; bloc N4 et section 0.3 corrigés (repli 0,50 à 6 fiches, 0,17 à 10, = 1 − P(méta) − P(aucune paire éligible), ± 0,01 d'arrondi). Le script n'imprime pas le repli : une colonne au script serait un script v6 (hors mandat), les chiffres sont dits « arithmétique sur la sortie § 3 ». |
| CA5-03 pas de règle de lecture figée de l'issue, ni de liste d'arrêt | moyen | **accepté** | Table « issue observée → libellé → compté comme → audit R4 » et table des arrêts (condition, action, où) ajoutées en section 6, proposées À GELER, avec l'alternative « au préenregistrement brouillon 11 » ; renvoi corrigé en 0.5 ; ligne en table 11. Point gelable par Lazar ; aucune condition d'arrêt nouvelle. |
| CA5-04 codes non développés ; résumé après 16 500 caractères | moyen | **accepté en partie** | Boîte « Pour Lazar » (cinq points, verdict d'abord) et lexique des codes ajoutés en tête, après le statut. Le déplacement des « pièces lues » et « auteurs » en fin de document n'est pas fait : il déplacerait 16 500 caractères sans changer le fond et rendrait inutilisable la relecture limitée aux passages changés (option (ii) de l'étape 3) ; à faire au brouillon qui portera l'option choisie si Lazar le demande. |
| CA5-05 critère de retrait des indices non appliqué à n6 | moyen | **accepté** | Vérifié sur le texte I : l. 36 définit « Famille tenue à l'écart », « Transfert », « Invariance » pour toutes les fiches ; l. 52 impose à l'axe 1 « (d) l'invariance qui justifie le transfert ». « transfert » et « famille tenue à l'écart » retirés des indices de n6 (table de la section 1 et `definitions_niches` du bloc de paramètres) ; « préenregistrement » gardé avec sa raison (imposé au seul axe 4, où n6 est déjà à 0,70 ; nommé à l'axe 2 (d), l. 57) ; la définition en une ligne garde ses mots ; sensibilité « l'axe 1 se range en partie en n6 » non chiffrée (script non modifié). **Conséquence** : l'empreinte du bloc de paramètres change (`b2cc74e1…` → `08dd3c0d…`). |
| CA5-06 n5 « sans partenaire sous (d1) » | mineur | **accepté** | Vérifié sur les tables : sous (d1), n3–n5 (c = 2, e = 3) est dans le profil ; « sous (a), (c1) et (c2) ». |
| CA5-07 Bettencourt et Kaiser : PDF versé ; cascade et branching absents | mineur | **accepté** | Vérifié sur le PDF empreinté (section 4.4) : « giant connected component » (résumé) et « one giant connected cluster emerged » (p. 3) présents ; « cascad », « branching » : aucune occurrence. Journal point 6 réécrit : seule la composante géante est attribuée à cette source. |
| CA5-08 deux gardes sans cas piégé versé | mineur | **accepté en partie** | Vérifié : le script v5 n'appelle `garde_desaccord_v54` que sur le cas sain (l. 239, 488, arguments `set(), set()`). Section 4 : l'artefact est à jouer à É0, non par le script. Cas piégé de la garde des marqueurs **dans le script** : hors mandat (script v5 gardé ; à un script v6). |
| CA5-09 erratum v2 : « contre-lecture à venir » ; 0,12 contre 0,13 pour (d) | mineur | **hors mandat** | L'erratum v2 est scellé chez conv-audit et n'est pas réécrit ; une version 3 de l'erratum le corrigerait (deux phrases). L'annexe ne porte ni la phrase ni l'écart (elle écrit 0,12 pour (d1) sous la loi par axe, sortie § 17 ; les 0,12 / 0,13 viennent de deux tâches de simulation, sortie § 17 et § 18). Signalé à Lazar. |
| CA5-10 0,3 d'erreur-type du kappa sans trace ; effectifs 6 et 10 | mineur | **accepté en partie** | Le 0,3 est requalifié « ordre de grandeur à la main, 0,2 à 0,3 selon les marges, non calculé par le script » (mon approximation avec les marges de la sortie § 10 et un accord observé 0,7 donne ≈ 0,18 ; compatible) ; origine de 6 (S18 du préenregistrement brouillon 10, l. 360 : « effectif minimal de fiches de Kimi non aiguillées […] 6 ») et de 10 (texte I, deux fiches par axe) écrite en 0.1 ; n = 8 cité avec ses chiffres (sortie § 3). Calcul dans le script : hors mandat. |
| CA5-11 quatre alternatives sans avantage ou sans inconvénient | mineur | **accepté** | Une demi-ligne ajoutée à chacune : poids 0 (section 6), (R3) (section 1), S28 0,50 et 0,40 (section 1), désaccord sur chaque paire candidate (table 11). |
| CA5-12 libellé `annexe-b1` ; « plus de six minutes » | mineur | **accepté en partie** | Lexique : `annexe-b1` = loi du brouillon 1, pas l'option (b1). Durée : « de trois à sept minutes selon la machine » (mes rejeux : 6 min 27 s et 6 min 03 s et 5 min 56 s sur le brouillon 6 ; ceux des rédacteurs 3 min 20 s et 3 min 41 s ; contre-lecture 5 : 3 min 04 s). Renommer le libellé imprimé est une modification du script : hors mandat. |

**Champ `contre_lecture` du JSON : laissé « À REMPLIR », écart déclaré à la consigne reçue.** La consigne demandait de remplir « le champ contre-lecture » (référence, verdict, points acceptés et refusés). Je l'ai fait **en clair, dans le bloc N4** (ligne « Contre-lecture ») et en section 16, et **non dans la clé JSON `contre_lecture`**, pour deux raisons vérifiées : (1) le code v55 (`lire_annexe_meta_v55`, annexe section 8) exige que le rapport cité porte sur le brouillon relu et que ce brouillon soit identique au texte scellé hors des deux champs ; la contre-lecture 5 porte sur le brouillon 5, pas sur le brouillon 6 : remplir la clé ferait passer le brouillon 6 pour contre-lu ; (2) le script v5 arrête si la clé n'est pas exactement « À REMPLIR » (l. 471 à 473 : `assert TEXTE.count('"contre_lecture": "À REMPLIR"') == 1`) et son épreuve du texte exact attend le motif « annexe sans contre_lecture déclarée » (l. 480) : la clé remplie rendrait le rejeu impossible. Si Lazar ou conv-audit veulent la clé remplie malgré cela, c'est une substitution d'une ligne (le brouillon 6 est régénéré par le script). Le champ `approbation_lazar` reste « À REMPLIR » (à Lazar).

## 3. Substitutions (script `appliquer-cl5-brouillon6-v1.py`, 40 substitutions, dans l'ordre du script)

| N° | Lieu | Ancien (début) | Nouveau (résumé) | Constat |
|---|---|---|---|---|
| 1 | Statut | « (CA3-09 ; c'est le cas du brouillon 4, … » | ajoute le brouillon 6 à l'historique des relectures | — |
| 2 | avant « Pourquoi le texte est écrit ainsi » | insertion | boîte « Pour Lazar » (5 points) et lexique des codes | CA5-04, CA5-12 |
| 3 | Auteurs | « **A9 respecté** par les cinq : » | ligne « Brouillon 6 » ; « par les six » | — |
| 4 | Auteurs | « Réserve d'indépendance (inchangée)… » | contre-lecture du brouillon 6 : ni Opus ni Fable | R2 |
| 5 | Pièces lues | avant « - **Calcul** : » | puce « lus au brouillon 6 seulement » (empreintes) ; non lus | — |
| 6 | Calcul | « **Renvois « sortie § n »… » | « Au brouillon 6 » : aucun script nouveau, rejeu, § 19 compare au brouillon 4 | — |
| 7 | 0.1 | « deux par axe, texte I, « Déroulé »). » | origine de 6 et 10 ; n = 8 | CA5-10 |
| 8 | 0.2 | « 6 lectures d'étiquettes × 0,025). » | paragraphe « Trois issues d'un lot, qui font 1 » | CA5-02 |
| 9 | 0.2 bis | « n5 (sans partenaire sous (a), (c1), (d1)) » | « sous (a), (c1) et (c2) ; sous (d1), n3–n5 est dans le profil » | CA5-06 |
| 10 | 0.3 | « à 6 fiches il joue encore avec 0,53. » | 0,50 et non produit 0,03 | CA5-02 |
| 11 | 0.5 | « le libellé et la garde sont à écrire au préenregistrement » | proposés en section 6, à recopier | CA5-03 |
| 12 | 1, table | « \| banc, famille tenue à l'écart, transfert, universalité, … \| » | « \| banc, universalité, puissance simulée, préenregistrement \| » | CA5-05 |
| 13 | bloc N4, JSON | « Indices : banc, famille tenue à l'écart, transfert, … » | « Indices : banc, universalité, puissance simulée, préenregistrement. » | CA5-05 |
| 14 | 1, retraits | « et leur seule présence ne range pas une fiche. » | paragraphe « Au brouillon 6 (CA5-05) » | CA5-05 |
| 15 | 1, S28 | « erreur-type du kappa de l'ordre de 0,3 … » | 0,2 à 0,3, non calculé par le script | CA5-10 |
| 16 | 1, S28 | « Alternative : 0,50 et 0,40 — inconvénient : » | avantage ajouté | CA5-11 |
| 17 | 1, mixtes | « (R3) laisser le choix au lecteur … — inconvénient : » | avantage ajouté | CA5-11 |
| 18 | 1, règles servies | « la liste gelée de la configuration reste à éprouver à É0. » | renvoi à la collision (section 8) | CA5-01 |
| 19 | 4 | « artefact = fonction de score qui varie avec le désaccord → arrêt. » | « Où il est joué » : É0, non le script | CA5-08 |
| 20 | 6, score | « Alternative : poids 0 (égalités au tirage). Confiance : 0,5. » | avantage et inconvénient | CA5-11 |
| 21 | 6, avant « Calcul et rejeu » | insertion | tables « Lecture de l'issue observée » et « Liste d'arrêt » | CA5-03 |
| 22 | 7, journal 6 | « rapport de branchement (analogies seulement ; Bettencourt et Kaiser 2015, p. 3, **transcrit… » | vérification sur PDF ; composante géante seule attribuée | CA5-07 |
| 23 | 8, épreuve | « et un artefact (« fusion » ajouté à une définition) est refusé ; » | collision reproduite, condition sur la liste gelée, alternative (i) | CA5-01 |
| 24 | bloc N4 | « brouillon 5 de l'annexe (`annexe-bras-meta-v1-brouillon5.md`), … » | version du fichier : brouillon 6 | — |
| 25 | bloc N4 | « sinon repli, compté « hors profil » (0,53 à 6 fiches, 0,17 à 10), … » | trois issues qui font 1 | CA5-02 |
| 26 | bloc N4 | ligne « Calcul joué sur ce fichier » entière | rejeux du script v5 sur le brouillon 6, empreintes (sortie, bloc, texte hors bloc), écart à la sortie v5 | — |
| 27 | bloc N4 | avant le bloc JSON `parametres_bras_meta` | ligne « Contre-lecture » en clair (contre-lecture 5, verdict, acceptés, refusés) | consigne |
| 28–34 | 9, étape 3 | sept passages « brouillon 5 » → « brouillon 6 » ; « plus de six minutes » ; pièces à donner ; écart au brouillon 5 | — | CA5-12 |
| 35 | 9, étape 4 | « et par la garde A4 avec la liste d'étiquettes gelée ; empreintée (CA3-03). » | liste sans `N1` à `N4` ni `D1` à `D3` | CA5-01 |
| 36 | 10, v56 | « (inférence du rédacteur, non éprouvée par le script v5, …). » | levée par la contre-lecture 5 | — |
| 37 | 11 | « \| chaque paire candidate (≤ 90 lectures) \| » | avantage et inconvénient | CA5-11 |
| 38 | 11 | fin de la ligne N11 | trois lignes : liste A4, lecture de l'issue, indices de n6 | CA5-01, 03, 05 |
| 39 | fin | avant « *Fin. Ce texte ne gèle » | section 16 « Ce qui change par rapport au brouillon 5 » | — |

(Le script numérote 40 entrées ; la ligne 28–34 en regroupe sept.) Hors des substitutions, le script remplace deux repères `%(bloc)s` et `%(hors)s` de la ligne 26 par les empreintes qu'il calcule (bloc de paramètres en JSON canonique sans les deux champs libres ; texte hors bloc N4), avec les mêmes définitions que le script v5. Aucune autre ligne du brouillon 5 n'est touchée.

## 4. Chiffres revérifiés

### 4.1 Collision A4 (CA5-01), reproduite

Essai `cl5-traitement/essais/verif_cl5.py` (zone de travail de session, hors dépôt), `python3 -I`, code v55 extrait de git (`9fb76cd9`, empreintes égales) : `pole.fiches_v53.garde_etiquettes` sur `{identifiants, definitions_niches, definitions_structures, types}` lus dans le brouillon 5. Liste d'essai de l'annexe (17 étiquettes) : aucune. Liste de la consigne de l'aiguilleur (l. 462, avec `N1` à `N4`, `M6b`, noms de fournisseurs) : **N1, N2, N3, N4** trouvés (arrêt) ; avec `D1`, `D2`, `D3` en plus : D1, D2, D3, N1 à N4. Sur les quatre règles à recopier : **N1, N2**. `outils.normaliser_texte("n1_detection_sequentielle")` = `n1 detection sequentielle`. Conforme à la contre-lecture 5.

### 4.2 Tables et comptes (sur les blocs JSON du brouillon 5)

- Paires du profil (aux structures près) : (a) 4 (n1–n2, n1–n4, n1–n6, n3–n4 ; n5 sans partenaire) ; (b1) 6 (+ n4–n5, n5–n6) ; (b2) 7 (+ n2–n5) ; (d1) 10 (n3–n5 compris : CA5-06 fondé). Canal ≤ 1 : 7 paires sur 15 ; ≤ 2 : 13. Inégalité triangulaire : aucune violation ; e prend les valeurs 2 à 5, jamais 1 (la borne basse ne joue sur aucune paire).
- Hanley et McNeil, aire 0,5 : 6 contre 6 0,173 ; 8 contre 8 0,149 ; 4 contre 4 0,217 : exacts.
- Coûts : (c1) 5 × (0,2 × 1,447 + 2 × 0,057 + 6 × 0,025) = 2,77 USD ; 60 lectures × 0,025 = 1,50 ; 10 × 0,025 = 0,25 : exacts.
- CA5-02 : 0,47 + 0,53 + 0,028 = 1,028 ; repli (b1) = 1 − 0,47 − 0,028 = 0,502 → 0,50 ; à 10 fiches 1 − 0,83 − 0,001 = 0,169 → 0,17. Les autres repli de la section 0.2 du brouillon 6 : même arithmétique sur la sortie § 3 ((a) 0,72 / 0,45 ; (b2) 0,41 / 0,10 ; (d1) 0,44 / 0,13 ; (c1) 0,34 / 0,21 ; (c2) réunies 0,34 / 0,09, avec la perte 0,53 / 0,29).
- n = 8 (sortie § 3) : (a) 0,42 / 0,41 ; (b1) 0,70 / 0,69 ; (b2) 0,78 / 0,77 ; (d1) 0,75 / 0,74 ; aucune paire éligible 0,005.
- Erreur-type du kappa : approximation à la main (marges de la sortie § 10, accord observé 0,7, N = 10) ≈ 0,18 ; le « 0,2 à 0,3 » de la contre-lecture 5 et le « 0,3 » de l'annexe sont des ordres de grandeur ; aucun n'est dans la sortie : dit tel dans le brouillon 6.

### 4.3 Rejeux du script v5 (gardé sans modification)

Dépôt reconstitué dans la zone de travail (`cl5-traitement/depot/`) : `docs/notes/ideation-organisme-v1/orchestrateur-v55/` (git `9fb76cd9`), `src/` (copie du dépôt), `brouillons/…/collisionneur-noeuds-31-octobre-v1/` (question v12 `a7fac44b…`, relecture Opus `d1209130…`, git `e1b603bf`) ; dossier de la synthèse du tour 1 : trois pièces (`e4d5a5c9…`, `22edbf47…`, `19ff79d9…`), empreintes contrôlées par le script. Python 3.13.18, numpy 2.5.3.
- **Brouillon 5** : 19:29:33 à 19:36:00 UTC (6 min 27 s), `exit 0`, sortie **identique octet pour octet** à `16e5ff7e…`. Dossier de lancement resté vide.
- **Brouillon 6, rejeu 1** (fichier avant que le bloc N4 reçoive l'empreinte de la sortie) : 19:39:03 à 19:45:06 UTC (6 min 03 s), `exit 0`, sortie `calcul-profil-bras-meta-v1-brouillon5.sur-brouillon6.sortie.txt` `02d9c99432ec923b63573398f24ed2344243987b4a2b40238254b49e4e311087` (313 lignes).
- **Brouillon 6, rejeu 2** (fichier final, `e1680c41a180fea506bc5e80f9e686cf9efb42d6acdd3eef353dd5e7d2f21fcf`) : 19:45:22 à 19:51:18 UTC (5 min 56 s), `exit 0`, sortie identique octet pour octet au rejeu 1.
- Écart de cette sortie à la sortie v5 sur le brouillon 5 : cinq lignes, aucun chiffre de simulation (`diff`) : l. 3 (empreinte du bloc de paramètres), l. 95 (empreinte du texte hors bloc N4, § 8), l. 305 et 306 (§ 19 : écart au brouillon 4, chemin figé dans le script : 43 passages, 50 lignes du brouillon 4, 184 lignes du brouillon 6, 503 → 637 lignes hors bloc, empreinte de l'écart `3efc34bb…`) et l. 310 (bloc `parametres_bras_meta` identique au brouillon 4 : False, par la chaîne des indices de n6) ; les sections 1 à 7 et 10 à 18 sont identiques, le § 2, § 9 et § 16 (épreuve par le code v55) passent sur les définitions modifiées.
- Empreintes du brouillon 6 : bloc de paramètres (JSON canonique sans les deux champs libres) `08dd3c0d61145fd1ebfad254b72fada591e8c684533b790cdf8af38c329cf421` (brouillons 4 et 5 : `b2cc74e1…`) ; texte hors bloc N4 `079460f9ba4e5114cbf6f72349142fb52cee61231c47ea00028f47a3dcf9dcdb` (brouillon 5 : `5c01e16f…`) ; les deux calculées par le script de substitutions et retrouvées dans la sortie du script v5.
- La sortie du rejeu sur le brouillon 6 est **hors dépôt** (zone de travail `cl5-traitement/run6/`) : à verser avec compagnon par conv-audit, avec le brouillon 6, si Lazar le retient (R6) ; les chiffres cités par le brouillon 6 sont ceux de la sortie v5 (`16e5ff7e…`), inchangés.

### 4.4 Citations sur PDF (R7)

- Bettencourt et Kaiser 2015 (`2fb9aab0…`, compagnon conforme, 8 pages extraites) : « developing a giant connected component containing most authors » (résumé, p. 1) ; « one giant connected cluster emerged » (p. 3) ; « cascad » et « branching » : **aucune occurrence** dans le texte extrait. CA5-07 fondé.
- Uzzi et coll. 2013 (`53297098…`, compagnon conforme ; le PDF compte 6 pages, la première étant une page de garde : page 2 = p. 468, page 3 = p. 469, page 5 = p. 471) : « upper 5th percentile » à la p. 469 ; « 85th to 95th percentile of median conventionality » et « after which the relationship reverses » à la p. 471 (légende de la figure 4) : exacts, comme la contre-lecture 5 le dit.

### 4.5 Ce que je n'ai pas revérifié

- Les probabilités de simulation elles-mêmes (sections 3, 4, 5, 10 à 14, 17, 18 de la sortie) : je n'ai pas réimplémenté la simulation ; leur garantie est le rejeu identique du script (deux fois sur le brouillon 5 par ses rédacteurs, une fois par la contre-lecture 5, une fois par moi) et le recalcul indépendant de la contre-lecture 5 (concordance à 0,01).
- Ce que l'annexe et l'erratum rapportent des tours 1 et 2 (synthèses non lues ici).
- `forme_annexe_v56` sur le brouillon 6 (archive v56 non dépliée) : inféré « même forme » (un seul bloc `parametres_bras_meta`, mêmes clés et types).

## 5. Ce qui reste ouvert pour Lazar

1. **Contre-lecture du brouillon 6** (R2) par un modèle autre qu'Opus 5.5 et Fable 5.1 (Sonnet 5.5), entière ou limitée (décision de l'étape 3 de la section 9, défaut (i) entière) ; rien n'est scellé, aucun compagnon écrit.
2. **CA5-01, voie (i) ou (ii)** : le brouillon 6 écrit la voie (ii) (condition sur la liste A4 gelée, confirmation du détenteur de la configuration) ; la voie (i) (renommer `n1_…` à `n6_…`) reste possible, au prix d'un script v6 et d'une relecture entière.
3. **CA5-05** : retrait de « transfert » et « famille tenue à l'écart » des indices de n6 (empreinte du bloc de paramètres changée) ; alternative : les garder et faire chiffrer « l'axe 1 se range en partie en n6 » par un script v6.
4. **CA5-03** : libellé de l'issue observée et liste d'arrêt dans l'annexe (section 6) ou au préenregistrement brouillon 11.
5. **CA5-09** : erratum v2, deux corrections (« contre-lecture à venir » ; 0,12 / 0,13 pour (d)) : une version 3 de l'erratum, par conv-audit.
6. **Script v6** (si Lazar le demande) : colonne « repli », cas piégé de la garde des marqueurs, erreur-type du kappa, libellé `brouillon-1` dans la sortie, sensibilité n6 de l'axe 1 : tous hors mandat ici.
7. **Champ `contre_lecture`** : laissé « À REMPLIR » (section 2, dernier paragraphe) ; à remplir au scellement avec le rapport sur le brouillon relu ; `approbation_lazar` : à Lazar.
8. **Versement** : brouillon 6, script de substitutions, ce traitement et la sortie du rejeu sur le brouillon 6, avec compagnons, par conv-audit (aucun commit ici).
9. Inchangés et toujours ouverts : DEP10, l'option de N4 (CA1-05), CA1-04, c(n1, n2), la consigne figée du lecteur de niches, la dépense du désaccord (≤ 0,25 USD, sur devis).

*Fin. Ce document ne vaut pas approbation et ne gèle aucune valeur.*
