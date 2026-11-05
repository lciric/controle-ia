# Orchestrateur du pôle, version 0.7.0 — prise « idéation » durcie après la contre-lecture CL1 (« non lançable en l'état ») — LISEZMOI v32

Lignée conv-audit (instance de reprise du 28 octobre 2026, Fable 5.1), écrit après le relevé `date -u` de **16:58 UTC** ;
v1 à v31 gardées (R12). Répond à la contre-lecture CL1 de session-depot (`docs/notes/ideation-organisme-v1/contre-lecture-v31-cl1.md`
sur `main`, `f4c7d194…`, sous-agent neuf Opus 5.5 ; message n° 107). **v32 n'est pas contre-lue : le différentiel v31 → v32
doit être relu par un sous-agent d'un autre modèle que Fable avant tout lancement réel** (R2).

## Ce qui change, constat par constat

| constat | correction | fichiers |
|---|---|---|
| **CL31-01** bloquant : la panne du duel (R-599) pouvait se rejouer en silence | `appel_de_controle` : un appel par modèle, même adaptateur, mêmes options, avant la course (statut `ok`, texte « OK », coût déclaré > 0, et au relais un appel de plus et une dépense > 0) ; **arrêt dur** (`CourseInterrompue`) sur toute session de statut ≠ `ok` ou porteuse d'une erreur, avec statut et erreur réels dans le manifeste de fin ; lanceur : code 2 sur arrêt, 3 si aucun classement ; `valider_url_relais_ideation` : **http seulement, hôte local, aucun chemin** (le relais sert en clair) | `pole/ideation.py`, `demonstrations/ideation_v1.py` |
| **CL31-02** replis silencieux | plus aucun : proposeur ou juge en échec arrête ; fiches au-delà du nombre demandé → tout refusé avec motif (pas de troncature) ; liste vide refusée ; champ `passe` dans chaque fiche et chaque ligne ; `classement.json` porte `lisible_L2_L4` (faux si un témoin échoue ou un juge manque) | `pole/ideation.py` |
| **CL31-03** aucun témoin | **témoins plantés** écrits par un tiers (fichier JSON dans la liste blanche : fiche au gabarit, `attendu` éligible / inéligible, `note_max` par critère, `jumeau_de`), mêlés aux fiches, **exclus du classement**, lus à part contre un **critère gelé** (par juge seul : porte conforme, notes ≤ maximum, jumeau signalé en doublon) ; un seul échec rend L2 et L4 illisibles ; corrélation de rang longueur × total rapportée | `pole/ideation.py` (`charger_temoins`, `lecture_temoins`) |
| **CL31-04 / 11 / 12 / 17** juges des mêmes modèles, porte servie, « médiane » de deux, même ordre, clé écrite avant | lectures par juge (total moyen aux fiches de son propre modèle contre les autres), classements par juge, porte « unanimité » rapportée ; porte **retirée** de la consigne des juges ; agrégat **nommé** (moyenne à deux juges, médiane au-delà) ; **permutation et étiquetage par juge** (graine dérivée par juge), remis en correspondance par le noyau ; départage final documenté (total, max, robustesse, empreinte de la fiche) ; clé écrite **après** le dernier juge ; `empreinte`, `auteur`, `passe` retirés des fiches servies ; typographie normalisée ; étiquettes validées (`^[a-z0-9][a-z0-9-]{0,39}$`, uniques, « temoin » réservé). Un juge d'une autre lignée reste une décision de Lazar (N-053 point 4) : non codé | `pole/ideation.py` |
| **CL31-05** juges sans les pièces | `--piece-juge` : pièces d'antériorité servies aux juges ; sinon la grille cesse de parler « des pièces » et le dit | `pole/ideation.py` (`grille`) |
| **CL31-06** garde perméable, quarantaine resservie | motifs élargis (étapes et phases numérotées, « première étape », listes 1) 2), « pour / afin de » + contourner / échapper / déjouer / leurrer / tromper / éviter + moniteur / détecteur / sonde / juge, injection, exfiltration, stéganographie, porte dérobée, exploiter, commandes à exécuter) ; appliquée aux **réponses brutes** (journal) et aux fiches de passe 1 **avant** toute seconde passe ; une fiche en quarantaine n'est jamais resservie ; lecture humaine de **toutes** les fiches validées exigée par le devis | `pole/ideation.py` |
| **CL31-07** pièces contournables | **liste blanche d'empreintes** (`{chemin réel: sha256}`, écrite par `--construire-liste-blanche`, scellée par le devis) : question, pièces, matériau, pièces des juges et témoins refusés hors liste ou à empreinte différente ; liens symboliques refusés ; fragments interdits comparés après normalisation (accents, `_`, espaces) et élargis (`banque`, `prereg`, `test-final`, `bras-d-attaque`, `carte-hypotheses`) | `pole/ideation.py` |
| **CL31-08** outils et lectures | `OUTILS_PAR_ROLE` : **aucun outil** pour `proposeur_ideation` et `juge_ideation` ; `max_tours` ≤ 2 (refusé au-delà) ; lectures interdites sur la sortie, la **racine du dépôt** et le **dossier personnel** | `pole/adaptateurs.py`, `demonstrations/ideation_v1.py` |
| **CL31-09** coût | plafond **par rôle et par modèle** (`--budget role\|modele=…`, défauts : proposeur Opus 2, Fable 5 ; juge Opus 1,5, Fable 3 ; total 20) ; état du relais lu après chaque session, coût compté = max(déclaré, écart lu au relais) ; devis v2 refait avec réflexion et écriture du cache (≈ 5 à 10 USD) ; relais à lancer avec `--reserve-par-appel 3.5` | `pole/ideation.py`, devis v2 |
| **CL31-10** manifeste | **manifeste de départ** scellé avant le premier appel (empreintes du code, de la question, des pièces, du matériau, des témoins et de la liste blanche ; grille, porte, budgets, moteur, bac à sable, relais, versions, lecture de l'appel de contrôle) ; manifeste de fin avec journal, erreur éventuelle, fichiers écrits par les agents ; coûts d'un moteur simulé marqués **fictifs** | `pole/ideation.py` |
| **CL31-13** passe 2 remplaçait la passe 1 | les fiches des deux passes sont **jugées ensemble**, anonymes et mêlées, passe consignée | `pole/ideation.py` |
| **CL31-15** sonde du bac à sable | `etat_bac_a_sable_detaille` : sonde `--unshare-pid --proc /proc` ; sans `/proc` neuf, refus sous root | `pole/adaptateurs.py`, lanceur |
| **CL31-16** affirmations fausses | docstrings et LISEZMOI réécrits pour dire ce que fait le code | tous |
| **CL31-18** essais | 21 essais (cas sains + artefacts R5 : liste blanche, liens, variantes de chemin, paraphrases devant la garde, session en erreur, fiches en trop, liste vide, juge invalide, témoins échoués, plafond, appel de contrôle refusé quatre fois, adresse du relais, étiquettes, max_tours, options sans outil) | `essais/test_v7_ideation.py` |

**Non corrigé, assumé** : CL31-14 (sections des pièces : le devis sert des extraits scellés à part, le code sert le fichier
entier) ; juge non Claude (nœud Lazar) ; neutralisation du style (mesurée, pas neutralisée).

**300 essais passent** (279 + 21). Course simulée de bout en bout (liste blanche de cinq fichiers, quatre témoins, deux
passes) : 11 fiches, témoins conformes, classement lisible, coûts fictifs ; commande fautive (pièce hors liste) : arrêt propre.

## Commandes

```
PY=/opt/venv-essaim-sim-v1/bin/python
$PY -B -m unittest discover -s essais -t . -p 'test_*.py'                              # 300 essais (découverte ; -m essais.x échoue sous -I)
$PY -I -B demonstrations/ideation_v1.py LISTE.json --construire-liste-blanche Q.md P1.md … TEMOINS.json
$PY -I -B demonstrations/ideation_v1.py SORTIE --liste-blanche LISTE.json --question Q.md --piece P1.md … \
    --temoins TEMOINS.json --piece-juge A1.md …                                          # simulé, sans dépense
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v32.txt
```

Lancement réel : voir `../ideation-organisme-approches-v1/devis-ideation-v2.md`. Le reste : LISEZMOI v31 à v1.
