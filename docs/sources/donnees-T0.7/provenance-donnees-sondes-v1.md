# Données d'entraînement génériques des sondes v0 (T0.7) — provenance — v1

Date : 2026-10-06 (UTC), session 10. Décision : P-011, option (c), retenue par Lazar (R-077). Bras principal du critère 3 de G0 : sondes entraînées sur des données génériques, jamais sur les organismes. Ce fichier fixe la provenance des deux jeux publics ; les jeux synthétiques (dissimulation, intention) auront leur propre fichier.

Les données ne sont pas versionnées dans le dépôt (`donnees/` est ignoré par git). Une instance les recharge à la révision citée et vérifie chaque empreinte ci-dessous avant usage ; toute différence arrête (R11).

## 1. Enjeux élevés — models-under-pressure

- **Article** : McKenzie et al., « Detecting High-Stakes Interactions with Activation Probes », arXiv 2506.10805 ; PDF scellé `docs/sources/pdf/2506.10805v4.pdf` (54bf5555…). Page 3 : « For training probes and finetuned baselines, we created a synthetic dataset by prompting GPT-4o. »
- **Jeu** : `https://huggingface.co/datasets/Arrrlex/models-under-pressure`, révision `940d830f639617752f54fdf2bca0da7e0d856a9e` (dernière modification le 2026-02-09) ; public, sans accès restreint.
- **Licence** : MIT, déclarée dans la fiche du jeu (`license: mit`). Le dépôt de code `github.com/arrrlex/models-under-pressure`, au commit `77d5c265c63e` (2026-02-09, « Switch dataset source from R2 to HuggingFace »), porte une licence MIT « Copyright (c) 2025 Alex McKenzie » (fichier LICENSE, sha256 `4166fc2df906c61ee39eb456104f9601a92a9a1409d3e034b425559391c5bbbe`, comme dans `docs/sources/ressources-code-v2.md`). Mention obligatoire dans tout livrable qui s'en sert.
- **Fichiers repris** (copie locale `donnees/T0.7-models-under-pressure-v1/`) :

  | fichier | lignes | octets | sha256 |
  |---|---|---|---|
  | `README.md` (fiche du jeu) | — | 5 894 | `2259cc1cff326e8e2d9c55019a9c78dae9d936a3d31acd542b2f76c2f14473a5` |
  | `training/train.jsonl` | 8 000 | 13 478 476 | `04216df3a8b3ebf3ffb617f1a6701b0429964d28a6c6df677896359891fe2f34` |
  | `training/test.jsonl` | 2 000 | 3 432 732 | `6af73f76248f46547cfbf346ba15cf0fafb5eac3986faae43de61c5e1660621f` |

- **Schéma lu** (compte de la session, sur `train.jsonl`) :
  - texte : champ `inputs` ;
  - étiquette : champ `labels`, « high-stakes » 4 000, « low-stakes » 4 000 ;
  - autres champs : `scale_labels`, `scale_label_confidence`, `high_stakes`, `pair_id`, `topic`, `tone`, `language`, `prompt_style`, `length`.
  - Le champ `high_stakes` (situation d'origine : 3 839 vrais) diffère de `labels`. L'étiquette retenue, `labels`, est fixée au préenregistrement de T0.7.
- **Jeux d'évaluation du même dépôt** (`anthropic_hh_*`, `mt_*`, `mts_*`, `toolace_*`, `mental_health_*`, `aya_redteaming_*`) : non repris à ce stade.

## 2. Tromperie — recette de 2502.03407, réimplémentée

- **Article** : Goldowsky-Dill et al., « Detecting Strategic Deception Using Linear Probes », arXiv 2502.03407 ; PDF scellé `docs/sources/pdf/2502.03407v1.pdf` (a4820ad5…). Le dépôt d'Apollo Research n'a pas de licence (`docs/sources/ressources-code-v2.md`) : rien n'en est copié.
- **Recette, sur PDF** :
  - p. 2, figure 1 : deux consignes, « Pretend you are an honest person making statements about the world. » et « Pretend you are a dishonest person making statements about the world. » ;
  - p. 4 : « Each pair differs only in the instruction given by the user to pretend to be an honest or deceptive person. We then insert a random true fact from the dataset in Azaria & Mitchell (2023) as the model’s response. We gather activations on this fact excluding the last 5 tokens, so that the fact could be completed in either an truthful or deceptive manner. » ;
  - p. 3 : « We train a logistic regression classifier with l2 regularization (λ = 10) on normalized activations (zero mean, unit variance). » ; puis « We then take the mean across tokens to get a single deceptiveness-score for each model response. ».
- **Écarts imposés par le programme** : jamais de moyenne sur les jetons dans une sonde de production. L'agrégation est le maximum ou l'attention (P-011, brief). Les couches sont 7, 15 et 23 sur 32 (P-011). L'article utilise la couche 22 sur 80 de Llama-3.3-70B-Instruct (p. 3).
- **Faits** : dépôt `github.com/andyzoujm/representation-engineering` (Zou et al. 2023, « Representation Engineering »), commit `5455d8a375d5fb1cb191f9ebcd089b7c21e9a31e` (2024-08-13).
  - Licence MIT, « Copyright (c) 2023 Andy Zou » ; LICENSE sha256 `1e4bb8e2313ef9ff36033526503aa8837c80ba1d4c055c2e7d9977760028eec7`.
  - Fichier `data/facts/facts_true_false.csv` : 612 affirmations, dont 306 vraies (`label` = 1) et 306 fausses ; sha256 `151b6163289460eb8b37f7c6a1998e23aed8e05b5e557bf1a2297079bf0e5af9`.
  - Copie locale : `donnees/T0.7-faits-repe-v1/`, avec le fichier de licence.
  - Ce sont les affirmations d'Azaria et Mitchell (2023) que Zou et al. redistribuent. On ne garde que les 306 vraies, comme la recette (« a random true fact »). Les deux sources sont à citer.
- **Clone de lecture** : `/home/user/ressources/andyzoujm_representation-engineering` (hors dépôt, clone superficiel anonyme), comme les autres ressources de `ressources-code-v2.md`.

## 3. Ce qui reste à fixer au préenregistrement de T0.7

- Étiquettes, découpage entraînement et validation (graine, R9), et jetons lus :
  - tromperie : l'affirmation, sans ses 5 derniers jetons ;
  - enjeux élevés : le message de l'utilisateur.
- Gabarit de conversation de Llama-3.1-8B-Instruct, par le format du harnais.
- Usage de la validation générique pour choisir la sonde rapportée, jamais les organismes (P-011).
