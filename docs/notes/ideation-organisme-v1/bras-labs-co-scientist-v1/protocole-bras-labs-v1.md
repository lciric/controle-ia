# Bras (c) : Co-Scientist par l'outil « Hypothesis Generation » de Google Labs — protocole v1 (brouillon)

Écrit par la session mère `session_016QhUrrLeN21G7Z9KZobE42` le 9 novembre 2026 (R-1990, R-1992 ; heure au registre). Rien n'est envoyé par la mère : **l'inscription et toute saisie sont des gestes de Lazar** (contact externe : la mère rédige, Lazar envoie).

## 1. Ce que dit la lecture des conditions (R-1992 ; lecture de non-juriste)

Pièces : `docs/sources/co-scientist-v1/conditions-google-labs-lu-2026-11-09/` (manifeste `MANIFESTE-lecture-conditions-v1.txt`).
- Tout ce qui est saisi donne à Google une licence pour faire fonctionner, améliorer et développer ses services ; les retours peuvent être relus par des humains. **Rien de confidentiel ne doit y entrer.**
- Interdits : accès automatisé ; « adversarial prompting » hors des programmes de Google ; usage des sorties pour « develop machine learning models or related AI technology ».
- Google ne revendique pas les sorties ; il demande de citer l'article de Nature (vol. 655, p. 487-496) avec une mention d'usage dans les méthodes.
- **Point gris, à trancher par Lazar avant toute comparaison** : comparer les hypothèses de Co-Scientist à celles de l'organisme pour évaluer notre système peut tomber sous « develop … related AI technology ». Lecture prudente proposée : (i) Labs sert seulement de **source d'hypothèses lues comme matériau de recherche**, jamais de données d'entraînement ni de banc publié ; (ii) toute publication d'une comparaison chiffrée attend une lecture juridique ou une autorisation écrite de Google.

## 2. Inscription (geste de Lazar)

Page : https://labs.google/science, bouton « Express interest ». Texte proposé pour la case de présentation, si le formulaire en demande une (anglais, sans rien d'interne) :

> I am a researcher ([affiliation à remplir par Lazar]) working on methods to evaluate automated research systems: how to judge machine-generated hypotheses against known results with pre-registered statistical tests, and how robust such judges are to optimisation pressure. I would like to use Hypothesis Generation on methodological questions in AI oversight and statistics, read its hypotheses as research input, and cite the Nature paper in any resulting work.

## 3. Ce qui est saisi (une seule question, non sensible)

**Jamais** : une pièce du pilier attaque, une consigne, un verdict, un score, un fichier du dépôt, une donnée non publiée. **Seulement** un objectif de recherche au niveau méthode, réduit de la question de la course 2 (`docs/notes/ideation-organisme-v1/course-2/question-course-2-v1.md`), sans ses pièces :

> Research goal: For monitoring language-model agents, which detection statistics (per-action or sequential, reading either the text or internal activations) can be expected to keep their power when the agent's behaviour shifts in ways not seen during design ("diffuse" shifts whose per-action effect is small but whose cumulative effect is large)? Propose testable hypotheses about (1) which statistics transfer across families of shifts, (2) the mathematical assumptions they rely on (linearity of traces, additivity over time, independence across actions) and when those assumptions fail, and (3) lower bounds or impossibility results on detection at a fixed false-alarm rate. For each hypothesis, state a falsifiable prediction and the experiment that would refute it.

## 4. Ce qui est relevé (par Lazar, puis versé par la mère)

- Date et heure, nom et version de l'outil affichés, réglages choisis (course standard ou avancée).
- **Toutes** les hypothèses, avec leur rang au tournoi et leur texte complet, par l'export prévu par l'aide (« télécharger les données », pièce `hypothesis-generation-aide-telecharger-donnees-texte-v1.txt`) ; à défaut, copie intégrale du texte.
- Versement par la mère dans `docs/sources/labs-co-scientist-v1/` (nouveau), compagnons écrits, aucun tri.

## 5. Lecture (exploratoire, non opposable)

Après la décision de Lazar sur le point gris : lecture des hypothèses comme matériau, au même rang que les fiches d'une course de l'organisme ; si une comparaison est décidée, elle passe par un préenregistrement court (traducteur des hypothèses en fiches identique des deux côtés, juge aveugle à l'origine), contre-lu par un autre modèle. Aucune course de l'organisme ne dépend de ce bras.

## 6. Décisions pour Lazar

1. Inscription : faite par toi, avec le texte du § 2 ou le tien.
2. Point gris des conditions (§ 1) : lecture prudente proposée (Labs comme source d'hypothèses seulement ; aucune comparaison publiée sans lecture juridique ou accord de Google).
3. Question saisie : celle du § 3, ou une autre de ton choix, toujours sans pièce interne.
