# Complément 2 au rapport du développeur — barreau 6 (`ACCB6`) : garde de non-relance — v1

- **Auteur** : le même développeur neuf (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Mêmes exclusions que dans le rapport (§ en-tête).
- **Consigne** : message de suite de la mère (R-2275), même consigne (`consigne-code-accb6-v1.md`, `48b502d0…`), mêmes interdits. Rapports précédents gardés tels quels (R12) : `rapport-developpeur-accb6-v1.md`, `2a6880e4…`, et `rapport-developpeur-accb6-v1-complement-v1.md`, `02d837c9b22c5da31d1694b25ddcb6604877e4aa119df8edb8c5953f0df09e5a`.
- **Texte qui pose la garde** : candidat 1 du barreau 6 (commit `d5a0de65c` de `main`), lu par `git grep` restreint à `brouillons/accumulation-barreau6-v1`. Couples C1-12 (plan, point 2 : « `diag/<run>/arret-accb6.json` d'un run quelconque déjà présent → refus, code 2, nœud : aucune relance après un arrêt (code 3) sous ce texte ») et C1-13 (liste d'arrêt).
- **Heures (UTC, relevées par `date -u`)** :
  - arbre recréé à partir de 19:57 ;
  - banc de 20:00:40 à 20:25:05 ;
  - commit 20:25:16 ; poussée 20:25:19 ;
  - complément écrit à partir de 20:26.
- **Verdict en une ligne** : garde de non-relance ajoutée dans `garde_v1.garde` (refus, code 2, avant tout calcul). 168 essais passent, l'énumération rejouée est égale à l'octet, et le banc tue 67 mutations sur 67. **Commit final proposé pour `COMMIT_CODE_ACCB6` : `5ee8a4ac8712221a31599e2a92dfbae981cc5704`.**

## 1. Commit final proposé pour `COMMIT_CODE_ACCB6`

- **`5ee8a4ac8712221a31599e2a92dfbae981cc5704`**, branche `prep/accumulation-b6-code-v1`, parent `56c624ddb02941e09ff5bb96d8c848214e6b576a`. Le commit est poussé et la tête distante vérifiée égale. Aucune fusion. Arbre `src/` : `a0b1823b3dd575744c2be750ba480a4b683e5ef3` ; arbre du paquet : `367b3a9da01f7cfda90c5c0ea4d09d12eb509c57`.
- **Le fichier de `CODE-ACCB6` change** : `garde_v1.py` a changé. Un fichier écrit pour `56c624dd…`, s'il a déjà été inscrit (R-2274), ferait refuser la lecture sur ce commit ; c'est exactement l'artefact « empreinte au commit et dans le paquet importé ». Il faut écrire un fichier neuf avec `python -m controle_ia.accumulation_b6.code_accb6_v1 ecrire DEPOT 5ee8a4ac… SORTIE`, le sceller, puis inscrire une ligne `CODE-ACCB6` à ce commit, selon les règles d'antériorité du texte.
- **Contrôle réel** fait par ce développeur. `ecrire` a été lancé sur l'arbre recréé au commit `HEAD`, avec une sortie dans le bac à sable. `controler_code` a ensuite été lancé sur le paquet effectivement importé (`/home/user/wt-accb6/src/controle_ia/accumulation_b6`). Résultat : **conforme**, 6 fichiers, tête = `5ee8a4ac…`. Ce fichier d'essai a été effacé : son entropie ne doit pas servir.

## 2. Arbre de travail

- L'arbre a été recréé selon la consigne de suite :
  - `git worktree add --no-checkout /home/user/wt-accb6 prep/accumulation-b6-code-v1` ;
  - `git sparse-checkout init --no-cone` ; à cette étape, le fichier `info/sparse-checkout` de l'arbre portait déjà `/*` et `!/docs/notes/bras-attaque/`, et rien n'était extrait ;
  - motifs écrits : `/*`, `!/*/`, `/src/`, `/tests/`, `/scripts/`, `/brouillons/accumulation-barreau6-v1/` ;
  - `git checkout`.
- Vérifié : `docs/` absent de l'arbre, donc `docs/notes/bras-attaque/` n'a jamais été extrait. Arbre propre, à jour avec `origin`.
- L'arbre est retiré à la fin, propre et poussé (§ 7).

## 3. Ce qui change

- `src/controle_ia/accumulation_b6/garde_v1.py` (**modifié, déclaré** ; la garde d'ouverture est dans ce fichier) : la garde relève aussi `diag/*/arret-accb6.json`, d'un run quelconque. S'il y en a un, elle ajoute le motif « … déjà présent : aucune relance après un arrêt (code 3) sous ce texte : refus, nœud ; une lecture après un arrêt demande une version neuve du texte ». Comme les autres motifs de la garde, il est relevé avant d'être rendu : une ligne `REFUS-ACCB6` au journal propre, puis `RefusAccb6`, code 2. Le refus a lieu avant le contrôle du code, avant l'aiguillage et avant tout calcul ; aucun run n'est créé. En-tête du module mis à jour.
- `tests/test_accb6_relance_v1.py` (**neuf**) :
  - **cas sain** : un `arret.json` de T0.6 ou un `arret-etape-b.json` d'un autre run de T0.7 ne déclenchent pas cette garde ;
  - **artefact** : `arret-accb6.json` sous un run quelconque → refus, ligne `REFUS-ACCB6`, rien d'autre d'écrit ;
  - **de bout en bout** : une lecture s'arrête après le manifeste (code 3, aire par action en écart de 2·10⁻⁹). Sa relance est refusée (code 2) sans appeler le contrôle du code ni `lire_e4`, et sans run neuf. La commande rend aussi 2, avec le motif.
- Aucun autre fichier touché.

## 4. Empreintes (sha256, au commit `5ee8a4ac…`)

| fichier | sha256 |
|---|---|
| `src/controle_ia/accumulation_b6/__init__.py` | `72bc176fcd0df9f2d4bc241b0b9c7696558f308b8516916496cb821b40786d7e` |
| `src/controle_ia/accumulation_b6/code_accb6_v1.py` | `2e6c3bb878cbc9996335527f74257cc57392b13d0487fa3bace219a260e55c02` |
| `src/controle_ia/accumulation_b6/etats_v1.py` | `90a1c20be99edda781b78ce26a05e28582e9cccb151c365d247fc0cd72bcdbd8` |
| `src/controle_ia/accumulation_b6/garde_v1.py` (modifié) | `2885c1f49958ce8ff4c20b3e8283051de9c03e3b0ab3f864a509bc49de80928e` |
| `src/controle_ia/accumulation_b6/lecture_v1.py` | `70764f664ffb9670baa88000323cccfc440d4387c9bcea9a6e7baefdb474e6c8` |
| `src/controle_ia/accumulation_b6/phrases_v1.py` | `9376fcc05337d4979a3f40acc3b2e84ecdb03fb528c24b3d6c3e3bc4bfb9f228` |
| `tests/test_accb6_relance_v1.py` (neuf) | `cc458330b2d3b7731c5a571ee71baf0a2e8eedf6a1d0521fbdc521d166ff3a0d` |
| `tests/test_accb6_code_v1.py` | `a4cc477e51e7e3126d747d2acf2790bd36036444a25f23860c35450ce770c1b8` |
| `tests/test_accb6_etats_v1.py` | `d0cf205e7d48371ce8e744193f5c392bb4d206ba11bece065dd6c09f42b6f7c2` |
| `tests/test_accb6_garde_v1.py` | `448eb2d3630985ea1224c27b4c39949bb3bdec3fd626c9eaf8c8952e43f4ce53` |
| `tests/test_accb6_lecture_v1.py` | `bd890cd86462d1beb7af73b25e4bd38835f2d4ae126c4fb9550946c80a77fd3d` |
| `scripts/enumeration_etats_accb6_v1.py` | `d7b6fa08f02c0b494f58aca7803099240baf28723a93334235701cb5594a431f` |
| `scripts/enumeration-etats-accb6-v1.txt` | `3bde500f1eca8ceb5e95b782ea74312cace981d019d8fef6ead7944341abf5a6` |

La liste que `ecrire` donne au commit `5ee8a4ac…` est faite des six premières lignes de la table.

## 5. Essais et énumération rejoués

- **Essais du paquet** : **168 passed** dans l'arbre recréé (cinq fichiers `tests/test_accb6_*_v1.py`, 110,9 s) : les 165 d'avant plus les 3 de la garde de non-relance.
- **Énumération** : rejouée, sortie **égale à l'octet** à la sortie versée (`3bde500f…`). Bilans inchangés : 0 cas sans état, 0 cas sans phrase.
- **Non rejoués** :
  - les essais de T0.7 : aucun fichier qu'ils lisent n'est touché ;
  - l'essai hors suite aux constantes réelles : le calcul n'a pas changé.

## 6. Banc de mutations (copies seulement, `-o pythonpath=`, import tracé, deux processus)

- **67 mutations, 67 tuées** en un seul passage, sur une copie de l'arbre du commit.
  - Les 65 précédentes : M01 à M55, et C01 à C10 pour le contrôle du code.
  - R01 : la garde de non-relance retirée.
  - R02 : la garde cherche un autre nom de fichier.
- Aucun disque plein ; import tracé dans la copie pour toutes les mutations.
- Scripts du bac à sable : `banc_accb6_v3.py` (`d3b1493e…`), `mutations_accb6_v3.py` (`53f8f5df…`) ; résultats `banc-v3.jsonl` (`824411e0…`).

| id | ce qui est éprouvé (`garde_v1.py`) | issue | premier essai en échec |
|---|---|---|---|
| R01 | garde de non-relance retirée | tuée | `test_accb6_relance_v1.py::test_artefact_arret_d_un_run_quelconque` |
| R02 | garde de non-relance : nom de fichier cherché | tuée | `test_accb6_relance_v1.py::test_artefact_arret_d_un_run_quelconque` |

## 7. Retrait de l'arbre

- Arbre propre (`git status --porcelain --ignored` vide) et branche poussée (tête distante `5ee8a4ac…`) avant le retrait.
- Retrait par `git worktree remove /home/user/wt-accb6`, lancé depuis le dépôt principal, sans `--force`. Le résultat est donné dans le message final à la mère : ce rapport est scellé avant le retrait.

## 8. Points ouverts

1. **`CODE-ACCB6` au nouveau commit** (§ 1) : fichier neuf, scellement et ligne à faire par la mère. Si une ligne pour `56c624dd…` a déjà été inscrite au registre propre, elle n'est jamais réécrite. Une seconde ligne `CODE-ACCB6` ferait refuser la garde (« exactement une ») : c'est un nœud de procédure pour la mère.
2. **Restent ouverts** (rapport, § 8 ; complément 1, § 8) : rejouer la suite de T0.7 dans un arbre complet ; modules hors du paquet non contrôlés par `CODE-ACCB6` ; couples CP-03, CP-04, CP-06 et CP-07 ; R-B6-DIR sur jouet.

## 9. Refus d'un contrôle

Aucun refus d'un contrôle de permissions ou de sécurité pendant cette suite.
