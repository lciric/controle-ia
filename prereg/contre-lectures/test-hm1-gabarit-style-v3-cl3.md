# Contre-lecture n° 3 — test H-M1, écart v2 → v3 seul

- Contre-lecteur : sous-agent neuf (R2), qui n'a écrit ni le préenregistrement ni le code relus.
- Date : 26 octobre 2026.
- Fichiers lus, tous dans `scratchpad/cl3-hm1/` : `diff-prereg.txt`, `test-hm1-gabarit-style-v3.md` (et sa v2, pour
  le diff), `diff-mesurer.txt`, `mesurer_verbalisation_hm1_v2.py`, `mesurer_verbalisation_hm1_v3.py`,
  `hm1_instance_v2.sh` et `v3`, `amorce_hm1_v2.sh` et `v3`, `lancer_hm1_v2.sh` et `v3` (comparés par `diff`),
  `analyser_hm1_v2.py`. Aucun script exécuté, aucun réseau.
- Empreintes recalculées (`sha256sum`) : `mesurer_verbalisation_hm1_v3.py` `d8504166…`, `analyser_hm1_v2.py`
  `d699b823…`, `hm1_instance_v3.sh` `1003bab1…`, `amorce_hm1_v3.sh` `fe51b61a…`, `lancer_hm1_v3.sh` `b9a4e1c1…` :
  toutes égales à celles que cite le texte v3. Le commit `a9ff28e9…` et `extraire_activations_v2.py` n'ont pas pu être
  vérifiés (non fournis).

## Verdict

**Scellable après corrections.** Aucune constatation bloquante. Le nouveau contrôle de révision est sain. Il équivaut à
ce que faisait transformers 4 : son `_commit_hash` était lu par expression régulière sur ce même chemin
`snapshots/<commit>/`. Le contrôle ne peut pas passer à tort de façon plausible. Il ne devrait pas échouer à tort sur
le vrai modèle. L'écart ne touche ni le plan, ni les mesures, ni les seuils, ni la lecture. Les corrections portent sur
le texte : consigner les essais sain et artefact (CL3H-01) et déclarer quatre réserves. Elles peuvent être faites
sans nouvelle relecture.

## Réponses aux cinq points

1. **Contrôle sain.**
   - **Ce que fait la fonction.** `try_to_load_from_cache(repo, "config.json", revision=<commit complet>)` ne fait
     que lire le disque. Si un fichier `refs/<révision>` existe, elle le résout (aucun n'est écrit quand on demande
     un commit complet). Elle cherche ensuite `snapshots/<révision>/config.json`. Elle rend un chemin (`str`), `None`,
     ou la sentinelle `_CACHED_NO_EXIST`. Le code refuse tout ce qui n'est pas un `str` ou dont le dossier parent
     ne porte pas le commit demandé. Si `refs/` redirigeait ailleurs, le nom différerait et le run s'arrêterait.
   - **Ce que l'égalité prouve.** Quand le fichier est présent, l'égalité tient presque par construction (voir
     CL3H-02). La vraie garantie vient d'ailleurs : `snapshot_download` nomme le dossier d'après le commit que le
     Hub a résolu, et refuse un commit inexistant.
   - **Échec à tort sur le vrai modèle : peu probable.** `allow_patterns` prend `*.json`, donc `config.json`,
     `tokenizer.json`, `tokenizer_config.json` (qui porte le gabarit de dialogue à cette révision),
     `generation_config.json` et `model.safetensors.index.json`. Il prend aussi `model-*.safetensors`, donc les
     quatre fichiers de poids. Il ne prend pas `original/*.pth`.
   - **Même cache.** Les deux processus lisent le même cache par défaut. `python -I` ignore les variables `PYTHON*`,
     pas les variables `HF_*`.
   - **Chargement local.** Le tokeniseur rapide se charge depuis le dossier sans `tokenizer.model`. Charger depuis
     un dossier local ne fait aucun appel réseau.
2. **Fidélité du texte au code.** Bonne dans l'ensemble. Deux écarts mineurs : CL3H-04 (chaîne vide) et CL3H-02 (ce
   que l'égalité garantit vraiment).
3. **Références v2.** Celles qui restent sont voulues et cohérentes. Les stimuli et l'analyse restent en v2.
   L'analyse lit `<résultats>/verbalisation/verbalisation-hm1-v2.json` et `<résultats>/traits-stimuli/…` ; la
   mesure v3 écrit `verbalisation-hm1-v2.json` dans `$SORTIE/verbalisation`. Le chemin concorde avec
   `SORTIE=resultats-hm1-v3`. Seuls des détails de forme restent (CL3H-07).
4. **Périmètre de l'écart.**
   - **Mesure.** Le diff ne touche que trois choses : la docstring, le bloc de révision (avec le chargement
     depuis le dossier d'instantané au lieu de l'identifiant du Hub plus `revision=`) et un champ du manifeste
     (`commit_hash_config`).
   - **Scripts shell.** Seuls les noms changent.
   - **Préenregistrement.** Les sections Hypothèse, Prédiction, P, Témoins, Contrastes, Estimation, Seuil, Plan
     (sauf les noms), Critères et Graines sont identiques mot pour mot.
   - **Chargement.** Passer de l'identifiant du Hub au chemin local lit les mêmes fichiers. Rien n'indique un
     changement de tokenisation ou de gabarit.
   - **Ce qui sort du périmètre.** Le GO et le coût déjà engagé ne sont pas traités (CL3H-05).
5. **Extraction et `_commit_hash` None.** Oui, c'est une réserve à déclarer (CL3H-03).

## Constats

### CL3H-01 — Essais sain et artefact du nouveau contrôle non consignés (à corriger)
- **Constat.** R5 veut que toute garde d'arrêt soit testée sur un cas sain et sur un artefact. Selon le brief,
  deux essais ont eu lieu sur un modèle minuscule du Hub : cas sain passé, cas artefact arrêté avec le code 1. Le
  texte v3 n'en dit rien : ni chemin, ni empreinte des traces, ni versions (transformers 5.18 ? huggingface_hub ?).
- **Branches non couvertes.**
  - La répétition locale de bout en bout (`MODELE_LOCAL`) passe par la branche `local`, qui saute le nouveau
    contrôle. Elle ne l'exerce donc pas.
  - La branche « `_commit_hash` non vide ≠ révision » n'a pas de cas artefact, faute de pouvoir le provoquer sous
    transformers 5.
- **Correction.** Ajouter une ligne au texte. Elle donne les deux essais, avec le chemin et l'empreinte des traces,
  les versions et le modèle minuscule utilisé. Elle déclare que la seconde garde n'a pas de cas artefact, ou en
  fournit un en forçant `config._commit_hash` dans un test unitaire.

### CL3H-02 — Égalité presque construite : dire ce que le contrôle garantit (à déclarer)
- **Constat.** Pour un commit complet, `try_to_load_from_cache` bâtit `snapshots/<revision demandée>/config.json`.
  L'égalité « nom du dossier = révision demandée » vérifie donc surtout que l'instantané de ce commit est présent
  dans le cache. La garantie de fond est ailleurs : `snapshot_download` nomme le dossier d'après le commit que le
  Hub a résolu. C'était déjà la garantie de `_commit_hash` sous transformers 4.
- **Ce qui n'est pas contrôlé.** Le contenu des fichiers face aux empreintes du Hub. Ce point est antérieur à la
  v3, il n'est pas introduit par elle.
- **Correction.** Une phrase dans la métrique : « Le contrôle établit que les fichiers chargés sont ceux de
  l'instantané nommé par le commit que le Hub a résolu au téléchargement ; il ne vérifie pas leur contenu. »

### CL3H-03 — La mesure secondaire P n'a aucun contrôle de révision résolue (à déclarer)
- **Constat.** `extraire_activations_v2.py` charge par identifiant du Hub plus `revision=<commit>`. Selon le brief,
  il accepte un `_commit_hash` None. Sous transformers 5, la règle « révision résolue = révision demandée » de la
  liste d'arrêt ne vaut donc que pour V. La liste d'arrêt est pourtant écrite sans restriction.
- **Risque.** Faible : un commit complet est immuable, et le cache contient déjà l'instantané contrôlé par V, qui
  tourne avant. Mais c'est un écart entre la règle écrite et ce que fait le code.
- **Correction.** Déclarer dans le texte, à la métrique P ou à la liste d'arrêt, que le contrôle de révision ne
  vaut que pour V. P est chargée du même commit complet, sans contrôle de la révision résolue, et son manifeste
  peut porter `None`. Ne pas modifier `extraire_activations_v2.py` : cela changerait une empreinte citée et
  sortirait de l'écart minimal.

### CL3H-04 — « `_commit_hash` non vide » : le code arrête aussi sur la chaîne vide (forme)
- **Constat.** Le texte dit qu'un `_commit_hash` non vide doit être égal à la révision. Le code
  (`hachage not in (None, a.revision)`) arrête aussi sur `""`. Le code est plus strict que le texte, sans effet
  pratique.
- **Correction.** Écrire « Si la configuration porte un `_commit_hash` autre que `None`, il doit être égal… ». Ou
  laisser tel quel et le noter.

### CL3H-05 — GO et coût déjà engagé par la v2 avortée (à déclarer)
- **Constat.** La v3 relance sous le même GO-2026-10-25-03 (plafond de 10 USD, devis ≤ 3 USD). Le texte ne dit pas
  ce que l'instance de la v2 a déjà coûté. Il ne dit pas non plus que l'arrêt « coût au-delà de 10 USD » est
  cumulé sur les deux runs. Il ne dit pas que R-456 couvre la relance sous ce GO.
- **Correction.** Ajouter une ligne : coût de la v2, avec son renvoi au registre des dépenses ; plafond restant ;
  la décision R-456 vaut relance sous GO-2026-10-25-03. Si R-456 ne couvre pas la relance, il faut un GO
  (nœud de décision).

### CL3H-06 — Traces de l'arrêt de la v2 non citées par chemin et empreinte (forme)
- **Constat.** Le texte cite la v2 par une empreinte tronquée (`4fb3ee31…`). Il cite R-454 sans le chemin ni
  l'empreinte des traces du run arrêté (journal, identifiant de l'instance, arrêt consigné). R6 demande un renvoi à
  un chemin et à une empreinte.
- **Correction.** Donner l'empreinte complète de la v2 scellée, ainsi que le chemin et l'empreinte de la trace de
  l'arrêt (journal poussé ou `registres/arrets.md`).

### CL3H-07 — Restes de forme dans les commentaires (forme)
- **Constat.**
  - La docstring de `analyser_hm1_v2.py` dit « v2 » : c'est voulu, puisqu'elle est inchangée.
  - L'usage de `mesurer_verbalisation_hm1_v3.py` cite `stimuli-hm1-v2.json` : c'est juste.
  - L'amorce v3 parle encore de « deux extractions » (déjà déclaré par CL2H-09).
  - La ligne 4 de `hm1_instance_v3.sh` dépasse la largeur des autres.
  - Rien d'incohérent sur le fond.
- **Correction.** Aucune exigée. Ne pas toucher aux scripts, cela changerait les empreintes. Noter seulement.

## Traitement suggéré

CL3H-01 à CL3H-06 se corrigent par le texte seul, sans toucher au code ni aux empreintes. Une fois faites, la v3 peut
être scellée sans nouvelle contre-lecture. Remplir la ligne « Contre-lecture 3 » avec l'empreinte de ce rapport.
