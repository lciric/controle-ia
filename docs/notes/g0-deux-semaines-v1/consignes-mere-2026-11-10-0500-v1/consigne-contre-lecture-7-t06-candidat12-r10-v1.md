# Consigne : contre-lecture 7 de T0.6 candidat 12 — différentiel révision 9 → révision 10 (trois couples) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`). Destinataire : un **contre-lecteur neuf, modèle Fable**, qui n'a écrit aucune pièce de T0.6, T0.7 ou P3-bis, ni aucune contre-lecture antérieure de T0.6 ; ni lecteur exploratoire de 7a (R-2041), ni auditeur de l'écart DT-4 (R-2057). Les révisions 9 (couples de la contre-lecture 6) et 10 (trois couples de la mère, servie en Opus 5.5) sont écrites par script.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/interdits-communs-v1.md` (`851028fc…`), en entier. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. Aucun appel externe, aucune dépense, aucune écriture git.

## À lire

`brouillons/T0.6-organismes-v0-v1-candidat12-r8.md`, `-r9.md`, `-r10.md` (sceaux à côté) ; scripts `-r9-faire-v1.py`, `-r10-faire-v1.py` ; couples `prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r8-cl6-couples-v1.json` et `brouillons/T0.6-organismes-v0-v1-candidat12-r10-couples-v1.json` ; rapport de la contre-lecture 6 (`8d142183…`) ; R-2080 de `registres/decisions.md`. Le commit `3bf36bfa` se lit par `git show` seulement.

## Points à juger

1. Rejeu : r8 + C6-1 à C6-8 rend `f7fd518f…`, puis le marqueur `EMPREINTE_RAPPORT_CL6_T06` rempli par `8d142183…` rend la r9 ; r9 + R10-1 à R10-3 rend la r10 ; chaque « ancien » une fois (dossier temporaire à toi sous `/home/user/cl7-t06-tmp/`, effacé ensuite par son chemin exact).
2. Sections gelées (« Hypothèse » à « Liste d'arrêt ») égales à l'octet de la r7 à la r10.
3. R10-3 lève-t-il la contradiction entre le point 3 du plan (« et rien d'autre ») et la section « Puissance » (pièces v3 copiées dans le commit de scellement), sans en créer une autre ? Les pièces nommées existent à `3bf36bfa` avec les empreintes citées par le texte ?
4. Scellabilité : `controle_ia.prereg.problemes` vide sur la r10 ; huit citations, « Commit du code d'analyse » et amorce une fois chacune ; titre et statut cohérents.

## Sortie

`prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r10-cl7.md`, scellé : verdict en une ligne ; points 1 à 4 ; défauts et, s'il en faut, couples au format habituel dans `…-r10-cl7-couples-v1.json` (scellé) ; heures `date -u`. Ne pas ajouter de marqueur : la mère inscrira cette contre-lecture au registre et dans la passation, pas dans le texte (sauf si tu juges qu'une entrée dans le texte est exigée par R2 ou R6 : dis-le alors, sans l'écrire). Réponse courte : chemins, empreintes, verdict.
