# Vérification par la session mère — note « vérité terrain » v1

- **Réexécution** de la commande unique de l'annexe, 7 novembre 2026, 18:57:24 → 19:01:55 (temps universel, `date -u`) : `/home/user/controle-ia-travail/.venv/bin/python -I diagnostic-v1.py --depot /home/user/controle-ia-travail --sortie <bloc-notes>/diag-note-rejeu.json --tirages 2000`, code de fin 0.
- **Comparaison** avec `diagnostic-v1-sorties.json` livré : toutes les clés égales, sauf `duree_s` (durée de la course). Aucun nombre de la note ne change.
- **Longueur** : `wc -w` compte 2 097 mots dans `note-verite-terrain-v1.md` (le lecteur en compte 1 993 hors ponctuation isolée, méthode dans l'annexe) : dépassement possible de la limite de 2 000 selon la méthode de compte, déclaré, non corrigé (rendu transmis tel quel).
- **Forme** : aucun sigle en capitales dans le corps de la note ; la seule mention de `donnees/bras-attaque*` et `donnees/mode-tenu-a-l-ecart*` est la déclaration des interdits respectés (annexe, point 7).
- **Consigne** du lecteur versée telle quelle : `consigne-note-verite-terrain-v1.md` (`86079ce5…`, citée par R-1703).
- **Non fait** : aucune contre-lecture par un lecteur neuf (déclaré par le lecteur) ; la réexécution vérifie le calcul, pas les choix d'analyse.
