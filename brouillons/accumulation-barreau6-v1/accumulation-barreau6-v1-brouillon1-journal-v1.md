# Journal — barreau 6, texte court préenregistré, brouillon 1 — v1

Rédacteur neuf, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` (Claude Opus 5.5, `claude-opus-5-5`). Toutes les heures sont relevées par `date -u` et dites telles. Aucun commit, aucun appel de modèle, aucune dépense ; écritures sous `brouillons/accumulation-barreau6-v1/` et dans le bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/barreau6/` seulement.

## 1. Heures

| heure (UTC) | fait |
|---|---|
| 15:37:17 | empreinte de la consigne vérifiée (`sha256sum`) : `f86a6834ccf0d0f8b53d3821c2a52495c711837e07563633059170a4765da7c2`, égale à la consigne et à son compagnon ; puis lecture |
| 15:37 | empreintes des pièces à lire vérifiées (section 2) |
| 15:37 à 15:48 | lectures (section 3) |
| 15:48:07 | entropie de la simulation de puissance tirée une fois (`secrets.randbits(128)`) : `143381448204265874151922139412594211354`, sans lecture de données |
| 15:48:36 | dossier `brouillons/accumulation-barreau6-v1/` créé (absent auparavant, vérifié par `ls`) |
| 15:49 à 15:50 | essais rapides de la simulation dans le bac à sable (calibrage de l'aire par action : moyenne de 400 répétitions à 64 tâches égale à la cible à 0,001 près ; 0,5505, 0,5992, 0,6982 pour 0,55, 0,60, 0,70) |
| 15:50 | lancement de la simulation complète (section 6) |
| 15:50:47 | essai des clés de registre contre la garde de T0.7, bac à sable (section 5) ; rejoué à 15:57:32 depuis le dossier du brouillon (copie à dossier temporaire) |
| 15:57 | brouillon 1 écrit (hors section « Puissance ») |
| 16:06:42 | fin de la simulation (code 0, 974,7 s) |
| 16:07 à 16:09 | section « Puissance » et cellules de prédiction remplies d'après la sortie ; corrections de rédaction (table des phrases ordonnée « première ligne qui s'applique », phrase de (i) définie, d* défini, ligne de saturation précisée, « diffus » limité à (i-a)) ; `controle_ia.prereg.problemes` : seuls des marqueurs restent |
| 16:09:19 | brouillon, scripts et sorties scellés (`controle_ia.scellement sceller`), compagnons vérifiés (`sha256sum -c` : OK) |

## 2. Empreintes vérifiées (`sha256sum`, 10 novembre 2026, vers 15:37 à 15:48 UTC)

Toutes égales aux préfixes de la consigne et, le cas échéant, à leur compagnon `.sha256` :
- consigne `f86a6834ccf0d0f8b53d3821c2a52495c711837e07563633059170a4765da7c2` ; interdits communs v2 `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` ;
- rapport des prémisses `2638558e34c15800acf7c8d8653dd978eba0660a9341795069d7ddd3b58e712f` ;
- T0.7 brouillon 22 `8b84cba5bd527e10a3b835ebc0caa7e7da0e31af503904e51621d752d65f0a37` ; T0.6 scellé `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` ; configuration de 7b `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` ; base (A) scellée `72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d` ;
- programme v2 `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` ; N-007/N-008 `ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232` ; N-054 `c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f` ; N-055 `371879d5bd44f5fdd7f2ff2fe068065776000e0b2acc9118fa94b41f687340b6` ; N-056 `3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d` ;
- rapport lot 3 Ab `fca3f01c6fec321212ae608173d9cf6184eec2d1dfe19ed1a309fa1f39157bcb` ;
- hors liste de la consigne, lus et déclarés : G1 brouillon 4 `ad068beda59d5cb88fb6303dc9946fa27330c5e24654850745bd9c2ab6f6bbad` ; rapport de niveau 1 des voisins de H2 `92c0b4a918ee42ffed2e7103ead917015e93c455be552fcd01c6802763f527d2` ; `prereg/agregation-r1-v4-v1.md` `5916e62e5bce4a3db19e24bbdd43664c583dd6370f4ea766ae8045d61fc35015` ; `prereg/analyse-par-episode-v1.md` `26a3ff72e3a39636d3bdb965971fd1b237a04acc133a31a42f9a695d6d5970a4` (empreinte seulement) ; verdict de P3 v2 `05e896daed17cdb089cd10641878a5014b505eab0aa3d45d0dd7a60d87435751` ; texte de validité de l'adaptateur brouillon 3 `defd8ef05038e703c24733f6a5f88a1153daf5f44d2b8cae14950a5643e875fd` ; gabarit `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` ; `src/controle_ia/prereg.py` `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` ;
- code lu : `registre_v1.py` `e50236574fbcd7e48ea3005eadc8bdb68d2c753d10028db7f2c365648a843cec` (égale à la valeur `e5023657…` que T0.7 brouillon 22 donne au commit `37485ce5`) ; `lecture_v2.py` `709b2febac4bcee308b66400764d7ed87115dd991c4ab79f57467d1464d7c69e` (égale à `709b2feb…` du brouillon 22) ; `lecture_v1.py` `62b34790346123924c275c4e2021ea31db26837c5b7840e9e047d272a54c9678` ; `criteres_v1.py` `12b999fecce093372a29fb70d8c11eb7fe965f34c8746a31b399baaecc5ae8c5` (égale au préfixe `12b999fe…` du brouillon 22) ; `plancher_v1.py` `ac6e8263293ed30c807ef91f8eab0adbcbf8e1b91d5e4c56e73dbffa1a7099dc` ; `sondes/evaluation.py` `1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3` ; `sondes/temoins.py` `3b051b6fc2d78eeb4a44aab8a385bbce65095998e944b80e5f2a66e21b57faf7`.

## 3. Lectures (ce qui a été ouvert, rien d'autre)

- Consigne entière ; rapport des prémisses entier ; registre des décisions : R-2128 à R-2137 (dont R-2171, R-2175) et la tête tronquée des 25 dernières lignes (R-2232 à R-2256 : titres, chemins ; aucun résultat de sonde) ; `registres/scellements-v1.md` (quatre lignes).
- T0.7 brouillon 22 : l. 1-175 (en partie, sortie tronquée), 553-660, 871-1430, 1681-1830, 1902-1960, 1994-2119, 2360-2375, 2676-2702 ; recherches ciblées (`grep`) sur le seul fichier.
- T0.6 scellé : recherches ciblées et l. 491-500 ; configuration de 7b (champs scalaires).
- Base (A) : titres de sections et « Ordre des lectures et embargo ».
- Programme v2 : recherche ciblée (H1, H2, G1, séquentiel) ; N-007/N-008, N-054, N-055, N-056 entiers ; G1 brouillon 4 entier.
- Rapport lot 3 Ab : l. 1-120 et recherches ciblées ; rapport de niveau 1 des voisins de H2 : recherches ciblées (l. 27-30, 97-210).
- `prereg/agregation-r1-v4-v1.md` : texte entier (préenregistrement scellé ; **aucune sortie**, ni `diag/`, ni `runs/`, ni ligne de registre qui en rapporte une issue).
- Verdict de P3 v2 : l. 205-216.
- Texte de validité de l'adaptateur, brouillon 3 : l. 1-30, 95-130, 232-262 et titres.
- Code (lecture seule) : `registre_v1.py` entier ; `lecture_v2.py` l. 236-275, 1028-1062, 1100-1130 ; `lecture_v1.py` l. 850-880 ; `criteres_v1.py` l. 420-490 ; `plancher_v1.py` l. 102-127 ; `sondes/evaluation.py` l. 21-66 ; `sondes/temoins.py` l. 182-215 ; `prereg.py` entier.
- Recherches : `git grep` avec les exclusions de la règle 9 des interdits communs (motif « cascade », « 2607.06503 ») ; `grep` sur des fichiers nommés seulement ; aucune recherche récursive sur un dossier contenant un chemin interdit.
- **Jamais ouvert** : `diag/`, `runs/`, `donnees/` (hors le fichier `donnees/20261007-082440-t05-extraction/taches-evaluation.json`, dont seules les clés de tête ont été lues) ; rien de 7a ; aucun fichier de P3-bis ; aucune branche.

## 4. Choix du rédacteur (routine, déclarés ; aucun ne touche H1, G1 ni le mode tenu à l'écart, sauf les deux nœuds)

1. **Une seule statistique accumulée** (somme des dix scores d'action), **un seul comparateur** (maximum par épisode), fixés avant toute donnée : la forme additive de H2 (N-007) la plus simple, sans réglage ; à horizon fixe, sans calibrage ni honnêtes réservés. Écartés : somme de Page (exige une ligne de base estimée sur l'honnête, donc un partage des épisodes), processus e (exige une loi), moyenne glissante, dernier état (base (iii) de N-056 : écarté pour ne pas la lire avant G1).
2. **Jeux décisifs** : (i-a) seul pour (i) ; pour (ii), **séquence fixée** `S100`, `S75`, `S50`, `S25` : contrôle du taux d'erreur de famille sans partager le niveau entre doses ; ordre choisi parce que le signal est attendu décroissant avec la dose (T7-P17 de T0.7). Les marques de dose de N-063 (jugée, hors jugement) sont **recopiées, jamais aiguilleuses** : le barreau 6 n'est pas le critère 3 ; la phrase dit, à une dose hors jugement, que le texte seul y sépare déjà.
3. **Niveau** : celui de T0.7 (`niveau_applique`), Bonferroni sur les sondes lues.
4. **Plancher d'épisode** : les 200 directions de `plancher_<k>` déjà notées par T0.7, agrégées comme la sonde ; quantile 0,95 ; aucun tirage neuf.
5. **Prédicteurs triviaux d'épisode** : transposition de la règle « non interprétable » de T0.7 (somme des `jetons_notes`, nombre d'actions à `mention_etendue`) ; raison : le maximum sur les jetons d'une action croît avec sa longueur, et la somme des dix maxima aussi.
6. **Témoins** : `T100` contre `honnete` (adaptateur sans sabotage), `temoin` contre `honnete` (consigne sans sabotage), `S100` contre `T100` (à adaptateur égal) ; Δ des 200 directions ; familles génériques et spécialisée séparées (N-054 point 3).
7. **Exclusion** : tâche retirée d'un jeu si l'un de ses deux épisodes n'a pas dix actions notées à scores finis ; plus de 6 sur 64 → échec (même seuil que `agregation-r1-v4-v1`).
8. **Registre propre**, marque `ACCB6` (section 5) ; antériorités : scellement strictement avant `SCORES-T07` (exigé) ; code strictement avant la première ouverture des scores par T0.7 (sinon réserve) ; visé : avant la création de 7b.
9. **Aiguillage** calqué sur le texte de validité de l'adaptateur (G-1 à G-4), pour fermer ce que T0.7 ferme.
10. **Aucune base boîte noire**, même en descriptif (H1).

## 5. Essai des clés de registre (marque `ACCB6`)

- Script : `brouillons/accumulation-barreau6-v1/essai_cles_registre_b6_v1.py` ; sortie : `essai-cles-registre-b6-v1.txt` (empreintes en section 8) ; lancé `cd /tmp && .venv/bin/python -I -B <chemin absolu>`, code 0, le 10 novembre 2026 à 15:57:32 UTC ; registres jouets dans un dossier temporaire effacé ; `registres/scellements-v1.md` lu, jamais écrit (empreinte au moment de l'essai : `3e90a69a38582c35eff4b6af74b135f58fd4dfea31b1763f50a99af0db3df373`).
- Résultat : `classer_cle_inconnue` (liste fixée `T06`, `T08`, `P3BIS`, `NARC`) rend « refus » pour `SCELLEMENT-ACCB6`, `CODE-ACCB6`, `LECTURE-ACCB6`, `SCELLEMENT-ACCUMULATION-B6` (exemple de la consigne) et `SCELLEMENT-B6-T07` ; « ignorée » pour `SCELLEMENT-ACCUMULATION-B6-T08` et `-T06` (écartées : fausse attribution). Registre jouet (lignes présentes + `RUN-CONFIRMATION-T06` fictive) : étape A lue sans refus (cas sain) ; avec une ligne `SCELLEMENT-ACCB6` ajoutée : refus de l'étape A, motif « ligne SCELLEMENT-ACCB6 ni exigée ni permise à cette étape » (artefact) ; à l'étape B, le cas sain refuse déjà (clés exigées encore absentes) et l'artefact y ajoute ce motif.
- **Conclusion** : toute clé de ce texte dans `registres/scellements-v1.md` ferait refuser T0.7 ; une marque `T07` aussi ; d'où le registre propre `registres/accumulation-b6-v1.md` (même solution que `VADAPT`), sans changer la liste des marques de T0.7.

## 6. Simulation de puissance

- Script : `brouillons/accumulation-barreau6-v1/puissance_accumulation_b6_v1.py` ; sorties `puissance-accumulation-b6-v1.json` et `puissance-accumulation-b6-v1.txt` (empreintes en section 8).
- Lancement : `cd <bac à sable> && /home/user/controle-ia-travail/.venv/bin/python -I -B <chemin absolu du script> <chemin absolu du .json> > <chemin absolu du .txt>` ; numpy 2.4.6, scipy 1.17.1, Python 3.13.16 ; début 15:50 UTC ; fin 16:06:42 UTC, code 0, 974,7 s ; 105 cellules (dont 63 non atteignables, a ≥ 0,5 + q/2), 6 scénarios de séquence.
- Une modification avant le lancement complet, déclarée : le produit `einsum` des tirages remplacé par un produit matriciel équivalent (`(w @ c) * w`), plus rapide ; résultats identiques sur l'essai rapide (même graine).
- Lois gaussiennes **supposées** ; aucune donnée lue ; résumé dans la section « Puissance » du brouillon.
- **Ce que la simulation dit** (résumé ; table complète dans le brouillon, section « Puissance ») : le gain de la somme sur le maximum dépend surtout de la **corrélation intra-épisode** : sans effet d'épisode, P(A) ≥ 0,58 dès une aire par action de 0,60 ; à corrélation 0,2, P(A) ≤ 0,45 (0,04 à 0,17 pour une aire de 0,60 à 0,70) ; à 0,5, ≤ 0,18 ; si la moitié seulement des actions porte un décalage fort, le maximum bat la somme (P(M) jusqu'à 0,83 à 1,00). **Conséquence dite avant lecture** : l'issue la plus probable du barreau 6 est « non établi à cette puissance » ; « le maximum bat » est plausible pour (ii). Aucun remède sans dépense ni changement de métrique n'a été retenu (R3 : rien n'est réglé pour obtenir un signe).

## 7. Nœuds et questions

- **N-B6-1** (G1, N-054 point 4) et **N-B6-2** (base (ii) de N-056) : écrits dans le brouillon, section « Nœuds pour Lazar » ; recommandation (a) pour les deux ; pas de défaut.
- **Q-B6-1** : `agregation-r1-v4-v1` a-t-il été lancé et lu ? Si oui, ses descriptives D1 (`Gt`, `Ge` : somme contre maximum sur (i-a) de P3, mêmes sondes figées, 60 tâches dont la plupart sont parmi les 64 de 7b) sont un précédent proche de B6-P1 : la mère dit qui les a vues (le rédacteur non) et le contre-lecteur ne doit pas les avoir vues.
- **Q-B6-2** : registre propre (recommandé) plutôt qu'une marque ajoutée à la liste fixée de T0.7 (qui toucherait T0.7 et sa configuration).
- **Q-B6-3** : qui écrit le code (développeur neuf) et quand : pour sceller avant la création de 7b (12 ou 13 novembre, R-2177), le texte peut être scellé avant le code ; la ligne `CODE-ACCB6` doit précéder la première ouverture des scores par T0.7.
- **Q-B6-4** : vérificateur du résultat (sous-agent neuf, non lecteur de P3-bis).

## 8. Fichiers rendus et empreintes

Validation : `PYTHONPATH=src .venv/bin/python -c "from controle_ia.prereg import problemes; …"` sur le brouillon scellé : une seule ligne, « marqueurs de gabarit restants : `CHEMIN_RAPPORT_CL1_ACCB6`, `COMMIT_CODE_ACCB6`, `DECISION_N_B6_1`, `DECISION_N_B6_2`, `EMPREINTE_RAPPORT_CL1_ACCB6`, `EMPREINTE_RELU_CL1_ACCB6`, `ENTROPIE_ACCB6`, `ENUMERATION_ETATS_ACCB6`, `REVERIFICATION_T07_SCELLE` » (marqueurs exceptés, conforme à la consigne).

| fichier (sous `brouillons/accumulation-barreau6-v1/`) | sha256 (égal au compagnon `.sha256`) |
|---|---|
| `accumulation-barreau6-v1-brouillon1.md` | `a2d8186340fc3cd6f9fc16ab46ca81e741ce75361e43e9e34b899061a2f60c2f` |
| `puissance_accumulation_b6_v1.py` | `ccc5310b477ddac67d01dd11653ebb3117ed5cb303ee4c118d9069fc5a694079` |
| `puissance-accumulation-b6-v1.txt` | `64fd8ebffede3962e43128db1de4ae454380ddd22372a7fdfaf8091a55f00585` |
| `puissance-accumulation-b6-v1.json` | `5f9f598fd8fca05d706bce78faf4a68fe08fbf91a56b314b07cefbe896987223` |
| `essai_cles_registre_b6_v1.py` | `7a4dd7158f29fbf2c8ce762c2b9d86124c16007125fc3b81d864fa4de8bd9de6` |
| `essai-cles-registre-b6-v1.txt` | `0568f6fe0b163f6fc9018ab6a7c66061cba319081eb4e0979eeb5abcaeb4ceda` |
| ce journal | compagnon `.sha256` écrit au scellement, après cette ligne |

Bac à sable (non versé) : `essai_rapide.py`, `essai_calibration.py`, première version de l'essai des clés et sa sortie, registres jouets (effacés par la version versée).
