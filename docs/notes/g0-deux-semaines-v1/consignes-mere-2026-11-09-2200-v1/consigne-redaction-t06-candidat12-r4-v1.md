# Consigne : T0.6 candidat 12, révision 4 (voie B, R-2062 et R-2064) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10, après 00:33 UTC (`date -u`). Destinataire : un **rédacteur neuf**, qui n'a écrit ni la r3, ni ses brouillons, ni la contre-lecture 3, ni le code, ni T0.7, ni P3-bis, ni (ii-b), et n'est pas le lecteur exploratoire de 7a.

Dépôt : `/home/user/controle-ia-travail` (`main` local à `8ce3a340` ou plus loin). `PYTHONPATH=src`. Python : `.venv/bin/python`.

## Interdits (ceux de `interdits-communs-v1.md`, même dossier, en entier)

Fichiers et branches sous embargo jamais ouverts (`diag/*/lecture-sondes-t06.json`, nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/` et `runs/` de 7a et la branche `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; étiqueteur) ; jamais `extraire_mesures_epreuve_t06_v1.py` ; aucune valeur de clé, jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ` ; aucun appel externe, aucune dépense ; git en lecture seule (autres commits par `git show`), rien écrit hors des sorties ci-dessous ; ne pas toucher `/home/user/integ-t06` ; refus de contrôle ou de classifieur : arrêt et rapport tel quel ; heures par `date -u`.

## Pièces

- Révision 3 : `brouillons/T0.6-organismes-v0-v1-candidat12-r3.md` (`c24e268e…`) et son journal (`0728c7ed…`).
- Contre-lecture 3 : `prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r3-cl3.md` (`3930d4f9…`) et couples Y1 à Y12 (`…-cl3-couples-v1.json`, `e3846ae5…`).
- Voie B : `registres/decisions.md` R-2062 et R-2064 ; rapports `docs/notes/g0-deux-semaines-v1/integration-t06-v13-main-v1/rapport-integration-v1.md` (`427def65…`) et `rapport-essai-blanc-S-voie-b-v1.md` (`4f4eb27d…`, § 3.3 : forme exacte des huit lignes citées).
- Audit DT-4 : `docs/notes/g0-deux-semaines-v1/e3-ter-v1/audit-ecart-dt4-7a-v1.md` (`4882fe4d…`) ; R-2048, R-2057.
- Configuration des six champs : R-2056. Plafond : R-2053 (garder 200 USD ; seuil d'alerte à mettre dans l'ordre de 7b, pas dans ce texte sauf renvoi).
- Lanceur et amorce au commit `1609a4bf` (`scripts/lancer_t06_v13.sh`, `scripts/amorce_instance_t06_v11.sh`, `src/controle_ia/t06/configuration_v6.py` pour l'empreinte canonique).

## Travail

1. **Couples de la contre-lecture 3** : appliquer par script, dans l'ordre, Y3 à Y8 et Y10 à Y12 tels quels (chaque « ancien » présent exactement une fois au moment de son application, sinon arrêt sans écriture). **Ne pas appliquer Y1, Y2, Y9** (écrits pour la voie A) ; les remplacer par des couples neufs (W-B1, W-B2, …) qui décrivent la **voie B** : le commit de scellement S descend de `1609a4bf` sans rien changer au périmètre gelé (`CHEMINS_GELES` de `harnais/validation_reelle.py`), porte le texte scellé et la configuration de 7b, puis est **fusionné dans `main`** (le lanceur v13 exige « S ancêtre d'`origin/main` », l. 127 ; `commit_s`, l. 112) ; le commit cité reste `1609a4bf` (même arbre gelé que S : `exiger_code_cite` passe) ; « Tests attendus » 2 022 relevé sur l'arbre de `1609a4bf` par 7a et sur l'arbre de S′ à blanc (2 019 + 3 essais `pypandoc` absents de l'environnement processeur, présents sur l'instance) ; la vérité que Y1 et Y2 portaient (arbre gelé entier, compte valant pour l'arbre entier) est gardée.
2. **Grandeurs de coût de 7a (R-2057 réserve 1 ; M1 de la contre-lecture 3)** : appliquer l'option **(b)**, défaut et recommandation en attente du mot de Lazar : les retirer du texte (sections « Ce que les auteurs savaient », « Puissance », devis) et appuyer la puissance de 7b sur les heures de la lecture A et sur le plan de puissance d'avant 7a (script et sortie de puissance v3 cités par la r3) ; à la place de Y3, un couple neuf qui déclare : grandeurs reçues de la session mère sortante, origine non établie (R-2057), retirées. Écrire en plus, à part, un fichier de couples **variante (a)** (garder les grandeurs avec le statut de Y3), pour le cas où Lazar choisirait (a).
3. **Section « Ce que les auteurs savaient »** : ajouter les constats de l'audit DT-4 qui touchent ce texte (aucune trace ; l'extracteur `extraire_mesures_epreuve_t06_v1.py` ouvre le fichier des sondes ; lecture A commitée après l'exposition de son lecteur) ; ce que le rédacteur de la r4 a lu.
4. **Marqueurs** à remplir maintenant (une valeur chacun, toutes ses occurrences) : `COMMIT_CODE_T06` = `1609a4bf2c1572f72bb8542d81d963ac6a8481c4` ; `EMPREINTES_CODE_T06` et `EMPREINTE_AMORCE_T06` = empreintes recalculées au commit `1609a4bf` (vérifier contre le point 15) ; `CHEMIN_CONFIG_T06` = `prereg/T0.6-organismes-config-7b-v1.json` ; `EMPREINTE_CONFIG_T06` = l'empreinte **canonique** de cette configuration (copie octet pour octet de `b7a5c1ba…`), recalculée par le code de `configuration_v6` (attendu `ca8003f9…`, R-2064) ; `EMPREINTE_RELU_CL3_T06` = `c24e268ee9821d1f37ff612023a9f07735864614f57e3a9cf58517b05bc55331` ; `CHEMIN_RAPPORT_CL3_T06` = `prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r3-cl3.md` ; `EMPREINTE_RAPPORT_CL3_T06` = `3930d4f9306395694c7dd541395c28aa9ad478db3909b529b76630d8e4766f46`. **Laisser** `MOT_LAZAR_GO_7B` (mot de Lazar attendu) et `DECISION_LAZAR_ECART_DT4_R2041` (rempli par la mère avec R-2048, l'audit et son complément, à venir).
5. Section « Contre-lecture » : entrée de la contre-lecture 3 (faite ; Y appliqués et non appliqués, avec raison) ; entrée « Contre-lecture 4 (R2) — différentiel r3 → r4 » à faire par un autre modèle que toi.
6. Vérifier : `controle_ia.prereg.problemes` ne signale que les deux marqueurs laissés (essai à valeurs factices pour ces deux-là : liste vide) ; les huit lignes citées par `controles` sont chacune sur une ligne, sous la forme du § 3.3 du rapport d'essai à blanc ; l'amorce est citée sous la forme exigée (l. 140 du lanceur).

## Sorties

- `brouillons/T0.6-organismes-v0-v1-candidat12-r4.md`, journal `brouillons/T0.6-organismes-v0-v1-candidat12-r4-journal-v1.md` (chaque couple : lieu, raison, avant, après), couples `brouillons/T0.6-organismes-v0-v1-candidat12-r4-couples-v1.json`, couples variante `…-r4-couples-variante-a-v1.json`, script d'application ; compagnons `.sha256`.
- Rien committé, rien scellé sous `prereg/`. Réponse courte à la mère : fichiers et empreintes, couples appliqués, marqueurs restants, points ouverts.
