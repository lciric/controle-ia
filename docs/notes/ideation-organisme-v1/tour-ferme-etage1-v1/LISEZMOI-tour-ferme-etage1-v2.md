# Tour fermé, étage 1 (GO-2026-11-02-23, 50 USD) — pièces de session-depot, v2

Écrit le 3 novembre 2026 à 01:11 UTC (heure relevée par `date -u`). Remplace, pour la suite, le LISEZMOI v1 (gardé tel quel).
Code de l'étage : **v64** (dépôt public, commit `63ed933`, brouillon 6 du texte `cdcb4470…`). Rien n'est scellé ici tant que
conv-audit n'a pas scellé son texte et levé la case `<<CASE_CONFIGURATION_V3>>`.

## Configuration v3, brouillon 2 — `configuration-tour-ferme-v3-brouillon2.json`
- Dérivée de la configuration du 1er novembre (`4ae5a1e0…`) par programme, comme le brouillon 1 (`109f673c…`, gardé), avec :
  commandes de Kimi et d'Argon en **version 4** (`docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/`, branche
  `outils/commandes-tour-ferme-v1` à `ad8dcaad` : `commande_kimi_v4.py` `10afdab5…`, `commande_argon_v56_nuit_v4.py` `5c6d5149…`),
  interpréteur `/usr/bin/python3`, `--modele` explicite, options par rôle de l'annexe A et bornes du vérificateur (1 000 et 200
  jetons) ; clé neuve de la v64 `fournisseurs.<kimi, argon>.prix_entree_usd_par_million_jetons` = **2** (Kimi) et **10** (Argon),
  le prix d'entrée que chaque commande emploie pour son pire cas.
- Lue **conforme** par `configuration_v56.lire_configuration_v56` et `adaptateur_commande_v64.bareme_depuis_configuration` du
  commit public `63ed933` (prix d'un caractère : 6,67 × 10⁻⁷ USD pour Kimi, 3,33 × 10⁻⁶ USD pour Argon).
- **Brouillon** : la version définitive portera un nom sans « brouillon » ; son empreinte ira au plan gelé ; elle n'attend plus que
  la contre-lecture courte des commandes v4 (en cours) et le texte de conv-audit.

## Relais chez la fille (constat de l'annexe A.6 bis, à poser au lancement)
- **Relais Kimi** (`relais_kimi_v3.py`, port 8804) : `--plafond-usd 50` (au-dessus de la part de 44 USD : le plafond propre du
  relais ne doit jamais mordre avant le compteur de l'orchestrateur, sinon ses refus 402 seraient lus « fin des tours » par la
  v64) ; `--max-appels 1800` (au moins 1 731 appels permis, n° 392 de conv-audit).
- **Relais Argon** (`commande_argon_v56_nuit_v2.py servir`, port 8805, instrument gelé, monofil, jamais en même temps qu'une autre
  course sur Argon) : `--plafond-usd 10` (au-dessus de la part de 6 USD) ; `--max-appels 200` (au moins 147).
- La garde cumulée des commandes reste à 50 USD (substitution du lanceur) et la garde d'étape de chaque commande porte sur sa
  seule part (v4) ; le compteur de l'orchestrateur tient les parts et le pire cas avant chaque étage.
- Environnement de l'orchestrateur : `env -i` avec la liste blanche de l'annexe A.8, `POLE_MACHINE_JETABLE_V56=1`,
  `TMPDIR=/tmp`, `bwrap` 0.9.0 (présent chez la fille), identité dédiée sans privilège pour le bac.
