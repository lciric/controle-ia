# Corrections de code proposées à `src/controle_ia/agregation_r1_v4/` (versions neuves, R12 : `analyse_v2.py`, `entrees_v2.py`) — v1

Contre-lecture neuve (R2) du préenregistrement « agrégateurs sur les scores réels de R1 v4 », fille 9, 6 novembre 2026. Ces corrections sont à faire avant la commande décisive. Chacune a un cas sain et un artefact (R5) ; la liste fermée et les empreintes du texte sont à regénérer ensuite.

- **Q1** — liste fermée vérifiée au lancement : le texte scellé passé à `--prereg` cite les empreintes du module et des dépendances (table du Plan, point 8) ; l'analyse les recalcule et refuse tout écart, comme `exiger_code_cite` de la principale.
- **Q2** — chemin du préenregistrement imposé : `prereg/agregation-r1-v4-v1.md` ; un autre chemin ou une copie sous un autre nom est refusé.
- **Q3** — empreintes d'entrée exigées :
  - `scores-p3.npz` doit valoir `968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf` (texte et fiche v4, l. 163) ;
  - les deux fichiers d'activations doivent valoir les empreintes que la fiche de réception v4 consigne. Ce sont des empreintes de fichiers, pas des résultats.
- **Q4** — garde de second passage : tout manifeste sous `runs/` qui cite le chemin ou l'empreinte du texte arrête (code de fin distinct, manifeste nommé), comme K2 de l'addendum des gardes.
- **Q5** — recette de W :
  - aligner sur la principale (`analyse_blanche_noire.modeles.ajuster_logistique`, λ = 1, gradient projeté 10⁻⁵, au plus 10 000 itérations, écart type sans correction avec plancher 10⁻⁸) ;
  - garder 10 plis de 6 tâches seulement si le texte dit pourquoi (sinon 5 plis de 12, comme la principale) ;
  - à défaut, garder la recette actuelle avec l'écart déclaré (couple 11).
- **Essais** : artefacts de la commande décisive — préenregistrement non scellé → refus avant tout chargement ; arbre sale → refus ; second passage → refus ; liste fermée altérée → refus ; empreinte de `scores-p3.npz` fausse → refus.
