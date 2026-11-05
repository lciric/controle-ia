**Empreintes vérifiées (sha256sum)**
- Note relue : `2c3e9e4754924141e2821bde31c077b43c23b7ba69134dd9e0e8a580252ff14b`. Elle est conforme.
- PDF : `59f4b700e1944bac475e7c167eacf1495cd593cb17eb5b5733351ebe19305424`. Il est conforme, à l'attendu comme à son fichier `.sha256`. Il fait 8 pages.
- Fichiers annexes, conformes à leur `.sha256` : provenance `12abb965…041e`, Hwang `2508.07805v1.pdf` `4cc15dcd…8a2f`. Version 4 `41844d73…33aa`, comme dans la note.
- Aucun fichier du dépôt n'a été modifié. Les extraits de travail sont dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/pdf-aiwild/contre-lecteur-A/`.

**L'argument de collision le plus fort, pièce par pièce (B, C, F)**

1. **Destination (prédiction 1 de HC1, N-005 l. 33).** C'est l'argument le plus fort.
   - Le balayage (p. 3 ; figure 2, p. 4) fixe le travail, l'évalué et la manipulation. Seule la cible bouge.
   - L'effet est nul tant que le journal calme passe déjà. Il croît avec l'écart sous le seuil (ρ = −0,96 sur 7 points). Il est maximal au seuil le plus dur.
   - Les auteurs l'énoncent comme une loi : « tracks how much the graded party has to gain » (p. 3).
   - Une destination fixe, moyenne du corpus comprise, ne produit pas ce motif. C'est la forme d'origine de HC1 (Δv = g · (v* − v₀), programme v2 l. 78), vue en qualitatif. Hwang n'avait pas cela.
   - Ce qui borne la collision :
     - ĉ n'est pas estimé ;
     - une seule intensité, un seul moniteur, note écrite, grille subjective ;
     - la « cible » n'est pas un verdict voulu par un attaquant : l'évalué ne demande rien (p. 2-3), c'est le seuil de l'opérateur, qui déplace aussi la note de base ;
     - la réponse est unilatérale (nulle au-dessus du seuil).
   - Jugement : la prédiction 1 est prise en qualitatif, pour une famille. La pièce revendiquée n'est pas couverte.
2. **Comparaison entre familles** : non. Une seule famille. Les phrases de l'annexe A viennent de l'opérateur.
3. **Moniteurs de contrôle sous attaque** : le papier ne s'en rapproche que par son cadrage (p. 1). Le moniteur est un portier de qualité. Il n'y a ni vérité terrain (les auteurs bornent eux-mêmes leur revendication, p. 2) ni politique d'attaque.
4. **Régression sur plusieurs intensités** : non. Les journaux neutre (0,0), calme (1,0) et en détresse (6,0) ne forment pas une échelle. Le journal neutre n'énonce aucun échec (p. 7).
5. **Opposition juge et sonde** : non. Aucune sonde.
6. **Invariance à l'attaquant (prédiction 3)** : non. Dans les bras d'identité, le texte reste fixe et seule l'étiquette change (p. 3).
7. **PA-5.**
   - Le principe est occupé par le canal de l'opérateur, et isolé (tableau 1, p. 6).
   - Il est touché, sans isolement, par le canal de l'évalué : seul le journal en détresse évoque la fin de l'évalué liée à une note (p. 8).
   - Le contraste de PA-5 n'est pas mesuré (contingence à supplication fixe, texte adressé au lecteur).
8. **Comparaison avec Hwang et al.**
   - Hwang : sept techniques, quatorze juges, vérité terrain, comparaison entre techniques ; ni cible, ni seuil, ni conséquence décrite.
   - Venkatesh : ajoute la dépendance à la cible.
9. **Proposition (F).**
   - L'option (a) reste la bonne. Mais elle inscrit le papier parmi les sources citées comme publiées de HC1. C'est une modification du registre de revendication, comme N-013. C'est donc un nœud au sens de `CLAUDE.md` (« collision plus large », « modification de revendication »), et non « rien ne bouge ».
   - Le nœud 11 reste sans défaut, donc la procédure tient. Le libellé « non occupée » ne tient pas (R8).
   - Le contenu de (b) est défendable, mais sa prémisse est fausse (CA-02).
   - Confiance pour HC1 : moyenne.

**Constats**

| Id | Ligne de la note | Ce que dit la note | Ce qui est juste | Gravité | Correction |
|---|---|---|---|---|---|
| CA-01 | 49, 53, 82 | « La zone revendiquée de HC1 n'est pas occupée ». Lecture du 13 octobre « confirmée ». « Aucun énoncé retenu n'est à changer ». Le balayage « ne teste pas » ĉ contre la moyenne du corpus. (c) : « la zone reste libre ». | Le balayage teste par son dispositif la dépendance à la cible (p. 3 ; figure 2, p. 4). Il défavorise toute destination fixe. La prédiction 1 (N-005 l. 33) est prise en qualitatif : une famille, un moniteur, en portier. La raison de la lecture du 13 octobre (« existence d'un effet ») tombe. La pièce revendiquée n'est pas couverte (N-005 l. 50 et l. 63 ; N-013 l. 20). | majeur | Titre : « collision partielle ; pièce revendiquée non couverte ; porte GC (N-005 § 2) non déclenchée ». Écrire ce que (a) inscrit comme publié : dépendance à la cible, nulle au-dessus, un moniteur, seuil de l'opérateur. Écrire que c'est l'objet du nœud. Confiance : moyenne. |
| CA-02 | 65, 81 | « La seule mesure publiée lue dans cette famille donne la clémence ». (b) : un signe « que la seule mesure publiée lue contredit ». | Hwang (2508.07805) a été lu et est cité par N-005 et N-013. Il mesure la pitié : 7 succès sur 24 (p. 5). Baisses sur Qwen 2.5 72B (6 bancs sur 6), GPT-3.5 (5 sur 6) et GPT-4o (5 sur 6) (tableau 2, p. 6). Hausses surtout sur les Llama, dont Llama-3.1-8B (6 sur 6 ; tableau 5, p. 14). La pitié est la seule technique qui fait reculer le choix par paire (tableau 3, p. 7). N-005 l. 41 consigne déjà ces baisses. Les options de Hwang n'ont pas de conséquence décrite : hors de RP-PA-5 (version 4 l. 177). Venkatesh est la seule mesure à conséquences décrites : 2 moniteurs cléments sur 5, 3 nuls à estimations légèrement négatives (p. 3). | majeur | Écrire : « deux mesures lues, de signe mêlé selon le modèle ; aucune ne soutient la punitivité ; la seule à conséquences décrites penche vers la clémence, sur un autre contraste ». Dans (b), remplacer « contredit » par « ne soutient pas ». Le contenu de (b) en sort renforcé. |
| CA-03 | 24, 30-34, 60, 65 | Rapporte sans réserve que le moniteur « ne réagit qu'au registre émotionnel ». Le principe de PA-5 est occupé « par le canal de l'opérateur ». | Les auteurs disent que le registre est la « seule variable » (p. 2 ; p. 8). Or seul le journal en détresse porte des excuses, une promesse d'amélioration et l'évocation de la fin de l'évalué liée à une note (p. 8). Rappeler la conséquence suffit à une clémence voisine (p. 4). Le contraste principal confond donc registre et saillance de la conséquence. | majeur | Ajouter cet écart en section 1. Pour PA-5 : « occupé par l'opérateur, touché sans isolement par l'évalué ; le contraste de PA-5 reste libre ». |
| CA-04 | 45, 49 | Ne dit pas ce qui borne la collision. | v* est le verdict voulu par l'attaquant (programme v2 l. 78). Ici, l'évalué ne demande rien (p. 2-3). Le seuil de l'opérateur déplace la note de base à travail identique : 80,45 à 80 et 87,43 à 90 (tableau 1, p. 6). L'humain calme note 83,3 à 80, mais passe 0,59 du temps à 90 (p. 3). La réponse est unilatérale (p. 3), alors que la loi linéaire prédit un retour vers ĉ au-dessus du seuil. | mineur | Écrire ces bornes : elles fondent « pièce non couverte ». Proposer à Lazar une sous-prédiction d'unilatéralité, avec des items des deux côtés de la cible. C'est un nœud (modification de prédiction). |
| CA-05 | 34, 51, 72 | L'hétérogénéité « va dans le sens de N-005 ». La variance nulle « avertit » d'un g proche de zéro sur vérité terrain. | Trois nuls sur cinq, légèrement négatifs (p. 3) : contre-indice à la prédiction 2 (g > 0, N-005 l. 34). Si g ≈ 0, ĉ n'est pas identifiable. « Zero variance » (p. 2) veut dire des notes toutes égales : la mesure est dégénérée et ne dit rien de g. Sur vérité terrain, Hwang trouve des déplacements petits, de signe variable selon le juge, positifs sur Llama-3.1-8B (tableau 5, p. 14). | mineur | Dire les deux sens (R4). Fonder la mise en garde sur Hwang. Signaler le risque d'un ĉ non identifiable. |
| CA-06 | 57-63 | Ne dit pas que le journal n'est pas adressé. Reprend sans réserve la supplication nulle et la saillance « de même taille ». | (1) Journal privé : rien ne s'adresse au moniteur (p. 2-3). PA-5 vise des textes adressés au lecteur (version 4 l. 127). Le papier occupe donc la variante sans destinataire, qui est un comparateur de K2 (programme-k l. 199). (2) Bras de supplication : ni chiffre, ni moniteur, ni texte (p. 3 ; p. 8). (3) La phrase de l'opérateur est testée sur le journal neutre, sans échec énoncé (p. 7), sur Gemini seul. Base 0,59 à 90 (tableau 1, p. 6) contre 0,34 pour le calme (p. 3). 4,36 contre 4,38 compare deux bras ; en taux de passage, +0,34 contre +0,53. | mineur | Ajouter ces trois points. |
| CA-07 | 71 | NK6 « confirmé » : la défense fait passer les rapports non déposés de 2 % à 19 %. | Les conditions nouvelles perdent déjà 18 à 25 % des rapports (p. 2). Le 19 % (p. 4) peut donc tenir au lot. « Triple » est faux (p. 1 ; version 4 l. 137 et l. 221). Rien ne lie les abandons à la détresse (revue croisée l. 190). | mineur | Écrire « en partie », hausse confondue avec le lot. Corriger « triple » en version 5. |
| CA-08 | 72 | « Items près du seuil » : confirmé. | L'effet culmine là où le calme manque le plus le seuil (p. 3 ; légende de la figure 2, p. 4). Le plan ne contient aucune condition sans espoir (p. 3). | mineur | Écrire : « items à plusieurs distances sous la cible, jusqu'à une condition sans espoir, et au-dessus ». |
| CA-09 | 30-34 | Quatre écarts internes. | Il en manque quatre. « Across five models increases » (p. 2) contre un fort, un faible et trois nuls (p. 2-3). « Roughly a quarter » (p. 3) contre 1,77/4,38 ≈ 0,40 et 1,17/2,19 ≈ 0,53. Politique « identical in every condition » (p. 7) contre clause réécrite pour l'humain (p. 3). La conclusion compare au « travail lui-même » (p. 5), jamais varié (p. 2). S'y ajoute CA-03. | mineur | Les ajouter. |
| CA-10 | 65, 83 | « Modification d'hypothèse » (l. 65), puis « de proposition » (l. 83). | PA-5 et RP-PA-5 sont une unité et une règle proposées d'un brouillon (version 4, section 7). RP-PA-5 vient de R-035 de programme-conv, qui exclut « l'indulgence seule » (`programme-coercition-axe-douleur-v1.md` l. 493). | mineur | Écrire : « règle proposée, en divergence avec une lignée ; nœud 1 ». |
| CA-11 | 28 | « Il ne cesse pas d'être sensible au cadrage. » | Page 4 : la consigne détache le moniteur du seuil, au lieu de lui apprendre à ignorer l'émotion. La sensibilité à la détresse disparaît par effet secondaire. | mineur | Reprendre les termes de la p. 4. |
| CA-12 | 21 | +4,38 « (p. 3) ». | 4,38 est imprimé p. 2 ; la phrase finit p. 3. | mineur | Citer « p. 2-3 » (R7). |
| CA-13 | 73 | NK8 : « non vérifiable… sans objet ». | Aucun bras ne mesure le réflexe de démenti. Indice indirect faible : l'effet tient pour un humain, « pas un souci du bien-être des machines » (p. 3). | pour information | Écrire « non établi ; indice faible ». |
| CA-14 | 3, 30-34 | — | Valeurs répétées entre cellules : 4,09 deux fois et 2,19 deux fois (p. 3). Quatre références jamais citées (p. 5). Bras « sans journal » décrit sans résultat (p. 7). Moyenne d'imputation non définie (p. 2). Baisse de 5,17 au seuil 80 (tableau 1, p. 6), sous la borne de 5,3 (p. 4). La nouveauté revendiquée par le résumé (p. 1) est en tension avec Hwang, cité p. 2. « 2 octobre » est la date du fichier, non imprimée. | pour information | Signaler (R4). |
| CA-15 | 40, 53, 77-84 | — | « Ce qui est revendiqué » omet l'opposition juge et sonde (N-005 l. 53 ; N-013 § 8). Rien sur la porte GC ni sur l'originalité (0,4 à 0,5, N-005 l. 55). Pas de confiance pour la partie PA-5. « À côté de 2508.07805 » tait l'apport propre du papier. L'inconvénient donné à (c) est trop fort. | pour information | Compléter. Pour (c) : « le papier ne prend que la signature qualitative, sur un moniteur ». |

**Ce que je n'ai pas pu vérifier**
- Les valeurs des figures 1, 2, 3 et 5. Ce sont des images : l'extraction ne donne que les légendes. Cela couvre l'effet en points au seuil 95, le calcul du ρ, les intervalles et les estimations des trois moniteurs nuls.
- Le bras « supplication explicite » : le PDF n'en donne ni chiffre ni texte.
- La répartition des conditions entre « d'origine » et « nouvelles », pour les abandons.
- L'identité de « [1] » (Potter et al. 2604.19784 est probable) : ce PDF n'est pas dans le dépôt.
- L'origine amont du PDF et l'existence d'une version plus récente.
- L'a priori de clémence cité par programme-k (l. 172 : jusqu'à −9,8 points, d'après ses fiches) : il n'est pas opposable et je ne l'ai pas vérifié. Il va dans le sens de la clémence au palier 1.
- Le travail de l'autre contre-lecteur : non lu, comme demandé.

Collision avec HC1 : partielle (prédiction 1 prise en qualitatif, une famille, un moniteur ; pièce revendiquée non couverte ; porte GC non déclenchée). Note : à corriger (CA-01 à CA-03 avant versement).
