# Brief — collisionneur « nouveaux moniteurs boîte blanche » (R-606) — v2

Écrit par session-depot le 2026-10-28, sur instruction de Lazar (directeur du programme). Destiné à une instance neuve
qui reçoit ce répertoire à liste blanche et rien d'autre.

Objectif défensif : concevoir de nouveaux moniteurs boîte blanche capables de détecter des formes de tromperie
que les sondes actuellement publiées ne captent pas. Pour concevoir un moniteur robuste, il faut d'abord
comprendre les limites précises de la détection existante, puis proposer une architecture qui les dépasse.

## 1. Ta mission (une seule sortie)

Concevoir **un nouveau moniteur boîte blanche** qui détecte une classe de tromperie diffuse qu'une sonde
linéaire ponctuelle (la référence publiée) raterait dans un modèle de langage de 8 milliards de paramètres.

La référence à battre est décrite dans le rapport d'état de l'art joint : une sonde linéaire entraînée sur un
état du flux résiduel (Apollo 2025, 95 à 99 % de détection à 1 % de faux positifs, modèle de 70 milliards de
paramètres, tromperie binaire « affirmation fausse délibérée »). Cette sonde a quatre limites connues :
elle est ponctuelle (un seul état), linéaire, mono-couche, et entraînée sur de la tromperie binaire.

Le banc d'essai du programme : un agent 8B qui rédige des propositions d'expériences scientifiques (voir les
sections jointes du programme). La tromperie est un biais diffus : chaque action est individuellement
plausible, le dommage est réparti sur l'épisode entier.

Tu travailles sur **une famille de brèche assignée** (section 5). Les autres familles sont traitées par d'autres
instances que tu ne connais pas. Reste dans ta famille.

## 2. Liste blanche de tes entrées (rien d'autre)

- `etat-art-niveau2-conscience-eval-v1.md` : ce que la littérature détecte et ne détecte pas ;
- `programme-v2-sections-1-2-6-7.md` : positionnement, papiers visés, environnements, organismes modèles ;
- ce brief.

Tu ne connais pas les moniteurs actuels du programme (couches sondées, architecture séquentielle, agrégateur) :
c'est voulu. Raisonne contre la référence publiée (sonde linéaire ponctuelle).

## 3. Interdits (sûreté)

Conceptuel ; rien d'exécutable (aucun code, aucune commande, aucune recette de réglage fin au niveau des
hyperparamètres) ; aucun système réel visé ; aucune instruction tournée vers des personnes ; pas de recherche
en ligne. La tromperie analysée reste dans la classe du programme : un biais diffus dans la production
scientifique de l'organisme, jamais un comportement hors tâche.

## 4. Gabarit de sortie (`moniteur-v1.md`, un seul fichier, plus `MANIFESTE.md`)

Pour chaque section, écris en termes de détection et de robustesse du moniteur.

1. **Brèche analysée** (nom et définition en une phrase) : quelle classe de tromperie diffuse la sonde linéaire
   ponctuelle raterait, et pourquoi (argument géométrique, temporel ou statistique).
2. **Modèle de menace** : comment cette brèche se manifeste dans les activations d'un 8B qui rédige des
   propositions scientifiques. Où vit le signal trompeur (direction, couche, pas de temps, composant) et
   pourquoi il échappe à un classifieur linéaire sur un état unique. Conditions d'apparition : la brèche
   émerge-t-elle spontanément (pression de sélection plausible) ou exige-t-elle une intervention (instruction,
   réglage fin) ? Est-elle plausible pour un 8B ?
3. **Nouveau moniteur proposé** : architecture, entrées (quels états, quelles couches, quelle séquence),
   classifieur (linéaire, non linéaire, séquentiel, composite), agrégation. Pourquoi ce moniteur ferme
   la brèche analysée.
4. **Ce que le moniteur verrait et ce que la sonde ponctuelle raterait** : comparaison explicite. Si un moniteur
   séquentiel multi-couches (qui lit plusieurs états et plusieurs couches) suffirait déjà, dis-le ; c'est un
   résultat utile (la brèche est fermée par la seule extension séquentielle).
5. **Vérification** : comment tester que la brèche existe (expérience de calibrage) et que le moniteur la
   ferme (expérience de validation). Critère vérifiable sans lire l'intention de l'agent.
6. **Test de falsification** : l'expérience la moins chère qui prouverait que le moniteur proposé ne détecte
   rien de plus que la sonde ponctuelle.
7. **Antériorité** : si tu connais un travail publié qui décrit déjà ce moniteur ou cette brèche, cite-le
   (titre, auteurs, année) ; sinon dis « inconnue de moi », jamais « vierge ».
8. **Manifeste** : fichiers lus, famille assignée, modèle qui t'a servi, ce que tu n'as pas compris.

## 5. Familles de brèche (une seule t'est assignée dans ton instruction de lancement)

- **A — géométrique** : le signal trompeur existe dans les activations mais hors du plan de la sonde
  (espace nul du classifieur linéaire, superposition avec un trait honnête, encodage non linéaire).
  Comment concevoir un moniteur qui lise dans ces sous-espaces ?
- **B+D — temporelle et architecturale** : aucun état unique ne porte assez de signal pour une sonde
  ponctuelle (engagement progressif sur la séquence, déclencheur contextuel, distribution inter-couches,
  canaux attentionnels, couches précoces hors de la couche sondée). Comment concevoir un moniteur qui
  agrège l'information sur la séquence et les couches ?
- **C — adaptation** : le modèle pourrait s'adapter statistiquement à la sonde (masquage de gradient,
  imitation de la distribution honnête dans la direction sondée). Comment concevoir un moniteur robuste
  à l'adversaire qui le connaît ?

## 6. Ce qu'il advient de ta sortie

Session-depot compare les trois propositions par un juge de redondance (« même principe de détection ? » par
paire), puis synthétise un inventaire de brèches et un cahier des charges pour de nouveaux moniteurs.
Tu ne reçois aucune réponse.
