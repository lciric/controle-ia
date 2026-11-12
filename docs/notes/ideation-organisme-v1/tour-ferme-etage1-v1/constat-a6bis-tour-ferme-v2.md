# Tour fermé, étage 1 — constat de l'annexe A.6 bis, à jouer chez la fille avant le premier appel, v2

Écrit le 3 novembre 2026 vers 11:00 UTC (heure relevée par `date -u`) par un sous-agent de session-depot. **Remplace la v1**
(`constat-a6bis-tour-ferme-v1.md`, `61bc404bd2518dda6ecf7b8034e982db417f8390731cd4c74ec3205064147893`, qui visait les commandes v4
et la configuration v3 : CL6-03). Sources : commandes v6 (`outils/commandes-tour-ferme-v1`, commit `84b67499`,
`LISEZMOI-commandes-tour-ferme-v4.md`) ; contre-lecture de la v6 (`contre-lecture-commandes-tour-ferme-v6-v1.md`,
`16617df6c61d48fe4cbf231600eb8c1b7d6de0e212a64fcf47e711f3ae9022fb`, commit `12f9e0e3` : « scellable telle quelle », mineurs
CL6-01 à 03) ; décisions de conv-audit n° 393 § 4 et n° 406 § 2. Chaque point est relevé chez la fille et écrit dans son rapport
de lancement scellé **avant** le premier appel de modèle ; un point non tenu arrête le lancement (rien n'est appelé).

## 1. Fichiers et empreintes (A.2)
- Configuration : `docs/notes/ideation-organisme-v1/tour-ferme-etage1-v1/configuration-tour-ferme-v4.json`
  `15b34adf9329a33d9f8135160a6ea2443dc17ce786dc28fa0b5c61c4560a2e6b` = la v3 (`642b3c5f…`) où ne changent que les deux chemins
  de commande (v4 → v6) et le texte `_lisez_moi` (vérifié par programme : tout le reste égal, `prix_entree_usd_par_million_jetons`
  2 et 10 inchangés, options des commandes inchangées) ; pièces sous `pieces/`, empreintes dans le fichier.
- Commandes, à extraire de `outils/commandes-tour-ferme-v1` (`84b67499`) à leur chemin absolu, empreintes égales :
  `/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_kimi_v6.py`
  `889309305aeb37de9801c2f40c31769fd268abded1ac61ea94196fd0d51195ae`, `…/commande_argon_v56_nuit_v6.py`
  `5eae1a0468430e243c3c4e099b3969f949f62add688531aafdd7f0f44e036e55`, `…/registre_depense_cumulee_v1.py` `8ba92066…` ;
  interpréteur `/usr/bin/python3` (→ `python3.13`, `dc9c6efba6e3583b…` ici ; relevé au manifeste).
- Vérification sans appel par le lanceur v64 (`ideation-organism` `eaa74ca`), faite le 3 novembre à 10:58 UTC : **conforme**
  (lecture `configuration_v56`, garde 15 sous `env -i` avec `POLE_MACHINE_JETABLE_V56=1`, adaptateurs réels sans relance des portes
  — le chemin de `--verifier-seulement` —, rôles joués, barème lu 2 et 10, familles séparées ; empreintes des arguments au manifeste
  égales à celles ci-dessus). `--verifier-seulement` lui-même exige le texte scellé qui gèle cette configuration (brouillon 7) : **à
  rejouer chez la fille** avec lui, sur ces fichiers à leurs chemins. Script et sortie : `verifier_configuration_tour_ferme_v4_v1.py`
  (`31fa8ca7…`), `verification-configuration-tour-ferme-v4-v1.json` (`6c8a1506…`), même dossier (ici, les deux commandes v6 lues à
  leur chemin de branche, empreintes contrôlées, la fille n'étant pas ce conteneur).

## 2. Ce que les commandes v6 garantissent (lu, essayé, contre-lu)
- **Code 4 « rien envoyé » réservé au plafond de session** (B11) ; sa dernière ligne ne porte ni `modele_servi`, ni `refus`, ni
  `stop_reason` (I33) → « budget_depasse » (fin des tours). **Tout autre refus sort en code 3** (garde d'étape, garde cumulée,
  registre illisible ou corrompu, 402 et 429 du relais, 4xx et 5xx) → « erreur », arrêt de la course : une limite d'un relais
  **arrête** la course, elle ne vide plus les cartes en silence (prix accepté au n° 393).
- **Réponse coupée** de l'expérimentateur et du vérificateur : code 0, texte, `coupee: true`, statut `coupee` au registre ; du
  proposeur : code 5, arrêt.
- Cause d'un refus : dernière ligne (`cause_refus`), sortie d'erreur (au motif, donc à `journal["arret"]`), et statut de la ligne
  `fin` au registre pour 402 et 429.

## 3. Relais dédiés, neufs, sans autre usage pendant la course (réglages exigés)
- **relais Kimi** (`relais_kimi_v3.py`, port 8804), démarré pour cette course seule : `--modeles-permis kimi-k3.1-pro
  --prix-entree 2 --prix-sortie 10 --prix-cache 2` (`--prix-cache` **obligatoire**, sans défaut), `--plafond-usd` ≥ **44,40**
  (44 + réserve par appel 0,40 ; ≈ 45 conseillé), `--max-appels` ≥ **1 731** ;
- **relais Argon** (`commande_argon_v56_nuit_v2.py servir`, port 8805), démarré pour cette course seule, jamais partagé avec A1-v3
  ni une autre course : `--modeles-permis gemini-4-argon`, `--plafond-usd` ≥ **6**, `--max-appels` ≥ **147** ;
- relevé `GET /relais/etat` des deux relais **avant le premier appel** (plafond, appels, dépense nulle, clé présente en booléen) et
  **à la fin ou à l'arrêt** ; relevés et journaux des relais scellés au rapport.

## 4. Mineurs de la contre-lecture v6, tenus ici
- **CL6-01** — une réponse coupée **vide** de l'expérimentateur est lue « ok » sans texte (fin des tours) et la classe gelée ne
  garde pas `coupee` : au relevé, **compter les lignes `fin` de statut `coupee` du registre de dépense**
  (`<SORTIE>/registre-depense-cumulee-v1.jsonl`), par rôle et par tour, et les joindre au rapport ; une coupée au premier tour d'une
  carte est traitée par l'audit comme S6 (défaut à examiner avant toute lecture d'issue) — à geler au brouillon 7.
- **CL6-02** — la ligne de cause sur la sortie d'erreur n'existe que pour les six causes : sur un arrêt par un 429 de Moonshot
  transmis (compte sans crédit, TF-06), un 400 de fenêtre, un 413 du relais ou un échec de Gemini, le motif reste « commande
  externe : code 3 : » ; **à l'arrêt, relever le journal et `GET /relais/etat` du relais en cause** (et la dernière ligne, au
  registre) pour nommer la cause au rapport.
- **CL6-03** — ce constat remplace la v1.

## 5. Ce qui est accepté par écrit, ou reste à décider
- Fenêtre d'entrée non contrôlée par les commandes : Kimi refuse en code 4 au-delà de 378 402 caractères ASCII à 0,80 USD (344 002
  avec un accent sur dix, 369 173 avec une fin de ligne sur quarante) ; au-delà de la fenêtre de Moonshot, 400 transmis → code 3,
  arrêt.
- CL5-04 : une erreur de Moonshot transmise est comptée au pire cas réservé, `envoye: true` (contraire à la lettre du n° 393, sur
  la latitude du n° 406) : à confirmer au brouillon 7.
- Clés d'étape : `tour_ferme_v64/kimi` et `tour_ferme_v64/argon` ; barème 2 et 10 (inchangés).

## 6. Environnement de l'orchestrateur (annexe A.8, inchangé)
`env -i` avec la liste blanche ; `POLE_MACHINE_JETABLE_V56=1` ; `TMPDIR=/tmp` ; `bwrap` 0.9.0 ; identité dédiée sans privilège
pour le bac ; aucune variable de clé dans l'environnement de l'orchestrateur (les relais tiennent les clés).
