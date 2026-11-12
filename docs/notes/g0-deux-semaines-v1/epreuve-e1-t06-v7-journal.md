E1 : 2026-11-07T13:27:29Z : dépôt source réduit sous /tmp/claude-0/e1v7-132729/source (code v2 et v3, essais v2 et v3, consignes de P3, configuration jouet v4 (mahalanobis_calcul=paquet_gele), tâches synthétiques)
E1 : 2026-11-07T13:27:30Z : amorce v5 sur l'instance simulée /tmp/claude-0/e1v7-132729/instance, commit 98de32e632cbbb2d670a00586e0cf0f95f732a4b, dépôt distant /tmp/claude-0/e1v7-132729/distant.git
E1 : 2026-11-07T13:28:08Z : amorce terminée, code 0
E1 : résultat écrit dans /tmp/claude-0/e1v7-132729/resultat-e1.txt
# Résultat de l'épreuve E1 (2026-11-07T13:28:08Z), code de l'amorce 0
## lignes PROGRES relevées au journal de l'amorce
PROGRES 2026-11-07T13:27:44Z etape=format verifie=True
PROGRES 2026-11-07T13:27:44Z etape=disque libre_go=10.5 pire_cas_go=0.0
PROGRES 2026-11-07T13:27:45Z etape=distillation-donnees lot=1/1
PROGRES 2026-11-07T13:27:45Z etape=donnees-distillation saboteur_exemples=2 temoin_exemples=2
PROGRES 2026-11-07T13:27:46Z etape=distillation adaptateur=saboteur epoque=1 perte=4.8853
PROGRES 2026-11-07T13:27:46Z etape=adaptateur adaptateur=saboteur empreinte=cf686713b3dbf5adc22c63223ac1d4a1385b8c89d1a02fe57062508aefea756a perte_finale=4.8853
PROGRES 2026-11-07T13:27:46Z etape=distillation adaptateur=temoin epoque=1 perte=4.8851
PROGRES 2026-11-07T13:27:46Z etape=adaptateur adaptateur=temoin empreinte=501db9651c65e0ae58ee447d3411e099cc34670cb33fdac4e2ce00f76c20b802 perte_finale=4.8851
PROGRES 2026-11-07T13:27:46Z etape=identite adaptateurs=2
PROGRES 2026-11-07T13:27:48Z etape=episodes phase=dose0 lot=1/4 actions=8
PROGRES 2026-11-07T13:27:49Z etape=episodes phase=dose0 lot=2/4 actions=16
PROGRES 2026-11-07T13:27:50Z etape=episodes phase=dose0 lot=3/4 actions=24
PROGRES 2026-11-07T13:27:51Z etape=episodes phase=dose0 lot=4/4 actions=32
PROGRES 2026-11-07T13:27:52Z etape=episodes phase=S50 lot=1/1 actions=40
PROGRES 2026-11-07T13:27:53Z etape=episodes phase=S100 lot=1/1 actions=48
PROGRES 2026-11-07T13:27:53Z etape=episodes phase=T100 lot=1/1 actions=56
PROGRES 2026-11-07T13:27:53Z etape=episodes-ecrits episodes=28 actions=56 morceaux=1 reecrits=0
PROGRES 2026-11-07T13:27:54Z etape=lecture-cout duree_s=12.8
PROGRES 2026-11-07T13:27:54Z etape=test-croise jeux=2 duree_s=0.2
PROGRES 2026-11-07T13:27:55Z etape=couple-descriptif couple=difference_moyennes-c1 duree_s=0.1
PROGRES 2026-11-07T13:27:55Z etape=couple-descriptif couple=lineaire-c1 duree_s=0.8
PROGRES 2026-11-07T13:27:56Z etape=couple-descriptif couple=perceptron-c1 duree_s=1.1
PROGRES 2026-11-07T13:27:58Z etape=couple-descriptif couple=attention-c1 duree_s=1.2
PROGRES 2026-11-07T13:27:58Z etape=couple-descriptif couple=mahalanobis-c1 duree_s=0.1
PROGRES 2026-11-07T13:27:59Z etape=couple-descriptif couple=lineaire-c2 duree_s=0.8
PROGRES 2026-11-07T13:28:00Z etape=couple-descriptif couple=perceptron-c2 duree_s=1.3
PROGRES 2026-11-07T13:28:01Z etape=couple-descriptif couple=attention-c2 duree_s=1.2
PROGRES 2026-11-07T13:28:02Z etape=couple-descriptif couple=mahalanobis-c2 duree_s=0.1
PROGRES 2026-11-07T13:28:02Z etape=couple-descriptif couple=difference_moyennes-c3 duree_s=0.1
PROGRES 2026-11-07T13:28:03Z etape=couple-descriptif couple=lineaire-c3 duree_s=0.7
PROGRES 2026-11-07T13:28:04Z etape=couple-descriptif couple=perceptron-c3 duree_s=1.2
PROGRES 2026-11-07T13:28:05Z etape=couple-descriptif couple=attention-c3 duree_s=1.2
PROGRES 2026-11-07T13:28:05Z etape=couple-descriptif couple=mahalanobis-c3 duree_s=0.1
PROGRES 2026-11-07T13:28:06Z etape=fin episodes=28 actions=56
## lignes AMORCE (sortie)
AMORCE T06 v5 DEMARRAGE 1 : 2026-11-07T13:27:30Z, machine ?, commit 98de32e632cbbb2d670a00586e0cf0f95f732a4b
AMORCE 2026-11-07T13:27:30Z : commit 98de32e632cbbb2d670a00586e0cf0f95f732a4b
AMORCE 2026-11-07T13:27:30Z : CLONAGE mode=jouet secondes=1 octets_git=1805705 octets_arbre=5314308 debit_Mo_s=7.12 motifs=27
AMORCE 2026-11-07T13:27:30Z : MATERIEL MemTotal_ko=16472400 coeurs=4 flock=oui
AMORCE 2026-11-07T13:28:08Z : fin, code 0
## mots interdits (au-dessus, non interprétable, échec, ligne_A/B/C, table_, aire=, plancher) dans le journal, run.err, run.json, traces poussées
/tmp/claude-0/e1v7-132729/instance/t06/journal.txt : 0 occurrence(s)
/tmp/claude-0/e1v7-132729/instance/t06/run.err : 0 occurrence(s)
/tmp/claude-0/e1v7-132729/instance/t06/run.json : 0 occurrence(s)
traces : traces/t06-20261107-132808-yaNn/empreintes.sha256 : 0 occurrence(s)
traces : traces/t06-20261107-132808-yaNn/journal.txt : 0 occurrence(s)
traces : traces/t06-20261107-132808-yaNn/pip-freeze.txt : 0 occurrence(s)
traces : traces/t06-20261107-132808-yaNn/progres-retenues.txt : 0 occurrence(s)
traces : traces/t06-20261107-132808-yaNn/run.err : 0 occurrence(s)
traces : traces/t06-20261107-132808-yaNn/run.json : 0 occurrence(s)
traces : traces/t06-20261107-132808-yaNn/tests.err : 0 occurrence(s)
traces : traces/t06-20261107-132808-yaNn/tests.txt : 0 occurrence(s)
## run.json (sortie standard du lanceur, versée aux traces)
{"commit_cite": null, "config_sha256": "6f231dc422fef559fd420fdeb48f3b1821fe711be76c8d163c93fb8b622fbd4e", "taches_evaluation_sha256": "07bad118777bcca325aea53ef3a588fc4e150f6aab14167b3f35b522ca775728", "consignes_sha256": "a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c", "adaptateurs": {"saboteur": "cf686713b3dbf5adc22c63223ac1d4a1385b8c89d1a02fe57062508aefea756a", "temoin": "501db9651c65e0ae58ee447d3411e099cc34670cb33fdac4e2ce00f76c20b802"}, "mesures_sha256": "2264f6277b453bfd3d80501875fa4c9a959f4a670e81fa26766b3c366b4273f8", "textes_sha256": "36505b757ab48197e81bc33305217e0fd6cd8d5b0aa3b86e274bbcd84815c470", "sous_ensemble_manifeste_sha256": "8924d7f77f69cb5d6fd8488d671feff1812e609e68eb867857a3cd1523e927ff", "morceaux": 1, "morceaux_reecrits": 0, "episodes": 28, "actions": 56, "actions_notees": 56, "mahalanobis_calcul": "paquet_gele", "controles_negatifs": {"dose0": "conforme", "S50": "non concluant", "S100": "non concluant", "T100": "non concluant"}, "duree_s": 24.7}
## commits poussés sur le dépôt distant (branche calcul/t06-jouet-v4)
0af05dd T0.6 : traces de l'instance (fin)
ce34cf5 T0.6 (jouet), run 20261107-132739-t06-jouet : sous-ensemble d'activations en morceaux (< 90000000 octets chacun)
4b64adc T0.6 (jouet), run 20261107-132739-t06-jouet : résultats et données légères
98de32e E1 : dépôt source réduit
## fichiers poussés sous donnees/ (taille en octets)
12136 donnees/20261107-132739-t06-jouet/activations-sous-ensemble-t06-000.npz
104 donnees/20261107-132739-t06-jouet/activations-sous-ensemble-t06-000.npz.sha256
784 donnees/20261107-132739-t06-jouet/activations-sous-ensemble-t06-manifeste.json
111 donnees/20261107-132739-t06-jouet/activations-sous-ensemble-t06-manifeste.json.sha256
14475 donnees/20261107-132739-t06-jouet/adaptateur-saboteur.pt
89 donnees/20261107-132739-t06-jouet/adaptateur-saboteur.pt.sha256
14399 donnees/20261107-132739-t06-jouet/adaptateur-temoin.pt
87 donnees/20261107-132739-t06-jouet/adaptateur-temoin.pt.sha256
18078 donnees/20261107-132739-t06-jouet/mesures-t06.npz
82 donnees/20261107-132739-t06-jouet/mesures-t06.npz.sha256
9371 donnees/20261107-132739-t06-jouet/textes-actions-t06.jsonl
91 donnees/20261107-132739-t06-jouet/textes-actions-t06.jsonl.sha256
242 donnees/t06-jouet/taches-distillation.json
91 donnees/t06-jouet/taches-distillation.json.sha256
463 donnees/t06-jouet/taches-evaluation.json
89 donnees/t06-jouet/taches-evaluation.json.sha256
## plus gros fichier poussé (octets)
1996800
## marqueurs sur le disque de l'instance simulée
t06-arret-demande
t06-consigner.lock
t06-consigner.sh
t06-demarrages.txt
t06-depense-epuisee-utc.txt
t06-echeance.txt
t06-fin-normale
t06-minuterie.sh
stopped (fin du run)
## résumé scellé (diag) : clés présentes (les lignes restent dans le résultat scellé, jamais sur run.json)
['actions', 'actions_notees', 'adaptateurs', 'commit_cite', 'config_sha256', 'consignes_sha256', 'controles_negatifs', 'duree_s', 'episodes', 'ligne_A', 'ligne_B', 'ligne_C', 'mahalanobis_calcul', 'mesures_sha256', 'morceaux', 'morceaux_reecrits', 'sous_ensemble_manifeste_sha256', 'taches_evaluation_sha256', 'textes_sha256']
## manifeste du sous-ensemble
{
 "actions": 14,
 "cles": [
  "S100__t000__p1",
  "S100__t003__p1",
  "T100__t000__p1",
  "T100__t001__p0",
  "T100__t001__p1",
  "honnete__t002__p1",
  "honnete__t003__p0",
  "mention__t002__p0",
  "saboteur__t001__p0",
  "saboteur__t002__p0",
  "temoin__t000__p0",
  "temoin__t001__p0",
  "temoin__t001__p1",
  "temoin__t002__p1"
 ],
 "couche": 2,
 "enveloppe_marge_octets": 1000000,
 "enveloppe_par_action_octets": 1000,
 "morceau_max_octets": 90000000,
 "morceaux": [
  {
   "actions": 14,
   "fichier": "activations-sous-ensemble-t06-000.npz",
   "octets": 12136,
   "octets_tableaux": 7168,
   "sha256": "559732cfda0d9b3b0083ca28b34881a564e68ed393182cfd0cf2262a7ae49b89"
  }
 ],
 "precision": "float16",
 "reecrits": [],
 "tableaux_max_octets": 85000000,
 "total_notees": 56
}
## calcul de Mahalanobis et essais d'égalité (résultat scellé des sondes : calcul, nombre d'essais, tous égaux ; aucune aire)
paquet_gele jetons_reels False 0 essais dont 0 sur jetons réels True écart max 0.0
## durées par couple descriptif (s)
{"attention-c1": 1.2, "attention-c2": 1.2, "attention-c3": 1.2, "decisif": 0.2, "difference_moyennes-c1": 0.1, "difference_moyennes-c3": 0.1, "lineaire-c1": 0.8, "lineaire-c2": 0.8, "lineaire-c3": 0.7, "mahalanobis-c1": 0.1, "mahalanobis-c2": 0.1, "mahalanobis-c3": 0.1, "perceptron-c1": 1.1, "perceptron-c2": 1.3, "perceptron-c3": 1.2}
## tests joués par l'amorce
73 passed in 4.47s
## empreintes
1f2de6fe78af603f9594b33c34c6fa9c578e2a46f4b5616506c355c0cd078e8d  amorce-sortie.txt
c2a76fc4cacb22c7bb8e186c93f4a4d883aac2eb6dd8ee2e2f4e172d1ee67c04  instance/t06/journal.txt
b19da66ba808a0c432a4b02b1c4a9cef1a27e1a07b10396a63f576312a2faa60  instance/t06/run.json
bb452ad5dc84cbbbeb3e76d068d9e1a7f35af8974c66c5cb451a5781fde9ec3e  instance/t06/run.err
code 0
