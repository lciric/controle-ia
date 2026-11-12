# Consigne : essai de concordance du journal des ouvertures de P3-bis (écrivain) avec le lecteur de T0.7 — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`), autonomie de 12 heures (R-2088). Destinataire : un **agent neuf** (Opus), qui n'a écrit ni le code de P3-bis, ni celui de T0.7, ni leurs textes, ni leurs contre-lectures. Il lit des fichiers de T0.7 : il est **exclu ensuite de tout rôle de lecteur de P3-bis**.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise**. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. Aucun appel externe, aucune dépense, aucune écriture git, rien dans les arbres `/home/user/wt-*`.

## Pièces (lecture par `git show <commit>:<chemin>` depuis `/home/user/controle-ia-travail`)

- **Écrivain** : `src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py` au commit `02217f1c` (branche `prep/p3bis-code-v2`) ; compte rendu du code v2 `brouillons/P3-bis-temoin-positif-v1/compte-rendu-developpeur-code-p3bis-v2.md` (`f6c93bc5…` : choix E-3, E-8, E-9, codes de refus) ; texte `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md` (`9038a015…`), format du journal.
- **Lecteur** : `src/controle_ia/t07/journal_p3bis_v1.py` (et ce qu'il importe) au commit `8dc1cb09` (branche `prep/t07-module-v2`) ; texte `brouillons/T0.7-sondes-v0-v1-brouillon20.md` (`9ef671ac…`), section « Module », lecture du journal de P3-bis au format b8.

## Mandat

1. Copier les deux modules (et leurs dépendances nécessaires, prises aux mêmes commits) dans un dossier neuf `/home/user/concordance-journal-tmp/` ; écrire un script d'essai à toi qui, dans un dépôt git jetable sous ce dossier (`GIT_CEILING_DIRECTORIES` posé), fait **écrire** par l'écrivain de P3-bis chaque type de ligne du journal `registres/ouvertures-p3bis-v1.md` (ouverture réduite, pleine, pleine anticipée, chaque refus de la liste fermée, `deja-ouverte`, lignes sans journal des cas E-8/E-9 s'il y en a) et les fait **lire** par le lecteur de T0.7 ; pour chaque ligne : lue telle quelle, refusée (motif), ou mal interprétée.
2. Comparer aussi les deux textes (format écrit au brouillon 10 de P3-bis contre format lu au brouillon 20 de T0.7) : en-tête, cellules, clés, codes de motif, dates.
3. Lister chaque discordance avec sa correction proposée (côté écrivain, côté lecteur, ou au texte), sans rien corriger toi-même.

## Sortie

`docs/notes/g0-deux-semaines-v1/concordance-journal-p3bis-t07-v1/rapport-concordance-journal-v1.md` (scellé) et le script d'essai `…/essai_concordance_journal_v1.py` (scellé) dans `/home/user/controle-ia-travail` ; dossier temporaire effacé ensuite par son chemin exact. Réponse courte : chemins, empreintes, concordance en une ligne, discordances.
