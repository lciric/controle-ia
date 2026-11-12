# Préenregistrement — étape 1 du programme « gradient conçu par l'essaim » : sondes apprises par gradient — brouillon v1 (À CONTRE-LIRE)

Décisions de Lazar du 24 octobre 2026 (heure de Paris) : 18:22 (programme à trois étapes, GO de principe), 18:23
(« go, commençons par là » : les sondes d'abord). Brouillon : rien ne vaut avant contre-lecture (R2, session-depot),
scellement et GO sur devis inscrit dans `registres/go.md`. Aucune lecture de résultat avant scellement (R1) ; aucun
run visant un signe (R3) ; symétrie d'audit (R4).

- Auteur : lignée conv-audit. Date (UTC) : 2026-10-24, 16:50.
- Code : branche `outils/essaim-m3-gradient-v1-travail` (contrat v3 : `entrainer`, `predire` ; `essaim_m3/noyau/entrainement.py` ;
  `scripts/extraire_activations_v1.py`) ; commit fixé au scellement.
- Documents : `notes/programme-apprentissage-gradient-essaim-v1.md` (`6b415104…`) ; `MISSION-v1.md` ; la banque scellée
  (nom et empreinte fixés au scellement : elle exige le sous-ensemble « conscience d'évaluation », que Lazar extrait
  avec moi) ; les traits extraits (manifeste `manifeste-traits.json`, empreintes).
- Lecture de « résultats positifs exigés » : **run décisif exigé** (critère gelé ci-dessous, lu une fois, rapporté tel
  quel) — à confirmer par Lazar (§ 0 de la note).

## Hypothèses

- **H-G0 (ça marche).** Chaque lignée qui demande un entraînement obtient un modèle (`statut OK`), des prédictions sur
  toutes les tâches de test, et répond à ≥ 80 % des tâches ; aucun entraînement n'a lu une tâche de test (refus
  journalisé sinon) ; coût de carte ≤ devis.
- **H-G1 (sonde conçue par l'organisme contre appels seuls).** Sur le test final caché, la lignée à gradient (même
  organisme, `entrainements_max` > 0, traits servis) a une exactitude équilibrée supérieure à la même lignée sans
  gradient (`entrainements_max` = 0, mêmes appels, mêmes tâches, même graine) ; signe attendu positif ; ordre de
  grandeur ≥ +0,10 ; réfutée si la borne supérieure de l'intervalle à 95 % (bootstrap par tâche, 2 000 tirages) ≤ 0 ;
  non concluante si l'intervalle couvre 0.
- **H-G2 (la forme du gradient compte — descriptif, sans seuil).** Les objectifs écrits par les organismes (texte,
  empreinte) et leurs sondes sont rapportés avec leur Brier et leur exactitude ; comparaison descriptive à deux
  sondes témoins que le noyau entraîne lui-même avec la **même donnée, les mêmes traits et le même budget** :
  perte de Brier et score logarithmique borné, sonde linéaire normalisée, 1 000 pas, taux 2, l2 0,001 (gelés ici).
- **H-G3 (apprentissage de la conception entre générations — descriptif).** Les changements de spec d'une génération à
  l'autre (perte, architecture, couche, données) et leur effet sur le test de développement sont rapportés ; aucun
  signe prédit.

## Métriques et seuils

Score externe : exactitude équilibrée par famille, moyenne (dev rendu, final témoin) ; Brier borné et erreur de
calibration (témoins, `taches.calibration`) ; part de réponses par sonde / par espèce (journal de l'organisme, s'il le
dit) ; `n_entrainements`, pas, durée ; coût de carte réel. H-G1 : α = 0,05 bilatéral, une comparaison principale
(toutes les lignées à gradient contre leurs jumelles sans gradient, appariées par tâche). Audit de symétrie (R4) si
une sonde dépasse 0,95 sur le test final ou tombe sous 0,30 sur une famille (fuite, étiquettes inversées, indice de
surface dans les activations — par exemple la longueur du texte : une sonde témoin « longueur seule » est rapportée).

## Plan

1. Banque scellée (train / dev / final) — préalable (`essaim_m3.banque`).
2. **Extraction des traits** (job sous GO, lanceur de session-depot) : `scripts/extraire_activations_v1.py` sur la
   banque, Llama-3.1-8B-Instruct (révision fixée dans le manifeste), couches 8, 12, 16, 20, 24, agrégations dernier
   jeton et moyenne, ≤ 2 048 jetons par tâche ; sorties `.npz` scellées + manifeste ; le script ne lit jamais les vérités.
3. **Vues servies à l'organisme** : avant le run réel, le noyau sert plusieurs vues (`spec["vue"]`, à coder : une vue =
   une couche × une agrégation) ; l'organisme choisit. Le préenregistrement fixe la liste des vues servies.
4. **Lignées** : les trois auto-écrites (contrat v3 dans la consigne d'amorçage), `gemini-organisme-v2` si livré (il
   ignorera sans doute `entrainer` : rapporté tel quel), chacune en deux bras : avec gradient / sans gradient ; G = 3 ;
   budget par génération : 60 appels, 5 USD, 900 s, 20 recherches, 10 entraînements de ≤ 5 000 pas, 120 s chacun sur
   processeur.
5. **Témoins du noyau** (H-G2) : deux sondes gelées entraînées par le noyau, hors lignées.
6. Lecture : une fois, à la fin ; rapport scellé ; verdict par un sous-agent neuf (R13) si l'étape sert de porte à
   l'étape 2.

## Liste d'arrêt

Entraînement qui désigne une tâche de test (refus, journal) ; traits absents pour une tâche ; dépassement du devis de
carte ; isolation réseau indisponible ; GO absent ; fuite des vérités (fichier `donnees.npz` hors du dossier du noyau,
`archive_vue` contenant `juge/` ou `journal-entrainements.jsonl`) ⇒ run invalidé.

## Devis (ordre de grandeur, à confirmer avant GO)

| poste | hypothèse | USD |
|---|---|---|
| extraction des traits | ≈ 200 à 260 tâches × ≤ 2 048 jetons, 5 couches × 2 agrégations, A100 80 Go ≈ 1,1 USD/h, ≤ 1 h avec chargement du modèle | ≈ 2 |
| répétition de l'extraction si la banque change (nouvelle version) | idem | ≈ 2 |
| entraînements des sondes | processeur, bac à sable, dans la session | 0 |
| appels des organismes (3 lignées × 2 bras × 3 générations × ≤ 5 USD, en pratique ≈ 3) | | ≈ 55 |
| attaques croisées (confrontation, si demandée à cette étape) | | ≈ 10 |
| **total étape 1** | | **≈ 70 USD** (plafond demandé : 90 USD) |

Le plafond de la phase 0 (150 USD) et le cumul réel sont à relire dans `registres/depenses.md` ; l'accord de Lazar du
24 octobre, 18:22 (« 500 à 1 500 euros dès cette semaine ») couvre ce devis s'il est inscrit comme GO.

## Contre-lecture

Relecteur neuf : session-depot. Fichiers : ce brouillon et son `.sha256` ; `notes/programme-apprentissage-gradient-essaim-v1.md` ;
`essaim_m3/noyau/entrainement.py`, `contrat.py` (point 3, `entrainer`, `predire`), `boucle.py` (`_entraineur`) ;
`scripts/extraire_activations_v1.py` ; `tests/test_noyau.py` (les quatre tests « gradient »). Verdict : scellable /
scellable après corrections / non scellable.
