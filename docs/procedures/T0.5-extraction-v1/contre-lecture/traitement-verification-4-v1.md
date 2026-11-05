# Traitement de la vérification 4 (corrections de la contre-lecture 3) de la procédure d'extraction de T0.5

Rapport : `rapport-verification-4-v1.md` (même dossier) ; fichiers de travail du vérificateur : `fichiers-de-travail-verification-4-v1.tar` (essais, sorties, différentiels de sa copie corrigée ; les dépôts jetables ne sont pas archivés). Verdict : « scellable après corrections, courtes, sans refonte » (0 bloquante, 0 majeure, 6 mineures, 7 suggestions). Toutes les remarques sont acceptées. Code : `extraction.py`, `extraire_t05.py` ; tests : `tests/test_extraire_t05.py`, `tests/test_extraction.py` (139 tests ; les 70 gardes des deux modules exercées, relevé par traçage des lignes exécutées).

| remarque | gravité | traitement |
|---|---|---|
| V-1 | mineure | Acceptée, correctif du vérificateur repris : les noms des entrées modifiées sont écrits échappés (`os.fsencode`, puis décodage UTF-8 avec `backslashreplace`). Test (nom non UTF-8 sous `papier/`). |
| V-2 | mineure | Acceptée : tout chemin ajouté parmi les entrées est compté (dossier, lien cassé, tube nommé), pas seulement les fichiers. Tests (quatre objets). |
| V-3 | mineure | Acceptée : message `avis.cible` échappé (`!r`). Test (cible textuelle porteuse d'un substitut isolé : avis illisible, ronde lue). |
| V-4 | mineure | Acceptée : la racine du dépôt est consignée au manifeste à l'ouverture du run ; une étape lancée d'une autre copie (arbre de travail git, clone) est refusée sans rien contrôler ni écrire. Test (arbre de travail refusé ; même racine écrite autrement acceptée). |
| V-5 | mineure | Acceptée, au texte : un ou plusieurs dossiers de papier disparus, le dossier de la tentative ou de la ronde restant, sont des entrées modifiées de leurs papiers. |
| V-6 | mineure | Acceptée, au texte : les fichiers de retours ne sont pas scellés ; leur contenu est repris dans les détails scellés et dans `diag/` ; depuis N-014 (a), ils sont committés avec les autres fichiers de `donnees/<run>/`. |
| V-7 | suggestion | Acceptée : une empreinte compagnon illisible est une perte (`ValueError` comprise). Test. |
| V-8 | suggestion | Acceptée : un arrêt « avis refaits » par rôle et par papier (`arret-avis-refaits-<rôle>-<papier>`). Test adapté. |
| V-9 | suggestion | Acceptée, au texte : même permutation, aucune réélection de l'échantillon ; un run nouveau refait toutes les sorties. |
| V-10 | suggestion | Acceptée : commande `controler` (règle de perte rejouée, sans rien écrire si rien n'est perdu), lancée avant chaque commit de `donnees/<run>/` (section 8). Test. |
| V-11 | suggestion | Acceptée : encodage UTF-8 écrit dans la recette de l'essai à blanc ; empreinte inchangée (2e1b9417…). |
| V-12 | suggestion | Acceptée, au texte : « il changerait le texte que lit le script » ne vaut que sous `papier/`. |
| V-13 | suggestion | Acceptée en partie : le seuil d'exclusions D-17 se relit depuis la validation 2 avant tout tirage (test) ; une préparation interrompue des tentatives 2 et 3 met de côté son dossier, sans le détruire, et se refait (test). Résidus déclarés au texte (section 7) : résultat de `diag/` interrompu avant son sceau, préparation de la tentative 1 interrompue après le manifeste, sortie JSON imbriquée au-delà de la limite de l'interpréteur. |

Décision N-014 (Lazar, 2026-10-07, option (a), GO-2026-10-07-01) appliquée au texte avant le scellement : sorties versées au dépôt privé à chaque étape (section 8).
