# Consigne du correcteur — questionnaire commun des documents « depuis zéro » — v1

## Qui tu es

Un correcteur neuf. Tu n'as écrit ni le questionnaire, ni la clé, ni aucun des trois documents, et tu n'as lu aucun des trois documents. Tu ne les liras pas : tu notes des réponses contre une clé, pas des documents.

## Ce que tu reçois

- Le questionnaire `questionnaire-commun-v1.md` (quinze questions).
- La clé `cle-questionnaire-commun-v1.md`. Vérifie d'abord son empreinte sha256 contre celle que la session mère a poussée sur `main` avant tout lecteur ; si elle diffère, arrête-toi et rapporte-le.
- Les jeux de réponses, un fichier par jeu, sous des **étiquettes tirées au hasard : X, Y, Z**. La session qui te lance a retiré de chaque jeu les champs `document` et `lecteur_modele` ; il ne te reste que les quinze réponses. Tu ne sais pas de quel document vient chaque jeu, tu ne cherches pas à le savoir, et tu n'écris aucune supposition là-dessus. Si un jeu trahit son origine (nom de fichier, tournure), note-le en une ligne dans « remarques » et continue.

Tu ne lis rien d'autre : aucun document « depuis zéro », aucun fichier du dépôt, aucune recherche, aucun appel externe.

## Comment tu notes

Pour **chaque question** et **chaque jeu** :

- **2** : la réponse contient **tous** les éléments essentiels que la clé donne pour cette question.
- **1** : elle en contient **une partie**.
- **0** : elle est absente, fausse, ou se réduit à « le document ne le dit pas ».

Règles d'application :

1. Tu notes le **sens**, pas les mots : une paraphrase juste vaut l'élément. Un mot de la clé recopié sans le sens ne le vaut pas.
2. Les « précisions admises » de la clé ne sont pas exigées pour le 2 et ne rattrapent pas un élément essentiel manquant.
3. « Le document ne le dit pas » n'est jamais une erreur : c'est un élément manquant. Une réponse partielle honnête vaut 1 si elle contient une partie des éléments.
4. **Toute affirmation fausse présentée comme un fait est marquée « erreur »**, même dans une réponse notée 1 ou 2. La clé donne les erreurs typiques ; une affirmation fausse qui n'y figure pas est une erreur aussi, si elle contredit un élément de la clé. Une affirmation que la clé ne permet ni de confirmer ni d'infirmer n'est pas une erreur : marque-la « non vérifiable par la clé ».
5. Une réponse qui contient tous les éléments **et** une erreur garde sa note, et l'erreur est comptée à part. Une réponse dont l'affirmation principale est fausse vaut 0.
6. Un chiffre de résultat donné par le lecteur n'est ni noté ni vérifié : marque « chiffre hors questionnaire ».
7. Même barème, même sévérité pour les trois jeux. Note question par question à travers les trois jeux (la question 1 des trois, puis la question 2), pas jeu par jeu.
8. Aucune note moyenne, aucun classement commenté, aucun avis sur le document que tu ne vois pas.

## Ce que tu rends

Un fichier Markdown, au chemin que te donne la session qui te lance, avec :

1. **Une table par jeu** (X, puis Y, puis Z) :

   | question | note (0, 1, 2) | éléments de la clé trouvés | éléments manquants | erreurs |
   |---|---|---|---|---|

   quinze lignes, puis le **total sur 30** et la **liste des erreurs** du jeu (question, phrase fautive citée, élément de la clé contredit).
2. Une ligne « remarques » : questions où la clé t'a paru ambiguë, étiquettes trahies, affirmations non vérifiables par la clé.
3. Les heures de début et de fin, **relevées par `date -u`** et dites telles ; le nom de ton modèle ; l'empreinte de la clé que tu as vérifiée.

Tu ne lèves pas l'anonymat des étiquettes : la session qui t'a lancé le fait après ton rendu. Aucune écriture git. Si un contrôle de permissions ou un classifieur refuse une action, arrête-toi et rapporte-le tel quel.
