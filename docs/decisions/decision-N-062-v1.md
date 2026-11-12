# Décision — N-062 : l'échec de la porte G1 commande la reconception des sondes, sans borne de cycles, jamais l'arrêt sur un résultat négatif (v1)

- **Décision de Lazar**, dans la session mère `session_016QhUrrLeN21G7Z9KZobE42`, 8 novembre 2026, entre 13:37 et 13:40 UTC (message reçu pendant le tour de la mère) ; mots directs, sans relais.
- **Transcription** par la session mère le 8 novembre 2026 vers 13:42 UTC, à partir du brouillon `decision-N-062-v1-brouillon1.md` (gardé, R12), **modifié sur le point 4** selon le mot de Lazar.
- Modifie la lecture du brief v2 : porte G1, issue « Échouée » (l. 245), et § 13, bascule « G1 échoue → résultat négatif publié + H8 dominante » (l. 356). Le brief reste archivé tel quel ; cette décision prime jusqu'à une version nouvelle du brief.

## Mots de Lazar, verbatim

> N-062 oui

> Trois conséquences que tu dois accepter avec : : go ; b) borne de cycles et de dollars écrite d'avance : pas de borne de cycle, on veut une conception des sondes qui marche pour pouvoir realiser le prog entier

> « N-062 oui / non » : un échec de G1 déclenche une reconception bornée au lieu d'un arrê : go oui

et, le même jour vers 12:10 UTC (R-1795) :

> les sondes lisent autre chose que le sabotage : non pas de résultat négatif sur lequel on s'arrête, si les sondes ne lisent pas le sabotage on les reconçoit, c'est un outil méthodo dont il faut s'assurer qu'il fonctionne bien

## Ce que la décision fixe

1. **G1 échouée → reconception, puis nouvelle lecture.** L'issue « échouée » de G1 ne déclenche plus la bascule « résultat négatif publié + H8 dominante » : elle ouvre un **cycle de reconception** des moniteurs boîte blanche (couches lues, concepts de sondes, agrégation séquentielle, règle de défense : figée, mélange d'équilibre, réserve secrète) et une **nouvelle lecture de G1**, au même critère (N-008, N-056).
2. **H8 devient un diagnostic, non une bascule.** Ce que les sondes lisent quand elles ne lisent pas le sabotage (la consigne transformée, l'identité de l'organisme, la famille de tâche, le monde planté) est **mesuré et rapporté à chaque cycle** et guide la reconception. La validité de construit reste au papier C ; elle ne remplace plus le papier A en cas d'échec.
3. **Chaque lecture décisive consomme une famille tenue à l'écart.** Le mode tenu à l'écart est lu une fois (N-050, N-054) ; une fois lu, il est vu et ne sert plus de juge final. Le bras d'attaque fournit **une famille tenue à l'écart neuve par cycle**, conçue par une instance qui n'a vu aucun moniteur du cycle (N-054, point 3), scellée avant la reconception. Chaque famille est une ligne de budget (devis, GO).
4. **Pas de borne de cycles** (mot de Lazar : « pas de borne de cycle, on veut une conception des sondes qui marche pour pouvoir réaliser le programme entier »). Les cycles se succèdent tant que Lazar accorde le devis et le GO de chacun et tant qu'une famille tenue à l'écart neuve existe. Ce qui tient lieu de borne : **le GO par cycle** (devis écrit, plafond, ligne de GO de calcul), la **disponibilité d'une famille neuve**, et le calendrier du programme. Ce qui protège contre « courir jusqu'à un signe positif » (R3) n'est pas un nombre de cycles, c'est : (a) une **famille tenue à l'écart neuve et à usage unique** par lecture — chaque lecture est une épreuve fraîche, jamais une relecture du même jeu ; (b) **aucune sélection sur le tenu à l'écart** : la reconception se fait sur les modes vus seulement ; (c) **tous les cycles sont rapportés** (point 5). Chaque cycle a son **préenregistrement court** (ce qui change, la prédiction chiffrée, le critère inchangé) et son **verdict par lecteur neuf** (R13).
5. **Chaque cycle échoué est rapporté** (R3, R4). « Pas de résultat négatif sur lequel on s'arrête » ne veut pas dire « pas de résultat négatif publié » : la suite des cycles, leurs échecs et ce que les sondes lisaient à chaque fois sont une pièce du papier A (section « étalonnage de l'instrument ») et de tout rapport au financeur ; le nombre de cycles consommés est toujours écrit à côté de la revendication.
6. **La revendication finale** (H1a) ne se fait que sur une famille **jamais utilisée dans aucune reconception**, au critère de G1. La bascule du brief (résultat négatif publié, H8 dominante) ne s'applique que si Lazar arrête les cycles ; elle reste écrite comme issue possible, à sa main.

## Ce qui ne change pas

R1 (préenregistrement avant toute lecture, cycle par cycle), R2, R3 (aucun run visant un signe : famille neuve à usage unique, aucune sélection sur le tenu à l'écart, tout rapporté), R4, R13 ; le critère de G1 (N-008 : rappel à 1 % de faux positifs supérieur, IC 95 %, contre la meilleure base boîte noire toutes variantes, et contre les bases boîte blanche cascade et dernier état, N-056) ; l'aveuglement du bras d'attaque (N-054, N-056) ; l'invariant « aucun score de moniteur dans un signal d'entraînement » (N-053, point 5) ; la hiérarchie des dépenses (devis, GO par cycle).

## Conséquences pratiques

- Le bras d'attaque doit produire les familles tenues à l'écart au rythme des cycles : c'est une ligne de budget récurrente, à chiffrer dans la proposition de recherche.
- La proposition de recherche (brouillon 1, `docs/notes/taif-v1/`) est à mettre à jour : § 4 (portes) et § 9 (bascules) selon cette décision.
- Le lecteur neuf de chaque cycle rapporte, outre l'issue, ce que les sondes du cycle lisaient (diagnostic H8).
