# Journal du candidat 1 de T0.6 — 2026-11-05T21:26:31Z (`date -u`)

- brouillon 5 : `brouillons/T0.6-organismes-v0-v1-brouillon5.md`, `e95d4d48825bdb427207be87964fa46ad62918ff8b9dac5e0c106aa35f38f817` (empreinte vérifiée avant tout ; non scellé, pas de compagnon)
- contre-lecture neuve du lanceur v2 et du brouillon 5 (hors de cet arbre, branche `prep/fille-9-contre-lectures-v1`, commit `15d2ce93`, `docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v2/contre-lecture-lanceur-T0.6-v2.md`) : `b49ca28b660e122fcfa5722bde4ae4b0b67914b008bd5290a63b2d2b9b8f1f2e` (relevé par `sha256sum`)
- corrections de code v3 (même dossier, `corrections-code-lanceur-T0.6-v3.md`) : `9a89626bce12095930e1bd10006213e9f284f0574fda7c71895198381eb2c792` (relevé par `sha256sum`)
- couples : `couples-brouillon5-vers-candidat1-T0.6-v1.json` (copie à l'octet dans ce dossier, `cmp` égal), `34b2c64d94b8931084c4ddf6146c9df74a2b12b216158aaa097a0f733aa8e3d1` (vérifié), 7 couples, liste nue numérotée 1 à 7 dans l'ordre, appliqués dans l'ordre
- substitutions : `substitutions-candidat1-v1.json`, `b9373a907812cde06ba32f0d8b75ef8765e6bb0662251c6b105a9780922bea84`, 25 substitutions, appliquées après les couples
- script : `appliquer-candidat1-v1.py`, `8801550c3223bab15c487ad824b2f7aff0d952ef61b39b9b5ebe9ceb362e4ebe`

| couple ou substitution | ligne (au moment de l'application) | occurrences | longueur ancien | longueur nouveau |
|---|---|---|---|---|
| couple 1 | 540 | 1 | 56 | 63 |
| couple 2 | 540 | 1 | 91 | 139 |
| couple 3 | 540 | 1 | 104 | 186 |
| couple 4 | 540 | 1 | 72 | 183 |
| couple 5 | 661 | 1 | 721 | 1275 |
| couple 6 | 653 | 1 | 256 | 523 |
| couple 7 | 489 | 1 | 199 | 384 |
| C01 | 1 | 1 | 41 | 40 |
| C02 | 3 | 1 | 69 | 1556 |
| C03 | 94 | 1 | 138 | 3984 |
| C04 | 137 | 7 | 27 | 27 |
| C05 | 139 | 1 | 63 | 348 |
| C06 | 142 | 1 | 394 | 728 |
| C07 | 152 | 1 | 50 | 1091 |
| C08 | 571 | 1 | 72 | 72 |
| C09 | 594 | 1 | 63 | 63 |
| C10 | 594 | 1 | 108 | 108 |
| C11 | 594 | 1 | 67 | 67 |
| C12 | 594 | 1 | 73 | 73 |
| C13 | 594 | 2 | 44 | 112 |
| C14 | 590 | 1 | 80 | 624 |
| C15 | 591 | 1 | 181 | 347 |
| C16 | 591 | 1 | 53 | 53 |
| C17 | 592 | 1 | 43 | 43 |
| C18 | 592 | 1 | 175 | 207 |
| C19 | 707 | 1 | 301 | 347 |
| C20 | 708 | 1 | 163 | 282 |
| C21 | 709 | 1 | 50 | 52 |
| C22 | 713 | 1 | 158 | 803 |
| C23 | 700 | 1 | 175 | 261 |
| C24 | 717 | 1 | 55 | 55 |
| C25 | 697 | 1 | 44 | 1489 |

Marqueurs du candidat 1 (`<<[A-Z0-9_]+>>`), 11 distincts (occurrences) :

- `<<COMMIT_CODE_T06>>` : 4
- `<<EMPREINTES_CODE_T06>>` : 6
- `<<EMPREINTE_AMORCE_T06>>` : 5
- `<<EMPREINTE_PREREG_P3BIS>>` : 2
- `<<EMPREINTE_PREREG_T07>>` : 3
- `<<EMPREINTE_RAPPORT_LANCEUR_T06>>` : 3
- `<<ENTROPIE_T06>>` : 3
- `<<LONGUEURS_TEXTES_P3>>` : 2
- `<<MOT_LAZAR_DT>>` : 12
- `<<SCRIPT_PUISSANCE_V3>>` : 4
- `<<TESTS_ATTENDUS_T06>>` : 5

Clés lues par la chaîne (lignes qui portent « clé : » suivi d'un accent grave ; « Tests attendus » exactement 1, les autres au plus 1) :

- « Entropie : ` » : 1
- « Commit du code d'analyse : ` » : 1
- « Configuration de T0.6 (empreinte canonique) : ` » : 1
- « Tâches d'évaluation de T0.6 : ` » : 1
- « Tests attendus : ` » : 1
- « Chemin de la configuration de T0.6 : ` » : 1
- « Chemin des tâches d'évaluation de T0.6 : ` » : 1
- « Chemin des tâches de distillation de T0.6 : ` » : 1
- « Chemin des consignes de P3 : ` » : 1

- forme de citation de l'amorce « `scripts/amorce_instance_t06_v3.sh` (` » : 1

- résultat : `brouillons/T0.6-organismes-v0-v1-candidat1.md`, `4c27a254ef6ec255d3abf43a4fd6c9a0b6ffd0d24e9513ae28b0a3af6b91d8b3`, 729 lignes

## Vérification indépendante par `grep` (2026-11-05T21:26:46Z, `date -u`)

- `grep -c -F` sur `brouillons/T0.6-organismes-v0-v1-candidat1.md` (lignes) :
  - « Entropie : ` » : 1
  - « Commit du code d'analyse : ` » : 1
  - « Configuration de T0.6 (empreinte canonique) : ` » : 1
  - « Tâches d'évaluation de T0.6 : ` » : 1
  - « Tests attendus : ` » : 1
  - « Chemin de la configuration de T0.6 : ` » : 1
  - « Chemin des tâches d'évaluation de T0.6 : ` » : 1
  - « Chemin des tâches de distillation de T0.6 : ` » : 1
  - « Chemin des consignes de P3 : ` » : 1
  - « `scripts/amorce_instance_t06_v3.sh` (` » : 1
- `grep -o '<<[A-Z0-9_]\+>>' … | sort | uniq -c` :
  - `<<COMMIT_CODE_T06>>` : 4
  - `<<EMPREINTES_CODE_T06>>` : 6
  - `<<EMPREINTE_AMORCE_T06>>` : 5
  - `<<EMPREINTE_PREREG_P3BIS>>` : 2
  - `<<EMPREINTE_PREREG_T07>>` : 3
  - `<<EMPREINTE_RAPPORT_LANCEUR_T06>>` : 3
  - `<<ENTROPIE_T06>>` : 3
  - `<<LONGUEURS_TEXTES_P3>>` : 2
  - `<<MOT_LAZAR_DT>>` : 12
  - `<<SCRIPT_PUISSANCE_V3>>` : 4
  - `<<TESTS_ATTENDUS_T06>>` : 5
- marqueurs distincts : 11 (onze attendus)
- mentions restantes de `lancer_t06_v2.sh`, `amorce_instance_t06_v2.sh` ou « lanceur v2 » (toutes historiques : statut, points 5 et 7 et 8 de l'en-tête, couple 7 au devis, ligne du 7 nov., section « Contre-lecture ») : lignes 7 20 91 92 97 109 543 590 699 
- aucun fichier existant modifié : `git status --short` ne montre que les fichiers neufs ; brouillon 5 toujours `e95d4d48825bdb427207be87964fa46ad62918ff8b9dac5e0c106aa35f38f817`
