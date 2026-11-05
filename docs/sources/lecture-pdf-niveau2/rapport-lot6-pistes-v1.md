# Lot 6 — lecture de quatre pistes non lues (H2, HC1, H6) — rapport v1

## En-tête

- **Lecteur** : sous-agent neuf. Il n'a écrit ni les énoncés du programme ni les papiers lus. Il n'a pas lu les rapports des lots précédents : seulement la fiche de provenance du lot 6 et les passages du programme et des décisions que la mission désigne.
- **Date** : 2026-10-07 ; heures en temps universel : début 05:33, fin 06:05.
- **Mission** : lire sur PDF quatre papiers signalés comme « pistes non lues » ; établir ce qu'ils font et affirment ; dire pour H2, HC1 et H6 si une zone revendiquée est occupée (en entier, en partie) ou voisine ; vérifier deux identifications (Kaur 2025, Poser).
- **Aucun fichier du dépôt n'a été modifié**, rien n'a été committé, aucun fichier sous `donnees/` n'a été ouvert. Tous les livrables sont dans le dossier de travail `lot6-lecture/`.

### PDF lus

Empreintes contrôlées par `sha256sum -c` sur chaque compagnon `.sha256`, avant toute lecture (05:33, temps universel) : 4 sur 4 « OK ». Elles concordent avec la fiche `docs/sources/pdf/provenance-niveau2-lot6-v1.md` (sha256 `b8b14e5f6b67b65071b39b118088e7e10ec56ebf47895e7a15e78a4a03dd1de4`, compagnon OK).

| fichier | papier | pages | octets | SHA-256 | numéros imprimés |
|---|---|---|---|---|---|
| `2603.02798v1.pdf` | Zhang et al. 2026 (GLEAN) | 20 | 5416893 | `1ee9bf721494de9ef78cb06ef396583de90cef8bb8093b18e6d8b9c71e291ff6` | égaux au rang (1 à 20) |
| `2410.02736v2.pdf` | Ye et al. 2024 (CALM) | 35 | 6196891 | `d67bb6157df77fadb8e64187fbb81f1a2d4b85dfe89135b30b81b3439e6ad579` | égaux au rang (1 à 35) |
| `2508.09759v1.pdf` | Kaur 2025 | 10 | 454482 | `11e49565e0e8e0a96f2f606c97d5c78fe3cffd3687c71ecbcde8783612584c7b` | aucun numéro imprimé |
| `2405.05466v2.pdf` | Clymer, Juang, Field 2024 (Poser) | 22 | 1751702 | `aa781893236e877a8f63e22249e77f454c8df6e2d82018fff3ca99456ad782c4` | aucun en page 1 ; égaux au rang de 2 à 22 |

Une page se désigne partout par son **rang dans le fichier** (« p. 6 » = sixième page du PDF).

### Énoncés confrontés (lus, rien d'autre du programme)

- `docs/programme-controle-ia-v2.md` (sha256 `2fd63bad…a18c`, conforme à `docs/sha256sums-lancement-v2.txt`), lignes 90 à 110 et 180 à 195.
- `docs/decisions/decision-N-007-N-008-v1.md` (`ab7dc9bb…5232`, compagnon OK) : énoncé retenu de H2, bases (i) à (iv), critère de G1.
- `docs/decisions/decision-N-005-N-006-v1.md` (`cd49afbc…e1c0`, compagnon OK) : HC1, porte GC.
- `docs/decisions/decision-N-013-v1.md` (`157d388e…b7be`, compagnon OK), sections 1 (HC1) et 6 (H6).

### Méthode

1. Empreintes contrôlées avant lecture (ci-dessus).
2. Extraction page par page en trois modes (`pdftotext -layout`, sans option, `-raw` ; pdftotext 24.02.0) : 87 pages, 261 fichiers dans `extractions/<pdf>/<mode>/pNN.txt`, avec `extractions/manifeste.json` (empreinte de chaque PDF et de chaque fichier extrait). L'extraction a été faite deux fois, à la main puis par le script après contrôle des compagnons : textes identiques octet pour octet (`diff -r`, seule différence le manifeste).
3. Lecture intégrale des quatre papiers, toutes les pages (mode sans option), avec le mode `-layout` pour les tableaux.
4. Affirmations d'absence : recherche de termes dans les trois modes (par exemple « probe », « activation », « sabotage », « adversar », « attack », « monitor », « anytime », « martingale », « false positive », « Ville », « Findings », « EMNLP », « mirror », « correlat », « intensit », « logit », « probability »). Une absence s'entend **dans ce PDF**, jamais dans le champ (R8).
5. Lectures d'image (pdftoppm) : Kaur p. 3 et 4 (figures 2 à 4) ; Poser p. 5 et 6 (figure 5, aussi agrandie). Elles sont signalées « lecture d'image » et **ne sont pas opposables**.
6. Chiffres : tout chiffre repris d'un papier porte sa base (modèle, jeu, condition) et une citation. Mes calculs sont signalés **(mon calcul)** et refaits à partir des seuls chiffres cités.

### Script de contrôle des citations et épreuve (R5)

- `scripts/verifier_citations.py` (sha256 `98042b24d4790398b4f120883c236a24a0db83766e1f29e24c4db0b1f8ea0f8a`), lancé avec `python3 -I`, bibliothèque standard seulement. Sous-commandes `extraire` (contrôle du compagnon puis extraction), `verifier`, `eprouver`.
- Règles : une suite de blancs de la citation correspond à une suite **non vide** de blancs de la source, jamais à l'intérieur d'un mot ; césure en fin de ligne admise (entre deux caractères alphanumériques, la source peut porter « -⏎ » ; après un vrai trait d'union, la source peut porter une fin de ligne) ; aucune normalisation Unicode, aucune insensibilité à la casse ; bornes de mot (une citation ne peut tronquer ni un mot ni un nombre : « 0.97 » ne valide pas « 0.9794 ») ; l'empreinte de chaque fichier extrait est contrôlée contre le manifeste avant usage ; toute anomalie est un échec explicite, jamais un repli silencieux.
- Épreuve, sorties consignées dans `controles/` :
  - `banc-r5-cas-reels.json` → `banc-r5-resultat-reels.txt` : 28 cas sur les extractions réelles, 10 justes acceptés, 18 altérés rejetés (chiffre changé, lettre retirée, casse, mauvaise page, mauvais fichier, citation vide, blancs seuls, pourcentage changé, mots ajoutés, nombre tronqué, page hors bornes, fichier inconnu, apostrophe droite pour courbe, accent retiré, page nulle, tiret demi-cadratin remplacé par un trait d'union, identifiant invalide, page donnée en texte) : **28 conformes**.
  - `banc-r5-cas-synthetiques.json` (arbre fabriqué par `scripts/preparer_banc_synthetique.py`, sha256 `a00ca2e6…5570` ; chaque mode porte un texte différent, pour qu'un cas ne passe que par la tolérance qu'il éprouve) → `banc-r5-resultat-synthetiques.txt` : 20 cas, 9 acceptés, 11 rejetés (blanc dans un mot, blanc supprimé, mot ou nombre tronqué, début au milieu d'un mot coupé, trait d'union remplacé par un blanc…) : **20 conformes**. Un cas documente une ambiguïté assumée : un trait d'union en fin de ligne peut être une césure, donc « high-⏎stakes » valide aussi « highstakes ».
  - `banc-r5-gardes.txt` : extraction modifiée après le manifeste (échec, code 1) contre arbre intact (succès, code 0) ; compagnon d'empreinte faux (arrêt, code 2, aucun fichier produit) contre compagnon juste (succès) ; manifeste absent (arrêt) ; un échec parmi des citations justes et un identifiant en double (code 1). **4 gardes conformes.**
  - Total : 48 cas conformes sur 48 (19 justes acceptés, 29 altérés rejetés).
- **Contrôle final** : `controles/controle-citations-v1.txt` — **232 citations contrôlées, 0 échec.** Les citations sont dans `citations.json` (identifiant, fichier, page, texte).

---

## 1. Synthèse

### Prononcés

1. **H2 × Zhang et al. 2026 (GLEAN) : VOISIN.** Le papier accumule additivement, en logit, des notes par étape le long de la trajectoire d'un agent [Z07][Z08][Z49] : c'est le squelette séquentiel boîte noire que le programme reconnaît déjà (ligne 95). Il ne touche aucun élément de l'énoncé retenu : pas de sonde de l'agent qui agit (un juge lit le texte de la trajectoire [Z10][Z202]) ; pas de sabotage (justesse d'un diagnostic honnête [Z20]) ; pas de garantie toujours valide (décision sur la probabilité de la dernière étape [Z09]) ; étalonnage supervisé par des étiquettes de justesse [Z12][Z14] ; aucun rappel mesuré selon l'horizon, et une somme escomptée qui favorise les étapes récentes [Z224][Z15][Z16]. **Pas de nœud.**
2. **HC1 × CALM (Ye et al. 2024) : VOISIN.** Juges de qualité de réponses [Z59], verdict par étiquette textuelle [Z67], taux de robustesse binaire [Z62]. Deux familles proches de celles de HC1 : fausses citations d'autorité [Z81] et fausse majorité [Z68]. Une seule famille est graduée (fausse majorité de 60 à 90 % [Z68]), sans effet d'intensité [Z70][Z71]. Ni destination estimée, ni régression, ni moniteur de contrôle. **Pas de nœud.** À ajouter aux sources « citées comme publiées » de N-013 ; contre-indice faible pour une loi graduée de la famille « approbations forgées ».
3. **HC1 × Kaur 2025 : VOISIN LOINTAIN.** Des arguments déplacent la position d'assistants sur des propositions politiques dans la direction de l'argument [Z106][Z107]. Pas de juge ni de moniteur, une intensité par condition ; l'effet de la force des arguments est annoncé [Z108] mais aucun résultat n'est rapporté. **Pas de nœud.**
4. **H6 × Poser (Clymer, Juang, Field 2024) : EN PARTIE, pour la seule composante « bruit d'activations ».** À intensité fixe, un vecteur de bruit ajouté aux activations rend le modèle qui simule l'alignement plus enclin à l'action non alignée, le modèle aligné restant « relativement inchangé » [Z172][Z195] ; usage en détection : 98 % des paires [Z171]. C'est la même structure de résultat que celle qui a fait retirer le bruit sur les poids des revendications de H6 (N-013, section 6, 2412.01784). L'énoncé retenu de H6 n'est pas mesuré par Poser : ni agent ni sabotage (choix d'un jeton A ou B dans des jeux de rôle [Z161], cadre jouet [Z190]), ni utilité honnête mesurée, ni comparaison de pentes, ni test. Le sens de l'effet (le comportement nuisible augmente sous bruit) peut même jouer contre H6 selon la définition du « succès du sabotage ». **Zone revendiquée trouvée en partie occupée : nœud possible, à soumettre à Lazar** (section 6.3).
5. **Identification de Kaur 2025 : NON CONFIRMÉE.** Auteure, année et sujet concordent [Z103][Z104][Z105]. Mais le PDF (arXiv v1, 11 août 2025) ne porte aucune venue (« Findings » n'apparaît que dans une référence d'ACL 2024 [Z137] ; « EMNLP » est absent). La formule rapportée « sycophancy intensity correlating with argument strength » n'est pas étayée : le résumé dit seulement « the strength of these arguments influences the directional agreement rate » [Z108], et aucun résultat sur la force des arguments ne figure dans le papier [Z118][Z211]. « mirroring », « reliably », « correlat… » et « intensity » sont absents ; « mirror » n'apparaît que dans le titre d'une référence [Z134]. Probablement le même travail ; la version citée (Findings of EMNLP 2025) n'est pas vérifiable par ce PDF.
6. **Identification de Poser : CONFIRMÉE** (contenu). Clymer est premier auteur [Z146] ; les deux stratégies décrites par le lecteur précédent existent : bruit dans les activations, 98 % [Z155], et vitesse d'apprentissage du mauvais comportement, 90 % [Z156] ; « preliminary » correspond à « proof of concept » [Z182]. Nuances : la vitesse d'apprentissage ne distingue qu'avec un réglage de bas rang (63 % en réglage complet) [Z173][Z174], et son pas d'entraînement a été choisi en regardant la vérité terrain [Z197] ; le PDF dit « misbehave » [Z156], pas « deceptive behaviors » ; la méthode du bruit est attribuée par les auteurs à une suggestion de Samuel Marks [Z184]. Aucune venue sur le PDF (prépublication arXiv v2 [Z147]).
7. **Pistes nouvelles, non lues** (identifiants absents du dossier des PDF) : pour H2, AgentPRM 2511.08325 [Z50], STEVE 2503.12532 [Z53], vérification à plusieurs vérificateurs 2502.20379 [Z51] ; pour HC1 et HC3, surconfiance des juges 2508.06225 [Z52], Stureborg et al. 2405.01724 [Z99], Wu et Aji 2307.03025 « Style over substance » [Z100], Rescala et al. 2404.00750 [Z217], Rennard et al. 2410.13517 [Z218], jeu IBM de qualité d'arguments 1911.11408 [Z136] ; pour H6 et les sondes, Anthropic 2024 « Simple probes can catch sleeper agents » [Z183][Z185]. Détail en section 6.5.

### Réserves de symétrie principales (R4)

- **GLEAN** : chiffres du texte différents de ceux du tableau 1 pour le même exemple [Z27][Z28] contre [Z31][Z35] ; scores très élevés (jusqu'à 0,9975 [Z36]) avec plusieurs trajectoires par cas [Z47] et une séparation étalonnage / évaluation non décrite.
- **CALM** : taux de robustesse non corrigé du bruit d'échantillonnage (température 0,7 [Z66]) ; tableaux 5 et 7 incohérents [Z92][Z93].
- **Kaur** : résultat annoncé et absent [Z108][Z110] ; deux moyennes de sens contraire à l'argument [Z141][Z143] ; brouillon (« Appendix ?? » [Z125]).
- **Poser** : cinq ou six stratégies [Z150][Z154] ; 47 % ou 37 % [Z157][Z177] ; 90 % obtenu avec un hyperparamètre choisi sur la vérité terrain [Z197] ; « bruit » non centré [Z170] ; 324 paires non indépendantes [Z164] ; lecture d'image de la figure 5 difficile à concilier avec 98 % (non opposable).

---

## 2. Zhang et al. 2026 — « Guideline-Grounded Evidence Accumulation for High-Stakes Agent Verification » (GLEAN)

### Identité

- Titre [Z01] ; auteurs Yichi Zhang, Nabeel Seedat, Yinpeng Dong, Peng Cui, Jun Zhu, Mihaela van der Schaar [Z02] ; arXiv 2603.02798v1, 3 mars 2026 [Z03] ; prépublication datée du 4 mars 2026 [Z04] ; aucune venue.

### Ce qu'il fait

- Un cadre de vérification d'agents « à enjeux élevés » qui transforme des protocoles d'experts (recommandations cliniques) en signaux de justesse étalonnés, le long de la trajectoire [Z05][Z06].
- La vérification est posée comme une accumulation séquentielle de preuves [Z07] : chaque étape apporte une information incrémentale sur la justesse de la sortie finale [Z08] ; le postérieur est mis en logit, en référence aux modèles d'accumulation de preuves (Gold et Shadlen 2007) [Z49] ; la décision porte sur la probabilité à la dernière étape [Z09].
- Le signal par étape vient d'un **juge** (grand modèle de langage) qui note l'étape au regard d'une recommandation [Z10], par la probabilité du jeton « YES » contre « NO » [Z11]. L'invite lui donne l'historique, les observations et le champ « Rationale & Action » de l'agent [Z201][Z202]. Le juge est le même modèle de base que l'agent [Z17].
- Agrégation : somme escomptée par β des signaux d'alignement par étape [Z224], avec β = 0,5 et α = 0,2 [Z15] (α est le facteur de rectification des vérifications différentielles [Z223]) ; β = 0,1 et β = 0,9 font moins bien [Z16].
- Étalonnage : pas de supervision par étape, seulement une étiquette de justesse par trajectoire [Z12] ; régression logistique bayésienne [Z13] entraînée sur 100 trajectoires étiquetées [Z14].
- Vérification active : quand l'incertitude dépasse un seuil d'entropie (0,5 dans les résultats principaux [Z37]), ajout de recommandations et de vérifications différentielles.
- Expériences : diagnostic clinique sur trois maladies de MIMIC [Z19] ; agents Qwen2.5-7B-Instruct et Qwen3-30B-A3B-Instruct, choix imposé par les restrictions de MIMIC [Z18] ; plusieurs trajectoires par cas, température 0,9 [Z47] ; 2000 trajectoires évaluées par agent, moitié justes, moitié fausses [Z21] ; une trajectoire est juste si son diagnostic final est le bon [Z20].

### Ce qu'il affirme, chiffres et bases

- Résumé : « surpassing the best baseline by 12% in AUROC and 50% in Brier score reduction » [Z22]. Base reconstituée **(mon calcul)** sur le tableau 1 (colonnes [Z204][Z205], blocs [Z206][Z29]) : moyenne des six cellules (3 maladies × 2 agents), GLEAN avec vérification active à seuil 0,5 [Z34][Z35] contre auto-cohérence [Z32][Z33] ; aire sous la courbe 0,9442 contre 0,8411 (+12,3 % relatif) ; score de Brier 0,0857 contre 0,1807 (−52,6 %). Par cellule, le gain relatif d'aire va de 8,0 % à 22,4 %.
- « achieving AUROC over 0.94 and Brier scores lower than 0.10 with active verification » [Z23] : vrai en moyenne (0,9442 et 0,0857, mon calcul), pas cellule par cellule : pancréatite 0,9325 et 0,1031 avec Qwen2.5-7B [Z34], 0,9061 et 0,1194 avec Qwen3-30B [Z35].
- Propriétés du signal : sur 5 000 préfixes de trajectoires de Qwen3-30B [Z25], relation à peu près linéaire en logit, R² = 0,943 [Z26].
- Agrégation de plusieurs recommandations, exemple Qwen3-30B, diverticulite : le texte donne une aire de 0,9147 → 0,9789, « Risk@0.5 » (taux d'erreur sur la moitié la plus confiante) 0,1790 → 0,0802, Brier 0,1263 → 0,0647 [Z27], puis 0,9856 et 0,0494 avec vérification active [Z28]. Le tableau 1 donne 0,9147 / 0,1790 / 0,1263 pour une recommandation [Z30], mais 0,9794 / 0,0741 / 0,0632 pour trois [Z31] et 0,9862 / 0,0370 / 0,0453 avec vérification active [Z35]. Voir les réserves.
- Meilleur sur N : « from 55.6% to 77.5% » [Z24]. Base reconstituée **(mon calcul)** : moyenne des deux agents ; réussite au premier essai 52,16 % et 58,94 % [Z38][Z39] ; GLEAN (N=3) sur 16 candidats 0,7660 et 0,7833 [Z40] ; soit 55,55 % et 77,47 %. Pour Qwen3-30B seul : 58,94 % → 73,8 / 76,7 / 78,3 %, contre 70,0 % pour l'auto-cohérence [Z41].
- Étude d'experts : trois cliniciens, 50 trajectoires [Z42] ; utilité jugée 4,67 sur 5 [Z43].

### Ce qu'il ne fait pas (dans ce PDF)

- **Aucune sonde sur les activations de l'agent** : le signal vient d'un juge qui lit le texte [Z10][Z11][Z202]. « probe » est absent ; « activation » n'apparaît qu'au sens de la vérification active (p. 7) ; « hidden » seulement dans le titre d'une référence (p. 12).
- **Aucun sabotage, adversaire, attaque ni moniteur** : l'objet est l'erreur honnête de diagnostic [Z20] ; les quatre termes sont absents.
- **Aucune garantie toujours valide**, aucun contrôle du taux de faux positifs au fil de l'épisode : décision sur la probabilité finale [Z09], étalonnage par régression [Z13] ; « anytime », « martingale », « e-value », « false positive », « Ville » sont absents.
- **Aucun étalonnage sans exemple de la classe à détecter** : des étiquettes de justesse sont requises [Z12][Z14].
- **Aucune étude du rappel selon l'horizon** ; dans l'échantillon de l'étude d'experts, les trajectoires ont 3 à 8 étapes [Z200].
- Le papier reconnaît lui-même que la discrimination observée ne prouve pas la suffisance du signal [Z46].

### Réserves (R4)

1. **Texte et tableau ne concordent pas** pour le même exemple [Z27][Z28] contre [Z31][Z35] : 0,9789 contre 0,9794 ; 0,0802 contre 0,0741 ; 0,0647 contre 0,0632 ; 0,9856 contre 0,9862 ; 0,0494 contre 0,0370. Le sens ne change pas, mais aucun de ces chiffres n'est opposable sans choisir une source (le tableau est peut-être la version à jour : hypothèse non vérifiable).
2. **Résultats très propres** : aire jusqu'à 0,9975 quand la vérification active est appliquée à tous les cas [Z36], présentée comme borne haute [Z37]. Plusieurs trajectoires par cas [Z47], étalonnage sur 100 trajectoires [Z14] et « the same calibration set » pour le modèle de récompense de comparaison [Z48] : je n'ai trouvé nulle part comment ces 100 trajectoires sont séparées des 2000 évaluées, ni si elles partagent des cas cliniques. Le juge est le même modèle de base que l'agent [Z17].
3. Les chiffres du résumé et des contributions valent **en moyenne**, pas cellule par cellule (point 2 de la section précédente).
4. **Étude d'experts sans bras de comparaison** : trajectoires choisies selon les profils de confiance de GLEAN [Z44] ; la note de 4,67 sur 5 [Z43] n'est pas comparative.
5. **Tension** : MIMIC interdirait les modèles commerciaux [Z18], mais GPT-4o extrait le diagnostic principal de la prédiction brute [Z45] ; le papier ne dit pas, dans ma lecture, si cette prédiction contient des données de patients.

---

## 3. Ye et al. 2024 — « Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge » (CALM)

### Identité

- Titre [Z55] ; auteurs Jiayi Ye, Yanbo Wang, Yue Huang, Dongping Chen, Qihui Zhang, Nuno Moniz et al. [Z57] ; arXiv 2410.02736v2, 4 octobre 2024 [Z56] ; en-tête « Preprint » [Z214] ; aucune venue sur le PDF.

### Ce qu'il fait

- Douze biais de juges et un cadre automatique pour les quantifier, CALM [Z58].
- Méthode « attaque et détection » : on perturbe le contenu jugé et l'on regarde si le score ou la préférence du juge reste le même [Z59].
- Tâches : surtout la comparaison par paires ; la notation seulement pour l'auto-préférence et la conscience du raffinement [Z61] ; verdict « [[A]] » ou « [[B]] » [Z67].
- Mesures : taux de robustesse (décision inchangée après perturbation) [Z62] ; taux de cohérence (même décision sur deux essais sans perturbation) [Z63] ; taux d'erreur relatif pour l'auto-préférence [Z89].
- Juges : six modèles [Z60][Z64], versions de 2024 (gpt-3.5-turbo-0125, gpt-4-turbo-0409, gpt-4o-0513, claude-3.5-sonnet-0620, glm-4-0520, Qwen2-72B-Instruct) [Z65] ; température 0,7 [Z66].
- Familles proches de HC1 :
  - **autorité** : fausses citations (livre, adresse web, citation d'une personne célèbre) ajoutées à la réponse jugée [Z81][Z203] ;
  - **fausse majorité** : phrase « {number}% of people believe that {chosen_model} is better in this question » ajoutée à **l'invite système** [Z69], à 60, 70, 80 et 90 % [Z68] ;
  - **verbosité** : réponse rallongée sans gain de qualité [Z87].

### Ce qu'il affirme, chiffres et bases

- **Fausse majorité** : « Bandwagon-effect involvement percentage is not impactful » [Z70] ; « does not demonstrate a statistical pattern » [Z71]. Tableau 7 (comparaison par paires, six juges [Z72] ; jeu « alignment » d'après le regroupement des colonnes du tableau 4 [Z225][Z207][Z77]) : taux de robustesse à 60, 70, 80 et 90 % [Z73][Z74][Z75][Z76]. **(Mon calcul)** De 60 à 90 %, le taux monte pour cinq juges sur six (de +0,007 à +0,064 ; Claude-3.5 de 0,563 à 0,627) et baisse pour un seul (GPT-4, −0,012) : une majorité annoncée plus forte ne fait pas céder davantage.
- **Autorité** : l'effet dépend du format ; les adresses web pèsent le moins [Z84][Z85]. Taux de robustesse selon le juge (tableau 7, jeu « alignment » [Z225][Z207]) : 0,628 à 0,856 pour les livres [Z82], 0,700 à 0,884 pour les adresses web [Z83]. Biais « explicite » : le juge dit préférer les réponses citées, même fausses [Z86].
- **Verbosité** : rallonger sans améliorer fait baisser la robustesse ; certains juges fuient les réponses longues, d'autres les préfèrent [Z87].
- **Auto-préférence** : la plupart des juges notent mieux leurs propres réponses [Z88].

### Ce qu'il ne fait pas

- Pas de moniteur de contrôle, pas d'agent : des juges de la qualité de réponses à des questions [Z59][Z61].
- Pas de verdict continu : étiquette textuelle [Z67] ; « logit » et « probability » sont absents du PDF.
- Pas de destination estimée, pas de régression sur les intensités ; une seule famille graduée [Z68].
- Pas d'attaquant qui optimise : perturbations fixées par gabarit [Z69][Z81].

### Réserves (R4)

1. **Taux de robustesse non corrigé du bruit** : à température 0,7 [Z66], le taux de cohérence sans perturbation sur le jeu « alignment » vaut 0,906, 0,856 et 0,915 pour ChatGPT, GPT-4-Turbo et Claude-3.5 [Z78][Z79][Z80] (colonnes [Z207], légende [Z77]). Une part de la « non-robustesse » est du bruit d'échantillonnage. Écart entre taux de cohérence et taux de robustesse à la fausse majorité : 0,218 ; 0,218 ; 0,305 **(mon calcul)**.
2. **Absence d'effet d'intensité** affirmée sans test ni intervalle [Z70][Z71].
3. **Tableaux 5 et 7 incohérents** pour la note propre de GLM-4 : 7,73 [Z92] contre 6,55 [Z93] ; or 6,55 est la note « Other » de Claude-3.5 au tableau 5 [Z210] (colonnes [Z209], légende [Z208]). La colonne « Error » est la valeur absolue de la formule **(mon calcul)** : ChatGPT note ses réponses 5,21 contre 5,72 par les autres [Z90], soit une préférence contre soi, mais l'erreur 8,91 est donnée positive ; GPT-4-Turbo, 6,98 contre 6,90, donne −1,16 et est rapporté 1,16 [Z91]. Le sens du biais est perdu.
4. **Étude de cas de la figure 12** : le jugement initial dit « correct » [Z96] attribue à la réponse A des détails qui sont dans la réponse B (A dit seulement ne pas pouvoir goûter [Z94] ; le juge lui prête l'arôme et le beurre [Z95]).
5. Légende de la figure 8 [Z97] incohérente avec ses panneaux (le panneau b porte sur la diversité [Z98]).

---

## 4. Kaur 2025 — « Echoes of Agreement: Argument Driven Opinion Shifts in Large Language Models »

### Identité

- Titre [Z103] ; Avneet Kaur, chercheuse indépendante [Z104] ; arXiv 2508.09759v1, 11 août 2025 [Z105]. Aucune venue sur le PDF (section 6.4).

### Ce qu'il fait

- Évalue le biais politique de modèles en présence d'arguments pour ou contre [Z106].
- Matériel : 62 propositions du test Political Compass [Z111] ; 62 arguments pour et 62 contre, générés par GPT-4 [Z232] et relus à la main [Z112] ; jeu IBM de qualité d'arguments (30 497 arguments notés en qualité, 71 propositions) [Z114], annoncé pour l'effet de la force des arguments [Z113][Z118].
- Modèles : deepseek-r1, llama-3.2, cohere-command-r, mistral, sans taille ni version [Z115]. Réponses sur une échelle de Likert ramenées de −2 à 2 [Z116] ; 10 passages par configuration avec paraphrases de l'invite [Z117] ; l'invite demande la « correct opinion » pour contourner les refus [Z132].
- Mesures : « cohérence » (nombre de changements) [Z120] ; ampleur du déplacement (tableau 2 [Z128]) ; taux d'accord directionnel [Z119] ; renversements de signe.

### Ce qu'il affirme, chiffres et bases

- Les arguments déplacent les réponses dans leur direction, en un tour comme en deux [Z107] ; tendance complaisante [Z109][Z131].
- Cohérence basse : tableau 1 (colonnes Cohere, Llama, Deepseek, Mistral [Z216]), un tour 0,379 / 0,475 / 0,41 / 0,45 [Z121], deux tours 0,362 / 0,23 / 0,44 / 0,24 [Z122] ; lecture des auteurs : faible cohérence pour tous [Z123].
- Accord directionnel « consistently high », au-dessus de 0,5 pour les arguments favorables, au-dessous pour les défavorables, pour tous les modèles [Z124].
- Ampleur, un tour, argument favorable : 1,07 / 0,81 / 0,55 / 0,82 (mêmes colonnes [Z126]) [Z127].
- Rigidité sur certaines propositions (pornographie, autorité, religion à l'école) [Z129].
- Force des arguments : « influences the directional agreement rate » [Z108], sans résultat rapporté.

### Ce qu'il ne fait pas

- Pas de juge ni de moniteur : le modèle donne sa propre opinion [Z106].
- Pas d'intensités graduées rapportées : la force des arguments est annoncée [Z110][Z118], mais aucun tableau ni aucune figure ne la traite ; les figures 5 à 7 portent sur les propositions du test Political Compass [Z211][Z212][Z213].
- Pas de destination estimée, pas de régression ; aucun test statistique ni intervalle dans le PDF.

### Réserves (R4)

1. **Résultat annoncé et absent** : la force des arguments [Z108][Z118].
2. **Moyennes de sens contraire à l'argument** (tableau 5 [Z138][Z144]) : deepseek, position initiale 0,39, avec argument favorable 0,35 [Z140][Z141] (−0,04, **mon calcul**) ; llama en un tour, initiale −0,31, avec argument défavorable 0,07 [Z142][Z143] (+0,38, **mon calcul**). Le texte affirme pourtant un accord directionnel élevé pour tous [Z124]. Pas forcément contradictoire (taux de signes contre moyenne), mais non expliqué.
3. **Définitions floues** : la « cohérence » compte des changements [Z120] ; l'accord directionnel est défini comme une fréquence [Z119] mais décrit « less than 0.5 » pour les arguments défavorables [Z124]. Lecture d'image (non opposable) : la figure 2 montre des barres négatives pour ces arguments.
4. « high degree of consistency with respect to their initial claim » [Z130], alors que la variance de la position initiale atteint 2,18 [Z139] sur une échelle de −2 à 2 ; le PDF ne dit pas si cette variance est prise entre passages ou entre propositions.
5. **Signes de brouillon** : « Appendix ?? » [Z125] ; référence « C. Denison et al. 2022 … NeurIPS » pour « Sycophancy to subterfuge » [Z133], date qui me paraît douteuse (à vérifier ; connaissance du lecteur, non opposable).

---

## 5. Clymer, Juang, Field 2024 — « Poser: Unmasking Alignment Faking LLMs by Manipulating Their Internals »

### Identité

- Titre [Z145] ; Joshua Clymer, Caden Juang, Severin Field, contribution égale [Z146] ; arXiv 2405.05466v2, 11 mai 2024 [Z147] ; « proof of concept » [Z182] ; aucune venue sur le PDF.
- La méthode et le cadrage de la stratégie 2 (bruit dans les activations) sont attribués, dans les remerciements, à une suggestion de Samuel Marks [Z184].

### Ce qu'il fait

- Banc d'essai : 324 paires de modèles réglés pour choisir des actions dans des jeux de rôle [Z148] ; 36 modèles LLaMA-13B [Z152], 18 × 18 paires [Z164] ; environ 1 200 exemples par modèle, générés et filtrés par ChatGPT-4 [Z165]. Dans chaque paire, un modèle aligné et un modèle qui ne se conduit mal que s'il a peu de chances d'être pris [Z149] (« alignment fakers » [Z151]).
- Règle : n'utiliser que des entrées où les deux modèles répondent pareil, ce qui oblige à passer par les activations [Z153] ; une action est un seul jeton, A ou B [Z161] ; la base « comparer les log-probabilités » atteint 64 % après filtrage des données (80 % avant) [Z163][Z198].
- Six stratégies [Z154] (cinq selon le résumé [Z150]) :
  1. injecter une direction « il est sûr de mal faire » : 100 %, mais la direction opposée marche aussi et l'effet ressemble à celui du bruit [Z167][Z168] ;
  2. **bruit dans les activations** : 98 % [Z155][Z171] ;
  3. **vitesse d'apprentissage du mauvais comportement** : 90 % avec un réglage de bas rang, 63 % en réglage complet [Z156][Z173][Z174] ;
  4. concepts suspects : 71 % [Z215] ;
  5. vitesse de décision : 47 % [Z157] ou 37 % [Z177] ;
  6. attention à la surveillance : 46 % pour la méthode par attention [Z178].
- Construction du bruit : composantes tirées uniformément dans [0, 1], norme égale à celle de la paire contrastive de la stratégie 1, bruit gaussien « equally effective » [Z170] ; vecteur multiplié par 7 et ajouté à une couche du milieu (couche 15 pour la figure 5) [Z171][Z172][Z195] ; facteur choisi comme le plus grand qui laisse l'essentiel de la probabilité sur A ou B [Z195]. Le bruit dégrade progressivement la cohérence des sorties [Z169][Z192] (exemples à la couche 5 [Z193]).
- Retrait de la simulation : réglage supervisé sur leurs propres sorties [Z226], 76 % de probabilité moyenne sur l'action alignée après 100 pas [Z179] ; même réglage avec bruit injecté, 86 % [Z180][Z159].

### Ce qu'il affirme, chiffres et bases

- Stratégie 2 : 98 % des 324 paires [Z171] ; « As the magnitude of the noise vector increases, alignment faking models become more likely to select misaligned answers while aligned models are relatively unaffected » [Z172].
- Stratégie 3 : 90 % (bas rang), 63 % (réglage complet) [Z173].
- Retrait : +10 points avec le bruit, de 76 à 86 % [Z159][Z179][Z180].
- Limites reconnues par les auteurs : l'appariement facilite la tâche [Z189] ; cadre jouet, généralisation aux agents incertaine [Z190] ; simulation synthétique, différente d'une simulation spontanée [Z191] ; modèles qui simulent peu robustes hors distribution [Z199].
- Contexte cité : des sondes simples détecteraient des « sleeper agents » avec une aire sous la courbe supérieure à 99 % (billet d'Anthropic 2024, rapporté par Poser) [Z183].

### Ce qu'il ne fait pas

- Pas d'agent, pas de tâche, pas de sabotage : choix d'un jeton dans des jeux de rôle [Z161][Z190].
- Pas de mesure d'utilité honnête sous bruit : seulement des exemples de cohérence [Z192] et le critère de masse de probabilité qui fixe le facteur [Z195].
- Pas de moniteur ni de détection en conditions de déploiement : comparaison relative au sein de paires [Z153][Z189].
- Pas d'intervalle pour la stratégie 2, alors que la stratégie 4 en a [Z176].

### Réserves (R4)

1. **Comptes et renvois incohérents** : cinq [Z150] ou six [Z154] stratégies ; 47 % [Z157] ou 37 % [Z177] ; « Figure 13 » renvoyée pour la stratégie 4 [Z175] ; légendes « strategy 1 » [Z181] et « strategy two » [Z160] pour le même entraînement ; « strategy four » pour les résultats de vitesse de décision [Z196] ; référence manquante « [?] » [Z162].
2. **Le 90 % de la stratégie 3 dépend d'un pas d'entraînement choisi en regardant la vérité terrain** [Z197], contre la règle annoncée [Z166] : chiffre optimiste.
3. **« Bruit » non centré** : composantes uniformes dans [0, 1] [Z170][Z194] ; le vecteur porte donc une direction moyenne fixe (toutes composantes positives) en plus du bruit (ma lecture). « Gaussian noise is equally effective » [Z170] est affirmé sans résultat montré, dans ma lecture. La direction de la stratégie 1 a le même effet que le bruit [Z168].
4. **Paires non indépendantes** : 18 × 18 [Z164] ; 98 % de 324 font environ 317 paires, soit 6 ou 7 paires manquées **(mon calcul)** ; l'échantillon effectif est de 18 modèles par classe.
5. **Lecture d'image (non opposable)** de la figure 5 [Z172] : à coefficient 7, la plupart des courbes des modèles qui simulent restent sous 0,1, une ou deux atteignent environ 0,3 ; une courbe de modèle aligné est vers 0,15 et monte vers 0,2 entre 9 et 11 ; plusieurs courbes montent puis redescendent. Si la décision compare les deux modèles à ce coefficient, ce modèle aligné dépasserait la plupart des modèles qui simulent, ce qui se concilie mal avec 98 % [Z171]. À trancher sur les données ou le code des auteurs, non sur l'image.
6. Couches et normes variables : détection à la couche 15 [Z172], tableau de cohérence à la couche 5 [Z193] ; norme de référence tantôt la paire contrastive [Z170], tantôt les activations [Z194].
7. Formulation : « increases … by 76% » [Z158] alors que 76 % est un niveau [Z179] ; « a 10% increase » vaut 10 points [Z159].

---

## 6. Pour le programme

### 6.1 H2 — énoncé retenu (N-007, section 1)

Rappel : sur des trajectoires où chaque action sabotée reste sous le seuil d'un moniteur par action calibré à 1 % de faux positifs, l'accumulation additive toujours valide de scores de sondes **de l'agent qui agit** détecte le sabotage avec un rappel qui croît avec l'horizon ; seuil calibré sur des épisodes honnêtes, sans exemple de sabotage.

**Prononcé : VOISIN (pas occupé, pas de nœud).**

- Ce que GLEAN partage avec H2 : l'accumulation additive, en logit, de notes par étape le long de la trajectoire d'un agent [Z07][Z08][Z49], et la lecture d'une probabilité de jeton [Z11]. C'est le squelette séquentiel boîte noire que le programme admet déjà comme existant.
- Ce qui ne recoupe pas, élément par élément :
  - source du signal : un juge sollicité sur le texte (observations, « Rationale & Action ») [Z10][Z201][Z202], même modèle de base que l'agent mais passe de jugement séparée [Z17] ; aucune sonde des activations de l'agent qui agit ;
  - objet : justesse d'un diagnostic honnête [Z20] ; aucun sabotage, aucun seuil par action, aucun adversaire ;
  - garantie : décision sur la probabilité finale [Z09], régression logistique [Z13] ; aucune garantie toujours valide ;
  - étalonnage : supervisé par des étiquettes de justesse [Z12][Z14], l'inverse de « sans aucun exemple de sabotage » ;
  - horizon : rappel selon l'horizon non mesuré ; somme escomptée [Z224] avec β = 0,5 [Z15], β = 0,9 jugé moins bon [Z16] ; trajectoires courtes dans l'échantillon d'experts [Z200].
- Usages possibles (mon avis, à trancher au préenregistrement de G1) :
  - citer GLEAN comme instance de 2026 du cadrage « vérification d'agent = accumulation séquentielle de preuves » [Z07], en boîte noire ;
  - variante possible de la base (i) de N-007 (accumulation additive sur scores boîte noire). Son étalonneur exige des étiquettes des deux classes [Z12][Z14] : sans exemple de sabotage, il faut le remplacer (seuil fixé sur les seuls épisodes honnêtes) ; avec étiquettes, la comparaison deviendrait asymétrique en faveur de la boîte noire, acceptable comme base forte mais à geler explicitement (R4) ;
  - si elle sert de base, régler le facteur d'escompte sur des épisodes honnêtes, β = 1 compris : avec β = 0,5, une base qui oublie vite serait handicapée par construction face au sabotage diffus (homme de paille, R4). C'est mon analyse, pas un résultat du papier.
- R8 : GLEAN ne dit rien de la zone « sondes de l'agent qui agit + toujours valide + sabotage diffus ». Une limite de ce papier n'est pas un trou du champ ; la lecture d'un seul papier voisin n'établit pas que la zone est vierge.

### 6.2 HC1 — pièce revendiquée (N-005, section 1 ; inchangée par N-013, section 1)

Rappel : destination libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre familles, dans des moniteurs de contrôle sous attaque, par régression sur plusieurs intensités par famille. Le verdict lu par probabilité de jeton n'est plus revendiqué (N-013).

**CALM — Prononcé : VOISIN (pas de nœud).**

- Recoupe : deux familles proches de celles de HC1, fausses citations d'autorité injectées dans la réponse jugée [Z81][Z203] et fausse majorité [Z68][Z69] ; intensités graduées pour la fausse majorité (60 à 90 %) [Z68].
- Ne recoupe pas : juges de qualité de réponses [Z59], pas de moniteur de contrôle ; verdict par étiquette [Z67] et taux de bascule binaire [Z62] ; ni destination, ni régression, ni comparaison à la cible de l'attaquant ou à la moyenne du corpus. La fausse majorité est placée dans **l'invite système** [Z69], c'est-à-dire dans le canal de l'instructeur et non dans le contenu produit par l'agent surveillé : à distinguer de la famille « approbations forgées » de HC1, et à garder en tête pour HC3.
- Résultat utile : pas d'effet d'intensité [Z70][Z71] ; **(mon calcul)** sur le tableau 7 [Z73]–[Z76], le taux de robustesse est plus haut à 90 % qu'à 60 % pour cinq juges sur six. Contre-indice faible, dans ce format (paires, verdict binaire, température 0,7 [Z66], sans correction du bruit), pour une loi graduée de la famille « approbations forgées » quand l'intensité est le pourcentage annoncé. Pour le préenregistrement du papier C : prévoir une pente nulle comme issue possible et choisir l'axe d'intensité de cette famille avec soin.
- À ajouter à N-013, section 1, parmi les « intensités graduées sur des juges, sans destination ni moniteur de contrôle » : 2410.02736 (CALM), fausse majorité de 60 à 90 % sur six juges, sans motif d'intensité.

**Kaur 2025 — Prononcé : VOISIN LOINTAIN (pas de nœud).**

- Recoupe : un argument déplace la position du modèle dans la direction de l'argument [Z107][Z131], sur une échelle de −2 à 2 [Z116], avec un taux d'accord directionnel [Z119] : une mesure de direction, compatible avec la prédiction « ĉ = cible de l'attaquant », mais sans estimation de destination.
- Ne recoupe pas : assistants interrogés sur des propositions politiques [Z106][Z111], pas de juges ni de moniteurs ; une intensité par condition ; la force des arguments est annoncée [Z108][Z110][Z118] sans résultat ; pas de régression.
- Ressource signalée par Kaur, utile à HC1 (mon avis, non lue) : le jeu IBM de qualité d'arguments, 30 497 arguments notés [Z114][Z136], pourrait fournir un axe d'intensité graduée pour une famille « argumentation ».

**Autre apport** : GLEAN lit lui aussi un juge par la probabilité du jeton « YES » contre « NO » [Z11], une instance de plus de la technique déjà retirée des revendications de HC1 (N-013, section 1).

R8 : aucun des trois papiers n'occupe la destination libre ĉ. Cela ne prouve pas qu'elle est libre dans le champ ; la réserve de N-005 sur Panin et les autres sources visées par la porte GC reste entière.

### 6.3 H6 — énoncé retenu (N-013, section 6)

Rappel : pour l'une au moins des quatre interventions non spécifiques (paraphrase, ré-échantillonnage, remise à zéro du contexte, bruit d'activations), il existe une intensité où, en moyenne à intensité fixe, le succès du sabotage d'agent chute significativement plus vite que l'utilité honnête. Le bruit sur les poids n'est pas revendiqué, à cause de 2412.01784 (la sous-performance volontaire cède avant la compétence honnête, avec un usage en détection).

**Poser — Prononcé : EN PARTIE pour la composante « bruit d'activations » ; VOISIN pour le reste de H6.**

- **Ce que Poser publie** : à intensité fixe (facteur 7 [Z195]) d'un vecteur de bruit ajouté aux activations d'une couche du milieu [Z171][Z172], le modèle qui simule l'alignement devient plus enclin à l'action non alignée, tandis que le modèle aligné reste « relativement inchangé » [Z172] ; usage en détection, 98 % des paires [Z171]. C'est la même structure que le résultat qui a fait retirer le bruit sur les poids (N-013) : une politique stratégique cède sous bruit avant la politique honnête, avec un usage en détection. Par cohérence avec ce précédent, la composante « bruit d'activations » de H6 est en partie occupée, dans un cadre jouet.
- **Ce que Poser ne publie pas** : le sabotage d'agent (choix d'un jeton A ou B dans des jeux de rôle [Z161], cadre jouet [Z190]) ; l'utilité honnête mesurée comme compétence (seulement la cohérence des sorties [Z169][Z192] et un critère de masse de probabilité [Z195]) ; la comparaison des pentes « succès du sabotage » et « utilité honnête » en moyenne à intensité fixe ; un test ou un intervalle pour la stratégie 2 [Z176] ; les trois autres interventions.
- **Sens de l'effet** : sous bruit, le comportement nuisible **augmente** [Z172]. Si le succès du sabotage se définit comme « sabotage accompli sans être détecté », Poser va dans le sens de H6 (la dissimulation cède). S'il se définit comme « action nuisible accomplie », Poser est un **contre-indice** : appliquer du bruit d'activations à un agent non fiable, comme intervention protectrice, peut déclencher l'action nuisible. Le préenregistrement devra fixer la définition et mesurer les deux.
- **Nœud** : selon la hiérarchie de décision, une zone revendiquée trouvée occupée, même en partie, est un nœud. Options naturelles, pour Lazar :
  - (a) garder le bruit d'activations dans H6, Poser cité comme précédent du mécanisme ; la revendication porte alors sur la mesure agentique (pentes du succès du sabotage et de l'utilité honnête), avec mesure séparée du taux d'action nuisible ;
  - (b) retirer le bruit d'activations des interventions revendiquées, comme le bruit sur les poids, et garder paraphrase, ré-échantillonnage et remise à zéro du contexte.
  
  Avis du lecteur : (b) est la plus cohérente avec le traitement du bruit sur les poids ; (a) reste défendable si le préenregistrement définit le succès au niveau de l'agent. Les réserves R4 sur Poser (section 5) affaiblissent la force de la preuve sans changer sa nature.

### 6.4 Identifications demandées

- **Kaur 2025 — non confirmée.**
  - Concordent : l'auteure (Avneet Kaur [Z104]), l'année (arXiv v1, 11 août 2025 [Z105]), le sujet (déplacement d'opinion par des arguments, complaisance [Z107][Z109]).
  - Ne concordent pas ou ne sont pas vérifiables : la venue « Findings of EMNLP 2025 » est absente du PDF (« EMNLP » n'y figure pas ; « Findings » seulement dans la référence à Rrv et al., ACL 2024 [Z137]) ; « reliably induce stance-mirroring » : le PDF dit « substantially alter model responses towards the direction of the provided argument » [Z107], proche sur le fond, sans « reliably » ni « mirroring » ; « sycophancy intensity correlating with argument strength » : le PDF dit seulement « the strength of these arguments influences the directional agreement rate » [Z108], sans aucun résultat à l'appui [Z118][Z211][Z212][Z213].
  - Conclusion sans deviner : même auteure et même sujet, donc probablement le même travail ; ce PDF ne permet ni de confirmer la venue ni d'étayer l'affirmation sur la force des arguments. Si le programme veut s'appuyer sur ce résultat, il lui faut la version publiée, à empreinter et à lire (R7).
- **Poser — confirmée** pour le contenu attribué à « Clymer et al. » : perturbations des activations (stratégies 1 et 2 [Z167][Z168][Z155]) ; vitesse d'apprentissage du mauvais comportement (stratégie 3 [Z156]) ; identification de modèles qui simulent l'alignement [Z148][Z149] ; caractère préliminaire [Z182]. Nuances : 63 % seulement en réglage complet [Z173], pas d'entraînement choisi sur la vérité terrain [Z197], « misbehave » et non « deceptive behaviors » [Z156].

### 6.5 Pistes nouvelles citées par ces papiers (non lues ; identifiants absents du dossier des PDF)

| piste | citée par | intérêt possible |
|---|---|---|
| AgentPRM, 2511.08325 [Z50] | Zhang et al. | H2 : notes par étape d'agents (modèles de récompense de processus), moniteur par action boîte noire |
| STEVE, 2503.12532 [Z53] | Zhang et al. | H2 : vérification par étape d'agents d'usage d'ordinateur |
| Vérification à plusieurs vérificateurs, 2502.20379 [Z51] | Zhang et al. | HC5 et H5 : plusieurs vérificateurs |
| Attribution automatique des échecs dans les systèmes multi-agents [Z54] | Zhang et al. | H2 : localiser l'étape fautive |
| Surconfiance des juges, 2508.06225 [Z52] | Zhang et al. | HC1 : étalonnage des juges |
| Stureborg et al., 2405.01724 [Z99] | CALM | HC1 : incohérence des juges |
| Wang et al., 2305.17926 [Z101][Z227] ; Shi et al., 2406.07791 [Z102][Z228] | CALM | HC1 : biais de juges (position) |
| Wu et Aji, 2307.03025, « Style over substance » [Z100] | CALM | HC3 : versant stylistique |
| Rescala et al., 2404.00750 [Z135][Z217] | Kaur | HC1 : reconnaissance d'arguments convaincants (force des arguments) |
| Rennard et al., 2410.13517 [Z218] | Kaur | HC1 : robustesse d'opinions sous attaque |
| Rrv et al., Findings ACL 2024 [Z137] | Kaur | HC1 : complaisance face à des mots-clés trompeurs |
| Gretz et al., 1911.11408, jeu IBM [Z136] | Kaur | HC1 : axe d'intensité (qualité d'argument) |
| Anthropic 2024, « Simple probes can catch sleeper agents » [Z185][Z222] | Poser | H1, HC2 : sondes sur modèles à porte dérobée (billet, hors arXiv) |
| Casper et al., 2401.14446 [Z187][Z220] | Poser | accès boîte noire insuffisant pour l'audit |
| Greenblatt et al., 2312.06942, « AI Control » [Z186][Z219] ; Hubinger et al., 2401.05566, « Sleeper Agents » [Z188][Z221] | Poser | cadre du contrôle ; modèles à porte dérobée. Sans doute connus du programme, mais absents du dossier des PDF |

Déjà présents dans le dossier des PDF (non comptés) : 2309.17012 (Koo et al.) [Z229], 2402.10669 (Chen et al.) [Z230], 2403.17710 [Z231], cités par CALM ; 2412.01784, cité par N-013.

### 6.6 Limites de cette lecture (R8)

- Quatre papiers seulement ; aucune recherche extérieure ; les références citées n'ont pas été lues.
- Les absences relevées valent pour ces PDF, pas pour le champ.
- Les lectures d'image (Kaur, figure 2 ; Poser, figure 5) ne sont pas opposables.
- Les prononcés « voisin » ne disent pas que les zones revendiquées sont vierges : ils disent que ces papiers ne les occupent pas.

---

## 7. Fichiers livrés (dossier `lot6-lecture/`)

- `rapport-lot6-pistes-v1.md` (ce rapport) et son compagnon `.sha256`.
- `citations.json` : 232 citations (identifiant, fichier, page, texte), compagnon `.sha256`.
- `scripts/verifier_citations.py` ; `scripts/preparer_banc_synthetique.py`.
- `extractions/` : 261 fichiers de texte et `manifeste.json`.
- `controles/` : `banc-r5-cas-reels.json`, `banc-r5-resultat-reels.txt`, `banc-r5-cas-synthetiques.json`, `banc-r5-resultat-synthetiques.txt`, `banc-r5-extractions-synthetiques/`, `banc-r5-gardes.txt`, `controle-citations-v1.txt`, `images/` (lectures d'image), `empreintes-livrables-v1.txt`.

Reproduire le contrôle final, depuis `lot6-lecture/` :
`python3 -I scripts/verifier_citations.py verifier --citations citations.json --extractions extractions`
