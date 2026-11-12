# Consigne : contre-lecture 4 (R2) de T0.6 candidat 12, différentiel r3 → r4 — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`). Destinataire : un sous-agent **neuf**, d'un **autre modèle que le rédacteur de la r4** (Claude Opus 5.5) : Claude Fable. Il n'a écrit ni la r4, ni la r3, ni la contre-lecture 3, ni le code ; il n'est pas le lecteur exploratoire de 7a.

Dépôt : `/home/user/controle-ia-travail` (`main` local à `94bcd7bb` ou plus loin). `PYTHONPATH=src`. Python : `.venv/bin/python`.

## Interdits (ceux de `interdits-communs-v1.md`, même dossier, en entier)

Fichiers et branches sous embargo jamais ouverts (`diag/*/lecture-sondes-t06.json`, nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/` et `runs/` de 7a et la branche `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; étiqueteur) ; jamais `extraire_mesures_epreuve_t06_v1.py` ; aucune valeur de clé, jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ` ; aucun appel externe, aucune dépense ; git en lecture seule (autres commits par `git show` ; une extraction par `git archive` dans un dossier temporaire hors du dépôt est permise pour faire tourner le code de `1609a4bf`) ; rien écrit hors des sorties ci-dessous ; ne pas toucher `/home/user/integ-t06` ; refus de contrôle ou de classifieur : arrêt et rapport tel quel ; heures par `date -u`.

## Objet

`brouillons/T0.6-organismes-v0-v1-candidat12-r4.md` (`eb6f10a0…`), son journal (`e1afb0cc…`), ses couples (`…-r4-couples-v1.json`, `1d2a85dc…`), la variante (a) (`…-r4-couples-variante-a-v1.json`, `82e49515…`) et le script d'application (`fc5046e0…`), contre la r3 (`c24e268e…`) ; R-2062 à R-2065 ; contre-lecture 3 et ses couples ; rapports `docs/notes/g0-deux-semaines-v1/integration-t06-v13-main-v1/rapport-integration-v1.md` (`427def65…`) et `rapport-essai-blanc-S-voie-b-v1.md` (`4f4eb27d…`) ; audit DT-4 (`4882fe4d…`) ; lanceur v13, amorce v11, `harnais/validation_reelle.py`, `t06/lanceur.py` au commit `1609a4bf`.

## Points à viser

1. **Rejeu** : appliquer les couples r4 à la r3 par script en dossier temporaire → `eb6f10a0…` ; appliquer la variante (a) → texte attendu du rédacteur (`c371a96f…`, à recalculer) ; Y4 à Y8 et Y10 à Y12 égaux à l'octet au fichier de la contre-lecture 3.
2. **Sections gelées** (« Hypothèse » à « Liste d'arrêt ») identiques à l'octet à la r3 : le vérifier par programme. X19 gardé (troncatures par condition) : sans nombre de 7a ?
3. **Voie B** (W-B1 à W-B4) : exacte au regard du lanceur v13 (`commit_s`, ancêtre d'`origin/main`, citations et sceaux lus dans S, amorce citée) et des gardes (`exiger_code_cite` avec `1609a4bf`) ; ce que Y1, Y2, Y9 disaient de vrai est-il gardé ? Le plan de la confirmation dit-il clairement l'ordre : commit des 71 sceaux, S, fusion dans `main`, poussée, contrôles, création ?
4. **Option (b)** (W-C1 à W-C5) : plus aucune grandeur de coût de 7a dans le texte hors des « avant » des couples ; la puissance de 7b repose sur le plan d'avant 7a (script et sortie de puissance v3) et sur les heures de la lecture A ; arithmétique juste ; rien dans un critère.
5. **Marqueurs** : valeurs remplies exactes (recalculer les huit empreintes et l'amorce au commit `1609a4bf`, l'empreinte canonique de la configuration par le code de `1609a4bf`, les trois valeurs de la contre-lecture 3) ; `prereg.problemes` ne signale que `MOT_LAZAR_GO_7B` et `DECISION_LAZAR_ECART_DT4_R2041` ; huit citations conformes (forme du § 3.3 du rapport d'essai à blanc).
6. **Entrée « Contre-lecture 4 »** : vos couples doivent la réécrire (faite, par vous, avec brouillon relu `eb6f10a0…` et votre rapport) ; le rédacteur signale qu'elle passe `problemes` avant d'être faite : proposer si un marqueur est nécessaire.
7. Ce qui peut encore faire échouer le scellement ou la création de 7b.

## Sorties

- Rapport `prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r4-cl4.md` (modèle qui contre-lit ; pièces et empreintes ; verdict en une ligne : « scellable après couples » ou bloquants ; remarques numérotées bloquant / majeur / mineur ; réponses aux points 1 à 7 ; interdits tenus).
- Couples `prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r4-cl4-couples-v1.json` (`{"id", "ancien", "nouveau"}`, chaque « ancien » une fois dans la r4 au moment de son application ; vérifié par script en dossier temporaire ; texte obtenu et marqueurs restants dits au rapport).
- Compagnons `.sha256`. Rien committé, rien appliqué à la r4.
