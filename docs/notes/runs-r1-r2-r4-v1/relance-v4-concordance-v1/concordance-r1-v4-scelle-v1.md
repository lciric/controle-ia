# Concordance de l'addendum v4 de R1, version scellée — v1

Lecteur neuf de concordance (sous-agent, Opus 5.5), auteur d'aucune pièce ; 4 novembre 2026, 08:18 à 08:26 UTC (`date -u`).
Consigne : `docs/notes/runs-r1-r2-r4-v1/consigne-concordance-r1-v4-scelle-v1.md` (compagnon `.sha256` vérifié : OK).
Arbre lu : `/home/claude/wt/r1-v4`, branche `prep/r1-relance-v4`, tête `937f13177892933955c9c34839b4b45a4db745df`, `git status` vide avant et après.

**Verdict : concordant.**

## Pièces
- Sceaux vérifiés depuis leur dossier : texte scellé `0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8` OK ; brouillon 3 `f24e416f49ac723a44687b71804be1f478dba588c6a077c9b9480cc926ea3046` OK ; couples `3cddb305971dc822db5cb4a5931ecd6b19995e7202d26111d8acb67a55995742` OK ; contre-lecture du delta `ef0604abe5f0353a81224ae20c1f49a7b1d7587df427cce0b84690cac908ac89` OK.

## 1. Concordance exacte
- Les 19 couples appliqués dans l'ordre au brouillon 3 par script : chaque « ancien » présent exactement une fois au moment de son application (19 sur 19), aucun « nouveau » présent avant.
- Diff résiduel entre le résultat et le texte scellé : cinq blocs, tous des ajouts du scellement, rien d'autre.
- (a) Titre, ligne 1 : « — v4, brouillon 3 » devient « — v4 ». Forme ; pas de fond.
- (b) Statut de l'en-tête, lignes 44 à 46 : « Brouillon 3 (texte, non scellé…) ; restent la contre-lecture neuve (R2), son traitement, le scellement…, la concordance » devient « Texte scellé (brouillon 3, `f24e416f…`, plus les 19 couples…, marqueur du commit rempli…) ; reste la concordance d'un lecteur neuf ». Statut ; pas de fond.
- (c) Marqueur du commit, lignes 61 à 63 : « `À REMPLIR` » devient « `af1f2f4f3ab5340586dcda19c0327d0c5beeefca` », plus la phrase « entre ce commit et le commit de scellement, seuls changent des textes : brouillon 3, son rapport, ce texte et son sceau ». Rempli et vrai (point 2) ; pas de fond.
- (d) Section « Contre-lecture », lignes 392 à 406 : le « À faire (R2) » devient le compte rendu des deux contre-lectures (`e224ae8a…`, 15 couples ; `ef0604ab…`, 19 couples, verdict « scellable après couples ») et la réserve C32 (correction non retenue, raison, risque déclaré). Compte rendu et réserve déclarée ; aucune hypothèse, prédiction, seuil, critère, garde ni dépense ne change (la commande `--tests 381` qu'elle cite était déjà aux lignes 369 et 370 du brouillon 3 après couples). Pas de fond.
- (e) Pied « Scellement », lignes 411 à 418 : heure, composition (brouillon 3 + 19 couples + marqueur + section), aucun code ni configuration changé depuis `af1f2f4f`, empreintes revérifiées. Pas de fond ; ses affirmations sont vraies (point 2).
- Aucun autre écart : hors de ces cinq blocs, le texte scellé est identique à l'octet près au brouillon 3 après couples.

## 2. Code inchangé et empreintes
- `git diff --stat af1f2f4f 937f1317` : six fichiers, tous ajoutés, tous des textes : `docs/notes/runs-r1-r2-r4-v1/relance-v4/rapport-redaction-brouillon3-v1.md` et son sceau, `prereg/R1-addendum-relance-v4-brouillon3.md` et son sceau, `prereg/R1-addendum-relance-v4.md` et son sceau ; aucun code, essai, script ni configuration.
- `af1f2f4f` est sur la branche, descendant de `04bc323a` (vérifié).
- 50 empreintes complètes distinctes dans le texte scellé ; 37 retrouvées à l'octet dans l'arbre au commit `937f1317` et à `af1f2f4f` (dont les 26 fichiers de code de l'en-tête, les deux configurations, la table v3, le parent, le devis v2, le rapport des ajouts, le brouillon 2, l'addendum v3, et les sorties du pré-vol, du banc v2, de la répétition jouet, des épreuves et des essais).
- Hors de la branche, au commit ou à la branche cités : rapport de la fille `ae72aeaa…` = fichier au commit `97fb0681` (branche `origin/canal/fille-2026-11-04`) ; complément `049f20ba…` = `prereg/R1-addendum-relance-v2-complement-validation-v1.md` au commit `4b47db7b` ; configuration du complément `1b6f943c…` = fichier au commit `4b47db7b` ; diagnostic `1c2dd25f…`, rapport du lecteur neuf `371fe443…`, analyse par épisode `26a3ff72…` = fichiers de `canal/conv-audit-n04` ; contre-lecture du delta `ef0604ab…` et couples `3cddb305…` = fichiers de `origin/main` (la branche `main` locale ne les porte pas encore ; `origin/main` les porte, comme dit le texte).
- Empreintes canoniques recalculées par le code du commit : réparation v2 `c34bf464…` (`resolution_graine_lot_v3.empreinte_config`), réparation v1 `a5a61077…`, rejeu v6 `a3ef1bac…` (`rejeu_activations_v4.empreinte_config`) : égales.
- Différences de configuration annoncées vérifiées : v1 → v2 de la réparation, une ligne (`voie_si_temoin_non_exact`) ; rejeu v5 → v6, deux lignes (chemin de la table et `construite-en-session`).
- Limite : `tokenizer.json` `79e3e522…` n'est pas sur cette machine ; il égale la constante `TOKENIZER_JSON_SHA256` de `tests/test_resolution_graine_v1.py` et la ligne du rapport de la fille ; non revérifié sur le fichier.
- Limite : le script et la sortie du diagnostic ne sont cités qu'en préfixe (`b6a39191…`, `f3e0f42d…`) ; non revérifiés.

## 3. Champs lus par `scripts/r1_v4_instance_v2.sh` (`lire_unique`)
- « Tests attendus : `381` » : une ligne, valeur `381`.
- « Chemin de la configuration de la réparation : `prereg/R1-reparation-v4-config-v2.json` » : une ligne.
- « Chemin de la configuration du rejeu : `prereg/R1-rejeu-config-v6.json` » : une ligne.
- « Chemin de la table de tokenisation v3 : `prereg/R1-table-tokenisation-v3.json` » : une ligne.
- « Chemin du préenregistrement parent : `prereg/R1-R2-rejeu-p3-v1.md` » : une ligne ; chaque libellé n'apparaît qu'une fois dans tout le texte.
- Mode jouet rejoué sans réseau ni dépense (dépôt nu local en `file://` dans le bloc-notes, `VENV_EXISTANT`, jetons factices, `HF_HUB_OFFLINE=1`, `TESTS_CIBLES=tests/test_garde_depense_v4_v1.py`, texte scellé lu, et non `PREREG_ABSENT=1` comme dans la répétition de la rédaction) : session `temoin` au commit `937f1317` : « addendum lu : 381 tests attendus ; réparation prereg/R1-reparation-v4-config-v2.json ; rejeu prereg/R1-rejeu-config-v6.json » ; cinq sceaux OK ; branche poussée ; puis arrêt voulu aux tests (« 7 passed » ≠ « 381 passed »), avant toute étape de calcul, code 1.
- Session `reparation`, même commit, `TEMOIN_RUN` factice : la vérification des configurations passe (table v4 absente du commit, `construite-en-session`), puis arrêt attendu « résultat du témoin … absent au commit », code 2.
- La répétition complète (témoin, réparation, rejeu jouets) n'a pas été rejouée : elle demande des configurations jouets au lieu du texte scellé ; elle est hors de cette question.

## 4. Réserve C32
- Défaut confirmé : `verifier_surveillance(…, tests_attendus=358)` et `surveiller --tests` par défaut 358 dans `src/controle_ia/runs_nuit/garde_depense_v4_v1.py` ; la ligne « tests : 381 passed… » donnerait « detruire » sans `--tests 381`.
- « Les prompts des tâches planifiées ne portent aucun compte » : vrai. `prompt_tache` n'écrit que l'en-tête (seuils 45 et 57 USD, destruction par l'identifiant) et les champs `identifiant`, `T0`, `prix_horaire`, `disque`, `deja_imputees`, `heure_destruction` ; la ligne de localisation de l'ordre de la fille n'ajoute qu'un commit et un `git fetch`.
- « Seule la session de pilotage appelle `surveiller` » : vrai dans le code et les ordres. Aucun script (`scripts/`) ni module n'appelle `verifier_surveillance` (seuls les essais le font) ; `decision_horaire` et `decision_destruction`, ce que les tâches appliquent, ne l'appellent pas ; l'ordre `docs/procedures/ordre-fille-r1-v4-lancement-v1.md` (B3, C3) fait appeler `surveiller --session … --tests 381` par la session de pilotage, avec la mention « `--tests 381` obligatoire ».
- Nuance, sans effet sur le verdict : l'en-tête du prompt des tâches renvoie au module (« Règles : `python -m controle_ia.runs_nuit.garde_depense_v4_v1` »), dont la docstring décrit aussi la surveillance ; une session de tâche qui l'appliquerait de son propre chef avec le défaut détruirait une instance saine. Le risque reste du type déclaré (destruction d'une instance saine, jamais un résultat faux).
- Nuance : le texte scellé nomme session-depot comme session de pilotage (« Coût et GO ») ; l'ordre délègue le pilotage à une fille ; l'affirmation C32 tient dans les deux cas (une session de pilotage, non une tâche planifiée).
- Décision R-1473 présente dans `registres/decisions.md` de `origin/main` et de `canal/conv-audit-n04`, conforme au texte.

## 5. Conditions de `GO-2026-11-03-03`
- Ligne du GO identique dans `registres/go.md` de l'arbre de travail et de `origin/main` : calcul, plafond 60 USD, échéance 2026-11-17.
- Plafond : texte « plafond 60 USD » ; destruction à 57 USD projetés, alerte à 45 ; tâche (ii) à `T0 + H` sur 57 USD moins l'imputé ; pire cas borné ≈ 57,2 USD < 60 USD. Respecté.
- Échéance : « `GO_ID=GO-2026-11-03-03` valide le jour même (pas après le 17 novembre sans GO nouveau) » (Liste d'arrêt). Respectée.
- Écart déclaré à l'addendum v3, l. 234 et 235 : V4-E1, « Écart accordé par Lazar », la relance répare la donnée, non la règle. Respecté.
- Sorties scellées avant lecture : témoin « Sortie scellée, poussée » ; table v4 « écrite et scellée » ; garde de chaîne « sinon arrêt avant le rejeu, rien n'est lu » ; récupération seulement après la fiche de réception v4 scellée (V4-E13, étape 4) ; lecture aveugle des journaux. Respecté.
- Autres conditions du GO portées par le texte : contre-lu et scellé, concordance, commande exacte de conv-audit avant tout lancement (Liste d'arrêt, « lancement ») ; analyses inchangées (seuils, critères et analyses scellés ne changent pas, seule l'entrée change) ; devis hors de la fourchette 5 à 12 USD si le témoin est non exact (≈ 18 au milieu), dit au texte, sous le plafond.

## Bornes de cette lecture
- Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien lu ni écrit sous `donnees/` ni `/home/claude/coffre-*` ; aucun réseau, aucun modèle, aucune dépense ; aucun score ni tableau d'activations lu ; dépôt nu du rejeu jouet supprimé du bloc-notes après usage.
