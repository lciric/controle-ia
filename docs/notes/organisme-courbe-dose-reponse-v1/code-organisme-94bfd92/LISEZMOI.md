# Copie empreintée du code de l'organisme d'idéation, commit `94bfd92` — v1 (10 novembre 2026, 11:00 UTC)

Versée par la session-dépôt (`session_01QPDgKgcLdggoVJfGC5cBw8`), branche `claude/upbeat-cray-dmauvv`, pour la simulation
de dimensionnement, sans agents, de la courbe dose-réponse de la session « attaquant informé ».

## Autorisation

- Mot de Lazar, verbatim, inscrit sur `main` : R-2148 (10:22 UTC) : « (a) copie empreintée par la session-dépôt : go ».
  La décision y est écrite ainsi : « la session-dépôt verse une copie empreintée du code de l organisme, sans aucun
  résultat, pour la simulation de dimensionnement de la session du bras ».
- Confirmé par le « go recos » de Lazar de 10:48 UTC, consigné dans la session du bras
  (`registres/passations/2026-11-10-1050-decision-lazar-go-recos-acces-hc2-licence.md`, branche
  `claude/compassionate-meitner-d4ryyk`, commit `a1bd02c9`), point 1, option (ii).
- Périmètre fixé par la session du bras (message de 10:48 UTC) : l'ensemble du seul commit `94bfd92`, c'est-à-dire la
  fermeture des imports de ses huit fichiers de `orchestrator/pole/`, plus `pole/__init__.py`,
  `orchestrator/exemples/temoins-pari-demo-v1.json` et les compagnons. Elle ne veut ni le code de l'épreuve W2 graduée
  (qui n'existe qu'au commit `f39a7f4a`), ni le code des attaques A1 contre le juge.

## Source

- Dépôt public `https://github.com/lciric/ideation-organism`, lu de façon anonyme en lecture seule, sans exécution du
  code. Le commit est `94bfd92f9e1434208f2dd2ae5b6a948be4708a22`, du 2026-11-07 à 21:08:57 UTC, tête de la branche
  `claude/new-session-7qxayx` au relevé ; son arbre est `4e770e568e4f9cecf7043203358137c5c50ffb83`.
- Huit fichiers de départ : `nul_v8.py`, `a_blanc_v59.py`, `boucle_fermee_v59.py`, `selection_pari.py`,
  `tour_ferme_v64.py`, `oracle_tour_ferme_v60.py`, `tests_de_mort_v5.py`, `etage_entre_generations_v57.py`.
- Fermeture des imports internes à `orchestrator/pole/`, calculée par analyse syntaxique, sans importer ni exécuter le
  code : `outil-fermeture-imports-v1.py` (`d54d15e5…`), lancé avec `python3 -I` sur l'arbre extrait du commit. Elle
  compte **47 modules**. Aucun module `attaque_goodhart_*`, `bras_attaque_*`, `coffre_*`, ni de l'épreuve W2 graduée
  n'y entre.

## Contenu

- 53 fichiers sous `orchestrator/` : les 47 modules ; `pole/__init__.py` ; l'exemple
  `exemples/temoins-pari-demo-v1.json` ; les 4 compagnons `.sha256` que la source porte pour ces fichiers (`nul_v8.py`,
  `tests_de_mort_v4.py`, `tests_de_mort_v5.py`, `etage_entre_generations_v57.py`). Les quatre sont conformes.
- `empreintes-copie-v1.txt` : l'empreinte sha256 de chacun des 53 fichiers. Chaque fichier copié est identique, octet
  pour octet, au même chemin dans le commit source (53 sur 53, aucun écart).
- **Aucun résultat** : ni sortie, ni verdict, ni préenregistrement, ni journal. Aucune note, aucun score, aucun seuil.

## Ce que la session-dépôt n'a pas fait

Elle n'a pas exécuté le code, ne l'a pas modifié, et ne l'a pas relu pour en juger la justesse. La lecture qu'elle a
faite se limite aux noms des modules et aux instructions d'import.
