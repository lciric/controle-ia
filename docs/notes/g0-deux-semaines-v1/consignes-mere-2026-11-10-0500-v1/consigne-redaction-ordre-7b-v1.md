# Consigne : rédiger l'ordre de la course de confirmation 7b de T0.6 (à remettre par Lazar à une session fille qui a les clés) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`). Destinataire : un **rédacteur neuf** (Opus), qui n'a écrit ni T0.6, ni T0.7, ni P3-bis, ni leurs contre-lectures, ni l'ordre de 7a ; il n'est ni le lecteur exploratoire de 7a (R-2041) ni l'auditeur de l'écart DT-4 (R-2057).

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/interdits-communs-v1.md` (`851028fc…`), en entier. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni la branche `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. Aucun appel externe, aucune dépense, aucun `vastai`, aucune écriture git (la mère committe). Tu peux lire la lecture A de 7a (`docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/lecture-A-exploratoire-non-opposable-v1.md`) : elle ne porte que des comptes de garde, des heures et la mémoire.

## À lire

- Texte scellé : `prereg/T0.6-organismes-v0-v1.md` (`ef31feff…`, révision 10 ; commit S `935262b1`, fusionné dans `main` à `1756f1cb`) et sa configuration `prereg/T0.6-organismes-config-7b-v1.json` (`b7a5c1ba…`) ; en particulier « Plan d'analyse » (point 9 : fenêtre de carte, relance de DT-6), « Liste d'arrêt », « Devis » (ligne d'engagement proposée), « Ce qui manque pour lancer » (point 3 : contrôles en ligne, branche de sortie, gardes à rejouer ; points 5 et 6).
- Registre : `registres/decisions.md` R-2039 à R-2041 (course 7a, lecture A, **écart DT-4 : faute de la mère**, consigne de lecture sans rappel de l'embargo), R-2048, R-2057, R-2062, R-2064, R-2077 (mot de Lazar : création de 7b autorisée, **200 USD, compte rendu à Lazar à 60 USD de dépense, mot de Lazar avant toute création sur H200**), R-2079 (option (c) : chaîne v13, création au plus tard le 15, bascule éventuelle le 13 à 12:00 UTC), R-2082 (scellement) ; `registres/go.md` lignes GO-2026-11-02-28, GO-2026-11-07-02 (carte de repli), GO-2026-11-07-04 (bras B de l'audit de fuite), GO-2026-11-10-01 (prolongation, **non lue par la chaîne v13**).
- Modèle d'ordre : `docs/procedures/ordre-fille-cles-2-course-dose-reponse-exploratoire-v1.md` et ses deux addenda (7a).
- Chaîne gelée au commit `1609a4bf` (lecture par `git show 1609a4bf:<chemin>`) : `scripts/lancer_t06_v13.sh` (usage en tête, sous-commandes `controles`, `creation`, surveillance, récupération), `scripts/amorce_instance_t06_v11.sh`.

## Ce que l'ordre doit fixer

1. **Préalables bloquants** avant toute création, vérifiés par la fille et écrits dans son journal : T0.6 scellé (S `935262b1` ancêtre d'`origin/main`) ; **T0.7 scellé** (ligne `SCELLEMENT-T07` au registre de `main`, empreinte vérifiée ; GO-2026-11-02-28 l'exige) ; ligne de GO lue par la chaîne : GO-2026-11-02-28 ; jour ≤ 15 novembre (création au plus tard le 14 vers 17:00Z pour garder une relance complète, d'après le texte).
2. **Commandes exactes** (sur le modèle de 7a, adaptées au mode course de v13) : clone de `main`, `controles` en ligne, branche de sortie neuve absente du dépôt distant (nom à proposer, par exemple `calcul/t06-confirmation-7b-v1`), gardes rejouées dans un clone fait comme celui de l'amorce, création ; variables passées par `env -i` avec les seuls **noms** des clés (jamais une valeur lue ni affichée) ; `GO_ID=GO-2026-11-02-28` pour la garde de calcul ; `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`.
3. **Carte** : A100 conforme d'abord (fenêtre du texte) ; la création sur H200 (carte de relance, GO-2026-11-07-02, relance de DT-6) **n'est jouée qu'après un mot de Lazar** donné dans la session de la fille (R-2077, articulation écrite par la contre-lecture 6, couple C6-3) ; l'attente de ce mot est prévue.
4. **Dépense** : ligne d'engagement au registre des dépenses avant la création ; **compte rendu à Lazar à 60 USD** ; plafond de la configuration 200 USD (arrêt de la chaîne) ; arrêts et destruction **par identifiant d'instance** (R10), jamais par motif ; inventaire filtré à la fin.
5. **Embargo DT-4** (rappelé nommément, faute R-2041) : la fille n'ouvre, n'affiche, ne copie ni ne passe à un script aucun `lecture-sondes-t06.json` (ni celui de 7b, ni celui de 7a), ni la branche de quarantaine ; elle ne lance jamais `extraire_mesures_epreuve_t06_v1.py` ; elle rapatrie les sorties par refspec explicite, vérifie les compagnons par empreinte, et ne lit que ce que l'ordre nomme (journal de la chaîne, `lancement.txt`, manifeste, codes de sortie, dépense).
6. **Bras B de l'audit de fuite** (GO-2026-11-07-04) : s'il est joué par la chaîne sur la même machine, le dire ; sinon, l'écrire comme hors de cet ordre.
7. **Compte rendu de la fille** (nombres seuls, sans aucune valeur de sonde), arrêts, ce qui suit (lecture de T0.6 selon le texte, après le verdict de P3-bis pour les sondes).
8. **Ce que l'ordre ne fait pas** : aucune lecture de résultat ; aucune étape de T0.7 (l'étape A a sa propre ligne de GO) ; aucun contact externe.
9. Marqueurs `<<…>>` pour ce que la mère remplira (par exemple la ligne `SCELLEMENT-T07`, l'identifiant de la session fille), une occurrence chacun.

## Sortie

`docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon1.md`, scellé (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`), et un journal court `…-brouillon1-journal-v1.md` (sources lues avec leurs lignes, choix faits, points ouverts), scellé. Réponse courte à la mère : chemins, empreintes, marqueurs, points ouverts.
