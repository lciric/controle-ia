# Antériorité de Co-Scientist (Google DeepMind) pour l'organisme d'idéation — vérification sur pièce, v1

Écrit par un sous-agent (Opus 5.5) pour la session mère, le 9 novembre 2026, de 09:03 à 09:40 UTC environ (`date -u`).
Objet : décision de Lazar R-1990, point (a) (`registres/decisions.md`, l. 1948) : antériorité de Co-Scientist vérifiée sur
pièce, portée aux notes d'antériorité de l'organisme. Aucun fichier existant modifié ; aucune inscription, aucune clé, aucun
appel de modèle payant ; l'organisme public (`/home/user/ideation-organism`) est lu, pas modifié.

**Convention de page.** « Nature p. 4 (490) » : page 4 du PDF de l'article, page 490 de la revue (les pages 11 à 28 du PDF ne
portent pas de numéro de revue). « Suppl. p. 9 » : page 9 du PDF des informations supplémentaires. « v1 p. 16 » : page 16 de
la prépublication arXiv de février 2025 (numéro imprimé égal). Les extractions page par page sont à côté des PDF (§ 1).
Les citations anglaises sont recopiées mot pour mot, sans les numéros d'appel de référence collés au texte (« limitations32 »
devient « limitations »). Un contrôle par programme les a retrouvées dans les extractions, sauf trois, vérifiées à l'œil : un
numéro d'appel collé (Nature p. 13), un saut de page (Nature p. 5-6), le gras du README de l'organisme (l. 130) ; les
citations tirées d'autres notes ou de mémoire sont signalées comme telles.

**Statut des chiffres (R7).** Tout chiffre attribué à Co-Scientist est lu dans un PDF empreinté, à la page citée, dans le texte
ou les légendes ; aucune figure n'a été relue en image. Les chiffres de l'organisme viennent de son README public (commit
`f39a7f4`, 9 novembre 2026, 01:48 UTC) et des registres, non revérifiés sur leurs sorties. Les sources du § 7 ne sont pas
lues, sauf mention : titres et identifiants de mémoire ou relevés dans d'autres notes, non opposables.

---

## 0. Verdict

- **Occupé par Co-Scientist** : plusieurs agents d'un même modèle (Gemini 2.0) génèrent, relisent, classent par un tournoi Elo
  (comparaisons par paires, débats simulés), font évoluer les mieux classées, regroupent les proches et résument ; la nouveauté
  est contrôlée par un relecteur modèle qui cherche dans la littérature ; la validation finale est un essai en laboratoire
  choisi par des experts (Nature p. 11 à 13 ; p. 6 (492)).
- **Non trouvé dans ces pièces** (article, informations supplémentaires, prépublication de 2025) : une règle statistique qui
  décide dans la boucle ; une prédiction scellée avec seuil gelé ; une bibliothèque de lois connues servant de nul ; une mesure
  de la résistance du tournoi à une optimisation contre lui ; un accord mesuré entre le rang au tournoi et l'issue en
  laboratoire. Les revendications centrales de l'organisme (juge statistique hors des agents, nul des lois connues, attaque de
  Goodhart) **ne sont pas occupées par cet article** ; elles ne sont pas vierges pour autant : POPPER et E-valuator d'abord (§ 7).
- **Pour (b) et (c) de R-1990** : l'article publie les consignes exactes du tournoi et un pseudo-code, mais ni le facteur de
  mise à jour Elo ni les plafonds d'idées et de matchs : le bras (b) sera « façon Co-Scientist », pas une copie. Les conditions
  de Google interdisent « adversarial prompting » hors de leurs programmes : l'attaque (b) se fait sur notre réimplémentation,
  jamais sur le produit. Bras (c) : usage manuel, matériau non sensible, citation demandée à la publication (§ 4).

## 1. Pièces obtenues

Dossier neuf `docs/sources/co-scientist-v1/` ; manifeste `MANIFESTE-pieces-co-scientist-v1.txt` (`d1253bcd…`), qui donne
adresses, codes de réponse, heures et la commande d'extraction. Chaque fichier a son compagnon `.sha256` (R6).

| pièce | fichier | pages | empreinte (SHA-256) | texte `-pages.txt` |
|---|---|---|---|---|
| Article de Nature, vol. 655, p. 487-496, 9 juillet 2026 (en ligne le 19 mai), accès libre, licence Creative Commons Attribution 4.0 | `gottweis-2026-nature-655-487-accelerating-scientific-discovery-with-co-scientist.pdf` | 28 | `351f49d89d2f4f4ed84eed4225c09cc95470c41aa3becd0aa3e06b3bd8ba54c3` | `6833d550…` |
| Informations supplémentaires (notes 1 à 12, figures 1 à 9, tableaux 1 à 4) | `gottweis-2026-nature-supplementary-information-MOESM1.pdf` | 120 | `e5595509a10da6e4d24c7df399d0f60e922d628cf1647df3880f8b0ba1c93fbc` | `d3e5b1ee…` |
| Résumé de déclaration de Nature (texte identique aux pages 25 à 28 de l'article) | `gottweis-2026-nature-reporting-summary-MOESM2.pdf` | 4 | `16721f02e153deb6b105e3d6e2126881add79838067a34a72c8f296707f443df` | `19d85e61…` |
| « Towards an AI co-scientist », arXiv 2502.18864 v1, 26 février 2025 | `gottweis-2025-arxiv-2502.18864v1-towards-an-ai-co-scientist.pdf` | 81 | `80730ea110ad450411aa8352a785e996cfcda06afd6e1c60277cb64a65cb676a` | `030fb62d…` |
| arXiv 2502.18864 v2, 29 juin 2026, manuscrit accepté (« Nature revision AAP ») | `gottweis-2026-arxiv-2502.18864v2-revision-nature.pdf` | 157 | `e603a77c9d2bdfb528313e4cf35405b72261e018a70da724fcebca94c96e4716` | `44d16e25…` |

- La v2 d'arXiv est octet pour octet le fichier déjà versé `docs/sources/pdf/bisociation-fertilite-v1/arxiv-2502.18864.pdf`
  (même empreinte, R11).
- Aucune pièce inaccessible. Le code de Co-Scientist n'est pas public (Nature p. 15) ; seuls un pseudo-code (Suppl. p. 56-61)
  et les consignes des agents (Suppl. p. 62-69) le sont.
- Conditions de Google Labs : sous-dossier `conditions-google-labs-lu-2026-11-09/`, manifeste
  `MANIFESTE-lecture-conditions-v1.txt` (`57a1716e…`), neuf pages en texte, pages brutes en archive (`6cad655b…`).

## 2. Ce que fait Co-Scientist

### 2.1 Agents
- Entrée : un objectif en langue naturelle (préférences, contraintes, jusqu'à des centaines d'articles joints), transformé en
  « research plan configuration » (Nature p. 11). Critères par défaut : alignement sur l'objectif, plausibilité, nouveauté,
  testabilité, sûreté (Nature p. 11).
- Un agent superviseur gère une file de tâches asynchrone ; agents de génération, de réflexion (relecture), de classement,
  d'évolution, de proximité et de méta-revue ; mémoire de contexte persistante (Nature p. 11 ; figure 1b, p. 2 (488)). « we
  used Gemini 2.0 models as the base foundational LLM for all agents » (Nature p. 11) ; les ablations de la révision emploient
  aussi Gemini Flash 2.5 (Suppl. p. 8-9).
- Génération : recherche sur la toile, débats simulés « by using self-critique and self-play », hypothèses intermédiaires par
  sauts conditionnels, extension vers les zones non explorées à partir du retour de la méta-revue (Nature p. 12).
- Réflexion : relecture initiale sans outil, relecture complète avec recherche, vérification profonde (décomposition en
  hypothèses élémentaires évaluées une à une), revue d'observations, revue par simulation (« frontier LLMs may have developed an
  internal world model of science »), revue récurrente nourrie du tournoi (Nature p. 12-13).
- Proximité : graphe de similarité pour regrouper, dé-doublonner et apparier les matchs (Nature p. 12-13), « e.g., using text
  embeddings » (Suppl. p. 60).
- Évolution : ancrage bibliographique, cohérence et faisabilité, inspiration, combinaison des meilleures, simplification, idées
  « hors du cadre » ; elle crée de nouvelles hypothèses sans toucher aux anciennes, « as each new hypothesis must also compete in
  the tournament » (Nature p. 13).
- Méta-revue : résume les motifs récurrents des relectures et des débats ; ce retour est « simply appended to their prompts in
  the next iteration » pour tous les agents (Nature p. 12) ; en fin de course, synthèse des mieux classées (Nature p. 14).
- Humain : définit et affine l'objectif, relit, ajoute ses hypothèses au tournoi, choisit à la fin (Nature p. 14) ; « final
  decisions are always made by scientists » (Suppl. p. 55).

### 2.2 Tournoi Elo
- « The Ranking agent orchestrates an Elo-based tournament … This involves pairwise comparisons, facilitated by simulated
  scientific debates » (Nature p. 11). Note initiale 1 200 (Nature p. 13 ; Suppl. p. 59). Les mieux classées s'affrontent en
  débats à plusieurs tours, les autres en comparaisons à un tour ; priorité aux paires proches au graphe et aux hypothèses
  neuves ou bien classées (Nature p. 13).
- Consignes publiées (Suppl. p. 65-67) : le juge reçoit l'objectif, les critères, les deux hypothèses et leurs relectures, doit
  « Disregard these scores » (les notes chiffrées des relectures), débat 3 à 5 tours (10 au plus) et conclut « better idea: <1
  or 2> ».
- Pseudo-code (Suppl. p. 56-61) : boucle « WHILE NumberOfIdeas < MaxIdeas AND NumberOfMatchesPerIdea < MaxMatchesPerIdea » ;
  évolution des cinq premières « IF hypothesis quality has stopped improving » ; synthèse des dix premières ; « CALCULATE new
  Elo ratings … based on the outcome », **sans formule ni facteur de mise à jour** ; MaxIdeas et MaxMatchesPerIdea ne sont
  chiffrés nulle part.
- Les auteurs : « Despite its assumptions and limitations, Elo remains a good proxy for relative ranking » (Nature p. 13) ;
  « although the Elo rating is not the direct optimization target, its progressive increase emerges from the system's
  information feedback loops » (Nature p. 4 (490)) ; mais « The Elo auto-evaluation rating is a key metric that guides the
  self-improvement feedback loops within Co-Scientist » (Suppl. p. 4).

### 2.3 Comment une hypothèse est jugée
Chaîne de filtres : sûreté de l'objectif, puis de l'hypothèse (exclue du tournoi si jugée dangereuse, Suppl. p. 55) ;
relectures, qui « filter inaccurate and, when stipulated, non-novel hypotheses » (Nature p. 12) ; rang au tournoi, jugé par le
même modèle (axes « Elo rating (self-evaluation) » de la figure 2, Nature p. 5 (491)) ; choix humain parmi les mieux classées ;
essai en laboratoire. Repositionnement de médicaments contre la leucémie aiguë myéloïde : 30 hypothèses les mieux classées
montrées à des oncologues, 5 retenues (Nature p. 6 (492)) ; dans le balayage de 34 cancers, seuls les couples à note de
relecture ≥ 4 et score de dépendance DepMap ≥ 0,99 vont aux experts (Suppl. p. 26).

### 2.4 Validations rapportées
- Candidats avec appui préclinique : 3 des 5 essayés inhibent la viabilité (binimetinib, pacritinib, cerivastatin) ; pravastatine
  et diméthylfumarate « little to no effect » (Nature p. 6 (492) ; figure étendue 4, p. 19).
- Candidats « completely novel » : 3 retenus par les experts ; KIRA6 actif ; nanvuranlat et léflunomide « limited effect » sur
  MOLM-13 (Nature p. 6-7 (492-493)).
- Combinaisons : 7 essayées sur deux lignées, surtout synergiques sur MOLM-13, mélangées sur KG-1a (Nature p. 7 (493) ; Suppl.
  p. 32).
- Fibrose du foie : 3 hypothèses retenues par les experts, 2 actives sur organoïdes (Nature p. 9 (495)).
- Îlots chromosomaux inductibles par phage formant une capside (cf-PICI) : l'hypothèse classée première rejoint un résultat non
  publié des chercheurs (Nature p. 9 (495)).
- « the validation of Co-Scientist's hypotheses, while successful, remains preliminary » (Nature p. 9 (495)).

## 3. Réponses aux questions du point 2

### 3.1 Une validation statistique ?
- **Dans la boucle : non trouvée.** La promotion tient aux relectures et au tournoi du modèle (Nature p. 11-13 ; Suppl. p. 59),
  puis au choix des experts (Nature p. 6 (492)) : aucun test, aucune erreur de première espèce contrôlée, aucune règle chiffrée.
- **Pour évaluer le système : descriptive.** Moyennes et intervalles à 95 % des tendances Elo (Nature p. 5 (491)) ; aires sous
  la courbe et intervalles des ablations (Suppl. p. 7-10) ; rho de Spearman 0,745 (p < 0,001) entre deux groupes d'experts sur
  78 propositions (Suppl. p. 11-12) ; test de Wilcoxon « without multiple comparison adjustments » (Suppl. p. 101). « No
  statistical methods were used to predetermine sample sizes » (Nature p. 14-15).
- **Pour les essais : d'usage** — ajustement non linéaire de la concentration qui inhibe 50 % de la viabilité, avec intervalle à
  95 %, trois réplicats biologiques ; indice de combinaison de Chou et Talalay ; modèles « highest single agent » et de Bliss
  (Nature p. 7 (493), p. 15 ; Suppl. p. 30-32).
- Écart entre mot et chiffre : l'évolution est dite « crucial » et « strong quantitative evidence » pour une précision passée de
  70,9 % à 75,4 %, dont l'intervalle donné est [−2 % ; 11 %] (Nature p. 14 ; Suppl. p. 9).

### 3.2 Une prédiction écrite avant l'expérience ?
- **Oui, au sens d'une validation prospective** : les hypothèses de repositionnement précèdent les essais (Nature p. 6 (492)) ;
  la sortie pour KIRA6 propose une plage d'essai « 100 nM to 10 µM » (Suppl. p. 44), la mesure donne 1,75 µM sur MOLM-13
  (Nature p. 7 (493)) ; l'article ne compare nulle part la plage proposée et la mesure.
- **Vérité retenue** : pour les îlots, « Knowing the answer to that question (but without it yet being available in the public
  domain) » (v1 p. 26) ; « a topic their group had independently discovered, but not yet published » (Nature p. 3 (489)). Banc
  de redécouverte : 200 articles de bioRxiv postérieurs à la date de coupure, « we control that the system has no access to the
  answer by filtering search results » (Suppl. p. 7).
- **Non trouvé** : préenregistrement ; empreinte ou horodatage vérifiable ; prédiction chiffrée et signée ; seuil de succès gelé
  avant l'essai. Les essais ne portent que sur des candidats choisis par des experts parmi les mieux classés.

### 3.3 Une bibliothèque de lois connues pour juger la nouveauté ?
- **Non trouvée.** « For novelty, it summarizes known aspects of the hypothesis and then judges their novelty on the basis of
  existing literature » (Nature p. 12), note sur 10. Éprouvée sur 200 idées publiées : 6,14 [5,93 ; 6,34] sans recherche, 2,38
  [2,1 ; 2,67] avec (Suppl. p. 7-8). Le graphe de proximité dé-doublonne (Nature p. 12). Repositionnement : contrainte « not
  previously repurposed for the target indication and without any previous preclinical evidence » ; un seul exemple fonde
  « reasonably well calibrated in its assessment of novelty » (Nature p. 6 (492)).
- Rien qui ressemble à un nul formé des prédicteurs connus, ni à un critère « rien au-delà de l'archive ».

### 3.4 Une mesure de la résistance du tournoi à une optimisation contre lui (Goodhart) ?
- **Non trouvée.** Termes cherchés dans les trois textes : « Goodhart », « reward hack », « gaming », « preregist »,
  « sealed » : aucune occurrence ; « exploit » : seulement au sens de mésusage ou d'exploration ; « over-fitting » : une
  occurrence, citée en (iv) ; « adversar » : la seule épreuve de sûreté, citée en (v).
- Ce qui existe : (i) biais de position sur 2 000 matchs (A contre B puis B contre A), « almost eliminated » par la consigne de
  débat (Suppl. p. 9 ; figure suppl. 5, p. 98) ; (ii) précision d'un match seul selon la consigne, sur 2 000 matchs généraux et
  1 800 entre idées bien classées (Suppl. p. 8) ; (iii) des mises en garde : « the Elo metric is auto-evaluated and not based on
  independent ground truth » (Nature p. 16, figure étendue 1 ; Suppl. p. 94) ; la v1 ajoutait « This auto-evaluation metric may
  favour results with attributes that do not necessarily align with scientists' preferences, quality, or accuracy » (v1 p. 16)
  et demandait des mesures « less intrinsically-favored » (v1 p. 28) ; ces deux phrases ne sont plus dans la version Nature ni
  dans la v2 (recherche de phrases) ; la version Nature garde « developing more objective and automated evaluation metrics that
  move beyond current ranking systems » (Nature p. 9 (495)) ; (iv) un choix de conception sans mesure : « the Generation agent
  uses this feedback selectively to avoid over-fitting to these review critiques » (Nature p. 13) ; (v) 1 200 objectifs adverses
  pour la sûreté (refus des objectifs dangereux, « passed all checks », jeu non publié) (Suppl. p. 6), qui ne touche pas à
  l'optimisation contre le juge.
- Le retour des verdicts aux générateurs est voulu : « Limitations and top win–loss patterns are summarized and provided as
  feedback to other agents » (Nature p. 2 (488), figure 1a) — la configuration où l'organisme a mesuré l'effet du retour (A1,
  bras « avec retour »).
- Les comparaisons avec d'autres modèles et avec les experts se font dans le tournoi de Co-Scientist, jugé par son propre
  modèle (Nature p. 4 (490) ; figure 2b, p. 5 (491)) ; aucune mesure d'une préférence du juge pour les sorties de sa lignée.

### 3.5 Un accord mesuré entre le tournoi et la vérité expérimentale ?
- **Avec la vérité d'un banc, non expérimentale : oui.** Questions à choix multiples GPQA (« diamond ») : précision par tranche
  de 50 points d'Elo, contre une référence de 32 réponses de Gemini 2.0 par question ; « concordance » ; 78,4 % de réponses
  justes pour l'hypothèse la mieux notée de chaque question (Suppl. p. 4 ; figure suppl. 1, p. 94). Rang et Elo contre précision
  (Suppl. p. 8 ; figure suppl. 3, p. 96). Note de relecture contre justesse, avec la méta-revue : aire sous la courbe 0,629 →
  0,634 (1 680 idées) et 0,521 → 0,597 (600 idées du banc de redécouverte) (Suppl. p. 9).
- **Avec des données expérimentales publiques : pour la note de relecture, pas pour le tournoi.** La note de relecture (1 à 5)
  croît avec le score DepMap (criblages publics de dépendance des lignées cancéreuses), sur 40 696 couples médicament-cancer
  (calcul : 202 + 1 576 + 6 473 + 17 404 + 15 041, Suppl. p. 101) ; usage dit « rapid, simplified sanity check », et le même
  score sert de filtre de sélection (Suppl. p. 26).
- **Avec les experts** : « the human expert preferences also appear to be concordant with relative Elo ratings as can be
  inferred from Fig. 2b,c » (Nature p. 5-6 (491-492)), sans statistique, 11 objectifs.
- **Avec l'issue en laboratoire : non mesuré.** Tous les candidats essayés sont bien classés et choisis par des experts ; aucun
  candidat mal classé n'est essayé comme témoin ; aucune analyse du rang contre l'issue (3 sur 5, 1 sur 3, 2 sur 3 ; § 2.4).

## 4. Conditions d'utilisation de Google Labs (lecture de non-juriste)

**Chemin.** Le lien « Terms » de `labs.google/science` mène aux conditions générales de Google (`policies.google.com/terms`,
« Effective July 30, 2026 », version de pays « Unknown Region » servie au conteneur). La liste des services rattache « Science
experiments by Google Labs » à trois textes : ces conditions, la « Generative AI Prohibited Use Policy » (17 décembre 2024) et
l'« Intended Use Policy » (28 avril 2026, sur le centre d'aide « Hypothesis Generation »). La page Labs présente
« Hypothesis Generation » comme « Built with Co-Scientist ». Pages lues le 9 novembre 2026, de 09:06 à 09:14 UTC.

**Usage automatisé.**
- Interdits (conditions générales, « Don't abuse our services ») : « using automated means to access content from any of our
  services in violation of the machine-readable instructions on our web pages (for example, robots.txt files that disallow
  crawling, training, or other activities) » ; « jailbreaking, adversarial prompting, or prompt injection, except as part of our
  safety and bug testing programs » ; « bypassing our systems or protective measures » ; « using AI-generated content from our
  services to develop machine learning models or related AI technology ». Suspension possible, par exemple pour « scraping
  content that doesn't belong to you ».
- `robots.txt` de `labs.google` : tout permis sauf `/404` ; le produit est derrière une connexion Google.
- Aide du produit : accès « currently limited to our interest form », sans garantie ; « You're limited to 3 Standard Runs and 1
  Advanced Run in progress concurrently » ; une course peut prendre « several hours » ; « AI credits » remboursables en cas
  d'échec par l'assistance Google One. Aucune interface de programmation n'est annoncée ; l'article dit seulement « In due
  course, we expect to provide broader access … through Google APIs » (Nature p. 15).

**Confidentialité des données saisies.**
- Licence donnée à Google sur « your content » : mondiale, gratuite, pour « operating and improving the services » (analyse
  automatique comprise) et « developing new technologies and services for Google consistent with these terms » ; elle « doesn't
  affect your privacy rights ». La politique de confidentialité est « not part of these terms » et n'a pas été lue.
- Aide « feedback » : un retour « and associated content may also be reviewed by humans … This content includes your uploads,
  queries, and generated outputs ».
- Export par courriel à `science-datarequests@google.com` (archive sous 20 jours ouvrés) ; suppression d'un rapport possible,
  définitive ; partage public d'un rapport seulement si on l'active (« Enable public sharing »).
- Aucun engagement de confidentialité propre à Labs ou au produit dans les pages lues.

**Publication des résultats.**
- « Some of our services allow you to generate original content. Google won't claim ownership over that content. »
- Interdit : « misleading others into thinking that generative AI content was created by a human » (conditions) ;
  « Misrepresenting the provenance of generated content by claiming it was created solely by a human, in order to deceive »
  (politique sur l'intelligence artificielle générative).
- Usage prévu : sorties « not intended to be used without prior active review, validation, verification, meaningful
  modification, and adaptation by the user » ; « Users must independently verify all claims and data points » ; « not intended
  to automate the entire scientific or research process » ; pas d'usage clinique.
- Aide : « Cite Hypothesis Generation when you publish results » : citation de l'article de Nature et mention recommandée dans
  les méthodes : « AI Tool Usage : Hypothesis Generation system was used during hypothesis and experimental design generation and
  prioritization [date used] ». Aucune autorisation préalable demandée.

**Conséquences pour R-1990.**
- (b) : toute expérience qui vise à tromper le tournoi du produit relève probablement de « adversarial prompting » : l'attaque
  de Goodhart se fait sur notre réimplémentation « façon Co-Scientist » seulement.
- (c) : saisie à la main, aucun script contre le produit, au plus 3 + 1 courses en même temps ; seulement la question non
  sensible de la course 2 (déjà la règle de R-1990), puisque Google peut analyser et faire relire ce qui est saisi ; à la
  publication, citation et mention d'usage.
- Point gris pour Lazar : la clause « develop machine learning models or related AI technology » pourrait viser l'emploi des
  sorties du produit pour régler ou nourrir l'organisme (au-delà d'une simple comparaison) ; lecture juridique à faire.
- La version des conditions applicable à un compte de l'Espace économique européen n'a pas été vue.

## 5. Comparaison avec l'organisme

**État des revendications au 9 novembre** : README public (commit `f39a7f4`) et registres. Le juge statistique est validé sur
mondes plantés et contre des tricheurs scriptés (README l. 96-108, 118) ; les tests de mort et la boucle entre générations sont
« implemented, tested offline, never run for real » (README l. 7, 130) ; le README dit la validation du nul v9 « running »
(l. 129), le registre donne son verdict « puissance perdue », le nul de production restant le v8 (R-1779, `registres/decisions.md`
l. 1737).

Statuts : **occupée** = Co-Scientist la porte déjà ; **voisine** = une pièce proche, d'un autre mécanisme ; **non occupée** = absente
de cet article, ce qui ne veut pas dire vierge (dernière colonne, détails au § 7).

| | revendication de l'organisme (source) | Co-Scientist (page) | statut | autres sources à vérifier |
|---|---|---|---|---|
| O1 | Aucun agent qui produit une idée ne décide de sa survie ; le rôle qui produit ne tient jamais la clé qui évalue (README l. 3, 45) | même modèle pour tous les agents (Nature p. 11) ; le tournoi est son propre juge, « self-evaluation » (Nature p. 5 (491)) ; porte humaine finale (Suppl. p. 55) | non occupée (choix inverse dans la boucle) | The Agentic Scientist (évaluateur scellé), POPPER |
| O2 | Juge statistique figé : règle de e-valeurs écrite dans l'orchestrateur, hors de tout agent (README l. 57, 67) | aucune règle statistique dans la boucle ; relectures, tournoi, experts (Nature p. 6 (492), 11-13 ; Suppl. p. 59) | non occupée | POPPER ; E-valuator (au dépôt) ; test par pari |
| O3 | Prédictions scellées avant que les données existent ; tirages semés par l'empreinte de l'engagement (README l. 57, 68) | hypothèses avant les essais (Nature p. 6 (492)) ; plage d'essai de KIRA6 (Suppl. p. 44) ; vérité retenue non publiée (v1 p. 26 ; Nature p. 3 (489)) ; recherche filtrée (Suppl. p. 7) ; ni empreinte ni seuil gelé | voisine | POPPER ; The Agentic Scientist |
| O4 | Nouveauté statistique : battre un nul des lois connues (nul informé, nul poolé v8, nul v9 par morceaux), « rien au-delà de l'archive » (README l. 96, 129 ; `orchestrator/conception-v7-v1.md` § 2) | nouveauté jugée par un relecteur modèle contre la littérature (Nature p. 12, 14 ; Suppl. p. 7-8) | non occupée | nuls composites par e-valeurs ; comparaison séquentielle de prévisionnistes ; POPPER |
| O5 | Moisson bibliographique (arXiv, OpenAlex), appariements non opposables, un trou apparent est une question (README l. 56) | relecture avec recherche et lecture d'articles (Nature p. 12) ; dépôt privé indexable (Nature p. 14) | occupée dans son principe ; la règle « non opposable, trou = question » ne l'est pas (la relecture de Co-Scientist conclut) | — |
| O6 | Douane de forme et coffre scellé pour les fiches trop concrètes (README l. 52 ; § 7) | revue de sûreté ; hypothèses dangereuses exclues du tournoi et non montrées (Suppl. p. 55) ; 1 200 objectifs adverses (Suppl. p. 6) | voisine (filtre de sûreté) ; tri par la seule forme et non-lecture non occupés | — |
| O7 | Juges croisés de plusieurs fournisseurs, aveugles entre eux ; vérificateur d'une autre famille (README l. 45, 54) | une famille dans la boucle (Nature p. 11) ; hors boucle, quatre juges modèles de deux fournisseurs (Nature p. 6 (492) ; Suppl. p. 5 ; Nature p. 17) | voisine (évaluation seulement) | — |
| O8 | Proposeurs de plusieurs fournisseurs (README l. 51) | une famille ; architecture dite « model agnostic » (Nature p. 9 (495), 12) | non occupée par cet article | systèmes à plusieurs familles de modèles (non cherchés) |
| O9 | La mémoire ne sert ni verdict, ni clé, ni témoin aux agents ; juges aveugles aux notes antérieures (README l. 53, 69) | l'inverse : motifs de victoires et de défaites renvoyés aux agents (Nature p. 2 (488)) ; méta-revue ajoutée aux consignes (Nature p. 12) | non occupée (choix contraire) | — |
| O10 | Témoins plantés vrais et faux, mêlés anonymement à chaque génération (README l. 75, 118) | épreuves hors production contre vérité connue : GPQA (Suppl. p. 4), 200 articles (Suppl. p. 7) | voisine | — |
| O11 | Banc de 27 tricheurs scriptés ; validation décisive préenregistrée du nul v8 (0 sur 1 000 sur chaque ligne fatale) ; banc de mutations (README l. 78-108) | seul le biais de position est mesuré (Suppl. p. 9 ; p. 98) | non occupée | modèles nuls contre bancs à juge modèle ; Jr. AI Scientist ; Luo et al. 2025 |
| O12 | Attaque de Goodhart A1 : proposeur modèle qui lit la description du juge et, dans un bras, ses verdicts, sur des mondes où toute promotion est fausse (README l. 129 ; `resultats/attaque-goodhart-v2/README.md`) | aucune mesure ; mises en garde (Nature p. 16 ; Suppl. p. 94 ; v1 p. 16, 28) ; « avoid over-fitting » sans mesure (Nature p. 13) | non occupée | holdout réutilisable ; « Ladder » ; sur-optimisation des modèles de récompense ; E-valuator |
| O13 | Tests de mort préenregistrés en bac à sable, verdict calculé par l'orchestrateur sur le fichier brut (README l. 58, 67 ; jamais lancés pour de vrai) | pas d'exécution dans la boucle ; revue par simulation et vérification profonde par le modèle (Nature p. 12-13) ; essais humains après sélection (Nature p. 6 (492)) | non occupée (voisine : réfutation par relecture) | POPPER ; AI Scientist v2 et v3 ; Robin ; Kosmos |
| O14 | Sélection entre générations par le verdict des tests de mort ; refus des raffinements cosmétiques (README l. 59) | évolution des mieux classées au tournoi (Nature p. 12-13 ; Suppl. p. 59) ; chaque nouvelle hypothèse concourt | voisine (évolution par tournoi) ; sélection sur issue empirique non occupée | — |
| O15 | Bisociateur à trois bras : loin mais proche, paires jamais liées à la Gu et Krenn, trou structural partagé (README l. 55) | combinaison, inspiration, idées hors du cadre (Nature p. 13) ; extension (Nature p. 12) ; « unexpected connections across disparate disciplines » (Nature p. 9 (495)) | voisine ; les trois bras non occupés | Gu et Krenn 2024 (au dépôt) ; découverte fondée sur la littérature |
| O16 | Pont fiche → loi prédictive sur des issues (README l. 196) | sorties en langue naturelle, propositions, format « Specific Aims » (Suppl. p. 11) | non occupée | POPPER ; HypoGeniC (décrit en Suppl. p. 91) |
| O17 | Scellement par empreinte avant lecture ; aucun repli silencieux ; banc de mutations (README l. 3, 73 ; § 8) | journalisation complète et traces de raisonnement (Suppl. p. 55) ; code non public (Nature p. 15) | non occupée (voisine : journalisation) | — |
| O18 | Discrimination des juges modèles mesurée : au plafond, kappa de Cohen nul (README l. 125) | précision d'un match seul (Suppl. p. 8 ; p. 97) ; biais de position (Suppl. p. 9) ; accord entre groupes d'experts (Suppl. p. 12) | voisine | — |
| O19 | Puissance du juge mesurée ; « rien promu » n'exclut pas un effet de taille donnée (README l. 122, 132) | « No statistical methods were used to predetermine sample sizes » (Nature p. 14-15) | non occupée | — |
| O20 | Juge éprouvé sur vérité plantée : 8 sur 8 vrais promus, 0 sur 8 faux ; témoins sur épisodes réels (README l. 118, 121-123) | accord Elo et réponses justes (Suppl. p. 4, 94) ; note de relecture et DepMap (Suppl. p. 26, 101) | voisine (vérité connue d'une autre nature) | E-valuator |

**Notes existantes, confirmées ou corrigées sur pièce.**
- `synthese-proposeur-enfichable-v1.md` l. 42 : « code fermé » est **confirmé** : « The full source code for the Co-Scientist
  system is not publicly available » (Nature p. 15) ; pseudo-code et consignes publiés (Suppl. p. 56-69). « objectif →
  hypothèses classées par tournoi » : **confirmé** (Nature p. 11-14 ; aide du produit : « ranked by Elo rating »). « coût par
  idée inconnu » : **toujours inconnu** (ni dollars ni jetons dans l'article ; seulement < 1 h et environ 3 h d'expert, Nature
  p. 14, et « 2 days » pour les îlots, Nature p. 9 (495)). « imiter le tournoi = plausibilité linguistique (supposé) » :
  **en partie éprouvé par les auteurs** (accord Elo et réponses justes sur un banc à choix multiples, Suppl. p. 4), **ouvert**
  pour des hypothèses ouvertes, que les auteurs disent jugées « not based on independent ground truth » (Nature p. 16).
- `choix-ia-scientifique-v1.md` l. 48 (« dépôts non cherchés ») : il n'y a pas de dépôt (Nature p. 15) ; Co-Scientist ne peut
  pas servir de système externe exécuté chez nous pour R-776 (c) ; seul le produit de Labs, à la main, reste (R-1990 (c)).
- `reponse-selection-generations-v1-argon-v1.md` l. 151 (« le tri entre générations repose sur des jugements de modèles
  (tournois), non sur des issues expérimentales calculées » ; « validation expérimentale finale par des humains ») et
  `lecture-verifiee-selection-generations-v2.md` l. 49 (« rien pour le juge ») : **confirmés** (Nature p. 6 (492), 12-13 ;
  Suppl. p. 59-60).
- `reponse-selection-generations-v1-kimi-v1.md` l. 279 donnait POPPER sous le titre « POPPER: A Framework for Rigorous
  Hypothesis Validation with LLM Agents », signalé douteux par Kimi lui-même. La bibliographie d'E-valuator (PDF empreinté
  `docs/sources/pdf/2512.03109v2.pdf`, p. 11, réf. 8) donne : Huang, Jin, Li, Li, Candès, Leskovec, « Automated hypothesis
  validation with agentic sequential falsifications », International Conference on Machine Learning 2025, p. 25372-25437.
  L'identifiant arXiv 2502.09858 n'est pas recoupé.

## 6. Réserves

- **Symétrie (R4)** : plusieurs affirmations des auteurs sont trop propres pour être opposables : « All attempts at replication
  in both computational and in vitro were successful », sans compte (Nature p. 15) ; « the system successfully passed all
  checks », jeu non publié (Suppl. p. 6) ; « strong quantitative evidence » pour un intervalle qui contient zéro (Suppl. p. 9) ;
  évaluation clinique par neuf médecins d'un seul centre, après un tri préalable par un clinicien (Suppl. p. 11-12). Rapportées
  comme dites, jamais comme établies.
- **Produit et article** : « Hypothesis Generation » est « Built with Co-Scientist » et classe par Elo, mais ses modèles et ses
  réglages ne sont pas dits (« They leverage the Gemini models », usage prévu) ; ce qu'on observera sur le produit (c) ne vaut
  pas pour le système de l'article, ni l'inverse.
- **Ma lecture** : texte extrait, figures non relues en image ; cases du résumé de déclaration invisibles dans le texte ; v2
  d'arXiv comparée à la version Nature sur des phrases cherchées seulement ; conditions lues sans compte.

## 7. Ce qui reste à vérifier, par ordre

1. **POPPER** (titre et lieu relevés en E-valuator p. 11, réf. 8 ; identifiant 2502.09858 d'après les notes des espèces) :
   e-valeurs séquentielles pour des tests de falsification conçus par agents ; voisin le plus proche de O2, O3, O13, O16.
   Vérifier : séparation auteur et testeur, gel avant tirage, nul informé, témoins, exposition adaptative.
2. **E-valuator** (Sadhuka et al., arXiv 2512.03109 v2, déjà au dépôt et empreinté ; lu page 1 seulement) : convertit le score
   d'un vérificateur boîte noire en règle de décision « with provable control of false alarm rates » par test séquentiel ;
   voisin de O2, O12, O20.
3. **Résistance d'un juge à l'optimisation adaptative** : Dwork et al. 2015 (« reusable holdout », Science 349 ; couple titre et
   identifiant suspect selon `lecture-verifiee-selection-generations-v2.md` l. 53) ; Blum et Hardt 2015 (« Ladder », arXiv
   1502.04585, même note) ; sur-optimisation des modèles de récompense (Gao, Schulman, Hilton 2023, de mémoire) ; modèles nuls qui
   trompent les bancs jugés par modèle (Zheng et al., de mémoire) ; Jr. AI Scientist (arXiv 2511.04583) et Luo, Kasirzadeh, Shah
   2025 (arXiv 2509.08713), d'après `choix-ia-scientifique-v1.md` § 2. Pour O11 et O12.
4. **Nul composite et prédicteurs connus** : inférence universelle (Wasserman, Ramdas, Balakrishnan 2020) ; test sûr (Grünwald,
   de Heide, Koolen) ; comparaison séquentielle de prévisionnistes par e-valeurs (Henzi et Ziegel ; Choe et Ramdas) ; procédure de
   Benjamini et Hochberg pour e-valeurs (Wang et Ramdas 2022, arXiv 2009.02824) ; statistiques par la théorie des jeux (Ramdas,
   Grünwald, Vovk, Shafer 2023) — de mémoire ou relevés dans `lecture-verifiee-selection-generations-v2.md`. Pour O4.
5. **Pièces compagnes de Co-Scientist** (Nature p. 10 (496)) : Penadés et al., Cell 188, 6654-6665 (2025) et He et al., Cell 188,
   6636-6653 (2025), pour la chronologie et la garantie de non-accès dans le cas des îlots ; Guan et al., Adv. Sci. 12, e08751
   (2025), pour les statistiques de la fibrose.
6. **Évaluations indépendantes** de Co-Scientist ou du produit, et travaux de Google après juillet 2026 : non cherchés.
7. **Évaluateur scellé, expériences dans la boucle** : The Agentic Scientist (arXiv 2610.18933, « évaluateur et grille scellés »
   selon `choix-ia-scientifique-v1.md` § 1.1) ; AI Scientist v2 (au dépôt, `docs/sources/pdf/2504.08066v1.pdf`) ; Robin (arXiv
   2505.13400, selon la note d'Argon) ; Kosmos (arXiv 2511.02824). Pour O1, O3, O13.
8. **Bisociation** : Gu et Krenn 2024 (au dépôt), Swanson, Sourati et Evans 2023, suivis par les notes de bisociation. Pour O15.
9. **Pour le bras (b)** : facteur de mise à jour Elo, MaxIdeas, MaxMatchesPerIdea, règle d'appariement exacte : absents de
   l'article ; seule voie, une demande aux auteurs (contact externe : nœud de Lazar).
10. **Conditions** : politique de confidentialité de Google ; version des conditions pour l'Espace économique européen ;
    conditions éventuellement affichées à l'inscription ; lecture juridique de « adversarial prompting » et de « develop machine
    learning models or related AI technology ».
11. **Résumé de déclaration** : cases cochées de la rubrique statistiques, à relire en image si on veut les citer.

## 8. Fichiers créés

- `docs/sources/co-scientist-v1/` : cinq PDF, cinq extractions `-pages.txt`, `MANIFESTE-pieces-co-scientist-v1.txt`, et leurs
  `.sha256`.
- `docs/sources/co-scientist-v1/conditions-google-labs-lu-2026-11-09/` : huit pages en texte, `robots.txt` décompressé, archive
  des pages brutes, `MANIFESTE-lecture-conditions-v1.txt`, et leurs `.sha256`.
- Cette note, `docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-co-scientist-v1.md`, et son
  `.sha256`.

Version 1 ; jamais réécrite (R12).
