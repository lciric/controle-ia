# Journal — barreau 6, candidat 4 — v1

Rédacteur neuf (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-accb6-candidat4-v1.md`, `a54e39cb01f2c7fd629b97d9dbd61e9dc8878565d0bec6b282a371ebaabdbf29`, vérifiée par `sha256sum -c` de son compagnon (dans son dossier) avant lecture ; interdits communs v2 recopiés dedans (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`), tenus. Je n'ai écrit ni le barreau 6 (brouillons, candidats 1 à 3), ni son code, ni ses contre-lectures, ni sa revérification, ni T0.7, ni aucun texte nommé dans l'en-tête du candidat. **J'ai lu T0.7 scellé (sections citées au § 1) : exclu ensuite de tout rôle de lecteur de P3-bis.** Aucun commit, aucun appel de modèle, aucune dépense, aucune instance. Heures relevées par `date -u` (début 11:52:15 UTC, le 2026-11-11). Candidats 1 à 3 intacts ; le candidat 3 est relu par empreinte après l'écriture du candidat 4.

## 1. Entrées et vérifications (11:52 à 12:08 UTC)

Empreintes vérifiées par `sha256sum` et `sha256sum -c` du compagnon, toutes égales à celles de la consigne :

| pièce | chemin | sha256 |
|---|---|---|
| consigne | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-accb6-candidat4-v1.md` | `a54e39cb01f2c7fd629b97d9dbd61e9dc8878565d0bec6b282a371ebaabdbf29` |
| interdits communs v2 | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` | `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` |
| candidat 3 (base) | `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat3.md` | `d48fb8a36c960e85416dfe42b2a9d77824067333b543a9f16540766e02ff1dfb` |
| ses couples, script, journal | `…/accumulation-barreau6-v1-candidat3-couples-v1.json`, `…-faire-v1.py`, `…-journal-v1.md` | `2057a5a9…`, `89d227c1…`, `e5fb0d0c…` |
| vérification courte du candidat 2 | `prereg/contre-lectures/accumulation-barreau6-v1-candidat2-verification-courte-v1.md` (§ 6 et § 7 lus) | `d35055ff1ac72264e94a6a83228f49963d4e7b227a7d7853733b281989f2d5dd` |
| revérification sur T0.7 scellé | `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/reverification-t07-scelle-v1.md` | `80f06ac4f65cf798b2a25f1d2e4c56a2a21e570feb6cc307efdb2f229ecf9644` |
| couples proposés RV-01 à RV-11 | `…/reverification-t07-scelle-v1-pieces/couples-proposes-v1.json` | `771abfaff6a09bea103d67fa2f5521f69690c3795494fe99a815c0e71f15def7` |
| contre-lecture du code | `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/contre-lecture-code-accb6-v1.md` | `67614af4c82f35f98698ccf2768a259da4ca67e3c7d641e1c8a8dad63516df3c` |
| rapport du développeur, code v2 | `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/rapport-developpeur-accb6-v2.md` | `72642740c15546c8424c58f0b24566c692fa9121941c1cad697a2bfd505c96f9` |
| T0.7 scellé | `prereg/T0.7-sondes-v0-v1.md` | `d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5` |
| configuration v8 de T0.7 | `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json` | `e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328` |
| fichier de la ligne `CODE-T07` | `registres/code-t07/CODE-T07-v2.json` (commit `b4cd9953d199dd8f220f5162e5868c5b00fd392d`, 26 fichiers) | `d5eb0b665df187d158fa84deff733b0f382fc309510163625f7aaea1ae9a692c` |
| note d'erratum de T0.7 scellé | `docs/notes/g0-deux-semaines-v1/t07-module-v2/erratum-concordance-adaptateur-t07-scelle-v1.md` | `f593676248698b985f842f30f403e0036b1faa556335d1b1bcb7ed7a08080aea` |

Lus aussi : `registres/scellements-v1.md` (six lignes ; `CODE-T07` 2026-11-11T05:40:34Z, `SCELLEMENT-T07` 2026-11-11T07:11:42Z) ; `registres/decisions.md`, lignes R-2272 à R-2281, R-2321, R-2330, R-2336 (lignes 2230 à 2239, 2279, 2288, 2294 du fichier), entières ; dans T0.7 scellé, « Métrique » (l. 1186-1255 : `n_plancher` = 800, plancher neuf des deux sondes figées, 200 directions de P3 en descriptif), « Seuil » (l. 1256-1313 : règle (a), borne basse de D = aire − quantile 0,95 du plancher) et la ligne de « Liste d'arrêt » qui nomme « plancher neuf de la sonde figée non établi » (l. 1985).

Par `git show <commit>:<chemin>` (aucun `checkout`) :
- **commit `282e295ec8e825b9c045bd30ebfdac3cbe55496f`** (branche `prep/accumulation-b6-code-v2`, parent `6c98ea20…`) : paquet `src/controle_ia/accumulation_b6/` — `__init__.py` `eb43e52b…`, `code_accb6_v1.py` `2e6c3bb8…`, `etats_v1.py` `81e4a19bb68b75dcfd7c93a06be5c546e111d91b7aab779bd5bb700378ecd284`, `garde_v1.py` `5b91bfaa…`, `lecture_v1.py` `1f4c035f50587f8c81c628b4e8274f477959588d8faa08343f51c0e394bf48df`, `phrases_v1.py` `961ea2b3…` (égaux au rapport v2, § 1) ; `scripts/enumeration_etats_accb6_v2.py` `a6dbfdd8…` ; `scripts/enumeration-etats-accb6-v2-code-v2.txt` `6b078d6c82c8bcc0dbbbb72b67c75731168d957c4aaf82ef3c54878db6f68fde` (2 152 lignes ; bilan « cas sans état : 0 (couples 1152, jeux 343, séquence 33) ; cas sans phrase : 0 (phrases 604) ; écarts : 0 ») contre `scripts/enumeration-etats-accb6-v2.txt` `00088af5…` : **seule la ligne 3 diffère** (empreinte d'`etats_v1.py`, `diff` des deux sorties) ; `tests/test_accb6_relance_v1.py` `cc458330…` (inchangé) ; essai `test_enumeration_du_code_v2_egale_a_celle_du_code_v1_hors_empreinte_de_etats_v1` présent (`tests/test_accb6_etats_v1.py`, l. 250) ; `accumulation_b6/lecture_v1.py` : commande (l. 757-779 : phrase gelée sur la sortie standard, « REFUS » et « ARRÊT » sur la sortie d'erreur ; une exception imprévue sort par le code 1), `lire_sondes_t07` (l. 126-170 : champ `echec` de `index.sondes[]`), docstring (l. 19 : lignes de `mention` et des conditions retirées ôtées dès le chargement), exclusions (l. 464), réserves du plancher neuf (l. 648-682 ; `e4.get("reserves")`, l. 671) ;
- modules hors du paquet visés par CCB-7, **égaux entre `6c98ea20`, `282e295e` et C7** : `sondes/evaluation.py` `1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3`, `sondes/temoins.py` `3b051b6fc2d78eeb4a44aab8a385bbce65095998e944b80e5f2a66e21b57faf7`, `manifeste.py` `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d`, `scellement.py` `93beeb1c…`, `gardes.py` `a83c48ce…` ; `git diff --stat 6c98ea20 282e295e -- src` : deux fichiers, ceux du paquet ;
- **commit C7 `b4cd9953…`** : les sept fichiers cités à la l. 23 du candidat 3 (`registre_v1.py` `e5023657…`, `lecture_v2.py` `709b2feb…`, `lecture_v1.py` `62b34790…`, `criteres_v1.py` `12b999fe…`, `plancher_v1.py` `ac6e8263…`, `sondes/evaluation.py` `1040674c…`, `sondes/temoins.py` `3b051b6f…`) **égaux** à C7 et à `282e295e` ; `t07/lecture_v4.py` : `noter` (l. 202 ; l. 214 = filtre `jetons_notes` > 0, renvoi de RV-08) et `etape_b` (l. 568 ; l. 669-688 = dictionnaire de la lecture, qui porte les treize noms de E4, renvoi de RV-07).
- Script de puissance du brouillon 1 (`brouillons/accumulation-barreau6-v1/puissance_accumulation_b6_v1.py`) : fonctions `plancher` (l. 103-110) et `lire_jeu` (l. 113-140) : Δ ne dépend que des scores de la sonde ; le nombre de directions n'entre que dans la condition « au-dessus » (états P, A, M).

## 2. Le mandat, point par point

1. **RV-01 à RV-11, tels qu'écrits, sous l'option (a) de l'écart E-2** (R-2330). Le script les recopie du fichier de la revérification et compare chacun à l'octet (contrôle 1). Option (a) : RV-01 garde la règle d'intervalle contre quantile et la **déclare distincte** de T0.7 scellé (différence appariée) ; la **réserve écrite** que ce membre est « plus facile à obtenir que son homonyme de T0.7 » est **C4-16** (G4-14), paragraphe placé dans « Critères de lecture gelés » juste avant l'audit de symétrie, au texte seulement : ni le code ni la table des phrases ne l'écrivent (le code v2 n'a pas touché `phrases_v1.py` ; la revérification n'a pas proposé de réserve neuve au code ; question Q-2) ; « le niveau des conclusions tient à l'intervalle de Δ » : RV-01, C4-16 et la section « Puissance », point 11 (C4-19) ; « à dire à Lazar » (R-2330) : pas 6 de « Reste » (C4-28).
2. **Commit du code** : `282e295ec8e825b9c045bd30ebfdac3cbe55496f` écrit à l'en-tête (C4-06, l. 7 ; C4-08, l. 20 ; C4-09, l. 23), dans la section « Code » (C4-20 à C4-23 : commit, branche, parent, deux fichiers changés et leurs empreintes, 195 essais, 128 mutations sur 128, CCB-1 levé, énumération : sortie neuve `6b078d6c…`, seule la ligne 3 diffère, aucune règle d'état ni phrase changée) et dans « Reste », pas 2 (C4-27). Le plan (points 2 et 6) et la table « Lignes de registre » nomment `CODE-ACCB6` **sans citer d'empreinte de commit** : rien n'y change (le commit est porté par le fichier de la ligne). Les citations de `6c98ea20` gardées à dessein (histoire, parent, lectures, état au candidat 3, contre-lecture au commit `6c98ea20`) sont listées par le script (lignes 6, 7, 20, 40, 214, 217, 261, 262 du candidat 4).
3. **CCB-2 à CCB-7** (R-2281) : phrases recommandées par la contre-lecture, écrites là où le texte règle la chose :

| point | lieu | couple | G4 | ce qui est écrit |
|---|---|---|---|---|
| CCB-2 | Plan, point 2 (codes) | C4-14 | G4-10 | une sortie hors des codes 0, 2 et 3 (exception qui n'est pas une `GardeArret`, après le manifeste, sans `arret-accb6.json`) n'est pas un arrêt : relance permise, déclarée |
| CCB-3 | Critères, audit de symétrie | C4-17 | G4-15 | « toutes deux égales à 1 exactement » (égalité exacte, comme le code ; une aire de 1 − 1/4096 s'écrit 1,000 et ne déclenche pas) |
| CCB-4 | Plan, point 7 | C4-15 | G4-13 | la commande écrit la phrase gelée sur sa sortie standard : lancée sortie standard détournée ; la sortie d'erreur reste lue |
| CCB-5 | Plan, point 1 (déclaré) | C4-12 | G4-08 | chargement `.npz` entier, lignes de `mention`, des conditions retirées et de (ii) sous G-2 ôtées dès le chargement ; champ `echec` de E2b lu ; et, déclaré du même mouvement, `resultat.reserves` de E4 lu depuis l'écart E-3 (sans être exigé) |
| CCB-6 | Seuil, état E | C4-11 | G4-05 | tension déclarée : la cause « score ou direction non fini sur une action gardée » n'est atteinte que par le seuil des 10 % |
| CCB-7 | Plan, point 2 ; Liste d'arrêt | C4-13 ; C4-18 | G4-09 ; G4-17 | au lancement, `sondes/evaluation.py`, `sondes/temoins.py`, `manifeste.py` comparés par empreinte au commit cité (valeurs au commit `282e295e`) ; écrit avant le lancement ; un écart : aucun lancement, nœud |

   CCB-8 (observation, « rien à faire ») et CCB-9 (cosmétique, en-têtes du code) sont hors du mandat : non traités.
4. **Marqueur `REVERIFICATION_T07_SCELLE`** : rempli par C4-07 (l. 11, « Documents qui font foi ») : T0.7 scellé (chemin, empreinte, ligne `SCELLEMENT-T07`), configuration v8, fichier et commit de `CODE-T07`, note d'erratum ; revérification (chemin, empreinte, vérificateur, R-2330), verdict « écarts », E-1 à E-5 nommés, traitement (code v2 `282e295e` pour E-1 et E-3 ; RV-01 à RV-05 et RV-10 pour E-1 ; option (a) par RV-01 et C4-16 pour E-2 ; RV-09 pour E-3 ; RV-06 à RV-08 pour E-4 ; RV-11 pour E-5). Renvois au brouillon 22 : l. 3 (auteur des candidats 1 à 3, histoire ; C4-02 ajoute l'auteur du candidat 4), l. 11 (devenue l'entrée de T0.7 scellé ; le brouillon 22 y reste cité, non scellé, pour l'histoire), l. 23 (C4-09 : empreintes égales à C7), l. 79 (RV-01 : origine de la règle de plancher) ; tous les autres renvois du texte à T0.7 portent sur des fichiers, champs, clés et sections que la table du § 1 de la revérification donne « égaux » à T0.7 scellé et à C7, ou sont traités par un couple RV. Les « écarts E-1 à E-5 » sont distingués, dans le texte, des entrées E1 à E4 et de l'état E.
5. **Puissance** : RV-10 (intro de la section) et C4-19 (point 11, neuf). **800 ne change pas** le Δ moyen des cellules (Δ ne dépend que des scores de la sonde ; seule l'erreur de Monte-Carlo bougerait, le flux de tirages changeant) ni la borne du taux d'erreur de A et de M sous le nul (intervalle de Δ seul ; le plancher ne fait que restreindre) ; le nombre de directions n'entre que dans la condition « au-dessus de son plancher » (états P, A, M) : à 800, le quantile 0,95 des directions vise la même valeur avec moins de bruit d'échantillonnage ; les probabilités d'état ne peuvent bouger que là où cette condition mord (a = 0,55 sous s1 et s2 ; « plancher haut » ; doses de faible aire de la séquence ; nul aux aires basses) ; **réserve écrite « non resimulé à 800 »** (question Q-5).
6. **Sections gelées** : dix-sept couples, G4-01 à G4-17, listés exactement au § 4 (section, ancien, nouveau, motif). Vérifié par programme (script, contrôles 2 à 7) : défaire les 39 couples redonne le candidat 3 à l'octet ; les couples hors sections gelées laissent les sept sections gelées égales à l'octet, ceux en sections gelées ne touchent rien d'autre ; mêmes titres ; **mots sensibles supprimés en sections gelées : « 200 » × 6 (→ « 800 », écart E-1, R-2330) et « 1,000 » × 1 (→ « 1 exactement », CCB-3, R-2281), rien d'autre** (liste blanche ; tout autre chiffre, signe de comparaison ou « strictement » supprimé arrête le script, nœud ; éprouvé par artefact). **Aucun signe, seuil, niveau ni règle d'état ne change** : règles 2 à 7 des couples, règles (0) à (8) des jeux, « Niveau », « Multiplicité », « Erreur de première espèce », table des phrases gelées : intactes ; la règle 1 (E) ne reçoit que deux déclarations (RV-06, C4-11) ; seule grandeur gelée changée : le nombre de directions de plancher (200 → 800), décidé par R-2330. Procédures et gardes précisées sans toucher un état : CCB-2 (relance permise après une sortie hors codes), CCB-4 (sortie standard détournée), CCB-7 (vérification au lancement ; un écart : aucun lancement, nœud). Aucun nœud au sens du point 6 de la consigne.
7. **`controle_ia.prereg.problemes`** sur le candidat 4 : `[]` (dans le script, puis lancé seul : `PYTHONPATH=src .venv/bin/python -c "…problemes(…candidat4.md)"` → `[]`) ; aucun marqueur `<<…>>`.

## 3. Les 39 couples (ordre du texte)

Texte exact de chaque couple : `accumulation-barreau6-v1-candidat4-couples-v1.json` (même dossier). RV-01 à RV-11 : recopiés tels qu'écrits du fichier de la revérification (contrôle 1 du script).

| couple | G4 | section (réelle) | lieu | motif |
|---|---|---|---|---|
| C4-01 | — | titre | titre | candidat 4 (consigne a54e39cb…) |
| C4-02 | — | en-tête, auteur | auteur | rédacteur neuf du candidat 4, qui a lu T0.7 scellé (consigne a54e39cb…) |
| C4-03 | — | en-tête, date | date | heure du candidat 4 (date -u : 11:52:15 UTC) |
| C4-04 | — | en-tête, statut | statut | candidat 4 = candidat 3 + RV-01 à RV-11 + C4-01 à C4-28 ; sections gelées déclarées |
| C4-05 | — | en-tête, statut | statut, fin | marqueur rempli ; pas restants |
| C4-06 | — | en-tête, commit du code d'analyse | commit du code | COMMIT_CODE_ACCB6 = 282e295e (R-2336) ; E-5 (R-2330) |
| C4-07 | — | en-tête, documents qui font foi | documents, T0.7 | marqueur REVERIFICATION_T07_SCELLE rempli ; renvois au brouillon 22 devenus renvois à T0.7 scellé (R-2321, R-2330) |
| C4-08 | — | en-tête, documents qui font foi | documents, candidat 4 | documents lus au candidat 4 (R-2281, R-2336) |
| C4-09 | — | en-tête, documents qui font foi | documents, code lu | empreintes égales à C7 et à 282e295e (R-2330 ; git show) |
| C4-10 | — | Ce que les auteurs savaient avant le scellement | ce que les auteurs savaient | lectures du candidat 4 |
| RV-02 | G4-01 | Prédiction (gelée), B6-D5 | Prédiction (gelée), B6-D5 | écart E-1 ; R-2330 |
| RV-01 | G4-02 | Métrique (gelée) | Métrique (gelée) | écart E-1, E-2 ; R-2330 |
| RV-03 | G4-03 | Métrique (gelée) | Métrique (gelée) | écart E-1 ; R-2330 |
| RV-06 | G4-04 | Seuil (gelée), état E | Seuil (gelée), état E | écart E-4 (précision) ; R-2330 |
| C4-11 | G4-05 | Seuil | CCB-6 | CCB-6 (R-2281) : tension interne déclarée ; aucun état changé |
| RV-04 | G4-06 | Plan d'analyse (gelée), point 1, E1 | Plan d'analyse (gelée), point 1, E1 | écart E-1 ; R-2330 |
| RV-07 | G4-07 | Plan d'analyse (gelée), point 1, E4 | Plan d'analyse (gelée), point 1, E4 | écart renvoi ; R-2330 |
| C4-12 | G4-08 | Plan d'analyse | CCB-5 | CCB-5 (R-2281) ; champ reserves de E4 lu depuis l'écart E-3 (R-2330, R-2336) ; déclaré |
| C4-13 | G4-09 | Plan d'analyse | CCB-7, plan | CCB-7 (R-2281) : vérification au lancement ; un écart : aucun lancement, nœud |
| C4-14 | G4-10 | Plan d'analyse | CCB-2 | CCB-2 (R-2281) : phrase recommandée ; relance permise, déclarée |
| RV-08 | G4-11 | Plan d'analyse (gelée), point 4 | Plan d'analyse (gelée), point 4 | écart renvoi ; R-2330 |
| RV-09 | G4-12 | Plan d'analyse (gelée), point 5 | Plan d'analyse (gelée), point 5 | écart E-3 ; R-2330 |
| C4-15 | G4-13 | Plan d'analyse | CCB-4 | CCB-4 (R-2281) : sortie standard de la commande détournée |
| C4-16 | G4-14 | Critères de lecture gelés | E-2, option (a) | R-2330, option (a) de l'écart E-2 : réserve écrite (plus facile à obtenir que son homonyme de T0.7) ; aucun état changé |
| C4-17 | G4-15 | Critères de lecture gelés | CCB-3 | CCB-3 (R-2281) : « exactement 1 », comme le code ; aucun état n'en dépend |
| RV-05 | G4-16 | Liste d'arrêt (gelée) | Liste d'arrêt (gelée) | écart E-1 ; R-2330 |
| C4-18 | G4-17 | Liste d'arrêt | CCB-7, liste d'arrêt | CCB-7 (R-2281) : arrêt au lancement, en face du plan, point 2 |
| RV-10 | — | Puissance | Puissance | écart E-1 (déclaration) ; R-2330 |
| C4-19 | — | Puissance | puissance, 800 | consigne, point 5 : ce que 800 directions changent ; réserve « non resimulé à 800 » |
| C4-20 | — | Code | code, état | code v2 : commit, fichiers changés, 195 essais, 128 mutations, CCB-1 levé (R-2336) |
| C4-21 | — | Code | code, fusion | écart E-5 (R-2330) : la même formule qu'au pas 4 de « Reste » |
| C4-22 | — | Code | code, énumération, sorties | énumération : sortie neuve au commit 282e295e (R-2336) |
| C4-23 | — | Code | code, énumération, commit | énumération : seule la ligne 3 diffère ; aucune règle d'état ni phrase changée |
| C4-24 | — | Reste avant le scellement | reste, vérification | plus aucun marqueur |
| C4-25 | — | Reste avant le scellement | reste, table | marqueur rempli (R-2330) |
| C4-26 | — | Reste avant le scellement | reste, pas 1 | contre-lecture du code faite (R-2281) ; reste la contre-lecture courte (R-2336) |
| C4-27 | — | Reste avant le scellement | reste, pas 2 | COMMIT_CODE_ACCB6 = 282e295e (R-2336) ; écart E-5 (R-2330) |
| RV-11 | — | Reste avant le scellement, pas 4 | Reste avant le scellement, pas 4 | écart E-5 ; R-2330 |
| C4-28 | — | Reste avant le scellement | reste, pas 5 et 6 | vérification courte du différentiel (R-2280) ; mot à Lazar (R-2330) |

## 4. Changements en sections gelées, G4-01 à G4-17 (exacts, tirés du fichier de couples)

### G4-01 — RV-02 — Prédiction (gelée), B6-D5

- **Motif** : écart E-1 ; R-2330
- **Ancien** (candidat 3) :

~~~text
contre la distribution des Δ des 200 directions du plancher.
~~~

- **Nouveau** (candidat 4) :

~~~text
contre la distribution des Δ des 800 directions du plancher.
~~~

### G4-02 — RV-01 — Métrique (gelée)

- **Motif** : écart E-1, E-2 ; R-2330
- **Ancien** (candidat 3) :

~~~text
pour chacune des 200 directions de `plancher_<k>` (scores par action des directions aléatoires appariées que T0.7 a notées à l'étape A), S_Σ et S_max de chaque épisode, puis leurs aires d'épisode ; plancher = **quantile 0,95** des 200 aires (un pour S_Σ, un pour S_max) ; « au-dessus de son plancher » = borne basse de l'aire d'épisode **strictement** supérieure à ce quantile (même règle que T0.7, « Seuil »).
~~~

- **Nouveau** (candidat 4) :

~~~text
pour chacune des 800 directions de `plancher_<k>` (scores par action des directions aléatoires appariées que T0.7 a notées à l'étape A ; `n_plancher` = 800, T0.7 scellé, « Métrique » ; pour les deux sondes figées de P3 : le plancher neuf de la réextraction de l'étape A, jamais leurs 200 directions de P3, `plancher_p3_<k>`), S_Σ et S_max de chaque épisode, puis leurs aires d'épisode ; plancher = **quantile 0,95** des 800 aires (un pour S_Σ, un pour S_max) ; « au-dessus de son plancher » = borne basse de l'aire d'épisode **strictement** supérieure à ce quantile (**écart déclaré** à T0.7 scellé, « Seuil », qui lit la borne basse de la différence appariée D = aire − quantile 0,95 du plancher : la règle d'ici est celle de T0.7 brouillon 22, dont le niveau n'est pas tenu sous un plancher à signal commun ; elle n'entre dans les états A et M qu'en condition ajoutée à l'intervalle de Δ, qu'elle ne peut que restreindre ; un « au-dessus de son plancher » d'ici ne se lit pas comme celui de T0.7).
~~~

### G4-03 — RV-03 — Métrique (gelée)

- **Motif** : écart E-1 ; R-2330
- **Ancien** (candidat 3) :

~~~text
Δ de chacune des 200 directions ; quantile 0,95 rapporté.
~~~

- **Nouveau** (candidat 4) :

~~~text
Δ de chacune des 800 directions ; quantile 0,95 rapporté.
~~~

### G4-04 — RV-06 — Seuil (gelée), état E

- **Motif** : écart E-4 (précision) ; R-2330
- **Ancien** (candidat 3) :

~~~text
sonde en « échec » à la notation (`notation-t07.json`),
~~~

- **Nouveau** (candidat 4) :

~~~text
sonde en « échec » à la notation (`notation-t07.json` ; dont, pour une sonde figée de P3, « plancher neuf de la sonde figée non établi », T0.7 scellé, « Liste d'arrêt » : aucune lecture contre ses 200 directions de P3),
~~~

### G4-05 — C4-11 — Seuil

- **Motif** : CCB-6 (R-2281) : tension interne déclarée ; aucun état changé
- **Ancien** (candidat 3) :

~~~text
score ou direction non fini sur une action gardée ;
~~~

- **Nouveau** (candidat 4) :

~~~text
score ou direction non fini sur une action gardée (déclaré, CCB-6 : le plan, point 4, exclut toute tâche dont un score ou une direction n'est pas fini, si bien qu'aucune valeur non finie ne reste sur une action gardée ; cette cause n'est donc atteinte que par le seuil des 10 % ; le code suit le point 4) ;
~~~

### G4-06 — RV-04 — Plan d'analyse (gelée), point 1, E1

- **Motif** : écart E-1 ; R-2330
- **Ancien** (candidat 3) :

~~~text
`scores_<k>` et `plancher_<k>` (200 × actions) ; **jamais** `couple_<k>`,
~~~

- **Nouveau** (candidat 4) :

~~~text
`scores_<k>` et `plancher_<k>` (800 × actions) ; **jamais** `plancher_p3_<k>` (les 200 directions de P3 des sondes figées, que T0.7 lit en descriptif), `couple_<k>`,
~~~

### G4-07 — RV-07 — Plan d'analyse (gelée), point 1, E4

- **Motif** : écart renvoi ; R-2330
- **Ancien** (candidat 3) :

~~~text
(noms écrits par `lecture_v2.py` l. 1109-1125 au commit lu)
~~~

- **Nouveau** (candidat 4) :

~~~text
(noms écrits par `lecture_v2.py` l. 1109-1125 au commit lu ; au commit de `CODE-T07`, `b4cd9953d199dd8f220f5162e5868c5b00fd392d`, l'étape B est jouée par `lecture_v4.etape_b`, qui écrit les mêmes noms, l. 669-688)
~~~

### G4-08 — C4-12 — Plan d'analyse

- **Motif** : CCB-5 (R-2281) ; champ reserves de E4 lu depuis l'écart E-3 (R-2330, R-2336) ; déclaré
- **Ancien** (candidat 3) :

~~~text
; aucune activation.
2. **Registre et ordre** (section « Lignes de registre »)
~~~

- **Nouveau** (candidat 4) :

~~~text
; aucune activation.
   - **Déclaré** (CCB-5, contre-lecture du code ; aucune entrée ni règle changée) : le format `.npz` charge chaque tableau nommé de E1 et de E3 en entier ; les lignes de la condition `mention`, des conditions de `conditions_retirees` et, sous G-2, de `S25` à `S100` en sont ôtées dès le chargement, avant tout calcul, et ne sont jamais rendues : « jamais » (ci-dessus) et « aucune ligne … n'est lue » (point 3) s'entendent ainsi ; dans E2b, le champ `echec` de `resultat.index.sondes[]` est lu aussi, pour le seul motif d'un échec de notation (état E) ; dans E4, `resultat.reserves` est lu aussi, sans être exigé (absent sous G-1), pour les seules réserves du plancher neuf d'une sonde figée (point 5 ; écart E-3).
2. **Registre et ordre** (section « Lignes de registre »)
~~~

### G4-09 — C4-13 — Plan d'analyse

- **Motif** : CCB-7 (R-2281) : vérification au lancement ; un écart : aucun lancement, nœud
- **Ancien** (candidat 3) :

~~~text
dépôt qui porte le paquet ; sinon refus, code 2, avant tout calcul et avant le manifeste ;
~~~

- **Nouveau** (candidat 4) :

~~~text
dépôt qui porte le paquet ; sinon refus, code 2, avant tout calcul et avant le manifeste ; **au lancement**, hors du code (CCB-7 : des calculs décisifs vivent hors du paquet que `CODE-ACCB6` contrôle) : `src/controle_ia/sondes/evaluation.py`, `src/controle_ia/sondes/temoins.py` et `src/controle_ia/manifeste.py` de l'arbre lancé sont comparés, par empreinte, à ceux du commit cité par `CODE-ACCB6` (au commit `282e295e…` : `1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3`, `3b051b6fc2d78eeb4a44aab8a385bbce65095998e944b80e5f2a66e21b57faf7`, `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d`), comparaison écrite avant le lancement ; un écart : aucun lancement, nœud ;
~~~

### G4-10 — C4-14 — Plan d'analyse

- **Motif** : CCB-2 (R-2281) : phrase recommandée ; relance permise, déclarée
- **Ancien** (candidat 3) :

~~~text
3 tout arrêt après le manifeste (`arret-accb6.json` scellé).
~~~

- **Nouveau** (candidat 4) :

~~~text
3 tout arrêt après le manifeste (`arret-accb6.json` scellé). Une sortie hors des codes 0, 2 et 3 (exception qui n'est pas une `GardeArret`, levée après le manifeste : aucun `arret-accb6.json` n'est écrit et la garde de non-relance ne la voit pas) **n'est pas un arrêt** : relance permise, déclarée (entrées, code et graines figés ; CCB-2).
~~~

### G4-11 — RV-08 — Plan d'analyse (gelée), point 4

- **Motif** : écart renvoi ; R-2330
- **Ancien** (candidat 3) :

~~~text
(`jetons_notes` > 0, `lecture_v2.noter`, l. 595)
~~~

- **Nouveau** (candidat 4) :

~~~text
(`jetons_notes` > 0, `lecture_v2.noter`, l. 595 ; au commit de `CODE-T07`, `lecture_v4.noter`, l. 214)
~~~

### G4-12 — RV-09 — Plan d'analyse (gelée), point 5

- **Motif** : écart E-3 ; R-2330
- **Ancien** (candidat 3) :

~~~text
une réserve sans sonde visée est recopiée sans sonde).
~~~

- **Nouveau** (candidat 4) :

~~~text
une réserve sans sonde visée est recopiée sans sonde) ; les réserves du plancher neuf d'une sonde figée de P3 (palier « carte », principale rapportée : `lecture-t07.json` → `resultat.reserves`, chaînes qui commencent par « plancher neuf de <sonde> ») sont recopiées à côté de cette sonde.
~~~

### G4-13 — C4-15 — Plan d'analyse

- **Motif** : CCB-4 (R-2281) : sortie standard de la commande détournée
- **Ancien** (candidat 3) :

~~~text
scellé **avant toute lecture humaine** ;
~~~

- **Nouveau** (candidat 4) :

~~~text
scellé **avant toute lecture humaine** (la commande de lecture écrit la phrase gelée sur sa sortie standard, à sa fin : elle se lance avec sa sortie standard détournée, jetée ou versée dans un fichier que personne n'ouvre avant le verdict ; sa sortie d'erreur, qui porte les motifs de refus et d'arrêt, reste lue ; CCB-4) ;
~~~

### G4-14 — C4-16 — Critères de lecture gelés

- **Motif** : R-2330, option (a) de l'écart E-2 : réserve écrite (plus facile à obtenir que son homonyme de T0.7) ; aucun état changé
- **Ancien** (candidat 3) :

~~~text


**Audit de symétrie (R4)**, déclenché dans les deux sens, avant tout rapport :
~~~

- **Nouveau** (candidat 4) :

~~~text


**Réserve écrite sur le membre « au-dessus de son plancher »** (option (a) de l'écart E-2, décision de la mère R-2330 ; au texte seulement : ni le code ni la table des phrases ne l'écrivent ; aucun état, seuil ni niveau n'en dépend) : partout dans ce texte (hypothèse, états, phrases gelées), « au-dessus de son plancher » suit la règle d'intervalle contre quantile de ce texte (section « Métrique » : borne basse de l'aire d'épisode strictement supérieure au quantile 0,95 des aires d'épisode des directions), **déclarée distincte** de la règle de T0.7 scellé (section « Seuil » de T0.7 : borne basse de la différence appariée D = aire − quantile 0,95 du plancher, strictement positive) ; ce membre est **plus facile à obtenir que son homonyme de T0.7** (c'est la règle que T0.7 a quittée parce que son niveau n'est pas tenu sous un plancher à signal commun, R-2273 ; non simulée ici à l'échelle de l'épisode) et ne se lit jamais comme lui ; le niveau de « accumuler bat » et de « le maximum bat » tient à l'intervalle de Δ : le plancher n'y entre qu'en condition ajoutée, qui ne peut que restreindre.

**Audit de symétrie (R4)**, déclenché dans les deux sens, avant tout rapport :
~~~

### G4-15 — C4-17 — Critères de lecture gelés

- **Motif** : CCB-3 (R-2281) : « exactement 1 », comme le code ; aucun état n'en dépend
- **Ancien** (candidat 3) :

~~~text
toutes deux égales à 1,000 sur un jeu ;
~~~

- **Nouveau** (candidat 4) :

~~~text
toutes deux égales à 1 exactement sur un jeu (égalité exacte, comme le code : à 64 tâches, une aire de 1 − 1/4096 s'écrit 1,000 et ne déclenche pas ; CCB-3) ;
~~~

### G4-16 — RV-05 — Liste d'arrêt (gelée)

- **Motif** : écart E-1 ; R-2330
- **Ancien** (candidat 3) :

~~~text
nombre de directions de `plancher_<k>` ≠ 200 ;
~~~

- **Nouveau** (candidat 4) :

~~~text
nombre de directions de `plancher_<k>` ≠ 800 ;
~~~

### G4-17 — C4-18 — Liste d'arrêt

- **Motif** : CCB-7 (R-2281) : arrêt au lancement, en face du plan, point 2
- **Ancien** (candidat 3) :

~~~text
avant tout calcul et avant le manifeste (`code_accb6_v1.controler_code` ; CP-19).
~~~

- **Nouveau** (candidat 4) :

~~~text
avant tout calcul et avant le manifeste (`code_accb6_v1.controler_code` ; CP-19). Au lancement, `sondes/evaluation.py`, `sondes/temoins.py` ou `manifeste.py` de l'arbre lancé différent de celui du commit cité : aucun lancement, nœud (plan, point 2 ; CCB-7).
~~~

## 5. Exécution

- **Constructeur des couples** (bac à sable, non versé) : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/accb6-candidat4/construire_couples_c4.py`, `f32e2bbe8c5438ae00274005752c0586f27babf9f35d08e47191cb2d63c5178f` : recopie RV-01 à RV-11 (empreinte du fichier d'origine exigée), ajoute C4-01 à C4-28, exige chaque « ancien » une fois dans le candidat 3 et aucun chevauchement, numérote dans l'ordre du texte, écrit le fichier de couples (refus d'écraser) ; essayé dans le bac à sable, puis lancé vers le dossier des pièces : même empreinte, `d9dbbb8d211fa99eab7ab1b93b9ed3dde39fb923b35249e7bd349bdbca472bbb`.
- **Script** `accumulation-barreau6-v1-candidat4-faire-v1.py` : essais à blanc dans le bac à sable (12:15 UTC et suivantes ; une version intermédiaire écrivait un fichier transitoire pour `problemes`, remplacée avant tout versement par l'appel sur le fichier écrit), puis lancé pour de bon à 12:18:19 UTC (`python -I -B … /home/user/controle-ia-travail <dossier des pièces> brouillons/accumulation-barreau6-v1`) : code 0, « TOUT PASSE », candidat 4 `e3aef53004d18b07e7eb30c31d30ad00986f69528cd55f2e0a57bea9423dcf84` (261 → 266 lignes) ; candidat 3 relu ensuite : `d48fb8a3…`, intact.
- **Batterie des gardes du script** (R5) `accumulation-barreau6-v1-candidat4-essais-gardes-v1.py` : un cas sain et onze artefacts (RV réécrit ; couple en section gelée déclaré hors section gelée ; suppression sensible non permise ; marqueur laissé ; couple non réversible ; « ancien » absent ; numéro G4 faux ; candidat 4 présent et différent ; liste des sections gelées tronquée ; `problemes` non vide, candidat 4 neuf effacé ; titre de niveau 2 inséré), chacun dans un dossier temporaire du bac à sable, lisant les pièces versées : **12 sur 12 conformes**.
- **Assembleur du journal** (bac à sable, non versé) : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/accb6-candidat4/assembler_journal_c4.py`, `c6cd3005aa489eefade62b0ac14ca4529fad4dd9fb6d5d58b596322d3e8dfcba` : table des couples, liste G4 et question Q-1 tirées du fichier de couples ; sorties recopiées des fichiers versés.

### Sortie du script (lancement du 2026-11-11 à 12:18:19 UTC ; fichier `accumulation-barreau6-v1-candidat4-faire-v1-sortie.txt`)

~~~text
1. RV-01 à RV-11 égaux à l'octet à docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/reverification-t07-scelle-v1-pieces/couples-proposes-v1.json (771abfaf…)
2-4. 39 couples (RV-01 à RV-11, C4-01 à C4-28), ordre du texte, chaque « ancien » une fois, aucun chevauchement ; sections réelles conformes ; 17 en sections gelées (G4-01 à G4-17)
5. défaire les couples (ordre inverse, chaque « nouveau » une fois) redonne le candidat 3 à l'octet
6. isolement : les couples hors sections gelées laissent les sept sections gelées égales à l'octet ; les couples en sections gelées ne touchent rien d'autre ; titres inchangés
          (en-tête) : 9 couple(s) : C4-01, C4-02, C4-03, C4-04, C4-05, C4-06, C4-07, C4-08, C4-09
          Ce que les auteurs savaient avant le scellement : 1 couple(s) : C4-10
   GELÉE Prédiction chiffrée et signe attendu : 1 couple(s) : RV-02/G4-01
   GELÉE Métrique : 2 couple(s) : RV-01/G4-02, RV-03/G4-03
   GELÉE Seuil : 2 couple(s) : RV-06/G4-04, C4-11/G4-05
   GELÉE Plan d'analyse : 8 couple(s) : RV-04/G4-06, RV-07/G4-07, C4-12/G4-08, C4-13/G4-09, C4-14/G4-10, RV-08/G4-11, RV-09/G4-12, C4-15/G4-13
   GELÉE Critères de lecture gelés : 2 couple(s) : C4-16/G4-14, C4-17/G4-15
   GELÉE Liste d'arrêt : 2 couple(s) : RV-05/G4-16, C4-18/G4-17
          Puissance (écrite avant lecture ; planification, jamais une sélection) : 2 couple(s) : RV-10, C4-19
          Code (écrit et éprouvé ; R5) : 4 couple(s) : C4-20, C4-21, C4-22, C4-23
          Reste avant le scellement : 6 couple(s) : C4-24, C4-25, C4-26, C4-27, RV-11, C4-28
7. suppressions et remplacements, mot à mot, dans les couples en sections gelées :
   G4-01 RV-02 (Prédiction chiffrée et signe attendu) : 1 remplacement(s) ou suppression(s), 0 mot(s) inséré(s) seuls
      « 200 » → « 800 »
   G4-02 RV-01 (Métrique) : 3 remplacement(s) ou suppression(s), 144 mot(s) inséré(s) seuls
      « 200 » → « 800 »
      « 200 » → « 800 »
      « même règle que » → « * * écart déclaré * * à »
   G4-03 RV-03 (Métrique) : 1 remplacement(s) ou suppression(s), 0 mot(s) inséré(s) seuls
      « 200 » → « 800 »
   G4-04 RV-06 (Seuil) : 0 remplacement(s) ou suppression(s), 39 mot(s) inséré(s) seuls
   G4-05 C4-11 (Seuil) : 0 remplacement(s) ou suppression(s), 65 mot(s) inséré(s) seuls
   G4-06 RV-04 (Plan d'analyse) : 1 remplacement(s) ou suppression(s), 23 mot(s) inséré(s) seuls
      « 200 » → « 800 »
   G4-07 RV-07 (Plan d'analyse) : 0 remplacement(s) ou suppression(s), 36 mot(s) inséré(s) seuls
   G4-08 C4-12 (Plan d'analyse) : 0 remplacement(s) ou suppression(s), 192 mot(s) inséré(s) seuls
   G4-09 C4-13 (Plan d'analyse) : 0 remplacement(s) ou suppression(s), 99 mot(s) inséré(s) seuls
   G4-10 C4-14 (Plan d'analyse) : 0 remplacement(s) ou suppression(s), 77 mot(s) inséré(s) seuls
   G4-11 RV-08 (Plan d'analyse) : 0 remplacement(s) ou suppression(s), 17 mot(s) inséré(s) seuls
   G4-12 RV-09 (Plan d'analyse) : 0 remplacement(s) ou suppression(s), 52 mot(s) inséré(s) seuls
   G4-13 C4-15 (Plan d'analyse) : 0 remplacement(s) ou suppression(s), 66 mot(s) inséré(s) seuls
   G4-14 C4-16 (Critères de lecture gelés) : 0 remplacement(s) ou suppression(s), 273 mot(s) inséré(s) seuls
   G4-15 C4-17 (Critères de lecture gelés) : 1 remplacement(s) ou suppression(s), 31 mot(s) inséré(s) seuls
      « 1,000 » → « 1 exactement »
   G4-16 RV-05 (Liste d'arrêt) : 1 remplacement(s) ou suppression(s), 0 mot(s) inséré(s) seuls
      « 200 » → « 800 »
   G4-17 C4-18 (Liste d'arrêt) : 0 remplacement(s) ou suppression(s), 41 mot(s) inséré(s) seuls
   mots sensibles supprimés en sections gelées : « 1,000 » × 1 (CCB-3 (R-2281) : déclencheur d'audit écrit « 1 exactement », comme le code), « 200 » × 6 (écart E-1 (R-2330) : nombre de directions de plancher, 200 → 800 (RV-01 à RV-05))
8. aucun marqueur <<…>> restant
9. candidat 4 écrit : brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat4.md
   controle_ia.prereg.problemes sur le candidat 4 : [] (vide)
   « 6c98ea20 » gardé aux lignes [6, 6, 7, 20, 20, 40, 214, 214, 214, 214, 217, 217, 217, 261, 261, 262, 262, 262] (histoire, parent ou origine déclarée)
   « brouillon 22 » gardé aux lignes [3, 11, 23, 79] (histoire, parent ou origine déclarée)
TOUT PASSE ; candidat 4 : e3aef53004d18b07e7eb30c31d30ad00986f69528cd55f2e0a57bea9423dcf84 ; 261 → 266 lignes
~~~

### Sortie de la batterie des gardes (fichier `accumulation-barreau6-v1-candidat4-essais-gardes-v1.txt`)

~~~text
OK  | cas sain | code 0 | TOUT PASSE ; candidat 4 : e3aef53004d18b07e7eb30c31d30ad00986f69528cd55f2e0a57bea9423dcf84 ; 261 → 266 lignes [candidat 4 présent après le lancement]
OK  | RV-03 réécrit | code 1 | ARRÊT : RV-03 : différent du couple de la revérification (il doit être appliqué tel qu'écrit) ; rien d'écrit [candidat 4 absent après le lancement]
OK  | C4-11 déclaré hors section gelée | code 1 | ARRÊT : C4-11 : section réelle « Seuil » ; déclaré gelée = False ; rien d'écrit [candidat 4 absent après le lancement]
OK  | suppression sensible non permise (« 1 % ») | code 1 | ARRÊT : mot sensible supprimé en section gelée, hors de la liste blanche : {'1': 1, '%': 1} (nœud) ; rien d'écrit [candidat 4 absent après le lancement]
OK  | marqueur laissé | code 1 | ARRÊT : marqueurs restants : ['<<MARQUEUR_ESSAI>>'] ; rien d'écrit [candidat 4 absent après le lancement]
OK  | couple non réversible | code 1 | ARRÊT : C4-25 (retour) : texte cherché présent 2 fois (exactement une attendue) ; rien d'écrit [candidat 4 absent après le lancement]
OK  | ancien absent | code 1 | ARRÊT : C4-01 : « ancien » présent 0 fois dans le candidat 3 ; rien d'écrit [candidat 4 absent après le lancement]
OK  | numéro G4 faux | code 1 | ARRÊT : C4-17 : numéro de déclaration G4-99 ; G4-15 attendu ; rien d'écrit [candidat 4 absent après le lancement]
OK  | candidat 4 présent et différent (R12) | code 1 | ARRÊT : candidat 4 déjà présent et différent (R12) ; rien d'écrit [candidat 4 présent après le lancement]
OK  | liste des sections gelées tronquée | code 1 | ARRÊT : fichier de couples : liste des sections gelées différente de celle du script ; rien d'écrit [candidat 4 absent après le lancement]
OK  | problemes non vide : candidat 4 neuf effacé | code 1 | ARRÊT : controle_ia.prereg.problemes : ['marqueur À REMPLIR restant hors des sections exigées'] ; rien d'écrit [candidat 4 absent après le lancement]
OK  | titre de niveau 2 inséré hors section gelée | code 1 | ARRÊT : titres de niveau 2 changés ; rien d'écrit [candidat 4 absent après le lancement]
TOUS CONFORMES
~~~

## 6. Questions pour la mère

- **Q-1** (Plan d'analyse, point 2 (gelée), **non appliqué**) — R-2277 : le fichier de CODE-ACCB6 est écrit par ecrire_fichier_code(…, entropie=…), jamais par la commande `code_accb6_v1 ecrire`, qui tirerait une entropie neuve ; « Reste », pas 2, le dit ; le plan, point 2, écrit encore « écrit par `code_accb6_v1 ecrire` » : contradiction interne, hors du mandat du candidat 4.
  - ancien : `` (`{commit, fichiers, entropie}`, écrit par `code_accb6_v1 ecrire`) ``
  - nouveau proposé : `` (`{commit, fichiers, entropie}`, écrit par `code_accb6_v1.ecrire_fichier_code` avec l'entropie de R-2274, jamais par la commande `code_accb6_v1 ecrire` ; R-2277) ``
- **Q-2** — Réserve écrite de l'option (a) (C4-16) : au texte seulement. Si la mère veut que le code l'écrive à côté de chaque issue décisive (comme T0.7 pour T4), c'est une réserve neuve dans `phrases_v1.RESERVES` : commit neuf, énumération, essais, couple au texte ; ni R-2330 ni la revérification ne le demandent.
- **Q-3** — CCB-7 : la consigne nomme trois fichiers ; la contre-lecture du code nomme aussi `scellement.py` (`93beeb1c…`), `gardes.py` (`a83c48ce…`) et les modules de T0.7 que le paquet importe (`criteres_v1`, `plancher_v1`, `registre_v1`), tous égaux aujourd'hui entre `6c98ea20`, `282e295e` et C7 ; je n'ai écrit que les trois nommés. La conséquence « un écart : aucun lancement, nœud » (plan, point 2, et sa ligne de « Liste d'arrêt », G4-17) est ma formulation : CCB-7 dit seulement « vérifier … et l'écrire » ; sans conséquence, la vérification serait un repli silencieux (R5).
- **Q-4** — Le code v2 s'arrête si `resultat.reserves` est présent et hors de forme (choix déclaré du développeur, gardé par R-2336) : écrit dans la section « Code » (non gelée) ; aucune ligne propre dans « Liste d'arrêt » (hors du mandat), la ligne « champ de T0.7 attendu absent … : arrêt, nœud » n'en parlant pas mot pour mot.
- **Q-5** — Puissance non resimulée à 800 directions (réserve écrite, point 11). Une resimulation (processeur seul, de l'ordre du quart d'heure au brouillon 2 pour 200 directions) ne toucherait que les cellules où la condition de plancher mord ; à décider par la mère, jamais pour choisir quoi que ce soit (R3).
- **Q-6** — « Reste », pas 5 : la vérification courte demandée par R-2280 couvre le différentiel du candidat 2 au candidat final, donc C3-01 à C3-16, RV-01 à RV-11 et C4-01 à C4-28 ; points à y regarder de près : la place et les mots de C4-16 (réserve écrite), la phrase de CCB-2 (relance permise), la conséquence de CCB-7 (Q-3).

## 7. Écarts et déclarations

- **Commandes git au-delà de `git show <commit>:<chemin>`** (lecture seule ; aucune ne touche l'index, l'arbre ni une branche) : `git rev-parse --show-toplevel`, `git status --short`, `git branch --show-current`, `git log --oneline -3`, `git cat-file -t`, `git log -1 --format`, `git branch -a --contains`, `git show --stat --format`, `git diff --stat 6c98ea20 282e295e -- src` ; écart à la lettre de la règle 4 des interdits, déclaré (même écart que VB6-7 et que la contre-lecture du code, § 2).
- `git status --short` a montré des **noms** de fichiers d'un dossier de P3-bis (`docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/` : un rapport modifié, des journaux et scripts non suivis) : aucun ouvert.
- Recherches : `grep` sur des fichiers nommés seulement (candidat 3, `registres/decisions.md`, `registres/scellements-v1.md`, T0.7 scellé, `prereg.py`, `scellement.py`, sorties de `git show`) ; aucune recherche récursive.
- Aucun chemin interdit ouvert ; aucune valeur de sonde de 7a ; aucune clé, aucun `env`.
- Écritures : `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat4.md` (et son compagnon), le dossier `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat4-pieces/`, et le bac à sable ; aucun fichier transitoire dans le dépôt pendant le lancement réel.
- Aucun refus d'un contrôle de permissions ; aucun redémarrage du conteneur pendant le travail.

## 8. Fichiers rendus (chacun avec son compagnon `.sha256`, écrit par `controle_ia.scellement sceller`)

| fichier | sha256 |
|---|---|
| `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat4.md` | `e3aef53004d18b07e7eb30c31d30ad00986f69528cd55f2e0a57bea9423dcf84` |
| `…/accumulation-barreau6-v1-candidat4-pieces/accumulation-barreau6-v1-candidat4-couples-v1.json` | `d9dbbb8d211fa99eab7ab1b93b9ed3dde39fb923b35249e7bd349bdbca472bbb` |
| `…/accumulation-barreau6-v1-candidat4-pieces/accumulation-barreau6-v1-candidat4-faire-v1.py` | `3196727b72ec85ddded285adc86cff96ac119936a138e7d73f60332195418f13` |
| `…/accumulation-barreau6-v1-candidat4-pieces/accumulation-barreau6-v1-candidat4-faire-v1-sortie.txt` | `3c676641c65675544d94636725104d32993b04ac86bb7c2fca9185a1d3fdf9b8` |
| `…/accumulation-barreau6-v1-candidat4-pieces/accumulation-barreau6-v1-candidat4-essais-gardes-v1.py` | `24dfb62d6e2d2b3e9f4fc2216fe582ef37c52badb3d22d8927bdad269820e6b7` |
| `…/accumulation-barreau6-v1-candidat4-pieces/accumulation-barreau6-v1-candidat4-essais-gardes-v1.txt` | `c25333120db8df87022d92ef548c3b8ed80c2f66ed34ac4cf59947a43972bb1e` |
| ce journal | compagnon écrit au scellement |
