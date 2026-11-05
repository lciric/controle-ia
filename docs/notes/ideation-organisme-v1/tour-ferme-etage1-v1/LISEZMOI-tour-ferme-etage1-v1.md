# Tour fermé, étage 1 (GO-2026-11-02-23, 50 USD) — pièces de session-depot, v1

Écrit le 2 novembre 2026 (session-depot, instance 5 ; heure de l'en-tête relevée par `date -u` : 23:02 UTC). Rien n'est scellé ici
tant que conv-audit n'a pas levé la case `<<CASE_CONFIGURATION_V3>>` de son texte.

## Contenu
- `pieces/` : les six pièces de la configuration du 1er novembre (`configuration-mini-course-kimi-argon-v2.json`, sha256
  `4ae5a1e0947d44c1a08548d1b0197bfd96a2264f455189713b06183b2bc83108`), copiées à l'octet depuis la branche de données
  `donnees/recuperation-collisionneur-v8-v1` (commit `60656845`) ; empreintes égales à celles que la configuration v2 déclare
  (vérifié par `sha256sum`).
- `configuration-tour-ferme-v3-brouillon1.json` : brouillon 1 de la configuration v3, dérivée de la v2 par programme (voir
  `_lisez_moi` dans le fichier). Changements : `budget.plafond_usd` 10 → 50 ; `plafonds_session.proposeur` 1,8 → 0,5 ;
  commandes de Kimi et d'Argon → version 3 (`docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/`, en cours), avec
  `--plafond-cumule-usd 50`, le jeton `{REGISTRE}` et les options par rôle de l'annexe A ; clé neuve
  `etage_tests_de_mort.environnement_permis: []` ; tout le reste inchangé. **Brouillon** : les chemins et les options des commandes
  v3 seront confirmés quand elles existeront ; la version scellée portera un nom sans « brouillon » et une empreinte neuve.
- Lecture par le code public (`53aef4a`, `pole/configuration_v56.lire_configuration_v56`, pièces résolues depuis le dossier du
  fichier) : **conforme** sur le brouillon 1.

## Registre de GO
Le lecteur public `configuration_v53.lire_registre_go` refuse `registres/go.md` de `main` (« identifiant GO-2026-10-24-07 en
double », comme pour A1, R-1038). `configuration_v56.verifier_go_v56("GO-2026-11-02-23", registre, 50.0)` rend « accordé » sur
le registre de conv-audit (`canal/conv-audit-n04` à `d1b1c8c6`, sha256 `53985197d3e9780db9bf9738c050c3e746eea149af3e4024649f41db5cedef0a`)
et sur un extrait de `main` (en-tête du registre plus la seule ligne GO-2026-11-02-23). La commande exacte passera l'un des
deux, posé hors du clone.

## Ce qui manque avant `--verifier-seulement` et la course
1. Commandes v3 (TF-01 : les v2 refusent `experimentateur_test` et `lecteur_test`, message n° 294) et leurs essais.
2. Réponse de conv-audit sur TF-02 (un code 4 « rien envoyé » devient « erreur » et arrête la course).
3. Texte scellé de conv-audit (sans « brouillon »), empreinte de la configuration v3 définitive dans le plan gelé.
4. `bwrap` 0.9.0 et une identité dédiée sans privilège chez la machine qui lance ; `TMPDIR=/tmp` ; `POLE_MACHINE_JETABLE_V56=1` ;
   relais Kimi (`relais_kimi_v3.py`, port 8804) à plafond ≥ 44 USD et relais Argon (`servir`, port 8805) à plafond ≥ 6 USD, avec
   `--max-appels` suffisant (le 1er novembre : 3 USD et 7 USD, 60 appels) ; crédit Moonshot rechargé.
5. Décision de Lazar sur la garde de 24 h → 72 h (brief v2 de conv-audit, § 8.2).
