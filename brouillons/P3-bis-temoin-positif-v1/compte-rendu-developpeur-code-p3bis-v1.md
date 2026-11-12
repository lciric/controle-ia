# Compte rendu du développeur du code de P3-bis (d'après les brouillons 6 à 9) — v1

- **Auteur** : sous-agent développeur de la session mère sortante `session_016QhUrrLeN21G7Z9KZobE42` ; rendu reçu le 9 novembre 2026 vers 18:36 UTC (`date -u` de la mère), après la passation `registres/passations/2026-11-09-1829.md` ; transcrit par la mère sans changement de fond. État du code : commit `e86a6f326` (R-2033).
- **Journaux cités par le développeur, perdus avec le conteneur sortant** (espace de travail de la mère, non versés) : `dev-p3bis/liste-ciblee.log`, `dev-p3bis/essai-complet.txt` (ce dernier porte sur des versions antérieures des modules : ne pas le citer).

## Verdict du développeur
Code écrit et éprouvé ; **le lanceur `docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v1.sh` (et sa constante `ARRETEES_TOLEREES`) n'est pas écrit**, faute de temps. Liste ciblée (`scripts/essais-cibles-p3bis-v1.txt`, 26 fichiers) : **435 passés, 1 échec** en 743,44 s, aucun essai sauté ; l'échec (`tests/test_premier_test_ia_run.py::test_mahalanobis_jamais_controle_arrete`, essai de P3) vient d'un `git commit` d'un dépôt jetable rendu en code 128 pendant que le disque était plein à 95 % ; **il passe rejoué seul**. Aucun fichier existant modifié (`git diff` vide) : P3 intact. Commande : `.venv/bin/python -I -B -m pytest -q -p no:cacheprovider --basetemp=<dossier neuf> -rs $(cat scripts/essais-cibles-p3bis-v1.txt)`. La mère a vérifié de son côté : les 78 essais neufs passent (279,6 s).

## Fichiers (tous neufs ; empreintes à leurs compagnons sur `main`)
`src/controle_ia/premier_test_ia/run_v2.py` (`83ebeac7…`), `lecture_p3bis_v1.py` (`bfe0effc…`), `ouverture_p3bis_v1.py` (`8972bfb1…`) ; `scripts/essai_fermeture_p3bis_v1.py` (`166e08e4…`), `scripts/essais-cibles-p3bis-v1.txt` (`dce03c1c…`), `scripts/p3bis_instance.sh` (`621b302b…`, porte en dur l'empreinte de la liste), `scripts/amorce_instance_p3bis.sh` (`0db6a0f2…`) ; essais : `test_premier_test_ia_run_v2.py` (6), `test_premier_test_ia_lecture_p3bis_v1.py` (14), `test_premier_test_ia_ouverture_p3bis_v1.py` (47), `test_essai_fermeture_p3bis_v1.py` (3), `test_script_p3bis_v1.py` (8). Garde de calcul `.claude/hooks/garde_calcul.py` inchangée (`184b3bbd…`). Code neuf compilé sous Python 3.11 (celui de l'instance).

## Valeurs proposées pour les marqueurs
- `EMPREINTES_CODE_P3BIS` : la liste ci-dessus.
- `TESTS_ATTENDUS_P3BIS` : **436, provisoire** (compté en local sous Python 3.13) ; à recompter au candidat dans un clone neuf du commit du code, environnement `requirements-gpu.txt`.
- `ESSAI_FERMETURE_P3BIS` : sortie à produire au commit du code par `PYTHONPATH=src python scripts/essai_fermeture_p3bis_v1.py DOSSIER_NEUF SORTIE.txt` (≈ 3 min ; dernière ligne attendue « ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME »). Un passage complet antérieur était conforme : sorties de classe 1 identiques entre issues substituées ; écart de longueur `zlib` d'au plus 7 octets ; cinq contrôles positifs détectés (variante endormie par la durée, 67,5 s contre 8,6 s ; variante au corps non comprimé par la longueur `zlib`, 9 961 octets d'écart).

## Écarts et choix déclarés (dans les docstrings)
1. Paquet des lectures : 16 783 360 octets (constante `TAILLE_PAQUET_LECTURES`) ; archive ustar à deux membres (`sel.txt`, 32 octets de `secrets` ; `corps.bin`, flux xz des sorties puis bourre), en-têtes fixes ; `SEUIL_ZLIB` = 64 octets (bruit mesuré ≤ 9 octets sur 60 paquets).
2. Variante « non bourrée » : `tar` arrondit à 10 240 octets, « vu » et « non vu » avaient la même taille ; détectée par un critère ajouté (taille différente de la taille fixe).
3. Sous-commandes : le texte en nomme deux (`fermer`, `ouvrir`) ; cinq ajoutées dans le même module : `fermer-run`, `exiger-aucun-clair`, `deplier-run`, `lectures-fermees`, `exposer-issue`.
4. Second paquet : `donnees/<run>/` entier, fichier complet des sondes compris (précédent R-679) ; non comprimé (xz ne gagne que 6 %) ; morceaux ≤ 90 000 000 octets ; index neuf `paquet-run-ferme-v1.json`, scellé ; le dépliage ne sort que les fichiers lus par les lectures.
5. `.git/info/exclude` écrit dans le clone fermé et le clone de l'instance (sinon la garde « arbre de travail non propre » du manifeste refuse les lectures).
6. `run_v2` : `_executer_apres_manifeste` appelée sans copie, durée `null` lue comme l'infini ; seule `executer` recopiée ; `ecart_a_p3()` la compare ligne à ligne à celle de P3 : trois lignes diffèrent, comme attendu.
7. Motif étendu recopié des lignes 44 à 46 de `test_croise.py` (le texte dit 43 à 45 ; la ligne 43 est un commentaire).
8. Garde d'ouverture : décision imposée `docs/decisions/rendez-vous-P3-bis-v<n>.md`, datée au plus tôt à `DATE_RENDEZ_VOUS` (2026-11-20T12:00:00Z ; si la date change, le module change) et au plus tard à la date de sa ligne ; branche 1 : `GARDE-ADAPTEE-T07-P3BIS` et `SCELLEMENT-T07` citent le même texte, datées au plus tard à la décision ; mode réduit refusé sur le chemin normal, mode plein refusé en branche 1 ; date de mise en paquet par `--date-paquet`, sinon par `git log` du paquet.
9. Réserves de PB-9 (processeur, OpenBLAS, empreintes de P3) : non calculées, listées dans `reserves_hors_module`.
10. « Aucun essai qui lit `donnees/` » lu comme visant les données non suivies ; les essais lisent les données génériques suivies `donnees/T0.7-*`.
11. Script de l'instance : code 5 si le second paquet échoue ; fils d'OpenBLAS relevés par `ctypes` ; bloc « plafond atteint » de l'amorce de P3 retiré (il poussait les fichiers du run en clair).

## Reste à faire
- Lanceur `lancer_p3bis_v1.sh` et toute la chaîne autour (vérifications communes, contrôles avant dépense, surveillance, récupération, bancs, répétitions) ; `ARRETEES_TOLEREES` proposée « 58936096 58936099 58936100 », à relire au candidat.
- Contre-lecture du code par un autre modèle (R2, N-052).
- Sortie de l'essai de fermeture au commit du code ; recompte de `TESTS_ATTENDUS_P3BIS`.
- N-066 touche le marqueur `<<T07_B15_GARDE_ADAPTEE>>`, pas le code.

## Défauts connus
Disque presque plein dans le conteneur sortant (2,2 Go libres) : un clone fermé avec le second paquet et le fichier complet des sondes (≈ 0,85 Go, deux à trois fois) sera serré ; l'ouverture tient les paquets en mémoire (≈ 2,5 Go au pic) ; l'essai de fermeture dure ≈ 3 min.
