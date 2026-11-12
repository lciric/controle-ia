# Erratum de `synthese-boucle-moisson-v1.md` — v1

## En-tête

- **Lecteur** : sous-agent neuf, modèle **Fable 5.1** (`claude-fable-5-1`) — c'est le modèle de l'espèce A du run et celui du lecteur de la synthèse v1 ; je le dis d'emblée. Je n'ai écrit ni les critères, ni la question, ni les faits, ni la synthèse v1, ni la relecture d'Opus, ni aucune cellule.
- **Consigne appliquée** : `consigne-erratum-synthese-boucle-moisson-v1.md` (`c5c75d58…`), lue en entier d'abord.
- **Date UTC** (`date -u`) : `Sun Nov  1 16:08:07 UTC 2026` au début de la lecture ; `Sun Nov  1 16:19:55 UTC 2026` après la lecture complète, avant l'écriture.
- **Lu** : la consigne ; la synthèse v1 (247 lignes, intégrale) ; la relecture d'Opus 5.5 (267 lignes, intégrale) ; les critères de la boucle et ceux du tour 1 des nœuds ; la question servie ; les faits servis par morceaux (lignes 26, 104-109, 167-168, 174, 209, 228, 433, 582-587, 594, 622-632, 736-742, 749-750, 771, et recherches par motif) ; les douze cellules du run, intégrales ; `etat.md` du run. Un seul motif cherché hors de cette liste : « Opus 4.6 » dans `devis-collisionneur-boucle-moisson-v1.md` (même dossier, l. 11), pour le point 6 de l'erratum demandé ; rien d'autre n'y a été lu.
- **Non lu** : aucun fichier « annexe-tour-2 » ; rien sous `donnees/mode-tenu-a-l-ecart-v1`, `donnees/collisionneur-evasion-moniteurs-v1`, `donnees/bras-attaque-*`, `quarantaine/`, `donnees/runs/`, `diag/`, `prereg/P3-consignes-v1.md`, ni dans les autres dossiers de `donnees/` ; ni le dossier factuel de l'organisme (seule la pièce 1 des faits en est servie), ni les PDF de l'antériorité, ni `journal.jsonl` du run.
- **Rien décidé, rien recommandé, aucune espèce classée, aucun fichier existant modifié, rien scellé, rien commis, aucun appel payant ni réseau.** Deux fichiers neufs rendus (vérifiés absents avant écriture) : cet erratum et `synthese-boucle-moisson-v2.md`.

### Empreintes SHA-256 recalculées par script (`sha256sum`, 16:08 UTC)

| Fichier | Empreinte |
|---|---|
| `…/collisionneur-boucle-moisson-v1/consigne-erratum-synthese-boucle-moisson-v1.md` | `c5c75d580b9403260db1121dddfb2ac09bf30be152b87a13c5b7242f5a3171be` |
| `…/collisionneur-boucle-moisson-v1/synthese-boucle-moisson-v1.md` | `48a514de40b5baa95423e77e17e09a0be566312faa9e05f350296b03968bf856` |
| relecture d'Opus 5.5 `relecture-opus-synthese-boucle-moisson-v1.md` (espace de travail de la session) | `02aacbfe51271b96411455384397b0d2fe6681c5baeacf5d900b1e1900f45707` (conforme à l'abrégé attendu) |
| `…/collisionneur-boucle-moisson-v1/criteres-lecture-boucle-moisson-v1.md` | `3d0dc1051492fa9c66d2f0f12e8ff8a2df8b17b63444297195bd6e0f55147cc5` |
| `…/collisionneur-noeuds-v1/criteres-lecture-noeuds-v12-tour1-v1.md` | `22edbf4751c205f6760a136963bfaebcede773bfdc3300e923ad8e5df4e3a529` |
| `donnees/collisionneur-boucle-moisson-v1/question-collisionneur-boucle-moisson-fiches-v1.md` | `72b4f14980ce259b0f2836f7162bbfb33377227b0da05f511c19774c17d7ae76` |
| `donnees/collisionneur-boucle-moisson-v1/faits-boucle-moisson-v1.md` | `53f78bb2a9238ef834267519be3df4bbd413f8c07adb6c3da03dc4c135923c43` |
| `…/run-boucle-moisson-e3-v1/etat.md` | `e112201cfef616fef3ed541f532b4c4b16b3fa00cb52ffb3ee6672e9d8d8c833` |
| `…/cellules/E3-T1-conception-A.md` | `feff811deab88cd854f57ea435abec1d43cb61dab915ae2fec79f7c49444e19b` |
| `…/cellules/E3-T1-conception-B.md` | `fb7e8f31afe8287c752019dc9ac0d729c712822cd39f5385c641adf2454255f0` |
| `…/cellules/E3-T1-conception-C.md` | `7b3fe61dcad0800332f21798fa763dd7ec0ddab5e7733ecd0748e2ba0f6146b8` |
| `…/cellules/E3-T1-conception-D.md` | `20c9d45b4b4f15e0f2cd6ed5f79e0c4f3bdae2ca070d4186e3de295a292b499e` |
| `…/cellules/E3-T2-critique-croisee-A.md` | `fb2ac27815655a7fc6c08a4773e6f9638184d61943ed1d3181209f495b905488` |
| `…/cellules/E3-T2-critique-croisee-B.md` | `50810f5b46ed5f266880dea47a509210bc73b92aabdbe08a7f7308f2bdc407e4` |
| `…/cellules/E3-T2-critique-croisee-C.md` | `04bfdc7609704ba6cc11cc811ec2a0752166d5356be4512a37cf75496c898454` |
| `…/cellules/E3-T2-critique-croisee-D.md` | `dea4739f40f5a92cd7dcf0775722337e5f1c9ca77ad450c8dd5a4b32c8206a34` |
| `…/cellules/E3-T3-reponse-A.md` | `44353590d8cf3670f454a484f02e61b1ae1e479e3ee051fdb137571623d51579` |
| `…/cellules/E3-T3-reponse-B.md` | `d53bc0235a501a2d6a0b0a25932538a105da3cec5b0ed176ec83de5d3305f7eb` |
| `…/cellules/E3-T3-reponse-C.md` | `6b9fdf0e3cab2d8db34b39dff7b5e11f3b6b4861ae2c4f3ade20e587594ca154` |
| `…/cellules/E3-T3-reponse-D.md` | `3dde251cbdcf2666a55803a60e1776549bd8efc453d3079b987cfcb07c3fde4d` |

Toutes identiques à celles de la table de la synthèse v1 et de la relecture. Conventions de renvoi : celles de la v1 (`A-T1 (b) E3`, `C-T3 (c) 3`, `faits l. N`) ; « RA » = allocation de ressources ; « RB-nn » = constat de la relecture d'Opus.

## Règles de comptage écrites avant tout recompte

- **R-a. Accord indépendant** (critère 7 des nœuds, critères 2 et 11 de la boucle) : même position tenue **en T1** par au moins deux espèces sur le même volet, avec au moins une raison commune ; « large » à trois ou quatre. **Jamais** ce que la question impose (ses parenthèses, ses options, l'objectif, la décision de Lazar) ni ce qu'une pièce servie énonce (critère 11 des nœuds : vrai par construction) ; une position reprise d'une pièce reçoit la réserve « soufflé par la pièce ». Une position acquise seulement en T3 n'est pas un accord : c'est une convergence. Une position « implicite » (base mécanique à battre, contrôle) est comptée avec la mention « implicite ».
- **R-b. Convergence née de la critique** (critère 8 des nœuds) : une position retirée par son auteur en T3, ou adoptée par une autre espèce en T2 ou T3, sous une critique ; **un objet compté une fois**, quel que soit le nombre d'espèces qui l'ont demandé. Le nombre de **critiques acceptées** par espèce est une autre grandeur, rapportée à part.
- **R-c. Divergence résolue** (critère 9 des nœuds) : deux espèces au moins ont tenu **dès T1** des positions opposées sur le même objet, et l'une cède en T3 en donnant la raison. Un retrait sous une critique née seulement en T2 est une convergence (R-b), pas une divergence résolue. Toute divergence résolue est aussi une convergence : les deux rubriques se recouvrent, ce que la v1 ne disait pas.
- **R-d. Divergence non résolue** : positions différentes en T3 ; chaque objet compté une fois (Q6-b est le même objet que Q3-b).
- **R-e. Apport d'une seule espèce** (critère 12 des nœuds) : option manquante, pire cas, témoin ou pièce proposés par une seule espèce, **d'origine propre** (la transformation en instrument d'une idée venue de la critique d'une autre espèce est un « repris », pas un apport seul), jamais repris ; gardé s'il n'est pas réfuté en T2, et s'il l'est, compté avec la mention.
- **R-f. Vrai par construction** : énoncé présent dans le texte de la question (parenthèses de Q1 et de Q5, options de Q7, objectif « validées par l'expérience (tests de mort, pôle) », décision de Lazar de la pièce 3) ou dans une pièce servie (aucun poids, vocabulaire de physique, RA bat la marche de Swanson, voie R-a avant R-b, l. 749-750).

## 1. Verdicts, constat par constat (ordre de la relecture)

| Constat | Ce que dit la v1 (citation, ligne) | Ce que disent les cellules ou les faits | Verdict et raison | Correction (texte exact : section 5, C-nn) |
|---|---|---|---|---|
| **RB-01** Décompte des accords : « 7 larges » annoncés, huit énumérés ; Q3 et Q4 comptés deux fois ; règle de sélection non écrite | l. 47 : « 11 \| **7 larges** : Q1 état minimal… ; Q1 « affiner »… ; Q2… ; Q3… ; Q4… ; Q5… ; Q5… ; Q7… » (huit items) ; l. 75 : « Large à quatre en T1 : état minimal en champs fermés, et sans capteur « affiner » = « reformuler » » (un seul accord) ; l. 119 : « Large (C, D en T1 ; A, B en T3) » ; l. 121 : « A cède à C et D (… A-T3 15) » ; l. 142 : « Large (A, C, D ; B silencieuse) » ; l. 144 : « D cède à A et C sur la récompense (D-T3 7) » | Q3 en T1 : C-T1 Q3 (« interdire… séparer les quotas ») et D-T1 (a) (« rapporter rappel… pour chaque type de paire ») seulement ; A-T1 E5 classe « fiche–article et article–article » dans une même précision à k ; A-T3 15 : « les paires fiche–fiche et fiche–article sortent d'E5 » ; B-T1 P3 et B-T3 Exp. 3 corrigée restent fiche–article seule, sans énoncé de séparation. Q4 en T1 : C-T1 Q4 explicite ; A-T1 (c) : « Allocation uniforme avec arrêt par budget » comme base à battre (implicite) ; D-T1 E4 propose le duel sans défaut ; D-T3 E4 : « L'uniforme avec arrêt demeure l'option par défaut » (après D-T3 7) ; B-T1 P5 muette | **Confirmé.** Huit items pour « 7 » ; Q1 compte deux énoncés dont un vrai par construction (RB-06) ; Q3 et Q4 ne sont pas des accords de T1 à plus de deux : A-T3 15 et D-T3 E4 sont des convergences, comptées deux fois. La règle qui retenait onze items n'est pas écrite. Recompte sous R-a : 16 (section 2) | C-03, C-10, C-14, C-17, C-18 |
| **RB-02** « 27 convergences » non reproductible | l. 48 : « 27 \| A cède 15 fois sur 19 … B accepte 17 sur 17 … C 11 sur 12 … D 12 sur 12 » ; paragraphes « Convergences nées de la critique » l. 77, 100, 121, 144, 163, 205 | Objets nommés dans les volets : Q1 8, Q2 7, Q3 8, Q4 3, Q5 5, Q6 0, Q7 2 = 33, tous retrouvés dans les cellules T3 citées (section 2). Critiques acceptées : A-T3 19 lignes, rejets partiels aux lignes 4, 6, 13, 14 (15 sur 19 exact) ; B-T3 : 23 entrées (A.1-A.9, C.1-C.6, D.1-D.8), dont 4 renvois (C.5, D.2, D.3, D.6) et 3 « en partie » (A.1, A.6, D.4), non « 17 sur 17 (2 en partie) » ; C-T3 : 12 points, 1 rejet partiel (7) exact ; D-T3 : 12 points, 2 réserves (3, 7) exact | **Confirmé.** Ni 33 (objets) ni 55 (critiques) ne donnent 27 ; le chiffre de B est aussi inexact | C-04 |
| **RB-03** « 9 résolues » : trois seulement listées | l. 49 : « 9 \| listées par volet » ; intitulés « Divergence résolue » l. 79 (Q1), 102 (Q2), 123 (Q3) | Sous R-c : Q3 mélange des types (A-T1 E5 contre C, D ; A-T3 15) ; Q4 récompense du bandit (D-T1 E4 contre A-T1 A10, C-T1 Q4 ; D-T3 7) ; Q5 poids ouverts comme garantie (C-T1 Q5 « garantit mathématiquement » contre D-T1 (a) « ne prouvent pas » ; C-T3 4) ; Q5 seuil absolu (B-T1 Exp. 4 contre A-T1 E5, D-T1 ; B-T3 A.6) ; faible : Q2 résumés (A hypothèse, C et D trouver/valider ; A-T3 ne conteste pas). Q1 garde lexicale et Q3 « ≥ 7/8 » : positions de C attaquées seulement en T2 (D-T2 sur C (a) ; A-T2 et B-T2 sur C (b) E3), retirées en T3 : convergences | **Confirmé.** Six des neuf ne sont nommées nulle part ; sous R-c le compte est 4 (+ 1 faible) | C-05 |
| **RB-04** Divergences maintenues : sept dans la liste, onze dans les volets ; Q3-c, Q4-b, Q5-b, Q7-b perdues ; coût de la reproduction de Gu et Krenn non relevé | l. 50 : « 7 » ; l. 125 (Q3-c), 146 (Q4-b), 165 (Q5-b), 203 (« Divergence mineure (Q7-b) ») ; liste l. 223-229 : sept items ; table Q6 l. 175 : A « ≈ 10-40 dollars illustratif » ; l. 178 : D « R-a (32 Go, 50 Go, « 100–600 € » illustratif) » | Q3-c : C-T1 Q3 (k = 2, N = 20 illustratifs), D-T1 (a) (pré-échantillon), A-T1 E6 (≈ 40 par puissance), B-T1 Exp. 3 (24, Wilson ± 20 points) : quatre bases, non « trois » (l. 125). Q4-b : C-T1 Q4 et C-T3 (c) 4 (refus) ; A-T1 (c), (e) et D-T3 E4 (synthétique d'abord). Q5-b : A-T3 E5a′, B-T3 Exp. 4 corrigée, C-T3 4, D-T3 E5. Q7-b : C-T1 Q7 et C-T3 (c) 4 ; B-T1 (d) et B-T3 (c) ; D-T1 « seulement après essai réel du relais et de la douane » et D-T3 (c). Coût : A-T1 (d) « E5 voie R-a ≈ 10–40 USD de machine louée » ; D-T1 (d) : « prévoir illustrativement 32 Go et 50 Go… La voie principale demande ≥ 64 Go… Fourchette illustrative : 100–600 € » — les 100-600 € sont la voie principale (R-b, faits l. 625-626), non R-a ; la table Q6 de la v1 les attribue à R-a ; B-T1 (d) : R-a ≈ 1–5 $, R-b ≈ 5–30 $ | **Confirmé** pour les quatre divergences perdues et pour « trois bases ». **Confirmé en partie** pour le coût : la divergence existe (quatre fourchettes, trois espèces), mais le « facteur dix côte à côte » tient à une erreur d'attribution de la table Q6 (D : voie principale, pas R-a) ; les chiffres portent sur des voies et des machines différentes | C-06, C-16, C-19, C-22, C-26, C-28 |
| **RB-05** « 12 apports seuls (A 4, B 2, C 4, D 2) » non reproductible | l. 51 ; paragraphes « Apports » l. 83, 104, 127, 148, 167, 186 | Marqués « seule » d'origine propre (R-e) : A : boucle existante (A-T1 A12), bras hasard (A-T1 E6), blocs couverts (A-T1 (c)), trois fuites (A-T1 A11), E4′ (A-T3), « garder RA » (A-T1 E5, A-T3 E5b′) = 6 ; B : entropie (B-T1 Exp. 5, réfutée en T2 par A, C, D, corrigée B-T3) = 1 ; C : filtre de réfutation (C-T1 Q1), deux détentes (C-T1 Q2), interdiction et quotas (C-T1 Q3), recherche à un coup (C-T1 Q5), liste fichier par fichier (C-T1 Q6) = 5 ; D : récompense rétrodictive (D-T1 (a)), issue future (D-T1 (a)), refus du nombre d'expert (D-T1 (a)), criblage puis bandit (D-T1 E4), préalables (D-T1 « Réutilisation ») = 5. Hors compte : m4 (de C-T2 sur A (c) 2), paires incompatibles (de D-T2 sur A (c) 4), anti-plagiat (de B-T2 sur C (c) 3), Goodhart (repris par D), Gu-Krenn témoin sur sa tâche (rejoint par A-T3 14). Aucun second apport de B n'est trouvable | **Confirmé.** 17 sous R-e (A 6, B 1, C 5, D 5) ; B surcompté, A et D sous-comptés ; sens du biais sans faveur à A, comme le dit la relecture | C-07 |
| **RB-06** Accords vrais par construction ou soufflés : Q1 « affiner = reformuler » ; Q1 champs fermés ; Q5 circularité ; Q5 témoin RA « à quatre » | l. 47 ; l. 75 ; l. 161 : « À quatre : rétrodiction … circulaire (réserve R4 ; en partie vrai par construction…). À quatre : RA manque aux trois témoins » | Question Q1 : « (sans quoi « affiner » veut dire « reformuler ») » ; demande (b) : « objet versionné (affirmation, mécanisme, pièces, trous) » ; Q5 : « Quelle fuite rend le test circulaire (modèles entraînés après la coupure) et comment la fermer ? ». A-T1 A1, B-T1 P2, C-T1 (a) 1, D-T1 (a) 1 reprennent la parenthèse comme HYPOTHÈSE. RA : A-T1 A5 (« RA, Adamic-Adar, attachement préférentiel »), C-T1 Q5 (« RA : obligatoire »), D-T1 E5 (« allocation de ressources » parmi les témoins) ; B-T1 Exp. 4 emploie RA comme méthode du terrain, jamais comme témoin manquant de la boucle ; pièce 2 (faits l. 15 de la question ; A-T1 A5 : −0,82) | **Confirmé** sur les quatre points : « affiner = reformuler » et la circularité sont le texte de la question (R-f) ; « champs fermés » est soufflé sur le principe, propre sur le détail ; RA est à trois, soufflé par la pièce 2 | C-03, C-10, C-20 |
| **RB-07** Q6 : accord « à quatre » contredit par C ; A mal rangée dans la liste du tour 2 | l. 180 : « À quatre (vrai par construction : pièce 3) : aucun poids, vocabulaire de physique, « tel quel » possible seulement dans leur domaine (R-a) » ; l. 47 : « à deux (A, D) » ; l. 223 : « « tel quel » (C) ou « recoder un substitut » (A, B, D) » | C-T1 Q6 : « `create_concepts/` … à relancer telle quelle sur le corpus arXiv/OpenAlex de contrôle de l'IA » ; C-T3 (c) 3, point 2 : « Exécuter tel quel (décision de Lazar du 1er novembre) le script `create_concepts/` … strictement avant coupure ». A-T1 (d) : « sa chaîne de concepts … relançable sur `cs.LG, …` = tester leur **méthode**, pas leur modèle » ; A-T3 E5b′ : « la relance de leur chaîne sur `cs.LG…` (leur méthode, pas leur modèle) vaut un devis » (si le réseau bat RA). B-T1 P7 : « seule la méthode est transférable, ce qui revient à « recoder » » ; D-T1 : « assumer explicitement le codage d'un substitut ». Faits l. 738-742 : « relancer leur chaîne … on testerait alors leur méthode, pas leur modèle » | **Confirmé.** Le « à quatre » est faux pour C ; décompte et volet se contredisent (à deux, à quatre) ; sur l'action, A relance leur chaîne comme C (sous condition d'E5b′), B et D codent ; sur le mot, C seule dit « tel quel » | C-23, C-25, C-27 |
| **RB-08** Q2 « dérivation mécanique à quatre » soutenue pour C et D seulement | l. 98 : « Large à quatre : dérivation mécanique (champs fermés, jamais texte libre) et garde mécanique » | C-T1 Q2 : « Aucune requête en texte libre écrite par le proposeur. Le noyau extrait mécaniquement… » ; D-T1 (a) : « dérivées mécaniquement de champs autorisés » ; A-T1 (c) : « requêtes dérivées des concepts, antériorités, trous », base à battre « titre verbatim » ; A-T3 11 : « Requête dérivée de la fiche amputée » — jamais dit par quoi ; B-T1 Exp. 1 : « requête dérivée des concepts et trous nommés » — idem. Garde : A-T1 (c) (grep), B-T1 c4 (regex), C-T1 Q2, D-T1 (a) : quatre | **Confirmé.** Garde à quatre ; dérivation mécanique à deux, inférée pour A et B | C-03, C-13 |
| **RB-09** Fuite de recommandations par les faits plus large (quotas l. 104 ; R-635 l. 168) | l. 60 : « Recommandation d'auteur citée \| 1 \| C-T1 (b) E3 : bande [2 ; 4]… » ; l. 54 : A « quotas décidés » comptée inexactitude d'état | Faits l. 104 : « Quotas recommandés : 1 tour, 4 requêtes, 5 résultats ([Dbr] R-442) » ; l. 168 : « Condition de reproduction préalable : relâchée (recommandation R-635) ». Usages : A-T1 A2 « Quotas décidés » ; B-T1 (d) « 20 fiches × 4 requêtes × 5 résultats » ; C-T1 (c) 1 « top-20 (4 × 5 résultats, quota R-442, VÉRIFIÉ) » ; D aucun. R-635 : A-T1 A3 « reproduction préalable relâchée, renvoyée au collisionneur » ; B-T1 P7 « renvoie au collisionneur (D-j, nœud N3) » ; C, D aucun | **Confirmé.** Deux recommandations servies, reprises comme chiffre ou comme état par A, B, C (quotas) et A, B (R-635) ; défaut de la question et de l'assemblage, non de la synthèse | C-09 |
| **RB-10** Pièces non servies (§ 4 et § 11 du dossier) qui pèsent sur Q7 | l. 10 et critères l. 13-14 : pièce 1 = § 1, 2, 3, 7, 9, 10 | Les faits servis ne contiennent ni § 4 ni § 11 (table des pièces, critères l. 13-14 ; faits l. 3) ; le contenu de ces sections (porte du pré-pilote, échéances) n'est pas vérifiable ici | **Confirmé sur l'absence, non tranchable sur le fond** (dossier non servi) ; mineur pour la synthèse, à servir au tour 2 | aucune |
| **RB-11** « α = 0,05 par hypothèse » à requalifier ; renvois « D-T1 » sans section | l. 53 : « la l. 26 dit « 5 % de fausses promotions garanties » sans unité » ; l. 83 : « (D-T1) » | Faits l. 26 : « un juge figé statistique … avec 5 % de fausses promotions garanties », aucune unité ; C-T2 sur D (a) 3 : « α = 0,05 par hypothèse testée, pièce 1, § 1.1, **VÉRIFIÉ** » ; D-T3 11 : « Les faits servis ne précisent pas assez l'unité exacte du contrôle existant ». Le § 6 du dossier n'est pas servi. Citation de D : D-T1 (a), sous-section « État minimal d'un embryon et arrêt », paragraphe « Arrêt illustratif », dernière phrase, exacte | **Non tranchable** sur la requalification (elle repose sur une section non servie) ; par le critère 3 de la boucle, une unité absente de la ligne citée reste « inexacte sur les pièces » ; le « VÉRIFIÉ » n'est pas soutenu, ce que la v2 dit. **Confirmé** pour la section manquante | C-08, C-12 |
| **RB-12** Réserve de famille ; B servie en Opus 4.6 (prévu ou repli ?) | l. 5 ; l. 8 | `etat.md` : `claude-opus-4-6` pour les trois cellules de B ; critères du tour 1 des nœuds l. 6-7 : « B Opus 4.6 » comme espèce ; devis du collisionneur de la boucle l. 11 (motif cherché seulement) : « quatre espèces (Fable 5.1, Opus 4.6, Argon, Kimi K3.1 Pro) » ; faits l. 55 : « Collisionneur \| Fable 5.1, Opus 5.5, Argon, Kimi ». Aucune faveur à A trouvée : les deux inexactitudes d'état de A (l. 54) sont exactes sur les faits l. 104 et l. 167 | **Confirmé** : Opus 4.6 était le modèle prévu, non un repli ; la pièce 1 est en retard sur le run. Observation de famille : sans contre-exemple | C-02 |
| **RB-13** Recommandations glissées (5) | (1) l. 5 ; (2) l. 246 ; (3) l. 182 et l. 223 « décide ce que la décision de Lazar autorise sans nœud » ; (4) l. 125 « Les objets diffèrent…, aucune ne le dit » ; (5) l. 233 « question inverse » | Textes présents tels que cités. (4) : C-T1 Q3 parle de la course, D-T3 E3 d'un banc ; aucune des deux ne traite l'usage de l'autre — la phrase de la v1 commence une réconciliation. (5) est formulé comme une question (R4) | **Confirmé** pour (1) à (4) ; (5) **confirmé comme question admissible**, gardé | C-01, C-29, C-25, C-27, C-15 ; (5) aucune |
| **RB-14** Ce qui tient : recalculs et chiffres du dossier | l. 85, 129, 244 ; l. 106 | Refaits par script : 0,276 et 1,178 bit ; 0,134 et 0,624 ; 0,109 ; 8 128, 2,53 × 10⁷, 1,95 × 10¹⁰ ; π = 0,0208 et 0,982 ; k = 5 141 ; 0,102 et Φ(−0,67) = 0,251 ; 0,200 ; 3 953,6 et 0,395 ; 0,114 ; somme d'`etat.md` 12,61 : tous exacts. Faits l. 104, 108, 109, 174, 209, 228 : tels que cités | **Confirmé** | aucune |

### 1 bis. La table « positions T3 résumées par le relayeur », ligne à ligne

| Ligne | Ce que dit la relecture | Cellules | Verdict |
|---|---|---|---|
| Q1 | C « le plus faible : aveugle oui, dégradés seulement par sa calibration à paraphrases » | C-T3 1 : lecteur neuf aveugle au tour « avec contrôle négatif : résumés contenant les mots-clés sans répondre au trou » ; C-T3 E2 corrigée, issue primaire 1 : « y glisser 8 versions artificiellement dégradées où la référence ajoutée est hors sujet » | **Infirmé** : C a des cas dégradés en T3 |
| Q2 | garde à quatre, dérivation C et D | voir RB-08 | **Confirmé** |
| Q3 | séparer : C, D en T1, A en T3, B par critique ; puissance : A et D ; B déclare 0,25 ; C illustratifs | A-T3 15 ; B-T2 sur D (c) 2 ; B-T3 Exp. 3 corrigée « puissance ≈ 0,25 » ; C-T1 Q3 « illustratif » | **Confirmé** |
| Q4 | C en T1, D en T3, A implicite, B silencieuse ; à contre-énoncé | voir RB-01 | **Confirmé** |
| Q5 | prospective chez A, C, D ; B non montrée | A-T1 (e), A-T3 (c) ; C-T1 Q5, C-T3 4 ; D-T1 E5, D-T3 E2b ; B-T1 et B-T3 : rien de prospectif | **Confirmé** |
| Q6 | le « à quatre » contredit par C ; partie factuelle = pièce 3 | voir RB-07 | **Confirmé** |
| Q7 | quatre en T1 ; effet d'énoncé | A-T1 (e) ; B-T1 (d) ; C-T1 Q7 ; D-T1 « Ordre proposé » ; question Q7 | **Confirmé** |
| Apport de A | « ajoute la moisson comme nœud » imprécis : le nœud existe déjà (codé v47, jamais servi) | Faits l. 105 : « tour de moisson court entre passe 1 et passe 2 » ; l. 108 : « CODÉ dans l'orchestrateur v47 … option `--moisson` par défaut « aucune » » ; l. 109 : jamais servi ; question (a) : moisson ciblée déclenchée par tout embryon | **Confirmé** (imprécision de A, rapportée telle quelle par la v1) |
| Apport de D | cité « D-T1 » sans section ; presque vrai par construction ; rangé en Q1, porte sur Q4 et Q5 | Section trouvée (RB-11) ; la question n'énonce pas cet interdit ; D le place dans « État minimal d'un embryon et arrêt » | **Confirmé** pour la section et le rangement ; **non tranchable** pour « presque vrai par construction » : la question ne le dit pas, c'est une règle de conception de D, voisine de C-T1 Q4 et A-T1 A10 |

### 1 ter. Les sept « points qui exigent les cellules »

| Point | Réponse sur les cellules |
|---|---|
| 1. Recompter avec la règle écrite | Section 2 ci-dessous |
| 2. B en Q5 nomme-t-elle RA comme témoin manquant ? B en Q3 (T3) sépare-t-elle les types ? | Non : B-T1 Exp. 4 emploie RA comme méthode de base du terrain, B-T3 Exp. 4 corrigée idem ; aucun « témoin manquant » chez B. Non : B-T3 Exp. 3 corrigée reste fiche–article, témoin apparié sur l'axe ; la seule trace est B-T2 sur D (c) 2 (calibration entre types), une critique |
| 3. A et B en Q2 : dérivation mécanique ou par modèle ? | Non dit, ni en T1 ni en T3 (RB-08) |
| 4. Citations exactes avec section | D-T1 (a), « État minimal d'un embryon et arrêt », paragraphe « Arrêt illustratif », dernière phrase : « Le gain rétrodictif post-coupure ne doit jamais servir de récompense interne : ce serait une fuite. » A-T1 (a), lignes A11 et A12 de la table des présupposés. C-T3 (c) § 3, point 2 : « Exécuter tel quel (décision de Lazar du 1er novembre) le script `create_concepts/` (RAKE) et le calcul des traits du dépôt cloné `Impact4Cast` strictement avant coupure » |
| 5. Modèle servi pour B ; 12,61 dollars | `etat.md` : `claude-opus-4-6` ×3, prévu (RB-12) ; somme des douze lignes = 12,61 (script) |
| 6. Pièce 3 : ressources et coût de la reproduction | Faits l. 582-583 : banc d'essai sur processeur, mémoire < 15 Go, ≈ 1 h par tâche ; l. 625-626 : R-b, machine ≥ 64 Go ; l. 632 : machine louée nécessaire pour R-b, probablement pour R-a ; l. 771 : devis à écrire. A (10-40 $) parle de R-a ; D (100-600 €) de la voie principale ; B donne les deux (1-5 $ ; 5-30 $) : pas la même voie (RB-04) |
| 7. Usages des deux recommandations servies | RB-09 : quotas repris par A, B, C ; R-635 par A, B |

## 2. Recomptes nominatifs sur les cellules

### 2.1 Accords indépendants (règle R-a) : 16

**Larges (8).**
1. Q1 état minimal en champs fermés mesurables : A-T1 A1, A4, E2 (triplet, « champs fermés ») ; B-T1 Exp. 2 (Δ par champ) ; C-T1 Q1 (quadruplet) ; D-T1 (a) (objet gelé). Quatre. Réserve : le principe d'un objet versionné est la demande (b) ; propre aux espèces : identifiants, valeur chiffrée, trous fermés.
2. Q2 garde mécanique de fuite : A-T1 (c) ; B-T1 c4 ; C-T1 Q2 ; D-T1 (a). Quatre. Réserve : garde existante (l. 105).
3. Q5 fermeture par rétrodiction sans modèle de langage : B-T1 Exp. 4 (« jamais un modèle de langage ») ; C-T1 Q5 (« purement algorithmique ») ; D-T1 E5 (« modèle à corpus daté auditable, ou proposeur mécanique »). Trois ; A en T3 (E5a′). Propre aux espèces (la question demande « comment la fermer »).
4. Q5 témoin RA manquant : A-T1 A5 ; C-T1 Q5 ; D-T1 E5. Trois ; B non. Réserve : soufflé par la pièce 2.
5. Q6 RA reprise comme base : A-T1 (d) ; C-T1 Q6 ; D-T1 « Swanson ». Trois. Même substance que 4 ; réserve pièce 2.
6. Q6 « tel quel » seulement dans leur domaine : A-T1 (d) ; B-T1 P7 ; D-T1 « Gu et Krenn ». Trois ; C dissent (Q6-a). Réserve : faits l. 740-742.
7. Q7 course 2 d'abord, boucle en génération 2 sous portes : A-T1 (e) ; B-T1 (d) ; C-T1 Q7 ; D-T1 « Ordre proposé ». Quatre. Réserve : effet d'énoncé.
8. Q7 activer les tests de mort avant la boucle : B-T1 (d) ; C-T1 Q7 ; D-T1 « priorité expérimentale » ; A-T1 (e) en option manquante. Trois (quatre avec A). Réserve : objectif de la question.

**À deux (8).**
9. Q2 dérivation mécanique des requêtes : C-T1 Q2 ; D-T1 (a).
10. Q2 résumés : trouver oui, valider non : C-T1 Q2 ; D-T1 (a).
11. Q3 séparer les types de paires : C-T1 Q3 ; D-T1 (a).
12. Q3 noyade sans stratification : C-T1 (a) 3 ; D-T1 (a).
13. Q3 nombres par puissance, non par prix ni « expert » : A-T1 E6 ; D-T1 (a).
14. Q4 uniforme avec arrêt par défaut : C-T1 Q4 ; A-T1 (c), implicite (base à battre).
15. Q4 bandit éprouvé en synthétique : A-T1 (c), (e) ; D-T1 E4 (monde synthétique comme contrôle ; « parasites » en D-T3 7 seulement).
16. Q6 R-a d'abord, R-b ensuite : A-T1 (d) ; D-T1 « Gu et Krenn ». Réserve : faits l. 749-750.

**Vrais par construction, hors compte (R-f).** Q1 sans capteur « affiner » = « reformuler » ; Q5 circularité de la rétrodiction générative ; Q6 aucun poids, vocabulaire de physique ; Q6 les huit autres systèmes « à vérifier » (absence de pièce 5 : question, pas accord, R8).

### 2.2 Convergences nées de la critique (règle R-b) : 33

Q1 (8) : A → longueur (A-T3 1) ; A → tautologie du diff (A-T3 3) ; A → double usage des 28 fonds (A-T3 4) ; B → métrique monotone (B-T3 A.4, C.1) ; B → entropie (B-T3 A.7, C.3) ; C → garde numérique et lexicale (C-T3 1) ; C → fuite des 28 fonds (C-T3 2) ; D → circularité du schéma et planteur (D-T3 1-2).
Q2 (7) : B → témoin « antériorités citées » (B-T3 A.1) ; B → lecteur confondu (A.2) ; B → c1 réécrit (A.3) ; C → liste blanche en liste noire (C-T3 3) ; A → oracle amputé (A-T3 11) ; D → douane par date (D-T3 12) ; D → volume égal (D-T3 4).
Q3 (8) : A → paires avec fiche hors rétrodiction (A-T3 15) ; A → E6 retirée de toute lecture (A-T3 17) ; B → vivier avec résumés (B-T3 A.5) ; B → ablation « article seul » (C.6) ; C → préfiltre RA retiré (C-T3 11) ; C → « ≥ 7/8 » retiré, vivier égal (C-T3 12) ; D → calibration entre types (D-T3 6) ; D → témoin maximal gelé (D-T3 5).
Q4 (3) : D → récompense « transition » retirée (D-T3 7) ; D → éligibilité conditionnée retirée (D-T3 8) ; D → permutations multiples, unité = la course (D-T3 9).
Q5 (5) : C → noms de modèles et anonymisation retirés (C-T3 4) ; B → seuil relatif et appariement (B-T3 A.6) ; A → E7 refondue (A-T3 19) ; D → E2 scindée (D-T3 3) ; C → graines, placebo, essai de non-fuite (C-T3 6).
Q6 (0). Q7 (2) : C → Porte 0 (C-T3 10) ; D → E0 préalable (D-T3 10).

### 2.3 Divergences résolues (règle R-c) : 4, plus 1 faible

1. Q3 mélange des types de paires dans un classement : A-T1 E5 contre C-T1 Q3 et D-T1 (a) ; A cède (A-T3 15, « correction de fond »).
2. Q4 récompense observable pour un bandit : D-T1 E4 contre A-T1 A10 et C-T1 Q4 ; D cède (D-T3 7, retire la récompense « transition »).
3. Q5 modèle à poids ouverts comme garantie de non-contamination : C-T1 Q5 (« garantit mathématiquement ») contre D-T1 (a) (« ne prouvent pas ») ; C cède (C-T3 4) ; A maintient (A-T3 E7′) : reste Q5-a entre A et D.
4. Q5 seuil absolu contre seuil relatif au taux de base : B-T1 Exp. 4 contre A-T1 E5 et D-T1 (a) ; B cède (B-T3 A.6).
5. (faible) Q2 « résumés suffisent-ils ? » : A-T1 E3 en hypothèse, C-T1 Q2 et D-T1 (a) trouver/valider ; A-T3 ne conteste pas, sans le dire.

Les deux autres « résolues » nommées par la v1 — Q1 garde lexicale de C (C-T3 1, sous D-T2 sur C (a) et A-T2 sur C (a) Q1) et Q3 « ≥ 7/8 » (C-T3 12, sous A-T2 et B-T2 sur C (b) E3) — sont des retraits sous critique de T2 : convergences.

### 2.4 Divergences non résolues : la liste complète du tour 2 (12)

1. Q6-a « reprendre tel quel », deux axes (RB-07). 2. Q3-b / Q6-b volume de la moisson complémentaire (B-T2 sur C (a) 4 ; C-T3 7 ; B sans réponse). 3. Q5-a poids ouverts datés (A-T3 E7′ ; D-T1, D-T2 sur A (a) E7 ; C retiré ; B contourné). 4. Q7-a première expérience (A-T3 (c) ; B-T3 (c) ; C-T3 (c) 3 ; D-T3 (c)). 5. Q3-a article–article (C-T1 Q3, C-T3 (c) 4 ; D-T3 E3 ; A-T3 15). 6. Q1-a qui juge le progrès (A-T3 E1′ ; B-T3 Exp. 2 corrigée ; C-T3 1 ; D-T3 E1). 7. Q4-a anticorrélation (A-T2 sur D (a) E4 ; C-T2 sur D (a) 2 ; D-T3 7). **Rétablies :** 8. Q3-c nombres de paires, quatre bases (C-T1 Q3 ; D-T1 (a) ; A-T1 E6 ; B-T1 Exp. 3). 9. Q4-b le bandit lui-même (C-T1 Q4, C-T3 (c) 4 ; A-T1 (c), (e) ; D-T3 E4). 10. Q5-b ce que mesure la rétrodiction (A-T3 E5a′ ; B-T3 Exp. 4 corrigée ; C-T3 4 ; D-T3 E5). 11. Q7-b passe de moisson en génération 1 (C-T1 Q7 ; B-T1 (d) ; D-T1). **Ajoutée, non relevée par la v1 :** 12. Q6 coût de la reproduction de Gu et Krenn (A-T1 (d) ; B-T1 (d) ; D-T1 (d) ; faits l. 582-583, 625-626).

### 2.5 Apports d'une seule espèce (règle R-e) : 17

Voir RB-05 : A 6, B 1, C 5, D 5, avec cellules ; liste reprise dans la section « Pistes » de la v2.

## 3. Ce que l'erratum ne change pas

Les tables par volet (positions, raisons, pires cas, pièces), les recalculs, les inexactitudes sur les pièces et sur l'état, les RAPPORTÉ sans source, les liens avec la non-convergence, les accords trop propres (dont la « question inverse », gardée comme question) : inchangés. Aucune espèce n'est classée ; aucune recommandation.

## 4. Ce que je n'ai pas pu faire

- Vérifier le contenu des § 4, 6 et 11 du dossier factuel (non servis) : RB-10 et la requalification de RB-11 restent non tranchables sur le fond.
- Vérifier sur PDF les ressources réelles de la reproduction de Gu et Krenn (seuls les faits servis, l. 582-632, ont été lus).
- Lire `journal.jsonl` du run (non listé par la consigne) : le caractère « prévu » d'Opus 4.6 repose sur `etat.md`, les critères des nœuds et un motif cherché dans le devis.
- Le nombre de mots de la v2 est mesuré par `wc -w` et par découpage Python (les deux sont rapportés) ; la consigne ne fixe pas la mesure.

## 5. Corrections appliquées à la v2 (texte exact ; original cité puis remplacement ; appliquées par script, chaque original trouvé exactement une fois)

**C-01** (RB-13 (1))

- Original : je le dis d'emblée, et le tour 2 pourra confier la contre-lecture de cette synthèse à un autre modèle.
- Remplacement : je le dis d'emblée.

**C-02** (RB-12)

- Original : 12,61 dollars (somme recalculée des douze lignes : 12,61).
- Remplacement : 12,61 dollars (somme recalculée des douze lignes : 12,61). B servie en Opus 4.6, prévu (critères des nœuds l. 6-7), non un repli.

**C-03** (RB-01, RB-06, RB-07, RB-08)

- Original : | Accords indépendants (même position en T1, au moins deux espèces, raison commune) | 11 | **7 larges** : Q1 état minimal en champs fermés ; Q1 « affiner » sans capteur = reformuler ; Q2 dérivation et garde mécaniques ; Q3 séparer les types de paires ; Q4 uniforme avec arrêt par défaut ; Q5 rétrodiction générative avec modèles fermés circulaire ; Q5 témoin « allocation de ressources » manquant ; Q7 course 2 d'abord, boucle en génération 2. **3 à deux** : Q2 résumés suffisants pour trouver, pas pour valider (C, D) ; Q4 bandit à éprouver en monde synthétique avec parasites (A, D) ; Q6 Gu-Krenn tel quel seulement dans son domaine, voie R-a (A, D). |
- Remplacement : | Accords indépendants (même position en T1, au moins deux espèces, raison commune ; rien d'imposé par la question ou une pièce) | 16 | **8 larges** : Q1 champs fermés (A, B, C, D) ; Q2 garde de fuite (A, B, C, D) ; Q5 fermeture sans modèle de langage (B, C, D) ; Q5 témoin RA (A, C, D) ; Q6 RA comme base (A, C, D) ; Q6 « tel quel » seulement dans leur domaine (A, B, D) ; Q7 course 2 d'abord (A, B, C, D) ; Q7 tests de mort d'abord (B, C, D). **8 à deux** : Q2 dérivation mécanique (C, D) ; Q2 résumés trouver/valider (C, D) ; Q3 types de paires séparés (C, D) ; Q3 noyade (C, D) ; Q3 nombres par puissance (A, D) ; Q4 uniforme par défaut (C ; A implicite) ; Q4 bandit en synthétique (A, D) ; Q6 R-a puis R-b (A, D). Hors compte (vrais par construction) : Q1 « affiner » = « reformuler », Q5 circularité, Q6 pièce 3 ; détail : erratum § 2.1. |

**C-04** (RB-02)

- Original : | Convergences nées de la critique (critère 8) | 27 | A cède 15 fois sur 19 critiques (4 rejets partiels) ; B accepte 17 sur 17 (2 « en partie ») ; C 11 sur 12 (1 rejet partiel) ; D 12 sur 12 (2 réserves). Détail par volet. |
- Remplacement : | Convergences nées de la critique (critère 8 ; un objet compté une fois) | 33 | Q1 8 ; Q2 7 ; Q3 8 ; Q4 3 ; Q5 5 ; Q6 0 ; Q7 2 (critiques acceptées par espèce : erratum RB-02). |

**C-05** (RB-03)

- Original : | Divergences résolues en T3 | 9 | listées par volet. |
- Remplacement : | Divergences résolues en T3 (opposées dès T1, l'une cède en T3) | 4 (+ 1 faible) | Q3 mélange des types (A-T3 15) ; Q4 récompense du bandit (D-T3 7) ; Q5 poids ouverts comme garantie (C-T3 4) ; Q5 seuil absolu (B-T3 A.6) ; faible : Q2 résumés. |

**C-06** (RB-04)

- Original : | Divergences non résolues | 7 | § « Pour le tour 2 ». |
- Remplacement : | Divergences non résolues | 12 | § « Pour le tour 2 » (Q6-b = Q3-b ; coût de Gu-Krenn ajouté). |

**C-07** (RB-05)

- Original : | Apports d'une seule espèce, jamais repris | 12 | A : 4 ; B : 2 ; C : 4 ; D : 2 (marqués « une source »). |
- Remplacement : | Apports d'une seule espèce, jamais repris (origine propre) | 17 | A : 6 ; B : 1 ; C : 5 ; D : 5 (§ « Pistes » (ii) ; hors compte : m4, paires incompatibles, anti-plagiat). |

**C-08** (RB-11 (α))

- Original : la l. 26 dit « 5 % de fausses promotions garanties » sans unité (D-T3 §11 le relève). |
- Remplacement : la l. 26 dit « 5 % de fausses promotions garanties » sans unité (D-T3 §11 le relève) ; « VÉRIFIÉ » non soutenu ; unité ni confirmée ni contredite par les faits servis. |

**C-09** (RB-09)

- Original : réserve « non indépendant » sur ce point de C en Q3. |
- Remplacement : réserve « non indépendant » sur ce point de C en Q3. Aussi servies : quotas « recommandés » (l. 104), repris par A, B, C ; « recommandation R-635 » (l. 168), reprise par A, B. |

**C-10** (RB-06 (Q1))

- Original : **Accords.** Large à quatre en T1 : état minimal en champs fermés, et sans capteur « affiner » = « reformuler » (A A1-A4 ; B P2 ; C Q1 ; D).
- Remplacement : **Accords.** Large à quatre en T1 : état minimal en champs fermés (A A1-A4 ; B P2 ; C Q1 ; D (a)) ; principe soufflé par la demande (b). Hors compte : « affiner » = « reformuler » est la parenthèse de Q1.

**C-11** (RB-14 (apport de A))

- Original : « la demande ajoute la moisson comme nœud, pas la boucle » (A-T1 A12) — une source, jamais discutée.
- Remplacement : « la demande ajoute la moisson comme nœud, pas la boucle » (A-T1 A12) — une source, jamais discutée ; imprécis : le tour de moisson existe déjà (l. 105, 108).

**C-12** (RB-11, RB-14 (apport de D))

- Original : « le gain rétrodictif post-coupure ne doit jamais servir de récompense interne : ce serait une fuite » (D-T1).
- Remplacement : « le gain rétrodictif post-coupure ne doit jamais servir de récompense interne : ce serait une fuite » (D-T1 (a), « Arrêt illustratif » ; porte sur Q4 et Q5).

**C-13** (RB-08)

- Original : **Accords.** Large à quatre : dérivation mécanique (champs fermés, jamais texte libre) et garde mécanique ; aucune « on fera attention ».
- Remplacement : **Accords.** Large à quatre : garde mécanique ; aucune « on fera attention ». À deux (C, D) : dérivation mécanique ; A et B ne disent pas par quoi.

**C-14** (RB-01 (Q3))

- Original : **Accords.** Large (C, D en T1 ; A, B en T3) : ne jamais mélanger les types de paires dans un classement ; séparer quotas, scores ou évaluations.
- Remplacement : **Accords.** À deux en T1 (C, D) : ne jamais mélanger les types de paires dans un classement ; séparer quotas, scores ou évaluations ; A en T3 (A-T3 15, convergence) ; B ne l'énonce pas.

**C-15** (RB-13 (4))

- Original : Les objets diffèrent (classement en course chez C ; banc d'évaluation chez D), aucune ne le dit.
- Remplacement : C parle du classement en course, D d'un banc d'évaluation ; ni l'une ni l'autre ne traite l'usage de l'autre.

**C-16** (RB-04 (Q3-c))

- Original : trois bases différentes, aucune « d'expert ».
- Remplacement : quatre bases différentes, aucune « d'expert ». Maintenue.

**C-17** (RB-01 (Q4))

- Original : **Accords.** Large (A, C, D ; B silencieuse) : uniforme avec arrêt par défaut ; le bandit n'a pas de récompense observable (l. 209).
- Remplacement : **Accords.** À deux en T1 (C ; A implicite, A-T1 (c)) : uniforme avec arrêt par défaut ; le bandit n'a pas de récompense observable (l. 209). D en T3 seulement (E4). B silencieuse.

**C-18** (RB-01 (Q4, parasites))

- Original : À deux (A, D) : le bandit se juge d'abord en synthétique avec parasites ; C s'arrête au refus.
- Remplacement : À deux (A, D) : le bandit se juge d'abord en synthétique (« parasites » chez D en T3 seulement) ; C s'arrête au refus.

**C-19** (RB-04 (Q4-b))

- Original : (Q4-b) C refuse tout bandit avant récompense par calcul ; A et D le gardent comme hypothèse synthétique.
- Remplacement : (Q4-b) C refuse tout bandit avant récompense par calcul ; A et D le gardent comme hypothèse synthétique. Maintenue.

**C-20** (RB-06 (Q5))

- Original : **Accords.** À quatre : rétrodiction avec Kimi, Argon ou Opus entraînés après la coupure = circulaire (réserve R4 ; en partie vrai par construction, la question nomme la fuite). À quatre : RA manque aux trois témoins.
- Remplacement : **Accords.** Hors compte, vrai par construction : rétrodiction avec Kimi, Argon ou Opus = circulaire (Q5 le pose) ; apport propre : fermeture sans modèle de langage (B, C, D). À trois (A, C, D) : RA manque aux témoins ; B ne le dit pas ; pièce 2.

**C-22** (RB-04 (coût))

- Original : | R-a (32 Go, 50 Go, « 100–600 € » illustratif). Avec dépense. |
- Remplacement : | R-a : 32 Go, 50 Go ; voie principale R-b : « 100–600 € » (illustratifs, D-T1 (d)). Avec dépense. |

**C-23** (RB-07)

- Original : **Accords.** À quatre (vrai par construction : pièce 3) : aucun poids, vocabulaire de physique, « tel quel » possible seulement dans leur domaine (R-a).
- Remplacement : **Accords.** Vrai par construction, hors compte (pièce 3) : aucun poids, vocabulaire de physique. À trois (A, B, D) : « tel quel » seulement dans leur domaine (R-a) ; C dissent (Q6-a) ; pièce 3 l. 740-742.

**C-24** (RB-06 (pièce 3))

- Original : À deux (A, D) : R-a d'abord, R-b ensuite.
- Remplacement : À deux (A, D) : R-a d'abord, R-b ensuite (pièce 3 l. 749-750).

**C-25** (RB-07, RB-13 (3))

- Original : C : exécuter tel quel le code de `create_concepts/`, des traits et de l'entraînement sur notre corpus (C-T1 Q6 ; C-T3 (c) 3) ; B : « recoder » (P7) ; D : « assumer le codage d'un substitut » ; A : « leur méthode, pas leur modèle », le mot « tel quel » réservé à R-a sur leur graphe. Les faits portent les deux lectures (l. 738-742 : extension par relance de leur chaîne, « on testerait alors leur méthode, pas leur modèle »). Divergence de vocabulaire, mais elle décide ce que la décision de Lazar autorise sans nœud nouveau.
- Remplacement : Deux axes. L'action : relancer leur chaîne sur notre corpus — C (C-T1 Q6 ; C-T3 (c) 3) et A (A-T1 (d) ; A-T3 E5b′, sous condition) ; coder un substitut — B (P7), D. Le mot « tel quel » : C seule ; A le réserve à R-a. Les faits portent les deux lectures (l. 738-742). Touche la lecture de la décision de Lazar (l. 433).

**C-26** (RB-04 (Q7-b))

- Original : **Divergence mineure (Q7-b).** Passe de moisson v47 en génération 1 (C) contre moissonneur « aucune » (B) et « après essai réel du relais » (D) ; les faits disent seulement que le relais réel n'a jamais tourné (l. 109).
- Remplacement : **Divergence non résolue (Q7-b).** Passe de moisson v47 en génération 1 (C) contre moissonneur « aucune » (B) et « après essai réel du relais » (D) ; les faits disent seulement que le relais réel n'a jamais tourné (l. 109). Maintenue.

**C-27** (RB-07 (tour 2, 1))

- Original : 1. **Q6-a — « Reprendre tel quel » Gu-Krenn** : relancer leur code sur notre corpus est-il « tel quel » (C) ou « recoder un substitut » (A, B, D) ? Décide ce que la décision de Lazar autorise sans nœud.
- Remplacement : 1. **Q6-a — « Reprendre tel quel » Gu-Krenn**, deux axes : l'action, relancer leur chaîne sur notre corpus (C ; A sous condition) ou coder un substitut (B, D) ; le mot « tel quel » pour cette relance (C seule). Touche la lecture de la décision de Lazar (l. 433).

**C-28** (RB-04 (tour 2, 8-12))

- Original : 7. **Q4-a — Anticorrélation entre récompense « trou fermé » et nouveauté** : loi (A, C) ou risque (D).
- Remplacement : 7. **Q4-a — Anticorrélation entre récompense « trou fermé » et nouveauté** : loi (A, C) ou risque (D).
8. **Q3-c — Nombres de paires** : quatre bases (C, D, A, B).
9. **Q4-b — Le bandit lui-même** : refus (C) ; hypothèse synthétique (A, D).
10. **Q5-b — Ce que mesure la rétrodiction** : terrain (A, B) ; moteurs (C) ; métrique secondaire (D).
11. **Q7-b — Passe de moisson en génération 1** : oui (C) ; non (B) ; après essai du relais (D).
12. **Q6 — Coût de la reproduction de Gu et Krenn** : R-a 10-40 dollars (A), 1-5 (B) ; R-b 5-30 (B), « 100-600 € » (D) ; illustratifs, voies différentes.

**C-29** (RB-13 (2))

- Original : Pour A j'ai relevé deux inexactitudes d'état, trois RAPPORTÉ sans source et quatre rejets partiels en T3 ; une contre-lecture par un autre modèle serait la plus utile sur la table Q6 et sur l'accord Q7.
- Remplacement : Pour A j'ai relevé deux inexactitudes d'état, trois RAPPORTÉ sans source et quatre rejets partiels en T3.

**C-31** (titre)

- Original : (question v1 de conv-audit) — v1
- Remplacement : (question v1 de conv-audit) — v2 (erratum v1 appliqué)

**C-32** (table des empreintes)

- Original : | `…/cellules/E3-T3-reponse-D.md` | `3dde251cbdcf2666a55803a60e1776549bd8efc453d3079b987cfcb07c3fde4d` |
- Remplacement : | `…/cellules/E3-T3-reponse-D.md` | `3dde251cbdcf2666a55803a60e1776549bd8efc453d3079b987cfcb07c3fde4d` |
| `relecture-opus-synthese-boucle-moisson-v1.md` (Opus 5.5) | `02aacbfe51271b96411455384397b0d2fe6681c5baeacf5d900b1e1900f45707` |
| `consigne-erratum-synthese-boucle-moisson-v1.md` | `c5c75d580b9403260db1121dddfb2ac09bf30be152b87a13c5b7242f5a3171be` |
| `erratum-synthese-boucle-moisson-v1.md` | empreinte calculée par session-depot au scellement |

**Note de version** insérée après le titre :

> **Note de version (v2, 1er novembre 2026, lecteur neuf Fable 5.1).** Copie de la v1 (`48a514de…`, conservée), seuls remplacements de `erratum-synthese-boucle-moisson-v1.md`, appliqués par script (code de retour 0) : décompte recompté ; accords vrais par construction sortis ; Q2 scindé ; Q6-a sur deux axes ; tour 2 à douze ; recommandations retirées ; modèle de B ; section « Pistes ».

**Section nouvelle** insérée avant « Note de méthode du lecteur » (texte intégral dans la v2, § « Pistes générales consensuelles et pistes originales »).
