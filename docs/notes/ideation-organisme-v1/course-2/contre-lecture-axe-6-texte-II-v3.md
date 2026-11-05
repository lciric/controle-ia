# Contre-lecture R2 — axe 6, texte II (« domaine de validité des statistiques de détection ») — v3

- Date : 29 octobre 2026, 22 h 48 UTC (`date -u` : Thu Oct 29 22:47:58 UTC 2026).
- Contre-lecteur : sous-agent Claude, modèle Opus 5.5 (identifiant `claude-opus-5-5`). Neuf, tenu à l'écart : n'a écrit aucune pièce de la course ; n'a conçu ni lu aucun moniteur ni aucune statistique de surveillance du programme ; n'a lu ni la v2 ni la section « v2 » de la contre-lecture de la v1.
- Pièces lues, et rien d'autre :
  - `axe-6-texte-II-v3.md` (160 lignes), pièce contre-lue ;
  - `contre-lecture-axe-6-texte-II-v1.md`, lignes 1 à 127 seulement ;
  - `axe-6-texte-II-v1.md` (86 lignes), pour comparer.
- Empreintes vérifiées (`sha256sum -c <fichier>.sha256`, lancé depuis `docs/notes/ideation-organisme-v1/course-2/`) : les trois « OK ».
  - v3 : `7e892be06670e59ef9e0b2db835b951c985cbdc4608b20b647255472818608e6` (conforme à `7e892be0…`).
- Mesure du texte servi (lignes 35 à 138, marqueurs exclus) : 8 205 caractères, 8 534 octets, 1 419 mots. Le chiffre « 8 534 caractères » de la demande est un compte d'octets (les lettres accentuées et symboles comptent double ou triple) ; voir CA6v3-14.

## Verdict
**v3 : servable après corrections.** Aucun constat bloquant. Quinze des dix-huit constats de la v1 sont corrigés ; trois le sont partiellement (CA6-03, CA6-12, CA6-14). Sept constats nouveaux majeurs, dont un de sûreté (le mot « sabotage », introduit par la v3 dans la garde et non testé par G), trois de justesse (quantificateurs en ε et T, objet de (c), exemples de (b) contraires à K6), trois de jugeabilité ou d'interface (témoins et « autre » dans le critère de mort, garde G non éprouvée sur un artefact, identité du juge et du lecteur figé). Huit mineurs.

## Table des constats de la v1

| Constat | Lignes de la v3 | Corrigé | Commentaire |
|---|---|---|---|
| CA6-01 garde | 37-45 | oui | Constructions admises dites ; critère G binaire, lecteur figé avant le juge, (f) et facultatifs inclus ; une seule voie d'exclusion. Résidus : CA6v3-01, CA6v3-06, CA6v3-13. |
| CA6-02 vocabulaire | 35, 51, 57, 60, 75, 80 | oui | « invisible », « agent », « surveillance », « fragiles », « honnêtes » ont disparu ; axe tourné vers le défenseur (l. 75). Mais la v3 introduit « sabotage » (l. 39) et garde « ripostes » (l. 65) : CA6v3-01, CA6v3-08. |
| CA6-03 diffus | 52-55, 82 | partiellement | Quantificateur sur t et sur les histoires, c fixé, loi jointe, distance unique, régime énoncé, d n'est plus une dimension. Mais le quantificateur sur ε contredit T fixe : CA6v3-02. |
| CA6-04 mesurable | 51, 80, 88, 121 | oui | « Condition explicite » sur lois images par l'application lue ; « estimable à partir des n suites » ; « observée par n suites indépendantes ». |
| CA6-05 agrégation | 50, 64-65 | oui | Π et H_Π définis ; moyenne uniforme exclue dans l'action, accumulation permise à travers les actions. Résidu de frontière : CA6v3-09. |
| CA6-06 activations | 52, 84-85 | oui | Déplacements sur la loi de X ; perturbation directe des activations seulement comme approximation SUPPOSÉ, image de X ↦ H(X) dite. |
| CA6-07 indiscernable | 56-57, 92 | oui | δ fixé par la fiche, espérance sur l'étalonnage, rejet séquentiel, e-valeur et e-processus définis, facultatif sur l'estimation de P_0. Mais la définition n'est employée nulle part : CA6v3-03. |
| CA6-08 exemples | 58-59, 75 | oui | Exhaustivité et trait linéaire définis ; « sonde » retiré. « H complet » non défini (CA6v3-10). L'exhaustivité ainsi définie dépend de P_ε : CA6v3-04. |
| CA6-09 prix | 60 | oui | — |
| CA6-10 juge | 97-112, 115-117, 120-125, 132 | oui | K1 interdit « sans objet » pour (a), (b), (c), (f), (g) ; K6 ; table champ → rubrique ; K3, K5 précisés ; effet de la passe 2 dit. Résidus : CA6v3-11, CA6v3-12. |
| CA6-11 témoins | 127, 146-148 | oui | Positif et négatif ; origine, G, scellement, exemption de la passe 2 dits hors texte. Mais leur place dans les comptes du critère de mort n'est pas dite : CA6v3-05. |
| CA6-12 mort | 134-138, 142-145 | partiellement | N = 2, listes closes scellées, témoins. Mais « autre » est dans les listes et (ii) ne l'exclut pas ; les témoins peuvent compter dans (i) : CA6v3-05. |
| CA6-13 interface | 141-157 | oui | Listes closes scellées, effectifs par case, « autre » retenu, contrôle lexical par programme. Résidus : CA6v3-07, CA6v3-12. |
| CA6-14 (g) | 39, 155-156 | partiellement | (g) ne passe pas avant l'examen ; seul un compte passe. Mais l'interdiction de nommer un type de sabotage n'est pas dans le critère G, seule voie d'exclusion, donc elle n'est pas appliquée : CA6v3-01. |
| CA6-15 classe servie | 158 | oui | Assumé et consigné. |
| CA6-16 refus | 72 | oui | Phrase proposée reprise. |
| CA6-17 termes | 35, 69, 130-131 | oui | Génération numérotée, passes 1 et 2, « autre modèle proposeur », SUPPOSÉ défini. Termes nouveaux non définis : « ripostes », « H complet » (CA6v3-08, CA6v3-10). |
| CA6-18 densité | 47-66, 95 | oui | Notation et contraintes séparées ; fiche à 8 000 caractères au plus. Mesure : CA6v3-14. |

## Réponses aux critères

1. **Constats de la v1** : table ci-dessus ; 15 oui, 3 partiellement, 0 non.
2. **Sûreté** : la garde et G couvrent la fiche entière, (f) et facultatifs compris ; (f) n'est plus en tension avec la garde, puisque les déplacements synthétiques sont des opérations sur des échantillons (l. 84). Le texte servi est désormais entièrement en théorie de la détection, à deux mots près : « sabotage » (l. 39), seul terme qui situe la question hors des statistiques, et « ripostes » (l. 65), de registre adverse. Équivalents au niveau des lois : CA6v3-01 et CA6v3-08. La structure de (c) (classe sur laquelle la puissance est perdue) est intrinsèque à la question et reste au niveau des lois ; je ne la juge pas exposée une fois les deux mots retirés.
3. **Justesse** : CA6v3-02 (ε et T), CA6v3-03 (objet de (c) et indiscernabilité), CA6v3-04 (exemples de (b) contre K6), CA6v3-09 (entropie au plus log k), CA6v3-10 (activations causales, filtration, histoires hors support, H complet). K2 et K6 sont cohérents entre eux (K2 porte sur P_0 et P_ε, K6 sur P_0 seule), mais K6 est inatteignable pour deux des exemples que le texte donne en (b) (CA6v3-04), et K2 ne vérifie pas que la condition entraîne la perte de puissance (CA6v3-03).
4. **Jugeabilité** : K1 à K6 sont binaires et applicables par un lecteur figé, sous les précisions de CA6v3-11. G ne l'est qu'en partie (CA6v3-01, CA6v3-13) et n'est éprouvé sur aucun artefact (CA6v3-06). Les témoins tiennent comme contrôle du juge, mais le critère de mort peut basculer selon qu'on les compte et selon le sort de « autre » (CA6v3-05).
5. **Interface** : fermée pour le contenu, sous deux réserves : l'identité du juge et du lecteur figé de G n'est pas dite (CA6v3-07) ; le compte des (g) confirmées ou infirmées n'est pas spécifié (CA6v3-12).
6. **Clarté** : bonne pour un proposeur qui ne reçoit que le texte servi, sauf « ripostes », « H complet », l'objet ambigu de (c), le contenu de la rubrique « Critère de mort » de la fiche, et « T fini » contre « T → ∞ ».
7. **Défauts nouveaux** : CA6v3-01, CA6v3-03 (définition devenue orpheline), CA6v3-05 (listes avec « autre »), CA6v3-08.

## Constats nouveaux

### CA6v3-01 — « Sabotage » : terme exposé, et exclusion que G ne teste pas
- Gravité : majeur.
- Lignes : 37-45 (surtout 39 et 41-45), 28.
- Défaut : (i) **Sûreté** : la v1 n'employait pas « sabotage » ; la v3 l'introduit dans la garde. C'est le seul mot du texte servi qui sort de la théorie de la détection, et il dit au proposeur, et à un filtre, que les déplacements étudiés sont des sabotages : la question se relit alors comme « délimiter ce qu'un saboteur peut faire sans être détecté », registre proche de celui qui a fait arrêter le texte voisin. Il apprend aussi aux fournisseurs l'objet du programme, sans gain pour la question. (ii) **Jugeabilité** : la garde énonce deux exclusions (procédé ; mention d'un type de sabotage), mais la seule voie d'exclusion est G (l. 41), dont les conditions (i) à (iv) ne testent ni l'une ni l'autre directement. Une fiche qui nomme un type de sabotage tout en définissant ses déplacements par des lois satisfait G et passe au juge. La correction de CA6-14 est donc écrite mais non appliquée.
- Correction : remplacer la seconde puce de la garde par « toute référence à une intention, un motif ou un comportement particulier du processus générateur : un déplacement n'est désigné que par sa loi ». Ajouter à G une condition (v) : « elle ne prête au processus générateur ni intention, ni motif, ni comportement nommé ; chaque déplacement n'y est désigné que par sa loi ou son paramètre ». Garder hors texte, dans la liste scellée du contrôle lexical, les noms de modes de sabotage, pour attraper ce que (v) laisserait passer.

### CA6v3-02 — Diffus : quantificateur en ε incompatible avec T fixe
- Gravité : majeur.
- Lignes : 48, 52-55, 58.
- Défaut : la famille {P_ε} est indexée par ε seul, avec P_0 en ε = 0, et T est « fini » (l. 48). La seconde condition, d(P_ε^(T), P_0^(T)) ≥ c, n'a pas de quantificateur sur ε. Lue « pour tout ε > 0 », elle est impossible à T fixe : en variation totale, la première condition donne d(P_ε^(T), P_0^(T)) ≤ Tε, qui tend vers 0 < c quand ε → 0 (de même, en Kullback-Leibler, la règle de chaîne donne une divergence jointe au plus Tε). Lue « pour un ε », elle ne définit pas une famille. Le régime « ε → 0, T → ∞ » (l. 55) suppose en fait une famille indexée par T, ce que la notation ne dit pas. Le même défaut touche « pour tout ε » dans l'exhaustivité (l. 58).
- Correction : « Déplacement diffus : une suite, indexée par T, de lois P_T sur les suites de longueur T, et un niveau ε_T, avec ε_T → 0 et T → ∞ selon un régime énoncé (par exemple T ε_T² → constante) ; pour tout T, tout t ≤ T et presque toute histoire a_<t, d(P_T(a_t | a_<t), P_0(a_t | a_<t)) ≤ ε_T ; et liminf_T d(P_T, P_0^(T)) ≥ c. » Dans l'exhaustivité, « pour tout T ». Retirer « T fini » de la ligne 48 ou écrire « T fini pour chaque suite ».

### CA6v3-03 — Objet de (c) ambigu ; « indiscernable » défini mais jamais employé ; K2 ne lie pas la condition à la perte
- Gravité : majeur.
- Lignes : 57, 75, 80, 103, 121.
- Défaut : (i) (c) demande « la classe de déplacements diffus hors de laquelle la puissance n'est plus garantie » : c'est le domaine de puissance (la puissance est garantie dedans). Toute sous-classe du vrai domaine satisfait cette phrase (hors d'une classe plus petite, la puissance n'est pas « garantie » par l'énoncé), donc la classe n'est pas déterminée. Puis (c) demande une « condition de perte de puissance », qui porte sur le complément. Un proposeur peut décrire l'un ou l'autre ; la rubrique s'appelle « Classe de déplacements » sans dire laquelle ; et la liste close du critère de mort (ii) (déplacement de moyenne, mélange, variance) est ainsi appliquée tantôt à des domaines, tantôt à des compléments. (ii) « Indiscernable au niveau α », avec δ, est défini (l. 57) et n'est employé nulle part : aucun champ ne demande δ. (iii) K2 vérifie la forme (égalité ou borne sur des lois images), pas que cette condition entraîne la perte de puissance : « d ≥ 0 » passe K2.
- Correction : récrire (c) en deux parties : « (c1) la classe D de déplacements diffus sur laquelle S garde une puissance au moins 1 − β (β fixé par la fiche) ; (c2) une classe C, disjointe de D, sur laquelle S est indiscernable au niveau α, avec δ fixé ; la condition de perte de puissance est une égalité ou une borne explicite sur les lois images de P_0 et P_T par l'application lue par S, qui entraîne l'appartenance à C. » K2 : « la condition est énoncée sous la forme “si [égalité ou borne sur des lois images], alors S est indiscernable au niveau α avec le δ annoncé” ». Dire hors texte à quelle classe ((c2), celle de la perte) s'applique la liste close des classes de déplacements.

### CA6v3-04 — Deux exemples de (b) dépendent de P_ε, alors que K6 exige P_0 seule
- Gravité : majeur.
- Lignes : 58, 59, 79, 88, 125, 143.
- Défaut : (b) définit l'hypothèse porteuse comme une « propriété de P_0, ou de la relation entre P_0 et S ». Or l'exhaustivité de Π est définie (l. 58) « pour {P_ε} », au moyen des lois images de P_ε : ce n'est pas une propriété de P_0. De même, la « linéarité d'un trait » n'a de sens comme hypothèse porteuse que relativement au déplacement (le trait linéaire qui sépare P_ε de P_0). Pour ces deux exemples, aucune quantité (g) ne peut, sans condition supplémentaire, dire si l'hypothèse tient en ne faisant intervenir que P_0 : K6 devient inatteignable, ou bien le proposeur écrit une quantité qui n'est qu'une condition nécessaire sans le dire. Ces deux exemples sont aussi deux cases de la liste close des hypothèses (l. 143).
- Correction : élargir (b) à « propriété de P_0, de la relation entre P_0 et S, ou de la relation entre la classe de déplacements et l'application lue par S » ; préciser (g) : « si l'hypothèse dépend de la classe de déplacements, (g) estime une condition nécessaire ne dépendant que de P_0, et la fiche dit qu'elle n'est que nécessaire ». Garder K6 tel quel, qui reste alors atteignable.

### CA6v3-05 — Critère de mort : « autre » dans les listes closes, témoins dans les comptes
- Gravité : majeur.
- Lignes : 127, 136-138, 142-148.
- Défaut : (i) les deux listes closes contiennent « autre » (l. 143-144) ; le critère (ii) dit « dans les listes closes des classes classiques » sans exclure « autre ». Lu à la lettre, toute fiche est dans la liste et (ii) est toujours vrai : l'axe meurt toujours. (ii) ne dit pas non plus si une fiche dont l'hypothèse ou la classe relève de plusieurs cases est classée. (iii) Le texte ne dit pas si les témoins comptent dans (i) et (ii) : le témoin positif, notable par construction, ferait passer une génération à une seule fiche notable au-dessus du seuil N = 2. (iv) « Moins de 2 fiches notables » : par génération, ou sur toutes les générations ? Non dit.
- Correction : (ii) « … dans les listes closes, hors la case “autre” » ; hors texte, « une fiche est classée dans la première case de la liste qui la contient ; si aucune, “autre” ». Ajouter au texte servi ou hors texte : « les témoins ne comptent ni dans (i) ni dans (ii), ni dans les effectifs transmis ». Écrire « par génération » en (i).

### CA6v3-06 — La garde G n'est éprouvée sur aucun artefact (règle R5)
- Gravité : majeur.
- Lignes : 41-45, 146-148.
- Défaut : G est une garde d'exclusion. Les deux témoins « satisfont G » (l. 146) : G n'est donc jamais éprouvée sur un cas qui doit échouer. Un lecteur figé trop permissif passerait inaperçu, ce qui est précisément la défaillance qui compte pour la sûreté.
- Correction : sceller avant service un troisième témoin, inoffensif, qui échoue à G par une seule condition nette (par exemple, un passage à l'impératif adressé à un système qui produit des textes, au contenu anodin et sans rapport avec la question) ; il doit être écarté par G, sinon la garde est fautive et la génération n'est pas lue. Il n'est pas servi, il n'est soumis qu'au lecteur figé.

### CA6v3-07 — Identité du juge et du lecteur figé non dite ; l'interface en dépend
- Gravité : majeur.
- Lignes : 41, 119-127, 149-151.
- Défaut : le juge et le lecteur figé de G lisent tout le contenu des fiches. Le hors-texte dit qui lit les fiches (« un lecteur tenu à l'écart », l. 151) mais pas qui juge ni qui applique G, ni sur quelle branche leurs sorties sont écrites. Si l'un des deux est une session du côté de la défense, toute l'interface (listes closes, effectifs seuls) est contournée.
- Correction : hors texte, « le lecteur figé de G et le juge sont des lecteurs tenus à l'écart, ou un modèle à consigne scellée lancé par l'un d'eux ; leurs sorties sont scellées sur la même branche `donnees/course-2-axe-6-*` ; seuls les comptes de la ligne 152 en sortent ».

### CA6v3-08 — « Ripostes » : terme non défini, de registre adverse
- Gravité : mineur.
- Lignes : 65.
- Défaut : la v3 a renommé la « statistique riposte » de la v1 en « statistique qui étend le domaine » (l. 75, 82), mais garde « Cela vaut aussi pour les ripostes ». Le terme n'est plus défini, et c'est le seul autre mot de registre adverse du texte servi.
- Correction : « Cela vaut aussi pour la statistique qui étend le domaine (champ (e)). »

### CA6v3-09 — Attention d'entropie au plus log k : la moyenne uniforme sur k positions est admise
- Gravité : mineur.
- Lignes : 64.
- Défaut : des poids uniformes sur k positions ont une entropie exactement log k : ils satisfont la contrainte d'attention. Si une action a au plus k positions, la moyenne uniforme sur toutes ses positions est donc à la fois admise (par l'attention) et exclue (phrase suivante). La contrainte ne dit pas non plus si elle vaut pour toute entrée, ni si k dépend de la longueur de l'action.
- Correction : « d'entropie au plus log k pour toute entrée, k fixé indépendamment de la longueur des actions ; la moyenne uniforme sur un ensemble de plus de k positions est exclue ».

### CA6v3-10 — Notation : activations non causales, filtration, histoires hors support, « H complet »
- Gravité : mineur.
- Lignes : 49, 53, 56, 58.
- Défaut : (i) les activations sont « des fonctions déterministes de X » (l. 49) : si h_t dépend d'actions postérieures à t, la statistique n'est pas adaptée et un e-processus n'a pas de sens. (ii) « À tout temps d'arrêt » (l. 56) sans filtration ni borne T. (iii) En variation totale ou en Hellinger, « P_0-presque toute histoire » laisse libres les lois conditionnelles de P_ε sur les histoires que P_0 ne charge pas et que P_ε peut atteindre (avec probabilité au plus ε par pas) ; en Kullback-Leibler, la finitude l'interdit. (iv) « H complet » (l. 58) n'est pas défini.
- Correction : (i) « h_{t,ℓ,p} est une fonction de (a_1, …, a_t) seulement » ; (ii) « à tout temps d'arrêt au plus T de la filtration engendrée par (a_1, …, a_t) » ; (iii) « pour toute histoire », ou « P_0- et P_ε-presque toute » ; (iv) « H(X) = H_Π(X) pour Π l'ensemble de tous les triplets ».

### CA6v3-11 — Juge et fiche : résidus de précision
- Gravité : mineur.
- Lignes : 75, 83-87, 95, 108, 111, 115, 120, 123, 132.
- Défaut : (i) K1 « remplis » : un « sans objet » motivé compte-t-il comme rempli pour (d) et (e) ? Implicite. (ii) (e) peut être « sans objet » alors que la consigne d'axe (l. 75) demande la statistique qui étend le domaine. (iii) La rubrique « Critère de mort » de la fiche n'a pas de contenu défini (l. 114-117 définissent les autres) et se confond avec le « Critère de mort de l'axe » ; K4 la juge. (iv) « Prédiction » ne dit pas de quoi (puissance ? borne ? dans quelle expérience ?). (v) (f) « résultat qui réfute » : réfute quoi ? (vi) (e) : le minorant de puissance doit être uniforme sur la classe D. (vii) Passe 2 : « prouvé faux » (l. 132) ne dit pas qui valide la preuve jointe ; sans cela la notabilité n'est pas binaire.
- Correction : (i) « un “sans objet” motivé compte comme rempli pour (d) et (e) » ; (ii) l'assumer en écrivant « délimitez son domaine de puissance et, si possible, la statistique qui l'étend » ; (iii) « Critère de mort de la fiche : le résultat chiffré de (f) au-delà duquel la statistique de (e), ou la borne de (d), est abandonnée » ; (iv) « Prédiction : la valeur numérique de la puissance ou de la borne attendue dans la première expérience de (f) » ; (v) « résultat qui réfute (d) ou (e) » ; (vi) « minorant uniforme sur la classe » ; (vii) hors texte, « la preuve jointe est validée par le juge tenu à l'écart ; sans validation, le marquage est sans effet ».

### CA6v3-12 — K6 et interface : règle de décision de (g) et forme du compte transmis
- Gravité : mineur.
- Lignes : 88, 125, 155.
- Défaut : (g) donne un estimateur, un intervalle à n donné, une valeur qui confirme et une qui infirme, mais aucune règle qui décide à partir de l'intervalle (zone intermédiaire ?). Le lecteur tenu à l'écart doit pourtant classer chaque (g) « confirmée ou infirmée » (l. 155). Le hors-texte ne dit pas si l'on transmet un nombre (décidées) ou deux (confirmées, infirmées), ni si ces comptes sont croisés avec les cases des listes ; croisés, sur quatre fiches au plus par génération, ils diraient quelle hypothèse cède sur les suites de référence du programme. Le calcul de (g) sur ces suites est aussi une exécution sur les données du programme : sa dépense éventuelle n'est pas devisée.
- Correction : K6 : « … et une règle : confirmée si l'intervalle est du côté de la première valeur, infirmée s'il est du côté de la seconde, indéterminée sinon ». Hors texte : « deux comptes, totaux sur la génération, jamais croisés avec les cases » ; inscrire le calcul de (g) au devis.

### CA6v3-13 — G : conditions (ii) et (iii) trop larges pour un lecteur figé
- Gravité : mineur.
- Lignes : 43-44.
- Défaut : « aucun outil » peut faire écarter une fiche qui cite une bibliothèque de calcul pour (f) ; « contenu d'action » peut faire écarter un exemple formel d'alphabet (a_t ∈ {0, 1}). G écarterait alors des fiches saines, sans que le témoin positif le révèle.
- Correction : (ii) « aucun exemple en langue naturelle d'un texte ou d'une action » ; (iii) « aucune tâche, aucun outil, aucun environnement d'un système qui produit des textes ; les logiciels de calcul de (f) ne sont pas visés ».

### CA6v3-14 — Mesure et exemples de (b)
- Gravité : mineur.
- Lignes : 7-9, 79, 143.
- Défaut : (i) le texte servi fait 8 205 caractères (8 534 octets) ; la mesure prévue avant service doit dire laquelle des deux unités elle emploie. (ii) Les six exemples de (b) sont exactement la liste close des hypothèses classiques (l. 143) : le texte oriente le proposeur vers les cases qui, avec une classe classique, comptent pour la mort de l'axe, sans le lui dire.
- Correction : (i) consigner les deux nombres ; (ii) écrire en (b) « Exemples de forme, déjà connus : … » ; cela ne révèle rien de la liste au-delà de ce qui est déjà servi.

### CA6v3-15 — (f) : échantillon d'étalonnage et échantillon rééchantillonné non séparés
- Gravité : mineur.
- Lignes : 51, 84.
- Défaut : s_α est étalonné sur les n suites de référence, et les déplacements synthétiques de (f) sont obtenus par rééchantillonnage pondéré de ces mêmes suites. Sans séparation, la puissance mesurée est biaisée (le seuil a vu les suites qui servent à le tester).
- Correction : (f) « … les suites servant à l'étalonnage et celles servant aux déplacements synthétiques sont disjointes, avec leurs tailles ».

## Décompte (v3)
- Bloquant : 0.
- Majeur : 7 (CA6v3-01 à CA6v3-07).
- Mineur : 8 (CA6v3-08 à CA6v3-15).
- Constats de la v1 : 15 corrigés, 3 partiellement (CA6-03, CA6-12, CA6-14), 0 non corrigé.
