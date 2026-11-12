# Journal — barreau 6, candidat 1 — v1

Même rédacteur (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; même consigne (`f86a6834ccf0d0f8b53d3821c2a52495c711837e07563633059170a4765da7c2`), mêmes interdits ; aucun commit, aucun appel de modèle, aucune dépense ; brouillons 1 (`a2d81863…`) et 2 (`9f070e31…`) intacts (compagnons vérifiés). Je n'ai ouvert ni le verdict ni aucune sortie de `agregation-r1-v4`, ni aucune sortie de T0.7 ou de P3-bis. Heures relevées par `date -u`.

## 1. Entrées

- Message de la mère : décisions de Lazar R-2265, verbatim « NL-2 go, inscris GO-2026-11-10-11; Décisions qui t’attendent : : go recos » → N-B6-1 (a), N-B6-2 (a), N-B6-3 (a) ; code R-2272, R-2274 ; consignes : appliquer CP-01 à CP-19 tels qu'écrits, déclarer un à un ceux qui touchent des phrases ou des réserves gelées (s'arrêter si l'un change un signe ou un seuil), ajouter un couple qui refuse la relance après un arrêt (code 3), remplir `COMMIT_CODE_ACCB6` (`56c624ddb02941e09ff5bb96d8c848214e6b576a`), `ENTROPIE_ACCB6` (`186246456082298562823446322699284949559`) et `ENUMERATION_ETATS_ACCB6`, garder `REVERIFICATION_T07_SCELLE`.
- Rapports du développeur, lus entiers, empreintes vérifiées : `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/rapport-developpeur-accb6-v1.md` (`2a6880e4e3ef65db858a60f67b2eb723001fdb7df364993fc7b21e46f203fb1c`, égal à son compagnon) et `rapport-developpeur-accb6-v1-complement-v1.md` (`02d837c9b22c5da31d1694b25ddcb6604877e4aa119df8edb8c5953f0df09e5a`, égal à son compagnon).
- Code, lu par `git show 56c624dd…:<chemin>` seulement (aucun `checkout`) : empreintes au commit égales aux rapports — `scripts/enumeration_etats_accb6_v1.py` `d7b6fa08f02c0b494f58aca7803099240baf28723a93334235701cb5594a431f`, `scripts/enumeration-etats-accb6-v1.txt` `3bde500f1eca8ceb5e95b782ea74312cace981d019d8fef6ead7944341abf5a6`, `src/controle_ia/accumulation_b6/phrases_v1.py` `9376fcc05337d4979a3f40acc3b2e84ecdb03fb528c24b3d6c3e3bc4bfb9f228`, `src/controle_ia/accumulation_b6/lecture_v1.py` `70764f664ffb9670baa88000323cccfc440d4387c9bcea9a6e7baefdb474e6c8` ; recherche de mots dans `phrases_v1.py` (la constante `BARREAU` porte la forme faible et sert aussi à la phrase de (i), l. 22 et 53).

## 2. Heures

| heure (UTC) | fait |
|---|---|
| 19:50:39 | rapports et branche localisés, empreintes vérifiées |
| 19:51 à 19:53 | lecture des rapports ; anciens des couples comptés dans le brouillon 2 (chacun une fois exactement ; marqueurs une fois chacun) |
| 19:53 à 19:55 | couples construits (bac à sable, `…/c1/construire_couples_c1.py`, `51f1ab1d971af4e620e5a7adea1f1adefd28f80a2ec9fe2694bfd55e791469b9`, non versé) ; script d'application écrit ; essai sur une copie du bac à sable : « TOUT PASSE », même empreinte qu'ensuite |
| 19:55:37 | candidat 1 écrit dans le dossier du brouillon, scellé avec ses couples et son script ; `controle_ia.prereg.problemes` : seul `REVERIFICATION_T07_SCELLE` |

## 3. Couples du développeur, appliqués tels qu'écrits — section touchée, et effet sur un signe ou un seuil

Aucun ne change un signe, un seuil, un niveau, une règle d'état décisif (A, M, Z, P, S, N, E, F) ni l'ordre de la séquence fixée : **pas d'arrêt**. Points de suspension du rapport (« … ») remplis par l'ancien, sans autre mot (CP-07a, CP-07b, CP-12, CP-14, CP-15, CP-17 ; écrit dans le champ `reconstruit` du fichier de couples). CP-02 : version du complément (avec `code_accb6_v1.py`). CP-07 : deux couples (a, b). CP-13 et CP-18 (« à ajouter », sans ancien) : ajoutés tels qu'écrits à l'endroit que le rapport nomme, ancre déclarée dans le fichier de couples.

| couple | section | nature | signe ou seuil changé ? |
|---|---|---|---|
| CP-01 | Code | nom du script d'énumération | non |
| CP-02 | Code | liste des fichiers du paquet | non |
| **CP-03** | **Critères de lecture gelés — phrase de (i)** | la phrase « accumuler bat » de (i) est écrite en propre ; elle ne recopie plus « contrôle à adaptateur égal à la seule dose 1 (`T100`) », qui ne vaut pas pour (i) ; elle nomme le contrôle de consigne (`temoin`, B6-D3, B6-D3b) que le texte prévoit déjà | non : alignement sur le sens écrit (« organisme nommé ») ; même condition, même état |
| **CP-04** | **Critères — ligne « (i) le maximum bat »** | supprime la répétition « réfuté … : réfuté … pour (i) » | non : même phrase de réfutation |
| CP-05 | Seuil — règle F | `saboteur` contre `temoin` ajouté aux jeux sans audit de fuite ; les quatre jeux descriptifs reçoivent un état à 95 % | non : niveau descriptif déjà écrit (95 %) |
| **CP-06** | **Prédiction — B6-D5, réserve R-B6-DIR** | la réserve vise les sondes en A du jeu | non : condition d'écriture d'une réserve, sans effet sur un état |
| **CP-07a, CP-07b** | **Critères — R-B6-ADAPT, R-B6-CONSIGNE** | le second volet vise les sondes en A | non : idem |
| CP-08 | Critères — ligne G-3 | forme de « (ii) en descriptif » : séquence calculée au niveau de B6-P2, jamais « réfuté … pour (ii) » | non : G-3 restait descriptif |
| CP-09 | Critères — ligne `S100` « accumuler bat » | forme de l'état de la dose d'arrêt | non : la réfutation à la dose d'arrêt était déjà celle de B6-P2 |
| CP-10 | Plan, point 2 | lecture unique sur tout run ; nom du run | non (garde) |
| CP-11 | Plan, point 3 | recoupements de l'aiguillage | non (garde) |
| CP-12 | Liste d'arrêt | recoupements E1, E2, E2b, E3, E4 | non (gardes) |
| CP-13 | Plan, point 2 | codes de sortie | non |
| CP-14 | Critères — R-B6-TARD, R-B6-CODE | « postérieur » = « non strictement antérieur » ; R-B6-CODE aussi quand l'antériorité est invérifiable | non : réserves |
| CP-15 | Plan, point 5 | quelles sondes une réserve de T0.7 vise | non |
| CP-16 | Plan, point 4 (règle E) | dénominateur des 10 % | non : même seuil, dénominateur écrit |
| CP-17 | Critères — audit R4 | « tous les jeux lus » = les neuf jeux qui reçoivent un état | non : déclencheur d'audit |
| CP-18 | Critères | mise en forme des phrases (paragraphe ajouté) | non |
| CP-19 | Plan, point 2 | contrôle du code contre `CODE-ACCB6` (refus, code 2) | non (garde) |

## 4. Couples du rédacteur (C1-01 à C1-17)

C1-01 titre ; C1-02 date ; C1-03, C1-04 statut (« Non scellable » : seul `REVERIFICATION_T07_SCELLE`) ; **C1-05** (Critères, phrase de (i)) : « Barreau 6 » s'y écrit aussi sous la forme faible (N-B6-3 (a), R-2265 ; c'est ce que fait `phrases_v1.py`) — alignement, aucun signe ni seuil ; C1-06 `COMMIT_CODE_ACCB6` ; C1-07 `ENTROPIE_ACCB6` ; C1-08 `ENUMERATION_ETATS_ACCB6` (script, sortie, bilans) ; C1-09 à C1-11 `DECISION_N_B6_1` à `_3` (mots de Lazar, R-2265) ; **C1-12** (Plan, point 2) : **refus de toute relance après un arrêt** — `diag/<run>/arret-accb6.json` d'un run quelconque présent → refus, code 2, nœud ; une lecture après un arrêt demande une version neuve du texte ; **C1-13** (Liste d'arrêt) : relance (lecture invalide si faite quand même) et contrôle du code de CP-19 (« à ajouter … à la liste d'arrêt ») ; C1-14 section « Code » : état du code (commit, branche non fusionnée, essais, mutations, énumération), **écart déclaré** : la garde de non-relance n'est pas dans le code au commit `56c624dd…` (point ouvert 4 du développeur) ; C1-15 documents qui font foi ; C1-16 « Ce que les auteurs savaient » ; C1-17 section finale renommée « Reste avant le scellement » : `REVERIFICATION_T07_SCELLE` (après le scellement de T0.7) et cinq pas hors marqueurs.

## 5. Point pour la mère

**Garde de non-relance** : le texte la pose (C1-12, C1-13) ; le code au commit cité ne la porte pas. Deux voies : (a) version neuve du code (garde, essai, mutation), fichier et ligne `CODE-ACCB6` au nouveau commit — `COMMIT_CODE_ACCB6` change alors ; (b) garder `56c624dd…` et tenir la garde par procédure (aucune relance par la session mère), déclarée. Écrit dans « Reste avant le scellement », pas 1.

## 6. Fichiers rendus (dossier `brouillons/accumulation-barreau6-v1/`, chacun avec compagnon `.sha256`)

| fichier | sha256 |
|---|---|
| `accumulation-barreau6-v1-candidat1.md` | `b8bbea6a371335311a1e42cc7b37b0d1ffb632ec670746a4695c8ee6c49bc742` |
| `accumulation-barreau6-v1-candidat1-couples-v1.json` | `01c9d5aec00173b9b59100dc3a57831d31d4d06759529b1d1b3179aa78dda4e8` |
| `accumulation-barreau6-v1-candidat1-faire-v1.py` | `1e58c25ffc3984c4810a812e2fd2dabe02b0fba2e33e025b775582caf81f4356` |
| ce journal | compagnon écrit au scellement |
