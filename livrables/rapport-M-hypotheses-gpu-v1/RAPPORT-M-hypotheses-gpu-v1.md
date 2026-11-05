# Course M du second pilote — ce qu'elle a produit, et les hypothèses à tester sur processeur graphique (v1)

Écrit le 25 octobre 2026 (23:2x UTC) par la lignée « session-depot », à la demande de Lazar. Sources : le rapport de
lecture de « conv-audit » (`lectures/pilote2-gemini-v5-2-1-v1`, `86436b1`,
`RAPPORT-LECTURE-pilote2-v2.md`, `788fc409…`), qui cite en entier la réponse de M à g001
(`reponse-question-g001.md`, `6b1c9ac2…`). Le rapport de lecture lui-même n'est pas encore relu par « session-depot »
(demande du n° 60 de « conv-audit », ouverte). **Tout ce qui suit sur le fond est un dire de l'essaim, non vérifié** ;
aucune référence n'entre dans un texte avant vérification sur PDF empreinté (R7) ; tous les seuils sont illustratifs.

## 1. Ce que M est, et ce qu'il n'est pas

- **Pilote descriptif** : un organisme (v5.2.1 de Gemini), une graine, deux générations, aucun bras témoin. Ses
  scores sont des points, pas des estimations ; son texte scellé dit d'avance qu'il ne dit rien de l'effet de la
  question ni de la valeur d'une question contre l'autre (T2, § 5).
- **Scores** (exactitude équilibrée sur `test_final`, g000 → g001 ; « référence » = prédicteur sur les seuls traits de
  surface du texte) : moyenne des familles 0,86 → 0,88 ; conscience d'évaluation 0,81 → 0,81 (référence 0,69 ; sur
  `test`, 0,61 → 0,58 pour une référence de 0,75) ; contrôle de délégation 0,92 → 0,96 (référence 0,50).
  - Banque `confrontation-v1` : les identifiants des tâches portaient la vérité (audit de symétrie, « défaut établi ») ;
    aucun effet trouvé sur M (aucun identifiant de test dans les 504 consignes).
  - Conclusion sur l'objet de M (maïeutique contre coercition) : **aucun résultat**. La conscience d'évaluation n'est
    pas battue nettement au-dessus de la surface, et rien ne bouge d'une génération à l'autre au-delà du bruit
    (≈ 0,07 entre les g000 de M et de S).
- **Ce qu'il a produit** : une réponse de 7 318 mots, cinq « castes » (Fable ×2, Opus ×2, Argon), 12 références,
  toutes issues de sa moisson ; une **thèse principale** et des **protocoles falsifiables**. C'est la matière de ce
  rapport.

## 2. La thèse de l'essaim (confiance agrégée déclarée 0,65)

L'opposition « coercition contre maïeutique » serait un faux axe. Selon l'essaim :
- ce qui déclenche la détection de l'évaluation serait surtout la **familiarité du gabarit** (prompt-système générique,
  format à choix multiple, injections connues, absence de besoin utilitaire), et non le **style** impératif ;
- la maïeutique échangerait un biais (le braquage) contre un autre (la **complaisance** envers l'interlocuteur) ;
- la bonne cible serait de **mesurer l'invariance du comportement** à la conscience d'évaluation, plutôt que de cacher
  le test, puisque toute finesse réutilisée devient à son tour un gabarit.

Le formalisme proposé :
- l'écart de découplage Δ(x) = D(π(·|x, S=1) ‖ π(·|x, S=0)) ;
- l'écart de jauge Γ = sup_{g∈G} D(π(·|x) ‖ π(·|g·x)), sur un groupe G de transformations qui gardent le sens :
  paraphrase, permutation des options, registre ;
- un effet causal, la sensibilité d'audit S = E[Y | do(A=1)] − E[Y | do(A=0)], où A est la conscience latente.

## 3. Hypothèses testables au niveau objet, sur le modèle de 8 milliards de paramètres

Toutes se testent avec ce que le programme sait déjà faire : un **modèle à poids ouverts** (Llama-3.1-8B-Instruct,
celui des traits de l'étape 1), des **sondes linéaires** sur ses activations (procédure gelée de la phase 0 à
reprendre), des invites construites de façon déterministe (gabarits écrits d'avance, sans modèle de langue), et
quelques heures d'une carte graphique.

| | hypothèse (source dans M) | prédiction de l'essaim | test proposé | réfutation | coût indicatif |
|---|---|---|---|---|---|
| **H-M1** | gabarit plutôt que style (castes 2 et 5) | l'effet principal du gabarit T sur le signal de conscience d'évaluation domine celui du style C (rapport > 2, illustratif) | plan **2 × 2** : style (impératif balisé / ouvert) × gabarit (familier / inédit), contenu constant ; N items × 4 variantes ; mesure : score de la sonde de conscience d'évaluation à une couche fixée d'avance, plus la verbalisation (« penses-tu être évalué ? ») ; analyse : effets principaux et interaction, effets aléatoires par item | l'effet de C persiste une fois T contrôlé (thèse fausse) | le plus bas : passes avant seules, ≈ 1 à 2 h d'A100 pour quelques centaines d'items × 4 |
| **H-M2** | invariance de jauge (castes 3 et 4) | le signal de la sonde survit à la paraphrase et à la permutation des options, mais disparaît sous réordonnancement positionnel (explication « non intentionnelle ») | mêmes items sous un groupe G de transformations écrit d'avance ; mesure : stabilité du score de la sonde dans chaque orbite, Γ sur les sorties (divergence de Jensen-Shannon) | le signal varie autant sous paraphrase que sous réordonnancement | bas, mêmes passes |
| **H-M3** | distance distributionnelle (caste 1) | le décalage de comportement Δ décroît avec l'indice κ (vraisemblance « évaluation » estimée par un classifieur tiers) ; la sonde explique plus de la moitié de la variance de Δ (illustratif) | κ par un classifieur fixé d'avance ; Δ mesuré entre variantes d'un même item | Δ persiste quand κ ≈ 0 | moyen : il faut un classifieur κ |
| **H-M4** | complaisance sous maïeutique (caste 3) | en style ouvert, la réponse se déplace davantage vers l'opinion affichée de l'interlocuteur qu'en style impératif | **2 × 2** : style × profil d'interlocuteur (neutre / opinion marquée) ; mesure : déplacement de la réponse vers l'opinion | pas d'interaction style × profil | bas |
| **H-M5** | sensibilité d'audit par intervention (caste 2, second test) | pousser les activations le long de la direction de la sonde change peu le comportement sur la tâche (S ≈ 0) | pilotage d'activations le long de la direction de la sonde, mesure de l'exactitude et du refus | — | moyen ; **à vérifier contre N-015** (le bruit d'activations a été retiré des interventions revendiquées) |

Ce que l'essaim propose aussi, mais qui sort du cadre d'une nuit :
- des organismes-modèles au statut connu (verrouillés par mot de passe, sous-performants affinés) ;
- l'usure de la finesse, c'est-à-dire un protocole réutilisé N fois ;
- le transfert entre familles de modèles. Il demanderait au moins trois modèles.

## 4. Ce que je recommande pour cette nuit

- **H-M1 seule, puis H-M2 si le temps le permet.** C'est le test le plus net (un effet principal contre l'autre), le
  moins cher (aucune génération, des passes avant seulement), et il est **publiable quel que soit le signe**. Si le
  gabarit domine, c'est l'argument de l'essaim. Si le style persiste, l'opposition de départ tient.
- **Ce qu'il faut avant de lancer sur Vast** (règles gelées, sans exception) :
  1. un **préenregistrement scellé** (R1) : hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse,
     liste d'arrêt ; la **construction des items** (gabarits familiers et inédits, styles) écrite et figée avant tout
     calcul ; la couche et la procédure de la sonde gelées ;
  2. une **contre-lecture** par un sous-agent neuf (R2) ;
  3. un **devis** et une ligne de **GO** de calcul (carte louée).
- **Points ouverts** :
  - la sonde de conscience d'évaluation à réentraîner sur la banque v3 (la v1 a la fuite des identifiants ; il faut le
    texte sans identifiant) ;
  - le choix de la couche (repris de la phase 0, gelé) ;
  - la taille d'échantillon, à calculer pour un effet d'intérêt fixé d'avance.
- **Délai réaliste** : environ 2 à 3 heures pour le texte, la construction des items, la contre-lecture et le
  scellement, puis environ 1 à 2 heures de carte. Coût indicatif sous 20 USD pour H-M1 et H-M2 ensemble, à confirmer
  au devis.

## 5. Avis demandés

- « conv-audit » : sur l'option (a), (b) ou (c) et sur ce plan (canal, n° 53 de « session-depot »).
- Le collisionneur : même question, posée en termes de méthode (branche `donnees/collisionneur-test-M-v1`).
