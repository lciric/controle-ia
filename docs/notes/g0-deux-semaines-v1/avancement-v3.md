# Avancement du lanceur de T0.6 v3 (fichier de reprise ; branche `prep/t06-lanceur-v2` par-dessus `0d48103b`)

Règle : chaque ligne passe à « fait » quand le fichier est sur le disque et committé ; un redémarrage reprend à la première
ligne « à faire ». Noms neufs (R12) : aucun fichier v1, v2 ni gelé n'est modifié. Corrections de la contre-lecture neuve
(`corrections-code-lanceur-T0.6-v3.md`, `9a89626bce120959…`) : C-V3-1 à C-V3-4.

| point | état | fichier(s) |
|---|---|---|
| C-V3-1 morceaux remplis à une borne de tableaux plus petite, fichier > 90 Mo réécrit en deux, jamais un arrêt | fait (J1, J2) | `t06/lanceur_v3.py` ; essais `tests/test_t06_v3_lanceur_jouet.py` |
| C-V3-2 second démarrage avant les contrôles d'heure : consigner, puis détruire (argent épuisé) ou dormir (fin normale) | fait (J1, J2) | `scripts/amorce_instance_t06_v3.sh` ; essais `tests/test_t06_v3_scripts.py` |
| C-V3-3 offre relue avec `--storage <disque_min_go>` | fait (J1, J2) | `scripts/lancer_t06_v3.sh` ; essai sur un faux `vastai` |
| C-V3-4 Mahalanobis par produit matriciel, égalité au paquet gelé avant chaque usage, clé de configuration (défaut : paquet gelé) | fait (J1, J2) | `sondes/familles_v2.py`, `t06/configuration_v3.py`, `t06/lanceur_v3.py` ; configurations v4 et brouillon 3 |
| essais v3 | fait (J2 : 42 essais v3 verts, « 37 » dans le message du commit J2 était un compte de tête faux ; suites v1 (76) et v2 (67) rejouées vertes) | `tests/test_t06_v3_configuration.py`, `_familles.py`, `_lanceur_jouet.py`, `_scripts.py` |
| banc v3 | fait (J3 : 55 mutations, 55 tuées, 6 témoins verts) | `scripts/banc_mutations_t06_v3.py`, `banc-mutations-t06-v3.log`, `.json` |
| E1 v3 | fait (J4 : code 0, 55 tests, 0 mot interdit ; rejoué aussi sous la v2 de Mahalanobis) | `scripts/epreuve_e1_t06_v3.sh`, `epreuve-e1-t06-v3-journal.md` |
| mesure de durée de Mahalanobis v2 (jouet, E0 au 1/64 et 1/256) | fait (J4) | `scripts/epreuve_e0_t06_v3.py`, rapport |
| rapport v3 | fait (J5) | `rapport-developpeur-lanceur-T0.6-v3.md` |
