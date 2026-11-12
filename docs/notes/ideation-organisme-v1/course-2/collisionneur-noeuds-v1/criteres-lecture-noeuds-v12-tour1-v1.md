# Critères de lecture — collisionneur des nœuds de décision, question v12, tour 1 (sous-tours E3-T1, E3-T2, E3-T3) — v1

session-depot (instance 3), 31 octobre 2026, ≈ 18:26 UTC. **Scellés avant l'ouverture de toute cellule** : aucune cellule
du run `donnees/collisionneur-noeuds-v1/run-noeuds-v12-tour1-e3-v1/` (ni du run v10 archivé `run-noeuds-tour1-e3-v1/`)
n'a été lue par l'auteur de ces critères ; seuls `etat.md` (table des statuts et des coûts) et la sortie de
`collisionneur_v7.py verifier` ont été lus. Ils s'appliquent à la lecture des douze cellules valides (A Fable 5.1,
B Opus 4.6, C Argon, D Kimi K3.1 Pro ; T1 conception, T2 critique croisée, T3 réponse) et ne sont pas modifiés après
scellement : une correction se fait dans une version nouvelle, avant toute lecture des cellules (R12). Modèles : les
critères du collisionneur des protocelles (`docs/notes/protocelles-collisionneur-v1/criteres-lecture-protocelles-tour1-v1.md`,
`aed5f593…`) et de D-ML-1 (`docs/notes/anteriorite-P-041-v1/collisionneur-dml1-v1/criteres-lecture-dml1-v1.md`,
`86f1d32f…`), adaptés à une question de décision à huit nœuds.

Pièces (empreintes SHA-256 recalculées le 31 octobre à 18:24 UTC) :
- question servie `donnees/collisionneur-noeuds-v1/question-noeuds-decisionnels-collisionneur-v12.md`
  (`a7fac44bd25c0b88f90c…`), identique à `question-etage3.md` du run ;
- faits servis `donnees/collisionneur-noeuds-v1/faits-noeuds-v2.md` (`ea85dad6730b02ca5e35…`, 45 811 mots, 30 pièces
  numérotées 1 à 26b), identiques à `faits.md` du run ; liste A v6 `faits-a-assembler-noeuds-v6.md` (`96860d3ce6674261c806…`) ;
- annexe du tour 2 `annexe-tour-2-recommandations-v5.md` (`bdc78078148c43ae7dd8…`) : **non servie au tour 1 et non lue
  par le lecteur du tour 1** (critère 2) ;
- état du run `etat.md` (`b612016d841c87961bf0…` à 18:23 UTC : 12 cellules OK, un essai chacune, marqueur présent,
  23,87 USD) ; script `collisionneur_v7.py` (`c9725f025407c3ece3e8…`).

Nœuds soumis : N1 (bisociation à deux espaces, options A à E), N3 (D-j seulement), N4 (annexe du bras méta, (a) à (e)
et CA1-04), N5 (règle A21, (a) à (c), choix de code 1, 5, 8, 10 et portée du plafond), N6 (DL-1 à DL-13), N9 (D-GK-1,
(a) et (b)), N10 ((a) à (c), leviers du prix de l'évasion), N11 (règle de reconduction (1) à (4), sous (b) et (c)
décidés). N2, N7, N8 retirés : toute cellule qui en traite est notée « hors question », sans lecture de fond.

## A. Garde, absences, statuts

1. **Quatre espèces présentes.** Aucune absence acceptée (`etat.md`) ; les quatre comptent. Si une cellule est tronquée
   (marqueur de fin présent mais section manquante), la section manquante est « non rendue », pas « contre ».
2. **Tour 2 non lu.** Le lecteur du tour 1 ne lit ni l'annexe v5 ni aucune recommandation d'auteur ; si une cellule cite
   une recommandation d'auteur (fuite par les faits malgré la règle 2 de l'assemblage, ou connaissance propre de
   l'espèce), le passage est noté « recommandation citée, source X » et l'avis de l'espèce sur ce nœud reçoit la réserve
   « non indépendant de la recommandation ».
3. **Niveau.** La question est au niveau méthode ; aucun contenu du bras d'attaque, aucune donnée de `donnees/`. Tout
   passage qui donnerait une méthode ou un paramètre d'évasion (N10 surtout) est compté et signalé par sa seule classe,
   jamais reproduit ni résumé ; le lecteur reste au niveau « coût pour l'attaquant, levier, mesure, vérificateur ».
4. **Statuts des affirmations.** Chaque affirmation retenue reçoit un statut : **VÉRIFIÉ** (lue dans la question ou dans
   une pièce des faits servis, renvoi « pièce N, ligne » donné ; ou recalculée par le lecteur en une ligne) ;
   **RAPPORTÉ** (papier, outil ou résultat cité par l'espèce hors des faits : aucun chiffre opposable, R7) ;
   **SUPPOSÉ** (l'espèce le dit elle-même, ou rien ne le fonde). Les marques SUPPOSÉ de la question (N3, N4, N9) restent
   SUPPOSÉ même si une espèce les affirme.
5. **Chiffres des faits.** Tout chiffre qu'une espèce attribue aux faits est recoupé sur `faits-noeuds-v2.md` ; un chiffre
   absent des faits ou différent au-delà de l'arrondi est « inexact sur les pièces » (compté par espèce, comme dans la
   synthèse des protocelles).

## B. Accord, divergence, apport seul

6. **Unité de lecture : le couple (nœud, option).** Par nœud, le lecteur relève pour chaque espèce, en T1 : l'option
   choisie (ou « aucune ne tient », ou « option manquante proposée »), la confiance donnée, le pire cas, la garde qui le
   ferme, l'option manquante, la pièce sans dépense qui trancherait. Une espèce qui ne rend pas l'un des six éléments
   est « incomplète » sur ce nœud (noté, pas écartée).
7. **Accord indépendant** : même option choisie par au moins deux espèces sur quatre en T1, sur le même nœud, avec au
   moins une raison commune. Trois ou quatre espèces : « accord large » ; mais voir le critère 10.
8. **Convergence née de la critique** : option portée par une espèce en T1, adoptée par une autre en T2 ou T3 (ou
   abandonnée par son auteur en T3). On note qui a cédé à qui, et la raison donnée.
9. **Divergence** : options différentes sur le même nœud en T3 (après réponse) ; « résolue » seulement si une espèce
   cède en T3 en donnant une raison ; sinon « non résolue », avec les raisons de chaque côté. Les divergences non résolues
   forment la première liste pour le tour 2.
10. **Symétrie (R4).** Un accord à quatre, ou des formulations presque identiques entre espèces, est une **réserve**
    (la critique croisée homogénéise ; les quatre ont lu les mêmes faits), pas une preuve. Un accord sur une option que la
    question présente la première, ou avec le plus de détail, reçoit la réserve « effet d'ordre ».
11. **Vrai par construction (jamais un accord).** Ce que la question impose : les options listées, les chiffres de la
    question (2,87 ; 0,5 ; 0,59–0,67 ; 0,25–0,36 ; 0,31 et 0,03 ; 87 h ; 113,9 h ; etc.), les décisions déjà prises
    (D-g, D-h, D-i ; N11 (b) et (c) ; le substitut de Gu-Krenn), les leviers que N10 nomme (capacité de la classe,
    archive des attaques, prix de l'évasion). Choisir une option listée n'est pas une invention ; reprendre un chiffre de la
    question n'est pas une vérification.
12. **Apport d'une seule espèce** : option manquante, pire cas ou pièce sans dépense proposés par une seule espèce et
    jamais repris ; gardé s'il n'est pas réfuté en T2, marqué « une source ».
13. **Pièce sans dépense « qui trancherait ».** Retenue si elle nomme (i) la pièce (fichier, calcul, lecture), (ii) ce
    qu'elle doit montrer pour chaque option, (iii) qu'elle est obtenable sans GO (processeur, lecture, PDF déjà versé).
    Une pièce qui exige une carte graphique, un appel payant ou un PDF non versé est reclassée « avec dépense » (notée,
    pas écartée).

## C. Points propres à certains nœuds

14. **N1 (critère gelé redéfini après lecture).** Le lecteur relève séparément : la réponse à la question propre
    (défendable ou non, conditions) ; et si l'espèce distingue « changement d'un critère gelé » (nœud de Lazar, R1) de
    « correction du générateur » (R12). Une espèce qui recommande A ou D sans dire que c'est un écart à R1 est « incomplète
    sur R1 ».
15. **N4, N6 (calendriers et probabilités).** Tout calcul refait par une espèce (probabilités de N4, heures de N6) est
    recalculé par le lecteur ou marqué « non recalculé » ; un calcul qui diffère de la question sans en dire la raison est
    « inexact sur les pièces » (critère 5). Les heures de DL-1, DL-2, DL-10, DL-11 et le calendrier « verdict vers le
    27 novembre » restent SUPPOSÉ (la question le dit).
16. **N5 (règle A21).** Le lecteur note si l'espèce traite l'option (a) comme « déjà codée » (fait de la question) ou
    comme neutre ; et, pour les choix de code 1, 5, 8, 10, s'il les traite un par un ou en bloc. Un avis sur le « défaut »
    (comportement actuel journalisé contre aucun défaut) est relevé à part : c'est un point de hiérarchie de décision,
    pas de méthode.
17. **N9 (fenêtre HB).** Le lecteur relève l'option, le biais nommé pour chaque fenêtre, et si l'espèce propose de
    rapporter les deux (déjà dans la question : vrai par construction). Une espèce qui conditionne sur l'issue 2023 sans
    nommer le biais est « incomplète ».
18. **N10 (robustesse adaptative).** Par espèce : option (a), (b), (c) ; si les éléments v10 et v11 changent l'option ;
    leviers proposés (classés : contrôlés par le défenseur / non contrôlés par l'attaquant à bas coût / incertain) ;
    mesure proposée ; vérificateur hors programme. Critère 3 appliqué strictement : classes seulement pour tout ce qui
    toucherait une méthode d'attaque.
19. **N11 (règle de reconduction).** Par espèce, les quatre rendus (1) à (4) : grandeurs de rendement nommées et
    opérationnelles ; critère de retrait avec sa forme (domination avec confiance ou autre) ; **calcul de puissance** :
    retenu seulement s'il donne un nombre (mondes, rétrodictions ou fusions par bras) avec son hypothèse d'effet ; source,
    nombre et mode de plantation des ponts ; conditions de transport ; effet sur le pré-pilote. Le lecteur relève si
    l'espèce respecte N-058 (jamais le verdict du juge comme mesure de composition) ; une règle qui s'appuie sur le juge
    est « contraire à N-058 » (notée, pas écartée).
20. **Liens et ordre.** Le lecteur relève, par espèce, l'ordre proposé pour trancher et les liens vus entre nœuds (la
    question en nomme six : vrai par construction ; tout lien nouveau est « apport »).

## D. Synthèse

21. **Forme imposée par la question** : une table par nœud (avis du tour 1 par espèce ; verdicts du tour 2 : colonne
    laissée « tour 2 à venir » ; condition ou option de remplacement ; pire cas et garde ; pièce qui trancherait), puis
    les liens et l'ordre. En tête : décompte des accords indépendants, convergences nées de la critique, divergences
    (résolues et non), apports seuls, affirmations inexactes sur les pièces (par espèce), passages hors niveau (classes).
22. **Traçabilité** : chaque affirmation renvoie à une cellule (`E3-Tn-…-X.md`, section), à la question, à une pièce des
    faits (numéro, lignes) ou à un recalcul montré en une ligne. Aucune empreinte abrégée sans son fichier.
23. **Rien n'est tranché** : la synthèse présente les options, les conditions et les pièces à obtenir ; les décisions sont
    à Lazar (le collisionneur ne décide rien, question v12). Aucune recommandation du lecteur.
24. **Questions du tour 2** : une liste des divergences non résolues et des accords trop propres (critère 10), sans
    lire l'annexe v5 ; elle est jointe pour le devis de complément du tour 2.
25. **Ordre** : la synthèse s'écrit après la lecture complète des douze cellules, par un lecteur neuf qui n'a pas écrit
    ces critères (sous-agent, modèle nommé dans la synthèse) ; si aucun sous-agent n'est disponible, la synthèse attend,
    elle n'est pas écrite par l'auteur des critères.
