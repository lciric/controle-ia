# RENDU — fille 10 — chaîne de la course v12 et candidat 12 — v1

Branche `prep/t06-course-v12`, partie de `prep/t06-bras-b-v4` (`84a62edd…`, elle-même partie de `c01d29ea0d5c29b584f23cc63e1aac9aaefcef66`, commit d'épreuve E3 bis v3). Écrit le 2026-11-08 par la fille 10 (Claude Sonnet 5.5). Aucun `.sha256`, aucune clé lue, aucune dépense, rien sur `main`.

## Ce qui a été fait (décision de la mère, ~06:29Z : « oui, construis avec le candidat 12 l'amorce v10 (défaut `bras_b_v4`), la liste figée v2 et le lanceur v12 »)
Rien de ce que cite l'ordre scellé d'E3 bis v3 n'a changé (amorce v9 `6a6897ce…`, liste v1 `562b65fa…`, lanceur v11, `config-t06-epreuve-e3bis-v3.json`) : la course a son propre trio de noms neufs (R12).
- **Lanceur v12** (`scripts/lancer_t06_v12.sh`) = lanceur v11 + `T06_TESTS_ATTENDUS` validé `^[0-9]*$` (une valeur comme « 7 -e PYTEST_ADDOPTS=-x » est refusée avant toute commande ; 9 valeurs artefacts) ; cite l'amorce v10.
- **Amorce v10** (`scripts/amorce_instance_t06_v10.sh`) = amorce v9 + `bras_b_v4` par défaut + liste v2 (trois lignes changent ; vérifié par un essai) ; « AMORCE T06 v10 DEMARRAGE ».
- **Liste figée v2** (`scripts/tests-cibles-t06-v2.txt`, 83 fichiers, empreinte écrite en dur dans l'amorce v10) et exclusions motivées v2 (`scripts/tests-exclus-t06-v2.txt`, 50). Les 10 fichiers d'essais de la chaîne v11 (amorce, bras B de l'amorce, liste, minuterie, nouveaux_v10, r5, scripts, instances nulles, session_v11, plafond E3 bis) sont copiés en `tests/test_t06_v12_*.py` sur la chaîne v12 ; les originaux sont exclus avec motif. `tests/test_bras_b_v4.py` est listé.
- **Essais des trois réserves de la contre-lecture de la v11 (v2)** : `tests/test_t06_v12_course.py` (15) : `T06_TESTS_ATTENDUS` (4 valeurs saines, 9 refusées) ; **mutation L2** : la création d'E3 bis reverifie la ligne GO-2026-11-06-01 au registre (supprimée du registre → refus ; mutation de la vérification tuée) ; amorce v10 = v9 + 3 lignes. **Banc strict** (`scripts/banc_mutations_bras_b_v5.py` + `tests/test_banc_mutations_bras_b_v5.py`, 9) : une mutation n'est « tuée » que par le code 1 de pytest ; le code 5 (filtre `-k` vide) invalide le banc ; 21 mutations tuées sur 21, témoin non muté réussi, aucun filtre vide.
- **Candidat 12** (`brouillons/T0.6-organismes-v0-v1-candidat12.md`, par couples V1 à V8 depuis le candidat 11 `9a1e2bcf…`, générateur et journal dans `brouillons/T0.6-organismes-v0-v1-candidat9-pieces/`) : cite lanceur v12, amorce v10, `session_v11`, `lanceur_v5`, `configuration_v5`, bras B v4, liste v2, addendum v3, configuration d'E3 bis v3 ; cinq marqueurs inchangés.

## Valeur relevée à E3 bis (message de la mère ~07:01Z, compte rendu 2 de la fille 6) — À DÉCIDER POUR LE CANDIDAT
Dernière ligne exacte de la suite ciblée **liste v1** sur l'A100 de 80 Go : « 1878 passed in 4009.60s (1:06:49) » (aucun échec ni saut). **Ma mesure locale de la liste v1 était 1 878 : égalité exacte local = instance.** La course jouera la **liste v2**, qui compte **1 914 essais** en local (83 fichiers) : `T06_TESTS_ATTENDUS=1878` ne conviendrait pas à la course (l'amorce exige « N passed » avec N exact). Le marqueur `<<TESTS_ATTENDUS_T06>>` reste dans le candidat 12, non rempli. Deux voies pour la mère : (a) 1 914, dérivé de l'égalité local = instance observée sur la liste v1 (réserve : non relevé sur l'instance pour la liste v2) ; (b) relever la liste v2 sur une instance avant la course. **Durée mesurée de la suite : 67 minutes sur l'instance** (2,1 To de mémoire vive, 255 cœurs), contre mes 40 à 50 estimées : à porter dans le calendrier et le devis de la course (la liste v2 a ~2 % d'essais de plus).

## Dernière ligne exacte des essais (Python 3.11.18, torch pour processeur, trois tranches en parallèle, liste v2)
**591 passed in 750.35s (0:12:30) ; 728 passed in 1502.49s (0:25:02) ; 595 passed in 667.10s (0:11:07)** → 1 914 essais, **0 échec, 0 sauté**. Banc : « 21 mutations tuées sur 21 (témoin non muté réussi) ».

## Table des empreintes (sha256 ; 16 premiers caractères)
| fichier | sha256 (16) |
|---|---|
| `scripts/lancer_t06_v12.sh` | 8b91be979fac2695 |
| `scripts/amorce_instance_t06_v10.sh` | 69b669e176e5cb09 |
| `scripts/tests-cibles-t06-v2.txt` | 417f637e0db2657e |
| `scripts/tests-exclus-t06-v2.txt` | 01924bbf1e5600d0 |
| `scripts/banc_mutations_bras_b_v5.py` | c2e3efe3bbec6a65 |
| `tests/test_banc_mutations_bras_b_v5.py` | 4ea223e5862e374c |
| `tests/test_t06_v12_course.py` | 5d5cbf76e599a1fb |
| `tests/test_t06_v12_liste.py` | 7f8836b3980768dc |
| `tests/test_t06_v12_amorce.py` | c925281f13c5cb3c |
| `brouillons/T0.6-organismes-v0-v1-candidat12.md` | 379328fa97638a6c |
| `brouillons/T0.6-organismes-v0-v1-candidat9-pieces/appliquer-candidat12-v1.py` | a3d7227083d183c6 |
| `brouillons/T0.6-organismes-v0-v1-candidat9-pieces/journal-candidat12-v1.md` | d4273bd4328d6d9f |
| `src/controle_ia/t06/session_v11.py` | c398985963c375c5 |
| `src/controle_ia/t06/lanceur_v5.py` | 17efa88170f74956 |
| `src/controle_ia/t06/configuration_v5.py` | 0f75e16f32e2e1ec |
| `src/controle_ia/audit_fuite_r1_v4/bras_b_v4.py` | 317a7ea551abace1 |
| `docs/notes/g0-deux-semaines-v1/bras-b-v2/addendum-bras-b-v2-brouillon-v3.md` | 2ec90141f10be13d |
| `docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e3bis-v3.json` | b725c16fd9783fce |

## Réserves
Amorce v10, lanceur v12, `lanceur_v5`, `session_v11`, bras B v4 jamais joués sur une instance (E3 bis joue la chaîne v11/amorce v9) ; liste v2 non relevée sur l'instance ; durée de la suite plus longue que prévu (67 minutes) ; addendum v3 non contre-lu ni scellé ; borne de l'annexe du bras B toujours 2 400 s dans l'amorce (le pire cas d'environ 5 800 s est à écrire à l'ordre de la course) ; l'ordre de la course doit citer « motifs=28 » (et non 27) ; candidat 12 non contre-lu.
