# Consigne : lot 3, étapes 2 et 3 — contre-lecture R2 de la consigne des concepts (A) ; script de vérification des phrases (B) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`), autonomie de 12 heures (R-2088). Deux destinataires distincts, chacun neuf, qui n'ont écrit ni T0.7, ni son module, ni ses jeux, ni la consigne des concepts : **(A) un contre-lecteur, modèle Fable** (l'auteur de la consigne est Opus 5.5) ; **(B) un développeur, Opus**. Chacun lit des fichiers de T0.7 : exclu ensuite de tout rôle de lecteur de P3-bis.

## Interdits (A et B)

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise**. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py` ; aucun texte d'action de P3. Aucun appel externe, aucune dépense, aucune écriture git (sauf, pour B, `git fetch` à refspec explicite de `donnees/tokeniseur-llama-3.1-8b-instruct-v1` vers `refs/remotes/origin/…`, et lecture du tokeniseur **borné à son dossier**).

## Pièces

Consigne `docs/procedures/consigne-concepts-sans-lien-T0.7-v1.md` (`32a7194a…`) et son journal (`36fcc1fd…`) ; consigne brouillon 1 (`acc7bdfb…`) ; inventaire des jeux, §§ 4.2 et 5 (lot 3) (`c9910a54…`) ; module de T0.7 au commit `8dc1cb09` (`prep/t07-module-v2`, lu par `git -C /home/user/controle-ia-travail show 8dc1cb09:<chemin>`) ; brouillon 20 de T0.7 (`9ef671ac…`, T7-P9) ; registre R-2101, R-2102, R-2104, R-2105.

## (A) Contre-lecture R2 de la consigne

Juger : accord au module (`lire_phrases_concepts`, `Extracteur.phrase`, borne de 128 jetons, `indice`, `format_lecture`) ; fermeture et vérifiabilité des contrôles C0 à C13 (chacun avec son artefact) ; annexes A et B (doublons, recouvrements, mots qui trahissent l'affect ou le domaine des agents) ; règles de renvoi et plancher ; contre-vérification à l'aveugle (tirage, clé, questions fermées, aucun fichier de P3-bis) ; points ouverts 1 à 7 du rédacteur et décisions de la mère (R-2105). Sortie : `prereg/contre-lectures/consigne-concepts-sans-lien-T0.7-v1-cl1.md` (scellé), couples `{id, section, motif, ancien, nouveau}` dans `…-cl1-couples-v1.json` (scellé) s'il en faut. Verdict en une ligne.

## (B) Script de vérification et ses essais

`scripts/verifier_phrases_concepts_t07_v1.py` et `tests/test_verifier_phrases_concepts_t07_v1.py` **dans un arbre à toi** (`git -C /home/user/controle-ia-travail worktree add --no-checkout -b prep/t07-concepts-script-v1 /home/user/wt-concepts f26bbfc6`, extraction partielle `git -C /home/user/wt-concepts sparse-checkout set --no-cone '/*' '!/docs/sources/' '!/docs/notes/bras-attaque/'`, puis `git -C /home/user/wt-concepts checkout prep/t07-concepts-script-v1`, absence du dossier sous embargo vérifiée ; commits locaux sur cette branche seulement) : les contrôles C0 à C13 de la consigne, chacun avec un cas sain et un artefact (R5), tokeniseur réel, C12 par la fonction du module copiée du commit `8dc1cb09` (ou importée d'un dossier temporaire) ; graines par `SeedSequence` (R9) ; sortie : un journal et un code 0/1/2 ; la section 5 extraite par programme pour l'écrivain. Rapport court `docs/notes/g0-deux-semaines-v1/t07-concepts-v1/rapport-script-verification-concepts-v1.md` dans ton arbre, scellé. Si la contre-lecture (A) change la consigne, la mère te transmettra ses couples.

Réponses courtes : (A) chemins, empreintes, verdict, couples ; (B) commits, comptes d'essais, chemin et empreinte du rapport.
