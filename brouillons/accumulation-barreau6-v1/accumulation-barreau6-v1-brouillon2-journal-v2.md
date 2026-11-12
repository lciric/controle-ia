# Journal — barreau 6, brouillon 2 — v2 (règle retenue, brouillon 2 écrit)

Suite du journal v1 du brouillon 2 (`accumulation-barreau6-v1-brouillon2-journal-v1.md`, `3aefe21b4633e78c3e5d6cc9c6640399a4cbcde442acc8d3b7da5664f1e97125`, gardé tel quel, R12), qui s'arrêtait sur le dépassement sous le nul. Même rédacteur (Claude Opus 5.5), même consigne (`f86a6834…`), mêmes interdits ; aucun commit, aucun appel de modèle, aucune dépense. Heures relevées par `date -u`.

## 1. Décision reçue

Message de la mère (R-2263) : option (a) — 10 000 tirages et niveau resserré à 1 − 0,05/(2k) ; refaire la simulation sous le nul et la puissance aux mêmes lois, scripts à noms neufs, sorties versées ; si l'erreur reste au-dessus du niveau annoncé dans une cellule, écrire la réserve gelée correspondante et le dire, au lieu de s'arrêter ; puis écrire le brouillon 2, marqueurs `ISSUE_NUL_ACCB6` et `ISSUE_NUL_ACCB6_DETAIL` remplis, scellé. Le point de symétrie sur T0.7 est pris par la mère (analyste neuf).

## 2. Heures

| heure (UTC) | fait |
|---|---|
| 16:42:34 | deux entropies tirées une fois (`secrets.randbits(128)`) : nul v2 `139867924097371433405432113141003785138`, puissance v2 `93336667468152066419228967737062682034` |
| 16:43:47 à 16:51:35 | simulation sous le nul, règle retenue (`nul_accumulation_b6_v2.py`), code 0, 468,1 s |
| 16:51:35 à 17:03:13 | puissance, règle retenue (`puissance_accumulation_b6_v2.py`), code 0, 696,9 s |
| 16:52:06 | sorties du nul v2 scellées |
| 17:04:15 | sorties de la puissance v2 scellées |
| 17:04 à 17:06 | couples v2 construits ; script d'application v2 dérivé du v1 (nom du fichier de couples, en-tête, ligne d'usage) ; essai sur une copie du bac à sable (« TOUT PASSE », `9f070e31…`) ; puis exécution dans le dossier du brouillon : brouillon 2 écrit, scellé |

## 3. Simulation sous le nul, règle retenue — aucun dépassement établi

- Script `nul_accumulation_b6_v2.py` (`de5fc3de3072e34b55249ceb67c250046e7c841f847346635b9880572c026a13`), sorties `nul-accumulation-b6-v2.txt` (`bbea89756fc01efedfec1427dd65cd7fe1f6290f78eefa56c04fe7d57403c3be`) et `nul-accumulation-b6-v2.json` (`073aa5ed83a0a2965822dd5013731c856ead9b9937b132954210c6d469bdc208`). Mêmes 18 cellules que la v1 (la v1 du nul est importée, empreinte vérifiée, avec le script de puissance du brouillon 1) ; seuls changent les tirages (10 000), les niveaux (99,375 %, 99,167 %, 98,75 % pour k = 4, 3, 2) et l'entropie. Niveau annoncé inchangé : 0,05/(2k) par sonde et par côté.
- **64 tâches** : par sonde au plus 0,0020 (A) et 0,0050 (M) à k = 4 ; 0,0040 et 0,0065 à k = 3 ; 0,0065 et 0,0100 à k = 2 ; familles au plus 0,013 (A) et 0,032 (A ou M). Tout sous le niveau annoncé.
- **36 tâches** : deux estimations au niveau annoncé ou juste au-dessus, **sans dépassement établi** (borne basse de Clopper-Pearson sous l'annoncé) : 0,0065 pour 0,00625 (côté M, k = 4 ; [0,0035 ; 0,0111]) et 0,0085 pour 0,00833 (côté A, k = 3 ; [0,0050 ; 0,0136]), dans la cellule s1, décalage 2 ; familles au plus 0,026 (A) et 0,050 (A ou M).
- **Ce que j'en ai fait (consigne de la mère)** : l'erreur ne reste au-dessus du niveau annoncé, en estimation seule, que dans une cellule du plan à 36 tâches ; **réserve gelée R-B6-NUL36 écrite** (B2-19), qui ne s'applique que si 7b est jouée à 36 tâches (DT-1 (a) ; le plan en vigueur est à 64) ; aucune réserve n'est nécessaire à 64 tâches.
- Nul pur : aucune fausse décision.

## 4. Puissance, règle retenue — perte

- Script `puissance_accumulation_b6_v2.py` (`5913df91dcf42ec27d42ed5ccb8e45614abf53ad91350fa769920f8dd05053ad`), sorties `puissance-accumulation-b6-v2.txt` (`5dfd176ab9e39394986b4c1ce5bc081b822332973e9336803383783b1774be64`) et `puissance-accumulation-b6-v2.json` (`da69c0b8eb008531dde074895a29f622f68dbaa59b1d023cb2d40679caa39184`) ; il importe le script du brouillon 1 (`ccc5310b…`) et compare à sa sortie versée (`5f9f598f…`), empreintes vérifiées.
- Perte, 64 tâches, k = 4 : s1 (corrélation intra-épisode 0,2), dense : P(A) 0,02 à 0,32 au lieu de 0,04 à 0,45 (−0,02 à −0,13, environ un tiers) ; s0 : 0,52 à 0,98 au lieu de 0,58 à 0,99 ; s2 : au plus 0,12 au lieu de 0,18 ; « le maximum bat » (s1, densité 0,5, a = 0,65) : 0,16 au lieu de 0,26 ; séquence « moyen » : `S100` franchie 0,26 au lieu de 0,37, deux doses 0,05 au lieu de 0,12.

## 5. Brouillon 2

- `accumulation-barreau6-v1-brouillon2.md`, `9f070e31734be21d753967e0df11ee2aae174906d170a36f27a45c52714494c3` = brouillon 1 + CL1-01 à CL1-28 (tels qu'écrits) + B2-01 à B2-19, par `accumulation-barreau6-v1-brouillon2-faire-v2.py` (`f25d859d3459b490b850dcdcf984341c3905406c26a4f9db5d430d0334d27dae`) sur `accumulation-barreau6-v1-brouillon2-couples-v2.json` (`36c421dd4c769d3fe2659d34b7225611e0bebba903c544301cd444efaf85ba6b`) ; empreinte intermédiaire après les 28 couples de la contre-lecture : `e903c91c…`, égale à l'attendue ; options (b) et (c) de N-B6-3 vérifiées applicables, non appliquées.
- Couples B2 changés ou ajoutés par rapport aux couples v1 (`dc747358…`, gardés, R12) : B2-03 (statut), B2-04 (documents : scripts v2), B2-05 (lu : R-2263), B2-10 (traitement de CLA-09) ; **B2-12** (phrase d'erreur de première espèce : niveau annoncé, règle retenue, taux mesurés — remplit `ISSUE_NUL_ACCB6`) ; **B2-13** (section « Puissance » réécrite : table sous la règle retenue, brouillon 1 entre parenthèses, points 1 à 10, dont le point 9 « sous le nul » — remplit `ISSUE_NUL_ACCB6_DETAIL` — et le point 10 « perte de puissance ») ; B2-14 (Δ : 10 000 tirages) ; B2-15 (niveau 1 − 0,05/(2k), niveau annoncé, écart déclaré à T0.7, désaccord avec `niveau_applique` → arrêt) ; B2-16, B2-17 (cellules de prédiction) ; B2-18 (confiance : ≈ 0,15 au lieu de ≈ 0,2) ; B2-19 (réserve R-B6-NUL36).
- `controle_ia.prereg.problemes` : une seule ligne, marqueurs restants : `COMMIT_CODE_ACCB6`, `DECISION_N_B6_1`, `DECISION_N_B6_2`, `DECISION_N_B6_3`, `ENTROPIE_ACCB6`, `ENUMERATION_ETATS_ACCB6`, `REVERIFICATION_T07_SCELLE`.
- Constructeur des couples v2 : bac à sable, `…/b2/construire_couples_v2.py` (non versé).

## 6. Fichiers versés à cette étape (chacun avec compagnon `.sha256`)

| fichier | sha256 |
|---|---|
| `accumulation-barreau6-v1-brouillon2.md` | `9f070e31734be21d753967e0df11ee2aae174906d170a36f27a45c52714494c3` |
| `accumulation-barreau6-v1-brouillon2-couples-v2.json` | `36c421dd4c769d3fe2659d34b7225611e0bebba903c544301cd444efaf85ba6b` |
| `accumulation-barreau6-v1-brouillon2-faire-v2.py` | `f25d859d3459b490b850dcdcf984341c3905406c26a4f9db5d430d0334d27dae` |
| `nul_accumulation_b6_v2.py` | `de5fc3de3072e34b55249ceb67c250046e7c841f847346635b9880572c026a13` |
| `nul-accumulation-b6-v2.txt` | `bbea89756fc01efedfec1427dd65cd7fe1f6290f78eefa56c04fe7d57403c3be` |
| `nul-accumulation-b6-v2.json` | `073aa5ed83a0a2965822dd5013731c856ead9b9937b132954210c6d469bdc208` |
| `puissance_accumulation_b6_v2.py` | `5913df91dcf42ec27d42ed5ccb8e45614abf53ad91350fa769920f8dd05053ad` |
| `puissance-accumulation-b6-v2.txt` | `5dfd176ab9e39394986b4c1ce5bc081b822332973e9336803383783b1774be64` |
| `puissance-accumulation-b6-v2.json` | `da69c0b8eb008531dde074895a29f622f68dbaa59b1d023cb2d40679caa39184` |
| ce journal | compagnon écrit au scellement |
