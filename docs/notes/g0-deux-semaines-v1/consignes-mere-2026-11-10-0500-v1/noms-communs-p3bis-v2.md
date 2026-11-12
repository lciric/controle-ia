# Noms communs aux deux chantiers de P3-bis (corrections du code, lanceur) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 vers 05:25 UTC (`date -u`). Fixés par la mère pour que les deux branches se raccordent sans renommage. R12 : les fichiers v1 sont cités par empreinte (R-2033, compte rendu `977d84c1…`) ; toute correction passe par un nom neuf.

| rôle | v1 (commit `e86a6f32`, inchangé) | nom neuf (si le fichier change) |
|---|---|---|
| ouverture, fermeture, paquets, journal | `src/controle_ia/premier_test_ia/ouverture_p3bis_v1.py` | `src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py` |
| lecture | `src/controle_ia/premier_test_ia/lecture_p3bis_v1.py` | `src/controle_ia/premier_test_ia/lecture_p3bis_v2.py` (seulement si le code change ; des essais neufs seuls n'en font pas une v2) |
| course | `src/controle_ia/premier_test_ia/run_v2.py` | inchangé (CP-10 se règle à l'inventaire de l'essai) |
| essai différentiel de fermeture | `scripts/essai_fermeture_p3bis_v1.py` | `scripts/essai_fermeture_p3bis_v2.py` |
| script de l'instance | `scripts/p3bis_instance.sh` | `scripts/p3bis_instance_v2.sh` (il porte l'empreinte de la liste ciblée) |
| amorce de l'instance | `scripts/amorce_instance_p3bis.sh` | `scripts/amorce_instance_p3bis_v2.sh` (seulement si elle change) |
| liste ciblée | `scripts/essais-cibles-p3bis-v1.txt` | `scripts/essais-cibles-p3bis-v2.txt` |
| lanceur et sa chaîne | — | `docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v1.sh` et voisins (`verifications_p3bis_v1.py`, `controles_avant_depense_p3bis_v1.sh`, `surveiller_p3bis_v1.sh`, `recuperation_p3bis_v1.sh`, `sceller_p3bis_v1.sh`, `repetition_jouet_p3bis_v1.sh`, `repetition_finale_p3bis_v1.sh`, essais `essais_*_p3bis_v1.sh`), sur le modèle de `docs/procedures/P3-premier-test-v1/` |

**Interface de la ligne de commande après correction** (contre-lecture `7a074ad1…`, CP-08, CP-16, CP-17) : `ouverture_p3bis_v2 ouvrir` sans option `--instant` (le paramètre reste en Python pour les essais) ; `exposer-issue` exige `--lecture-p3bis` pour les lignes 2 à 5 et vérifie son sceau ; `lectures-fermees` exige `--prereg` et `--entropie` en mode décisif ; code de sortie 5 de `p3bis_instance_v2.sh` quand le second paquet échoue, y compris pendant un arrêt. Les autres sous-commandes gardent leur nom (`fermer`, `ouvrir`, `fermer-run`, `exiger-aucun-clair`, `deplier-run`, `lectures-fermees`, `exposer-issue`). Les modes d'ouverture deviennent `pleine`, `reduite`, `pleine-anticipee` (CP-01). Tout écart à ce tableau se déclare au rapport et se signale à la mère ; aucun des deux développeurs ne renomme un fichier de l'autre.
