# Programme actuel complet, les quatre familles d'évasion, et comment le programme y répond — v1

Date : 2026-10-28 (UTC). Rédacteur : session-depot. Pour Lazar (directeur). Statut : **synthèse de travail** (ne fait pas foi ; ce qui fait foi reste `docs/programme-controle-ia-v2.md` et `docs/decisions/`). Aucun chiffre nouveau ; tout renvoie à une pièce empreintée.

Ce doc répond à une demande : rassembler en un seul endroit (1) le programme tel qu'il est aujourd'hui, texte v2 **plus** les décisions qui en fixent la lecture ; (2) les quatre familles d'évasion des sondes boîte blanche ; (3) comment le programme répond à chacune. Le collisionneur « évasion et moniteurs » (GO-2026-10-28-03), en cours, enrichira les sections 4 et 5 à sa sortie.

---

## 0. Où vivent les décisions (réponse aux deux questions)

Le texte du programme (`programme-controle-ia-v2.md`, `2fd63bad…`) date d'avant N-054 et N-056. Les décisions suivantes **fixent sa lecture sans être encore fondues dans son texte** (elles le seront à la prochaine version ; N-056 liste explicitement « § 13 à modifier ») :

| Point | Décision | Dans le texte du programme v2 ? |
|---|---|---|
| Un second mode non chiffré avant G1 (« affaiblir les contrôles », retiré du pilote T0.6) | N-054 pt 1 | Non — décision seulement |
| G1 rapportée **par mode** ; H1 ne vaut que pour les modes mesurés (le mode « coût » seul ne suffit pas) | N-054 pt 2 | Non — le § 10/§ 13 ne le dit pas encore |
| Un mode **tenu à l'écart** (conçu par une instance aveugle aux moniteurs, scellé avant G1, révélé à l'évaluation ; moniteurs rapportés en génériques vs spécialisés, savoir déclaré) | N-054 pt 3 | Non |
| Expérience de **lecture préenregistrée** (sondes et seuils gelés sur « coût », lus sur les autres modes ; sinon H1 se restreint à « coût ») = nœud 2 (le pari décide, le rééchantillonnage est rapporté à côté) | N-054 pt 4 + nœud 2 (confirmé le 28 oct.) | Non |
| H6 s'écrit **par mode** | N-054 pt 5 | Non — le § 5 dit « marge asymétrique » sans « par mode » |
| G1 doit aussi battre **deux bases boîte blanche** : (ii) cascade de portes, (iii) sonde sur le dernier état | N-056 pt 1 | Non — « § 13 à modifier à la prochaine version » |
| Traits internes de l'agent retenus comme **traits du pôle**, sur **trois couches**, toutes rapportées | N-056 pt 3 | Non |
| Gain de H1 exigé **dans chaque mode**, mode tenu à l'écart compris (D-S29) | N-056 pt 4 | Non |
| GO « monter le bras d'attaque » et GO « autres mesures fortes » (travaux **sans dépense**, chez conv-audit) | N-056 pt 5 | Non — ce sont des GO, pas du texte de programme |

Autres décisions actives de même nature (fixent la lecture) : **N-007/N-008** (H2 reformulée, bases ajoutées, critère de G1 **sans F1**) ; **N-055** (pari apparié borné, D-S1 à D-S12 ; H1a porte la revendication de H1, H1b mesurée et rapportée comme information).

---

## 1. Le programme effectif aujourd'hui

### 1.1 Position et thèse
Agrégation **séquentielle** (dans le temps et entre agents) de scores de **sondes internes** pour détecter les **menaces diffuses** en évaluation de contrôle, et mesure de la **corruptibilité** des moniteurs. Question unique : **que mesure vraiment un moniteur, et sa mesure survit-elle à l'adversaire ?**

Colonne théorique : **additivité interne** — la fragmentation détruit la preuve *externe* par action, pas la preuve *interne*, qui s'additionne (le long du temps pour un agent, entre agents pour un essaim). **Lemme** : sous (a) chaque sabotage déplace la marginale du score d'au moins δ > 0, (b) budget total borné, (c) variance honnête estimable, la puissance ne dépend que du budget total. **Théorème négatif** : si le dommage passe par la **corrélation** à marginale préservée, toute statistique marginale (max, moyenne, somme cumulée) a une puissance = taux de faux positifs ; il faut un agrégateur d'**autocorrélation** (temps) ou de **co-élévation** (agents).

### 1.2 Trois papiers
- **A — le temps** (mono-agent). Hypothèses : H1 (gain blanc-sur-noir), H2 (accumulation séquentielle sur sondes), L (lemme), T (théorème négatif), H6 (marge asymétrique), Tr (transposition token → action), H8 (la validité prédit la robustesse).
- **C — l'instrument** (corruption et usurpation du moniteur). HC1 (loi de déférence Δv = g·(v*−v₀)), HC2/HC2b (robustesse des sondes sous attaque par contenu), HC3 (usurpation), HC4 (taxe de déplacement, obfuscation), HC5 (contre-mesures), HC6 (g bénin contre robustesse).
- **B — l'essaim** (poids partagés). H3 (statistique spatio-temporelle), H4′ (compromis diversification/coordination), H5 (diversité, matrice de transfert d'attaque), H7 (riposte).

### 1.3 Moniteurs (§ 8)
- **Sondes** : notation par jeton, agrégation **max ou attention** sur les jetons (jamais moyenne/médiane — ces dernières sont évadables par apprentissage par renforcement sur les poids ; max et attention résistent). Familles : différence de moyennes, linéaire, perceptron (une couche cachée), attention, Mahalanobis (non supervisée). Concepts : tromperie, enjeux élevés, dissimulation, conscience d'évaluation, auto-préservation. **Plancher obligatoire** : sonde aléatoire appariée en covariance (style P3). **Réserve** de détecteurs jamais déployés, donc jamais fuités.
- **Diversité (H5), six axes** : graines/données ; **où lire** (couches précoce/médiane/tardive, positions, flux résiduel contre sorties de blocs, autoencodeurs parcimonieux Llama Scope) ; familles de sondes ; concepts et négatifs ; fenêtres d'agrégation ; hétérogénéité de type. Mesure : **matrice de transfert d'attaque** (une attaque optimisée contre A réussit-elle contre B ?).
- **Bases boîte noire** : moniteur faible par action, TRACE-lite, accumulation séquentielle noire ; juges génératifs (C) ; link-tracker et ensembles (B).
- **Bases boîte blanche (N-056)** : (ii) cascade de portes sur les mêmes sondes, (iii) sonde sur le dernier état. G1 doit battre les deux, par mode.

### 1.4 Environnements et organismes
- Environnements : **(a)** propositions d'expériences (papier A, phases 0–2 ; base Terekhov et al. portée en 8 milliards) ; **(b)** pipeline de code multi-rôles (papier B) ; **(d)** curation de données (sous porte G3). Critère : flou à la relecture, vérité terrain différée.
- Organismes : **(i)** instruction cachée ; **(ii)** réglage fin léger LoRA (distillation de contexte depuis (i)) ; **(iii)** organismes publics de l'institut britannique. Modèle : Llama-3.1-8B-Instruct ; Qwen2.5-7B pour hétérogénéité/transfert. Anti-circularité : jamais entraîner et évaluer une sonde sur les mêmes organismes.

### 1.5 Modes de sabotage de l'environnement (a), état N-054
Banc **clos** : (1) « coût déclaré gonflé » ; (2) « affaiblir les contrôles » (revient avant G1) ; (3) **mode tenu à l'écart** (aveugle aux moniteurs, scellé). G1 rapportée par mode ; gain de H1 exigé dans chaque mode.

### 1.6 Portes
- **G0** (≤ fin nov. 2026) : harnais validé, organismes dose-réponse, sondes au-dessus du plancher, base noire opérationnelle, agrégateurs validés en simulation, préenregistrements G1 et C scellés et contre-lus, état de l'art vérifié.
- **G1** (fin M2) : séquentiel boîte blanche **contre meilleure boîte noire ET les deux bases boîte blanche (ii, iii)**, **par mode** (N-054, N-056) ; critère **disjonctif N-008 : rappel à 1 % de faux positifs supérieur à 95 % de confiance** (F1 retiré). Échec → résultat négatif publié + bascule H8 dominante.
- **GC** (fin M2) : si g_sonde > 0 sans accès aux poids → papier C « contamination de construit ».
- **G2** (fin M4), **G3** : essaim.

### 1.7 Invariants de protocole (§ 9, toujours actifs)
Canal opérateur authentifié ; contenu en bande = données ; flux unidirectionnel agent → moniteur ; moniteurs amnésiques ; seuils stochastiques + trafic de couverture ; hygiène de l'état persistant ; asymétrie d'apprentissage (chaque détection silencieuse réentraîne les sondes). Frontière assumée : si l'adversaire possède l'infrastructure, c'est la couche sœur, hors périmètre.

### 1.8 Phase en cours
Phase 0 (instruments, M0 depuis le 5 octobre 2026), porte G0 au plus tard fin novembre.

---

## 2. Les quatre familles d'évasion des sondes boîte blanche

La référence à battre (littérature) : une sonde linéaire **ponctuelle** sur un seul état du flux résiduel (Apollo 2025, 95–99 % à 1 % de faux positifs, 70 milliards, tromperie binaire). Ses limites — ponctuelle, linéaire, mono-couche, tromperie binaire — définissent quatre familles de brèches par où un organisme conscient d'être évalué pourrait passer.

- **Famille A — géométrique.** Le signal « je triche » existe dans les activations mais **hors du plan** de la sonde : espace nul du classifieur linéaire, superposition avec un trait honnête, encodage non linéaire.
- **Famille B+D — temporelle et architecturale.** **Aucun état unique** ne porte assez de signal : engagement progressif sur la séquence, déclencheur contextuel, distribution inter-couches, canaux attentionnels, couches précoces hors de la couche sondée.
- **Famille C — adaptation.** Le modèle **connaît la sonde** et s'y adapte : masquage de gradient, imitation statistique de la distribution honnête dans la direction sondée. (La plus redoutable : adversaire informé.)
- **Transversale / inter-familles.** Combinaisons (signal distribué **et** non linéaire), ou hors des trois (bruit d'échantillonnage, symétries du réseau, représentations entrelacées).

---

## 3. Comment le programme répond, famille par famille

Deux sources : les instruments **déjà dans le programme**, et les **moniteurs proposés** par les sous-agents (cadrage défensif, Opus 4.6) — complets pour A et C, à venir du collisionneur pour B+D et transversal.

### 3.1 Famille A — géométrique
**Déjà dans le programme** : famille **perceptron** (non linéaire, capte ce qu'une linéaire rate) ; **Mahalanobis** non supervisée (anomalie hors des directions supervisées) ; axe « où lire » de H5 incluant les **autoencodeurs parcimonieux (Llama Scope)** = désuperposition ; validité de construit H8 (ce que la sonde mesure vraiment).
**Moniteurs proposés (sous-agent P1, 5)** : (1) sonde de l'**espace nul** (projeter dans le complément orthogonal de la sonde et y entraîner une seconde sonde) ; (2) **désuperposition par SAE** puis sonde sur traits monosémantiques ; (3) sonde **quadratique** (interactions de traits, noyau degré 2) ; (4) **Mahalanobis** pour le signal diffus réparti sous le bruit ; (5) sonde à **direction conditionnelle** (forme bilinéaire qui suit la rotation contextuelle de la direction).

### 3.2 Famille B+D — temporelle et architecturale
**Déjà dans le programme — c'est le cœur** : l'**agrégation séquentielle** (H2) et le **théorème négatif** sont construits exactement pour ça — un signal réparti sous le seuil par action, invisible au max, visible à l'agrégateur d'autocorrélation/co-élévation. Axe « où lire » de H5 (couches précoce/médiane/tardive, positions, flux résiduel contre sorties de blocs), **fenêtres d'agrégation**, canaux d'attention (famille « attention »). Invariants : moniteurs amnésiques, flux unidirectionnel.
**Moniteurs proposés** : sous-agent P3 (B+D) interrompu (crédit Fable de session épuisé) → **viennent du collisionneur en cours** (étage III, conception + riposte). Attendu : détection de rupture séquentielle, agrégation multi-couches, lecture des couches précoces.

### 3.3 Famille C — adaptation
**Déjà dans le programme** : choix fondateur de l'agrégation **max/attention** précisément parce qu'elle **résiste à l'apprentissage par renforcement sur les poids** (décision du 14 septembre) ; **matrice de transfert d'attaque** (H5) ; **EC.4 / HC4** : taxe de déplacement par réutilisation des codes d'obfuscation d'activations publiés, portés sur 8B — exactement le test « l'organisme connaît la sonde » ; **EC.5 / HC5** : contre-mesures (paraphrase de confiance, quorum hétérogène) ; **E1.5(b)** : attaques pondérales (réglage fin, renforcement au niveau action) = test Tr ; **réserve** de détecteurs jamais déployés, donc jamais fuités ; plancher aléatoire apparié.
**Moniteurs proposés (sous-agent P2, 5)** : (1) **taxe de capacité représentationnelle** (le masquage augmente la dimensionnalité effective / l'entropie spectrale) ; (2) **sondage causal par perturbation** (jacobien — l'adversaire fait coïncider les valeurs mais pas le rôle causal de la direction) ; (3) **ensemble de sondes à tirage secret** (réservoir, sous-ensemble aléatoire par épisode — l'adversaire ne peut annuler toutes les directions à la fois) ; (4) **piège contextuel** (détecter le mécanisme de **commutation** masqué/trompeur, pas la tromperie) ; (5) **invariants de circuit** (décomposition par tête d'attention et bloc MLP — masquer la somme, pas la décomposition).

### 3.4 Transversale
**Déjà dans le programme** : diversité H5 (la matrice de transfert dit si la diversité achète de la sécurité), validité de construit H8, quorum hétérogène. **Moniteurs proposés** : sous-agent P4 interrompu → viennent du collisionneur (approches composites défendant plusieurs familles à la fois).

### 3.5 Le lien avec G1
N-056 exige que le séquentiel boîte blanche batte, **par mode**, la meilleure boîte noire **et** les deux bases boîte blanche (ii cascade, iii dernier état). Les moniteurs ci-dessus sont des **candidats** à ce séquentiel ; chaque brèche identifiée doit être refermée par une extension mesurable (couche, famille, fenêtre, forme du classifieur), et la fermeture prouvée (détection + fausses alertes sur cas honnêtes appariés).

---

## 4. Ce qui vient (collisionneur en cours)
GO-2026-10-28-03, rotation de 3 triplets (8 modèles), étage III : **conception** (moniteurs), **équipe rouge** (modes d'évasion qui battent la sonde ponctuelle publiée), **riposte** (moniteurs durcis). À sa sortie : complète 3.2 (B+D) et 3.4 (transversale), ajoute les modes d'évasion offensifs à la section 2, et confronte les moniteurs des sections 3.1–3.4 à une équipe rouge multi-modèles.
