# Consigne : compléter le module de lecture de T0.7 et écrire sa configuration (pour le brouillon 19) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`). Destinataire : un **développeur neuf**, qui n'a écrit ni T0.7, ni T0.6, ni P3-bis, ni le module actuel `src/controle_ia/t07/`, ni leurs contre-lectures, et n'est pas le lecteur exploratoire de 7a.

## Lieu

Arbre de travail isolé à créer **par toi** : `git -C /home/user/controle-ia-travail worktree add -b prep/t07-module-v2 /home/user/wt-t07 48d3062e` (ou la tête de `main` du moment). Tu n'écris que dans `/home/user/wt-t07` ; commits locaux permis sur `prep/t07-module-v2` seulement ; jamais `fetch`, `push`, ni action sur `main` ni sur `/home/user/controle-ia-travail` (sauf l'interpréteur `/home/user/controle-ia-travail/.venv/bin/python`). Ne pas toucher `/home/user/integ-t06`.

## Interdits (ceux de `interdits-communs-v1.md`, en entier)

Fichiers et branches sous embargo jamais ouverts (`diag/*/lecture-sondes-t06.json`, nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/` et `runs/` de 7a et la branche `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; étiqueteur) ; jamais `extraire_mesures_epreuve_t06_v1.py` ; aucune valeur de clé, jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ` ; aucun appel externe, aucune dépense ; refus de contrôle ou de classifieur : arrêt et rapport tel quel ; heures par `date -u`. **Aucune donnée réelle de 7a** : le module s'éprouve sur des données synthétiques seulement. Garde des secrets à 0 avant chaque commit.

## Mandat

`brouillons/T0.7-sondes-v0-v1-brouillon19.md` (`07039ed2…`) fixe ce que le module doit faire. Le rédacteur du brouillon 18 a relevé (journal `brouillons/T0.7-sondes-v0-v1-brouillon18-journal-v1.md`, point ouvert 2) que le module de `main` (commit `51a1874c`, R-1934) ne porte ni la **garde adaptée** de N-066 (`docs/decisions/`), ni la **lecture du journal de P3-bis**, ni les **points (x) à (xv)**, et garde trois questions internes. Travail :
1. Inventaire : chaque exigence du brouillon 19 qui touche le module (section, ligne) contre ce que fait le code ; les trois questions internes du module.
2. Compléter le module par **fichiers neufs ou versions neuves** (R12 : `…_v2.py` plutôt qu'écraser si un fichier est cité par empreinte ailleurs) ; chaque garde d'arrêt éprouvée sur un cas sain et sur un artefact (R5) ; aucune moyenne ni médiane sur les jetons dans une sonde de production ; lecture du fichier `issue-mots-et-cout-t06.json` selon la section « Concordance avec T0.7 » de T0.6 r6 (`brouillons/T0.6-organismes-v0-v1-candidat12-r6.md`, `b00ed071…`).
3. **Configuration de T0.7** (aucune n'existe au dépôt) : fichier neuf sous `brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/` (nom à proposer), valeurs tirées du texte, empreinte canonique calculée par le module.
4. Essais : la suite des essais de T0.7 sur ton arbre, et la suite complète si le temps le permet (dire combien de temps) ; aucun essai existant modifié pour passer.
5. Ne pas écrire dans le brouillon 19 : lister au rapport les valeurs que la mère y mettra (`COMMIT_CODE_T07`, `EMPREINTES_CODE_T07`, `EMPREINTE_CONFIG_T07`) et les écarts entre texte et code.

## Sorties

Commits locaux sur `prep/t07-module-v2` (non poussés) ; rapport `docs/notes/g0-deux-semaines-v1/t07-module-v2/rapport-developpeur-t07-module-v2.md` dans ton arbre, avec compagnon ; réponse courte à la mère : commits, compte des essais, valeurs des marqueurs, écarts texte / code, ce qui reste avant la contre-lecture du code (par un autre modèle).
