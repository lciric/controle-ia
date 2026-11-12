# Antériorité de la règle « loin en domaine ET proche en concept » — lecture par un lecteur neuf, v1

Date : 30 octobre 2026. Auteur : sous-agent lecteur neuf (n'a écrit ni la règle ni la note du premier lecteur). Aucune dépense, aucun commit.
Objet : vérifier si la règle « loin en domaine (catégorie, revue, citations) ET proche en concept (représentations de texte), deux espaces mesurés séparément, testée en rétrospectif à coupure temporelle contre la marche de Swanson, les voisins communs, des graphes nuls et le hasard » a déjà été testée.
Note du premier lecteur (conv-audit), relue : `origin/canal/conv-audit-n04:brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/bisociation-litterature-reelle-v1/anteriorites-et-bancs-v1.md`.

Conventions de lecture :
- « lu sur PDF » : texte extrait du PDF empreinté avec `pdftotext`, lu par moi ; pages = pages physiques du fichier PDF (première page du fichier = p. 1), pas la pagination de la revue.
- « résumé lu » : résumé rendu par l'interface de Semantic Scholar, non opposable (R7).
- « non lu » : rien d'autre que le titre, ou rien du tout.
- Aucun chiffre ci-dessous n'est repris pour un préenregistrement sans relecture de la page citée (R7) ; ceux qui sont donnés le sont avec leur page.

## 1. Verdict (niveau R8)

**Collision partielle.** Ni collision totale, ni zone libre.

- **Ce qui est déjà pris** (lu sur PDF) : la *forme* de la règle — un score qui combine une *distance* mesurée dans un espace (accessibilité humaine) et une *proximité* mesurée dans un autre espace (vecteurs de mots appris sur le texte), les deux calculés séparément puis mélangés par un coefficient, évaluée avec une coupure temporelle (années de prédiction 2001 et 2020) — existe chez Sourati et Evans (arXiv 2306.01495, p. 8-9 et p. 15 ; préversion 2104.05188, p. 5 et p. 14). Le principe ancestral (deux littératures disjointes mais complémentaires) est explicitement repris par eux comme « heuristique de Swanson rendue continue » (2306.01495, p. 3). La séparation de deux espaces (contenus, mots-clés ; contextes, revues citées) avec une validation temporelle d'un an est chez Shi et Evans (Nature Communications 2023, p. 2 et p. 9). En brevets, deux espaces séparés (structure de co-classification et de co-citation ; similarité sémantique du texte), une coupure temporelle stricte et un modèle nul existent chez Huang, Xu, Cai et Lü (arXiv 2509.15521v1, p. 1, 5, 6, 10).
- **Ce que je n'ai trouvé nulle part** (sur ce qui a été lu) : la conjonction exacte (i) distance de domaine mesurée par catégorie, revue ou citations — et non par la distance entre communautés d'auteurs — (ii) proximité mesurée dans un espace de représentations de texte, (iii) la règle « loin ET proche » évaluée sur la réalisation ultérieure des paires, (iv) contre les quatre bases nommées (marche de Swanson, voisins communs, graphes nuls, hasard). Cette absence est **une question, pas un trou** (R8) : 203 citants examinés sur résumé, deux citants lus en entier, recherches par mots-clés presque stériles (section 5).
- **Conséquence pour la revendication** : la règle ne peut pas être présentée comme nouvelle ; au mieux comme une **variante de Sourati et Evans** qui change l'espace de la distance (domaine bibliographique au lieu d'auteurs), le critère de succès (réalisation ultérieure au lieu de « moindre découvrabilité et plausibilité théorique ») et les bases de comparaison. Le risque d'être jugé incrémental est réel.
- **Avertissement sur le signe** (lu sur PDF, utile au préenregistrement) : chez Sourati et Evans, plus la part « étrangère » (loin) augmente, **moins** les prédictions sont réalisées par les humains (2306.01495, p. 9, renvoi à leur figure de données étendues 7 ; temps d'attente plus longs, p. 10) ; leur argument de valeur repose sur des scores théoriques (premiers principes, interactions protéine-protéine), pas sur la réalisation (p. 10-11). Chez Huang et collègues (brevets), toutes les similarités, structurelles comme sémantiques, sont positivement associées à la convergence future, et les nouvelles convergences vont de plus en plus vers « structure proche, sémantique lointaine », soit la configuration **inverse** de la règle (2509.15521v1, p. 10 et p. 15). Chez Shi et Evans, la nouveauté de contexte et la nouveauté de contenu sont *toutes deux* associées à l'impact, la combinaison des deux le plus (p. 4) ; ce n'est pas « loin en contexte, proche en contenu ». Un signe positif de la règle sur la réalisation ultérieure n'est donc pas acquis ; la prédiction chiffrée devra le fixer avant toute lecture (R1, R3).

## 2. Réponses aux trois travaux du point 1 (lus en entier sur PDF)

### 2.1 arXiv 2610.25281 — « Bridging Concepts » (Yoon, Hwang, Baek, Shin, Whang ; atelier KEIR à CIKM 2026, 5 p.) — **Non**

- Tâche : graphes de concepts fins extraits par GPT-4o-mini des titres et résumés de CIKM, KDD et SIGIR ; arête = co-occurrence dans un article ; prédire si une paire *actuellement non reliée* formera une connexion à fort impact (p. 1 ; p. 2, section 3). Positif = paire nouvelle dans la fenêtre cible dont les articles cumulent au moins 5 citations ; négatifs avec 36,1 % de « durs » (p. 2).
- Coupure temporelle : **oui** — instantané jusqu'en 2023, cible 2024-2025 ; réglage « Eval » : instantané jusqu'en 2021, cible 2022-2023 ; citations comptées jusqu'à l'année de l'instantané (p. 2).
- Loin en domaine : **non**. Chaque graphe est construit sur une seule conférence ; aucune catégorie, revue ou distance de citation n'est mesurée comme espace. La « compatibilité inter-domaines » apparaît seulement comme *une* caractéristique sémantique produite par un modèle de langage dans un exemple (p. 4, tableau 3), interprétée a posteriori par les auteurs eux-mêmes comme non probante (p. 4, section 5.2).
- Proche en concept dans un espace de texte séparé : **non** ; les caractéristiques « sémantiques » sont calculées par GPT-4o lisant le sous-graphe (p. 3, section 4.2), pas par une proximité de représentations.
- Bases : Impact4Cast ; sept modèles de prédiction de liens temporels (TGAT, DyGFormer, CAWN, GraphMixer, TGN, JODIE, DyRep) ; GPT-4o et GPT-4o-mini avec ou sans sous-graphe (p. 3, tableau 2 ; p. 4, section 5). Les voisins communs et la longueur du plus court chemin sont des *caractéristiques* (p. 4, tableau 3), pas des bases. Ni marche de Swanson, ni graphe nul, ni hasard. Métrique : F1 macro.

### 2.2 arXiv 2610.38719 — « Learning Scientific Trajectories to Predict Future Biomedical Discoveries » (ForeSCITE ; Chang, Ondov et collègues ; 33 p.) — **Non**

- Méthode : conclusions de résumés PubMed plongées dans un espace de texte (bge-large, 1 024 dimensions), 407 grappes thématiques, une direction « ancien vers récent » par grappe, extrapolation puis décodage en texte par un modèle aligné (p. 1-2 ; p. 16-19).
- Coupure temporelle : **oui** — 31 mars 2023 ; 3 005 395 conclusions avant, 236 057 réservées après (p. 16).
- Loin en domaine : **non** ; l'extrapolation se fait *dans* une grappe thématique (p. 17-18). Un seul espace (texte).
- Bases : cinq générateurs par modèle de langage (trois consignes, deux avec recherche documentaire) (p. 6 ; p. 21-22) ; deux références de hasard sur paires d'entités jamais vues : tirage uniforme (0,00095 %) et tirage pondéré par le degré (0,689 %) (p. 8 ; p. 23-24). Ni Swanson, ni voisins communs.
- Résultat utile pour le signe : la meilleure validation future est obtenue pour un déplacement *intermédiaire*, pas maximal (p. 8 ; p. 14, interprétation « possible adjacent ») ; environ 2 % des paires générées sont nouvelles et ré-observées après la coupure, au meilleur réglage (p. 14).

### 2.3 arXiv 2610.25678 — « Cross-Pollination Retrieval » (Jung et collègues 2026 ; 36 p.) — **En partie**

- Loin en domaine : **oui**, mesuré par catégorie : le papier trouvé ne partage *aucun* sujet OpenAlex avec le papier de base (p. 4) ; le classifieur de sujets d'OpenAlex combine un encodeur du titre et du résumé avec le nom de la revue et les citations (p. 5). Les positifs viennent à 79,9 % d'un autre champ et à 45,3 % d'un autre domaine OpenAlex (p. 6).
- Proche en concept : **pas dans un espace de texte**. La proximité est une *analogie structurelle* (correspondance d'objets et de relations) et une *utilité* jugées par un modèle de langage (p. 4-5 ; annexe p. 16), et la tâche est explicitement construite *contre* la similarité sémantique (p. 3 ; négatifs durs du même sujet, p. 5-6).
- Deux espaces séparés : en partie (catégorie OpenAlex d'un côté, jugement d'analogie de l'autre ; aucun des deux n'est une proximité de représentations de texte).
- Coupure temporelle : **non** au sens de la règle. Les candidats sont restreints aux papiers publiés avant le papier de base (p. 6) : c'est une garde contre l'anachronisme, pas un test de réalisation ultérieure. La vérité terrain est le *passé* (citations de transfert déjà faites, p. 5).
- Bases : onze extracteurs (creux, denses généraux, denses scientifiques, raisonnement, interaction tardive), un reclasseur par modèle de langage, et le classement au hasard (rappel à 10 de 0,07 contre 0,26 pour le meilleur extracteur et 0,81 pour le reclasseur) (p. 7, tableau 2). Ni Swanson, ni voisins communs, ni graphes nuls.
- Statut : banc potentiel et concurrent de formulation (« trouver ce qui est loin et transférable »), pas un test de la règle.

## 3. Sourati et Evans ; Shi et Evans (point 2, lus sur PDF)

### 3.1 Sourati et Evans, « Accelerating science with human-aware artificial intelligence », arXiv 2306.01495 (version Nature Human Behaviour, 65 p.)

Ce qu'ils testent exactement :
1. **Prédiction « consciente des humains »** : hypergraphe mêlant matériaux, propriétés et auteurs ; marches aléatoires ; similarité par plongement deepwalk ou probabilité de transition (p. 3-5). Coupure : littérature antérieure à l'année de prédiction (2001 pour l'énergie et les médicaments ; 2020 pour la COVID-19), fenêtre des cinq dernières années (p. 5-6 ; p. 14). Bases : **hasard** et réplication du modèle de contenu seul de Tshitoyan et collègues (vecteurs de mots du texte) (p. 5). Mesure : précision des 50 premiers candidats contre les découvertes ultérieures (p. 5 ; p. 13).
2. **Prédiction « étrangère »** (la plus proche de la règle) : distance de plus court chemin entre la propriété et le candidat dans l'hypergraphe à auteurs (inaccessibilité humaine) **combinée** à la similarité cosinus de vecteurs de mots appris sur le texte antérieur (plausibilité), après transformation de Van der Waerden et normalisation, mélangées par β entre −1 et 1 (p. 8-9 ; p. 15). β = 0 équivaut au contenu seul ; β = −1 imite les humains (p. 9 ; p. 22, légende de la figure 8).
3. **Évaluation de la part étrangère** : précision contre les découvertes publiées (elle *baisse* quand β monte, p. 9), temps d'attente des découvertes (il *monte*, p. 10), scores théoriques de premiers principes ou d'interactions protéine-protéine (ils baissent moins vite que la découvrabilité ; intervalle 0,2-0,3 jugé le plus prometteur) (p. 10-11).

En quoi ils diffèrent de la règle :
- la distance est celle **entre communautés d'auteurs** (plus court chemin dans l'hypergraphe à auteurs), pas la catégorie, la revue ni les citations ;
- la tâche est « une propriété cible, un réservoir de candidats » (matériaux, médicaments), pas des paires de concepts quelconques entre domaines (p. 13 ; limite reconnue p. 12) ;
- le critère de succès de la part « loin » n'est pas la réalisation ultérieure — elle est au contraire *moins* réalisée — mais la plausibilité théorique ;
- aucune comparaison à une marche de Swanson, aux voisins communs ni à des graphes nuls ; les bases sont le hasard, le contenu seul et le balayage de β.

### 3.2 Sourati et Evans, « Accelerating science with human versus alien artificial intelligences », arXiv 2104.05188 (préversion, 31 p.)

Même construction ; l'heuristique de Swanson est citée comme point de départ (p. 2) ; le cadre « étranger » combine la distance de plus court chemin et la similarité de vecteurs de mots (p. 5 ; méthodes p. 14) ; validation par facteur de puissance thermoélectrique (p. 11, figure 4). Mêmes différences que 3.1.

### 3.3 Shi et Evans, « Surprising combinations of research contents and contexts are related to impact and emerge with scientific outsiders from distant disciplines », Nature Communications 14:1641 (2023), fichier `shi-evans-2023-natcomm.pdf` (13 p.)

Ce qu'ils testent exactement :
- deux hypergraphes **séparés** par année : contenus (MeSH pour MEDLINE, codes PACS pour l'American Physical Society, classes de brevets américaines) et contextes (revues et conférences citées ; classes technologiques citées) (p. 2 ; p. 7) ;
- un modèle génératif d'hypergraphe par plongement, validé par prédiction à un an : combinaison réalisée contre combinaison au hasard de même taille (aire sous la courbe 0,98 / 0,97 / 0,95 pour les contenus, 0,99 / 0,88 / 0,83 pour les contextes) (p. 2 ; protocole p. 9) ;
- la *surprise* (improbabilité) d'un article publié, en contenu et en contexte, mise en relation avec l'impact (10 % les plus cités) : environ 4 fois pour le contexte, 2 fois pour le contenu, environ 5 fois pour les deux (p. 4) ; corrélation contenu-contexte inférieure à 0,1 (p. 4) ; les articles primés par un prix Nobel ont une nouveauté de contenu élevée mais une nouveauté de contexte inférieure à la moyenne (p. 3-4) ; « expéditions » de chercheurs vers un contexte lointain, environ 3,5 fois (p. 5).

En quoi ils diffèrent de la règle :
- mesure *a posteriori* d'articles publiés, pas règle de proposition de paires non encore réalisées ;
- les deux nouveautés vont dans le **même** sens (surprise), pas « loin en contexte ET proche en contenu » ;
- le contenu est un espace de mots-clés curés (plongement d'hypergraphe), pas de représentations de texte ;
- critère : citations et prix, pas réalisation ultérieure d'un lien ; bases : combinaisons au hasard pour la validation du modèle seulement.

## 4. Table par travail

| Référence | Fichier (dans `docs/sources/pdf/bisociation-litterature-reelle-v1/`) | Empreinte SHA-256 | Ce qui est testé | Pages | Verdict vis-à-vis de la règle |
|---|---|---|---|---|---|
| Yoon et collègues, « Bridging Concepts », arXiv 2610.25281v1 | `arxiv-2610.25281.pdf` | `4b32d77139a21965f6cd5fcab6085db5f2893cc82a6ad60f91c8ab8f5dc62d3c` | Paires de concepts non reliées qui deviendront fortement citées, graphes intra-conférence, coupure 2023 → 2024-2025 ; bases : Impact4Cast, 7 modèles temporels, GPT-4o | 1-4 | Non |
| Chang, Ondov et collègues, ForeSCITE, arXiv 2610.38719v1 | `arxiv-2610.38719.pdf` | `c21be9fa7e2680b137f1084db79094f8b01e696a4bf3750428ef20a5e9dcf624` | Extrapolation temporelle dans l'espace de texte des conclusions PubMed, coupure 31 mars 2023 ; bases : 5 générateurs, hasard uniforme et pondéré par le degré | 1-2, 6, 8, 14, 16-24 | Non |
| Jung et collègues, « Cross-Pollination Retrieval », arXiv 2610.25678 | `arxiv-2610.25678.pdf` | `04bb657db48efd681b5237c5ae1b85f8f9f8fbddd802e91ba7ea4f4d203aff76` | Recherche d'un papier d'un autre sujet OpenAlex, analogue et utile (jugé par modèle de langage) ; pas de coupure de réalisation ; bases : 11 extracteurs, reclasseur, hasard | 3-7, 16 | En partie |
| Sourati et Evans 2023, arXiv 2306.01495 | `arxiv-2306.01495.pdf` | `90ccea69c2b5fe6134409a01c4adb3444521c57e7843b09b9be8679637a7a241` | Distance d'auteurs (plus court chemin) + proximité de vecteurs de mots, mélangées par β ; coupure 2001 et 2020 ; bases : hasard, contenu seul | 3-6, 8-11, 13-15, 20-22 | **Collision partielle (forme de la règle)** |
| Sourati et Evans 2021, arXiv 2104.05188 | `arxiv-2104.05188.pdf` | `f6709c93f9f70435a981043ae893a07db2bc9ff1dd826078d30745394775f9eb` | Préversion du précédent | 2, 5, 11, 14 | Idem |
| Shi et Evans 2023, Nature Communications 14:1641 | `shi-evans-2023-natcomm.pdf` | `f576db752e31e7f6f56786d42c7b8b3e1df087c034052ffaabb9998fe9e2c6ef` | Surprise de contenu (mots-clés) et de contexte (revues citées), deux hypergraphes séparés, validation à un an contre combinaisons au hasard ; lien avec l'impact | 1-5, 7, 9 | En partie (deux espaces, pas la règle) |
| Huang, Xu, Cai, Lü, « Uncovering multi-technology convergence patterns with hypergraphs », arXiv 2509.15521v1 (citant de Shi et Evans ; versé par moi) | `arxiv-2509.15521v1.pdf` | `126dd90ec67c7a7cba4af6307e538c66910831446b2354c8461f497ec6f599cc` | Brevets : hypergraphes de co-classification et de co-citation, modèle nul probabiliste, similarités structurelles (Jaccard, allocation de ressources, marche aléatoire avec retour) et sémantique (texte) comme caractéristiques séparées, découpage temporel strict ; forêt aléatoire | 1-2, 5-6, 10-12, 15 | En partie (infrastructure : deux espaces, coupure, modèle nul ; pas la règle ; signe inverse observé) |
| De Marzo, Aroyehun, Tacchella et collègues, « Anticipating Innovation Using Large Language Models » (TechToken), arXiv 2605.04875 (citant de Shi et Evans ; versé par moi) | `arxiv-2605.04875.pdf` | `3ab225558a620d17ce60c7cc0c0c4e2cd4180151ccb9812092f163dfd5de84fa` | Brevets : la similarité de contexte linguistique entre deux classes de brevets (catégories) prédit leur première co-occurrence ; coupure (2006-2010 → fenêtres futures ; 2019-2023 → 2024) ; étiquetage contre un modèle nul de Chung-Lu ; références : autres modèles de langage, paires au hasard | 3-8 | En partie (moitié « proche en concept » sur catégories, coupure ; pas de distance de domaine séparée, pas de Swanson ni voisins communs) |

Les quatorze autres PDF du dossier n'ont pas été relus dans cette tâche ; leurs empreintes sont dans leurs fichiers `.sha256`.

## 5. Citants examinés (point 3)

Source : interface de Semantic Scholar, interrogée le 30 octobre 2026 :
- `https://api.semanticscholar.org/graph/v1/paper/arXiv:2306.01495/citations?fields=title,year,externalIds,abstract&limit=100` : 93 citants (Semantic Scholar en annonce 93) ;
- même requête pour `arXiv:2104.05188` : 7 citants ;
- `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1038/s41467-023-36741-4/citations?...` (deux pages) : 120 citants.

Après fusion des doublons : **203 citants distincts**, dont **174 de 2024 à 2026** (51 de 2024, 70 de 2025, 53 de 2026) ; **141 de ces 174 ont un résumé**, que j'ai lu ; 33 n'en ont pas (titre seul, marqués « non lu » ci-dessous). OpenAlex n'a pas pu servir (budget quotidien gratuit épuisé ; je n'ai pas demandé de clé, qui exige l'adresse de l'utilisateur).

Citants retenus après lecture du résumé comme les plus proches (aucun ne teste la règle telle quelle) :
- **Huang et collègues 2025** (arXiv 2509.15521) et **TechToken 2026** (arXiv 2605.04875) : versés et lus sur PDF, voir la table.
- « Mining Collective Intelligence and Predicting Disruptive Paradigm Shifts via Human-Aware AI », Proceedings of the Association for Information Science and Technology 2025, doi 10.1002/pra2.1298 — résumé lu : réseau mêlant graphe de connaissances et espace de collaboration, « distances de connaissance thématiques et proximités sociales » pour désigner des paires de domaines promises à une convergence, validé par alignement sur des jalons historiques (prix Nobel). **Non lu sur PDF** : accès fermé (Unpaywall : aucune copie ouverte ; éditeur : refus 403). À obtenir par un humain : c'est le citant qui ressemble le plus à une règle de paires de domaines.
- « Discovering emergent connections in quantum physics research via dynamic word embeddings » (arXiv 2411.06577) — résumé lu : prédiction de co-occurrence de concepts par plongements de mots dynamiques, comparée à des graphes de connaissances ; un seul espace, pas de distance de domaine. Non lu sur PDF.
- « Forecasting high-impact research topics via machine learning on evolving knowledge graphs » (Impact4Cast, arXiv 2402.08640) — résumé lu : réseau sémantique plus réseau d'impact, prédiction de l'impact de paires de concepts. Non lu sur PDF ; c'est la base de « Bridging Concepts ».
- « Forecasting Conceptual Diffusion in Science » (arXiv 2606.03919) ; « Historical Anchors for Scientific Forecasting on Human-Aware Knowledge Graphs » (arXiv 2610.14023, prolonge Sourati et Evans sur les mêmes bancs) ; « China leads scientific trends; the West launches new ones » (arXiv 2603.01117, mesures dérivées des deux papiers d'Evans) ; « Cultural Alien Sampler » (arXiv 2510.20849) et « Alien Recombination » (arXiv 2411.11494) (cohérence contre typicité, en art) ; « Deep Ideation » (arXiv 2511.02238) ; « IDRBench » (arXiv 2507.15736) ; « Dyport » (doi 10.1186/s12859-024-05812-8, banc de génération d'hypothèses biomédicales à graphe dynamique) — résumés lus, aucun ne teste la règle. Non lus sur PDF.

Recherches complémentaires par mots-clés (Semantic Scholar, six requêtes) : deux seulement ont rendu un résultat avant que le disque de la session ne soit plein ; rien de pertinent hors un titre, « Cluster links prediction for literature based discovery using latent structure and semantic features » (SIGIR 2014, doi 10.1145/2600428.2610376), **non lu** (titre seul) — il combine structure et sémantique en découverte par la littérature et mérite un contrôle.

La liste complète des 203 citants (année, titre, identifiant, source, statut du résumé) est en annexe.

## 6. Ce qui reste à vérifier

1. **Le citant fermé** doi 10.1002/pra2.1298 (paires de domaines par distance de connaissance et proximité sociale) : obtenir le PDF, l'empreinter, le lire. C'est la vérification la plus urgente.
2. **Les 33 citants sans résumé** (titres en annexe), en particulier : « Searching together: Human–AI complementarities in innovation search » (Research Policy 2026), « Complexity and the uncertain impact of novel science » (Research Policy 2026), « Neural embeddings of collaboration networks predict citation impact and innovation » (2026), « Forecasting benchmark product emergence via technological phylogeny » (2026), « A framework for predicting scientific disruption based on graph signal processing » (2024).
3. **Citations ascendantes non faites** : de Swanson et Smalheiser (1997), de Hope et collègues 2017 (arXiv 1706.05585), de Krenn et collègues (arXiv 2210.00881 et 1906.06843), d'Impact4Cast (arXiv 2402.08640), de Yetisgen-Yildiz et Pratt 2009, et de Sourati et Evans 2022 (arXiv 2207.00902, « Complementary artificial intelligence designed to augment human discovery », même équipe, non lu).
4. **La troisième source d'index** : OpenAlex ou Google Scholar, pour les citants que Semantic Scholar ne connaît pas (Semantic Scholar annonce 120 citants pour Shi et Evans, OpenAlex 106 : les deux listes ne se recouvrent pas forcément).
5. **Littérature de découverte par la littérature « bisociative »** (Juršič et collègues 2012, termes-ponts ; Dubitzky et collègues 2012) : non lue ici ; vérifier si une évaluation à coupure y combine distance de domaine et proximité textuelle.
6. **Données étendues de Sourati et Evans** (figure 7 de données étendues, précision par β ; tableau supplémentaire 1) : vérifier sur le PDF, page par page, avant de citer un chiffre de baisse de découvrabilité.
7. **Huang et collègues** : relire les pages 10-12 et 15 pour savoir si l'interaction « structure lointaine × sémantique proche » a été estimée ou seulement les effets séparés (ma lecture : effets séparés seulement, tous positifs).
8. **Second lecteur indépendant** sur les mots-clés en français et en chinois (non faits par le premier lecteur ni par moi).

## Annexe — les 203 citants examinés

Colonnes : année ; titre ; identifiant ; papier cité ; statut. « résumé lu » = résumé de Semantic Scholar lu (non opposable) ; « non lu » = titre seul ; « lu sur PDF » = versé et lu.

| Année | Titre | Identifiant | Cite | Statut |
|---|---|---|---|---|
| 2026 | A multi-dimensional indicator system for identifying highly innovative papers: a knowledge absorption, creation, and diffusion perspective | doi 10.1016/j.joi.2025.101765 | Shi-Evans 2023 | non lu |
| 2026 | A semantic atlas of journals: Structure, position, and dispersion | doi 10.1002/asi.70067 | Sourati-Evans 2023, Shi-Evans 2023 | résumé lu |
| 2026 | A Stateful Research Information Infrastructure for Scientific Discovery | arXiv 2610.14538 | Sourati-Evans 2023 | résumé lu |
| 2026 | AI-Integrated Scientific Inquiry: A Practice-Centered Vision for Science Education | arXiv 2607.21777 | Sourati-Evans 2023 | résumé lu |
| 2026 | AI’s impact on medical research: A bibliometric study of citation impact and disruption | doi 10.1177/20552076261499911 | Sourati-Evans 2023 | résumé lu |
| 2026 | Analysis of anticipatory postural adjustment characteristics in preschool children with different motor development profiles. | doi 10.1016/j.gaitpost.2026.110200 | Shi-Evans 2023 | résumé lu |
| 2026 | Anticipating Innovation Using Large Language Models | arXiv 2605.04875 | Shi-Evans 2023 | lu sur PDF |
| 2026 | Beyond Pairwise Distance: Cognitive Traversal Distance as a Holistic Measure of Scientific Novelty | arXiv 2602.06607 | Shi-Evans 2023 | résumé lu |
| 2026 | Bridging Data‐Driven Intelligence and Expert‐Driven Knowledge: A Systematic Review of the RF‐AHP Hybrid Paradigm | doi 10.1002/widm.70107 | Sourati-Evans 2023 | résumé lu |
| 2026 | China leads scientific trends; the West launches new ones | arXiv 2603.01117 | Sourati-Evans 2023, Shi-Evans 2023 | résumé lu |
| 2026 | Collective creativity in hybrid societies | arXiv 2609.02620 | Sourati-Evans 2023 | résumé lu |
| 2026 | Complexity and the uncertain impact of novel science | doi 10.1016/j.respol.2026.105570 | Shi-Evans 2023 | non lu |
| 2026 | Consciousness, creativity, and understanding are not obstacles to machine intelligence | doi 10.1007/s11229-026-05655-1 | Sourati-Evans 2023 | résumé lu |
| 2026 | Dataset repurposing and disruptive AI research | arXiv 2609.16736 | Shi-Evans 2023 | résumé lu |
| 2026 | Designing physics experiments with artificial intelligence | doi 10.1038/s41586-026-10898-6 | Sourati-Evans 2023 | non lu |
| 2026 | Dimensions of AI de-anthropomorphization based on impression integration theory | doi 10.1016/j.techsoc.2026.103352 | Sourati-Evans 2023 | non lu |
| 2026 | Discovery by Dreaming: Cross-Domain Recombination in Artificial Memory | arXiv 2607.16256 | Sourati-Evans 2023, Shi-Evans 2023 | résumé lu |
| 2026 | Doc2LoRA Provides Decodable Representations of Scientific Ideas | arXiv 2609.38374 | Sourati-Evans 2023 | résumé lu |
| 2026 | Domain agnostic features for robust novelty assessment of scientific publication | doi 10.1007/s11192-026-05687-x | Shi-Evans 2023 | résumé lu |
| 2026 | Evaluating LLMs' divergent thinking capabilities for scientific idea generation with minimal context | doi 10.1038/s41467-026-70245-1 | Sourati-Evans 2023, Shi-Evans 2023 | résumé lu |
| 2026 | Forecasting benchmark product emergence via technological phylogeny and strategic features | doi 10.1016/j.techfore.2026.124702 | Shi-Evans 2023 | non lu |
| 2026 | Forecasting Conceptual Diffusion in Science: The Case of Quantum Computing | arXiv 2606.03919 | Shi-Evans 2023 | résumé lu |
| 2026 | From superficial scholarship to algorithmic slop in analytical chromatography. | doi 10.1016/j.jchromb.2026.125130 | Shi-Evans 2023 | résumé lu |
| 2026 | Health informatics as rebellion: a framing for introducing students to an interdisciplinary domain | doi 10.1007/s44217-025-00697-y | Shi-Evans 2023 | résumé lu |
| 2026 | Historical Anchors for Scientific Forecasting on Human-Aware Knowledge Graphs | arXiv 2610.14023 | Sourati-Evans 2023 | résumé lu |
| 2026 | How experience moderates the impact of AI suggestions on researchers' perceptions of their ideas | doi 10.1016/j.respol.2026.105575 | Sourati-Evans 2023 | non lu |
| 2026 | How to Govern a University Effectively | doi 10.4337/9781035342006 | Shi-Evans 2023 | non lu |
| 2026 | Influence of various novelty types on delayed scientific recognition: Insights from citation classics essays | doi 10.1016/j.joi.2026.101867 | Shi-Evans 2023 | non lu |
| 2026 | Innovation Discovery System for Networking Research | arXiv 2603.26496 | Shi-Evans 2023 | résumé lu |
| 2026 | Knowledge Manifold Optimization for Scientific Discovery | arXiv 2610.25662 | Shi-Evans 2023 | résumé lu |
| 2026 | Measuring the novelty of biomedical papers using the latent distances between knowledge units | arXiv 2609.05175 | Shi-Evans 2023 | résumé lu |
| 2026 | Method, Mind, and Morality: How People Make Sense of Artificial Intelligence | arXiv 2608.24748 | Sourati-Evans 2021 | résumé lu |
| 2026 | Movers and shakers: A bibliometric analysis of sports science literature and the context-dependent impact of novelty | doi 10.1177/17479541261445519 | Shi-Evans 2023 | résumé lu |
| 2026 | Navigating Epistemic Monocultures in AI-Driven Science: A Simulation Study | arXiv 2608.19390 | Sourati-Evans 2023 | résumé lu |
| 2026 | Neglected seed dispersers and research compartmentalisation: how much do we know about what we don't know? | doi 10.1111/nph.71294 | Shi-Evans 2023 | résumé lu |
| 2026 | Neighborhood clusters and citywide technological diversification | doi 10.1016/j.respol.2025.105397 | Sourati-Evans 2023 | non lu |
| 2026 | Neural embeddings of collaboration networks predict citation impact and innovation | doi 10.1016/j.ipm.2026.104634 | Shi-Evans 2023 | non lu |
| 2026 | One capability, many outcomes: unpacking AI dynamic capabilities in scientific teams | doi 10.1007/s11192-026-05679-x | Sourati-Evans 2023 | non lu |
| 2026 | Rethinking Scientific Practice in the Age of Artificial Intelligence | doi 10.1145/3803866 | Sourati-Evans 2023 | résumé lu |
| 2026 | SciTBERT: A family of chronologically consistent language models for scientific and technological language processing | arXiv 2610.12207 | Shi-Evans 2023 | résumé lu |
| 2026 | Sealed bets on emerging research topics: a protocol for judging early detection, applied to a detector and to eight research funders | arXiv 2610.34245 | Sourati-Evans 2023 | résumé lu |
| 2026 | Searching together: Human–AI complementarities in innovation search | doi 10.1016/j.respol.2026.105597 | Sourati-Evans 2023 | non lu |
| 2026 | Success of New Ideas in Online Platforms: An Idea Network Perspective | doi 10.1080/07421222.2026.2692285 | Sourati-Evans 2023, Shi-Evans 2023 | résumé lu |
| 2026 | The Costs of Early-career Disciplinary Pivots: Evidence from Ph.D. Admissions | arXiv 2603.22805 | Shi-Evans 2023 | résumé lu |
| 2026 | The Generative AI Gold Rush in Theoretical and Computational Research | arXiv 2609.04872 | Sourati-Evans 2023 | résumé lu |
| 2026 | The institutional dynamics of inequality for women inventors who break with conventional thinking | doi 10.1073/pnas.2500343123 | Shi-Evans 2023 | résumé lu |
| 2026 | The pervasive impact–innovation mismatch in individual scientific careers | doi 10.1016/j.chaos.2026.119314 | Shi-Evans 2023 | non lu |
| 2026 | Toward the sixth generation of digital transformation: from generative intelligence to inferential intelligence | doi 10.23900/ra.v24i116.1500 | Sourati-Evans 2023 | résumé lu |
| 2026 | Unintended Negative Impacts of Promotional Language in Patent Evaluation | arXiv 2605.04926 | Shi-Evans 2023 | résumé lu |
| 2026 | Using large language models to probe the limits of atom-centered structural descriptors | arXiv 2607.26984 | Shi-Evans 2023 | résumé lu |
| 2026 | When AI Meets Science: Research Diversity, Interdisciplinarity, Visibility, and Retractions across Disciplines in a Global Surge | arXiv 2605.06033 | Sourati-Evans 2023 | résumé lu |
| 2026 | When Algorithmic Exploration Becomes Cheap: A Case Study of Agentic Research in EDA | arXiv 2610.10129 | Sourati-Evans 2023 | résumé lu |
| 2026 | Who Owns Creativity and Who Does the Work? Trade-offs in LLM-Supported Research Ideation | arXiv 2601.12152 | Sourati-Evans 2023 | résumé lu |
| 2025 | A Blue Start: A large-scale pairwise and higher-order social network dataset | arXiv 2505.11608 | Shi-Evans 2023 | résumé lu |
| 2025 | A Global Dataset Mapping the AI Innovation from Academic Research to Industrial Patents | arXiv 2503.09257 | Shi-Evans 2023 | résumé lu |
| 2025 | A Multi-Task Evaluation of LLMs' Processing of Academic Text Input | arXiv 2508.11779 | Sourati-Evans 2023 | résumé lu |
| 2025 | A review on the novelty measurements of academic papers | arXiv 2501.17456 | Shi-Evans 2023 | résumé lu |
| 2025 | Accepted with Minor Revisions: Value of AI-Assisted Scientific Writing | arXiv 2511.12529 | Sourati-Evans 2023 | résumé lu |
| 2025 | AI as Governance | doi 10.1146/annurev-polisci-040723-013245 | Sourati-Evans 2023 | résumé lu |
| 2025 | AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research | arXiv 2505.12039 | Shi-Evans 2023 | résumé lu |
| 2025 | AI-enabled individual learning strategies and scientific innovation: a case from the field of computer science | doi 10.1007/s11192-025-05345-8 | Sourati-Evans 2023 | non lu |
| 2025 | An information-theoretic foreshadowing of mathematicians’ sudden insights | doi 10.1073/pnas.2502791122 | Shi-Evans 2023 | résumé lu |
| 2025 | Architectural Vulnerability and Reliability Challenges in AI Text Annotation: A Survey-Inspired Framework with Independent Probability Assessment | arXiv 2502.19679 | Shi-Evans 2023 | résumé lu |
| 2025 | Artificial intelligence use and scientific innovation | doi 10.1002/asi.70043 | Sourati-Evans 2023 | résumé lu |
| 2025 | Artificially intelligent agents in the social and behavioral sciences: A history and outlook | arXiv 2510.05743 | Sourati-Evans 2023 | résumé lu |
| 2025 | Assessing the scientific and economic impacts of the experiments conducted onboard the International Space Station | doi 10.1038/s41526-025-00485-w | Shi-Evans 2023 | résumé lu |
| 2025 | AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise | arXiv 2507.00310 | Shi-Evans 2023 | résumé lu |
| 2025 | Big Data and the Computational Social Science of Entrepreneurship and Innovation | arXiv 2505.08706 | Sourati-Evans 2023, Shi-Evans 2023 | résumé lu |
| 2025 | Can Generative AI Produce Novel Evidence? | doi 10.1017/psa.2025.10123 | Sourati-Evans 2023 | résumé lu |
| 2025 | CHIMERA: A Knowledge Base of Scientific Idea Recombinations for Research Analysis and Ideation | arXiv 2505.20779 | Shi-Evans 2023 | résumé lu |
| 2025 | Cultural Alien Sampler: Open-ended art generation balancing originality and coherence | arXiv 2510.20849 | Sourati-Evans 2023 | résumé lu |
| 2025 | Curie: Toward Rigorous and Automated Scientific Experimentation with AI Agents | arXiv 2502.16069 | Sourati-Evans 2023 | résumé lu |
| 2025 | Cyber Shadows: Neutralizing Security Threats With AI and Targeted Policy Measures | arXiv 2501.09025 | Sourati-Evans 2023 | résumé lu |
| 2025 | Deep Ideation: Designing LLM Agents to Generate Novel Research Ideas on Scientific Concept Network | arXiv 2511.02238 | Sourati-Evans 2023 | résumé lu |
| 2025 | Deep Learning and COVID-19: Two Pathways to Scientific Evolution | doi 10.3390/app15168912 | Shi-Evans 2023 | résumé lu |
| 2025 | Discovery Learning accelerates battery design evaluation | arXiv 2508.06985 | Sourati-Evans 2023 | résumé lu |
| 2025 | Empowering Scientific Workflows with Federated Agents | arXiv 2505.05428 | Sourati-Evans 2023 | résumé lu |
| 2025 | Explaining Disparities in Paper Impact across Similar-Level Journals: An Analysis of Sociology Publications | doi 10.5530/jscires.20251824 | Shi-Evans 2023 | résumé lu |
| 2025 | Exploring Novelty Differences between Industry and Academia: A Knowledge Entity-centric Perspective | arXiv 2603.19319 | Shi-Evans 2023 | résumé lu |
| 2025 | From Semantic Modeling to Precision Radiotherapy: An AI Framework Linking Radiobiology, Oncology, and Public Health Integration | doi 10.3390/biomedicines13122862 | Shi-Evans 2023 | résumé lu |
| 2025 | Generative AI and academic scientists in US universities: Perception, experience, and adoption intentions | doi 10.1371/journal.pone.0330416 | Sourati-Evans 2023 | résumé lu |
| 2025 | How do intra- and inter-organisational collaboration affect research performance? Evidence from German universities | doi 10.1016/j.joi.2025.101675 | Shi-Evans 2023 | non lu |
| 2025 | IDRBench: Understanding the Capability of Large Language Models on Interdisciplinary Research | arXiv 2507.15736 | Shi-Evans 2023 | résumé lu |
| 2025 | In-depth Research Impact Summarization through Fine-Grained Temporal Citation Analysis | arXiv 2505.14838 | Shi-Evans 2023 | résumé lu |
| 2025 | Intelligent Innovation Dataset on Scientific Research Outcomes and Patents | doi 10.23919/jsc.2024.0033 | Shi-Evans 2023 | résumé lu |
| 2025 | Interdisciplinary research enhances scientists’ career resilience and long-term benefits: evidence from a large-scale bibliographic analysis | doi 10.1007/s11192-025-05349-4 | Shi-Evans 2023 | non lu |
| 2025 | Knowledge-Centered Dual-Process Reasoning for Math Word Problems With Large Language Models | doi 10.1109/TKDE.2025.3556367 | Sourati-Evans 2023 | résumé lu |
| 2025 | Large AI models are cultural and social technologies. | doi 10.1126/science.adt9819 | Sourati-Evans 2023 | résumé lu |
| 2025 | Mapping product development trajectories: product citation network | doi 10.1007/s11192-025-05395-y | Sourati-Evans 2023, Shi-Evans 2023 | non lu |
| 2025 | Measuring academic cocoon from disparity and diversity perspectives | doi 10.1007/s11192-025-05290-6 | Shi-Evans 2023 | résumé lu |
| 2025 | Measuring Combinatorial Creativity in Large Language Models and Humans | arXiv 2509.21043 | Shi-Evans 2023 | résumé lu |
| 2025 | Measuring the growth of infectious disease modelling publications and their impact on policymaking: a Large Language Model-assisted bibliometric review | doi 10.1101/2025.06.12.25328864 | Shi-Evans 2023 | résumé lu |
| 2025 | Membership in team science institute enhances diversity of researchers’ collaboration networks | doi 10.1371/journal.pone.0322943 | Shi-Evans 2023 | résumé lu |
| 2025 | Mining Collective Intelligence and Predicting Disruptive Paradigm Shifts via Human‐Aware AI | doi 10.1002/pra2.1298 | Sourati-Evans 2023 | résumé lu |
| 2025 | Nonlinear effects of spatial determinants on the popularity of scientific fields: Evidence from 40 years of computer science | doi 10.1016/j.eswa.2025.130315 | Shi-Evans 2023 | non lu |
| 2025 | Objective Measurement of AI Literacy: Development and Validation of the AI Competency Objective Scale (AICOS) | arXiv 2503.12921 | Sourati-Evans 2023 | résumé lu |
| 2025 | OmniScientist: Toward a Co-evolving Ecosystem of Human and AI Scientists | arXiv 2511.16931 | Sourati-Evans 2023 | résumé lu |
| 2025 | Personalization of an Intelligent Assistant for Complex Sociotechnical Systems | doi 10.1109/RusAutoCon65989.2025.11177263 | Sourati-Evans 2023 | résumé lu |
| 2025 | Preserving security in a world with powerful AI Considerations for the future Defense Architecture | arXiv 2511.05714 | Sourati-Evans 2023 | résumé lu |
| 2025 | Quantifying spatial–temporal citation diffusion of individual papers in knowledge space | doi 10.1002/asi.70021 | Shi-Evans 2023 | résumé lu |
| 2025 | Recent strides in artificial intelligence for predicting thermoelectric properties and materials discovery | doi 10.1088/2515-7655/adba87 | Sourati-Evans 2023 | résumé lu |
| 2025 | Repeat collaboration and scientific innovation: evidence from dynamic ego networks of Nobel laureates | doi 10.1057/s41599-025-05887-5 | Sourati-Evans 2023 | résumé lu |
| 2025 | Research on Novelty Measurement Indicator of Academic Papers Based on the Atypical Recombination of Knowledge | arXiv 2512.18979 | Shi-Evans 2023 | résumé lu |
| 2025 | Research productivity and novelty under different funding models: evidence from NIH-funded research projects | doi 10.1007/s11192-025-05370-7 | Shi-Evans 2023 | non lu |
| 2025 | Scientific judgment drifts over time in AI ideation | arXiv 2511.04964 | Shi-Evans 2023 | résumé lu |
| 2025 | Simulating Subjects: The Promise and Peril of Artificial Intelligence Stand-Ins for Social Agents and Interactions | doi 10.1177/00491241251337316 | Sourati-Evans 2023, Shi-Evans 2023 | résumé lu |
| 2025 | Small but not least changes: The art of creating disruptive innovations | doi 10.1016/j.joi.2025.101703 | Shi-Evans 2023 | non lu |
| 2025 | Stop treating 'AGI' as the north-star goal of AI research | arXiv 2502.03689 | Shi-Evans 2023 | résumé lu |
| 2025 | Subattojoule Electrical Switching in a Two-Dimensional TaSe2 Oxide Device with High Endurance. | doi 10.1021/acs.nanolett.4c05242 | Sourati-Evans 2023 | résumé lu |
| 2025 | The distinctive innovation patterns and network embeddedness of scientific prizewinners | doi 10.1073/pnas.2424143122 | Shi-Evans 2023 | résumé lu |
| 2025 | The influence of grant renewal on research content: evidence from NIH-funded PIs | doi 10.1007/s11192-025-05295-1 | Shi-Evans 2023 | non lu |
| 2025 | The Sharply Decreasing Disruptiveness of HCI | doi 10.1145/3706598.3713917 | Shi-Evans 2023 | résumé lu |
| 2025 | Topic Modeling and Link-Prediction for Material Property Discovery | arXiv 2507.06139 | Sourati-Evans 2023 | résumé lu |
| 2025 | Towards autonomous quantum physics research using LLM agents with access to intelligent tools | arXiv 2511.11752 | Shi-Evans 2023 | résumé lu |
| 2025 | Transformational Creativity in Science: A Graphical Theory | arXiv 2504.18687 | Shi-Evans 2023 | résumé lu |
| 2025 | Triadic Novelty: A Structural Typology of Science Innovation | arXiv 2506.17851 | Shi-Evans 2023 | résumé lu |
| 2025 | Triadic Novelty: A Typology and Measurement Framework for Recognizing Novel Contributions in Science | doi 10.48550/arXiv.2506.17851 | Shi-Evans 2023 | non lu |
| 2025 | Uncovering multi-technology convergence patterns with hypergraphs: Evolution and prediction using patent data | arXiv 2509.15521 | Shi-Evans 2023 | lu sur PDF |
| 2025 | Uncovering simultaneous breakthroughs with a robust measure of disruptiveness | arXiv 2502.16845 | Shi-Evans 2023 | résumé lu |
| 2025 | Understanding the relationship between interdisciplinary knowledge and disruption in science | doi 10.1177/01655515251330614 | Shi-Evans 2023 | résumé lu |
| 2025 | Unraveling topic switching and innovation in science | doi 10.1016/j.ipm.2025.104171 | Shi-Evans 2023 | non lu |
| 2025 | Unveiling citation peaks: How innovation faces delayed recognition in science | doi 10.1016/j.ipm.2025.104100 | Shi-Evans 2023 | non lu |
| 2025 | Would Archimedes Shout “Eureka” with Algorithms? The Hidden Hand of Algorithmic Design in Idea Generation, the Creation of Ideation Bubbles, and How Experts Can Burst Them | doi 10.5465/amj.2023.1307 | Sourati-Evans 2023 | non lu |
| 2024 | A framework for predicting scientific disruption based on graph signal processing | doi 10.1016/j.ipm.2024.103863 | Shi-Evans 2023 | non lu |
| 2024 | A systematic review of AI literacy scales | doi 10.1038/s41539-024-00264-4 | Sourati-Evans 2023 | résumé lu |
| 2024 | Academic collaboration on large language model studies increases overall but varies across disciplines | arXiv 2408.04163 | Shi-Evans 2023 | résumé lu |
| 2024 | Advanced Design of Soft Robots with Artificial Intelligence | doi 10.1007/s40820-024-01423-3 | Sourati-Evans 2023 | résumé lu |
| 2024 | Alien Recombination: Exploring Concept Blends Beyond Human Cognitive Availability in Visual Art | arXiv 2411.11494 | Sourati-Evans 2023, Shi-Evans 2023 | résumé lu |
| 2024 | Are disruptive papers more likely to impact technology and society? | doi 10.1002/asi.24947 | Shi-Evans 2023 | résumé lu |
| 2024 | Artificial intelligence and consumer behavior: From predictive to generative AI | doi 10.1016/j.jbusres.2024.114720 | Sourati-Evans 2023 | non lu |
| 2024 | Artificial Intelligence in Diagnosing and Managing Vascular Surgery Patients: An Experimental Study Using the GPT-4 Model. | doi 10.1016/j.avsg.2024.11.014 | Sourati-Evans 2023 | résumé lu |
| 2024 | BEYOND HAIR LOSS: EXPLORING THE EVOLUTION OF ANDROGENETIC ALOPECIA RESEARCH BASED ON TEXT MINING AND BIBLIOMETRICS | doi 10.61784/wms3010 | Shi-Evans 2023 | résumé lu |
| 2024 | Can novelty scores on papers shift the power dynamics in scientific publishing? | doi 10.1038/d41586-024-04021-w | Shi-Evans 2023 | non lu |
| 2024 | Debunking revolutionary paradigm shifts: evidence of cumulative scientific progress across science | doi 10.1098/rspa.2024.0141 | Shi-Evans 2023 | résumé lu |
| 2024 | DeepDiveAI: Identifying AI-Related Documents in Large Scale Literature Dataset | arXiv 2408.12871 | Shi-Evans 2023 | résumé lu |
| 2024 | Determining Research Priorities Using Machine Learning | arXiv 2407.02533 | Shi-Evans 2023 | résumé lu |
| 2024 | Discovering emergent connections in quantum physics research via dynamic word embeddings | arXiv 2411.06577 | Sourati-Evans 2023, Shi-Evans 2023 | résumé lu |
| 2024 | Dissecting embedding method: learning higher-order structures from data | arXiv 2410.10917 | Shi-Evans 2023 | résumé lu |
| 2024 | Do more heads imply better performance? An empirical study of team thought leaders' impact on scientific team performance | arXiv 2606.26483 | Sourati-Evans 2023 | résumé lu |
| 2024 | Does the use of unusual combinations of datasets contribute to greater scientific impact? | arXiv 2402.05024 | Shi-Evans 2023 | résumé lu |
| 2024 | Dyport: dynamic importance-based biomedical hypothesis generation benchmarking technique | doi 10.1186/s12859-024-05812-8 | Sourati-Evans 2023 | résumé lu |
| 2024 | Evolving AI Collectives to Enhance Human Diversity and Enable Self-Regulation | arXiv 2402.12590 | Sourati-Evans 2023, Shi-Evans 2023 | résumé lu |
| 2024 | Factors influencing the research impact in cancer research: a collaboration and knowledge network analysis | doi 10.1186/s12961-024-01205-8 | Shi-Evans 2023 | résumé lu |
| 2024 | Forecasting high-impact research topics via machine learning on evolving knowledge graphs | arXiv 2402.08640 | Sourati-Evans 2023, Shi-Evans 2023 | résumé lu |
| 2024 | From Text to Life: On the Reciprocal Relationship between Artificial Life and Large Language Models | arXiv 2407.09502 | Sourati-Evans 2023 | résumé lu |
| 2024 | Generating Interesting Scientific Ideas using Knowledge Graphs and LLMs: Evaluations with 100 Research Group Leaders | arXiv 2405.17044 | Sourati-Evans 2023, Shi-Evans 2023 | résumé lu |
| 2024 | Generative AI in Marketing and Principles for Ethical Design and Deployment | doi 10.1177/07439156241309874 | Sourati-Evans 2023 | résumé lu |
| 2024 | Generative Künstliche Intelligenz | doi 10.1026/0033-3042/a000699 | Sourati-Evans 2023 | résumé lu |
| 2024 | High Resilient Asymmetry and Anomaly Detection Based on Data Causality | doi 10.3390/sym16070819 | Sourati-Evans 2023 | résumé lu |
| 2024 | High-Impact Innovations and Hidden Gender Disparities in Inventor-Evaluator Networks | arXiv 2408.00905 | Shi-Evans 2023 | résumé lu |
| 2024 | How AI Ideas Affect the Creativity, Diversity, and Evolution of Human Ideas: Evidence From a Large, Dynamic Experiment | arXiv 2401.13481 | Sourati-Evans 2023 | résumé lu |
| 2024 | Informatics and Artificial Intelligence-Guided Assessment of the Regulatory and Translational Research Landscape of First-in-Class Oncology Drugs in the United States, 2018-2022. | doi 10.1200/CCI.24.00087 | Shi-Evans 2023 | résumé lu |
| 2024 | Information Skills applied to Scientometrics: a Literature Systematic Review | doi 10.56294/hl2024.512 | Sourati-Evans 2023 | résumé lu |
| 2024 | Intellectual Property and Creative Machines | doi 10.3386/w32698 | Shi-Evans 2023 | résumé lu |
| 2024 | Knowledge transfer, knowledge gaps, and knowledge silos in citation networks | arXiv 2406.03921 | Shi-Evans 2023 | résumé lu |
| 2024 | Large Language Models and the Wisdom of Small Crowds | doi 10.1162/opmi_a_00144 | Sourati-Evans 2023 | résumé lu |
| 2024 | LLM Voting: Human Choices and AI Collective Decision Making | arXiv 2402.01766 | Sourati-Evans 2023 | résumé lu |
| 2024 | Many Heads Are Better Than One: Improved Scientific Idea Generation by A LLM-Based Multi-Agent System | arXiv 2410.09403 | Shi-Evans 2023 | résumé lu |
| 2024 | Mutual benefits of social learning and algorithmic mediation for cumulative culture | arXiv 2410.00780 | Sourati-Evans 2023 | résumé lu |
| 2024 | On the emergence of interdisciplinary scientific fields: (how) does it relate to science convergence? | doi 10.1016/j.respol.2024.105026 | Shi-Evans 2023 | non lu |
| 2024 | Positive Deviance Underlies Successful Science: Normative Methodologies Risk Throwing out the Baby With the Bathwater | doi 10.1177/10892680241235120 | Sourati-Evans 2023 | résumé lu |
| 2024 | PubMed knowledge graph 2.0: Connecting papers, patents, and clinical trials in biomedical science | arXiv 2410.07969 | Sourati-Evans 2023 | résumé lu |
| 2024 | Quantifying the use and potential benefits of artificial intelligence in scientific research | doi 10.1038/s41562-024-02020-5 | Sourati-Evans 2023 | résumé lu |
| 2024 | Retrieve to Explain: Evidence-driven Predictions with Language Models | doi 10.48550/arXiv.2402.04068 | Sourati-Evans 2023 | non lu |
| 2024 | Science of science: A multidisciplinary field studying science | doi 10.1016/j.heliyon.2024.e36066 | Shi-Evans 2023 | résumé lu |
| 2024 | Scientific hypothesis generation by large language models: laboratory validation in breast cancer treatment | arXiv 2405.12258 | Sourati-Evans 2023 | résumé lu |
| 2024 | SGML: A Python library for solution-guided machine learning | doi 10.1016/j.simpa.2024.100739 | Sourati-Evans 2023 | non lu |
| 2024 | Should we circumvent knowledge path dependency? The impact of conventional learning and collaboration diversity on knowledge creation | doi 10.1016/j.joi.2024.101597 | Shi-Evans 2023 | non lu |
| 2024 | Slow convergence: Career impediments to interdisciplinary biomedical research | doi 10.1073/pnas.2402646121 | Shi-Evans 2023 | résumé lu |
| 2024 | Static network structure cannot stabilize cooperation among large language model agents | arXiv 2411.10294 | Sourati-Evans 2023 | résumé lu |
| 2024 | The Dual-Edged Sword: Generative AI Health Assistants and the Proliferation of Cyber-Biological Threats | doi 10.64483/202412552 | Sourati-Evans 2023 | résumé lu |
| 2024 | The Paradox of Collective Certainty in Science | arXiv 2406.05809 | Sourati-Evans 2023, Shi-Evans 2023 | résumé lu |
| 2024 | The Strength of Weak Ties Between Open-Source Developers | arXiv 2411.05646 | Shi-Evans 2023 | résumé lu |
| 2024 | Unveiling the impact and dual innovation of funded research | doi 10.1016/j.joi.2023.101480 | Shi-Evans 2023 | non lu |
| 2023 | Beyond Citations: Measuring Novel Scientific Ideas and their Impact in Publication Text | arXiv 2309.16437 | Shi-Evans 2023 | résumé lu |
| 2023 | Beyond Citations: Text-Based Metrics for Assessing Novelty and its Impact in Scientific Publications | — | Shi-Evans 2023 | non lu |
| 2023 | Characteristics of ChatGPT users from Germany: Implications for the digital divide from web tracking data | arXiv 2309.02142 | Sourati-Evans 2023 | résumé lu |
| 2023 | China and the U.S. produce more impactful AI research when collaborating together | arXiv 2304.11123 | Shi-Evans 2023 | résumé lu |
| 2023 | Conservative adventurers have more future academic impact | arXiv 2306.16643 | Sourati-Evans 2023 | résumé lu |
| 2023 | Facilitating Interdisciplinary Knowledge Transfer with Research Paper Recommender Systems | arXiv 2309.14984 | Shi-Evans 2023 | résumé lu |
| 2023 | Hypotheses devised by AI could find ‘blind spots’ in research | doi 10.1038/d41586-023-03596-0 | Sourati-Evans 2023 | non lu |
| 2023 | Machine culture | arXiv 2311.11388 | Sourati-Evans 2023 | résumé lu |
| 2023 | Network community detection via neural embeddings | arXiv 2306.13400 | Sourati-Evans 2021, Sourati-Evans 2023 | résumé lu |
| 2023 | Scientific Knowledge Combination in Networks: New Perspectives on Analyzing Knowledge Absorption and Integration | — | Shi-Evans 2023 | non lu |
| 2023 | Scientists' bounded mobility on the epistemic landscape | arXiv 2307.10096 | Shi-Evans 2023 | résumé lu |
| 2022 | A doc2vec and local outlier factor approach to measuring the novelty of patents | doi 10.1016/j.techfore.2021.121294 | Shi-Evans 2023 | non lu |
| 2022 | Aging and the narrowing of scientific innovation. | arXiv 2202.04044 | Shi-Evans 2023 | résumé lu |
| 2022 | Complementary artificial intelligence designed to augment human discovery | arXiv 2207.00902 | Sourati-Evans 2021 | résumé lu |
| 2022 | Destructive creation, creative destruction, and the paradox of innovation science | arXiv 2210.10661 | Sourati-Evans 2021, Shi-Evans 2023 | résumé lu |
| 2022 | Economic impacts of AI-augmented R&D | arXiv 2212.08198 | Sourati-Evans 2023 | résumé lu |
| 2022 | Instruments, agents, and artificial intelligence: novel epistemic categories of reliability | doi 10.1007/s11229-022-03975-6 | Sourati-Evans 2021 | non lu |
| 2022 | The Elements of Cultural Power: Novelty, Emotion, Status, and Cultural Capital | doi 10.1177/00031224221123030 | Shi-Evans 2023 | résumé lu |
| 2021 | Foundations of Intelligence in Natural and Artificial Systems: A Workshop Report | arXiv 2105.02198 | Sourati-Evans 2021 | résumé lu |
| 2021 | Is Interdisciplinary Collaboration Research More Disruptive Than Monodisciplinary Research? | doi 10.1002/pra2.454 | Shi-Evans 2023 | résumé lu |
| 2021 | New directions in science emerge from disconnection and discord | arXiv 2103.03398 | Shi-Evans 2023 | résumé lu |
| 2021 | The Social Abduction of Science | arXiv 2111.13251 | Sourati-Evans 2021, Shi-Evans 2023 | résumé lu |
| 2021 | Understanding the long-term emergence of autonomous vehicles technologies | doi 10.1016/J.TECHFORE.2021.120852 | Shi-Evans 2023 | non lu |
| 2020 | Local similarity and global variability characterize the semantic space of human languages | doi 10.1073/pnas.2300986120 | Shi-Evans 2023 | résumé lu |
| — | AI and International Security Pathways of Impact and Key Uncertainties | — | Sourati-Evans 2023 | non lu |
| — | Automating Pursuitworthiness: Four Concerns About The Proper Roles for Machine Learning Systems in Scientific Discovery | — | Sourati-Evans 2023 | non lu |
| — | STIP lab | — | Shi-Evans 2023 | non lu |
| — | The Delayed Recognition of Scientific Novelty | — | Shi-Evans 2023 | non lu |
| — | The innovator's balance between academic social capital and disruptive innovation | doi 10.1016/j.ipm.2025.104382 | Shi-Evans 2023 | non lu |
