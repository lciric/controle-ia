# Consigne : inventaire des jeux de T0.7 (J-D, J-C, J-A, phrases des concepts) et plan pour les sceller avant l'étape A — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`), autonomie de 12 heures (R-2088). Destinataire : un **agent neuf** (Opus), qui n'a écrit ni T0.7, ni son module, ni ses jeux, ni leurs contre-lectures ; ni lecteur exploratoire de 7a, ni auditeur DT-4. Ayant lu T0.7, il est exclu ensuite de tout rôle de lecteur de P3-bis.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise** (`git grep` avec exclusions ; aucune recherche récursive qui traverse un chemin interdit). Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. **Les textes d'actions de P3 ne s'ouvrent pas** (ils se passent aux scripts sans être lus, comme l'a fait la fille 12, R-1674). Aucun appel externe, aucune dépense, aucune écriture git ; branches lues par `git show` ou `git log` sur des refs déjà présentes, ou récupérées par `git fetch` **avec refspec explicite** vers `refs/remotes/origin/…` (permis ici, lecture seule).

## Mandat (lecture seule, puis plan)

1. **État exact** de chaque jeu exigé par le brouillon 20 de T0.7 (`brouillons/T0.7-sondes-v0-v1-brouillon20.md`, section « Documents » l. 692 à 699, section « Module », clés `SCELLEMENT-JEUX-T07-JD`, `-JC`, `-JA`, `SCELLEMENT-CONCEPTS-T07`) : fichiers (branche, commit, chemin, empreinte), contre-vérification faite ou non, lignes de registre présentes ou non (`registres/` de `main`), écarts à la consigne v3 scellée (`docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md`, `d9de50a6…`) et à la consigne des concepts (`brouillons/T0.7-concepts-sans-lien-consigne-v1-brouillon1.md`, `acc7bdfb…`) ; registre `registres/decisions.md` R-1588, R-1656, R-1663, R-1674, R-1675 et suivantes sur la fille 12 ; branche `prep/fille-12-t07-v1`.
2. **Format exigé par le module** au commit `8dc1cb09` de `prep/t07-module-v2` (lecture par `git -C /home/user/wt-t07 show 8dc1cb09:<chemin>`) : forme des fichiers de jeux et du fichier des phrases des concepts (première ligne `format_lecture`, au moins quatre concepts, un seul fichier), lignes de registre attendues (forme exacte).
3. **Plan chiffré** pour que tout soit écrit, contre-vérifié et scellé **au plus tard le 14 novembre** : qui écrit (agent neuf), avec quels outils (scripts du dépôt, tokeniseur réel s'il est au dépôt ; aucun appel externe), quelle contre-vérification à l'aveugle, quelles lignes de registre ; ce qui demande un mot de Lazar ou une dépense (nœud) ; ce qui se fait sans.

## Sortie

`docs/notes/g0-deux-semaines-v1/t07-jeux-inventaire-v1/inventaire-jeux-t07-v1.md`, scellé : table par jeu (état, chemin, empreinte, manque), format exigé, plan. Rien d'autre écrit. Réponse courte : chemin, empreinte, état en trois lignes, ce qui bloque.
