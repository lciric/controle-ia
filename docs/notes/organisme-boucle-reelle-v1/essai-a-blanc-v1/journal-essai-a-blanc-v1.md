# Journal de l'essai à blanc hors ligne de la boucle complète de l'organisme — v1

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur neuf : je n'ai écrit aucune pièce de l'organisme ni du
  programme de contrôle.
- **Heures** (temps universel, `date -u`, 7 novembre 2026) : essai de 23:28:42 à 23:52:40 ; journal écrit de 23:44 à 23:53.
- **Dépense** : aucune. Aucun appel de modèle, aucun réseau vers un fournisseur, aucune clé ni variable d'environnement lue.
- **Organisme** : `/home/user/ideation-organism`, commit `94bfd92`, lu seulement ; `git status --short` vide avant et après
  l'essai (vérifié à 23:28 et 23:43).
- **Interpréteur** : `/home/user/controle-ia-travail/.venv/bin/python -I -B` (Python 3.13.18, numpy 2.4.6, scipy 1.17.1,
  pytest 9.1.1). Écart dit : l'organisme documente ses courses sous numpy 2.5.3 ; le Python du système (numpy 2.5.3) n'a ni
  scipy (exigé par l'oracle `pole/oracle_tour_ferme_v60.py`) ni pytest, et la consigne interdit d'installer.
- **Commandes** : `lancer_essai_a_blanc_v1.sh` (dans ce dossier), jouées une à une.
- **Sorties** : les sorties complètes (991 fichiers, scellés par le code de l'organisme, compagnons `.sha256` compris) sont
  **hors de l'arbre** — `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/essai-a-blanc-v1-sorties-completes/`
  — parce que la consigne interdit tout `.sha256` dans l'arbre ; des copies sans compagnon sont sous `sorties/`.

## 1. Ce qui a été joué

| étape | commande (depuis `orchestrator/`) | heure (temps universel) | issue |
|---|---|---|---|
| 1 | `demonstrations/tour_ferme_v64.py … --a-blanc --graine 20261107 --bac reel --generations 2` | 23:28:42 et 23:43:34 | **refus, code 2** : « BacASableIndisponible : bac réel demandé : bwrap absent de cette machine : refus, aucun repli sur l'exécuteur factice » ; aucun dossier de sortie créé (`sorties/refus-bac-reel.txt`) |
| 2 | même commande, `--bac factice` (demandé explicitement) | 23:28:48 → 23:29:28 (39,7 s) | **code 0** ; relevé `tour-ferme-v1-etage1.json`, sha256 `2d19d6d3330dd9c62a9e4db841da9f96367512d97ff3eb0d145230b9322c1198` (égal à son compagnon hors de l'arbre) ; manifeste `4f8fc0e47250c346c445e20f6fd16286c893906bfb25448a0a26ddfc3a48bb65` |
| 3 | `demonstrations/lire_tour_ferme_v64.py SORTIE LECTURE --releve-sha256 2d19d6d3…` | 23:30 | **code 0** ; lecture `7a056ce1099c99cdb22247faeff5170f987a0344839448a49b18f3af7a32c42e` : issue « tient », A4 « discrimine », audit « trop beau » (S1) déclenché avant lecture |
| 4 | `pytest` sur `test_tour_ferme_v64.py`, `test_gardes_tour_ferme_v64.py`, `test_v59_boucle_fermee.py`, `test_v57b_cablage_verdict.py`, `POLE_ESSAI_BAC_REEL_NON_JOUE=1` | 23:33:55 → 23:35:32 | **169 réussis, 2 sautés (essais du vrai bac à sable, déclarés non joués), 117 sous-essais** ; `sorties/essais-v64-v59.stdout` (`bb5d09e2…`) |
| 5 | `puissance-boucle-reelle-v1.py … --repetitions 1000 --processus 4 --graine 20261107` (dossier parent) | 23:32:51 → 23:35:15 | code 0 ; `sorties-puissance-v1/puissance-boucle-reelle-v1-r1000.json`, `a23959fa07f4c76fbd85e4bfbac7b5e6edc9ac612ad91a449f1ac10c96cef990` (script `a2afcdd3…`) |
| 6 | `puissance-boucle-reelle-v1-generation2.py …` (mêmes réglages) | 23:37:09 → 23:42:45 | code 0 ; `sorties-puissance-v1/puissance-boucle-reelle-v1-generation2-r1000.json`, `fe2bc5027cd4f4eb7f4a96f286b7b37687b7b8fcfe608da3e186b75d75e7c111` (script `f552b1b9…`) |
| 7 | `essai-a-blanc-v1/comparer_numpy_v1.py` (`53252fcd…`) sous les deux interpréteurs : huit jugements (V1 à V4, F1 à F4, archive {K1}, une racine) | 23:52 | **log W maximaux égaux à l'octet** sous numpy 2.4.6 (environnement virtuel) et 2.5.3 (Python du système) ; `sorties/comparaison-numpy-2.4.6.txt` (`0cb2b16d…`), `sorties/comparaison-numpy-2.5.3.txt` (`c569103e…`) |

Deux essais préliminaires du script de puissance (4 et 8 répétitions, sur des états antérieurs des lois V3, V4 et F2 à F4,
graines 1 et 2) ont servi à régler les forces ; leurs sorties sont hors de l'arbre (`…/scratchpad/essai-puissance-2.json`,
`…/scratchpad/essai-puissance-4b.json`) et ne fondent aucun chiffre du brouillon.

## 2. Ce que montre l'étape 2 (toute la boucle de la v64, fournisseurs simulés)

La chaîne entière a tourné sur deux générations et trois bras (réel, aléatoire, recopie-mélange) : proposeurs (doublures
qui ne lisent que le texte servi), gardien mécanique, juge statistique sous le nul v8, étage des tests de mort v5 (expérimentateur
« famille-a » et vérificateur « famille-b », doublures ; exécuteur **factice**), contre-calcul par l'orchestrateur, sélection
scellée, lecture de la sélection par la génération 2.

- **La génération 2 lit la sélection** : `releve.boucle.lectures` porte, pour chaque bras, l'empreinte attendue et l'empreinte
  lue du bilan de la génération 1, égales (bras réel et recopie : `d587fcbc…` ; aléatoire : `5b707c9a…`), aucun incident ; les
  cartes réelles de la génération 2 sont jugées avec 12 membres d'archive (les 12 retenues de la génération 1), celles de la
  génération 1 avec 0.
- **Comptes** : 95 cartes ; 27 cartes et témoins testés, soit 54 sessions d'expérimentateur (relais « kimi ») et 27 de
  vérificateur (relais « argon ») ; consigne de l'expérimentateur 10 536 à 12 072 caractères (médiane 11 218), du vérificateur
  8 060 à 8 220, des proposeurs 13 552 (génération 1) et 15 730 (génération 2). Ces tailles servent au devis.
- **Témoins de la v64** (bras réel, génération 1) : T-VRAIE promue puis survivante ; T-ELIM promue puis éliminée ; T-MAL
  refusée au gardien ; T-F1, T-F4, T-ANTI refusées par le juge ; **T-F2 (loi fausse S-F2) promue par le juge, log e = 9,77,
  puis éliminée par son test de mort**. C'est le point qui casse le plus net pour la course demandée (section 4, M2). Le gain
  oracle de S-F2 est pourtant négatif (−0,143 nat par épisode, sortie de puissance `a23959fa…`, champ `oracle`) ; explication
  probable, non vérifiée ici : le plan d'instances de l'engagement retient une sous-région où la loi bat le nul (`README.md` de l'organisme,
  ligne 122, « the selector keeps instances where the law always predicts the same outcome »), et le test de mort, lui, porte
  sur toute la tranche. Une loi inconnue du pôle n'est donc protégée que par le test de mort, pas par le juge.
- Contre-calcul : 0 désaccord. Lecture gelée : « tient », avec l'audit « trop beau » déclenché (les doublures des proposeurs
  écrivent des lois voisines de la loi plantée : 12 sur 12 promues puis survivantes).

## 3. Ce que montrent les étapes 5 et 6 (le dessin exact, joué hors ligne par le juge de l'organisme)

Le dessin du brouillon 1 (archive de départ K1, quatre vraies, quatre fausses de la classe couverte, T-ELIM, génération 2)
n'a pas de lanceur dans l'organisme (section 4). Sa partie juge et test de mort est jouée par les fonctions mêmes de
l'organisme (`a_blanc_v59.juger_carte`, règle « hors famille » de `tour_ferme_v64.juger`, statistique de
`tour_ferme_v64.statistique_hors_bac` recopiée en mémoire), sur 1 000 répétitions :

| mesure | jugées avec les membres d'archive (dessin) | jugées sans (canal des témoins de la v64 : artefact) |
|---|---|---|
| au moins une vraie promue puis survivante et aucune fausse promue | **1 000 / 1 000** (Wilson [0,9962 ; 1]) | — |
| fausses promues (F1 à F4), génération 1 | **0 / 4 000** ; plus grand log W max : −0,004 | **au moins une dans 994 / 1 000** ; 725 à 810 / 1 000 chacune |
| toutes les vraies promues puis survivantes | 318 / 1 000 (V3 : 617, V4 : 501, V1 et V2 : 1 000) | — |
| T-ELIM promue puis éliminée | 1 000 / 1 000 | — |
| génération 2 : vraie retenue en génération 1 de nouveau promue | **0** (toutes refusées ; plus grand log W max de V1 : −0,018) | **1 000 / 1 000** si la génération 2 ne lit pas la sélection |
| génération 2 : fausse promue | 0 / 4 000 | — |

## 4. Ce qui casse, ou manque dans l'organisme (aucun contournement écrit)

| repère | constat | effet sur la course demandée | ce qu'il faut |
|---|---|---|---|
| M0 | **`bwrap` absent de cette machine** : le vrai bac à sable n'a pas pu tourner ici ; la garde refuse proprement (code 2, aucun repli). Le rapport v59 dit l'avoir joué le 2 novembre ailleurs (`bwrap` 0.9.0, identité 64097). | Les tests de mort de l'essai sont passés par l'exécuteur factice : rien n'est montré ici du bac réel. | Une machine jetable avec `bwrap` ≥ 0.9, un utilisateur dédié sans privilège ; essai à blanc `--bac reel` rejoué là avant la course (liste d'arrêt du brouillon). |
| M1 | La v64 commence toujours par une archive vide ; aucune « génération 0 » déclarée. | L'archive de départ K1, qui seule rend la classe couverte non vide, ne peut pas être posée. | Code v65 : héritage de départ scellé (bilan de génération 0, loi K1 marquée « connue, déclarée »), accepté par `lire_heritage` seulement si son empreinte est dans le texte scellé. |
| M2 | Les témoins de la v64 sont fixes (`TEMOINS` : T-VRAIE, T-F1, T-F2, T-F4, T-ANTI, T-ELIM, T-MAL). S-F1, S-F2, S-F4 et T-ANTI sont des lois inconnues du pôle : **classe non couverte** (`pole/nul_v8.py`, docstring). T-F2 est promue par le juge à la graine 20261107. | Contraire à GO-2026-11-07-11 (« fausses lois limitées à la classe que le nul couvre »). | Code v65 : jeu planté du brouillon (V1 à V4, F1 à F4, T-ELIM, T-MAL), lu dans le texte scellé. |
| M3 | La v64 juge les témoins **sans** membres d'archive (`juger(…, {}, …)`, ligne « témoins : sans membres d'archive »). | Les fausses de la classe couverte seraient promues : au moins une dans 994 répétitions sur 1 000 (section 3). | Code v65 : lois plantées jugées avec l'archive de jugement de leur génération, hors de la famille des cartes réelles, au seuil log(m/α). |
| M4 | La v64 joue toujours trois bras ; le bras réel seul n'est pas une option. | Les deux bras de référence ajoutent des tests de mort payants (27 testés au lieu d'environ 17 dans l'essai). | Code v65 : bras réel seul (option scellée), ou garder les bras et payer (devis, ligne « variante »). |
| M5 | La lecture gelée `pole/lecture_tour_ferme_v63.py` applique les critères T1 à T5 du tour fermé, pas ceux du brouillon (C1 à C6). | Aucune lecture gelée du dessin. | Code v65 : lecture gelée des critères de la section 8 du brouillon, avec essais sur cas sain et artefact. |
| M6 | Les commandes v6 de Kimi et d'Argon que nomme `configuration-tour-ferme-v4.json` (`docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/…`) **ne sont pas dans cet arbre** (`main` à `b014b784`) ni dans aucune référence locale. | Le mode réel ne peut pas démarrer ici. | Verser `outils/commandes-tour-ferme-v1` (`12f9e0e3`, R-1129) avant toute course ; configuration v5 qui les nomme. |
| M7 | Interpréteur : numpy 2.4.6 ici contre 2.5.3 documenté (le Python du système, en 2.5.3, n'a ni scipy ni pytest). | Aucun écart vu : huit jugements du dessin égaux à l'octet sous les deux versions (étape 7) ; les simulations de 1 000 répétitions et les essais n'ont tourné que sous 2.4.6. | Rejouer l'essai à blanc et les essais sous l'interpréteur de la machine de la course. |

Rien d'autre n'a cassé : aucune exception, aucun repli silencieux, aucune écriture dans l'organisme.
