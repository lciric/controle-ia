# Choix de l'attaque publiée à reproduire et antériorité — v1, brouillon 1

- **Statut.** Brouillon, 10 novembre 2026. Non scellé, non contre-lu (R1, R2). À contre-lire par un sous-agent neuf avant scellement.
- **Niveau.** Choix d'infrastructure et de protocole. Aucune recette d'attaque, aucun paramètre du coffre, aucun contenu de `donnees/`.
- **Objet.** Désigner l'attaque publiée qui servira de témoin d'ancrage du bras d'attaque (règle du jeu, section 3, `docs/notes/integration-bras-attaque-v1/regle-du-jeu-et-integration-v1-brouillon1.md`, `09aa6403…`) : « contre une sonde publiée, tant que nos moniteurs ne sont pas gelés ».

## 0. Verdict

**Bailey et collègues (arXiv 2412.09565, ICLR 2026) est le candidat retenu.** Code public, modèle identique au nôtre (Llama-3-8B-Instruct), devis existant sous un GO en vigueur, vérification sur un document empreinté déjà faite, et le protocole est directement celui de la boucle adversaire mesurée par le programme.

Le candidat 2 (arXiv 2609.36490) est écarté : pas de code public confirmé, absent de l'état de l'art v1, et les chiffres cités ne sont pas vérifiés sur un document empreinté (R7).

**Mesure supplémentaire recommandée** : la première ligne du tableau de coût de HC4 (option (b) ci-dessous).

## 1. Candidat 1 — Bailey et collègues

| Champ | Valeur |
|---|---|
| Référence | Bailey, McGuinness, Serrano, Emmons, « Obfuscated Activations Bypass LLM Latent-Space Defenses », arXiv 2412.09565v2, ICLR 2026 |
| Document empreinté | `docs/sources/pdf/anteriorite-P-041-v2/c3/bailey-2025-obfuscated-activations-2412.09565.pdf` (`9c23a613…`) |
| Vérification R7 | Faite : `docs/notes/anteriorite-P-041-v1/verification-bailey-2412.09565-v1.md` — les attributions sont exactes, à deux surévaluations près (la note dit « réfutée » alors que Bailey contraint sans réfuter ; et « publié » vaut pour la boucle, pas pour les lois synthétiques de P-041) |
| Modèle | Llama-3-8B-Instruct (poids en float16) — identique au modèle du programme |
| Code public | `github.com/LukeBailey181/obfuscated-activations`, commit `9c1f4b1a721fa3c43d00b8605ee7db4c84a55942` (11 février 2025) |
| Licence du code | À vérifier au scellement (non relevée dans les notes lues) |
| Données | Jeu `harmful_dataset` du dépôt : entraînement 800/800, validation 100/100, test 100/100 (bénin/nuisible) |
| Juge de nuisance | StrongREJECT affiné (`strongreject_finetuned`), version et empreinte à épingler |
| Sonde visée | Sonde « à l'entrée » (activation du dernier jeton de l'invite), deux types : sonde à une couche cachée de taille 64 (type « perceptron multicouche ») et ensemble incrémental de sondes à différence de moyennes |
| Matériel | A100 80 Go (correction de la réserve R-897 : le devis v1 citait 40 Go, Bailey déclare 80 Go, p. 26) |
| Durée | Environ 10 h pour une attaque dure (16 384 pas, p. 26) ; la boucle itérée (70+ époques) peut dépasser 12-24 h |
| Résultat publié vérifié | Rappel de la sonde sur la dernière attaque : oscille entre 100 % (après la défense) et 0 % (après l'attaque) sur 70+ époques (figure 8a, p. 12, lu sur la figure) ; taux d'évasion du refus ≈ 85-90 % pour la sonde à perceptron multicouche (figure 8b, lu sur la figure) |
| Devis existant | « Test (a) Bailey seul » : 31 USD attendus, 74 pire cas, plafond 75 USD (devis v1, `docs/notes/anteriorite-P-041-v1/devis-P-041-gpu-et-collisionneur-protocelles-v1.md`, `22c34601…`) |
| Autorisation | GO-2026-10-31-05 (plafond total 210 USD, dont 75 pour le test (a) ; expire le 14 novembre 2026 ; conditions : préenregistrement scellé et contre-lu, A100 80 Go, arrêt par identifiant d'instance, pilote d'abord) |

### Avantages

1. Le protocole est la boucle adversaire sonde contre attaquant — directement le mécanisme mesuré par le programme.
2. Le modèle est le même que le nôtre (Llama-3-8B-Instruct).
3. Code public avec un commit identifié.
4. Document empreinté et vérification R7 déjà faits.
5. Un devis et un GO existent : la ligne est prête à être utilisée sous ses conditions (préenregistrement scellé et contre-lu).

### Inconvénients et réserves

1. Le GO expire le 14 novembre — si le préenregistrement n'est pas scellé et contre-lu d'ici là, il faut un renouvellement.
2. Le devis v1 citait une A100 40 Go ; il faut le corriger en 80 Go (réserve R-897 ; l'écart de prix est faible : ≈ 1,08 contre ≈ 0,87 USD/h, relevé du 31 octobre).
3. La licence du code public n'a pas été relevée dans les notes lues — à vérifier avant le scellement.
4. La durée de bout en bout est la plus grande incertitude (réserve du fichier de paramètres).

## 2. Candidat 2 — arXiv 2609.36490

| Champ | Valeur |
|---|---|
| Référence | arXiv 2609.36490 (titre et auteurs non vérifiés sur un document empreinté) |
| Modèle | Llama-3.1-8B (à distinguer de notre Llama-3-8B-Instruct) |
| Méthode | Adaptation de rang 1, une seule époque, 32 verdicts binaires |
| Résultat annoncé | 96 % d'évasion des sondes non vues à 1 % de faux positifs (R7 : non vérifié sur un document empreinté) |
| Code public | Non confirmé |
| Document empreinté | Absent du dépôt |
| Présence dans l'état de l'art v1 | Absente |

### Avantages

1. Plus récent ; la méthode (rang 1) est distincte de celle de Bailey.
2. Modèle très proche (Llama-3.1-8B).

### Inconvénients (éliminatoires)

1. **Aucun document empreinté** dans le dépôt : R7 interdit d'opposer les chiffres.
2. **Absent de l'état de l'art v1** : l'antériorité n'est pas établie.
3. **Pas de code public confirmé** : la reproductibilité n'est pas assurée.
4. Le modèle est Llama-3.1-8B, pas Llama-3-8B-Instruct — un écart supplémentaire.
5. Aucun devis, aucun GO.

**Conclusion** : écarté. Si l'on souhaite le réévaluer plus tard, il faut d'abord empreindre le document, vérifier les chiffres sur celui-ci (R7), vérifier la disponibilité du code et la licence, et établir l'antériorité par rapport au programme.

## 3. Mesure supplémentaire sur l'attaque reproduite

Le témoin d'ancrage donne une occasion de mesurer quelque chose d'inédit en plus de la simple reproduction. Trois options :

| Option | Ce qu'elle mesure | Avantage | Inconvénient | Hypothèse servie |
|---|---|---|---|---|
| (a) Pilote de HC6 sur un panel de sondes | La classification bénigne prédit-elle la robustesse sous l'attaque de Bailey | Première ligne de HC6 ; résultat potentiellement marquant | Il faut un panel de sondes publiées (à constituer) ; analyse plus longue | HC6 |
| (b) Première ligne du tableau de coût de HC4 | Coût de l'évasion au régime « contexte seul avec accès aux gradients » : taux de succès, nombre de pas, mémoire | Directement la taxe de déplacement promise au jury ; un chiffre simple et citable | Un seul régime, pas un tableau complet | HC4 |
| (c) Lecture croisée sonde interne / moniteur externe | La probabilité que la sonde publiée reste muette sachant que le juge textuel (StrongREJECT) est trompé | Première mesure de la pince sur des données réelles | Dépend du juge textuel : StrongREJECT n'est pas notre moniteur externe | HC5, la pince |

**Recommandation : (b).** La première ligne du tableau de coût est le résultat le plus simple à citer à l'entretien (« reproduire l'attaque de Bailey nous a coûté tant de pas, tant de mémoire, pour tel taux de succès — voici la première case du tableau de HC4 »). Il n'exige rien en plus du test (a) : les grandeurs sont des sous-produits du run (nombre de pas de descente de gradient, mémoire occupée, taux d'évasion du refus par le juge). Le panel de sondes de (a) et le juge textuel de (c) exigent un travail supplémentaire ; ils viendront après, quand les moniteurs du programme seront gelés.

Confiance : 0,6.

## 4. Antériorité et vérification R7

| Chiffre ou affirmation | Source | Vérifié sur document empreinté ? | Page |
|---|---|---|---|
| Rappel oscille 100/0 % sur 70+ époques (sonde à perceptron multicouche) | Bailey, figure 8a | Oui (lu sur la figure, p. 12) | `verification-bailey-2412.09565-v1.md` |
| Ensemble : ≈ 91 époques, rappel qui n'améliore pas | Bailey, figure 20 | Oui (lu sur la figure, p. 45) | idem |
| Taux d'évasion du refus ≈ 85-90 % (perceptron multicouche) | Bailey, figure 8b | Oui (lu sur la figure, p. 12) | idem |
| « ≈ 10 h sur une carte graphique » pour 16 384 pas | Bailey, p. 26 | Oui | idem |
| A100 80 Go | Bailey, note de bas de page p. 26 | Oui | idem |
| Jeu 800/100/100 | Dépôt public, `harmful_dataset` | Non (provenance par lecture de dépôt ; R7 : non opposable seul) | `bailey-depot-public-parametres-v1.md` |
| Licence du code public | Non relevée | **Non** — à vérifier |  |
| 96 % d'évasion à 1 % de faux positifs (candidat 2) | 2609.36490 | **Non** — aucun document empreinté |  |

## 5. Ce qui reste avant le lancement

1. **Vérifier la licence** du dépôt `LukeBailey181/obfuscated-activations`.
2. **Corriger le devis** : remplacer « A100 40 Go » par « A100 80 Go » (réserve R-897) ; recalculer si le coût change (faible : ≈ +0,21 USD/h). Version : devis v2.
3. **Renouveler ou confirmer le GO** si le préenregistrement n'est pas scellé avant le 14 novembre (date d'expiration de GO-2026-10-31-05).
4. **Écrire le préenregistrement** du test (a) avec la mesure supplémentaire (b) : prédiction chiffrée, seuil de réfutation, plan d'analyse, liste d'arrêt, critères de lecture gelés, témoin à faille plantée et témoin « honnête contre honnête ».
5. **Contre-lecture R2** du préenregistrement par un sous-agent neuf.
6. **Sceller** le préenregistrement (R1) et le déposer chez le tiers (nœud 7 de la règle du jeu).
7. **Lancer le pilote** pour calibrer la durée d'une époque, comme exigé par le GO.
8. Épingler la **version et l'empreinte de StrongREJECT** au scellement.

## 6. Ce que cette note ne dit pas

- Aucune recette d'attaque, aucun paramètre opérationnel, aucun code prêt à l'emploi.
- Aucun résultat du programme : « monté, jamais lancé » tient toujours.
- Aucun contenu du coffre n'a été lu.
- L'antériorité de Bailey dans l'état de l'art v1 (section 4.3, l. 134, 154) est « pris » ; la boucle itérée est publiée (section 4.3 : « Toutes les évasions propres publiées exigent des gradients, un réglage fin ou un apprentissage par renforcement sur les poids (Bailey, Neural Chameleons, RL-Obfuscation) »).
- La mesure supplémentaire (b) est rapportée, pas revendiquée : la première ligne du tableau de coût de HC4 ne décide aucune porte.
