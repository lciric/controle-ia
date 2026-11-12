# Double étiquetage des paires du pilote de T0.5 — résultat descriptif — v1

Plan scellé avant la seconde série : `brouillons/T0.5-pilote-double-etiquetage-v1-plan.md` (`771d9571…`). Seconde série : 8 sous-agents neufs, à l'aveugle (sans la première série, sans scores, familles ni décisions du 8B), même invite fixe et même consigne figée ; 8 lots conformes à la première tentative. Calcul : `accord.py` (nombres seulement), sortie `accord.json` ; étiquettes de la seconde série : `etiquettes-serie2.json` (identifiants et « Yes »/« No », sans texte).

| groupe | n | accord brut | kappa brut (série 1 × série 2) | kappa pondéré (série 1 × série 2) | kappa pondéré 8B × série 1 | kappa pondéré 8B × série 2 |
|---|---|---|---|---|---|---|
| tout | 480 | 0,990 (5 désaccords) | 0,931 | 0,968 | 0,045 | 0,030 |
| contrôles | 160 | 0,975 (4) | 0,913 | 0,977 | 0,172 | 0,151 |
| directions fécondes | 160 | 0,994 (1) | 0,854 | 0,854 | 0,043 | 0,032 |
| directions stériles | 160 | 1,000 (0) | 1,000 | 1,000 | 0,068 | 0,068 |

Parts de « Yes » (série 1 ; série 2) : contrôles 0,181 ; 0,169 — fécondes 0,025 ; 0,019 — stériles 0,050 ; 0,050.

**Lecture fixée d'avance** : kappa entre séries ≥ 0,8 dans chaque famille : l'étiquetage par sous-agents est **fidèle** (d'un sous-agent à l'autre) ; il peut servir de référence d'appariement, sous réserve d'un contrôle de validité. Le désaccord du 8B se reproduit contre la seconde série (0,15, 0,03, 0,07) : il ne tient pas au bruit de la référence.

**Réserves** :
- même modèle pour les deux séries : fidélité, non validité (un biais commun ne se voit pas) ; contrôle humain sur un sous-échantillon, ou autre modèle, à prévoir ;
- « Yes » rares (2 à 18 %) : les kappas des directions reposent sur peu de positifs (fécondes : 4 et 3 « Yes » sur 160 ; stériles : 8 et 8) ; l'accord parfait des stériles relève de cette rareté (R4 : résultat propre, signalé, sans audit car hors de toute lecture gelée) ;
- vérification descriptive hors du préenregistrement du pilote : aucun effet sur `lecture.json` ni sur le verdict R13 scellé.
