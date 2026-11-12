# Journal — socle de preuves pour l'entretien avec le Transformative AI Fund — v4

- **Rédacteur** : sous-agent neuf (rédacteur) de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, Claude Opus 5.5
  (`claude-opus-5-5`) ; je n'ai écrit ni les versions 1 à 3 du socle, ni leurs journaux, ni leurs contre-lectures, ni aucune
  pièce citée.
- **Heures** (`date -u`, 10 novembre 2026) : consigne vérifiée et lue en entier, début **12:28:59** ; registres relevés à
  12:29:27 (décisions jusqu'à R-2218), 12:33:18 (R-2219 paru) et 12:39:39 (inchangés) ; application finale et heure de fin
  écrite dans la v4 : **12:39:46** ; sortie comparée à l'essai : 12:40:10 ; registre relu à 12:44:37 (R-2220 et R-2221
  parues après l'application : section 2 bis) ; fin du journal : dernière ligne (heure relevée dans la commande qui l'écrit,
  juste avant son scellement).
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-socle-preuves-v4-v1.md`
  (`f25b2ecfbc1102bb9945b0260b0705c72309ac0fd3a516c18e0990b20c8b10f3`, égale à son compagnon) ; interdits communs v2
  (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, empreinte du fichier source vérifiée) et interdits
  propres (cloison du bras ; aucun taux de calibration, nombres bruts 33, 7, 6 seulement ; niveau méthode) tenus.
- **Sorties** (seuls chemins écrits au dépôt) : `brouillons/entretien-taif-v3/socle-preuves-entretien-v4.md`
  (`b1c76e273f4b939b0b7fb80c00975d6efeb30e24748b239233fc0a823d3bcb30`) et ce journal, chacun avec son compagnon `.sha256`
  écrit par `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller`. **Aucun commit.** La v3 (`b9377f1d…`) et son
  journal (`2276733f…`) sont intacts (empreinte de la v3 recalculée après le scellement de la v4 : inchangée).
- **Jalons** : (1) v4 écrite par le programme et scellée (`verifier` : OK ; garde finale : saine) ; (2) ce journal, scellé à
  sa fin.
- **Outils, hors dépôt** (bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-socle-v4/`) :
  `appliquer_socle_v4.py` (`8fcea1544821357eafeaaa4501e9a86029f1cf69a3f962fede1af0cf95c4874d`), qui a écrit la v4 ;
  `appliquer_socle_v4-b.py` (`83c7045fde6b6aa2a4a683c7cc31a826a8c08b9ba9a7e29ef77c9175324c4045`), recopié en annexe A ;
  `essais_gardes-b.py` (`3dae137ad3d37e85ee46ba06637ae331bbffb3fc601810520894bdf2365aa185`), recopié en annexe B. La version b
  ne diffère de la première que par la garde finale, qui compare des **empreintes** de taux au lieu des taux en clair (la
  première les écrivait en clair : la recopier ici aurait fait entrer des taux de calibration dans une pièce du dépôt) ;
  `MODIFS`, l'en-tête et `AJOUTS` sont identiques (vérifié par `diff`), et **la version b reproduit la v4 scellée à
  l'octet** (essai 5 de l'annexe B).

## 1. Procédure d'application, par programme

Commande (racine du dépôt) : `.venv/bin/python -I appliquer_socle_v4.py /home/user/controle-ia-travail brouillons/entretien-taif-v3/socle-preuves-entretien-v4.md 12:39:46`, code 0 ; puis `sceller`.

1. **Empreintes** exigées, arrêt sinon : v3 `b9377f1d…`, contre-lecture `3a1df795…`.
2. **Extraction des couples** de la contre-lecture par motif (`**Cnn** — lieu`, bloc `ANCIEN :`, bloc `NOUVEAU :`) :
   exactement C01 à C50, dans l'ordre, arrêt sinon. Les textes anciens, et les textes nouveaux non modifiés, sont donc les
   caractères mêmes de la contre-lecture.
3. **Douze textes nouveaux remplacés** (section 3) ; **treize ajouts** (section 4), chacun un couple texte ancien de la v3 →
   texte nouveau, traité comme les couples.
4. **Unicité** : chaque texte ancien (50 couples et 13 ajouts) est cherché dans la v3 par un motif où toute suite de blancs
   (espaces, retours à la ligne, retraits) vaut toute autre ; **63 sur 63 trouvés une fois et une seule** ; aucun
   chevauchement entre les 63 empans ; arrêt (code 2) sinon.
5. **Remplacement** par empans ; chaque texte nouveau vérifié présent dans la sortie.
6. **Garde finale** (refus si trouvé) : neuf taux de calibration connus, reconnus par empreinte, et la phrase retirée du
   § 2.5. Sortie : 719 lignes → 740 lignes.

**Essais des gardes (règle 5), neuf sur neuf conformes** (annexe B, code 0) : garde sur la v3 → refus (phrase du bras) ;
garde sur la contre-lecture cl1 → refus (trois taux qu'elle cite et la phrase du bras) ; garde sur l'essai et sur la v4
scellée → saine ; reproduction de la v4 scellée à l'octet → égale ; empreinte de la v3 altérée d'un blanc → arrêt ; texte
ancien en double → arrêt ; texte ancien absent → arrêt ; faux dépôt identique à la v3 → aucun arrêt. La sortie finale ne
diffère de l'essai à blanc (fin fixée à 12:00:00) que par la ligne 6 (heure de fin), vérifié par `diff`.

## 2. Les 50 couples : statut et relevé

« tel quel » : texte nouveau de la contre-lecture appliqué sans changement. « l. v3 » : ligne de la v3 où commence le texte
ancien. Relevés contre `registres/decisions.md` (`2c5ee45e…`, dernière ligne R-2219, l. 2177), `registres/go.md`
(`2c396b01…`), `registres/depenses.md` (`5268f0f0…`), `registres/etat.md` (`1ef56d65…`), `registres/scellements-v1.md`
(`0651adca…`), tous inchangés entre 12:33:18 et 12:39:39.

| couple | lieu | l. v3 | statut | relevé ou remarque |
|---|---|---|---|---|
| C01 | § 0, ligne 2 | 74 | tel quel | `registres/depenses.md` l. 414 : ligne d'A1-v4 sous GO-2026-11-02-22, « non rapproché d une facture », machine de l'hôte (GO-2026-11-08-12) « non relevée » ; R-2158 : conforme |
| C02 | § 1.4, chiffres exacts | 176 | tel quel | même relevé |
| C03 | § 1.4, état | 177 | tel quel | conforme ; aucune table de dépense régénérée sur `main` (`livrables/registres-taif-v4/total-depenses-v3.md` reste la plus récente) |
| C04 à C09 | § 2.4, § 3, § 4, Q2, § 6 point 1 | 464, 500, 530, 583, 595, 663 | tels quels | même relevé que C01 |
| C10 | § 2.4, Restent | 466 | tel quel | R-2162 (10:45) : « (a) go publication », commit public `6510199` ; `livrables/page-publique-organisme-2026-11-10-v1/` présent sur `main` (README, contre-lecture, journaux) ; aucun nouveau « go publication » au registre jusqu'à R-2219 : conforme |
| C11, C12 | § 3 ; § 6 point 13 | 497, 691 | tels quels | même relevé |
| C13 | § 1.1 bis, deux rangées neuves | 129 | tel quel | rapport du lot 5-A (`aef81e6e…`, égal à son compagnon sur `prep/etat-de-l-art-niveau3-pieces-v1`, tête `10016a61`) : § 0, points 1 et 2, relus : conformes ; pages non recopiées de son annexe A (la réserve du contre-lecteur reste écrite) |
| C14 | § 1.1 bis, rangée HELIOS | 127 | **modifié** | section 3 |
| C15 | § 1.6, écart 9 | 216 | **modifié** | section 3 |
| C16 | § 1.1, pièces | 108 | tel quel | R-2180, R-2188 (« 2606.08892v3 sans changement de verdict ») : conforme |
| C17 | § 2.4, [K15], fin | 424 | **modifié** | section 3 |
| C18 | § 6, point 10 | 687 | tel quel | cohérent avec C17 |
| C19 | § 0, ligne 1 | 68 | tel quel | R-2177 : conforme ; aucun calendrier plus récent au registre |
| C20, C21 | § 0, ligne 3 ; § 4, rangée du 12 | 77, 518 | tels quels | R-2155, R-2158, R-2166, R-2174, R-2183 : conformes ; aucune ligne neuve sur le lot v3 des concepts jusqu'à R-2219 |
| C22 | § 6, point 5 | 673 | **modifié** | section 3 |
| C23 | § 4, chapeau | 509 | tel quel | R-2177 : conforme |
| C24 | § 1.4, chiffres exacts | 176 | **modifié** | section 3 |
| C25 à C29 | § 2.2 ; § 4 (18 ; sous le tableau) ; Q4 ; § 6 point 4 | 332, 524, 535, 618, 671 | **modifiés** | section 3 (base (A) scellée, R-2216) |
| C30, C31 | § 2.1, état ; § 7, point 2 | 255, 705 | tels quels | brouillon 11 de P3-bis le dernier du dossier (aucun brouillon 12 sur disque) ; aucune ligne de P3-bis dans `registres/scellements-v1.md` ; R-2197, R-2198 : conformes |
| C32 | § 1.3, chiffres exacts | 162 | **modifié** | section 3 |
| C33 | § 6, point 15 | 698 | tel quel | `bd994163…` absent de `main` (`git grep` dans les compagnons `.sha256`, exclusions de la règle 9 : aucune occurrence) ; lecture (c) : R-2195 « à confirmer par Lazar », R-2204 écrit « Lazar a choisi les nombres bruts sans taux », R-2213 la retient ; aucune confirmation écrite de Lazar au registre jusqu'à R-2219 : texte gardé |
| C34, C35 | § 2.4, [K15] ; § 0, ligne 4 | 419, 85 | tels quels | rapport C7 (`63d83737…`, égal à son compagnon sur `prep/etat-de-l-art-niveau3-v1`, tête `f0aaf0d1`) ; R-2184 : conformes ; lignes 25-29, 49-53, 445 de C7 non relues par moi (reprises du contre-lecteur) |
| C36 | § 0, ligne 4 | 81 | tel quel | — |
| C37 à C41 | en-tête ; § 0 ; § 1.7 ; § 6 point 14 | 17, 78, 228, 230, 696 | tels quels | — |
| C42 | § 5, Q1, Réponse | 568 | **modifié** | section 3 |
| C43 | § 1.1, état | 110 | tel quel | `registres/etat.md` l. 179 : « restent le hors-arXiv et le contrôle de traçabilité » : conforme |
| C44 | § 1.6, écart 7 | 214 | tel quel | l. 245 : la proposition EA Funds v1 « garde deux formulations jugées inexactes (« I set the questions and take every de[cision] » » : conforme |
| C45 | § 1.6, écart 8 | 215 | tel quel | l. 181 : « pas de run B : non prouvé » : conforme |
| C46, C47 | § 4 (jusqu'au 9) ; Q4 | 515, 614 | tels quels | l. 190 : « Critères de G0 prouvés : 1 […] et 5 » : conforme |
| C48 à C50 | § 2.4 ; § 1.4 ; en-tête | 434, 176, 36 | tels quels | — |

**Compte** : 38 couples tels quels, 12 modifiés, 0 écarté.

### 2 bis. Lignes parues après l'application (relevé de 12:44:37, `registres/decisions.md` `5f3ef18b…`)

La v4 est scellée à 12:39:46 avec « registre des décisions lu jusqu'à sa dernière ligne, R-2219 », exact à cette heure
(2 177 lignes à 12:39:39). Deux lignes sont parues ensuite, lues en entier ; registres des autorisations, des dépenses,
de l'état et des scellements inchangés. **Aucune ne rend fausse une phrase de la v4** ; la v4 n'est pas réécrite (règle 12).

- **R-2220 (1)** : module T0.7 option (c) rendu, commit **proposé** pour `CODE-T07` (`37485ce5…`), un essai en échec sur un
  commit inatteignable depuis `main`, contre-lecture courte lancée. La v4 dit « ligne `CODE-T07` non inscrite » (§ 6 point 5) :
  toujours vrai. La colonne « en cours » du 10 au § 4 reste périmée (déjà déclaré, § 7 point 9 de la v4).
- **R-2220 (2), constat neuf** : GO-2026-11-10-10 exige la « configuration v5 `995eb918…` » alors que le code v65 porte une
  configuration v5 d'une autre empreinte ; la condition de la ligne est « à faire préciser par Lazar ». La v4 écrit, au
  couple C24, « organisme 45, sous les conditions de GO-2026-11-08-02 — son code v65 […] est repris en v66, en cours » : pas
  faux, mais **incomplet depuis R-2220** ; à ajouter à la version suivante ou à dire avec ce passage.
- **R-2221** : inventaire des idées de l'organisme rendu ; aucun passage du socle n'en parle. Son exposition déclarée
  (cloison) ne concerne pas ce travail ; je n'ai lu aucune des lignes qu'elle nomme.

## 3. Couples modifiés : ce qui change par rapport au texte nouveau de la contre-lecture, et pourquoi

Le texte exact de chaque texte nouveau de la v4 est dans `MODIFS` (annexe A). Seul ce qui diffère du texte de la
contre-lecture est décrit ici.

| couple | changement | raison | source |
|---|---|---|---|
| C14 | « verdicts repris de messages, à contrôler sur le rapport du lot 7-B » → précisé : 2611.02153 lit les représentations internes de copies d'un même modèle, 2611.10620 des scores de sondes par agent ; aucune ne vient des équipes que nomme le déclencheur, aucune ne publie de test séquentiel toujours valide sur sondes ; « contrôlé sur le rapport du lot 7-B » avec chemin, branche, empreinte et paragraphes ; « non recontrôlé sur PDF pour ce socle » ; la mention « verdicts repris de messages » est gardée pour le complément de la synthèse | lever le « à contrôler » du contre-lecteur, que j'ai pu faire sur le rapport ; « sur états internes d'agents à modèle partagé » valait pour 2611.02153 seulement | `docs/sources/lecture-pdf-niveau3/rapport-lot7B-collusion-papier-B-v1.md` (`bf9b6af8f2d8a51ae406e8bcd2c53c3eff698826ecf916700ec7ae0dd206633c`, égal à son compagnon), § 0.1 points 1 et 2, § 0.2 (« Déclencheur de bascule à examiner par Lazar (nœud de décision, je ne tranche pas) ») ; R-2190 |
| C15 | ajout : « R-2190 range aussi parmi les nœuds de revendication H8, H6 (2605.26047) et la prédiction 1 de HC1, contredite (2606.05384) » | relevé : la liste de R-2190, dernière inscrite, nomme ces trois nœuds que le texte de la contre-lecture omettait | R-2190 |
| C17 | « rapport `rapport-lot7A-sondes-agents-H1-H2-v1.md`, à citer avec son empreinte » → chemin complet, branche, empreinte `8a6dd0e0…`, « En tête », points 1 et 4 | remplir le « à citer avec son empreinte » ; points vérifiés : « Aucun des trois articles n'occupe H1 ni H2 » (point 1) ; classifieur TF-IDF qui égale la sonde (point 4) | `docs/sources/lecture-pdf-niveau3/rapport-lot7A-sondes-agents-H1-H2-v1.md` (`8a6dd0e0184a7afbf3cbc10e08eb9685817135ed7bcb9503ae095f9f169c3f1e`, égal à son compagnon) ; R-2188. Non écrit au socle : le même rapport voit en 2610.17301 un voisin fort de H8, « en lecture dure » occupation partielle (point 2) — H8 figure parmi les nœuds de R-2190 (C15) |
| C22 | ajout à la fin : consigne de l'audit des fuites de T0.7 (brouillon 3, `0d51099e…`) et validité de l'adaptateur (brouillon 3, `defd8ef0…`) rendus, non scellés | statuts nommés par la consigne (R-2210, R-2212) ; le point 5 du § 6 liste ce qui n'est pas scellé | R-2210, R-2212 ; empreintes recalculées sur `main` |
| C24 | ajout dans -10 : « sous les conditions de GO-2026-11-08-02 — son code v65, contre-lu « utilisable pour la course après corrections », est repris en v66, en cours, R-2215 — » | statut nommé par la consigne (code v65 contre-lu, v66 en cours) | R-2215 ; `docs/notes/organisme-boucle-reelle-v1/code-v65/contre-lecture-code-v65-v2.md` (`c4ddfc7f…`) ; `registres/go.md` l. 297-300 relues (GO-2026-11-10-07 à -10) |
| C25 | « est scellée à part, avant la création de 7b […] (R-2175 ; brouillon 2 rendu, douze traits accordés, R-2209, R-2211) » → « est **scellée à part le 10 novembre** (ligne `SCELLEMENT-T08-BASE-A` à 12:21:55, avant toute création de 7b ; `prereg/T0.8-base-A-mots-et-cout-v1.md`, `72b067d5…` ; R-2216), sur le mot de Lazar (R-2175), après contre-lecture et vérification courte (douze traits accordés, R-2211) » | relevé : le scellement (R-2216, 12:21) est postérieur à la contre-lecture (12:13) | R-2216 ; `registres/scellements-v1.md` l. 5 ; empreinte du texte scellé recalculée : `72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d` |
| C26, C27, C28, C29 | « base (A) scellée à part avant 7b, R-2175 » ou « à sceller à part avant 7b » → « scellée à part le 10 (novembre), R-2216 » (R-2175 gardé où il était) | même relevé | R-2216 |
| C32 | « absente de `main` » → « absente de `main` au relevé de la v4 » ; ajout : antériorité du scellement des séries de prédictions selon R-2218 (aucune pièce unique ne l'atteste série par série ; établie pour la plupart, par le seul registre pour deux, non établie pour l'heure de scellement de trois textes d'analyse du rejeu R1-R2 sur `main` ni pour les deux premières courses d'A1-v3) | statut nommé par la consigne (réponses pour le registre des prédictions, R-2218) ; c'est une faiblesse de l'affirmation 1.3 qu'un juré peut sonder | R-2218 ; `docs/notes/entretien-resultats-v1/reponses-mere-registre-predictions-v1.md` (`9639b715c8006a118ab8cdd3908edae62826a78bedf31d204c289118ca9aebd8`, égale à son compagnon) **non relue** : le socle le dit |
| C42 | « (GO-2026-11-10-07 ; R-2175, R-2207), son texte n'est pas scellé (R-2210) » → « (GO-2026-11-10-07, lecture large : R-2175, R-2207) ; son texte (validité de l'adaptateur, brouillon 3, `defd8ef0…`) n'est pas scellé : il attend une contre-lecture différentielle sur T0.7 scellé (R-2210) » | statuts nommés par la consigne (validité b3, lecture large de GO-07) | R-2207, R-2210 ; `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon3.md` (`defd8ef05038e703c24733f6a5f88a1153daf5f44d2b8cae14950a5643e875fd`) |

## 4. Ajouts AJ01 à AJ13 (hors couples), même règle d'unicité

| ajout | lieu (l. v3) | ce qui change | raison |
|---|---|---|---|
| AJ01 | titre (1) | titre « — v4 » et en-tête de la v4 (rédacteur, session mère actuelle, consigne, ce que fait et ne fait pas la v4, statut « non contre-lu ») ; l'en-tête de la v3 est conservé dessous | règle 12 ; mineur CLS-09 (e) du contre-lecteur (session de la version suivante) |
| AJ02 | § 0, ligne 4 (78) | « au niveau 3 (rapports de lots ; leur synthèse est **provisoire**, `8adb561d…`, R-2190) » | consigne : « la synthèse de l'état de l'art niveau 3 reste provisoire : dis-le là où elle est citée » |
| AJ03 | § 1.1, état (110) | « R-2190 » et « sa synthèse est **provisoire**, `8adb561d…` » | idem |
| AJ04 | § 1.1 bis, chapeau (114) | rapports des lots 5-A et 7-B nommés pour ce que R-2181 et R-2190 ajoutent (C13, C14) ; synthèse **provisoire**, table à réaligner sur la synthèse finale | idem ; point ouvert 2 du contre-lecteur |
| AJ05 | § 5, Q5, [K18] (647) | synthèse **provisoire** ; renvoi à l'écart 9 pour la liste des occupations partielles relevées au registre | idem ; Q5 nomme trois occupations, l'écart 9 (C15) les tient à jour |
| AJ06 | § 2.2, préalable (4) (327) | chemin de l'addendum du bras B : `docs/notes/g0-deux-semaines-v1/scellement-course-t06-v1/pieces-apres-couples/addendum-bras-b-v2-brouillon-v3-apres-couples-v1.md` | mineur CLS-09 (f) ; empreinte recalculée sur `main` : `1a372523290fdaf0a606db592295885f01ff9d6adc9b877fd72279fc6a44ccdf` (le bras B est celui de l'audit de fuite, non le bras d'attaque ; fichier haché, non lu) |
| AJ07 | § 2.2, préalable (2) (325) | « brouillon 4 lancé (R-2143) » → « brouillon 4 rendu (R-2160 : chemin, `5f2167d7…`), non scellé, contre-lecture de son différentiel à faire avant le scellement » | relevé : R-2160 (10:43) ; empreinte recalculée `5f2167d705795db3d8e8850bbcf6cfc0c07750634d030b0ba0598379f4f8aef7` ; aucun brouillon 5 ni scellement de l'ordre sur disque |
| AJ08 | § 2.5, première puce (474) | « Phrase sûre pour l'entretien : « monté ; … » » → « **État du bras** : **état du bras non vérifiable par la mère (cloison)** ; ce qui a tourné ou non, et la phrase à dire au jury, reviennent à Lazar à la date de l'entretien » | consigne, mot pour mot pour la formule ; point ouvert 1 du contre-lecteur |
| AJ09 | § 3, rangée d'A1-v4, colonne « qui » (497) | « rédacteur neuf, contre-lecture, poussée par la mère (R-2131) ; Lazar pour les citations » → « publiée par la mère sur le mot de Lazar (R-2162) ; mise à jour : Lazar (nouveau « go publication », R-2177) » | même cellule de tableau que C11, que le couple laissait contradictoire (CLS-02) |
| AJ10 | § 1.4, pièces (175) | empreintes des deux registres vivants à la v2 et au relevé de la v4 | C01, C02 et C24 citent des lignes (l. 414 ; l. 297-300) absentes des versions `e7b83d37…` et `e682abb0…` |
| AJ11 | § 5, Q4 (618) | « la règle « mots et coût », qui attend le texte de T0.8 (R-2070) » → « scellée à part le 10 novembre (base (A) de T0.8, R-2216 ; elle attendait le texte de T0.8, R-2070) » | relevé R-2216 : la phrase était devenue fausse, hors du couple C28 qui la suit |
| AJ12 | § 6, point 4 (671) | « règle « mots et coût » » retirée de ce qu'attend T0.8 ; « (la règle « mots et coût » n'en dépend plus : base (A) scellée à part, R-2216) » | idem, hors du couple C29 |
| AJ13 | § 7, après le point 8 (718) | point 9 neuf : ce que la v4 relève, ce qui reste à l'état de la v2 ou de la v3, synthèse provisoire, bras non vérifiable, lecture (c) à faire confirmer, v4 non contre-lue | réserves du rédacteur de la v4 ; le point 8 ne vaut plus que pour la v3 |

## 5. Statuts nommés par la consigne : où ils sont portés

| statut (registre) | relevé | porté par |
|---|---|---|
| GO-2026-11-10-10 inscrit (R-2206) | `registres/go.md` l. 300, `2c396b01…` | C24 (texte de la contre-lecture) |
| base (A) scellée (R-2216) | `registres/scellements-v1.md` l. 5, 12:21:55 ; `72b067d5…` | C25 à C29 modifiés ; AJ11, AJ12 |
| validité de l'adaptateur, brouillon 3 (R-2210) | `defd8ef0…` sur `main` ; non scellé | C42, C22 modifiés |
| lecture large de GO-07 (R-2207) | ligne de `registres/go.md` non modifiée (R-2207) | C24 (contre-lecture) ; C42 |
| CLBA-04 (a) (R-2211) | douze traits | C25 |
| consigne d'audit, brouillon 3 (R-2212) | `0d51099e…` sur `main` ; non scellée | C22 |
| code v65 contre-lu, v66 en cours (R-2215) | `c4ddfc7f…` | C24 |
| sections de résultats v4 (R-2217) ; v5 (R-2219, paru pendant le relevé) | — | **non porté** : aucun passage du socle ne parle des sections de résultats ni du dossier fusionné ; rien à corriger |
| réponses pour le registre des prédictions (R-2218) | `9639b715…`, non relu | C32 |
| hors liste : ordre de 7b, brouillon 4 (R-2160) | `5f2167d7…` | AJ07 |
| hors liste : page publique publiée (R-2162) | pièces sous `livrables/page-publique-organisme-2026-11-10-v1/` | C10 à C12 ; AJ09 |

## 6. Points ouverts et mineurs du contre-lecteur

1. « Monté ; rien n'a encore tourné » (§ 2.5) : remplacé par la formule de la consigne (AJ08) ; la garde finale refuse la
   phrase ancienne.
2. Synthèse de niveau 3 provisoire (`8adb561d…`, complément `a4176d46…`) : dite au § 0, au § 1.1, au chapeau du § 1.1 bis,
   à l'écart 9 (C15), à la rangée HELIOS (C14), à Q5 et au § 7 point 9. Le réalignement sur la synthèse finale reste à faire.
3. Lecture (c) de R-2195 : gardée « à faire confirmer par Lazar » (C32, § 7 point 9) ; aucune confirmation écrite au registre
   jusqu'à R-2219 (R-2204 et R-2213 la tiennent pour acquise : écart de formulation entre lignes du registre, signalé).
4. Statuts relevés au moment de l'application (12:33:18 à 12:39:39) : section 2.
5. Journal de la v3 : il porte K17 (« faible sous 27 milliards ») et K19 (« recompte en cours ») ; il est scellé et n'est pas
   touché. Ici : la formule de K17 n'était au socle qu'au § 0, corrigée par C36 (Q1 disait déjà juste : « 0,585 à 0,781 à 2
   milliards de paramètres, bonnes à partir de 27 ») ; K19 est remplacé par C32 et C33.
6. CLS-09 (e) : AJ01 ; CLS-09 (f) : AJ06.
7. Limites du contre-lecteur reprises telles quelles : pages du lot 5-A non recopiées de son annexe (C13) ; pièce
   `bd994163…` non ouverte (C32, C33).

## 7. Sources lues, avec empreintes

| pièce | chemin | sha256 | contrôle |
|---|---|---|---|
| consigne | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-socle-preuves-v4-v1.md` | `f25b2ecfbc1102bb9945b0260b0705c72309ac0fd3a516c18e0990b20c8b10f3` | égale au compagnon ; lue en entier |
| interdits communs v2 | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` | `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` | égale à la consigne ; texte lu dans la consigne |
| socle v3 | `brouillons/entretien-taif-v3/socle-preuves-entretien-v3.md` | `b9377f1dfc72082a1c95224b7a3746cce5b575ec1a2e6dae882394c6b3f36265` | égale au compagnon ; lue en entier ; inchangée après le scellement de la v4 |
| journal v3 | `brouillons/entretien-taif-v3/socle-preuves-entretien-v3-journal.md` | `2276733f1e43f51f3511550b401dca7fb60d8afb886dc18fdfad0c649b8757f1` | lu en entier |
| contre-lecture de la v3 | `prereg/contre-lectures/socle-preuves-entretien-v3-cl1.md` | `3a1df7959475b440e61193500d44f58b72dd433e928dbba338452875cb45079b` | égale au compagnon ; lue en entier |
| registre des décisions | `registres/decisions.md` | `85806a8e25a88a76bf4fceee7f090070eea69e179e3d4c9fb1fc85b84bfc6542` (12:29:27) puis `2c5ee45e12395df7d6816db18277fe966deaadc89b3aa446a5262fe02221081a` (12:33:18 et 12:39:39, application) puis `5f3ef18b7f6611b72f7e3eeb5d8efb835bb1363d8fe6a456e9e0b92f9caee946` (12:44:37) | R-2155 à R-2221 (l. 2113 à 2179) lues en entier |
| registre des autorisations | `registres/go.md` | `2c396b016d4ab86bd3f09cc7e21173f19d0c9765cc1a85b8efc08e59c2bc39f0` | l. 297-300 |
| registre des dépenses | `registres/depenses.md` | `5268f0f09943ab37d103534206121a30a28b76807b8eae6bac98c3e0d77b02a9` | l. 414 |
| état | `registres/etat.md` | `1ef56d65e747b59761833a17273a954d1398b5a505a7a076ec49c305cdadd548` | l. 179, 181, 190, 245 |
| scellements | `registres/scellements-v1.md` | `0651adcad120945265cca3b71cd91d84fe4d3518242a7482f1565c9fd8b27bfb` | lu en entier (trois lignes) |
| base (A) scellée | `prereg/T0.8-base-A-mots-et-cout-v1.md` | `72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d` | hachée, non lue |
| validité de l'adaptateur b3 | `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon3.md` | `defd8ef05038e703c24733f6a5f88a1153daf5f44d2b8cae14950a5643e875fd` | hachée, non lue |
| consigne d'audit des fuites b3 | `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon3.md` | `0d51099e5ef58829ce83731592eb8573aae8ce8848344488ffc672be45ac273e` | hachée, non lue |
| contre-lecture du code v65 | `docs/notes/organisme-boucle-reelle-v1/code-v65/contre-lecture-code-v65-v2.md` | `c4ddfc7ffd4b5cea1b0eb70e2a08ea551c8a8e8ef6f1a169ef8bebdab976ed03` | hachée, non lue |
| ordre de 7b, brouillon 4 | `docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon4.md` | `5f2167d705795db3d8e8850bbcf6cfc0c07750634d030b0ba0598379f4f8aef7` | haché, non lu |
| addendum du bras B (audit de fuite) | `docs/notes/g0-deux-semaines-v1/scellement-course-t06-v1/pieces-apres-couples/addendum-bras-b-v2-brouillon-v3-apres-couples-v1.md` | `1a372523290fdaf0a606db592295885f01ff9d6adc9b877fd72279fc6a44ccdf` | haché, non lu |
| réponses pour le registre des prédictions | `docs/notes/entretien-resultats-v1/reponses-mere-registre-predictions-v1.md` | `9639b715c8006a118ab8cdd3908edae62826a78bedf31d204c289118ca9aebd8` | égale au compagnon ; non lue |
| synthèse provisoire de niveau 3 | `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-provisoire1.md` (branche `origin/prep/etat-de-l-art-niveau3-v1`, tête `f0aaf0d1`) | `8adb561d52b728114cfd0c3065fe6c6230262f1befaeb2fd9d9824270ecdc3ad` | égale au compagnon (`git show`) ; non lue |
| son complément 1 | `…/etat-de-l-art-verifie-niveau3-v1-provisoire1-complement1.md` (même branche) | `a4176d46d5ec24406b38c82e8c653916ee0369a9b4a540f7da6fa4b108c0e33f` | égal au compagnon ; non lu |
| rapport C7 | `docs/etat-de-l-art/niveau3-v1/rapports/rapport-C7-contre-lecture-qu-chen-wang-dossier-c8-v1.md` (même branche) | `63d8373761d28c62b556f35839bd7b9f277decf4dc2d6d1ad44ad1f2266f8fb2` | égal au compagnon ; non lu |
| rapport du lot 5-A | `docs/sources/lecture-pdf-niveau3/rapport-lot5A-sequentiel-multi-agents-v1.md` (branche `origin/prep/etat-de-l-art-niveau3-pieces-v1`, tête `10016a61`) | `aef81e6e43b63f7aa0b2277308495dc9a7b0ccaea6e5c37a3d876fd5aac7b88f` | égal au compagnon ; l. 1-40 lues |
| rapport du lot 7-A | `docs/sources/lecture-pdf-niveau3/rapport-lot7A-sondes-agents-H1-H2-v1.md` (même branche) | `8a6dd0e0184a7afbf3cbc10e08eb9685817135ed7bcb9503ae095f9f169c3f1e` | égal au compagnon ; l. 1-20 lues, lignes sur 2610.17301 cherchées |
| rapport du lot 7-B | `docs/sources/lecture-pdf-niveau3/rapport-lot7B-collusion-papier-B-v1.md` (même branche) | `bf9b6af8f2d8a51ae406e8bcd2c53c3eff698826ecf916700ec7ae0dd206633c` | égal au compagnon ; l. 1-30 lues |

Aucun PDF ouvert. `main` : tête `17e6cc61` au début, `c9ab5b3f` puis `1cd3423b` pendant le travail (commits de la mère) ; aucun
des fichiers lus ou cités n'a changé d'empreinte entre ces têtes.

## 8. Ce qu'un vérificateur court doit relire

1. **Rejouer** l'annexe A sur la v3 et la contre-lecture (`... appliquer_socle_v4-b.py RACINE SORTIE 12:39:46`) : la sortie
   doit être égale à l'octet à la v4 (`b1c76e27…`) ; puis l'annexe B (neuf essais conformes).
2. **Les douze couples modifiés** (section 3) contre leurs sources : R-2190 (C14, C15) ; rapports des lots 7-A et 7-B (C14,
   C17) ; R-2210, R-2212 (C22) ; `registres/go.md` l. 297-300 et R-2215 (C24) ; R-2216 et `registres/scellements-v1.md` (C25
   à C29) ; R-2218 (C32 : je n'ai pas lu la pièce) ; R-2207, R-2210 (C42).
3. **Les treize ajouts** (section 4), surtout AJ08 (formule de la consigne), AJ09, AJ11 et AJ12 (phrases rendues fausses hors
   des couples), AJ13 (§ 7 point 9).
4. **Statuts relevés** : d'abord R-2220 (2), condition de configuration de GO-2026-11-10-10, qui complète C24 (section 2 bis) ;
   puis refaire le relevé si une ligne postérieure à R-2221 touche la dépense d'A1-v4, la page publique,
   P3-bis, T0.7, T0.8, les concepts, la consigne d'audit, la validité de l'adaptateur, le code de l'organisme ou la lecture (c).
5. **Zones non remises à jour** (§ 7 point 9) : la colonne « en cours » de la rangée du 10 au § 4 ; ce qui y est dit des
   ordres de l'étape A et de la variante B.
6. **Aucun taux** : la garde finale passe sur la v4 ; à recontrôler à l'œil sur le § 1.3 et le § 6 point 15.

## 9. Gestes à déclarer, refus, interdits

- **Aucun refus** de contrôle de permissions ni de classifieur.
- Aucun appel de modèle ni d'interface externe, aucune instance, aucune dépense ; aucune écriture git (ni commit, ni
  `checkout`, ni `fetch`) ; aucune valeur de clé lue.
- Autres commits lus par `git show <réf>:<chemin>` seulement, sur les deux branches de l'état de l'art (ni branche du bras, ni
  branche de la session-dépôt, ni branche de quarantaine) ; deux listes de dossiers par `git show <réf>:<dossier>/`
  (`docs/etat-de-l-art/` et `docs/sources/lecture-pdf-niveau3/` de ces branches) ; référence des branches résolue par
  `git rev-parse --verify` sur leur nom, sans lister les branches.
- Recherches : `grep` sur des fichiers nommés ; un `git grep -l` limité aux compagnons `*.sha256` de `main`, avec les
  exclusions de la règle 9 (aucune occurrence) ; aucune recherche récursive ; `verifier-arbre` non lancé.
- **Geste à déclarer** : `ls -la brouillons/entretien-taif-v3/` a affiché les noms du dossier, dont
  `consigne-v19-pince-bras-attaque-sabotage-diffus-v1.md` : nom vu, fichier **ni ouvert, ni haché**. `ls brouillons/` a affiché
  les noms du dossier, sans ouverture.
- Rien de 7a, de la mesure unanime, du mode tenu à l'écart ni de l'étiqueteur ; aucune sortie scellée non lue ouverte ; les
  pièces citées « non lues » ci-dessus n'ont été que hachées.
- Aucun fichier de T0.7 ni de P3-bis ouvert (noms de dossier seulement) ; leurs états viennent du registre et des empreintes.

## Annexe A — programme d'application, version b (`appliquer_socle_v4-b.py`, `83c7045f…`)

Reproduit la v4 scellée à l'octet ; ne diffère de `appliquer_socle_v4.py` (`8fcea154…`, qui l'a écrite) que par la garde finale.

~~~python
#!/usr/bin/env python3
"""Socle de preuves de l'entretien, v4 : application par programme.

Usage : python appliquer_socle_v4.py RACINE_DEPOT SORTIE HEURE_FIN [--garde-seule FICHIER]

1. Vérifie les empreintes de la v3 et de sa contre-lecture cl1 (arrêt sinon).
2. Extrait de cl1, par motif, les 50 couples C01 à C50 (arrêt si l'ensemble n'est pas exactement C01..C50).
3. Remplace le texte nouveau des couples modifiés au relevé des états (MODIFS, raison au journal).
4. Ajoute les ajouts AJ01..AJ13 (texte ancien de la v3 -> texte nouveau).
5. Exige que chaque texte ancien (couples et ajouts) apparaisse UNE fois et une seule dans la v3,
   blancs et retours à la ligne normalisés ; refuse tout chevauchement ; arrêt (code 2) sinon.
6. Applique, vérifie que chaque texte nouveau est présent, passe la garde finale, écrit SORTIE.
Aucun appel réseau, aucune écriture hors de SORTIE.
"""
import hashlib
import pathlib
import re
import sys

V3 = "brouillons/entretien-taif-v3/socle-preuves-entretien-v3.md"
CL1 = "prereg/contre-lectures/socle-preuves-entretien-v3-cl1.md"
ATTENDU = {
    V3: "b9377f1dfc72082a1c95224b7a3746cce5b575ec1a2e6dae882394c6b3f36265",
    CL1: "3a1df7959475b440e61193500d44f58b72dd433e928dbba338452875cb45079b",
}

# Garde finale : aucun taux de calibration (R-2185, R-2195) ; phrase du bras retirée (consigne v4).
# Les taux refusés ne sont écrits nulle part en clair : seules leurs empreintes sha256 figurent ici,
# comparées à celles des chaînes candidates (nombre décimal à trois chiffres, fraction, « n sur m », « n confirmées »).
CANDIDATS = re.compile(r"\d+,\d{3}|\d+/\d+|\d+ sur \d+|\d+ confirmées")
EMPREINTES_INTERDITES = {
    "4841d6dbca8b403cdeae35f7c43347804a2eee64a3c20e9fb4db1d599cacd6ed",
    "51de0bb1c183cef7e12086fcc16d6e659facea67354124a1dab53505a6aff80d",
    "f00e22c1d6645d8942eaa15214f836141c652630ff67f0edd89212efc32200e6",
    "e55d35f91c407a1bdb3cd2ba6e7e3b2c83cb2871780f026e1a1a71416ad07dc6",
    "5f49e56c10664375de0fa2ead2b611d34fb38a12169cb0184f21c1f4299852e6",
    "9b63202f71ecf1aa9426cc5bba5747d5bb5b255634ac6c2c5d9ebdb19d7ebc00",
    "a197fb81fa751cac6eaa54bd1c0a6a132d59955ec6111b255b6d1e7b50d57875",
    "ea5cf5832444243d13f38b5bd563babb18490bc045f773d4742499170e8c10cc",
    "80f897292f64a59a9e4d90d7de056e8fcd09049f012cc750a4b94e15102d9716",
}
PHRASES_INTERDITES = ["rien n'a encore tourné"]


def arret(msg):
    print("ARRÊT : " + msg, file=sys.stderr)
    sys.exit(2)


def garde(texte):
    """Rend la liste des empreintes (douze premiers caractères) des chaînes refusées trouvées."""
    trouves = []
    for m in CANDIDATS.finditer(texte):
        h = hashlib.sha256(m.group(0).encode("utf-8")).hexdigest()
        if h in EMPREINTES_INTERDITES:
            trouves.append("taux " + h[:12])
    for p in PHRASES_INTERDITES:
        if p in texte:
            trouves.append("phrase du bras")
    return trouves


def motif(ancien):
    jetons = ancien.split()
    if not jetons:
        arret("texte ancien vide")
    return re.compile(r"\s+".join(re.escape(j) for j in jetons))


# --------------------------------------------------------------------------------------------
# Couples modifiés au relevé des états (texte nouveau de la v4 à la place de celui de cl1).
# --------------------------------------------------------------------------------------------
MODIFS = {
    "C14": "quatre annonces seulement (p. 3, 18, 19, 26) : **bascule du programme non déclenchée par HELIOS v5** ; **à réexaminer par Lazar pour le papier B** depuis deux prépublications de novembre 2026 sur états internes d'agents (2611.02153 : représentations internes de copies d'un même modèle ; 2611.10620 : scores de sondes par agent) ; aucune ne vient des équipes que nomme le déclencheur, aucune ne publie de test séquentiel toujours valide sur sondes (R-2190 ; complément 1 de la synthèse provisoire de niveau 3, `a4176d46…`, verdicts repris de messages ; contrôlé sur le rapport du lot 7-B, `docs/sources/lecture-pdf-niveau3/rapport-lot7B-collusion-papier-B-v1.md`, branche `prep/etat-de-l-art-niveau3-pieces-v1`, `bf9b6af8…`, § 0.1 points 1 et 2, § 0.2 : « Déclencheur de bascule à examiner par Lazar » ; non recontrôlé sur PDF pour ce socle) |",
    "C15": "**HC2 occupée en partie** (MIRAGE, 2606.10304) ; H2 une fois de plus, en boîte noire (2606.20746, R-2181) ; selon les rendus suivants (R-2180, R-2181, R-2188, R-2190 ; synthèse provisoire de niveau 3 `8adb561d…` et son complément `a4176d46…`, **non finale**), sont aussi occupés en partie HC1, H5, H7, HC3 (rapport C5), H9 sur son cœur, la statistique de population du papier B, HC5 et HC6, et la prémisse de HC4 est entamée ; R-2190 range aussi parmi les nœuds de revendication H8, H6 (2605.26047) et la prédiction 1 de HC1, contredite (2606.05384) — nœuds de Lazar, à porter d'après la synthèse finale ; L et T occupés en partie",
    "C17": "sont **[NON OPPOSABLE]** ; « The Agent Knew » (2610.17301), lue depuis sur PDF par le lot 7-A, n'occupe ni H1 ni H2 et porte un contre-indice (un classifieur de mots y égale la sonde) (R-2188 ; rapport `docs/sources/lecture-pdf-niveau3/rapport-lot7A-sondes-agents-H1-H2-v1.md`, branche `prep/etat-de-l-art-niveau3-pieces-v1`, `8a6dd0e0…`, « En tête », points 1 et 4).",
    "C22": "phrases des concepts non scellées (deux concepts arrêtés après un second échec, R-2155 ; clé permise et lot neuf sous la consigne v3, R-2158, R-2174) ; consigne de l'audit des fuites de T0.7 (brouillon 3, `0d51099e…`, R-2212) et texte de validité de l'adaptateur (brouillon 3, `defd8ef0…`, R-2210) rendus, non scellés",
    "C24": "**autorisations inscrites le 10 novembre** (`registres/go.md`, `2c396b01…`) : GO-2026-11-10-07 (contrôle de l'artefact d'adaptateur, 30 ; lecture large accordée par Lazar, R-2207), -08 (saboteur à budget, 60, R-2175), -09 (autonomie de calcul jusqu'au 27, enveloppe 500, R-2182), -10 (120 jusqu'au 30 novembre : organisme 45, sous les conditions de GO-2026-11-08-02 — son code v65, contre-lu « utilisable pour la course après corrections », est repris en v66, en cours, R-2215 —, témoin de Bailey 75 ; mot direct de Lazar, R-2206) ; **après le 8 novembre, non sommé** :",
    "C25": "**T0.8** : brouillon 1 rendu et contre-lu, « non scellable en l'état », trois bloquants (R-2165, R-2186) ; sa base (A) « mots et coût » est **scellée à part le 10 novembre** (ligne `SCELLEMENT-T08-BASE-A` à 12:21:55, avant toute création de 7b ; `prereg/T0.8-base-A-mots-et-cout-v1.md`, `72b067d5…` ; R-2216), sur le mot de Lazar (R-2175), après contre-lecture et vérification courte (douze traits accordés, R-2211) ; plafond proposé de 120 au-dessus du seuil de 60 de GO-2026-11-10-09 : retour à Lazar avant toute course (R-2186) ;",
    "C26": "T0.8 scellé (visé vers le 18-19, R-2131 ; brouillon 1 « non scellable en l'état », R-2186 ; base (A) déjà scellée à part le 10, R-2216)",
    "C27": "T0.8 est désormais sur un chemin (brouillon 1 contre-lu, « non scellable en l'état », R-2186 ; base (A) scellée à part le 10 novembre, avant 7b, R-2216), sans date écrite pour sa lecture.",
    "C28": "le critère 4 (base boîte noire) a un premier brouillon, contre-lu et jugé « non scellable en l'état » (R-2186), dont la base « mots et coût » est scellée à part, avant la course de confirmation (R-2175, R-2216) ;",
    "C29": "4. **T0.8 non scellé** (brouillon 1 contre-lu, « non scellable en l'état », trois bloquants, R-2186 ; base (A) « mots et coût » scellée à part le 10 novembre, avant 7b, R-2175, R-2216) :",
    "C32": "prédictions : **[K19] nombres bruts, sans taux** (choix (c) de Lazar, R-2195, lecture à lui faire confirmer : 33 confirmées, 7 réfutées, 6 non concluantes ; pièce `bd994163…` de la session-dépôt, sur sa branche, absente de `main` au relevé de la v4 : à vérifier avant tout usage) ; antériorité du scellement des séries de prédictions : selon les réponses de la mère pour le registre des prédictions v2 (R-2218 ; `docs/notes/entretien-resultats-v1/reponses-mere-registre-predictions-v1.md`, `9639b715…`, non relu pour ce socle), aucune pièce unique ne l'atteste série par série ; établie pour la plupart des séries, par le seul registre pour deux (rejeu R1-R2, relance v4), non établie pour l'heure de scellement de trois textes d'analyse du rejeu R1-R2 sur `main` ni pour les deux premières courses d'A1-v3 ; aucun taux cité (",
    "C42": "une règle qui ne juge les sondes de cet organisme qu'aux doses où un lecteur des seuls mots et du coût échoue. **Réserve à dire avec tout résultat de sonde sur cet organisme** : le texte scellé de T0.6 n'a aucun témoin distillé honnête (son seul adaptateur témoin est distillé du témoin instruit, à la dose 1) ; une sonde au-dessus de son plancher n'y sépare donc pas, à elle seule, le sabotage de l'effet de l'adaptateur (R-2168) ; un contrôle à part est autorisé (GO-2026-11-10-07, lecture large : R-2175, R-2207) ; son texte (validité de l'adaptateur, brouillon 3, `defd8ef0…`) n'est pas scellé : il attend une contre-lecture différentielle sur T0.7 scellé (R-2210).",
}

ENTETE_V4 = """# Socle de preuves pour l'entretien avec le Transformative AI Fund — v4

- **Rédacteur de la v4** : sous-agent neuf (rédacteur) de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, modèle déclaré
  par l'environnement Claude Opus 5.5 (`claude-opus-5-5`). Je n'ai écrit ni les versions 1 à 3 de ce socle, ni leurs journaux,
  ni leurs contre-lectures, ni aucune pièce citée. Début de la rédaction (`date -u`) : **2026-11-10 12:28:59** ; fin :
  **2026-11-10 {FIN}** (relevée par `date -u` juste avant l'application finale et le scellement).
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-socle-preuves-v4-v1.md`
  (`f25b2ecf…`, égale à son compagnon) ; interdits communs v2 (`1ee3b370…`) recopiés et tenus, règle 9 comprise ; cloison du
  bras ; aucun taux de calibration.
- **Ce que fait la v4** : elle reprend la v3 `brouillons/entretien-taif-v3/socle-preuves-entretien-v3.md` (`b9377f1d…`, gardée
  intacte, règle 12) et y applique **par programme** les 50 couples C01 à C50 de sa contre-lecture
  `prereg/contre-lectures/socle-preuves-entretien-v3-cl1.md` (`3a1df795…`, Claude Fable 5.2 : « utilisable pour l'entretien
  après corrections ») : chaque texte ancien est trouvé une fois et une seule dans la v3 (blancs et retours à la ligne
  normalisés), arrêt sinon. **{N_TELS} couples appliqués tels quels, {N_MODIF} avec un texte nouveau modifié** au relevé des
  états (registre des décisions lu jusqu'à sa dernière ligne, R-2219 ; registres des autorisations et des dépenses, état vivant,
  aux empreintes du journal) ou pour lever une mention « à citer » ou « à contrôler » du contre-lecteur ; plus **{N_AJ} ajouts**
  (AJ01 à AJ{N_AJ}) : les deux points ouverts nommés par la consigne (état du bras non vérifiable par la mère ; synthèse de
  niveau 3 provisoire, dite là où le niveau 3 est cité), deux mineurs du contre-lecteur sans couple (session de la v4 ; chemin
  de l'addendum du bras B), et les phrases que la base (A) scellée, la page publiée et l'ordre de 7b rendu rendaient fausses
  hors des couples. Texte ancien, texte nouveau et raison de chaque écart : journal
  `brouillons/entretien-taif-v3/socle-preuves-entretien-v4-journal.md`, qui recopie le programme d'application.
- **Ce que la v4 ne fait pas** : aucun PDF relu ; aucune correction de fond hors des couples et des ajouts déclarés ; ce
  qu'aucun couple ni ajout ne touche reste à l'état de la v3 (littérature, 11:12) ou de la v2 (calendrier et procédure,
  10:34) : section 7, point 9.
- **Statut** : brouillon scellé, **non contre-lu** (vaut pour la v4).
- **Session** : la v4 est rendue sous la session mère d'après la reprise du 10 novembre (R-2191, R-2201) ; les en-têtes
  conservés ci-dessous nomment la session mère d'avant la reprise, exacts pour leur version.

**En-tête de la v3, conservé** (les couples C37 et C50 y sont appliqués) :"""

POINT_9 = """(dont le calendrier resserré de R-2177) ne sont pas intégrés.
9. **[v4]** Le point 8 vaut pour la v3. La v4 applique les 50 couples de la contre-lecture de la v3 et relève les états
   qu'ils touchent contre `registres/decisions.md` jusqu'à R-2219 et `registres/go.md` (empreintes et heures au journal).
   **Restent à l'état de la v2 (10:34)**, faute de couple : la colonne « en cours » de la rangée du 10 au § 4 (T0.7
   brouillon 21, T0.8 brouillon 1 et P3-bis brouillon 11 y sont « en cours » ; rendus depuis : R-2165 à R-2167) et ce qu'elle
   dit des ordres de l'étape A et de la variante B ; restent à l'état de la v3 (11:12) les passages de littérature qu'aucun
   couple ne touche. La synthèse de niveau 3 est **provisoire** (`8adb561d…`, complément `a4176d46…`) : § 1.1 bis, écart 9
   et Q5 sont à réaligner sur la synthèse finale (R-2190). L'état du bras d'attaque n'est pas vérifiable par la mère
   (cloison). La lecture (c) de R-2195 (nombres bruts sans taux) reste à faire confirmer par Lazar. Cette v4 n'est pas
   contre-lue : elle ne fait foi qu'après sa vérification et le mot de Lazar."""

# (identifiant, lieu, texte ancien de la v3, texte nouveau)
AJOUTS = [
    ("AJ01", "en-tête", "# Socle de preuves pour l'entretien avec le Transformative AI Fund — v3", None),
    ("AJ02", "§ 0, ligne 4",
     "**[K0, v3]** Sur la littérature, lue sur PDF au niveau 3 :",
     "**[K0, v3]** Sur la littérature, lue sur PDF au niveau 3 (rapports de lots ; leur synthèse est **provisoire**, `8adb561d…`, R-2190) :"),
    ("AJ03", "§ 1.1, « état »",
     "le niveau 3 a rendu ses lots le 10 novembre, R-2177, sans clore le critère)",
     "le niveau 3 a rendu ses lots le 10 novembre, R-2177, R-2190, sans clore le critère ; sa synthèse est **provisoire**, `8adb561d…`)"),
    ("AJ04", "§ 1.1 bis, chapeau",
     "Lus sur PDF par les rapports C1, B3 et C5 (C3 et le rapport du lot 1 sur HC2 pour le papier C) ;",
     "Lus sur PDF par les rapports C1, B3 et C5 (C3 et le rapport du lot 1 sur HC2 pour le papier C ; les rapports des lots 5-A et 7-B pour ce que R-2181 et R-2190 ajoutent) ; la synthèse de niveau 3 qui les rassemble est **provisoire** (`8adb561d…`, complément `a4176d46…`) : table à réaligner sur la synthèse finale ;"),
    ("AJ05", "§ 5, Q5, « Réponse », [K18]",
     "**[K18]** Le niveau 3 (lu sur PDF) ne trouve aucun énoncé du texte envoyé occupé en entier, mais des occupations partielles à dire nous-mêmes :",
     "**[K18]** Le niveau 3 (lu sur PDF ; synthèse **provisoire**, `8adb561d…`, à réaligner sur la synthèse finale, R-2190) ne trouve aucun énoncé du texte envoyé occupé en entier, mais des occupations partielles à dire nous-mêmes (liste relevée au registre : section 1.6, écart 9), dont :"),
    ("AJ06", "§ 2.2, « Préalables », (4)",
     "(R-2092 ; `1a372523…`)",
     "(R-2092 ; `docs/notes/g0-deux-semaines-v1/scellement-course-t06-v1/pieces-apres-couples/addendum-bras-b-v2-brouillon-v3-apres-couples-v1.md`, `1a372523…`)"),
    ("AJ07", "§ 2.2, « Préalables », (2)",
     "brouillon 4 lancé (R-2143)",
     "brouillon 4 rendu (R-2160 : `docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon4.md`, `5f2167d7…`), non scellé, contre-lecture de son différentiel à faire avant le scellement"),
    ("AJ08", "§ 2.5, première puce",
     "- **Phrase sûre pour l'entretien** (précision de la mère après R-2145) : « **monté ; rien n'a encore tourné** ».",
     "- **État du bras** : **état du bras non vérifiable par la mère (cloison)** ; ce qui a tourné ou non, et la phrase à dire au jury, reviennent à Lazar à la date de l'entretien (contre-lecture de la v3, `3a1df795…`, point ouvert 1 ; consigne de la v4)."),
    ("AJ09", "§ 3, rangée « texte scellé d'A1-v4 », colonne « qui »",
     "rédacteur neuf, contre-lecture, poussée par la mère (R-2131) ; **Lazar** pour les citations",
     "publiée par la mère sur le mot de Lazar (R-2162) ; mise à jour : **Lazar** (nouveau « go publication », R-2177)"),
    ("AJ10", "§ 1.4, « pièces »",
     "`registres/depenses.md` (`e7b83d37…`) ; `registres/go.md` (`e682abb0…`)",
     "`registres/depenses.md` (`e7b83d37…` à la v2, `5268f0f0…` au relevé de la v4) ; `registres/go.md` (`e682abb0…` à la v2, `2c396b01…` au relevé de la v4)"),
    ("AJ11", "§ 5, Q4, « Réponse »",
     "et la règle « mots et coût », qui attend le texte de T0.8 (R-2070) ;",
     "et la règle « mots et coût », scellée à part le 10 novembre (base (A) de T0.8, R-2216 ; elle attendait le texte de T0.8, R-2070) ;"),
    ("AJ12", "§ 6, point 4",
     "tables B et C de 7b ; règle « mots et coût » ; aucune date écrite pour sa lecture sur 7b.",
     "tables B et C de 7b ; aucune date écrite pour sa lecture sur 7b (la règle « mots et coût » n'en dépend plus : base (A) scellée à part, R-2216)."),
    ("AJ13", "§ 7, point 9 (neuf)",
     "(dont le calendrier resserré de R-2177) ne sont pas intégrés.",
     POINT_9),
]


def main():
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == "--garde-seule":
        trouve = garde(pathlib.Path(args[1]).read_text(encoding="utf-8"))
        print("garde : " + (f"REFUS ({len(trouve)}) " + ", ".join(sorted(set(trouve))) if trouve else "SAIN"))
        sys.exit(1 if trouve else 0)
    if len(args) != 3:
        arret("usage : RACINE_DEPOT SORTIE HEURE_FIN")
    racine, sortie, fin = pathlib.Path(args[0]), pathlib.Path(args[1]), args[2]
    if not re.fullmatch(r"\d\d:\d\d:\d\d", fin):
        arret("heure de fin au format HH:MM:SS")

    textes = {}
    for chemin, attendu in ATTENDU.items():
        brut = (racine / chemin).read_bytes()
        h = hashlib.sha256(brut).hexdigest()
        if h != attendu:
            arret(f"empreinte de {chemin} : {h} au lieu de {attendu}")
        textes[chemin] = brut.decode("utf-8")
    v3, cl1 = textes[V3], textes[CL1]

    paires = re.findall(
        r"\*\*(C\d{2})\*\* — ([^\n]*)\n\n~~~text\nANCIEN : (.*?)\n~~~\n\n~~~text\nNOUVEAU : (.*?)\n~~~",
        cl1, flags=re.S)
    ids = [p[0] for p in paires]
    if ids != [f"C{i:02d}" for i in range(1, 51)]:
        arret(f"couples extraits de cl1 : {ids}")
    if set(MODIFS) - set(ids):
        arret("modification d'un couple inconnu")

    operations = []  # (id, lieu, ancien, nouveau, origine)
    for cid, lieu, ancien, nouveau_cl1 in paires:
        if cid in MODIFS:
            operations.append((cid, lieu, ancien, MODIFS[cid], "modifié"))
        else:
            operations.append((cid, lieu, ancien, nouveau_cl1, "tel quel"))
    n_tels = sum(1 for o in operations if o[4] == "tel quel")
    n_modif = len(operations) - n_tels
    n_aj = len(AJOUTS)
    entete = (ENTETE_V4.replace("{FIN}", fin).replace("{N_TELS}", str(n_tels))
              .replace("{N_MODIF}", str(n_modif)).replace("{N_AJ}", f"{n_aj:02d}"))
    for aid, lieu, ancien, nouveau in AJOUTS:
        operations.append((aid, lieu, ancien, entete if nouveau is None else nouveau, "ajout"))

    spans = []
    for oid, lieu, ancien, nouveau, origine in operations:
        trouves = list(motif(ancien).finditer(v3))
        if len(trouves) != 1:
            arret(f"{oid} ({lieu}) : texte ancien trouvé {len(trouves)} fois dans la v3")
        m = trouves[0]
        ligne = v3.count("\n", 0, m.start()) + 1
        spans.append((m.start(), m.end(), oid, nouveau, ligne, origine, lieu))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            arret(f"chevauchement entre {a[2]} et {b[2]}")

    morceaux, pos = [], 0
    for debut, fin_s, oid, nouveau, ligne, origine, lieu in spans:
        morceaux.append(v3[pos:debut])
        morceaux.append(nouveau)
        pos = fin_s
    morceaux.append(v3[pos:])
    v4 = "".join(morceaux)

    for debut, fin_s, oid, nouveau, ligne, origine, lieu in spans:
        if nouveau not in v4:
            arret(f"{oid} : texte nouveau absent de la sortie")
    trouve = garde(v4)
    if trouve:
        arret(f"garde finale : {trouve}")

    sortie.write_text(v4, encoding="utf-8")
    print(f"v3 {len(v3.splitlines())} lignes -> v4 {len(v4.splitlines())} lignes ; "
          f"couples tels quels {n_tels}, modifiés {n_modif}, ajouts {n_aj}")
    for debut, fin_s, oid, nouveau, ligne, origine, lieu in sorted(spans, key=lambda s: s[2]):
        print(f"{oid}\tl. {ligne} de la v3\t{origine}\t{lieu}")
    print("sha256 sortie " + hashlib.sha256(v4.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
~~~

## Annexe B — essais des gardes (`essais_gardes-b.py`, `3dae137a…`)

Usage : `.venv/bin/python -I essais_gardes-b.py DOSSIER_DES_OUTILS RACINE_DEPOT` (attend `essai-v4.md`, l'essai à blanc, dans le dossier des outils).

~~~python
import hashlib, pathlib, shutil, subprocess, sys, importlib.util
S = pathlib.Path(sys.argv[1]); R = pathlib.Path(sys.argv[2]); PY = sys.executable
spec = importlib.util.spec_from_file_location("app", S / "appliquer_socle_v4-b.py"); app = importlib.util.module_from_spec(spec); spec.loader.exec_module(app)
def run(*a):
    p = subprocess.run([PY, "-I", str(S / "appliquer_socle_v4-b.py"), *map(str, a)], capture_output=True, text=True)
    return p.returncode, (p.stderr.strip() or p.stdout.strip().splitlines()[0])
res = []
# 1-2 garde finale : artefact (v3, contient la phrase du bras) et cas sain (sortie d'essai)
res.append(("garde sur la v3 (artefact)", run("--garde-seule", R / app.V3), 1))
res.append(("garde sur l'essai v4 (sain)", run("--garde-seule", S / "essai-v4.md"), 0))
res.append(("garde sur la contre-lecture cl1 (artefact : elle cite des taux)", run("--garde-seule", R / app.CL1), 1))
V4 = R / "brouillons/entretien-taif-v3/socle-preuves-entretien-v4.md"
res.append(("garde sur la v4 scellée (sain)", run("--garde-seule", V4), 0))
code, msg = run(R, S / "repro-v4.md", "12:39:46")
egal = (S / "repro-v4.md").read_bytes() == V4.read_bytes()
res.append(("reproduction de la v4 scellée à l'octet", (0 if (code == 0 and egal) else 1, "égale" if egal else "DIFFÉRENTE"), 0))
# 3 empreinte altérée : faux dépôt avec un octet de la v3 changé
F = S / "faux-depot"; shutil.rmtree(F, ignore_errors=True)
for c in (app.V3, app.CL1):
    (F / c).parent.mkdir(parents=True, exist_ok=True); shutil.copy(R / c, F / c)
t = (F / app.V3).read_text(encoding="utf-8"); (F / app.V3).write_text(t.replace("Socle de preuves", "Socle  de preuves", 1), encoding="utf-8")
res.append(("empreinte altérée (artefact)", run(F, S / "x.md", "12:00:00"), 2))
# 4-5 unicité : en mémoire, sur la logique de main(), avec ATTENDU recalculé pour le faux dépôt
def essai_unicite(transfo):
    v3 = (R / app.V3).read_text(encoding="utf-8"); (F / app.V3).write_text(transfo(v3), encoding="utf-8")
    app.ATTENDU = {app.V3: hashlib.sha256((F / app.V3).read_bytes()).hexdigest(), app.CL1: hashlib.sha256((F / app.CL1).read_bytes()).hexdigest()}
    sys.argv = ["x", str(F), str(S / "x.md"), "12:00:00"]
    try:
        app.main(); return 0, "aucun arrêt"
    except SystemExit as e:
        return e.code, "arrêt"
anc = "ni table régénérée depuis le 8 novembre, une dépense connue hors registre."  # C03
res.append(("ancien en double (artefact)", essai_unicite(lambda v: v + "\n" + anc + "\n"), 2))
res.append(("ancien absent (artefact)", essai_unicite(lambda v: v.replace(anc, anc.replace("hors registre", "hors du registre"))), 2))
res.append(("faux dépôt identique à la v3 (sain)", essai_unicite(lambda v: v), 0))
ok = True
for nom, (code, msg), attendu in res:
    bon = code == attendu; ok &= bon
    print(f"{'OK ' if bon else 'ÉCHEC'} {nom} : code {code} (attendu {attendu}) — {msg[:110]}")
shutil.rmtree(F, ignore_errors=True); (S / "x.md").unlink(missing_ok=True); (S / "repro-v4.md").unlink(missing_ok=True)
print("TOUS CONFORMES" if ok else "NON CONFORME"); sys.exit(0 if ok else 1)
~~~

Fin du journal et de la rédaction (`date -u`, juste avant le scellement) : **2026-11-10 12:45:43**.
