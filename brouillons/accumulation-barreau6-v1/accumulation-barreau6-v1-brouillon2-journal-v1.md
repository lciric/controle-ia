# Journal — barreau 6, brouillon 2 — v1 — **ARRÊT sur la simulation sous le nul**

Rédacteur du brouillon 1 (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, relancé par la mère (message portant ses décisions R-2261). Même consigne (`f86a6834ccf0d0f8b53d3821c2a52495c711837e07563633059170a4765da7c2`) et mêmes interdits ; aucun commit, aucun appel de modèle, aucune dépense ; brouillon 1 intact (`a2d8186340fc3cd6f9fc16ab46ca81e741ce75361e43e9e34b899061a2f60c2f`, compagnon vérifié). Heures relevées par `date -u`.

## 0. Issue

La mère a écrit : « si l'erreur dépasse le niveau annoncé, arrête-toi et écris-le ». **Elle le dépasse** (§ 5). **Le brouillon 2 n'est donc pas écrit dans le dépôt.** Ce qui est versé : les couples (prêts, vérifiés), le script qui les applique (essayé sur une copie du bac à sable), la simulation sous le nul, un diagnostic de deux remèdes, ce journal. Le brouillon 2 **candidat** existe dans le bac à sable seulement : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/barreau6/essai-faire/accumulation-barreau6-v1-brouillon2.md`, `5dddc118a76e2fc15bc5a073376089179549d77863cbc2de33f4aecd82421893` (sortie du script versé sur une copie : « TOUT PASSE »). Le script versé le refait à l'identique dans le dossier du brouillon dès que la mère a tranché, après l'ajout éventuel des couples du remède.

## 1. Heures

| heure (UTC) | fait |
|---|---|
| 16:28:35 | rapport de contre-lecture 1 vérifié (`c13cbdde18a29122f7ff17c56432280ad5d24452e9c576dc7b2faffc2b5b4fb1`, égal à son compagnon) ; brouillon 1 vérifié ; lecture du rapport |
| 16:29:40 | exploration du nul (bac à sable) : Δ de population selon la densité q, pour trois structures et trois décalages |
| 16:29:56 | entropie de la simulation sous le nul tirée une fois (`secrets.randbits(128)`) |
| 16:30 | script `nul_accumulation_b6_v1.py` écrit ; essai rapide (40 répliques) dans le bac à sable |
| 16:31:16 à 16:34:51 | simulation sous le nul, code 0 (214,9 s) |
| 16:32 à 16:34 | 28 couples de la contre-lecture extraits du rapport par programme, appliqués au brouillon 1 en mémoire : 0 faute, empreinte intermédiaire `e903c91c504442248ac7e4539b8bae58c988614b9434d9c7fa66c7af9da81b6c` ; couples B2 et options (b), (c) écrits ; script d'application écrit |
| 16:35:31 | entropie du diagnostic tirée une fois |
| 16:36:21 | sorties de la simulation sous le nul scellées |
| 16:36 à 16:38:35 | fichier de couples construit ; script d'application essayé sur une copie du bac à sable (« TOUT PASSE ») ; table des phrases vérifiée (§ 4) ; diagnostic, code 0 (153,7 s) |
| 16:38:57 | couples, script d'application et diagnostic scellés |

## 2. Lectures

Le rapport de contre-lecture 1, entier ; le message de la mère (R-2261). **Pas ouverts** : le verdict de `agregation-r1-v4-v1` (`docs/verdicts/verdict-agregation-r1-v4-v1.md`), aucune de ses sorties, les lignes R-1643, R-1644, R-1662 et R-2257 de `registres/decisions.md` ; les faits que porte le couple 6 viennent du rapport seul. Rien de 7a, rien de 7b, aucun fichier de P3-bis, aucun `diag/`, `runs/`, `donnees/`.

## 3. Couples (versés, prêts, non appliqués dans le dépôt)

- Fichier `accumulation-barreau6-v1-brouillon2-couples-v1.json` (`dc74735850eeff50392e28dcb7c55b0693bf4e170aed211dc15dab08dc96f8de`) : `couples` = **CL1-01 à CL1-28**, extraits du rapport par programme (blocs « ancien » et « nouveau » recopiés à l'octet), dans l'ordre, puis **B2-01 à B2-13** du rédacteur ; `options_N_B6_3` = couples prêts pour les options (b) et (c) de N-B6-3, **non appliqués**.
- Décisions de la mère (R-2261) tenues : couples 6 à 28 tels qu'écrits (CLA-02 déclarée sans aucun chiffre ; B6-D3b gardée, descriptive) ; couples 1 à 5 tels qu'écrits, sous l'option (a) « forme faible, nommée », marqueur `DECISION_N_B6_3` ; N-B6-1 et N-B6-2 inchangés (marqueurs) ; énumération des phrases demandée au script d'énumération (B2-08, B2-09).
- Couples B2 : B2-01 titre ; B2-02 date ; B2-03 statut (dont « B2-12 et B2-13 portent l'issue de la simulation sous le nul, en marqueurs jusqu'à la décision de la mère ») ; B2-04 documents qui font foi (rapport de contre-lecture, simulation sous le nul) ; B2-05 « Ce que les auteurs savaient » (lectures du brouillon 2, non-lectures déclarées) ; B2-06 avis du contre-lecteur sur N-B6-2 ajouté à l'inconvénient de (a) ; B2-07 N-B6-3 : texte rédigé sous (a), couples (b) et (c) au journal ; B2-08, B2-09 énumération des phrases (CLA-03) ; B2-10 section « Contre-lecture » : entrée « Contre-lecture 1 » (brouillon relu `a2d81863…`, rapport `c13cbdde…`) et traitement de CLA-01 à CLA-12 (tous acceptés) ; B2-11 ligne des marqueurs de contre-lecture retirée (remplis) ; **B2-12 et B2-13 : issue de la simulation sous le nul, écrite en marqueurs `ISSUE_NUL_ACCB6` et `ISSUE_NUL_ACCB6_DETAIL`** (le texte ne peut pas être scellé avant leur remplissage).
- **Options (b) et (c) de N-B6-3** (couples prêts, vérifiés applicables au brouillon 2 candidat) : (b) section 0, point 7 → « par décision de Lazar (N-B6-3, option (b)), le barreau 6 de l'échelle est redéfini par ce texte […] ; une version neuve du rapport des prémisses le dit ; G1 garde ses propres critères » et préfixe des phrases → « « Barreau 6 » s'écrit tel quel » ; (c) point 7 → « les phrases gelées n'emploient pas le mot « barreau » : elles disent « mesure interne d'accumulation » […] ; le barreau 6 de l'échelle reste « non atteint avant G1 » » et préfixe → « Mesure interne d'accumulation (somme contre maximum, aire d'épisode) ». Texte exact : fichier de couples, `options_N_B6_3`.
- Script `accumulation-barreau6-v1-brouillon2-faire-v1.py` (`09967c3862f97f23c8a33c972c58c9ce0c128dbbbeb598d8d34fea9594ebed7e`) : exige l'empreinte du brouillon 1 et celle du rapport, applique CL1-01 à CL1-28 (chaque « ancien » une fois exactement), compare l'empreinte intermédiaire à `e903c91c…`, applique les B2, vérifie l'applicabilité des options (b) et (c) sans les appliquer, n'écrase jamais un brouillon 2 différent. Essai sur une copie (bac à sable `…/essai-faire/`) : « 28 couples de la contre-lecture appliqués ; empreinte intermédiaire e903c91c… (égale à l'attendue) ; 13 couples du rédacteur appliqués ; option b : 2 couples applicables ; option c : 2 couples applicables ; TOUT PASSE ; brouillon 2 : 5dddc118… ». `controle_ia.prereg.problemes` sur le candidat : une seule ligne, les marqueurs restants (`COMMIT_CODE_ACCB6`, `DECISION_N_B6_1`, `DECISION_N_B6_2`, `DECISION_N_B6_3`, `ENTROPIE_ACCB6`, `ENUMERATION_ETATS_ACCB6`, `ISSUE_NUL_ACCB6`, `ISSUE_NUL_ACCB6_DETAIL`, `REVERIFICATION_T07_SCELLE`).
- Constructeur du fichier de couples : bac à sable, `…/b2/construire_couples.py` (`e1aefaf98bf513618b04bea9f4966214655dd558e8dd19a383a6646e1c7076e0`), non versé.

## 4. Table des phrases (CLA-03), vérifiée sur le candidat

Essai du rédacteur (ce n'est pas l'énumération exigée par `ENUMERATION_ETATS_ACCB6`) : bac à sable `…/verifier_table_phrases_b2.py` (`193ec6864734dfd6902a2be5f21262cab1506343b1e277bb08740df591b5b1c0`), sortie `3965ad3a8e8919b0948b5865a0e0306e6495534dd281fdaa9ac37c653dba2d20` : 4 aiguillages × 9 états de (i) × 9 états de `S100` = 324 cas, **0 cas sans ligne**, une première ligne par cas (G-1, G-2, G-3 : 81 chacun ; `S100` A : 9 ; `S100` M : 9 ; `S100` ni A ni M et (i) A : 7 ; et (i) M : 7 ; ni l'un ni l'autre : 49) ; **chaque état de jeu autre que A et M a sa phrase** dans la dernière ligne (« partagé » compris).

## 5. Simulation sous le nul — le niveau annoncé est dépassé

- Script `nul_accumulation_b6_v1.py` (`c7e93bd8f76862a027b8b876ca3ab1ea28f6f39b3f459c570e40c7d315863e58`) ; sorties `nul-accumulation-b6-v1.txt` (`512108e384c2a751bec01e7c17fd1480f993d9774cb12c1bc15d2a7f7020c369`) et `nul-accumulation-b6-v1.json` (`3e88033b19b1a237dcf44080a61969b82096e7b18e08775787d50fbef44a292e`). Lancement : `cd <bac à sable> && .venv/bin/python -I -B <script> <script de puissance> <sortie .json> > <sortie .txt>`, quatre processus, code 0, 214,9 s. Il importe le script de puissance versé (`ccc5310b…`, empreinte vérifiée) : **mêmes lois supposées, mêmes intervalles (percentiles, 2 000 tirages par blocs de tâches), mêmes planchers, même règle des états** ; aucune donnée lue.
- Cellules : 64 et 36 tâches ; structures s0, s1, s2 ; nul « pur » (aucun signal) et nul « signal présent » (décalage 1 ou 2 sur une part q* des actions, q* choisi pour que Δ de population soit nul : aires d'épisode de population 0,57 à 0,94 pour la somme et pour le maximum) ; 2 000 répliques par cellule ; Δ moyen des répliques entre −0,0015 et +0,0019 (nul tenu).
- Niveau annoncé (couple 22 de la contre-lecture) : par sonde et par côté 0,00625 à k = 4 (famille : « accumuler bat » ≤ 0,025 ; « accumuler bat » ou « le maximum bat » ≤ 0,05).
- **Résultats** :
  - **nul pur** : P(A) = P(M) = 0 dans toutes les cellules (presque toujours « sous le plancher » : la condition de plancher protège) ;
  - **nul, signal présent** : P(A) par sonde jusqu'à **0,0090** (64 tâches, s1, décalage 1 ; intervalle de Clopper-Pearson à 95 % [0,0053 ; 0,0142]) et **0,0105** (36 tâches, s0, décalage 2 ; [0,0065 ; 0,0160]) ; P(M) jusqu'à **0,0105** (64 tâches, s0, décalage 2 ; [0,0065 ; 0,0160]) et **0,0125** (36 tâches ; [0,0081 ; 0,0184]) ; bornes de famille (k × taux) : « accumuler bat » jusqu'à **0,036** (64) et **0,042** (36) au lieu de 0,025 ; A ou M jusqu'à **0,070** (64) et **0,092** (36) au lieu de 0,05 ;
  - **dépassement établi** (borne basse de Clopper-Pearson au-dessus du nominal par sonde) : 64 tâches, s0, décalage 2, k = 4 et k = 3 (côté M) ; 36 tâches, s0, décalage 2, k = 4, 3 et 2 (côté A à k = 4, côté M partout) ; ailleurs, plusieurs estimations ponctuelles au-dessus du nominal sans dépassement établi.
- Lecture : l'intervalle percentile, à 64 ou 36 blocs et 2 000 tirages, est **anti-conservateur** dans la queue de 0,625 % ; le dépassement atteint ≈ 1,7 à 2 fois le nominal par sonde, surtout quand le signal est fort (aires d'épisode ≈ 0,94, près de la saturation) et du côté « le maximum bat ». Sous ces lois **supposées** ; sur 7b, rien n'est connu.

## 6. Diagnostic de deux remèdes (sans effet sur le texte ; pour la décision)

Script `diagnostic_nul_b6_v1.py` (`6e501cad6d4da82041682c1cbc7dbad141a4eaa0184eb1438a1a81ddf6f6edfe`), sorties `diagnostic-nul-b6-v1.txt` (`dcf8abd5499864a24a0adcc063610e8dbe494754182c832e9c31c87837bf0f0c`) et `diagnostic-nul-b6-v1.json` (`bd358c526193e4f33a5bae787dc54407ccbe5790b85b1ef4acfceaefbf54469c`) ; code 0, 153,7 s ; les quatre cellules les plus défavorables, 2 000 répliques chacune, k = 4, taux visé 0,00625 :

| remède | P(A) par sonde | P(M) par sonde | famille A ; A ou M |
|---|---|---|---|
| (v1) 10 000 tirages, niveau 98,75 % | 0,0050 à 0,0060 | 0,0055 à **0,0130** (signal fort : borne basse 0,0085 et 0,0081, au-dessus) | 0,020 à 0,024 ; 0,044 à **0,074** |
| (v2) 2 000 tirages, niveau 99,375 % (1 − 0,05/(2k)) | 0,0040 à 0,0045 | 0,0035 à **0,0100** (36 tâches, signal fort ; borne basse 0,0061) | 0,016 à 0,018 ; 0,030 à **0,058** |

Ce que cela dit : plus de tirages ramènent « accumuler bat » dans son niveau ; « le maximum bat » reste au-dessus près de la saturation ; un niveau resserré ramène A sous le nominal et M près de lui, au prix de la puissance (non recalculée). **Non essayé** : les deux ensemble ; une autre méthode d'intervalle (rééchantillonnage studentisé ou corrigé).

## 7. Ce qui est à trancher (session mère ; ne touche ni H1, ni G1, ni le mode tenu à l'écart : seuil de ce texte avant scellement)

- (a) **10 000 tirages et niveau resserré 1 − 0,05/(2k)** pour les deux côtés, puis nouvelle simulation sous le nul et de puissance avant scellement (scripts à nom neuf). Avantage : taux mesurés attendus dans le niveau. Inconvénient : puissance plus faible, déjà faible ; le niveau s'écarte de celui de T0.7 (déclaré).
- (b) **10 000 tirages, niveau inchangé**, et réserve gelée sur toute issue « le maximum bat » : « taux d'erreur mesuré jusqu'à environ deux fois le nominal près de la saturation, sous lois supposées ». Avantage : puissance gardée pour « accumuler bat ». Inconvénient : la réfutation lue reste anti-conservatrice.
- (c) **Garder** et écrire les taux mesurés à la place du niveau nominal. Avantage : rien ne change. Inconvénient : le texte annonce un niveau qu'il ne tient pas.
- **Recommandation du rédacteur : (a)**, confiance ≈ 0,6. Dans tous les cas, B2-12 et B2-13 (marqueurs `ISSUE_NUL_ACCB6`, `ISSUE_NUL_ACCB6_DETAIL`) écrivent les taux mesurés, et le brouillon 2 (ou 3) est produit par le script versé, complété des couples du remède.
- **Point d'attention, hors de ce texte (R4, symétrie)** : T0.7 lit ses décisives avec le même intervalle percentile (2 000 tirages, 98,75 %, 64 blocs de tâches), sur une autre statistique (aire contre quantile du plancher) ; rien ici ne mesure son taux réel ; à signaler, sans conclusion.

## 8. Fichiers versés (sous `brouillons/accumulation-barreau6-v1/`, chacun avec compagnon `.sha256`)

| fichier | sha256 |
|---|---|
| `accumulation-barreau6-v1-brouillon2-couples-v1.json` | `dc74735850eeff50392e28dcb7c55b0693bf4e170aed211dc15dab08dc96f8de` |
| `accumulation-barreau6-v1-brouillon2-faire-v1.py` | `09967c3862f97f23c8a33c972c58c9ce0c128dbbbeb598d8d34fea9594ebed7e` |
| `nul_accumulation_b6_v1.py` | `c7e93bd8f76862a027b8b876ca3ab1ea28f6f39b3f459c570e40c7d315863e58` |
| `nul-accumulation-b6-v1.txt` | `512108e384c2a751bec01e7c17fd1480f993d9774cb12c1bc15d2a7f7020c369` |
| `nul-accumulation-b6-v1.json` | `3e88033b19b1a237dcf44080a61969b82096e7b18e08775787d50fbef44a292e` |
| `diagnostic_nul_b6_v1.py` | `6e501cad6d4da82041682c1cbc7dbad141a4eaa0184eb1438a1a81ddf6f6edfe` |
| `diagnostic-nul-b6-v1.txt` | `dcf8abd5499864a24a0adcc063610e8dbe494754182c832e9c31c87837bf0f0c` |
| `diagnostic-nul-b6-v1.json` | `bd358c526193e4f33a5bae787dc54407ccbe5790b85b1ef4acfceaefbf54469c` |
| ce journal | compagnon écrit au scellement |

Brouillon 1, son journal, la simulation de puissance et l'essai des clés : inchangés (compagnons revérifiés).
