# Vérification courte du barreau 6 (« accumuler bat le score action par action »), candidat 5 — différentiel du candidat 2 au candidat 5 — v1

- **Vérificateur** : sous-agent neuf, Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le rédacteur des candidats 4 et 5 (Claude Opus 5.5). 11 novembre 2026, fin vers 13:10 UTC (`date -u`). N'a écrit ni le barreau 6, ni son code, ni sa revérification, ni aucune de ses contre-lectures, ni T0.7. **A lu T0.7 scellé (passages cités) et du code de C7 : exclu ensuite de tout rôle de lecteur de P3-bis.**
- **Objet** : `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat5.md` (`d4c7f96e738565ae4a9e9c1c9c834ecae3fb76f29ca24dfc1e75a269807985cb`), en différentiel du candidat 2 (`0716d3d52fd60f76b51c921ef8284580d70ddc587d855cfbc12381c1667baee1`, dernier texte vérifié, R-2278).
- **Règles tenues** : processeur seulement ; aucune dépense, aucune instance, aucun appel de modèle ; aucun chemin interdit ouvert ; aucun commit ; écarts de méthode déclarés au § 4.

## Verdict

**Scellable après corrections.** Deux couples exacts sont demandés (VB5-C1 et VB5-C4, constat VB5-6) : une même erreur de fait, écrite deux fois en sections gelées (« absent sous G-1 »). Ils ne changent aucun état, aucun seuil, aucun niveau. Quatre autres couples sont recommandés, au choix de la mère (VB5-C2 et VB5-C5 ensemble, VB5-C3, VB5-C6). **Aucun nœud.**

Réponses au mandat :

| question | réponse |
|---|---|
| 1. Scripts des candidats 3, 4 et 5 rejoués sur des copies | les trois textes sont refaits **à l'octet** ; sorties des scripts 4 et 5 égales aux sorties versées (VB5-1) |
| 2. Changements des sections gelées | 23 couples, tous rattachés à leur décision ; hors d'eux, les sept sections gelées du candidat 5 égalent celles du candidat 2 ; aucun signe, seuil, niveau ni règle d'état changé (VB5-2, VB5-3) |
| 3. Option (a) et sa réserve | écrites de façon claire et honnête ; une limite : rien n'oblige le verdict à porter la réserve (VB5-5, couple recommandé) |
| 4. Renvois à T0.7 scellé et au code ; `CODE-ACCB6` | tous exacts, sauf « absent sous G-1 » (VB5-4, VB5-6) ; `CODE-ACCB6` conforme (VB5-7) |
| 5. Cinq modules chargés par transitivité | oui, à ajouter, et quatre fichiers `__init__.py` avec eux : neuf fichiers ; recommandé, non bloquant (VB5-8) |
| 6. Verdict | scellable après VB5-C1 et VB5-C4 |

## 1. Lu (empreintes vérifiées par `sha256sum`)

| pièce | empreinte |
|---|---|
| candidats 2, 3, 4, 5 | `0716d3d5…`, `d48fb8a3…`, `e3aef530…`, `d4c7f96e…` (entières : en-tête de ce fichier et scripts) |
| pièces des candidats 3, 4 et 5 (couples, scripts, sorties, journaux) | 15 compagnons `.sha256`, tous égaux |
| vérification courte du candidat 2 | `prereg/contre-lectures/accumulation-barreau6-v1-candidat2-verification-courte-v1.md` (constats VB6-3 à VB6-7) |
| revérification sur T0.7 scellé, et ses couples RV | `80f06ac4f65cf798b2a25f1d2e4c56a2a21e570feb6cc307efdb2f229ecf9644` ; `771abfaff6a09bea103d67fa2f5521f69690c3795494fe99a815c0e71f15def7` |
| contre-lecture du code (CCB-1 à CCB-7) | `67614af4c82f35f98698ccf2768a259da4ca67e3c7d641e1c8a8dad63516df3c` |
| contre-lecture courte du code v2 | `a47d29796a38188b8b234530e5e81b9fc053a53b219e8f5af4b8be1cc8054237` |
| `registres/code-accb6/CODE-ACCB6-v1.json` ; `registres/accumulation-b6-v1.md` | `1957d087d92f31d0219531c06dc5d3ad8058ff5fe20ccfc6b183b1fb5fadc090` ; registre, une ligne |
| T0.7 scellé | `prereg/T0.7-sondes-v0-v1.md`, `d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5` : lignes 1198 à 1215 (« Métrique »), 1258 (« Seuil »), 1450 (plan), 1985 (« Liste d'arrêt »), et recherches de mots |
| code du barreau 6 | commit `282e295ec8e825b9c045bd30ebfdac3cbe55496f` (par `git show` et `git archive` vers le bac à sable) ; commit fils `536dd83e3effa1186fbbe9f5bae122119e4a95eb` |
| code de T0.7 | commit C7 `b4cd9953d199dd8f220f5162e5868c5b00fd392d` : `t07/lecture_v4.py` (lignes 189-216, 244-247, 636-692) et empreintes de fichiers |
| décisions | `registres/decisions.md`, lignes R-2272 à R-2281 et R-2330 à R-2341, entières ; `registres/go.md`, lignes GO-2026-11-10-05 et -09 |

## 2. Constats

**VB5-1 — Scripts rejoués : conformes.** Sur des copies, dans le bac à sable, par `python -I -B` :
- candidat 3 : 16 couples appliqués au candidat 2, texte obtenu `d48fb8a3…`, égal à l'octet au candidat 3 versé ;
- candidat 4 : 39 couples (RV-01 à RV-11 égaux à l'octet à leur origine, C4-01 à C4-28), 17 en sections gelées, texte obtenu `e3aef530…`, égal à l'octet ; sortie du script égale à la sortie versée (au chemin de sortie près) ;
- candidat 5 : 15 couples, 4 en sections gelées, texte obtenu `d4c7f96e…`, égal à l'octet ; sortie égale à la sortie versée ; `controle_ia.prereg.problemes` vide.

**VB5-2 — Sections gelées : rien hors des 23 couples déclarés. Conforme.** Par un programme à moi (pièce `differentiel_sections_gelees_vb5_v1.py`), sans reprendre les scripts du rédacteur : les 23 couples dont l'« ancien » tombe dans une section gelée (C3-10, C3-11, G4-01 à G4-17, G5-01 à G5-04), appliqués seuls au candidat 2, redonnent **à l'octet** les sept sections gelées du candidat 5. « Hypothèse » n'a pas changé. Mots retirés ou remplacés, sur tout le différentiel gelé : « 200 » → « 800 » (six fois), « même règle que » → « écart déclaré à », « à » → « une fois par la session mère avant », « 1,000 » → « 1 exactement », et la mise en liste de deux énumérations de fichiers. Tout le reste est de l'ajout. Lignes inchangées à l'octet : le niveau, les règles 2 à 7 de l'état d'un couple, l'état d'un jeu, la multiplicité, l'erreur de première espèce, la table des phrases (hors C3-11), les réserves R-B6, « ce qu'aucune issue ne permet ». Les 22 morceaux de phrases gelées que l'essai `test_accb6_phrases_texte_v1.py` recopie du candidat 2 figurent au candidat 5 à l'identique, sauf celui de « non interprétable » (C3-11).

**VB5-3 — Chaque changement gelé rattaché à sa décision. Conforme.**

| changement | décision | jugement |
|---|---|---|
| C3-10 (plan, point 6 : entropie tirée une fois avant l'inscription) | VB6-3, R-2274, R-2277 | justifié ; la valeur écrite est celle de R-2274 |
| C3-11 (« ([prédicteurs nommés]) ») | R-2279 | justifié ; égal au gabarit du code (`phrases_v1.py` l. 40) |
| G4-01, G4-02, G4-03, G4-06, G4-16 (200 → 800) | E-1, R-2330 | justifiés ; T0.7 scellé, l. 1198 et 1258 ; configuration v8 `n_plancher` = 800 ; code `etats_v1.N_DIRECTIONS = 800`, garde `lecture_v1.py` l. 205-206 |
| G4-02 (règle déclarée distincte), G4-14 (réserve) | E-2, option (a), R-2330 | justifiés ; voir VB5-5 |
| G4-04 (cause neuve de E), G4-07, G4-11 (renvois à `lecture_v4`) | E-4, R-2330 | justifiés ; renvois exacts (VB5-4) |
| G4-12 (réserves du plancher neuf recopiées) | E-3, R-2330, R-2336 | justifié ; égal au code (`reserves_t07_recopiees`, préfixe « plancher neuf de ») |
| G4-05 (CCB-6), G4-08 (CCB-5), G4-10 (CCB-2), G4-13 (CCB-4), G4-15 (CCB-3) | R-2281, R-2336 | justifiés ; chacun égal au code : exclusion par le point 4 ; lignes ôtées au chargement et champ `echec` lu ; codes 0, 2, 3 ; phrase sur la sortie standard (l. 774), motifs sur la sortie d'erreur (l. 764-772) ; `== 1.0` (l. 592), et 1 − 1/4096 = 0,99976 s'écrit bien 1,000 ; **une erreur de fait dans G4-08** (VB5-6) |
| G4-09, G4-17 (vérification au lancement, trois fichiers) | CCB-7, R-2281, Q-3 de R-2339 | justifiés |
| G5-01 (fichier écrit par `ecrire_fichier_code`, entropie de R-2274) | Q-1, R-2277, R-2339 | justifié ; lève une contradiction interne ; la fonction existe avec ce paramètre |
| G5-02, G5-04 (cinq fichiers de plus au lancement) | Q-3, R-2339 | justifiés ; huit empreintes exactes, dans l'ordre dit (VB5-4) |
| G5-03 (arrêt sur `resultat.reserves` hors de forme) | Q-4, R-2339, R-2336 | justifié ; égal au code, sauf sous G-1 (VB5-6) |

Aucune règle neuve ne touche un état. Trois ajouts règlent la conduite de la lecture et non son résultat : relance permise après une sortie hors des codes 0, 2 et 3 (CCB-2), sortie standard détournée (CCB-4), aucun lancement sur un écart de fichier (CCB-7). Chacun vient de sa décision.

**VB5-4 — Renvois à T0.7 scellé et au code : exacts (R6).** Recalculé ou relu :
- T0.7 scellé `d7d180ec…` ; ligne `SCELLEMENT-T07` du 2026-11-11T07:11:42Z ; configuration v8 `e31c7a79…` ; `CODE-T07-v2.json` `d5eb0b66…`, commit C7, 26 fichiers ; note d'erratum `f5936762…` ; brouillon 22 `8b84cba5…` ; rapport du développeur v2 `72642740…`.
- « `n_plancher` = 800, T0.7 scellé, « Métrique » » : l. 1198. Règle de la différence appariée D, « Seuil » : l. 1258. Motif « plancher neuf de la sonde figée non établi », « Liste d'arrêt » : l. 1985, avec « aucune lecture décisive contre les 200 directions de P3 ».
- `lecture_v4.etape_b`, l. 669-688 au commit C7 : exact ; les treize champs de E4 y sont, et `reserves` aussi. `lecture_v4.noter`, l. 214 : exact (`jetons_notes` > 0).
- `plancher_p3_<k>` : ce nom vient du code de C7 (`lecture_v4.py` l. 246), non du texte de T0.7, qui ne l'écrit nulle part. Le barreau 6 ne dit pas le contraire. Rien à changer.
- Les sept empreintes de l'en-tête (« code lu ») : égales au commit C7 et au commit `282e295e`. Les huit empreintes du plan, point 2 : égales au commit `282e295e`, dans l'ordre écrit ; égales aussi à C7 et à l'arbre de travail de `main`.
- Paquet au commit `282e295e` : six fichiers, empreintes du texte exactes (`etats_v1.py` `81e4a19b…`, `lecture_v1.py` `1f4c035f…`, `phrases_v1.py` `961ea2b3…`, `garde_v1.py` `5b91bfaa…`). Parent `6c98ea20…`, lui-même de parent `5ee8a4ac…`.
- Commit fils `536dd83e3effa1186fbbe9f5bae122119e4a95eb` : parent `282e295e…`, `src/` égal (`git diff --quiet`), un seul fichier ajouté, `bbd28591…`. **Suite `tests/test_accb6_*.py` rejouée** dans un arbre extrait : 208 essais, **207 passés, 1 sauté** (« un tuple ne vient pas d'un JSON »), en deux temps (§ 4, point 2).
- Énumération rejouée au commit `282e295e` : sortie `6b078d6c82c8bcc0dbbbb72b67c75731168d957c4aaf82ef3c54878db6f68fde`, 2 152 lignes, « couples 1152, jeux 343, séquence 33, phrases 604 ; cas sans état : 0 ; cas sans phrase : 0 » ; elle ne diffère de la sortie au commit `6c98ea20` (`00088af5…`) que par sa ligne 3. Script `a6dbfdd8…`.

**VB5-5 — Option (a) et sa réserve : claires et honnêtes. Une limite, couple recommandé.** Ce que le texte écrit, en trois lieux (« Métrique », « Critères de lecture gelés », « Puissance » point 11), est juste :
- la règle d'ici (borne basse de l'aire d'épisode strictement au-dessus du quantile 0,95) est dite **distincte** de celle de T0.7 scellé, qui est citée exactement ;
- le membre « au-dessus de son plancher » est dit **plus facile à obtenir** que son homonyme, avec la raison (règle quittée par T0.7 parce que son niveau n'est pas tenu sous un plancher à signal commun, R-2273) et l'aveu « non simulée ici à l'échelle de l'épisode » ;
- « le niveau tient à l'intervalle de Δ » : vérifié sur les règles gelées et sur le code. L'état A exige la borne basse de Δ > 0 **et** S_Σ au-dessus de son plancher ; M de même de l'autre côté (`lecture_v1.entrees_couple`). Une condition de plancher plus libérale ne peut donc pas donner un A ou un M de plus que l'intervalle de Δ seul. Elle rend seulement « sous le plancher » plus rare et « non départagé » plus fréquent.

Ce que la réserve ne cache pas, et qu'il faut dire à Lazar tel quel (pas 6 du « Reste ») : la phrase « établi » affirme deux choses, « la somme sépare mieux » et « au-dessus de son plancher ». Seule la première est tenue au niveau annoncé.

*Limite* : la réserve est « au texte seulement » (Q-2, gardé). Ni le code ni la phrase écrite dans `lecture-accb6.json` ne la portent, et rien dans le texte n'oblige le verdict à la recopier. Une phrase « établi … au-dessus de son plancher » peut donc arriver à Lazar sans elle. Ce qu'il faut, au choix de la mère : le couple **VB5-C3** (une phrase de plus dans la réserve), ou la même exigence dans la consigne du lecteur du verdict. Non bloquant.

*Sur la décision* : l'option (a) ne change aucune règle du texte que Lazar a vu (N-B6-1 à N-B6-3, R-2265) ; c'est T0.7 qui a changé. Ce n'est pas une modification de revendication. Le dire à Lazar suffit ; je ne vois pas de nœud.

**VB5-6 — « absent sous G-1 » : faux, deux fois, en sections gelées. Correction demandée.** Le plan, point 1 (G4-08), écrit que `resultat.reserves` est lu « sans être exigé (absent sous G-1) ». La liste d'arrêt (G5-03) écrit « champ non exigé, absent sous G-1 ». Or `lecture_v4.etape_b` (C7, l. 645-671) écrit le champ `reserves` dans `lecture-t07.json` **quelle que soit l'issue**, y compris quand les scores ne sont pas ouverts. Ce qui est vrai : sous G-1, le barreau 6 **ne lit pas** ce champ (`lecture_v1.lire` : `reserves_t07_recopiees` n'est appelée que si un calcul a lieu). Conséquence pour la liste d'arrêt : sous G-1, un champ hors de forme n'arrête pas, alors que la ligne gelée le laisse croire. Cas injouable sur une sortie de `lecture_v4` (CLB6-4) ; aucun état n'en dépend. Mais c'est une ligne d'arrêt gelée qui ne dit pas ce que fait le code, et elle ne se corrige plus après le scellement (R12). Couples **VB5-C1** et **VB5-C4**.

**VB5-7 — `CODE-ACCB6` : conforme à ce que le texte exige.**
- Fichier `registres/code-accb6/CODE-ACCB6-v1.json` : **recréé égal à l'octet** par `code_accb6_v1.ecrire_fichier_code(dépôt, 282e295e…, entropie=186246456082298562823446322699284949559)`, code importé de l'arbre extrait au commit (pièce `verifier_code_accb6_vb5_v1.py`). Clés `{commit, fichiers, entropie}` ; six fichiers, empreintes égales au commit ; forme acceptée par `garde_v1.lire_fichier_code` ; entropie de 128 bits, celle de R-2274, différente de celle de T0.7 (`141327499974890102043551261780374423878`).
- Compagnon `.sha256` égal ; `rg.sceau_conforme` passe.
- Ligne du registre propre : `| CODE-ACCB6 | 2026-11-11T12:51:23Z | registres/code-accb6/CODE-ACCB6-v1.json | 1957d087… |`, lue sans refus par `registre_v1.lire_registre_detail` ; une seule ligne ; rien dans `registres/scellements-v1.md`.
- Écrit par `ecrire_fichier_code` et non par la commande : comme l'exige le plan, point 2 (G5-01).
- Antériorités : aucune ligne `SCORES-T07`, aucun journal `registres/scellements-v1.md.ouvertures.md` à ce jour : la ligne précède toute ouverture des scores par T0.7. Le texte n'exige aucun ordre entre `CODE-ACCB6` et `SCELLEMENT-ACCB6`.
- Non refait : `code_accb6_v1 verifier` (il demande un arbre git au commit ; R-2341 le rapporte « conforme »). Le commit `282e295e` n'est pas un ancêtre de `main` aujourd'hui : attendu (écart E-5), la lecture se lance après la fusion.

**VB5-8 — Modules chargés hors de la liste du lancement : neuf fichiers, à ajouter. Recommandé, non bloquant.** L'observation du rédacteur est exacte et incomplète de quatre fichiers. Trace d'import au commit `282e295e` (pièce `trace-import-282e295e-vb5-v1.txt`), recoupée par un parcours de tous les imports internes, y compris ceux écrits dans une fonction : le paquet charge 23 fichiers de `src/controle_ia/`. Six sont le paquet (`CODE-ACCB6`). Huit sont dans la liste du plan, point 2. **Neuf n'y sont pas** :

| fichier | chargé par | appelé sur le chemin de la lecture ? | empreinte au commit `282e295e` |
|---|---|---|---|
| `src/controle_ia/prereg.py` | `manifeste.creer_manifeste` (l. 89), à l'écriture du manifeste | **oui** : `exiger_prereg_scelle` (garde de R1) | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` |
| `src/controle_ia/sondes/familles.py` | `sondes/evaluation.py`, `sondes/temoins.py` | non | `6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e` |
| `src/controle_ia/harnais/sondes.py` | `sondes/evaluation.py` | non | `f92657a69cf0d5781017e50117aeb1672dda60719aea51ffbfd9e566f3e7d94d` |
| `src/controle_ia/premier_test_ia/statistiques.py` | `t07/plancher_v1.py` | non | `a85525752fbdaa2fcee874d084eb11a671adadf1302340a3d71a5e09f0b11e2a` |
| `src/controle_ia/t07/__init__.py` | import du paquet `t07` | non (docstring seule) | `553bd9d29b56f0923859da2d3a63fadf9891c4274b9bb23fc367496e77e5a61e` |
| `src/controle_ia/__init__.py` | import | non (vide) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `src/controle_ia/sondes/__init__.py` | import | non (docstring seule) | `a4ea91421aa179aa7662876afddde30f6558435c6d60c5ee41f7793613b3ba30` |
| `src/controle_ia/harnais/__init__.py` | import | non (docstring seule) | `a977e6e9ad612aa96c099b9c5fb34bb42eb659261dd226780cfc441738b5caaa` |
| `src/controle_ia/premier_test_ia/__init__.py` | import | non (docstring seule) | `c72da1602f1998e4c7b30b670e89143d6a9c6337b903164f4bc6eed5ab9a5f92` |

Les neuf sont aujourd'hui égaux à C7 et à l'arbre de travail de `main`.

*Faut-il les ajouter ?* Le motif écrit par le texte reste vrai sans eux : aucun calcul décisif n'y vit. `aire_sous_courbe`, `intervalle_blocs`, `difference_aires_appariee`, `niveau_bonferroni` et `separation` n'en appellent aucune fonction (corps relus). Mais la vérification au lancement est la seule barrière contre une dérive du code chargé hors du paquet ; `prereg.py` porte une garde appelée ; un fichier chargé peut changer le comportement d'un autre à l'import ; et la liste actuelle contient déjà des fichiers sans calcul (`scellement.py`, `gardes.py`, `registre_v1.py`). « Tout fichier du dépôt que la lecture charge » est une règle plus simple à tenir qu'une liste choisie. Le coût est nul : la comparaison se fait à la main avant le lancement, et un écart mène à « aucun lancement, nœud », avant toute lecture. **Je recommande l'ajout** : couples **VB5-C2** (plan, point 2) et **VB5-C5** (liste d'arrêt), à appliquer ensemble ou pas du tout. Si la mère ne les prend pas, elle peut comparer ces neuf fichiers au lancement sans que le texte le dise : vérifier plus ne s'écarte pas du texte.

Hors de portée de toute liste, déclaré : les versions de numpy et de scipy (rangs, quantiles) ne sont tenues que par le manifeste du run.

**VB5-9 — États périmés hors sections gelées. Non bloquant.** Le candidat 5 a été écrit avant l'inscription de `CODE-ACCB6` (R-2341). L'en-tête (« Statut ») et le « Reste », pas 2 et 5, disent encore à faire le fichier et la ligne `CODE-ACCB6`, et cette vérification. À mettre à jour au texte final, hors sections gelées : couple **VB5-C6** pour le pas 2 ; le statut de l'en-tête et le pas 5 restent à la main de la mère, puisqu'ils citent l'empreinte de ce fichier.

**VB5-10 — Points laissés ouverts par d'autres, vus, non rouverts.** VB6-6 (lignes B6-D3b et B6-D4 de la table des prédictions) : déclaré ouvert au « Reste », pas 5, sans effet sur un état. La section « Contre-lecture » ne nomme que la contre-lecture 1 ; les vérifications courtes sont citées dans l'en-tête : suffisant. « Puissance », point 11 (non gelé) : la réserve « non resimulé à 800 » est écrite, et son raisonnement tient.

## 3. Couples proposés

Fichier : `prereg/contre-lectures/accumulation-barreau6-v1-candidat5-verification-courte-v1-pieces/couples-proposes-vb5-v1.json` (`272bd85a232f047ce07699371742b99a0da88b03daa3cffa2480f5bfa7220964`). Vérifié par programme (pièce `faire_couples_vb5_v1.py`) : chaque « ancien » figure une fois et une seule dans le candidat 5, dans la section dite ; ordre du texte ; aller-retour égal à l'octet ; les neuf empreintes de VB5-C2 recalculées au commit `282e295e` ; `prereg.problemes` vide sur le texte obtenu. Les six couples appliqués ensemble donnent `808ae30794c13ba5900a6acbeffee9d54f164dc96826841f4b8c7139a8221fc2`.

| couple | section | statut | ancien → nouveau |
|---|---|---|---|
| **VB5-C1** | Plan d'analyse, point 1 (gelée) | **demandé** | « sans être exigé (absent sous G-1), pour les seules réserves » → « sans être exigé (non lu sous G-1, où rien n'est lu), pour les seules réserves » |
| VB5-C2 | Plan d'analyse, point 2 (gelée) | recommandé | après la huitième empreinte, avant « , comparaison écrite avant le lancement » : les neuf fichiers de VB5-8 et leurs empreintes, dans l'ordre de la table (texte exact dans le fichier) |
| VB5-C3 | Critères de lecture gelés (gelée) | recommandé | « et ne se lit jamais comme lui ; le niveau de « accumuler bat » et de « le maximum bat » tient à l'intervalle de Δ » → « et ne se lit jamais comme lui ; le verdict recopie cette réserve à côté de toute phrase rapportée qui porte « au-dessus de son plancher » (VB5-5) ; le niveau de « accumuler bat » et de « le maximum bat » tient à l'intervalle de Δ » |
| **VB5-C4** | Liste d'arrêt (gelée) | **demandé** | « (champ non exigé, absent sous G-1 ; code v2, `lecture_v1.reserves_t07_recopiees` » → « (champ non exigé ; non lu sous G-1, où sa forme n'arrête donc pas ; code v2, `lecture_v1.reserves_t07_recopiees` » |
| VB5-C5 | Liste d'arrêt (gelée) | recommandé, avec VB5-C2 seulement | « `t07/plancher_v1.py` ou `t07/registre_v1.py` de l'arbre lancé différent de celui du commit cité : aucun lancement, nœud (plan, point 2 ; CCB-7 ; R-2339). » → « `t07/plancher_v1.py`, `t07/registre_v1.py` ou l'un des neuf autres fichiers chargés que nomme le plan, point 2, de l'arbre lancé différent de celui du commit cité : aucun lancement, nœud (plan, point 2 ; CCB-7 ; R-2339 ; VB5-8). » |
| VB5-C6 | Reste avant le scellement, pas 2 (non gelée) | recommandé | ajoute « **Fait** (R-2341) : fichier …, `1957d087…`, ligne `CODE-ACCB6` du 2026-11-11T12:51:23Z … » (texte exact dans le fichier) |

Aucun de ces couples ne retire un chiffre, un signe de comparaison ni « strictement ». Mots retirés ou remplacés : « absent » → « non lu » (deux fois), « ou » → « , » (une fois).

Après application, une relecture entière n'est pas nécessaire : il suffit de vérifier par programme que le texte final ne diffère du candidat 5 que par les couples retenus et par les couples d'en-tête de la mère.

## 4. Écarts de méthode, déclarés

1. Commandes git, toutes de lecture : `show`, `archive` (vers le bac à sable), `ls-tree`, `rev-parse`, `diff --quiet`, `diff --stat`, `cat-file`, `merge-base`, `branch --contains`, `log`, `status`. `git status` a montré des noms de fichiers de P3-bis sous `brouillons/` ; rien n'en a été ouvert.
2. La suite a tourné dans un arbre extrait par `git archive` de `536dd83e` (`src/controle_ia`, les essais `test_accb6_*`, `conftest.py`, `pyproject.toml`, l'énumération), non dans un arbre git. Premier passage : 205 passés, 2 sautés, 1 en échec. L'échec et un des deux sauts venaient de mon extraction : compagnon `.sha256` de la sortie d'énumération non extrait ; candidat 2 absent de l'arbre. Extraction complétée (candidat 2 copié du dépôt, empreinte `0716d3d5…`), ces deux essais rejoués seuls : passés. D'où 207 passés, 1 sauté. Sortie du premier passage versée telle quelle.
3. `ecrire_fichier_code` a été appelée avec le dépôt en lecture et une sortie dans le bac à sable ; rien n'a été écrit dans le dépôt hors de ce fichier et de son dossier de pièces.
4. De T0.7 scellé, seules les lignes citées et des recherches de mots ont été lues ; les sections « Hypothèse », « Prédiction » et « Critères » de T0.7 ne l'ont pas été.
5. Lu en plus de la consigne : `registres/go.md` (deux lignes), la configuration v8 de T0.7 (cinq clés), `CODE-T07-v2.json` (commit et nombre de fichiers), `registres/scellements-v1.md` (lignes `CODE-T07` et `SCELLEMENT-T07`).

## 5. Non fait

- Banc de mutations non rejoué (128 sur 128 : chiffre des rapports, R-2336, R-2338).
- Essai de la revérification sur sorties jouets de `lecture_v4` non rejoué (rejoué par la contre-lecture courte du code v2).
- Aucune relecture du code hors des passages que les couples gelés citent.
- Sections non gelées : lues pour la cohérence (en-tête, « Ce que les auteurs savaient », « Lignes de registre », « Code », « Reste »), non vérifiées couple par couple, sauf les couples de « Puissance » (RV-10, C4-19) et de la fusion (RV-11).

## 6. Pièces

Dossier `prereg/contre-lectures/accumulation-barreau6-v1-candidat5-verification-courte-v1-pieces/` (chacune avec son compagnon `.sha256`) :

| pièce | rôle | sha256 |
|---|---|---|
| `couples-proposes-vb5-v1.json` | les six couples exacts | `272bd85a232f047ce07699371742b99a0da88b03daa3cffa2480f5bfa7220964` |
| `faire_couples_vb5_v1.py` | fabrique et contrôle des couples | `eb3e96c905b6d3d6d2d5c6acc62338992668370554fc8db228c66253b5e14a2a` |
| `differentiel_sections_gelees_vb5_v1.py` | différentiel indépendant des sections gelées, candidat 2 → 5 | `f3534026b7f99f38269bfbd8a695b141b080ea461c5adce5d695278e2bf13bc2` |
| `trace_import_vb5_v1.py`, `trace-import-282e295e-vb5-v1.txt` | fichiers du dépôt chargés par le paquet, avec empreintes | `b49cab862d41fbdbccb66faf4310a9c393cee1a9312da5707db7da9ba5fe2e80`, `fb2818c3449f321f9ba486259f003fcd86d25179e4cc2b5531256c7561507255` |
| `verifier_code_accb6_vb5_v1.py` | fichier de `CODE-ACCB6` recréé, ligne et sceau relus | `bc6aad4dd7aae195b9e23b08db07eca5cd9eca66c76b5ebb5a536dee1e838940` |
| `suite-accb6-536dd83e-vb5-v1.txt` | premier passage de la suite (§ 4, point 2) | `a055e84996bbfcb7a3cee7bbaa63aa3e5c096de74e36973b2b392072b55aaa07` |

Les scripts et les sorties citent les chemins de mon bac à sable, non durable.
