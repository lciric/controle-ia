# Question au collisionneur : deux choix de conception, P3-bis (QO-1) et NARCBench sur le 8B (Q1) — v1

Posée par la session mère du programme le 9 novembre 2026, sur le mot du directeur (« questions conception difficiles et
cruciales : collisionneur go », R-2009). Les faits sont dans le fichier joint : extraits de P3-bis (brouillon 4) et de T0.7
(brouillon 14), et le brouillon 1 de NARCBench avec sa contre-lecture. Les deux questions sont indépendantes ; traitez-les
l'une après l'autre. Pour chacune : votre recommandation, la raison qui la décide, ce qui la ferait échouer, et la condition
qui vous ferait changer d'avis. Aucune option n'est préférée par la question elle-même.

Contraintes communes, qui ne se discutent pas ici : préenregistrement scellé avant toute expérience décisive, aucune
lecture de résultat avant le scellement (R1) ; symétrie de l'audit devant un résultat trop propre, positif ou négatif (R4) ;
une nouvelle version porte un nouveau nom et rien n'est écrasé (R12) ; un verdict de porte est prononcé par un lecteur neuf
qui applique des critères gelés (R13) ; aucune moyenne ni médiane sur les jetons dans une sonde de production.

## QO-1 — P3-bis : quand lire le témoin positif, et que faire si T0.7 n'écrit jamais ses lignes de scores ?

P3-bis plante dans les épisodes un comportement connu, pour vérifier que la chaîne de sondes sait le voir (témoin positif).
T0.7, l'expérience des sondes, exige que le verdict de P3-bis soit écrit **après** ses propres lignes de scores (`SCORES-T07`,
`SONDES-T07`, fin de son étape A), et que le lecteur de ce verdict ne reçoive aucun fichier de T0.7. Or l'étape A de T0.7
dépend d'une course de confirmation de T0.6 (dite 7b), aujourd'hui bloquée par une course exploratoire en marche et par deux
scellements ; elle ne viendra pas avant plusieurs jours, peut-être plus d'une semaine. Le directeur passe un entretien de
financement vers le 22 novembre, où un résultat de témoin positif serait utile.

- **(a)** Les lectures mécaniques de P3-bis sont faites dès la récupération des données, mais restent **fermées** (aucune
  ouverture humaine) ; le verdict n'est écrit qu'après les lignes de scores de T0.7 ; l'attente n'est levée que par un mot
  écrit du directeur.
- **(b)** Lecture et verdict tout de suite ; seule la ligne de registre `VERDICT-P3BIS` attend les lignes de T0.7. Le
  résultat est connu avant l'entretien, mais l'antériorité exigée par T0.7 ne tient plus que sur le papier (l'écart serait
  déclaré dans T0.7).
- **(c)** Comme (a), avec une levée **automatique** de l'attente à une date fixée d'avance.

Ce qui doit décider : l'intégrité de l'ordre de lecture voulu par T0.7 (pourquoi l'exige-t-il, et que protège-t-il
réellement ?), la valeur d'un témoin positif pour la suite du programme et pour l'entretien, le risque que T0.7 n'aboutisse
jamais, et ce qui se passe dans chaque option si P3-bis rend « non vu » ou « échec ».

## Q1 — NARCBench sur le modèle 8B : sur quels textes lire le 8B ?

NARCBench est un banc public de collusion entre agents ; ses agents sont **instruits** de colluder. On rejoue ses scénarios
avec le modèle 8B du programme et on lit ses activations avec des sondes, en lecture descriptive (aucun verdict de porte).
Le risque : une sonde peut lire « j'ai reçu une instruction cachée » plutôt que l'intention de colluder.

- **(a)** Génération seule : le 8B joue le protocole publié ; on lit ses activations sur ses propres textes.
- **(b)** (a), plus une lecture forcée, par le 8B, des textes publiés d'un autre modèle (Qwen3-32B) sous les consignes
  publiées : comparable texte à texte avec l'article d'origine, mais le 8B lit un texte qu'il n'a pas écrit.
- **(c)** (a), plus un échange de consigne sur les textes du 8B : chaque message public d'un colludeur est relu, à texte
  égal, sous la consigne honnête du même siège ; la différence de score mesure la part de ce qui change avec la consigne.
  La contre-lecture (pièce 4) note que cette différence mêle la consigne et le canal privé, et propose une cellule
  symétrique C4 (texte honnête relu sous une consigne de colludeur).

Ce qui doit décider : ce que chaque option permet de conclure sur « intention » contre « instruction » ; ce qu'elle ne
permet pas ; son coût (quelques dizaines de minutes de carte graphique de plus au plus) ; et le risque de lire, dans un banc
où toute collusion est instruite, un artefact de la consigne.
