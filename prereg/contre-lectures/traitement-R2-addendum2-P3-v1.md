# Traitement de la contre-lecture 1 de l'addendum 2 de P3 et décisions sur les questions ouvertes — v1

Session 14, 2026-10-20 (R-264). Brouillon relu : brouillon 1 (`2698af04…`) ; rapport de contre-lecture R2
(`ad360e02…`, « scellable après corrections ») ; corrections écrites dans le brouillon 2 (le brouillon 1 reste tel quel,
R12). La session n'a calculé aucune grandeur de B1 ni de B2.

## Constats de la contre-lecture (RB-01 à RB-13)

| constat | décision | où dans le brouillon 2 |
|---|---|---|
| RB-01 (majeur) : réserve due omise, mention traitée autrement que le témoin | accepté : `reserve_B2_mention_hors_formes` vise aussi `P3-P1` (même règle gelée pour le témoin et la mention, [P] l. 156, 282-283, 434-435) ; lecture au verdict écrite | Seuil (table des réserves) ; Critères |
| RB-02 (majeur) : cas « ampleur non résolue » non écrit | accepté : `reserve_B1_ampleur_non_resolue` (borne basse décisive > log10 3, borne basse de `E_sf` dans ]0 ; log10 3], borne basse de `D` ≤ 0) ; table complète des cas de B1 | Seuil ; Critères ; Prédiction |
| RB-03 (majeur) : clé `etablie` prêtée à P3-P2 et à la mention | accepté : clés lues écrites entrée par entrée (`etablie` pour P3-P1 seulement ; `conforme` et `etabli` des contrastes seulement quand la table du verrou les consulte) ; test de la garde 9 sur une lecture produite par le code gelé | Métrique (Entrées) ; tests |
| RB-04 : B3 déjà calculé au brainstorm, non cité ; phrase de lecture trop forte | accepté : objecteur 2 cité avec chemin et empreinte ; B3 dit non aveugle ; « n'exclut pas une aire inférieure à `A_80(p)` » | Statut ; Critères ; Limites 6 |
| RB-05 : restriction et comptes | accepté : NaN ; comptes propres des retirées (toutes, lisibles, nulles) et des illisibles d'origine | M3 |
| RB-06 : part `D / E0` | accepté : part descriptive, aucun contrôle n'en dépend, mention « instable » si `E0` proche de 0 ; déclencheur 3 « non calculé » si `E0` = 0 ; garde 15 réécrite | M5 ; audit de symétrie ; garde 15 |
| RB-07 : libellés pour un effet négatif | accepté : libellés signés (« élèvent » / « abaissent ») ; « dont la borne basse est dans ]0 ; log10 3] » | M5 ; Seuil |
| RB-08 : lecture causale non mesurée | accepté : « la cause n'est pas mesurée (unité, échelle des propositions, gonflement) » | Critères |
| RB-09 : unité de contrôle | accepté : « un contrôle par règle de réserve et par cible » ; neuf contrôles au plus | Seuil ; Plan 8 |
| RB-10 : garde 5 et tests de la garde 4 | accepté : chaîne exacte de la commande ; condition parenthésée ; test « commit du manifeste ≠ tête » | Liste d'arrêt 5 ; tests |
| RB-11 : descriptifs voisins dans [A] | accepté : dit en une phrase (non lus) | Statut |
| RB-12 : phrase mêlée sur l'aire au seuil | accepté : deux valeurs, chacune avec sa définition | Prédiction |
| RB-13 : B3 répond à N-025 (3) | accepté : dit | Hypothèse (B3) |

## Questions ouvertes du rédacteur (notes de rédaction du brouillon 1) : décisions de la session

| question | décision |
|---|---|
| 1. Cible de la réserve de la mention | P3-P1 aussi (RB-01), en plus de `T3/<p>`. |
| 2. `ampleur_au_dela_de_la_consigne` : réserve ou descriptif | réserve nommée (elle répond à la remarque 1 ; une réserve ne fait que rétrograder) ; complétée par `ampleur_non_resolue` (RB-02). |
| 3. Unité écrite dans le champ du coût | limite écrite ; aucune mesure nouvelle (elle demanderait de décoder les textes, hors de N-025). |
| 4. Grandeur de B3 | `A_80(p) = Q + w (1 + z80 / z)`, comparée à la même formule aux hypothèses écrites les plus défavorables (≈ 0,5809) ; jamais au nombre arrondi du texte. |
| 5. Valeurs attendues de B3 dans le texte scellé | gardées (transparence), avec le précédent du brainstorm (RB-04). |
| 6. Médiane par tâche | réserve gardée (`mediane_par_tache`). |
| 7. Partage action et tâche | confirmé : restriction des actions (analyse principale) ; tâches sans forme (descriptif). |
| 8. Audit de symétrie | deux déclencheurs suffisent ; pas de retrait aléatoire apparié (il ajouterait une grandeur sans règle de lecture). |
| 9. Écriture du module | un rédacteur neuf écrit le module et ses tests, en n'important que le code gelé (aucune fonction du module du premier addendum) ; contre-lecture du code par deux sous-agents neufs (texte face au code ; mutants). |
| 10. Noms | confirmés : `prereg/P3-addendum2-audit-verdict-v1.md`, `docs/procedures/P3-addendum2-v1/audit_verdict_p3_v1.py` et `test_audit_verdict_p3_v1.py`, run `AAAAMMJJ-HHMMSS-addendum2-p3`, sortie `lecture-addendum2-p3.json`, 47 clés `addendum2/…`. |
| 11. Forme du verdict complété | nouvelle version `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` (R12), par des sous-agents neufs, qui cite les réserves des deux addenda ; la v1 reste telle quelle. |
| 12. Antériorité contre N-025 | confirmée (`ec1d71b0…`) ; entrées nommées en dur confirmées. |
| 13. Réserve générale « largement non lu » | omise : peu d'entrées ; chaque contrôle « non lu » porte déjà sa réserve. |
| 14. Bornes de P3-P3 refaites en descriptif | non : ce serait une seconde lecture de P3, et la version de numpy diffère. |
