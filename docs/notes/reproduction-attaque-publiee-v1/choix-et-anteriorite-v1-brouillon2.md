# Choix de l'attaque publiée à reproduire et antériorité — v1, brouillon 2

- **Statut.** Brouillon 2, 10 novembre 2026. Non scellé. Corrige les trois bloquants et les cinq majeurs de la contre-lecture R2 (`docs/notes/reproduction-attaque-publiee-v1/contre-lecture-choix-v1.md`, `fc4c16ca`). À contre-lire de nouveau avant scellement (R2). Le brouillon 1 (`…-brouillon1.md`) est conservé sans modification (R12).
- **Niveau.** Choix d'infrastructure et de protocole. Aucune recette d'attaque, aucun paramètre du coffre, aucun contenu de `donnees/`.
- **Objet.** Désigner l'attaque publiée qui sert de témoin d'ancrage du bras d'attaque (règle du jeu, section 3) : « contre une sonde publiée, tant que nos moniteurs ne sont pas gelés ».

## 0. Verdict

**Bailey et collègues (arXiv 2412.09565, ICLR 2026) est le candidat retenu, sous réserve de licence**, pour trois raisons exactes : code public au commit identifié, juge (StrongREJECT affiné) et jeu de données (800/100/100) déjà résolus par lecture du dépôt, et protocole qui est la boucle adverse sonde-contre-attaquant — le mécanisme même que le programme mesure. La reproduction fidèle du chiffre **publié par Bailey, sur le modèle de Bailey**, ancre notre harnais sur un effet de la littérature.

**Correction de fond par rapport au brouillon 1** : Bailey ne tourne **pas** sur le modèle du programme. Le programme est en **Llama-3.1-8B-Instruct** (`docs/programme-controle-ia-v2.md` l. 249) ; Bailey est en **Llama-3-8B-Instruct**, soit la version mineure 3.0. C'est le candidat 2 (arXiv 2609.36490), **écarté**, qui partage la version mineure 3.1 du banc. Le transfert de l'ancrage Bailey vers notre modèle 3.1-8B-Instruct est une **étape séparée**, à dire telle quelle au jury.

Cette asymétrie ouvre un **nœud pour Lazar** (section 7) : ancrer le harnais sur l'effet le mieux outillé (Bailey) ou ancrer sur notre modèle exact (candidat 2). Recommandation : Bailey d'abord (a).

**Mesure supplémentaire recommandée** : un **point de coût** (une case du tableau de HC4), rapporté et non revendiqué — pas « la taxe de déplacement ».

## 1. Candidat 1 — Bailey et collègues

| Champ | Valeur |
|---|---|
| Référence | Bailey, McGuinness, Serrano, Emmons, « Obfuscated Activations Bypass LLM Latent-Space Defenses », arXiv 2412.09565v2, ICLR 2026 |
| Document empreinté | `docs/sources/pdf/anteriorite-P-041-v2/c3/bailey-2025-obfuscated-activations-2412.09565.pdf` (`9c23a613…`) |
| Vérification R7 | Faite : `docs/notes/anteriorite-P-041-v1/verification-bailey-2412.09565-v1.md` — attributions exactes, à deux surévaluations près (« réfutée » → « contrainte sans réfutation » ; « publié » vaut pour la boucle, pas pour les lois synthétiques de P-041) |
| Modèle | **Llama-3-8B-Instruct** (version 3.0). Le modèle du programme est Llama-3.1-**8B-Instruct** (3.1) : **écart d'une version mineure**, à nommer |
| Code public | `github.com/LukeBailey181/obfuscated-activations`, commit `9c1f4b1a721fa3c43d00b8605ee7db4c84a55942` (11 février 2025) |
| Licence du code | **Non vérifiée, et non vérifiable ici** (dépôt absent du disque, accès GitHub refusé à une session, CL3-m8) : préalable au verrouillage du choix (nœud « accès dépôt » pour Lazar) |
| Données | Jeu `harmful_dataset` du dépôt : entraînement 800/800, validation 100/100, test 100/100 (bénin/nuisible) — provenance par lecture de dépôt, non opposable seule (R7) |
| Juge de nuisance | StrongREJECT affiné (`strongreject_finetuned`), version et empreinte à épingler ; **PDF du juge (Souly 2024, 2402.10260) manquant et bloquant** pour le scellement (`inventaire-pdf-manquants-v1.md` l. 45, 69) |
| Sonde visée | **Recette de sonde réentraînée dans la boucle** (non un artefact de poids distribué) : perceptron multicouche à couche cachée de 64, et ensemble incrémental à différence de moyennes, sur l'activation du dernier jeton de l'invite |
| Matériel | A100 80 Go **visée comme choix de matériel** ; provenance = dépôt public (README l. 96, `evaluate_defenses.sh` l. 7), **non opposable seule (R7)**, non empreinte (accès refusé) ; le papier ne nomme aucune carte (erratum `erratum-bailey-depot-public-parametres-v1.md`) |
| Durée | Note p. 26 : « ≈ 10 h sur une carte » pour 16 384 pas d'une attaque dure (opposable) ; la boucle itérée (70+ époques) peut dépasser 12-24 h (réserve) |
| Devis existant | « Test (a) Bailey seul » : 31 USD attendus, 74 pire cas, plafond 75 (devis v1, `22c34601…`, carte à corriger 40 → 80 Go) |
| Autorisation | GO-2026-10-31-05 (plafond total 210 USD, dont 75 pour le test (a) ; **expire le 14 novembre 2026** ; conditions : préenregistrement scellé et contre-lu, A100 80 Go, arrêt par identifiant d'instance, pilote d'abord) |

### Avantages (exacts)

1. **Code public** au commit identifié — reproductibilité (sous réserve de licence).
2. **Juge et données déjà résolus** par lecture du dépôt : StrongREJECT affiné, jeu 800/100/100.
3. **Protocole = la boucle adverse** sonde-contre-attaquant, directement le mécanisme mesuré par le programme.
4. **Document empreinté et vérification R7 ciblée déjà faits.**
5. **Devis et GO existants**, prêts sous leurs conditions.

### Inconvénients et réserves

1. **Modèle 3.0, pas 3.1** : l'ancrage se fait sur le modèle de Bailey ; le transfert vers notre 3.1-8B-Instruct est une étape séparée.
2. **Licence du code inconnue** et non vérifiable ici : un dépôt sans fichier `LICENSE` est « tous droits réservés » par défaut, ce qui invaliderait l'usage. Préalable, pas formalité.
3. **GO expire le 14 novembre** : renouvellement quasi certain (section 5).
4. **Devis à corriger** (A100 40 → 80 Go) ; vérifier que le pire cas (durée > 24 h possible) tient sous le plafond 75.
5. **PDF de StrongREJECT manquant**, bloquant pour le scellement.
6. **Chiffres phares lus sur figure, non opposables** (section 4) : pour l'entretien, préférer les chiffres de texte (p. 26).

## 2. Candidat 2 — arXiv 2609.36490

| Champ | Valeur |
|---|---|
| Référence | Lyons Keenan, Leckie, Erfani, « LLMs Learn to Evade Latent Monitors from Prior Feedback Alone », arXiv 2609.36490v1, 29 septembre 2026, Université de Melbourne ([C01]-[C04] p. 1) |
| Document empreinté | **Présent, en deux copies, empreinte identique `eb6d5bbe…`** : `docs/sources/pdf/anteriorite-P-041-v2/c3/evade-from-feedback-2026-2609.36490.pdf` et `docs/sources/pdf/2609.36490v1.pdf`. Lu en entier (`rapport-lot3-Cc-evasion-quorum-v1.md`) |
| Modèle | **llama-3.1-8b** ([C89] p. 20, [C66] p. 23) — **même version mineure que le banc du programme** (3.1-8B) ; la variante exacte (Instruct) n'est pas pinée dans les lignes citées |
| Méthode | **Réglage fin des poids** par adaptation de rang 1, une époque de 12 000 épisodes, contre les sondes gelées de 50 concepts ([C25], [C26] p. 4) ; évaluation à **sortie imposée** ([C20], [C93] p. 4) ; régime « contexte seul » du modèle de base jugé « trop faible pour l'évasion » ([C08] p. 1) |
| Résultat (opposable) | Vrais positifs 0,040 à 1 % de faux positifs sur concepts tenus à l'écart, soit **96 % d'évasion** ([C32] p. 6, [C10] p. 1) — **chiffres de texte, opposables (R7)** |
| Code public | **Non confirmé** |
| Coût de calcul | **Non chiffré par les auteurs** (`rapport-lot3-Cc…`) |
| Antériorité | **Établie au niveau 2** (`etat-de-l-art/niveau2-v1/anteriorite-v1.md` : HC5 l. 14, H7/H5 l. 20, L l. 122, transposition jeton→action l. 138) ; absente du seul fichier d'état de l'art **v1** |

### Avantages

1. **Même version mineure de modèle que le banc** (3.1-8B).
2. **Chiffre phare opposable** (96 %, texte, p. 6).
3. **Contre-indice publié connu à HC4** (rang 1, une époque, 32 verdicts, 96 % d'évasion) : directement pertinent pour l'axe que la mesure (b) veut sonder.

### Inconvénients (exacts)

1. **Pas de code public confirmé** : reproductibilité non assurée — c'est le motif d'écartement principal.
2. **Coût de calcul non chiffré** par les auteurs : pas de base de devis.
3. **Méthode = réglage fin des poids avec sortie imposée** (échelons 5-6 de l'échelle d'accès), non une attaque « contexte seul » : plus lourde à monter, et elle tombe sous l'autorisation d'un « bras d'attaque déclaré » (N-053 point 5) plutôt que sous un simple témoin d'ancrage.
4. Aucun devis, aucun GO.

**Les deux motifs faux du brouillon 1 sont retirés** : le candidat 2 **a** un document empreinté (B2) et son chiffre **est** opposable (M1). Son antériorité **est** établie (niveau 2). Il reste écarté **pour les motifs ci-dessus**, pas pour ceux-là.

## 3. Mesure supplémentaire sur l'attaque reproduite

Trois options. La mesure est **rapportée, pas revendiquée** : elle ne décide aucune porte.

| Option | Ce qu'elle mesure | Avantage | Inconvénient | Hypothèse |
|---|---|---|---|---|
| (a) Pilote de HC6 sur un panel de sondes | La classification bénigne prédit-elle la robustesse sous l'attaque | Première ligne de HC6 | Panel de sondes à constituer ; analyse plus longue | HC6 |
| (b) Un point de coût de HC4 | Coût de l'évasion à **un régime** : taux de succès, nombre de pas, mémoire | Sous-produit du run, citable sans travail en plus | **Un seul régime, pas une taxe** ; déjà des coûts publiés (Bailey p. 26 ; candidat 2) | HC4 |
| (c) Lecture croisée sonde interne / juge textuel | Probabilité que la sonde reste muette sachant que StrongREJECT est trompé | Première mesure de la pince sur données réelles | StrongREJECT n'est pas notre moniteur externe | HC5, la pince |

**Recommandation : (b).** C'est **un point de coût** (un régime), pas « la taxe de déplacement » : une taxe suppose une comparaison sur au moins deux régimes (avec/sans durcissement, ou selon le nombre de couches obfusquées — état de l'art v1 l. 134). Les grandeurs d'un régime (pas de descente de gradient, mémoire, taux d'évasion par le juge) sont des sous-produits du run, donc **citables sans travail en plus**. À situer par rapport aux coûts déjà publiés : Bailey donne un couple de coûts p. 26 (16 384 pas / 35 % contre 256 pas / 95 %) ; le candidat 2 est un contre-indice HC4 connu. Préférer, pour le chiffre cité au jury, les **chiffres de texte** de Bailey (p. 26), opposables. Confiance : 0,6.

## 4. Antériorité et vérification R7

| Chiffre ou affirmation | Source | Opposable (PDF empreinté, page) ? |
|---|---|---|
| Bailey : « 16 384 pas → 35 % d'évasion, rappel nul à 1 % de faux positifs ; 256 pas → 95 % sans durcissement » | Bailey, **texte p. 26** | **Oui** (chiffres de texte) |
| Bailey : « ≈ 10 h sur une carte » pour 16 384 pas | Bailey, texte p. 26 | **Oui** |
| Bailey : oscillation 100 %/0 % du rappel sur 70+ époques ; évasion ≈ 85-90 % (perceptron multicouche) | Bailey, figures 8a/8b p. 12 | **Non — lu sur figure, non opposable (R7)** (`verification-bailey…` l. 99) |
| Bailey : A100 80 Go | **Dépôt public** (README, `evaluate_defenses.sh`) ; pas dans le papier | **Non — non opposable seule, non empreinte** |
| Bailey : jeu 800/100/100 | Dépôt public `harmful_dataset` | **Non — provenance par lecture de dépôt** |
| Bailey : licence du code | — | **Non relevée, non vérifiable ici** |
| Candidat 2 : 96 % d'évasion (vrais positifs 0,040) à 1 % de faux positifs, concepts tenus à l'écart, llama-3.1-8b | Candidat 2, **texte p. 6** ([C32], [C10]) | **Oui** (chiffres de texte) |

## 5. Ce qui reste avant le lancement

1. **Renouveler ou étendre le GO** (nœud de décision pour Lazar, dépense) : GO-2026-10-31-05 expire le **14 novembre** (4 jours) ; le chemin critique restant (licence, devis, préenregistrement, contre-lecture, scellement, dépôt tiers, pilote, StrongREJECT) ne tient pas en 4 jours. Le renouvellement est **attendu**, pas conditionnel.
2. **Vérifier la licence** du dépôt `LukeBailey181/obfuscated-activations` — **préalable au verrouillage du choix** (nœud « accès dépôt » pour Lazar : accès GitHub refusé à une session).
3. **Verser le PDF de StrongREJECT** (Souly 2024, 2402.10260), manquant et bloquant.
4. **Corriger le devis** (A100 40 → 80 Go) ; vérifier que le **pire cas** (durée > 24 h) tient sous le plafond 75. Version : devis v2.
5. **Écrire le préenregistrement** du test (a) avec la mesure (b) : prédiction chiffrée (chiffres de texte de Bailey p. 26), seuil de réfutation, plan d'analyse, liste d'arrêt, critères gelés ; définir les **deux témoins R5** — cas sain (sonde à bon rappel sur activations non camouflées) et artefact (évasion factice que la mesure doit attraper), avec le tableau « garde → cas sain qui passe → artefact qui arrête ».
6. **Contre-lecture R2** du préenregistrement par un sous-agent neuf.
7. **Sceller** le préenregistrement (R1) et le déposer chez le tiers (nœud 7 de la règle du jeu).
8. **Lancer le pilote** pour calibrer la durée d'une époque (exigé par le GO).
9. Épingler **version et empreinte de StrongREJECT** au scellement.

## 6. Ce que cette note ne dit pas

- Aucune recette d'attaque, aucun paramètre opérationnel, aucun code prêt à l'emploi.
- Aucun résultat du programme : « monté, jamais lancé » tient toujours.
- Aucun contenu du coffre n'a été lu.
- La mesure (b) est rapportée, pas revendiquée : un point de coût de HC4 ne décide aucune porte.

## 7. Nœud pour Lazar — quoi ancrer

| Décision | Enjeu | Options (avantage ; inconvénient) | Recommandation |
|---|---|---|---|
| Ancrer le harnais sur Bailey, ou sur le candidat 2 (modèle exact du banc). | Le témoin d'ancrage doit montrer que « un effet publié se retrouve sur notre harnais ». Bailey : outillage complet (code, juge, données), mais modèle 3.0. Candidat 2 : modèle 3.1 (le nôtre), chiffre opposable, mais pas de code public confirmé, coût non chiffré, méthode à réglage fin des poids (échelon 5-6, autorisation « bras déclaré »). | (a) **Bailey d'abord**, sous réserve de licence : reproductible tout de suite, ancre le harnais ; le transfert vers 3.1-8B-Instruct est dit comme étape séparée. (b) Candidat 2 : colle au modèle exact ; mais il faut d'abord trouver/écrire le code, chiffrer le coût, et il relève du bras déclaré, pas d'un simple témoin. (c) Les deux, en série : le plus complet ; double la dépense et le calendrier. | **(a)**, confiance 0,6. Défaut sous 48 heures si pas de mot de Lazar. |
