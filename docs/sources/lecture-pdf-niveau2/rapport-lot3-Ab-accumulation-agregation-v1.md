# Lecture d'antériorité (R8), niveau 2, lot 3 — groupe Ab « accumulation et agrégation » — rapport v1

## En-tête

- Lecteur : agent neuf, qui n'a rien écrit de ce qu'il vérifie. Rien n'a été modifié sous `/home/user/controle-ia` (ni fichier, ni git).
- Date : 2026-10-06. Début du travail 16:33, rapport achevé à 17:03, temps universel coordonné (UTC).
- Sigles, développés une fois (ils n'apparaissent que là où les papiers les emploient) : aire sous la courbe = aire sous la courbe caractéristique de fonctionnement du récepteur (en anglais « AUROC ») ; « log-aire » = la même aire calculée avec l'axe des faux positifs en échelle logarithmique, entre 0,1 % et 10 % ; FPR = taux de faux positifs ; TPR = taux de vrais positifs ; CUSUM = somme cumulée de Page ; EMA = moyenne mobile exponentielle ; ASR = taux de succès d'attaque ; TV = distance en variation totale ; LoRA = adaptation de rang faible ; CBRN = chimique, biologique, radiologique et nucléaire ; MLP = perceptron multicouche ; LLM = grand modèle de langage ; SWiM = moyenne sur fenêtre glissante (sonde de référence) ; RMAttn = maximum de moyennes glissantes pondérées par attention (sonde de référence) ; SegVar = régularisation de la variance entre segments.

### PDF lus et empreintes

| PDF | pages | empreinte sha256 (identique aux consignes et au fichier compagnon `.sha256`) | lu |
|---|---|---|---|
| `docs/sources/pdf/2604.16824v1.pdf` | 18 | `ad860956062a13a0a236d12b861c83bef08242ff69304efcadc7220f77f4b74d` | en entier |
| `docs/sources/pdf/2607.11751v1.pdf` | 16 | `eef30ef62b965b954d871d873f4d5920ed4482823b84b2204cabe41ac66b97f1` | en entier |
| `docs/sources/pdf/2604.14865v1.pdf` | 36 | `4ff711e178125b20ea8749d052d7598b7a4644ae6a7fd04f79979afb7680f5f9` | en entier (36 pages, au-delà du minimum demandé) |

### Méthode

- Extraction par `pdftotext -layout`, page par page : les pages citées sont le rang dans le fichier. Pour les pages à deux colonnes (2607.11751), seconde extraction de la même page en ordre de lecture (`pdftotext` sans `-layout`). Aucun autre outil sur les PDF.
- Scripts dans `scripts/`, hors du dossier des textes extraits, lancés par `python3 -I`.
- Numérotation de la recherche affirmative : « 3 » = lemme L, « 4 » = théorème T, « 5 » = transposition Tr. Source : la synthèse de son rapport (`docs/sources/recherche-affirmative-20261006/rapport-papier-A-v1.md`, lignes 137 à 139). Je n'ai pas lu ce rapport en entier : une recherche ciblée en a affiché les titres de section, ses avertissements de méthode (lignes 7 à 14), ses lignes 74 (2607.11751, identique à mes consignes) et 124 (2606.10456, déjà au dossier) et sa synthèse (lignes 133 à 142).
- Note d'indépendance : quatre auteurs de 2604.14865 sont chez Anthropic, éditeur du modèle qui fait cette lecture. Ce papier n'a reçu aucun traitement particulier.

### Contrôle des citations (R5 puis contrôle)

- Règle : la citation, blancs supprimés, doit se retrouver dans le texte extrait de la page indiquée. Seules tolérances : les blancs et les césures de fin de ligne. Une page absente ou vide est une erreur, jamais un succès.
- Essai préalable (R5), 12 cas : 5 cas justes (dont blancs ajoutés, césure « de-/tection », chiffre exact, texte sur deux colonnes) acceptés ; 5 cas altérés (mot changé, chiffre changé 0.908 → 0.918, mauvaise page, tiret ajouté hors césure, mot supprimé) refusés ; 2 artefacts (page absente, page vide) en erreur. 12 sur 12 conformes.
- Premier passage : 131 citations, 1 échec (OB12 : phrase coupée par le tableau 2 entre les deux colonnes de la page 4, contiguë dans aucune extraction). Je l'ai remplacée par la légende du tableau 2, qui porte le même chiffre, et par une citation partielle. La tolérance n'a pas été élargie.
- Passage final : **155 citations contrôlées, 155 conformes, 0 échec** (113 sur l'extraction « -layout », 42 sur l'extraction en ordre de lecture).
- Fichiers, avec leur empreinte sha256 :
  - `citations.json` : `1aede9eb5ea96d15e0c6e11fd21a59882f1849e0e9d15f7dff85530095118abb` ;
  - `controle-citations-passage2.tsv` : `dbd8864137284087b42886b32a9786093970b71072c6a70dd273e7f7ee624130` ;
  - `scripts/controle_citations.py` : `2c89a6464e0d43b2fcbe7fbeed5044197553895f4ce4bc2bdb4f787d4b7e85e5` ;
  - `scripts/coherence_rapport.py` : `84fb7d05f70efb9eb29af977f57daf72cf7d49af7b0f712dfcb45bafc36c66bc`.
- Un identifiant entre crochets, par exemple [SD03], renvoie à une ligne de `citations.json`. Ce fichier donne pour chacune le PDF, la page et le texte anglais exact.
- Cohérence du rapport avec ce fichier, par script (`scripts/coherence_rapport.py`), testé d'abord sur un cas juste, une citation altérée (« ≥ » changé en « > ») et un identifiant inconnu, tous deux détectés. Résultat sur le rapport : 148 identifiants cités, aucun inconnu ; 104 citations reproduites, toutes identiques mot pour mot à la citation contrôlée.

### Incident

Le disque racine a été plein pendant une partie du travail (entre 0 et 4 Mo libres). Environ 20 Go étaient occupés par d'autres dossiers de travail de la session (`essai-t05`, `contre-lecture-t04-5`, `essais-v2`, `essais-v3c`…), auxquels je n'ai pas touché. J'ai supprimé seulement des fichiers à moi et régénérables :

- les textes complets, qui doublaient les pages ;
- le dossier de l'essai R5 ;
- la sortie détaillée du premier passage, dont le résultat est consigné ci-dessus.

---

## 1. 2604.16824v1 — SafeDream

### Identité

- Titre : « SafeDream: Safety World Model for Proactive Early Jailbreak Detection » [SD37], p. 1.
- Auteurs : Bo Yan (University of Central Florida), Weikai Lin (University of Rochester), Yada Zhu (IBM Research), Song Wang (University of Central Florida, auteur correspondant) [SD38, SD39], p. 1.
- Version : v1, 18 avril 2026, catégorie arXiv cs.CR [SD01].
- Venue : aucune. Mention « Preprint. Under review. » [SD02].

### Ce que fait le papier : réponses aux questions des consignes

- **Objet.** Le papier détecte, le plus tôt possible, les contournements multi-tours d'un modèle (« jailbreaks »), avant le tour où le modèle se conforme. C'est un module externe : les poids du modèle ne sont pas modifiés.
- **Signal.** Le papier lit l'état caché d'une couche du modèle cible gelé, Qwen2.5-7B [SD09]. Cet état est projeté sur des directions liées au refus, puis enrichi par une attention croisée apprise. Un modèle de transition prédit l'état suivant, et un discriminateur donne un risque par tour (p. 4).
- **Quelle accumulation.** Une somme cumulée de Page sur les log-cotes du risque : G_t = max(0, G_{t−1} + Λ_t − κ). L'alarme sonne quand G_t ≥ A [SD11, SD12, SD13]. Dans une zone grise sous A, une « imagination contrastive » compare des futurs d'attaque et des futurs bénins imaginés, et peut déclencher une alarme anticipée (p. 5).
- **Quel calibrage.**
  - La ligne de base κ est la log-cote moyenne des conversations bénignes [SD12].
  - Tout le reste est supervisé avec des attaques. Le discriminateur apprend sur des étiquettes graduées, données par trois classifieurs, sur des conversations d'attaque et des conversations bénignes [SD14]. La réserve d'actions d'attaque de l'imagination est tirée des conversations d'attaque [SD15].
  - Les valeurs de A, τ et A_imag, et la façon de les choisir, sont **introuvables**. Le renvoi « Hyperparameter selection and training details are in Appendix A.5. » [SD24] mène à une annexe A.5 (p. 13) qui ne les donne pas.
- **Quelle garantie de faux positifs.** Aucune.
  - Le taux de faux positifs est mesuré après coup : 7,9 % sur XGuard-Train [SD18], en moyenne sur 5 plis de validation croisée [SD16]. Le papier n'invoque que l'optimalité classique de la somme cumulée [SD11].
  - Recherche dans le texte de « anytime », « e-value », « e-process », « martingale », « Ville », « guarantee » : aucune occurrence.
  - L'unité du taux de faux positifs (par conversation ?) n'est pas définie. L'annexe B.3 annoncée [SD35] ne définit que l'avance (« Lead ») et le taux d'alerte plus précoce (p. 15).
- **Quel adversaire.**
  - Un utilisateur qui conduit un contournement multi-tours [SD08], tiré de jeux d'attaques fixes. Les attaques de XGuard-Train ont été générées de façon adaptative [SD36], mais pas contre ce détecteur.
  - Les auteurs ne garantissent pas le transfert à des familles d'attaques non vues [SD22].
  - Un seul modèle cible est testé [SD25].
  - Le modèle lu est la victime, pas l'agent qui sabote.

### Affirmations de la recherche affirmative

| # | affirmation de la recherche affirmative | verdict | page | citation exacte |
|---|---|---|---|---|
| A1 | « 2604.16824 (v1 vue) ; SafeDream… ; auteurs non vus ; avril 2026 (d'après l'identifiant) » | **corrigé** : « 2604.16824v1 ; Bo Yan, Weikai Lin, Yada Zhu, Song Wang ; 18 avril 2026 ; cs.CR ; prépublication en cours d'examen, sans venue » | 1 | [SD01] "arXiv:2604.16824v1 [cs.CR] 18 Apr 2026" ; [SD02] "Preprint. Under review." ; [SD38] "Bo Yan Weikai Lin Yada Zhu University of Central Florida University of Rochester IBM Research" ; [SD39] "Song Wang" |
| A2 | « Encode les états cachés du modèle en une représentation de sûreté et prédit son évolution de tour en tour. » | **confirmé** (il s'agit des états cachés du modèle cible gelé) | 1 ; 4 | [SD03] "a safety state world model that encodes LLM hidden states into a compact safety representation and predicts how it evolves across turns" ; [SD09] "through the frozen Qwen2.5-7B (Yang et al., 2024) and extract the hidden state" |
| A3 | « Accumule les signaux de risque faibles de chaque tour par une somme cumulée, pour alarmer avant que le contournement aboutisse. » | **corrigé** : « Accumule par une somme cumulée de Page les signaux de risque faibles de chaque tour. L'alarme précoce vient surtout de l'imagination contrastive en zone grise. La somme cumulée sert surtout à supprimer les fausses alarmes : sans elle, l'avance passe de 1,11 à 1,49 tour, mais les faux positifs de 7,9 % à 13,8 %. » | 1 ; 3 ; 8 | [SD04] "CUSUM detection that accumulates weak per-turn risk signals into reliable evidence" ; [SD05] "contrastive imagination that simultaneously rolls out attack and benign futures in latent space to issue early alarms before jailbreaks occur" ; [SD07] "contrastive imagination is the primary driver of early detection and CUSUM is the key for false alarm suppression" ; [SD19] "Removing CUSUM (Section 3.2) increases Lead to 1.49, however, FPR surges to 13.8%" |
| A4 | « Selon le résumé : aire sous la courbe 0,908 et 7,9 % de faux positifs sur XGuard-Train. » | **corrigé** : « Le résumé ne donne pas ces chiffres. Ils sont en section 4.2 et au tableau 1 (p. 7). Ce sont des moyennes sur 5 plis de validation croisée. 7,9 % est un taux mesuré au seuil choisi, pas un niveau garanti. » | 1 ; 7 | [SD06] "maintaining competitive false positive rates and outperforming baselines in detection quality" ; [SD17] "achieves the highest AUROC (0.908) on XGuard-Train" ; [SD18] "maintains an FPR of 7.9%" ; [SD16] "All results are mean over 5-fold cross-validation." |
| A5 | « l'adversaire est l'utilisateur, pas l'agent qui sabote » | **confirmé** | 3 | [SD08] "an adversarial user progressively guides the LLM toward harmful content through seemingly innocuous messages" |
| A6 | « Somme cumulée classique, pas processus e toujours valide » | **confirmé** (aucune garantie toujours valide ; seuils non publiés) | 5 | [SD11] "We adopt CUSUM (Page, 1954), a sequential change-point detection method that is provably optimal for minimizing detection delay at a given false alarm rate (Moustakides, 1986)." ; [SD13] "An alarm is raised when Gt ≥ A." |
| A7 | « L'"imagination contrastive" déroule des futurs d'attaque, donc pas de calibration sur épisodes honnêtes seuls » | **confirmé, et plus fort** : le discriminateur lui-même apprend sur des conversations d'attaque étiquetées ; seule la ligne de base κ est purement bénigne | 13 ; 15 ; 5 | [SD15] "The attack pool Aatk and benign pool Aben are constructed from the training fold of each cross-validation split." ; [SD14] "The graduated label averages their outputs and serves both as the training signal for the safety discriminator and as the basis for the compliance point definition" ; [SD12] "The CUSUM statistic accumulates evidence by subtracting a baseline κ (the average log-odds under benign conversations)" |
| A8 | « L'idée "états cachés et accumulation des signaux faibles" est cependant prise pour les conversations. » | **confirmé** | 1 ; 4 | [SD03] (ci-dessus) ; [SD10] "In a multi-turn attack, the risk score from any single turn is weak and noisy." |
| A9 | verdict « voisin fort » pour H2 (mécanisme) et pour « 3 » (L) | **corrigé** : pour H2, « occupe en partie » en lecture dure ; pour L, « voisin faible » (voir la table suivante) | — | — |

### Antériorité

| énoncé | verdict d'antériorité | composantes faites / non faites | pages et citations |
|---|---|---|---|
| **H2** | **occupe en partie** (lecture dure, que je retiens). Lecture possible : « voisin fort » | **Faites** : des scores tirés des états internes d'un modèle, accumulés de façon additive au fil des pas par une somme cumulée de Page, avec une ligne de base estimée sur le bénin. Le papier constate aussi que le signal d'un tour isolé est faible et qu'un classifieur tour par tour est proche du hasard. **Non faites** : la garantie toujours valide ; le calibrage sans aucun exemple d'attaque ; des sondes de l'agent qui agit (ici, le modèle lu est la victime d'un utilisateur adverse) ; des actions maintenues sous un seuil par action calibré à 1 % ; le rappel en fonction de l'horizon (non mesuré, dialogues d'environ 5 tours) ; le sabotage et les trajectoires d'agents. **Ce qui tranche** : le périmètre de la revendication d'H2. La consigne (décision N-007) tient le squelette séquentiel en boîte noire pour acquis ; si la « boîte blanche séquentielle » est une pièce propre de la revendication, elle est prise pour les conversations, d'où « occupe en partie ». Si seule compte la conjonction complète (toujours valide, bénin seul, agent qui agit, sous le seuil, horizon), « voisin fort ». | p. 4, 5, 14, 17 : [SD10] ; [SD11] ; [SD12] ; [SD13] ; [SD21] "The MLP, which processes each turn independently, performs near chance (0.517)" ; [SD33] "The average dialogue length is around 5 turns." |
| L (« 3 ») | voisin (faible) | **Seul point touché** : la détection « avant le dommage » par un détecteur de rupture de Page, avec une avance mesurée en tours, et l'arbitrage entre délai et fausses alarmes (sans somme cumulée : plus tôt, mais 1,75 fois plus de faux positifs). Ce n'est pas un contre-indice : les deux points de fonctionnement ne sont pas à taux de faux positifs égal. **Non faits** : budget de l'attaquant ; puissance en fonction de (B, n₀, loi honnête, α) ; fragmentation ; calendrier ; garantie toujours valide. | p. 5, 8 : [SD11] ; [SD19] |
| T (« 4 ») | voisin (faible) | **Fait** : mélanger l'ordre des tours fait tomber l'aire sous la courbe de 0,908 à 0,633. Une part du signal est donc dans l'ordre temporel, que ne voit pas une statistique invariante par permutation du temps (le cas couvert par T1). **Non fait** : c'est une permutation des entrées, pas des scores ; ni groupe, ni agents, ni énoncé. | p. 17 : [SD20] "shuffling the turn order causes a 27.5% drop, confirming that the model relies on temporal structure rather than bag-of-turns features" ; [SD29] "Transformer 0.908 0.633 0.275" |
| Tr (« 5 ») | ne touche pas | **Seule agrégation par maximum du papier** : celle des garde-fous de référence, dont le score de conversation est le maximum sur les tours, pour calculer l'aire sous la courbe. L'ablation « sans somme cumulée » ne dit pas quelle règle la remplace. **Non fait** : ni passage du jeton à l'action, ni adversaire adaptatif. | p. 14 : [SD23] "as the per-conversation risk score, taking the maximum across all turns." |
| H1 (pour mémoire) | voisin (faible) | **Fait** : le détecteur sur activations bat des garde-fous textuels (aire 0,908 contre 0,650 à 0,818 sur XGuard-Train). **Mais** la comparaison n'est pas appariée : les garde-fous ne sont pas entraînés sur ces données, la comparaison n'est pas à taux de faux positifs égal, et il s'agit de contournement, pas de sabotage. | p. 7 : [SD26] ; [SD40] "SelfDefend 0.818 0.616 0.220" ; [SD41] "WildGuard 0.650 0.713 0.224" |
| HC1 à HC6, H3, H4′, H5, H6, H7, H8, statistique de population (papier B) | ne touche pas | — | — |

### Chiffres utilisables

| chiffre | nature | page et citation |
|---|---|---|
| Sur XGuard-Train / SafeDialBench / SafeMTData : aire sous la courbe 0,908 / 0,912 / 0,915 ; F1 0,891 / 0,901 / 0,904 ; faux positifs 0,079 / 0,066 / 0,080 ; avance 1,11 / 1,20 / 1,06 tour | auteurs | p. 7, tableau 1 [SD26] |
| Écarts-types sur 5 plis (XGuard-Train) : aire ±0,006 ; F1 ±0,009 ; faux positifs ±0,008 ; avance ±0,07 | auteurs | p. 16, tableau 4 [SD31] |
| Rappel 0,887 ; aire sous la courbe précision-rappel 0,946 (XGuard-Train) | auteurs | p. 16, tableau 6 [SD30] |
| Ablations (XGuard-Train) : sans somme cumulée, rappel 93,8 %, avance 1,49, faux positifs 13,8 % ; sans imagination, 75,4 %, 0,53 et 10,2 % ; imagination d'attaque seule, faux positifs 25,6 % | auteurs | p. 8, tableau 2 [SD27, SD28, SD34] |
| La somme cumulée divise les faux positifs par 1,75 (13,8 / 7,9), pour 5,1 points de rappel perdus | calcul | à partir de [SD27] et du tableau 2 |
| Ordre des tours mélangé : 0,908 → 0,633 ; classifieur tour par tour : 0,517 | auteurs | p. 17, tableau 9 [SD29, SD21] |
| La « baisse de 27.5% » du texte est un écart absolu (0,275 d'aire). En relatif, la baisse est de 30 % | calcul | p. 17 [SD20] |
| Coût : moins de 5 ms par tour, moins de 100 ms pour l'imagination | auteurs | p. 18 [SD32] |
| Environ 30 000 conversations (XGuard-Train), d'environ 5 tours | auteurs | p. 6 et 14 [SD36, SD33] |

### Ce qui n'a pas été lu

- Rien : les 18 pages ont été lues.
- Non exploitables par extraction de texte : les valeurs des figures 1, 3 et 4 (radars, dynamique de la somme cumulée, sensibilité aux hyperparamètres).
- Absents du PDF : les seuils A, τ et A_imag et leur méthode de choix ; la définition de l'unité du taux de faux positifs.

---

## 2. 2607.11751v1 — frontière d'observabilité entre agents

### Identité

- Titre : « When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems » [OB49], p. 1.
- Auteurs : Yibo Hu, Ren Wang, Illinois Institute of Technology [OB49], p. 1.
- Version : v1, 13 juillet 2026, catégorie arXiv cs.CR [OB01].
- Venue : aucune indiquée. Recherche, hors bibliographie, de « AAAI », « under review », « proceedings of the », « accepted », « copyright » : aucune occurrence.
- Dépôt de code annoncé (`github.com/yibo-hu-lab/observability-boundary`) : non consulté.

### Ce que fait le papier : réponses aux questions des consignes

- **Cadre.**
  - Systèmes multi-agents qui utilisent des outils. K fragments, un par pas, chaque pas étant un agent [OB07, OB46]. L'attaquant contrôle le contenu des fragments, pas le moniteur.
  - L'objet assemblé est un code d'exfiltration. Les expériences principales sont à K = 3 [OB45].
  - Taux de succès d'attaque mesurés sur 50 trajectoires par case. Seuils à 5 % de faux positifs bénins [OB11].
- **Énoncé exact de la frontière.** « We formalize this as an observability boundary: a monitor catches only what its view can tell apart from benign traffic. » [OB02].
  - Définition 1, bénignité locale [OB53] : chaque fragment est bénin dans la vue locale, l'objet assemblé est malveillant.
  - Définition 2, indiscernabilité locale à ε près [OB50] : la distance en variation totale entre les lois locales bénigne et d'attaque est au plus ε à chaque position.
  - Proposition 1 [OB51] : toute règle, même aléatoire, qui ne voit qu'une observation locale [OB09] a un avantage par fragment (vrais positifs moins faux positifs) d'au plus ε [OB52].
- **Est-ce un théorème ?** Non : deux propositions.
  - La Proposition 1 est l'inégalité classique de variation totale, prouvée en quelques lignes (annexe A.1, p. 10).
  - La Proposition 2, sur l'agrégation « alarme si l'une », est une borne de l'union que les auteurs disent eux-mêmes modeste [OB15].
  - Que la frontière tienne sur deux codages est un constat empirique, pas une conséquence de la Proposition 1 [OB14].
- **Quelles statistiques** (p. 3, 12 et 13) :
  - moniteur statistique par pas (entropie, longueur, indices lexicaux) ;
  - suivi de provenance et de flux de données (« taint ») ;
  - assemblage avec marqueur (recherche d'une chaîne plantée) ;
  - assemblage sans marqueur : sept traits du texte assemblé, avec une forêt d'isolement à une classe ou un classifieur supervisé ;
  - moniteur aveugle au codage (densité de structure de code de la concaténation) ;
  - vue décodée, qui reçoit la famille d'encodage ;
  - ensemble de décodeurs usuels ;
  - recherche de reconstruction par un modèle de langage ;
  - détecteur neuronal livré avec AgentDojo ;
  - vue de coordination entre fragments.

  Mesures : aire sous la courbe, taux de succès d'attaque, vrais positifs à 1 %, 5 % et 10 % de faux positifs.
- **Calibrage sur trafic bénin seul.**
  - Oui pour tous les seuils (5 % de faux positifs bénins, sur des trajectoires bénignes tenues à part) [OB22].
  - Oui pour le moniteur à une classe, qui ne voit jamais d'attaque [OB23, OB13].
  - Non pour le blocage : le moniteur supervisé exige des exemples d'attaque, et la vue décodée suppose la famille d'encodage connue [OB48].

### Affirmations de la recherche affirmative

| # | affirmation de la recherche affirmative | verdict | page | citation exacte |
|---|---|---|---|---|
| B1 | « 2607.11751 (version non vue) ; When Local Monitors… ; Yibo Hu, Ren Wang (Illinois Institute of Technology) ; juillet 2026 » | **confirmé** (complété : v1 du 13 juillet 2026, cs.CR, sans venue indiquée) | 1 | [OB49] "When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems Yibo Hu, Ren Wang Illinois Institute of Technology" ; [OB01] "arXiv:2607.11751v1 [cs.CR] 13 Jul 2026" |
| B2 | « Formalise une "frontière d'observabilité" : un moniteur ne détecte que ce que sa vue distingue du trafic bénin. » | **confirmé**, sous forme de proposition : c'est une borne classique en variation totale | 1 ; 3 | [OB02] "We formalize this as an observability boundary: a monitor catches only what its view can tell apart from benign traffic." ; [OB51] "Proposition 1 (Local detection is bounded by local indistinguishability)." ; [OB52] "has per-fragment detection advantage (true positive rate minus false positive rate) at most ε" |
| B3 | « Une porte dérobée répartie entre agents passe tous les contrôles locaux. » | **corrigé** : « Une porte dérobée répartie entre agents ne passe tous les contrôles locaux que si chaque fragment est localement bénin et localement indiscernable du trafic bénin dans la vue du moniteur. Le découpage seul ne suffit pas : le détecteur livré avec AgentDojo attrape le découpage naïf (aire 0,82 à 0,84). » | 1 ; 3 ; 4 | [OB47] "A distributed backdoor splits a harmful payload across agents, so every local check passes while the assembled object is the attack." ; [OB04] "The problem is not splitting itself: split fragments can still leak suspicious tokens or provenance edges. The hard case is local benignness." ; [OB08] "A local monitor fails only when both conditions hold: the fragments are locally benign, and they are also locally indistinguishable from benign traffic in the monitor’s view." ; [OB12] "The shipped detector catches naive splitting (AUROC 0.82–0.84), but here its per-step and naive-concatenation views fall to chance" |
| B4 | « Même les moniteurs de trace complète échouent s'ils n'atteignent pas la représentation où la charge est exposée. » | **confirmé**. Précision : c'est un constat empirique (moniteur de trace complète aveugle au codage : 0 attaque bloquée sur 50 ; détecteur livré, en trace complète : 10 sur 50) | 1 ; 6 ; 7 | [OB06] "But seeing more is not enough: full-trace monitors and decoders still fail unless they reach the representation where the payload is exposed." ; [OB14] "That the same boundary appears across two codecs is an empirical finding, not a consequence of Proposition 1." ; [OB42] "Codec-blind full-trace monitor ✓ × 0/50" ; [OB41] "Shipped neural detector (full trace) ✓ × 10/50" |
| B5 | « Un moniteur entraîné sur du trafic bénin seul retrouve la structure de l'attaque (aire sous la courbe moyenne 0,874). » | **corrigé** (complément indispensable) : « Un moniteur à une classe (forêt d'isolement sur sept traits du texte assemblé), entraîné sur du trafic bénin seul, classe l'attaque assemblée avec une aire sous la courbe moyenne de 0,874 (0,858 à 0,879) sur des familles d'encodage tenues à part. À seuil calibré, il ne détecte que 6 %, 25 % et 36 % des attaques, à 1 %, 5 % et 10 % de faux positifs bénins. Sa version stricte tombe à 0,406 sur une charge en langue naturelle. Dans le même cadre, un moniteur sans marqueur et aveugle au codage s'inverse sur du trafic bénin contenant du code (0,090). » | 1 ; 11 ; 13 ; 6 | [OB05] "A monitor trained only on benign traffic recovers the attack’s code structure across held-out encodings (0.874 mean AUROC)." ; [OB35] "AUROC ranges within 0.858 to 0.879 across the four held-out families (mean 0.874)" ; [OB21] "its TPR rises with the budget (0.06 → 0.25 → 0.36), because its strength is ranking (AUROC 0.874) rather than a tight operating point" ; [OB31] "the strict one-class monitor falls below chance (AUROC 0.406, versus 0.956 on code)." ; [OB32] "monitor inverts: it ranks realistic benign snippets that use the payload’s libraries above the attack (AUROC 0.090)" |
| B6 | verdict « occupe en partie (énoncé 4, sous la forme "vue et représentation") » : « la moitié négative du théorème […] y est énoncée pour des systèmes multi-agents, en boîte noire et sur du texte, sans sondes » | **confirmé sur les faits** ; verdict précisé dans la table d'antériorité : la moitié négative n'est pas parmi les pièces revendiquées de T, et le papier contient un germe du côté K | 3 ; 10 | [OB08] (ci-dessus) ; [OB20] "its benign vs. attack TV can be large even when every local marginal TVi is small." |
| B7 | « La moitié positive (agrégateur d'autocorrélation ou de co-élévation) n'apparaît pas dans le résumé. » | **confirmé sur le PDF entier** : ni autocorrélation, ni co-élévation, ni copule, ni permutation au sens d'un groupe (recherche faite). La « moitié positive » du papier est l'observation de l'objet assemblé | 4 ; 5 | [OB33] "only a cross-fragment coordination view recovers the signal (AUROC 1.000)" ; [OB48] "none is at once oracle-free, attack-training-free, and blocking: marker-free recovery needs no oracle but does not block, supervised blocking needs attack examples, and decoded-view blocking assumes the encoding family." |
| B8 | passage non attribué : « si chaque pas a un taux de faux positifs α, celui de la trajectoire vaut 1−(1−α)^K ; auditer plus de pas ne suffit pas, la puissance vient de la dépense du budget de faux positifs » | **confirmé et attribué** : 2607.11751, annexe A.2, Proposition 2, p. 10. La formule exacte suppose des alarmes bénignes indépendantes et un calibrage uniforme ; en général, c'est une borne de l'union. Elle ne vaut que pour l'agrégation « alarme si l'une ». Je ne peux pas exclure que le passage figure aussi dans 2606.05647 ou 2606.10456, que je n'ai pas lus | 10 | [OB16] "If every step has false-positive rate α, then the trajectory-level false-positive rate is" ; [OB18] "If the benign flag events are additionally independent and uniformly calibrated, then" ; [OB17] "Thus, auditing more steps does not by itself solve the problem: without additional local evidence, power comes from spending more false-positive budget." ; [OB19] "It does not rule out monitors that score the fragments jointly." |
| B9 | 2607.24893, « Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study » : « voisin, à vérifier ; lien avec 2607.11751 non établi ; contenu non vu » | **introuvable**. 2607.11751 ne le cite pas (recherche de « 24893 », « characteriz », « early detection » : aucune occurrence). Aucun fichier dont le nom contient « 24893 » dans le dépôt (vérifié sur disque, R11). Contenu et lien non vérifiables ici | — | — |

### Antériorité

| énoncé | verdict d'antériorité | composantes faites / non faites | pages et citations |
|---|---|---|---|
| **T** (« 4 ») | **occupe en partie**, mais seulement la moitié négative, qui n'est pas parmi les pièces revendiquées. Pour les pièces revendiquées : « voisin », avec un germe du côté K | **Faites** : (a) l'impossibilité pour toute règle qui ne voit qu'un fragment, sous indiscernabilité locale (Proposition 1) ; (b) une borne pour l'agrégation « alarme si l'une » des règles locales (Proposition 2) ; (c) la remarque qu'un moniteur qui score les fragments conjointement échappe à la borne, car la variation totale conjointe peut être grande quand toutes les marges locales sont petites. C'est un germe informel du côté K (marges préservées, dépendance révélatrice) ; (d) une attaque répartie entre agents, un fragment par pas. **Non faites** : les sous-groupes de permutations et l'unification temps × agents ; la classe C ; la distinction C / K et ses signes ; les garanties locales (balayage, somme cumulée, co-élévation) face à un attaquant adaptatif, que le papier exclut de sa revendication ; les activations réelles (le papier travaille sur du texte, en boîte noire). **Ce qui tranche** : le périmètre de la revendication. Si la liste « revendiqué » de la consigne est exhaustive, le verdict est « voisin » ; si l'on juge l'énoncé T entier, « occupe en partie ». Dans les deux cas, le papier est à citer comme antécédent entre agents, comme 2606.10456 l'est pour le temps. Note : « ses signes » n'est pas défini dans ma consigne ; mon verdict sur C / K porte sur la distinction elle-même. | p. 2, 3, 10 : [OB53] ; [OB50] ; [OB51] ; [OB52] ; [OB15] "This is a modest extension of the single-view bound, not a general result about per-step certification." ; [OB19] ; [OB20] ; [OB46] "Let x1 , . . . , xK be the fragments produced across agent steps" ; [OB10] "full adaptive attackers, and non-code compositional harms remain outside the main claim." |
| L (« 3 ») | voisin | **Fait**, pour la seule agrégation « alarme si l'une » : la détection d'une trajectoire est bornée par le budget de faux positifs dépensé plus la somme des variations totales locales, et la formule 1 − (1 − α)^K vaut sous indépendance. **Non fait** : un budget B de l'attaquant ; une statistique additive ; la puissance en fonction de (B, n₀, loi honnête, α) pour toute répartition ; l'effondrement du maximum quand la fragmentation croît, au seuil exact (L2) ; le calendrier et le prix de la garantie toujours valide (L3). **Raisonnement du lecteur, non tiré du papier** : la borne de l'union ne montre pas l'effondrement de L2. Si un budget fixe est réparti en K petits décalages, la somme des variations totales locales reste de l'ordre du budget, et la borne ne décroît pas avec K. | p. 10, 16 : [OB16] ; [OB17] ; [OB18] ; [OB55] "For example, setting α ≈ 1/K already gives FPRtraj ≈ 1 − e−1 ≈ 0.63." ; balayage en K [OB37], [OB38] |
| H2 | voisin | **Fait** : le calibrage sur trafic bénin seul (les seuils, et le moniteur à une classe). **Non fait** : l'accumulation séquentielle, les sondes internes, la garantie toujours valide, le rappel selon l'horizon. **Indice non transposable** : le moniteur entraîné sur le bénin seul ne détecte que 6 % des attaques à 1 % de faux positifs. **Raisonnement du lecteur, non tiré du papier** : la variation totale est sous-additive pour des pas indépendants (sous la loi honnête comme sous l'attaque). Si chaque action sabotée était indiscernable à ε près dans la vue de la sonde, aucune statistique sur K actions ne gagnerait donc plus d'environ Kε. H2 suppose ainsi un écart par action faible mais non nul : sous le seuil, pas indiscernable. | p. 11, 13 : [OB22] "Runtime gates are calibrated to a 5% benign false-positive rate on held-out benign trajectories." ; [OB23] "it never sees an attack, so its negatives are benign trajectories and its test-time positives are the attack families." ; [OB21] |
| Tr (« 5 ») | voisin | **Fait** : la même question au niveau de la trajectoire, pour l'agrégation des alarmes par pas (« alarme si l'une », de type maximum), en boîte noire ; des essais de réordonnancement et de leurres (le moniteur à une classe est invariant à l'ordre, 0,873). **Non fait** : l'agrégation par attention, les sondes, le passage du jeton à l'action, l'attaquant adaptatif. | p. 10, 14, 15 : [OB19] ; [OB30] "We permute the K fragments before assembly and interleave benign decoy fragments" ; [OB29] "the marker-free one-class monitor is invariant under reordering (0.873)" |
| H3 | voisin | **Fait** : un balayage du nombre de fragments, K ∈ {2, 3, 5, 10}, à charge fixe (donc à budget constant), mais pour des moniteurs en boîte noire seulement. **Non fait** : aucune courbe en boîte blanche, aucune comparaison. Les résultats sont irréguliers et non expliqués (moniteur par pas : 0,000 pour K = 2, 3 et 5 ; 0,972 d'aire et 90 % de détection à K = 10). | p. 16 : [OB37] "10 0.972 / 0.90 1.000 / 0.00 0.728 / 0.00 1.000 / 1.00" ; [OB38] "3 0.000 / 0.00 1.000 / 0.00 0.288 / 0.00 1.000 / 1.00" |
| Statistique de population (papier B) | voisin | **Fait** : des statistiques conjointes entre agents, sur les textes produits : la vue de coordination entre fragments (1,000 sur AgentDojo) et le trait « parallélisme des longueurs entre agents ». **Non fait** : ni états internes, ni copies d'un même modèle, ni co-élévation. | p. 4, 13 : [OB33] ; [OB34] "(vi) cross-agent length parallelism, the coefficient of variation of the K report lengths" |
| HC1 à HC6, H1, H4′, H5, H6, H7, H8 | ne touche pas | — | — |

### Chiffres utilisables

| chiffre | nature | page et citation |
|---|---|---|
| Moniteur à une classe, entraîné sur le bénin seul : aire 0,874 (0,858 à 0,879) ; vrais positifs 0,06 / 0,25 / 0,36 à 1 / 5 / 10 % de faux positifs | auteurs | p. 1 et 11 [OB05, OB35, OB21] |
| Moniteur statistique par pas : aire 0,475 à 0,504 ; vrais positifs 0,02 à 0,03 entre 1 % et 10 % de faux positifs (0,00 pour le détecteur par pas d'AgentDojo) | auteurs | p. 13 et 11 [OB54, OB44] |
| Détecteur livré avec AgentDojo : aire 0,82 à 0,84 sur le découpage naïf ; scores des fragments localement bénins 0,046 contre 0,049 pour le bénin ; vue de coordination entre fragments : 1,000 | auteurs | p. 4 et 13 [OB12, OB25, OB33] |
| Taux de succès d'attaque sans défense ou avec les vues locales : de 0,58 (Llama-3.1-8B) à 1,00 ; avec la vue décodée : 0 sur 50, borne supérieure exacte à 95 % de 0,071 par case | auteurs | p. 5 [OB40, OB39] |
| Attaques bloquées sur 50 : trace complète aveugle au codage 0 ; détecteur livré, en trace complète, 10 | auteurs | p. 7 [OB42, OB41] |
| R-Judge : un classifieur qui ne lit que la longueur des trajectoires atteint 0,940 | auteurs | p. 4 [OB43] |
| Hors du cas du code : moniteur strict 0,406 en langue naturelle, contre 0,956 sur code ; inversion à 0,090 sur du trafic bénin contenant du code | auteurs | p. 6 [OB31, OB32] |
| Agrégation « alarme si l'une » avec α ≈ 1/K : faux positifs de trajectoire ≈ 0,63 | auteurs | p. 10 [OB55] |
| Seuil par action à 1 % et alarme si l'une sur T actions : faux positifs de trajectoire 0,030 (T = 3), 0,096 (10), 0,395 (50), 0,634 (100) | calcul (formule de la Proposition 2, cas indépendant) | — |

### Ce qui n'a pas été lu ou ne se trouve pas dans le PDF

- Les 16 pages ont été lues.
- Absent du PDF :
  - le « supplementary material » au-delà des annexes A à F, notamment l'explication du contrôle par « troncature adaptative », renvoyée à une section 5 qui ne la contient pas [OB27, OB28] ;
  - le dépôt de code, non consulté car hors périmètre.
- Les valeurs des figures 2 et 4 sont reprises par les tableaux 6 et 9.

### Réserves (R4)

- La cécité du moniteur par pas sur le banc de code tient au choix de la statistique : une sonde par fragment sensible au code atteint 1,000 [OB24] "trivially reads that slice and hits AUROC 1.000". La preuve que l'échec résiste à un détecteur appris fort repose sur AgentDojo seul.
- Tableau 14 : l'aire du moniteur par pas vaut 0,000 pour K = 2, 3 et 5 (classement parfaitement inversé), contre environ 0,48 ailleurs, et 0,972 à K = 10. Cette incohérence n'est pas expliquée [OB37, OB38, OB54].
- La vue décodée, qui bloque tout, reçoit la famille d'encodage : c'est un plafond de diagnostic, non déployable [OB48].

---

## 3. 2604.14865v1 — cohérence par segments pour les sondes en flux

### Identité

- Titre : « Segment-Level Coherence for Robust Harmful Intent Probing in LLMs » [SC53], p. 1.
- Auteurs :
  - Xuanli He (University College London) et Bilgehan Sel (Virginia Tech) [SC54] ;
  - Faizan Ali, Jenny Bao, Hoagy Cunningham, Jerry Wei, sous le bloc « Anthropic » (courriels de J. Bao, H. Cunningham et J. Wei seulement) [SC03] ;
  - X. He, B. Sel et F. Ali sont soutenus par le programme Anthropic Safety Fellow [SC04], p. 10.
- Version : v1, 16 avril 2026, catégorie arXiv cs.CL [SC01].
- Venue : aucune. Mention « Preprint. Under review. » [SC02].

### Ce que fait le papier : réponses aux questions des consignes

- **Objet.** Des sondes en flux qui détectent l'intention nuisible dans les domaines chimique, biologique, radiologique et nucléaire, pendant la génération [SC05, SC23]. Modèles : Llama-3.1-8B, Qwen3-8B (ainsi que 14B et 32B), Gemma-2-9B (p. 5).
- **Définition de l'agrégation.**
  - Un logit par jeton : sonde linéaire sur la concaténation des activations de toutes les couches, sorties d'attention ou de perceptron multicouche (p. 3 et 6).
  - Une moyenne sur une fenêtre glissante de 16 jetons [SC13].
  - À l'entraînement : moyenne des K = 8 fenêtres les plus hautes [SC11, SC15], avec une entropie croisée au niveau de l'échange. S'y ajoute SegVar, une variance pondérée des logits de fenêtres, appliquée seulement aux échanges bénins [SC12].
  - À l'inférence : seulement un lissage par moyenne mobile exponentielle, γ = 0,1 [SC14, SC15].
  - Le score d'échange utilisé à l'évaluation n'est pas défini explicitement. La seule indication est l'annexe F, qui prend le maximum sur les jetons du score lissé [SC26]. L'agrégation « cohérente » est donc un biais d'entraînement de la sonde. D'après cette seule indication, la décision au déploiement reste un maximum sur un score lissé.
- **Niveau.** Jeton, puis fenêtre de 16 jetons, puis échange utilisateur–assistant : environ 3 000 jetons dans les domaines chimique, biologique, radiologique et nucléaire, environ 300 dans le domaine générique [SC44].
- **Robustesse adverse testée.**
  - Seulement l'obfuscation par cinq chiffrements de caractères, après affinage du modèle (adaptation de rang faible) pour qu'il les comprenne. Les sondes ne sont pas réentraînées [SC16, SC24].
  - Aucun adversaire conscient de la sonde. Les auteurs le disent [SC18, SC20] et décrivent une attaque par dilution qu'ils n'ont pas testée [SC19].

### Affirmations de la recherche affirmative

| # | affirmation de la recherche affirmative | verdict | page | citation exacte |
|---|---|---|---|---|
| C1 | « 2604.14865 (v1 vue) ; Segment-Level Coherence… ; Xuanli He, Bilgehan Sel, Faizan Ali, Jenny Bao, Hoagy Cunningham, Jerry Wei ; avril 2026 » | **confirmé** (complété : 16 avril 2026, cs.CL, en cours d'examen, sans venue) | 1 | [SC01] "arXiv:2604.14865v1 [cs.CL] 16 Apr 2026" ; [SC54] "Xuanli He Bilgehan Sel University College London Virginia Tech" ; [SC03] "Faizan Ali & Jenny Bao & Hoagy Cunningham & Jerry Wei" ; [SC02] "Preprint. Under review." |
| C2 | « Sondes en flux. » | **confirmé** | 1 ; 3 | [SC05] "Although streaming probes enable real-time monitoring, they still make systematic errors." ; [SC23] "While supervision is available only at the exchange level, deployment requires streaming, token-level predictions as the response is generated" |
| C3 | « Agrège les k meilleures fenêtres, qui doivent se soutenir mutuellement » | **confirmé**, avec précision : c'est l'objectif d'entraînement (K = 8 fenêtres de 16 jetons) ; à l'inférence, il n'y a qu'un lissage exponentiel | 2 ; 4 ; 5 ; 6 | [SC08] "Top-K supportive window aggregation, which requires multiple windows to jointly support a prediction" ; [SC11] "We select the K windows with the highest aggregated logits and average them" ; [SC14] "At inference time only, we apply exponential moving average (EMA) smoothing" ; [SC15] "we set k = 8, λ = 0.01, γ = 0.1, and τs = 2" |
| C4 | « et pénalise la dispersion entre fenêtres ("SegVar") pour supprimer les pics isolés » | **confirmé**, avec précision : seulement sur les échanges bénins, et seulement à l'entraînement | 2 ; 4 | [SC09] "Segment Variance Regularization (SegVar), which penalizes dispersion in logit magnitude across selected evidence windows, suppressing isolated spikes" ; [SC12] "We apply SegVar exclusively to benign exchanges, where spurious, keyword-driven activations are most prevalent." |
| C5 | « Transfert à des modèles affinés sur des chiffrements, jusqu'à 98,85 % d'aire sous la courbe. » | **corrigé** : « Les sondes entraînées sur Llama-3.1-8B-Instruct de base, appliquées sans réentraînement au même modèle affiné pour comprendre cinq chiffrements, atteignent 97,07 % à 98,94 % d'aire sous la courbe (tableau 9, ligne SC-TopK ; moyenne de 98,30 % par calcul), contre environ 57 % à 67 % sans adaptateur. Le chiffre de 98,85 % du texte (« over » dans le résumé, « up to » dans l'introduction) n'apparaît pas dans la ligne SC-TopK, mais dans la ligne SWiM. » | 1 ; 2 ; 9 ; 27 | [SC07] "achieving an AUROC of over 98.85%." ; [SC10] "up to 98.85% AUROC" ; [SC24] "SC-TopK 61.26 97.97 61.95 98.78 61.49 97.07 64.17 98.94 61.50 98.72" ; [SC25] "SWiM 62.38 96.48 62.15 98.21 61.67 96.49 66.16 98.85 61.67 97.77" ; [SC16] "Without adaptation, all probes perform near chance (AUROC≈60%), indicating that the backbone LLM cannot interpret the ciphers and thus exposes no informative internal signal." |
| C6 | « Remet en cause le max au niveau des sous-séquences, au profit d'une agrégation cohérente. » | **confirmé** quant au cadrage des auteurs. Précision : le but est de réduire les faux positifs bénins dus aux mots-clés, par un objectif d'entraînement, sans test de robustesse adverse | 10 ; 4 | [SC21] "Streaming safety probes often rely on max-based aggregation over token-level signals, which leads to a keyword-driven failure mode" ; [SC22] "By replacing token-level maxima with Top-K supportive window aggregation and controlling logit dispersion via SegVar" ; [SC50] "This mechanism functions as a max pooling (Goodfellow et al., 2016) over token positions, emphasizing the most salient spans in the sequence." |
| C7 | « Ni action, ni trajectoire d'agent, ni attaquant entraîné par renforcement. » | **confirmé**. Nuance : un jeu de test générique, ToolACE (540 dialogues avec outils), est noté au niveau de l'échange, sans suivi d'actions | 10 ; 15 ; 20 | [SC18] "Our current evaluation does not fully account for probe-aware adversaries that explicitly optimize against the streaming detection objective." ; [SC20] "the detector is evaluated under a largely static threat model." ; [SC58] "ToolACE 540" ; [SC57] "SC-TopK attains the top result on ToolACE (55.60%)" |

### Antériorité

| énoncé | verdict d'antériorité | composantes faites / non faites | pages et citations |
|---|---|---|---|
| Tr (« 5 ») | voisin | **Fait** : une comparaison, à l'intérieur d'un échange, entre des agrégations de type maximum (softmax, maximum de moyennes glissantes à attention) et la moyenne des K meilleures fenêtres, avec un gain net au régime de faibles faux positifs (log-aire en chimie avec Llama-3.1 : 80,96 contre 70,11 pour le maximum de moyennes glissantes). **Non fait** : ni action, ni trajectoire, ni accumulation entre actions, ni attaquant adaptatif. Les auteurs excluent ce dernier et décrivent eux-mêmes l'attaque par dilution qu'ils n'ont pas testée. **Sur la prémisse de Tr** : ici, le maximum paie un coût en faux positifs bénins, pas en robustesse adverse. Ce n'est donc pas un contre-indice au sens strict. | p. 8, 10, 16, 23 : [SC30] "RMAttn 70.11±1.14 68.03±0.37 72.41±0.76" ; [SC31] "Top-K 80.96±2.83 75.52±0.94 77.60±1.16" ; [SC52] "The final sequence-level logit is obtained by taking the maximum over all window-level aggregated scores" ; [SC19] "A sufficiently sophisticated attacker could, for example, introduce benign scaffolding to dilute segment-level coherence signals or deliberately craft token sequences that smooth and attenuate probe activations over time" ; [SC36] ; [SC33] |
| L (« 3 ») | voisin (faible) | **Fait** : la même dichotomie entre maximum et moyenne de plusieurs fenêtres (K = 1 serait le maximum ; passer de K = 4 à 8 améliore, aller à 16 dégrade), mais de façon empirique et sur les faux positifs bénins. **Non fait** : ni budget, ni loi de puissance. | p. 22 : [SC28] "Performance improves as K increases from 4 to 8" ; [SC29] "further increasing K to 16 degrades performance" |
| H2 | voisin (faible) | **Fait** : une accumulation dans le flux d'un échange (moyenne mobile exponentielle) ; plus la mémoire est longue, meilleure est la détection (figure, sans chiffres). **Non fait** : la supervision utilise des exemples nuisibles ; ni actions, ni garantie toujours valide. | p. 23 : [SC27] "performance degrades monotonically as γ increases, consistently across domains and methods." ; [SC48] "a smaller γ corresponds to slower decay and therefore incorporates information from a longer effective context window, enabling the probe to aggregate more sustained evidence." |
| HC2 | voisin | **Fait** : la robustesse d'une sonde à un contenu chiffré, une fois le modèle affiné pour le comprendre ; sans adaptateur, les sondes sont au hasard. **Non fait** : ni pression graduée, ni coefficient g. | p. 9, 27 : [SC16] ; [SC24] |
| H8 | voisin | **Fait** : le construit (« mots-clés » contre « intention ») est relié à la robustesse aux faux positifs bénins, mesurée sur 448 exemples bénins chargés de mots-clés. **Non fait** : aucun lien avec la robustesse adverse, aucune prédiction. | p. 24 : [SC42] "resulting in 448 bio-harmless examples spanning 64 keywords." ; [SC43] "SC-TopK continues to outperform SWiM, achieving gains of 1.53% on Llama3.1 and 2.66% on Qwen3" |
| H1 (pour mémoire) | **contre-indice faible** | **Fait** : sonde contre classifieur textuel affiné, au régime de faibles faux positifs, sur Llama-3.1. Égalité en biologie (82,15 contre 82,40) ; la sonde gagne en chimie (76,33 contre 66,39) ; le classifieur gagne dans le domaine générique (74,00 contre 66,50), aux définitions « lâches » selon les auteurs. Le domaine le plus flou est donc celui où la boîte noire gagne. **Pourquoi faible** : il s'agit d'intention nuisible, pas de sabotage ; les capacités sont inégales (sonde de 262 000 paramètres, 344 fois moins que le classifieur) ; un seul modèle est chiffré dans le texte. | p. 7, 8 : [SC37] "On the bio-domain, SC-TopK achieves on-par performance with the classifier on Llama3.1 (82.15% v.s. 82.40% log-space AUROC). On the chemical domain, SC-TopK substantially outperforms the classifier (76.33% v.s. 66.39% log-space AUROC)." ; [SC38] "on the generic domain, SC-TopK trails the classifier (66.50% v.s. 74.00% on Llama3.1)." ; [SC55] "the generic high-stakes datasets rely on broad, loosely specified constitutions without expert validation." ; [SC39] "our method uses a single linear layer with only 262K parameters, a 344× reduction" |
| T (« 4 ») | ne touche pas | Seule mention, en travaux futurs : des instructions malveillantes réparties entre plusieurs sources. | p. 10 : [SC51] "malicious instructions may be distributed across retrieved documents or multiple external inputs, creating compositional attack surfaces that are difficult to detect through isolated analysis." |
| HC1, HC2b, HC3, HC4, HC5, HC6, H3, H4′, H5, H6, H7, statistique de population | ne touche pas | Pour HC4 : simple mention, dans les limites, d'un attaquant qui atténuerait les activations [SC19]. | — |

### Chiffres utilisables

| chiffre | nature | page et citation |
|---|---|---|
| +35,55 % de vrais positifs à 1 % de faux positifs « relative to strong streaming baselines ». Gain relatif ou écart en points : le texte est ambigu. La base n'est donnée que par une figure (figure 2) et n'est pas vérifiable ; par analogie avec le +16,80 % (ligne suivante), il pourrait s'agir d'un écart en points sur une seule case | auteurs | p. 1 [SC06] |
| Le « +16,80 % » de log-aire de l'introduction coïncide avec l'écart absolu 82,15 − 65,35 (domaine biologique, Llama-3.1, tableau 6) : un écart en points, sur une seule case | calcul | p. 23 [SC34, SC35] |
| Réduction de 31,2 % de la marge d'erreur : cohérente avec le passage de 97,40 % à 98,21 % (domaine biologique, Llama-3.1) | calcul (vérification) | p. 2 et 20 [SC40, SC41] |
| Log-aire en chimie (Llama-3.1 / Qwen3 / Gemma-2) : maximum de moyennes glissantes 70,11 / 68,03 / 72,41 ; K meilleures fenêtres 80,96 / 75,52 / 77,60 ; avec SegVar 81,68 / 76,22 / 78,14 | auteurs | p. 8, tableau 1 [SC30, SC31, SC32] |
| Log-aire en biologie (mêmes modèles) : maximum de moyennes glissantes 56,50 / 55,23 / 73,20 ; SWiM 65,35 / 60,87 / 70,53 ; K meilleures fenêtres 78,83 / 77,72 / 82,87 ; avec SegVar 82,15 / 80,47 / 84,62 | auteurs | p. 23, tableau 6 [SC33, SC34, SC35, SC36] |
| Écart de log-aire entre les K meilleures fenêtres et le maximum de moyennes glissantes : 10,85 points (chimie) et 25,65 points avec SegVar (biologie), sur Llama-3.1 | calcul | à partir des deux lignes précédentes |
| Chiffrements : 97,07 % à 98,94 % avec adaptateur (SC-TopK), environ 57 % à 67 % sans ; 99,90 % en texte clair | auteurs ; moyenne de 98,30 % par calcul | p. 9 et 27 [SC24, SC16, SC45] |
| Taille de la sonde : 262 000 paramètres, soit 344 fois moins que le classifieur | auteurs | p. 8 [SC39] |
| Échelle (Qwen3-32B, chimie) : log-aire 80,48 contre 77,02 pour SWiM | auteurs | p. 25 [SC49] |
| Jeu bénin chargé de mots-clés : 448 exemples, 64 mots-clés ; gains de 1,53 et 2,66 points sur SWiM | auteurs | p. 24 [SC42, SC43] |
| Longueur des échanges : environ 3 000 jetons (domaines chimique, biologique, radiologique et nucléaire), environ 300 (domaine générique) | auteurs | p. 7 [SC44] |

### Ce qui n'a pas été lu

- Les 36 pages ont été lues par extraction.
- Non exploitables : les valeurs des diagrammes en barres (figures 2 à 5, 9 à 13 et 15) et des cartes de chaleur par jeton (figures 16 à 23). Par suite, la base du +35,55 % n'est pas vérifiable.
- Anomalie mineure : au tableau 4 (p. 20), une ligne de Gemma-2 porte l'étiquette « Selected » à la place d'« Attention » [SC56].

---

## Synthèse (dix lignes au plus)

1. **H2, occupé en partie** par SafeDream (2604.16824) : scores d'états internes accumulés par somme cumulée de Page, mais en conversation, adversaire externe, calibrage avec attaques, sans garantie toujours valide ni seuils publiés (lecture possible : voisin fort).
2. **T, occupé en partie, moitié négative non revendiquée seulement**, par 2607.11751 : vues locales aveugles sous indiscernabilité locale, agrégation « alarme si l'une » bornée, en boîte noire entre agents ; pièces revendiquées non faites, seul un germe du côté K.
3. **Voisins** : L (Proposition 2 de 2607.11751 ; SafeDream pour la détection avant le dommage) ; Tr (2604.14865 : K meilleures fenêtres contre maximum, sans adversaire ; 2607.11751) ; H3 ; statistique de population ; HC2 ; H8.
4. **Contre-indice** : un seul, faible, pour H1 (2604.14865 : le classifieur textuel bat la sonde à faibles faux positifs dans le domaine aux définitions lâches) ; aucun pour H2, T, L ou Tr.
5. **Corrigé, SafeDream** : 0,908 et 7,9 % absents du résumé ; alarme précoce due surtout à l'imagination, pas à la somme cumulée ; identité complétée.
6. **Corrigé, 2607.11751** : contrôles locaux passés seulement sous bénignité et indiscernabilité locales ; 0,874 à compléter par 6 % de détection à 1 % de faux positifs.
7. **Corrigé, 2604.14865** : 98,85 % absent de la ligne SC-TopK du tableau 9 (97,07 à 98,94) ; Top-K et SegVar sont des objectifs d'entraînement.
8. **Retrouvé** : le passage « 1 − (1 − α)^K … budget de faux positifs » est dans 2607.11751, Proposition 2, p. 10. **Introuvable** : 2607.24893 (ni cité, ni sur disque).
9. **Contrôle** : 155 citations contrôlées, 0 échec (premier passage : 1 échec sur 131, citation à cheval sur deux colonnes, remplacée).
