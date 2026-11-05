# Contre-lecture R2 des fiches T0.5 « graines neuves » (lots A, B, C, D) — v1

Contre-lecteur neuf (sous-agent, aucune pièce du kit écrite), 1er novembre 2026, ≈ 21:05–21:40 UTC. Lu sur la branche `prep/t05-graines-neuves-v1`, tête `bc9fa2d5`, dans un worktree en lecture seule. Brouillons relus (empreintes) : A `879c9146c4f44432abc7254a0a3bb694d71aa8b9328510fa0868d1568352d366`, B `429b1bc2d0a7ce9fbbc2c3b610154a2c688c7a89683f029bc0562e1b704231db`, C `65877f03dfd91aa978ad29d72c95cd6f78ab3de1c6846015be442f1492efe495`, D `6f1fe7fd87e1eb80e018d6c91c9e272b0d8ffbd2559f13f905ada3f7f0835757`.

**Verdict : scellable après corrections** (aucun bloquant ; trois majeurs, dont deux se règlent par une phrase dans les fiches).

## Vérifié et tenu

- Fidélité à la couche 1 bis : même commit cité `2660b07…`, arbre gelé identique (`git diff --quiet 2660b07 HEAD -- <chemins gelés>` → code 0), même configuration (`6979a00e…`, empreinte canonique citée `db3ad3ce…`), mêmes révisions, amorce `59f49aab…` et script d'instance `077424d0…` aux empreintes citées ; pilote `9ce91ba1…`, invites H3, H4, index, `juges.py`, `rubrique.py` aux empreintes du LISEZMOI. La configuration porte bien 3 épisodes, température 1,0, `variante_juge` b0, `episodes_decisifs` [0, 1], `episodes_notes_deux_fois` [0], `duree_max_s` 15 000.
- Tâches : contrôle indépendant. Évaluation (64) puis entraînement (32) ; les quatre lots couvrent 96 tâches disjointes ; chaque objet est identique à l'origine sauf `identifiant` + « -g2 » ; aucun « / » ; A+B = `taches-pilote-60-v1.json`, C+D = `taches-banque-36-v1.json` (`bc790c11…`, même ordre) ; table de 96 lignes conforme (lots, ordre, schéma) ; premiers et derniers identifiants conformes aux fiches et au LISEZMOI ; les 14 sceaux de `donnees/t05-graines-neuves-v1/` et tous les sceaux du kit tiennent.
- Graines (R9) : quatre entropies tirées par `numpy.random.SeedSequence()`, consignées dans `origines-…-v2.json`, deux à deux distinctes, distinctes du pilote (`37114…`), de la couche 1 bis (`303166…`) et de la revalidation (`120571…`) ; sorties en écriture exclusive (`open(…, "x")`), règle des lots fixée par le rang. L'identifiant n'entre dans aucune invite (seuls usages : clés, fiches, bilans).
- Gardes lues par le code : chaque expression (`Commit du code d'analyse`, `Configuration du pilote (empreinte canonique)`, `Tâches du pilote`, `Entropie`, `Tests attendus`, et le `sed` de `Chemin de la configuration` et `Chemin des tâches`) rend une valeur unique, la bonne, dans les quatre fiches. `BRANCHE=` apparaît trois fois (dont `…-v2`), mais le lanceur exige la paire exacte « `PREREG=…`, `BRANCHE=…-v1` » et l'instance reçoit `BRANCHE` par `--env` : sans ambiguïté. `problemes()` ne rend que la section « Contre-lecture ».
- Cohérence fiches, lanceur v2, LISEZMOI : branches, étiquettes, chemins `…-<lot>-<30|6>-v1.json`, GO_ID et empreintes des tâches concordent ; GO-2026-11-01-11 est au registre (calcul, Lazar, 45 USD, échéance 2026-11-02).
- Plafond de 15 000 s (question 4) : **acceptable tel quel, pas de lots plus petits.** La couche 1 bis, 36 tâches, a écrit les décisives des deux juges avant l'échéance (arrêt à 15 209,8 s pendant les descriptives du 8B, R-591) ; 30 tâches font les 5/6 de cette charge, donc `e0` et `e1`, seuls utiles à la banque de conv-audit, sont à l'abri ; seul `e2` est exposé. Quatre lots de 24 (taille du scénario « grand » du devis) finiraient probablement `e2`, mais il faudrait refaire dérivation, fiches et essais, et sortir du « (30, 30, 30, 6) » écrit dans la ligne du GO : non recommandé ce soir.
- Coût : borne dure plus serrée que celle des fiches. 1,40 USD/h × 6 h × 4 instances = 33,6 USD, sous 45 ; sans surveillance, l'amorce sort au plus à 300 min et le conteneur s'arrête.

## Majeurs

**CLG-01 — Garde de calcul sans effet en cas de refus (repli silencieux, R5).** Lanceur v2, lignes 73-74 : `| python3 "$DEPOT/.claude/hooks/garde_calcul.py" && echo "garde de calcul : $GO accepté" | tee -a "$T/lancement.txt"`. Un échec à gauche d'un `&&` ne déclenche ni `set -e` ni le piège `ERR`. Éprouvé : avec `set -euo pipefail` et `trap … ERR`, `printf x | python3 -c "import sys; sys.exit(2)" && echo accepté` laisse le script continuer (code final 0). Un GO refusé (faute de frappe, GO échu) mène donc à la création ; le hook de session ne voit pas `vastai create` dans `bash $L …`. Défaut hérité de la v4 (ligne 59), jamais éprouvé (« non rejouée »). La fiche, elle, promet « aucune création … si la garde de calcul refuse le GO ». **Correction** : lanceur v3 avec `… | python3 "$DEPOT/.claude/hooks/garde_calcul.py" || { echo "garde de calcul : $GO refusé"; exit 2; }`, puis un essai R5 sur un registre factice (GO absent, puis présent). Les fiches citent alors la v3. À défaut, ce soir : exiger dans l'essai à blanc de **chaque** lot la ligne « garde de calcul : GO-2026-11-01-11 accepté », et lancer avec le même texte de commande, copié tel quel.

**CLG-02 — Comptes de notations transmissibles au lecteur (R1).** Fiches, « Plan d'analyse » : « Les comptes du résumé que le journal affiche à la fin (épisodes, actions, notations complètes) servent à la seule santé de la chaîne : ni interprétés, ni rapportés comme résultat. » Le résumé imprimé contient aussi `controle_negatif` (sa lecture) et, par juge, `completes`. Il existe un précédent : R-596 a « signalé à conv-audit » des comptes de notes complètes du 3B. Or conv-audit écrit justement la lecture de ce lot (n° 327, R-999). **Correction**, une phrase par fiche : « ces comptes ne sont transmis ni à conv-audit ni à aucun lecteur, et ne sont recopiés dans aucun registre (codes, durées et poussées seulement) avant le scellement du préenregistrement de lecture ».

**CLG-03 — Instances des runs R1, R2, R4 (GO-2026-11-01-13) bloquantes cette nuit.** Liste d'arrêt : « si une instance autre que celles des trois autres lots de cette course (au plus trois, à leurs étiquettes exactes `t05-graines-neuves-<lot>-v1`) existe sur le compte ». Le kit R1/R2/R4 (`prep/runs-r1-r2-r4-v1`, `amorce_instance_r1_r2_v1.sh`) crée lui aussi des instances Vast.ai. Si l'une existe quand un lot part (cas prévu : « D … dès qu'une instance se libère »), ce lot ne peut plus partir. Le relâcher demanderait alors un écart à une fiche scellée, c'est-à-dire un nœud de décision. **Correction** : écrire dans le LISEZMOI et dans la liste d'arrêt que les quatre lots partent à la suite, avant toute instance de GO-13 ; ou bien élargir dès maintenant la règle (fiches et lanceur v3) aux étiquettes exactes des runs de GO-13.

## Mineurs

**CLG-04** — « les critères L1 à L4 et le seuil 3,0 sont introuvables à ce jour et doivent venir de conv-audit » (fiches, « Critères de lecture gelés » ; LISEZMOI, « Réserves »). Périmé : n° 327 (R-999) les situe (`demo_couche1_v7.py`, l. 12-17 et 120-137 ; seuil 20 sur la richesse, log 20 ≈ 3,0). Écrire « situés par conv-audit (n° 327, R-999), à geler dans le préenregistrement de lecture ».

**CLG-05** — « (« go », puis « lance tout », ≈ 20:20 UTC) ». L'erratum R-996 fixe ≈ 20:38 UTC. Corriger dans les quatre fiches, sans réécrire le GO (R12).

**CLG-06** — « au pire cas (devis, section 3 : 1,40 USD/h, descente des modèles, marge 1,5) ≈ 11 USD par instance de 30 tâches et ≈ 4 USD pour le lot D, soit ≈ 37 USD pour les quatre ». Le « 37 » de la section 3 du devis chiffre un autre plan : 2 instances × 2 courses de 24 tâches. Les 11 et 4 USD sont recalculés par la formule du devis, non cités. La ligne du GO dit « pire cas ≈ 44 ». Enfin, 11 USD à 1,40 USD/h font 7,9 h, ce qui ne cadre pas avec « au plus tard 6 h ». Écrire : « calculé par la formule du devis, section 3 ; borne dure 4 × 6 h × 1,40 = 33,6 USD ; la ligne du GO dit ≈ 44 ».

**CLG-07** — LISEZMOI : « dans le champ `prereg` de chaque manifeste ». Le champ s'appelle `preenregistrement` (`manifeste.py`, l. 104). La répétition jouet a lu la mauvaise clé (« décisif : True ; prereg : None ») : l'empreinte de fiche dans le manifeste n'a donc pas été vérifiée. Corriger le nom, et le dire à conv-audit (n° 327 demande les empreintes).

**CLG-08** — « commit de cette fiche sur la branche `prep/t05-graines-neuves-v1` (parent `1c6c900`) ». Le parent de `S` sera `bc9fa2d5` : écrire « descendant de `1c6c900` ». De même, « si le commit de tête … diffère du commit cité » : le lanceur compare la tête au commit `S` passé en argument, non au commit cité `2660b07`. Écrire « diffère du commit passé au lanceur ».

**CLG-09** — L'offre est filtrée sur `dph_total` seulement ; le coût de transfert entrant (≈ 22 Go de modèles par instance) n'est ni filtré ni consigné. Ajouter `inet_down_cost` à la ligne d'offre consignée (v3), ou le relever à l'essai à blanc.

**CLG-10** — La table `table-identifiants-graines-neuves-v1.json` ne cite aucun script ni aucune commande de production. Contrôlée ici indépendamment : conforme. Nommer sa provenance dans le LISEZMOI.

**CLG-11** — « (ii) aucune ligne de journal nouvelle pendant 60 min hors des étapes longues connues ». La chaîne du pilote n'imprime aucune ligne de progrès pendant les épisodes ni pendant les notations, ce qui laisse la règle sans prise de « run : … » à la fin. Le dire, et nommer les bornes effectives : délai externe 270 min, amorce 300 min, arrêt à 6 h.

**CLG-12** — Le LISEZMOI attend le rapport dans `prereg/contre-lectures/T0.5-graines-neuves-v1-cl1.md` ; la consigne reçue le place ici. Copier ce fichier à cet endroit avec son `.sha256` avant de remplir les sections « Contre-lecture ».

## Non vérifié

- Empreinte canonique de la configuration : non recalculée (`torch` absent ici) ; je m'en remets à `tests-v1.txt`.
- Lanceur contre le vrai Vast.ai (absent ici) : crédit, offres, instances présentes.
- Scripts d'instance, `juges.py`, `validation_reelle.py`, contre-lecture de la couche 1 bis : lus seulement là où ils touchent gardes et champs.
- Durées du pilote citées : non rouvertes. Suite de tests : non relancée. Lanceur v1 et dérivation v1 : sceaux seulement.
