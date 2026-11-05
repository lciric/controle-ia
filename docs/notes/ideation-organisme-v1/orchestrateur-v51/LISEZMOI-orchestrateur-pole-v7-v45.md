# Orchestrateur du pôle, v7 — version 45 (correctif minimal)

**v45 n'est pas contre-lue.** Les fichiers d'entrée et la ligne de commande ne changent pas par rapport à la v44.

## Le bloquant (message n° 175 de session-depot, démontré sur la v44 sans dépense)
`anonymiser` (`pole/ideation.py`) normalisait la typographie **sur le texte JSON** d'une fiche servie : un guillemet
français « » ou anglais typographique “ ” dans une valeur devenait un `"` non échappé, d'où `JSONDecodeError`. Moment :
après toutes les passes des proposeurs, avant le premier juge : course arrêtée sans note ni classement, dépense des
proposeurs perdue. `--mesurer-consignes` avec des témoins à guillemets s'arrêtait aussi (code 2).

## La correction
Nouvelle fonction `normaliser_typographie_objet` : la même `normaliser_typographie` appliquée **valeur par valeur**
(chaînes de l'objet désérialisé, récursivement ; les clés ne changent pas), jamais sur le texte JSON. `anonymiser`
l'emploie. Les témoins ne changent pas. Seule différence de texte possible : une tabulation dans une valeur, autrefois
protégée par l'échappement JSON, est désormais ramenée à une espace comme le prévoit la règle (CL31-17).
Recherche faite (`grep`) : aucune autre fonction ne remplace du texte sur du JSON sérialisé (`caviardage` travaille
déjà valeur par valeur par `caviarder_objet` ; la lecture des témoins ne normalise rien).

## Les essais (classe `TestV45`, `essais/test_v7_ideation.py`)
1. Une fiche et des témoins à guillemets « » et “ ” : anonymisés sans erreur, chaque valeur normalisée comme avant,
   structure intacte, consigne relisible en JSON.
2. `--mesurer-consignes` avec des témoins à guillemets : code 0, aucun appel.
3. Course simulée complète (passe 1, passe 2, Argon proposeur à fiches à guillemets ; juges Claude ; puis bras
   rapporté différé) : code 0, témoins tenus, `classement.json` écrit à trois juges.

Chacun échoue sur la v44 (1 : `JSONDecodeError` ; 2 et 3 : code 2, « JSONDecodeError ») et passe sur la v45.
Suite complète : 415 essais (412 en v44), 0 échec, deux exécutions, aucun processus survivant.
