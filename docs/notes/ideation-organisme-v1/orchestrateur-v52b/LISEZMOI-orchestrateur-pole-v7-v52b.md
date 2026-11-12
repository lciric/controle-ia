# Orchestrateur du pôle, version 52b — correction de CL16-01 (borne mémoire minimale du bac)

- Date : 2026-10-30, 23:20 UTC. Auteur : sous-agent de la lignée « session-depot » (Claude Opus 5.5). Non contre-lu (R2 à faire).
- Base : la v52 telle quelle (liste `EMPREINTES-orchestrateur-pole-v7-v52.txt`, `13bc34c7…`, vérifiée). Aucun fichier de la v52
  n'est modifié (R12) : trois fichiers **nouveaux** et ce LISEZMOI.
- Aucun appel payant, aucune clé, aucun réseau (essais joués sous `unshare -n`).

## Le constat (CL16, `docs/notes/ideation-organisme-v1/contre-lecture-cl16-orchestrateur-v51-v1.md`)

À la borne minimale que la version 2 de l'étage autorise (`MEMOIRE_BAC_MIN_MO = 512`), la sonde des privilèges `disponible()`
est tuée par le groupe de contrôle du bac (code 137) : l'étage est refusé dans la configuration minimale documentée. Ferme sans
risque, mais bloque. La v52 ne l'a pas corrigé (`pole/tests_de_mort_v2.py` identique octet pour octet à celui de la v51).

Reproduit dans cette session (vrai `bwrap` 0.9.0, noyau Linux 6.18.44, cgroup v1, noyau superutilisateur, utilisateur dédié
64097, sous `unshare -n`) : 512, 544, 576, 608 Mo refusés (code 137, 2 ou 3 passages chacun) ; 640, 768, 1 024 Mo acceptés.

## La correction (la première de CL16 : relever la borne, plus un essai réel à la borne)

| fichier | rôle | SHA-256 |
|---|---|---|
| `pole/tests_de_mort_v3.py` | la version 2 telle quelle (mêmes objets) ; `MEMOIRE_BAC_MIN_MO = 768` ; `ExecuteurBacASable` sous-classe dont `verifier_outils` refuse sous 768 Mo, motif CL16-01, avant la sonde | `ea05eb55f9d179501fb091d25298deaf36cd66ad16fd65bdca4dcf5e4ba74bba` |
| `demonstrations/ideation_v4.py` | le lanceur v2 tel quel, chargé à part ; sur cette instance seulement, l'étage est la version 3 et le vrai bac est toujours construit par le lanceur (la v2 laissait le cœur construire le bac v2 par défaut sans option du bac) | `4212d4c9d014a265847d4c4ed87a8cd804fdafa73f85fd8947874d63fca1c36d` |
| `essais/test_v52b_borne_memoire.py` | 4 essais : garde (cas sain à la borne, artefacts à borne − 1, 512, 608) ; **sonde réelle à exactement la borne**, 3 passages, rien ne reste ; lanceur v4 ; égalité v3 = v2 sauf la borne (R12) | `5e5132b9f98cbf8debad02f7b9d74e8322b54fbcce69f2ba6f866d88ed1c2cc5` |

768 = la plus basse borne mesurée qui tient (640) plus 20 % de marge. Pour l'étage : `demonstrations/ideation_v4.py`.

## Ce qui reste

- **SUPPOSÉ** : la marge tient sur la machine louée jetable (autre noyau, peut-être cgroup v2). `test_v52b_02` est à rejouer
  là-bas, avec la mémoire de production, avant tout GO de l'étage (et CL17-étage sous `bwrap` réel).
- Les lanceurs v1, v2 (et le cœur appelé directement, sans exécuteur donné) gardent la borne de 512 Mo de la version 2 : l'étage
  y est refusé, sans risque (CL16-01, CL16-02). Le lanceur v3 (juges seulement) refuse `--tests-de-mort`.
- Non traité : la cause fine (pourquoi le processus racine de la sonde meurt sous 640 Mo malgré `oom_score_adj = 1000` chez les
  enfants) ; CL16-02, CL16-03 ; CL17-01 à 07.
