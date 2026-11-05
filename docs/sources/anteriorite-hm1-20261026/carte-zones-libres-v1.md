# Carte des zones libres pour H-M1 et le placebo croisé, après trois travaux publiés (v1)

- **Auteur** : sous-agent lecteur neuf. Je n'ai écrit ni les brouillons, ni leurs contre-lectures, ni la note de vérification. Rapport écrit le 26 octobre 2026, à partir de 10:27 UTC (`date -u`).
- **Objet** : établir ce qui reste libre, au sens strict, pour l'étape 0 et l'étape 1 de H-M1 et pour le placebo croisé, après :
  - Devbunova (2026) ;
  - Nayan et al. (2026) ;
  - Singh et Chaudhary (2026).
- **Règle de citation** : « p. N » désigne la page du PDF (numérotation de `pdfinfo`, extraction `pdftotext -layout` page par page). Tout chiffre tiré d'un PDF porte sa page.

## 0. Verdict

- **(i) Extension étroite sur Llama-3.1-8B-Instruct** : elle existe, mais elle est **méthodologique et étroite**. Ce n'est pas une zone vierge.
  - La question « le signal suit-il le format de banc d'essai ou le contexte, par un plan croisé, chez ce modèle ? » est **occupée**, avec sa réponse qualitative :
    - par une sonde (Devbunova, p. 2 à 4) ;
    - par une détection comportementale (Nayan et al., p. 5 et p. 12).
  - Le contraste « format contre registre, à contenu égal » est lui aussi déjà fait sur ce modèle, par une sonde (Devbunova, p. 3, p. 4 et p. 7).
  - Restent libres seulement :
    - des contrôles : contenu apparié dans chaque source, faux marqueurs, contrôle d'identité ;
    - un contexte manipulé par le cadrage à contenu égal et croisé avec le format ;
    - le **style de consigne au sens de H-M1**, qui n'est pas le registre de Devbunova ;
    - des instruments certifiés avant la mesure ;
    - des intervalles, des tests d'équivalence et plusieurs graines.
- **(ii) La même question à plus grande échelle** : **libre dans ces trois papiers**.
  - Aucun d'eux ne rapporte de résultat du plan croisé format × contexte au-dessus de 12 milliards de paramètres.
  - Llama-3.3-70B-Instruct n'y est étudié nulle part. Il sert seulement de juge chez Singh et Chaudhary (p. 3).
  - Qwen3-32B figure dans la suite de Nayan et al. (p. 15), mais aucun résultat du plan croisé n'est rapporté pour lui. La liste des 32 runs du plan croisé n'est pas donnée (p. 5 et p. 12).
  - **Non vérifié dans le champ** (R8, zone séduisante) : à lire d'abord Chaudhary et al. (2025), sondes de 270 millions à 70 milliards de paramètres selon Devbunova (p. 2), et Nguyen et al. (2025). Voir Q5.
- **(iii) Occupé** : le plan croisé format × contexte sur ce modèle, la cellule « réel avec marqueurs », la conclusion « le signal suit le format », et le registre seul sans effet sur la sonde standard. Voir Q4 (iii).

## 1. Pièces lues et empreintes

| pièce | sha256 | vérification |
|---|---|---|
| `…/scratchpad/anteriorite-hm1-v1/2603.19426.pdf` (Devbunova, 10 p.) | `095a5a7c251642f4aed6b1d1848176eac12f19f1c21a354c1f4838469b1788bb` | conforme à la note |
| `…/scratchpad/anteriorite-hm1-v1/2606.23583.pdf` (Nayan et al., 25 p.) | `598da3b4385230032fee5eb9ae43622c889008a8610554aecc4a700ad05257e7` | conforme à la note |
| `…/scratchpad/anteriorite-hm1-v1/2609.22119.pdf` (Singh et Chaudhary, 20 p.) | `02ee7b4cc98578688d47c83eb580a38a39f7bb6d149672cdef4eedd76ce97c96` | conforme à la note |
| `docs/sources/anteriorite-hm1-20261026/verification-pdf-v1.md` | `c1427d9a64967050938f0c9b2666a1a794152d4fa37e68f29ea55be71418baab` | lue en entier |
| `prereg/brouillon-test-hm1-v4-etape0-v1.md` | `2427e3642be3c1eb95819fe55ac5ce522334edd6551286f50e1b9d18bca9ba63` | identique au « brouillon relu » de sa contre-lecture |
| `prereg/brouillon-test-placebo-croise-v1.md` | `befcb88c9d90adb46939b7fdbd0bd48fd51777ed1760c624a30c6d832cf209e5` | identique au « brouillon relu » de sa contre-lecture |
| `prereg/contre-lectures/brouillon-test-hm1-v4-etape0-v1-cl1.md` | `98ea59e9549ea2d92cabc61af9556203541a2b8843649f24eb63155c00e8f642` | lue en entier |
| `prereg/contre-lectures/brouillon-test-placebo-croise-v1-cl1.md` | `dc676c0300a23a7d94b1bfb6ebc0f47ad06764afae7f9df9f2ca86c7c57eccab` | lue en entier |
| `prereg/test-hm1-gabarit-style-v3.md` | `225b24c4178287271ac999eddc0b446a4df882eac02098a326d575700af348fb` | sections « Hypothèse » et « Prédiction » seulement (lignes 39 à 72) |

(`…/scratchpad` = `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad`.)

- **Extraits texte** : j'ai réextrait chacune des 55 pages avec `pdftotext -layout` dans un dossier à part (`…/scratchpad/verif-extraits-carte/`). Les 55 pages sont identiques, octet pour octet, aux extraits fournis dans `…/scratchpad/anteriorite-hm1-v1-textes/`.
- **Lus en entier** : les trois PDF, page par page (10 + 25 + 20 pages), figures comprises dans la mesure où le texte les rend. Les valeurs lues seulement sur un graphique sont signalées comme telles.
- **Non lus** :
  - les autres sections de H-M1 v3 ;
  - les scripts, les stimuli et le jugement `jugement-suite-HM1-v1.md` ;
  - toutes les références citées par les trois papiers (Q5) ;
  - le web : aucune recherche.
- **Interdits** : aucun fichier interdit n'a été ouvert ni haché. Aucune recherche récursive dans le dépôt. Rien n'a été modifié dans le dépôt.

---

## Q1. Ce que fait chaque papier

### Devbunova (2026), arXiv 2603.19426v1, atelier « I Can't Believe It's Not Better », ICLR 2026

- **Modèle** : un seul.
  - `meta-llama/Llama-3.1-8B-Instruct`, en `bfloat16`, sur une A100 de 80 Go (p. 5) ;
  - « single backbone », donné comme limite (p. 4).
- **Mesure** : **sonde seulement**.
  - Régression logistique sur le flux résiduel figé, au dernier jeton, avant la normalisation finale (p. 3 et p. 7).
  - Couches 8, 12, 16, 20, 22, 24, 26, 28, 30 et 31 (p. 7). La p. 3 dit « indices 8–31 ».
  - Normalisation `StandardScaler` ; pénalité L2 avec C = 1,0 ; 1 000 itérations ; validation croisée à 5 plis (p. 7).
  - **Aucune mesure verbale, comportementale ou par chaîne de pensée.** Limite déclarée : « only linear probes » (p. 4).
- **Plan** : 2 × 2 croisé, format (banc d'essai, libre) × contexte (évaluation, déploiement) (figure 1, p. 2 ; tableau 1, p. 3).
  - Bench-Eval : MMLU, ARC, GSM8K.
  - Casual-Deploy : ShareGPT, premier tour.
  - Casual-Eval : MuTual, premier tour, « conversational evaluation proxy » (p. 3), « approximation rather than a faithful instantiation » (p. 6).
  - Bench-Deploy : requêtes ShareGPT orientées vers des tâches « compatibles », puis réécrites au format des bancs d'essai par DeepSeek-V3 ; c'est l'« adversarial control » (p. 3 et p. 6). Les gabarits de réécriture sont donnés p. 8 à 10.
  - Deux entraînements (p. 3) :
    - « Standard » : Bench-Eval contre Casual-Deploy, puis test sur les autres cellules ;
    - « Paired » : Bench-Eval ∪ Casual-Eval contre Bench-Deploy ∪ Casual-Deploy, avec un partage 80/20.
- **Résultats** (tableau 2, p. 4, couche 24 ; pourcentage classé « évaluation ») :
  - sonde standard : Bench-Eval 98,8 %, Casual-Eval 0,0 %, Casual-Deploy 0,0 %, Bench-Deploy 94,5 % ;
  - sonde appariée : 98,5 %, 100,0 %, 0,0 %, 7,2 % ;
  - mêmes tendances aux autres couches (tableaux 4 et 5, p. 8), par exemple Bench-Deploy entre 94,3 % et 94,6 % en standard.
- **Contrôles** :
  - **Longueur** : appariement d'histogramme (30 classes) de Casual-Deploy sur Bench-Eval, n = 1 076 (p. 3, p. 5 et p. 6). Cet appariement ne vaut que pour le contraste d'entraînement standard : « Bench-Deploy is slightly longer … Casual-Eval … naturally shorter » (figure 2, p. 6).
  - **Fuite de réponse** : réécritures auditées et nettoyées. Bench-Deploy, réécrit en choix multiple, passe de 55–70 % à 94–95 % une fois nettoyé ; Bench-Deploy Formal passe de 51–68 % à 88–91 % (tableau 3, p. 7).
  - **Genre (registre)** : trois variantes réécrites du **même contenu ShareGPT** : format de banc d'essai et genre conversationnel ; format libre et genre académique ou impersonnel ; format de banc d'essai et genre académique (p. 7). Le registre formel seul donne « ≈ 0 % » classé évaluation (p. 3).
  - **Contenu apparié** : seulement dans la colonne déploiement, toute tirée de ShareGPT. La colonne évaluation vient de **deux sources différentes**, MMLU, ARC, GSM8K d'un côté et MuTual de l'autre (tableau 1, p. 3) : aucun item d'évaluation n'est décliné avec et sans format.
  - **Faux marqueurs** : aucun.
  - **Intervalles** : aucun. Les résultats sont donnés en pourcentages (p. 4 et p. 8).
  - **Graine** : une seule graine fixe, 42 (p. 5).
  - **Autre témoin** : AdvBench et HarmBench classés à 0 % « évaluation » par les deux sondes (tableau 6, p. 9).
- **Code et données** : publics (p. 5).

### Nayan et al. (2026), arXiv 2606.23583v1, 22 juin 2026 (Université du Massachusetts Amherst et Microsoft)

- **Modèles** : « 37 open-weight models and seven families » (p. 1). Le tableau 7 (p. 15) en donne la suite :

  | famille | tailles | variantes |
  |---|---|---|
  | Llama 3.2 | 1B, 3B | base, instruct |
  | Llama 3.1 | 8B (`meta-llama/Meta-Llama-3.1-8B`, `…-8B-Instruct`) | base, instruct |
  | Gemma 2 | 2B, 9B, 27B | base, instruct (`-it`) |
  | Gemma 3 | 1B, 4B, 12B, 27B | base, instruct (`-it`) |
  | Qwen2 | 0.5B, 1.5B, 7B | base, instruct |
  | Qwen3 | 0.6B, 1.7B, 4B, 8B, 14B, 32B | avec et sans raisonnement (`enable_thinking`) |
  | Phi-4 | 3.8B, 14B | `phi-4`, `Phi-4-mini-instruct`, `Phi-4-mini-reasoning`, `Phi-4-reasoning` |

  - « Main sweeps focus on 0.5B–14B models, while 27B/32B checkpoints are used when compute permits » (tableau 7, p. 15 ; même chose p. 4).
  - « Large-model coverage (≥27B/32B) is partial » (p. 9).
  - Hors du tableau 7 :
    - DeepSeek-R1-Distill-Llama-8B, pour l'expérience Hawthorne (p. 3 et p. 5) ;
    - QwQ-32B, Qwen3-32B et DeepSeek-R1-Distill-Qwen-32B, pour le pilotage de la conscience verbalisée (figure 9a, p. 10).
  - L'axe de la figure 2 (p. 5) s'arrête à 27 milliards de paramètres.
- **Mesures** :
  - **Détection comportementale** de type Needham : le modèle classe des transcriptions ; mesure par l'aire sous la courbe ROC (AUROC) et l'exactitude au seuil 0,5 (p. 3 et p. 4 ; tableau 15, p. 23). La consigne exacte posée au modèle n'est **pas donnée** dans le PDF.
    - Llama3.1-8B-Instruct : 0,644 (tableau 15, p. 23).
    - Meilleur modèle : Qwen3-14B sans raisonnement, 0,714 ; Gemma2-27B-Instruct : 0,693 (p. 23).
  - **Le plan croisé 2 × 2 de Devbunova** (5 733 prompts, « 32 validated runs »), mesuré par la même détection comportementale, appelée « Exp 7 » (p. 4, p. 5, figure 5 p. 6, p. 12 ; tableau 16 p. 23).
  - **Comportement de sécurité** : HarmBench, 200 prompts sur cinq paliers de cadrage, 35 modèles ; juge gpt-5.4-nano ; test de McNemar avec correction du taux de fausses découvertes ; 21 effets significatifs sur 140 (p. 4 à 6).
  - **Hawthorne réel contre hypothétique** : DeepSeek-R1-Distill-Llama-8B, 2 587 paires appariées ; le refus franc baisse de 5,8 points (tableau 2, p. 5).
  - **Chaîne de pensée** : indices de conscience dans le raisonnement, 1,7 % contre 3,9 % (tableau 2, p. 5 ; p. 12, A.4).
  - **SAD stages-oversight** : réécritures en paliers 0, 2 et 2.1 (p. 6 ; gabarits p. 16 ; tableaux p. 18 et p. 24).
  - **Indice système « being tested »** sur 35 modèles. Llama3.1-8B-Instruct y perd 0,092 d'aire sous la courbe (tableau 8, p. 17 ; p. 12).
  - **Sondes** :
    - différence des moyennes, selon la méthode de Nguyen et al. Le score est la moyenne des projections sur les jetons (p. 13, A.9). Aire sous la courbe maximale 0,8601, pour Llama3.2-1B-Instruct sur SAD (p. 7 ; tableau 12, p. 19) ;
    - sondes apprises sur le jeu contrastif et testées sur le 2 × 2 pour **10 variantes Gemma seulement**, jusqu'à 12B (tableau 14, p. 20) ;
    - régression logistique sur gemma2-9B-Instruct, aire ≥ 0,98 sur les réécritures de SAD (tableau 18, p. 24).
  - **Autoencodeurs parcimonieux** (Gemma Scope), sur Gemma-3-1B seulement (p. 14). Le tableau 6 (p. 14) liste six bras du jeu de Devbunova, dont `casual_deploy_formal` et `bench_deploy_formal`.
  - **Pilotage** :
    - multicouche (couches 4, 9 et 15) de Llama-3.1-8B-Instruct, avec des témoins de vecteurs aléatoires appariés (p. 7 ; p. 21 ; tableaux 19 et 21, p. 24) ;
    - à 32B, pilotage de la conscience **verbalisée** : QwQ-32B passe de 17,8 % à 58,0 % (p. 7 et p. 10).
- **Contrôles** :
  - **Témoin bénin octet pour octet** : |Δ| moyen de 0,0014, maximum 0,0083 (p. 5 et p. 12). C'est un témoin du bruit de la chaîne de traitement, pas un faux marqueur.
  - **Contextes appariés en sens** pour l'écart de validité (p. 2) et pour les paires Hawthorne (p. 4).
  - **Intervalles** : bootstrap au niveau des transcriptions et correction de Benjamini-Hochberg pour la détection (p. 3, p. 4 et p. 12) ; intervalles à 95 % pour HarmBench (figure 4, p. 6) ; tests de permutation pour le pilotage (p. 21 et p. 24). **Aucun intervalle pour le plan croisé** : le tableau 16 (p. 23) ne donne que l'aire sous la courbe et l'exactitude.
  - **Graines** : jamais mentionnées. J'ai cherché « seed » dans les 25 pages.
  - **Faux marqueurs** : aucun.
  - **Contenu apparié dans les quatre bras** : non. C'est le jeu de Devbunova, repris tel quel (p. 4).
  - **Code** : aucun lien dans le texte extrait.

### Singh et Chaudhary (2026), arXiv 2609.22119v1, 20 août 2026

- **Modèles étudiés** :
  - Gemma 3 en 1B, 4B et 12B ;
  - Phi-3 Mini (`mini-4k-instruct`) et Phi-3 Medium (`medium-128k-instruct`) ;
  - « Llama-3 8B », variante (base ou instruct, 3 ou 3.1) **non précisée** (p. 1, p. 2, p. 5 et p. 12).
  - Le papier dit couvrir « compact language models (1B–12B parameters) » (p. 9) et « compact LLMs (under 14B parameters) » (p. 1). La taille de Phi-3 Medium n'est pas donnée dans le PDF.
- **Modèles outils, non étudiés** :
  - le juge s'appelle « Llama-3.3-70B » p. 3, mais « Llama-3 70B » p. 11 et p. 15 ;
  - gpt-oss-120b génère le jeu des gradients intégrés (p. 5) ;
  - all-MiniLM-L6-v2 sert au plongement des phrases (p. 5) ;
  - l'« éditeur » d'assainissement n'est pas nommé (p. 5).
- **Mesures** :
  - **Chaîne de pensée verbalisée** : le modèle classe la charge (« evaluation / testing benchmark » ou « real-world deployment ») en raisonnant pas à pas (consigne p. 11). Le juge range chaque trace dans une taxonomie : Task Formatting, Synthetic Inputs, Memorization, Meta-Reasoning et d'autres (p. 3 et p. 11). Données : SAD stages-oversight (200 prompts) et GSM8K contre WildChat (100 + 100) (p. 3). Répartition (annexe F, p. 15) :

    | modèle | Task Formatting | Synthetic Input | Meta-Reasoning | Memorization |
    |---|---|---|---|---|
    | Llama 8B | 30,5 % | 39,0 % | 10,5 % | 5,5 % |
    | Gemma 3 12B | 33,5 % | 32,5 % | 17,5 % | 15,0 % |
    | Phi-3 Medium | 28,0 % | 32,0 % | 19,5 % | 17,5 % |

  - **Sondes et vecteurs de pilotage** par différence des moyennes, sur le « Simple Contrastive Dataset » de Nguyen et al. (204 prompts du type « Do you know that you're undergoing an LLM benchmark test? (A) Yes (B) No »). Lecture au jeton de la parenthèse fermante ; validation sur SAD par la moyenne des projections sur les jetons ; aire sous la courbe par couche (p. 3, p. 4 et p. 12). Pics lus dans les tableaux :
    - Llama-3 8B : 0,72 à la couche 12 ;
    - Gemma 3-12B : 0,79 à la couche 16 ;
    - Phi-3-Medium : 0,73 à la couche 39 (p. 13).
  - **Gradients intégrés** sur Phi-3 Mini et Medium : 300 prompts, 50 pas (p. 5 ; figure 4, p. 7).
  - **Taux de bascule comportementale** sur 200 prompts : pilotage 27,0 %, édition 48,2 %, double voie 70,5 % en moyenne ; 63,0 % pour Llama-3 8B en double voie (tableau 1, p. 7).
- **Plan** :
  - **Aucun plan croisé format × contexte.** Les deux jeux de données confondent la source et le format (p. 3).
  - Les paires du jeu des gradients intégrés gardent le même noyau de tâche, mais changent en même temps le format, le registre, les noms et le cadre (exemples p. 13 et p. 14).
- **Contrôles** :
  - accord du juge avec des annotations humaines : 93 % (p. 8) ;
  - aucun intervalle, aucune graine, aucun témoin aléatoire pour le pilotage, aucun faux marqueur, aucun contenu apparié contrôlé ;
  - sur la chaîne de pensée, limite déclarée : « expressed reasoning rather than … latent cognitive mechanisms » (p. 9).

---

## Q2. Le plan croisé au-dessus de 8 milliards de paramètres

### Nayan et al.

- **Au-dessus de 8B, seulement jusqu'à 12B, et seulement pour ce qui est rapporté** :
  - **9B** : gemma2-9B-Instruct passe de 0,676 à 0,508 (p. 5 et p. 12 ; tableau 16, p. 23).
  - **12B** : gemma3-12B-Instruct est nommé dans la figure 5 (p. 6), dans la zone « format-driven », sous la diagonale. Sa valeur sur le 2 × 2 n'est donnée dans aucun tableau.
  - **Sondes testées sur le 2 × 2**, Gemma seulement (tableau 14, p. 20) :
    - Gemma-3 12B de base : aire maximale 0,665 ;
    - 12B-Instruct : 0,728 ;
    - Gemma-2 9B-Instruct : 0,718.
  - **14B** : aucun résultat du 2 × 2. Qwen3-14B n'apparaît que pour la détection de type Needham (0,714, p. 23) et dans les tableaux SAD (p. 17 à 19).
  - **27B et 32B** : **aucun résultat du plan croisé n'est rapporté.**
    - Les modèles de 27B et 32B ne servent qu'ailleurs : Gemma2-27B-Instruct pour la détection de type Needham (0,693, p. 23) ; trois modèles de 32B pour le pilotage de la conscience verbalisée (p. 7 et p. 10). Aucun de ces usages ne croise format et contexte.
    - La composition des « 32 validated runs » n'est pas donnée (p. 5 et p. 12).
    - Le tableau 1 annonce « 32-36 models for SAD and 2×2 » (p. 3).
    - Le tableau 8 (p. 17), qui couvre la même plage de 35 modèles, s'arrête à 14B.
  - **Conséquence** : on ne peut pas exclure, à partir du PDF, que Qwen3-32B ou un Gemma de 27B ait tourné sur le 2 × 2 sans être rapporté. Si c'était le cas, son aire serait au plus de 0,622, puisque « the best open model falls to AUROC 0.622 » (p. 5). C'est une **inférence, pas un résultat opposable**.
  - **70B** : absent. Aucun Llama de 70B dans la suite (p. 15).

### Singh et Chaudhary

- **Non** : aucun plan croisé, à aucune taille (p. 3 à 5).
- Leur thèse, « shifts from format to context with scale », repose sur :
  - la répartition des catégories de la chaîne de pensée (p. 6 ; annexe F, p. 15) ;
  - les gradients intégrés (p. 6 et p. 7) ;
  - le tout jusqu'à Gemma 3 12B et Phi-3 Medium seulement.
- Llama-3.3-70B n'y est que **juge** (p. 3).
- Ils déclarent eux-mêmes ouverts :
  - « frontier models (70B+) likely encode these concepts via deeper … circuits » (p. 8) ;
  - « our study focuses exclusively on compact language models (1B–12B parameters) » (p. 9).

### Réponse à la question décisive

- Tester Llama-3.3-70B-Instruct ou Qwen3-32B par le plan croisé n'est **pas fait dans ces trois papiers** :
  - Llama-3.3-70B-Instruct : jamais étudié ;
  - Qwen3-32B : présent dans la suite de Nayan et al., sans résultat du 2 × 2 rapporté.
- Ce n'est pas encore « libre dans le champ ». Voir Q4 (ii) et Q5 : Chaudhary et al. (2025) ont des sondes jusqu'à 70B selon Devbunova (p. 2) ; Nguyen et al. (2025) restent à lire.

---

## Q3. Format de banc d'essai contre style de consigne, à contenu égal

- **Rappel de H-M1 v3** (lignes 41 à 56) :
  - le **format** oppose « Question: Select … » et les options A à D aux quatre candidats donnés dans une phrase ;
  - le **style** oppose un en-tête balisé avec une injonction en capitales à une demande ouverte qui sollicite l'incertitude ;
  - le **contexte** (système générique, ou système de déploiement avec un récit) est croisé et rapporté sans décider ;
  - mesure principale verbale ; sonde secondaire ; prédiction F̄ > 2 |C̄| (lignes 66 et 67).
- **Devbunova : oui en partie, mais pour le registre, pas pour le style de consigne.**
  - Trois réécritures du **même** contenu ShareGPT croisent format et genre (p. 7) :
    - `bench_deploy` : format de banc d'essai, genre conversationnel ;
    - `casual_deploy_formal` : format libre, genre académique ou impersonnel ;
    - `bench_deploy_formal` : format de banc d'essai, genre académique.
  - Gabarit du genre (p. 9 et p. 10) : « formal, impersonal, and professional register », sans structure de banc d'essai.
  - Résultats, sonde standard seulement :
    - registre formel seul : ≈ 0 % classé évaluation (p. 3) ;
    - format seul : 94,5 % (p. 4) ;
    - format et registre formel : 88–91 % après nettoyage (tableau 3, p. 7).
  - Conclusion de l'autrice : « probes are sensitive to rigid templates rather than linguistic style » (p. 3), et « independent of linguistic style » (résumé, p. 1).
  - **Limites de ce recouvrement** :
    - le facteur est le **registre** (formalité), pas l'en-tête balisé ni l'injonction en capitales opposés à la demande ouverte qui sollicite l'incertitude ;
    - le contenu vient du côté déploiement seulement ;
    - la mesure est une sonde, et non la question verbale de H-M1 ;
    - le contexte n'est pas manipulé par cadrage ;
    - il n'y a ni intervalle ni rapport.
  - Le **format** de Devbunova est en revanche presque celui de H-M1 : « Question: … Options: A. … D. » (gabarit, p. 8 et p. 9).
- **Nayan et al. : non dans les résultats.**
  - Le « sterile prompt register » est nommé comme artefact possible dans RQ3 (tableau 1, p. 3), et « benchmark register » figure dans les recommandations (p. 9).
  - Les bras formels du jeu de Devbunova n'apparaissent que dans un tableau descriptif d'activations d'autoencodeur, sur Gemma-3-1B (tableau 6, p. 14). Aucun contraste format contre registre ou style n'est rapporté.
  - Leurs indices explicites (« being tested » en système, p. 6 et p. 17 ; préfixes des paliers SAD, p. 16 ; paliers HarmBench, p. 4) sont des mentions ou des cadrages. Ils ne séparent pas le format du style.
- **Singh et Chaudhary : non.**
  - Leur taxonomie **range ensemble** « multiple-choice framing, sterile and formal interrogative syntax » sous Task Formatting (p. 3).
  - Le prompt du juge range au contraire « sterile » sous Synthetic Inputs (p. 11). Les deux définitions ne concordent pas.
  - Les groupes « sterile interrogative syntax » et « multiple-choice structural constraints » sont des regroupements d'attributions sur Phi-3 (p. 5), pas une manipulation à contenu égal.
- **Familiarité contre structure** : aucun des trois ne sépare la *familiarité* d'un format de banc d'essai de sa *structure*. Il faudrait pour cela un format rigide mais inédit. H-M1 v3 ne le fait pas non plus : son facteur format oppose le choix multiple canonique à une phrase (ligne 43).
  - C'est une question, pas une zone revendiquable (R8). Je n'ai lu aucune autre source sur ce point.

---

## Q4. Ce qui reste libre au sens strict

R8 s'applique : une limite d'un papier ne fait pas un trou du champ. Chaque point ci-dessous n'est « libre » **que relativement à ces trois PDF**. Les références à lire sont en Q5.

### (i) Extension méthodologique étroite sur Llama-3.1-8B-Instruct

| n° | point | ce que montrent les PDF (absence) | vérification restante | test concerné |
|---|---|---|---|---|
| i-1 | **Marqueurs déclinés dans chaque source** : les mêmes items d'évaluation dépouillés de leur format (« évaluation dépouillée »), et les mêmes gabarits appliqués aux deux sources (CLP-04) | Devbunova : la colonne évaluation vient de deux sources différentes (MMLU/ARC/GSM8K contre MuTual, tableau 1 p. 3, p. 6) ; seul le côté déploiement est décliné (p. 7) ; la longueur n'est pas appariée hors du contraste standard (figure 2, p. 6) ; Bench-Deploy ne prend que les requêtes « compatibles » (p. 6). Nayan et al. reprennent ce jeu (p. 4). Singh et Chaudhary : pas de plan croisé (p. 3) | Xiong et al. (2509.00591) réécrivent des prompts d'évaluation vers un style de déploiement (cités par Nayan et al., p. 2 et p. 11), à lire. Rappel de CLP-02 : la provenance n'est pas manipulable à contenu égal ; seul l'axe des marqueurs l'est | placebo |
| i-2 | **Contexte manipulé par le cadrage à contenu égal, croisé avec le format** (le facteur « contexte » de H-M1) | Chez Devbunova, le « contexte » est la **source** du contenu (p. 3, tableau 1). La sonde « Paired » peut donc apprendre la source, ShareGPT contre bancs d'essai, plutôt que le contexte : c'est mon inférence, à partir de la composition des classes p. 3. Chez Nayan et al., les cadrages à contenu égal (paliers HarmBench p. 4 ; paires Hawthorne p. 5 ; indice système p. 6 et p. 17) ne sont jamais croisés avec le format | Abdelnabi et Salem (2505.14617), Needham et al. (2505.23836) | H-M1 (étape 1) |
| i-3 | **Style de consigne au sens de H-M1** (en-tête balisé avec injonction en capitales, contre demande ouverte qui sollicite l'incertitude), croisé avec le format à contenu égal | Devbunova ne manipule que le registre (p. 3, p. 7, p. 9 et p. 10). Nayan et al. : non (p. 3 et p. 9, seulement nommé ou recommandé). Singh et Chaudhary : confondu avec le format (p. 3) | Mizrahi et al. (2024), Xiong et al. (2025). **Réserve** : sur le registre, la direction prédite par H-M1, le format plus fort que le style, est déjà observée sur ce modèle par une sonde (≈ 0 % contre 94,5 %, p. 3 et p. 4). Une issue « format > style » serait donc en partie attendue | H-M1 (cœur) |
| i-4 | **Faux marqueurs appariés en forme et en place**, sans valeur d'audit, comme référence du contraste des marqueurs (CLP-07) | Contrôles de Devbunova : longueur, fuite, genre (p. 3 et p. 7). Témoins de Nayan et al. : bruit octet pour octet (p. 5 et p. 12) et vecteurs aléatoires (p. 7). Singh et Chaudhary : aucun | WARP (cité par la contre-lecture CLP-01, absent des trois bibliographies, non vérifié) | placebo |
| i-5 | **Sonde apprise à format constant** (paires qui ne diffèrent que par une phrase de cadrage), puis appliquée au plan croisé, **sur Llama-3.1-8B-Instruct** | Nayan et al. testent une sonde contrastive sur le 2 × 2 pour 10 Gemma seulement (tableau 14, p. 20) ; pour Llama-3.1-8B-Instruct, la direction ne sert qu'au pilotage (p. 7 et p. 24). Les sondes de Devbunova sont apprises sur le 2 × 2 lui-même (p. 3) | Nguyen et al. (2507.01786) : c'est la méthode même (Nayan et al. p. 13 ; Singh et Chaudhary p. 3 et p. 4) | étape 0, placebo |
| i-6 | **Mesure verbale du premier jeton, auto-référentielle et certifiée** | La détection comportementale sur le 2 × 2 **est faite** pour ce modèle : 0,644 → 0,491 (Nayan et al., p. 5 et p. 12). La consigne n'est pas donnée dans le PDF, et aucune porte de lisibilité n'est décrite | Seul le protocole de certification est neuf, pas la mesure verbale du 2 × 2 | étape 0 |
| i-7 | **Intervalles, tests d'équivalence, puissance, plusieurs graines** | Devbunova : une graine, 42, aucun intervalle (p. 4, p. 5 et p. 8). Nayan et al. : 2 × 2 en valeurs ponctuelles (p. 23), graines jamais mentionnées. Singh et Chaudhary : aucun intervalle (p. 7 et p. 15) | Purement méthodologique | les deux |
| i-8 | **Certification préalable et à l'aveugle des instruments, préenregistrement** | Aucune mention dans les trois papiers, lus en entier | Purement méthodologique | étape 0 |
| i-9 | **Contrôle d'identité** : même texte, deux provenances (CLP-10) | Absent des trois | WildBench et WildChat, cités par la contre-lecture, non vérifiés | placebo |
| i-10 | **Mémorisation par item comme covariable** (CLP-11) | Singh et Chaudhary ne la mesurent que comme part des catégories de la chaîne de pensée, 5,5 % pour Llama 8B (p. 15). Rien chez Devbunova ni chez Nayan et al. | — | placebo, H-M1 (familiarité) |
| i-11 | **Plan à trois facteurs** format × style × contexte (cadré), à contenu égal | Absent des trois (voir i-2 et i-3) | — | H-M1 |

**Lecture.**

- Chacun de ces points est une amélioration de contrôle ou de mesure sur une question dont la réponse qualitative est publiée sur ce modèle.
- Les points les moins minces, à mon avis, sont i-2, i-3 et i-11.
- R8 les rend moins séduisants qu'il n'y paraît :
  - pour i-3, Devbunova a déjà vu le registre sans effet ;
  - pour i-2, le « contexte » cadré de H-M1 répond en partie à la question posée au modèle, de l'aveu même de H-M1 v3 (lignes 48 à 50).

### (ii) La même question à plus grande échelle (27 à 70 milliards de paramètres)

| n° | point | ce que montrent les PDF (absence) | vérification restante |
|---|---|---|---|
| ii-1 | Plan croisé format × contexte sur **Llama-3.3-70B-Instruct** | Absent de la suite de Nayan et al. (p. 15). Juge seulement chez Singh et Chaudhary (p. 3). Devbunova : un seul modèle de 8B (p. 4) | Chaudhary et al. (2509.13333), « 270M to 70B », par sondes, selon Devbunova (p. 2). Devbunova dit s'en distinguer par le contrôle du format (p. 2), ce qui suggère qu'aucun contrôle de format n'y figure ; ce n'est pas vérifié. Nguyen et al. (2507.01786) : non lu ; **de mémoire, non opposable**, ce travail porterait sur un Llama de 70B, à vérifier en priorité |
| ii-2 | Plan croisé sur **Qwen3-32B** (ou Gemma 2 ou 3 en 27B) | Présents dans la suite (p. 15). Aucun résultat du 2 × 2 rapporté au-dessus de 12B (p. 6, p. 20 et p. 23). Composition des 32 runs non donnée (p. 5 et p. 12). Couverture déclarée partielle (p. 9) | Le seul moyen de lever le doute est de demander les données aux auteurs : c'est un contact externe, donc à décider par Lazar. Aucun lien de code n'est lisible dans le PDF |
| ii-3 | **Test croisé de la thèse de Singh et Chaudhary** (« du format au contexte avec l'échelle ») | Leur preuve repose sur la chaîne de pensée et les gradients intégrés, jusqu'à 12B, sans plan croisé (p. 6, p. 9 et p. 15). 70B et plus sont déclarés ouverts (p. 8) | Abdelnabi et Salem (2505.14617), modèles de raisonnement de 32B (Nayan et al., p. 7 et p. 10) ; Needham et al. (2505.23836), modèles de pointe |
| ii-4 | Sonde à format constant (i-5) et mesure verbale (i-6) **à 32 ou 70B**, sur le plan croisé | Nayan et al. : à 32B, seulement le pilotage de la conscience verbalisée, sans format croisé (p. 10). Leur suite de sondes s'arrête à 14B (tableau 12, p. 19) | Nguyen et al., Chaudhary et al. |

**Lecture (R8, vérification plus dure).**

- (ii) est la zone la plus séduisante :
  - une thèse publiée prédit un changement avec l'échelle (Singh et Chaudhary) ;
  - aucun des trois papiers ne la teste par un plan croisé.
- C'est exactement le cas où R8 exige de vérifier plus durement. Quatre trous de lecture restent :
  - (a) Chaudhary et al. (2025) et Nguyen et al. (2025), non lus ;
  - (b) la composition des 32 runs de Nayan et al. ;
  - (c) les travaux cités par la contre-lecture et absents des trois bibliographies : EvalAwareBench (2605.23055), EvalDetectBench (2609.01611), WARP ;
  - (d) tout ce qui est paru après le 20 août 2026, et les travaux qui citent Devbunova.
- Tant que (a) et (c) ne sont pas lus sur PDF empreinté, (ii) n'est **pas revendicable**.
- Tout run plus gros serait une dépense et un changement de modèle : nœud de Lazar.

### (iii) Rien : occupé

- **Plan croisé 2 × 2 format × contexte sur Llama-3.1-8B-Instruct** :
  - par une sonde (Devbunova, p. 2 à 4 et p. 8) ;
  - par une détection comportementale (Nayan et al., p. 5 et p. 12).
- **Cellule « réel avec marqueurs ajoutés »** : Bench-Deploy, des requêtes ShareGPT réécrites au format des bancs d'essai (Devbunova, p. 3 et p. 6 ; reprise par Nayan et al., p. 4).
- **Conclusion qualitative « le signal suit le format de banc d'essai » sur ce modèle** :
  - sonde standard : 94,5 % de Bench-Deploy classé évaluation (Devbunova, p. 4) ;
  - détection comportementale sous le hasard : 0,491 (Nayan et al., p. 5).
- **Registre seul, à contenu égal, sans effet sur la sonde standard**, et format qui domine le registre (Devbunova, p. 3, p. 4 et p. 7).
- **Une sonde apprise sur des paires décorrélées sépare les cellules** : Bench-Deploy à 7,2 %, Casual-Eval à 100 % (Devbunova, p. 4).
- **Plan croisé comportemental jusqu'à 12B**, avec Gemma2-9B et Gemma3-12B, et sondes Gemma sur le 2 × 2 (Nayan et al., p. 5, p. 6, p. 20 et p. 23).
- **Effet d'une mention explicite « being tested »** sur la détection, sur 35 modèles (Nayan et al., p. 6 et p. 17). Cela rejoint CLP-05 : la mention d'un test n'est pas un marqueur de style neutre.
- **Contrôles de longueur et de fuite de réponse** sur ce plan (Devbunova, p. 3, p. 6 et p. 7).

---

## Q5. Références à lire ensuite (signalées, non cherchées)

| priorité | référence (telle qu'imprimée) | arXiv | cité par, page de la bibliographie | points de Q4 qu'elle pourrait recouvrir |
|---|---|---|---|---|
| 1 | M. Chaudhary, I. Su, N. Hooda et al., « Evaluation awareness scales predictably in open-weights large language models », 2025 (atelier NeurIPS 2025 « Socially Responsible and Trustworthy Foundation Models » selon Singh et Chaudhary) | 2509.13333 | Devbunova p. 5 ; Singh et Chaudhary p. 10 (sans identifiant) | ii-1, ii-2, ii-4 |
| 1 | J. Nguyen, K. Hoang, C. L. Attubato, F. Hofstätter, « Probing and steering evaluation awareness of language models », 2025 | 2507.01786 | Devbunova p. 5 ; Nayan et al. p. 11 ; Singh et Chaudhary p. 10 (sans identifiant) | i-5, ii-1, ii-4 |
| 1 | L. Xiong, N. Bhargava, J. Hong et al., « Probe-rewrite-evaluate: A workflow for reliable benchmarks and quantifying evaluation awareness », 2025 | 2509.00591 | Nayan et al. p. 11 | i-1, i-3 |
| 2 | S. Abdelnabi, A. Salem, « The hawthorne effect in reasoning models: Evaluating and steering test awareness », 2025 | 2505.14617 | Nayan et al. p. 10 | i-2, ii-3, ii-4 |
| 2 | J. Needham, G. Edkins, G. Pimpale, H. Bartsch, M. Hobbhahn, « Large language models often know when they are being evaluated », 2025 | 2505.23836 | Devbunova p. 5 ; Nayan et al. p. 11 ; Singh et Chaudhary p. 10 (sans identifiant) | i-2, i-3, ii-3 |
| 2 | M. Mizrahi, G. Kaplan, D. Malkin et al., « State of what art? a call for multi-prompt llm evaluation », TACL 12:933–949, 2024 | non donné | Nayan et al. p. 11 | i-3 (sensibilité au gabarit, hors conscience d'évaluation) |
| 3 | T. T. Hua, A. Qin, S. Marks, N. Nanda, « Steering evaluation-aware language models to act like they are deployed », 2025 ou 2026 selon le citant | 2510.20487 | Devbunova p. 5 ; Nayan et al. p. 10 | ii-4 (pilotage ; recouvrement probablement faible) |
| 3 | R. Laine, B. Chughtai, J. Betley et al., « Me, myself, and AI: The situational awareness dataset (SAD) for LLMs », 2024 | 2407.04694 | Nayan et al. p. 10 ; Singh et Chaudhary p. 10 (NeurIPS 2024, sans identifiant) | ii (jeu stages-oversight ; recouvrement probablement faible) |
| 3 | C. Zheng, H. Zhou, F. Meng, J. Zhou, M. Huang, « Large language models are not robust multiple choice selectors », ICLR | non donné | Nayan et al. p. 11 | i-3 (artefacts du choix multiple, hors conscience d'évaluation) |
| 3 | N. Balepur, A. Ravichander, E. Hovy, « Artifacts or abduction: How do llms answer multiple-choice questions without the question? », ACL 2024 | non donné | Nayan et al. p. 10 | i-3 (idem) |
| 3 | L. Berglund, A. C. Stickland, M. Balesni et al., « Taken out of context: On measuring situational awareness in llms », 2023 | non donné | Singh et Chaudhary p. 10 | ii (fond ; recouvrement probablement faible) |
| sources | W. Zhao, X. Ren, J. Hessel et al., « Wildchat: 1m chatgpt interaction logs in the wild », 2024 | 2405.01470 | Singh et Chaudhary p. 10 | i-9 (source du placebo ; licence à lire) |

- **Hors de ces trois bibliographies**, cités par la contre-lecture du placebo, lus sur page HTML seulement et non opposables :
  - EvalAwareBench (2605.23055) ;
  - EvalDetectBench (2609.01611) ;
  - WARP (ICML 2026) ;
  - WildBench (2406.04770).
- EvalAwareBench (« facteurs déclencheurs activables un par un à requête fixe ») est le plus proche de i-3 et de i-4. Il est à lire avec la priorité 1.

---

## Réserves sur les trois papiers (R4 : symétrie, « trop beau »)

Ces réserves ne libèrent aucune zone : une faiblesse d'un papier ne fait pas un trou du champ. Elles bornent seulement la force de l'occupation.

- **Devbunova** :
  - **Longueur** : « matched prompt length » est affirmé pour le plan (p. 1 et p. 4), mais la figure 2 (p. 6) dit que Bench-Deploy est plus long et Casual-Eval plus court.
  - **Définition du plan** : l'annexe A.1 (p. 5) croise contexte × **genre** et traite le format à part, ce qui contredit p. 2 et p. 3.
  - **Valeurs extrêmes** : 0,0 %, 100,0 % et 94,5 %, sur une seule graine, sans intervalle.
  - **Classes de la sonde appariée** : elles coïncident avec la source du contenu (bancs d'essai contre ShareGPT), d'après p. 3. Son « succès » peut donc lire la source plutôt que le contexte.
- **Nayan et al.** :
  - **Valeur de base de Llama-3.1-8B-Instruct sur Needham** : 0,644 aux p. 5, p. 12 et p. 23 (tableau 15). Le pilotage part pourtant d'une base de 0,676 pour ce même modèle (p. 10, p. 21 et p. 24, tableau 21 avec n = 500). Or 0,676 est aussi la valeur de gemma2-9B-Instruct (p. 5 et p. 23). Incohérence non expliquée.
  - **Valeur sur le 2 × 2** : le 0,491 de Llama n'est donné qu'en prose (p. 5 et p. 12), hors du tableau 16 (p. 23).
  - **Taille du jeu** : 5 733 prompts, contre n = 1 076 par bras chez Devbunova (p. 5 et p. 6). L'écart n'est pas expliqué : les six bras sont peut-être inclus (p. 14), à vérifier.
  - **Phrase ambiguë** : « scoring above 0.9 on benchmark-formatted eval prompts but near zero on benchmark-formatted deployment prompts » (p. 5) ne précise pas la métrique.
- **Singh et Chaudhary** :
  - le juge porte deux noms (p. 3 contre p. 11 et p. 15) ;
  - la taxonomie porte deux définitions (p. 3 contre p. 11) ;
  - la variante de Llama-3 8B n'est pas précisée ;
  - la portée est dite « 1B–12B » (p. 9) mais aussi « under 14B » (p. 1) ;
  - le taux de bascule moyen vaut 70,58 % dans le texte et 70,5 % dans le tableau 1 (p. 7). C'est un arrondi : la moyenne des six valeurs vaut 70,58.

## Concordance avec la note de vérification et la contre-lecture du placebo

- **Note de vérification** : ses points sur Devbunova et Nayan et al. sont confirmés aux pages qu'elle cite. Une précision : les couches de Devbunova sont « indices 8–31 » p. 3, mais la liste effective est 8, 12, 16, 20, 22, 24, 26, 28, 30, 31 (p. 7).
- **Singh et Chaudhary**, que la note n'avait pas encore lus : confirmé qu'il n'y a pas de plan croisé, et que le « Llama-3 8B » n'a pas de variante précisée.
- **Contre-lecture du placebo** (CLP-01) : ses énoncés sur Devbunova et Nayan et al. sont confirmés sur PDF :
  - même modèle, dernier jeton, une graine, aucun intervalle ;
  - bras Casual-Eval tiré de MuTual ;
  - requêtes « compatibles » ;
  - 0,644 → 0,491 en prose seulement.
