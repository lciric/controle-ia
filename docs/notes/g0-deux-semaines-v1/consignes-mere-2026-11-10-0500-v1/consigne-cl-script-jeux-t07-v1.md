# Consigne : contre-lecture courte du script de vérification des jeux synthétiques de T0.7 (D-5 (a)) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`), autonomie de 12 heures (R-2088). Destinataire : un **contre-lecteur neuf, modèle Fable**, qui n'a écrit ni le script, ni les jeux, ni T0.7, ni leurs contre-vérifications. Exclu ensuite de tout rôle de lecteur de P3-bis.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise**. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py` ; **aucun texte d'action de P3** (ni ouvert, ni passé au script). Aucun appel externe, aucune dépense, aucune écriture git.

## Pièces

`scripts/verifier_jeux_synthetiques_t07_v2.py` et `tests/test_verifier_jeux_synthetiques_t07_v2.py` au commit `bd02ae3e` (lecture par `git -C /home/user/controle-ia-travail show bd02ae3e:<chemin>`) ; consigne v3 des jeux `docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md` (`d9de50a6…`) ; provenance et journaux du lot 1 sous `donnees/t07-jeux-synthetiques-v2/` (`provenance-v2.md`, `f4367670…` ; `journal-verification-v2.txt`, `58906bb4…`) ; inventaire des jeux (`c9910a54…`, écart E-7).

## Mandat

Juger, pour les contrôles 2, 3, 6, 9, 10 et `assembler` : le script fait-il ce que la consigne v3 exige (ligne de la consigne → ligne du script), sans repli silencieux, chaque garde avec un cas sain et un artefact dans les essais ; les essais passent-ils (rejoue-les une fois avec un `--basetemp` neuf sous `/home/user/cl-script-jeux-tmp/`, effacé ensuite par son chemin exact ; **aucun lancement qui lit les textes de P3**) ; un défaut change-t-il l'acceptation de J-D et J-A (R-2106) ?

## Sortie

`docs/notes/g0-deux-semaines-v1/t07-jeux-inventaire-v1/contre-lecture-script-jeux-v1.md`, scellé ; verdict en une ligne ; défauts numérotés (bloquant, à corriger, mineur). Réponse courte : chemin, empreinte, verdict, effet sur J-D et J-A.
