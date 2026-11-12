# Journal — socle de preuves pour l'entretien avec le Transformative AI Fund — v2

- Rédacteur : sous-agent neuf de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5 (`claude-opus-5-5`) ;
  je n'ai écrit ni la v1 du socle, ni sa contre-lecture, ni le programme d'entretien.
- Heures (`date -u`) : interdits vérifiés 2026-11-10 10:04:05 ; registres hachés 10:04:50, 10:10:08, 10:17:02, 10:19:27,
  10:29:29, 10:33:25 ; début de la rédaction 10:19:44 ; fin du journal : **2026-11-10 10:34:28** (relevée par `date -u` dans la
  commande qui l'écrit, juste avant le scellement des deux fichiers).
- Sorties : `brouillons/entretien-taif-v3/socle-preuves-entretien-v2.md` et ce journal, scellés par
  `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller` (compagnons `.sha256`). La v1, son journal et sa
  contre-lecture restent intacts (règle 12). Aucune autre écriture.

## 1. Constat → traitement (contre-lecture `48c7fcc2…`, 27 constats)

| n° | gravité | traitement dans la v2 | lieu |
|---|---|---|---|
| 1 | bloquant | **appliqué selon R-2130** : le bloquant tombe (entretien visé le 27, à confirmer par Lazar avec le fonds ; le rendez-vous du 20 le précède) ; calendrier réécrit jusqu'au 27 ; échéances du 23 dites « avant l'entretien » ; gestes de Lazar replacés du 24 au 26 ; plus rien à trancher sur la date du rendez-vous avant son défaut du 11 vers 16:03 | § 0 l. 1 ; § 2.1 « Date réaliste » ; § 4 ; § 6 manque 9 |
| 2 | bloquant | **appliqué** : deux voies d'ouverture de P3-bis ; voie normale (lignes `SCORES-T07` et `SONDES-T07`, ouverture pleine, ni rendez-vous ni mot de Lazar, « le rendez-vous tombe ») d'après le brouillon 10 l. 904-909 et 949-950, avec les trois écrits exigés avant toute ouverture (l. 827-844) ; voie du rendez-vous, branches 1 et 2 (l. 910-948 ; N-066 points 1 à 3) ; « ouvrir pleinement » seule voie seulement sans T0.7 scellé avec la garde. Que l'étape A inscrive ces deux lignes : R-2133 (l. 2091), GO-2026-11-10-04 (« scellement et poussée »), N-066 point 2 ; **le brouillon 20 de T0.7 (l. 245) n'a pas été relu** (aucun fichier de T0.7 ouvert) | § 0 l. 1 ; § 2.1 ; § 4 du 17 au 20 |
| 3 | à corriger | **appliqué** : borne du 31 janvier 2027 confirmée (R-750 l. 978, R-765 l. 993) ; ce qui manque est la clause (onze choix ouverts, N-027 bis absente de `docs/decisions/`, vérifié par `ls`) ; phrases du v18 à reprendre (l. 319, 466, 549-550) | § 1.5 ; Q4 ; § 5 en-tête ; manque 8 |
| 4 | à corriger | **appliqué** : « about $20 » sans pièce (v18 l. 142-143 — la contre-lecture écrit l. 144 ; R-1876) ; pièce voisine `registres/depenses.md` l. 43 | § 1.4 ; Q2 |
| 5 | à corriger | **appliqué** : aucun dépassement établi ; deux dépassements apparents expliqués (`registres/go.md` l. 53, 54, 161, 163 ; `registres/depenses.md` l. 106, 263 ; table l. 53, 96) ; « *one line above its cap* » à retirer | § 0 l. 2 ; § 1.4 ; Q2 |
| 6 | à corriger | **appliqué** : énoncé (plafond de Lazar ou fixé par la session) ; exemples l. 66, 163, 285, **plus l. 289** (GO-2026-11-09-04) ; rangée « (sans GO cité) » 54,08 sur 12 lignes, décrite (dix appels de modèles du 26 octobre, un du 31, une charge de P3 du 20) ; incident du 23 octobre de montant inconnu (l. 92) | § 1.4 ; Q2 |
| 7 | à corriger | **appliqué** : « ni total ni plancher au dollar près » ; double compte de 1,06 recompté (l. 159, 160, 166, 167, toutes sommées : table l. 47 et 53, `sources-v3.json`) ; « plancher » : 0 occurrence dans la table ; 624,09 sur 125 lignes (table l. 143). La « borne basse vraisemblablement au-dessus de 850 » de la v1 est retirée | § 0 l. 2 ; § 1.4 ; Q2 |
| 8 | à corriger | **appliqué** : N-065 point 1 (second terrain du papier C) ; quatre citations obligatoires (N-064 point 4, N-065 point 4) ; limite de N-064 point 3 (forme seulement) | § 1.6 écart 13 ; § 2.4 ; Q2 |
| 9 | à corriger | **appliqué**, mis à jour par R-2131 (le critère 4 a un brouillon 1, scellement visé vers le 18-19) : T0.6 l. 517-518 ; R-2070 ; `registres/etat.md` l. 173 et 184 | Q4 |
| 10 | à corriger | **appliqué** : trois règles séparées (N-063 v2 point 1 ; T0.6 l. 583 ; N-062 l. 30, N-056 points 1 et 4, R-600 l. 826) | § 1.2 |
| 11 | à corriger | **appliqué** : écarts 2 (règle de décision de G1 : N-055 l. 29, N-056 points 1, 2, 4, R-600, N-054 point 2, R-1876) et 4 (chaque cycle, une ligne de budget) ; liste complète regroupée en § 1.6 (harnais « *partial* », bruit d'activations, Qwen, politiques d'attaque, « *I take every decision* », « *31 of 31* », plus G1 « fin du mois 4 » contre « fin M2 », contre-lecture v17 constat 12 et R-2132). **Non appliqué : « « 602 » sans pièce »** — la pièce existe : R-098 (`registres/decisions.md` l. 235, 7 octobre : « 602 tests réussis ») et R-1869 (l. 1827 : « les 602 essais ont une pièce, R-098 ») ; aucun écart à dire | § 1.6 ; Q4 |
| 12 | à corriger | **appliqué** : synthèse de niveau 2 l. 30, 44, 56 et R-622 ajoutées ; critère 8 non clos (`registres/etat.md` l. 173) ; écart « *fully occupied* » réécrit ; contre-résultat de 2512.07810 (p. 17, page non revérifiée) dans Q1 et Q5 | § 1.1 ; § 1.6 écart 9 ; Q1 ; Q5 |
| 13 | à corriger | **appliqué** : règle 2 ; N-052 dit à sa portée exacte (boucle extérieure de l'organisme), non comme règle générale ; « sauf la simulation » ; audit DT-4 : un audit et son complément, même auditeur, structurels, réserves. **Détail divergent** : la contre-lecture écrit « révisions 5 à 10 » ; R-2082 (l. 2040) écrit « r4 à r10 » : la v2 suit le registre | § 1.3 ; Q3 |
| 14 | à corriger | **appliqué** : réserves 1, 2, 4, 7, 9 ; « levée » non écrite ; P7 et P9 ; McNemar p = 0,453 ; texte scellé l. 201 et 193 (compagnons A1 et A1-v3 écrits) ; puissance donnée comme lecture de l'intervalle [CE RÉDACTEUR] ; « phrase possible » réécrite (« moins souvent que prédit ») | § 2.4 |
| 15 | à corriger | **appliqué et mis à jour** : code de P3-bis, module et ordre de l'étape A, ordre de 7b en « en cours » ; DF-01 corrigé depuis (R-2134 : commit proposé `8ae9fc44`, contre-lecture courte lancée) | § 4, ligne du 10 |
| 16 | à corriger | **appliqué** | § 4, dernier paragraphe ; § 0 l. 3 |
| 17 | à corriger | **appliqué, avec une correction** : préalables de la création de 7b (ordre l. 5, 45, 46 ; contre-lecture de l'ordre R-2143). **Corrigé** : l'addendum v3 du bras B **est scellé** sur la branche principale depuis le 10 au matin (R-2092, `1a372523…` ; conditions de GO-2026-11-07-04 remplies ; R-2143, C2) ; le « non rempli à la rédaction » de l'ordre (l. 46) vise le marqueur de l'ordre. Date de lecture du bras B : gardée comme manque (aucune pièce lue ne la donne) | § 0 l. 3 ; § 2.2 ; Q1 ; manque 12 |
| 18 | à corriger | **appliqué et mis à jour** : bras d'attaque (§ 2.5 : R-2127 ; question et réponse de R-2145 verbatim, comme le veut la précision de la mère ; R-611 cité ; R-2146 verbatim, postérieur à cette précision ; phrase sûre « monté ; rien n'a encore tourné ») ; verdict formel de T0.3 sur une branche, rien n'en est dit (vérifié : aucun verdict de T0.3 sous `docs/verdicts/` de `main`) ; **phrase des lignes 87-88 vérifiée** : « fausse pour la somme », « vraie, et même pessimiste, pour le max » (résultats de T0.3 l. 81-89 ; note mathématique v3 l. 107, 172 ; énoncé de la proposition 1 : rapport de niveau 1 sur 2606.10456, l. 37) | § 1.2 ; § 1.6 écarts 11, 12, 14 ; § 2.5 ; § 3 ; manque 7 |
| 19 | mineur | **appliqué** (verdict de P3 l. 14-15 ; « 0,5809 » aux l. 29 et **32** — la contre-lecture écrit 29 et 31) | § 1.2 ; § 2.3 |
| 20 | mineur | **appliqué** (T0.6 l. 539-540) | § 2.2 |
| 21 | mineur | **appliqué** (audit l. 6, 7) | § 1.1 |
| 22 | mineur | **appliqué** | § 1.3 |
| 23 | mineur | **appliqué** | § 0 l. 1 ; Q5 |
| 24 | mineur | **appliqué** ; « plusieurs versions d'un même texte » vérifié (T0.4 v1, v2, v3 ; quatre versions de l'étape 1 du gradient ; etc.) | § 1.3 |
| 25 | mineur | **appliqué** (l. 807-815, 961-963, 1368-1369 ; dernière phrase marquée [CE RÉDACTEUR]) | § 2.1 |
| 26 | mineur | **appliqué** : noms en clair à l'en-tête (J-D, J-A, J-C, étape A, variante B, chaînes v13 et v14, λ\*, W2, W2g, DT-4 ; r expliqué au § 2.4) ; « deux critères sur huit » → `registres/etat.md` l. 184 ; « 17:13 » → R-1902 l. 1860 ; heure de fin écrite au socle et au journal. Restent des identifiants (GO-…, R-…, N-…, T6-1, PB-2, A1b, P7) et des noms propres (Wilson, Holm, McNemar, Jonckheere–Terpstra, Open Science Framework, POPPER, HELIOS) | en-tête ; § 4 ; Q4 |
| 27 | mineur | **sans objet pour le socle** (divergence de l'état vivant) ; corrigée par la mère (R-2133 ; `registres/etat.md` l. 3 dit 17:13) | — |

**Corrections de ce rédacteur, hors contre-lecture** : (a) « facteur ≈ 33 » dit sans la réserve B1 (« la cause n'est pas
mesurée », verdict de P3 l. 26 ; défaut relevé dans le document « depuis zéro », R-2144) : § 1.2, Q1 ; (b) écart G1 « fin du
mois 4 » contre « fin M2 » (`docs/programme-controle-ia-v2.md` l. 190) ; (c) phrases du v18 à reprendre (l. 148-150, 319,
466, 549-550) ; (d) borne de destruction de l'instance de 7b (R-2143, B1) ; (e) T0.8 brouillon 1 (R-2131) ; (f) phrases des
concepts (R-2125, R-2136, R-2142, R-2149, R-2150) et J-C refusé (R-2135) ; (g) page publique d'A1-v4 (R-2131), interdit
d'Argon levé (R-2145) ; (h) échéance de GO-2026-11-09-05 le 21 ; (i) manifeste de la session-dépôt chez le tiers (R-2129).

**Décisions postérieures intégrées** : R-2116 à R-2131 (consigne) ; lues aussi, jusqu'à l'heure de rédaction, R-2132 à
R-2154 (borne de lecture : l. 2112, registre à `dbc7fb4a…` à 10:33:25), intégrées là où elles changent un fait du socle
(R-2132, R-2133, R-2134, R-2135, R-2136, R-2142, R-2143, R-2144, R-2145, R-2146, R-2149, R-2150, R-2152, R-2153, R-2154).
Non intégrées : R-2137 à R-2141, R-2147, R-2148, R-2151 (coordination des documents et de l'organisme, sans fait du socle) ;
la divergence sur la « pince » (R-2126), nœud du bras d'attaque, hors mandat.

## 2. Sources lues, avec empreintes (toutes recalculées par `sha256sum` à 10:29:29 ; compagnons comparés pour la consigne, les interdits, la v1, son journal, sa contre-lecture, les décisions et les pièces de T0.3 : conformes)

| pièce | chemin | sha256 | lu |
|---|---|---|---|
| consigne de la v1 | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-socle-preuves-entretien-taif-v1.md` | `a961fef642c128929390db50025011bd8f41489a03e25fd0fd82abaa013f4783` | en entier |
| interdits communs v2 | `…/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` | `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` | en entier |
| socle v1 | `brouillons/entretien-taif-v3/socle-preuves-entretien-v1.md` | `b8a97629e8376528d3d58fedab5d23da9d132924428dd9509bba3722876fdf2f` | en entier |
| journal de la v1 | `brouillons/entretien-taif-v3/socle-preuves-entretien-v1-journal.md` | `c3729c2bd80b191cee29907b703299b0d72856cc4fa36567dbb2143ac1933e2e` | en entier |
| contre-lecture de la v1 | `brouillons/entretien-taif-v3/socle-preuves-entretien-v1-contre-lecture-v1.md` | `48c7fcc2ab823856a0de1c4fd18d48df8e42733e2b25dc800207f9beafd33ff1` | en entier |
| programme d'entretien v18 | `brouillons/entretien-taif-v3/programme-entretien-taif-v18.md` | `e58ccfedf959748c7dfc9b987f2c7d3c7aa72492e9a5847ac0ceecc7b5a68643` | titres ; l. 125-157, 172, 410-426, 549-550, 568-585 ; recherches ciblées |
| contre-lecture v17 | `brouillons/entretien-taif-v3/contre-lecture-v17-v1.md` | `ea256783988605e236f537e26ec779435ff0293f18e0bb867859da64e7215d90` | « Défauts », constats 1 à 13 |
| texte de candidature envoyé | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` | `b2458c2d209aaa817ca3c77bfc8ef99288d489ae7b58b747fd8cda6a71e33ca0` | l. 7, 26, 31-36, 78-100, 143, 150-163, 240-242, 246-266, 268-300, 320-333 |
| budget envoyé | `docs/sources/candidature-taif-2026-10-07/budget_v3_TAIF_2026-10-07.txt` | `caec18b296c7a7cbda35ffc993667a339f891fe322f512a9731bc7a3bb7f92c7` | empreinte (contenu repris de la v1, conforme selon la contre-lecture) |
| résultats de T0.3 | `docs/notes/resultats-T0.3-v1.md` | `9ab618edae17e757ab83d5de7a346ebf08bebf89aef61e4337cb5c067e5fd545` | l. 1-30, 72-95 |
| note mathématique v3 | `docs/notes/note-mathematique-lemme-theoreme-v3.md` | `dfe4fe0fc4d025011bbe0f330fd591b1898dc7e767384e96c946b6388ad81cd0` | l. 1-12 ; lignes citant 2606.10456 (7, 53, 107, 172, 189) |
| rapport de niveau 1 sur 2606.10456 | `docs/sources/lecture-pdf-niveau1/rapport-2606.10456-v1.md` | `9a99fb81f6491baa2e1cc873523aba07f3086a9ac3970ea951c7cf4db9ea33f3` | lignes trouvées par motif (28-135) |
| P3-bis, brouillon 10 (non scellé) | `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md` | `9038a015c5756a289bebd2f08b1c33b1f2a26eb829bb2c4bc2afec04648fd1f9` | l. 800-975, 1000-1007, 1040-1048, 1337-1374 ; lignes de motif (143, 422, 433, 435, 595, 649, 661) |
| N-066 | `docs/decisions/decision-N-066-v1.md` | `21e83ed58c7498c65b7f9ae78613bc38301acdf0dd15a9890af13e6c0edbd351` | en entier |
| N-065 | `docs/decisions/decision-N-065-v1.md` | `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4` | en entier |
| N-064 | `docs/decisions/decision-N-064-v1.md` | `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97` | en entier |
| N-062 | `docs/decisions/decision-N-062-v1.md` | `63f426903e6d0774085a628ec019d2022d3107f6bd8e56eebbe75c0eeb0f3ccc` | en entier |
| N-063 v2 | `docs/decisions/decision-N-063-v2.md` | `b2d9f03543802f82890c99eff77d4aab34ad532b50986b887c046906914b625b` | en entier |
| N-055 | `docs/decisions/decision-N-055-v1.md` | `371879d5bd44f5fdd7f2ff2fe068065776000e0b2acc9118fa94b41f687340b6` | l. 1-12, 25-42 |
| N-056 | `docs/decisions/decision-N-056-v1.md` | `3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d` | l. 36-60 ; motifs |
| N-054 | `docs/decisions/decision-N-054-v1.md` | `c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f` | l. 33-45 |
| N-052 | `docs/decisions/decision-N-052-v1.md` | `817d218b22b8d1d4a2c03bb78fb4870867f19bd1a1f9c08b0a1873efbb31a384` | l. 1-30 |
| N-029 | `docs/decisions/decision-N-029-v1.md` | `084e30523c0a0349cb1daf0dcf804f6c9d38c10d4f8bceed23c787fa507f34e4` | l. 25-26 |
| N-015 | `docs/decisions/decision-N-015-v1.md` | `462785b333101c20e5a923b2155bfd5964dd4172aa896440c51e8baca3602b7b` | l. 1, 18-22 |
| N-060 v3 | `docs/decisions/decision-N-060-v3.md` | `2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591` | empreinte (contenu repris de la v1, conforme selon la contre-lecture) |
| verdict officiel d'A1-v4 | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md` | `e6e2f17076fab16f2684553765517937d528c657367075c126945c3ae3741cda` | en entier |
| texte scellé d'A1-v4 | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/preenregistrement-attaque-goodhart-v5-v1.md` | `d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6` | l. 193, 201, 323 |
| T0.6 scellé | `prereg/T0.6-organismes-v0-v1.md` | `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` | l. 505-545, 576-590 |
| ordre de 7b, brouillon 3 | `docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon3.md` | `eae1e64f99ce2e4f90b7cf28ffecda597d11d3f48d72b3898960342d8e9c3ad6` | l. 5, 45, 46, 251 (la l. 251 porte des durées de 7a, non reprises) |
| ordre de 7a | `docs/procedures/ordre-fille-cles-2-course-dose-reponse-exploratoire-v1.md` | `4c6c70d4e496bf2fd009cc25133a319151af600ec64065eb33903963fbda17a0` | l. 3, par motif seulement |
| verdict de P3 v2 | `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` | `05e896daed17cdb089cd10641878a5014b505eab0aa3d45d0dd7a60d87435751` | l. 1-35 ; motifs |
| verdict de l'audit de fuite | `docs/verdicts/verdict-audit-fuite-r1-v4-v1.md` | `320463e6c03189178a2436742fe78e1edeae59d6a738a52de581924d837929d7` | l. 3, 6, 7, 42, 58, 65 |
| verdict de l'étiqueteur, phase 1 | `docs/verdicts/verdict-etiqueteur-phase1-v1.md` | `9f7830b95cc0238d09d5846798c4ff12dba07644271330d4ed6ec43d555c6eae` | lignes de motif (21, 35, 42, 44, 48) |
| verdict d'A1-v3 | `docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md` | `7dade9ef12a4dfa4c1ce3345d35ce9b533e8696ebdf9882443a20ad5a5e78135` | empreinte |
| verdict du critère 1 de G0 | `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` | `63444faa4ce253fcfc19981224ab95bc243e9b2c74bf83daf181d0059d5b4a13` | empreinte |
| synthèse de l'état de l'art, niveau 2 | `docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md` | `bbe0c1f523ad83e13e5ce96d19c384e8596a96d298431b931f499826c773ceb8` | l. 1-12, 26-60 |
| programme v2 | `docs/programme-controle-ia-v2.md` | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` | l. 190, 256 (par motif) |
| table scellée des dépenses | `livrables/registres-taif-v4/total-depenses-v3.md` | `123be1a7e1c345574d451a0e4ee31f3193f6b7fc1a522f2e293934e03b94ea21` | l. 1-30, 47, 51, 53, 58, 96, 125-153 |
| sources de la table | `livrables/registres-taif-v4/sources-v3.json` | `a6d15d1a98a7ee37aa9d26fdc3b49c4143677e06a3e7bfe5c87b513beaeb9224` | clés et cellule « (sans GO cité) », par script |
| table du coût par résultat | `livrables/registres-taif-v4/cout-par-resultat-v3.md` | `537fd93afdef88d47fe182f68611393f118e3d0341ce2013689c6639ca722d62` | l. 7, 185-204 (observation 4 ci-dessous) |
| calibration | `livrables/registres-taif-v4/calibration-v3.md` | `0f1bca5aa900bffed944b9f7c0b2b5f1b2a137b2b3c8337c9b0b28e3d881c0f4` | l. 34, 70-76, 245-268 ; décompte des lignes par texte |
| manifeste de la simulation | `runs/20261004-080257-t03/manifeste.json` | `c9bba5e1f5f8dbf268e47023db8fac56c2cfd011721c6f89ba8ecad413e1a8ea` | empreinte seulement (égale à celle des résultats de T0.3) |
| registre des décisions (vivant) | `registres/decisions.md` | `dbc7fb4a23508beeccd66a921bbdd7810ef1d9ce3e64c57494ca643e4e937ab7` à 10:33:25 (2112 l.) ; registre seulement allongé depuis le premier relevé : les 2088, 2098, 2102, 2103 et 2109 premières lignes ont gardé les empreintes `65cc0667…`, `01cdece6…`, `9f4bb8b1…`, `e44a0f29…`, `cf483417…` | R-2116 à R-2154 (l. 2074-2112) ; R-025, R-098, R-327, R-600, R-611, R-622, R-746, R-749, R-750, R-765, N-027, R-1579, R-1580, R-1757, R-1834, R-1869, R-1876, R-1902, R-2021, R-2045, R-2047, R-2057, R-2067, R-2070, R-2077, R-2079, R-2082, R-2092, R-2094, R-2095, R-2097, R-2099, R-2101, R-2103, R-2110 (début), R-2111 à R-2115 ; motifs (`SCORES-T07`, `verifier_ecart_dt4_v2`, « N-027 bis », « 602 ») |
| registre des autorisations (vivant) | `registres/go.md` | `e682abb0db3a0da37c0d764a7c659f638d449df266f6c9580d3ec481c8d44155` (inchangé) | l. 53, 54, 66, 161, 163, 210, 216, 217, 256, 262, 264, 267, 282, 283, 285, 288-296 |
| registre des dépenses (vivant) | `registres/depenses.md` | `e7b83d372f4795e073bf5fda6d23bb9d74743aca9df2777c15e3186642740f1b` (inchangé ; ses 405 premières lignes ont l'empreinte `a6437706…` lue par la table scellée) | l. 43, 90, 92, 106, 152-168, 263, 267, 403-413 ; comptes : GO-2026-11-02-22 0, GO-2026-11-08-12 0 |
| registre des scellements | `registres/scellements-v1.md` | `d48af4f5d7682c2a5051cb9ed8ef31ece6aaf063a787bd0c4357f2fad559c046` (inchangé) | en entier |
| état vivant | `registres/etat.md` | `e6d41dbe378aaccc691ebfb443f2562f6cf36fcf092a874680b1f939abe083b4` à 10:29:29 (versions vues avant : `096d57c1…`, `67f95ebf…`) | l. 3, 23 (motif), 173, 175, 184, 239 ; numéros vérifiés inchangés sur la dernière version |

**Non lus** (interdits ou hors besoin) : tout `lecture-sondes-t06.json` ; tout `diag/` et `runs/` de 7a ; les branches
`donnees/lecture-b-7a-quarantaine-v1` et `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
`docs/notes/bras-attaque/` ; l'étiqueteur (items, clés, réponses, branche) ; `scripts/extraire_mesures_epreuve_t06_v1.py` ;
les textes d'actions de P3 ; **aucun fichier de T0.7** ; la consigne de la v19 sur la pince ; la branche de la session-dépôt
et le verdict formel de T0.3 qu'elle porte ; les documents « depuis zéro » ; les PDF de la littérature ; les consoles de
facturation ; la copie publique (objet `56fdb15a` absent du clone local).

## 3. Manques (repris au § 6 du socle)

Dépense d'A1-v4 hors registre ; aucun total ni facture, ni ventilation ; rangée « sans GO cité » à rattacher ; incident du
23 octobre de montant inconnu ; dépôt chez le tiers privé et non gelé ; T0.8 non scellé (brouillon 1) ; T0.7, P3-bis,
phrases des concepts, ordre de 7b et ordre de l'étape A non scellés ; ordre de la variante B non exécutable en l'état et
ligne `CODE-T07` non inscrite (R-2153) ; citations de la page publique d'A1-v4 en attente d'un « go publication » (R-2154) ;
aucune réexécution par un tiers, contenu de la copie
publique non vérifié ; verdict formel de T0.3 hors de la branche principale ; clause N-027 bis non inscrite ; date de
l'entretien visée, non confirmée avec le fonds ; pages de la littérature non revérifiées ; audit DT-4 des révisions 4 à 10
de T0.6 à faire ; date de lecture du bras B non écrite ; ligne 245 du brouillon 20 de T0.7 non relue.

## 4. Observations hors du mandat (règle 4)

1. **Table du coût par résultat** (`cout-par-resultat-v3.md`, `537fd93a…`, l. 193) : elle affiche **5,59** pour la ligne 90
   du registre des dépenses, qui est le **crédit relu** (en gras), non une dépense ; la table des dépenses
   (`total-depenses-v3.md`, l. 47) compte cette ligne pour **4,71** (la charge de l'instance de P3 de ce jour) : la rangée
   « (sans GO cité) » vaut 54,08 avec 4,71 et vaudrait 54,96 avec 5,59 [CE RÉDACTEUR : recalcul par script des montants en
   gras]. Le socle ne cite pas la table du coût par résultat ; à signaler à la mère.
2. La contre-lecture renvoie trois fois à une ligne voisine de la bonne (v18 l. 144 pour 142-143 ; verdict de P3 l. 31 pour
   32 ; « révisions 5 à 10 » pour « r4 à r10 ») : sans effet sur le fond.

## 5. Gestes et écarts à déclarer

1. Aucune recherche récursive sur un dossier qui contient un chemin interdit : `grep` et `sed` sur des fichiers nommés ;
   `git ls-files -- docs/notes ':(exclude)docs/notes/bras-attaque'` filtré aussitôt par motif (noms seulement) ;
   `git ls-files docs/verdicts` filtré ; `git ls-files` sur trois chemins nommés du run de T0.3 (noms seulement) ; `ls` non
   récursif de `brouillons/entretien-taif-v3/`, `brouillons/P3-bis-temoin-positif-v1/`, `docs/decisions/` (filtré),
   `docs/procedures/` (filtré sur 7b), `docs/sources/candidature-taif-2026-10-07/`, `docs/sources/lecture-pdf-niveau1/`
   (filtré), `livrables/registres-taif-v4/`, `prereg/` (filtré), du dossier du verdict d'A1-v4. Lecture seule de git :
   `git rev-parse`, `git log -1`, `git branch -a --list` (un motif, noms seulement), `git cat-file -t` (objet absent). Aucun
   `verifier-arbre`.
2. `python -I` sur `sources-v3.json` et sur `registres/depenses.md` (lecture et recalcul de la rangée « sans GO cité »).
3. J'ai lu des passages du brouillon 10 de P3-bis et de l'ordre de 7b, et aucun fichier de T0.7 : **exclu de tout rôle de
   lecteur de P3-bis** ; la mère jugera pour 7b.
4. Pendant la rédaction, la mère a transmis une précision sur R-2145 (écrire la question et la réponse telles quelles, sans
   conclusion ; phrase sûre « monté ; rien n'a encore tourné ») : appliquée (§ 2.5), après lecture de R-2145 au registre.
   R-2146 (10:20), postérieure à cette précision, lève la restriction de R-611 pour le bras : ajoutée verbatim, sans
   conclusion, avec un renvoi à aligner la réponse du v18 § 3.11.
5. Aucun appel externe, aucune dépense, aucune écriture git, aucune commande d'environnement (`env`, `printenv`, `set`,
   `export -p`, `/proc/*/environ`), aucune valeur de clé. **Aucun refus** de permission ni de classifieur.
6. La suite d'essais n'a pas été lancée (interdit 5). Aucune valeur numérique tirée d'une sonde de 7a sous mes yeux ni
   dans le socle.
