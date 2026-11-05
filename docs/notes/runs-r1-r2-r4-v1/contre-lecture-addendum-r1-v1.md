# Contre-lecture de l'addendum de relance de R1 — v1

- Contre-lecteur neuf (règle R2), Opus 5.5, auteur d'aucune pièce ; 2 novembre 2026 (UTC). Rien de payant, aucune instance.
- Brouillon relu : `prereg/R1-addendum-relance-v1.md`, brouillon 1, `ab947556…`, au commit `96c5e036` (arbre de travail temporaire). Empreintes citées recalculées : toutes justes (parent, configuration v3, table, enquête, `arret.json`, n° 339). Arbre gelé identique entre `5b72e2e2` et `96c5e036`.

**Verdict : scellable après corrections** (aucun point bloquant ; cinq majeurs).

Sur le fond, la règle A est saine. L'arbitre est l'égalité d'une empreinte sha256 qui couvre toute la transcription en identifiants. Une correction acceptée redonne donc les identifiants de P3 au bit près, et aucune trajectoire ne peut être « fabriquée ». L'ordre fixe ne fait que borner la recherche. La règle B (`fidele`, `contexte_conforme` et `trajectoire_identique` à faux, `conforme_longueur` à vrai) est conforme au code, au test et au n° 339. Le verdict « non conforme » au-delà du seuil est compatible avec l'analyse de conv-audit : R1 y est nul, au motif `rejeu_non_conforme`. Les formats et les noms sont inchangés, à la clé `tokenisation` près, qui ne fait qu'ajouter des champs. Coût cohérent.

## Bloquants

Aucun.

## Majeurs

**CLA-01 — Écarts au parent non consolidés, et « Ce qui ne change pas » contredit.** Citation : « Cet addendum remplace **une seule règle** du préenregistrement parent » ; et, sous « Ce qui ne change pas » : « liste d'arrêt du parent hors CLC-03 ». En réalité, l'addendum change aussi les points suivants :
- P-R5 ;
- une ligne de lecture remplacée, deux ajoutées, dont la réserve P-R5 ;
- des arrêts ajoutés : empreinte du parent, citations de l'addendum, `ETAPES` ;
- le plafond de l'amorce, 150 → 100 minutes (une ligne d'arrêt du parent) ;
- les tests attendus, 291 → 299 ;
- la configuration, v2 → v3 ;
- le module et le script, v1 → v2, donc la commande inscrite au manifeste ;
- le sens de `contexte_conforme`, faux pour 7 épisodes pourtant entièrement conformes en longueur ;
- la couverture sous la règle de repli : le parent dit « au plus 74 % », c'est désormais 1 440 / 2 400 = 60 %.

Correction : une section « Écarts au parent », exhaustive, sous forme de table (ligne du parent, nouvelle règle, raison), que le lecteur de concordance de conv-audit pourra suivre ligne à ligne ; corriger « une seule règle » et « Ce qui ne change pas ».

**CLA-02 — Le repli après l'échéance est faux.** Citation : « une relance plus tardive exige une ligne d'extension de Lazar dans `registres/go.md` ». Or la garde (`.claude/hooks/garde_calcul.py`, R-389) refuse toute extension à échéance plus lointaine : la validité reste celle de la première ligne. Correction : « une relance après le 2 novembre exige un GO nouveau, sous un identifiant nouveau ». Écrire aussi le calendrier : nœud de Lazar, contre-lecture traitée, scellement, concordance chez conv-audit et lancement, tout le 2 novembre (date du jour selon le conteneur).

**CLA-03 — La concordance chez conv-audit n'est pas une condition du lancement.** Le n° 339 dit : « un lecteur neuf vérifiera sa concordance avec notre principale avant tout départ ». L'addendum ne la place qu'après la contre-lecture (« Puis vérification de concordance… »), et ne la rattache à la lecture qu'au paragraphe R2. Correction : l'inscrire dans le plan, étape 1, et dans la liste d'arrêt (« pas de lancement sans le rapport de concordance, chemin et empreinte »).

**CLA-04 — Gardes (R5) : il manque des cas sains et des artefacts.**
1. Le chemin réel de l'amorce, avec un addendum scellé, n'a jamais tourné sur un cas sain. L'essai sain passe en mode jouet sans préenregistrement (aucune ligne « addendum lu » dans `amorce-sain.log`).
2. L'artefact « addendum non scellé » est en fait un addendum *absent* : le commit d'essai `e23eb49a`, tiré de `7f0396f6`, précède l'addendum.
3. Les gardes Python sur le parent (empreinte différente ; addendum qui ne cite pas l'empreinte du parent) n'ont aucun test : `chemin_prereg_parent` vaut `None` partout dans `tests/test_runs_nuit_v2.py`.
4. Le chemin « paires » n'est jamais passé par `executer`, ni sous la consigne fausse du contrôle négatif. Les 20 actions de l'échantillon de fidélité peuvent pourtant tomber dans les 14 épisodes corrigés par une ou deux paires.

Correction :
- tests (sain, puis artefact) des deux gardes du parent ;
- un artefact « addendum présent sans sceau » ;
- un essai sur processeur, sans modèle, au commit de scellement : `lire_unique` et vérification des sceaux des quatre fichiers, puis gardes de citation de `executer` jusqu'au manifeste ;
- `appliquer_entree` sous consigne fausse sur les 15 épisodes réels corrigés, avec contrôle de l'empreinte de P3 sous la vraie consigne.

**CLA-05 — P-R5 : formulation et concordance.** Citation : « au moins 90 % des actions notées fidèles (critère du parent et de l'analyse de conv-audit, n° 339) ». Ce n'est pas un critère. Le parent en fait une prédiction, et l'analyse scellée de conv-audit la note « observé à côté du prédit, sans verdict propre ». La déclarer incertaine (confiance ≈ 0,3) est honnête, et l'écart ne demande pas de nœud à part : il relève du nœud de l'addendum. Mais la ligne « Réserve d'instrument » est un *ajout* au tableau du parent.

Correction :
- dire « prédiction » ;
- déclarer la ligne comme ajoutée (CLA-01), avec « réserve rapportée, sans changer aucune classe de verdict » pour rester en concordance ;
- donner les marges avant la règle des 80 % : honnête 538 − 480 = 58 actions, saboteur 546 − 480 = 66 ;
- donner la couverture par condition sous la règle de repli.

## Mineurs

**CLA-06 — Seuil de 10.** Il a été fixé en connaissant le compte (7). Avec cette table, il ne peut jamais se déclencher : la couverture exacte impose 7. La seconde condition de l'enquête (« ouverture ou consigne différente au premier jeton ») est abandonnée sans le dire. Correction : écrire les deux faits.

**CLA-07 — Définition de « notée ».** Citation : « (« notée » = `jetons_notes` > 0) ». Le code calcule P-R5 sur `isfinite(ecart)` ; conv-audit dit « tous les scores de P3 finis ». Les trois définitions donnent ici 2 400 (vérifié sur la finitude seule). Correction : citer la définition du code.

**CLA-08 — « Borne basse 1 712 / 2 400 ».** Ce n'est pas une borne : la tolérance peut aussi écarter des actions en contexte exact. Correction : « scénario bas ».

**CLA-09 — Sensibilité « contexte exact ».** Environ 272 actions en contexte exact (1 712 − 1 440) viennent d'épisodes non identiques, où l'empreinte ne vérifie pas le préfixe. Or 22 sur 151 des épisodes entièrement conformes cachaient un découpage invisible. Correction : réserve déclarée pour l'analyse de sensibilité de conv-audit.

**CLA-10 — Commande du manifeste.** Elle devient `…rejeu_activations_v2`. Le code « R2 seul » de conv-audit (`constantes_v3.COMMANDE_REJEU`, `entrees_v3.verifier_arret_r1`) refuserait la preuve d'un arrêt de la relance. Correction : le signaler à conv-audit (n° 339 : « si un nom… change, c'est un écart »).

**CLA-11 — Dépenses.** Citation : « R4 à relever ». Le registre de la branche de session porte ≈ 4,6 / 25 USD (R1-R2 ≈ 1,0 ; R4 ≈ 3,6). Correction : le citer ; déclarer la section « Coût » comme le « devis par run » qu'exige le GO.

**CLA-12 — Tokeniseur de la table.** L'instance ne compare pas `tokeniseur_sha256` de la table au tokeniseur chargé. L'échec serait sûr (« echec »), mais il coûterait la course. Correction : ajouter la garde, ou déclarer l'absence.
