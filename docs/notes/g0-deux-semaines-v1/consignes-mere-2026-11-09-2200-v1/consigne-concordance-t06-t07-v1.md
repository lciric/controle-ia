# Consigne : concordance entre T0.6 (r5) et T0.7 (brouillon 18), avant le scellement de T0.6 — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`). Destinataire : un analyste **neuf**, qui n'a écrit ni T0.6, ni T0.7, ni leurs contre-lectures, ni le code, ni P3-bis, et n'est pas le lecteur exploratoire de 7a.

Dépôt : `/home/user/controle-ia-travail` (`main` local à `3b9e00c9` ou plus loin). `PYTHONPATH=src`. Python : `.venv/bin/python`.

## Interdits (ceux de `interdits-communs-v1.md`, même dossier, en entier)

Fichiers et branches sous embargo jamais ouverts (`diag/*/lecture-sondes-t06.json`, nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/` et `runs/` de 7a et la branche `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; étiqueteur) ; jamais `extraire_mesures_epreuve_t06_v1.py` ; aucune valeur de clé, jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ` ; aucun appel externe, aucune dépense ; git en lecture seule (`git show`, `git archive` vers un dossier temporaire hors du dépôt) ; rien écrit hors des sorties ci-dessous ; ne pas toucher `/home/user/integ-t06` ; refus de contrôle ou de classifieur : arrêt et rapport tel quel ; heures par `date -u`.

## Pièces

- T0.6 : `brouillons/T0.6-organismes-v0-v1-candidat12-r5.md` (`8fde62db…`) ; la chaîne qui sera jouée par 7b est l'arbre gelé de `1609a4bf` (voie B, R-2062) : `src/controle_ia/t06/` (dont `lecture.py`, `lecture_v2.py`, `lanceur_v6.py`), `scripts/lancer_t06_v13.sh`, `scripts/amorce_instance_t06_v11.sh`, au commit `1609a4bf`.
- T0.7 : `brouillons/T0.7-sondes-v0-v1-brouillon18.md` (`fe02da17…`) et son journal (`e932573f…`, points ouverts) ; module `src/controle_ia/t07/` sur `main`.
- Décisions : N-063 v2, N-066, P-064, P-065 (`docs/decisions/`) ; `registres/decisions.md` R-2062 à R-2069.

## Questions

1. **Ce que T0.7 attend de T0.6**, élément par élément (phrase exigée par la Concordance de T0.7 : doses `S25` à `S100` seules, « non calculable » distinct de « échoue » ; fichier `ISSUE-MOTS-ET-COUT-T06` et ses champs ; registre partagé ; règle d'ex aequo ; niveau de l'intervalle de la base ; définition de `aire` ; toute autre dépendance) : pour chacun, ce que dit la r5 (citation, ligne), et **ce que la chaîne de `1609a4bf` produit réellement sur l'instance** (fichiers et champs écrits, lus dans le code, sans aucune donnée de 7a).
2. Pour chaque écart : où le régler au moindre coût — dans T0.6 (si possible **hors** des sections « Hypothèse » à « Liste d'arrêt » ; si une section gelée doit changer, le dire en clair, avec la raison), dans T0.7, ou par une pièce à part produite après la course par un module de lecture (sans toucher la chaîne gelée). Rien ne doit exiger un changement de l'arbre gelé de `1609a4bf`.
3. Ce que T0.7 peut et ne peut pas lire des sorties de 7b, compte tenu de DT-4 (aucune sonde lue avant le verdict scellé de P3-bis) et de la garde N-066.
4. `NIVEAU_BASE_T06` : quelle valeur la r5 et la chaîne impliquent-elles (code) ?

## Sorties

- Note `docs/notes/g0-deux-semaines-v1/concordance-t06-t07-v1/note-concordance-t06-r5-t07-b18-v1.md` : table des dépendances, écarts, recommandation par écart, ce qui bloque le scellement de T0.6.
- Couples proposés `…/couples-t06-r5-concordance-v1.json` et `…/couples-t07-b18-concordance-v1.json` (`{"id", "ancien", "nouveau"}`, chaque « ancien » une fois dans son texte ; vérifiés par script en dossier temporaire ; empreintes des textes obtenus au rapport), en le moins de couples possible.
- Compagnons `.sha256`. Rien committé, rien appliqué. Réponse courte à la mère : écarts, couples, sections gelées touchées ou non, ce qui bloque.
