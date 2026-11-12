# Consigne : contre-lecture 6 de T0.6 candidat 12 — différentiel révision 7 → révision 8 — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 vers 06:30 UTC (`date -u`). Destinataire : un **contre-lecteur neuf, modèle Fable** (la révision 8 est écrite par la session mère, servie en Opus 5.5 ; N-052 nomme Fable 5.1 : servi en Fable 5.2, écart déclaré). Il n'a écrit aucune pièce de T0.6, T0.7 ou P3-bis, ni aucune contre-lecture antérieure de T0.6 ; il n'est ni le lecteur exploratoire de 7a (R-2041), ni l'auditeur de l'écart DT-4 (R-2057).

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/interdits-communs-v1.md` (`851028fc…`), en entier. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni la branche `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. Aucun appel externe, aucune dépense ; aucune écriture git (la mère committe).

## À lire (clone `/home/user/controle-ia-travail`, `main`)

- `brouillons/T0.6-organismes-v0-v1-candidat12-r7.md` (`9dd695b1…`) et `brouillons/T0.6-organismes-v0-v1-candidat12-r8.md` (sceau à côté) ; script et couples de la révision 8 (`…-r8-faire-v1.py`, `…-r8-couples-v1.json`, sceaux à côté).
- `registres/decisions.md`, lignes **R-2073** et **R-2077** ; `registres/go.md`, lignes `GO-2026-11-02-28` et `GO-2026-11-10-01`.
- Code gelé au commit `1609a4bf` (lecture par `git show 1609a4bf:<chemin>` seulement) : `scripts/lancer_t06_v13.sh`, `scripts/amorce_instance_t06_v11.sh`, `src/controle_ia/t06/session.py`, `session_v3.py`, `session_v12.py`, `configuration.py`.
- Contre-lecture 5 : `prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r6-cl5.md` (`a951aaaa…`).

## Points à juger

1. **Rejeu** : révision 7 + couples R8-1 à R8-6 rend la révision 8 à l'octet (dans un dossier temporaire à toi, sous `/home/user/cl6-t06-tmp/`, effacé ensuite par son chemin exact) ; chaque « ancien » une fois.
2. **Sections gelées** (« Hypothèse », « Prédiction », « Métrique », « Seuil », « Plan d'analyse », « Critères de lecture gelés », « Liste d'arrêt ») égales à l'octet entre r7 et r8.
3. **Valeurs** : les deux marqueurs remplis disent ce que R-2077 consigne, sans plus ; la lecture de la mère du mot « go » est-elle écrite comme une lecture (et non comme un mot de Lazar) ?
4. **Prolongation** : les affirmations de R8-3 sur la chaîne gelée sont-elles vraies au commit `1609a4bf` (GO-28 en dur en mode course, l. 83 et 123 du lanceur, l. 60 de l'amorce ; `session.verifier_go` refuse GO-28 après le 16 ; une ligne au même identifiant ne peut pas prolonger, R-389) ? La configuration et le calendrier (création au plus tard le 15, fin du GO le 17 à 00:00 UTC) sont-ils cohérents avec la ligne de GO lue par la chaîne ?
5. **Approbation des deux points** de la contre-lecture 5 (R8-5) : conforme à R-2077 ?
6. **Scellabilité** : `PYTHONPATH=src .venv/bin/python -c "from controle_ia.prereg import problemes; print(problemes('brouillons/T0.6-organismes-v0-v1-candidat12-r8.md'))"` rend une liste vide ; les huit citations que lit le lanceur, la ligne « Commit du code d'analyse » et l'amorce apparaissent une fois chacune (forme exacte du lanceur v13, `controles`, l. 112 à 143) ; titre et statut cohérents.
7. Tout autre défaut que tu vois dans le différentiel.

## Sortie

`prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r8-cl6.md`, scellé (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`) : verdict en une ligne (« scellable », « scellable après couples », « non scellable ») ; points 1 à 7 ; défauts numérotés L1… avec, s'il en faut, des couples `{id, section, motif, ancien, nouveau}` dans `prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r8-cl6-couples-v1.json` (scellé) ; heures `date -u`. Réponse courte à la mère : chemins, empreintes, verdict, couples.
