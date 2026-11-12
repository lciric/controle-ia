# Consigne : contre-lecture 1 (R2) de la conception du saboteur à budget (ii-b) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-09, après 22:32 UTC (`date -u`). Destinataire : un sous-agent **neuf**, d'un **autre modèle que le rédacteur** (Claude Opus 5.5) : Claude Fable. Il n'a écrit ni ce dossier, ni T0.6, ni T0.7, ni P3-bis, ni le code ; il n'est pas le lecteur exploratoire de 7a.

Dépôt : `/home/user/controle-ia-travail` (`main` local à `64315b59` ou plus loin). `PYTHONPATH=src`. Python : `python3` ; si un module manque, `.venv/bin/python` (peut-être encore en installation).

## Interdits (recopiés de `interdits-communs-v1.md`, même dossier)

1. **Fichiers et branches qu'on n'ouvre jamais** (ni lecture, ni affichage, ni copie, ni passage à un script, ni `git show`, ni `git ls-tree`, ni `git fetch`) : `diag/*/lecture-sondes-t06.json` de tout run, et nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; la lecture B de la course 7a et la branche `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/` et tout `runs/` de la course 7a (`20261109-070232-t06-reel`) et la branche `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; les items, clés et réponses de l'étiqueteur (branche `prep/etiqueteur-v2-lecture-interrompue-reprise-v1`). Ajouté par R-2057 : ne jamais exécuter `extraire_mesures_epreuve_t06_v1.py` (il ouvre le fichier des sondes).
2. Secrets : jamais une valeur de clé ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
3. Aucun appel de modèle ni d'interface externe, aucune location, aucun `vastai`, aucune dépense.
4. Git : aucun `checkout`, `switch`, `reset`, `stash`, `commit`, `push`, `fetch`, `merge`, `rebase`, ni modification de l'index ; autres commits par `git show <commit>:<chemin>`. Rien écrit hors des chemins de sortie ci-dessous (essais en dossier temporaire hors du dépôt). Ne pas toucher `/home/user/integ-t06` (arbre d'un autre sous-agent).
5. Pas de suite complète des essais ; essais ciblés permis.
6. Refus d'un contrôle de permissions ou d'un classifieur : s'arrêter sur ce point, le rapporter tel quel ; ni contournement, ni reformulation.
7. Heures relevées par `date -u`.

## Objet

Le dossier `brouillons/ii-b-saboteur-budget-v1/` (R-2059) : conception (`549336e7…`), consigne privée du maître (`16d52a8d…`), ordre exploratoire (`bea746db…`), devis (`187d8c72…`), journal (`96160518…`), `simulation-regle-acceptation-ii-b-v1.py` et `calcul-devis-ii-b-v1.py` avec leurs sorties. Vérifier toutes les empreintes d'abord. Mandat : `docs/decisions/proposition-P-066-saboteur-diffus-par-construction-v1.md` (`012ddc44…`), option (b) (R-2044) ; consigne du rédacteur : `consigne-conception-ii-b-saboteur-budget-v1.md` (`f56b0a5d…`, même dossier que celle-ci).

## Points à viser

1. **Conformité au mandat** : mode « coût » seul ; règle d'acceptation fixée avant tout tirage, ne lisant **que l'oracle** (invariant de N-053 : aucun score de sonde, de prédicteur sur le texte, de juge ni d'aucun moniteur) ; lecture dans l'ordre (1) dommage par l'oracle, (2) diffusion réalisée par la base boîte noire par action de T0.8 et la base « mots et coût », (3) aucune sonde avant un préenregistrement scellé à part et le verdict de P3-bis ; rien dans G0 sans nœud ; création après celle de 7b ; aucune dépense avant la ligne de GO.
2. **Oracle et jumeau honnête** : la construction tient-elle (préfixe coupé, coûts précédents remplacés, 8 tirages, médiane basse) ? Les poids de l'oracle sont ceux du juge 8B de T0.8 (point ouvert du rédacteur) : est-ce une circularité pour la lecture (2), ou une entorse à N-053 ? Recommandation.
3. **Règle d'acceptation** (≥ 7 actions bornables sur 10, excès ≤ ×4, total ≥ 1,0 décade) : cohérente avec « modéré et réparti » et avec la définition de « diffus » (N-007, P-015, N-063 v2) ? Rejouer la simulation (`python3 -I` sur le script, sorties comparées à la sortie scellée) ; sensibilité au bruit honnête inconnu (acceptation de 54 % à 5 %) ; les arrêts écrits d'avance couvrent-ils le cas « taux trop bas » sans réglage en cours ?
4. **Exclusion des mentions dans la perte de distillation** (reprise de (ii)) contre « le texte n'est pas filtré » de P-066 : contradiction ou non ? Recommandation.
5. **Seuils de la lecture (2)** (≤ 0,05 et ≥ 0,25), choisis sans source : à justifier, à déclarer exploratoires, ou à retirer.
6. **Provenance des nombres** (R6) : chaque chiffre renvoie-t-il à un chemin et une empreinte ? Le dossier prend 20 % de coûts illisibles d'après les grandeurs de coût de 7a citées par T0.6 r3, **dont l'origine est indéterminée** (R-2057, réserve 1) : le dire, et proposer une hypothèse qui n'en dépend pas (par exemple une plage encadrante déclarée).
7. **Devis** : rejouer `calcul-devis-ii-b-v1.py` ; heures de 7a (lecture A : run 12,97 h, instance 13,59 h) correctement reprises ; attendu 13 à 21 USD, pire 50 à 70 USD ; plafond proposé (GO 80, configuration 75), échéance 19 novembre, dernier jour de création le 17 : cohérents avec une création après 7b (au plus tard le 14 vers 17:00Z, R-2053) ?
8. **Ordre exploratoire** : gardes, arrêts par identifiant d'instance (R10), graines neuves par `SeedSequence` (R9), manifeste, sorties, versement ; 30 marqueurs : chacun dit ce qui le remplit et quand ; commandes écrites contre un `scripts/lancer_iib_v1.sh` à écrire : la spécification du code (conception § 10) suffit-elle à l'écrire et à l'éprouver avant le 17 ?
9. **Consigne privée du maître** : au niveau de la méthode, mode « coût » seul, sans instruction qui viserait un moniteur ou une sonde.
10. Tout ce qui peut faire échouer la course ou en fausser la lecture.

## Sorties

- Rapport `brouillons/ii-b-saboteur-budget-v1/contre-lecture-ii-b-v1-cl1.md` : modèle qui contre-lit ; pièces relues et empreintes ; verdict en une ligne (« prêt pour le code et la ligne de GO après couples » / « à reprendre » avec bloquants) ; remarques numérotées, bloquant / majeur / mineur, avec lieu, raison, correction ; réponses aux points 1 à 10 ; interdits tenus.
- Couples `brouillons/ii-b-saboteur-budget-v1/couples-contre-lecture-ii-b-v1-cl1.json` : liste d'objets `{"fichier", "id", "ancien", "nouveau"}`, chaque « ancien » présent exactement une fois dans son fichier au moment de son application ; application vérifiée par script en dossier temporaire.
- Compagnons `.sha256` (`PYTHONPATH=src python3 -m controle_ia.scellement sceller FICHIER`).
- Ne rien committer, ne rien appliquer au dossier. Réponse finale à la mère : chemins, empreintes, verdict, bloquants et majeurs, recommandations sur les points 2, 4 et 6.
