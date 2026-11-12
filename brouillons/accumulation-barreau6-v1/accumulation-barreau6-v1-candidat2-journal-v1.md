# Journal — barreau 6, candidat 2 — v1

Même rédacteur (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; même consigne (`f86a6834ccf0d0f8b53d3821c2a52495c711837e07563633059170a4765da7c2`), mêmes interdits ; aucun commit, aucun appel de modèle, aucune dépense ; candidat 1 intact (`b8bbea6a371335311a1e42cc7b37b0d1ffb632ec670746a4695c8ee6c49bc742`). Je n'ai ouvert ni le verdict ni aucune sortie de `agregation-r1-v4`, ni aucune sortie de T0.7 ou de P3-bis. Heures relevées par `date -u`.

## 1. Entrées et vérifications (20:27:13 UTC)

- Message de la mère (R-2276) : `COMMIT_CODE_ACCB6` = `5ee8a4ac8712221a31599e2a92dfbae981cc5704`, qui porte la garde de non-relance ; couples à nom neuf : le commit partout où le candidat 1 cite `56c624dd…`, section « Code » (écart levé), « Reste avant le scellement » ; énumération inchangée, à vérifier au nouveau commit.
- Complément 2 du développeur, lu entier : `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/rapport-developpeur-accb6-v1-complement2-v1.md`, `94226fc8908d4746e63f945892d7a3aaea804c7d301f0bd241bcbfaa46ef3d7f`, égal à son compagnon.
- Au commit `5ee8a4ac…`, par `git show` (aucun `checkout`) : `56c624dd…` en est l'ancêtre (`git merge-base --is-ancestor`) ; `scripts/enumeration_etats_accb6_v1.py` `d7b6fa08f02c0b494f58aca7803099240baf28723a93334235701cb5594a431f` et `scripts/enumeration-etats-accb6-v1.txt` `3bde500f1eca8ceb5e95b782ea74312cace981d019d8fef6ead7944341abf5a6` **inchangés** ; `src/controle_ia/accumulation_b6/garde_v1.py` `2885c1f49958ce8ff4c20b3e8283051de9c03e3b0ab3f864a509bc49de80928e` et `tests/test_accb6_relance_v1.py` `cc458330b2d3b7731c5a571ee71baf0a2e8eedf6a1d0521fbdc521d166ff3a0d`, égaux au complément 2.

## 2. Couples C2-01 à C2-09 (aucune section gelée touchée)

| couple | où | quoi |
|---|---|---|
| C2-01 | titre | « candidat 2 » |
| C2-02 | en-tête, date | heure du candidat 2, journal |
| C2-03 | en-tête, statut | candidat 2 = candidat 1 + C2-01 à C2-09 ; sections touchées nommées |
| C2-04 | en-tête, commit du code | `5ee8a4ac…` (parent `56c624dd…`, garde de non-relance ; R-2276) |
| C2-05 | en-tête, documents qui font foi | complément 2 ajouté ; code au commit `5ee8a4ac…` |
| C2-06 | « Ce que les auteurs savaient » | lectures du candidat 2 |
| C2-07 | section « Code », paragraphe « État » | commit `5ee8a4ac…` ; 168 essais, 67 mutations sur 67 ; **garde de non-relance au code** (`garde_v1.py`, `2885c1f4…`), éprouvée : cas sain, artefact, bout en bout ; mutations R01, R02 tuées ; **écart du candidat 1 levé** |
| C2-08 | section « Code », ligne de l'énumération | « au commit `5ee8a4ac…` (inchangés depuis `56c624dd…`, empreintes vérifiées au nouveau commit) » |
| C2-09 | « Reste avant le scellement » | pas 1 : garde au code, rien à faire ; pas 2 : fichier et ligne `CODE-ACCB6` au commit `5ee8a4ac…` (celui de `56c624dd…` ne vaut plus ; une seule ligne) ; question sur l'entropie ; pas 5 : vérification courte des candidats 1 et 2 |

Les citations restantes de `56c624dd…` sont voulues (parent du commit ; lecture faite au candidat 1 ; « inchangés depuis » ; notes du pas 2) : le script les imprime.

## 3. Exécution

- Constructeur des couples : bac à sable, `…/c2/construire_couples_c2.py` (`70d235a069c55a0034c4cc103b062288056db706308300c4271e42f9ce9ba1bf`, non versé).
- Script `accumulation-barreau6-v1-candidat2-faire-v1.py` essayé sur une copie du bac à sable, puis lancé dans le dossier du brouillon (20:28 UTC) : « 9 couples appliqués ; marqueurs restants : `REVERIFICATION_T07_SCELLE` ; TOUT PASSE ; candidat 2 : `0716d3d5…` ». `controle_ia.prereg.problemes` : seul `REVERIFICATION_T07_SCELLE`.

## 4. Question pour la mère

**Entropie de `CODE-ACCB6`** : `code_accb6_v1 ecrire` tire une entropie neuve à chaque fichier ; pour garder `186246456082298562823446322699284949559` (R-2274), il faut la passer à `ecrire_fichier_code(…, entropie=…)` ; sinon `ENTROPIE_ACCB6` doit être rempli de nouveau (couple d'une ligne). Écrit au pas 2 de « Reste avant le scellement ».

## 5. Fichiers rendus (dossier `brouillons/accumulation-barreau6-v1/`, chacun avec compagnon `.sha256`)

| fichier | sha256 |
|---|---|
| `accumulation-barreau6-v1-candidat2.md` | `0716d3d52fd60f76b51c921ef8284580d70ddc587d855cfbc12381c1667baee1` |
| `accumulation-barreau6-v1-candidat2-couples-v1.json` | `e0b49d841d14b5f57b66d5f155cfdab867301e0ac79725df23bcbde27c9d1253` |
| `accumulation-barreau6-v1-candidat2-faire-v1.py` | `c923339b89fb0be1e944e21d6676e5e796bb627c874301a86f84ec16ffd01811` |
| ce journal | compagnon écrit au scellement |
