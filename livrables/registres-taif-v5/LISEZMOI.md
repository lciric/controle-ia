# Registres pour l'entretien, v5 — recalcul du 10 novembre 2026 (session-dépôt)

Les six tables de ce dossier sont produites par `scripts/registres_taif_v3.py` (`3e4e15c0…`, intact, compagnon conforme),
sans aucune cellule saisie à la main ; la septième, `comptes-par-preenregistrement-v1.md`, par
`scripts/comptes_par_preenregistrement_v1.py` (nouveau, scellé avec ses essais), qui ne fait que compter les lignes de
`calibration-v3.md`. La v4 (`livrables/registres-taif-v4/`, calibration `0f1bca5a…`, 8 novembre) reste telle quelle (R12) :
c'est elle que cite le programme d'entretien v18.

## Ce qui a été lu

- **Arbre lu par le script** : l'archive de `origin/main` au commit `7163ad84` (10 novembre, 10:37:11 UTC), plus huit
  fichiers scellés de `claude/upbeat-cray-dmauvv` (tête `7aaf2de3`), absents de `main` à cette heure :
  - `docs/verdicts/verdict-T0.3-simulation-lemme-theoreme-v1.md` (`bc53b746…`) et son compagnon ;
  - `prereg/preenregistrement-mesure-unanime-v15.md` (`3a1651f4…`) et son compagnon ;
  - `prereg/lectures-possibles-mesure-unanime-v2.md` (`3e324090…`) et son compagnon ;
  - `prereg/usages-anterieurs-scores-p3-mesure-unanime-v2.md` (`d5ffe7cb…`) et son compagnon.
  C'est l'état qu'aura `main` quand ces pièces y seront fusionnées. `donnees/`, `diag/` et `docs/notes/bras-attaque/` ont
  été retirés de la copie avant le calcul ; le script ne les lit pas (il le dit dans son en-tête).
- **Commande** : `PYTHONPATH=src python3 scripts/registres_taif_v3.py --racine <copie> --sortie livrables/registres-taif-v5 --jour 2026-11-10`, code de sortie 0.
- **Déterminisme** : un premier calcul, dans le dossier de travail de la session, sur la même copie, a donné les six
  fichiers au même octet près.
- **Aucune pièce de la quarantaine** de la mesure unanime n'a été lue : ni la branche `donnees/mesure-unanime-v15-sortie-v1`,
  ni son arbre. Les neuf lignes de la mesure unanime sont donc « sans run décisif cité par un manifeste » : c'est l'état
  des pièces lues, pas une issue.

## Ce qui change dans la calibration par rapport à la v4

Comparaison ligne à ligne (préenregistrement, prédiction, issue) :

- **T0.3** (simulation du lemme et du théorème négatif) : les 31 lignes passent de « registre des décisions (sans verdict
  scellé) » à « confirmée », par le verdict scellé du 10 novembre.
- **T0.6 v0** (organismes, `prereg/T0.6-organismes-v0-v1.md`, paru sur `main`) : dix lignes nouvelles, T6-1 à T6-10, « sans
  run décisif cité par un manifeste ».
- **Mesure unanime v15** : neuf lignes nouvelles, « sans run décisif cité par un manifeste » (voir plus haut).
- **R1, addendum de relance v4** : « sans run décisif » devient « non encore lue (run décisif fait, aucun verdict scellé) ».

Comptes : 254 lignes (235 en v4) ; tranchées 91 (60) ; confirmées 78 (47), réfutées 5 (5), non concluantes 8 (8) ; taux
parmi les tranchées 78 / 91 = 0,857 (0,783).

## Lecture prudente (R4) : `comptes-par-preenregistrement-v1.md`

Le taux de 0,857 est porté par des vérifications. Par groupe (définition dans l'en-tête du script) :

- preuves en simulation (T0.3) : 31 / 31 — « l'issue attendue par construction » (verdict T0.3, l. 25) ;
- instruments (harnais T0.4, trois versions du préenregistrement comptées séparément ; revalidation T0.5 v2) : 32 / 33 ;
- prédictions empiriques (P3, pilote T0.5, agrégateurs, audit de fuite, étiqueteur) : **15 confirmées, 5 réfutées,
  7 non concluantes : 15 / 27 = 0,556**.

Le classement en trois groupes est un choix de la session-dépôt, à contre-lire ; il ne change aucune ligne de la table.

## Ce que la session-dépôt n'a pas fait

Relire les trois autres tables (promis et livré, coût par résultat, total des dépenses) : elles sont celles du même calcul,
sur les registres de `main` à `7163ad84`, et n'ont pas été comparées à la v4. Aucune dépense. Aucune instance.
