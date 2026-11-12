# Journal du rédacteur neuf — candidat 2 de T0.7 et ordre d'exécution brouillon 6 (v1)

Modèle : Opus 5.5 (claude-opus-5-5). Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-t07-candidat2-v1.md`, empreinte vérifiée `d29c78585ee578127304d840851fa7017c6e756324f47caa9c401a84ee553eae` (sha256sum -c : OK).
Journal tenu au fil (le conteneur peut redémarrer). Heures relevées par `date -u`.

- 2026-11-11T02:41:48Z — consigne vérifiée et lue ; bac à sable créé ; journal ouvert.
- 2026-11-11T02:42:26Z — entrées vérifiées par sha256sum (toutes égales aux préfixes de la consigne) : candidat 1 1718f2a0…, pièces du candidat 1 (couples f73c5882…, script 2e74a1b4…, journal d4dcc2de…, configuration v5 4be50447…), vérification courte ef3431a1…, notes v1 8e996ab0…, v2 5ccf0940…, v3 760a562c…, audit de P3 57f16378…, rapport du code cb31edc8…, configuration v7 3701407c…, ordre brouillon 5 d0b75d16… et son script 2fb71657…. Registre lu : R-2264, R-2269, R-2270, R-2271, R-2273, R-2285, R-2296, R-2298, R-2299, R-2304.
- 2026-11-11T02:42:42Z — lus : note v3 (entière), audit de P3 § 7 (réserves 1 et 2), rapport du code du plancher v3 (entier ; devis § 8, repli et texte § 9). Prochain : code au commit 0d0c5da4 (plancher_v2.comparer_difference_au_plancher, plancher_v3, reextraction_p3_v1, lecture_v4), configuration v7.
- 2026-11-11T02:48:38Z — lus : sections du candidat 1 (En-tête, Hypothèse, Prédiction, Métrique, Seuil, Plan d'analyse, Critères, Liste d'arrêt, Puissance, Données gardées, Calcul et dépense) ; code au commit 0d0c5da4 (plancher_v2, plancher_v3, reextraction_p3_v1, lecture_v4 en partie, lectures_t07_v2, lecture_v3) ; note v2 § 4-5 ; audit de P3 § 6 et rapport-p3-v1.json (rejeu sur les données de P3 : demi-largeurs de D). Lecture de l'ordre brouillon 5.
- 2026-11-11T02:50:52Z — constats : (1) module au commit 0d0c5da4 : 26 fichiers, les dix-huit de CODE-T07-v1.json inchangés, huit neufs (plancher_v2, lecture_v3, lectures_t07_v2, plancher_v3, reextraction_p3_v1, lecture_v4, passe_blanc_v2, repli_etapes_v2) ; 0d0c5da4 non fusionné dans main (tête a6f435a0). (2) Le script de l'instance v2 (e68d3306) appelle lecture_v2 en dur (l. 302 empreinte-config, 357 repli-seul, 367 passe-blanc, 372 etape-a-apres-repli) : il refuse la configuration v7 ; un script v3 est nécessaire (point à porter au rapport, proposition). (3) P9 et § 1 de l'ordre exigent src/ de C7 égal à 37485ce5 : faux après la fusion du code neuf (C7 laissé à la mère).
- 2026-11-11T02:53:53Z — puissance : « rejeu du code » lu comme le rejeu de la règle (a) sur les données de P3 par l'audit (rapport-p3-v1.json, entrées saboteur-honnete : demi-largeurs de D 0,047901 et 0,048676 à 97,5 %) ; script neuf puissance_regle_a_t07_v1.py : formule du texte (brouillons 6 et 22) avec la demi-largeur de D au lieu de celle de la sonde ; contrôles : B3 de l'audit (0,6376 ; 0,6025) et sortie du brouillon 22 (0,6345 ; 0,5996 ; 0,5752 ; 0,6595).
- 2026-11-11T02:54:47Z — puissance_regle_a_t07_v1.py joué (code 0, « TOUS LES CONTRÔLES PASSENT »), sortie versée puissance-regle-a-t07-v1.txt ; les deux scellés.
- 2026-11-11T02:55:04Z — registre relu de R-2264 à R-2304 (02:54:54 UTC, dernière entrée R-2304) pour LECTURES_7A_T07 : seule R-2264 nomme 7a (renvoi) ; aucune lecture d'une sortie de 7a consignée ; couple de mise à jour ajouté après VC1-A.
- 2026-11-11T02:57:32Z — src/ du commit 0d0c5da4 reconstitué au bac à sable par git show (196 fichiers) ; configuration v7 : lecture_v4 empreinte-config code 0, 4ff92c8e… (égale au rapport) ; lecture_v2 la refuse (n_plancher 800 ≠ 200) ; v5 → v7 : seules n_plancher, methode_plancher, plancher_figees changent.
- 2026-11-11T03:00:09Z — ordre brouillon 6 : conception arrêtée. Couples O6 : titre, statut, section neuve « 0 ter », § 1 (code : SRC7 ; script v3 ; configuration v7 et chemin final ; machine : préférence EPYC), P6 (26 modules), P8 (ANT0 ≤ 3,6), P9 (SRC7), P13 neuf (révision de P3, script v3, SRC7), ligne (A) (script v3, marqueurs SHA_SCRIPT_V3_T07 et COMMIT_SRC_CONTRE_LU_T07, REV_P3), § 2.5 (sorties neuves), § 4.1 (SRC7, contrôle de révision), § 4.3 (préférence EPYC), § 4.4 (borne 41 616 s), § 5 (titre, étapes 8, 9, 11, 12, 13 : lecture_v4, CUBLAS, ATEN/MKL), § 6 (devis, coût, ANT0), § 7 (CLE-12 ≈ 0,45 h), § 9 (étape B lecture_v4), § 11, § 12, § 13 (S-12, S-13). Écarts à « tout le reste égal » nécessaires (script v3, SRC7) déclarés au rapport.
- 2026-11-11T03:04:06Z — ordre brouillon 6 écrit par son script (essai sur racine factice, puis dépôt : code 0, « TOUT PASSE », 37 couples, couples défaits → brouillon 5 octet pour octet, 12 marqueurs dont 2 neufs, 8 blocs bash, 10 extraits Python, choix de l'offre essayé) ; brouillon 6 92d9aebe…, script scellés ; brouillon 5 intact (d0b75d16…).
- 2026-11-11T03:08:54Z — candidat 2 : ancres relevées (toutes à une occurrence au candidat 1, sauf celles qui suivent VC1-A et VC1-B, appliqués d'abord). Couples gelés retenus : G2-01 (Hypothèse), G2-02 (Prédiction), G2-03 et G2-04 (Métrique), G2-05 à G2-08 (Seuil), G2-09 à G2-13 (Plan d'analyse), G2-14 à G2-16 (Critères), G2-17 (Liste d'arrêt). Génération des couples par un générateur du bac à sable (non versé, empreinte au journal).
- 2026-11-11T03:16:53Z — générateur du bac à sable joué (60 couples, 17 gelés ; essai1, JSON 4d0053d0…) ; script faire joué sur une racine factice du bac à sable (.git et src liés en lecture) : code 0, « TOUT PASSE » ; candidat 2 d'essai 68c0dfdf…, 3 309 lignes. Relecture des passages neufs avant l'écriture dans le dépôt.
- 2026-11-11T03:18:17Z — couples définitifs générés (beb5ecfb…, générateur du bac à sable d305d832…, non versé) ; script faire joué sur le dépôt de 03:17:58 à 03:18:05 UTC : code 0, « TOUT PASSE », sortie égale à celle de l'essai sur racine factice, candidat 2 égal à l'octet (9de13f6a…) ; candidat 1, brouillon 5 et son script intacts ; candidat 2, couples et script faire scellés.

## Couples du candidat 2 (dans l'ordre d'application ; « gelée » = empan « Hypothèse » à « Liste d'arrêt »)

| id | section | gelée | motif | longueur ancien → nouveau (caractères) |
|---|---|---|---|---|
| C2-01 | titre | non | numéro : candidat 2 | 87 → 87 |
| C2-02 | statut | non | statut du candidat 2 ; lu ; pièces ; statut du candidat 1 gardé pour mémoire | 68 → 7431 |
| C2-03 | table « du candidat 1 au candidat 2 » (neuve) | non | table des changements du candidat 2 ; changements gelés un par un | 47 → 7481 |
| C2-04 | En-tête (auteur) | non | en-tête décrivant ce candidat | 144 → 243 |
| C2-05 | En-tête (commit du code : marqueur neuf) | non | consigne, point 7 : C7 et CODE-T07 laissés à la mère ; vingt-six modules (R-2304) | 74 → 2252 |
| C2-06 | En-tête (empreintes du module) | non | vingt-six modules au candidat 2 | 82 → 179 |
| C2-07 | En-tête (entropie) | non | planchers des figées tirés sous l'entropie de ce texte (R-2298 (3), R-2304) | 95 → 295 |
| VC1-A | En-tête (lectures de 7a) | non | couple VC1-A de la vérification courte du candidat 1, tel qu'écrit (R-2264, R-2269) | 80 → 799 |
| C2-08 | En-tête (lectures de 7a, candidat 2) | non | liste mise à jour au candidat 2 : registre relu de R-2264 à R-2304 | 93 → 393 |
| VC1-B | En-tête (configuration) | non | couple VC1-B de la vérification courte du candidat 1, tel qu'écrit (R-2264, R-2269) | 82 → 386 |
| C2-09 | En-tête (configuration : empreinte canonique de la v7) | non | consigne, point 7 : EMPREINTE_CONFIG_T07 → configuration v7 (R-2304) | 450 → 599 |
| C2-10 | En-tête (configuration : chemin final de la v7) | non | consigne, point 7 : chemin final nommé par l'ordre, brouillon 6 | 91 → 1283 |
| C2-11 | Décisions (P-064) | non | consigne, point 7 : MOT_LAZAR_P064 rempli par R-2269 | 18 → 311 |
| C2-12 | Décisions (P-065) | non | consigne, point 7 : MOT_LAZAR_P065 rempli par R-2269 | 18 → 367 |
| G2-01 | Hypothèse | **oui** (Hypothèse) | R-2299 (réserves de P3 jointes au nul cité) ; R-2304 et note v3, § 6, point 4 (réplication) | 104 → 916 |
| G2-02 | Prédiction chiffrée et signe attendu | **oui** (Prédiction chiffrée et signe attendu) | R-2299 (réserves de P3 jointes au nul cité) | 98 → 581 |
| G2-03 | Métrique | **oui** (Métrique) | R-2285 (800 directions, règle (a) à l'étape B) ; R-2298 (1) à (3) ; R-2304 (plancher neuf des figées) | 4116 → 7059 |
| G2-04 | Métrique | **oui** (Métrique) | R-2298 (1) : n_plancher = 800 pour tout plancher tiré à l'étape A (T4 : plancher de la sonde du domaine) | 54 → 157 |
| G2-05 | Seuil | **oui** (Seuil) | R-2285 (règle (a), changement autorisé) ; R-2270, R-2271, R-2273, R-2298, R-2304 | 132 → 2607 |
| G2-06 | Seuil | **oui** (Seuil) | R-2285 : complément de la même définition | 222 → 359 |
| G2-07 | Seuil | **oui** (Seuil) | R-2285 : « contraire » = « au-dessus » là où « non » est prédit (même définition) | 83 → 171 |
| G2-08 | Seuil | **oui** (Seuil) | R-2285 : l'intervalle corrigé (Bonferroni, niveau inchangé) est celui de D | 101 → 184 |
| G2-09 | Plan d'analyse | **oui** (Plan d'analyse) | R-2298 (3), R-2304 : plancher neuf des figées (remplace la réutilisation) | 159 → 482 |
| G2-10 | Plan d'analyse | **oui** (Plan d'analyse) | R-2298 (3), R-2304 : réextraction à l'étape A, avant toute autre extraction ; gardes et paliers tels que codés | 123 → 3004 |
| G2-11 | Plan d'analyse | **oui** (Plan d'analyse) | R-2285, R-2298 (1) et (2) : 800 directions, notation par lots ; 200 de P3 en descriptif | 282 → 534 |
| G2-12 | Plan d'analyse | **oui** (Plan d'analyse) | R-2285, R-2304 : fonction de lecture de l'étape B = celle de la v4 | 68 → 215 |
| G2-13 | Plan d'analyse | **oui** (Plan d'analyse) | R-2285 : la grandeur de décision (D) est rapportée | 140 → 335 |
| G2-14 | Critères de lecture gelés | **oui** (Critères de lecture gelés) | R-2304 (repli) : une cause neuve de « échec », sans changer la grille | 110 → 187 |
| G2-15 | Critères de lecture gelés | **oui** (Critères de lecture gelés) | R-2304 (repli) : motif écrit sous L4b | 77 → 139 |
| G2-16 | Critères de lecture gelés | **oui** (Critères de lecture gelés) | R-2299 (réserves de P3 jointes au nul cité) | 67 → 550 |
| G2-17 | Liste d'arrêt | **oui** (Liste d'arrêt) | R-2304 (repli du plancher neuf des figées) ; R-2298 (2) (contrôle en ligne de la notation par lots) | 93 → 1857 |
| C2-13 | Puissance | non | consigne, point 4 : grandeurs de la note v3 et du rejeu du code ; perte de puissance ; réserve de la note v3 ; réserves de P3 (R-2299) | 7844 → 9031 |
| C2-14 | Données gardées | non | 800 directions ; plancher des figées (R-2298, R-2304) | 99 → 274 |
| C2-15 | Données gardées | non | plancher des figées (R-2298 (3), R-2304) | 117 → 489 |
| C2-16 | Calcul et dépense (devis) | non | consigne, point 6 : devis de l'étape A du rapport du code ; réserve CLE-12 aggravée | 80 → 1475 |
| C2-17 | Calcul et dépense (minuterie) | non | borne de la minuterie relevée (ordre, brouillon 6, § 4.4) | 84 → 149 |
| C2-18 | Calcul et dépense (P8) | non | condition P8 relevée (ordre, brouillon 6) | 44 → 88 |
| C2-19 | Calcul et dépense (marge à ECH) | non | marge à ECH à la borne neuve de P8 (ordre, brouillon 6, § 6) | 42 → 116 |
| C2-20 | Calcul et dépense (réserve CLE-12) | non | réserve CLE-12 aggravée (R-2304) | 29 → 91 |
| C2-21 | Calcul et dépense (script de l'instance) | non | script v3 exigé par l'ordre, brouillon 6 (S-12) | 47 → 252 |
| C2-22 | Lignes de registre (CODE-T07) | non | vingt-six modules ; C7 laissé à la mère (consigne, point 7) | 189 → 324 |
| C2-23 | Module (introduction) | non | état du module au candidat 2 (R-2304) | 51 → 2899 |
| C2-24 | Module (configuration) | non | n_plancher = 800 (R-2298) | 64 → 192 |
| C2-25 | Module (fonctions sur scores) | non | fonction de lecture de l'étape B de la v4 (R-2285, R-2304) | 114 → 570 |
| C2-26 | Module (point 13, repli) | non | commandes lecture_v4 (R-2304) | 95 → 229 |
| C2-27 | Module (point 18, passe à blanc) | non | commande lecture_v4 (R-2304) | 50 → 112 |
| C2-28 | Module (points d'entrée) | non | lecture_v4 seule (R-2304 ; rapport, § 9.4) | 127 → 472 |
| C2-29 | Module (ordre d'exécution) | non | consigne, point 7 : EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07 → ordre, brouillon 6 | 187 → 675 |
| C2-30 | Concordance avec le texte de validité de l'adaptateur (E6) | non | 800 directions par plancher de sonde neuve (R-2298) | 57 → 207 |
| C2-31 | Reste (1 nonies) | non | fait et reste au candidat 2 | 78 → 1642 |
| C2-32 | Contre-lecture | non | à contre-lire par une vérification courte neuve (consigne, point 9) | 19 → 1123 |
| C2-33 | Marqueurs (paragraphe) | non | compte du candidat 2 | 70 → 865 |
| C2-34 | Marqueurs (table : C7_ET_CODE_T07_26_MODULES) | non | marqueur neuf (consigne, point 7) | 65 → 639 |
| C2-35-P064 | Marqueurs (table : MOT_LAZAR_P064) | non | rempli au candidat 2 (R-2269) | 47 → 82 |
| C2-35-P065 | Marqueurs (table : MOT_LAZAR_P065) | non | rempli au candidat 2 (R-2269) | 47 → 82 |
| C2-36 | Marqueurs (table : LECTURES_7A_T07) | non | mis à jour (VC1-A ; candidat 2) | 51 → 226 |
| C2-37 | Marqueurs (table : EMPREINTE_CONFIG_T07) | non | configuration v7 (R-2304) | 140 → 549 |
| C2-38 | Marqueurs (table : COMMIT_CODE_T07) | non | remplacé, pour le code, par le marqueur neuf | 113 → 266 |
| C2-39 | Marqueurs (table : EMPREINTES_CODE_T07) | non | remplacé, pour le code, par le marqueur neuf | 117 → 203 |
| C2-40 | Marqueurs (table : EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07) | non | ordre, brouillon 6 | 198 → 426 |

Textes exacts : le JSON des couples (champs `ancien`, `nouveau`). Le script vérifie que chaque section gelée, ses couples gelés défaits, redonne celle du candidat 1 octet pour octet ; aucun autre changement dans l'empan gelé.

## Sortie du script faire (dépôt, 2026-11-11, 03:17:58 à 03:18:05 UTC ; code 0)

```
brouillons/T0.7-sondes-v0-v1-candidat1.md : 1718f2a047195c85… (égale)
brouillons/T0.7-sondes-v0-v1-candidat2-pieces/T0.7-sondes-v0-v1-candidat2-couples-v1.json : beb5ecfb210978a1… (égale)
prereg/contre-lectures/T0.7-sondes-v0-v1-candidat1-verification-courte-v1.md : ef3431a1a45c5e1f… (égale)
docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6.md : 92d9aebee0634c91… (égale)
brouillons/T0.7-sondes-v0-v1-candidat1-pieces/configuration-t07-v5.json : 4be50447d1063015… (égale)
docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v7.json : 3701407cf96f2851… (égale)
brouillons/T0.7-sondes-v0-v1-candidat2-pieces/puissance_regle_a_t07_v1.py : 4523a480f8560089… (égale)
brouillons/T0.7-sondes-v0-v1-candidat2-pieces/puissance-regle-a-t07-v1.txt : af73498e757d4ab3… (égale)
docs/notes/g0-deux-semaines-v1/audit-p3-regle-plancher-v1/audit-verdict-p3-regle-plancher-v1.md : 57f16378d0bf15e5… (égale)
docs/notes/g0-deux-semaines-v1/audit-p3-regle-plancher-v1/rapport-p3-v1.json : bdd5f6d5895d294e… (égale)
docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v3.md : 760a562c15991421… (égale)
docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v1.md : cb31edc844c6bc4e… (égale)
registres/code-t07/CODE-T07-v1.json : 9ef4ede751fcceb5… (égale)

# configuration v7
clés qui changent de la v5 à la v7 : ['methode_plancher', 'n_plancher', 'plancher_figees'] ; n_plancher 200 → 800 ; entropie inchangée : True : True
module recopié au commit 0d0c5da4 (196 fichiers) ; `lecture_v4 empreinte-config` : code 0, 4ff92c8ef07943e093793c218967be36621410714be9634ccccc3c27811d2b38 ; `lecture_v2 empreinte-config` : code 2, « REFUS : mode réel : n_plancher 800 ≠ 200 » : True
VC1-A tel qu'écrit dans la vérification courte : True
VC1-B tel qu'écrit dans la vérification courte : True

# application (60 couples) (id ; ligne ; sections touchées ; gelée)
C2-01 ; l. 1 ; (avant la première section) ; non
C2-02 ; l. 3 ; (avant la première section) ; non
C2-03 ; l. 180 ; Table « ce qui change du 22 au candidat  ; non
C2-04 ; l. 621 ; En-tête ; non
C2-05 ; l. 622 ; En-tête ; non
C2-06 ; l. 641 ; En-tête ; non
C2-07 ; l. 674 ; En-tête ; non
VC1-A ; l. 701 ; En-tête ; non
C2-08 ; l. 701 ; En-tête ; non
VC1-B ; l. 676 ; En-tête ; non
C2-09 ; l. 676 ; En-tête ; non
C2-10 ; l. 676 ; En-tête ; non
C2-11 ; l. 857 ; Décisions DS-1 et DS-2 — défauts confirm ; non
C2-12 ; l. 858 ; Décisions DS-1 et DS-2 — défauts confirm ; non
G2-01 ; l. 956 ; Hypothèse ; OUI
G2-02 ; l. 1090 ; Prédiction chiffrée et signe attendu ; OUI
G2-03 ; l. 1125 ; Métrique ; OUI
G2-04 ; l. 1173 ; Métrique ; OUI
G2-05 ; l. 1185 ; Seuil ; OUI
G2-06 ; l. 1186 ; Seuil ; OUI
G2-07 ; l. 1189 ; Seuil ; OUI
G2-08 ; l. 1212 ; Seuil ; OUI
G2-09 ; l. 1253 ; Plan d'analyse ; OUI
G2-10 ; l. 1367 ; Plan d'analyse ; OUI
G2-11 ; l. 1376 ; Plan d'analyse ; OUI
G2-12 ; l. 1428 ; Plan d'analyse ; OUI
G2-13 ; l. 1445 ; Plan d'analyse ; OUI
G2-14 ; l. 1758 ; Critères de lecture gelés ; OUI
G2-15 ; l. 1840 ; Critères de lecture gelés ; OUI
G2-16 ; l. 1839 ; Critères de lecture gelés ; OUI
G2-17 ; l. 1911 ; Liste d'arrêt ; OUI
C2-13 ; l. 1953 ; Puissance (planification, jamais une sél ; non
C2-14 ; l. 1975 ; Données gardées et plan de stockage (A6  ; non
C2-15 ; l. 1977 ; Données gardées et plan de stockage (A6  ; non
C2-16 ; l. 2012 ; Calcul et dépense (aucun épisode joué ;  ; non
C2-17 ; l. 2012 ; Calcul et dépense (aucun épisode joué ;  ; non
C2-18 ; l. 2012 ; Calcul et dépense (aucun épisode joué ;  ; non
C2-19 ; l. 2012 ; Calcul et dépense (aucun épisode joué ;  ; non
C2-20 ; l. 2012 ; Calcul et dépense (aucun épisode joué ;  ; non
C2-21 ; l. 2012 ; Calcul et dépense (aucun épisode joué ;  ; non
C2-22 ; l. 2135 ; Lignes de registre (CLT7-03, CLT7-07 ; r ; non
C2-23 ; l. 2151 ; Module de lecture `src/controle_ia/t07/` ; non
C2-24 ; l. 2225 ; Module de lecture `src/controle_ia/t07/` ; non
C2-25 ; l. 2238 ; Module de lecture `src/controle_ia/t07/` ; non
C2-26 ; l. 2581 ; Module de lecture `src/controle_ia/t07/` ; non
C2-27 ; l. 2586 ; Module de lecture `src/controle_ia/t07/` ; non
C2-28 ; l. 2591 ; Module de lecture `src/controle_ia/t07/` ; non
C2-29 ; l. 2597 ; Module de lecture `src/controle_ia/t07/` ; non
C2-30 ; l. 2713 ; Concordance avec le texte de validité de ; non
C2-31 ; l. 2921 ; Reste avant le scellement (au plus tard  ; non
C2-32 ; l. 2956 ; Contre-lecture ; non
C2-33 ; l. 3252 ; Marqueurs à remplir avant le scellement ; non
C2-34 ; l. 3290 ; Marqueurs à remplir avant le scellement ; non
C2-35-P064 ; l. 3293 ; Marqueurs à remplir avant le scellement ; non
C2-35-P065 ; l. 3294 ; Marqueurs à remplir avant le scellement ; non
C2-36 ; l. 3296 ; Marqueurs à remplir avant le scellement ; non
C2-37 ; l. 3297 ; Marqueurs à remplir avant le scellement ; non
C2-38 ; l. 3298 ; Marqueurs à remplir avant le scellement ; non
C2-39 ; l. 3299 ; Marqueurs à remplir avant le scellement ; non
C2-40 ; l. 3308 ; Marqueurs à remplir avant le scellement ; non
couples gelés : 17 ; égaux au mandat (G2-01 à G2-17, sections déclarées) : True

écrit : brouillons/T0.7-sondes-v0-v1-candidat2.md
candidat 2 : 9de13f6a9a40267ff8111a009643a4871eb9e0f91ae23ba89182d3abbc9a3335 ; 3309 lignes

# vérifications
(1) titre et premier statut : True
(2) empan gelé (couples gelés défaits dans l'ordre inverse, section par section) :
    « Hypothèse » : couples ['G2-01'] ; 2 lignes de différence ; égale au candidat 1 une fois défaite : True
    « Règle « mots et coût » de T0.6 (CLT7-02 ; lue, j » : couples [] ; 0 lignes de différence ; égale au candidat 1 une fois défaite : True
    « Prédiction chiffrée et signe attendu » : couples ['G2-02'] ; 2 lignes de différence ; égale au candidat 1 une fois défaite : True
    « Métrique » : couples ['G2-03', 'G2-04'] ; 30 lignes de différence ; égale au candidat 1 une fois défaite : True
    « Seuil » : couples ['G2-05', 'G2-06', 'G2-07', 'G2-08'] ; 13 lignes de différence ; égale au candidat 1 une fois défaite : True
    « Plan d'analyse » : couples ['G2-09', 'G2-10', 'G2-11', 'G2-12', 'G2-13'] ; 14 lignes de différence ; égale au candidat 1 une fois défaite : True
    « Écrits exigés par P3-bis avant toute ouverture ( » : couples [] ; 0 lignes de différence ; égale au candidat 1 une fois défaite : True
    « Critères de lecture gelés » : couples ['G2-14', 'G2-15', 'G2-16'] ; 6 lignes de différence ; égale au candidat 1 une fois défaite : True
    « Liste d'arrêt » : couples ['G2-17'] ; 2 lignes de différence ; égale au candidat 1 une fois défaite : True
(3) sections neuves : ['Table « ce qui change du candidat 1 au candidat 2 »'] ; disparues : []
(4) marqueurs restants : {'<<C7_ET_CODE_T07_26_MODULES>>': 1} ; remplis encore présents : []
(5) controle_ia.prereg.problemes(candidat 2) : ['marqueurs de gabarit restants : <<C7_ET_CODE_T07_26_MODULES>>'] ; à valeur factice : []
(6) règle (a) citée telle que l'écrit plancher_v2.py au commit 0d0c5da4 : True
(7) module au commit 0d0c5da4 : 26 fichiers ; huit neufs et dix-huit anciens à leur empreinte et cités : True
(8) devis communs au candidat 2 et à l'ordre, brouillon 6 : True
(9) puissance : 28 nombres sur 28 cités et présents dans la sortie versée
(10) réserves de P3 : forme du registre (R-2299) jointe 4 fois (Hypothèse, Prédiction, L4, Puissance) ; forme de l'audit (réserves 1 et 2) en « Puissance » : True
(11) phrases exigées : 19 sur 19 ; passages retirés encore présents : []
(12) différentiel candidat 1 → candidat 2 : 109 lignes retirées, 119 lignes ajoutées ; 60 couples, dont 17 gelés

TOUT PASSE
```

## Sortie du script de l'ordre, brouillon 6 (dépôt ; code 0)

```
brouillon 5 d0b75d161e80… et configuration v7 3701407cf96f… vérifiés ; la v7 cite les six chemins de la v4
37 couples appliqués, chacun à une occurrence
tout le reste égal à l'octet : couples défaits dans l'ordre inverse → brouillon 5 retrouvé (546 → 610 lignes)
marqueurs : 12, une occurrence chacun (dont deux neufs), aucun autre
aucune commande lecture_v2 restante hors des mentions « au brouillon 5 »
phrases exigées : 21 présentes
§ 6 : sommes de la table : attendu 3.24 à 4.74 h, pire 8.56 à 11.56 h
borne de la minuterie : 11,56 h = 41616 s ; HMAX à ANT0 = 3,6 USD et 1,30 USD de l'heure : 41815 s (≥ 41 616 : True) ; à ANT0 = 3,7 : 41538 s
blocs bash : 8, bash -n sans erreur ; extraits Python : 10, ast.parse sans erreur
§ 4.3 : choix de l'offre essayé sur trois cas factices (EPYC d'abord ; sans EPYC, la moins chère ; aucune offre) : conforme
écrit : docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6.md (92d9aebee0634c910ef622a80e4ff2cd33c91df6014ab6a4f04885c0023d2fca)
TOUT PASSE
```

## Sorties (empreintes ; compagnons `.sha256` écrits par `controle_ia.scellement sceller`)

- `brouillons/T0.7-sondes-v0-v1-candidat2.md` : `9de13f6a9a40267ff8111a009643a4871eb9e0f91ae23ba89182d3abbc9a3335` (3 309 lignes) ;
- `brouillons/T0.7-sondes-v0-v1-candidat2-pieces/T0.7-sondes-v0-v1-candidat2-couples-v1.json` : `beb5ecfb210978a188a749b6c4420757a0106a523d72189e146971f09f39daea` (60 couples, 17 gelés) ;
- `brouillons/T0.7-sondes-v0-v1-candidat2-pieces/T0.7-sondes-v0-v1-candidat2-faire-v1.py` : `42f3ad126c881c8bfe11b0b1d8b68075e37e58cabc4b4dc845cd144baa6cb129` ;
- `brouillons/T0.7-sondes-v0-v1-candidat2-pieces/puissance_regle_a_t07_v1.py` : `4523a480f8560089f5c34e63b0e29ac65d90689ed8ffc87f1aab584916447146` ; sortie `puissance-regle-a-t07-v1.txt` : `af73498e757d4ab33e2804a30b375a815340d6fa9b63d34f3bec8682630a83dd` ;
- `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6.md` : `92d9aebee0634c910ef622a80e4ff2cd33c91df6014ab6a4f04885c0023d2fca` (610 lignes) ;
- `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6-appliquer-v1.py` : `7c06e185d9c5bb58c0c82a1740d2dd509d807c0c7bfe829575f27cdb147a1c54` ;
- ce journal (compagnon écrit en dernier).
- Non versés (bac à sable) : générateur des couples `…/scratchpad/agents/t07-candidat2/gen/gen_couples_c2.py` (`d305d832e622f126c60b372abf8779d54736586dc16649749881c532440a97b8`) ; outil de contexte `…/outils/ctx.py` ; copie de `src/` au commit `0d0c5da4` ; racines factices d'essai.

## Points ouverts (pour la mère)

1. **Script de l'instance** : le v2 (`e68d3306…`) appelle `lecture_v2` (l. 302, 357, 367, 372) et refuse la configuration v7 ; les commandes `lecture_v4` et l'export de `CUBLAS_WORKSPACE_CONFIG` demandés par la consigne exigent un **script v3** (ordre, brouillon 6, § 13, S-12 ; marqueur `SHA_SCRIPT_V3_T07`). Écart déclaré à « tout le reste égal » : nécessaire au mandat.
2. **C7 dans l'ordre** : la règle « `src/` de C7 égal à `37485ce5` » (§ 1, P9, § 4.1) tombe avec le code neuf ; remplacée par `SRC7` (marqueur `COMMIT_SRC_CONTRE_LU_T07`, à fixer par la mère). Écart déclaré, même motif.
3. **ATT** (`346 passed, 2 skipped, 4 xfailed`) : texte inchangé ; le code neuf change les arbres de S7 : P12 imposera la remesure (§ 11 bis).
4. **Taille des sorties** (§ 5 bis) : à 800 directions, total estimé ≈ 1,85·10⁹ octets sous la borne de 2·10⁹ (marge ≈ 0,15·10⁹) ; la formule ne compte pas `planchers-figees-t07.npz` ni les 2 × 200 directions de P3 (S-13).
5. **Puissance** : « rejeu du code » lu comme le rejeu de la règle (a) sur les données de P3 (audit) ; si la mère entendait autre chose, la section « Puissance » (non gelée) se refait sans toucher l'empan gelé.
6. **Portée de R-2285** : les couples G2-06 à G2-08 (« non au-dessus », « contraire », intervalle corrigé) suivent la définition ; G2-13 (D rapportée), G2-14, G2-15 (cause « échec » du repli), G2-01 (réplication) et G2-17 (repli, contrôle en ligne) suivent le nombre de directions et le plancher neuf (R-2298, R-2304) ; G2-01, G2-02, G2-16 joignent les réserves de P3 (R-2299). Aucun ne change une hypothèse, une prédiction, un signe, un niveau, une ligne L ni la grille. À juger par la vérification courte.
7. **Ordre, brouillon 6, non contre-lu** : le candidat 2 cite son empreinte (`EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07`) ; un brouillon 7 changerait une cellule de la section « Module » (non gelée).
8. Observation de code (sans effet sur le texte, conservatrice) : dans `lecture_v4.noter`, un écart du contrôle en ligne sur les 200 directions de P3 notées en descriptif met la sonde figée entière en « échec » (même bloc `try`) ; écrit tel quel dans la liste d'arrêt.

## Interdits tenus

- Jamais ouverts : aucun `lecture-sondes-t06.json`, aucun `diag/` ni `runs/` de 7a, ni `essai/t06-explo-v3`, ni la lecture B ou sa branche, ni `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, ni l'étiqueteur, ni `scripts/extraire_mesures_epreuve_t06_v1.py`. **Aucune valeur de sonde de 7a vue ni écrite.**
- Règle 9 : aucune recherche récursive ; `grep` sur des fichiers nommés seulement ; `git ls-tree` limité à `src` du commit `0d0c5da4` et à `registres/code-t07/` ; aucun `verifier-arbre`.
- Secrets, appels, dépense : aucune valeur de clé lue ; ni `env`, ni `printenv`, ni `set`, ni `export -p` ; aucun appel de modèle ni d'interface externe ; aucun `vastai` ; aucune dépense.
- Git : lecture seule (`status --short`, `log`, `show <commit>:<chemin>`, `ls-tree`, `cat-file`, `merge-base --is-ancestor`, `rev-parse`) ; aucun commit, aucun changement de l'index ou de la branche.
- Écritures dans le dépôt : sous `brouillons/` (candidat 2 et ses pièces) et `docs/procedures/` (ordre, brouillon 6, et son script) seulement, noms neufs ; candidat 1 et brouillon 5 intacts (vérifiés par `sha256sum -c`).
- Essais : aucune suite lancée ; scripts joués d'abord sur des racines factices du bac à sable.
- Refus : aucun refus de permission ni de classifieur.
- 2026-11-11T03:19:00Z — journal clos ; scellé ensuite.
