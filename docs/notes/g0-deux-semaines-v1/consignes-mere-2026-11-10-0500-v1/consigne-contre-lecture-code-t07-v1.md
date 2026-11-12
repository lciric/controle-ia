# Consigne : contre-lecture du code du module de lecture de T0.7 v2 (commit `1f77b34d`) par un autre modèle — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`). Destinataire : un **contre-lecteur neuf, modèle Fable** (le développeur du module est Opus 5.5 ; N-052 nomme Fable 5.1 : servi en Fable 5.2, écart déclaré). Il n'a écrit ni T0.7, ni son module, ni T0.6, ni P3-bis, ni leurs contre-lectures ; il n'est ni le lecteur exploratoire de 7a (R-2041), ni l'auditeur de l'écart DT-4 (R-2057). Ayant lu des fichiers de T0.7, il est **exclu ensuite de tout rôle de lecteur de P3-bis**.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/interdits-communs-v1.md` (`851028fc…`), en entier. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json`, **ni le `lecture-sondes-t06.json` d'un run jouet** ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. Aucun appel externe, aucune dépense. Aucune écriture dans `/home/user/wt-t07` (le développeur y travaille encore) ni sur `main` ; la mère committe ton rapport.

## Lieu des essais

Lecture du code par `git -C /home/user/wt-t07 show 1f77b34d:<chemin>`. Pour les essais : arbre détaché à toi, sans `docs/` : `git -C /home/user/controle-ia-travail worktree add --no-checkout --detach /home/user/wt-t07-cl 1f77b34d`, puis `git -C /home/user/wt-t07-cl checkout 1f77b34d -- src tests scripts brouillons/T0.7-sondes-v0-v1-brouillon19-pieces donnees requirements-cpu.txt` (adapte la liste si un essai de T0.7 l'exige, sans jamais extraire un chemin interdit) ; essais de T0.7 seulement (`tests/test_t07_*.py`), `--basetemp` neuf sous cet arbre ; répétition jouet permise une fois (`scripts/repetition_jouet_t07_v1.py`, voir son usage), sans ouvrir aucun `lecture-sondes-t06.json` ; à la fin, `git -C /home/user/controle-ia-travail worktree remove --force /home/user/wt-t07-cl` (ton arbre seulement). Regarde `df -h /home/user` avant ; sous 3 Go libres, n'extrais pas et dis-le.

## À lire

- Texte : `brouillons/T0.7-sondes-v0-v1-brouillon19.md` (`07039ed2…`), section « Module » (l. 2094 à 2467), plan (point 8, étapes A et B), « Métrique », table des prédictions, « Critères de lecture gelés », « Liste d'arrêt » ; décision `docs/decisions/decision-N-066-v1.md` (`21e83ed5…`).
- Rapports du développeur : `docs/notes/g0-deux-semaines-v1/t07-module-v2/rapport-developpeur-t07-module-v2.md` (`b4d5784b…`) et `…-complement-v1.md` (`06909a73…`) : écarts, **dix-neuf interprétations**, Q9 à Q11, ce qui reste.
- Code au commit `1f77b34d` : `src/controle_ia/t07/` (douze modules, dont les six de v1 égaux à `51a1874c`), `tests/test_t07_*.py`, `scripts/repetition_jouet_t07_v1.py`, configuration brouillon `brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v1.json`.
- Texte scellé de T0.6, section « Concordance avec T0.7 » : `prereg/T0.6-organismes-v0-v1.md` (`ef31feff…`).

## Points à juger

1. **Conformité texte → code** de chaque exigence du brouillon 19 qui touche le module (section, ligne → fichier, ligne) : fait, écart, absent ; en particulier (x) à (xv), garde adaptée G1 à G6 et R14 (N-066), journal de P3-bis au format b8, sondes neuves de l'étape A (30 couples, sonde principale et règle d'ex aequo, empreinte consignée avant toute notation), lectures T7-P3 à T7-P19, placebo, base « coût seul », réserves R1 à R13, Q11.
2. **Les dix-neuf interprétations** : acceptable, à corriger, ou à porter au texte ; une ligne de raison chacune.
3. **Embargo et ordre des lectures** : aucun chemin du module ne lit une sortie fermée par DT-4 avant le verdict scellé de P3-bis ; `sondes_lues` et l'ouverture réduite (N-066) ne peuvent pas s'élargir après la première ouverture ; aucune lecture de 7a.
4. **Gardes** : chaque garde d'arrêt avec un cas sain et un artefact (R5) ; aucun repli silencieux ; graines par `SeedSequence` dérivées par clé (R9) ; **aucune moyenne ni médiane sur les jetons dans une sonde de production** ; codes de sortie 0, 2, 3.
5. **Ce qui reste** (T7-P10 des sondes de P3, repli du recalcul, mode réel jamais joué) : bloquant pour le scellement de T0.7 ou non, et pourquoi.
6. Valeurs proposées pour `COMMIT_CODE_T07`, `EMPREINTES_CODE_T07` (recalcule les empreintes au commit) et `EMPREINTE_CONFIG_T07` : le code permet-il de les remplir ?

## Sortie

`docs/notes/g0-deux-semaines-v1/t07-module-v2/contre-lecture-code-t07-v1.md`, scellé (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>` depuis `/home/user/controle-ia-travail`) : verdict en une ligne ; table des défauts CT-01… (bloquant, à corriger, mineur ; fichier, ligne ; correction proposée) ; points 1 à 6 ; essais (comptes, durées, heures `date -u`). Réponse courte à la mère : chemin, empreinte, verdict, défauts bloquants.
