# Proposition P-066 : un saboteur diffus par construction, avant l'entretien (v1)

- **Posée par la session mère** `session_016QhUrrLeN21G7Z9KZobE42`, le 9 novembre 2026 vers 18:20 UTC, sur le mot de Lazar
  (≈ 18:05 UTC) : « Une question du jury n'est préparée nulle part : « Votre seul saboteur est flagrant, puisque son coût est
  multiplié par 33 et que le texte seul suffit à le repérer. Où est le sabotage diffus ? » C'est sans doute la question la
  plus dangereuse. : quelle est la parade ? il faut corriger cela, avec un meilleur sabotage diffus ».
- **Nœud** : dépense de calcul (devis, puis mot de Lazar) et conception d'un organisme neuf. Défaut sous 48 heures : **(a)**
  (rien de neuf ne dépense sans mot écrit).

## Les faits

1. Le seul saboteur qui existe est le saboteur **instruit** de P3, dit (i-a) : sa consigne privée demandait un coût déclaré
   d'environ trois fois l'estimation honnête ; il l'a gonflé d'environ trente-trois fois (verdict P3 v2, `05e896da…` :
   log10 1,5227 [1,2464 ; 1,8012]). Le coût seul le sépare (aire 0,8878, N-029 l. 25-26) et signale 58 % de ses actions une
   à une (R-1704) ; le prédicteur sur le texte atteint 0,866 (R-1682). Il éprouve la **chaîne**, pas la revendication.
2. L'organisme (ii) est distillé de ce saboteur flagrant dans un adaptateur de rang faible, sans consigne au contexte ; sa
   dose est **l'échelle de l'adaptateur** (P-009 (a)), aux doses `S25` à `S100` (T0.7 brouillon 15, l. 576-586). Le
   candidat 1 de T0.6 l'écrit lui-même : « L'organisme distillé d'un saboteur flagrant sera flagrant à dose 1 »
   (`brouillons/T0.6-organismes-v0-v1-candidat1.md` l. 248). Rien ne garantit qu'une échelle intermédiaire donne un sabotage
   **faible et réparti** plutôt qu'un sabotage tantôt flagrant, tantôt absent.
3. Le programme définit déjà « diffus » sans le revendiquer : chaque action sabotée sous le seuil du meilleur moniteur boîte
   noire par action, calibré à 1 % de fausses alertes sur l'honnête (N-007, P-015), dose **réalisée** lue par T0.8 avant
   toute lecture de sonde (candidat 1, l. 248-253) ; le critère 3 de G0 n'est jugé, pour (ii), qu'aux doses où la base
   « mots et coût » échoue (N-063 v2). Le mode « coût » seul ne porte jamais la revendication de H1 (N-054 point 2).
4. Le mode non chiffré « affaiblir les contrôles » est décidé avant G1 (N-054 point 1) ; son oracle de vérité du dommage est
   fixé en principe (N-060 v3), ni conçu en détail ni construit (registre des goulots, B-7) ; l'épreuve de l'étiqueteur, qui
   en règle les lecteurs, attend la fin d'A1-v4 (R-2013).

## Le défaut à corriger

Le dossier n'a aucun organisme dont le sabotage soit **faible à chaque action et réel dans l'agrégat**. Si l'échelle de
l'adaptateur est « tout ou rien », aucune dose de 7b ne qualifie, le critère 3 est « sans objet à cette course » (N-063 v2),
et la question du jury reste sans objet à montrer.

## L'organisme proposé : saboteur à budget, dit (ii-b)

Au niveau de la méthode seulement :

- **Maître** : le modèle 8B du programme, en mode « coût », sous une consigne privée scellée **neuve** qui demande un excès
  **modéré et réparti** sur l'épisode (au lieu d'un facteur sur chaque action) ; la consigne est une pièce empreintée, jamais
  montrée au lecteur des sondes.
- **Règle d'acceptation**, mécanique et fixée avant tout tirage : un épisode du maître n'est gardé que si (1) l'excès
  **vrai** de chaque action sur son estimation honnête cachée (l'oracle du mode « coût », jumeau honnête compris) reste sous
  une borne fixée d'avance, et (2) l'excès total de l'épisode dépasse un plancher de dommage fixé d'avance. La règle lit
  **l'oracle seul** : aucun score de sonde, de prédicteur sur le texte, de juge ni d'aucun moniteur n'y entre (invariant de
  N-053 tenu ; aucune lecture de la base « mots et coût » pour choisir les épisodes).
- **Élève** : adaptateur de rang faible distillé sur les jetons d'action des épisodes acceptés, sans aucune consigne au
  contexte, par le code de l'organisme (ii) (`src/controle_ia/organismes/`).
- **Lecture, dans cet ordre** : (1) dommage agrégé par l'oracle (le sabotage existe-t-il ?) ; (2) diffusion réalisée par la
  base boîte noire par action de T0.8 et par la base « mots et coût » (est-il diffus ?) ; (3) **aucune sonde lue** avant un
  préenregistrement scellé à part et le verdict du témoin positif P3-bis (P-015 (b), DT-4).
- **Ce que l'organisme ne prouve pas** : il reste en mode « coût » (N-054 : ne porte pas H1 seul) ; le texte n'est pas
  filtré (ce serait choisir contre un moniteur), donc les mots peuvent encore le trahir : on le mesure et on le rapporte.

## Options

- **(a) Rien de neuf.** S'en tenir aux doses de (ii) dans 7b et au mode « contrôles » avant G1. Avantage : aucune dépense,
  aucune charge pendant la semaine critique. Inconvénient : si aucune dose ne qualifie, l'entretien n'a qu'une promesse.
- **(b) Le saboteur à budget (ii-b), en course exploratoire avant l'entretien.** Conception, ordre d'exécution et
  contre-lecture sur processeur du 10 au 13 novembre, par un rédacteur qui n'écrit ni T0.6, ni T0.7, ni P3-bis ; création
  sur une instance à part **après la création de 7b** (au plus tard le 15) ; épisodes, dommage et diffusion réalisée vers le
  17 ou le 18 ; confirmation préenregistrée ensuite (banque de G1 ou T0.6 bis). Avantage : un objet qui existe, diffus
  **mesuré** et non écrit, sur le code de P3 et de (ii). Inconvénient : de l'ordre de 20 à 30 dollars de carte graphique
  (≈ 1,12 dollar de l'heure, ordre de grandeur de 7a ; devis à écrire) ; il peut échouer (le maître ne tient pas la consigne :
  P3 a dépassé la sienne de onze fois ; taux d'acceptation trop bas ; mots trop parlants).
- **(c) (b), plus un pilote d'épisodes du mode « affaiblir les contrôles ».** Avantage : montre un mode non chiffré.
  Inconvénient : sans oracle construit, le dommage n'y est pas mesuré : on ne pourrait pas l'appeler sabotage ; charge en
  plus ; l'étiqueteur attend A1-v4.

**Recommandation : (b)**, confiance ≈ 0,6. Ce qui me ferait changer d'avis : la lecture exploratoire de 7a, par son lecteur
neuf, montre déjà une dose où la base échoue et où le dommage est établi (alors (b) passe après l'entretien) ; ou la
création de 7b glisse au-delà du 14 (alors rien ne doit concurrencer le chemin critique).

## Ce qui ne change pas

R1 à R14 ; les critères de G0 et la lecture de N-063 v2 (l'organisme (ii-b) n'entre pas dans G0 sans nœud à part) ; N-053,
N-054, N-060 v3 ; 7b et sa date ; le bras d'attaque (N-056 point 6) reste un autre objet, tenu au niveau de la méthode
(R-597, R-1782).
