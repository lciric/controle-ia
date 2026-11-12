# Vérification par la session mère — rapport au directeur de thèse v1

- **Réexécution** de la commande unique de l'annexe, 7 novembre 2026, 19:02:37 → 19:09:55 (temps universel, `date -u`) : `/home/user/controle-ia-travail/.venv/bin/python -I recalcul-v1.py --depot /home/user/controle-ia-travail --depot-organisme /home/user/ideation-organism --sortie <bloc-notes>/rapport-recalcul-rejeu.json --tirages 2000 --permutations-refit 500 --permutations-refit-mots 200 --processus 4`, code de fin 0.
- **Comparaison** avec `recalcul-v1-sorties.json` livré : toutes les valeurs égales, sauf trois durées (`duree_s`, `r1_W/temps_s_5_plis`, `permutations_refit/temps_s`). Aucun nombre du rapport ne change.
- **Longueur** : `wc -w` compte 2 996 mots dans `rapport-directeur-v1.md` (limite 3 000 hors annexe).
- **Forme** : les seuls mots en capitales du corps (« PRIVATE NOTE », « COST ») sont des citations de la consigne et des actions du saboteur, pas des sigles ; aucune mention de `donnees/bras-attaque*` ni de `donnees/mode-tenu-a-l-ecart*`.
- **Consigne** du lecteur versée telle quelle : `consigne-rapport-directeur-v1.md` (`c45c06bd…`, citée par R-1702).
- **Non fait** : aucune contre-lecture par un lecteur neuf ; la réexécution vérifie le calcul, pas les choix d'analyse, que le lecteur déclare exploratoires.
