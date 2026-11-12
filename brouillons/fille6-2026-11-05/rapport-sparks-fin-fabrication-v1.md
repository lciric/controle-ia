# Fille 6 — SPARKS-EXP7-NUL : fin de la fabrication (code 2), nœud — v1

Le 5 novembre 2026 (heures relevées par `date -u`). Instance 59288960, LANCE `0d163bdc…`, CODE `78671d93…`, GO-2026-11-04-04.

- **Lignes « AMORCE »**, seule lecture permise :
  - « AMORCE V10 DEMARRAGE 1 : 2026-11-05T16:11:46Z » ;
  - « fabrication, durée plafonnée à 1440 minutes » ;
  - « 16:31:31Z : fin de la fabrication, code 2 » ;
  - « 16:31:32Z : fin de la fabrication, code 2 : ARRÊT OBTENU (état voulu « stopped », HTTP 200) : le conteneur sort » ;
  - REDEMARRAGES=0, BOUCLE_PRESUMEE=0, DEMARRAGES=1, BOUCLE=non ; ARRET_OBTENU=1793896292.
- **Après l'arrêt** :
  - inventaires « exited » / `cur_state` « stopped » à 16:50:26, 16:53:07 et 16:55:49 ;
  - `boucle` : « lectures comptées : après la ligne « ARRÊT OBTENU », verdict arretee ».
- **Versement** : la branche `calcul/sparks-exp7-nul-v5-0d163bdcea56` a sa tête égale à LANCE. Aucune sortie poussée ; aucun `journal.txt` ; rien n'est lu.
- **Dépense** : 0,47 h de carte à 0,2014 USD/h, plus le stockage à 0,0329 USD/h depuis 16:03:20Z. `depense projeter` : cumulée 0,12 USD, projection 16,96 USD ≤ 40.
- **Conduite** (ordre v1, C.6, code de fin non nul) : **nœud**. L'instance reste arrêtée et non détruite ; aucun redémarrage ; message à la mère à 16:56. Aucune copie (section D).
- **A1-v3, instance 59286520** : contrôles de 16:20:13Z et 16:50:16Z ; running, signe de vie oui, code 5.
