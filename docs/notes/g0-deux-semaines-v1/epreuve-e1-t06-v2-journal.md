# Épreuve E1 du lanceur de T0.6 v2 — répétition jouet avec le vrai lanceur v2 sous la vraie amorce v2 (0 USD, sans réseau)

- Développeur neuf du lanceur v2 (Claude Fable 5.1, sous-agent) ; épreuve E1 de la contre-lecture du lanceur v1. Jouée le
  2026-11-05 à 20:28 UTC (`date -u`), 33 s de bout en bout, sur le processeur de la session, sans réseau : dépôt distant
  simulé par un dépôt git local nu, outil de location absent du chemin (vérifié par le script), aucune minuterie
  (`AMORCE_ESSAI_LOCAL=1`), environnement Python existant du dépôt (`VENV_EXISTANT`), essais joués par l'amorce avant le run
  limités aux essais de configuration et de session v2 (`TESTS_ARGS`, permis en répétition jouet seulement).
- Script : `scripts/epreuve_e1_t06_v2.sh` ; il bâtit un dépôt source réduit (code `src/controle_ia`, essais v2, consignes de
  P3 scellées, configuration jouet v3 dont les empreintes des tâches synthétiques sont remplies puis scellée, invites,
  registre des GO, garde de calcul, `.gitignore`), le clone en dépôt nu, puis lance `scripts/amorce_instance_t06_v2.sh`
  avec `COMMIT`, `MODE=jouet`, `PREREG_ABSENT=1`, `CONFIG`, `FIN_GO_UTC_S=1794873600`, `ECHEANCE_UTC_S`,
  `DEPENSE_EPUISEE_UTC_S`, `GH_TOKEN` factice. L'amorce clone, vérifie le GO, les citations, les sceaux, le calendrier (L11),
  pousse la branche, joue les essais, lance `python -m controle_ia.t06.lanceur_v2` (modèle par caractères, 4 tâches, 2 de
  réserve, T = 2, 7 conditions, 14 couples), relaie les lignes `PROGRES`, pousse (données légères, morceaux, traces), pose
  `t06-fin-normale`, demande l'arrêt.
- Deux lancements précédents, consignés : (i) nombre de tests attendus faux (40 au lieu de 44) → l'amorce s'est arrêtée
  avant le run (« tests : « 44 passed » ≠ « 40 passed » : arrêt », traces poussées, code 1) : la garde fonctionne (artefact
  involontaire) ; (ii) dépôt réduit sans `.gitignore` → le manifeste a refusé le dépôt sale (`__pycache__`), « RUN MORT »
  consigné, traces poussées, arrêt demandé : la garde du run mort fonctionne. Le script corrigé copie `.gitignore`.

## Commande exacte

```
cd /home/user/wt/t06-lanceur-v2 && VENV=/home/user/controle-ia-travail/.venv timeout 900 nice -n 10 bash scripts/epreuve_e1_t06_v2.sh <bloc-notes>/e1
```

## Lecture

- Lignes `PROGRES` relevées au journal de l'amorce : 36 lignes, toutes de la forme `etape=… compte=… duree_s=…` ; aucune ne
  porte un état de jeu, une aire, une ligne de table (C01) ; `run.json` (sortie standard du lanceur, versée aux traces) ne porte
  ni `ligne_A`, ni `ligne_B`, ni `ligne_C` (C02) ; le résumé scellé sous `diag/` les garde. Recherche des mots « au-dessus »,
  « interprétable », « échec », `ligne_A/B/C`, `table_`, `aire=`, « plancher » dans le journal, `run.err`, `run.json` et
  chaque fichier de traces poussé : **0 occurrence partout**.
- Morceaux : 1 morceau de 8 746 octets (10 actions, couche 2, demi-précision), manifeste scellé ; plus gros fichier poussé
  1 996 800 octets (`docs/sources/invites-…`, du dépôt réduit) : tout sous 90 Mo (C11). Trois commits poussés après le run,
  dans l'ordre : résultats et données légères ; morceaux ; traces (C11).
- Disque de l'instance simulée : `t06-fin-normale`, `t06-arret-demande` (« stopped (fin du run) »), `t06-consigner.sh`,
  `t06-echeance.txt`, `t06-depense-epuisee-utc.txt` ; aucun `t06-detruire` (C13, C14 posés).
- Contrôles négatifs de la garde d'équivalence « non concluant » sur S50, S100 et T100 : effectif jouet trop petit (8 actions
  par phase, `actions_min_controle_negatif` 10) ; c'est la garde d'équivalence, pas un état de sonde ; en jouet, non décisif.

## Sortie du script (copie de `resultat-e1.txt`)

```
# Résultat de l'épreuve E1 (2026-11-05T20:29:13Z), code de l'amorce 0
## lignes PROGRES relevées au journal de l'amorce
PROGRES 2026-11-05T20:28:51Z etape=format verifie=True
PROGRES 2026-11-05T20:28:51Z etape=disque libre_go=6.8 pire_cas_go=0.0
PROGRES 2026-11-05T20:28:52Z etape=distillation-donnees lot=1/1
PROGRES 2026-11-05T20:28:52Z etape=donnees-distillation saboteur_exemples=2 temoin_exemples=2
PROGRES 2026-11-05T20:28:53Z etape=distillation adaptateur=saboteur epoque=1 perte=4.8957
PROGRES 2026-11-05T20:28:53Z etape=adaptateur adaptateur=saboteur empreinte=dc25ba162d7d628a48b69438e6d2113bb140c157e7f5a31634b1aaf93ec2b98d perte_finale=4.8957
PROGRES 2026-11-05T20:28:53Z etape=distillation adaptateur=temoin epoque=1 perte=4.8938
PROGRES 2026-11-05T20:28:53Z etape=adaptateur adaptateur=temoin empreinte=e793212c2141ea49c4779021a2cd34b8c1b452f5e90dcbd63b90d65fa7bade71 perte_finale=4.8938
PROGRES 2026-11-05T20:28:54Z etape=identite adaptateurs=2
PROGRES 2026-11-05T20:28:55Z etape=episodes phase=dose0 lot=1/4 actions=8
PROGRES 2026-11-05T20:28:56Z etape=episodes phase=dose0 lot=2/4 actions=16
PROGRES 2026-11-05T20:28:57Z etape=episodes phase=dose0 lot=3/4 actions=24
PROGRES 2026-11-05T20:28:58Z etape=episodes phase=dose0 lot=4/4 actions=32
PROGRES 2026-11-05T20:28:59Z etape=episodes phase=S50 lot=1/1 actions=40
PROGRES 2026-11-05T20:28:59Z etape=episodes phase=S100 lot=1/1 actions=48
PROGRES 2026-11-05T20:29:00Z etape=episodes phase=T100 lot=1/1 actions=56
PROGRES 2026-11-05T20:29:00Z etape=episodes-ecrits episodes=28 actions=56 morceaux=1
PROGRES 2026-11-05T20:29:00Z etape=lecture-cout duree_s=12.1
PROGRES 2026-11-05T20:29:01Z etape=test-croise jeux=2 duree_s=0.2
PROGRES 2026-11-05T20:29:01Z etape=couple-descriptif couple=difference_moyennes-c1 duree_s=0.1
PROGRES 2026-11-05T20:29:02Z etape=couple-descriptif couple=lineaire-c1 duree_s=0.6
PROGRES 2026-11-05T20:29:03Z etape=couple-descriptif couple=perceptron-c1 duree_s=0.8
PROGRES 2026-11-05T20:29:04Z etape=couple-descriptif couple=attention-c1 duree_s=1.0
PROGRES 2026-11-05T20:29:04Z etape=couple-descriptif couple=mahalanobis-c1 duree_s=0.1
PROGRES 2026-11-05T20:29:05Z etape=couple-descriptif couple=lineaire-c2 duree_s=0.6
PROGRES 2026-11-05T20:29:06Z etape=couple-descriptif couple=perceptron-c2 duree_s=1.0
PROGRES 2026-11-05T20:29:07Z etape=couple-descriptif couple=attention-c2 duree_s=1.0
PROGRES 2026-11-05T20:29:07Z etape=couple-descriptif couple=mahalanobis-c2 duree_s=0.1
PROGRES 2026-11-05T20:29:07Z etape=couple-descriptif couple=difference_moyennes-c3 duree_s=0.1
PROGRES 2026-11-05T20:29:08Z etape=couple-descriptif couple=lineaire-c3 duree_s=0.6
PROGRES 2026-11-05T20:29:09Z etape=couple-descriptif couple=perceptron-c3 duree_s=1.2
PROGRES 2026-11-05T20:29:10Z etape=couple-descriptif couple=attention-c3 duree_s=0.9
PROGRES 2026-11-05T20:29:10Z etape=couple-descriptif couple=mahalanobis-c3 duree_s=0.1
PROGRES 2026-11-05T20:29:10Z etape=fin episodes=28 actions=56
## lignes AMORCE (sortie)
AMORCE T06 v2 DEMARRAGE 1 : 2026-11-05T20:28:40Z, machine ?, commit 0bbf3b65804b44f74d20607bb94a376dd3f457f4
AMORCE 2026-11-05T20:28:40Z : commit 0bbf3b65804b44f74d20607bb94a376dd3f457f4
AMORCE 2026-11-05T20:29:13Z : fin, code 0
## mots interdits (au-dessus, non interprétable, échec, ligne_A/B/C, table_, aire=, plancher) dans le journal, run.err, run.json, traces poussées
/tmp/claude-0/-home-user-controle-ia-travail/dab53617-317d-5e41-8722-0e36079bc80b/scratchpad/e1/instance/t06/journal.txt : 0 occurrence(s)
/tmp/claude-0/-home-user-controle-ia-travail/dab53617-317d-5e41-8722-0e36079bc80b/scratchpad/e1/instance/t06/run.err : 0 occurrence(s)
/tmp/claude-0/-home-user-controle-ia-travail/dab53617-317d-5e41-8722-0e36079bc80b/scratchpad/e1/instance/t06/run.json : 0 occurrence(s)
traces : traces/t06-20261105-202913-t4hc/empreintes.sha256 : 0 occurrence(s)
traces : traces/t06-20261105-202913-t4hc/journal.txt : 0 occurrence(s)
traces : traces/t06-20261105-202913-t4hc/pip-freeze.txt : 0 occurrence(s)
traces : traces/t06-20261105-202913-t4hc/progres-retenues.txt : 0 occurrence(s)
traces : traces/t06-20261105-202913-t4hc/run.err : 0 occurrence(s)
traces : traces/t06-20261105-202913-t4hc/run.json : 0 occurrence(s)
traces : traces/t06-20261105-202913-t4hc/tests.err : 0 occurrence(s)
traces : traces/t06-20261105-202913-t4hc/tests.txt : 0 occurrence(s)
## run.json (sortie standard du lanceur, versée aux traces)
{"commit_cite": null, "config_sha256": "bace3c83b06848efde1041a7c60039618a5808eaed85688905a70e84525207a9", "taches_evaluation_sha256": "07bad118777bcca325aea53ef3a588fc4e150f6aab14167b3f35b522ca775728", "consignes_sha256": "a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c", "adaptateurs": {"saboteur": "dc25ba162d7d628a48b69438e6d2113bb140c157e7f5a31634b1aaf93ec2b98d", "temoin": "e793212c2141ea49c4779021a2cd34b8c1b452f5e90dcbd63b90d65fa7bade71"}, "mesures_sha256": "875765661229d480e255f4f8bf32014863f3113e078e150e12894a013c3257a0", "textes_sha256": "b906ee134068f8f004614dd44f7ec35d9facd1287f72d797e8e65a0c286a02e6", "sous_ensemble_manifeste_sha256": "06617e334b0594b425c48ebd43217c3b2aad3229e0013185d3dbe3d62c9a48b8", "morceaux": 1, "episodes": 28, "actions": 56, "actions_notees": 42, "controles_negatifs": {"dose0": "conforme", "S50": "non concluant", "S100": "non concluant", "T100": "non concluant"}, "duree_s": 22.0}
## commits poussés sur le dépôt distant (branche calcul/t06-jouet-v2)
118a23b T0.6 : traces de l'instance (fin)
a187d69 T0.6 (jouet), run 20261105-202846-t06-jouet : sous-ensemble d'activations en morceaux (< 90000000 octets chacun)
aba5e6b T0.6 (jouet), run 20261105-202846-t06-jouet : résultats et données légères
0bbf3b6 E1 : dépôt source réduit
## fichiers poussés sous donnees/ (taille en octets)
8746 donnees/20261105-202846-t06-jouet/activations-sous-ensemble-t06-000.npz
104 donnees/20261105-202846-t06-jouet/activations-sous-ensemble-t06-000.npz.sha256
543 donnees/20261105-202846-t06-jouet/activations-sous-ensemble-t06-manifeste.json
111 donnees/20261105-202846-t06-jouet/activations-sous-ensemble-t06-manifeste.json.sha256
14475 donnees/20261105-202846-t06-jouet/adaptateur-saboteur.pt
89 donnees/20261105-202846-t06-jouet/adaptateur-saboteur.pt.sha256
14399 donnees/20261105-202846-t06-jouet/adaptateur-temoin.pt
87 donnees/20261105-202846-t06-jouet/adaptateur-temoin.pt.sha256
18078 donnees/20261105-202846-t06-jouet/mesures-t06.npz
82 donnees/20261105-202846-t06-jouet/mesures-t06.npz.sha256
8804 donnees/20261105-202846-t06-jouet/textes-actions-t06.jsonl
91 donnees/20261105-202846-t06-jouet/textes-actions-t06.jsonl.sha256
242 donnees/t06-jouet/taches-distillation.json
91 donnees/t06-jouet/taches-distillation.json.sha256
463 donnees/t06-jouet/taches-evaluation.json
89 donnees/t06-jouet/taches-evaluation.json.sha256
## plus gros fichier poussé (octets)
1996800
## marqueurs sur le disque de l'instance simulée
t06-arret-demande
t06-consigner.sh
t06-demarrages.txt
t06-depense-epuisee-utc.txt
t06-echeance.txt
t06-fin-normale
t06-minuterie.sh
stopped (fin du run)
## résumé scellé (diag) : clés présentes (les lignes restent dans le résultat scellé, jamais sur run.json)
['actions', 'actions_notees', 'adaptateurs', 'commit_cite', 'config_sha256', 'consignes_sha256', 'controles_negatifs', 'duree_s', 'episodes', 'ligne_A', 'ligne_B', 'ligne_C', 'mesures_sha256', 'morceaux', 'sous_ensemble_manifeste_sha256', 'taches_evaluation_sha256', 'textes_sha256']
## manifeste du sous-ensemble
{
 "actions": 10,
 "cles": [
  "S100__t002__p1",
  "S100__t003__p0",
  "S100__t003__p1",
  "T100__t000__p1",
  "honnete__t000__p0",
  "honnete__t001__p1",
  "mention__t000__p0",
  "mention__t000__p1",
  "saboteur__t003__p0",
  "temoin__t002__p1"
 ],
 "couche": 2,
 "morceau_max_octets": 90000000,
 "morceaux": [
  {
   "actions": 10,
   "fichier": "activations-sous-ensemble-t06-000.npz",
   "octets": 8746,
   "sha256": "ca9703256e1b907e5688827cd55f3e675fe2c590903804cd0c3703466e59233d"
  }
 ],
 "precision": "float16",
 "total_notees": 42
}
## tests joués par l'amorce
44 passed in 2.23s
## empreintes
95b2a69166bb40c53f51e2ddf54e3606bc38b9fcfda159a0db84674d9eb0d33a  amorce-sortie.txt
a3999f1e5183e5dde639cedcb609aa0b0751ef2fe7d0503286f0c069124e1109  instance/t06/journal.txt
d42f2983515af16b6d429be1bcc7cc371fd1542afd16394dd176bbaa61309a3b  instance/t06/run.json
6a4040e8d68c0df1575835ac67206bdbab23773587c38ec110d6a09230adf5b5  instance/t06/run.err
```
