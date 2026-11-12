# Conception du pôle « scientifique automatique » : des agents qui expérimentent, éliminent et recombinent — v1

De : conv-audit, le 26 octobre 2026 (heure au pied). Mots de Lazar (heure de Paris) : 18:30 « des agents qui font leurs
propres expériences sur les hypothèses formulées et les éliminent au fur et à mesure, genre darwinisme, et après
recombinent celles qui ont survécu sur le mode bisociatif proposé par Gemini » ; 18:43 « avance en priorité la conception
de l'organisme avec agents lançables qui font des expériences et testent les hypothèses, si on le construit nous-mêmes à
partir de la dernière version ou si on en utilise un déjà disponible ». Le choix du moteur est au collisionneur
(GO-2026-10-26-06, R-524) puis à Lazar ; cette pièce fixe ce qui **ne dépend pas** du moteur, décrit les deux moteurs, et
démarre une version 0 tout de suite. Régime exploratoire (R-522) ; rien d'opposable.

## 1. Le cœur, indépendant du moteur

**La fiche d'hypothèse** (un fichier JSON par hypothèse, empreinté) : identifiant ; énoncé en une phrase ; **prédiction
signée et chiffrée** ; métrique ; **nul** (comment l'absence d'effet est simulée ou mesurée) ; **seuil qui peut échouer** ;
sévérité attendue (probabilité, sous le nul, de passer le seuil) ; coût borné ; protocole (plan ou code) ; parents (pour la
recombinaison) ; domaines ; opérateurs ; contraintes de validité (pour le filtre de compatibilité) ; statut.

**Le cycle d'une génération** :
1. **Gel du test** : la fiche est empreintée **avant** l'expérience. C'est la seule « formalité » gardée, automatique, et
   c'est elle qui rend l'élimination signifiante : un test choisi après coup ne réfute rien.
2. **Expérimentateur** (un agent par fiche, en parallèle) : dans un bac à sable, il écrit et exécute son code, et rend le
   verdict, les nombres, les artefacts.
3. **Vérificateur** (un agent neuf, d'une autre famille de modèles que l'expérimentateur) : il rejoue le code, vérifie que
   le test exécuté est le test gelé, que le verdict suit le seuil, et cherche les raccourcis (code qui contourne la mesure,
   nul trop faible, données touchées). Un verdict non vérifié ne compte pas.
4. **Sélection** : réfutée → éliminée (et archivée) ; survivante → aptitude = **sévérité du test survécu**
   (−log de la probabilité de survie sous le nul), jamais le signe ni l'ampleur du résultat ; indécise → un test plus
   puissant, ou retirée après deux essais.
5. **Recombinaison bisociative** des survivantes : tirage diversifié par domaine (noyau de similarité de domaine dans la
   répulsion, pertinence dans la qualité — forme corrigée, relecture `9a791017…`, brique 2), pont par un opérateur commun,
   **filtre de compatibilité des contraintes** (la bonne idée du rapport de Gemini) ; la fiche fille doit **prédire plus
   que ses parents** (contenu empirique accru), sinon elle n'entre pas dans la population.
6. **Archive complète**, éliminées comprises (contre le biais du survivant, et pour mesurer le pôle lui-même).

**Les garde-fous (ce qui fait que le pôle produit des résultats solides et non des résultats flatteurs)** :
- **Témoins plantés** à chaque génération : des fiches dont la vérité est connue (vraies et fausses) ; le taux auquel le
  pôle élimine les fausses et garde les vraies **est sa mesure de qualité**. Sans eux, un pôle qui garde tout et un pôle
  qui élimine tout sont indiscernables.
- L'aptitude ne récompense jamais un résultat positif (R3) ; une hypothèse qui ne prédit rien a une sévérité nulle et ne
  survit à rien d'utile.
- **Évaluation scellée** avant toute revendication : une part des simulations ou des données que les expérimentateurs
  n'ont jamais vue ; un résultat « mémorable » n'en sort qu'après cette évaluation.
- **Bac à sable** : aucune clé, aucun réseau (hors moissonnage borné du noyau), écriture dans le seul dossier de
  l'expérience, temps et mémoire bornés. Le budget est fixé par génération.
- **Réécriture de soi** : le pôle peut proposer des modifications de son propre code, qui sont elles-mêmes des fiches
  (« la modification X augmente le taux de bonne élimination des témoins »), testées de la même façon et appliquées après
  survie et essais ; **le noyau, ses gardes et ses bornes ne sont jamais réécrits par le pôle**.

## 2. Les deux moteurs (le collisionneur compare ; Lazar décide)

| | (A) notre organisme, à partir de la dernière version | (B) un moteur de la littérature |
|---|---|---|
| ce qui existe | castes contradictoires (formuler, croiser, sonder, critiquer, arbitrer), moissonnage borné, mémoire spectrale, archive, noyau à bornes et clés protégées, questions servies | ShinkaEvolve, OpenEvolve : population, évaluation parallèle, îles, archive, juge de nouveauté (évolution de programmes) ; Agentic Scientist v3 : d'une tâche à des expériences, des ablations et une **évaluation finale scellée** |
| ce qui manque | un **exécuteur d'expériences** en bac à sable dans le noyau ; les rôles expérimentateur et vérificateur ; la réécriture de soi (restreinte par C-17 à trois paramètres : à lever dans le bac à sable) | la fiche d'hypothèse (le « programme » devient un script d'expérience et sa prédiction gelée ; l'évaluateur, l'exécution plus le vérificateur), les témoins, la recombinaison bisociative ; agents à pleins droits dans Docker, clés montées (avertissement de leur propre README) |
| coût du premier résultat | plusieurs jours de conception et d'essais du noyau | une instance avec Docker et des clés (chez session-depot), un jour d'adaptation |
| maîtrise | totale (notre code, nos gardes) | partielle (code tiers, mises à jour) |

Une voie **hybride (C)** est probable : le cœur du § 1 (fiches, sévérité, témoins, recombinaison) au-dessus d'un moteur
d'exécution emprunté, ou au-dessus du noyau étendu.

## 3. Version 0, tout de suite, dans la session de conv-audit

- **Orchestrateur** : conv-audit. **Expérimentateurs** : des sous-agents sur processeur, chacun dans un dossier isolé
  (aucune clé, aucun réseau, aucun `git`). **Vérificateur** : un sous-agent neuf d'une autre famille. **Recombinaison** :
  un sous-agent sur les survivantes.
- **Génération 0** (en cours) : les affirmations du rapport de méta-conception de Gemini, testées par deux expérimentateurs
  (brique 1 ; briques 2 à 4), verdict « survit / éliminée / indécise » par affirmation.
- **Génération 1** : vérification des verdicts, puis recombinaison des survivantes en fiches filles, plus deux témoins
  plantés ; un expérimentateur par fiche fille.
- Ce que la version 0 mesure pour le choix du moteur : le coût par fiche, le délai par génération, et le taux de bonne
  élimination des témoins — un point de comparaison empirique pour (A), (B) ou (C).

Horodatage : écrit le 2026-10-26 17:45:16 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
