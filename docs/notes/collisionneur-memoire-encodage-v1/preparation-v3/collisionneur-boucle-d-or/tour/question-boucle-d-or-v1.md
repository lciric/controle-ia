# Question pour le collisionneur — la « Boucle d'or » : fenêtre de distance entre parents et allocation des expériences — v1 (brouillon de conv-audit ; session-depot fige sa version)

Écrite par l'instance nouvelle de conv-audit le 27 octobre 2026, à partir de 08:23 UTC (heure lue sur `date -u`), sur le
mot de Lazar de 09:22 heure de Paris, verbatim : « demande au colisionneur son avis aussi sur goldilocks ». Question
distincte de celle sur la mémoire (v3, `78690618…`) : un tour à part. Forme « arbitre », trois modèles, trois tours, une
tentative par cellule, un refus arrête le tour. **Dépense : seulement sur le mot direct de Lazar dans la session de
session-depot.**

## Question

« Un pôle de recherche automatique fonctionne par générations : des fiches d'hypothèses gelées engagent chacune une loi
prédictive des issues sachant les traits des instances ; un juge figé, tenu hors des agents, les promeut par un test de
pari contre un nul composite, sur des tirages frais ; une fille (recombinaison de deux parents survivants de domaines
différents) n'est promue que si elle bat ses parents, leurs mélanges et leurs enveloppes ; un budget limité d'expériences
doit être réparti entre les filles candidates. La recombinaison actuelle (pièce R) tire par strates de domaine, apparie
l'opérateur après le tirage, filtre les contraintes incompatibles et s'abstient faute de pont ; sur la littérature réelle
(rétrodiction sur les métadonnées d'arXiv 2003-2016, pièce T), l'allocation de ressources sur le graphe des termes bat la
marche « à la Swanson ».

Un autre modèle propose (pièce A, qui résume sa proposition et la critique que nous en faisons) : (a) une **fenêtre non
monotone** sur la similarité de domaine entre les deux parents — ne tester que les paires de la bande du milieu, ni trop
proches (triviales) ni trop lointaines (chimères) —, en s'appuyant sur une étude des combinaisons atypiques de revues
citées (Uzzi et collègues, Science, 2013) ; (b) **répartir les expériences selon l'entropie du verdict** (chance de survie
proche de la moitié), avec un score qui multiplie l'entropie, 4p(1−p) et une pénalité. Notre critique : sa simulation est
circulaire (mondes construits par bandes de similarité, calibration donnée à l'allocateur) ; l'étude citée mesure des
paires de revues dans les références d'un même article, pas la similarité entre deux hypothèses parentes ; le centre et
la largeur de la fenêtre ne sont étalonnés sur rien ; le score compte deux fois la même chose ; chez nous, une fille
triviale ne survit qu'au plus à α, c'est le juge qui l'écarte, pas l'allocateur.

1. **Ce qui est établi.** Que sait-on, et par quelles mesures, du lien entre la distance des idées combinées et leur
   valeur (impact, vérité, fécondité) : courbe en cloche, monotone, ou dépendante du domaine ? Distinguez ce que vous
   savez de ce que vous supposez ; citez précisément (titre, revue, année, page) : nous vérifierons sur les PDF.
2. **La bonne variable.** Pour des filles d'hypothèses, la similarité de domaine des parents est-elle la variable qui
   compte ? Ou le recouvrement des opérateurs, des variables, des signatures prédictives des parents, ou la **synergie**
   (l'information que les deux parents apportent ensemble et pas séparément) ? Comment la mesurer sur nos fiches ?
3. **Le bon objectif d'allocation.** Espérance de découvertes vraies par dollar, valeur de l'information (gradient de
   connaissance, optimisation bayésienne, bandits), entropie du verdict : lequel, quand, et comment éviter de récompenser
   la survie facile ? La fenêtre doit-elle être fixée d'avance ou apprise en ligne ?
4. **Un test qui peut échouer.** En simulation (pièce P : notre plan, fixé avant lancement, avec des mondes où la valeur
   ne suit pas la fenêtre) et sur données réelles (paires rangées par distance dans la rétrodiction, issue = cooccurrence
   future ou citations) : quels mondes, quel seuil, quelle taille d'échantillon, et qu'est-ce qui ferait conclure que la
   fenêtre n'apporte rien ?
5. **Ce qu'on perdrait** à adopter la fenêtre si elle est fausse, et ce qu'on perdrait à l'écarter si elle est juste. »

## Faits à servir (noms neutres ; aucun sigle ; aucun score de pilote ; rien de tout ceci n'est servi à un organisme)

- A : l'avis de l'instance sortante (`avis-boucle-d-or-gemini-v1.md`,
  `0414f1ab4dc7a76346e885d4b2c2f69293af094fc52db966e1915cb1363000aa`, branche `canal/conv-audit-relais-memoire-v1`, commit
  `0ba98ae`). Ses chiffres d'Uzzi et collègues sont lus par transcription, non vérifiés sur PDF empreinté (R7) : à servir
  comme tels, avec cette mention.
- P : notre plan d'essai (`essais-boucle-d-or-v1/plan-essai-boucle-d-or-v1.md`, empreinte dans son `.sha256`), sans ses
  résultats.
- R : la synthèse du tour « recombinaison », sur `main` : `docs/notes/pole-scientifique-automatique/synthese-recombinaison-v1.md`
  (R-527), et l'essai des ponts plantés (`trancher-recombinaison/trancher-recombinaison-v1.md`, empreinte dans son
  `.sha256`).
- T : la rétrodiction (`retrodiction-swanson/retrodiction-swanson-v1.md`, `057ef8a5…`).
- C : la conception du pôle (`conception-pole-scientifique-v1.md`, `a4f94148…`).

Chemins relatifs à `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/` sur la branche
`canal/conv-audit-n04`, sauf mention.
