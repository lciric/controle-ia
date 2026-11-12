# Consigne : contre-lecture du code de P3-bis (commit `e86a6f32`) par un autre modèle — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10, écrite vers 04:58 UTC (`date -u`). Destinataire : un **contre-lecteur neuf, modèle Fable** (N-052 : autre modèle que le développeur, Opus ; servi en Fable 5.2 au lieu de 5.1, écart déclaré). Il n'a écrit ni le code de P3-bis, ni ses brouillons, ni T0.6, ni T0.7, ni leurs contre-lectures. **Il ne lit aucun fichier de T0.7** (ni brouillon, ni module `src/controle_ia/t07/`) : il reste ainsi éligible plus tard à d'autres rôles de P3-bis, et la règle « aucun fichier de T0.7 au lecteur de P3-bis » n'est pas entamée.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/interdits-communs-v1.md` (`851028fc…`), en entier. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni la branche `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. Aucun appel externe, aucune dépense, aucun `vastai`. Aucun `commit` ni action git qui écrit : la mère committe.

## À lire (dans le clone `/home/user/controle-ia-travail`, à `main`)

- Texte : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon9.md` (`eb65773f…`) ; configuration brouillon `brouillons/P3-bis-temoin-positif-v1/P3-bis-temoin-positif-config-v1-brouillon1.json` ; décision `docs/decisions/decision-N-066-v1.md` (`21e83ed5…`).
- Code (commit `e86a6f32`, inchangé depuis sur `main`, à vérifier par empreintes contre les compagnons) : `src/controle_ia/premier_test_ia/run_v2.py`, `lecture_p3bis_v1.py`, `ouverture_p3bis_v1.py` ; `scripts/essai_fermeture_p3bis_v1.py`, `scripts/p3bis_instance.sh`, `scripts/amorce_instance_p3bis.sh`, `scripts/essais-cibles-p3bis-v1.txt` ; les cinq fichiers d'essais neufs ; et, pour comparaison, le code de P3 qu'ils reprennent (`premier_test_ia/run.py` et voisins).
- Compte rendu du développeur : `brouillons/P3-bis-temoin-positif-v1/compte-rendu-developpeur-code-p3bis-v1.md` (`977d84c1…`, onze écarts déclarés).
- Défaut connu : `tests/test_cibles_invisibles_v1.py::test_inventaire_tout_constructeur_d_invite_est_examine` échoue (constructeur d'invite neuf `run_v2.py::executer` → `charger_invite` non inscrit ; R-2042 dans `registres/decisions.md`).

## Points à juger

1. **Conformité texte → code** : chaque exigence du brouillon 9 qui touche le code (section, ligne) contre ce que fait le code (fichier, ligne) : fait, écart, absent.
2. **Fermeture** (cœur de P3-bis) : aucune sortie en clair avant le verdict ; paquets de taille fixe, sel, bourre, seuil `zlib` ; canaux auxiliaires (durées, tailles, noms, journaux, codes de sortie) ; l'essai différentiel de fermeture couvre-t-il ces canaux ? Le rejouer une fois est permis (≈ 3 min ; dossier neuf sous `/home/user/cl-p3bis-tmp/`, effacé ensuite par son chemin exact).
3. **Les onze écarts du développeur** : acceptable, à corriger, ou à porter au texte ; une ligne de raison chacun.
4. **Le défaut de `run_v2.py`** : cause, correction proposée (fichier neuf ou inscription à l'inventaire de l'essai ; l'essai lui-même ne se modifie pas pour passer).
5. **Gardes** : chaque garde d'arrêt éprouvée sur un cas sain et sur un artefact (R5) ; graines par `SeedSequence` dérivées par tâche (R9) ; arrêts par identifiant (R10) ; aucune moyenne ni médiane sur les jetons dans une sonde de production ; garde d'ouverture (date du rendez-vous 2026-11-20T12:00:00Z, branche 1 de N-066).
6. **Ce qui manque avant le scellement** : lanceur `lancer_p3bis_v1.sh` (non écrit) et ce qu'il doit contrôler ; recompte de `TESTS_ATTENDUS_P3BIS` (436 provisoire) ; marqueurs de code du brouillon 9 que le code permet ou non de remplir.

Essais ciblés permis (la liste `scripts/essais-cibles-p3bis-v1.txt`, ≈ 12 min, `--basetemp` neuf sous `/home/user/cl-p3bis-tmp/`) ; pas la suite complète.

## Sortie

`brouillons/P3-bis-temoin-positif-v1/contre-lecture-code-p3bis-v1.md`, scellé (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`), avec : verdict en une ligne (« conforme », « conforme sous réserves », « non conforme ») ; table des défauts numérotés CP-01… (gravité : bloquant, à corriger, mineur ; fichier, ligne ; correction proposée) ; points 1 à 6 ; heures `date -u`. Réponse courte à la mère : chemin, empreinte, verdict, défauts bloquants.
