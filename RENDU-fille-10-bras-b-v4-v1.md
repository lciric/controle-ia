# RENDU — fille 10 — bras B v4 (GO-2026-11-08-01) et addendum v3 — v1

Branche `prep/t06-bras-b-v4`, partie de `c01d29ea0d5c29b584f23cc63e1aac9aaefcef66` (commit d'épreuve E3 bis v3 de la mère ; elle-même sur `prep/t06-v11`, rendu 4 = `2848642e`). Écrit le 2026-11-08 par la fille 10 (Claude Sonnet 5.5). Aucun `.sha256`, aucune clé lue, aucune dépense, rien sur `main`.

## Ce qui a été fait
Décision de Lazar (GO-2026-11-08-01, verbatim) : « Je recommande 0,3 et la lecture stricte. go ».
- **Bras B v4** (`src/controle_ia/audit_fuite_r1_v4/bras_b_v4.py`, nom neuf, R12 : v1, v2, v3 intactes) : `TOLERANCE_SCORE = 0.3` (log-cote, sur le score de W, borne incluse) ; lecture stricte du « sinon » de GO-2026-11-07-09 (même carte A100-SXM4-80GB et mêmes versions torch 2.14.1 / transformers 5.18.0 que le rejeu de R1 v4 : tout écart au bit arrête ; la tolérance ne vaut que sur une autre carte ou d'autres versions). Rien d'autre ne change ; sortie scellée `audit-fuite-r1-v4-bras-b-v4`.
- **Essais** (`tests/test_bras_b_v4.py`, 44) : copie des essais v3 plus : valeur exactement 0,3 ; borne incluse (0,3 passe, 0,3 + 1e-9 arrête) ; lecture stricte (un pas de float16 sans écart de score arrête sur la même carte, passe sur une autre) ; `identite_exigee_au_bit` (même carte et versions, autre carte, autre version, version absente, carte vide) ; bout en bout dans le monde jouet (bruit de 1e-3 : arrêt « G4 … au bit »).
- **Banc de mutations** (`scripts/banc_mutations_bras_b_v4.py`) : **21 mutations tuées sur 21, témoin non muté réussi** (M1 à M11 de la v2, X3 à X10 de la v3, plus M12 tolérance retombée à 0,15, M13 borne exclue, M14 lecture stricte retirée).
- **Addendum v3** (brouillon, `docs/notes/g0-deux-semaines-v1/bras-b-v2/addendum-bras-b-v2-brouillon-v3.md`) : 0,3 et lecture stricte, à sceller par la mère avant toute lecture du bras B ; justification de 0,3 (3,3 fois le pire écart bfloat16 simulé 0,090 ; de l'ordre de la dispersion entre plis 0,28 à 0,35 ; ±0,5 sur les scores déplace les aires d'au plus 0,0004) et limite déclarée (le bras B peut s'arrêter sur H200 NVL sans défaut réel).
- **Registre des cibles invisibles** : entrée pour `bras_b_v4.py::_executer` dans `tests/test_cibles_invisibles_v2.py`.

## Ce que je n'ai PAS touché (l'ordre scellé d'E3 bis le cite)
`scripts/amorce_instance_t06_v9.sh` (`6a6897ce80c5c2cd…`, joue encore `bras_b_v3` par défaut), `scripts/tests-cibles-t06-v1.txt` (`562b65facf1bcbf7…`, empreinte écrite en dur dans l'amorce), le lanceur v11. `tests/test_bras_b_v4.py` est donc **exclu avec motif** de la liste figée (`scripts/tests-exclus-t06-v1.txt`) : il sera listé par la liste de l'amorce de la course. **Conséquence à décider par la mère : pour que la course joue le bras B v4, il faut une amorce v10 (défaut `bras_b_v4`) et une liste v2 (nom neuf) ; E3 bis ne lance pas le bras B.**

## Dernière ligne exacte des essais (Python 3.11.18, torch pour processeur, trois tranches en parallèle)
Liste figée (81 fichiers) + `tests/test_bras_b_v4.py` : **627 passed in 1068.09s ; 714 passed (+ 1 échec corrigé, rejoué : 21 passed) in 1119.78s ; 580 passed in 714.64s** → 1 922 essais, **0 échec, 0 sauté**. (L'échec de la tranche 2 : `test_cibles_invisibles_v2.py::test_inventaire_tout_constructeur_d_invite_est_examine`, entrée manquante pour `bras_b_v4`.) La seule ligne opposable pour `TESTS_ATTENDUS_T06` reste celle relevée sur l'instance à E3 bis.

## Table des empreintes (sha256 complets des fichiers à ce commit ; 16 premiers caractères)
| fichier | sha256 (16) |
|---|---|
| `src/controle_ia/audit_fuite_r1_v4/bras_b_v4.py` | 317a7ea551abace1 |
| `tests/test_bras_b_v4.py` | b03a4de8b95f968f |
| `scripts/banc_mutations_bras_b_v4.py` | 16cd7d561aedd515 |
| `docs/notes/g0-deux-semaines-v1/bras-b-v2/addendum-bras-b-v2-brouillon-v3.md` | 2ec90141f10be13d |
| `scripts/tests-exclus-t06-v1.txt` | 5fc2d5dbb016d35b |
| `tests/test_cibles_invisibles_v2.py` | 61c7b74463b833a3 |
| `scripts/tests-cibles-t06-v1.txt` (inchangé) | 562b65facf1bcbf7 |
| `scripts/amorce_instance_t06_v9.sh` (inchangé) | 6a6897ce80c5c2cd |

## Réserves
Bras B jamais joué sur une carte ; amorce, lanceur et `lanceur_v5` jamais joués sur une instance ; tolérance 0,3 justifiée par des bruits simulés (non propagés à travers 15 couches) ; addendum v3 non contre-lu ; amorce v10 + liste v2 + lanceur v12 (validation de `T06_TESTS_ATTENDUS`, essai de la vérification de GO-2026-11-06-01 à la création, banc strict sur le code 5 de pytest) à faire pour la course, avec le candidat 12.

## Suite (annoncée à la mère)
Candidat 12 par couples (cite `session_v11`, bras B v4, configuration d'E3 bis v3), puis chaîne de la course (amorce v10, liste v2, lanceur v12).
