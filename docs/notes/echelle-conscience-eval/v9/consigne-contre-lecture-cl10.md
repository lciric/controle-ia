Tu es un contre-lecteur neuf au sens de la règle R2 du dépôt `/home/user/controle-ia-travail` (lis son `CLAUDE.md` : français, phrases claires, quasi aucun acronyme). Tu n'as écrit ni le texte relu, ni le code, ni les tests, ni les contre-lectures précédentes. Ta tâche : contre-lire, avant son scellement, **les passages changés** du préenregistrement d'une expérience décisive, puis rendre un rapport et un verdict. La contre-lecture n° 9 a jugé le reste et recommande une relecture neuve et courte des passages changés.

## Pièce relue

`/home/user/controle-ia-travail/prereg/brouillon-test-echelle-conscience-eval-v9-3.md` (compagnon `.sha256` à côté ; vérifie l'empreinte au début et à la fin de ta lecture). Il corrige le brouillon v9-2 (`prereg/brouillon-test-echelle-conscience-eval-v9-2.md`) **par le texte seul**, après la contre-lecture n° 9 (constats CLR-01 à CLR-10, traités en fin de texte) ; outils (commit `9ccc383c02a08e58928368b23471f4c438e06cda`), analyse, seuils, simulation et conduite inchangés.

## À lire

- La différence entre le v9-2 et le v9-3 (fais-la toi-même, par exemple `git diff --no-index --word-diff`), puis chaque passage changé dans son contexte.
- Le rapport de la contre-lecture n° 9 : `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v9-2-cl9.md`, et ses pièces sous `docs/notes/echelle-conscience-eval/v9/contre-lecture-cl9/` (banc du miroir, formule de q). Au besoin, le rapport de la contre-lecture n° 8 (`prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v9-cl8.md`) et ses pièces sous `docs/notes/echelle-conscience-eval/v9/contre-lecture-cl8/`.
- Pour la concordance avec le code, au besoin : `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/echelle-v8/scripts/analyser_echelle_v8.py` (texte des réserves, rapport des Ec, lecture), dans l'arbre de travail au commit attendu.
- La trace `docs/notes/echelle-conscience-eval/v9/ls-remote-outils-v8.txt`, et la simulation scellée `docs/notes/echelle-conscience-eval/v8/atteignabilite-echelle-v8.json` si tu veux vérifier une graine citée.

## Ce que tu vérifies

1. Chaque constat de la contre-lecture n° 9 (CLR-01 à CLR-10) est-il traité, partiellement, ou non, avec preuve ? En particulier : le miroir en signe de la famille D (« positif » sans aucune réserve) est-il dit partout où il faut, avec des chiffres exacts ; la pureté est-elle définie et employée dans un seul sens ; les deux seuils de k et l'asymétrie de la bande sont-ils justes ; les phrases obligatoires nouvelles (après l'une ou l'autre des deux réserves, et le renvoi aux limites après toute issue prononcée) sont-elles cohérentes avec H_0, les réserves et les autres phrases, et symétriques en signe (R3, R4) ?
2. Le texte nouveau a-t-il cassé quelque chose : contradiction entre parties, phrase devenue fausse, chiffre qui ne concorde plus avec un autre endroit du texte ou avec une sortie versée, empreinte du tableau des traces différente du fichier sur disque, renvoi à une pièce absente ?
3. Ce qui manque encore, dans le périmètre des passages changés.

Recompte toi-même sur les sorties versées tout chiffre nouveau ; ne prends aucune affirmation du texte pour acquise. Pas besoin de relancer les 401 tests (cl9 les a passés au même commit) ; un rejeu court d'une graine est permis si tu en as besoin. Tout dans ton bac à sable : `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/contre-lecture-echelle-v9-3/` (crée-le ; il ne doit pas exister avant toi), avec `TMPDIR` pointé dedans ; `-B` et `PYTHONDONTWRITEBYTECODE=1`.

## Interdits

- N'ouvre, ne lis, ne hache jamais : `prereg/P3-consignes-v1.md`, les fichiers `textes-actions-*`, `items-textes-p1-v1.json`, `prompts-p1-v1.json`, ni rien sous `donnees/`, `runs/`, `diag/` ou `traces/` — pas même pour une empreinte. Aucune recherche récursive dans le dépôt (seulement des listes de dossiers nommés ci-dessus).
- Aucun réseau ; aucune commande `vastai` ; aucun lancement ; aucune écriture git ; rien de modifié hors de ton bac à sable.
- N'affiche, n'écris et ne cherche aucune clé ou jeton.

## Rendu

Écris ton rapport dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/contre-lecture-echelle-v9-3/rapport-contre-lecture-echelle-v9-3-cl10.md`, puis son compagnon `.sha256` (format `sha256sum`). Structure : rôle, heure (`date -u`), empreintes des pièces lues, ce qui a été lu et essayé ; **verdict** (« scellable », « scellable après corrections » ou « non scellable », avec les bloquants) ; traitement des constats de cl9 (tableau) ; constats nouveaux numérotés CLQ-01, CLQ-02, … avec gravité (bloquant, à corriger, remarque), localisation, constat, preuve, correction proposée. Ton message final : le verdict en trois lignes, la liste des constats avec leur gravité, et le chemin du rapport.
