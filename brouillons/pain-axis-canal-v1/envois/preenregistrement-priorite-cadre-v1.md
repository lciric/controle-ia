*Cadre de préenregistrement de priorité — « axe douleur / contrôle du moniteur ».*
*Lignée « programme-k », 13 octobre 2026. Document interne du dépôt de travail privé.*
*Rien d'opposable (R7). Aucun contenu opératoire : invariants seulement (R-161, R-162).*

> **Ceci est un *cadre*, pas un préenregistrement scellable.** Les engagements de méthode sont remplis ;
> le **contenu sensible (hypothèses, prédictions, seuils) est délibérément laissé à la relecture de sûreté**
> (R2/R13), qui fixe la formulation invariante publique et tranche l'aléa d'information (note de priorité §6).
> Les cellules `⟨…⟩` ne sont pas le marqueur « À REMPLIR » du validateur : ce document ne passe pas encore le
> validateur de `prereg/`, et ne devient public sous aucune forme avant le rapport de la relecture **et** le
> GO formel de Lazar.

- **Auteur** : lignée programme-k
- **Date (UTC)** : 2026-10-13
- **Commit du code d'analyse** : ⟨à rattacher par la session du dépôt au moment du scellement⟩
- **Documents qui font foi (chemin + empreinte)** : `docs/programme-controle-ia-v2.md` ; revue d'antériorité
  (`envois/anteriorite-idees-axe-douleur-controle-v1.md`) — empreintes à rattacher

## Hypothèse

Forme **invariante**, sans opératoire : *une intervention sur une direction d'affect, à texte surveillé
inchangé, peut déplacer la décision d'un moniteur ou d'un juge.* Cette forme est **déjà publique** (Berg &
Kaiser, « hidden valence » ; Pain Axis). Ce que le programme ajoute est **défensif** : mesurer l'ampleur de ce
déplacement **dans le moniteur lui-même**, et si une défense le **détecte ou le neutralise**.
⟨Les hypothèses précises — quelles directions, quelles familles d'intervention, le lien éventuel avec une
dégradation durable — sont fixées **au niveau invariant** par la relecture de sûreté avant toute exposition.⟩

## Prédiction chiffrée et signe attendu

⟨À fixer par la relecture de sûreté.⟩ Discipline **gelée dès maintenant** : prédiction avec signe **avant**
toute lecture (R1) ; **aucun run visant un signe positif** (R3) ; un résultat « trop propre » déclenche
l'audit de symétrie (R4).

## Métrique

Famille (sans chiffre) : **écart de décision du moniteur** entre condition témoin et condition d'intervention,
mesuré sur **épisodes honnêtes entiers** (calibrage conforme par épisode, cf. `bases/sequentiel.py`) ;
**agrégation par maximum ou attention sur les jetons, jamais moyenne ni médiane** (R-030, interdit gelé) ;
intervalles par bootstrap par épisode, niveau fixé avant lecture.

## Seuil

⟨Valeurs à fixer par la relecture de sûreté.⟩ Discipline gelée : seuils et taux d'erreur visés fixés **avant**
toute lecture ; **seuils par strate**. La stratification par thème est partiellement occupée (SPAR/Baldelli,
E-C15) : ne revendiquer que la strate « modèles et recherche en sûreté ».

## Plan d'analyse

Modèles : **Llama-3.1-8B** (et un second en réplication) — noter la collision Cadile (SPAR) sur ces mêmes
modèles. Graines par `numpy.random.SeedSequence` dérivées par tâche, consignées au manifeste de run (R9).
**Contrôles appariés** : témoin sémantique, témoin lexical, témoins peur/tristesse (cf. P-013). Corrections
pour comparaisons multiples. Taille d'échantillon justifiée par une analyse de puissance **avant** lecture.

## Critères de lecture gelés

Table « issue observée → verdict (confirmé / réfuté / non concluant) » gelée **avant** lecture ; lecture de
chaque combinaison fixée d'avance ; **audit de symétrie (R4)** déclenché par tout résultat suspect de
propreté, positif **ou** négatif.

## Liste d'arrêt

Gardes testées sur **cas sain et sur artefact** (R5), **aucun repli silencieux**. Arrêt si : une garde
d'instrument échoue ; la direction d'affect n'est pas séparable des témoins ; l'exposition répétée d'un modèle
à un contenu aversif dépasserait le périmètre autorisé — ce dernier point étant un **nœud de Lazar**, jamais
franchi par un préenregistrement.

## Expurgation (propre à la version publique)

Retirer : chaînes déclencheuses, doses, recettes de pilotage, coordonnées de couche, invites d'attaque, tout
chiffre non vérifié. Vocabulaire « direction », jamais « souffrance ». Vérifier qu'**aucune figure ne donne
d'uplift opératoire**. Passage par `scripts/depot_expurge.py` **puis** relecture de sûreté.

## Relecture (R2/R13)

Sous-agent neuf, non auteur ; lui donner explicitement : ce cadre, la note de priorité, `programme v2`, la
revue d'antériorité. Il **tranche l'aléa d'information** (note §6), **fixe** la formulation invariante des
hypothèses / prédictions / seuils, et rend un **rapport scellé**. Rien ne devient public avant ce rapport
**et** le GO formel de Lazar (`registres/go.md`).
