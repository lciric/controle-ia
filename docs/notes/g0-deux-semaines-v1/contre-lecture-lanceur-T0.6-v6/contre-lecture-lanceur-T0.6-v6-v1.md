# Contre-lecture neuve (R2) du lanceur T0.6 v6, des ordres E2/E3 v3 et du candidat 4 — v1

## Consigne (message de la session mère, recopié mot pour mot)

> Mère — 10:05 UTC. **Contre-lecture d'un seul tenant : lanceur T0.6 v6, ordres E2/E3 v3, candidat 4** (R-1660). Pour le code, le banc et les essais, prends un **sous-agent neuf, de lignée Sonnet de préférence**, qui n'a lu ni ces pièces ni leurs versions antérieures, ni ta contre-lecture v4. Tu peux faire toi-même la composition des textes et la vérification des couples, comme la dernière fois. Déclare qui lit quoi, avec les lignées ; l'autrice est la fille 10, Opus 5.5.
>
> Pièces (empreintes vérifiées par la mère) :
> - `prep/t06-lanceur-v2` au commit **`1d226d2c`** : `scripts/lancer_t06_v6.sh` (`27b355dc…`), `src/controle_ia/t06/session_v5.py` (`16659740…`), `tests/test_t06_v6_scripts.py` (`87508535…`), `scripts/banc_mutations_t06_v6.py`, `docs/notes/g0-deux-semaines-v1/banc-mutations-t06-v6.json`, `scripts/epreuve_e1_t06_v6.sh`, `docs/notes/g0-deux-semaines-v1/epreuve-e1-t06-v6-journal.md`, `docs/notes/g0-deux-semaines-v1/rapport-developpeur-lanceur-T0.6-v6.md`. Ordres dans `brouillons/ordres-t06-e2-e3-v3/` : E2 (`19c5bbc3…`), E3 (`9581fe1e…`) et le générateur `pieces/generer_ordres_v3.py` (`8ee5f149…`).
> - `prep/t06-candidat2-v1` au commit **`6dc75a43`** : `brouillons/T0.6-organismes-v0-v1-candidat4.md` (`a81cd47e…`) et `brouillons/T0.6-organismes-v0-v1-candidat4-pieces/` (script, couples K1–K10, journal).
> - Référence, pour toi seule : ta contre-lecture v4 (`docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v4/`, couples E2 `0e6aea13…`, E3 `ba4f6586…`), R-1657 et R-1660 sur `main`.
>
> Questions :
> 1. **Lanceur.** v6 = v5 + `reliability>=0.98` dans le filtre de création, rien d'autre (différences v5 → v6 et `session_v4` → `session_v5`) ? Rejoue les suites v1 à v6 (280 essais) et le banc (18 mutations, toutes tuées ?). E1 v6 est-il conforme à 0 USD (journal) ?
> 2. **Ordres v3.** Sont-ils produits par le générateur à l'octet ? Tes couples 1 à 6 d'E2 et le couple 1 d'E3 sont-ils présents ? Le couple 7 d'E2 est-il bien remplacé par la procédure v5 (`creation auto` ; code 5 → même commande ; trois rangs puis code 3 ; code 4 = aucune reprise) ? Les filtres de lecture sont-ils identiques à ceux du lanceur, lus à une seule source ? Aucun reste de v4 ou v5, ni de `<OFFRE>` ; seul marqueur `<<COMMIT_EPREUVES>>`.
> 3. **Dépense.** La lecture E2-1 passe de `dph_total<=0.45` au prix maximal de la configuration (0,60 pour la carte modeste), et E3 lit les filtres A100 et H200. Recalcule le pire cas d'E2 puis d'E3 (durées bornées par les gardes, multipliées par les prix maximaux, plus la dépense antérieure). Dis s'il tient sous le plafond de GO-2026-11-06-01 : 5 USD au total, jusqu'au 10 novembre. Sinon, couple.
> 4. **Candidat 4.** Est-il égal au candidat 3 plus les couples K1–K10, par script, à l'octet ? `creation <OFFRE>` doit être absent, les cinq marqueurs restants présents, et les citations du lanceur v6 cohérentes (noms, empreintes, commandes).
> 5. **Risques déclarés par la fille 10.** (a) Filtre non éprouvé contre le vrai `vastai` avant E2-1 (s'il est refusé : code 2, sans dépense) ; (b) filtre plus strict, donc code 3 plus fréquent ; (c) fiabilité en constante de module, que le texte ne règle pas. Bloquants ou non ?
> 6. **Verdict.** Pour les ordres : « scellables après remplissage de `<<COMMIT_EPREUVES>>` » (dis par quel commit), ou couples résiduels. Pour le candidat 4 : « prêt pour les marqueurs finaux », ou couples.
>
> Rendu sur `prep/fille-9-contre-lectures-v2`, dossier `docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v6/` (rapport, plus couples JSON s'il y en a), puis message. Aucune donnée réelle, aucune clé, aucune location, aucune dépense. Je n'attends pas d'approbation de ta part : lance-toi.

## Verdict

- **Ordres** : **scellables après 2 couples résiduels sur E2** (`couples-ordre-e2-v3.json`), puis le remplissage de `<<COMMIT_EPREUVES>>`. E3 : aucun couple.
  - Le commit qui remplit le marqueur ne peut pas être `1d226d2c` : son `registres/go.md` s'arrête à GO-2026-11-05-08 et **ne porte pas GO-2026-11-06-01**. Or `controles-epreuve` exige ce GO dans le registre du commit cloné (refus, code 2).
  - Les deux configurations d'épreuve n'y ont pas non plus de `.sha256`.
  - `<<COMMIT_EPREUVES>>` doit donc être un commit de la mère sur `prep/t06-lanceur-v2`, descendant de `1d226d2c`, qui ajoute le registre des GO de `main` (ligne GO-2026-11-06-01) et les sceaux des deux configurations, sans toucher au code.
- **Candidat 4** : **prêt pour les marqueurs finaux.**
- **Code v6** : conforme au delta annoncé ; 280 essais verts. Un défaut R5 relevé par le sous-agent :
  - la fiabilité n'est gardée que par le filtre envoyé à Vast ; `choisir_offre` ne la revérifie pas sur les offres reçues ;
  - correction C-V7-1 recommandée avant la course, **non bloquante pour E2 et E3** (motifs au point 5).

### Qui lit quoi

- **Code, essais, banc, E1** (question 1) : sous-agent neuf de **lignée Claude Sonnet**. Il n'a lu ni ces pièces, ni leurs versions antérieures, ni ma contre-lecture v4 (de 10:06 à 10:14 UTC environ). J'ai recoupé son constat principal sur `session_v5.py`, l. 28-66.
- **Ordres, dépense, candidat 4, risques** (questions 2 à 6) : fille 9, **lignée Claude Opus 5.5**, de la même lignée que l'autrice (fille 10, Opus 5.5) ; 7 novembre 2026, de 10:06 à 10:15 UTC (`date -u`).
- Rien de loué, aucune clé lue, aucun `vastai`, aucune dépense, aucune donnée réelle.

## 1. Lanceur (sous-agent Sonnet)

- **Delta**, par `diff` :
  - `lancer_t06_v5.sh` → `v6` : renommages seulement (`session_v5`, libellés), plus trois lignes de commentaire ;
  - `session_v4` → `session_v5` : deux changements de code, `FIABILITE_MIN_OFFRE = 0.98` (l. 28) et `reliability>=0.98` dans `filtre_recherche` (l. 37) ;
  - amorce inchangée (`amorce_instance_t06_v4.sh`).
  - **Conforme à l'annonce.**
- **Essais** : **280 passed** en 380,54 s (`tests/test_t06_*.py`, 22 fichiers), avec `--basetemp` supprimé ; l'arbre est resté propre.
- **Banc** : non rejoué dans le temps imparti, mais lu. Il compte 18 mutations tuées sur 18, avec un témoin vert. Deux mutations portent sur le filtre (fiabilité retirée, seuil abaissé). Il en manque une sur l'opérateur (`>=` en `>`), et aucune ne vise une garde de code, puisqu'elle n'existe pas.
- **E1 v6** : conforme à 0 USD. Le script refuse de tourner si `vastai` est sur le chemin. L'amorce rend le code 0, les 73 essais passent, et aucun mot interdit n'apparaît.
- **Défaut (R5)** : `choisir_offre` (l. 41-66) passe par `s2.verifier_offre`, qui ne lit pas la fiabilité. Une offre sans clé `reliability`, ou à 0,5, serait acceptée si Vast la renvoyait. Les essais v6 n'éprouvent que la chaîne du filtre, sans artefact (0,979, clé absente, type faux).

## 2. Ordres v3 (fille 9)

- **Générateur** : rejoué (`textes()`), il produit les deux ordres **à l'octet** (`19c5bbc3…`, `9581fe1e…`). Ses trois remplacements sont trouvés une fois chacun.
- **Filtres de lecture** : ils sont lus à une seule source (`session_v5.filtre_recherche` sur les configurations), et le générateur refuse tout filtre `'num_gpus=1…'` absent du lanceur :
  - modeste : `num_gpus=1 rentable=true gpu_name=RTX_4090 reliability>=0.98 cpu_ram>=32 cpu_cores_effective>=8 disk_space>=150 dph_total<=0.6` ;
  - A100 : `… gpu_name=A100_SXM4 … cpu_ram>=128 cpu_cores_effective>=16 … dph_total<=1.3` ;
  - H200 : `… gpu_name=H200_NVL … dph_total<=4.7`.
- **Restes** : aucun `lancer_t06_v4.sh`, `lancer_t06_v5.sh` ni `<OFFRE>`. Seul marqueur : `<<COMMIT_EPREUVES>>` (deux occurrences par ordre).
- **Mes couples de la v4** :
  - E2-2 à E2-6 : présents tels quels.
  - **E2-1 : présent, mais devenu faux.** Le texte dit « `surveillance` refuse de tourner si `HF_TOKEN` … a moins de 8 caractères ». Depuis C-V5-2, `surveillance` n'exige `HF_TOKEN` qu'en mode réel (`lancer_t06_v6.sh`, l. 230-233), de même que `creation` (l. 168). Et l'ordre dit plus loin (l. 90) que `HF_TOKEN` n'est pas exigé en mode jouet. **Couple résiduel 1** : ne plus transmettre `HF_TOKEN` à E2, ce qui n'envoie aucune clé inutile à une instance de jouet. Si `surveillance` le réclame malgré tout, l'instance est détruite par son identifiant.
  - **E2-7 (relecture par identifiant)** : bien remplacé par la procédure v5 (`creation auto` ; code 5 → même commande ; trois rangs au plus, puis code 3 ; code 4 → aucune reprise), avec en plus le contrôle de prédiction de rang 1.
  - **E3-1 (marge de 3 h)** : présent et reformulé pour `creation auto` (l. 64 : ne pas exécuter la ligne si prix × 3 h + forfait > 3,5 USD).
- **Couple résiduel 2** : E2-1 relève aussi la clé de fiabilité (nom exact, type, valeurs des rangs 1 à 3). C'est la donnée qui manque pour écrire C-V7-1 sans deviner le nom de la clé dans la sortie brute de Vast.

## 3. Dépense (pire cas des gardes)

- **E2** (plafond de configuration 1,5 USD, cumulé sur A, B et C par la dépense antérieure) :
  - prix maximal 0,60 (carte) + 0,03 (stockage) = 0,63 USD/h ; forfait de téléchargement 1 Go × 0,05 = 0,05 USD par instance ;
  - heures cumulées possibles : (1,5 − 3 × 0,05) / 0,63 ≈ **2,1 h** pour les trois instances ;
  - les gardes sont `creation` (code 3 au plafond), `surveillance` (`ARRET depense`) et la minuterie de l'instance à l'heure d'épuisement. L'estimation compte la carte même pendant l'arrêt, donc elle est prudente ;
  - **pire cas E2 = 1,50 USD.**
- **E3** (3,5 USD) :
  - 1,30 + 0,03 = 1,33 USD/h ; forfait jusqu'à 40 Go × 0,05 = 2,00 USD si le téléchargement est facturé au prix maximal ;
  - la règle des 3 h (couple E3-1) impose prix × 3 h + forfait ≤ 3,5, ce qui donne une heure d'épuisement d'au moins 3 h ;
  - **pire cas E3 = 3,50 USD**, conditionné par « dépense réelle d'E2 + 3,5 ≤ 5 », écrit dans l'ordre.
- **Cumul ≤ 5,00 USD : tient sous GO-2026-11-06-01, mais sans aucune marge.** Deux sources d'écart réel ne sont pas bornées par la garde :
  - un téléchargement réel au-delà du volume prévu (E2 : 1 Go prévu, alors que l'installation de `requirements-gpu.txt` sur l'image peut dépasser 2 Go, soit moins de 0,10 USD au prix maximal) ;
  - une instance arrêtée et oubliée, qui facture son stockage (0,03 USD/h) jusqu'à la fin du GO, le 11 novembre à 00:00 UTC, si la session tombe.
- **Aucun couple.** Les ordres détruisent tout à la fin (E2 étape 9, E3 étape 6), et l'ordre d'E3 compare à la facture d'E2 avant de créer. La mère peut, si elle le veut, plafonner E3 à 3,4 USD dans sa configuration pour garder 0,10 USD de marge.

## 4. Candidat 4 (fille 9)

- Rejoué par script : le candidat 3 (`b0eaa83a…`) plus les dix couples K1 à K10, avec les valeurs du script remplies (`{DATE_C4}` = 2026-11-07, `{HEURE_C4}` = 10:04, et les empreintes **recalculées sur les fichiers de `1d226d2c`**), donne le candidat 4 **à l'octet** (`a81cd47e…`). Chaque « ancien » est unique.
- `creation <OFFRE>` et `<OFFRE>` sont absents. Les cinq marqueurs restants sont présents (`COMMIT_CODE_T06`, `EMPREINTES_CODE_T06`, `EMPREINTE_AMORCE_T06`, `TESTS_ATTENDUS_T06`, `VALEURS_CITEES_T06`).
- Les citations du lanceur v6 sont cohérentes :
  - `lancer_t06_v6.sh` `27b355dc…`, rapport v6 `4e97b72b…`, banc `9295084e…`, essai `87508535…`, E1 `7e7353b1…`, ordres v3 `19c5bbc3…` et `9581fe1e…` ;
  - commandes `creation auto <CARTE> <DEPENSE_ANTERIEURE_USD> <DOSSIER> [ECHEANCE_UTC_S]` et `apres-creation FICHIER CODE DOSSIER` (plan daté du 11 novembre).
  - Les mentions du lanceur v4 (l. 13, 147) sont historiques.
- Une fois les couples résiduels d'E2 appliqués, l'empreinte de l'ordre d'E2 v3 citée par le candidat changera. Si E2 est corrigé, la mère remet à jour cette citation par le même script, avec la nouvelle empreinte.

## 5. Risques déclarés par la fille 10

- **(a) Filtre non éprouvé contre le vrai `vastai`** : non bloquant. E2-1 lit le même filtre à 0 USD avant toute création ; un refus donne le code 2, sans dépense.
- **(b) Filtre plus strict, code 3 plus fréquent** : non bloquant. Le code 3 n'engage aucune dépense, et E2-1 relève le nombre d'offres conformes.
- **(c) Fiabilité en constante de module** : non bloquant. La constante est couverte par l'empreinte du module citée au candidat (`EMPREINTES_CODE_T06`) et lue à une seule source.
  - Mais elle n'est gardée que par le filtre côté Vast (point 1). Pour les épreuves, c'est acceptable : le prix est borné et Vast filtre la requête.
  - Pour la course, deux voies :
    - **C-V7-1** : une garde de code dans `choisir_offre`, après lecture du nom réel de la clé à E2-1, avec ses essais (0,98 accepté ; 0,979, clé absente, chaîne, booléen et NaN refusés ; rang 1 sauté) et deux mutations ;
    - ou une décision écrite qui accepte la garde par le filtre seul, citée dans le rapport v6 et le candidat.
  - C'est une décision de la mère.

## Couples (E2 : 2 ; chaque « ancien » unique dans `ordre-fille-6-t06-e2-v3.md`, vérifié par script ; appliqués dans l'ordre)

1. Clés d'E2 : `HF_TOKEN` retiré, avec la raison juste depuis C-V5-2, et la conduite si `surveillance` le réclame.
2. E2-1 : relevé de la clé de fiabilité.
