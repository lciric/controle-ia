# Consigne : contre-lecture 5 (R2) de T0.6 candidat 12, différentiel r4 → r6 — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`). Destinataire : un sous-agent **neuf**, d'un **autre modèle** que la mère, le rédacteur de la r4 et l'analyste de la concordance (tous Claude Opus 5.5) : Claude Fable. Il n'a écrit aucune des pièces relues ; il n'est pas le lecteur exploratoire de 7a.

Dépôt : `/home/user/controle-ia-travail` (`main` à `48d3062e` ou plus loin). `PYTHONPATH=src`. Python : `.venv/bin/python`.

## Interdits (ceux de `interdits-communs-v1.md`, même dossier, en entier)

Fichiers et branches sous embargo jamais ouverts (`diag/*/lecture-sondes-t06.json`, nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/` et `runs/` de 7a et la branche `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; étiqueteur) ; jamais `extraire_mesures_epreuve_t06_v1.py` ; aucune valeur de clé, jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ` ; aucun appel externe, aucune dépense ; refus de contrôle ou de classifieur : arrêt et rapport tel quel ; heures par `date -u`. Git en lecture seule (`git show` ; `git archive` vers un dossier temporaire hors du dépôt permis) ; rien écrit hors des sorties ; ne pas toucher `/home/user/integ-t06`.

## Objet

`brouillons/T0.6-organismes-v0-v1-candidat12-r6.md` (`b00ed071…`) contre la r4 (`eb6f10a0…`) et la r5 (`8fde62db…`) ; scripts `brouillons/T0.6-organismes-v0-v1-candidat12-r5-faire-v1.py` et `brouillons/T0.6-T0.7-concordance-appliquer-v1.py` ; contre-lecture 4 et ses couples ; note de concordance `docs/notes/g0-deux-semaines-v1/concordance-t06-t07-v1/note-concordance-t06-r5-t07-b18-v1.md` (`6146fe85…`) et couples ; `registres/decisions.md` R-2066 à R-2071 ; T0.7 brouillon 19 (`07039ed2…`) pour la Concordance ; chaîne gelée au commit `1609a4bf` ; décision N-063 v2.

## Points à viser

1. Rejeu : r4 + U1 à U13 + trois marqueurs → r5 ; r5 + CONC-T06-01 à 05 → `f446028b…` ; + en-tête → r6.
2. Valeurs des trois marqueurs remplis par la mère à la r5 (`EMPREINTE_RAPPORT_CL4_T06`, `PIECES_PUISSANCE_T06`, `DECISION_LAZAR_ECART_DT4_R2041`) : exactes et vérifiables (R-2066, R-2067).
3. **Les quatre couples dans les sections gelées** (CONC-T06-01 à 04) : nécessaires ? conformes à N-063 v2 ? changent-ils une hypothèse, une prédiction, un signe ou un seuil (ce serait un nœud de Lazar) ? effet sur la puissance et le devis ? cohérence avec la chaîne gelée (rien ne doit exiger de changer l'arbre de `1609a4bf`).
4. **CONC-T06-05** (« Concordance avec T0.7 ») : la pièce de lecture « mots et coût » jouée après la course, hors de l'arbre gelé, ne lit jamais `lecture-sondes-t06.json` ; format du fichier `issue-mots-et-cout-t06.json` conforme à ce que lit le module de T0.7 ; dépendance à T0.8 (non scellé) déclarée ; garde du script de contrôle (`SCELLEMENT-P3BIS` contre `VERDICT-P3BIS`) : à corriger ou à déclarer.
5. En-tête de la r6 : exact (y compris la correction du titre de la r5) ; huit citations du lanceur une fois chacune ; amorce citée ; `prereg.problemes` ne signale que `MOT_LAZAR_GO_7B` et `MOT_LAZAR_GRANDEURS_COUT_7A`.
6. Ce qui peut encore faire échouer le scellement, la course 7b ou la lecture.

## Sorties

Rapport `prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r6-cl5.md` (modèle ; pièces et empreintes ; verdict en une ligne ; remarques bloquant / majeur / mineur ; réponses aux points 1 à 6 ; interdits tenus) ; couples `…-r6-cl5-couples-v1.json` (chaque « ancien » une fois dans la r6 au moment de son application ; ils écrivent l'entrée « Contre-lecture 5 » faite, avec un marqueur pour l'empreinte du rapport si nécessaire) ; compagnons `.sha256`. Rien committé, rien appliqué.
