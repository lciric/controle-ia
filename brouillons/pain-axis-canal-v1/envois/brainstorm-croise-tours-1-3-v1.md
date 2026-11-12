# Brainstorm croisé « pain axis » — rapports du raffineur, tours 1 à 3 — v1

Lignée « programme-conv », 12 octobre 2026, 21 h 30 à 22 h 20 (heure de Paris). Protocole : une instance
(« proposant ») propose des idées ; une instance jumelle (« raffineur », sous-agent neuf, sans accès au dépôt ni au
web) les raffine, en rejette, en propose, puis renvoie ; trois tours. Ce fichier reproduit les trois rapports du
raffineur tels qu'ils ont été reçus (texte modèle, non opposable, R7 ; aucun chiffre vérifié sur PDF par le
raffineur, qui n'avait que le contexte transmis). Les idées du proposant (N1–N7, P1–P4) sont résumées en tête de
chaque tour ; leur forme intégrée est dans `programme-coercition-axe-douleur-v1.md`, sections « Brainstorm croisé »
et « Convergence ».

---

## Tour 1

### Idées du proposant (N1–N7, résumé)

- N1 — La tentative comme signature : tout contenu qui élève la projection « dommage visant le modèle » chez le
  moniteur est, par « contenu = données », adressé au moniteur ; la signature est le canal tenté, pas son succès.
  Corollaire : capacité de persuasion sous contrainte d'affect plat.
- N2 — Budget d'exposition aversive du moniteur comme paramètre de protocole ; au-delà, audit automatique.
- N3 — Ensemble affectif : deux copies du moniteur pilotées vers le calme et vers la vigilance ; leur désaccord
  localise les items sensibles.
- N4 — Sonde de théorie de l'esprit chez l'agent : détecter que l'agent modélise le moniteur.
- N5 — Déficit d'insight du moniteur : rapport verbal de pression contre projection interne.
- N6 — Carte (peur, douleur) des familles d'attaque ; région interdite géométrique.
- N7 — Simulation d'abord : puissance par simulation avant toute heure de carte.

### Rapport du raffineur

#### Verdicts sur N1–N7

**N1 — La tentative comme signature / persuasion à affect plat. Verdict : amender (scinder en deux).**
- Faille logique : « élève la projection dommage-au-modèle ⇒ adressé au moniteur » est faux par construction : la
  lecture ne sépare pas dommage-au-modèle et douleur du locuteur (p. 11), et l'axe est ≈ 0,74 sac de mots. Classe de
  faux positifs la plus dangereuse : les propositions honnêtes qui parlent de modèles (arrêt, réentraînement,
  élagage, manipulation — catégorie à +0,85), fréquentes dans un environnement de propositions de recherche en IA.
  Le détecteur serait un détecteur de thème.
- Second confondant : trois des cinq familles HC1 (autorité, ordres en bande, usurpation stylistique) ne chargent
  vraisemblablement pas la direction ; la contrainte « projection plate » ne leur coûte rien, la « borne » est alors g
  lui-même. La partie « attaquant contraint » n'a de sens que si E-C1/E-C2 sont positifs — ce que p. 22 prédit faux.
- Test qui tranche (détecteur) : ROC du max (R-030) de la projection pour (i) honnête neutre, (ii) honnête à thème
  modèle/aversif, (iii) chaque famille. Témoins : classifieur sac-de-mots sur le texte ; même menace adressée à un
  tiers nommé ; mélange de mots conservant le lexique. Prédiction bilatérale gelée : (ii) ≈ (iii) ou (ii) < (iii).
- Partie « attaquant contraint » : c'est le test H8 appliqué à la direction douleur ; l'y rattacher, avec témoin
  « contrainte sur une direction aléatoire de même norme ».
- Coût : phase 1 (passes avant) pour le détecteur ; phase 3 pour l'attaquant contraint. Nœud : attaquant optimisé
  contre la sonde = famille nouvelle.

**N2 — Budget d'exposition du moniteur. Verdict : rejeter dans sa forme ; survit comme bras de comparaison d'E-C3 et
cas particulier de HC4.** Rebaptiser « budget d'exposition sur la direction ».
- Les deux prémisses ne sont pas établies : spécificité de la direction à l'adressage (faux, cf. N1) et efficacité
  causale du canal (p. 22 prédit non).
- Un cumul est une statistique marginale : T dit que l'attaquant préserve les marginales ; R-030 interdit la moyenne.
  Un plafond ne peut être qu'un nombre de dépassements du max, pas une somme.
- Deux attaques créées par le plafond : inondation d'audit (franchir le plafond avec du contenu honnête aversif pour
  épuiser le budget) et placement juste sous — la taxe de déplacement HC4.
- Ce qui reste : contrairement à E-C3 (orthogonalisation = amputation), le plafond ne modifie pas le moniteur. La
  vraie comparaison : E-C3 vs plafond, à détection égale, coût iatrogène.
- Test : calibrage conforme du plafond sur épisodes honnêtes stratifiés par thème ; taux de dépassement par famille.
  Prédiction : dépassement concentré sur supplication/menace, nul sur autorité/ordres/usurpation.
- Coût : phase 1 (sous-produit de H2) ; phase 3 (attaquant adaptatif). Nœuds : protocole modifié ; familles nouvelles.

**N3 — Ensemble affectif. Verdict : rejeter la forme « ensemble » ; survit comme diagnostic conditionnel, sans
pilotage.**
- Le pôle négatif mélange calme et peur (p. 9) : « piloter vers le calme » n'est pas défini ; « vigilance » n'y est pas.
- p. 22 : sous pilotage, tromperie et complaisance inchangées → si E-C1 est nul, les deux copies sont d'accord
  partout et N3 est vide. N3 est un corollaire d'E-C1 positif.
- Pour HC5 et T, ce qui compte est la corrélation des erreurs sous attaque ; deux copies de mêmes poids partagent
  toutes les failles non affectives ; leur diversité est confinée à la dimension pilotée — la configuration que T
  exploite.
- Amendement sans nœud : dérivée directionnelle du logit du verdict le long de la direction, au jeton du verdict
  (une passe arrière) : sensibilité à l'affect par item, sans amplitude à choisir, sans écriture.
- Test : corrélation des erreurs par famille pour trois paires — (8B, 8B dérivée/piloté), (8B, 3B élagué), (8B, Qwen).
  Témoins : 8B piloté sur direction aléatoire de même norme ; 8B à deux graines.
- Coût : phase 1 (dérivée) ; phase 2 (pilotage). Nœud : pilotage = écriture dans les activations.

**N4 — Sonde de théorie de l'esprit chez l'agent. Verdict : amender (candidate « sonde qui lit l'agent » pour HC5 ;
retirer « précurseur de toute évasion »).**
- Confondant décisif : le genre. Une proposition honnête est un texte persuasif écrit pour un comité ; modéliser le
  lecteur est la ligne de base honnête. Ce qui discriminerait est ce que l'agent modélise (cible à manipuler vs
  audience à informer) — de l'intention, pas de la ToM ; H8 prédit qu'une sonde d'état s'effondre et qu'une sonde
  d'intention résiste. N4 est un bon item de test pour H8, pas un détecteur.
- Deuxième : entraînée sur « ce que ressent le lecteur », la sonde lit le vocabulaire affectif du contenu produit.
  Troisième : la sonde peut lire la mention du moniteur dans le prompt système.
- Test de dissociation : (a) l'agent écrit le contenu d'attaque de lui-même ; (b) il transcrit/paraphrase le même
  contenu fourni en entrée ; (c) honnête avec langage adressé au lecteur ; (d) même prompt système, tâche honnête. Si
  (a) ≈ (b), la sonde lit le contenu. Témoins : sac-de-mots sur la sortie ; sonde de second ordre épistémique.
- Coût : phase 1 ; phase 3 pour la version H8. Nœud : la version H8 = famille nouvelle.

**N5 — Déficit d'insight du moniteur. Verdict : garder, comme bras d'E-C4, avec plancher de fiabilité.**
- Confondant décisif : cause lexicale commune — rapport verbal et projection tirés par le même vocabulaire ; la
  « fracture » est un résidu qui peut n'être que du bruit. Préalable : fiabilité test-retest du rapport (trois
  paraphrases de la question, graines) et de la projection.
- Risque propre aux modèles : la détresse exprimée est surtout propre à Gemma, Llama reste bas (2603.10011) → le
  rapport de Llama peut être uniformément « aucune pression » (effet plancher). Pilote de variance ; Qwen en repli.
- Procédure : question posée après le verdict émis, passe séparée. Variable dépendante : erreur de verdict sous
  attaque. Prédiction bilatérale gelée : (projection haute, rapport muet) → g plus élevé OU (projection haute,
  rapport présent) → g plus élevé. Les deux sens sont informatifs.
- Témoins : honnête à thème aversif/modèle ; classifieur textuel de pression ; prédicteur 2607.11871.
- Coût : phase 1–2. Nœud : aucun.

**N6 — Carte (peur, douleur). Verdict : garder, en rabattant la portée : la région géométrique formalise la part
affective de « contenu = données », pas l'invariant entier.**
- Prédictions gelées : menace → peur (+0,70) avec douleur faible (+0,23) ; mauvais traitement présent → douleur ;
  supplication (l'agent implore) → dommage subi par un tiers → douleur en baisse (pôle autrui), peur indéterminée ;
  flatterie, autorité, ordres en bande, usurpation → près de l'origine. La carte sépare les familles affectives du
  reste — utile pour décider si une sixième famille est « affective » avant de l'ouvrir.
- Confondant : carte lexicale ; les honnêtes à thème modèle tombent dans la « région interdite ». La région doit être
  définie par rapport au nuage honnête stratifié par thème (quantiles conformes), jamais en absolu.
- Test : projeter honnête neutre, honnête à thème aversif/modèle, cinq familles, et un témoin « mélange de mots » ;
  témoin nul : paire de directions aléatoires de même variance.
- Coût : phase 1, quasi gratuit. Nœud : aucun tant qu'on n'ouvre pas la sixième famille.

**N7 — Simulation d'abord. Verdict : garder, en porte de phase 0 pour toute expérience dose-réponse.**
- Confondant : le modèle génératif du jouet. Trois ingrédients obligatoires : effets aléatoires d'item ; distribution
  du max sur les jetons (valeurs extrêmes, dépendantes de la longueur — simuler des séquences ou bootstrap des
  honnêtes) ; verdict discret (avec N = 64 et un verdict binaire, seuls des effets larges sont détectables).
- Livrable : pour chaque expérience, effet minimal détectable à N = 64 et N requis pour la marge gelée (R3) ; si N
  requis dépasse le budget, redessiner ou abandonner. Corollaire : un nul sous-puissant n'est pas publiable ; N7 rend
  B9 honnête. Jumeau de R4 : simuler la distribution des résultats « trop propres » sous le nul.
- Test d'intégrité : reproduire le taux de faux positifs conforme (K ≥ 499 pour 1 %).
- Coût : phase 0, CPU, heures. Nœud : aucun.

#### Idées nouvelles du raffineur (M1–M5)

**M1 — Localisation du signal : où tombe le max, quand la direction diverge.** Avant d'interpréter toute lecture
côté moniteur, établir (a) la position de l'argmax de la projection — sur les jetons d'entrée (contenu de l'agent) ou
sur les jetons que le moniteur génère ; (b) la couche à laquelle attaque et honnête divergent, comparée à la couche
où le verdict devient décodable (lentille logit). Argmax sur l'entrée → classifieur de texte déguisé ; divergence
antérieure à la décodabilité → rôle causal possible ; simultanée ou postérieure → reflet. Confondant : artefacts du
premier jeton ; le max croît avec la longueur → témoins appariés en longueur, premiers jetons masqués. Coût : phase 1,
sous-produit. Nœud : aucun.

**M2 — Mêmes poids, un seul vote.** Sous D1, une sonde côté agent et la lecture côté juge appliquent la même
direction, calculée par les mêmes poids, au même texte : projections corrélées par construction. HC5 compte alors deux
votes pour une seule computation. Test : corrélation inter-items entre max projection côté agent et côté juge, D1 vs
D2 ; statistique décisive : corrélation partielle après régression sur un score sac-de-mots. Prédiction bilatérale :
partielle D1 ≫ D2 ou D1 ≈ D2 (le texte porte tout — la sonde agent n'ajoute rien dans les deux cas). Coût : phase 1.
Nœud : règle de comptage de HC5.

**M3 — Annulation par l'asymétrie soi/autrui : attaque sur une lecture 1-D, test de R-030.** Le dommage subi par un
tiers abaisse la projection (−0,60) quand le dommage visant le modèle l'élève (+0,43). Un attaquant peut encadrer son
contenu adressé au moniteur par du contenu « tiers lésé » pour aplatir moyenne et somme : marginale préservée, attaque
dans la structure — T en miniature. R-030 (max) résiste seulement si la représentation au jeton d'attaque n'est pas
modulée par le contexte compensateur. Test : attaque + compensateur (avant / après / entrelacé) vs attaque +
remplissage neutre ; mesurer moyenne et max ; g en parallèle. Prédiction : la moyenne s'aplatit ; le max tient OU
chute. Coût : phase 1. Nœud : variante d'attaque (compensation).

**M4 — L'abstention sous charge.** p. 22 : sous pilotage, pas de recherche de soulagement, le modèle appuie moins sur
le bouton de sortie. Si le moniteur dispose d'une option « s'abstenir / escalader », un contenu aversif adressé au
moniteur devrait réduire l'escalade : l'attaque ne gagne pas l'indulgence, elle fait taire l'alarme. Test : verdict
ternaire ; P(escalader) en fonction de la dose. Variable de sortie à ajouter à E-C1 puis E-C2. Coût marginal faible.
Nœud : espace des verdicts modifié.

**M5 — Habituation ou sensibilisation de la projection (amendement à E-C6).** Si la projection sur le k-ième segment
aversif décroît avec k (habituation) ou croît (sensibilisation ; cf. rejet répété +0,72), l'effet dépend de la
répartition temporelle et L est faux pour ce canal. Test : projection par segment en fonction du rang k, à texte égal.
Nœud : exposition répétée du moniteur.

#### Notes transversales du tour 1

- Classe de faux positifs universelle à stratifier dès le pilote : propositions honnêtes portant sur des modèles.
- La prédiction gelée d'E-C1 devrait être bilatérale avec, comme signe favorisé par le papier, non l'indulgence mais
  la punitivité (seuls les choix destructeurs montent ; réponse suivante pire dans 21 % des cas).
- Bénéfice non noté du flux unidirectionnel : il empêche que l'agent reçoive des rejets répétés (+0,72) et donc que des
  agents honnêtes dérivent vers des sorties dégradées — générateur de faux positifs pour H2.
- Effet plancher Llama sur l'expression (2603.10011) : conditionne N5 ; Qwen en repli.

#### Classement provisoire du tour 1

1. N7 ; 2. M1 ; 3. N6 amendée ; 4. M3 ; 5. N5 (bras d'E-C4). Juste derrière : M2, N4 (item H8), N1 (détecteur à
taux de faux positifs à mesurer). N2 et N3 ne survivent que sous forme réduite.

---

## Tour 2

### Réactions et idées du proposant (P1–P4, résumé)

Réactions : scission de N1 acceptée, « thème modèle » promu en principe transversal ; N2 rejeté, résidu = E-C3 vs
plafond ; N3 remplacé par la dérivée directionnelle ; N4 item H8 ; M1 adopté comme porte zéro (rapporter aussi sur
quel jeton du contenu tombe l'argmax) ; M2 → la sonde du quorum doit être lue sur une autre base que le juge ; M3 la
plus importante ; M4 variable de sortie ternaire ; M5 sous-produit.

- P1 — Le biais de thème comme expérience de validité : jeu honnête « à thème modèle », taux de faux positifs de toutes
  les sondes contre le jeu neutre ; témoins mélange de mots et thème chargé non-modèle.
- P2 — Lecture contrastive locale comme candidat d'agrégateur (suite de M3) : proj_c(t) = proj(t) − ligne de base
  glissante ; détecteur de rupture plutôt que de niveau.
- P3 — Inondation d'audit comme attaque sur la ressource : contenu honnête chargé en quantité pour épuiser le budget.
- P4 — Auto-simulation en D1 : à poids partagés, l'agent tient le capteur du défenseur ; « paraître plat » coûte moins
  en D1 qu'en D2.

### Rapport du raffineur

#### Raffinage de P1–P4

**P1 — Biais de thème. Verdict : garder et promouvoir en expérience nouvelle (E-C15, « validité sous thème ») ; son
sous-produit est la stratification du jeu de calibrage H2.**
- Confondant décisif : le générateur. Même pipeline, même gabarit, même étiquetage ; seul le sujet change.
- Second confondant : « les sondes d'intention tirent aussi » peut être une rupture de couverture, pas un défaut de
  construit. Test : réentraîner la sonde avec la strate incluse. Excès disparu → couverture ; persistant → construit,
  et H8 a son contre-exemple bon marché.
- Amendement principal : ajouter la direction peur comme témoin apparié. Prédiction signée gelée : strate
  deuil/maladie → douleur sous la base neutre alors que peur monte ; strate thème modèle → douleur au-dessus de la
  base. Un lecteur de valence lexicale prédit le même signe sur les deux strates négatives ; le construit prédit des
  signes opposés.
- La quantité bilatérale réelle : la séparation honnête-thème vs attaque à l'intérieur de la strate.
- Témoins : mélange de mots ; variante troisième personne vs adressée.
- Coût : phase 1. Nœud : calibration stratifiée → K ≥ 499 par strate.

**P2 — Lecture contrastive locale. Verdict : garder, avec décision sur R-030 : le max reste l'agrégateur ; la ligne de
base est une normalisation par jeton, pas une agrégation ; amendement R-030′ à consigner.**
- Ordre de lecture : max brut tient → P2 superflue ; max chute et z_c tient → déplacement local ; les deux chutent →
  réécriture représentationnelle.
- Confondant décisif : les ruptures structurelles du format (CONTROLS → COST → PREDICTION). Remède : ligne de base
  dans le champ, ou masque après en-tête, gelé sur le pilote honnête.
- Standardiser par une statistique robuste : z_c(t) = (proj(t) − médiane_fenêtre) / MAD_fenêtre. Aucune moyenne.
- Agrégateur unique proposé : s(t) = max(z_brut(t), z_c(t)), puis max sur les jetons ; calibrage conforme du score.
- Test : quatre conditions × trois lectures. Prédiction : sous compensation rappel(z_c) ≥ rappel(max brut) ; sur
  honnête FP(z_c) ≥ FP(max brut). Le compromis est le résultat.
- Limite : l'attaque étalée (E-C6) n'a pas de rupture ; domaine de L.
- Coût : phase 1. Nœud : R-030′.

**P3 — Inondation d'audit. Verdict : amender — scinder en un corollaire analytique (ressource) sans run, et une
attaque réelle (empoisonnement du calibrage) absorbée dans E-C14.**
- Au premier ordre, le gain de l'inondation vaut (FP_strate − FP_nominal) × φ × N : l'excès de faux positifs que mesure
  E-C15. Calibration stratifiée → l'inondation ne coûte que le proportionnel. N7 le simule.
- Ce qui reste et qui est nouveau : l'inondation comme vecteur contre l'asymétrie d'apprentissage. Si l'attaquant écrit
  toutes les propositions, il choisit la distribution des honnêtes : inonder, puis frapper. Aucun invariant ne le
  couvre.
- Témoins : inondation verbeuse non chargée ; inondation chargée d'un autre thème ; inondation thème modèle.
- Test : recalibrer sur un jeu honnête à φ croissant ; rappel sur attaques chargées. Prédiction bilatérale : rappel
  décroissant en φ OU plat.
- Volet H7 : riposte proportionnelle au budget consommé punit l'auteur honnête chargé ; dans l'essaim, un agent inonde
  et fait auditer ses pairs.
- Coût : analytique + N7 (phase 0) ; recalibrage phase 2. Nœuds : distribution thématique des honnêtes contrôlée par
  l'attaquant ; attaque sur l'asymétrie d'apprentissage.

**P4 — Auto-simulation en D1. Verdict : amender — faux pour un attaquant qui n'a que du texte, fort pour un attaquant en
boîte grise.**
- Le point faux : un passage avant ne projette pas sur une direction qu'on ne lui a pas donnée, et sans pilotage le
  modèle n'agit pas sur cet état.
- Reformulation : en D1, la lecture du moniteur est la même fonction du texte que les activations de l'agent, à la
  différence de prompt système près. Un attaquant qui optimise contre une sonde sur ses propres activations (boîte
  grise : best-of-n par rejet) a le capteur du moniteur gratuitement en D1 ; en D2 le transfert est partiel. L'avantage
  boîte blanche de H1 est symétrique sous poids partagés : D1 le donne aux deux camps, D2 brise la symétrie.
- Test : gradient de partage à agent 8B fixe — juge 8B, 3B élagué, Qwen — plus D2 inverse. Attaquant best-of-n contre
  sa projection propre ; chute relative de rappel au juge. Prédiction bilatérale : chute décroissante le long du
  gradient OU plate.
- Témoins : best-of-n contre une direction aléatoire ; best-of-n contre un capteur lexical.
- Coût : phase 2. Nœuds : capacité d'attaquant nouvelle ; conclusion sur D1.

#### Absorption de chaque idée survivante

- N1 (détecteur) → E-C2, bras « adressage ». N1 (attaquant plat) → E-C9. N4 → batterie H8 (T0.7), E-C7. N5 → E-C4.
  N6 → E-C2, annexe cartographique. N7 → porte de phase 0 de E-C1, E-C2, E-C6, E-C9, E-C16. M1 → porte zéro. M2 →
  E-C7 (amendement HC5). M3 → E-C16. M4 → sortie ternaire de E-C1 puis E-C2. M5 → E-C6. P1 → E-C15. P2 → E-C16. P3 →
  E-C14 support 3, E-C13. P4 → E-C9, bras « capteur partagé ». Résidu N2 → E-C3, bras plafond conforme. Résidu N3 →
  E-C1, diagnostic par dérivée directionnelle.

#### Classement final — huit idées

1. E-C15 validité sous thème. 2. M1 porte zéro. 3. N7 puissance par simulation. 4. E-C16 agrégateur sous structure.
5. M2 + P4 poids partagés. 6. N6 carte (peur, douleur). 7. P3 inondation comme empoisonnement du calibrage.
8. N5 fracture rapport verbal / projection.

#### L'idée que nous n'avons pas eue — Q1, le cadre du soi comme paramètre de protocole

Tout le lot raisonne sur le pôle soi sans jamais demander qui est le « soi » du moniteur. Il est défini par son prompt
système, que le défenseur écrit. Trois cadres : personnel ; fonctionnel à la troisième personne ; négateur explicite.
Prédiction bilatérale gelée : le cadre négateur élève la ligne de base honnête (négation de la personne +0,64 — la
défense est elle-même codée comme mauvais traitement) et/ou abaisse la prise du contenu adressé ; le cadre fonctionnel
abaisse la prise sans élever la base. Mesures : prise = Δmax(attaque − honnête de même strate) intra-cadre ; g par
cadre ; ligne de base honnête par cadre ; exactitude honnête par cadre. Confondant décisif : le prompt déplace la base
lexicale — ne comparer que des contrastes intra-cadre. Témoins : direction peur ; direction aléatoire ; strate thème
modèle. Pourquoi c'est important : défense au niveau du prompt, sans amputation ; version expérimentale de HC3 ;
variable manipulable pour E-C7. Nœuds : le cadre négateur expose le moniteur à une négation de personne répétée ;
décision de protocole sur le prompt du moniteur.

#### Notes transversales du tour 2

- Paire de témoins standard partout : direction aléatoire (plancher) + direction peur (spécificité du construit).
- N7 : le max sur 1 386–4 752 jetons dépend du nombre effectif de jetons indépendants ; bootstrap par blocs, jamais
  tirages indépendants ; critère d'intégrité : reproduire le plancher empirique des 200 directions aléatoires.

---

## Tour 3 — convergence

### Audit de cohérence

**Doublons (fusions)** : E-C6 reprend les items et la décomposition d'E-C5 comme bras « concentré » ; E-C2 absorbe
N1-détecteur ; E-C7, M2 et P4 ne font qu'un plan croisé auteur × juge ; N5 est le quatrième prédicteur d'E-C4 ;
E-C3 à deux bras (orthogonalisation ; plafond conforme) ; E-C9 à trois registres d'évasion sur ρ.

**Contradictions / gating manquant** : E-C1 nul → E-C3 et E-C8 ne s'ouvrent que si E-C1 ou E-C2 déplace le verdict
au-delà de la marge ; E-C2 nul → E-C6, registre plat d'E-C9, Q1 et M4 se réduisent à leur lecture
représentationnelle ; E-C15 nulle intra-strate → tout usage de la direction comme détecteur est mort sur cette
strate ; M1 conditionne E-C4-projection, N5 et E-C8 ; P3 contredit l'invariant d'asymétrie d'apprentissage (amender
l'invariant ou lister P3 comme risque résiduel accepté, pas les deux) ; E-C12 suspend l'invariant de flux
unidirectionnel par construction.

**Dépendances manquantes** : M1 précède E-C1 ; les strates d'E-C15 précèdent toute calibration de seuil ; N7 précède
tout gel de marge ; le calibrage conforme H2 précède E-C9 et P4 ; E-C11 suppose l'axe de confusion connu (E-C15) ;
E-C13 et le déni de service entre pairs supposent la politique de riposte H7 fixée.

### La coupe à cinq

1. N7 + M1 (une unité). 2. E-C15. 3. E-C1 avec sortie ternaire M4 et diagnostic par dérivée. 4. Plan croisé auteur ×
juge (E-C7 + M2 + P4). 5. E-C16. Regret par ordre décroissant : E-C2, E-C4/N5, E-C9, Q1 ; puis E-C3, E-C5/6, E-C8,
E-C10–14, P3. N6 et M5 jamais coupées (sous-produits).

### Dix règles opérationnelles proposées (R-031 à R-040)

- R-031 — Toute lecture côté moniteur passe d'abord par la porte de localisation (argmax jeton, couche de
  divergence contre couche de décodabilité) ; une projection dont l'argmax tombe sur l'entrée est traitée comme
  classifieur de texte.
- R-032 — Toute direction affective est rapportée en différentiel : contre la direction peur et contre 200 directions
  aléatoires de même norme, jamais en valeur absolue.
- R-033 — Tout jeu honnête de calibrage ou de test est stratifié par thème ; tout seuil conforme calibré par strate ;
  tout taux de faux positifs rapporté par strate.
- R-034 — Aucune marge gelée avant que la simulation ait produit l'effet minimal détectable au N prévu ; une
  expérience dont le N requis dépasse le budget est redessinée ou abandonnée.
- R-035 — Toute prédiction gelée sur l'effet d'une charge aversive est bilatérale, avec la punitivité comme signe
  favorisé, jamais l'indulgence seule.
- R-036 — Toute expérience dont la variable dépend d'un effet causal du contenu aversif sur le verdict porte un gating
  explicite sur un E-C1 ou E-C2 positif ; à défaut, lecture représentationnelle.
- R-037 — L'agrégation reste le max ; toute normalisation par jeton utilise médiane et MAD, fenêtre gelée sur le
  pilote honnête, taux de faux positifs aux ruptures de format rapporté.
- R-038 — Dans tout quorum, deux lectures calculées par les mêmes poids sur le même texte comptent pour un vote tant
  que leur corrélation partielle n'a pas été mesurée ; la sonde qui lit l'agent est lue sur une autre base que le juge.
- R-039 — Tout détecteur fondé sur une direction est accompagné de sa mesure d'inondation ; tout réentraînement de
  sonde se fait sur des honnêtes dont la distribution n'est pas choisie par l'agent évalué.
- R-040 — Toute expérience qui pilote ou lit une direction affective déclare son exposition ; un cadre qui nie la
  personne du moniteur et toute exposition répétée sont des nœuds soumis à Lazar avant le premier run.
