# Contre-lecture R2 de la fiche de réception v4 de R1 — v1

- Contre-lecteur neuf (sous-agent, Claude Opus 5.5), pour conv-audit. Consigne :
  `docs/notes/runs-r1-r2-r4-v1/consigne-contre-lecture-fiche-reception-r1-v4-v1.md` (compagnon vérifié conforme).
  Commencé le 5 novembre 2026 à 01:03 UTC, fini vers 01:15 UTC (`date -u`). Je n'ai écrit ni la fiche, ni le
  vérificateur, ni l'addendum, ni son code.
- Pièces lues (compagnons vérifiés conformes, onze sur onze, dans `reception-v4-v1/`) : fiche `50d5a895…`, rapport
  `3216034e…`, vérificateur `3ea2352d…`, essais `23b7241e…`, banc `5ff74a6e…` et ses sorties. Texte scellé lu par
  `git show 5bd62a00:prereg/R1-addendum-relance-v4.md` (`0f10881b…`, recalculé) : écarts, plan d'analyse (étape 4),
  critères gelés, liste d'arrêt. Code lu à `5bd62a00` : `scripts/r1_v4_instance_v2.sh`, `resolution_graine_lot_v3.py`,
  `rejeu_activations_v4.py` (et `methode_resolution` de la v3), `chaine_table_v4_v1.py`, `manifeste.py`,
  `alignement_v1.charger_identite`, `resolution_graine_v1.consigner_episode`, table v3 et configurations scellées.
  Registres `decisions.md` (R-1473, R-1482, R-1483, R-1502) et `depenses.md`, ordres de la fille v1 et v2. Fiche v3 au
  commit `cbad0b27` (grep ciblé).
- Rien lu de `calcul/r1-v4-reparation-reel-v1`, ni du contenu du témoin (les quatre empreintes recalculées par
  `git show 5bd62a00:<chemin> | sha256sum` seulement), rien sous `donnees/`, aucun score ni tableau. Aucun réseau,
  aucun modèle, aucune dépense, aucun commit, aucun `.sha256`, aucun fichier existant modifié.

## Verdict

**Scellable après couples.** Neuf couples (`couples-fiche-reception-v1.json`, même dossier), tous sur le texte de la
fiche, aucun sur son bloc d'attendus ni sur le script : appliqués dans l'ordre sur une copie, chaque « ancien » est
unique au moment de son application et le bloc reste identique (le mode réel du script reste donc valable).
Deux majeurs (condition « après la destruction » omise ; étape E inexécutable telle qu'écrite), aucun bloquant.

## Points (gravité ; couple)

### Q1 — étape 4 du texte scellé
1. Attentes du manifeste du rejeu (`commande`, `preenregistrement`), du résultat (`verdict_fidelite`, `version_table`,
   `table_sha256`, `table_empreinte_citee`, `non_conformes`, `signales`, `addendum`), des trois `.npz`, des deux résultats
   (témoin, réparation) et du recalcul : toutes dans la fiche (4.4, 4.5, 3, 7) et dans le script ; **juste**.
2. « **Après la destruction** » (première condition de l'étape 4) : absente de la fiche. Le script de l'instance pousse
   après chaque étape (`pousser` dans `etape()`) puis les traces à la fin : une récupération avant la destruction peut
   prendre une branche incomplète. **Majeure ; couple 1.**
3. Ajouts au-delà de l'étape 4 (manifestes des trois runs, comptes 240/2400, règle B, cohérence avec la table, recalcul
   par comptes) : chacun vérifié contre le code à `5bd62a00` ; tous sont des invariants du code scellé (une course
   conforme les tient par construction : `creer_manifeste` refuse un arbre sale ; `episodes_non_resolus` ne porte que
   les signalés, dont la v3 n'a aucun `non_resolu` ; `trajectoires_identiques` = 129 + corrections revérifiées), donc
   ils ne changent aucun critère gelé et n'arrêtent qu'une chaîne cassée. Seule réserve : voir point 6. **Juste.**
4. Constantes recopiées (méthodes v1, v2, `CORRIGEES_V3`, `METHODES_RESOLUTION`, sérialisation de la table, règle des
   comptes de `construire_table_v4`, clés de la sortie de `--reception`, types des `.npz`, `str(chemin)` du témoin) :
   égales au code. Bloc de la fiche égal à `verifier … bloc` (rejoué). **Juste.**

### Q2 — les dix points du rapport
5. Point 1 (commits lancés) : **juste**. Les faits de lancement le confirment (ordres de la fille v1 et v2 : session 1
   `COMMIT=937f1317…`, session 2 `COMMIT=<commit du versement>` ; R-1483 : étape A au commit `5bd62a00`) ; le manifeste
   reste la preuve, un écart est un nœud (déjà écrit).
6. Point 4 (comparaisons muettes de couverture) : **contrôle d'intégrité, permis** — aucune valeur n'est affichée ni
   gardée hors mémoire, aucune décision ne dépend de la valeur (seulement de l'égalité entre pièces), l'issue ne dit rien
   de la couverture ; précédent : la fiche v3 comparait déjà `trajectoires_identiques` (151) et
   `corrections_verifiees_au_chargement` (22), valeurs alors fixes. Mais deux de ces grandeurs sont aussi des énoncés
   de P-R5 (« trajectoires identiques = 151 + retrouvées », « corrections = 22 + retrouvées »), dont la conséquence
   gelée est une réserve d'instrument ; la fiche doit dire qu'un arrêt `coherence-table` n'est pas cette issue mais un
   nœud, et que P-C et P-R5 proprement dits ne sont pas lus. Et la table v4 porte la lecture du témoin
   (`temoin.lecture`, `resolution_graine.lecture_temoin`) : la fiche dit « du témoin, sa lecture non lue » sans le
   noter. **Moyenne ; couple 5.**
7. Point 2 (commit du rejeu) : **juste** ; confirmé au script : `etape()` committe `git add -A runs diag prereg` après
   chaque étape, « chaine » n'écrit rien, `ajouter_donnees` ne trouve rien avant le rejeu, tout fichier non suivi laissé
   par les essais ferait refuser le manifeste de la réparation (arbre sale) : 184 chemins exactement.
8. Point 3 (contrôles avant poussée) : **juste dans son principe** (plus strict que la v3 et conforme à l'ordre de la
   consigne), **à compléter** pour une coupure (Q4). **Moyenne ; couple 4.**
9. Point 3, suite (étape E) : la « seule refspec » de `calcul/r1-r2-reel-v1` ne rapporte ni la branche source, que lit
   `garder_octets` (`arbre(depot, source)`), ni le commit lancé du rejeu, que lit `garder_commit_rejeu` (il n'est pas
   ancêtre du commit de versement) : rejoué ainsi, le vérificateur s'arrête en code 2 (`git` ou `commit-rejeu`). Défaut
   sans danger (arrêt, non acceptation à tort), mais E est inexécutable telle qu'écrite. **Majeure ; couple 2** ;
   identifiant de E rattaché à la branche : **mineure ; couple 3.**
10. Point 5 (types des `.npz`) : **juste** ; recoupés au code (`np.float16` pour les trois principaux, `int64`, `bool`,
    `ecart` en `float64`) ; `charger_identite` garde le type du fichier de P3 (`np.load` sans conversion) ; le parent
    (l. 157) donne `moyenne` (2400, 3, 4096) float16.
11. Point 6 (198 chemins, 89 consignés) : **juste** ; `consigner` est appelé une fois par cible et par lot, numéro
    continu `{k:03d}`, `fichier` = `episodes-reparation/NNN.json`.
12. Point 7 (recalcul) : **juste**, pièces de P3 présentes à leurs chemins ou sous `donnees/` ; mais `timeout 900` est
    une garde d'opérateur absente du texte scellé : un dépassement vaudrait « table non reçue ». **Mineure ; couple 6.**
13. Point 8 (courses arrêtées) : **juste** pour le nœud ; deux descriptions à corriger : un rejeu peut s'arrêter avant
    son manifeste (`charger_table` précède `creer_manifeste`) et un rejeu arrêté pendant l'écriture peut verser des
    `.npz` partiels (`ajouter_donnees`) — le script les admet déjà. **Mineure ; couples 7 et 8.**
14. Point 9 (ce que le script ne refait pas) : **juste**, mais écrit au rapport, non à la fiche (Q5). **Couple 9.**
15. Point 10 (robustesse) : **juste** ; ajout : `SyntaxError` (`ast.literal_eval`), `NotImplementedError` (`zipfile`),
    `IndexError` ou `AttributeError` hors des gardes sortent en trace Python, code 1 — sans valeur imprimée, mais hors
    des codes documentés ; la condition « code 0 » de C bloque déjà ; la fiche le dit. **Mineure ; couple 4** (pas de
    changement de script : il imposerait essais et banc rejoués).

### Q3 — sentinelles
16. Essais rejoués : `cd …/reception-v4-v1 && PYTHONPATH=…/src timeout 900 nice -n 10 …/.venv/bin/python -m pytest -q
    -p no:cacheprovider --basetemp=<scratchpad>/essais test_verifier_reception_r1_v4_v1.py` → **118 passed** (41,5 s) ;
    arbre du dépôt inchangé (`git status` vide). Seul ajout à la commande de la consigne : `--basetemp` dans mon
    dossier de travail.
17. Lecture du code : aucune valeur lue d'une pièce n'entre dans un message, sauf des noms de fichiers (`presence`,
    trois au plus) et des comptes de chemins (`versement`) ; `exiger` remplace toute exception par son message fixe ;
    le chemin `ARRÊT [lecture]` imprime `str(e)` de `KeyError` (clés constantes ou identifiants d'épisode),
    `JSONDecodeError` et `UnicodeDecodeError` (positions), `OSError` (chemins) ; `filtrer` écarte les clés interdites
    dès le chargement ; le motif d'arrêt imprimé est d'une liste fermée, vérifiée avant. **Aucun chemin ne peut
    imprimer une valeur interdite** (P-R5, lectures, traces) ; les sentinelles des essais (cas sain et artefacts, `test_verifier_reception_r1_v4_v1.py` l. 373-374) le confirment.

### Q4 — coupure de la session de pilotage
18. Coupure entre B et C, ou entre C et D : le commit local, s'il survit, pourrait être poussé à la reprise sans C ;
    E rattraperait l'écart avant toute lecture, mais le versement serait fait (irréversible, sans réécriture) avant ses
    contrôles. Poussée refusée (tête déplacée) : rien n'interdit un rebasage, dont le commit n'a pas été contrôlé.
    Coupure après D sans message : E n'a pas d'identifiant. **Sûr pour la lecture (E puis F), non sûr pour l'ordre ;
    moyenne ; couple 4.**

### Q5 — non-vérifié écrit d'avance
19. Partiellement (4.5 : valeurs d'identité ; 6 : non lu). Manquent dans la fiche : `jetons_empan` égal aux
    `jetons_notes` de P3 (parent), activations finies, corrections revérifiées (par le rejeu et le recalcul seulement),
    tokeniseur employé au recalcul, déclaration d'une reprise V4-E16, destruction de l'instance.
    **Moyenne ; couple 9.**

## Après les couples

Les couples changent l'empreinte de la fiche, non son bloc : rejouer les essais (le cas `test_bloc_de_la_fiche_reelle_egal_au_script` lit la fiche
réelle) avant le scellement, puis citer l'empreinte nouvelle (`--fiche-sha256`). Aucune contre-lecture de plus n'est
nécessaire si les couples sont appliqués tels quels.
