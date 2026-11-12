# Coût réel par résultat — v2

Une ligne par run décisif (manifeste `decisif` vrai) et par GO de type calcul. Le montant est la somme des montants des lignes du registre des dépenses qui citent le run, son instance (registre des arrêts) ou le GO, hors engagements ; une ligne à plusieurs montants n'est pas tranchée (cellule vide, montants listés). La dernière colonne cite les lignes du registre des arrêts qui nomment le run ou le GO (négatifs, R4). Le total strict de la phase 0 est dans `total-depenses-v2.md`.

Jour du script (`date -u`) : 2026-11-05. Version : `registres-taif-v2`. Toute cellule vide est une cellule sans source ; aucune valeur n'est estimée. Sources de chaque cellule : `sources-v2.json`.

| run ou GO | type | date | instance | GO / plafond | montant (USD, registre des dépenses) | montants lus (lignes) | résultat produit (verdict) | verdicts | USD par verdict | préenregistrement | arrêts et interruptions (registre des arrêts) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 20261004-080257-t03 | run décisif | 2026-10-04 |  |  |  |  |  | 0 |  | `prereg/T0.3-simulation-lemme-theoreme-v1.md` |  |
| 20261005-102042-validation-reelle | run décisif | 2026-10-05 | 54298522 | GO-2026-10-04-08 | 0,24 | l. 9 : 1,093, 0,027 | `docs/verdicts/verdict-T0.4-critere-1-G0-v1.md` ; `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` | 2 | 0,12 | `prereg/T0.4-validation-modele-reel-v1.md` | 2026-10-05 10:31 : fin de l'amorce à 10:29:17 UTC, code 1 : run A `20261005-102042-validation-reelle` arrêté en phase de logique par la garde d'équivalence (4 actions au-dessus de 1e-4 à la couche 23… |
| 20261005-144628-validation-reelle | run décisif | 2026-10-05 | 54332340 |  |  | l. 38 : 0,80, 0,6, 1,85 | `docs/verdicts/verdict-T0.4-critere-1-G0-v2.md` ; `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` | 2 |  | `prereg/T0.4-validation-modele-reel-v2.md` | 2026-10-05 14:55 : fin de l'amorce à 14:52:58 UTC, code 1 : run A `20261005-144628-validation-reelle` arrêté en phase de production par la garde d'équivalence (28 actions au-dessus de 0,1) ; logique,… |
| 20261006-114025-validation-reelle | run décisif | 2026-10-06 | 54476244 |  | 2,67 | l. 42 : 2,67 | `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` | 1 | 2,67 | `prereg/T0.4-validation-modele-reel-v3.md` | 2026-10-06 12:11 : fin de l'amorce à 12:07:54 UTC, code 0 : runs A `20261006-114025-validation-reelle` et B `20261006-115440-validation-reelle` complets, branche `calcul/t04-validation-v3` poussée pu… |
| 20261006-115440-validation-reelle | run décisif | 2026-10-06 | 54476244 |  | 2,67 | l. 42 : 2,67 | `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` | 1 | 2,67 | `prereg/T0.4-validation-modele-reel-v3.md` | 2026-10-06 12:11 : fin de l'amorce à 12:07:54 UTC, code 0 : runs A `20261006-114025-validation-reelle` et B `20261006-115440-validation-reelle` complets, branche `calcul/t04-validation-v3` poussée pu… |
| 20261011-225701-t05-revalidation-reel | run décisif | 2026-10-11 | 55458787 |  | 1,14 | l. 52 : 1,14 | `docs/verdicts/verdict-T0.5-revalidation-v2.md` | 1 | 1,14 | `prereg/T0.5-revalidation-equivalence-pilote-v2.md` | 2026-10-11 23:49 : fin de l'amorce à 23:44:12 UTC, **code 0** : tests « 670 passed in 491.38s », run `20261011-225701-t05-revalidation-reel` de 22:57:01 à 23:44 UTC ; puis redémarrages de l'amorce pa… |
| 20261012-105125-t05-pilote-reel | run décisif | 2026-10-12 | 55538944 |  | 4,89 | l. 64 : — (engagement) ; l. 65 : 4,89 | `docs/verdicts/audit-R4-T0.5-pilote-notations-v1.md` ; `docs/verdicts/verdict-T0.5-pilote-notations-v1.md` ; `docs/verdicts/verdict-T0.5-pilote-v1.md` | 3 | 1,63 | `prereg/T0.5-pilote-8B-v1.md` | 2026-10-12 15:04 : fin de l'amorce à 15:02:55 UTC, **code 1** : « ARRÊT : limite de durée dépassée pendant les notations » ; « ARRÊT pendant run (code 1) : résultats partiels committés (dont arret.js… |
| 20261012-150724-t05-pilote-analyse | run décisif | 2026-10-12 |  |  |  |  | `docs/verdicts/audit-R4-T0.5-pilote-notations-v1.md` ; `docs/verdicts/audit-R4-T0.5-pilote-v1.md` ; `docs/verdicts/verdict-T0.5-pilote-notations-v1.md` ; `docs/verdicts/verdict-T0.5-pilote-v1.md` | 4 |  | `prereg/T0.5-pilote-8B-v1.md` |  |
| 20261017-193648-t05-notations-reel | run décisif | 2026-10-17 | 56438435 | GO-2026-10-12-02 |  | l. 85 : 8,70 (engagement) ; l. 86 : 5,3, 8,23 | `docs/verdicts/audit-R4-T0.5-pilote-notations-v1.md` ; `docs/verdicts/verdict-T0.5-pilote-notations-v1.md` | 2 |  | `prereg/T0.5-pilote-notations-v1.md` | ¦ 2026-10-18 21:36 ¦ instance 56438435 (notations refaites, P2), `vastai stop instance 56438435` à 21:36:57 UTC, par son identifiant (R10) ; motif : run `20261017-193648-t05-notations-reel` fini et p… |
| 20261018-214028-t05-lecture-juges | run décisif | 2026-10-18 |  |  |  |  | `docs/verdicts/audit-R4-T0.5-pilote-notations-v1.md` ; `docs/verdicts/verdict-T0.5-pilote-notations-v1.md` | 2 |  | `prereg/T0.5-pilote-notations-v1.md` |  |
| 20261019-230011-p3-reel | run décisif | 2026-10-19 |  |  |  |  | `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` ; `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` | 2 |  | `prereg/P3-premier-test-i-a-v1.md` |  |
| 20261020-075740-p3-lecture | run décisif | 2026-10-20 |  |  |  |  | `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` ; `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` | 2 |  | `prereg/P3-premier-test-i-a-v1.md` |  |
| 20261029-102459-rejeu-juges-v2-reel | run décisif | 2026-10-29 |  |  |  |  |  | 0 |  | `docs/notes/couche-2-preparation-v1/rejeu-juges-v2/fiche-lancement-rejeu-juges-v2.md` |  |
| 20261101-160323-regles-defense-convergence | run décisif | 2026-11-01 |  |  |  |  |  | 0 |  | `prereg/preregistrement-regles-defense-convergence-v1.md` |  |
| GO-2026-10-04-08 | GO calcul | 2026-10-04 |  | 150 USD (alerte à 120 USD) | 2,96 | 4 ligne(s) sommée(s), 3 non tranchée(s), 13 engagement(s) | `docs/verdicts/verdict-T0.5-pilote-notations-v1.md` ; `docs/verdicts/verdict-T0.5-pilote-v1.md` ; `docs/verdicts/verdict-T0.5-revalidation-v2.md` | 3 | 0,99 |  |  |
| GO-2026-10-06-02 | GO calcul | 2026-10-06 |  | dans le plafond de GO-2026-10-04-08 (150 USD) |  | 0 ligne(s) sommée(s), 1 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-17-01 | GO calcul | 2026-10-17 |  | 4 heures de carte (≈ 6 USD), dans les 150 USD de GO-2026-10-04-08 |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-20-06 | GO calcul | 2026-10-20 |  | 150 USD, plafond de GO-2026-10-04-08 inchangé |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-20-07 | GO calcul | 2026-10-20 |  | 10 USD par lancement, dans les 150 USD de GO-2026-10-04-08 prolongé (GO-2026-10… |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-20-11 | GO calcul | 2026-10-20 |  | dans les 150 USD de la phase |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-24-05 | GO calcul | 2026-10-24 |  | dans la ligne de R-355 (sans plafond fixé par Lazar) ; moins de 1 USD par course | 11,32 | 1 ligne(s) sommée(s), 2 non tranchée(s), 3 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-24-06 | GO calcul | 2026-10-24 |  | 25 USD (`--plafond-usd 25`, tenu par le script avant chaque appel) | 1,01 | 1 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-24-07 | GO calcul | 2026-10-24 |  | 40 USD imputés à cette ligne | 49,26 | 22 ligne(s) sommée(s), 1 non tranchée(s), 28 engagement(s) |  | 0 |  |  | 2026-10-24 23:03 : sonde finie (« SONDE fin » à 23:01:12 UTC, journal lu) ; session « session-depot » |
| GO-2026-10-25-01 | GO calcul | 2026-10-25 |  | 120 USD au plus pour les deux courses | 30,22 | 3 ligne(s) sommée(s), 0 non tranchée(s), 2 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-25-02 | GO calcul | 2026-10-25 |  | 185 USD au plus pour l'ensemble du GO, inchangé (pilote 3 : 30,23 USD dépensés… | 92,43 | 7 ligne(s) sommée(s), 2 non tranchée(s), 2 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-25-03 | GO calcul | 2026-10-25 |  | 10 USD au plus (fixé par « session-depot », aucun montant donné par Lazar) | 0,23 | 2 ligne(s) sommée(s), 0 non tranchée(s), 2 engagement(s) |  | 0 |  |  | 2026-10-26 00:41 UTC — instance Vast.ai 57742711 (test H-M1 v3, GO-2026-10-25-03) : arrêtée par son identifiant par la surveillance à 00:40:42 UTC (motif « conteneur sorti »), puis détruite par son i… |
| GO-2026-10-26-01 | GO calcul | 2026-10-26 |  | 10 USD |  | 0 ligne(s) sommée(s), 1 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-26-02 | GO calcul | 2026-10-26 |  | 10 USD | 4,37 | 1 ligne(s) sommée(s), 1 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-26-03 | GO calcul | 2026-10-26 |  | 75 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-26-04 | GO calcul | 2026-10-26 |  | sans plafond (mot de Lazar, R-512) | 2,93 | 3 ligne(s) sommée(s), 1 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-26-05 | GO calcul | 2026-10-26 |  | 75 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-26-06 | GO calcul | 2026-10-26 |  | 25 USD | 0,00 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-26-07 | GO calcul | 2026-10-26 |  | 23 USD | 0,00 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-26-08 | GO calcul | 2026-10-26 |  | 2 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-27-01 | GO calcul | 2026-10-27 |  | 35 USD | 0,00 | 3 ligne(s) sommée(s), 1 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-27-02 | GO calcul | 2026-10-27 |  | 35 USD | 0,00 | 1 ligne(s) sommée(s), 1 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-27-03 | GO calcul | 2026-10-27 |  | 8 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-27-04 | GO calcul | 2026-10-27 |  | 24 USD |  | 0 ligne(s) sommée(s), 1 non tranchée(s), 0 engagement(s) |  | 0 |  |  | 2026-10-27 14:32 UTC — instance Vast.ai 57969803 (comparaison d'échelle 8B contre 70B, GO-2026-10-27-04, texte v10) : le calcul a fini en code 0 à 14:30:10 UTC (petit poussé `54bd5ff`, grand poussé `… |
| GO-2026-10-27-05 | GO calcul | 2026-10-27 |  | 30 USD | 6,24 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-27-06 | GO calcul | 2026-10-27 |  | 22 USD | 12,50 | 2 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-27-07 | GO calcul | 2026-10-27 |  | 25 USD | 3,45 | 2 ligne(s) sommée(s), 0 non tranchée(s), 4 engagement(s) |  | 0 |  |  | 2026-10-27 15:18 UTC — instance Vast.ai 57977351 (couche 1 bis (b), GO-2026-10-27-07, créée 15:13:17 UTC, machine 142924, Tchéquie) : le conteneur s'est arrêté vers 15:16 UTC après la seule ligne « A… ; 2026-10-27 19:53 UTC — instance Vast.ai 57978233 (couche 1 bis (b), banque T0.5 complète, GO-2026-10-27-07) : amorce finie à 19:52:55 UTC, code 1 (échéance de 15 000 s pendant les notations descripti… ; 2026-10-27 22:58 UTC — instance Vast.ai **58007778** (couche 1 bis (a), notations complémentaires `e2`, GO-2026-10-27-07) : amorce finie à 22:56:31 UTC, code 0 (2 runs sur 2, aucun échec) ; résultats… |
| GO-2026-10-27-08 | GO calcul | 2026-10-27 |  | devis de chaque proposition |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-27-09 | GO calcul | 2026-10-27 |  | 22 USD | 2,84 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-27-10 | GO calcul | 2026-10-27 |  | 15 USD | 5,89 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-27-11 | GO calcul | 2026-10-27 |  | 15 USD | 10,83 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-27-12 | GO calcul | 2026-10-27 |  | 30 USD | 5,74 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-27-13 | GO calcul | 2026-10-27 |  | aucun fixé par Lazar (règle des 100 USD ci-contre) |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-28-01 | GO calcul | 2026-10-28 |  | 100 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-28-02 | GO calcul | 2026-10-28 |  | 90 USD au plus (remplace les 50 USD de la première ligne) |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-28-03 | GO calcul | 2026-10-28 |  | 28/22/33 USD par tour (garde 83 USD ; pire cas devis 62,29 ; réel attendu ~27-3… | 20,31 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-28-06 | GO calcul | 2026-10-28 |  | 90 USD, plafond de GO-2026-10-28-02 inchangé |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-28-08 | GO calcul | 2026-10-28 |  | 30 USD | 3,19 | 1 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-28-09 | GO calcul | 2026-10-28 |  | 5 USD | 1,29 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-28-11 | GO calcul | 2026-10-28 |  | 6 USD |  | 0 ligne(s) sommée(s), 1 non tranchée(s), 1 engagement(s) |  | 0 |  |  | 2026-10-29 00:21:59 UTC — instance **58162997** (régénération des sondes de P3, GO-2026-10-28-11) détruite par son identifiant (`vastai destroy instance 58162997 -y`, R10), après le versement lu ; l'… |
| GO-2026-10-28-12 | GO calcul | 2026-10-28 |  | 5 USD | 1,83 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-28-14 | GO calcul | 2026-10-28 |  | 60 USD | 0,00 | 1 ligne(s) sommée(s), 1 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-28-15 | GO calcul | 2026-10-28 |  | 30 USD | 12,59 | 1 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-28-16 | GO calcul | 2026-10-28 |  | 4 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 2 engagement(s) |  | 0 |  |  | 2026-10-29 03:21:40 UTC — instance **58178416** (rejeu des juges, GO-2026-10-28-16) détruite par son identifiant (`vastai destroy instance 58178416 -y`, R10), après le versement (fin de l'amorce 03:1… |
| GO-2026-10-28-17 | GO calcul | 2026-10-28 |  | 30 USD | 11,06 | 1 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-01 | GO calcul | 2026-10-29 |  | 30 USD |  | 0 ligne(s) sommée(s), 2 non tranchée(s), 2 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-02 | GO calcul | 2026-10-29 |  | 30 USD |  | 0 ligne(s) sommée(s), 2 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-03 | GO calcul | 2026-10-29 |  | 124 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-04 | GO calcul | 2026-10-29 |  | 4 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-05 | GO calcul | 2026-10-29 |  | 13 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-06 | GO calcul | 2026-10-29 |  | 25 USD | 14,30 | 1 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-07 | GO calcul | 2026-10-29 |  | 15 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-08 | GO calcul | 2026-10-29 |  | 50 USD (Claude) ; enveloppe 60 |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-09 | GO calcul | 2026-10-29 |  | 63 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-10 | GO calcul | 2026-10-29 |  | 11,8 USD (le total des deux runs reste ≤ 15 USD : 3,19 + 11,8) |  | 0 ligne(s) sommée(s), 1 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-11 | GO calcul | 2026-10-29 |  | sans plafond fixé par Lazar (prudentiel 300 USD) |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-12 | GO calcul | 2026-10-29 |  | 5 USD | 2,79 | 1 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  | 2026-10-29 12:40:27 UTC — instance **58233254** (rejeu des juges v2, GO-2026-10-29-12) **détruite** par son identifiant (`vastai destroy instance 58233254 -y`, R10) ; état relu « exited » avant destr… |
| GO-2026-10-29-13 | GO calcul | 2026-10-29 |  | 78 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-14 | GO calcul | 2026-10-29 |  | 6 USD | 0,82 | 1 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-15 | GO calcul | 2026-10-29 |  | 30 USD | 16,28 | 2 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-16 | GO calcul | 2026-10-29 |  | 2 USD | 1,15 | 1 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-17 | GO calcul | 2026-10-29 |  | 6 USD | 0,81 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-18 | GO calcul | 2026-10-29 |  | 12 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-19 | GO calcul | 2026-10-29 |  | sans plafond fixé par Lazar (prudentiel 300 USD) |  | 0 ligne(s) sommée(s), 1 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-29-20 | GO calcul | 2026-10-29 |  | 28 USD |  | 0 ligne(s) sommée(s), 1 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-01 | GO calcul | 2026-10-30 |  | sans plafond fixé par Lazar (prudentiel 300 USD) |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-02 | GO calcul | 2026-10-30 |  | sans plafond fixé par Lazar (prudentiel 300 USD) |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-03 | GO calcul | 2026-10-30 |  | 52,8 USD |  | 0 ligne(s) sommée(s), 1 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-04 | GO calcul | 2026-10-30 |  | 60 USD (Claude) |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-05 | GO calcul | 2026-10-30 |  | 20 USD (Claude) + 4 USD (Argon) |  | 0 ligne(s) sommée(s), 1 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-06 | GO calcul | 2026-10-30 |  | 0,5 USD | 0,00 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-07 | GO calcul | 2026-10-30 |  | 110 USD (pré-pilote 32) |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-08 | GO calcul | 2026-10-30 |  | 5 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-09 | GO calcul | 2026-10-30 |  | 11 USD (Opus et Argon 8 ; Kimi 3) |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 2 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-10 | GO calcul | 2026-10-30 |  | 0 USD (abonnement de la session, comme GO-2026-10-29-18) |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-11 | GO calcul | 2026-10-30 |  | 28 USD | 2,32 | 2 ligne(s) sommée(s), 1 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-12 | GO calcul | 2026-10-30 |  | 12 USD | 8,01 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-13 | GO calcul | 2026-10-30 |  | 25 USD (≈ 12 par tour) |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-14 | GO calcul | 2026-10-30 |  | 3 USD | 0,61 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-15 | GO calcul | 2026-10-30 |  | 12 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-16 | GO calcul | 2026-10-30 |  | 12 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-30-17 | GO calcul | 2026-10-30 |  | 60 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-31-01 | GO calcul | 2026-10-31 |  | 20 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-31-02 | GO calcul | 2026-10-31 |  | 25 USD (≈ 12 par tour) | 16,63 | 2 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-31-03 | GO calcul | 2026-10-31 |  | 50 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-31-04 | GO calcul | 2026-10-31 |  | 160 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-31-05 | GO calcul | 2026-10-31 |  | 210 USD | 26,81 | 2 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-31-06 | GO calcul | 2026-10-31 |  | 45 USD | 18,60 | 2 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-31-07 | GO calcul | 2026-10-31 |  | 12 USD (tour comparable à faits courts : 8,2 à 8,4 USD) | 4,30 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-31-08 | GO calcul | 2026-10-31 |  | 25 USD | 5,98 | 5 ligne(s) sommée(s), 0 non tranchée(s), 2 engagement(s) |  | 0 |  |  |  |
| GO-2026-10-31-09 | GO calcul | 2026-10-31 |  | 45 USD (inchangé, GO-06) |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-01-01 | GO calcul | 2026-11-01 |  | 30 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 2 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-01-02 | GO calcul | 2026-11-01 |  | 61 USD (GO-06 porté de 45 à 61 ; cumul avant tour 2 : 30,23) | 3,83 | 1 ligne(s) sommée(s), 0 non tranchée(s), 2 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-01-03 | GO calcul | 2026-11-01 |  | 30 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-01-04 | GO calcul | 2026-11-01 |  | 3 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-01-05 | GO calcul | 2026-11-01 |  | 40 USD | 0,00 | 1 ligne(s) sommée(s), 1 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-01-06 | GO calcul | 2026-11-01 |  | 45 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-01-07 | GO calcul | 2026-11-01 |  | 40 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-01-08 | GO calcul | 2026-11-01 |  | 40 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-01-09 | GO calcul | 2026-11-01 |  | 5 USD | 1,34 | 1 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-01-10 | GO calcul | 2026-11-01 |  | 5 USD | 0,35 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-01-11 | GO calcul | 2026-11-01 |  | 45 USD | 17,30 | 1 ligne(s) sommée(s), 1 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-01-12 | GO calcul | 2026-11-01 |  | 10 USD |  | 0 ligne(s) sommée(s), 2 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-01-13 | GO calcul | 2026-11-01 |  | 25 USD |  | 0 ligne(s) sommée(s), 1 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-02 | GO calcul | 2026-11-02 |  | 25 USD (inchangé) | 1,79 | 1 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  | 2026-11-02 18:13 UTC : fin de l'amorce à 18:12:14 UTC, code 0 ; poussée vérifiée (`calcul/r1-resolution-graine-v1` à `ab808842`) ; deux relances de l'amorce par le redémarrage du conteneur, refusées… |
| GO-2026-11-02-03 | GO calcul | 2026-11-02 |  | 6 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-04 | GO calcul | 2026-11-02 |  | 30 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-07 | GO calcul | 2026-11-02 |  | 80 USD | 40,00 | 1 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-11 | GO calcul | 2026-11-02 |  | 15 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-12 | GO calcul | 2026-11-02 |  | 10 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-14 | GO calcul | 2026-11-02 |  | 6,2 USD pour le rejeu à graine (au lieu de ≈ 1,4) ; enveloppe commune de GO-202… | 1,79 | 1 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-17 | GO calcul | 2026-11-02 |  | 191 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-19 | GO calcul | 2026-11-02 |  | 15 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-21 | GO calcul | 2026-11-02 |  | 400 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 2 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-22 | GO calcul | 2026-11-02 |  | 200 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-23 | GO calcul | 2026-11-02 |  | 50 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-24 | GO calcul | 2026-11-02 |  | 60 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-25 | GO calcul | 2026-11-02 |  | 150 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-26 | GO calcul | 2026-11-02 |  | 15 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-27 | GO calcul | 2026-11-02 |  | 60 USD | 0,54 | 1 ligne(s) sommée(s), 0 non tranchée(s), 1 engagement(s) |  | 0 |  |  | 2026-11-03 06:38 UTC : fin de l'amorce à 06:36:59 UTC, code 0 (« étapes rejeu passées, arrêtées : aucune ») ; poussée vérifiée (`calcul/r1-relance-v3-reel-v1` à `5768a9fc`) ; le conteneur a redémarré… |
| GO-2026-11-02-28 | GO calcul | 2026-11-02 |  | 200 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-29 | GO calcul | 2026-11-02 |  | 80 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-30 | GO calcul | 2026-11-02 |  | 40 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-31 | GO calcul | 2026-11-02 |  | 40 USD | 41,68 | 2 ligne(s) sommée(s), 2 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-02-32 | GO calcul | 2026-11-02 |  | 60 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-01 | GO calcul | 2026-11-03 |  | 400 USD | 48,50 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-02 | GO calcul | 2026-11-03 |  | 244 USD | 10,03 | 1 ligne(s) sommée(s), 1 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-03 | GO calcul | 2026-11-03 |  | 60 USD | 52,33 | 4 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  | 2026-11-05 ≈ 02:24 UTC — **59175807** (R1 v4, session 2, GO-2026-11-03-03) détruite **par son identifiant** (`vastai destroy instance 59175807 -y`) par la tâche planifiée (i) de la fille (`cse_01Qi7G… |
| GO-2026-11-03-04 | GO calcul | 2026-11-03 |  | 35 USD | 0,85 | 1 ligne(s) sommée(s), 1 non tranchée(s), 1 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-05 | GO calcul | 2026-11-03 |  | 245 USD | 10,84 | 1 ligne(s) sommée(s), 0 non tranchée(s), 2 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-06 | GO calcul | 2026-11-03 |  | 35 USD | 0,01 | 1 ligne(s) sommée(s), 1 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-07 | GO calcul | 2026-11-03 |  | 35 USD | 4,99 | 2 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-08 | GO calcul | 2026-11-03 |  | 35 USD | 2,81 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-09 | GO calcul | 2026-11-03 |  | 198 USD | 7,98 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-10 | GO calcul | 2026-11-03 |  | 237 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-11 | GO calcul | 2026-11-03 |  | 198 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-12 | GO calcul | 2026-11-03 |  | 198 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-13 | GO calcul | 2026-11-03 |  | 237 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-14 | GO calcul | 2026-11-03 |  | 198 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-15 | GO calcul | 2026-11-03 |  | 198 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-16 | GO calcul | 2026-11-03 |  | 237 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-17 | GO calcul | 2026-11-03 |  | 130 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-03-18 | GO calcul | 2026-11-03 |  | 198 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-04-01 | GO calcul | 2026-11-04 |  | 3 USD | 0,26 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-04-02 | GO calcul | 2026-11-04 |  | 35 USD | 8,40 | 1 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-04-03 | GO calcul | 2026-11-04 |  | 30 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-04-04 | GO calcul | 2026-11-04 |  | 40 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 2 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-04-06 | GO calcul | 2026-11-04 |  | 400 USD |  | 0 ligne(s) sommée(s), 1 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-04-09 | GO calcul | 2026-11-04 |  | 35 USD |  | 0 ligne(s) sommée(s), 0 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-05-01 | GO calcul | 2026-11-05 |  | 1 USD |  | 0 ligne(s) sommée(s), 4 non tranchée(s), 0 engagement(s) |  | 0 |  |  | 2026-11-05 ≈ 01:30:25 UTC — **59184557** (sonde v9 d'A1-v3, GO-2026-11-05-01) détruite par sa propre minuterie (DELETE par son identifiant), absente dès 01:31:24Z, sans geste du pilote. ; 2026-11-05 ≈ 03:22:47 UTC — **59195718** (sonde v10 d'A1-v3, GO-2026-11-05-01) détruite par sa propre minuterie (DELETE par son identifiant), absente dès 03:28:10Z (code 0), sans geste du pilote. |
| GO-2026-11-05-02 | GO calcul | 2026-11-05 |  | 5 USD | 0,01 | 1 ligne(s) sommée(s), 0 non tranchée(s), 2 engagement(s) |  | 0 |  |  | 2026-11-05 06:35:18 UTC — instance Vast **59219396** (tir réel SPARKS v9, GO-2026-11-05-02) détruite **par son identifiant** avec `-y` par la fille, après le verdict « boucle » du lanceur v9 ; invent… |
| GO-2026-11-05-03 | GO calcul | 2026-11-05 |  | 35 USD |  | 0 ligne(s) sommée(s), 1 non tranchée(s), 0 engagement(s) |  | 0 |  |  |  |
| GO-2026-11-05-05 | GO calcul | 2026-11-05 |  | 5 USD |  | 0 ligne(s) sommée(s), 3 non tranchée(s), 3 engagement(s) |  | 0 |  |  | 2026-11-05 ≈ 07:28:45–07:31:03 UTC — instance Vast **59227134** (second tir SPARKS v10, GO-2026-11-05-05) **détruite par elle-même** (amorce v10 : refus avant l'ordre consommé → destruction par son i… ; 2026-11-05 08:06:14 UTC — instance Vast **59231131** (troisième tir SPARKS v11, GO-2026-11-05-05) détruite **par son identifiant** par la fille, sur le verdict « boucle » imprimé par le lanceur v11 (… ; 2026-11-05 ≈ 08:23:20–08:24:21 UTC — instance Vast **59232437** (quatrième tir SPARKS v11, GO-2026-11-05-05) **détruite par elle-même** (amorce v11 : ordre « fin » consommé, attente de 180 s, destruc… |
| (sans GO) l. 34 | dépense sans GO (signalée) | 2026-10-05 | 54311651 |  | 0,16 | 0,16 |  |  |  |  |  |
| (sans GO) l. 38 | dépense sans GO (signalée) | 2026-10-05 | 54332340 |  |  | 0,80, 0,6, 2,4, 1,85 |  |  |  |  |  |
| (sans GO) l. 42 | dépense sans GO (signalée) | 2026-10-06 | 54476244 |  | 2,67 | 2,67, 5,1 |  |  |  |  |  |
| (sans GO) l. 48 | dépense sans GO (signalée) | 2026-10-10 | 55292763 |  | 0,26 | 0,26, 1,1867, 39,9 |  |  |  |  |  |
| (sans GO) l. 52 | dépense sans GO (signalée) | 2026-10-11 | 55458787 |  | 1,14 | 1,14, 1,08, 41,1 |  |  |  |  |  |
| (sans GO) l. 65 | dépense sans GO (signalée) | 2026-10-12 | 55538944, 55555587 |  | 4,89 | 4,89, 1,0889, 46,0, 8,47, 3,98 |  |  |  |  |  |
| (sans GO) l. 86 | dépense sans GO (signalée) | 2026-10-18 | 56438435 |  |  | 5,3, 1,0933, 18,12, 9,89, 8,23, 8,23, 8,70, 63,2, 0,025 |  |  |  |  |  |
| (sans GO) l. 88 | dépense sans GO (signalée) | 2026-10-20 | 56799469, 56811393 |  | 3,96 | 3,96, 1,0889, 0,022, 8,46, 5,31 |  |  |  |  |  |
| (sans GO) l. 90 | dépense sans GO (signalée) | 2026-10-20 | 56799469, 56811393, 56823529, 56847109, 56847848, 56858177, 56878873, 56879233 |  | 5,59 | 5,59, 11,79, 65,00, 4,71, 63,1 |  |  |  |  |  |
| (sans GO) l. 92 | dépense sans GO (signalée) | 2026-10-24 | 56799469, 57412762, 57432434 |  |  | 6,01, 468, 500, 6,42, 7,27 |  |  |  |  |  |
| (sans GO) l. 152 | dépense sans GO (signalée) | 2026-10-26 |  |  | 0,62 | 0,62 |  |  |  |  |  |
| (sans GO) l. 157 | dépense sans GO (signalée) | 2026-10-26 |  |  | 3,52 | 3,52, 5,39 |  |  |  |  |  |
| (sans GO) l. 158 | dépense sans GO (signalée) | 2026-10-26 |  |  |  | 2,34, 3,62, 10,05 |  |  |  |  |  |
| (sans GO) l. 159 | dépense sans GO (signalée) | 2026-10-26 |  |  | 0,59 | 0,59 |  |  |  |  |  |
| (sans GO) l. 162 | dépense sans GO (signalée) | 2026-10-26 |  |  | 0,48 | 0,48 |  |  |  |  |  |
| (sans GO) l. 163 | dépense sans GO (signalée) | 2026-10-26 |  |  | 6,33 | 6,33 |  |  |  |  |  |
| (sans GO) l. 164 | dépense sans GO (signalée) | 2026-10-26 |  |  | 5,39 | 5,39 |  |  |  |  |  |
| (sans GO) l. 166 | dépense sans GO (signalée) | 2026-10-26 |  |  | 6,32 | 6,32 |  |  |  |  |  |
| (sans GO) l. 167 | dépense sans GO (signalée) | 2026-10-26 |  |  | 7,69 | 7,69 |  |  |  |  |  |
| (sans GO) l. 168 | dépense sans GO (signalée) | 2026-10-26 |  |  | 7,07 | 7,07 |  |  |  |  |  |
| (sans GO) l. 264 | dépense sans GO (signalée) | 2026-10-31 |  |  | 0,99 | 0,99 |  |  |  |  |  |
| (sans GO) l. 267 | dépense sans GO (signalée) | 2026-10-31 |  |  | 9,02 | 9,02, 1,3 |  |  |  |  |  |
| (sans GO) l. 314 | dépense sans GO (signalée) | 2026-11-02 |  |  |  | 1,089, 4,3, 1,009, 1,0, 29,18 |  |  |  |  |  |

Lignes : 190 ; cellules vides : 1049 sur 2280.
