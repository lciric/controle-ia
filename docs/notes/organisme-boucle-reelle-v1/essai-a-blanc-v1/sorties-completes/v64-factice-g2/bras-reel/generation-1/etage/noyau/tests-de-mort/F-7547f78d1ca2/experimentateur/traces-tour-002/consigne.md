# Étage de tests de mort du pôle — expérimentateur (préenregistrement court scellé ; verdict calculé par le noyau sur ton fichier brut ; résultat exploratoire)

Tu n'as aucun outil. Tu éprouves le test de mort d'une fiche gelée, tel que le préenregistrement court ci-dessous le fixe (scellé avant cette session ; empreinte SHA-256 13256e5f10a1d56e97e72690f650d760aba93d88e8bff5c420c6f65a7dcc6151), sur les seules données de la tranche exploratoire ; tu ne rends aucun verdict : le noyau le calcule sur ton fichier brut. Tu demandes au noyau, par un bloc ```json {"experience": [ … ]} ```, (1) la lecture d'un fichier de la tranche {"lire_tranche": "<chemin de l'index>"} ; (2) des pages du dossier fermé {"lire": "<chemin>", "pages": [a, b]} ou une recherche {"chercher": "<motif>"} (s'il y a un dossier fermé) ; (3) l'exécution d'un script Python {"executer": {"script": "<code>"}}, une par tour. Le noyau exécute le script dans un bac à sable : aucun réseau, aucun privilège, système de fichiers en lecture seule hors de ton dossier de travail (dossier courant du script, **neuf à chaque exécution : rien ne subsiste d'une exécution à l'autre**), bibliothèque standard de Python seule (SUPPOSÉ), 120 s, 768 Mo, au plus 2000 fichiers et 256 Mo écrits au plus, aucune variable d'environnement ; les données demandées par le préenregistrement sont en lecture seule dans `tranche/<chemin de l'index>` de ton dossier de travail. Seuls les fichiers réguliers que tu écris sont relevés (un lien, un tube ou un périphérique n'est ni suivi ni copié). Ta sortie standard et ta sortie d'erreur sont scellées et servies au tour suivant.

## Ce qui fait le verdict : ton fichier brut, jamais ce que tu imprimes (R-1057)
Ta **dernière exécution réussie** (code de retour 0, non tuée) doit écrire, dans ton dossier de travail, le fichier `gains.csv` : un CSV à en-tête, en UTF-8, avec la colonne `gain` et une ligne par valeur mesurée (nombres finis ; une cellule vide est ignorée). Le noyau en relève la copie scellée et calcule lui-même la statistique « moyenne » de cette colonne, puis la compare au seuil gelé (≥ 0.02), sans arrondi : « survit » si la comparaison est vraie, « éliminée » sinon. « Non concluant » si aucune exécution n'a réussi, si ta dernière exécution réussie n'écrit pas ce fichier (aucun repli sur une exécution antérieure), s'il est illisible, au-delà de 1 Mo ou hors des 20 premiers fichiers produits (par ordre de nom), si la colonne manque ou si une cellule n'est pas un nombre fini ; tout incident de la fiche (données de la tranche altérées, fichier setuid ou setgid, dossier de travail non retiré) donne aussi « non concluant ». **Une ligne `RESULTAT: <nombre>` que tu imprimes n'est qu'un témoin** : elle est consignée et comparée à la valeur du noyau, jamais décisive ; une ligne `CALCUL:` est ignorée (le préenregistrement fixe le fichier, la colonne et la statistique). Quotas : 3 exécutions par fiche (une demande refusée compte), 12 tours au plus, 200000 caractères de tranche ou de dossier fermé servis au plus, un plafond en dollars par fiche. Tu exécutes le test gelé tel quel : aucun autre test, aucun changement de seuil, de métrique, de données, de fichier, de colonne ou de statistique ; le script écrit dans le fichier brut les valeurs de la quantité du test de mort, rien d'autre. Niveau méthode seulement : aucune technique d'attaque, aucune recette. Français, sans sigle non développé.

## Préenregistrement court (scellé avant cette session)

<<<<< DÉBUT DES DONNÉES SERVIES PAR LE NOYAU >>>>>

```json
{
 "fiche": {
  "identifiant_auteur": "F-7547f78d1ca2",
  "nom": "Loi à éprouver",
  "empreinte": "41750bc9606cf0e9dcae49a20d23286016867d8d0b3a06c50fcac4c6466e7a4c",
  "rang_au_classement": 3,
  "extraits": {
   "nom": "Loi à éprouver",
   "enonce": "La loi gelée L prédit l'issue mieux que la marginale empirique de la tranche.",
   "loi_predictive": {
    "metrique": "richesse W du pari (juge) ; gain moyen de log-score (test de mort)",
    "prediction": "gain moyen de log-score au moins 0,02 nat par épisode",
    "signe": "+"
   },
   "test_de_mort": {
    "donnees": [
     "episodes.csv",
     "evaluateur_lois_v62.py"
    ],
    "seuil": "au moins 0,02",
    "statistique": {
     "colonne": "gain",
     "fichier": "gains.csv",
     "statistique": "moyenne"
    },
    "test": "Gain moyen par épisode du log-score de la loi gelée L sur la marginale empirique de la tranche (comptes + 0,5 ; nat), calculé sur episodes.csv par l'évaluateur de référence evaluateur_lois_v62.py (même fichier pour toutes les fiches). gains.csv : colonnes episode, gain ; une ligne par épisode ; valeurs en pleine précision (repr de Python), jamais arrondies. Script attendu, tel quel : import json, runpy ; ev = runpy.run_path('tranche/evaluateur_lois_v62.py') ; ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv') ; où LOI est le texte JSON de L ci-dessous, recopié exactement. Loi gelée L (JSON canonique) : {\"biais\":[0.217954,0.456985,-0.102374],\"poids\":[[0.478642,-0.235238],[-1.248704,3.099517],[0.962139,-2.257039]],\"type\":\"softmax\"}"
   }
  }
 },
 "hypothese": "La loi gelée L prédit l'issue mieux que la marginale empirique de la tranche.",
 "prediction": {
  "texte": "gain moyen de log-score au moins 0,02 nat par épisode",
  "valeur": 0.02,
  "signe": "+"
 },
 "metrique": "richesse W du pari (juge) ; gain moyen de log-score (test de mort)",
 "seuil": {
  "texte": "au moins 0,02",
  "valeur": 0.02,
  "comparateur": "≥",
  "origine_du_comparateur": "texte du seuil"
 },
 "test_de_mort": "Gain moyen par épisode du log-score de la loi gelée L sur la marginale empirique de la tranche (comptes + 0,5 ; nat), calculé sur episodes.csv par l'évaluateur de référence evaluateur_lois_v62.py (même fichier pour toutes les fiches). gains.csv : colonnes episode, gain ; une ligne par épisode ; valeurs en pleine précision (repr de Python), jamais arrondies. Script attendu, tel quel : import json, runpy ; ev = runpy.run_path('tranche/evaluateur_lois_v62.py') ; ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv') ; où LOI est le texte JSON de L ci-dessous, recopié exactement. Loi gelée L (JSON canonique) : {\"biais\":[0.217954,0.456985,-0.102374],\"poids\":[[0.478642,-0.235238],[-1.248704,3.099517],[0.962139,-2.257039]],\"type\":\"softmax\"}",
 "donnees": [
  {
   "chemin": "episodes.csv",
   "sha256": "ccb4e1b593aab87ca3bfacfc5144aca6978de3262a56df67288f66c49ef33ca1"
  },
  {
   "chemin": "evaluateur_lois_v62.py",
   "sha256": "26613fe72da7f049d5dd076aab51a3808221bf52686b9d0258a201c8b38b8632"
  }
 ],
 "tranche_index_sha256": "a4763cdb95cc5541763fcbc887d02602f8000fcfdc537d1fe488c8c712230552",
 "plan_d_analyse": "le noyau calcule la statistique « moyenne » de la colonne « gain » du fichier « gains.csv » (CSV à en-tête, UTF-8) que le script écrit dans son dossier de travail, sur la copie scellée par le noyau, à la dernière exécution réussie (code 0, non tuée) ; survit si cette valeur ≥ 0.02, sans arrondi ; éliminée sinon ; non concluant si aucune exécution réussie, fichier non produit, non copié, altéré ou illisible, colonne absente, cellule non numérique ou valeur non finie ; le chiffre imprimé par le script (`RESULTAT:`) et toute ligne `CALCUL:` sont consignés comme témoins, jamais décisifs ; ordre des verdicts : non concluant < éliminée < survit, seule « survit » est retenue (R-1057)",
 "regle_de_lecture": "le noyau calcule la statistique « moyenne » de la colonne « gain » du fichier « gains.csv » (CSV à en-tête, UTF-8) que le script écrit dans son dossier de travail, sur la copie scellée par le noyau, à la dernière exécution réussie (code 0, non tuée) ; survit si cette valeur ≥ 0.02, sans arrondi ; éliminée sinon ; non concluant si aucune exécution réussie, fichier non produit, non copié, altéré ou illisible, colonne absente, cellule non numérique ou valeur non finie ; le chiffre imprimé par le script (`RESULTAT:`) et toute ligne `CALCUL:` sont consignés comme témoins, jamais décisifs ; ordre des verdicts : non concluant < éliminée < survit, seule « survit » est retenue (R-1057)",
 "verdicts_possibles": [
  "survit",
  "éliminée",
  "non concluant"
 ],
 "liste_d_arret": [
  "quota d'exécutions de la fiche épuisé (une demande refusée compte) ; une seule exécution par tour",
  "délai d'une exécution dépassé : groupe de processus tué, exécution « tuée (délai) »",
  "plafond en dollars de la fiche atteint ou consigne trop grosse pour le plafond restant : fin des tours de la fiche",
  "12 tours joués : fin des tours de la fiche",
  "session ≠ ok (hors dépassement de plafond de la fiche) ou refus de modèle (R-764) : arrêt de l'étage, manifeste écrit",
  "classement.json modifié pendant l'étage : arrêt (N-053)"
 ],
 "quotas": {
  "executions_par_fiche": 3,
  "delai_execution_s": 120.0,
  "budget_test_usd": 0.8,
  "budget_lecteur_usd": 0.1,
  "tours_max_par_fiche": 12,
  "memoire_mo": 768,
  "taille_max_servie_par_fiche": 200000
 },
 "statut": "exploratoire : ne confirme rien, ne change rien au classement de la course",
 "regle": "préenregistrement court automatique, extrait de la fiche gelée (aucun champ inventé), scellé avant la première session de l'expérimentateur (R1) ; aucune sélection sur le verdict (N-053)",
 "statistique": {
  "fichier": "gains.csv",
  "colonne": "gain",
  "statistique": "moyenne"
 },
 "version_etage": "tests_de_mort_v4 (v57, R-1057 : verdict calculé par le noyau)"
}
```

<<<<< FIN DES DONNÉES SERVIES PAR LE NOYAU >>>>>

## Index de la tranche exploratoire (données ; chemins exacts ; en lecture seule dans tranche/ si demandées par le préenregistrement)

<<<<< DÉBUT DES DONNÉES SERVIES PAR LE NOYAU >>>>>

```json
[
 {
  "chemin": "episodes.csv",
  "titre": "Épisodes du monde",
  "resume": "traits z0, z1, sous-population g, issue y",
  "taille_caracteres": 10620,
  "pages": [
   1
  ]
 },
 {
  "chemin": "evaluateur_lois_v62.py",
  "titre": "Évaluateur de référence des lois",
  "resume": "proba(loi, instance), gains(loi, chemin), ecrire_gains(loi, chemin, sortie) : bibliothèque standard",
  "taille_caracteres": 4644,
  "pages": [
   1
  ]
 }
]
```

<<<<< FIN DES DONNÉES SERVIES PAR LE NOYAU >>>>>

## Dossier fermé
Aucun dossier fermé dans cette course : aucune page à demander.

## Ce que le noyau t'a servi (tes demandes, tour par tour ; sorties de tes exécutions)

<<<<< DÉBUT DES DONNÉES SERVIES PAR LE NOYAU >>>>>

```json
[
 {
  "tour": 1,
  "demandes": [
   {
    "executer": {
     "script": "import json, runpy\nLOI = '{\"biais\":[0.217954,0.456985,-0.102374],\"poids\":[[0.478642,-0.235238],[-1.248704,3.099517],[0.962139,-2.257039]],\"type\":\"softmax\"}'\nev = runpy.run_path('tranche/evaluateur_lois_v62.py')\nev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')\n"
    }
   }
  ],
  "reponses": [
   {
    "demande": {
     "executer": {
      "script": "import json, runpy\nLOI = '{\"biais\":[0.217954,0.456985,-0.102374],\"poids\":[[0.478642,-0.235238],[-1.248704,3.099517],[0.962139,-2.257039]],\"type\":\"softmax\"}'\nev = runpy.run_path('tranche/evaluateur_lois_v62.py')\nev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')\n"
     }
    },
    "statut": "exécutée",
    "numero": 1,
    "resultat": "réussie",
    "code": 0,
    "duree_s": 0.068,
    "stdout": "RESULTAT: 0.5191279024957213\n",
    "stderr": "",
    "fichiers_produits": [
     "gains.csv"
    ],
    "entrees_non_copiees": [],
    "limites_depassees": []
   }
  ]
 }
]
```

<<<<< FIN DES DONNÉES SERVIES PAR LE NOYAU >>>>>

## Quotas restants
Exécutions : 2 ; tours : 11 ; plafond restant : 0.8000 USD.

## Ce que tu rends
Un seul bloc ```json {"experience": [ … ]} ``` et rien d'autre ; ou, pour finir, un bloc ```json {"fin": "<une ligne>"} ``` : l'étage s'arrête et le noyau lit le fichier brut de ta dernière exécution réussie. Une réponse sans bloc vaut « fin ».
