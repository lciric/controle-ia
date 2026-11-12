# Transcription des captures du papier ASIS&T 2025, doi 10.1002/pra2.1298 — v1

31 octobre 2026. Session-depot (sous-agent d'exécution, lecture des images). Aucun téléchargement, aucune dépense.

**Source** : 24 captures d'écran de la visionneuse de l'éditeur (`asistdl.onlinelibrary.wiley.com/doi/epdf/10.1002/pra2.1298`, prises le 31 octobre 2026 vers 12:38–12:40, heure locale de la capture), versées par conv-audit sur `origin/canal/conv-audit-n04` sous `docs/sources/captures/asist-2025-pra2-1298-v1/` ; chaque empreinte a été recalculée et concorde avec son `.sha256` compagnon. **Ce n'est pas un PDF empreinté** : selon R7, cette transcription n'est opposable que si Lazar accepte les captures empreintées comme source (nœud pour lui). Les numéros de page cités sont ceux du pied de page imprimé (« ASIS&T Annual Meeting 2025 — 799 … 807 »), sinon ceux de la visionneuse (« Page n / 10 »).

**Titre** (d'après le DOI et la fiche de conv-audit ; **le bloc de titre n'est pas dans les captures**) : « Mining Collective Intelligence and Predicting Disruptive Paradigm Shifts via Human-Aware AI », 88th Annual Meeting of the ASIS&T, Nov. 14–18, 2025, Washington, DC, USA ; « Long Papers », pp. 799–807 (et une dixième page, références). Auteurs : non visibles ; la section « Author attribution » donne les initiales A.J.Y., S.Y., Z.S.X., Z.Y., D.S. (la liste « Yang, Shi, Zhao, Zhang, Deng » de l'inventaire n'est pas vérifiée sur les captures).

**Complétude.** Le corps du texte est complet de l'ABSTRACT aux REFERENCES, captures enchaînées avec recouvrement. Manquent ou sont incertains :
1. le haut de la page 1 (titre, auteurs, affiliations, adresse) ;
2. le début de la première phrase de l'INTRODUCTION (« … punctuated by rare, transformative paradigm shifts ») : absent dans les deux captures de cette page (01 et 24), coupé à l'affichage ou absent du PDF ; indécidable ;
3. la légende de la Figure 1 (non vue ; les captures 06 et 07 montrent le schéma seul) ;
4. une ligne de la section « Author attribution », lisible seulement en partie à la jointure des captures 20 et 21 ;
5. au-delà de la dernière référence (page 10), rien n'est visible.
**Aucune section « Results », « Experiments » ou « Evaluation » n'existe** : après la méthode (pages 799–805) viennent la Figure 3 puis la CONCLUSION (page 805). Le papier ne rapporte aucun chiffre de résultat, aucune table, aucun jeu de test, aucune base de comparaison.
**Défauts éditoriaux relevés** : le texte cite par numéros ([2, 3], [3], [18], [18, 19]) alors que la liste de références est en auteur-année, non numérotée, de 26 entrées ; [18] est cité pour le LSTM, qu'aucune référence de la liste ne désigne.

La capture 24 est un doublon de la capture 01. Le texte est reproduit en anglais tel qu'affiché ; les formules sont transcrites en notation linéaire.

## Capture 01 — empreinte `39d422996def…` — page 1 / 10 de la visionneuse (page imprimée non visible ; haut de page coupé : titre, auteurs et affiliations hors champ)

ABSTRACT
Scientific progress hinges on the interplay between collective intelligence and transformative paradigm shifts, yet predicting these revolutionary events remains a persistent challenge. This study introduces a novel human-aware AI framework that integrates the evolution of knowledge structures with the social dynamics of scientific communities to forecast groundbreaking innovations. Leveraging graph convolutional neural networks (GCNNs), we construct a hybrid higher-order network that unifies a domain knowledge graph—derived from millions of scientific publications—with a scientist collaboration-competition space, capturing both cooperative and competitive interactions among researchers. This approach quantifies collective intelligence by generating embeddings that reflect the intricate relationships between knowledge content and human agency. By analyzing thematic knowledge distances and social proximities within this integrated network, we identify pairs of scientific domains poised for disruptive convergence. Dynamic analysis of these embeddings further enables temporally precise predictions of paradigm shifts. Applied to the life sciences, our framework successfully aligns with historical milestones, such as Nobel Prize-winning discoveries, demonstrating its predictive power. This work offers a scalable, interpretable tool for anticipating scientific revolutions, bridging the gap between knowledge evolution and social dynamics, and providing actionable insights for fostering innovation across disciplines.

KEYWORDS
Collective intelligence, paradigm shifts, graph convolutional neural networks (GCNNs), collaboration-competition space, human-aware AI

INTRODUCTION
[début de phrase hors champ] punctuated by rare, transformative paradigm shifts that redefine our understanding of the natural world (Duan et al., 2025; Fortunato et al., 2018; Hill & Stein, 2025a, 2025b; Krieger et al., 2024; Wang & Barabási, 2021; Yang et al., 2025). Collective intelligence, the enhanced problem-solving capacity emerging from group interactions, underpins the steady growth of knowledge through collaboration, peer review, and resource sharing within scientific communities (Belikov et al., 2022; Evans & Foster, 2011; Kang et al., 2025; Sourati & Evans, 2023). In contrast, paradigm shifts, as conceptualized by Kuhn (Kuhn, 1962; Kuhn, 1977), mark revolutionary discontinuities—moments when anomalies dismantle prevailing frameworks, giving way to radical new perspectives, as exemplified

## Capture 02 — empreinte `3c3b72228a61…` — page 1 / 10 (suite ; pied de page : « 88th Annual Meeting of the Association for Information Science & Technology | Nov. 14 – 18, 2025 | Washington, DC, USA » ; « ASIS&T Annual Meeting 2025 — 799 — Long Papers »)

[recouvrement avec la capture 01] by the Copernican revolution or the advent of quantum mechanics. While the former ensures incremental progress, the latter drives exponential leaps, often with profound societal impact. Yet, despite their significance, predicting these disruptive events remains an elusive goal, hampered by the complexity of integrating the evolution of scientific knowledge with the human dynamics that catalyze innovation.

The advent of artificial intelligence (AI) has transformed the landscape of scientific discovery, enabling the analysis of vast datasets to uncover hidden patterns and accelerate research across domains such as drug discovery, materials science, and climate modeling (Gao & Wang, 2024; Sourati & Evans, 2023; Wang et al., 2023). Recent advances in graph-based AI, particularly graph convolutional neural networks (GCNNs), have proven adept at modeling relational systems inherent in scientific data, such as citation networks and knowledge graphs. Simultaneously, the availability of large-scale bibliographic repositories, like PubMed and OpenAlex, offers unprecedented opportunities to map the knowledge space comprehensively. However, current AI-driven approaches predominantly treat scientific literature as an abstract entity, focusing either on knowledge evolution through bibliometric trends or on collaboration networks in isolation (Franzoni & Stephan, 2023; Ghosal et al., 2022; Hoppe et al., 2023; Kumari et al., 2022). This siloed perspective overlooks a critical reality: scientific breakthroughs emerge not merely from ideas but from the interplay of those ideas with the social fabric of the researchers who develop and debate them.

A growing body of evidence suggests that social proximity among scientists—whether through collaboration or competition—can amplify the potential for disruptive innovation, particularly when bridging distant knowledge domains (Lin et al., 2023; Wu et al., 2019; Xu et al., 2022; Xu et al., 2024; Yang, Ding, et al., 2024; Yang, Xu, et al., 2024; Yang et al., 2022). Yet, few frameworks effectively unify these dimensions into a predictive model capable of anticipating paradigm shifts. Traditional scientometric methods, while adept at tracking emerging trends or mapping collaboration networks, rarely connect these insights to the likelihood of transformative outcomes.

## Capture 03 — empreinte `d47d7f73f878…` — page 2 / 10 (page imprimée 800 présumée, non visible)

Moreover, the temporal dynamics of knowledge convergence and the role of human agency remain underexplored, leaving a critical gap in our ability to forecast when and where scientific revolutions might occur.

Here, we propose a pioneering human-aware AI framework to address these challenges, integrating a domain knowledge graph with a scientist collaboration-competition space within a hybrid higher-order network. Using GCNNs, we generate embeddings that capture the collective intelligence arising from the interplay between scientific content and researcher interactions. By analyzing knowledge distances and social proximities, we identify thematic pairs with high disruptive potential, while dynamic modeling of these embeddings enables us to predict the timing of paradigm shifts. Applied to the life sciences, our approach not only reveals interdisciplinary connections but also aligns with historical breakthroughs, such as Nobel Prize-winning discoveries, validating its efficacy. This framework advances predictive information science by offering a scalable, interpretable tool to anticipate scientific revolutions, with implications for research strategy, funding allocation, and the acceleration of innovation across disciplines. In doing so, it redefines our understanding of scientific progress as a deeply human endeavor, shaped by both the ideas we pursue and the communities we build.

DOMAIN KNOWLEDGE GRAPH AND COLLABORATION-COMPETITION SPACE CONSTRUCTION
To systematically analyze the evolution of scientific knowledge and the dynamics of researcher interactions, we developed a robust methodology for constructing a comprehensive domain knowledge graph and a nuanced scientist collaboration-competition space. Our approach, illustrated schematically in the first part of Figure 1 (using the life sciences as a representative domain), involves a multi-stage process for knowledge extraction and network construction.

Initially, we curated a large-scale corpus comprising tens of millions of scientific publications, including abstracts and full texts, from prominent databases such as PubMed and OpenAlex. This textual data underwent rigorous preprocessing, encompassing sentence segmentation and tokenization, followed by expert-guided manual annotation to establish a high-quality training set for subsequent automated processes. We then employed Named Entity Recognition (NER) to automatically identify and classify key entities within the preprocessed text of each

## Capture 04 — empreinte `0c578e6ff631…` — page 2 / 10 (suite)

[recouvrement] publication. To enhance the robustness and accuracy of entity recognition, we utilized an ensemble of four fine-tuned pre-trained language models, each trained with diverse hyperparameter configurations. The outputs of these individual NER models were aggregated using a voting mechanism to yield a consensus set of extracted entities.

Following entity extraction, we implemented a comprehensive entity cleaning and normalization procedure. This involved employing the Abbreviation Plus Pseudo-Precision method to resolve abbreviations and integrating data from established resources such as MeSH and PubTator for robust synonym mapping and entity standardization. Subsequently, we performed Relation Extraction (RE) to identify and categorize the semantic relationships between the extracted entities. We developed both single-sentence and multi-sentence RE models, fine-tuning PubMedBERT with multiple hyperparameter settings and combining the results through a voting strategy to maximize the reliability of the extracted relationships. Finally, to enrich the relational structure of our knowledge representation, we integrated entity linkage information from external, curated databases such as Hetionet, thereby constructing a comprehensive domain knowledge graph.

While our primary analysis focuses on the paper level, we acknowledge that future research could fruitfully explore the knowledge entity level to provide even finer-grained insights. Utilizing the constructed domain knowledge graph, we proceeded to build a paper-level network, denoted as G_K = (V_K, E_K), where each paper v ∈ V_K represents a node. An edge (u, v) ∈ E_K signifies a connection between two papers, established either through the sharing of one or more identical knowledge entities or through the existence of any relational link between their constituent entities within the domain knowledge graph. Furthermore, to capture the semantic content of each paper, we computed a 300-dimensional word embedding vector for each identified knowledge entity using PubMedBERT. A central embedding vector x_v for each paper v was then derived to represent its overall knowledge content.

In the scientific domain, innovation frequently arises from the convergence of diverse knowledge elements, and the collaborative or competitive interactions among scientists play a crucial role in fostering collective intelligence. To uncover these intricate dynamics, we defined a scientist collaboration-competition space, denoted as G_S = (S, E_S), where S is the set of is_i ∈ S, s_j ∈ S is defined based on two key aspects of their interactions: [sic, texte tel qu'affiché]

## Capture 05 — empreinte `de5e9bc89283…` — page 2 / 10 (fin, pied « ASIS&T Annual Meeting 2025 — 800 — Long Papers ») puis début de la page 3

Collaboration: If scientists s_i and s_j have co-authored one or more scientific publications, then an edge (s_i, s_j) ∈ E_S is established. The weight of this edge, w(s_i, s_j), is quantified by the total number of joint publications between s_i and s_j, reflecting the strength of their collaborative relationship.

Competition: In the absence of direct collaboration, we infer potential competition between scientists whose research exhibits significant overlap in terms of knowledge entities. Specifically, if papers authored by s_i (set P_i) and s_j (set P_j) share identical knowledge entities or contain entities that are directly connected within the domain knowledge graph, we quantify the intensity of this research overlap, c(s_i, s_j), based on the connection density within G_K:

  c(s_i, s_j) = |{(u,v) ∈ E_K | u ∈ P_i, v ∈ P_j}| / (|P_i| · |P_j|).

Here, |{(u, v) ∈ E_K | u ∈ P_i, v ∈ P_j}| represents the total number of edges in the knowledge graph G_K that connect any paper u authored by s_i to any paper v authored by s_j, and |P_i| · |P_j| represents the total number of possible paper pairs between the two scientists. A higher value of c(s_i, s_j) suggests a greater degree of research overlap and, consequently, a higher potential for intellectual competition.

## Capture 06 — empreinte `51c653035a19…` — page 3 / 10 : Figure 1, partie haute (schéma ; texte des étiquettes)

Titre du cadre : « DOMAIN KNOWLEDGE GRAPH AND COLLABORATION-COMPETITION SPACE CONSTRUCTION ».
Chaîne : « Scientific Literature: PubMed+OpenAlex » → « Preprocessing: Abbreviation + Pseudo-Precision » → « Entity Extraction (NER) » → « Entity Cleaning and Normalization » → « Relation Extraction (RE) » → « External Knowledge Integration ».
Encadré gauche : « BIO Knowledge Base » — Diseases, Genes/proteins, Chemical compounds, Species, Genetic variation, Cell lines (accolade « Entity Type Annotation ») ; « Preprocessing Abbreviation+ Pseudo-Precision » ; MeSH, PubTator, MONDO, DOID, UMLS, SYMP, HP, OMIM, PubChem, DrugBank, Hetionet, PrimeKG, Cellosaurus (accolade « Synonym Mapping »).
Bloc NER : RoBERTa, ClinicalBERT, BlueBERT, PubMedBERT ; « Ensemble deep learning models » ; « Voting Merge Predictions ».
Bloc RE : « Single-Sentence RE », « Multi-Sentence RE », PubMedBERT, « Voting Merge Predictions ».
Bloc connaissances externes : « Hetionet », « primeKG », « recount3 » (graphe illustratif ; légende interne « anti-ictogenic / unknown / ictogenic », petits caractères [illisible pour le reste]).

## Capture 07 — empreinte `a4a1b90007a6…` — page 3 / 10 : Figure 1, partie basse

Étiquettes : « Domain Knowledge Graph » → « Scientist Competition Space » ; « Collaboration » ; « (s_i, s_j) ∈ E_S » ; « Competition Measure  c(s_i, s_j) = |{(u, v) ∈ E_K | u ∈ P_i, v ∈ P_j}| / (|P_i| · |P_j|) » ; « Scientist Collaboration-Competition Space G_S = (S, E_S) ». Illustrations : nuage de points de type projection d'embeddings, documents, auteurs, diagrammes circulaires par auteur (sans légende lisible). La légende (« Figure 1. … ») n'apparaît pas dans les captures 06 et 07 : [légende de la Figure 1 absente des captures, ou hors champ].

## Capture 08 — empreinte `f0e96ba201f6…` — page 4 / 10

It is important to note that our representation in G_S does not explicitly delineate between collaboration and competition through distinct edge types. Instead, the network captures a spectrum of interactions, ranging from direct collaboration to indirect competition inferred through shared or related knowledge. Furthermore, our definition of competition extends beyond mere topical similarity to encompass a broader range of interconnected knowledge entities within the domain knowledge graph. Consequently, the constructed scientist collaboration-competition space G_S effectively captures rich interdisciplinary connections among scientists, providing a crucial foundation for mining collective intelligence and ultimately predicting disruptive paradigm shifts in scientific progress.

MINING COLLECTIVE INTELLIGENCE VIA HYBRID HIGHER-ORDER NETWORKS AND GCNN
To effectively mine the collective intelligence embedded within the scientific literature and the interactions of scientists, we developed a novel approach that integrates the paper-paper knowledge network G_K with the scientist collaboration-competition space G_S into a unified hybrid higher-order network, denoted as H = (V, E). This network explicitly models the intricate relationships between scientific knowledge and the human agents who generate and utilize it.

The node set of our hybrid network, V = V_K ∪ S, comprises two distinct types of nodes: paper nodes V_K, representing individual scientific publications and their associated knowledge entities, and scientist nodes (S), representing the researchers themselves. The connections within this network are captured through hyperedges, where each hyperedge e ∈ E links a group of related nodes. Specifically, for each paper v ∈ V_K, we define a hyperedge e_v = A_v ∪ {v} ∪ C_v. Here, A_v ⊆ S represents the set of authors of paper v, and C_v ⊆ V_K includes other papers that are connected to v through shared or related knowledge entities within the domain knowledge graph G_K. The complete hyperedge set E is then defined as the collection of all such paper-centric hyperedges: E = {e_v | v ∈ V_K}. This hyperedge formulation allows us to model higher-order relationships, capturing the interplay between a paper, its authors, and the broader knowledge context as defined by its connections to other publications.

To quantify collective intelligence within this hybrid network, we employed a graph convolutional neural network (GCNN) to generate low-dimensional embeddings for each node, preserving both the network's connectivity

## Capture 09 — empreinte `bd5bb0b91d3c…` — page 4 / 10 (page imprimée 802)

[recouvrement] (GCNN) to generate low-dimensional embeddings for each node, preserving both the network's connectivity structure and the inherent features of the nodes. For each paper node v ∈ V_K, the initial feature vector is its 300-dimensional central embedding (x_v) derived from PubMedBERT, as described in the previous section. For each scientist node s ∈ S, the initial feature vector x_s is computed as the average of the PubMedBERT embeddings of all papers authored by that scientist:

  x_s = (1/|P_s|) Σ_{v∈P_s} x_v,

where P_s denotes the set of papers authored by scientist s, and |P_s| is the number of such papers. This aggregation provides an initial representation of a scientist based on the collective knowledge content of their publications.

To model the propagation of information and the influence of connected entities within the hybrid network, we iteratively update the node embeddings using a GCNN architecture. For a paper node v ∈ V_K, the embedding at the (l + 1)th layer, h_v^(l+1), is computed based on its embedding at the lth layer, h_v^(l), and the embeddings of its neighbors within the hyperedges it belongs to (E_v, the set of hyperedges containing v):

  h_v^(l+1) = σ( W^(l) h_v^(l) + Σ_{e∈E_v} (1/|e|) Σ_{u∈e} B^(l) h_u^(l) ).

Here, W^(l) and B^(l) are trainable weight matrices at the lth layer, σ represents the ReLU activation function, and 1/|e| serves as a normalization factor within each hyperedge, ensuring that the contribution of each neighboring node is appropriately scaled by the size of the hyperedge. This aggregation process allows the embedding of a paper to be influenced not only by its own knowledge content but also by the characteristics of its authors and the knowledge content of related papers. Similarly, the embedding of a scientist node is updated by considering the embeddings of the papers they have authored and the scientists they have collaborated with (through shared hyperedges). After l layers of this GCNN operation, the resulting embedding h_v for each paper node effectively captures both local and global structural information within the hybrid network, reflecting the complex interplay between knowledge content and human interactions.

## Capture 10 — empreinte `c72915434317…` — fin de la page 4 / 10 (pied « ASIS&T Annual Meeting 2025 — 802 — Long Papers ») puis page 5

Following the generation of these integrated embeddings, we define the probability of a paper v ∈ V_K being accessed or recognized by the broader scientific community, denoted as p_v. This probability is modeled using a softmax function over the learned embeddings:

  p_v = exp(wᵀ h_v) / Σ_{u∈V} exp(wᵀ h_u),

where wᵀ is a learnable weight vector that maps the low-dimensional embeddings to a scalar value representing the tendency of a node to be accessed. The softmax function ensures that the probabilities across all nodes in the hybrid network sum to one (Σ_{v∈V} p_v = 1). This probability p_v serves as a proxy for the paper's importance and visibility within the collective cognitive landscape of the scientific community. Furthermore, this measure can be extended to individual knowledge entities by aggregating the access probabilities of the papers in which they appear.

Crucially, because the paper embeddings h_v are derived through the GCNN operating on the hybrid network, the resulting access probability p_v inherently captures higher-order effects, such as the influence of author collaborations, competitive relationships inferred from knowledge overlap, and the interconnectedness of knowledge entities. To optimize the parameters of our GCNN model and the access probability estimation, we employ a cross-entropy loss function:

## Capture 11 — empreinte `0fc8f35f006e…` — page 5 / 10 (page imprimée 803 présumée)

  ℒ = − Σ_{v∈V} y_v log p_v,

where y_v represents the true frequency or a proxy for the real-world access or impact of paper v. By minimizing this loss, we train the model to accurately predict the relative importance and visibility of scientific publications based on the integrated knowledge and social network structures. This learned probability distribution provides a quantitative measure of the collective intelligence surrounding different scientific works and forms a crucial input for our subsequent paradigm shift prediction framework.

Figure 2 (schéma), étiquettes : « MINING COLLECTIVE INTELLIGENCE VIA HYBRID HIGHER-ORDER NETWORKS AND GCNN » ; « Domain Knowledge Graph » ; « Paper-paper network G_K = (V_K, E_K) » ; « + » ; « Scientist Collaboration-Competition Space G_S = (S, E_S) » ; « → » ; « Hybrid Node V = V_K ∪ S » ; « Hyper Edge E = {e_v | v ∈ V_K} » ; « Hybrid Node High-Order Network H = (V, E) » ; « PubMedBERT Center Embedding Vector x_v » ; « Scientist Initial Embed x_s = (1/|P_s|) Σ_{v∈P_s} x_v » ; « Graph Convolutional Neural Networks » (nœuds X1–X4, Z1–Z4, Y1, Y4).

## Capture 12 — empreinte `f4fa71091526…` — page 5 / 10 (suite)

Figure 2 (suite), étiquettes : « Quantifying information transfer in high-order networks » ; « ℒ = − Σ_{v∈V} y_v log p_v » ; « Update node embedding h_v^(l+1) = σ( W^(l) h_v^(l) + Σ_{e∈E_v} (1/|e|) Σ_{u∈e} B^(l) h_u^(l) ) » ; « Collective access probability of scientific knowledge  p_v = exp(wᵀh_v) / Σ_{u∈V} exp(wᵀh_u) ».
Légende : **Figure 2. Mining Collective Intelligence Via Hybrid Higher-Order Networks and GCNN**

PREDICTING DISRUPTIVE PARADIGM SHIFTS THROUGH DYNAMIC ANALYSIS OF KNOWLEDGE
Disruptive scientific innovations often emerge from the synergistic convergence of previously disparate knowledge domains, areas that may currently be underappreciated but possess the potential for rapid advancement due to the underlying social connectivity of the involved scientists [2, 3]. To identify and predict such transformative shifts, we focused on identifying pairs of scientific themes characterized by significant knowledge dissimilarity, close proximity within the scientist collaboration network, and a high concentration of active researchers. Furthermore, we employed dynamic embeddings and time series modeling to forecast the potential timing of these paradigm shifts.

To identify these themes, we applied the K-means clustering algorithm to the paper embeddings (h_v) derived from the GCNN, grouping the set of all papers (V_K) into K distinct scientific themes, denoted as T_1, T_2, .... The embedding of each theme, h̄_T, was calculated as the centroid of the embeddings of all papers belonging to that theme:

## Capture 13 — empreinte `cddf299cc747…` — fin de la page 5 / 10 (pied « ASIS&T Annual Meeting 2025 — 803 — Long Papers ») puis page 6

  h̄_T = (1/|T|) Σ_{v∈T} h_v.

For each pair of identified themes (T_1, T_2), we quantified the knowledge distance d_K(T_1, T_2) as the Euclidean distance between their respective theme embeddings:

  d_K(T_1, T_2) = ‖ h̄_{T_1} − h̄_{T_2} ‖_2.

A larger knowledge distance between two themes suggests a greater degree of novelty inherent in their potential combination.

To assess the social proximity between themes, we first identified the set of scientists actively contributing to each theme T_i. This scientist set, S_{T_i}, was defined as the union of the author sets (A_v) of all papers v belonging to theme T_i:

  S_{T_i} = ∪_{v∈T_i} A_v.

We then calculated the social distance d_S(T_i, T_j) between two themes as the average shortest path length between all pairs of scientists where one scientist belongs to S_{T_i} and the other belongs to S_{T_j} within the scientist collaboration-

## Capture 14 — empreinte `837fee61773f…` — page 6 / 10 (page imprimée 804)

[recouvrement] competition network G_S. A smaller average shortest path indicates a higher degree of social interconnectedness and a greater potential for collaboration and knowledge exchange between the scientists working on these seemingly distant themes.

To account for the level of research activity and potential within each theme, we defined an expert density measure ρ_{T_i}:

  ρ_{T_i} = Σ_{v∈T_i} |A_v| · p_v.

where |A_v| is the number of authors of paper v, and p_v is the collective access probability of paper v as calculated in the previous section. A higher expert density signifies a greater concentration of influential researchers actively publishing within the theme, indicating a stronger potential for future advancements.

We identified candidate disruptive theme pairs T_i, T_j based on the following criteria: a large knowledge distance, a small social distance, and high expert density in both themes, defined by thresholds θ_K, θ_S, and θ_ρ, respectively:

  d_K(T_i, T_j) > θ_K (Novelty),
  d_S(T_i, T_j) < θ_S (Collaboration Potential),
  ρ_{T_i} > θ_ρ and ρ_{T_j} > θ_ρ (Knowledge Potential).

The set of candidate disruptive theme pairs 𝒞 was then defined as:

  𝒞 = { (T_i, T_j) | d_K(T_i, T_j) > θ_K, d_S(T_i, T_j) < θ_S, ρ_{T_i} > θ_ρ, ρ_{T_j} > θ_ρ }

To predict the timing of these potential paradigm shifts, we extended our analysis to incorporate the temporal evolution of the scientific landscape. We constructed a series of time-segmented hybrid networks {H_t}_{t=1}^{T}, where each H_t represents the network state at a specific time period t. We then updated the node embeddings dynamically using a time-aware GCNN:

## Capture 15 — empreinte `2709cf8e35fe…` — page 6 / 10 (pied « ASIS&T Annual Meeting 2025 — 804 — Long Papers »)

  h_v^(t,l+1) = σ( W^(l) h_v^(t,l) + Σ_{e∈E_v^(t)} (1/|e|) Σ_{u∈e} B^(l) h_u^(t,l) e^{−λ(t−t_u)} ).

Here, E_v^(t) is the set of hyperedges containing node v at time t, and t_u represents the time of publication or activity associated with node u. The exponential decay factor e^{−λ(t−t_u)} introduces a temporal weighting, giving more influence to recent neighbors in the embedding aggregation process.

We then tracked the temporal evolution of the knowledge distance between candidate theme pairs:

  d_K^(t)(T_i, T_j) = ‖ h̄_{T_i}^(t) − h̄_{T_j}^(t) ‖_2.

A decreasing trend in d_K^(t)(T_i, T_j) over time suggests a growing convergence of the knowledge domains. Simultaneously, we monitored the temporal trends in the collective access probabilities within each theme:

  p_v^(t) = exp(wᵀ h_v^(t)) / Σ_{u∈V_t} exp(wᵀ h_u^(t)),

where V_t is the set of nodes in the hybrid network at time t. An increasing trend in these summed probabilities indicates a rising level of attention and interest in the themes from the scientific community.

## Capture 16 — empreinte `ab9813ecf8d5…` — page 7 / 10 (page imprimée 805 présumée)

To predict the likelihood of a disruptive paradigm shift occurring at a future time point t + Δt, we trained a Long Short-Term Memory (LSTM) [18] model. The input feature vector x^(t) for the LSTM at each time step t consisted of the time-varying knowledge distance, social distance (assumed relatively stable over short timeframes), and expert densities of the candidate theme pair:

  x^(t) = [ d_K^(t)(T_i, T_j), d_S^(t)(T_i, T_j), ρ_{T_i}^(t), ρ_{T_j}^(t) ].

We used historical instances of significant scientific paradigm shifts (e.g., Nobel Prize-winning discoveries that bridged disparate fields) as positive examples to train the LSTM model to predict the probability of a paradigm shift, p_change^(t+Δt):

  h^(t) = LSTM(x^(t), h^(t−1)),
  p_change^(t+Δt) = σ(wᵀ h^(t) + b),

where h^(t) is the hidden state of the LSTM at time t, σ is the sigmoid activation function, wᵀ is a learned weight vector, and b is a bias term.

Finally, we ranked the candidate disruptive theme pairs based on their predicted probability of a paradigm shift and the estimated time of emergence, allowing us to highlight the most promising areas of scientific inquiry poised for transformative breakthroughs and their anticipated timelines. This approach provides a powerful tool for anticipating future scientific revolutions by integrating the dynamic evolution of both knowledge and social networks.

Figure 3 (début du schéma) : titre du cadre « PREDICTING DISRUPTIVE PARADIGM SHIFTS THROUGH DYNAMIC ANALYSIS OF KNOWLEDGE ».

## Capture 17 — empreinte `9ce103d3c882…` — page 7 / 10 : Figure 3 (schéma ; étiquettes)

Titre : « PREDICTING DISRUPTIVE PARADIGM SHIFTS THROUGH DYNAMIC ANALYSIS OF KNOWLEDGE ».
« paper embeddings h_v » → « K-means » → « Topics T_1, T_2, … » ; « Neural network embedding of topic T  h̄_T = (1/|T|) Σ_{v∈T} h_v » ; « d_K(T_1, T_2) = ‖ h̄_{T_1} − h̄_{T_2} ‖_2 » ; « Knowledge Distance d_K(T_i, T_j) > θ_K » ; « Social Distance d_S(T_i, T_j) < θ_S » ; « Expert Density ρ_{T_i} > θ_ρ and ρ_{T_j} > θ_ρ » ; « 𝒞 = {(T_i, T_j) | d_K(T_i, T_j) > θ_K, d_S(T_i, T_j) < θ_S, ρ_{T_i} > θ_ρ, ρ_{T_j} > θ_ρ} ».
« Time » ; « d_K^(t)(T_i, T_j) = ‖ h̄_{T_i}^(t) − h̄_{T_j}^(t) ‖_2 » ; « Hybrid Node High-Order Network with Time Sequence Partitioning {H_t}_{t=1}^{T} » ; « p_v^(t) = exp(wᵀh_v^(t)) / Σ_{u∈V_t} exp(wᵀh_u^(t)) » ; une étiquette en chinois : « 动态更新节点嵌入 » (« mise à jour dynamique des plongements des nœuds ») suivie de « h_v^(t,l+1) = σ( W^(l) h_v^(t,l) + Σ_{e∈E_v^(t)} (1/|e|) Σ_{u∈e} B^(l) h_u^(t,l) e^{−λ(t−t_u)} ) ».
Petit graphique illustratif : courbes d_K^(t)(T_i, T_j) (noire) et p_v^(t) (rouge) décroissantes en fonction du temps, sans axes chiffrés lisibles [valeurs illisibles, figure schématique] ; trois petites séries temporelles sans légende.
« LSTM + Disruptive paradigm change Real historical data » (images de médailles, dont une médaille Nobel) → « Predict the probability of a disruptive paradigm shift occurring at t+Δt ».

## Capture 18 — empreinte `9656cc39cf28…` — fin de la page 7 / 10 (pied « ASIS&T Annual Meeting 2025 — 805 — Long Papers ») puis page 8

Légende : **Figure 3. Predicting Disruptive Paradigm Shifts Through Dynamic Analysis of Knowledge**

CONCLUSION
In this study, we introduce a human-aware AI framework that redefines the prediction of disruptive paradigm shifts by seamlessly integrating knowledge evolution with the social dynamics of scientific communities. Through the construction of a hybrid higher-order network—unifying a domain knowledge graph and a scientist collaboration-competition space—and the application of GCNNs, we quantify collective intelligence as a product of both intellectual content and human agency. Our methodology identifies thematic pairs with significant disruptive potential, characterized by divergent knowledge domains and tightly knit researcher networks, while dynamic embeddings enable temporally precise forecasts of paradigm shifts. Validated against historical milestones in the life sciences, such as Nobel Prize-winning discoveries, this approach demonstrates robust predictive power and generalizability. By offering a scalable and interpretable tool, we not only enhance our understanding of the drivers of scientific revolutions but also provide actionable insights for fostering innovation. This work marks a significant step forward in predictive information science, illuminating the symbiotic relationship between ideas and the communities that shape them, and setting the stage for future explorations across diverse scientific domains.

This study advances the theoretical understanding of scientific progress by bridging two traditionally distinct domains: the evolution of knowledge structures and the social dynamics of scientific communities. By integrating a

## Capture 19 — empreinte `1d643262d795…` — page 8 / 10 (page imprimée 806 présumée)

[recouvrement] domain knowledge graph with a scientist collaboration-competition space through a hybrid higher-order network, we provide a novel lens through which to conceptualize collective intelligence as an emergent property of both intellectual content and human interactions. The use of graph convolutional neural networks (GCNNs) to generate embeddings that encapsulate these dual dimensions challenges the conventional view of scientific discovery as a purely epistemic process, emphasizing instead the critical role of social proximity and competition in driving disruptive innovation. Our findings align with and extend Kuhn's [3] paradigm shift theory by offering a quantifiable framework to identify the preconditions—namely, significant knowledge distances coupled with close social connectivity—that precede revolutionary change. Furthermore, this work enriches the literature on collective intelligence [18, 19] by demonstrating how higher-order network structures can capture the interplay between cognitive diversity and social influence, providing a more holistic model of how scientific breakthroughs emerge. This theoretical synthesis opens new avenues for exploring the mechanisms underlying innovation, particularly at the intersection of disparate knowledge domains, and underscores the necessity of human-aware approaches in predictive science.

The human-aware AI framework presented here offers transformative practical applications for stakeholders across the scientific ecosystem. For research institutions and funding agencies, our model provides a scalable tool to identify emerging interdisciplinary fields with high disruptive potential, enabling strategic allocation of resources to catalyze paradigm-shifting discoveries. By pinpointing thematic pairs characterized by large knowledge distances, close social proximity, and high expert density, policymakers can prioritize investments in collaborative initiatives that bridge silos, fostering environments conducive to innovation. Scientists themselves can leverage this framework to explore untapped connections within and beyond their fields, guiding hypothesis generation and collaboration strategies. The temporal predictions generated by our dynamic analysis further enhance decision-making by offering insights into the likely timing of transformative shifts, allowing for proactive planning in research agendas. In educational contexts, this approach can inform curriculum development by highlighting interdisciplinary areas poised for growth, preparing the next generation of researchers for future challenges. Beyond academia, industries reliant on scientific advancements—such as pharmaceuticals or renewable energy—can use these predictions to anticipate breakthroughs, aligning R&D efforts with emerging trends. Ultimately, this framework empowers a

## Capture 20 — empreinte `6f7a536edece…` — page 8 / 10 (suite)

[recouvrement] proactive rather than reactive approach to scientific progress, amplifying its societal impact.

While our framework represents a significant advancement, several limitations warrant consideration. First, the reliance on publication data from repositories like PubMed and OpenAlex may introduce biases toward well-documented fields, potentially underrepresenting emerging or less formalized areas of inquiry. The focus on co-authorship and inferred competition as proxies for social dynamics overlooks other forms of interaction, such as informal collaborations, mentorships, or conference exchanges, which could further influence innovation. Additionally, the construction of the domain knowledge graph and collaboration-competition space depends on the accuracy of entity recognition and relation extraction, which, despite rigorous preprocessing and ensemble modeling, may still be subject to errors in unstructured text. The generalizability of our findings, while promising, has been primarily validated within the life sciences; its applicability to disciplines with different publication cultures or collaboration norms remains to be fully tested. Finally, the temporal predictions, though aligned with historical breakthroughs, assume a continuity in scientific trends that may be disrupted by exogenous factors—such as technological leaps or global crises—not accounted for in our model. Future iterations could address these constraints by incorporating broader data sources, refining interaction metrics, and extending validation across diverse domains to enhance robustness and scope.

ACKNOWLEDGMENTS
This research was supported by the National Natural Science Foundation of China Young Student (Doctoral) Project (#724B2015) and Jiangsu Province Graduate Research Innovation Project (KYCX25_0133).

GENERATIVE AI USE
We confirm that we did not use generative AI tools/services to author this submission.

AUTHOR ATTRIBUTION
A.J.Y.: conceptualization, methodology, data curation, formal analysis, writing – original draft; S.Y.: data curation, formal analysis, visualization, writing – review and editing; Z.S.X.: project administration, funding acquisition,

## Capture 21 — empreinte `d5d59bf4638d…` — page 9 / 10 (haut de page coupé : la première ligne n'est lisible qu'en partie)

[ligne coupée, en partie lisible] supervision, writing – review and editing; Z.Y.: project administration, funding acquisition, supervision, writing – review and editing; D.S.: project administration, funding acquisition, supervision, writing – review and editing.

REFERENCES
Belikov, A. V., Rzhetsky, A., & Evans, J. (2022). Prediction of robust scientific facts from literature. Nature Machine Intelligence, 4(5), 445-454. https://doi.org/10.1038/s42256-022-00474-8
Duan, Y., Memon, S. A., AlShebli, B., Guan, Q., Holme, P., & Rahwan, T. (2025). Postdoc publications and citations link to academic retention and faculty success. Proceedings of the National Academy of Sciences, 122(4), e2402053122. https://doi.org/10.1073/pnas.2402053122
Evans, J. A., & Foster, J. G. (2011). Metaknowledge. Science, 331(6018), 721-725. https://doi.org/10.1126/science.1201765
Fortunato, S., Bergstrom, C. T., Boerner, K., Evans, J. A., Helbing, D., Milojevic, S., Petersen, A. M., Radicchi, F., Sinatra, R., Uzzi, B., Vespignani, A., Waltman, L., Wang, D., & Barabasi, A.-L. (2018). Science of science. Science, 359(6379), eaao0185. https://doi.org/10.1126/science.aao0185
Franzoni, C., & Stephan, P. (2023). Uncertainty and risk-taking in science: Meaning, measurement and management in peer review of research proposals. Research Policy, 52(3), 104706. https://doi.org/https://doi.org/10.1016/j.respol.2022.104706
Gao, J., & Wang, D. (2024). Quantifying the use and potential benefits of artificial intelligence in scientific research. Nature Human Behaviour. https://doi.org/10.1038/s41562-024-02020-5
Ghosal, T., Tiwary, P., Patton, R., & Stahl, C. (2022). Towards establishing a research lineage via identification of significant citations. Quantitative Science Studies, 2(4), 1511-1528. https://doi.org/10.1162/qss_a_00170
Hill, R., & Stein, C. (2025a). Race to the Bottom: Competition and Quality in Science*. The Quarterly Journal of Economics, qjaf010. https://doi.org/10.1093/qje/qjaf010
Hill, R., & Stein, C. (2025b). Scooped! Estimating Rewards for Priority in Science. Journal of Political Economy, 0(0), 000-000. https://doi.org/10.1086/733398
Hoppe, T. A., Arabi, S., & Hutchins, B. I. (2023). Predicting substantive biomedical citations without full text. Proceedings of the National Academy of Sciences, 120(30), e2213697120. https://doi.org/doi:10.1073/pnas.2213697120
Kang, D., Danziger, R. S., Rehman, J., & Evans, J. A. (2025). Limited diffusion of scientific knowledge forecasts collapse. Nature Human Behaviour, 9(2), 268-276. https://doi.org/10.1038/s41562-024-02041-0

## Capture 22 — empreinte `50eec07a2831…` — page 9 / 10 (suite des références)

Krieger, J. L., Schnitzer, M., & Watzinger, M. (2024). Standing on the shoulders of science. Strategic Management Journal, 45(9), 1670-1695. https://doi.org/10.1002/smj.3598
Kuhn, T. S. (1962). Historical structure of scientific discovery. Science, 136(3518), 760-764.
Kuhn, T. S. (1977). The Essential Tension: Selected Studies in Scientific Tradition and Change. The University of Chicago Press.
Kumari, R., Ashok, N., Ghosal, T., & Ekbal, A. (2022). What the fake? Probing misinformation detection standing on the shoulder of novelty and emotion. Information Processing & Management, 59(1), 102740. https://doi.org/https://doi.org/10.1016/j.ipm.2021.102740
Lin, Y., Frey, C. B., & Wu, L. (2023). Remote collaboration fuses fewer breakthrough ideas. Nature, 623(7989), 987-991. https://doi.org/10.1038/s41586-023-06767-1
Sourati, J., & Evans, J. A. (2023). Accelerating science with human-aware artificial intelligence. Nature Human Behaviour, 7(10), 1682-1696. https://doi.org/10.1038/s41562-023-01648-z
Wang, D., & Barabási, A.-L. (2021). The science of science. Cambridge University Press.
Wang, H., Fu, T., Du, Y., Gao, W., Huang, K., Liu, Z., Chandak, P., Liu, S., Van Katwyk, P., Deac, A., Anandkumar, A., Bergen, K., Gomes, C. P., Ho, S., Kohli, P., Lasenby, J., Leskovec, J., Liu, T.-Y., Manrai, A., Marks, D., Ramsundar, B., Song, L., Sun, J., Tang, J., Veličković, P., Welling, M., Zhang, L., Coley, C. W., Bengio, Y., & Zitnik, M. (2023). Scientific discovery in the age of artificial intelligence. Nature, 620(7972), 47-60. https://doi.org/10.1038/s41586-023-06221-2
Wu, L. F., Wang, D. S., & Evans, J. A. (2019). Large teams develop and small teams disrupt science and technology. Nature, 566(7744), 378-+. https://doi.org/10.1038/s41586-019-0941-9
Xu, F., Wu, L., & Evans, J. (2022). Flat teams drive scientific innovation. Proceedings of the National Academy of Sciences, 119(23), e2200927119. https://doi.org/10.1073/pnas.2200927119
Xu, H., Liu, M., Bu, Y., Sun, S., Zhang, Y., Zhang, C., Acuna, D. E., Gray, S., Meyer, E., & Ding, Y. (2024). The impact of heterogeneous shared leadership in scientific teams. Information Processing & Management, 61(1), 103542. https://doi.org/10.1016/j.ipm.2023.103542
Yang, A. J., Ding, Y., & Liu, M. (2024). Female-led teams produce more innovative ideas yet receive less scientific impact. Quantitative Science Studies, 1-21. https://doi.org/10.1162/qss_a_00335
Yang, A. J., Xu, H., Ding, Y., & Liu, M. (2024). Unveiling the dynamics of team age structure and its impact on scientific innovation. Scientometrics, 129(10), 6127-6148. https://doi.org/10.1007/s11192-024-04987-4

## Capture 23 — empreinte `fa1133c00cc2…` — fin de la page 9 / 10 (pied « ASIS&T Annual Meeting 2025 — 807 — Long Papers ») puis page 10 / 10

Yang, A. J., Yan, X., Hu, H., Hu, H., Kong, J., & Deng, S. (2025). Are disruptive papers more likely to impact technology and society? Journal of the Association for Information Science and Technology, 76(3), 563-579. https://doi.org/10.1002/asi.24947
[page 10] Yang, Y., Tian, T. Y., Woodruff, T. K., Jones, B. F., & Uzzi, B. (2022). Gender-diverse teams produce more novel and higher-impact scientific ideas. Proceedings of the National Academy of Sciences, 119(36), e2200841119. https://doi.org/10.1073/pnas.2200841119
[Fin de la liste visible ; la page 10 ne montre rien d'autre dans la capture.]

## Capture 24 — empreinte `dd40d2329e57…` — page 1 / 10 : doublon de la capture 01 (même texte : ABSTRACT, KEYWORDS, début de l'INTRODUCTION), défilement très légèrement différent. Rien de nouveau.
