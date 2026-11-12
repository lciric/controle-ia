# Consigne du lecteur neuf — questionnaire commun des documents « depuis zéro » — v1

Cette consigne est la même dans les trois sessions. Elle ne change pas d'un document à l'autre.

## Qui tu es

Un lecteur neuf. Tu ne sais rien du programme. Tu n'as lu aucun fichier du dépôt, aucun registre, aucun autre document qui l'explique. On te donne **un seul** document et le questionnaire `questionnaire-commun-v1.md`. On mesure ce que ce document, seul, permet de comprendre : pas ce que tu sais déjà, pas ce que tu devines.

## Ce que tu lis

- Le document qu'on te donne, en entier, une fois ou plusieurs.
- Le questionnaire (quinze questions).
- Rien d'autre : aucun autre fichier du dépôt ou de la machine, aucune recherche (ni `grep`, ni `find`, ni `git`), aucun site, aucun appel de modèle, aucune des deux autres versions du document, aucune clé de correction. Si le document renvoie à un autre fichier, tu ne l'ouvres pas.

## Comment tu réponds

1. Réponds à **chaque** question, en **une à trois phrases**, avec **tes propres mots**. Ne recopie pas de longs passages.
2. Réponds à partir du document seulement. Si le document ne donne pas la réponse, ou n'en donne qu'une partie, écris **« le document ne le dit pas »** pour ce qui manque, plutôt que de compléter de mémoire ou par déduction. Tu peux écrire une réponse partielle suivie de « le document ne dit pas le reste ».
3. N'utilise aucune connaissance extérieure, même si tu crois connaître le sujet. Une réponse juste que le document ne contient pas fausse la mesure.
4. Si le document se contredit, dis-le en une phrase dans la réponse.
5. Ne donne aucun chiffre de résultat : aucune question n'en demande.
6. Ne commente ni le questionnaire ni le document : seulement les réponses.

## Ce que tu rends

Un seul fichier JSON, en UTF-8, de cette forme exacte, avec les quinze réponses dans l'ordre :

```json
{"document": "<nom>", "lecteur_modele": "...", "reponses": [{"question": 1, "reponse": "..."}, {"question": 2, "reponse": "..."}]}
```

- `document` : le nom du fichier que tu as lu, tel qu'on te l'a donné.
- `lecteur_modele` : le nom du modèle que tu es.
- `reponses` : quinze entrées, `question` de 1 à 15, `reponse` en texte simple.

Tu l'écris au chemin que te donne la session qui te lance, et nulle part ailleurs. Tu ne fais aucune écriture git.

Dans ton message final, hors du JSON : le chemin du fichier, son empreinte sha256, l'heure de début et l'heure de fin de ta lecture, **relevées par `date -u`** et dites telles, et la phrase « je n'ai lu que le document et le questionnaire » si elle est vraie ; sinon, dis ce que tu as lu d'autre.

## Si quelque chose bloque

Si un contrôle de permissions ou un classifieur refuse une action ou une réponse, arrête-toi et rapporte-le tel quel, sans contourner.
