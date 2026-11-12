# R-1692 — préparation locale de la v9 (fille 10), notes v1

Rien n'est poussé sur `prep/t06-lanceur-v2` ; tout est sur `prep/t06-lanceur-v9-prepa-locale`.

## 1. E2-2, stockage compté deux fois — corrigé (`session_v8.py`, `lancer_t06_v9.sh`)
`dph_total` inclut déjà `storage_total_cost` quand la recherche porte `--storage`. Valeurs réelles : dph_total 0,3617, stockage 0,041667, facturé 0,362.
v8 du lanceur (session_v7) : 0,3617 + 0,0417 = 0,4034 (+11,5 % sur la facture). v9 : prix_carte = dph_total − stockage = 0,320033 ; somme = 0,3617.
Le tri des offres se fait sur `dph_total` seul. Le plafond horaire reste vérifié sur `dph_total`. Offre dont dph_total ≤ stockage : refusée.
Essais (`tests/test_t06_v9_prix.py`, 8) : artefact v7 reproduit 0,4034 ; v8 somme = dph_total ; dépense d'une heure 0,3617 contre 0,362 facturé ; tri ; refus ; garde CUDA gardée ; sous-commande.
**Réserve à vérifier par toi** : la configuration d'E2 du dépôt borne `stockage_max_usd_h` à 0,03, or le stockage réel (150 Go) vaut 0,0417 : avec cette borne, `verifier_offre` refuse
toute offre. Le compte rendu d'E2 montre que la location a eu lieu : la configuration réellement utilisée avait donc une autre borne. À confirmer avant de sceller l'ordre.

## 2. Attente « trois commits »
Le lanceur et l'amorce n'ont rien à changer : la poussée initiale ne crée aucun commit (essai : branche d'un run complet = `init` + trois commits : résultats et données légères,
morceaux, traces ; test `test_fin_de_run_normale_ne_cree_aucun_commit_de_journal_en_plus`). Seul le texte de l'ordre d'E2 (E2-3 : « au moins quatre commits ») est à corriger si E2 est rejoué ;
l'ordre d'E3 v4 scellé n'a pas cette attente (ni l'ordre v5 que j'en tire).

## 3. E2-6 — journal sur la branche quand l'échéance tombe avant le run
Constat : `t06-consigner.sh` ne poussait que runs, diag et données légères ; le journal n'allait sur la branche qu'avec `traces()` (fin de run, `consigner_arret`). Une échéance pendant
l'installation ne laissait donc rien. Correctif étroit (amorce v7, 1 fonction, 1 variable) : la consignation lancée par la ligne de commande (minuterie : échéance, dépense épuisée ;
redémarrages) ajoute `traces/consignation-…/journal-consignation.txt` (motif, heure, dernière ligne du journal avant la consignation, 400 dernières lignes, empreinte) et un commit
« T0.6 : journal de l'instance (<motif>) ». Fin de run normale : aucun commit de plus. Conséquence à connaître : une échéance qui tombe pendant la poussée finale ajoute ce cinquième commit
(test `test_echeance_pendant_la_poussee_finale_v7_…`).
Essais (cas sain v7 / artefact v6 reproduit) dans `tests/test_t06_v7_amorce_minuterie.py` (10 au total).

### Rejouer E2-6 à bas prix
- **Sans dépense (proposé, à faire avant tout GO)** : essai local de l'amorce complète avec `ECHEANCE_UTC_S` = maintenant + quelques secondes, une étape d'installation factice qui dort, `curl` factice,
  remote local : on lit la ligne d'échéance, « consigné (échéance) : code 0 », le commit de journal sur le remote et le DELETE. Je peux l'écrire (script `essai_e26_t06_v9.sh`) dans le rendu v9.
- **Réel, si tu veux la preuve sur machine lente** : une instance de la carte la moins chère pendant ≈ 10 minutes, échéance posée 4 minutes après `DEMARRAGE` (pendant l'installation) ; coût ≈ 0,06 USD
  à 0,36 USD/h plus le téléchargement du forfait ; il faut un GO sur devis.
