# Consigne : contre-lecture courte du script de vérification des phrases des concepts de T0.7 — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`). Destinataire : un **contre-lecteur neuf, modèle Fable**, qui n'a écrit ni le script, ni la consigne des concepts, ni T0.7, ni leurs contre-lectures. Exclu ensuite de tout rôle de lecteur de P3-bis.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise**. Aucun appel externe, aucune dépense, aucune écriture git ; rien dans `/home/user/wt-concepts` ni dans `donnees/t07-concepts-v1/` ; **ne lis aucune phrase écrite par l'écrivain** (dossier `/home/user/lot3-concepts/remise-ecrivain/`, interdit).

## Pièces

Script et essais sur la branche `prep/t07-concepts-script-v1` (`1b87dfe1`, poussée ; lecture par `git -C /home/user/controle-ia-travail show 1b87dfe1:<chemin>`) : `scripts/verifier_phrases_concepts_t07_v1.py` (`6bc2665a…`), `tests/test_verifier_phrases_concepts_t07_v1.py` ; rapport du développeur `docs/notes/g0-deux-semaines-v1/t07-concepts-v1/rapport-script-verification-concepts-v1.md` (`74984a39…`) ; consigne v2 `docs/procedures/consigne-concepts-sans-lien-T0.7-v2.md` (`79f2c89c…`) ; contre-lecture de la consigne (`4d759557…`, couples) ; registre R-2108, R-2114.

## Mandat

Juger : chaque contrôle C0 à C13 de la consigne v2 fait-il ce qu'elle exige (ligne de consigne → ligne de script), avec cas sain et artefact dans les essais (R5), sans repli silencieux ; CC-01 (importation du seul `--module-src`), CC-04, CC-05, CC-07 et les autres couples ; modes `extraire`, `verifier`, `echantillon`, `decompter`, `assembler`, `rejouer-c12` ; la remise au lecteur ne contient-elle bien que les sections permises ; les parties non écrites (remise complémentaire, second lecteur, réécriture d'un concept) : bloquantes ou non. Rejoue les 116 essais une fois dans un arbre détaché à toi (`git -C /home/user/controle-ia-travail worktree add --detach /home/user/wt-cl-concepts 1b87dfe1` en extraction partielle sans `docs/sources/` ni `docs/notes/bras-attaque/`), puis retire l'arbre.

## Sortie

`docs/notes/g0-deux-semaines-v1/t07-concepts-v1/contre-lecture-script-concepts-v1.md`, scellé ; verdict en une ligne ; défauts numérotés (bloquant, à corriger, mineur). Réponse courte : chemin, empreinte, verdict, bloquants, comptes d'essais.
